# SNMP MIB module (PEPWAVE-MAX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PEPWAVE-MAX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:38:24 2024
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

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

pepwaveMAX = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27662, 1)
)
pepwaveMAX.setRevisions(
        ("2012-06-06 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TableIndex(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class ConnectionNum(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class NameString(OctetString, TextualConvention):
    status = "current"
    displayHint = "80a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )



class PortSpeedType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("fullDulplex10", 2),
          ("fullDulplex100", 4),
          ("fullDulplex1000", 6),
          ("halfDulplex10", 3),
          ("halfDulplex100", 5),
          ("halfDulplex1000", 7),
          ("unknown", 0))
    )



# MIB Managed Objects in the order of their OIDs

_MaxStatus_ObjectIdentity = ObjectIdentity
maxStatus = _MaxStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27662, 1, 1)
)
_MaxSystem_ObjectIdentity = ObjectIdentity
maxSystem = _MaxSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27662, 1, 1, 1)
)
_MaxFirmware_Type = NameString
_MaxFirmware_Object = MibScalar
maxFirmware = _MaxFirmware_Object(
    (1, 3, 6, 1, 4, 1, 27662, 1, 1, 1, 1),
    _MaxFirmware_Type()
)
maxFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxFirmware.setStatus("current")
_MaxSerialNumber_Type = NameString
_MaxSerialNumber_Object = MibScalar
maxSerialNumber = _MaxSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 27662, 1, 1, 1, 2),
    _MaxSerialNumber_Type()
)
maxSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxSerialNumber.setStatus("current")
_MaxTime_Type = NameString
_MaxTime_Object = MibScalar
maxTime = _MaxTime_Object(
    (1, 3, 6, 1, 4, 1, 27662, 1, 1, 1, 3),
    _MaxTime_Type()
)
maxTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxTime.setStatus("current")
_MaxUpTime_Type = TimeTicks
_MaxUpTime_Object = MibScalar
maxUpTime = _MaxUpTime_Object(
    (1, 3, 6, 1, 4, 1, 27662, 1, 1, 1, 4),
    _MaxUpTime_Type()
)
maxUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxUpTime.setStatus("current")
_MaxLan_ObjectIdentity = ObjectIdentity
maxLan = _MaxLan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27662, 1, 1, 1, 6)
)
_MaxLanStatus_Type = NameString
_MaxLanStatus_Object = MibScalar
maxLanStatus = _MaxLanStatus_Object(
    (1, 3, 6, 1, 4, 1, 27662, 1, 1, 1, 6, 1),
    _MaxLanStatus_Type()
)
maxLanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxLanStatus.setStatus("current")
_MaxLanIp_Type = IpAddress
_MaxLanIp_Object = MibScalar
maxLanIp = _MaxLanIp_Object(
    (1, 3, 6, 1, 4, 1, 27662, 1, 1, 1, 6, 2),
    _MaxLanIp_Type()
)
maxLanIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxLanIp.setStatus("current")
_MaxLanSubnetMask_Type = IpAddress
_MaxLanSubnetMask_Object = MibScalar
maxLanSubnetMask = _MaxLanSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 27662, 1, 1, 1, 6, 3),
    _MaxLanSubnetMask_Type()
)
maxLanSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxLanSubnetMask.setStatus("current")
_MaxLinkStatus_ObjectIdentity = ObjectIdentity
maxLinkStatus = _MaxLinkStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27662, 1, 1, 2)
)
_MaxLinkNumber_Type = Counter32
_MaxLinkNumber_Object = MibScalar
maxLinkNumber = _MaxLinkNumber_Object(
    (1, 3, 6, 1, 4, 1, 27662, 1, 1, 2, 1),
    _MaxLinkNumber_Type()
)
maxLinkNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxLinkNumber.setStatus("current")
_LinkTable_Object = MibTable
linkTable = _LinkTable_Object(
    (1, 3, 6, 1, 4, 1, 27662, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    linkTable.setStatus("current")
_LinkEntry_Object = MibTableRow
linkEntry = _LinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 27662, 1, 1, 2, 2, 1)
)
linkEntry.setIndexNames(
    (0, "PEPWAVE-MAX-MIB", "linkConnNum"),
)
if mibBuilder.loadTexts:
    linkEntry.setStatus("current")
