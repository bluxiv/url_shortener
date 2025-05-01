<template>
  <div class="d-flex align-center justify-center">
    <v-progress-circular
      color="primary"
      indeterminate
      :size="57"
      :width="6"
    ></v-progress-circular>
  </div>
</template>

<script setup lang="ts">
definePageMeta({
  middleware: ["redirect"],
});
</script>

<style></style>
