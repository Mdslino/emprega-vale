<template lang="pug">
    b-navbar
        template(slot="brand")
            b-navbar-item(tag="router-link", :to="{ path: '/' }")
                img(src="https://raw.githubusercontent.com/buefy/buefy/dev/static/img/buefy-logo.png",
                    alt="Lightweight UI components for Vue.js based on Bulma")
        template(slot="start")
            b-navbar-item(href="#") Inicio
            b-navbar-item(href="#") Documentação
            b-navbar-dropdown(label="Informação" )
                b-navbar-item(href="#") Sobre
                b-navbar-item(href="#") Contato
        template(slot="end")
            b-navbar-item(tag="end")
                b-navbar-item(tag="end")
                    .buttons
                        a.button.is-primary
                            strong Registrar
                        a.button.is-light Entrar
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";

@Component
export default class Navigation extends Vue {}
</script>
