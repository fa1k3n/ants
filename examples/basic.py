from ants import worker

if __name__ == '__main__':
	i = 0
	@worker
	def test():
		global i
		print("Hello world")
		i += 1

	test.start()

	while i < 5:
		pass
		
	test.stop()