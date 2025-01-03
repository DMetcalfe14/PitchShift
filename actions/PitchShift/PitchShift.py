# Import StreamController modules
from src.backend.PluginManager.ActionBase import ActionBase
from src.backend.DeckManagement.DeckController import DeckController
from src.backend.DeckManagement.InputIdentifier import Input, InputEvent
from src.backend.PageManagement.Page import Page
from src.backend.PluginManager.PluginBase import PluginBase

import os

class PitchShift(ActionBase):
    def __init__(self, action_id: str, action_name: str,
                 deck_controller: DeckController, page: Page, coords: str, plugin_base: PluginBase):
        super().__init__(action_id=action_id, action_name=action_name,
            deck_controller=deck_controller, page=page, coords=coords, plugin_base=plugin_base)

        backend_path = os.path.join(self.plugin_base.PATH, "actions", "PitchShift", "backend", "backend.py") 
        self.launch_backend(backend_path = backend_path, open_in_terminal = True) 
        
    def on_ready(self):
        self.set_center_label(str(self.backend.get_count()))
    
    def event_callback(self, event: InputEvent, data: dict = None):
        if event == Input.Key.Events.SHORT_UP:
            self.backend.on_short_press()
            self.set_center_label(str(self.backend.get_count()))
        elif event == Input.Key.Events.HOLD_START:
            self.backend.on_long_press()
            self.set_center_label(str(self.backend.get_count()))