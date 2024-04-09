from pathlib import Path
import ast,sys,math,random,re
from config import *
import math
import random

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


def modifyValues(t, n=None, u=None):
    if isinstance(t, (int, float)):
        return str(rounding(t, n))
    if not isinstance(t, dict):
        return str(t)
    if u is None:
        u = []
    for k in t.keys():
        if str(k)[0] != "_":
            if len(t) > 0:
                u.append(o(t[k], n))
            else:
                u.append(f"{o(k, n)}: {o(t[k], n)}")
    return "{" + ", ".join(u) + "}"

def rounding(n, ndecs=None):
    if not isinstance(n, (int, float)):
        return n
    if math.floor(n) == n:
        return n
    mult = 10**(ndecs or 2)
    return math.floor(n * mult + 0.5) / mult

def o(t, n=None, u=None):
    if isinstance(t, (int, float)):
        return str(rnd(t, n))
    if not isinstance(t, dict):
        return str(t)
    if u is None:
        u = []
    for k in t.keys():
        if str(k)[0] != "_":
            if len(t) > 0:
                u.append(o(t[k], n))
            else:
                u.append(f"{o(k, n)}: {o(t[k], n)}")
    return "{" + ", ".join(u) + "}"

def any(t):
    return t[random.randint(0, len(t) - 1)]

def cos(a,b,c):
    den = 1 if c == 0 else 2*c
    x1 = (a**2 + c**2 - b**2) / den
    return x1

def many(t,n):
    u=[]
    for _ in range(1,n+1):
        u.append(any(t))
    return u

def settings(s):
    pat = r"[-][-]([\S]+)[^\n]+= ([\S]+)"
    return dict(re.findall(pat, s))

def cli(options):
    args = sys.argv[1:]
    for k, v in options.items():
        for n, x in enumerate(args):
            if x == '-' + k[0] or x == '--' + k:
                v = 'true' if v == 'false' else 'false' if v == 'true' else args[n + 1]
        options[k] = coerce(v)
    return options

def rnd(n, ndecs=None):
    if type(n) != float:
        return n

    if math.floor(n) == n:
        return n

    mult = 10**(ndecs or 2)
    return math.floor(n * mult + 0.5) / mult

def powerset(s):
        t = [[]]
        for i in range(len(s)):
            for j in range(len(t)):
                t.append([s[i]] + t[j])
        return t

def shuffle(t):
    u = list(t)
    for i in range(len(u) -1, 1, -1):
        j=random.randint(0, i)
        u[i], u[j] = u[j], u[i]
    return u

def entropy(t):
    n = sum(t.values())
    e = 0
    for v in t.values():
        e -= (v / n) * math.log2(v / n)
    return e, n

def score(t, goal, LIKE, HATE):
    like, hate, tiny = 0, 0, 1e-30
    for klass, n in t.items():
        if klass == goal:
            like += n
        else:
            hate += n
    if like == 0 and hate == 0:
        return 0  # Return 0 if both like and hate are zero
    like, hate = like / (LIKE + tiny), hate / (HATE + tiny)
    return 0 if hate > like else (like ** the.get("Support")) / (like + hate)
