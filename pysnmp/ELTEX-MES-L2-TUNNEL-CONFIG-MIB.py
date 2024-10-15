# SNMP MIB module (ELTEX-MES-L2-TUNNEL-CONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ELTEX-MES-L2-TUNNEL-CONFIG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:37:49 2024
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

(eltMes,) = mibBuilder.importSymbols(
    "ELTEX-MES",
    "eltMes")

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
 MacAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

eltMesL2TunnelConfig = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 13)
)
eltMesL2TunnelConfig.setRevisions(
        ("2015-11-19 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class EltLtcTunneledProtocolIndex(Integer32, TextualConvention):
    status = "deprecated"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("stp", 1)
    )



# MIB Managed Objects in the order of their OIDs

_EltMesLtcMIBObjects_ObjectIdentity = ObjectIdentity
eltMesLtcMIBObjects = _EltMesLtcMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 1)
)
_EltMesLtcGlobal_ObjectIdentity = ObjectIdentity
eltMesLtcGlobal = _EltMesLtcGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 1, 1)
)
_EltLtcNotificationEnable_Type = TruthValue
_EltLtcNotificationEnable_Object = MibScalar
eltLtcNotificationEnable = _EltLtcNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 1, 1, 1),
    _EltLtcNotificationEnable_Type()
)
eltLtcNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltLtcNotificationEnable.setStatus("deprecated")


class _EltLtcTunnelMacAddress_Type(MacAddress):
    """Custom type eltLtcTunnelMacAddress based on MacAddress"""
    defaultHexValue = "0100EEEE0000"


_EltLtcTunnelMacAddress_Object = MibScalar
eltLtcTunnelMacAddress = _EltLtcTunnelMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 1, 1, 2),
    _EltLtcTunnelMacAddress_Type()
)
eltLtcTunnelMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltLtcTunnelMacAddress.setStatus("deprecated")
_EltMesLtcTunneledProtocol_ObjectIdentity = ObjectIdentity
eltMesLtcTunneledProtocol = _EltMesLtcTunneledProtocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 1, 2)
)
_EltLtcTunneledProtocolTable_Object = MibTable
eltLtcTunneledProtocolTable = _EltLtcTunneledProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 1, 2, 1)
)
if mibBuilder.loadTexts:
    eltLtcTunneledProtocolTable.setStatus("deprecated")
_EltLtcTunneledProtocolEntry_Object = MibTableRow
eltLtcTunneledProtocolEntry = _EltLtcTunneledProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 1, 2, 1, 1)
)
eltLtcTunneledProtocolEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    eltLtcTunneledProtocolEntry.setStatus("deprecated")


class _EltLtcTunneledProtocolType_Type(Bits):
    """Custom type eltLtcTunneledProtocolType based on Bits"""
    namedValues = NamedValues(
        *(("stp", 0),
          ("workaround", 1))
    )

_EltLtcTunneledProtocolType_Type.__name__ = "Bits"
_EltLtcTunneledProtocolType_Object = MibTableColumn
eltLtcTunneledProtocolType = _EltLtcTunneledProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 1, 2, 1, 1, 1),
    _EltLtcTunneledProtocolType_Type()
)
eltLtcTunneledProtocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltLtcTunneledProtocolType.setStatus("deprecated")
_EltLtcTunnelCos_Type = QosLayer2Cos
_EltLtcTunnelCos_Object = MibTableColumn
eltLtcTunnelCos = _EltLtcTunnelCos_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 1, 2, 1, 1, 2),
    _EltLtcTunnelCos_Type()
)
eltLtcTunnelCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltLtcTunnelCos.setStatus("deprecated")
_EltMesLtcTunnelThreshold_ObjectIdentity = ObjectIdentity
eltMesLtcTunnelThreshold = _EltMesLtcTunnelThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 1, 3)
)
_EltLtcTunnelThresholdTable_Object = MibTable
eltLtcTunnelThresholdTable = _EltLtcTunnelThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 1, 3, 1)
)
if mibBuilder.loadTexts:
    eltLtcTunnelThresholdTable.setStatus("deprecated")
_EltLtcTunnelThresholdEntry_Object = MibTableRow
eltLtcTunnelThresholdEntry = _EltLtcTunnelThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 1, 3, 1, 1)
)
eltLtcTunnelThresholdEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ELTEX-MES-L2-TUNNEL-CONFIG-MIB", "eltLtcTunnelThresholdProtocolIndex"),
)
if mibBuilder.loadTexts:
    eltLtcTunnelThresholdEntry.setStatus("deprecated")
