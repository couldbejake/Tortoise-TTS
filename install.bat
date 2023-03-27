pip3 install -U scipy && pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118 && git clone https://github.com/jnordberg/tortoise-tts.git && cd tortoise-tts && pip3 install transformers && pip3 install -r requirements.txt && python setup.py install --user && PAUSE

pip uninstall numpy
pip install numpy==1.23.5
pip install --upgrade librosa