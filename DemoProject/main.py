#Dataframe la du lieu duoc trinh bay nhu file diabetes.csv, la mot mang 2 chieu
#Series la mang 1 chieu, tuc la 1 dataframe co nhieu dong 1 cot

import pandas as pd

df = pd.read_csv('diabetes.csv')    #tra ve 1 dataframe co tat ca hang va cot trong file
#mac dinh lay cac gia tri cua hang dau tien lam ten cot
#Tu hang thu 2 cua excel, dc tinh la hang 0 trong dataframe

data = df.head() #default trả về dataframe co 5 rows dau tien,
data2 = data['Glucose'] #ta co trong data co 5 rows, day la cach access 1 col cua dataframe
#no tra ve 1 series co 5 phan tu trong cot Glucose

data3 = df[['Insulin', 'BMI']].tail(6) #trả về dataframe co 6 rows cuoi cung va 2 cot
#Khi co 2 cot tro len, no thanh mang 2 chieu (tuc la dataframe) nen moi co 2 dau []

data4 = df[['Age', 'Outcome']][3:5] #dataframe tu hang 3 den 5-1 (dem tu 0)
#[:10] tu dau den hang 9

data5 = df[df['Age'] < 30] #df['Age'] < 30: tra ve 1 series [False, False, False,..False, True]
#data5 se la 1 dataframe con cua df sau khi da loai bo false row

#Luu y: data.Glucose = data['Glucose']

print(df)

#muốn có 1 model, trước tiên phải tạo model (tạo object), sau đó train/learn (method .fit(X, Y))
#VD:
# from sklearn.neighbors import KNeighborsRegressor
# model = KNeighborsRegressor()
# model.fit(X, Y)
# model.predict(X)

#Preprocessing: X ->|transform| -> |Model|: X sau khi transform mới đưa vào model (tiền xử lý)
# from sklearn.preprocessing import StandardScaler
# X_new = StandardScaler().fit_transform(X)     -> Trả về mảng 2 chiều numpy, method này tính toán
# các tham số cần thiết (như tính độ lệch chuẩn, trung bình) và chuẩn hóa dữ liệu (để độ lệch chuẩn = 1 và mean =0

