# Demucs-Tutorial
Demucs使用教程
## Usage \& Installation
### Command Usage
If you want to use command to separate tracks, you can install with
```bash
python3 -m pip install -U demucs
```
And the you can run using command from any folder
```bash
demucs zjl.WAV
```
If you only want to separate vocals out of an audio, use `--two-stems=vocals`
```bash
demucs --two-stems=vocals zjl.WAV
```
### Python Api Usage
If you want to use demucs from python api, you can install with
```bash
pip install git+https://github.com/CarlGao4/demucs#egg=demucs
```
And the demo for separate vocal and background using python api is in **api.py**

