import google.generativeai as genai
import os

def get_car_ai_bio(model, brand, year):
    prompt = f'''me mostre uma descrição de venda para o carro {brand} {model} {year} em apenas 
    200 caracteres. Descreva especificações técnicas desse modelo de carro.'''
    genai.configure(api_key=os.environ["API_GEMINI"])
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text
  

