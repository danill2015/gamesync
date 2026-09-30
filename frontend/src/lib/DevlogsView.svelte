<script lang="ts">
  // Список девлогів згідно з макетом Devlogs & Updates
  let devlogEntries = $state([
    {
      id: "entry-1",
      number: "DEVLOG #047",
      title: "Spatial Audio System & Enemy AI Refactor",
      status: "Published",
      version: "v0.9.2-alpha Linked",
      project: "VOID PROTOCOL",
      date: "Sep 15, 2026",
      readTime: "4 min read",
      views: "1,482",
      likes: "127",
      comments: "34",
      image: "https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=400&q=80"
    },
    {
      id: "entry-2",
      number: "DEVLOG #046",
      title: "Implementing Inventory Physics and Item Inspection",
      status: "Published",
      version: "v0.9.1-alpha Linked",
      project: "VOID PROTOCOL",
      date: "Aug 28, 2026",
      readTime: "6 min read",
      views: "3,210",
      likes: "215",
      comments: "58",
      image: "https://images.unsplash.com/photo-1511512578047-dfb367046420?w=400&q=80"
    },
    {
      id: "entry-3",
      number: "DEVLOG #045",
      title: "Multiplayer Networking & Custom Lobby Architecture",
      status: "Archived",
      version: "v0.8.4 Linked",
      project: "VOID PROTOCOL",
      date: "Aug 12, 2026",
      readTime: "8 min read",
      views: "2,804",
      likes: "184",
      comments: "42",
      image: "https://images.unsplash.com/photo-1542751371-adc38448a05e?w=400&q=80"
    }
  ]);

  let activeTab = $state("All Entries (12)");
  let tabs = ["All Entries (12)", "Published (9)", "Drafts (3)", "Scheduled"];
</script>

