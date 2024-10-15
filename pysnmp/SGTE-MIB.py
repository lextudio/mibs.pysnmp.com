# SNMP MIB module (SGTE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SGTE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:50:26 2024
# On host MacBook-Pro.local platform Darwin version 24.0.0 by user lextm
# Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint,
 ConstraintsUnion) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint",
    "ConstraintsUnion")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Sgte_ObjectIdentity = ObjectIdentity
sgte = _Sgte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13743)
)
_SEci48VP_ObjectIdentity = ObjectIdentity
sEci48VP = _SEci48VP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13743, 1)
)
_CIDENTIFICATION_ObjectIdentity = ObjectIdentity
cIDENTIFICATION = _CIDENTIFICATION_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13743, 1, 1)
)


class _INomEquipement_Type(DisplayString):
    """Custom type iNomEquipement based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )


_INomEquipement_Type.__name__ = "DisplayString"
_INomEquipement_Object = MibScalar
iNomEquipement = _INomEquipement_Object(
    (1, 3, 6, 1, 4, 1, 13743, 1, 1, 1),
    _INomEquipement_Type()
)
iNomEquipement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iNomEquipement.setStatus("optional")


class _INomConstructeur_Type(DisplayString):
    """Custom type iNomConstructeur based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )


_INomConstructeur_Type.__name__ = "DisplayString"
_INomConstructeur_Object = MibScalar
iNomConstructeur = _INomConstructeur_Object(
    (1, 3, 6, 1, 4, 1, 13743, 1, 1, 2),
    _INomConstructeur_Type()
)
iNomConstructeur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iNomConstructeur.setStatus("optional")


class _IMarqueCommerciale_Type(DisplayString):
    """Custom type iMarqueCommerciale based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )


_IMarqueCommerciale_Type.__name__ = "DisplayString"
_IMarqueCommerciale_Object = MibScalar
iMarqueCommerciale = _IMarqueCommerciale_Object(
    (1, 3, 6, 1, 4, 1, 13743, 1, 1, 3),
    _IMarqueCommerciale_Type()
)
iMarqueCommerciale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iMarqueCommerciale.setStatus("optional")


class _IVersionLogiciel_Type(DisplayString):
    """Custom type iVersionLogiciel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )


_IVersionLogiciel_Type.__name__ = "DisplayString"
_IVersionLogiciel_Object = MibScalar
iVersionLogiciel = _IVersionLogiciel_Object(
    (1, 3, 6, 1, 4, 1, 13743, 1, 1, 4),
    _IVersionLogiciel_Type()
)
iVersionLogiciel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iVersionLogiciel.setStatus("optional")


class _ICaracterisationFine_Type(DisplayString):
    """Custom type iCaracterisationFine based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )


_ICaracterisationFine_Type.__name__ = "DisplayString"
_ICaracterisationFine_Object = MibScalar
iCaracterisationFine = _ICaracterisationFine_Object(
    (1, 3, 6, 1, 4, 1, 13743, 1, 1, 5),
    _ICaracterisationFine_Type()
)
iCaracterisationFine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iCaracterisationFine.setStatus("optional")
_CMESURES_ObjectIdentity = ObjectIdentity
cMESURES = _CMESURES_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13743, 1, 2)
)


class _MTensionUtilisation_Type(DisplayString):
    """Custom type mTensionUtilisation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )


_MTensionUtilisation_Type.__name__ = "DisplayString"
_MTensionUtilisation_Object = MibScalar
mTensionUtilisation = _MTensionUtilisation_Object(
    (1, 3, 6, 1, 4, 1, 13743, 1, 2, 1),
    _MTensionUtilisation_Type()
)
mTensionUtilisation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mTensionUtilisation.setStatus("optional")


class _MTensionBatterie_Type(DisplayString):
    """Custom type mTensionBatterie based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )


_MTensionBatterie_Type.__name__ = "DisplayString"
_MTensionBatterie_Object = MibScalar
mTensionBatterie = _MTensionBatterie_Object(
    (1, 3, 6, 1, 4, 1, 13743, 1, 2, 2),
    _MTensionBatterie_Type()
)
mTensionBatterie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mTensionBatterie.setStatus("optional")


class _MCourantUtilisation_Type(DisplayString):
    """Custom type mCourantUtilisation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )


_MCourantUtilisation_Type.__name__ = "DisplayString"
_MCourantUtilisation_Object = MibScalar
mCourantUtilisation = _MCourantUtilisation_Object(
    (1, 3, 6, 1, 4, 1, 13743, 1, 2, 3),
    _MCourantUtilisation_Type()
)
mCourantUtilisation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mCourantUtilisation.setStatus("optional")


class _MCourantBatterie1A_Type(DisplayString):
    """Custom type mCourantBatterie1A based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )


_MCourantBatterie1A_Type.__name__ = "DisplayString"
_MCourantBatterie1A_Object = MibScalar
mCourantBatterie1A = _MCourantBatterie1A_Object(
    (1, 3, 6, 1, 4, 1, 13743, 1, 2, 4),
    _MCourantBatterie1A_Type()
)
mCourantBatterie1A.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mCourantBatterie1A.setStatus("optional")


class _MCourantBatterie2A_Type(DisplayString):
    """Custom type mCourantBatterie2A based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )


