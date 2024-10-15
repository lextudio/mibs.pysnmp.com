# SNMP MIB module (Unisphere-Data-L2TP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-L2TP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:11:05 2024
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(usDataMibs,) = mibBuilder.importSymbols(
    "Unisphere-Data-MIBs",
    "usDataMibs")

(UsdEnable,) = mibBuilder.importSymbols(
    "Unisphere-Data-TC",
    "UsdEnable")


# MODULE-IDENTITY

usdL2tpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35)
)
usdL2tpMIB.setRevisions(
        ("2001-10-17 14:51",
         "2001-10-17 13:55",
         "2001-06-18 20:00",
         "2000-02-11 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class UsdL2tpTunnelId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class UsdL2tpSessionId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class UsdL2tpAdminState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("drain", 2),
          ("enabled", 0))
    )



class UsdL2tpTransport(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("udpIp", 1))
    )



# MIB Managed Objects in the order of their OIDs

_UsdL2tpTraps_ObjectIdentity = ObjectIdentity
usdL2tpTraps = _UsdL2tpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 0)
)
_UsdL2tpObjects_ObjectIdentity = ObjectIdentity
usdL2tpObjects = _UsdL2tpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1)
)
_UsdL2tpSystem_ObjectIdentity = ObjectIdentity
usdL2tpSystem = _UsdL2tpSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 1)
)
_UsdL2tpSystemConfig_ObjectIdentity = ObjectIdentity
usdL2tpSystemConfig = _UsdL2tpSystemConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 1, 1)
)
_UsdL2tpSysConfigAdminState_Type = UsdL2tpAdminState
_UsdL2tpSysConfigAdminState_Object = MibScalar
usdL2tpSysConfigAdminState = _UsdL2tpSysConfigAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 1, 1, 1),
    _UsdL2tpSysConfigAdminState_Type()
)
usdL2tpSysConfigAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdL2tpSysConfigAdminState.setStatus("current")


class _UsdL2tpSysConfigDestructTimeout_Type(Integer32):
    """Custom type usdL2tpSysConfigDestructTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 3600),
    )


_UsdL2tpSysConfigDestructTimeout_Type.__name__ = "Integer32"
_UsdL2tpSysConfigDestructTimeout_Object = MibScalar
usdL2tpSysConfigDestructTimeout = _UsdL2tpSysConfigDestructTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 1, 1, 2),
    _UsdL2tpSysConfigDestructTimeout_Type()
)
usdL2tpSysConfigDestructTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdL2tpSysConfigDestructTimeout.setStatus("current")
if mibBuilder.loadTexts:
    usdL2tpSysConfigDestructTimeout.setUnits("seconds")
_UsdL2tpSysConfigIpChecksumEnable_Type = UsdEnable
_UsdL2tpSysConfigIpChecksumEnable_Object = MibScalar
usdL2tpSysConfigIpChecksumEnable = _UsdL2tpSysConfigIpChecksumEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 1, 1, 3),
    _UsdL2tpSysConfigIpChecksumEnable_Type()
)
usdL2tpSysConfigIpChecksumEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdL2tpSysConfigIpChecksumEnable.setStatus("current")


class _UsdL2tpSysConfigTunnelSwitchingEnabled_Type(UsdEnable):
    """Custom type usdL2tpSysConfigTunnelSwitchingEnabled based on UsdEnable"""


_UsdL2tpSysConfigTunnelSwitchingEnabled_Object = MibScalar
usdL2tpSysConfigTunnelSwitchingEnabled = _UsdL2tpSysConfigTunnelSwitchingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 1, 1, 4),
    _UsdL2tpSysConfigTunnelSwitchingEnabled_Type()
)
usdL2tpSysConfigTunnelSwitchingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdL2tpSysConfigTunnelSwitchingEnabled.setStatus("current")


class _UsdL2tpSysConfigControlRetransmissions_Type(Integer32):
    """Custom type usdL2tpSysConfigControlRetransmissions based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 7),
    )


_UsdL2tpSysConfigControlRetransmissions_Type.__name__ = "Integer32"
_UsdL2tpSysConfigControlRetransmissions_Object = MibScalar
usdL2tpSysConfigControlRetransmissions = _UsdL2tpSysConfigControlRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 1, 1, 5),
    _UsdL2tpSysConfigControlRetransmissions_Type()
)
usdL2tpSysConfigControlRetransmissions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdL2tpSysConfigControlRetransmissions.setStatus("current")


class _UsdL2tpSysConfigTunnelIdleTimeout_Type(Integer32):
    """Custom type usdL2tpSysConfigTunnelIdleTimeout based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_UsdL2tpSysConfigTunnelIdleTimeout_Type.__name__ = "Integer32"
_UsdL2tpSysConfigTunnelIdleTimeout_Object = MibScalar
usdL2tpSysConfigTunnelIdleTimeout = _UsdL2tpSysConfigTunnelIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 1, 1, 6),
    _UsdL2tpSysConfigTunnelIdleTimeout_Type()
)
usdL2tpSysConfigTunnelIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdL2tpSysConfigTunnelIdleTimeout.setStatus("current")
if mibBuilder.loadTexts:
    usdL2tpSysConfigTunnelIdleTimeout.setUnits("seconds")
_UsdL2tpSysConfigReceiveDataSequencingIgnore_Type = UsdEnable
_UsdL2tpSysConfigReceiveDataSequencingIgnore_Object = MibScalar
usdL2tpSysConfigReceiveDataSequencingIgnore = _UsdL2tpSysConfigReceiveDataSequencingIgnore_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 1, 1, 7),
    _UsdL2tpSysConfigReceiveDataSequencingIgnore_Type()
)
usdL2tpSysConfigReceiveDataSequencingIgnore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdL2tpSysConfigReceiveDataSequencingIgnore.setStatus("current")
_UsdL2tpSystemStatus_ObjectIdentity = ObjectIdentity
usdL2tpSystemStatus = _UsdL2tpSystemStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 1, 2)
)


class _UsdL2tpSysStatusProtocolVersion_Type(OctetString):
    """Custom type usdL2tpSysStatusProtocolVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 256),
    )


_UsdL2tpSysStatusProtocolVersion_Type.__name__ = "OctetString"
_UsdL2tpSysStatusProtocolVersion_Object = MibScalar
usdL2tpSysStatusProtocolVersion = _UsdL2tpSysStatusProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 1, 2, 1),
    _UsdL2tpSysStatusProtocolVersion_Type()
)
usdL2tpSysStatusProtocolVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpSysStatusProtocolVersion.setStatus("current")
_UsdL2tpSysStatusVendorName_Type = DisplayString
_UsdL2tpSysStatusVendorName_Object = MibScalar
usdL2tpSysStatusVendorName = _UsdL2tpSysStatusVendorName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 1, 2, 2),
    _UsdL2tpSysStatusVendorName_Type()
)
usdL2tpSysStatusVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpSysStatusVendorName.setStatus("current")
_UsdL2tpSysStatusFirmwareRev_Type = Integer32
_UsdL2tpSysStatusFirmwareRev_Object = MibScalar
usdL2tpSysStatusFirmwareRev = _UsdL2tpSysStatusFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 1, 2, 3),
    _UsdL2tpSysStatusFirmwareRev_Type()
)
usdL2tpSysStatusFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpSysStatusFirmwareRev.setStatus("current")
_UsdL2tpSysStatusTotalDestinations_Type = Counter32
_UsdL2tpSysStatusTotalDestinations_Object = MibScalar
usdL2tpSysStatusTotalDestinations = _UsdL2tpSysStatusTotalDestinations_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 1, 2, 4),
    _UsdL2tpSysStatusTotalDestinations_Type()
)
usdL2tpSysStatusTotalDestinations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpSysStatusTotalDestinations.setStatus("current")
_UsdL2tpSysStatusFailedDestinations_Type = Counter32
_UsdL2tpSysStatusFailedDestinations_Object = MibScalar
usdL2tpSysStatusFailedDestinations = _UsdL2tpSysStatusFailedDestinations_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 1, 2, 5),
    _UsdL2tpSysStatusFailedDestinations_Type()
)
usdL2tpSysStatusFailedDestinations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpSysStatusFailedDestinations.setStatus("current")
_UsdL2tpSysStatusActiveDestinations_Type = Gauge32
_UsdL2tpSysStatusActiveDestinations_Object = MibScalar
usdL2tpSysStatusActiveDestinations = _UsdL2tpSysStatusActiveDestinations_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 1, 2, 6),
    _UsdL2tpSysStatusActiveDestinations_Type()
)
usdL2tpSysStatusActiveDestinations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpSysStatusActiveDestinations.setStatus("current")
_UsdL2tpSysStatusTotalTunnels_Type = Counter32
_UsdL2tpSysStatusTotalTunnels_Object = MibScalar
usdL2tpSysStatusTotalTunnels = _UsdL2tpSysStatusTotalTunnels_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 1, 2, 7),
    _UsdL2tpSysStatusTotalTunnels_Type()
)
usdL2tpSysStatusTotalTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpSysStatusTotalTunnels.setStatus("current")
_UsdL2tpSysStatusFailedTunnels_Type = Counter32
_UsdL2tpSysStatusFailedTunnels_Object = MibScalar
usdL2tpSysStatusFailedTunnels = _UsdL2tpSysStatusFailedTunnels_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 1, 2, 8),
    _UsdL2tpSysStatusFailedTunnels_Type()
)
usdL2tpSysStatusFailedTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpSysStatusFailedTunnels.setStatus("current")
_UsdL2tpSysStatusFailedTunnelAuthens_Type = Counter32
_UsdL2tpSysStatusFailedTunnelAuthens_Object = MibScalar
usdL2tpSysStatusFailedTunnelAuthens = _UsdL2tpSysStatusFailedTunnelAuthens_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 1, 2, 9),
    _UsdL2tpSysStatusFailedTunnelAuthens_Type()
)
usdL2tpSysStatusFailedTunnelAuthens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpSysStatusFailedTunnelAuthens.setStatus("current")
_UsdL2tpSysStatusActiveTunnels_Type = Gauge32
_UsdL2tpSysStatusActiveTunnels_Object = MibScalar
usdL2tpSysStatusActiveTunnels = _UsdL2tpSysStatusActiveTunnels_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 1, 2, 10),
    _UsdL2tpSysStatusActiveTunnels_Type()
)
usdL2tpSysStatusActiveTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpSysStatusActiveTunnels.setStatus("current")
_UsdL2tpSysStatusTotalSessions_Type = Counter32
_UsdL2tpSysStatusTotalSessions_Object = MibScalar
usdL2tpSysStatusTotalSessions = _UsdL2tpSysStatusTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 1, 2, 11),
    _UsdL2tpSysStatusTotalSessions_Type()
)
usdL2tpSysStatusTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpSysStatusTotalSessions.setStatus("current")
_UsdL2tpSysStatusFailedSessions_Type = Counter32
_UsdL2tpSysStatusFailedSessions_Object = MibScalar
usdL2tpSysStatusFailedSessions = _UsdL2tpSysStatusFailedSessions_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 1, 2, 12),
    _UsdL2tpSysStatusFailedSessions_Type()
)
usdL2tpSysStatusFailedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpSysStatusFailedSessions.setStatus("current")
_UsdL2tpSysStatusActiveSessions_Type = Gauge32
_UsdL2tpSysStatusActiveSessions_Object = MibScalar
usdL2tpSysStatusActiveSessions = _UsdL2tpSysStatusActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 1, 2, 13),
    _UsdL2tpSysStatusActiveSessions_Type()
)
usdL2tpSysStatusActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpSysStatusActiveSessions.setStatus("current")
_UsdL2tpDestination_ObjectIdentity = ObjectIdentity
usdL2tpDestination = _UsdL2tpDestination_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2)
)
_UsdL2tpDestConfig_ObjectIdentity = ObjectIdentity
usdL2tpDestConfig = _UsdL2tpDestConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 1)
)
_UsdL2tpDestConfigTable_Object = MibTable
usdL2tpDestConfigTable = _UsdL2tpDestConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    usdL2tpDestConfigTable.setStatus("current")
_UsdL2tpDestConfigEntry_Object = MibTableRow
usdL2tpDestConfigEntry = _UsdL2tpDestConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 1, 2, 1)
)
usdL2tpDestConfigEntry.setIndexNames(
    (0, "Unisphere-Data-L2TP-MIB", "usdL2tpDestConfigIfIndex"),
)
if mibBuilder.loadTexts:
    usdL2tpDestConfigEntry.setStatus("current")
_UsdL2tpDestConfigIfIndex_Type = InterfaceIndex
_UsdL2tpDestConfigIfIndex_Object = MibTableColumn
usdL2tpDestConfigIfIndex = _UsdL2tpDestConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 1, 2, 1, 1),
    _UsdL2tpDestConfigIfIndex_Type()
)
usdL2tpDestConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdL2tpDestConfigIfIndex.setStatus("current")
_UsdL2tpDestConfigRowStatus_Type = RowStatus
_UsdL2tpDestConfigRowStatus_Object = MibTableColumn
usdL2tpDestConfigRowStatus = _UsdL2tpDestConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 1, 2, 1, 2),
    _UsdL2tpDestConfigRowStatus_Type()
)
usdL2tpDestConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdL2tpDestConfigRowStatus.setStatus("current")


class _UsdL2tpDestConfigAdminState_Type(UsdL2tpAdminState):
    """Custom type usdL2tpDestConfigAdminState based on UsdL2tpAdminState"""


_UsdL2tpDestConfigAdminState_Object = MibTableColumn
usdL2tpDestConfigAdminState = _UsdL2tpDestConfigAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 1, 2, 1, 3),
    _UsdL2tpDestConfigAdminState_Type()
)
usdL2tpDestConfigAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdL2tpDestConfigAdminState.setStatus("current")
_UsdL2tpDestStatus_ObjectIdentity = ObjectIdentity
usdL2tpDestStatus = _UsdL2tpDestStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 2)
)
_UsdL2tpDestStatusTable_Object = MibTable
usdL2tpDestStatusTable = _UsdL2tpDestStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    usdL2tpDestStatusTable.setStatus("current")
_UsdL2tpDestStatusEntry_Object = MibTableRow
usdL2tpDestStatusEntry = _UsdL2tpDestStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 2, 1, 1)
)
usdL2tpDestStatusEntry.setIndexNames(
    (0, "Unisphere-Data-L2TP-MIB", "usdL2tpDestStatusIfIndex"),
)
if mibBuilder.loadTexts:
    usdL2tpDestStatusEntry.setStatus("current")
