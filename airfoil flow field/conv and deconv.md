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
p = k/2=n向下取整，k是奇数  
For any i and for k odd (k = 2n + 1),s=1  
卷积核的大小通常取奇数，步长取为1，此时，输入和输出的图像大小是相同的  
This is sometimes referred to as half (or same) padding  
这也通常被称为半或者相同填充  

Note that half padding also works for even-valued k and for s >1, but in that case the property that the output size is the same as the input size is lost. Some frameworks also implement the same convolution slightly differently  
如果k取偶数并且s大于1,此时输入输出图像大小相同的性质就会消失

Full padding  
While convolving a kernel generally decreases the output size with respect to the input size, sometimes the opposite is required. This can be achieved with proper zero padding  
卷积核通常会减小输出图片的大小相对于输入图片大小来说，但是有时候相反的情况是需要的，这可以通过合适的零填充获得  
For any i and k, and for p = k - 1 and s = 1
o = i+(k-1)  
This is sometimes referred to as full padding, because in this setting every possible partial or complete superimposition of the kernel on the input feature map is taken into account.  
这有时候也被称为全填充  

Transposed convolution arithmetic  
转置卷积  
转置卷积的需要通常源于希望使用在正常卷积的相反方向上进行的变换，即，从具有某种卷积输出形状的某种东西到具有其输入形状的某种东西，同时保持 与所述卷积兼容的连接模式。 例如，可以使用这种变换作为卷积自动编码器的解码层或将特征映射投影到更高维空间。  
Like for convolution arithmetic, the dissertation about transposed convolution arithmetic is simplified by the fact that transposed convolution properties don’t interact across axes.  
与卷积算法一样，关于转置卷积算法的论文通过转置卷积属性不跨轴交互这一事实得以简化。  

Convolution as a matrix operation  
将卷积作为矩阵运算的一种，参考知乎上的回答  
http://deeplearning.net/software/theano_versions/dev/tutorial/conv_arithmetic.html



