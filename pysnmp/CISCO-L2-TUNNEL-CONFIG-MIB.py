# SNMP MIB module (CISCO-L2-TUNNEL-CONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-L2-TUNNEL-CONFIG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:03:46 2024
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

(QosLayer2Cos,) = mibBuilder.importSymbols(
    "CISCO-QOS-PIB-MIB",
    "QosLayer2Cos")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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


# MODULE-IDENTITY

ciscoL2TunnelConfigMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 246)
)
ciscoL2TunnelConfigMIB.setRevisions(
        ("2007-02-15 00:00",
         "2006-07-25 00:00",
         "2005-06-27 00:00",
         "2004-06-09 00:00",
         "2003-09-03 00:00",
         "2002-05-31 10:00",
         "2002-02-14 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CltcMIBObjects_ObjectIdentity = ObjectIdentity
cltcMIBObjects = _CltcMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 246, 1)
)
_CltcGlobal_ObjectIdentity = ObjectIdentity
cltcGlobal = _CltcGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 246, 1, 1)
)
_CltcTunnelCos_Type = QosLayer2Cos
_CltcTunnelCos_Object = MibScalar
cltcTunnelCos = _CltcTunnelCos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 246, 1, 1, 1),
    _CltcTunnelCos_Type()
)
cltcTunnelCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cltcTunnelCos.setStatus("current")
_CltcNotificationEnable_Type = TruthValue
_CltcNotificationEnable_Object = MibScalar
cltcNotificationEnable = _CltcNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 246, 1, 1, 2),
    _CltcNotificationEnable_Type()
)
cltcNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cltcNotificationEnable.setStatus("current")
_CltcTunnelSysDropThreshold_Type = Unsigned32
_CltcTunnelSysDropThreshold_Object = MibScalar
cltcTunnelSysDropThreshold = _CltcTunnelSysDropThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 246, 1, 1, 3),
    _CltcTunnelSysDropThreshold_Type()
)
cltcTunnelSysDropThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cltcTunnelSysDropThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cltcTunnelSysDropThreshold.setUnits("PDUs/sec")
_CltcTunnelSysDropNotifEnable_Type = TruthValue
_CltcTunnelSysDropNotifEnable_Object = MibScalar
cltcTunnelSysDropNotifEnable = _CltcTunnelSysDropNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 246, 1, 1, 4),
    _CltcTunnelSysDropNotifEnable_Type()
)
cltcTunnelSysDropNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cltcTunnelSysDropNotifEnable.setStatus("current")
_CltcDot1qTunnel_ObjectIdentity = ObjectIdentity
cltcDot1qTunnel = _CltcDot1qTunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 246, 1, 2)
)
_CltcDot1qTunnelTable_Object = MibTable
cltcDot1qTunnelTable = _CltcDot1qTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 246, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cltcDot1qTunnelTable.setStatus("current")
_CltcDot1qTunnelEntry_Object = MibTableRow
cltcDot1qTunnelEntry = _CltcDot1qTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 246, 1, 2, 1, 1)
)
cltcDot1qTunnelEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cltcDot1qTunnelEntry.setStatus("current")


class _CltcDot1qTunnelMode_Type(Integer32):
    """Custom type cltcDot1qTunnelMode based on Integer32"""
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


_CltcDot1qTunnelMode_Type.__name__ = "Integer32"
_CltcDot1qTunnelMode_Object = MibTableColumn
cltcDot1qTunnelMode = _CltcDot1qTunnelMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 246, 1, 2, 1, 1, 1),
    _CltcDot1qTunnelMode_Type()
)
cltcDot1qTunnelMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cltcDot1qTunnelMode.setStatus("current")
_CltcTunneledProtocol_ObjectIdentity = ObjectIdentity
cltcTunneledProtocol = _CltcTunneledProtocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 246, 1, 3)
)
_CltcTunneledProtocolTable_Object = MibTable
cltcTunneledProtocolTable = _CltcTunneledProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 246, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cltcTunneledProtocolTable.setStatus("current")
_CltcTunneledProtocolEntry_Object = MibTableRow
cltcTunneledProtocolEntry = _CltcTunneledProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 246, 1, 3, 1, 1)
)
cltcTunneledProtocolEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cltcTunneledProtocolEntry.setStatus("current")


