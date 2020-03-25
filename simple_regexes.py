# P between 100 000 and 999 999
# No more than 1 alternating repetitive digit pair

re1 = r'^[1-9]{1}[0-9]{5}$'
#cyfra, i nastepna cyfra jest taka sama jak grupa 1
#czyli cyfraX-cyfra-cyfraX
re2 = r'(\d)(?=\d\1)'
