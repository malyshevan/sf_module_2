#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import datetime
import os
import collections


# In[2]:


data = pd.read_csv('data.csv')
data.head(5)


# In[3]:


len(data)


# # Предобработка датасета

# In[4]:


answer_ls = [] # создадим список с ответами. сюда будем добавлять ответы по мере прохождения теста
# сюда можем вписать создание новых колонок в датасете


# # 1. У какого фильма из списка самый большой бюджет?
# Варианты ответов:
# 1. The Dark Knight Rises (tt1345836)
# 2. Spider-Man 3 (tt0413300)
# 3. Avengers: Age of Ultron (tt2395427)
# 4. The Warrior's Way	(tt1032751)
# 5. Pirates of the Caribbean: On Stranger Tides (tt1298650)

# In[5]:


# тут вводим ваш ответ и добавлем в его список ответов (сейчас для примера стоит "1")
max_budget = data['budget'].idxmax()
data.iloc[max_budget]
answer_ls.append(4)


# # 2. Какой из фильмов самый длительный (в минутах)
# 1. The Lord of the Rings: The Return of the King	(tt0167260)
# 2. Gods and Generals	(tt0279111)
# 3. King Kong	(tt0360717)
# 4. Pearl Harbor	(tt0213149)
# 5. Alexander	(tt0346491)

# In[6]:


max_runtime = data['runtime'].idxmax()
data.iloc[max_runtime]
answer_ls.append(2)


# # 3. Какой из фильмов самый короткий (в минутах)
# Варианты ответов:
# 
# 1. Home on the Range	tt0299172
# 2. The Jungle Book 2	tt0283426
# 3. Winnie the Pooh	tt1449283
# 4. Corpse Bride	tt0121164
# 5. Hoodwinked!	tt0443536

# In[7]:


min_runtime = data['runtime'].idxmin()
data.iloc[min_runtime]
answer_ls.append(3)


# # 4. Средняя длительность фильма?
# 
# Варианты ответов:
# 1. 115
# 2. 110
# 3. 105
# 4. 120
# 5. 100
# 

# In[8]:


sum_runtime = round(data['runtime'].sum()/data['runtime'].count(),0)
answer_ls.append(2)


# # 5. Средняя длительность фильма по медиане?
# Варианты ответов:
# 1. 106
# 2. 112
# 3. 101
# 4. 120
# 5. 115
# 
# 
# 

# In[9]:


med = round(data['runtime'].median(),0)
answer_ls.append(1)


# # 6. Какой самый прибыльный фильм?
# Варианты ответов:
# 1. The Avengers	tt0848228
# 2. Minions	tt2293640
# 3. Star Wars: The Force Awakens	tt2488496
# 4. Furious 7	tt2820852
# 5. Avatar	tt0499549

# In[10]:


max_prib = (data['revenue'] - data['budget']).idxmax()
data.iloc[max_prib]
answer_ls.append(5)


# # 7. Какой фильм самый убыточный?
# Варианты ответов:
# 1. Supernova tt0134983
# 2. The Warrior's Way tt1032751
# 3. Flushed Away	tt0424095
# 4. The Adventures of Pluto Nash	tt0180052
# 5. The Lone Ranger	tt1210819

# In[11]:


min_prib = (data['revenue'] - data['budget']).idxmin()
data.iloc[min_prib]
answer_ls.append(2)


# # 8. Сколько всего фильмов в прибыли?
# Варианты ответов:
# 1. 1478
# 2. 1520
# 3. 1241
# 4. 1135
# 5. 1398
# 

# In[12]:


data['prib'] = (data['revenue'] - data['budget'])
data_1 = data['prib'] > 0
data['prib'].loc[data_1].count()
answer_ls.append(1)


# # 9. Самый прибыльный фильм в 2008 году?
# Варианты ответов:
# 1. Madagascar: Escape 2 Africa	tt0479952
# 2. Iron Man	tt0371746
# 3. Kung Fu Panda	tt0441773
# 4. The Dark Knight	tt0468569
# 5. Mamma Mia!	tt0795421

