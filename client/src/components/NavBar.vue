<template>
  <div
    class="bg-background-main top-0 z-50 box-border flex flex-col items-center justify-between gap-4 px-5 py-3 sm:px-16 md:flex-row lg:px-44"
  >
    <div class="nav-header flex w-full flex-row justify-between">
      <div class="logo text-accent text-brand-main select-none text-2xl font-extrabold">
        FastMark
      </div>
      <MenuIcon
        fillColor="white"
        class="hover:cursor-pointer md:hidden"
        v-if="!expanded"
        @click="openMenu"
      />
      <MenuCloseIcon
        fillColor="white"
        class="hover:cursor-pointer md:hidden"
        v-else
        @click="closeMenu"
      />
    </div>
    <ul
      :class="expanded ? 'flex' : 'hidden'"
      class="text-brand-main flex-col items-center gap-1 text-lg font-bold md:flex md:flex-row md:justify-between md:space-x-4"
    >
      <li
        class="bg-brand-main text-background-main select-none rounded-md px-2 hover:cursor-pointer"
      >
        +New
      </li>
      <li class="select-none hover:cursor-pointer">Collection</li>
      <li class="select-none hover:cursor-pointer">About</li>
      <li @click="toggleDarkMode" class="select-none hover:cursor-pointer">
        <ThemeLightDarkIcon />
      </li>
      <li class="select-none hover:cursor-pointer"><AccountBoxIcon /></li>
    </ul>
  </div>
</template>

<script>
import MenuIcon from 'vue-material-design-icons/Menu.vue'
import MenuCloseIcon from 'vue-material-design-icons/MenuClose.vue'
import ThemeLightDarkIcon from 'vue-material-design-icons/ThemeLightDark.vue'
import AccountBoxIcon from 'vue-material-design-icons/AccountBox.vue'

export default {
  components: {
    MenuIcon,
    MenuCloseIcon,
    ThemeLightDarkIcon,
    AccountBoxIcon,
  },
  data() {
    return {
      expanded: false,
    }
  },
  methods: {
    openMenu() {
      this.expanded = true
    },
    closeMenu() {
      this.expanded = false
    },
    toggleDarkMode() {
      if (document.documentElement.getAttribute('data-theme') === 'dark') {
        document.documentElement.setAttribute('data-theme', 'light')
      } else {
        document.documentElement.setAttribute('data-theme', 'dark')
      }
    },
  },
}
</script>
