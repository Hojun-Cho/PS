
import java.util.*;

public class Solution {
    public int solution(String begin, String target, String[] words) {
        int answer = 51;
        List<String> list = Arrays.asList(words);
        if (!list.contains(target)) {
            return 0;
        }
        Map<String, Boolean> visit = new HashMap<>();
        Deque<String> wordQueue = new ArrayDeque<>();
        Deque<Integer> countQueue = new ArrayDeque<>();

        wordQueue.add(begin);
        countQueue.add(0);
        while (!wordQueue.isEmpty()) {
            String nowWord = wordQueue.pollFirst();
            Integer nowCount = countQueue.pollFirst();

            if (nowWord.equals(target)) {
                answer = Math.min(answer, nowCount);
                continue;
            }

            visit.put(nowWord, Boolean.TRUE);
            for (String otherWord : list) {
                if (!visit.containsKey(otherWord)) {
                    int count = 0;
                    for (int i = 0; i < nowWord.length(); i++) {
                        if (nowWord.charAt(i) == otherWord.charAt(i)) {
                            count += 1;
                        }
                    }
                    if (count == nowWord.length() - 1) {
                        wordQueue.add(otherWord);
                        countQueue.add(nowCount+1);
                    }
                }
            }

        }

        return answer;
    }
}

//stream을 이용하면?

public class Solution {
    public int solution(String begin, String target, String[] words) {
        int answer = 51;
        List<String> inputWords = Arrays.asList(words);
        if (!inputWords.contains(target)) {
            return 0;
        }
        Map<String, Boolean> visit = new HashMap<>();
        Deque<String> wordQueue = new ArrayDeque<>();
        Deque<Integer> countQueue = new ArrayDeque<>();

        wordQueue.add(begin);
        countQueue.add(0);

        while (!wordQueue.isEmpty()) {
            String nowWord = wordQueue.pollFirst();
            Integer nowCount = countQueue.pollFirst();

            if (nowWord.equals(target)) {
                answer = Math.min(answer, nowCount);
                continue;
            }
            visit.put(nowWord, Boolean.TRUE);

            inputWords.stream()
                    .filter(word -> !visit.containsKey(word))
                    .parallel()
                    .filter(otherWord -> isValidWord(nowWord, otherWord))
                    .forEach(otherWord -> {
                        wordQueue.push(otherWord);
                        countQueue.push(nowCount + 1);
                    });
        }
        return answer;
    }

    private boolean isValidWord(String nowWord, String otherWrod) {
        int count = 0;
        for (int i = 0; i < nowWord.length(); i++) {
            if (nowWord.charAt(i) == otherWrod.charAt(i)) {
                count += 1;
            }
        }
        return count == nowWord.length() - 1;

    }
}


