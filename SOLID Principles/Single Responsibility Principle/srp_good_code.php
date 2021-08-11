<?php

class User {
  
    private $email;
    
    // Getter and setter...

    public function setEmail() {
      // Setter
    }

    public function getEmail() {
      // Getter
    }
}


class UserDB {
  
    public function store(User $user) {
        // Store the user into a database...
    }
}