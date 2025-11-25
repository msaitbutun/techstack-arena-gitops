from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import redis
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

redis_host = os.getenv("REDIS_HOST", "localhost")
r = redis.Redis(host=redis_host, port=6379, db=0, decode_responses=True)

def init_db():
    # Mevcut değilse oluştur, varsa dokunma (Reset hariç)
    if not r.exists("votes"):
        r.hset("votes", mapping={"Kubernetes": 0, "Docker": 0, "Terraform": 0, "Ansible": 0})

@app.on_event("startup")
async def startup_event():
    try:
        init_db()
    except:
        pass

@app.get("/")
def read_root():
    return {"status": "API is running", "version": "v1"}

@app.get("/votes")
def get_votes():
    try:
        data = r.hgetall("votes")
        return {k: int(v) for k, v in data.items()}
    except:
        return {"Kubernetes": 0, "Docker": 0, "Terraform": 0, "Ansible": 0}

@app.post("/vote/{tech}")
def vote(tech: str):
    try:
        r.hincrby("votes", tech, 1)
        return {"status": "success", "voted_for": tech}
    except:
        return {"status": "error"}

# --- YENİ EKLENEN KISIM: SIFIRLAMA ---
# ... (Üst kısımlar aynı)

# --- SIFIRLAMA ---
@app.delete("/votes")
def reset_votes():
    try:
        r.delete("votes") 
        # Hemen yeni boş tabloyu oluştur ki grafik patlamasın
        r.hset("votes", mapping={"Kubernetes": 0, "Docker": 0, "Terraform": 0, "Ansible": 0})
        return {"status": "reset_completed"}
    except Exception as e:
        print(f"Error: {e}") # Loglara hata bas
        return {"status": "error"}