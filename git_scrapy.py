import sys
import json
import requests
from bs4 import BeautifulSoup

problemsCategory = 'Strings'

page = requests.get(f'https://github.com/petbccufscar/URI/tree/master/Python/{problemsCategory}')

if page.status_code != 200:
	print('Error')
	exit()

soup = BeautifulSoup(page.content, 'html.parser')

rows = soup.find_all('div', {"role": "row"})

def get_problem_number_from_row(row):
	a = row.find('a', href=True)

	if a:
		text = a.text
		if '.py' in text:
			return text.replace('.py', '')
		else:
			return None
	else:
		return None

problemsDone = list(filter(lambda e : e != None, map(get_problem_number_from_row, rows)))

with open('problemsDone.json', 'r', encoding='utf-8') as file:
	current = json.load(file)

current[problemsCategory] = problemsDone

with open('problemsDone.json', 'w', encoding='utf-8') as file:
	json.dump(current, file, indent=4)
