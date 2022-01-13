#! /usr/bin/env python3.7 

# references
# https://github.com/linuxacademy/content-python-for-sys-admins


__author__ = "author name"
__copyright__ = "Copyright 2022, The test-scripr Project"
__credits__ = ["credits to be given to"]
__version__ = '1.0'
__maintainer__ = "devOps team"
__status__ = "non-production"

import os

# https://docs.python.org/3/library/argparse.html?highlight=parser --> (search for ArgumentParser objects, add_argument)
import argparse

# variable version for the program
program_version = __version__ 


# creating a parser Object from a ArgumentParser() class - Construct the argument parser
parser = argparse.ArgumentParser()

# using the parser Object with 'description' option
parser = argparse.ArgumentParser(description="""
Automated test-script
version: %s,
status:  %s,
maintainer: %s
""" %(__version__,__status__,__maintainer__))

# Add the arguments to the parser
parser.add_argument("-a", "--first_arg", required=False,
                    help="Pass the first arg")

parser.add_argument("-b", "--seccond_arg", required=False,
                    help="Pass the second arg")

parser.add_argument('-A', dest='fourth_arg', required=False, 
                    help='Fourth arg as a short flag - A')

parser.add_argument('-s', action='store', dest='simple_value',
                    help='Store a simple value')

parser.add_argument('--verbose', action='store_true',
                    help='verbose flag' )

parser.add_argument('--version', '-v', action='version', version='%(prog)s version ' + str(program_version),
                    help='version of this %(prog)s program')


# this call the '-h' flag
# args = vars(parser.parse_args(['-h']))


def example_parser_argument_call():
    print('\n $ python3.7 python_script_sys_admin_template -a "test"\n')

# Get the 'parser_dict' argument from the 'try-cactch & except' block
def check_parser_argument(parser_dict):
        if parser_dict['first_arg'] == None:
            # print(parser_dict)
            # parser.print_help()
            print("\n...ERR You are passing an 'None' required argument\n")
            parser.exit(1)
        elif not parser_dict['first_arg']:
            print("\n...ERR You are passing an 'empty' required argument\n")
            parser.exit(1)
        elif parser_dict['first_arg'].isspace():
            # parser.print_help()
            print("\n...ERR You are passing an 'blank' required argument\n")
            parser.exit(1)

# Keep the 'try-cactch & except' block small and tidy
try:
    # taking all argumente frim this Object 'args'
    # convert the 'Namespace' into var which became 'dict'
    args = vars(parser.parse_args())
    
    # Calling a function 'check_parser_argument' passing the dictionary 'args' - check with 'print(args)'
    check_parser_argument(args)
except argparse.ArgumentError:
     print('Catching an argumentError')
     print(parser.exit())


# How to run this script example
example_parser_argument_call()


# Printing the arguments

# call the "__name__"
# if __name__ == "__main__":
#    main(sys.argv[1:])
