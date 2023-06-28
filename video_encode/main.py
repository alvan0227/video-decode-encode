import tempfile
import os
import sys
import uuid
import argparse
import codec



def cmd_encode(args):
    codec.encode(args.i, args.video_filename, args.video_fps)


def cmd_decode(args):
    codec.decode(args.i, args.filename)


def main(args):
    parser = argparse.ArgumentParser('video-encode')
    subparsers = parser.add_subparsers(title="commands")

    encode_parser = subparsers.add_parser('encode', aliases=['en'], help='encode a file to mp4 video')
    encode_parser.add_argument('-i',
                               action='store',
                               metavar="input_filename",
                               help='encode file <input_filename> to a video')
    encode_parser.add_argument('--video-fps',
                               action='store',
                               metavar="video_fps",
                               default=20,
                               type=int,
                               help='set video fps, default value is 20')
    encode_parser.add_argument('video_filename',
                               action='store',
                               help='save the video to this filename')
    encode_parser.set_defaults(handle=cmd_encode)

    decode_parser = subparsers.add_parser('decode', aliases=['de'], help='decode a video to a file')
    decode_parser.add_argument('-i',
                               action='store',
                               metavar="input_video_filename",
                               help='decode the video <input_video_filename> to a file')
    decode_parser.add_argument('filename',
                               action='store',
                               help='Save the output file to this filename')
    decode_parser.set_defaults(handle=cmd_decode)


    arguments = parser.parse_args(args)
    if not hasattr(arguments, 'handle'):
        parser.print_help()
        sys.exit(1)

    arguments.handle(arguments)


def run():
    main(sys.argv[1:])


if __name__ == '__main__':
    main(sys.argv[1:])
