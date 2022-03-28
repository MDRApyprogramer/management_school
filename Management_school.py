# Management school

print('hello')
print('welcome')

# import

import sqlite3
from tabulate import tabulate

# connected sql

conn = sqlite3.connect(r'C:\Users\User\AppData\school_sql.db')
c = conn.cursor()

# function is create table

def CtStudent():

    'create table students'

    c.execute('''CREATE TABLE IF NOT EXISTS student (
                fname TEXT,
                lname TEXT,
                gpa INTEGER,
                grade INTEGER,
                age INTEGER
                )''')
    conn.commit()

def CtTeacher():

    'create table teachers'

    c.execute('''CREATE TABLE IF NOT EXISTS teacher(
                fname TEXT,
                lname TEXT,
                age INTEGER,
                lesson TEXT,
                grade TEXT,
                pay TEXT,
                message TEXT
               )''')
    conn.commit()

def CtStudentGpa():

    'Grade point average'

    c.execute('''CREATE TABLE IF NOT EXISTS gpa (
                name TEXT,
                gpa REAL
                    )''')
    conn.commit()

def CtWs():
    c.execute('''CREATE TABLE IF NOT EXISTS ws(
            class_name TEXT,
            week TEXT)''')
    conn.commit()

def CtManagement():
    c.execute('''CREATE TABLE IF NOT EXISTS management(
                fname TEXT,
                lname TEXT,
                age INTEGER,
                pay TEXT,
                message TEXT
               )''')
    conn.commit()

def init():
    CtManagement()
    CtStudent()
    CtStudentGpa()
    CtTeacher()
    CtWs()

# error handling

try :
    c.execute('SELECT * FROM student')
    print('students')
    print(tabulate(c.fetchall()))

    print('teachers')
    c.execute('SELECT * FROM teacher')
    print(tabulate(c.fetchall()))
except sqlite3.OperationalError:
    print('[::::::::::::]')

# this codes for oop

# -----------------------------------------------------------------------------------------------------------------------#

class student:  # this is class for management defines function (add, show, update, delete) for student
    def __init__(self, fname, lname, age, gpa, grade):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.gpa = gpa
        self.grade = grade

    def add(self):
        c.execute('''INSERT INTO student VALUES
        (:fname, :lname, :gpa, :grade, :age)''',
                  {'fname': self.fname, 'lname': self.lname, 'gpa': self.gpa, 'grade': self.grade, 'age': self.age})

    def show_fname(self, fname):
        c.execute('SELECT * FROM student WHERE fname = (:fname)', {'fname': fname})

        print(tabulate(c.fetchall()))

    def show_lname(self, lname):
        c.execute('SELECT * FROM student WHERE lname = (:lname)', {'lname': lname})

        print(tabulate(c.fetchall()))

    def show_age(self, age):
        c.execute('SELECT * FROM student WHERE age = (:age)', {'age': age})

        print(tabulate(c.fetchall()))

    def show_gpa(self, gpa):
        c.execute('SELECT * FROM student WHERE gpa = (:gpa)', {'gpa': gpa})

        print(tabulate(c.fetchall()))

    def show_grade(self, grade):
        c.execute('SELECT * FROM student WHERE grade = (:grade)', {'grade': grade})

        print(tabulate(c.fetchall()))

    def update_age(self, age, fname, lname):
        c.execute('''UPDATE student SET age = (:age)
        WHERE fname = (:fname) AND lname = (:lname)''',
                  {'age': age, 'fname': fname, 'lname': lname})

    def update_gpa(self, gpa, fname, lname):
        c.execute('''UPDATE student SET gpa = (:gpa)
        WHERE fname = (:fname) AND lname = (:lname)''',
                  {'fname': fname, 'lname': lname, 'gpa': gpa})

    def update_grad(self, grade, fname, lname):
        c.execute('''UPDATE student SET grade = (:grade)
        WHERE fname = (:fname) AND lname = (:lname)''',
                  {'fname': fname, 'lname': lname, 'grade': grade})

    def delete(self, fname, lname):
        c.execute('''DELETE FROM student WHERE fname = (:fname) AND lname = (:lname)''',
                  {'fname': fname, 'lname': lname})