_MCourantBatterie2A_Type.__name__ = "DisplayString"
_MCourantBatterie2A_Object = MibScalar
mCourantBatterie2A = _MCourantBatterie2A_Object(
    (1, 3, 6, 1, 4, 1, 13743, 1, 2, 5),
    _MCourantBatterie2A_Type()
)
mCourantBatterie2A.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mCourantBatterie2A.setStatus("optional")


class _MCourantBatterie3A_Type(DisplayString):
    """Custom type mCourantBatterie3A based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )


_MCourantBatterie3A_Type.__name__ = "DisplayString"
_MCourantBatterie3A_Object = MibScalar
mCourantBatterie3A = _MCourantBatterie3A_Object(
    (1, 3, 6, 1, 4, 1, 13743, 1, 2, 6),
    _MCourantBatterie3A_Type()
)
mCourantBatterie3A.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mCourantBatterie3A.setStatus("optional")


class _MCourantBatterie1B_Type(DisplayString):
    """Custom type mCourantBatterie1B based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )


_MCourantBatterie1B_Type.__name__ = "DisplayString"
_MCourantBatterie1B_Object = MibScalar
mCourantBatterie1B = _MCourantBatterie1B_Object(
    (1, 3, 6, 1, 4, 1, 13743, 1, 2, 7),
    _MCourantBatterie1B_Type()
)
mCourantBatterie1B.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mCourantBatterie1B.setStatus("optional")


class _MCourantBatterie2B_Type(DisplayString):
    """Custom type mCourantBatterie2B based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )


_MCourantBatterie2B_Type.__name__ = "DisplayString"
_MCourantBatterie2B_Object = MibScalar
mCourantBatterie2B = _MCourantBatterie2B_Object(
    (1, 3, 6, 1, 4, 1, 13743, 1, 2, 8),
    _MCourantBatterie2B_Type()
)
mCourantBatterie2B.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mCourantBatterie2B.setStatus("optional")


class _MCourantBatterie3B_Type(DisplayString):
    """Custom type mCourantBatterie3B based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )


_MCourantBatterie3B_Type.__name__ = "DisplayString"
_MCourantBatterie3B_Object = MibScalar
mCourantBatterie3B = _MCourantBatterie3B_Object(
    (1, 3, 6, 1, 4, 1, 13743, 1, 2, 9),
    _MCourantBatterie3B_Type()
)
mCourantBatterie3B.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mCourantBatterie3B.setStatus("optional")


class _MCourantRedresseur_Type(Integer32):
    """Custom type mCourantRedresseur based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MCourantRedresseur_Type.__name__ = "Integer32"
_MCourantRedresseur_Object = MibScalar
mCourantRedresseur = _MCourantRedresseur_Object(
    (1, 3, 6, 1, 4, 1, 13743, 1, 2, 10),
    _MCourantRedresseur_Type()
)
mCourantRedresseur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mCourantRedresseur.setStatus("optional")


class _MTauxCharge_Type(DisplayString):
    """Custom type mTauxCharge based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )


_MTauxCharge_Type.__name__ = "DisplayString"
_MTauxCharge_Object = MibScalar
mTauxCharge = _MTauxCharge_Object(
    (1, 3, 6, 1, 4, 1, 13743, 1, 2, 11),
    _MTauxCharge_Type()
)
mTauxCharge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mTauxCharge.setStatus("optional")


class _MEtape_Type(DisplayString):
    """Custom type mEtape based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )


_MEtape_Type.__name__ = "DisplayString"
_MEtape_Object = MibScalar
mEtape = _MEtape_Object(
    (1, 3, 6, 1, 4, 1, 13743, 1, 2, 12),
    _MEtape_Type()
)
mEtape.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mEtape.setStatus("optional")


class _MTensionDebutTestBatt_Type(DisplayString):
    """Custom type mTensionDebutTestBatt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )


_MTensionDebutTestBatt_Type.__name__ = "DisplayString"
_MTensionDebutTestBatt_Object = MibScalar
mTensionDebutTestBatt = _MTensionDebutTestBatt_Object(
    (1, 3, 6, 1, 4, 1, 13743, 1, 2, 13),
    _MTensionDebutTestBatt_Type()
)
mTensionDebutTestBatt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mTensionDebutTestBatt.setStatus("optional")


class _MTensionFinTestBatt_Type(DisplayString):
    """Custom type mTensionFinTestBatt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )


_MTensionFinTestBatt_Type.__name__ = "DisplayString"
_MTensionFinTestBatt_Object = MibScalar
mTensionFinTestBatt = _MTensionFinTestBatt_Object(
    (1, 3, 6, 1, 4, 1, 13743, 1, 2, 14),
    _MTensionFinTestBatt_Type()
)
mTensionFinTestBatt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mTensionFinTestBatt.setStatus("optional")


class _MCourantBatterie1ADebutTestBatt_Type(Integer32):
    """Custom type mCourantBatterie1ADebutTestBatt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_MCourantBatterie1ADebutTestBatt_Type.__name__ = "Integer32"
_MCourantBatterie1ADebutTestBatt_Object = MibScalar
mCourantBatterie1ADebutTestBatt = _MCourantBatterie1ADebutTestBatt_Object(
    (1, 3, 6, 1, 4, 1, 13743, 1, 2, 15),
    _MCourantBatterie1ADebutTestBatt_Type()
)
mCourantBatterie1ADebutTestBatt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mCourantBatterie1ADebutTestBatt.setStatus("optional")


