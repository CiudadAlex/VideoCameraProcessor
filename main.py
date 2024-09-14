from utils.Log import Log
from ActionExecutor import ActionExecutor
from commanders.MusicPlayCommander import MusicPlayCommander


if __name__ == '__main__2':
    Log.config()

    '''
    actions = ["ShowDetectionsProcessor", "VideoCameraClassImageSaverProcessor", "VideoCameraClassVideoSaverProcessor", 
               "ModelGenerator", "CameraMovementUI"]
    targets = ["LIGHTNINGS", "BIRDS",  "PEOPLE"]
    '''

    execute_action = "VideoCameraClassVideoSaverProcessor"
    target = "PEOPLE"
    ActionExecutor.execute(execute_action, target)


base_path = "C:/Alex/Musica"
music_play_commander = MusicPlayCommander(base_path)
music_play_commander.start()

# FIXME integrate MusicPlayCommander in ActionExecutor

