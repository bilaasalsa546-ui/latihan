fellowship = {
    'aragorn', 'gimli', 'legolas', 'gandalf',
    'boromir', 'frodo', 'sam', 'merry', 'pippin'
}

hobbits = {'frodo', 'sam', 'merry', 'pippin', 'bilbo'}

fellowship.difference_update(hobbits)
print("fellowship:", fellowship)