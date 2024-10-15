# SNMP MIB module (NETSCREEN-VR-RIPv2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETSCREEN-VR-RIPv2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:27:10 2024
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

nsVrRip2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 18, 7)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RouteTag(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )



# MIB Managed Objects in the order of their OIDs

_NsVrRip2GlobalsTable_Object = MibTable
nsVrRip2GlobalsTable = _NsVrRip2GlobalsTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 7, 1)
)
if mibBuilder.loadTexts:
    nsVrRip2GlobalsTable.setStatus("current")
_NsVrRip2GlobalsEntry_Object = MibTableRow
nsVrRip2GlobalsEntry = _NsVrRip2GlobalsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 7, 1, 1)
)
nsVrRip2GlobalsEntry.setIndexNames(
    (0, "NETSCREEN-VR-RIPv2-MIB", "nsVrRip2GlobalVRID"),
)
if mibBuilder.loadTexts:
    nsVrRip2GlobalsEntry.setStatus("current")
_NsVrRip2GlobalRouteChanges_Type = Counter32
_NsVrRip2GlobalRouteChanges_Object = MibTableColumn
nsVrRip2GlobalRouteChanges = _NsVrRip2GlobalRouteChanges_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 7, 1, 1, 1),
    _NsVrRip2GlobalRouteChanges_Type()
)
nsVrRip2GlobalRouteChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrRip2GlobalRouteChanges.setStatus("current")
_NsVrRip2GlobalQueries_Type = Counter32
_NsVrRip2GlobalQueries_Object = MibTableColumn
nsVrRip2GlobalQueries = _NsVrRip2GlobalQueries_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 7, 1, 1, 2),
    _NsVrRip2GlobalQueries_Type()
)
nsVrRip2GlobalQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrRip2GlobalQueries.setStatus("current")


class _NsVrRip2GlobalVRID_Type(Integer32):
    """Custom type nsVrRip2GlobalVRID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NsVrRip2GlobalVRID_Type.__name__ = "Integer32"
_NsVrRip2GlobalVRID_Object = MibTableColumn
nsVrRip2GlobalVRID = _NsVrRip2GlobalVRID_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 7, 1, 1, 3),
    _NsVrRip2GlobalVRID_Type()
)
nsVrRip2GlobalVRID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrRip2GlobalVRID.setStatus("current")
_NsVrRip2IfStatTable_Object = MibTable
nsVrRip2IfStatTable = _NsVrRip2IfStatTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 7, 2)
)
if mibBuilder.loadTexts:
    nsVrRip2IfStatTable.setStatus("current")
_NsVrRip2IfStatEntry_Object = MibTableRow
nsVrRip2IfStatEntry = _NsVrRip2IfStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 7, 2, 1)
)
nsVrRip2IfStatEntry.setIndexNames(
    (0, "NETSCREEN-VR-RIPv2-MIB", "nsVrRip2IfStatVRID"),
    (0, "NETSCREEN-VR-RIPv2-MIB", "nsVrRip2IfStatAddress"),
)
if mibBuilder.loadTexts:
    nsVrRip2IfStatEntry.setStatus("current")
_NsVrRip2IfStatAddress_Type = IpAddress
_NsVrRip2IfStatAddress_Object = MibTableColumn
nsVrRip2IfStatAddress = _NsVrRip2IfStatAddress_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 7, 2, 1, 1),
    _NsVrRip2IfStatAddress_Type()
)
nsVrRip2IfStatAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrRip2IfStatAddress.setStatus("current")
_NsVrRip2IfStatRcvBadPackets_Type = Counter32
_NsVrRip2IfStatRcvBadPackets_Object = MibTableColumn
nsVrRip2IfStatRcvBadPackets = _NsVrRip2IfStatRcvBadPackets_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 7, 2, 1, 2),
    _NsVrRip2IfStatRcvBadPackets_Type()
)
nsVrRip2IfStatRcvBadPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrRip2IfStatRcvBadPackets.setStatus("current")
_NsVrRip2IfStatRcvBadRoutes_Type = Counter32
_NsVrRip2IfStatRcvBadRoutes_Object = MibTableColumn
nsVrRip2IfStatRcvBadRoutes = _NsVrRip2IfStatRcvBadRoutes_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 7, 2, 1, 3),
    _NsVrRip2IfStatRcvBadRoutes_Type()
)
nsVrRip2IfStatRcvBadRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrRip2IfStatRcvBadRoutes.setStatus("current")
_NsVrRip2IfStatSentUpdates_Type = Counter32
_NsVrRip2IfStatSentUpdates_Object = MibTableColumn
nsVrRip2IfStatSentUpdates = _NsVrRip2IfStatSentUpdates_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 7, 2, 1, 4),
    _NsVrRip2IfStatSentUpdates_Type()
)
nsVrRip2IfStatSentUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrRip2IfStatSentUpdates.setStatus("current")
_NsVrRip2IfStatStatus_Type = RowStatus
_NsVrRip2IfStatStatus_Object = MibTableColumn
nsVrRip2IfStatStatus = _NsVrRip2IfStatStatus_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 7, 2, 1, 5),
    _NsVrRip2IfStatStatus_Type()
)
nsVrRip2IfStatStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsVrRip2IfStatStatus.setStatus("current")


class _NsVrRip2IfStatVRID_Type(Integer32):
    """Custom type nsVrRip2IfStatVRID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NsVrRip2IfStatVRID_Type.__name__ = "Integer32"
