#!/usr/bin/env python3
"""Dependencies: python 3.2; `convert`; `tesseract`"""
import subprocess
import argparse
import tempfile
import os
from pathlib import Path

parser = argparse.ArgumentParser(description='Parse text from a rect in a page of a pdf.')
parser.add_argument('--verbose',action='store_const',const=True,default=False,help='print information about attempted subcommands')
parser.add_argument('page', type=int, help='page of the pdf')
parser.add_argument('geometry', type=str, help='a ImageMagik-style geometry string: "<width>x<height>+x+y"')
parser.add_argument('fname', type=str, help='path of the pdf file to convert')
args = parser.parse_args()

p = Path(args.fname)

tmpfile = tempfile.NamedTemporaryFile(suffix='.jpg',delete=False)
tmpfilepath = tmpfile.name

cmd = ["convert", str(p) + "[" + str(args.page) + "]", "-crop", args.geometry, tmpfilepath]
if args.verbose:
    print("Processing file: {}".format(p))
    print("Image extraction command: {}".format(cmd))
subprocess.check_call(cmd, shell=False)

#tesseract dates.jpg - 2> /dev/null
cmd = ['tesseract',tmpfilepath,'-']
if args.verbose:
    print("OCR command: {}".format(cmd))
out = subprocess.check_output(cmd,stderr=subprocess.DEVNULL,shell=False)
outs = out.decode("utf-8").strip()
print(outs)
os.remove(tmpfilepath)
