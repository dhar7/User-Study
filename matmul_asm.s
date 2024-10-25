// For performanece oprimization, multiplication is done by assembly language
// for compilation: gcc main.c matmul_asm.s -o matrix_multiply
    .global matmul_asm
matmul_asm:
    push {r4, r5, r6, r7, r8, r9, lr}  // Save necessary registers
    // Load N (matrix size) into r3
    ldr r3, [sp, #16]          // Load N from the stack (4th argument)
    mov r4, #0                 // i = 0 (outer loop for rows of A and C)
outer_loop:
    cmp r4, r3                 // Compare i with N (i >= N?)
    bge end_outer_loop          // If i >= N, exit outer loop
    mov r5, #0                 // j = 0 (inner loop for columns of B and C)
inner_loop:
    cmp r5, r3                 // Compare j with N (j >= N?)
    bge end_inner_loop         // If j >= N, exit inner loop
    // C[i][j] = 0 (Initialize sum for C[i][j])
    mov r6, #0                 // r6 will store the sum for C[i][j]
    mov r7, #0                 // k = 0 (loop over elements in the row/column)
k_loop:
    cmp r7, r3                 // Compare k with N (k >= N?)
    bge end_k_loop             // If k >= N, exit k-loop
    // Load A[i][k] into r8
    ldr r8, [r0, r4, lsl #2]   // r0 is the base address of A, compute address of A[i]
    ldr r8, [r8, r7, lsl #2]   // Offset to get A[i][k]
    // Load B[k][j] into r9
    ldr r9, [r1, r7, lsl #2]   // r1 is the base address of B, compute address of B[k]
    ldr r9, [r9, r5, lsl #2]   // Offset to get B[k][j]
    // sum += A[i][k] * B[k][j]
    mla r6, r8, r9, r6         // Multiply A[i][k] * B[k][j] and accumulate into r6
    add r7, r7, #1             // k = k + 1
    b k_loop                   // Repeat k-loop
end_k_loop:
    // Store the result C[i][j]
    ldr r8, [r2, r4, lsl #2]   // r2 is the base address of C, compute address of C[i]
    str r6, [r8, r5, lsl #2]   // Store the sum (C[i][j]) at the proper location
    add r5, r5, #1             // j = j + 1
    b inner_loop               // Repeat inner-loop
end_inner_loop:
    add r4, r4, #1             // i = i + 1
    b outer_loop               // Repeat outer-loop
end_outer_loop:
    pop {r4, r5, r6, r7, r8, r9, lr}   // Restore registers
    bx lr                              // Return from the function