class _MCourantBatterie1AFinTestBatt_Type(Integer32):
    """Custom type mCourantBatterie1AFinTestBatt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_MCourantBatterie1AFinTestBatt_Type.__name__ = "Integer32"
_MCourantBatterie1AFinTestBatt_Object = MibScalar
mCourantBatterie1AFinTestBatt = _MCourantBatterie1AFinTestBatt_Object(
    (1, 3, 6, 1, 4, 1, 13743, 1, 2, 16),
    _MCourantBatterie1AFinTestBatt_Type()
)
mCourantBatterie1AFinTestBatt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mCourantBatterie1AFinTestBatt.setStatus("optional")


class _MCourantBatterie2ADebutTestBatt_Type(Integer32):
    """Custom type mCourantBatterie2ADebutTestBatt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_MCourantBatterie2ADebutTestBatt_Type.__name__ = "Integer32"
_MCourantBatterie2ADebutTestBatt_Object = MibScalar
mCourantBatterie2ADebutTestBatt = _MCourantBatterie2ADebutTestBatt_Object(
    (1, 3, 6, 1, 4, 1, 13743, 1, 2, 17),
    _MCourantBatterie2ADebutTestBatt_Type()
)
mCourantBatterie2ADebutTestBatt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mCourantBatterie2ADebutTestBatt.setStatus("optional")


class _MCourantBatterie2AFinTestBatt_Type(Integer32):
    """Custom type mCourantBatterie2AFinTestBatt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_MCourantBatterie2AFinTestBatt_Type.__name__ = "Integer32"
_MCourantBatterie2AFinTestBatt_Object = MibScalar
mCourantBatterie2AFinTestBatt = _MCourantBatterie2AFinTestBatt_Object(
    (1, 3, 6, 1, 4, 1, 13743, 1, 2, 18),
    _MCourantBatterie2AFinTestBatt_Type()
)
mCourantBatterie2AFinTestBatt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mCourantBatterie2AFinTestBatt.setStatus("optional")


class _MCourantBatterie3ADebutTestBatt_Type(Integer32):
    """Custom type mCourantBatterie3ADebutTestBatt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_MCourantBatterie3ADebutTestBatt_Type.__name__ = "Integer32"
_MCourantBatterie3ADebutTestBatt_Object = MibScalar
mCourantBatterie3ADebutTestBatt = _MCourantBatterie3ADebutTestBatt_Object(
    (1, 3, 6, 1, 4, 1, 13743, 1, 2, 19),
    _MCourantBatterie3ADebutTestBatt_Type()
)
mCourantBatterie3ADebutTestBatt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mCourantBatterie3ADebutTestBatt.setStatus("optional")


class _MCourantBatterie3AFinTestBatt_Type(Integer32):
    """Custom type mCourantBatterie3AFinTestBatt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_MCourantBatterie3AFinTestBatt_Type.__name__ = "Integer32"
_MCourantBatterie3AFinTestBatt_Object = MibScalar
mCourantBatterie3AFinTestBatt = _MCourantBatterie3AFinTestBatt_Object(
    (1, 3, 6, 1, 4, 1, 13743, 1, 2, 20),
    _MCourantBatterie3AFinTestBatt_Type()
)
mCourantBatterie3AFinTestBatt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mCourantBatterie3AFinTestBatt.setStatus("optional")


class _MCourantBatterie1BDebutTestBatt_Type(Integer32):
    """Custom type mCourantBatterie1BDebutTestBatt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_MCourantBatterie1BDebutTestBatt_Type.__name__ = "Integer32"
_MCourantBatterie1BDebutTestBatt_Object = MibScalar
mCourantBatterie1BDebutTestBatt = _MCourantBatterie1BDebutTestBatt_Object(
    (1, 3, 6, 1, 4, 1, 13743, 1, 2, 21),
    _MCourantBatterie1BDebutTestBatt_Type()
)
mCourantBatterie1BDebutTestBatt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mCourantBatterie1BDebutTestBatt.setStatus("optional")


class _MCourantBatterie1BFinTestBatt_Type(Integer32):
    """Custom type mCourantBatterie1BFinTestBatt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_MCourantBatterie1BFinTestBatt_Type.__name__ = "Integer32"
_MCourantBatterie1BFinTestBatt_Object = MibScalar
mCourantBatterie1BFinTestBatt = _MCourantBatterie1BFinTestBatt_Object(
    (1, 3, 6, 1, 4, 1, 13743, 1, 2, 22),
    _MCourantBatterie1BFinTestBatt_Type()
)
mCourantBatterie1BFinTestBatt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mCourantBatterie1BFinTestBatt.setStatus("optional")


class _MCourantBatterie2BDebutTestBatt_Type(Integer32):
    """Custom type mCourantBatterie2BDebutTestBatt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_MCourantBatterie2BDebutTestBatt_Type.__name__ = "Integer32"
_MCourantBatterie2BDebutTestBatt_Object = MibScalar
mCourantBatterie2BDebutTestBatt = _MCourantBatterie2BDebutTestBatt_Object(
    (1, 3, 6, 1, 4, 1, 13743, 1, 2, 23),
    _MCourantBatterie2BDebutTestBatt_Type()
)
mCourantBatterie2BDebutTestBatt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mCourantBatterie2BDebutTestBatt.setStatus("optional")


