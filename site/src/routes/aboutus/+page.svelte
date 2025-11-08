<script lang="ts">
    import type { PageProps } from './$types.js';
    import Button from '$lib/components/ui/button/button.svelte';
	import Particles from '$lib/components/ui/Particles.svelte';
    import { base } from '$app/paths';
    
    let { data }: PageProps = $props();
</script>

<style>
  .about-box {
    display: flex;
    align-items: center;           
    justify-content: space-between;
    width: 1000px;
    background-color: rgb(53, 50, 50);
    border-radius: 15px;
    padding: 20px;
    margin: 20px auto;           
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  }

  .about-text {
    flex: 1;
    text-align: left;
    margin-right: 30px;
  }

  .about-text h2 {
    margin: 0 0 10px 0;
    color:  white;
    font-size: 20px;
    font-style: italic;
    margin-left: 15px;
  }

  .about-text p {
    margin: 0;
    font-size: 14px;
    margin-left: 15px;
  }

  .profile-pic {
    width: 120px;
    height: 120px;
    border-radius: 50%;
    object-fit: cover;
    flex-shrink: 0;         
  }
</style>

<section class="mt-10 mb-30 flex flex-col gap-6 items-center align-middle justify-center">
    <h1 class="text-7xl font-bold text-center ">About Us</h1>
    <Button
        href="{base}/"
        size="sm"
        variant="secondary"
    >
        Go Back Home
    </Button>

</section>
<div class="about-box">
  <img src="/lance.jpg" alt="Lance Joseph D. Padilla" class="profile-pic" />
  <div class="about-text">
    <h2>Lance Joseph D. Padilla</h2>
    <p>Team Developer</p>
  </div>
</div>

<div class="about-box">
  <img src="/stephen.jpg" alt="Stephen James S. Gonda" class="profile-pic" />
  <div class="about-text">
    <h2>Stephen James S. Gonda</h2>
    <p>Team Developer</p>
  </div>
</div>

<div class="about-box">
  <img src="/geraldine.jpg" alt="Geraldine Abigail A. Badiola" class="profile-pic" />
  <div class="about-text">
    <h2>Geraldine Abigail A. Badiola</h2>
    <p>Team Developer</p>
  </div>
</div>

<Particles className="absolute inset-0 -z-10" refresh={true} />
