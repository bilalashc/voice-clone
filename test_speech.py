import os
from TTS.api import TTS

def clone_voice_for_presentation(source_audio_path, output_dir, sentences):
    """
    Clone a voice from source audio to speak sentences in a supported language.
    
    Args:
        source_audio_path (str): Path to the WAV source audio file
        output_dir (str): Directory to save output files
        sentences (list): List of sentences to synthesize
    """
    try:
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Initialize TTS with multilingual model
        print("Initializing TTS model...")
        tts = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2")
        
        # Process each sentence
        for idx, sentence in enumerate(sentences, 1):
            output_path = os.path.join(output_dir, f'sentence_{idx:02d}.wav')
            
            print(f"\nProcessing sentence {idx}/{len(sentences)}:")
            print(f"Text: {sentence}")
            
            # Generate speech with cloned voice
            tts.tts_to_file(
                text=sentence,
                speaker_wav=source_audio_path,
                language="en",  # Using English as the base language
                file_path=output_path
            )
            
            print(f"Generated: {output_path}")
        
        print("\nVoice cloning completed successfully!")
        
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")
        raise

# File paths
SOURCE_AUDIO = "/Users/bilal/Desktop/engineering/projects/voice-clone/sample_dad_audio.wav"
OUTPUT_DIR = "/Users/bilal/Desktop/engineering/projects/voice-clone/output_audio"

# Example sentences in English or phonetic approximation
presentation_sentences = [
    "The quick brown fox jumped over the lazy. I want you to say it again. The quick brown fox jumped over the lazy dog"
]

if __name__ == "__main__":
    # Run the voice cloning
    clone_voice_for_presentation(
        source_audio_path=SOURCE_AUDIO,
        output_dir=OUTPUT_DIR,
        sentences=presentation_sentences
    )