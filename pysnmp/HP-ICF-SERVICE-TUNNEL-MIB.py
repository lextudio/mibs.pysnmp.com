# SNMP MIB module (HP-ICF-SERVICE-TUNNEL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-SERVICE-TUNNEL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:58:08 2024
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

(ifAlias,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifAlias",
    "ifIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")

(tunnelIfEntry,
 tunnelInetConfigEntry) = mibBuilder.importSymbols(
    "TUNNEL-MIB",
    "tunnelIfEntry",
    "tunnelInetConfigEntry")


# MODULE-IDENTITY

hpicfServiceTunnel = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 100)
)
hpicfServiceTunnel.setRevisions(
        ("2014-06-17 00:00",
         "2013-06-13 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfServiceTunnelNotifications_ObjectIdentity = ObjectIdentity
hpicfServiceTunnelNotifications = _HpicfServiceTunnelNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 100, 0)
)
_HpicfServiceTunnelConfigurationObjects_ObjectIdentity = ObjectIdentity
hpicfServiceTunnelConfigurationObjects = _HpicfServiceTunnelConfigurationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 100, 1)
)
_HpicfServiceTunnelScalars_ObjectIdentity = ObjectIdentity
hpicfServiceTunnelScalars = _HpicfServiceTunnelScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 100, 1, 1)
)
_HpicfMaxIPv4ServiceTunnels_Type = Unsigned32
_HpicfMaxIPv4ServiceTunnels_Object = MibScalar
hpicfMaxIPv4ServiceTunnels = _HpicfMaxIPv4ServiceTunnels_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 100, 1, 1, 1),
    _HpicfMaxIPv4ServiceTunnels_Type()
)
hpicfMaxIPv4ServiceTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMaxIPv4ServiceTunnels.setStatus("current")
_HpicfTotalIPv4ServiceTunnels_Type = Unsigned32
_HpicfTotalIPv4ServiceTunnels_Object = MibScalar
hpicfTotalIPv4ServiceTunnels = _HpicfTotalIPv4ServiceTunnels_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 100, 1, 1, 2),
    _HpicfTotalIPv4ServiceTunnels_Type()
)
hpicfTotalIPv4ServiceTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfTotalIPv4ServiceTunnels.setStatus("current")
_HpicfMaxInterceptServiceTunnels_Type = Unsigned32
_HpicfMaxInterceptServiceTunnels_Object = MibScalar
hpicfMaxInterceptServiceTunnels = _HpicfMaxInterceptServiceTunnels_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 100, 1, 1, 3),
    _HpicfMaxInterceptServiceTunnels_Type()
)
hpicfMaxInterceptServiceTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMaxInterceptServiceTunnels.setStatus("current")
_HpicfTotalIPv4InterceptServiceTunnels_Type = Unsigned32
_HpicfTotalIPv4InterceptServiceTunnels_Object = MibScalar
hpicfTotalIPv4InterceptServiceTunnels = _HpicfTotalIPv4InterceptServiceTunnels_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 100, 1, 1, 4),
    _HpicfTotalIPv4InterceptServiceTunnels_Type()
)
hpicfTotalIPv4InterceptServiceTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfTotalIPv4InterceptServiceTunnels.setStatus("current")
_HpicfMaxIPv4TapServiceTunnels_Type = Unsigned32
_HpicfMaxIPv4TapServiceTunnels_Object = MibScalar
hpicfMaxIPv4TapServiceTunnels = _HpicfMaxIPv4TapServiceTunnels_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 100, 1, 1, 5),
    _HpicfMaxIPv4TapServiceTunnels_Type()
)
hpicfMaxIPv4TapServiceTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMaxIPv4TapServiceTunnels.setStatus("current")
_HpicfTotalIPv4TapServiceTunnels_Type = Unsigned32
_HpicfTotalIPv4TapServiceTunnels_Object = MibScalar
hpicfTotalIPv4TapServiceTunnels = _HpicfTotalIPv4TapServiceTunnels_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 100, 1, 1, 6),
    _HpicfTotalIPv4TapServiceTunnels_Type()
)
hpicfTotalIPv4TapServiceTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfTotalIPv4TapServiceTunnels.setStatus("current")
_HpicfServiceTunnelTable_Object = MibTable
hpicfServiceTunnelTable = _HpicfServiceTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 100, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfServiceTunnelTable.setStatus("current")
_HpicfServiceTunnelEntry_Object = MibTableRow
hpicfServiceTunnelEntry = _HpicfServiceTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 100, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hpicfServiceTunnelEntry.setStatus("current")


