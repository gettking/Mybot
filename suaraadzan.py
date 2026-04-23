import asyncio
import edge_tts

text = """
Allahu Akbar, Allahu Akbar.
Ashhadu alla ilaha illallah.
Ashhadu anna Muhammadar Rasulullah.
Hayya 'alas salah.
Hayya 'alal falah.
Allahu Akbar, Allahu Akbar.
La ilaha illallah.
"""

async def main():
    communicate = edge_tts.Communicate(text, "id-ID-ArdiNeural")
    await communicate.save("azan.mp3")

asyncio.run(main())
