# def function():
#     """Display s simple geeting message"""
#     print('heelo worid')
# function()


# def greet(username):
#     print("hello,{}".format(username))
# greet("mohd")
# greet("sayyed")

# def display_message():
#     print("i am learning function in this chapter")
# display_message()

# def favorite_book(title):
#     print(f"One of my favorite books is {title.title()} in wonderland"
# favorite_book("alice")

# def make_tshirt(size="L", message="I Love Python"):
#     print(f"Hi cool {message} ,and tshirt size is {size}")
# make_tshirt('M')
# make_tshirt(size="L")
# s="Python is High level language,"
# s+="it is independent language"
# make_tshirt(size="s", message=s)

# def describe_cities(city, country="India"):
#     print(f"{city} is in {country}")
# describe_cities("Delhi")
# describe_cities(city="Allahabad")
# describe_cities("bangaluru", country="Saudi Arabia")

# def city_country(city, country):
#     country=(f'"{city}, {country}"')
#     return country
# pair=city_country(city="Santiago", country="Chile")
# print(pair)
# pair=city_country(city="Allahabad", country="India")
# print(pair)
# pair=city_country(city="Delhi", country="india")
# print(pair)

# def make_album(artist_name, album,number_song=None):
    
#     album_dict={"Artist Name":artist_name, 
#                 "Album Nmae":album }
#     if number_song:
#         album_dict['Number of Song']=number_song
#     return album_dict
    

# name_album=make_album("AR Rahman", "XYZ")
# print(name_album)
# print(make_album("arijit singh", "Meri Ashiqui"))
# print(make_album(artist_name="lata mangeskar", album="Ye duniya"))
# name_album=make_album("Nusrat Fateh Ali Khan", "dam_dama_dam",12)
# print(name_album)


# def make_album(artist, title, song_number=''):
#     album_dict={"artistname":artist, "title of album":title}
#     if song_number:
#         album_dict["number of song"]=song_number
#     return album_dict
# while True:
#     artist_name=input("Artist Name:")
#     if artist_name=="quit":
#         break
#     album_title=input("Album Title:")
#     if album_title=="quit":
#         break
#     call_make_album=make_album(artist_name,album_title)
#     print(call_make_album)




# def show_messsage(list_message,completed_message):
#     while list_message:
#         current_list=list_message.pop()
#         print(f"You are good{current_list}")
#         completed_message.append(current_list)


# def send_message(completed_message):
#     print("\n The following list has been printed:")
#     for message in completed_message:
#         print(message)

    
# list_message=["Good", "Awesome","Charming", "Handsome"]
# completed_message=[]
# show_messsage(list_message, completed_message)
# send_message(completed_message[:])
# print("original message llist is :")
# send_message(completed_message)
# print(list_message)
# print(completed_message)





# def person_sandwich(*sandwich):
#     return sandwich
# print(person_sandwich("peperani"))
# print(person_sandwich("veg_sandwich", "chicken_sandwich", "potato_sandwich"))
# print(person_sandwich('cheese_sandwich', "mix_veg_sandwich","ginger_garlic_sandwich",\
#     "nuts_sanwich"))

def build_profile(first, last, **other):
    dict={"first":first, "lastName":last, }
    return other, dict
user_profile=build_profile("mohd", "Hujifa", age=26,address="saidahan", salary=50000)
print(user_profile)


def cars(manufacturer,model_name, **car):
    car["Manufacturer Date"]=manufacturer
    car["Model Name"]=model_name
    return car
print(cars(2018, "Volkswagen", color="red", tow_package=True))

