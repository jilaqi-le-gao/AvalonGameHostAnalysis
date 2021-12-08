<template>
  <v-app>
    <v-container 
      fill-height fluid 
    >
      <v-layout align-center justify-center>
        <v-flex xs12 sm8 md4 lg2 xl2>
          <v-card class="elevation-12">
            <v-toolbar dark color="primary">
              <v-toolbar-title>你已登出</v-toolbar-title>
            </v-toolbar>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn
                color="primary"
                text
                href="../login"
              >
                重新登录
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </v-app>
</template>


<script>

  export default {
    name: 'LogOut',
    components: {
      
    },

    data: () => ({
      //
    }),
    mounted () {
      
    },
    methods: {

    },
  };
</script>

<style lang="css" scoped>

</style>