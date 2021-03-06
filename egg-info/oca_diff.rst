+--------------------------------------+------------------+-----------------+------------------------------------------------------------------------------------+
| Description / Descrizione            | Odoo Italia      | OCA             | Notes / Note                                                                       |
.. $if branch in '6.1'
+--------------------------------------+------------------+-----------------+------------------------------------------------------------------------------------+
| Coverage                             | |Codecov Status| | | OCA Codecov | |                                                                                    |
.. $fi
.. $if branch in '7.0'
+--------------------------------------+------------------+-----------------+------------------------------------------------------------------------------------+
| Test compatibilità OCA e Odoo        | |no_check|       | |check|         | `Errore import decimal precision <https://github.com/OCA/OCB/issues/629>`__        |
.. $fi
.. $if branch not in '12.0'
+--------------------------------------+------------------+-----------------+------------------------------------------------------------------------------------+
| Gestione evoluta anagrafiche         | |check|          | |no_check|      | `l10n_it_base <https://github.com/zeroincombenze/l10n-italy/tree/8.0/l10n_it_base> |
.. $fi
+--------------------------------------+------------------+-----------------+------------------------------------------------------------------------------------+
| Piano dei conti evoluto              | |check|          | |no_check|      |                                                                                    |
+--------------------------------------+------------------+-----------------+------------------------------------------------------------------------------------+
| Codici IVA completi                  | |check|          | |no_check|      |                                                                                    |
.. $if branch in '7.0' '8.0'
+--------------------------------------+------------------+-----------------+------------------------------------------------------------------------------------+
| Dichiaritivi fiscali                 | 2018             | 2017            |                                                                                    |
+--------------------------------------+------------------+-----------------+------------------------------------------------------------------------------------+
| Controllo date                       | Per anno fiscale | No anno fiscale | Versione OCA non permette l'accavallamento numerazioni a inizio anno               |
+--------------------------------------+------------------+-----------------+------------------------------------------------------------------------------------+
| Controllo date fatture emesse        | |check|          | |no_check|      |                                                                                    |
+--------------------------------------+------------------+-----------------+------------------------------------------------------------------------------------+
| FatturaPA                            | v1.2             | v1.1            |                                                                                    |
.. $fi
.. $if branch not in '12.0'
+--------------------------------------+------------------+-----------------+------------------------------------------------------------------------------------+
| Validazione Codice Fiscale           | |check|          | |no_check|      |                                                                                    |
.. $fi
+--------------------------------------+------------------+-----------------+------------------------------------------------------------------------------------+
