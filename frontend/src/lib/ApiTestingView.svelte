<script lang="ts">
  let endpoint = $state('/api/v1/lobbies');
  let responseData = $state<any>(null);
  let isLoading = $state(false);
  let latency = $state<number | null>(null);

  async function sendRequest() {
    isLoading = true;
    const start = performance.now();
    try {
      const res = await fetch(`http://localhost:8000${endpoint}`);
      responseData = await res.json();
      latency = Math.round(performance.now() - start);
    } catch (e) {
      responseData = { error: "Не вдалося з'єднатися з FastAPI бекендом", detail: String(e) };
      latency = 0;
    } finally {
      isLoading = false;
    }
  }
</script>

<div class="flex-1 overflow-y-auto p-8 space-y-6">
  <div>
    <h1 class="text-2xl font-bold text-white tracking-tight">API Testing</h1>
    <p class="text-xs text-slate-400 font-mono">GameSync REST API • Base URL: http://localhost:8000</p>
  </div>

  <div class="flex gap-3 bg-[#0e1424] p-3 rounded-xl border border-[#1c263c]">
    <span class="px-3 py-2 rounded-lg bg-emerald-950/80 text-emerald-400 font-mono text-xs font-bold flex items-center border border-emerald-800/40">GET</span>
    <input 
      bind:value={endpoint} 
      class="flex-1 bg-transparent text-sm text-white font-mono focus:outline-none" 
      placeholder="/api/v1/..."
    />
    <button 
      onclick={sendRequest} 
      disabled={isLoading}
      class="px-5 py-2 rounded-lg bg-[#7c3aed] hover:bg-[#6d28d9] text-white text-xs font-bold flex items-center gap-2 transition-colors shadow-md"
    >
      {isLoading ? 'Надсилання...' : 'Send Request'}
    </button>
  </div>

  <div class="grid grid-cols-2 gap-6">
    <div class="bg-[#0e1424] p-5 rounded-2xl border border-[#1c263c] space-y-3 font-mono text-xs">
      <div class="text-slate-400 font-sans font-semibold">Request Headers</div>
      <div class="p-3 bg-[#070b14] rounded-lg text-slate-300 space-y-1">
        <div>Authorization: <span class="text-purple-400">Bearer gsk_live_a3f9c2d1e8b7...</span></div>
        <div>Content-Type: <span class="text-purple-400">application/json</span></div>
        <div>X-Game-ID: <span class="text-purple-400">void-protocol</span></div>
      </div>
    </div>

    <div class="bg-[#0e1424] p-5 rounded-2xl border border-[#1c263c] space-y-3">
      <div class="flex justify-between items-center text-xs">
        <span class="font-semibold text-slate-400">Response Body</span>
        {#if latency !== null}
          <span class="font-mono text-emerald-400 font-bold">200 OK • {latency}ms</span>
        {/if}
      </div>
      <pre class="p-4 bg-[#070b14] rounded-xl text-emerald-400 font-mono text-xs overflow-x-auto min-h-[160px]">
        {responseData ? JSON.stringify(responseData, null, 2) : '// Натисніть "Send Request" для виконання реального запиту'}
      </pre>
    </div>
  </div>
</div>