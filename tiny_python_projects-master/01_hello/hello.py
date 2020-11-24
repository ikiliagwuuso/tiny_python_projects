#!/usr/bin/env python3
"""
Author : rhymeinstein <ikiliagwu.usothegenius@gmail.com>
Date   : 2020-10-29
Purpose: Choose the article
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Choose the article',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='A position')


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.word
    article = 'a'

    if word[0].lower() in "aeiou":
      article = 'an'
    
    print('Ahoy, Captain, '+article+ ' ' + word + ' off the larboard bow!')

# --------------------------------------------------
if __name__ == '__main__':
    main()