# In[13]:


data['prib'] = (data['revenue'] - data['budget'])
max_prib = data[data.release_year == 2008].prib.max()
more_2008 = data[(data.prib == max_prib)]
answer_ls.append(4)


# # 10. Самый убыточный фильм за период с 2012 по 2014 (включительно)?
# Варианты ответов:
# 1. Winter's Tale	tt1837709
# 2. Stolen	tt1656186
# 3. Broken City	tt1235522
# 4. Upside Down	tt1374992
# 5. The Lone Ranger	tt1210819
# 

# In[14]:


data['prib'] = (data['revenue'] - data['budget'])
min_prib = data[(data.release_year > 2012) & (data.release_year <= 2014)].prib.min()
min_prib_film = data[(data.prib == min_prib)]
min_prib_film
answer_ls.append(5)


# # 11. Какого жанра фильмов больше всего?
# Варианты ответов:
# 1. Action
# 2. Adventure
# 3. Drama
# 4. Comedy
# 5. Thriller

# In[15]:


res = []
for i in data.genres:
    str_1 = i.split('|')
    for b in str_1:
        res.append(b)
dict_1 = {b:res.count(b) for b in res}
dict_1
# print(sorted(dict_1.items(), key = lambda kv:(kv[1],kv[0])))
answer_ls.append(3)


# # 12. Какого жанра среди прибыльных фильмов больше всего?
# Варианты ответов:
# 1. Drama
# 2. Comedy
# 3. Action
# 4. Thriller
# 5. Adventure

# In[16]:


data = pd.read_csv('data.csv')
data.head(5)
data['col1']=data['genres'].str.split('|').str.get(0)
data_1 = data
data['col1']=data['genres'].str.split('|').str.get(1)
data_2 = data
data['col1']=data['genres'].str.split('|').str.get(2)
data_3 = data
data['col1']=data['genres'].str.split('|').str.get(3)
data_4 = data
data_itog = pd.concat([data_1, data_2,data_3,data_4])
data_itog_1 = data_itog.reset_index()
data_itog_1.drop('index', axis = 1)
data_itog_1['prib'] = (data_1['revenue'] - data_1['budget'])
data_itog_1.groupby('col1').sum().sort_values('prib',ascending=False)
answer_ls.append(4)


# # 13. Кто из режиссеров снял больше всего фильмов?
# Варианты ответов:
# 1. Steven Spielberg
# 2. Ridley Scott 
# 3. Steven Soderbergh
# 4. Christopher Nolan
# 5. Clint Eastwood

# In[17]:


data['prib'] = (data['revenue'] - data['budget'])
data_1 = data.director.value_counts(normalize = False).sort_values(ascending=False)
answer_ls.append(3)


# # 14. Кто из режиссеров снял больше всего Прибыльных фильмов?
# Варианты ответов:
# 1. Steven Soderbergh
# 2. Clint Eastwood
# 3. Steven Spielberg
# 4. Ridley Scott
# 5. Christopher Nolan

# In[18]:


data['prib'] = (data['revenue'] - data['budget'])
data_1 = data[data.prib > 0].director.value_counts(normalize = False).sort_values(ascending=False)
answer_ls.append(4)


# # 15. Кто из режиссеров принес больше всего прибыли?
# Варианты ответов:
# 1. Steven Spielberg
# 2. Christopher Nolan
# 3. David Yates
# 4. James Cameron
# 5. Peter Jackson
# 

# In[19]:


data['prib'] = data.revenue - data.budget
films = []
films.append(data[data.director.str.contains('Steven Spielberg', na=False)].prib.sum())
films.append(data[data.director.str.contains('Christopher Nolan', na=False)].prib.sum())
films.append(data[data.director.str.contains('David Yates', na=False)].prib.sum())
films.append(data[data.director.str.contains('James Cameron', na=False)].prib.sum())
films.append(data[data.director.str.contains('Peter Jackson', na=False)].prib.sum())
films
answer_ls.append(5)


