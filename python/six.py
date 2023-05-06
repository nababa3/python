import page = requests.get("https://drive.google.com/open?id=1nf9WMDjZWIUnlnKyz7qomEYDdtWfW1Uf")
import soup = BeautifukSoup(page.content,'html.parser')
# Calculating the frequencies of dress colors
dress_colors_freq = {}
for color in dress_colors:  
    if color in dress_colors_freq:
        dress_colors_freq[color] +=1
    else:
        dress_colors_freq[color] = 1
# saving dress colors and thier frqeuncies to psodtgresql database
conn = psycopg2.connect("dbname=your_db_name user=your_username password=your_password host=your_host")
cur = conn.cursor()
for color, freq in dress_colors_freq.items():
    cur.execute("INSERT INTO dress_colors (color, frequency) VALUES (%s, %s)", (color, freq))
    conn.commit()
    cur.close()
    conn.close