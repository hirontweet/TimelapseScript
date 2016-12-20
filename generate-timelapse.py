from moviepy.video.io.ImageSequenceClip import ImageSequenceClip
import sys

def createTimeLapse(dir, filename, fpsValue):
	# First argument has several options, in this case I used directory path of images
	clip = ImageSequenceClip(dir, fps = fpsValue)

	# Export a timelapse video
	clip.write_videofile(filename)


if __name__ == '__main__':
	# Get Command-Line arguments
	args = sys.argv

	if len(args) != 4:
		print("args length: " + str(len(args)))
		print("missing arguments\n1st: relative path\n2nd: Filename of Exported video(include .mp4 at the end\n3rd: fps")
	else:
		createTimeLapse(args[1], args[2], int(args[3]))

