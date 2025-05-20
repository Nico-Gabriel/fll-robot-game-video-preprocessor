# Copyright (c) 2025 Nico-Gabriel Ruckendorfer
#
# This software is released under the MIT License.
# For more information, see the LICENSE file in the root directory of this project.


def _calculate_content_line_length(
	title: str,
	note: str | None,
	list_title: str | None,
	list_items: list[str] | None,
	title_icon_length: int,
	list_icon_length: int,
	separator_length: int,
	min_padding: int,
) -> int:
	min_title_line_length: int = len(title) + (separator_length + title_icon_length + min_padding) * 2
	min_note_line_length: int = len(note) + min_padding * 2 if note else 0
	min_list_title_line_length: int = len(list_title) + separator_length + min_padding if list_title else 0
	max_list_item_length: int = max(len(list_item) for list_item in list_items) if list_items else 0
	min_list_items_line_length: int = (
		max_list_item_length + separator_length * 2 + list_icon_length + min_padding if list_items else 0
	)

	return max(min_title_line_length, min_note_line_length, min_list_title_line_length, min_list_items_line_length)


def _split_spaces(number_of_spaces: int) -> tuple[int, int]:
	left_spaces: int = number_of_spaces // 2
	right_spaces: int = number_of_spaces // 2 + number_of_spaces % 2

	return left_spaces, right_spaces


def _generate_title_line(
	title: str,
	border_icon: str,
	title_icon: str,
	title_icon_length: int,
	separator_length: int,
	content_line_length: int,
) -> str:
	spaces: int = content_line_length - len(title) - (separator_length + title_icon_length) * 2
	left_spaces, right_spaces = _split_spaces(spaces)

	return (
		border_icon
		+ " " * left_spaces
		+ title_icon
		+ " " * separator_length
		+ title
		+ " " * separator_length
		+ title_icon
		+ " " * right_spaces
		+ border_icon
	)


def _generate_note_line(note: str) -> str:
	return ""


def generate_info_box(
	title: str,
	note: str | None = None,
	list_title: str | None = None,
	list_items: list[str] | None = None,
	border_icon: str = "*",
	border_icon_length: int = 1,
	title_icon: str = "✨",
	title_icon_length: int = 2,
	list_icon: str = "➡️ ",
	list_icon_length: int = 2,
	separator_length: int = 1,
	min_padding: int = 3,
) -> str:
	"""
	set lengths of icons manually due to issues with emoji width
	"""

	info_box: str = ""

	...

	content_line_length: int = _calculate_content_line_length(
		title, note, list_title, list_items, title_icon_length, list_icon_length, separator_length, min_padding
	)
	box_line_length: int = content_line_length + border_icon_length * 2

	border_line: str = border_icon * box_line_length
	spacer_line: str = border_icon + " " * content_line_length + border_icon
	title_line: str = _generate_title_line(title)
	note_line: str | None = _generate_note_line(note) if note else None

	...

	return info_box


def print_info_box(
	title: str,
	note: str | None = None,
	list_title: str | None = None,
	list_items: list[str] | None = None,
	border_icon: str = "*",
	border_icon_length: int = 1,
	title_icon: str = "✨",
	title_icon_length: int = 2,
	list_icon: str = "➡️ ",
	list_icon_length: int = 2,
	separator_length: int = 1,
	min_padding: int = 3,
) -> None:
	print(
		generate_info_box(
			title,
			note,
			list_title,
			list_items,
			border_icon,
			border_icon_length,
			title_icon,
			title_icon_length,
			list_icon,
			list_icon_length,
			separator_length,
			min_padding,
		)
	)


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
