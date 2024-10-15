# SNMP MIB module (HUAWEI-STACK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-STACK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:06:01 2024
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

(entPhysicalIndex,
 entPhysicalName) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex",
    "entPhysicalName")

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

huaweiStackMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183)
)
huaweiStackMIB.setRevisions(
        ("2015-08-07 09:25",
         "2015-06-24 09:25",
         "2015-04-15 09:25",
         "2015-03-06 09:25",
         "2015-02-15 09:25",
         "2015-02-10 14:25",
         "2014-12-17 14:25",
         "2014-10-25 14:25",
         "2014-10-21 15:21",
         "2014-09-18 16:50",
         "2014-09-01 14:34",
         "2014-08-19 21:09",
         "2014-08-04 17:11",
         "2014-07-11 15:58",
         "2014-06-21 15:13",
         "2014-06-18 13:48",
         "2014-06-13 16:17",
         "2014-06-09 10:43",
         "2014-04-14 00:00",
         "2014-03-18 17:30",
         "2014-03-04 15:10",
         "2014-02-24 18:31",
         "2014-02-22 10:24",
         "2014-02-19 00:00",
         "2014-01-26 10:44",
         "2014-01-14 14:59",
         "2014-01-13 15:54",
         "2013-12-31 08:45",
         "2013-12-24 09:22",
         "2013-12-10 11:22",
         "2013-12-06 13:00",
         "2013-11-08 15:36",
         "2013-11-06 19:38",
         "2013-11-05 15:37",
         "2013-10-11 09:31",
         "2013-04-20 17:03",
         "2013-03-28 14:35",
         "2012-08-30 09:36")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwStackObject_ObjectIdentity = ObjectIdentity
hwStackObject = _HwStackObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1)
)
_HwStackRun_Type = EnabledStatus
_HwStackRun_Object = MibScalar
hwStackRun = _HwStackRun_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 1),
    _HwStackRun_Type()
)
hwStackRun.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwStackRun.setStatus("current")


class _HwStackTopoType_Type(Integer32):
    """Custom type hwStackTopoType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("link", 2),
          ("ring", 1))
    )


_HwStackTopoType_Type.__name__ = "Integer32"
_HwStackTopoType_Object = MibScalar
hwStackTopoType = _HwStackTopoType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 2),
    _HwStackTopoType_Type()
)
hwStackTopoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStackTopoType.setStatus("current")


class _HwStackMacAddressSwitchTime_Type(Integer32):
    """Custom type hwStackMacAddressSwitchTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
        ValueRangeConstraint(255, 255),
    )


_HwStackMacAddressSwitchTime_Type.__name__ = "Integer32"
_HwStackMacAddressSwitchTime_Object = MibScalar
hwStackMacAddressSwitchTime = _HwStackMacAddressSwitchTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 3),
    _HwStackMacAddressSwitchTime_Type()
)
hwStackMacAddressSwitchTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwStackMacAddressSwitchTime.setStatus("current")
_HwStackSystemMac_Type = MacAddress
_HwStackSystemMac_Object = MibScalar
hwStackSystemMac = _HwStackSystemMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 4),
    _HwStackSystemMac_Type()
)
hwStackSystemMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStackSystemMac.setStatus("current")
_HwStackIsStackDevice_Type = TruthValue
_HwStackIsStackDevice_Object = MibScalar
hwStackIsStackDevice = _HwStackIsStackDevice_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 5),
    _HwStackIsStackDevice_Type()
)
hwStackIsStackDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStackIsStackDevice.setStatus("current")


class _HwStackReservedVlanId_Type(Integer32):
    """Custom type hwStackReservedVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HwStackReservedVlanId_Type.__name__ = "Integer32"
_HwStackReservedVlanId_Object = MibScalar
hwStackReservedVlanId = _HwStackReservedVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 6),
    _HwStackReservedVlanId_Type()
)
hwStackReservedVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwStackReservedVlanId.setStatus("current")


class _HwStackClearUnsupportCfg_Type(Integer32):
    """Custom type hwStackClearUnsupportCfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_HwStackClearUnsupportCfg_Type.__name__ = "Integer32"
_HwStackClearUnsupportCfg_Object = MibScalar
hwStackClearUnsupportCfg = _HwStackClearUnsupportCfg_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 7),
    _HwStackClearUnsupportCfg_Type()
)
hwStackClearUnsupportCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwStackClearUnsupportCfg.setStatus("current")


class _HwStackLinkAlarmThreshold_Type(Integer32):
    """Custom type hwStackLinkAlarmThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_HwStackLinkAlarmThreshold_Type.__name__ = "Integer32"
_HwStackLinkAlarmThreshold_Object = MibScalar
hwStackLinkAlarmThreshold = _HwStackLinkAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 8),
    _HwStackLinkAlarmThreshold_Type()
)
hwStackLinkAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwStackLinkAlarmThreshold.setStatus("current")


class _HwStackMemberThreshold_Type(Integer32):
    """Custom type hwStackMemberThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_HwStackMemberThreshold_Type.__name__ = "Integer32"
_HwStackMemberThreshold_Object = MibScalar
hwStackMemberThreshold = _HwStackMemberThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 9),
    _HwStackMemberThreshold_Type()
)
hwStackMemberThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStackMemberThreshold.setStatus("current")


class _HwStackMode_Type(Integer32):
    """Custom type hwStackMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("card", 1),
          ("serviceport", 2))
    )


_HwStackMode_Type.__name__ = "Integer32"
_HwStackMode_Object = MibScalar
hwStackMode = _HwStackMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 10),
    _HwStackMode_Type()
)
hwStackMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwStackMode.setStatus("current")


class _HwStackMemberSpec_Type(Integer32):
    """Custom type hwStackMemberSpec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HwStackMemberSpec_Type.__name__ = "Integer32"
_HwStackMemberSpec_Object = MibScalar
hwStackMemberSpec = _HwStackMemberSpec_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 11),
    _HwStackMemberSpec_Type()
)
hwStackMemberSpec.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwStackMemberSpec.setStatus("current")


class _HwStackMacAddressAlarmTime_Type(Integer32):
    """Custom type hwStackMacAddressAlarmTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
        ValueRangeConstraint(255, 255),
    )


_HwStackMacAddressAlarmTime_Type.__name__ = "Integer32"
_HwStackMacAddressAlarmTime_Object = MibScalar
hwStackMacAddressAlarmTime = _HwStackMacAddressAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 12),
    _HwStackMacAddressAlarmTime_Type()
)
hwStackMacAddressAlarmTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwStackMacAddressAlarmTime.setStatus("current")
_HwLeafMaxNumber_Type = Integer32
_HwLeafMaxNumber_Object = MibScalar
hwLeafMaxNumber = _HwLeafMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 13),
    _HwLeafMaxNumber_Type()
)
hwLeafMaxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLeafMaxNumber.setStatus("current")


class _HwFabricCurrentForwardModel_Type(Integer32):
    """Custom type hwFabricCurrentForwardModel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("centralized", 2),
          ("distributed", 1),
          ("hybrid", 3),
          ("unknown", 255))
    )


_HwFabricCurrentForwardModel_Type.__name__ = "Integer32"
_HwFabricCurrentForwardModel_Object = MibScalar
hwFabricCurrentForwardModel = _HwFabricCurrentForwardModel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 14),
    _HwFabricCurrentForwardModel_Type()
)
hwFabricCurrentForwardModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFabricCurrentForwardModel.setStatus("current")


class _HwFabricConfigForwardModel_Type(Integer32):
    """Custom type hwFabricConfigForwardModel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("centralized", 2),
          ("distributed", 1),
          ("hybrid", 3),
          ("unknown", 255))
    )


_HwFabricConfigForwardModel_Type.__name__ = "Integer32"
_HwFabricConfigForwardModel_Object = MibScalar
hwFabricConfigForwardModel = _HwFabricConfigForwardModel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 15),
    _HwFabricConfigForwardModel_Type()
)
hwFabricConfigForwardModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwFabricConfigForwardModel.setStatus("current")


class _HwLeafSingleHomedAlarmEnable_Type(Integer32):
    """Custom type hwLeafSingleHomedAlarmEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unknown", 255))
    )


_HwLeafSingleHomedAlarmEnable_Type.__name__ = "Integer32"
_HwLeafSingleHomedAlarmEnable_Object = MibScalar
hwLeafSingleHomedAlarmEnable = _HwLeafSingleHomedAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 16),
    _HwLeafSingleHomedAlarmEnable_Type()
)
hwLeafSingleHomedAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLeafSingleHomedAlarmEnable.setStatus("current")


class _HwFabricExcludeLeafType_Type(Integer32):
    """Custom type hwFabricExcludeLeafType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("ce5810ei", 1),
          ("default", 0),
          ("unknown", 255))
    )


_HwFabricExcludeLeafType_Type.__name__ = "Integer32"
_HwFabricExcludeLeafType_Object = MibScalar
hwFabricExcludeLeafType = _HwFabricExcludeLeafType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 17),
    _HwFabricExcludeLeafType_Type()
)
hwFabricExcludeLeafType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwFabricExcludeLeafType.setStatus("current")
_HwStackMemberInfoTable_Object = MibTable
hwStackMemberInfoTable = _HwStackMemberInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 20)
)
if mibBuilder.loadTexts:
    hwStackMemberInfoTable.setStatus("current")
_HwStackMemberInfoEntry_Object = MibTableRow
hwStackMemberInfoEntry = _HwStackMemberInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 20, 1)
)
hwStackMemberInfoEntry.setIndexNames(
    (0, "HUAWEI-STACK-MIB", "hwMemberCurrentStackId"),
)
if mibBuilder.loadTexts:
    hwStackMemberInfoEntry.setStatus("current")


class _HwMemberCurrentStackId_Type(Integer32):
    """Custom type hwMemberCurrentStackId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_HwMemberCurrentStackId_Type.__name__ = "Integer32"
_HwMemberCurrentStackId_Object = MibTableColumn
hwMemberCurrentStackId = _HwMemberCurrentStackId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 20, 1, 1),
    _HwMemberCurrentStackId_Type()
)
hwMemberCurrentStackId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMemberCurrentStackId.setStatus("current")


class _HwMemberStackPriority_Type(Integer32):
    """Custom type hwMemberStackPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_HwMemberStackPriority_Type.__name__ = "Integer32"
_HwMemberStackPriority_Object = MibTableColumn
hwMemberStackPriority = _HwMemberStackPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 20, 1, 2),
    _HwMemberStackPriority_Type()
)
hwMemberStackPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMemberStackPriority.setStatus("current")


class _HwMemberStackRole_Type(Integer32):
    """Custom type hwMemberStackRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 3),
          ("standby", 2))
    )


_HwMemberStackRole_Type.__name__ = "Integer32"
_HwMemberStackRole_Object = MibTableColumn
hwMemberStackRole = _HwMemberStackRole_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 20, 1, 3),
    _HwMemberStackRole_Type()
)
hwMemberStackRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMemberStackRole.setStatus("current")


class _HwMemberStackMacAddress_Type(OctetString):
    """Custom type hwMemberStackMacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwMemberStackMacAddress_Type.__name__ = "OctetString"
_HwMemberStackMacAddress_Object = MibTableColumn
hwMemberStackMacAddress = _HwMemberStackMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 20, 1, 4),
    _HwMemberStackMacAddress_Type()
)
hwMemberStackMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMemberStackMacAddress.setStatus("current")


class _HwMemberStackDeviceType_Type(OctetString):
    """Custom type hwMemberStackDeviceType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwMemberStackDeviceType_Type.__name__ = "OctetString"
_HwMemberStackDeviceType_Object = MibTableColumn
hwMemberStackDeviceType = _HwMemberStackDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 20, 1, 5),
    _HwMemberStackDeviceType_Type()
)
hwMemberStackDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMemberStackDeviceType.setStatus("current")


class _HwMemberConfigStackId_Type(Integer32):
    """Custom type hwMemberConfigStackId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_HwMemberConfigStackId_Type.__name__ = "Integer32"
_HwMemberConfigStackId_Object = MibTableColumn
hwMemberConfigStackId = _HwMemberConfigStackId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 20, 1, 6),
    _HwMemberConfigStackId_Type()
)
hwMemberConfigStackId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMemberConfigStackId.setStatus("current")
_HwMemberStackObjectId_Type = ObjectIdentifier
_HwMemberStackObjectId_Object = MibTableColumn
hwMemberStackObjectId = _HwMemberStackObjectId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 20, 1, 7),
    _HwMemberStackObjectId_Type()
)
hwMemberStackObjectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMemberStackObjectId.setStatus("current")
_HwStackPortTable_Object = MibTable
hwStackPortTable = _HwStackPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 21)
)
if mibBuilder.loadTexts:
    hwStackPortTable.setStatus("current")
_HwStackPortEntry_Object = MibTableRow
hwStackPortEntry = _HwStackPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 21, 1)
)
hwStackPortEntry.setIndexNames(
    (0, "HUAWEI-STACK-MIB", "hwStackPortStackId"),
    (0, "HUAWEI-STACK-MIB", "hwStackPortId"),
)
if mibBuilder.loadTexts:
    hwStackPortEntry.setStatus("current")


class _HwStackPortStackId_Type(Integer32):
    """Custom type hwStackPortStackId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_HwStackPortStackId_Type.__name__ = "Integer32"
_HwStackPortStackId_Object = MibTableColumn
hwStackPortStackId = _HwStackPortStackId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 21, 1, 1),
    _HwStackPortStackId_Type()
)
hwStackPortStackId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwStackPortStackId.setStatus("current")


class _HwStackPortId_Type(Integer32):
    """Custom type hwStackPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwStackPortId_Type.__name__ = "Integer32"
_HwStackPortId_Object = MibTableColumn
hwStackPortId = _HwStackPortId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 21, 1, 2),
    _HwStackPortId_Type()
)
hwStackPortId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwStackPortId.setStatus("current")


class _HwStackPortName_Type(OctetString):
    """Custom type hwStackPortName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HwStackPortName_Type.__name__ = "OctetString"
_HwStackPortName_Object = MibTableColumn
hwStackPortName = _HwStackPortName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 21, 1, 3),
    _HwStackPortName_Type()
)
hwStackPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStackPortName.setStatus("current")


class _HwStackNeighborInfo_Type(OctetString):
    """Custom type hwStackNeighborInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HwStackNeighborInfo_Type.__name__ = "OctetString"
_HwStackNeighborInfo_Object = MibTableColumn
hwStackNeighborInfo = _HwStackNeighborInfo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 21, 1, 4),
    _HwStackNeighborInfo_Type()
)
hwStackNeighborInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStackNeighborInfo.setStatus("current")


class _HwStackPortStatus_Type(Integer32):
    """Custom type hwStackPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_HwStackPortStatus_Type.__name__ = "Integer32"
_HwStackPortStatus_Object = MibTableColumn
hwStackPortStatus = _HwStackPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 21, 1, 5),
    _HwStackPortStatus_Type()
)
hwStackPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStackPortStatus.setStatus("current")
_HwStackEventsV2_ObjectIdentity = ObjectIdentity
hwStackEventsV2 = _HwStackEventsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 22)
)
_HwStackMemberPortEnableTable_Object = MibTable
hwStackMemberPortEnableTable = _HwStackMemberPortEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 23)
)
if mibBuilder.loadTexts:
    hwStackMemberPortEnableTable.setStatus("current")
_HwStackMemberPortEnableEntry_Object = MibTableRow
hwStackMemberPortEnableEntry = _HwStackMemberPortEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 23, 1)
)
hwStackMemberPortEnableEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    hwStackMemberPortEnableEntry.setStatus("current")


