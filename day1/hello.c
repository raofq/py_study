#include <stdio.h>

int main(void)
{
  char *a = "abc";
  char *b = a;
  a = "xyz";

  printf("a=%s\n", a);
  printf("b=%s\n", b);
}
