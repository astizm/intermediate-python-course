"""random dice game"""
#main function
def main():
  #import random package
  import random
  
  #set player detail
  player = str(input("What's your name? "))
  #set roll limit and dice details
  roll = int
  dice_rolls = int(input('How many dice would you like to roll? '))  
  dice_sum = 0
  dice_size = int(input('How many sides are the dice? '))
  
  for i in range(0, dice_rolls):
   #set random outcome to variable with dice size range
   roll = random.randint(1,dice_size)
   dice_sum += roll
   #add score to list
   scores = list((player,roll, dice_sum))
   #print outcome 
   if roll == 1:
    print(f'You rolled a {roll}! Critical Fail')
    print(scores)
    quit()
   elif roll == dice_size:
     print(f'You rolled a {roll}! Critical Success')     
   else:
    print(f'You rolled a {roll}')
    print(f'You have rolled a total of {dice_sum}')
  

    
  print(scores)
  


if __name__ == "__main__":
  main()