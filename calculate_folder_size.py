# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 16:15:16 2021
"""
import os
import os.path

import os
import os.path


def calculate_total_size(folder_path):
    total_size = 0
    for file_name in os.listdir(folder_path):
        path = os.path.join(folder_path, file_name)
        if os.path.isdir(path):  # 递归调用，计算子孙文件夹中所包含的文件总大小
            total_size = total_size + calculate_total_size(path)
        if os.path.isfile(path):  # 直接计算
            total_size = total_size + os.path.getsize(path)
    return total_size

def calculate_total_size_2(path):
    '''
    返回的是一个三元组(root,dirs,files)。

    root 所指的是当前正在遍历的这个文件夹的本身的地址
    dirs 是一个 list ，内容是该文件夹中所有的目录的名字(不包括子目录)
    files 同样是 list , 内容是该文件夹中所有的文件(不包括子目录)
    '''
    lst_files = os.walk(path)
    
    total = 0
    for dirpath,dirname,filename in lst_files:
        #print(dirpath)
        #print(dirname)
        #print(filename)
        for f in filename:
            total += os.path.getsize(os.path.abspath(dirpath+'\\'+f))
        #total += os.path.getsize(os.path.abspath(filename))
        print('---------------')
    return total


    
def main():
    path = r'C:\Users\未央\.spyder-py3\socket\socket1.2'
    print(calculate_total_size(path),'MB')
    print(calculate_total_size_2(path),'MB')
    
    
if __name__ == "__main__":
    main()