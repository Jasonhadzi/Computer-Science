#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 22:34:38 2020

Create a marketplace for people and organizations to buy and sell pieces of art!

In this project we’ll be developing classes and objects that represent the various responsibilities of art dealership software.
@author: jasonhadzikostas
"""

class Art:
  def __init__(self, artist, title, medium, year, owner):
    self.artist = artist
    self.title = title
    self.medium = medium
    self.year = year
    self.owner = owner
  def __repr__(self):
    return "{name}. '{title}'. {year}, {medium}. {owner_name}, {owner_location}".format(name = self.artist, title=self.title, year = self.year, medium = self.medium,owner_name=self.owner.name,owner_location = self.owner.location  )


class Marketplace:
  def __init__(self):
    self.listings = []
  def add_listing(self, new_listing):
    self.listings.append(new_listing)
  def remove_listing(self, expired_listing):
    self.listings.remove(expired_listing)
  def show_listings(self):
    for listing in self.listings:
      print(listing)

  
class Listing:
  def __init__(self,art,price,seller):
    self.art = art
    self.price = price
    self.seller = seller
  def __repr__(self):
    return "{name}, {price}".format(name=self.art.title, price=self.price)


class Client:
  def __init__(self,name,location,is_museum):
    self.name =name
    self.is_museum = is_museum
    if is_museum:
      self.location = location
    else:
      self.location = 'Private Collector'
  def sell_artwork(self,artwork,price):
    ##A method cannot know what names we will give to its class instances, that is why it always uses self as the context variable to identify the current owner instance of the method.
    if artwork.owner == self:
      new_listing = Listing(artwork,price,self)
      veneer.add_listing(new_listing)

  def buy_artwork(self,artwork):
    if artwork.owner !=self:
      art_listing = None
      for listing in veneer.listings:
        if listing.art == artwork:
          art_listing = listing
          #we add break for optimisation, once it finds a match it will stop searching. we save time
          break
      if art_listing != None:
        art_listing.art.owner = self
        veneer.remove_listing(art_listing)

veneer = Marketplace()

edytta = Client('Edytta Halpirt',None,False)

moma = Client('The MOMA','New York',True)
#print(veneer.show_listings())

girl_with_mandolin = Art('Picasso, Pablo',"Girl with a Mandolin",1910,"oil on canvas",edytta)
#print(girl_with_mandolin)

edytta.sell_artwork(girl_with_mandolin, '$6M (USD)')
print(girl_with_mandolin)
veneer.show_listings()
moma.buy_artwork(girl_with_mandolin)
print(girl_with_mandolin)
veneer.show_listings()
