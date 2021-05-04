#Michael Fontes
#Final Project
#Program is Questionaire with fantasy elements.
#Players goal is to reach the end of the quest before either dying or answereing too mnay questions wrong

import random
import time
import os  #https://stackoverflow.com/questions/4810537/how-to-clear-the-screen-in-python

def welcome():
	print('\n\n\n')
	print("                                  /   \								    ")
	print("                          )      ((   ))     (						    ")
	print("(@)                      /|\      ))_((     /|\						    ")
	print("|-|                     / | \    (/\|/\)   / | \                      (@)")
	print("| | -------------------/--|-voV---\`|'/--Vov-|--\---------------------|-|")
	print("|-|                         '^`   (o o)  '^`                          | |")
	print("| |                               `\Y/'                               |-|")
	print("|-|                                                                   | |")	#https://asciiart.website/index.php?art=creatures/dragons Artwork by: Jeff Ferris
	print("| |                          Trivial Journey                          |-|")
	print("|-|                                                                   | |")
	print("| |                                                                   |-|")
	print("|_|___________________________________________________________________| |")
	print("(@)              l   /\ /         ( (       \ /\   l                `\|-|")
	print("             	l /   V           \ \       V   \ l                  (@)")
	print("                 l/                _) )_          \I						")
	print("                               	  `\ /'								    ")

def rules():
	print('\n\n\n')
	print("Welcome to Trival Journey\n")
	time.sleep(1)
	print("Here are the rules:\n")
	time.sleep(1)
	print("You will recruit 3 crewmates")
	time.sleep(1)
	print('Then you are going to be set off to a journey')
	time.sleep(1)
	print("In this Journey you will encounter strangers")
	time.sleep(1)
	print("these strangers will ask you some tough questions")
	time.sleep(1)
	print('If you answer the question correctly, you will be able to proceed on')
	time.sleep(1)
	print('If do not answer the question correctly...')
	time.sleep(1)
	print('You will have to leave one of your crewmates behind')
	time.sleep(1)
	print('If you lose all your crewmates, your journey ends')
	time.sleep(1)
	print('Lets Start Your Journey!!')
	print('\n')
	input('Press ENTER To Continue')

def what_is_your_name(name):
	print('\n\n')
	name = input('What is your name? ')
	return name

def journey_start():
	print('\n\n')
	print('You are woken up by a soldier who entered your chambers. The soldier')
	time.sleep(1)
	print('explains that the king needs to see you immediately')
	time.sleep(1)
	print('You head to the Kings Court and the King explains that you,',name,'are his most')
	time.sleep(1)
	print('loyal and trusted guards. The King asks you to travel north to the')
	time.sleep(1)
	print('The Mountain of Aplusplus to aquire the Kings Daughter')
	time.sleep(1)
	print('You save your questions and immediately head out on your quest.')
	time.sleep(1)
	print('You travel through the castle to recruit 3 crewmates.')
	time.sleep(1)
	input('Press ENTER To Continue')

def battle_system(playerHealth):

	enemyHealth = 5
	diceRoll = [1 , 2 , 3, 4, 5, 6]
	runDice = [1, 2, 3]
	attackDamage = random.choice(diceRoll)
	runChance = random.choice(runDice)
	print('You encounter an enemy on the road')
	encounter = input('Do you FIGHT or RUN? ').upper()
	time.sleep(1)
	if encounter == "FIGHT":
		print('You chose to fight')
		print('players health: ',playerHealth)
		print('enemies health: ',enemyHealth)
		while not playerHealth >= 1 or enemyHealth >= 1:
			action = input('ATTACK or RUN: ').upper()
			time.sleep(2)
			if action == "ATTACK":
				print('You attack with a slash from your sword')
				time.sleep(1)
				enemyHealth = enemyHealth - attackDamage
				print('Enemy health:', enemyHealth, '\n')
				if enemyHealth < 1:
					print('you successfuly defeated the enemy')
					#print('You recieve', lootCoin,'coin')
					return playerHealth
					break
				time.sleep(2)
				print('Enemy hits back with a hammer smash')
				playerHealth = playerHealth - attackDamage
				print('Player health:', playerHealth, '\n')
				if playerHealth < 1:
					print('The enemy has defeated you')
					print('GAME OVER')
					exit()
					break
			elif action == "RUN":
				if runChance == 1 or runChance == 2:
					print('You have successfully ran away from the fight')
					return playerHealth
					break
				elif runChance == 3:
					print('Enemy blocked your path from running away')
					time.sleep(1)
					print('Enemy delivers a quick strike as you get back to battle position')
					playerHealth = playerHealth - attackDamage
					print('Player Health:', playerHealth)
					continue
			else:
				print('Thats Not A Command')
				print('Please Enter ATTACK or RUN')
				continue
	elif encounter == "RUN":
		print('You ran away from the attack')
		return playerHealth
	else:
		print('You were to incompetent to make a command')
		print('Your Crew Pulls you out of the battle')
		print('The enemy manages to sneak in a sucker punch')
		print('-5 to', name, 'health')
		playerHealth = playerHealth - 5
		return playerHealth

