# PA4
## Initialization
Import pandas, matplot, and seaborn. Pandas for dataframes, matplot and seaborn for graphing. Make sure that board2.csv is also within the folder of the ipynb.
## Instru = [“Name”, “GEAS”, “Electronics >70”]; where track is constant as Instrumentation and hometown Luzon
### a.) Dataframe
1. Instru = pd.DataFrame(board2, columns = ['Name','GEAS','Electronics','Track','Hometown'])
  - This reads board2, and initializes the columns as the given, proper punctuation is needed.
2. Instru.loc[(Instru['Electronics']>70)&(Instru['Track']=='Instrumentation')&(Instru['Hometown']=='Luzon')]
  - This locates what's being asked.
  - The dataframe is done, no need to edit unless you're crazy since it's already organized.
### b.) Visuals
1. Instru_visuals = Instru.loc[(Instru['Electronics']>70)&(Instru['Track']=='Instrumentation')&(Instru['Hometown']=='Luzon')]
2. Assign these values:
- plt.figure(figsize=(10, 6)) _- - - sets the size (row, column)_
- plt.bar(Instru_visuals['Name'], Instru_visuals['Electronics']) _- - - sets what should be shown in (x,y)_
- plt.xlabel('Name') _- - - sets the name of x_
- plt.ylabel('Electronics Score') _- - - sets the name of y_
- plt.title('Electronics Scores of Instrumentation Students from Luzon') _- - - sets the title_
- plt.xticks(rotation=45) _- - - rotates the names of x by 45° (so it looks better)_
- plt.show() _- - - i wonder what this does_
## Mindy = [ “Name”, “Track”, “Electronics”, “Average >=55”]; where hometown is constant as Mindanao and gender Female
### a.) Dataframe
1. Mindy = pd.DataFrame(board2, columns = ['Name','Track','Math','Electronics','GEAS','Communication','Hometown','Gender'])
   - Reads board2, and initializes what's needed.
2. Mindy['Average'] = Mindy[['Math', 'Electronics', 'GEAS', 'Communication']].mean(axis=1)
   - Sets the average by getting the mean of the four subjects.
3. Mindy.loc[(Mindy['Average']>=55)&(Mindy['Hometown']=='Mindanao')&(Mindy['Gender']=='Female')]
   - This is what's being asked.
   - This dataframe is done too.
### b.) Visuals
1. Mindy['Average'] = Mindy[['Math', 'Electronics', 'GEAS', 'Communication']].mean(axis=1)
2. Mindy_visuals = Mindy.loc[(Mindy['Average']>=55)&(Mindy['Hometown']=='Mindanao')&(Mindy['Gender']=='Female')]
   - Set these two again just for safe measure.
3. Assign these values (I don't need to explain them again, I still used matplot here as I think it's the best library for this question.):
- plt.figure(figsize=(10, 6))
- plt.bar(Mindy_visuals['Name'], Mindy_visuals['Average'])
- plt.xlabel('Name')
- plt.ylabel('Average')
- plt.title('Average Scores for Female Students from Mindanao with Average >= 55')
- plt.xticks(rotation=45)
- plt.show()
## Create a visualization that shows how the different features contributes to average grade. Does chosen track in college, gender, or hometown contributes to a higher average score?
### Initialization
1. nyv = pd.DataFrame(board2, columns = ['Name','Gender','Track','Hometown','Math','Electronics','GEAS','Communication'])
2. nyv['Average'] = nyv[['Math', 'Electronics', 'GEAS', 'Communication']].mean(axis=1)
  - These were explained in Mindy. In addition, any function that's been already explained earlier will not be explained again.
### Plot 1
- plt.figure(figsize=(14, 6))
- plt.subplot(1, 3, 1) _- - - assigns a row and a column, plus the location of this plot (row, column, index)_
- sns.boxplot(x='Track', y='Average', data=nyv)
- plt.title('Average Score by Track') 
- plt.xticks(rotation=45)
### Plot 2
- plt.subplot(1, 3, 2)
- sns.boxplot(x='Gender', y='Average', data=nyv)
- plt.title('Average Score by Gender')
### Plot 3
- plt.subplot(1, 3, 3)
- sns.boxplot(x='Hometown', y='Average', data=nyv)
- plt.title('Average Score by Hometown')
- plt.xticks(rotation=45)
- plt.tight_layout() _- - - automatically adjusts the spacing between subplots so it doesn't overlap_
- plt.show()
### Plot 4
- sns.pairplot(nyv[['Math', 'Electronics', 'GEAS', 'Communication', 'Average']]) _- - - creates a matrix of scatterplots to visualize the relationship between these variables_
- plt.suptitle('Pair Plot of Subjects vs. Average', y=1.03) _- - - a very big title (name, position in the y-axis(set to 1.03 so it doesn't overlap))_
- plt.show()
### Plot 5
- corr = nyv[['Math', 'Electronics', 'GEAS', 'Communication', 'Average']].corr() _- - - .corr() correlates the plots_
- plt.figure(figsize=(8, 6))
- sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f') _- - - annot=True annotates each cell with the correlation efficient, cmap='coolwarm' is the color decided for the heatmap, fmt = '.2f' is the format for -displaying correlation coefficients in the heatmap_
- plt.title('Correlation Heatmap')
- plt.show()
### Learnings
1. I now know what Matplot and Seaborn does, they focus on graphs but vary slightly on what graphs they excel on.
2. Grasped how to Pandas slightly better.
3. Memorizing the cheat sheets are a pain, better to use them from time to time and understand.
