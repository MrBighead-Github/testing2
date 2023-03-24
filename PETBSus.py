print('© ThatDevSabrina 2022')
print('Hello, welcome to the S.U.S.S.Y testing quiz! Answer as many questions as possible to pass!')

ans = input('Are you ready to play? (yes/no) :')
score = 0
total_q = 10

if ans == 'yes' :
  ans = input('1. Did red vent?')
  if ans.lower() == 'yes' :
    score += 1
    print('Correct!')
else:
    print('Incorrect.')
    
ans = input('2. Are you the impostor?')
if ans.lower() == 'no' :
    score += 1
    print('Correct!')
else:
    print('Incorrect.')
    
ans = input('3. Did orange kill pink?')
if ans.lower() == 'yes' :
    score += 1
    print('Correct!')
else:
    print('Incorrect.')
    
ans = input('4. Did orange vent?')
if ans.lower() == 'yes' :
    score += 694206849291
    print('Correct.')
else:
    print('Incorrect.')
    
ans = input('5.Did cyan fake the card swipe?')
if ans.lower() == 'no' :
    score += 0
    print('Correct.')
else:
    print('OIncorrect.')
    
ans = input('6. How many impostors as there?')
if ans.lower() == '2' :
    score += 0
    print('Correct!')
else:
    print('Incorrect.')
    
ans = input('Are you ready to exit? (yes/no) :')
if ans == 'yes' :
  print('END')