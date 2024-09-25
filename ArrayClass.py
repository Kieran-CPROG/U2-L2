#Kieran Uptagrafft
#Making a bigger and better list
#9/24/24

import ctypes

class DynamicArray:
  def __init__(self):
    self.__n = 0
    self.__capacity = 1
    self.__A = self.__make_array(self.__capacity)

  def __str__(self):
    if self.__n == 0:
        return "[]"

    out = '['
    for i, element in enumerate(self.__A):
        try:
            out += str(element) + ', '
            temp = self.__A[i+1]
        except:
            break
            
    return out[:-2] + ']'

  def get_cap(self):
    #Returns the capacity of the array
    
    return self.__capacity

  def __make_array(self, c):
    """return new array with capacity c"""

    return (c * ctypes.py_object)()

  def __getitem__(self, k):
    """return element at index"""
    if k <= 0 or k >= self.__n:
        raise IndexError("invalid index")
    
    return self.__A[k]
    
  def __resize(self):
    #Makes a temp array with double the capacity.
    #Add everything from the existing array. 
    #Make the existing array equal temp array.

    self.__capacity += self.__capacity
    temp = self.__make_array(self.__capacity)
    for x in range(self.__n):
      try:
        temp[x] = self.__A[x]
      except:
        pass

    self.__A = temp

  def append(self, element):
    #Adds a item to the end of a array.
    if self.__capacity == self.__n:
      self.__resize()
         
    self.__A[self.__n] = element        
    self.__n += 1
  def __len__(self):
    #Returns the number of elements in a array.

    return self.__n