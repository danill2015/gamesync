<script lang="ts">
  let devlogs = $state([
    {
      id: "devlog-047",
      title: "Spatial Audio System & Enemy AI Refactor",
      project: "VOID PROTOCOL",
      version: "v0.9.2-alpha",
      author: "Mira Solvang",
      text: "Spent the last two weeks completely overhauling how enemies perceive the player. The old raycasting approach was causing jittery behavior in tight corridors — now using a layered field-of-view model with dynamic cone adjustment based on alert state.",
      tags: ["gameplay", "audio", "AI", "optimization", "stealth"],
      likes: 127,
      comments: 34,
      image: "https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=1200&q=80"
    }
  ]);

  let activeFilter = $state('All');
</script>

<div class="flex-1 overflow-y-auto p-8 flex gap-8">
  <div class="flex-1 max-w-4xl space-y-6">
    <div class="flex items-center justify-between">
      <div>
        <h1 class="text-2xl font-bold text-white tracking-tight">Developer Feed</h1>
        <p class="text-xs text-slate-400">Останні девлоги від проєктів, за якими ви стежите</p>
      </div>
      <div class="flex bg-[#0f172a] p-1 rounded-lg border border-[#1e293b] text-xs">
        {#each ['All', 'Following', 'Trending'] as filter}
          <button 
            onclick={() => activeFilter = filter}
            class="px-3 py-1 rounded-md transition-colors {activeFilter === filter ? 'bg-[#7c3aed] text-white font-medium' : 'text-slate-400 hover:text-slate-200'}"
          >{filter}</button>
        {/each}
      </div>
    </div>

    {#each devlogs as log}
      <article class="bg-[#0e1424] rounded-2xl border border-[#1c263c] overflow-hidden p-6 space-y-4 shadow-xl">
        <div class="flex items-center justify-between">
          <div class="flex items-center gap-2">
            <span class="px-2 py-0.5 rounded text-[11px] font-mono font-bold bg-[#7c3aed]/20 text-[#a78bfa] border border-[#7c3aed]/40">DEVLOG #047</span>
            <span class="px-2 py-0.5 rounded text-[11px] font-mono font-bold bg-emerald-950/60 text-emerald-400 border border-emerald-800/40">{log.version}</span>
          </div>
          <span class="text-xs font-mono tracking-wider text-slate-400 uppercase bg-[#141d33] px-2.5 py-1 rounded-md">PROJECT {log.project}</span>
        </div>

        <h2 class="text-xl font-bold text-white">{log.title}</h2>

        <div class="flex items-center gap-3 text-xs text-slate-400">
          <span>{log.author}</span> • <span>Sep 15, 2026</span> • <span>4 min read</span>
        </div>

        <div class="flex flex-wrap gap-1.5">
          {#each log.tags as tag}
            <span class="px-2 py-0.5 rounded-full text-[11px] bg-[#1a233a] text-slate-300 font-medium">#{tag}</span>
          {/each}
        </div>

        <p class="text-sm text-slate-300 leading-relaxed font-sans">{log.text}</p>

        <div class="rounded-xl overflow-hidden border border-[#202d49] max-h-96">
          <img src={log.image} alt="Прев'ю" class="w-full h-full object-cover" />
        </div>

        <div class="flex items-center justify-between pt-2 border-t border-[#1a233a]">
          <div class="flex gap-4 text-xs text-slate-400 font-medium">
            <span class="flex items-center gap-1.5 text-slate-300">👍 {log.likes}</span>
            <span class="flex items-center gap-1.5 text-slate-300">💬 {log.comments}</span>
          </div>
          <button class="px-4 py-1.5 rounded-lg bg-[#7c3aed] hover:bg-[#6d28d9] text-white text-xs font-semibold flex items-center gap-2 transition-all shadow-md">
            <span>Download Build ({log.version})</span>
          </button>
        </div>
      </article>
    {/each}
  </div>

  <div class="w-80 space-y-6 shrink-0">
    <div class="bg-[#0e1424] rounded-2xl border border-[#1c263c] p-5 space-y-4">
      <h3 class="text-xs font-bold uppercase tracking-wider text-slate-400">Build Metrics</h3>
      <div class="space-y-3">
        <div class="flex justify-between items-center p-3 rounded-lg bg-[#070b14]">
          <span class="text-xs text-slate-400">Total Downloads</span>
          <span class="text-sm font-bold text-white font-mono">1,482 <span class="text-[10px] text-emerald-400 font-normal">+12%</span></span>
        </div>
        <div class="flex justify-between items-center p-3 rounded-lg bg-[#070b14]">
          <span class="text-xs text-slate-400">Active Playtesters</span>
          <span class="text-sm font-bold text-white font-mono">89</span>
        </div>
        <div class="flex justify-between items-center p-3 rounded-lg bg-[#070b14]">
          <span class="text-xs text-slate-400">Bug Reports</span>
          <span class="text-sm font-bold text-white font-mono">34</span>
        </div>
        <div class="flex justify-between items-center p-3 rounded-lg bg-[#070b14]">
          <span class="text-xs text-slate-400">Avg Session</span>
          <span class="text-sm font-bold text-white font-mono">24m</span>
        </div>
      </div>
    </div>
  </div>
</div>