# SNMP MIB module (RFC1389-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RFC1389-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:15:09 2024
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


# Types definitions



class RouteTag(OctetString):
    """Custom type RouteTag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Mgmt_ObjectIdentity = ObjectIdentity
mgmt = _Mgmt_ObjectIdentity(
    (1, 3, 6, 1, 2)
)
_Mib_2_ObjectIdentity = ObjectIdentity
mib_2 = _Mib_2_ObjectIdentity(
    (1, 3, 6, 1, 2, 1)
)
_Rip2_ObjectIdentity = ObjectIdentity
rip2 = _Rip2_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 23)
)
_Rip2GlobalGroup_ObjectIdentity = ObjectIdentity
rip2GlobalGroup = _Rip2GlobalGroup_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 23, 1)
)
_Rip2GlobalRouteChanges_Type = Counter32
_Rip2GlobalRouteChanges_Object = MibScalar
rip2GlobalRouteChanges = _Rip2GlobalRouteChanges_Object(
    (1, 3, 6, 1, 2, 1, 23, 1, 1),
    _Rip2GlobalRouteChanges_Type()
)
rip2GlobalRouteChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rip2GlobalRouteChanges.setStatus("mandatory")
_Rip2GlobalQueries_Type = Counter32
_Rip2GlobalQueries_Object = MibScalar
rip2GlobalQueries = _Rip2GlobalQueries_Object(
    (1, 3, 6, 1, 2, 1, 23, 1, 2),
    _Rip2GlobalQueries_Type()
)
rip2GlobalQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rip2GlobalQueries.setStatus("mandatory")
_Rip2IfStatTable_Object = MibTable
rip2IfStatTable = _Rip2IfStatTable_Object(
    (1, 3, 6, 1, 2, 1, 23, 2)
)
if mibBuilder.loadTexts:
    rip2IfStatTable.setStatus("mandatory")
_Rip2IfStatEntry_Object = MibTableRow
rip2IfStatEntry = _Rip2IfStatEntry_Object(
    (1, 3, 6, 1, 2, 1, 23, 2, 1)
)
rip2IfStatEntry.setIndexNames(
    (0, "RFC1389-MIB", "rip2IfStatAddress"),
)
if mibBuilder.loadTexts:
    rip2IfStatEntry.setStatus("mandatory")
_Rip2IfStatAddress_Type = IpAddress
_Rip2IfStatAddress_Object = MibTableColumn
rip2IfStatAddress = _Rip2IfStatAddress_Object(
    (1, 3, 6, 1, 2, 1, 23, 2, 1, 1),
    _Rip2IfStatAddress_Type()
)
rip2IfStatAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rip2IfStatAddress.setStatus("mandatory")
_Rip2IfStatRcvBadPackets_Type = Counter32
_Rip2IfStatRcvBadPackets_Object = MibTableColumn
rip2IfStatRcvBadPackets = _Rip2IfStatRcvBadPackets_Object(
    (1, 3, 6, 1, 2, 1, 23, 2, 1, 2),
    _Rip2IfStatRcvBadPackets_Type()
)
rip2IfStatRcvBadPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rip2IfStatRcvBadPackets.setStatus("mandatory")
_Rip2IfStatRcvBadRoutes_Type = Counter32
_Rip2IfStatRcvBadRoutes_Object = MibTableColumn
rip2IfStatRcvBadRoutes = _Rip2IfStatRcvBadRoutes_Object(
    (1, 3, 6, 1, 2, 1, 23, 2, 1, 3),
    _Rip2IfStatRcvBadRoutes_Type()
)
rip2IfStatRcvBadRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rip2IfStatRcvBadRoutes.setStatus("mandatory")
_Rip2IfStatSentUpdates_Type = Counter32
_Rip2IfStatSentUpdates_Object = MibTableColumn
rip2IfStatSentUpdates = _Rip2IfStatSentUpdates_Object(
    (1, 3, 6, 1, 2, 1, 23, 2, 1, 4),
    _Rip2IfStatSentUpdates_Type()
)
rip2IfStatSentUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rip2IfStatSentUpdates.setStatus("mandatory")


class _Rip2IfStatStatus_Type(Integer32):
    """Custom type rip2IfStatStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_Rip2IfStatStatus_Type.__name__ = "Integer32"
_Rip2IfStatStatus_Object = MibTableColumn
rip2IfStatStatus = _Rip2IfStatStatus_Object(
    (1, 3, 6, 1, 2, 1, 23, 2, 1, 5),
    _Rip2IfStatStatus_Type()
)
rip2IfStatStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rip2IfStatStatus.setStatus("mandatory")
_Rip2IfConfTable_Object = MibTable
rip2IfConfTable = _Rip2IfConfTable_Object(
    (1, 3, 6, 1, 2, 1, 23, 3)
)
if mibBuilder.loadTexts:
    rip2IfConfTable.setStatus("mandatory")
