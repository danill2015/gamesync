<script lang="ts">
  let { triggerDelete } = $props<{ triggerDelete: (id: string, name: string) => void }>();

  let builds = $state([
    { id: 'b-1', version: 'v0.9.2-alpha', channel: 'Public Alpha', status: 'Active Playtest', size: '1.42 GB', date: '6 годин тому', downloads: 1482, players: 89 },
    { id: 'b-2', version: 'v0.9.1-alpha', channel: 'Public Alpha', status: 'Archived', size: '1.38 GB', date: '12 днів тому', downloads: 3120, players: 0 },
    { id: 'b-3', version: 'v0.9.3-nightly', channel: 'Internal Staging', status: 'Processing', size: '1.47 GB', date: '41 хвилину тому', downloads: 0, players: 0 }
  ]);
</script>

<div class="flex-1 overflow-y-auto p-8 flex gap-8">
  <div class="flex-1 space-y-6">
    <div>
      <h1 class="text-2xl font-bold text-white tracking-tight">Builds & Release Channels</h1>
      <p class="text-xs text-slate-400">Керування ігровими клієнтами, альфа/бета каналами та дистрибуцією плейтестів</p>
    </div>

    <!-- Дропзона завантаження нового білду -->
    <div class="p-6 rounded-2xl border-2 border-dashed border-[#1c263c] bg-[#0e1424]/50 flex items-center justify-between">
      <div class="space-y-1">
        <div class="text-sm font-semibold text-white">Завантажити новий архів збірки гри</div>
        <div class="text-xs text-slate-400">Підтримуються формати .zip, .tar.gz, .exe (до 5 ГБ для тарифу Indie Pro)</div>
      </div>
      <button class="px-4 py-2 rounded-lg bg-[#7c3aed] hover:bg-[#6d28d9] text-white text-xs font-bold transition-all shadow-md">
        + Upload New Build
      </button>
    </div>

    <!-- Список релізів -->
    <div class="space-y-3">
      {#each builds as build}
        <div class="bg-[#0e1424] rounded-2xl border border-[#1c263c] p-5 flex items-center justify-between shadow-lg">
          <div class="space-y-2">
            <div class="flex items-center gap-3">
              <span class="text-base font-bold text-white font-mono">{build.version}</span>
              <span class="px-2 py-0.5 rounded text-[10px] font-mono font-bold {build.status === 'Active Playtest' ? 'bg-emerald-950/60 text-emerald-400 border border-emerald-800/40' : 'bg-slate-800 text-slate-400'}">
                {build.status}
              </span>
              <span class="text-xs text-slate-400 bg-[#141d33] px-2 py-0.5 rounded">{build.channel}</span>
            </div>
            <div class="flex gap-4 text-xs text-slate-400">
              <span>{build.size}</span> • <span>{build.date}</span> • <span>{build.downloads} завантажень</span>
            </div>
          </div>

          <div class="flex items-center gap-2">
            <button class="px-3.5 py-1.5 rounded-lg bg-[#7c3aed] text-white text-xs font-semibold hover:bg-[#6d28d9] transition-all">
              Download Build (.zip)
            </button>
            <!-- Виклик модального вікна підтвердження видалення (Вимога Лаб №4) -->
            <button onclick={() => triggerDelete(build.id, build.version)} title="Видалити білд" class="p-1.5 rounded-lg text-slate-400 hover:text-red-400 hover:bg-[#1a233a] transition-colors">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path></svg>
            </button>
          </div>
        </div>
      {/each}
    </div>
  </div>

  <div class="w-80 space-y-6 shrink-0">
    <div class="bg-[#0e1424] rounded-2xl border border-[#1c263c] p-5 space-y-3">
      <h3 class="text-xs font-bold uppercase tracking-wider text-slate-400">Storage Quota</h3>
      <div class="text-2xl font-bold font-mono text-white">8.4 GB <span class="text-xs font-normal text-slate-400">/ 25 GB</span></div>
      <div class="w-full bg-[#070b14] h-2 rounded-full overflow-hidden">
        <div class="bg-gradient-to-r from-purple-500 to-indigo-500 h-full w-[34%]"></div>
      </div>
      <div class="text-[11px] text-emerald-400">16.6 GB вільно на тарифі Indie Pro</div>
    </div>
  </div>
</div>