from proj07 import calc_similarity_scores, num_in_common_between_lists

network=[[1, 2, 3], [0, 4, 6, 7, 9], [0, 3, 6, 8, 9], [0, 2, 8, 9], [1, 6, 7, 8], [9], [1, 2, 4, 8], [1, 4, 8], [2, 3, 4, 6, 7], [1, 2, 3, 5]]
similarity_matrix = calc_similarity_scores(network)
print("similarity matrix")
print(similarity_matrix)
print(20*"-")
print("similarity matrix printed nicely:")
for i, L in enumerate(similarity_matrix):
    print(i,":",L)
