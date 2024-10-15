# SNMP MIB module (NETSCREEN-RIPv2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETSCREEN-RIPv2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:26:51 2024
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

(netscreenVR,) = mibBuilder.importSymbols(
    "NETSCREEN-SMI",
    "netscreenVR")

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

nsRip2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 18, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RouteTag(OctetString, TextualConvention):
    status = "deprecated"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )



# MIB Managed Objects in the order of their OIDs

_NsRip2GlobalsTable_Object = MibTable
nsRip2GlobalsTable = _NsRip2GlobalsTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 4, 1)
)
if mibBuilder.loadTexts:
    nsRip2GlobalsTable.setStatus("deprecated")
_NsRip2GlobalsEntry_Object = MibTableRow
nsRip2GlobalsEntry = _NsRip2GlobalsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 4, 1, 1)
)
nsRip2GlobalsEntry.setIndexNames(
    (0, "NETSCREEN-RIPv2-MIB", "nsRip2GlobalVRID"),
)
if mibBuilder.loadTexts:
    nsRip2GlobalsEntry.setStatus("deprecated")
_NsRip2GlobalRouteChanges_Type = Counter32
_NsRip2GlobalRouteChanges_Object = MibTableColumn
nsRip2GlobalRouteChanges = _NsRip2GlobalRouteChanges_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 4, 1, 1, 1),
    _NsRip2GlobalRouteChanges_Type()
)
nsRip2GlobalRouteChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsRip2GlobalRouteChanges.setStatus("deprecated")
_NsRip2GlobalQueries_Type = Counter32
_NsRip2GlobalQueries_Object = MibTableColumn
nsRip2GlobalQueries = _NsRip2GlobalQueries_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 4, 1, 1, 2),
    _NsRip2GlobalQueries_Type()
)
nsRip2GlobalQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsRip2GlobalQueries.setStatus("deprecated")


class _NsRip2GlobalVRID_Type(Integer32):
    """Custom type nsRip2GlobalVRID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NsRip2GlobalVRID_Type.__name__ = "Integer32"
_NsRip2GlobalVRID_Object = MibTableColumn
nsRip2GlobalVRID = _NsRip2GlobalVRID_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 4, 1, 1, 3),
    _NsRip2GlobalVRID_Type()
)
nsRip2GlobalVRID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsRip2GlobalVRID.setStatus("deprecated")
_NsRip2IfStatTable_Object = MibTable
nsRip2IfStatTable = _NsRip2IfStatTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 4, 2)
)
if mibBuilder.loadTexts:
    nsRip2IfStatTable.setStatus("deprecated")
_NsRip2IfStatEntry_Object = MibTableRow
nsRip2IfStatEntry = _NsRip2IfStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 4, 2, 1)
)
nsRip2IfStatEntry.setIndexNames(
    (0, "NETSCREEN-RIPv2-MIB", "nsRip2IfStatAddress"),
    (0, "NETSCREEN-RIPv2-MIB", "nsRip2IfStatVRID"),
)
if mibBuilder.loadTexts:
    nsRip2IfStatEntry.setStatus("deprecated")
_NsRip2IfStatAddress_Type = IpAddress
_NsRip2IfStatAddress_Object = MibTableColumn
nsRip2IfStatAddress = _NsRip2IfStatAddress_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 4, 2, 1, 1),
    _NsRip2IfStatAddress_Type()
)
nsRip2IfStatAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsRip2IfStatAddress.setStatus("deprecated")
_NsRip2IfStatRcvBadPackets_Type = Counter32
_NsRip2IfStatRcvBadPackets_Object = MibTableColumn
nsRip2IfStatRcvBadPackets = _NsRip2IfStatRcvBadPackets_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 4, 2, 1, 2),
    _NsRip2IfStatRcvBadPackets_Type()
)
nsRip2IfStatRcvBadPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsRip2IfStatRcvBadPackets.setStatus("deprecated")
_NsRip2IfStatRcvBadRoutes_Type = Counter32
_NsRip2IfStatRcvBadRoutes_Object = MibTableColumn
nsRip2IfStatRcvBadRoutes = _NsRip2IfStatRcvBadRoutes_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 4, 2, 1, 3),
    _NsRip2IfStatRcvBadRoutes_Type()
)
nsRip2IfStatRcvBadRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsRip2IfStatRcvBadRoutes.setStatus("deprecated")
_NsRip2IfStatSentUpdates_Type = Counter32
_NsRip2IfStatSentUpdates_Object = MibTableColumn
nsRip2IfStatSentUpdates = _NsRip2IfStatSentUpdates_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 4, 2, 1, 4),
    _NsRip2IfStatSentUpdates_Type()
)
nsRip2IfStatSentUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsRip2IfStatSentUpdates.setStatus("deprecated")
_NsRip2IfStatStatus_Type = RowStatus
_NsRip2IfStatStatus_Object = MibTableColumn
nsRip2IfStatStatus = _NsRip2IfStatStatus_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 4, 2, 1, 5),
    _NsRip2IfStatStatus_Type()
)
nsRip2IfStatStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsRip2IfStatStatus.setStatus("deprecated")


class _NsRip2IfStatVRID_Type(Integer32):
    """Custom type nsRip2IfStatVRID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NsRip2IfStatVRID_Type.__name__ = "Integer32"
