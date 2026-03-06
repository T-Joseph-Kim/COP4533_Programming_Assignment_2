# Project Commit Plan (6 Commits)

## Commit 1: Project skeleton and entry flow
- Create the base Python script structure (`main`, imports, execution guard).
- Add input-loading scaffolding (stdin/file/default file path behavior).
- Verify the program runs without crashing on empty input.

## Commit 2: Input parsing and validation
- Implement `parse_input(data)` for `k`, `m`, and request sequence extraction.
- Add validation checks (`k >= 1`, request count must match `m`).
- Add clear error messages for invalid input formats.

## Commit 3: FIFO cache replacement
- Implement `fifo_misses(k, requests)` using `set` + `deque`.
- Ensure cache hits do not alter miss count.
- Validate FIFO eviction order with small manual test cases.

## Commit 4: LRU cache replacement
- Implement `lru_misses(k, requests)` using `OrderedDict`.
- Update recency on every hit and evict least-recently-used item on miss/full cache.
- Cross-check behavior against known LRU examples.

## Commit 5: OPTFF cache replacement
- Implement `optff_misses(k, requests)` using future-position tracking + heap.
- Handle stale heap entries safely when selecting eviction candidates.
- Validate OPTFF on edge cases (repeated values, no future occurrences).

## Commit 6: Output formatting and final polish
- Wire all algorithms into `main()` and print final counts in required format.
- Clean up naming/comments and remove dead code.
- Run end-to-end checks with sample input files and final review pass.
