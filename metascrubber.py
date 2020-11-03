#!/usr/bin/python3
import os
import time

directory = "x"


def intro():
    os.system("clear")
    print("Welcome to MetaScrubber, a sort of addon for mat2!")
    time.sleep(1)
    print("INSTRUCTIONS: THIS ADDON ONLY WORKS ON FILES THAT ARE COMPATIBLE WITH 'MAT2'. PLEASE REFER TO"
          "DOCUMENTATION FOR 'MAT2' FOR FURTHER GUIDANCE ON SUPPORTED FILE TYPES!")
    time.sleep(5)
    os.system("clear")


def setup():
    global directory
    directory = input("Please specify directory of files to be scrubbed: ")
    time.sleep(2.5)
    os.system("clear")
    for i in range(3):
        time.sleep(2)
        print("INITIALIZING METASCRUBBER")
        time.sleep(2)
        os.system("clear")


def run():
    global directory
    for filename in os.listdir(directory):
        path = (directory, filename)
        path2 = "/".join(path)
        print("ANALYZING " + path2)
        os.system("mat2 -s " + path2)
        time.sleep(1)
        print("SCRUBBING " + path2)
        os.system("mat2 --inplace " + path2)
        time.sleep(1)
        print("RE-ANALYZING " + path2)
        os.system("mat2 -s " + path2)
        time.sleep(1)
    print("Metadata has been scrubbed for all files in " + directory)
    time.sleep(2)
    os.system("clear")
    print("Shutting down MetaScrubber in 10 seconds")
    time.sleep(10)
    os.system("clear")

intro()
setup()
run()
