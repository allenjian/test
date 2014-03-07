from sys import argv  #导入argv包

script, filename = argv  #定义变量

print "We're going to erase %r." % filename  #打印filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")  #键盘输入

print "Opening the file..."
target = open(filename, 'w') #以write模式打开文件

print "Truncating the file. Goodbye!"
target.truncate()   #截断？

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)  #在test中写入raw_input
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()
