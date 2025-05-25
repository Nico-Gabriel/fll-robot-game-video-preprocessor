# Copyright (c) 2025 Nico-Gabriel Ruckendorfer
#
# This software is released under the MIT License.
# For more information, see the LICENSE file in the root directory of this project.


def _validate_generate_info_box_parameter_types(
	title: str,
	note: str | None,
	list_title: str | None,
	list_items: list[str] | None,
	border_icon: str,
	border_icon_length: int,
	title_icon: str,
	title_icon_length: int,
	list_icon: str,
	list_icon_length: int,
	separator_length: int,
	min_padding: int,
) -> None:
	if not isinstance(title, str):
		raise TypeError("Parameter 'title' must be of type 'str'.")

	if not isinstance(note, str) and note is not None:
		raise TypeError("Parameter 'note' must be of type 'str' or 'None'.")

	if not isinstance(list_title, str) and list_title is not None:
		raise TypeError("Parameter 'list_title' must be of type 'str' or 'None'.")

	if not isinstance(list_items, list) and list_items is not None:
		raise TypeError("Parameter 'list_items' must be of type 'list' or 'None'.")

	if not all(isinstance(list_item, str) for list_item in list_items) if list_items else True:
		raise TypeError("Parameter 'list_items' must only contain elements of type 'str'.")

	if not isinstance(border_icon, str):
		raise TypeError("Parameter 'border_icon' must be of type 'str'.")

	if not isinstance(border_icon_length, int):
		raise TypeError("Parameter 'border_icon_length' must be of type 'int'.")

	if not isinstance(title_icon, str):
		raise TypeError("Parameter 'title_icon' must be of type 'str'.")

	if not isinstance(title_icon_length, int):
		raise TypeError("Parameter 'title_icon_length' must be of type 'int'.")

	if not isinstance(list_icon, str):
		raise TypeError("Parameter 'list_icon' must be of type 'str'.")

	if not isinstance(list_icon_length, int):
		raise TypeError("Parameter 'list_icon_length' must be of type 'int'.")

	if not isinstance(separator_length, int):
		raise TypeError("Parameter 'separator_length' must be of type 'int'.")

	if not isinstance(min_padding, int):
		raise TypeError("Parameter 'min_padding' must be of type 'int'.")


def _validate_generate_info_box_parameter_values(
	title: str,
	border_icon: str,
	border_icon_length: int,
	title_icon: str,
	title_icon_length: int,
	list_icon: str,
	list_icon_length: int,
	separator_length: int,
	min_padding: int,
) -> None:
	if not title:
		raise ValueError("Parameter 'title' must not be empty.")

	if not border_icon:
		raise ValueError("Parameter 'border_icon' must not be empty.")

	if border_icon_length < 1:
		raise ValueError("Parameter 'border_icon_length' must be at least 1.")

	if not title_icon:
		raise ValueError("Parameter 'title_icon' must not be empty.")

	if title_icon_length < 1:
		raise ValueError("Parameter 'title_icon_length' must be at least 1.")

	if not list_icon:
		raise ValueError("Parameter 'list_icon' must not be empty.")

	if list_icon_length < 1:
		raise ValueError("Parameter 'list_icon_length' must be at least 1.")

	if separator_length < 0:
		raise ValueError("Parameter 'separator_length' must be greater than or equal to 0.")

	if min_padding < 0:
		raise ValueError("Parameter 'min_padding' must be greater than or equal to 0.")


def _validate_generate_info_box_parameters(
	title: str,
	note: str | None,
	list_title: str | None,
	list_items: list[str] | None,
	border_icon: str,
	border_icon_length: int,
	title_icon: str,
	title_icon_length: int,
	list_icon: str,
	list_icon_length: int,
	separator_length: int,
	min_padding: int,
) -> None:
	_validate_generate_info_box_parameter_types(
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
	_validate_generate_info_box_parameter_values(
		title,
		border_icon,
		border_icon_length,
		title_icon,
		title_icon_length,
		list_icon,
		list_icon_length,
		separator_length,
		min_padding,
	)


def round_up_x_to_multiple_of_y(x: int, y: int) -> int:
	if x <= 0 or y <= 0:
		raise ValueError("Both parameters 'x' and 'y' must be greater than 0.")

	return x if x % y == 0 else x + y - x % y


def _calculate_content_line_length(
	title: str,
	note: str | None,
	list_title: str | None,
	list_items: list[str] | None,
	border_icon_length: int,
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
	max_line_length: int = max(
		min_title_line_length, min_note_line_length, min_list_title_line_length, min_list_items_line_length
	)

	return round_up_x_to_multiple_of_y(max_line_length, border_icon_length)


def _calculate_box_line_length(border_icon_length: int, content_line_length: int) -> int:
	return content_line_length + border_icon_length * 2


def _generate_border_line(border_icon: str, border_icon_length: int, box_line_length: int) -> str:
	return border_icon * (box_line_length // border_icon_length)


def _generate_spacer_line(border_icon: str, content_line_length: int) -> str:
	return border_icon + " " * content_line_length + border_icon


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


def _generate_note_line(note: str, border_icon: str, content_line_length: int) -> str:
	spaces: int = content_line_length - len(note)
	left_spaces, right_spaces = _split_spaces(spaces)

	return border_icon + " " * left_spaces + note + " " * right_spaces + border_icon


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

	_validate_generate_info_box_parameters(
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

	info_box: str = ""

	...

	content_line_length: int = _calculate_content_line_length(
		title,
		note,
		list_title,
		list_items,
		border_icon_length,
		title_icon_length,
		list_icon_length,
		separator_length,
		min_padding,
	)
	box_line_length: int = _calculate_box_line_length(border_icon_length, content_line_length)

	border_line: str = _generate_border_line(border_icon, border_icon_length, box_line_length)
	spacer_line: str = _generate_spacer_line(border_icon, content_line_length)
	title_line: str = _generate_title_line(
		title, border_icon, title_icon, title_icon_length, separator_length, content_line_length
	)
	note_line: str | None = _generate_note_line(note, border_icon, content_line_length) if note else None

	...

	info_box += border_line + "\n"
	info_box += spacer_line + "\n"
	info_box += title_line + "\n"
	info_box += spacer_line + "\n"
	if note_line:
		info_box += note_line + "\n"
		info_box += spacer_line + "\n"
	info_box += border_line + "\n"

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
