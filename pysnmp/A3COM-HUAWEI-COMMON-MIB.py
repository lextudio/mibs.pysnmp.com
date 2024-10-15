# SNMP MIB module (A3COM-HUAWEI-COMMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-COMMON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:27:25 2024
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

(hwSystem,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "hwSystem")

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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _HwWriteConfig_Type(Integer32):
    """Custom type hwWriteConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("save", 1)
    )


_HwWriteConfig_Type.__name__ = "Integer32"
_HwWriteConfig_Object = MibScalar
hwWriteConfig = _HwWriteConfig_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 6, 5),
    _HwWriteConfig_Type()
)
hwWriteConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWriteConfig.setStatus("current")


class _HwStartFtpServer_Type(Integer32):
    """Custom type hwStartFtpServer based on Integer32"""
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


_HwStartFtpServer_Type.__name__ = "Integer32"
_HwStartFtpServer_Object = MibScalar
hwStartFtpServer = _HwStartFtpServer_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 6, 6),
    _HwStartFtpServer_Type()
)
hwStartFtpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwStartFtpServer.setStatus("current")


class _HwReboot_Type(Integer32):
    """Custom type hwReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reboot", 1)
    )


_HwReboot_Type.__name__ = "Integer32"
_HwReboot_Object = MibScalar
hwReboot = _HwReboot_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 6, 7),
    _HwReboot_Type()
)
hwReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwReboot.setStatus("current")
_HwSystemNotification_ObjectIdentity = ObjectIdentity
hwSystemNotification = _HwSystemNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 6, 8)
)
_HwSoftwareVersion_Type = DisplayString
_HwSoftwareVersion_Object = MibScalar
hwSoftwareVersion = _HwSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 6, 9),
    _HwSoftwareVersion_Type()
)
hwSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSoftwareVersion.setStatus("current")


class _HwSysBootType_Type(Integer32):
    """Custom type hwSysBootType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("coldStart", 1),
          ("warmStart", 2))
    )


_HwSysBootType_Type.__name__ = "Integer32"
_HwSysBootType_Object = MibScalar
hwSysBootType = _HwSysBootType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 6, 10),
    _HwSysBootType_Type()
)
hwSysBootType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSysBootType.setStatus("current")
_HwSystemInfo_ObjectIdentity = ObjectIdentity
hwSystemInfo = _HwSystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 6, 11)
)


class _HwSysStatisticPeriod_Type(Integer32):
    """Custom type hwSysStatisticPeriod based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_HwSysStatisticPeriod_Type.__name__ = "Integer32"
_HwSysStatisticPeriod_Object = MibScalar
hwSysStatisticPeriod = _HwSysStatisticPeriod_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 6, 11, 1),
    _HwSysStatisticPeriod_Type()
)
hwSysStatisticPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSysStatisticPeriod.setStatus("current")
if mibBuilder.loadTexts:
    hwSysStatisticPeriod.setUnits("seconds")


class _HwSysSamplePeriod_Type(Integer32):
    """Custom type hwSysSamplePeriod based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_HwSysSamplePeriod_Type.__name__ = "Integer32"
_HwSysSamplePeriod_Object = MibScalar
hwSysSamplePeriod = _HwSysSamplePeriod_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 6, 11, 2),
    _HwSysSamplePeriod_Type()
)
hwSysSamplePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSysSamplePeriod.setStatus("current")
if mibBuilder.loadTexts:
    hwSysSamplePeriod.setUnits("seconds")


class _HwSysTrapResendPeriod_Type(Integer32):
    """Custom type hwSysTrapResendPeriod based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_HwSysTrapResendPeriod_Type.__name__ = "Integer32"
_HwSysTrapResendPeriod_Object = MibScalar
hwSysTrapResendPeriod = _HwSysTrapResendPeriod_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 6, 11, 3),
    _HwSysTrapResendPeriod_Type()
)
hwSysTrapResendPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSysTrapResendPeriod.setStatus("current")
if mibBuilder.loadTexts:
    hwSysTrapResendPeriod.setUnits("seconds")


