# Operating System Detector using Python

## Overview

This Python script detects and displays detailed information about the operating system running on a computer. It uses Python's built-in `platform` module to gather system information and identify the OS type.

## Features

* Detects the operating system name.
* Displays the OS version.
* Shows the OS release number.
* Displays the machine architecture/type.
* Identifies whether the system is:

  * Microsoft Windows
  * Linux
  * macOS
  * Unknown Operating System

## Technologies Used

* Python 3
* Built-in `platform` module

## How It Works

The script collects system information using functions from the `platform` module:

* `platform.system()` → Returns the operating system name.
* `platform.version()` → Returns the OS version.
* `platform.release()` → Returns the OS release.
* `platform.machine()` → Returns the machine architecture.

The script then compares the detected OS name and prints a user-friendly message indicating the operating system type.

## Example Output

```text
Detecting Operating system...

-----SYSTEM INFORMATION-----
Operating System: Windows
OS Version: 10.0.26100
OS Release: 11
Machine Type: AMD64

-----OS TYPE DETECTION-----
This system is running Microsoft Windows.
```

## Use Cases

* Learning Python system programming.
* Beginner cybersecurity projects.
* System inventory and auditing.
* Environment detection before running scripts.
* IT support and troubleshooting tools.
* Educational projects involving operating systems.

## Requirements

* Python 3.x

No external libraries are required.

## Running the Script

```bash
python os_detector.py
```

## Project Structure

```text
Os-detection/
│
├── os.py
└── README.md
```

## Future Improvements

* Display processor information.
* Show hostname and IP address.
* Detect installed RAM.
* Export system information to a text file.
* Add GUI support using Tkinter.

## License

This project is open-source and available for educational purposes.
