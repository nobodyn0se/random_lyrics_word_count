# Random Lyrics Word Count 
This roughly 100 lines of script picks up a random song from songmeanings.com, obtains its lyrics and creates a graph of unique words (removed top 10% and bottom 10%) 

Known issues:
1. Sometimes it requests a song which might be unavailable in the user's region due to copyright or intellectual property rights laws, displays an error message but creates a graph of these words. 
2. The script sorts the words into a list by decreasing order of occurrences then randomly removes top 10% and bottom 10% words hence, common words like a, the can be visible in the graph. 
3. Does not show the title of the song in the graph displayed. 
4. Three-four unwanted lines get added to the list as the script writes the lyrics into a text file. The lines need to be removed as they make the graph distorted. 
5. Gets lyrics from one source only. 
6. Don't tell me .... 
