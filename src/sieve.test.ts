import { describe, expect, it } from "vitest";
import { buildPrimeGapRows, MAX_SIEVE_LIMIT } from "./sieve";

describe("buildPrimeGapRows", () => {
  it("matches the original normalized gap rows", () => {
    const rows = buildPrimeGapRows(300);
    const rowFor = (prime: number) => rows.find((row) => row.prime === prime);

    expect(rowFor(3)?.markedComposites.slice(0, 4)).toEqual([9, 15, 21, 27]);
    expect(rowFor(3)?.gapSteps.slice(0, 8)).toEqual([1, 1, 1, 1, 1, 1, 1, 1]);
    expect(rowFor(5)?.markedComposites.slice(0, 4)).toEqual([25, 35, 55, 65]);
    expect(rowFor(5)?.gapSteps.slice(0, 4)).toEqual([1, 2, 1, 2]);
    expect(rowFor(7)?.gapSteps.slice(0, 5)).toEqual([2, 1, 2, 1, 2]);
    expect(rowFor(2)).toBeUndefined();
  });

  it("derives the next prime and first new composite from an original gap step", () => {
    const rows = buildPrimeGapRows(100);

    for (const row of rows) {
      const firstGapStep = row.gapSteps[0];
      if (firstGapStep === undefined) continue;

      const gap = firstGapStep * 2 * row.prime;
      const nextPrime = row.prime + gap / row.prime;
      const firstNewComposite = row.markedComposites[1];

      expect(Number.isInteger(nextPrime)).toBe(true);
      expect(firstNewComposite).toBe(row.prime * nextPrime);
    }
  });

  it("retains the original one-position row shift", () => {
    const rows = buildPrimeGapRows(100);

    expect(rows.find((row) => row.prime === 3)?.offset).toBe(1);
    expect(rows.find((row) => row.prime === 5)?.offset).toBe(2);
    expect(rows.find((row) => row.prime === 7)?.offset).toBe(3);
  });

  it("rejects limits outside the supported integer range", () => {
    expect(() => buildPrimeGapRows(1)).toThrow(RangeError);
    expect(() => buildPrimeGapRows(2.5)).toThrow(RangeError);
    expect(() => buildPrimeGapRows(MAX_SIEVE_LIMIT + 1)).toThrow(RangeError);
  });
});
