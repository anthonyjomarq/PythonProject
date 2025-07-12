import cohstats.parser as parser
import math
from typing import Dict, List, Any, Union

def data_list(data: Dict[str, Dict[Any, int]]) -> Dict[str, List[Any]]:
    data_processed = {}
    for row_number, call_info in data.items():
        data_processed[row_number] = []
        keys = [row_number]
        for key in call_info:
            i = 0
            while i < call_info[key]:
                data_processed[keys[0]].append(key)
                i += 1
    return data_processed


def variance(data: Dict[str, Dict[Any, int]], metadata: str) -> float:
    data_processed = data_list(data)
    count = len(data_processed[metadata])
    mean = sum(data_processed[metadata]) / count
    deviations = [(x - mean) ** 2 for x in data_processed[metadata]]
    result = sum(deviations) / count
    return result


#################
# Given a metadata and column as arguments, computes the average of the values for a category
# Returns: the average as a float number
#################
def compute_average(data: Dict[str, List[Any]], metadata: str, column: str, category: str) -> float:
    if column == "":
        data_processed = data_list(data)
        total = sum(data_processed[metadata])
        count = len(data_processed[metadata])
        return total/count
    else:
        new_list = []
        last_list = []
        i = 0
        for i in range(len(data[metadata])):
            if data[column][i] == category:
                new_list.append(i)
        for x in new_list:
            last_list.append(data[metadata][x])
        total = sum(last_list)
        count = len(last_list)
        return total / count


#################
# Given a metadata and column as arguments, computes the standard deviation of the values for a category
# Returns: the standard deviation as a float number
#################

def compute_stdev(data: Dict[str, List[Any]], metadata: str, column: str, category: str) -> float:
    # write here your code for this function
    if column == "":
        var = variance(data, metadata)
        result = math.sqrt(var)
        return result
    else:
        new_list = []
        last_list = []
        i = 0
        for i in range(len(data[metadata])):
            if data[column][i] == category:
                new_list.append(i)
        for x in new_list:
            last_list.append(data[metadata][x])
        total = sum(last_list)
        count = len(last_list)
        mean = total / count
        deviations = [(x - mean) ** 2 for x in last_list]
        var = sum(deviations) / count
        result = math.sqrt(var)
        return result


#################
# Given a a metadata and a number (float) as arguments, finds all entries in
# column with values greater than the value passed to the parameter limit
# Returns: A list of strings from the column whose values are greater than limit
#################
def greater_than(data: Dict[str, List[Any]], metadata: str, column: str, limit: Union[int, float]) -> List[Any]:
    # write here your code for this function
    result = []
    i = 0
    for x in data[metadata]:
        if x > limit:
            result.append(data[column][i])
        i += 1
    return result


#################
# Given a a metadata and a number (float) as arguments, finds all entries in
# column with values greater than the value passed to the parameter limit
# Returns: A list of strings from the column whose values are less than limit
#################
def less_than(data: Dict[str, List[Any]], metadata: str, column: str, limit: Union[int, float]) -> List[Any]:
    # write here your code for this function
    result = []
    i = 0
    for x in data[metadata]:
        if x < limit:
            result.append(data[column][i])
        i += 1
    return result
