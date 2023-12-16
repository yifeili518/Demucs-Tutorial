import demucs.api

# Initialize with default parameters:
separator = demucs.api.Separator()

# Use another model and segment:
separator = demucs.api.Separator(model="mdx_extra", segment=12)

# You can also use other parameters defined

# Separating an audio file
origin, separated = separator.separate_audio_file("zjl.WAV")

# Separating a loaded audio
# origin, separated = separator.separate_tensor(audio)

# If you encounter an error like CUDA out of memory, you can use this to change parameters like `segment`:
# separator.update_parameter(segment=smaller_segment)

# Remember to create the destination folder before calling `save_audio`
# Or you are likely to recieve `FileNotFoundError`
# print(separated)
vocals = separated["vocals"]
background = origin - vocals

# for file, sources in separated:
#     for stem, source in sources.items():
#         demucs.api.save_audio(source, f"{stem}_{file}", samplerate=separator.samplerate)

file = 'zjl.WAV'
demucs.api.save_audio(vocals, f"vocals_{file}", samplerate=separator.samplerate)
demucs.api.save_audio(background, f"background_{file}", samplerate=separator.samplerate)