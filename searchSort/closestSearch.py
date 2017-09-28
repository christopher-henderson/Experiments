from __future__ import division
from random import random

INDEX = {193540.0: 'Czech Republic',
 195880.0: 'Greece',
 200490.0: 'Vietnam',
 205860.0: 'Portugal',
 226760.0: 'Bangladesh',
 234900.0: 'Chile',
 239190.0: 'Finland',
 274140.0: 'Colombia',
 280370.0: 'South Africa',
 284520.0: 'Pakistan',
 296640.0: 'Singapore',
 302570.0: 'Denmark',
 302750.0: 'Malaysia',
 307920.0: 'Ireland',
 311690.0: 'Philippines',
 311740.0: 'Israel',
 316070.0: 'Hong Kong SAR',
 333720.0: 'Venezuela',
 346570.0: 'Egypt',
 375020.0: 'United Arab Emirates',
 376270.0: 'Norway',
 387300.0: 'Austria',
 390590.0: 'Thailand',
 412300.0: 'Islamic Republic of Iran',
 415080.0: 'Nigeria',
 467350.0: 'Poland',
 470180.0: 'Belgium',
 517440.00000000006: 'Sweden',
 519150.0: 'Taiwan Province of China',
 541750.0: 'Argentina',
 637790.0: 'Saudi Arabia',
 662480.0: 'Switzerland',
 735720.0: 'Turkey',
 769930.0: 'Netherlands',
 940950.0: 'Indonesia',
 1063610.0: 'Mexico',
 1252160.0: 'Spain',
 1256640.0: 'Australia',
 1267750.0: 'Russia',
 1404380.0: 'Korea',
 1532340.0: 'Canada',
 1769600.0: 'Brazil',
 1852500.0: 'Italy',
 2250990.0: 'India',
 2488280.0: 'France',
 2649890.0: 'United Kingdom',
 3494900.0: 'Germany',
 4730300.0: 'Japan',
 11391620.0: 'China',
 18561930.0: 'United States'
}

GDPS = sorted(INDEX.keys())

# STATES = {
# 	"California": 2602672,
# 	"Texas": 1616801,
# 	"New York": 1487998,
# 	"Florida": 926817,
# 	"Illinois": 791608,
# 	"Pennsylvania": 724936,
# 	"Ohio": 625715,
# 	"New Jersey": 581122,
# 	"Georgia": 525360,
# 	"North Carolina": 517904,
# 	"Massachusetts": 507913,
# 	"Virginia": 494349,
# 	"Michigan": 487239,
# 	"Washington": 469739,
# 	"Maryland": 378280,
# 	"Indiana": 341909,
# 	"Minnesota": 335147,
# 	"Tennessee": 328770,
# 	"Colorado": 323692,
# 	"Wisconsin": 309536,
# 	"Arizona": 302952,
# 	"Missouri": 300891,
# 	"Connecticut": 263379,
# 	"Louisiana": 235109,
# 	"Oregon": 226821,
# 	"South Carolina": 209716,
# 	"Alabama": 204861,
# 	"Kentucky": 197043,
# 	"Oklahoma": 182937,
# 	"Iowa": 178766,
# 	"Utah": 156352,
# 	"Kansas": 153258,
# 	"Nevada": 147475,
# 	"District of Columbia": 126815,
# 	"Arkansas": 120689,
# 	"Nebraska": 115345,
# 	"Mississippi": 107680,
# 	"New Mexico": 93297,
# 	"Hawaii": 83917,
# 	"New Hampshire": 77855,
# 	"West Virginia": 73374,
# 	"Delaware": 70387,
# 	"Idaho": 67275,
# 	"Maine": 59275,
# 	"Rhode Island": 57433,
# 	"North Dakota": 52089,
# 	"Alaska": 50713,
# 	"South Dakota": 48139,
# 	"Montana": 45994,
# 	"Wyoming": 37858,
# 	"Vermont": 31092
# }

STATES = {
	2602672: "California",
	1616801: "Texas",
	1487998: "New York",
	926817: "Florida",
	791608: "Illinois",
	724936: "Pennsylvania",
	625715: "Ohio",
	581122: "New Jersey",
	525360: "Georgia",
	517904: "North Carolina",
	507913: "Massachusetts",
	494349: "Virginia",
	487239: "Michigan",
	469739: "Washington",
	378280: "Maryland",
	341909: "Indiana",
	335147: "Minnesota",
	328770: "Tennessee",
	323692: "Colorado",
	309536: "Wisconsin",
	302952: "Arizona",
	300891: "Missouri",
	263379: "Connecticut",
	235109: "Louisiana",
	226821: "Oregon",
	209716: "South Carolina",
	204861: "Alabama",
	197043: "Kentucky",
	182937: "Oklahoma",
	178766: "Iowa",
	156352: "Utah",
	153258: "Kansas",
	147475: "Nevada",
	126815: "District of Columbia",
	120689: "Arkansas",
	115345: "Nebraska",
	107680: "Mississippi",
	93297: "New Mexico",
	83917: "Hawaii",
	77855: "New Hampshire",
	73374: "West Virginia",
	70387: "Delaware",
	67275: "Idaho",
	59275: "Maine",
	57433: "Rhode Island",
	52089: "North Dakota",
	50713: "Alaska",
	48139: "South Dakota",
	45994: "Montana",
	37858: "Wyoming",
	31092: "Vermont"
}


def closest_search(collection, value, closest=None):
	if len(collection) is 0:
		return closest
	if len(collection) is 1:
		return choose(closest, collection[0], value)
	mid = len(collection) // 2
	mid_value = collection[mid]
	if mid_value == value:
		# We actually found it!
		return mid_value
	closest = choose(closest, mid_value, value)
	if mid_value > value:
		return closest_search(collection[:mid:], value, closest)
	else:
		return closest_search(collection[mid::], value, closest)

def choose(current, candidate, value):
	if current is None:
		return candidate
	return current if abs(current - value) <= abs(candidate - value) else candidate

if __name__ == '__main__':
	for gdp in reversed(sorted(STATES.keys())):
		state = STATES[gdp]
		national_gdp = closest_search(GDPS, gdp)
		print('The closest national GDP to {STATE} (${SGDP} million) is {NATION} (${NGDP} million)'.format(
				STATE=state,
				SGDP=gdp,
				NATION=INDEX[national_gdp],
				NGDP=national_gdp
			))