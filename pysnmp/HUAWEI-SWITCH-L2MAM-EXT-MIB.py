# SNMP MIB module (HUAWEI-SWITCH-L2MAM-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-SWITCH-L2MAM-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:06:04 2024
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

(entPhysicalName,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalName")

(hwBaseTrapEventType,
 hwBaseTrapProbableCause,
 hwBaseTrapSeverity) = mibBuilder.importSymbols(
    "HUAWEI-BASE-TRAP-MIB",
    "hwBaseTrapEventType",
    "hwBaseTrapProbableCause",
    "hwBaseTrapSeverity")

(hwCfgFdbMac,
 hwCfgFdbVlanId,
 hwCfgFdbVsiName,
 hwMacEntityUsage,
 hwMacEntityUsageThreshold,
 hwPortSecurityProtectAction) = mibBuilder.importSymbols(
    "HUAWEI-L2MAM-MIB",
    "hwCfgFdbMac",
    "hwCfgFdbVlanId",
    "hwCfgFdbVsiName",
    "hwMacEntityUsage",
    "hwMacEntityUsageThreshold",
    "hwPortSecurityProtectAction")

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(InterfaceIndex,
 ifDescr) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifDescr")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

hwSWITCH_L2MAM_EXT = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 315)
)
hwSWITCH_L2MAM_EXT.setRevisions(
        ("2014-03-26 16:00",
         "2014-03-26 16:00",
         "2014-03-19 16:00",
         "2014-02-14 16:00",
         "2004-06-08 00:00",
         "1996-10-31 00:00",
         "1999-12-07 00:00",
         "2004-06-08 00:00",
         "2004-06-08 00:00",
         "1996-10-31 00:00",
         "1999-12-07 00:00",
         "2004-06-08 00:00",
         "1996-10-31 00:00",
         "1999-12-07 00:00",
         "1996-10-31 00:00",
         "1999-12-07 00:00",
         "2004-06-08 00:00",
         "2004-06-08 00:00",
         "2004-06-08 00:00",
         "2010-08-11 16:00",
         "2014-02-14 16:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwSwitchL2MamExtObjects_ObjectIdentity = ObjectIdentity
hwSwitchL2MamExtObjects = _HwSwitchL2MamExtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 315, 1)
)
_HwMacTrapPortCfgTable_Object = MibTable
hwMacTrapPortCfgTable = _HwMacTrapPortCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 315, 1, 1)
)
if mibBuilder.loadTexts:
    hwMacTrapPortCfgTable.setStatus("current")
_HwMacTrapPortCfgEntry_Object = MibTableRow
hwMacTrapPortCfgEntry = _HwMacTrapPortCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 315, 1, 1, 1)
)
hwMacTrapPortCfgEntry.setIndexNames(
    (0, "HUAWEI-SWITCH-L2MAM-EXT-MIB", "hwMacTrapPortCfgIfIndex"),
)
if mibBuilder.loadTexts:
    hwMacTrapPortCfgEntry.setStatus("current")
_HwMacTrapPortCfgIfIndex_Type = InterfaceIndex
_HwMacTrapPortCfgIfIndex_Object = MibTableColumn
hwMacTrapPortCfgIfIndex = _HwMacTrapPortCfgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 315, 1, 1, 1, 1),
    _HwMacTrapPortCfgIfIndex_Type()
)
hwMacTrapPortCfgIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMacTrapPortCfgIfIndex.setStatus("current")


class _HwMacTrapPortCfgLearn_Type(Integer32):
    """Custom type hwMacTrapPortCfgLearn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HwMacTrapPortCfgLearn_Type.__name__ = "Integer32"
_HwMacTrapPortCfgLearn_Object = MibTableColumn
hwMacTrapPortCfgLearn = _HwMacTrapPortCfgLearn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 315, 1, 1, 1, 2),
    _HwMacTrapPortCfgLearn_Type()
)
hwMacTrapPortCfgLearn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacTrapPortCfgLearn.setStatus("current")


class _HwMacTrapPortCfgAging_Type(Integer32):
    """Custom type hwMacTrapPortCfgAging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HwMacTrapPortCfgAging_Type.__name__ = "Integer32"
