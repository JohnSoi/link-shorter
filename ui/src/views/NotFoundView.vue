<script setup lang="ts"></script>

<template>
    <div class="NotFoundView__wrapper flex items-center justify-center w-full h-full">
        <div class="NotFoundView__content w-1/2 h-full flex items-center justify-center flex-col">
            <h2 class="text-4xl mb-16 font-bold">Упс! У мы такого не нашли...</h2>
            <div class="text-2xl w-1/2 mb-8 font-thin">
                Мы любим мир, где видят вещи, которых на самом деле нет. Но этой страницы
                действительно нет.
            </div>
            <div>
                <a href="/" class="text-blue-300 hover:text-blue-700">Вернуться на главную</a>
            </div>
        </div>
        <div class="NotFoundView__image w-1/2 h-full">
            <img class="w-full h-full" src="/404.jpg" alt="Not found cat image" />
        </div>
    </div>
</template>

<style scoped></style>
