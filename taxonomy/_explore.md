# Explore metrics

A filterable view over all 221 metrics in the taxonomy. Pick filters on the left; the table on the right updates live. Click any ref-ID to jump to the metric's full body.

!!! note "Starting point — same caveat as everywhere else"

    The filters here are aids for finding metrics, not authoritative classifications. Tier assignments, applicability labels, and dimensional values are taxonomy-proposed starting points (see [How to use](how-to-use.md) and the [Calibration & Context principle](calibration-and-context.md)). A metric appearing or not appearing under a given filter is not a substitute for reading its body and calibrating to your deployment context.

<style>
  .explorer-wrapper { display: grid; grid-template-columns: 240px 1fr; gap: 1.5rem; margin-top: 1rem; }
  @media (max-width: 800px) { .explorer-wrapper { grid-template-columns: 1fr; } }
  .explorer-filters { font-size: 0.85rem; }
  .explorer-filters fieldset { border: 1px solid var(--md-default-fg-color--lightest); border-radius: 4px; padding: 0.5rem 0.75rem; margin: 0 0 0.75rem 0; }
  .explorer-filters legend { font-weight: 600; padding: 0 0.4rem; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.04em; }
  .explorer-filters select, .explorer-filters input[type="search"] { width: 100%; padding: 0.3rem 0.4rem; border-radius: 4px; border: 1px solid var(--md-default-fg-color--lightest); background: var(--md-default-bg-color); color: var(--md-default-fg-color); }
  .explorer-filters .reset-btn { width: 100%; padding: 0.4rem; border-radius: 4px; border: 1px solid var(--md-default-fg-color--lightest); background: var(--md-default-bg-color); color: var(--md-default-fg-color); cursor: pointer; }
  .explorer-filters .reset-btn:hover { background: var(--md-default-fg-color--lightest); }
  .explorer-results { font-size: 0.9rem; }
  .explorer-summary { padding: 0.5rem 0.75rem; background: var(--md-default-fg-color--lightest); border-radius: 4px; margin-bottom: 0.75rem; font-size: 0.85rem; }
  .explorer-table { width: 100%; border-collapse: collapse; }
  .explorer-table th, .explorer-table td { text-align: left; padding: 0.5rem 0.6rem; border-bottom: 1px solid var(--md-default-fg-color--lightest); vertical-align: top; }
  .explorer-table th { background: var(--md-default-fg-color--lightest); font-weight: 600; cursor: pointer; user-select: none; }
  .explorer-table th:hover { background: var(--md-accent-fg-color--transparent); }
  .explorer-table th.sort-asc::after { content: " ▲"; opacity: 0.6; }
  .explorer-table th.sort-desc::after { content: " ▼"; opacity: 0.6; }
  .explorer-table tr:hover { background: var(--md-default-fg-color--lightest); }
  .explorer-table .refid { font-family: var(--md-code-font); white-space: nowrap; }
  .explorer-table .tier-icon { font-size: 1rem; }
  .explorer-empty { padding: 2rem; text-align: center; color: var(--md-default-fg-color--light); font-style: italic; }
  .explorer-loading { padding: 2rem; text-align: center; color: var(--md-default-fg-color--light); }
</style>

<div class="explorer-wrapper">
  <aside class="explorer-filters" aria-label="Metric filters">
    <fieldset>
      <legend>Search</legend>
      <input type="search" id="ex-search" placeholder="Name, ref-ID, group…" aria-label="Free-text search" />
    </fieldset>
    <fieldset>
      <legend>Tier</legend>
      <select id="ex-tier" aria-label="Tier filter">
        <option value="">All tiers</option>
      </select>
    </fieldset>
    <fieldset>
      <legend>Cluster</legend>
      <select id="ex-cluster" aria-label="Cluster filter">
        <option value="">All clusters</option>
      </select>
    </fieldset>
    <fieldset>
      <legend>Group</legend>
      <select id="ex-group" aria-label="Group filter">
        <option value="">All groups</option>
      </select>
    </fieldset>
    <fieldset>
      <legend>Cadence</legend>
      <select id="ex-cadence" aria-label="Measurement cadence">
        <option value="">All cadences</option>
      </select>
    </fieldset>
    <fieldset>
      <legend>Responsible actor</legend>
      <select id="ex-actor" aria-label="Responsible actor">
        <option value="">All actors</option>
      </select>
    </fieldset>
    <fieldset>
      <legend>Applicability</legend>
      <select id="ex-applicability" aria-label="Applicability">
        <option value="">All applicability</option>
      </select>
    </fieldset>
    <fieldset>
      <legend>Lifecycle phase</legend>
      <select id="ex-lifecycle" aria-label="Lifecycle phase">
        <option value="">All lifecycle phases</option>
      </select>
    </fieldset>
    <fieldset>
      <legend>Pipeline layer</legend>
      <select id="ex-layer" aria-label="Pipeline layer">
        <option value="">All layers</option>
      </select>
    </fieldset>
    <fieldset>
      <legend>Maturity</legend>
      <select id="ex-maturity" aria-label="Maturity">
        <option value="">All maturity</option>
      </select>
    </fieldset>
    <button type="button" class="reset-btn" id="ex-reset">Reset all filters</button>
  </aside>

  <div class="explorer-results">
    <div class="explorer-summary" id="ex-summary">Loading metrics…</div>
    <div id="ex-table-wrap"><div class="explorer-loading">Loading…</div></div>
  </div>
