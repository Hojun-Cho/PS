import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.concurrent.atomic.AtomicInteger;

class Solution {
    private Comparator<Integer> integerComparator = (o1, o2) -> {
        if (o1 > o2)
            return 1;
        else if (o1 < o2)
            return -1;
        return 0;
    };

    public int invoke(List<Integer> times, int n) {
        times.sort(integerComparator);
        AtomicInteger sum = new AtomicInteger();
        times.stream()
                .reduce(0, (total, time) -> {
                    total += time;
                    sum.addAndGet(total);
                    return total;
                });
        return sum.get();
    }

}

public class Main {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static StringTokenizer st;


    private static int run() throws IOException {
        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());

        List<Integer> times = new ArrayList<>();

        st = new StringTokenizer(br.readLine());
        for (int j = 0; j < N; j++) {
            times.add(Integer.parseInt(st.nextToken()));
        }
        return new Solution().invoke(times, N);

    }

    public static void main(String[] args) throws IOException {
        System.out.println(run());
    }

}
