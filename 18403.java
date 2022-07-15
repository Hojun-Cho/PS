import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Point {
    int x;
    int y;

    public Point(int[] point) {
        this.x = point[0];
        this.y = point[1];
    }

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

class Boomerang {
    final Point a;
    final Point b;
    final Point c;
    final int durability;

    public Boomerang(Point a, Point b, Point c, int durability) {
        this.a = a;
        this.b = b;
        this.c = c;
        this.durability = durability;
    }
}

class Maps {
    private final int[][] maps;
    final int n;
    final int m;

    public Maps(int[][] maps, int n, int m) {
        this.maps = maps;
        this.n = n;
        this.m = m;
    }

    public int getDurability(Point point) {
        return maps[point.x][point.y];
    }

    public boolean isValidIndex(Point src, Point[] bias) {
        return src.x + bias[0].x >= 0 && src.x + bias[0].x < n
                && src.y + bias[0].y >= 0 && src.y + bias[0].x < m
                && src.x + bias[1].x >= 0 && src.x + bias[1].x < n
                && src.y + bias[1].y >= 0 && src.y + bias[1].y < m;
    }
}

class Visited {
    private boolean[][] visited;

    public Visited(int n, int m) {
        this.visited = new boolean[n][m];
    }

    public void visit(Boomerang boo) {
        set(true, boo);
    }

    public void cancelVisit(Boomerang boo) {
        set(false, boo);
    }

    public boolean isVisited(Point p) {
        return visited[p.x][p.y];
    }

    public boolean isVisited(Boomerang boo) {
        return isVisited(boo.a) ||
                isVisited(boo.b) ||
                isVisited(boo.c);
    }

    private void set(boolean value, Boomerang boo) {
        visited[boo.a.x][boo.a.y] = value;
        visited[boo.b.x][boo.b.y] = value;
        visited[boo.c.x][boo.c.y] = value;
    }

    public boolean isVisitedAll(List<Boomerang> boomerangs) {
        for (Boomerang boomerang : boomerangs) {
            if (!isVisited(boomerang))
                return false;
        }
        return true;
    }
}

class BoomerangFactory {
    private static final Point[] a = {new Point(1, 0), new Point(0, 1)};
    private static final Point[] b = {new Point(0, -1), new Point(1, 0)};
    private static final Point[] c = {new Point(-1, 0), new Point(0, 1)};
    private static final Point[] d = {new Point(0, -1), new Point(-1, 0)};
    private static final Point[][] all = {a, b, c, d};
    private final Maps maps;

    public BoomerangFactory(Maps maps) {
        this.maps = maps;
    }

    public List<Boomerang> make(Point src) {
        List<Boomerang> list = new ArrayList<>();
        for (Point[] shape : all) {
            if (maps.isValidIndex(src, shape)) {
                list.add(makePiece(src, shape));
            }
        }
        return list;
    }

    private Boomerang makePiece(Point src, Point[] shape) {
        Point a = new Point(src.x + shape[0].x, src.y + shape[0].y);
        Point b = new Point(src.x, src.y);
        Point c = new Point(src.x + shape[1].x, src.y + shape[1].y);
        int sum = maps.getDurability(a) + maps.getDurability(b) * 2 + maps.getDurability(c);
        return new Boomerang(a, b, c, sum);
    }
}

class Solution {
    private final Maps maps;
    private final Visited visited;
    private final BoomerangFactory boomerangFactory;
    private int answer;

    public Solution(int n, int m, int[][] maps) {
        this.maps = new Maps(maps, n, m);
        visited = new Visited(n, m);
        boomerangFactory = new BoomerangFactory(this.maps);
    }

    public int invoke() {
        dfs(0);
        return answer;
    }

    private void dfs(int nowMax) {
        for (int i = 0; i < maps.n; i++) {
            for (int j = 0; j < maps.m; j++) {
                Point point = new Point(i, j);
                if (visited.isVisited(point)) {
                    answer = Math.max(answer, nowMax);
                    continue;
                }
                List<Boomerang> boomerangs = boomerangFactory.make(point);
                if (boomerangs.size() == 0 || visited.isVisitedAll(boomerangs)) {
                    answer = Math.max(answer, nowMax);
                    continue;

                }
                for (Boomerang boomerang : boomerangs) {
                    if (!visited.isVisited(boomerang)) {
                        visited.visit(boomerang);
                        dfs(nowMax + boomerang.durability);
                        visited.cancelVisit(boomerang);
                    }
                }
            }
        }
    }
}

public class Main {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static StringTokenizer st;


    private static void run() throws IOException {
        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[][] maps = new int[N][M];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                maps[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        int result = new Solution(N, M, maps).invoke();
        System.out.println(result);
    }

    public static void main(String[] args) throws IOException {
        run();
    }

}

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Point {
    int x;
    int y;

    public Point(int[] point) {
        this.x = point[0];
        this.y = point[1];
    }

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

class Boomerang {
    final Point a;
    final Point b;
    final Point c;
    final int durability;

    public Boomerang(Point a, Point b, Point c, int durability) {
        this.a = a;
        this.b = b;
        this.c = c;
        this.durability = durability;
    }
}

class Maps {
    private final int[][] maps;
    final int n;
    final int m;

    public Maps(int[][] maps, int n, int m) {
        this.maps = maps;
        this.n = n;
        this.m = m;
    }

    public int getDurability(Point point) {
        return maps[point.x][point.y];
    }

    public boolean isValidIndex(Point src, Point[] bias) {
        return src.x + bias[0].x >= 0 && src.x + bias[0].x < n
                && src.y + bias[0].y >= 0 && src.y + bias[0].x < m
                && src.x + bias[1].x >= 0 && src.x + bias[1].x < n
                && src.y + bias[1].y >= 0 && src.y + bias[1].y < m;
    }
}

class Visited {
    private boolean[][] visited;

    public Visited(int n, int m) {
        this.visited = new boolean[n][m];
    }

    public void visit(Boomerang boo) {
        set(true, boo);
    }

    public void cancelVisit(Boomerang boo) {
        set(false, boo);
    }

    public boolean isVisited(Point p) {
        return visited[p.x][p.y];
    }

    public boolean isVisited(Boomerang boo) {
        return isVisited(boo.a) ||
                isVisited(boo.b) ||
                isVisited(boo.c);
    }

    private void set(boolean value, Boomerang boo) {
        visited[boo.a.x][boo.a.y] = value;
        visited[boo.b.x][boo.b.y] = value;
        visited[boo.c.x][boo.c.y] = value;
    }

    public boolean isVisitedAll(List<Boomerang> boomerangs) {
        for (Boomerang boomerang : boomerangs) {
            if (!isVisited(boomerang))
                return false;
        }
        return true;
    }
}

class BoomerangFactory {
    private static final Point[] a = {new Point(1, 0), new Point(0, 1)};
    private static final Point[] b = {new Point(0, -1), new Point(1, 0)};
    private static final Point[] c = {new Point(-1, 0), new Point(0, 1)};
    private static final Point[] d = {new Point(0, -1), new Point(-1, 0)};
    private static final Point[][] all = {a, b, c, d};
    private final Maps maps;

    public BoomerangFactory(Maps maps) {
        this.maps = maps;
    }

    public List<Boomerang> make(Point src) {
        List<Boomerang> list = new ArrayList<>();
        for (Point[] shape : all) {
            if (maps.isValidIndex(src, shape)) {
                list.add(makePiece(src, shape));
            }
        }
        return list;
    }

    private Boomerang makePiece(Point src, Point[] shape) {
        Point a = new Point(src.x + shape[0].x, src.y + shape[0].y);
        Point b = new Point(src.x, src.y);
        Point c = new Point(src.x + shape[1].x, src.y + shape[1].y);
        int sum = maps.getDurability(a) + maps.getDurability(b) * 2 + maps.getDurability(c);
        return new Boomerang(a, b, c, sum);
    }
}

class Solution {
    private final Maps maps;
    private final Visited visited;
    private final BoomerangFactory boomerangFactory;
    private int answer;

    public Solution(int n, int m, int[][] maps) {
        this.maps = new Maps(maps, n, m);
        visited = new Visited(n, m);
        boomerangFactory = new BoomerangFactory(this.maps);
    }

    public int invoke() {
        dfs(0);
        return answer;
    }

    private void dfs(int nowMax) {
        for (int i = 0; i < maps.n; i++) {
            for (int j = 0; j < maps.m; j++) {
                Point point = new Point(i, j);
                if (visited.isVisited(point)) {
                    answer = Math.max(answer, nowMax);
                    continue;
                }
                List<Boomerang> boomerangs = boomerangFactory.make(point);
                if (boomerangs.size() == 0 || visited.isVisitedAll(boomerangs)) {
                    answer = Math.max(answer, nowMax);
                    continue;

                }
                for (Boomerang boomerang : boomerangs) {
                    if (!visited.isVisited(boomerang)) {
                        visited.visit(boomerang);
                        dfs(nowMax + boomerang.durability);
                        visited.cancelVisit(boomerang);
                    }
                }
            }
        }
    }
}

public class Main {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static StringTokenizer st;


    private static void run() throws IOException {
        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[][] maps = new int[N][M];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                maps[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        int result = new Solution(N, M, maps).invoke();
        System.out.println(result);
    }

    public static void main(String[] args) throws IOException {
        run();
    }

}
