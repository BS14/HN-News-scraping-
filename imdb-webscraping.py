from bs4 import BeautifulSoup
import requests, openpyxl

excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = 'Top Rated Movies'
print(excel.sheetnames)
sheet.append(['Movies Rank', 'Movie Name', 'Year of Release', 'IMDB Rating'])

 
#This try catch block will check the validity of the URL along with printing the error message 
try:
    source = requests.get('https://www.imdb.com/chart/top/')

    #Checking validity of the URL provided 
    source.raise_for_status()

    soup = BeautifulSoup(source.text,'html.parser')
    #print(soup)
    movies = soup.find('tbody', class_="lister-list").find_all('tr')
    #print(len(movies))
    #Access the tr tag and then the td tag so that we can access the movies neame 
    for movie in movies:

        #This block iterates to each tr tag and then access the td tag within tr tag. From td tag, it access the "a href" section and then prints the text only ommitting attributes 
        name = movie.find('td', class_="titleColumn").a.text
        #Strip is going to remove all the new line character extra spaces. Split will divide the output based on the apperance of '.'
        rank = movie.find('td', class_="titleColumn").get_text(strip=True).split('.')[0]
        year = movie.find('td', class_="titleColumn").span.text.strip('()')
        rating = movie.find('td', class_="ratingColumn imdbRating").strong.text
        print(rank, name, year, rating)
        sheet.append([rank, name, year, rating])


except Exception as e: 
    #Printing the error message 
    print(e)

excel.save('IMDB Movie Rating.xlsx')