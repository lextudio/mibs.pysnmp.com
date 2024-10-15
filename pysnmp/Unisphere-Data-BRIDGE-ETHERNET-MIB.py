# SNMP MIB module (Unisphere-Data-BRIDGE-ETHERNET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-BRIDGE-ETHERNET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:10:23 2024
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

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(usDataMibs,) = mibBuilder.importSymbols(
    "Unisphere-Data-MIBs",
    "usDataMibs")

(UsdNextIfIndex,) = mibBuilder.importSymbols(
    "Unisphere-Data-TC",
    "UsdNextIfIndex")


# MODULE-IDENTITY

usdBridgeEthernetMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 31)
)
usdBridgeEthernetMIB.setRevisions(
        ("2000-09-26 14:43",
         "2000-03-27 23:45",
         "1999-12-10 18:30")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UsdBridgedEthernetObjects_ObjectIdentity = ObjectIdentity
usdBridgedEthernetObjects = _UsdBridgedEthernetObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 31, 1)
)
_UsdBridgedEthernetIfLayer_ObjectIdentity = ObjectIdentity
usdBridgedEthernetIfLayer = _UsdBridgedEthernetIfLayer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 31, 1, 1)
)
_UsdBridgedEthernetNextIfIndex_Type = UsdNextIfIndex
_UsdBridgedEthernetNextIfIndex_Object = MibScalar
usdBridgedEthernetNextIfIndex = _UsdBridgedEthernetNextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 31, 1, 1, 1),
    _UsdBridgedEthernetNextIfIndex_Type()
)
usdBridgedEthernetNextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBridgedEthernetNextIfIndex.setStatus("current")
_UsdBridgedEthernetIfTable_Object = MibTable
usdBridgedEthernetIfTable = _UsdBridgedEthernetIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 31, 1, 1, 2)
)
if mibBuilder.loadTexts:
    usdBridgedEthernetIfTable.setStatus("current")
_UsdBridgedEthernetIfEntry_Object = MibTableRow
usdBridgedEthernetIfEntry = _UsdBridgedEthernetIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 31, 1, 1, 2, 1)
)
usdBridgedEthernetIfEntry.setIndexNames(
    (0, "Unisphere-Data-BRIDGE-ETHERNET-MIB", "usdBridgedEthernetIfIfIndex"),
)
if mibBuilder.loadTexts:
    usdBridgedEthernetIfEntry.setStatus("current")
_UsdBridgedEthernetIfIfIndex_Type = InterfaceIndex
_UsdBridgedEthernetIfIfIndex_Object = MibTableColumn
usdBridgedEthernetIfIfIndex = _UsdBridgedEthernetIfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 31, 1, 1, 2, 1, 1),
    _UsdBridgedEthernetIfIfIndex_Type()
)
usdBridgedEthernetIfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBridgedEthernetIfIfIndex.setStatus("current")


