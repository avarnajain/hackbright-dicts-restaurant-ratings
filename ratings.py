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
    

#call function to open and parse file, and then sort it
sort_restaurants(restaurant_ratings('scores.txt'))

print('*' * 80)

def add_restaurant_rating():
    """Get user to add and rate restauant and print entire ratings list"""
    
    #Get user input
    user_restaurant = input('Add the name of the restaurant you wish to rate: ')
    user_rating = input('Rate {} out of 5 stars: '.format(user_restaurant))

    #call function to return list of restaurants from earlier
    restaurant_list = restaurant_ratings('scores.txt')

    #add user input to list
    restaurant_list.append([user_restaurant.capitalize(), user_rating])
    
    print('*' * 80)
    
    #call sorting function on list
    sort_restaurants(restaurant_list)


print('*' * 80)

#ask for user input
add_restaurant_rating()