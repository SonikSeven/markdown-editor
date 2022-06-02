# Markdown Editor

This project is a Python-based command-line interface (CLI) tool that simplifies the creation of Markdown documents. It allows users to interactively apply formatting options such as headers, bold or italic text, links, ordered and unordered lists, and more. The final formatted content is saved to a Markdown file, making it easy to generate well-structured documentation or notes without memorizing Markdown syntax.

## Features

- **Interactive Interface:** Offers a step-by-step guide to choose formatting options.
- **Multiple Formatting Options:** Supports headers, bold, italic, inline-code text, links, and lists.
- **Lists:** Create both ordered and unordered lists.
- **Automatic File Saving:** Outputs the final content to `output.md`.

## Requirements

- [Python 3](https://www.python.org/downloads/)

## Installation

This application is written in Python, so you'll need Python installed on your computer to run it. If you don't have Python installed, you can download it from [python.org](https://www.python.org/downloads/).

To install this project, clone the repository to your local machine:

```
git clone https://github.com/SonikSeven/markdown-editor.git
```

## How to Run

To run the program, follow these steps:

1. Open a terminal and navigate to the directory where the script is located.
2. Run the script using Python:

```
python main.py
```

## Usage

Follow the on-screen prompts to select formatting options and input your text. Here's a brief overview of the commands:

- `!help` - Displays the available formatters and special commands.
- `!done` - Saves the current content to `output.md` and exits the script.

### Available Formatters

- `plain` - Inserts plain text.
- `bold` - Applies bold formatting.
- `italic` - Applies italic formatting.
- `header` - Inserts a header of specified level.
- `link` - Creates a hyperlink.
- `inline-code` - Applies inline code formatting.
- `ordered-list` - Generates an ordered list.
- `unordered-list` - Generates an list.
- `new-line` - Inserts a new line.

## License

This project is open-source and available under the [MIT License](LICENSE).
