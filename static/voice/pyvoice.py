import subprocess

# convert oga to wav
def convert_voice(file_path):
    src_f = file_path
    dst_f = "test.wav"
    # src_f의 이름을 parsing하여 name + '.wav' 로 설정해도되고
    # file_path도 base_dir 로 설정해서 해도되고 왜냐하면 저장할곳을 모르기때문에


    proces = subprocess.run(['ffmpeg', '-i', src_f, dst_f])

convert_voice("test.oga")