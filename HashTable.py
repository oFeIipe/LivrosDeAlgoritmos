class HashMap:
    def __init__(self, size):
        self.size = size
        self.buckets = [[] for i in range(self.size)]

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self._hash(key)
        bucket = self.buckets[index]

        if bucket:
            for i, (k, v) in enumerate(bucket):
                if k == key:
                    bucket[i] = (key, value)
                    return

        bucket.append((key, value))

    def get(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]

        if bucket:
            for i, (k, v) in enumerate(bucket):
                if k == key:
                    return bucket[i]
        return None

    def delete(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]

        if bucket:
            for i, (k, v) in enumerate(bucket):
                if k == key:
                    bucket.pop(i)



hashTeste = HashMap(2)

hashTeste.put("Felipe", 21)
hashTeste.put("Fulanderson", 41)

value = hashTeste.get("Felipe")
hashTeste.delete("Felipe")
