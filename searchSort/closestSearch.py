#/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division

import sqlite3

# https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)
# As per the United Nations.
INDEX = {
	18036648: "United States",
	16832631: "European Union",
	11158457: "China",
	4383076: "Japan",
	3363600: "Germany",
	2858003: "United Kingdom",
	2418946: "France",
	2116239: "India",
	1821580: "Italy",
	1772591: "Brazil",
	1552808: "Canada",
	1377873: "South Korea",
	1326016: "Russia[n 3]",
	1230859: "Australia",
	1192955: "Spain",
	1140724: "Mexico",
	861934: "Indonesia",
	750318: "Netherlands",
	717887: "Turkey",
	670789: "Switzerland",
	653219: "Saudi Arabia",
	571090: "Sweden",
	568499: "Nigeria",
	544959: "Poland",
	543490: "Argentina",
	531547: "Belgium",
	509968: "Venezuela",
	500519: "Norway",
	436888: "Austria",
	425326: "Iran",
	404824: "Thailand",
	399451: "United Arab Emirates",
	377740: "Colombia",
	349819: "South Africa",
	346119: "Denmark",
	326933: "Malaysia",
	307872: "Singapore",
	305673: "Israel",
	290896: "Philippines",
	282242: "Egypt",
	274027: "Hong Kong",
	272217: "Finland",
	258062: "Chile",
	251255: "Pakistan",
	250814: "Ireland",
	235574: "Greece",
	230117: "Portugal",
	225422: "Iraq",
	216036: "Kazakhstan",
	213518: "Algeria",
	211817: "Qatar",
	205270: "Czech Republic",
	201809: "Peru",
	199045: "Romania",
	198652: "New Zealand",
	186205: "Vietnam",
	173062: "Bangladesh",
	163637: "Kuwait",
	146676: "Angola",
	138347: "Hungary",
	131806: "Ukraine",
	110009: "Morocco",
	103676: "Puerto Rico",
	100917: "Ecuador",
	100249: "Slovakia",
	87205: "Cuba",
	81894: "Sudan",
	81797: "Oman",
	76139: "Belarus",
	75193: "Azerbaijan",
	74941: "Sri Lanka",
	66478: "Myanmar",
	64874: "Luxembourg",
	63969: "Dominican Republic",
	63030: "Uzbekistan",
	60936: "Kenya",
	58827: "Guatemala",
	57471: "Uruguay",
	57137: "Croatia",
	56718: "Bulgaria",
	55502: "Macau",
	53638: "Ethiopia",
	49631: "Lebanon",
	49553: "Costa Rica",
	49491: "Slovenia",
	49166: "Panama",
	48392: "Lithuania",
	48030: "Tanzania",
	47932: "Turkmenistan",
	47423: "Tunisia",
	43866: "Serbia",
	41319: "Libya",
	37177: "Ghana",
	37131: "Yemen",
	35909: "Democratic Republic of the Congo",
	35827: "Jordan",
	34254: "Côte d'Ivoire",
	33850: "Bahrain",
	32996: "Bolivia",
	32051: "Cameroon",
	31286: "Latvia",
	30985: "Paraguay",
	28069: "Trinidad and Tobago",
	27465: "Uganda",
	26963: "Zambia",
	26485: "Estonia",
	25164: "El Salvador",
	23077: "Cyprus",
	21122: "Afghanistan",
	19497: "Honduras",
	19489: "Nepal",
	18491: "Bosnia and Herzegovina",
	17412: "Gabon",
	17396: "North Korea",
	17104: "Brunei",
	17081: "Mozambique",
	17036: "Iceland",
	16778: "Cambodia",
	16731: "Equatorial Guinea",
	16576: "Papua New Guinea",
	16530: "Georgia",
	15813: "Botswana",
	15658: "Senegal",
	14719: "Zimbabwe",
	14077: "Congo Republic of the",
	13927: "Jamaica",
	13429: "Namibia",
	13413: "Albania",
	12791: "Chad",
	12766: "Arab Palestinian areas",
	12756: "Burkina Faso",
	12616: "Mauritius",
	12067: "Mongolia",
	11979: "Mali",
	11806: "Nicaragua",
	11749: "Laos",
	11319: "Macedonia",
	11007: "South Sudan",
	10889: "Armenia",
	10674: "Madagascar",
	10536: "Malta",
	10234: "New Caledonia",
	9575: "Benin",
	9242: "Tajikistan",
	8599: "Haiti",
	8510: "The Bahamas",
	8169: "Niger",
	7944: "Moldova",
	7903: "Rwanda",
	7404: "Kyrgyzstan",
	7387: "Kosovo",
	7060: "Monaco",
	6579: "Guinea",
	5855: "Liechtenstein",
	5720: "Malawi",
	5623: "French Polynesia",
	5601: "Bermuda",
	5210: "Suriname",
	5092: "Mauritania",
	4970: "Timor-Leste",
	4893: "Sierra Leone",
	4588: "Montenegro",
	4576: "Togo",
	4532: "Fiji",
	4482: "Swaziland",
	4353: "Barbados",
	3858: "Eritrea",
	3480: "Cayman Islands",
	3278: "Andorra",
	3159: "Curaçao",
	3086: "Guyana",
	3032: "Maldives",
	2869: "Burundi",
	2664: "Aruba",
	2441: "Greenland",
	2122: "Liberia",
	2081: "Lesotho",
	1965: "Bhutan",
	1855: "Cape Verde",
	1845: "San Marino",
	1838: "Central African Republic",
	1699: "Belize",
	1589: "Djibouti",
	1511: "Seychelles",
	1406: "Saint Lucia",
	1375: "Somalia",
	1289: "Zanzibar",
	1248: "Antigua and Barbuda",
	1209: "Guinea-Bissau",
	1103: "Solomon Islands",
	1059: "Sint Maarten",
	902: "British Virgin Islands",
	884: "Grenada",
	852: "Saint Kitts and Nevis",
	851: "The Gambia",
	824: "Samoa",
	812: "Vanuatu",
	797: "Turks and Caicos Islands",
	729: "Saint Vincent and the Grenadines",
	648: "Comoros",
	533: "Dominica",
	435: "Tonga",
	337: "São Tomé and Príncipe",
	308: "Federated States of Micronesia",
	311: "Cook Islands",
	311: "Anguilla",
	234: "Palau",
	209: "Marshall Islands",
	182: "Nauru",
	180: "Kiribati",
	63: "Montserrat",
	38: "Tuvalu"
}


