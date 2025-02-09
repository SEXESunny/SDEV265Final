from datetime import datetime, timedelta


class CurrentWeekSignInSignOut:
    def __init__(self, db):
        self.db = db

    # This is mostly just for testing purposes. We'll mainly be using the update entry method.
    # It is here however if we need it.
    def add_entry(self, badge_num, date, sign_in_time, sign_out_time, additional_notes):
        with self.db.connect() as conn:
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO CurrentWeekSignInSignOut (BadgeNum, Date, SignInTime, SignOutTime, AdditionalNotes)
                              VALUES (?, ?, ?, ?, ?)''',
                           (badge_num, date, sign_in_time, sign_out_time, additional_notes))
            conn.commit()

    # The main driving code to update current weekly entries
    def update_entry(self, record_id, sign_in_time, sign_out_time, additional_notes):
        with self.db.connect() as conn:
            cursor = conn.cursor()
            cursor.execute('''UPDATE CurrentWeekSignInSignOut
                                      SET SignInTime = ?, SignOutTime = ?, AdditionalNotes = ?
                                      WHERE RecordID = ?''',
                           (sign_in_time, sign_out_time, additional_notes, record_id))
            conn.commit()

    # Return ALL current weekly entries
    def get_all_entries(self):
        with self.db.connect() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM CurrentWeekSignInSignOut')
            return cursor.fetchall()

    # Clear every entry.
    def clear_entries(self):
        with self.db.connect() as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM CurrentWeekSignInSignOut')
            conn.commit()

    # Get the week date range for the current week. This could be a static method but I try to avoid them as much as
    # possible.
    def get_current_week_dates(self):
        today = datetime.today()
        start_of_week = today - timedelta(days=today.weekday())  # Monday
        return [start_of_week + timedelta(days=i) for i in range(7)]  # List of 7 days
