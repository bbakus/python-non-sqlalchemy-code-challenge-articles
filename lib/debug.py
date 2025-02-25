#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    author_1 = Author("Kentaro Miura")
    author_2 = Author("Johnny Knoxville")
    author_3 = Author("Donna Summers")

    article_2 = Article("Kentaro Miura", "Vogue", "Berserk")
    article_3 = Article("Johnny Knoxville", "Elle", "Booze n shit")
    article_4 = Article("Donna Summers", "Home Cooking", "Turkey Legs")

    magazine_1 = Magazine("Vogue", "Dark Fantasy")
    magazine_2 = Magazine("Elle", "Gossip")
    magazine_3 = Magazine("Home Cooking", "Lifestyle")

    # don't remove this line, it's for debugging!
    ipdb.set_trace()