_UsdL2tpDestStatusIfIndex_Type = InterfaceIndex
_UsdL2tpDestStatusIfIndex_Object = MibTableColumn
usdL2tpDestStatusIfIndex = _UsdL2tpDestStatusIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 2, 1, 1, 1),
    _UsdL2tpDestStatusIfIndex_Type()
)
usdL2tpDestStatusIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdL2tpDestStatusIfIndex.setStatus("current")
_UsdL2tpDestStatusTransport_Type = UsdL2tpTransport
_UsdL2tpDestStatusTransport_Object = MibTableColumn
usdL2tpDestStatusTransport = _UsdL2tpDestStatusTransport_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 2, 1, 1, 2),
    _UsdL2tpDestStatusTransport_Type()
)
usdL2tpDestStatusTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpDestStatusTransport.setStatus("current")
_UsdL2tpDestStatusEffectiveAdminState_Type = UsdL2tpAdminState
_UsdL2tpDestStatusEffectiveAdminState_Object = MibTableColumn
usdL2tpDestStatusEffectiveAdminState = _UsdL2tpDestStatusEffectiveAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 2, 1, 1, 3),
    _UsdL2tpDestStatusEffectiveAdminState_Type()
)
usdL2tpDestStatusEffectiveAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpDestStatusEffectiveAdminState.setStatus("current")
_UsdL2tpDestStatusTotalTunnels_Type = Counter32
_UsdL2tpDestStatusTotalTunnels_Object = MibTableColumn
usdL2tpDestStatusTotalTunnels = _UsdL2tpDestStatusTotalTunnels_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 2, 1, 1, 4),
    _UsdL2tpDestStatusTotalTunnels_Type()
)
usdL2tpDestStatusTotalTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpDestStatusTotalTunnels.setStatus("current")
_UsdL2tpDestStatusFailedTunnels_Type = Counter32
_UsdL2tpDestStatusFailedTunnels_Object = MibTableColumn
usdL2tpDestStatusFailedTunnels = _UsdL2tpDestStatusFailedTunnels_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 2, 1, 1, 5),
    _UsdL2tpDestStatusFailedTunnels_Type()
)
usdL2tpDestStatusFailedTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpDestStatusFailedTunnels.setStatus("current")
_UsdL2tpDestStatusFailedTunnelAuthens_Type = Counter32
_UsdL2tpDestStatusFailedTunnelAuthens_Object = MibTableColumn
usdL2tpDestStatusFailedTunnelAuthens = _UsdL2tpDestStatusFailedTunnelAuthens_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 2, 1, 1, 6),
    _UsdL2tpDestStatusFailedTunnelAuthens_Type()
)
usdL2tpDestStatusFailedTunnelAuthens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpDestStatusFailedTunnelAuthens.setStatus("current")
_UsdL2tpDestStatusActiveTunnels_Type = Gauge32
_UsdL2tpDestStatusActiveTunnels_Object = MibTableColumn
usdL2tpDestStatusActiveTunnels = _UsdL2tpDestStatusActiveTunnels_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 2, 1, 1, 7),
    _UsdL2tpDestStatusActiveTunnels_Type()
)
usdL2tpDestStatusActiveTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpDestStatusActiveTunnels.setStatus("current")
_UsdL2tpDestStatusTotalSessions_Type = Counter32
_UsdL2tpDestStatusTotalSessions_Object = MibTableColumn
usdL2tpDestStatusTotalSessions = _UsdL2tpDestStatusTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 2, 1, 1, 8),
    _UsdL2tpDestStatusTotalSessions_Type()
)
usdL2tpDestStatusTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpDestStatusTotalSessions.setStatus("current")
_UsdL2tpDestStatusFailedSessions_Type = Counter32
_UsdL2tpDestStatusFailedSessions_Object = MibTableColumn
usdL2tpDestStatusFailedSessions = _UsdL2tpDestStatusFailedSessions_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 2, 1, 1, 9),
    _UsdL2tpDestStatusFailedSessions_Type()
)
usdL2tpDestStatusFailedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpDestStatusFailedSessions.setStatus("current")
_UsdL2tpDestStatusActiveSessions_Type = Gauge32
_UsdL2tpDestStatusActiveSessions_Object = MibTableColumn
usdL2tpDestStatusActiveSessions = _UsdL2tpDestStatusActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 2, 1, 1, 10),
    _UsdL2tpDestStatusActiveSessions_Type()
)
usdL2tpDestStatusActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpDestStatusActiveSessions.setStatus("current")
_UsdL2tpDestStatistics_ObjectIdentity = ObjectIdentity
usdL2tpDestStatistics = _UsdL2tpDestStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 3)
)
_UsdL2tpDestStatTable_Object = MibTable
usdL2tpDestStatTable = _UsdL2tpDestStatTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    usdL2tpDestStatTable.setStatus("current")
_UsdL2tpDestStatEntry_Object = MibTableRow
usdL2tpDestStatEntry = _UsdL2tpDestStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 3, 1, 1)
)
usdL2tpDestStatEntry.setIndexNames(
    (0, "Unisphere-Data-L2TP-MIB", "usdL2tpDestStatIfIndex"),
)
if mibBuilder.loadTexts:
    usdL2tpDestStatEntry.setStatus("current")
_UsdL2tpDestStatIfIndex_Type = InterfaceIndex
_UsdL2tpDestStatIfIndex_Object = MibTableColumn
usdL2tpDestStatIfIndex = _UsdL2tpDestStatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 3, 1, 1, 1),
    _UsdL2tpDestStatIfIndex_Type()
)
usdL2tpDestStatIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdL2tpDestStatIfIndex.setStatus("current")
_UsdL2tpDestStatCtlRecvOctets_Type = Counter32
_UsdL2tpDestStatCtlRecvOctets_Object = MibTableColumn
usdL2tpDestStatCtlRecvOctets = _UsdL2tpDestStatCtlRecvOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 3, 1, 1, 2),
    _UsdL2tpDestStatCtlRecvOctets_Type()
)
usdL2tpDestStatCtlRecvOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpDestStatCtlRecvOctets.setStatus("current")
_UsdL2tpDestStatCtlRecvPackets_Type = Counter32
_UsdL2tpDestStatCtlRecvPackets_Object = MibTableColumn
usdL2tpDestStatCtlRecvPackets = _UsdL2tpDestStatCtlRecvPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 3, 1, 1, 3),
    _UsdL2tpDestStatCtlRecvPackets_Type()
)
usdL2tpDestStatCtlRecvPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpDestStatCtlRecvPackets.setStatus("current")
_UsdL2tpDestStatCtlRecvErrors_Type = Counter32
_UsdL2tpDestStatCtlRecvErrors_Object = MibTableColumn
usdL2tpDestStatCtlRecvErrors = _UsdL2tpDestStatCtlRecvErrors_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 3, 1, 1, 4),
    _UsdL2tpDestStatCtlRecvErrors_Type()
)
usdL2tpDestStatCtlRecvErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpDestStatCtlRecvErrors.setStatus("current")
_UsdL2tpDestStatCtlRecvDiscards_Type = Counter32
_UsdL2tpDestStatCtlRecvDiscards_Object = MibTableColumn
usdL2tpDestStatCtlRecvDiscards = _UsdL2tpDestStatCtlRecvDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 3, 1, 1, 5),
    _UsdL2tpDestStatCtlRecvDiscards_Type()
)
usdL2tpDestStatCtlRecvDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpDestStatCtlRecvDiscards.setStatus("current")
_UsdL2tpDestStatCtlSendOctets_Type = Counter32
_UsdL2tpDestStatCtlSendOctets_Object = MibTableColumn
usdL2tpDestStatCtlSendOctets = _UsdL2tpDestStatCtlSendOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 3, 1, 1, 6),
    _UsdL2tpDestStatCtlSendOctets_Type()
)
usdL2tpDestStatCtlSendOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpDestStatCtlSendOctets.setStatus("current")
_UsdL2tpDestStatCtlSendPackets_Type = Counter32
_UsdL2tpDestStatCtlSendPackets_Object = MibTableColumn
usdL2tpDestStatCtlSendPackets = _UsdL2tpDestStatCtlSendPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 3, 1, 1, 7),
    _UsdL2tpDestStatCtlSendPackets_Type()
)
usdL2tpDestStatCtlSendPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpDestStatCtlSendPackets.setStatus("current")
_UsdL2tpDestStatCtlSendErrors_Type = Counter32
_UsdL2tpDestStatCtlSendErrors_Object = MibTableColumn
usdL2tpDestStatCtlSendErrors = _UsdL2tpDestStatCtlSendErrors_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 3, 1, 1, 8),
    _UsdL2tpDestStatCtlSendErrors_Type()
)
usdL2tpDestStatCtlSendErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpDestStatCtlSendErrors.setStatus("current")
_UsdL2tpDestStatCtlSendDiscards_Type = Counter32
_UsdL2tpDestStatCtlSendDiscards_Object = MibTableColumn
usdL2tpDestStatCtlSendDiscards = _UsdL2tpDestStatCtlSendDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 3, 1, 1, 9),
    _UsdL2tpDestStatCtlSendDiscards_Type()
)
usdL2tpDestStatCtlSendDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpDestStatCtlSendDiscards.setStatus("current")
_UsdL2tpDestStatPayRecvOctets_Type = Counter32
_UsdL2tpDestStatPayRecvOctets_Object = MibTableColumn
usdL2tpDestStatPayRecvOctets = _UsdL2tpDestStatPayRecvOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 3, 1, 1, 10),
    _UsdL2tpDestStatPayRecvOctets_Type()
)
usdL2tpDestStatPayRecvOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpDestStatPayRecvOctets.setStatus("current")
_UsdL2tpDestStatPayRecvPackets_Type = Counter32
_UsdL2tpDestStatPayRecvPackets_Object = MibTableColumn
usdL2tpDestStatPayRecvPackets = _UsdL2tpDestStatPayRecvPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 3, 1, 1, 11),
    _UsdL2tpDestStatPayRecvPackets_Type()
)
usdL2tpDestStatPayRecvPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpDestStatPayRecvPackets.setStatus("current")
_UsdL2tpDestStatPayRecvErrors_Type = Counter32
_UsdL2tpDestStatPayRecvErrors_Object = MibTableColumn
usdL2tpDestStatPayRecvErrors = _UsdL2tpDestStatPayRecvErrors_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 3, 1, 1, 12),
    _UsdL2tpDestStatPayRecvErrors_Type()
)
usdL2tpDestStatPayRecvErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpDestStatPayRecvErrors.setStatus("current")
_UsdL2tpDestStatPayRecvDiscards_Type = Counter32
_UsdL2tpDestStatPayRecvDiscards_Object = MibTableColumn
usdL2tpDestStatPayRecvDiscards = _UsdL2tpDestStatPayRecvDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 3, 1, 1, 13),
    _UsdL2tpDestStatPayRecvDiscards_Type()
)
usdL2tpDestStatPayRecvDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpDestStatPayRecvDiscards.setStatus("current")
_UsdL2tpDestStatPaySendOctets_Type = Counter32
_UsdL2tpDestStatPaySendOctets_Object = MibTableColumn
usdL2tpDestStatPaySendOctets = _UsdL2tpDestStatPaySendOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 3, 1, 1, 14),
    _UsdL2tpDestStatPaySendOctets_Type()
)
usdL2tpDestStatPaySendOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpDestStatPaySendOctets.setStatus("current")
_UsdL2tpDestStatPaySendPackets_Type = Counter32
_UsdL2tpDestStatPaySendPackets_Object = MibTableColumn
usdL2tpDestStatPaySendPackets = _UsdL2tpDestStatPaySendPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 3, 1, 1, 15),
    _UsdL2tpDestStatPaySendPackets_Type()
)
usdL2tpDestStatPaySendPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpDestStatPaySendPackets.setStatus("current")
_UsdL2tpDestStatPaySendErrors_Type = Counter32
_UsdL2tpDestStatPaySendErrors_Object = MibTableColumn
usdL2tpDestStatPaySendErrors = _UsdL2tpDestStatPaySendErrors_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 3, 1, 1, 16),
    _UsdL2tpDestStatPaySendErrors_Type()
)
usdL2tpDestStatPaySendErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpDestStatPaySendErrors.setStatus("current")
_UsdL2tpDestStatPaySendDiscards_Type = Counter32
_UsdL2tpDestStatPaySendDiscards_Object = MibTableColumn
usdL2tpDestStatPaySendDiscards = _UsdL2tpDestStatPaySendDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 2, 3, 1, 1, 17),
    _UsdL2tpDestStatPaySendDiscards_Type()
)
usdL2tpDestStatPaySendDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpDestStatPaySendDiscards.setStatus("current")
_UsdL2tpTunnel_ObjectIdentity = ObjectIdentity
usdL2tpTunnel = _UsdL2tpTunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3)
)
_UsdL2tpTunnelConfig_ObjectIdentity = ObjectIdentity
usdL2tpTunnelConfig = _UsdL2tpTunnelConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 1)
)
_UsdL2tpTunnelConfigTable_Object = MibTable
usdL2tpTunnelConfigTable = _UsdL2tpTunnelConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    usdL2tpTunnelConfigTable.setStatus("current")
_UsdL2tpTunnelConfigEntry_Object = MibTableRow
usdL2tpTunnelConfigEntry = _UsdL2tpTunnelConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 1, 2, 1)
)
usdL2tpTunnelConfigEntry.setIndexNames(
    (0, "Unisphere-Data-L2TP-MIB", "usdL2tpTunnelConfigIfIndex"),
)
if mibBuilder.loadTexts:
    usdL2tpTunnelConfigEntry.setStatus("current")
_UsdL2tpTunnelConfigIfIndex_Type = InterfaceIndex
_UsdL2tpTunnelConfigIfIndex_Object = MibTableColumn
usdL2tpTunnelConfigIfIndex = _UsdL2tpTunnelConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 1, 2, 1, 1),
    _UsdL2tpTunnelConfigIfIndex_Type()
)
usdL2tpTunnelConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdL2tpTunnelConfigIfIndex.setStatus("current")
_UsdL2tpTunnelConfigRowStatus_Type = RowStatus
_UsdL2tpTunnelConfigRowStatus_Object = MibTableColumn
usdL2tpTunnelConfigRowStatus = _UsdL2tpTunnelConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 1, 2, 1, 2),
    _UsdL2tpTunnelConfigRowStatus_Type()
)
usdL2tpTunnelConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdL2tpTunnelConfigRowStatus.setStatus("current")


class _UsdL2tpTunnelConfigAdminState_Type(UsdL2tpAdminState):
    """Custom type usdL2tpTunnelConfigAdminState based on UsdL2tpAdminState"""


_UsdL2tpTunnelConfigAdminState_Object = MibTableColumn
usdL2tpTunnelConfigAdminState = _UsdL2tpTunnelConfigAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 1, 2, 1, 3),
    _UsdL2tpTunnelConfigAdminState_Type()
)
usdL2tpTunnelConfigAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdL2tpTunnelConfigAdminState.setStatus("current")
_UsdL2tpTunnelStatus_ObjectIdentity = ObjectIdentity
usdL2tpTunnelStatus = _UsdL2tpTunnelStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 2)
)
_UsdL2tpTunnelStatusTable_Object = MibTable
usdL2tpTunnelStatusTable = _UsdL2tpTunnelStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    usdL2tpTunnelStatusTable.setStatus("current")
_UsdL2tpTunnelStatusEntry_Object = MibTableRow
usdL2tpTunnelStatusEntry = _UsdL2tpTunnelStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 2, 1, 1)
)
usdL2tpTunnelStatusEntry.setIndexNames(
    (0, "Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatusIfIndex"),
)
if mibBuilder.loadTexts:
    usdL2tpTunnelStatusEntry.setStatus("current")
_UsdL2tpTunnelStatusIfIndex_Type = InterfaceIndex
_UsdL2tpTunnelStatusIfIndex_Object = MibTableColumn
usdL2tpTunnelStatusIfIndex = _UsdL2tpTunnelStatusIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 2, 1, 1, 1),
    _UsdL2tpTunnelStatusIfIndex_Type()
)
usdL2tpTunnelStatusIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdL2tpTunnelStatusIfIndex.setStatus("current")
_UsdL2tpTunnelStatusTransport_Type = UsdL2tpTransport
_UsdL2tpTunnelStatusTransport_Object = MibTableColumn
usdL2tpTunnelStatusTransport = _UsdL2tpTunnelStatusTransport_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 2, 1, 1, 2),
    _UsdL2tpTunnelStatusTransport_Type()
)
usdL2tpTunnelStatusTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpTunnelStatusTransport.setStatus("current")
_UsdL2tpTunnelStatusLocalTunnelId_Type = UsdL2tpTunnelId
_UsdL2tpTunnelStatusLocalTunnelId_Object = MibTableColumn
usdL2tpTunnelStatusLocalTunnelId = _UsdL2tpTunnelStatusLocalTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 2, 1, 1, 3),
    _UsdL2tpTunnelStatusLocalTunnelId_Type()
)
usdL2tpTunnelStatusLocalTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpTunnelStatusLocalTunnelId.setStatus("current")
_UsdL2tpTunnelStatusRemoteTunnelId_Type = UsdL2tpTunnelId
_UsdL2tpTunnelStatusRemoteTunnelId_Object = MibTableColumn
usdL2tpTunnelStatusRemoteTunnelId = _UsdL2tpTunnelStatusRemoteTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 2, 1, 1, 4),
    _UsdL2tpTunnelStatusRemoteTunnelId_Type()
)
usdL2tpTunnelStatusRemoteTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpTunnelStatusRemoteTunnelId.setStatus("current")
_UsdL2tpTunnelStatusEffectiveAdminState_Type = UsdL2tpAdminState
_UsdL2tpTunnelStatusEffectiveAdminState_Object = MibTableColumn
usdL2tpTunnelStatusEffectiveAdminState = _UsdL2tpTunnelStatusEffectiveAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 2, 1, 1, 5),
    _UsdL2tpTunnelStatusEffectiveAdminState_Type()
)
usdL2tpTunnelStatusEffectiveAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpTunnelStatusEffectiveAdminState.setStatus("current")


