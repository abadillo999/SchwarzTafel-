import sys
from Controller import BlackboardController

def main():
        controller = BlackboardController()
        controller.controll()

if __name__== "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(4, "EXIT: Keyboard Interrupt.")
        sys.exit(1)


