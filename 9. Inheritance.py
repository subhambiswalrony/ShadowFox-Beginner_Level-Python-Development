'''
1. Create inheritance using MobilePhone as base class and Apple & Samsung as child class
    1. The base class should have properties:
        1. ScreenType = Touch Screen
        2. NetworkType = 4G/5G
        3. DualSim = True or False
        4. FrontCamera = (5MP/8MP/12MP/16MP)
        5. rearCamera = (8MP/12MP/16MP/32MP/48MP)
        6. RAM = (2GB/3GB/4GB)
        7. Storage = (16GB/32GB/64GB)
2. Create basic mobile phone functionalities in the classes like: make_call, recieve_call, take_a_picture, etc.
3. Use super() constructor for calling parent class’s constructor
4. Make some objects of Apple class with different properties
5. Make some objects of Samsung class with different properties
'''

class MobilePhone:
    def __init__(self, screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage):
        self.screen_type = screen_type
        self.network_type = network_type
        self.dual_sim = dual_sim
        self.front_camera = front_camera
        self.rear_camera = rear_camera
        self.ram = ram
        self.storage = storage

    def make_call(self, number):
        print(f"Calling {number}...")

    def receive_call(self, caller_name):
        print(f"Call from {caller_name}")

    def take_a_picture(self):
        print("Taking a picture...")

class Apple(MobilePhone):
    def __init__(self, model, **kwargs):
        super().__init__(**kwargs)
        self.model = model

class Samsung(MobilePhone):
    def __init__(self, model, **kwargs):
        super().__init__(**kwargs)
        self.model = model

iphone12 = Apple(model="iPhone 12", screen_type="Touch Screen", network_type="5G",
                 dual_sim=False, front_camera="12MP", rear_camera="48MP", ram="4GB", storage="64GB")

galaxyS21 = Samsung(model="Galaxy S21", screen_type="Touch Screen", network_type="5G",
                     dual_sim=True, front_camera="16MP", rear_camera="32MP", ram="6GB", storage="128GB")

iphone12.make_call("+91-98611-75061")
galaxyS21.take_a_picture()
iphone12.receive_call("Subham Biswal")
