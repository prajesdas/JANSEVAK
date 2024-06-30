package com.intakhab.hospitalmanagementhackonit.Repository;

import com.intakhab.hospitalmanagementhackonit.Model.User;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.UUID;

@Repository
public interface UserRepo extends JpaRepository<User, UUID> {
    User findByEmailOrMobileOrUsername(String email,String mobile,String username);
    User findByToken(String token);

    User findByUsername(String username);

    User findByEmail(String emailId);

    User findByMobile(String phoneNumber);

    List<User> findByRole(String admin);
}
