# Import StreamController modules
from src.backend.PluginManager.ActionBase import ActionBase
from src.backend.DeckManagement.DeckController import DeckController
from src.backend.PageManagement.Page import Page
from src.backend.PluginManager.PluginBase import PluginBase

class PitchShift(ActionBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.count: int = 0
        
    def on_ready(self):
        self.set_center_label(str(self.count))
        
    def on_key_down(self):
        self.count += 1
        self.set_center_label(str(self.count))

    def on_long_press(self):
        self.count -= 1
        self.set_center_label(str(self.count))