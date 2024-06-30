package com.intakhab.hospitalmanagementhackonit.Model;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class Contact {
    private String name;
    private String email;
    private String message;
}
