import psutil
import time
import sqlite3
from datetime import datetime

database = "activity.db"

connection = sqlite3.connect(database)
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS activity (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    application TEXT,
    start_time TEXT,
    end_time TEXT,
    duration REAL
)
""")

connection.commit()


def get_active_application():
    try:
        import win32gui
        import win32process

        window = win32gui.GetForegroundWindow()

        if window == 0:
            return "Unknown"

        _, process_id = win32process.GetWindowThreadProcessId(window)

        process = psutil.Process(process_id)

        return process.name()

    except:
        return "Unknown"


def save_activity(application, start_time, end_time, duration):

    cursor.execute(
        """
        INSERT INTO activity
        (application, start_time, end_time, duration)
        VALUES (?, ?, ?, ?)
        """,
        (
            application,
            start_time,
            end_time,
            duration
        )
    )

    connection.commit()


def main():

    print("Computer Activity Analyzer Started")
    print("Press Ctrl+C to stop")

    current_application = None
    start_time = time.time()

    try:

        while True:

            application = get_active_application()

            if application != current_application:

                if current_application is not None:

                    end_time = time.time()

                    duration = end_time - start_time

                    save_activity(
                        current_application,
                        datetime.fromtimestamp(start_time).strftime("%Y-%m-%d %H:%M:%S"),
                        datetime.fromtimestamp(end_time).strftime("%Y-%m-%d %H:%M:%S"),
                        duration
                    )

                    print(
                        current_application
                        + " : "
                        + str(round(duration / 60, 2))
                        + " minutes"
                    )

                current_application = application
                start_time = time.time()

            time.sleep(2)

    except KeyboardInterrupt:

        print("\nActivity tracking stopped.")

    connection.close()


main()