import os
import random

# 定义文件夹和文件数量
base_dir = 'resources'
categories = ['almighty-sword-domain']
num_files = 66  # 每个类别创建10个文件
lines_per_file = 50  # 每个文件至少50行内容

# 创建基础文件夹
if not os.path.exists(base_dir):
    os.mkdir(base_dir)

# 内容生成函数
def generate_content(num_lines):
    content = []
    for _ in range(num_lines):
        line = 'This is a sample line number ' + str(random.randint(1, 1000))
        content.append(line)
    return '\n'.join(content)

# 创建文件并写入内容
for category in categories:
    category_dir = os.path.join(base_dir, category)
    if not os.path.exists(category_dir):
        os.mkdir(category_dir)
    
    for i in range(num_files):
        file_path = os.path.join(category_dir, f'ch{i}.txt')
        with open(file_path, 'w') as file:
            content = generate_content(lines_per_file)
            file.write(content)

print(f'{num_files} files created in each category with {lines_per_file} lines each.')
