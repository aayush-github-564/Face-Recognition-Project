import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://faceattendancesystem-ffeb1-default-rtdb.asia-southeast1.firebasedatabase.app/"
})

ref = db.reference('Students')

data = {
    "1RF22EC001":
        {
            "name": "Aayush Mishra",
            "major": "ECE",
            "starting_year": 2022,
            "total_attendance": 3,
            "section": "E",
            "sem": 5,
            "last_attendance_time": "2024-12-15 00:54:34"
        },
    "1RF22EC005":
        {
            "name": "Anku Kumar",
            "major": "ECE",
            "starting_year": 2022,
            "total_attendance": 2,
            "section": "D",
            "sem": 5,
            "last_attendance_time": "2024-12-11 00:54:34"
        },
    "1RF22EC009":
        {
            "name": "Sarvamangala",
            "major": "ECE",
            "starting_year": 2022,
            "total_attendance": 2,
            "section": "D",
            "sem": 5,
            "last_attendance_time": "2024-12-11 00:54:34"
        },
    "1RF22EC010":
        {
            "name": "Basava",
            "major": "ECE",
            "starting_year": 2022,
            "total_attendance": 2,
            "section": "D",
            "sem": 5,
            "last_attendance_time": "2024-12-11 00:54:34"
        },
    "1RF22EC012":
        {
            "name": "Chetan",
            "major": "ECE",
            "starting_year": 2022,
            "total_attendance": 2,
            "section": "D",
            "sem": 5,
            "last_attendance_time": "2024-12-11 00:54:34"
        },
    "1RF22EC013":
        {
            "name": "Danish Ali",
            "major": "ECE",
            "starting_year": 2022,
            "total_attendance": 4,
            "section": "B",
            "sem": 5,
            "last_attendance_time": "2024-12-11 00:54:34"
        },
    "1RF22EC017":
        {
            "name": "Karthik",
            "major": "ECE",
            "starting_year": 2022,
            "total_attendance": 2,
            "section": "D",
            "sem": 5,
            "last_attendance_time": "2024-12-11 00:54:34"
        },
    "1RF22EC032":
        {
            "name": "Pranav Athreya",
            "major": "ECE",
            "starting_year": 2022,
            "total_attendance": 2,
            "section": "D",
            "sem": 5,
            "last_attendance_time": "2024-12-11 00:54:34"
        },
    "1RF22EC048":
        {
            "name": "Shrujan",
            "major": "ECE",
            "starting_year": 2022,
            "total_attendance": 2,
            "section": "D",
            "sem": 5,
            "last_attendance_time": "2024-12-11 00:54:34"
        },
    "1RF22EC050":
        {
            "name": "Soham Mandal",
            "major": "ECE",
            "starting_year": 2022,
            "total_attendance": 2,
            "section": "D",
            "sem": 5,
            "last_attendance_time": "2024-12-11 00:54:34"
        },
    "1RF22EC051":
        {
            "name": "Suchit",
            "major": "ECE",
            "starting_year": 2022,
            "total_attendance": 2,
            "section": "D",
            "sem": 5,
            "last_attendance_time": "2024-12-11 00:54:34"
        },
    "1RF22EC055":
        {
            "name": "Suraj Kumar",
            "major": "ECE",
            "starting_year": 2022,
            "total_attendance": 2,
            "section": "D",
            "sem": 5,
            "last_attendance_time": "2024-12-11 00:54:34"
        },
    "1RF22EC061":
        {
            "name": "Vijay Kumar",
            "major": "ECE",
            "starting_year": 2022,
            "total_attendance": 2,
            "section": "D",
            "sem": 5,
            "last_attendance_time": "2024-12-11 00:54:34"
        },
    "1RF22EC400":
        {
            "name": "Manas",
            "major": "ECE",
            "starting_year": 2022,
            "total_attendance": 2,
            "section": "D",
            "sem": 5,
            "last_attendance_time": "2024-12-11 00:54:34"
        },
    "1RF22EC401":
        {
            "name": "Manoj",
            "major": "ECE",
            "starting_year": 2022,
            "total_attendance": 2,
            "section": "D",
            "sem": 5,
            "last_attendance_time": "2024-12-11 00:54:34"
        }
    }

for key, value in data.items():
    ref.child(key).set(value)