# SNMP MIB module (ENTERASYS-ENCR-8021X-REKEYING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENTERASYS-ENCR-8021X-REKEYING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:38:49 2024
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

(etsysModules,) = mibBuilder.importSymbols(
    "ENTERASYS-MIB-NAMES",
    "etsysModules")

(dot1xPaePortNumber,) = mibBuilder.importSymbols(
    "IEEE8021-PAE-MIB",
    "dot1xPaePortNumber")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 TimeTicks,
 Unsigned32,
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
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

etsysEncr8021xRekeyingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 20)
)
etsysEncr8021xRekeyingMIB.setRevisions(
        ("2002-03-14 20:49",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EtsysEncrDot1xRekeyingObjects_ObjectIdentity = ObjectIdentity
etsysEncrDot1xRekeyingObjects = _EtsysEncrDot1xRekeyingObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 20, 1)
)
_EtsysEncrDot1xRekeyBaseBranch_ObjectIdentity = ObjectIdentity
etsysEncrDot1xRekeyBaseBranch = _EtsysEncrDot1xRekeyBaseBranch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 20, 1, 1)
)
_EtsysEncrDot1xRekeyConfigTable_Object = MibTable
etsysEncrDot1xRekeyConfigTable = _EtsysEncrDot1xRekeyConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 20, 1, 1, 1)
)
if mibBuilder.loadTexts:
    etsysEncrDot1xRekeyConfigTable.setStatus("current")
_EtsysEncrDot1xRekeyConfigEntry_Object = MibTableRow
etsysEncrDot1xRekeyConfigEntry = _EtsysEncrDot1xRekeyConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 20, 1, 1, 1, 1)
)
etsysEncrDot1xRekeyConfigEntry.setIndexNames(
    (0, "IEEE8021-PAE-MIB", "dot1xPaePortNumber"),
)
if mibBuilder.loadTexts:
    etsysEncrDot1xRekeyConfigEntry.setStatus("current")


class _EtsysEncrDot1xRekeyEnabled_Type(OctetString):
    """Custom type etsysEncrDot1xRekeyEnabled based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EtsysEncrDot1xRekeyEnabled_Type.__name__ = "OctetString"
_EtsysEncrDot1xRekeyEnabled_Object = MibTableColumn
etsysEncrDot1xRekeyEnabled = _EtsysEncrDot1xRekeyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 20, 1, 1, 1, 1, 1),
    _EtsysEncrDot1xRekeyEnabled_Type()
)
etsysEncrDot1xRekeyEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysEncrDot1xRekeyEnabled.setStatus("current")


class _EtsysEncrDot1xRekeyPeriod_Type(OctetString):
    """Custom type etsysEncrDot1xRekeyPeriod based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EtsysEncrDot1xRekeyPeriod_Type.__name__ = "OctetString"
_EtsysEncrDot1xRekeyPeriod_Object = MibTableColumn
etsysEncrDot1xRekeyPeriod = _EtsysEncrDot1xRekeyPeriod_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 20, 1, 1, 1, 1, 2),
    _EtsysEncrDot1xRekeyPeriod_Type()
)
etsysEncrDot1xRekeyPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysEncrDot1xRekeyPeriod.setStatus("current")


class _EtsysEncrDot1xRekeyLength_Type(OctetString):
    """Custom type etsysEncrDot1xRekeyLength based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EtsysEncrDot1xRekeyLength_Type.__name__ = "OctetString"
_EtsysEncrDot1xRekeyLength_Object = MibTableColumn
etsysEncrDot1xRekeyLength = _EtsysEncrDot1xRekeyLength_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 20, 1, 1, 1, 1, 3),
    _EtsysEncrDot1xRekeyLength_Type()
)
etsysEncrDot1xRekeyLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysEncrDot1xRekeyLength.setStatus("current")


class _EtsysEncrDot1xRekeyAsymmetric_Type(OctetString):
    """Custom type etsysEncrDot1xRekeyAsymmetric based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EtsysEncrDot1xRekeyAsymmetric_Type.__name__ = "OctetString"
_EtsysEncrDot1xRekeyAsymmetric_Object = MibTableColumn
etsysEncrDot1xRekeyAsymmetric = _EtsysEncrDot1xRekeyAsymmetric_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 20, 1, 1, 1, 1, 4),
    _EtsysEncrDot1xRekeyAsymmetric_Type()
)
etsysEncrDot1xRekeyAsymmetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysEncrDot1xRekeyAsymmetric.setStatus("current")
_EtsysEncrDot1xRekeyingConformance_ObjectIdentity = ObjectIdentity
etsysEncrDot1xRekeyingConformance = _EtsysEncrDot1xRekeyingConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 20, 2)
)
_EtsysEncrDot1xRekeyingGroups_ObjectIdentity = ObjectIdentity
etsysEncrDot1xRekeyingGroups = _EtsysEncrDot1xRekeyingGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 20, 2, 1)
)
_EtsysEncrDot1xRekeyingCompliances_ObjectIdentity = ObjectIdentity
etsysEncrDot1xRekeyingCompliances = _EtsysEncrDot1xRekeyingCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 20, 2, 2)
)

# Managed Objects groups

etsysEncrDot1xRekeyingBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 20, 2, 1, 1)
)
etsysEncrDot1xRekeyingBaseGroup.setObjects(
      *(("ENTERASYS-ENCR-8021X-REKEYING-MIB", "etsysEncrDot1xRekeyPeriod"),
        ("ENTERASYS-ENCR-8021X-REKEYING-MIB", "etsysEncrDot1xRekeyEnabled"),
        ("ENTERASYS-ENCR-8021X-REKEYING-MIB", "etsysEncrDot1xRekeyLength"),
        ("ENTERASYS-ENCR-8021X-REKEYING-MIB", "etsysEncrDot1xRekeyAsymmetric"))
)
if mibBuilder.loadTexts:
    etsysEncrDot1xRekeyingBaseGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etsysEncrDot1xRekeyingCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 20, 2, 2, 1)
)
if mibBuilder.loadTexts:
    etsysEncrDot1xRekeyingCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-ENCR-8021X-REKEYING-MIB",
    **{"etsysEncr8021xRekeyingMIB": etsysEncr8021xRekeyingMIB,
       "etsysEncrDot1xRekeyingObjects": etsysEncrDot1xRekeyingObjects,
       "etsysEncrDot1xRekeyBaseBranch": etsysEncrDot1xRekeyBaseBranch,
       "etsysEncrDot1xRekeyConfigTable": etsysEncrDot1xRekeyConfigTable,
       "etsysEncrDot1xRekeyConfigEntry": etsysEncrDot1xRekeyConfigEntry,
       "etsysEncrDot1xRekeyEnabled": etsysEncrDot1xRekeyEnabled,
       "etsysEncrDot1xRekeyPeriod": etsysEncrDot1xRekeyPeriod,
       "etsysEncrDot1xRekeyLength": etsysEncrDot1xRekeyLength,
       "etsysEncrDot1xRekeyAsymmetric": etsysEncrDot1xRekeyAsymmetric,
       "etsysEncrDot1xRekeyingConformance": etsysEncrDot1xRekeyingConformance,
       "etsysEncrDot1xRekeyingGroups": etsysEncrDot1xRekeyingGroups,
       "etsysEncrDot1xRekeyingBaseGroup": etsysEncrDot1xRekeyingBaseGroup,
       "etsysEncrDot1xRekeyingCompliances": etsysEncrDot1xRekeyingCompliances,
       "etsysEncrDot1xRekeyingCompliance": etsysEncrDot1xRekeyingCompliance}
)
