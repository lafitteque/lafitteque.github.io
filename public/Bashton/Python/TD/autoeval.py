from contextlib import contextmanager
import pprint
import sys
from typing import Any, NamedTuple
import inspect
from collections import abc
from unittest import result

_LISTS = (abc.Sequence,)
_DICTS = (abc.Mapping,)
_STRS = (str, bytes)

def _compare(a, b):
    if type(a) != type(b):
        return False
    if isinstance(a, Exception) and isinstance(b, Exception):
        return a.__class__ == b.__class__ and str(a) == str(b)
    if isinstance(a, _STRS) and isinstance(b, _STRS):
        return a == b
    elif isinstance(a, _DICTS) and isinstance(b, _DICTS):
        return all(k in b and _compare(a[k], b[k]) for k in a)
    elif isinstance(a, _LISTS) and isinstance(b, _LISTS):
        return all(_compare(x, y) for x, y in zip(a, b))
    elif isinstance(a, float) and isinstance(b, float):
        return abs(a - b) < 1e-9
    else:
        return a == b


class TestResult(NamedTuple):
    success: bool
    type: str
    message: str
    item: Any
    arguments: Any
    target: Any
    result: Any
    diff: Any

    def __str__(self):
        arguments = pprint.pformat(self.arguments)
        target = pprint.pformat(self.target)
        result = pprint.pformat(self.result)
        message = f"{self.type} : {self.message}. {self.item} {arguments} : attendu = {target}, résultat = {result}"
        if self.success:
            return "\033[92m✅ {}\033[00m".format(message)
        return "\033[91m❌ {}\033[00m".format(message)

class Validation:
    def __init__(self, total: int = 0, **kwargs):
        self._passed = []
        self._failed = []
        self.total: int = total
        self.kwargs = kwargs
        self.last_exception = None

    
    @contextmanager
    def exec(self):
        self.last_exception = None
        try:
            yield
        except Exception as e:
            self.last_exception = e

    def failed(self, type, message="", item="", arguments="", target="", result="", diff=""):
        self._failed.append(TestResult(False, type=type, message=message, item=item, 
                                       arguments=arguments, target=target, result=result, diff=diff))
    
    def success(self, type, message="", item="", arguments="", target="", result="", diff=""):
        self._passed.append(TestResult(True, type=type, message=message, item=item, 
                                       arguments=arguments, target=target, result=result, diff=diff))

    def finalize(self):
        for f in self._failed:
            print(f, file=sys.stderr, flush=True)
        for p in self._passed:
            print(p, file=sys.stdout, flush=True)
        return len(self._failed) == 0
    
        

class ValidateVariables(Validation):
    def __init__(self, names_and_values: dict[str, Any], **kwargs):
        """
        Validate the given variables
        :param names_and_values: dict of variable names and their values
        """
        super().__init__(len(names_and_values), **kwargs)
        self.names_and_values = names_and_values
        self.kwargs = kwargs

    def __call__(self) -> Any:
        """
        Validate the given variables
        :return: None
        """
        g = inspect.stack()[1].frame.f_globals
        for name, value in self.names_and_values.items():
            if name in g:
                if not _compare(value, g[name]):
                    self.failed(type="variable",
                                message="Valeur différente",
                                item= name,
                                target= value,
                                result= g[name])
                else:
                    self.success("variable", 
                                 message="Valeur correspondante",
                                 item=name,
                                 result=value,
                                 target=g[name])
            else:
                self.failed(type="variable", message="Variable manquante", item=name)
        return self.finalize()

