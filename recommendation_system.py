import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import MinMaxScaler

# Dataset 50 Film
data = {
    "title": [
        # Superhero (0)
        "The Avengers", "Guardians of the Galaxy", "Iron Man", "Thor: Ragnarok", "Black Panther",
        "Spider-Man: Homecoming", "Wonder Woman", "The Dark Knight", "Captain America: Civil War", "Doctor Strange",
        # Animation (1)
        "Toy Story 3", "The Lion King", "Frozen", "The Incredibles", "Up",
        "Finding Nemo", "Shrek", "Zootopia", "Coco", "How to Train Your Dragon",
        "Inside Out", "Moana", "Kung Fu Panda", "Ratatouille", "Wall-E",
        # Romance (2)
        "La La Land", "The Notebook", "The Fault in Our Stars", "Titanic", "Pride and Prejudice",
        "Crazy, Stupid, Love", "The Shape of Water", "A Star is Born", "500 Days of Summer", "The Vow",
        "Me Before You", "The Proposal", "Notting Hill", "The Time Traveler's Wife", "Eternal Sunshine of the Spotless Mind",
        # Horror (3)
        "Get Out", "The Conjuring", "A Quiet Place", "The Exorcist", "Hereditary",
        "The Babadook", "It", "The Shining", "A Nightmare on Elm Street", "The Ring"
    ],
    "Genre": [
        # Superhero (0)
        0, 0, 0, 0, 0,
        0, 0, 0, 0, 0,
        # Animation (1)
        1, 1, 1, 1, 1,
        1, 1, 1, 1, 1,
        1, 1, 1, 1, 1,
        # Romance (2)
        2, 2, 2, 2, 2,
        2, 2, 2, 2, 2,
        2, 2, 2, 2, 2,
        # Horror (3)
        3, 3, 3, 3, 3,
        3, 3, 3, 3, 3
    ],
    "Rating": [
        # Superhero (0)
        8.0, 8.0, 7.9, 7.9, 7.3,
        7.4, 7.4, 9.0, 7.8, 7.5,
        # Animation (1)
        8.3, 8.5, 7.4, 8.0, 8.2,
        8.1, 7.8, 8.0, 8.4, 8.1,
        8.1, 7.6, 7.6, 8.0, 8.4,
        # Romance (2)
        8.0, 7.8, 7.7, 7.8, 7.8,
        7.4, 7.3, 7.6, 7.7, 6.7,
        7.4, 6.7, 7.0, 7.1, 8.3,
        # Horror (3)
        7.7, 7.5, 7.5, 8.0, 7.3,
        6.8, 7.3, 8.4, 7.4, 7.1
    ],
    "Duration": [
        # Superhero (0)
        143, 121, 126, 130, 134,
        133, 141, 152, 147, 115,
        # Animation (1)
        103, 88, 102, 115, 96,
        100, 90, 108, 105, 98,
        95, 107, 92, 111, 98,
        # Romance (2)
        128, 123, 126, 195, 129,
        118, 123, 136, 95, 104,
        110, 108, 124, 107, 108,
        # Horror (3)
        104, 112, 90, 122, 127,
        93, 135, 146, 91, 115
    ]
}

# Membuat Dataframe
df = pd.DataFrame(data)

# Menentukan atribut yang digunakan (genre, rating, durasi)
features = df[['Genre', 'Rating', 'Duration']] 

# Meningkatkan relevansi atribut genre (data dikalikan dengan tiga)
features['Genre'] = features['Genre'] * 3

scaler = MinMaxScaler()  # Normalisasi dengan MinMax
scaled_features = scaler.fit_transform(features)

# Meng-setup Nearest Neighbour
nn = NearestNeighbors(n_neighbors=6, metric='manhattan')  # Menggunakan teknik Manhattan Distance
nn.fit(scaled_features)

# Input User
print("🎬 Selamat datang dalam Sistem Rekomendasi Film! 🎬")
input("Sebutkan film yang sudah kamu tonton:")

# Validasi Input User
def get_valid_input(prompt, input_type, valid_range=None):
    while True:
        try:
            user_input = input_type(input(prompt))
            if valid_range and user_input not in valid_range:
                print(f"Input Invalid. Tolong masukkan input dalam rentang {valid_range}.")
                continue
            return user_input
        except ValueError:
            print("Input Invalid. Tolong masukkan Input yang valid.")

genre = get_valid_input(
    "Genre (Superhero=0, Animasi=1, Romance=2, Horror=3): ",
    int,
    valid_range=[0, 1, 2, 3]
)
rating = get_valid_input(
    "Rating (1-10): ",
    float
)
duration = get_valid_input(
    "Durasi (dalam menit): ",
    int
)

# Meningkatkan relevansi atribut genre (dikalikan dengan 3)
user_input = [genre * 3, rating, duration]
scaled_user_input = scaler.transform([user_input])

# Menemukan neighbor terdekat
distances, indices = nn.kneighbors(scaled_user_input)

# Output Rekomendasi 5 film terbaik
print("\n🌟 Ini adalah TOP 5 rekomendasi film yang harus kamu tonton! 🌟")
print("=============================================")
for i, idx in enumerate(indices[0][0:5]):
    movie = df.iloc[idx]
    print(f"\n🎥 Rekomendasi #{i + 1}:")
    print(f"   Judul: {movie['title']}")
    print(f"   Genre: {['Superhero', 'Animasi', 'Romance', 'Horror'][movie['Genre']]}")
    print(f"   Rating: {movie['Rating']}")
    print(f"   Durasi: {movie['Duration']} minutes")
print("\n=============================================")
print("Selamat Marathon! 🍿🎉")