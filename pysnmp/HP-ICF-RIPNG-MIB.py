# SNMP MIB module (HP-ICF-RIPNG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-RIPNG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:58:05 2024
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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpicfRipng = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 113)
)
hpicfRipng.setRevisions(
        ("2015-05-11 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfRipngNotifications_ObjectIdentity = ObjectIdentity
hpicfRipngNotifications = _HpicfRipngNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 113, 0)
)
_HpicfRipngObjects_ObjectIdentity = ObjectIdentity
hpicfRipngObjects = _HpicfRipngObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 113, 1)
)
_HpicfRipngBaseScalars_ObjectIdentity = ObjectIdentity
hpicfRipngBaseScalars = _HpicfRipngBaseScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 113, 1, 1)
)
_HpicfRipngGlobalRouteChanges_Type = Counter32
_HpicfRipngGlobalRouteChanges_Object = MibScalar
hpicfRipngGlobalRouteChanges = _HpicfRipngGlobalRouteChanges_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 113, 1, 1, 1),
    _HpicfRipngGlobalRouteChanges_Type()
)
hpicfRipngGlobalRouteChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRipngGlobalRouteChanges.setStatus("current")
_HpicfRipngGlobalQueries_Type = Counter32
_HpicfRipngGlobalQueries_Object = MibScalar
hpicfRipngGlobalQueries = _HpicfRipngGlobalQueries_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 113, 1, 1, 2),
    _HpicfRipngGlobalQueries_Type()
)
hpicfRipngGlobalQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRipngGlobalQueries.setStatus("current")


class _HpicfRipngAdminStatus_Type(Integer32):
    """Custom type hpicfRipngAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HpicfRipngAdminStatus_Type.__name__ = "Integer32"
_HpicfRipngAdminStatus_Object = MibScalar
hpicfRipngAdminStatus = _HpicfRipngAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 113, 1, 1, 3),
    _HpicfRipngAdminStatus_Type()
)
hpicfRipngAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfRipngAdminStatus.setStatus("current")


class _HpicfRipngDefaultMetric_Type(Integer32):
    """Custom type hpicfRipngDefaultMetric based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_HpicfRipngDefaultMetric_Type.__name__ = "Integer32"
_HpicfRipngDefaultMetric_Object = MibScalar
hpicfRipngDefaultMetric = _HpicfRipngDefaultMetric_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 113, 1, 1, 4),
    _HpicfRipngDefaultMetric_Type()
)
hpicfRipngDefaultMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfRipngDefaultMetric.setStatus("current")


class _HpicfRipngDistance_Type(Integer32):
    """Custom type hpicfRipngDistance based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HpicfRipngDistance_Type.__name__ = "Integer32"
_HpicfRipngDistance_Object = MibScalar
hpicfRipngDistance = _HpicfRipngDistance_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 113, 1, 1, 5),
    _HpicfRipngDistance_Type()
)
hpicfRipngDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfRipngDistance.setStatus("current")


class _HpicfRipngUpdateTime_Type(Unsigned32):
    """Custom type hpicfRipngUpdateTime based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 65535),
    )


_HpicfRipngUpdateTime_Type.__name__ = "Unsigned32"
_HpicfRipngUpdateTime_Object = MibScalar
hpicfRipngUpdateTime = _HpicfRipngUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 113, 1, 1, 6),
    _HpicfRipngUpdateTime_Type()
)
hpicfRipngUpdateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfRipngUpdateTime.setStatus("current")
if mibBuilder.loadTexts:
    hpicfRipngUpdateTime.setUnits("seconds")


class _HpicfRipngTimeoutTime_Type(Unsigned32):
    """Custom type hpicfRipngTimeoutTime based on Unsigned32"""
    defaultValue = 180

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 65535),
    )


_HpicfRipngTimeoutTime_Type.__name__ = "Unsigned32"
_HpicfRipngTimeoutTime_Object = MibScalar
hpicfRipngTimeoutTime = _HpicfRipngTimeoutTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 113, 1, 1, 7),
    _HpicfRipngTimeoutTime_Type()
)
hpicfRipngTimeoutTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfRipngTimeoutTime.setStatus("current")
if mibBuilder.loadTexts:
    hpicfRipngTimeoutTime.setUnits("seconds")


