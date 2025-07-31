import redis
r = redis.Redis()

def get_cached_answer(query):
    cached = r.get(query)
    if cached:
        return cached.decode("utf-8")
    return None

def cache_answer(query, answer):
    r.set(query, answer)

