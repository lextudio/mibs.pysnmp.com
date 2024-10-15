# SNMP MIB module (ALTEON-ASF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALTEON-ASF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:37:47 2024
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

(firewall,) = mibBuilder.importSymbols(
    "ALTEON-ROOT-MIB",
    "firewall")

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
 MacAddress,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

alteonAsfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1)
)
alteonAsfMIB.setRevisions(
        ("1902-03-11 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AsfStatistics_ObjectIdentity = ObjectIdentity
asfStatistics = _AsfStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 9)
)
if mibBuilder.loadTexts:
    asfStatistics.setStatus("current")
_AsfPortStats_ObjectIdentity = ObjectIdentity
asfPortStats = _AsfPortStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 9, 1)
)
if mibBuilder.loadTexts:
    asfPortStats.setStatus("current")
_AsfPortNetStatsTime_Type = Integer32
_AsfPortNetStatsTime_Object = MibScalar
asfPortNetStatsTime = _AsfPortNetStatsTime_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 9, 1, 1),
    _AsfPortNetStatsTime_Type()
)
asfPortNetStatsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asfPortNetStatsTime.setStatus("current")
_AsfPortNetStatsTable_Object = MibTable
asfPortNetStatsTable = _AsfPortNetStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 9, 1, 2)
)
if mibBuilder.loadTexts:
    asfPortNetStatsTable.setStatus("current")
_AsfPortNetStatsEntry_Object = MibTableRow
asfPortNetStatsEntry = _AsfPortNetStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 9, 1, 2, 1)
)
asfPortNetStatsEntry.setIndexNames(
    (0, "ALTEON-ASF-MIB", "asfPortCountIndex"),
)
if mibBuilder.loadTexts:
    asfPortNetStatsEntry.setStatus("current")


