import pandas as pd
import numpy as np 
import sqlite3
import matplotlib.pyplot as plt
import matplotlib
import folium
import csv

def main():
        while(1):
                print("\n\n")
                print("Welcome to the program how to train best\n")
                ID = input("Please enter your Player ID: ")
                print("Please enter your Stat as following: \n")
                stat1 = float(input("Enter your USG measurement(Yes is 1, No is 0) : "))
                stat2 = float(input("Enter your Pain(Yes is 1, No is 0) : "))
                stat3 = float(input("Enter your Sleep Hours : "))
                stat4 = float(input("Enter your Monitoring Score(According to your data) : "))
                B1L = 0.000
                B1H = 0.000
                B2L = 0.000
                B2H = 0.000
                B3L = 7.938
                B3H = 9.000
                B4L = 17.000
                B4H = 21.000
                P = 45 + stat1*(-28.6935) + stat2*(-24.9273) + stat3*2.9492 + stat4*1.1154
                print("Dear"+ID+", your Score Percentage is "+ str(P)+"%")
                if stat1 < B1L:
                        print("your USG is too low")                               
                elif stat1 > B1H:
                        print("your USG is too high") 
                else:
                        print("your USG is great")
                if stat2 < B2L:
                        print("your Pain is too low") 
                elif stat2 > B2H:
                        print("your Pain is too high") 
                else:
                        print("your Pain is great")
                if stat3 < B3L:
                        print("your Sleep Hours is too short, sleep more!")
                elif stat3 > B3H:
                        print("your Sleep Hours is too long, do not be lazy!")
                else:
                        print("your Sleep Hours is great") 
                if stat4 < B4L:
                        print("your Monitoring Score is too low")
                elif stat4 > B4H:
                        print("your Monitoring Score is too high")
                else:
                        print("your Monitoring Score is great")  
                
                print("In order to better train yourslef to prove your Score Percentage\nYou need to do following")
                if stat1 != 0:
                        print("1. You need to control USG level, train more")
                        if stat2 != 0:
                                print("2. Do not train so that bad to hurt yourself") 
                                if stat3 < B3L or stat3 > B3H:
                                        print("3. Sleep well") 
                                        if stat4 < B4L or stat4 > B4H:
                                                print("4. Keep good condition of monitoring")
                                        else:
                                                print("Good Job! Keep Traning!")
                                else:
                                        print("Good Job! Keep Traning!")
                        else: 
                                print("Good Job! Keep Traning!")
                                
                elif stat2 != 0:
                        print("1. Do not train so that bad to hurt yourself") 
                        if stat3 < B3L or stat3 > B3H:
                                print("2. Sleep well") 
                                if stat4 < B4L or stat4 > B4H:
                                        print("3. Keep good condition of monitoring")
                                else:
                                        print("Good Job! Keep Traning!")
                        else: 
                                print("Good Job! Keep Traning!") 
                                
                elif stat3 < B3L or stat3 > B3H:
                        print("1. Sleep well")
                        if stat4 < B4L or stat4 > B4H:
                                print("2. Keep good condition of monitoring")
                        else: 
                                print("Good Job! Keep Traning!")                          
                elif stat4 < B4L or stat4 > B4H:
                        print("1. Keep good condition of monitoring")
                else:
                        print("Good Job! Keep Traning!")
                                                      
        
if __name__ == '__main__':
        main()

