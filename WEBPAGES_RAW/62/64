// ConnectDoc.h : interface of the CConnectDoc class
//
/////////////////////////////////////////////////////////////////////////////

#if !defined(AFX_CONNECTDOC_H__10677EA6_AD29_11D1_B3B2_004F49017471__INCLUDED_)
#define AFX_CONNECTDOC_H__10677EA6_AD29_11D1_B3B2_004F49017471__INCLUDED_

#if _MSC_VER >= 1000
#pragma once
#endif // _MSC_VER >= 1000

// Definitions from the ConnectK class
#define BLANK ' '
#define X     'X'
#define O     'O'
#define WIN_X   1000000
#define WIN_O   -1000000
#define MAX_HEURISTIC 1000000
#define MIN_HEURISTIC -1000000

typedef char * CharArray;
typedef CharArray * CharArrayArray; 
// End definitions from the ConnectK class

class CConnectDoc : public CDocument
{
protected: // create from serialization only
	CConnectDoc();
	DECLARE_DYNCREATE(CConnectDoc)

// Attributes
public:
	char mark;
	char playersmark;
	int numMoves;
	ConnectK* ck;

	bool playersMove;
	long seconds;

	long humanSeconds;
	long computerSeconds;

	CTime currTime1;
	CTime currTime2;
	CTimeSpan humanTime;
	CTimeSpan compTime;

	int M;
	int N;
	int K;
	bool G;
	int depthLevel;

// Variables imported from the ConnectK class
	char computerMark;  // mark played by AI player for board evaluation

	CharArrayArray board;    // board is index by [row][column]
	int numOccupied;
// end variables imported from the ConnectK class


	// added for tournament
	int m_nPlayerNumber;



// Operations
public:
	void GameOverCheck();
	bool ComputerMove(int row, int col);
	bool PlayerMove(int row, int col);

// Overrides
	// ClassWizard generated virtual function overrides
	//{{AFX_VIRTUAL(CConnectDoc)
	public:
	virtual BOOL OnNewDocument();
	virtual void Serialize(CArchive& ar);
	//}}AFX_VIRTUAL

// Implementation
public:
	void GameLog(CString currentCompetitor, int x, int y);
	void deleteBoard();
	bool isOccupied(int row, int col);
	bool inRange(int row, int col);
	bool isMarkGood(char mark);
	long evaluate();
	char at(int row, int col);
	bool occupy(int row, int col, char mark);
	bool tie();
	bool win(char &mark);
	void newBoard();
	void OnResetGame();
	virtual ~CConnectDoc();
#ifdef _DEBUG
	virtual void AssertValid() const;
	virtual void Dump(CDumpContext& dc) const;
#endif

protected:

// Generated message map functions
protected:
	//{{AFX_MSG(CConnectDoc)
	afx_msg void OnFileNewgame();
	//}}AFX_MSG
	DECLARE_MESSAGE_MAP()
};

/////////////////////////////////////////////////////////////////////////////

//{{AFX_INSERT_LOCATION}}
// Microsoft Developer Studio will insert additional declarations immediately before the previous line.

#endif // !defined(AFX_CONNECTDOC_H__10677EA6_AD29_11D1_B3B2_004F49017471__INCLUDED_)
