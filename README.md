# UdemyDataAnlalysis

#### Udemy is a platform has more than 40 million students, 155,000 courses and 70,000 instructors teaching courses in over 65 languages. There have been over 480 million course enrollments. Students and instructors come from 180+ countries and 2/3 of the students are located outside of the U.S.

#### here we have [data.csv](https://drive.google.com/file/d/1zglnQkX756nfySz9RT8V3p1R6-69RHmS/view) file of udemy website, which contain total 9 columns..
* course name
* paid/free
* price
* subscribers
* reviews
* no_of_lec
* levles
* timestemp
* subject
---
## TASK:- VISULIZE THE DATA USING PYTHON PANDAS DATAFRAME.
Prepare and Clean the data. Take 1000 data sample from the dataset for analysis
Perform exploratory data analysis and answer these questions
  1. Which are top selling courses?
  1. Show all the courses which are free?
  1. Which subject has the maximum number of courses?
  1. List out all the courses that are related to 'Java’.
---
so here we import some python library for visulization and performing action...
```bash
pip install pandas
pip install numpy
pip install matplolib
pip install seaborn
pip install plotly
```
Now we just check the dataset which we grab from udemy website..!
<img src="https://user-images.githubusercontent.com/84271454/118900525-c8987180-b92e-11eb-94a8-f8829301f4c8.png" width="800" height="300">

After analyze the data now we know that here single column has not contain __NULL__ data.Then we removing duplicate data from dataset.
and now we our dataset is ready for further process..
But as mention in the task we take only 1000 raw's data as input.

---

### TASK_SOLUSTION.START:-
1. Show all the courses which are free?<br>
<!-- <img src="https://user-images.githubusercontent.com/84271454/118901089-12358c00-b930-11eb-83d5-1d3293cf6df0.png" width="800" height="350"> -->
couses derived on the base of 
|is_paid|total|
|-------|-----|
|False  |85   |
|True   |915  |

2. Which subject has the maximum number of courses?<br>
<!-- ![thirdpic](https://user-images.githubusercontent.com/84271454/118901788-bff56a80-b931-11eb-889a-e957f7af13e9.png) -->

|subject|count|
|-------|-----|
|Business Finance     |333|
|Graphic Design       |148|
|Musical Instruments  |177|
|Web Development      |342|

3. List out all the courses that are related to 'Java’.
    For finding java cousrse we finding, __[java and jquery]__ word in course_title columns<br>
<!-- ![fourthpic](https://user-images.githubusercontent.com/84271454/118902068-79ecd680-b932-11eb-96f4-39084e7e08d9.png) -->

|subject|
|-------|
|JavaScript, jQuery and Ajax|
|JQuery DOM and Ajax Concept Explained for Begi...|
|JavaScript Game Development: Create Your Own B...|
|Explore JavaScript Beginners Guide to Coding J..|
|Learn Javascript & JQuery From Scratch|
|Learn JavaScript from scratch|
.<br>
.<br>
.<br>
|Javascript Essentials|
|Professional Web Scraping with Java|

---
Now, fourth most important part is coming... at the point of view of our task but its also important for ML training user for course prediction and recommndation system..<br><br> 
4. Which are top selling courses?<br><br>
  for finding ans of this question we need to check all params. Like how much percent each columns is corelated with another columns.
  so we are using heatmap for this and check what's the output...<br>  
|Heatmap|snsburn|
|:---:|:---:|
|![](https://user-images.githubusercontent.com/84271454/118902492-5d9d6980-b933-11eb-8b47-453cb44197f6.png)|![](https://user-images.githubusercontent.com/84271454/118904862-4b71fa00-b938-11eb-9eca-8bd491541cad.png)|<br/>
  here we see that [no_reviews] is corelate [with no_lecture] + [price]
  
  So we agian check that, does Most Selling Course depend on views, price and timeperiod ??
|SUBvsPRICE|SUBvsYEAR|
|:---:|:---:|
|![](https://user-images.githubusercontent.com/84271454/118905763-ff27b980-b939-11eb-8ea5-5c0b5df6fd1c.png)|![](https://user-images.githubusercontent.com/84271454/118905772-03ec6d80-b93a-11eb-8d68-304a37d5f2ea.png)|<br/>

So after analyize All thr params of columns and we get that two result...<br>
----
## FINAL RESULT:-
1. Top 30 best selling and most popular course on the base of num_of_subscribers
![newplot (1)](https://user-images.githubusercontent.com/84271454/118906070-a147a180-b93a-11eb-8549-2a7c64707e7f.png)
2. Top 30 best selling and most popular course on the base of num_reviews<br>
![newplot (2)](https://user-images.githubusercontent.com/84271454/118906073-a3116500-b93a-11eb-9893-efdf67dd7154.png)
----
## ANALYSIS:-
#### AFTER SEEING THIS BOTH RESULT I AM CONCLUDE THAT, MOST OF STUDENT ARE INTERESTED IN WEB-DEVELOPMENT AS COMPARED OTHER SUBJECTS. ALSO WEB-DESIGINING IS MOST POPULAR TOPIC IN CURRENT TIME.




















