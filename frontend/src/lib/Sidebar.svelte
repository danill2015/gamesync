<script lang="ts">
  let { currentTab = $bindable(), openAuthModal } = $props<{
    currentTab: string;
    openAuthModal: () => void;
  }>();

  const menuItems = [
    { id: 'feed', label: 'Feed', icon: 'M4 6h16M4 12h16M4 18h7' },
    { id: 'devlogs', label: 'Devlogs', badge: '3', icon: 'M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z' },
    { id: 'builds', label: 'Builds', icon: 'M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4' },
    { id: 'api', label: 'API Testing', icon: 'M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4' },
    { id: 'analytics', label: 'Analytics', icon: 'M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z' }
  ];
</script>

<aside class="w-60 bg-[#070b14] border-r border-[#1a2333] flex flex-col justify-between shrink-0 h-screen select-none font-sans">
  <div>
    <!-- Логотип платформи GameSync з іконкою блискавки -->
    <div class="h-16 flex items-center px-6 gap-2 border-b border-[#1a2333]">
      <div class="w-6 h-6 rounded-md bg-gradient-to-tr from-purple-600 to-indigo-500 flex items-center justify-center text-white text-xs font-bold shadow-sm">⚡</div>
      <span class="text-white font-bold text-lg tracking-wide lowercase">gamesync</span>
    </div>

    <!-- Список головної навігації -->
    <nav class="p-3 space-y-1">
      <div class="px-3 py-2 text-[10px] font-bold uppercase tracking-wider text-slate-500">Navigation</div>
      {#each menuItems as item}
        <button
          onclick={() => currentTab = item.id}
          class="w-full flex items-center justify-between px-3 py-2.5 rounded-lg text-sm font-medium transition-colors {currentTab === item.id ? 'bg-[#7c3aed]/15 text-[#a78bfa] border border-[#7c3aed]/40' : 'text-slate-400 hover:text-slate-200 hover:bg-[#111827]'}"
        >
          <div class="flex items-center gap-3">
            <svg class="w-4 h-4 stroke-current fill-none stroke-2" viewBox="0 0 24 24"><path d={item.icon}></path></svg>
            <span>{item.label}</span>
          </div>
          {#if item.badge}
            <span class="px-1.5 py-0.5 text-xs rounded-full bg-purple-900/60 text-purple-300 font-mono">{item.badge}</span>
          {/if}
        </button>
      {/each}
    </nav>
  </div>

  <!-- Профіль поточного користувача -->
  <div class="p-3 border-t border-[#1a2333]">
    <div class="p-2.5 rounded-xl bg-[#0f172a] border border-[#1e293b] flex items-center justify-between">
      <div class="flex items-center gap-2.5">
        <div class="w-8 h-8 rounded-full bg-slate-700 overflow-hidden ring-1 ring-purple-500/50">
          <img src="https://api.dicebear.com/7.x/bottts/svg?seed=Mira" alt="Аватар" />
        </div>
        <div>
          <div class="text-xs font-semibold text-white">Mira Solvang</div>
          <div class="text-[10px] text-purple-400 font-medium">Indie Pro Plan</div>
        </div>
      </div>
      <button onclick={openAuthModal} title="Авторизація / Зміна профілю" class="text-slate-400 hover:text-white transition-colors">
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"></path></svg>
      </button>
    </div>
  </div>
</aside>