class _MCourantBatterie2BFinTestBatt_Type(Integer32):
    """Custom type mCourantBatterie2BFinTestBatt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_MCourantBatterie2BFinTestBatt_Type.__name__ = "Integer32"
_MCourantBatterie2BFinTestBatt_Object = MibScalar
mCourantBatterie2BFinTestBatt = _MCourantBatterie2BFinTestBatt_Object(
    (1, 3, 6, 1, 4, 1, 13743, 1, 2, 24),
    _MCourantBatterie2BFinTestBatt_Type()
)
mCourantBatterie2BFinTestBatt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mCourantBatterie2BFinTestBatt.setStatus("optional")


class _MCourantBatterie3BDebutTestBatt_Type(Integer32):
    """Custom type mCourantBatterie3BDebutTestBatt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_MCourantBatterie3BDebutTestBatt_Type.__name__ = "Integer32"
_MCourantBatterie3BDebutTestBatt_Object = MibScalar
mCourantBatterie3BDebutTestBatt = _MCourantBatterie3BDebutTestBatt_Object(
    (1, 3, 6, 1, 4, 1, 13743, 1, 2, 25),
    _MCourantBatterie3BDebutTestBatt_Type()
)
mCourantBatterie3BDebutTestBatt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mCourantBatterie3BDebutTestBatt.setStatus("optional")


class _MCourantBatterie3BFinTestBatt_Type(Integer32):
    """Custom type mCourantBatterie3BFinTestBatt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_MCourantBatterie3BFinTestBatt_Type.__name__ = "Integer32"
_MCourantBatterie3BFinTestBatt_Object = MibScalar
mCourantBatterie3BFinTestBatt = _MCourantBatterie3BFinTestBatt_Object(
    (1, 3, 6, 1, 4, 1, 13743, 1, 2, 26),
    _MCourantBatterie3BFinTestBatt_Type()
)
mCourantBatterie3BFinTestBatt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mCourantBatterie3BFinTestBatt.setStatus("optional")


class _MTemperature_Type(DisplayString):
    """Custom type mTemperature based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )


_MTemperature_Type.__name__ = "DisplayString"
_MTemperature_Object = MibScalar
mTemperature = _MTemperature_Object(
    (1, 3, 6, 1, 4, 1, 13743, 1, 2, 27),
    _MTemperature_Type()
)
mTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mTemperature.setStatus("optional")
_CETATS_ObjectIdentity = ObjectIdentity
cETATS = _CETATS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13743, 1, 3)
)


class _EModifHeure_Type(Integer32):
    """Custom type eModifHeure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_EModifHeure_Type.__name__ = "Integer32"
_EModifHeure_Object = MibScalar
eModifHeure = _EModifHeure_Object(
    (1, 3, 6, 1, 4, 1, 13743, 1, 3, 1),
    _EModifHeure_Type()
)
eModifHeure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModifHeure.setStatus("optional")


class _EModifParam_Type(Integer32):
    """Custom type eModifParam based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_EModifParam_Type.__name__ = "Integer32"
_EModifParam_Object = MibScalar
eModifParam = _EModifParam_Object(
    (1, 3, 6, 1, 4, 1, 13743, 1, 3, 2),
    _EModifParam_Type()
)
eModifParam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eModifParam.setStatus("optional")


class _ELiaisonJbus_Type(Integer32):
    """Custom type eLiaisonJbus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ELiaisonJbus_Type.__name__ = "Integer32"
_ELiaisonJbus_Object = MibScalar
eLiaisonJbus = _ELiaisonJbus_Object(
    (1, 3, 6, 1, 4, 1, 13743, 1, 3, 3),
    _ELiaisonJbus_Type()
)
eLiaisonJbus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eLiaisonJbus.setStatus("optional")


class _ETestEnCours_Type(Integer32):
    """Custom type eTestEnCours based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ETestEnCours_Type.__name__ = "Integer32"
_ETestEnCours_Object = MibScalar
eTestEnCours = _ETestEnCours_Object(
    (1, 3, 6, 1, 4, 1, 13743, 1, 3, 4),
    _ETestEnCours_Type()
)
eTestEnCours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eTestEnCours.setStatus("optional")


class _EUBMin_Type(Integer32):
    """Custom type eUBMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_EUBMin_Type.__name__ = "Integer32"
_EUBMin_Object = MibScalar
eUBMin = _EUBMin_Object(
    (1, 3, 6, 1, 4, 1, 13743, 1, 3, 5),
    _EUBMin_Type()
)
eUBMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eUBMin.setStatus("optional")


class _ETestNonRealise_Type(Integer32):
    """Custom type eTestNonRealise based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ETestNonRealise_Type.__name__ = "Integer32"
_ETestNonRealise_Object = MibScalar
eTestNonRealise = _ETestNonRealise_Object(
    (1, 3, 6, 1, 4, 1, 13743, 1, 3, 6),
    _ETestNonRealise_Type()
)
eTestNonRealise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eTestNonRealise.setStatus("optional")


class _EDefUnRed_Type(Integer32):
    """Custom type eDefUnRed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_EDefUnRed_Type.__name__ = "Integer32"
_EDefUnRed_Object = MibScalar
eDefUnRed = _EDefUnRed_Object(
    (1, 3, 6, 1, 4, 1, 13743, 1, 3, 7),
    _EDefUnRed_Type()
)
eDefUnRed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eDefUnRed.setStatus("optional")


class _EDefPlusRed_Type(Integer32):
    """Custom type eDefPlusRed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_EDefPlusRed_Type.__name__ = "Integer32"
_EDefPlusRed_Object = MibScalar
eDefPlusRed = _EDefPlusRed_Object(
    (1, 3, 6, 1, 4, 1, 13743, 1, 3, 8),
    _EDefPlusRed_Type()
)
eDefPlusRed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eDefPlusRed.setStatus("optional")