_Rip2IfConfEntry_Object = MibTableRow
rip2IfConfEntry = _Rip2IfConfEntry_Object(
    (1, 3, 6, 1, 2, 1, 23, 3, 1)
)
rip2IfConfEntry.setIndexNames(
    (0, "RFC1389-MIB", "rip2IfConfAddress"),
)
if mibBuilder.loadTexts:
    rip2IfConfEntry.setStatus("mandatory")
_Rip2IfConfAddress_Type = IpAddress
_Rip2IfConfAddress_Object = MibTableColumn
rip2IfConfAddress = _Rip2IfConfAddress_Object(
    (1, 3, 6, 1, 2, 1, 23, 3, 1, 1),
    _Rip2IfConfAddress_Type()
)
rip2IfConfAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rip2IfConfAddress.setStatus("mandatory")
_Rip2IfConfDomain_Type = RouteTag
_Rip2IfConfDomain_Object = MibTableColumn
rip2IfConfDomain = _Rip2IfConfDomain_Object(
    (1, 3, 6, 1, 2, 1, 23, 3, 1, 2),
    _Rip2IfConfDomain_Type()
)
rip2IfConfDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rip2IfConfDomain.setStatus("deprecated")


class _Rip2IfConfAuthType_Type(Integer32):
    """Custom type rip2IfConfAuthType based on Integer32"""
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


_Rip2IfConfAuthType_Type.__name__ = "Integer32"
_Rip2IfConfAuthType_Object = MibTableColumn
rip2IfConfAuthType = _Rip2IfConfAuthType_Object(
    (1, 3, 6, 1, 2, 1, 23, 3, 1, 3),
    _Rip2IfConfAuthType_Type()
)
rip2IfConfAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rip2IfConfAuthType.setStatus("mandatory")


class _Rip2IfConfAuthKey_Type(OctetString):
    """Custom type rip2IfConfAuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Rip2IfConfAuthKey_Type.__name__ = "OctetString"
_Rip2IfConfAuthKey_Object = MibTableColumn
rip2IfConfAuthKey = _Rip2IfConfAuthKey_Object(
    (1, 3, 6, 1, 2, 1, 23, 3, 1, 4),
    _Rip2IfConfAuthKey_Type()
)
rip2IfConfAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rip2IfConfAuthKey.setStatus("mandatory")


class _Rip2IfConfSend_Type(Integer32):
    """Custom type rip2IfConfSend based on Integer32"""
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


_Rip2IfConfSend_Type.__name__ = "Integer32"
_Rip2IfConfSend_Object = MibTableColumn
rip2IfConfSend = _Rip2IfConfSend_Object(
    (1, 3, 6, 1, 2, 1, 23, 3, 1, 5),
    _Rip2IfConfSend_Type()
)
rip2IfConfSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rip2IfConfSend.setStatus("mandatory")


class _Rip2IfConfReceive_Type(Integer32):
    """Custom type rip2IfConfReceive based on Integer32"""
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


_Rip2IfConfReceive_Type.__name__ = "Integer32"
_Rip2IfConfReceive_Object = MibTableColumn
rip2IfConfReceive = _Rip2IfConfReceive_Object(
    (1, 3, 6, 1, 2, 1, 23, 3, 1, 6),
    _Rip2IfConfReceive_Type()
)
rip2IfConfReceive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rip2IfConfReceive.setStatus("mandatory")


class _Rip2IfConfDefaultMetric_Type(Integer32):
    """Custom type rip2IfConfDefaultMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Rip2IfConfDefaultMetric_Type.__name__ = "Integer32"
_Rip2IfConfDefaultMetric_Object = MibTableColumn
rip2IfConfDefaultMetric = _Rip2IfConfDefaultMetric_Object(
    (1, 3, 6, 1, 2, 1, 23, 3, 1, 7),
    _Rip2IfConfDefaultMetric_Type()
)
rip2IfConfDefaultMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rip2IfConfDefaultMetric.setStatus("mandatory")


