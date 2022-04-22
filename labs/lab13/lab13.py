"""
Name: Thomas Scola
algorithms.py
Problem: to form a program that reads a file and performs an algorithm to produce warning and alerts for certain trades
Certification of Authenticity:
I received help from the CSL lab with Brooke Duvall and used stack overflow for brief help with reading the files
"""
def trade_alert(file_name):
    with open("trades.txt", "r") as f:
        trades = f.readline()
        trade_list = trades.split()
        #print(trade_list)
        for i in range(len(trade_list)):
            trade_list[i] = int(trade_list[i])

        for integer in range(len(trade_list)):
            if trade_list[integer] > 830:
                print("Warning over 830 trades in one second")
                print(integer)
            elif trade_list[integer] == 500:
                print("ALERT! 500 trades in one second")
                print(integer)

    trades.close()
def main():
    trade_alert("trades.txt")