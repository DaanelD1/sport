import random
sportsmen = []
results = []

for i in range(int(input("Введите количество спортсменов "))):
	n = input("Имя спортсмена ")
	sportsmen.append(n)
	results.append(random.randint(10,100))


def best():
	best_value = 0
	sport_max = []
	for x in results:
		if x > best_value: 
			best_value = x
	for x in results:
		if x == best_value:
			index = results.index(x)
			sport_max.append(sportsmen[index])
	return sport_max, best_value
def pedestal():
	best_value = 0
	sport_max = []
	pedestal = []
	pedestal_score = []
	for x in results:
		if x > best_value: 
			best_value = x
	pedestal_score.append(best_value)
	for x in results:
		if x == best_value:
			index = results.index(x)
			sport_max.append(sportsmen[index])
			pedestal.append(sportsmen[index])
			break
	while best_value > 0 or len(pedestal) < 3:
		try:
			best_value -= 1
			index = results.index(best_value)
			pedestal.append(sportsmen[index])
			pedestal_score.append(results[index])
			if len(pedestal) == 3:
				break
			if(best_value <= 0):
				break
		except:
			if len(pedestal) == 3:
				break
			if(best_value <= 0):
				break
			continue

	return pedestal, pedestal_score
def top():
	best_value = 0
	sport_max = []
	top_names = []
	top_score = []
	sportsmen_copy = sportsmen.copy()
	results_copy = results.copy()
	for x in results:
		if x > best_value: 
			best_value = x
	top_score.append(best_value)
	for x in results:
		if x == best_value:
			index = results.index(x)
			sport_max.append(sportsmen_copy[index])
			top_names.append(sportsmen_copy[index])
			break
	while best_value > 0:
		try:
			best_value -= 1
			index = results_copy.index(best_value)
			top_names.append(sportsmen_copy[index])
			top_score.append(results_copy[index])
			results_copy.pop(index)
			sportsmen_copy.pop(index)
			if(best_value <= 0):
				break
		except:
			if(best_value <= 0):
				break
			continue

	return top_names, top_score
def disq():
	i = 0
	while True:
		has = False
		value = 0
		for a in results:
			if a < 50:
				has = True
				value = a
				break
		if not has:
			break
		ind = results.index(value)
		results.pop(ind)
		sportsmen.pop(ind)

while True:
	print("1 - Вывести лучших спорстменов")
	print("2 - Отобразить спорстменов на пьедестале")
	print("3 - Дисквалифицировать участников (<50)")
	print("4 - Таблица рекордов")
	komanda = input("Введите команду ")
	if komanda == "1":
		print(best())
	elif komanda == "2":
		ped, sc = pedestal()
		mesto = 1
		for a in ped:
			ind = ped.index(a)
			text = f"{mesto}# {a} {sc[ind]}"
			print(text)
			mesto += 1
	elif komanda == "3":
		disq()
		print(results)
		print(sportsmen)
	elif komanda == "4":
		sportsmen,results = top()
		mesto = 1
		for a in sportsmen:
			ind = sportsmen.index(a)
			text = f"{mesto}# {a} {results[ind]}"
			print(text)
			mesto += 1

