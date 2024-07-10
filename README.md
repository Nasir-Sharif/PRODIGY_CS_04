# PRODIGY_CS_04

# Keylogger GUI in Python

## Introduction

This project implements a keylogger with a hacker-themed graphical user interface (GUI) using Python. The keylogger captures keystrokes and logs them to a file while providing a visually engaging interface using the `tkinter` library for GUI development and `pynput` for capturing keystrokes.

## Prerequisites

Before running this keylogger, ensure you have Python installed on your system. You will also need to install the following Python libraries:

- `tkinter`: Used for creating the GUI.
- `pynput`: Used for capturing and monitoring keyboard inputs.

Install `pynput` using pip:

```bash
pip install pynput
```

## Getting Started

### Step 1: Clone the Repository

```

### Step 2: Navigate to the Directory

Navigate into the cloned repository directory:

```bash
cd keylogger-project
```

### Step 3: Run the Keylogger

Run the `keylogger_gui.py` script:

```bash
python keylogger_gui.py
```

## Functionality

### GUI Layout

The GUI features:
- A black background with green text to give a hacker-themed appearance.
- Start and Stop buttons to control the keylogger.
- A label displaying "Keylogger By Nasir Sharif".

### Keylogging

The keylogger:
- Captures keystrokes including letters, numbers, and special keys.
- Writes keystrokes to the `keylog.txt` file in the same directory.
- Stops capturing keystrokes when the 'Esc' key is pressed.

### Threaded Keylogger

To ensure responsiveness:
- The keylogger runs in a separate thread using Python's `threading` module.
- This allows the GUI to remain responsive while the keylogger captures keystrokes in the background.

## Ethical Considerations

### Consent

Ensure you have explicit consent from all users being monitored by this keylogger.

### Legal Compliance

Adhere to all relevant laws and regulations regarding the use of keyloggers in your jurisdiction.

### Transparency

Clearly communicate the purpose and use of the keylogger to all stakeholders.

## Troubleshooting

- **Not Responding**: If the GUI becomes unresponsive, check for errors in the terminal and ensure Python and necessary libraries are properly installed.

## Contributing

Contributions to enhance the functionality or improve the codebase are welcome! Please fork the repository, make your changes, and submit a pull request.


## Acknowledgments

- Special thanks to Prodigy Infotech for their support and resources during the development of this project.

