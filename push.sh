#!/bin/bash
# push.sh


echo -n "Pusing to repo!"
git add .
git commit -a -m "update"
git push -u origin main

