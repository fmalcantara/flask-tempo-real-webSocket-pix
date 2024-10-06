from repository.database import db

class Payment(db.Model):
  #id, value, paid, bank_paid_id, qr_code, expiration_date
  id = db.Column(db.Integer, primary_key=True)
  value = db.Column(db.Float)
  paid = db.Column(db.Boolean, default=False)
  bank_paid_id = db.Column(db.String(200), nullable=True)
  qr_code = db.Column(db.String(100), nullable=True)
  expiration_date = db.Column(db.DateTime) # 2024-05-10 10h:15m:32s
  
  def to_dict(self):
    return {
      "id": self.id,
      "value": self.value,
      "paid": self.paid,
      "bank_paid_id": self.bank_paid_id,
      "qr_code": self.qr_code,
      "expiration_date": self.expiration_date
    }