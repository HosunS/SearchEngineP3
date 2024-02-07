// lookup - find paragraph containing string in file
// David Eppstein / Columbia University / 11 Feb 1986

// Edit history:
// wormwood:/i0/di/ua/eppstein/public_html/161/lookup/lookup.c, 27 Feb 1996
//   Make this code compile again (C++ has changed between 1988 and now)
//   and strip out some unnecessary junk to make better example for ICS 161
// gar:/u/tom/eppstein/src/match/lookup.c, 29-Jan-1988 12:33:16 by eppstein
//   Rewrite in C++, split out string match code
// garfield:/u/tom/eppstein/src/bin/lookup.c,  2-Oct-1987 13:39:34 by eppstein
//   Add -c case sensitivity, -r print rest of file after match.
// garfield:/usr1/eppstein/src/bin/lookup.c, 12-Dec-1986 16:26:43 by eppstein
//   Save start of paragraph in a buffer instead of using fseek().
//   Stop using getenv("LOOKUP") -- user must always give file.
// garfield:/usr1/eppstein/src/lookup.c, 14-May-1986 16:03:16 by eppstein
//   Treat form feed the same as linefeed (and xlate to lfd on output)
// garfield:/usr1/eppstein/src/lookup.c, 13-Feb-1986 by eppstein
//   Create this file (actually this was done on the DEC20).

#include "match.h"
#include "lineb.h"
#include <stream.h>


// Return the lowercase version of a char; set csense = 0 to disable.

int csense = 'a' - 'A';		// assume case insensitive

inline char casify(char c)
{
    if (c >= 'A' && c <= 'Z') return c + csense;
    else return c;
}


// Read char into variable, returning nz if end of line or end of page.

inline int eolgetc(char & v, istream & i)
{
    i.get(v);
    return (!i.eof() && (v == '\n' || v == '\014'));
}

// Add a char to the save buffer.

inline void reset(line_buffer & lb) { lb.set_buffer(0); }
void add(line_buffer & lb, char c)  { lb.replace(lb.textlen(), &c, 1, 0); }

// Complain about inappropriate args

extern "C" void exit(int);

const char * progname = "lookup";

void usage()
{
    cerr << "usage: " << progname << "[-cr] word < file\n";
    exit (1);
}


// Do the search.
//
// The outer loop procedes a line at a time, and the inner one a
// character at a time.  When we find a match, we go back to the
// last paragraph break, print up to the next paragraph break,
// and continue the line-at-a-time loop from there.

int rest = 0;			// nonzero means print whole file after match
int first_para = 1;		// zero when a para has already been output

void
process(istream & in, string_match & target)
{
    line_buffer para;
    int was_eol = 1;
    target.reset();

    while (!in.eof()) {		// looping over chars in file
	char inchar;
	if (eolgetc(inchar, in)) { // end of line?
	    target.reset();	// match does not extend over line
	    if (was_eol) reset(para); // two newlines, para break
	    else {
		was_eol = 1;	// one newline, remember the next
		add(para,'\n'); // but assume internal to para for now
	    }
	    continue;		// back to top of loop
	}
	if (in.eof()) return;	// maybe eolgetc() above hit eof?
	was_eol = 0;		// if we got here, have non-line-break char

	if (!target.match(casify(inchar))) add(para, inchar);
	else {

	    // Here when we found a complete match.
	    //
	    // We print the paragraph it occurs in, including the parts
	    // before it, and move on to the start of the next paragraph.

	    if (first_para) first_para = 0;
	    else cout.put('\n');

	    cout << para.text(); // first send text before match
	    cout.put(inchar); // then end of match itself
	    while (!in.eof()) { // then previously unread part
		if (eolgetc (inchar, in) && !rest) {
		    cout.put('\n');	// maybe start of para break, copy
		    if (eolgetc (inchar, in)) break; // and test again
		}
		cout.put(inchar);	// send char after nl or non-nl char
	    }
	    reset(para);	// now at paragraph break
	    was_eol = 1;	// flush any further newlines
	}			// end code for matched target
    }				// end loop over chars in line
}


// The main program.

main (int argc, char ** argv)
{
    // If we have enough args, first arg might be flags.
    // Read and process them.  Currently defined flags:
    //  -c  turn on case sensitivity
    //  -r  print whole rest of file after a match

    if (argc == 0) usage();
    progname = argv[0];
    while (argc > 2 && argv[1][0] == '-') {
	argc--;
	const char * cp = *++argv;
	while (*++cp != '\0') switch (*cp) {
	case 'c':
	    csense = 0;
	    break;

	case 'r':
	    rest = 1;
	    break;

	default:
	    usage();
	}
    }
    if (argc != 2) usage();

    // Get target string, casify it, and make a string matcher.

    for (char * cp = argv[1]; *cp != '\0'; cp++) *cp = casify(*cp);
    string_match target(argv[1]);

    // Process standard input.
    process(cin, target);
}
