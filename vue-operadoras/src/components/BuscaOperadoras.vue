<template>
  <div class="container">
    <h2>Buscar Operadoras</h2>
    <input type="text" v-model="termoBusca" @input="buscarOperadoras" placeholder="Digite para buscar..." />
    <ul v-if="operadoras.length">
      <li v-for="operadora in operadoras" :key="operadora.registro_ans">
        Razão Social da Operadora: {{ operadora.Razao_Social }} | Registro ANS: ({{ operadora.Registro_ANS }})
      </li>
    </ul>
    <p v-else>Nenhum resultado encontrado.</p>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      termoBusca: "",
      operadoras: [],
    };
  },
  methods: {
    async buscarOperadoras() {
      if (this.termoBusca.length < 1) {
        this.operadoras = [];
        return;
      }

      try {
        const response = await axios.get(`http://127.0.0.1:8000/buscar/`, {
          params: { q: this.termoBusca }
        });
        this.operadoras = response.data.resultados;
      } catch (error) {
        console.error("Erro ao buscar operadoras:", error);
      }
    }
  }
};
</script>

<style>
.container {
  max-width: 600px;
  margin: auto;
  padding: 20px;
}
input {
  width: 100%;
  padding: 10px;
  margin-bottom: 10px;
}
ul {
  list-style: none;
  padding: 0;
}
li {
  padding: 5px;
  border-bottom: 1px solid #ccc;
}
</style>
