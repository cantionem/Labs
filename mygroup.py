groupmates = [
{
"name": "Андрей",
"surname": "Соколов",
"exams": ["Инженерная и копмьютерная графика", "Философия", "Основы программирования"],
"marks": [4, 3, 4]
},
{
"name": "Борис",
"surname": "Егоров",
"exams": ["Структуры и алгоритмы обработки данных", "Математический анализ", "Теория информации"],
"marks": [3, 4, 3]
},
{
"name": "Влад",
"surname": "Кузнецов",
"exams": ["СиМРИС", "Системы реального времени", "Дискретная математика"],
"marks": [5, 4, 5]
},
{
"name": "Георгий",
"surname": "Орлов",
"exams": ["Безопасность жизнедеятельности", "Технологии баз данных", "Электроника"],
"marks": [5, 5, 4,]
},
{
"name": "Иван",
"surname": "Иванов",
"exams": ["Инженерная и копмьютерная графика", "Дискретная математика", "Теория информации"],
"marks": [4, 5, 4]
},
{
"name": "Семен",
"surname": "Сидоров",
"exams": ["Философия", "Безопасность жизнедеятельности", "СиМРИС"],
"marks": [3, 4, 5]
}
]

def calc_average(_marks):
	average = 0
	num_of_marks = 0
	for mark in _marks:
		average += mark
		num_of_marks += 1
	average = average/num_of_marks
	return average


def print_students(_students, _average):
		print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20))
		for student in _students:
			if calc_average(student["marks"]) > _average:
				print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30), str(student["marks"]).ljust(20))
			
			
average_mark = input('Введите средний балл:') 
print_students(groupmates, float(average_mark))