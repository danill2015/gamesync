<script lang="ts">
  let kpis = [
    { label: "Total Downloads", val: "1,482", badge: "+12% vs last week", positive: true },
    { label: "Active Playtesters", val: "89", badge: "Peak 142 today", positive: true },
    { label: "Average Playtime", val: "24m 18s", badge: "+3m improvement", positive: true },
    { label: "Crash-Free Rate", val: "98.4%", badge: "Stable builds", positive: true }
  ];
</script>

<div class="flex-1 overflow-y-auto p-8 space-y-6">
  <div>
    <h1 class="text-2xl font-bold text-white tracking-tight">Project Analytics & Telemetry</h1>
    <p class="text-xs text-slate-400">Метрики в реальному часі для проєкту VOID PROTOCOL • Active Build v0.9.2-alpha</p>
  </div>

  <!-- Карточки KPI -->
  <div class="grid grid-cols-4 gap-4">
    {#each kpis as kpi}
      <div class="bg-[#0e1424] p-5 rounded-2xl border border-[#1c263c] space-y-2">
        <div class="text-xs text-slate-400">{kpi.label}</div>
        <div class="text-2xl font-bold text-white font-mono">{kpi.val}</div>
        <div class="text-[11px] text-emerald-400">{kpi.badge}</div>
      </div>
    {/each}
  </div>

  <!-- График активности -->
  <div class="bg-[#0e1424] p-6 rounded-2xl border border-[#1c263c] space-y-4">
    <div class="flex justify-between items-center">
      <div class="text-sm font-bold text-white">Daily Active Testers & Build Downloads</div>
      <div class="text-xs text-slate-400 font-mono">Last 30 Days</div>
    </div>
    <div class="h-48 w-full flex items-end gap-2 pt-8">
      {#each [24, 32, 45, 38, 55, 62, 70, 65, 80, 89] as height, i}
        <div class="flex-1 flex flex-col items-center gap-2 h-full justify-end">
          <div class="w-full bg-[#7c3aed]/40 hover:bg-[#7c3aed] transition-colors rounded-t-md" style="height: {height * 1.8}px;"></div>
          <span class="text-[10px] text-slate-500 font-mono">D{i+1}</span>
        </div>
      {/each}
    </div>
  </div>
</div>