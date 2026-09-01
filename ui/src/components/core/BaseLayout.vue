<script setup lang="ts">
import BaseMenu from "@/components/core/BaseMenu.vue";
</script>

<template>
    <div class="BaseLayout__wrapper w-full h-full overflow-hidden flex flex-col">
        <BaseMenu/>
        <main><RouterView /></main>
    </div>
</template>

<style scoped></style>
