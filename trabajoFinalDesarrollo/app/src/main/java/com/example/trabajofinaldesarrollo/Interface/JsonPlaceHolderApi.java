package com.example.trabajofinaldesarrollo.Interface;

import com.example.trabajofinaldesarrollo.Model.Posts;

import java.util.List;

import retrofit2.Call;
import retrofit2.http.GET;

public interface JsonPlaceHolderApi {
    @GET("erp/category/API/")
    Call<List<Posts>> getPost();
}


