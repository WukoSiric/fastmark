<template>
  <div
    class="sticky top-0 flex flex-col items-center justify-between gap-4 bg-background-main px-5 py-3 sm:px-16 md:flex-row lg:px-44"
  >
    <div class="nav-header flex w-full flex-row justify-between">
      <RouterLink
        to="/"
        class="logo text-accent select-none text-2xl font-extrabold text-brand-main"
      >
        FastMark
      </RouterLink>
      <MenuIcon
        fillColor="var(--blue-brand)"
        class="hover:cursor-pointer md:hidden"
        v-if="!expanded"
        @click="openMenu"
      />
      <MenuCloseIcon
        fillColor="var(--blue-brand)"
        class="hover:cursor-pointer md:hidden"
        v-else
        @click="closeMenu"
      />
    </div>
    <ul
      :class="expanded ? 'flex' : 'hidden'"
      class="flex-col items-center gap-1 text-lg font-bold text-brand-main md:flex md:flex-row md:justify-between md:space-x-4"
    >
      <RouterLink
        to="/editor"
        class="select-none rounded-md bg-brand-main px-2 text-background-main hover:cursor-pointer"
      >
        Editor
      </RouterLink>
      <li class="select-none hover:cursor-pointer">
        <RouterLink to="/collection">Collection</RouterLink>
      </li>
      <li @click="toggleDarkMode" class="select-none hover:cursor-pointer">
        <ThemeLightDarkIcon />
      </li>
      <li class="select-none hover:cursor-pointer">
        <RouterLink to="/auth"><AccountBoxIcon /></RouterLink>
      </li>
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
