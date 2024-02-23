from DATA import DATA
from utils import *
from config import *
def getCliValues():
    for key, value in cli(settings(help)).items():
        the[key] = value

def calculateCentroid(node):
    if 'left' not in node and 'right' not in node:
        value = node['data'].mid().cells
        centroid = sum(value)/len(value)
        return centroid
    else:
        left = calculateCentroid(node['left'])
        right = calculateCentroid(node['right'])
        return {'left': left, 'right': right}

def printLeafCentroids(node):
    if 'left' not in node and 'right' not in node:
        print(node)
    else:
        printLeafCentroids(node['left'])
        printLeafCentroids(node['right'])



def doubletap():
    data = DATA("../data/auto93.csv")
    print("---------PART1----------")
    r1 = data.rows[0]
    rows = r1.neighbors(data)

    for index, row in enumerate(rows):
        if index%30 == 0:
            print(index+1,o(row.cells),rounding(row.dist(r1,data)))

    print("\n\n---------PART2----------")
    att = 1
    a, b, distance = data.farapart(data)
    while distance > 0.95 and att < 100:
        a, b, distance = data.farapart(data)
        att += 1

    print(f'far1: {o(a.cells)},\nfar2: {o(b.cells)}')
    print(f'distance = {distance}')

    cluster_result = data.cluster(data.rows)
    #print(cluster_result)
    leaf_centroids = calculateCentroid(cluster_result)
    #printLeafCentroids(leaf_centroids) 


if __name__ == '__main__':
    getCliValues()
    doubletap()
