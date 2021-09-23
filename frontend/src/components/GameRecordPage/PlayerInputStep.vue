<template>
  <v-stepper-content class="mb-2" step="1">
    <v-col cols="12">
      <v-combobox
        v-model="SelectedPlayers"
        :items="PlayerList"
        label="选择本局参与的玩家"
        multiple
        chips
      ></v-combobox>
    </v-col>

    <v-col cols="12">
      <v-alert
        dense
        type="info"
      >
        本局为 {{ PlayerNumber }} 人局
      </v-alert>
    </v-col>

    <v-btn
      color="primary"
      :disabled="PlayerNumber<5"
      @click="NextStep"
    >
      确认
    </v-btn>

    <v-btn text>
      取消
    </v-btn>
  </v-stepper-content>
</template>
<script>
import { mapGetters } from "vuex";

export default {
  name: 'PlayerInputSetp',
  components: {
  },
  data: function () {
    return {
    }
  },
  mounted () {

  },
  methods: {
    NextStep(){
      this.$store.dispatch('GameProgressData/updateStep', 2);
    },
  },
  computed: {
    ...mapGetters ({
      PlayerList: 'GameProgressData/get_PlayerList',
    }),
    SelectedPlayers: {
      get () {
        return this.$store.state.GameProgressData.SelectedPlayers;
      },
      set (value) {
        this.$store.dispatch('GameProgressData/saveSelectedPlayers', value)
      },
    },
    PlayerNumber (){
      return this.SelectedPlayers.length;
    },
  }
}
</script>