class _EAlimSecteur_Type(Integer32):
    """Custom type eAlimSecteur based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_EAlimSecteur_Type.__name__ = "Integer32"
_EAlimSecteur_Object = MibScalar
eAlimSecteur = _EAlimSecteur_Object(
    (1, 3, 6, 1, 4, 1, 13743, 1, 3, 9),
    _EAlimSecteur_Type()
)
eAlimSecteur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eAlimSecteur.setStatus("optional")


class _EFuseBatt_Type(Integer32):
    """Custom type eFuseBatt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_EFuseBatt_Type.__name__ = "Integer32"
_EFuseBatt_Object = MibScalar
eFuseBatt = _EFuseBatt_Object(
    (1, 3, 6, 1, 4, 1, 13743, 1, 3, 10),
    _EFuseBatt_Type()
)
eFuseBatt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eFuseBatt.setStatus("optional")


class _EFuseDep_Type(Integer32):
    """Custom type eFuseDep based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_EFuseDep_Type.__name__ = "Integer32"
_EFuseDep_Object = MibScalar
eFuseDep = _EFuseDep_Object(
    (1, 3, 6, 1, 4, 1, 13743, 1, 3, 11),
    _EFuseDep_Type()
)
eFuseDep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eFuseDep.setStatus("optional")


class _EFuseAux_Type(Integer32):
    """Custom type eFuseAux based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_EFuseAux_Type.__name__ = "Integer32"
_EFuseAux_Object = MibScalar
eFuseAux = _EFuseAux_Object(
    (1, 3, 6, 1, 4, 1, 13743, 1, 3, 12),
    _EFuseAux_Type()
)
eFuseAux.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eFuseAux.setStatus("optional")


class _EUMin_Type(Integer32):
    """Custom type eUMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_EUMin_Type.__name__ = "Integer32"
_EUMin_Object = MibScalar
eUMin = _EUMin_Object(
    (1, 3, 6, 1, 4, 1, 13743, 1, 3, 13),
    _EUMin_Type()
)
eUMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eUMin.setStatus("optional")


class _EUMax_Type(Integer32):
    """Custom type eUMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_EUMax_Type.__name__ = "Integer32"
_EUMax_Object = MibScalar
eUMax = _EUMax_Object(
    (1, 3, 6, 1, 4, 1, 13743, 1, 3, 14),
    _EUMax_Type()
)
eUMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eUMax.setStatus("optional")


class _ETauxCharge_Type(Integer32):
    """Custom type eTauxCharge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ETauxCharge_Type.__name__ = "Integer32"
_ETauxCharge_Object = MibScalar
eTauxCharge = _ETauxCharge_Object(
    (1, 3, 6, 1, 4, 1, 13743, 1, 3, 15),
    _ETauxCharge_Type()
)
eTauxCharge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eTauxCharge.setStatus("optional")


class _ETemperature_Type(Integer32):
    """Custom type eTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ETemperature_Type.__name__ = "Integer32"
_ETemperature_Object = MibScalar
eTemperature = _ETemperature_Object(
    (1, 3, 6, 1, 4, 1, 13743, 1, 3, 16),
    _ETemperature_Type()
)
eTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eTemperature.setStatus("optional")


class _EIBatt_Type(Integer32):
    """Custom type eIBatt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_EIBatt_Type.__name__ = "Integer32"
_EIBatt_Object = MibScalar
eIBatt = _EIBatt_Object(
    (1, 3, 6, 1, 4, 1, 13743, 1, 3, 17),
    _EIBatt_Type()
)
eIBatt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eIBatt.setStatus("optional")


class _EChargeI_Type(Integer32):
    """Custom type eChargeI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_EChargeI_Type.__name__ = "Integer32"
_EChargeI_Object = MibScalar
eChargeI = _EChargeI_Object(
    (1, 3, 6, 1, 4, 1, 13743, 1, 3, 18),
    _EChargeI_Type()
)
eChargeI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eChargeI.setStatus("optional")


class _EChargeU_Type(Integer32):
    """Custom type eChargeU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_EChargeU_Type.__name__ = "Integer32"
_EChargeU_Object = MibScalar
eChargeU = _EChargeU_Object(
    (1, 3, 6, 1, 4, 1, 13743, 1, 3, 19),
    _EChargeU_Type()
)
eChargeU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eChargeU.setStatus("optional")


class _EFloating_Type(Integer32):
    """Custom type eFloating based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_EFloating_Type.__name__ = "Integer32"
_EFloating_Object = MibScalar
eFloating = _EFloating_Object(
    (1, 3, 6, 1, 4, 1, 13743, 1, 3, 20),
    _EFloating_Type()
)
eFloating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eFloating.setStatus("optional")


class _EComptAH_Type(Integer32):
    """Custom type eComptAH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_EComptAH_Type.__name__ = "Integer32"
_EComptAH_Object = MibScalar
eComptAH = _EComptAH_Object(
    (1, 3, 6, 1, 4, 1, 13743, 1, 3, 21),
    _EComptAH_Type()
)
eComptAH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eComptAH.setStatus("optional")


class _ETestBattOK_Type(Integer32):
    """Custom type eTestBattOK based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ETestBattOK_Type.__name__ = "Integer32"
