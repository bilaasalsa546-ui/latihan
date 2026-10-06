fellowship = {
    'aragorn', 'gimli', 'legolas', 'gandalf',
    'boromir', 'frodo', 'sam', 'merry', 'pippin'
}

hobbits = {'frodo', 'sam', 'merry', 'pippin', 'bilbo'}

diff = fellowship.difference(hobbits)
print("diff:", diff)