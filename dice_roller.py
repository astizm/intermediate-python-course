"""random dice game"""
#main function
def main():
  #import random package
  import random
  #set roll limit and dice details
  dice_rolls = int(input('How many dice would you like to roll?'))  
  dice_sum = 0
  dice_size = int(input('How many sides are the dice?'))
  for i in range(0, dice_rolls):
   #set random outcome to variable with dice size range
   roll = random.randint(1,dice_size)
   dice_sum += roll
   #print outcome
   if roll == 1:
    print(f'You rolled a {roll}! Critical Fail')
    quit()
   elif roll == dice_size:
     print(f'You rolled a {roll}! Critical Success')     
   else:
    print(f'You rolled a {roll}')
    print(f'You have rolled a total of {dice_sum}')



if __name__ == "__main__":
  main()