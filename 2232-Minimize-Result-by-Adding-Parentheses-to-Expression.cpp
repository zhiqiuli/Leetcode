class Solution {
public:
    string minimizeResult(string expression) {
        int index = expression.find("+");
        string exp_part1 = expression.substr(0, index);
        string exp_part2 = expression.substr(index + 1, expression.length() - index);

        int min_val = INT_MAX;
        string min_res = "";

        for (int i = 0; i < exp_part1.length(); i++) {
            for (int j = 1; j < exp_part2.length() + 1; j++) {
                string key =         exp_part1.substr(0, i) + "(" + exp_part1.substr(i, exp_part1.length() - i) \
                             + "+" + exp_part2.substr(0, j) + ")" + exp_part2.substr(j, exp_part2.length() - j);
                int val = evaluate(key);

                if (val < min_val) {
                    min_val = val;
                    min_res = key;
                }
            }
        }

        return min_res;
    }

    int evaluate(string expression) {
        int index1 = expression.find("(");
        int index2 = expression.find("+");
        int index3 = expression.find(")");

        string a1_str = expression.substr(0, index1);
        string a2_str = expression.substr(index1 + 1, index2 - index1 - 1);
        string a3_str = expression.substr(index2 + 1, index3 - index2 - 1);
        string a4_str = expression.substr(index3 + 1, expression.length() - index3 - 1);

        int a1;
        int a2 = stoi(a2_str);
        int a3 = stoi(a3_str);
        int a4;

        if (a1_str.length() == 0) {
            a1 = 1;
        } else {
            a1 = stoi(a1_str);
        }
    
        if (a4_str.length() == 0) {
            a4 = 1;
        } else {
            a4 = stoi(a4_str);
        }

        return a1 * (a2 + a3) * a4;
    }
};
