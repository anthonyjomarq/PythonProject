import string
from typing import Dict, List, Any

# city_data is a variable of type dictionary, where each element is a key : value pair,
# the key is an integer representing the line number in the text file; the value of each key
# is a list containing the values read from the text file. Note that when building the dictionary some values
# have to be converted into integer.
import cohstats.stats

input_data = {}

# city_data is a variable of type dictionary, where each element is a key : value pair,
# the key is one of the 13 metadata; the value of each key is a list containing the
# values read from the text file. Note that when building the dictionary some values
# have to be converted into integer.
city_data = {}

# city_counts is a variable of type dictionary (a nested dictionary), where the key is
# one of 10 metadata (day_of_week, hour_of_day, neighborhood, district, division,
# serv_type, queue, wait, days, origin). The value is another dictionary;
# where the key is a unique information from the dataset for that metadata and
# its corresponding value is a count of how many times, that information appears
# in the dataset.
city_counts = {}

# city_stats is a variable of type dictionary (a nested dictionary), where the key is
# one of only 4 metadata: 'day_of_week', 'hour_of_day', 'wait', 'days'; the value is
# another dictionary; where the keys are: 'avg', 'stdev', 'var', and their
# corresponding values will be computed by invoking functions defined in the stats module
city_stats = {}


# reads from a text file in disk and stores its content in a dictionary
# DON'T MODIFY THIS FUNCTION
def read_file(file: str) -> Dict[int, List[Any]]:
    list_of_lines = {}

    print('input file is: ' + file)

    try:
        with open('data/' + file) as f:
            count = 1
            for line in f:
                if count > 1:
                    values_in_line = line.replace('\n', '').split('|')
                    # replaces the third element in the list with its corresponding
                    # value as integer
                    values_in_line[2] = int(values_in_line[2])
                    list_of_lines[count - 1] = values_in_line
                count += 1
    except FileNotFoundError:
        print(f"Error: File 'data/{file}' not found.")
        return {}
    except Exception as e:
        print(f"Error reading file: {e}")
        return {}

    print('read a total of ', count, ' lines from file: ', file)
    # returns a list with  all lines read from the input file
    return list_of_lines


# invoke this function in your test script to build the city_data dictionary
# this function has to be invoked only once in your entire code
def builds_city_data(data: Dict[int, List[Any]]) -> Dict[str, List[Any]]:
    data_processed = {}
    keys = [
        'date',
        'time',
        'day_of_week',
        'hour_of_day',
        'neighborhood',
        'key_map',
        'district',
        'division',
        'serv_type',
        'queue',
        'wait',
        'days',
        'origin',
    ]
    for key in keys:
        data_processed[key] = []
    for row_number, call_info in data.items():
        call_info[3] = int(call_info[3])
        call_info[10] = int(call_info[10])
        call_info[11] = int(call_info[11])
        for i in range(len(keys)):
            data_processed[keys[i]].append(call_info[i])
    return data_processed


# invoke this function in your test script to build the city_counts dictionary
# this function has to be invoked only once in your entire code
def builds_city_counts(data: Dict[str, List[Any]]) -> Dict[str, Dict[Any, int]]:
    data_processed = {}
    del data['date']
    del data['time']
    del data['key_map']
    # row_number is the key and call_info is the value
    for row_number, call_info in data.items():
        duplicate_dict = {}
        for i in call_info:
            duplicate_dict[i] = call_info.count(i)
            data_processed[row_number] = duplicate_dict
    return data_processed


# invoke this function in your test script to build the city_stats dictionary
# this function has to be invoked only once in your entire code
def builds_city_stats(data: Dict[int, List[Any]]) -> Dict[str, Dict[str, float]]:
    data_processed = {}
    print('Building city stats...\n')
    citydata = builds_city_data(data)
    citycounts = builds_city_counts(citydata)
    del citycounts['neighborhood']
    del citycounts['district']
    del citycounts['division']
    del citycounts['serv_type']
    del citycounts['queue']
    del citycounts['origin']
    data_processed['day_of_week'] = {"avg": cohstats.stats.compute_average(citycounts, 'day_of_week', "", ""),
                                     "stdev": cohstats.stats.compute_stdev(citycounts, 'day_of_week', "", ""),
                                     "var": cohstats.stats.variance(citycounts, 'day_of_week')}
    data_processed['hour_of_day'] = {"avg": cohstats.stats.compute_average(citycounts, 'hour_of_day', "", ""),
                                     "stdev": cohstats.stats.compute_stdev(citycounts, 'hour_of_day', "", ""),
                                     "var": cohstats.stats.variance(citycounts, 'hour_of_day')}
    data_processed['wait'] = {"avg": cohstats.stats.compute_average(citycounts, 'wait', "", ""),
                              "stdev": cohstats.stats.compute_stdev(citycounts, 'wait', "", ""),
                              "var": cohstats.stats.variance(citycounts, 'wait')}
    data_processed['days'] = {"avg": cohstats.stats.compute_average(citycounts, 'days', "", ""),
                              "stdev": cohstats.stats.compute_stdev(citycounts, 'days', "", ""),
                              "var": cohstats.stats.variance(citycounts, 'days')}
    return data_processed
