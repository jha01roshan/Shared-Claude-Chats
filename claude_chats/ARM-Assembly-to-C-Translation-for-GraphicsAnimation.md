# ARM Assembly to C Translation for Graphics/Animation

- Source: https://claude.ai/share/79006cbb-e143-4c25-9016-f89ece45e9be
- Author: Bruno
- Created: 2025-05-04
- Messages: 4

---

## Human

You have the following assembly code from ARMv7 in thumb mode:
```
	thumb_func_start sub_8063D38
sub_8063D38: @ 0x08063D38
	push {r4, r5, r6, r7, lr}
	mov r7, r8
	push {r7}
	sub sp, #0x2c
	adds r6, r0, #0
	ldrb r0, [r6, #8]
	cmp r0, #1
	beq _08063DA0
	adds r5, r6, #0
	adds r5, #0x5c
	ldrb r0, [r5]
	subs r0, #0x10
	strb r0, [r5]
	adds r4, r6, #0
	adds r4, #0x5d
	ldrb r0, [r4]
	subs r0, #0x10
	strb r0, [r4]
	adds r3, r6, #0
	adds r3, #0x5e
	ldrb r0, [r3]
	subs r0, #0x10
	strb r0, [r3]
	adds r2, r6, #0
	adds r2, #0x5f
	ldrb r0, [r2]
	subs r0, #0x10
	strb r0, [r2]
	adds r1, r6, #0
	adds r1, #0x64
	ldrb r0, [r1]
	subs r0, #0x10
	strb r0, [r1]
	adds r1, #1
	ldrb r0, [r1]
	subs r0, #0x10
	strb r0, [r1]
	adds r1, #1
	ldrb r0, [r1]
	subs r0, #0x10
	strb r0, [r1]
	adds r1, #1
	ldrb r0, [r1]
	subs r0, #0x10
	strb r0, [r1]
	ldrb r0, [r6, #8]
	mov r8, r5
	adds r7, r4, #0
	adds r5, r3, #0
	adds r4, r2, #0
	cmp r0, #1
	bne _08063DC4
_08063DA0:
	adds r4, r6, #0
	adds r4, #0x5c
	movs r0, #0xfc
	strb r0, [r4]
	adds r3, r6, #0
	adds r3, #0x5d
	strb r0, [r3]
	adds r2, r6, #0
	adds r2, #0x5e
	movs r0, #4
	strb r0, [r2]
	adds r1, r6, #0
	adds r1, #0x5f
	strb r0, [r1]
	mov r8, r4
	adds r7, r3, #0
	adds r5, r2, #0
	adds r4, r1, #0
_08063DC4:
	adds r0, r6, #0
	mov r1, sp
	bl sub_8063EDC
	str r0, [sp, #4]
	adds r0, r6, #0
	adds r0, #0x38
	str r0, [sp, #0x1c]
	ldr r0, [r6, #0x1c]
	str r0, [sp, #0x10]
	ldr r0, [r6, #0x20]
	str r0, [sp, #0x14]
	mov r1, sp
	ldrh r0, [r6, #0xc]
	movs r2, #0
	strh r0, [r1, #0xc]
	ldrh r0, [r6, #0xe]
	strh r0, [r1, #0xe]
	ldr r0, [r6]
	str r0, [sp]
	ldrb r0, [r6, #7]
	strb r0, [r1, #8]
	mov r0, sp
	str r2, [sp, #0x28]
	bl sub_805C280
	adds r3, r0, #0
	ldrb r0, [r6, #8]
	ldr r2, [sp, #0x28]
	cmp r0, #1
	beq _08063E44
	mov r1, r8
	ldrb r0, [r1]
	adds r0, #0x10
	strb r0, [r1]
	ldrb r0, [r7]
	adds r0, #0x10
	strb r0, [r7]
	ldrb r0, [r5]
	adds r0, #0x10
	strb r0, [r5]
	ldrb r0, [r4]
	adds r0, #0x10
	strb r0, [r4]
	adds r1, r6, #0
	adds r1, #0x64
	ldrb r0, [r1]
	adds r0, #0x10
	strb r0, [r1]
	adds r1, #1
	ldrb r0, [r1]
	adds r0, #0x10
	strb r0, [r1]
	adds r1, #1
	ldrb r0, [r1]
	adds r0, #0x10
	strb r0, [r1]
	adds r1, #1
	ldrb r0, [r1]
	adds r0, #0x10
	strb r0, [r1]
	ldrb r0, [r6, #8]
	cmp r0, #1
	bne _08063E4E
_08063E44:
	mov r0, r8
	strb r2, [r0]
	strb r2, [r7]
	strb r2, [r5]
	strb r2, [r4]
_08063E4E:
	adds r0, r3, #0
	add sp, #0x2c
	pop {r3}
	mov r8, r3
	pop {r4, r5, r6, r7}
	pop {r1}
	bx r1
```
Translate it to an equivalent code in C.

