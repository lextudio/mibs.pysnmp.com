# SNMP MIB module (Unisphere-Data-L2F-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-L2F-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:11:03 2024
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

usdL2fMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53)
)
usdL2fMIB.setRevisions(
        ("2001-09-25 13:54",
         "2001-09-19 18:07")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class UsdL2fTunnelId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class UsdL2fSessionId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class UsdL2fAdminState(Integer32, TextualConvention):
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



class UsdL2fTransport(Integer32, TextualConvention):
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

_UsdL2fTraps_ObjectIdentity = ObjectIdentity
usdL2fTraps = _UsdL2fTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 0)
)
_UsdL2fObjects_ObjectIdentity = ObjectIdentity
usdL2fObjects = _UsdL2fObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1)
)
_UsdL2fSystem_ObjectIdentity = ObjectIdentity
usdL2fSystem = _UsdL2fSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 1)
)
_UsdL2fSystemConfig_ObjectIdentity = ObjectIdentity
usdL2fSystemConfig = _UsdL2fSystemConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 1, 1)
)
_UsdL2fSysConfigAdminState_Type = UsdL2fAdminState
_UsdL2fSysConfigAdminState_Object = MibScalar
usdL2fSysConfigAdminState = _UsdL2fSysConfigAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 1, 1, 1),
    _UsdL2fSysConfigAdminState_Type()
)
usdL2fSysConfigAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdL2fSysConfigAdminState.setStatus("current")


class _UsdL2fSysConfigDestructTimeout_Type(Integer32):
    """Custom type usdL2fSysConfigDestructTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_UsdL2fSysConfigDestructTimeout_Type.__name__ = "Integer32"
_UsdL2fSysConfigDestructTimeout_Object = MibScalar
usdL2fSysConfigDestructTimeout = _UsdL2fSysConfigDestructTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 1, 1, 2),
    _UsdL2fSysConfigDestructTimeout_Type()
)
usdL2fSysConfigDestructTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdL2fSysConfigDestructTimeout.setStatus("current")
if mibBuilder.loadTexts:
    usdL2fSysConfigDestructTimeout.setUnits("seconds")
_UsdL2fSysConfigIpChecksumEnable_Type = UsdEnable
_UsdL2fSysConfigIpChecksumEnable_Object = MibScalar
usdL2fSysConfigIpChecksumEnable = _UsdL2fSysConfigIpChecksumEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 1, 1, 3),
    _UsdL2fSysConfigIpChecksumEnable_Type()
)
usdL2fSysConfigIpChecksumEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdL2fSysConfigIpChecksumEnable.setStatus("current")
_UsdL2fSysConfigReceiveDataSequencingIgnore_Type = UsdEnable
_UsdL2fSysConfigReceiveDataSequencingIgnore_Object = MibScalar
usdL2fSysConfigReceiveDataSequencingIgnore = _UsdL2fSysConfigReceiveDataSequencingIgnore_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 1, 1, 4),
    _UsdL2fSysConfigReceiveDataSequencingIgnore_Type()
)
usdL2fSysConfigReceiveDataSequencingIgnore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdL2fSysConfigReceiveDataSequencingIgnore.setStatus("current")
_UsdL2fSystemStatus_ObjectIdentity = ObjectIdentity
usdL2fSystemStatus = _UsdL2fSystemStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 1, 2)
)


class _UsdL2fSysStatusProtocolVersion_Type(OctetString):
    """Custom type usdL2fSysStatusProtocolVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 256),
    )


_UsdL2fSysStatusProtocolVersion_Type.__name__ = "OctetString"
_UsdL2fSysStatusProtocolVersion_Object = MibScalar
usdL2fSysStatusProtocolVersion = _UsdL2fSysStatusProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 1, 2, 1),
    _UsdL2fSysStatusProtocolVersion_Type()
)
usdL2fSysStatusProtocolVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fSysStatusProtocolVersion.setStatus("current")
_UsdL2fSysStatusVendorName_Type = DisplayString
_UsdL2fSysStatusVendorName_Object = MibScalar
usdL2fSysStatusVendorName = _UsdL2fSysStatusVendorName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 1, 2, 2),
    _UsdL2fSysStatusVendorName_Type()
)
usdL2fSysStatusVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fSysStatusVendorName.setStatus("current")
_UsdL2fSysStatusFirmwareRev_Type = Integer32
_UsdL2fSysStatusFirmwareRev_Object = MibScalar
usdL2fSysStatusFirmwareRev = _UsdL2fSysStatusFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 1, 2, 3),
    _UsdL2fSysStatusFirmwareRev_Type()
)
usdL2fSysStatusFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fSysStatusFirmwareRev.setStatus("current")
_UsdL2fSysStatusTotalDestinations_Type = Counter32
_UsdL2fSysStatusTotalDestinations_Object = MibScalar
usdL2fSysStatusTotalDestinations = _UsdL2fSysStatusTotalDestinations_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 1, 2, 4),
    _UsdL2fSysStatusTotalDestinations_Type()
)
usdL2fSysStatusTotalDestinations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fSysStatusTotalDestinations.setStatus("current")
_UsdL2fSysStatusFailedDestinations_Type = Counter32
_UsdL2fSysStatusFailedDestinations_Object = MibScalar
usdL2fSysStatusFailedDestinations = _UsdL2fSysStatusFailedDestinations_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 1, 2, 5),
    _UsdL2fSysStatusFailedDestinations_Type()
)
usdL2fSysStatusFailedDestinations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fSysStatusFailedDestinations.setStatus("current")
_UsdL2fSysStatusActiveDestinations_Type = Gauge32
_UsdL2fSysStatusActiveDestinations_Object = MibScalar
usdL2fSysStatusActiveDestinations = _UsdL2fSysStatusActiveDestinations_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 1, 2, 6),
    _UsdL2fSysStatusActiveDestinations_Type()
)
usdL2fSysStatusActiveDestinations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fSysStatusActiveDestinations.setStatus("current")
_UsdL2fSysStatusTotalTunnels_Type = Counter32
_UsdL2fSysStatusTotalTunnels_Object = MibScalar
usdL2fSysStatusTotalTunnels = _UsdL2fSysStatusTotalTunnels_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 1, 2, 7),
    _UsdL2fSysStatusTotalTunnels_Type()
)
usdL2fSysStatusTotalTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fSysStatusTotalTunnels.setStatus("current")
_UsdL2fSysStatusFailedTunnels_Type = Counter32
_UsdL2fSysStatusFailedTunnels_Object = MibScalar
usdL2fSysStatusFailedTunnels = _UsdL2fSysStatusFailedTunnels_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 1, 2, 8),
    _UsdL2fSysStatusFailedTunnels_Type()
)
usdL2fSysStatusFailedTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fSysStatusFailedTunnels.setStatus("current")
_UsdL2fSysStatusFailedTunnelAuthens_Type = Counter32
_UsdL2fSysStatusFailedTunnelAuthens_Object = MibScalar
usdL2fSysStatusFailedTunnelAuthens = _UsdL2fSysStatusFailedTunnelAuthens_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 1, 2, 9),
    _UsdL2fSysStatusFailedTunnelAuthens_Type()
)
usdL2fSysStatusFailedTunnelAuthens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fSysStatusFailedTunnelAuthens.setStatus("current")
_UsdL2fSysStatusActiveTunnels_Type = Gauge32
_UsdL2fSysStatusActiveTunnels_Object = MibScalar
usdL2fSysStatusActiveTunnels = _UsdL2fSysStatusActiveTunnels_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 1, 2, 10),
    _UsdL2fSysStatusActiveTunnels_Type()
)
usdL2fSysStatusActiveTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fSysStatusActiveTunnels.setStatus("current")
_UsdL2fSysStatusTotalSessions_Type = Counter32
_UsdL2fSysStatusTotalSessions_Object = MibScalar
usdL2fSysStatusTotalSessions = _UsdL2fSysStatusTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 1, 2, 11),
    _UsdL2fSysStatusTotalSessions_Type()
)
usdL2fSysStatusTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fSysStatusTotalSessions.setStatus("current")
_UsdL2fSysStatusFailedSessions_Type = Counter32
_UsdL2fSysStatusFailedSessions_Object = MibScalar
usdL2fSysStatusFailedSessions = _UsdL2fSysStatusFailedSessions_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 1, 2, 12),
    _UsdL2fSysStatusFailedSessions_Type()
)
usdL2fSysStatusFailedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fSysStatusFailedSessions.setStatus("current")
_UsdL2fSysStatusActiveSessions_Type = Gauge32
_UsdL2fSysStatusActiveSessions_Object = MibScalar
usdL2fSysStatusActiveSessions = _UsdL2fSysStatusActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 1, 2, 13),
    _UsdL2fSysStatusActiveSessions_Type()
)
usdL2fSysStatusActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fSysStatusActiveSessions.setStatus("current")
_UsdL2fDestination_ObjectIdentity = ObjectIdentity
usdL2fDestination = _UsdL2fDestination_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 2)
)
_UsdL2fDestConfig_ObjectIdentity = ObjectIdentity
usdL2fDestConfig = _UsdL2fDestConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 2, 1)
)
_UsdL2fDestConfigTable_Object = MibTable
usdL2fDestConfigTable = _UsdL2fDestConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    usdL2fDestConfigTable.setStatus("current")
_UsdL2fDestConfigEntry_Object = MibTableRow
usdL2fDestConfigEntry = _UsdL2fDestConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 2, 1, 2, 1)
)
usdL2fDestConfigEntry.setIndexNames(
    (0, "Unisphere-Data-L2F-MIB", "usdL2fDestConfigIfIndex"),
)
if mibBuilder.loadTexts:
    usdL2fDestConfigEntry.setStatus("current")
_UsdL2fDestConfigIfIndex_Type = InterfaceIndex
_UsdL2fDestConfigIfIndex_Object = MibTableColumn
usdL2fDestConfigIfIndex = _UsdL2fDestConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 2, 1, 2, 1, 1),
    _UsdL2fDestConfigIfIndex_Type()
)
usdL2fDestConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdL2fDestConfigIfIndex.setStatus("current")
_UsdL2fDestConfigRowStatus_Type = RowStatus
_UsdL2fDestConfigRowStatus_Object = MibTableColumn
usdL2fDestConfigRowStatus = _UsdL2fDestConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 2, 1, 2, 1, 2),
    _UsdL2fDestConfigRowStatus_Type()
)
usdL2fDestConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdL2fDestConfigRowStatus.setStatus("current")


class _UsdL2fDestConfigAdminState_Type(UsdL2fAdminState):
    """Custom type usdL2fDestConfigAdminState based on UsdL2fAdminState"""


_UsdL2fDestConfigAdminState_Object = MibTableColumn
usdL2fDestConfigAdminState = _UsdL2fDestConfigAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 2, 1, 2, 1, 3),
    _UsdL2fDestConfigAdminState_Type()
)
usdL2fDestConfigAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdL2fDestConfigAdminState.setStatus("current")
_UsdL2fDestStatus_ObjectIdentity = ObjectIdentity
usdL2fDestStatus = _UsdL2fDestStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 2, 2)
)
_UsdL2fDestStatusTable_Object = MibTable
usdL2fDestStatusTable = _UsdL2fDestStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    usdL2fDestStatusTable.setStatus("current")
_UsdL2fDestStatusEntry_Object = MibTableRow
usdL2fDestStatusEntry = _UsdL2fDestStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 2, 2, 1, 1)
)
usdL2fDestStatusEntry.setIndexNames(
    (0, "Unisphere-Data-L2F-MIB", "usdL2fDestStatusIfIndex"),
)
if mibBuilder.loadTexts:
    usdL2fDestStatusEntry.setStatus("current")
