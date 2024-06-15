<template>
  <div class="background h-full">
    <div class="h-full backdrop-blur-sm">
      <div class="grid place-items-start gap-2 p-10 md:p-32 xl:p-60">
        <h1
          class="logo text-accent select-none rounded-2xl bg-background-main p-2 text-2xl font-extrabold text-brand-main drop-shadow-lg"
        >
          FastMark
        </h1>
        <p class="w-full text-4xl font-light text-slate-50 drop-shadow-lg md:w-1/2">
          A quick and convenient markdown editor to match all of your needs! Start creating
          immediately or sign in to sync your documents.
        </p>
        <div class="flex flex-wrap gap-2">
          <RouterLink
            to="/editor"
            class="select-none rounded-2xl bg-brand-main px-4 py-1 text-lg font-bold uppercase text-background-main text-slate-50 drop-shadow-lg transition-all duration-75 ease-in-out hover:scale-105 hover:cursor-pointer"
          >
            Editor
          </RouterLink>
          <RouterLink
            to="/auth"
            class="select-none rounded-2xl bg-brand-main px-4 py-1 text-lg font-bold uppercase text-background-main text-slate-50 drop-shadow-lg transition-all duration-75 ease-in-out hover:scale-105 hover:cursor-pointer"
          >
            Register
          </RouterLink>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
.background {
  background-image: linear-gradient(rgba(75, 75, 75, 0.534), rgba(0, 0, 0, 0.925) 80%),
    url('../assets/backgrounds/landing.png');
  background-size: cover;
  background-position: center;
}
</style>