_ETestBattOK_Object = MibScalar
eTestBattOK = _ETestBattOK_Object(
    (1, 3, 6, 1, 4, 1, 13743, 1, 3, 22),
    _ETestBattOK_Type()
)
eTestBattOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eTestBattOK.setStatus("optional")


class _ETestBattKO_Type(Integer32):
    """Custom type eTestBattKO based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ETestBattKO_Type.__name__ = "Integer32"
_ETestBattKO_Object = MibScalar
eTestBattKO = _ETestBattKO_Object(
    (1, 3, 6, 1, 4, 1, 13743, 1, 3, 23),
    _ETestBattKO_Type()
)
eTestBattKO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eTestBattKO.setStatus("optional")


class _ETestImpossible_Type(Integer32):
    """Custom type eTestImpossible based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ETestImpossible_Type.__name__ = "Integer32"
_ETestImpossible_Object = MibScalar
eTestImpossible = _ETestImpossible_Object(
    (1, 3, 6, 1, 4, 1, 13743, 1, 3, 24),
    _ETestImpossible_Type()
)
eTestImpossible.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eTestImpossible.setStatus("optional")


class _ETestRepousse_Type(Integer32):
    """Custom type eTestRepousse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ETestRepousse_Type.__name__ = "Integer32"
_ETestRepousse_Object = MibScalar
eTestRepousse = _ETestRepousse_Object(
    (1, 3, 6, 1, 4, 1, 13743, 1, 3, 25),
    _ETestRepousse_Type()
)
eTestRepousse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eTestRepousse.setStatus("optional")


class _ETestInterrompu_Type(Integer32):
    """Custom type eTestInterrompu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ETestInterrompu_Type.__name__ = "Integer32"
_ETestInterrompu_Object = MibScalar
eTestInterrompu = _ETestInterrompu_Object(
    (1, 3, 6, 1, 4, 1, 13743, 1, 3, 26),
    _ETestInterrompu_Type()
)
eTestInterrompu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eTestInterrompu.setStatus("optional")


class _ETestMiniKO_Type(Integer32):
    """Custom type eTestMiniKO based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ETestMiniKO_Type.__name__ = "Integer32"
_ETestMiniKO_Object = MibScalar
eTestMiniKO = _ETestMiniKO_Object(
    (1, 3, 6, 1, 4, 1, 13743, 1, 3, 27),
    _ETestMiniKO_Type()
)
eTestMiniKO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eTestMiniKO.setStatus("optional")


class _EPuissTestBatt_Type(Integer32):
    """Custom type ePuissTestBatt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_EPuissTestBatt_Type.__name__ = "Integer32"
_EPuissTestBatt_Object = MibScalar
ePuissTestBatt = _EPuissTestBatt_Object(
    (1, 3, 6, 1, 4, 1, 13743, 1, 3, 28),
    _EPuissTestBatt_Type()
)
ePuissTestBatt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePuissTestBatt.setStatus("optional")


class _EDefEprom_Type(Integer32):
    """Custom type eDefEprom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_EDefEprom_Type.__name__ = "Integer32"
_EDefEprom_Object = MibScalar
eDefEprom = _EDefEprom_Object(
    (1, 3, 6, 1, 4, 1, 13743, 1, 3, 29),
    _EDefEprom_Type()
)
eDefEprom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eDefEprom.setStatus("optional")


class _EDetectionCSB_Type(Integer32):
    """Custom type eDetectionCSB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_EDetectionCSB_Type.__name__ = "Integer32"
_EDetectionCSB_Object = MibScalar
eDetectionCSB = _EDetectionCSB_Object(
    (1, 3, 6, 1, 4, 1, 13743, 1, 3, 30),
    _EDetectionCSB_Type()
)
eDetectionCSB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eDetectionCSB.setStatus("optional")


