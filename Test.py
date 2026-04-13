#include <stdio.h>
#include <assert.h>

// Equivalent of Main1.Add
int Add(int a, int b) {
    return a + b;
}

void TestAdd() {
    assert(Add(3, 4) == 7);
    printf("Test Passed\n");
}

int main() {
    TestAdd();
    return 0;
}
