package com.intakhab.hospitalmanagementhackonit;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.PropertySource;

@SpringBootApplication
@PropertySource("classpath:views.properties")
public class HospitalManagementHackONitApplication {

    public static void main(String[] args) {
        SpringApplication.run(HospitalManagementHackONitApplication.class, args);
    }

}
