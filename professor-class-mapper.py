import csv
import os

professors = dict()
classes = dict()


def map_professors_and_classes(filename):
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            current_professors = row[10].replace('&#233;', 'e').split(';')
            current_class = row[1]
            for current_professor in current_professors:
                current_professor = current_professor.strip()
                if not current_professor:
                    continue

                # Add to the professors dict
                if current_professor in professors:
                    professors[current_professor].add(current_class)
                else:
                    professors[current_professor] = {current_class}

                # Add to the classes dict
                if current_class in classes:
                    classes[current_class].add(current_professor)
                else:
                    classes[current_class] = {current_professor}


if __name__ == '__main__':
    map_professors_and_classes(os.path.join('data', 'Fall 2021 ScheduleOfClasses.csv'))
    map_professors_and_classes(os.path.join('data', 'Spring 2021 ScheduleOfClasses.csv'))
    map_professors_and_classes(os.path.join('data', 'Fall 2020 ScheduleOfClasses.csv'))
    map_professors_and_classes(os.path.join('data', 'Spring 2020 ScheduleOfClasses.csv'))
    map_professors_and_classes(os.path.join('data', 'Fall 2019 ScheduleOfClasses.csv'))
    map_professors_and_classes(os.path.join('data', 'Spring 2019 ScheduleOfClasses.csv'))

    input_val = ''
    while input_val != 'classes' and input_val != 'professors' and input_val != 'both':
        print('Would you like information on classes or professors?')
        print('Please enter "classes", "professors", or "both"')
        input_val = input().lower()
        print()

    if input_val == 'classes' or input_val == 'both':
        for class_name, professor_names in sorted(classes.items()):
            print('{:9} {}'.format(class_name, professor_names))
    if input_val == 'both':
        print()
        print('-'*100)
        print()
    if input_val == 'professors' or input_val == 'both':
        for professor_name, class_names in sorted(professors.items()):
            print('{:30} {}'.format(professor_name, class_names))
