from bs4 import BeautifulSoup
import requests

def searchnews():

    topic = input("Enter the topic you want to see the news for: ")
    words = topic.split(" ")
    n = len(words)
    if n == 1:
        word = words[0]
    else:
        i = 0
        search = ""
        while i < n - 1:
            search = search + words[i] + "+"
            i = i + 1
        search = search + words[n - 1]
        word = search

    site = "https://www.ndtv.com/search?searchtext=" + word
    req = requests.get(site).text
    soup = BeautifulSoup(req, 'html5lib')
    items = soup.find_all("li", class_="src_lst-li")
    for item in items:
        contents = item.find_all("div", class_="src_lst-rhs")
        for content in contents:
            boxes1 = content.find_all("div", class_="src_itm-ttl")
            for box1 in boxes1:
                headlines = box1.find("a")
                for headline in headlines:
                    headline = headline.text.strip()
                    print(headline)
            boxes2 = content.find_all("div", class_="src_itm-txt")
            for box2 in boxes2:
                news_content = box2.text.strip()
                print(news_content)
                print("")


def trendingnews():
    site = "https://www.ndtv.com/trends"
    req = requests.get(site).text
    soup = BeautifulSoup(req, 'html5lib')
    items = soup.find_all("div", class_="trend-list")
    for item in items:
        contents = item.find_all("div", class_="trend-list_desc")
        for content in contents:
            boxes1 = content.find_all("h3", class_="trenz_news_head lh22 listing_story_title")
            for box1 in boxes1:
                headlines = box1.find("a")
                for headline in headlines:
                    headline = headline.text.strip()
                    print(headline)
            boxes2 = content.find_all("p", class_="trenz_dateline")
            for box2 in boxes2:
                news_content = box2.text
                print(news_content)
            boxes3 = content.find_all("div", class_="ndtv_user_counter")
            for box3 in boxes3:
                count = box3.find("a").text
                print(count)
                print("")



def opinionnews():
    site = "https://www.ndtv.com/opinion#pfrom=home-ndtv_mainnavgation"
    req = requests.get(site).text
    soup = BeautifulSoup(req, 'html5lib')
    items = soup.find_all("div", class_="news_Itm")
    for item in items:
        contents = item.find_all("div", class_="news_Itm-cont")
        for content in contents:
            boxes1 = content.find_all("h2", class_="newsHdng")
            for box1 in boxes1:
                headlines = box1.find("a")
                for headline in headlines:
                    headline = headline.text.strip()
                    print(headline)
            boxes2 = content.find_all("p", class_="newsCont")
            for box2 in boxes2:
                news_content = box2.text
                print(news_content)
                print("")


def technews():
    site = "https://gadgets360.com/news"
    req = requests.get(site).text
    soup = BeautifulSoup(req, 'html5lib')
    items = soup.find_all("div", class_="caption_box")
    for item in items:
        boxes1 = item.find_all("span", class_="news_listing")
        for box1 in boxes1:
            headlines = box1.text
            print(headlines)
        boxes2 = item.find_all("div", class_="dateline")
        for box2 in boxes2:
            dateline = box2.text
            print(dateline)
        boxes3 = item.find_all("a", class_="catname")
        for box3 in boxes3:
            category = box3.text
            print(category)
            print("")


def sportsnews():
    site = "https://indianexpress.com/section/sports/"
    req = requests.get(site).text
    soup = BeautifulSoup(req, 'html5lib')
    items = soup.find_all("div", class_="articles")
    for item in items:
        boxes1 = item.find_all("h2", class_="title")
        for box1 in boxes1:
            headlines = box1.find("a")
            for headline in headlines:
                headline = headline.text.strip()
                print(headline)
        boxes2 = item.find_all("div", class_="date")
        for box2 in boxes2:
            date = box2.text.strip()
            print(date)
        boxes3 = item.find_all("p", class_="")
        for box3 in boxes3:
            news_content = box3.text
            print(news_content)
            print("")


