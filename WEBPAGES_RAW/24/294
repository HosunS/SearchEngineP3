/*
** line_buffer -- class to provide buffer for line editor
** David Eppstein / Columbia University / 13 Sep 1987
*/

#ifndef LINE_BUFFER_H
#define LINE_BUFFER_H

class line_buffer {
    char * buffer;		// contents being edited
    int bufsize;		// dim of array not length of string
    int buflen;

 public:
    line_buffer();
    ~line_buffer();

    void add_char(char c) {	// speed up file read
	if (buflen + 2 > bufsize) replace(buflen, &c, 1, 0);
	else {
	    buffer[buflen++] = c;
	    buffer[buflen] = '\0';
	}
    }
    virtual int replace(int, const char *, int = -1, int = 0);
    int set_buffer(const char *s, int n = -1) { return replace(0, s, n, -1); }
    const char * text() { return buffer; }
    int textlen() { return buflen; }
};

#endif