class ValidateFunction(Validation):
    def __init__(self, 
                 func_name: str,
                 test_values,
                 target_values=None,
                 valid_function=None,
                 check_signature=False,
                 **kwargs):
        """
        Validate the given function
        """
        super().__init__(len(test_values), **kwargs)
        self.func_name = func_name
        self.test_values = test_values
        self.target_values = target_values
        self.valid_function = valid_function
        self.check_signature = check_signature
        self.kwargs = kwargs

    def __call__(self) -> bool:
        """
        Validate the given function
        :return: None
        """
        g = inspect.stack()[1].frame.f_globals
        if self.func_name not in g:
            return False

        func = g[self.func_name]
        # Check the respective function signatures
        if self.check_signature:
            if not inspect.signature(func) == inspect.signature(self.valid_function):
                self.failed(
                    type="signature",
                     message="Les arguments de la fonction ne sont pas corrects",
                      item= self.func_name,
                       arguments="",
                        target=inspect.signature(self.valid_function),
                        result= inspect.signature(func))
        
        if self.valid_function is None:
            for res, tgt in zip(self.test_values, self.target_values):
                with self.exec():
                    result = func(*res)
                if not _compare(result, tgt):
                    self.failed("function_result", message="Résultats différents lors de l'appel de la fonction", 
                                item=self.func_name, arguments=res,
                                target=tgt, result=result)
                else:
                    self.success("result", message="Résultats identiques", item=self.func_name, arguments=res,
                                 target=tgt, result=result)
        else:
            for test_values in self.test_values:
                target_result = result_result = None
                with self.exec():
                    target_result = self.valid_function(*test_values)
                target_exception = self.last_exception
                with self.exec():
                    result_result = func(*test_values)
                result_exception = self.last_exception
                if not _compare(target_exception, result_exception):
                    self.failed(type="function_exception", message="Exceptions différentes lors de l'exécution", 
                                item=self.func_name, arguments=test_values, 
                                target=target_exception, result=result_exception)
                else:
                    if target_exception is not None:
                        self.success("function_exception", message="Exceptions identiques", item=self.func_name, arguments=test_values,
                                    target=target_exception, result=result_exception)
                    if not _compare(target_result, result_result):
                        self.failed("function_result", message="Résultats différents lors de l'appel de la fonction", 
                                    item=self.func_name, arguments=test_values,
                                    target=target_result, result=result_result)
                    else:
                        self.success("result", message="Résultats identiques", item=self.func_name, arguments=test_values,
                                    target=target_result, result=result_result)
        return self.finalize()
                 

class ValidateFunctionPretty(ValidateFunction):
    pass

class ValidateClassContent(Validation):
    """Permet de tester le contenu d'un objet en fonction des pamateres passés a l'instanciation.
    """
    def __init__(self, class_name, parameters_init, attributs, methods):
        """
        parameters
        ----------
        class_name : str
            le nom de la classe a tester
            
        parameters_init : list de tuple
            Les parametres a passer lors des instanciations. 
            Chaque élément de la liste est un tuple contenant les parametres a transmettre.
            Si pas de paramètre, mettre un tuple vide.
            
        attributs : dict
            le nom de chaque attribut (str) est une clé du dictionnaire. Les valeur sont des listes contenant
            les valeurs successives prisent par l'attribut lors des instaciations successives.
            
        methods : list
            La liste des noms des méthodes a vérifier.
        """
        super().__init__()
        self.class_name = class_name
        self.attributs = attributs
        self.methods = methods
        self.parametres = parameters_init
        

    def __call__(self):
        for i in range(len(self.parametres)):
            try:
                import __main__
                # instancie l'objet
                _class = getattr(__main__, self.class_name)                
                instance = _class(*self.parametres[i])
                
                # test du contenu de la classe
                # les bons attributs et leur valeur
                for a in self.attributs:
                    if hasattr(instance, a):
                        self.success("attribut", message="Attribut déclaré", item=a)
                        att_a = getattr(instance, a)
                        if att_a is self.attributs[a][i]:
                            self.success("attribut_value", message="Valeur correcte", item=a, result=att_a, target=self.attributs[a][i])
                        else:
                            self.failed("attribut_value", message="Valeur incorrecte", item=a, result=att_a, target=self.attributs[a][i])
                    else:
                        self.failed("attribut", message="Attribut manquant", item=a)
                        flag_error = True

                for m in self.methods:
                    if hasattr(instance, m):
                        self.success("method", message="Méthode déclarée", item=m)
                    else:
                        self.failed("method", message="Méthode manquante", item=m)
                        
            except AssertionError:
                self.failed("exception", message="Erreur lors de l'instanciation", item=self.class_name)
        return self.finalize()
    
