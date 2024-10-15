# SNMP MIB module (HPN-ICF-COMMON-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-COMMON-SYSTEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:59:35 2024
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

(hpnicf,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicf")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

hpnicfSystem = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 6)
)
hpnicfSystem.setRevisions(
        ("2004-06-30 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _HpnicfWriteConfig_Type(Integer32):
    """Custom type hpnicfWriteConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("save", 1)
    )


_HpnicfWriteConfig_Type.__name__ = "Integer32"
_HpnicfWriteConfig_Object = MibScalar
hpnicfWriteConfig = _HpnicfWriteConfig_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 6, 5),
    _HpnicfWriteConfig_Type()
)
hpnicfWriteConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfWriteConfig.setStatus("current")


class _HpnicfStartFtpServer_Type(Integer32):
    """Custom type hpnicfStartFtpServer based on Integer32"""
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


_HpnicfStartFtpServer_Type.__name__ = "Integer32"
_HpnicfStartFtpServer_Object = MibScalar
hpnicfStartFtpServer = _HpnicfStartFtpServer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 6, 6),
    _HpnicfStartFtpServer_Type()
)
hpnicfStartFtpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfStartFtpServer.setStatus("current")


class _HpnicfReboot_Type(Integer32):
    """Custom type hpnicfReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("reboot", 1))
    )


_HpnicfReboot_Type.__name__ = "Integer32"
_HpnicfReboot_Object = MibScalar
hpnicfReboot = _HpnicfReboot_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 6, 7),
    _HpnicfReboot_Type()
)
hpnicfReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfReboot.setStatus("current")
_HpnicfSystemNotification_ObjectIdentity = ObjectIdentity
hpnicfSystemNotification = _HpnicfSystemNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 6, 8)
)
_HpnicfSoftwareVersion_Type = DisplayString
_HpnicfSoftwareVersion_Object = MibScalar
hpnicfSoftwareVersion = _HpnicfSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 6, 9),
    _HpnicfSoftwareVersion_Type()
)
hpnicfSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSoftwareVersion.setStatus("current")


class _HpnicfSysBootType_Type(Integer32):
    """Custom type hpnicfSysBootType based on Integer32"""
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


_HpnicfSysBootType_Type.__name__ = "Integer32"
_HpnicfSysBootType_Object = MibScalar
hpnicfSysBootType = _HpnicfSysBootType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 6, 10),
    _HpnicfSysBootType_Type()
)
hpnicfSysBootType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSysBootType.setStatus("current")
_HpnicfSystemInfo_ObjectIdentity = ObjectIdentity
hpnicfSystemInfo = _HpnicfSystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 6, 11)
)


class _HpnicfSysStatisticPeriod_Type(Integer32):
    """Custom type hpnicfSysStatisticPeriod based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_HpnicfSysStatisticPeriod_Type.__name__ = "Integer32"
_HpnicfSysStatisticPeriod_Object = MibScalar
hpnicfSysStatisticPeriod = _HpnicfSysStatisticPeriod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 6, 11, 1),
    _HpnicfSysStatisticPeriod_Type()
)
hpnicfSysStatisticPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSysStatisticPeriod.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfSysStatisticPeriod.setUnits("seconds")


class _HpnicfSysSamplePeriod_Type(Integer32):
    """Custom type hpnicfSysSamplePeriod based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_HpnicfSysSamplePeriod_Type.__name__ = "Integer32"
_HpnicfSysSamplePeriod_Object = MibScalar
hpnicfSysSamplePeriod = _HpnicfSysSamplePeriod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 6, 11, 2),
    _HpnicfSysSamplePeriod_Type()
)
hpnicfSysSamplePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSysSamplePeriod.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfSysSamplePeriod.setUnits("seconds")


class _HpnicfSysTrapResendPeriod_Type(Integer32):
    """Custom type hpnicfSysTrapResendPeriod based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_HpnicfSysTrapResendPeriod_Type.__name__ = "Integer32"
_HpnicfSysTrapResendPeriod_Object = MibScalar
hpnicfSysTrapResendPeriod = _HpnicfSysTrapResendPeriod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 6, 11, 3),
    _HpnicfSysTrapResendPeriod_Type()
)
hpnicfSysTrapResendPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSysTrapResendPeriod.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfSysTrapResendPeriod.setUnits("seconds")


class _HpnicfSysTrapCollectionPeriod_Type(Integer32):
    """Custom type hpnicfSysTrapCollectionPeriod based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_HpnicfSysTrapCollectionPeriod_Type.__name__ = "Integer32"
