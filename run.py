#!/usr/bin/env python3.8
import bulleter

def read_file(this_file):
    a = bulleter.read_file(this_file)
    if a == None:
        print("Text processing Unsuccessful!")
    else:
        print("Successful! Check project folder for new.txt document")

def processor():
    bulleter.process_document()

def output():
    bulleter.give_output()

def main():
    print("Enter name of file")
    my_file = input()
    read_file(my_file)
    processor()
    output()

if __name__ == '__main__':
    main()
