/*
** line_buffer -- class to display buffer for line editor
** David Eppstein / Columbia University / 13 Sep 1987
*/

#include "lineb.h"
#include <string.h>

static const int bufsize_incr = 256;

/*
** Initialize data structures; clean up when done
*/

line_buffer::line_buffer()
{
    buffer = 0;			// let replace() actually alloc buffer
    bufsize = 0;
    buflen = 0;
}

line_buffer::~line_buffer()
{
    delete buffer;
}

/*
** Replace a substring of the buffer with some other substring.
** Return value is nonzero on error.  Length arguments are as
** for save_string; the default is to insert the string at the
** current position without overwriting any old text.
**
** The cursor is left at the end of the replaced text.
*/

int
line_buffer::replace(int start, const char * s, int len = -1, int oldlen = 0)
{
    if (s == 0) len = 0;
    else if (len < 0) len = strlen(s);
    if (oldlen < 0) {
	if (buffer == 0) oldlen = 0;
	else oldlen = strlen(buffer + start);
    }

    // make sure buffer is big enough for the change
    if (buflen + len + 1 - oldlen > bufsize) {
	char *newbuf = new char[buflen + len + 1 - oldlen + bufsize_incr];
	if (newbuf == 0) return 1; // out of memory
	if (buflen != 0) memcpy(newbuf, buffer, buflen);
	newbuf[buflen] = '\0';
	delete buffer;
	buffer = newbuf;
	bufsize = buflen + len + 1 - oldlen + bufsize_incr;
    }

    if (oldlen < len) {		// replacement longer, raise rest of buffer
	for (int i = buflen; i >= start + oldlen; i--)
	    buffer[i + len - oldlen] = buffer[i];
    } else if (oldlen > len) {	// replacement shorter, drop rest of buffer
	for (int i = start + oldlen; i <= buflen; i++)
	    buffer[i + len - oldlen] = buffer[i];
    }
    if (len != 0) memcpy(buffer+start, s, len); // drop new text in
    buflen += len - oldlen;
    return 0;
}
