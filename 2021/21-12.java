package net.codejava;

import java.io.File;
import java.io.FileNotFoundException;  // Import this class to handle errors
import java.util.Scanner; // Import the Scanner class to read text files
import java.util.List;
import java.util.ArrayList;
import java.util.*;


public class AdventofCode {

    static int mv(String op, Hashtable<String, Integer> smdict, 
    		Integer depth, List<String> pl, List<String> sts, 
    		List<String> ends, String path,Integer pt) 
    {    	
    	Integer ct = 0;
    	for(int i = 0; i < pl.size();i++)
    		if(smdict.get(pl.get(i)) > 1 )
    			ct++;
    	if(ct > 1)
    		return 0;
    	if(op.indexOf("end") != -1)    	
    		return 1;    		
    	if((op.indexOf("start") != -1) && (depth != 0))    	    		
    		return 0;    	
    	int tkc = 0;
    	for(int i = 0; i < sts.size();i++)
    	{    		
    		if (sts.get(i).indexOf(op) != -1)
    		{    		
    			if (smdict.get(op) < pt)
    			{    		
    				Hashtable<String, Integer> nsmdict = new Hashtable<String, Integer>();
    				nsmdict = (Hashtable<String, Integer>) smdict.clone();    				
    				nsmdict.put(op, nsmdict.get(op) + 1);
    				tkc += mv(ends.get(i), nsmdict, depth+1, pl, sts, ends, path + ", " + op,pt);
    			}
    		}
    	}
    	return tkc;    
	}

	public static void main(String[] args) 
	{		
		try 
		{
			File myObj = new File("21-12.txt");
			Scanner myReader = new Scanner(myObj);
			List<String> sts = new ArrayList<>();
			List<String> ends = new ArrayList<>();			
		    while (myReader.hasNextLine()) 
		    {
		    	String data[] = myReader.nextLine().split("-");
		    	sts.add(data[0].toString());
		    	ends.add(data[1].toString());
		    	sts.add(data[1].toString());
		    	ends.add(data[0].toString());
		    }		    
		    List<String> pl = new ArrayList<>();
		    Hashtable<String, Integer> smdict = new Hashtable<String, Integer>();
		    for(int i = 0; i<sts.size();i++)
		    	if (!pl.contains(sts.get(i)))
		    	{
		    		pl.add(sts.get(i));
		    		char lt = sts.get(i).charAt(0);
		    		if((lt >= 'a') && (lt <= 'z'))
		    			smdict.put(sts.get(i), 0);	
		    		else smdict.put(sts.get(i), -100000);
		    	}				    		    
		    System.out.println("Part 1 - " + mv("start", smdict,0,pl,sts,ends,"",1));
		    System.out.println("Part 2 - " + mv("start", smdict,0,pl,sts,ends,"",2));
	    
		}		
		catch (FileNotFoundException e) 
		{
		      System.out.println("An error occurred.");
		      e.printStackTrace();
		}
	}
}
