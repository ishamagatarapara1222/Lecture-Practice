#include<stdio.h>

// Function declaration
int sumArray(int arr[], int size);

int main() {
    int n, i;

    printf("Enter array size: ");
    scanf("%d", &n);

    int arr[n];

    printf("Enter array elements:\n");
    for(i = 0; i < n; i++) {
        printf("a[%d] = ", i);
        scanf("%d", &arr[i]);
    }

    // Function call
    int sum = sumArray(arr, n);

    printf("The sum of an Array: %d\n", sum);

    return 0;
}

// Function definition
int sumArray(int arr[], int size) {
    int i, sum = 0;

    for(i = 0; i < size; i++) {
        sum += arr[i];
    }

    return sum;
}
