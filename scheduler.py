import sys
import json

if __name__ == '__main__':
	if len(sys.argv) > 1:
		if len(sys.argv) == 4:
			problemClass = sys.argv[1]
			groupNumber  = sys.argv[2]
			groupSize    = sys.argv[3]
		else:
			print(f'Use: python {sys.argv[0]} problemClass groupNumber groupSize')
			exit(1)

	else:
		problemClass = input('Classe dos problemas: ')
		groupNumber  = input('Número de grupos: ')
		groupSize    = input('Número de problemas por grupo: ')
	
	groupNumber = int(groupNumber)
	groupSize   = int(groupSize)

	with open('problems.json', 'r', encoding='utf-8') as file:
		problems = json.load(file)

	startsWith = 1002

	problems   = [*filter(lambda e : e['category'] == problemClass, problems)]
	problemsID = [*map(lambda e : e['id'], problems)]
	problemsID = [*filter(lambda e : int(e) >= startsWith, problemsID)]


	for i in range(groupNumber):
		print(' '.join(problemsID[i*groupSize:(i + 1)*groupSize]))