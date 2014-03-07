
from sys import argv  #导入argv
from os.path import exists  #导入exists

script, from_file, to_file = argv  #定义变量

print "Copying from %s to %s" % (from_file, to_file)  #打印文件名和拷贝文件名

#we could do these two on one line too, how?
in_file = open(from_file)  #定义打开文件
indata = in_file.read()   #定义读取数据

print "The input file is %d bytes long" % len(indata)  #打印源文件内容长度

print "Does the output file exist? %r" % exists(to_file)  #判断复制文件名是否存在
print "Ready, hit RETURN to continue, CTRL-C to abort."  
raw_input()  #继续还是中断

out_file = open(to_file,'w')  #写入模式打开复制文件

out_file.write(indata)  #写入源文件内容

print "Alright, all done."

out_file.close()  
in_file.close()
