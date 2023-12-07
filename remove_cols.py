import csv
with open("bad.csv") as source:
    rdr= csv.reader( source )
    with open("result.csv","w") as result:
        wtr= csv.writer( result )
        for r in rdr:
            wtr.writerow( (r[0], r[1], r[4], r[5]) )