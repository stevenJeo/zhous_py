import os

# os.rename("file2.txt", "file.txt") #对文件重命名
# os.remove("file.txt") #删除一个已存在的文件
os.mkdir("director")  # 创建目录,若存在报错
cwd = os.getcwd()  # 显示当前目录
print ("当前目录为：",cwd)
os.chdir("director")  # 改变当前位置到指定目录，如“/usr/bin”
cwd = os.getcwd()
print("当前目录为：", cwd)

os.rmdir("director")  # 相对路径从当前位置搜索