./CSVtoJSON ../data/PER_data.csv ../data/PER_data.json
./CSVtoJSON ../data/PER_full_data.csv ../data/PER_full_data.json

git add ../data/PER_data.csv
git add ../data/PER_full_data.csv
git add ../data/PER_data.json
git add ../data/PER_full_data.json
git commit -m "updated Peru data $1"
git push

git add ../res/graphs/
git add ../res/tweets.dat
git commit -m "updated Peru graphs and tweet contents $1"
git push