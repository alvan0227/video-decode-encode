#!/usr/bin/python
"""Store files as YouTube videos."""
from distutils.core import setup

setup_kwargs = {
    "name": "video-encode-decode",
    "version": "0.0.1",
    "url": "https://github.com/alvan0227/video-decode-encode",
    "packages": ["video_encode/"],
    "scripts": ["bin/youtube-drive"],
    "license": "Apache-2.0 license",
    "long_description": " ".join(__doc__.strip().splitlines()),
    "classifiers": [
        'Topic :: Internet :: WWW/HTTP',
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3',
    ],
    "entry_points": {
        'console_scripts': [
            'youtube-drive = youtube_drive.main:run'
        ],
    },
    "install_requires": [
        'numpy',
        'opencv-python',
        'pillow',
    ],
   
}

setup(**setup_kwargs)
