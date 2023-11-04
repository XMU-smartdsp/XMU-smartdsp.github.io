import os

# 指定文件夹路径
folder_path = "./"

# 遍历文件夹内的所有文件
for filename in os.listdir(folder_path):
    # 检查是否是文件
    if os.path.isfile(os.path.join(folder_path, filename)):
        # 将文件名分割为文件名和后缀名
        name, ext = os.path.splitext(filename)

        # 将后缀名从大写转为小写
        ext = ext.lower()

        # 构建新的文件名
        new_filename = name + ext

        # 重命名文件
        os.rename(
            os.path.join(folder_path, filename), os.path.join(folder_path, new_filename)
        )
