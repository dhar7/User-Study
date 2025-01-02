global _matrix_multiply
section .text
_matrix_multiply:
    push ebp
    mov ebp, esp
    ; Get pointers to matrices and result
    mov esi, [ebp + 8]   ; matrix1
    mov edi, [ebp + 12]  ; matrix2
    mov ebx, [ebp + 16]  ; result
    ; Calculate result[0,0]
    mov eax, [esi]
    imul dword [edi]
    mov ecx, eax
    mov eax, [esi + 4]
    imul dword [edi + 8]
    add eax, ecx
    mov [ebx], eax
    ; Calculate result[0,1]
    mov eax, [esi]
    imul dword [edi + 4]
    mov ecx, eax
    mov eax, [esi + 4]
    imul dword [edi + 12]
    add eax, ecx
    mov [ebx + 4], eax
    ; Calculate result[1,0]
    mov eax, [esi + 8]
    imul dword [edi]
    mov ecx, eax
    mov eax, [esi + 12]
    imul dword [edi + 8]
    add eax, ecx
    mov [ebx + 8], eax
    ; Calculate result[1,1]
    mov eax, [esi + 8]
    imul dword [edi + 4]
    mov ecx, eax
    mov eax, [esi + 12]
    imul dword [edi + 12]
    add eax, ecx
    mov [ebx + 12], eax
    mov esp, ebp
    pop ebp
    ret
