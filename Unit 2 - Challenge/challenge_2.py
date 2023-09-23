#create a class called Player
class Player:

	def play(self):
		print("The player is playing cricket.")

class Batsman(Player):

	def play(self):
		print("The batsman is batting.")

class Bowler(Player):

	def play(self):
		print("The  bowler is bowling.")
#create two object called batsman and bowler
batsman = Batsman()
bowler = Bowler()
#call object and function or method
batsman.play()
bowler.play()
