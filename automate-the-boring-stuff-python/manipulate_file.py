import os
import sys
import argparse
import shutil

parser = argparse.ArgumentParser(prog="File Manipulation", usage='%(prog)s [options]')
parser.add_argument('--rename', action='store_true', help="Rename a file")
parser.add_argument('--move', action='store_true', help='Move a file')
parser.add_argument('--source', required=True, help='Source file path')
parser.add_argument('--dest', required=True, help="Destination path")

args = parser.parse_args()

def main():
  if args.rename:
    if args.source and args.dest:
      os.rename(args.source, args.dest)
      print(f"Renamed {args.source} to {args.dest}")
    else:
      print("Error: --source and --dest are required for rename")
  elif args.move:
    if args.source and args.dest:
      shutil.move(args.source, args.dest)
      print(f'Moved {args.source} to {args.dest}')
    else:
      print('Error: --source and --dest are required for move')
  else:
    print("No action specified. Use --rename or --move")

if __name__ == "__main__":
  if '-h' not in sys.argv and '--help' not in sys.argv:
    main()