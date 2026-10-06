fellowship = {
    'aragorn', 'gimli', 'legolas', 'gandalf',
    'boromir', 'frodo', 'sam', 'merry', 'pippin'
}

hobbits = {'frodo', 'sam', 'merry', 'pippin', 'bilbo'}

res = fellowship.intersection(hobbits)
print("res:", res)