# https://en.wikipedia.org/wiki/List_of_U.S._states_by_GDP
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

INCOME = {
	"Maryland": 75847,
	"District of Columbia": 75628,
	"Hawaii": 73486,
	"Alaska": 73355,
	"New Jersey": 72222,
	"Connecticut": 71346,
	"Massachusetts": 70628,
	"New Hampshire": 70303,
	"Virginia": 66262,
	"California": 64500,
	"Washington": 64129,
	"Colorado": 63909,
	"Minnesota": 63488,
	"Utah": 62912,
	"Delaware": 61255,
	"New York": 60850,
	"North Dakota": 60557,
	"Wyoming": 60214,
	"Illinois": 59588,
	"Rhode Island": 58073,
	"Vermont": 56990,

	"Pennsylvania": 55702,
	"Texas": 55653,
	"Wisconsin": 55638,
	"Nebraska": 54996,
	"Iowa": 54736,
	"Oregon": 54148,
	"Kansas": 53906,
	"South Dakota": 53017,
	"Nevada": 52431,
	"Maine": 51494,
	"Arizona": 51492,
	"Georgia": 51244,
	"Michigan": 51084,
	"Ohio": 51075,
	"Indiana": 50532,
	"Missouri": 50238,
	"Montana": 49509,
	"Florida": 49426,
	"Oklahoma": 48568,
	"Idaho": 48275,
	"North Carolina": 47830,
	"Tennessee": 47275,
	"South Carolina": 47238,
	"Louisiana": 45727,
	"New Mexico": 45382,
	"Kentucky": 45215,
	"Alabama": 44765,
	"West Virginia": 42019,
	"Arkansas": 41995,
	"Mississippi": 40593,
	"Puerto Rico": 18626,
}

# POPULATIONS = {
# 	"California": 39250017,
# 	"Texas": 27862596,
# 	"Florida": 20612439,
# 	"New York": 19745289,
# 	"Illinois": 12801539,
# 	"Pennsylvania": 12784227,
# 	"Ohio": 11646273,
# 	"Georgia": 10310371,
# 	"Michigan": 9928300,
# 	"New Jersey": 8944469,
# 	"Virginia": 8411808,
# 	"Washington": 7288000,
# 	"Arizona": 6931071,
# 	"Massachusetts": 6811779,
# 	"Tennessee": 6651194,
# 	"Indiana": 6633053,
# 	"Missouri": 6093000,
# 	"Maryland": 6016447,
# 	"Wisconsin": 5778708,
# 	"Colorado": 5540545,
# 	"Minnesota": 5519952,
# 	"South Carolina": 4961119,
# 	"Alabama": 4863300,
# 	"Louisiana": 4681666,
# 	"Kentucky": 4436974,
# 	"Oregon": 4093465,
# 	"Oklahoma": 3923561,
# 	"Connecticut": 3576452,
# 	"Puerto Rico": 3411307,
# 	"Iowa": 3134693,
# 	"Utah": 3051217,
# 	"Mississippi": 2988726,
# 	"Arkansas": 2988248,
# 	"Nevada": 2940058,
# 	"Kansas": 2907289,
# 	"New Mexico": 2081015,
# 	"Nebraska": 1907116,
# 	"West Virginia": 1831102,
# 	"Idaho": 1683140,
# 	"Hawaii": 1428557,
# 	"New Hampshire": 1334795,
# 	"Maine": 1331479,
# 	"Rhode Island": 1056426,
# 	"Montana": 1042520,
# 	"Delaware": 952065,
# 	"South Dakota": 865454,
# 	"North Dakota": 757952,
# 	"Alaska": 741894,
# 	"District of Columbia": 681170,
# 	"Vermont": 624594,
# 	"Wyoming": 585501,
# 	"North Carolina": 10146788
# }

