from music21 import *
us = environment.UserSettings()
us['musicxmlPath'] = 'D:/bin/MuseScore3.exe'
s = corpus.parse('bach/bwv65.2.xml')
s.analyze('key')
s.show()