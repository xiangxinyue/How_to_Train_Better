import pandas as pd
import numpy as np
import sqlite3
import matplotlib.pyplot as plt
import matplotlib
import folium
import csv

def mode_1(country):
        c = country
        csv_name = str(c)+".csv"
        df = pd.read_csv(csv_name)
        #print("lalala1")
        #print(df)        
    
        plot = df.plot.bar(x="Date")
        plt.plot()
        pic = str(c)+".png"
        plt.savefig(pic)#this line is to save the pic
        plt.show()

def mode_2(session):
        n = session
        csv_name = str(n)+".csv"
        df = pd.read_csv(csv_name)
        #print("lalala1")
        #print(df)
        array_data = np.array(df)#np.ndarray()
        list_data= array_data.tolist()#list
        #print("lalala2")
        #print(list_data)#the list is all the data
        
        m = folium.Map(location=[100, 0], zoom_start=1.5)
        #[11, 'Dubai', 'Spain', 'W', 19, 0, 40.463669, -3.7492199999999998, '100%', 19, 1.0]
        for i in range(len(list_data)):
                if list_data[i][3] == 'L':
                        folium.Circle(
                                location=[list_data[i][6],list_data[i][7]],
                                # location
                                popup= ("%s <br> %s  <br> %s:%s <br> %s" % (list_data[i][2],list_data[i][3],list_data[i][4],list_data[i][5],list_data[i][8])),
                                # popup text
                                radius= list_data[i][10] * 400000,
                                # size of radius in meter
                                color= 'crimson',
                                fill= True,
                                # whether to fill the map
                                fill_color= 'crimson'                        
                                # color to fill with
                                ).add_to(m)
                elif list_data[i][3] == 'W':
                        folium.Circle(
                                location=[list_data[i][6],list_data[i][7]],
                                # location
                                popup= ("%s <br> %s  <br> %s:%s <br> %s" % (list_data[i][2],list_data[i][3],list_data[i][4],list_data[i][5],list_data[i][8])),
                                # popup text
                                radius= list_data[i][10] * 400000,
                                # size of radius in meter
                                color= 'green',
                                fill= True,
                                # whether to fill the map
                                fill_color= 'green'                        
                                # color to fill with
                                ).add_to(m)                        
                                           
            # creating the marker with a popup and add it to map
            # saving the marker
        html = "gamesession"+str(n)+".html"
        m.save(html)          

def main():
        while(1):
                print("Welcome to GameDataVisual Program! :)")
                print("Mode1 is to compare the data against the same country")
                print("Mode2 is to copare the data in the same game session")
                inp = input("Please enter the mode you choose or E to Exit\n")
                if inp == '1':
                        print("There are 9 counties has more than 1 game with Canada")
                        print("Australia ; England ; Ireland ; Russia ; New Zealand") 
                        print("France ; Fiji ; Spain ; USA")
                        country = input("Please enter the country you want to visual \n")
                        mode_1(country)
                elif inp == '2':
                        print("It has 6 sessions:\n1: Dubai(2017 Nov-Dec) 2: Sydney(2018 Jan) 3: Commonwealth(2018 Apr)")
                        print("4: Langford(2018 May) 5: Paris(2018 June) 6: WorldCup(2018 July)")
                        session = int(input("Please enter the session you want to visual \n"))
                        mode_2(session)
                elif inp == 'E':
                        return
                else:
                        print("Please enter a valid mode :) \n")
            
        
if __name__ == '__main__':
        main()

