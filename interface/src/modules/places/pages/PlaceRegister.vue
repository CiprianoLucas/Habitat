<template>
    <div class="container mt-5">
		<h1 class="text-center">Registrar condomínio</h1>
			<div class="mb-3">
				<label for="name" class="form-label">Nome:</label>
				<input 
					type="text" 
					class="form-control" 
					id="name" 
					v-model="placeForm.name" 
					required 
				/>
			</div>

	<div class="mb-3">
		<label for="number" class="form-label">Número:</label>
		<input 
			type="text" 
			class="form-control" 
			id="number" 
			v-model="placeForm.number" 
			required 
		/>
	</div>

	<div class="mb-3">
		<label for="street" class="form-label">Rua:</label>
		<input 
			type="text" 
			class="form-control" 
			id="street" 
			v-model="placeForm.street" 
			required 
		/>
	</div>

	<div class="mb-3">
		<label for="city" class="form-label">Cidade:</label>
		<input 
			type="text" 
			class="form-control" 
			id="city" 
			v-model="placeForm.city" 
			required 
		/>
	</div>

	<div class="mb-3">
		<label for="state" class="form-label">Estado:</label>
		<input 
			type="text" 
			class="form-control" 
			id="state" 
			v-model="placeForm.state" 
			required 
		/>
	</div>

      	<button v-if="!placeId" @click="registerPlace" class="btn btn-primary">Cadastrar</button>
		<div v-else>
      		<button  @click="updatePlace" class="btn btn-primary mx-3">Atualizar</button>
			<router-link class="btn btn-secondary mx-3" :to="`/condominio/${placeId}/sindicos`">Cadastrar síndicos</router-link>
			<router-link class="btn btn-secondary mx-3" :to="`/condominio/${placeId}/moradores`">Cadastrar moradores</router-link>
		</div>
  	</div>
</template>
  
<script lang="ts" setup>
    import { ref, onMounted } from 'vue'
	import { useRoute, useRouter } from 'vue-router'
    import { api } from '@/http'
    
	const route = useRoute();
	const router = useRouter();
	const placeId = ref(route.params.id);

    const placeForm = ref({
        name: '',
        number: '',
        street: '',
        city: '',
        state: ''
    });

    function registerPlace() {
        api.post('/place/', placeForm.value)
		.then(({data})=>{
			placeId.value = data.id
			router.push({ name: 'condominio_editar', params: { id: data.id } })
		})
    };

	function updatePlace() {
        api.put(`/place/${placeId.value}/`, placeForm.value)
    };

	onMounted(() => {
		if (placeId.value){
			api.get(`/place/${placeId.value}/`)
			.then(response => {
				placeForm.value = response.data;
			})
			.catch(error => {
				console.error("Erro ao obter os detalhes do local:", error);
			});
		}
	});

</script>