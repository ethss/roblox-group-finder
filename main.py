import multiprocessing 
from src.threading import *

if __name__ == "__main__":
    multiprocessing.freeze_support()
    main = RoSpeed()
    main.main()
