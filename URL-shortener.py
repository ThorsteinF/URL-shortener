import random
import os
import sys

alfabet = "ABCDEFGHIJLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
log = {}

def main():
    choice = input("1. Shorten URL\n2. Decode URL\n3. List of URLs\n>")
    if choice == "1":
        os.system("cls")
        create()
    elif choice == "2":
        os.system("cls")
        lookup()
    elif choice == "3":
      os.system("cls")
      urllist()
    else:
        os.system("cls")
        main()
        return
    
def create():
    url = input("URL: ")

    while True:
        short = "sho.rt/" + alfabet[random.randrange(0, len(alfabet))] + str(random.randrange(0, 9)) + alfabet[random.randrange(0, len(alfabet))] + str(random.randrange(0, 9)) + alfabet[random.randrange(0, len(alfabet))]
        if short in log:
            continue
        else:
            log[url] = short
            print("Shortened url for " + url + ": " + short)
            input("Press ENTER to return to the menu")
            os.system("cls")
            main()
            break
    
def lookup():
    short = input("Shortened url: ")
    for i, j in log.items():
        if short == j:
            print(j + ": " + i)
            input("Press ENTER to return to the menu")
            os.system("cls")
            main()
            break
    input("Could not find URL. Press ENTER to return to the menu")
    os.system("cls")
    main()

def urllist():
  if not log:
    input("There are no URLs! Press ENTER to return to the menu")
    os.system("cls")
    main()
  else:
    for i, j in log.items():
      print(i + ": " + j)
    input("Press ENTER to return to the menu")
    os.system("cls")
    main()

main()