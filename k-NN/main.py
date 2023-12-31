# 50 yoshli erkak uchun sistolik qon bosim   120 mm - 140 mm simob ustuni bo'lsa normal
# diastolik 80 - 90  mm simob ustuni normal hisoblandi
# yurak urishlar soni 80 - 100  ta
# 1 - kasallik yo'q
# 0 - kasallik bor

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier


# Ma'lumotlarni olish
data_set = pd.read_csv('data.csv')
X = data_set.iloc[:, [1, 2, 3]].values
Y = data_set.iloc[:, -1].values

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X, Y)


sistolik = data_set.iloc[:, [1]].values
yurak = data_set.iloc[:, [3]].values

# Joriy nuqtalarni chizish
plt.scatter(sistolik, yurak, color='red', s=60, label='Joriy nuqtalar')

# Boshorat qiymatini kiritish
predict_value = tuple(map(int, input("Bashorat qiymatlarni kiriting: ").split()))

# KNN modeli orqali natijani hisoblash
y_pred = knn.predict([predict_value])

# Boshorat nuqtasini chizish
plt.scatter(predict_value[0], predict_value[2], color='blue', s=60, label='Boshorat nuqtasi')

# Grafik so'rovnoma va o'zgaruvchilarni hisoblash
plt.title("k-NN")
plt.xlabel("Sistolik qon bosimi")
plt.ylabel("Yurak urishlar soni")
plt.legend()

plt.show()

print("Natija:", y_pred)




# # Decision Tree modeli
# decision_tree = DecisionTreeClassifier()
# decision_tree.fit(X, Y)

# sistolik = data_set.iloc[:, [1]].values
# yurak = data_set.iloc[:, [3]].values

# # Joriy nuqtalarni chizish
# plt.scatter(sistolik, yurak, color='red', s=60, label='Joriy nuqtalar')

# # Boshorat qiymatini kiritish
# predict_value = tuple(map(int, input("Bashorat qiymatlarni kiriting: ").split()))

# # Decision Tree modeli orqali natijani hisoblash
# y_pred = decision_tree.predict([predict_value])

# # Boshorat nuqtasini chizish
# plt.scatter(predict_value[0], predict_value[2], color='blue', s=60, label='Boshorat nuqtasi')


# plt.title("Decision Tree")
# plt.xlabel("Sistolik qon bosimi")
# plt.ylabel("Yurak urishlar soni")
# plt.legend()

# plt.show()

# print("Natija:", y_pred)






# def euclidean_distance(point1, point2):
#     return math.sqrt(sum((a - b) ** 2 for a, b in zip(point1, point2)))

# # K-nearest neighbors algoritmi
# def k_nearest_neighbors(data, labels, k, new_point):
#     # Yangi nuqta va ma'lumotlar orasidagi masofalarni hisoblash
#     distances = [(euclidean_distance(new_point, data_point), label) for data_point, label in zip(data, labels)]
    
#     # Masofalarni katta dan kichik guruhlash va k eng yaqin masofali nuqtalarni aniqlash
#     sorted_distances = sorted(distances, key=lambda x: x[0])
#     k_nearest_labels = [label for distance, label in sorted_distances[:k]]
    
#     # K eng yaqin masofali nuqtalarning ko'rsatkichi bo'yicha aniqlik hisoblash
#     return max(set(k_nearest_labels), key=k_nearest_labels.count)

# # Ma'lumotlarni olish
# data_set = pd.read_csv('data.csv')
# X = data_set.iloc[:, [1, 2, 3]].values
# Y = data_set.iloc[:, -1].values

# # Asosiy ma'lumotlar
# sistolik = data_set.iloc[:, [1]].values
# yurak = data_set.iloc[:, [3]].values

# # Joriy nuqtalarni chizish
# for i in range(len(sistolik)):
#     plt.scatter(sistolik[i], yurak[i], color='red', s=60)

# # Boshorat qiymatini kiritish
# predict_value = tuple(map(int, input("Bashorat qiymatlarni kiriting: ").split()))

# # kNN algoritmi orqali natijani hisoblash
# y_pred = k_nearest_neighbors(X, Y, 3, predict_value)

# # Boshorat nuqtasini chizish
# plt.scatter(predict_value[0], predict_value[2], color='blue', s=60)

# # Grafik so'rovnoma va o'zgaruvchilarni hisoblash
# plt.title("k-NN")
# plt.xlabel("Sistolik qon bosimi")
# plt.ylabel("Yurak urishlar soni")

# # Nuqtalarni chizishni ko'rsatish
# plt.show()

# # Natija ekranga chiqarish
# print("Natija:", y_pred)