class _HwEnableStackMode_Type(Integer32):
    """Custom type hwEnableStackMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_HwEnableStackMode_Type.__name__ = "Integer32"
_HwEnableStackMode_Object = MibTableColumn
hwEnableStackMode = _HwEnableStackMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 23, 1, 1),
    _HwEnableStackMode_Type()
)
hwEnableStackMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEnableStackMode.setStatus("current")
_HwAddingPhyPortToStackPortTable_Object = MibTable
hwAddingPhyPortToStackPortTable = _HwAddingPhyPortToStackPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 24)
)
if mibBuilder.loadTexts:
    hwAddingPhyPortToStackPortTable.setStatus("current")
_HwAddingPhyPortToStackPortEntry_Object = MibTableRow
hwAddingPhyPortToStackPortEntry = _HwAddingPhyPortToStackPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 24, 1)
)
hwAddingPhyPortToStackPortEntry.setIndexNames(
    (0, "HUAWEI-STACK-MIB", "hwEnabledStackModePhyPortIndex"),
)
if mibBuilder.loadTexts:
    hwAddingPhyPortToStackPortEntry.setStatus("current")


class _HwEnabledStackModePhyPortIndex_Type(Integer32):
    """Custom type hwEnabledStackModePhyPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwEnabledStackModePhyPortIndex_Type.__name__ = "Integer32"
_HwEnabledStackModePhyPortIndex_Object = MibTableColumn
hwEnabledStackModePhyPortIndex = _HwEnabledStackModePhyPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 24, 1, 1),
    _HwEnabledStackModePhyPortIndex_Type()
)
hwEnabledStackModePhyPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnabledStackModePhyPortIndex.setStatus("current")


class _HwStackPortID_Type(Integer32):
    """Custom type hwStackPortID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("port1", 1),
          ("port2", 2),
          ("unjoinable", 3))
    )


_HwStackPortID_Type.__name__ = "Integer32"
_HwStackPortID_Object = MibTableColumn
hwStackPortID = _HwStackPortID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 24, 1, 2),
    _HwStackPortID_Type()
)
hwStackPortID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwStackPortID.setStatus("current")
_HwStackMemberInformationTable_Object = MibTable
hwStackMemberInformationTable = _HwStackMemberInformationTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 25)
)
if mibBuilder.loadTexts:
    hwStackMemberInformationTable.setStatus("current")
_HwStackMemberInformationEntry_Object = MibTableRow
hwStackMemberInformationEntry = _HwStackMemberInformationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 25, 1)
)
hwStackMemberInformationEntry.setIndexNames(
    (0, "HUAWEI-STACK-MIB", "hwStackIdIndex"),
)
if mibBuilder.loadTexts:
    hwStackMemberInformationEntry.setStatus("current")


class _HwStackIdIndex_Type(Integer32):
    """Custom type hwStackIdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_HwStackIdIndex_Type.__name__ = "Integer32"
_HwStackIdIndex_Object = MibTableColumn
hwStackIdIndex = _HwStackIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 25, 1, 1),
    _HwStackIdIndex_Type()
)
hwStackIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwStackIdIndex.setStatus("current")


class _HwStackPriority_Type(Integer32):
    """Custom type hwStackPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_HwStackPriority_Type.__name__ = "Integer32"
_HwStackPriority_Object = MibTableColumn
hwStackPriority = _HwStackPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 25, 1, 2),
    _HwStackPriority_Type()
)
hwStackPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwStackPriority.setStatus("current")


class _HwStackRole_Type(Integer32):
    """Custom type hwStackRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("leaf", 4),
          ("master", 1),
          ("slave", 3),
          ("spine", 5),
          ("standby", 2))
    )


_HwStackRole_Type.__name__ = "Integer32"
_HwStackRole_Object = MibTableColumn
hwStackRole = _HwStackRole_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 25, 1, 3),
    _HwStackRole_Type()
)
hwStackRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStackRole.setStatus("current")
_HwStackMacAddress_Type = MacAddress
_HwStackMacAddress_Object = MibTableColumn
hwStackMacAddress = _HwStackMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 25, 1, 4),
    _HwStackMacAddress_Type()
)
hwStackMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStackMacAddress.setStatus("current")


class _HwStackDeviceType_Type(OctetString):
    """Custom type hwStackDeviceType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwStackDeviceType_Type.__name__ = "OctetString"
_HwStackDeviceType_Object = MibTableColumn
hwStackDeviceType = _HwStackDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 25, 1, 5),
    _HwStackDeviceType_Type()
)
hwStackDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStackDeviceType.setStatus("current")


class _HwStackId_Type(Integer32):
    """Custom type hwStackId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_HwStackId_Type.__name__ = "Integer32"
_HwStackId_Object = MibTableColumn
hwStackId = _HwStackId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 25, 1, 6),
    _HwStackId_Type()
)
hwStackId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStackId.setStatus("current")


class _HwStackConfigId_Type(Integer32):
    """Custom type hwStackConfigId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 254),
    )


_HwStackConfigId_Type.__name__ = "Integer32"
_HwStackConfigId_Object = MibTableColumn
hwStackConfigId = _HwStackConfigId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 25, 1, 7),
    _HwStackConfigId_Type()
)
hwStackConfigId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwStackConfigId.setStatus("current")


class _HwStackSysOid_Type(OctetString):
    """Custom type hwStackSysOid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwStackSysOid_Type.__name__ = "OctetString"
_HwStackSysOid_Object = MibTableColumn
hwStackSysOid = _HwStackSysOid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 25, 1, 8),
    _HwStackSysOid_Type()
)
hwStackSysOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStackSysOid.setStatus("current")


class _HwStackDescription_Type(OctetString):
    """Custom type hwStackDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 81),
    )


_HwStackDescription_Type.__name__ = "OctetString"
_HwStackDescription_Object = MibTableColumn
hwStackDescription = _HwStackDescription_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 25, 1, 9),
    _HwStackDescription_Type()
)
hwStackDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwStackDescription.setStatus("current")


class _HwStackCurrentUplinkPort_Type(Integer32):
    """Custom type hwStackCurrentUplinkPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("autoNegotiation", 1),
          ("port2x40ge", 5),
          ("port4x10ge", 4),
          ("port4x40ge", 3),
          ("port8x10ge", 2),
          ("unknown", 255))
    )


_HwStackCurrentUplinkPort_Type.__name__ = "Integer32"
_HwStackCurrentUplinkPort_Object = MibTableColumn
hwStackCurrentUplinkPort = _HwStackCurrentUplinkPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 25, 1, 10),
    _HwStackCurrentUplinkPort_Type()
)
hwStackCurrentUplinkPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStackCurrentUplinkPort.setStatus("current")


class _HwStackConfigUplinkPort_Type(Integer32):
    """Custom type hwStackConfigUplinkPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("autoNegotiation", 1),
          ("port2x40ge", 5),
          ("port4x10ge", 4),
          ("port4x40ge", 3),
          ("port8x10ge", 2),
          ("unknown", 255))
    )


_HwStackConfigUplinkPort_Type.__name__ = "Integer32"
_HwStackConfigUplinkPort_Object = MibTableColumn
hwStackConfigUplinkPort = _HwStackConfigUplinkPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 25, 1, 11),
    _HwStackConfigUplinkPort_Type()
)
hwStackConfigUplinkPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwStackConfigUplinkPort.setStatus("current")


class _HwStackCurrentSwitchMode_Type(Integer32):
    """Custom type hwStackCurrentSwitchMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("autoNegotiation", 1),
          ("leaf", 2),
          ("stack", 3),
          ("unknown", 255))
    )


_HwStackCurrentSwitchMode_Type.__name__ = "Integer32"
_HwStackCurrentSwitchMode_Object = MibTableColumn
hwStackCurrentSwitchMode = _HwStackCurrentSwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 25, 1, 12),
    _HwStackCurrentSwitchMode_Type()
)
hwStackCurrentSwitchMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStackCurrentSwitchMode.setStatus("current")


class _HwStackConfigSwitchMode_Type(Integer32):
    """Custom type hwStackConfigSwitchMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("autoNegotiation", 1),
          ("leaf", 2),
          ("stack", 3),
          ("unknown", 255))
    )


_HwStackConfigSwitchMode_Type.__name__ = "Integer32"
_HwStackConfigSwitchMode_Object = MibTableColumn
hwStackConfigSwitchMode = _HwStackConfigSwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 25, 1, 13),
    _HwStackConfigSwitchMode_Type()
)
hwStackConfigSwitchMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwStackConfigSwitchMode.setStatus("current")
_HwAddingPhyPortToFabricPortTable_Object = MibTable
hwAddingPhyPortToFabricPortTable = _HwAddingPhyPortToFabricPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 26)
)
if mibBuilder.loadTexts:
    hwAddingPhyPortToFabricPortTable.setStatus("current")
_HwAddingPhyPortToFabricPortEntry_Object = MibTableRow
hwAddingPhyPortToFabricPortEntry = _HwAddingPhyPortToFabricPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 26, 1)
)
hwAddingPhyPortToFabricPortEntry.setIndexNames(
    (0, "HUAWEI-STACK-MIB", "hwEnabledStackModePortIndex"),
)
if mibBuilder.loadTexts:
    hwAddingPhyPortToFabricPortEntry.setStatus("current")


class _HwEnabledStackModePortIndex_Type(Integer32):
    """Custom type hwEnabledStackModePortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwEnabledStackModePortIndex_Type.__name__ = "Integer32"
_HwEnabledStackModePortIndex_Object = MibTableColumn
hwEnabledStackModePortIndex = _HwEnabledStackModePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 26, 1, 1),
    _HwEnabledStackModePortIndex_Type()
)
hwEnabledStackModePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnabledStackModePortIndex.setStatus("current")


class _HwFabricPortID_Type(Integer32):
    """Custom type hwFabricPortID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_HwFabricPortID_Type.__name__ = "Integer32"
_HwFabricPortID_Object = MibTableColumn
hwFabricPortID = _HwFabricPortID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 26, 1, 2),
    _HwFabricPortID_Type()
)
hwFabricPortID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwFabricPortID.setStatus("current")
_HwFabricPortTable_Object = MibTable
hwFabricPortTable = _HwFabricPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 27)
)
if mibBuilder.loadTexts:
    hwFabricPortTable.setStatus("current")
_HwFabricPortEntry_Object = MibTableRow
hwFabricPortEntry = _HwFabricPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 27, 1)
)
hwFabricPortEntry.setIndexNames(
    (0, "HUAWEI-STACK-MIB", "hwFabricPortIndex"),
)
if mibBuilder.loadTexts:
    hwFabricPortEntry.setStatus("current")


class _HwFabricPortIndex_Type(Integer32):
    """Custom type hwFabricPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwFabricPortIndex_Type.__name__ = "Integer32"
_HwFabricPortIndex_Object = MibTableColumn
hwFabricPortIndex = _HwFabricPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 27, 1, 1),
    _HwFabricPortIndex_Type()
)
hwFabricPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFabricPortIndex.setStatus("current")


class _HwFabricMemberID_Type(Integer32):
    """Custom type hwFabricMemberID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(101, 254),
    )


_HwFabricMemberID_Type.__name__ = "Integer32"
_HwFabricMemberID_Object = MibTableColumn
hwFabricMemberID = _HwFabricMemberID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 27, 1, 2),
    _HwFabricMemberID_Type()
)
hwFabricMemberID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwFabricMemberID.setStatus("current")


class _HwFabricLoadBalance_Type(Integer32):
    """Custom type hwFabricLoadBalance based on Integer32"""
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
        *(("destinationIp", 5),
          ("destinationMac", 2),
          ("sourceAndDestinationIp", 6),
          ("sourceAndDestinationMac", 3),
          ("sourceIp", 4),
          ("sourceMac", 1))
    )


_HwFabricLoadBalance_Type.__name__ = "Integer32"
_HwFabricLoadBalance_Object = MibTableColumn
hwFabricLoadBalance = _HwFabricLoadBalance_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 27, 1, 3),
    _HwFabricLoadBalance_Type()
)
hwFabricLoadBalance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwFabricLoadBalance.setStatus("current")


class _HwFabricProtocolState_Type(Integer32):
    """Custom type hwFabricProtocolState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_HwFabricProtocolState_Type.__name__ = "Integer32"
_HwFabricProtocolState_Object = MibTableColumn
hwFabricProtocolState = _HwFabricProtocolState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 27, 1, 4),
    _HwFabricProtocolState_Type()
)
hwFabricProtocolState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFabricProtocolState.setStatus("current")


class _HwFabricConfiguredLinkNum_Type(Integer32):
    """Custom type hwFabricConfiguredLinkNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_HwFabricConfiguredLinkNum_Type.__name__ = "Integer32"
_HwFabricConfiguredLinkNum_Object = MibTableColumn
hwFabricConfiguredLinkNum = _HwFabricConfiguredLinkNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 27, 1, 5),
    _HwFabricConfiguredLinkNum_Type()
)
hwFabricConfiguredLinkNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwFabricConfiguredLinkNum.setStatus("current")
_HwFabricPhyLinkTable_Object = MibTable
hwFabricPhyLinkTable = _HwFabricPhyLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 28)
)
if mibBuilder.loadTexts:
    hwFabricPhyLinkTable.setStatus("current")
_HwFabricPhyLinkEntry_Object = MibTableRow
hwFabricPhyLinkEntry = _HwFabricPhyLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 28, 1)
)
hwFabricPhyLinkEntry.setIndexNames(
    (0, "HUAWEI-STACK-MIB", "hwSpinePortIndex"),
)
if mibBuilder.loadTexts:
    hwFabricPhyLinkEntry.setStatus("current")
_HwSpinePortIndex_Type = Integer32
_HwSpinePortIndex_Object = MibTableColumn
hwSpinePortIndex = _HwSpinePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 28, 1, 1),
    _HwSpinePortIndex_Type()
)
hwSpinePortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSpinePortIndex.setStatus("current")


class _HwSpineStackId_Type(Integer32):
    """Custom type hwSpineStackId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HwSpineStackId_Type.__name__ = "Integer32"
_HwSpineStackId_Object = MibTableColumn
hwSpineStackId = _HwSpineStackId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 28, 1, 2),
    _HwSpineStackId_Type()
)
hwSpineStackId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSpineStackId.setStatus("current")


class _HwSpinePortName_Type(OctetString):
    """Custom type hwSpinePortName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HwSpinePortName_Type.__name__ = "OctetString"
_HwSpinePortName_Object = MibTableColumn
hwSpinePortName = _HwSpinePortName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 28, 1, 3),
    _HwSpinePortName_Type()
)
hwSpinePortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSpinePortName.setStatus("current")


class _HwSpinePortStatus_Type(Integer32):
    """Custom type hwSpinePortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_HwSpinePortStatus_Type.__name__ = "Integer32"
_HwSpinePortStatus_Object = MibTableColumn
hwSpinePortStatus = _HwSpinePortStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 28, 1, 4),
    _HwSpinePortStatus_Type()
)
hwSpinePortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSpinePortStatus.setStatus("current")
_HwLeafPortIndex_Type = Integer32
_HwLeafPortIndex_Object = MibTableColumn
hwLeafPortIndex = _HwLeafPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 28, 1, 5),
    _HwLeafPortIndex_Type()
)
hwLeafPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLeafPortIndex.setStatus("current")


class _HwLeafStackId_Type(Integer32):
    """Custom type hwLeafStackId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(101, 255),
    )


_HwLeafStackId_Type.__name__ = "Integer32"
_HwLeafStackId_Object = MibTableColumn
hwLeafStackId = _HwLeafStackId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 28, 1, 6),
    _HwLeafStackId_Type()
)
hwLeafStackId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLeafStackId.setStatus("current")


class _HwLeafPortName_Type(OctetString):
    """Custom type hwLeafPortName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HwLeafPortName_Type.__name__ = "OctetString"
