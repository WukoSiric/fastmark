<template>
  <div class="mt-8 grid h-full grid-cols-1 items-start gap-4 px-48 md:mt-24 md:grid-cols-2">
    <div
      class="grid w-full place-items-center gap-4 rounded-xl bg-background-sidebar py-12 drop-shadow-2xl"
    >
      <h1 class="text-4xl font-bold text-brand-main drop-shadow-md">Register</h1>
      <input
        name="username"
        type="text"
        placeholder="Username"
        v-model="username"
        class="rounded-md bg-background-main p-2 text-txt-editor drop-shadow-md"
      />
      <input
        name="password"
        type="password"
        placeholder="Password"
        v-model="password"
        class="rounded-md bg-background-main p-2 text-txt-editor drop-shadow-md"
      />
      <input
        name="confirmPassword"
        type="password"
        placeholder="Confirm Password"
        v-model="confirmPassword"
        class="rounded-md bg-background-main p-2 text-txt-editor drop-shadow-md"
      />
      <button
        class="rounded-md bg-brand-main px-5 py-2 font-bold text-background-main hover:cursor-pointer"
        @click="register"
      >
        Register
      </button>
    </div>
    <div
      class="grid w-full place-items-center gap-4 rounded-xl bg-background-sidebar py-12 drop-shadow-2xl"
    >
      <h1 class="text-4xl font-bold text-brand-main drop-shadow-md">Login</h1>
      <input
        name="loginUsername"
        type="text"
        placeholder="Username"
        v-model="loginUsername"
        class="rounded-md bg-background-main p-2 text-txt-editor drop-shadow-md"
      />
      <input
        name="loginPassword"
        type="password"
        placeholder="Password"
        v-model="loginPassword"
        class="rounded-md bg-background-main p-2 text-txt-editor drop-shadow-md"
      />
      <button
        class="rounded-md bg-brand-main px-5 py-2 font-bold text-background-main hover:cursor-pointer"
        @click="login"
      >
        Login
      </button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      // Register
      username: '',
      password: '',
      confirmPassword: '',
      // Login
      loginUsername: '',
      loginPassword: '',
    }
  },
  methods: {
    register() {
      console.log('Registering...')
    },
    login() {
      console.log('Logging in...')
    },
  },
}
</script>

<style></style>
