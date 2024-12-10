rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
print('Welcome to the Rock, Paper, Scissors Game!')
choice_1=input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors')
choice_list=[]

if choice_1=='0':
    print('You chose: '+ rock)
    choice_list.append(rock)
if choice_1=='1':
    print('You chose: ' + paper)
    choice_list.append(paper)
if choice_1=='2':
    print('You chose: '+ scissors)
    choice_list.append(scissors)
list1=[rock, paper, scissors]
comp_choice=random.choice(list1)
print('Computer chose: '+ comp_choice)

if choice_list[0]==comp_choice:
    print('Its a draw')
elif choice_1=='0' and comp_choice==scissors:
    print('You win')
elif choice_1=='1' and comp_choice==rock:
    print('You win')
elif choice_1=='2' and comp_choice==paper:
    print('You win')
else:
    print('You lose sucker')