_HwLeafPortName_Object = MibTableColumn
hwLeafPortName = _HwLeafPortName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 28, 1, 7),
    _HwLeafPortName_Type()
)
hwLeafPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLeafPortName.setStatus("current")


class _HwLeafPortStatus_Type(Integer32):
    """Custom type hwLeafPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("null", 3),
          ("up", 1))
    )


_HwLeafPortStatus_Type.__name__ = "Integer32"
_HwLeafPortStatus_Object = MibTableColumn
hwLeafPortStatus = _HwLeafPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 28, 1, 8),
    _HwLeafPortStatus_Type()
)
hwLeafPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLeafPortStatus.setStatus("current")
_HwStackUpgradeTable_Object = MibTable
hwStackUpgradeTable = _HwStackUpgradeTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 30)
)
if mibBuilder.loadTexts:
    hwStackUpgradeTable.setStatus("current")
_HwStackUpgradeEntry_Object = MibTableRow
hwStackUpgradeEntry = _HwStackUpgradeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 30, 1)
)
hwStackUpgradeEntry.setIndexNames(
    (0, "HUAWEI-STACK-MIB", "hwStackUpgradeIndex"),
)
if mibBuilder.loadTexts:
    hwStackUpgradeEntry.setStatus("current")


class _HwStackUpgradeIndex_Type(Integer32):
    """Custom type hwStackUpgradeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwStackUpgradeIndex_Type.__name__ = "Integer32"
_HwStackUpgradeIndex_Object = MibTableColumn
hwStackUpgradeIndex = _HwStackUpgradeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 30, 1, 1),
    _HwStackUpgradeIndex_Type()
)
hwStackUpgradeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwStackUpgradeIndex.setStatus("current")


class _HwStackUpgradeGrpType_Type(Integer32):
    """Custom type hwStackUpgradeGrpType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allMembers", 1),
          ("memberIdList", 2))
    )


_HwStackUpgradeGrpType_Type.__name__ = "Integer32"
_HwStackUpgradeGrpType_Object = MibTableColumn
hwStackUpgradeGrpType = _HwStackUpgradeGrpType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 30, 1, 2),
    _HwStackUpgradeGrpType_Type()
)
hwStackUpgradeGrpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwStackUpgradeGrpType.setStatus("current")


class _HwStackUpgradeGrpValue_Type(OctetString):
    """Custom type hwStackUpgradeGrpValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_HwStackUpgradeGrpValue_Type.__name__ = "OctetString"
_HwStackUpgradeGrpValue_Object = MibTableColumn
hwStackUpgradeGrpValue = _HwStackUpgradeGrpValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 30, 1, 3),
    _HwStackUpgradeGrpValue_Type()
)
hwStackUpgradeGrpValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwStackUpgradeGrpValue.setStatus("current")


class _HwStackUpgradeFileType_Type(Integer32):
    """Custom type hwStackUpgradeFileType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("patchFile", 2),
          ("startupFile", 1))
    )


_HwStackUpgradeFileType_Type.__name__ = "Integer32"
_HwStackUpgradeFileType_Object = MibTableColumn
hwStackUpgradeFileType = _HwStackUpgradeFileType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 30, 1, 4),
    _HwStackUpgradeFileType_Type()
)
hwStackUpgradeFileType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwStackUpgradeFileType.setStatus("current")
_HwStackUpgradeFileInfo_Type = OctetString
_HwStackUpgradeFileInfo_Object = MibTableColumn
hwStackUpgradeFileInfo = _HwStackUpgradeFileInfo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 30, 1, 5),
    _HwStackUpgradeFileInfo_Type()
)
hwStackUpgradeFileInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwStackUpgradeFileInfo.setStatus("current")


class _HwStackUpgradeFtpIp_Type(IpAddress):
    """Custom type hwStackUpgradeFtpIp based on IpAddress"""
    defaultHexValue = "FFFFFFFF"


_HwStackUpgradeFtpIp_Object = MibTableColumn
hwStackUpgradeFtpIp = _HwStackUpgradeFtpIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 30, 1, 6),
    _HwStackUpgradeFtpIp_Type()
)
hwStackUpgradeFtpIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwStackUpgradeFtpIp.setStatus("current")


class _HwStackUpgradeFtpUserName_Type(OctetString):
    """Custom type hwStackUpgradeFtpUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwStackUpgradeFtpUserName_Type.__name__ = "OctetString"
_HwStackUpgradeFtpUserName_Object = MibTableColumn
hwStackUpgradeFtpUserName = _HwStackUpgradeFtpUserName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 30, 1, 7),
    _HwStackUpgradeFtpUserName_Type()
)
hwStackUpgradeFtpUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwStackUpgradeFtpUserName.setStatus("current")


class _HwStackUpgradeFtpPassword_Type(OctetString):
    """Custom type hwStackUpgradeFtpPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwStackUpgradeFtpPassword_Type.__name__ = "OctetString"
_HwStackUpgradeFtpPassword_Object = MibTableColumn
hwStackUpgradeFtpPassword = _HwStackUpgradeFtpPassword_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 30, 1, 8),
    _HwStackUpgradeFtpPassword_Type()
)
hwStackUpgradeFtpPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwStackUpgradeFtpPassword.setStatus("current")


class _HwStackUpgradeServerPort_Type(Integer32):
    """Custom type hwStackUpgradeServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwStackUpgradeServerPort_Type.__name__ = "Integer32"
_HwStackUpgradeServerPort_Object = MibTableColumn
hwStackUpgradeServerPort = _HwStackUpgradeServerPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 30, 1, 9),
    _HwStackUpgradeServerPort_Type()
)
hwStackUpgradeServerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwStackUpgradeServerPort.setStatus("current")


class _HwStackUpgradeFileSize_Type(Integer32):
    """Custom type hwStackUpgradeFileSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwStackUpgradeFileSize_Type.__name__ = "Integer32"
_HwStackUpgradeFileSize_Object = MibTableColumn
hwStackUpgradeFileSize = _HwStackUpgradeFileSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 30, 1, 10),
    _HwStackUpgradeFileSize_Type()
)
hwStackUpgradeFileSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwStackUpgradeFileSize.setStatus("current")


class _HwStackUpgradeTransmitProtocol_Type(Integer32):
    """Custom type hwStackUpgradeTransmitProtocol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 1),
          ("sftp", 2),
          ("tftp", 3))
    )


_HwStackUpgradeTransmitProtocol_Type.__name__ = "Integer32"
_HwStackUpgradeTransmitProtocol_Object = MibTableColumn
hwStackUpgradeTransmitProtocol = _HwStackUpgradeTransmitProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 30, 1, 11),
    _HwStackUpgradeTransmitProtocol_Type()
)
hwStackUpgradeTransmitProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwStackUpgradeTransmitProtocol.setStatus("current")
_HwStackUpgradeRowStatus_Type = RowStatus
_HwStackUpgradeRowStatus_Object = MibTableColumn
hwStackUpgradeRowStatus = _HwStackUpgradeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 30, 1, 51),
    _HwStackUpgradeRowStatus_Type()
)
hwStackUpgradeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwStackUpgradeRowStatus.setStatus("current")
_HwStackUpgradeResultTable_Object = MibTable
hwStackUpgradeResultTable = _HwStackUpgradeResultTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 31)
)
if mibBuilder.loadTexts:
    hwStackUpgradeResultTable.setStatus("current")
_HwStackUpgradeResultEntry_Object = MibTableRow
hwStackUpgradeResultEntry = _HwStackUpgradeResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 31, 1)
)
hwStackUpgradeResultEntry.setIndexNames(
    (0, "HUAWEI-STACK-MIB", "hwStackUpgradeResultIndex"),
    (0, "HUAWEI-STACK-MIB", "hwStackUpgradeResultMemberId"),
)
if mibBuilder.loadTexts:
    hwStackUpgradeResultEntry.setStatus("current")


class _HwStackUpgradeResultIndex_Type(Integer32):
    """Custom type hwStackUpgradeResultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwStackUpgradeResultIndex_Type.__name__ = "Integer32"
_HwStackUpgradeResultIndex_Object = MibTableColumn
hwStackUpgradeResultIndex = _HwStackUpgradeResultIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 31, 1, 1),
    _HwStackUpgradeResultIndex_Type()
)
hwStackUpgradeResultIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwStackUpgradeResultIndex.setStatus("current")


class _HwStackUpgradeResultMemberId_Type(Integer32):
    """Custom type hwStackUpgradeResultMemberId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_HwStackUpgradeResultMemberId_Type.__name__ = "Integer32"
_HwStackUpgradeResultMemberId_Object = MibTableColumn
hwStackUpgradeResultMemberId = _HwStackUpgradeResultMemberId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 31, 1, 2),
    _HwStackUpgradeResultMemberId_Type()
)
hwStackUpgradeResultMemberId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStackUpgradeResultMemberId.setStatus("current")


class _HwStackUpgradeResult_Type(Integer32):
    """Custom type hwStackUpgradeResult based on Integer32"""
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
        *(("failure", 2),
          ("running", 3),
          ("success", 1),
          ("timeout", 4))
    )


_HwStackUpgradeResult_Type.__name__ = "Integer32"
_HwStackUpgradeResult_Object = MibTableColumn
hwStackUpgradeResult = _HwStackUpgradeResult_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 31, 1, 3),
    _HwStackUpgradeResult_Type()
)
hwStackUpgradeResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStackUpgradeResult.setStatus("current")


class _HwStackUpgradeResultInProcess_Type(Integer32):
    """Custom type hwStackUpgradeResultInProcess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwStackUpgradeResultInProcess_Type.__name__ = "Integer32"
_HwStackUpgradeResultInProcess_Object = MibTableColumn
hwStackUpgradeResultInProcess = _HwStackUpgradeResultInProcess_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 31, 1, 4),
    _HwStackUpgradeResultInProcess_Type()
)
hwStackUpgradeResultInProcess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStackUpgradeResultInProcess.setStatus("current")


class _HwStackUpgradeResultFailReason_Type(Integer32):
    """Custom type hwStackUpgradeResultFailReason based on Integer32"""
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
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("opDeviceBusy", 8),
          ("opFileChecksumError", 10),
          ("opFileTransferError", 9),
          ("opInvalidFileInfo", 4),
          ("opInvalidFileType", 5),
          ("opInvalidServerAddress", 6),
          ("opInvalidUserOrPassword", 7),
          ("opMasterDiskNoSpace", 2),
          ("opNoMemory", 11),
          ("opNonmasterDiskNoSpace", 3),
          ("opUnknownFailure", 14),
          ("opUpgradeDeviceAbsent", 13),
          ("opUpgradeInvalidValue", 15),
          ("opUpgradeSuccess", 1),
          ("opVersionFileNotMatch", 12))
    )


_HwStackUpgradeResultFailReason_Type.__name__ = "Integer32"
_HwStackUpgradeResultFailReason_Object = MibTableColumn
hwStackUpgradeResultFailReason = _HwStackUpgradeResultFailReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 31, 1, 5),
    _HwStackUpgradeResultFailReason_Type()
)
hwStackUpgradeResultFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStackUpgradeResultFailReason.setStatus("current")
_HwStackTrapObject_ObjectIdentity = ObjectIdentity
hwStackTrapObject = _HwStackTrapObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 32)
)
_HwStackLocalIfName_Type = OctetString
_HwStackLocalIfName_Object = MibScalar
hwStackLocalIfName = _HwStackLocalIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 32, 1),
    _HwStackLocalIfName_Type()
)
hwStackLocalIfName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwStackLocalIfName.setStatus("current")
_HwStackPeerIfName_Type = OctetString
_HwStackPeerIfName_Object = MibScalar
hwStackPeerIfName = _HwStackPeerIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 32, 2),
    _HwStackPeerIfName_Type()
)
hwStackPeerIfName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwStackPeerIfName.setStatus("current")
_HwStackConnectErrReason_Type = OctetString
_HwStackConnectErrReason_Object = MibScalar
hwStackConnectErrReason = _HwStackConnectErrReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 32, 3),
    _HwStackConnectErrReason_Type()
)
hwStackConnectErrReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwStackConnectErrReason.setStatus("current")
_HwConfigureFailedStackId_Type = OctetString
_HwConfigureFailedStackId_Object = MibScalar
hwConfigureFailedStackId = _HwConfigureFailedStackId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 32, 4),
    _HwConfigureFailedStackId_Type()
)
hwConfigureFailedStackId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwConfigureFailedStackId.setStatus("current")
_HwCssTrapErrorPortId_Type = OctetString
_HwCssTrapErrorPortId_Object = MibScalar
hwCssTrapErrorPortId = _HwCssTrapErrorPortId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 32, 5),
    _HwCssTrapErrorPortId_Type()
)
hwCssTrapErrorPortId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwCssTrapErrorPortId.setStatus("current")
_HwStackConnectMethod_Type = OctetString
_HwStackConnectMethod_Object = MibScalar
hwStackConnectMethod = _HwStackConnectMethod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 32, 6),
    _HwStackConnectMethod_Type()
)
hwStackConnectMethod.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwStackConnectMethod.setStatus("current")


class _HwStackCfgConflictStackId_Type(Integer32):
    """Custom type hwStackCfgConflictStackId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_HwStackCfgConflictStackId_Type.__name__ = "Integer32"
_HwStackCfgConflictStackId_Object = MibScalar
hwStackCfgConflictStackId = _HwStackCfgConflictStackId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 32, 7),
    _HwStackCfgConflictStackId_Type()
)
hwStackCfgConflictStackId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwStackCfgConflictStackId.setStatus("current")
_HwStackFabricPort_Type = OctetString
_HwStackFabricPort_Object = MibScalar
hwStackFabricPort = _HwStackFabricPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 32, 8),
    _HwStackFabricPort_Type()
)
hwStackFabricPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwStackFabricPort.setStatus("current")
_HwStackFabricMemberPort_Type = OctetString
_HwStackFabricMemberPort_Object = MibScalar
hwStackFabricMemberPort = _HwStackFabricMemberPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 32, 9),
    _HwStackFabricMemberPort_Type()
)
hwStackFabricMemberPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwStackFabricMemberPort.setStatus("current")


class _HwStackMemberId_Type(Integer32):
    """Custom type hwStackMemberId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_HwStackMemberId_Type.__name__ = "Integer32"
_HwStackMemberId_Object = MibScalar
hwStackMemberId = _HwStackMemberId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 32, 10),
    _HwStackMemberId_Type()
)
hwStackMemberId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwStackMemberId.setStatus("current")


class _HwStackLeafMemberId_Type(Integer32):
    """Custom type hwStackLeafMemberId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(101, 254),
    )


