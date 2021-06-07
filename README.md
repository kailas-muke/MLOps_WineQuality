create env

conda create -n wineq python=3.7 -y
activate env

conda activate wineq
created a req file

install the req

pip install -r requirements.txt

download the data from

https://drive.google.com/drive/folders/18zqQiCJVgF7uzXgfbIJ-04zgz1ItNfF5?usp=sharing

git init

dvc init 

dvc add data_given/winequality.csv

git add .

git commit -m "first commit"
oneliner updates for readme


git add . && git commit -m "update Readme.md"

git branch -M main 

git remote add origin https://github.com/kailas-muke/simple-dvc.git

git push origin main
