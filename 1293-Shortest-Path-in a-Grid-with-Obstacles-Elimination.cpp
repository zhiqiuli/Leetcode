class Solution {
public:
    /**
     * @param grid: a list of list
     * @param k: an integer
     * @return: Return the minimum number of steps to walk
     */
    int dx[4] = {1, 0, -1, 0};
    int dy[4] = {0, 1, 0, -1};
    int shortestPath(vector<vector<int>> &grid, int k) {
        int m = grid.size(), n = grid[0].size();
        if (m == 1 && n == 1) return 0;

        set<int> visited;
        visited.insert(code(0,0,k));
        queue<int> q;
        q.push(code(0,0,k));

        int step = 0;
        while (!q.empty()){
            step++;
            int cnt = q.size();
            for (int _ = 0; _ < cnt; _ ++) {
                int x, y, rest;
                decode(q.front(), &x, &y, &rest);
                q.pop();
                for (int k = 0; k < 4; k += 1){
                    int nx = x + dx[k];
                    int ny = y + dy[k];
                    // within the grid
                    if (0 <= nx && nx < m && 0 <= ny && ny < n){
                        if (grid[nx][ny] == 0 && visited.count(code(nx,ny,rest)) == 0) {
                            if (nx == m - 1 && ny == n - 1) return step;
                            q.push(code(nx, ny, rest));
                            visited.insert(code(nx, ny, rest));
                        } else if (grid[nx][ny] == 1 && visited.count(code(nx,ny,rest-1)) == 0 && rest > 0){
                            q.push(code(nx, ny, rest-1));
                            visited.insert(code(nx, ny, rest-1));
                        }
                    }
                }
            }
        }
        return -1;
    }

    int code(int x, int y, int rest) {
        return (rest + y * int(1e4) + x * int(1e6));
    }

    void decode(int c, int* x, int* y, int* rest) {
        *rest = c % int(1e4); c /= int(1e4);
        *y = c % 100; c /= 100;
        *x = c;
    }


};