class _CltcTunneledProtocolType_Type(Bits):
    """Custom type cltcTunneledProtocolType based on Bits"""
    namedValues = NamedValues(
        *(("cdp", 0),
          ("eoam", 3),
          ("lldp", 4),
          ("stp", 2),
          ("vtp", 1))
    )

_CltcTunneledProtocolType_Type.__name__ = "Bits"
_CltcTunneledProtocolType_Object = MibTableColumn
cltcTunneledProtocolType = _CltcTunneledProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 246, 1, 3, 1, 1, 1),
    _CltcTunneledProtocolType_Type()
)
cltcTunneledProtocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cltcTunneledProtocolType.setStatus("current")
_CltcTunnelThreshold_ObjectIdentity = ObjectIdentity
cltcTunnelThreshold = _CltcTunnelThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 246, 1, 4)
)
_CltcTunnelThresholdTable_Object = MibTable
cltcTunnelThresholdTable = _CltcTunnelThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 246, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cltcTunnelThresholdTable.setStatus("current")
_CltcTunnelThresholdEntry_Object = MibTableRow
cltcTunnelThresholdEntry = _CltcTunnelThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 246, 1, 4, 1, 1)
)
cltcTunnelThresholdEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-L2-TUNNEL-CONFIG-MIB", "cltcTunnelThresholdProtocolIndex"),
)
if mibBuilder.loadTexts:
    cltcTunnelThresholdEntry.setStatus("current")


class _CltcTunnelThresholdProtocolIndex_Type(Integer32):
    """Custom type cltcTunnelThresholdProtocolIndex based on Integer32"""
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
        *(("all", 1),
          ("cdp", 2),
          ("eoam", 5),
          ("lldp", 6),
          ("stp", 4),
          ("vtp", 3))
    )


_CltcTunnelThresholdProtocolIndex_Type.__name__ = "Integer32"
_CltcTunnelThresholdProtocolIndex_Object = MibTableColumn
cltcTunnelThresholdProtocolIndex = _CltcTunnelThresholdProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 246, 1, 4, 1, 1, 1),
    _CltcTunnelThresholdProtocolIndex_Type()
)
cltcTunnelThresholdProtocolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cltcTunnelThresholdProtocolIndex.setStatus("current")


class _CltcTunnelDropThreshold_Type(Unsigned32):
    """Custom type cltcTunnelDropThreshold based on Unsigned32"""
    defaultValue = 0


_CltcTunnelDropThreshold_Object = MibTableColumn
cltcTunnelDropThreshold = _CltcTunnelDropThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 246, 1, 4, 1, 1, 2),
    _CltcTunnelDropThreshold_Type()
)
cltcTunnelDropThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cltcTunnelDropThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cltcTunnelDropThreshold.setUnits("PDUs/sec")


class _CltcTunnelShutdownThreshold_Type(Unsigned32):
    """Custom type cltcTunnelShutdownThreshold based on Unsigned32"""
    defaultValue = 0


_CltcTunnelShutdownThreshold_Object = MibTableColumn
cltcTunnelShutdownThreshold = _CltcTunnelShutdownThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 246, 1, 4, 1, 1, 3),
    _CltcTunnelShutdownThreshold_Type()
)
cltcTunnelShutdownThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cltcTunnelShutdownThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cltcTunnelShutdownThreshold.setUnits("PDUs/sec")
_CltcTunnelStatistics_ObjectIdentity = ObjectIdentity
cltcTunnelStatistics = _CltcTunnelStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 246, 1, 5)
)
_CltcTunnelStatisticsTable_Object = MibTable
cltcTunnelStatisticsTable = _CltcTunnelStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 246, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cltcTunnelStatisticsTable.setStatus("current")
_CltcTunnelStatisticsEntry_Object = MibTableRow
cltcTunnelStatisticsEntry = _CltcTunnelStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 246, 1, 5, 1, 1)
)
cltcTunnelStatisticsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-L2-TUNNEL-CONFIG-MIB", "cltcTunneledProtocolIndex"),
)
if mibBuilder.loadTexts:
    cltcTunnelStatisticsEntry.setStatus("current")


