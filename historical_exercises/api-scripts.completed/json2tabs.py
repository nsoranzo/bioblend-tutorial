#!/usr/bin/env python
"""
Utility for reading json from stdin, tabs, and pick keys.
"""

import sys
import json
import argparse
import output

# -----------------------------------------------------------------------------
argparser = argparse.ArgumentParser( description='filter json from stdin and convert to TSV' )
argparser.add_argument( '-keys', default='', help='only show the given keys from the json object' )
argparser.add_argument( '--json', default=False, action='store_true', help='do not convert to TSV, output more json' )
args = argparser.parse_args()
args.keys = args.keys.split( ',' ) if args.keys else []


# -----------------------------------------------------------------------------
def read_stdin():
    returned = ''.join( list( line for line in sys.stdin ) )
    return returned

def pick( d, keys, include_blanks=True ):
    """
    Get the attributes named in keys from dict d. If include_blanks, include
    attributes missing from d with an empty string as the value.
    """
    if not keys:
        return d
    returned = {}
    for key in keys:
        if key in d:
            returned[ key ] = d[ key ]
        elif include_blanks:
            returned[ key ] = ''
    return returned

def dict_to_tabs( d, order=None ):
    """
    Return tab-separated values for all values in d and ordered
    by the keys in order (if given).
    """
    order = order or d.keys()
    return '\t'.join([ str( d[ key ] ) for key in order ])

def output_dict( d, keys, include_blanks=True, as_json=False ):
    """
    Pick and tabify (or pretty print as json if as_json) values in d.
    """
    picked = pick( d, keys, include_blanks=include_blanks )
    if not as_json:
        return dict_to_tabs( picked, keys )
    return output.pformat_as_json( picked )

def output_list( l, keys, include_blanks=True, as_json=False ):
    #TODO: not quite correct - as json will not be an array
    returned = []
    for elem in l:
        returned.append( output_dict( elem, keys, include_blanks=include_blanks, as_json=as_json ) )
    return '\n'.join( returned )


# -----------------------------------------------------------------------------
if __name__ == '__main__':
    json_str = read_stdin()
    data = json.loads( json_str )
    if isinstance( data, list ):
        print output_list( data, args.keys, as_json=args.json )
    elif isinstance( data, dict ):
        print output_dict( data, args.keys, as_json=args.json )
    else:
        raise TypeError( 'Unhandled json type: %s, %s' %( type( data ), data ) )
