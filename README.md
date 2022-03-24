# text-mining

Please read the [instructions](instructions.md).
Google doc link for [Project Writeup and Reflection](https://docs.google.com/document/d/18dcVZ3D3bmgqXKxxnCC8As9EPKBAW6rJWj_1Q-3S1-c/edit)

Ziya Aydin 
3/23/22
OIM 3640
Professor Li

***Project Writeup and Reflection***

For this project, from Project Gutenberg Books, I used the book “The Foundation of the Ottoman Empire; a history of the Osmanlis up to the death of Bayezid I (1300-1403)” written by Herbert Adams Gibbons. It is a history book that explains the first 103 years of the Ottoman Empire. There are 4 chapters in the book and each of them talks about a different Sultan. I started my project with characterizing by word frequencies and computing summary statistics. I found the most common 20 words excluding and including StopWords in the whole book and each chapter. By looking at the most common words in each chapter, I wanted to understand what and who is each chapter about. Later, by using Natural Language Processing, I calculated the Sentiment Intensity of the whole book and each chapter. By doing this, I wanted to have an idea of the author's perspective on 4 Sultans. Lastly, By using The Fuzz Library which uses Levenshtein Distance, I calculated the distance of each chapter with each other to find the most similar chapters. 


I wanted to compare the chapters to each other, so I created a new text file for each of the 4 chapters. For example (Chapter_1.txt). Besides the 4 chapters, the book also had a long Bibliography and Index parts. To get a better understanding of the content I manually deleted Bibliography and Index and created a new version of the book called “Cleaned_56836-0.txt”. I believe that instead of writing the code of “just look at chapter 1” or “exclude bibliography”, manually editing the text file simplified my code and made me gain some time. It is true that if I had many chapters manually editing the text files would not be ideal but in this case, I think it was the easiest option. 

I had a general to specific approach in my analysis. I first looked at the most common words including the stopwords, then the most common words excluding the stop words in the whole book. Then I had the same analysis for the whole book minus Bibliography and Index. Later I looked at the most common words in each chapter. Furthermore, I found the Sentiment Intensity of each chapter. Finally, after learning more about the book and each chapter I compared each chapter with the other by using  Levenshtein Distance. I think that my approach of general to specific helped me to have a macro and micro point of view for the book and each chapter.


For the results, when I looked at the most common words in the whole book, obviously 19/20 of the words were StopWords [Exhibit1](images/Exhibit1.PNG). Later, when I had the most common words excluding the StopWords, 9/20 of the words were from Bibliography or Index [Exhibit2](images/Exhibit2.PNG). So I decided to use to analyze the whole book and each chapter excluding the StopWord, Bibliography, and Index. 

Chapter 1 is about Sultan Osman and the most common word in Chapter 1 is “osman”. At the same time, based on the other history books one of the most important accomplishments of Sultan Osman is conquering Bursa and one of the most common word in the chapter is “brusa” [Exhibit3](images/Exhibit3.PNG). From this analysis, we can understand that in this chapter the author is explaining how Sultan Osman conquered Bursa. Chapter 2 is about Sultan Orkhan and the most common word in Chapter 2 is “orkhan”. Based on the history books the most important thing about Sultan Orkhan is the war with Byzantine Emperor Andronicus and the two of the most popular words in the chapter are “andronicus” and “byzantine” [Exhibit4](images/Exhibit4.PNG). Chapter 3 is about Sultan Murad and the most common word in Chapter 3 is “murad”. During his time Sultan Murad had wars with Serbians in the Balkans and the most three common words in the chapter are “serbian”, “serbians” and “balkan” [Exhibit5](images/Exhibit5.PNG). Lastly, chapter 4 is about Sultan Bayezid and the most common word in Chapter 4 is “bayezid”. Sultan Bayezid tried to conquer Istanbul (Constantinople) and had a big loss against Timur. Two of the most common words in the chapter are “constantinople” and “timur” [Exhibit6](images/Exhibit6.PNG). As it can be seen from these examples, from the most common 20 words of each chapter we can understand the Sultan and some major events of that time.

Furthermore, by using Natural Language Processing, I calculated the Sentiment Intensity of the whole book and each chapter. Based on the results, the whole book is 81% neutral which was expected because of the nature of a history book. Although the numbers are pretty close, Chapter 3 has the lowest Neutrality and highest Negativity and Positivity. Based on this we might say that the author used more emotional language for Sultan Murad [Exhibit7](images/Exhibit7.PNG).

Lastly, By using The Fuzz Library which uses Levenshtein Distance, I calculated the distance of each chapter with each other to find the most similar chapters. Based on the results, Chapters 1 and 4 have the closest Levenshtein Distance and Chapters 3 and 4 have the longest distance [Exhibit8](images/Exhibit8.PNG). Although chapters 1 and 4 look the most similar chapters and 3 and 4 look the least similar chapters the numbers are very similar to make a conclusion like that. 


In conclusion, I really enjoyed working on this project. First of all the project showed me the importance of text analysis and what Python is capable of doing. I understood how to use different libraries and how convenient it is to use them. Furthermore, to gain some time and simplify the code I manually edited the data file and create different versions of the book. If I had bigger data with more chapters this would not be possible. If I used if line.startswith or similar codes and finish the analysis inside the code I think I would have even learned more from the project. But for the scope of my project, I think I did a good job to preprocess my data. Moreover, if I had to re-do a project like this I would have chosen a text with more emotions, for example, a movie review, because having a sentiment analysis for a history book was not ideal.I also had an idea how Turnitin Algorithm works thanks to Levanhstein distance. Lastly I tried to have Markov Text Synthesis, but I was not successful at it, I could have worked harder and smarter on it. But in general, I really enjoyed working on this project and looking forward to exploring python more. 

***Exhibits***

[Exhibit1](images/Exhibit1.PNG)
[Exhibit2](images/Exhibit2.PNG)
[Exhibit3](images/Exhibit3.PNG)
[Exhibit4](images/Exhibit4.PNG)
[Exhibit5](images/Exhibit5.PNG)
[Exhibit6](images/Exhibit6.PNG)
[Exhibit7](images/Exhibit7.PNG)
[Exhibit8](images/Exhibit8.PNG)



