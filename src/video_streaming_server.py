# Copyright (c) 2025 Nico-Gabriel Ruckendorfer
#
# This software is released under the MIT License.
# For more information, see the LICENSE file in the root directory of this project.


from cv2.typing import MatLike
from mjpeg_streamer import MjpegServer, Stream


class VideoStreamingServer:
	def __init__(self, host: str = "localhost", port: int = 8080) -> None:
		self._server: MjpegServer = MjpegServer(host, port)
		self._streams: dict[str, Stream] = {}

	def add_stream(self, stream_id: str) -> None:
		if stream_id in self._streams:
			raise ValueError(f'Stream with ID "{stream_id}" already exists.')

		stream: Stream = Stream(stream_id)

		self._server.add_stream(stream)
		self._streams[stream_id] = stream

	def update_stream(self, stream_id: str, frame: MatLike) -> None:
		if stream_id not in self._streams:
			raise ValueError(f'Stream with ID "{stream_id}" does not exist.')

		self._streams[stream_id].set_frame(frame)

	def start(self) -> None:
		self._server.start()

	def stop(self) -> None:
		self._server.stop()
