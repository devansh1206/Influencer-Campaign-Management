<template>
    <div class="landing-page">
      <!-- Navbar -->
      <nav class="navbar navbar-expand-lg navbar-dark bg-transparent fixed-top">
        <div class="container">
          <a class="navbar-brand" href="#">CampaignManager</a>
          <button
            class="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarNav"
            aria-controls="navbarNav"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav ms-auto">
              <li class="nav-item">
                <button @click="toLogin" class="btn btn-outline-light me-2">Login</button>
              </li>
              <li class="nav-item">
                <button @click="toInfluencerRegister" class="btn btn-outline-success me-2">Register as Influencer</button>
              </li>
              <li class="nav-item">
                <button @click="toSponsorRegister" class="btn btn-outline-info">Register as Sponsor</button>
              </li>
            </ul>
          </div>
        </div>
      </nav>
  
      <!-- Hero Section -->
      <div class="hero-section d-flex flex-column justify-content-center align-items-center">
        <div class="text-center text-white">
          <h1 class="display-3 fw-bold">Campaigns Made Easy</h1>
          <p class="lead">Connecting influencers with sponsors for successful campaigns.</p>
          <div class="mt-4">
            <button @click="toCampaigns" class="btn btn-primary btn-lg me-3">Explore Campaigns</button>
            <button @click="toCreateCampaign" class="btn btn-outline-light btn-lg">Create a Campaign</button>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "Home",
    methods: {
      toLogin() {
        this.$router.push('/userLogin');
      },
      toInfluencerRegister() {
        this.$router.push('/influencerRegister');
      },
      toSponsorRegister() {
        this.$router.push('/sponsorRegister');
      },
      toCampaigns() {
        this.$router.push('/campaigns'); // Assuming you have a route for viewing campaigns
      },
      toCreateCampaign() {
        this.$router.push('/createCampaign'); // Assuming a route for campaign creation
      }
    }
  };
  </script>
  
  <style scoped>
  /* Hero Section Background */
  .landing-page {
    height: 100vh;
    background-image: url('https://wallpapercave.com/wp/wp5181437.jpg'); /* Replace with actual campaign-related image */
    background-size: cover;
    background-position: center;
    position: relative;
  }
  
  /* Overlay for darkening background */
  .landing-page::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.5); /* Dark overlay */
    z-index: 0;
  }
  
  /* Hero content */
  .hero-section {
    z-index: 1;
    text-align: center;
    padding: 0 2rem;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    color: white;
  }
  
  /* Styling for buttons */
  button {
    padding: 0.75rem 1.5rem;
    font-size: 1.25rem;
  }
  
  button:hover {
    transition: background-color 0.3s ease;
  }
  
  /* Navbar styling */
  .navbar {
    padding: 1rem 2rem;
    background: transparent;
  }
  
  .navbar-brand {
    font-size: 1.75rem;
    font-weight: bold;
  }
  
  .navbar-toggler-icon {
    color: white;
  }
  
  @media (max-width: 768px) {
    h1 {
      font-size: 2.5rem;
    }
  
    p.lead {
      font-size: 1.25rem;
    }
  }
  </style>
  