# -----------------------------------------------------------------------------------------------------------------------#

class teachers:  # this is class for management defines function (add, show, update, delete) for teacher
    def __init__(self, fname, lname, age, lesson, grade, message, pay):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.lesson = lesson
        self.grade = grade
        self.message = message
        self.pay = pay

    def add(self):
        c.execute('INSERT INTO teacher VALUES (:fname , :lname , :age , :lesson , :grade , :pay , :message)',
                  {'fname': self.fname, 'lname': self.lname, 'age': self.age, 'lesson': self.lesson,
                   'grade': self.grade, 'pay': self.pay, 'message': self.message})

    def show_fname(self, fname, a):
        c.execute(f'SELECT * FROM {a} WHERE fname = (:fname)', {'fname': fname})

        print(tabulate(c.fetchall()))

    def show_lname(self, lname, a):
        c.execute(f'SELECT * FROM {a} WHERE lname = (:lname)', {'lname': lname})

        print(tabulate(c.fetchall()))

    def show_age(self, age, a):
        c.execute(f'SELECT * FROM {a} WHERE age = (:age)', {'age': age})

        print(tabulate(c.fetchall()))

    def show_lesson(self, lesson):
        c.execute('SELECT * FROM teacher WHERE lesson = (:lesson)', {'lesson': lesson})

        print(tabulate(c.fetchall()))

    def show_grade(self, grade):
        c.execute('SELECT * FROM teacher WHERE grade = (:grade)', {'grade': grade})

        print(tabulate(c.fetchall()))

    def show_pay(self, pay, a):
        c.execute(f'SELECT * FROM {a} WHERE pay = (:pay)', {'pay': pay})

        print(tabulate(c.fetchall()))

    def update_age(self, age, fname, lname, a):
        c.execute(f'''UPDATE {a} SET age = (:age)
        WHERE fname = (:fname) AND lname = (:lname)''',
                  {'age': age, 'fname': fname, 'lname': lname})

    def update_pay(self, pay, fname, lname, a):
        c.execute(f'''UPDATE {a} SET pay = (:pay)
        WHERE fname = (:fname) AND lname = (:lname)''',
                  {'fname': fname, 'lname': lname, 'pay': pay})

    def update_grad(self, grade, fname, lname):
        c.execute('''UPDATE teacher SET grade = (:grade)
        WHERE fname = (:fname) AND lname = (:lname)''',
                  {'fname': fname, 'lname': lname, 'grade': grade})

    def update_msg(self, msg, fname, lname):
        c.execute('''UPDATE teacher SET message = (:msg)
        WHERE fname = (:fname) AND lname = (:lname)''',
                  {'fname': fname, 'lname': lname, 'msg': msg})

    def delete(self, fname, lname, grade):
        c.execute('DELETE FROM teacher WHERE fname = (:fname) AND lname = (:lname) AND grade = (:grade)',
                  {'fname': fname, 'lname': lname, 'grade': grade})


# -----------------------------------------------------------------------------------------------------------------------#

