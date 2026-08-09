# 1. I-install ang mga kinakailangang package
pip install yt-dlp whisperx pyannote.audio

# 2. I-run ang utos para sa extraction at diarization
whisperx "https://www.youtube.com/watch?v=YOUR_VIDEO_ID" --model base --diarize --hf_token YOUR_HUGGINGFACE_TOKEN --output_format md