_NsVrRip2IfStatVRID_Object = MibTableColumn
nsVrRip2IfStatVRID = _NsVrRip2IfStatVRID_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 7, 2, 1, 6),
    _NsVrRip2IfStatVRID_Type()
)
nsVrRip2IfStatVRID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrRip2IfStatVRID.setStatus("current")
_NsVrRip2IfConfTable_Object = MibTable
nsVrRip2IfConfTable = _NsVrRip2IfConfTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 7, 3)
)
if mibBuilder.loadTexts:
    nsVrRip2IfConfTable.setStatus("current")
_NsVrRip2IfConfEntry_Object = MibTableRow
nsVrRip2IfConfEntry = _NsVrRip2IfConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 7, 3, 1)
)
nsVrRip2IfConfEntry.setIndexNames(
    (0, "NETSCREEN-VR-RIPv2-MIB", "nsVrRip2IfConfVRID"),
    (0, "NETSCREEN-VR-RIPv2-MIB", "nsVrRip2IfConfAddress"),
)
if mibBuilder.loadTexts:
    nsVrRip2IfConfEntry.setStatus("current")
_NsVrRip2IfConfAddress_Type = IpAddress
_NsVrRip2IfConfAddress_Object = MibTableColumn
nsVrRip2IfConfAddress = _NsVrRip2IfConfAddress_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 7, 3, 1, 1),
    _NsVrRip2IfConfAddress_Type()
)
nsVrRip2IfConfAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrRip2IfConfAddress.setStatus("current")


class _NsVrRip2IfConfDomain_Type(RouteTag):
    """Custom type nsVrRip2IfConfDomain based on RouteTag"""
    defaultHexValue = "0000"


_NsVrRip2IfConfDomain_Object = MibTableColumn
nsVrRip2IfConfDomain = _NsVrRip2IfConfDomain_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 7, 3, 1, 2),
    _NsVrRip2IfConfDomain_Type()
)
nsVrRip2IfConfDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsVrRip2IfConfDomain.setStatus("obsolete")


class _NsVrRip2IfConfAuthType_Type(Integer32):
    """Custom type nsVrRip2IfConfAuthType based on Integer32"""
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


_NsVrRip2IfConfAuthType_Type.__name__ = "Integer32"
_NsVrRip2IfConfAuthType_Object = MibTableColumn
nsVrRip2IfConfAuthType = _NsVrRip2IfConfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 7, 3, 1, 3),
    _NsVrRip2IfConfAuthType_Type()
)
nsVrRip2IfConfAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsVrRip2IfConfAuthType.setStatus("current")


class _NsVrRip2IfConfAuthKey_Type(OctetString):
    """Custom type nsVrRip2IfConfAuthKey based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_NsVrRip2IfConfAuthKey_Type.__name__ = "OctetString"
_NsVrRip2IfConfAuthKey_Object = MibTableColumn
nsVrRip2IfConfAuthKey = _NsVrRip2IfConfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 7, 3, 1, 4),
    _NsVrRip2IfConfAuthKey_Type()
)
nsVrRip2IfConfAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsVrRip2IfConfAuthKey.setStatus("current")


class _NsVrRip2IfConfSend_Type(Integer32):
    """Custom type nsVrRip2IfConfSend based on Integer32"""
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


_NsVrRip2IfConfSend_Type.__name__ = "Integer32"
_NsVrRip2IfConfSend_Object = MibTableColumn
nsVrRip2IfConfSend = _NsVrRip2IfConfSend_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 7, 3, 1, 5),
    _NsVrRip2IfConfSend_Type()
)
nsVrRip2IfConfSend.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsVrRip2IfConfSend.setStatus("current")


class _NsVrRip2IfConfReceive_Type(Integer32):
    """Custom type nsVrRip2IfConfReceive based on Integer32"""
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


_NsVrRip2IfConfReceive_Type.__name__ = "Integer32"
_NsVrRip2IfConfReceive_Object = MibTableColumn
nsVrRip2IfConfReceive = _NsVrRip2IfConfReceive_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 7, 3, 1, 6),
    _NsVrRip2IfConfReceive_Type()
)
nsVrRip2IfConfReceive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsVrRip2IfConfReceive.setStatus("current")


class _NsVrRip2IfConfDefaultMetric_Type(Integer32):
    """Custom type nsVrRip2IfConfDefaultMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_NsVrRip2IfConfDefaultMetric_Type.__name__ = "Integer32"
