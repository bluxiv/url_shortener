<template>
  <v-app class="bg-light-blue-lighten-5 h-100 w-100">
    <v-app-bar flat class="bg-light-blue-lighten-5 border-b">
      <v-container
        class="mx-auto d-flex align-center justify-space-between ga-2 position-relative"
      >
        <div class="position-absolute w-100 d-flex align-center justify-center">
          <v-btn
            v-for="(item, index) in 3"
            :text="`link ${index + 1}`"
            variant="text"
            class="rounded-pill"
          ></v-btn>
        </div>
        <v-btn
          class="rounded-pill"
          variant="text"
          :to="{ name: 'index' }"
          text="home"
        >
        </v-btn>
        <v-btn
          variant="flat"
          color="light-blue"
          class="rounded-pill"
          append-icon="mdi-arrow-right"
        >
          LINK 4
        </v-btn>
      </v-container>
    </v-app-bar>
    <v-main
      style="
        --v-layout-left: 0px;
        --v-layout-right: 0px;
        --v-layout-top: 64px;
        --v-layout-bottom: 0px;
      "
    >
      <v-container>
        <slot />
      </v-container>
    </v-main>
  </v-app>
</template>

<script setup lang="ts"></script>

<style scoped></style>
