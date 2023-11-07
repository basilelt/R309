from functions. import
import sys, getopt

if __name__ == "__main__":
    try:
        opts, args = getopt.getopt(sys.argv[1:], ":", ["="])
        if not args:
            raise ValueError("main.py ")
    except getopt.GetoptError:
        print("main.py ")
        sys.exit(2)

        