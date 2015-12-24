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
        with open(os.path.join(self.recording, "info")) as infoFile:
            for line in infoFile:
                infoType = line[:1]
                content = line[2:].strip()
                if (infoType == 'T'):
                    self.title = content
                elif (infoType == 'D'):
                    self.description = content
    
    def filename(self):
        return format_filename(self.title)
        
    def __repr__(self):
        return self.filename()
        
def read_recordings(parent, folder):
    recordings = []
    if (folder == None):
        recording = parent
    else :
        recording = os.path.join(parent, folder)
    if (recording[-3:] == "rec"):
        recordings.append(RecordingInfo(recording))
    elif (os.path.isdir(recording)) :
        for subfolder in os.listdir(recording):
            recordings.extend(read_recordings(recording, subfolder))
    return recordings

print "converting VDR recordings from directory " + config.recordings
print(read_recordings(config.recordings, None))
