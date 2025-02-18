file1 = "History is the systematic study of the past"
file2 = "History is the systematic study of the past this is just for practice"
def jaccard_simularity(text1,text2):
  set1 = set(text1.split())
  set2 = set(text2.split())

  intersection = set1.intersection(set2)
  union = set1.union(set2)
  similarity = len(intersection) / len (union)
  return similarity, intersection

similarity,common_words=jaccard_simularity(file1,file2)
print(f"similality {similarity:.2f}")
print("common words",common_words)
