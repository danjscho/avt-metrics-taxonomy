# Explore metrics

Two views over all 221 metrics:

- **Matrix** — visual cluster × tier grid. Drag a metric card between tier rows to see what a re-tiering would look like. Local what-if only — refresh resets.
- **Table** — filterable table beneath the matrix, identical filter set, identical filtered subset. Click any ref-ID to jump to the metric body.

!!! warning "Drag-and-drop is a *local what-if* only"

    Re-tiering a metric in the matrix is a thinking aid. It does **not** edit the catalogue, propose a change, or persist across page refreshes. The bottom-left "Modified assignments" panel lists every move so you can see your what-if state and revert. Tier assignments in the canonical taxonomy are author-judgement starting points (see [How to use](how-to-use.md) and [Calibration & Context](calibration-and-context.md)); local re-tiering against deployment context is exactly what the [Calibration & Context principle](calibration-and-context.md) names. Use this view to think out loud, screenshot, share — not to publish.

<style>
  .ex-toolbar { display: flex; gap: 0.5rem; align-items: center; flex-wrap: wrap; margin-bottom: 0.5rem; }
  .ex-toolbar button { padding: 0.3rem 0.7rem; border-radius: 4px; border: 1px solid var(--md-default-fg-color--lightest); background: var(--md-default-bg-color); color: var(--md-default-fg-color); cursor: pointer; font-size: 0.85rem; }
  .ex-toolbar button:hover { background: var(--md-default-fg-color--lightest); }
  .ex-toolbar .ex-summary-inline { font-size: 0.85rem; color: var(--md-default-fg-color--light); margin-left: auto; }

  .matrix-filter-strip { display: flex; gap: 0.6rem; align-items: center; flex-wrap: wrap; padding: 0.5rem 0.75rem; background: var(--md-default-fg-color--lightest); border-radius: 4px; margin-bottom: 0.5rem; font-size: 0.85rem; }
  .matrix-filter-strip label { font-weight: 600; font-size: 0.78rem; text-transform: uppercase; letter-spacing: 0.04em; color: var(--md-default-fg-color--light); }
  .matrix-filter-strip select, .matrix-filter-strip input[type="search"] { padding: 0.25rem 0.45rem; border-radius: 3px; border: 1px solid var(--md-default-fg-color--lightest); background: var(--md-default-bg-color); color: var(--md-default-fg-color); font-size: 0.85rem; }
  .matrix-filter-strip input[type="search"] { min-width: 180px; }
  .matrix-filter-strip select { min-width: 160px; }
  .matrix-filter-strip .strip-spacer { flex: 1; }
  .matrix-filter-strip .strip-hint { font-size: 0.75rem; color: var(--md-default-fg-color--light); font-style: italic; }
  .matrix-filter-strip a.scroll-link { font-size: 0.78rem; color: var(--md-default-fg-color--light); }

  .matrix-wrap { margin: 1rem 0 2rem; }
  /* Layout: 1 row-label column + 3 tier columns (or 1 row-label + N when
     a cluster is focused, where each row is a group inside the cluster).
     The row axis is the cluster (or group when focused); the column axis
     is always tier (1/2/3). Three tier columns + a label column fits any
     reasonable viewport without horizontal scroll. */
  .matrix-grid { display: grid; grid-template-columns: 140px repeat(3, minmax(220px, 1fr)); gap: 4px; }
  .matrix-corner, .matrix-cluster-header, .matrix-tier-header, .matrix-row-header { padding: 0.4rem 0.5rem; font-weight: 600; font-size: 0.8rem; text-align: center; background: var(--md-default-fg-color--lightest); border-radius: 3px; user-select: none; }
  .matrix-tier-header { font-size: 0.85rem; }
  /* Row labels (cluster or group) on the left. Top-aligned so the label
     stays visible at the top of the row even when the row is very tall
     (GV/Tier-2 spans 2000+ px). align-self: start prevents the grid
     from stretching the header vertically; the visible header is then
     a compact box at the top of the row. */
  .matrix-row-header { display: flex; align-items: flex-start; justify-content: flex-start; text-align: left; font-size: 0.78rem; text-transform: uppercase; letter-spacing: 0.03em; line-height: 1.25; padding: 0.5rem 0.6rem; align-self: start; }
  .matrix-cell { background: var(--md-default-bg-color); border: 1px dashed var(--md-default-fg-color--lightest); border-radius: 3px; padding: 4px; min-height: 90px; display: flex; flex-direction: column; gap: 4px; align-content: flex-start; transition: background 80ms ease, border-color 80ms ease; }
  .matrix-cell.drag-over { background: var(--md-accent-fg-color--transparent); border-color: var(--md-accent-fg-color); border-style: solid; }
  .matrix-card { font-size: 0.7rem; padding: 4px 6px; border-radius: 3px; background: var(--md-default-fg-color--lightest); cursor: grab; user-select: none; line-height: 1.3; border-left: 3px solid transparent; display: flex; flex-direction: column; gap: 1px; }
  .matrix-card:hover { background: var(--md-accent-fg-color--transparent); }
  .matrix-card[draggable="true"]:active { cursor: grabbing; }
  .matrix-card .card-ref { font-family: var(--md-code-font); font-weight: 600; white-space: nowrap; }
  .matrix-card .card-name { font-size: 0.68rem; color: var(--md-default-fg-color--light); overflow: hidden; text-overflow: ellipsis; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; }
  .matrix-card.tier-1 { border-left-color: #4caf50; }
  .matrix-card.tier-2 { border-left-color: #ff9800; }
  .matrix-card.tier-3 { border-left-color: #2196f3; }
  .matrix-card.moved { box-shadow: 0 0 0 2px var(--md-accent-fg-color); }
  .matrix-card.dragging { opacity: 0.4; }
  .matrix-card a { color: inherit; text-decoration: none; }
  .matrix-card a:hover { text-decoration: underline; }
  .matrix-cell-empty { color: var(--md-default-fg-color--light); font-style: italic; font-size: 0.7rem; padding: 0.5rem; text-align: center; width: 100%; }
  .matrix-focus-banner { padding: 0.4rem 0.7rem; background: var(--md-accent-fg-color--transparent); border-radius: 4px; font-size: 0.8rem; margin-bottom: 0.5rem; display: flex; align-items: center; gap: 0.5rem; }
  .matrix-focus-banner button { font-size: 0.75rem; padding: 0.2rem 0.5rem; background: var(--md-default-bg-color); border: 1px solid var(--md-default-fg-color--lightest); border-radius: 3px; cursor: pointer; }

  .moves-panel { margin-top: 0.75rem; padding: 0.6rem 0.8rem; border-radius: 4px; border: 1px solid var(--md-default-fg-color--lightest); background: var(--md-default-fg-color--lightest); font-size: 0.85rem; }
  .moves-panel.empty { display: none; }
  .moves-panel h4 { margin: 0 0 0.4rem; font-size: 0.85rem; }
  .moves-list { list-style: none; padding: 0; margin: 0; max-height: 180px; overflow-y: auto; }
  .moves-list li { display: flex; align-items: center; gap: 0.5rem; padding: 0.15rem 0; font-family: var(--md-code-font); font-size: 0.75rem; }
  .moves-list .move-revert { background: none; border: 1px solid var(--md-default-fg-color--lightest); border-radius: 2px; padding: 1px 6px; cursor: pointer; font-size: 0.7rem; color: var(--md-default-fg-color--light); }
  .moves-list .move-revert:hover { color: var(--md-default-fg-color); border-color: var(--md-default-fg-color--light); }

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

## Matrix view

<div class="matrix-filter-strip" aria-label="Matrix-specific quick filters">
  <label for="mx-search">Search</label>
  <input type="search" id="mx-search" placeholder="Name, ref-ID, group…" aria-label="Free-text search (matrix)" />
  <label for="mx-cluster">Focus cluster</label>
  <select id="mx-cluster" aria-label="Focus a single cluster">
    <option value="">All clusters</option>
  </select>
  <span class="strip-spacer"></span>
  <span class="strip-hint">Use the filter sidebar below for more dimensions.</span>
</div>

<div class="ex-toolbar">
  <button type="button" id="matrix-reset-moves">Reset all moves</button>
  <span class="ex-summary-inline" id="matrix-summary">Loading…</span>
</div>

<div class="matrix-focus-banner" id="matrix-focus-banner" style="display:none">
  <span id="matrix-focus-text"></span>
  <button type="button" id="matrix-focus-clear">Show all clusters</button>
</div>

<div class="matrix-wrap">
  <div class="matrix-grid" id="matrix-grid" aria-label="Cluster × tier matrix">
    <!-- corner + headers + cells inserted by JS -->
  </div>
</div>

<div class="moves-panel empty" id="moves-panel">
  <h4>Modified tier assignments</h4>
  <ul class="moves-list" id="moves-list"></ul>
</div>

## Table view

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
  // Cluster order matches the canonical TP → PI → HL → IO → GV → ES sequence.
  const CLUSTER_ORDER = ['TP', 'PI', 'HL', 'IO', 'GV', 'ES'];
  const CLUSTER_RANK = Object.fromEntries(CLUSTER_ORDER.map((c, i) => [c, i]));
  // Cluster short labels for matrix headers (avoids wrapping at narrow widths).
  const CLUSTER_LABELS = {
    TP: 'TP — Technical Pipeline',
    PI: 'PI — Pipeline Interactions',
    HL: 'HL — Human Layer',
    IO: 'IO — Impact & Outcomes',
    GV: 'GV — System Governance',
    ES: 'ES — Eval Science',
  };
  const TIER_LABELS = { 1: '🟢 Tier 1', 2: '🟡 Tier 2', 3: '🔵 Tier 3' };
  // Map a tier number to the label used in the table column / filter
  // dropdown (matches metric.tier_label produced by build_site).
  const TIER_LABEL_FOR_TIER = { 1: 'Minimum Viable', 2: 'Recommended', 3: 'Advanced / Research' };

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

  const state = {
    metrics: [],
    filters: {},
    sort: { col: 'ref_id', dir: 'asc' },
    // moves[ref_id] = { from: 1|2|3, to: 1|2|3 }. Original tier in `from`,
    // current effective tier in `to`. Only present for moved metrics.
    moves: {},
  };

  function effectiveTier(m) {
    return state.moves[m.ref_id] ? state.moves[m.ref_id].to : m.tier;
  }

  // ---------- Hash persistence ----------
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

  // ---------- Field extraction ----------
  function getValues(metric, key) {
    const f = FIELDS[key];
    if (key === 'tier') return [TIER_LABEL_FOR_TIER[effectiveTier(metric)] || metric.tier_label];
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

  // Apply a filter change from any control. Updates state, writes hash,
  // re-renders, and syncs every <select> bound to the same key so the
  // matrix-strip dropdown and the sidebar dropdown stay in lock-step.
  function setFilter(key, value) {
    if (value) state.filters[key] = value;
    else delete state.filters[key];
    writeHash();
    syncControls();
    renderAll();
  }

  function syncControls() {
    // Sync each select bound to a filter key
    for (const [key, f] of Object.entries(FIELDS)) {
      const v = state.filters[key] || '';
      for (const id of [f.id, ...(EXTRA_SELECT_IDS[key] || [])]) {
        const sel = document.getElementById(id);
        if (sel && sel.value !== v) sel.value = v;
      }
    }
    // Sync search inputs
    const q = state.filters.q || '';
    for (const id of ['ex-search', 'mx-search']) {
      const inp = document.getElementById(id);
      if (inp && inp.value !== q) inp.value = q;
    }
  }

  // Map filter keys to extra <select> ids beyond FIELDS[key].id (for the
  // matrix-strip duplicates).
  const EXTRA_SELECT_IDS = {
    cluster: ['mx-cluster'],
  };

  function fillSelectOptions(key, sel) {
    if (!sel) return;
    const f = FIELDS[key];
    let valueRanks = null;
    if (f.sortKey) {
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
  }

  function populateSelect(key) {
    const f = FIELDS[key];
    const sel = document.getElementById(f.id);
    if (!sel) return;
    fillSelectOptions(key, sel);
    if (state.filters[key]) sel.value = state.filters[key];
    sel.addEventListener('change', () => setFilter(key, sel.value));

    // Also populate any matrix-strip duplicate of this filter
    for (const extraId of EXTRA_SELECT_IDS[key] || []) {
      const dup = document.getElementById(extraId);
      if (dup) {
        fillSelectOptions(key, dup);
        if (state.filters[key]) dup.value = state.filters[key];
        dup.addEventListener('change', () => setFilter(key, dup.value));
      }
    }
  }

  // ---------- Filter ----------
  function metricMatches(m) {
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

  // ---------- Matrix render ----------
  // Layout: tiers are always columns (Tier 1 / Tier 2 / Tier 3, left to
  // right). Rows depend on focus mode:
  //   Mode A (default): rows = clusters (TP / PI / HL / IO / GV / ES).
  //   Mode B (cluster focus set): rows = groups within the focused cluster.
  // Three tier columns + a label column fits any viewport without horizontal
  // scroll, and dragging left-to-right matches the "more important / less
  // important" tier intuition.
  function focusedCluster() {
    const want = state.filters.cluster;
    if (!want) return null;
    // Map cluster_name back to the 2-letter code so the filter and matrix agree.
    for (const m of state.metrics) {
      if (m.cluster_name === want) return m.cluster;
    }
    return null;
  }

  function groupsInCluster(cluster) {
    // Preserve catalogue order via _idx — first appearance of each (cluster, group) wins.
    const seen = new Map();
    for (const m of state.metrics) {
      if (m.cluster !== cluster) continue;
      if (!seen.has(m.group)) seen.set(m.group, m._idx);
    }
    return [...seen.entries()].sort((a, b) => a[1] - b[1]).map(e => e[0]);
  }

  function renderFocusBanner(focus) {
    const banner = document.getElementById('matrix-focus-banner');
    const text = document.getElementById('matrix-focus-text');
    if (focus) {
      banner.style.display = '';
      text.textContent = `Focused on ${CLUSTER_LABELS[focus]} — rows are groups within this cluster.`;
    } else {
      banner.style.display = 'none';
      text.textContent = '';
    }
  }

  function attachCellHandlers(cell, cluster, tier, group) {
    cell.dataset.cluster = cluster;
    cell.dataset.tier = String(tier);
    if (group !== undefined) cell.dataset.group = group;
    cell.addEventListener('dragover', e => {
      e.preventDefault();
      e.dataTransfer.dropEffect = 'move';
      cell.classList.add('drag-over');
    });
    cell.addEventListener('dragleave', () => cell.classList.remove('drag-over'));
    cell.addEventListener('drop', e => {
      e.preventDefault();
      cell.classList.remove('drag-over');
      const refId = e.dataTransfer.getData('text/plain');
      if (refId) handleDrop(refId, cell);
    });
  }

  function fillCell(cell, metrics) {
    if (metrics.length === 0) {
      const empty = document.createElement('span');
      empty.className = 'matrix-cell-empty';
      empty.textContent = '—';
      cell.appendChild(empty);
    } else {
      for (const m of metrics) cell.appendChild(buildCard(m));
    }
  }

  function renderMatrix(filtered) {
    const grid = document.getElementById('matrix-grid');
    grid.innerHTML = '';
    const focus = focusedCluster();
    renderFocusBanner(focus);

    // Decide row set: clusters by default, groups when a cluster is focused.
    // The column axis (tier) is always the same shape: three tiers.
    const rows = focus
      ? groupsInCluster(focus).map(g => ({ label: g, cluster: focus, group: g }))
      : CLUSTER_ORDER.map(c => ({ label: CLUSTER_LABELS[c], cluster: c, group: undefined }));

    // Header row: corner + Tier 1 / Tier 2 / Tier 3
    const corner = document.createElement('div');
    corner.className = 'matrix-corner';
    corner.innerHTML = focus ? 'group ↓<br>tier →' : 'cluster ↓<br>tier →';
    grid.appendChild(corner);
    for (const tier of [1, 2, 3]) {
      const h = document.createElement('div');
      h.className = 'matrix-tier-header';
      h.textContent = TIER_LABELS[tier];
      grid.appendChild(h);
    }

    // Body rows: row-label + 3 cells (one per tier)
    for (const row of rows) {
      const rh = document.createElement('div');
      rh.className = 'matrix-row-header';
      rh.textContent = row.label;
      grid.appendChild(rh);

      for (const tier of [1, 2, 3]) {
        const cell = document.createElement('div');
        cell.className = 'matrix-cell';
        attachCellHandlers(cell, row.cluster, tier, row.group);

        const inCell = filtered
          .filter(m => {
            if (m.cluster !== row.cluster) return false;
            if (effectiveTier(m) !== tier) return false;
            if (row.group !== undefined && m.group !== row.group) return false;
            return true;
          })
          .sort((a, b) => (a._idx ?? 0) - (b._idx ?? 0));
        fillCell(cell, inCell);
        grid.appendChild(cell);
      }
    }
  }

  function buildCard(m) {
    const card = document.createElement('div');
    card.className = 'matrix-card tier-' + effectiveTier(m);
    if (state.moves[m.ref_id]) card.classList.add('moved');
    card.draggable = true;
    card.dataset.refid = m.ref_id;
    const dims = m.dimensions || {};
    card.title = `${m.ref_id} — ${m.name}\n${m.cluster_name} / ${m.group}\n` +
                 `Cadence: ${dims['Measurement Cadence'] || ''}\n` +
                 `Actor: ${dims['Responsible Actors'] || ''}\n` +
                 `Drag between tier rows to re-tier (local what-if only)`;

    const refSpan = document.createElement('span');
    refSpan.className = 'card-ref';
    const link = document.createElement('a');
    link.href = metricLink(m);
    link.textContent = m.ref_id;
    link.draggable = false;
    link.addEventListener('click', e => e.stopPropagation());
    refSpan.appendChild(link);
    card.appendChild(refSpan);

    const nameSpan = document.createElement('span');
    nameSpan.className = 'card-name';
    nameSpan.textContent = m.name;
    card.appendChild(nameSpan);

    card.addEventListener('dragstart', e => {
      card.classList.add('dragging');
      e.dataTransfer.setData('text/plain', m.ref_id);
      e.dataTransfer.effectAllowed = 'move';
    });
    card.addEventListener('dragend', () => card.classList.remove('dragging'));
    return card;
  }

  function handleDrop(refId, cell) {
    const m = state.metrics.find(x => x.ref_id === refId);
    if (!m) return;
    const targetTier = parseInt(cell.dataset.tier, 10);
    const targetCluster = cell.dataset.cluster;
    if (targetCluster !== m.cluster) {
      // Don't allow moving between clusters — clusters are structural.
      // Visually shake or just no-op silently. No-op for now.
      return;
    }
    if (targetTier === m.tier) {
      delete state.moves[refId]; // returning to original
    } else {
      state.moves[refId] = { from: m.tier, to: targetTier };
    }
    renderAll();
  }

  function renderMoves() {
    const panel = document.getElementById('moves-panel');
    const list = document.getElementById('moves-list');
    const moves = Object.entries(state.moves);
    if (moves.length === 0) {
      panel.classList.add('empty');
      list.innerHTML = '';
      return;
    }
    panel.classList.remove('empty');
    list.innerHTML = '';
    // Sort moves by ref_id for stable display
    moves.sort((a, b) => a[0].localeCompare(b[0]));
    for (const [refId, mv] of moves) {
      const li = document.createElement('li');
      li.innerHTML = `<span>${escapeHtml(refId)}: ${TIER_LABELS[mv.from]} → ${TIER_LABELS[mv.to]}</span>`;
      const btn = document.createElement('button');
      btn.className = 'move-revert';
      btn.type = 'button';
      btn.textContent = 'revert';
      btn.title = 'Move ' + refId + ' back to ' + TIER_LABELS[mv.from];
      btn.addEventListener('click', () => {
        delete state.moves[refId];
        renderAll();
      });
      li.appendChild(btn);
      list.appendChild(li);
    }
  }

  function renderMatrixSummary(filtered) {
    const sum = document.getElementById('matrix-summary');
    const moves = Object.keys(state.moves).length;
    const t1 = filtered.filter(m => effectiveTier(m) === 1).length;
    const t2 = filtered.filter(m => effectiveTier(m) === 2).length;
    const t3 = filtered.filter(m => effectiveTier(m) === 3).length;
    const movesText = moves ? ` · ${moves} re-tiered` : '';
    sum.textContent = `${filtered.length} metrics shown — 🟢 ${t1} · 🟡 ${t2} · 🔵 ${t3}${movesText}`;
  }

  // ---------- Table render (existing v0.1 explorer) ----------
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
    const slug = m.group_file.replace(/\.md$/, '').split('/').pop();
    return '../groups/' + slug + '/#' + refIdToAnchor(m.ref_id);
  }

  function renderTable(filtered) {
    const sortCol = COLUMNS.find(c => c.key === state.sort.col) || COLUMNS[0];
    const sorted = filtered.slice().sort((a, b) => {
      let cmp;
      if (sortCol.key === 'tier_label') {
        cmp = effectiveTier(a) - effectiveTier(b);
      } else if (sortCol.key === 'ref_id') {
        cmp = (a._idx ?? 0) - (b._idx ?? 0);
      } else if (sortCol.key === 'cluster') {
        cmp = (CLUSTER_RANK[a.cluster] ?? 99) - (CLUSTER_RANK[b.cluster] ?? 99);
      } else {
        cmp = String(colValue(a, sortCol)).toLowerCase().localeCompare(String(colValue(b, sortCol)).toLowerCase());
      }
      return state.sort.dir === 'asc' ? cmp : -cmp;
    });

    // Summary
    const summary = document.getElementById('ex-summary');
    const total = state.metrics.length;
    const t1 = sorted.filter(m => effectiveTier(m) === 1).length;
    const t2 = sorted.filter(m => effectiveTier(m) === 2).length;
    const t3 = sorted.filter(m => effectiveTier(m) === 3).length;
    summary.textContent = `Showing ${sorted.length} of ${total} metrics — 🟢 ${t1} · 🟡 ${t2} · 🔵 ${t3}`;

    const wrap = document.getElementById('ex-table-wrap');
    if (sorted.length === 0) {
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
    for (const m of sorted) {
      const link = metricLink(m);
      const tier = effectiveTier(m);
      const tierIcon = { 1: '🟢', 2: '🟡', 3: '🔵' }[tier] || m.tier_icon;
      const tierLabel = TIER_LABEL_FOR_TIER[tier] || m.tier_label;
      const movedMark = state.moves[m.ref_id] ? ' *' : '';
      html += '<tr>';
      html += `<td class="refid"><a href="${link}">${escapeHtml(m.ref_id)}</a>${movedMark}</td>`;
      html += `<td>${escapeHtml(m.name)}</td>`;
      html += `<td><span class="tier-icon">${tierIcon}</span> ${escapeHtml(tierLabel)}</td>`;
      html += `<td>${escapeHtml(m.cluster_name || m.cluster)}</td>`;
      html += `<td>${escapeHtml(m.group)}</td>`;
      html += `<td>${escapeHtml(m.dimensions['Measurement Cadence'] || '')}</td>`;
      html += `<td>${escapeHtml(m.dimensions['Responsible Actors'] || '')}</td>`;
      html += `<td>${escapeHtml(m.applicability || '')}</td>`;
      html += '</tr>';
    }
    html += '</tbody></table>';
    wrap.innerHTML = html;

    for (const th of wrap.querySelectorAll('th[data-col]')) {
      th.addEventListener('click', () => {
        const col = th.dataset.col;
        if (state.sort.col === col) state.sort.dir = state.sort.dir === 'asc' ? 'desc' : 'asc';
        else { state.sort.col = col; state.sort.dir = 'asc'; }
        writeHash();
        renderAll();
      });
    }
  }

  function escapeHtml(s) {
    return String(s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  }

  // ---------- Top-level render ----------
  function renderAll() {
    const filtered = state.metrics.filter(metricMatches);
    renderMatrix(filtered);
    renderMatrixSummary(filtered);
    renderMoves();
    renderTable(filtered);
  }

  function resetFilters() {
    state.filters = {};
    state.sort = { col: 'ref_id', dir: 'asc' };
    writeHash();
    syncControls();
    renderAll();
  }

  function resetMoves() {
    state.moves = {};
    renderAll();
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
      document.getElementById('matrix-summary').textContent = 'Error loading.';
      console.error('Failed to load metrics:', err);
      return;
    }

    // Wire up search inputs (sidebar + matrix-strip)
    for (const id of ['ex-search', 'mx-search']) {
      const search = document.getElementById(id);
      if (!search) continue;
      if (state.filters.q) search.value = state.filters.q;
      search.addEventListener('input', () => {
        state.filters.q = search.value;
        writeHash();
        syncControls();
        renderAll();
      });
    }
    for (const key of Object.keys(FIELDS)) populateSelect(key);
    document.getElementById('ex-reset').addEventListener('click', resetFilters);
    document.getElementById('matrix-reset-moves').addEventListener('click', resetMoves);
    document.getElementById('matrix-focus-clear').addEventListener('click', () => {
      setFilter('cluster', '');
    });

    window.addEventListener('hashchange', () => {
      const h = readHash();
      state.filters = {};
      if (h.q) state.filters.q = h.q;
      for (const k of Object.keys(FIELDS)) if (h[k]) state.filters[k] = h[k];
      syncControls();
      renderAll();
    });

    renderAll();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
</script>
