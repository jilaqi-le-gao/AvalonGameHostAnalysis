<template>
<v-app>
    <GeneralNavi />
    <v-main>
        <GameProgress />
    </v-main>
</v-app>
</template>

<script>
import GeneralNavi from '@/components/NavigationSide';
import GameProgress from '@/components/GameRecordPage/GameProgress';

export default {
	name: 'GameRecordPage',
	components: {
        GeneralNavi,
        GameProgress,
	},
	data: () => {

	},
	mounted () {

	},
	methods: {

	},
}
</script>