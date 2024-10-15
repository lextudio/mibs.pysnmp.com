# SNMP MIB module (HUAWEI-MAC-AUTHEN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-MAC-AUTHEN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:04:51 2024
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

(InterfaceIndexOrZero,
 ifDescr) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifDescr")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(VlanIdOrNone,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIdOrNone")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hwMacAuthenMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 171)
)
hwMacAuthenMIB.setRevisions(
        ("2009-12-15 18:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwMacAuthenObjects_ObjectIdentity = ObjectIdentity
hwMacAuthenObjects = _HwMacAuthenObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 171, 1)
)
_HwMacAuthenGlobalEnable_Type = EnabledStatus
_HwMacAuthenGlobalEnable_Object = MibScalar
hwMacAuthenGlobalEnable = _HwMacAuthenGlobalEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 171, 1, 1),
    _HwMacAuthenGlobalEnable_Type()
)
hwMacAuthenGlobalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacAuthenGlobalEnable.setStatus("current")


class _HwMacAuthenModeUsername_Type(Integer32):
    """Custom type hwMacAuthenModeUsername based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 3),
          ("macAddressWithHyphen", 2),
          ("macAddressWithoutHyphen", 1))
    )


_HwMacAuthenModeUsername_Type.__name__ = "Integer32"
_HwMacAuthenModeUsername_Object = MibScalar
hwMacAuthenModeUsername = _HwMacAuthenModeUsername_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 171, 1, 2),
    _HwMacAuthenModeUsername_Type()
)
hwMacAuthenModeUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacAuthenModeUsername.setStatus("current")
_HwMacAuthenPassword_Type = DisplayString
_HwMacAuthenPassword_Object = MibScalar
hwMacAuthenPassword = _HwMacAuthenPassword_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 171, 1, 3),
    _HwMacAuthenPassword_Type()
)
hwMacAuthenPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacAuthenPassword.setStatus("current")
_HwMacAuthenUsername_Type = DisplayString
_HwMacAuthenUsername_Object = MibScalar
hwMacAuthenUsername = _HwMacAuthenUsername_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 171, 1, 4),
    _HwMacAuthenUsername_Type()
)
hwMacAuthenUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacAuthenUsername.setStatus("current")
_HwMacAuthenDomain_Type = DisplayString
_HwMacAuthenDomain_Object = MibScalar
hwMacAuthenDomain = _HwMacAuthenDomain_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 171, 1, 5),
    _HwMacAuthenDomain_Type()
)
hwMacAuthenDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacAuthenDomain.setStatus("current")


class _HwMacAuthenTimerOfflineDetect_Type(Integer32):
    """Custom type hwMacAuthenTimerOfflineDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 7200),
    )


_HwMacAuthenTimerOfflineDetect_Type.__name__ = "Integer32"
_HwMacAuthenTimerOfflineDetect_Object = MibScalar
hwMacAuthenTimerOfflineDetect = _HwMacAuthenTimerOfflineDetect_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 171, 1, 6),
    _HwMacAuthenTimerOfflineDetect_Type()
)
hwMacAuthenTimerOfflineDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacAuthenTimerOfflineDetect.setStatus("current")


class _HwMacAuthenTimerQuiet_Type(Integer32):
    """Custom type hwMacAuthenTimerQuiet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 3600),
    )


_HwMacAuthenTimerQuiet_Type.__name__ = "Integer32"
_HwMacAuthenTimerQuiet_Object = MibScalar
hwMacAuthenTimerQuiet = _HwMacAuthenTimerQuiet_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 171, 1, 7),
    _HwMacAuthenTimerQuiet_Type()
)
hwMacAuthenTimerQuiet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacAuthenTimerQuiet.setStatus("current")


class _HwMacAuthenTimerServerTimeout_Type(Integer32):
    """Custom type hwMacAuthenTimerServerTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_HwMacAuthenTimerServerTimeout_Type.__name__ = "Integer32"
_HwMacAuthenTimerServerTimeout_Object = MibScalar
hwMacAuthenTimerServerTimeout = _HwMacAuthenTimerServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 171, 1, 8),
    _HwMacAuthenTimerServerTimeout_Type()
)
hwMacAuthenTimerServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacAuthenTimerServerTimeout.setStatus("current")


