<?php

abstract class Quadrilateral {

  public abstract function setHeight($h);
 
  public abstract function setWidth($w);
 
  public abstract function getArea();

}
 
class Rectangle implements Quadrilateral {

    public function setWidth($h) {
      // Do Stuff
    }
 
    public function setHeight($h) {
      // Do Stuff
    }

    public function getArea() {
      // Do Stuff
    }
}
 
class Square implements Quadrilateral {

    public function setHeight($h) {
      // Do Stuff
    }

    public function setWidth($h) {
      // Do Stuff
    }

    public function getArea() {
      // Do Stuff
    }
}