<template>
  <div>
    <Header />
    <Filter-menu/>
    <Slider />
  </div>
</template>

<script>
  import Header from '../components/Header.vue'
  import FilterMenu from '../components/FilterMenu.vue'
  import Slider from '../components/Slider.vue'
  export default {
    name: 'Home',
    components: {
      Header,
      FilterMenu,
      Slider
    }
  }
</script>

