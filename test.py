# coding=utf8

import sys
import table2excel

def run_test():
    table = [["a", "b", "c"], [1, 2, 3], [4, 5, 6]]
    excel = table2excel.dumpExcel('test', table)
    sys.stdout.write(excel)
    sys.stdout.flush()
    

if __name__ == "__main__":
    run_test()
