#!/usr/bin/python
import config, os, string

def format_filename(s):
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    filename = s.replace('/','-')
    filename = ''.join(c for c in filename if c in valid_chars)
    filename = filename.replace(' ','_')
    return filename

class RecordingInfo:

    def __init__(self, recording):
        self.recording = recording
        self.__readInfo()

    def __readInfo(self):
        with open(os.path.join(recording, "info")) as infoFile:
            for line in infoFile:
                infoType = line[:1]
                content = line[2:].strip()
                if (infoType == 'T'):
                    self.title = content
                elif (infoType == 'D'):
                    self.description = content
    
    def filename(self):
        return format_filename(self.title)

print "converting VDR recordings from directory " + config.recordings
for rec in os.listdir(config.recordings):
    if (rec.startswith("%") or not config.convertCut):
        for folder in os.listdir(os.path.join(config.recordings, rec)):
            recording = os.path.join(config.recordings, rec, folder)
            info = RecordingInfo(recording)
            print(info.recording)
            print(info.title)
            print(info.description)
            print(info.filename())
            
