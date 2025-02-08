import sys
import whisper

def transcribe_video(video_path):
    model = whisper.load_model("base")  # Load Whisper model (change to "small", "medium", or "large" for better accuracy)
    result = model.transcribe(video_path)
    
    transcript = result["text"]
    return transcript

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python transcribe_video.py <video_file>")
        sys.exit(1)

    video_file = sys.argv[1]
    transcript = transcribe_video(video_file)

    output_file = "transcript.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(transcript)

    print(f"Transcript saved to {output_file}")