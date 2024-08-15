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
    async register() {
      if (this.username === '' || this.password === '') {
        console.log('Fill out all from elements')
        return
      }

      if (this.password != this.confirmPassword) {
        console.log('Passwords do not match')
        console.log(this.password + this.confirmPassword)
        return
      }

      const response = await fetch('http://localhost:5001/register', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          username: this.username,
          password: this.password,
        }),
      })

      if (response.ok) {
        console.log('Account created')
        console.log(response.text)
      } else {
        console.log('Response failed')
        console.log(response.text)
      }
    },
    async login() {
      const response = await fetch('http://localhost:5001/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          username: this.loginUsername,
          password: this.loginPassword,
        }),
      })

      const data = await response.json()
      if (response.ok) {
        console.log('login succeeded')
        console.log(data)
      } else {
        console.log('Login failed. Try again')
      }
    },
  },
}
</script>

<style></style>