_LinkConnNum_Type = ConnectionNum
_LinkConnNum_Object = MibTableColumn
linkConnNum = _LinkConnNum_Object(
    (1, 3, 6, 1, 4, 1, 27662, 1, 1, 2, 2, 1, 1),
    _LinkConnNum_Type()
)
linkConnNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    linkConnNum.setStatus("current")
_LinkName_Type = NameString
_LinkName_Object = MibTableColumn
linkName = _LinkName_Object(
    (1, 3, 6, 1, 4, 1, 27662, 1, 1, 2, 2, 1, 2),
    _LinkName_Type()
)
linkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkName.setStatus("current")
_LinkStatus_Type = NameString
_LinkStatus_Object = MibTableColumn
linkStatus = _LinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 27662, 1, 1, 2, 2, 1, 3),
    _LinkStatus_Type()
)
linkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStatus.setStatus("current")
_LinkThroughputIn_Type = Counter32
_LinkThroughputIn_Object = MibTableColumn
linkThroughputIn = _LinkThroughputIn_Object(
    (1, 3, 6, 1, 4, 1, 27662, 1, 1, 2, 2, 1, 4),
    _LinkThroughputIn_Type()
)
linkThroughputIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkThroughputIn.setStatus("current")
_LinkThroughputOut_Type = Counter32
_LinkThroughputOut_Object = MibTableColumn
linkThroughputOut = _LinkThroughputOut_Object(
    (1, 3, 6, 1, 4, 1, 27662, 1, 1, 2, 2, 1, 5),
    _LinkThroughputOut_Type()
)
linkThroughputOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkThroughputOut.setStatus("current")
_LinkDataTransferred_Type = Counter64
_LinkDataTransferred_Object = MibTableColumn
linkDataTransferred = _LinkDataTransferred_Object(
    (1, 3, 6, 1, 4, 1, 27662, 1, 1, 2, 2, 1, 6),
    _LinkDataTransferred_Type()
)
linkDataTransferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkDataTransferred.setStatus("current")
_LinkIpTable_Object = MibTable
linkIpTable = _LinkIpTable_Object(
    (1, 3, 6, 1, 4, 1, 27662, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    linkIpTable.setStatus("current")
_LinkIpEntry_Object = MibTableRow
linkIpEntry = _LinkIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 27662, 1, 1, 2, 3, 1)
)
linkIpEntry.setIndexNames(
    (0, "PEPWAVE-MAX-MIB", "linkIpConnNum"),
    (0, "PEPWAVE-MAX-MIB", "linkIpIndex"),
)
if mibBuilder.loadTexts:
    linkIpEntry.setStatus("current")
_LinkIpConnNum_Type = ConnectionNum
_LinkIpConnNum_Object = MibTableColumn
linkIpConnNum = _LinkIpConnNum_Object(
    (1, 3, 6, 1, 4, 1, 27662, 1, 1, 2, 3, 1, 1),
    _LinkIpConnNum_Type()
)
linkIpConnNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    linkIpConnNum.setStatus("current")
_LinkIpIndex_Type = TableIndex
_LinkIpIndex_Object = MibTableColumn
linkIpIndex = _LinkIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 27662, 1, 1, 2, 3, 1, 2),
    _LinkIpIndex_Type()
)
linkIpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    linkIpIndex.setStatus("current")
_LinkIp_Type = IpAddress
_LinkIp_Object = MibTableColumn
linkIp = _LinkIp_Object(
    (1, 3, 6, 1, 4, 1, 27662, 1, 1, 2, 3, 1, 3),
    _LinkIp_Type()
)
linkIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkIp.setStatus("current")
_WanUsageTable_Object = MibTable
wanUsageTable = _WanUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 27662, 1, 1, 3)
)
if mibBuilder.loadTexts:
    wanUsageTable.setStatus("current")
_WanUsageEntry_Object = MibTableRow
wanUsageEntry = _WanUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 27662, 1, 1, 3, 1)
)
wanUsageEntry.setIndexNames(
    (0, "PEPWAVE-MAX-MIB", "wanUsageIndex"),
)
if mibBuilder.loadTexts:
    wanUsageEntry.setStatus("current")
