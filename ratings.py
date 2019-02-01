"""Restaurant rating lister."""

# put your code here

def restaurant_ratings(filename):
    """ Convert restaurant file into list with name and ratings"""
    #open file
    file_object = open(filename)
    
    #create empty list
    restaurant_list = []

    #read and clean file, add to list
    for line in file_object:
        line = line.rstrip().split(':')
        restaurant_list += [line]

    return restaurant_list
    

def sort_restaurants(restaurant_list):
    """ Sort list of restaurants, convert to dictionary and print ratings"""
    
    #sort list
    restaurant_list.sort()

    #create empty dictionary
    restaurant_dict = {}

    #convert sorted list to dictionary
    for restaurant in restaurant_list:
        restaurant_dict[restaurant[0]] = restaurant[1]

    #print restaurants and their rating
    for restaurant, rating in restaurant_dict.items():
        print(restaurant, 'is rated at', rating)

    user_choice()
    

def add_restaurant_rating():
    """Get user to add and rate restauant and print entire ratings list"""
    
    #Get user input
    user_restaurant = input('Add the name of the restaurant you wish to rate: ')
    user_rating = input('Rate {} out of 5 stars: '.format(user_restaurant))
    if user_rating not in range(1, 6):
            print('Rating must be between 1 and 5. Try again!')
            user_rating = input('Rate {} out of 5 stars: '.format(user_restaurant))
    #call function to return list of restaurants from earlier
    restaurant_list = restaurant_ratings('scores.txt')

    #add user input to list
    restaurant_list.append([user_restaurant.capitalize(), user_rating])
    
    #call sorting function on list
    sort_restaurants(restaurant_list)

def user_choice():
    user_choice = input('Select an option: \n1. Would you like to see all the ratings? \n2. Would you like to add a rating \n3. Would you like to quit? \nType choice here: ')
    if user_choice == '1':
        print('*' * 80)
        sort_restaurants(restaurant_ratings('scores.txt'))
    elif user_choice == '2':
        print('*' * 80)
        add_restaurant_rating()
    elif user_choice == '3':
        print('Goodbye!')
        exit()
    else:
        print('Try again. Your choice should be either 1, 2 or 3.')
        user_choice = input('Select an option: \n1. Would you like to see all the ratings? \n2. Would you like to add a rating \n3. Would you like to quit? \nType choice here: ')


user_choice()
