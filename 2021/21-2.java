package net.codejava;

import java.io.File;
import java.io.FileNotFoundException;  // Import this class to handle errors
import java.util.Scanner; // Import the Scanner class to read text files

public class AOC {

	public static void main(String[] args) {		
		int x = 0; int y = 0; int y2 = 0; int aim = 0;
		try 
		{
			File myObj = new File("21-2.txt");
			Scanner myReader = new Scanner(myObj);
			
		    while (myReader.hasNextLine()) 
		    {
		          String data[] = myReader.nextLine().split(" ");
		          if(data[0].indexOf("forward") != -1)
		          {
		        	  x += Integer.valueOf(data[1]);
		          	  y2 += aim * Integer.valueOf(data[1]);
		          }
		          if(data[0].indexOf("down") != -1)
		          {
		        	  y += Integer.valueOf(data[1]);
		          	  aim += Integer.valueOf(data[1]);
		          }
		          if(data[0].indexOf("up") != -1)
		          {
		        	  y -= Integer.valueOf(data[1]);
		          	  aim -= Integer.valueOf(data[1]);
		          }
		    }
		    System.out.println("part 1 - " + x*y);
		    System.out.println("part 2 - " + x*y2);
		}		
		catch (FileNotFoundException e) 
		{
		      System.out.println("An error occurred.");
		      e.printStackTrace();
		}
	}
}