class _CltcTunneledProtocolIndex_Type(Integer32):
    """Custom type cltcTunneledProtocolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("cdp", 2),
          ("eoam", 5),
          ("lldp", 6),
          ("stp", 4),
          ("vtp", 3))
    )


_CltcTunneledProtocolIndex_Type.__name__ = "Integer32"
_CltcTunneledProtocolIndex_Object = MibTableColumn
cltcTunneledProtocolIndex = _CltcTunneledProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 246, 1, 5, 1, 1, 1),
    _CltcTunneledProtocolIndex_Type()
)
cltcTunneledProtocolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cltcTunneledProtocolIndex.setStatus("current")
_CltcTunnelEncapStats_Type = Counter32
_CltcTunnelEncapStats_Object = MibTableColumn
cltcTunnelEncapStats = _CltcTunnelEncapStats_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 246, 1, 5, 1, 1, 2),
    _CltcTunnelEncapStats_Type()
)
cltcTunnelEncapStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cltcTunnelEncapStats.setStatus("current")
if mibBuilder.loadTexts:
    cltcTunnelEncapStats.setUnits("encapsulated PDUs")
_CltcTunnelDeEncapStats_Type = Counter32
_CltcTunnelDeEncapStats_Object = MibTableColumn
cltcTunnelDeEncapStats = _CltcTunnelDeEncapStats_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 246, 1, 5, 1, 1, 3),
    _CltcTunnelDeEncapStats_Type()
)
cltcTunnelDeEncapStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cltcTunnelDeEncapStats.setStatus("current")
if mibBuilder.loadTexts:
    cltcTunnelDeEncapStats.setUnits("de-encapsulated PDUs")
_CltcTunnelDropStats_Type = Counter32
_CltcTunnelDropStats_Object = MibTableColumn
cltcTunnelDropStats = _CltcTunnelDropStats_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 246, 1, 5, 1, 1, 4),
    _CltcTunnelDropStats_Type()
)
cltcTunnelDropStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cltcTunnelDropStats.setStatus("current")
if mibBuilder.loadTexts:
    cltcTunnelDropStats.setUnits("PDUs")
_CltcTunnelDropStatTable_Object = MibTable
cltcTunnelDropStatTable = _CltcTunnelDropStatTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 246, 1, 5, 2)
)
if mibBuilder.loadTexts:
    cltcTunnelDropStatTable.setStatus("current")
_CltcTunnelDropStatEntry_Object = MibTableRow
cltcTunnelDropStatEntry = _CltcTunnelDropStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 246, 1, 5, 2, 1)
)
cltcTunnelDropStatEntry.setIndexNames(
    (0, "CISCO-L2-TUNNEL-CONFIG-MIB", "cltcTunneledProtocolIndex"),
)
if mibBuilder.loadTexts:
    cltcTunnelDropStatEntry.setStatus("current")
_CltcTunnelTotalDropStats_Type = Counter32
_CltcTunnelTotalDropStats_Object = MibTableColumn
cltcTunnelTotalDropStats = _CltcTunnelTotalDropStats_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 246, 1, 5, 2, 1, 1),
    _CltcTunnelTotalDropStats_Type()
)
cltcTunnelTotalDropStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cltcTunnelTotalDropStats.setStatus("current")
if mibBuilder.loadTexts:
    cltcTunnelTotalDropStats.setUnits("encapsulated PDUs")
_CltcDot1qAllTagged_ObjectIdentity = ObjectIdentity
cltcDot1qAllTagged = _CltcDot1qAllTagged_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 246, 1, 6)
)
_CltcDot1qAllTaggedEnabled_Type = TruthValue
_CltcDot1qAllTaggedEnabled_Object = MibScalar
cltcDot1qAllTaggedEnabled = _CltcDot1qAllTaggedEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 246, 1, 6, 1),
    _CltcDot1qAllTaggedEnabled_Type()
)
cltcDot1qAllTaggedEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cltcDot1qAllTaggedEnabled.setStatus("current")
_CltcDot1qAllTaggedIfTable_Object = MibTable
cltcDot1qAllTaggedIfTable = _CltcDot1qAllTaggedIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 246, 1, 6, 2)
)
if mibBuilder.loadTexts:
    cltcDot1qAllTaggedIfTable.setStatus("current")
_CltcDot1qAllTaggedIfEntry_Object = MibTableRow
cltcDot1qAllTaggedIfEntry = _CltcDot1qAllTaggedIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 246, 1, 6, 2, 1)
)
cltcDot1qAllTaggedIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cltcDot1qAllTaggedIfEntry.setStatus("current")
_CltcDot1qAllTaggedIfEnabled_Type = TruthValue
_CltcDot1qAllTaggedIfEnabled_Object = MibTableColumn
cltcDot1qAllTaggedIfEnabled = _CltcDot1qAllTaggedIfEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 246, 1, 6, 2, 1, 1),
    _CltcDot1qAllTaggedIfEnabled_Type()
)
cltcDot1qAllTaggedIfEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cltcDot1qAllTaggedIfEnabled.setStatus("current")
_CltcMIBNotifications_ObjectIdentity = ObjectIdentity
cltcMIBNotifications = _CltcMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 246, 2)
)
_CltcMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
cltcMIBNotificationsPrefix = _CltcMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 246, 2, 0)
)
_CltcMIBConformance_ObjectIdentity = ObjectIdentity
cltcMIBConformance = _CltcMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 246, 3)
)
_CltcMIBCompliances_ObjectIdentity = ObjectIdentity
cltcMIBCompliances = _CltcMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 246, 3, 1)
)
_CltcMIBGroups_ObjectIdentity = ObjectIdentity
cltcMIBGroups = _CltcMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 246, 3, 2)
)

# Managed Objects groups

cltcDot1qTunnelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 246, 3, 2, 1)
)
cltcDot1qTunnelGroup.setObjects(
    ("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcDot1qTunnelMode")
)
if mibBuilder.loadTexts:
    cltcDot1qTunnelGroup.setStatus("current")

cltcTunneledProtocolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 246, 3, 2, 2)
)
cltcTunneledProtocolGroup.setObjects(
      *(("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcTunneledProtocolType"),
        ("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcTunnelCos"))
)
if mibBuilder.loadTexts:
    cltcTunneledProtocolGroup.setStatus("current")

cltcTunnelThresholdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 246, 3, 2, 3)
)
cltcTunnelThresholdGroup.setObjects(
      *(("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcTunnelDropThreshold"),
        ("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcTunnelShutdownThreshold"))
)
if mibBuilder.loadTexts:
    cltcTunnelThresholdGroup.setStatus("current")

cltcTunnelStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 246, 3, 2, 4)
)
cltcTunnelStatisticsGroup.setObjects(
      *(("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcTunnelEncapStats"),
        ("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcTunnelDeEncapStats"))
)
if mibBuilder.loadTexts:
    cltcTunnelStatisticsGroup.setStatus("current")

cltcDot1qAllTaggedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 246, 3, 2, 5)
)
cltcDot1qAllTaggedGroup.setObjects(
      *(("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcDot1qAllTaggedEnabled"),
        ("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcDot1qAllTaggedIfEnabled"))
)
if mibBuilder.loadTexts:
    cltcDot1qAllTaggedGroup.setStatus("current")

cltcTunnelDropStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 246, 3, 2, 6)
)
cltcTunnelDropStatisticsGroup.setObjects(
    ("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcTunnelDropStats")
)
if mibBuilder.loadTexts:
    cltcTunnelDropStatisticsGroup.setStatus("current")

cltcNotifsEnableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 246, 3, 2, 7)
)
cltcNotifsEnableGroup.setObjects(
    ("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcNotificationEnable")
)
if mibBuilder.loadTexts:
    cltcNotifsEnableGroup.setStatus("current")

cltcTunnelTotalDropGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 246, 3, 2, 9)
)
cltcTunnelTotalDropGroup.setObjects(
    ("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcTunnelTotalDropStats")
)
if mibBuilder.loadTexts:
    cltcTunnelTotalDropGroup.setStatus("current")

cltcTunnelSysDropNotifEnableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 246, 3, 2, 10)
)
cltcTunnelSysDropNotifEnableGroup.setObjects(
    ("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcTunnelSysDropNotifEnable")
)
if mibBuilder.loadTexts:
    cltcTunnelSysDropNotifEnableGroup.setStatus("current")

cltcTunnelSysDropGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 246, 3, 2, 11)
)
cltcTunnelSysDropGroup.setObjects(
    ("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcTunnelSysDropThreshold")
)
if mibBuilder.loadTexts:
    cltcTunnelSysDropGroup.setStatus("current")


# Notification objects

cltcTunnelDropThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 246, 2, 0, 1)
)
cltcTunnelDropThresholdExceeded.setObjects(
    ("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcTunnelDropThreshold")
)
if mibBuilder.loadTexts:
    cltcTunnelDropThresholdExceeded.setStatus(
        "current"
    )

cltcTunnelShutdownThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 246, 2, 0, 2)
)
cltcTunnelShutdownThresholdExceeded.setObjects(
    ("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcTunnelShutdownThreshold")
)
if mibBuilder.loadTexts:
    cltcTunnelShutdownThresholdExceeded.setStatus(
        "current"
    )

cltcTunnelSysDropThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 246, 2, 0, 3)
)
cltcTunnelSysDropThresholdExceeded.setObjects(
    ("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcTunnelSysDropThreshold")
)
if mibBuilder.loadTexts:
    cltcTunnelSysDropThresholdExceeded.setStatus(
        "current"
    )


# Notifications groups

cltcTunnelThresholdNotifsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 246, 3, 2, 8)
)
cltcTunnelThresholdNotifsGroup.setObjects(
      *(("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcTunnelDropThresholdExceeded"),
        ("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcTunnelShutdownThresholdExceeded"))
)
if mibBuilder.loadTexts:
    cltcTunnelThresholdNotifsGroup.setStatus(
        "current"
    )

cltcTunnelSysDropNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 246, 3, 2, 12)
)
cltcTunnelSysDropNotifGroup.setObjects(
    ("CISCO-L2-TUNNEL-CONFIG-MIB", "cltcTunnelSysDropThresholdExceeded")
)
if mibBuilder.loadTexts:
    cltcTunnelSysDropNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cltcMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 246, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cltcMIBCompliance.setStatus(
        "deprecated"
    )

cltcMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 246, 3, 1, 2)
)
if mibBuilder.loadTexts:
    cltcMIBCompliance2.setStatus(
        "deprecated"
    )

cltcMIBCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 246, 3, 1, 3)
)
if mibBuilder.loadTexts:
    cltcMIBCompliance3.setStatus(
        "deprecated"
    )

cltcMIBCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 246, 3, 1, 4)
)
if mibBuilder.loadTexts:
    cltcMIBCompliance4.setStatus(
        "deprecated"
    )

cltcMIBCompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 246, 3, 1, 5)
)
if mibBuilder.loadTexts:
    cltcMIBCompliance5.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-L2-TUNNEL-CONFIG-MIB",
    **{"ciscoL2TunnelConfigMIB": ciscoL2TunnelConfigMIB,
       "cltcMIBObjects": cltcMIBObjects,
       "cltcGlobal": cltcGlobal,
       "cltcTunnelCos": cltcTunnelCos,
       "cltcNotificationEnable": cltcNotificationEnable,
       "cltcTunnelSysDropThreshold": cltcTunnelSysDropThreshold,
       "cltcTunnelSysDropNotifEnable": cltcTunnelSysDropNotifEnable,
       "cltcDot1qTunnel": cltcDot1qTunnel,
       "cltcDot1qTunnelTable": cltcDot1qTunnelTable,
       "cltcDot1qTunnelEntry": cltcDot1qTunnelEntry,
       "cltcDot1qTunnelMode": cltcDot1qTunnelMode,
       "cltcTunneledProtocol": cltcTunneledProtocol,
       "cltcTunneledProtocolTable": cltcTunneledProtocolTable,
       "cltcTunneledProtocolEntry": cltcTunneledProtocolEntry,
       "cltcTunneledProtocolType": cltcTunneledProtocolType,
       "cltcTunnelThreshold": cltcTunnelThreshold,
       "cltcTunnelThresholdTable": cltcTunnelThresholdTable,
       "cltcTunnelThresholdEntry": cltcTunnelThresholdEntry,
       "cltcTunnelThresholdProtocolIndex": cltcTunnelThresholdProtocolIndex,
       "cltcTunnelDropThreshold": cltcTunnelDropThreshold,
       "cltcTunnelShutdownThreshold": cltcTunnelShutdownThreshold,
       "cltcTunnelStatistics": cltcTunnelStatistics,
       "cltcTunnelStatisticsTable": cltcTunnelStatisticsTable,
       "cltcTunnelStatisticsEntry": cltcTunnelStatisticsEntry,
       "cltcTunneledProtocolIndex": cltcTunneledProtocolIndex,
       "cltcTunnelEncapStats": cltcTunnelEncapStats,
       "cltcTunnelDeEncapStats": cltcTunnelDeEncapStats,
       "cltcTunnelDropStats": cltcTunnelDropStats,
       "cltcTunnelDropStatTable": cltcTunnelDropStatTable,
       "cltcTunnelDropStatEntry": cltcTunnelDropStatEntry,
       "cltcTunnelTotalDropStats": cltcTunnelTotalDropStats,
       "cltcDot1qAllTagged": cltcDot1qAllTagged,
       "cltcDot1qAllTaggedEnabled": cltcDot1qAllTaggedEnabled,
       "cltcDot1qAllTaggedIfTable": cltcDot1qAllTaggedIfTable,
       "cltcDot1qAllTaggedIfEntry": cltcDot1qAllTaggedIfEntry,
       "cltcDot1qAllTaggedIfEnabled": cltcDot1qAllTaggedIfEnabled,
       "cltcMIBNotifications": cltcMIBNotifications,
       "cltcMIBNotificationsPrefix": cltcMIBNotificationsPrefix,
       "cltcTunnelDropThresholdExceeded": cltcTunnelDropThresholdExceeded,
       "cltcTunnelShutdownThresholdExceeded": cltcTunnelShutdownThresholdExceeded,
       "cltcTunnelSysDropThresholdExceeded": cltcTunnelSysDropThresholdExceeded,
       "cltcMIBConformance": cltcMIBConformance,
       "cltcMIBCompliances": cltcMIBCompliances,
       "cltcMIBCompliance": cltcMIBCompliance,
       "cltcMIBCompliance2": cltcMIBCompliance2,
       "cltcMIBCompliance3": cltcMIBCompliance3,
       "cltcMIBCompliance4": cltcMIBCompliance4,
       "cltcMIBCompliance5": cltcMIBCompliance5,
       "cltcMIBGroups": cltcMIBGroups,
       "cltcDot1qTunnelGroup": cltcDot1qTunnelGroup,
       "cltcTunneledProtocolGroup": cltcTunneledProtocolGroup,
       "cltcTunnelThresholdGroup": cltcTunnelThresholdGroup,
       "cltcTunnelStatisticsGroup": cltcTunnelStatisticsGroup,
       "cltcDot1qAllTaggedGroup": cltcDot1qAllTaggedGroup,
       "cltcTunnelDropStatisticsGroup": cltcTunnelDropStatisticsGroup,
       "cltcNotifsEnableGroup": cltcNotifsEnableGroup,
       "cltcTunnelThresholdNotifsGroup": cltcTunnelThresholdNotifsGroup,
       "cltcTunnelTotalDropGroup": cltcTunnelTotalDropGroup,
       "cltcTunnelSysDropNotifEnableGroup": cltcTunnelSysDropNotifEnableGroup,
       "cltcTunnelSysDropGroup": cltcTunnelSysDropGroup,
       "cltcTunnelSysDropNotifGroup": cltcTunnelSysDropNotifGroup}
)
