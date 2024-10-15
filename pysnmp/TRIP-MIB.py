# SNMP MIB module (TRIP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TRIP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:07:44 2024
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

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(applIndex,
 applRFC2788Group) = mibBuilder.importSymbols(
    "NETWORK-SERVICES-MIB",
    "applIndex",
    "applRFC2788Group")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DateAndTime,
 DisplayString,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")

(TripAddressFamily,
 TripAppProtocol,
 TripCommunityId,
 TripId,
 TripItad,
 TripProtocolVersion,
 TripSendReceiveMode) = mibBuilder.importSymbols(
    "TRIP-TC-MIB",
    "TripAddressFamily",
    "TripAppProtocol",
    "TripCommunityId",
    "TripId",
    "TripItad",
    "TripProtocolVersion",
    "TripSendReceiveMode")


# MODULE-IDENTITY

tripMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 116)
)
tripMIB.setRevisions(
        ("2004-09-02 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TripMIBNotifications_ObjectIdentity = ObjectIdentity
tripMIBNotifications = _TripMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 116, 0)
)
_TripMIBObjects_ObjectIdentity = ObjectIdentity
tripMIBObjects = _TripMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 116, 1)
)
_TripCfgTable_Object = MibTable
tripCfgTable = _TripCfgTable_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 1)
)
if mibBuilder.loadTexts:
    tripCfgTable.setStatus("current")
_TripCfgEntry_Object = MibTableRow
tripCfgEntry = _TripCfgEntry_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 1, 1)
)
tripCfgEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
)
if mibBuilder.loadTexts:
    tripCfgEntry.setStatus("current")
_TripCfgProtocolVersion_Type = TripProtocolVersion
_TripCfgProtocolVersion_Object = MibTableColumn
tripCfgProtocolVersion = _TripCfgProtocolVersion_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 1, 1, 1),
    _TripCfgProtocolVersion_Type()
)
tripCfgProtocolVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tripCfgProtocolVersion.setStatus("current")
_TripCfgItad_Type = TripItad
_TripCfgItad_Object = MibTableColumn
tripCfgItad = _TripCfgItad_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 1, 1, 2),
    _TripCfgItad_Type()
)
tripCfgItad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tripCfgItad.setStatus("current")
_TripCfgIdentifier_Type = TripId
_TripCfgIdentifier_Object = MibTableColumn
tripCfgIdentifier = _TripCfgIdentifier_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 1, 1, 3),
    _TripCfgIdentifier_Type()
)
tripCfgIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tripCfgIdentifier.setStatus("current")


class _TripCfgAdminStatus_Type(Integer32):
    """Custom type tripCfgAdminStatus based on Integer32"""
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


_TripCfgAdminStatus_Type.__name__ = "Integer32"
_TripCfgAdminStatus_Object = MibTableColumn
tripCfgAdminStatus = _TripCfgAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 1, 1, 4),
    _TripCfgAdminStatus_Type()
)
tripCfgAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tripCfgAdminStatus.setStatus("current")


class _TripCfgOperStatus_Type(Integer32):
    """Custom type tripCfgOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("faulty", 3),
          ("unknown", 0),
          ("up", 1))
    )


_TripCfgOperStatus_Type.__name__ = "Integer32"
_TripCfgOperStatus_Object = MibTableColumn
tripCfgOperStatus = _TripCfgOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 1, 1, 5),
    _TripCfgOperStatus_Type()
)
tripCfgOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tripCfgOperStatus.setStatus("current")
_TripCfgAddrIAddrType_Type = InetAddressType
_TripCfgAddrIAddrType_Object = MibTableColumn
tripCfgAddrIAddrType = _TripCfgAddrIAddrType_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 1, 1, 6),
    _TripCfgAddrIAddrType_Type()
)
tripCfgAddrIAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tripCfgAddrIAddrType.setStatus("current")
_TripCfgAddr_Type = InetAddress
_TripCfgAddr_Object = MibTableColumn
tripCfgAddr = _TripCfgAddr_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 1, 1, 7),
    _TripCfgAddr_Type()
)
tripCfgAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tripCfgAddr.setStatus("current")
_TripCfgPort_Type = InetPortNumber
_TripCfgPort_Object = MibTableColumn
tripCfgPort = _TripCfgPort_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 1, 1, 8),
    _TripCfgPort_Type()
)
tripCfgPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tripCfgPort.setStatus("current")


class _TripCfgMinItadOriginationInterval_Type(Unsigned32):
    """Custom type tripCfgMinItadOriginationInterval based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TripCfgMinItadOriginationInterval_Type.__name__ = "Unsigned32"
_TripCfgMinItadOriginationInterval_Object = MibTableColumn
tripCfgMinItadOriginationInterval = _TripCfgMinItadOriginationInterval_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 1, 1, 9),
    _TripCfgMinItadOriginationInterval_Type()
)
tripCfgMinItadOriginationInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tripCfgMinItadOriginationInterval.setStatus("current")
if mibBuilder.loadTexts:
    tripCfgMinItadOriginationInterval.setUnits("Seconds")


class _TripCfgMinRouteAdvertisementInterval_Type(Unsigned32):
    """Custom type tripCfgMinRouteAdvertisementInterval based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TripCfgMinRouteAdvertisementInterval_Type.__name__ = "Unsigned32"
_TripCfgMinRouteAdvertisementInterval_Object = MibTableColumn
tripCfgMinRouteAdvertisementInterval = _TripCfgMinRouteAdvertisementInterval_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 1, 1, 10),
    _TripCfgMinRouteAdvertisementInterval_Type()
)
tripCfgMinRouteAdvertisementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tripCfgMinRouteAdvertisementInterval.setStatus("current")
if mibBuilder.loadTexts:
    tripCfgMinRouteAdvertisementInterval.setUnits("Seconds")


class _TripCfgMaxPurgeTime_Type(Unsigned32):
    """Custom type tripCfgMaxPurgeTime based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TripCfgMaxPurgeTime_Type.__name__ = "Unsigned32"
_TripCfgMaxPurgeTime_Object = MibTableColumn
tripCfgMaxPurgeTime = _TripCfgMaxPurgeTime_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 1, 1, 11),
    _TripCfgMaxPurgeTime_Type()
)
tripCfgMaxPurgeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tripCfgMaxPurgeTime.setStatus("current")
if mibBuilder.loadTexts:
    tripCfgMaxPurgeTime.setUnits("Seconds")


class _TripCfgDisableTime_Type(Unsigned32):
    """Custom type tripCfgDisableTime based on Unsigned32"""
    defaultValue = 180

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TripCfgDisableTime_Type.__name__ = "Unsigned32"
_TripCfgDisableTime_Object = MibTableColumn
tripCfgDisableTime = _TripCfgDisableTime_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 1, 1, 12),
    _TripCfgDisableTime_Type()
)
tripCfgDisableTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tripCfgDisableTime.setStatus("current")
if mibBuilder.loadTexts:
    tripCfgDisableTime.setUnits("Seconds")
_TripCfgSendReceiveMode_Type = TripSendReceiveMode
_TripCfgSendReceiveMode_Object = MibTableColumn
tripCfgSendReceiveMode = _TripCfgSendReceiveMode_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 1, 1, 13),
    _TripCfgSendReceiveMode_Type()
)
tripCfgSendReceiveMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tripCfgSendReceiveMode.setStatus("current")


class _TripCfgStorage_Type(StorageType):
    """Custom type tripCfgStorage based on StorageType"""


_TripCfgStorage_Object = MibTableColumn
tripCfgStorage = _TripCfgStorage_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 1, 1, 14),
    _TripCfgStorage_Type()
)
tripCfgStorage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tripCfgStorage.setStatus("current")
_TripRouteTypeTable_Object = MibTable
tripRouteTypeTable = _TripRouteTypeTable_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 2)
)
if mibBuilder.loadTexts:
    tripRouteTypeTable.setStatus("current")