_NsVrRip2IfConfDefaultMetric_Object = MibTableColumn
nsVrRip2IfConfDefaultMetric = _NsVrRip2IfConfDefaultMetric_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 7, 3, 1, 7),
    _NsVrRip2IfConfDefaultMetric_Type()
)
nsVrRip2IfConfDefaultMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsVrRip2IfConfDefaultMetric.setStatus("current")
_NsVrRip2IfConfStatus_Type = RowStatus
_NsVrRip2IfConfStatus_Object = MibTableColumn
nsVrRip2IfConfStatus = _NsVrRip2IfConfStatus_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 7, 3, 1, 8),
    _NsVrRip2IfConfStatus_Type()
)
nsVrRip2IfConfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsVrRip2IfConfStatus.setStatus("current")
_NsVrRip2IfConfSrcAddress_Type = IpAddress
_NsVrRip2IfConfSrcAddress_Object = MibTableColumn
nsVrRip2IfConfSrcAddress = _NsVrRip2IfConfSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 7, 3, 1, 9),
    _NsVrRip2IfConfSrcAddress_Type()
)
nsVrRip2IfConfSrcAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nsVrRip2IfConfSrcAddress.setStatus("current")


class _NsVrRip2IfConfVRID_Type(Integer32):
    """Custom type nsVrRip2IfConfVRID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NsVrRip2IfConfVRID_Type.__name__ = "Integer32"
_NsVrRip2IfConfVRID_Object = MibTableColumn
nsVrRip2IfConfVRID = _NsVrRip2IfConfVRID_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 7, 3, 1, 10),
    _NsVrRip2IfConfVRID_Type()
)
nsVrRip2IfConfVRID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrRip2IfConfVRID.setStatus("current")
_NsVrRip2PeerTable_Object = MibTable
nsVrRip2PeerTable = _NsVrRip2PeerTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 7, 4)
)
if mibBuilder.loadTexts:
    nsVrRip2PeerTable.setStatus("current")
_NsVrRip2PeerEntry_Object = MibTableRow
nsVrRip2PeerEntry = _NsVrRip2PeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 7, 4, 1)
)
nsVrRip2PeerEntry.setIndexNames(
    (0, "NETSCREEN-VR-RIPv2-MIB", "nsVrRip2PeerVRID"),
    (0, "NETSCREEN-VR-RIPv2-MIB", "nsVrRip2PeerAddress"),
    (0, "NETSCREEN-VR-RIPv2-MIB", "nsVrRip2PeerDomain"),
)
if mibBuilder.loadTexts:
    nsVrRip2PeerEntry.setStatus("current")
_NsVrRip2PeerAddress_Type = IpAddress
_NsVrRip2PeerAddress_Object = MibTableColumn
nsVrRip2PeerAddress = _NsVrRip2PeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 7, 4, 1, 1),
    _NsVrRip2PeerAddress_Type()
)
nsVrRip2PeerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrRip2PeerAddress.setStatus("current")
_NsVrRip2PeerDomain_Type = RouteTag
_NsVrRip2PeerDomain_Object = MibTableColumn
nsVrRip2PeerDomain = _NsVrRip2PeerDomain_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 7, 4, 1, 2),
    _NsVrRip2PeerDomain_Type()
)
nsVrRip2PeerDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrRip2PeerDomain.setStatus("current")
_NsVrRip2PeerLastUpdate_Type = TimeTicks
_NsVrRip2PeerLastUpdate_Object = MibTableColumn
nsVrRip2PeerLastUpdate = _NsVrRip2PeerLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 7, 4, 1, 3),
    _NsVrRip2PeerLastUpdate_Type()
)
nsVrRip2PeerLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrRip2PeerLastUpdate.setStatus("current")


class _NsVrRip2PeerVersion_Type(Integer32):
    """Custom type nsVrRip2PeerVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NsVrRip2PeerVersion_Type.__name__ = "Integer32"
