from django.db import models

class IdAuteur(models.Model):
	id_auteur = models.AutoField('Id_Auteur', primary_key=True)

	def __str__(self):
		return '%d' % (self.id_auteur)

class Auteur(models.Model):
	id_auteur = models.ForeignKey(IdAuteur)
	nom = models.CharField(max_length=50, primary_key=True)
	nb_texte_poste = models.IntegerField()
	
	def __str__(self):
		return '%s' % (self.nom)

class Texte(models.Model):
	id_texte = models.AutoField('Id_Texte', primary_key=True)
	auteur = models.ForeignKey(Auteur)
	nom_texte = models.CharField(max_length=50)
	date_publication = models.DateTimeField()
	
	def __str__(self):
		return '%s ecrit par %s' % (self.nom_texte, self.auteur)

class Statistiques(models.Model):
	id_statistiques = models.AutoField('Id_Stats', primary_key=True)
	id_texte = models.ForeignKey(Texte)
	date = models.DateTimeField()
	nb_lecteurs = models.IntegerField()
	nb_connexions = models.IntegerField()
	
	def __str__(self):
		return '%d' % (self.id_statistiques)
		
class Lecteur(models.Model):
	id_session = models.AutoField('Id_session', primary_key=True)
	id_texte_lu = models.ForeignKey(Texte)
	
	def __str__(self):
		return '%d' % (self.id_session)

class DonneesBrutes(models.Model):
	id_session = models.ForeignKey(Lecteur)
	id_texte_lu = models.ForeignKey(Texte)
	date = models.DateTimeField()
	position_haut = models.IntegerField()
	hauteur_affichee = models.IntegerField()
	hauteur_texte = models.IntegerField()
	pertinent = models.BooleanField(default='False')
	
	def __str__(self):
		return 'id_session %d  id_texte %d' % (self.id_session, self.id_texte_lu)
	
	class Meta:
		ordering = ['date','id_texte_lu','id_session']
		
class DonneesStatistiques(models.Model):
	id_session = models.ForeignKey(Lecteur)
	id_texte_lu = models.ForeignKey(Texte)
	date = models.DateTimeField()
	position_fin = models.FloatField()
	
	def __str__(self):
		return 'id_session %d id_texte %d date %Y-%m-%d %H:%M:%S position_fin %f' % (self.id_session, self.id_texte_lu, self.date, self.position_fin)

	class Meta:
		ordering = ['id_texte_lu','date']