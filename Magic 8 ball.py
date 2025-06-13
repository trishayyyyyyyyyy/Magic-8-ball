# Write code below 💖
import random

question = input('Enter your question : ')

num = random.randint(1, 9)

if num == 1:
  answer = ('yes definitely')
elif num == 2:
  answer = ('It is decidedly so')
elif num == 3:
   answer = ('Without a doubt.')
elif num == 4:
   answer = ('Reply hazy, try again.')
elif num == 5:
   answer = ('Ask again later.')
elif num == 6:
  answer = ('Better not tell you now.')
elif num == 7:
  answer = ('My sources say no.')
elif num == 8:
  answer = ('Outlook not so good.')
elif num  == 9:
  answer = ('very doubtful')
  
print('Magic 8 Ball:  ' + answer)


