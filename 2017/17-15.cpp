int main(){

  //-----Inputs
  long f0 = 722;
  long f1 = 354;
  //-------
  
  long d = 2147483647;
  long ct = 0;
  long a = 16807;
  long b = 48271;
  long mor = 65536;
  
  for (int i=0; i< 40000000; i++) 
  {
    f0 = (a*f0)%d;
    f1 = (b*f1)%d;
    if ((f0%mor) == (f1%mor))
         ct++;
  }
  printf("part 1 - %ld \n", ct);
  f0 = 722;
  f1 = 354;
  ct = 0;
  for (int i=0; i < 5000000; i++) 
  {
  		f0 = (a*f0)%d;
  	 	while(f0%4!=0)
	   		f0 = (a*f0)%d;
	   	f1 = (b*f1)%d;
  	 	while(f1%8!=0)
	   		f1 = (b*f1)%d;
    	if ((f0%mor) == (f1%mor)) ct++;
   }
   printf("part 2 - %ld ", ct);
}
