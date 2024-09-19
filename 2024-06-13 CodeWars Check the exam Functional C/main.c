#include <stddef.h>

int req(size_t n, const char answers[n], const char student[n]) {
  if (n == 1) {
    if (student[0] == ' ') {
      return 0;
    }
    if (student[0] == answers[0]) {
      return 4;
    }
    return -1;
  }
  if (student[0] == ' ') {
    return 0 + req(n - 1, &answers[1], &student[1]);
  }
  if (student[0] == answers[0]) {
    return 4 + req(n - 1, &answers[1], &student[1]);
  }
  return - 1 + req(n - 1, &answers[1], &student[1]);
}

int check_exam(size_t n, const char answers[n], const char student[n]) {
  int result = req(n, answers, student);
  if (result < 0) {
    return 0;
  }
  return result;
}