_TripRouteTypeEntry_Object = MibTableRow
tripRouteTypeEntry = _TripRouteTypeEntry_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 2, 1)
)
tripRouteTypeEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
    (0, "TRIP-MIB", "tripRouteTypeAddrInetType"),
    (0, "TRIP-MIB", "tripRouteTypeAddr"),
    (0, "TRIP-MIB", "tripRouteTypePort"),
    (0, "TRIP-MIB", "tripRouteTypeProtocolId"),
    (0, "TRIP-MIB", "tripRouteTypeAddrFamilyId"),
)
if mibBuilder.loadTexts:
    tripRouteTypeEntry.setStatus("current")
_TripRouteTypeAddrInetType_Type = InetAddressType
_TripRouteTypeAddrInetType_Object = MibTableColumn
tripRouteTypeAddrInetType = _TripRouteTypeAddrInetType_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 2, 1, 1),
    _TripRouteTypeAddrInetType_Type()
)
tripRouteTypeAddrInetType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tripRouteTypeAddrInetType.setStatus("current")
_TripRouteTypeAddr_Type = InetAddress
_TripRouteTypeAddr_Object = MibTableColumn
tripRouteTypeAddr = _TripRouteTypeAddr_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 2, 1, 2),
    _TripRouteTypeAddr_Type()
)
tripRouteTypeAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tripRouteTypeAddr.setStatus("current")
_TripRouteTypePort_Type = InetPortNumber
_TripRouteTypePort_Object = MibTableColumn
tripRouteTypePort = _TripRouteTypePort_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 2, 1, 3),
    _TripRouteTypePort_Type()
)
tripRouteTypePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tripRouteTypePort.setStatus("current")
_TripRouteTypeProtocolId_Type = TripAppProtocol
_TripRouteTypeProtocolId_Object = MibTableColumn
tripRouteTypeProtocolId = _TripRouteTypeProtocolId_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 2, 1, 4),
    _TripRouteTypeProtocolId_Type()
)
tripRouteTypeProtocolId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tripRouteTypeProtocolId.setStatus("current")
_TripRouteTypeAddrFamilyId_Type = TripAddressFamily
_TripRouteTypeAddrFamilyId_Object = MibTableColumn
tripRouteTypeAddrFamilyId = _TripRouteTypeAddrFamilyId_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 2, 1, 5),
    _TripRouteTypeAddrFamilyId_Type()
)
tripRouteTypeAddrFamilyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tripRouteTypeAddrFamilyId.setStatus("current")


class _TripRouteTypePeer_Type(Integer32):
    """Custom type tripRouteTypePeer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_TripRouteTypePeer_Type.__name__ = "Integer32"
_TripRouteTypePeer_Object = MibTableColumn
tripRouteTypePeer = _TripRouteTypePeer_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 2, 1, 6),
    _TripRouteTypePeer_Type()
)
tripRouteTypePeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tripRouteTypePeer.setStatus("current")
_TripSupportedCommunityTable_Object = MibTable
tripSupportedCommunityTable = _TripSupportedCommunityTable_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 3)
)
if mibBuilder.loadTexts:
    tripSupportedCommunityTable.setStatus("current")
_TripSupportedCommunityEntry_Object = MibTableRow
tripSupportedCommunityEntry = _TripSupportedCommunityEntry_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 3, 1)
)
tripSupportedCommunityEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
    (0, "TRIP-MIB", "tripSupportedCommunityId"),
)
if mibBuilder.loadTexts:
    tripSupportedCommunityEntry.setStatus("current")
_TripSupportedCommunityId_Type = TripCommunityId
_TripSupportedCommunityId_Object = MibTableColumn
tripSupportedCommunityId = _TripSupportedCommunityId_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 3, 1, 1),
    _TripSupportedCommunityId_Type()
)
tripSupportedCommunityId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tripSupportedCommunityId.setStatus("current")
_TripSupportedCommunityItad_Type = TripItad
_TripSupportedCommunityItad_Object = MibTableColumn
tripSupportedCommunityItad = _TripSupportedCommunityItad_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 3, 1, 2),
    _TripSupportedCommunityItad_Type()
)
tripSupportedCommunityItad.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tripSupportedCommunityItad.setStatus("current")


class _TripSupportedCommunityStorage_Type(StorageType):
    """Custom type tripSupportedCommunityStorage based on StorageType"""


_TripSupportedCommunityStorage_Object = MibTableColumn
tripSupportedCommunityStorage = _TripSupportedCommunityStorage_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 3, 1, 3),
    _TripSupportedCommunityStorage_Type()
)
tripSupportedCommunityStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tripSupportedCommunityStorage.setStatus("current")
_TripSupportedCommunityRowStatus_Type = RowStatus
_TripSupportedCommunityRowStatus_Object = MibTableColumn
tripSupportedCommunityRowStatus = _TripSupportedCommunityRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 3, 1, 4),
    _TripSupportedCommunityRowStatus_Type()
)
tripSupportedCommunityRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tripSupportedCommunityRowStatus.setStatus("current")
_TripPeerTable_Object = MibTable
tripPeerTable = _TripPeerTable_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 4)
)
if mibBuilder.loadTexts:
    tripPeerTable.setStatus("current")
_TripPeerEntry_Object = MibTableRow
tripPeerEntry = _TripPeerEntry_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 4, 1)
)
tripPeerEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
    (0, "TRIP-MIB", "tripPeerRemoteAddrInetType"),
    (0, "TRIP-MIB", "tripPeerRemoteAddr"),
    (0, "TRIP-MIB", "tripPeerRemotePort"),
)
if mibBuilder.loadTexts:
    tripPeerEntry.setStatus("current")
_TripPeerRemoteAddrInetType_Type = InetAddressType
_TripPeerRemoteAddrInetType_Object = MibTableColumn
tripPeerRemoteAddrInetType = _TripPeerRemoteAddrInetType_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 4, 1, 1),
    _TripPeerRemoteAddrInetType_Type()
)
tripPeerRemoteAddrInetType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tripPeerRemoteAddrInetType.setStatus("current")
_TripPeerRemoteAddr_Type = InetAddress
_TripPeerRemoteAddr_Object = MibTableColumn
tripPeerRemoteAddr = _TripPeerRemoteAddr_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 4, 1, 2),
    _TripPeerRemoteAddr_Type()
)
tripPeerRemoteAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tripPeerRemoteAddr.setStatus("current")
_TripPeerRemotePort_Type = InetPortNumber
_TripPeerRemotePort_Object = MibTableColumn
tripPeerRemotePort = _TripPeerRemotePort_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 4, 1, 3),
    _TripPeerRemotePort_Type()
)
tripPeerRemotePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tripPeerRemotePort.setStatus("current")
_TripPeerIdentifier_Type = TripId
_TripPeerIdentifier_Object = MibTableColumn
tripPeerIdentifier = _TripPeerIdentifier_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 4, 1, 4),
    _TripPeerIdentifier_Type()
)
tripPeerIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tripPeerIdentifier.setStatus("current")


class _TripPeerState_Type(Integer32):
    """Custom type tripPeerState based on Integer32"""
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
        *(("active", 3),
          ("connect", 2),
          ("established", 6),
          ("idle", 1),
          ("openConfirm", 5),
          ("openSent", 4))
    )


_TripPeerState_Type.__name__ = "Integer32"
_TripPeerState_Object = MibTableColumn
tripPeerState = _TripPeerState_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 4, 1, 5),
    _TripPeerState_Type()
)
tripPeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tripPeerState.setStatus("current")


class _TripPeerAdminStatus_Type(Integer32):
    """Custom type tripPeerAdminStatus based on Integer32"""
    defaultValue = 1

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


_TripPeerAdminStatus_Type.__name__ = "Integer32"
_TripPeerAdminStatus_Object = MibTableColumn
tripPeerAdminStatus = _TripPeerAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 4, 1, 6),
    _TripPeerAdminStatus_Type()
)
tripPeerAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tripPeerAdminStatus.setStatus("current")
_TripPeerNegotiatedVersion_Type = TripProtocolVersion
_TripPeerNegotiatedVersion_Object = MibTableColumn
tripPeerNegotiatedVersion = _TripPeerNegotiatedVersion_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 4, 1, 7),
    _TripPeerNegotiatedVersion_Type()
)
tripPeerNegotiatedVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tripPeerNegotiatedVersion.setStatus("current")
_TripPeerSendReceiveMode_Type = TripSendReceiveMode
_TripPeerSendReceiveMode_Object = MibTableColumn
tripPeerSendReceiveMode = _TripPeerSendReceiveMode_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 4, 1, 8),
    _TripPeerSendReceiveMode_Type()
)
tripPeerSendReceiveMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tripPeerSendReceiveMode.setStatus("current")
_TripPeerRemoteItad_Type = TripItad
_TripPeerRemoteItad_Object = MibTableColumn
tripPeerRemoteItad = _TripPeerRemoteItad_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 4, 1, 9),
    _TripPeerRemoteItad_Type()
)
tripPeerRemoteItad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tripPeerRemoteItad.setStatus("current")


class _TripPeerConnectRetryInterval_Type(Unsigned32):
    """Custom type tripPeerConnectRetryInterval based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TripPeerConnectRetryInterval_Type.__name__ = "Unsigned32"
