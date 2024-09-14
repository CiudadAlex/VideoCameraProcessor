from utils.Log import Log
from ActionExecutor import ActionExecutor


if __name__ == '__main__':
    Log.config()

    '''
    actions = ["ShowDetectionsProcessor", "VideoCameraClassImageSaverProcessor", "VideoCameraClassVideoSaverProcessor", 
               "ModelGenerator", "CameraMovementUI", "MusicPlayCommander"]
    targets = ["LIGHTNINGS", "BIRDS",  "PEOPLE"]
    '''

    execute_action = "MusicPlayCommander"
    target = "PEOPLE"
    ActionExecutor.execute(execute_action, target)

