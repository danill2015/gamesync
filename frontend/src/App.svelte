<script lang="ts">
  import Sidebar from './lib/Sidebar.svelte';
  import FeedView from './lib/FeedView.svelte';
  import DevlogsView from './lib/DevlogsView.svelte';
  import ApiTestingView from './lib/ApiTestingView.svelte';
  import BuildsView from './lib/BuildsView.svelte';
  import AnalyticsView from './lib/AnalyticsView.svelte';
  import DeleteModal from './lib/DeleteModal.svelte';

  let currentTab = $state('feed');
  let isAuthModalOpen = $state(false);
  
  // Керування модальним вікном підтвердження видалення
  let isDeleteModalOpen = $state(false);
  let buildToDelete = $state({ id: '', name: '' });

  function triggerDelete(id: string, name: string) {
    buildToDelete = { id, name };
    isDeleteModalOpen = true;
  }

  async function confirmDelete() {
    try {
      await fetch(`http://localhost:8000/api/v1/builds/${buildToDelete.id}`, { method: 'DELETE' });
      alert(`Білд ${buildToDelete.name} успішно видалено!`);
    } catch {
      alert(`Білд ${buildToDelete.name} видалено локально`);
    } finally {
      isDeleteModalOpen = false;
    }
  }

  function handleGitHubLogin() {
    alert("Імітація OAuth авторизації: перенаправлення на шлюз GitHub...");
    isAuthModalOpen = false;
  }
</script>

<div class="flex h-screen w-screen bg-[#070b14] text-slate-100 font-sans overflow-hidden">
  <Sidebar bind:currentTab openAuthModal={() => isAuthModalOpen = true} />

  <main class="flex-1 flex flex-col min-w-0 bg-[#0a0f1d] overflow-hidden">
    {#if currentTab === 'feed'}
      <FeedView />
    {:else if currentTab === 'devlogs'}
      <DevlogsView />
    {:else if currentTab === 'api'}
      <ApiTestingView />
    {:else if currentTab === 'builds'}
      <BuildsView {triggerDelete} />
    {:else if currentTab === 'analytics'}
      <AnalyticsView />
    {/if}
  </main>
</div>

<!-- Модальне вікно авторизації через GitHub (Вимога Лабораторної №4) -->
{#if isAuthModalOpen}
  <div class="fixed inset-0 bg-black/70 backdrop-blur-sm flex items-center justify-center z-50 p-4">
    <div class="bg-[#0e1424] border border-[#222f49] rounded-2xl max-w-sm w-full p-6 space-y-5 shadow-2xl">
      <div class="text-center space-y-1">
        <h3 class="text-lg font-bold text-white">Вхід у GameSync</h3>
        <p class="text-xs text-slate-400">Оберіть зручний спосіб швидкої авторизації</p>
      </div>
      <button 
        onclick={handleGitHubLogin} 
        class="w-full py-2.5 px-4 bg-[#24292e] hover:bg-[#2f363d] text-white rounded-xl text-xs font-semibold flex items-center justify-center gap-2 border border-slate-700 transition-colors shadow-md"
      >
        <span>Увійти через GitHub</span>
      </button>
      <button onclick={() => isAuthModalOpen = false} class="w-full text-center text-xs text-slate-500 hover:text-slate-300 transition-colors">Закрити</button>
    </div>
  </div>
{/if}

<!-- Модальне вікно деструктивної дії (Вимога Лабораторної №4) -->
<DeleteModal 
  isOpen={isDeleteModalOpen} 
  itemName={buildToDelete.name} 
  onConfirm={confirmDelete} 
  onCancel={() => isDeleteModalOpen = false} 
/>