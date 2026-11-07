#!/usr/bin/env bash
# Stage 1a of the pipeline: pull the structured databases once (sequential because of API rate limits).
set -u
cd "$(dirname "$0")/../.."
F="python3 tools/data/fetch.py"
REP="276,842,156,392,410,356,250,826,380,360"   # DE, US, CN, JP, KR, IN, FR, UK, IT, ID
$F usgs
$F pinksheet
$F stan --countries DEU,FRA,ITA,GBR,USA,JPN,KOR --activity C20,C24,C25,C26,C27,C28,C29,C30,C32 --measure P1 --start 2010
$F stan --countries DEU,FRA,ITA,GBR,USA,JPN,KOR --activity C20,C24,C25,C26,C27,C28,C29,C30,C32 --measure B1G --start 2010
$F prodcom --reporters EU27_2020,DE,FR,IT,SE,AT --years 2019-2024
for HS in 7502 7505 7506 7507 7504 8105 8109 7219 7220 7223 7409 7606 8311 8411; do
  $F comtrade --hs $HS --reporters $REP --years 2019-2024 --flow X,M
done
echo "PULL_ALL DONE"
