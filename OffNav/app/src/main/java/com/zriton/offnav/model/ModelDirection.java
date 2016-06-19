package com.zriton.offnav.model;

/**
 * Created by aditya on 18/06/16.
 */
public class ModelDirection {


    public String content;
    public String distance;
    public int flag;

    public ModelDirection(String content, String distance, int flag) {
        this.content = content;
        this.distance = distance;
        this.flag = flag;
    }

    public ModelDirection() {
    }
}
