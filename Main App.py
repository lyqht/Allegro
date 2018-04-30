" Last Update: 5/4/2018 "

# Core stuf
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from firebase import firebase
from kivy.lang import Builder

# Child Widgets
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.clock import Clock

# Layouts
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton

# Graphics
from kivy.graphics.vertex_instructions import (Rectangle,
                                               Ellipse,
                                               Line)
# Matplot for generating graph
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random
import os

" VERY IMPORTANT : PLEASE DONT SPAM THE REFRESH BUTTON. APP WILL DIE."
" Python Code Starts here "
Builder.load_file('Main.kv')


class RootManager(ScreenManager):
    pass


class StartScreen(Screen):
    txt = "Check Status"
    pass

class DataScreen(Screen):

    def __init__(self, **kwargs):
        super(DataScreen, self).__init__(**kwargs)
        """
        In this particular implementation, these are the following
        required data
        """
        self.curr_data = []
        self.curr_time = ""
        self.db = self.get_database()
        self.data_store_counter = 0
        Clock.schedule_once(self.get_data,-1)
        Clock.schedule_once(self.get_data,0)
        Clock.schedule_once(self.get_data,2)
        trigger = Clock.create_trigger(self.simpleGraph, 5)
        trigger()
        
        Clock.schedule_interval(self.get_data, 60)
        Clock.schedule_interval(self.simpleGraph, 100)
        # getting default time and parameter variables
        self.check_mem = []
        self._time_mem = []
        self._temp_mem = []
        self._humi_mem = []
        self._airq_mem = []
        self._ligh_mem = []
        self._score_mem = []
        self._elapsed_time = 0
        # to see if there is data stored

    def get_database(self):
        url = "https://iot-dw-10-009.firebaseio.com"  # URL to Firebase database
        token = "2id286geOP4affeJQepYOWR7ZqJiWst09ZVXvHCO"  # unique token used for authentication
        db = firebase.FirebaseApplication(url, token)
        return db

    def access_database(self, db):
        root = "/"
        origin = root + "allegro_app/"
        data_names = ["humidity", "temperature", "air_quality",
                      "ambient_light", "time_mdy", "time_hms"]
        data = []
        for i in data_names:
            data.append(db.get(origin + i))
        if float(data[0]) < 100 and float(data[1]) > 10:
            return data
        else:
            return []

    def assess_data(self, data):
        if data == []:
            return None
        humi = float(data[0])
        temp = float(data[1])
        airq = int(data[2])
        ambl = int(data[3])
        humi_score = 100 - (humi - 50) * 2
        temp_score = (temp - 27) * 20
        airq_score = (airq - 100) // 2 + 50
        ambl_score = (ambl) // 3

        # Total score lower than it should be.
        total = (humi_score + temp_score + airq_score + ambl_score) 
        return [temp_score, humi_score, airq_score, ambl_score, total]

    def update_memory(self, time, new_scores):
        # limit size of memory
        if len(self.check_mem) == 30:
            self.check_mem.pop(0)
            self._time_mem.pop(0)
            self._temp_mem.pop(0)
            self._humi_mem.pop(0)
            self._airq_mem.pop(0)
            self._ligh_mem.pop(0)
            self._score_mem.pop(0)

        # add stuff to memory
        self.check_mem.append(1)
        self._time_mem.append(time)
        self._temp_mem.append(new_scores[0])
        self._humi_mem.append(new_scores[1])
        self._airq_mem.append(new_scores[2])
        self._ligh_mem.append(new_scores[3])
        self._score_mem.append(new_scores[4])
        self._elapsed_time += 1
        print("Updated Memory.")

    def get_data(self, dt):
        print("Getting Data")
        data = self.access_database(self.db)
        # print(data)
        if data != []:
            scores = self.assess_data(data)
            time = data[5]
            self.update_memory(time, scores)
            self.curr_data = scores
            self.curr_time = time

    ########### Graphing ################

    colors = {'Temperature': 'red', 'Humidity': 'blue', 'Air Quality': 'green', 'Light': 'black'}
    def comment(self):
        if self._temp_mem[-1] > 80:
            return "Something is getting hot in your laundry room. Be wary."
        if self._airq_mem[-1] > 80:
            return "Did you leave your detergent out? The air is getting bad"
        if np.average(self._score_mem) < 500:
            return "It's a good day to do laundry"
        elif self._temp_mem[-1] < 31 and self._humi_mem [-1]> 90:
            return "Seems to be raining."
        else:
            return "Probably not a good day to do laundry."
    
    def simpleGraph(self, dt):
        print("Refreshing. Syncing data and Generating Graph")
        self.get_data(0)
        x_axis = range(self._elapsed_time)
        plt.plot(x_axis, self._score_mem)
        plt.title("Brisk Score")
        plt.xlabel("Time")
        plt.gca().set_facecolor("#f7f7f7")
        
        self.ids['comment'].text = self.comment()
        file_counter = 1
        directory = 'Saved Graphs'
        if not os.path.exists(directory):
            os.makedirs(directory)

        filename = 'graph' + str(file_counter) + '.png'
        filepath = directory + '/' + filename
        while os.path.exists(filepath):
            filepath = directory + '/' + 'graph' + str(file_counter) + '.png'
            file_counter += 1

        plt.savefig(filepath)
        plt.clf()

        # Display latest graph image file
        self.ids['graph'].source = filepath


    # Filter helper functions
    filtervars = {}
    def get_aq(self):
        self.filtervars["Air Quality"] = self._airq_mem
    def get_temp(self):
        self.filtervars["Temperature"] = self._temp_mem
    def get_humidity(self):
        self.filtervars["Humidity"] = self._humi_mem
    def get_light(self):
        self.filtervars["Light"] = self._ligh_mem
    def remove_aq(self):
        if "Air Quality" in self.filtervars:
            self.filtervars.pop("Air Quality")
    def remove_temp (self):
        if "Temperature" in self.filtervars:
            self.filtervars.pop("Temperature")
    def remove_humidity(self):
        if "Humidity" in self.filtervars:
            self.filtervars.pop("Humidity")
    def remove_light(self):
        if "Light" in self.filtervars:
            self.filtervars.pop("Light")
            
    # Plotting filtered graphs
    def detailedGraph(self, timelist, ydict):
        nrows = len(ydict.keys())
        crow = 0

        for y in ydict.keys():
            crow += 1
            plt.subplot(nrows, 1, crow)
            plt.plot(timelist, ydict[y], color=self.colors[y], marker='o', linestyle='solid', linewidth=1, markersize=4)
            
            plt.title(y)
            plt.grid()
            plt.gca().set_facecolor("#f7f7f7")
        plt.xlabel("Time/ h")
        plt.tight_layout()

        # Counting the number of files in the folder and naming them accordingly
        file_counter = 1
        directory = 'Saved Graphs'
        if not os.path.exists(directory):
            os.makedirs(directory)

        filename = 'graph' + str(file_counter) + '.png'
        filepath = directory + '/' + filename
        while os.path.exists(filepath):
            filepath = directory + '/' + 'graph' + str(file_counter) + '.png'
            file_counter += 1

        plt.savefig(filepath)
        plt.clf()

        # Display latest graph image file
        self.ids['graph'].source = filepath
        
        # Quit app function
    def quit_app(*args):
        App.get_running_app().stop()
        Window.close()


class MainApp(App):
    def build(self):
        return RootManager()

    # to add function to delete existing graph pics upon app exit.


# run the app   
if __name__ == '__main__':
    MainApp().run()
