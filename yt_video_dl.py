from pytube import YouTube as yt
import argparse as ap



def download(url, outPath):
  ytLink = yt(url)
  vidStream = ytLink.streams.get_highest_resolution()
  vidStream.download(outPath)

def main():
  parser = ap.ArgumentParser()
  parser.add_argument('url', help='URL of the YouTube video to download.')
  parser.add_argument('--output', '-o', help='Output path for the video file.')
  args = parser.parse_args()
  outPath = args.output or '.'
  download = (args.url, outPath)

if __name__ == '__main__':
  main()




