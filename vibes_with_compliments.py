import time
import random

#List

compliments=['You are so pretty', 'You should be proud of yourself', 'You are enough', 'You are so smart', 'You are awesome!']

#Function

def true_vibe(vibing):

    while True:

        if vibing == 'yes':
            print ('Lovely! Keep on vibing! =)')
            break

        if vibing == 'no':
            print()
            print("Ok, let's get you there")
            time.sleep(1)
            print()
            print('Step 1: Stop!')
            time.sleep(2)
            print()
            print('Step 2: Breathe!')
            time.sleep(2)
            print()
            print('Step 3:  Smile!')
            time.sleep(2)
            print()
            print(random.choice(compliments))
            time.sleep(1)
            print()
            vibing=input('All done, can you feel it? ').lower()

            true_vibe(vibing)
            break

        else:
            print ('Sorry - I did not catch the vibe there. Could you please try again?')
            vibing = input('Are the good vibes with you today? ').lower()

            true_vibe (vibing)
            break

#Flow

vibing = input('Hello there. Are you feeling the good vibes today? ').lower()


true_vibe(vibing)
