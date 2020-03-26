import os

class Development():
 SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:admin@127.0.0.1:5432/sales_demo'
 SECCRET_KEY='abcd087'
 DEBUG = True
 JWT_SECRET_KEY = 'GHJKHA!#H67'

class Production():
 SQLALCHEMY_DATABASE_URI = 'postgres://rvidlaydphywgb:5ee796e24b69c26072f1a1bb3d76dd82c60a61be2a97b4df791f78e551146cc7@ec2-46-137-91-216.eu-west-1.compute.amazonaws.com:5432/dh3k70smcrjnd'
 SECRET_KEY = 'fc0413eae060c46c0b2fcff8aaa24ec9'
 DEBUG = False

 JWT_SECRET_KEY='GHJKHA!#H67'