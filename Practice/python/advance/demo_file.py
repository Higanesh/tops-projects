
fi = open('demo-file.txt','w')
fi.write("Java is oops language\nJava is secure language\nI am ganesh")
fi.close()

def replace_java_python(file_path,old_word,new_word):
    with open(file_path,'r') as fi:
        data = fi.read()
    modified_data = data.replace(old_word,new_word)
    with open(file_path,'w') as fi:
        fi.write(modified_data)

def line_no_contains_language(file_path,substr):
    # Open the file
    with open(file_path, 'r') as fi:
    # Iterate through each line with line number
        for line_number, line in enumerate(fi, start=1):  # start=1 to start counting from 1
            if substr in line:
                print(f"Line number: {line_number}")
            else:
                pass

def is_oops_exist(file_path,substr):
#     # Open the file
    with open(file_path, 'r') as fi:
    # Iterate through each line with line number
        data = fi.read()
        if substr in data:
            print("oops is exist in a file")
        else:
            print("oops is not exist in a file")

file_path = 'demo-file.txt'

replace_java_python(file_path,'Java','CPP')
line_no_contains_language(file_path,'language')
is_oops_exist(file_path,'oops')



