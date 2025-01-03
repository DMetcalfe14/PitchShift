# Import StreamController modules
from src.backend.PluginManager.PluginBase import PluginBase
from src.backend.PluginManager.ActionHolder import ActionHolder

# Import actions
from .actions.PitchShift.PitchShift import PitchShift

class PluginTemplate(PluginBase):
    def __init__(self):
        super().__init__()

        ## Register actions
        self.pitch_shift_holder = ActionHolder(
            plugin_base = self,
            action_base = PitchShift,
            action_id = "dev_core447_PitchShift::PitchShift", # Change this to your own plugin id
            action_name = "Pitch Shift",
        )
        self.add_action_holder(self.pitch_shift_holder)

        # Register plugin
        self.register(
            plugin_name = "Pitch Shift",
            github_repo = "https://github.com/StreamController/PluginTemplate",
            plugin_version = "1.0.0",
            app_version = "1.1.1-alpha"
        )