class ValidateMethod(Validation):
    """Permet de tester une classe.
    """
    def __init__(self, class_name=None, parameters_init=None, instance=None, method_name=None, 
                 test_values=None, return_values=None, method_verif=None, return_values_verif=None):
        """
        parameters
        ----------
        class_name : str
            le nom de la classe a tester. Valeur par défaut None. Si fourni l'objet sera instancié à partir de cette classe.
            
        parameters_init : tuple
            Les parametres a passer lors de l'instanciation. 
            
        instance : str
            nom d'une instance de la classe a tester, par défaut None. Si défini, c'est cette instance qui sera testée.
            
        method_name : str
            le nom de la méthode a tester
            
        test_values : list de tuple
            Chaque tuple contient les parametres de la méthode (method_name) a passer lors du test. 
            Un tuple vide attendu si aucun parametre.
            
        return_values : list
            Chaque élément de la list est la valeur de retour attendu du test correspondant.
            
        method_verif : str
            Le nom d'une méthode ou d'un attribut a tester en plus. Si c'est une méthode, elle ne doit pas demander
            d'argument. Permet de tester l'état de l'objetaprès exécution de method_name. Optionnel, par defaut None.
            
        return_values_verif : list
            La liste des valeur de retour attendues lors de l'exécution de method_verif.
        """
        
        super().__init__()
        self.class_name = class_name
        self.parameters_init = parameters_init
        self.instance = instance
        self.method_name = method_name
        self.test_values = test_values
        self.return_values = return_values
        self.return_values_verif = return_values_verif
        self.method_verif_name = method_verif

            
    def __call__(self):
        # instancie un objet de la classe ou récupère directement une instance
        import __main__
        if self.instance is None:
            if self.class_name is not None and self.parameters_init is not None:
                _class = getattr(__main__, self.class_name)
                inst = _class(*self.parameters_init)                
            else:
                self.failed("exception", message="Il manque des arguments ...")
                return self.finalize()
        else:
            inst = getattr(__main__, self.instance)    
            
        verif = False
        if self.method_verif_name is not None and self.return_values_verif is not None:
            self.method_verif = getattr(inst, self.method_verif_name)
            verif = True            
           
        # essaye de récupérer la méthode a tester
        try:
            self.method = getattr(inst, self.method_name)
        except:
            self.failed("exception", message=f"{self.method_name} ne semble pas exister dans votre classe.")
            return self.finalize()
        
        # début des tests
        flag_error = False
        for i in range(len(self.test_values)):
            # test des valeurs de retour de la méthode
            value_returned = self.method(*self.test_values[i])
            if value_returned == self.return_values[i]:
                self.success("method", message=f"la méthode {self.method.__name__}{self.test_values[i]} renvoi bien {value_returned}.")
            else:
                self.failed("method", message=f"pour des parametres d'entrée {self.test_values[i]}, la méthode renvoi {value_returned} au lieu de {self.return_values[i]} !")
            
            if verif:
                # vérification de l'état de lobjet par une autre méthode ou un attribut: method_verif
                if callable(self.method_verif):
                    value_verif = self.method_verif()
                else:
                    #il s'agit d'un attribut
                    value_verif = self.method_verif
                if value_verif == self.return_values_verif[i]:
                    self.success("method_verif", message=f"la méthode {self.method_verif.__name__} renvoi bien {value_verif}")
                else:
                    self.failed("method_verif", message=f"la méthode de vérification renvoi {value_verif} au lieu de {self.return_values_verif[i]} !")
        return self.finalize()