_TripPeerConnectRetryInterval_Object = MibTableColumn
tripPeerConnectRetryInterval = _TripPeerConnectRetryInterval_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 4, 1, 10),
    _TripPeerConnectRetryInterval_Type()
)
tripPeerConnectRetryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tripPeerConnectRetryInterval.setStatus("current")
if mibBuilder.loadTexts:
    tripPeerConnectRetryInterval.setUnits("Seconds")


class _TripPeerMaxRetryInterval_Type(Unsigned32):
    """Custom type tripPeerMaxRetryInterval based on Unsigned32"""
    defaultValue = 360

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TripPeerMaxRetryInterval_Type.__name__ = "Unsigned32"
_TripPeerMaxRetryInterval_Object = MibTableColumn
tripPeerMaxRetryInterval = _TripPeerMaxRetryInterval_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 4, 1, 11),
    _TripPeerMaxRetryInterval_Type()
)
tripPeerMaxRetryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tripPeerMaxRetryInterval.setStatus("current")
if mibBuilder.loadTexts:
    tripPeerMaxRetryInterval.setUnits("Seconds")


class _TripPeerHoldTime_Type(Unsigned32):
    """Custom type tripPeerHoldTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TripPeerHoldTime_Type.__name__ = "Unsigned32"
_TripPeerHoldTime_Object = MibTableColumn
tripPeerHoldTime = _TripPeerHoldTime_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 4, 1, 12),
    _TripPeerHoldTime_Type()
)
tripPeerHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tripPeerHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    tripPeerHoldTime.setUnits("Seconds")


class _TripPeerKeepAlive_Type(Unsigned32):
    """Custom type tripPeerKeepAlive based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TripPeerKeepAlive_Type.__name__ = "Unsigned32"
_TripPeerKeepAlive_Object = MibTableColumn
tripPeerKeepAlive = _TripPeerKeepAlive_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 4, 1, 13),
    _TripPeerKeepAlive_Type()
)
tripPeerKeepAlive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tripPeerKeepAlive.setStatus("current")
if mibBuilder.loadTexts:
    tripPeerKeepAlive.setUnits("Seconds")


class _TripPeerHoldTimeConfigured_Type(Unsigned32):
    """Custom type tripPeerHoldTimeConfigured based on Unsigned32"""
    defaultValue = 240

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 65535),
    )


_TripPeerHoldTimeConfigured_Type.__name__ = "Unsigned32"
_TripPeerHoldTimeConfigured_Object = MibTableColumn
tripPeerHoldTimeConfigured = _TripPeerHoldTimeConfigured_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 4, 1, 14),
    _TripPeerHoldTimeConfigured_Type()
)
tripPeerHoldTimeConfigured.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tripPeerHoldTimeConfigured.setStatus("current")
if mibBuilder.loadTexts:
    tripPeerHoldTimeConfigured.setUnits("Seconds")


class _TripPeerKeepAliveConfigured_Type(Unsigned32):
    """Custom type tripPeerKeepAliveConfigured based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TripPeerKeepAliveConfigured_Type.__name__ = "Unsigned32"
_TripPeerKeepAliveConfigured_Object = MibTableColumn
tripPeerKeepAliveConfigured = _TripPeerKeepAliveConfigured_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 4, 1, 15),
    _TripPeerKeepAliveConfigured_Type()
)
tripPeerKeepAliveConfigured.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tripPeerKeepAliveConfigured.setStatus("current")
if mibBuilder.loadTexts:
    tripPeerKeepAliveConfigured.setUnits("Seconds")


class _TripPeerMaxPurgeTime_Type(Unsigned32):
    """Custom type tripPeerMaxPurgeTime based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TripPeerMaxPurgeTime_Type.__name__ = "Unsigned32"
_TripPeerMaxPurgeTime_Object = MibTableColumn
tripPeerMaxPurgeTime = _TripPeerMaxPurgeTime_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 4, 1, 16),
    _TripPeerMaxPurgeTime_Type()
)
tripPeerMaxPurgeTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tripPeerMaxPurgeTime.setStatus("current")
if mibBuilder.loadTexts:
    tripPeerMaxPurgeTime.setUnits("Seconds")


class _TripPeerDisableTime_Type(Unsigned32):
    """Custom type tripPeerDisableTime based on Unsigned32"""
    defaultValue = 180

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TripPeerDisableTime_Type.__name__ = "Unsigned32"
_TripPeerDisableTime_Object = MibTableColumn
tripPeerDisableTime = _TripPeerDisableTime_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 4, 1, 17),
    _TripPeerDisableTime_Type()
)
tripPeerDisableTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tripPeerDisableTime.setStatus("current")
if mibBuilder.loadTexts:
    tripPeerDisableTime.setUnits("Seconds")


class _TripPeerLearned_Type(TruthValue):
    """Custom type tripPeerLearned based on TruthValue"""


_TripPeerLearned_Object = MibTableColumn
tripPeerLearned = _TripPeerLearned_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 4, 1, 18),
    _TripPeerLearned_Type()
)
tripPeerLearned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tripPeerLearned.setStatus("current")


class _TripPeerStorage_Type(StorageType):
    """Custom type tripPeerStorage based on StorageType"""


_TripPeerStorage_Object = MibTableColumn
tripPeerStorage = _TripPeerStorage_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 4, 1, 19),
    _TripPeerStorage_Type()
)
tripPeerStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tripPeerStorage.setStatus("current")
_TripPeerRowStatus_Type = RowStatus
_TripPeerRowStatus_Object = MibTableColumn
tripPeerRowStatus = _TripPeerRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 4, 1, 20),
    _TripPeerRowStatus_Type()
)
tripPeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tripPeerRowStatus.setStatus("current")
_TripPeerStatisticsTable_Object = MibTable
tripPeerStatisticsTable = _TripPeerStatisticsTable_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 5)
)
if mibBuilder.loadTexts:
    tripPeerStatisticsTable.setStatus("current")
_TripPeerStatisticsEntry_Object = MibTableRow
tripPeerStatisticsEntry = _TripPeerStatisticsEntry_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 5, 1)
)
if mibBuilder.loadTexts:
    tripPeerStatisticsEntry.setStatus("current")
