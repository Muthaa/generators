import random 
import datetime
# from time import sleep
from functools import cache
from collections import Counter
from alive_progress import alive_bar

@cache
# def bar(): 
#     with alive_bar(999, bar ='bubbles', spinner ='notes2') as bar:
#         i = 1
#         while i < 1000:
#             library = ["vodka", "whiskey", "bourbon", "brandy", "scotch", "rum", "scotch-whiskey", 
#          	"whiskey-vodka", "whiskey-brandy", "whiskey-rum", "liqour", "gin", "absinthe"]
#             drink = random.choice(library)
#             with open ("alc", 'a+') as file:
#                 file.write(drink+"\n")
#                 bar()
#             if 1 == 1000:
#                 break
#             i+=1
#         else:
#             print('....updated dataset')
def bar(): 
    with alive_bar(999999, bar ='bubbles', spinner ='notes2') as bar:
        i = 1
        d = []
        library = ["vodka", "whiskey", "bourbon", "brandy", "scotch", "rum", "scotch-whiskey", 
     	"whiskey-vodka", "whiskey-brandy", "whiskey-rum", "liqour", "gin", "absinthe"]
        while i < 1000000:
            drink = random.choice(library)
            d.append(drink)
            bar()
            if i == 1000000:
                break
            i+=1
        else:
            print('....updated dataset')
    f = Counter(d)
    print(f.most_common()[::])
# def al():
#     drink=[]
#     with open ("alc", 'r') as file:
#         for line in file:
#             drink.append(line.strip())
#         d = Counter(drink)
#         print(d.most_common()[::])

def barT():
	library = ["vodka", "whiskey", "bourbon", "brandy", "scotch", "rum", "scotch-whiskey", 
	"whiskey-vodka", "whiskey-brandy", "whiskey-rum", "liqour", "gin", "absinthe"]
	drink = random.choice(library)
	print(drink)


def dd():
    drinkdays = []
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    f = month,"-", day
    with open ("dd", 'r') as file:
        for line in file:
            drinkdays.append(line.strip())
        if f == drinkdays:
            print(f)
# while True:
bar()
#barT()
#al()             
dd()