# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ReviewsAllocineItem(scrapy.Item):
    actor_even = scrapy.Field() # Le titre du film
    actor_odd = scrapy.Field() # Le commentaire
    actor = scrapy.Field()
    review = scrapy.Field() # La note donnée au film par l'auteur du commentaie
    film = scrapy.Field()
    title = scrapy.Field()

class Film_Info(scrapy.Item):
    film = scrapy.Field()  # Le titre du film
    film_id = scrapy.Field()  # L'id du film sur IMDB'
    director = scrapy.Field() # Le realisateur
    writer = scrapy.Field()  # Le(s) scénariste(s)
    rating_score = scrapy.Field() # Le rating moyen
    rating_amount = scrapy.Field() # Le nombre de rating
    genre = scrapy.Field() # Le(s) genre(s)
    certificate = scrapy.Field() # Le certificat
    parent_guide = scrapy.Field() # Le niveau parental
    release_date = scrapy.Field() # La date de sortie
    origin_country = scrapy.Field() # Le pays d'origine
    budget = scrapy.Field() # Le budget
    box_office_worldwide = scrapy.Field() #Le box-office mondial (jusqu'au moment du scrap)
    box_office_na = scrapy.Field() # Le box-office en amérique du nord (jusqu'au moment du scrap)
    box_office_na_we = scrapy.Field() # Le box office en amérique du nord (le week-end de sortie)
    runtime = scrapy.Field() # La durée du film
    color = scrapy.Field() # Couleur ou noir et blanc
    sound_mix = scrapy.Field() # Le type de sortie sonore
    aspect_ratio = scrapy.Field() # L'aspect ratio du film

class Film_awards(scrapy.Item):
    total_win = scrapy.Field()
    total_nominations = scrapy.Field()

class FilmographyItem(scrapy.Item):
    #role = scrapy.Field()
    film_title = scrapy.Field()
    film_date = scrapy.Field()
    actor = scrapy.Field()
    #film_date_clean = scrapy.Field()
    film_url = scrapy.Field()
    #personage_and_extra_info = scrapy.Field()
    personage_and_extra_info_clean = scrapy.Field()
    job = scrapy.Field()