_TripPeerInUpdates_Type = Counter32
_TripPeerInUpdates_Object = MibTableColumn
tripPeerInUpdates = _TripPeerInUpdates_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 5, 1, 1),
    _TripPeerInUpdates_Type()
)
tripPeerInUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tripPeerInUpdates.setStatus("current")
_TripPeerOutUpdates_Type = Counter32
_TripPeerOutUpdates_Object = MibTableColumn
tripPeerOutUpdates = _TripPeerOutUpdates_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 5, 1, 2),
    _TripPeerOutUpdates_Type()
)
tripPeerOutUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tripPeerOutUpdates.setStatus("current")
_TripPeerInTotalMessages_Type = Counter32
_TripPeerInTotalMessages_Object = MibTableColumn
tripPeerInTotalMessages = _TripPeerInTotalMessages_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 5, 1, 3),
    _TripPeerInTotalMessages_Type()
)
tripPeerInTotalMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tripPeerInTotalMessages.setStatus("current")
_TripPeerOutTotalMessages_Type = Counter32
_TripPeerOutTotalMessages_Object = MibTableColumn
tripPeerOutTotalMessages = _TripPeerOutTotalMessages_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 5, 1, 4),
    _TripPeerOutTotalMessages_Type()
)
tripPeerOutTotalMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tripPeerOutTotalMessages.setStatus("current")
_TripPeerFsmEstablishedTransitions_Type = Counter32
_TripPeerFsmEstablishedTransitions_Object = MibTableColumn
tripPeerFsmEstablishedTransitions = _TripPeerFsmEstablishedTransitions_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 5, 1, 5),
    _TripPeerFsmEstablishedTransitions_Type()
)
tripPeerFsmEstablishedTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tripPeerFsmEstablishedTransitions.setStatus("current")
_TripPeerFsmEstablishedTime_Type = DateAndTime
_TripPeerFsmEstablishedTime_Object = MibTableColumn
tripPeerFsmEstablishedTime = _TripPeerFsmEstablishedTime_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 5, 1, 6),
    _TripPeerFsmEstablishedTime_Type()
)
tripPeerFsmEstablishedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tripPeerFsmEstablishedTime.setStatus("current")
_TripPeerInUpdateElapsedTime_Type = TimeInterval
_TripPeerInUpdateElapsedTime_Object = MibTableColumn
tripPeerInUpdateElapsedTime = _TripPeerInUpdateElapsedTime_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 5, 1, 7),
    _TripPeerInUpdateElapsedTime_Type()
)
tripPeerInUpdateElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tripPeerInUpdateElapsedTime.setStatus("current")
_TripPeerStateChangeTime_Type = TimeStamp
_TripPeerStateChangeTime_Object = MibTableColumn
tripPeerStateChangeTime = _TripPeerStateChangeTime_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 5, 1, 8),
    _TripPeerStateChangeTime_Type()
)
tripPeerStateChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tripPeerStateChangeTime.setStatus("current")
_TripRouteTable_Object = MibTable
tripRouteTable = _TripRouteTable_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 6)
)
if mibBuilder.loadTexts:
    tripRouteTable.setStatus("current")
_TripRouteEntry_Object = MibTableRow
tripRouteEntry = _TripRouteEntry_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 6, 1)
)
tripRouteEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
    (0, "TRIP-MIB", "tripRouteAppProtocol"),
    (0, "TRIP-MIB", "tripRouteAddressFamily"),
    (0, "TRIP-MIB", "tripRouteAddress"),
    (0, "TRIP-MIB", "tripRoutePeer"),
)
if mibBuilder.loadTexts:
    tripRouteEntry.setStatus("current")
_TripRouteAppProtocol_Type = TripAppProtocol
_TripRouteAppProtocol_Object = MibTableColumn
tripRouteAppProtocol = _TripRouteAppProtocol_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 6, 1, 1),
    _TripRouteAppProtocol_Type()
)
tripRouteAppProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tripRouteAppProtocol.setStatus("current")
_TripRouteAddressFamily_Type = TripAddressFamily
_TripRouteAddressFamily_Object = MibTableColumn
tripRouteAddressFamily = _TripRouteAddressFamily_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 6, 1, 2),
    _TripRouteAddressFamily_Type()
)
tripRouteAddressFamily.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tripRouteAddressFamily.setStatus("current")


class _TripRouteAddress_Type(OctetString):
    """Custom type tripRouteAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 105),
    )


_TripRouteAddress_Type.__name__ = "OctetString"
_TripRouteAddress_Object = MibTableColumn
tripRouteAddress = _TripRouteAddress_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 6, 1, 3),
    _TripRouteAddress_Type()
)
tripRouteAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tripRouteAddress.setStatus("current")
_TripRoutePeer_Type = TripId
_TripRoutePeer_Object = MibTableColumn
tripRoutePeer = _TripRoutePeer_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 6, 1, 4),
    _TripRoutePeer_Type()
)
tripRoutePeer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tripRoutePeer.setStatus("current")


class _TripRouteTRIBMask_Type(Bits):
    """Custom type tripRouteTRIBMask based on Bits"""
    namedValues = NamedValues(
        *(("adjTribIns", 0),
          ("adjTribOut", 3),
          ("extTrib", 1),
          ("locTrib", 2))
    )

_TripRouteTRIBMask_Type.__name__ = "Bits"
_TripRouteTRIBMask_Object = MibTableColumn
tripRouteTRIBMask = _TripRouteTRIBMask_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 6, 1, 5),
    _TripRouteTRIBMask_Type()
)
tripRouteTRIBMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tripRouteTRIBMask.setStatus("current")


class _TripRouteAddressSequenceNumber_Type(Unsigned32):
    """Custom type tripRouteAddressSequenceNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TripRouteAddressSequenceNumber_Type.__name__ = "Unsigned32"
_TripRouteAddressSequenceNumber_Object = MibTableColumn
tripRouteAddressSequenceNumber = _TripRouteAddressSequenceNumber_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 6, 1, 6),
    _TripRouteAddressSequenceNumber_Type()
)
tripRouteAddressSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tripRouteAddressSequenceNumber.setStatus("current")
_TripRouteAddressOriginatorId_Type = TripId
_TripRouteAddressOriginatorId_Object = MibTableColumn
tripRouteAddressOriginatorId = _TripRouteAddressOriginatorId_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 6, 1, 7),
    _TripRouteAddressOriginatorId_Type()
)
tripRouteAddressOriginatorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tripRouteAddressOriginatorId.setStatus("current")
_TripRouteNextHopServerIAddrType_Type = InetAddressType
_TripRouteNextHopServerIAddrType_Object = MibTableColumn
tripRouteNextHopServerIAddrType = _TripRouteNextHopServerIAddrType_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 6, 1, 8),
    _TripRouteNextHopServerIAddrType_Type()
)
tripRouteNextHopServerIAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tripRouteNextHopServerIAddrType.setStatus("current")
_TripRouteNextHopServer_Type = InetAddress
_TripRouteNextHopServer_Object = MibTableColumn
tripRouteNextHopServer = _TripRouteNextHopServer_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 6, 1, 9),
    _TripRouteNextHopServer_Type()
)
tripRouteNextHopServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tripRouteNextHopServer.setStatus("current")
_TripRouteNextHopServerPort_Type = InetPortNumber
_TripRouteNextHopServerPort_Object = MibTableColumn
tripRouteNextHopServerPort = _TripRouteNextHopServerPort_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 6, 1, 10),
    _TripRouteNextHopServerPort_Type()
)
tripRouteNextHopServerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tripRouteNextHopServerPort.setStatus("current")
_TripRouteNextHopServerItad_Type = TripItad
_TripRouteNextHopServerItad_Object = MibTableColumn
tripRouteNextHopServerItad = _TripRouteNextHopServerItad_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 6, 1, 11),
    _TripRouteNextHopServerItad_Type()
)
tripRouteNextHopServerItad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tripRouteNextHopServerItad.setStatus("current")


