using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using PSIUWeb.Data.Interface;
using PSIUWeb.Models;

namespace PSIUWeb.Controllers
{
    public class PsicoController : Controller
    {
        private IPsicoRepository psicoRepository;

        public PsicoController(
            IPsicoRepository _psicoRepo
        )
        {
            psicoRepository = _psicoRepo;
        }

        [HttpGet]
        public IActionResult Index()
        {
            return View(
                psicoRepository.GetPsicos()
            );
        }

        [HttpGet]
        public IActionResult Edit(int? id)
        {
            if (id <= 0 || id == null)
                return NotFound();

            Psico? psico =
                psicoRepository.GetPsicoById(id.Value);

            if (psico == null)
                return NotFound();

            return View(psico);

        }

        [HttpPost]
        [ValidateAntiForgeryToken]
        public IActionResult Edit(Psico psico)
        {
            if (ModelState.IsValid)
            {
                try
                {
                    psicoRepository.Update(psico);
                    return View("Index", psicoRepository.GetPsicos());
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

            Psico? psico =
                psicoRepository.GetPsicoById(id.Value);

            if (psico == null)
                return NotFound();

            return View(psico);
        }

        [HttpPost]
        [ValidateAntiForgeryToken]
        public IActionResult DeleteConfirmed(int id)
        {
            if (id == null || id == 0)
                return NotFound();

            psicoRepository.Delete(id);

            return RedirectToAction(nameof(Index));
        }

        [HttpGet]
        public IActionResult Insert()
        {
            return View();
        }

        [HttpPost]
        public IActionResult Insert(Psico psico)
        {

            if (ModelState.IsValid)
            {
                try
                {
                    psicoRepository.Create(psico);
                    return View("Index", psicoRepository.GetPsicos());
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
