import os
import shutil
import argparse
import glob
import torch
import random
import pandas as pd
import numpy as np
import time
import tqdm

from piano_transcription_inference.inference import PianoTranscription
from piano_transcription_inference import config
from piano_transcription_inference.utilities import load_audio



def audio2MIDI(song, output, device):
    st = time.time()
    
    # Load audio
    (audio, _) = load_audio(song, sr=config.sample_rate, mono=True)

    # Transcriptor
    transcriptor = PianoTranscription(device=device)

    # Transcribe and write out to MIDI file
    # Check if output directory exists
    if not os.path.exists(output):
        os.makedirs(output)
    name = song.split(".")[0].split("/")[-1]
    transcribed_dict = transcriptor.transcribe(audio, os.path.join(output, name+".mid"))
    ed = time.time()
    
    return os.path.join(output, name+".mid")
    

# Transcribe mp3 to MIDI
def transcribe(song_list, output, device):  # song_list, output, device
    count = 0
    for i in tqdm.tqdm(range(len(song_list))):
    #for audio_path in song_list:
        audio_path = song_list[i]
        #count += 1
        midi = audio2MIDI(audio_path, output, device)  # Transcribe, return midi path
        
        #if count % 100 == 0:
            #print("### Finished audio No.{}".format(count))

            
def main():
    # Arugments & parameters
    audio_path = glob.glob(args.audio_path)
    output_midi_path = args.output_midi_path
    device = 'cuda:4' if args.cuda and torch.cuda.is_available() else 'cpu'
    
    transcribe(audio_path, output_midi_path, device)
    
    
    
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--audio_path', type=str, required=False, default="./PEmoDataset/audios/seg/*.mp3")
    parser.add_argument('--output_midi_path', type=str, required=False, default="./midi/")
    parser.add_argument('--cuda', action='store_true', required=True)

    args = parser.parse_args()
    main()
