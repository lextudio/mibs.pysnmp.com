# SNMP MIB module (CISCO-WAN-ATM-PREF-ROUTE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-WAN-ATM-PREF-ROUTE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:12:51 2024
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

(PnniNodeId,
 PnniPortId) = mibBuilder.importSymbols(
    "PNNI-MIB",
    "PnniNodeId",
    "PnniPortId")

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


# MODULE-IDENTITY

ciscoWanATMPrefRouteMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99996)
)
ciscoWanATMPrefRouteMIB.setRevisions(
        ("2002-06-25 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RouteId(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoWanATMPrefRouteMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoWanATMPrefRouteMIBNotifs = _CiscoWanATMPrefRouteMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99996, 0)
)
_CiscoWanATMPrefRouteMIBObjects_ObjectIdentity = ObjectIdentity
ciscoWanATMPrefRouteMIBObjects = _CiscoWanATMPrefRouteMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99996, 1)
)
_CwaPrefRouteConfTable_Object = MibTable
cwaPrefRouteConfTable = _CwaPrefRouteConfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99996, 1, 1)
)
if mibBuilder.loadTexts:
    cwaPrefRouteConfTable.setStatus("current")
_CwaPrefRouteConfEntry_Object = MibTableRow
cwaPrefRouteConfEntry = _CwaPrefRouteConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99996, 1, 1, 1)
)
cwaPrefRouteConfEntry.setIndexNames(
    (0, "CISCO-WAN-ATM-PREF-ROUTE-MIB", "cwaPrefRouteId"),
)
if mibBuilder.loadTexts:
    cwaPrefRouteConfEntry.setStatus("current")
_CwaPrefRouteId_Type = RouteId
_CwaPrefRouteId_Object = MibTableColumn
cwaPrefRouteId = _CwaPrefRouteId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99996, 1, 1, 1, 1),
    _CwaPrefRouteId_Type()
)
cwaPrefRouteId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwaPrefRouteId.setStatus("current")


class _CwaPrefRouteNwElemCount_Type(Unsigned32):
    """Custom type cwaPrefRouteNwElemCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_CwaPrefRouteNwElemCount_Type.__name__ = "Unsigned32"
_CwaPrefRouteNwElemCount_Object = MibTableColumn
cwaPrefRouteNwElemCount = _CwaPrefRouteNwElemCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99996, 1, 1, 1, 2),
    _CwaPrefRouteNwElemCount_Type()
)
cwaPrefRouteNwElemCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwaPrefRouteNwElemCount.setStatus("current")
_CwaPrefRouteRowStatus_Type = RowStatus
_CwaPrefRouteRowStatus_Object = MibTableColumn
cwaPrefRouteRowStatus = _CwaPrefRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99996, 1, 1, 1, 3),
    _CwaPrefRouteRowStatus_Type()
)
cwaPrefRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwaPrefRouteRowStatus.setStatus("current")
_CwaPrefRouteNwElemTable_Object = MibTable
cwaPrefRouteNwElemTable = _CwaPrefRouteNwElemTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99996, 1, 2)
)
if mibBuilder.loadTexts:
    cwaPrefRouteNwElemTable.setStatus("current")
_CwaPrefRouteNwElemEntry_Object = MibTableRow
cwaPrefRouteNwElemEntry = _CwaPrefRouteNwElemEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99996, 1, 2, 1)
)
cwaPrefRouteNwElemEntry.setIndexNames(
    (0, "CISCO-WAN-ATM-PREF-ROUTE-MIB", "cwaPrefRouteId"),
    (0, "CISCO-WAN-ATM-PREF-ROUTE-MIB", "cwaPrefRouteNwElemPos"),
)
if mibBuilder.loadTexts:
    cwaPrefRouteNwElemEntry.setStatus("current")


class _CwaPrefRouteNwElemPos_Type(Unsigned32):
    """Custom type cwaPrefRouteNwElemPos based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_CwaPrefRouteNwElemPos_Type.__name__ = "Unsigned32"
