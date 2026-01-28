# Copyright (c) 2025 TheHamkerAlone
# Licensed under the MIT License.
# Optimized for Minimalist Style

from pyrogram import types
from AloneX import app, config

class Inline:
    def __init__(self):
        self.ikm = types.InlineKeyboardMarkup
        self.ikb = types.InlineKeyboardButton

    def start_key(self, lang: dict = None) -> types.InlineKeyboardMarkup:
        # Sadece Gruba Ekle, Kanal ve Kapat
        return self.ikm(
            [
                [
                    self.ikb(
                        text="➕ Beni Grubuna Ekle",
                        url=f"https://t.me/{app.username}?startgroup=true",
                    )
                ],
                [
                    self.ikb(text="📢 Kanal", url=config.SUPPORT_CHANNEL),
                    self.ikb(text="🗑 Kapat", callback_data="close"),
                ],
            ]
        )

    def controls(self, chat_id: int, is_playing: bool = True) -> types.InlineKeyboardMarkup:
        # Müzik kontrollerini de sadeleştirdik
        return self.ikm(
            [
                [
                    self.ikb(text="⏮", callback_data=f"controls replay {chat_id}"),
                    self.ikb(text="⏸" if is_playing else "▶️", callback_data=f"controls {'pause' if is_playing else 'resume'} {chat_id}"),
                    self.ikb(text="⏭", callback_data=f"controls skip {chat_id}"),
                ],
                [
                    self.ikb(text="⏹ Durdur", callback_data=f"controls stop {chat_id}"),
                    self.ikb(text="🗑 Kapat", callback_data="close"),
                ],
            ]
        )

    def close_key(self) -> types.InlineKeyboardMarkup:
        # Tek tıkla kapatma butonu
        return self.ikm([[self.ikb(text="🗑 Kapat", callback_data="close")]])
