#Runtime Complexity

commands = ['n', 's', 'w', 'e', ... 1000]

selection = input()

'''In the worst case, we'd have to iterate over every element 
    in the list to find what we're looking for '''
#So this is a linear operation    
if selectioin in commands:
    #this is a valid command
    #perform the user's command

#Constant time; does't grow at all as the size of the input increases
commands[3]

''' the size of the input has no bearing on the efficiency of this operation'''

#Linear time; gorws 1 to 1 as the size of the input increases
for command in commands:
    print(command)
''' the size of the input will decrease the efficiency of this operation; 
    has a direct bearing ofn the efficiency'''

#Constant < Linear
''' Wht's being compared is how quickly the efficiency grows as a result'''

#Big O allows us to drop constants