class _AsfPortCountIndex_Type(Integer32):
    """Custom type asfPortCountIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_AsfPortCountIndex_Type.__name__ = "Integer32"
_AsfPortCountIndex_Object = MibTableColumn
asfPortCountIndex = _AsfPortCountIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 9, 1, 2, 1, 1),
    _AsfPortCountIndex_Type()
)
asfPortCountIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asfPortCountIndex.setStatus("current")
_AsfPortInBytes_Type = Counter64
_AsfPortInBytes_Object = MibTableColumn
asfPortInBytes = _AsfPortInBytes_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 9, 1, 2, 1, 2),
    _AsfPortInBytes_Type()
)
asfPortInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asfPortInBytes.setStatus("current")
_AsfPortOutBytes_Type = Counter64
_AsfPortOutBytes_Object = MibTableColumn
asfPortOutBytes = _AsfPortOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 9, 1, 2, 1, 3),
    _AsfPortOutBytes_Type()
)
asfPortOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asfPortOutBytes.setStatus("current")
_AsfPortInPackets_Type = Counter64
_AsfPortInPackets_Object = MibTableColumn
asfPortInPackets = _AsfPortInPackets_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 9, 1, 2, 1, 4),
    _AsfPortInPackets_Type()
)
asfPortInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asfPortInPackets.setStatus("current")
_AsfPortOutPackets_Type = Counter64
_AsfPortOutPackets_Object = MibTableColumn
asfPortOutPackets = _AsfPortOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 9, 1, 2, 1, 5),
    _AsfPortOutPackets_Type()
)
asfPortOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asfPortOutPackets.setStatus("current")
_AsfPortInUcastPackets_Type = Counter64
_AsfPortInUcastPackets_Object = MibTableColumn
asfPortInUcastPackets = _AsfPortInUcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 9, 1, 2, 1, 6),
    _AsfPortInUcastPackets_Type()
)
asfPortInUcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asfPortInUcastPackets.setStatus("current")
_AsfPortOutUcastPackets_Type = Counter64
_AsfPortOutUcastPackets_Object = MibTableColumn
asfPortOutUcastPackets = _AsfPortOutUcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 9, 1, 2, 1, 7),
    _AsfPortOutUcastPackets_Type()
)
asfPortOutUcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asfPortOutUcastPackets.setStatus("current")
_AsfPortInBcastPackets_Type = Counter64
_AsfPortInBcastPackets_Object = MibTableColumn
asfPortInBcastPackets = _AsfPortInBcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 9, 1, 2, 1, 8),
    _AsfPortInBcastPackets_Type()
)
asfPortInBcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asfPortInBcastPackets.setStatus("current")
_AsfPortOutBcastPackets_Type = Counter64
_AsfPortOutBcastPackets_Object = MibTableColumn
asfPortOutBcastPackets = _AsfPortOutBcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 9, 1, 2, 1, 9),
    _AsfPortOutBcastPackets_Type()
)
asfPortOutBcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asfPortOutBcastPackets.setStatus("current")
_AsfPortInMcastPackets_Type = Counter64
_AsfPortInMcastPackets_Object = MibTableColumn
asfPortInMcastPackets = _AsfPortInMcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 9, 1, 2, 1, 10),
    _AsfPortInMcastPackets_Type()
)
asfPortInMcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asfPortInMcastPackets.setStatus("current")
_AsfPortOutMcastPackets_Type = Counter64
_AsfPortOutMcastPackets_Object = MibTableColumn
asfPortOutMcastPackets = _AsfPortOutMcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 9, 1, 2, 1, 11),
    _AsfPortOutMcastPackets_Type()
)
asfPortOutMcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asfPortOutMcastPackets.setStatus("current")
_AsfPortInDiscards_Type = Counter64
_AsfPortInDiscards_Object = MibTableColumn
asfPortInDiscards = _AsfPortInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 9, 1, 2, 1, 12),
    _AsfPortInDiscards_Type()
)
asfPortInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asfPortInDiscards.setStatus("current")
_AsfPortOutDiscards_Type = Counter64
_AsfPortOutDiscards_Object = MibTableColumn
asfPortOutDiscards = _AsfPortOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 9, 1, 2, 1, 13),
    _AsfPortOutDiscards_Type()
)
asfPortOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asfPortOutDiscards.setStatus("current")
_AsfPortInErrors_Type = Counter64
_AsfPortInErrors_Object = MibTableColumn
asfPortInErrors = _AsfPortInErrors_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 9, 1, 2, 1, 14),
    _AsfPortInErrors_Type()
)
asfPortInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asfPortInErrors.setStatus("current")
_AsfPortOutErrors_Type = Counter64
_AsfPortOutErrors_Object = MibTableColumn
asfPortOutErrors = _AsfPortOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 9, 1, 2, 1, 15),
    _AsfPortOutErrors_Type()
)
asfPortOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asfPortOutErrors.setStatus("current")
_AsfPortInUnknowns_Type = Counter64
_AsfPortInUnknowns_Object = MibTableColumn
asfPortInUnknowns = _AsfPortInUnknowns_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 9, 1, 2, 1, 16),
    _AsfPortInUnknowns_Type()
)
asfPortInUnknowns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asfPortInUnknowns.setStatus("current")
_AsfIsdStats_ObjectIdentity = ObjectIdentity
asfIsdStats = _AsfIsdStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 9, 2)
)
if mibBuilder.loadTexts:
    asfIsdStats.setStatus("current")
_AsfIsdSessStatsTime_Type = Integer32
_AsfIsdSessStatsTime_Object = MibScalar
asfIsdSessStatsTime = _AsfIsdSessStatsTime_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 9, 2, 1),
    _AsfIsdSessStatsTime_Type()
)
asfIsdSessStatsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asfIsdSessStatsTime.setStatus("current")
_AsfIsdSessStatsTable_Object = MibTable
asfIsdSessStatsTable = _AsfIsdSessStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 9, 2, 2)
)
if mibBuilder.loadTexts:
    asfIsdSessStatsTable.setStatus("current")
_AsfIsdSessStatsEntry_Object = MibTableRow
asfIsdSessStatsEntry = _AsfIsdSessStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 9, 2, 2, 1)
)
asfIsdSessStatsEntry.setIndexNames(
    (0, "ALTEON-ASF-MIB", "asfIsdCountIndex"),
)
if mibBuilder.loadTexts:
    asfIsdSessStatsEntry.setStatus("current")


class _AsfIsdCountIndex_Type(Integer32):
    """Custom type asfIsdCountIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_AsfIsdCountIndex_Type.__name__ = "Integer32"
