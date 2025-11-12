from vanna.flask import VannaFlaskApp
from vanna.remote import VannaDefault

vn = VannaDefault(model="chinook", api_key="vanna_api_key")
vn.connect_to_sqlite("https://vanna.ai/Chinook.sqlite")
vn.ask("What are the top 10 artists by sales?")
vn.ask("What is the average sales per artist?")
vn.ask("What is the total sales for each genre?")
vn.ask("How many albums are there in the database?")
vn.ask("What are the top-selling albums for each artist?")

VannaFlaskApp(vn).run()
