import os
import eel
from backend_features.sound import playAssistantSound

eel.init('www')
os.system('start msedge.exe --app="http://localhost:8000/index.html"')

playAssistantSound()
eel.start('index.html',mode=None)