_AsfIsdCountIndex_Object = MibTableColumn
asfIsdCountIndex = _AsfIsdCountIndex_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 9, 2, 2, 1, 1),
    _AsfIsdCountIndex_Type()
)
asfIsdCountIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asfIsdCountIndex.setStatus("current")
_AsfIsdIPAddress_Type = IpAddress
_AsfIsdIPAddress_Object = MibTableColumn
asfIsdIPAddress = _AsfIsdIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 9, 2, 2, 1, 2),
    _AsfIsdIPAddress_Type()
)
asfIsdIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asfIsdIPAddress.setStatus("current")
_AsfNoOfSessions_Type = Integer32
_AsfNoOfSessions_Object = MibTableColumn
asfNoOfSessions = _AsfNoOfSessions_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 9, 2, 2, 1, 3),
    _AsfNoOfSessions_Type()
)
asfNoOfSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asfNoOfSessions.setStatus("current")
_AsfNotifications_ObjectIdentity = ObjectIdentity
asfNotifications = _AsfNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 12)
)
if mibBuilder.loadTexts:
    asfNotifications.setStatus("current")
_AsfEvents_ObjectIdentity = ObjectIdentity
asfEvents = _AsfEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 12, 1)
)
if mibBuilder.loadTexts:
    asfEvents.setStatus("current")
_AsfAlarms_ObjectIdentity = ObjectIdentity
asfAlarms = _AsfAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 12, 2)
)
if mibBuilder.loadTexts:
    asfAlarms.setStatus("current")
_AsfNotificationObjs_ObjectIdentity = ObjectIdentity
asfNotificationObjs = _AsfNotificationObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 13)
)
if mibBuilder.loadTexts:
    asfNotificationObjs.setStatus("current")
_DeviceIpAddress_Type = IpAddress
_DeviceIpAddress_Object = MibScalar
deviceIpAddress = _DeviceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 13, 1),
    _DeviceIpAddress_Type()
)
deviceIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    deviceIpAddress.setStatus("current")
_DeviceTimeStamp_Type = TimeStamp
_DeviceTimeStamp_Object = MibScalar
deviceTimeStamp = _DeviceTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 13, 2),
    _DeviceTimeStamp_Type()
)
deviceTimeStamp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    deviceTimeStamp.setStatus("current")
_InfoString_Type = DisplayString
_InfoString_Object = MibScalar
infoString = _InfoString_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 13, 3),
    _InfoString_Type()
)
infoString.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    infoString.setStatus("current")
_MemoryUsed_Type = Unsigned32
_MemoryUsed_Object = MibScalar
memoryUsed = _MemoryUsed_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 13, 4),
    _MemoryUsed_Type()
)
memoryUsed.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    memoryUsed.setStatus("current")


