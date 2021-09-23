<template>
<v-container
fluid
>
    <v-stepper v-model="current_steps" non-linear vertical>
      <v-stepper-step
        editable
        step="1"
      >
        玩家参与确认
      </v-stepper-step>

      <PlayerInputSetp />



      <v-stepper-step
        editable
        step="2"
      >
        第1轮出车记录
      </v-stepper-step>

      <SingleRoundInput :RoundNumber="1" :StepNumber="2" />



      <v-stepper-step 
        editable
        step="3">
        第2轮出车记录
      </v-stepper-step>

      <SingleRoundInput :RoundNumber="2" :StepNumber="3" />

      

      <v-stepper-step 
        editable
        step="4">
        第3轮出车记录
      </v-stepper-step>
      
      <SingleRoundInput :RoundNumber="3" :StepNumber="4" />


      <v-stepper-step 
        editable
        step="5">
        第4轮出车记录
      </v-stepper-step>
      
      <SingleRoundInput :RoundNumber="4" :StepNumber="5" />
      

      <v-stepper-step 
        editable
        step="6">
        第5轮出车记录
      </v-stepper-step>

      
      <SingleRoundInput :RoundNumber="5" :StepNumber="6" />
      

      <v-stepper-step 
        editable
        step="7">
        局终总结
      </v-stepper-step>


  </v-stepper>
</v-container>
</template>
<script>
// import { mapGetters  } from 'vuex';
import PlayerInputSetp from './PlayerInputStep.vue';
import SingleRoundInput from './SingleRoundInput.vue';

export default {
  name: "GameProgress",
  data: function () {
    return {
    }
  },
  components: {
    PlayerInputSetp,
    SingleRoundInput,
  },
  computed: {
    current_steps: {
      get () {
        return this.$store.state.GameProgressData.Stepper;
      },
      set (value) {
        this.$store.dispatch('GameProgressData/updateStep', value)
      },
    },
    // ...mapGetters ({
    //   // Stepper: 'GameProgressData/get_stepper',
    // }),
    },
}
</script>