class _UsdL2tpTunnelStatusState_Type(Integer32):
    """Custom type usdL2tpTunnelStatusState based on Integer32"""
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
        *(("connecting", 1),
          ("disconnecting", 3),
          ("established", 2),
          ("idle", 0))
    )


_UsdL2tpTunnelStatusState_Type.__name__ = "Integer32"
_UsdL2tpTunnelStatusState_Object = MibTableColumn
usdL2tpTunnelStatusState = _UsdL2tpTunnelStatusState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 2, 1, 1, 6),
    _UsdL2tpTunnelStatusState_Type()
)
usdL2tpTunnelStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpTunnelStatusState.setStatus("current")


class _UsdL2tpTunnelStatusInitiated_Type(Integer32):
    """Custom type usdL2tpTunnelStatusInitiated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("none", 0),
          ("remote", 2))
    )


_UsdL2tpTunnelStatusInitiated_Type.__name__ = "Integer32"
_UsdL2tpTunnelStatusInitiated_Object = MibTableColumn
usdL2tpTunnelStatusInitiated = _UsdL2tpTunnelStatusInitiated_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 2, 1, 1, 7),
    _UsdL2tpTunnelStatusInitiated_Type()
)
usdL2tpTunnelStatusInitiated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpTunnelStatusInitiated.setStatus("current")
_UsdL2tpTunnelStatusRemoteHostName_Type = DisplayString
_UsdL2tpTunnelStatusRemoteHostName_Object = MibTableColumn
usdL2tpTunnelStatusRemoteHostName = _UsdL2tpTunnelStatusRemoteHostName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 2, 1, 1, 8),
    _UsdL2tpTunnelStatusRemoteHostName_Type()
)
usdL2tpTunnelStatusRemoteHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpTunnelStatusRemoteHostName.setStatus("current")
_UsdL2tpTunnelStatusRemoteVendorName_Type = DisplayString
_UsdL2tpTunnelStatusRemoteVendorName_Object = MibTableColumn
usdL2tpTunnelStatusRemoteVendorName = _UsdL2tpTunnelStatusRemoteVendorName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 2, 1, 1, 9),
    _UsdL2tpTunnelStatusRemoteVendorName_Type()
)
usdL2tpTunnelStatusRemoteVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpTunnelStatusRemoteVendorName.setStatus("current")
_UsdL2tpTunnelStatusRemoteFirmwareRevision_Type = Integer32
_UsdL2tpTunnelStatusRemoteFirmwareRevision_Object = MibTableColumn
usdL2tpTunnelStatusRemoteFirmwareRevision = _UsdL2tpTunnelStatusRemoteFirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 2, 1, 1, 10),
    _UsdL2tpTunnelStatusRemoteFirmwareRevision_Type()
)
usdL2tpTunnelStatusRemoteFirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpTunnelStatusRemoteFirmwareRevision.setStatus("current")


class _UsdL2tpTunnelStatusRemoteProtocolVersion_Type(OctetString):
    """Custom type usdL2tpTunnelStatusRemoteProtocolVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_UsdL2tpTunnelStatusRemoteProtocolVersion_Type.__name__ = "OctetString"
_UsdL2tpTunnelStatusRemoteProtocolVersion_Object = MibTableColumn
usdL2tpTunnelStatusRemoteProtocolVersion = _UsdL2tpTunnelStatusRemoteProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 2, 1, 1, 11),
    _UsdL2tpTunnelStatusRemoteProtocolVersion_Type()
)
usdL2tpTunnelStatusRemoteProtocolVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpTunnelStatusRemoteProtocolVersion.setStatus("current")


class _UsdL2tpTunnelStatusRemoteBearerCapabilities_Type(Integer32):
    """Custom type usdL2tpTunnelStatusRemoteBearerCapabilities based on Integer32"""
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
        *(("analog", 2),
          ("digital", 1),
          ("digitalAnalog", 3),
          ("none", 0))
    )


_UsdL2tpTunnelStatusRemoteBearerCapabilities_Type.__name__ = "Integer32"
_UsdL2tpTunnelStatusRemoteBearerCapabilities_Object = MibTableColumn
usdL2tpTunnelStatusRemoteBearerCapabilities = _UsdL2tpTunnelStatusRemoteBearerCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 2, 1, 1, 12),
    _UsdL2tpTunnelStatusRemoteBearerCapabilities_Type()
)
usdL2tpTunnelStatusRemoteBearerCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpTunnelStatusRemoteBearerCapabilities.setStatus("current")


class _UsdL2tpTunnelStatusRemoteFramingCapabilities_Type(Integer32):
    """Custom type usdL2tpTunnelStatusRemoteFramingCapabilities based on Integer32"""
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
        *(("async", 2),
          ("none", 0),
          ("sync", 1),
          ("syncAsync", 3))
    )


_UsdL2tpTunnelStatusRemoteFramingCapabilities_Type.__name__ = "Integer32"
_UsdL2tpTunnelStatusRemoteFramingCapabilities_Object = MibTableColumn
usdL2tpTunnelStatusRemoteFramingCapabilities = _UsdL2tpTunnelStatusRemoteFramingCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 2, 1, 1, 13),
    _UsdL2tpTunnelStatusRemoteFramingCapabilities_Type()
)
usdL2tpTunnelStatusRemoteFramingCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpTunnelStatusRemoteFramingCapabilities.setStatus("current")
_UsdL2tpTunnelStatusRecvWindowSize_Type = Gauge32
_UsdL2tpTunnelStatusRecvWindowSize_Object = MibTableColumn
usdL2tpTunnelStatusRecvWindowSize = _UsdL2tpTunnelStatusRecvWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 2, 1, 1, 14),
    _UsdL2tpTunnelStatusRecvWindowSize_Type()
)
usdL2tpTunnelStatusRecvWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpTunnelStatusRecvWindowSize.setStatus("current")
_UsdL2tpTunnelStatusSendWindowSize_Type = Gauge32
_UsdL2tpTunnelStatusSendWindowSize_Object = MibTableColumn
usdL2tpTunnelStatusSendWindowSize = _UsdL2tpTunnelStatusSendWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 2, 1, 1, 15),
    _UsdL2tpTunnelStatusSendWindowSize_Type()
)
usdL2tpTunnelStatusSendWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpTunnelStatusSendWindowSize.setStatus("current")
_UsdL2tpTunnelStatusSendQueueDepth_Type = Gauge32
_UsdL2tpTunnelStatusSendQueueDepth_Object = MibTableColumn
usdL2tpTunnelStatusSendQueueDepth = _UsdL2tpTunnelStatusSendQueueDepth_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 2, 1, 1, 16),
    _UsdL2tpTunnelStatusSendQueueDepth_Type()
)
usdL2tpTunnelStatusSendQueueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpTunnelStatusSendQueueDepth.setStatus("current")


class _UsdL2tpTunnelStatusRecvSeq_Type(Integer32):
    """Custom type usdL2tpTunnelStatusRecvSeq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UsdL2tpTunnelStatusRecvSeq_Type.__name__ = "Integer32"
_UsdL2tpTunnelStatusRecvSeq_Object = MibTableColumn
usdL2tpTunnelStatusRecvSeq = _UsdL2tpTunnelStatusRecvSeq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 2, 1, 1, 17),
    _UsdL2tpTunnelStatusRecvSeq_Type()
)
usdL2tpTunnelStatusRecvSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpTunnelStatusRecvSeq.setStatus("current")


class _UsdL2tpTunnelStatusRecvSeqAck_Type(Integer32):
    """Custom type usdL2tpTunnelStatusRecvSeqAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UsdL2tpTunnelStatusRecvSeqAck_Type.__name__ = "Integer32"
_UsdL2tpTunnelStatusRecvSeqAck_Object = MibTableColumn
usdL2tpTunnelStatusRecvSeqAck = _UsdL2tpTunnelStatusRecvSeqAck_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 2, 1, 1, 18),
    _UsdL2tpTunnelStatusRecvSeqAck_Type()
)
usdL2tpTunnelStatusRecvSeqAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpTunnelStatusRecvSeqAck.setStatus("current")


class _UsdL2tpTunnelStatusSendSeq_Type(Integer32):
    """Custom type usdL2tpTunnelStatusSendSeq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UsdL2tpTunnelStatusSendSeq_Type.__name__ = "Integer32"
_UsdL2tpTunnelStatusSendSeq_Object = MibTableColumn
usdL2tpTunnelStatusSendSeq = _UsdL2tpTunnelStatusSendSeq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 2, 1, 1, 19),
    _UsdL2tpTunnelStatusSendSeq_Type()
)
usdL2tpTunnelStatusSendSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpTunnelStatusSendSeq.setStatus("current")


class _UsdL2tpTunnelStatusSendSeqAck_Type(Integer32):
    """Custom type usdL2tpTunnelStatusSendSeqAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UsdL2tpTunnelStatusSendSeqAck_Type.__name__ = "Integer32"
_UsdL2tpTunnelStatusSendSeqAck_Object = MibTableColumn
usdL2tpTunnelStatusSendSeqAck = _UsdL2tpTunnelStatusSendSeqAck_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 2, 1, 1, 20),
    _UsdL2tpTunnelStatusSendSeqAck_Type()
)
usdL2tpTunnelStatusSendSeqAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpTunnelStatusSendSeqAck.setStatus("current")
_UsdL2tpTunnelStatusTotalSessions_Type = Counter32
_UsdL2tpTunnelStatusTotalSessions_Object = MibTableColumn
usdL2tpTunnelStatusTotalSessions = _UsdL2tpTunnelStatusTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 2, 1, 1, 21),
    _UsdL2tpTunnelStatusTotalSessions_Type()
)
usdL2tpTunnelStatusTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpTunnelStatusTotalSessions.setStatus("current")
_UsdL2tpTunnelStatusFailedSessions_Type = Counter32
_UsdL2tpTunnelStatusFailedSessions_Object = MibTableColumn
usdL2tpTunnelStatusFailedSessions = _UsdL2tpTunnelStatusFailedSessions_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 2, 1, 1, 22),
    _UsdL2tpTunnelStatusFailedSessions_Type()
)
usdL2tpTunnelStatusFailedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpTunnelStatusFailedSessions.setStatus("current")
_UsdL2tpTunnelStatusActiveSessions_Type = Gauge32
_UsdL2tpTunnelStatusActiveSessions_Object = MibTableColumn
usdL2tpTunnelStatusActiveSessions = _UsdL2tpTunnelStatusActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 2, 1, 1, 23),
    _UsdL2tpTunnelStatusActiveSessions_Type()
)
usdL2tpTunnelStatusActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpTunnelStatusActiveSessions.setStatus("current")


class _UsdL2tpTunnelStatusLastResultCode_Type(Integer32):
    """Custom type usdL2tpTunnelStatusLastResultCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UsdL2tpTunnelStatusLastResultCode_Type.__name__ = "Integer32"
_UsdL2tpTunnelStatusLastResultCode_Object = MibTableColumn
usdL2tpTunnelStatusLastResultCode = _UsdL2tpTunnelStatusLastResultCode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 2, 1, 1, 24),
    _UsdL2tpTunnelStatusLastResultCode_Type()
)
usdL2tpTunnelStatusLastResultCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpTunnelStatusLastResultCode.setStatus("current")


class _UsdL2tpTunnelStatusLastErrorCode_Type(Integer32):
    """Custom type usdL2tpTunnelStatusLastErrorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UsdL2tpTunnelStatusLastErrorCode_Type.__name__ = "Integer32"
_UsdL2tpTunnelStatusLastErrorCode_Object = MibTableColumn
usdL2tpTunnelStatusLastErrorCode = _UsdL2tpTunnelStatusLastErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 2, 1, 1, 25),
    _UsdL2tpTunnelStatusLastErrorCode_Type()
)
usdL2tpTunnelStatusLastErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpTunnelStatusLastErrorCode.setStatus("current")
_UsdL2tpTunnelStatusLastErrorMessage_Type = DisplayString
_UsdL2tpTunnelStatusLastErrorMessage_Object = MibTableColumn
usdL2tpTunnelStatusLastErrorMessage = _UsdL2tpTunnelStatusLastErrorMessage_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 2, 1, 1, 26),
    _UsdL2tpTunnelStatusLastErrorMessage_Type()
)
usdL2tpTunnelStatusLastErrorMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpTunnelStatusLastErrorMessage.setStatus("current")
_UsdL2tpTunnelStatusCumEstabTime_Type = Unsigned32
_UsdL2tpTunnelStatusCumEstabTime_Object = MibTableColumn
usdL2tpTunnelStatusCumEstabTime = _UsdL2tpTunnelStatusCumEstabTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 2, 1, 1, 27),
    _UsdL2tpTunnelStatusCumEstabTime_Type()
)
usdL2tpTunnelStatusCumEstabTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpTunnelStatusCumEstabTime.setStatus("current")
if mibBuilder.loadTexts:
    usdL2tpTunnelStatusCumEstabTime.setUnits("seconds")
_UsdL2tpTunnelStatistics_ObjectIdentity = ObjectIdentity
usdL2tpTunnelStatistics = _UsdL2tpTunnelStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 3)
)
_UsdL2tpTunnelStatTable_Object = MibTable
usdL2tpTunnelStatTable = _UsdL2tpTunnelStatTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    usdL2tpTunnelStatTable.setStatus("current")
_UsdL2tpTunnelStatEntry_Object = MibTableRow
usdL2tpTunnelStatEntry = _UsdL2tpTunnelStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 3, 1, 1)
)
usdL2tpTunnelStatEntry.setIndexNames(
    (0, "Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatIfIndex"),
)
if mibBuilder.loadTexts:
    usdL2tpTunnelStatEntry.setStatus("current")
