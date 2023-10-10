#!/bin/bash
inotify_pid=$(ps aux | grep 'inotifywait' | grep -v 'grep' | awk '{print $2}')
# Command to execute when changes are detected
FILE_ORGANIZER_SCRIPT="file_organizer.py"

if [ -n "$inotify_pid" ]; then
    # Kill the inotifywait process
    echo "Killed inotifywait process with PID $inotify_pid."
    sleep 1
    kill -9 "$inotify_pid"
fi

send_notification() {
    echo "$1"
    if [ -z "$1" ]; then
        return
    fi
    notify-send --app-name="File Organizer:$DIRECTORY_TO_ORGANIZE_PATH" --icon=dialog-information "$1"
}

# Monitor the Downloads folder for events
inotifywait -m -e modify,move,create,delete "$DIRECTORY_TO_ORGANIZE_PATH" "$FILE_ORGANIZER_SCRIPT" |
    while read -r directory event filename; do
        # Run your script when changes are detected
        if [ "$directory" == "$FILE_ORGANIZER_SCRIPT" ]; then

            # Reload the watch_downloads.sh script
            log_message=$(python3 "$FILE_ORGANIZER_SCRIPT" 2>&1)
            send_notification "$log_message"

        elif [[ "$event" == "MODIFY" || "$event" == "CREATE" ]]; then
            log_message=$(python3 "$FILE_ORGANIZER_SCRIPT" 2>&1)
            send_notification "$log_message"
        fi
    done