_NsRip2IfStatVRID_Object = MibTableColumn
nsRip2IfStatVRID = _NsRip2IfStatVRID_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 4, 2, 1, 6),
    _NsRip2IfStatVRID_Type()
)
nsRip2IfStatVRID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsRip2IfStatVRID.setStatus("deprecated")
_NsRip2IfConfTable_Object = MibTable
nsRip2IfConfTable = _NsRip2IfConfTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 4, 3)
)
if mibBuilder.loadTexts:
    nsRip2IfConfTable.setStatus("deprecated")
_NsRip2IfConfEntry_Object = MibTableRow
nsRip2IfConfEntry = _NsRip2IfConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 4, 3, 1)
)
nsRip2IfConfEntry.setIndexNames(
    (0, "NETSCREEN-RIPv2-MIB", "nsRip2IfConfAddress"),
    (0, "NETSCREEN-RIPv2-MIB", "nsRip2IfConfVRID"),
)
if mibBuilder.loadTexts:
    nsRip2IfConfEntry.setStatus("deprecated")
_NsRip2IfConfAddress_Type = IpAddress
_NsRip2IfConfAddress_Object = MibTableColumn
nsRip2IfConfAddress = _NsRip2IfConfAddress_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 4, 3, 1, 1),
    _NsRip2IfConfAddress_Type()
)
nsRip2IfConfAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsRip2IfConfAddress.setStatus("deprecated")


class _NsRip2IfConfDomain_Type(RouteTag):
    """Custom type nsRip2IfConfDomain based on RouteTag"""
    defaultHexValue = "0000"


_NsRip2IfConfDomain_Object = MibTableColumn
nsRip2IfConfDomain = _NsRip2IfConfDomain_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 4, 3, 1, 2),
    _NsRip2IfConfDomain_Type()
)
nsRip2IfConfDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsRip2IfConfDomain.setStatus("obsolete")


class _NsRip2IfConfAuthType_Type(Integer32):
    """Custom type nsRip2IfConfAuthType based on Integer32"""
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
        *(("md5", 3),
          ("noAuthentication", 1),
          ("simplePassword", 2))
    )


_NsRip2IfConfAuthType_Type.__name__ = "Integer32"
_NsRip2IfConfAuthType_Object = MibTableColumn
nsRip2IfConfAuthType = _NsRip2IfConfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 4, 3, 1, 3),
    _NsRip2IfConfAuthType_Type()
)
nsRip2IfConfAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsRip2IfConfAuthType.setStatus("deprecated")


class _NsRip2IfConfAuthKey_Type(OctetString):
    """Custom type nsRip2IfConfAuthKey based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_NsRip2IfConfAuthKey_Type.__name__ = "OctetString"
_NsRip2IfConfAuthKey_Object = MibTableColumn
nsRip2IfConfAuthKey = _NsRip2IfConfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 4, 3, 1, 4),
    _NsRip2IfConfAuthKey_Type()
)
nsRip2IfConfAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsRip2IfConfAuthKey.setStatus("deprecated")


class _NsRip2IfConfSend_Type(Integer32):
    """Custom type nsRip2IfConfSend based on Integer32"""
    defaultValue = 3

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
        *(("doNotSend", 1),
          ("rip1Compatible", 3),
          ("ripV1Demand", 5),
          ("ripV2Demand", 6),
          ("ripVersion1", 2),
          ("ripVersion2", 4))
    )


_NsRip2IfConfSend_Type.__name__ = "Integer32"
_NsRip2IfConfSend_Object = MibTableColumn
nsRip2IfConfSend = _NsRip2IfConfSend_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 4, 3, 1, 5),
    _NsRip2IfConfSend_Type()
)
nsRip2IfConfSend.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsRip2IfConfSend.setStatus("deprecated")


class _NsRip2IfConfReceive_Type(Integer32):
    """Custom type nsRip2IfConfReceive based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("doNotRecieve", 4),
          ("rip1", 1),
          ("rip1OrRip2", 3),
          ("rip2", 2))
    )


