# SNMP MIB module (ELTEX-L2-TUNNEL-CONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ELTEX-L2-TUNNEL-CONFIG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:37:13 2024
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

(eltexLtd,) = mibBuilder.importSymbols(
    "ELTEX-SMI-ACTUAL",
    "eltexLtd")

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

eltexL2TunnelConfig = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 37)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class EltexLtcTunneledProtocolIndex(Integer32, TextualConvention):
    status = "current"
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

_EltexLtcMIBObjects_ObjectIdentity = ObjectIdentity
eltexLtcMIBObjects = _EltexLtcMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 37, 1)
)
_EltexLtcGlobal_ObjectIdentity = ObjectIdentity
eltexLtcGlobal = _EltexLtcGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 37, 1, 1)
)
_EltexLtcNotificationEnable_Type = TruthValue
_EltexLtcNotificationEnable_Object = MibScalar
eltexLtcNotificationEnable = _EltexLtcNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 37, 1, 1, 1),
    _EltexLtcNotificationEnable_Type()
)
eltexLtcNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexLtcNotificationEnable.setStatus("current")


class _EltexLtcTunnelMacAddress_Type(MacAddress):
    """Custom type eltexLtcTunnelMacAddress based on MacAddress"""
    defaultHexValue = "0100EEEE0000"


_EltexLtcTunnelMacAddress_Object = MibScalar
eltexLtcTunnelMacAddress = _EltexLtcTunnelMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 35265, 37, 1, 1, 2),
    _EltexLtcTunnelMacAddress_Type()
)
eltexLtcTunnelMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexLtcTunnelMacAddress.setStatus("current")
_EltexLtcTunneledProtocol_ObjectIdentity = ObjectIdentity
eltexLtcTunneledProtocol = _EltexLtcTunneledProtocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 37, 1, 2)
)
_EltexLtcTunneledProtocolTable_Object = MibTable
eltexLtcTunneledProtocolTable = _EltexLtcTunneledProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 37, 1, 2, 1)
)
if mibBuilder.loadTexts:
    eltexLtcTunneledProtocolTable.setStatus("current")
_EltexLtcTunneledProtocolEntry_Object = MibTableRow
eltexLtcTunneledProtocolEntry = _EltexLtcTunneledProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 37, 1, 2, 1, 1)
)
eltexLtcTunneledProtocolEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    eltexLtcTunneledProtocolEntry.setStatus("current")


class _EltexLtcTunneledProtocolType_Type(Bits):
    """Custom type eltexLtcTunneledProtocolType based on Bits"""
    namedValues = NamedValues(
        *(("stp", 0),
          ("workaround", 1))
    )

_EltexLtcTunneledProtocolType_Type.__name__ = "Bits"
_EltexLtcTunneledProtocolType_Object = MibTableColumn
eltexLtcTunneledProtocolType = _EltexLtcTunneledProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 37, 1, 2, 1, 1, 1),
    _EltexLtcTunneledProtocolType_Type()
)
eltexLtcTunneledProtocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexLtcTunneledProtocolType.setStatus("current")
_EltexLtcTunnelCos_Type = QosLayer2Cos
_EltexLtcTunnelCos_Object = MibTableColumn
eltexLtcTunnelCos = _EltexLtcTunnelCos_Object(
    (1, 3, 6, 1, 4, 1, 35265, 37, 1, 2, 1, 1, 2),
    _EltexLtcTunnelCos_Type()
)
eltexLtcTunnelCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexLtcTunnelCos.setStatus("current")
_EltexLtcTunnelThreshold_ObjectIdentity = ObjectIdentity
eltexLtcTunnelThreshold = _EltexLtcTunnelThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 37, 1, 3)
)
_EltexLtcTunnelThresholdTable_Object = MibTable
eltexLtcTunnelThresholdTable = _EltexLtcTunnelThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 37, 1, 3, 1)
)
if mibBuilder.loadTexts:
    eltexLtcTunnelThresholdTable.setStatus("current")
_EltexLtcTunnelThresholdEntry_Object = MibTableRow
eltexLtcTunnelThresholdEntry = _EltexLtcTunnelThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 37, 1, 3, 1, 1)
)
eltexLtcTunnelThresholdEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ELTEX-L2-TUNNEL-CONFIG-MIB", "eltexLtcTunnelThresholdProtocolIndex"),
)
if mibBuilder.loadTexts:
    eltexLtcTunnelThresholdEntry.setStatus("current")
