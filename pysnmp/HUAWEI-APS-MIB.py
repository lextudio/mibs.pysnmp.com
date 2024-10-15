# SNMP MIB module (HUAWEI-APS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-APS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:02:45 2024
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

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysUpTime,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysUpTime")

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


# MODULE-IDENTITY

hwApsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 161)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwApsObjects_ObjectIdentity = ObjectIdentity
hwApsObjects = _HwApsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 161, 1)
)
_HwApsProtectionTable_Object = MibTable
hwApsProtectionTable = _HwApsProtectionTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 161, 1, 1)
)
if mibBuilder.loadTexts:
    hwApsProtectionTable.setStatus("current")
_HwApsProtectionEntry_Object = MibTableRow
hwApsProtectionEntry = _HwApsProtectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 161, 1, 1, 1)
)
hwApsProtectionEntry.setIndexNames(
    (0, "HUAWEI-APS-MIB", "hwApsIfIndex"),
)
if mibBuilder.loadTexts:
    hwApsProtectionEntry.setStatus("current")
_HwApsIfIndex_Type = InterfaceIndex
_HwApsIfIndex_Object = MibTableColumn
hwApsIfIndex = _HwApsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 161, 1, 1, 1, 1),
    _HwApsIfIndex_Type()
)
hwApsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwApsIfIndex.setStatus("current")


class _HwApsProtectionGroupNum_Type(Unsigned32):
    """Custom type hwApsProtectionGroupNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_HwApsProtectionGroupNum_Type.__name__ = "Unsigned32"
_HwApsProtectionGroupNum_Object = MibTableColumn
hwApsProtectionGroupNum = _HwApsProtectionGroupNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 161, 1, 1, 1, 2),
    _HwApsProtectionGroupNum_Type()
)
hwApsProtectionGroupNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApsProtectionGroupNum.setStatus("current")


class _HwApsIfType_Type(Integer32):
    """Custom type hwApsIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("protection", 2),
          ("work", 1))
    )


_HwApsIfType_Type.__name__ = "Integer32"
_HwApsIfType_Object = MibTableColumn
hwApsIfType = _HwApsIfType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 161, 1, 1, 1, 3),
    _HwApsIfType_Type()
)
hwApsIfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApsIfType.setStatus("current")


class _HwApsRestoreWaitTime_Type(Integer32):
    """Custom type hwApsRestoreWaitTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 12),
    )


_HwApsRestoreWaitTime_Type.__name__ = "Integer32"
_HwApsRestoreWaitTime_Object = MibTableColumn
hwApsRestoreWaitTime = _HwApsRestoreWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 161, 1, 1, 1, 4),
    _HwApsRestoreWaitTime_Type()
)
hwApsRestoreWaitTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApsRestoreWaitTime.setStatus("current")


class _HwApsProtectSwitch_Type(Integer32):
    """Custom type hwApsProtectSwitch based on Integer32"""
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
        *(("auto", 4),
          ("force", 2),
          ("lock", 1),
          ("manual", 3))
    )


_HwApsProtectSwitch_Type.__name__ = "Integer32"
_HwApsProtectSwitch_Object = MibTableColumn
hwApsProtectSwitch = _HwApsProtectSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 161, 1, 1, 1, 5),
    _HwApsProtectSwitch_Type()
)
hwApsProtectSwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApsProtectSwitch.setStatus("current")


class _HwApsWorkingIfType_Type(Integer32):
    """Custom type hwApsWorkingIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_HwApsWorkingIfType_Type.__name__ = "Integer32"
_HwApsWorkingIfType_Object = MibTableColumn
hwApsWorkingIfType = _HwApsWorkingIfType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 161, 1, 1, 1, 6),
    _HwApsWorkingIfType_Type()
)
hwApsWorkingIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApsWorkingIfType.setStatus("current")
_HwApsRowStatus_Type = RowStatus
_HwApsRowStatus_Object = MibTableColumn
hwApsRowStatus = _HwApsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 161, 1, 1, 1, 7),
    _HwApsRowStatus_Type()
)
hwApsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwApsRowStatus.setStatus("current")
_HwApsNotifications_ObjectIdentity = ObjectIdentity
hwApsNotifications = _HwApsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 161, 2)
)
_HwApsConformance_ObjectIdentity = ObjectIdentity
hwApsConformance = _HwApsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 161, 3)
)
_HwApsCompliances_ObjectIdentity = ObjectIdentity
hwApsCompliances = _HwApsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 161, 3, 1)
)
_HwApsGroups_ObjectIdentity = ObjectIdentity
hwApsGroups = _HwApsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 161, 3, 2)
)

# Managed Objects groups

hwApsProtectionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 161, 3, 2, 1)
)
hwApsProtectionGroup.setObjects(
      *(("HUAWEI-APS-MIB", "hwApsProtectionGroupNum"),
        ("HUAWEI-APS-MIB", "hwApsIfType"),
        ("HUAWEI-APS-MIB", "hwApsRestoreWaitTime"),
        ("HUAWEI-APS-MIB", "hwApsProtectSwitch"),
        ("HUAWEI-APS-MIB", "hwApsWorkingIfType"),
        ("HUAWEI-APS-MIB", "hwApsRowStatus"))
)
if mibBuilder.loadTexts:
    hwApsProtectionGroup.setStatus("current")


