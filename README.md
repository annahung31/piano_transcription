
### Authors
This scripts is edited by [Joann](https://github.com/joann8512).
It is modified from [GiantMIDI](https://github.com/bytedance/GiantMIDI-Piano)

# Transcription Guide
Instructions for using the transcription code

## Folder Structure
- transcription/
    - README.md  
    - midi/  
    - piano_transcription_inference/  
        - __init__.py  
        - config.py  
        - inference.py  
        - models.py  
        - piano_vad.py  
        - pytorch_utils.py  
        - utilities.py  
    - metadata.csv  
        - ID  
        - 4Q  
        - annotator
    - transcribe.py  
    
* The folder `midi` will be automatically created after running **transcribe.py**
    
## Usage
### Selecting GPU
If using GPU, go to line55 in transcribe.py to change GPU number.  
```ruby
device = 'cuda:4' if args.cuda and torch.cuda.is_available() else 'cpu'
```

### Start Transcribing
Run   
```
python3 transcribe.py
```

## TODO
1. Add **timestamps** to `metadata.csv` for the final version.
