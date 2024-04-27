<script setup lang="ts">
import axios, { type AxiosResponse } from 'axios';

const props = defineProps<{
  id:number,
  numero: number,
  nome:string,
  email:string,
  telefone:number,
  data:string,
  src:string
}>()
const formata_data = function(data:string){
  return data.replace(/T.*/,'').split('-').reverse().join('/')
}

const excluir = function(id:number){
  axios.delete('http://127.0.0.1:8000/agenda/delete/' + id + '/',)
  .then((response) => {
      if (response.status == 200) {
        console.log("Sucesso:", response.data)
        
      }
    }
  )   
}
</script>

<template>
  <div class="container d-flex border border-3 border-dark rounded p-2">
    <h1 class="d-flex align-items-center">#{{ numero }}</h1>
    <img class="border border-dark mx-3 d-flex flex-shrink-1" :src="src" width="140" height="140" >
    <div class="container d-flex flex-column flex-grow-1 justify-content-between p-0">
        <div class="fw-bold fs-5">Nome:{{ nome }}</div>
        <div class="fw-bold fs-5">Email: {{ email }}</div>
        <div class="fw-bold fs-5">Telefone:{{ telefone }}</div>
        <div class="fw-bold fs-5">Data de nascimento:{{ formata_data(data) }}</div>
    </div>
    <div class="container d-flex flex-column justify-content-evenly" style="max-width: fit-content;">
        <button class="btn btn-warning bi bi-pencil px-3" @click="$emit('novo_contato',nome)"> Editar</button>
        <button class="btn btn-danger bi bi-x-square px-3" @click="() => {excluir(id);$emit('response',[true,props.numero-1])}"> Excluir</button>
    </div>

  </div>
</template>

<style scoped>
</style>