_HwStackLeafMemberId_Type.__name__ = "Integer32"
_HwStackLeafMemberId_Object = MibScalar
hwStackLeafMemberId = _HwStackLeafMemberId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 32, 11),
    _HwStackLeafMemberId_Type()
)
hwStackLeafMemberId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwStackLeafMemberId.setStatus("current")
_HwStackReason_Type = OctetString
_HwStackReason_Object = MibScalar
hwStackReason = _HwStackReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 32, 12),
    _HwStackReason_Type()
)
hwStackReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwStackReason.setStatus("current")
_HwStackLeafPort_Type = OctetString
_HwStackLeafPort_Object = MibScalar
hwStackLeafPort = _HwStackLeafPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 32, 13),
    _HwStackLeafPort_Type()
)
hwStackLeafPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwStackLeafPort.setStatus("current")
_HwStackCurrentLinkNum_Type = Integer32
_HwStackCurrentLinkNum_Object = MibScalar
hwStackCurrentLinkNum = _HwStackCurrentLinkNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 32, 14),
    _HwStackCurrentLinkNum_Type()
)
hwStackCurrentLinkNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwStackCurrentLinkNum.setStatus("current")
_HwFabricCurrentLinkNum_Type = Integer32
_HwFabricCurrentLinkNum_Object = MibScalar
hwFabricCurrentLinkNum = _HwFabricCurrentLinkNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 32, 15),
    _HwFabricCurrentLinkNum_Type()
)
hwFabricCurrentLinkNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwFabricCurrentLinkNum.setStatus("current")
_HwStackErrorDownRecoverReason_Type = OctetString
_HwStackErrorDownRecoverReason_Object = MibScalar
hwStackErrorDownRecoverReason = _HwStackErrorDownRecoverReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 32, 16),
    _HwStackErrorDownRecoverReason_Type()
)
hwStackErrorDownRecoverReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwStackErrorDownRecoverReason.setStatus("current")
_HwCssObject_ObjectIdentity = ObjectIdentity
hwCssObject = _HwCssObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3)
)
_HwCssGlobalObject_ObjectIdentity = ObjectIdentity
hwCssGlobalObject = _HwCssGlobalObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 1)
)
_HwCssEnable_Type = EnabledStatus
_HwCssEnable_Object = MibScalar
hwCssEnable = _HwCssEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 1, 1),
    _HwCssEnable_Type()
)
hwCssEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCssEnable.setStatus("current")
_HwCssMemberInfoTable_Object = MibTable
hwCssMemberInfoTable = _HwCssMemberInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 2)
)
if mibBuilder.loadTexts:
    hwCssMemberInfoTable.setStatus("current")
_HwCssMemberInfoEntry_Object = MibTableRow
hwCssMemberInfoEntry = _HwCssMemberInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 2, 1)
)
hwCssMemberInfoEntry.setIndexNames(
    (0, "HUAWEI-STACK-MIB", "hwCssMemberFrameId"),
)
if mibBuilder.loadTexts:
    hwCssMemberInfoEntry.setStatus("current")


class _HwCssMemberFrameId_Type(Integer32):
    """Custom type hwCssMemberFrameId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HwCssMemberFrameId_Type.__name__ = "Integer32"
_HwCssMemberFrameId_Object = MibTableColumn
hwCssMemberFrameId = _HwCssMemberFrameId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 2, 1, 1),
    _HwCssMemberFrameId_Type()
)
hwCssMemberFrameId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCssMemberFrameId.setStatus("current")


class _HwCssMemberConfigFrameId_Type(Integer32):
    """Custom type hwCssMemberConfigFrameId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwCssMemberConfigFrameId_Type.__name__ = "Integer32"
_HwCssMemberConfigFrameId_Object = MibTableColumn
hwCssMemberConfigFrameId = _HwCssMemberConfigFrameId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 2, 1, 2),
    _HwCssMemberConfigFrameId_Type()
)
hwCssMemberConfigFrameId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCssMemberConfigFrameId.setStatus("current")


class _HwCssMemberPriority_Type(Integer32):
    """Custom type hwCssMemberPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwCssMemberPriority_Type.__name__ = "Integer32"
_HwCssMemberPriority_Object = MibTableColumn
hwCssMemberPriority = _HwCssMemberPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 2, 1, 3),
    _HwCssMemberPriority_Type()
)
hwCssMemberPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCssMemberPriority.setStatus("current")


class _HwCssMemberConfigPriority_Type(Integer32):
    """Custom type hwCssMemberConfigPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwCssMemberConfigPriority_Type.__name__ = "Integer32"
_HwCssMemberConfigPriority_Object = MibTableColumn
hwCssMemberConfigPriority = _HwCssMemberConfigPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 2, 1, 4),
    _HwCssMemberConfigPriority_Type()
)
hwCssMemberConfigPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCssMemberConfigPriority.setStatus("current")


class _HwCssMemberMasterForce_Type(Integer32):
    """Custom type hwCssMemberMasterForce based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unknown", 255))
    )


_HwCssMemberMasterForce_Type.__name__ = "Integer32"
_HwCssMemberMasterForce_Object = MibTableColumn
hwCssMemberMasterForce = _HwCssMemberMasterForce_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 2, 1, 5),
    _HwCssMemberMasterForce_Type()
)
hwCssMemberMasterForce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCssMemberMasterForce.setStatus("current")


class _HwCssMemberConfigMasterForce_Type(Integer32):
    """Custom type hwCssMemberConfigMasterForce based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unknown", 255))
    )


_HwCssMemberConfigMasterForce_Type.__name__ = "Integer32"
_HwCssMemberConfigMasterForce_Object = MibTableColumn
hwCssMemberConfigMasterForce = _HwCssMemberConfigMasterForce_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 2, 1, 6),
    _HwCssMemberConfigMasterForce_Type()
)
hwCssMemberConfigMasterForce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCssMemberConfigMasterForce.setStatus("current")


class _HwCssMemberConfigEnable_Type(Integer32):
    """Custom type hwCssMemberConfigEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unknown", 255))
    )


_HwCssMemberConfigEnable_Type.__name__ = "Integer32"
_HwCssMemberConfigEnable_Object = MibTableColumn
hwCssMemberConfigEnable = _HwCssMemberConfigEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 2, 1, 7),
    _HwCssMemberConfigEnable_Type()
)
hwCssMemberConfigEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCssMemberConfigEnable.setStatus("current")


class _HwCssMemberRole_Type(Integer32):
    """Custom type hwCssMemberRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              10)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("single", 4),
          ("slave", 3),
          ("standby", 2),
          ("unknown", 10))
    )


_HwCssMemberRole_Type.__name__ = "Integer32"
_HwCssMemberRole_Object = MibTableColumn
hwCssMemberRole = _HwCssMemberRole_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 2, 1, 8),
    _HwCssMemberRole_Type()
)
hwCssMemberRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCssMemberRole.setStatus("current")
_HwCssTrap_ObjectIdentity = ObjectIdentity
hwCssTrap = _HwCssTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 3)
)
_HwCssTrapObjects_ObjectIdentity = ObjectIdentity
hwCssTrapObjects = _HwCssTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 3, 1)
)
_HwCssTrapFrameId1_Type = Integer32
_HwCssTrapFrameId1_Object = MibScalar
hwCssTrapFrameId1 = _HwCssTrapFrameId1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 3, 1, 1),
    _HwCssTrapFrameId1_Type()
)
hwCssTrapFrameId1.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwCssTrapFrameId1.setStatus("current")
_HwCssTrapSlotId1_Type = Integer32
_HwCssTrapSlotId1_Object = MibScalar
hwCssTrapSlotId1 = _HwCssTrapSlotId1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 3, 1, 2),
    _HwCssTrapSlotId1_Type()
)
hwCssTrapSlotId1.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwCssTrapSlotId1.setStatus("current")
_HwCssTrapPortId1_Type = Integer32
_HwCssTrapPortId1_Object = MibScalar
hwCssTrapPortId1 = _HwCssTrapPortId1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 3, 1, 3),
    _HwCssTrapPortId1_Type()
)
hwCssTrapPortId1.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwCssTrapPortId1.setStatus("current")
_HwCssTrapFrameId2_Type = Integer32
_HwCssTrapFrameId2_Object = MibScalar
hwCssTrapFrameId2 = _HwCssTrapFrameId2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 3, 1, 4),
    _HwCssTrapFrameId2_Type()
)
hwCssTrapFrameId2.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwCssTrapFrameId2.setStatus("current")
_HwCssTrapSlotId2_Type = Integer32
_HwCssTrapSlotId2_Object = MibScalar
hwCssTrapSlotId2 = _HwCssTrapSlotId2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 3, 1, 5),
    _HwCssTrapSlotId2_Type()
)
hwCssTrapSlotId2.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwCssTrapSlotId2.setStatus("current")
_HwCssTrapPortId2_Type = Integer32
_HwCssTrapPortId2_Object = MibScalar
hwCssTrapPortId2 = _HwCssTrapPortId2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 3, 1, 6),
    _HwCssTrapPortId2_Type()
)
hwCssTrapPortId2.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwCssTrapPortId2.setStatus("current")
_HwCssTrapFrameId3_Type = Integer32
_HwCssTrapFrameId3_Object = MibScalar
hwCssTrapFrameId3 = _HwCssTrapFrameId3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 3, 1, 7),
    _HwCssTrapFrameId3_Type()
)
hwCssTrapFrameId3.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwCssTrapFrameId3.setStatus("current")
_HwCssTrapSlotId3_Type = Integer32
_HwCssTrapSlotId3_Object = MibScalar
hwCssTrapSlotId3 = _HwCssTrapSlotId3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 3, 1, 8),
    _HwCssTrapSlotId3_Type()
)
hwCssTrapSlotId3.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwCssTrapSlotId3.setStatus("current")
_HwCssTrapPortId3_Type = Integer32
_HwCssTrapPortId3_Object = MibScalar
hwCssTrapPortId3 = _HwCssTrapPortId3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 3, 1, 9),
    _HwCssTrapPortId3_Type()
)
hwCssTrapPortId3.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwCssTrapPortId3.setStatus("current")
_HwCssTrapConfigureFailedSlotId_Type = OctetString
_HwCssTrapConfigureFailedSlotId_Object = MibScalar
hwCssTrapConfigureFailedSlotId = _HwCssTrapConfigureFailedSlotId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 3, 1, 10),
    _HwCssTrapConfigureFailedSlotId_Type()
)
hwCssTrapConfigureFailedSlotId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwCssTrapConfigureFailedSlotId.setStatus("current")
_HwCssTraps_ObjectIdentity = ObjectIdentity
hwCssTraps = _HwCssTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 3, 2)
)
_HwCssPortInfoTable_Object = MibTable
hwCssPortInfoTable = _HwCssPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 4)
)
if mibBuilder.loadTexts:
    hwCssPortInfoTable.setStatus("current")
_HwCssPortInfoEntry_Object = MibTableRow
hwCssPortInfoEntry = _HwCssPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 4, 1)
)
hwCssPortInfoEntry.setIndexNames(
    (0, "HUAWEI-STACK-MIB", "hwCssPortFrameId"),
    (0, "HUAWEI-STACK-MIB", "hwCssPortSlotId"),
    (0, "HUAWEI-STACK-MIB", "hwCssPortCardId"),
    (0, "HUAWEI-STACK-MIB", "hwCssPortPortId"),
    (0, "HUAWEI-STACK-MIB", "hwCssPortName"),
)
if mibBuilder.loadTexts:
    hwCssPortInfoEntry.setStatus("current")


class _HwCssPortFrameId_Type(Integer32):
    """Custom type hwCssPortFrameId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_HwCssPortFrameId_Type.__name__ = "Integer32"
_HwCssPortFrameId_Object = MibTableColumn
hwCssPortFrameId = _HwCssPortFrameId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 4, 1, 1),
    _HwCssPortFrameId_Type()
)
hwCssPortFrameId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwCssPortFrameId.setStatus("current")


class _HwCssPortSlotId_Type(Integer32):
    """Custom type hwCssPortSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HwCssPortSlotId_Type.__name__ = "Integer32"
_HwCssPortSlotId_Object = MibTableColumn
hwCssPortSlotId = _HwCssPortSlotId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 4, 1, 2),
    _HwCssPortSlotId_Type()
)
hwCssPortSlotId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwCssPortSlotId.setStatus("current")


class _HwCssPortCardId_Type(Integer32):
    """Custom type hwCssPortCardId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwCssPortCardId_Type.__name__ = "Integer32"
_HwCssPortCardId_Object = MibTableColumn
hwCssPortCardId = _HwCssPortCardId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 4, 1, 3),
    _HwCssPortCardId_Type()
)
hwCssPortCardId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwCssPortCardId.setStatus("current")


class _HwCssPortPortId_Type(Integer32):
    """Custom type hwCssPortPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_HwCssPortPortId_Type.__name__ = "Integer32"
_HwCssPortPortId_Object = MibTableColumn
hwCssPortPortId = _HwCssPortPortId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 4, 1, 4),
    _HwCssPortPortId_Type()
)
hwCssPortPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwCssPortPortId.setStatus("current")
_HwCssPortName_Type = OctetString
_HwCssPortName_Object = MibTableColumn
hwCssPortName = _HwCssPortName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 4, 1, 5),
    _HwCssPortName_Type()
)
hwCssPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCssPortName.setStatus("current")
_HwCssPortSpeed_Type = OctetString
_HwCssPortSpeed_Object = MibTableColumn
hwCssPortSpeed = _HwCssPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 4, 1, 6),
    _HwCssPortSpeed_Type()
)
hwCssPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCssPortSpeed.setStatus("current")


class _HwCssPortOperStatus_Type(Integer32):
    """Custom type hwCssPortOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_HwCssPortOperStatus_Type.__name__ = "Integer32"
_HwCssPortOperStatus_Object = MibTableColumn
hwCssPortOperStatus = _HwCssPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 4, 1, 7),
    _HwCssPortOperStatus_Type()
)
hwCssPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCssPortOperStatus.setStatus("current")


class _HwCssPortAdminStatus_Type(Integer32):
    """Custom type hwCssPortAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("shutdown", 1),
          ("undoshutdown", 0))
    )


