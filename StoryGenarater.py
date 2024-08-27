import random

a1 = input('Choose an adjective: ')

a2 = input('Choose another adjective: ')

a3 = input('Choose another one: ')

a4 = input('Chose one more: ')

a5 = input('Alright, last one: ')

a6 = input('Okay, actuall last one: ')

storys = ("story 1", "story 2", "story 3", "story 4")
stories = random.randint(1,3)
print('------------------------------------------')
if stories<2:

    print("Wow, the weather is", a1)

    print("My cat is acting really", a2, "today")

    print("I'm feeling", a3)

    print("My brother is", a4)

    print("My food is", a5)

    print("I'm having such a", a6, "day")

elif stories==2:
    print("My sister is not", a1)
          
    print("tommorrow will be", a2)
    
    print("I like to eat", a5)

    print("I'm trying to make my dog", a4)
    
    print("why is my fish", a6)
    
    print("I think I'm really", a3)
    
else:
    print("I think school is", a4)
    
    print("I have a", a3, "child" )
    
    print("My friends think I'm very", a1 )
    
    print("My parents say that", a2, "people are", a5)
    
    print("Yesterday was a", a6, "day")
    
    
