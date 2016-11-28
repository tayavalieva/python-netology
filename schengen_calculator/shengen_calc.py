residence_limit = 90  
schengen_constraint = 180

# вынесли в функцию самую часто используемую операцию
# в которой не хотелось бы ошибиться
def date_difference (leave, arrive):
	result = leave - arrive + 1
	return result

# сделали работу с длиной визитов более удобной
def visit_length (visit):
	return date_difference(visit[1], visit[0])

def get_days_for_visits(visits):
	days_for_visits = []
	for visit in visits:
	    days_for_visit = 0
	    for past_visit in visits:
	        if visit[0] - schengen_constraint < past_visit[0] < visit[0]:
	            days_for_visit += visit_length(past_visit)
	    days_for_visit += visit_length(visit)
	    days_for_visits.append(days_for_visit)
	return days_for_visits
	
def count_days_future_visit(visits, date_in_future):
	visits_for_future = visits + [[date_in_future, date_in_future]]
	days_for_future_visits = get_days_for_visits(visits_for_future)
	days_in_es = residence_limit - days_for_future_visits[len(days_for_future_visits) - 1] + 1
	return days_in_es

def check_residence_limit_violation(visits):
	days_for_visits = get_days_for_visits(visits)

	for visit, total_days in zip(visits, days_for_visits):
	    if total_days > residence_limit:
	        overstay_time = total_days - residence_limit
	        print('Во время визита', visit, 'количество время пребывания превышено на', overstay_time, 'дней')

# Проверка того, чтобы дата нового въезда была раньше даты выезда
def check_if_entry_date_first(start,end):
	return start <= end
# Проверка того, чтобы новый визит не накладывался на последний визит
def trips_not_intersected(new_visit_start,visits):
	last_trip_end = visits[len(visits)-1][1]
	return new_visit_start > last_trip_end

#чтение списка визитов из файла
def read_visits_from_file(file_name):
	visits = []
	with open(file_name) as visits_dates:
		for one_visit_line in visits_dates: 
			one_visit_dates = one_visit_line.split()
			visit_start = int(one_visit_dates[0])
			visit_end = int(one_visit_dates[1])
			visits.append([visit_start,visit_end])
	return visits

#функция записи в файл визитов
def write_visits_to_file(visits, file_name):
	with open(file_name, 'w') as visits_dates:
		for visit in visits:
			visit_line = '%d %d\n'%(visit[0],visit[1])
			visits_dates.write(visit_line)
	return

file_name_for_visits = 'visits_dates.txt'	
visits = read_visits_from_file(file_name_for_visits)	
	
#функция вывода меню
def main_menu_inquiry(): 
	print('v - добавить визит')
	print ('p - узнать сколько дней можно провести в Шенгенской зоне.')
	print ('i - показать даты ваших текущих поездок')
	print ('e - выход из Шенгенского калькулятора')

#функция вывода всех текущих поездок в ЕС
def print_all_visits():
	print ('Даты ваших текущих поездок в ЕС:', visits)

#функция добавления нового визита
def add_new_visit_to_list():
	print('Начало:')
	start = int(input())
	print('Конец:')
	end = int(input())
	if check_if_entry_date_first(start,end):
		if trips_not_intersected(start,visits):
			visits.append([start, end])
			print_all_visits()
		else: 
			print('Произошла ошибка! Новая поездка началась раньше, чем закончилась предыдущая. Введите корректную дату нового въезда в ЕС.')
			add_new_visit_to_list()
	else:
		print(' Произошла ошибка! Дата выезда из ЕС должна быть позже даты въезда.')
		add_new_visit_to_list()

#функция: сколько дней можно провести в ЕС
def print_days_for_future_visit():
	print ('Введите дату въезда:')
	date_in_future = int(input())
	if trips_not_intersected(date_in_future,visits):
		print ('Если въедем %s числа, сможем провести в шенгене %s дней' % (date_in_future, count_days_future_visit(visits, date_in_future)))
	else:
		print('Произошла ошибка! Новая поездка началась раньше, чем закончилась предыдущая. Введите корректную дату нового въезда в ЕС.')


print ('Нажмите "h", чтобы вывести на экран справку о командах.')
while True: 
	user_input = input()
	if user_input == 'i':
		print_all_visits()
	if user_input == 'h':
		main_menu_inquiry()  
	if user_input == 'p':
		print_days_for_future_visit()
	if user_input == 'v':
		add_new_visit_to_list()
		check_residence_limit_violation(visits)
	if user_input == 'e':
		print('Пока-пока!')
		write_visits_to_file(visits,file_name_for_visits)
		break

