import logging
from unittest import runner
from dotenv import load_dotenv
import os

from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

from agent import root_agent

from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

# Load environment variables from .env file
load_dotenv()


# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)

SESSION_RUNNER: dict[str, Runner] = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )

# Session and Runner
async def setup_session_and_runner(app_name: str, user_id: str, session_id: str):
    """Ця функція створює сесію та Runner для агента."""
    session_service = InMemorySessionService()
    session = await session_service.create_session(app_name=app_name, user_id=user_id, session_id=session_id)
    runner = Runner(agent=root_agent, app_name=app_name, session_service=session_service)
    return session, runner


async def reply_from_ai_agent(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = str(update.message.text)
    user = str(update.message.from_user.username)
    session_id = str(update.message.chat_id)
    logger.info(f"Отримано повідомлення: {text} | Користувач: {user} | Чат: {session_id}")
    content = types.Content(role='user', parts=[
        types.Part(text=f"Користувач: {user} задає наступне запитання: "), 
        types.Part(text=text)]
        )
    if session_id not in SESSION_RUNNER.keys():
        _, runner = await setup_session_and_runner(
            app_name="telegram_bot",
            user_id=user,
            session_id=session_id
        )
        SESSION_RUNNER[session_id] = runner
        logger.info(f"Створено нову сесію та Runner для чату {session_id}")
    else:
        runner = SESSION_RUNNER[session_id]
        logger.info(f"Знайдено існуючу сесію та Runner для чату {session_id}")
    
    events = runner.run_async(user_id=user, session_id=session_id, new_message=content)

    async for event in events:

        if event.is_final_response():

            final_response = event.content.parts[0].text

            logger.info("Agent Response: %s", final_response)

            await update.message.reply_text(final_response)

def main():
    token = os.getenv("TOKEN")
    logger.info("Hello, Telegram Bot!")
    application = Application.builder().token(token).build()
    logger.info(f"Bot started successfully")
    # on different commands - answer in Telegram
    
    application.add_handler(CommandHandler("start", start))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_from_ai_agent))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()