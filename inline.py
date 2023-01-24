from html import escape
from uuid import uuid4

from telegram import InlineQueryResultArticle, InputTextMessageContent, Update
from telegram.constants import ParseMode
from telegram.ext import Application, CommandHandler, ContextTypes, InlineQueryHandler


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    """Send a message when the command /start is issued."""

    await update.message.reply_text("Hi!")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    """Send a message when the command /help is issued."""

    await update.message.reply_text("Help!")


async def inline_query(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    """Handle the inline query. This is run when you type: @botusername <query>"""

    query = update.inline_query.query

    if query == "":
        return
    results = [
        InlineQueryResultArticle(
            id=str(uuid4()),
            title="Caps",
            input_message_content=InputTextMessageContent(query.upper()),
        ),
        InlineQueryResultArticle(
            id=str(uuid4()),
            title="Bold",
            input_message_content=InputTextMessageContent(
                f"<b>{escape(query)}</b>", parse_mode=ParseMode.HTML
            ),
        ),
        InlineQueryResultArticle(
            id=str(uuid4()),
            title="Italic",
            input_message_content=InputTextMessageContent(
                f"<i>{escape(query)}</i>", parse_mode=ParseMode.HTML
            ),
        ),

    ]

    await update.inline_query.answer(results)


def main() -> None:

    application = Application.builder().token("5519492104:AAHqshbIG-CmFdl6UDLSRqJWi4XtLvriaCw").build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(InlineQueryHandler(inline_query))
    # Run the bot until the user presses Ctrl-C

    application.run_polling()


async def inline_caps(self, update, context):
    """Handle the inline query. This is run when you type: @botusername <query>"""
    query = update.inline_query.query
    if not query:
        return
    results = [InlineQueryResultArticle(
        id=query.upper(),
        title='Caps',
        input_message_content=InputTextMessageContent(query.upper())
    ), InlineQueryResultArticle(
        id=str(uuid4()),
        title="Bold",
        input_message_content=InputTextMessageContent(
            f"<b>{escape(query)}</b>", parse_mode=ParseMode.HTML
        ),
    ), InlineQueryResultArticle(
        id=str(uuid4()),
        title="Italic",
        input_message_content=InputTextMessageContent(
            f"<i>{escape(query)}</i>", parse_mode=ParseMode.HTML
        ),
    )]
    await context.bot.answer_inline_query(update.inline_query.id, results)


if __name__ == "__main__":
    main()