class _UsdBridgedEthernetProxyArp_Type(Integer32):
    """Custom type usdBridgedEthernetProxyArp based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enableRestricted", 1),
          ("enableUnrestricted", 2))
    )


_UsdBridgedEthernetProxyArp_Type.__name__ = "Integer32"
_UsdBridgedEthernetProxyArp_Object = MibTableColumn
usdBridgedEthernetProxyArp = _UsdBridgedEthernetProxyArp_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 31, 1, 1, 2, 1, 2),
    _UsdBridgedEthernetProxyArp_Type()
)
usdBridgedEthernetProxyArp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBridgedEthernetProxyArp.setStatus("obsolete")
_UsdBridgedEthernetIfLowerIfIndex_Type = InterfaceIndexOrZero
_UsdBridgedEthernetIfLowerIfIndex_Object = MibTableColumn
usdBridgedEthernetIfLowerIfIndex = _UsdBridgedEthernetIfLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 31, 1, 1, 2, 1, 3),
    _UsdBridgedEthernetIfLowerIfIndex_Type()
)
usdBridgedEthernetIfLowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBridgedEthernetIfLowerIfIndex.setStatus("current")
_UsdBridgedEthernetIfRowStatus_Type = RowStatus
_UsdBridgedEthernetIfRowStatus_Object = MibTableColumn
usdBridgedEthernetIfRowStatus = _UsdBridgedEthernetIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 31, 1, 1, 2, 1, 4),
    _UsdBridgedEthernetIfRowStatus_Type()
)
usdBridgedEthernetIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBridgedEthernetIfRowStatus.setStatus("current")
_UsdBridgeEthernetConformance_ObjectIdentity = ObjectIdentity
usdBridgeEthernetConformance = _UsdBridgeEthernetConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 31, 4)
)
_UsdBridgeEthernetCompliances_ObjectIdentity = ObjectIdentity
usdBridgeEthernetCompliances = _UsdBridgeEthernetCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 31, 4, 1)
)
_UsdBridgeEthernetGroups_ObjectIdentity = ObjectIdentity
usdBridgeEthernetGroups = _UsdBridgeEthernetGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 31, 4, 2)
)

# Managed Objects groups

usdBridgedEthernetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 31, 4, 2, 1)
)
usdBridgedEthernetGroup.setObjects(
      *(("Unisphere-Data-BRIDGE-ETHERNET-MIB", "usdBridgedEthernetNextIfIndex"),
        ("Unisphere-Data-BRIDGE-ETHERNET-MIB", "usdBridgedEthernetIfIfIndex"),
        ("Unisphere-Data-BRIDGE-ETHERNET-MIB", "usdBridgedEthernetProxyArp"),
        ("Unisphere-Data-BRIDGE-ETHERNET-MIB", "usdBridgedEthernetIfLowerIfIndex"),
        ("Unisphere-Data-BRIDGE-ETHERNET-MIB", "usdBridgedEthernetIfRowStatus"))
)
if mibBuilder.loadTexts:
    usdBridgedEthernetGroup.setStatus("obsolete")

usdBridgedEthernetGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 31, 4, 2, 2)
)
usdBridgedEthernetGroup2.setObjects(
      *(("Unisphere-Data-BRIDGE-ETHERNET-MIB", "usdBridgedEthernetNextIfIndex"),
        ("Unisphere-Data-BRIDGE-ETHERNET-MIB", "usdBridgedEthernetIfIfIndex"),
        ("Unisphere-Data-BRIDGE-ETHERNET-MIB", "usdBridgedEthernetIfLowerIfIndex"),
        ("Unisphere-Data-BRIDGE-ETHERNET-MIB", "usdBridgedEthernetIfRowStatus"))
)
if mibBuilder.loadTexts:
    usdBridgedEthernetGroup2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

usdBridgedEthernetCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 31, 4, 1, 1)
)
if mibBuilder.loadTexts:
    usdBridgedEthernetCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-BRIDGE-ETHERNET-MIB",
    **{"usdBridgeEthernetMIB": usdBridgeEthernetMIB,
       "usdBridgedEthernetObjects": usdBridgedEthernetObjects,
       "usdBridgedEthernetIfLayer": usdBridgedEthernetIfLayer,
       "usdBridgedEthernetNextIfIndex": usdBridgedEthernetNextIfIndex,
       "usdBridgedEthernetIfTable": usdBridgedEthernetIfTable,
       "usdBridgedEthernetIfEntry": usdBridgedEthernetIfEntry,
       "usdBridgedEthernetIfIfIndex": usdBridgedEthernetIfIfIndex,
       "usdBridgedEthernetProxyArp": usdBridgedEthernetProxyArp,
       "usdBridgedEthernetIfLowerIfIndex": usdBridgedEthernetIfLowerIfIndex,
       "usdBridgedEthernetIfRowStatus": usdBridgedEthernetIfRowStatus,
       "usdBridgeEthernetConformance": usdBridgeEthernetConformance,
       "usdBridgeEthernetCompliances": usdBridgeEthernetCompliances,
       "usdBridgedEthernetCompliance": usdBridgedEthernetCompliance,
       "usdBridgeEthernetGroups": usdBridgeEthernetGroups,
       "usdBridgedEthernetGroup": usdBridgedEthernetGroup,
       "usdBridgedEthernetGroup2": usdBridgedEthernetGroup2}
)
