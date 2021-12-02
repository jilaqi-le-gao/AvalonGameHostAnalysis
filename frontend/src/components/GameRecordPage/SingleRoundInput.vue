<template>
  <v-stepper-content class="mb-2" :step="StepNumber">
    
    <v-card
      elevation="8"
      outlined
      class="mb-5"
    >
      <v-card-title>
        第一试车
      </v-card-title>
      <v-combobox
        class="mx-2"
        v-model="RoundInfo.TestCarOne.Initiator"
        :items="SelectedPlayers"
        label="带车人"
        chips
      ></v-combobox>
      <v-combobox
        class="mx-2"
        v-model="RoundInfo.TestCarOne.CarPlayers"
        :items="SelectedPlayers"
        label="出车人选"
        multiple
        chips
      ></v-combobox>
      <v-combobox
        class="mx-2"
        v-model="RoundInfo.TestCarOne.VoteForYes"
        :items="SelectedPlayers"
        label="赞同本车人员"
        multiple
        chips
      ></v-combobox>
      <v-alert type="error" v-if="RoundInfo.TestCarOne.VoteForYes.length<=SelectedPlayers.length/2">同意出车人数太少！</v-alert>
      <v-alert type="info" v-if="RoundInfo.TestCarOne.VoteForYes.length>SelectedPlayers.length/2">意见一致出车！</v-alert>
      <v-select 
      v-if="RoundInfo.TestCarOne.VoteForYes.length>SelectedPlayers.length/2" 
      v-model="RoundInfo.TestCarOne.VoteResultFailNumber" 
      :items="BoomNumber"
      label="出车几炸"></v-select>
    </v-card>

    <v-card
      elevation="8"
      outlined
      class="mb-5"
    >
      <v-card-title>
        第二试车
      </v-card-title>
      <v-combobox
        class="mx-2"
        v-model="RoundInfo.TestCarTwo.Initiator"
        :items="SelectedPlayers"
        label="带车人"
        chips
      ></v-combobox>
      <v-combobox
        class="mx-2"
        v-model="RoundInfo.TestCarTwo.CarPlayers"
        :items="SelectedPlayers"
        label="出车人选"
        multiple
        chips
      ></v-combobox>
      <v-combobox
        class="mx-2"
        v-model="RoundInfo.TestCarTwo.VoteForYes"
        :items="SelectedPlayers"
        label="赞同本车人员"
        multiple
        chips
      ></v-combobox>
      <v-alert type="error" v-if="RoundInfo.TestCarTwo.VoteForYes.length<=SelectedPlayers.length/2">同意出车人数太少！</v-alert>
      <v-alert type="info" v-if="RoundInfo.TestCarTwo.VoteForYes.length>SelectedPlayers.length/2">意见一致出车！</v-alert>
      <v-select 
      v-if="RoundInfo.TestCarTwo.VoteForYes.length>SelectedPlayers.length/2" 
      v-model="RoundInfo.TestCarTwo.VoteResultFailNumber" 
      :items="BoomNumber"
      label="出车几炸"></v-select>
    </v-card>

    <v-card
      elevation="8"
      outlined
      class="mb-12"
    >
      <v-card-title>
        必出位
      </v-card-title>
      <v-combobox
        class="mx-2"
        v-model="RoundInfo.FinalCar.Initiator"
        :items="SelectedPlayers"
        label="带车人"
        chips
      ></v-combobox>
      <v-combobox
        class="mx-2"
        v-model="RoundInfo.FinalCar.CarPlayers"
        :items="SelectedPlayers"
        label="出车人选"
        multiple
        chips
      ></v-combobox>
      <v-select 
      v-model="RoundInfo.FinalCar.VoteResultFailNumber" 
      :items="BoomNumber"
      label="出车几炸"></v-select>
    </v-card>

    <v-btn
      color="primary"
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
  name: 'SingleRoundInput',
  props: [
    'RoundNumber',
    'StepNumber',
  ],
  components: {
  },
  data: function () {
    return {
      RoundInfo: {
        WinOrLoss: false,
        TestCarOne: {
          VoteResultFailNumber: null,
          Initiator: '',
          CarPlayers: [],
          VoteForYes: [],
        },
        TestCarTwo: {
          VoteResultFailNumber: null,
          Initiator: '',
          CarPlayers: [],
          VoteForYes: [],
        },
        FinalCar: {
          VoteResultFailNumber: null,
          Initiator: '',
          CarPlayers: []
        }
      },
      TestCarNum: 1,
      BoomNumber: [0, 1, 2, 3]
    }
  },
  mounted () {

  },
  methods: {
    NextStep(){
      this.$store.dispatch('GameProgressData/updateStep', this.StepNumber + 1);
    },
  },
  computed: {
    ...mapGetters ({
      SelectedPlayers: 'GameProgressData/get_SelectedPlayer',
    }),

  }
}
</script>
