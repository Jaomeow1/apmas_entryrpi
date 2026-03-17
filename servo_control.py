import httpx
import asyncio

# ── ตั้งค่า ──────────────────────────────────────────
PI4_IP   = "10.153.161.13"   # ← เปลี่ยนเป็น IP จริงของ Pi4
PI4_PORT = 8001              # port ที่ Pi4 รับคำสั่ง (แยกจาก port Server)
PI4_URL  = f"http://{PI4_IP}:{PI4_PORT}"
# ─────────────────────────────────────────────────────

async def open_gate(ticket_id: str) -> dict:
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            res = await client.post(f"{PI4_URL}/gate/open",
                                    json={"ticket_id": ticket_id, "action": "open"})
            return {"success": True, "response": res.json()}
    except httpx.ConnectError:
        return {"success": False, "error": "เชื่อมต่อ Pi4 ไม่ได้"}
    except httpx.TimeoutException:
        return {"success": False, "error": "Pi4 timeout"}
    except Exception as e:
        return {"success": False, "error": str(e)}