class _HpicfRipngGarbageCollectTime_Type(Unsigned32):
    """Custom type hpicfRipngGarbageCollectTime based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 65535),
    )


_HpicfRipngGarbageCollectTime_Type.__name__ = "Unsigned32"
_HpicfRipngGarbageCollectTime_Object = MibScalar
hpicfRipngGarbageCollectTime = _HpicfRipngGarbageCollectTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 113, 1, 1, 8),
    _HpicfRipngGarbageCollectTime_Type()
)
hpicfRipngGarbageCollectTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfRipngGarbageCollectTime.setStatus("current")
if mibBuilder.loadTexts:
    hpicfRipngGarbageCollectTime.setUnits("seconds")


class _HpicfRipngNotificationEnable_Type(OctetString):
    """Custom type hpicfRipngNotificationEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_HpicfRipngNotificationEnable_Type.__name__ = "OctetString"
_HpicfRipngNotificationEnable_Object = MibScalar
hpicfRipngNotificationEnable = _HpicfRipngNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 113, 1, 1, 9),
    _HpicfRipngNotificationEnable_Type()
)
hpicfRipngNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfRipngNotificationEnable.setStatus("current")
_HpicfRipngIfConfTable_Object = MibTable
hpicfRipngIfConfTable = _HpicfRipngIfConfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 113, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfRipngIfConfTable.setStatus("current")
_HpicfRipngIfConfEntry_Object = MibTableRow
hpicfRipngIfConfEntry = _HpicfRipngIfConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 113, 1, 2, 1)
)
hpicfRipngIfConfEntry.setIndexNames(
    (0, "HP-ICF-RIPNG-MIB", "hpicfRipngIfConfIndex"),
    (0, "HP-ICF-RIPNG-MIB", "hpicfRipngIfConfInstId"),
)
if mibBuilder.loadTexts:
    hpicfRipngIfConfEntry.setStatus("current")
_HpicfRipngIfConfIndex_Type = InterfaceIndex
_HpicfRipngIfConfIndex_Object = MibTableColumn
hpicfRipngIfConfIndex = _HpicfRipngIfConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 113, 1, 2, 1, 1),
    _HpicfRipngIfConfIndex_Type()
)
hpicfRipngIfConfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfRipngIfConfIndex.setStatus("current")


class _HpicfRipngIfConfInstId_Type(Integer32):
    """Custom type hpicfRipngIfConfInstId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpicfRipngIfConfInstId_Type.__name__ = "Integer32"
_HpicfRipngIfConfInstId_Object = MibTableColumn
hpicfRipngIfConfInstId = _HpicfRipngIfConfInstId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 113, 1, 2, 1, 2),
    _HpicfRipngIfConfInstId_Type()
)
hpicfRipngIfConfInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfRipngIfConfInstId.setStatus("current")


class _HpicfRipngIfConfMetric_Type(Integer32):
    """Custom type hpicfRipngIfConfMetric based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_HpicfRipngIfConfMetric_Type.__name__ = "Integer32"
_HpicfRipngIfConfMetric_Object = MibTableColumn
hpicfRipngIfConfMetric = _HpicfRipngIfConfMetric_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 113, 1, 2, 1, 3),
    _HpicfRipngIfConfMetric_Type()
)
hpicfRipngIfConfMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfRipngIfConfMetric.setStatus("current")
_HpicfRipngIfConfStatus_Type = RowStatus
_HpicfRipngIfConfStatus_Object = MibTableColumn
hpicfRipngIfConfStatus = _HpicfRipngIfConfStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 113, 1, 2, 1, 4),
    _HpicfRipngIfConfStatus_Type()
)
hpicfRipngIfConfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfRipngIfConfStatus.setStatus("current")
_HpicfRipngIfConfSrcAddressType_Type = InetAddressType
_HpicfRipngIfConfSrcAddressType_Object = MibTableColumn
hpicfRipngIfConfSrcAddressType = _HpicfRipngIfConfSrcAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 113, 1, 2, 1, 5),
    _HpicfRipngIfConfSrcAddressType_Type()
)
hpicfRipngIfConfSrcAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRipngIfConfSrcAddressType.setStatus("current")