class _HpicfServiceTunnelType_Type(Integer32):
    """Custom type hpicfServiceTunnelType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("intercept", 1),
          ("none", 0),
          ("tap", 2))
    )


_HpicfServiceTunnelType_Type.__name__ = "Integer32"
_HpicfServiceTunnelType_Object = MibTableColumn
hpicfServiceTunnelType = _HpicfServiceTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 100, 1, 2, 1, 1),
    _HpicfServiceTunnelType_Type()
)
hpicfServiceTunnelType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfServiceTunnelType.setStatus("current")
_HpicfServiceTunnelName_Type = SnmpAdminString
_HpicfServiceTunnelName_Object = MibTableColumn
hpicfServiceTunnelName = _HpicfServiceTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 100, 1, 2, 1, 2),
    _HpicfServiceTunnelName_Type()
)
hpicfServiceTunnelName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfServiceTunnelName.setStatus("current")
_HpicfServiceTunnelIfTable_Object = MibTable
hpicfServiceTunnelIfTable = _HpicfServiceTunnelIfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 100, 1, 3)
)
if mibBuilder.loadTexts:
    hpicfServiceTunnelIfTable.setStatus("current")
_HpicfServiceTunnelIfEntry_Object = MibTableRow
hpicfServiceTunnelIfEntry = _HpicfServiceTunnelIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 100, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hpicfServiceTunnelIfEntry.setStatus("current")
_HpicfServiceTunnelIfMTU_Type = Unsigned32
_HpicfServiceTunnelIfMTU_Object = MibTableColumn
hpicfServiceTunnelIfMTU = _HpicfServiceTunnelIfMTU_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 100, 1, 3, 1, 1),
    _HpicfServiceTunnelIfMTU_Type()
)
hpicfServiceTunnelIfMTU.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfServiceTunnelIfMTU.setStatus("current")


class _HpicfServiceTunnelInterfaceStatus_Type(Integer32):
    """Custom type hpicfServiceTunnelInterfaceStatus based on Integer32"""
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


_HpicfServiceTunnelInterfaceStatus_Type.__name__ = "Integer32"
_HpicfServiceTunnelInterfaceStatus_Object = MibTableColumn
hpicfServiceTunnelInterfaceStatus = _HpicfServiceTunnelInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 100, 1, 3, 1, 2),
    _HpicfServiceTunnelInterfaceStatus_Type()
)
hpicfServiceTunnelInterfaceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfServiceTunnelInterfaceStatus.setStatus("current")


class _HpicfServiceTunnelInterfaceDownReason_Type(Integer32):
    """Custom type hpicfServiceTunnelInterfaceDownReason based on Integer32"""
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
        *(("ifAdminDown", 3),
          ("noRouteToDestination", 2),
          ("notApplicable", 0),
          ("resourceUnavailable", 1))
    )


_HpicfServiceTunnelInterfaceDownReason_Type.__name__ = "Integer32"
_HpicfServiceTunnelInterfaceDownReason_Object = MibTableColumn
hpicfServiceTunnelInterfaceDownReason = _HpicfServiceTunnelInterfaceDownReason_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 100, 1, 3, 1, 3),
    _HpicfServiceTunnelInterfaceDownReason_Type()
)
hpicfServiceTunnelInterfaceDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfServiceTunnelInterfaceDownReason.setStatus("current")


class _HpicfServiceTunnelInterfaceTruncate_Type(Integer32):
    """Custom type hpicfServiceTunnelInterfaceTruncate based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_HpicfServiceTunnelInterfaceTruncate_Type.__name__ = "Integer32"
