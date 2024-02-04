from DATA import DATA
from config import *

def print_task1(data):
    class_counts = {}
    total_rows = len(data.rows)

    for row in data.rows:
        class_label = row.cells[data.cols.all[-1].at]
        class_counts[class_label] = class_counts.get(class_label, 0) + 1

    print("     Class         \t    Percentage   ")
    print("------------------ \t ----------------")
    for class_label, count in class_counts.items():
        percentage = (count / total_rows) * 100
        print(f"{class_label.ljust(25)} \t {percentage:.2f}%")

def bayes(path):
    wme = {'acc': 0, 'datas': {}, 'tries': 0, 'n': 0}
    data = DATA(path)
    for row in data.rows:
        learn(data, row, wme)
    return wme['acc'] / wme['tries']

def learn(data, row, my):
    my["n"] += 1
    kl = row.cells[data.cols.klass.at]

    if my["n"] > 10:
        my["tries"] += 1
        my["acc"] += 1 if kl == row.likes(my["datas"]) else 0

    my["datas"][kl] = my["datas"].get(kl, DATA(data.cols.names))
    my["datas"][kl].add(row)


if __name__ == "__main__":
    data = DATA('../data/diabetes.csv')
    print("******************************")
    print("\n\nTASK 1")
    print("-----------------")
    print("diabetes dataset")
    print_task1(data)
    data = DATA("../data/soybean.csv")
    print("-----------------")
    print('soyabeans dataset')
    print_task1(data)

    print("******************************")
    print("\n\nTASK 3")
    accuracyFromDiabetes = bayes('../data/diabetes.csv')
    print("diabetes accuracy",accuracyFromDiabetes)

    print("******************************")
    print("\n\nTASK 4")
    path = '../data/soybean.csv'

    for k in range(4):
        for m in range(1,4):
            the['k'] = k
            the['m'] = m
            accuracyFromSoya = bayes(path)
            print(f"for the values of k {k} and values m {m}, accuracy is {accuracyFromSoya}")
