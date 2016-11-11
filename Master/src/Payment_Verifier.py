#!/usr/bin/env python

import os
import pandas

class HistoryChecker:
    """This class defines the HistoryChecker object.

    It finds the batch_payment file and iterates along its lines to create the
    initial state of transactions between users
    
    When defined, it creates a new TransactionsKeeper object with the list of
    users connections
    """
    def __init__(self):
        # Class initialization
       self 
        
    def CheckHistory(self):       
        # Creates the initial state of connections 
    
        CurrentDir = os.path.abspath(__file__ + "/../../")
        InputDir1 = CurrentDir+'/paymo_input/batch_payment.txt'
        InputDir2 = CurrentDir+'/paymo_input/batch_payment.csv'
        Keeper = TransactionsKeeper()

        try:
            CSVFrame = pandas.read_csv(InputDir1, header=None, names=range(2),
                                       skiprows=1,
                                       converters={'\r':'\s','':'\s'}, 
                                       usecols=[1,2],
                                       encoding='utf-8', lineterminator='\n', 
                                       quoting=3)

        except:
           CSVFrame = pandas.read_csv(InputDir2, header=None, names=range(2),
                                       skiprows=1,
                                       converters={'\r':'\s','':'\s'}, 
                                       usecols=[1,2],
                                       encoding='utf-8', lineterminator='\n', 
                                       quoting=3)
                                 
        IDList = CSVFrame.values.tolist()
        
        [ Keeper.NewTransaction([int(Row[0]),int(Row[1])]) for Row in IDList ]
        
        return Keeper

class TransactionsKeeper:
    """This class defines the TransactionsKeeper object.

    It creates, controls and modifies the degrees of transactions between users
    by iterating through the new set of payments in stream_payment 
    
    Attribuites:


    """

    def __init__(self):
        # Class initialization.

        self.IDList = {}
        CurrentDir = os.path.abspath(__file__ + "/../../")
        self.Output1 = open(CurrentDir + '/paymo_output/output1.txt', 'w')
        self.Output2 = open(CurrentDir + '/paymo_output/output2.txt', 'w')
        self.Output3 = open(CurrentDir + '/paymo_output/output3.txt', 'w')

    def NewTransaction(self,Row):
        # Creates the necesary connections for each new transaction
    
        if Row[0] not in self.IDList:
            self.IDList[Row[0]]=[]
                
        if Row[1] not in self.IDList:
            self.IDList[Row[1]]=[]
            
        #build edge
        if Row[1] not in self.IDList[Row[0]]:
            self.IDList[Row[0]].append(Row[1])
            
        #build edge
        if Row[0] not in self.IDList[Row[1]]:
            self.IDList[Row[1]].append(Row[0])

    def CheckNewTransactions(self):
        # This function is called to check new transactions in the 
        # stream_payment file.        

        CurrentDir = os.path.abspath(__file__ + "/../../")
        InputDir1 = CurrentDir+'/paymo_input/stream_payment.txt'
        InputDir2 = CurrentDir+'/paymo_input/stream_payment.csv'
        
        try:
            CSVFrame = pandas.read_csv(InputDir1, header=None, names=[0,1,2],
                                       skiprows=1,
                                       converters={'\r':'\s','':'\s'}, 
                                       usecols=[0,1,2],
                                       encoding='utf-8', lineterminator='\n', 
                                       quoting=3)

        except:
            CSVFrame = pandas.read_csv(InputDir2, header=None, names=[0,1,2],
                                       skiprows=1,
                                       converters={'\r':'\s','':'\s'}, 
                                       usecols=[0,1,2],
                                       encoding='utf-8', lineterminator='\n', 
                                       quoting=3)        
                               
        IDList = CSVFrame.values.tolist()
        
        [self.CheckFeatures([Row[0],int(Row[1]),int(Row[2])]) for Row in IDList]
        
    def CheckFeatures(self,Row):
        #
        Status1 = self.CheckFeature1([Row[1],Row[2]])
        Status2 = self.CheckFeature2([Row[1],Row[2]])
        Status3 = self.CheckFeature3([Row[1],Row[2]])
#        Status4 = self.CheckFeature4(Row[0])

        self.Output1.write(Status1 + '\n')  # Write to txt file 
        self.Output2.write(Status2 + '\n')  # Write to txt file 
        self.Output3.write(Status3 + '\n')  # Write to txt file          
        
        self.NewTransaction([Row[1],Row[2]])


    def CheckFeature1(self,Row):
        # Check if users meet feature 1

        verification = 'unverified'
        if Row[0] in self.IDList and Row[1] in self.IDList:  
            if Row[0] in self.IDList[Row[1]]:
                verification = 'trusted'
        return verification


    def CheckFeature2(self,Row):
        # Check if users meet feature 2
        
        verification = 'unverified'
        if Row[0] in self.IDList and Row[1] in self.IDList: 
            if Row[0] in self.IDList[Row[1]]:
                verification = 'trusted'
            else:        
                for SecDegID in self.IDList[Row[1]]:
                    if Row[0] in self.IDList[SecDegID]:
                        verification = 'trusted'
        return verification


    def CheckFeature3(self,Row):
        # Check if users meet feature 3
        
        verification = 'unverified'
        if Row[0] in self.IDList and Row[1] in self.IDList:
            if Row[0] in self.IDList[Row[1]]:
                verification = 'trusted'
            else:        
                for SecDegID in self.IDList[Row[1]]:
                    if Row[0] in self.IDList[SecDegID]:
                        verification = 'trusted'
                    else:
                        for ThirDegID in self.IDList[SecDegID]:
                            if Row[0] in self.IDList[ThirDegID]:
                                verification = 'trusted'
                            else:   
                                for FouDegID in self.IDList[ThirDegID]:
                                    if Row[0] in self.IDList[FouDegID]:
                                        verification = 'trusted'         
        return verification


#    def CheckFeature4(self,Date):
#    # Check if users meet feature 4
#    
#        TransTime = datetime.datetime.strptime(Date, '%Y-%m-%d %H:%M:%S')
        

def main(): 

    Checker = HistoryChecker()
    Keeper = Checker.CheckHistory()
    Keeper.CheckNewTransactions()
        
main()