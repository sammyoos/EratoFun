import { useMemo, useState } from "react";
import { buildPrimeGapRows, MAX_SIEVE_LIMIT, type PrimeGapRow } from "./sieve";

const MIN_LIMIT = 500;
const DEFAULT_LIMIT = 3_000;
const VISIBLE_GAP_COUNT = 140;
const STARTING_COMPARISON = [3, 5, 7];

function gapTone(value: number): number {
  return Math.min(8, Math.ceil(Math.log2(value + 1)));
}

function App() {
  const [limit, setLimit] = useState(DEFAULT_LIMIT);
  const [selectedPrimes, setSelectedPrimes] = useState(STARTING_COMPARISON);
  const [focusedPrime, setFocusedPrime] = useState(3);
  const rows = useMemo(() => buildPrimeGapRows(limit), [limit]);
  const selectedRow = rows.find((row) => row.prime === focusedPrime && row.gapSteps.length > 0)
    ?? rows.find((row) => row.gapSteps.length > 0);
  const firstGapStep = selectedRow?.gapSteps[0];
  const firstActualGap = selectedRow && firstGapStep !== undefined
    ? 2 * selectedRow.prime * firstGapStep
    : undefined;
  const nextPrimeFromGap = selectedRow && firstGapStep !== undefined
    ? selectedRow.prime + 2 * firstGapStep
    : undefined;
  const comparedRows = rows.filter((row) => selectedPrimes.includes(row.prime));
  const maxVisibleGaps = Math.min(
    VISIBLE_GAP_COUNT,
    Math.max(0, ...rows.map((row) => row.gapSteps.length)),
  );
  const gridColumnCount = Math.max(1, ...rows.map((row) => row.offset))
    + maxVisibleGaps;

  function toggleComparison(prime: number) {
    setSelectedPrimes((current) => current.includes(prime)
      ? current.filter((value) => value !== prime)
      : [...current, prime]);
  }

  function focusRow(row: PrimeGapRow) {
    setFocusedPrime(row.prime);
  }

  return (
    <div className="app-shell">
      <header className="site-header">
        <a className="wordmark" href="#top" aria-label="EratoFun home">
          <span className="wordmark-mark" aria-hidden="true">E</span>
          <span>EratoFun</span>
        </a>
        <a className="header-link" href="#sammy-conjecture">Sammy&apos;s conjecture <span aria-hidden="true">↗</span></a>
      </header>

      <main id="top">
        <section className="hero">
          <div className="hero-copy">
            <p className="eyebrow"><span className="eyebrow-dot" /> A hands-on prime-number lab</p>
            <h1>A sieve,<br /><span>seen in the gaps.</span></h1>
            <p className="hero-description">
              The Sieve of Eratosthenes crosses out composites, prime by prime.
              Look at the spaces between each prime&apos;s marks, and a pattern starts to emerge.
            </p>
            <a className="hero-cta" href="#gap-patterns">Explore the pattern <span aria-hidden="true">↓</span></a>
          </div>
          <div className="hero-visual" aria-hidden="true">
            <div className="orbit orbit-one" />
            <div className="orbit orbit-two" />
            <div className="orbit orbit-three" />
            <div className="hero-number">p²</div>
            <span className="orbit-label orbit-label-top">mark</span>
            <span className="orbit-label orbit-label-side">skip</span>
            <span className="orbit-label orbit-label-bottom">repeat</span>
          </div>
        </section>

        <section className="intro-strip" aria-label="How to read the chart">
          <div className="intro-step"><span className="step-number">01</span><p>Start marking at the prime&apos;s square.</p></div>
          <div className="intro-step"><span className="step-number">02</span><p>Skip composites marked by smaller primes.</p></div>
          <div className="intro-step"><span className="step-number">03</span><p>Compare the gaps between new marks.</p></div>
        </section>

        <section className="explorer-section" id="gap-patterns">
          <div className="section-heading">
            <div>
              <p className="eyebrow section-eyebrow">The pattern explorer</p>
              <h2>Every prime leaves a rhythm.</h2>
            </div>
            <p className="section-aside">
              Each row follows an odd prime. Starting at <strong>p²</strong>, a tile counts
              the <strong>2p-sized steps</strong> to the next composite that prime newly marks.
            </p>
          </div>

          <div className="control-card">
            <div className="control-copy">
              <label htmlFor="sieve-limit">Sieve numbers up to</label>
              <p>Raise the limit to reveal more marks and prime rows.</p>
            </div>
            <div className="range-control">
              <output htmlFor="sieve-limit" className="limit-value">{limit.toLocaleString()}</output>
              <input
                id="sieve-limit"
                type="range"
                min={MIN_LIMIT}
                max={MAX_SIEVE_LIMIT}
                step="250"
                value={limit}
                onChange={(event) => setLimit(Number(event.currentTarget.value))}
              />
              <div className="range-ends" aria-hidden="true"><span>{MIN_LIMIT}</span><span>{MAX_SIEVE_LIMIT.toLocaleString()}</span></div>
            </div>
          </div>

          <div className="legend-row">
            <p><span className="legend-chip" /> A tile shows <strong>gap ÷ 2p</strong>, matching the original chart.</p>
            <p>Rows shift right by one place. The original chart omits 2, which marks evens separately.</p>
          </div>

          <div className="table-frame">
            <div className="table-scroll" role="region" aria-label="Prime gap pattern rows" tabIndex={0}>
              <table className="gap-table">
                <thead>
                  <tr>
                    <th scope="col" className="prime-column">Prime</th>
                    <th scope="col" colSpan={gridColumnCount} className="sequence-heading">
                      Gap-step sequence <span>· first {VISIBLE_GAP_COUNT} intervals at most</span>
                    </th>
                  </tr>
                </thead>
                <tbody>
                  {rows.map((row) => (
                    <tr
                      key={row.prime}
                      className={selectedPrimes.includes(row.prime) ? "is-compared" : ""}
                    >
                      <th scope="row" className="prime-column">
                        <div className="prime-controls">
                          <button
                            type="button"
                            className="prime-focus"
                            aria-label={`Explain the row for prime ${row.prime}`}
                            aria-pressed={selectedRow?.prime === row.prime}
                            onClick={() => focusRow(row)}
                          >
                            {row.prime}
                          </button>
                          <label className="compare-check" title={`Compare prime ${row.prime}`}>
                            <input
                              type="checkbox"
                              checked={selectedPrimes.includes(row.prime)}
                              onChange={() => toggleComparison(row.prime)}
                              aria-label={`Compare prime ${row.prime}`}
                            />
                          </label>
                        </div>
                      </th>
                      {row.offset > 0 && <td className="offset-cell" colSpan={row.offset} aria-hidden="true" />}
                      {row.gapSteps.slice(0, VISIBLE_GAP_COUNT).map((gapStep, index) => (
                        <td
                          key={`${row.prime}-${index}`}
                          className={`gap-cell tone-${gapTone(gapStep)}`}
                          title={`Gap ${index + 1}: ${gapStep} steps of ${2 * row.prime} (${gapStep * 2 * row.prime} integers)`}
                        >
                          {gapStep}
                        </td>
                      ))}
                      {row.gapSteps.length > VISIBLE_GAP_COUNT && (
                        <td className="more-cell" title={`${row.gapSteps.length - VISIBLE_GAP_COUNT} more intervals`}>
                          +{row.gapSteps.length - VISIBLE_GAP_COUNT}
                        </td>
                      )}
                      {row.gapSteps.length === 0 && (
                        <td className="empty-cell">No new marks in this range</td>
                      )}
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
            <div className="table-foot">
              <span><span className="compare-dot" /> Select checkboxes to compare rows below</span>
              <span>{rows.length} prime rows · {limit.toLocaleString()} numbers sieved</span>
            </div>
          </div>

          {comparedRows.length > 0 && (
            <section className="comparison-panel" aria-labelledby="comparison-title">
              <div className="comparison-heading">
                <div>
                  <p className="eyebrow">Side by side</p>
                  <h3 id="comparison-title">Compare selected rows</h3>
                </div>
                <p>Tiles line up by gap number so the sequences are easy to scan.</p>
              </div>
              <div className="compare-scroll" role="region" aria-label="Selected prime rows compared by gap number" tabIndex={0}>
                <table className="compare-table">
                  <thead>
                    <tr>
                      <th scope="col">Prime</th>
                      {Array.from({ length: maxVisibleGaps }, (_, index) => (
                        <th scope="col" key={index}>{index + 1}</th>
                      ))}
                    </tr>
                  </thead>
                  <tbody>
                    {comparedRows.map((row) => (
                      <tr key={row.prime}>
                        <th scope="row">{row.prime}</th>
                        {row.gapSteps.slice(0, maxVisibleGaps).map((gapStep, index) => (
                          <td key={`${row.prime}-${index}`} className={`gap-cell tone-${gapTone(gapStep)}`}>
                            {gapStep}
                          </td>
                        ))}
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </section>
          )}
        </section>

        <section className="conjecture-section" id="sammy-conjecture">
          <div className="conjecture-copy">
            <p className="eyebrow section-eyebrow">The observation</p>
            <h2>Sammy&apos;s<br />conjecture.</h2>
            <p>
              Take a prime <em>p</em>, then find the next composite <em>c</em> after <em>p²</em>
              that wasn&apos;t already crossed out by a smaller prime. Let <em>g</em> be that gap:
              <em> g = c − p²</em>.
            </p>
            <p>
              The gap is always divisible by <em>p</em>. Add <em>g/p</em> to <em>p</em>, and
              you get the next prime, <em>p′</em>. The new composite is their product.
            </p>
          </div>
          <div className="equation-card">
            <div className="equation-topline">
              <span className="equation-tag">Try a row</span>
              {selectedRow ? (
                <span className="equation-prime">
                  <span className="focus-indicator" />
                  p = {selectedRow.prime}
                </span>
              ) : <span className="equation-prime">Choose a row above</span>}
            </div>
            {selectedRow && firstGapStep !== undefined && firstActualGap !== undefined && nextPrimeFromGap !== undefined ? (
              <>
                <p className="equation-caption">The first gap after p² · {firstGapStep} steps of 2p</p>
                <p className="equation-line">
                  <span className="equation-variable">g</span>
                  <span className="equation-equals">=</span>
                  <span>{firstActualGap}</span>
                  <span className="equation-unit">integers</span>
                </p>
                <div className="equation-divider" />
                <p className="equation-line equation-main">
                  <span className="equation-variable">p′</span>
                  <span className="equation-equals">=</span>
                  <span>{selectedRow.prime} + {firstActualGap} / {selectedRow.prime}</span>
                  <span className="equation-equals">=</span>
                  <strong>{nextPrimeFromGap}</strong>
                </p>
                <p className="equation-result">
                  c = {selectedRow.markedComposites[1]} = {selectedRow.prime} × {nextPrimeFromGap}
                </p>
              </>
            ) : (
              <p className="no-gap-message">Increase the sieve limit to reveal the next newly marked composite for this prime.</p>
            )}
          </div>
        </section>

        <section className="why-section">
          <span className="why-icon" aria-hidden="true">↗</span>
          <div>
            <p className="eyebrow">Why this works</p>
            <p>
              Between consecutive primes <em>p</em> and <em>p′</em>, every composite multiple
              <em> p × q</em> with composite <em>q</em> has already been marked by a smaller
              prime. So the next fresh mark is <em>p × p′</em>; its distance from <em>p²</em> is
              <em> p(p′ − p)</em>. The relationship follows directly from how the sieve works.
            </p>
          </div>
        </section>
      </main>

      <footer className="site-footer">
        <a className="wordmark footer-wordmark" href="#top"><span className="wordmark-mark" aria-hidden="true">E</span><span>EratoFun</span></a>
        <p>A little more curiosity, one prime at a time.</p>
        <a href="https://github.com/sammyoos/EratoFun">View the project <span aria-hidden="true">↗</span></a>
      </footer>
    </div>
  );
}

export default App;
