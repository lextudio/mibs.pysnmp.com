# SNMP MIB module (CISCO-IMAGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IMAGE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:02:26 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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

ciscoImageMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 25)
)
ciscoImageMIB.setRevisions(
        ("1995-08-15 00:00",
         "1995-01-16 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoImageMIBObjects_ObjectIdentity = ObjectIdentity
ciscoImageMIBObjects = _CiscoImageMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 25, 1)
)
_CiscoImageTable_Object = MibTable
ciscoImageTable = _CiscoImageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 25, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoImageTable.setStatus("current")
_CiscoImageEntry_Object = MibTableRow
ciscoImageEntry = _CiscoImageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 25, 1, 1, 1)
)
ciscoImageEntry.setIndexNames(
    (0, "CISCO-IMAGE-MIB", "ciscoImageIndex"),
)
if mibBuilder.loadTexts:
    ciscoImageEntry.setStatus("current")


class _CiscoImageIndex_Type(Integer32):
    """Custom type ciscoImageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CiscoImageIndex_Type.__name__ = "Integer32"
_CiscoImageIndex_Object = MibTableColumn
ciscoImageIndex = _CiscoImageIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 25, 1, 1, 1, 1),
    _CiscoImageIndex_Type()
)
ciscoImageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoImageIndex.setStatus("current")
_CiscoImageString_Type = DisplayString
_CiscoImageString_Object = MibTableColumn
ciscoImageString = _CiscoImageString_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 25, 1, 1, 1, 2),
    _CiscoImageString_Type()
)
ciscoImageString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoImageString.setStatus("current")
_CiscoImageMIBConformance_ObjectIdentity = ObjectIdentity
ciscoImageMIBConformance = _CiscoImageMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 25, 2)
)
_CiscoImageMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoImageMIBCompliances = _CiscoImageMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 25, 2, 1)
)
_CiscoImageMIBGroups_ObjectIdentity = ObjectIdentity
ciscoImageMIBGroups = _CiscoImageMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 25, 2, 2)
)

# Managed Objects groups

ciscoImageMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 25, 2, 2, 1)
)
ciscoImageMIBGroup.setObjects(
    ("CISCO-IMAGE-MIB", "ciscoImageString")
)
if mibBuilder.loadTexts:
    ciscoImageMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoImageMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 25, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoImageMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IMAGE-MIB",
    **{"ciscoImageMIB": ciscoImageMIB,
       "ciscoImageMIBObjects": ciscoImageMIBObjects,
       "ciscoImageTable": ciscoImageTable,
       "ciscoImageEntry": ciscoImageEntry,
       "ciscoImageIndex": ciscoImageIndex,
       "ciscoImageString": ciscoImageString,
       "ciscoImageMIBConformance": ciscoImageMIBConformance,
       "ciscoImageMIBCompliances": ciscoImageMIBCompliances,
       "ciscoImageMIBCompliance": ciscoImageMIBCompliance,
       "ciscoImageMIBGroups": ciscoImageMIBGroups,
       "ciscoImageMIBGroup": ciscoImageMIBGroup}
)