def battle_system_hard(playerHealth):

	enemyHealth = 10
	diceRoll = [1 , 2 , 3, 4, 5, 6]
	runDice = [1, 2, 3]
	attackDamage = random.choice(diceRoll)
	runChance = random.choice(runDice)

	print('You encounter an enemy on the road')
	encounter = input('Do you FIGHT or RUN? ').upper()
	time.sleep(1)
	if encounter == "FIGHT":
		print('You chose to fight')
		print('players health: ',playerHealth)
		print('enemies health: ',enemyHealth)
		while not playerHealth >= 1 or enemyHealth >= 1:
			action = input('ATTACK or RUN: ').upper()
			time.sleep(2)
			if action == "ATTACK":
				print('You attack with a swing of your hammer')
				time.sleep(1)
				enemyHealth = enemyHealth - attackDamage
				print('Enemy health:', enemyHealth, '\n')
				if enemyHealth < 1:
					print('you successfuly defeated the enemy')
					return playerHealth
					break
				time.sleep(2)
				print('Enemy hits back with a hammer smash')
				playerHealth = playerHealth - runChance
				print('Player health:', playerHealth, '\n')
				if playerHealth < 1:
					print('The enemy has defeated you')
					print('GAME OVER')
					exit()
					break
					time.sleep(2)
			elif action == "RUN":
				print(runChance)
				if runChance == 1 or runChance == 2:
					print('You have successfully ran away from the fight')
					return playerHealth
					break
				elif runChance == 3:
					print('Enemy blocked your path from running away')
					time.sleep(1)
					print('Enemy delivers a quick strike as you get back to battle position')
					playerHealth = playerHealth - attackDamage
					print('Player Health:', playerHealth)
					continue
			else:
				print('Thats Not A Command')
				print('Please Enter ATTACK or RUN')
				continue
	elif encounter == "RUN":
		print('You ran away from the attack')
		return playerHealth
	else:
		print('You were to incompetent to make a command')
		print('Your Crew Pulls you out of the battle')
		print('The enemy manages to sneak in a sucker punch')
		print('-5 to', name, 'health')
		playerHealth = playerHealth - 5
		return playerHealth

def quest1(answer):
	attempt = 1
	result = 0
	line = open('quest1.txt').read()
	line = line.splitlines()
	line_choice = random.choice(line)
	line_split = line_choice.split("/")
	question = line_split[0]
	answer = line_split[1].upper()
	answer = answer.rstrip(" ")
	choice1 = line_split[2].upper()
	choice2 = line_split[3].upper()
	choice3 = line_split[4].upper()
	print('You hit your first quest marker.')
	time.sleep(1)
	print('The man you encounter is dressed in rags')
	time.sleep(1)
	print('He looks at you and asks')
	time.sleep(1)
	print('------------------------------------------')
	time.sleep(2.5)
	while attempt != 0:
		print(question)
		print('A.', choice3)
		print('B.', answer)
		print('C.', choice1)
		print('D.', choice2)
		print('-----------------------------------------')
		guess = input('What is your guess stranger?? ').upper()
		time.sleep(2)
		if guess == answer or guess == "B":
			print('\n')
			print('Correct. You May Pass To The Next Town')
			result = "GOOD"
			break
		elif guess != answer:
			print('\n')
			print('Thats wrong mate!')
			print('The correct answer is', answer)
			print('The price to pass is now one of your crewmates')
			print('You can pass to the next town')
			attempt = attempt - 1
			result = "BAD"
			return result
	return result

def quest2(answer):
	attempt = 1
	result = 0
	line = open('quest2.txt').read()
	line = line.splitlines()
	line_choice = random.choice(line)
	line_split = line_choice.split("/")
	question = line_split[0]
	answer = line_split[1].upper()
	answer = answer.rstrip(" ")
	choice1 = line_split[2].upper()
	choice2 = line_split[3].upper()
	choice3 = line_split[4].upper()
	print('You Enter Town')
	time.sleep(1)
	print('You find the quest guardian')
	time.sleep(1)
	print('An Overweight mustache man, dressed dapperly')
	time.sleep(1)
	print('He greets you and asks:')
	time.sleep(1)
	print('-----------------------------------------')
	time.sleep(2.5)
	while attempt != 0:
		print(question)
		print('A.', choice3)
		print('B.', choice2)
		print('C.', choice1)
		print('D.', answer)
		print('-----------------------------------------')
		guess = input('OI! What It be Chap!?? ').upper()
		time.sleep(2)
		if guess == answer or guess == "D":
			print('\n')
			print('Alright...Very Good...You Shall Pass')
			result = "GOOD"
			break
		elif guess != answer:
			print('All Worng Chap!')
			print('The correct answer is', answer)
			print('The price to pass is now one of your crewmates')
			print('You can pass to the next town')
			attempt = attempt - 1
			result = "BAD"
			return result
	return result

