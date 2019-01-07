对卷积和转置卷积的一些新的学习  
A convolutional layer’s output shape is affected by the shape of its input as well as the choice of kernel shape, zero padding and strides, and the relationship between these properties is not trivial to infer.  
一个卷积层的输出的形状是由多种因素影响的，包括输入的形状，卷积核的形状，零填充，步长，这些性质之间的关系并不是微不足道不重要的  
This contrasts with fully-connected layers, whose output size is independent of the input size.   
这与全连接层形成了鲜明的对比，全连接层的输出形状与输入的形状是独立的。  

Refresher: discrete convolutions  
 补习课程，离散卷积  
 Images, sound clips and many other similar kinds of data have an intrinsic structure. More formally, they share these important properties:  
 图片、声音片段或者其他相似的数据，都有一个本质的结构，共同拥有如下重要的性质  
 They are stored as multi-dimensional arrays.  
 都被存储为高维的数组  
They feature one or more axes for which ordering matters (e.g., width and height axes for an image, time axis for a sound clip).  
它们具有一个或多个轴，其排序很重要（例如，图像的宽度和高度轴，声音剪辑的时间轴）。  
One axis, called the channel axis, is used to access different views of the data (e.g., the red, green and blue channels of a color image, or the left and right channels of a stereo audio track).  
一个轴（称为通道轴）用于访问数据的不同视图（例如，彩色图像的红色，绿色和蓝色通道，或立体声音轨的左右通道）。  
A discrete convolution is a linear transformation that preserves this notion of ordering. It is sparse (only a few input units contribute to a given output unit) and reuses parameters (the same weights are applied to multiple locations in the input).  
离散卷积是一种线性变换，它保留了这种排序概念。 它是稀疏的（只有少数输入单元对给定的输出单元有贡献）并重用参数（相同的权重应用于输入中的多个位置）。  
这就是所谓的稀疏矩阵和权值共享  

No zero padding, unit step  
o为输出图形的大小， i为输入图形的大小，k为卷积核的大小  
o = (i-k)+1  

zero padding, unit step  
p为周围填充的0的个数
o = (i-k)+2p+1  
Half(same) padding  
Having the output size be the same as the input size (i.e., o = i) can be a desirable property:  
输入和输出的图像大小是相同的  
p = k/2向下取整，k是奇数  
For any i and for k odd (k = 2n + 1, \quad n \in
\mathbb{N}), s = 1 and p = \lfloor k / 2 \rfloor = n