def autonews():
    site = "https://www.carandbike.com/#pfrom=home-ndtv_auto"
    req = requests.get(site).text
    soup = BeautifulSoup(req, 'html5lib')
    items = soup.find_all("div", class_="banner-list__link")
    for item in items:
        boxes1 = item.find_all("div", class_="banner-list__ttl")
        for box1 in boxes1:
            headlines = box1.find("a", class_="h__truncate-line js-href-target").text
            print(headlines)
            print("")


def educationnews():
    site = "https://indianexpress.com/section/education/"
    req = requests.get(site).text
    soup = BeautifulSoup(req, 'html5lib')
    items = soup.find_all("div", class_="articles")
    for item in items:
        boxes1 = item.find_all("h2", class_="title")
        for box1 in boxes1:
            headlines = box1.find("a")
            for headline in headlines:
                headline = headline.text.strip()
                print(headline)
        boxes2 = item.find_all("div", class_="date")
        for box2 in boxes2:
            date = box2.text.strip()
            print(date)
        boxes3 = item.find_all("p", class_="")
        for box3 in boxes3:
            news_content = box3.text.strip()
            print(news_content)
            print("")


def businessnews():
    site = "https://www.moneycontrol.com/news/business/"
    req = requests.get(site).text
    soup = BeautifulSoup(req, 'html5lib')
    items = soup.find_all("li", class_="clearfix")
    for item in items:
        boxes1 = item.find_all("h2")
        for box1 in boxes1:
            headlines = box1.find("a")
            for headline in headlines:
                headline = headline.text.strip()
                print(headline)
        boxes2 = item.find_all("span")
        for box2 in boxes2:
            date = box2.text.strip()
            print(date)
        boxes3 = item.find_all("p", class_="")
        for box3 in boxes3:
            news_content = box3.text.strip()
            print(news_content)
            print("")


def biggestbook():
    site = "https://bookmarks.reviews/biggest-new-books/"
    req = requests.get(site).text
    soup = BeautifulSoup(req, 'html5lib')
    items = soup.find_all("div", class_="latest_book")
    for item in items:
        boxes1 = item.find_all("div", class_="book_item_ranking")
        for box1 in boxes1:
            genres = box1.find_all("div", class_="book_genre")
            for genre in genres:
                headline = genre.text.strip()
                print(headline)
        boxes1 = item.find_all("div", class_="latest_book_text")
        for box1 in boxes1:
            names = box1.find_all("div", class_="latest_book_title super_clarendon")
            for name in names:
                name=name.text.strip()
                print("Book Name: "+name)
            authors = box1.find_all("div", class_="latest_book_author")
            for author in authors:
                author = author.text.strip()
                print("Author: "+author)
            reviews = box1.find_all("span", class_="featured_book_review_index")
            for review in reviews:
                review = review.text.strip()
                print("Review: "+review)
                print("")


def searchbook():

    bookname = input("Enter the name of book you want to search for: ")
    words = bookname.split(" ")
    n = len(words)
    if n == 1:
        word = words[0]
    else:
        i = 0
        search = ""
        while i < n - 1:
            search = search + words[i] + "+"
            i = i + 1
        search = search + words[n - 1]
        word=search

    site = "https://bookmarks.reviews/?post_type=bookmark&s=" + word
    req = requests.get(site).text
    soup = BeautifulSoup(req, 'html5lib')
    items = soup.find_all("div", class_="latest_book")
    for item in items:
        boxes1 = item.find_all("div", class_="book_item_ranking")
        for box1 in boxes1:
            genres = box1.find_all("div", class_="book_genre")
            for genre in genres:
                genre = genre.text.strip()
                print("Genre: "+genre)
        boxes1 = item.find_all("div", class_="latest_book_text")
        for box1 in boxes1:
            names = box1.find_all("div", class_="latest_book_title super_clarendon")
            for name in names:
                name = name.text.strip()
                print("Book Name: "+name)
            authors = box1.find_all("div", class_="latest_book_author")
            for author in authors:
                author = author.text.strip()
                print("Author: "+author)
            reviews = box1.find_all("span", class_="featured_book_review_index")
            for review in reviews:
                review=review.text.strip()
                print("Review: "+review)
                print("")


