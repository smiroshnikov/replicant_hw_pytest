import pyttsx3


class VoiceGenerator:
    def __init__(self):
        pass

    @staticmethod
    def generate_fake_voice(what_to_say: str, filename: str, voice=2, rate=190):
        """
        Generates a synth voice
        :param rate: int  - affects tonality
        :param filename: - output mp3 file name
        :param what_to_say: string to be said
        :param voice:0 - russian accent , 1 -  female , 2 - male
        :return: None
        """
        engine = pyttsx3.init()
        engine.setProperty('rate', rate)
        engine.setProperty('volume', 1)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[voice].id)
        engine.say(what_to_say)
        engine.save_to_file(what_to_say, filename=filename)
        engine.runAndWait()


if __name__ == '__main__':
    # test
    VoiceGenerator.generate_fake_voice("Yes this is him , I cannot speak right now , call me back in 15 minutes ",
                                       filename="1.mp3")
