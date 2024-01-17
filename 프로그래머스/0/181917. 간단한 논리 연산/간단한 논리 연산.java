class Solution {
    public boolean solution(boolean x1, boolean x2, boolean x3, boolean x4) {
        boolean xx1;
        boolean xx2;
        if (x1 == true || x2 == true) {
            xx1 = true;
        } else {
            xx1 = false;
        }
        if (x3 == true || x4 == true) {
            xx2 = true;
        }
        else {
            xx2 = false;
        }
        
        if (xx1 == true && xx2 == true) {
            return true;
        } else if (xx1 == false && xx2 == false) {
            return false;
        } else {
            return false;
        }
        
    }
}