def quest3(answer):
	attempt = 1
	result = 0
	line = open('quest3.txt').read()
	line = line.splitlines()
	line_choice = random.choice(line)
	line_split = line_choice.split("/")
	question = line_split[0]
	answer = line_split[1].upper()
	answer = answer.rstrip(" ")
	choice1 = line_split[2].upper()
	choice2 = line_split[3].upper()
	choice3 = line_split[4].upper()
	print("You Enter Myspoint")
	time.sleep(1)
	print('You see a pencil thin man covered in tattoos')
	time.sleep(1)
	print('He grins and you see that his teeth are made of metal')
	time.sleep(1)
	print('He points and gestures to come over to him')
	time.sleep(1)
	print('"Oi Bruv! I am the quest guardian ere. eres the question"')
	time.sleep(1)
	print('------------------------------------------')
	time.sleep(2.5)
	while attempt != 0:
		print(question)
		print('A.', answer)
		print('B.', choice2)
		print('C.', choice1)
		print('D.', choice3)
		print('-----------------------------------------')
		guess = input('Wuts the answer bruv!?? ').upper()
		time.sleep(2)
		if guess == answer or guess == "A":
			print('Waddya know?..You May Pass')
			result = "GOOD"
			break
		elif guess != answer:
			print('Hahahaha no no no...all wrong')
			print('The correct answer is', answer)
			print('The price to pass is now one of your crewmates')
			print('You can pass to the next town')
			attempt = attempt - 1
			result = "BAD"
			return result
	return result

def quest4(answer):
	attempt = 1
	result = 0
	line = open('quest4.txt').read()
	line = line.splitlines()
	line_choice = random.choice(line)
	line_split = line_choice.split("/")
	question = line_split[0]
	answer = line_split[1].upper()
	answer = answer.rstrip(" ")
	choice1 = line_split[2].upper()
	choice2 = line_split[3].upper()
	choice3 = line_split[4].upper()
	print('You enter the Kingdom of Mediocre')
	time.sleep(1)
	print('Immediately you are greeted by the quest guardian')
	time.sleep(1)
	print('A woman who is 9 foot tall, dressed in steel gold armor, stares at you')
	time.sleep(1)
	print('"Well listen here! Answer this question and Ill let you pass"')
	time.sleep(1)
	print('------------------------------------------')
	time.sleep(2.5)
	while attempt != 0:
		print(question)
		print('A.', choice1)
		print('B.', choice2)
		print('C.', answer)
		print('D.', choice3)
		print('-----------------------------------------')
		guess = input('The Amazonian points her blade at you and awaits your answer: ').upper()
		time.sleep(2)
		if guess == answer or guess == "C":
			print('Hmmm....Ill have relay a message to future quest givers to make these questions harder')
			print('You may pass')
			result = "GOOD"
			break
		elif guess != answer:
			print('She swings her sword and with that, a crewmate falls to the ground')
			print('The correct answer is', answer)
			print('The price to pass is now one of your crewmates')
			print('You can pass to the next town')
			attempt = attempt - 1
			result = "BAD"
			return result
	return result

def quest5(answer):
	attempt = 1
	result = 0
	line = open('quest5.txt').read()
	line = line.splitlines()
	line_choice = random.choice(line)
	line_split = line_choice.split("/")
	question = line_split[0]
	answer = line_split[1].upper()
	answer = answer.rstrip(" ")
	choice1 = line_split[2].upper()
	choice2 = line_split[3].upper()
	choice3 = line_split[4].upper()
	print('You Enter Middleton')
	time.sleep(1)
	print('Luckily for you, the quest giver stands out in the open, awaiting you')
	time.sleep(1)
	print('"Oi I heard a lot about you. You are on the quest to Aplusplus"')
	time.sleep(1)
	print('Luckily you are half way there. Just answer this question and you can pass')
	time.sleep(1)
	print('------------------------------------------')
	time.sleep(2.5)
	while attempt != 0:
		print(question)
		print('A.', choice1)
		print('B.', choice2)
		print('C.', answer)
		print('D.', choice3)
		print('-----------------------------------------')
		guess = input('Well! Give Me answer!: ').upper()
		time.sleep(2)
		if guess == answer or guess == "C":
			print('Correct! That was a tough one too!')
			print('Go on through')
			result = "GOOD"
			break
		elif guess != answer:
			print('"Oi! All Wrong"')
			print('The correct answer is', answer)
			print('One of your crewmates gets carried off by a couple of guards')
			print('He screams and begs to be let go...You turn your head in anger')
			print('"You can pass to the next town"')
			attempt = attempt - 1
			result = "BAD"
			return result
	return result