_UsdL2tpTunnelStatIfIndex_Type = InterfaceIndex
_UsdL2tpTunnelStatIfIndex_Object = MibTableColumn
usdL2tpTunnelStatIfIndex = _UsdL2tpTunnelStatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 3, 1, 1, 1),
    _UsdL2tpTunnelStatIfIndex_Type()
)
usdL2tpTunnelStatIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdL2tpTunnelStatIfIndex.setStatus("current")
_UsdL2tpTunnelStatCtlRecvOctets_Type = Counter32
_UsdL2tpTunnelStatCtlRecvOctets_Object = MibTableColumn
usdL2tpTunnelStatCtlRecvOctets = _UsdL2tpTunnelStatCtlRecvOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 3, 1, 1, 2),
    _UsdL2tpTunnelStatCtlRecvOctets_Type()
)
usdL2tpTunnelStatCtlRecvOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpTunnelStatCtlRecvOctets.setStatus("current")
_UsdL2tpTunnelStatCtlRecvPackets_Type = Counter32
_UsdL2tpTunnelStatCtlRecvPackets_Object = MibTableColumn
usdL2tpTunnelStatCtlRecvPackets = _UsdL2tpTunnelStatCtlRecvPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 3, 1, 1, 3),
    _UsdL2tpTunnelStatCtlRecvPackets_Type()
)
usdL2tpTunnelStatCtlRecvPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpTunnelStatCtlRecvPackets.setStatus("current")
_UsdL2tpTunnelStatCtlRecvErrors_Type = Counter32
_UsdL2tpTunnelStatCtlRecvErrors_Object = MibTableColumn
usdL2tpTunnelStatCtlRecvErrors = _UsdL2tpTunnelStatCtlRecvErrors_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 3, 1, 1, 4),
    _UsdL2tpTunnelStatCtlRecvErrors_Type()
)
usdL2tpTunnelStatCtlRecvErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpTunnelStatCtlRecvErrors.setStatus("current")
_UsdL2tpTunnelStatCtlRecvDiscards_Type = Counter32
_UsdL2tpTunnelStatCtlRecvDiscards_Object = MibTableColumn
usdL2tpTunnelStatCtlRecvDiscards = _UsdL2tpTunnelStatCtlRecvDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 3, 1, 1, 5),
    _UsdL2tpTunnelStatCtlRecvDiscards_Type()
)
usdL2tpTunnelStatCtlRecvDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpTunnelStatCtlRecvDiscards.setStatus("current")
_UsdL2tpTunnelStatCtlSendOctets_Type = Counter32
_UsdL2tpTunnelStatCtlSendOctets_Object = MibTableColumn
usdL2tpTunnelStatCtlSendOctets = _UsdL2tpTunnelStatCtlSendOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 3, 1, 1, 6),
    _UsdL2tpTunnelStatCtlSendOctets_Type()
)
usdL2tpTunnelStatCtlSendOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpTunnelStatCtlSendOctets.setStatus("current")
_UsdL2tpTunnelStatCtlSendPackets_Type = Counter32
_UsdL2tpTunnelStatCtlSendPackets_Object = MibTableColumn
usdL2tpTunnelStatCtlSendPackets = _UsdL2tpTunnelStatCtlSendPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 3, 1, 1, 7),
    _UsdL2tpTunnelStatCtlSendPackets_Type()
)
usdL2tpTunnelStatCtlSendPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpTunnelStatCtlSendPackets.setStatus("current")
_UsdL2tpTunnelStatCtlSendErrors_Type = Counter32
_UsdL2tpTunnelStatCtlSendErrors_Object = MibTableColumn
usdL2tpTunnelStatCtlSendErrors = _UsdL2tpTunnelStatCtlSendErrors_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 3, 1, 1, 8),
    _UsdL2tpTunnelStatCtlSendErrors_Type()
)
usdL2tpTunnelStatCtlSendErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpTunnelStatCtlSendErrors.setStatus("current")
_UsdL2tpTunnelStatCtlSendDiscards_Type = Counter32
_UsdL2tpTunnelStatCtlSendDiscards_Object = MibTableColumn
usdL2tpTunnelStatCtlSendDiscards = _UsdL2tpTunnelStatCtlSendDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 3, 1, 1, 9),
    _UsdL2tpTunnelStatCtlSendDiscards_Type()
)
usdL2tpTunnelStatCtlSendDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpTunnelStatCtlSendDiscards.setStatus("current")
_UsdL2tpTunnelStatPayRecvOctets_Type = Counter32
_UsdL2tpTunnelStatPayRecvOctets_Object = MibTableColumn
usdL2tpTunnelStatPayRecvOctets = _UsdL2tpTunnelStatPayRecvOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 3, 1, 1, 10),
    _UsdL2tpTunnelStatPayRecvOctets_Type()
)
usdL2tpTunnelStatPayRecvOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpTunnelStatPayRecvOctets.setStatus("current")
_UsdL2tpTunnelStatPayRecvPackets_Type = Counter32
_UsdL2tpTunnelStatPayRecvPackets_Object = MibTableColumn
usdL2tpTunnelStatPayRecvPackets = _UsdL2tpTunnelStatPayRecvPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 3, 1, 1, 11),
    _UsdL2tpTunnelStatPayRecvPackets_Type()
)
usdL2tpTunnelStatPayRecvPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpTunnelStatPayRecvPackets.setStatus("current")
_UsdL2tpTunnelStatPayRecvErrors_Type = Counter32
_UsdL2tpTunnelStatPayRecvErrors_Object = MibTableColumn
usdL2tpTunnelStatPayRecvErrors = _UsdL2tpTunnelStatPayRecvErrors_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 3, 1, 1, 12),
    _UsdL2tpTunnelStatPayRecvErrors_Type()
)
usdL2tpTunnelStatPayRecvErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpTunnelStatPayRecvErrors.setStatus("current")
_UsdL2tpTunnelStatPayRecvDiscards_Type = Counter32
_UsdL2tpTunnelStatPayRecvDiscards_Object = MibTableColumn
usdL2tpTunnelStatPayRecvDiscards = _UsdL2tpTunnelStatPayRecvDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 3, 1, 1, 13),
    _UsdL2tpTunnelStatPayRecvDiscards_Type()
)
usdL2tpTunnelStatPayRecvDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpTunnelStatPayRecvDiscards.setStatus("current")
_UsdL2tpTunnelStatPaySendOctets_Type = Counter32
_UsdL2tpTunnelStatPaySendOctets_Object = MibTableColumn
usdL2tpTunnelStatPaySendOctets = _UsdL2tpTunnelStatPaySendOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 3, 1, 1, 14),
    _UsdL2tpTunnelStatPaySendOctets_Type()
)
usdL2tpTunnelStatPaySendOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpTunnelStatPaySendOctets.setStatus("current")
_UsdL2tpTunnelStatPaySendPackets_Type = Counter32
_UsdL2tpTunnelStatPaySendPackets_Object = MibTableColumn
usdL2tpTunnelStatPaySendPackets = _UsdL2tpTunnelStatPaySendPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 3, 1, 1, 15),
    _UsdL2tpTunnelStatPaySendPackets_Type()
)
usdL2tpTunnelStatPaySendPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpTunnelStatPaySendPackets.setStatus("current")
_UsdL2tpTunnelStatPaySendErrors_Type = Counter32
_UsdL2tpTunnelStatPaySendErrors_Object = MibTableColumn
usdL2tpTunnelStatPaySendErrors = _UsdL2tpTunnelStatPaySendErrors_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 3, 1, 1, 16),
    _UsdL2tpTunnelStatPaySendErrors_Type()
)
usdL2tpTunnelStatPaySendErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpTunnelStatPaySendErrors.setStatus("current")
_UsdL2tpTunnelStatPaySendDiscards_Type = Counter32
_UsdL2tpTunnelStatPaySendDiscards_Object = MibTableColumn
usdL2tpTunnelStatPaySendDiscards = _UsdL2tpTunnelStatPaySendDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 3, 1, 1, 17),
    _UsdL2tpTunnelStatPaySendDiscards_Type()
)
usdL2tpTunnelStatPaySendDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpTunnelStatPaySendDiscards.setStatus("current")
_UsdL2tpTunnelStatCtlRecvZLB_Type = Counter32
_UsdL2tpTunnelStatCtlRecvZLB_Object = MibTableColumn
usdL2tpTunnelStatCtlRecvZLB = _UsdL2tpTunnelStatCtlRecvZLB_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 3, 1, 1, 18),
    _UsdL2tpTunnelStatCtlRecvZLB_Type()
)
usdL2tpTunnelStatCtlRecvZLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpTunnelStatCtlRecvZLB.setStatus("current")
_UsdL2tpTunnelStatCtlRecvOutOfSequence_Type = Counter32
_UsdL2tpTunnelStatCtlRecvOutOfSequence_Object = MibTableColumn
usdL2tpTunnelStatCtlRecvOutOfSequence = _UsdL2tpTunnelStatCtlRecvOutOfSequence_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 3, 1, 1, 19),
    _UsdL2tpTunnelStatCtlRecvOutOfSequence_Type()
)
usdL2tpTunnelStatCtlRecvOutOfSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpTunnelStatCtlRecvOutOfSequence.setStatus("current")
_UsdL2tpTunnelStatCtlRecvOutOfWindow_Type = Counter32
_UsdL2tpTunnelStatCtlRecvOutOfWindow_Object = MibTableColumn
usdL2tpTunnelStatCtlRecvOutOfWindow = _UsdL2tpTunnelStatCtlRecvOutOfWindow_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 3, 1, 1, 20),
    _UsdL2tpTunnelStatCtlRecvOutOfWindow_Type()
)
usdL2tpTunnelStatCtlRecvOutOfWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpTunnelStatCtlRecvOutOfWindow.setStatus("current")
_UsdL2tpTunnelStatCtlSendZLB_Type = Counter32
_UsdL2tpTunnelStatCtlSendZLB_Object = MibTableColumn
usdL2tpTunnelStatCtlSendZLB = _UsdL2tpTunnelStatCtlSendZLB_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 3, 1, 1, 21),
    _UsdL2tpTunnelStatCtlSendZLB_Type()
)
usdL2tpTunnelStatCtlSendZLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpTunnelStatCtlSendZLB.setStatus("current")
_UsdL2tpTunnelStatCtlSendRetransmits_Type = Counter32
_UsdL2tpTunnelStatCtlSendRetransmits_Object = MibTableColumn
usdL2tpTunnelStatCtlSendRetransmits = _UsdL2tpTunnelStatCtlSendRetransmits_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 3, 1, 1, 22),
    _UsdL2tpTunnelStatCtlSendRetransmits_Type()
)
usdL2tpTunnelStatCtlSendRetransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpTunnelStatCtlSendRetransmits.setStatus("current")
_UsdL2tpTunnelMap_ObjectIdentity = ObjectIdentity
usdL2tpTunnelMap = _UsdL2tpTunnelMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 4)
)
_UsdL2tpMapTifSidToSifTable_Object = MibTable
usdL2tpMapTifSidToSifTable = _UsdL2tpMapTifSidToSifTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 4, 1)
)
if mibBuilder.loadTexts:
    usdL2tpMapTifSidToSifTable.setStatus("current")
_UsdL2tpMapTifSidToSifEntry_Object = MibTableRow
usdL2tpMapTifSidToSifEntry = _UsdL2tpMapTifSidToSifEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 4, 1, 1)
)
usdL2tpMapTifSidToSifEntry.setIndexNames(
    (0, "Unisphere-Data-L2TP-MIB", "usdL2tpMapTifSidToSifTunnelIfIndex"),
    (0, "Unisphere-Data-L2TP-MIB", "usdL2tpMapTifSidToSifLocalSessionId"),
)
if mibBuilder.loadTexts:
    usdL2tpMapTifSidToSifEntry.setStatus("current")
_UsdL2tpMapTifSidToSifTunnelIfIndex_Type = InterfaceIndex
_UsdL2tpMapTifSidToSifTunnelIfIndex_Object = MibTableColumn
usdL2tpMapTifSidToSifTunnelIfIndex = _UsdL2tpMapTifSidToSifTunnelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 4, 1, 1, 1),
    _UsdL2tpMapTifSidToSifTunnelIfIndex_Type()
)
usdL2tpMapTifSidToSifTunnelIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdL2tpMapTifSidToSifTunnelIfIndex.setStatus("current")
_UsdL2tpMapTifSidToSifLocalSessionId_Type = UsdL2tpSessionId
_UsdL2tpMapTifSidToSifLocalSessionId_Object = MibTableColumn
usdL2tpMapTifSidToSifLocalSessionId = _UsdL2tpMapTifSidToSifLocalSessionId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 4, 1, 1, 2),
    _UsdL2tpMapTifSidToSifLocalSessionId_Type()
)
usdL2tpMapTifSidToSifLocalSessionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdL2tpMapTifSidToSifLocalSessionId.setStatus("current")
_UsdL2tpMapTifSidToSifSessionIfIndex_Type = InterfaceIndex
_UsdL2tpMapTifSidToSifSessionIfIndex_Object = MibTableColumn
usdL2tpMapTifSidToSifSessionIfIndex = _UsdL2tpMapTifSidToSifSessionIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 4, 1, 1, 3),
    _UsdL2tpMapTifSidToSifSessionIfIndex_Type()
)
usdL2tpMapTifSidToSifSessionIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpMapTifSidToSifSessionIfIndex.setStatus("current")
_UsdL2tpMapTidToTifTable_Object = MibTable
usdL2tpMapTidToTifTable = _UsdL2tpMapTidToTifTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 4, 2)
)
if mibBuilder.loadTexts:
    usdL2tpMapTidToTifTable.setStatus("current")
_UsdL2tpMapTidToTifEntry_Object = MibTableRow
usdL2tpMapTidToTifEntry = _UsdL2tpMapTidToTifEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 4, 2, 1)
)
usdL2tpMapTidToTifEntry.setIndexNames(
    (0, "Unisphere-Data-L2TP-MIB", "usdL2tpMapTidToTifLocalTunnelId"),
)
if mibBuilder.loadTexts:
    usdL2tpMapTidToTifEntry.setStatus("current")
_UsdL2tpMapTidToTifLocalTunnelId_Type = UsdL2tpTunnelId
_UsdL2tpMapTidToTifLocalTunnelId_Object = MibTableColumn
usdL2tpMapTidToTifLocalTunnelId = _UsdL2tpMapTidToTifLocalTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 4, 2, 1, 1),
    _UsdL2tpMapTidToTifLocalTunnelId_Type()
)
usdL2tpMapTidToTifLocalTunnelId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdL2tpMapTidToTifLocalTunnelId.setStatus("current")
_UsdL2tpMapTidToTifIfIndex_Type = InterfaceIndex
_UsdL2tpMapTidToTifIfIndex_Object = MibTableColumn
usdL2tpMapTidToTifIfIndex = _UsdL2tpMapTidToTifIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 3, 4, 2, 1, 2),
    _UsdL2tpMapTidToTifIfIndex_Type()
)
usdL2tpMapTidToTifIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpMapTidToTifIfIndex.setStatus("current")
_UsdL2tpSession_ObjectIdentity = ObjectIdentity
usdL2tpSession = _UsdL2tpSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4)
)
_UsdL2tpSessionConfig_ObjectIdentity = ObjectIdentity
usdL2tpSessionConfig = _UsdL2tpSessionConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 1)
)
_UsdL2tpSessionConfigTable_Object = MibTable
usdL2tpSessionConfigTable = _UsdL2tpSessionConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 1, 2)
)
if mibBuilder.loadTexts:
    usdL2tpSessionConfigTable.setStatus("current")
_UsdL2tpSessionConfigEntry_Object = MibTableRow
usdL2tpSessionConfigEntry = _UsdL2tpSessionConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 1, 2, 1)
)
usdL2tpSessionConfigEntry.setIndexNames(
    (0, "Unisphere-Data-L2TP-MIB", "usdL2tpSessionConfigIfIndex"),
)
if mibBuilder.loadTexts:
    usdL2tpSessionConfigEntry.setStatus("current")
_UsdL2tpSessionConfigIfIndex_Type = InterfaceIndex
_UsdL2tpSessionConfigIfIndex_Object = MibTableColumn
usdL2tpSessionConfigIfIndex = _UsdL2tpSessionConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 1, 2, 1, 1),
    _UsdL2tpSessionConfigIfIndex_Type()
)
usdL2tpSessionConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdL2tpSessionConfigIfIndex.setStatus("current")
_UsdL2tpSessionConfigRowStatus_Type = RowStatus
_UsdL2tpSessionConfigRowStatus_Object = MibTableColumn
usdL2tpSessionConfigRowStatus = _UsdL2tpSessionConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 1, 2, 1, 2),
    _UsdL2tpSessionConfigRowStatus_Type()
)
usdL2tpSessionConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdL2tpSessionConfigRowStatus.setStatus("current")