class _ERAZ_Type(Integer32):
    """Custom type eRAZ based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ERAZ_Type.__name__ = "Integer32"
_ERAZ_Object = MibScalar
eRAZ = _ERAZ_Object(
    (1, 3, 6, 1, 4, 1, 13743, 1, 3, 31),
    _ERAZ_Type()
)
eRAZ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eRAZ.setStatus("optional")
_CALARMES_ObjectIdentity = ObjectIdentity
cALARMES = _CALARMES_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13743, 1, 4)
)

# Managed Objects groups


# Notification objects

aModifHeure = NotificationType(
    (1, 3, 6, 1, 4, 1, 13743, 1, 4, 0, 1)
)
if mibBuilder.loadTexts:
    aModifHeure.setStatus(
        ""
    )

aModifParam = NotificationType(
    (1, 3, 6, 1, 4, 1, 13743, 1, 4, 0, 2)
)
if mibBuilder.loadTexts:
    aModifParam.setStatus(
        ""
    )

aLiaisonJbus = NotificationType(
    (1, 3, 6, 1, 4, 1, 13743, 1, 4, 0, 3)
)
if mibBuilder.loadTexts:
    aLiaisonJbus.setStatus(
        ""
    )

aTestEnCours = NotificationType(
    (1, 3, 6, 1, 4, 1, 13743, 1, 4, 0, 4)
)
if mibBuilder.loadTexts:
    aTestEnCours.setStatus(
        ""
    )

aUBMin = NotificationType(
    (1, 3, 6, 1, 4, 1, 13743, 1, 4, 0, 5)
)
if mibBuilder.loadTexts:
    aUBMin.setStatus(
        ""
    )

aTestNonRealise = NotificationType(
    (1, 3, 6, 1, 4, 1, 13743, 1, 4, 0, 6)
)
if mibBuilder.loadTexts:
    aTestNonRealise.setStatus(
        ""
    )

aDefUnRed = NotificationType(
    (1, 3, 6, 1, 4, 1, 13743, 1, 4, 0, 7)
)
if mibBuilder.loadTexts:
    aDefUnRed.setStatus(
        ""
    )

aDefPlusRed = NotificationType(
    (1, 3, 6, 1, 4, 1, 13743, 1, 4, 0, 8)
)
if mibBuilder.loadTexts:
    aDefPlusRed.setStatus(
        ""
    )

aAlimSecteur = NotificationType(
    (1, 3, 6, 1, 4, 1, 13743, 1, 4, 0, 9)
)
if mibBuilder.loadTexts:
    aAlimSecteur.setStatus(
        ""
    )

aFuseBatt = NotificationType(
    (1, 3, 6, 1, 4, 1, 13743, 1, 4, 0, 10)
)
if mibBuilder.loadTexts:
    aFuseBatt.setStatus(
        ""
    )

aFuseDep = NotificationType(
    (1, 3, 6, 1, 4, 1, 13743, 1, 4, 0, 11)
)
if mibBuilder.loadTexts:
    aFuseDep.setStatus(
        ""
    )

aFuseAux = NotificationType(
    (1, 3, 6, 1, 4, 1, 13743, 1, 4, 0, 12)
)
if mibBuilder.loadTexts:
    aFuseAux.setStatus(
        ""
    )

aUMin = NotificationType(
    (1, 3, 6, 1, 4, 1, 13743, 1, 4, 0, 13)
)
if mibBuilder.loadTexts:
    aUMin.setStatus(
        ""
    )

aUMax = NotificationType(
    (1, 3, 6, 1, 4, 1, 13743, 1, 4, 0, 14)
)
if mibBuilder.loadTexts:
    aUMax.setStatus(
        ""
    )

aTauxCharge = NotificationType(
    (1, 3, 6, 1, 4, 1, 13743, 1, 4, 0, 15)
)
if mibBuilder.loadTexts:
    aTauxCharge.setStatus(
        ""
    )

aTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 13743, 1, 4, 0, 16)
)
if mibBuilder.loadTexts:
    aTemperature.setStatus(
        ""
    )

aIBatt = NotificationType(
    (1, 3, 6, 1, 4, 1, 13743, 1, 4, 0, 17)
)
if mibBuilder.loadTexts:
    aIBatt.setStatus(
        ""
    )

aChargeI = NotificationType(
    (1, 3, 6, 1, 4, 1, 13743, 1, 4, 0, 18)
)
if mibBuilder.loadTexts:
    aChargeI.setStatus(
        ""
    )

aChargeU = NotificationType(
    (1, 3, 6, 1, 4, 1, 13743, 1, 4, 0, 19)
)
if mibBuilder.loadTexts:
    aChargeU.setStatus(
        ""
    )

aFloating = NotificationType(
    (1, 3, 6, 1, 4, 1, 13743, 1, 4, 0, 20)
)
if mibBuilder.loadTexts:
    aFloating.setStatus(
        ""
    )

aComptAH = NotificationType(
    (1, 3, 6, 1, 4, 1, 13743, 1, 4, 0, 21)
)
if mibBuilder.loadTexts:
    aComptAH.setStatus(
        ""
    )

aTestBattOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 13743, 1, 4, 0, 22)
)
if mibBuilder.loadTexts:
    aTestBattOK.setStatus(
        ""
    )

aTestBattKO = NotificationType(
    (1, 3, 6, 1, 4, 1, 13743, 1, 4, 0, 23)
)
if mibBuilder.loadTexts:
    aTestBattKO.setStatus(
        ""
    )

aTestImpossible = NotificationType(
    (1, 3, 6, 1, 4, 1, 13743, 1, 4, 0, 24)
)
if mibBuilder.loadTexts:
    aTestImpossible.setStatus(
        ""
    )

aTestRepousse = NotificationType(
    (1, 3, 6, 1, 4, 1, 13743, 1, 4, 0, 25)
)
if mibBuilder.loadTexts:
    aTestRepousse.setStatus(
        ""
    )

aTestInterrompu = NotificationType(
    (1, 3, 6, 1, 4, 1, 13743, 1, 4, 0, 26)
)
if mibBuilder.loadTexts:
    aTestInterrompu.setStatus(
        ""
    )

aTestMiniKO = NotificationType(
    (1, 3, 6, 1, 4, 1, 13743, 1, 4, 0, 27)
)
if mibBuilder.loadTexts:
    aTestMiniKO.setStatus(
        ""
    )

aPuissTestBatt = NotificationType(
    (1, 3, 6, 1, 4, 1, 13743, 1, 4, 0, 28)
)
if mibBuilder.loadTexts:
    aPuissTestBatt.setStatus(
        ""
    )

aDefEprom = NotificationType(
    (1, 3, 6, 1, 4, 1, 13743, 1, 4, 0, 29)
)
if mibBuilder.loadTexts:
    aDefEprom.setStatus(
        ""
    )

aDetectionCSB = NotificationType(
    (1, 3, 6, 1, 4, 1, 13743, 1, 4, 0, 30)
)
if mibBuilder.loadTexts:
    aDetectionCSB.setStatus(
        ""
    )

aRAZ = NotificationType(
    (1, 3, 6, 1, 4, 1, 13743, 1, 4, 0, 31)
)
if mibBuilder.loadTexts:
    aRAZ.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SGTE-MIB",
    **{"sgte": sgte,
       "sEci48VP": sEci48VP,
       "cIDENTIFICATION": cIDENTIFICATION,
       "iNomEquipement": iNomEquipement,
       "iNomConstructeur": iNomConstructeur,
       "iMarqueCommerciale": iMarqueCommerciale,
       "iVersionLogiciel": iVersionLogiciel,
       "iCaracterisationFine": iCaracterisationFine,
       "cMESURES": cMESURES,
       "mTensionUtilisation": mTensionUtilisation,
       "mTensionBatterie": mTensionBatterie,
       "mCourantUtilisation": mCourantUtilisation,
       "mCourantBatterie1A": mCourantBatterie1A,
       "mCourantBatterie2A": mCourantBatterie2A,
       "mCourantBatterie3A": mCourantBatterie3A,
       "mCourantBatterie1B": mCourantBatterie1B,
       "mCourantBatterie2B": mCourantBatterie2B,
       "mCourantBatterie3B": mCourantBatterie3B,
       "mCourantRedresseur": mCourantRedresseur,
       "mTauxCharge": mTauxCharge,
       "mEtape": mEtape,
       "mTensionDebutTestBatt": mTensionDebutTestBatt,
       "mTensionFinTestBatt": mTensionFinTestBatt,
       "mCourantBatterie1ADebutTestBatt": mCourantBatterie1ADebutTestBatt,
       "mCourantBatterie1AFinTestBatt": mCourantBatterie1AFinTestBatt,
       "mCourantBatterie2ADebutTestBatt": mCourantBatterie2ADebutTestBatt,
       "mCourantBatterie2AFinTestBatt": mCourantBatterie2AFinTestBatt,
       "mCourantBatterie3ADebutTestBatt": mCourantBatterie3ADebutTestBatt,
       "mCourantBatterie3AFinTestBatt": mCourantBatterie3AFinTestBatt,
       "mCourantBatterie1BDebutTestBatt": mCourantBatterie1BDebutTestBatt,
       "mCourantBatterie1BFinTestBatt": mCourantBatterie1BFinTestBatt,
       "mCourantBatterie2BDebutTestBatt": mCourantBatterie2BDebutTestBatt,
       "mCourantBatterie2BFinTestBatt": mCourantBatterie2BFinTestBatt,
       "mCourantBatterie3BDebutTestBatt": mCourantBatterie3BDebutTestBatt,
       "mCourantBatterie3BFinTestBatt": mCourantBatterie3BFinTestBatt,
       "mTemperature": mTemperature,
       "cETATS": cETATS,
       "eModifHeure": eModifHeure,
       "eModifParam": eModifParam,
       "eLiaisonJbus": eLiaisonJbus,
       "eTestEnCours": eTestEnCours,
       "eUBMin": eUBMin,
       "eTestNonRealise": eTestNonRealise,
       "eDefUnRed": eDefUnRed,
       "eDefPlusRed": eDefPlusRed,
       "eAlimSecteur": eAlimSecteur,
       "eFuseBatt": eFuseBatt,
       "eFuseDep": eFuseDep,
       "eFuseAux": eFuseAux,
       "eUMin": eUMin,
       "eUMax": eUMax,
       "eTauxCharge": eTauxCharge,
       "eTemperature": eTemperature,
       "eIBatt": eIBatt,
       "eChargeI": eChargeI,
       "eChargeU": eChargeU,
       "eFloating": eFloating,
       "eComptAH": eComptAH,
       "eTestBattOK": eTestBattOK,
       "eTestBattKO": eTestBattKO,
       "eTestImpossible": eTestImpossible,
       "eTestRepousse": eTestRepousse,
       "eTestInterrompu": eTestInterrompu,
       "eTestMiniKO": eTestMiniKO,
       "ePuissTestBatt": ePuissTestBatt,
       "eDefEprom": eDefEprom,
       "eDetectionCSB": eDetectionCSB,
       "eRAZ": eRAZ,
       "cALARMES": cALARMES,
       "aModifHeure": aModifHeure,
       "aModifParam": aModifParam,
       "aLiaisonJbus": aLiaisonJbus,
       "aTestEnCours": aTestEnCours,
       "aUBMin": aUBMin,
       "aTestNonRealise": aTestNonRealise,
       "aDefUnRed": aDefUnRed,
       "aDefPlusRed": aDefPlusRed,
       "aAlimSecteur": aAlimSecteur,
       "aFuseBatt": aFuseBatt,
       "aFuseDep": aFuseDep,
       "aFuseAux": aFuseAux,
       "aUMin": aUMin,
       "aUMax": aUMax,
       "aTauxCharge": aTauxCharge,
       "aTemperature": aTemperature,
       "aIBatt": aIBatt,
       "aChargeI": aChargeI,
       "aChargeU": aChargeU,
       "aFloating": aFloating,
       "aComptAH": aComptAH,
       "aTestBattOK": aTestBattOK,
       "aTestBattKO": aTestBattKO,
       "aTestImpossible": aTestImpossible,
       "aTestRepousse": aTestRepousse,
       "aTestInterrompu": aTestInterrompu,
       "aTestMiniKO": aTestMiniKO,
       "aPuissTestBatt": aPuissTestBatt,
       "aDefEprom": aDefEprom,
       "aDetectionCSB": aDetectionCSB,
       "aRAZ": aRAZ}
)