class gpa:  # this is class for management defines function (add, show, update, delete) for Grade point average

    def __init__(self, name, Science, Math, Persian, Writing, dictation, Arabic, Heavenly_messages, BT, Quran, social,
                 English, Physical_education):
        self.name = name
        self.gpa = f'Science : {Science}, Math : {Math}, Persian : {Persian}, Writing : {Writing}, dictation : {dictation}, Arabic : {Arabic}, Heavenly messages : {Heavenly_messages}, {BT}, Quran : {Quran}, Social : {social}, English : {English}, Physical education : {Physical_education}'

    def add(self):
        c.execute('INSERT INTO gpa VALUES (:name, :gpa)', {'name': self.name, 'gpa': self.gpa})

    def show(self, name):
        c.execute('SELECT * FROM gpa WHERE name = (:name)', {'name': name})
        print(tabulate(c.fetchall()))

    def update_gpa(self, name, Science=0, Math=0, Persian=0, Writing=0, dictation=0, Arabic=0, Heavenly_messages=0, BT=0, Quran=0, social=0, English=0, Physical_education=0):
        gpa = f'Science : {Science}, Math : {Math}, Persian : {Persian}, Writing : {Writing}, dictation : {dictation}, Arabic : {Arabic}, Heavenly messages : {Heavenly_messages},Business and Technology : {BT}, Quran : {Quran}, Social : {social}, English : {English}, Physical education : {Physical_education}'
        c.execute('UPDATE gpa SET gpa = (:gpa) WHERE name = (:name)',
                  {'gpa': gpa, 'name': name})

    def delete(self, name):
        c.execute('DELETE FROM gpa WHERE name = (:name)', {'name': name})


# -----------------------------------------------------------------------------------------------------------------------#

class Ws:  # this is class for management defines function (add, show, update, delete) for Weekly schedule
    def __init__(self, class_name, one: list, two: list, tree: list, fore: list, five: list):
        self.week = f'''

        {one[0]} {one[1]} {one[2]}
        {two[0]} {two[1]} {two[2]}
        {tree[0]} {tree[1]} {tree[2]}
        {fore[0]} {fore[1]} {fore[2]}
        {five[0]} {five[1]} {five[2]}'''
        self.class_name = f'''{class_name}
        '''

    def add(self):
        c.execute('INSERT INTO ws VALUES(:class_name , :week)', {'class_name': self.class_name, 'week': self.week})

    def show(self, name):
        c.execute('SELECT * FROM ws ')

        my_v = c.fetchall()
        for i in my_v:
            for a in i:
                if a[:len(name)] == name:
                    print(a[:len(name)])
                    b = i[1]
                    print(tabulate(b))

    def update(self, class_name, one: list, two: list, tree: list, fore: list, five: list):
        week = f'''

                {one[0]} {one[1]} {one[2]}
                {two[0]} {two[1]} {two[2]}
                {tree[0]} {tree[1]} {tree[2]}
                {fore[0]} {fore[1]} {fore[2]}
                {five[0]} {five[1]} {five[2]}
                '''

        c.execute('''UPDATE ws SET week = (:week) WHERE class_name = (:class_name)''',
                  {'week': week, 'class_name': class_name})

    def delete(self, name):
        c.execute('DELETE FROM ws WHERE class_name = (:name)', {'name': name})


# -----------------------------------------------------------------------------------------------------------------------#

class management():  # this is class for management defines function (add, show, update, delete) for management
    def __init__(self, fname='management first name', lname='management last name', age='management age', message='...',
                 pay=200):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.message = message
        self.pay = pay

    def add(self):
        c.execute('INSERT INTO management VALUES (:fname, :lname, :age, :pay, :message)',
                  {'fname': self.fname, 'lname': self.lname, 'age': self.age, 'pay': self.pay, 'message': self.message})

    def show_fname(self, fname, a):
        c.execute(f'SELECT * FROM {a} WHERE fname = (:fname)', {'fname': fname})

        print(tabulate(c.fetchall()))

    def show_lname(self, lname, a):
        c.execute(f'SELECT * FROM {a} WHERE lname = (:lname)', {'lname': lname})

        print(tabulate(c.fetchall()))

    def show_age(self, age, a):
        c.execute(f'SELECT * FROM {a} WHERE age = (:age)', {'age': age})

        print(tabulate(c.fetchall()))

    def show_pay(self, pay, a):
        c.execute(f'SELECT * FROM {a} WHERE pay = :pay', {'pay': pay})

        print(tabulate(c.fetchall()))

    def update_age(self, age, fname, lname, a):
        c.execute(f'''UPDATE {a} SET age = (:age)
        WHERE fname = (:fname) AND lname = (:lname)''',
                  {'age': age, 'fname': fname, 'lname': lname})

    def update_pay(self, pay, fname, lname, a):
        c.execute(f'''UPDATE {a} SET pay = (:pay)
        WHERE fname = (:fname) AND lname = (:lname)''',
                  {'fname': fname, 'lname': lname, 'pay': pay})

    def update_msg(self, msg, fname, lname):
        c.execute(f'''UPDATE management SET message = (:msg)
        WHERE fname = (:fname) AND lname = (:lname)''',
                  {'fname': fname, 'lname': lname, 'msg': msg})

    def delete(self, fname, lname):
        c.execute('''DELETE FROM management WHERE fname = (:fname) AND lname = (:lname)''',
                  {'fname': fname, 'lname': lname})



