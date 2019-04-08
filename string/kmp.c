#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int kmp_match(char [], char []);
int kmp_match_count(char [], char []);
int* kmp_failure(char []);

int main() {
  char T[] = "XYXZXYXXYXYZXYZZZXYXYZZZXYZ";
  char P[] = "XYZZZXYZ";

  printf("count: %d\n", kmp_match_count(T, P));
}

int kmp_match(char T[], char P[]) {
  int* fail = kmp_failure(P);
  int T_length = strlen(T);
  int P_length = strlen(P);
  int i = 0;
  int j = 0;

  while (i < T_length) {
    if (T[i] == P[j]) {
      if (j == P_length - 1) {
        free(fail);
        return i - j;
      }
      else {
        i++;
        j++;
      }
    }
    else {
      if (j > 0)
        j = fail[j - 1];
      else
        i++;
    }
  }

  free(fail);
  return -1;
}

int kmp_match_count(char T[], char P[]) {
  int* fail = kmp_failure(P);
  int T_length = strlen(T);
  int P_length = strlen(P);
  int i = 0;
  int j = 0;
  int count = 0;

  while (i < T_length) {
    count++;
    if (T[i] == P[j]) {
      if (j == P_length - 1) {
        free(fail);
        return count;
      }
      else {
        i++;
        j++;
      }
    }
    else {
      if (j > 0)
        j = fail[j - 1];
      else
        i++;
    }

  }

  free(fail);
  return -1;
}

int* kmp_failure(char pattern[]) {
  int pattern_length = strlen(pattern);
  int* failure = malloc(sizeof(int) * pattern_length);
  int i = 1;
  int j = 0;
  failure[0] = 0;

  while (i < pattern_length) {
    if (pattern[j] == pattern[i]) {
      j++;
      failure[i] = j;
      i++;
    }
    else {
      if (j != 0) { 
        j = failure[j - 1]; 
      } 
      else 
      { 
        failure[i] = 0; 
        i++; 
      }
    }
  }

  return failure;
}
