using Microsoft.AspNetCore.Identity;
using Microsoft.AspNetCore.Mvc;
using System.ComponentModel.DataAnnotations;


namespace PjJoaoVitorGodinho.Models
{
    public enum Gender { Feminino, Masculino, Outros }
    public class AppUser : IdentityUser
    {
        [Required(ErrorMessage = "Nome requerido.")]
        [Display(Name = "Nome completo")]
        public string? Name { get; set; }

        [Required(ErrorMessage = "Data requerida.")]
        [Display(Name = "Data de nascimento")]
        public DateTime Birthdate { get; set; }

        [Required(ErrorMessage = "Gênero requerido.")]
        [Display(Name = "Gênero")]
        public Gender Gender { get; set; }

        public DateTime CreationDate { get; set; }

    }
}