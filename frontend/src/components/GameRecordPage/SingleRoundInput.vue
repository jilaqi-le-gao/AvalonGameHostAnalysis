<template>
  <v-stepper-content step="2">
    <v-card
      class="mb-12"
      color="grey lighten-1"
      height="200px"
    ></v-card>

    <v-btn
      color="primary"
      @click="e1 = 2"
    >
      确认
    </v-btn>

    <v-btn text>
      取消
    </v-btn>
  </v-stepper-content>
</template>
<script>
export default {
  name: 'SingleRoundInput',
  components: {
  },
  data: function () {
    return {
    }
  },
  mounted () {

  },
  methods: {

  },
}
</script>
