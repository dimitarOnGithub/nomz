from nomz import db


class Category(db.Model):
    __tablename__ = "categories"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    blurb = db.Column(db.Text)
    img_src = db.Column(db.String(150))

