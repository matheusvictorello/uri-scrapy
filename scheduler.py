import sys
import json

if __name__ == '__main__':
	if len(sys.argv) > 1:
		if len(sys.argv) == 2:
			problemClass = sys.argv[1]
		else:
			print(f'Use: python {sys.argv[0]} problemClass')
			exit(1)

	else:
		problemClass = input('Classe dos problemas: ')

	with open('problems.json', 'r', encoding='utf-8') as file:
		problems = json.load(file)

	problems = [*filter(lambda e : e['category'] == problemClass, problems)]
	
	startsWith = 1002

	for i in range(1, 11):
		print(f'Level {i}')
		problems_level   = [*filter(lambda e : int(e['level']) == i, problems)]
		problemsID = [*map(lambda e : e['id'], problems_level)]
		problemsID = [*filter(lambda e : int(e) >= startsWith, problemsID)]

		while len(problemsID) >= 3:
			p1, p2, p3, *problemsID = problemsID
			print(' '.join([p1, p2, p3]))

		print(' '.join(problemsID))
