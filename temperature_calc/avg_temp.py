temperature = []
with open('temperature.txt') as t:
	for line in t:
		temperature.append(int(line))
print (temperature)
avg = sum(temperature)/len(temperature)

temperature_deviation = []
for t in temperature:
	temperature_deviation.append(t- avg)

print('Средняя температура \n в НН:', avg)

with open('average_temperature.txt', 'w') as t_average_file:
	t_average_file.write("%.2f" % avg)

with open('temperature_deviation.txt', 'w') as t_deviation_file:
	for t in temperature_deviation:
		t_deviation_file.write('%.2f\n' % t)