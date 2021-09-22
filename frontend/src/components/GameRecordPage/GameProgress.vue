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

      <v-stepper-content class="mb-2" step="1">
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



      <v-stepper-step
        editable
        step="2"
      >
        第一局
      </v-stepper-step>

      <v-stepper-content class="mb-2" step="2">
        <v-card
          class="mb-12"
          color="grey lighten-1"
          height="200px"
        ></v-card>

        <v-btn
          color="primary"
          @click="e1 = 3"
        >
          Continue
        </v-btn>

        <v-btn text>
          Cancel
        </v-btn>
      </v-stepper-content>



      <v-stepper-step 
        editable
        step="3">
        第二局
      </v-stepper-step>

      <v-stepper-content class="mb-2" step="3">
        <v-card
          class="mb-12"
          color="grey lighten-1"
          height="200px"
        ></v-card>

        <v-btn
          color="primary"
          @click="e1 = 1"
        >
          Continue
        </v-btn>

        <v-btn text>
          Cancel
        </v-btn>
      </v-stepper-content>

      

      <v-stepper-step 
        editable
        step="4">
        第三局
      </v-stepper-step>


      <v-stepper-step 
        editable
        step="5">
        第四局
      </v-stepper-step>
      

      <v-stepper-step 
        editable
        step="6">
        第五局
      </v-stepper-step>
      

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
export default {
  name: "GameProgress",
  data: function () {
    return {
    }
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
