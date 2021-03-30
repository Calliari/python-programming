#! /usr/bin/env python3.7 

# references
# https://github.com/linuxacademy/content-python-for-sys-admins

# https://docs.python.org/3/library/argparse.html?highlight=parser --> (search for ArgumentParser objects, add_argument)
import argparse

# crating a parser Object from a ArgumentParser() class - Construct the argument parser
parser = argparse.ArgumentParser()

# using the parser Object with 'description' option
parser = argparse.ArgumentParser(description="""
Template for creating python CLI scripts
""")

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

parser.add_argument('--version', '-v', action='version', version='%(prog)s 1.0',
                    help="version of this script")


# this call the '-h' flag
# args = vars(parser.parse_args(['-h']))


def example_parser_argument_call():
    print('\n $ python3.7 python_script_sys_admin_template -a "test"\n')


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



try:
    # taking all argumente frim this Object 'args'
    # convert the 'Namespace' into var 'dict'
    args = vars(parser.parse_args())
    check_parser_argument(args)
except argparse.ArgumentError:
     print('Catching an argumentError')
     print(parser.exit())


# How to run this script example
example_parser_argument_call()


# Printing the arguments