class _HwMacAuthenReauthInterval_Type(Integer32):
    """Custom type hwMacAuthenReauthInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7200),
    )


_HwMacAuthenReauthInterval_Type.__name__ = "Integer32"
_HwMacAuthenReauthInterval_Object = MibScalar
hwMacAuthenReauthInterval = _HwMacAuthenReauthInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 171, 1, 9),
    _HwMacAuthenReauthInterval_Type()
)
hwMacAuthenReauthInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacAuthenReauthInterval.setStatus("current")
_HwMacAuthenCfgTable_Object = MibTable
hwMacAuthenCfgTable = _HwMacAuthenCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 171, 1, 10)
)
if mibBuilder.loadTexts:
    hwMacAuthenCfgTable.setStatus("current")
_HwMacAuthenCfgEntry_Object = MibTableRow
hwMacAuthenCfgEntry = _HwMacAuthenCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 171, 1, 10, 1)
)
hwMacAuthenCfgEntry.setIndexNames(
    (0, "HUAWEI-MAC-AUTHEN-MIB", "hwMacAuthenPortIndex"),
)
if mibBuilder.loadTexts:
    hwMacAuthenCfgEntry.setStatus("current")


class _HwMacAuthenPortIndex_Type(Integer32):
    """Custom type hwMacAuthenPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1280),
    )


_HwMacAuthenPortIndex_Type.__name__ = "Integer32"
_HwMacAuthenPortIndex_Object = MibTableColumn
hwMacAuthenPortIndex = _HwMacAuthenPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 171, 1, 10, 1, 1),
    _HwMacAuthenPortIndex_Type()
)
hwMacAuthenPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMacAuthenPortIndex.setStatus("current")


class _HwMacAuthenPortEnable_Type(EnabledStatus):
    """Custom type hwMacAuthenPortEnable based on EnabledStatus"""


_HwMacAuthenPortEnable_Object = MibTableColumn
hwMacAuthenPortEnable = _HwMacAuthenPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 171, 1, 10, 1, 2),
    _HwMacAuthenPortEnable_Type()
)
hwMacAuthenPortEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMacAuthenPortEnable.setStatus("current")
_HwMacAuthenGuestVlan_Type = VlanIdOrNone
_HwMacAuthenGuestVlan_Object = MibTableColumn
hwMacAuthenGuestVlan = _HwMacAuthenGuestVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 171, 1, 10, 1, 3),
    _HwMacAuthenGuestVlan_Type()
)
hwMacAuthenGuestVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMacAuthenGuestVlan.setStatus("current")


class _HwMacAuthenMaxUserNum_Type(Integer32):
    """Custom type hwMacAuthenMaxUserNum based on Integer32"""
    defaultValue = 256

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8192),
    )


_HwMacAuthenMaxUserNum_Type.__name__ = "Integer32"
_HwMacAuthenMaxUserNum_Object = MibTableColumn
hwMacAuthenMaxUserNum = _HwMacAuthenMaxUserNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 171, 1, 10, 1, 4),
    _HwMacAuthenMaxUserNum_Type()
)
hwMacAuthenMaxUserNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMacAuthenMaxUserNum.setStatus("current")
_HwMacAuthenPortDomain_Type = DisplayString
_HwMacAuthenPortDomain_Object = MibTableColumn
hwMacAuthenPortDomain = _HwMacAuthenPortDomain_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 171, 1, 10, 1, 5),
    _HwMacAuthenPortDomain_Type()
)
hwMacAuthenPortDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacAuthenPortDomain.setStatus("current")


class _HwMacAuthenPortModeUserName_Type(Integer32):
    """Custom type hwMacAuthenPortModeUserName based on Integer32"""
    defaultValue = 1

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
        *(("fixed", 4),
          ("macAddressWithHyphen", 3),
          ("macAddressWithoutHyphen", 2),
          ("obeyGlobalConfiguration", 1))
    )


