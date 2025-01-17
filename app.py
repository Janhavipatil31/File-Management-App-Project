import os

def create_file(filename):
    try:
        with open(filename,'x') as f:
            print(f"file Name {filename}: created successfully!")
    except FileExistsError:
        print(f'file name {filename} already exists!')

    except Exception as E:
        print('An error occured!')

def view_all_files():
    files=os.listdir()
    if not files:
        print("No file found!")
    else:
        print("files in directory!")
        for file in files:
            print(file)

def delete_file(filename):
    try:
        os.remove(filename)
        print("filename has been deleted successfully!")
    except FileNotFoundError:

        print("file not found")
    except Exception as e:
        print("An error occured!")


def read_file(filename):
    try:
        with open('Untitled-1.txt','r') as f:
            content=f.read()
            print(f"content of '{filename}' :\n{content}")

    except FileNotFoundError:
        print(f"{filename} doesn't exist!")
    except Exception as f:
        print('An error occurred!')

def edit_file(filename):
    try:
        with open('Untitled-1.txt','a') as f:
            content=input('enter data to add=')
            f.write(content+"\n")
            print('content added to{filename} successfully!')
    except FileNotFoundError:
        print(f"{filename} doesn't exist!")
    except Exception as e:
        print('An error occured!')

def main():
    while True:
        print('FILE MANAGEMENT APP')
        print('1: create file')
        print('2: view all files')
        print('3: delete file')
        print('4: read file')
        print('5: edit file')
        print('6: Exist')
        
           
        choice=input('Enter your choice(1-6)=')

        if choice == '1':
            filename=input("Enter the file-name to create=")
            create_file(filename)
        elif choice=='2':
            view_all_files()
        elif choice=='3':
            filename=input('Enter the name of file you want to delete =')
            delete_file(filename)
        elif choice=='4':
            filename=input('enter the file name to read =')
            read_file(filename)
        elif choice=='5':
            filename=input('enter file name to edit=')
            edit_file(filename)
        elif choice=='6':
            print('closing the app.....')
            break
        else:
            print('In-valid syntax')


if __name__=="__main__":
    main()

                

