from google.adk.agents.llm_agent import Agent
from datetime import datetime
from google.adk.tools.tool_context import ToolContext

def get_current_datetime() -> dict:
    """
    Інструмент для визначення поточної дати та часу.
    Повертає словник з поточною датою та часом у форматі "YYYY-MM-DD HH:MM:SS".
    """
    return {"status": "success", "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

def save_user_preferences(tool_context: ToolContext, preferences: dict) -> dict:
    """
    Інструмент для збереження уподобань користувача.
    Приймає словник з уподобаннями та зберігає їх у базі даних (симуляція).
    Повертає словник з результатом операції.
    args:
    - tool_context: Контекст інструменту, який може містити інформацію про користувача та інші дані.
    - preferences: Словник з уподобаннями користувача, який потрібно зберегти.
    """
    # Симуляція збереження в базі даних
    # У реальному застосуванні тут буде код для взаємодії з базою даних
    for preference_type, value in preferences.items():
        existing_state = tool_context.state.get(preference_type, [])
        tool_context.state[preference_type] = existing_state + [value]
        print(f"[Оновлено конфігурацію {preference_type}] {value}")
    return {"status": "success", "message": "Уподобання користувача збережено."}

def get_user_preferences(tool_context: ToolContext, preference_type: str) -> dict:
    """
    Інструмент для отримання уподобань користувача.
    Повертає словник з уподобаннями користувача, які зберігаються в контексті інструменту.
    args:
    - tool_context: Контекст інструменту, який може містити інформацію про користувача та інші дані.
    - preference_type: Тип уподобань, які потрібно отримати (наприклад, "learning_preferences").
    returns:
    - status: Статус операції (успіх або помилка).
    - preferences: Словник з уподобаннями користувача, які зберіються в контексті інструменту.
    """
    preferences = tool_context.state.get(preference_type, [])
    return {"status": "success", "preferences": preferences}

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='АІ агент для допомоги групі КН-33',
    instruction="""
Ти - АІ агент для допомоги групі КН-33. 
Твоє завдання - відповідати на запитання студентів українською мовою та допомагати їм з навчанням. 
Відповідай на запитання чітко та зрозуміло. Паямтай що відповіді надсилаються в месенджкер Telegram, тому будь лаконічним, повідомлення мають бути короткими та інформативними. Не більше 200 слів.
Використовуй скуфську лексику та завжди в кінці пиши - "З повагою, твій АІ помічник".
Кожне повідомлення буде містити імя користувача який до тебе звертається, тому завжди звертайся до нього по імені.
### Використання інструментів:
- `get_current_datetime`: для визначення поточної дати та часу.
- `save_user_preferences`: для збереження уподобань або корисної інформації про користувача.
- `get_user_preferences`: для отримання уподобань або корисної інформації про користувача.
""",
    tools=[get_current_datetime, save_user_preferences, get_user_preferences]
)
