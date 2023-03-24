print('© DustyZero 2021')
print('Any information you enter into this program will be deleted as soon as the application is terminated.'
)
print('You dont actually press enter to begin lol')


print('Hello, welcome to the I_o1 testing quiz! Answer as many questions as possible to pass!')

ans = input('Are you ready to play? (yes/no) :')
score = 0
total_q = 10

if ans == 'yes' :
  ans = input('1. What is the name of the game?')
  if ans.lower() == 'Press enter to begin' :
    score += 1
    print('Correct!')
else:
    print('Incorrect.')
    
ans = input('2. Who made Press enter to begin?')
if ans.lower() == 'ThatDevSabrina' :
    score += 1
    print('Correct!')
else:
    print('Incorrect.')
    
ans = input('3. Who did the Albanian translation of the game?')
if ans.lower() == 'PoggersCube.' :
    score += 1
    print('Correct!')
else:
    print('Incorrect.')
    
ans = input('4. Is Press enter to being made in Unity?')
if ans.lower() == 'no' :
    score += 694206849291
    print('Correct.')
else:
    print('Incorrect.')
        
print('Thank you for participating in this short quiz! We hope we didnt make you feel uncomfortable! This program will now be terminated.')
print('You got [INSERT ERROR MESSAGE HERE] questions correct!')

ans = input('Are you ready to exit? (yes/no) :')
if ans == 'yes' :
  print('END')