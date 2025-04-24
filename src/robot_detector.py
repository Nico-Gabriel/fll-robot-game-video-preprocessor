# Copyright (c) 2025 Nico-Gabriel Ruckendorfer
#
# This software is released under the MIT License.
# For more information, see the LICENSE file in the root directory of this project.


from cv2.typing import MatLike


class RobotDetector:
	def detect_robot(self, frame: MatLike) -> tuple[int, int, int, int] | None: ...