_EltexLtcTunnelThresholdProtocolIndex_Type = EltexLtcTunneledProtocolIndex
_EltexLtcTunnelThresholdProtocolIndex_Object = MibTableColumn
eltexLtcTunnelThresholdProtocolIndex = _EltexLtcTunnelThresholdProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 37, 1, 3, 1, 1, 1),
    _EltexLtcTunnelThresholdProtocolIndex_Type()
)
eltexLtcTunnelThresholdProtocolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexLtcTunnelThresholdProtocolIndex.setStatus("current")


class _EltexLtcTunnelDropThreshold_Type(Unsigned32):
    """Custom type eltexLtcTunnelDropThreshold based on Unsigned32"""
    defaultValue = 0


_EltexLtcTunnelDropThreshold_Object = MibTableColumn
eltexLtcTunnelDropThreshold = _EltexLtcTunnelDropThreshold_Object(
    (1, 3, 6, 1, 4, 1, 35265, 37, 1, 3, 1, 1, 2),
    _EltexLtcTunnelDropThreshold_Type()
)
eltexLtcTunnelDropThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexLtcTunnelDropThreshold.setStatus("current")
if mibBuilder.loadTexts:
    eltexLtcTunnelDropThreshold.setUnits("PDUs/sec")


class _EltexLtcTunnelShutdownThreshold_Type(Unsigned32):
    """Custom type eltexLtcTunnelShutdownThreshold based on Unsigned32"""
    defaultValue = 0


_EltexLtcTunnelShutdownThreshold_Object = MibTableColumn
eltexLtcTunnelShutdownThreshold = _EltexLtcTunnelShutdownThreshold_Object(
    (1, 3, 6, 1, 4, 1, 35265, 37, 1, 3, 1, 1, 3),
    _EltexLtcTunnelShutdownThreshold_Type()
)
eltexLtcTunnelShutdownThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexLtcTunnelShutdownThreshold.setStatus("current")
if mibBuilder.loadTexts:
    eltexLtcTunnelShutdownThreshold.setUnits("PDUs/sec")
_EltexLtcTunnelStatistics_ObjectIdentity = ObjectIdentity
eltexLtcTunnelStatistics = _EltexLtcTunnelStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 37, 1, 4)
)
_EltexLtcTunnelStatisticsTable_Object = MibTable
eltexLtcTunnelStatisticsTable = _EltexLtcTunnelStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 37, 1, 4, 1)
)
if mibBuilder.loadTexts:
    eltexLtcTunnelStatisticsTable.setStatus("current")
_EltexLtcTunnelStatisticsEntry_Object = MibTableRow
eltexLtcTunnelStatisticsEntry = _EltexLtcTunnelStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 37, 1, 4, 1, 1)
)
eltexLtcTunnelStatisticsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ELTEX-L2-TUNNEL-CONFIG-MIB", "eltexLtcTunneledProtocolIndex"),
)
if mibBuilder.loadTexts:
    eltexLtcTunnelStatisticsEntry.setStatus("current")
_EltexLtcTunneledProtocolIndex_Type = EltexLtcTunneledProtocolIndex
_EltexLtcTunneledProtocolIndex_Object = MibTableColumn
eltexLtcTunneledProtocolIndex = _EltexLtcTunneledProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 37, 1, 4, 1, 1, 1),
    _EltexLtcTunneledProtocolIndex_Type()
)
eltexLtcTunneledProtocolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexLtcTunneledProtocolIndex.setStatus("current")
_EltexLtcTunnelEncapStats_Type = Counter32
_EltexLtcTunnelEncapStats_Object = MibTableColumn
eltexLtcTunnelEncapStats = _EltexLtcTunnelEncapStats_Object(
    (1, 3, 6, 1, 4, 1, 35265, 37, 1, 4, 1, 1, 2),
    _EltexLtcTunnelEncapStats_Type()
)
eltexLtcTunnelEncapStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexLtcTunnelEncapStats.setStatus("current")
if mibBuilder.loadTexts:
    eltexLtcTunnelEncapStats.setUnits("encapsulated PDUs")
_EltexLtcTunnelDecapStats_Type = Counter32
_EltexLtcTunnelDecapStats_Object = MibTableColumn
eltexLtcTunnelDecapStats = _EltexLtcTunnelDecapStats_Object(
    (1, 3, 6, 1, 4, 1, 35265, 37, 1, 4, 1, 1, 3),
    _EltexLtcTunnelDecapStats_Type()
)
eltexLtcTunnelDecapStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexLtcTunnelDecapStats.setStatus("current")
if mibBuilder.loadTexts:
    eltexLtcTunnelDecapStats.setUnits("de-encapsulated PDUs")
