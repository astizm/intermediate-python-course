"""random dice game"""
#main function
def main():
  #import random package
  import random
  #set roll limit
  dice_rolls = 2
  dice_sum = 0
  for i in range(0, dice_rolls):
   #set random outcome to variable with range 1-6
   roll = random.randint(1,6)
   dice_sum += roll
   #print outcome
   print(f'You rolled a {roll}')
   print(f'You have rolled a total of {dice_sum}')


if __name__ == "__main__":
  main()