_HpicfServiceTunnelInterfaceTruncate_Object = MibTableColumn
hpicfServiceTunnelInterfaceTruncate = _HpicfServiceTunnelInterfaceTruncate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 100, 1, 3, 1, 4),
    _HpicfServiceTunnelInterfaceTruncate_Type()
)
hpicfServiceTunnelInterfaceTruncate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfServiceTunnelInterfaceTruncate.setStatus("current")
_HpicfServiceTunnelStatisticsObjects_ObjectIdentity = ObjectIdentity
hpicfServiceTunnelStatisticsObjects = _HpicfServiceTunnelStatisticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 100, 2)
)
_HpicfServiceTunnelScalarStats_ObjectIdentity = ObjectIdentity
hpicfServiceTunnelScalarStats = _HpicfServiceTunnelScalarStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 100, 2, 1)
)
_HpicfServiceTunnelStatsRxInvalidKey_Type = Counter64
_HpicfServiceTunnelStatsRxInvalidKey_Object = MibScalar
hpicfServiceTunnelStatsRxInvalidKey = _HpicfServiceTunnelStatsRxInvalidKey_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 100, 2, 1, 1),
    _HpicfServiceTunnelStatsRxInvalidKey_Type()
)
hpicfServiceTunnelStatsRxInvalidKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfServiceTunnelStatsRxInvalidKey.setStatus("current")
_HpicfServiceTunnelStatsRxFragmentDrops_Type = Counter64
_HpicfServiceTunnelStatsRxFragmentDrops_Object = MibScalar
hpicfServiceTunnelStatsRxFragmentDrops = _HpicfServiceTunnelStatsRxFragmentDrops_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 100, 2, 1, 2),
    _HpicfServiceTunnelStatsRxFragmentDrops_Type()
)
hpicfServiceTunnelStatsRxFragmentDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfServiceTunnelStatsRxFragmentDrops.setStatus("current")
_HpicfServiceTunnelStatsTxMTUViolationDrop_Type = Counter64
_HpicfServiceTunnelStatsTxMTUViolationDrop_Object = MibScalar
hpicfServiceTunnelStatsTxMTUViolationDrop = _HpicfServiceTunnelStatsTxMTUViolationDrop_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 100, 2, 1, 3),
    _HpicfServiceTunnelStatsTxMTUViolationDrop_Type()
)
hpicfServiceTunnelStatsTxMTUViolationDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfServiceTunnelStatsTxMTUViolationDrop.setStatus("current")
_HpicfServiceTunnelStatsUnknownSrcMac_Type = Counter64
_HpicfServiceTunnelStatsUnknownSrcMac_Object = MibScalar
hpicfServiceTunnelStatsUnknownSrcMac = _HpicfServiceTunnelStatsUnknownSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 100, 2, 1, 4),
    _HpicfServiceTunnelStatsUnknownSrcMac_Type()
)
hpicfServiceTunnelStatsUnknownSrcMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfServiceTunnelStatsUnknownSrcMac.setStatus("current")
_HpicfServiceTunnelStatsScalarClear_Type = TruthValue
_HpicfServiceTunnelStatsScalarClear_Object = MibScalar
hpicfServiceTunnelStatsScalarClear = _HpicfServiceTunnelStatsScalarClear_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 100, 2, 1, 5),
    _HpicfServiceTunnelStatsScalarClear_Type()
)
hpicfServiceTunnelStatsScalarClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfServiceTunnelStatsScalarClear.setStatus("current")
_HpicfServiceTunnelStatsIfTable_Object = MibTable
hpicfServiceTunnelStatsIfTable = _HpicfServiceTunnelStatsIfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 100, 2, 2)
)
if mibBuilder.loadTexts:
    hpicfServiceTunnelStatsIfTable.setStatus("current")
