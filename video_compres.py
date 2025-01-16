from util import input, path, ffmpeg, consol

def video_compress():
    is_video_path = False
    video_path = ''

    while not is_video_path:
        video_path = input.my_input('请输入视频地址: ')
        video_path = video_path[1:-1]

        if path.is_video(video_path):
            is_video_path = True
        else:
            consol.error('文件不是视频格式')
            
    path.check(video_path)
    ffmpeg.compres(video_path)

if __name__ == '__main__':
    video_compress()