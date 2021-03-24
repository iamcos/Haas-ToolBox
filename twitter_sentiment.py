import twint

c = twint.Config()

c.Search = "data science"
# Custom output format
c.Format = "Username: {username} |  Tweet: {tweet}"
c.Limit = 1
c.Pandas = True
twint.run.Search(c)