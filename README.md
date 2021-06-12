Created environment conda create -n environment_name

Activate environment conda activate environment_name

Create a requirements.txt file fsutil file createnew requirements.txt 0

Add required library to the requirements.txt file sklearn dvc dvc[gdrive]

Installed requirements pip install -r requirements.txt

Create README.md file and add above performed steps

Create a template file fsutil file createnew template.py

Added dirs required for the project

Copy the data to data_given folder. You can get data from https://drive.google.com/drive/folders/18zqQiCJVgF7uzXgfbIJ-04zgz1ItNfF5?usp=sharing

Do git init

Do dvc init

Do dvc add data_given/winequality.csv

Do git add . to move files to staging area

Do git commit -m "First commit"

Create a github repository

Do git remote add origin your repo link for eg.: git remote add origin https://github.com/kailas-muke/simple-dvc.git

Do git branch -M main

Do git push -u origin main

Lets beign for actual code

Update the params.yaml file with the configuration paths and values

Commit your changes using git add . git commit -m "Updated params.yaml" git push -u origin main

Create a new file under src folder get_data.py which will contain code to get the data fsutil file createnew src\get_data.py 0

Write the code to get data

Create load_data.py file in src where we will be adding data in raw folder fsutil file createnew src\load_data.py 0

24, Run the file and check that raw folder should be updated with winequality.csv file

Now add stages in the dvc.yaml file. Stages are nothing but it is a pipeline We have given the first stage name as load_data

After adding the cmd, deps and outs we will run the pipeline using command dvc repro

After running this command dvc.lock file is created, and it tracks the record if there is some change in the file then it reruns again and create new hash value else the hash value remains the same.

Create a new file split_data.py to split data set into training and testing instances fsutil file createnew src\split_data.py 0

Add the code to the split_data.py

Create stage 2 in dvc.yaml

Run dvc repro

Successfully we have implemented two stages i.e. two pipelines created

Push your code

Create a new file for training now fsutil file createnew src\train_and_evaluate.py 0

Write the code for training and add as pipeline for stage in dvc.yaml

Create a folder reports mkdir report

Create a file params.json file and scores.json fsutil file createnew report/params.json 0 fsutil file createnew report/scores.json 0

We need not worry about what is to be added it will automatically be updated by the dvc pipelines.

38 Do dvc repo

All the metrics related scores and params are updated after running above command.

Now let's check whether dvc is tracking the metrics or not. Run below command: dvc metrics show

We can also track the differences from past dvc metrics diff

Push the code to github now

Let's do some experiement with the params to check the tracking of model. Let's change the params value passed to model in params.yaml file

Do dvc repro

Let's compare the previously generated and newly generated metrics using dvc metrics diff

You can rollback to any previous stage using git checkout and the commit id.

Now that we have basic code implementation done. Lets look into over the testing part.

Install tox and pytest library
What is tox tox is mainly used as a command line tool and needs a tox.ini or a tool.tox section in pyproject.toml containing the configuration. tox can be used for ... creating development environments running static code analysis and test tools automating package builds running tests against the package built by tox checking that packages install correctly with different Python versions/interpreters unifying Continuous Integration and command line based testing building and deploying project documentation releasing a package to PyPI or any other platform

Let's create tox.ini file now in the root directory

Add environment list and command to the tox file

Create a directory tests which will contain testcases mkdir tests

Add a file conftest.py, init.py and test_config.py to tests folder fsutil file createnew tests/conftest.py 0 fsutil file createnew tests/test_config.py 0 fsutil file createnew tests/init.py 0

You can write the test cases in test_config.py file. Note that the testcases must start with test

Now create setup.py file which will help virtual env created by tox to identify the code package. fsutil file createnew setup.py 0

Add code in setup file.

Let's install the package created in setup.py pip install -e .

Use of doing this is src will be treated as package here and you will be able to import it

You can use pytest to run the testcases and tox to run complete environment related task including testcases.

We will not just check basic validations and put the validation check in test_config.py file

Update your tox file to include PEP8 standard.

Psh your changes.