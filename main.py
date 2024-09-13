from utils.Log import Log
from ActionExecutor import ActionExecutor
from processors.audio_commander.AudioCommanderProcessor import AudioCommanderProcessor


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

def process_text(text):
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ " + text)


audio_commander_processor = AudioCommanderProcessor.from_config_file('config.properties')
audio_commander_processor.start_recording(save_audio_files=True, function_with_recognized_text=process_text)
