cd ..
git add PER_data.csv
git add PER_full_data.csv
git commit -m "updated Peru data $1"
git push
git add ../res/graphs
git add ../res/tweets.dat
git commit -m "updated Peru graphs and tweet contents $1"
git push