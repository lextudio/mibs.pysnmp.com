# SNMP MIB module (ENTERASYS-8021X-REKEYING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENTERASYS-8021X-REKEYING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:38:40 2024
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

etsys8021xRekeyingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 17)
)
etsys8021xRekeyingMIB.setRevisions(
        ("2004-07-14 15:07",
         "2002-03-07 20:06")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EtsysDot1xRekeyingObjects_ObjectIdentity = ObjectIdentity
etsysDot1xRekeyingObjects = _EtsysDot1xRekeyingObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 17, 1)
)
_EtsysDot1xRekeyBaseBranch_ObjectIdentity = ObjectIdentity
etsysDot1xRekeyBaseBranch = _EtsysDot1xRekeyBaseBranch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 17, 1, 1)
)
_EtsysDot1xRekeyConfigTable_Object = MibTable
etsysDot1xRekeyConfigTable = _EtsysDot1xRekeyConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 17, 1, 1, 1)
)
if mibBuilder.loadTexts:
    etsysDot1xRekeyConfigTable.setStatus("current")
_EtsysDot1xRekeyConfigEntry_Object = MibTableRow
etsysDot1xRekeyConfigEntry = _EtsysDot1xRekeyConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 17, 1, 1, 1, 1)
)
etsysDot1xRekeyConfigEntry.setIndexNames(
    (0, "IEEE8021-PAE-MIB", "dot1xPaePortNumber"),
)
if mibBuilder.loadTexts:
    etsysDot1xRekeyConfigEntry.setStatus("current")


class _EtsysDot1xRekeyEnabled_Type(TruthValue):
    """Custom type etsysDot1xRekeyEnabled based on TruthValue"""


_EtsysDot1xRekeyEnabled_Object = MibTableColumn
etsysDot1xRekeyEnabled = _EtsysDot1xRekeyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 17, 1, 1, 1, 1, 1),
    _EtsysDot1xRekeyEnabled_Type()
)
etsysDot1xRekeyEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysDot1xRekeyEnabled.setStatus("current")


class _EtsysDot1xRekeyPeriod_Type(Unsigned32):
    """Custom type etsysDot1xRekeyPeriod based on Unsigned32"""
    defaultValue = 1800


_EtsysDot1xRekeyPeriod_Object = MibTableColumn
etsysDot1xRekeyPeriod = _EtsysDot1xRekeyPeriod_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 17, 1, 1, 1, 1, 2),
    _EtsysDot1xRekeyPeriod_Type()
)
etsysDot1xRekeyPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysDot1xRekeyPeriod.setStatus("current")


class _EtsysDot1xRekeyLength_Type(Integer32):
    """Custom type etsysDot1xRekeyLength based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("keylen128", 2),
          ("keylen40", 1))
    )


_EtsysDot1xRekeyLength_Type.__name__ = "Integer32"
_EtsysDot1xRekeyLength_Object = MibTableColumn
etsysDot1xRekeyLength = _EtsysDot1xRekeyLength_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 17, 1, 1, 1, 1, 3),
    _EtsysDot1xRekeyLength_Type()
)
etsysDot1xRekeyLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysDot1xRekeyLength.setStatus("current")


class _EtsysDot1xRekeyAsymmetric_Type(TruthValue):
    """Custom type etsysDot1xRekeyAsymmetric based on TruthValue"""


_EtsysDot1xRekeyAsymmetric_Object = MibTableColumn
etsysDot1xRekeyAsymmetric = _EtsysDot1xRekeyAsymmetric_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 17, 1, 1, 1, 1, 4),
    _EtsysDot1xRekeyAsymmetric_Type()
)
etsysDot1xRekeyAsymmetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysDot1xRekeyAsymmetric.setStatus("current")


class _EtsysDot1xRekeyPairwise_Type(TruthValue):
    """Custom type etsysDot1xRekeyPairwise based on TruthValue"""


_EtsysDot1xRekeyPairwise_Object = MibTableColumn
etsysDot1xRekeyPairwise = _EtsysDot1xRekeyPairwise_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 17, 1, 1, 1, 1, 5),
    _EtsysDot1xRekeyPairwise_Type()
)
etsysDot1xRekeyPairwise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysDot1xRekeyPairwise.setStatus("current")
_EtsysDot1xRekeyingConformance_ObjectIdentity = ObjectIdentity
etsysDot1xRekeyingConformance = _EtsysDot1xRekeyingConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 17, 2)
)
_EtsysDot1xRekeyingGroups_ObjectIdentity = ObjectIdentity
etsysDot1xRekeyingGroups = _EtsysDot1xRekeyingGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 17, 2, 1)
)
_EtsysDot1xRekeyingCompliances_ObjectIdentity = ObjectIdentity
etsysDot1xRekeyingCompliances = _EtsysDot1xRekeyingCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 17, 2, 2)
)

# Managed Objects groups

etsysDot1xRekeyingBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 17, 2, 1, 1)
)
etsysDot1xRekeyingBaseGroup.setObjects(
      *(("ENTERASYS-8021X-REKEYING-MIB", "etsysDot1xRekeyPeriod"),
        ("ENTERASYS-8021X-REKEYING-MIB", "etsysDot1xRekeyEnabled"),
        ("ENTERASYS-8021X-REKEYING-MIB", "etsysDot1xRekeyLength"),
        ("ENTERASYS-8021X-REKEYING-MIB", "etsysDot1xRekeyAsymmetric"))
)
if mibBuilder.loadTexts:
    etsysDot1xRekeyingBaseGroup.setStatus("current")

etsysDot1xRekeyingPairwiseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 17, 2, 1, 2)
)
etsysDot1xRekeyingPairwiseGroup.setObjects(
    ("ENTERASYS-8021X-REKEYING-MIB", "etsysDot1xRekeyPairwise")
)
if mibBuilder.loadTexts:
    etsysDot1xRekeyingPairwiseGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etsysDot1xRekeyingCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 17, 2, 2, 1)
)
if mibBuilder.loadTexts:
    etsysDot1xRekeyingCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-8021X-REKEYING-MIB",
    **{"etsys8021xRekeyingMIB": etsys8021xRekeyingMIB,
       "etsysDot1xRekeyingObjects": etsysDot1xRekeyingObjects,
       "etsysDot1xRekeyBaseBranch": etsysDot1xRekeyBaseBranch,
       "etsysDot1xRekeyConfigTable": etsysDot1xRekeyConfigTable,
       "etsysDot1xRekeyConfigEntry": etsysDot1xRekeyConfigEntry,
       "etsysDot1xRekeyEnabled": etsysDot1xRekeyEnabled,
       "etsysDot1xRekeyPeriod": etsysDot1xRekeyPeriod,
       "etsysDot1xRekeyLength": etsysDot1xRekeyLength,
       "etsysDot1xRekeyAsymmetric": etsysDot1xRekeyAsymmetric,
       "etsysDot1xRekeyPairwise": etsysDot1xRekeyPairwise,
       "etsysDot1xRekeyingConformance": etsysDot1xRekeyingConformance,
       "etsysDot1xRekeyingGroups": etsysDot1xRekeyingGroups,
       "etsysDot1xRekeyingBaseGroup": etsysDot1xRekeyingBaseGroup,
       "etsysDot1xRekeyingPairwiseGroup": etsysDot1xRekeyingPairwiseGroup,
       "etsysDot1xRekeyingCompliances": etsysDot1xRekeyingCompliances,
       "etsysDot1xRekeyingCompliance": etsysDot1xRekeyingCompliance}
)