def quest6(answer):
	attempt = 1
	result = 0
	line = open('quest6.txt').read()
	line = line.splitlines()
	line_choice = random.choice(line)
	line_split = line_choice.split("/")
	question = line_split[0]
	answer = line_split[1].upper()
	answer = answer.rstrip(" ")
	choice1 = line_split[2].upper()
	choice2 = line_split[3].upper()
	choice3 = line_split[4].upper()
	print('You enter the Sewers')
	time.sleep(1)
	print('A rat looking man spits at your feet, stopping you dead in your tracks')
	time.sleep(1)
	print('*hacks* "Not another step child"')
	time.sleep(1)
	print('"You answer this and I will let you pass"')
	time.sleep(1)
	print('------------------------------------------')
	time.sleep(2.5)
	while attempt != 0:
		print(question)
		print('A.', choice1)
		print('B.', choice2)
		print('C.', choice3)
		print('D.', answer)
		print('-----------------------------------------')
		guess = input('*spits* Alright...what is it then?? ').upper()
		time.sleep(2)
		if guess == answer or guess == "D":
			print('pff go on through')
			result = "GOOD"
			break
		elif guess != answer:
			print('*hacks* "Awful...No..."*spits* "Wrong!"')
			print('The correct answer is', answer)
			print('The Rat Man unleashes a flemmy spit onto one of your crewmates eyes')
			print('Your crewmate screams in agony and fall to the ground')
			print('The Rat Man wipes his mouth with his dirty sleeve and lets you pass')
			print('The guilt wears on you heavily')
			attempt = attempt - 1
			result = "BAD"
			return result
	return result

def quest7(answer):
	attempt = 1
	result = 0
	line = open('quest7.txt').read()
	line = line.splitlines()
	line_choice = random.choice(line)
	line_split = line_choice.split("/")
	question = line_split[0]
	answer = line_split[1].upper()
	answer = answer.rstrip(" ")
	choice1 = line_split[2].upper()
	choice2 = line_split[3].upper()
	choice3 = line_split[4].upper()
	print('You enter The Swamp')
	time.sleep(1)
	print('A Lizard humanoid stands before you')
	time.sleep(1)
	print('Their claws sharp, their teeth bloodstained')
	time.sleep(1)
	print('It hands you a scroll. When you open it, you read the question')
	print('------------------------------------------')
	time.sleep(2.5)
	while attempt != 0:
		print(question)
		print('A.', choice1)
		print('B.', choice2)
		print('C.', choice3)
		print('D.', answer)
		print('-----------------------------------------')
		guess = input('*speaking in tongues* You assume this lizard human wants an answer: ').upper()
		time.sleep(2)
		if guess == answer or guess == "D":
			print('*Squints* Lizard Human waves you through to the path to your next quest')
			result = "GOOD"
			break
		elif guess != answer:
			print('*UNGODLY SCREECH* The Lizard Human slays one of your crewmates')
			print('The Lizard Human does not give you the answer to the question')
			print('However this thing lets you pass')
			print('You step over your fallen crewmate and proceed')
			attempt = attempt - 1
			result = "BAD"
			return result
	return result

def quest8(answer):
	attempt = 1
	result = 0
	line = open('quest8.txt').read()
	line = line.splitlines()
	line_choice = random.choice(line)
	line_split = line_choice.split("/")
	question = line_split[0]
	answer = line_split[1].upper()
	answer = answer.rstrip(" ")
	choice1 = line_split[2].upper()
	choice2 = line_split[3].upper()
	choice3 = line_split[4].upper()
	print('You Enter The Cave')
	time.sleep(1)
	print('An Orc with one eye stands in front of an army of Orcs')
	time.sleep(1)
	print('It carries a battle axe and is standing in front of the path')
	time.sleep(1)
	print('It hands a piece of old linen with a question written in what you guess is blood')
	print('it reads: ')
	time.sleep(1)
	print('------------------------------------------')
	time.sleep(2.5)
	while attempt != 0:
		print(question)
		print('A.', answer)
		print('B.', choice2)
		print('C.', choice3)
		print('D.', choice1)
		print('-----------------------------------------')
		guess = input('awaiting your answer: ').upper()
		time.sleep(2)
		if guess == answer or guess == "A":
			print('The Orc steps aside and allows you to path ')
			time.sleep(2)
			result = "GOOD"
			break
		elif guess != answer:
			print('The Orc grins, exposing his blackstained teeth')
			print('He unleashes a roar as he swings his axe')
			print('You see one of your crewmates fall')
			print('You now know that circumstances are becoming more serious')
			print('You step over your fallen crewmate and proceed')
			print('You realize the orc never gave you the answer to the question')
			print('At this point, you could not care less, you just focus on getting to the end')
			attempt = attempt - 1
			result = "BAD"
			return result
	return result

