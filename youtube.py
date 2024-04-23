from pytube import YouTube, Playlist
import ffmpeg
import os

class YT:
    def DownloadAudio(self, url):
        video = YouTube(url)
        title = self.ConvertTitle(video.title)
        stream = video.streams.get_by_itag("251")
        stream.download(output_path="./download")
        input = stream.get_file_path(output_path="download")
        self.ConvertAudio(input, title)
    def DownloadVideo(self, url):
        video = YouTube(url)
        stream = video.streams.get_highest_resolution()
        stream.download(output_path="./download")
    def DownloadPlaylist(self):
        pl = Playlist(self.url)
        for videos in pl.videos:
            self.DownloadAudio(videos.watch_url)
    def ConvertAudio(self,input, title):
        input_stream = ffmpeg.input(input)
        input_stream = ffmpeg.output(input_stream, f"./download/{title}.mp3", format="mp3")
        ffmpeg.overwrite_output(input_stream)
        ffmpeg.run(input_stream)
        os.remove(input)
    def ConvertTitle(self, title = ""):
        list_char = ['"', '<', '>', ':', '/', '|', '?', '*']
        aux = title
        for i in list_char:
            if i in aux:
                aux.replace(i, " ") 
        return aux