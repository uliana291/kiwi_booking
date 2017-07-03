# kiwi_booking

List of possible invocations:

./book_flight.py --date 2017-10-13 --from BCN --to DUB --one-way
./book_flight.py --date 2017-10-13 --from LHR --to DXB --return 5
./book_flight.py --date 2017-10-13 --from NRT --to SYD --cheapest
./book_flight.py --date 2017-10-13 --from CPH --to MIA --shortest

where --one-way (make this the default option) indicates need of flight only to location and --return 5 should book flight with passenger staying 5 nights in destination,

--cheapest (default) will book the cheapest flight and --shortest will work similarly

The program will output a PNR number which serves as confirmation of booking

The --from and --to parameters only need to support airport IATA codes
