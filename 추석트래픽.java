
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

class Solution {
    public static final double RANGE = 1.0;

    public int solution(String[] lines) {
        List<TimeVO> dates = new Formatter().invoke(lines);
        int answer = 0;
        for (TimeVO times : dates) {
            Double start = times.start;
            Double end = times.end;
            int candidateAnswer = Math.max(test(new TimeVO(start, start + RANGE), dates),
                    test(new TimeVO(end, end + RANGE), dates));

            answer = Math.max(answer, candidateAnswer);
        }
        return answer;
    }

    public static int test(TimeVO now, List<TimeVO> dates) {
        return (int) dates.parallelStream()
                .filter(target -> target.end >= now.start && target.start < now.end)
                .count();

    }

    public class Formatter {
        private Time time = new Time();
        public List<TimeVO> invoke(String[] lines) {
           return Arrays.stream(lines)
                    .parallel()
                    .map(line ->{
                        String[] s = line.split(" ");
                        Double endTime = time.localDateTimeToDouble(s[0] + s[1]);
                        Double duration = time.stringToNanoSecond(s[2]);
                        return new TimeVO(endTime - duration + 0.001, endTime);
                    })
                    .collect(Collectors.toList());
        }
    }

    public class Time {
        private DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-ddHH:mm:ss.SSS");

        public Double localDateTimeToDouble(String localDateTime) {
            LocalDateTime date = LocalDateTime.parse(localDateTime, formatter);

            int hour = date.getHour();
            int minute = date.getMinute();
            int second = date.getSecond();
            Double nano = date.getNano() * 0.000000001;
            Double time = hour * 60 * 60 + minute * 60 + second + nano;

            return time;
        }

        public Double stringToNanoSecond(String nanoSecond) {
            return (Double.parseDouble(nanoSecond.split("s")[0]));
        }
    }

    public class TimeVO {
        public final Double start;
        public final Double end;

        public TimeVO(Double start, Double end) {
            this.start = start;
            this.end = end;
        }
    }

}
