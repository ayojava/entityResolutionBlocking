import csv


entity={}
entitiesList=[]
wantedDirectors=['Stanley Kubrick','Robert Rodriguez','Quentin Tarantino','Rainer Werner Fassbinder',
                 'Francis Ford Coppola', 'Ethan Coen', 'Akira Kurosawa', 'Christopher Nolan', 'James Cameron',
                 'Martin Scorsese']
wantedMovies=[]
with open('name.basics.tsv') as nameFile:
    next(nameFile) # skip headings
    reader=csv.reader(nameFile,delimiter='\t')
    for id, name, birthYear, deathYear,	primaryProfession, knownForTitles in reader:
        if name in wantedDirectors:
            # extracting the author
            entity= {'idIMDB' : id, 'name' : name, 'birthYear' : birthYear,  'deathYear' : deathYear,
                     'primaryProfession': primaryProfession, 'knownForTitles': knownForTitles }
            entitiesList.append(entity)
            wantedDirectors.remove(name) # There were several duplicate names but the 'famous' people have the lower id
                                        # and therefore appear first in the files

            # extracting the movies s/he is famous for
            knownFor = knownForTitles.split(",")
            wantedMovies.extend(knownFor) # Collecting the movies from the current director in the to query list

with open('title.basics.tsv') as moviesFile:
    next(moviesFile) # skip headings
    reader = csv.reader(moviesFile, delimiter='\t')
    for tconst, titleType, primaryTitle, originalTitle, isAdult, startYear, endYear, runtimeMinutes, genres in reader:
        if tconst in wantedMovies:
            entity={'idIMDB': tconst, 'title': originalTitle, 'year': startYear}
            entitiesList.append(entity)


for entity in entitiesList:
    print "\n new entity \n"
    for key in entity:
        print key + ' ' + entity[key]