def quest9(answer):
	attempt = 1
	result = 0
	line = open('quest9.txt').read()
	line = line.splitlines()
	line_choice = random.choice(line)
	line_split = line_choice.split("/")
	question = line_split[0]
	answer = line_split[1].upper()
	answer = answer.rstrip(" ")
	choice1 = line_split[2].upper()
	choice2 = line_split[3].upper()
	choice3 = line_split[4].upper()
	print('You enter the Temple that leads to the mountain of Aplusplus')
	time.sleep(1)
	print('A Wizard stands behind an alchemy table and glares at you')
	time.sleep(1)
	print('He lifts his staff and says')
	time.sleep(1)
	print('Answer this question my child and you shall pass')
	time.sleep(1)
	print('------------------------------------------')
	time.sleep(2.5)
	while attempt != 0:
		print(question)
		print('A.', answer)
		print('B.', choice2)
		print('C.', choice3)
		print('D.', choice1)
		print('-----------------------------------------')
		guess = input('The Wizard Stands In The Way of Your Path and Awaits for an answer: ').upper()
		time.sleep(2)
		if guess == answer or guess == "A":
			print('The Wizard steps aside and points at a cavern wall with his magic staff')
			print('A path is revealed and you travel onwards')
			result = "GOOD"
			break
		elif guess != answer:
			print('The Wizard points his staff at one of your crewmates')
			print('Before your eyes, one of your crewmates is reduced to ash')
			print('The Wizard reveals a path that leads to your final quest')
			print('You only feel awful as you proceed.')
			attempt = attempt - 1
			result = "BAD"
			return result
	return result

def final_quest(answer):
	attempt = 1
	result = 0
	line = open('quest10.txt').read()
	line = line.splitlines()
	line_choice = random.choice(line)
	line_split = line_choice.split("/")
	question = line_split[0]
	answer = line_split[1].upper()
	answer = answer.rstrip(" ")
	choice1 = line_split[2].upper()
	choice2 = line_split[3].upper()
	choice3 = line_split[4].upper()
	print('You Enter the mountain of Aplusplus')
	time.sleep(1)
	print('You see the Kings Daughter chained to a wall behind a Dragon')
	time.sleep(1)
	print('the Dragon awaits for you, It rests atop treasures ')
	time.sleep(1)
	print('The dragon speaks, "If you answer this final question correctly...You may have all the gold in this mountain"')
	time.sleep(1)
	print('"I will also allow you to have the Kings Daughter as Well"')
	time.sleep(1)
	print('The Dragon gets as close as it can get to your face...breathing hot smoke onto you. ')
	time.sleep(1)
	print('------------------------------------------')
	time.sleep(2.5)
	while attempt != 0:
		print(question)
		print('A.', answer)
		print('B.', choice2)
		print('C.', choice3)
		print('D.', choice1)
		print('-----------------------------------------')
		guess = input('It awaits your answer: ').upper()
		time.sleep(2)
		if guess == answer or guess == "A":
			print('The Dragon Roars, It spreads its wings and flys out of the mountain')
			print('You watch as it dissapears into the clouds, never to be seen again')
			print('You rejoice and start collecting as much treasure as you possibly can')
			print('You grab the Kings Daughter and start heading back to the Kingdom')
			result = "GOOD"
			break
		elif guess != answer:
			print('The Dragon lifts its head back and you opens its mouth')
			print('you Watch as a Ball of fire forms from the dragons mouth')
			print('The dragon spits the ball of inferno on to you and your crew')
			print('Everyone is reduced to ashes. The Dragon Smiles and lays back down in his bed of treasure')
			attempt = attempt - 1
			result = "BAD"
			time.sleep(3)
			print('The Quest Ends for You Here')
			time.sleep(1)
			result = "BAD"
			return result
	return result

####### Variables ###########
name = 0
coin = [3 , 5 , 10]
quest1Answer = 0
result = 0
totalmates = 3
playerHealth = 10
playerCoin = 0
score = 0
buy = 0
lootCoin = random.choice(coin)

##### GAME BOOT ###########
os.system('cls')
time.sleep(1)
welcome()

time.sleep(2)
rules()
name = what_is_your_name(name).upper()
journey_start()
time.sleep(2)

#Easy Difficulty for early quests
print('\nYou travel onwards to your first quest!')
time.sleep(1)
print('\n\n')
input('You enter the Poor Kingdom of Dyrt\nPress ENTER to Enter Dyrt')
print('\n')
time.sleep(1)
result = quest1(quest1Answer)
if result == "GOOD":
	score = score + 1
