import firebase_admin
from firebase_admin import credentials, db

FIREBASE_CRED_PATH = "serviceAccountKey.json"
FIREBASE_DB_URL    = "https://apmas-parking-default-rtdb.asia-southeast1.firebasedatabase.app"

def init_firebase():
    try:
        cred = credentials.Certificate(FIREBASE_CRED_PATH)
        firebase_admin.initialize_app(cred, {"databaseURL": FIREBASE_DB_URL})
        print("[Firebase] Connected OK")
    except Exception as e:
        print(f"[Firebase] Error: {e}")

def get_tickets_ref():       return db.reference("/tickets")
def get_ticket_ref(tid):     return db.reference(f"/tickets/{tid}")
def get_slots_ref():         return db.reference("/slots")        # ← เพิ่ม
def get_slot_ref(slot_id):   return db.reference(f"/slots/{slot_id}")  # ← เพิ่ม