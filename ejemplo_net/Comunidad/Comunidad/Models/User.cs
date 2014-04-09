using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Web;

namespace Comunidad.Models
{
    public class User
    {
        public int Id { get; set; }
        
        [Required]
        [Display(Name="Nombre")]
        public string Name { get; set; }

        [Required]
        [Display(Name = "Correo electrónico")]
        public string Email { get; set; }

        [Required]
        public string Password { get; set; }
    }
}