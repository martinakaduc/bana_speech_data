import os
import sys
import subprocess

if __name__ == "__main__":
    dir = sys.argv[1]
    full_dir = os.path.join(dir, "audio_by_word")
    full_dir_mp3 = os.path.join(dir, "audio_by_word_mp3")
    list_files = os.listdir(full_dir)

    for word in list_files:
        lsf_dir = os.path.join(full_dir, word)
        lsf_dir_mp3 = os.path.join(full_dir_mp3, word)
        os.mkdir(lsf_dir_mp3)

        list_sound_files = os.listdir(lsf_dir)
        for sf in list_sound_files:
            subprocess.run(["ffmpeg", "-i", os.path.join(lsf_dir, sf), "-acodec", "mp3", "-ab", "128k", os.path.join(lsf_dir_mp3, sf).replace("wav", "mp3")])
