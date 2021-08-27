/*
将圆周率的值写入二进制文件再进行读取
*/

#include <stdio.h>

int main(int argc, char const *argv[])
{
	FILE *fp;
	double pi = 3.14159265358979323846;

	printf("get pi from variable PI is %23.21f. \n", pi);

	/*写入操作*/
	if ((fp=fopen("PI.bin", "wb")) == NULL){
		printf("\a file open failed \n");
	}else{
		fwrite(&pi, sizeof(double), 1, fp);   //从pi写入
		fclose(fp);
	}

	/*读取操作*/
	if ((fp = fopen("PI.bin", "rb")) == NULL){
		printf("\a file open failed. \n");
	}else{
		fread(&pi, sizeof(double), 1, fp);    //读取至pi
		printf("read from file the PI is %23.21f. \n", pi);
		fclose(fp);
	}
	return 0;
}


/*
get pi from variable PI is 3.141592653589793100000.
read from file the PI is 3.141592653589793100000.
*/
