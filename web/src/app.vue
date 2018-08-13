<style scoped>
    @import 'styles/common.css';


</style>
<template>
    <div>


        <router-link to="/">首页 </router-link>
        <router-link to="/table">表格 </router-link>

        <router-view></router-view>
    </div>
</template>
<script>


    export default {
        data () {
            return {}
        },
        mounted () {

        },
        beforeDestroy () {

        },
        methods: {

        }
    }
</script>
