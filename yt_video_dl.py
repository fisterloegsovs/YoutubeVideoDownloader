# Somehow only workd for python and not python3, one could also just use pytube <url> but this is more fun

from pytube import YouTube as yt
import argparse as ap
import os
from tqdm import tqdm
import sys

def progress_function(stream, chunk, bytes_remaining):
    current = ((stream.filesize - bytes_remaining)/stream.filesize)
    percent = ('{0}').format(int(current*100))
    progress = int(50*current)
    sys.stdout.write('\r')
    sys.stdout.write("[%-50s] %d%%" % ('='*progress, int(current*100)))
    sys.stdout.flush()

def download(url, outPath=None):
    if outPath is None:
        outPath = "C:/Users/Anders/Documents/Github/YoutubeVideoDownloader/downloadedVideos/"
    
    ytLink = yt(url, on_progress_callback=progress_function)
    vidStream = ytLink.streams.get_highest_resolution()
    vidStream.download(output_path=outPath)

def main():
  parser = ap.ArgumentParser()
  parser.add_argument('url', help='URL of the YouTube video to download.')
  parser.add_argument('--output', '-o', help='Output path for the video file.')
  args = parser.parse_args()

  if args.output is not None:
    outPath = args.output
    download(args.url, outPath)
  else:
    download(args.url)

if __name__ == '__main__':
  main()