---

## Assistant

Let me analyze this ARM assembly code and translate it to C. Here are the key observations:

1. The function takes one parameter (in r0)
2. It manipulates various byte offsets from the base pointer (r6)
3. There are conditional branches based on a byte at offset 8
4. It makes calls to two other functions: sub_8063EDC and sub_805C280
5. It performs arithmetic on bytes at various offsets

Here's the equivalent C code:

```c
// Function prototype for the called functions
int sub_8063EDC(void* arg1, void* sp);
int sub_805C280(void* sp);

int sub_8063D38(void* param) {
    struct {
        void* field0;        // [sp + 0]
        int field4;          // [sp + 4]
        uint16_t field0C;    // [sp + C]
        uint16_t field0E;    // [sp + E]
        int field10;         // [sp + 10]
        int field14;         // [sp + 14]
        void* field1C;       // [sp + 1C]
        int field28;         // [sp + 28]
        // Other stack variables might exist
    } stack_struct;

    if (*(uint8_t*)(param + 8) != 1) {
        // Subtract 0x10 from bytes at various offsets
        *(uint8_t*)(param + 0x5C) -= 0x10;
        *(uint8_t*)(param + 0x5D) -= 0x10;
        *(uint8_t*)(param + 0x5E) -= 0x10;
        *(uint8_t*)(param + 0x5F) -= 0x10;
        *(uint8_t*)(param + 0x64) -= 0x10;
        *(uint8_t*)(param + 0x65) -= 0x10;
        *(uint8_t*)(param + 0x66) -= 0x10;
        *(uint8_t*)(param + 0x67) -= 0x10;
    }

    if (*(uint8_t*)(param + 8) == 1) {
        // Set specific values at offsets
        *(uint8_t*)(param + 0x5C) = 0xFC;
        *(uint8_t*)(param + 0x5D) = 0xFC;
        *(uint8_t*)(param + 0x5E) = 4;
        *(uint8_t*)(param + 0x5F) = 4;
    }

    // Setup stack_struct fields
    int result = sub_8063EDC(param, &stack_struct);
    stack_struct.field4 = result;
    stack_struct.field1C = param + 0x38;
    stack_struct.field10 = *(int*)(param + 0x1C);
    stack_struct.field14 = *(int*)(param + 0x20);
    stack_struct.field0C = *(uint16_t*)(param + 0xC);
    stack_struct.field0E = *(uint16_t*)(param + 0xE);
    stack_struct.field0 = *(void**)(param);
    stack_struct.field28 = 0;
    *(uint8_t*)((char*)&stack_struct + 8) = *(uint8_t*)(param + 7);

    result = sub_805C280(&stack_struct);

    if (*(uint8_t*)(param + 8) != 1) {
        // Add 0x10 to bytes at various offsets
        *(uint8_t*)(param + 0x5C) += 0x10;
        *(uint8_t*)(param + 0x5D) += 0x10;
        *(uint8_t*)(param + 0x5E) += 0x10;
        *(uint8_t*)(param + 0x5F) += 0x10;
        *(uint8_t*)(param + 0x64) += 0x10;
        *(uint8_t*)(param + 0x65) += 0x10;
        *(uint8_t*)(param + 0x66) += 0x10;
        *(uint8_t*)(param + 0x67) += 0x10;
    }

    if (*(uint8_t*)(param + 8) == 1) {
        // Zero out bytes at offsets
        *(uint8_t*)(param + 0x5C) = 0;
        *(uint8_t*)(param + 0x5D) = 0;
        *(uint8_t*)(param + 0x5E) = 0;
        *(uint8_t*)(param + 0x5F) = 0;
    }

    return result;
}
```

A few notes about this translation:

1. I've used a local struct to represent the stack frame that's being manipulated. The assembly allocates 0x2C (44) bytes on the stack, though not all fields are clearly visible in the usage.

2. The function appears to be manipulating some kind of data structure passed as a pointer, with various byte offsets having special meaning.

3. There's a special condition when the byte at offset 8 is 1, which causes different behavior in how the bytes are modified.

4. The function makes calls to two other functions (sub_8063EDC and sub_805C280) and passes them pointers to either the input parameter or the stack structure.

