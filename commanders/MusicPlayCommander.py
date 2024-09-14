from processors.audio_commander.AudioCommanderProcessor import AudioCommanderProcessor
from utils.FileUtils import FileUtils
from utils.MatchUtils import MatchUtils
import subprocess


class MusicPlayCommander:

    def __init__(self, root_dir):
        self.map_file_name_path = FileUtils.get_map_file_name_2_path(root_dir, MusicPlayCommander.preprocess_name, MusicPlayCommander.preprocess_path)

    @staticmethod
    def preprocess_name(name):
        return name.lower().replace(".mp3", "").replace(".wav", "").replace("_", " ").replace("-", " ")

    @staticmethod
    def preprocess_path(path):
        return path.replace("/", "\\")

    def process_text(self, text):

        most_similar_key = MatchUtils.get_most_matching_text_item(text.lower(), self.map_file_name_path.keys())
        path_music_file = self.map_file_name_path[most_similar_key]

        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> " + path_music_file)
        file1 = subprocess.run(["C:/Program Files (x86)/VideoLAN/VLC/vlc.exe", "--started-from-file", path_music_file])

    def start(self):
        audio_commander_processor = AudioCommanderProcessor.from_config_file('config.properties')
        audio_commander_processor.start_recording(save_audio_files=False, function_with_recognized_text=self.process_text)

