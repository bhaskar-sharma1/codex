#include <stdio.h>
#include <stdlib.h>
#include <limits.h>  // For INT_MAX and abs()

// Comparator function for sorting
int compare(const void *a, const void *b) {
    return (*(int *)a - *(int *)b);
}

// Function to find the closest 3-sum
int threeSumClosest(int* nums, int numsSize, int target) {
    qsort(nums, numsSize, sizeof(int), compare); // Sort the array
    int closest_sum = INT_MAX;  // Initialize with a large value

    for (int i = 0; i < numsSize - 2; i++) {
        int left = i + 1;
        int right = numsSize - 1;

        while (left < right) {
            int current_sum = nums[i] + nums[left] + nums[right];

            // Update closest_sum if it's closer to the target
            if (abs(target - current_sum) < abs(target - closest_sum)) {
                closest_sum = current_sum;
            }

            if (current_sum < target) {
                left++;
            } else if (current_sum > target) {
                right--;
            } else {
                return current_sum;  // Exact match found, return immediately
            }
        }
    }
    return closest_sum;
}

// Testing function
int main() {
    int nums1[] = {-1, 2, 1, -4};
    int nums2[] = {0, 0, 0};
    int nums3[] = {1, 1, 1, 1};
    int nums4[] = {-1, 0, 1, 1};
    int nums5[] = {4, -1, 2, 1};

    printf("Test Case 1: %d\n", threeSumClosest(nums1, 4, 1));  // Expected: 2
    printf("Test Case 2: %d\n", threeSumClosest(nums2, 3, 1));  // Expected: 0
    printf("Test Case 3: %d\n", threeSumClosest(nums3, 4, 3));  // Expected: 3
    printf("Test Case 4: %d\n", threeSumClosest(nums4, 4, 2));  // Expected: 2
    printf("Test Case 5: %d\n", threeSumClosest(nums5, 4, 5));  // Expected: 5

    return 0;
}
