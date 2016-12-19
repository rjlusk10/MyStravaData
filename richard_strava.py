#!/usr/bin/python

class Ride:
    def __init__(self):
        self.ride_id = 0
    def load_from_json_data(self, data):
        self.ride_id = data['id']
    def dummy(self):
        return "asdf"

class Rider:
    """example class for every bike rider """
    def __init__(self):
        self.name = ""
        self.rides = []
    
    def load_from_json_data(self,data):
        
        for d in data:
            r=Ride()
            r.load_from_json_data(d)
            self.rides.append(r)
        
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
