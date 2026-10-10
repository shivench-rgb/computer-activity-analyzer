<<<<<<< HEAD
# Computer Activity Analyzer

A Python-based application that tracks computer activity and records the time spent using different applications.

## Features

* Detects the currently active Windows application
* Tracks application usage time
* Records start and end time
* Stores activity data in SQLite database
* Displays application usage in the terminal
* Automatically creates the activity database
* Tracks multiple applications during a session

## Technologies Used

* Python
* Psutil
* PyWin32
* SQLite
* Datetime

## Project Structure

```text
computer-activity-analyzer/
│
├── computer_activity_analyzer.py
├── README.md
└── .gitignore
```

## Installation

Install the required Python libraries:

```bash
pip install psutil pywin32
```

## How to Run

Clone the repository:

```bash
git clone https://github.com/shivenchaware995-spec/computer-activity-analyzer.git
```

Open the project folder:

```bash
cd computer-activity-analyzer
```

Run the program:

```bash
python computer_activity_analyzer.py
```

The program will start monitoring the active application.

Press:

```text
Ctrl + C
```

to stop the activity tracker.

## Example Output

```text
Computer Activity Analyzer Started
Press Ctrl+C to stop

Code.exe : 5.42 minutes
brave.exe : 2.31 minutes
explorer.exe : 0.45 minutes

Activity tracking stopped.
```

## How It Works

```text
Active Windows Application
          ↓
Detect Process
          ↓
Record Start Time
          ↓
Monitor Application
          ↓
Detect Application Change
          ↓
Calculate Usage Time
          ↓
Save Data to SQLite
```

The program detects the application currently being used on Windows. When the user switches to another application, the program calculates how long the previous application was active and stores the information in an SQLite database.

## Database

The application automatically creates:

```text
activity.db
```

The database stores:

* Application name
* Start time
* End time
* Duration

The database is excluded from GitHub using `.gitignore` because it contains personal computer activity data.

## Future Improvements

* Streamlit dashboard
* Daily usage reports
* Weekly usage reports
* Application usage charts
* Productivity score
* Most-used application analysis
* Idle time detection
* Website usage tracking
* Export reports to CSV
* Productivity and entertainment classification

## Author

Shiven Chaware

GitHub: https://github.com/shivenchaware995-spec
=======
# computer-activity-analyzer
A Python-based computer activity tracker that monitors active Windows applications, records usage duration, and stores activity logs in an SQLite database.
>>>>>>> 4f6c3717e005c94b20ea5f5f7304dd2eff66803c