class _HwSysTrapCollectionPeriod_Type(Integer32):
    """Custom type hwSysTrapCollectionPeriod based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_HwSysTrapCollectionPeriod_Type.__name__ = "Integer32"
_HwSysTrapCollectionPeriod_Object = MibScalar
hwSysTrapCollectionPeriod = _HwSysTrapCollectionPeriod_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 6, 11, 4),
    _HwSysTrapCollectionPeriod_Type()
)
hwSysTrapCollectionPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSysTrapCollectionPeriod.setStatus("current")
if mibBuilder.loadTexts:
    hwSysTrapCollectionPeriod.setUnits("seconds")
_HwSysSnmpPort_Type = Integer32
_HwSysSnmpPort_Object = MibScalar
hwSysSnmpPort = _HwSysSnmpPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 6, 11, 5),
    _HwSysSnmpPort_Type()
)
hwSysSnmpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSysSnmpPort.setStatus("current")
_HwSysSnmpTrapPort_Type = Integer32
_HwSysSnmpTrapPort_Object = MibScalar
hwSysSnmpTrapPort = _HwSysSnmpTrapPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 6, 11, 6),
    _HwSysSnmpTrapPort_Type()
)
hwSysSnmpTrapPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSysSnmpTrapPort.setStatus("current")


class _HwSysNetID_Type(OctetString):
    """Custom type hwSysNetID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_HwSysNetID_Type.__name__ = "OctetString"
_HwSysNetID_Object = MibScalar
hwSysNetID = _HwSysNetID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 6, 11, 7),
    _HwSysNetID_Type()
)
hwSysNetID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSysNetID.setStatus("current")
_HwSysLastSampleTime_Type = DateAndTime
_HwSysLastSampleTime_Object = MibScalar
hwSysLastSampleTime = _HwSysLastSampleTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 6, 11, 8),
    _HwSysLastSampleTime_Type()
)
hwSysLastSampleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSysLastSampleTime.setStatus("current")


class _HwSysTrapSendNum_Type(Integer32):
    """Custom type hwSysTrapSendNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_HwSysTrapSendNum_Type.__name__ = "Integer32"
_HwSysTrapSendNum_Object = MibScalar
hwSysTrapSendNum = _HwSysTrapSendNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 6, 11, 9),
    _HwSysTrapSendNum_Type()
)
hwSysTrapSendNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSysTrapSendNum.setStatus("current")
_HwSysFirstTrapTime_Type = TimeTicks
_HwSysFirstTrapTime_Object = MibScalar
hwSysFirstTrapTime = _HwSysFirstTrapTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 6, 11, 10),
    _HwSysFirstTrapTime_Type()
)
hwSysFirstTrapTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwSysFirstTrapTime.setStatus("current")

# Managed Objects groups


# Notification objects

hwWriteSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 6, 8, 1)
)
if mibBuilder.loadTexts:
    hwWriteSuccessTrap.setStatus(
        "current"
    )

hwWriteFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 6, 8, 2)
)
if mibBuilder.loadTexts:
    hwWriteFailureTrap.setStatus(
        "current"
    )

hwRebootSendTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 6, 8, 3)
)
if mibBuilder.loadTexts:
    hwRebootSendTrap.setStatus(
        "current"
    )

hwSysColdStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 6, 8, 4)
)
hwSysColdStartTrap.setObjects(
    ("A3COM-HUAWEI-COMMON-MIB", "hwSysFirstTrapTime")
)
if mibBuilder.loadTexts:
    hwSysColdStartTrap.setStatus(
        "current"
    )

hwSysWarmStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 6, 8, 5)
)
hwSysWarmStartTrap.setObjects(
    ("A3COM-HUAWEI-COMMON-MIB", "hwSysFirstTrapTime")
)
if mibBuilder.loadTexts:
    hwSysWarmStartTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-COMMON-MIB",
    **{"hwWriteConfig": hwWriteConfig,
       "hwStartFtpServer": hwStartFtpServer,
       "hwReboot": hwReboot,
       "hwSystemNotification": hwSystemNotification,
       "hwWriteSuccessTrap": hwWriteSuccessTrap,
       "hwWriteFailureTrap": hwWriteFailureTrap,
       "hwRebootSendTrap": hwRebootSendTrap,
       "hwSysColdStartTrap": hwSysColdStartTrap,
       "hwSysWarmStartTrap": hwSysWarmStartTrap,
       "hwSoftwareVersion": hwSoftwareVersion,
       "hwSysBootType": hwSysBootType,
       "hwSystemInfo": hwSystemInfo,
       "hwSysStatisticPeriod": hwSysStatisticPeriod,
       "hwSysSamplePeriod": hwSysSamplePeriod,
       "hwSysTrapResendPeriod": hwSysTrapResendPeriod,
       "hwSysTrapCollectionPeriod": hwSysTrapCollectionPeriod,
       "hwSysSnmpPort": hwSysSnmpPort,
       "hwSysSnmpTrapPort": hwSysSnmpTrapPort,
       "hwSysNetID": hwSysNetID,
       "hwSysLastSampleTime": hwSysLastSampleTime,
       "hwSysTrapSendNum": hwSysTrapSendNum,
       "hwSysFirstTrapTime": hwSysFirstTrapTime}
)
