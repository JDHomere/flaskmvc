from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
import datetime


class Courses(db.Model):
    courseID = db.Column(db.Integer, primary_key=True)
    jobID = db.Column(db.Integer, db.ForeignKey('jobs.jobID'), nullable=False)
    courseName = db.Column(db.String(80), nullable=True)
    courseDescription = db.Column(db.String(1000), nullable=True)
    skills = db.Column(db.String(100), nullable=True)
    jobs = db.relationship('Jobs')
    def toDict(self):
        return {
            "courseID": self.courseID,
            "courseName": self.courseName,
            "courseDescription": self.courseDescription,
            "skills": self.skills
            }