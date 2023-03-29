# numbers, hand = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"	#"LRLLLRLLRRL"
numbers, hand = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],	"left"	#"LRLLRRLLLRR"
# numbers, hand = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],	"right"	#"LLRLLRLLRL"
def location(handNumber, nextNumber):
    phone = {1:[0,0], 2:[1,0], 3:[2,0], 
             4:[0,1], 5:[1,1], 6:[2,1], 
             7:[0,2], 8:[1,2], 9:[2,2], 
             '*':[0,3], 0:[1,3], '#':[2,3]}
    x1,y1 = phone[handNumber]
    x2,y2 = phone[nextNumber]
    return abs(x1-x2)+abs(y1-y2)

def solution(numbers, hand):
    leftHand, rightHand = '*', '#'
    answer = ''
    for number in numbers:
        if number==1 or number==4 or number==7 or number=='*':
            answer+='L'
            leftHand = number
        elif number==3 or number==6 or number==9 or number=='#':
            answer+='R'
            rightHand = number
        elif number==2 or number==5 or number==8 or number==0:
            leftDistance = location(leftHand, number)
            rightDistance = location(rightHand, number)
            if leftDistance < rightDistance:
                answer+='L'
                leftHand = number
            elif rightDistance < leftDistance:
                answer+='R'
                rightHand = number
            elif rightDistance == leftDistance:
                if hand == 'right':
                    answer+='R'
                    rightHand = number
                else: 
                    answer+='L'
                    leftHand = number
    return answer
solution(numbers, hand)
