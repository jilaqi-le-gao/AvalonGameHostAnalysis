<template>
  <v-stepper-content class="mb-2" :step="StepNumber">
    
    <!-- <v-card
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
      v-model="RoundInfo.VoteResultFailNumber" 
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
      v-model="RoundInfo.VoteResultFailNumber" 
      :items="BoomNumber"
      label="出车几炸"></v-select>
    </v-card> -->

    <v-card
      elevation="8"
      outlined
      class="mb-12"
    >
      <v-card-subtitle>
        <v-checkbox
          v-model="RoundInfo.lancelot_change"
          label="兰斯洛特是否变身份"
          color="indigo"
        ></v-checkbox>
      </v-card-subtitle>
      <v-card-title>
        最终车型
      </v-card-title>
      <v-combobox
        class="mx-2"
        v-model="RoundInfo.FinalCar.Initiator"
        :items="SelectedPlayers"
        label="带车人"
        chips
        clearable
      ></v-combobox>
      <v-combobox
        class="mx-2"
        v-model="RoundInfo.FinalCar.CarPlayers"
        :items="SelectedPlayers"
        label="出车人选"
        multiple
        chips
        clearable
      ></v-combobox>
      <v-select 
      v-model="RoundInfo.VoteResultFailNumber" 
      :items="BoomNumber"
      clearable
      label="出车几炸"></v-select>
    </v-card>

    <v-btn
      color="primary"
      @click="NextStep"
    >
      下一步
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
      TestCarNum: 1,
      BoomNumber: [0, 1, 2, 3]
    }
  },
  mounted () {

  },
  methods: {
    NextStep(){
      this.$store.dispatch('GameProgressData/updateStep', this.StepNumber + 1);
      
      // this.$store.dispatch('GameProgressData/save_each_round', {
      //   RoundInfo: this.RoundInfo,
      //   RoundIndex: this.RoundNumber,
      // })
    },
  },
  computed: {
    ...mapGetters ({
      SelectedPlayers: 'GameProgressData/get_SelectedPlayer',
    }),
    RoundInfo: {
      get () {
        return this.$store.state.GameProgressData.RoundsData[this.RoundNumber-1];
      },
      set (value) {
        this.$store.dispatch('GameProgressData/save_each_round', {
          RoundInfo: value,
          RoundIndex: this.RoundNumber,
        })
      },
    }
  },
  watch: {
    'RoundInfo.VoteResultFailNumber' (newVal) {
      if (newVal > 0){
        this.RoundInfo.WinOrLoss = false;
      }else{
        this.RoundInfo.WinOrLoss = true;
      }
    }
  }
}
</script>
