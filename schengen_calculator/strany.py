import json
from pprint import pprint

schengen_countries = set()
sea_countries = set()
hot_countries = set()
enough_money_countries = set()

number_of_days = 30
money_amount = 100000

with open('countries_list.json') as countries_file:
	countries = json.load(countries_file)
for country_name, properties in countries.items():
  if properties['average_temperature'] > 12:
    hot_countries.add(country_name)
  if properties['sea']:
    sea_countries.add(country_name)
  if properties['schengen']:
    schengen_countries.add(country_name)
  if money_amount >= properties['day_cost_of_living']*properties['currency_rate']*number_of_days:
    enough_money_countries.add(country_name)

sea_or_shengen_countries = sea_countries | schengen_countries
hot_sea_or_shengen_countries = sea_or_shengen_countries & hot_countries
hot_sea_or_shengen_enough_money_countries = hot_sea_or_shengen_countries & enough_money_countries
#print (hot_sea_or_shengen_countries)
print('Теплые страны с морем или теплые страны в Шенгенской зоне, где указанной суммы денег хватит на 30 дней:', hot_sea_or_shengen_enough_money_countries)



#тёплые и есть море или находятся в шенгене, и нам хватит денег прожить там месяц.

#for country_name, properties in countries.items():
#	if properties['schengen']:
#		schengen_countries.add(country_name)
#	if properties['sea']:
#		sea_countries.add(country_name)


#Форматирование вывода
#money_amount = 10000
#for country in countries:
 # currency_amount = money_amount / country['currency_rate']
#  print('У нас будет %.3f денег в местной валюте' % currency_amount)



# Подход со списками словарей
#for country_name in sea_schengen_countries:
#	for country in countries:
#		if country['name'] == country_name:
#			print(country)
#			break

# Подход со словарем словарей
#for country_name in sea_schengen_countries:
#	print(country_name, countries[country_name])