_WanUsageIndex_Type = TableIndex
_WanUsageIndex_Object = MibTableColumn
wanUsageIndex = _WanUsageIndex_Object(
    (1, 3, 6, 1, 4, 1, 27662, 1, 1, 3, 1, 1),
    _WanUsageIndex_Type()
)
wanUsageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wanUsageIndex.setStatus("current")
_WanUsageThroughputIn_Type = Counter32
_WanUsageThroughputIn_Object = MibTableColumn
wanUsageThroughputIn = _WanUsageThroughputIn_Object(
    (1, 3, 6, 1, 4, 1, 27662, 1, 1, 3, 1, 2),
    _WanUsageThroughputIn_Type()
)
wanUsageThroughputIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanUsageThroughputIn.setStatus("current")
_WanUsageThroughputOut_Type = Counter32
_WanUsageThroughputOut_Object = MibTableColumn
wanUsageThroughputOut = _WanUsageThroughputOut_Object(
    (1, 3, 6, 1, 4, 1, 27662, 1, 1, 3, 1, 3),
    _WanUsageThroughputOut_Type()
)
wanUsageThroughputOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanUsageThroughputOut.setStatus("current")
_WanUsageDataTransferred_Type = Counter64
_WanUsageDataTransferred_Object = MibTableColumn
wanUsageDataTransferred = _WanUsageDataTransferred_Object(
    (1, 3, 6, 1, 4, 1, 27662, 1, 1, 3, 1, 4),
    _WanUsageDataTransferred_Type()
)
wanUsageDataTransferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanUsageDataTransferred.setStatus("current")
_MaxMaintenance_ObjectIdentity = ObjectIdentity
maxMaintenance = _MaxMaintenance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27662, 1, 2)
)
_MaxReboot_Type = NameString
_MaxReboot_Object = MibScalar
maxReboot = _MaxReboot_Object(
    (1, 3, 6, 1, 4, 1, 27662, 1, 2, 1),
    _MaxReboot_Type()
)
maxReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxReboot.setStatus("current")
_MaxLanConfig_ObjectIdentity = ObjectIdentity
maxLanConfig = _MaxLanConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27662, 1, 3)
)
_PortLanSpeedConfig_Type = PortSpeedType
_PortLanSpeedConfig_Object = MibScalar
portLanSpeedConfig = _PortLanSpeedConfig_Object(
    (1, 3, 6, 1, 4, 1, 27662, 1, 3, 1),
    _PortLanSpeedConfig_Type()
)
portLanSpeedConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portLanSpeedConfig.setStatus("current")
_PortWanSpeedConfigTable_Object = MibTable
portWanSpeedConfigTable = _PortWanSpeedConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 27662, 1, 3, 2)
)
if mibBuilder.loadTexts:
    portWanSpeedConfigTable.setStatus("current")
_PortWanSpeedConfigEntry_Object = MibTableRow
portWanSpeedConfigEntry = _PortWanSpeedConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 27662, 1, 3, 2, 1)
)
portWanSpeedConfigEntry.setIndexNames(
    (0, "PEPWAVE-MAX-MIB", "portWanSpeedConfigIndex"),
)
if mibBuilder.loadTexts:
    portWanSpeedConfigEntry.setStatus("current")
_PortWanSpeedConfigIndex_Type = TableIndex
_PortWanSpeedConfigIndex_Object = MibTableColumn
portWanSpeedConfigIndex = _PortWanSpeedConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 27662, 1, 3, 2, 1, 1),
    _PortWanSpeedConfigIndex_Type()
)
portWanSpeedConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portWanSpeedConfigIndex.setStatus("current")
_PortWanSpeedConfig_Type = PortSpeedType
_PortWanSpeedConfig_Object = MibTableColumn
portWanSpeedConfig = _PortWanSpeedConfig_Object(
    (1, 3, 6, 1, 4, 1, 27662, 1, 3, 2, 1, 2),
    _PortWanSpeedConfig_Type()
)
portWanSpeedConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portWanSpeedConfig.setStatus("current")
_LanConfigIp_Type = IpAddress
_LanConfigIp_Object = MibScalar
lanConfigIp = _LanConfigIp_Object(
    (1, 3, 6, 1, 4, 1, 27662, 1, 3, 3),
    _LanConfigIp_Type()
)
lanConfigIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanConfigIp.setStatus("current")
_LanConfigSubnetMask_Type = IpAddress
_LanConfigSubnetMask_Object = MibScalar
lanConfigSubnetMask = _LanConfigSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 27662, 1, 3, 4),
    _LanConfigSubnetMask_Type()
)
lanConfigSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanConfigSubnetMask.setStatus("current")
_MaxConformance_ObjectIdentity = ObjectIdentity
maxConformance = _MaxConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27662, 1, 50)
)
_MaxCompliances_ObjectIdentity = ObjectIdentity
maxCompliances = _MaxCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27662, 1, 50, 1)
)
_MaxGroups_ObjectIdentity = ObjectIdentity
maxGroups = _MaxGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27662, 1, 50, 2)
)

# Managed Objects groups

maxSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27662, 1, 50, 2, 1)
)
maxSystemGroup.setObjects(
      *(("PEPWAVE-MAX-MIB", "maxFirmware"),
        ("PEPWAVE-MAX-MIB", "maxSerialNumber"),
        ("PEPWAVE-MAX-MIB", "maxTime"),
        ("PEPWAVE-MAX-MIB", "maxUpTime"),
        ("PEPWAVE-MAX-MIB", "maxLanStatus"),
        ("PEPWAVE-MAX-MIB", "maxLanIp"),
        ("PEPWAVE-MAX-MIB", "maxLanSubnetMask"))
)
if mibBuilder.loadTexts:
    maxSystemGroup.setStatus("current")

maxLinkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27662, 1, 50, 2, 2)
)
maxLinkGroup.setObjects(
      *(("PEPWAVE-MAX-MIB", "maxLinkNumber"),
        ("PEPWAVE-MAX-MIB", "linkName"),
        ("PEPWAVE-MAX-MIB", "linkStatus"),
        ("PEPWAVE-MAX-MIB", "linkIp"),
        ("PEPWAVE-MAX-MIB", "linkThroughputIn"),
        ("PEPWAVE-MAX-MIB", "linkThroughputOut"),
        ("PEPWAVE-MAX-MIB", "linkDataTransferred"))
)
if mibBuilder.loadTexts:
    maxLinkGroup.setStatus("current")

maxWanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27662, 1, 50, 2, 3)
)
maxWanGroup.setObjects(
      *(("PEPWAVE-MAX-MIB", "wanUsageThroughputIn"),
        ("PEPWAVE-MAX-MIB", "wanUsageThroughputOut"),
        ("PEPWAVE-MAX-MIB", "wanUsageDataTransferred"))
)
if mibBuilder.loadTexts:
    maxWanGroup.setStatus("current")

maxSetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27662, 1, 50, 2, 4)
)
maxSetGroup.setObjects(
      *(("PEPWAVE-MAX-MIB", "maxReboot"),
        ("PEPWAVE-MAX-MIB", "portWanSpeedConfig"),
        ("PEPWAVE-MAX-MIB", "portLanSpeedConfig"),
        ("PEPWAVE-MAX-MIB", "lanConfigIp"),
        ("PEPWAVE-MAX-MIB", "lanConfigSubnetMask"))
)
if mibBuilder.loadTexts:
    maxSetGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

maxCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27662, 1, 50, 1, 1)
)
if mibBuilder.loadTexts:
    maxCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PEPWAVE-MAX-MIB",
    **{"TableIndex": TableIndex,
       "ConnectionNum": ConnectionNum,
       "NameString": NameString,
       "PortSpeedType": PortSpeedType,
       "pepwaveMAX": pepwaveMAX,
       "maxStatus": maxStatus,
       "maxSystem": maxSystem,
       "maxFirmware": maxFirmware,
       "maxSerialNumber": maxSerialNumber,
       "maxTime": maxTime,
       "maxUpTime": maxUpTime,
       "maxLan": maxLan,
       "maxLanStatus": maxLanStatus,
       "maxLanIp": maxLanIp,
       "maxLanSubnetMask": maxLanSubnetMask,
       "maxLinkStatus": maxLinkStatus,
       "maxLinkNumber": maxLinkNumber,
       "linkTable": linkTable,
       "linkEntry": linkEntry,
       "linkConnNum": linkConnNum,
       "linkName": linkName,
       "linkStatus": linkStatus,
       "linkThroughputIn": linkThroughputIn,
       "linkThroughputOut": linkThroughputOut,
       "linkDataTransferred": linkDataTransferred,
       "linkIpTable": linkIpTable,
       "linkIpEntry": linkIpEntry,
       "linkIpConnNum": linkIpConnNum,
       "linkIpIndex": linkIpIndex,
       "linkIp": linkIp,
       "wanUsageTable": wanUsageTable,
       "wanUsageEntry": wanUsageEntry,
       "wanUsageIndex": wanUsageIndex,
       "wanUsageThroughputIn": wanUsageThroughputIn,
       "wanUsageThroughputOut": wanUsageThroughputOut,
       "wanUsageDataTransferred": wanUsageDataTransferred,
       "maxMaintenance": maxMaintenance,
       "maxReboot": maxReboot,
       "maxLanConfig": maxLanConfig,
       "portLanSpeedConfig": portLanSpeedConfig,
       "portWanSpeedConfigTable": portWanSpeedConfigTable,
       "portWanSpeedConfigEntry": portWanSpeedConfigEntry,
       "portWanSpeedConfigIndex": portWanSpeedConfigIndex,
       "portWanSpeedConfig": portWanSpeedConfig,
       "lanConfigIp": lanConfigIp,
       "lanConfigSubnetMask": lanConfigSubnetMask,
       "maxConformance": maxConformance,
       "maxCompliances": maxCompliances,
       "maxCompliance": maxCompliance,
       "maxGroups": maxGroups,
       "maxSystemGroup": maxSystemGroup,
       "maxLinkGroup": maxLinkGroup,
       "maxWanGroup": maxWanGroup,
       "maxSetGroup": maxSetGroup}
)
