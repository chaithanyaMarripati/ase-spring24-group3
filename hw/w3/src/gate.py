from DATA import DATA

def learn(data, row, my):
    my['n'] += 1
    kl = row['cells'][data['cols']['klass']['at']]

    if my['n'] > 10:
        my['tries'] += 1
        my['acc'] += 1 if kl == row.likes(my['datas']) else 0

    my['datas'][kl] = my['datas'].get(kl, Data(data['cols']['names']))
    my['datas'][kl].add(row)


def eg_bayes():
    wme = {'acc': 0, 'datas': {}, 'tries': 0, 'n': 0}
    # Assuming you have a function DATA.new that takes a file path and a callback function
    # and calls the given function for each row in the data
    DATA.new("../data/diabetes.csv", lambda data, t: learn(data, t, wme))
    
    print(wme['acc'] / (wme['tries']))
    return wme['acc'] / (wme['tries']) > 0.72


print(eg_bayes())