_HpnicfSysTrapCollectionPeriod_Object = MibScalar
hpnicfSysTrapCollectionPeriod = _HpnicfSysTrapCollectionPeriod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 6, 11, 4),
    _HpnicfSysTrapCollectionPeriod_Type()
)
hpnicfSysTrapCollectionPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSysTrapCollectionPeriod.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfSysTrapCollectionPeriod.setUnits("seconds")
_HpnicfSysSnmpPort_Type = Integer32
_HpnicfSysSnmpPort_Object = MibScalar
hpnicfSysSnmpPort = _HpnicfSysSnmpPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 6, 11, 5),
    _HpnicfSysSnmpPort_Type()
)
hpnicfSysSnmpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSysSnmpPort.setStatus("current")
_HpnicfSysSnmpTrapPort_Type = Integer32
_HpnicfSysSnmpTrapPort_Object = MibScalar
hpnicfSysSnmpTrapPort = _HpnicfSysSnmpTrapPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 6, 11, 6),
    _HpnicfSysSnmpTrapPort_Type()
)
hpnicfSysSnmpTrapPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSysSnmpTrapPort.setStatus("current")


class _HpnicfSysNetID_Type(OctetString):
    """Custom type hpnicfSysNetID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_HpnicfSysNetID_Type.__name__ = "OctetString"
_HpnicfSysNetID_Object = MibScalar
hpnicfSysNetID = _HpnicfSysNetID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 6, 11, 7),
    _HpnicfSysNetID_Type()
)
hpnicfSysNetID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSysNetID.setStatus("current")
_HpnicfSysLastSampleTime_Type = DateAndTime
_HpnicfSysLastSampleTime_Object = MibScalar
hpnicfSysLastSampleTime = _HpnicfSysLastSampleTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 6, 11, 8),
    _HpnicfSysLastSampleTime_Type()
)
hpnicfSysLastSampleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSysLastSampleTime.setStatus("current")


class _HpnicfSysTrapSendNum_Type(Integer32):
    """Custom type hpnicfSysTrapSendNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_HpnicfSysTrapSendNum_Type.__name__ = "Integer32"
_HpnicfSysTrapSendNum_Object = MibScalar
hpnicfSysTrapSendNum = _HpnicfSysTrapSendNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 6, 11, 9),
    _HpnicfSysTrapSendNum_Type()
)
hpnicfSysTrapSendNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSysTrapSendNum.setStatus("current")
_HpnicfSysFirstTrapTime_Type = TimeTicks
_HpnicfSysFirstTrapTime_Object = MibScalar
hpnicfSysFirstTrapTime = _HpnicfSysFirstTrapTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 6, 11, 10),
    _HpnicfSysFirstTrapTime_Type()
)
hpnicfSysFirstTrapTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfSysFirstTrapTime.setStatus("current")


class _HpnicfSysBannerMOTD_Type(OctetString):
    """Custom type hpnicfSysBannerMOTD based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2000),
    )


_HpnicfSysBannerMOTD_Type.__name__ = "OctetString"
_HpnicfSysBannerMOTD_Object = MibScalar
hpnicfSysBannerMOTD = _HpnicfSysBannerMOTD_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 6, 11, 11),
    _HpnicfSysBannerMOTD_Type()
)
hpnicfSysBannerMOTD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSysBannerMOTD.setStatus("current")
_HpnicfSystemNotificationInfo_ObjectIdentity = ObjectIdentity
hpnicfSystemNotificationInfo = _HpnicfSystemNotificationInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 6, 12)
)
_HpnicfSysLoghostIndex_Type = Integer32
_HpnicfSysLoghostIndex_Object = MibScalar
hpnicfSysLoghostIndex = _HpnicfSysLoghostIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 6, 12, 1),
    _HpnicfSysLoghostIndex_Type()
)
hpnicfSysLoghostIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfSysLoghostIndex.setStatus("current")
_HpnicfSysLoghostIpaddressType_Type = InetAddressType
_HpnicfSysLoghostIpaddressType_Object = MibScalar
hpnicfSysLoghostIpaddressType = _HpnicfSysLoghostIpaddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 6, 12, 2),
    _HpnicfSysLoghostIpaddressType_Type()
)
hpnicfSysLoghostIpaddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfSysLoghostIpaddressType.setStatus("current")
_HpnicfSysLoghostIpaddress_Type = InetAddress
_HpnicfSysLoghostIpaddress_Object = MibScalar
hpnicfSysLoghostIpaddress = _HpnicfSysLoghostIpaddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 6, 12, 3),
    _HpnicfSysLoghostIpaddress_Type()
)
hpnicfSysLoghostIpaddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfSysLoghostIpaddress.setStatus("current")


class _HpnicfSysLoghostTrapVpnName_Type(DisplayString):
    """Custom type hpnicfSysLoghostTrapVpnName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HpnicfSysLoghostTrapVpnName_Type.__name__ = "DisplayString"
