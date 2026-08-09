import subprocess
import sys

def process_youtube_video(video_url, hf_token):
    print(f"[*] Ino-download at pinoproseso ang audio mula sa: {video_url}")
    
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
        print("[+] Tapos na ang Transcription at Diarization! Tingnan ang folder na './transcripts' para sa iyong .md file.")
    except Exception as e:
        print(f"[-] Nagkaroon ng problema: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Paano gamitin: python get_youtube_diarization.py <YOUTUBE_URL> <HUGGINGFACE_TOKEN>")
    else:
        process_youtube_video(sys.argv[1], sys.argv[2])