class _UsdL2tpSessionConfigAdminState_Type(UsdL2tpAdminState):
    """Custom type usdL2tpSessionConfigAdminState based on UsdL2tpAdminState"""


_UsdL2tpSessionConfigAdminState_Object = MibTableColumn
usdL2tpSessionConfigAdminState = _UsdL2tpSessionConfigAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 1, 2, 1, 3),
    _UsdL2tpSessionConfigAdminState_Type()
)
usdL2tpSessionConfigAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdL2tpSessionConfigAdminState.setStatus("current")
_UsdL2tpSessionStatus_ObjectIdentity = ObjectIdentity
usdL2tpSessionStatus = _UsdL2tpSessionStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 2)
)
_UsdL2tpSessionStatusTable_Object = MibTable
usdL2tpSessionStatusTable = _UsdL2tpSessionStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    usdL2tpSessionStatusTable.setStatus("current")
_UsdL2tpSessionStatusEntry_Object = MibTableRow
usdL2tpSessionStatusEntry = _UsdL2tpSessionStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 2, 1, 1)
)
usdL2tpSessionStatusEntry.setIndexNames(
    (0, "Unisphere-Data-L2TP-MIB", "usdL2tpSessionStatusIfIndex"),
)
if mibBuilder.loadTexts:
    usdL2tpSessionStatusEntry.setStatus("current")
_UsdL2tpSessionStatusIfIndex_Type = InterfaceIndex
_UsdL2tpSessionStatusIfIndex_Object = MibTableColumn
usdL2tpSessionStatusIfIndex = _UsdL2tpSessionStatusIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 2, 1, 1, 1),
    _UsdL2tpSessionStatusIfIndex_Type()
)
usdL2tpSessionStatusIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdL2tpSessionStatusIfIndex.setStatus("current")
_UsdL2tpSessionStatusLacPppIfIndex_Type = InterfaceIndexOrZero
_UsdL2tpSessionStatusLacPppIfIndex_Object = MibTableColumn
usdL2tpSessionStatusLacPppIfIndex = _UsdL2tpSessionStatusLacPppIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 2, 1, 1, 2),
    _UsdL2tpSessionStatusLacPppIfIndex_Type()
)
usdL2tpSessionStatusLacPppIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpSessionStatusLacPppIfIndex.setStatus("deprecated")
_UsdL2tpSessionStatusLocalSessionId_Type = UsdL2tpSessionId
_UsdL2tpSessionStatusLocalSessionId_Object = MibTableColumn
usdL2tpSessionStatusLocalSessionId = _UsdL2tpSessionStatusLocalSessionId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 2, 1, 1, 3),
    _UsdL2tpSessionStatusLocalSessionId_Type()
)
usdL2tpSessionStatusLocalSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpSessionStatusLocalSessionId.setStatus("current")
_UsdL2tpSessionStatusRemoteSessionId_Type = UsdL2tpSessionId
_UsdL2tpSessionStatusRemoteSessionId_Object = MibTableColumn
usdL2tpSessionStatusRemoteSessionId = _UsdL2tpSessionStatusRemoteSessionId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 2, 1, 1, 4),
    _UsdL2tpSessionStatusRemoteSessionId_Type()
)
usdL2tpSessionStatusRemoteSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpSessionStatusRemoteSessionId.setStatus("current")
_UsdL2tpSessionStatusUserName_Type = DisplayString
_UsdL2tpSessionStatusUserName_Object = MibTableColumn
usdL2tpSessionStatusUserName = _UsdL2tpSessionStatusUserName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 2, 1, 1, 5),
    _UsdL2tpSessionStatusUserName_Type()
)
usdL2tpSessionStatusUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpSessionStatusUserName.setStatus("current")
_UsdL2tpSessionStatusEffectiveAdminState_Type = UsdL2tpAdminState
_UsdL2tpSessionStatusEffectiveAdminState_Object = MibTableColumn
usdL2tpSessionStatusEffectiveAdminState = _UsdL2tpSessionStatusEffectiveAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 2, 1, 1, 6),
    _UsdL2tpSessionStatusEffectiveAdminState_Type()
)
usdL2tpSessionStatusEffectiveAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpSessionStatusEffectiveAdminState.setStatus("current")


class _UsdL2tpSessionStatusState_Type(Integer32):
    """Custom type usdL2tpSessionStatusState based on Integer32"""
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
        *(("connecting", 1),
          ("disconnecting", 3),
          ("established", 2),
          ("idle", 0))
    )


_UsdL2tpSessionStatusState_Type.__name__ = "Integer32"
_UsdL2tpSessionStatusState_Object = MibTableColumn
usdL2tpSessionStatusState = _UsdL2tpSessionStatusState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 2, 1, 1, 7),
    _UsdL2tpSessionStatusState_Type()
)
usdL2tpSessionStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpSessionStatusState.setStatus("current")


class _UsdL2tpSessionStatusCallType_Type(Integer32):
    """Custom type usdL2tpSessionStatusCallType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("lacIncoming", 1),
          ("lacOutgoing", 3),
          ("lnsIncoming", 2),
          ("lnsOutgoing", 4),
          ("none", 0))
    )


_UsdL2tpSessionStatusCallType_Type.__name__ = "Integer32"
_UsdL2tpSessionStatusCallType_Object = MibTableColumn
usdL2tpSessionStatusCallType = _UsdL2tpSessionStatusCallType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 2, 1, 1, 8),
    _UsdL2tpSessionStatusCallType_Type()
)
usdL2tpSessionStatusCallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpSessionStatusCallType.setStatus("current")
_UsdL2tpSessionStatusCallSerialNumber_Type = Integer32
_UsdL2tpSessionStatusCallSerialNumber_Object = MibTableColumn
usdL2tpSessionStatusCallSerialNumber = _UsdL2tpSessionStatusCallSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 2, 1, 1, 9),
    _UsdL2tpSessionStatusCallSerialNumber_Type()
)
usdL2tpSessionStatusCallSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpSessionStatusCallSerialNumber.setStatus("current")
_UsdL2tpSessionStatusTxConnectSpeed_Type = Integer32
_UsdL2tpSessionStatusTxConnectSpeed_Object = MibTableColumn
usdL2tpSessionStatusTxConnectSpeed = _UsdL2tpSessionStatusTxConnectSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 2, 1, 1, 10),
    _UsdL2tpSessionStatusTxConnectSpeed_Type()
)
usdL2tpSessionStatusTxConnectSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpSessionStatusTxConnectSpeed.setStatus("current")
_UsdL2tpSessionStatusRxConnectSpeed_Type = Integer32
_UsdL2tpSessionStatusRxConnectSpeed_Object = MibTableColumn
usdL2tpSessionStatusRxConnectSpeed = _UsdL2tpSessionStatusRxConnectSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 2, 1, 1, 11),
    _UsdL2tpSessionStatusRxConnectSpeed_Type()
)
usdL2tpSessionStatusRxConnectSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpSessionStatusRxConnectSpeed.setStatus("current")


class _UsdL2tpSessionStatusCallBearerType_Type(Integer32):
    """Custom type usdL2tpSessionStatusCallBearerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("analog", 2),
          ("digital", 1),
          ("none", 0))
    )


_UsdL2tpSessionStatusCallBearerType_Type.__name__ = "Integer32"
_UsdL2tpSessionStatusCallBearerType_Object = MibTableColumn
usdL2tpSessionStatusCallBearerType = _UsdL2tpSessionStatusCallBearerType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 2, 1, 1, 12),
    _UsdL2tpSessionStatusCallBearerType_Type()
)
usdL2tpSessionStatusCallBearerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpSessionStatusCallBearerType.setStatus("current")


class _UsdL2tpSessionStatusFramingType_Type(Integer32):
    """Custom type usdL2tpSessionStatusFramingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("async", 2),
          ("none", 0),
          ("sync", 1))
    )


_UsdL2tpSessionStatusFramingType_Type.__name__ = "Integer32"
_UsdL2tpSessionStatusFramingType_Object = MibTableColumn
usdL2tpSessionStatusFramingType = _UsdL2tpSessionStatusFramingType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 2, 1, 1, 13),
    _UsdL2tpSessionStatusFramingType_Type()
)
usdL2tpSessionStatusFramingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpSessionStatusFramingType.setStatus("current")
_UsdL2tpSessionStatusPhysChanId_Type = Integer32
_UsdL2tpSessionStatusPhysChanId_Object = MibTableColumn
usdL2tpSessionStatusPhysChanId = _UsdL2tpSessionStatusPhysChanId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 2, 1, 1, 14),
    _UsdL2tpSessionStatusPhysChanId_Type()
)
usdL2tpSessionStatusPhysChanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpSessionStatusPhysChanId.setStatus("current")
_UsdL2tpSessionStatusDnis_Type = DisplayString
_UsdL2tpSessionStatusDnis_Object = MibTableColumn
usdL2tpSessionStatusDnis = _UsdL2tpSessionStatusDnis_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 2, 1, 1, 15),
    _UsdL2tpSessionStatusDnis_Type()
)
usdL2tpSessionStatusDnis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpSessionStatusDnis.setStatus("current")
_UsdL2tpSessionStatusClid_Type = DisplayString
_UsdL2tpSessionStatusClid_Object = MibTableColumn
usdL2tpSessionStatusClid = _UsdL2tpSessionStatusClid_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 2, 1, 1, 16),
    _UsdL2tpSessionStatusClid_Type()
)
usdL2tpSessionStatusClid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpSessionStatusClid.setStatus("current")
_UsdL2tpSessionStatusSubAddress_Type = DisplayString
_UsdL2tpSessionStatusSubAddress_Object = MibTableColumn
usdL2tpSessionStatusSubAddress = _UsdL2tpSessionStatusSubAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 2, 1, 1, 17),
    _UsdL2tpSessionStatusSubAddress_Type()
)
usdL2tpSessionStatusSubAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpSessionStatusSubAddress.setStatus("current")
_UsdL2tpSessionStatusPrivateGroupId_Type = DisplayString
_UsdL2tpSessionStatusPrivateGroupId_Object = MibTableColumn
usdL2tpSessionStatusPrivateGroupId = _UsdL2tpSessionStatusPrivateGroupId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 2, 1, 1, 18),
    _UsdL2tpSessionStatusPrivateGroupId_Type()
)
usdL2tpSessionStatusPrivateGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpSessionStatusPrivateGroupId.setStatus("current")
_UsdL2tpSessionStatusProxyLcp_Type = TruthValue
_UsdL2tpSessionStatusProxyLcp_Object = MibTableColumn
usdL2tpSessionStatusProxyLcp = _UsdL2tpSessionStatusProxyLcp_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 2, 1, 1, 19),
    _UsdL2tpSessionStatusProxyLcp_Type()
)
usdL2tpSessionStatusProxyLcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpSessionStatusProxyLcp.setStatus("current")


class _UsdL2tpSessionStatusAuthMethod_Type(Integer32):
    """Custom type usdL2tpSessionStatusAuthMethod based on Integer32"""
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
        *(("none", 0),
          ("pppChap", 1),
          ("pppMsChap", 3),
          ("pppPap", 2))
    )


_UsdL2tpSessionStatusAuthMethod_Type.__name__ = "Integer32"
_UsdL2tpSessionStatusAuthMethod_Object = MibTableColumn
usdL2tpSessionStatusAuthMethod = _UsdL2tpSessionStatusAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 2, 1, 1, 20),
    _UsdL2tpSessionStatusAuthMethod_Type()
)
usdL2tpSessionStatusAuthMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpSessionStatusAuthMethod.setStatus("current")


class _UsdL2tpSessionStatusSequencingState_Type(Integer32):
    """Custom type usdL2tpSessionStatusSequencingState based on Integer32"""
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
        *(("both", 3),
          ("local", 2),
          ("none", 0),
          ("remote", 1))
    )


_UsdL2tpSessionStatusSequencingState_Type.__name__ = "Integer32"
_UsdL2tpSessionStatusSequencingState_Object = MibTableColumn
usdL2tpSessionStatusSequencingState = _UsdL2tpSessionStatusSequencingState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 2, 1, 1, 21),
    _UsdL2tpSessionStatusSequencingState_Type()
)
usdL2tpSessionStatusSequencingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpSessionStatusSequencingState.setStatus("current")


class _UsdL2tpSessionStatusSendSeq_Type(Integer32):
    """Custom type usdL2tpSessionStatusSendSeq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UsdL2tpSessionStatusSendSeq_Type.__name__ = "Integer32"
_UsdL2tpSessionStatusSendSeq_Object = MibTableColumn
usdL2tpSessionStatusSendSeq = _UsdL2tpSessionStatusSendSeq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 2, 1, 1, 22),
    _UsdL2tpSessionStatusSendSeq_Type()
)
usdL2tpSessionStatusSendSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpSessionStatusSendSeq.setStatus("current")


