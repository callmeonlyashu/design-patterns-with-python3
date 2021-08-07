<?php

interface Worker {
  public function takeBreak();
  public function getPaid();
}
 
interface Coder {
  public function code();
}
 
interface ClientFacer {
  public function callToClient();
  public function attendMeetings();
}

class Developer implements Worker, Coder {
  // Do your stuff
}
 
class Manager implements Worker, ClientFacer {
  // Do your stuff.
}