_HwMacAuthenPortModeUserName_Type.__name__ = "Integer32"
_HwMacAuthenPortModeUserName_Object = MibTableColumn
hwMacAuthenPortModeUserName = _HwMacAuthenPortModeUserName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 171, 1, 10, 1, 6),
    _HwMacAuthenPortModeUserName_Type()
)
hwMacAuthenPortModeUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacAuthenPortModeUserName.setStatus("current")
_HwMacAuthenPortUserName_Type = DisplayString
_HwMacAuthenPortUserName_Object = MibTableColumn
hwMacAuthenPortUserName = _HwMacAuthenPortUserName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 171, 1, 10, 1, 7),
    _HwMacAuthenPortUserName_Type()
)
hwMacAuthenPortUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacAuthenPortUserName.setStatus("current")
_HwMacAuthenPortPassWord_Type = DisplayString
_HwMacAuthenPortPassWord_Object = MibTableColumn
hwMacAuthenPortPassWord = _HwMacAuthenPortPassWord_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 171, 1, 10, 1, 8),
    _HwMacAuthenPortPassWord_Type()
)
hwMacAuthenPortPassWord.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacAuthenPortPassWord.setStatus("current")


class _HwMacAuthenPortPwdType_Type(Integer32):
    """Custom type hwMacAuthenPortPwdType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cipher", 2),
          ("simple", 1))
    )


_HwMacAuthenPortPwdType_Type.__name__ = "Integer32"
_HwMacAuthenPortPwdType_Object = MibTableColumn
hwMacAuthenPortPwdType = _HwMacAuthenPortPwdType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 171, 1, 10, 1, 9),
    _HwMacAuthenPortPwdType_Type()
)
hwMacAuthenPortPwdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacAuthenPortPwdType.setStatus("current")


class _HwMacAuthenPwdType_Type(Integer32):
    """Custom type hwMacAuthenPwdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cipher", 2),
          ("simple", 1))
    )


_HwMacAuthenPwdType_Type.__name__ = "Integer32"
_HwMacAuthenPwdType_Object = MibScalar
hwMacAuthenPwdType = _HwMacAuthenPwdType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 171, 1, 11),
    _HwMacAuthenPwdType_Type()
)
hwMacAuthenPwdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacAuthenPwdType.setStatus("current")
_HwMacAuthenMibTraps_ObjectIdentity = ObjectIdentity
hwMacAuthenMibTraps = _HwMacAuthenMibTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 171, 2)
)
_HwMacAuthenConformance_ObjectIdentity = ObjectIdentity
hwMacAuthenConformance = _HwMacAuthenConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 171, 3)
)
_HwMacAuthenCompliances_ObjectIdentity = ObjectIdentity
hwMacAuthenCompliances = _HwMacAuthenCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 171, 3, 1)
)
_HwMacAuthenCfgGroups_ObjectIdentity = ObjectIdentity
hwMacAuthenCfgGroups = _HwMacAuthenCfgGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 171, 3, 2)
)

# Managed Objects groups

hwMacAuthenCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 171, 3, 2, 1)
)
hwMacAuthenCfgGroup.setObjects(
      *(("HUAWEI-MAC-AUTHEN-MIB", "hwMacAuthenGlobalEnable"),
        ("HUAWEI-MAC-AUTHEN-MIB", "hwMacAuthenModeUsername"),
        ("HUAWEI-MAC-AUTHEN-MIB", "hwMacAuthenPassword"),
        ("HUAWEI-MAC-AUTHEN-MIB", "hwMacAuthenUsername"),
        ("HUAWEI-MAC-AUTHEN-MIB", "hwMacAuthenDomain"),
        ("HUAWEI-MAC-AUTHEN-MIB", "hwMacAuthenTimerOfflineDetect"),
        ("HUAWEI-MAC-AUTHEN-MIB", "hwMacAuthenTimerQuiet"),
        ("HUAWEI-MAC-AUTHEN-MIB", "hwMacAuthenTimerServerTimeout"),
        ("HUAWEI-MAC-AUTHEN-MIB", "hwMacAuthenReauthInterval"),
        ("HUAWEI-MAC-AUTHEN-MIB", "hwMacAuthenPortEnable"),
        ("HUAWEI-MAC-AUTHEN-MIB", "hwMacAuthenGuestVlan"),
        ("HUAWEI-MAC-AUTHEN-MIB", "hwMacAuthenMaxUserNum"),
        ("HUAWEI-MAC-AUTHEN-MIB", "hwMacAuthenPortDomain"),
        ("HUAWEI-MAC-AUTHEN-MIB", "hwMacAuthenPortModeUserName"),
        ("HUAWEI-MAC-AUTHEN-MIB", "hwMacAuthenPortUserName"),
        ("HUAWEI-MAC-AUTHEN-MIB", "hwMacAuthenPortPassWord"),
        ("HUAWEI-MAC-AUTHEN-MIB", "hwMacAuthenPortPwdType"),
        ("HUAWEI-MAC-AUTHEN-MIB", "hwMacAuthenPwdType"))
)
if mibBuilder.loadTexts:
    hwMacAuthenCfgGroup.setStatus("current")


