import random
rock = '''
 _______)
      ---'   ____)
            (_____)
            (_____)
    VK      (____)
      ---.__(___)
'''
paper = '''
          _______
      ---'   ____)____
                ______)
                _______)
    VK         _______)
      ---.__________)
'''
scissors ='''
 _______
      ---'   ____)____
                ______)
             __________)
    VK      (____)
      ---.__(___)
'''
game_images = [rock,paper,scissors]
user_choice = int(input('What do want to choose.Type "0" for rock "1" for paper and "2" for scissors\n'))
if user_choice >=3 or user_choice <0:
    print("You have chosen a number which is not defined. You Lose!")
else:
    print(game_images[user_choice])
    computer_choice = random.randint(0,1)
    print(f"computer chooses :{computer_choice}")
    print(game_images[computer_choice])
    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose!")
    elif computer_choice > user_choice:
        print("You Lose!")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice == user_choice:
        print("its a draw!")