elif result == "BAD":
	totalmates = totalmates - 1
	print(totalmates,"remain in the party")
time.sleep(2)

#Second Quest - Easy
#Battle Introduced
#Battles - 1
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('You travel onward to the next quest')
time.sleep(1)
print('\n')
print('><!<>!<>!<>!<>!<>!<>!<>!<>!<>!<>!<>')
playerHealth = battle_system(playerHealth)
print('You recieve', lootCoin,'coin')
playerCoin = playerCoin + lootCoin
print(name,'Health =', playerHealth)
print(name, 'has', playerCoin, 'coins\n')
time.sleep(2)

input('You see the Port Kingdom of Whet Puul\nPress ENTER to Enter Whet Puul')
print('\n')
result = quest2(quest1Answer)
if result == "GOOD":
	score = score + 1
elif result == "BAD":
	totalmates = totalmates - 1
	print(totalmates,"remain in the party")
time.sleep(2)

#Thrid Quest - Easy
#Battles - 1
#Introduction to Shop
#Shop - Cheap Prices
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('You travel onward to the next quest')
time.sleep(1)
print('\n')
print('><!<>!<>!<>!<>!<>!<>!<>!<>!<>!<>!<>')
playerHealth = battle_system(playerHealth)
print('You recieve', lootCoin,'coin')
playerCoin = playerCoin + lootCoin
print(name,'Health =', playerHealth)
print(name, 'has', playerCoin, 'coins\n')
time.sleep(2)

input('You see the Crooked Looking Kingdom of Myspoint\nPress ENTER to Enter Myspoint')
print('\n')

################## Shop 1 #############################
print('You See a Traveling Merchant')
print('You have the choice to buy from the Merchant or Continue on your journey')
move = input('What is your decision? BUY or CONTINUE ').upper()
if move == "BUY":
	print('You speak to the Merchant')
	print('He asks "What you like to buy?"')
	print('HEALTH - 5 Coin')
	print('HIRE CREWMATE - 15 Coin')
	print('LEAVE')
	while buy != "LEAVE":
		buy = input('What you buying (HEALTH/HIRE/LEAVE)').upper()
		if buy == "HEALTH":
			if playerCoin < 5:
				print('You do not have enough')
				continue
			else:
				playerHealth = playerHealth + 5
				playerCoin = playerCoin - 5
				print('You add +5 to your health')
				time.sleep(1)
				print('You currently have', playerCoin, 'coin left')
				print('Your Health: ', playerHealth)
		elif buy == "HIRE":
			if playerCoin < 15:
				print('You do not have enough')
				continue
			else:
				totalmates = totalmates + 1
				playerCoin = playerCoin - 15
				print('You added +1 to your crew')
				print('You currently have', playerCoin, 'coin left')
				print('Crew = ', totalmates)
		elif buy == "LEAVE":
			print('Have A Nice Day!')
			break
		else:
			print('Not Sure If thats for sale')
			continue
elif move == "CONTINUE":
	print('You move on')
################# End OF Shop ######################################

result = quest3(quest1Answer)
if result == "GOOD":
	score = score + 1
elif result == "BAD":
	totalmates = totalmates - 1
	print(totalmates,"remain in the party")
time.sleep(2)

#Fourth quest - Intermidiate
#No Battles
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('You travel onward to the next quest')
time.sleep(1)

input('You see the Average Looking Kingdom of Mediocre\nPress ENTER to Enter Mediocre')
print('\n')
result = quest4(quest1Answer)
if result == "GOOD":
	score = score + 1
elif result == "BAD":
	totalmates = totalmates - 1
	if totalmates == 0:
		print('Game Over')
		exit()
	print(totalmates,"remain in the party")
time.sleep(2)

#Fifth Quest - Intermidiate
#No Battles
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('You travel onward to the next quest')
time.sleep(1)
input('You see the Kingdom of Middleton\nPress ENTER to Enter Middleton')
print('\n')
result = quest5(quest1Answer)
if result == "GOOD":
	score = score + 1
elif result == "BAD":
	totalmates = totalmates - 1
	if totalmates == 0:
		print('Game Over')
		exit()
	print(totalmates,"remain in the party")
time.sleep(2)

#Sixth Quest - Hard
#Battles -2
#Shop - Cheap
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('You travel onward to the next quest')
time.sleep(1)
print('\n')
print('><!<>!<>!<>!<>!<>!<>!<>!<>!<>!<>!<>')
playerHealth = battle_system(playerHealth)
print('You recieve', lootCoin,'coin')
playerCoin = playerCoin + lootCoin
print(name,'Health =', playerHealth)
print(name, 'has', playerCoin, 'coins')
time.sleep(2)

