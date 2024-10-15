# SNMP MIB module (PEPLINK-BALANCE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PEPLINK-BALANCE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:38:23 2024
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

peplinkBalance = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 23695, 1)
)
peplinkBalance.setRevisions(
        ("2009-03-05 00:00",
         "2009-03-05 00:00")
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

_BalanceStatus_ObjectIdentity = ObjectIdentity
balanceStatus = _BalanceStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23695, 1, 1)
)
_BalanceSystem_ObjectIdentity = ObjectIdentity
balanceSystem = _BalanceSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23695, 1, 1, 1)
)
_BalFirmware_Type = NameString
_BalFirmware_Object = MibScalar
balFirmware = _BalFirmware_Object(
    (1, 3, 6, 1, 4, 1, 23695, 1, 1, 1, 1),
    _BalFirmware_Type()
)
balFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    balFirmware.setStatus("current")
_BalSerialNumber_Type = NameString
_BalSerialNumber_Object = MibScalar
balSerialNumber = _BalSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 23695, 1, 1, 1, 2),
    _BalSerialNumber_Type()
)
balSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    balSerialNumber.setStatus("current")
_BalTime_Type = NameString
_BalTime_Object = MibScalar
balTime = _BalTime_Object(
    (1, 3, 6, 1, 4, 1, 23695, 1, 1, 1, 3),
    _BalTime_Type()
)
balTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    balTime.setStatus("current")
_BalUpTime_Type = TimeTicks
_BalUpTime_Object = MibScalar
balUpTime = _BalUpTime_Object(
    (1, 3, 6, 1, 4, 1, 23695, 1, 1, 1, 4),
    _BalUpTime_Type()
)
balUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    balUpTime.setStatus("current")
_BalanceLan_ObjectIdentity = ObjectIdentity
balanceLan = _BalanceLan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23695, 1, 1, 1, 6)
)
_BalLanStatus_Type = NameString
_BalLanStatus_Object = MibScalar
balLanStatus = _BalLanStatus_Object(
    (1, 3, 6, 1, 4, 1, 23695, 1, 1, 1, 6, 1),
    _BalLanStatus_Type()
)
balLanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    balLanStatus.setStatus("current")
_BalLanIp_Type = IpAddress
_BalLanIp_Object = MibScalar
balLanIp = _BalLanIp_Object(
    (1, 3, 6, 1, 4, 1, 23695, 1, 1, 1, 6, 2),
    _BalLanIp_Type()
)
balLanIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    balLanIp.setStatus("current")
_BalLanSubnetMask_Type = IpAddress
_BalLanSubnetMask_Object = MibScalar
balLanSubnetMask = _BalLanSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 23695, 1, 1, 1, 6, 3),
    _BalLanSubnetMask_Type()
)
balLanSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    balLanSubnetMask.setStatus("current")
_BalLinkStatus_ObjectIdentity = ObjectIdentity
balLinkStatus = _BalLinkStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23695, 1, 1, 2)
)
_BalLinkNumber_Type = Counter32
_BalLinkNumber_Object = MibScalar
balLinkNumber = _BalLinkNumber_Object(
    (1, 3, 6, 1, 4, 1, 23695, 1, 1, 2, 1),
    _BalLinkNumber_Type()
)
balLinkNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    balLinkNumber.setStatus("current")
_LinkTable_Object = MibTable
linkTable = _LinkTable_Object(
    (1, 3, 6, 1, 4, 1, 23695, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    linkTable.setStatus("current")
_LinkEntry_Object = MibTableRow
linkEntry = _LinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 23695, 1, 1, 2, 2, 1)
)
linkEntry.setIndexNames(
    (0, "PEPLINK-BALANCE-MIB", "linkConnNum"),
)
if mibBuilder.loadTexts:
    linkEntry.setStatus("current")
