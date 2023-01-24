from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes


class QueBot:
    def __init__(self, items, text, chosen_text):
        self.items = items
        self.text = text
        self.chosen_text = chosen_text
        self.current_list = []

    async def questionnaire(self, update, context):
        await self.clear(update, context)
        await update.message.reply_text(self.text, reply_markup=self.build_que())

    def build_que(self, current_list=None) -> InlineKeyboardMarkup:
        """Helper function to build the next inline keyboard."""
        if current_list is None:
            current_list = []

        items_diff = list(set(self.items).difference(set(current_list)))
        self.current_list = current_list
        return InlineKeyboardMarkup.from_column(
            [InlineKeyboardButton(i, callback_data=i) for i in items_diff]
        )

    async def clear(self, update, context):
        context.bot.callback_data_cache.clear_callback_data()
        context.bot.callback_data_cache.clear_callback_queries()

    async def clear_with_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Clears the callback data cache"""
        await self.clear(update, context)
        await update.effective_message.reply_text("All clear!")

    async def list_button(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Parses the CallbackQuery and updates the message text."""
        query = update.callback_query
        await query.answer()

        item = query.data
        item_list = self.current_list

        item_list.append(item)

        list_text = ", ".join(item_list)
        await query.edit_message_text(
            text=f"{self.chosen_text}: {list_text}. Choose the next.",
            reply_markup=self.build_que(item_list),
        )

    async def handle_invalid_button(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Informs the user that the button is no longer available."""
        await update.callback_query.answer()
        await update.effective_message.edit_text(
            "Sorry, I could not process this button click 😕 Please send /start to get a new keyboard."
        )