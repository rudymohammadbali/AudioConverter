# Audio-Tool
Convert audio files to other audio formats with custom options using ffmpeg.

## Examlpe
```python
from audio_tool import audio_converter

input_video = "C:\\Users\\usr\\Downloads\\input.mp3"
output_video = "C:\\Users\\usr\\Downloads"
output_format = "mp3"
audio_options = {"audio_codec": "libmp3lame", "bitrate": 192, "channel": "stereo", "sample_rate": "48000", "volume": 0}

# Usage
audio_converter(input_video, output_video, output_format, audio_options)
```

Make sure you have installed ffmpeg on your system! 
https://www.ffmpeg.org/download.html


###

<h2 align="left">Support</h2>

###

<p align="left">If you'd like to support my ongoing efforts in sharing fantastic open-source projects, you can contribute by making a donation via PayPal.</p>

###

<div align="center">
  <a href="https://www.paypal.com/paypalme/iamironman0" target="_blank">
    <img src="https://img.shields.io/static/v1?message=PayPal&logo=paypal&label=&color=00457C&logoColor=white&labelColor=&style=flat" height="40" alt="paypal logo"  />
  </a>
</div>

###
