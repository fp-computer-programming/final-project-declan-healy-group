#Declan Healy

restart = 1


while restart == 1:

  
  # this is the while loop for the question asking the player if they are ready?
  i = 0
  # this is code below prints the introduction/title of the quiz/game
  print('WELCOME TO THE QUIZ GAME BY ME')
  
  # input code for the user's name
  user_name = input('What is your User Name?')
  
  # code that prints instructions for completing the quiz
  print ('\nHI THERE ' + user_name + '! Lets play a quiz!\n')
  print ('So you basically you have a question in front of you.\n\nYou have options and you write if it is a, b, c, or d(case censitive)\n')
  print ('If you get it correct you get a point.\n\nIf you get it incorrect you lose a point\n')
  print ('If you start from level one you can attempt a bonus question\n')
  
  # score initialization
  score = 0
  
  # asking the player if he/she is prepared to answer the questions
  while i<1:
    ready = input("Are You Ready? Type 'yes' or 'no'\n")
    if ready == 'yes' or ready == 'Yes':
      print('let\'s go then\n')
      i = 1
    
  # player's choice for difficulty
  user_level_choice = input('What level do you like to start from, Easy or Hard. Type level 1 or level 2:\n')
  if user_level_choice == 'level 1': 
    # Start of question 1
    print("Question 1: What is 2+2?\n")
    print("a: 2")
    print("b: 4")
    print("c: 6")
    print("d: 8\n")
  
    # Code defining whether player's input is right or wrong for question 1 and if right he gets a point else loses 1 point
    response = input("What is your answer to this question?\n")
    if response == "b":
      print("Correct, good job!")
      score += 2
    else:
      print("sorry incorrect, don't worry many questions left to go!, try again")
    score -= 1
    print("your score is {}\n".format(score))
  
    # Start of question 2
  
    print("Question 2: How long did jesus stay in the desert?\n")
    print("a: 30 days")
    print("b: 40 days")
    print("c: 50 days")
    print("d: 60 days\n")
  
    # Code defining whether player's input is right or wrong for question 2 and if right he gets a point else loses 1 point
    response = input("What is your answer to this question?\n")
    if response == "b":
      print("Correct, have a point")
      score += 2
    else:
      print("sorry incorrect")
    score -= 1
    print("your score is {}\n".format(score))
  
    # Start of question 3
  
    print("Question 3: What year was saint Ignatious born?\n")
    print("a: 1436")
    print("b: 1450")
    print("c: 1500")
    print("d: 1491\n")
  
    # Code defining whether player's input is right or wrong for question 3 and if right he gets a point else loses 1 point
    response = input("What is your answer to this question?\n")
    if response == "d":
      print("Correct, good job")
      score += 2
    else:
      print("sorry incorrect")
    score -= 1
    print("your score is {}\n".format(score))
  
    # Start of question 4
  
    print("What year was Saint Ignatious hit by a cannonball?\n")
    print("a: 1536 ")
    print("b: 1511 ")
    print("c: 1521")
    print("d: 1543\n")
  
    # Code defining whether player's input is right or wrong for question 4 and if right he gets a point else loses 1 point
    response = input("What is your answer to this question?\n")
    if response == "c":
      print("Correct")
      score += 2
    else:
      print("sorry incorrect")
    score -= 1
    print("your score is {}\n".format(score))
  
  
    # Start of question 5
  
    print("Question 5: What year did Saint Ignatious die?\n")
    print("a: 1563")
    print("b: 1561")
    print("c: 1554")
    print("d: 1556\n")
  
    # Code defining whether player's input is right or wrong for question 5 and if right he gets a point else loses 1 point
    response = input("What is your answer to this question?\n")
    if response == "d":
      print("Correct")
      score += 2
    else:
      print("sorry incorrect, don't get upset always can get free points for a next level")
    score -= 1
    print("your score is {}\n\n".format(score))
  
   # code that asks the player if they want to continue to level 2 and it'll only appear if they start from level 1 as it is in a while loop
    level_2 = input("You have reached level 2, do you wish to continue or exit?\n")
    if level_2 == "continue" or level_2 == "yes":
      print ('have 2 free points for keeping up\n!')
      score += 2
      print ('your score is {}\n\n'.format(score))
      
        # Start of question 6
      print("Question 6: Where did Saint Ignatious die?\n")
      print("a: France ")
      print("b: Rome ")
  
      # Code defining whether player's input is right or wrong for question 6 and if right he gets a point else loses 1 point
      response = input("What is your answer to this question?\n")
      if response == "b":
        print("Correct, way to go")
        score += 2
      else:
        print("sorry incorrect")
      score -= 1
      print("your score is {}\n".format(score))
  
  
      # Start of question 7
  
      print("Question 7: Where was Saint Ignatious born?\n")
      print("a: Spain ")
      print("b: Rome")
      print("c: France")
  
      # Code defining whether player's input is right or wrong for question 7 and if right he gets a point else loses 1 point
      response = input("What is your answer to this question?\n")
      if response == "a":
        print("Correct, nice job here have a point")
        score += 2
      else:
        print("sorry, next time")
      score -= 1
      print("your score is {}\n".format(score))
  
      # Start of question 8
  
      print("Question 8: Roughly how many students go to prep?\n")
      print("a: 800")
      print("b: 900")
      print("c: 700")
      print("d: 600")
      
      # Code defining whether player's input is right or wrong and if right then should he get a point or not
      response = input("What is your answer to this question?") 
      if response == "a":
        print("Correct!")
        score += 2
      else:
        print("sorry incorrect")
      score -= 1
      print("your score is {}\n".format(score))
  
      print("Question 9: What order did Saint Ignatious found?\n")
      print("a: The Orthodox")
      print("b: The jesuits")
      print("c: The Catholic society")
      print("d: The jesus gang")
  
      # Code defining whether player's input is right or wrong for question 9 and if right he gets a point else loses 1 point
      response = input("What is your answer to this question?\n")
      if response == "b":
        print("Correct, have a point")
        score += 2
      else:
        print("sorry incorrect")
      score -= 1
      print("your score is {}\n".format(score))
  
      # Start of question 10
  
      print("Question 10: What age did Saint Ignatious die at?.\n")
      print("a: 72 ")
      print("b: 61")
      print("c: 64")
      print("d: 69")
  
      # Code defining whether player's input is right or wrong for question 10 and if right he gets a point else loses 1 point
      response = input("What is your answer to this question?\n")
      if response == "c":
        print("Correct, nice job here have a point\n\n")
        score += 2
      else:
        print("sorry, incorrect\n")
      score -= 1
      print('your score is {}'.format(score))
      
      if score>8:
        print('Wow amazing performance try this bonus question!\n\n')
  
      #Stating that if the score is more than 8 then bonus question appears:
      if score>8 :
        print('Bonus Question: What is the capital of CT?')
        print('a: New Haven')
        print("b: Stamford")
        print("c: Hartford")
        print("d: Bridgeport\n")
  
      # Code defining whether player's input is right or wrong for question 1 and if right he gets a point else loses 1 point
      if score>8 :
        response = input("What is your answer to this question?\n")
      if response == "c":
        print("Correct!\n")
        score += 2
      else:
        print("Sorry, Incorrect\n")
      score -= 1
      print("your Final score is {}!\n\n".format(score))
        
      print("THANKS FOR PLAYING!")
  
      # asking the player's feedback
      PLAYERS_FEEDBACK = input(" Please rate this quiz out of ten \n")
  
      play_again = input("Do you want to restart? Yes or No\n")
  
      # this code is asking the user if he wants to restart
      if play_again == "Yes" or play_again == "yes":
          exec(open("./final.py").read())
      else:
          exit()
  
  
      print("Great choice\n\n")
    else:
      quit()
  
      
  else:
    # Start of question 6
    print("Question 6: Where did Saint Ignatious die?\n")
    print("a: France ")
    print("b: Rome ")
  
    # Code defining whether player's input is right or wrong for question 6 and if right he gets a point else loses 1 point
    response = input("What is your answer to this question?\n")
    if response == "b":
      print("Correct, way to go")
      score += 2
    else:
      print("sorry, not bad")
    score -= 1
    print("your score is {}\n".format(score))
  
  
    # Start of question 7
  
    print("Question 7: Where was Saint Ignatious born?\n")
    print("a: Spain ")
    print("b: Rome")
    print("c: France")
  
    # Code defining whether player's input is right or wrong for question 7 and if right he gets a point else loses 1 point
    response = input("What is your answer to this question?\n")
    if response == "a":
      print("Correct, nice job here have a point")
      score += 2
    else:
      print("sorry, next time")
    score -= 1
    print("your score is {}\n".format(score))
  
    # Start of question 8
  
    print("Question 8: Roughly how many students go to prep?\n")
    print("a: 800")
    print("b: 900")
    print("c: 700")
    print("d: 600")
      
    # Code defining whether player's input is right or wrong and if right then should he get a point or not
    response = input("What is your answer to this question?\n") 
    if response == "a":
      print("Correct!")
      score += 2
    else:
      print("sorry, incorrect")
      score -= 1
    print("your score is {}\n".format(score))
  
    # Start of question 9
  
    print("Question 9: What order did Saint Ignatious found?\n")
    print("a: The Orthodox")
    print("b: The jesuits")
    print("c: The Catholic society")
    print("d: The jesus gang")
  
    # Code defining whether player's input is right or wrong for question 9 and if right he gets a point else loses 1 point
    response = input("What is your answer to this question?\n")
    if response == "a" or response == "b":
      print("Correct!")
      score += 2
    else:
      print("sorry, incorrect")
    score -= 1
    print("your score is {}\n".format(score))
  
    # Start of question 10
  
    print("Question 10: What age did Saint Ignatious die at?.\n")
    print("a: 72 ")
    print("b: 61")
    print("c: 64")
    print("d: 69")
  
    # Code defining whether player's input is right or wrong for question 10 and if right he gets a point else loses 1 point
    response = input("What is your answer to this question?\n")
    if response == "c":
      print("Correct!")
      score += 2
    else:
      print("sorry, incorrect\n")
    score -= 1
  
    print("your Final score is {}!\n\n".format(score))
      
    print("THANKS FOR PLAYING!")
  
    # asking the player's feedback
    PLAYERS_FEEDBACK = input(" Please rate this quiz out of ten and tell us what we could improve on \n")
  
    play_again = input("Do you want to restart/play again? Yes or No\n")
  
    # this code is asking the user if s/he wants to restart
    if play_again == "Yes" or play_again == "yes":
        restart = 1 
    else:
        restart = 0
        exit()
  