class _MemoryUsageType_Type(Integer32):
    """Custom type memoryUsageType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absolute", 1),
          ("percentage", 2))
    )


_MemoryUsageType_Type.__name__ = "Integer32"
_MemoryUsageType_Object = MibScalar
memoryUsageType = _MemoryUsageType_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 13, 5),
    _MemoryUsageType_Type()
)
memoryUsageType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    memoryUsageType.setStatus("current")


class _MemoryUsageUnit_Type(Integer32):
    """Custom type memoryUsageUnit based on Integer32"""
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
        *(("gb", 3),
          ("kb", 1),
          ("mb", 2),
          ("none", 4))
    )


_MemoryUsageUnit_Type.__name__ = "Integer32"
_MemoryUsageUnit_Object = MibScalar
memoryUsageUnit = _MemoryUsageUnit_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 13, 6),
    _MemoryUsageUnit_Type()
)
memoryUsageUnit.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    memoryUsageUnit.setStatus("current")


class _AlarmSeverity_Type(Integer32):
    """Custom type alarmSeverity based on Integer32"""
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
        *(("cleared", 1),
          ("critical", 3),
          ("indeterminate", 2),
          ("major", 4),
          ("minor", 5),
          ("warning", 6))
    )


_AlarmSeverity_Type.__name__ = "Integer32"
_AlarmSeverity_Object = MibScalar
alarmSeverity = _AlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 13, 7),
    _AlarmSeverity_Type()
)
alarmSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmSeverity.setStatus("current")
_DeviceMACAddress_Type = MacAddress
_DeviceMACAddress_Object = MibScalar
deviceMACAddress = _DeviceMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 13, 8),
    _DeviceMACAddress_Type()
)
deviceMACAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    deviceMACAddress.setStatus("current")

# Managed Objects groups


# Notification objects

asfAcceleratorAddedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 12, 1, 1)
)
asfAcceleratorAddedTrap.setObjects(
    ("ALTEON-ASF-MIB", "deviceMACAddress")
)
if mibBuilder.loadTexts:
    asfAcceleratorAddedTrap.setStatus(
        "current"
    )

asfAcceleratorRemovedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 12, 1, 2)
)
asfAcceleratorRemovedTrap.setObjects(
    ("ALTEON-ASF-MIB", "deviceMACAddress")
)
if mibBuilder.loadTexts:
    asfAcceleratorRemovedTrap.setStatus(
        "current"
    )

asfExtraAcceleratorDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 12, 1, 3)
)
asfExtraAcceleratorDetected.setObjects(
    ("ALTEON-ASF-MIB", "deviceMACAddress")
)
if mibBuilder.loadTexts:
    asfExtraAcceleratorDetected.setStatus(
        "current"
    )

asfAcceleratorConnEstablished = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 12, 1, 4)
)
asfAcceleratorConnEstablished.setObjects(
    ("ALTEON-ASF-MIB", "deviceMACAddress")
)
if mibBuilder.loadTexts:
    asfAcceleratorConnEstablished.setStatus(
        "current"
    )

asfConfigUpdateSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 12, 1, 8)
)
asfConfigUpdateSuccess.setObjects(
      *(("ALTEON-ASF-MIB", "deviceIpAddress"),
        ("ALTEON-ASF-MIB", "deviceMACAddress"))
)
if mibBuilder.loadTexts:
    asfConfigUpdateSuccess.setStatus(
        "current"
    )

asfConfigUpdateFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 12, 1, 9)
)
asfConfigUpdateFail.setObjects(
      *(("ALTEON-ASF-MIB", "deviceIpAddress"),
        ("ALTEON-ASF-MIB", "deviceMACAddress"))
)
if mibBuilder.loadTexts:
    asfConfigUpdateFail.setStatus(
        "current"
    )

asfFirewallStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 12, 1, 10)
)
asfFirewallStarted.setObjects(
    ("ALTEON-ASF-MIB", "deviceIpAddress")
)
if mibBuilder.loadTexts:
    asfFirewallStarted.setStatus(
        "current"
    )

asfIsdFirewallFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 12, 2, 1)
)
asfIsdFirewallFail.setObjects(
    ("ALTEON-ASF-MIB", "deviceIpAddress")
)
if mibBuilder.loadTexts:
    asfIsdFirewallFail.setStatus(
        "current"
    )

asfWebServerFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 12, 2, 2)
)
asfWebServerFail.setObjects(
    ("ALTEON-ASF-MIB", "deviceIpAddress")
)
if mibBuilder.loadTexts:
    asfWebServerFail.setStatus(
        "current"
    )

asfWebServerStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 12, 2, 3)
)
asfWebServerStart.setObjects(
    ("ALTEON-ASF-MIB", "deviceIpAddress")
)
if mibBuilder.loadTexts:
    asfWebServerStart.setStatus(
        "current"
    )

asfFileSystemWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 12, 2, 5)
)
asfFileSystemWarning.setObjects(
      *(("ALTEON-ASF-MIB", "deviceIpAddress"),
        ("ALTEON-ASF-MIB", "infoString"),
        ("ALTEON-ASF-MIB", "memoryUsed"))
)
if mibBuilder.loadTexts:
    asfFileSystemWarning.setStatus(
        "current"
    )

asfFileSystemCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 12, 2, 6)
)
asfFileSystemCritical.setObjects(
      *(("ALTEON-ASF-MIB", "deviceIpAddress"),
        ("ALTEON-ASF-MIB", "infoString"),
        ("ALTEON-ASF-MIB", "memoryUsed"))
)
if mibBuilder.loadTexts:
    asfFileSystemCritical.setStatus(
        "current"
    )

asfMemoryWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 12, 2, 7)
)
asfMemoryWarning.setObjects(
      *(("ALTEON-ASF-MIB", "deviceIpAddress"),
        ("ALTEON-ASF-MIB", "memoryUsed"))
)
if mibBuilder.loadTexts:
    asfMemoryWarning.setStatus(
        "current"
    )

asfMemoryCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 12, 2, 8)
)
asfMemoryCritical.setObjects(
      *(("ALTEON-ASF-MIB", "deviceIpAddress"),
        ("ALTEON-ASF-MIB", "memoryUsed"))
)
if mibBuilder.loadTexts:
    asfMemoryCritical.setStatus(
        "current"
    )

asfIsdStateDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1872, 2, 3, 3, 1, 12, 2, 9)
)
asfIsdStateDown.setObjects(
    ("ALTEON-ASF-MIB", "deviceIpAddress")
)
if mibBuilder.loadTexts:
    asfIsdStateDown.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALTEON-ASF-MIB",
    **{"alteonAsfMIB": alteonAsfMIB,
       "asfStatistics": asfStatistics,
       "asfPortStats": asfPortStats,
       "asfPortNetStatsTime": asfPortNetStatsTime,
       "asfPortNetStatsTable": asfPortNetStatsTable,
       "asfPortNetStatsEntry": asfPortNetStatsEntry,
       "asfPortCountIndex": asfPortCountIndex,
       "asfPortInBytes": asfPortInBytes,
       "asfPortOutBytes": asfPortOutBytes,
       "asfPortInPackets": asfPortInPackets,
       "asfPortOutPackets": asfPortOutPackets,
       "asfPortInUcastPackets": asfPortInUcastPackets,
       "asfPortOutUcastPackets": asfPortOutUcastPackets,
       "asfPortInBcastPackets": asfPortInBcastPackets,
       "asfPortOutBcastPackets": asfPortOutBcastPackets,
       "asfPortInMcastPackets": asfPortInMcastPackets,
       "asfPortOutMcastPackets": asfPortOutMcastPackets,
       "asfPortInDiscards": asfPortInDiscards,
       "asfPortOutDiscards": asfPortOutDiscards,
       "asfPortInErrors": asfPortInErrors,
       "asfPortOutErrors": asfPortOutErrors,
       "asfPortInUnknowns": asfPortInUnknowns,
       "asfIsdStats": asfIsdStats,
       "asfIsdSessStatsTime": asfIsdSessStatsTime,
       "asfIsdSessStatsTable": asfIsdSessStatsTable,
       "asfIsdSessStatsEntry": asfIsdSessStatsEntry,
       "asfIsdCountIndex": asfIsdCountIndex,
       "asfIsdIPAddress": asfIsdIPAddress,
       "asfNoOfSessions": asfNoOfSessions,
       "asfNotifications": asfNotifications,
       "asfEvents": asfEvents,
       "asfAcceleratorAddedTrap": asfAcceleratorAddedTrap,
       "asfAcceleratorRemovedTrap": asfAcceleratorRemovedTrap,
       "asfExtraAcceleratorDetected": asfExtraAcceleratorDetected,
       "asfAcceleratorConnEstablished": asfAcceleratorConnEstablished,
       "asfConfigUpdateSuccess": asfConfigUpdateSuccess,
       "asfConfigUpdateFail": asfConfigUpdateFail,
       "asfFirewallStarted": asfFirewallStarted,
       "asfAlarms": asfAlarms,
       "asfIsdFirewallFail": asfIsdFirewallFail,
       "asfWebServerFail": asfWebServerFail,
       "asfWebServerStart": asfWebServerStart,
       "asfFileSystemWarning": asfFileSystemWarning,
       "asfFileSystemCritical": asfFileSystemCritical,
       "asfMemoryWarning": asfMemoryWarning,
       "asfMemoryCritical": asfMemoryCritical,
       "asfIsdStateDown": asfIsdStateDown,
       "asfNotificationObjs": asfNotificationObjs,
       "deviceIpAddress": deviceIpAddress,
       "deviceTimeStamp": deviceTimeStamp,
       "infoString": infoString,
       "memoryUsed": memoryUsed,
       "memoryUsageType": memoryUsageType,
       "memoryUsageUnit": memoryUsageUnit,
       "alarmSeverity": alarmSeverity,
       "deviceMACAddress": deviceMACAddress}
)