class _HpicfRipngIfConfSrcAddress_Type(InetAddress):
    """Custom type hpicfRipngIfConfSrcAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_HpicfRipngIfConfSrcAddress_Type.__name__ = "InetAddress"
_HpicfRipngIfConfSrcAddress_Object = MibTableColumn
hpicfRipngIfConfSrcAddress = _HpicfRipngIfConfSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 113, 1, 2, 1, 6),
    _HpicfRipngIfConfSrcAddress_Type()
)
hpicfRipngIfConfSrcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRipngIfConfSrcAddress.setStatus("current")


class _HpicfRipngIfConfDoPoisonReverse_Type(TruthValue):
    """Custom type hpicfRipngIfConfDoPoisonReverse based on TruthValue"""


_HpicfRipngIfConfDoPoisonReverse_Object = MibTableColumn
hpicfRipngIfConfDoPoisonReverse = _HpicfRipngIfConfDoPoisonReverse_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 113, 1, 2, 1, 7),
    _HpicfRipngIfConfDoPoisonReverse_Type()
)
hpicfRipngIfConfDoPoisonReverse.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfRipngIfConfDoPoisonReverse.setStatus("current")
_HpicfRipngPeerTable_Object = MibTable
hpicfRipngPeerTable = _HpicfRipngPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 113, 1, 3)
)
if mibBuilder.loadTexts:
    hpicfRipngPeerTable.setStatus("current")
_HpicfRipngPeerEntry_Object = MibTableRow
hpicfRipngPeerEntry = _HpicfRipngPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 113, 1, 3, 1)
)
hpicfRipngPeerEntry.setIndexNames(
    (0, "HP-ICF-RIPNG-MIB", "hpicfRipngPeerAddressType"),
    (0, "HP-ICF-RIPNG-MIB", "hpicfRipngPeerAddress"),
)
if mibBuilder.loadTexts:
    hpicfRipngPeerEntry.setStatus("current")
_HpicfRipngPeerAddressType_Type = InetAddressType
_HpicfRipngPeerAddressType_Object = MibTableColumn
hpicfRipngPeerAddressType = _HpicfRipngPeerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 113, 1, 3, 1, 1),
    _HpicfRipngPeerAddressType_Type()
)
hpicfRipngPeerAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfRipngPeerAddressType.setStatus("current")


class _HpicfRipngPeerAddress_Type(InetAddress):
    """Custom type hpicfRipngPeerAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_HpicfRipngPeerAddress_Type.__name__ = "InetAddress"
_HpicfRipngPeerAddress_Object = MibTableColumn
hpicfRipngPeerAddress = _HpicfRipngPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 113, 1, 3, 1, 2),
    _HpicfRipngPeerAddress_Type()
)
hpicfRipngPeerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfRipngPeerAddress.setStatus("current")
_HpicfRipngPeerLastUpdate_Type = Unsigned32
_HpicfRipngPeerLastUpdate_Object = MibTableColumn
hpicfRipngPeerLastUpdate = _HpicfRipngPeerLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 113, 1, 3, 1, 3),
    _HpicfRipngPeerLastUpdate_Type()
)
hpicfRipngPeerLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRipngPeerLastUpdate.setStatus("current")
_HpicfRipngPeerRcvBadPackets_Type = Counter32
_HpicfRipngPeerRcvBadPackets_Object = MibTableColumn
hpicfRipngPeerRcvBadPackets = _HpicfRipngPeerRcvBadPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 113, 1, 3, 1, 4),
    _HpicfRipngPeerRcvBadPackets_Type()
)
hpicfRipngPeerRcvBadPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfRipngPeerRcvBadPackets.setStatus("current")
_HpicfRipngNotificationEntry_ObjectIdentity = ObjectIdentity
hpicfRipngNotificationEntry = _HpicfRipngNotificationEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 113, 1, 4)
)


