package sudoku;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;

import cspSolver.Constraint;
import cspSolver.ConstraintNetwork;
import cspSolver.Variable;


public class Converter {

	public static ConstraintNetwork SudokuFileToConstraintNetwork(SudokuFile sf)
	{
		int [][] board = sf.getBoard();

		List<Variable> variables = new ArrayList<Variable>();
		int value = 0;

		for (int i = 0; i < sf.getN(); i++)
		{
			for (int j = 0; j < sf.getN(); j++)
			{
				value = board[i][j];
				List<Integer> domain = new ArrayList<Integer>();

				if (value == 0)
				{
					for (int d = 1; d <= sf.getN(); d++)
					{
						domain.add(d);
					}
				}
				else
				{
					domain.add(value);
				}

				int block = (i/sf.getP() * sf.getP()) + j/sf.getQ();

				variables.add(new Variable(domain, i, j, block));
			}
		}

		Map<Integer, List<Variable>> rows = new HashMap<Integer, List<Variable>>();
		Map<Integer, List<Variable>> cols = new HashMap<Integer, List<Variable>>();
		Map<Integer, List<Variable>> blocks = new HashMap<Integer, List<Variable>>();

		for (Variable v : variables)
		{
			int row = v.row();
			int col = v.col();
			int block = v.block();

			if (!rows.containsKey(row))
			{
				rows.put(row, new ArrayList<Variable>());
			}

			if (!cols.containsKey(col))
			{
				cols.put(col, new ArrayList<Variable>());
			}

			if (!blocks.containsKey(block))
			{
				blocks.put(block, new ArrayList<Variable>());
			}
			rows.get(row).add(v);
			cols.get(col).add(v);
			blocks.get(block).add(v);
		}

		ConstraintNetwork cn = new ConstraintNetwork();

		for (Variable v : variables)
		{
			cn.add(v);
		}

		for (Entry<Integer, List<Variable>> e : rows.entrySet())
		{
			Constraint c = new Constraint();
			for(Variable v : e.getValue())
			{
				c.addVariable(v);
			}
			cn.add(c);
		}

		for (Entry<Integer, List<Variable>> e : cols.entrySet())
		{
			Constraint c = new Constraint();
			for(Variable v : e.getValue())
			{
				c.addVariable(v);
			}
			cn.add(c);
		}

		for (Entry<Integer, List<Variable>> e : blocks.entrySet())
		{
			Constraint c = new Constraint();
			for(Variable v : e.getValue())
			{
				c.addVariable(v);
			}
			cn.add(c);
		}
		return cn;
	}
	
	public static SudokuFile ConstraintNetworkToSudokuFile(ConstraintNetwork cn, int n, int p, int q)
	{
		SudokuFile sf = new SudokuFile();
		int [][] board = new int[n][n];
		int row = 0, col = 0;
		for(Variable v : cn.getVariables())
		{
			board[row++][col] = v.getAssignment();
			if(row == n)
			{
				row = 0;
				col++;
			}
		}
		sf.setBoard(board);
		sf.setN(n);
		sf.setP(p);
		sf.setQ(q);
		return sf;
	}
	
}
