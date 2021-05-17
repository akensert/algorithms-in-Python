

class SimpleHashTable:
    """
    Implements a very simple hash table. Could be said to avoid collisions
    via chaining.
    """
    def __init__(self, num_buckets=1000):
        self.num_buckets = num_buckets
        self.data = [[] for _ in range(self.num_buckets)]
        self.occupied_buckets = set() # only for __repr__

    def _hashing(self, key):
        return sum(ord(k) for k in str(key))

    def _compression(self, hash_code):
        return hash_code % self.num_buckets

    def _delete_if_exists(self, bucket_idx, key):
        bucket_length = len(self.data[bucket_idx])
        for i in range(bucket_length):
            if self.data[bucket_idx][i][0] == key:
                del self.data[bucket_idx][i]
        if bucket_length == 1: # only for __repr__
            self.occupied_buckets.remove(bucket_idx) # only for __repr__

    def __getitem__(self, key):
        bucket_idx = self._compression(self._hashing(key))
        for item in self.data[bucket_idx]:
            if item[0] == key:
                return item[1]
        return None

    def __setitem__(self, key, value):
        bucket_idx = self._compression(self._hashing(key))
        self._delete_if_exists(bucket_idx, key)
        self.data[bucket_idx].append((key, value))
        self.occupied_buckets.add(bucket_idx) # only for __repr__

    def __delitem__(self, key):
        bucket_idx = self._compression(self._hashing(key))
        self._delete_if_exists(bucket_idx, key)

    def __repr__(self):
        output = '{\n'
        for bucket_idx in self.occupied_buckets:
            for item in self.data[bucket_idx]:
                output += f'{item[0]!r}: {item[1]!r},\n'
            if len(output) > 100: # set limit at 100 characters
                output += '...\n'
                break
        return output + '}'


if __name__ == '__main__':

    hash_table = SimpleHashTable()

    hash_table['foo'] = 3.14
    hash_table['bar'] = 42
    hash_table[3.14] = 'Jane'
    hash_table[0] = 'Joe'
    hash_table['hello world'] = 'foo bar'

    print(hash_table)