class _Rip2IfConfStatus_Type(Integer32):
    """Custom type rip2IfConfStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_Rip2IfConfStatus_Type.__name__ = "Integer32"
_Rip2IfConfStatus_Object = MibTableColumn
rip2IfConfStatus = _Rip2IfConfStatus_Object(
    (1, 3, 6, 1, 2, 1, 23, 3, 1, 8),
    _Rip2IfConfStatus_Type()
)
rip2IfConfStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rip2IfConfStatus.setStatus("mandatory")
_Rip2IfConfSrcAddress_Type = IpAddress
_Rip2IfConfSrcAddress_Object = MibTableColumn
rip2IfConfSrcAddress = _Rip2IfConfSrcAddress_Object(
    (1, 3, 6, 1, 2, 1, 23, 3, 1, 9),
    _Rip2IfConfSrcAddress_Type()
)
rip2IfConfSrcAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rip2IfConfSrcAddress.setStatus("mandatory")
_Rip2PeerTable_Object = MibTable
rip2PeerTable = _Rip2PeerTable_Object(
    (1, 3, 6, 1, 2, 1, 23, 4)
)
if mibBuilder.loadTexts:
    rip2PeerTable.setStatus("mandatory")
_Rip2PeerEntry_Object = MibTableRow
rip2PeerEntry = _Rip2PeerEntry_Object(
    (1, 3, 6, 1, 2, 1, 23, 4, 1)
)
rip2PeerEntry.setIndexNames(
    (0, "RFC1389-MIB", "rip2PeerAddress"),
    (0, "RFC1389-MIB", "rip2PeerDomain"),
)
if mibBuilder.loadTexts:
    rip2PeerEntry.setStatus("mandatory")
_Rip2PeerAddress_Type = IpAddress
_Rip2PeerAddress_Object = MibTableColumn
rip2PeerAddress = _Rip2PeerAddress_Object(
    (1, 3, 6, 1, 2, 1, 23, 4, 1, 1),
    _Rip2PeerAddress_Type()
)
rip2PeerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rip2PeerAddress.setStatus("mandatory")
_Rip2PeerDomain_Type = RouteTag
_Rip2PeerDomain_Object = MibTableColumn
rip2PeerDomain = _Rip2PeerDomain_Object(
    (1, 3, 6, 1, 2, 1, 23, 4, 1, 2),
    _Rip2PeerDomain_Type()
)
rip2PeerDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rip2PeerDomain.setStatus("mandatory")
_Rip2PeerLastUpdate_Type = TimeTicks
_Rip2PeerLastUpdate_Object = MibTableColumn
rip2PeerLastUpdate = _Rip2PeerLastUpdate_Object(
    (1, 3, 6, 1, 2, 1, 23, 4, 1, 3),
    _Rip2PeerLastUpdate_Type()
)
rip2PeerLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rip2PeerLastUpdate.setStatus("mandatory")


class _Rip2PeerVersion_Type(Integer32):
    """Custom type rip2PeerVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Rip2PeerVersion_Type.__name__ = "Integer32"
_Rip2PeerVersion_Object = MibTableColumn
rip2PeerVersion = _Rip2PeerVersion_Object(
    (1, 3, 6, 1, 2, 1, 23, 4, 1, 4),
    _Rip2PeerVersion_Type()
)
rip2PeerVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rip2PeerVersion.setStatus("mandatory")
_Rip2PeerRcvBadPackets_Type = Counter32
_Rip2PeerRcvBadPackets_Object = MibTableColumn
rip2PeerRcvBadPackets = _Rip2PeerRcvBadPackets_Object(
    (1, 3, 6, 1, 2, 1, 23, 4, 1, 5),
    _Rip2PeerRcvBadPackets_Type()
)
rip2PeerRcvBadPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rip2PeerRcvBadPackets.setStatus("mandatory")
_Rip2PeerRcvBadRoutes_Type = Counter32
_Rip2PeerRcvBadRoutes_Object = MibTableColumn
rip2PeerRcvBadRoutes = _Rip2PeerRcvBadRoutes_Object(
    (1, 3, 6, 1, 2, 1, 23, 4, 1, 6),
    _Rip2PeerRcvBadRoutes_Type()
)
rip2PeerRcvBadRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rip2PeerRcvBadRoutes.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RFC1389-MIB",
    **{"RouteTag": RouteTag,
       "mgmt": mgmt,
       "mib-2": mib_2,
       "rip2": rip2,
       "rip2GlobalGroup": rip2GlobalGroup,
       "rip2GlobalRouteChanges": rip2GlobalRouteChanges,
       "rip2GlobalQueries": rip2GlobalQueries,
       "rip2IfStatTable": rip2IfStatTable,
       "rip2IfStatEntry": rip2IfStatEntry,
       "rip2IfStatAddress": rip2IfStatAddress,
       "rip2IfStatRcvBadPackets": rip2IfStatRcvBadPackets,
       "rip2IfStatRcvBadRoutes": rip2IfStatRcvBadRoutes,
       "rip2IfStatSentUpdates": rip2IfStatSentUpdates,
       "rip2IfStatStatus": rip2IfStatStatus,
       "rip2IfConfTable": rip2IfConfTable,
       "rip2IfConfEntry": rip2IfConfEntry,
       "rip2IfConfAddress": rip2IfConfAddress,
       "rip2IfConfDomain": rip2IfConfDomain,
       "rip2IfConfAuthType": rip2IfConfAuthType,
       "rip2IfConfAuthKey": rip2IfConfAuthKey,
       "rip2IfConfSend": rip2IfConfSend,
       "rip2IfConfReceive": rip2IfConfReceive,
       "rip2IfConfDefaultMetric": rip2IfConfDefaultMetric,
       "rip2IfConfStatus": rip2IfConfStatus,
       "rip2IfConfSrcAddress": rip2IfConfSrcAddress,
       "rip2PeerTable": rip2PeerTable,
       "rip2PeerEntry": rip2PeerEntry,
       "rip2PeerAddress": rip2PeerAddress,
       "rip2PeerDomain": rip2PeerDomain,
       "rip2PeerLastUpdate": rip2PeerLastUpdate,
       "rip2PeerVersion": rip2PeerVersion,
       "rip2PeerRcvBadPackets": rip2PeerRcvBadPackets,
       "rip2PeerRcvBadRoutes": rip2PeerRcvBadRoutes}
)
