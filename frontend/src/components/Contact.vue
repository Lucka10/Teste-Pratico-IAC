<script setup lang="ts">
import { ref, Teleport }  from 'vue'
import axios, { type AxiosResponse } from 'axios';
const props = defineProps<{
  id:number,
  numero: number,
  nome:string,
  email:string,
  telefone:string,
  data:string,
  src:string
}>()

const confirmação = ref(false)
const Excluido = ref('')

const formata_data = function(data:string){
  return data.replace(/T.*/,'').split('-').reverse().join('/')
}

const mascara = function() {
 return '(' + props.telefone.substring(0,2) + ') ' + props.telefone.substring(2,7) + '-' + props.telefone.substring(7)
}

const excluir = function(id:number){
  axios.delete('http://127.0.0.1:8000/agenda/' + id + '/',)
  .then((response) => {
      if (response.status == 200) {
        console.log("Sucesso:", response.data)
        confirmação.value=false
        emit('excluir',[true,props.numero-1])
      }
    }
  )   
}

const emit = defineEmits(['editar','excluir'])

</script>

<template>
  <div class="container d-flex border border-3 border-dark rounded p-2"
  v-if="!confirmação"
  >
    <h1 class="d-flex align-items-center flex-row">#{{  String(numero).padStart(3, '0') }}</h1>
    <img class="border border-dark mx-3 d-flex flex-shrink-1 img-thumbnail" :src="src" width="140px" height="140px  " >
    <div class="container d-flex flex-column flex-grow-1 justify-content-between p-0">
        <div class="fw-bold fs-5">Nome:{{ nome }}</div>
        <div class="fw-bold fs-5">Email: {{ email }}</div>
        <div class="fw-bold fs-5">Telefone:{{ mascara() }}</div>
        <div class="fw-bold fs-5">Data de nascimento:{{ formata_data(data) }}</div>
    </div>
    <div class="container d-flex flex-column justify-content-evenly" style="max-width: fit-content;">
        <button class="btn btn-warning bi bi-pencil px-3" @click="emit('editar',[nome,mascara()])"> Editar</button>
        <button class="btn btn-danger bi bi-x-square px-3" @click="() => {confirmação=true;Excluido=nome}"> Excluir</button>
    </div>
  </div>

  <div class="container d-flex border border-3 border-dark rounded p-2"
  v-if="confirmação">

  <h1 class="d-flex align-items-center">#{{  String(numero).padStart(3, '0') }}</h1>
  <img class="border border-dark mx-3 d-flex flex-shrink-1 img-thumbnail" :src="src" width="140px" height="140px" >

  <div class="container d-flex flex-column flex-grow-1 gap-3 justify-content-center align-items-center p-0">
    <h2>Confirmar exclusão de {{ Excluido }}?</h2>
    <div class="container d-flex justify-content-around ">
      <button class="btn btn-success px-4"  @click="confirmação = !confirmação"> Cancelar</button>
      <button class="btn btn-danger bi bi-x-square px-3" 
        @click="() => {excluir(id);}">Excluir
      </button>
    </div>
  </div>
  </div>
</template>

<style scoped>
</style>
