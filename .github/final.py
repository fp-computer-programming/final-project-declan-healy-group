#Declan Healy

restart = 1


while restart == 1:

  
  # this is the while loop for the question asking the player if they are ready?
  i = 0
  # this is code below prints the introduction/title of the quiz/game
  print('WELCOME TO THE NOT GREATEST QUIZ GAME BY ME')
  
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
      print("Correct, here have a point")
      score += 2
    else:
      print("sorry incorrect, next time")
    score -= 1
    print("your score is {}\n".format(score))
  
    # Start of question 3
  
    print("Question 3: How long is Ninety Mile beach in Northland?\n")
    print("a: 85 Miles")
    print("b: 90 Miles")
    print("c: 91 Miles")
    print("d: 55 Miles\n")
  
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
  
    print("Question 4: Where is the famous landmark L&P from?\n")
    print("a: Hamilton ")
    print("b: Lemon ")
    print("c: Paeroa")
    print("d: Tauranga\n")
  
    # Code defining whether player's input is right or wrong for question 4 and if right he gets a point else loses 1 point
    response = input("What is your answer to this question?\n")
    if response == "c":
      print("Correct, here have a point")
      score += 2
    else:
      print("sorry incorrect, for the loss of your points")
    score -= 1
    print("your score is {}\n".format(score))
  
  
    # Start of question 5
  
    print("Question 5: What is rarity is the grenade launcher in Fortnite?\n")
    print("a: Rare")
    print("b: Epic")
    print("c: Common and Rare")
    print("d: Epic and Legendary\n")
  
    # Code defining whether player's input is right or wrong for question 5 and if right he gets a point else loses 1 point
    response = input("What is your answer to this question?\n")
    if response == "d" or response == "a":
      print("Correct, continue with the streak")
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
      print("Question 6: It takes 16 seconds for the chug jug in Fortnite Battle Royale?\n")
      print("a: True ")
      print("b: False ")
  
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
  
      print("Question 7: Which planet did Superman come from?\n")
      print("a: Krypton ")
      print("b: Kripton")
      print("c: crypton")
  
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
  
      print("Question 8: In a standard pack of cards, which king is the only one to not have a moustache?\n")
      print("a: king of heart")
      print("b: king of spades")
      print("c: king of clubs")
      print("d: Queen of heart")
      
      # Code defining whether player's input is right or wrong and if right then should he get a point or not
      response = input("What is your answer to this question?") 
      if response == "a":
        print("Correct, don't stop!")
        score += 2
      else:
        print("sorry, but next time")
      score -= 1
      print("your score is {}\n".format(score))
  
      print("Question 9: What is the standard unit of distance in the metric system?\n")
      print("a: meter")
      print("b: kilometer")
      print("c: miles")
      print("d: grams")
  
      # Code defining whether player's input is right or wrong for question 9 and if right he gets a point else loses 1 point
      response = input("What is your answer to this question?\n")
      if response == "a" or response == "b":
        print("Correct, nice job here have a point")
        score += 2
      else:
        print("sorry, next time")
      score -= 1
      print("your score is {}\n".format(score))
  
      # Start of question 10
  
      print("Question 10: What game features the terms love, deuce, match and volley?.\n")
      print("a: Soccer ")
      print("b: basketball")
      print("c: Tennis")
      print("d: badminton-maybe this one")
  
      # Code defining whether player's input is right or wrong for question 10 and if right he gets a point else loses 1 point
      response = input("What is your answer to this question?\n")
      if response == "c":
        print("Correct, nice job here have a point\n\n")
        score += 2
      else:
        print("sorry, next time\n")
      score -= 1
      print('your score is {}'.format(score))
      
      if score>8:
        print('Wow amazing performance try this bonus question!\n\n')
  
      #Stating that if the score is more than 8 then bonus question appears:
      if score>8 :
        print('Bonus Question: What is the abbreviation of our school?')
        print('a: Papa High')
        print("b: Papatoetoe High School")
        print("c: PHS")
        print("d: None of the above\n")
  
      # Code defining whether player's input is right or wrong for question 1 and if right he gets a point else loses 1 point
      if score>8 :
        response = input("What is your answer to this question?\n")
      if response == "c":
        print("Out-standing performance keep it up!\n")
        score += 2
      else:
        print("No worries no one's perfect but we can be perfect\n")
      score -= 1
      print("your Final score is {}!\n\n".format(score))
        
      print("THANKS FOR PLAYING!")
  
      # asking the player's feedback
      PLAYERS_FEEDBACK = input(" Please rate this quiz out of ten and tell us what we could improve on \n")
  
      play_again = input("Do you want to restart? Yes or No\n")
  
      # this code is asking the user if he wants to restart
      if play_again == "Yes" or play_again == "yes":
          exec(open("./Python quiz by Tanish.py").read())
      else:
          exit()
  
  
      print("Great choice\n\n")
    else:
      quit()
  
      
  else:
    # Start of question 6
    print("Question 6: It takes 16 seconds for the chug jug in Fortnite Battle royale?\n")
    print("a: True ")
    print("b: False ")
  
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
  
    print("Question 7: Which planet did Superman come from?\n")
    print("a: Krypton ")
    print("b: Kripton")
    print("c: crypton")
  
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
  
    print("Question 8: In a standard pack of cards, which king is the only one to not have a moustache?\n")
    print("a: king of heart")
    print("b: knig of spades")
    print("c: king of clubs")
    print("d: queen of heart")
      
    # Code defining whether player's input is right or wrong and if right then should he get a point or not
    response = input("What is your answer to this question?\n") 
    if response == "a":
      print("Correct, don't stop!")
      score += 2
    else:
      print("sorry, but next time")
      score -= 1
    print("your score is {}\n".format(score))
  
    # Start of question 9
  
    print("Question 9: What is the standard unit of distance in the metric system?\n")
    print("a: meter ")
    print("b: kilometer")
    print("c: miles")
    print("d: grams")
  
    # Code defining whether player's input is right or wrong for question 9 and if right he gets a point else loses 1 point
    response = input("What is your answer to this question?\n")
    if response == "a" or response == "b":
      print("Correct, nice job here have a point")
      score += 2
    else:
      print("sorry, next time")
    score -= 1
    print("your score is {}\n".format(score))
  
    # Start of question 10
  
    print("Question 10: What game features the terms love, deuce, match and volley?\n")
    print("a: Soccer ")
    print("b: basketball")
    print("c: Tennis")
    print("d: badminton-maybe this one")
  
    # Code defining whether player's input is right or wrong for question 10 and if right he gets a point else loses 1 point
    response = input("What is your answer to this question?\n")
    if response == "c":
      print("Correct, nice job here have a point")
      score += 2
    else:
      print("sorry, next time\n")
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
  



