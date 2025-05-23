from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# ------------------ Student ------------------
class Student(db.Model):
    __tablename__ = 'students'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))
    contact = db.Column(db.String(20))
    
    batch_id = db.Column(db.String(20), db.ForeignKey('batches.bid'))
    performance_scores = db.relationship('PerformanceScore', backref='student', cascade="all, delete-orphan")


# ------------------ Coach ------------------
class Coach(db.Model):
    __tablename__ = 'coaches'
    
    cid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    
    batch_id = db.Column(db.String(20), db.ForeignKey('batches.bid'))

    supervisor_id = db.Column(db.Integer, db.ForeignKey('coaches.cid'))

    salary = db.Column(db.Float)

    supervisor = db.relationship(
        'Coach',
        remote_side=[cid],
        backref='supervised_coaches'
    )


# ------------------ Batch ------------------
class Batch(db.Model):
    __tablename__ = 'batches'
    
    bid = db.Column(db.String(20), primary_key=True)
    fees = db.Column(db.Float)
    location = db.Column(db.String(50))
    
    students = db.relationship('Student', backref='batch', cascade="all, delete-orphan")
    coaches = db.relationship('Coach', backref='batch', cascade="all, delete-orphan")
    waiting_students = db.relationship('WaitingStudent', backref='batch', cascade="all, delete-orphan")
    schedule_entries = db.relationship('ScheduleEntry', backref='batch', cascade="all, delete-orphan")


# ------------------ Waiting List ------------------
class WaitingStudent(db.Model):
    __tablename__ = 'waiting_students'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(20))
    
    batch_id = db.Column(db.String(20), db.ForeignKey('batches.bid'))


# ------------------ Schedule Entry ------------------
class ScheduleEntry(db.Model):
    __tablename__ = 'schedule_entries'
    
    id = db.Column(db.Integer, primary_key=True)
    
    batch_id = db.Column(db.String(20), db.ForeignKey('batches.bid'), nullable=False)
    day_of_week = db.Column(db.String(10), nullable=False)
    start_time = db.Column(db.Time, nullable=False)
    end_time = db.Column(db.Time, nullable=False)


# ------------------ Performance Score ------------------
class PerformanceScore(db.Model):
    __tablename__ = 'performance_scores'
    
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    test1 = db.Column(db.Integer)
    test2 = db.Column(db.Integer)
    test3 = db.Column(db.Integer)