def bestmovie():

    site = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
    req = requests.get(site).text
    soup = BeautifulSoup(req, 'html5lib')
    items = soup.find_all("tr")
    for item in items:
        boxes1 = item.find_all("td", class_="titleColumn")
        for box1 in boxes1:
            names = box1.find_all("a")
            for name in names:
                name = name.text.strip()
                print(name)
        reviews = item.find_all("td", class_="ratingColumn imdbRating")
        for review in reviews:
            rating = review.text.strip()
            print("IMDb Rating: "+rating)
            print("")


def bestshow():
    site = "https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250"
    req = requests.get(site).text
    soup = BeautifulSoup(req, 'html5lib')
    items = soup.find_all("tr")
    for item in items:
        boxes1 = item.find_all("td", class_="titleColumn")
        for box1 in boxes1:
            names = box1.find_all("a")
            for name in names:
                name = name.text.strip()
                print(name)
        reviews = item.find_all("td", class_="ratingColumn imdbRating")
        for review in reviews:
            rating = review.text.strip()
            print("IMDb Rating: "+rating)
            print("")


def searchmovie():

    moviename = input("Enter the name of movie you want to search for: ")
    words = moviename.split(" ")
    n = len(words)
    if n == 1:
        word = words[0]
    else:
        i = 0
        search = ""
        while i < n - 1:
            search = search + words[i] + "+"
            i = i + 1
        search = search + words[n - 1]
        word = search

    site = "https://www.rottentomatoes.com/search?search=" + word
    req = requests.get(site).text
    soup = BeautifulSoup(req, 'html5lib')
    contents = soup.find_all("search-page-media-row")
    for content in contents:
        items = content.find_all("a", class_="unset")
        for item in items:
            name = item.text.strip()
            print("Name: "+name)
        year = content.get("releaseyear")
        print("Year: "+year)
        cast1 = content.get("cast")
        print("Cast: "+cast1)
        rating = content.get("tomatometerscore")
        print("Tomato Meter Rating: "+rating)
        print("")

def news():
    print('''What types of news do you want to see?
    
1: Search for a particular news topic
2: Trending News
3: Opinion News
4: Tech News
4: Sports News
5: Auto News
6: Education News
7: Business News''')

    inp2 = int(input("Enter your choice: "))
    if inp2 == 1:
        searchnews()
    elif inp2 == 2:
        trendingnews()
    elif inp2 == 3:
        opinionnews()
    elif inp2 == 4:
        technews()
    elif inp2 == 5:
        autonews()
    elif inp2 == 6:
        educationnews()
    elif inp2 == 7:
        businessnews()


def books():
    print('''What types of books reviews do you want to see?

1: Search for a particular book
2: Biggest Books''')

    inp2 = int(input("Enter your choice: "))
    if inp2 == 1:
        searchbook()
    elif inp2 == 2:
        biggestbook()


def movies():
    print('''What types of movie reviews do you want to see?

1: Search for a particular movie
2: Best Movies
3: Best Shows''')

    inp2 = int(input("Enter your choice: "))
    if inp2 == 1:
        searchmovie()
    elif inp2 == 2:
        bestmovie()
    elif inp2 == 3:
        bestshow()

print('''What do you want to search the Internet for

Enter 1 For News
Enter 2 for Books Reviews
Enter 3 for Movies Reviews
''')

inp1 = int(input("Enter your choice: "))
if inp1 == 1:
    news()
elif inp1 == 2:
    books()
elif inp1 == 3:
    movies()