# EratoFun

An interactive exploration of the Sieve of Eratosthenes and the gaps between composites marked by each prime.

## Explore

The app shows one row for each odd prime up to the square root of the selected sieve limit. It starts marking at that prime's square, skips composites already marked by smaller primes, and records its new marks. A tile counts the `2p`-sized steps between marks (`gap / 2p`), matching the original chart's normalized values. Rows shift right by one position to make their patterns easier to compare. Like the original, the chart omits 2 because the sieve handles even composites separately.

Use the limit slider to change the maximum number in the sieve. Click a prime to show its worked example, and check one or more primes to compare their gap sequences aligned by gap number. The main chart displays up to the first 140 intervals per row. This is a number ceiling, unlike the original generator's `maxPrimeCandidate` setting; the default therefore displays fewer prime rows than the original static table.

## Sammy's conjecture

For a prime `p`, let `c` be the first composite after `p²` that is newly marked by `p`, and let `g = c - p²`. If the first chart tile is `s`, then `g = 2ps`; Sammy's observation is that the next prime `p'` satisfies:

```text
p' = p + g / p
```

Equivalently, the original chart's tile gives `p' = p + 2s`, and `c = p × p'`. Between consecutive primes `p` and `p'`, every composite multiple `p × q` with composite `q` has already been marked by a smaller prime. The next fresh mark is therefore `p × p'`, and its distance from `p²` is `p(p' - p)`. The app converts the selected row's normalized tile back to the full gap `g` before showing Sammy's formula.

## Run locally

Requires Node.js 22 or later.

```sh
npm ci
npm run dev
```

Run the focused sieve tests and create a production build with:

```sh
npm test
npm run build
```

The built site is written to `dist/`. The GitHub Actions workflow deploys it to GitHub Pages when changes are pushed to `master` or when manually triggered. The repository's Pages source must be set to **GitHub Actions**.

`erato.py` is retained as a historical version of the original static table generator; the web app no longer uses it.

_Sam_
