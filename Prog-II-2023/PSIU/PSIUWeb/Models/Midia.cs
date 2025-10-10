using System.ComponentModel.DataAnnotations;

namespace PSIUWeb.Models
{
    public enum TypeMidia
    {
        Imagem,
        Vídeo,
        Música,
        Outros
    }
    public class Midia
    {

        [Key]
        public int Id { get; set; }
        [Required(ErrorMessage = "URL Obtigatória.")]
        [Display(Name = "URL mídia")]
        public string? Url { get; set; }
        [Required(ErrorMessage = "tipo de midia requerido.")]
        [Display(Name = "Tipo de mídia")]

        //public string? TipoMidia { get; set; }

        public TypeMidia TypeMidia { get; set; }
    }
}