# # 16. Какой актер принес больше всего прибыли?
# Варианты ответов:
# 1. Emma Watson
# 2. Johnny Depp
# 3. Michelle Rodriguez
# 4. Orlando Bloom
# 5. Rupert Grint

# In[20]:


data['prib'] = data.revenue - data.budget
films = []
films.append(data[data.cast.str.contains('Emma Watson', na=False)].prib.sum())
films.append(data[data.cast.str.contains('Johnny Depp', na=False)].prib.sum())
films.append(data[data.cast.str.contains('David Yates', na=False)].prib.sum())
films.append(data[data.cast.str.contains('Michelle Rodriguez', na=False)].prib.sum())
films.append(data[data.cast.str.contains('Rupert Grint', na=False)].prib.sum())
films
answer_ls.append(1)


# # 17. Какой актер принес меньше всего прибыли в 2012 году?
# Варианты ответов:
# 1. Nicolas Cage
# 2. Danny Huston
# 3. Kirsten Dunst
# 4. Jim Sturgess
# 5. Sami Gayle

# In[21]:


data['prib'] = data.revenue - data.budget
films = []
films.append(data[(data.cast.str.contains('Nicolas Cage', na=False))&(data.release_year == 2012)].prib.sum())
films.append(data[(data.cast.str.contains('Danny Huston', na=False))&(data.release_year == 2012)].prib.sum())
films.append(data[(data.cast.str.contains('Kirsten Dunst', na=False))&(data.release_year == 2012)].prib.sum())
films.append(data[(data.cast.str.contains('Jim Sturgess', na=False))&(data.release_year == 2012)].prib.sum())
films.append(data[(data.cast.str.contains('Sami Gayle', na=False))&(data.release_year == 2012)].prib.sum())
answer_ls.append(3)


# # 18. Какой актер снялся в большем количестве высокобюджетных фильмов? (в фильмах где бюджет выше среднего по данной выборке)
# Варианты ответов:
# 1. Tom Cruise
# 2. Mark Wahlberg 
# 3. Matt Damon
# 4. Angelina Jolie
# 5. Adam Sandler

# In[22]:


films = []
films.append(data[(data.cast.str.contains('Tom Cruise', na=False))&(data.budget > data.budget.mean())].original_title.count())
films.append(data[(data.cast.str.contains('Mark Wahlberg', na=False))&(data.budget > data.budget.mean())].original_title.count())
films.append(data[(data.cast.str.contains('Matt Damon', na=False))&(data.budget > data.budget.mean())].original_title.count())
films.append(data[(data.cast.str.contains('Angelina Jolie', na=False))&(data.budget > data.budget.mean())].original_title.count())
films.append(data[(data.cast.str.contains('Adam Sandler', na=False))&(data.budget > data.budget.mean())].original_title.count())
answer_ls.append(3)


# # 19. В фильмах какого жанра больше всего снимался Nicolas Cage?  
# Варианты ответа:
# 1. Drama
# 2. Action
# 3. Thriller
# 4. Adventure
# 5. Crime

# In[23]:


films = []
str_1 = 'Nicolas Cage'
films.append(data[(data.cast.str.contains(str_1, na=False))&(data.genres.str.contains('Drama', na=False))].original_title.count())
films.append(data[(data.cast.str.contains(str_1, na=False))&(data.genres.str.contains('Action', na=False))].original_title.count())
films.append(data[(data.cast.str.contains(str_1, na=False))&(data.genres.str.contains('Thriller', na=False))].original_title.count())
films.append(data[(data.cast.str.contains(str_1, na=False))&(data.genres.str.contains('Adventure', na=False))].original_title.count())
films.append(data[(data.cast.str.contains(str_1, na=False))&(data.genres.str.contains('Crime', na=False))].original_title.count())
answer_ls.append(2)