_EltLtcTunnelThresholdProtocolIndex_Type = EltLtcTunneledProtocolIndex
_EltLtcTunnelThresholdProtocolIndex_Object = MibTableColumn
eltLtcTunnelThresholdProtocolIndex = _EltLtcTunnelThresholdProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 1, 3, 1, 1, 1),
    _EltLtcTunnelThresholdProtocolIndex_Type()
)
eltLtcTunnelThresholdProtocolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltLtcTunnelThresholdProtocolIndex.setStatus("deprecated")


class _EltLtcTunnelDropThreshold_Type(Unsigned32):
    """Custom type eltLtcTunnelDropThreshold based on Unsigned32"""
    defaultValue = 0


_EltLtcTunnelDropThreshold_Object = MibTableColumn
eltLtcTunnelDropThreshold = _EltLtcTunnelDropThreshold_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 1, 3, 1, 1, 2),
    _EltLtcTunnelDropThreshold_Type()
)
eltLtcTunnelDropThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltLtcTunnelDropThreshold.setStatus("deprecated")
if mibBuilder.loadTexts:
    eltLtcTunnelDropThreshold.setUnits("PDUs/sec")


class _EltLtcTunnelShutdownThreshold_Type(Unsigned32):
    """Custom type eltLtcTunnelShutdownThreshold based on Unsigned32"""
    defaultValue = 0


_EltLtcTunnelShutdownThreshold_Object = MibTableColumn
eltLtcTunnelShutdownThreshold = _EltLtcTunnelShutdownThreshold_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 1, 3, 1, 1, 3),
    _EltLtcTunnelShutdownThreshold_Type()
)
eltLtcTunnelShutdownThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltLtcTunnelShutdownThreshold.setStatus("deprecated")
if mibBuilder.loadTexts:
    eltLtcTunnelShutdownThreshold.setUnits("PDUs/sec")
_EltMesLtcTunnelStatistics_ObjectIdentity = ObjectIdentity
eltMesLtcTunnelStatistics = _EltMesLtcTunnelStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 1, 4)
)
_EltLtcTunnelStatisticsTable_Object = MibTable
eltLtcTunnelStatisticsTable = _EltLtcTunnelStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 1, 4, 1)
)
if mibBuilder.loadTexts:
    eltLtcTunnelStatisticsTable.setStatus("deprecated")
_EltLtcTunnelStatisticsEntry_Object = MibTableRow
eltLtcTunnelStatisticsEntry = _EltLtcTunnelStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 1, 4, 1, 1)
)
eltLtcTunnelStatisticsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ELTEX-MES-L2-TUNNEL-CONFIG-MIB", "eltLtcTunneledProtocolIndex"),
)
if mibBuilder.loadTexts:
    eltLtcTunnelStatisticsEntry.setStatus("deprecated")
_EltLtcTunneledProtocolIndex_Type = EltLtcTunneledProtocolIndex
_EltLtcTunneledProtocolIndex_Object = MibTableColumn
eltLtcTunneledProtocolIndex = _EltLtcTunneledProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 1, 4, 1, 1, 1),
    _EltLtcTunneledProtocolIndex_Type()
)
eltLtcTunneledProtocolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltLtcTunneledProtocolIndex.setStatus("deprecated")
_EltLtcTunnelEncapStats_Type = Counter32
_EltLtcTunnelEncapStats_Object = MibTableColumn
eltLtcTunnelEncapStats = _EltLtcTunnelEncapStats_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 1, 4, 1, 1, 2),
    _EltLtcTunnelEncapStats_Type()
)
eltLtcTunnelEncapStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltLtcTunnelEncapStats.setStatus("deprecated")
if mibBuilder.loadTexts:
    eltLtcTunnelEncapStats.setUnits("encapsulated PDUs")
_EltLtcTunnelDecapStats_Type = Counter32
_EltLtcTunnelDecapStats_Object = MibTableColumn
eltLtcTunnelDecapStats = _EltLtcTunnelDecapStats_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 1, 4, 1, 1, 3),
    _EltLtcTunnelDecapStats_Type()
)
eltLtcTunnelDecapStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltLtcTunnelDecapStats.setStatus("deprecated")
if mibBuilder.loadTexts:
    eltLtcTunnelDecapStats.setUnits("de-encapsulated PDUs")
