<?php

interface CarInterface {
    public function drive();
}

interface AirplaneInterface {
    public function fly();
}

class FutureCar implements CarInterface, AirplaneInterface {
    
    public function drive() {
        echo 'Driving a future car!';
    }
  
    public function fly() {
        echo 'Flying a future car!';
    }
}

class Car implements CarInterface {
    
    public function drive() {
        echo 'Driving a car!';
    }
}

class Airplane implements AirplaneInterface {
    
    public function fly() {
        echo 'Flying an airplane!';
    }
}