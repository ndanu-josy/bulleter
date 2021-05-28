my_file = "test.txt"
write_file = "new.txt"

new_data = []

def read_file(my_file):
    '''
    Function that reads a text file and returns the data  from the text file
    Test to confirm that an exception is raised when a wrong file is inputted
    Raises:
        FileNotFoundError: if it cannot file file
    '''
    try:
        with open (my_file,"r") as bullet:
            data = bullet.readlines()
          
            return data
    except FileNotFoundError:
        print("The text file was not found")
        return None



def process_document():
    for i in read_file(my_file):
        cap_lines = i.capitalize()
        new_sentence = ("*"+cap_lines[0:])
        new_data.append(new_sentence)
    
    return new_data

def give_output():
    with open(write_file,"w") as writer:
        writer.writelines(process_document())
      


def main():
    print("Enter name of file")
    my_file = input()
    read_file(my_file)
    process_document()
    give_output()

main()