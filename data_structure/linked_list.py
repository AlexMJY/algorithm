from __future__ import annotations
from typing import Any, Type

class Node:
    # 연결리스트용 노드 클래스
    def __init__(self, data: Any = None, next: Node = None):
        self.data = data
        self.next = next
        
class LinkedList:
    # 연결리스트 클래스
    def __init__(self):
        self.no = 0 # 노드의 개수
        self.head = None # 머리 노드
        self.current = None # 주목 노드
        
    def __len__(self):
        return self.no
    
    def search(self, data):
        cnt = 0
        ptr = self.head
        while ptr is not None:
            if ptr.data == data:
                self.current = ptr
                return cnt
            cnt += 1
            ptr = ptr.next
        return -1

    def __contains__(self, data) -> bool:
        # 연결리스트에 data가 포함되어 있는지 확인
        return self.search(data) >= 0
    
    def add_first(self, data):
        ptr = self.head
        self.head = self.current = Node(data, ptr)
        self.no += 1
        
    def add_last(self, data):
        if self.head is None:
            self.add_first(data)
        else:
            ptr = self.head
            while ptr.next is not None:
                ptr = ptr.next
            ptr.next = self.current = Node(data, None)
            self.no += 1
            
    def remove_first(self):
        if self.head is not None:
            self.head = self.current = self.head.next
        self.no -= 1
        
    def remove_last(self):
        if self.head is not None:
            if self.head.next is None:
                self.remove_first()
            else:
                ptr = self.head
                pre = self.head
                
                while ptr.next is not None:
                    pre = ptr
                    ptr = ptr.next
                pre.next = None
                self.current = pre
                self.no -= 1
                
    def remove(self, p: Node):
        if self.head is not None:
            if p is self.head:
                self.remove_first()
            else:
                ptr = self.head
                
                while ptr.next is not p:
                    ptr = ptr.next
                    if ptr is None:
                        return
                ptr.next = p.next
                self.current = ptr
                self.no -= 1
                
    def remove_current_node(self):
        self.remove(self.current)
        
    def clear(self):
        while self.head is not None:
            self.remove_first()
        self.current = None
        self.no = 0
        
    def next(self):
        # 주목 노드를 한 칸 뒤로 이동
        if self.current is None or self.current.next is None:
            return False
        self.current = self.current.next
        return True
    
    
    def print_current_node(self):
        if self.current is None:
            print("주목 노드가 존재하지 않습니다.")
        else:
            print(self.current.data)
            
    def print(self):
        # 모든 노드 출력
        ptr = self.head
        
        while ptr is not None:
            print(ptr.data)
            ptr = ptr.next
            
    def __iter__(self):
        return LinkedListIterator(self.head)        
    
class LinkedListIterator:
    def __init__(self, head):
        self.current = head
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.next
            return data