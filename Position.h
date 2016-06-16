#ifndef _POSITION_H
#define _POSITION_H

class Position
{
  private:
    Position(){};
    virtual ~Position(){};	
    static Position* pos;
  public:	
    static Position* getInstance(void){
      return pos;
    };
    float reducer;
};


#endif