POPULATIONS = {
	"Alabama": 2172599,
	"Alaska": 359974,
	"Arizona": 3241843,
	"Arkansas": 1342501,
	"California": 19132887,
	"Colorado": 2897177,
	"Connecticut": 1891278,
	"Delaware": 472077,
	"District of Columbia": 392080,
	"Florida": 9845281,
	"Georgia": 4932454,
	"Hawaii": 687048,
	"Idaho": 816697,
	"Illinois": 6514368,
	"Indiana": 3325384,
	"Iowa": 1699773,
	"Kansas": 1480809,
	"Kentucky": 2000905,
	"Louisiana": 2112540,
	"Maine": 694043,
	"Maryland": 3171266,
	"Massachusetts": 3586562,
	"Michigan": 4833276,
	"Minnesota": 2998818,
	"Mississippi": 1280627,
	"Missouri": 3105609,
	"Montana": 526891,
	"Nebraska": 1010525,
	"Nevada": 1428963,
	"New Hampshire": 750008,
	"New Jersey": 4513965,
	"New Mexico": 927184,
	"New York": 9536018,
	"New York City": 4130179,
	"North Carolina": 4875585,
	"North Dakota": 416810,
	"Ohio": 5699533,
	"Oklahoma": 1823438,
	"Oregon": 2062731,
	"Pennsylvania": 6450125,
	"Rhode Island": 552539,
	"South Carolina": 2297229,
	"South Dakota": 453764,
	"Tennessee": 3151938,
	"Texas": 13290348,
	"Utah": 1517461,
	"Vermont": 345248,
	"Virginia": 4242706,
	"Washington": 3656845,
	"West Virginia": 783093,
	"Wisconsin": 3119918,
	"Wyoming": 301844,
	"Puerto Rico": 1117320
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


def main():
	million = 1000000
	connection = sqlite3.connect("lol")
	cursor = connection.cursor()
	cursor.execute("drop table if exists states")
	cursor.execute("drop table if exists nations")
	cursor.execute("create table nations (id INTEGER PRIMARY KEY AUTOINCREMENT, name text, gdp float);")
	cursor.execute("create table states (id INTEGER PRIMARY KEY, name text, gdp float, population integer, gdppc float, avg_income integer, inequity float, nearest integer, foreign key(nearest) references nations);")
	national_gdps = sorted(INDEX.keys())
	state_gdps = reversed(sorted(STATES.keys())) 
	for state_gdp in state_gdps:
		state_name = STATES[state_gdp]
		national_gdp = closest_search(national_gdps, state_gdp)
		print('The closest national GDP to {STATE} (${SGDP} million) is {NATION} (${NGDP} million)'.format(
				STATE=state_name,
				SGDP=state_gdp,
				NATION=INDEX[national_gdp],
				NGDP=national_gdp
			))
		n = cursor.execute("select id from nations where name = '{}'".format(INDEX[national_gdp]))
		result = n.fetchone()
		if not result:
			cursor.execute("insert into nations (name, gdp) values ('{}', {})".format(INDEX[national_gdp], national_gdp))
			n = cursor.execute("select id from nations where name = '{}'".format(INDEX[national_gdp]))
			result = n.fetchone()
		n_id = result[0]
		gdppc = state_gdp / POPULATIONS[state_name] * million
		cursor.execute("insert into states (name, gdp, population, gdppc, avg_income, inequity, nearest) values ('{}', {}, {}, {}, {}, {}, {})".format(
			state_name, state_gdp, POPULATIONS[state_name], gdppc, INCOME[state_name], INCOME[state_name] / gdppc, n_id
		))
	connection.commit()


if __name__ == '__main__':
	main()