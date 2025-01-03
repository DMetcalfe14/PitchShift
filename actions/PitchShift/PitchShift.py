# Import StreamController modules
from src.backend.PluginManager.ActionBase import ActionBase
from src.backend.DeckManagement.DeckController import DeckController
frin src.backend.DeckManagement.InputIdentifier import Input, InputEvent
from src.backend.PageManagement.Page import Page
from src.backend.PluginManager.PluginBase import PluginBase

class PitchShift(ActionBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.count: int = 0
        
    def on_ready(self):
        self.set_center_label(str(self.count))
        
    # def on_key_down(self):
    #     self.count += 1
    #     self.set_center_label(str(self.count))

    def event_callback(self, event: InputEvent, data: dict = None):
        if event == Input.Key.Events.SHORT_UP:
            self.on_short_press()
        elif event == Input.Key.Events.HOLD_START:
            self.on_long_press()

    def on_long_press(self):
        self.count -= 1
        self.set_center_label(str(self.count))

    def on_short_press(self):
        self.count += 1
        self.set_center_label(str(self.count))
        