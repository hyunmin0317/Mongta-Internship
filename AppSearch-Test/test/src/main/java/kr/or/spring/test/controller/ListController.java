package kr.or.spring.test.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;


@Controller
public class ListController {
	
	@GetMapping(path="/list")
	public String list() {
		return "list";
	}
}