class _TripRouteMultiExitDisc_Type(Unsigned32):
    """Custom type tripRouteMultiExitDisc based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TripRouteMultiExitDisc_Type.__name__ = "Unsigned32"
_TripRouteMultiExitDisc_Object = MibTableColumn
tripRouteMultiExitDisc = _TripRouteMultiExitDisc_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 6, 1, 12),
    _TripRouteMultiExitDisc_Type()
)
tripRouteMultiExitDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tripRouteMultiExitDisc.setStatus("current")


class _TripRouteLocalPref_Type(Unsigned32):
    """Custom type tripRouteLocalPref based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TripRouteLocalPref_Type.__name__ = "Unsigned32"
_TripRouteLocalPref_Object = MibTableColumn
tripRouteLocalPref = _TripRouteLocalPref_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 6, 1, 13),
    _TripRouteLocalPref_Type()
)
tripRouteLocalPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tripRouteLocalPref.setStatus("current")


class _TripRouteAdvertisementPath_Type(OctetString):
    """Custom type tripRouteAdvertisementPath based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 252),
    )


_TripRouteAdvertisementPath_Type.__name__ = "OctetString"
_TripRouteAdvertisementPath_Object = MibTableColumn
tripRouteAdvertisementPath = _TripRouteAdvertisementPath_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 6, 1, 14),
    _TripRouteAdvertisementPath_Type()
)
tripRouteAdvertisementPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tripRouteAdvertisementPath.setStatus("current")


class _TripRouteRoutedPath_Type(OctetString):
    """Custom type tripRouteRoutedPath based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 252),
    )


_TripRouteRoutedPath_Type.__name__ = "OctetString"
_TripRouteRoutedPath_Object = MibTableColumn
tripRouteRoutedPath = _TripRouteRoutedPath_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 6, 1, 15),
    _TripRouteRoutedPath_Type()
)
tripRouteRoutedPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tripRouteRoutedPath.setStatus("current")
_TripRouteAtomicAggregate_Type = TruthValue
_TripRouteAtomicAggregate_Object = MibTableColumn
tripRouteAtomicAggregate = _TripRouteAtomicAggregate_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 6, 1, 16),
    _TripRouteAtomicAggregate_Type()
)
tripRouteAtomicAggregate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tripRouteAtomicAggregate.setStatus("current")


class _TripRouteUnknown_Type(OctetString):
    """Custom type tripRouteUnknown based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TripRouteUnknown_Type.__name__ = "OctetString"
_TripRouteUnknown_Object = MibTableColumn
tripRouteUnknown = _TripRouteUnknown_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 6, 1, 17),
    _TripRouteUnknown_Type()
)
tripRouteUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tripRouteUnknown.setStatus("current")
_TripRouteWithdrawn_Type = TruthValue
_TripRouteWithdrawn_Object = MibTableColumn
tripRouteWithdrawn = _TripRouteWithdrawn_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 6, 1, 18),
    _TripRouteWithdrawn_Type()
)
tripRouteWithdrawn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tripRouteWithdrawn.setStatus("current")
_TripRouteConverted_Type = TruthValue
_TripRouteConverted_Object = MibTableColumn
tripRouteConverted = _TripRouteConverted_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 6, 1, 19),
    _TripRouteConverted_Type()
)
tripRouteConverted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tripRouteConverted.setStatus("current")
_TripRouteReceivedTime_Type = TimeStamp
_TripRouteReceivedTime_Object = MibTableColumn
tripRouteReceivedTime = _TripRouteReceivedTime_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 6, 1, 20),
    _TripRouteReceivedTime_Type()
)
tripRouteReceivedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tripRouteReceivedTime.setStatus("current")
_TripRouteCommunityTable_Object = MibTable
tripRouteCommunityTable = _TripRouteCommunityTable_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 7)
)
if mibBuilder.loadTexts:
    tripRouteCommunityTable.setStatus("current")
_TripRouteCommunityEntry_Object = MibTableRow
tripRouteCommunityEntry = _TripRouteCommunityEntry_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 7, 1)
)
tripRouteCommunityEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
    (0, "TRIP-MIB", "tripRouteAppProtocol"),
    (0, "TRIP-MIB", "tripRouteAddressFamily"),
    (0, "TRIP-MIB", "tripRouteAddress"),
    (0, "TRIP-MIB", "tripRoutePeer"),
    (0, "TRIP-MIB", "tripRouteCommunityId"),
)
if mibBuilder.loadTexts:
    tripRouteCommunityEntry.setStatus("current")
_TripRouteCommunityId_Type = TripCommunityId
_TripRouteCommunityId_Object = MibTableColumn
tripRouteCommunityId = _TripRouteCommunityId_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 7, 1, 1),
    _TripRouteCommunityId_Type()
)
tripRouteCommunityId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tripRouteCommunityId.setStatus("current")
_TripRouteCommunityItad_Type = TripItad
_TripRouteCommunityItad_Object = MibTableColumn
tripRouteCommunityItad = _TripRouteCommunityItad_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 7, 1, 2),
    _TripRouteCommunityItad_Type()
)
tripRouteCommunityItad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tripRouteCommunityItad.setStatus("current")
_TripItadTopologyTable_Object = MibTable
tripItadTopologyTable = _TripItadTopologyTable_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 8)
)
if mibBuilder.loadTexts:
    tripItadTopologyTable.setStatus("current")
_TripItadTopologyEntry_Object = MibTableRow
tripItadTopologyEntry = _TripItadTopologyEntry_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 8, 1)
)
tripItadTopologyEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
    (0, "TRIP-MIB", "tripItadTopologyOrigId"),
)
if mibBuilder.loadTexts:
    tripItadTopologyEntry.setStatus("current")
_TripItadTopologyOrigId_Type = TripId
_TripItadTopologyOrigId_Object = MibTableColumn
tripItadTopologyOrigId = _TripItadTopologyOrigId_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 8, 1, 1),
    _TripItadTopologyOrigId_Type()
)
tripItadTopologyOrigId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tripItadTopologyOrigId.setStatus("current")


class _TripItadTopologySeqNum_Type(Unsigned32):
    """Custom type tripItadTopologySeqNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TripItadTopologySeqNum_Type.__name__ = "Unsigned32"
_TripItadTopologySeqNum_Object = MibTableColumn
tripItadTopologySeqNum = _TripItadTopologySeqNum_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 8, 1, 2),
    _TripItadTopologySeqNum_Type()
)
tripItadTopologySeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tripItadTopologySeqNum.setStatus("current")
_TripItadTopologyIdTable_Object = MibTable
tripItadTopologyIdTable = _TripItadTopologyIdTable_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 9)
)
if mibBuilder.loadTexts:
    tripItadTopologyIdTable.setStatus("current")
_TripItadTopologyIdEntry_Object = MibTableRow
tripItadTopologyIdEntry = _TripItadTopologyIdEntry_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 9, 1)
)
tripItadTopologyIdEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
    (0, "TRIP-MIB", "tripItadTopologyOrigId"),
    (0, "TRIP-MIB", "tripItadTopologyId"),
)
if mibBuilder.loadTexts:
    tripItadTopologyIdEntry.setStatus("current")
_TripItadTopologyId_Type = TripId
_TripItadTopologyId_Object = MibTableColumn
tripItadTopologyId = _TripItadTopologyId_Object(
    (1, 3, 6, 1, 2, 1, 116, 1, 9, 1, 1),
    _TripItadTopologyId_Type()
)
tripItadTopologyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tripItadTopologyId.setStatus("current")
_TripMIBConformance_ObjectIdentity = ObjectIdentity
tripMIBConformance = _TripMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 116, 2)
)
_TripMIBCompliances_ObjectIdentity = ObjectIdentity
tripMIBCompliances = _TripMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 116, 2, 1)
)
_TripMIBGroups_ObjectIdentity = ObjectIdentity
tripMIBGroups = _TripMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 116, 2, 2)
)
_TripMIBNotifObjects_ObjectIdentity = ObjectIdentity
tripMIBNotifObjects = _TripMIBNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 116, 3)
)


