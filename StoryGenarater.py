import random

a1 = input('Choose an adjective: ')

a2 = input('Choose another adjective: ')

a3 = input('Choose another one: ')

a4 = input('Chose one more: ')

a5 = input('Alright, last one: ')

a6 = input('Okay, actuall last one: ')

storys = ("story 1", "story 2", "story 3", "story 4")
stories = random.randint(1,4)
print('------------------------------------------')
if stories==1:

    print("Wow, the weather is", a1)

    print("My cat is acting really", a2, "today")

    print("I'm feeling", a3)

    print("My brother is", a4)

    print("My food is", a5)

    print("I'm having such a", a6, "day")

elif stories==2:
    print("My sister is not", a1)
          
    print("tommorrow will be", a2)
    
    print("I like to eat", a5, "food")

    print("my dog was", a4)
    
    print("why is my fish", a6)
    
    print("I think I'm really", a3)
    
elif stories==3:
    print("I think school is", a4)
    
    print("I have a", a3, "child" )
    
    print("My friends think I'm very", a1 )
    
    print("My parents say that", a2, "people are", a5)
    
    print("Yesterday was a", a6, "day")
    
elif stories==4:
    print("I saw a", a3, "animal")
    
    print("My friend wore a", a1, "shirt today")
    
    print("I found a", a6, "book at the library today")
    
    print("The restaraunt's menu was", a4,)
    
    print("I don't like my neihghber beacause he is ", a2)
    
    print("I wore", a5, "shoes")
    
    
