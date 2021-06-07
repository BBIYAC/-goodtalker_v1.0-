'''
    run model code in here
    1. get file url -> file_url
    2. run code
    3. return data
    4. text is str, data is list
'''
import os
import speech_recognition as sr
from speech_recognition import UnknownValueError, Recognizer
from tensorflow.keras.preprocessing.text import Tokenizer


# print text script
def Audio_file_Read(filename):
    universal_dict={}
    cnt = {}
    token = Tokenizer()
    recog = Recognizer()
    try:
        audioFile = sr.AudioFile(filename)
        with audioFile as source:
            audio = recog.record(source)
            recognized = recog.recognize_google(audio,language="ko-KR")
            text = recognized
            return text
    except UnknownValueError:
            text = "당신이 말한 문장이 없습니다."
            return text


def run_ml(file_path):
    # input code here

    # example data
    # you sould follow under data type
    result={}
    text = Audio_file_Read(file_path)
    data = [1,2,3]

    #--------
    result['text'] = text
    result['data'] = data
    # print("result: {}".format(result))
    os.remove(file_path)
    return result