_CwaPrefRouteNwElemPos_Object = MibTableColumn
cwaPrefRouteNwElemPos = _CwaPrefRouteNwElemPos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99996, 1, 2, 1, 1),
    _CwaPrefRouteNwElemPos_Type()
)
cwaPrefRouteNwElemPos.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwaPrefRouteNwElemPos.setStatus("current")
_CwaPrefRouteNwElemNodeId_Type = PnniNodeId
_CwaPrefRouteNwElemNodeId_Object = MibTableColumn
cwaPrefRouteNwElemNodeId = _CwaPrefRouteNwElemNodeId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99996, 1, 2, 1, 2),
    _CwaPrefRouteNwElemNodeId_Type()
)
cwaPrefRouteNwElemNodeId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwaPrefRouteNwElemNodeId.setStatus("current")
_CwaPrefRouteNwElemPortId_Type = PnniPortId
_CwaPrefRouteNwElemPortId_Object = MibTableColumn
cwaPrefRouteNwElemPortId = _CwaPrefRouteNwElemPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99996, 1, 2, 1, 3),
    _CwaPrefRouteNwElemPortId_Type()
)
cwaPrefRouteNwElemPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwaPrefRouteNwElemPortId.setStatus("current")
_CwaPrefRouteNwElemRowStatus_Type = RowStatus
_CwaPrefRouteNwElemRowStatus_Object = MibTableColumn
cwaPrefRouteNwElemRowStatus = _CwaPrefRouteNwElemRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99996, 1, 2, 1, 4),
    _CwaPrefRouteNwElemRowStatus_Type()
)
cwaPrefRouteNwElemRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cwaPrefRouteNwElemRowStatus.setStatus("current")
_CwaPrefRouteConformance_ObjectIdentity = ObjectIdentity
cwaPrefRouteConformance = _CwaPrefRouteConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99996, 2)
)
_CwaPrefRouteCompliances_ObjectIdentity = ObjectIdentity
cwaPrefRouteCompliances = _CwaPrefRouteCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99996, 2, 1)
)
_CwaPrefMIBGroups_ObjectIdentity = ObjectIdentity
cwaPrefMIBGroups = _CwaPrefMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99996, 2, 2)
)

# Managed Objects groups

cwaPrefRouteMIBGroups = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 99996, 2, 2, 1)
)
cwaPrefRouteMIBGroups.setObjects(
      *(("CISCO-WAN-ATM-PREF-ROUTE-MIB", "cwaPrefRouteNwElemCount"),
        ("CISCO-WAN-ATM-PREF-ROUTE-MIB", "cwaPrefRouteRowStatus"),
        ("CISCO-WAN-ATM-PREF-ROUTE-MIB", "cwaPrefRouteNwElemNodeId"),
        ("CISCO-WAN-ATM-PREF-ROUTE-MIB", "cwaPrefRouteNwElemPortId"),
        ("CISCO-WAN-ATM-PREF-ROUTE-MIB", "cwaPrefRouteNwElemRowStatus"))
)
if mibBuilder.loadTexts:
    cwaPrefRouteMIBGroups.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cwaPrefMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 99996, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cwaPrefMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WAN-ATM-PREF-ROUTE-MIB",
    **{"RouteId": RouteId,
       "ciscoWanATMPrefRouteMIB": ciscoWanATMPrefRouteMIB,
       "ciscoWanATMPrefRouteMIBNotifs": ciscoWanATMPrefRouteMIBNotifs,
       "ciscoWanATMPrefRouteMIBObjects": ciscoWanATMPrefRouteMIBObjects,
       "cwaPrefRouteConfTable": cwaPrefRouteConfTable,
       "cwaPrefRouteConfEntry": cwaPrefRouteConfEntry,
       "cwaPrefRouteId": cwaPrefRouteId,
       "cwaPrefRouteNwElemCount": cwaPrefRouteNwElemCount,
       "cwaPrefRouteRowStatus": cwaPrefRouteRowStatus,
       "cwaPrefRouteNwElemTable": cwaPrefRouteNwElemTable,
       "cwaPrefRouteNwElemEntry": cwaPrefRouteNwElemEntry,
       "cwaPrefRouteNwElemPos": cwaPrefRouteNwElemPos,
       "cwaPrefRouteNwElemNodeId": cwaPrefRouteNwElemNodeId,
       "cwaPrefRouteNwElemPortId": cwaPrefRouteNwElemPortId,
       "cwaPrefRouteNwElemRowStatus": cwaPrefRouteNwElemRowStatus,
       "cwaPrefRouteConformance": cwaPrefRouteConformance,
       "cwaPrefRouteCompliances": cwaPrefRouteCompliances,
       "cwaPrefMIBCompliance": cwaPrefMIBCompliance,
       "cwaPrefMIBGroups": cwaPrefMIBGroups,
       "cwaPrefRouteMIBGroups": cwaPrefRouteMIBGroups}
)
