import nemreader as nr


def output_file():

    from nemreader import output_as_csv
    file_name = 'example.csv'
    output_file = output_as_csv(file_name)


def print_meter_record(file_path, rows=5):
    """ Output readings for specified number of rows to console """
    m = nr.read_nem_file(file_path)
    print('Header:', m.header)
    print('Transactions:', m.transactions)
    for nmi in m.readings:
        for channel in m.readings[nmi]:
            print(nmi, 'Channel', channel)
            for reading in m.readings[nmi][channel][-rows:]:
                print('', reading)


def print_examples():

    print('Example NEM12 - Actual Interval:')
    print('-' * 10)
    print_meter_record('examples/Example_NEM12_actual_interval.csv', 5)

    print('\nExample NEM12 - Substituted Interval:')
    print('-' * 10)
    print_meter_record('examples/Example_NEM12_substituted_interval.csv', 5)

    print('\nExample NEM12 - Multiple Quality Methods:')
    print('-' * 10)
    print_meter_record('examples/Example_NEM12_multiple_quality.csv', 5)

    print('\nExample NEM12 - Multiple Meters:')
    print('-' * 10)
    print_meter_record('examples/Example_NEM12_multiple_meters.csv', 5)

    print('\nExample NEM13 - Actual Read:')
    print('-' * 10)
    print_meter_record('examples/Example_NEM13_consumption_data.csv', 5)

    print('\nExample NEM13 - Forward Estimates:')
    print('-' * 10)
    print_meter_record('examples/Example_NEM13_forward_estimate.csv', 5)

    print('\nReal NEM13 Example:')
    print('-' * 10)
    print_meter_record('examples/NEM13#DATA_14121801#WBAYM#3044076134.V01', 5)

    print('\nReal NEM12 Example:')
    print('-' * 10)
    print_meter_record('examples/NEM12#DATA_16081001#WBAYM#3044076134.V01', 5)

    print('\nZipped NEM12 Example:')
    print('-' * 10)
    print_meter_record('examples/NEM12#NEM1201005Scenario1#GLOBALM#NEMMCO.ZIP',
                       5)

if __name__ == '__main__':
    output_file()
    #print_examples()