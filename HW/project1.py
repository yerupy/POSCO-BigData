import sys
import os
import copy

def avg_1(a, b):
    avg = (a + b) /2
    if avg >= 90:
        grade = 'A'
    elif int(avg) >= 80:
        grade = 'B'
    elif int(avg) >= 70:
        grade = 'C'
    elif int(avg) >= 60:
        grade = 'D'
    else:
        grade = 'F'
    return avg, grade

def print_():
    print(' Student'+' '*15+'Name'+'   Midterm'+'  Final'+'  Average'+'  Grade')
    print('-'*63)

def show():
    print_()
    stu_list.sort(key=lambda e : e[4],reverse=True)
    for i in stu_list:
        print('\t'.join(i))
    
def search(n, a, list):
    cnt = 0
    for i in stu_list:
        if i[n] == a:
            cnt += 1
            return i
        else:
            pass
    if cnt == 0:
        return None
        
def changescore(c, n):
    if int(c) > 100 or int(c) < 0:
        pass
    else:
        for i, j in zip(stu_list1, stu_list):
            if i[0] == stu_id:
                i[n] = c
                avg, grade = avg_1(int(i[2]), int(i[3]))
                i[4] = (str(avg))
                i[5] = (grade)
                print_()
                print('\t'.join(j))
                print('Score changed.')
                print('\t'.join(i))

if len(sys.argv) > 1:
    fr = open(sys.argv[1],'r')
    data = fr.read()
    fr.close()

elif len(sys.argv)== 1:
    with open('students.txt','r') as fr:
        data = fr.read()
        fr.close()

data = data.split('\n')
stu_list = []
for i in data:
    stu_list.append(i.split('\t'))
for i in stu_list:
    avg, grade = avg_1(int(i[2]),int(i[3]))
    i.append(str(avg))
    i.append(grade)

while True:
    a = input('#')
    a = a.lower()
    
    #show 설정
    if a == 'show':
        show()

    #search 설정        
    if a == 'search':
        stu_id = input('Student ID: ')
        i = search(0, stu_id, stu_list)
        if i != None:
            print_()
            print('\t'.join(i))
        else:
            print('NO SUCH PERSON')


    #changescore 설정
    if a == 'changescore':
        stu_id = input('Student ID: ')
        stu_list1 = copy.deepcopy(stu_list)
        i = search(0, stu_id, stu_list)
        if i == None:
            print('NO SUCH PERSON')
        for j in stu_list1:
            if j[0] == stu_id:
                b = input('Mid/Final?')
                if b == 'mid':
                    c = input('Input new score: ')
                    changescore(c, 2)
                elif b == 'final':
                    c = input('Input new score: ')
                    changescore(c, 3)
        stu_list = stu_list1

    #add 설정
    if a == 'add':
        stu_id = input('Student ID: ')
        if search(0, stu_id, stu_list) != None:
            print('ALREADY EXISTS')
        else:
            name = input('Name :')
            mid = input('Midterm Score: ')
            final = input('Final Score: ')
            print('Student added.')
            list_ = [stu_id, name, mid, final]
            avg, grade = avg_1(int(list_[2]),int(list_[3]))
            list_.append(str(avg))
            list_.append(grade)
            stu_list.append(list_)

    #searchgrade 설정
    if a == 'searchgrade':
        grade = input('Grade to search: ')
        cnt = 0
        g_list = ['A','B','C','D','F']
        if grade in g_list:
            list_ = []
            for i in stu_list:
                if i[5] == grade:
                    cnt +=1
                    list_.append(i)
            if cnt == 0:
                print('NO RESULTS.')
            else:
                print_()
                for i in list_:
                    print('\t'.join(i))

    #remove 설정
    if a == 'remove':
        if len(stu_list) == 0:
            print('List is empty')
        else:
            stu_id = input('Student ID: ')
            i = search(0, stu_id, stu_list)
            if i != None:
                stu_list.remove(i)
                print('Student removed.')
            else:
                print('NO SUCH PERSON')

    #quit 설정
    if a == 'quit':
        answer = input('Save data?[yes/no]: ')
        if answer == 'yes':
            f_name = input('File name: ')
            fw = open(f_name,'w')
            stu_list.sort(key=lambda e : e[4],reverse=True)
            for i in stu_list:
                data = '\t'.join(i[0:4]) + '\n'
                fw.write(data)
            fw.close()
            break