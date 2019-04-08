from setting import config

if __name__ == '__main__':
    conf = config['db']
    print(conf)
 #   pool = await aiomysql.create_pool(
 #       host= conf['host'],
 #       user= conf['user'],
 #       password= conf['password'],
 #       db="test",
 #       cursorclass=DictCursor,
 #       loop=loop
 #   )
