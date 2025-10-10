using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using PSIUWeb.Data.Interface;
using PSIUWeb.Models;

namespace PSIUWeb.Controllers
{
    public class ContentController : Controller
    {
        private IContentRepository contentRepository;

        public ContentController(IContentRepository repo)
        {
            contentRepository = repo;
        }

        [HttpGet]
        public IActionResult Index()
        {
            return View(
                contentRepository.GetContents()
            );
        }
        [HttpPost]
        [ValidateAntiForgeryToken]
        public IActionResult Edit(Content content)
        {
            if (ModelState.IsValid)
            {
                try
                {
                    contentRepository.Update(content);
                    return View("Index", contentRepository.GetContents());
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

            Content? c =
                contentRepository.GetContentById(id.Value);

            if (c == null)
                return NotFound();

            return View(c);
        }

        [HttpPost]
        [ValidateAntiForgeryToken]
        public IActionResult DeleteConfirmed(int id)
        {
            if (id == null || id == 0)
                return NotFound();

            contentRepository.Delete(id);

            return RedirectToAction(nameof(Index));
        }

        [HttpGet]
        public IActionResult Insert()
        {
            return View();
        }

        [HttpPost]
        public IActionResult Insert(Content c)
        {

            if (ModelState.IsValid)
            {
                try
                {
                    contentRepository.Create(c);
                    return View("Index", contentRepository.GetContents());
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
