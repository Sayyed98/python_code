# def display_message(message):
#     print(f"i am learning {message} programming language")
# display_message("python")

# def favorite_book(title1):
#     print(f"One of my favorite book is {title1.title()} in wonderland")
    
# favorite_book("alice")

# def make_shirt(size="L", text="I love go programming"):
#     print(f"The gucci shirt size is {size}, and {text} ")
# make_shirt()
# make_shirt(size="M", text="Python is easy language")
# # 8.4 practice
# make_shirt(size="L")
# make_shirt(size="M")
# make_shirt(size="XXL", text="React is one the trending language")


# 8.5 practice number

# def describe_cities(city, country="INdia"):
#     print(f"{city} is in {country}")

# describe_cities(city="Allahabad")
# describe_cities(city="Bangaluru")
# describe_cities(city="Mecca", country="Saudi Arabia")


# 8.6 practice number
# def city_country(city, country):
    
#     message=f'"{city.title()}, {country.title()}"'

#     return message
# pair=city_country(city="Mumbai",country="India")
# print(pair)
# pair=city_country(city="Allahabad", country="India")
# print(pair)
# pair=city_country(city="Luckhnow", country="India")
# print(pair)

# def make_album(artist, album1, songs=None):
#     empty_dict={}
#     empty_dict={"Artis tName":artist, "Album Title":album1}
#     if songs:
#         empty_dict['songs']=songs
#     return empty_dict
# while True:
#     ArtistName=input("enter a artist name: ")
#     if ArtistName=="q":
#         break
#     AlbumTitle=input("enter album title name: ")  
#     if AlbumTitle=="q":
#         break
#     userinput=make_album(ArtistName,AlbumTitle)
#     print(userinput)
# album=make_album("A.R. Rahman", "Sultan")
# print(album)

#           this is used for checking that returned data types is dictionary is not
# print(isinstance(album, dict))
# for key,value in album.items():
#     if (key=='artist'):
#         print(f"The {key} name is {value.title()}.")
#     elif(key=='album1'):
#         print(f"The albums {key}, is {value.title()}")
#     elif(key=='songs'):
#         print(f"the no of {key}, is {value.title()}.")
# print(" ")

# album=make_album("Lata Mangeskar", "Ishq", songs=10)
# print(album)
# print(isinstance(album, dict))
# for key,value in album.items():
#     if (key=='artist'):
#         print(f"The {key} name is {value.title()}.")
#     elif(key=='album1'):
#         print(f"The albums {key}, is {value.title()}")
#     elif(key=='no_of_songs'):
#         print(f"the no of {key}, is {value.title()}.")
# print(" ")

# album=make_album("Atif Aslam", "Coke", 25)
# print(album)
# print(isinstance(album, dict))
# for key,value in album.items():
#     if (key=='artist'):
#         print(f"The {key} name is {value.title()}.")
#     elif(key=='album1'):
#         print(f"The albums {key}, is {value.title()}")
#     elif(key=='no_of_songs'):
#         print(f"the no of {key}, is {value.title()}.")
# print(" ")




# def show_message(message_list):
#     print("\n showing message")
#     for mess in message_list:
#         print("-----------------------------")
#         print(mess)
#         print("-----------------------------")

# def send_message(message_list):
#     print("\n sending message")
#     while message_list:
#         old_message=list1.pop()
#         print("===========================")
#         print(old_message)
#         print("===========================")
#         sent_message.append(old_message)
    
# list1=["pepperani","cheese", "chicken"]
# print("original messages before sending")
# print(list1)
# sent_message=[]
# show_message(list1)
# send_message(list1)
# print("original message list after sending")
# print(sent_message)



# def send_messsages(list_message):
#     while list_message:
#         new_list=list.pop()
#         print("new list is ", new_list)
#         sent_message.append(new_list)
# def print_list(input_list):
#     if input_list:
#         print("this list contains the following list: ")
#         for value in input_list:
#             print(value)
#     else:
#         print('this list is empty')
    
# list=["hOw","are","you", "good thandks", "bye"]
# sent_message=[]
# send_messsages(list)
# print("\n original messages list")
# print_list(list)
# print("\n sent messages list")
# print_list(sent_message)



# def list_of_sandwich(*types):
#     for list in types:
#         print(f"You have order {list} sandwich")
# list_of_sandwich("potato", "cheese")
# list_of_sandwich("mix", "veg", "tomato", "chicken")
# print(list_of_sandwich("mutton","maggi","butter","carrot","mayoneese"))


# def build_profile(first, last, **user_info):
#     user_info['First Name']=first
#     user_info["Last Name"]=last
#     return user_info
# user_profile=build_profile('Mohd', "Hujaifa", Age=20, Address="Saidahan", salary=20000)
# print(user_profile)


# def car_func(manufacturer, model, **car_info):
#     car_info["manufacturer name"]=manufacturer
#     car_info["model name"]=model
#     return car_info
# car_details=car_func("honda","city",color="REd")
# print(car_details)