_NsVrRip2PeerVersion_Object = MibTableColumn
nsVrRip2PeerVersion = _NsVrRip2PeerVersion_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 7, 4, 1, 4),
    _NsVrRip2PeerVersion_Type()
)
nsVrRip2PeerVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrRip2PeerVersion.setStatus("current")
_NsVrRip2PeerRcvBadPackets_Type = Counter32
_NsVrRip2PeerRcvBadPackets_Object = MibTableColumn
nsVrRip2PeerRcvBadPackets = _NsVrRip2PeerRcvBadPackets_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 7, 4, 1, 5),
    _NsVrRip2PeerRcvBadPackets_Type()
)
nsVrRip2PeerRcvBadPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrRip2PeerRcvBadPackets.setStatus("current")
_NsVrRip2PeerRcvBadRoutes_Type = Counter32
_NsVrRip2PeerRcvBadRoutes_Object = MibTableColumn
nsVrRip2PeerRcvBadRoutes = _NsVrRip2PeerRcvBadRoutes_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 7, 4, 1, 6),
    _NsVrRip2PeerRcvBadRoutes_Type()
)
nsVrRip2PeerRcvBadRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrRip2PeerRcvBadRoutes.setStatus("current")


class _NsVrRip2PeerVRID_Type(Integer32):
    """Custom type nsVrRip2PeerVRID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NsVrRip2PeerVRID_Type.__name__ = "Integer32"
_NsVrRip2PeerVRID_Object = MibTableColumn
nsVrRip2PeerVRID = _NsVrRip2PeerVRID_Object(
    (1, 3, 6, 1, 4, 1, 3224, 18, 7, 4, 1, 7),
    _NsVrRip2PeerVRID_Type()
)
nsVrRip2PeerVRID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVrRip2PeerVRID.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETSCREEN-VR-RIPv2-MIB",
    **{"RouteTag": RouteTag,
       "nsVrRip2": nsVrRip2,
       "nsVrRip2GlobalsTable": nsVrRip2GlobalsTable,
       "nsVrRip2GlobalsEntry": nsVrRip2GlobalsEntry,
       "nsVrRip2GlobalRouteChanges": nsVrRip2GlobalRouteChanges,
       "nsVrRip2GlobalQueries": nsVrRip2GlobalQueries,
       "nsVrRip2GlobalVRID": nsVrRip2GlobalVRID,
       "nsVrRip2IfStatTable": nsVrRip2IfStatTable,
       "nsVrRip2IfStatEntry": nsVrRip2IfStatEntry,
       "nsVrRip2IfStatAddress": nsVrRip2IfStatAddress,
       "nsVrRip2IfStatRcvBadPackets": nsVrRip2IfStatRcvBadPackets,
       "nsVrRip2IfStatRcvBadRoutes": nsVrRip2IfStatRcvBadRoutes,
       "nsVrRip2IfStatSentUpdates": nsVrRip2IfStatSentUpdates,
       "nsVrRip2IfStatStatus": nsVrRip2IfStatStatus,
       "nsVrRip2IfStatVRID": nsVrRip2IfStatVRID,
       "nsVrRip2IfConfTable": nsVrRip2IfConfTable,
       "nsVrRip2IfConfEntry": nsVrRip2IfConfEntry,
       "nsVrRip2IfConfAddress": nsVrRip2IfConfAddress,
       "nsVrRip2IfConfDomain": nsVrRip2IfConfDomain,
       "nsVrRip2IfConfAuthType": nsVrRip2IfConfAuthType,
       "nsVrRip2IfConfAuthKey": nsVrRip2IfConfAuthKey,
       "nsVrRip2IfConfSend": nsVrRip2IfConfSend,
       "nsVrRip2IfConfReceive": nsVrRip2IfConfReceive,
       "nsVrRip2IfConfDefaultMetric": nsVrRip2IfConfDefaultMetric,
       "nsVrRip2IfConfStatus": nsVrRip2IfConfStatus,
       "nsVrRip2IfConfSrcAddress": nsVrRip2IfConfSrcAddress,
       "nsVrRip2IfConfVRID": nsVrRip2IfConfVRID,
       "nsVrRip2PeerTable": nsVrRip2PeerTable,
       "nsVrRip2PeerEntry": nsVrRip2PeerEntry,
       "nsVrRip2PeerAddress": nsVrRip2PeerAddress,
       "nsVrRip2PeerDomain": nsVrRip2PeerDomain,
       "nsVrRip2PeerLastUpdate": nsVrRip2PeerLastUpdate,
       "nsVrRip2PeerVersion": nsVrRip2PeerVersion,
       "nsVrRip2PeerRcvBadPackets": nsVrRip2PeerRcvBadPackets,
       "nsVrRip2PeerRcvBadRoutes": nsVrRip2PeerRcvBadRoutes,
       "nsVrRip2PeerVRID": nsVrRip2PeerVRID}
)
