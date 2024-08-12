import os

import ffmpeg

FORMAT_OPTIONS = {
    'mp3': {
        'codecs': ['libmp3lame'],
        'bitrates': ['128k', '192k', '256k', '320k'],
        'sample_rates': [44100, 48000],
        'channels': [1, 2],
        'volume': [0.5, 1.0, 1.5]
    },
    'aac': {
        'codecs': ['aac'],
        'bitrates': ['128k', '192k', '256k'],
        'sample_rates': [44100, 48000],
        'channels': [1, 2],
        'volume': [0.5, 1.0, 1.5]
    },
    'wav': {
        'codecs': ['pcm_s16le'],
        'bitrates': ['256k', '512k', '1024k'],
        'sample_rates': [44100, 48000, 96000],
        'channels': [1, 2],
        'volume': [0.5, 1.0, 1.5]
    },
    'flac': {
        'codecs': ['flac'],
        'bitrates': ['512k', '1024k', '2048k'],
        'sample_rates': [44100, 48000, 96000],
        'channels': [1, 2],
        'volume': [0.5, 1.0, 1.5]
    },
    'm4a': {
        'codecs': ['aac'],
        'bitrates': ['128k', '192k', '256k'],
        'sample_rates': [44100, 48000],
        'channels': [1, 2],
        'volume': [0.5, 1.0, 1.5]
    },
    'wma': {
        'codecs': ['wmav2'],
        'bitrates': ['128k', '192k', '256k'],
        'sample_rates': [44100, 48000],
        'channels': [1, 2],
        'volume': [0.5, 1.0, 1.5]
    }
}


def get_valid_option(options, key, default):
    return options.get(key) if options.get(key) in default else default[0]


def convert_audio(input_file: str, output_file: str, **kwargs) -> None:
    filename, extension = os.path.splitext(os.path.basename(input_file))
    format_key = extension[1:]
    format_opts = FORMAT_OPTIONS.get(format_key, {})

    codec = get_valid_option(kwargs, 'codec', format_opts.get('codecs', []))
    bit_rate = get_valid_option(kwargs, 'bit_rate', format_opts.get('bitrates', []))
    sample_rate = get_valid_option(kwargs, 'sample_rate', format_opts.get('sample_rates', []))
    channels = get_valid_option(kwargs, 'channels', format_opts.get('channels', []))
    volume = get_valid_option(kwargs, 'volume', format_opts.get('volume', []))

    print(codec, bit_rate, sample_rate, channels, volume)

    try:
        (
            ffmpeg
            .input(input_file)
            .output(output_file, acodec=codec, audio_bitrate=bit_rate, ar=sample_rate, ac=channels,
                    af=f'volume={volume}')
            .run(overwrite_output=True)
        )
        print(f"Conversion successful: {output_file}")
    except ffmpeg.Error as e:
        print(f"Error occurred: {e.stderr.decode('utf8')}")


# Example usage
audio_options = {
    "codec": "aac",
    "bit_rate": "192k",
    "sample_rate": 44100,
    "channels": 2,
    "volume": 1.0
}
convert_audio('input.mp3', 'output.aac', **audio_options)
