# AudioConverter
Convert audio files to other audio formats with custom options using ffmpeg.

## Example
```python
from audio_converter import convert_audio

def success_callback(msg: str) -> None:
    print(msg)


def failure_callback(msg: str) -> None:
    print(msg)


# Example usage
audio_options = {
    "codec": "libmp3lame",
    "bit_rate": "256k",
    "sample_rate": 48000,
    "channels": 2,
    "volume": 1
}
convert_audio("input.mp3", 'output.mp3', success_callback, failure_callback, **audio_options)
```

<h2 align="left">Requirements</h2>


```
pip install ffmpeg-python==0.2.0
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
