import uuid
import qrcode

class Pix:
  def __init__(self):
    pass
  
  def create_payment(self):
    #criar o pagamento na instituição financeira
    bank_paid_id = str(uuid.uuid4())
    
    #código copia e cola_123
    hash_payment = f'hash_payment_{bank_paid_id}'
    
    #qr_code 
    img = qrcode.make(hash_payment)
    
    #salva o arquivo como imagem png
    img.save(f"static/img/qr_code_payment_{bank_paid_id}.png")
    
    return {"bank_paid_id": bank_paid_id,
             "qr_code_path": f"qr_code_payment_{bank_paid_id}"}