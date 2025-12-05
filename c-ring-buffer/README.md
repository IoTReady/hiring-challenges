# Ring Buffer Implementation Challenge

## Overview

Build a robust ring buffer library in C with file-backed persistence. Ring buffers (also called circular buffers) are fundamental data structures in IoT and embedded systems, used everywhere from sensor data buffering to communication protocol handling.

Your task is to implement a production-quality ring buffer that can handle continuous data streams and survive process restarts by persisting to disk.

**Time Estimate:** 3-4 hours
**Target Platform:** Choose one - Windows, Linux, or macOS (your implementation doesn't need to be cross-platform)

---

## Part 1: Core Ring Buffer Implementation

Implement a ring buffer library with the following functionality:

### Required API

Your library should expose these functions (or equivalent):

```c
// Create a new ring buffer with specified capacity and optional backing file
ring_buffer_t* ring_buffer_create(size_t capacity, const char* backing_file);

// Write data to the buffer (returns bytes written, or error code)
ssize_t ring_buffer_write(ring_buffer_t* rb, const void* data, size_t size);

// Read data from the buffer (returns bytes read, or error code)
ssize_t ring_buffer_read(ring_buffer_t* rb, void* data, size_t size);

// Get current buffer status
size_t ring_buffer_available(ring_buffer_t* rb);  // Bytes available to read
size_t ring_buffer_space(ring_buffer_t* rb);      // Bytes available to write
bool ring_buffer_is_empty(ring_buffer_t* rb);
bool ring_buffer_is_full(ring_buffer_t* rb);

// Clean up and destroy the buffer
void ring_buffer_destroy(ring_buffer_t* rb);
```

### Requirements

1. **Circular Behavior:** When write pointer reaches the end, it wraps to the beginning
2. **Overflow Handling:** Define clear behavior when buffer is full (overwrite oldest data OR reject new writes - document your choice)
3. **Memory Safety:** No memory leaks, proper bounds checking
4. **Error Handling:** Clear error codes/return values for failure cases

---

## Part 2: File-Backed Persistence

Add persistence so the ring buffer survives program restarts:

### Requirements

1. **Persistent Storage:** Buffer contents must be written to the backing file specified in `ring_buffer_create()`
2. **State Recovery:** When a ring buffer is opened with an existing backing file, it should restore previous contents and read/write positions
3. **Implementation Choice:** Use ONE of these approaches:
   - **Standard File I/O:** `fopen()`, `fwrite()`, `fseek()` - simpler but may be slower
   - **Memory-mapped files:** Platform-specific (`mmap()` on POSIX, `CreateFileMapping()` on Windows) - faster but more complex

4. **Metadata Storage:** Persist buffer state (read position, write position, capacity) along with data

### Example Behavior

```c
// First run
ring_buffer_t* rb = ring_buffer_create(1024, "sensor.buf");
ring_buffer_write(rb, sensor_data, sizeof(sensor_data));
ring_buffer_destroy(rb);

// Program restarts...

// Second run - data should still be there
rb = ring_buffer_create(1024, "sensor.buf");
ring_buffer_read(rb, retrieved_data, sizeof(sensor_data));
// retrieved_data should match original sensor_data
```

---

## Part 3: Test Harness

Create a comprehensive test program that validates your implementation:

### Required Tests

Your test harness (`test_harness.c` or similar) should:

1. **Basic Operations:**
   - Write data, read it back, verify correctness
   - Test with different data sizes
   - Verify read/write position tracking

2. **Wraparound Behavior:**
   - Fill buffer, read some data, write more data
   - Verify circular behavior works correctly

3. **Boundary Conditions:**
   - Empty buffer reads
   - Full buffer writes
   - Reading more data than available
   - Writing more data than space available

4. **Persistence:**
   - Write data, destroy buffer, recreate it, verify data survives
   - Test state recovery (positions, capacity)

5. **Sensor Data Simulation:**
   - Use a realistic data structure like:
   ```c
   typedef struct {
       uint64_t timestamp;  // Unix timestamp or tick count
       float temperature;   // Degrees Celsius
       float humidity;      // Percentage
       uint16_t sensor_id;  // Device identifier
   } __attribute__((packed)) sensor_reading_t;
   ```
   - Generate fake sensor readings
   - Write streams of readings to buffer
   - Read and verify data integrity

### Test Output

Print clear pass/fail results for each test:
```
[PASS] Basic write/read operations
[PASS] Buffer wraparound behavior
[FAIL] Persistence after destroy - data mismatch
[PASS] Sensor data stream handling
...
Total: 8/9 tests passed
```

---

## Part 4: Bonus Features (Optional)

If you finish early, consider implementing:

1. **Thread Safety:** Add mutex/lock protection for concurrent access
2. **Peek Operations:** Read without consuming data
3. **Clear/Reset:** Empty buffer without destroying it
4. **Statistics:** Track total bytes written/read, overflow events
5. **Multiple Readers:** Support one writer, multiple readers pattern
6. **Bulk Operations:** Optimized vectored I/O for multiple writes/reads

---

## Deliverables

Submit a GitHub repository containing:

1. **Source Files:**
   - `ring_buffer.h` - Public API header
   - `ring_buffer.c` - Implementation
   - `test_harness.c` - Test program
   - Build files (`Makefile`, `CMakeLists.txt`, or platform-specific build script)

2. **Documentation:**
   - `README.md` with:
     - How to build and run (exact commands)
     - Platform requirements (OS, compiler)
     - Design decisions (overflow behavior, file format, etc.)
     - Known limitations or trade-offs
     - Test results summary

3. **Test Output:**
   - Include sample output from your test harness run
   - Can be in README or separate `test_output.txt`

---

## Submission Instructions

1. **Create a GitHub repository** with your solution
2. **Email the repository link** to: **work@iotready.co**
3. **Email subject:** "Ring Buffer Challenge - [Your Name]"
4. **Include:** Brief introduction and any notes about your implementation

---

## Technical Requirements & Constraints

- **Language:** C (C99 or later)
- **Platform:** Choose ONE - Windows, Linux, or macOS
- **Compiler:** Specify which one you used (gcc, clang, msvc, etc.)
- **External Libraries:** Standard library only - no third-party dependencies
- **Build:** Must compile with a single command or simple build script

### Platform-Specific APIs Allowed

You may use platform-specific APIs for:
- File I/O and memory-mapped files
- Threading/synchronization (if implementing bonus features)

Use `#ifdef` blocks or separate implementations for different platforms if you want, but it's not required - pick one platform and implement for it.

---

## Notes & Guidelines

- **No AI-Generated Code:** We want to see YOUR implementation and problem-solving approach. We're not just checking if it works - we want to understand how you think about data structures, memory management, and system programming.

- **Code Quality Matters:** Write clean, readable code with appropriate comments. Think about edge cases and error conditions.

- **Test Thoroughly:** Your test harness is as important as the implementation. Good engineers validate their own work.

- **Documentation:** Explain your design choices. Why did you choose standard I/O vs memory-mapped files? How does your overflow handling work? What trade-offs did you consider?

- **Don't Over-Engineer:** A working, well-tested implementation is better than an over-complicated one. Start simple, then add features if time allows.

---

## Why This Matters for IoT

Ring buffers are everywhere in IoT systems:
- **Sensor Buffering:** Collecting high-frequency sensor data while slower processing happens
- **Communication Queues:** UART, SPI, I2C data buffering
- **Logging:** Circular log buffers that overwrite old entries
- **Audio/Video:** Streaming media buffers
- **Network Packets:** Buffering data between network and application layers

This challenge tests your ability to work with:
- Low-level memory management
- File system APIs
- Data structure implementation
- System programming concepts
- Testing and validation

Good luck! We're excited to see your implementation.