_UsdL2fDestStatusIfIndex_Type = InterfaceIndex
_UsdL2fDestStatusIfIndex_Object = MibTableColumn
usdL2fDestStatusIfIndex = _UsdL2fDestStatusIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 2, 2, 1, 1, 1),
    _UsdL2fDestStatusIfIndex_Type()
)
usdL2fDestStatusIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdL2fDestStatusIfIndex.setStatus("current")
_UsdL2fDestStatusTransport_Type = UsdL2fTransport
_UsdL2fDestStatusTransport_Object = MibTableColumn
usdL2fDestStatusTransport = _UsdL2fDestStatusTransport_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 2, 2, 1, 1, 2),
    _UsdL2fDestStatusTransport_Type()
)
usdL2fDestStatusTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fDestStatusTransport.setStatus("current")
_UsdL2fDestStatusEffectiveAdminState_Type = UsdL2fAdminState
_UsdL2fDestStatusEffectiveAdminState_Object = MibTableColumn
usdL2fDestStatusEffectiveAdminState = _UsdL2fDestStatusEffectiveAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 2, 2, 1, 1, 3),
    _UsdL2fDestStatusEffectiveAdminState_Type()
)
usdL2fDestStatusEffectiveAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fDestStatusEffectiveAdminState.setStatus("current")
_UsdL2fDestStatusTotalTunnels_Type = Counter32
_UsdL2fDestStatusTotalTunnels_Object = MibTableColumn
usdL2fDestStatusTotalTunnels = _UsdL2fDestStatusTotalTunnels_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 2, 2, 1, 1, 4),
    _UsdL2fDestStatusTotalTunnels_Type()
)
usdL2fDestStatusTotalTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fDestStatusTotalTunnels.setStatus("current")
_UsdL2fDestStatusFailedTunnels_Type = Counter32
_UsdL2fDestStatusFailedTunnels_Object = MibTableColumn
usdL2fDestStatusFailedTunnels = _UsdL2fDestStatusFailedTunnels_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 2, 2, 1, 1, 5),
    _UsdL2fDestStatusFailedTunnels_Type()
)
usdL2fDestStatusFailedTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fDestStatusFailedTunnels.setStatus("current")
_UsdL2fDestStatusFailedTunnelAuthens_Type = Counter32
_UsdL2fDestStatusFailedTunnelAuthens_Object = MibTableColumn
usdL2fDestStatusFailedTunnelAuthens = _UsdL2fDestStatusFailedTunnelAuthens_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 2, 2, 1, 1, 6),
    _UsdL2fDestStatusFailedTunnelAuthens_Type()
)
usdL2fDestStatusFailedTunnelAuthens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fDestStatusFailedTunnelAuthens.setStatus("current")
_UsdL2fDestStatusActiveTunnels_Type = Gauge32
_UsdL2fDestStatusActiveTunnels_Object = MibTableColumn
usdL2fDestStatusActiveTunnels = _UsdL2fDestStatusActiveTunnels_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 2, 2, 1, 1, 7),
    _UsdL2fDestStatusActiveTunnels_Type()
)
usdL2fDestStatusActiveTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fDestStatusActiveTunnels.setStatus("current")
_UsdL2fDestStatusTotalSessions_Type = Counter32
_UsdL2fDestStatusTotalSessions_Object = MibTableColumn
usdL2fDestStatusTotalSessions = _UsdL2fDestStatusTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 2, 2, 1, 1, 8),
    _UsdL2fDestStatusTotalSessions_Type()
)
usdL2fDestStatusTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fDestStatusTotalSessions.setStatus("current")
_UsdL2fDestStatusFailedSessions_Type = Counter32
_UsdL2fDestStatusFailedSessions_Object = MibTableColumn
usdL2fDestStatusFailedSessions = _UsdL2fDestStatusFailedSessions_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 2, 2, 1, 1, 9),
    _UsdL2fDestStatusFailedSessions_Type()
)
usdL2fDestStatusFailedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fDestStatusFailedSessions.setStatus("current")
_UsdL2fDestStatusActiveSessions_Type = Gauge32
_UsdL2fDestStatusActiveSessions_Object = MibTableColumn
usdL2fDestStatusActiveSessions = _UsdL2fDestStatusActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 2, 2, 1, 1, 10),
    _UsdL2fDestStatusActiveSessions_Type()
)
usdL2fDestStatusActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fDestStatusActiveSessions.setStatus("current")
_UsdL2fDestStatistics_ObjectIdentity = ObjectIdentity
usdL2fDestStatistics = _UsdL2fDestStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 2, 3)
)
_UsdL2fDestStatTable_Object = MibTable
usdL2fDestStatTable = _UsdL2fDestStatTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    usdL2fDestStatTable.setStatus("current")
_UsdL2fDestStatEntry_Object = MibTableRow
usdL2fDestStatEntry = _UsdL2fDestStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 2, 3, 1, 1)
)
usdL2fDestStatEntry.setIndexNames(
    (0, "Unisphere-Data-L2F-MIB", "usdL2fDestStatIfIndex"),
)
if mibBuilder.loadTexts:
    usdL2fDestStatEntry.setStatus("current")
_UsdL2fDestStatIfIndex_Type = InterfaceIndex
_UsdL2fDestStatIfIndex_Object = MibTableColumn
usdL2fDestStatIfIndex = _UsdL2fDestStatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 2, 3, 1, 1, 1),
    _UsdL2fDestStatIfIndex_Type()
)
usdL2fDestStatIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdL2fDestStatIfIndex.setStatus("current")
_UsdL2fDestStatCtlRecvOctets_Type = Counter32
_UsdL2fDestStatCtlRecvOctets_Object = MibTableColumn
usdL2fDestStatCtlRecvOctets = _UsdL2fDestStatCtlRecvOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 2, 3, 1, 1, 2),
    _UsdL2fDestStatCtlRecvOctets_Type()
)
usdL2fDestStatCtlRecvOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fDestStatCtlRecvOctets.setStatus("current")
_UsdL2fDestStatCtlRecvPackets_Type = Counter32
_UsdL2fDestStatCtlRecvPackets_Object = MibTableColumn
usdL2fDestStatCtlRecvPackets = _UsdL2fDestStatCtlRecvPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 2, 3, 1, 1, 3),
    _UsdL2fDestStatCtlRecvPackets_Type()
)
usdL2fDestStatCtlRecvPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fDestStatCtlRecvPackets.setStatus("current")
_UsdL2fDestStatCtlRecvErrors_Type = Counter32
_UsdL2fDestStatCtlRecvErrors_Object = MibTableColumn
usdL2fDestStatCtlRecvErrors = _UsdL2fDestStatCtlRecvErrors_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 2, 3, 1, 1, 4),
    _UsdL2fDestStatCtlRecvErrors_Type()
)
usdL2fDestStatCtlRecvErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fDestStatCtlRecvErrors.setStatus("current")
_UsdL2fDestStatCtlRecvDiscards_Type = Counter32
_UsdL2fDestStatCtlRecvDiscards_Object = MibTableColumn
usdL2fDestStatCtlRecvDiscards = _UsdL2fDestStatCtlRecvDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 2, 3, 1, 1, 5),
    _UsdL2fDestStatCtlRecvDiscards_Type()
)
usdL2fDestStatCtlRecvDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fDestStatCtlRecvDiscards.setStatus("current")
_UsdL2fDestStatCtlSendOctets_Type = Counter32
_UsdL2fDestStatCtlSendOctets_Object = MibTableColumn
usdL2fDestStatCtlSendOctets = _UsdL2fDestStatCtlSendOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 2, 3, 1, 1, 6),
    _UsdL2fDestStatCtlSendOctets_Type()
)
usdL2fDestStatCtlSendOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fDestStatCtlSendOctets.setStatus("current")
_UsdL2fDestStatCtlSendPackets_Type = Counter32
_UsdL2fDestStatCtlSendPackets_Object = MibTableColumn
usdL2fDestStatCtlSendPackets = _UsdL2fDestStatCtlSendPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 2, 3, 1, 1, 7),
    _UsdL2fDestStatCtlSendPackets_Type()
)
usdL2fDestStatCtlSendPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fDestStatCtlSendPackets.setStatus("current")
_UsdL2fDestStatCtlSendErrors_Type = Counter32
_UsdL2fDestStatCtlSendErrors_Object = MibTableColumn
usdL2fDestStatCtlSendErrors = _UsdL2fDestStatCtlSendErrors_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 2, 3, 1, 1, 8),
    _UsdL2fDestStatCtlSendErrors_Type()
)
usdL2fDestStatCtlSendErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fDestStatCtlSendErrors.setStatus("current")
_UsdL2fDestStatCtlSendDiscards_Type = Counter32
_UsdL2fDestStatCtlSendDiscards_Object = MibTableColumn
usdL2fDestStatCtlSendDiscards = _UsdL2fDestStatCtlSendDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 2, 3, 1, 1, 9),
    _UsdL2fDestStatCtlSendDiscards_Type()
)
usdL2fDestStatCtlSendDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fDestStatCtlSendDiscards.setStatus("current")
_UsdL2fDestStatPayRecvOctets_Type = Counter32
_UsdL2fDestStatPayRecvOctets_Object = MibTableColumn
usdL2fDestStatPayRecvOctets = _UsdL2fDestStatPayRecvOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 2, 3, 1, 1, 10),
    _UsdL2fDestStatPayRecvOctets_Type()
)
usdL2fDestStatPayRecvOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fDestStatPayRecvOctets.setStatus("current")
_UsdL2fDestStatPayRecvPackets_Type = Counter32
_UsdL2fDestStatPayRecvPackets_Object = MibTableColumn
usdL2fDestStatPayRecvPackets = _UsdL2fDestStatPayRecvPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 2, 3, 1, 1, 11),
    _UsdL2fDestStatPayRecvPackets_Type()
)
usdL2fDestStatPayRecvPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fDestStatPayRecvPackets.setStatus("current")
_UsdL2fDestStatPayRecvErrors_Type = Counter32
_UsdL2fDestStatPayRecvErrors_Object = MibTableColumn
usdL2fDestStatPayRecvErrors = _UsdL2fDestStatPayRecvErrors_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 2, 3, 1, 1, 12),
    _UsdL2fDestStatPayRecvErrors_Type()
)
usdL2fDestStatPayRecvErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fDestStatPayRecvErrors.setStatus("current")
_UsdL2fDestStatPayRecvDiscards_Type = Counter32
_UsdL2fDestStatPayRecvDiscards_Object = MibTableColumn
usdL2fDestStatPayRecvDiscards = _UsdL2fDestStatPayRecvDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 2, 3, 1, 1, 13),
    _UsdL2fDestStatPayRecvDiscards_Type()
)
usdL2fDestStatPayRecvDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fDestStatPayRecvDiscards.setStatus("current")
_UsdL2fDestStatPaySendOctets_Type = Counter32
_UsdL2fDestStatPaySendOctets_Object = MibTableColumn
usdL2fDestStatPaySendOctets = _UsdL2fDestStatPaySendOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 2, 3, 1, 1, 14),
    _UsdL2fDestStatPaySendOctets_Type()
)
usdL2fDestStatPaySendOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fDestStatPaySendOctets.setStatus("current")
_UsdL2fDestStatPaySendPackets_Type = Counter32
_UsdL2fDestStatPaySendPackets_Object = MibTableColumn
usdL2fDestStatPaySendPackets = _UsdL2fDestStatPaySendPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 2, 3, 1, 1, 15),
    _UsdL2fDestStatPaySendPackets_Type()
)
usdL2fDestStatPaySendPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fDestStatPaySendPackets.setStatus("current")
_UsdL2fDestStatPaySendErrors_Type = Counter32
_UsdL2fDestStatPaySendErrors_Object = MibTableColumn
usdL2fDestStatPaySendErrors = _UsdL2fDestStatPaySendErrors_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 2, 3, 1, 1, 16),
    _UsdL2fDestStatPaySendErrors_Type()
)
usdL2fDestStatPaySendErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fDestStatPaySendErrors.setStatus("current")
_UsdL2fDestStatPaySendDiscards_Type = Counter32
_UsdL2fDestStatPaySendDiscards_Object = MibTableColumn
usdL2fDestStatPaySendDiscards = _UsdL2fDestStatPaySendDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 2, 3, 1, 1, 17),
    _UsdL2fDestStatPaySendDiscards_Type()
)
usdL2fDestStatPaySendDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fDestStatPaySendDiscards.setStatus("current")
_UsdL2fTunnel_ObjectIdentity = ObjectIdentity
usdL2fTunnel = _UsdL2fTunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 3)
)
_UsdL2fTunnelConfig_ObjectIdentity = ObjectIdentity
usdL2fTunnelConfig = _UsdL2fTunnelConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 3, 1)
)
_UsdL2fTunnelConfigTable_Object = MibTable
usdL2fTunnelConfigTable = _UsdL2fTunnelConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    usdL2fTunnelConfigTable.setStatus("current")
_UsdL2fTunnelConfigEntry_Object = MibTableRow
usdL2fTunnelConfigEntry = _UsdL2fTunnelConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 3, 1, 2, 1)
)
usdL2fTunnelConfigEntry.setIndexNames(
    (0, "Unisphere-Data-L2F-MIB", "usdL2fTunnelConfigIfIndex"),
)
if mibBuilder.loadTexts:
    usdL2fTunnelConfigEntry.setStatus("current")
