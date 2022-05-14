/*
剑指 Offer 06. 从尾到头打印链表
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。
输入：head = [1,3,2]
输出：[2,3,1]
解题思路
1. 首先遍历整个链表，求出节点个数count
2. 创建一个大小为count的数组
3. 重新遍历链表，并且将其数值赋值给数组
4. 置换数组
*/
int* reversePrint(struct ListNode* head, int* returnSize){
      struct ListNode*p=head;
      int count=0;
      while(p){
          count++;
          p=p->next;
      }
      int *ret=(int*)malloc(sizeof(int)*count);
      *returnSize=count;
      int i=0;
      p=head;
      while(p){
        ret[i++]=p->val;
        p=p->next;
      }
      for(i=0;i<count/2;i++){
            int temp=ret[i];
            ret[i]=ret[count-1-i];
            ret[count-1-i]=temp;
      }
      return ret;
}