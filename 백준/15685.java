import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Point {
    int x;
    int y;

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public void add(int dx, int dy) {
        x += dx;
        y += dy;
    }
}

class Square {
    public static int countSquare(boolean[][] map) {
        int answer = 0;
        for (int i = 0; i < map.length - 1; i++) {
            for (int j = 0; j < map.length - 1; j++) {
                if (map[i][j] && map[i + 1][j] && map[i][j + 1] && map[i + 1][j + 1]) {
                    answer += 1;
                }
            }
        }
        return answer;
    }
}

class DragonMap {
    private final static boolean[][] map = new boolean[101][101];
    private final static int[] dx = {0, -1, 0, 1};
    private final static int[] dy = {1, 0, -1, 0};

    public int getSquares() {
        return Square.countSquare(map);
    }

    public void makeDragon(Point now, int d, int g) {
        List<Integer> directions = new ArrayList<>();
        marking(now);
        now.add(dx[d], dy[d]);
        marking(now);
        directions.add(d);
        for (int i = 0; i < g; i++) {
            runGenerations(now, directions);
        }
    }

    private void runGenerations(Point point, List<Integer> directions) {
        for (int i = directions.size() - 1; i >= 0; i--) {
            int d = (1 + directions.get(i)) % 4;

            point.add(dx[d], dy[d]);
            marking(point);

            directions.add(d);
        }
    }

    private void marking(Point point) {
        map[point.x][point.y] = true;
    }
}

public class Main {
    private final static DragonMap dragonMap = new DragonMap();

    private static void invoke() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            int d = Integer.parseInt(st.nextToken());
            int g = Integer.parseInt(st.nextToken());

            dragonMap.makeDragon(new Point(y, x), d, g);
        }
        int answer = dragonMap.getSquares();
        System.out.println(answer);
    }

    public static void main(String[] args) throws IOException {
        invoke();
    }
}