print('You continue on the path to the Next Destination')
time.sleep(1)
print('To your dismay, you see more enemies ahead')
time.sleep(1)
print('These enemies, however, look tougher.')
print('\n')
print('><!<>!<>!<>!<>!<>!<>!<>!<>!<>!<>!<>')
playerHealth = battle_system_hard(playerHealth)
print('You recieve', lootCoin,'coin')
playerCoin = playerCoin + lootCoin
print(name,'Health =', playerHealth)
print(name, 'has', playerCoin, 'coins')
time.sleep(2)

input('You see signs that point to a Sewer\nPress ENTER to Enter The Sewer Kingdom')
print('\n')

############## SHOP 2 #########################
print('You See a Traveling Lizard Merchant')
print('You have the choice to buy from the Merchant or Continue on your journey')
move = input('Whatssss isssss your decissssion? PURCHASE or ESCAPE ').upper()
if move == "PURCHASE":
	print('You speak to the Merchant')
	print('He asks "What you like to Purchase?"')
	print('HEALTH - 5 Coin')
	print('HIRE CREWMATE - 15 Coin')
	print('LEAVE')
	while buy != "LEAVE":
		buy = input('What you buying (HEALTH/HIRE/LEAVE)').upper()
		if buy == "HEALTH":
			if playerCoin < 5:
				print('You do not have enough')
				continue
			else:
				playerHealth = playerHealth + 5
				playerCoin = playerCoin - 5
				print('You add +5 to your health')
				time.sleep(1)
				print('You currently have', playerCoin, 'coin left')
				print('Your Health: ', playerHealth)
		elif buy == "HIRE":
			if playerCoin < 15:
				print('You do not have enough')
				continue
			else:
				totalmates = totalmates + 1
				playerCoin = playerCoin - 15
				print('You added +1 to your crew')
				print('You currently have', playerCoin, 'coin left')
				print('Crew = ', totalmates)
		elif buy == "LEAVE":
			print('Ssssee you around!')
			break
		else:
			print('Not Sure If thats for sale')
			continue
elif move == "ESCAPE":
	print('You escape from the shady merchant')
################# End OF Shop ######################################

result = quest6(quest1Answer)
if result == "GOOD":
	score = score + 1
elif result == "BAD":
	totalmates = totalmates - 1
	if totalmates == 0:
		print('Game Over')
		exit()
	print(totalmates,"remain in the party")
time.sleep(2)

#Seventh Quest - Intermidiate
#No Battles
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('You travel onward to the next quest')
time.sleep(1)
input('You head out of the Sewer Kingdom and You are led to a Swamp\nPress ENTER to Enter The Swamp')
print('\n')
result = quest7(quest1Answer)
if result == "GOOD":
	score = score + 1
elif result == "BAD":
	totalmates = totalmates - 1
	if totalmates == 0:
		print('Game Over')
		exit()
	print(totalmates,"remain in the party")
time.sleep(2)

#Eighth Quest - Hard
#Battles - 2
#Shop - Middle Price
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('You travel onward to the next quest')
time.sleep(1)
print('\n')
print('><!<>!<>!<>!<>!<>!<>!<>!<>!<>!<>!<>')
playerHealth = battle_system_hard(playerHealth)
print('You recieve', lootCoin,'coin')
playerCoin = playerCoin + lootCoin
print(name,'Health =', playerHealth)
print(name, 'has', playerCoin, 'coins')
time.sleep(2)

print('The Lizard enemies seem to be strong against your attacks')
time.sleep(1)
print('You see more up ahead and you hope that you overcome the challenge')
time.sleep(1)
print('\n')
print('><!<>!<>!<>!<>!<>!<>!<>!<>!<>!<>!<>')
playerHealth = battle_system(playerHealth)
print('You recieve', lootCoin,'coin')
playerCoin = playerCoin + lootCoin
print(name,'Health =', playerHealth)
print(name, 'has', playerCoin, 'coins')
time.sleep(2)

input('You trod out of the Swamp and find yourself standing in front of a cave\nPress ENTER to Enter the Cave')
print('\n')

###############  Shop 3  ###################################
print('You See a Traveling Orc Merchant')
print('You have the choice to buy from the Merchant or Continue on your journey')
move = input('What is your decision? SPEND or WALK ').upper()
if move == "SPEND":
	print('You speak to the Merchant')
	print('He asks "What you like to buy?"')
	print('HEALTH - 10 Coin')
	print('HIRE CREWMATE - 25 Coin')
	print('LEAVE')
	while buy != "LEAVE":
		buy = input('What you buying (HEALTH/HIRE/LEAVE)').upper()
		if buy == "HEALTH":
			if playerCoin < 10:
				print('You do not have enough')
				continue
			else:
				playerHealth = playerHealth + 5
				playerCoin = playerCoin - 10
				print('You add +5 to your health')
				time.sleep(1)
				print('You currently have', playerCoin, 'coin left')
				print('Your Health: ', playerHealth)
		elif buy == "HIRE":
			if playerCoin < 25:
				print('You do not have enough')
				continue
			else:
				totalmates = totalmates + 1
				playerCoin = playerCoin - 25
				print('You added +1 to your crew')
				print('You currently have', playerCoin, 'coin left')
				print('Crew = ', totalmates)
		elif buy == "LEAVE":
			print('LEAVE HUMAN')
			break
		else:
			print('Not Sure If thats for sale')
			continue
