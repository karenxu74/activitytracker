import sqlite3
from datetime import datetime

#Connect to the database (create a new file if it doesn't exist)
conn = sqlite3.connect('activity_tracker.db')
c = conn.cursor()

#create the table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS activity_log (datetime TEXT, activity TEXT, happiness_score INTEGER)''')

# Function to get user input and store in the database
def log_activity():
    activity = input("What activity are you working on?")
    happiness_score = int(input("Enter a happiness score (1-5): "))

    #Get the current date and time
    now = datetime.now()
    dt_string =now.strftime("%Y-%m-%d %H:%M:%S")

    #insert the data into the table
    c.execute("INSERT INTO activity_log VALUES(?, ?, ?)",(dt_string, activity, happiness_score))
    conn.commit()
    print("Activity logged successfully!")

#Call the log_activity function
log_activity()
conn.close()