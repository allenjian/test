#_*_ coding:UTF-8 _*_
from sys import argv  

script, input_file = argv   #����script��input_file�������������е��������������ֵ������

def print_all(f):  #��f�ļ���ȡ���ӡ��ȫ������
	print f.read()
	
def rewind(f):   #��f�ļ�����ʼλ�ÿ�ʼ�ƶ�
	f.seek(0)
	
def print_a_line(line_count, f):   #��ӡ����������һ�е�����
	print line_count, f.readline()
	
current_file = open(input_file)  #����һ�����ļ��ķ���

print "First let's print the whole file:\n"

print_all(current_file)  #���ú���print_all��ӡ��input_file������

print "Now let's rewind, kind of like a tape."

rewind(current_file)  

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)   #��ӡ��һ������������

current_line += 1
print_a_line(current_line, current_file)   #��ӡ�ڶ�������������

current_line += 1
print_a_line(current_line, current_file)   #��ӡ����������������