_NsRip2IfConfReceive_Type.__name__ = "Integer32"
_NsRip2IfConfReceive_Object = MibTableColumn
nsRip2IfConfReceive = _NsRip2IfConfReceive_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 4, 3, 1, 6),
    _NsRip2IfConfReceive_Type()
)
nsRip2IfConfReceive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsRip2IfConfReceive.setStatus("deprecated")


class _NsRip2IfConfDefaultMetric_Type(Integer32):
    """Custom type nsRip2IfConfDefaultMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_NsRip2IfConfDefaultMetric_Type.__name__ = "Integer32"
_NsRip2IfConfDefaultMetric_Object = MibTableColumn
nsRip2IfConfDefaultMetric = _NsRip2IfConfDefaultMetric_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 4, 3, 1, 7),
    _NsRip2IfConfDefaultMetric_Type()
)
nsRip2IfConfDefaultMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsRip2IfConfDefaultMetric.setStatus("deprecated")
_NsRip2IfConfStatus_Type = RowStatus
_NsRip2IfConfStatus_Object = MibTableColumn
nsRip2IfConfStatus = _NsRip2IfConfStatus_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 4, 3, 1, 8),
    _NsRip2IfConfStatus_Type()
)
nsRip2IfConfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsRip2IfConfStatus.setStatus("deprecated")
_NsRip2IfConfSrcAddress_Type = IpAddress
_NsRip2IfConfSrcAddress_Object = MibTableColumn
nsRip2IfConfSrcAddress = _NsRip2IfConfSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 4, 3, 1, 9),
    _NsRip2IfConfSrcAddress_Type()
)
nsRip2IfConfSrcAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsRip2IfConfSrcAddress.setStatus("deprecated")


class _NsRip2IfConfVRID_Type(Integer32):
    """Custom type nsRip2IfConfVRID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NsRip2IfConfVRID_Type.__name__ = "Integer32"
_NsRip2IfConfVRID_Object = MibTableColumn
nsRip2IfConfVRID = _NsRip2IfConfVRID_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 4, 3, 1, 10),
    _NsRip2IfConfVRID_Type()
)
nsRip2IfConfVRID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsRip2IfConfVRID.setStatus("deprecated")
_NsRip2PeerTable_Object = MibTable
nsRip2PeerTable = _NsRip2PeerTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 4, 4)
)
if mibBuilder.loadTexts:
    nsRip2PeerTable.setStatus("deprecated")
_NsRip2PeerEntry_Object = MibTableRow
nsRip2PeerEntry = _NsRip2PeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 4, 4, 1)
)
nsRip2PeerEntry.setIndexNames(
    (0, "NETSCREEN-RIPv2-MIB", "nsRip2PeerAddress"),
    (0, "NETSCREEN-RIPv2-MIB", "nsRip2PeerDomain"),
    (0, "NETSCREEN-RIPv2-MIB", "nsRip2PeerVRID"),
)
if mibBuilder.loadTexts:
    nsRip2PeerEntry.setStatus("deprecated")
_NsRip2PeerAddress_Type = IpAddress
_NsRip2PeerAddress_Object = MibTableColumn
nsRip2PeerAddress = _NsRip2PeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 4, 4, 1, 1),
    _NsRip2PeerAddress_Type()
)
nsRip2PeerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsRip2PeerAddress.setStatus("deprecated")
_NsRip2PeerDomain_Type = RouteTag
_NsRip2PeerDomain_Object = MibTableColumn
nsRip2PeerDomain = _NsRip2PeerDomain_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 4, 4, 1, 2),
    _NsRip2PeerDomain_Type()
)
nsRip2PeerDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsRip2PeerDomain.setStatus("deprecated")
_NsRip2PeerLastUpdate_Type = TimeTicks
_NsRip2PeerLastUpdate_Object = MibTableColumn
nsRip2PeerLastUpdate = _NsRip2PeerLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 4, 4, 1, 3),
    _NsRip2PeerLastUpdate_Type()
)
nsRip2PeerLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsRip2PeerLastUpdate.setStatus("deprecated")


