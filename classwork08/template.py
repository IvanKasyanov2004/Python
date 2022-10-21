def task1():
	a, b = map(int, input().split())
	c = a ** 2 + b ** 2
	print(c)

def task2():
	s = input()
	k = 0
	for x in s:
	if (ord(x) >= 48) and (ord(x) <= 57):
        k = k + 1
	print(k)

def task3():
	a = input().split()
	k = 0
	for s in a:
	    s0 = []
	    for i in s:
	        s0.append(i)
	    if (s0[0] == "A") and (s0[1] == "b") and (s0[2] == "o"):
	        k = k + 1
	print(k)

def task4(generator):
    # TODO: четвертое задание

def task5(list_of_smth):
    list = []
    for i in range(1, len(list_of_smth), 2):
        list.append(list_of_smth[i])
    print(list[len(list)-2: 1: -1])


def task6(list1, list2, list3, list4):
    d1 = set(list1)
    d2 = set(list2)
    d3 = set(list3)
    d4 = set(list4)
    m1 = d1 | d4
    m2 = d2 | d3
    m = m1 & m2
    print(m)


def task7():
    import numpy as np
    np.random.seed(3)
    matrix = np.random.randint(36, size=36).reshape(6,6)
    matrix1 = np.delete(matrix, 5, 0)
    matrix2 = np.delete(matrix1, 0, 1)
    det = np.linalg.det(matrix2)
    return(matrix, det)

def task8(f, min_x, max_x, N, min_y, max_y):
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib as mpl
    x = np.linspace(min_x, max_x, N)
    y = f(x)
    plt.xscale('log')
    plt.plot(x, y, "k.")
    plt.grid(True)
    plt.ylim((min_y, max_y))

    y1 = plt.derivative(f, x)
    plt.plot(x, y1)
    plt.show
    plt.savefig('function.jpg')

def task9(data, x_array, y_array, threshold):
    # TODO: ...

def task10(list_of_smth, n):
    # TODO: ...

def task11(filename="infile.csv"):
    # TODO: ...

def task12(filename="video-games.csv"):
	import pandas as pd
	import numpy as np
	d = pd.read_csv("video-games.csv")
	n_games = len(d.groupby(["title"]).agg('count'))
	
	by_years = d.groupby(["year"]).agg({"Unnamed: 0": "count"})
	by_years
	
	pub = d[d["publisher"] == "EA"]
	mean_price = pub.groupby(["title"]).agg({"price": "mean"})
	
	rait = d[(d["max_players"] == 1) | (d["max_players"] == 2)]
	mean_raiting_1_2 = rait["review_raiting"].mean()
	
	n_games_by_age = d.groupby("review_raiting").agg({"Unnamed: 0": "count"})
	n_games_by_age
	
	p = d.groupby(["publisher"]).agg('count')
	p.index.values
	m = set()
	for x in p.index.values:
	    if len(x.split(',')) == 1:
	        m.add(x)
	creators = list(m)
	creators
	
	dict = dict()
	dict["n_games"] = n_games
	dict["by_years"] = by_years
	dict["mean_price"] = mean_price
	dict["mean_raiting_1_2"] = mean_raiting_1_2
	dict["n_games_by_age"] = n_games_by_age
	dict["creators"] = creators
	dict
