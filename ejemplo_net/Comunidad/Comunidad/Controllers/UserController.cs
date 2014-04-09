using System;
using System.Collections.Generic;
using System.Data;
using System.Data.Entity;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using Comunidad.Models;
using Servicios;

namespace Comunidad.Controllers
{   
    public class UserController : Controller
    {
        private ComunidadContext context = new ComunidadContext();

        //
        // GET: /User/

        public ViewResult Index()
        {
            // al resultado del método get, lo convierto a una lista de tipo User (definida en Models).
            // sería el equivalente a

            //List<RepositorioClases.User> usuarios = UserService.Get(null);
            //List<User> usuariosModels = new List<User>();

            //foreach (RepositorioClases.User u in usuarios)
            //{
            //    User usuario = new User();

            //    usuario.Email = u.Email;
            //    usuario.Id = u.Id;
            //    usuario.Name = u.Name;
            //    usuario.Password = u.Password;

            //    usuariosModels.Add(usuario);
            //}           

            return View(UserService.Get(null).Select(u => new User() {
                Email = u.Email,
                Id = u.Id,
                Name = u.Name,
                Password = u.Password
            }).ToList());
        }

        //
        // GET: /User/Details/5

        public ViewResult Details(int id)
        {
            User user = UserService.Get(id).Select(u => new User()
            {
                Email = u.Email,
                Id = u.Id,
                Name = u.Name,
                Password = u.Password
            }).FirstOrDefault();

            return View(user);
        }

        //
        // GET: /User/Create

        public ActionResult Create()
        {
            return View();
        } 

        //
        // POST: /User/Create

        [HttpPost]
        public ActionResult Create(User user)
        {
            if (ModelState.IsValid)
            {
                UserService.Create(new RepositorioClases.User()
                {
                    Email = user.Email,
                    Name = user.Name,
                    Password = user.Password
                });
                return RedirectToAction("Index");  
            }

            return View(user);
        }
        
        //
        // GET: /User/Edit/5
 
        public ActionResult Edit(int id)
        {
            User user = UserService.Get(id).Select(u => new User()
            {
                Email = u.Email,
                Id = u.Id,
                Name = u.Name,
                Password = u.Password
            }).FirstOrDefault();

            return View(user);
        }

        //
        // POST: /User/Edit/5

        [HttpPost]
        public ActionResult Edit(User user)
        {
            if (ModelState.IsValid)
            {
                UserService.Edit(new RepositorioClases.User()
                {
                    Email = user.Email,
                    Id = user.Id,
                    Name = user.Name,
                    Password = user.Password
                });
                
                return RedirectToAction("Index");
            }
            return View(user);
        }

        //
        // GET: /User/Delete/5
 
        public ActionResult Delete(int id)
        {
            User user = UserService.Get(id).Select(u => new User()
            {
                Email = u.Email,
                Id = u.Id,
                Name = u.Name,
                Password = u.Password
            }).FirstOrDefault();

            return View(user);
        }

        //
        // POST: /User/Delete/5

        [HttpPost, ActionName("Delete")]
        public ActionResult DeleteConfirmed(int id)
        {
            UserService.Delete(new RepositorioClases.User()
            {
                Id = id,
                DeletedDate = DateTime.Now
            });

            return RedirectToAction("Index");
        }
    }
}