"""Restaurant rating lister."""


# put your code here

def restaurant_ratings(filename):
    """ Print restaurants and their ratins"""
    #open file
    file_object = open(filename)

    #creat empty data structures
    combined_list = []
    restaurant_dict = {}
    
    #read and clean file, add to list
    for line in file_object:
        line = line.rstrip().split(':')
        combined_list += [line]
    
    #sort list
    combined_list.sort()

    #convert sorted list to dictionary
    for restaurant in combined_list:
        restaurant_dict[restaurant[0]] = restaurant[1]

    #print restaurants and their rating
    for restaurant, rating in restaurant_dict.items():
        print(restaurant, 'is rated at', rating)


restaurant_ratings('scores.txt')