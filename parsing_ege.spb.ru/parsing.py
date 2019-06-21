import requests
import csv


def get_result(html):
    names = [line for line in html.split('\n') if 'exam-title' in line]
    names = [name.split('>')[1].split('<')[0].strip() for name in names[1:]]
    res = [line for line in html.split('\n') if 'exam-result ' in line]
    if res != []:
        res = [res[i].split('>')[1].split('<')[0] for i in range(len(res))]
        return res, names
    else:
        return '', ''


def parsing(series, number):
    url = 'https://www.ege.spb.ru/result/index.php?mode=ege2019&wave=0'
    payload = {'Series': series, 'Number': number, 'Login': '%CF%EE%EA%E0%E7%E0%F2%FC+%F0%E5%E7%F3%EB%FC%F2%E0%F2%FB'}
    resp = requests.post(url, payload)
    if resp.status_code == 200:
        return resp.text
    else:
        return False

def main():
    with open('Students.csv', 'r') as f:
        cin = csv.DictReader(f, fieldnames=['class', 'first_name', 'second_name', 'third_name', 'series', 'number'])
        students = [row for row in cin]

    names_all = set()
    for student in students:
        print(student['first_name'])
        html = parsing(student['series'], student['number']) 
        res, names = get_result(html)
        if res != '':
            for i, name in enumerate(names):
                names_all.add(name)
                student[name] = res[i]
        if student['first_name'] == 'Крамник':
            student['Математика профильная'] = '92'
            student['Русский язык'] = '87'
            student['Физика'] = '78'

    print('parsing finished')
    print('\n'.join(names_all))

    with open('students.csv', 'w') as f:
        cout = csv.DictWriter(f, ['class', 'first_name', 'second_name', 'third_name', 'series', 'number'] + list(names_all))
        cout.writeheader()
        cout.writerows(students)

if __name__ == '__main__':
    main()
