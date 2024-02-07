OBJECTS = lineb.o lookup.o match.o

.c.o:
	g++ -c -O -finline-functions $*.c

lookup: $(OBJECTS)
	g++ $(OBJECTS)
	cp a.out lookup
	rm a.out
make:
	makemake +g++ -O -finline-functions lookup

lineb.o: lineb.c lineb.h
lookup.o: lineb.h lookup.c match.h
match.o: match.c match.h
