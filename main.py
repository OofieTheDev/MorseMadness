import random
import sys
import string
from colorama import Fore
import os
import textwrap

class Morse:
	MORSE = {
		'a':'.-',
		'b':'-...',
		'c':'-.-.',
		'd':'-..',
		'e':'.',
		'f':'..-.',
		'g':'--.',
		'h':'....',
		'i':'..',
		'j':'.---',
		'k':'-.-',
		'l':'.-..',
		'm':'--',
		'n':'-.',
		'o':'---',
		'p':'.--.',
		'q':'--.-',
		'r':'.-.',
		's':'...',
		't':'-',
		'u':'..-',
		'v':'...-',
		'w':'.--',
		'x':'-..-',
		'y':'-.--',
		'z':'--..'
	}	
	OPTIONS = ("Name the Dots/Slashes", "Name the Alphabet")	
	NO = (1, 2)	
	GUIDE = "\nNOTE: ONLY DOTS AND DASHES SHOULD BE USED IF YOU SELECT OPTION 2\n"

	def __init__(self):
		self.choice = None
		self.points = 0
		self.reOrdered = None
		self.currentQn = 1

	def startMenu(self):
		self.currentQn = 1

		print(Fore.CYAN + textwrap.dedent("""
		███╗░░░███╗░█████╗░██████╗░░██████╗███████╗  ███╗░░░███╗░█████╗░██████╗░███╗░░██╗███████╗░██████╗░██████╗
		████╗░████║██╔══██╗██╔══██╗██╔════╝██╔════╝  ████╗░████║██╔══██╗██╔══██╗████╗░██║██╔════╝██╔════╝██╔════╝
		██╔████╔██║██║░░██║██████╔╝╚█████╗░█████╗░░  ██╔████╔██║███████║██║░░██║██╔██╗██║█████╗░░╚█████╗░╚█████╗░
		██║╚██╔╝██║██║░░██║██╔══██╗░╚═══██╗██╔══╝░░  ██║╚██╔╝██║██╔══██║██║░░██║██║╚████║██╔══╝░░░╚═══██╗░╚═══██╗
		██║░╚═╝░██║╚█████╔╝██║░░██║██████╔╝███████╗  ██║░╚═╝░██║██║░░██║██████╔╝██║░╚███║███████╗██████╔╝██████╔╝
		╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚═╝╚═════╝░╚══════╝  ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚══╝╚══════╝╚═════╝░╚═════╝░
		"""))

		print(Fore.YELLOW + textwrap.dedent("""
		█▄▄ █▄█   █▀█ █▀█ █▀▀ █ █▀▀ ▀█▀ █░█ █▀▀ █▀▄ █▀▀ █░█
		█▄█ ░█░   █▄█ █▄█ █▀░ █ ██▄ ░█░ █▀█ ██▄ █▄▀ ██▄ ▀▄▀
	  	"""))

		for n, o in enumerate(Morse.OPTIONS, start=1):
			print(Fore.LIGHTMAGENTA_EX + f"{n}. {o}")
	
		print(Morse.GUIDE)
		choice = int(input(Fore.YELLOW + "Enter your choice: "))
		self.validateChoice(choice)

	def validateChoice(self, choice):
		if choice in Morse.NO:
			self.choice = choice
			self.initialize()
			self.startGame()
		else:
			print(Fore.RED + "Invalid choice, program terminating.")
			sys.exit(1)
	
	def validateAns(self, ans):
		if self.choice == 1:
			if self.sanitize(ans) not in string.ascii_lowercase:
				print(Fore.RED + "Invalid option, program terminating.")
				sys.exit(1)
			else:
				return ans	
		if self.choice == 2:
			if "." in ans or "-" in ans:
				return ans
			else:
				print(Fore.RED + "Invalid option, program terminating.")
				sys.exit(1)

	def startGame(self):
		if self.choice == 1:
			for key, value in self.reOrdered.items():
				print(Fore.MAGENTA + "\n" + str(self.currentQn) + "/26")
				print(Fore.YELLOW + f"\nWhat alphabet is this?\n{value}")
				ans = self.validateAns(input("Answer: "))
				if self.sanitize(ans) == key:
					self.points += 1
					print(Fore.GREEN + "\nCorrect answer! Next question...\n")
				else:
					print(Fore.RED + f"\nIncorrect answer! The answer is {key}\n")
				self.currentQn += 1	
			self.endGame()

		if self.choice == 2:
			for key, value in self.reOrdered.items():
				print(Fore.MAGENTA + "\n" + str(self.currentQn) + "/26")
				print(Fore.YELLOW + f"\nWhat is the morse representation of {key}?\n")
				ans = self.validateAns(input("Answer: "))
				if self.sanitize(ans) == value:
					self.points += 1
					print(Fore.GREEN + "\nCorrect answer! Next question...\n")
				else:
					print(Fore.RED + f"\nIncorrect answer! The answer is {value}\n")
				self.currentQn += 1	
		self.endGame()

		if self.choice not in Morse.NO:
			print(Fore.RED + "Invalid option, program terminating.")
			sys.exit(1)

	def endGame(self):
		print(Fore.CYAN + """
		░██████╗░░█████╗░███╗░░░███╗███████╗  ██╗░░██╗░█████╗░░██████╗  ███████╗███╗░░██╗██████╗░███████╗██████╗░
		██╔════╝░██╔══██╗████╗░████║██╔════╝  ██║░░██║██╔══██╗██╔════╝  ██╔════╝████╗░██║██╔══██╗██╔════╝██╔══██╗
		██║░░██╗░███████║██╔████╔██║█████╗░░  ███████║███████║╚█████╗░  █████╗░░██╔██╗██║██║░░██║█████╗░░██║░░██║
		██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░  ██╔══██║██╔══██║░╚═══██╗  ██╔══╝░░██║╚████║██║░░██║██╔══╝░░██║░░██║
		╚██████╔╝██║░░██║██║░╚═╝░██║███████╗  ██║░░██║██║░░██║██████╔╝  ███████╗██║░╚███║██████╔╝███████╗██████╔╝
		░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝  ╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░  ╚══════╝╚═╝░░╚══╝╚═════╝░╚══════╝╚═════╝░
		""")
		print(Fore.YELLOW + f"\nResult: {self.points}/26")
		cont = input("Would you like to play again? y/n: ")
		if self.sanitize(cont) == "y":
			os.system("cls")
			self.reset()
			self.startMenu()
		if self.sanitize(cont) == "n":
			sys.exit(1)
	
	def initialize(self):
		l = list(Morse.MORSE.items())
		random.shuffle(l)
		self.reOrdered = dict(l)	
		
	def reset(self):
		self.__init__()

	@staticmethod
	def sanitize(target):
		return target.lower().strip()

m = Morse()
m.startMenu()