class _TripNotifApplIndex_Type(Integer32):
    """Custom type tripNotifApplIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TripNotifApplIndex_Type.__name__ = "Integer32"
_TripNotifApplIndex_Object = MibScalar
tripNotifApplIndex = _TripNotifApplIndex_Object(
    (1, 3, 6, 1, 2, 1, 116, 3, 1),
    _TripNotifApplIndex_Type()
)
tripNotifApplIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tripNotifApplIndex.setStatus("current")
_TripNotifPeerAddrInetType_Type = InetAddressType
_TripNotifPeerAddrInetType_Object = MibScalar
tripNotifPeerAddrInetType = _TripNotifPeerAddrInetType_Object(
    (1, 3, 6, 1, 2, 1, 116, 3, 2),
    _TripNotifPeerAddrInetType_Type()
)
tripNotifPeerAddrInetType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tripNotifPeerAddrInetType.setStatus("current")
_TripNotifPeerAddr_Type = InetAddress
_TripNotifPeerAddr_Object = MibScalar
tripNotifPeerAddr = _TripNotifPeerAddr_Object(
    (1, 3, 6, 1, 2, 1, 116, 3, 3),
    _TripNotifPeerAddr_Type()
)
tripNotifPeerAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tripNotifPeerAddr.setStatus("current")


class _TripNotifPeerErrCode_Type(Integer32):
    """Custom type tripNotifPeerErrCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("cease", 6),
          ("finiteStateMachine", 5),
          ("holdTimerExpired", 4),
          ("messageHeader", 1),
          ("openMessage", 2),
          ("tripNotification", 7),
          ("updateMessage", 3))
    )


_TripNotifPeerErrCode_Type.__name__ = "Integer32"
_TripNotifPeerErrCode_Object = MibScalar
tripNotifPeerErrCode = _TripNotifPeerErrCode_Object(
    (1, 3, 6, 1, 2, 1, 116, 3, 4),
    _TripNotifPeerErrCode_Type()
)
tripNotifPeerErrCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tripNotifPeerErrCode.setStatus("current")