</div>

<script>
(function() {
  const METRICS_URL = '../downloads/metrics.json';
  // Cluster order matches the canonical TP → PI → HL → IO → GV → ES sequence
  // used everywhere else in the taxonomy. Used for stable default sort
  // and for the cluster filter dropdown.
  const CLUSTER_ORDER = ['TP', 'PI', 'HL', 'IO', 'GV', 'ES'];
  const CLUSTER_RANK = Object.fromEntries(CLUSTER_ORDER.map((c, i) => [c, i]));

  const FIELDS = {
    tier: { id: 'ex-tier', dim: null, getter: m => m.tier_label, label: 'Tier',
            sortKey: m => m.tier },
    cluster: { id: 'ex-cluster', dim: null, getter: m => m.cluster_name, label: 'Cluster',
               sortKey: m => CLUSTER_RANK[m.cluster] ?? 99 },
    group: { id: 'ex-group', dim: null, getter: m => m.group, label: 'Group' },
    cadence: { id: 'ex-cadence', dim: 'Measurement Cadence', label: 'Cadence' },
    actor: { id: 'ex-actor', dim: 'Responsible Actors', label: 'Actor', multi: true },
    applicability: { id: 'ex-applicability', dim: 'Applicability', label: 'Applicability' },
    lifecycle: { id: 'ex-lifecycle', dim: 'Lifecycle Phases', label: 'Lifecycle phase', multi: true },
    layer: { id: 'ex-layer', dim: 'Pipeline Layer', label: 'Pipeline layer' },
    maturity: { id: 'ex-maturity', dim: 'Maturity', label: 'Maturity' },
  };

  const state = { metrics: [], filters: {}, sort: { col: 'ref_id', dir: 'asc' } };

  // Hash-based persistence: filters serialize to URL hash so views are shareable.
  function readHash() {
    const hash = location.hash.replace(/^#/, '');
    if (!hash) return {};
    const out = {};
    for (const pair of hash.split('&')) {
      const [k, v] = pair.split('=');
      if (k && v) out[decodeURIComponent(k)] = decodeURIComponent(v);
    }
    return out;
  }
  function writeHash() {
    const parts = [];
    for (const [k, v] of Object.entries(state.filters)) {
      if (v) parts.push(encodeURIComponent(k) + '=' + encodeURIComponent(v));
    }
    if (state.sort.col !== 'ref_id' || state.sort.dir !== 'asc') {
      parts.push('sort=' + state.sort.col + ':' + state.sort.dir);
    }
    const newHash = parts.length ? '#' + parts.join('&') : '';
    if (newHash !== location.hash) {
      history.replaceState(null, '', location.pathname + location.search + newHash);
    }
  }

  // Field value extraction: dimensions can be "A, B" (multi) or "A" (single).
  function getValues(metric, key) {
    const f = FIELDS[key];
    if (f.getter) return [f.getter(metric)];
    const raw = metric.dimensions[f.dim] || '';
    if (f.multi) return raw.split(',').map(s => s.trim()).filter(Boolean);
    return [raw];
  }

  function uniqueSorted(values, customCmp) {
    const arr = [...new Set(values.filter(Boolean))];
    arr.sort(customCmp || ((a, b) => a.localeCompare(b)));
    return arr;
  }

  function populateSelect(key) {
    const f = FIELDS[key];
    const sel = document.getElementById(f.id);
    if (!sel) return;
    let valueRanks = null;
    if (f.sortKey) {
      // Build label → rank map from the metric corpus so the dropdown
      // sorts in the same order the data is naturally arranged.
      valueRanks = new Map();
      for (const m of state.metrics) {
        for (const v of getValues(m, key)) {
          if (v && !valueRanks.has(v)) valueRanks.set(v, f.sortKey(m));
        }
      }
    }
    const all = state.metrics.flatMap(m => getValues(m, key));
    const cmp = valueRanks
      ? (a, b) => (valueRanks.get(a) ?? 0) - (valueRanks.get(b) ?? 0) || a.localeCompare(b)
      : null;
    for (const v of uniqueSorted(all, cmp)) {
      const opt = document.createElement('option');
      opt.value = v;
      opt.textContent = v;
      sel.appendChild(opt);
    }
    if (state.filters[key]) sel.value = state.filters[key];
    sel.addEventListener('change', () => {
      state.filters[key] = sel.value;
      writeHash();
      render();
    });
  }

  function metricMatches(m) {
    // Free-text search
    const q = (state.filters.q || '').toLowerCase().trim();
    if (q) {
      const hay = (m.ref_id + ' ' + m.name + ' ' + m.group + ' ' + m.cluster_name).toLowerCase();
      if (!hay.includes(q)) return false;
    }
    for (const key of Object.keys(FIELDS)) {
      const want = state.filters[key];
      if (!want) continue;
      const have = getValues(m, key);
      if (!have.includes(want)) return false;
    }
    return true;
  }

  const COLUMNS = [
    { key: 'ref_id', label: 'Ref' },
    { key: 'name', label: 'Name' },
    { key: 'tier_label', label: 'Tier' },
    { key: 'cluster', label: 'Cluster', getter: m => m.cluster_name || m.cluster },
    { key: 'group', label: 'Group' },
    { key: 'cadence', label: 'Cadence', getter: m => m.dimensions['Measurement Cadence'] || '' },
    { key: 'actor', label: 'Actor', getter: m => m.dimensions['Responsible Actors'] || '' },
    { key: 'applicability', label: 'Applicability', getter: m => m.applicability || '' },
  ];

  function colValue(m, col) {
    if (col.getter) return col.getter(m);
    return m[col.key] || '';
  }

  function refIdToAnchor(refId) { return refId.toLowerCase().replace(/\./g, '-'); }
  function metricLink(m) {
    // /explore/ is a sibling of /groups/, so the relative path needs ../
    // to escape the explore/ directory before descending into groups/.
    const slug = m.group_file.replace(/\.md$/, '').split('/').pop();
    return '../groups/' + slug + '/#' + refIdToAnchor(m.ref_id);
  }

  function render() {
    const filtered = state.metrics.filter(metricMatches);
    // Sort
    const sortCol = COLUMNS.find(c => c.key === state.sort.col) || COLUMNS[0];
    filtered.sort((a, b) => {
      let cmp;
      if (sortCol.key === 'tier_label') {
        // Tier-numeric (1 / 2 / 3), not alphabetic on label.
        cmp = a.tier - b.tier;
      } else if (sortCol.key === 'ref_id') {
        // Default natural order: use the index in metrics.json directly.
        // build_site emits metrics in the canonical TP→PI→HL→IO→GV→ES
        // sequence with each group in its build.py order, so this is the
        // "as-listed" view a reader of the catalogue would expect.
        cmp = (a._idx ?? 0) - (b._idx ?? 0);
      } else if (sortCol.key === 'cluster') {
        cmp = (CLUSTER_RANK[a.cluster] ?? 99) - (CLUSTER_RANK[b.cluster] ?? 99);
      } else {
        const av = String(colValue(a, sortCol)).toLowerCase();
        const bv = String(colValue(b, sortCol)).toLowerCase();
        cmp = av.localeCompare(bv);
      }
      return state.sort.dir === 'asc' ? cmp : -cmp;
    });

    // Summary
    const summary = document.getElementById('ex-summary');
    const total = state.metrics.length;
    const t1 = filtered.filter(m => m.tier === 1).length;
    const t2 = filtered.filter(m => m.tier === 2).length;
    const t3 = filtered.filter(m => m.tier === 3).length;
    summary.textContent = `Showing ${filtered.length} of ${total} metrics — 🟢 ${t1} · 🟡 ${t2} · 🔵 ${t3}`;

    // Table
    const wrap = document.getElementById('ex-table-wrap');
    if (filtered.length === 0) {
      wrap.innerHTML = '<div class="explorer-empty">No metrics match these filters. <a href="#" id="ex-reset-inline">Reset?</a></div>';
      const link = document.getElementById('ex-reset-inline');
      if (link) link.addEventListener('click', e => { e.preventDefault(); resetFilters(); });
      return;
    }

    let html = '<table class="explorer-table"><thead><tr>';
    for (const col of COLUMNS) {
      const cls = col.key === state.sort.col ? ('sort-' + state.sort.dir) : '';
      html += `<th data-col="${col.key}" class="${cls}">${col.label}</th>`;
    }
    html += '</tr></thead><tbody>';
    for (const m of filtered) {
      const link = metricLink(m);
      html += '<tr>';
      html += `<td class="refid"><a href="${link}">${m.ref_id}</a></td>`;
      html += `<td>${escapeHtml(m.name)}</td>`;
      html += `<td><span class="tier-icon">${m.tier_icon}</span> ${escapeHtml(m.tier_label)}</td>`;
      html += `<td>${escapeHtml(m.cluster_name || m.cluster)}</td>`;
      html += `<td>${escapeHtml(m.group)}</td>`;
      html += `<td>${escapeHtml(m.dimensions['Measurement Cadence'] || '')}</td>`;
      html += `<td>${escapeHtml(m.dimensions['Responsible Actors'] || '')}</td>`;
      html += `<td>${escapeHtml(m.applicability || '')}</td>`;
      html += '</tr>';
    }
    html += '</tbody></table>';
    wrap.innerHTML = html;

    // Sort header click handlers
    for (const th of wrap.querySelectorAll('th[data-col]')) {
      th.addEventListener('click', () => {
        const col = th.dataset.col;
        if (state.sort.col === col) {
          state.sort.dir = state.sort.dir === 'asc' ? 'desc' : 'asc';
        } else {
          state.sort.col = col;
          state.sort.dir = 'asc';
        }
        writeHash();
        render();
      });
    }
  }

  function escapeHtml(s) {
    return String(s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  }

  function resetFilters() {
    state.filters = {};
    state.sort = { col: 'ref_id', dir: 'asc' };
    document.getElementById('ex-search').value = '';
    for (const f of Object.values(FIELDS)) {
      const sel = document.getElementById(f.id);
      if (sel) sel.value = '';
    }
    writeHash();
    render();
  }

  async function init() {
    // Hash → state
    const hash = readHash();
    state.filters = {};
    if (hash.q) state.filters.q = hash.q;
    for (const k of Object.keys(FIELDS)) if (hash[k]) state.filters[k] = hash[k];
    if (hash.sort) {
      const [col, dir] = hash.sort.split(':');
      if (col && (dir === 'asc' || dir === 'desc')) state.sort = { col, dir };
    }

    // Fetch
    try {
      const res = await fetch(METRICS_URL);
      if (!res.ok) throw new Error('HTTP ' + res.status);
      const data = await res.json();
      state.metrics = (data.metrics || []).map((m, i) => ({ ...m, _idx: i }));
    } catch (err) {
      document.getElementById('ex-summary').textContent = 'Error loading metrics.json — see console for details.';
      document.getElementById('ex-table-wrap').innerHTML = '<div class="explorer-empty">Could not load metrics data.</div>';
      console.error('Failed to load metrics:', err);
      return;
    }

    // Wire up
    const search = document.getElementById('ex-search');
    if (state.filters.q) search.value = state.filters.q;
    search.addEventListener('input', () => {
      state.filters.q = search.value;
      writeHash();
      render();
    });
    for (const key of Object.keys(FIELDS)) populateSelect(key);
    document.getElementById('ex-reset').addEventListener('click', resetFilters);

    // Hash navigation (back/forward) keeps filters in sync
    window.addEventListener('hashchange', () => {
      const h = readHash();
      state.filters = {};
      if (h.q) state.filters.q = h.q;
      for (const k of Object.keys(FIELDS)) if (h[k]) state.filters[k] = h[k];
      document.getElementById('ex-search').value = state.filters.q || '';
      for (const [key, f] of Object.entries(FIELDS)) {
        const sel = document.getElementById(f.id);
        if (sel) sel.value = state.filters[key] || '';
      }
      render();
    });

    render();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
</script>
