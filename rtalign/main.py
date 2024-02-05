#!/usr/bin/env python3
from __namespace__ import *
from argparse import ArgumentParser
from sys import argv
from rich import print as rprint
from rich.traceback import install
install(show_locals=True)

parser: ArgumentParser = ArgumentParser(
    description=DESCRIPTION, add_help=True)
subparsers = parser.add_subparsers(
    help='Available subcommands', dest="subcommands")

parser._positionals.title = 'Subcommands'
parser._optionals.title = 'Global Arguments'

## Subparser for command1 ##

parser_1: ArgumentParser = subparsers.add_parser(
    'command1',
    help=""
)
parser_1.add_argument("file", type=str, help="Path to a file")

## Subparser for command1 ##

parser_2: ArgumentParser = subparsers.add_parser(
    'command2',
    help=""
)
parser_2.add_argument("file", type=str, help="Path to a file")

#######################################
args = parser.parse_args()
#######################################


def main() -> None:
    "Main call for subprograms"
    if len(argv) == 1:
        rprint(
            "[dark_orange]You need to provide a command and its arguments for the program to work.\n"
            "Try to use -h or --help to get list of available commands."
        )
        exit(1)
    match args.subcommands:
        case 'command1':
            # Do some stuff here
            print("Command1")
        case 'command2':
            # Do some stuff here
            print("Command2")
        case _:
            rprint(
                "[dark_orange]Unknown command. Please use the help to see available commands.")
            exit(1)