class _TripNotifPeerErrSubcode_Type(Unsigned32):
    """Custom type tripNotifPeerErrSubcode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TripNotifPeerErrSubcode_Type.__name__ = "Unsigned32"
_TripNotifPeerErrSubcode_Object = MibScalar
tripNotifPeerErrSubcode = _TripNotifPeerErrSubcode_Object(
    (1, 3, 6, 1, 2, 1, 116, 3, 5),
    _TripNotifPeerErrSubcode_Type()
)
tripNotifPeerErrSubcode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tripNotifPeerErrSubcode.setStatus("current")
tripPeerEntry.registerAugmentions(
    ("TRIP-MIB",
     "tripPeerStatisticsEntry")
)
tripPeerStatisticsEntry.setIndexNames(*tripPeerEntry.getIndexNames())

# Managed Objects groups

tripConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 116, 2, 2, 1)
)
tripConfigGroup.setObjects(
      *(("TRIP-MIB", "tripCfgProtocolVersion"),
        ("TRIP-MIB", "tripCfgItad"),
        ("TRIP-MIB", "tripCfgIdentifier"),
        ("TRIP-MIB", "tripCfgOperStatus"),
        ("TRIP-MIB", "tripCfgAdminStatus"),
        ("TRIP-MIB", "tripCfgAddrIAddrType"),
        ("TRIP-MIB", "tripCfgAddr"),
        ("TRIP-MIB", "tripCfgPort"),
        ("TRIP-MIB", "tripCfgMinItadOriginationInterval"),
        ("TRIP-MIB", "tripCfgMinRouteAdvertisementInterval"),
        ("TRIP-MIB", "tripCfgMaxPurgeTime"),
        ("TRIP-MIB", "tripCfgDisableTime"),
        ("TRIP-MIB", "tripCfgSendReceiveMode"),
        ("TRIP-MIB", "tripCfgStorage"),
        ("TRIP-MIB", "tripSupportedCommunityItad"),
        ("TRIP-MIB", "tripSupportedCommunityStorage"),
        ("TRIP-MIB", "tripRouteTypePeer"),
        ("TRIP-MIB", "tripSupportedCommunityRowStatus"))
)
if mibBuilder.loadTexts:
    tripConfigGroup.setStatus("current")

tripPeerTableConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 116, 2, 2, 2)
)
tripPeerTableConfigGroup.setObjects(
      *(("TRIP-MIB", "tripPeerIdentifier"),
        ("TRIP-MIB", "tripPeerState"),
        ("TRIP-MIB", "tripPeerAdminStatus"),
        ("TRIP-MIB", "tripPeerNegotiatedVersion"),
        ("TRIP-MIB", "tripPeerSendReceiveMode"),
        ("TRIP-MIB", "tripPeerRemoteItad"),
        ("TRIP-MIB", "tripPeerConnectRetryInterval"),
        ("TRIP-MIB", "tripPeerMaxRetryInterval"),
        ("TRIP-MIB", "tripPeerHoldTime"),
        ("TRIP-MIB", "tripPeerKeepAlive"),
        ("TRIP-MIB", "tripPeerHoldTimeConfigured"),
        ("TRIP-MIB", "tripPeerKeepAliveConfigured"),
        ("TRIP-MIB", "tripPeerMaxPurgeTime"),
        ("TRIP-MIB", "tripPeerDisableTime"),
        ("TRIP-MIB", "tripPeerLearned"),
        ("TRIP-MIB", "tripPeerStorage"),
        ("TRIP-MIB", "tripPeerRowStatus"))
)
if mibBuilder.loadTexts:
    tripPeerTableConfigGroup.setStatus("current")

tripPeerTableStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 116, 2, 2, 3)
)
tripPeerTableStatsGroup.setObjects(
      *(("TRIP-MIB", "tripPeerInUpdates"),
        ("TRIP-MIB", "tripPeerOutUpdates"),
        ("TRIP-MIB", "tripPeerInTotalMessages"),
        ("TRIP-MIB", "tripPeerOutTotalMessages"),
        ("TRIP-MIB", "tripPeerFsmEstablishedTransitions"),
        ("TRIP-MIB", "tripPeerFsmEstablishedTime"),
        ("TRIP-MIB", "tripPeerInUpdateElapsedTime"),
        ("TRIP-MIB", "tripPeerStateChangeTime"))
)
if mibBuilder.loadTexts:
    tripPeerTableStatsGroup.setStatus("current")

tripRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 116, 2, 2, 4)
)
tripRouteGroup.setObjects(
      *(("TRIP-MIB", "tripRouteTRIBMask"),
        ("TRIP-MIB", "tripRouteAddressSequenceNumber"),
        ("TRIP-MIB", "tripRouteAddressOriginatorId"),
        ("TRIP-MIB", "tripRouteNextHopServerIAddrType"),
        ("TRIP-MIB", "tripRouteNextHopServer"),
        ("TRIP-MIB", "tripRouteNextHopServerPort"),
        ("TRIP-MIB", "tripRouteNextHopServerItad"),
        ("TRIP-MIB", "tripRouteMultiExitDisc"),
        ("TRIP-MIB", "tripRouteLocalPref"),
        ("TRIP-MIB", "tripRouteAdvertisementPath"),
        ("TRIP-MIB", "tripRouteRoutedPath"),
        ("TRIP-MIB", "tripRouteAtomicAggregate"),
        ("TRIP-MIB", "tripRouteUnknown"),
        ("TRIP-MIB", "tripRouteWithdrawn"),
        ("TRIP-MIB", "tripRouteConverted"),
        ("TRIP-MIB", "tripRouteReceivedTime"),
        ("TRIP-MIB", "tripRouteCommunityItad"))
)
if mibBuilder.loadTexts:
    tripRouteGroup.setStatus("current")

tripItadTopologyGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 116, 2, 2, 5)
)
tripItadTopologyGroup.setObjects(
      *(("TRIP-MIB", "tripItadTopologySeqNum"),
        ("TRIP-MIB", "tripItadTopologyId"))
)
if mibBuilder.loadTexts:
    tripItadTopologyGroup.setStatus("current")

tripNotifObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 116, 2, 2, 7)
)
tripNotifObjectGroup.setObjects(
      *(("TRIP-MIB", "tripNotifApplIndex"),
        ("TRIP-MIB", "tripNotifPeerAddrInetType"),
        ("TRIP-MIB", "tripNotifPeerAddr"),
        ("TRIP-MIB", "tripNotifPeerErrCode"),
        ("TRIP-MIB", "tripNotifPeerErrSubcode"))
)
if mibBuilder.loadTexts:
    tripNotifObjectGroup.setStatus("current")


# Notification objects

tripConnectionEstablished = NotificationType(
    (1, 3, 6, 1, 2, 1, 116, 0, 1)
)
tripConnectionEstablished.setObjects(
      *(("TRIP-MIB", "tripNotifApplIndex"),
        ("TRIP-MIB", "tripNotifPeerAddrInetType"),
        ("TRIP-MIB", "tripNotifPeerAddr"))
)
if mibBuilder.loadTexts:
    tripConnectionEstablished.setStatus(
        "current"
    )

tripConnectionDropped = NotificationType(
    (1, 3, 6, 1, 2, 1, 116, 0, 2)
)
tripConnectionDropped.setObjects(
      *(("TRIP-MIB", "tripNotifApplIndex"),
        ("TRIP-MIB", "tripNotifPeerAddrInetType"),
        ("TRIP-MIB", "tripNotifPeerAddr"))
)
if mibBuilder.loadTexts:
    tripConnectionDropped.setStatus(
        "current"
    )

tripFSM = NotificationType(
    (1, 3, 6, 1, 2, 1, 116, 0, 3)
)
tripFSM.setObjects(
      *(("TRIP-MIB", "tripNotifApplIndex"),
        ("TRIP-MIB", "tripNotifPeerAddrInetType"),
        ("TRIP-MIB", "tripNotifPeerAddr"),
        ("TRIP-MIB", "tripNotifPeerErrCode"),
        ("TRIP-MIB", "tripNotifPeerErrSubcode"),
        ("TRIP-MIB", "tripPeerState"))
)
if mibBuilder.loadTexts:
    tripFSM.setStatus(
        "current"
    )

tripOpenMessageError = NotificationType(
    (1, 3, 6, 1, 2, 1, 116, 0, 4)
)
tripOpenMessageError.setObjects(
      *(("TRIP-MIB", "tripNotifApplIndex"),
        ("TRIP-MIB", "tripNotifPeerAddrInetType"),
        ("TRIP-MIB", "tripNotifPeerAddr"),
        ("TRIP-MIB", "tripNotifPeerErrCode"),
        ("TRIP-MIB", "tripNotifPeerErrSubcode"),
        ("TRIP-MIB", "tripPeerState"))
)
if mibBuilder.loadTexts:
    tripOpenMessageError.setStatus(
        "current"
    )

tripUpdateMessageError = NotificationType(
    (1, 3, 6, 1, 2, 1, 116, 0, 5)
)
tripUpdateMessageError.setObjects(
      *(("TRIP-MIB", "tripNotifApplIndex"),
        ("TRIP-MIB", "tripNotifPeerAddrInetType"),
        ("TRIP-MIB", "tripNotifPeerAddr"),
        ("TRIP-MIB", "tripNotifPeerErrCode"),
        ("TRIP-MIB", "tripNotifPeerErrSubcode"),
        ("TRIP-MIB", "tripPeerState"))
)
if mibBuilder.loadTexts:
    tripUpdateMessageError.setStatus(
        "current"
    )

tripHoldTimerExpired = NotificationType(
    (1, 3, 6, 1, 2, 1, 116, 0, 6)
)
tripHoldTimerExpired.setObjects(
      *(("TRIP-MIB", "tripNotifApplIndex"),
        ("TRIP-MIB", "tripNotifPeerAddrInetType"),
        ("TRIP-MIB", "tripNotifPeerAddr"),
        ("TRIP-MIB", "tripNotifPeerErrCode"),
        ("TRIP-MIB", "tripNotifPeerErrSubcode"),
        ("TRIP-MIB", "tripPeerState"))
)
if mibBuilder.loadTexts:
    tripHoldTimerExpired.setStatus(
        "current"
    )

tripConnectionCollision = NotificationType(
    (1, 3, 6, 1, 2, 1, 116, 0, 7)
)
tripConnectionCollision.setObjects(
    ("TRIP-MIB", "tripNotifApplIndex")
)
if mibBuilder.loadTexts:
    tripConnectionCollision.setStatus(
        "current"
    )

tripCease = NotificationType(
    (1, 3, 6, 1, 2, 1, 116, 0, 8)
)
tripCease.setObjects(
      *(("TRIP-MIB", "tripNotifApplIndex"),
        ("TRIP-MIB", "tripNotifPeerAddrInetType"),
        ("TRIP-MIB", "tripNotifPeerAddr"),
        ("TRIP-MIB", "tripNotifPeerErrCode"),
        ("TRIP-MIB", "tripNotifPeerErrSubcode"),
        ("TRIP-MIB", "tripPeerState"))
)
if mibBuilder.loadTexts:
    tripCease.setStatus(
        "current"
    )

tripNotificationErr = NotificationType(
    (1, 3, 6, 1, 2, 1, 116, 0, 9)
)
tripNotificationErr.setObjects(
    ("TRIP-MIB", "tripNotifApplIndex")
)
if mibBuilder.loadTexts:
    tripNotificationErr.setStatus(
        "current"
    )


# Notifications groups

tripNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 116, 2, 2, 6)
)
tripNotificationGroup.setObjects(
      *(("TRIP-MIB", "tripConnectionEstablished"),
        ("TRIP-MIB", "tripConnectionDropped"),
        ("TRIP-MIB", "tripFSM"),
        ("TRIP-MIB", "tripOpenMessageError"),
        ("TRIP-MIB", "tripUpdateMessageError"),
        ("TRIP-MIB", "tripHoldTimerExpired"),
        ("TRIP-MIB", "tripConnectionCollision"),
        ("TRIP-MIB", "tripCease"),
        ("TRIP-MIB", "tripNotificationErr"))
)
if mibBuilder.loadTexts:
    tripNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tripMIBFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 116, 2, 1, 1)
)
if mibBuilder.loadTexts:
    tripMIBFullCompliance.setStatus(
        "current"
    )

tripMIBReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 116, 2, 1, 2)
)
if mibBuilder.loadTexts:
    tripMIBReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TRIP-MIB",
    **{"tripMIB": tripMIB,
       "tripMIBNotifications": tripMIBNotifications,
       "tripConnectionEstablished": tripConnectionEstablished,
       "tripConnectionDropped": tripConnectionDropped,
       "tripFSM": tripFSM,
       "tripOpenMessageError": tripOpenMessageError,
       "tripUpdateMessageError": tripUpdateMessageError,
       "tripHoldTimerExpired": tripHoldTimerExpired,
       "tripConnectionCollision": tripConnectionCollision,
       "tripCease": tripCease,
       "tripNotificationErr": tripNotificationErr,
       "tripMIBObjects": tripMIBObjects,
       "tripCfgTable": tripCfgTable,
       "tripCfgEntry": tripCfgEntry,
       "tripCfgProtocolVersion": tripCfgProtocolVersion,
       "tripCfgItad": tripCfgItad,
       "tripCfgIdentifier": tripCfgIdentifier,
       "tripCfgAdminStatus": tripCfgAdminStatus,
       "tripCfgOperStatus": tripCfgOperStatus,
       "tripCfgAddrIAddrType": tripCfgAddrIAddrType,
       "tripCfgAddr": tripCfgAddr,
       "tripCfgPort": tripCfgPort,
       "tripCfgMinItadOriginationInterval": tripCfgMinItadOriginationInterval,
       "tripCfgMinRouteAdvertisementInterval": tripCfgMinRouteAdvertisementInterval,
       "tripCfgMaxPurgeTime": tripCfgMaxPurgeTime,
       "tripCfgDisableTime": tripCfgDisableTime,
       "tripCfgSendReceiveMode": tripCfgSendReceiveMode,
       "tripCfgStorage": tripCfgStorage,
       "tripRouteTypeTable": tripRouteTypeTable,
       "tripRouteTypeEntry": tripRouteTypeEntry,
       "tripRouteTypeAddrInetType": tripRouteTypeAddrInetType,
       "tripRouteTypeAddr": tripRouteTypeAddr,
       "tripRouteTypePort": tripRouteTypePort,
       "tripRouteTypeProtocolId": tripRouteTypeProtocolId,
       "tripRouteTypeAddrFamilyId": tripRouteTypeAddrFamilyId,
       "tripRouteTypePeer": tripRouteTypePeer,
       "tripSupportedCommunityTable": tripSupportedCommunityTable,
       "tripSupportedCommunityEntry": tripSupportedCommunityEntry,
       "tripSupportedCommunityId": tripSupportedCommunityId,
       "tripSupportedCommunityItad": tripSupportedCommunityItad,
       "tripSupportedCommunityStorage": tripSupportedCommunityStorage,
       "tripSupportedCommunityRowStatus": tripSupportedCommunityRowStatus,
       "tripPeerTable": tripPeerTable,
       "tripPeerEntry": tripPeerEntry,
       "tripPeerRemoteAddrInetType": tripPeerRemoteAddrInetType,
       "tripPeerRemoteAddr": tripPeerRemoteAddr,
       "tripPeerRemotePort": tripPeerRemotePort,
       "tripPeerIdentifier": tripPeerIdentifier,
       "tripPeerState": tripPeerState,
       "tripPeerAdminStatus": tripPeerAdminStatus,
       "tripPeerNegotiatedVersion": tripPeerNegotiatedVersion,
       "tripPeerSendReceiveMode": tripPeerSendReceiveMode,
       "tripPeerRemoteItad": tripPeerRemoteItad,
       "tripPeerConnectRetryInterval": tripPeerConnectRetryInterval,
       "tripPeerMaxRetryInterval": tripPeerMaxRetryInterval,
       "tripPeerHoldTime": tripPeerHoldTime,
       "tripPeerKeepAlive": tripPeerKeepAlive,
       "tripPeerHoldTimeConfigured": tripPeerHoldTimeConfigured,
       "tripPeerKeepAliveConfigured": tripPeerKeepAliveConfigured,
       "tripPeerMaxPurgeTime": tripPeerMaxPurgeTime,
       "tripPeerDisableTime": tripPeerDisableTime,
       "tripPeerLearned": tripPeerLearned,
       "tripPeerStorage": tripPeerStorage,
       "tripPeerRowStatus": tripPeerRowStatus,
       "tripPeerStatisticsTable": tripPeerStatisticsTable,
       "tripPeerStatisticsEntry": tripPeerStatisticsEntry,
       "tripPeerInUpdates": tripPeerInUpdates,
       "tripPeerOutUpdates": tripPeerOutUpdates,
       "tripPeerInTotalMessages": tripPeerInTotalMessages,
       "tripPeerOutTotalMessages": tripPeerOutTotalMessages,
       "tripPeerFsmEstablishedTransitions": tripPeerFsmEstablishedTransitions,
       "tripPeerFsmEstablishedTime": tripPeerFsmEstablishedTime,
       "tripPeerInUpdateElapsedTime": tripPeerInUpdateElapsedTime,
       "tripPeerStateChangeTime": tripPeerStateChangeTime,
       "tripRouteTable": tripRouteTable,
       "tripRouteEntry": tripRouteEntry,
       "tripRouteAppProtocol": tripRouteAppProtocol,
       "tripRouteAddressFamily": tripRouteAddressFamily,
       "tripRouteAddress": tripRouteAddress,
       "tripRoutePeer": tripRoutePeer,
       "tripRouteTRIBMask": tripRouteTRIBMask,
       "tripRouteAddressSequenceNumber": tripRouteAddressSequenceNumber,
       "tripRouteAddressOriginatorId": tripRouteAddressOriginatorId,
       "tripRouteNextHopServerIAddrType": tripRouteNextHopServerIAddrType,
       "tripRouteNextHopServer": tripRouteNextHopServer,
       "tripRouteNextHopServerPort": tripRouteNextHopServerPort,
       "tripRouteNextHopServerItad": tripRouteNextHopServerItad,
       "tripRouteMultiExitDisc": tripRouteMultiExitDisc,
       "tripRouteLocalPref": tripRouteLocalPref,
       "tripRouteAdvertisementPath": tripRouteAdvertisementPath,
       "tripRouteRoutedPath": tripRouteRoutedPath,
       "tripRouteAtomicAggregate": tripRouteAtomicAggregate,
       "tripRouteUnknown": tripRouteUnknown,
       "tripRouteWithdrawn": tripRouteWithdrawn,
       "tripRouteConverted": tripRouteConverted,
       "tripRouteReceivedTime": tripRouteReceivedTime,
       "tripRouteCommunityTable": tripRouteCommunityTable,
       "tripRouteCommunityEntry": tripRouteCommunityEntry,
       "tripRouteCommunityId": tripRouteCommunityId,
       "tripRouteCommunityItad": tripRouteCommunityItad,
       "tripItadTopologyTable": tripItadTopologyTable,
       "tripItadTopologyEntry": tripItadTopologyEntry,
       "tripItadTopologyOrigId": tripItadTopologyOrigId,
       "tripItadTopologySeqNum": tripItadTopologySeqNum,
       "tripItadTopologyIdTable": tripItadTopologyIdTable,
       "tripItadTopologyIdEntry": tripItadTopologyIdEntry,
       "tripItadTopologyId": tripItadTopologyId,
       "tripMIBConformance": tripMIBConformance,
       "tripMIBCompliances": tripMIBCompliances,
       "tripMIBFullCompliance": tripMIBFullCompliance,
       "tripMIBReadOnlyCompliance": tripMIBReadOnlyCompliance,
       "tripMIBGroups": tripMIBGroups,
       "tripConfigGroup": tripConfigGroup,
       "tripPeerTableConfigGroup": tripPeerTableConfigGroup,
       "tripPeerTableStatsGroup": tripPeerTableStatsGroup,
       "tripRouteGroup": tripRouteGroup,
       "tripItadTopologyGroup": tripItadTopologyGroup,
       "tripNotificationGroup": tripNotificationGroup,
       "tripNotifObjectGroup": tripNotifObjectGroup,
       "tripMIBNotifObjects": tripMIBNotifObjects,
       "tripNotifApplIndex": tripNotifApplIndex,
       "tripNotifPeerAddrInetType": tripNotifPeerAddrInetType,
       "tripNotifPeerAddr": tripNotifPeerAddr,
       "tripNotifPeerErrCode": tripNotifPeerErrCode,
       "tripNotifPeerErrSubcode": tripNotifPeerErrSubcode}
)
