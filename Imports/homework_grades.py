import Imports.grade_average_service as grade_service
import random

homework_assignment_grades = {
    'homework_1': random.randint(90, 100),
    'homework_2': random.randint(50, 100),
    'homework_3': random.randint(50, 100)
}


grade_service.calculate_homework(homework_assignment_grades)