elif move == "WALK":
	print('You move on')
################# End OF Shop ######################################

result = quest8(quest1Answer)
if result == "GOOD":
	score = score + 1
elif result == "BAD":
	totalmates = totalmates - 1
	if totalmates == 0:
		print('Game Over')
		exit()
	print(totalmates,"remain in the party")
time.sleep(2)

#Ninth Quest
#Battles - 1
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('You travel onward to the next quest')
time.sleep(1)
print('\n')
print('><!<>!<>!<>!<>!<>!<>!<>!<>!<>!<>!<>')
playerHealth = battle_system_hard(playerHealth)
print(name,'Health =', playerHealth)
print('You recieve', lootCoin,'coin')
playerCoin = playerCoin + lootCoin
print(name, 'has', playerCoin, 'coins')
time.sleep(2)

input('You find light within the cave and it leads you to a Temple\nPress ENTER to Enter the Temple')
print('\n')
result = quest9(quest1Answer)
if result == "GOOD":
	score = score + 1
elif result == "BAD":
	totalmates = totalmates - 1
	if totalmates == 0:
		print('Game Over')
		exit()
	print(totalmates,"remain in the party")
time.sleep(2)

#Final Quest - Hard
#No Battles
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('You travel onward to the mountain of Aplusplus')

time.sleep(1)
input('You see the entrance to Mount Aplusplus\nPress ENTER to Enter the Mountain')
print('\n')
result = final_quest(quest1Answer)
if result == "GOOD":
	score = score + 1
elif result == "BAD":
	print('GAME OVER')
	input('Press ENTER to Exit')
	exit()
time.sleep(2)

########## ENDINGS #################
#https://stackoverflow.com/questions/47188473/python-how-to-make-an-if-statement-between-x-and-y
#Resource I used to figure out how to do an in between number
if score <= 3:
	print('Although You were to solve your way through the quest barely')
	time.sleep(1)
	print('you manage to make it out with the princess')
	time.sleep(1)
	print('On the adventure back, the guilt of all your fallen crewmates wears on you')
	time.sleep(1)
	print('You slowly let the guilt take over and spiral into madness')
	time.sleep(1)
	print('You decide to live the rest of your days in the Swamp')
	time.sleep(1)
	print('As for the princess')
	time.sleep(1)
	print('....')
	time.sleep(1)
	print('Lets say the princess never returned and the Lizard People of the Swamp ate well that day')
	time.sleep(1)
	print('You Have Recieved the Bad Ending for this quest')
	time.sleep(1)
	print('Play Again and Try to see the True Ending')
	time.sleep(1)
	input('Press ENTER to Exit')
	exit()
elif 4 <= score <= 7:
	print('You manage to collect as much treaure as possible in your traveling bag')
	time.sleep(1)
	print('You then escape with the princess and head off to the kingdom')
	time.sleep(1)
	print('The King awards you with a promotion to General and a room of your own within the castle')
	time.sleep(1)
	print('Although you should feel happy for your accomplishments')
	time.sleep(1)
	print('You cannot help but notice that some soldiers look at you with certain disapproval')
	time.sleep(1)
	print('You question to yourself if you deserved all the reward for a quest that you barely made through')
	time.sleep(1)
	print('You spend the rest of your life trying to seek approval and respect from other soldiers')
	time.sleep(1)
	print('A task that is never achieved in your lifetime')
	time.sleep(1)
	print('You Have Recieved the Mediocre Ending for this quest')
	time.sleep(1)
	print('Play Again and Try to see the True Ending')
	time.sleep(1)
	input('Press ENTER to Exit')
	exit()
elif 8 <= score <= 10:
	print('You Grab the Dragon as it tries to fly away and slay it')
	time.sleep(1)
	print('You look over at your crewmates and they cheer and howl')
	time.sleep(1)
	print('The Princess could not thank you enough and is impressed by your intelligence and strength')
	time.sleep(1)
	print('As you return to the Kingdom, News has spread and people start showering you with gifts')
	time.sleep(1)
	print('The King declares a feast in your honor')
	time.sleep(1)
	print('You get your own kingdom and life is good')
	time.sleep(1)
	print('Congrat! You Got the Best Ending')
	time.sleep(1)
	input('Press ENTER to Exit')
	exit()