# # 20. Какая студия сняла больше всего фильмов?
# Варианты ответа:
# 1. Universal Pictures (Universal)
# 2. Paramount Pictures
# 3. Columbia Pictures
# 4. Warner Bros
# 5. Twentieth Century Fox Film Corporation

# In[24]:


c = {}
data['prib'] = data['revenue'] - data['budget']
companies = set(data.production_companies.str.split('|').sum())
for x in companies:
    c[x] = data[(data.production_companies.str.contains(x))].original_title.count()
print(sorted(c.items(), key = lambda kv:(kv[1],kv[0])))

answer_ls.append(1)


# # 21. Какая студия сняла больше всего фильмов в 2015 году?
# Варианты ответа:
# 1. Universal Pictures
# 2. Paramount Pictures
# 3. Columbia Pictures
# 4. Warner Bros
# 5. Twentieth Century Fox Film Corporation

# In[25]:


films = []
films.append(data[((data.production_companies.str.contains('Universal Pictures', na=False))&(data.release_year == 2015))].original_title.count())
films.append(data[((data.production_companies.str.contains('Paramount', na=False))&(data.release_year == 2015))].original_title.count())
films.append(data[((data.production_companies.str.contains('Columbia', na=False))&(data.release_year == 2015))].original_title.count())
films.append(data[((data.production_companies.str.contains('Warner Bros', na=False))&(data.release_year == 2015))].original_title.count())
films.append(data[((data.production_companies.str.contains('Twentieth', na=False))&(data.release_year == 2015))].original_title.count())
films
answer_ls.append(4)


# # 22. Какая студия заработала больше всего денег в жанре комедий за все время?
# Варианты ответа:
# 1. Warner Bros
# 2. Universal Pictures (Universal)
# 3. Columbia Pictures
# 4. Paramount Pictures
# 5. Walt Disney

# In[26]:


films = []
films.append(data[(data.production_companies.str.contains('Warner Bros', na=False))&(data.genres.str.contains('Comedy', na=False))].revenue.sum())
films.append(data[(data.production_companies.str.contains('Universal', na=False))&(data.genres.str.contains('Comedy', na=False))].revenue.sum())
films.append(data[(data.production_companies.str.contains('Columbia', na=False))&(data.genres.str.contains('Comedy', na=False))].revenue.sum())
films.append(data[(data.production_companies.str.contains('Warner Bros', na=False))&(data.genres.str.contains('Comedy', na=False))].revenue.sum())
films.append(data[(data.production_companies.str.contains('Walt Disney', na=False))&(data.genres.str.contains('Comedy', na=False))].revenue.sum())
films
answer_ls.append(2)


# # 23. Какая студия заработала больше всего денег в 2012 году?
# Варианты ответа:
# 1. Universal Pictures (Universal)
# 2. Warner Bros
# 3. Columbia Pictures
# 4. Paramount Pictures
# 5. Lucasfilm

# In[27]:


c = {}
data['prib'] = data['revenue'] - data['budget']
companies = set(data.production_companies.str.split('|').sum())
for x in companies:
    c[x] = data[(data.release_year == 2012)&(data.production_companies.str.contains(x))].prib.sum()
print(sorted(c.items(), key = lambda kv:(kv[1],kv[0])))
answer_ls.append(3)


# # 24. Самый убыточный фильм от Paramount Pictures
# Варианты ответа:
# 
# 1. K-19: The Widowmaker tt0267626
# 2. Next tt0435705
# 3. Twisted tt0315297
# 4. The Love Guru tt0811138
# 5. The Fighter tt0964517

# In[28]:


data['prib'] = data['revenue'] - data['budget']
companies = 'Paramount Pictures'
data[data.production_companies.str.contains(companies)].sort_values(by = 'prib')
answer_ls.append(1)


# # 25. Какой Самый прибыльный год (заработали больше всего)?
# Варианты ответа:
# 1. 2014
# 2. 2008
# 3. 2012
# 4. 2002
# 5. 2015

# In[29]:


c = {}
data['prib'] = data['revenue'] - data['budget']
year = set(data.release_year)
year
for x in year:
     c[x] = data[(data.release_year == x)].prib.sum()
c
answer_ls.append(5)


# # 26. Какой Самый прибыльный год для студии Warner Bros?
# Варианты ответа:
# 1. 2014
# 2. 2008
# 3. 2012
# 4. 2010
# 5. 2015

# In[30]:


c = {}
data['prib'] = data['revenue'] - data['budget']
year = set(data.release_year)
comp = 'Warner Bros'
year
for x in year:
     c[x] = data[(data.release_year == x)&(data.production_companies.str.contains(comp))].prib.sum()
print(sorted(c.items(), key = lambda kv:(kv[1],kv[0])))
answer_ls.append(1)


# # 27. В каком месяце за все годы суммарно вышло больше всего фильмов?
# Варианты ответа:
# 1. Январь
# 2. Июнь
# 3. Декабрь
# 4. Сентябрь
# 5. Май

# In[31]:


c = {}
data['month'] = data.release_date.str.split('/').str.get(0)
month_str = set(data.month)
for i in month_str:
    c[i] = data[(data.month == i)].original_title.count()
print(sorted(c.items(), key = lambda kv:(kv[1],kv[0])))
answer_ls.append(4)


# # 28. Сколько суммарно вышло фильмов летом? (за июнь, июль, август)
# Варианты ответа:
# 1. 345
# 2. 450
# 3. 478
# 4. 523
# 5. 381

# In[32]:


c = {}
data['month'] = data.release_date.str.split('/').str.get(0)
month_str = set(data.month)
for i in month_str:
    c[i] = data[(data.month == i)].original_title.count()
summer = c['6']+c['7']+c['8']
print(summer)
answer_ls.append(2)


# # 29. Какой режисер выпускает (суммарно по годам) больше всего фильмов зимой?
# Варианты ответов:
# 1. Steven Soderbergh
# 2. Christopher Nolan
# 3. Clint Eastwood
# 4. Ridley Scott
# 5. Peter Jackson

# In[33]:


c = {}
data['month'] = data.release_date.str.split('/').str.get(0)
month_str
director = set(data.director)
director
for i in director:
    c[i] = data[((data.month == '1')|(data.month == '2')|(data.month == '12'))&(data.director == i)].original_title.count()
print(sorted(c.items(), key = lambda kv:(kv[1],kv[0])))
answer_ls.append(5)


# # 30. Какой месяц чаще всего по годам самый прибыльный?
# Варианты ответа:
# 1. Январь
# 2. Июнь
# 3. Декабрь
# 4. Сентябрь
# 5. Май

# In[34]:


data_pivot = data.pivot_table(values='prib', columns=['month'], index=['release_year'], aggfunc = 'sum')
data_pivot
data_pivot.idxmax(axis = 1).value_counts()
answer_ls.append(2)


# # 31. Названия фильмов какой студии в среднем самые длинные по количеству символов?
# Варианты ответа:
# 1. Universal Pictures (Universal)
# 2. Warner Bros
# 3. Jim Henson Company, The
# 4. Paramount Pictures
# 5. Four By Two Productions

# In[35]:


c = {}
data['len_original_title'] = data.original_title.str.len()
data.len_original_title.unique()
company = ['Universal','Warner Bros','Jim Henson Company, The','Paramount Pictures','Four By Two Productions']
for i in company:
     c[i] = data[(data.production_companies.str.contains(i))].len_original_title.sum()/data[(data.production_companies.str.contains(i))].original_title.count()
print(sorted(c.items(), key = lambda kv:(kv[1],kv[0])))
answer_ls.append(5)


# # 32. Названия фильмов какой студии в среднем самые длинные по количеству слов?
# Варианты ответа:
# 1. Universal Pictures (Universal)
# 2. Warner Bros
# 3. Jim Henson Company, The
# 4. Paramount Pictures
# 5. Four By Two Productions

# In[36]:


c = {}
data['len_original_title_word'] = data['original_title'].str.count(' ') + 1
c = {}
data.len_original_title.unique()
company = ['Universal','Warner Bros','Jim Henson Company, The','Paramount Pictures','Four By Two Productions']
for i in company:
     c[i] = data[(data.production_companies.str.contains(i))].len_original_title_word.sum()/data[(data.production_companies.str.contains(i))].original_title.count()
print(sorted(c.items(), key = lambda kv:(kv[1],kv[0])))
answer_ls.append(5)


# # 33. Сколько разных слов используется в названиях фильмов?(без учета регистра)
# Варианты ответа:
# 1. 6540
# 2. 1002
# 3. 2461
# 4. 28304
# 5. 3432

# In[37]:


words = []
new_words = []
for i in data['original_title'].to_list():
    for j in i.lower().split():
        words.append(j)
for i in words:
    if i in new_words:
        continue
    else:
        new_words.append(i)
len(new_words)
answer_ls.append(3)


# # 34. Какие фильмы входят в 1 процент лучших по рейтингу?
# Варианты ответа:
# 1. Inside Out, Gone Girl, 12 Years a Slave
# 2. BloodRayne, The Adventures of Rocky & Bullwinkle
# 3. The Lord of the Rings: The Return of the King
# 4. 300, Lucky Number Slevin

# In[38]:


data.sort_values(by = 'vote_average', ascending = False)
data_1 = data.sort_values(by = 'vote_average', ascending = False).reset_index()
c = int(round(data_1.original_title.count()*0.01,0)-1)
print(data_1.original_title.loc[1:c].sort_values())
answer_ls.append(1)


# # 35. Какие актеры чаще всего снимаются в одном фильме вместе
# Варианты ответа:
# 1. Johnny Depp & Helena Bonham Carter
# 2. Hugh Jackman & Ian McKellen
# 3. Vin Diesel & Paul Walker
# 4. Adam Sandler & Kevin James
# 5. Daniel Radcliffe & Rupert Grint

# In[39]:


films = []
films.append(data[(data.cast.str.contains('Johnny Depp', na=False))&(data.cast.str.contains('Helena Bonham Carter', na=False))].original_title.count())
films.append(data[(data.cast.str.contains('Hugh Jackman', na=False))&(data.cast.str.contains('Ian McKellen', na=False))].original_title.count())
films.append(data[(data.cast.str.contains('Vin Diesel', na=False))&(data.cast.str.contains('Paul Walker', na=False))].original_title.count())
films.append(data[(data.cast.str.contains('Adam Sandler', na=False))&(data.cast.str.contains('Kevin James', na=False))].original_title.count())
films.append(data[(data.cast.str.contains('Daniel Radcliffe', na=False))&(data.cast.str.contains('Rupert Grint', na=False))].original_title.count())
films
answer_ls.append(5)


# # 36. У какого из режиссеров выше вероятность выпустить фильм в прибыли? (5 баллов)101
# Варианты ответа:
# 1. Quentin Tarantino
# 2. Steven Soderbergh
# 3. Robert Rodriguez
# 4. Christopher Nolan
# 5. Clint Eastwood

# In[40]:


c = {}

data['prib'] = data['revenue'] - data['budget']
director = ['Quentin Tarantino','Steven Soderbergh','Robert Rodriguez','Christopher Nolan','Clint Eastwood']
for x in director:
    list_1 = []
    list_films_all = []
    list_films_procent = []
    list_films_procent.append(data[(data.prib > 0)&(data.director == x)].original_title.count()/data[(data.director == x)].original_title.count()*100)
    list_films_all.append(data[(data.director == x)].original_title.count())
    list_1 = list_films_all + list_films_procent

    c[x] = list_1
c
answer_ls.append(4)


# # Submission

# In[41]:


len(answer_ls)


# In[43]:


pd.DataFrame({'Id':range(1,len(answer_ls)+1), 'Answer':answer_ls}, columns=['Id', 'Answer'])


# In[ ]:




