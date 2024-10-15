# SNMP MIB module (DDN-WOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DDN-WOS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:23:28 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

wosMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1)
)
wosMIB.setRevisions(
        ("2012-01-04 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class WosSeverityLevel(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("alert", 2),
          ("critical", 3),
          ("debug", 8),
          ("emergency", 1),
          ("error", 4),
          ("informational", 7),
          ("notice", 6),
          ("warning", 5))
    )



class WosSyslogFacility(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23)
        )
    )
    namedValues = NamedValues(
        *(("auth", 4),
          ("authpriv", 10),
          ("cron", 9),
          ("daemon", 3),
          ("ftp", 11),
          ("local0", 16),
          ("local1", 17),
          ("local2", 18),
          ("local3", 19),
          ("local4", 20),
          ("local5", 21),
          ("local6", 22),
          ("local7", 23),
          ("lpr", 6),
          ("mail", 2),
          ("news", 7),
          ("syslog", 5),
          ("user", 1),
          ("uucp", 8))
    )



# MIB Managed Objects in the order of their OIDs

_Datadirect_ObjectIdentity = ObjectIdentity
datadirect = _Datadirect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6894)
)
_Wos_ObjectIdentity = ObjectIdentity
wos = _Wos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6894, 4)
)
_WosNotifications_ObjectIdentity = ObjectIdentity
wosNotifications = _WosNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 0)
)
_WosObjects_ObjectIdentity = ObjectIdentity
wosObjects = _WosObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1)
)
_WosNotificationInfo_ObjectIdentity = ObjectIdentity
wosNotificationInfo = _WosNotificationInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 1)
)
_WosTrapDesc_Type = DisplayString
_WosTrapDesc_Object = MibScalar
wosTrapDesc = _WosTrapDesc_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 1, 1),
    _WosTrapDesc_Type()
)
wosTrapDesc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wosTrapDesc.setStatus("current")
_WosTrapSeverity_Type = WosSeverityLevel
_WosTrapSeverity_Object = MibScalar
wosTrapSeverity = _WosTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 1, 2),
    _WosTrapSeverity_Type()
)
wosTrapSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wosTrapSeverity.setStatus("current")
_WosTrapType_Type = DisplayString
_WosTrapType_Object = MibScalar
wosTrapType = _WosTrapType_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 1, 3),
    _WosTrapType_Type()
)
wosTrapType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wosTrapType.setStatus("current")
_WosTrapLocation_Type = DisplayString
_WosTrapLocation_Object = MibScalar
wosTrapLocation = _WosTrapLocation_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 1, 4),
    _WosTrapLocation_Type()
)
wosTrapLocation.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wosTrapLocation.setStatus("current")
_WosStatsInfo_ObjectIdentity = ObjectIdentity
wosStatsInfo = _WosStatsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 2)
)
_WosStatsFRPS_Type = Gauge32
_WosStatsFRPS_Object = MibScalar
wosStatsFRPS = _WosStatsFRPS_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 2, 1),
    _WosStatsFRPS_Type()
)
wosStatsFRPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosStatsFRPS.setStatus("current")
if mibBuilder.loadTexts:
    wosStatsFRPS.setUnits("file reads per second")
_WosStatsFWPS_Type = Gauge32
_WosStatsFWPS_Object = MibScalar
wosStatsFWPS = _WosStatsFWPS_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 2, 2),
    _WosStatsFWPS_Type()
)
wosStatsFWPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosStatsFWPS.setStatus("current")
if mibBuilder.loadTexts:
    wosStatsFWPS.setUnits("file writes per second")
_WosStatsFDPS_Type = Gauge32
_WosStatsFDPS_Object = MibScalar
wosStatsFDPS = _WosStatsFDPS_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 2, 3),
    _WosStatsFDPS_Type()
)
wosStatsFDPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosStatsFDPS.setStatus("current")
if mibBuilder.loadTexts:
    wosStatsFDPS.setUnits("file deletes per second")
_WosStatsReadLatency_Type = Gauge32
_WosStatsReadLatency_Object = MibScalar
wosStatsReadLatency = _WosStatsReadLatency_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 2, 4),
    _WosStatsReadLatency_Type()
)
wosStatsReadLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosStatsReadLatency.setStatus("current")
if mibBuilder.loadTexts:
    wosStatsReadLatency.setUnits("milliseconds")
_WosStatsWriteLatency_Type = Gauge32
_WosStatsWriteLatency_Object = MibScalar
wosStatsWriteLatency = _WosStatsWriteLatency_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 2, 5),
    _WosStatsWriteLatency_Type()
)
wosStatsWriteLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosStatsWriteLatency.setStatus("current")
if mibBuilder.loadTexts:
    wosStatsWriteLatency.setUnits("milliseconds")
_WosStatsDeleteLatency_Type = Gauge32
_WosStatsDeleteLatency_Object = MibScalar
wosStatsDeleteLatency = _WosStatsDeleteLatency_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 2, 6),
    _WosStatsDeleteLatency_Type()
)
wosStatsDeleteLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosStatsDeleteLatency.setStatus("current")
if mibBuilder.loadTexts:
    wosStatsDeleteLatency.setUnits("milliseconds")
_WosStatsReadThroughput_Type = Gauge32
_WosStatsReadThroughput_Object = MibScalar
wosStatsReadThroughput = _WosStatsReadThroughput_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 2, 7),
    _WosStatsReadThroughput_Type()
)
wosStatsReadThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosStatsReadThroughput.setStatus("current")
if mibBuilder.loadTexts:
    wosStatsReadThroughput.setUnits("kilobytes per second")
_WosStatsWriteThroughput_Type = Gauge32
_WosStatsWriteThroughput_Object = MibScalar
wosStatsWriteThroughput = _WosStatsWriteThroughput_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 2, 8),
    _WosStatsWriteThroughput_Type()
)
wosStatsWriteThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosStatsWriteThroughput.setStatus("current")
if mibBuilder.loadTexts:
    wosStatsWriteThroughput.setUnits("kilobytes per second")
_WosStatsReadCount_Type = Counter64
_WosStatsReadCount_Object = MibScalar
wosStatsReadCount = _WosStatsReadCount_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 2, 9),
    _WosStatsReadCount_Type()
)
wosStatsReadCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosStatsReadCount.setStatus("current")
_WosStatsWriteCount_Type = Counter64
_WosStatsWriteCount_Object = MibScalar
wosStatsWriteCount = _WosStatsWriteCount_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 2, 10),
    _WosStatsWriteCount_Type()
)
wosStatsWriteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosStatsWriteCount.setStatus("current")
_WosStatsDeleteCount_Type = Counter64
_WosStatsDeleteCount_Object = MibScalar
wosStatsDeleteCount = _WosStatsDeleteCount_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 2, 11),
    _WosStatsDeleteCount_Type()
)
wosStatsDeleteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosStatsDeleteCount.setStatus("current")
_WosAlertsInfo_ObjectIdentity = ObjectIdentity
wosAlertsInfo = _WosAlertsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 3)
)
_WosAlertTable_Object = MibTable
wosAlertTable = _WosAlertTable_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    wosAlertTable.setStatus("current")
_WosAlertEntry_Object = MibTableRow
wosAlertEntry = _WosAlertEntry_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 3, 1, 1)
)
wosAlertEntry.setIndexNames(
    (0, "DDN-WOS-MIB", "wosAlertIndex"),
)
if mibBuilder.loadTexts:
    wosAlertEntry.setStatus("current")
_WosAlertIndex_Type = Unsigned32
_WosAlertIndex_Object = MibTableColumn
wosAlertIndex = _WosAlertIndex_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 3, 1, 1, 1),
    _WosAlertIndex_Type()
)
wosAlertIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wosAlertIndex.setStatus("current")
_WosAlertSeverity_Type = WosSeverityLevel
_WosAlertSeverity_Object = MibTableColumn
wosAlertSeverity = _WosAlertSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 3, 1, 1, 2),
    _WosAlertSeverity_Type()
)
wosAlertSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosAlertSeverity.setStatus("current")
_WosAlertTime_Type = DateAndTime
_WosAlertTime_Object = MibTableColumn
wosAlertTime = _WosAlertTime_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 3, 1, 1, 3),
    _WosAlertTime_Type()
)
wosAlertTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosAlertTime.setStatus("current")
_WosAlertType_Type = DisplayString
_WosAlertType_Object = MibTableColumn
wosAlertType = _WosAlertType_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 3, 1, 1, 4),
    _WosAlertType_Type()
)
wosAlertType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosAlertType.setStatus("current")
_WosAlertLocation_Type = DisplayString
_WosAlertLocation_Object = MibTableColumn
wosAlertLocation = _WosAlertLocation_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 3, 1, 1, 5),
    _WosAlertLocation_Type()
)
wosAlertLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosAlertLocation.setStatus("current")
_WosAlertDesc_Type = DisplayString
_WosAlertDesc_Object = MibTableColumn
wosAlertDesc = _WosAlertDesc_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 3, 1, 1, 6),
    _WosAlertDesc_Type()
)
wosAlertDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosAlertDesc.setStatus("current")
_WosClusterInfo_ObjectIdentity = ObjectIdentity
wosClusterInfo = _WosClusterInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 4)
)
_WosClusterName_Type = DisplayString
_WosClusterName_Object = MibScalar
wosClusterName = _WosClusterName_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 4, 1),
    _WosClusterName_Type()
)
wosClusterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosClusterName.setStatus("current")
_WosClusterId_Type = DisplayString
_WosClusterId_Object = MibScalar
wosClusterId = _WosClusterId_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 4, 2),
    _WosClusterId_Type()
)
wosClusterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosClusterId.setStatus("current")
_WosClusterStatus_Type = DisplayString
_WosClusterStatus_Object = MibScalar
wosClusterStatus = _WosClusterStatus_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 4, 3),
    _WosClusterStatus_Type()
)
wosClusterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosClusterStatus.setStatus("current")
_WosClusterPrimaryNodeAddressType_Type = InetAddressType
_WosClusterPrimaryNodeAddressType_Object = MibScalar
wosClusterPrimaryNodeAddressType = _WosClusterPrimaryNodeAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 4, 4),
    _WosClusterPrimaryNodeAddressType_Type()
)
wosClusterPrimaryNodeAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosClusterPrimaryNodeAddressType.setStatus("current")
_WosClusterPrimaryNodeAddress_Type = InetAddress
_WosClusterPrimaryNodeAddress_Object = MibScalar
wosClusterPrimaryNodeAddress = _WosClusterPrimaryNodeAddress_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 4, 5),
    _WosClusterPrimaryNodeAddress_Type()
)
wosClusterPrimaryNodeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosClusterPrimaryNodeAddress.setStatus("current")
_WosClusterTotalNodeCount_Type = Unsigned32
_WosClusterTotalNodeCount_Object = MibScalar
wosClusterTotalNodeCount = _WosClusterTotalNodeCount_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 4, 6),
    _WosClusterTotalNodeCount_Type()
)
wosClusterTotalNodeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosClusterTotalNodeCount.setStatus("current")
_WosClusterActiveNodeCount_Type = Unsigned32
_WosClusterActiveNodeCount_Object = MibScalar
wosClusterActiveNodeCount = _WosClusterActiveNodeCount_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 4, 7),
    _WosClusterActiveNodeCount_Type()
)
wosClusterActiveNodeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosClusterActiveNodeCount.setStatus("current")
_WosClusterDisconnectedNodeCount_Type = Unsigned32
_WosClusterDisconnectedNodeCount_Object = MibScalar
wosClusterDisconnectedNodeCount = _WosClusterDisconnectedNodeCount_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 4, 8),
    _WosClusterDisconnectedNodeCount_Type()
)
wosClusterDisconnectedNodeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosClusterDisconnectedNodeCount.setStatus("current")
_WosClusterConnectedClientsCount_Type = Unsigned32
_WosClusterConnectedClientsCount_Object = MibScalar
wosClusterConnectedClientsCount = _WosClusterConnectedClientsCount_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 4, 9),
    _WosClusterConnectedClientsCount_Type()
)
wosClusterConnectedClientsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosClusterConnectedClientsCount.setStatus("current")
_WosClusterObjectCountLow_Type = Unsigned32
_WosClusterObjectCountLow_Object = MibScalar
wosClusterObjectCountLow = _WosClusterObjectCountLow_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 4, 10),
    _WosClusterObjectCountLow_Type()
)
wosClusterObjectCountLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosClusterObjectCountLow.setStatus("current")
_WosClusterObjectCountHigh_Type = Unsigned32
_WosClusterObjectCountHigh_Object = MibScalar
wosClusterObjectCountHigh = _WosClusterObjectCountHigh_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 4, 11),
    _WosClusterObjectCountHigh_Type()
)
wosClusterObjectCountHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosClusterObjectCountHigh.setStatus("current")
_WosClusterUsableCapacity_Type = Unsigned32
_WosClusterUsableCapacity_Object = MibScalar
wosClusterUsableCapacity = _WosClusterUsableCapacity_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 4, 12),
    _WosClusterUsableCapacity_Type()
)
wosClusterUsableCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosClusterUsableCapacity.setStatus("current")
if mibBuilder.loadTexts:
    wosClusterUsableCapacity.setUnits("gigabytes")
_WosClusterUsedCapacity_Type = Unsigned32
_WosClusterUsedCapacity_Object = MibScalar
wosClusterUsedCapacity = _WosClusterUsedCapacity_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 4, 13),
    _WosClusterUsedCapacity_Type()
)
wosClusterUsedCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosClusterUsedCapacity.setStatus("current")
if mibBuilder.loadTexts:
    wosClusterUsedCapacity.setUnits("gigabytes")
_WosClusterFreeCapacity_Type = Unsigned32
_WosClusterFreeCapacity_Object = MibScalar
wosClusterFreeCapacity = _WosClusterFreeCapacity_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 4, 14),
    _WosClusterFreeCapacity_Type()
)
wosClusterFreeCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosClusterFreeCapacity.setStatus("current")
if mibBuilder.loadTexts:
    wosClusterFreeCapacity.setUnits("gigabytes")
_WosZonesInfo_ObjectIdentity = ObjectIdentity
wosZonesInfo = _WosZonesInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 5)
)
_WosZoneTable_Object = MibTable
wosZoneTable = _WosZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    wosZoneTable.setStatus("current")
_WosZoneEntry_Object = MibTableRow
wosZoneEntry = _WosZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 5, 1, 1)
)
wosZoneEntry.setIndexNames(
    (0, "DDN-WOS-MIB", "wosZoneId"),
)
if mibBuilder.loadTexts:
    wosZoneEntry.setStatus("current")