_LinkConnNum_Type = ConnectionNum
_LinkConnNum_Object = MibTableColumn
linkConnNum = _LinkConnNum_Object(
    (1, 3, 6, 1, 4, 1, 23695, 1, 1, 2, 2, 1, 1),
    _LinkConnNum_Type()
)
linkConnNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    linkConnNum.setStatus("current")
_LinkName_Type = NameString
_LinkName_Object = MibTableColumn
linkName = _LinkName_Object(
    (1, 3, 6, 1, 4, 1, 23695, 1, 1, 2, 2, 1, 2),
    _LinkName_Type()
)
linkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkName.setStatus("current")
_LinkStatus_Type = NameString
_LinkStatus_Object = MibTableColumn
linkStatus = _LinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 23695, 1, 1, 2, 2, 1, 3),
    _LinkStatus_Type()
)
linkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStatus.setStatus("current")
_LinkThroughputIn_Type = Counter32
_LinkThroughputIn_Object = MibTableColumn
linkThroughputIn = _LinkThroughputIn_Object(
    (1, 3, 6, 1, 4, 1, 23695, 1, 1, 2, 2, 1, 4),
    _LinkThroughputIn_Type()
)
linkThroughputIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkThroughputIn.setStatus("current")
_LinkThroughputOut_Type = Counter32
_LinkThroughputOut_Object = MibTableColumn
linkThroughputOut = _LinkThroughputOut_Object(
    (1, 3, 6, 1, 4, 1, 23695, 1, 1, 2, 2, 1, 5),
    _LinkThroughputOut_Type()
)
linkThroughputOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkThroughputOut.setStatus("current")
_LinkDataTransferred_Type = Counter64
_LinkDataTransferred_Object = MibTableColumn
linkDataTransferred = _LinkDataTransferred_Object(
    (1, 3, 6, 1, 4, 1, 23695, 1, 1, 2, 2, 1, 6),
    _LinkDataTransferred_Type()
)
linkDataTransferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkDataTransferred.setStatus("current")
_LinkIpTable_Object = MibTable
linkIpTable = _LinkIpTable_Object(
    (1, 3, 6, 1, 4, 1, 23695, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    linkIpTable.setStatus("current")
_LinkIpEntry_Object = MibTableRow
linkIpEntry = _LinkIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 23695, 1, 1, 2, 3, 1)
)
linkIpEntry.setIndexNames(
    (0, "PEPLINK-BALANCE-MIB", "linkIpConnNum"),
    (0, "PEPLINK-BALANCE-MIB", "linkIpIndex"),
)
if mibBuilder.loadTexts:
    linkIpEntry.setStatus("current")
_LinkIpConnNum_Type = ConnectionNum
_LinkIpConnNum_Object = MibTableColumn
linkIpConnNum = _LinkIpConnNum_Object(
    (1, 3, 6, 1, 4, 1, 23695, 1, 1, 2, 3, 1, 1),
    _LinkIpConnNum_Type()
)
linkIpConnNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    linkIpConnNum.setStatus("current")
_LinkIpIndex_Type = TableIndex
_LinkIpIndex_Object = MibTableColumn
linkIpIndex = _LinkIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 23695, 1, 1, 2, 3, 1, 2),
    _LinkIpIndex_Type()
)
linkIpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    linkIpIndex.setStatus("current")
_LinkIp_Type = IpAddress
_LinkIp_Object = MibTableColumn
linkIp = _LinkIp_Object(
    (1, 3, 6, 1, 4, 1, 23695, 1, 1, 2, 3, 1, 3),
    _LinkIp_Type()
)
linkIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkIp.setStatus("current")
_WanUsageTable_Object = MibTable
wanUsageTable = _WanUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 23695, 1, 1, 3)
)
if mibBuilder.loadTexts:
    wanUsageTable.setStatus("current")
_WanUsageEntry_Object = MibTableRow
wanUsageEntry = _WanUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 23695, 1, 1, 3, 1)
)
wanUsageEntry.setIndexNames(
    (0, "PEPLINK-BALANCE-MIB", "wanUsageIndex"),
)
if mibBuilder.loadTexts:
    wanUsageEntry.setStatus("current")
