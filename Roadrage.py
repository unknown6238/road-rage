import random

class Road():
	def __init__(self, length = 1000,curve = 0):
		self.length = length
		self.curve = curve

	def road_loop(self , car_list, car, next_car):
		if next_car.position[0] - 5 < 6:
			print("Next car position < 6: ", next_car.position)
			print("Next car bumper < 6: ", next_car.position[0] - 5)
			car.position[0] = 1000
			car.speed = 0
		else:
			car.position[0] -= 1000
			print("Car list in road loop else before pop: ", car_list[0].position, car_list[1].position, car_list[2].position)
			car_list.insert(0,car_list.pop())
			print("Car list in road loop else after pop: ", car_list[0].position, car_list[1].position, car_list[2].position)
			car.change_speed()
			car.collision_check(next_car)
		print("Car list car 1: ", car_list[0].position)
		return car_list

class Car():
	def __init__(self, position, max_speed = 33.3, length = 5, speed = 10):
		self.length = length
		self.position = position
		self.bumper = self.position[0] - 5
		self.max_speed = max_speed
		self.speed = speed
		self.accel = 2


	def __str__(self):
		"I'm at position {}".format(self.position)


	def change_speed(self):
		if random.randint(1,10) == 7:
			self.speed -= self.accel
		if self.speed + self.accel > self.max_speed:
			self.speed = self.max_speed
		else:
			self.speed += self.accel

	def collision_check(self, next_car):
		difference = (next_car.position[0] - 5) - self.position[0]
		if difference < self.speed:
			if difference <= 0:
				self.position[0] = next_car.position[0] - 7
				self.speed = 0
			else:
				self.speed = next_car.speed
		return self.position


	def move_car(self):
		self.position[0] += self.speed
		self.position[1] +=  1
		return self.position

	def needs_road_loop(self):
		if self.position[0] > 1000:
			return True

class Sim():
	def __init__(self):
		self.num_of_cars = 5
		self.car_list = []
		self.car_position_list = []
		self.car_speed_list = []


	def __str__():
		print("Runs the simulation.")

	def create_cars(self):
		self.car_list = [Car([i * 30 + 1, 0]) for i in range(self.num_of_cars)]
		return self.car_list

	def update_positions(self, road):
		self.car_position_list = []
		for i, car in enumerate(self.car_list):
			print("\nRun: ", i+1)
			print("Car pos + spd at start: ", car.position, car.speed)
			self.next_car = self.find_next_car(car, self.car_list, i)
			car.move_car()

			if car == self.car_list[-1]:
				if car.needs_road_loop():
					print("\nCar pos when needing loop: ", car.position)
					# print("\nCar[0] when needing loop: ", self.car_list[0].position)
					self.car_list = road.road_loop(self.car_list, car, self.next_car)
				else:
					car.change_speed()

			else:
				print("Car pos before speed change: ", car.position)
				car.change_speed()
				print("\nCar pos before collision_check: ", car.position)
				print("Next car pos before collision_check: ", self.next_car.position)
				car.position = car.collision_check(self.next_car)
				print("Car pos after collision_check: ", car.position)

			print("Car pos after updates: ", car.position)
			self.add_to_position_list(car, self.car_list)
			# print("\nCar list after add to positions: ", self.car_list[0].position, self.car_list[1].position, self.car_list[2].position)
			# print("\nPostion list: ", self.car_position_list)
			self.add_to_speed_list(car, self.car_list)
			print("Car pos + spd at end: ", car.position, car.speed)
		# print("\nCar position list: ", self.car_position_list)
		return self.car_position_list


	def add_to_position_list(self, car, car_list):
		if car == car_list[-1] and car.position[0] < car.max_speed + 1:
			self.car_position_list.insert(0, car.position)
		else:
			self.car_position_list.append(car.position)


	def add_to_speed_list(self, car, car_list):
		if car == car_list[-1] and car.position[0] < car.max_speed + 1:
			self.car_speed_list.insert(0, car.speed)
		else:
			self.car_speed_list.append(car.speed)


	def find_next_car(self, car, car_list, i):
		if car != self.car_list[-1]:
			next_car = self.car_list[i+1]
		else:
			next_car = self.car_list[0]
		return next_car


<<<<<<< HEAD
sim = Sim()

def main():
	car_stat_list = []
	
	for _ in range():
		car_stat_list.append()

	sim.create_cars()
	print(sim.car_list)
	road = Road()
	sim.update_positions(road)
	#??? car? sim.car? 
	sim.find_next_car(car,car_list,i)

if __name__ == '__main__':
	main()

=======
def main():

	sim = Sim()
	road = Road()

	positions_over_time = []
	sim.create_cars()
	start_list = []

	for i in sim.car_list:
		start_list.append(i.position)

	positions_over_time.append(start_list)
	print("Initial position list: ", positions_over_time)

	for i in range(1,3):
		sim.update_positions(road)
		# print("\n\nPosition list: ", sim.car_position_list)
		positions_over_time.append(sim.car_position_list)
		print("Position list from sim: ", sim.car_position_list)
		print("Round {}:\nPosition list from this run: {}".format((i+1), positions_over_time[i]))

	print("Full position list of lists: ", positions_over_time)


main()
>>>>>>> 66c902a1b2c867fa8150b25975b9fa1046d742ae
