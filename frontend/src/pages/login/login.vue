<template>
  <v-app :style="{background: $vuetify.theme.themes[theme].background}">
    <v-main>
      <v-container fill-height>
        <div class="auth-wrapper auth-v1">
          <div class="auth-inner">
            <v-card class="auth-card">
              <v-card-title class="d-flex align-center justify-center py-7">
                <router-link
                  to="/"
                  class="d-flex align-center"
                >
                  <v-img
                    src="@/assets/sibyl.jpg"
                    max-height="50px"
                    max-width="50px"
                    alt="logo"
                    contain
                    class="ma-3 "
                  ></v-img>

                  
                </router-link>
                <h2 class="text-2xl font-weight-semibold">
                  阿瓦隆--西比拉系统
                </h2>
              </v-card-title>

              <!-- title -->
              <v-card-text>
                <p class="text-2xl font-weight-semibold text--primary mb-2">
                  阿瓦隆小分队
                </p>
                <p class="mb-2">
                  准备登入
                </p>
              </v-card-text>

              <v-card-text>
                <form 
                  @submit.prevent="signin"
                >
                  <v-row>
                    <v-text-field
                      prepend-icon="mdi-account"
                      outlined
                      hide-details
                      label="用户名"
                      v-model="LoginInfo.username"
                      class="mb-3"
                    >
                    </v-text-field>
                  </v-row>
                  <v-row>
                    <v-text-field
                      outlined
                      :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
                      :type="show1 ? 'text' : 'password'"
                      @click:append="show1 = !show1"
                      prepend-icon="mdi-key"
                      label="密码"
                      hide-details
                      v-model="LoginInfo.password"
                    >
                    </v-text-field>
                  </v-row>
                  <v-row>
                    <div class="d-flex align-center justify-space-between flex-wrap">
                      <v-checkbox
                        label="记住我"
                        hide-details
                        class="me-3 mt-1"
                      >
                      </v-checkbox>
                    </div>
                  </v-row>

                  <v-row
                    justify="center"
                  >
                    <v-btn
                      block
                      class="my-6"
                      type="submit"
                      color="primary"
                    >
                      登录
                    </v-btn>
                  </v-row>
                </form>
              </v-card-text>
            </v-card>
          </div>
        </div>
        <div class="text-center">
          <v-dialog
            v-model="login_fail_status"
            width="500"
          >
            <v-card>
              <v-card-title class="text-h5 grey lighten-2">
                登录失败
              </v-card-title>

              <v-card-text>
                用户名密码不正确，请检查
              </v-card-text>

              <v-divider></v-divider>

              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn
                  color="primary"
                  text
                  @click="close_login_dialog"
                >
                  了解
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
        </div>
      </v-container>
    </v-main>
    <v-footer app="app" class="justify-center" color="background">
      © 2021. 阿瓦隆小组 用爱发电
    </v-footer>
  </v-app>
</template>


<script>

  export default {
    name: 'LogIn',
    components: {
      
    },

    data: () => ({
      //
      show1: false,
      LoginInfo: {
        // username,
        // password,
      }
    }),
    mounted () {
      this.$store.dispatch('loginModule/getSaveCsrftoken');
    },
    methods: {
      signin () {
        this.$store.dispatch('loginModule/loginUser', this.LoginInfo);
      },
      close_login_dialog () {
        this.$store.dispatch('loginModule/closeLoginFail');
      }
    },
    computed: {
      login_fail_status () {
        return this.$store.getters['loginModule/get_login_fail'];
      },
      theme(){
        return (this.$vuetify.theme.dark) ? 'dark' : 'light'
      }
    }
  };
</script>

<style lang="scss">
  .auth-wrapper {
    display: flex;
    min-height: calc(var(--vh, 1vh) * 100);
    width: 100%;
    flex-basis: 100%;
    align-items: center;

  // common style for both v1 and v2
  a {
    text-decoration: unset;
  }

  // auth v1
  &.auth-v1 {
    align-items: center;
    justify-content: center;
    overflow: hidden;
    padding: 1.5rem;

    .auth-mask-bg {
      position: absolute;
      bottom: 0;
      width: 100%;
    }
    .auth-tree,
    .auth-tree-3 {
      position: absolute;
    }
    .auth-tree {
      bottom: 0;
      left: 0;
    }
    .auth-tree-3 {
      bottom: 0;
      right: 0;
    }

    // auth card
    .auth-inner {
      width: 28rem;
      z-index: 1;
      .auth-card {
        padding: 0.9375rem 0.875rem;
      }
    }
  }
}
</style>