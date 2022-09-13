from database import db

def create(object):
    try:
        db.session.add(object)
    except Exception as e:
        print("Error:", e)
        return False
    else:
        db.session.commit()
        return True

def update(object):
    try:     
        db.session.add(object)
    except Exception as e:
        print("Error:", e)
        return False
    else:
        db.session.commit()
        return True

def delete(object):
    try:
        db.session.delete(object)
    except Exception as e:
        print("Error:", e)
        return False
    else:
        db.session.commit()
        return True
