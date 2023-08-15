from typing import List


class Solution:
    # In this question we are asked to check if the prerequisites provided for
    # some courses are possible. For example, if a course A has a course B as
    # a prerequisite, but course B has course A as a prerequisite, it would be
    # impossible to make the prerequisites for that course.
    #
    # Basically, this is a question to check to see if there are any cycles within
    # a digraph of course prerequisites.
    #
    # Cycles imply an impossible requirement for a course.
    def canFinish(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
        # We create an "adjacency list" from a course to its prerequisite courses.
        prerequisites_map = [[] for _ in range(num_courses)]
        for course, prerequisite in prerequisites:
            prerequisites_map[course].append(prerequisite)

        # Once we've done a full DFS within a course we will mark it as `seen`
        # and skip future traversals of it.
        #
        # This is a necessary optimization, as without it the tests will not pass.
        seen = set()
        seeing = set()
        for course in range(num_courses):
            if course in seen:
                continue

            # We enter the `course` and then exit the course again once a traversal is complete.
            #
            # This means that the courses legitimately get placed into the stack twice, once with
            # a `False` and later on with a `True`.
            #
            # The first entry is to explore its prerequisites, while the second is to mark it as
            # fully explored / `seen` (and to 'exit' from it) once all its prerequisites have been
            # processed.
            #
            # If they appear any other time during that traversal then it implies the existence
            # of a cycle.
            stack = [(course, False)]
            while stack:
                course, is_exit = stack.pop()

                # If we encounter a `course` that is marked as an exit,
                # we will add it to `seen` so as to never traverse it again,
                # and remove it from `seeing` so that this set does not affect
                # future traversals of course prerequisites.
                if is_exit:
                    seen.add(course)
                    seeing.remove(course)
                    continue

                if course in seen:
                    continue

                # If a `course` is found within `seeing`, that implies that
                # it has appeared in the `stack` a second time in the "enter"
                # (e.g. `is_exit=False`) state.
                if course in seeing:
                    return False
                seeing.add(course)

                # After executing these two lines, we will have appended
                # the current course with an `is_exit=True` state to signal
                # the end of a course's traversal followed by each of its
                # prerequisites that we traverse using DFS.
                #
                # Note: each prerequisite also gets an `is_exit=True` state
                #       followed by its own prerequisites.
                stack.append((course, True))
                stack.extend(
                    (prerequisite_course, False)
                    for prerequisite_course in prerequisites_map[course]
                )

        return True