_EltexLtcTunnelDropStats_Type = Counter32
_EltexLtcTunnelDropStats_Object = MibTableColumn
eltexLtcTunnelDropStats = _EltexLtcTunnelDropStats_Object(
    (1, 3, 6, 1, 4, 1, 35265, 37, 1, 4, 1, 1, 4),
    _EltexLtcTunnelDropStats_Type()
)
eltexLtcTunnelDropStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexLtcTunnelDropStats.setStatus("current")
if mibBuilder.loadTexts:
    eltexLtcTunnelDropStats.setUnits("PDUs")
_EltexLtcMIBNotifications_ObjectIdentity = ObjectIdentity
eltexLtcMIBNotifications = _EltexLtcMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 37, 2)
)
_EltexLtcMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
eltexLtcMIBNotificationsPrefix = _EltexLtcMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 37, 2, 0)
)

# Managed Objects groups


# Notification objects

eltexLtcTunnelDropThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 37, 2, 0, 1)
)
eltexLtcTunnelDropThresholdExceeded.setObjects(
    ("ELTEX-L2-TUNNEL-CONFIG-MIB", "eltexLtcTunnelDropThreshold")
)
if mibBuilder.loadTexts:
    eltexLtcTunnelDropThresholdExceeded.setStatus(
        "current"
    )

eltexLtcTunnelShutdownThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 37, 2, 0, 2)
)
eltexLtcTunnelShutdownThresholdExceeded.setObjects(
    ("ELTEX-L2-TUNNEL-CONFIG-MIB", "eltexLtcTunnelShutdownThreshold")
)
if mibBuilder.loadTexts:
    eltexLtcTunnelShutdownThresholdExceeded.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-L2-TUNNEL-CONFIG-MIB",
    **{"EltexLtcTunneledProtocolIndex": EltexLtcTunneledProtocolIndex,
       "eltexL2TunnelConfig": eltexL2TunnelConfig,
       "eltexLtcMIBObjects": eltexLtcMIBObjects,
       "eltexLtcGlobal": eltexLtcGlobal,
       "eltexLtcNotificationEnable": eltexLtcNotificationEnable,
       "eltexLtcTunnelMacAddress": eltexLtcTunnelMacAddress,
       "eltexLtcTunneledProtocol": eltexLtcTunneledProtocol,
       "eltexLtcTunneledProtocolTable": eltexLtcTunneledProtocolTable,
       "eltexLtcTunneledProtocolEntry": eltexLtcTunneledProtocolEntry,
       "eltexLtcTunneledProtocolType": eltexLtcTunneledProtocolType,
       "eltexLtcTunnelCos": eltexLtcTunnelCos,
       "eltexLtcTunnelThreshold": eltexLtcTunnelThreshold,
       "eltexLtcTunnelThresholdTable": eltexLtcTunnelThresholdTable,
       "eltexLtcTunnelThresholdEntry": eltexLtcTunnelThresholdEntry,
       "eltexLtcTunnelThresholdProtocolIndex": eltexLtcTunnelThresholdProtocolIndex,
       "eltexLtcTunnelDropThreshold": eltexLtcTunnelDropThreshold,
       "eltexLtcTunnelShutdownThreshold": eltexLtcTunnelShutdownThreshold,
       "eltexLtcTunnelStatistics": eltexLtcTunnelStatistics,
       "eltexLtcTunnelStatisticsTable": eltexLtcTunnelStatisticsTable,
       "eltexLtcTunnelStatisticsEntry": eltexLtcTunnelStatisticsEntry,
       "eltexLtcTunneledProtocolIndex": eltexLtcTunneledProtocolIndex,
       "eltexLtcTunnelEncapStats": eltexLtcTunnelEncapStats,
       "eltexLtcTunnelDecapStats": eltexLtcTunnelDecapStats,
       "eltexLtcTunnelDropStats": eltexLtcTunnelDropStats,
       "eltexLtcMIBNotifications": eltexLtcMIBNotifications,
       "eltexLtcMIBNotificationsPrefix": eltexLtcMIBNotificationsPrefix,
       "eltexLtcTunnelDropThresholdExceeded": eltexLtcTunnelDropThresholdExceeded,
       "eltexLtcTunnelShutdownThresholdExceeded": eltexLtcTunnelShutdownThresholdExceeded}
)
