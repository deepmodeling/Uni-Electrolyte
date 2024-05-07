def read_last_line(file_path):
    with open(file_path, 'rb') as f:
        f.seek(-2, 2)  # 跳到文件的倒数第二个字节
        while f.read(1) != b'\n':  # 查找最后一行的开头
            f.seek(-2, 1)
        last_line = f.readline()  # 读取最后一行
        return last_line.decode('utf-8')  # 解码（如果是文本文件）
