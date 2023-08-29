
import torch
import torchaudio
import torch.nn as nn
import torch.nn.functional as F


from tortoise.api import TextToSpeech
from tortoise.utils.audio import load_audio, load_voice, load_voices

tts = TextToSpeech()

import os

# This is the text that will be spoken.
text = "Let's strive to make the world a better place, one code block at a time."

# Pick a "preset mode" to determine quality. Options: {"ultra_fast", "fast" (default), "standard", "high_quality"}. See docs in api.py
preset = "high_quality"

# upload at least 2 audio clips. They must be a WAV file, 6-10 seconds long.
CUSTOM_VOICE_NAME = "custom"

custom_voice_folder = f"tortoise/voices/{CUSTOM_VOICE_NAME}"
#os.makedirs(custom_voice_folder)
#for i, file_data in enumerate(files.upload().values()):
#  with open(os.path.join(custom_voice_folder, f'{i}.wav'), 'wb') as f:
#    f.write(file_data)

# Generate speech
voice_samples, conditioning_latents = load_voice(CUSTOM_VOICE_NAME)
gen = tts.tts_with_preset(text, voice_samples=voice_samples, conditioning_latents=conditioning_latents, 
                          preset=preset)
torchaudio.save(f'generated-{CUSTOM_VOICE_NAME}.wav', gen.squeeze(0).cpu(), 24000)
print(f'generated-{CUSTOM_VOICE_NAME}.wav')