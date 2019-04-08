#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int boyer_moore(char [], char [], char []);
int boyer_moore_count(char [], char [], char[]);
int* last_occurence(char [], char []);

int main() {
  char T[] = "ABBACCDABCDAABABBDCCDAABABAD";
  char P[] = "BABAD";
  char sigma[] = "ABCD";

  printf("%d\n", boyer_moore_count(T, P, sigma));
}

int boyer_moore(char T[], char P[], char sigma[]) {
  int* last = last_occurence(P, sigma);
  int T_length = strlen(T);
  int P_length = strlen(P);
  int sigma_length = strlen(sigma);
  int i = P_length - 1;
  int j = P_length - 1;

  for (int k = 0; k < T_length; k++) {
    if (T[i] == P[j]) {
      if (j == 0) {
        free(last);
        return i;
      }
      else {
        i--;
        j--;
      }
    }
    else {
      int l;

      for (int n = 0; n < sigma_length; n++)
        if (T[i] == sigma[n])
          l = last[n];

      int temp;

      if (j > l + 1)
        temp = l + 1;
      else
        temp = j;

      i = i + P_length - temp;
      j = P_length - 1;
    }
  }

  free(last);
  return -1;
}

int boyer_moore_count(char T[], char P[], char sigma[]) {
  int* last = last_occurence(P, sigma);
  int T_length = strlen(T);
  int P_length = strlen(P);
  int sigma_length = strlen(sigma);
  int i = P_length - 1;
  int j = P_length - 1;
  int count = 0;

  for (int k = 0; k < T_length; k++) {
    count++;
    if (T[i] == P[j]) {
      if (j == 0) {
        free(last);
        return count;
      }
      else {
        i--;
        j--;
      }
    }
    else {
      int l;

      for (int n = 0; n < sigma_length; n++)
        if (T[i] == sigma[n])
          l = last[n];

      int temp;

      if (j > l + 1)
        temp = l + 1;
      else
        temp = j;

      i = i + P_length - temp;
      j = P_length - 1;
    }
  }

  free(last);
  return -1;
}

int* last_occurence(char P[], char sigma[]) {
  int length = strlen(sigma);
  int* last = malloc(sizeof(int) * length);
  int P_length = strlen(P);
  int sigma_length = strlen(sigma);

  for (int i = 0; i < length; i++) {
    last[i] = -1;
  }

  for (int i = P_length - 1; i >= 0; i--) {
    for (int j = 0; j < sigma_length; j++) {
      if (sigma[j] == P[i] && last[j] == -1)
        last[j] = i;
    }
  }

  return last;
}
