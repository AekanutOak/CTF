from sys import argv
from time import sleep

password = "nev3rg"

def print_help():
    print("Options:")
    print("-h, --help\tthis script require only 1 argument which is password")

if __name__ == "__main__":
    if len(argv) == 2:
        arg = argv[1]
        if arg == "-h" or arg == "--help":
            print_help()
        else:
            if(len(arg)) != len(password):
                print("Incorrect password")
                exit(0)
            else:
                sleep(0.25)
                for i in range(1,len(password)+1):
                    if arg[:i] == password[:i]:
                        sleep(0.075)
                        i+=1
                    else:
                        print("Incorrect password")
                        exit(0)

                print("The password is correct!")
                print("Here is your secret operation")
                print("flag{t1m1ng_c0v3rt_chann3l}")

    else:
        print("Invalid number of arguments. Use -h or --help for usage information.")
