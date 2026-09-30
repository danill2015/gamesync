<script lang="ts">
  let { isOpen = false, itemName = '', onConfirm, onCancel } = $props<{
    isOpen: boolean;
    itemName: string;
    onConfirm: () => void;
    onCancel: () => void;
  }>();
</script>

{#if isOpen}
  <div class="fixed inset-0 bg-black/70 backdrop-blur-sm flex items-center justify-center z-50 p-4">
    <div class="bg-[#0e1424] border border-[#2d3748] rounded-2xl max-w-md w-full p-6 space-y-4 shadow-2xl">
      <div class="w-10 h-10 rounded-full bg-red-500/10 border border-red-500/20 text-red-400 flex items-center justify-center font-bold">⚠️</div>
      <div>
        <h3 class="text-lg font-bold text-white">Видалити релізний білд?</h3>
        <p class="text-xs text-slate-400 mt-1 leading-relaxed">
          Ви впевнені, що хочете видалити <strong>{itemName}</strong>? Цю дію неможливо скасувати, а тестувальники втратять доступ до посилання на завантаження.
        </p>
      </div>
      <div class="flex justify-end gap-3 pt-2">
        <button onclick={onCancel} class="px-4 py-2 rounded-lg text-xs font-semibold text-slate-300 hover:bg-[#1a233a] transition-colors">Скасувати</button>
        <button onclick={onConfirm} class="px-4 py-2 rounded-lg text-xs font-semibold bg-red-600 hover:bg-red-700 text-white transition-colors shadow-lg">Підтвердити видалення</button>
      </div>
    </div>
  </div>
{/if}