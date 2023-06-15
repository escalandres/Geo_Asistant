# import wikipediaapi
# # Crear un objeto de la API de Wikipedia
# wiki_wiki = wikipediaapi.Wikipedia('es')

# # Buscar un mineral y obtener su página
# mineral = input("Ingrese el nombre del mineral: ")
# page = wiki_wiki.page(mineral)

# if page.exists():
#     # Obtener el contenido del resumen del mineral
#     resumen = page.summary
#     print("Resumen:")
#     print(resumen)
# else:
#     print("No se encontró información sobre el mineral.")
import wolframalpha
app_id = "RGKTU7-VYTGGTHK2Y"
client = wolframalpha.Client(app_id)
person = "what platino is?"
wolfram_res = next(client.query(person).results).text
print(wolfram_res)