from main import main

def lambda_handler(event, context):
   print("Ми запустили лямбда-функцію!")
   main()
   print("Ми завершили виконання лямбда-функції!")