_EltLtcTunnelDropStats_Type = Counter32
_EltLtcTunnelDropStats_Object = MibTableColumn
eltLtcTunnelDropStats = _EltLtcTunnelDropStats_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 1, 4, 1, 1, 4),
    _EltLtcTunnelDropStats_Type()
)
eltLtcTunnelDropStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltLtcTunnelDropStats.setStatus("deprecated")
if mibBuilder.loadTexts:
    eltLtcTunnelDropStats.setUnits("PDUs")
_EltMesLtcMIBNotifications_ObjectIdentity = ObjectIdentity
eltMesLtcMIBNotifications = _EltMesLtcMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 2)
)
_EltMesLtcMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
eltMesLtcMIBNotificationsPrefix = _EltMesLtcMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 2, 0)
)

# Managed Objects groups


# Notification objects

eltLtcTunnelDropThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 2, 0, 1)
)
eltLtcTunnelDropThresholdExceeded.setObjects(
    ("ELTEX-MES-L2-TUNNEL-CONFIG-MIB", "eltLtcTunnelDropThreshold")
)
if mibBuilder.loadTexts:
    eltLtcTunnelDropThresholdExceeded.setStatus(
        "deprecated"
    )

eltLtcTunnelShutdownThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 13, 2, 0, 2)
)
eltLtcTunnelShutdownThresholdExceeded.setObjects(
    ("ELTEX-MES-L2-TUNNEL-CONFIG-MIB", "eltLtcTunnelShutdownThreshold")
)
if mibBuilder.loadTexts:
    eltLtcTunnelShutdownThresholdExceeded.setStatus(
        "deprecated"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-L2-TUNNEL-CONFIG-MIB",
    **{"EltLtcTunneledProtocolIndex": EltLtcTunneledProtocolIndex,
       "eltMesL2TunnelConfig": eltMesL2TunnelConfig,
       "eltMesLtcMIBObjects": eltMesLtcMIBObjects,
       "eltMesLtcGlobal": eltMesLtcGlobal,
       "eltLtcNotificationEnable": eltLtcNotificationEnable,
       "eltLtcTunnelMacAddress": eltLtcTunnelMacAddress,
       "eltMesLtcTunneledProtocol": eltMesLtcTunneledProtocol,
       "eltLtcTunneledProtocolTable": eltLtcTunneledProtocolTable,
       "eltLtcTunneledProtocolEntry": eltLtcTunneledProtocolEntry,
       "eltLtcTunneledProtocolType": eltLtcTunneledProtocolType,
       "eltLtcTunnelCos": eltLtcTunnelCos,
       "eltMesLtcTunnelThreshold": eltMesLtcTunnelThreshold,
       "eltLtcTunnelThresholdTable": eltLtcTunnelThresholdTable,
       "eltLtcTunnelThresholdEntry": eltLtcTunnelThresholdEntry,
       "eltLtcTunnelThresholdProtocolIndex": eltLtcTunnelThresholdProtocolIndex,
       "eltLtcTunnelDropThreshold": eltLtcTunnelDropThreshold,
       "eltLtcTunnelShutdownThreshold": eltLtcTunnelShutdownThreshold,
       "eltMesLtcTunnelStatistics": eltMesLtcTunnelStatistics,
       "eltLtcTunnelStatisticsTable": eltLtcTunnelStatisticsTable,
       "eltLtcTunnelStatisticsEntry": eltLtcTunnelStatisticsEntry,
       "eltLtcTunneledProtocolIndex": eltLtcTunneledProtocolIndex,
       "eltLtcTunnelEncapStats": eltLtcTunnelEncapStats,
       "eltLtcTunnelDecapStats": eltLtcTunnelDecapStats,
       "eltLtcTunnelDropStats": eltLtcTunnelDropStats,
       "eltMesLtcMIBNotifications": eltMesLtcMIBNotifications,
       "eltMesLtcMIBNotificationsPrefix": eltMesLtcMIBNotificationsPrefix,
       "eltLtcTunnelDropThresholdExceeded": eltLtcTunnelDropThresholdExceeded,
       "eltLtcTunnelShutdownThresholdExceeded": eltLtcTunnelShutdownThresholdExceeded}
)