_HwCssPortAdminStatus_Type.__name__ = "Integer32"
_HwCssPortAdminStatus_Object = MibTableColumn
hwCssPortAdminStatus = _HwCssPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 4, 1, 8),
    _HwCssPortAdminStatus_Type()
)
hwCssPortAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCssPortAdminStatus.setStatus("current")
_HwCssPortInOctets_Type = Counter64
_HwCssPortInOctets_Object = MibTableColumn
hwCssPortInOctets = _HwCssPortInOctets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 4, 1, 9),
    _HwCssPortInOctets_Type()
)
hwCssPortInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCssPortInOctets.setStatus("current")
_HwCssPortInUcastPkts_Type = Counter64
_HwCssPortInUcastPkts_Object = MibTableColumn
hwCssPortInUcastPkts = _HwCssPortInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 4, 1, 10),
    _HwCssPortInUcastPkts_Type()
)
hwCssPortInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCssPortInUcastPkts.setStatus("current")
_HwCssPortInMcastPkts_Type = Counter64
_HwCssPortInMcastPkts_Object = MibTableColumn
hwCssPortInMcastPkts = _HwCssPortInMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 4, 1, 11),
    _HwCssPortInMcastPkts_Type()
)
hwCssPortInMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCssPortInMcastPkts.setStatus("current")
_HwCssPortInBcastPkts_Type = Counter64
_HwCssPortInBcastPkts_Object = MibTableColumn
hwCssPortInBcastPkts = _HwCssPortInBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 4, 1, 12),
    _HwCssPortInBcastPkts_Type()
)
hwCssPortInBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCssPortInBcastPkts.setStatus("current")
_HwCssPortInDiscards_Type = Counter64
_HwCssPortInDiscards_Object = MibTableColumn
hwCssPortInDiscards = _HwCssPortInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 4, 1, 13),
    _HwCssPortInDiscards_Type()
)
hwCssPortInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCssPortInDiscards.setStatus("current")
_HwCssPortInErrors_Type = Counter64
_HwCssPortInErrors_Object = MibTableColumn
hwCssPortInErrors = _HwCssPortInErrors_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 4, 1, 14),
    _HwCssPortInErrors_Type()
)
hwCssPortInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCssPortInErrors.setStatus("current")
_HwCssPortInCRCErrors_Type = Counter64
_HwCssPortInCRCErrors_Object = MibTableColumn
hwCssPortInCRCErrors = _HwCssPortInCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 4, 1, 15),
    _HwCssPortInCRCErrors_Type()
)
hwCssPortInCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCssPortInCRCErrors.setStatus("current")
_HwCssPortOutOctets_Type = Counter64
_HwCssPortOutOctets_Object = MibTableColumn
hwCssPortOutOctets = _HwCssPortOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 4, 1, 16),
    _HwCssPortOutOctets_Type()
)
hwCssPortOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCssPortOutOctets.setStatus("current")
_HwCssPortOutUcastPkts_Type = Counter64
_HwCssPortOutUcastPkts_Object = MibTableColumn
hwCssPortOutUcastPkts = _HwCssPortOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 4, 1, 17),
    _HwCssPortOutUcastPkts_Type()
)
hwCssPortOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCssPortOutUcastPkts.setStatus("current")
_HwCssPortOutMcastPkts_Type = Counter64
_HwCssPortOutMcastPkts_Object = MibTableColumn
hwCssPortOutMcastPkts = _HwCssPortOutMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 4, 1, 18),
    _HwCssPortOutMcastPkts_Type()
)
hwCssPortOutMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCssPortOutMcastPkts.setStatus("current")
_HwCssPortOutBcastPkts_Type = Counter64
_HwCssPortOutBcastPkts_Object = MibTableColumn
hwCssPortOutBcastPkts = _HwCssPortOutBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 4, 1, 19),
    _HwCssPortOutBcastPkts_Type()
)
hwCssPortOutBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCssPortOutBcastPkts.setStatus("current")
_HwCssPortOutDiscards_Type = Counter64
_HwCssPortOutDiscards_Object = MibTableColumn
hwCssPortOutDiscards = _HwCssPortOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 4, 1, 20),
    _HwCssPortOutDiscards_Type()
)
hwCssPortOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCssPortOutDiscards.setStatus("current")
_HwCssPortOutErrors_Type = Counter64
_HwCssPortOutErrors_Object = MibTableColumn
hwCssPortOutErrors = _HwCssPortOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 4, 1, 21),
    _HwCssPortOutErrors_Type()
)
hwCssPortOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCssPortOutErrors.setStatus("current")
_HwCssLinkInfoTable_Object = MibTable
hwCssLinkInfoTable = _HwCssLinkInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 5)
)
if mibBuilder.loadTexts:
    hwCssLinkInfoTable.setStatus("current")
_HwCssLinkInfoEntry_Object = MibTableRow
hwCssLinkInfoEntry = _HwCssLinkInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 5, 1)
)
hwCssLinkInfoEntry.setIndexNames(
    (0, "HUAWEI-STACK-MIB", "hwCssLinkLocFrameId"),
    (0, "HUAWEI-STACK-MIB", "hwCssLinkLocSlotId"),
    (0, "HUAWEI-STACK-MIB", "hwCssLinkLocCardId"),
    (0, "HUAWEI-STACK-MIB", "hwCssLinkLocPortId"),
)
if mibBuilder.loadTexts:
    hwCssLinkInfoEntry.setStatus("current")


class _HwCssLinkLocFrameId_Type(Integer32):
    """Custom type hwCssLinkLocFrameId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_HwCssLinkLocFrameId_Type.__name__ = "Integer32"
_HwCssLinkLocFrameId_Object = MibTableColumn
hwCssLinkLocFrameId = _HwCssLinkLocFrameId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 5, 1, 1),
    _HwCssLinkLocFrameId_Type()
)
hwCssLinkLocFrameId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwCssLinkLocFrameId.setStatus("current")


class _HwCssLinkLocSlotId_Type(Integer32):
    """Custom type hwCssLinkLocSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HwCssLinkLocSlotId_Type.__name__ = "Integer32"
_HwCssLinkLocSlotId_Object = MibTableColumn
hwCssLinkLocSlotId = _HwCssLinkLocSlotId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 5, 1, 2),
    _HwCssLinkLocSlotId_Type()
)
hwCssLinkLocSlotId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwCssLinkLocSlotId.setStatus("current")


class _HwCssLinkLocCardId_Type(Integer32):
    """Custom type hwCssLinkLocCardId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwCssLinkLocCardId_Type.__name__ = "Integer32"
_HwCssLinkLocCardId_Object = MibTableColumn
hwCssLinkLocCardId = _HwCssLinkLocCardId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 5, 1, 3),
    _HwCssLinkLocCardId_Type()
)
hwCssLinkLocCardId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwCssLinkLocCardId.setStatus("current")


class _HwCssLinkLocPortId_Type(Integer32):
    """Custom type hwCssLinkLocPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_HwCssLinkLocPortId_Type.__name__ = "Integer32"
_HwCssLinkLocPortId_Object = MibTableColumn
hwCssLinkLocPortId = _HwCssLinkLocPortId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 5, 1, 4),
    _HwCssLinkLocPortId_Type()
)
hwCssLinkLocPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwCssLinkLocPortId.setStatus("current")
_HwCssLinkLocPortName_Type = OctetString
_HwCssLinkLocPortName_Object = MibTableColumn
hwCssLinkLocPortName = _HwCssLinkLocPortName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 5, 1, 5),
    _HwCssLinkLocPortName_Type()
)
hwCssLinkLocPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCssLinkLocPortName.setStatus("current")


class _HwCssLinkRemFrameId_Type(Integer32):
    """Custom type hwCssLinkRemFrameId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_HwCssLinkRemFrameId_Type.__name__ = "Integer32"
_HwCssLinkRemFrameId_Object = MibTableColumn
hwCssLinkRemFrameId = _HwCssLinkRemFrameId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 5, 1, 6),
    _HwCssLinkRemFrameId_Type()
)
hwCssLinkRemFrameId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCssLinkRemFrameId.setStatus("current")


class _HwCssLinkRemSlotId_Type(Integer32):
    """Custom type hwCssLinkRemSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HwCssLinkRemSlotId_Type.__name__ = "Integer32"
_HwCssLinkRemSlotId_Object = MibTableColumn
hwCssLinkRemSlotId = _HwCssLinkRemSlotId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 5, 1, 7),
    _HwCssLinkRemSlotId_Type()
)
hwCssLinkRemSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCssLinkRemSlotId.setStatus("current")


class _HwCssLinkRemCardId_Type(Integer32):
    """Custom type hwCssLinkRemCardId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwCssLinkRemCardId_Type.__name__ = "Integer32"
_HwCssLinkRemCardId_Object = MibTableColumn
hwCssLinkRemCardId = _HwCssLinkRemCardId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 5, 1, 8),
    _HwCssLinkRemCardId_Type()
)
hwCssLinkRemCardId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCssLinkRemCardId.setStatus("current")


class _HwCssLinkRemPortId_Type(Integer32):
    """Custom type hwCssLinkRemPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_HwCssLinkRemPortId_Type.__name__ = "Integer32"
_HwCssLinkRemPortId_Object = MibTableColumn
hwCssLinkRemPortId = _HwCssLinkRemPortId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 5, 1, 9),
    _HwCssLinkRemPortId_Type()
)
hwCssLinkRemPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCssLinkRemPortId.setStatus("current")
_HwCssLinkRemPortName_Type = OctetString
_HwCssLinkRemPortName_Object = MibTableColumn
hwCssLinkRemPortName = _HwCssLinkRemPortName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 5, 1, 10),
    _HwCssLinkRemPortName_Type()
)
hwCssLinkRemPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCssLinkRemPortName.setStatus("current")
_HwCssLinkSpeed_Type = OctetString
_HwCssLinkSpeed_Object = MibTableColumn
hwCssLinkSpeed = _HwCssLinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 5, 1, 11),
    _HwCssLinkSpeed_Type()
)
hwCssLinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCssLinkSpeed.setStatus("current")
_HwStackConformance_ObjectIdentity = ObjectIdentity
hwStackConformance = _HwStackConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 100)
)
_HwStackCompliances_ObjectIdentity = ObjectIdentity
hwStackCompliances = _HwStackCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 100, 1)
)
_HwStackGroups_ObjectIdentity = ObjectIdentity
hwStackGroups = _HwStackGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 100, 1, 2)
)
_HwCssConformance_ObjectIdentity = ObjectIdentity
hwCssConformance = _HwCssConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 101)
)
_HwCssCompliances_ObjectIdentity = ObjectIdentity
hwCssCompliances = _HwCssCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 101, 1)
)
_HwCssGroups_ObjectIdentity = ObjectIdentity
hwCssGroups = _HwCssGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 101, 1, 2)
)

# Managed Objects groups

hwStackObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 100, 1, 2, 1)
)
hwStackObjectGroup.setObjects(
      *(("HUAWEI-STACK-MIB", "hwStackRun"),
        ("HUAWEI-STACK-MIB", "hwStackTopoType"),
        ("HUAWEI-STACK-MIB", "hwStackMacAddressSwitchTime"),
        ("HUAWEI-STACK-MIB", "hwStackSystemMac"),
        ("HUAWEI-STACK-MIB", "hwStackIsStackDevice"),
        ("HUAWEI-STACK-MIB", "hwStackReservedVlanId"),
        ("HUAWEI-STACK-MIB", "hwStackClearUnsupportCfg"),
        ("HUAWEI-STACK-MIB", "hwStackLinkAlarmThreshold"),
        ("HUAWEI-STACK-MIB", "hwStackMemberThreshold"),
        ("HUAWEI-STACK-MIB", "hwStackMode"),
        ("HUAWEI-STACK-MIB", "hwStackMemberSpec"),
        ("HUAWEI-STACK-MIB", "hwLeafMaxNumber"),
        ("HUAWEI-STACK-MIB", "hwFabricCurrentForwardModel"),
        ("HUAWEI-STACK-MIB", "hwFabricConfigForwardModel"),
        ("HUAWEI-STACK-MIB", "hwLeafSingleHomedAlarmEnable"),
        ("HUAWEI-STACK-MIB", "hwFabricExcludeLeafType"),
        ("HUAWEI-STACK-MIB", "hwMemberCurrentStackId"),
        ("HUAWEI-STACK-MIB", "hwMemberStackPriority"),
        ("HUAWEI-STACK-MIB", "hwMemberStackRole"),
        ("HUAWEI-STACK-MIB", "hwMemberStackMacAddress"),
        ("HUAWEI-STACK-MIB", "hwMemberStackDeviceType"),
        ("HUAWEI-STACK-MIB", "hwMemberConfigStackId"),
        ("HUAWEI-STACK-MIB", "hwMemberStackObjectId"),
        ("HUAWEI-STACK-MIB", "hwStackPriority"),
        ("HUAWEI-STACK-MIB", "hwStackRole"),
        ("HUAWEI-STACK-MIB", "hwStackMacAddress"),
        ("HUAWEI-STACK-MIB", "hwStackDeviceType"),
        ("HUAWEI-STACK-MIB", "hwStackId"),
        ("HUAWEI-STACK-MIB", "hwStackConfigId"),
        ("HUAWEI-STACK-MIB", "hwStackSysOid"),
        ("HUAWEI-STACK-MIB", "hwStackDescription"),
        ("HUAWEI-STACK-MIB", "hwStackCurrentUplinkPort"),
        ("HUAWEI-STACK-MIB", "hwStackConfigUplinkPort"),
        ("HUAWEI-STACK-MIB", "hwStackCurrentSwitchMode"),
        ("HUAWEI-STACK-MIB", "hwStackConfigSwitchMode"),
        ("HUAWEI-STACK-MIB", "hwEnabledStackModePortIndex"),
        ("HUAWEI-STACK-MIB", "hwFabricPortID"),
        ("HUAWEI-STACK-MIB", "hwFabricPortIndex"),
        ("HUAWEI-STACK-MIB", "hwFabricMemberID"),
        ("HUAWEI-STACK-MIB", "hwFabricLoadBalance"),
        ("HUAWEI-STACK-MIB", "hwFabricProtocolState"),
        ("HUAWEI-STACK-MIB", "hwFabricConfiguredLinkNum"),
        ("HUAWEI-STACK-MIB", "hwSpineStackId"),
        ("HUAWEI-STACK-MIB", "hwSpinePortName"),
        ("HUAWEI-STACK-MIB", "hwSpinePortStatus"),
        ("HUAWEI-STACK-MIB", "hwLeafPortIndex"),
        ("HUAWEI-STACK-MIB", "hwLeafStackId"),
        ("HUAWEI-STACK-MIB", "hwLeafPortName"),
        ("HUAWEI-STACK-MIB", "hwLeafPortStatus"),
        ("HUAWEI-STACK-MIB", "hwStackPortStackId"),
        ("HUAWEI-STACK-MIB", "hwStackPortId"),
        ("HUAWEI-STACK-MIB", "hwStackPortName"),
        ("HUAWEI-STACK-MIB", "hwStackNeighborInfo"),
        ("HUAWEI-STACK-MIB", "hwStackPortStatus"),
        ("HUAWEI-STACK-MIB", "hwStackUpgradeGrpType"),
        ("HUAWEI-STACK-MIB", "hwStackUpgradeGrpValue"),
        ("HUAWEI-STACK-MIB", "hwStackUpgradeFileType"),
        ("HUAWEI-STACK-MIB", "hwStackUpgradeFileInfo"),
        ("HUAWEI-STACK-MIB", "hwStackUpgradeFtpIp"),
        ("HUAWEI-STACK-MIB", "hwStackUpgradeFtpUserName"),
        ("HUAWEI-STACK-MIB", "hwStackUpgradeFtpPassword"),
        ("HUAWEI-STACK-MIB", "hwStackUpgradeServerPort"),
        ("HUAWEI-STACK-MIB", "hwStackUpgradeFileSize"),
        ("HUAWEI-STACK-MIB", "hwStackUpgradeTransmitProtocol"),
        ("HUAWEI-STACK-MIB", "hwStackUpgradeRowStatus"),
        ("HUAWEI-STACK-MIB", "hwStackUpgradeResultMemberId"),
        ("HUAWEI-STACK-MIB", "hwStackUpgradeResult"),
        ("HUAWEI-STACK-MIB", "hwStackUpgradeResultInProcess"),
        ("HUAWEI-STACK-MIB", "hwStackUpgradeResultFailReason"),
        ("HUAWEI-STACK-MIB", "hwStackMacAddressAlarmTime"))
)
if mibBuilder.loadTexts:
    hwStackObjectGroup.setStatus("current")

hwStackTrapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 100, 1, 2, 3)
)
hwStackTrapGroup.setObjects(
      *(("HUAWEI-STACK-MIB", "hwStackLocalIfName"),
        ("HUAWEI-STACK-MIB", "hwStackPeerIfName"),
        ("HUAWEI-STACK-MIB", "hwConfigureFailedStackId"),
        ("HUAWEI-STACK-MIB", "hwStackConnectErrReason"),
        ("HUAWEI-STACK-MIB", "hwCssTrapErrorPortId"),
        ("HUAWEI-STACK-MIB", "hwStackConnectMethod"),
        ("HUAWEI-STACK-MIB", "hwStackCfgConflictStackId"),
        ("HUAWEI-STACK-MIB", "hwStackFabricPort"),
        ("HUAWEI-STACK-MIB", "hwStackFabricMemberPort"),
        ("HUAWEI-STACK-MIB", "hwStackMemberId"),
        ("HUAWEI-STACK-MIB", "hwStackLeafMemberId"),
        ("HUAWEI-STACK-MIB", "hwStackReason"),
        ("HUAWEI-STACK-MIB", "hwStackLeafPort"),
        ("HUAWEI-STACK-MIB", "hwStackCurrentLinkNum"),
        ("HUAWEI-STACK-MIB", "hwFabricCurrentLinkNum"),
        ("HUAWEI-STACK-MIB", "hwStackErrorDownRecoverReason"))
)
if mibBuilder.loadTexts:
    hwStackTrapGroup.setStatus("current")

hwCssObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 101, 1, 2, 1)
)
hwCssObjectGroup.setObjects(
      *(("HUAWEI-STACK-MIB", "hwCssMemberFrameId"),
        ("HUAWEI-STACK-MIB", "hwCssMemberConfigFrameId"),
        ("HUAWEI-STACK-MIB", "hwCssMemberPriority"),
        ("HUAWEI-STACK-MIB", "hwCssMemberConfigPriority"),
        ("HUAWEI-STACK-MIB", "hwCssMemberMasterForce"),
        ("HUAWEI-STACK-MIB", "hwCssMemberConfigMasterForce"),
        ("HUAWEI-STACK-MIB", "hwCssMemberConfigEnable"),
        ("HUAWEI-STACK-MIB", "hwCssMemberRole"),
        ("HUAWEI-STACK-MIB", "hwCssEnable"))
)
if mibBuilder.loadTexts:
    hwCssObjectGroup.setStatus("current")

hwCssTrapObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 101, 1, 2, 2)
)
hwCssTrapObjectGroup.setObjects(
      *(("HUAWEI-STACK-MIB", "hwCssTrapFrameId2"),
        ("HUAWEI-STACK-MIB", "hwCssTrapSlotId2"),
        ("HUAWEI-STACK-MIB", "hwCssTrapPortId2"),
        ("HUAWEI-STACK-MIB", "hwCssTrapFrameId3"),
        ("HUAWEI-STACK-MIB", "hwCssTrapSlotId3"),
        ("HUAWEI-STACK-MIB", "hwCssTrapPortId3"),
        ("HUAWEI-STACK-MIB", "hwCssTrapFrameId1"),
        ("HUAWEI-STACK-MIB", "hwCssTrapSlotId1"),
        ("HUAWEI-STACK-MIB", "hwCssTrapPortId1"),
        ("HUAWEI-STACK-MIB", "hwCssTrapConfigureFailedSlotId"))
)
if mibBuilder.loadTexts:
    hwCssTrapObjectGroup.setStatus("current")


# Notification objects

hwStackLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 22, 1)
)
hwStackLinkUp.setObjects(
      *(("HUAWEI-STACK-MIB", "hwStackPortStackId"),
        ("HUAWEI-STACK-MIB", "hwStackPortId"),
        ("HUAWEI-STACK-MIB", "hwStackPortStatus"))
)
if mibBuilder.loadTexts:
    hwStackLinkUp.setStatus(
        "current"
    )

hwStackLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 22, 2)
)
hwStackLinkDown.setObjects(
      *(("HUAWEI-STACK-MIB", "hwStackPortStackId"),
        ("HUAWEI-STACK-MIB", "hwStackPortId"),
        ("HUAWEI-STACK-MIB", "hwStackPortStatus"))
)
if mibBuilder.loadTexts:
    hwStackLinkDown.setStatus(
        "current"
    )

hwStackStandbyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 22, 3)
)
hwStackStandbyChange.setObjects(
    ("HUAWEI-STACK-MIB", "hwMemberCurrentStackId")
)
if mibBuilder.loadTexts:
    hwStackStandbyChange.setStatus(
        "current"
    )

hwStackSwitchOver = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 22, 4)
)
hwStackSwitchOver.setObjects(
    ("HUAWEI-STACK-MIB", "hwMemberCurrentStackId")
)
if mibBuilder.loadTexts:
    hwStackSwitchOver.setStatus(
        "current"
    )

hwStackSystemRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 22, 5)
)
hwStackSystemRestart.setObjects(
    ("HUAWEI-STACK-MIB", "hwMemberCurrentStackId")
)
if mibBuilder.loadTexts:
    hwStackSystemRestart.setStatus(
        "current"
    )

hwStackStackMemberAdd = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 22, 6)
)
hwStackStackMemberAdd.setObjects(
    ("HUAWEI-STACK-MIB", "hwMemberCurrentStackId")
)
if mibBuilder.loadTexts:
    hwStackStackMemberAdd.setStatus(
        "current"
    )

hwStackStackMemberLeave = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 22, 7)
)
hwStackStackMemberLeave.setObjects(
    ("HUAWEI-STACK-MIB", "hwMemberCurrentStackId")
)
if mibBuilder.loadTexts:
    hwStackStackMemberLeave.setStatus(
        "current"
    )

hwStackStackMacChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 22, 8)
)
hwStackStackMacChange.setObjects(
    ("HUAWEI-STACK-MIB", "hwMemberStackMacAddress")
)
if mibBuilder.loadTexts:
    hwStackStackMacChange.setStatus(
        "current"
    )

hwStackLogicStackPortLinkErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 22, 9)
)
hwStackLogicStackPortLinkErr.setObjects(
      *(("HUAWEI-STACK-MIB", "hwStackLocalIfName"),
        ("HUAWEI-STACK-MIB", "hwStackPeerIfName"))
)
if mibBuilder.loadTexts:
    hwStackLogicStackPortLinkErr.setStatus(
        "current"
    )

hwStackPhyStackPortLinkErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 22, 10)
)
hwStackPhyStackPortLinkErr.setObjects(
      *(("HUAWEI-STACK-MIB", "hwStackLocalIfName"),
        ("HUAWEI-STACK-MIB", "hwStackPeerIfName"))
)
if mibBuilder.loadTexts:
    hwStackPhyStackPortLinkErr.setStatus(
        "current"
    )

hwPhyStackPortIsDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 22, 11)
)
hwPhyStackPortIsDown.setObjects(
    ("HUAWEI-STACK-MIB", "hwStackLocalIfName")
)
if mibBuilder.loadTexts:
    hwPhyStackPortIsDown.setStatus(
        "current"
    )

hwPhyStackPortIsUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 22, 12)
)
hwPhyStackPortIsUp.setObjects(
    ("HUAWEI-STACK-MIB", "hwStackLocalIfName")
)
if mibBuilder.loadTexts:
    hwPhyStackPortIsUp.setStatus(
        "current"
    )

hwStackLogicStackPortLinkErrResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 22, 13)
)
hwStackLogicStackPortLinkErrResume.setObjects(
      *(("HUAWEI-STACK-MIB", "hwStackLocalIfName"),
        ("HUAWEI-STACK-MIB", "hwStackPeerIfName"))
)
if mibBuilder.loadTexts:
    hwStackLogicStackPortLinkErrResume.setStatus(
        "current"
    )

hwStackPortConfigureFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 22, 14)
)
hwStackPortConfigureFailed.setObjects(
    ("HUAWEI-STACK-MIB", "hwConfigureFailedStackId")
)
if mibBuilder.loadTexts:
    hwStackPortConfigureFailed.setStatus(
        "current"
    )

hwStackLinkLimitAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 22, 15)
)
hwStackLinkLimitAlarm.setObjects(
      *(("HUAWEI-STACK-MIB", "hwStackLocalIfName"),
        ("HUAWEI-STACK-MIB", "hwStackCurrentLinkNum"),
        ("HUAWEI-STACK-MIB", "hwStackLinkAlarmThreshold"))
)
if mibBuilder.loadTexts:
    hwStackLinkLimitAlarm.setStatus(
        "current"
    )

hwStackLinkLimitAlarmResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 22, 16)
)
hwStackLinkLimitAlarmResume.setObjects(
      *(("HUAWEI-STACK-MIB", "hwStackLocalIfName"),
        ("HUAWEI-STACK-MIB", "hwStackCurrentLinkNum"),
        ("HUAWEI-STACK-MIB", "hwStackLinkAlarmThreshold"))
)
if mibBuilder.loadTexts:
    hwStackLinkLimitAlarmResume.setStatus(
        "current"
    )

hwStackConfigConflict = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 22, 17)
)
hwStackConfigConflict.setObjects(
      *(("HUAWEI-STACK-MIB", "hwMemberCurrentStackId"),
        ("HUAWEI-STACK-MIB", "hwStackCfgConflictStackId"))
)
if mibBuilder.loadTexts:
    hwStackConfigConflict.setStatus(
        "current"
    )

hwStackFabricPortLinkErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 22, 18)
)
hwStackFabricPortLinkErr.setObjects(
      *(("HUAWEI-STACK-MIB", "hwStackFabricPort"),
        ("HUAWEI-STACK-MIB", "hwStackFabricMemberPort"))
)
if mibBuilder.loadTexts:
    hwStackFabricPortLinkErr.setStatus(
        "current"
    )

hwStackFabricPortLinkErrResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 22, 19)
)
hwStackFabricPortLinkErrResume.setObjects(
      *(("HUAWEI-STACK-MIB", "hwStackFabricPort"),
        ("HUAWEI-STACK-MIB", "hwStackFabricMemberPort"))
)
if mibBuilder.loadTexts:
    hwStackFabricPortLinkErrResume.setStatus(
        "current"
    )

hwStackLeafSingleHomedAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 22, 20)
)
hwStackLeafSingleHomedAlarm.setObjects(
      *(("HUAWEI-STACK-MIB", "hwStackMemberId"),
        ("HUAWEI-STACK-MIB", "hwStackLeafMemberId"))
)
if mibBuilder.loadTexts:
    hwStackLeafSingleHomedAlarm.setStatus(
        "current"
    )

hwStackLeafSingleHomedAlarmResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 22, 21)
)
hwStackLeafSingleHomedAlarmResume.setObjects(
      *(("HUAWEI-STACK-MIB", "hwStackMemberId"),
        ("HUAWEI-STACK-MIB", "hwStackLeafMemberId"))
)
if mibBuilder.loadTexts:
    hwStackLeafSingleHomedAlarmResume.setStatus(
        "current"
    )

hwStackMemberLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 22, 22)
)
hwStackMemberLimit.setObjects(
    ("HUAWEI-STACK-MIB", "hwStackMemberThreshold")
)
if mibBuilder.loadTexts:
    hwStackMemberLimit.setStatus(
        "current"
    )

hwStackMemberAdd = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 22, 23)
)
hwStackMemberAdd.setObjects(
    ("HUAWEI-STACK-MIB", "hwStackId")
)
if mibBuilder.loadTexts:
    hwStackMemberAdd.setStatus(
        "current"
    )

hwStackMemberLeave = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 22, 24)
)
hwStackMemberLeave.setObjects(
    ("HUAWEI-STACK-MIB", "hwStackId")
)
if mibBuilder.loadTexts:
    hwStackMemberLeave.setStatus(
        "current"
    )

hwStackConfigDifferent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 22, 25)
)
hwStackConfigDifferent.setObjects(
      *(("HUAWEI-STACK-MIB", "hwStackId"),
        ("HUAWEI-STACK-MIB", "hwStackReason"))
)
if mibBuilder.loadTexts:
    hwStackConfigDifferent.setStatus(
        "current"
    )

hwStackLeafConfigConflict = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 22, 26)
)
hwStackLeafConfigConflict.setObjects(
    ("HUAWEI-STACK-MIB", "hwStackLeafPort")
)
if mibBuilder.loadTexts:
    hwStackLeafConfigConflict.setStatus(
        "current"
    )

hwStackChipSingleHomedAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 22, 27)
)
hwStackChipSingleHomedAlarm.setObjects(
    ("HUAWEI-STACK-MIB", "hwStackLeafMemberId")
)
if mibBuilder.loadTexts:
    hwStackChipSingleHomedAlarm.setStatus(
        "current"
    )

hwStackChipSingleHomedAlarmResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 22, 28)
)
hwStackChipSingleHomedAlarmResume.setObjects(
    ("HUAWEI-STACK-MIB", "hwStackLeafMemberId")
)
if mibBuilder.loadTexts:
    hwStackChipSingleHomedAlarmResume.setStatus(
        "current"
    )

hwStackLeafMemberAdd = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 22, 29)
)
hwStackLeafMemberAdd.setObjects(
    ("HUAWEI-STACK-MIB", "hwStackId")
)
if mibBuilder.loadTexts:
    hwStackLeafMemberAdd.setStatus(
        "current"
    )

hwFabricLinkLimitAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 22, 30)
)
hwFabricLinkLimitAlarm.setObjects(
      *(("HUAWEI-STACK-MIB", "hwStackFabricPort"),
        ("HUAWEI-STACK-MIB", "hwFabricCurrentLinkNum"),
        ("HUAWEI-STACK-MIB", "hwFabricConfiguredLinkNum"))
)
if mibBuilder.loadTexts:
    hwFabricLinkLimitAlarm.setStatus(
        "current"
    )

hwFabricLinkLimitAlarmResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 22, 31)
)
hwFabricLinkLimitAlarmResume.setObjects(
      *(("HUAWEI-STACK-MIB", "hwStackFabricPort"),
        ("HUAWEI-STACK-MIB", "hwFabricCurrentLinkNum"),
        ("HUAWEI-STACK-MIB", "hwFabricConfiguredLinkNum"))
)
if mibBuilder.loadTexts:
    hwFabricLinkLimitAlarmResume.setStatus(
        "current"
    )

hwStackMemberExceedSpec = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 22, 32)
)
hwStackMemberExceedSpec.setObjects(
    ("HUAWEI-STACK-MIB", "hwStackMemberSpec")
)
if mibBuilder.loadTexts:
    hwStackMemberExceedSpec.setStatus(
        "current"
    )

hwStackMacInconsistence = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 22, 33)
)
hwStackMacInconsistence.setObjects(
    ("HUAWEI-STACK-MIB", "hwStackSystemMac")
)
if mibBuilder.loadTexts:
    hwStackMacInconsistence.setStatus(
        "current"
    )

hwStackMacInconsistenceResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 22, 34)
)
hwStackMacInconsistenceResume.setObjects(
    ("HUAWEI-STACK-MIB", "hwStackSystemMac")
)
if mibBuilder.loadTexts:
    hwStackMacInconsistenceResume.setStatus(
        "current"
    )

hwFabricLinkProtocolAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 22, 35)
)
hwFabricLinkProtocolAlarm.setObjects(
    ("HUAWEI-STACK-MIB", "hwStackFabricPort")
)
if mibBuilder.loadTexts:
    hwFabricLinkProtocolAlarm.setStatus(
        "current"
    )

hwFabricLinkProtocolAlarmResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 22, 36)
)
hwFabricLinkProtocolAlarmResume.setObjects(
    ("HUAWEI-STACK-MIB", "hwStackFabricPort")
)
if mibBuilder.loadTexts:
    hwFabricLinkProtocolAlarmResume.setStatus(
        "current"
    )

hwFabricMemberPortProtocolAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 22, 37)
)
hwFabricMemberPortProtocolAlarm.setObjects(
    ("HUAWEI-STACK-MIB", "hwStackFabricMemberPort")
)
if mibBuilder.loadTexts:
    hwFabricMemberPortProtocolAlarm.setStatus(
        "current"
    )

hwFabricMemberPortProtocolAlarmResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 22, 38)
)
hwFabricMemberPortProtocolAlarmResume.setObjects(
    ("HUAWEI-STACK-MIB", "hwStackFabricMemberPort")
)
if mibBuilder.loadTexts:
    hwFabricMemberPortProtocolAlarmResume.setStatus(
        "current"
    )

hwLeafMaxNumberExceededAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 22, 39)
)
hwLeafMaxNumberExceededAlarm.setObjects(
      *(("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-STACK-MIB", "hwLeafMaxNumber"))
)
if mibBuilder.loadTexts:
    hwLeafMaxNumberExceededAlarm.setStatus(
        "current"
    )

hwLeafMaxNumberExceededAlarmResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 22, 40)
)
hwLeafMaxNumberExceededAlarmResume.setObjects(
      *(("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-STACK-MIB", "hwLeafMaxNumber"))
)
if mibBuilder.loadTexts:
    hwLeafMaxNumberExceededAlarmResume.setStatus(
        "current"
    )

hwPhyStackPortErrorDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 22, 41)
)
hwPhyStackPortErrorDown.setObjects(
    ("HUAWEI-STACK-MIB", "hwStackLocalIfName")
)
if mibBuilder.loadTexts:
    hwPhyStackPortErrorDown.setStatus(
        "current"
    )

hwPhyStackPortErrorDownRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 1, 22, 42)
)
hwPhyStackPortErrorDownRecover.setObjects(
      *(("HUAWEI-STACK-MIB", "hwStackLocalIfName"),
        ("HUAWEI-STACK-MIB", "hwStackErrorDownRecoverReason"))
)
if mibBuilder.loadTexts:
    hwPhyStackPortErrorDownRecover.setStatus(
        "current"
    )

hwCssLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 3, 2, 1)
)
hwCssLinkDown.setObjects(
      *(("HUAWEI-STACK-MIB", "hwCssTrapFrameId1"),
        ("HUAWEI-STACK-MIB", "hwCssTrapSlotId1"),
        ("HUAWEI-STACK-MIB", "hwCssTrapPortId1"))
)
if mibBuilder.loadTexts:
    hwCssLinkDown.setStatus(
        "current"
    )

hwCssLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 3, 2, 2)
)
hwCssLinkUp.setObjects(
      *(("HUAWEI-STACK-MIB", "hwCssTrapFrameId1"),
        ("HUAWEI-STACK-MIB", "hwCssTrapSlotId1"),
        ("HUAWEI-STACK-MIB", "hwCssTrapPortId1"))
)
if mibBuilder.loadTexts:
    hwCssLinkUp.setStatus(
        "current"
    )

hwCssSwitchOver = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 3, 2, 3)
)
hwCssSwitchOver.setObjects(
    ("HUAWEI-STACK-MIB", "hwCssTrapFrameId1")
)
if mibBuilder.loadTexts:
    hwCssSwitchOver.setStatus(
        "current"
    )

hwCssConnectError = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 3, 2, 4)
)
hwCssConnectError.setObjects(
      *(("HUAWEI-STACK-MIB", "hwCssTrapFrameId1"),
        ("HUAWEI-STACK-MIB", "hwCssTrapSlotId1"),
        ("HUAWEI-STACK-MIB", "hwCssTrapPortId1"),
        ("HUAWEI-STACK-MIB", "hwCssTrapFrameId2"),
        ("HUAWEI-STACK-MIB", "hwCssTrapSlotId2"),
        ("HUAWEI-STACK-MIB", "hwCssTrapPortId2"),
        ("HUAWEI-STACK-MIB", "hwCssTrapFrameId3"),
        ("HUAWEI-STACK-MIB", "hwCssTrapSlotId3"),
        ("HUAWEI-STACK-MIB", "hwCssTrapPortId3"))
)
if mibBuilder.loadTexts:
    hwCssConnectError.setStatus(
        "current"
    )

hwCssSplit = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 3, 2, 5)
)
if mibBuilder.loadTexts:
    hwCssSplit.setStatus(
        "current"
    )

hwCssEstablish = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 3, 2, 6)
)
if mibBuilder.loadTexts:
    hwCssEstablish.setStatus(
        "current"
    )

hwCssFastUpgradeFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 3, 2, 7)
)
if mibBuilder.loadTexts:
    hwCssFastUpgradeFail.setStatus(
        "current"
    )

hwCssPhyCsuConnectError = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 3, 2, 8)
)
hwCssPhyCsuConnectError.setObjects(
      *(("HUAWEI-STACK-MIB", "hwStackLocalIfName"),
        ("HUAWEI-STACK-MIB", "hwStackPeerIfName"),
        ("HUAWEI-STACK-MIB", "hwStackConnectErrReason"))
)
if mibBuilder.loadTexts:
    hwCssPhyCsuConnectError.setStatus(
        "current"
    )

hwCssLpuInvalidLicense = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 3, 2, 9)
)
if mibBuilder.loadTexts:
    hwCssLpuInvalidLicense.setStatus(
        "current"
    )

hwCssPortConfigureFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 3, 2, 10)
)
hwCssPortConfigureFailed.setObjects(
    ("HUAWEI-STACK-MIB", "hwCssTrapConfigureFailedSlotId")
)
if mibBuilder.loadTexts:
    hwCssPortConfigureFailed.setStatus(
        "current"
    )

hwCssPortUpDownAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 3, 2, 11)
)
hwCssPortUpDownAlarm.setObjects(
    ("HUAWEI-STACK-MIB", "hwCssTrapErrorPortId")
)
if mibBuilder.loadTexts:
    hwCssPortUpDownAlarm.setStatus(
        "current"
    )

hwCssPortCrcErrorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 3, 2, 12)
)
hwCssPortCrcErrorAlarm.setObjects(
    ("HUAWEI-STACK-MIB", "hwCssTrapErrorPortId")
)
if mibBuilder.loadTexts:
    hwCssPortCrcErrorAlarm.setStatus(
        "current"
    )

hwCssPortErrorDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 3, 2, 13)
)
hwCssPortErrorDown.setObjects(
    ("HUAWEI-STACK-MIB", "hwCssTrapErrorPortId")
)
if mibBuilder.loadTexts:
    hwCssPortErrorDown.setStatus(
        "current"
    )

hwCssPortErrorDownRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 3, 2, 14)
)
hwCssPortErrorDownRecover.setObjects(
    ("HUAWEI-STACK-MIB", "hwCssTrapErrorPortId")
)
if mibBuilder.loadTexts:
    hwCssPortErrorDownRecover.setStatus(
        "current"
    )

hwCssPhyVs08ConnectError = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 3, 2, 15)
)
hwCssPhyVs08ConnectError.setObjects(
      *(("HUAWEI-STACK-MIB", "hwStackLocalIfName"),
        ("HUAWEI-STACK-MIB", "hwStackPeerIfName"),
        ("HUAWEI-STACK-MIB", "hwStackConnectMethod"))
)
if mibBuilder.loadTexts:
    hwCssPhyVs08ConnectError.setStatus(
        "current"
    )

hwCssStandbyError = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 3, 2, 16)
)
if mibBuilder.loadTexts:
    hwCssStandbyError.setStatus(
        "current"
    )

hwCssStandbyErrorRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 3, 2, 17)
)
if mibBuilder.loadTexts:
    hwCssStandbyErrorRestore.setStatus(
        "current"
    )

hwCssPortStateError = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 3, 2, 18)
)
hwCssPortStateError.setObjects(
    ("HUAWEI-STACK-MIB", "hwCssTrapErrorPortId")
)
if mibBuilder.loadTexts:
    hwCssPortStateError.setStatus(
        "current"
    )

hwCssPhyCardConnectError = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 3, 3, 2, 19)
)
hwCssPhyCardConnectError.setObjects(
      *(("HUAWEI-STACK-MIB", "hwStackLocalIfName"),
        ("HUAWEI-STACK-MIB", "hwStackPeerIfName"),
        ("HUAWEI-STACK-MIB", "hwStackConnectErrReason"))
)
if mibBuilder.loadTexts:
    hwCssPhyCardConnectError.setStatus(
        "current"
    )


# Notifications groups

hwStackNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 100, 1, 2, 2)
)
hwStackNotificationGroup.setObjects(
      *(("HUAWEI-STACK-MIB", "hwStackLinkUp"),
        ("HUAWEI-STACK-MIB", "hwStackLinkDown"),
        ("HUAWEI-STACK-MIB", "hwStackStandbyChange"),
        ("HUAWEI-STACK-MIB", "hwStackSwitchOver"),
        ("HUAWEI-STACK-MIB", "hwStackSystemRestart"),
        ("HUAWEI-STACK-MIB", "hwStackStackMemberAdd"),
        ("HUAWEI-STACK-MIB", "hwStackStackMemberLeave"),
        ("HUAWEI-STACK-MIB", "hwStackStackMacChange"),
        ("HUAWEI-STACK-MIB", "hwStackLogicStackPortLinkErr"),
        ("HUAWEI-STACK-MIB", "hwStackPhyStackPortLinkErr"),
        ("HUAWEI-STACK-MIB", "hwPhyStackPortIsDown"),
        ("HUAWEI-STACK-MIB", "hwPhyStackPortIsUp"),
        ("HUAWEI-STACK-MIB", "hwStackLogicStackPortLinkErrResume"),
        ("HUAWEI-STACK-MIB", "hwStackPortConfigureFailed"),
        ("HUAWEI-STACK-MIB", "hwStackLinkLimitAlarm"),
        ("HUAWEI-STACK-MIB", "hwStackLinkLimitAlarmResume"),
        ("HUAWEI-STACK-MIB", "hwStackConfigConflict"),
        ("HUAWEI-STACK-MIB", "hwStackFabricPortLinkErr"),
        ("HUAWEI-STACK-MIB", "hwStackFabricPortLinkErrResume"),
        ("HUAWEI-STACK-MIB", "hwStackLeafSingleHomedAlarm"),
        ("HUAWEI-STACK-MIB", "hwStackLeafSingleHomedAlarmResume"),
        ("HUAWEI-STACK-MIB", "hwStackMemberLimit"),
        ("HUAWEI-STACK-MIB", "hwStackMemberAdd"),
        ("HUAWEI-STACK-MIB", "hwStackMemberLeave"),
        ("HUAWEI-STACK-MIB", "hwStackConfigDifferent"),
        ("HUAWEI-STACK-MIB", "hwStackLeafConfigConflict"),
        ("HUAWEI-STACK-MIB", "hwStackChipSingleHomedAlarm"),
        ("HUAWEI-STACK-MIB", "hwStackChipSingleHomedAlarmResume"),
        ("HUAWEI-STACK-MIB", "hwStackLeafMemberAdd"),
        ("HUAWEI-STACK-MIB", "hwFabricLinkLimitAlarm"),
        ("HUAWEI-STACK-MIB", "hwFabricLinkLimitAlarmResume"),
        ("HUAWEI-STACK-MIB", "hwStackMemberExceedSpec"),
        ("HUAWEI-STACK-MIB", "hwStackMacInconsistence"),
        ("HUAWEI-STACK-MIB", "hwStackMacInconsistenceResume"),
        ("HUAWEI-STACK-MIB", "hwFabricLinkProtocolAlarm"),
        ("HUAWEI-STACK-MIB", "hwFabricLinkProtocolAlarmResume"),
        ("HUAWEI-STACK-MIB", "hwFabricMemberPortProtocolAlarm"),
        ("HUAWEI-STACK-MIB", "hwFabricMemberPortProtocolAlarmResume"),
        ("HUAWEI-STACK-MIB", "hwLeafMaxNumberExceededAlarm"),
        ("HUAWEI-STACK-MIB", "hwLeafMaxNumberExceededAlarmResume"),
        ("HUAWEI-STACK-MIB", "hwPhyStackPortErrorDown"),
        ("HUAWEI-STACK-MIB", "hwPhyStackPortErrorDownRecover"))
)
if mibBuilder.loadTexts:
    hwStackNotificationGroup.setStatus(
        "current"
    )

hwCssNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 101, 1, 2, 3)
)
hwCssNotificationGroup.setObjects(
      *(("HUAWEI-STACK-MIB", "hwCssLinkDown"),
        ("HUAWEI-STACK-MIB", "hwCssLinkUp"),
        ("HUAWEI-STACK-MIB", "hwCssSwitchOver"),
        ("HUAWEI-STACK-MIB", "hwCssConnectError"),
        ("HUAWEI-STACK-MIB", "hwCssSplit"),
        ("HUAWEI-STACK-MIB", "hwCssEstablish"),
        ("HUAWEI-STACK-MIB", "hwCssFastUpgradeFail"),
        ("HUAWEI-STACK-MIB", "hwCssPhyCsuConnectError"),
        ("HUAWEI-STACK-MIB", "hwCssLpuInvalidLicense"),
        ("HUAWEI-STACK-MIB", "hwCssPortConfigureFailed"),
        ("HUAWEI-STACK-MIB", "hwCssPortUpDownAlarm"),
        ("HUAWEI-STACK-MIB", "hwCssPortCrcErrorAlarm"),
        ("HUAWEI-STACK-MIB", "hwCssPortErrorDown"),
        ("HUAWEI-STACK-MIB", "hwCssPortErrorDownRecover"),
        ("HUAWEI-STACK-MIB", "hwCssPhyVs08ConnectError"),
        ("HUAWEI-STACK-MIB", "hwCssStandbyError"),
        ("HUAWEI-STACK-MIB", "hwCssStandbyErrorRestore"),
        ("HUAWEI-STACK-MIB", "hwCssPortStateError"),
        ("HUAWEI-STACK-MIB", "hwCssPhyCardConnectError"))
)
if mibBuilder.loadTexts:
    hwCssNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwStackCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 100, 1, 1)
)
if mibBuilder.loadTexts:
    hwStackCompliance.setStatus(
        "current"
    )

hwCssCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 183, 101, 1, 1)
)
if mibBuilder.loadTexts:
    hwCssCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-STACK-MIB",
    **{"huaweiStackMIB": huaweiStackMIB,
       "hwStackObject": hwStackObject,
       "hwStackRun": hwStackRun,
       "hwStackTopoType": hwStackTopoType,
       "hwStackMacAddressSwitchTime": hwStackMacAddressSwitchTime,
       "hwStackSystemMac": hwStackSystemMac,
       "hwStackIsStackDevice": hwStackIsStackDevice,
       "hwStackReservedVlanId": hwStackReservedVlanId,
       "hwStackClearUnsupportCfg": hwStackClearUnsupportCfg,
       "hwStackLinkAlarmThreshold": hwStackLinkAlarmThreshold,
       "hwStackMemberThreshold": hwStackMemberThreshold,
       "hwStackMode": hwStackMode,
       "hwStackMemberSpec": hwStackMemberSpec,
       "hwStackMacAddressAlarmTime": hwStackMacAddressAlarmTime,
       "hwLeafMaxNumber": hwLeafMaxNumber,
       "hwFabricCurrentForwardModel": hwFabricCurrentForwardModel,
       "hwFabricConfigForwardModel": hwFabricConfigForwardModel,
       "hwLeafSingleHomedAlarmEnable": hwLeafSingleHomedAlarmEnable,
       "hwFabricExcludeLeafType": hwFabricExcludeLeafType,
       "hwStackMemberInfoTable": hwStackMemberInfoTable,
       "hwStackMemberInfoEntry": hwStackMemberInfoEntry,
       "hwMemberCurrentStackId": hwMemberCurrentStackId,
       "hwMemberStackPriority": hwMemberStackPriority,
       "hwMemberStackRole": hwMemberStackRole,
       "hwMemberStackMacAddress": hwMemberStackMacAddress,
       "hwMemberStackDeviceType": hwMemberStackDeviceType,
       "hwMemberConfigStackId": hwMemberConfigStackId,
       "hwMemberStackObjectId": hwMemberStackObjectId,
       "hwStackPortTable": hwStackPortTable,
       "hwStackPortEntry": hwStackPortEntry,
       "hwStackPortStackId": hwStackPortStackId,
       "hwStackPortId": hwStackPortId,
       "hwStackPortName": hwStackPortName,
       "hwStackNeighborInfo": hwStackNeighborInfo,
       "hwStackPortStatus": hwStackPortStatus,
       "hwStackEventsV2": hwStackEventsV2,
       "hwStackLinkUp": hwStackLinkUp,
       "hwStackLinkDown": hwStackLinkDown,
       "hwStackStandbyChange": hwStackStandbyChange,
       "hwStackSwitchOver": hwStackSwitchOver,
       "hwStackSystemRestart": hwStackSystemRestart,
       "hwStackStackMemberAdd": hwStackStackMemberAdd,
       "hwStackStackMemberLeave": hwStackStackMemberLeave,
       "hwStackStackMacChange": hwStackStackMacChange,
       "hwStackLogicStackPortLinkErr": hwStackLogicStackPortLinkErr,
       "hwStackPhyStackPortLinkErr": hwStackPhyStackPortLinkErr,
       "hwPhyStackPortIsDown": hwPhyStackPortIsDown,
       "hwPhyStackPortIsUp": hwPhyStackPortIsUp,
       "hwStackLogicStackPortLinkErrResume": hwStackLogicStackPortLinkErrResume,
       "hwStackPortConfigureFailed": hwStackPortConfigureFailed,
       "hwStackLinkLimitAlarm": hwStackLinkLimitAlarm,
       "hwStackLinkLimitAlarmResume": hwStackLinkLimitAlarmResume,
       "hwStackConfigConflict": hwStackConfigConflict,
       "hwStackFabricPortLinkErr": hwStackFabricPortLinkErr,
       "hwStackFabricPortLinkErrResume": hwStackFabricPortLinkErrResume,
       "hwStackLeafSingleHomedAlarm": hwStackLeafSingleHomedAlarm,
       "hwStackLeafSingleHomedAlarmResume": hwStackLeafSingleHomedAlarmResume,
       "hwStackMemberLimit": hwStackMemberLimit,
       "hwStackMemberAdd": hwStackMemberAdd,
       "hwStackMemberLeave": hwStackMemberLeave,
       "hwStackConfigDifferent": hwStackConfigDifferent,
       "hwStackLeafConfigConflict": hwStackLeafConfigConflict,
       "hwStackChipSingleHomedAlarm": hwStackChipSingleHomedAlarm,
       "hwStackChipSingleHomedAlarmResume": hwStackChipSingleHomedAlarmResume,
       "hwStackLeafMemberAdd": hwStackLeafMemberAdd,
       "hwFabricLinkLimitAlarm": hwFabricLinkLimitAlarm,
       "hwFabricLinkLimitAlarmResume": hwFabricLinkLimitAlarmResume,
       "hwStackMemberExceedSpec": hwStackMemberExceedSpec,
       "hwStackMacInconsistence": hwStackMacInconsistence,
       "hwStackMacInconsistenceResume": hwStackMacInconsistenceResume,
       "hwFabricLinkProtocolAlarm": hwFabricLinkProtocolAlarm,
       "hwFabricLinkProtocolAlarmResume": hwFabricLinkProtocolAlarmResume,
       "hwFabricMemberPortProtocolAlarm": hwFabricMemberPortProtocolAlarm,
       "hwFabricMemberPortProtocolAlarmResume": hwFabricMemberPortProtocolAlarmResume,
       "hwLeafMaxNumberExceededAlarm": hwLeafMaxNumberExceededAlarm,
       "hwLeafMaxNumberExceededAlarmResume": hwLeafMaxNumberExceededAlarmResume,
       "hwPhyStackPortErrorDown": hwPhyStackPortErrorDown,
       "hwPhyStackPortErrorDownRecover": hwPhyStackPortErrorDownRecover,
       "hwStackMemberPortEnableTable": hwStackMemberPortEnableTable,
       "hwStackMemberPortEnableEntry": hwStackMemberPortEnableEntry,
       "hwEnableStackMode": hwEnableStackMode,
       "hwAddingPhyPortToStackPortTable": hwAddingPhyPortToStackPortTable,
       "hwAddingPhyPortToStackPortEntry": hwAddingPhyPortToStackPortEntry,
       "hwEnabledStackModePhyPortIndex": hwEnabledStackModePhyPortIndex,
       "hwStackPortID": hwStackPortID,
       "hwStackMemberInformationTable": hwStackMemberInformationTable,
       "hwStackMemberInformationEntry": hwStackMemberInformationEntry,
       "hwStackIdIndex": hwStackIdIndex,
       "hwStackPriority": hwStackPriority,
       "hwStackRole": hwStackRole,
       "hwStackMacAddress": hwStackMacAddress,
       "hwStackDeviceType": hwStackDeviceType,
       "hwStackId": hwStackId,
       "hwStackConfigId": hwStackConfigId,
       "hwStackSysOid": hwStackSysOid,
       "hwStackDescription": hwStackDescription,
       "hwStackCurrentUplinkPort": hwStackCurrentUplinkPort,
       "hwStackConfigUplinkPort": hwStackConfigUplinkPort,
       "hwStackCurrentSwitchMode": hwStackCurrentSwitchMode,
       "hwStackConfigSwitchMode": hwStackConfigSwitchMode,
       "hwAddingPhyPortToFabricPortTable": hwAddingPhyPortToFabricPortTable,
       "hwAddingPhyPortToFabricPortEntry": hwAddingPhyPortToFabricPortEntry,
       "hwEnabledStackModePortIndex": hwEnabledStackModePortIndex,
       "hwFabricPortID": hwFabricPortID,
       "hwFabricPortTable": hwFabricPortTable,
       "hwFabricPortEntry": hwFabricPortEntry,
       "hwFabricPortIndex": hwFabricPortIndex,
       "hwFabricMemberID": hwFabricMemberID,
       "hwFabricLoadBalance": hwFabricLoadBalance,
       "hwFabricProtocolState": hwFabricProtocolState,
       "hwFabricConfiguredLinkNum": hwFabricConfiguredLinkNum,
       "hwFabricPhyLinkTable": hwFabricPhyLinkTable,
       "hwFabricPhyLinkEntry": hwFabricPhyLinkEntry,
       "hwSpinePortIndex": hwSpinePortIndex,
       "hwSpineStackId": hwSpineStackId,
       "hwSpinePortName": hwSpinePortName,
       "hwSpinePortStatus": hwSpinePortStatus,
       "hwLeafPortIndex": hwLeafPortIndex,
       "hwLeafStackId": hwLeafStackId,
       "hwLeafPortName": hwLeafPortName,
       "hwLeafPortStatus": hwLeafPortStatus,
       "hwStackUpgradeTable": hwStackUpgradeTable,
       "hwStackUpgradeEntry": hwStackUpgradeEntry,
       "hwStackUpgradeIndex": hwStackUpgradeIndex,
       "hwStackUpgradeGrpType": hwStackUpgradeGrpType,
       "hwStackUpgradeGrpValue": hwStackUpgradeGrpValue,
       "hwStackUpgradeFileType": hwStackUpgradeFileType,
       "hwStackUpgradeFileInfo": hwStackUpgradeFileInfo,
       "hwStackUpgradeFtpIp": hwStackUpgradeFtpIp,
       "hwStackUpgradeFtpUserName": hwStackUpgradeFtpUserName,
       "hwStackUpgradeFtpPassword": hwStackUpgradeFtpPassword,
       "hwStackUpgradeServerPort": hwStackUpgradeServerPort,
       "hwStackUpgradeFileSize": hwStackUpgradeFileSize,
       "hwStackUpgradeTransmitProtocol": hwStackUpgradeTransmitProtocol,
       "hwStackUpgradeRowStatus": hwStackUpgradeRowStatus,
       "hwStackUpgradeResultTable": hwStackUpgradeResultTable,
       "hwStackUpgradeResultEntry": hwStackUpgradeResultEntry,
       "hwStackUpgradeResultIndex": hwStackUpgradeResultIndex,
       "hwStackUpgradeResultMemberId": hwStackUpgradeResultMemberId,
       "hwStackUpgradeResult": hwStackUpgradeResult,
       "hwStackUpgradeResultInProcess": hwStackUpgradeResultInProcess,
       "hwStackUpgradeResultFailReason": hwStackUpgradeResultFailReason,
       "hwStackTrapObject": hwStackTrapObject,
       "hwStackLocalIfName": hwStackLocalIfName,
       "hwStackPeerIfName": hwStackPeerIfName,
       "hwStackConnectErrReason": hwStackConnectErrReason,
       "hwConfigureFailedStackId": hwConfigureFailedStackId,
       "hwCssTrapErrorPortId": hwCssTrapErrorPortId,
       "hwStackConnectMethod": hwStackConnectMethod,
       "hwStackCfgConflictStackId": hwStackCfgConflictStackId,
       "hwStackFabricPort": hwStackFabricPort,
       "hwStackFabricMemberPort": hwStackFabricMemberPort,
       "hwStackMemberId": hwStackMemberId,
       "hwStackLeafMemberId": hwStackLeafMemberId,
       "hwStackReason": hwStackReason,
       "hwStackLeafPort": hwStackLeafPort,
       "hwStackCurrentLinkNum": hwStackCurrentLinkNum,
       "hwFabricCurrentLinkNum": hwFabricCurrentLinkNum,
       "hwStackErrorDownRecoverReason": hwStackErrorDownRecoverReason,
       "hwCssObject": hwCssObject,
       "hwCssGlobalObject": hwCssGlobalObject,
       "hwCssEnable": hwCssEnable,
       "hwCssMemberInfoTable": hwCssMemberInfoTable,
       "hwCssMemberInfoEntry": hwCssMemberInfoEntry,
       "hwCssMemberFrameId": hwCssMemberFrameId,
       "hwCssMemberConfigFrameId": hwCssMemberConfigFrameId,
       "hwCssMemberPriority": hwCssMemberPriority,
       "hwCssMemberConfigPriority": hwCssMemberConfigPriority,
       "hwCssMemberMasterForce": hwCssMemberMasterForce,
       "hwCssMemberConfigMasterForce": hwCssMemberConfigMasterForce,
       "hwCssMemberConfigEnable": hwCssMemberConfigEnable,
       "hwCssMemberRole": hwCssMemberRole,
       "hwCssTrap": hwCssTrap,
       "hwCssTrapObjects": hwCssTrapObjects,
       "hwCssTrapFrameId1": hwCssTrapFrameId1,
       "hwCssTrapSlotId1": hwCssTrapSlotId1,
       "hwCssTrapPortId1": hwCssTrapPortId1,
       "hwCssTrapFrameId2": hwCssTrapFrameId2,
       "hwCssTrapSlotId2": hwCssTrapSlotId2,
       "hwCssTrapPortId2": hwCssTrapPortId2,
       "hwCssTrapFrameId3": hwCssTrapFrameId3,
       "hwCssTrapSlotId3": hwCssTrapSlotId3,
       "hwCssTrapPortId3": hwCssTrapPortId3,
       "hwCssTrapConfigureFailedSlotId": hwCssTrapConfigureFailedSlotId,
       "hwCssTraps": hwCssTraps,
       "hwCssLinkDown": hwCssLinkDown,
       "hwCssLinkUp": hwCssLinkUp,
       "hwCssSwitchOver": hwCssSwitchOver,
       "hwCssConnectError": hwCssConnectError,
       "hwCssSplit": hwCssSplit,
       "hwCssEstablish": hwCssEstablish,
       "hwCssFastUpgradeFail": hwCssFastUpgradeFail,
       "hwCssPhyCsuConnectError": hwCssPhyCsuConnectError,
       "hwCssLpuInvalidLicense": hwCssLpuInvalidLicense,
       "hwCssPortConfigureFailed": hwCssPortConfigureFailed,
       "hwCssPortUpDownAlarm": hwCssPortUpDownAlarm,
       "hwCssPortCrcErrorAlarm": hwCssPortCrcErrorAlarm,
       "hwCssPortErrorDown": hwCssPortErrorDown,
       "hwCssPortErrorDownRecover": hwCssPortErrorDownRecover,
       "hwCssPhyVs08ConnectError": hwCssPhyVs08ConnectError,
       "hwCssStandbyError": hwCssStandbyError,
       "hwCssStandbyErrorRestore": hwCssStandbyErrorRestore,
       "hwCssPortStateError": hwCssPortStateError,
       "hwCssPhyCardConnectError": hwCssPhyCardConnectError,
       "hwCssPortInfoTable": hwCssPortInfoTable,
       "hwCssPortInfoEntry": hwCssPortInfoEntry,
       "hwCssPortFrameId": hwCssPortFrameId,
       "hwCssPortSlotId": hwCssPortSlotId,
       "hwCssPortCardId": hwCssPortCardId,
       "hwCssPortPortId": hwCssPortPortId,
       "hwCssPortName": hwCssPortName,
       "hwCssPortSpeed": hwCssPortSpeed,
       "hwCssPortOperStatus": hwCssPortOperStatus,
       "hwCssPortAdminStatus": hwCssPortAdminStatus,
       "hwCssPortInOctets": hwCssPortInOctets,
       "hwCssPortInUcastPkts": hwCssPortInUcastPkts,
       "hwCssPortInMcastPkts": hwCssPortInMcastPkts,
       "hwCssPortInBcastPkts": hwCssPortInBcastPkts,
       "hwCssPortInDiscards": hwCssPortInDiscards,
       "hwCssPortInErrors": hwCssPortInErrors,
       "hwCssPortInCRCErrors": hwCssPortInCRCErrors,
       "hwCssPortOutOctets": hwCssPortOutOctets,
       "hwCssPortOutUcastPkts": hwCssPortOutUcastPkts,
       "hwCssPortOutMcastPkts": hwCssPortOutMcastPkts,
       "hwCssPortOutBcastPkts": hwCssPortOutBcastPkts,
       "hwCssPortOutDiscards": hwCssPortOutDiscards,
       "hwCssPortOutErrors": hwCssPortOutErrors,
       "hwCssLinkInfoTable": hwCssLinkInfoTable,
       "hwCssLinkInfoEntry": hwCssLinkInfoEntry,
       "hwCssLinkLocFrameId": hwCssLinkLocFrameId,
       "hwCssLinkLocSlotId": hwCssLinkLocSlotId,
       "hwCssLinkLocCardId": hwCssLinkLocCardId,
       "hwCssLinkLocPortId": hwCssLinkLocPortId,
       "hwCssLinkLocPortName": hwCssLinkLocPortName,
       "hwCssLinkRemFrameId": hwCssLinkRemFrameId,
       "hwCssLinkRemSlotId": hwCssLinkRemSlotId,
       "hwCssLinkRemCardId": hwCssLinkRemCardId,
       "hwCssLinkRemPortId": hwCssLinkRemPortId,
       "hwCssLinkRemPortName": hwCssLinkRemPortName,
       "hwCssLinkSpeed": hwCssLinkSpeed,
       "hwStackConformance": hwStackConformance,
       "hwStackCompliances": hwStackCompliances,
       "hwStackCompliance": hwStackCompliance,
       "hwStackGroups": hwStackGroups,
       "hwStackObjectGroup": hwStackObjectGroup,
       "hwStackNotificationGroup": hwStackNotificationGroup,
       "hwStackTrapGroup": hwStackTrapGroup,
       "hwCssConformance": hwCssConformance,
       "hwCssCompliances": hwCssCompliances,
       "hwCssCompliance": hwCssCompliance,
       "hwCssGroups": hwCssGroups,
       "hwCssObjectGroup": hwCssObjectGroup,
       "hwCssTrapObjectGroup": hwCssTrapObjectGroup,
       "hwCssNotificationGroup": hwCssNotificationGroup}
)