5. The exact layout of the stack structure might not be 100% accurate as some fields might be used differently than shown, but this represents the observed access patterns in the assembly.

This looks like it might be part of a graphics or animation system, given the pattern of byte manipulations (adding/subtracting 0x10) and the regular structure of the offsets being modified.

---

## Human

Create a structure for `param`

---

## Assistant

Looking at how the code accesses various offsets from the param pointer, I can create a structure that represents its layout:

```c
struct Object {
    void* field0;           // offset 0x00: dereferenced and stored in stack_struct
    // Unknown fields from 0x04-0x06
    uint8_t field7;         // offset 0x07: copied to stack_struct+8
    uint8_t field8;         // offset 0x08: checked for value 1
    // Unknown fields from 0x09-0x0B
    uint16_t fieldC;        // offset 0x0C: copied to stack_struct
    uint16_t fieldE;        // offset 0x0E: copied to stack_struct
    // Unknown fields from 0x10-0x1B
    int field1C;            // offset 0x1C: copied to stack_struct
    int field20;            // offset 0x20: copied to stack_struct
    // Unknown fields from 0x24-0x37
    uint8_t field38[0x24];  // offset 0x38: pointer to this is stored in stack_struct
    // Unknown fields from 0x5C-0x5B
    uint8_t field5C;        // offset 0x5C: modified by +/- 0x10 or set to 0xFC/0
    uint8_t field5D;        // offset 0x5D: modified by +/- 0x10 or set to 0xFC/0
    uint8_t field5E;        // offset 0x5E: modified by +/- 0x10 or set to 4/0
    uint8_t field5F;        // offset 0x5F: modified by +/- 0x10 or set to 4/0
    // Unknown fields from 0x60-0x63
    uint8_t field64;        // offset 0x64: modified by +/- 0x10
    uint8_t field65;        // offset 0x65: modified by +/- 0x10
    uint8_t field66;        // offset 0x66: modified by +/- 0x10
    uint8_t field67;        // offset 0x67: modified by +/- 0x10
};
```

Now we can rewrite the function using this structure:

```c
int sub_8063EDC(struct Object* obj, void* sp);
int sub_805C280(void* sp);

int sub_8063D38(struct Object* obj) {
    struct {
        void* field0;
        int field4;
        uint16_t field0C;
        uint16_t field0E;
        int field10;
        int field14;
        void* field1C;
        int field28;
    } stack_struct;

    if (obj->field8 != 1) {
        obj->field5C -= 0x10;
        obj->field5D -= 0x10;
        obj->field5E -= 0x10;
        obj->field5F -= 0x10;
        obj->field64 -= 0x10;
        obj->field65 -= 0x10;
        obj->field66 -= 0x10;
        obj->field67 -= 0x10;
    }

    if (obj->field8 == 1) {
        obj->field5C = 0xFC;
        obj->field5D = 0xFC;
        obj->field5E = 4;
        obj->field5F = 4;
    }

    int result = sub_8063EDC(obj, &stack_struct);
    stack_struct.field4 = result;
    stack_struct.field1C = &obj->field38;
    stack_struct.field10 = obj->field1C;
    stack_struct.field14 = obj->field20;
    stack_struct.field0C = obj->fieldC;
    stack_struct.field0E = obj->fieldE;
    stack_struct.field0 = obj->field0;
    stack_struct.field28 = 0;
    *(uint8_t*)((char*)&stack_struct + 8) = obj->field7;

    result = sub_805C280(&stack_struct);

    if (obj->field8 != 1) {
        obj->field5C += 0x10;
        obj->field5D += 0x10;
        obj->field5E += 0x10;
        obj->field5F += 0x10;
        obj->field64 += 0x10;
        obj->field65 += 0x10;
        obj->field66 += 0x10;
        obj->field67 += 0x10;
    }

    if (obj->field8 == 1) {
        obj->field5C = 0;
        obj->field5D = 0;
        obj->field5E = 0;
        obj->field5F = 0;
    }

    return result;
}
```

This structure represents what we can observe from the assembly code's memory access patterns. Some notes:

1. There are several gaps in the structure where we don't see any accesses in this function. Those could contain other fields used by other functions.

2. I've labeled field38 as an array since we take its address, but it could be the start of another sub-structure.

3. The pattern of modifying bytes by ±0x10 in two groups (0x5C-0x5F and 0x64-0x67) suggests these might be color or graphics-related values, possibly alpha channels or palette indices.

4. The structure size must be at least 0x68 bytes (104 bytes) based on the highest offset accessed (0x67).

This structure layout could be refined further if we had access to more code that uses this object type or additional context about the program's purpose.