class _NsRip2PeerVersion_Type(Integer32):
    """Custom type nsRip2PeerVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NsRip2PeerVersion_Type.__name__ = "Integer32"
_NsRip2PeerVersion_Object = MibTableColumn
nsRip2PeerVersion = _NsRip2PeerVersion_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 4, 4, 1, 4),
    _NsRip2PeerVersion_Type()
)
nsRip2PeerVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsRip2PeerVersion.setStatus("deprecated")
_NsRip2PeerRcvBadPackets_Type = Counter32
_NsRip2PeerRcvBadPackets_Object = MibTableColumn
nsRip2PeerRcvBadPackets = _NsRip2PeerRcvBadPackets_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 4, 4, 1, 5),
    _NsRip2PeerRcvBadPackets_Type()
)
nsRip2PeerRcvBadPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsRip2PeerRcvBadPackets.setStatus("deprecated")
_NsRip2PeerRcvBadRoutes_Type = Counter32
_NsRip2PeerRcvBadRoutes_Object = MibTableColumn
nsRip2PeerRcvBadRoutes = _NsRip2PeerRcvBadRoutes_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 4, 4, 1, 6),
    _NsRip2PeerRcvBadRoutes_Type()
)
nsRip2PeerRcvBadRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsRip2PeerRcvBadRoutes.setStatus("deprecated")


class _NsRip2PeerVRID_Type(Integer32):
    """Custom type nsRip2PeerVRID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NsRip2PeerVRID_Type.__name__ = "Integer32"
_NsRip2PeerVRID_Object = MibTableColumn
nsRip2PeerVRID = _NsRip2PeerVRID_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 4, 4, 1, 7),
    _NsRip2PeerVRID_Type()
)
nsRip2PeerVRID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsRip2PeerVRID.setStatus("deprecated")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETSCREEN-RIPv2-MIB",
    **{"RouteTag": RouteTag,
       "nsRip2": nsRip2,
       "nsRip2GlobalsTable": nsRip2GlobalsTable,
       "nsRip2GlobalsEntry": nsRip2GlobalsEntry,
       "nsRip2GlobalRouteChanges": nsRip2GlobalRouteChanges,
       "nsRip2GlobalQueries": nsRip2GlobalQueries,
       "nsRip2GlobalVRID": nsRip2GlobalVRID,
       "nsRip2IfStatTable": nsRip2IfStatTable,
       "nsRip2IfStatEntry": nsRip2IfStatEntry,
       "nsRip2IfStatAddress": nsRip2IfStatAddress,
       "nsRip2IfStatRcvBadPackets": nsRip2IfStatRcvBadPackets,
       "nsRip2IfStatRcvBadRoutes": nsRip2IfStatRcvBadRoutes,
       "nsRip2IfStatSentUpdates": nsRip2IfStatSentUpdates,
       "nsRip2IfStatStatus": nsRip2IfStatStatus,
       "nsRip2IfStatVRID": nsRip2IfStatVRID,
       "nsRip2IfConfTable": nsRip2IfConfTable,
       "nsRip2IfConfEntry": nsRip2IfConfEntry,
       "nsRip2IfConfAddress": nsRip2IfConfAddress,
       "nsRip2IfConfDomain": nsRip2IfConfDomain,
       "nsRip2IfConfAuthType": nsRip2IfConfAuthType,
       "nsRip2IfConfAuthKey": nsRip2IfConfAuthKey,
       "nsRip2IfConfSend": nsRip2IfConfSend,
       "nsRip2IfConfReceive": nsRip2IfConfReceive,
       "nsRip2IfConfDefaultMetric": nsRip2IfConfDefaultMetric,
       "nsRip2IfConfStatus": nsRip2IfConfStatus,
       "nsRip2IfConfSrcAddress": nsRip2IfConfSrcAddress,
       "nsRip2IfConfVRID": nsRip2IfConfVRID,
       "nsRip2PeerTable": nsRip2PeerTable,
       "nsRip2PeerEntry": nsRip2PeerEntry,
       "nsRip2PeerAddress": nsRip2PeerAddress,
       "nsRip2PeerDomain": nsRip2PeerDomain,
       "nsRip2PeerLastUpdate": nsRip2PeerLastUpdate,
       "nsRip2PeerVersion": nsRip2PeerVersion,
       "nsRip2PeerRcvBadPackets": nsRip2PeerRcvBadPackets,
       "nsRip2PeerRcvBadRoutes": nsRip2PeerRcvBadRoutes,
       "nsRip2PeerVRID": nsRip2PeerVRID}
)
