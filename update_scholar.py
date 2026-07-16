import json
from scholarly import scholarly

# 1. REEMPLAZA ESTO CON TU ID DE GOOGLE SCHOLAR
# Lo encuentras en la URL de tu perfil (ej: https://scholar.google.com/citations?user=HJmXv08AAAAJ -> el ID es HJmXv08AAAAJ)
SCHOLAR_ID = "b7nyrXIAAAAJ"

# 2. Escribe tu nombre tal cual aparece en tus papers para que el script lo ponga en negrita automáticamente
MY_NAME = "Guillaume Jeanneret" 
MY_NAME2 = "Sanmiguel" 

def update_publications():
    try:
        print("Connecting to Google Scholar...")
        author = scholarly.search_author_id(SCHOLAR_ID)
        
        print(f"Author found: {author.get('name')}. Fetching publications list...")
        author = scholarly.fill(author, sections=['publications'], sortby='year')
        
        # ⚠️ PRO TIP: Limitamos a los primeros 12 artículos. 
        # Si intentas rellenar 50 artículos de golpe, Google te bloqueará por detectar tráfico bot.
        all_publications = author.get('publications', [])[:20]
        
        publications = []
        for index, pub in enumerate(all_publications):
            print(f"[{index+1}/{len(all_publications)}] Fetching deep details for: {pub.get('bib', {}).get('title')[:30]}...")
            
            # ✨ LA LÍNEA MÁGICA QUE FALTABA:
            # Esto obliga al script a descargar los autores, journal/conferencia completos.
            pub_filled = scholarly.fill(pub)
            
            bib = pub_filled.get('bib', {})
            title = bib.get('title', 'Untitled Paper')
            authors = bib.get('author', 'Unknown Authors')
            venue = bib.get('journal', bib.get('conference', bib.get('venue', 'N/A')))
            year = bib.get('pub_year', 'N/A')
            pub_url = pub_filled.get('pub_url', '#')
            
            # Ponemos tu nombre en negrita automáticamente
            formatted_authors = authors.replace(MY_NAME, f"<strong>{MY_NAME}</strong>").replace(MY_NAME2, f"<strong>{MY_NAME2}</strong>").replace(' and ', ', ')
            
            publications.append({
                "title": title,
                "authors": formatted_authors,
                "venue": f"{venue}, {year}" if year != 'N/A' else venue,
                "pdf": pub_url
            })
            
        # Guardamos en el archivo JSON
        with open('publications.json', 'w', encoding='utf-8') as f:
            json.dump(publications, f, indent=2, ensure_ascii=False)
            
        print("\nSuccess! Your publications.json is now complete with authors and venues.")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    update_publications()