import Vue from 'vue'
import Vuex from 'vuex'
import GameProgressData from './GameProgressData';

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
		GameProgressData,
	},
})
