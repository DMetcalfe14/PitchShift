from streamcontroller_plugin_tools import BackendBase 

class Backend(BackendBase):
    def __init__(self):
        super().__init__()
        
        self.client = udp_client.SimpleUDPClient("127.0.0.1", 22752)
        self.count: int = 0

    def get_count(self) -> int:
        return self.count

    def on_long_press(self):
        self.count -= 1
        self.send_message()

    def on_short_press(self):
        self.count += 1
        self.send_message()

    def send_message(self):
        self.client.send_message("/Carla/0/set_parameter_value", [2, float(self.count)])

backend = Backend()