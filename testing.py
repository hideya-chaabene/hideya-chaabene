from time import sleep 



class ImAClass:

	def __init__(self, time):

		self.time = time


	def run(self):

		while True:
			print(self.time)
			sleep(self.time)