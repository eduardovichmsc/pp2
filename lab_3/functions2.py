movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

# Task 1
def movie_five(title):
  for movie in movies:
    if movie.get("name") == title and int(movie.get("imdb")) >= 5.5:
      return True
  return False

# print(movie_five("We Two"))
# print(movie_five("Exam"))

# Task 2
def above_5():
  temp = []
  for movie in movies:
    if int(movie.get("imdb")) >= 5.5:
      temp.append(movie)
  return temp
    
array1 = above_5()
# print(array1)

# Task 3
def get_titles_by_category(category):
  temp = []
  for movie in movies:
    if str(movie.get("category")).lower() == str(category).lower():
      temp.append(movie)
  return temp

categorized_movies = get_titles_by_category("Romance")
# print(categorized_movies)

# Task 4
def calculate_avg():
  sum = 0
  counter = 0
  for movie in movies:
    sum += int(movie.get("imdb"))
    counter += 1
  return sum // counter 

# print(calculate_avg())

# Task 5
def avg_by_category(category):
  sum = 0
  counter = 0
  for movie in movies:
    if str(movie.get("category")).lower() == str(category).lower():
      sum += movie.get("imdb")
      counter += 1
  return sum // counter 
# print(avg_by_category("Suspense"))