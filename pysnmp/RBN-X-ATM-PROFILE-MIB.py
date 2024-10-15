# SNMP MIB module (RBN-X-ATM-PROFILE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RBN-X-ATM-PROFILE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:45:29 2024
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

(atmTrafficDescrParamEntry,) = mibBuilder.importSymbols(
    "ATM-MIB",
    "atmTrafficDescrParamEntry")

(rbnExperiment,) = mibBuilder.importSymbols(
    "RBN-SMI",
    "rbnExperiment")

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

rbnXAtmProfileMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 3, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RbnXAtmProfileMIBObjects_ObjectIdentity = ObjectIdentity
rbnXAtmProfileMIBObjects = _RbnXAtmProfileMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 3, 2, 1)
)
_RbnXAtmProfileTable_Object = MibTable
rbnXAtmProfileTable = _RbnXAtmProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rbnXAtmProfileTable.setStatus("current")
_RbnXAtmProfileEntry_Object = MibTableRow
rbnXAtmProfileEntry = _RbnXAtmProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 3, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    rbnXAtmProfileEntry.setStatus("current")


class _RbnXAtmServiceCategory_Type(Integer32):
    """Custom type rbnXAtmServiceCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("abr", 5),
          ("cbr", 2),
          ("nrtVbr", 4),
          ("other", 1),
          ("rtVbr", 3),
          ("ubr", 6))
    )


_RbnXAtmServiceCategory_Type.__name__ = "Integer32"
_RbnXAtmServiceCategory_Object = MibTableColumn
rbnXAtmServiceCategory = _RbnXAtmServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 2352, 3, 2, 1, 1, 1, 1),
    _RbnXAtmServiceCategory_Type()
)
rbnXAtmServiceCategory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnXAtmServiceCategory.setStatus("current")
_RbnXAtmProfileMIBConformance_ObjectIdentity = ObjectIdentity
rbnXAtmProfileMIBConformance = _RbnXAtmProfileMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 3, 2, 2)
)
_RbnXAtmProfileMIBGroups_ObjectIdentity = ObjectIdentity
rbnXAtmProfileMIBGroups = _RbnXAtmProfileMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 3, 2, 2, 1)
)
_RbnXAtmProfileMIBCompliances_ObjectIdentity = ObjectIdentity
rbnXAtmProfileMIBCompliances = _RbnXAtmProfileMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 3, 2, 2, 2)
)
atmTrafficDescrParamEntry.registerAugmentions(
    ("RBN-X-ATM-PROFILE-MIB",
     "rbnXAtmProfileEntry")
)
rbnXAtmProfileEntry.setIndexNames(*atmTrafficDescrParamEntry.getIndexNames())

# Managed Objects groups

rbnXAtmProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 3, 2, 2, 1, 1)
)
rbnXAtmProfileGroup.setObjects(
    ("RBN-X-ATM-PROFILE-MIB", "rbnXAtmServiceCategory")
)
if mibBuilder.loadTexts:
    rbnXAtmProfileGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rbnXAtmProfileMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 3, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    rbnXAtmProfileMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBN-X-ATM-PROFILE-MIB",
    **{"rbnXAtmProfileMIB": rbnXAtmProfileMIB,
       "rbnXAtmProfileMIBObjects": rbnXAtmProfileMIBObjects,
       "rbnXAtmProfileTable": rbnXAtmProfileTable,
       "rbnXAtmProfileEntry": rbnXAtmProfileEntry,
       "rbnXAtmServiceCategory": rbnXAtmServiceCategory,
       "rbnXAtmProfileMIBConformance": rbnXAtmProfileMIBConformance,
       "rbnXAtmProfileMIBGroups": rbnXAtmProfileMIBGroups,
       "rbnXAtmProfileGroup": rbnXAtmProfileGroup,
       "rbnXAtmProfileMIBCompliances": rbnXAtmProfileMIBCompliances,
       "rbnXAtmProfileMIBCompliance": rbnXAtmProfileMIBCompliance}
)