_WosZoneId_Type = Unsigned32
_WosZoneId_Object = MibTableColumn
wosZoneId = _WosZoneId_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 5, 1, 1, 1),
    _WosZoneId_Type()
)
wosZoneId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wosZoneId.setStatus("current")
_WosZoneName_Type = DisplayString
_WosZoneName_Object = MibTableColumn
wosZoneName = _WosZoneName_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 5, 1, 1, 2),
    _WosZoneName_Type()
)
wosZoneName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosZoneName.setStatus("current")
_WosZoneNodeCount_Type = Unsigned32
_WosZoneNodeCount_Object = MibTableColumn
wosZoneNodeCount = _WosZoneNodeCount_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 5, 1, 1, 3),
    _WosZoneNodeCount_Type()
)
wosZoneNodeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosZoneNodeCount.setStatus("current")
_WosNodesInfo_ObjectIdentity = ObjectIdentity
wosNodesInfo = _WosNodesInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 6)
)
_WosNodeTable_Object = MibTable
wosNodeTable = _WosNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    wosNodeTable.setStatus("current")
_WosNodeEntry_Object = MibTableRow
wosNodeEntry = _WosNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 6, 1, 1)
)
wosNodeEntry.setIndexNames(
    (0, "DDN-WOS-MIB", "wosZoneId"),
    (0, "DDN-WOS-MIB", "wosNodeIndex"),
)
if mibBuilder.loadTexts:
    wosNodeEntry.setStatus("current")
_WosNodeIndex_Type = Unsigned32
_WosNodeIndex_Object = MibTableColumn
wosNodeIndex = _WosNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 6, 1, 1, 1),
    _WosNodeIndex_Type()
)
wosNodeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wosNodeIndex.setStatus("current")
_WosNodeName_Type = DisplayString
_WosNodeName_Object = MibTableColumn
wosNodeName = _WosNodeName_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 6, 1, 1, 2),
    _WosNodeName_Type()
)
wosNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosNodeName.setStatus("current")
_WosNodeAddressType_Type = InetAddressType
_WosNodeAddressType_Object = MibTableColumn
wosNodeAddressType = _WosNodeAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 6, 1, 1, 3),
    _WosNodeAddressType_Type()
)
wosNodeAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosNodeAddressType.setStatus("current")
_WosNodeAddress_Type = InetAddress
_WosNodeAddress_Object = MibTableColumn
wosNodeAddress = _WosNodeAddress_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 6, 1, 1, 4),
    _WosNodeAddress_Type()
)
wosNodeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosNodeAddress.setStatus("current")
_WosNodeZoneName_Type = DisplayString
_WosNodeZoneName_Object = MibTableColumn
wosNodeZoneName = _WosNodeZoneName_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 6, 1, 1, 5),
    _WosNodeZoneName_Type()
)
wosNodeZoneName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosNodeZoneName.setStatus("current")
_WosNodeStatus_Type = DisplayString
_WosNodeStatus_Object = MibTableColumn
wosNodeStatus = _WosNodeStatus_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 6, 1, 1, 6),
    _WosNodeStatus_Type()
)
wosNodeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosNodeStatus.setStatus("current")
_WosNodeFwVersion_Type = DisplayString
_WosNodeFwVersion_Object = MibTableColumn
wosNodeFwVersion = _WosNodeFwVersion_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 6, 1, 1, 7),
    _WosNodeFwVersion_Type()
)
wosNodeFwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosNodeFwVersion.setStatus("current")
_WosNodeObjectCountLow_Type = Unsigned32
_WosNodeObjectCountLow_Object = MibTableColumn
wosNodeObjectCountLow = _WosNodeObjectCountLow_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 6, 1, 1, 8),
    _WosNodeObjectCountLow_Type()
)
wosNodeObjectCountLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosNodeObjectCountLow.setStatus("current")
_WosNodeObjectCountHigh_Type = Unsigned32
_WosNodeObjectCountHigh_Object = MibTableColumn
wosNodeObjectCountHigh = _WosNodeObjectCountHigh_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 6, 1, 1, 9),
    _WosNodeObjectCountHigh_Type()
)
wosNodeObjectCountHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosNodeObjectCountHigh.setStatus("current")
_WosNodeTotalCapacity_Type = Unsigned32
_WosNodeTotalCapacity_Object = MibTableColumn
wosNodeTotalCapacity = _WosNodeTotalCapacity_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 6, 1, 1, 10),
    _WosNodeTotalCapacity_Type()
)
wosNodeTotalCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosNodeTotalCapacity.setStatus("current")
if mibBuilder.loadTexts:
    wosNodeTotalCapacity.setUnits("gigabytes")
_WosNodeUsedCapacity_Type = Unsigned32
_WosNodeUsedCapacity_Object = MibTableColumn
wosNodeUsedCapacity = _WosNodeUsedCapacity_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 6, 1, 1, 11),
    _WosNodeUsedCapacity_Type()
)
wosNodeUsedCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosNodeUsedCapacity.setStatus("current")
if mibBuilder.loadTexts:
    wosNodeUsedCapacity.setUnits("gigabytes")


