from TTS.api import TTS
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=False)

# generate speech by cloning a voice using default settings
tts.tts_to_file(text="It took me quite a long time to develop a voice, and now that I have it I'm not going to be silent.",
                file_path="output.wav",
                # speaker_wav="/path/to/target/speaker.wav",
                language="en")

# from TTS.api import TTS

# # Initialize the TTS object with a model (example model name)
# tts = TTS(model_name="tts_models/en/ljspeech/glow-tts", progress_bar=False, gpu=False)

# # Generate speech and save to a file
# tts.tts_to_file(text="Hello world, this is a test.", file_path="output.wav")
