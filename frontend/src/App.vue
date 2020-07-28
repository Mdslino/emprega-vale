<template lang="pug">
    div#app.container.is-fluid
        Navigation
        router-view
</template>
<script>
import Navigation from "@/components/Navbar";

export default {
  name: "app",
  components: {
    Navigation: Navigation
  }
};
</script>
