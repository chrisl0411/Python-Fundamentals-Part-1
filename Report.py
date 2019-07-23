#  File: Report.py
#  Description: Prints formatted data report.
#  Student's Name: Christopher Lee
#  Student's UT EID: cl37976
#  Identifier: grizzlee19
#  Course Name: CS 303E 
#  Unique Number: 51200
#
#  Date Created: 10/10/18
#  Date Last Modified:

def main():
    # input data
    companyName = "Lone Star Corporation"
    date = "October 1, 2018"
    cash = 7505.54
    acctsRec = 502.21
    supplies = 313.89
    land = 6456.23
    buildings = 81598.00
    machAndEquip = 8329.99
    patents = 2000.00
    acctsPay = 93569.23
    stock = 88100.00

    #sum of total assets and liabilites/stockholders equity
    totalAssets = cash+acctsRec+supplies+land+buildings+machAndEquip+patents
    totalEquity = acctsPay+stock

    #print formatted data statement
    print("")
    print("lone star corporation".upper().center(80))
    print("Balance Sheet".center(80))
    print("October 1, 2018".center(80))
    print("")
    print(format("Liabilites and",">57s"))
    print(format("Assets","<6s"),format("Stockholders' Equity",">59s"))
    print("--------------------------------------------------------------------------------")
    print(format("   Cash","<31s"),format(cash,"8.2f"),format("Liabilities:",">14s"))
    print(format("   Accounts Receivable","<31s"),format(acctsRec,"8.2f"),format("Accounts Payable",">21s"),format(acctsPay,">17.2f"))
    print(format("   Supplies","<31s"),format(supplies,"8.2f"))
    print(format("   Land","<31s"),format(land,"8.2f"))
    print(format("   Buildings","<31s"),format(buildings,"8.2f"),format("Stockholders' Equity:",">26s"))
    print(format("   Machines and Equipment","31s"),format(machAndEquip,"8.2f"),format("Capital Stock",">21s"),format(stock,"17.2f"))
    print(format("   Patents","31s"),format(patents,"8.2f"))
    print("")
    print(format("Total Assets","<30s"),format(totalAssets,"9.2f"),format("Total Liabilites and",">22s"))
    print(format("Stockholders' Equity",">66s"),format(totalEquity,"13.2f"))
    print("")
    
main()
