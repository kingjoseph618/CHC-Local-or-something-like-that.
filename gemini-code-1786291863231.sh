# 1. Install required packages
pip install yt-dlp whisperx pyannote.audio

# 2. Run YouTube extraction & diarization command directly
whisperx "https://www.youtube.com/watch?v=YOUR_VIDEO_ID" --model base --diarize --hf_token YOUR_HUGGINGFACE_TOKEN --output_format md