<div class="flex-1 overflow-y-auto p-8 flex gap-8">
  <!-- Центральна панель керування публікаціями -->
  <div class="flex-1 space-y-6">
    <!-- Заголовок та кнопка створення -->
    <div class="flex items-center justify-between">
      <div>
        <h1 class="text-2xl font-bold text-white tracking-tight">Devlogs & Updates</h1>
        <p class="text-xs text-slate-400">Створюйте хроніки розробки, публікуйте апдейти у стрічку та прив'язуйте білди</p>
      </div>
      <button class="px-4 py-2 rounded-lg bg-[#7c3aed] hover:bg-[#6d28d9] text-white text-xs font-bold transition-all shadow-md flex items-center gap-1.5">
        <span>+ New Devlog Entry</span>
      </button>
    </div>

    <!-- Підвкладки фільтрації -->
    <div class="flex gap-4 border-b border-[#1c263c] text-xs pb-2">
      {#each tabs as tab}
        <button 
          onclick={() => activeTab = tab}
          class="transition-colors {activeTab === tab ? 'text-purple-400 font-bold border-b-2 border-purple-500 pb-2 -mb-2.5' : 'text-slate-400 hover:text-slate-200'}"
        >
          {tab}
        </button>
      {/each}
    </div>

    <!-- Банер активної чернетки -->
    <div class="p-4 rounded-xl bg-[#141b2d] border border-[#232e48] flex items-center justify-between shadow-lg">
      <div class="flex items-center gap-3">
        <div class="w-8 h-8 rounded-lg bg-purple-900/40 border border-purple-500/30 flex items-center justify-center text-sm">📝</div>
        <div>
          <div class="text-xs font-bold text-white">Draft in progress: Devlog #048: Procedural Level Generation</div>
          <div class="text-[10px] text-slate-400">Збережено 15 хв тому • 512 слів</div>
        </div>
      </div>
      <div class="flex items-center gap-2">
        <button class="px-3 py-1.5 rounded-lg bg-[#7c3aed] hover:bg-[#6d28d9] text-white text-xs font-semibold">Continue Editing</button>
        <button class="px-3 py-1.5 rounded-lg text-slate-400 hover:text-white text-xs">Discard</button>
      </div>
    </div>

    <!-- Список записів -->
    <div class="space-y-3">
      {#each devlogEntries as entry}
        <div class="bg-[#0e1424] rounded-2xl border border-[#1c263c] p-4 flex gap-4 items-center shadow-lg hover:border-slate-700 transition-colors">
          <div class="w-24 h-20 rounded-xl overflow-hidden shrink-0 border border-[#202d49]">
            <img src={entry.image} alt="Thumbnail" class="w-full h-full object-cover" />
          </div>

          <div class="flex-1 space-y-1.5">
            <div class="flex items-center gap-2">
              <span class="px-2 py-0.5 rounded text-[10px] font-mono font-bold {entry.status === 'Published' ? 'bg-emerald-950/60 text-emerald-400 border border-emerald-800/40' : 'bg-slate-800 text-slate-400'}">
                {entry.status}
              </span>
              <span class="px-2 py-0.5 rounded text-[10px] font-mono bg-[#7c3aed]/20 text-[#a78bfa] border border-[#7c3aed]/40">{entry.version}</span>
              <span class="text-[10px] font-mono text-slate-500 uppercase">{entry.project}</span>
            </div>

            <h3 class="text-sm font-bold text-white">{entry.title}</h3>

            <div class="text-[11px] text-slate-400">
              Published {entry.date} • {entry.readTime} • {entry.views} views • {entry.likes} likes • {entry.comments} comments
            </div>
          </div>

          <div class="flex items-center gap-2 shrink-0">
            <button class="px-3 py-1.5 rounded-lg bg-[#1a233a] hover:bg-[#232e48] text-xs font-medium text-slate-200">Edit Post</button>
            <button class="px-3 py-1.5 rounded-lg bg-[#1a233a] hover:bg-[#232e48] text-xs font-medium text-slate-200">View</button>
          </div>
        </div>
      {/each}
    </div>
  </div>

  <!-- Правий сайдбар віджетів (Building in Public / SEO) -->
  <div class="w-80 space-y-6 shrink-0">
    <!-- Віджет Building in Public -->
    <div class="bg-[#0e1424] rounded-2xl border border-[#1c263c] p-5 space-y-3 shadow-lg">
      <h3 class="text-xs font-bold uppercase tracking-wider text-slate-400">Building in Public Score</h3>
      <div class="flex items-center gap-4">
        <div class="w-14 h-14 rounded-full border-4 border-purple-500 flex items-center justify-center font-bold text-white text-base">
          85%
        </div>
        <div class="text-xs text-slate-400 space-y-1">
          <div class="text-white font-semibold">Відмінна активність!</div>
          <div class="text-purple-400 text-[10px]">+15% залучення за відеодевлоги</div>
        </div>
      </div>
    </div>

    <!-- Віджет прив'язки білду -->
    <div class="bg-[#0e1424] rounded-2xl border border-[#1c263c] p-5 space-y-3 shadow-lg">
      <h3 class="text-xs font-bold uppercase tracking-wider text-slate-400">Linked Build Status</h3>
      <div class="p-3 bg-[#070b14] rounded-xl border border-[#1c263c] space-y-2">
        <div class="flex justify-between items-center text-xs">
          <span class="font-bold text-white font-mono">Build v0.9.2-alpha</span>
          <span class="text-emerald-400 text-[10px]">● Active</span>
        </div>
        <div class="text-[10px] text-slate-400">1.42 GB • Windows/Linux</div>
      </div>
    </div>

    <!-- Віджет соціальних мереж -->
    <div class="bg-[#0e1424] rounded-2xl border border-[#1c263c] p-5 space-y-3 shadow-lg text-xs">
      <h3 class="text-xs font-bold uppercase tracking-wider text-slate-400">SEO & Social Sharing</h3>
      <div class="space-y-2">
        <div class="flex justify-between items-center text-slate-300">
          <span>Auto-post to Reddit (r/gamedev)</span>
          <span class="text-purple-400 font-bold">ON</span>
        </div>
        <div class="flex justify-between items-center text-slate-300">
          <span>Auto-post to X (Twitter)</span>
          <span class="text-purple-400 font-bold">ON</span>
        </div>
      </div>
    </div>
  </div>
</div>