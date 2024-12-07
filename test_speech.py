from TTS.api import TTS

def test_speech_generation():
    try:
        # Initialize TTS with the XTTS v2 model
        tts = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2")
        
        # Text to synthesize
        text = "Hello, this is a test of the text to speech system."
        
        # Generate speech
        print("Generating speech...")
        tts.tts_to_file(text=text, 
                        file_path="test_output.wav",
                        language="en")
        
        print("Speech generated successfully! Check test_output.wav")
        return True
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False

if __name__ == "__main__":
    test_speech_generation()