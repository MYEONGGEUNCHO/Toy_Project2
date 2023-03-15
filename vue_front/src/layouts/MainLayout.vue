<template>
  <q-layout view="hHh LpR fFf">
    <q-header elevated class="bg-primary text-white">
      <q-toolbar>
        <q-btn flat dense round icon="menu" aria-label="Menu" @click="toggleLeftDrawer" />

        <q-toolbar-title>
          <q-avatar rounded>
            <img src="src/assets/image/Bitcoin.jpg">
          </q-avatar>
          Bit Too
        </q-toolbar-title>

        <div>Quasar v{{ $q.version }}
          <q-btn color="secondary" icon="login" label="sign in" @click="loginHandler" class="q-mx-md" />
        </div>
      </q-toolbar>
    </q-header>

    <q-drawer v-model="leftDrawerOpen" side="left" overlay bordered>
      <q-list>
        <q-item-label header>
          <!-- Essential Links -->
          다들 꽉잡아 누워~ ●▅▇█▇▆▅▄▇
        </q-item-label>

        <EssentialLink v-for="link in essentialLinks" :key="link.title" v-bind="link" />
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>

    <q-footer elevated class="bg-grey-8 text-white">
      <q-toolbar>
        <q-toolbar-title>
          <div>이걸 진짜 만들고 있네</div>
        </q-toolbar-title>
      </q-toolbar>
    </q-footer>
  </q-layout>
</template>

<script setup>
import { ref } from 'vue'
import EssentialLink from 'components/EssentialLink.vue'
import { user } from 'src/boot/apiList'

const leftDrawerOpen = ref(false)

const essentialLinks = [
  {
    title: 'Docs',
    caption: 'quasar.dev',
    icon: 'school',
    link: 'https://quasar.dev'
  },
  {
    title: 'Github',
    caption: 'github.com/quasarframework',
    icon: 'code',
    link: 'https://github.com/quasarframework'
  },
];

const toggleLeftDrawer = () => {
  leftDrawerOpen.value = !leftDrawerOpen.value;
}

const loginHandler = () => {
  user.login({
    username: 1,
    password: 1234,
  }).then((res) => {
    console.log(res);
  })
}
</script>
