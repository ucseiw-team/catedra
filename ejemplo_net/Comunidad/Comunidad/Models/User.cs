using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Web;
using Servicios;

namespace Comunidad.Models
{
    public class User
    {
        public int Id { get; set; }

        [Required]
        [Display(Name = "Nombre")]
        public string Name { get; set; }

        [Required]
        [Display(Name = "Correo electrónico")]
        public string Email { get; set; }

        [Required]
        public string Password { get; set; }

        [Required]
        [Display(Name = "Rol")]
        public int IdRol { get; set; }

        public List<Rol> Roles
        {
            get
            {
                return UserService.GetRole(null).Select(r => new Rol()
                {
                    Description = r.Description,
                    Id = r.Id
                }).ToList();
            }

            set { }
        }
    }

    public class Rol
    {
        public int Id { get; set; }

        public string Description { get; set; }
    }
}