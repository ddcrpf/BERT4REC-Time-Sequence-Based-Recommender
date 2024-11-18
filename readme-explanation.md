# Time based Recommendation System

BERT4Rec: Sequential Recommendation with Bidirectional Encoder Representations from Transformer
Paper Link : https://arxiv.org/pdf/1904.06690
Article Link: https://towardsdatascience.com/build-your-own-movie-recommender-system-using-bert4rec-92e4e34938c5

predict user pattern over time.



Data analysis for bert4rec
used movie lens 25 m data set 

for every user:
    get the sequence of movie interactions based on timestamps (chronological order)
    you only consider movie titles.

    df looked like - 
    userid | movie list | len of list | movie-ids-list

where movie-list  was a list of dict. eg - [{'timestamp': '2006-05-17', 'movie': 'Lord .....

Then check for duplicates - 
Check for duplicate entries
                user_1 : [{'20-09-2024':'kal ho na ho'},{'10-09-2024': Gahzi Attack},...,{'20-08-2024':'kal ho na ho'}]
        if duplicate entires are found, capture their time duration,
            time duration = latest time of the movie watched - last to last time movie watched.
              plot the distribution of the list of movies which the user's have watched, for training the model
        movies must be sorted in chronological order of time!
        user_id         list of movies                length of list of movies.
        user_1 : [movie1, movie2, movie3,...,movien]. len1
        user_2 : [movie1, movie2, movie3,...,movien]. len2
    
    plot the distribution of "length of list of movie"
* 		remove outliers, consider data uptil 99%
* 	        analyze the outliers.

BERT4Rec

user ---> [moovie1,movie2, movie3,movie4,nmovie5]

----------[movie1, MASK, movie3, MASK, movie5]

---------------------BERT4Rec--------------------

---------[moovie1,movie2, movie3,movie4,nmovie5]. , [moovie6,movie7, movie8,movie9,nmovie10]

lets say user has interacted with 10 movies, 
--- from 10 movies, you consider k movies, lets say k = 5,
--- from 10 movies which user had watched/interacted you consider first 5 movies, and the add a MASK at the end of the 5th movie
--- predict the movies based on first 5 movies give to the model, lets say you recommend 15 movies, --> ideal order.
--- actual order = 5 movies which you to kept for evaluation 
--- based on actual order and ideal order tou can calucate ndgc@k and all.

----- 2 parameter
 -- splitining parameter for evaluation
 -- how many movies you want to recommend.


 NDCG@10: 0.34
so i guess it means model is capturing relevant items and ranking them somewhat effectively, but not consistently placing them near the top . 

Hit Rate@10: 0.2960
about 2 movies where correctly predicted and present in 10

but Precision@10: 0.2
this is low. i have tried multiple methods and retraining the model. but it is low.

But to my surprise, the performance of model wrt recommending item in related genres is pretty high even though no genre related info was given to the model.

Genre-Based Precision@10: 0.75
Genre NDCG@10: 0.6

so even though model is not recommending exactly the same items, it is recommending items consistent with user watch history 


