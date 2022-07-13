import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.IntStream;

public class Main {
    public static final int CONNECTED = 1;
    private static Map<Integer, Map<Integer, Boolean>> maps = new HashMap<>(new HashMap<>());
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static StringTokenizer st;
    private static int[] node;
    private static int N;
    private static int M;

    public static void main(String[] args) throws IOException {
        makeMap(N);
    }

    private static void makeMap(int N) throws IOException {
        N = Integer.parseInt(br.readLine());
        M = Integer.parseInt(br.readLine());
        node = IntStream.range(0, N)
                .toArray();

        for (int start = 0; start < N; start++) {
            st = new StringTokenizer(br.readLine(), " ");
            int finalStart = start;
            IntStream.range(0, N)
                    .filter(end -> Integer.parseInt(st.nextToken()) == CONNECTED)
                    .forEach(end -> union(finalStart, end));
        }

        int[] plans = Arrays.stream(br.readLine().split(" "))
                .mapToInt(city -> Integer.parseInt(city))
                .toArray();

        int root = node[plans[0] - 1];
        for (int now : plans){
            if(node[now-1] != root){
                System.out.println("NO");
                return;
            }
        }
        System.out.println("YES");
    }

    private static void union(int start, int end) {
        start = find(start);
        end = find(end);

        if (start < end) {
            node[end] = start;
            return;
        }
        node[start] = end;
    }

    private static int find(int start) {
        if (start == node[start]) {
            return start;
        }
        node[start] = find(node[start]);
        return node[start];
    }
}
