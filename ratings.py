"""Restaurant rating lister."""


# put your code here
restaurant_dict = {}

def restaurant_ratings(filename):
    """ Convert restaurant file into dictionary"""
    #open file
    file_object = open(filename)

    #creat empty data structures
    combined_list = []
    
    #read and clean file, add to list
    for line in file_object:
        line = line.rstrip().split(':')
        combined_list += [line]
    
    #sort list
    combined_list.sort()

    #convert sorted list to dictionary
    for restaurant in combined_list:
        restaurant_dict[restaurant[0]] = restaurant[1]

    print_ratings(restaurant_dict)
    #print restaurants and their rating
    

def print_ratings(restaurant_dictionary):
    """print restaurant ratings"""
    for restaurant, rating in restaurant_dict.items():
        print(restaurant, 'is rated at', rating)

#call function
restaurant_ratings('scores.txt')

print('*' * 80)

#Get user input
user_restaurant = input('Add the name of the restaurant you wish to rate: ')
user_rating = input('Rate {} out of 5 stars: '.format(user_restaurant))

#Add use input to global dictionary
restaurant_dict[user_restaurant] = user_rating


print('*' * 80)

#call printing function
print_ratings(restaurant_dict)