_WanUsageIndex_Type = TableIndex
_WanUsageIndex_Object = MibTableColumn
wanUsageIndex = _WanUsageIndex_Object(
    (1, 3, 6, 1, 4, 1, 23695, 1, 1, 3, 1, 1),
    _WanUsageIndex_Type()
)
wanUsageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wanUsageIndex.setStatus("current")
_WanUsageThroughputIn_Type = Counter32
_WanUsageThroughputIn_Object = MibTableColumn
wanUsageThroughputIn = _WanUsageThroughputIn_Object(
    (1, 3, 6, 1, 4, 1, 23695, 1, 1, 3, 1, 2),
    _WanUsageThroughputIn_Type()
)
wanUsageThroughputIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanUsageThroughputIn.setStatus("current")
_WanUsageThroughputOut_Type = Counter32
_WanUsageThroughputOut_Object = MibTableColumn
wanUsageThroughputOut = _WanUsageThroughputOut_Object(
    (1, 3, 6, 1, 4, 1, 23695, 1, 1, 3, 1, 3),
    _WanUsageThroughputOut_Type()
)
wanUsageThroughputOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanUsageThroughputOut.setStatus("current")
_WanUsageDataTransferred_Type = Counter64
_WanUsageDataTransferred_Object = MibTableColumn
wanUsageDataTransferred = _WanUsageDataTransferred_Object(
    (1, 3, 6, 1, 4, 1, 23695, 1, 1, 3, 1, 4),
    _WanUsageDataTransferred_Type()
)
wanUsageDataTransferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanUsageDataTransferred.setStatus("current")
_BalanceMaintenance_ObjectIdentity = ObjectIdentity
balanceMaintenance = _BalanceMaintenance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23695, 1, 2)
)
_BalReboot_Type = NameString
_BalReboot_Object = MibScalar
balReboot = _BalReboot_Object(
    (1, 3, 6, 1, 4, 1, 23695, 1, 2, 1),
    _BalReboot_Type()
)
balReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    balReboot.setStatus("current")
_BalanceLanConfig_ObjectIdentity = ObjectIdentity
balanceLanConfig = _BalanceLanConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23695, 1, 3)
)
_PortLanSpeedConfig_Type = PortSpeedType
_PortLanSpeedConfig_Object = MibScalar
portLanSpeedConfig = _PortLanSpeedConfig_Object(
    (1, 3, 6, 1, 4, 1, 23695, 1, 3, 1),
    _PortLanSpeedConfig_Type()
)
portLanSpeedConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portLanSpeedConfig.setStatus("current")
_PortWanSpeedConfigTable_Object = MibTable
portWanSpeedConfigTable = _PortWanSpeedConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 23695, 1, 3, 2)
)
if mibBuilder.loadTexts:
    portWanSpeedConfigTable.setStatus("current")
_PortWanSpeedConfigEntry_Object = MibTableRow
portWanSpeedConfigEntry = _PortWanSpeedConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 23695, 1, 3, 2, 1)
)
portWanSpeedConfigEntry.setIndexNames(
    (0, "PEPLINK-BALANCE-MIB", "portWanSpeedConfigIndex"),
)
if mibBuilder.loadTexts:
    portWanSpeedConfigEntry.setStatus("current")
_PortWanSpeedConfigIndex_Type = TableIndex
_PortWanSpeedConfigIndex_Object = MibTableColumn
portWanSpeedConfigIndex = _PortWanSpeedConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 23695, 1, 3, 2, 1, 1),
    _PortWanSpeedConfigIndex_Type()
)
portWanSpeedConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portWanSpeedConfigIndex.setStatus("current")
_PortWanSpeedConfig_Type = PortSpeedType
_PortWanSpeedConfig_Object = MibTableColumn
portWanSpeedConfig = _PortWanSpeedConfig_Object(
    (1, 3, 6, 1, 4, 1, 23695, 1, 3, 2, 1, 2),
    _PortWanSpeedConfig_Type()
)
portWanSpeedConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portWanSpeedConfig.setStatus("current")
_LanConfigIp_Type = IpAddress
_LanConfigIp_Object = MibScalar
lanConfigIp = _LanConfigIp_Object(
    (1, 3, 6, 1, 4, 1, 23695, 1, 3, 3),
    _LanConfigIp_Type()
)
lanConfigIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanConfigIp.setStatus("current")
_LanConfigSubnetMask_Type = IpAddress
_LanConfigSubnetMask_Object = MibScalar
lanConfigSubnetMask = _LanConfigSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 23695, 1, 3, 4),
    _LanConfigSubnetMask_Type()
)
lanConfigSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanConfigSubnetMask.setStatus("current")
_BalanceConformance_ObjectIdentity = ObjectIdentity
balanceConformance = _BalanceConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23695, 1, 50)
)
_BalCompliances_ObjectIdentity = ObjectIdentity
balCompliances = _BalCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23695, 1, 50, 1)
)
_BalGroups_ObjectIdentity = ObjectIdentity
balGroups = _BalGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23695, 1, 50, 2)
)