# Notification objects

hwApsProtectSwitchOver = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 161, 2, 1)
)
hwApsProtectSwitchOver.setObjects(
      *(("HUAWEI-APS-MIB", "hwApsProtectionGroupNum"),
        ("HUAWEI-APS-MIB", "hwApsIfType"),
        ("HUAWEI-APS-MIB", "hwApsWorkingIfType"))
)
if mibBuilder.loadTexts:
    hwApsProtectSwitchOver.setStatus(
        "current"
    )

hwApsProtectSwitchBackOver = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 161, 2, 2)
)
hwApsProtectSwitchBackOver.setObjects(
      *(("HUAWEI-APS-MIB", "hwApsProtectionGroupNum"),
        ("HUAWEI-APS-MIB", "hwApsIfType"),
        ("HUAWEI-APS-MIB", "hwApsWorkingIfType"))
)
if mibBuilder.loadTexts:
    hwApsProtectSwitchBackOver.setStatus(
        "current"
    )

hwApsProtectModeFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 161, 2, 3)
)
hwApsProtectModeFail.setObjects(
      *(("HUAWEI-APS-MIB", "hwApsProtectionGroupNum"),
        ("HUAWEI-APS-MIB", "hwApsIfType"),
        ("HUAWEI-APS-MIB", "hwApsWorkingIfType"))
)
if mibBuilder.loadTexts:
    hwApsProtectModeFail.setStatus(
        "current"
    )

hwApsProtectChnlFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 161, 2, 4)
)
hwApsProtectChnlFail.setObjects(
      *(("HUAWEI-APS-MIB", "hwApsProtectionGroupNum"),
        ("HUAWEI-APS-MIB", "hwApsIfType"),
        ("HUAWEI-APS-MIB", "hwApsWorkingIfType"))
)
if mibBuilder.loadTexts:
    hwApsProtectChnlFail.setStatus(
        "current"
    )

hwApsProtectInvldK1K2Fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 161, 2, 5)
)
hwApsProtectInvldK1K2Fail.setObjects(
      *(("HUAWEI-APS-MIB", "hwApsProtectionGroupNum"),
        ("HUAWEI-APS-MIB", "hwApsIfType"),
        ("HUAWEI-APS-MIB", "hwApsWorkingIfType"))
)
if mibBuilder.loadTexts:
    hwApsProtectInvldK1K2Fail.setStatus(
        "current"
    )

hwApsProtectRemoteFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 161, 2, 6)
)
hwApsProtectRemoteFail.setObjects(
      *(("HUAWEI-APS-MIB", "hwApsProtectionGroupNum"),
        ("HUAWEI-APS-MIB", "hwApsIfType"),
        ("HUAWEI-APS-MIB", "hwApsWorkingIfType"))
)
if mibBuilder.loadTexts:
    hwApsProtectRemoteFail.setStatus(
        "current"
    )


# Notifications groups

hwApsNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 161, 3, 2, 2)
)
hwApsNotificationsGroup.setObjects(
      *(("HUAWEI-APS-MIB", "hwApsProtectSwitchOver"),
        ("HUAWEI-APS-MIB", "hwApsProtectSwitchBackOver"),
        ("HUAWEI-APS-MIB", "hwApsProtectModeFail"),
        ("HUAWEI-APS-MIB", "hwApsProtectChnlFail"),
        ("HUAWEI-APS-MIB", "hwApsProtectInvldK1K2Fail"),
        ("HUAWEI-APS-MIB", "hwApsProtectRemoteFail"))
)
if mibBuilder.loadTexts:
    hwApsNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwApsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 161, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hwApsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-APS-MIB",
    **{"hwApsMIB": hwApsMIB,
       "hwApsObjects": hwApsObjects,
       "hwApsProtectionTable": hwApsProtectionTable,
       "hwApsProtectionEntry": hwApsProtectionEntry,
       "hwApsIfIndex": hwApsIfIndex,
       "hwApsProtectionGroupNum": hwApsProtectionGroupNum,
       "hwApsIfType": hwApsIfType,
       "hwApsRestoreWaitTime": hwApsRestoreWaitTime,
       "hwApsProtectSwitch": hwApsProtectSwitch,
       "hwApsWorkingIfType": hwApsWorkingIfType,
       "hwApsRowStatus": hwApsRowStatus,
       "hwApsNotifications": hwApsNotifications,
       "hwApsProtectSwitchOver": hwApsProtectSwitchOver,
       "hwApsProtectSwitchBackOver": hwApsProtectSwitchBackOver,
       "hwApsProtectModeFail": hwApsProtectModeFail,
       "hwApsProtectChnlFail": hwApsProtectChnlFail,
       "hwApsProtectInvldK1K2Fail": hwApsProtectInvldK1K2Fail,
       "hwApsProtectRemoteFail": hwApsProtectRemoteFail,
       "hwApsConformance": hwApsConformance,
       "hwApsCompliances": hwApsCompliances,
       "hwApsCompliance": hwApsCompliance,
       "hwApsGroups": hwApsGroups,
       "hwApsProtectionGroup": hwApsProtectionGroup,
       "hwApsNotificationsGroup": hwApsNotificationsGroup}
)
