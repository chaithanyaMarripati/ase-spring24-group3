"""
OPTIONS:
  -f --file   csv file containing data        = '../data/auto93.csv'
  -h --help   show help                       = False
"""


import sys

for arg in sys.argv:
    if arg in ["-h","--help"]:
        print(__doc__)
        exit(0)

print("Need to implement stuff")
