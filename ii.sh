#!/bin/bash
# -*- coding: utf-8 -*-

echo "${G}[*] Enter The Target's IP Address: ${G}"

read domain

echo "${G}Doing ReverseIP Lookup ${G}"

echo " ====================================="

curl "http://reverseip.logontube.com/?url=$domain&output=json" >abc.txt


echo "${G} Arranging up all the domains${G}"
echo "++++++++++++++++++++++++++++++++++++++"
echo "**************************************"
echo "++++++++++++++++++++++++++++++++++++++"
sed -i 's/{"hostip"/HOSTIP/g' abc.txt ; sed -i 's/"hostname"/HOSTNAME/g' abc.txt ; sed -i 's/"response" : {"domain_count" :/Domains Found/g' abc.txt ;  sed -i 's/ "domains" :/LIST OF DOMAINS/g' abc.txt ; cat abc.txt | tr "," "\n" ; rm abc.txt