class _HpicfRipngConfigErrorType_Type(Integer32):
    """Custom type hpicfRipngConfigErrorType based on Integer32"""
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
        *(("badField", 4),
          ("badHop", 3),
          ("badIPtype", 2),
          ("badVersion", 1),
          ("noError", 6),
          ("ownPkt", 5))
    )


_HpicfRipngConfigErrorType_Type.__name__ = "Integer32"
_HpicfRipngConfigErrorType_Object = MibScalar
hpicfRipngConfigErrorType = _HpicfRipngConfigErrorType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 113, 1, 4, 1),
    _HpicfRipngConfigErrorType_Type()
)
hpicfRipngConfigErrorType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfRipngConfigErrorType.setStatus("current")


class _HpicfRipngPacketType_Type(Integer32):
    """Custom type hpicfRipngPacketType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nullPacket", 3),
          ("request", 1),
          ("response", 2))
    )


_HpicfRipngPacketType_Type.__name__ = "Integer32"
_HpicfRipngPacketType_Object = MibScalar
hpicfRipngPacketType = _HpicfRipngPacketType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 113, 1, 4, 2),
    _HpicfRipngPacketType_Type()
)
hpicfRipngPacketType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfRipngPacketType.setStatus("current")
_HpicfRipngPacketSrcType_Type = InetAddressType
_HpicfRipngPacketSrcType_Object = MibScalar
hpicfRipngPacketSrcType = _HpicfRipngPacketSrcType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 113, 1, 4, 3),
    _HpicfRipngPacketSrcType_Type()
)
hpicfRipngPacketSrcType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfRipngPacketSrcType.setStatus("current")


class _HpicfRipngPacketSrc_Type(InetAddress):
    """Custom type hpicfRipngPacketSrc based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_HpicfRipngPacketSrc_Type.__name__ = "InetAddress"
_HpicfRipngPacketSrc_Object = MibScalar
hpicfRipngPacketSrc = _HpicfRipngPacketSrc_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 113, 1, 4, 4),
    _HpicfRipngPacketSrc_Type()
)
hpicfRipngPacketSrc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfRipngPacketSrc.setStatus("current")


