# SNMP MIB module (CISCO-PMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-PMON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:06:48 2024
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

(CiscoInterfaceIndexList,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoInterfaceIndexList")

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

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

ciscoPmonMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 779)
)
ciscoPmonMIB.setRevisions(
        ("2012-01-03 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoPmonMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoPmonMIBNotifs = _CiscoPmonMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 779, 0)
)
_CiscoPmonMIBObjects_ObjectIdentity = ObjectIdentity
ciscoPmonMIBObjects = _CiscoPmonMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 779, 1)
)
_CiscoPmonStatsMIBObjects_ObjectIdentity = ObjectIdentity
ciscoPmonStatsMIBObjects = _CiscoPmonStatsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 779, 1, 1)
)
_CiscoPmonPortGroupStatsTable_Object = MibTable
ciscoPmonPortGroupStatsTable = _CiscoPmonPortGroupStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 779, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoPmonPortGroupStatsTable.setStatus("current")
_CiscoPmonPortGroupStatsEntry_Object = MibTableRow
ciscoPmonPortGroupStatsEntry = _CiscoPmonPortGroupStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 779, 1, 1, 1, 1)
)
ciscoPmonPortGroupStatsEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-PMON-MIB", "ciscoPmonPortGroupStatsType"),
    (0, "CISCO-PMON-MIB", "ciscoPmonPortGroupIndex"),
)
if mibBuilder.loadTexts:
    ciscoPmonPortGroupStatsEntry.setStatus("current")


class _CiscoPmonPortGroupStatsType_Type(Integer32):
    """Custom type ciscoPmonPortGroupStatsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("errPktsFromPort", 1),
          ("errPktsFromXbar", 3),
          ("errPktsToXbar", 2))
    )


_CiscoPmonPortGroupStatsType_Type.__name__ = "Integer32"
_CiscoPmonPortGroupStatsType_Object = MibTableColumn
ciscoPmonPortGroupStatsType = _CiscoPmonPortGroupStatsType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 779, 1, 1, 1, 1, 1),
    _CiscoPmonPortGroupStatsType_Type()
)
ciscoPmonPortGroupStatsType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoPmonPortGroupStatsType.setStatus("current")


class _CiscoPmonPortGroupIndex_Type(Unsigned32):
    """Custom type ciscoPmonPortGroupIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CiscoPmonPortGroupIndex_Type.__name__ = "Unsigned32"
_CiscoPmonPortGroupIndex_Object = MibTableColumn
ciscoPmonPortGroupIndex = _CiscoPmonPortGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 779, 1, 1, 1, 1, 2),
    _CiscoPmonPortGroupIndex_Type()
)
ciscoPmonPortGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoPmonPortGroupIndex.setStatus("current")
_CiscoPmonPortGroupIfIndexList_Type = CiscoInterfaceIndexList
_CiscoPmonPortGroupIfIndexList_Object = MibTableColumn
ciscoPmonPortGroupIfIndexList = _CiscoPmonPortGroupIfIndexList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 779, 1, 1, 1, 1, 3),
    _CiscoPmonPortGroupIfIndexList_Type()
)
ciscoPmonPortGroupIfIndexList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoPmonPortGroupIfIndexList.setStatus("current")
_CiscoPmonPortGroupStatsValue_Type = Counter64
_CiscoPmonPortGroupStatsValue_Object = MibTableColumn
ciscoPmonPortGroupStatsValue = _CiscoPmonPortGroupStatsValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 779, 1, 1, 1, 1, 4),
    _CiscoPmonPortGroupStatsValue_Type()
)
ciscoPmonPortGroupStatsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoPmonPortGroupStatsValue.setStatus("current")
_CiscoPmonMIBConformance_ObjectIdentity = ObjectIdentity
ciscoPmonMIBConformance = _CiscoPmonMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 779, 2)
)
_CiscoPmonMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoPmonMIBCompliances = _CiscoPmonMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 779, 2, 1)
)
_CiscoPmonMIBGroups_ObjectIdentity = ObjectIdentity
ciscoPmonMIBGroups = _CiscoPmonMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 779, 2, 2)
)

# Managed Objects groups

ciscoPmonPortGroupStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 779, 2, 2, 1)
)
ciscoPmonPortGroupStatsGroup.setObjects(
      *(("CISCO-PMON-MIB", "ciscoPmonPortGroupIfIndexList"),
        ("CISCO-PMON-MIB", "ciscoPmonPortGroupStatsValue"))
)
if mibBuilder.loadTexts:
    ciscoPmonPortGroupStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoPmonMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 779, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoPmonMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-PMON-MIB",
    **{"ciscoPmonMIB": ciscoPmonMIB,
       "ciscoPmonMIBNotifs": ciscoPmonMIBNotifs,
       "ciscoPmonMIBObjects": ciscoPmonMIBObjects,
       "ciscoPmonStatsMIBObjects": ciscoPmonStatsMIBObjects,
       "ciscoPmonPortGroupStatsTable": ciscoPmonPortGroupStatsTable,
       "ciscoPmonPortGroupStatsEntry": ciscoPmonPortGroupStatsEntry,
       "ciscoPmonPortGroupStatsType": ciscoPmonPortGroupStatsType,
       "ciscoPmonPortGroupIndex": ciscoPmonPortGroupIndex,
       "ciscoPmonPortGroupIfIndexList": ciscoPmonPortGroupIfIndexList,
       "ciscoPmonPortGroupStatsValue": ciscoPmonPortGroupStatsValue,
       "ciscoPmonMIBConformance": ciscoPmonMIBConformance,
       "ciscoPmonMIBCompliances": ciscoPmonMIBCompliances,
       "ciscoPmonMIBCompliance": ciscoPmonMIBCompliance,
       "ciscoPmonMIBGroups": ciscoPmonMIBGroups,
       "ciscoPmonPortGroupStatsGroup": ciscoPmonPortGroupStatsGroup}
)
