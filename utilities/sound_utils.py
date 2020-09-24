import speech_recognition as sr
from utilities.random_utils import FileUtils

# _P = "C:\\Users\\Art3m15\\IdeaProjects\\replicant_hw_no_bdd\\customer_conversations"
_P = "/home/iidwuurliik/Desktop/py_dev/replicant_hw/replicant_hw_pytest/customer_conversations"

class GenerateTranscript:

    @staticmethod
    def get_fake_replicant_transcript():
        mp3_file = FileUtils.pick_a_random_file_from_folder(_P)
        r = sr.Recognizer()
        with sr.AudioFile(mp3_file) as source:
            # listen for the data (load audio to memory)
            audio_data = r.record(source)
            # recognize (convert from speech to text)
            text = r.recognize_google(audio_data)
            return text
            # print(text)

    @staticmethod
    def get_true_transcript(s: str) -> str:
        return s


if __name__ == '__main__':
    GenerateTranscript.get_fake_replicant_transcript()
