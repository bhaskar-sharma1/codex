function searchInsert(nums: number[], target: number): number {
    let left = 0, right = nums.length - 1;

    while (left <= right) {
        let mid = Math.floor((left + right) / 2);
        if (nums[mid] === target) {
            return mid;
        } else if (nums[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    return left;  // The correct insert position
}

// Testing function
function test() {
    const testCases: [number[], number, number][] = [
        [[1, 3, 5, 6], 5, 2],  // Expected output: 2
        [[1, 3, 5, 6], 2, 1],  // Expected output: 1
        [[1, 3, 5, 6], 7, 4],  // Expected output: 4
        [[1, 3, 5, 6], 0, 0],  // Expected output: 0
        [[1], 0, 0],           // Expected output: 0
        [[1], 2, 1]            // Expected output: 1
    ];

    testCases.forEach(([nums, target, expected], index) => {
        const result = searchInsert(nums, target);
        console.log(`Test Case ${index + 1}: nums=${JSON.stringify(nums)}, target=${target} -> ${result} ${result === expected ? '✅' : '❌'}`);
    });
}
test();