class _WosNodePercentFull_Type(Gauge32):
    """Custom type wosNodePercentFull based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_WosNodePercentFull_Type.__name__ = "Gauge32"
_WosNodePercentFull_Object = MibTableColumn
wosNodePercentFull = _WosNodePercentFull_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 6, 1, 1, 12),
    _WosNodePercentFull_Type()
)
wosNodePercentFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosNodePercentFull.setStatus("current")
_WosPendingNodeTable_Object = MibTable
wosPendingNodeTable = _WosPendingNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 6, 2)
)
if mibBuilder.loadTexts:
    wosPendingNodeTable.setStatus("current")
_WosPendingNodeEntry_Object = MibTableRow
wosPendingNodeEntry = _WosPendingNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 6, 2, 1)
)
wosPendingNodeEntry.setIndexNames(
    (0, "DDN-WOS-MIB", "wosPendingNodeIndex"),
)
if mibBuilder.loadTexts:
    wosPendingNodeEntry.setStatus("current")
_WosPendingNodeIndex_Type = Unsigned32
_WosPendingNodeIndex_Object = MibTableColumn
wosPendingNodeIndex = _WosPendingNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 6, 2, 1, 1),
    _WosPendingNodeIndex_Type()
)
wosPendingNodeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wosPendingNodeIndex.setStatus("current")
_WosPendingNodeAddressType_Type = InetAddressType
_WosPendingNodeAddressType_Object = MibTableColumn
wosPendingNodeAddressType = _WosPendingNodeAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 6, 2, 1, 2),
    _WosPendingNodeAddressType_Type()
)
wosPendingNodeAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosPendingNodeAddressType.setStatus("current")
_WosPendingNodeAddress_Type = InetAddress
_WosPendingNodeAddress_Object = MibTableColumn
wosPendingNodeAddress = _WosPendingNodeAddress_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 6, 2, 1, 3),
    _WosPendingNodeAddress_Type()
)
wosPendingNodeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosPendingNodeAddress.setStatus("current")
_WosPendingNodeStatus_Type = DisplayString
_WosPendingNodeStatus_Object = MibTableColumn
wosPendingNodeStatus = _WosPendingNodeStatus_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 6, 2, 1, 4),
    _WosPendingNodeStatus_Type()
)
wosPendingNodeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosPendingNodeStatus.setStatus("current")
_WosNodeDriveTable_Object = MibTable
wosNodeDriveTable = _WosNodeDriveTable_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 6, 3)
)
if mibBuilder.loadTexts:
    wosNodeDriveTable.setStatus("current")
_WosNodeDriveEntry_Object = MibTableRow
wosNodeDriveEntry = _WosNodeDriveEntry_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 6, 3, 1)
)
wosNodeDriveEntry.setIndexNames(
    (0, "DDN-WOS-MIB", "wosNodeAddressType"),
    (0, "DDN-WOS-MIB", "wosNodeAddress"),
    (0, "DDN-WOS-MIB", "wosNodeDriveSlotNbr"),
)
if mibBuilder.loadTexts:
    wosNodeDriveEntry.setStatus("current")
_WosNodeDriveSlotNbr_Type = Unsigned32
_WosNodeDriveSlotNbr_Object = MibTableColumn
wosNodeDriveSlotNbr = _WosNodeDriveSlotNbr_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 6, 3, 1, 1),
    _WosNodeDriveSlotNbr_Type()
)
wosNodeDriveSlotNbr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wosNodeDriveSlotNbr.setStatus("current")
_WosNodeDriveNodeName_Type = DisplayString
_WosNodeDriveNodeName_Object = MibTableColumn
wosNodeDriveNodeName = _WosNodeDriveNodeName_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 6, 3, 1, 2),
    _WosNodeDriveNodeName_Type()
)
wosNodeDriveNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosNodeDriveNodeName.setStatus("current")
_WosNodeDriveMfgr_Type = DisplayString
_WosNodeDriveMfgr_Object = MibTableColumn
wosNodeDriveMfgr = _WosNodeDriveMfgr_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 6, 3, 1, 3),
    _WosNodeDriveMfgr_Type()
)
wosNodeDriveMfgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosNodeDriveMfgr.setStatus("current")
_WosNodeDriveModel_Type = DisplayString
_WosNodeDriveModel_Object = MibTableColumn
wosNodeDriveModel = _WosNodeDriveModel_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 6, 3, 1, 4),
    _WosNodeDriveModel_Type()
)
wosNodeDriveModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosNodeDriveModel.setStatus("current")
_WosNodeDriveSerialNbr_Type = DisplayString
_WosNodeDriveSerialNbr_Object = MibTableColumn
wosNodeDriveSerialNbr = _WosNodeDriveSerialNbr_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 6, 3, 1, 5),
    _WosNodeDriveSerialNbr_Type()
)
wosNodeDriveSerialNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosNodeDriveSerialNbr.setStatus("current")
_WosNodeDriveStatus_Type = DisplayString
_WosNodeDriveStatus_Object = MibTableColumn
wosNodeDriveStatus = _WosNodeDriveStatus_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 6, 3, 1, 6),
    _WosNodeDriveStatus_Type()
)
wosNodeDriveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosNodeDriveStatus.setStatus("current")
_WosNodeDriveCapacity_Type = Unsigned32
_WosNodeDriveCapacity_Object = MibTableColumn
wosNodeDriveCapacity = _WosNodeDriveCapacity_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 6, 3, 1, 7),
    _WosNodeDriveCapacity_Type()
)
wosNodeDriveCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosNodeDriveCapacity.setStatus("current")
if mibBuilder.loadTexts:
    wosNodeDriveCapacity.setUnits("gigabytes")
_WosPoliciesInfo_ObjectIdentity = ObjectIdentity
wosPoliciesInfo = _WosPoliciesInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 7)
)
_WosPolicyTable_Object = MibTable
wosPolicyTable = _WosPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 7, 1)
)
if mibBuilder.loadTexts:
    wosPolicyTable.setStatus("current")
_WosPolicyEntry_Object = MibTableRow
wosPolicyEntry = _WosPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 7, 1, 1)
)
wosPolicyEntry.setIndexNames(
    (0, "DDN-WOS-MIB", "wosPolicyIndex"),
    (0, "DDN-WOS-MIB", "wosPolicyReplicaIndex"),
)
if mibBuilder.loadTexts:
    wosPolicyEntry.setStatus("current")
_WosPolicyIndex_Type = Unsigned32
_WosPolicyIndex_Object = MibTableColumn
wosPolicyIndex = _WosPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 7, 1, 1, 1),
    _WosPolicyIndex_Type()
)
wosPolicyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wosPolicyIndex.setStatus("current")
_WosPolicyReplicaIndex_Type = Unsigned32
_WosPolicyReplicaIndex_Object = MibTableColumn
wosPolicyReplicaIndex = _WosPolicyReplicaIndex_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 7, 1, 1, 2),
    _WosPolicyReplicaIndex_Type()
)
wosPolicyReplicaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wosPolicyReplicaIndex.setStatus("current")
_WosPolicyId_Type = DisplayString
_WosPolicyId_Object = MibTableColumn
wosPolicyId = _WosPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 7, 1, 1, 3),
    _WosPolicyId_Type()
)
wosPolicyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosPolicyId.setStatus("current")
_WosPolicyName_Type = DisplayString
_WosPolicyName_Object = MibTableColumn
wosPolicyName = _WosPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 7, 1, 1, 4),
    _WosPolicyName_Type()
)
wosPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosPolicyName.setStatus("current")
_WosPolicyReplicaZoneName_Type = DisplayString
_WosPolicyReplicaZoneName_Object = MibTableColumn
wosPolicyReplicaZoneName = _WosPolicyReplicaZoneName_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 7, 1, 1, 5),
    _WosPolicyReplicaZoneName_Type()
)
wosPolicyReplicaZoneName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosPolicyReplicaZoneName.setStatus("current")
_WosPolicyReplicaCount_Type = Unsigned32
_WosPolicyReplicaCount_Object = MibTableColumn
wosPolicyReplicaCount = _WosPolicyReplicaCount_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 7, 1, 1, 6),
    _WosPolicyReplicaCount_Type()
)
wosPolicyReplicaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosPolicyReplicaCount.setStatus("current")
_WosPolicyReplicationType_Type = DisplayString
_WosPolicyReplicationType_Object = MibTableColumn
wosPolicyReplicationType = _WosPolicyReplicationType_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 7, 1, 1, 7),
    _WosPolicyReplicationType_Type()
)
wosPolicyReplicationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosPolicyReplicationType.setStatus("current")
_WosPolicyLocalDataProtection_Type = TruthValue
_WosPolicyLocalDataProtection_Object = MibTableColumn
wosPolicyLocalDataProtection = _WosPolicyLocalDataProtection_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 7, 1, 1, 8),
    _WosPolicyLocalDataProtection_Type()
)
wosPolicyLocalDataProtection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosPolicyLocalDataProtection.setStatus("current")
_WosPolicyObjCountLow_Type = Unsigned32
_WosPolicyObjCountLow_Object = MibTableColumn
wosPolicyObjCountLow = _WosPolicyObjCountLow_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 7, 1, 1, 9),
    _WosPolicyObjCountLow_Type()
)
wosPolicyObjCountLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosPolicyObjCountLow.setStatus("current")
_WosPolicyObjCountHigh_Type = Unsigned32
_WosPolicyObjCountHigh_Object = MibTableColumn
wosPolicyObjCountHigh = _WosPolicyObjCountHigh_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 7, 1, 1, 10),
    _WosPolicyObjCountHigh_Type()
)
wosPolicyObjCountHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosPolicyObjCountHigh.setStatus("current")
_WosPolicyNonComplObjCountLow_Type = Unsigned32
_WosPolicyNonComplObjCountLow_Object = MibTableColumn
wosPolicyNonComplObjCountLow = _WosPolicyNonComplObjCountLow_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 7, 1, 1, 11),
    _WosPolicyNonComplObjCountLow_Type()
)
wosPolicyNonComplObjCountLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosPolicyNonComplObjCountLow.setStatus("current")
_WosPolicyNonComplObjCountHigh_Type = Unsigned32
_WosPolicyNonComplObjCountHigh_Object = MibTableColumn
wosPolicyNonComplObjCountHigh = _WosPolicyNonComplObjCountHigh_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 7, 1, 1, 12),
    _WosPolicyNonComplObjCountHigh_Type()
)
wosPolicyNonComplObjCountHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosPolicyNonComplObjCountHigh.setStatus("current")
_WosPolicyUsedCapacity_Type = Unsigned32
_WosPolicyUsedCapacity_Object = MibTableColumn
wosPolicyUsedCapacity = _WosPolicyUsedCapacity_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 7, 1, 1, 13),
    _WosPolicyUsedCapacity_Type()
)
wosPolicyUsedCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosPolicyUsedCapacity.setStatus("current")
if mibBuilder.loadTexts:
    wosPolicyUsedCapacity.setUnits("gigabytes")
_WosPrefsInfo_ObjectIdentity = ObjectIdentity
wosPrefsInfo = _WosPrefsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 8)
)
_WosPrefStoreUnderReplObjs_Type = TruthValue
_WosPrefStoreUnderReplObjs_Object = MibScalar
wosPrefStoreUnderReplObjs = _WosPrefStoreUnderReplObjs_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 8, 1),
    _WosPrefStoreUnderReplObjs_Type()
)
wosPrefStoreUnderReplObjs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosPrefStoreUnderReplObjs.setStatus("current")
_WosPrefNodeDownDelay_Type = Unsigned32
_WosPrefNodeDownDelay_Object = MibScalar
wosPrefNodeDownDelay = _WosPrefNodeDownDelay_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 8, 2),
    _WosPrefNodeDownDelay_Type()
)
wosPrefNodeDownDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosPrefNodeDownDelay.setStatus("current")
if mibBuilder.loadTexts:
    wosPrefNodeDownDelay.setUnits("minutes")
_WosPrefEmailAlertNewInterval_Type = Unsigned32
_WosPrefEmailAlertNewInterval_Object = MibScalar
wosPrefEmailAlertNewInterval = _WosPrefEmailAlertNewInterval_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 8, 3),
    _WosPrefEmailAlertNewInterval_Type()
)
wosPrefEmailAlertNewInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosPrefEmailAlertNewInterval.setStatus("current")
if mibBuilder.loadTexts:
    wosPrefEmailAlertNewInterval.setUnits("minutes")
_WosPrefEmailAlertRmndrInterval_Type = Unsigned32
_WosPrefEmailAlertRmndrInterval_Object = MibScalar
wosPrefEmailAlertRmndrInterval = _WosPrefEmailAlertRmndrInterval_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 8, 4),
    _WosPrefEmailAlertRmndrInterval_Type()
)
wosPrefEmailAlertRmndrInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosPrefEmailAlertRmndrInterval.setStatus("current")
if mibBuilder.loadTexts:
    wosPrefEmailAlertRmndrInterval.setUnits("minutes")
_WosPrefEmailAlertFromAddr_Type = DisplayString
_WosPrefEmailAlertFromAddr_Object = MibScalar
wosPrefEmailAlertFromAddr = _WosPrefEmailAlertFromAddr_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 8, 5),
    _WosPrefEmailAlertFromAddr_Type()
)
wosPrefEmailAlertFromAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosPrefEmailAlertFromAddr.setStatus("current")
_WosPrefEmailAlertRecipientTable_Object = MibTable
wosPrefEmailAlertRecipientTable = _WosPrefEmailAlertRecipientTable_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 8, 6)
)
if mibBuilder.loadTexts:
    wosPrefEmailAlertRecipientTable.setStatus("current")
_WosPrefEmailAlertRecipientEntry_Object = MibTableRow
wosPrefEmailAlertRecipientEntry = _WosPrefEmailAlertRecipientEntry_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 8, 6, 1)
)
wosPrefEmailAlertRecipientEntry.setIndexNames(
    (0, "DDN-WOS-MIB", "wosPrefEmailAlertRecipientIndex"),
)
if mibBuilder.loadTexts:
    wosPrefEmailAlertRecipientEntry.setStatus("current")
_WosPrefEmailAlertRecipientIndex_Type = Unsigned32
_WosPrefEmailAlertRecipientIndex_Object = MibTableColumn
wosPrefEmailAlertRecipientIndex = _WosPrefEmailAlertRecipientIndex_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 8, 6, 1, 1),
    _WosPrefEmailAlertRecipientIndex_Type()
)
wosPrefEmailAlertRecipientIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wosPrefEmailAlertRecipientIndex.setStatus("current")
_WosPrefEmailAlertRecipient_Type = DisplayString
_WosPrefEmailAlertRecipient_Object = MibTableColumn
wosPrefEmailAlertRecipient = _WosPrefEmailAlertRecipient_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 8, 6, 1, 2),
    _WosPrefEmailAlertRecipient_Type()
)
wosPrefEmailAlertRecipient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosPrefEmailAlertRecipient.setStatus("current")
_WosPrefEmailAlertServerTable_Object = MibTable
wosPrefEmailAlertServerTable = _WosPrefEmailAlertServerTable_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 8, 7)
)
if mibBuilder.loadTexts:
    wosPrefEmailAlertServerTable.setStatus("current")
_WosPrefEmailAlertServerEntry_Object = MibTableRow
wosPrefEmailAlertServerEntry = _WosPrefEmailAlertServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 8, 7, 1)
)
wosPrefEmailAlertServerEntry.setIndexNames(
    (0, "DDN-WOS-MIB", "wosPrefEmailAlertServerIndex"),
)
if mibBuilder.loadTexts:
    wosPrefEmailAlertServerEntry.setStatus("current")
_WosPrefEmailAlertServerIndex_Type = Unsigned32
_WosPrefEmailAlertServerIndex_Object = MibTableColumn
wosPrefEmailAlertServerIndex = _WosPrefEmailAlertServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 8, 7, 1, 1),
    _WosPrefEmailAlertServerIndex_Type()
)
wosPrefEmailAlertServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wosPrefEmailAlertServerIndex.setStatus("current")
_WosPrefEmailAlertServer_Type = DisplayString
_WosPrefEmailAlertServer_Object = MibTableColumn
wosPrefEmailAlertServer = _WosPrefEmailAlertServer_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 8, 7, 1, 2),
    _WosPrefEmailAlertServer_Type()
)
wosPrefEmailAlertServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosPrefEmailAlertServer.setStatus("current")
_WosPrefSnmpManagerTable_Object = MibTable
wosPrefSnmpManagerTable = _WosPrefSnmpManagerTable_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 8, 8)
)
if mibBuilder.loadTexts:
    wosPrefSnmpManagerTable.setStatus("current")
_WosPrefSnmpManagerEntry_Object = MibTableRow
wosPrefSnmpManagerEntry = _WosPrefSnmpManagerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 8, 8, 1)
)
wosPrefSnmpManagerEntry.setIndexNames(
    (0, "DDN-WOS-MIB", "wosPrefSnmpManagerIndex"),
)
if mibBuilder.loadTexts:
    wosPrefSnmpManagerEntry.setStatus("current")
_WosPrefSnmpManagerIndex_Type = Unsigned32
_WosPrefSnmpManagerIndex_Object = MibTableColumn
wosPrefSnmpManagerIndex = _WosPrefSnmpManagerIndex_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 8, 8, 1, 1),
    _WosPrefSnmpManagerIndex_Type()
)
wosPrefSnmpManagerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wosPrefSnmpManagerIndex.setStatus("current")
_WosPrefSnmpManager_Type = DisplayString
_WosPrefSnmpManager_Object = MibTableColumn
wosPrefSnmpManager = _WosPrefSnmpManager_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 8, 8, 1, 2),
    _WosPrefSnmpManager_Type()
)
wosPrefSnmpManager.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosPrefSnmpManager.setStatus("current")
_WosPrefSnmpTrapCommunityName_Type = DisplayString
_WosPrefSnmpTrapCommunityName_Object = MibScalar
wosPrefSnmpTrapCommunityName = _WosPrefSnmpTrapCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 8, 9),
    _WosPrefSnmpTrapCommunityName_Type()
)
wosPrefSnmpTrapCommunityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosPrefSnmpTrapCommunityName.setStatus("current")
_WosPrefMgmtIpFilterTable_Object = MibTable
wosPrefMgmtIpFilterTable = _WosPrefMgmtIpFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 8, 10)
)
if mibBuilder.loadTexts:
    wosPrefMgmtIpFilterTable.setStatus("current")
_WosPrefMgmtIpFilterEntry_Object = MibTableRow
wosPrefMgmtIpFilterEntry = _WosPrefMgmtIpFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 8, 10, 1)
)
wosPrefMgmtIpFilterEntry.setIndexNames(
    (0, "DDN-WOS-MIB", "wosPrefMgmtIpFilterIndex"),
)
if mibBuilder.loadTexts:
    wosPrefMgmtIpFilterEntry.setStatus("current")
_WosPrefMgmtIpFilterIndex_Type = Unsigned32
_WosPrefMgmtIpFilterIndex_Object = MibTableColumn
wosPrefMgmtIpFilterIndex = _WosPrefMgmtIpFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 8, 10, 1, 1),
    _WosPrefMgmtIpFilterIndex_Type()
)
wosPrefMgmtIpFilterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wosPrefMgmtIpFilterIndex.setStatus("current")
_WosPrefMgmtIpFilter_Type = DisplayString
_WosPrefMgmtIpFilter_Object = MibTableColumn
wosPrefMgmtIpFilter = _WosPrefMgmtIpFilter_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 8, 10, 1, 2),
    _WosPrefMgmtIpFilter_Type()
)
wosPrefMgmtIpFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosPrefMgmtIpFilter.setStatus("current")
_WosPrefClientIpFilterTable_Object = MibTable
wosPrefClientIpFilterTable = _WosPrefClientIpFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 8, 11)
)
if mibBuilder.loadTexts:
    wosPrefClientIpFilterTable.setStatus("current")
_WosPrefClientIpFilterEntry_Object = MibTableRow
wosPrefClientIpFilterEntry = _WosPrefClientIpFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 8, 11, 1)
)
wosPrefClientIpFilterEntry.setIndexNames(
    (0, "DDN-WOS-MIB", "wosPrefClientIpFilterIndex"),
)
if mibBuilder.loadTexts:
    wosPrefClientIpFilterEntry.setStatus("current")
_WosPrefClientIpFilterIndex_Type = Unsigned32
_WosPrefClientIpFilterIndex_Object = MibTableColumn
wosPrefClientIpFilterIndex = _WosPrefClientIpFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 8, 11, 1, 1),
    _WosPrefClientIpFilterIndex_Type()
)
wosPrefClientIpFilterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wosPrefClientIpFilterIndex.setStatus("current")
_WosPrefClientIpFilter_Type = DisplayString
_WosPrefClientIpFilter_Object = MibTableColumn
wosPrefClientIpFilter = _WosPrefClientIpFilter_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 8, 11, 1, 2),
    _WosPrefClientIpFilter_Type()
)
wosPrefClientIpFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosPrefClientIpFilter.setStatus("current")
_WosPrefSyslogFacility_Type = WosSyslogFacility
_WosPrefSyslogFacility_Object = MibScalar
wosPrefSyslogFacility = _WosPrefSyslogFacility_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 8, 12),
    _WosPrefSyslogFacility_Type()
)
wosPrefSyslogFacility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosPrefSyslogFacility.setStatus("current")
_WosPrefSyslogRemoteHost_Type = DisplayString
_WosPrefSyslogRemoteHost_Object = MibScalar
wosPrefSyslogRemoteHost = _WosPrefSyslogRemoteHost_Object(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 1, 8, 13),
    _WosPrefSyslogRemoteHost_Type()
)
wosPrefSyslogRemoteHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wosPrefSyslogRemoteHost.setStatus("current")
_WosConformance_ObjectIdentity = ObjectIdentity
wosConformance = _WosConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 2)
)
_WosCompliances_ObjectIdentity = ObjectIdentity
wosCompliances = _WosCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 2, 1)
)
_WosGroups_ObjectIdentity = ObjectIdentity
wosGroups = _WosGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 2, 2)
)

# Managed Objects groups

wosNotificationsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 2, 2, 2)
)
wosNotificationsGroup.setObjects(
      *(("DDN-WOS-MIB", "wosTrapDesc"),
        ("DDN-WOS-MIB", "wosTrapSeverity"),
        ("DDN-WOS-MIB", "wosTrapType"),
        ("DDN-WOS-MIB", "wosTrapLocation"))
)
if mibBuilder.loadTexts:
    wosNotificationsGroup.setStatus("current")

wosStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 2, 2, 3)
)
wosStatsGroup.setObjects(
      *(("DDN-WOS-MIB", "wosStatsFRPS"),
        ("DDN-WOS-MIB", "wosStatsFWPS"),
        ("DDN-WOS-MIB", "wosStatsFDPS"),
        ("DDN-WOS-MIB", "wosStatsReadLatency"),
        ("DDN-WOS-MIB", "wosStatsWriteLatency"),
        ("DDN-WOS-MIB", "wosStatsDeleteLatency"),
        ("DDN-WOS-MIB", "wosStatsReadThroughput"),
        ("DDN-WOS-MIB", "wosStatsWriteThroughput"),
        ("DDN-WOS-MIB", "wosStatsReadCount"),
        ("DDN-WOS-MIB", "wosStatsWriteCount"),
        ("DDN-WOS-MIB", "wosStatsDeleteCount"))
)
if mibBuilder.loadTexts:
    wosStatsGroup.setStatus("current")

wosAlertsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 2, 2, 4)
)
wosAlertsGroup.setObjects(
      *(("DDN-WOS-MIB", "wosAlertSeverity"),
        ("DDN-WOS-MIB", "wosAlertTime"),
        ("DDN-WOS-MIB", "wosAlertType"),
        ("DDN-WOS-MIB", "wosAlertLocation"),
        ("DDN-WOS-MIB", "wosAlertDesc"))
)
if mibBuilder.loadTexts:
    wosAlertsGroup.setStatus("current")

wosClusterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 2, 2, 5)
)
wosClusterGroup.setObjects(
      *(("DDN-WOS-MIB", "wosClusterName"),
        ("DDN-WOS-MIB", "wosClusterId"),
        ("DDN-WOS-MIB", "wosClusterStatus"),
        ("DDN-WOS-MIB", "wosClusterPrimaryNodeAddressType"),
        ("DDN-WOS-MIB", "wosClusterPrimaryNodeAddress"),
        ("DDN-WOS-MIB", "wosClusterTotalNodeCount"),
        ("DDN-WOS-MIB", "wosClusterActiveNodeCount"),
        ("DDN-WOS-MIB", "wosClusterDisconnectedNodeCount"),
        ("DDN-WOS-MIB", "wosClusterConnectedClientsCount"),
        ("DDN-WOS-MIB", "wosClusterObjectCountLow"),
        ("DDN-WOS-MIB", "wosClusterObjectCountHigh"),
        ("DDN-WOS-MIB", "wosClusterUsableCapacity"),
        ("DDN-WOS-MIB", "wosClusterUsedCapacity"),
        ("DDN-WOS-MIB", "wosClusterFreeCapacity"))
)
if mibBuilder.loadTexts:
    wosClusterGroup.setStatus("current")

wosZonesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 2, 2, 6)
)
wosZonesGroup.setObjects(
      *(("DDN-WOS-MIB", "wosZoneName"),
        ("DDN-WOS-MIB", "wosZoneNodeCount"))
)
if mibBuilder.loadTexts:
    wosZonesGroup.setStatus("current")

wosNodesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 2, 2, 7)
)
wosNodesGroup.setObjects(
      *(("DDN-WOS-MIB", "wosNodeName"),
        ("DDN-WOS-MIB", "wosNodeAddressType"),
        ("DDN-WOS-MIB", "wosNodeAddress"),
        ("DDN-WOS-MIB", "wosNodeZoneName"),
        ("DDN-WOS-MIB", "wosNodeStatus"),
        ("DDN-WOS-MIB", "wosNodeFwVersion"),
        ("DDN-WOS-MIB", "wosNodeObjectCountLow"),
        ("DDN-WOS-MIB", "wosNodeObjectCountHigh"),
        ("DDN-WOS-MIB", "wosNodeTotalCapacity"),
        ("DDN-WOS-MIB", "wosNodeUsedCapacity"),
        ("DDN-WOS-MIB", "wosNodePercentFull"),
        ("DDN-WOS-MIB", "wosPendingNodeAddressType"),
        ("DDN-WOS-MIB", "wosPendingNodeAddress"),
        ("DDN-WOS-MIB", "wosPendingNodeStatus"),
        ("DDN-WOS-MIB", "wosNodeDriveNodeName"),
        ("DDN-WOS-MIB", "wosNodeDriveMfgr"),
        ("DDN-WOS-MIB", "wosNodeDriveModel"),
        ("DDN-WOS-MIB", "wosNodeDriveSerialNbr"),
        ("DDN-WOS-MIB", "wosNodeDriveStatus"),
        ("DDN-WOS-MIB", "wosNodeDriveCapacity"))
)
if mibBuilder.loadTexts:
    wosNodesGroup.setStatus("current")

wosPoliciesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 2, 2, 8)
)
wosPoliciesGroup.setObjects(
      *(("DDN-WOS-MIB", "wosPolicyId"),
        ("DDN-WOS-MIB", "wosPolicyName"),
        ("DDN-WOS-MIB", "wosPolicyReplicaZoneName"),
        ("DDN-WOS-MIB", "wosPolicyReplicaCount"),
        ("DDN-WOS-MIB", "wosPolicyReplicationType"),
        ("DDN-WOS-MIB", "wosPolicyLocalDataProtection"),
        ("DDN-WOS-MIB", "wosPolicyObjCountLow"),
        ("DDN-WOS-MIB", "wosPolicyObjCountHigh"),
        ("DDN-WOS-MIB", "wosPolicyNonComplObjCountLow"),
        ("DDN-WOS-MIB", "wosPolicyNonComplObjCountHigh"),
        ("DDN-WOS-MIB", "wosPolicyUsedCapacity"))
)
if mibBuilder.loadTexts:
    wosPoliciesGroup.setStatus("current")

wosPrefsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 2, 2, 9)
)
wosPrefsGroup.setObjects(
      *(("DDN-WOS-MIB", "wosPrefStoreUnderReplObjs"),
        ("DDN-WOS-MIB", "wosPrefNodeDownDelay"),
        ("DDN-WOS-MIB", "wosPrefEmailAlertNewInterval"),
        ("DDN-WOS-MIB", "wosPrefEmailAlertRmndrInterval"),
        ("DDN-WOS-MIB", "wosPrefEmailAlertFromAddr"),
        ("DDN-WOS-MIB", "wosPrefEmailAlertRecipient"),
        ("DDN-WOS-MIB", "wosPrefEmailAlertServer"),
        ("DDN-WOS-MIB", "wosPrefSnmpManager"),
        ("DDN-WOS-MIB", "wosPrefSnmpTrapCommunityName"),
        ("DDN-WOS-MIB", "wosPrefMgmtIpFilter"),
        ("DDN-WOS-MIB", "wosPrefClientIpFilter"),
        ("DDN-WOS-MIB", "wosPrefSyslogFacility"),
        ("DDN-WOS-MIB", "wosPrefSyslogRemoteHost"))
)
if mibBuilder.loadTexts:
    wosPrefsGroup.setStatus("current")


# Notification objects

wosTrapMessage = NotificationType(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 0, 1)
)
wosTrapMessage.setObjects(
      *(("DDN-WOS-MIB", "wosTrapSeverity"),
        ("DDN-WOS-MIB", "wosTrapType"),
        ("DDN-WOS-MIB", "wosTrapLocation"),
        ("DDN-WOS-MIB", "wosTrapDesc"))
)
if mibBuilder.loadTexts:
    wosTrapMessage.setStatus(
        "current"
    )


# Notifications groups

wosEventsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 2, 2, 1)
)
wosEventsGroup.setObjects(
    ("DDN-WOS-MIB", "wosTrapMessage")
)
if mibBuilder.loadTexts:
    wosEventsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

wosCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6894, 4, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    wosCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DDN-WOS-MIB",
    **{"WosSeverityLevel": WosSeverityLevel,
       "WosSyslogFacility": WosSyslogFacility,
       "datadirect": datadirect,
       "wos": wos,
       "wosMIB": wosMIB,
       "wosNotifications": wosNotifications,
       "wosTrapMessage": wosTrapMessage,
       "wosObjects": wosObjects,
       "wosNotificationInfo": wosNotificationInfo,
       "wosTrapDesc": wosTrapDesc,
       "wosTrapSeverity": wosTrapSeverity,
       "wosTrapType": wosTrapType,
       "wosTrapLocation": wosTrapLocation,
       "wosStatsInfo": wosStatsInfo,
       "wosStatsFRPS": wosStatsFRPS,
       "wosStatsFWPS": wosStatsFWPS,
       "wosStatsFDPS": wosStatsFDPS,
       "wosStatsReadLatency": wosStatsReadLatency,
       "wosStatsWriteLatency": wosStatsWriteLatency,
       "wosStatsDeleteLatency": wosStatsDeleteLatency,
       "wosStatsReadThroughput": wosStatsReadThroughput,
       "wosStatsWriteThroughput": wosStatsWriteThroughput,
       "wosStatsReadCount": wosStatsReadCount,
       "wosStatsWriteCount": wosStatsWriteCount,
       "wosStatsDeleteCount": wosStatsDeleteCount,
       "wosAlertsInfo": wosAlertsInfo,
       "wosAlertTable": wosAlertTable,
       "wosAlertEntry": wosAlertEntry,
       "wosAlertIndex": wosAlertIndex,
       "wosAlertSeverity": wosAlertSeverity,
       "wosAlertTime": wosAlertTime,
       "wosAlertType": wosAlertType,
       "wosAlertLocation": wosAlertLocation,
       "wosAlertDesc": wosAlertDesc,
       "wosClusterInfo": wosClusterInfo,
       "wosClusterName": wosClusterName,
       "wosClusterId": wosClusterId,
       "wosClusterStatus": wosClusterStatus,
       "wosClusterPrimaryNodeAddressType": wosClusterPrimaryNodeAddressType,
       "wosClusterPrimaryNodeAddress": wosClusterPrimaryNodeAddress,
       "wosClusterTotalNodeCount": wosClusterTotalNodeCount,
       "wosClusterActiveNodeCount": wosClusterActiveNodeCount,
       "wosClusterDisconnectedNodeCount": wosClusterDisconnectedNodeCount,
       "wosClusterConnectedClientsCount": wosClusterConnectedClientsCount,
       "wosClusterObjectCountLow": wosClusterObjectCountLow,
       "wosClusterObjectCountHigh": wosClusterObjectCountHigh,
       "wosClusterUsableCapacity": wosClusterUsableCapacity,
       "wosClusterUsedCapacity": wosClusterUsedCapacity,
       "wosClusterFreeCapacity": wosClusterFreeCapacity,
       "wosZonesInfo": wosZonesInfo,
       "wosZoneTable": wosZoneTable,
       "wosZoneEntry": wosZoneEntry,
       "wosZoneId": wosZoneId,
       "wosZoneName": wosZoneName,
       "wosZoneNodeCount": wosZoneNodeCount,
       "wosNodesInfo": wosNodesInfo,
       "wosNodeTable": wosNodeTable,
       "wosNodeEntry": wosNodeEntry,
       "wosNodeIndex": wosNodeIndex,
       "wosNodeName": wosNodeName,
       "wosNodeAddressType": wosNodeAddressType,
       "wosNodeAddress": wosNodeAddress,
       "wosNodeZoneName": wosNodeZoneName,
       "wosNodeStatus": wosNodeStatus,
       "wosNodeFwVersion": wosNodeFwVersion,
       "wosNodeObjectCountLow": wosNodeObjectCountLow,
       "wosNodeObjectCountHigh": wosNodeObjectCountHigh,
       "wosNodeTotalCapacity": wosNodeTotalCapacity,
       "wosNodeUsedCapacity": wosNodeUsedCapacity,
       "wosNodePercentFull": wosNodePercentFull,
       "wosPendingNodeTable": wosPendingNodeTable,
       "wosPendingNodeEntry": wosPendingNodeEntry,
       "wosPendingNodeIndex": wosPendingNodeIndex,
       "wosPendingNodeAddressType": wosPendingNodeAddressType,
       "wosPendingNodeAddress": wosPendingNodeAddress,
       "wosPendingNodeStatus": wosPendingNodeStatus,
       "wosNodeDriveTable": wosNodeDriveTable,
       "wosNodeDriveEntry": wosNodeDriveEntry,
       "wosNodeDriveSlotNbr": wosNodeDriveSlotNbr,
       "wosNodeDriveNodeName": wosNodeDriveNodeName,
       "wosNodeDriveMfgr": wosNodeDriveMfgr,
       "wosNodeDriveModel": wosNodeDriveModel,
       "wosNodeDriveSerialNbr": wosNodeDriveSerialNbr,
       "wosNodeDriveStatus": wosNodeDriveStatus,
       "wosNodeDriveCapacity": wosNodeDriveCapacity,
       "wosPoliciesInfo": wosPoliciesInfo,
       "wosPolicyTable": wosPolicyTable,
       "wosPolicyEntry": wosPolicyEntry,
       "wosPolicyIndex": wosPolicyIndex,
       "wosPolicyReplicaIndex": wosPolicyReplicaIndex,
       "wosPolicyId": wosPolicyId,
       "wosPolicyName": wosPolicyName,
       "wosPolicyReplicaZoneName": wosPolicyReplicaZoneName,
       "wosPolicyReplicaCount": wosPolicyReplicaCount,
       "wosPolicyReplicationType": wosPolicyReplicationType,
       "wosPolicyLocalDataProtection": wosPolicyLocalDataProtection,
       "wosPolicyObjCountLow": wosPolicyObjCountLow,
       "wosPolicyObjCountHigh": wosPolicyObjCountHigh,
       "wosPolicyNonComplObjCountLow": wosPolicyNonComplObjCountLow,
       "wosPolicyNonComplObjCountHigh": wosPolicyNonComplObjCountHigh,
       "wosPolicyUsedCapacity": wosPolicyUsedCapacity,
       "wosPrefsInfo": wosPrefsInfo,
       "wosPrefStoreUnderReplObjs": wosPrefStoreUnderReplObjs,
       "wosPrefNodeDownDelay": wosPrefNodeDownDelay,
       "wosPrefEmailAlertNewInterval": wosPrefEmailAlertNewInterval,
       "wosPrefEmailAlertRmndrInterval": wosPrefEmailAlertRmndrInterval,
       "wosPrefEmailAlertFromAddr": wosPrefEmailAlertFromAddr,
       "wosPrefEmailAlertRecipientTable": wosPrefEmailAlertRecipientTable,
       "wosPrefEmailAlertRecipientEntry": wosPrefEmailAlertRecipientEntry,
       "wosPrefEmailAlertRecipientIndex": wosPrefEmailAlertRecipientIndex,
       "wosPrefEmailAlertRecipient": wosPrefEmailAlertRecipient,
       "wosPrefEmailAlertServerTable": wosPrefEmailAlertServerTable,
       "wosPrefEmailAlertServerEntry": wosPrefEmailAlertServerEntry,
       "wosPrefEmailAlertServerIndex": wosPrefEmailAlertServerIndex,
       "wosPrefEmailAlertServer": wosPrefEmailAlertServer,
       "wosPrefSnmpManagerTable": wosPrefSnmpManagerTable,
       "wosPrefSnmpManagerEntry": wosPrefSnmpManagerEntry,
       "wosPrefSnmpManagerIndex": wosPrefSnmpManagerIndex,
       "wosPrefSnmpManager": wosPrefSnmpManager,
       "wosPrefSnmpTrapCommunityName": wosPrefSnmpTrapCommunityName,
       "wosPrefMgmtIpFilterTable": wosPrefMgmtIpFilterTable,
       "wosPrefMgmtIpFilterEntry": wosPrefMgmtIpFilterEntry,
       "wosPrefMgmtIpFilterIndex": wosPrefMgmtIpFilterIndex,
       "wosPrefMgmtIpFilter": wosPrefMgmtIpFilter,
       "wosPrefClientIpFilterTable": wosPrefClientIpFilterTable,
       "wosPrefClientIpFilterEntry": wosPrefClientIpFilterEntry,
       "wosPrefClientIpFilterIndex": wosPrefClientIpFilterIndex,
       "wosPrefClientIpFilter": wosPrefClientIpFilter,
       "wosPrefSyslogFacility": wosPrefSyslogFacility,
       "wosPrefSyslogRemoteHost": wosPrefSyslogRemoteHost,
       "wosConformance": wosConformance,
       "wosCompliances": wosCompliances,
       "wosCompliance": wosCompliance,
       "wosGroups": wosGroups,
       "wosEventsGroup": wosEventsGroup,
       "wosNotificationsGroup": wosNotificationsGroup,
       "wosStatsGroup": wosStatsGroup,
       "wosAlertsGroup": wosAlertsGroup,
       "wosClusterGroup": wosClusterGroup,
       "wosZonesGroup": wosZonesGroup,
       "wosNodesGroup": wosNodesGroup,
       "wosPoliciesGroup": wosPoliciesGroup,
       "wosPrefsGroup": wosPrefsGroup}
)
