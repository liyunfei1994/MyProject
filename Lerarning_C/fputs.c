#include <stdio.h>

int main ()
{
   FILE *fp;

   fp = fopen("file.txt", "w+");

   fputs("This is C.\n", fp);
   fputs("Hello World!", fp);

   fclose(fp);
   
   return(0);
}
