from birdy.twitter import AppClient
from sqlalchemy import create_engine
from models import Source, Mention, Base
from sqlalchemy.orm import sessionmaker
import datetime

engine = create_engine('sqlite:///sqlite.db')
Session = sessionmaker(bind=engine)

CONSUMER_KEY='ygHMdyqI5Rp5U8ocszeg'
CONSUMER_SECRET='Z1inuYmTC53Fnf6Pv5KDlhhYB8iDXICDefjPwzLBQ'
client = AppClient(CONSUMER_KEY,CONSUMER_SECRET)
access_token=client.get_access_token()
QUERIES=['oprah','einstein']

def get_twitter_mentions():
    """Return the number of new mentions found on Twitter."""
    statuses = []
    for query in QUERIES:
        response = client.api.search.tweets.get(q=query, count=10)
        statuses += response.data.statuses
    session = Session()
    twitter = session.query(Source).get(1)
    new_mentions = 0
    for status in statuses:
        print status
        if not session.query(Mention).filter(Mention.domain_id==status.id_str).count():
            created_at = datetime.datetime.strptime(status.created_at, r"%a %b %d %H:%M:%S +0000 %Y")
            m = Mention(text=status.text,
                    associated_user='{} ({})'.format(status.user.screen_name,
                        status.user.followers_count),
                        recorded_at=datetime.datetime.now(),
                        occurred_at=created_at,
                        source=twitter,
                        domain_id=status.id_str)
            new_mentions += 1
            session.add(m)
    session.commit()
    print new_mentions
    return new_mentions

get_twitter_mentions()