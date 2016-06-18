package com.zriton.offnav.adapter;

import android.content.Context;
import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;

import com.zriton.offnav.R;
import com.zriton.offnav.model.ModelDirection;

import java.util.ArrayList;

/**
 * Created by aditya on 18/06/16.
 */
public class DirectionAdapter extends RecyclerView.Adapter<DirectionAdapter.ViewHolder> {

    public ArrayList<ModelDirection> modelDirectionArrayList = new ArrayList<>();
    Context context;
    ModelDirection modelMessage = new ModelDirection();

    public DirectionAdapter(Context context, ArrayList<ModelDirection> modelDirectionArrayList) {
        this.context = context;
        this.modelDirectionArrayList = modelDirectionArrayList;
    }

    @Override
    public ViewHolder onCreateViewHolder(ViewGroup viewGroup, int i) {
        View v = LayoutInflater.from(viewGroup.getContext())
                .inflate(R.layout.layout_direction, viewGroup, false);
        return new ViewHolder(v);
    }

    @Override
    public void onBindViewHolder(final ViewHolder holder,final int i) {
        modelMessage = modelDirectionArrayList.get(i);
        holder.distance.setText(modelMessage.distance);
        holder.content.setText(modelMessage.content);

    }

    @Override
    public int getItemCount() {

        return modelDirectionArrayList.size();
    }

    class ViewHolder extends RecyclerView.ViewHolder {

        private TextView content,distance;
        private ImageView image;

        public ViewHolder(View view) {
            super(view);
            content = (TextView) view.findViewById(R.id.content);
            distance = (TextView) view.findViewById(R.id.distance);
            image = (ImageView) view.findViewById(R.id.image);
        }
    }


}


