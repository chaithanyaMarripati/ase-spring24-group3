from pathlib import Path
import ast


def coerce(x):
    try:
        return ast.literal_eval(x)
    except Exception:
        return x.strip()


def csv(sFilename, fun):
    fileDescriptor = Path(sFilename)
    if fileDescriptor.exists() == False:
        raise FileNotFoundError()
    if fileDescriptor.suffix != ".csv":
        raise Exception("data file should be csv")
    with open(fileDescriptor.absolute(), "r", encoding="utf-8") as file:
        for line in file:
            row = list(map(coerce, line.strip().split(",")))
            fun(row)