class _UsdL2tpSessionStatusRecvSeq_Type(Integer32):
    """Custom type usdL2tpSessionStatusRecvSeq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UsdL2tpSessionStatusRecvSeq_Type.__name__ = "Integer32"
_UsdL2tpSessionStatusRecvSeq_Object = MibTableColumn
usdL2tpSessionStatusRecvSeq = _UsdL2tpSessionStatusRecvSeq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 2, 1, 1, 23),
    _UsdL2tpSessionStatusRecvSeq_Type()
)
usdL2tpSessionStatusRecvSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpSessionStatusRecvSeq.setStatus("current")
_UsdL2tpSessionStatusLacTunneledIfIndex_Type = InterfaceIndexOrZero
_UsdL2tpSessionStatusLacTunneledIfIndex_Object = MibTableColumn
usdL2tpSessionStatusLacTunneledIfIndex = _UsdL2tpSessionStatusLacTunneledIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 2, 1, 1, 24),
    _UsdL2tpSessionStatusLacTunneledIfIndex_Type()
)
usdL2tpSessionStatusLacTunneledIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpSessionStatusLacTunneledIfIndex.setStatus("current")
_UsdL2tpSessionStatusCumEstabTime_Type = Unsigned32
_UsdL2tpSessionStatusCumEstabTime_Object = MibTableColumn
usdL2tpSessionStatusCumEstabTime = _UsdL2tpSessionStatusCumEstabTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 2, 1, 1, 25),
    _UsdL2tpSessionStatusCumEstabTime_Type()
)
usdL2tpSessionStatusCumEstabTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpSessionStatusCumEstabTime.setStatus("current")
if mibBuilder.loadTexts:
    usdL2tpSessionStatusCumEstabTime.setUnits("seconds")
_UsdL2tpSessionStatistics_ObjectIdentity = ObjectIdentity
usdL2tpSessionStatistics = _UsdL2tpSessionStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 3)
)
_UsdL2tpSessionStatTable_Object = MibTable
usdL2tpSessionStatTable = _UsdL2tpSessionStatTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 3, 1)
)
if mibBuilder.loadTexts:
    usdL2tpSessionStatTable.setStatus("current")
_UsdL2tpSessionStatEntry_Object = MibTableRow
usdL2tpSessionStatEntry = _UsdL2tpSessionStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 3, 1, 1)
)
usdL2tpSessionStatEntry.setIndexNames(
    (0, "Unisphere-Data-L2TP-MIB", "usdL2tpSessionStatIfIndex"),
)
if mibBuilder.loadTexts:
    usdL2tpSessionStatEntry.setStatus("current")
_UsdL2tpSessionStatIfIndex_Type = InterfaceIndex
_UsdL2tpSessionStatIfIndex_Object = MibTableColumn
usdL2tpSessionStatIfIndex = _UsdL2tpSessionStatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 3, 1, 1, 1),
    _UsdL2tpSessionStatIfIndex_Type()
)
usdL2tpSessionStatIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdL2tpSessionStatIfIndex.setStatus("current")
_UsdL2tpSessionStatPayRecvOctets_Type = Counter32
_UsdL2tpSessionStatPayRecvOctets_Object = MibTableColumn
usdL2tpSessionStatPayRecvOctets = _UsdL2tpSessionStatPayRecvOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 3, 1, 1, 2),
    _UsdL2tpSessionStatPayRecvOctets_Type()
)
usdL2tpSessionStatPayRecvOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpSessionStatPayRecvOctets.setStatus("current")
_UsdL2tpSessionStatPayRecvPackets_Type = Counter32
_UsdL2tpSessionStatPayRecvPackets_Object = MibTableColumn
usdL2tpSessionStatPayRecvPackets = _UsdL2tpSessionStatPayRecvPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 3, 1, 1, 3),
    _UsdL2tpSessionStatPayRecvPackets_Type()
)
usdL2tpSessionStatPayRecvPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpSessionStatPayRecvPackets.setStatus("current")
_UsdL2tpSessionStatPayRecvErrors_Type = Counter32
_UsdL2tpSessionStatPayRecvErrors_Object = MibTableColumn
usdL2tpSessionStatPayRecvErrors = _UsdL2tpSessionStatPayRecvErrors_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 3, 1, 1, 4),
    _UsdL2tpSessionStatPayRecvErrors_Type()
)
usdL2tpSessionStatPayRecvErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpSessionStatPayRecvErrors.setStatus("current")
_UsdL2tpSessionStatPayRecvDiscards_Type = Counter32
_UsdL2tpSessionStatPayRecvDiscards_Object = MibTableColumn
usdL2tpSessionStatPayRecvDiscards = _UsdL2tpSessionStatPayRecvDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 3, 1, 1, 5),
    _UsdL2tpSessionStatPayRecvDiscards_Type()
)
usdL2tpSessionStatPayRecvDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpSessionStatPayRecvDiscards.setStatus("current")
_UsdL2tpSessionStatPaySendOctets_Type = Counter32
_UsdL2tpSessionStatPaySendOctets_Object = MibTableColumn
usdL2tpSessionStatPaySendOctets = _UsdL2tpSessionStatPaySendOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 3, 1, 1, 6),
    _UsdL2tpSessionStatPaySendOctets_Type()
)
usdL2tpSessionStatPaySendOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpSessionStatPaySendOctets.setStatus("current")
_UsdL2tpSessionStatPaySendPackets_Type = Counter32
_UsdL2tpSessionStatPaySendPackets_Object = MibTableColumn
usdL2tpSessionStatPaySendPackets = _UsdL2tpSessionStatPaySendPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 3, 1, 1, 7),
    _UsdL2tpSessionStatPaySendPackets_Type()
)
usdL2tpSessionStatPaySendPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpSessionStatPaySendPackets.setStatus("current")
_UsdL2tpSessionStatPaySendErrors_Type = Counter32
_UsdL2tpSessionStatPaySendErrors_Object = MibTableColumn
usdL2tpSessionStatPaySendErrors = _UsdL2tpSessionStatPaySendErrors_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 3, 1, 1, 8),
    _UsdL2tpSessionStatPaySendErrors_Type()
)
usdL2tpSessionStatPaySendErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpSessionStatPaySendErrors.setStatus("current")
_UsdL2tpSessionStatPaySendDiscards_Type = Counter32
_UsdL2tpSessionStatPaySendDiscards_Object = MibTableColumn
usdL2tpSessionStatPaySendDiscards = _UsdL2tpSessionStatPaySendDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 3, 1, 1, 9),
    _UsdL2tpSessionStatPaySendDiscards_Type()
)
usdL2tpSessionStatPaySendDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpSessionStatPaySendDiscards.setStatus("current")
_UsdL2tpSessionStatRecvOutOfSequence_Type = Counter32
_UsdL2tpSessionStatRecvOutOfSequence_Object = MibTableColumn
usdL2tpSessionStatRecvOutOfSequence = _UsdL2tpSessionStatRecvOutOfSequence_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 3, 1, 1, 10),
    _UsdL2tpSessionStatRecvOutOfSequence_Type()
)
usdL2tpSessionStatRecvOutOfSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpSessionStatRecvOutOfSequence.setStatus("current")
_UsdL2tpSessionStatResequencingTimeouts_Type = Counter32
_UsdL2tpSessionStatResequencingTimeouts_Object = MibTableColumn
usdL2tpSessionStatResequencingTimeouts = _UsdL2tpSessionStatResequencingTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 3, 1, 1, 11),
    _UsdL2tpSessionStatResequencingTimeouts_Type()
)
usdL2tpSessionStatResequencingTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpSessionStatResequencingTimeouts.setStatus("current")
_UsdL2tpSessionStatPayLostPackets_Type = Unsigned32
_UsdL2tpSessionStatPayLostPackets_Object = MibTableColumn
usdL2tpSessionStatPayLostPackets = _UsdL2tpSessionStatPayLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 4, 3, 1, 1, 12),
    _UsdL2tpSessionStatPayLostPackets_Type()
)
usdL2tpSessionStatPayLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpSessionStatPayLostPackets.setStatus("current")
_UsdL2tpTransport_ObjectIdentity = ObjectIdentity
usdL2tpTransport = _UsdL2tpTransport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 5)
)
_UsdL2tpTransportUdpIp_ObjectIdentity = ObjectIdentity
usdL2tpTransportUdpIp = _UsdL2tpTransportUdpIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 5, 1)
)
_UsdL2tpUdpIpSystem_ObjectIdentity = ObjectIdentity
usdL2tpUdpIpSystem = _UsdL2tpUdpIpSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 5, 1, 1)
)
_UsdL2tpUdpIpDestination_ObjectIdentity = ObjectIdentity
usdL2tpUdpIpDestination = _UsdL2tpUdpIpDestination_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 5, 1, 2)
)
_UsdL2tpUdpIpDestTable_Object = MibTable
usdL2tpUdpIpDestTable = _UsdL2tpUdpIpDestTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 5, 1, 2, 1)
)
if mibBuilder.loadTexts:
    usdL2tpUdpIpDestTable.setStatus("current")
_UsdL2tpUdpIpDestEntry_Object = MibTableRow
usdL2tpUdpIpDestEntry = _UsdL2tpUdpIpDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 5, 1, 2, 1, 1)
)
usdL2tpUdpIpDestEntry.setIndexNames(
    (0, "Unisphere-Data-L2TP-MIB", "usdL2tpUdpIpDestIfIndex"),
)
if mibBuilder.loadTexts:
    usdL2tpUdpIpDestEntry.setStatus("current")
_UsdL2tpUdpIpDestIfIndex_Type = InterfaceIndex
_UsdL2tpUdpIpDestIfIndex_Object = MibTableColumn
usdL2tpUdpIpDestIfIndex = _UsdL2tpUdpIpDestIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 5, 1, 2, 1, 1, 1),
    _UsdL2tpUdpIpDestIfIndex_Type()
)
usdL2tpUdpIpDestIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdL2tpUdpIpDestIfIndex.setStatus("current")
_UsdL2tpUdpIpDestRouterIndex_Type = Unsigned32
_UsdL2tpUdpIpDestRouterIndex_Object = MibTableColumn
usdL2tpUdpIpDestRouterIndex = _UsdL2tpUdpIpDestRouterIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 5, 1, 2, 1, 1, 2),
    _UsdL2tpUdpIpDestRouterIndex_Type()
)
usdL2tpUdpIpDestRouterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpUdpIpDestRouterIndex.setStatus("current")
_UsdL2tpUdpIpDestLocalAddress_Type = IpAddress
_UsdL2tpUdpIpDestLocalAddress_Object = MibTableColumn
usdL2tpUdpIpDestLocalAddress = _UsdL2tpUdpIpDestLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 5, 1, 2, 1, 1, 3),
    _UsdL2tpUdpIpDestLocalAddress_Type()
)
usdL2tpUdpIpDestLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpUdpIpDestLocalAddress.setStatus("current")
_UsdL2tpUdpIpDestRemoteAddress_Type = IpAddress
_UsdL2tpUdpIpDestRemoteAddress_Object = MibTableColumn
usdL2tpUdpIpDestRemoteAddress = _UsdL2tpUdpIpDestRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 5, 1, 2, 1, 1, 4),
    _UsdL2tpUdpIpDestRemoteAddress_Type()
)
usdL2tpUdpIpDestRemoteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpUdpIpDestRemoteAddress.setStatus("current")
_UsdL2tpUdpIpTunnel_ObjectIdentity = ObjectIdentity
usdL2tpUdpIpTunnel = _UsdL2tpUdpIpTunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 5, 1, 3)
)
_UsdL2tpUdpIpTunnelTable_Object = MibTable
usdL2tpUdpIpTunnelTable = _UsdL2tpUdpIpTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 5, 1, 3, 1)
)
if mibBuilder.loadTexts:
    usdL2tpUdpIpTunnelTable.setStatus("current")
_UsdL2tpUdpIpTunnelEntry_Object = MibTableRow
usdL2tpUdpIpTunnelEntry = _UsdL2tpUdpIpTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 5, 1, 3, 1, 1)
)
usdL2tpUdpIpTunnelEntry.setIndexNames(
    (0, "Unisphere-Data-L2TP-MIB", "usdL2tpUdpIpTunnelIfIndex"),
)
if mibBuilder.loadTexts:
    usdL2tpUdpIpTunnelEntry.setStatus("current")
_UsdL2tpUdpIpTunnelIfIndex_Type = InterfaceIndex
_UsdL2tpUdpIpTunnelIfIndex_Object = MibTableColumn
usdL2tpUdpIpTunnelIfIndex = _UsdL2tpUdpIpTunnelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 5, 1, 3, 1, 1, 1),
    _UsdL2tpUdpIpTunnelIfIndex_Type()
)
usdL2tpUdpIpTunnelIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdL2tpUdpIpTunnelIfIndex.setStatus("current")
_UsdL2tpUdpIpTunnelRouterIndex_Type = Unsigned32
_UsdL2tpUdpIpTunnelRouterIndex_Object = MibTableColumn
usdL2tpUdpIpTunnelRouterIndex = _UsdL2tpUdpIpTunnelRouterIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 5, 1, 3, 1, 1, 2),
    _UsdL2tpUdpIpTunnelRouterIndex_Type()
)
usdL2tpUdpIpTunnelRouterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpUdpIpTunnelRouterIndex.setStatus("current")
_UsdL2tpUdpIpTunnelLocalAddress_Type = IpAddress
_UsdL2tpUdpIpTunnelLocalAddress_Object = MibTableColumn
usdL2tpUdpIpTunnelLocalAddress = _UsdL2tpUdpIpTunnelLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 5, 1, 3, 1, 1, 3),
    _UsdL2tpUdpIpTunnelLocalAddress_Type()
)
usdL2tpUdpIpTunnelLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpUdpIpTunnelLocalAddress.setStatus("current")
_UsdL2tpUdpIpTunnelLocalPort_Type = Integer32
_UsdL2tpUdpIpTunnelLocalPort_Object = MibTableColumn
usdL2tpUdpIpTunnelLocalPort = _UsdL2tpUdpIpTunnelLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 5, 1, 3, 1, 1, 4),
    _UsdL2tpUdpIpTunnelLocalPort_Type()
)
usdL2tpUdpIpTunnelLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpUdpIpTunnelLocalPort.setStatus("current")
_UsdL2tpUdpIpTunnelRemoteAddress_Type = IpAddress
_UsdL2tpUdpIpTunnelRemoteAddress_Object = MibTableColumn
usdL2tpUdpIpTunnelRemoteAddress = _UsdL2tpUdpIpTunnelRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 5, 1, 3, 1, 1, 5),
    _UsdL2tpUdpIpTunnelRemoteAddress_Type()
)
usdL2tpUdpIpTunnelRemoteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpUdpIpTunnelRemoteAddress.setStatus("current")
_UsdL2tpUdpIpTunnelRemotePort_Type = Integer32
_UsdL2tpUdpIpTunnelRemotePort_Object = MibTableColumn
usdL2tpUdpIpTunnelRemotePort = _UsdL2tpUdpIpTunnelRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 5, 1, 3, 1, 1, 6),
    _UsdL2tpUdpIpTunnelRemotePort_Type()
)
usdL2tpUdpIpTunnelRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2tpUdpIpTunnelRemotePort.setStatus("current")
_UsdL2tpUdpIpSession_ObjectIdentity = ObjectIdentity
usdL2tpUdpIpSession = _UsdL2tpUdpIpSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 1, 5, 1, 4)
)
_UsdL2tpTrapControl_ObjectIdentity = ObjectIdentity
usdL2tpTrapControl = _UsdL2tpTrapControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 2)
)
_UsdL2tpConformance_ObjectIdentity = ObjectIdentity
usdL2tpConformance = _UsdL2tpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 3)
)
_UsdL2tpGroups_ObjectIdentity = ObjectIdentity
usdL2tpGroups = _UsdL2tpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 3, 1)
)
_UsdL2tpCompliances_ObjectIdentity = ObjectIdentity
usdL2tpCompliances = _UsdL2tpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 3, 2)
)

# Managed Objects groups

usdL2tpConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 3, 1, 1)
)
usdL2tpConfigGroup.setObjects(
      *(("Unisphere-Data-L2TP-MIB", "usdL2tpSysConfigAdminState"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSysConfigDestructTimeout"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSysConfigIpChecksumEnable"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpDestConfigRowStatus"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpDestConfigAdminState"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelConfigRowStatus"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelConfigAdminState"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionConfigRowStatus"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionConfigAdminState"))
)
if mibBuilder.loadTexts:
    usdL2tpConfigGroup.setStatus("obsolete")

usdL2tpStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 3, 1, 2)
)
usdL2tpStatusGroup.setObjects(
      *(("Unisphere-Data-L2TP-MIB", "usdL2tpSysStatusProtocolVersion"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSysStatusVendorName"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSysStatusFirmwareRev"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSysStatusTotalDestinations"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSysStatusFailedDestinations"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSysStatusActiveDestinations"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSysStatusTotalTunnels"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSysStatusFailedTunnels"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSysStatusFailedTunnelAuthens"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSysStatusActiveTunnels"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSysStatusTotalSessions"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSysStatusFailedSessions"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSysStatusActiveSessions"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpDestStatusEffectiveAdminState"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpDestStatusTotalTunnels"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpDestStatusFailedTunnels"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpDestStatusFailedTunnelAuthens"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpDestStatusActiveTunnels"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpDestStatusTotalSessions"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpDestStatusFailedSessions"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpDestStatusActiveSessions"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatusEffectiveAdminState"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatusLocalTunnelId"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatusRemoteTunnelId"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatusState"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatusInitiated"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatusRemoteHostName"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatusRemoteVendorName"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatusRemoteFirmwareRevision"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatusRemoteProtocolVersion"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatusRemoteBearerCapabilities"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatusRemoteFramingCapabilities"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatusRecvWindowSize"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatusSendWindowSize"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatusSendQueueDepth"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatusRecvSeq"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatusRecvSeqAck"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatusSendSeq"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatusSendSeqAck"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatusTotalSessions"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatusFailedSessions"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatusActiveSessions"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatusLastResultCode"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatusLastErrorCode"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatusLastErrorMessage"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionStatusLacPppIfIndex"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionStatusLocalSessionId"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionStatusRemoteSessionId"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionStatusUserName"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionStatusState"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionStatusCallType"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionStatusCallSerialNumber"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionStatusTxConnectSpeed"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionStatusRxConnectSpeed"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionStatusCallBearerType"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionStatusFramingType"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionStatusPhysChanId"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionStatusDnis"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionStatusClid"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionStatusSubAddress"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionStatusPrivateGroupId"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionStatusProxyLcp"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionStatusAuthMethod"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionStatusSequencingState"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionStatusSendSeq"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionStatusRecvSeq"))
)
if mibBuilder.loadTexts:
    usdL2tpStatusGroup.setStatus("obsolete")

usdL2tpStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 3, 1, 3)
)
usdL2tpStatGroup.setObjects(
      *(("Unisphere-Data-L2TP-MIB", "usdL2tpDestStatCtlRecvOctets"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpDestStatCtlRecvPackets"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpDestStatCtlRecvErrors"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpDestStatCtlRecvDiscards"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpDestStatCtlSendOctets"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpDestStatCtlSendPackets"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpDestStatCtlSendErrors"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpDestStatCtlSendDiscards"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpDestStatPayRecvOctets"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpDestStatPayRecvPackets"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpDestStatPayRecvErrors"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpDestStatPayRecvDiscards"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpDestStatPaySendOctets"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpDestStatPaySendPackets"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpDestStatPaySendErrors"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpDestStatPaySendDiscards"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatCtlRecvOctets"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatCtlRecvPackets"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatCtlRecvErrors"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatCtlRecvDiscards"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatCtlSendOctets"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatCtlSendPackets"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatCtlSendErrors"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatCtlSendDiscards"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatPayRecvOctets"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatPayRecvPackets"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatPayRecvErrors"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatPayRecvDiscards"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatPaySendOctets"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatPaySendPackets"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatPaySendErrors"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatPaySendDiscards"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatCtlRecvZLB"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatCtlRecvOutOfSequence"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatCtlRecvOutOfWindow"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatCtlSendZLB"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatCtlSendRetransmits"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionStatPayRecvOctets"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionStatPayRecvPackets"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionStatPayRecvErrors"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionStatPayRecvDiscards"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionStatPaySendOctets"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionStatPaySendPackets"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionStatPaySendErrors"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionStatPaySendDiscards"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionStatRecvOutOfSequence"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionStatResequencingTimeouts"))
)
if mibBuilder.loadTexts:
    usdL2tpStatGroup.setStatus("obsolete")

usdL2tpMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 3, 1, 4)
)
usdL2tpMapGroup.setObjects(
      *(("Unisphere-Data-L2TP-MIB", "usdL2tpMapTifSidToSifSessionIfIndex"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpMapTidToTifIfIndex"))
)
if mibBuilder.loadTexts:
    usdL2tpMapGroup.setStatus("current")

usdL2tpUdpIpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 3, 1, 5)
)
usdL2tpUdpIpGroup.setObjects(
      *(("Unisphere-Data-L2TP-MIB", "usdL2tpUdpIpDestRouterIndex"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpUdpIpDestLocalAddress"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpUdpIpDestRemoteAddress"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpUdpIpTunnelRouterIndex"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpUdpIpTunnelLocalAddress"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpUdpIpTunnelLocalPort"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpUdpIpTunnelRemoteAddress"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpUdpIpTunnelRemotePort"))
)
if mibBuilder.loadTexts:
    usdL2tpUdpIpGroup.setStatus("current")

usdL2tpStatusGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 3, 1, 6)
)
usdL2tpStatusGroup2.setObjects(
      *(("Unisphere-Data-L2TP-MIB", "usdL2tpSysStatusProtocolVersion"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSysStatusVendorName"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSysStatusFirmwareRev"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSysStatusTotalDestinations"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSysStatusFailedDestinations"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSysStatusActiveDestinations"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSysStatusTotalTunnels"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSysStatusFailedTunnels"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSysStatusFailedTunnelAuthens"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSysStatusActiveTunnels"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSysStatusTotalSessions"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSysStatusFailedSessions"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSysStatusActiveSessions"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpDestStatusTransport"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpDestStatusEffectiveAdminState"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpDestStatusTotalTunnels"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpDestStatusFailedTunnels"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpDestStatusFailedTunnelAuthens"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpDestStatusActiveTunnels"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpDestStatusTotalSessions"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpDestStatusFailedSessions"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpDestStatusActiveSessions"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatusTransport"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatusLocalTunnelId"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatusRemoteTunnelId"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatusEffectiveAdminState"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatusState"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatusInitiated"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatusRemoteHostName"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatusRemoteVendorName"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatusRemoteFirmwareRevision"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatusRemoteProtocolVersion"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatusRemoteBearerCapabilities"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatusRemoteFramingCapabilities"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatusRecvWindowSize"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatusSendWindowSize"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatusSendQueueDepth"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatusRecvSeq"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatusRecvSeqAck"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatusSendSeq"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatusSendSeqAck"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatusTotalSessions"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatusFailedSessions"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatusActiveSessions"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatusLastResultCode"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatusLastErrorCode"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatusLastErrorMessage"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatusCumEstabTime"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionStatusLocalSessionId"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionStatusRemoteSessionId"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionStatusUserName"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionStatusEffectiveAdminState"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionStatusState"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionStatusCallType"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionStatusCallSerialNumber"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionStatusTxConnectSpeed"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionStatusRxConnectSpeed"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionStatusCallBearerType"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionStatusFramingType"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionStatusPhysChanId"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionStatusDnis"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionStatusClid"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionStatusSubAddress"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionStatusPrivateGroupId"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionStatusProxyLcp"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionStatusAuthMethod"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionStatusSequencingState"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionStatusSendSeq"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionStatusRecvSeq"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionStatusLacTunneledIfIndex"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionStatusCumEstabTime"))
)
if mibBuilder.loadTexts:
    usdL2tpStatusGroup2.setStatus("current")

usdL2tpStatGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 3, 1, 7)
)
usdL2tpStatGroup2.setObjects(
      *(("Unisphere-Data-L2TP-MIB", "usdL2tpDestStatCtlRecvOctets"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpDestStatCtlRecvPackets"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpDestStatCtlRecvErrors"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpDestStatCtlRecvDiscards"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpDestStatCtlSendOctets"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpDestStatCtlSendPackets"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpDestStatCtlSendErrors"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpDestStatCtlSendDiscards"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpDestStatPayRecvOctets"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpDestStatPayRecvPackets"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpDestStatPayRecvErrors"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpDestStatPayRecvDiscards"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpDestStatPaySendOctets"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpDestStatPaySendPackets"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpDestStatPaySendErrors"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpDestStatPaySendDiscards"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatCtlRecvOctets"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatCtlRecvPackets"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatCtlRecvErrors"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatCtlRecvDiscards"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatCtlSendOctets"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatCtlSendPackets"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatCtlSendErrors"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatCtlSendDiscards"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatPayRecvOctets"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatPayRecvPackets"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatPayRecvErrors"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatPayRecvDiscards"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatPaySendOctets"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatPaySendPackets"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatPaySendErrors"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatPaySendDiscards"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatCtlRecvZLB"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatCtlRecvOutOfSequence"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatCtlRecvOutOfWindow"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatCtlSendZLB"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelStatCtlSendRetransmits"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionStatPayRecvOctets"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionStatPayRecvPackets"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionStatPayRecvErrors"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionStatPayRecvDiscards"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionStatPaySendOctets"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionStatPaySendPackets"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionStatPaySendErrors"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionStatPaySendDiscards"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionStatRecvOutOfSequence"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionStatResequencingTimeouts"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionStatPayLostPackets"))
)
if mibBuilder.loadTexts:
    usdL2tpStatGroup2.setStatus("current")

usdL2tpConfigGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 3, 1, 8)
)
usdL2tpConfigGroup2.setObjects(
      *(("Unisphere-Data-L2TP-MIB", "usdL2tpSysConfigAdminState"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSysConfigDestructTimeout"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSysConfigIpChecksumEnable"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSysConfigReceiveDataSequencingIgnore"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpDestConfigRowStatus"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpDestConfigAdminState"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelConfigRowStatus"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelConfigAdminState"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionConfigRowStatus"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionConfigAdminState"))
)
if mibBuilder.loadTexts:
    usdL2tpConfigGroup2.setStatus("obsolete")

usdL2tpConfigGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 3, 1, 9)
)
usdL2tpConfigGroup3.setObjects(
      *(("Unisphere-Data-L2TP-MIB", "usdL2tpSysConfigAdminState"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSysConfigDestructTimeout"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSysConfigIpChecksumEnable"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSysConfigTunnelSwitchingEnabled"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSysConfigControlRetransmissions"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSysConfigTunnelIdleTimeout"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSysConfigReceiveDataSequencingIgnore"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpDestConfigRowStatus"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpDestConfigAdminState"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelConfigRowStatus"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpTunnelConfigAdminState"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionConfigRowStatus"),
        ("Unisphere-Data-L2TP-MIB", "usdL2tpSessionConfigAdminState"))
)
if mibBuilder.loadTexts:
    usdL2tpConfigGroup3.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

usdL2tpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 3, 2, 1)
)
if mibBuilder.loadTexts:
    usdL2tpCompliance.setStatus(
        "obsolete"
    )

usdL2tpCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 3, 2, 2)
)
if mibBuilder.loadTexts:
    usdL2tpCompliance2.setStatus(
        "obsolete"
    )

usdL2tpCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 3, 2, 3)
)
if mibBuilder.loadTexts:
    usdL2tpCompliance3.setStatus(
        "obsolete"
    )

usdL2tpCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 35, 3, 2, 4)
)
if mibBuilder.loadTexts:
    usdL2tpCompliance4.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-L2TP-MIB",
    **{"UsdL2tpTunnelId": UsdL2tpTunnelId,
       "UsdL2tpSessionId": UsdL2tpSessionId,
       "UsdL2tpAdminState": UsdL2tpAdminState,
       "UsdL2tpTransport": UsdL2tpTransport,
       "usdL2tpMIB": usdL2tpMIB,
       "usdL2tpTraps": usdL2tpTraps,
       "usdL2tpObjects": usdL2tpObjects,
       "usdL2tpSystem": usdL2tpSystem,
       "usdL2tpSystemConfig": usdL2tpSystemConfig,
       "usdL2tpSysConfigAdminState": usdL2tpSysConfigAdminState,
       "usdL2tpSysConfigDestructTimeout": usdL2tpSysConfigDestructTimeout,
       "usdL2tpSysConfigIpChecksumEnable": usdL2tpSysConfigIpChecksumEnable,
       "usdL2tpSysConfigTunnelSwitchingEnabled": usdL2tpSysConfigTunnelSwitchingEnabled,
       "usdL2tpSysConfigControlRetransmissions": usdL2tpSysConfigControlRetransmissions,
       "usdL2tpSysConfigTunnelIdleTimeout": usdL2tpSysConfigTunnelIdleTimeout,
       "usdL2tpSysConfigReceiveDataSequencingIgnore": usdL2tpSysConfigReceiveDataSequencingIgnore,
       "usdL2tpSystemStatus": usdL2tpSystemStatus,
       "usdL2tpSysStatusProtocolVersion": usdL2tpSysStatusProtocolVersion,
       "usdL2tpSysStatusVendorName": usdL2tpSysStatusVendorName,
       "usdL2tpSysStatusFirmwareRev": usdL2tpSysStatusFirmwareRev,
       "usdL2tpSysStatusTotalDestinations": usdL2tpSysStatusTotalDestinations,
       "usdL2tpSysStatusFailedDestinations": usdL2tpSysStatusFailedDestinations,
       "usdL2tpSysStatusActiveDestinations": usdL2tpSysStatusActiveDestinations,
       "usdL2tpSysStatusTotalTunnels": usdL2tpSysStatusTotalTunnels,
       "usdL2tpSysStatusFailedTunnels": usdL2tpSysStatusFailedTunnels,
       "usdL2tpSysStatusFailedTunnelAuthens": usdL2tpSysStatusFailedTunnelAuthens,
       "usdL2tpSysStatusActiveTunnels": usdL2tpSysStatusActiveTunnels,
       "usdL2tpSysStatusTotalSessions": usdL2tpSysStatusTotalSessions,
       "usdL2tpSysStatusFailedSessions": usdL2tpSysStatusFailedSessions,
       "usdL2tpSysStatusActiveSessions": usdL2tpSysStatusActiveSessions,
       "usdL2tpDestination": usdL2tpDestination,
       "usdL2tpDestConfig": usdL2tpDestConfig,
       "usdL2tpDestConfigTable": usdL2tpDestConfigTable,
       "usdL2tpDestConfigEntry": usdL2tpDestConfigEntry,
       "usdL2tpDestConfigIfIndex": usdL2tpDestConfigIfIndex,
       "usdL2tpDestConfigRowStatus": usdL2tpDestConfigRowStatus,
       "usdL2tpDestConfigAdminState": usdL2tpDestConfigAdminState,
       "usdL2tpDestStatus": usdL2tpDestStatus,
       "usdL2tpDestStatusTable": usdL2tpDestStatusTable,
       "usdL2tpDestStatusEntry": usdL2tpDestStatusEntry,
       "usdL2tpDestStatusIfIndex": usdL2tpDestStatusIfIndex,
       "usdL2tpDestStatusTransport": usdL2tpDestStatusTransport,
       "usdL2tpDestStatusEffectiveAdminState": usdL2tpDestStatusEffectiveAdminState,
       "usdL2tpDestStatusTotalTunnels": usdL2tpDestStatusTotalTunnels,
       "usdL2tpDestStatusFailedTunnels": usdL2tpDestStatusFailedTunnels,
       "usdL2tpDestStatusFailedTunnelAuthens": usdL2tpDestStatusFailedTunnelAuthens,
       "usdL2tpDestStatusActiveTunnels": usdL2tpDestStatusActiveTunnels,
       "usdL2tpDestStatusTotalSessions": usdL2tpDestStatusTotalSessions,
       "usdL2tpDestStatusFailedSessions": usdL2tpDestStatusFailedSessions,
       "usdL2tpDestStatusActiveSessions": usdL2tpDestStatusActiveSessions,
       "usdL2tpDestStatistics": usdL2tpDestStatistics,
       "usdL2tpDestStatTable": usdL2tpDestStatTable,
       "usdL2tpDestStatEntry": usdL2tpDestStatEntry,
       "usdL2tpDestStatIfIndex": usdL2tpDestStatIfIndex,
       "usdL2tpDestStatCtlRecvOctets": usdL2tpDestStatCtlRecvOctets,
       "usdL2tpDestStatCtlRecvPackets": usdL2tpDestStatCtlRecvPackets,
       "usdL2tpDestStatCtlRecvErrors": usdL2tpDestStatCtlRecvErrors,
       "usdL2tpDestStatCtlRecvDiscards": usdL2tpDestStatCtlRecvDiscards,
       "usdL2tpDestStatCtlSendOctets": usdL2tpDestStatCtlSendOctets,
       "usdL2tpDestStatCtlSendPackets": usdL2tpDestStatCtlSendPackets,
       "usdL2tpDestStatCtlSendErrors": usdL2tpDestStatCtlSendErrors,
       "usdL2tpDestStatCtlSendDiscards": usdL2tpDestStatCtlSendDiscards,
       "usdL2tpDestStatPayRecvOctets": usdL2tpDestStatPayRecvOctets,
       "usdL2tpDestStatPayRecvPackets": usdL2tpDestStatPayRecvPackets,
       "usdL2tpDestStatPayRecvErrors": usdL2tpDestStatPayRecvErrors,
       "usdL2tpDestStatPayRecvDiscards": usdL2tpDestStatPayRecvDiscards,
       "usdL2tpDestStatPaySendOctets": usdL2tpDestStatPaySendOctets,
       "usdL2tpDestStatPaySendPackets": usdL2tpDestStatPaySendPackets,
       "usdL2tpDestStatPaySendErrors": usdL2tpDestStatPaySendErrors,
       "usdL2tpDestStatPaySendDiscards": usdL2tpDestStatPaySendDiscards,
       "usdL2tpTunnel": usdL2tpTunnel,
       "usdL2tpTunnelConfig": usdL2tpTunnelConfig,
       "usdL2tpTunnelConfigTable": usdL2tpTunnelConfigTable,
       "usdL2tpTunnelConfigEntry": usdL2tpTunnelConfigEntry,
       "usdL2tpTunnelConfigIfIndex": usdL2tpTunnelConfigIfIndex,
       "usdL2tpTunnelConfigRowStatus": usdL2tpTunnelConfigRowStatus,
       "usdL2tpTunnelConfigAdminState": usdL2tpTunnelConfigAdminState,
       "usdL2tpTunnelStatus": usdL2tpTunnelStatus,
       "usdL2tpTunnelStatusTable": usdL2tpTunnelStatusTable,
       "usdL2tpTunnelStatusEntry": usdL2tpTunnelStatusEntry,
       "usdL2tpTunnelStatusIfIndex": usdL2tpTunnelStatusIfIndex,
       "usdL2tpTunnelStatusTransport": usdL2tpTunnelStatusTransport,
       "usdL2tpTunnelStatusLocalTunnelId": usdL2tpTunnelStatusLocalTunnelId,
       "usdL2tpTunnelStatusRemoteTunnelId": usdL2tpTunnelStatusRemoteTunnelId,
       "usdL2tpTunnelStatusEffectiveAdminState": usdL2tpTunnelStatusEffectiveAdminState,
       "usdL2tpTunnelStatusState": usdL2tpTunnelStatusState,
       "usdL2tpTunnelStatusInitiated": usdL2tpTunnelStatusInitiated,
       "usdL2tpTunnelStatusRemoteHostName": usdL2tpTunnelStatusRemoteHostName,
       "usdL2tpTunnelStatusRemoteVendorName": usdL2tpTunnelStatusRemoteVendorName,
       "usdL2tpTunnelStatusRemoteFirmwareRevision": usdL2tpTunnelStatusRemoteFirmwareRevision,
       "usdL2tpTunnelStatusRemoteProtocolVersion": usdL2tpTunnelStatusRemoteProtocolVersion,
       "usdL2tpTunnelStatusRemoteBearerCapabilities": usdL2tpTunnelStatusRemoteBearerCapabilities,
       "usdL2tpTunnelStatusRemoteFramingCapabilities": usdL2tpTunnelStatusRemoteFramingCapabilities,
       "usdL2tpTunnelStatusRecvWindowSize": usdL2tpTunnelStatusRecvWindowSize,
       "usdL2tpTunnelStatusSendWindowSize": usdL2tpTunnelStatusSendWindowSize,
       "usdL2tpTunnelStatusSendQueueDepth": usdL2tpTunnelStatusSendQueueDepth,
       "usdL2tpTunnelStatusRecvSeq": usdL2tpTunnelStatusRecvSeq,
       "usdL2tpTunnelStatusRecvSeqAck": usdL2tpTunnelStatusRecvSeqAck,
       "usdL2tpTunnelStatusSendSeq": usdL2tpTunnelStatusSendSeq,
       "usdL2tpTunnelStatusSendSeqAck": usdL2tpTunnelStatusSendSeqAck,
       "usdL2tpTunnelStatusTotalSessions": usdL2tpTunnelStatusTotalSessions,
       "usdL2tpTunnelStatusFailedSessions": usdL2tpTunnelStatusFailedSessions,
       "usdL2tpTunnelStatusActiveSessions": usdL2tpTunnelStatusActiveSessions,
       "usdL2tpTunnelStatusLastResultCode": usdL2tpTunnelStatusLastResultCode,
       "usdL2tpTunnelStatusLastErrorCode": usdL2tpTunnelStatusLastErrorCode,
       "usdL2tpTunnelStatusLastErrorMessage": usdL2tpTunnelStatusLastErrorMessage,
       "usdL2tpTunnelStatusCumEstabTime": usdL2tpTunnelStatusCumEstabTime,
       "usdL2tpTunnelStatistics": usdL2tpTunnelStatistics,
       "usdL2tpTunnelStatTable": usdL2tpTunnelStatTable,
       "usdL2tpTunnelStatEntry": usdL2tpTunnelStatEntry,
       "usdL2tpTunnelStatIfIndex": usdL2tpTunnelStatIfIndex,
       "usdL2tpTunnelStatCtlRecvOctets": usdL2tpTunnelStatCtlRecvOctets,
       "usdL2tpTunnelStatCtlRecvPackets": usdL2tpTunnelStatCtlRecvPackets,
       "usdL2tpTunnelStatCtlRecvErrors": usdL2tpTunnelStatCtlRecvErrors,
       "usdL2tpTunnelStatCtlRecvDiscards": usdL2tpTunnelStatCtlRecvDiscards,
       "usdL2tpTunnelStatCtlSendOctets": usdL2tpTunnelStatCtlSendOctets,
       "usdL2tpTunnelStatCtlSendPackets": usdL2tpTunnelStatCtlSendPackets,
       "usdL2tpTunnelStatCtlSendErrors": usdL2tpTunnelStatCtlSendErrors,
       "usdL2tpTunnelStatCtlSendDiscards": usdL2tpTunnelStatCtlSendDiscards,
       "usdL2tpTunnelStatPayRecvOctets": usdL2tpTunnelStatPayRecvOctets,
       "usdL2tpTunnelStatPayRecvPackets": usdL2tpTunnelStatPayRecvPackets,
       "usdL2tpTunnelStatPayRecvErrors": usdL2tpTunnelStatPayRecvErrors,
       "usdL2tpTunnelStatPayRecvDiscards": usdL2tpTunnelStatPayRecvDiscards,
       "usdL2tpTunnelStatPaySendOctets": usdL2tpTunnelStatPaySendOctets,
       "usdL2tpTunnelStatPaySendPackets": usdL2tpTunnelStatPaySendPackets,
       "usdL2tpTunnelStatPaySendErrors": usdL2tpTunnelStatPaySendErrors,
       "usdL2tpTunnelStatPaySendDiscards": usdL2tpTunnelStatPaySendDiscards,
       "usdL2tpTunnelStatCtlRecvZLB": usdL2tpTunnelStatCtlRecvZLB,
       "usdL2tpTunnelStatCtlRecvOutOfSequence": usdL2tpTunnelStatCtlRecvOutOfSequence,
       "usdL2tpTunnelStatCtlRecvOutOfWindow": usdL2tpTunnelStatCtlRecvOutOfWindow,
       "usdL2tpTunnelStatCtlSendZLB": usdL2tpTunnelStatCtlSendZLB,
       "usdL2tpTunnelStatCtlSendRetransmits": usdL2tpTunnelStatCtlSendRetransmits,
       "usdL2tpTunnelMap": usdL2tpTunnelMap,
       "usdL2tpMapTifSidToSifTable": usdL2tpMapTifSidToSifTable,
       "usdL2tpMapTifSidToSifEntry": usdL2tpMapTifSidToSifEntry,
       "usdL2tpMapTifSidToSifTunnelIfIndex": usdL2tpMapTifSidToSifTunnelIfIndex,
       "usdL2tpMapTifSidToSifLocalSessionId": usdL2tpMapTifSidToSifLocalSessionId,
       "usdL2tpMapTifSidToSifSessionIfIndex": usdL2tpMapTifSidToSifSessionIfIndex,
       "usdL2tpMapTidToTifTable": usdL2tpMapTidToTifTable,
       "usdL2tpMapTidToTifEntry": usdL2tpMapTidToTifEntry,
       "usdL2tpMapTidToTifLocalTunnelId": usdL2tpMapTidToTifLocalTunnelId,
       "usdL2tpMapTidToTifIfIndex": usdL2tpMapTidToTifIfIndex,
       "usdL2tpSession": usdL2tpSession,
       "usdL2tpSessionConfig": usdL2tpSessionConfig,
       "usdL2tpSessionConfigTable": usdL2tpSessionConfigTable,
       "usdL2tpSessionConfigEntry": usdL2tpSessionConfigEntry,
       "usdL2tpSessionConfigIfIndex": usdL2tpSessionConfigIfIndex,
       "usdL2tpSessionConfigRowStatus": usdL2tpSessionConfigRowStatus,
       "usdL2tpSessionConfigAdminState": usdL2tpSessionConfigAdminState,
       "usdL2tpSessionStatus": usdL2tpSessionStatus,
       "usdL2tpSessionStatusTable": usdL2tpSessionStatusTable,
       "usdL2tpSessionStatusEntry": usdL2tpSessionStatusEntry,
       "usdL2tpSessionStatusIfIndex": usdL2tpSessionStatusIfIndex,
       "usdL2tpSessionStatusLacPppIfIndex": usdL2tpSessionStatusLacPppIfIndex,
       "usdL2tpSessionStatusLocalSessionId": usdL2tpSessionStatusLocalSessionId,
       "usdL2tpSessionStatusRemoteSessionId": usdL2tpSessionStatusRemoteSessionId,
       "usdL2tpSessionStatusUserName": usdL2tpSessionStatusUserName,
       "usdL2tpSessionStatusEffectiveAdminState": usdL2tpSessionStatusEffectiveAdminState,
       "usdL2tpSessionStatusState": usdL2tpSessionStatusState,
       "usdL2tpSessionStatusCallType": usdL2tpSessionStatusCallType,
       "usdL2tpSessionStatusCallSerialNumber": usdL2tpSessionStatusCallSerialNumber,
       "usdL2tpSessionStatusTxConnectSpeed": usdL2tpSessionStatusTxConnectSpeed,
       "usdL2tpSessionStatusRxConnectSpeed": usdL2tpSessionStatusRxConnectSpeed,
       "usdL2tpSessionStatusCallBearerType": usdL2tpSessionStatusCallBearerType,
       "usdL2tpSessionStatusFramingType": usdL2tpSessionStatusFramingType,
       "usdL2tpSessionStatusPhysChanId": usdL2tpSessionStatusPhysChanId,
       "usdL2tpSessionStatusDnis": usdL2tpSessionStatusDnis,
       "usdL2tpSessionStatusClid": usdL2tpSessionStatusClid,
       "usdL2tpSessionStatusSubAddress": usdL2tpSessionStatusSubAddress,
       "usdL2tpSessionStatusPrivateGroupId": usdL2tpSessionStatusPrivateGroupId,
       "usdL2tpSessionStatusProxyLcp": usdL2tpSessionStatusProxyLcp,
       "usdL2tpSessionStatusAuthMethod": usdL2tpSessionStatusAuthMethod,
       "usdL2tpSessionStatusSequencingState": usdL2tpSessionStatusSequencingState,
       "usdL2tpSessionStatusSendSeq": usdL2tpSessionStatusSendSeq,
       "usdL2tpSessionStatusRecvSeq": usdL2tpSessionStatusRecvSeq,
       "usdL2tpSessionStatusLacTunneledIfIndex": usdL2tpSessionStatusLacTunneledIfIndex,
       "usdL2tpSessionStatusCumEstabTime": usdL2tpSessionStatusCumEstabTime,
       "usdL2tpSessionStatistics": usdL2tpSessionStatistics,
       "usdL2tpSessionStatTable": usdL2tpSessionStatTable,
       "usdL2tpSessionStatEntry": usdL2tpSessionStatEntry,
       "usdL2tpSessionStatIfIndex": usdL2tpSessionStatIfIndex,
       "usdL2tpSessionStatPayRecvOctets": usdL2tpSessionStatPayRecvOctets,
       "usdL2tpSessionStatPayRecvPackets": usdL2tpSessionStatPayRecvPackets,
       "usdL2tpSessionStatPayRecvErrors": usdL2tpSessionStatPayRecvErrors,
       "usdL2tpSessionStatPayRecvDiscards": usdL2tpSessionStatPayRecvDiscards,
       "usdL2tpSessionStatPaySendOctets": usdL2tpSessionStatPaySendOctets,
       "usdL2tpSessionStatPaySendPackets": usdL2tpSessionStatPaySendPackets,
       "usdL2tpSessionStatPaySendErrors": usdL2tpSessionStatPaySendErrors,
       "usdL2tpSessionStatPaySendDiscards": usdL2tpSessionStatPaySendDiscards,
       "usdL2tpSessionStatRecvOutOfSequence": usdL2tpSessionStatRecvOutOfSequence,
       "usdL2tpSessionStatResequencingTimeouts": usdL2tpSessionStatResequencingTimeouts,
       "usdL2tpSessionStatPayLostPackets": usdL2tpSessionStatPayLostPackets,
       "usdL2tpTransport": usdL2tpTransport,
       "usdL2tpTransportUdpIp": usdL2tpTransportUdpIp,
       "usdL2tpUdpIpSystem": usdL2tpUdpIpSystem,
       "usdL2tpUdpIpDestination": usdL2tpUdpIpDestination,
       "usdL2tpUdpIpDestTable": usdL2tpUdpIpDestTable,
       "usdL2tpUdpIpDestEntry": usdL2tpUdpIpDestEntry,
       "usdL2tpUdpIpDestIfIndex": usdL2tpUdpIpDestIfIndex,
       "usdL2tpUdpIpDestRouterIndex": usdL2tpUdpIpDestRouterIndex,
       "usdL2tpUdpIpDestLocalAddress": usdL2tpUdpIpDestLocalAddress,
       "usdL2tpUdpIpDestRemoteAddress": usdL2tpUdpIpDestRemoteAddress,
       "usdL2tpUdpIpTunnel": usdL2tpUdpIpTunnel,
       "usdL2tpUdpIpTunnelTable": usdL2tpUdpIpTunnelTable,
       "usdL2tpUdpIpTunnelEntry": usdL2tpUdpIpTunnelEntry,
       "usdL2tpUdpIpTunnelIfIndex": usdL2tpUdpIpTunnelIfIndex,
       "usdL2tpUdpIpTunnelRouterIndex": usdL2tpUdpIpTunnelRouterIndex,
       "usdL2tpUdpIpTunnelLocalAddress": usdL2tpUdpIpTunnelLocalAddress,
       "usdL2tpUdpIpTunnelLocalPort": usdL2tpUdpIpTunnelLocalPort,
       "usdL2tpUdpIpTunnelRemoteAddress": usdL2tpUdpIpTunnelRemoteAddress,
       "usdL2tpUdpIpTunnelRemotePort": usdL2tpUdpIpTunnelRemotePort,
       "usdL2tpUdpIpSession": usdL2tpUdpIpSession,
       "usdL2tpTrapControl": usdL2tpTrapControl,
       "usdL2tpConformance": usdL2tpConformance,
       "usdL2tpGroups": usdL2tpGroups,
       "usdL2tpConfigGroup": usdL2tpConfigGroup,
       "usdL2tpStatusGroup": usdL2tpStatusGroup,
       "usdL2tpStatGroup": usdL2tpStatGroup,
       "usdL2tpMapGroup": usdL2tpMapGroup,
       "usdL2tpUdpIpGroup": usdL2tpUdpIpGroup,
       "usdL2tpStatusGroup2": usdL2tpStatusGroup2,
       "usdL2tpStatGroup2": usdL2tpStatGroup2,
       "usdL2tpConfigGroup2": usdL2tpConfigGroup2,
       "usdL2tpConfigGroup3": usdL2tpConfigGroup3,
       "usdL2tpCompliances": usdL2tpCompliances,
       "usdL2tpCompliance": usdL2tpCompliance,
       "usdL2tpCompliance2": usdL2tpCompliance2,
       "usdL2tpCompliance3": usdL2tpCompliance3,
       "usdL2tpCompliance4": usdL2tpCompliance4}
)
