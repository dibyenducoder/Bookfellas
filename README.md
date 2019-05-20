# These are the main features of the website:
- [x] Lets users to search books, genres, and authors (taken from some existing database)
- [x] Let users to register and log in
- [ ] Let user catalog books(into three categories: Is read, has read, wants to read)
- [ ] Let users rate and review books and further comment on these reviews recursively(ie. comments can have further comments)
- [ ] Get recommendations based on reading history
- [ ] Lets users form groups, join groups and chat with other users.

# SOME DJANGO TERMS:

## MODELS
In django, we can create models which are database versions of real-world entities(just like classes, models can have data members and member functions, can be inherited, etc). These models can be related to each other in 3 possible ways:
1. **One-to-one relationship:** This is same as "is-a" relationship or inheritence in OOP(For ex: A model "sports_car" shares a one-to-one relationship with a "car" ).
2. **One-to-many relationship:** Object of model A can be related to many objects of model B, but not the other way round(For ex: An album can have many songs, but a song cannot have multiple albums)
3. **Many-to-many relationship:** Objects of model A can be related to multiples objects of model B, and vice versa(For ex: A band can have multiple singers, a singer can belong to multiple bands; can be recursive also,for ex- a user can have multiple users as followers and can follow multiples users)

## APPS
Apps add modularity to the website. Just like you can break up your C++ code into functions, you can break up a website into apps, each having a different functionality. (For ex- In a college website we might have an admissions app, an exams app, a noticeboard app, etc)

## VIEWS
Each url in a website is linked to a function call, which generally returns an HTML page. These functions are called views.

## TEMPLATES and STATIC
All HTML files are included in a 'templates' folder and all static files(files which are independent of any database; and wont change if database is updated) like CSS files, background image are included in a 'static' folder.
 

# IMPLEMENTATION DETAILS

## MODELS USED:
Book,Author,Genre,User,Review,Comment.

## RELATIONS:
- Book->Author(Many-to-many)
- Book->Genre(Many-to-many)
- Author->Genre(Many-to-many)
- User->Books(Many-to-many)
- Book->Review(One-to-many)
- Review->Comment(One-to-many)
- Comment->Comment(One-to-many)
- User->Review(One-to-many)
- User->Comment(One-to-many)

## APPS:
Only one app is made named 'books'(I tried with 1 app for 1 model but it was becoming messy with so many files per app).

## VIEWS:
As of now, I have made an indexed and detailed view for each of Book, Author and Genre, and also a User profile view and User registration view.

# SOME USEFUL LINKS
[This one](https://docs.djangoproject.com/en/2.2/), [this one](https://tutorial.djangogirls.org/en/) and [this one](https://www.youtube.com/playlist?list=PL6gx4Cwl9DGBlmzzFcLgDhKTTfNLfX1IK)
