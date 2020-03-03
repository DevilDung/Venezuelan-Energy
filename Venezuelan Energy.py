import time
import random
import os

loop = 1

random_facts = [['85% of the power from Guri is supplied by 3 main 765 kilovolt lines connecting to other substations.', '73% of the power in Venezuela comes from the Guri hydroelectric plant.'],[],[]]

print('Welcome to my history project, Venezuelan Energy. There was recently a huge power outage in Venezuela due to a malfunctioning dam called the Guri Dam. In this game, you play either a electrician trying to fix the broken hydroelectric turbines or a local resident who is trying to get water because they don\'t have running water.')
time.sleep(3)

while loop > 0:
  player_character = input('So, do you want to be the electrician or a local resident?\n').lower()

  if 'electrician' in player_character:
    print('You chose electrician.')
    time.sleep(1)
    print('There was vegetation fire, impacting three 765 kilovolt lines that connected the main hydroelectric plant Guri to 2 other substations! The lines and the towers that support these lines were covered with vegetation because it has not been maintained for years.')
    time.sleep(4)
    print('These wires overheated and impacted 3 turbines. The turbines shut down and had to be started over. But because 4 others had already shut down because of bad maintenance, it caused a destabilization, which caused the Guri Turbine Control System not to adjust the speed. This caused one of the turbines to accelerate and they had to stop all the turbines, and in doing that one of the turbine\'s internal wiring sizzled and fizzed out.')
    time.sleep(4)
    print('Work to fix the turbine!')
    time.sleep(1)
    print ('''
    _______________
    -------* *-----
    ''')
    answer = False
    while answer == False:
      tool = input('There seems to be a break in Wire 3. Which tool do you use to fix the wire- a sheet of impregnated reinforcement, wiring glue or a soldering iron?\n')
      if 'soldering' in tool:
        answer = True
        print('Correct!')
      else:
        print('Wrong! Here\'s a fun fact: ' + random.choice(random_facts[0]))
    print('Good work. Now that the generator is working, you crank the manual hard restart, and the turbine starts working again.')
    input('Thanks for playing! Press enter to play again.')

  elif 'resident' in player_character:
    print('You chose a local resident.')
    time.sleep(0.5)
    tunnel_water = 1
    friend_water = 1
    police_water = 2
    print('You are having trouble finding water because there is no running water at home.')
    time.sleep(1)
    are = 1
    while are == 1:
      print('Today is Monday. You must find water until the power outage ends on Wednesday and your runnning water comes back. You need at least 3 gallons of water a day.')
      time.sleep(1)
      water_spot = input('Do you want to go to the water spout in the underground tunnel, ask a friend for water, or go to the town square where you know police will hand out water?\n')
      if 'tunnel' in water_spot or 'spout' in water_spot:
        print('You drive 2 miles to the tunnel. In the tunnel, you find water cascading out of a spout. You brought three 1-gallon plastic containers. But because the water is shooting out of the spout super fast, one of the containers cracks, and the water leaks out. Now you only have 2 containers of water, but luckily someone driving by lends you a hand and a 1- gallon container.')
        time.sleep(4)
        print('As you fill up the final container, you notice the water isn\'t coming out as fast, until finally there\'s no water coming out of the spout anymore. But no worries, your containers are full.')
        time.sleep(3)
        tunnel_water -= 1
        are = 0
      elif 'friend' in water_spot:
        print('You go over to your friend Max\'s house. You knock on his door. He welcomes you. You ask for as much water as he has, and he says that he only has 3 gallons to spare. Perfect, you think.')
        time.sleep(1)
        friend_water -= 1
        are = 0
      elif 'police' in water_spot or 'square' in water_spot:
        print('You go to the town square in the morning, where the local police are handing out water.')
        time.sleep(1)
        print('You observe that there is a long line. Lots of people are in the same situation as you.')
        time.sleep(1)
        print('When you get to the front of the line, it is already late in the afternoon. You fill up three 1-gallon containers of water and go home.')
        time.sleep(1)
        police_water -= 1
        are = 0
    print('You were able to find water today.')
    time.sleep(1)
    print('Good morning! Today is Tuesday.')
    are = 1
    while are == 1:
      time.sleep(1)
      water_spot = input('Do you want to go to the water spout in the underground tunnel, ask a friend for water, or go to the town square where you know police will hand out water?\n')
      if 'tunnel' in water_spot or 'spout' in water_spot:
        if tunnel_water > 0:
          print('You drive 2 miles to the tunnel. In the tunnel, you find water cascading of a spout. You brought three 1-gallon plastic containers. But because the water is shooting out of the spout super fast, one of the containers cracks, and the water leaks out. Now you only have 2 containers of water, but luckily someone driving by lends you a hand and a 1- gallon container.')
          time.sleep(4)
          print('As you fill up the final container, you notice the water isn\'st coming out as fast, until finally there\'s no water coming out of the spout anymore. But no worries, your containers are full.')
          time.sleep(3)
          tunnel_water -= 1
          are -= 1
        else:
          print('Remember, the water from the tunnel ran out yesterday!')
      elif 'friend' in water_spot:
        if friend_water > 0:
          print('You go over to your friend Max\'s house. You knock on his door. He welcomes you. You ask for as much water as he has, and he says that he only has 3 gallons to spare. Perfect, you think.')
          time.sleep(1)
          friend_water -= 1
          are -= 1
        else:
          print('Remember, Max has no more water to spare!')
      elif 'police' in water_spot or 'square' in water_spot:
        if police_water == 1:
          print('You go to the town square in the morning, where the local police are handing out water.')
          time.sleep(1)
          print('You observe that there is a long line. Lots of people are in the same situation as you.')
          time.sleep(1)
          print('When you get to the front of the line, it is already late in the afternoon. You fill up three 1-gallon containers of water and go home. But as you are leaving, you hear shouts behind you. It seems like the police have run out of water!')
          time.sleep(1)
          police_water -= 1
          are -= 1
        else:
          print('You go to the town square in the morning, where the local police are handing out water.')
          time.sleep(1)
          print('You observe that there is a long line. Lots of people are in the same situation as you.')
          time.sleep(1)
          print('When you get to the front of the line, it is already late in the afternoon. You fill up three 1-gallon containers of water and go home.')
          time.sleep(1)
          police_water -= 1
          are -= 1
      else:
        are = 1

    print ('You found water today too! Hooray! Just one more day.')
    time.sleep(1)
    print('Good morning! Today is Wednesday.')
    are = 1
    while are == 1:
      time.sleep(1)
      water_spot = input('Do you want to go to the water spout in the underground tunnel, ask a friend for water, or go to the town square where you know police will hand out water?\n')
      if 'tunnel' in water_spot or 'spout' in water_spot:
        if tunnel_water > 0:
          print('You drive 2 miles to the tunnel. In the tunnel, you find water cascading out of a spout. You brought three 1-gallon plastic containers. But because the water is shooting out of the spout super fast, one of the containers cracks, and the water leaks out. Now you only have 2 containers of water, but luckily someone driving by lends you a hand and a 1- gallon container.')
          time.sleep(2)
          print('As you fill up the final container, you notice the water isn\'st coming out as fast, until finally there\'s no water coming out of the spout anymore. But no worries, your containers are full.')
          time.sleep(2)
          tunnel_water -= 1
          are = 0
        else:
          print('Remember, the water from the tunnel ran out!')
      elif 'friend' in water_spot:
        if friend_water > 0:
          print('You go over to your friend Max\'s house. You knock on his door. He welcomes you. You ask for as much water as he has, and he says that he only has 3 gallons to spare. Perfect, you think.')
          time.sleep(1)
          friend_water -= 1
          are = 0
        else:
          print('Remember, Max has no more water to spare!')
      elif 'police' in water_spot or 'square' in water_spot:
        if police_water > 0:
          if police_water == 1:
            print('You go to the town square in the morning, where the local police are handing out water.')
            time.sleep(1)
            print('You observe that there is a long line. Lots of people are in the same situation as you.')
            time.sleep(1)
            print('When you get to the front of the line, it is already late in the afternoon. You fill up three 1-gallon containers of water and go home. But as you are leaving, you hear shouts behind you. It seems like the police have run out of water!')
            time.sleep(1)
            police_water -= 1
            are -= 1
          else:
            print('You go to the town square in the morning, where the local police are handing out water.')
            time.sleep(1)
            print('You observe that there is a long line. Lots of people are in the same situation as you.')
            time.sleep(1)
            print('When you get to the front of the line, it is already late in the afternoon. You fill up three 1-gallon containers of water and go home.')
            time.sleep(1)
            police_water -= 1
            are = 0
        else:
          print('Remember, the police ran out of water yesterday!')
      else:
        are = 1
    print('Good work! You got water for all three days!')
    time.sleep(1)
    input('Thanks for playing! Press enter to run again.')
  else:
    print ('Huh?')
  

