<template>
  <v-stepper-content class="mb-2" step="7">
    <v-card
      elevation="8"
      outlined
      class="mb-5"
    >
      <v-select
        class="ma-2"
        v-model="RoundSummary.Kill"
        :items="SelectedPlayers"
        label="红方刀人"
      ></v-select>

      <v-switch
        class="ma-2"
        v-model="RoundSummary.WinOrLoss"
        inset
      >
        <template v-slot:label>
          <v-chip
            class="ma-2"
            label
            color="primary"
          >
            最终结果
          </v-chip>
          <v-chip color="green" v-if="RoundSummary.WinOrLoss">好人胜利</v-chip>
          <v-chip color="red" v-else>坏人胜利</v-chip>

        </template>
      </v-switch>
      
      <v-list>
        <v-subheader>人员角色</v-subheader>
        <v-list-item
          v-for="(one_c, i) in RoundSummary.Charactors"
          :key="i"
        >
          <v-select
            v-model="one_c.Player"
            :items="SelectedPlayers"
            :label="one_c.name"
          ></v-select>
        </v-list-item>
      </v-list>

      <v-combobox
        v-model="RoundSummary.ClaimPai"
        :items="SelectedPlayers"
        label="跳派玩家"
        multiple
        chips
      ></v-combobox>

    </v-card>

    <v-dialog
      v-model="dialog"
      width="500"
    >
      <v-card>
        <v-card-title class="text-h5 grey lighten-2">
          比赛记录已上传！
        </v-card-title>

        <v-card-text>
          积分统计在后台进行
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            text
          >
            俺知道了
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-btn
      color="primary"
      @click="UpdateEndGame"
    >
      确认
    </v-btn>
    
  </v-stepper-content>
</template>
<script>
import { mapGetters } from "vuex";

export default {
  name: 'GameEndingSummary',
  components: {
  },
  data: function () {
    return {
      RoundSummary: {
        Kill: '',
        WinOrLoss: false,
        Charactors: {
          Merlin: {Player: '', name: '梅林'},
          Pai: {Player: '', name: '派西维尔'},
          Morgana: {Player: '', name: '莫甘娜'},
          Assassin: {Player: '', name: '刺客'},
          BadGuy: {Player: '', name: '爪牙'},
          Aobolun: {Player: '', name: '奥博伦'},
          Modeleide: {Player: '', name: '莫德雷德'},
        },
        ClaimPai: [],
      },
      dialog: false,

    }
  },
  mounted () {

  },
  methods: {
    UpdateEndGame(){
      this.$store.dispatch('GameProgressData/save_end_game', this.RoundSummary);
      this.dialog = true;
    },
  },
  computed: {
    ...mapGetters ({
      SelectedPlayers: 'GameProgressData/get_SelectedPlayer',
    }),

  }
}
</script>
