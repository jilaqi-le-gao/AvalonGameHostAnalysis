<template>
    <div>
        <v-app-bar
        color="deep-purple accent-4"
        dense
        dark
        >
        <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>

        <v-toolbar-title>阿瓦隆-西比拉系统</v-toolbar-title>

        <v-spacer></v-spacer>
        </v-app-bar>

        <v-navigation-drawer
        v-model="drawer"
        absolute
        temporary>
            <v-list-item>
                <v-list-item-content>
                <v-list-item-title class="text-h6">
                    圆桌骑士团委员会
                </v-list-item-title>
                <v-list-item-subtitle>
                    阿瓦隆-西比拉系统(简)
                </v-list-item-subtitle>
                </v-list-item-content>
            </v-list-item>

            <v-divider></v-divider>

            <v-list
                dense
                nav
            >
                <v-list-item
                link
                >
                    <v-list-item-icon>
                        <v-icon>mdi-google-controller</v-icon>
                    </v-list-item-icon>

                    <v-list-item-content>
                        <v-list-item-title>游戏进程记录系统</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
                <v-list-item
                link
                >
                    <v-list-item-icon>
                        <v-icon>mdi-history</v-icon>
                    </v-list-item-icon>

                    <v-list-item-content>
                        <v-list-item-title>游戏历史查看</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
                <v-list-item
                link
                >
                    <v-list-item-icon>
                        <v-icon>mdi-account-check</v-icon>
                    </v-list-item-icon>

                    <v-list-item-content>
                        <v-list-item-title>玩家数据统计</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
                <v-list-item
                link
                >
                    <v-list-item-icon>
                        <v-icon>mdi-chess-king</v-icon>
                    </v-list-item-icon>

                    <v-list-item-content>
                        <v-list-item-title>西比拉认定脏王评选</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
            </v-list>
        </v-navigation-drawer>
    </div>
    
</template>
<script>
export default {
    name: 'GeneralNavi',
    data () {
        return {
            drawer: false,
        }
    },
}
</script>
