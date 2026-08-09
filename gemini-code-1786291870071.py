import subprocess
import sys

def process_youtube_video(video_url, hf_token):
    print(f"[*] Downloading and processing audio from: {video_url}")
    
    # Extract audio using yt-dlp and run WhisperX for transcription + speaker diarization
    cmd = [
        "whisperx",
        video_url,
        "--model", "base",
        "--diarize",
        "--hf_token", hf_token,
        "--output_format", "md",
        "--output_dir", "./transcripts"
    ]
    
    try:
        subprocess.run(cmd, check=True)
        print("[+] Transcription and Diarization complete! Check the './transcripts' folder for your .md file.")
    except Exception as e:
        print(f"[-] Error executing pipeline: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python get_youtube_diarization.py <YOUTUBE_URL> <HUGGINGFACE_TOKEN>")
    else:
        process_youtube_video(sys.argv[1], sys.argv[2])