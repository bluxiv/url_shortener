<template>
  <v-row>
    <v-col cols="8" class="d-flex flex-column justify-center">
      <h1 class="text-h2 font-weight-black text-light-blue mb-6 text-center">
        Shorten your links!
      </h1>

      <div>
        <LinkForm />
      </div>
    </v-col>
    <v-col cols="4">
      <v-img src="/hero.png" />
    </v-col>
    <v-col cols="12">
      <MostVisited />
    </v-col>
  </v-row>
</template>

<script setup lang="ts"></script>

<style scoped></style>
