import os
from typing import Callable

import ffmpeg

VOLUME_LIST: list[int] = list(range(0, 101))

FORMAT_OPTIONS = {
    'mp3': {
        'codecs': ['libmp3lame'],
        'bitrates': ['128k', '192k', '256k', '320k'],
        'sample_rates': [44100, 48000],
        'channels': [1, 2],
        'volume': VOLUME_LIST
    },
    'aac': {
        'codecs': ['aac'],
        'bitrates': ['128k', '192k', '256k'],
        'sample_rates': [44100, 48000],
        'channels': [1, 2],
        'volume': VOLUME_LIST
    },
    'wav': {
        'codecs': ['pcm_s16le'],
        'bitrates': ['256k', '512k', '1024k'],
        'sample_rates': [44100, 48000, 96000],
        'channels': [1, 2],
        'volume': VOLUME_LIST
    },
    'flac': {
        'codecs': ['flac'],
        'bitrates': ['512k', '1024k', '2048k'],
        'sample_rates': [44100, 48000, 96000],
        'channels': [1, 2],
        'volume': VOLUME_LIST
    },
    'm4a': {
        'codecs': ['aac'],
        'bitrates': ['128k', '192k', '256k'],
        'sample_rates': [44100, 48000],
        'channels': [1, 2],
        'volume': VOLUME_LIST
    },
    'wma': {
        'codecs': ['wmav2'],
        'bitrates': ['128k', '192k', '256k'],
        'sample_rates': [44100, 48000],
        'channels': [1, 2],
        'volume': VOLUME_LIST
    }
}


def get_valid_option(options, key, default):
    if key not in options:
        return default[1] if len(default) > 1 else default[0]
    return options[key] if options[key] in default else default[0]


def convert_audio(input_file: str, output_file: str, on_success: Callable, on_failure: Callable, **options) -> None:
    try:
        filename, extension = os.path.splitext(os.path.basename(output_file))
        format_key = extension[1:]
        format_opts = FORMAT_OPTIONS.get(format_key, {})

        codec = get_valid_option(options, 'codec', format_opts.get('codecs', []))
        bit_rate = get_valid_option(options, 'bit_rate', format_opts.get('bitrates', []))
        sample_rate = get_valid_option(options, 'sample_rate', format_opts.get('sample_rates', []))
        channels = get_valid_option(options, 'channels', format_opts.get('channels', []))
        volume = get_valid_option(options, 'volume', format_opts.get('volume', []))

        (
            ffmpeg
            .input(input_file)
            .output(output_file, acodec=codec, audio_bitrate=bit_rate, ar=sample_rate, ac=channels,
                    af=f'volume={volume}')
            .run(overwrite_output=True)
        )
        on_success(f"Conversion successful:\n{output_file}")
    except Exception as e:
        on_failure(f"Error occurred:\n{e}")
