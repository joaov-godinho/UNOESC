using Microsoft.AspNetCore.Identity;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace PjJoaoVitorGodinho.Models
{
    public class Psicologo : IdentityUser
    {
        [Key]
        public int Id { get; set; }

        [Required(ErrorMessage = "Nome requerido.")]
        [Display(Name = "Nome")]
        public string? Name { get; set; }

        [Required(ErrorMessage = "CRMV requerido.")]
        [Display(Name = "CRMV")]
        public string? Crmv { get; set; }

        [Required(ErrorMessage = "Liberação requirida.")]
        [Display(Name = "Liberação")]
        public Boolean? Liberate { get; set; }

        [ForeignKey("User")]
        public string? UserId { get; set; }
        public AppUser? User { get; set; }

    }
}