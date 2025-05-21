from utlies import *


#100lb 6 h

x_train, x_test, y_train, y_test = train_test_split(x1, y1, test_size=0.2, random_state=42)


model = LinearRegression()

model.fit(x_train, y_train)


y_pred = model.predict(x_test)


#200lb 6 h 

x_train2, x_test2, y_train2, y_test2 = train_test_split(x2, y2, test_size=0.2, random_state=42)

model2 =  LinearRegression()

model2.fit(x_train2, y_train2)

y_pred2 = model.predict(x_test2)

# 300lb 6 h 

x_train3, x_test3, y_train3, y_test3 = train_test_split(x3, y3, test_size=0.2, random_state=42)


model3 = LinearRegression()

model3.fit(x_train3,y_train3)

y_pred3 = model.predict(x_test3)

# 100lb 5.6 h - 5.11 h 

x_train1_1, x_test1_1, y_train1_1, y_test1_1 = train_test_split(x1_1, y1_1, test_size=0.2, random_state=42)


model1_1 = LinearRegression()

model1_1.fit(x_train1_1,y_train1_1)

pred1_1 = model1_1.predict(x_test1_1)

# 200lb 5.6 h - 5.11 h 

x_train1_2, x_test1_2, y_train1_2, y_test1_2 = train_test_split(x1_2, y1_2, test_size=0.2, random_state=42)


model1_2 = LinearRegression()

model1_2.fit(x_train1_2,y_train1_2)

pred1_2 = model1_2.predict(x_test1_2)

# 300lb 5.6h - 5.11 h 

x_train1_3, x_test1_3, y_train1_3, y_test1_3 = train_test_split(x1_3, y1_3, test_size=0.2, random_state=42)

model1_3 = LinearRegression()

model1_3.fit(x_train1_3,y_train1_3)

pred1_3 = model1_3.predict(x_test1_3)

# 100lb 5.5 or less 

x_train2_1, x_test2_1, y_train2_1, y_test2_1 = train_test_split(x2_1, y2_1, test_size=0.2, random_state=42)

model2_1 = LinearRegression()

model2_1.fit(x_train2_1,y_train2_1)

pred2_1 = model2_1.predict(x_test2_1)

# 200lb 5.5 or less 

x_train2_2, x_test2_2, y_train2_2, y_test2_2 = train_test_split(x2_2, y2_2, test_size=0.2, random_state=42)


model2_2 = LinearRegression()

model2_2.fit(x_train2_2,y_train2_2)

pred2_2 = model2_2.predict(x_test2_2)

# 300lb 5.5 or less 

x_train2_3, x_test2_3, y_train2_3, y_test2_3 = train_test_split(x2_3, y2_3, test_size=0.2, random_state=42)


model2_3 = LinearRegression()

model2_3.fit(x_train2_3,y_train2_3)

pred2_3 = model2_3.predict(x_test2_3)


