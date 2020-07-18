import argparse
import sys
import base_encoding


def main():
    # create parser
    parser = argparse.ArgumentParser()
    parser.add_argument('code', help='encode or decode text', choices=['encode', 'e', 'decode', 'd'])
    parser.add_argument('input', help='input value to be encoded / decoded')
    parser.add_argument('-s', '--string', dest='string', help='decode a string instead', action="store_true")
    parser.add_argument('-b', '--base', dest='base', help='specifying the encoding / decoding which format', default=64, type=int, choices=[64, 128, 256])
    # parse the arguments
    args = parser.parse_args()
    try:
        request = args.input if args.string else int(args.input)
    except Exception:
        sys.exit("Cannot convert that to integer!")
    encoder = base_encoding.StrEncoder() if args.string else base_encoding.IntEncoder()
    if args.code in ['encode', 'e']:
        if args.base == 64:
            print(encoder.encode_base64(request))
        elif args.base == 128:
            print(encoder.encode_base128(request))
        else:
            print(encoder.encode_base256(request))
    else:
        if args.base == 64:
            print(encoder.decode_base64(request))
        elif args.base == 128:
            print(encoder.decode_base128(request))
        else:
            print(encoder.decode_base256(request))


if __name__ == "__main__":
    main()