# defines in menu and program pages

    # defines functions add

def page_add_gpa():

    list_gpa = ['name','Science','Math','Persian','Writing','dictation','Arabic','Heavenly messages','BT','Quran','social','English','Physical education']
    list_ga = []

    for i in list_gpa:
        i = i + ' : '
        if i != 'name : ':
            a = int(input(i))
        elif i == 'name : ':
            a = input(i)
        list_ga.append(a)

    __gpa__ = gpa(list_ga[0], list_ga[1], list_ga[2], list_ga[3], list_ga[4], list_ga[5], list_ga[6], list_ga[7], list_ga[8], list_ga[9], list_ga[10], list_ga[11], list_ga[12])

    __gpa__.add()

def page_add_weekly_schedule():
    week = ('saturday', 'sunday', 'monday', 'tusday', 'wednesday')
    bell = ['first', 'Second', 'Third']

    inputing = '{} , bell {} : '

    class_name = input('class name : ')

    list_weekday = []

    for i in week:
        for a in bell:
            b = input(inputing.format(i, a))
            list_weekday.append(b)

    list_weekday = [list_weekday[0:3], list_weekday[3:6], list_weekday[6:9], list_weekday[9:12], list_weekday[12:]]

    __weekly_schedule__ = Ws(class_name,list_weekday[0], list_weekday[1], list_weekday[2], list_weekday[3], list_weekday[4])
    __weekly_schedule__.add()


def page_add_management():
    fname = input('first name : ')
    lname = input('last name : ')
    age = input('age : ')
    message = input('message : ')
    pay = input('pay : ')

    __managment__ = management(fname, lname, age, message, pay)

    __managment__.add()

def page_add_teacher():
    fname = input('first name : ')
    lname = input('last name : ')
    age = input('age : ')
    lesson = input('lesson : ')
    grade = input('grade : ')
    message = input('message : ')
    pay = input('pay : ')

    __teacher__ = teachers(fname, lname, age, lesson, grade, message, pay)

    __teacher__.add()

def page_add_student():
    fname = input('first name : ')
    lname = input('last name : ')
    age = input('age : ')
    gpa = input('Grade point average : ')
    grade = input('grade : ')

    __student__ = student(fname, lname, age, gpa, grade)

    __student__.add()

def add():

    list_add = ['Student','Teacher','Management','Weekly Schedule','gpa(Grade point average)', 'back']
    tuple_st = ('student', 'Student' , 's')
    tuple_tr = ('teacher' , 'Teacher' , 't')
    tuple_mt = ('Management','management','m')
    tuple_ws = ('ws', 'weekly schedule', 'Weekly schedule', 'Weekly Schedule', 'w')
    tuple_gpa= ('gpa', 'Gpa', 'GPA', 'Grade point average', 'Grade Point Average', 'grade point average', 'g', 'G')

    print(list_add)

    adet = input('/')

    if adet in tuple_st :
        page_add_student()

    elif adet in tuple_tr :
        page_add_teacher()

    elif adet in tuple_mt :
        page_add_management()

    elif adet in tuple_ws :
        page_add_weekly_schedule()

    elif adet in tuple_gpa:
        page_add_gpa()

    elif adet == 'back':
        pass

    else :
        print('I did not understand what you meant')
        add()

    # defines function show

