#include <stdio.h>
#include <string.h>

int brute_force(char[], char[]);
int brute_force_count(char [], char []);

int main() {
  char T[] = "peter piper picked a peck of pickled peppers";
  char P[] = "pickle";
  printf("%d\n", brute_force_count(T, P));
  return 0;
}

int brute_force_count(char T[], char P[]) {
  int T_length = strlen(T);
  int P_length = strlen(P);
  int count = 0;
  for (int i = 0; i < T_length - P_length; i++) {
    int j = 0;
    while (1) {
      if (j < P_length && T[i + j] == P[j]) {
        count++;
        j++;
        if (j == P_length)
          return count;
      }
      else {
        count++;
        break;
      }
    }
  }

  return -1;
}

int brute_force(char T[], char P[]) {
  int T_length = strlen(T);
  int P_length = strlen(P);
  for (int i = 0; i < T_length - P_length; i++) {
    int j = 0;
    while (j < P_length && T[i + j] == P[j]) {
      j++;
      if (j == P_length)
        return i;
    }
  }

  return -1;
}
