# Copyright (c) 2025 Nico-Gabriel Ruckendorfer
#
# This software is released under the MIT License.
# For more information, see the LICENSE file in the root directory of this project.


"""This module defines a class for a video streaming server."""

from cv2.typing import MatLike
from mjpeg_streamer import MjpegServer, Stream


class VideoStreamingServer:
	"""
	A class managing video streaming using the `mjpeg-streamer` library.
	It allows adding multiple independent streams, updating their frames, and starting/stopping the server.

	Attributes:
		server (MjpegServer): The underlying MJPEG server instance.
		streams (dict[str, Stream]): A dictionary mapping stream IDs to their corresponding stream objects.
	"""

	def __init__(self, host: str = "localhost", port: int = 8080) -> None:
		"""
		Initializes the `VideoStreamingServer` class.

		Args:
			host (str, optional): The hostname or IP address to bind the server to. Defaults to "localhost".
			port (int, optional): The port number to listen for connections on. Defaults to 8080.
		"""

		self._server: MjpegServer = MjpegServer(host, port)
		self._streams: dict[str, Stream] = {}

	def add_stream(self, stream_id: str) -> None:
		"""
		Creates a new stream with the given ID, adds it to the server, and stores it in the streams dictionary.

		Args:
			stream_id (str): A unique identifier for the new stream.

		Raises:
			ValueError: If a stream with the given ID already exists.
		"""

		if stream_id in self._streams:
			raise ValueError(f'Stream with ID "{stream_id}" already exists.')

		stream: Stream = Stream(stream_id)

		self._server.add_stream(stream)
		self._streams[stream_id] = stream

	def update_stream(self, stream_id: str, frame: MatLike) -> None:
		"""
		Updates the frame of the specified stream.

		Args:
			stream_id (str): The identifier of the stream to update.
			frame (MatLike): The new video frame to set for the stream.

		Raises:
			ValueError: If the stream with the given ID does not exist.
		"""

		if stream_id not in self._streams:
			raise ValueError(f'Stream with ID "{stream_id}" does not exist.')

		self._streams[stream_id].set_frame(frame)

	def start(self) -> None:
		"""
		Starts the MJPEG server (in a separate thread), making the video streams accessible to clients connecting to the
		server's host and port.
		"""

		self._server.start()

	def stop(self) -> None:
		"""Stops the MJPEG server, terminating all active streams and releasing its resources."""

		self._server.stop()
