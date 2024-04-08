class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        remains = {i : students.count(i) for i in [0, 1]}
    
        while students:
            # 이번 차례의 샌드위치
            want = sandwiches[0]
        
            if remains[want] != 0:
                idx = students.index(want)
                students = students[idx+1:] + students[:idx]
                sandwiches = sandwiches[1:]
                remains[want] -= 1
            else:
                break
        
        return len(students)
     