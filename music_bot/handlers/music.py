from aiogram import types
from aiogram.dispatcher import Dispatcher
import os
import asyncio
import subprocess
from youtube_search_python import VideosSearch
import yt_dlp

async def join_vc(chat_id):
    # Join the voice chat
    await bot.send_message(chat_id, "Bot has joined the Voice Chat!")

async def play_song(chat_id, song_name):
    videos_search = VideosSearch(song_name, limit=1)
    video = videos_search.result()["result"][0]
    video_url = video["link"]
    
    ydl_opts = {
        'format': 'bestaudio',
        'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3'}],
        'outtmpl': 'downloads/%(id)s.%(ext)s'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url, download=True)
        audio_file = ydl.prepare_filename(info).replace(".webm", ".mp3")

    await play_in_voice_chat(chat_id, audio_file)

async def play_in_voice_chat(chat_id, audio_file):
    process = subprocess.Popen(['ffmpeg', '-re', '-i', audio_file, '-f', 's16le', '-ac', '2', '-ar', '48000', '-'],
                                stdout=subprocess.PIPE)
    while True:
        output = process.stdout.read(1024)
        if not output:
            break
    os.remove(audio_file)

def register_music_handlers(dp: Dispatcher):
    dp.register_message_handler(join_vc, commands="join")
    dp.register_message_handler(play_song, commands="play")
