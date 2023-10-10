# File Organizer and Notification System

This repository contains two scripts for organizing folder and providing notifications when changes occur in the specified folder. This system automates file organization and keeps you informed about file-related events.

## Prerequisites

- Linux-based operating system (tested on Ubuntu).
- Python 3.x.
- `inotifywait` library for monitoring file changes (`sudo apt install inotify-tools`) for `file_watcher.sh`.
- `notify-send` utility for notifications (pre-installed on most Linux systems) for `file_watcher.sh`.
  
## `file_organizer.py` - File Organizer

`file_organizer.py` is a Python script designed to manage and organize files based on their file extensions. It categorizes files into different folders, making it easier to keep your folder tidy.

### Features

- Organizes files into categories like documents, images, videos, and more.
- Logs events and actions in `file_organizer.log`.
- Customizable sorting rules and destination directories.

### Configuration

1. Open `file_organizer.py`.
2. Modify the variable `DIRECTORY_TO_ORGANIZE_PATH` to the path of the directory you want to organize or set an environment variable with the same name.
3. Save the changes.

### Usage

To use the `file_organizer.py` script:

```bash
python3 file_organizer.py
```

## File watcher - Notification System

**file_watcher.sh** is a Bash script that complements the file organizer by monitoring changes in the specified folder and displaying notifications using `notify-send`.

### Features

- Monitors the specified folder and the `file_organizer.py` script for changes.
- Sends notifications for events like file moves and script reloads.

### Configuration

Customize the `DIRECTORY_TO_ORGANIZE_PATH` environment variable to specify the folder to monitor.

### Usage

To use the **file_watcher.sh** script:

```bash
chmod +x file_watcher.sh
./file_watcher.sh &
```

*Note* : The **&** at the end of the command runs the script in the background. You can also run the script in a separate terminal window.

## Customization

Feel free to customize the scripts to suit your specific needs. You can modify sorting rules, notification messages, and more according to your preferences.

## Contribution

Contributions are welcome! If you have ideas for improvements or new features, please open an issue or create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 