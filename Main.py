import argparse

import sys

def calc(args):

    if args.o == 'add':

        return args.x + args.y

    elif args.o == 'mul':

        return args.x * args.y

args.o == 'sub':

        return args.x - args.y

    elif args.o == 'div':

        return args.x / args.y

    else:

        return "