# Notification objects

hwMacAuthenMaxUserAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 171, 2, 1)
)
hwMacAuthenMaxUserAlarm.setObjects(
    ("IF-MIB", "ifDescr")
)
if mibBuilder.loadTexts:
    hwMacAuthenMaxUserAlarm.setStatus(
        "current"
    )


# Notifications groups

hwMacAuthenTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 171, 3, 2, 2)
)
hwMacAuthenTrapGroup.setObjects(
    ("HUAWEI-MAC-AUTHEN-MIB", "hwMacAuthenMaxUserAlarm")
)
if mibBuilder.loadTexts:
    hwMacAuthenTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwMacAuthenCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 171, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hwMacAuthenCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-MAC-AUTHEN-MIB",
    **{"hwMacAuthenMIB": hwMacAuthenMIB,
       "hwMacAuthenObjects": hwMacAuthenObjects,
       "hwMacAuthenGlobalEnable": hwMacAuthenGlobalEnable,
       "hwMacAuthenModeUsername": hwMacAuthenModeUsername,
       "hwMacAuthenPassword": hwMacAuthenPassword,
       "hwMacAuthenUsername": hwMacAuthenUsername,
       "hwMacAuthenDomain": hwMacAuthenDomain,
       "hwMacAuthenTimerOfflineDetect": hwMacAuthenTimerOfflineDetect,
       "hwMacAuthenTimerQuiet": hwMacAuthenTimerQuiet,
       "hwMacAuthenTimerServerTimeout": hwMacAuthenTimerServerTimeout,
       "hwMacAuthenReauthInterval": hwMacAuthenReauthInterval,
       "hwMacAuthenCfgTable": hwMacAuthenCfgTable,
       "hwMacAuthenCfgEntry": hwMacAuthenCfgEntry,
       "hwMacAuthenPortIndex": hwMacAuthenPortIndex,
       "hwMacAuthenPortEnable": hwMacAuthenPortEnable,
       "hwMacAuthenGuestVlan": hwMacAuthenGuestVlan,
       "hwMacAuthenMaxUserNum": hwMacAuthenMaxUserNum,
       "hwMacAuthenPortDomain": hwMacAuthenPortDomain,
       "hwMacAuthenPortModeUserName": hwMacAuthenPortModeUserName,
       "hwMacAuthenPortUserName": hwMacAuthenPortUserName,
       "hwMacAuthenPortPassWord": hwMacAuthenPortPassWord,
       "hwMacAuthenPortPwdType": hwMacAuthenPortPwdType,
       "hwMacAuthenPwdType": hwMacAuthenPwdType,
       "hwMacAuthenMibTraps": hwMacAuthenMibTraps,
       "hwMacAuthenMaxUserAlarm": hwMacAuthenMaxUserAlarm,
       "hwMacAuthenConformance": hwMacAuthenConformance,
       "hwMacAuthenCompliances": hwMacAuthenCompliances,
       "hwMacAuthenCompliance": hwMacAuthenCompliance,
       "hwMacAuthenCfgGroups": hwMacAuthenCfgGroups,
       "hwMacAuthenCfgGroup": hwMacAuthenCfgGroup,
       "hwMacAuthenTrapGroup": hwMacAuthenTrapGroup}
)
