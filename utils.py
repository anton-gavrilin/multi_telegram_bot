from telegram import Update
from telegram.ext import ContextTypes


class Notifier:
    def __init__(self, text, update: Update):
        self.text = text
        self.update = update

    async def alert_message(self, context: ContextTypes.DEFAULT_TYPE):
        await context.bot.send_message(text=self.text, chat_id=self.update.effective_chat.id)


def get_week_day(day: str):
    day = day.lower().strip()
    if day == "monday":
        return 1
    elif day == "tuesday":
        return 2
    elif day == "wednesday":
        return 3
    elif day == "thursday":
        return 4
    elif day == "friday":
        return 5
    elif day == "saturday":
        return 6
    elif day == "sunday":
        return 0