_HpicfServiceTunnelStatsIfEntry_Object = MibTableRow
hpicfServiceTunnelStatsIfEntry = _HpicfServiceTunnelStatsIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 100, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hpicfServiceTunnelStatsIfEntry.setStatus("current")
_HpicfServiceTunnelStatsRxPackets_Type = Counter64
_HpicfServiceTunnelStatsRxPackets_Object = MibTableColumn
hpicfServiceTunnelStatsRxPackets = _HpicfServiceTunnelStatsRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 100, 2, 2, 1, 1),
    _HpicfServiceTunnelStatsRxPackets_Type()
)
hpicfServiceTunnelStatsRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfServiceTunnelStatsRxPackets.setStatus("current")
_HpicfServiceTunnelStatsTxPackets_Type = Counter64
_HpicfServiceTunnelStatsTxPackets_Object = MibTableColumn
hpicfServiceTunnelStatsTxPackets = _HpicfServiceTunnelStatsTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 100, 2, 2, 1, 2),
    _HpicfServiceTunnelStatsTxPackets_Type()
)
hpicfServiceTunnelStatsTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfServiceTunnelStatsTxPackets.setStatus("current")
_HpicfServiceTunnelStatsRxHeartbeat_Type = Counter64
_HpicfServiceTunnelStatsRxHeartbeat_Object = MibTableColumn
hpicfServiceTunnelStatsRxHeartbeat = _HpicfServiceTunnelStatsRxHeartbeat_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 100, 2, 2, 1, 3),
    _HpicfServiceTunnelStatsRxHeartbeat_Type()
)
hpicfServiceTunnelStatsRxHeartbeat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfServiceTunnelStatsRxHeartbeat.setStatus("current")
_HpicfServiceTunnelStatsTxHeartbeat_Type = Counter64
_HpicfServiceTunnelStatsTxHeartbeat_Object = MibTableColumn
hpicfServiceTunnelStatsTxHeartbeat = _HpicfServiceTunnelStatsTxHeartbeat_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 100, 2, 2, 1, 4),
    _HpicfServiceTunnelStatsTxHeartbeat_Type()
)
hpicfServiceTunnelStatsTxHeartbeat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfServiceTunnelStatsTxHeartbeat.setStatus("current")
_HpicfServiceTunnelLastHeartbeatPacketTimestamp_Type = TimeTicks
_HpicfServiceTunnelLastHeartbeatPacketTimestamp_Object = MibTableColumn
hpicfServiceTunnelLastHeartbeatPacketTimestamp = _HpicfServiceTunnelLastHeartbeatPacketTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 100, 2, 2, 1, 5),
    _HpicfServiceTunnelLastHeartbeatPacketTimestamp_Type()
)
hpicfServiceTunnelLastHeartbeatPacketTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfServiceTunnelLastHeartbeatPacketTimestamp.setStatus("current")
_HpicfServiceTunnelStatsClear_Type = TruthValue
_HpicfServiceTunnelStatsClear_Object = MibTableColumn
hpicfServiceTunnelStatsClear = _HpicfServiceTunnelStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 100, 2, 2, 1, 6),
    _HpicfServiceTunnelStatsClear_Type()
)
hpicfServiceTunnelStatsClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfServiceTunnelStatsClear.setStatus("current")
_HpicfServiceTunnelConformance_ObjectIdentity = ObjectIdentity
hpicfServiceTunnelConformance = _HpicfServiceTunnelConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 100, 3)
)
_HpicfServiceTunnelCompliances_ObjectIdentity = ObjectIdentity
hpicfServiceTunnelCompliances = _HpicfServiceTunnelCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 100, 3, 1)
)
_HpicfServiceTunnelGroups_ObjectIdentity = ObjectIdentity
hpicfServiceTunnelGroups = _HpicfServiceTunnelGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 100, 3, 2)
)
tunnelInetConfigEntry.registerAugmentions(
    ("HP-ICF-SERVICE-TUNNEL-MIB",
     "hpicfServiceTunnelEntry")
)
hpicfServiceTunnelEntry.setIndexNames(*tunnelInetConfigEntry.getIndexNames())
tunnelIfEntry.registerAugmentions(
    ("HP-ICF-SERVICE-TUNNEL-MIB",
     "hpicfServiceTunnelIfEntry")
)
hpicfServiceTunnelIfEntry.setIndexNames(*tunnelIfEntry.getIndexNames())
tunnelIfEntry.registerAugmentions(
    ("HP-ICF-SERVICE-TUNNEL-MIB",
     "hpicfServiceTunnelStatsIfEntry")
)
hpicfServiceTunnelStatsIfEntry.setIndexNames(*tunnelIfEntry.getIndexNames())

