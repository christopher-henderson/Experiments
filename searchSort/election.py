# -*- coding: utf-8 -*-
from __future__ import division
import sqlite3


results = {'Mississippi': (40.11, 57.94), 'Oklahoma': (28.93, 65.32), 'Delaware': (53.09, 41.72), 'Minnesota': (46.44, 44.92), 'Illinois': (55.83, 38.76), 'Arkansas': (33.65, 60.57), 'New Mexico': (48.26, 40.04), 'Indiana': (37.91, 56.82), 'Maryland': (60.33, 33.91), 'Louisiana': (38.45, 58.09), 'Idaho': (27.49, 59.26), 'Wyoming': (21.63, 67.4), 'Tennessee': (34.72, 60.72), 'Arizona': (45.13, 48.67), 'Iowa': (41.74, 51.15), 'Michigan': (47.27, 47.5), 'Kansas': (36.05, 56.65), 'Utah': (27.46, 45.54), 'Virginia': (49.73, 44.41), 'Oregon': (50.07, 39.09), 'Connecticut': (54.57, 40.93), 'Montana': (35.75, 56.17), 'California': (61.73, 31.62), 'Massachusetts': (60.01, 32.81), 'West Virginia': (26.43, 68.5), 'South Carolina': (40.67, 54.94), 'New Hampshire': (46.98, 46.61), 'Wisconsin': (46.45, 47.22), 'Vermont': (56.68, 30.27), 'Georgia': (45.64, 50.77), 'North Dakota': (27.23, 62.96), 'Pennsylvania': (47.46, 48.18), 'Florida': (47.82, 49.02), 'Alaska': (36.55, 51.28), 'Kentucky': (32.68, 62.52), 'Hawaii': (62.22, 30.03), 'Nebraska': (33.7, 58.75), 'Missouri': (38.14, 56.77), 'Ohio': (43.56, 51.69), 'Alabama': (34.36, 62.08), 'New York': (59.01, 36.52), 'South Dakota': (31.74, 61.53), 'Colorado': (48.16, 43.25), 'New Jersey': (54.99, 41.0), 'Washington': (52.54, 36.83), 'North Carolina': (46.17, 49.83), 'District of Columbia': (90.48, 4.07), 'Texas': (43.24, 52.23), 'Nevada': (47.92, 45.5), 'Maine': (47.83, 44.87), 'Rhode Island': (54.41, 38.9)}

def main():
	connection = sqlite3.connect('lol')
	cursor = connection.cursor()
	cursor.execute('select sum(gdp) from states')
	us_gdp = cursor.fetchone()[0]
	print(us_gdp)
	cursor.execute('select name, gdp from states')
	states = cursor.fetchall()
	state_weights = {name: (gdp / us_gdp) for name, gdp in states}
	clinton = 0
	trump = 0
	# for state, weight in state_weights.items():
	# 	clinton += results[state][0] * weight
	# 	trump += results[state][1] * weight


	for state, weight in state_weights.items():
		if results[state][0] > results[state][1]:
			clinton += weight
		else:
			trump += weight


	clinton_wins = 0
	clinton_differential = 0
	red_nullification = 0
	trump_wins = 0
	trump_differential = 0
	blue_nullification = 0
	for state, result in results.items():
		if results[state][0] > results[state][1]:
			clinton_wins += 1
			clinton_differential += (results[state][0] - results[state][1])
			red_nullification += results[state][1] * state_weights[state]
		else:
			trump_wins += 1
			trump_differential += (results[state][1] - results[state][0])
			blue_nullification += results[state][0] * state_weights[state]
	print(red_nullification, blue_nullification)
	# print(clinton, trump, (trump - clinton) * 100)
	# print(clinton_differential / clinton_wins, trump_differential / trump_wins)
	# s = {gdp: (name, results[name])for name, gdp in states}
	# for key in reversed(sorted(s.keys())):
	# 	print(s[key])

main()