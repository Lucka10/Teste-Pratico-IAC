<script setup lang="ts">
defineProps<{
  numero: number,
  nome:string,
  email:string,
  telefone:string,
  date:string,
}>()
</script>

<template>
  <div class="container d-flex border border-3 border-dark rounded p-2">
    <h1 class="d-flex align-items-center">#{{ numero }}</h1>
    <img class="border border-dark mx-3" src="/src/assets/profilebase.jpeg" width="140" height="140" >
    <div class="container d-flex flex-column flex-grow-1 justify-content-between p-0">
        <div class="fw-bold fs-5">Nome:{{ nome }}</div>
        <div class="fw-bold fs-5">Email: {{ email }}</div>
        <div class="fw-bold fs-5">Telefone:{{ telefone }}</div>
        <div class="fw-bold fs-5">Data de nascimento:{{ date }}</div>
    </div>
    <div class="container d-flex flex-column justify-content-evenly" style="max-width: fit-content;">
        <button class="btn btn-warning bi bi-pencil px-3" > Editar</button>
        <button class="btn btn-danger bi bi-x-square px-3" > Excluir</button>
    </div>

  </div>
</template>

<style scoped>
</style>
