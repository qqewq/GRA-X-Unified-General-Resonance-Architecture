from gra_subject import SubjectSwapper, Identity

alice = Identity("Alice", {"role": "analyst"})
bob = Identity("Bob", {"role": "critic"})
swapper = SubjectSwapper(alice)
print("Current:", swapper.current.name)
swapper.swap(bob)
print("Swapped to:", swapper.current.name)
