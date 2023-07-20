sudo su - postgres, then psql


psql: youtubesplitter


CREATE DATABASE youtubesplitter;
CREATE USER hakosaj WITH PASSWORD 'SECRET';

ALTER ROLE hakosaj SET client_encoding TO 'utf8';
ALTER ROLE hakosah SET default_transaction_isolation TO 'read committed';
ALTER ROLE hakosaj SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE youtubesplitter TO hakosaj;


TD:

youtube splitter vaihe: mieti db configuration. stream get, now download. Have to link video details to the wav file, aloita unsuperivsed, mfcc shapes.

https://towardsdatascience.com/music-genre-classification-with-python-c714d032f0d8
