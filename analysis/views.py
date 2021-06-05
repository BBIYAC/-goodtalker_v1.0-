from django.shortcuts import render
import subprocess
from django.http import HttpResponse
import datetime
import os.path
from analysis.voice_ml import run_ml


def show_analysis(request):
    return render(request, 'show_anaylsis.html')

def loading(request):
    filename = 'voice'
    saved_file_path = convert_voice(filename)
    # print("saved_file_path: {}".format(saved_file_path))
    error_handle_code = saved_file_path.get('code')

    if error_handle_code == 999:
        text = saved_file_path.get('message')
        data = [0, 0, 0, 0]
        return render(request, 'show_anaylsis.html', {'text': text,})
    else:
        # saved_file_path = "C:\\Users\\iykim\\Downloads\\voice.wav"
        file_path = saved_file_path.get('message')
        result = get_file(file_path)

        # print("file result: {}".format(result))
        error_handle_code = result.get('code')

        if error_handle_code == 999:
            text = result.get('message')
            data = [0, 0, 0, 0]

        elif error_handle_code == 200:
            result = result.get('message')
            # print(result)
            text = result.get('text')
            data = result.get('data')
            return render(request, 'show_anaylsis.html', {'text': text, "data" : data})


# convert oga to wav
def convert_voice(filename):
    #TODO when save voice file, user can write filename and goodtalker get filename to use convert wav name
    src_f = "C:\\Users\\iykim\\Downloads\\{}.oga".format(filename)
    dst_f = "C:\\Users\\iykim\\Downloads\\{}.wav".format(filename)

    # print("src_f: {}".format(src_f))

    # print("os.path.isfile(dst_f): {}".format(os.path.isfile(dst_f)))
    if os.path.isfile(dst_f) ==True:
        res = {"code": 999, "message": "DST FILE EXISIT"}
        return res

    elif os.path.isfile(src_f) == False:
        res = {"code": 999, "message": "NOT VOICE FILE"}
        return res

    else:
        subprocess.run(['ffmpeg', '-i', src_f, dst_f])
        msg = {"code": 200, "message": str(dst_f)}
        return msg

# get voice.wav file
def get_file(file_path):
    if os.path.isfile(file_path) == False:
        res = {"code": 999, "message": "NOT WAV FILE"}
        return res

    else:
        result = run_ml(file_path)
        res = {"code": 200, "message": result}
        return res
