package com.zriton.offnav;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;

import com.zriton.offnav.adapter.DirectionAdapter;
import com.zriton.offnav.model.ModelDirection;

import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {

    RecyclerView recyclerView;
    DirectionAdapter directionAdapter;
    ArrayList<ModelDirection> modelDirectionArrayList = new ArrayList<>();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        initView();
        dummyData();
        setUpRecyclerView();
    }

    private void initView() {
        recyclerView = (RecyclerView) findViewById(R.id.recyclerView);
    }

    private void setUpRecyclerView() {
        RecyclerView.LayoutManager mLayoutManager = new LinearLayoutManager(this);
        recyclerView.setLayoutManager(mLayoutManager);
        directionAdapter = new DirectionAdapter(MainActivity.this, modelDirectionArrayList);
        recyclerView.setAdapter(directionAdapter);
    }

    private void dummyData()
    {
        for(int i=0;i<10;i++)
       modelDirectionArrayList.add(new ModelDirection("ajhksd","200 m","asd"));
    }
}