_HpnicfSysLoghostTrapVpnName_Object = MibScalar
hpnicfSysLoghostTrapVpnName = _HpnicfSysLoghostTrapVpnName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 6, 12, 4),
    _HpnicfSysLoghostTrapVpnName_Type()
)
hpnicfSysLoghostTrapVpnName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfSysLoghostTrapVpnName.setStatus("current")

# Managed Objects groups


# Notification objects

hpnicfWriteSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 6, 8, 1)
)
if mibBuilder.loadTexts:
    hpnicfWriteSuccessTrap.setStatus(
        "current"
    )

hpnicfWriteFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 6, 8, 2)
)
if mibBuilder.loadTexts:
    hpnicfWriteFailureTrap.setStatus(
        "current"
    )

hpnicfRebootSendTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 6, 8, 3)
)
if mibBuilder.loadTexts:
    hpnicfRebootSendTrap.setStatus(
        "current"
    )

hpnicfSysColdStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 6, 8, 4)
)
hpnicfSysColdStartTrap.setObjects(
    ("HPN-ICF-COMMON-SYSTEM-MIB", "hpnicfSysFirstTrapTime")
)
if mibBuilder.loadTexts:
    hpnicfSysColdStartTrap.setStatus(
        "current"
    )

hpnicfSysWarmStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 6, 8, 5)
)
hpnicfSysWarmStartTrap.setObjects(
    ("HPN-ICF-COMMON-SYSTEM-MIB", "hpnicfSysFirstTrapTime")
)
if mibBuilder.loadTexts:
    hpnicfSysWarmStartTrap.setStatus(
        "current"
    )

hpnicfSysLoghostUnreachableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 6, 8, 6)
)
hpnicfSysLoghostUnreachableTrap.setObjects(
      *(("HPN-ICF-COMMON-SYSTEM-MIB", "hpnicfSysLoghostIndex"),
        ("HPN-ICF-COMMON-SYSTEM-MIB", "hpnicfSysLoghostIpaddressType"),
        ("HPN-ICF-COMMON-SYSTEM-MIB", "hpnicfSysLoghostIpaddress"),
        ("HPN-ICF-COMMON-SYSTEM-MIB", "hpnicfSysLoghostTrapVpnName"))
)
if mibBuilder.loadTexts:
    hpnicfSysLoghostUnreachableTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-COMMON-SYSTEM-MIB",
    **{"hpnicfSystem": hpnicfSystem,
       "hpnicfWriteConfig": hpnicfWriteConfig,
       "hpnicfStartFtpServer": hpnicfStartFtpServer,
       "hpnicfReboot": hpnicfReboot,
       "hpnicfSystemNotification": hpnicfSystemNotification,
       "hpnicfWriteSuccessTrap": hpnicfWriteSuccessTrap,
       "hpnicfWriteFailureTrap": hpnicfWriteFailureTrap,
       "hpnicfRebootSendTrap": hpnicfRebootSendTrap,
       "hpnicfSysColdStartTrap": hpnicfSysColdStartTrap,
       "hpnicfSysWarmStartTrap": hpnicfSysWarmStartTrap,
       "hpnicfSysLoghostUnreachableTrap": hpnicfSysLoghostUnreachableTrap,
       "hpnicfSoftwareVersion": hpnicfSoftwareVersion,
       "hpnicfSysBootType": hpnicfSysBootType,
       "hpnicfSystemInfo": hpnicfSystemInfo,
       "hpnicfSysStatisticPeriod": hpnicfSysStatisticPeriod,
       "hpnicfSysSamplePeriod": hpnicfSysSamplePeriod,
       "hpnicfSysTrapResendPeriod": hpnicfSysTrapResendPeriod,
       "hpnicfSysTrapCollectionPeriod": hpnicfSysTrapCollectionPeriod,
       "hpnicfSysSnmpPort": hpnicfSysSnmpPort,
       "hpnicfSysSnmpTrapPort": hpnicfSysSnmpTrapPort,
       "hpnicfSysNetID": hpnicfSysNetID,
       "hpnicfSysLastSampleTime": hpnicfSysLastSampleTime,
       "hpnicfSysTrapSendNum": hpnicfSysTrapSendNum,
       "hpnicfSysFirstTrapTime": hpnicfSysFirstTrapTime,
       "hpnicfSysBannerMOTD": hpnicfSysBannerMOTD,
       "hpnicfSystemNotificationInfo": hpnicfSystemNotificationInfo,
       "hpnicfSysLoghostIndex": hpnicfSysLoghostIndex,
       "hpnicfSysLoghostIpaddressType": hpnicfSysLoghostIpaddressType,
       "hpnicfSysLoghostIpaddress": hpnicfSysLoghostIpaddress,
       "hpnicfSysLoghostTrapVpnName": hpnicfSysLoghostTrapVpnName}
)
