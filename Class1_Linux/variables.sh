#!/bin/bash

# # 1
# a=14
# b=asdf
# c=123asdf

# echo $a
# echo $b
# echo $c
# echo " a=$a  b=$b c=$c"
# echo ' a=$a  b=$b c=$c'

# 2 -> user input
# echo "What is your name?"
# read name
# echo "Hello, $name!"


# 3 -> command line arguments
# cmd + / -> comment/uncomment
# cmd + [ -> indent
# cmd + ] -> unindent

# usage -> ./script.sh arg1 arg2 arg3 ...
echo "Script name: $0"
echo "First argument: $1"
echo "Second argument: $2"
echo "All arguments: $@"
echo "Number of arguments: $#"
echo "Process ID: $$"
echo "Last command exit status: $?" # exit coode 0 -? success, 1 - fail 
ls -lkkkkkk
echo "Last command exit status: $?"