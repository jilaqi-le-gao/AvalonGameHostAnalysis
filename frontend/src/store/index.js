import Vue from 'vue'
import Vuex from 'vuex'
import GameProgressData from './GameProgressData';
import loginModule from './login';

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
		loginModule,
		GameProgressData,
	},
})
