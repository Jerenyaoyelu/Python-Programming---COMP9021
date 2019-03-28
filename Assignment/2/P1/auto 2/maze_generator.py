#coding=utf-8
#Written by Ricky Qi and Xin Li for COMP9021 Assignment 2


from random import seed, choice, randint
import os
import sys
import difflib
import argparse

def readfile(filename):
    try:
        with open(filename, 'r') as fileHandle:
            text = fileHandle.read().splitlines()
        return text
    except IOError as e:
        print("Read file Error:", e)
        sys.exit()

arg_for_seed = input('Please input a seed:')
file_name = input('Please input the name of file that you want to create to store txt and tex files: ').split()
file_name = '_'.join(file_name)
print(file_name)
print("检测并移除冲突文件夹")
os.system(f'rm -r {file_name}')
os.mkdir(file_name)
os.mkdir(file_name + '/tex')

times = int(input('How many maze TXT do you want to generate?: '))

#Written by Ricky Qi and Xin Li for COMP9021 Assignment 2
all_blocks = ('0', '1', '2', '3')
right_blocks = ('0', '2')
bottom_blocks = ('0', '1')
seed(arg_for_seed)

for i in range(times):
#Written by Ricky Qi and Xin Li for COMP9021 Assignment 2
    num_of_rows = randint(2, 41)
    num_of_cols = randint(2, 31)
    with open(f'{file_name}/{file_name}_{i}.txt', 'w') as f:
        for row in range(num_of_rows - 1):
            for col in range(num_of_cols - 1):
                f.write(choice(all_blocks))
            f.write(choice(right_blocks) + '\n')
        for col in range(num_of_cols - 1):
            f.write(choice(bottom_blocks))
        f.write('0')
#Written by Ricky Qi and Xin Li for COMP9021 Assignment 2
print(f'txt documents have already out put to {file_name}')
ERR = []
the_analyse = []
a_err = []
for i in range(times):
    command = f'python3 -c "from maze import *;maze = Maze(\'{file_name}/{file_name}_{i}.txt\');maze.display()"'
    os.system(command)


    print(f"正在处理... {file_name}_{i}.tex")
    print("文件已经生成，开始比较...")
    temp = os.popen(f'diff {file_name}/{file_name}_{i}.tex {file_name}_test/{file_name}_test_{i}.tex')
    info = temp.readlines()
    if len(info) != 0:
        print(f"文件存在差异，已存储到{file_name}_report.txt")
        ERR.append(f"错误文件信息{file_name}_{i}.tex")
        for line in info:
            print(line.strip())
            ERR.append(line.strip())
    else:
        print("文件无差异，Pass")
os.system(f'rm {file_name}_report.txt')
print("正在生成display()相关错误日志...")
with open(f'{file_name}_display_report.txt', 'w') as f:
    for e in ERR:
        print(e, file = f)

# Written by Ricky and Xin Li for COMP9021 Assignment 2

print("开始测试analyse模块")


for i in range(times):
    command1 = f'python3 -c "from maze import *;maze = Maze(\'{file_name}/{file_name}_{i}.txt\');maze.analyse()"'
    analyse = os.popen(command1)
    info_analyse = analyse.readlines()
    the_analyse.append(f'{file_name}_{i}.txt')
    print(f'正在处理{file_name}_{i}.txt...')
    for line1 in info_analyse:
        the_analyse.append(line1.strip())

print(f"将analyse()信息转储至文件{file_name}_analyse.txt中...")
with open(f'{file_name}_analyse.txt', 'w') as f1:
    for x in the_analyse:
        print(x, file = f1)

text1 = readfile(f'{file_name}_analyse.txt')
text2 = readfile(f'{file_name}_test_analyse.txt')
d = difflib.HtmlDiff()
result = d.make_file(text1, text2, f'{file_name}_analyse.txt', f'{file_name}_test_analyse.txt', context=True)

with open(f'{file_name}_analyse_report.html', 'w') as resultfile:
    resultfile.write(result)


# Written by Ricky and Xin Li for COMP9021 Assignment 2
