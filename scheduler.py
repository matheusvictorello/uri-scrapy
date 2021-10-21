import sys
import json

problemsCategory = 'Iniciante'

with open('problems.json', 'r', encoding='utf-8') as file:
	problems = json.load(file)

problems = [*filter(lambda e : e['category'] == problemsCategory, problems)]

with open('problemsDone.json', 'r', encoding='utf-8') as file:
	problemsDone = json.load(file)

problemsDone = problemsDone[problemsCategory]

problemsTodo = list(filter(lambda p : not p['id'] in problemsDone, problems))

problemsTodoIds = list(map(lambda p : (int(p['solved'].replace('.', '')), p['id']), problemsTodo))

problemsTodoIds.sort(reverse=True)

# for solved, id_ in problemsTodoIds:
# 	print(f'{id_} {solved}')

for solved, id_ in problemsTodoIds:
	print(f'{id_} - {problemsCategory}')