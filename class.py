class Car:
	def start(self):
		self.state = "driving"

	def stop(self):
			self.state = "stopped"

fiat = Car()

fiat.start()

print(fiat.state)
