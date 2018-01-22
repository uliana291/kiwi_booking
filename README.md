# kiwi_booking

List of possible invocations:

- `./book_flight.py --date 2017-10-13 --from BCN --to DUB --one-way`

- `./book_flight.py --date 2017-10-13 --from LHR --to DXB --return 5`
- `./book_flight.py --date 2017-10-13 --from NRT --to SYD --cheapest --bags 2`
- `./book_flight.py --date 2017-10-13 --from CPH --to MIA --fastest`

where `--one-way` (default) indicates need of flight only to location and `--return 5` book flight with passenger staying 5 nights in destination,

`--cheapest` (default) will book the cheapest flight and `--shortest` will work similarly

`--bags 2` will book a flight with 2 bags

The program will output a PNR number which serves as confirmation of booking

The `--from` and `--to` parameters support airport IATA codes