# Managed Objects groups

balSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 23695, 1, 50, 2, 1)
)
balSystemGroup.setObjects(
      *(("PEPLINK-BALANCE-MIB", "balFirmware"),
        ("PEPLINK-BALANCE-MIB", "balSerialNumber"),
        ("PEPLINK-BALANCE-MIB", "balTime"),
        ("PEPLINK-BALANCE-MIB", "balUpTime"),
        ("PEPLINK-BALANCE-MIB", "balLanStatus"),
        ("PEPLINK-BALANCE-MIB", "balLanIp"),
        ("PEPLINK-BALANCE-MIB", "balLanSubnetMask"))
)
if mibBuilder.loadTexts:
    balSystemGroup.setStatus("current")

balLinkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 23695, 1, 50, 2, 2)
)
balLinkGroup.setObjects(
      *(("PEPLINK-BALANCE-MIB", "balLinkNumber"),
        ("PEPLINK-BALANCE-MIB", "linkName"),
        ("PEPLINK-BALANCE-MIB", "linkStatus"),
        ("PEPLINK-BALANCE-MIB", "linkIp"),
        ("PEPLINK-BALANCE-MIB", "linkThroughputIn"),
        ("PEPLINK-BALANCE-MIB", "linkThroughputOut"),
        ("PEPLINK-BALANCE-MIB", "linkDataTransferred"))
)
if mibBuilder.loadTexts:
    balLinkGroup.setStatus("current")

balWanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 23695, 1, 50, 2, 3)
)
balWanGroup.setObjects(
      *(("PEPLINK-BALANCE-MIB", "wanUsageThroughputIn"),
        ("PEPLINK-BALANCE-MIB", "wanUsageThroughputOut"),
        ("PEPLINK-BALANCE-MIB", "wanUsageDataTransferred"))
)
if mibBuilder.loadTexts:
    balWanGroup.setStatus("current")

balSetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 23695, 1, 50, 2, 4)
)
balSetGroup.setObjects(
      *(("PEPLINK-BALANCE-MIB", "balReboot"),
        ("PEPLINK-BALANCE-MIB", "portWanSpeedConfig"),
        ("PEPLINK-BALANCE-MIB", "portLanSpeedConfig"),
        ("PEPLINK-BALANCE-MIB", "lanConfigIp"),
        ("PEPLINK-BALANCE-MIB", "lanConfigSubnetMask"))
)
if mibBuilder.loadTexts:
    balSetGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

balCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 23695, 1, 50, 1, 1)
)
if mibBuilder.loadTexts:
    balCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PEPLINK-BALANCE-MIB",
    **{"TableIndex": TableIndex,
       "ConnectionNum": ConnectionNum,
       "NameString": NameString,
       "PortSpeedType": PortSpeedType,
       "peplinkBalance": peplinkBalance,
       "balanceStatus": balanceStatus,
       "balanceSystem": balanceSystem,
       "balFirmware": balFirmware,
       "balSerialNumber": balSerialNumber,
       "balTime": balTime,
       "balUpTime": balUpTime,
       "balanceLan": balanceLan,
       "balLanStatus": balLanStatus,
       "balLanIp": balLanIp,
       "balLanSubnetMask": balLanSubnetMask,
       "balLinkStatus": balLinkStatus,
       "balLinkNumber": balLinkNumber,
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
       "balanceMaintenance": balanceMaintenance,
       "balReboot": balReboot,
       "balanceLanConfig": balanceLanConfig,
       "portLanSpeedConfig": portLanSpeedConfig,
       "portWanSpeedConfigTable": portWanSpeedConfigTable,
       "portWanSpeedConfigEntry": portWanSpeedConfigEntry,
       "portWanSpeedConfigIndex": portWanSpeedConfigIndex,
       "portWanSpeedConfig": portWanSpeedConfig,
       "lanConfigIp": lanConfigIp,
       "lanConfigSubnetMask": lanConfigSubnetMask,
       "balanceConformance": balanceConformance,
       "balCompliances": balCompliances,
       "balCompliance": balCompliance,
       "balGroups": balGroups,
       "balSystemGroup": balSystemGroup,
       "balLinkGroup": balLinkGroup,
       "balWanGroup": balWanGroup,
       "balSetGroup": balSetGroup}
)
