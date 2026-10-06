fellowship = {
    'aragorn', 'gimli', 'legolas', 'gandalf',
    'boromir', 'frodo', 'sam', 'merry', 'pippin'
}

print("fellowship:", fellowship)

fellowship.discard('boromir')
print("fellowship:", fellowship)

fellowship.remove('gandalf')
print("fellowship:", fellowship)