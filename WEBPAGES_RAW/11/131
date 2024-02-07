// ConnectView.h : interface of the CConnectView class
//
/////////////////////////////////////////////////////////////////////////////

#if !defined(AFX_CONNECTVIEW_H__10677EA8_AD29_11D1_B3B2_004F49017471__INCLUDED_)
#define AFX_CONNECTVIEW_H__10677EA8_AD29_11D1_B3B2_004F49017471__INCLUDED_

#if _MSC_VER >= 1000
#pragma once
#endif // _MSC_VER >= 1000

class CConnectView : public CFormView
{
protected: // create from serialization only
	CConnectView();
	DECLARE_DYNCREATE(CConnectView)

public:
	//{{AFX_DATA(CConnectView)
	enum{ IDD = IDD_CONNECT_FORM };
		// NOTE: the ClassWizard will add data members here
	//}}AFX_DATA

// Attributes
public:
	CConnectDoc* GetDocument();

	CPoint movePoint;

	CBitmap human;
	CBitmap computer;
	CDC dcMemHuman;
	CDC dcMemComputer;

	BITMAP bmHuman;
	BITMAP bmComputer;

	CClientDC* m_pClientDC;

// Operations
public:

// Overrides
	// ClassWizard generated virtual function overrides
	//{{AFX_VIRTUAL(CConnectView)
	public:
	virtual BOOL PreCreateWindow(CREATESTRUCT& cs);
	virtual void OnInitialUpdate();
	protected:
	virtual void DoDataExchange(CDataExchange* pDX);    // DDX/DDV support
	virtual BOOL OnPreparePrinting(CPrintInfo* pInfo);
	virtual void OnBeginPrinting(CDC* pDC, CPrintInfo* pInfo);
	virtual void OnEndPrinting(CDC* pDC, CPrintInfo* pInfo);
	virtual void OnPrint(CDC* pDC, CPrintInfo*);
	virtual void OnDraw(CDC* pDC);
	//}}AFX_VIRTUAL

// Implementation
public:
	void DrawBoard();
	virtual ~CConnectView();
#ifdef _DEBUG
	virtual void AssertValid() const;
	virtual void Dump(CDumpContext& dc) const;
#endif

protected:

// Generated message map functions
protected:
	//{{AFX_MSG(CConnectView)
	afx_msg void OnLButtonUp(UINT nFlags, CPoint point);
	afx_msg void OnButtonQuit();
	afx_msg void OnButtonNew();
	afx_msg void OnButtonReset();
	afx_msg void OnFileRestart();
	afx_msg void OnFileGamelog();
	//}}AFX_MSG
	afx_msg LRESULT OnPlayerOneMessage(WPARAM wParam, LPARAM lParam);
	afx_msg LRESULT OnPlayerTwoMessage(WPARAM wParam, LPARAM lParam);
	afx_msg LRESULT OnPlayerOneInitMessage(WPARAM wParam, LPARAM lParam);
	afx_msg LRESULT OnPlayerTwoInitMessage(WPARAM wParam, LPARAM lParam);


	DECLARE_MESSAGE_MAP()
};

#ifndef _DEBUG  // debug version in ConnectView.cpp
inline CConnectDoc* CConnectView::GetDocument()
   { return (CConnectDoc*)m_pDocument; }
#endif

/////////////////////////////////////////////////////////////////////////////

//{{AFX_INSERT_LOCATION}}
// Microsoft Developer Studio will insert additional declarations immediately before the previous line.

#endif // !defined(AFX_CONNECTVIEW_H__10677EA8_AD29_11D1_B3B2_004F49017471__INCLUDED_)
