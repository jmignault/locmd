#!/bin/bash
while read p; do
    sleep 30
    curl -k --rate 10/m https://lccn.loc.gov/"${p}"/marcxml -o "${p}".xml
done < $1
