from sys import float_repr_style
from os import getcwd
import os
import builtins


current_directory = getcwd()
sample =3
sum = 10

if True:
    print(current_directory)
    print(type(current_directory))
    print("My sister cpu count is",current_directory)
    print("My system cpu count is",current_directory, "with",sample,"example")
    print("My directory path is {} and the count is {} ".format(current_directory,sample))
    print("My directory path is {} and the count is {} and the total is {} ".format(current_directory,sample,sum))
    print("My directory path is {} ".format(current_directory,sample,sum))
    print("My directory path is: {current_directory} and the count is: {sample}")
    print(dir(builtins))