_HwMacTrapPortCfgAging_Object = MibTableColumn
hwMacTrapPortCfgAging = _HwMacTrapPortCfgAging_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 315, 1, 1, 1, 3),
    _HwMacTrapPortCfgAging_Type()
)
hwMacTrapPortCfgAging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacTrapPortCfgAging.setStatus("current")
_HwSwitchL2MamExtGeneralObjects_ObjectIdentity = ObjectIdentity
hwSwitchL2MamExtGeneralObjects = _HwSwitchL2MamExtGeneralObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 315, 2)
)
_HwMacTrapInterval_Type = Integer32
_HwMacTrapInterval_Object = MibScalar
hwMacTrapInterval = _HwMacTrapInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 315, 2, 1),
    _HwMacTrapInterval_Type()
)
hwMacTrapInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacTrapInterval.setStatus("current")
_HwMacTrapMacInfo_Type = OctetString
_HwMacTrapMacInfo_Object = MibScalar
hwMacTrapMacInfo = _HwMacTrapMacInfo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 315, 2, 2),
    _HwMacTrapMacInfo_Type()
)
hwMacTrapMacInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMacTrapMacInfo.setStatus("current")
_HwSwitchL2MamExtTraps_ObjectIdentity = ObjectIdentity
hwSwitchL2MamExtTraps = _HwSwitchL2MamExtTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 315, 3)
)
_HwSwitchL2MamExtConformance_ObjectIdentity = ObjectIdentity
hwSwitchL2MamExtConformance = _HwSwitchL2MamExtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 315, 4)
)
_HwSwitchL2MamExtCompliances_ObjectIdentity = ObjectIdentity
hwSwitchL2MamExtCompliances = _HwSwitchL2MamExtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 315, 4, 1)
)
_HwSwitchL2MamExtGroups_ObjectIdentity = ObjectIdentity
hwSwitchL2MamExtGroups = _HwSwitchL2MamExtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 315, 4, 2)
)

# Managed Objects groups

hwMacTrapGroups = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 315, 4, 2, 1)
)
hwMacTrapGroups.setObjects(
      *(("HUAWEI-SWITCH-L2MAM-EXT-MIB", "hwMacTrapPortCfgLearn"),
        ("HUAWEI-SWITCH-L2MAM-EXT-MIB", "hwMacTrapPortCfgAging"))
)
if mibBuilder.loadTexts:
    hwMacTrapGroups.setStatus("current")

hwL2MAMExtGeneralGrops = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 315, 4, 2, 2)
)
hwL2MAMExtGeneralGrops.setObjects(
      *(("HUAWEI-SWITCH-L2MAM-EXT-MIB", "hwMacTrapInterval"),
        ("HUAWEI-SWITCH-L2MAM-EXT-MIB", "hwMacTrapMacInfo"))
)
if mibBuilder.loadTexts:
    hwL2MAMExtGeneralGrops.setStatus("current")


# Notification objects

hwMacTrapAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 315, 3, 1)
)
hwMacTrapAlarm.setObjects(
    ("HUAWEI-SWITCH-L2MAM-EXT-MIB", "hwMacTrapMacInfo")
)
if mibBuilder.loadTexts:
    hwMacTrapAlarm.setStatus(
        "current"
    )

hwPortVlanSecureMacAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 315, 3, 2)
)
hwPortVlanSecureMacAlarm.setObjects(
      *(("IF-MIB", "ifDescr"),
        ("HUAWEI-L2MAM-MIB", "hwCfgFdbMac"),
        ("HUAWEI-L2MAM-MIB", "hwCfgFdbVlanId"),
        ("HUAWEI-L2MAM-MIB", "hwPortSecurityProtectAction"))
)
if mibBuilder.loadTexts:
    hwPortVlanSecureMacAlarm.setStatus(
        "current"
    )

hwSlotMacUsageRaisingThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 315, 3, 3)
)
hwSlotMacUsageRaisingThreshold.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-L2MAM-MIB", "hwMacEntityUsage"),
        ("HUAWEI-L2MAM-MIB", "hwMacEntityUsageThreshold"),
        ("ENTITY-MIB", "entPhysicalName"))
)
if mibBuilder.loadTexts:
    hwSlotMacUsageRaisingThreshold.setStatus(
        "current"
    )

hwSlotMacUsageFallingThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 315, 3, 4)
)
hwSlotMacUsageFallingThreshold.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("ENTITY-MIB", "entPhysicalName"))
)
if mibBuilder.loadTexts:
    hwSlotMacUsageFallingThreshold.setStatus(
        "current"
    )

hwMacTrapPortCfgAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 315, 3, 5)
)
hwMacTrapPortCfgAlarm.setObjects(
      *(("HUAWEI-SWITCH-L2MAM-EXT-MIB", "hwMacTrapMacInfo"),
        ("HUAWEI-L2MAM-MIB", "hwCfgFdbMac"),
        ("HUAWEI-L2MAM-MIB", "hwCfgFdbVlanId"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hwMacTrapPortCfgAlarm.setStatus(
        "current"
    )

hwMacTrapHashConflictAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 315, 3, 6)
)
hwMacTrapHashConflictAlarm.setObjects(
      *(("IF-MIB", "ifDescr"),
        ("HUAWEI-L2MAM-MIB", "hwCfgFdbMac"),
        ("HUAWEI-L2MAM-MIB", "hwCfgFdbVlanId"),
        ("HUAWEI-L2MAM-MIB", "hwCfgFdbVsiName"))
)
if mibBuilder.loadTexts:
    hwMacTrapHashConflictAlarm.setStatus(
        "current"
    )


# Notifications groups

hwL2MAMExtTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 315, 4, 2, 3)
)
hwL2MAMExtTrapGroup.setObjects(
      *(("HUAWEI-SWITCH-L2MAM-EXT-MIB", "hwMacTrapAlarm"),
        ("HUAWEI-SWITCH-L2MAM-EXT-MIB", "hwMacTrapPortCfgAlarm"),
        ("HUAWEI-SWITCH-L2MAM-EXT-MIB", "hwPortVlanSecureMacAlarm"),
        ("HUAWEI-SWITCH-L2MAM-EXT-MIB", "hwSlotMacUsageFallingThreshold"),
        ("HUAWEI-SWITCH-L2MAM-EXT-MIB", "hwSlotMacUsageRaisingThreshold"),
        ("HUAWEI-SWITCH-L2MAM-EXT-MIB", "hwMacTrapHashConflictAlarm"))
)
if mibBuilder.loadTexts:
    hwL2MAMExtTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwSwitchL2MamExtFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 315, 4, 1, 1)
)
if mibBuilder.loadTexts:
    hwSwitchL2MamExtFullCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-SWITCH-L2MAM-EXT-MIB",
    **{"hwSWITCH-L2MAM-EXT": hwSWITCH_L2MAM_EXT,
       "hwSwitchL2MamExtObjects": hwSwitchL2MamExtObjects,
       "hwMacTrapPortCfgTable": hwMacTrapPortCfgTable,
       "hwMacTrapPortCfgEntry": hwMacTrapPortCfgEntry,
       "hwMacTrapPortCfgIfIndex": hwMacTrapPortCfgIfIndex,
       "hwMacTrapPortCfgLearn": hwMacTrapPortCfgLearn,
       "hwMacTrapPortCfgAging": hwMacTrapPortCfgAging,
       "hwSwitchL2MamExtGeneralObjects": hwSwitchL2MamExtGeneralObjects,
       "hwMacTrapInterval": hwMacTrapInterval,
       "hwMacTrapMacInfo": hwMacTrapMacInfo,
       "hwSwitchL2MamExtTraps": hwSwitchL2MamExtTraps,
       "hwMacTrapAlarm": hwMacTrapAlarm,
       "hwPortVlanSecureMacAlarm": hwPortVlanSecureMacAlarm,
       "hwSlotMacUsageRaisingThreshold": hwSlotMacUsageRaisingThreshold,
       "hwSlotMacUsageFallingThreshold": hwSlotMacUsageFallingThreshold,
       "hwMacTrapPortCfgAlarm": hwMacTrapPortCfgAlarm,
       "hwMacTrapHashConflictAlarm": hwMacTrapHashConflictAlarm,
       "hwSwitchL2MamExtConformance": hwSwitchL2MamExtConformance,
       "hwSwitchL2MamExtCompliances": hwSwitchL2MamExtCompliances,
       "hwSwitchL2MamExtFullCompliance": hwSwitchL2MamExtFullCompliance,
       "hwSwitchL2MamExtGroups": hwSwitchL2MamExtGroups,
       "hwMacTrapGroups": hwMacTrapGroups,
       "hwL2MAMExtGeneralGrops": hwL2MAMExtGeneralGrops,
       "hwL2MAMExtTrapGroup": hwL2MAMExtTrapGroup}
)
