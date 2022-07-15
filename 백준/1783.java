import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static StringTokenizer st;


    private static int run() throws IOException {
        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        if (N == 1) {
            return 1;
        } else if (N == 2) {
            // 3회 이동 가능
            return Math.min(4, (M + 1) / 2);
        } else if (M <= 6) {
            return Math.min(4, M);
        }
        return M - 7 + 5;

    }

    public static void main(String[] args) throws IOException {
        System.out.println(run());
    }

}
