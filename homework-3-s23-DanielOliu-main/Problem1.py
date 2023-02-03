import numpy as np
import matplotlib.pyplot as plt


def norm_histogram(hist):
    """
    takes a list of counts and converts to a list of probabilities, which is an output
    with a sum of the counts, i.e. the number of samples(int)
    :param hist: a numpy ndarray object
    :return: a tuple that contains a list and a int, i.e. ([...], int)
    """
    samples = sum(hist)

    prob = {}

    a = np.array(hist)

    probability = a / samples

    k = 0
    while k < len(hist):
    
        prob[hist[k]] = (hist[k], probability[k]) 
        k += 1

    print(prob)


def compute_j(histo, width):
    """
    takes list of counts, uses norm_histogram function to output the list of probabilities and the number of samples, 
    then calculates compute_j for one bin width (reference: histogram.pdf page19)
    :param histo: list
    :param width: float
    :return: float
    """
    # please delete the "pass" below and your code starts here...
    
    m = sum(histo)
    output = norm_histogram(histo)
    
    for i in histo: 
    
        j = (2/((m-1) * width)) - ((m+1)/((m-1) * width)) * output[i]
    
    return(j)



def sweep_n(data, minimum, maximum, min_bins, max_bins):
    """
    find the optimal bin
    calculate compute_j for a full sweep [min_bins to max_bins]
    please make sure max_bins is included in your sweep
    
    The variable "data" is the raw data that still needs to be "processed"
    with matplotlib.pyplot.hist to output the histogram

    You need to utilize the variables (data, minimum, maximum, min_bins, max_bins) 
    in sweep_n functions to give values to (x, bins, range) in the function matplotlib.pyplot.hist
    Other input variables of matplotlib.pyplot.hist can be set as default value.
    
    :param data: list
    :param minimum: int
    :param maximum: int
    :param min_bins: int
    :param max_bins: int
    :return: list
    """
    # please delete the "pass" below and your code starts here...
    range = max_bins - min_bins 
    data_processed = plt.hist(data)
    number_of_bins = compute_j(range, data_processed)

    k = 0
    
    while k < len(number_of_bins):
        return(number_of_bins[k])



def help_find_small(l): #a helper function to be used to sort through the list and find the small numbers and their indexes

    smallest_num = min(l)
    index_smallest_num = l.index(smallest_num)

    l.remove(smallest_num) #removes the smallest mnumber out of the list so that the min function can be used again

    second_small = min(l)
    index_second_small = l.index(second_small)

    return(smallest_num, second_small, index_smallest_num, index_second_small)


def find_min(l):
    """
    takes a list of numbers and returns a tuple that contains the value and index of the two smallest numbers in that list and their mean.
    i.e. 
    ([index_of_smallest_number, index_of_second_smallest_number],[value_of_smallest_number, value_of_second_smallest_number], mean)}
    
    For example:
        If the input list (l) is [14,27,15,49,23,41,147]
        Then it should return ([0,2], [14,15], 14.5)

    :param l: list
    :return: tuple
    """
    # please delete the "pass" below and your code starts here...
    list_of_small_nums = help_find_small(l)

    mean = (list_of_small_nums[0] + list_of_small_nums[1]) / 2

    tuple_l = {f'[{list_of_small_nums[2]}, {list_of_small_nums[3]}]', f'[{list_of_small_nums[0]}, {list_of_small_nums[1]}]', mean}
    return(tuple_l)



if __name__ == "__main__":
    data = np.loadtxt("input.txt")  # reads data from input.txt
    lo = min(data)
    hi = max(data)
    bin_l = 1
    bin_h = 100
    js = sweep_n(data, lo, hi, bin_l, bin_h)
    """
    the values bin_l and bin_h represent the lower and higher bound of the range of bins.
    They will change when we test your code and you should be mindful of that.
    """
    print(find_min(js))
