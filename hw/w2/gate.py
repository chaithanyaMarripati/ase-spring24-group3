"""
OPTIONS:
  -f --file   csv file containing data        = '../data/auto93.csv'
  -h --help   show help                       = False
"""
import sys
from src.DATA import DATA
for arg in sys.argv:
    if arg in ["-h","--help"]:
        print(__doc__)
        exit(0)
data= DATA("../data/auto93.csv")
print(data.stats())
