<script setup lang="ts">
import {ref} from 'vue'
const props = defineProps<{
  
    text:string
    id:number
    alerta?:boolean
}>()

const classalert = ref('bg-success mx-2 my-2 fw-bold d-flex justify-content-center align-items-center border border-dark rounded p-2')
if (props.alerta) {
    classalert.value = 'bg-danger mx-2 my-2 fw-bold d-flex justify-content-center align-items-center border border-dark rounded p-2'
}

const emit = defineEmits(['fechar'])
setTimeout(()=>emit('fechar',props.id), 3000);
</script>

<template>
   <div :class="classalert" @click="$emit('fechar',id)"> 
      <h4>{{ text }}</h4>
    </div>
</template>

<style scoped>
</style>
