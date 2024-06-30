import os
import subprocess
from pathlib import Path


class UnsupportedAudioFormatError(Exception):
    def __init__(self, format_name: str):
        super().__init__(f"Unsupported audio format: {format_name}")


def path_exists(path: str) -> bool:
    return os.path.exists(path)


def is_file(path: str) -> bool:
    return os.path.isfile(path)


def extract_options(options: dict) -> dict:
    """
        Extracts valid audio conversion options from the given dictionary.

        Args:
            options (dict): A dictionary containing various conversion options.

        Returns:
            dict: A filtered dictionary containing valid options for audio conversion.

        Example:
            options = {
                "audio_codec": "aac",
                "bitrate": 192,
                "sample_rates": "48000",
                "channel": "stereo",
            }
            valid_options = extract_options(options)
            # valid_options will contain only the valid options based on predefined lists.
        """
    valid_options = {}

    audio_codec_list = ["copy", "aac", "ac3", "flac", "libmp3lame", "libopus"]
    bitrate = range(128, 320)
    channel = {"stereo": 2, "mono": 1}
    sample_rates = ["8000", "11025", "16000", "22050", "32000", "44100", "48000", "88200", "96000"]
    volume = range(-50, 100)

    for key, value in options.items():
        # Audio options
        if key == "audio_codec" and value in audio_codec_list:
            valid_options[key] = value
        elif key == "bitrate" and value in bitrate:
            valid_options[key] = f"{value}k"
        elif key == "channel" and value in channel:
            valid_options[key] = str(channel[value])
        elif key == "sample_rates" and value in sample_rates:
            valid_options[key] = value
        elif key == "volume" and value in volume:
            valid_options[key] = str(value)

    return valid_options


def audio_converter(input_path: str, output_path: str, target_format: str, options: dict) -> bool:
    """
        Converts an audio file from one format to another using FFmpeg.

        Args:
            input_path (str): Path to the input audio file.
            output_path (str): Path to the output folder where the converted audio will be saved.
            target_format (str): Target audio format (e.g., "mp3", "wav", "flac").
            options (dict): Dictionary containing audio conversion options.

        Raises:
            FileExistsError: If the input file does not exist.
            NotADirectoryError: If the output folder does not exist.
            UnsupportedVideoFormatError: If the target format is not supported.

        Returns:
            bool: True if conversion successful otherwise False.

        Example:
            options = {
                "audio_codec": "aac",
                "bitrate": 192,
                "sample_rates": "48000",
                "channel": "stereo",
            }
            audio_converter("input.wav", "output_folder", "mp3", options)
        """
    if not is_file(input_path):
        raise FileExistsError(f"File {input_path} does not exists.")

    if not path_exists(output_path):
        raise NotADirectoryError(f"Output folder {output_path} does not exists.")

    target_format = target_format.lower().strip()

    audio_formats = [
        "aac",
        "flac",
        "m4a",
        "mp3",
        "wav",
        "wma"
    ]

    if target_format.lower() not in audio_formats:
        raise UnsupportedAudioFormatError(target_format)

    filename, extension = os.path.splitext(os.path.basename(input_path))
    output_name = str(Path(output_path) / f"{filename}_converted.{target_format}")

    get_options = extract_options(options)

    ffmpeg_command = ["ffmpeg", "-i", input_path]

    for key, value in get_options.items():
        if key == "audio_codec":
            if target_format == "flac":
                ffmpeg_command.extend(["-c:a", "flac"])
            elif target_format == "wav":
                ffmpeg_command.extend(["-c:a", "libopus"])
            elif target_format == "mp3":
                ffmpeg_command.extend(["-c:a", "libmp3lame"])
            else:
                ffmpeg_command.extend(["-c:a", value])
        elif key == "bitrate":
            ffmpeg_command.extend(["-b:a", value])
        elif key == "channel":
            ffmpeg_command.extend(["-ac", value])
        elif key == "sample_rates":
            ffmpeg_command.extend(["-ar", value])
        elif key == "volume":
            ffmpeg_command.extend(["-af", f"volume={value}dB"])

    ffmpeg_command.append(output_name)

    try:
        subprocess.run(ffmpeg_command)
        return True
    except Exception as e:
        print(f"Error converting {input_path}: {e}")
        return False
