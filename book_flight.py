import argparse
import requests
import urllib

parser = argparse.ArgumentParser(description='Kiwi.com booking flight script')
parser.add_argument('--date', required=True,
                    help='specific date (format: YYYY-MM-DD)')
parser.add_argument('--from', required=True, dest='flyFrom',
                    help='departure airport (IATA code)')
parser.add_argument('--to', required=True,
                    help='destination airport (IATA code)')
parser.add_argument('--one-way', action='store_true', default=True,
                    help='a flight is only to location (default:True)')
parser.add_argument('--return', type=int, dest='nights_num',
                    help='a flight with passenger staying for N nights in destination')
parser.add_argument('--cheapest', default=True, action='store_true',
                    help='booking the cheapest flight (default:True')
parser.add_argument('--fastest', default=False, action='store_true',
                    help='booking the fastest flight')
parser.add_argument('--bags', type=int, dest='bags_count', default=0,
                    help='booking the fastest flight')

args = parser.parse_args()


def search_for_flights():
    """search for available flights with requested criteria provided in args
    :return: booking token and currency
    """
    date = args.date[8:10] + '/' + args.date[5:7] + '/' + args.date[0:4]
    date_encoded = urllib.parse.quote_plus(date)
    if args.fastest:
        filter_str = '&sort=duration'
    else:
        filter_str = ''
    if args.nights_num:
        filter_str += ('&typeFlight=round&daysInDestinationFrom=' + str(args.nights_num) +
                       '&daysInDestinationTo=' + str(args.nights_num))
    else:
        filter_str += '&typeFlight=oneway'
    string_request = ('https://api.skypicker.com/flights?flyFrom=' + args.flyFrom + '&to=' + args.to +
                      '&dateFrom=' + date_encoded + 
                      '&dateTo=' + date_encoded +
                      '&partner=picky&partner_market=us' + filter_str)
    data = requests.get(string_request)

    return data.json()['data'][0]['booking_token'], data.json()['currency']


def send_booking_request(tok, curr):
    """send booking request with specified token and currency
    :param tok: booking token
    :param curr: currency
    :return: pnr of booking
    """
    d = requests.post("http://128.199.48.38:8080/booking", json={
        "currency": curr,
        "booking_token": tok,
        "bags": args.bags_count,
        "passengers": {
            "lastName": "Test",
            "firstName": "Tester",
            "title": "Mr",
            "email": "test@gmail.com",
            "documentID": "12345678",
            "birthday": "1995-12-12"
        }
    })
    return d.json()['pnr']


if __name__ == '__main__':
    token, currency = search_for_flights()
    pnr = send_booking_request(token, currency)
    print('PNR: ' + pnr)