def show_student():
    list_show = ['first name', 'last name', 'age','grnde point average(gpa)', 'grade', 'back']

    print(list_show)

    a = student('x','y','n','n','n')

    shs = input('/')

    if shs == 'first name' or shs == 'f':
        b = input('first name : ')
        a.show_fname(b)

    elif shs == 'last name' or shs == 'l':
        b = input('last name : ')
        a.show_lname(b)

    elif shs == 'age' or shs == 'a':
        b = input('age : ')
        a.show_age(b)

    elif shs == 'gpa' or shs == 'grande point average':
        b = input('Grade point average : ')
        a.show_gpa(b)

    elif shs == 'grade' or shs == 'g' :
        b = input('grand : ')
        a.show_grade(b)

    elif shs == 'back':
        show()

    else :
        print('I did not understand what you meant')


def show_teacher():
    a = teachers('x','y','n','n','n', 'x','x')

    list_show = ['first name', 'last name', 'age', 'lesson', 'grade', 'pay', 'back']
    print(list_show)

    shs = input('/')

    if shs == 'first name' or shs == 'f':
        b = input('first name : ')
        a.show_fname(b,'teacher')

    elif shs == 'last name' or shs == 'l':
        b = input('last name : ')
        a.show_lname(b,'teacher')

    elif shs == 'age' or shs == 'a':
        b = input('age : ')
        a.show_age(b,'teacher')

    elif shs == 'lesson' or shs == 'le':
        b = input('lesson : ')
        a.show_lesson(b)

    elif shs == 'grade' or shs == 'g':
        b = input('grande : ')
        a.show_grade(b)

    elif shs == 'pay' or shs == 'p':
        b = input('pay : ')
        a.show_pay(b,'teacher')

    elif shs == 'back':
        show()

    else :
        print('I did not understand what you meant')

def show_management():
    a = management('x','y','n','n','n')

    list_show = ['first name', 'last name', 'age', 'pay', 'back']
    print(list_show)

    shm = input('/')

    if shm == 'first name' or shm == 'f':
        b = input('first name : ')
        a.show_fname(b,'management')

    elif shm == 'last name' or shm == 'l':
        b = input('last name : ')
        a.show_lname(b,'management')

    elif shm == 'age' or shm == 'a':
        b = input('age :')
        a.show_age(b,'management')

    elif shm == 'pay' or shm == 'p':
        b = input('pay : ')
        a.show_pay(b,'management')

    elif shm == 'back':
        show()

    else :
        print('I did not understand what you meant')

def show_ws():
    a = input('class name : ')
    list_E = ['','','']
    b = Ws('class name', list_E, list_E, list_E, list_E, list_E)

    b.show(a)

def show_gpa():
    name = input('name : ')
    a = gpa(name,0,0,0,0,0,0,0,0,0,0,0,0)
    a.show(name)

def show():
    list_show = ['Student','Teacher','Management','Weekly Schedule','gpa(Grade point average)']
    tuple_st = ('student', 'Student' , 's')
    tuple_tr = ('teacher' , 'Teacher' , 't')
    tuple_mt = ('Management','management','m')
    tuple_ws = ('ws', 'weekly schedule', 'Weekly schedule', 'Weekly Schedule', 'w')
    tuple_gpa= ('gpa', 'Gpa', 'GPA', 'Grade point average', 'Grade Point Average', 'grade point average', 'g', 'G')
    tuple_show = ('show', 'show all', 'Show all', 'sa', 'Show All')

    print(list_show)

    shet = input('/')

    if shet in tuple_st :
        show_student()

    elif shet in tuple_tr :
        show_teacher()

    elif shet in tuple_mt :
        show_management()

    elif shet in tuple_ws :
        show_ws()

    elif shet in tuple_gpa:
        show_gpa()

    elif shet in tuple_show:
        dict_for_show = {
            'student' : 'student',
            'teacher' : 'teacher',
            'management' : 'management',
            'weekly schedule' : 'ws',
            'grade point average' : 'gpa'
        }

        for i in dict_for_show:
            print(i)
            c.execute(f'SELECT * FROM {dict_for_show.get(i)}')
            print(tabulate(c.fetchall()))

    else :
        print('I did not understand what you meant')
        show()

