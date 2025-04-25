#!/usr/bin/env python3


# Copyright (c) 2025 Nico-Gabriel Ruckendorfer
#
# This software is released under the MIT License.
# For more information, see the LICENSE file in the root directory of this project.


"""Main entry point for the video processing application."""

from video_processor import VideoProcessor


def main() -> None:
	"""Instantiates and runs the `VideoProcessor` class."""

	video_processor: VideoProcessor = VideoProcessor()
	video_processor.run()


if __name__ == "__main__":
	main()
