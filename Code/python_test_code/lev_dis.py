from sklearn.feature_extraction.text import TfidfVectorizer
from fuzzywuzzy import fuzz

def levenshtein_similarity(a, b):
  """Calculates the similarity between two strings using the Levenshtein distance.

  Args:
    a: The first string.
    b: The second string.

  Returns:
    The similarity between the two strings, as a ratio between 0 and 1.
  """

  distance = levenshtein_distance(a, b)
  similarity = 1 - distance / max(len(a), len(b))
  return similarity


def levenshtein_distance(a, b):
  """Calculates the Levenshtein distance between two strings.

  Args:
    a: The first string.
    b: The second string.

  Returns:
    The Levenshtein distance between the two strings.
  """

  n, m = len(a), len(b)
  d = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

  for i in range(n + 1):
    for j in range(m + 1):
      if i == 0:
        d[i][j] = j
      elif j == 0:
        d[i][j] = i
      else:
        if a[i - 1] == b[j - 1]:
          d[i][j] = d[i - 1][j - 1]
        else:
          d[i][j] = min(d[i - 1][j] + 1, d[i][j - 1] + 1, d[i - 1][j - 1] + 1)

  return d[n][m]

# Example usage

a = "implementasi algoritma winnowing untuk deteksi kemiripan judul skripsi".lower()
b = "Implementasi algoritma tf-idf dan fuzzy matching untuk deteksi kemiripan judul skripsi (studi kasus: prodi teknik informatika iib darmajaya)".lower()

tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform([a, b])
query_vector = tfidf_vectorizer.transform([b])
tfidf_scores = (query_vector * tfidf_matrix.T).A[0]

fuzzyWuzzy = fuzz.token_set_ratio(a, b)

distance = levenshtein_similarity(a, b)

print(tfidf_scores[0] * (distance))
print(tfidf_scores[0] * (fuzzyWuzzy / 100))
print(fuzzyWuzzy / 100)
print(distance)