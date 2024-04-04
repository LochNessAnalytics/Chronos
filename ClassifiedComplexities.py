import copy

import tensorflow as tf


class BigOhN1:

  def __init__(self, arg_0, kwarg_0):
    self.arg_0 = arg_0
    self.kwarg_0 = kwarg_0

    self.attr_49 = None
    self.attr_50 = None
    self.attr_51 = None

  def sorter(self, arg_0, kwarg_0):
    """
      O(d*n) sorting algorithm for any list
        n := number of list elements
        d := number of digits

      similar to bin sort without any conditions
        actual sorting block contributes O(n) time complexity

      multi-stage to identify active sections of 2^d abstract space (unrealized)
        multi-stage contributes a constant time complexity
        determining the number of stages is dependent on space constraints or whatever else
      
      TensorFlow vectorized_map function enables parallel processing
        
    """
    pass

  def min_diff(self, arg_0, kwarg_0):
    """
    O(n) minimum difference between any two sequential elements in a sorted list
      n := number of list elements

    simple algorithm with approximate time complexity of T(n) = 3*n
    creates two lists (n-1) in length

      first resulting list is a copy of the list without the first element with another copy of the list

    :param arg_0:
    :param kwarg_0:
    :return:
    """
    original_list = arg_0
    list_length = len(original_list)

    copy_list_0 = copy.deepcopy(original_list)
    copy_list_1 = copy.deepcopy(original_list)

    copy_list_0.pop()
    copy_list_1.pop(0)

    diff_list_0 = copy_list_0 - copy_list_1
    min_diff =  min(abs(diff_list_0))

    return min_diff