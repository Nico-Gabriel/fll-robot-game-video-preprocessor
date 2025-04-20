from cv2.typing import MatLike
from mjpeg_streamer import MjpegServer, Stream


class VideoStreamingServer:
	def __init__(self, host: str = "localhost", port: int = 8080) -> None:
		self.server: MjpegServer = MjpegServer(host, port)
		self.streams: dict[str, Stream] = {}

	def add_stream(self, stream_id: str) -> None:
		if stream_id in self.streams:
			raise ValueError(f'Stream with ID "{stream_id}" already exists.')

		stream: Stream = Stream(stream_id)

		self.server.add_stream(stream)
		self.streams[stream_id] = stream

	def update_stream(self, stream_id: str, frame: MatLike) -> None:
		if stream_id not in self.streams:
			raise ValueError(f'Stream with ID "{stream_id}" does not exist.')

		self.streams[stream_id].set_frame(frame)

	def start(self) -> None:
		self.server.start()

	def stop(self) -> None:
		self.server.stop()
