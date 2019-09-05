import torch


tp = torch.arange(12, dtype=torch.float).view(3,4)
# tensor([[ 0.,  1.,  2.,  3.],
#         [ 4.,  5.,  6.,  7.],
#         [ 8.,  9., 10., 11.]])
tn = -tp
# tensor([[ -0.,  -1.,  -2.,  -3.],
#         [ -4.,  -5.,  -6.,  -7.],
#         [ -8.,  -9., -10., -11.]])

"torch.cat"

tc0 = torch.cat([tp, tn],dim=0)
# tc0 tensor([[  0.,   1.,   2.,   3.],
#         [  4.,   5.,   6.,   7.],
#         [  8.,   9.,  10.,  11.],
#         [ -0.,  -1.,  -2.,  -3.],
#         [ -4.,  -5.,  -6.,  -7.],
#         [ -8.,  -9., -10., -11.]])

# tc0.size torch.Size([6, 4])
# tc0.dim 2

tc1 = torch.cat(tensors=[tp, tn], dim=1)
# tc1 tensor([[  0.,   1.,   2.,   3.,  -0.,  -1.,  -2.,  -3.],
#         [  4.,   5.,   6.,   7.,  -4.,  -5.,  -6.,  -7.],
#         [  8.,   9.,  10.,  11.,  -8.,  -9., -10., -11.]])
# tc1.size torch.Size([3, 8])

"torch.stack()"
ts0 = torch.stack(tensors=[tp, tn], dim=0)
# ts0 tensor([[[  0.,   1.,   2.,   3.],
#          [  4.,   5.,   6.,   7.],
#          [  8.,   9.,  10.,  11.]],
#
#         [[ -0.,  -1.,  -2.,  -3.],
#          [ -4.,  -5.,  -6.,  -7.],
#          [ -8.,  -9., -10., -11.]]])
# ts0.size torch.Size([2, 3, 4])
# ts0.dim 3

ts1 = torch.stack(tensors=[tp, tn], dim=1)
# ts1 tensor([[[  0.,   1.,   2.,   3.],
#          [ -0.,  -1.,  -2.,  -3.]],
#
#         [[  4.,   5.,   6.,   7.],
#          [ -4.,  -5.,  -6.,  -7.]],
#
#         [[  8.,   9.,  10.,  11.],
#          [ -8.,  -9., -10., -11.]]])
# ts1.size torch.Size([3, 2, 4])
ts2 = torch.stack(tensors=[tp, tn], dim=2)
# tensor([[[  0.,  -0.],
#          [  1.,  -1.],
#          [  2.,  -2.],
#          [  3.,  -3.]],
# 
#         [[  4.,  -4.],
#          [  5.,  -5.],
#          [  6.,  -6.],
#          [  7.,  -7.]],
# 
#         [[  8.,  -8.],
#          [  9.,  -9.],
#          [ 10., -10.],
#          [ 11., -11.]]])
# torch.Size([3, 4, 2])
