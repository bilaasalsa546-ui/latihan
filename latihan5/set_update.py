hobbits = {'frodo', 'sam', 'merry', 'pippin'}
dunedain = {'aragorn'}
elf = {'legolas'}
dwarf = {'gimli'}
human = {'boromir'}
maiar = {'gandalf'}

hobbits.update(dunedain)
hobbits.update(elf)
hobbits.update(dwarf)
hobbits.update(human)
hobbits.update(maiar)

print("hobbits:", hobbits)