# Managed Objects groups

hpicfServiceScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 100, 3, 2, 1)
)
hpicfServiceScalarsGroup.setObjects(
      *(("HP-ICF-SERVICE-TUNNEL-MIB", "hpicfMaxIPv4ServiceTunnels"),
        ("HP-ICF-SERVICE-TUNNEL-MIB", "hpicfTotalIPv4ServiceTunnels"))
)
if mibBuilder.loadTexts:
    hpicfServiceScalarsGroup.setStatus("current")

hpicfServiceScalarsStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 100, 3, 2, 2)
)
hpicfServiceScalarsStatsGroup.setObjects(
      *(("HP-ICF-SERVICE-TUNNEL-MIB", "hpicfServiceTunnelStatsRxInvalidKey"),
        ("HP-ICF-SERVICE-TUNNEL-MIB", "hpicfServiceTunnelStatsRxFragmentDrops"),
        ("HP-ICF-SERVICE-TUNNEL-MIB", "hpicfServiceTunnelStatsTxMTUViolationDrop"),
        ("HP-ICF-SERVICE-TUNNEL-MIB", "hpicfServiceTunnelStatsUnknownSrcMac"),
        ("HP-ICF-SERVICE-TUNNEL-MIB", "hpicfServiceTunnelStatsScalarClear"))
)
if mibBuilder.loadTexts:
    hpicfServiceScalarsStatsGroup.setStatus("current")

hpicfServiceTunnelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 100, 3, 2, 3)
)
hpicfServiceTunnelGroup.setObjects(
      *(("HP-ICF-SERVICE-TUNNEL-MIB", "hpicfServiceTunnelType"),
        ("HP-ICF-SERVICE-TUNNEL-MIB", "hpicfServiceTunnelName"),
        ("HP-ICF-SERVICE-TUNNEL-MIB", "hpicfServiceTunnelIfMTU"),
        ("HP-ICF-SERVICE-TUNNEL-MIB", "hpicfServiceTunnelInterfaceStatus"),
        ("HP-ICF-SERVICE-TUNNEL-MIB", "hpicfServiceTunnelInterfaceDownReason"))
)
if mibBuilder.loadTexts:
    hpicfServiceTunnelGroup.setStatus("current")

hpicfServiceTunnelStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 100, 3, 2, 4)
)
hpicfServiceTunnelStatsGroup.setObjects(
      *(("HP-ICF-SERVICE-TUNNEL-MIB", "hpicfServiceTunnelStatsRxPackets"),
        ("HP-ICF-SERVICE-TUNNEL-MIB", "hpicfServiceTunnelStatsTxPackets"),
        ("HP-ICF-SERVICE-TUNNEL-MIB", "hpicfServiceTunnelStatsRxHeartbeat"),
        ("HP-ICF-SERVICE-TUNNEL-MIB", "hpicfServiceTunnelStatsTxHeartbeat"),
        ("HP-ICF-SERVICE-TUNNEL-MIB", "hpicfServiceTunnelLastHeartbeatPacketTimestamp"),
        ("HP-ICF-SERVICE-TUNNEL-MIB", "hpicfServiceTunnelStatsClear"))
)
if mibBuilder.loadTexts:
    hpicfServiceTunnelStatsGroup.setStatus("current")

hpicfServiceScalarsGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 100, 3, 2, 6)
)
hpicfServiceScalarsGroup1.setObjects(
      *(("HP-ICF-SERVICE-TUNNEL-MIB", "hpicfMaxIPv4ServiceTunnels"),
        ("HP-ICF-SERVICE-TUNNEL-MIB", "hpicfTotalIPv4ServiceTunnels"),
        ("HP-ICF-SERVICE-TUNNEL-MIB", "hpicfMaxInterceptServiceTunnels"),
        ("HP-ICF-SERVICE-TUNNEL-MIB", "hpicfTotalIPv4InterceptServiceTunnels"),
        ("HP-ICF-SERVICE-TUNNEL-MIB", "hpicfMaxIPv4TapServiceTunnels"),
        ("HP-ICF-SERVICE-TUNNEL-MIB", "hpicfTotalIPv4TapServiceTunnels"))
)
if mibBuilder.loadTexts:
    hpicfServiceScalarsGroup1.setStatus("current")

hpicfServiceTunnelGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 100, 3, 2, 7)
)
hpicfServiceTunnelGroup1.setObjects(
      *(("HP-ICF-SERVICE-TUNNEL-MIB", "hpicfServiceTunnelType"),
        ("HP-ICF-SERVICE-TUNNEL-MIB", "hpicfServiceTunnelName"),
        ("HP-ICF-SERVICE-TUNNEL-MIB", "hpicfServiceTunnelIfMTU"),
        ("HP-ICF-SERVICE-TUNNEL-MIB", "hpicfServiceTunnelInterfaceStatus"),
        ("HP-ICF-SERVICE-TUNNEL-MIB", "hpicfServiceTunnelInterfaceDownReason"),
        ("HP-ICF-SERVICE-TUNNEL-MIB", "hpicfServiceTunnelInterfaceTruncate"))
)
if mibBuilder.loadTexts:
    hpicfServiceTunnelGroup1.setStatus("current")


# Notification objects

hpicfServiceTunnelIfUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 100, 0, 1)
)
hpicfServiceTunnelIfUp.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    hpicfServiceTunnelIfUp.setStatus(
        "current"
    )

hpicfServiceTunnelIfDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 100, 0, 2)
)
hpicfServiceTunnelIfDown.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifAlias"),
        ("HP-ICF-SERVICE-TUNNEL-MIB", "hpicfServiceTunnelInterfaceDownReason"))
)
if mibBuilder.loadTexts:
    hpicfServiceTunnelIfDown.setStatus(
        "current"
    )


# Notifications groups

hpicfServiceTunnelNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 100, 3, 2, 5)
)
hpicfServiceTunnelNotificationGroup.setObjects(
      *(("HP-ICF-SERVICE-TUNNEL-MIB", "hpicfServiceTunnelIfUp"),
        ("HP-ICF-SERVICE-TUNNEL-MIB", "hpicfServiceTunnelIfDown"))
)
if mibBuilder.loadTexts:
    hpicfServiceTunnelNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hpicfServiceTunnelCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 100, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfServiceTunnelCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-SERVICE-TUNNEL-MIB",
    **{"hpicfServiceTunnel": hpicfServiceTunnel,
       "hpicfServiceTunnelNotifications": hpicfServiceTunnelNotifications,
       "hpicfServiceTunnelIfUp": hpicfServiceTunnelIfUp,
       "hpicfServiceTunnelIfDown": hpicfServiceTunnelIfDown,
       "hpicfServiceTunnelConfigurationObjects": hpicfServiceTunnelConfigurationObjects,
       "hpicfServiceTunnelScalars": hpicfServiceTunnelScalars,
       "hpicfMaxIPv4ServiceTunnels": hpicfMaxIPv4ServiceTunnels,
       "hpicfTotalIPv4ServiceTunnels": hpicfTotalIPv4ServiceTunnels,
       "hpicfMaxInterceptServiceTunnels": hpicfMaxInterceptServiceTunnels,
       "hpicfTotalIPv4InterceptServiceTunnels": hpicfTotalIPv4InterceptServiceTunnels,
       "hpicfMaxIPv4TapServiceTunnels": hpicfMaxIPv4TapServiceTunnels,
       "hpicfTotalIPv4TapServiceTunnels": hpicfTotalIPv4TapServiceTunnels,
       "hpicfServiceTunnelTable": hpicfServiceTunnelTable,
       "hpicfServiceTunnelEntry": hpicfServiceTunnelEntry,
       "hpicfServiceTunnelType": hpicfServiceTunnelType,
       "hpicfServiceTunnelName": hpicfServiceTunnelName,
       "hpicfServiceTunnelIfTable": hpicfServiceTunnelIfTable,
       "hpicfServiceTunnelIfEntry": hpicfServiceTunnelIfEntry,
       "hpicfServiceTunnelIfMTU": hpicfServiceTunnelIfMTU,
       "hpicfServiceTunnelInterfaceStatus": hpicfServiceTunnelInterfaceStatus,
       "hpicfServiceTunnelInterfaceDownReason": hpicfServiceTunnelInterfaceDownReason,
       "hpicfServiceTunnelInterfaceTruncate": hpicfServiceTunnelInterfaceTruncate,
       "hpicfServiceTunnelStatisticsObjects": hpicfServiceTunnelStatisticsObjects,
       "hpicfServiceTunnelScalarStats": hpicfServiceTunnelScalarStats,
       "hpicfServiceTunnelStatsRxInvalidKey": hpicfServiceTunnelStatsRxInvalidKey,
       "hpicfServiceTunnelStatsRxFragmentDrops": hpicfServiceTunnelStatsRxFragmentDrops,
       "hpicfServiceTunnelStatsTxMTUViolationDrop": hpicfServiceTunnelStatsTxMTUViolationDrop,
       "hpicfServiceTunnelStatsUnknownSrcMac": hpicfServiceTunnelStatsUnknownSrcMac,
       "hpicfServiceTunnelStatsScalarClear": hpicfServiceTunnelStatsScalarClear,
       "hpicfServiceTunnelStatsIfTable": hpicfServiceTunnelStatsIfTable,
       "hpicfServiceTunnelStatsIfEntry": hpicfServiceTunnelStatsIfEntry,
       "hpicfServiceTunnelStatsRxPackets": hpicfServiceTunnelStatsRxPackets,
       "hpicfServiceTunnelStatsTxPackets": hpicfServiceTunnelStatsTxPackets,
       "hpicfServiceTunnelStatsRxHeartbeat": hpicfServiceTunnelStatsRxHeartbeat,
       "hpicfServiceTunnelStatsTxHeartbeat": hpicfServiceTunnelStatsTxHeartbeat,
       "hpicfServiceTunnelLastHeartbeatPacketTimestamp": hpicfServiceTunnelLastHeartbeatPacketTimestamp,
       "hpicfServiceTunnelStatsClear": hpicfServiceTunnelStatsClear,
       "hpicfServiceTunnelConformance": hpicfServiceTunnelConformance,
       "hpicfServiceTunnelCompliances": hpicfServiceTunnelCompliances,
       "hpicfServiceTunnelCompliance": hpicfServiceTunnelCompliance,
       "hpicfServiceTunnelGroups": hpicfServiceTunnelGroups,
       "hpicfServiceScalarsGroup": hpicfServiceScalarsGroup,
       "hpicfServiceScalarsStatsGroup": hpicfServiceScalarsStatsGroup,
       "hpicfServiceTunnelGroup": hpicfServiceTunnelGroup,
       "hpicfServiceTunnelStatsGroup": hpicfServiceTunnelStatsGroup,
       "hpicfServiceTunnelNotificationGroup": hpicfServiceTunnelNotificationGroup,
       "hpicfServiceScalarsGroup1": hpicfServiceScalarsGroup1,
       "hpicfServiceTunnelGroup1": hpicfServiceTunnelGroup1}
)
