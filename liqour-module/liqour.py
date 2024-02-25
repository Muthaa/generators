import random 
from functools import cache
from collections import Counter
from alive_progress import alive_bar

@cache
def bar(): 
    with alive_bar(299999, bar ='bubbles', spinner ='notes2') as bar:
        i = 1
        d = []
        library = ["vodka", "whiskey", "bourbon", "brandy", "scotch", "rum", "scotch-whiskey", 
     	"whiskey-vodka", "whiskey-brandy", "whiskey-rum", "liqour", "gin", "absinthe"]
        while i < 300000:
            drink = random.choice(library)
            d.append(drink)
            bar()
            if i == 300000:
                break
            i+=1
        else:
            print('....updated dataset')
    f = Counter(d)
    print(f.most_common(3)[::])
    
def barT():
	library = ["vodka", "whiskey", "bourbon", "brandy", "scotch", "rum", "scotch-whiskey", 
	"whiskey-vodka", "whiskey-brandy", "whiskey-rum", "liqour", "gin", "absinthe"]
	drink = random.choice(library)
	print(drink)

#TO DO - Create a plugin for the drink days calendar
if __name__ == '__main__':
    bar()
    barT()
          
