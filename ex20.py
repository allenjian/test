#_*_ coding:UTF-8 _*_
from sys import argv  

script, input_file = argv   #定义script、input_file变量，将命令行的两个输入参数赋值给他们

def print_all(f):  #将f文件读取后打印出全部内容
	print f.read()
	
def rewind(f):   #将f文件从起始位置开始移动
	f.seek(0)
	
def print_a_line(line_count, f):   #打印出行数和这一行的内容
	print line_count, f.readline()
	
current_file = open(input_file)  #定义一个打开文件的方法

print "First let's print the whole file:\n"

print_all(current_file)  #调用函数print_all打印出input_file的内容

print "Now let's rewind, kind of like a tape."

rewind(current_file)  

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)   #打印第一行行数和内容

current_line += 1
print_a_line(current_line, current_file)   #打印第二行行数和内容

current_line += 1
print_a_line(current_line, current_file)   #打印第三行行数和内容