_UsdL2fTunnelConfigIfIndex_Type = InterfaceIndex
_UsdL2fTunnelConfigIfIndex_Object = MibTableColumn
usdL2fTunnelConfigIfIndex = _UsdL2fTunnelConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 3, 1, 2, 1, 1),
    _UsdL2fTunnelConfigIfIndex_Type()
)
usdL2fTunnelConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdL2fTunnelConfigIfIndex.setStatus("current")
_UsdL2fTunnelConfigRowStatus_Type = RowStatus
_UsdL2fTunnelConfigRowStatus_Object = MibTableColumn
usdL2fTunnelConfigRowStatus = _UsdL2fTunnelConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 3, 1, 2, 1, 2),
    _UsdL2fTunnelConfigRowStatus_Type()
)
usdL2fTunnelConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdL2fTunnelConfigRowStatus.setStatus("current")


class _UsdL2fTunnelConfigAdminState_Type(UsdL2fAdminState):
    """Custom type usdL2fTunnelConfigAdminState based on UsdL2fAdminState"""


_UsdL2fTunnelConfigAdminState_Object = MibTableColumn
usdL2fTunnelConfigAdminState = _UsdL2fTunnelConfigAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 3, 1, 2, 1, 3),
    _UsdL2fTunnelConfigAdminState_Type()
)
usdL2fTunnelConfigAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdL2fTunnelConfigAdminState.setStatus("current")
_UsdL2fTunnelStatus_ObjectIdentity = ObjectIdentity
usdL2fTunnelStatus = _UsdL2fTunnelStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 3, 2)
)
_UsdL2fTunnelStatusTable_Object = MibTable
usdL2fTunnelStatusTable = _UsdL2fTunnelStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    usdL2fTunnelStatusTable.setStatus("current")
_UsdL2fTunnelStatusEntry_Object = MibTableRow
usdL2fTunnelStatusEntry = _UsdL2fTunnelStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 3, 2, 1, 1)
)
usdL2fTunnelStatusEntry.setIndexNames(
    (0, "Unisphere-Data-L2F-MIB", "usdL2fTunnelStatusIfIndex"),
)
if mibBuilder.loadTexts:
    usdL2fTunnelStatusEntry.setStatus("current")
_UsdL2fTunnelStatusIfIndex_Type = InterfaceIndex
_UsdL2fTunnelStatusIfIndex_Object = MibTableColumn
usdL2fTunnelStatusIfIndex = _UsdL2fTunnelStatusIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 3, 2, 1, 1, 1),
    _UsdL2fTunnelStatusIfIndex_Type()
)
usdL2fTunnelStatusIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdL2fTunnelStatusIfIndex.setStatus("current")
_UsdL2fTunnelStatusTransport_Type = UsdL2fTransport
_UsdL2fTunnelStatusTransport_Object = MibTableColumn
usdL2fTunnelStatusTransport = _UsdL2fTunnelStatusTransport_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 3, 2, 1, 1, 2),
    _UsdL2fTunnelStatusTransport_Type()
)
usdL2fTunnelStatusTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fTunnelStatusTransport.setStatus("current")
_UsdL2fTunnelStatusLocalTunnelId_Type = UsdL2fTunnelId
_UsdL2fTunnelStatusLocalTunnelId_Object = MibTableColumn
usdL2fTunnelStatusLocalTunnelId = _UsdL2fTunnelStatusLocalTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 3, 2, 1, 1, 3),
    _UsdL2fTunnelStatusLocalTunnelId_Type()
)
usdL2fTunnelStatusLocalTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fTunnelStatusLocalTunnelId.setStatus("current")
_UsdL2fTunnelStatusRemoteTunnelId_Type = UsdL2fTunnelId
_UsdL2fTunnelStatusRemoteTunnelId_Object = MibTableColumn
usdL2fTunnelStatusRemoteTunnelId = _UsdL2fTunnelStatusRemoteTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 3, 2, 1, 1, 4),
    _UsdL2fTunnelStatusRemoteTunnelId_Type()
)
usdL2fTunnelStatusRemoteTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fTunnelStatusRemoteTunnelId.setStatus("current")
_UsdL2fTunnelStatusEffectiveAdminState_Type = UsdL2fAdminState
_UsdL2fTunnelStatusEffectiveAdminState_Object = MibTableColumn
usdL2fTunnelStatusEffectiveAdminState = _UsdL2fTunnelStatusEffectiveAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 3, 2, 1, 1, 5),
    _UsdL2fTunnelStatusEffectiveAdminState_Type()
)
usdL2fTunnelStatusEffectiveAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fTunnelStatusEffectiveAdminState.setStatus("current")


class _UsdL2fTunnelStatusState_Type(Integer32):
    """Custom type usdL2fTunnelStatusState based on Integer32"""
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


_UsdL2fTunnelStatusState_Type.__name__ = "Integer32"
_UsdL2fTunnelStatusState_Object = MibTableColumn
usdL2fTunnelStatusState = _UsdL2fTunnelStatusState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 3, 2, 1, 1, 6),
    _UsdL2fTunnelStatusState_Type()
)
usdL2fTunnelStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fTunnelStatusState.setStatus("current")


class _UsdL2fTunnelStatusInitiated_Type(Integer32):
    """Custom type usdL2fTunnelStatusInitiated based on Integer32"""
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


_UsdL2fTunnelStatusInitiated_Type.__name__ = "Integer32"
_UsdL2fTunnelStatusInitiated_Object = MibTableColumn
usdL2fTunnelStatusInitiated = _UsdL2fTunnelStatusInitiated_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 3, 2, 1, 1, 7),
    _UsdL2fTunnelStatusInitiated_Type()
)
usdL2fTunnelStatusInitiated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fTunnelStatusInitiated.setStatus("current")
_UsdL2fTunnelStatusRemoteHostName_Type = DisplayString
_UsdL2fTunnelStatusRemoteHostName_Object = MibTableColumn
usdL2fTunnelStatusRemoteHostName = _UsdL2fTunnelStatusRemoteHostName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 3, 2, 1, 1, 8),
    _UsdL2fTunnelStatusRemoteHostName_Type()
)
usdL2fTunnelStatusRemoteHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fTunnelStatusRemoteHostName.setStatus("current")
_UsdL2fTunnelStatusTotalSessions_Type = Counter32
_UsdL2fTunnelStatusTotalSessions_Object = MibTableColumn
usdL2fTunnelStatusTotalSessions = _UsdL2fTunnelStatusTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 3, 2, 1, 1, 9),
    _UsdL2fTunnelStatusTotalSessions_Type()
)
usdL2fTunnelStatusTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fTunnelStatusTotalSessions.setStatus("current")
_UsdL2fTunnelStatusFailedSessions_Type = Counter32
_UsdL2fTunnelStatusFailedSessions_Object = MibTableColumn
usdL2fTunnelStatusFailedSessions = _UsdL2fTunnelStatusFailedSessions_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 3, 2, 1, 1, 10),
    _UsdL2fTunnelStatusFailedSessions_Type()
)
usdL2fTunnelStatusFailedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fTunnelStatusFailedSessions.setStatus("current")
_UsdL2fTunnelStatusActiveSessions_Type = Gauge32
_UsdL2fTunnelStatusActiveSessions_Object = MibTableColumn
usdL2fTunnelStatusActiveSessions = _UsdL2fTunnelStatusActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 3, 2, 1, 1, 11),
    _UsdL2fTunnelStatusActiveSessions_Type()
)
usdL2fTunnelStatusActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fTunnelStatusActiveSessions.setStatus("current")


