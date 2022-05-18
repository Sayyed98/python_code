# names=['rishi', 'shoeb', 'sultan', 'tiwari']
# # print(names[0])
# # print(names[1])
# # print(names[2])
# # print(names[3])
# # for i in names:
# #     print(i)


# # names=['rishi', 'shoeb', 'sultan', 'tiwari']
# # for i in names:
# #     message=('hi',i, 'what are doing today')
# #     print(message)

# # transportation_mode=["car","ship", "bike"]
# # print("i would like to own a {}, because i love ride".format(transportation_mode[2]))
# # print("i love long drive with open sunroof {}, and i want to learn driving".format(transportation_mode[0]))
# # print("i want to take a tour through {}".format(transportation_mode[1]))

# friends=["ravi","utkarsh","sultan","pawan","shoeb","rishi","dilshad" ,"tauseef"]
# for i in friends:
#     print(f"Good afternoon, {i} today i am oraginizing a dinner party, so please come to this party")
# friends.remove("tauseef")
# friends.append("sahil")
# print(friends)
# for i in friends:
#     print(f"hi {i}, party is organizing again so let's enjoy the party")
# for i in friends:    
#     print(f"hi {i}, now i want to tell you that i found a bigger dinner table ")
# friends.insert(0,"MOhd")
# friends.insert(5,"sayyed")
# friends.append("kuldeep")
# print(friends)
# for i in friends:
#     print("hi all {} you, {},{} and{} joining the dinner table".format(i,("MOhd"),("sayyed"),("kuldeep")))
# for i in friends:
#     print(f"hi {i}i can invite only five people because my table is won't arrive in time.")
# popped_friend=friends.pop()
# print(f"i am sorry for that {popped_friend} there is no more space")
# popped_friend=friends.pop()
# print(f"i am sorry for that {popped_friend} there is no more space")
# popped_friend=friends.pop()
# print(f"i am sorry for that {popped_friend} there is no more space")
# opped_friend=friends.pop()
# print(f"i am sorry for that {popped_friend} there is no more space")
# opped_friend=friends.pop()
# print(f"i am sorry for that {popped_friend} there is no more space")
# for i in friends:
#     print(f"{friends}, you are still invited")
#     break
# # del friends[0:]
# print("now i have no list".format(friends))

# place=["arab","palestine","iraq","switzerland","arab","spain"]
# print(place)
# soted_place=sorted(place)
# print(soted_place)
# print(place)
# print(sorted(place, reverse=True))
# print(place)
# place.reverse()
# print(place)
# place.reverse()
# print(place)
# place.sort()
# print("order has been changed now it is in alphabetitcal order",place)
# place.sort(reverse=True)
# print(place)
# print("now i am inviting ",len(friends),"people")

def person(guest):
    print("hello " +guest+" i would like to invite you to dinner")
def sorry(guest):
    print(f"sorry {guest}.Sadly you cannot come since we wont have enough room for all of you")

guestList=["Hujaifa", "sultan", "ravi"]
list(map(person,guestList))
print("oh no! Ravi can not come due to some reason")
guestList.remove("ravi")
print(guestList)
guestList.append("utkarsh")
