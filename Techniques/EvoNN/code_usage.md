### Complete Code: 
Complete link to code can be found [here](https://drive.google.com/file/d/0ByNH8-pk8qJDYW96Y0dPdGUxdUpJc1EzT1RiNEFYLXgtMlFF/view)

### File Structure:
1. PPNGA_subsets.m : To generate the relevant subsets from the complete data set. In short , subset is basically frequent item sets.

( Steps to follow :

- Set input index ,Ex: (1:8) ( as per data given)
- Set output index ( based on outputs given. In lab , we were given 2 output indexes, 9 and 10) ( run code one by one for both output index)

SETSLOG file will be generated here )

2. Output.m : To train and test data based on default parameters. 

To know the parameters list , see the codes ( change variables setslog name )

3. PPopt.m : To optimize both output indexes ( One was UTS and other i can't remember) . This file is where multi objective optimization takes place. It's main aim is to handle the cases of pareto optimality. To know more, search on google :P

4. SVR.m : To show the dependency of each input variable on accuracy.

### How to run the Code?

-----------------------------------------------------------------------------------
Step 1 : Importing data
-----------------------------------------------------------------------------------
Things to remember :
- Do not convert whole data into text type
- Also remember to convert the variables on first 2 lines to text
- Duplicate the first line and overwrite the second line of variable( I don't know y, but krna h)

In the Home menu , there is import data. Click on that.

After that, select the file to be imported ( CSV only)

Now save the whole data as a CELL ARRAY in any variable ( dataSet )

Now select first 2 rows and convert them to text.

Save the first 2 rows as dataVar
-----------------------------------------------------------------------------------
Step 2: Saving workspace data into matlab file
-----------------------------------------------------------------------------------
Now close the Import data window. On the rightmost pane , you can see your workspace data.

Right click on that and save your data as matlab file. Save both dataSet and dataVar as set.mat and var.mat.
-----------------------------------------------------------------------------------
Step 3: Open PPNGA_subsets.m
-----------------------------------------------------------------------------------
Change
Data = 'set.mat';
DATANAME='var.mat';

Remember to set these:

in_index = [1:7] // Depends on dataset
out_index = [x] ( x= 8 for first time and 9 for second time)

Now run from editor menu and get 2 setslog file.
-----------------------------------------------------------------------------------
Step 4: Open output.m
-----------------------------------------------------------------------------------
// Set yours setslog name below . setslog will be generated after step 3. Also remember this command will run twice for 2 SETSLOG

Run below command :
err_table = output('Your_Setslog.mat')

Run and SAVE ALL IMAGES.
-----------------------------------------------------------------------------------
Step 5: Open PPopt.m
-----------------------------------------------------------------------------------
// Set yours setslog name in the below variables . setslog will be generated after step 3.

Setslog(1) = {'Setslog5-13_shanker.mat'};
Setslog(2) = {'Setslog5-14_shanker.mat'};

Run and SAVE ALL IMAGES.
-----------------------------------------------------------------------------------
Step6 : Open SVR.m
-----------------------------------------------------------------------------------
response = svr('Your_Setslog1.mat', 'figl', 'trend.mat');
Run and SAVE ALL 8 IMAGES SAVED in code directory.

response = svr('Your_Setslog2.mat', 'figl', 'trend.mat');
Run and SAVE ALL 8 IMAGES SAVED in code directory.

-----------------------------------------------------------------------------------
Note: Same steps for Biogp. Similar names and similar steps.
----------------------------------------------------------------------------------- 