def update_gpa():
    _gpa = gpa('','','','','','','','','','','','','')

    name = input('Name : ')

    try :

        _gpa.update_gpa(name, '','','','','','','','','','','','')

    except sqlite3.InterfaceError:
        print('this user , not in database')
        list_c = ([['Add this user to the database', 'Agane', 'back']])
        print(list_c)
        command = input('/')
        if command == 'add' or command == 'Add this user to the database' :
            print(f'first name : {name}')

            Science = input('Science : ')
            Math = input('Math : ')
            Persian = input('Persian : ')
            Writing = input('Writing : ')
            dictation = input('Dictation : ')
            Arabic = input('Arabic : ')
            Heavenly_messages = input('Heavenly messages : ')
            BT = input('Business and Technology : ')
            Quran = input('Quran : ')
            social = input('SOcial : ')
            English = input('English : ')
            Physical_education = input('Physical education')

            a = gpa(name, Science, Math, Persian, Writing, dictation, Arabic, Heavenly_messages, BT, Quran, social, English, Physical_education)
            a.add()

        elif command == 'agane' or command == 'a':
            update_gpa()

        elif 'back':
            ing()
    else :
        Science = input('Science : ')
        Math = input('Math : ')
        Persian = input('Persian : ')
        Writing = input('Writing : ')
        dictation = input('Dictation : ')
        Arabic = input('Arabic : ')
        Heavenly_messages = input('Heavenly messages : ')
        BT = input('Business and Technology : ')
        Quran = input('Quran : ')
        social = input('SOcial : ')
        English = input('English : ')
        Physical_education = input('Physical education')
        _gpa.update_gpa(name, Science, Math, Persian, Writing, dictation, Arabic, Heavenly_messages, BT, Quran, social, English, Physical_education)

def update_ws():
    week = ('saturday', 'sunday', 'monday', 'tusday', 'wednesday')
    bell = ['first', 'Second', 'Third']

    inputing = '{} , bell {} : '

    class_name = input('class name : ')

    list_weekday = []

    for i in week:
        for a in bell:
            b = input(inputing.format(i, a))
            list_weekday.append(b)

    list_weekday = [list_weekday[0:3], list_weekday[3:6], list_weekday[6:9], list_weekday[9:12], list_weekday[12:]]

    __weekly_schedule__ = Ws(class_name,list_weekday[0], list_weekday[1], list_weekday[2], list_weekday[3], list_weekday[4])
    __weekly_schedule__.update(class_name, list_weekday[0], list_weekday[1], list_weekday[2], list_weekday[3], list_weekday[4])


def update_management():
    _management = management('f', 'l', 20, 'm', 200)
    list_update = ['age', 'message', 'pay']
    print(list_update)

    ue = input('/')

    f = input('first name : ')
    l = input('last name : ')
    m = 'management'

    if ue == 'age' or ue == 'a':
        age = input('age : ')
        _management.update_age(age, f, l, m)

    elif ue == 'message' or ue == 'm':
        msg = input('message : ')
        _management.update_msg(msg, f, l)

    elif ue == 'pay' or ue == 'p':
        pay = input('pay : ')
        _management.update_pay(pay, f, l, m)


def update_teacher():
    _teacher = teachers('fname', 'lname', 20, 'math', 9, 'none', 500)
    list_update = ['age','grade','message','pay']
    print(list_update)

    ue = input('/')

    f = input('first name : ')
    l = input('last name : ')

    if ue == 'age' or ue == 'a':
        age = int(input('age : '))
        _teacher.update_age(age,f, l, 'teacher')

    elif ue == 'grade' or ue == 'g':
        grade = input('grade : ')
        _teacher.update_grad(grade,f,l)

    elif ue == 'message' or ue == 'm':
        msg = input('message : ')
        _teacher.update_msg(msg, f, l)

    elif ue == 'pay' or ue == 'p':
        pay = input('pay : ')
        _teacher.update_pay(pay ,f ,l ,'teacher')


