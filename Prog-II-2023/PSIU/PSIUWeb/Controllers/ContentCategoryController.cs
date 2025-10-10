using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using PSIUWeb.Data.Interface;
using PSIUWeb.Models;

namespace PSIUWeb.Controllers
{
    public class ContentCategoryController : Controller
    {
        private IContentCategoryRepository contentCategoryRepository;

        public ContentCategoryController(IContentCategoryRepository repo)
        {
            contentCategoryRepository = repo;
        }

        [HttpGet]
        public IActionResult Index()
        {
            return View(
                contentCategoryRepository.GetContentCategories()
            );
        }
        [HttpPost]
        [ValidateAntiForgeryToken]
        public IActionResult Edit(ContentCategory contentCategory)
        {
            if (ModelState.IsValid)
            {
                try
                {
                    contentCategoryRepository.Update(contentCategory);
                    return View("Index", contentCategoryRepository.GetContentCategories());
                }
                catch (DbUpdateConcurrencyException)
                {
                    throw;
                }
            }
            return View("Index");
        }

        [HttpGet]
        public IActionResult Delete(int? id)
        {
            if (id == null)
                return NotFound();

            ContentCategory? cc =
                contentCategoryRepository.GetContentCategoryById(id.Value);

            if (cc == null)
                return NotFound();

            return View(cc);
        }

        [HttpPost]
        [ValidateAntiForgeryToken]
        public IActionResult DeleteConfirmed(int id)
        {
            if (id == null || id == 0)
                return NotFound();

            contentCategoryRepository.Delete(id);

            return RedirectToAction(nameof(Index));
        }

        [HttpGet]
        public IActionResult Insert()
        {
            return View();
        }

        [HttpPost]
        public IActionResult Insert(ContentCategory cc)
        {

            if (ModelState.IsValid)
            {
                try
                {
                    contentCategoryRepository.Create(cc);
                    return View("Index", contentCategoryRepository.GetContentCategories());
                }
                catch (Exception)
                {
                    throw;
                }
            }
            return View("Index");
        }
    }
}
