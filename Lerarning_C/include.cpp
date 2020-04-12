/*
	2020年4月12日18:32:27
	include的一些误区

	#include 不是用来引入库的

	stdio.h 里只有printf的原型，printf的代码
	在另外的地方，某个.lib（windows）或者.a（Unix）中

	#include <stdio.h> 只是为了让编译器知道printf()
	函数的原型，

	现在的编译器会默认引入所有的标准库

	在使用和定义这个函数的地方都应该#include 这个头文件

	一般的做法是任何.c 都有对应的同名的.h
	把所有对外公开的函数的原型和全局变量的声明都放进去

	不对外公开的函数

	在函数前面加上static 就使得它成为只能在所在编译单元中被使用
	在全局变量前加上static 就使得它成为智能在所在编译单元使用

	int i; 是变量的定义
	extern int i; 是变量的声明

	声明是不产生代码的：函数原型， 变量声明，结构声明， 宏声明。。。。。
	只有声明可以被放在头文件中
	
	标准头文件结构

	#ifndef _MAX_H_
	#define _MAX_H_

	#include "node.h"

	typedef struct _list
	{
		Node* head;
		Node* tail;
	} List;

	#endif

	运用条件编译和宏，保证这个头文件在一个编译单元中只会被include一次
*/
