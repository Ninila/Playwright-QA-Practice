# Here I had some fun manipulating elements with drag and drop
# I'm starting to feel a lot more confidence 

from playwright.sync_api import Page, expect

url = "https://www.qa-practice.com/elements/dragndrop/boxes"

# Check for elements visibility
def test_drag_drop_visibility(page: Page):
    page.goto(url)
    expect(page.locator("#rect-droppable")).to_be_visible()
    expect(page.locator("#rect-draggable")).to_be_visible()

# Now for testing the actual drag and drop functionality
def test_drag_drop_functionality(page: Page):
    page.goto(url)
    # Store the elements into variables for further use
    droppable = page.locator("#rect-droppable")
    draggable = page.locator("#rect-draggable")

    # Testing the functionality and making sure the item dropping square can't be dragged and
    # that the draggable square can no longer be dragged after inserted in the drop point
    droppable.drag_to(draggable)
    wrong_droppable_location = page.locator("#rect-draggable > #rect-droppable")
    expect(wrong_droppable_location).not_to_be_visible()

    draggable.drag_to(droppable)

    final_droppable_location = page.locator("#rect-droppable > #rect-draggable")
    expect(final_droppable_location).to_be_visible()

    draggable.drag_to(page.locator("#content"))
    final_droppable_location = page.locator("#rect-droppable > #rect-draggable")

# Testing a new tab with a draggable image
# Starting with the visibility of elements
def test_drag_images_visibility(page: Page):
    page.goto(url)
    page.get_by_role("link", name="Images").click()
    expect(page.locator("#rect-droppable1")).to_be_visible()
    expect(page.locator("#rect-droppable2")).to_be_visible()
    expect(page.locator(".rect-draggable")).to_be_visible()

# Dragging the image from one square to another, checking that the image moved and the square contents are updated
def test_drag_images_functionality(page: Page):
    page.goto(url)
    page.get_by_role("link", name="Images").click()

    draggable = page.locator(".rect-draggable")
    droppable1 = page.locator("#rect-droppable1")
    droppable2 = page.locator("#rect-droppable2")

    # Dragging image from box1 to box2
    draggable.drag_to(droppable2)
    
    # Checking box2
    final_image_location_1 = page.locator("#rect-droppable2 > .rect-draggable")
    expect(final_image_location_1).to_be_visible()

    # Checking box1 emptiness
    wrong_image_location_1 = page.locator("#rect-droppable1 > .rect-draggable")
    expect(wrong_image_location_1).not_to_be_visible()

    # Dragging image from box2 to box1
    draggable.drag_to(droppable1)
    
    # Checking box1
    final_image_location_2 = page.locator("#rect-droppable1 > .rect-draggable")
    expect(final_image_location_2).to_be_visible()

    # Checking box2 emptiness
    wrong_image_location_2 = page.locator("#rect-droppable2 > .rect-draggable")
    expect(wrong_image_location_2).not_to_be_visible()
