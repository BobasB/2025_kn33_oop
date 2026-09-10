# Лабораторна робота 7. AI Агенти з Google ADK

- вручну потрібно буде внести у проект наступну частину у файл pyproject.toml:
```
requires-python = ">=3.13,<4.0"
```
Починаємо створювати проект та агента. Встановлюємо Google ADK:
```
poetry init
poetry add google-adk

eval $(poetry env activate)
adk --help

adk create cat

adk run cat
```
- Агент має запуститись і ми можемо задавати йому питання.
- не забувайте додати файли в .gitignore, щоб не пушити зайві файли в репозиторій

