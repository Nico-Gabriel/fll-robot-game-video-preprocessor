# Copyright (c) 2025 Nico-Gabriel Ruckendorfer
#
# This software is released under the MIT License.
# For more information, see the LICENSE file in the root directory of this project.


def generate_info_box(
	title: str,
	note: str | None = None,
	list_title: str | None = None,
	list_items: list[str] | None = None,
) -> str:
	info_box: str = ""
	border_icon: str = "*"
	title_icon: str = "✨"
	list_icon: str = "➡️"

	return info_box


def print_info_box(
	title: str,
	note: str | None = None,
	list_title: str | None = None,
	list_items: list[str] | None = None,
) -> None:
	print(generate_info_box(title, note, list_title, list_items))


def main() -> None:
	print_info_box(
		"FLL Robot Game Video Processor",
		"Press CTRL+C to exit",
		"Video streams:",
		[
			"http://localhost:8080/red-team-video",
			"http://localhost:8080/blue-team-video",
		],
	)


if __name__ == "__main__":
	main()