class _UsdL2fTunnelStatusLastErrorCode_Type(Integer32):
    """Custom type usdL2fTunnelStatusLastErrorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UsdL2fTunnelStatusLastErrorCode_Type.__name__ = "Integer32"
_UsdL2fTunnelStatusLastErrorCode_Object = MibTableColumn
usdL2fTunnelStatusLastErrorCode = _UsdL2fTunnelStatusLastErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 3, 2, 1, 1, 12),
    _UsdL2fTunnelStatusLastErrorCode_Type()
)
usdL2fTunnelStatusLastErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fTunnelStatusLastErrorCode.setStatus("current")
_UsdL2fTunnelStatusLastErrorMessage_Type = DisplayString
_UsdL2fTunnelStatusLastErrorMessage_Object = MibTableColumn
usdL2fTunnelStatusLastErrorMessage = _UsdL2fTunnelStatusLastErrorMessage_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 3, 2, 1, 1, 13),
    _UsdL2fTunnelStatusLastErrorMessage_Type()
)
usdL2fTunnelStatusLastErrorMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fTunnelStatusLastErrorMessage.setStatus("current")
_UsdL2fTunnelStatusCumEstabTime_Type = Unsigned32
_UsdL2fTunnelStatusCumEstabTime_Object = MibTableColumn
usdL2fTunnelStatusCumEstabTime = _UsdL2fTunnelStatusCumEstabTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 3, 2, 1, 1, 14),
    _UsdL2fTunnelStatusCumEstabTime_Type()
)
usdL2fTunnelStatusCumEstabTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fTunnelStatusCumEstabTime.setStatus("current")
if mibBuilder.loadTexts:
    usdL2fTunnelStatusCumEstabTime.setUnits("seconds")
_UsdL2fTunnelStatistics_ObjectIdentity = ObjectIdentity
usdL2fTunnelStatistics = _UsdL2fTunnelStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 3, 3)
)
_UsdL2fTunnelStatTable_Object = MibTable
usdL2fTunnelStatTable = _UsdL2fTunnelStatTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    usdL2fTunnelStatTable.setStatus("current")
_UsdL2fTunnelStatEntry_Object = MibTableRow
usdL2fTunnelStatEntry = _UsdL2fTunnelStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 3, 3, 1, 1)
)
usdL2fTunnelStatEntry.setIndexNames(
    (0, "Unisphere-Data-L2F-MIB", "usdL2fTunnelStatIfIndex"),
)
if mibBuilder.loadTexts:
    usdL2fTunnelStatEntry.setStatus("current")
_UsdL2fTunnelStatIfIndex_Type = InterfaceIndex
_UsdL2fTunnelStatIfIndex_Object = MibTableColumn
usdL2fTunnelStatIfIndex = _UsdL2fTunnelStatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 3, 3, 1, 1, 1),
    _UsdL2fTunnelStatIfIndex_Type()
)
usdL2fTunnelStatIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdL2fTunnelStatIfIndex.setStatus("current")
_UsdL2fTunnelStatCtlRecvOctets_Type = Counter32
_UsdL2fTunnelStatCtlRecvOctets_Object = MibTableColumn
usdL2fTunnelStatCtlRecvOctets = _UsdL2fTunnelStatCtlRecvOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 3, 3, 1, 1, 2),
    _UsdL2fTunnelStatCtlRecvOctets_Type()
)
usdL2fTunnelStatCtlRecvOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fTunnelStatCtlRecvOctets.setStatus("current")
_UsdL2fTunnelStatCtlRecvPackets_Type = Counter32
_UsdL2fTunnelStatCtlRecvPackets_Object = MibTableColumn
usdL2fTunnelStatCtlRecvPackets = _UsdL2fTunnelStatCtlRecvPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 3, 3, 1, 1, 3),
    _UsdL2fTunnelStatCtlRecvPackets_Type()
)
usdL2fTunnelStatCtlRecvPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fTunnelStatCtlRecvPackets.setStatus("current")
_UsdL2fTunnelStatCtlRecvErrors_Type = Counter32
_UsdL2fTunnelStatCtlRecvErrors_Object = MibTableColumn
usdL2fTunnelStatCtlRecvErrors = _UsdL2fTunnelStatCtlRecvErrors_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 3, 3, 1, 1, 4),
    _UsdL2fTunnelStatCtlRecvErrors_Type()
)
usdL2fTunnelStatCtlRecvErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fTunnelStatCtlRecvErrors.setStatus("current")
_UsdL2fTunnelStatCtlRecvDiscards_Type = Counter32
_UsdL2fTunnelStatCtlRecvDiscards_Object = MibTableColumn
usdL2fTunnelStatCtlRecvDiscards = _UsdL2fTunnelStatCtlRecvDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 3, 3, 1, 1, 5),
    _UsdL2fTunnelStatCtlRecvDiscards_Type()
)
usdL2fTunnelStatCtlRecvDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fTunnelStatCtlRecvDiscards.setStatus("current")
_UsdL2fTunnelStatCtlSendOctets_Type = Counter32
_UsdL2fTunnelStatCtlSendOctets_Object = MibTableColumn
usdL2fTunnelStatCtlSendOctets = _UsdL2fTunnelStatCtlSendOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 3, 3, 1, 1, 6),
    _UsdL2fTunnelStatCtlSendOctets_Type()
)
usdL2fTunnelStatCtlSendOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fTunnelStatCtlSendOctets.setStatus("current")
_UsdL2fTunnelStatCtlSendPackets_Type = Counter32
_UsdL2fTunnelStatCtlSendPackets_Object = MibTableColumn
usdL2fTunnelStatCtlSendPackets = _UsdL2fTunnelStatCtlSendPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 3, 3, 1, 1, 7),
    _UsdL2fTunnelStatCtlSendPackets_Type()
)
usdL2fTunnelStatCtlSendPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fTunnelStatCtlSendPackets.setStatus("current")
_UsdL2fTunnelStatCtlSendErrors_Type = Counter32
_UsdL2fTunnelStatCtlSendErrors_Object = MibTableColumn
usdL2fTunnelStatCtlSendErrors = _UsdL2fTunnelStatCtlSendErrors_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 3, 3, 1, 1, 8),
    _UsdL2fTunnelStatCtlSendErrors_Type()
)
usdL2fTunnelStatCtlSendErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fTunnelStatCtlSendErrors.setStatus("current")
_UsdL2fTunnelStatCtlSendDiscards_Type = Counter32
_UsdL2fTunnelStatCtlSendDiscards_Object = MibTableColumn
usdL2fTunnelStatCtlSendDiscards = _UsdL2fTunnelStatCtlSendDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 3, 3, 1, 1, 9),
    _UsdL2fTunnelStatCtlSendDiscards_Type()
)
usdL2fTunnelStatCtlSendDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fTunnelStatCtlSendDiscards.setStatus("current")
_UsdL2fTunnelStatPayRecvOctets_Type = Counter32
_UsdL2fTunnelStatPayRecvOctets_Object = MibTableColumn
usdL2fTunnelStatPayRecvOctets = _UsdL2fTunnelStatPayRecvOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 3, 3, 1, 1, 10),
    _UsdL2fTunnelStatPayRecvOctets_Type()
)
usdL2fTunnelStatPayRecvOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fTunnelStatPayRecvOctets.setStatus("current")
_UsdL2fTunnelStatPayRecvPackets_Type = Counter32
_UsdL2fTunnelStatPayRecvPackets_Object = MibTableColumn
usdL2fTunnelStatPayRecvPackets = _UsdL2fTunnelStatPayRecvPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 3, 3, 1, 1, 11),
    _UsdL2fTunnelStatPayRecvPackets_Type()
)
usdL2fTunnelStatPayRecvPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fTunnelStatPayRecvPackets.setStatus("current")
_UsdL2fTunnelStatPayRecvErrors_Type = Counter32
_UsdL2fTunnelStatPayRecvErrors_Object = MibTableColumn
usdL2fTunnelStatPayRecvErrors = _UsdL2fTunnelStatPayRecvErrors_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 3, 3, 1, 1, 12),
    _UsdL2fTunnelStatPayRecvErrors_Type()
)
usdL2fTunnelStatPayRecvErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fTunnelStatPayRecvErrors.setStatus("current")
_UsdL2fTunnelStatPayRecvDiscards_Type = Counter32
_UsdL2fTunnelStatPayRecvDiscards_Object = MibTableColumn
usdL2fTunnelStatPayRecvDiscards = _UsdL2fTunnelStatPayRecvDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 3, 3, 1, 1, 13),
    _UsdL2fTunnelStatPayRecvDiscards_Type()
)
usdL2fTunnelStatPayRecvDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fTunnelStatPayRecvDiscards.setStatus("current")
_UsdL2fTunnelStatPaySendOctets_Type = Counter32
_UsdL2fTunnelStatPaySendOctets_Object = MibTableColumn
usdL2fTunnelStatPaySendOctets = _UsdL2fTunnelStatPaySendOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 3, 3, 1, 1, 14),
    _UsdL2fTunnelStatPaySendOctets_Type()
)
usdL2fTunnelStatPaySendOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fTunnelStatPaySendOctets.setStatus("current")
_UsdL2fTunnelStatPaySendPackets_Type = Counter32
_UsdL2fTunnelStatPaySendPackets_Object = MibTableColumn
usdL2fTunnelStatPaySendPackets = _UsdL2fTunnelStatPaySendPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 3, 3, 1, 1, 15),
    _UsdL2fTunnelStatPaySendPackets_Type()
)
usdL2fTunnelStatPaySendPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fTunnelStatPaySendPackets.setStatus("current")
_UsdL2fTunnelStatPaySendErrors_Type = Counter32
_UsdL2fTunnelStatPaySendErrors_Object = MibTableColumn
usdL2fTunnelStatPaySendErrors = _UsdL2fTunnelStatPaySendErrors_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 3, 3, 1, 1, 16),
    _UsdL2fTunnelStatPaySendErrors_Type()
)
usdL2fTunnelStatPaySendErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fTunnelStatPaySendErrors.setStatus("current")
_UsdL2fTunnelStatPaySendDiscards_Type = Counter32
_UsdL2fTunnelStatPaySendDiscards_Object = MibTableColumn
usdL2fTunnelStatPaySendDiscards = _UsdL2fTunnelStatPaySendDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 3, 3, 1, 1, 17),
    _UsdL2fTunnelStatPaySendDiscards_Type()
)
usdL2fTunnelStatPaySendDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fTunnelStatPaySendDiscards.setStatus("current")
_UsdL2fTunnelStatCtlRecvOutOfSequence_Type = Counter32
_UsdL2fTunnelStatCtlRecvOutOfSequence_Object = MibTableColumn
usdL2fTunnelStatCtlRecvOutOfSequence = _UsdL2fTunnelStatCtlRecvOutOfSequence_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 3, 3, 1, 1, 18),
    _UsdL2fTunnelStatCtlRecvOutOfSequence_Type()
)
usdL2fTunnelStatCtlRecvOutOfSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fTunnelStatCtlRecvOutOfSequence.setStatus("current")
_UsdL2fTunnelMap_ObjectIdentity = ObjectIdentity
usdL2fTunnelMap = _UsdL2fTunnelMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 3, 4)
)
_UsdL2fMapTifSidToSifTable_Object = MibTable
usdL2fMapTifSidToSifTable = _UsdL2fMapTifSidToSifTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 3, 4, 1)
)
if mibBuilder.loadTexts:
    usdL2fMapTifSidToSifTable.setStatus("current")
_UsdL2fMapTifSidToSifEntry_Object = MibTableRow
usdL2fMapTifSidToSifEntry = _UsdL2fMapTifSidToSifEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 3, 4, 1, 1)
)
usdL2fMapTifSidToSifEntry.setIndexNames(
    (0, "Unisphere-Data-L2F-MIB", "usdL2fMapTifSidToSifTunnelIfIndex"),
    (0, "Unisphere-Data-L2F-MIB", "usdL2fMapTifSidToSifLocalSessionId"),
)
if mibBuilder.loadTexts:
    usdL2fMapTifSidToSifEntry.setStatus("current")
_UsdL2fMapTifSidToSifTunnelIfIndex_Type = InterfaceIndex
_UsdL2fMapTifSidToSifTunnelIfIndex_Object = MibTableColumn
usdL2fMapTifSidToSifTunnelIfIndex = _UsdL2fMapTifSidToSifTunnelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 3, 4, 1, 1, 1),
    _UsdL2fMapTifSidToSifTunnelIfIndex_Type()
)
usdL2fMapTifSidToSifTunnelIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdL2fMapTifSidToSifTunnelIfIndex.setStatus("current")
_UsdL2fMapTifSidToSifLocalSessionId_Type = UsdL2fSessionId
_UsdL2fMapTifSidToSifLocalSessionId_Object = MibTableColumn
usdL2fMapTifSidToSifLocalSessionId = _UsdL2fMapTifSidToSifLocalSessionId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 3, 4, 1, 1, 2),
    _UsdL2fMapTifSidToSifLocalSessionId_Type()
)
usdL2fMapTifSidToSifLocalSessionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdL2fMapTifSidToSifLocalSessionId.setStatus("current")
_UsdL2fMapTifSidToSifSessionIfIndex_Type = InterfaceIndex
_UsdL2fMapTifSidToSifSessionIfIndex_Object = MibTableColumn
usdL2fMapTifSidToSifSessionIfIndex = _UsdL2fMapTifSidToSifSessionIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 3, 4, 1, 1, 3),
    _UsdL2fMapTifSidToSifSessionIfIndex_Type()
)
usdL2fMapTifSidToSifSessionIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fMapTifSidToSifSessionIfIndex.setStatus("current")
_UsdL2fMapTidToTifTable_Object = MibTable
usdL2fMapTidToTifTable = _UsdL2fMapTidToTifTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 3, 4, 2)
)
if mibBuilder.loadTexts:
    usdL2fMapTidToTifTable.setStatus("current")
_UsdL2fMapTidToTifEntry_Object = MibTableRow
usdL2fMapTidToTifEntry = _UsdL2fMapTidToTifEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 3, 4, 2, 1)
)
usdL2fMapTidToTifEntry.setIndexNames(
    (0, "Unisphere-Data-L2F-MIB", "usdL2fMapTidToTifLocalTunnelId"),
)
if mibBuilder.loadTexts:
    usdL2fMapTidToTifEntry.setStatus("current")
_UsdL2fMapTidToTifLocalTunnelId_Type = UsdL2fTunnelId
_UsdL2fMapTidToTifLocalTunnelId_Object = MibTableColumn
usdL2fMapTidToTifLocalTunnelId = _UsdL2fMapTidToTifLocalTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 3, 4, 2, 1, 1),
    _UsdL2fMapTidToTifLocalTunnelId_Type()
)
usdL2fMapTidToTifLocalTunnelId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdL2fMapTidToTifLocalTunnelId.setStatus("current")
_UsdL2fMapTidToTifIfIndex_Type = InterfaceIndex
_UsdL2fMapTidToTifIfIndex_Object = MibTableColumn
usdL2fMapTidToTifIfIndex = _UsdL2fMapTidToTifIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 3, 4, 2, 1, 2),
    _UsdL2fMapTidToTifIfIndex_Type()
)
usdL2fMapTidToTifIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fMapTidToTifIfIndex.setStatus("current")
_UsdL2fSession_ObjectIdentity = ObjectIdentity
usdL2fSession = _UsdL2fSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 4)
)
_UsdL2fSessionConfig_ObjectIdentity = ObjectIdentity
usdL2fSessionConfig = _UsdL2fSessionConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 4, 1)
)
_UsdL2fSessionConfigTable_Object = MibTable
usdL2fSessionConfigTable = _UsdL2fSessionConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 4, 1, 2)
)
if mibBuilder.loadTexts:
    usdL2fSessionConfigTable.setStatus("current")
_UsdL2fSessionConfigEntry_Object = MibTableRow
usdL2fSessionConfigEntry = _UsdL2fSessionConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 4, 1, 2, 1)
)
usdL2fSessionConfigEntry.setIndexNames(
    (0, "Unisphere-Data-L2F-MIB", "usdL2fSessionConfigIfIndex"),
)
if mibBuilder.loadTexts:
    usdL2fSessionConfigEntry.setStatus("current")
_UsdL2fSessionConfigIfIndex_Type = InterfaceIndex
_UsdL2fSessionConfigIfIndex_Object = MibTableColumn
usdL2fSessionConfigIfIndex = _UsdL2fSessionConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 4, 1, 2, 1, 1),
    _UsdL2fSessionConfigIfIndex_Type()
)
usdL2fSessionConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdL2fSessionConfigIfIndex.setStatus("current")
_UsdL2fSessionConfigRowStatus_Type = RowStatus
_UsdL2fSessionConfigRowStatus_Object = MibTableColumn
usdL2fSessionConfigRowStatus = _UsdL2fSessionConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 4, 1, 2, 1, 2),
    _UsdL2fSessionConfigRowStatus_Type()
)
usdL2fSessionConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdL2fSessionConfigRowStatus.setStatus("current")


class _UsdL2fSessionConfigAdminState_Type(UsdL2fAdminState):
    """Custom type usdL2fSessionConfigAdminState based on UsdL2fAdminState"""


_UsdL2fSessionConfigAdminState_Object = MibTableColumn
usdL2fSessionConfigAdminState = _UsdL2fSessionConfigAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 4, 1, 2, 1, 3),
    _UsdL2fSessionConfigAdminState_Type()
)
usdL2fSessionConfigAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdL2fSessionConfigAdminState.setStatus("current")
_UsdL2fSessionStatus_ObjectIdentity = ObjectIdentity
usdL2fSessionStatus = _UsdL2fSessionStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 4, 2)
)
_UsdL2fSessionStatusTable_Object = MibTable
usdL2fSessionStatusTable = _UsdL2fSessionStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    usdL2fSessionStatusTable.setStatus("current")
_UsdL2fSessionStatusEntry_Object = MibTableRow
usdL2fSessionStatusEntry = _UsdL2fSessionStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 4, 2, 1, 1)
)
usdL2fSessionStatusEntry.setIndexNames(
    (0, "Unisphere-Data-L2F-MIB", "usdL2fSessionStatusIfIndex"),
)
if mibBuilder.loadTexts:
    usdL2fSessionStatusEntry.setStatus("current")
_UsdL2fSessionStatusIfIndex_Type = InterfaceIndex
_UsdL2fSessionStatusIfIndex_Object = MibTableColumn
usdL2fSessionStatusIfIndex = _UsdL2fSessionStatusIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 4, 2, 1, 1, 1),
    _UsdL2fSessionStatusIfIndex_Type()
)
usdL2fSessionStatusIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdL2fSessionStatusIfIndex.setStatus("current")
_UsdL2fSessionStatusLocalSessionId_Type = UsdL2fSessionId
_UsdL2fSessionStatusLocalSessionId_Object = MibTableColumn
usdL2fSessionStatusLocalSessionId = _UsdL2fSessionStatusLocalSessionId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 4, 2, 1, 1, 2),
    _UsdL2fSessionStatusLocalSessionId_Type()
)
usdL2fSessionStatusLocalSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fSessionStatusLocalSessionId.setStatus("current")
_UsdL2fSessionStatusRemoteSessionId_Type = UsdL2fSessionId
_UsdL2fSessionStatusRemoteSessionId_Object = MibTableColumn
usdL2fSessionStatusRemoteSessionId = _UsdL2fSessionStatusRemoteSessionId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 4, 2, 1, 1, 3),
    _UsdL2fSessionStatusRemoteSessionId_Type()
)
usdL2fSessionStatusRemoteSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fSessionStatusRemoteSessionId.setStatus("current")
_UsdL2fSessionStatusUserName_Type = DisplayString
_UsdL2fSessionStatusUserName_Object = MibTableColumn
usdL2fSessionStatusUserName = _UsdL2fSessionStatusUserName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 4, 2, 1, 1, 4),
    _UsdL2fSessionStatusUserName_Type()
)
usdL2fSessionStatusUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fSessionStatusUserName.setStatus("current")
_UsdL2fSessionStatusEffectiveAdminState_Type = UsdL2fAdminState
_UsdL2fSessionStatusEffectiveAdminState_Object = MibTableColumn
usdL2fSessionStatusEffectiveAdminState = _UsdL2fSessionStatusEffectiveAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 4, 2, 1, 1, 5),
    _UsdL2fSessionStatusEffectiveAdminState_Type()
)
usdL2fSessionStatusEffectiveAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fSessionStatusEffectiveAdminState.setStatus("current")


class _UsdL2fSessionStatusState_Type(Integer32):
    """Custom type usdL2fSessionStatusState based on Integer32"""
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


_UsdL2fSessionStatusState_Type.__name__ = "Integer32"
_UsdL2fSessionStatusState_Object = MibTableColumn
usdL2fSessionStatusState = _UsdL2fSessionStatusState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 4, 2, 1, 1, 6),
    _UsdL2fSessionStatusState_Type()
)
usdL2fSessionStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fSessionStatusState.setStatus("current")


class _UsdL2fSessionStatusCallType_Type(Integer32):
    """Custom type usdL2fSessionStatusCallType based on Integer32"""
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


_UsdL2fSessionStatusCallType_Type.__name__ = "Integer32"
_UsdL2fSessionStatusCallType_Object = MibTableColumn
usdL2fSessionStatusCallType = _UsdL2fSessionStatusCallType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 4, 2, 1, 1, 7),
    _UsdL2fSessionStatusCallType_Type()
)
usdL2fSessionStatusCallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fSessionStatusCallType.setStatus("current")
_UsdL2fSessionStatusTxConnectSpeed_Type = Integer32
_UsdL2fSessionStatusTxConnectSpeed_Object = MibTableColumn
usdL2fSessionStatusTxConnectSpeed = _UsdL2fSessionStatusTxConnectSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 4, 2, 1, 1, 8),
    _UsdL2fSessionStatusTxConnectSpeed_Type()
)
usdL2fSessionStatusTxConnectSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fSessionStatusTxConnectSpeed.setStatus("current")
_UsdL2fSessionStatusRxConnectSpeed_Type = Integer32
_UsdL2fSessionStatusRxConnectSpeed_Object = MibTableColumn
usdL2fSessionStatusRxConnectSpeed = _UsdL2fSessionStatusRxConnectSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 4, 2, 1, 1, 9),
    _UsdL2fSessionStatusRxConnectSpeed_Type()
)
usdL2fSessionStatusRxConnectSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fSessionStatusRxConnectSpeed.setStatus("current")
_UsdL2fSessionStatusProxyLcp_Type = TruthValue
_UsdL2fSessionStatusProxyLcp_Object = MibTableColumn
usdL2fSessionStatusProxyLcp = _UsdL2fSessionStatusProxyLcp_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 4, 2, 1, 1, 10),
    _UsdL2fSessionStatusProxyLcp_Type()
)
usdL2fSessionStatusProxyLcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fSessionStatusProxyLcp.setStatus("current")


class _UsdL2fSessionStatusAuthMethod_Type(Integer32):
    """Custom type usdL2fSessionStatusAuthMethod based on Integer32"""
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


_UsdL2fSessionStatusAuthMethod_Type.__name__ = "Integer32"
_UsdL2fSessionStatusAuthMethod_Object = MibTableColumn
usdL2fSessionStatusAuthMethod = _UsdL2fSessionStatusAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 4, 2, 1, 1, 11),
    _UsdL2fSessionStatusAuthMethod_Type()
)
usdL2fSessionStatusAuthMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fSessionStatusAuthMethod.setStatus("current")


class _UsdL2fSessionStatusSequencingState_Type(Integer32):
    """Custom type usdL2fSessionStatusSequencingState based on Integer32"""
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


_UsdL2fSessionStatusSequencingState_Type.__name__ = "Integer32"
_UsdL2fSessionStatusSequencingState_Object = MibTableColumn
usdL2fSessionStatusSequencingState = _UsdL2fSessionStatusSequencingState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 4, 2, 1, 1, 12),
    _UsdL2fSessionStatusSequencingState_Type()
)
usdL2fSessionStatusSequencingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fSessionStatusSequencingState.setStatus("current")
_UsdL2fSessionStatusLacTunneledIfIndex_Type = InterfaceIndexOrZero
_UsdL2fSessionStatusLacTunneledIfIndex_Object = MibTableColumn
usdL2fSessionStatusLacTunneledIfIndex = _UsdL2fSessionStatusLacTunneledIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 4, 2, 1, 1, 13),
    _UsdL2fSessionStatusLacTunneledIfIndex_Type()
)
usdL2fSessionStatusLacTunneledIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fSessionStatusLacTunneledIfIndex.setStatus("current")
_UsdL2fSessionStatusCumEstabTime_Type = Unsigned32
_UsdL2fSessionStatusCumEstabTime_Object = MibTableColumn
usdL2fSessionStatusCumEstabTime = _UsdL2fSessionStatusCumEstabTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 4, 2, 1, 1, 14),
    _UsdL2fSessionStatusCumEstabTime_Type()
)
usdL2fSessionStatusCumEstabTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fSessionStatusCumEstabTime.setStatus("current")
if mibBuilder.loadTexts:
    usdL2fSessionStatusCumEstabTime.setUnits("seconds")
_UsdL2fSessionStatistics_ObjectIdentity = ObjectIdentity
usdL2fSessionStatistics = _UsdL2fSessionStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 4, 3)
)
_UsdL2fSessionStatTable_Object = MibTable
usdL2fSessionStatTable = _UsdL2fSessionStatTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 4, 3, 1)
)
if mibBuilder.loadTexts:
    usdL2fSessionStatTable.setStatus("current")
_UsdL2fSessionStatEntry_Object = MibTableRow
usdL2fSessionStatEntry = _UsdL2fSessionStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 4, 3, 1, 1)
)
usdL2fSessionStatEntry.setIndexNames(
    (0, "Unisphere-Data-L2F-MIB", "usdL2fSessionStatIfIndex"),
)
if mibBuilder.loadTexts:
    usdL2fSessionStatEntry.setStatus("current")
_UsdL2fSessionStatIfIndex_Type = InterfaceIndex
_UsdL2fSessionStatIfIndex_Object = MibTableColumn
usdL2fSessionStatIfIndex = _UsdL2fSessionStatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 4, 3, 1, 1, 1),
    _UsdL2fSessionStatIfIndex_Type()
)
usdL2fSessionStatIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdL2fSessionStatIfIndex.setStatus("current")
_UsdL2fSessionStatPayRecvOctets_Type = Counter32
_UsdL2fSessionStatPayRecvOctets_Object = MibTableColumn
usdL2fSessionStatPayRecvOctets = _UsdL2fSessionStatPayRecvOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 4, 3, 1, 1, 2),
    _UsdL2fSessionStatPayRecvOctets_Type()
)
usdL2fSessionStatPayRecvOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fSessionStatPayRecvOctets.setStatus("current")
_UsdL2fSessionStatPayRecvPackets_Type = Counter32
_UsdL2fSessionStatPayRecvPackets_Object = MibTableColumn
usdL2fSessionStatPayRecvPackets = _UsdL2fSessionStatPayRecvPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 4, 3, 1, 1, 3),
    _UsdL2fSessionStatPayRecvPackets_Type()
)
usdL2fSessionStatPayRecvPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fSessionStatPayRecvPackets.setStatus("current")
_UsdL2fSessionStatPayRecvErrors_Type = Counter32
_UsdL2fSessionStatPayRecvErrors_Object = MibTableColumn
usdL2fSessionStatPayRecvErrors = _UsdL2fSessionStatPayRecvErrors_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 4, 3, 1, 1, 4),
    _UsdL2fSessionStatPayRecvErrors_Type()
)
usdL2fSessionStatPayRecvErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fSessionStatPayRecvErrors.setStatus("current")
_UsdL2fSessionStatPayRecvDiscards_Type = Counter32
_UsdL2fSessionStatPayRecvDiscards_Object = MibTableColumn
usdL2fSessionStatPayRecvDiscards = _UsdL2fSessionStatPayRecvDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 4, 3, 1, 1, 5),
    _UsdL2fSessionStatPayRecvDiscards_Type()
)
usdL2fSessionStatPayRecvDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fSessionStatPayRecvDiscards.setStatus("current")
_UsdL2fSessionStatPaySendOctets_Type = Counter32
_UsdL2fSessionStatPaySendOctets_Object = MibTableColumn
usdL2fSessionStatPaySendOctets = _UsdL2fSessionStatPaySendOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 4, 3, 1, 1, 6),
    _UsdL2fSessionStatPaySendOctets_Type()
)
usdL2fSessionStatPaySendOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fSessionStatPaySendOctets.setStatus("current")
_UsdL2fSessionStatPaySendPackets_Type = Counter32
_UsdL2fSessionStatPaySendPackets_Object = MibTableColumn
usdL2fSessionStatPaySendPackets = _UsdL2fSessionStatPaySendPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 4, 3, 1, 1, 7),
    _UsdL2fSessionStatPaySendPackets_Type()
)
usdL2fSessionStatPaySendPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fSessionStatPaySendPackets.setStatus("current")
_UsdL2fSessionStatPaySendErrors_Type = Counter32
_UsdL2fSessionStatPaySendErrors_Object = MibTableColumn
usdL2fSessionStatPaySendErrors = _UsdL2fSessionStatPaySendErrors_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 4, 3, 1, 1, 8),
    _UsdL2fSessionStatPaySendErrors_Type()
)
usdL2fSessionStatPaySendErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fSessionStatPaySendErrors.setStatus("current")
_UsdL2fSessionStatPaySendDiscards_Type = Counter32
_UsdL2fSessionStatPaySendDiscards_Object = MibTableColumn
usdL2fSessionStatPaySendDiscards = _UsdL2fSessionStatPaySendDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 4, 3, 1, 1, 9),
    _UsdL2fSessionStatPaySendDiscards_Type()
)
usdL2fSessionStatPaySendDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fSessionStatPaySendDiscards.setStatus("current")
_UsdL2fSessionStatRecvOutOfSequence_Type = Counter32
_UsdL2fSessionStatRecvOutOfSequence_Object = MibTableColumn
usdL2fSessionStatRecvOutOfSequence = _UsdL2fSessionStatRecvOutOfSequence_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 4, 3, 1, 1, 10),
    _UsdL2fSessionStatRecvOutOfSequence_Type()
)
usdL2fSessionStatRecvOutOfSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fSessionStatRecvOutOfSequence.setStatus("current")
_UsdL2fSessionStatResequencingTimeouts_Type = Counter32
_UsdL2fSessionStatResequencingTimeouts_Object = MibTableColumn
usdL2fSessionStatResequencingTimeouts = _UsdL2fSessionStatResequencingTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 4, 3, 1, 1, 11),
    _UsdL2fSessionStatResequencingTimeouts_Type()
)
usdL2fSessionStatResequencingTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fSessionStatResequencingTimeouts.setStatus("current")
_UsdL2fSessionStatPayLostPackets_Type = Unsigned32
_UsdL2fSessionStatPayLostPackets_Object = MibTableColumn
usdL2fSessionStatPayLostPackets = _UsdL2fSessionStatPayLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 4, 3, 1, 1, 12),
    _UsdL2fSessionStatPayLostPackets_Type()
)
usdL2fSessionStatPayLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fSessionStatPayLostPackets.setStatus("current")
_UsdL2fTransport_ObjectIdentity = ObjectIdentity
usdL2fTransport = _UsdL2fTransport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 5)
)
_UsdL2fTransportUdpIp_ObjectIdentity = ObjectIdentity
usdL2fTransportUdpIp = _UsdL2fTransportUdpIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 5, 1)
)
_UsdL2fUdpIpDestination_ObjectIdentity = ObjectIdentity
usdL2fUdpIpDestination = _UsdL2fUdpIpDestination_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 5, 1, 1)
)
_UsdL2fUdpIpDestTable_Object = MibTable
usdL2fUdpIpDestTable = _UsdL2fUdpIpDestTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 5, 1, 1, 1)
)
if mibBuilder.loadTexts:
    usdL2fUdpIpDestTable.setStatus("current")
_UsdL2fUdpIpDestEntry_Object = MibTableRow
usdL2fUdpIpDestEntry = _UsdL2fUdpIpDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 5, 1, 1, 1, 1)
)
usdL2fUdpIpDestEntry.setIndexNames(
    (0, "Unisphere-Data-L2F-MIB", "usdL2fUdpIpDestIfIndex"),
)
if mibBuilder.loadTexts:
    usdL2fUdpIpDestEntry.setStatus("current")
_UsdL2fUdpIpDestIfIndex_Type = InterfaceIndex
_UsdL2fUdpIpDestIfIndex_Object = MibTableColumn
usdL2fUdpIpDestIfIndex = _UsdL2fUdpIpDestIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 5, 1, 1, 1, 1, 1),
    _UsdL2fUdpIpDestIfIndex_Type()
)
usdL2fUdpIpDestIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdL2fUdpIpDestIfIndex.setStatus("current")
_UsdL2fUdpIpDestRouterIndex_Type = Unsigned32
_UsdL2fUdpIpDestRouterIndex_Object = MibTableColumn
usdL2fUdpIpDestRouterIndex = _UsdL2fUdpIpDestRouterIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 5, 1, 1, 1, 1, 2),
    _UsdL2fUdpIpDestRouterIndex_Type()
)
usdL2fUdpIpDestRouterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fUdpIpDestRouterIndex.setStatus("current")
_UsdL2fUdpIpDestLocalAddress_Type = IpAddress
_UsdL2fUdpIpDestLocalAddress_Object = MibTableColumn
usdL2fUdpIpDestLocalAddress = _UsdL2fUdpIpDestLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 5, 1, 1, 1, 1, 3),
    _UsdL2fUdpIpDestLocalAddress_Type()
)
usdL2fUdpIpDestLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fUdpIpDestLocalAddress.setStatus("current")
_UsdL2fUdpIpDestRemoteAddress_Type = IpAddress
_UsdL2fUdpIpDestRemoteAddress_Object = MibTableColumn
usdL2fUdpIpDestRemoteAddress = _UsdL2fUdpIpDestRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 5, 1, 1, 1, 1, 4),
    _UsdL2fUdpIpDestRemoteAddress_Type()
)
usdL2fUdpIpDestRemoteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fUdpIpDestRemoteAddress.setStatus("current")
_UsdL2fUdpIpTunnel_ObjectIdentity = ObjectIdentity
usdL2fUdpIpTunnel = _UsdL2fUdpIpTunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 5, 1, 2)
)
_UsdL2fUdpIpTunnelTable_Object = MibTable
usdL2fUdpIpTunnelTable = _UsdL2fUdpIpTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 5, 1, 2, 1)
)
if mibBuilder.loadTexts:
    usdL2fUdpIpTunnelTable.setStatus("current")
_UsdL2fUdpIpTunnelEntry_Object = MibTableRow
usdL2fUdpIpTunnelEntry = _UsdL2fUdpIpTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 5, 1, 2, 1, 1)
)
usdL2fUdpIpTunnelEntry.setIndexNames(
    (0, "Unisphere-Data-L2F-MIB", "usdL2fUdpIpTunnelIfIndex"),
)
if mibBuilder.loadTexts:
    usdL2fUdpIpTunnelEntry.setStatus("current")
_UsdL2fUdpIpTunnelIfIndex_Type = InterfaceIndex
_UsdL2fUdpIpTunnelIfIndex_Object = MibTableColumn
usdL2fUdpIpTunnelIfIndex = _UsdL2fUdpIpTunnelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 5, 1, 2, 1, 1, 1),
    _UsdL2fUdpIpTunnelIfIndex_Type()
)
usdL2fUdpIpTunnelIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdL2fUdpIpTunnelIfIndex.setStatus("current")
_UsdL2fUdpIpTunnelRouterIndex_Type = Unsigned32
_UsdL2fUdpIpTunnelRouterIndex_Object = MibTableColumn
usdL2fUdpIpTunnelRouterIndex = _UsdL2fUdpIpTunnelRouterIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 5, 1, 2, 1, 1, 2),
    _UsdL2fUdpIpTunnelRouterIndex_Type()
)
usdL2fUdpIpTunnelRouterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fUdpIpTunnelRouterIndex.setStatus("current")
_UsdL2fUdpIpTunnelLocalAddress_Type = IpAddress
_UsdL2fUdpIpTunnelLocalAddress_Object = MibTableColumn
usdL2fUdpIpTunnelLocalAddress = _UsdL2fUdpIpTunnelLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 5, 1, 2, 1, 1, 3),
    _UsdL2fUdpIpTunnelLocalAddress_Type()
)
usdL2fUdpIpTunnelLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fUdpIpTunnelLocalAddress.setStatus("current")
_UsdL2fUdpIpTunnelLocalPort_Type = Integer32
_UsdL2fUdpIpTunnelLocalPort_Object = MibTableColumn
usdL2fUdpIpTunnelLocalPort = _UsdL2fUdpIpTunnelLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 5, 1, 2, 1, 1, 4),
    _UsdL2fUdpIpTunnelLocalPort_Type()
)
usdL2fUdpIpTunnelLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fUdpIpTunnelLocalPort.setStatus("current")
_UsdL2fUdpIpTunnelRemoteAddress_Type = IpAddress
_UsdL2fUdpIpTunnelRemoteAddress_Object = MibTableColumn
usdL2fUdpIpTunnelRemoteAddress = _UsdL2fUdpIpTunnelRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 5, 1, 2, 1, 1, 5),
    _UsdL2fUdpIpTunnelRemoteAddress_Type()
)
usdL2fUdpIpTunnelRemoteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fUdpIpTunnelRemoteAddress.setStatus("current")
_UsdL2fUdpIpTunnelRemotePort_Type = Integer32
_UsdL2fUdpIpTunnelRemotePort_Object = MibTableColumn
usdL2fUdpIpTunnelRemotePort = _UsdL2fUdpIpTunnelRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 1, 5, 1, 2, 1, 1, 6),
    _UsdL2fUdpIpTunnelRemotePort_Type()
)
usdL2fUdpIpTunnelRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdL2fUdpIpTunnelRemotePort.setStatus("current")
_UsdL2fTrapControl_ObjectIdentity = ObjectIdentity
usdL2fTrapControl = _UsdL2fTrapControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 2)
)
_UsdL2fConformance_ObjectIdentity = ObjectIdentity
usdL2fConformance = _UsdL2fConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 3)
)
_UsdL2fGroups_ObjectIdentity = ObjectIdentity
usdL2fGroups = _UsdL2fGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 3, 1)
)
_UsdL2fCompliances_ObjectIdentity = ObjectIdentity
usdL2fCompliances = _UsdL2fCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 3, 2)
)

# Managed Objects groups

usdL2fConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 3, 1, 1)
)
usdL2fConfigGroup.setObjects(
      *(("Unisphere-Data-L2F-MIB", "usdL2fSysConfigAdminState"),
        ("Unisphere-Data-L2F-MIB", "usdL2fSysConfigDestructTimeout"),
        ("Unisphere-Data-L2F-MIB", "usdL2fSysConfigIpChecksumEnable"),
        ("Unisphere-Data-L2F-MIB", "usdL2fSysConfigReceiveDataSequencingIgnore"),
        ("Unisphere-Data-L2F-MIB", "usdL2fDestConfigRowStatus"),
        ("Unisphere-Data-L2F-MIB", "usdL2fDestConfigAdminState"),
        ("Unisphere-Data-L2F-MIB", "usdL2fTunnelConfigRowStatus"),
        ("Unisphere-Data-L2F-MIB", "usdL2fTunnelConfigAdminState"),
        ("Unisphere-Data-L2F-MIB", "usdL2fSessionConfigRowStatus"),
        ("Unisphere-Data-L2F-MIB", "usdL2fSessionConfigAdminState"))
)
if mibBuilder.loadTexts:
    usdL2fConfigGroup.setStatus("current")

usdL2fStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 3, 1, 2)
)
usdL2fStatusGroup.setObjects(
      *(("Unisphere-Data-L2F-MIB", "usdL2fSysStatusProtocolVersion"),
        ("Unisphere-Data-L2F-MIB", "usdL2fSysStatusVendorName"),
        ("Unisphere-Data-L2F-MIB", "usdL2fSysStatusFirmwareRev"),
        ("Unisphere-Data-L2F-MIB", "usdL2fSysStatusTotalDestinations"),
        ("Unisphere-Data-L2F-MIB", "usdL2fSysStatusFailedDestinations"),
        ("Unisphere-Data-L2F-MIB", "usdL2fSysStatusActiveDestinations"),
        ("Unisphere-Data-L2F-MIB", "usdL2fSysStatusTotalTunnels"),
        ("Unisphere-Data-L2F-MIB", "usdL2fSysStatusFailedTunnels"),
        ("Unisphere-Data-L2F-MIB", "usdL2fSysStatusFailedTunnelAuthens"),
        ("Unisphere-Data-L2F-MIB", "usdL2fSysStatusActiveTunnels"),
        ("Unisphere-Data-L2F-MIB", "usdL2fSysStatusTotalSessions"),
        ("Unisphere-Data-L2F-MIB", "usdL2fSysStatusFailedSessions"),
        ("Unisphere-Data-L2F-MIB", "usdL2fSysStatusActiveSessions"),
        ("Unisphere-Data-L2F-MIB", "usdL2fDestStatusTransport"),
        ("Unisphere-Data-L2F-MIB", "usdL2fDestStatusEffectiveAdminState"),
        ("Unisphere-Data-L2F-MIB", "usdL2fDestStatusTotalTunnels"),
        ("Unisphere-Data-L2F-MIB", "usdL2fDestStatusFailedTunnels"),
        ("Unisphere-Data-L2F-MIB", "usdL2fDestStatusFailedTunnelAuthens"),
        ("Unisphere-Data-L2F-MIB", "usdL2fDestStatusActiveTunnels"),
        ("Unisphere-Data-L2F-MIB", "usdL2fDestStatusTotalSessions"),
        ("Unisphere-Data-L2F-MIB", "usdL2fDestStatusFailedSessions"),
        ("Unisphere-Data-L2F-MIB", "usdL2fDestStatusActiveSessions"),
        ("Unisphere-Data-L2F-MIB", "usdL2fTunnelStatusTransport"),
        ("Unisphere-Data-L2F-MIB", "usdL2fTunnelStatusLocalTunnelId"),
        ("Unisphere-Data-L2F-MIB", "usdL2fTunnelStatusRemoteTunnelId"),
        ("Unisphere-Data-L2F-MIB", "usdL2fTunnelStatusEffectiveAdminState"),
        ("Unisphere-Data-L2F-MIB", "usdL2fTunnelStatusState"),
        ("Unisphere-Data-L2F-MIB", "usdL2fTunnelStatusInitiated"),
        ("Unisphere-Data-L2F-MIB", "usdL2fTunnelStatusRemoteHostName"),
        ("Unisphere-Data-L2F-MIB", "usdL2fTunnelStatusTotalSessions"),
        ("Unisphere-Data-L2F-MIB", "usdL2fTunnelStatusFailedSessions"),
        ("Unisphere-Data-L2F-MIB", "usdL2fTunnelStatusActiveSessions"),
        ("Unisphere-Data-L2F-MIB", "usdL2fTunnelStatusLastErrorCode"),
        ("Unisphere-Data-L2F-MIB", "usdL2fTunnelStatusLastErrorMessage"),
        ("Unisphere-Data-L2F-MIB", "usdL2fTunnelStatusCumEstabTime"),
        ("Unisphere-Data-L2F-MIB", "usdL2fSessionStatusLocalSessionId"),
        ("Unisphere-Data-L2F-MIB", "usdL2fSessionStatusRemoteSessionId"),
        ("Unisphere-Data-L2F-MIB", "usdL2fSessionStatusUserName"),
        ("Unisphere-Data-L2F-MIB", "usdL2fSessionStatusEffectiveAdminState"),
        ("Unisphere-Data-L2F-MIB", "usdL2fSessionStatusState"),
        ("Unisphere-Data-L2F-MIB", "usdL2fSessionStatusCallType"),
        ("Unisphere-Data-L2F-MIB", "usdL2fSessionStatusTxConnectSpeed"),
        ("Unisphere-Data-L2F-MIB", "usdL2fSessionStatusRxConnectSpeed"),
        ("Unisphere-Data-L2F-MIB", "usdL2fSessionStatusProxyLcp"),
        ("Unisphere-Data-L2F-MIB", "usdL2fSessionStatusAuthMethod"),
        ("Unisphere-Data-L2F-MIB", "usdL2fSessionStatusSequencingState"),
        ("Unisphere-Data-L2F-MIB", "usdL2fSessionStatusLacTunneledIfIndex"),
        ("Unisphere-Data-L2F-MIB", "usdL2fSessionStatusCumEstabTime"))
)
if mibBuilder.loadTexts:
    usdL2fStatusGroup.setStatus("current")

usdL2fStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 3, 1, 3)
)
usdL2fStatGroup.setObjects(
      *(("Unisphere-Data-L2F-MIB", "usdL2fDestStatCtlRecvOctets"),
        ("Unisphere-Data-L2F-MIB", "usdL2fDestStatCtlRecvPackets"),
        ("Unisphere-Data-L2F-MIB", "usdL2fDestStatCtlRecvErrors"),
        ("Unisphere-Data-L2F-MIB", "usdL2fDestStatCtlRecvDiscards"),
        ("Unisphere-Data-L2F-MIB", "usdL2fDestStatCtlSendOctets"),
        ("Unisphere-Data-L2F-MIB", "usdL2fDestStatCtlSendPackets"),
        ("Unisphere-Data-L2F-MIB", "usdL2fDestStatCtlSendErrors"),
        ("Unisphere-Data-L2F-MIB", "usdL2fDestStatCtlSendDiscards"),
        ("Unisphere-Data-L2F-MIB", "usdL2fDestStatPayRecvOctets"),
        ("Unisphere-Data-L2F-MIB", "usdL2fDestStatPayRecvPackets"),
        ("Unisphere-Data-L2F-MIB", "usdL2fDestStatPayRecvErrors"),
        ("Unisphere-Data-L2F-MIB", "usdL2fDestStatPayRecvDiscards"),
        ("Unisphere-Data-L2F-MIB", "usdL2fDestStatPaySendOctets"),
        ("Unisphere-Data-L2F-MIB", "usdL2fDestStatPaySendPackets"),
        ("Unisphere-Data-L2F-MIB", "usdL2fDestStatPaySendErrors"),
        ("Unisphere-Data-L2F-MIB", "usdL2fDestStatPaySendDiscards"),
        ("Unisphere-Data-L2F-MIB", "usdL2fTunnelStatCtlRecvOctets"),
        ("Unisphere-Data-L2F-MIB", "usdL2fTunnelStatCtlRecvPackets"),
        ("Unisphere-Data-L2F-MIB", "usdL2fTunnelStatCtlRecvErrors"),
        ("Unisphere-Data-L2F-MIB", "usdL2fTunnelStatCtlRecvDiscards"),
        ("Unisphere-Data-L2F-MIB", "usdL2fTunnelStatCtlSendOctets"),
        ("Unisphere-Data-L2F-MIB", "usdL2fTunnelStatCtlSendPackets"),
        ("Unisphere-Data-L2F-MIB", "usdL2fTunnelStatCtlSendErrors"),
        ("Unisphere-Data-L2F-MIB", "usdL2fTunnelStatCtlSendDiscards"),
        ("Unisphere-Data-L2F-MIB", "usdL2fTunnelStatPayRecvOctets"),
        ("Unisphere-Data-L2F-MIB", "usdL2fTunnelStatPayRecvPackets"),
        ("Unisphere-Data-L2F-MIB", "usdL2fTunnelStatPayRecvErrors"),
        ("Unisphere-Data-L2F-MIB", "usdL2fTunnelStatPayRecvDiscards"),
        ("Unisphere-Data-L2F-MIB", "usdL2fTunnelStatPaySendOctets"),
        ("Unisphere-Data-L2F-MIB", "usdL2fTunnelStatPaySendPackets"),
        ("Unisphere-Data-L2F-MIB", "usdL2fTunnelStatPaySendErrors"),
        ("Unisphere-Data-L2F-MIB", "usdL2fTunnelStatPaySendDiscards"),
        ("Unisphere-Data-L2F-MIB", "usdL2fTunnelStatCtlRecvOutOfSequence"),
        ("Unisphere-Data-L2F-MIB", "usdL2fSessionStatPayRecvOctets"),
        ("Unisphere-Data-L2F-MIB", "usdL2fSessionStatPayRecvPackets"),
        ("Unisphere-Data-L2F-MIB", "usdL2fSessionStatPayRecvErrors"),
        ("Unisphere-Data-L2F-MIB", "usdL2fSessionStatPayRecvDiscards"),
        ("Unisphere-Data-L2F-MIB", "usdL2fSessionStatPaySendOctets"),
        ("Unisphere-Data-L2F-MIB", "usdL2fSessionStatPaySendPackets"),
        ("Unisphere-Data-L2F-MIB", "usdL2fSessionStatPaySendErrors"),
        ("Unisphere-Data-L2F-MIB", "usdL2fSessionStatPaySendDiscards"),
        ("Unisphere-Data-L2F-MIB", "usdL2fSessionStatRecvOutOfSequence"),
        ("Unisphere-Data-L2F-MIB", "usdL2fSessionStatResequencingTimeouts"),
        ("Unisphere-Data-L2F-MIB", "usdL2fSessionStatPayLostPackets"))
)
if mibBuilder.loadTexts:
    usdL2fStatGroup.setStatus("current")

usdL2fMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 3, 1, 4)
)
usdL2fMapGroup.setObjects(
      *(("Unisphere-Data-L2F-MIB", "usdL2fMapTifSidToSifSessionIfIndex"),
        ("Unisphere-Data-L2F-MIB", "usdL2fMapTidToTifIfIndex"))
)
if mibBuilder.loadTexts:
    usdL2fMapGroup.setStatus("current")

usdL2fUdpIpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 3, 1, 5)
)
usdL2fUdpIpGroup.setObjects(
      *(("Unisphere-Data-L2F-MIB", "usdL2fUdpIpDestRouterIndex"),
        ("Unisphere-Data-L2F-MIB", "usdL2fUdpIpDestLocalAddress"),
        ("Unisphere-Data-L2F-MIB", "usdL2fUdpIpDestRemoteAddress"),
        ("Unisphere-Data-L2F-MIB", "usdL2fUdpIpTunnelRouterIndex"),
        ("Unisphere-Data-L2F-MIB", "usdL2fUdpIpTunnelLocalAddress"),
        ("Unisphere-Data-L2F-MIB", "usdL2fUdpIpTunnelLocalPort"),
        ("Unisphere-Data-L2F-MIB", "usdL2fUdpIpTunnelRemoteAddress"),
        ("Unisphere-Data-L2F-MIB", "usdL2fUdpIpTunnelRemotePort"))
)
if mibBuilder.loadTexts:
    usdL2fUdpIpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

usdL2fCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 53, 3, 2, 1)
)
if mibBuilder.loadTexts:
    usdL2fCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-L2F-MIB",
    **{"UsdL2fTunnelId": UsdL2fTunnelId,
       "UsdL2fSessionId": UsdL2fSessionId,
       "UsdL2fAdminState": UsdL2fAdminState,
       "UsdL2fTransport": UsdL2fTransport,
       "usdL2fMIB": usdL2fMIB,
       "usdL2fTraps": usdL2fTraps,
       "usdL2fObjects": usdL2fObjects,
       "usdL2fSystem": usdL2fSystem,
       "usdL2fSystemConfig": usdL2fSystemConfig,
       "usdL2fSysConfigAdminState": usdL2fSysConfigAdminState,
       "usdL2fSysConfigDestructTimeout": usdL2fSysConfigDestructTimeout,
       "usdL2fSysConfigIpChecksumEnable": usdL2fSysConfigIpChecksumEnable,
       "usdL2fSysConfigReceiveDataSequencingIgnore": usdL2fSysConfigReceiveDataSequencingIgnore,
       "usdL2fSystemStatus": usdL2fSystemStatus,
       "usdL2fSysStatusProtocolVersion": usdL2fSysStatusProtocolVersion,
       "usdL2fSysStatusVendorName": usdL2fSysStatusVendorName,
       "usdL2fSysStatusFirmwareRev": usdL2fSysStatusFirmwareRev,
       "usdL2fSysStatusTotalDestinations": usdL2fSysStatusTotalDestinations,
       "usdL2fSysStatusFailedDestinations": usdL2fSysStatusFailedDestinations,
       "usdL2fSysStatusActiveDestinations": usdL2fSysStatusActiveDestinations,
       "usdL2fSysStatusTotalTunnels": usdL2fSysStatusTotalTunnels,
       "usdL2fSysStatusFailedTunnels": usdL2fSysStatusFailedTunnels,
       "usdL2fSysStatusFailedTunnelAuthens": usdL2fSysStatusFailedTunnelAuthens,
       "usdL2fSysStatusActiveTunnels": usdL2fSysStatusActiveTunnels,
       "usdL2fSysStatusTotalSessions": usdL2fSysStatusTotalSessions,
       "usdL2fSysStatusFailedSessions": usdL2fSysStatusFailedSessions,
       "usdL2fSysStatusActiveSessions": usdL2fSysStatusActiveSessions,
       "usdL2fDestination": usdL2fDestination,
       "usdL2fDestConfig": usdL2fDestConfig,
       "usdL2fDestConfigTable": usdL2fDestConfigTable,
       "usdL2fDestConfigEntry": usdL2fDestConfigEntry,
       "usdL2fDestConfigIfIndex": usdL2fDestConfigIfIndex,
       "usdL2fDestConfigRowStatus": usdL2fDestConfigRowStatus,
       "usdL2fDestConfigAdminState": usdL2fDestConfigAdminState,
       "usdL2fDestStatus": usdL2fDestStatus,
       "usdL2fDestStatusTable": usdL2fDestStatusTable,
       "usdL2fDestStatusEntry": usdL2fDestStatusEntry,
       "usdL2fDestStatusIfIndex": usdL2fDestStatusIfIndex,
       "usdL2fDestStatusTransport": usdL2fDestStatusTransport,
       "usdL2fDestStatusEffectiveAdminState": usdL2fDestStatusEffectiveAdminState,
       "usdL2fDestStatusTotalTunnels": usdL2fDestStatusTotalTunnels,
       "usdL2fDestStatusFailedTunnels": usdL2fDestStatusFailedTunnels,
       "usdL2fDestStatusFailedTunnelAuthens": usdL2fDestStatusFailedTunnelAuthens,
       "usdL2fDestStatusActiveTunnels": usdL2fDestStatusActiveTunnels,
       "usdL2fDestStatusTotalSessions": usdL2fDestStatusTotalSessions,
       "usdL2fDestStatusFailedSessions": usdL2fDestStatusFailedSessions,
       "usdL2fDestStatusActiveSessions": usdL2fDestStatusActiveSessions,
       "usdL2fDestStatistics": usdL2fDestStatistics,
       "usdL2fDestStatTable": usdL2fDestStatTable,
       "usdL2fDestStatEntry": usdL2fDestStatEntry,
       "usdL2fDestStatIfIndex": usdL2fDestStatIfIndex,
       "usdL2fDestStatCtlRecvOctets": usdL2fDestStatCtlRecvOctets,
       "usdL2fDestStatCtlRecvPackets": usdL2fDestStatCtlRecvPackets,
       "usdL2fDestStatCtlRecvErrors": usdL2fDestStatCtlRecvErrors,
       "usdL2fDestStatCtlRecvDiscards": usdL2fDestStatCtlRecvDiscards,
       "usdL2fDestStatCtlSendOctets": usdL2fDestStatCtlSendOctets,
       "usdL2fDestStatCtlSendPackets": usdL2fDestStatCtlSendPackets,
       "usdL2fDestStatCtlSendErrors": usdL2fDestStatCtlSendErrors,
       "usdL2fDestStatCtlSendDiscards": usdL2fDestStatCtlSendDiscards,
       "usdL2fDestStatPayRecvOctets": usdL2fDestStatPayRecvOctets,
       "usdL2fDestStatPayRecvPackets": usdL2fDestStatPayRecvPackets,
       "usdL2fDestStatPayRecvErrors": usdL2fDestStatPayRecvErrors,
       "usdL2fDestStatPayRecvDiscards": usdL2fDestStatPayRecvDiscards,
       "usdL2fDestStatPaySendOctets": usdL2fDestStatPaySendOctets,
       "usdL2fDestStatPaySendPackets": usdL2fDestStatPaySendPackets,
       "usdL2fDestStatPaySendErrors": usdL2fDestStatPaySendErrors,
       "usdL2fDestStatPaySendDiscards": usdL2fDestStatPaySendDiscards,
       "usdL2fTunnel": usdL2fTunnel,
       "usdL2fTunnelConfig": usdL2fTunnelConfig,
       "usdL2fTunnelConfigTable": usdL2fTunnelConfigTable,
       "usdL2fTunnelConfigEntry": usdL2fTunnelConfigEntry,
       "usdL2fTunnelConfigIfIndex": usdL2fTunnelConfigIfIndex,
       "usdL2fTunnelConfigRowStatus": usdL2fTunnelConfigRowStatus,
       "usdL2fTunnelConfigAdminState": usdL2fTunnelConfigAdminState,
       "usdL2fTunnelStatus": usdL2fTunnelStatus,
       "usdL2fTunnelStatusTable": usdL2fTunnelStatusTable,
       "usdL2fTunnelStatusEntry": usdL2fTunnelStatusEntry,
       "usdL2fTunnelStatusIfIndex": usdL2fTunnelStatusIfIndex,
       "usdL2fTunnelStatusTransport": usdL2fTunnelStatusTransport,
       "usdL2fTunnelStatusLocalTunnelId": usdL2fTunnelStatusLocalTunnelId,
       "usdL2fTunnelStatusRemoteTunnelId": usdL2fTunnelStatusRemoteTunnelId,
       "usdL2fTunnelStatusEffectiveAdminState": usdL2fTunnelStatusEffectiveAdminState,
       "usdL2fTunnelStatusState": usdL2fTunnelStatusState,
       "usdL2fTunnelStatusInitiated": usdL2fTunnelStatusInitiated,
       "usdL2fTunnelStatusRemoteHostName": usdL2fTunnelStatusRemoteHostName,
       "usdL2fTunnelStatusTotalSessions": usdL2fTunnelStatusTotalSessions,
       "usdL2fTunnelStatusFailedSessions": usdL2fTunnelStatusFailedSessions,
       "usdL2fTunnelStatusActiveSessions": usdL2fTunnelStatusActiveSessions,
       "usdL2fTunnelStatusLastErrorCode": usdL2fTunnelStatusLastErrorCode,
       "usdL2fTunnelStatusLastErrorMessage": usdL2fTunnelStatusLastErrorMessage,
       "usdL2fTunnelStatusCumEstabTime": usdL2fTunnelStatusCumEstabTime,
       "usdL2fTunnelStatistics": usdL2fTunnelStatistics,
       "usdL2fTunnelStatTable": usdL2fTunnelStatTable,
       "usdL2fTunnelStatEntry": usdL2fTunnelStatEntry,
       "usdL2fTunnelStatIfIndex": usdL2fTunnelStatIfIndex,
       "usdL2fTunnelStatCtlRecvOctets": usdL2fTunnelStatCtlRecvOctets,
       "usdL2fTunnelStatCtlRecvPackets": usdL2fTunnelStatCtlRecvPackets,
       "usdL2fTunnelStatCtlRecvErrors": usdL2fTunnelStatCtlRecvErrors,
       "usdL2fTunnelStatCtlRecvDiscards": usdL2fTunnelStatCtlRecvDiscards,
       "usdL2fTunnelStatCtlSendOctets": usdL2fTunnelStatCtlSendOctets,
       "usdL2fTunnelStatCtlSendPackets": usdL2fTunnelStatCtlSendPackets,
       "usdL2fTunnelStatCtlSendErrors": usdL2fTunnelStatCtlSendErrors,
       "usdL2fTunnelStatCtlSendDiscards": usdL2fTunnelStatCtlSendDiscards,
       "usdL2fTunnelStatPayRecvOctets": usdL2fTunnelStatPayRecvOctets,
       "usdL2fTunnelStatPayRecvPackets": usdL2fTunnelStatPayRecvPackets,
       "usdL2fTunnelStatPayRecvErrors": usdL2fTunnelStatPayRecvErrors,
       "usdL2fTunnelStatPayRecvDiscards": usdL2fTunnelStatPayRecvDiscards,
       "usdL2fTunnelStatPaySendOctets": usdL2fTunnelStatPaySendOctets,
       "usdL2fTunnelStatPaySendPackets": usdL2fTunnelStatPaySendPackets,
       "usdL2fTunnelStatPaySendErrors": usdL2fTunnelStatPaySendErrors,
       "usdL2fTunnelStatPaySendDiscards": usdL2fTunnelStatPaySendDiscards,
       "usdL2fTunnelStatCtlRecvOutOfSequence": usdL2fTunnelStatCtlRecvOutOfSequence,
       "usdL2fTunnelMap": usdL2fTunnelMap,
       "usdL2fMapTifSidToSifTable": usdL2fMapTifSidToSifTable,
       "usdL2fMapTifSidToSifEntry": usdL2fMapTifSidToSifEntry,
       "usdL2fMapTifSidToSifTunnelIfIndex": usdL2fMapTifSidToSifTunnelIfIndex,
       "usdL2fMapTifSidToSifLocalSessionId": usdL2fMapTifSidToSifLocalSessionId,
       "usdL2fMapTifSidToSifSessionIfIndex": usdL2fMapTifSidToSifSessionIfIndex,
       "usdL2fMapTidToTifTable": usdL2fMapTidToTifTable,
       "usdL2fMapTidToTifEntry": usdL2fMapTidToTifEntry,
       "usdL2fMapTidToTifLocalTunnelId": usdL2fMapTidToTifLocalTunnelId,
       "usdL2fMapTidToTifIfIndex": usdL2fMapTidToTifIfIndex,
       "usdL2fSession": usdL2fSession,
       "usdL2fSessionConfig": usdL2fSessionConfig,
       "usdL2fSessionConfigTable": usdL2fSessionConfigTable,
       "usdL2fSessionConfigEntry": usdL2fSessionConfigEntry,
       "usdL2fSessionConfigIfIndex": usdL2fSessionConfigIfIndex,
       "usdL2fSessionConfigRowStatus": usdL2fSessionConfigRowStatus,
       "usdL2fSessionConfigAdminState": usdL2fSessionConfigAdminState,
       "usdL2fSessionStatus": usdL2fSessionStatus,
       "usdL2fSessionStatusTable": usdL2fSessionStatusTable,
       "usdL2fSessionStatusEntry": usdL2fSessionStatusEntry,
       "usdL2fSessionStatusIfIndex": usdL2fSessionStatusIfIndex,
       "usdL2fSessionStatusLocalSessionId": usdL2fSessionStatusLocalSessionId,
       "usdL2fSessionStatusRemoteSessionId": usdL2fSessionStatusRemoteSessionId,
       "usdL2fSessionStatusUserName": usdL2fSessionStatusUserName,
       "usdL2fSessionStatusEffectiveAdminState": usdL2fSessionStatusEffectiveAdminState,
       "usdL2fSessionStatusState": usdL2fSessionStatusState,
       "usdL2fSessionStatusCallType": usdL2fSessionStatusCallType,
       "usdL2fSessionStatusTxConnectSpeed": usdL2fSessionStatusTxConnectSpeed,
       "usdL2fSessionStatusRxConnectSpeed": usdL2fSessionStatusRxConnectSpeed,
       "usdL2fSessionStatusProxyLcp": usdL2fSessionStatusProxyLcp,
       "usdL2fSessionStatusAuthMethod": usdL2fSessionStatusAuthMethod,
       "usdL2fSessionStatusSequencingState": usdL2fSessionStatusSequencingState,
       "usdL2fSessionStatusLacTunneledIfIndex": usdL2fSessionStatusLacTunneledIfIndex,
       "usdL2fSessionStatusCumEstabTime": usdL2fSessionStatusCumEstabTime,
       "usdL2fSessionStatistics": usdL2fSessionStatistics,
       "usdL2fSessionStatTable": usdL2fSessionStatTable,
       "usdL2fSessionStatEntry": usdL2fSessionStatEntry,
       "usdL2fSessionStatIfIndex": usdL2fSessionStatIfIndex,
       "usdL2fSessionStatPayRecvOctets": usdL2fSessionStatPayRecvOctets,
       "usdL2fSessionStatPayRecvPackets": usdL2fSessionStatPayRecvPackets,
       "usdL2fSessionStatPayRecvErrors": usdL2fSessionStatPayRecvErrors,
       "usdL2fSessionStatPayRecvDiscards": usdL2fSessionStatPayRecvDiscards,
       "usdL2fSessionStatPaySendOctets": usdL2fSessionStatPaySendOctets,
       "usdL2fSessionStatPaySendPackets": usdL2fSessionStatPaySendPackets,
       "usdL2fSessionStatPaySendErrors": usdL2fSessionStatPaySendErrors,
       "usdL2fSessionStatPaySendDiscards": usdL2fSessionStatPaySendDiscards,
       "usdL2fSessionStatRecvOutOfSequence": usdL2fSessionStatRecvOutOfSequence,
       "usdL2fSessionStatResequencingTimeouts": usdL2fSessionStatResequencingTimeouts,
       "usdL2fSessionStatPayLostPackets": usdL2fSessionStatPayLostPackets,
       "usdL2fTransport": usdL2fTransport,
       "usdL2fTransportUdpIp": usdL2fTransportUdpIp,
       "usdL2fUdpIpDestination": usdL2fUdpIpDestination,
       "usdL2fUdpIpDestTable": usdL2fUdpIpDestTable,
       "usdL2fUdpIpDestEntry": usdL2fUdpIpDestEntry,
       "usdL2fUdpIpDestIfIndex": usdL2fUdpIpDestIfIndex,
       "usdL2fUdpIpDestRouterIndex": usdL2fUdpIpDestRouterIndex,
       "usdL2fUdpIpDestLocalAddress": usdL2fUdpIpDestLocalAddress,
       "usdL2fUdpIpDestRemoteAddress": usdL2fUdpIpDestRemoteAddress,
       "usdL2fUdpIpTunnel": usdL2fUdpIpTunnel,
       "usdL2fUdpIpTunnelTable": usdL2fUdpIpTunnelTable,
       "usdL2fUdpIpTunnelEntry": usdL2fUdpIpTunnelEntry,
       "usdL2fUdpIpTunnelIfIndex": usdL2fUdpIpTunnelIfIndex,
       "usdL2fUdpIpTunnelRouterIndex": usdL2fUdpIpTunnelRouterIndex,
       "usdL2fUdpIpTunnelLocalAddress": usdL2fUdpIpTunnelLocalAddress,
       "usdL2fUdpIpTunnelLocalPort": usdL2fUdpIpTunnelLocalPort,
       "usdL2fUdpIpTunnelRemoteAddress": usdL2fUdpIpTunnelRemoteAddress,
       "usdL2fUdpIpTunnelRemotePort": usdL2fUdpIpTunnelRemotePort,
       "usdL2fTrapControl": usdL2fTrapControl,
       "usdL2fConformance": usdL2fConformance,
       "usdL2fGroups": usdL2fGroups,
       "usdL2fConfigGroup": usdL2fConfigGroup,
       "usdL2fStatusGroup": usdL2fStatusGroup,
       "usdL2fStatGroup": usdL2fStatGroup,
       "usdL2fMapGroup": usdL2fMapGroup,
       "usdL2fUdpIpGroup": usdL2fUdpIpGroup,
       "usdL2fCompliances": usdL2fCompliances,
       "usdL2fCompliance": usdL2fCompliance}
)
