from datetime import timedelta, datetime


class PreviousWeeksSignInSignOut:
    def __init__(self, db):
        self.db = db

    # These 3 methods are essentially the same as the get current entries.
    def add_entry(self, badge_num, date, sign_in_time, sign_out_time, additional_notes):
        with self.db.connect() as conn:
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO PreviousWeeksSignInSignOut (BadgeNum, Date, SignInTime, SignOutTime, AdditionalNotes)
                              VALUES (?, ?, ?, ?, ?)''',
                           (badge_num, date, sign_in_time, sign_out_time, additional_notes))
            conn.commit()

    def update_entry(self, record_id, sign_in_time, sign_out_time, additional_notes):
        with self.db.connect() as conn:
            cursor = conn.cursor()
            cursor.execute('''UPDATE PreviousWeeksSignInSignOut
                              SET SignInTime = ?, SignOutTime = ?, AdditionalNotes = ?
                              WHERE RecordID = ?''',
                           (sign_in_time, sign_out_time, additional_notes, record_id))
            conn.commit()

    def get_entries_for_week(self, start_date, end_date):
        with self.db.connect() as conn:
            cursor = conn.cursor()
            cursor.execute('''SELECT * FROM PreviousWeeksSignInSignOut WHERE Date BETWEEN ? AND ?''',
                           (start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d')))
            return cursor.fetchall()





