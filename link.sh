# https://health-infobase.canada.ca/src/data/covidLive/covid19.csv
mv covid19.csv covid19.csv.bak
if wget "https://health-infobase.canada.ca/src/data/covidLive/covid19.csv"
then
	rm covid19.csv.bak
else
	mv covid19.csv.bak covid19.csv 
fi
