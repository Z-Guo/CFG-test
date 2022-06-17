# creating a pull request.....


# """
# Task 1 - Question 1
# """
# is_raining = input('Is it raining? y/n')
#
# if is_raining == 'y':
#     print('take an umbrella')
# elif is_raining == 'n':
#     print('You dont need an umbrella')
#

"""
Question 2
"""

# my_money = float(input('How much money do you have? '))
# boat_cost = 20 + 5
#
# if my_money > boat_cost:
# 	print('You can afford the boat hire')
# else :
# 	print('You cannot afford the board hire')
#

"""
Question 3 
"""

#
# book_year = int(input('Enter the year:'))
#
#
# def calculate():
#     century_decade = divmod(book_year, 100)
#     century = century_decade[0]
#     decade = century_decade[1]
#     if century == 18:
#         equivalent_century = 'Eighteenth Century'
#     elif century == 19:
#         equivalent_century = 'Nineteenth Century'
#     if 0 <= decade < 10:
#         equivalent_decade = 'Noughties'
#     elif 10 <= decade < 20:
#         equivalent_decade ='Teens'
#     elif 20 <= decade < 30:
#         equivalent_decade ='Tweenties'
#     elif 30 <= decade < 40:
#         equivalent_decade ='Thirties'
#     elif 40 <= decade < 50:
#         equivalent_decade ='Fourties'
#     elif 50 <= decade < 60:
#         equivalent_decade ='Fifties'
#     elif 60 <= decade < 70:
#         equivalent_decade ='Sixties'
#     elif 70 <= decade < 80:
#         equivalent_decade ='Seventies'
#     elif 80 <= decade < 90:
#         equivalent_decade ='Eighties'
#     elif 90 <= decade < 100:
#         equivalent_decade ='Nineties'
#     print(f'{equivalent_century}, {equivalent_decade}')
#
# if book_year >= 1800 and book_year <= 1950:
#     calculate()
# else:
#     print('Books sold are between 1800 and 1950, please try again')
#

"""
Task 2 - Question 1, the index should be 0 for the first item
"""
#
# shopping_list = [
# 	"oranges",
# 	"cat food",
# 	"sponge cake",
# 	"long-grain rice",
# 	"cheese board",
# ]
# print(shopping_list[0])

"""
Task 2 - Question 2
"""

# item = input('What type of chocolate is it?')
#
# chocolates = {
#
# 	'white': 1.50,
#
# 	'milk': 1.20,
#
# 	'dark': 1.80,
#
# 	'vegan': 2.00,
#
# }
#
# if item in chocolates:
#     print(f'£{chocolates[item]}')

"""
Task 2 - Question 3
"""
# import random
# lottery = [6,17,23,49,77,52,15]
# winninglist = []
#
#
# def winning_numbers():
#     for number in range(7):
#         value = random.randint(1,99)
#         winninglist.append(value)
#
# winning_numbers()
#
# def lotterycheck():
#     prize = 0
#     is_match = set(winninglist).intersection(lottery)
#     count_match = len(is_match)
#     if count_match < 3:
#         prize = 0
#     elif count_match == 3:
#         prize = 20
#     elif count_match == 4:
#         prize =40
#     elif count_match == 5:
#         prize =100
#     elif count_match == 6:
#         prize =10000
#     elif count_match == 7:
#         prize =1000000
#     print(f'You have won £{prize}')
# lotterycheck()
#
#


"""
Task 3.1 

Pip is a tool used to install and manage libraries that can be used in the Python projects. 
The benefit of using pip is that you can use an extensive packages and modules beyond the standard library. 
For example, by importing and using a camelcase package, you can convert strings into camel case. 
"""

"""
Task 3.2
"""

# poem = 'I like Python and I am not very good at poems'
# with open('poem.txt', 'w') as poem_file:
#     poem_file.write(poem)


"""
Task 3.3
"""
#
# song_lyrics = "You could never know what it's like\
# \n Your blood like winter freezes just like ice \
# \n And there's a cold lonely light that shines from you\
# \n You'll wind up like the wreck you hide behind that mask you use\
# \n And did you think this fool could never win?\
# \n Well look at me, I'm coming back again\
# \n I got a taste of love in a simple way\
# \n And if you need to know while I'm still standing, you just fade away\
# \n Don't you know I'm still standing better than I ever did\
# \n Looking like a true survivor, feeling like a little kid\
# \n I'm still standing after all this time\
# \n Picking up the pieces of my life without you on my mind\
# \n I'm still standing (Yeah, yeah, yeah)\
# \n I'm still standing (Yeah, yeah, yeah)"
#
# with open('lyrics.txt', 'w') as lyrics_file:
#     lyrics_file.write(song_lyrics)
#
# def finding_lyrics(file_name,word):
#     with open(file_name, 'r') as file:
#         for line in file:
#             if word in line:
#                 print(line)
#
# finding_lyrics('lyrics.txt','still')
#

"""
Question 4.1
"""

# import requests
# import pickle
# def pokemon_name_moves(ID):
#     data = []
#     url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(ID)
#     response = requests.get(url)
#     pokemon = response.json()
#     name = pokemon['name']
#     name_format = f"Pokemon's name:{name}"
#     data.append(name_format)
#     moves = pokemon['moves']
#     print(f"Pokemon's moves:")
#     for move in moves:
#        move_data= move['move']['name']
#        print(move_data)
#        data.append(move_data)
#     print(data)
#     with open('pokemon.txt', 'wb') as handle:
#       pickle.dump(data,handle)
#
#
# list = [1,2,3,4,5]
# for ID in list:
#     pokemon_name_moves(ID)
