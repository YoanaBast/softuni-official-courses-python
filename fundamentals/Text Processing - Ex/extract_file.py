path = input().split('\\')
file_ext = path[-1]
file, extention = file_ext.split('.')
print(f"File name: {file}")
print(f"File extension: {extention}")
