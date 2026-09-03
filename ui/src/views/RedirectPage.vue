<script setup lang="ts">
import { useRedirectPage } from "@/composables/useRedirectPage";

const { redirectByToken } = useRedirectPage();

redirectByToken();
</script>

<template>
    <div class="RedirectPage__wrapper flex items-center justify-center w-full h-full">
        <div class="flex items-center justify-center flex-col">
            Сейчас вы будете перенаправлены на страницу.
            <br />
            <div>
                Если этого не произошло
                <a
                    class="text-blue-300 hover:text-blue-700"
                    href="#"
                    @click.prevent="redirectByToken"
                >
                    повторите попытку
                </a>
                или
                <a
                    class="text-blue-300 hover:text-blue-700"
                    href="#"
                    @click.prevent="$router.push('/')"
                >
                    вернитесь на главную
                </a>
            </div>
        </div>
    </div>
</template>