class _HpicfRipngIfState_Type(Integer32):
    """Custom type hpicfRipngIfState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_HpicfRipngIfState_Type.__name__ = "Integer32"
_HpicfRipngIfState_Object = MibScalar
hpicfRipngIfState = _HpicfRipngIfState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 113, 1, 4, 5),
    _HpicfRipngIfState_Type()
)
hpicfRipngIfState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfRipngIfState.setStatus("current")
_HpicfRipngConformance_ObjectIdentity = ObjectIdentity
hpicfRipngConformance = _HpicfRipngConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 113, 2)
)
_HpicfRipngCompliances_ObjectIdentity = ObjectIdentity
hpicfRipngCompliances = _HpicfRipngCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 113, 2, 1)
)
_HpicfRipngGroups_ObjectIdentity = ObjectIdentity
hpicfRipngGroups = _HpicfRipngGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 113, 2, 2)
)

# Managed Objects groups

hpicfRipngBaseScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 113, 2, 2, 1)
)
hpicfRipngBaseScalarsGroup.setObjects(
      *(("HP-ICF-RIPNG-MIB", "hpicfRipngGlobalRouteChanges"),
        ("HP-ICF-RIPNG-MIB", "hpicfRipngGlobalQueries"),
        ("HP-ICF-RIPNG-MIB", "hpicfRipngAdminStatus"),
        ("HP-ICF-RIPNG-MIB", "hpicfRipngDefaultMetric"),
        ("HP-ICF-RIPNG-MIB", "hpicfRipngDistance"),
        ("HP-ICF-RIPNG-MIB", "hpicfRipngUpdateTime"),
        ("HP-ICF-RIPNG-MIB", "hpicfRipngTimeoutTime"),
        ("HP-ICF-RIPNG-MIB", "hpicfRipngGarbageCollectTime"),
        ("HP-ICF-RIPNG-MIB", "hpicfRipngNotificationEnable"))
)
if mibBuilder.loadTexts:
    hpicfRipngBaseScalarsGroup.setStatus("current")

hpicfRipngIfConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 113, 2, 2, 2)
)
hpicfRipngIfConfGroup.setObjects(
      *(("HP-ICF-RIPNG-MIB", "hpicfRipngIfConfMetric"),
        ("HP-ICF-RIPNG-MIB", "hpicfRipngIfConfStatus"),
        ("HP-ICF-RIPNG-MIB", "hpicfRipngIfConfSrcAddressType"),
        ("HP-ICF-RIPNG-MIB", "hpicfRipngIfConfSrcAddress"),
        ("HP-ICF-RIPNG-MIB", "hpicfRipngIfConfDoPoisonReverse"))
)
if mibBuilder.loadTexts:
    hpicfRipngIfConfGroup.setStatus("current")

hpicfRipngPeerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 113, 2, 2, 3)
)
hpicfRipngPeerGroup.setObjects(
      *(("HP-ICF-RIPNG-MIB", "hpicfRipngPeerLastUpdate"),
        ("HP-ICF-RIPNG-MIB", "hpicfRipngPeerRcvBadPackets"))
)
if mibBuilder.loadTexts:
    hpicfRipngPeerGroup.setStatus("current")

hpicfRipngNotificationObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 113, 2, 2, 4)
)
hpicfRipngNotificationObjectGroup.setObjects(
      *(("HP-ICF-RIPNG-MIB", "hpicfRipngConfigErrorType"),
        ("HP-ICF-RIPNG-MIB", "hpicfRipngPacketType"),
        ("HP-ICF-RIPNG-MIB", "hpicfRipngPacketSrcType"),
        ("HP-ICF-RIPNG-MIB", "hpicfRipngPacketSrc"),
        ("HP-ICF-RIPNG-MIB", "hpicfRipngIfState"))
)
if mibBuilder.loadTexts:
    hpicfRipngNotificationObjectGroup.setStatus("current")


# Notification objects

hpicfRipngIfStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 113, 0, 1)
)
hpicfRipngIfStateChange.setObjects(
      *(("HP-ICF-RIPNG-MIB", "hpicfRipngIfConfSrcAddress"),
        ("HP-ICF-RIPNG-MIB", "hpicfRipngIfState"))
)
if mibBuilder.loadTexts:
    hpicfRipngIfStateChange.setStatus(
        "current"
    )

hpicfRipngIfConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 113, 0, 2)
)
hpicfRipngIfConfigError.setObjects(
      *(("HP-ICF-RIPNG-MIB", "hpicfRipngIfConfSrcAddress"),
        ("HP-ICF-RIPNG-MIB", "hpicfRipngIfState"),
        ("HP-ICF-RIPNG-MIB", "hpicfRipngPacketSrc"),
        ("HP-ICF-RIPNG-MIB", "hpicfRipngConfigErrorType"),
        ("HP-ICF-RIPNG-MIB", "hpicfRipngPacketType"))
)
if mibBuilder.loadTexts:
    hpicfRipngIfConfigError.setStatus(
        "current"
    )

hpicfRipngIfRxBadPacket = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 113, 0, 3)
)
hpicfRipngIfRxBadPacket.setObjects(
      *(("HP-ICF-RIPNG-MIB", "hpicfRipngIfConfSrcAddress"),
        ("HP-ICF-RIPNG-MIB", "hpicfRipngIfState"),
        ("HP-ICF-RIPNG-MIB", "hpicfRipngPacketSrc"),
        ("HP-ICF-RIPNG-MIB", "hpicfRipngPacketType"))
)
if mibBuilder.loadTexts:
    hpicfRipngIfRxBadPacket.setStatus(
        "current"
    )


# Notifications groups

hpicfRipngNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 113, 2, 2, 5)
)
hpicfRipngNotificationGroup.setObjects(
      *(("HP-ICF-RIPNG-MIB", "hpicfRipngIfStateChange"),
        ("HP-ICF-RIPNG-MIB", "hpicfRipngIfConfigError"),
        ("HP-ICF-RIPNG-MIB", "hpicfRipngIfRxBadPacket"))
)
if mibBuilder.loadTexts:
    hpicfRipngNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hpicfRipngCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 113, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfRipngCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-RIPNG-MIB",
    **{"hpicfRipng": hpicfRipng,
       "hpicfRipngNotifications": hpicfRipngNotifications,
       "hpicfRipngIfStateChange": hpicfRipngIfStateChange,
       "hpicfRipngIfConfigError": hpicfRipngIfConfigError,
       "hpicfRipngIfRxBadPacket": hpicfRipngIfRxBadPacket,
       "hpicfRipngObjects": hpicfRipngObjects,
       "hpicfRipngBaseScalars": hpicfRipngBaseScalars,
       "hpicfRipngGlobalRouteChanges": hpicfRipngGlobalRouteChanges,
       "hpicfRipngGlobalQueries": hpicfRipngGlobalQueries,
       "hpicfRipngAdminStatus": hpicfRipngAdminStatus,
       "hpicfRipngDefaultMetric": hpicfRipngDefaultMetric,
       "hpicfRipngDistance": hpicfRipngDistance,
       "hpicfRipngUpdateTime": hpicfRipngUpdateTime,
       "hpicfRipngTimeoutTime": hpicfRipngTimeoutTime,
       "hpicfRipngGarbageCollectTime": hpicfRipngGarbageCollectTime,
       "hpicfRipngNotificationEnable": hpicfRipngNotificationEnable,
       "hpicfRipngIfConfTable": hpicfRipngIfConfTable,
       "hpicfRipngIfConfEntry": hpicfRipngIfConfEntry,
       "hpicfRipngIfConfIndex": hpicfRipngIfConfIndex,
       "hpicfRipngIfConfInstId": hpicfRipngIfConfInstId,
       "hpicfRipngIfConfMetric": hpicfRipngIfConfMetric,
       "hpicfRipngIfConfStatus": hpicfRipngIfConfStatus,
       "hpicfRipngIfConfSrcAddressType": hpicfRipngIfConfSrcAddressType,
       "hpicfRipngIfConfSrcAddress": hpicfRipngIfConfSrcAddress,
       "hpicfRipngIfConfDoPoisonReverse": hpicfRipngIfConfDoPoisonReverse,
       "hpicfRipngPeerTable": hpicfRipngPeerTable,
       "hpicfRipngPeerEntry": hpicfRipngPeerEntry,
       "hpicfRipngPeerAddressType": hpicfRipngPeerAddressType,
       "hpicfRipngPeerAddress": hpicfRipngPeerAddress,
       "hpicfRipngPeerLastUpdate": hpicfRipngPeerLastUpdate,
       "hpicfRipngPeerRcvBadPackets": hpicfRipngPeerRcvBadPackets,
       "hpicfRipngNotificationEntry": hpicfRipngNotificationEntry,
       "hpicfRipngConfigErrorType": hpicfRipngConfigErrorType,
       "hpicfRipngPacketType": hpicfRipngPacketType,
       "hpicfRipngPacketSrcType": hpicfRipngPacketSrcType,
       "hpicfRipngPacketSrc": hpicfRipngPacketSrc,
       "hpicfRipngIfState": hpicfRipngIfState,
       "hpicfRipngConformance": hpicfRipngConformance,
       "hpicfRipngCompliances": hpicfRipngCompliances,
       "hpicfRipngCompliance": hpicfRipngCompliance,
       "hpicfRipngGroups": hpicfRipngGroups,
       "hpicfRipngBaseScalarsGroup": hpicfRipngBaseScalarsGroup,
       "hpicfRipngIfConfGroup": hpicfRipngIfConfGroup,
       "hpicfRipngPeerGroup": hpicfRipngPeerGroup,
       "hpicfRipngNotificationObjectGroup": hpicfRipngNotificationObjectGroup,
       "hpicfRipngNotificationGroup": hpicfRipngNotificationGroup}
)
