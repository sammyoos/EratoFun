export const MAX_SIEVE_LIMIT = 10_000;

export interface PrimeGapRow {
  prime: number;
  offset: number;
  markedComposites: number[];
  gapSteps: number[];
}

export function buildPrimeGapRows(limit: number): PrimeGapRow[] {
  if (!Number.isInteger(limit) || limit < 2 || limit > MAX_SIEVE_LIMIT) {
    throw new RangeError(`The sieve limit must be an integer from 2 to ${MAX_SIEVE_LIMIT}.`);
  }

  const firstMarker = new Uint16Array(limit + 1);
  const rows: PrimeGapRow[] = [];

  for (let prime = 3; prime * prime <= limit; prime += 2) {
    if (firstMarker[prime] !== 0) continue;

    const markedComposites: number[] = [];
    for (let composite = prime * prime; composite <= limit; composite += 2 * prime) {
      if (firstMarker[composite] === 0) {
        firstMarker[composite] = prime;
        markedComposites.push(composite);
      }
    }

    const gapSteps = markedComposites.slice(1).map((composite, index) => {
      const gap = composite - markedComposites[index];
      const stepSize = 2 * prime;
      if (gap % stepSize !== 0) {
        throw new Error(`Unexpected gap ${gap} for prime ${prime}.`);
      }
      return gap / stepSize;
    });

    rows.push({
      prime,
      offset: rows.length + 1,
      markedComposites,
      gapSteps,
    });
  }

  return rows;
}
