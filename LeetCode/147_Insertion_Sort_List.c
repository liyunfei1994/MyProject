/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* insertionSortList(struct ListNode* head){
    if(head == NULL)                                                        //链表为空
        return NULL;
    
    struct ListNode* L = (struct ListNode*)malloc(sizeof(struct ListNode)); //辅助结点
    L->next = head;
    struct ListNode *cur = head->next, *pre = head, *tmp;

    while(cur != NULL){                                                     //遍历链表
        if(cur->val >= pre->val){                                           //寻找需要向前插入的结点
        //如果后一个元素比前一个元素大，则cur和pre就全都后移一位
            cur = cur->next;
            pre = pre->next;
        }else{
            //如果后一个元素比前一个元素小，则需要移动
            tmp = L;
            while(tmp->next->val < cur->val)                                //寻找插入位置
                tmp = tmp->next;
            //cur前面的元素要指向cur后面的元素
            pre->next = cur->next;                                          //进行插入
            //cur要指向pre
            cur->next = tmp->next;
            //此时cur成了第一个元素，tmp要指向cur
            tmp->next = cur;
            //新的cur，pre的后一个元素
            cur = pre->next;
            //全部操作完一遍，cur和pre全部后移一位
        }
    }

    return L->next;
}
