#student name : mumandam frank randy
#department: software engineering
#student matricule number: 520225
guest_list = ["franklin, angela, theodore, rexvan"]

for guest in  guest_list:
    print("franklin you are invited to dinner")
    print("angela you are invited to dinner")
    print("theodore you are invited to dinner")
    print("rexvan you are invited to dinner")

    guest_list = ["franklin, angela, theodore, rexvan"]
    guest_who_cant_make_it =("franklin")

print(f"sadly, {guest_who_cant_make_it}, cant make it")
del guest_list[0]

guest_list.insert(0, "thomas") 

print("thomas you are invited to dinner")
print("angela you are invited to dinner")
print("theodore you are invited to dinner")
print("rexvan you are invited to dinner")

guest_list = ["thomas, angela, theodore, rexvan"]

print("good news everyone! i just found a bigger dinner table.")

guest_list.insert(0, "awah")
guest_list.insert(2, "micheal")
guest_list.append("zubby")

print("awah, iminviting you to dinner")
print("thomas,im inviting you to dinner")
print("micheal, im inviting you to dinner")
print("angela, im inviting you to dinner")
print("theodore, im inviting you to dinner")
print("rexvan, im inviting you to dinner")
print("zubby, im inviting you to dinner")