def update_student():
    a = list([['age', 'Grade point average', 'grade']])

    print(tabulate(a))

    ue = input('/')
    fname = input('first name : ')
    lname = input('last name : ')
    uet = input(f'{ue} : ')

    _student = student('fname', 'lname', 15, 20, 9)
    list_update = ['age',_student.update_age,
                    'gpa',_student.update_gpa,
                    'grade point average',_student.update_gpa,
                    'grade',_student.update_grad]

    for i in list_update :
        if ue == i :
            a = list_update.index(i)
            a += 1
            func = list_update[a]
            func(fname, lname, uet)


def update():
    list_update = {'Student' : update_student,
                    'Teacher' : update_teacher,
                    'Management' : update_management,
                    'Weekly Schedule' : update_ws,
                    'gpa(Grade point average)' : update_gpa,
                    's' : update_student,
                    't' : update_teacher,
                    'm' : update_management,
                    'ws': update_ws,
                    'gpa' : update_gpa
    }

    for i in list_update:
        print(i, end = ' , ')
        if i == 'gpa(Grade point average)':
            break

    print('back')

    ue = input('/')

    for i in list_update :
        if ue == i :
            func = list_update.get(i)
            func()

    if ue == 'back':
        pass

    elif ue is not 'back' and ue not in list(list_update.keys()):
        print('I did not understand what you meant')
        update()

def delete():
    a = {
        'Student' : [
            'student',
            'Student',
            's', 's'
        ],


        'Teacher' : [
            'teacher',
            'Teacher',
            't', 'T'
        ],


        'Management' : [
            'management',
            'Management',
            'm', 'M'
        ],


        'Week schedule' : [
            'weekly schedule',
            'Weekly schedule',
            'Weekly Schedule',
            'ws', 'Ws', 'WS',
            'weeklyschdule',
            'Weeklyschdule',
            'WeeklySchdule'
        ],


        'Grade point average' : [
            'Grade point average',
            'grade point average',
            'Grade Point Average',
            'GPA', 'gpa', 'Gpa'
        ],


        'back' : 'back'
    }

    for i in list(a.keys()):
        print(i, end=' , ')

    print('')

    de = input('/')

    if de in a.get('Management'):
        f , l = input('first name : ') , input('last name : ')
        a = management('','','','','')
        a.delete(f, l)

    elif de in a.get('Student'):
        f , l  = input('first name : ') , input('last name : ')
        a = student('','','','','')
        a.delete(f,l,)

    elif de in a.get('Teacher'):

        f , l , g = input('first name : ') , input('last name : ') , input('grade : ')
        a = teachers('','','','','','','')
        a.delete(f,l,g)

    elif de in a.get('Week schedule'):
        n = input('name : ')
        List = ['','','']
        a = Ws('',List,List,List,List,List)
        a.delete(n)

    elif de in a.get('Grade point average'):
        n = input('name : ')
        a = gpa('','','','','','','','','','','','','')
        a.delete(n)

    elif de == 'back':
        pass

    else :
        print('I did not understand what you meant')
        delete()

def ing():
    print('menu')

    List_manu = ['add', 'show', 'update', 'delete', 'exit']

    print('******************************************************')

    for a in List_manu:
        if a != 'exit':
            print(a, end = '* *')
    print('exit')

    print('******************************************************')

    menu = input('/')

    if menu == 'add' or menu == 'a':
        add()

    elif menu == 'show' or menu == 's':
        show()

    elif menu == 'update' or menu == 'u':
        update()

    elif menu == 'delete' or menu == 'd':
        delete()

    elif menu == 'exit' :
        exit()

    else :
        print('I did not understand what you meant')

while True:
    init()
    print('pleas wait')
    ing()
