# SNMP MIB module (HH3C-COMMON-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-COMMON-SYSTEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:52:35 2024
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

(hh3cSystem,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cSystem")

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



class _Hh3cWriteConfig_Type(Integer32):
    """Custom type hh3cWriteConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("save", 1)
    )


_Hh3cWriteConfig_Type.__name__ = "Integer32"
_Hh3cWriteConfig_Object = MibScalar
hh3cWriteConfig = _Hh3cWriteConfig_Object(
    (1, 3, 6, 1, 4, 1, 25506, 6, 5),
    _Hh3cWriteConfig_Type()
)
hh3cWriteConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWriteConfig.setStatus("current")


class _Hh3cStartFtpServer_Type(Integer32):
    """Custom type hh3cStartFtpServer based on Integer32"""
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


_Hh3cStartFtpServer_Type.__name__ = "Integer32"
_Hh3cStartFtpServer_Object = MibScalar
hh3cStartFtpServer = _Hh3cStartFtpServer_Object(
    (1, 3, 6, 1, 4, 1, 25506, 6, 6),
    _Hh3cStartFtpServer_Type()
)
hh3cStartFtpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cStartFtpServer.setStatus("current")


class _Hh3cReboot_Type(Integer32):
    """Custom type hh3cReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reboot", 1)
    )


_Hh3cReboot_Type.__name__ = "Integer32"
_Hh3cReboot_Object = MibScalar
hh3cReboot = _Hh3cReboot_Object(
    (1, 3, 6, 1, 4, 1, 25506, 6, 7),
    _Hh3cReboot_Type()
)
hh3cReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cReboot.setStatus("current")
_Hh3cSystemNotification_ObjectIdentity = ObjectIdentity
hh3cSystemNotification = _Hh3cSystemNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 6, 8)
)
_Hh3cSoftwareVersion_Type = DisplayString
_Hh3cSoftwareVersion_Object = MibScalar
hh3cSoftwareVersion = _Hh3cSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 6, 9),
    _Hh3cSoftwareVersion_Type()
)
hh3cSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSoftwareVersion.setStatus("current")


class _Hh3cSysBootType_Type(Integer32):
    """Custom type hh3cSysBootType based on Integer32"""
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


_Hh3cSysBootType_Type.__name__ = "Integer32"
_Hh3cSysBootType_Object = MibScalar
hh3cSysBootType = _Hh3cSysBootType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 6, 10),
    _Hh3cSysBootType_Type()
)
hh3cSysBootType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSysBootType.setStatus("current")
_Hh3cSystemInfo_ObjectIdentity = ObjectIdentity
hh3cSystemInfo = _Hh3cSystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 6, 11)
)


class _Hh3cSysStatisticPeriod_Type(Integer32):
    """Custom type hh3cSysStatisticPeriod based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_Hh3cSysStatisticPeriod_Type.__name__ = "Integer32"
_Hh3cSysStatisticPeriod_Object = MibScalar
hh3cSysStatisticPeriod = _Hh3cSysStatisticPeriod_Object(
    (1, 3, 6, 1, 4, 1, 25506, 6, 11, 1),
    _Hh3cSysStatisticPeriod_Type()
)
hh3cSysStatisticPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSysStatisticPeriod.setStatus("current")
if mibBuilder.loadTexts:
    hh3cSysStatisticPeriod.setUnits("seconds")


class _Hh3cSysSamplePeriod_Type(Integer32):
    """Custom type hh3cSysSamplePeriod based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_Hh3cSysSamplePeriod_Type.__name__ = "Integer32"
_Hh3cSysSamplePeriod_Object = MibScalar
hh3cSysSamplePeriod = _Hh3cSysSamplePeriod_Object(
    (1, 3, 6, 1, 4, 1, 25506, 6, 11, 2),
    _Hh3cSysSamplePeriod_Type()
)
hh3cSysSamplePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSysSamplePeriod.setStatus("current")
if mibBuilder.loadTexts:
    hh3cSysSamplePeriod.setUnits("seconds")


class _Hh3cSysTrapResendPeriod_Type(Integer32):
    """Custom type hh3cSysTrapResendPeriod based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_Hh3cSysTrapResendPeriod_Type.__name__ = "Integer32"
_Hh3cSysTrapResendPeriod_Object = MibScalar
hh3cSysTrapResendPeriod = _Hh3cSysTrapResendPeriod_Object(
    (1, 3, 6, 1, 4, 1, 25506, 6, 11, 3),
    _Hh3cSysTrapResendPeriod_Type()
)
hh3cSysTrapResendPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSysTrapResendPeriod.setStatus("current")
if mibBuilder.loadTexts:
    hh3cSysTrapResendPeriod.setUnits("seconds")


class _Hh3cSysTrapCollectionPeriod_Type(Integer32):
    """Custom type hh3cSysTrapCollectionPeriod based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_Hh3cSysTrapCollectionPeriod_Type.__name__ = "Integer32"
_Hh3cSysTrapCollectionPeriod_Object = MibScalar
hh3cSysTrapCollectionPeriod = _Hh3cSysTrapCollectionPeriod_Object(
    (1, 3, 6, 1, 4, 1, 25506, 6, 11, 4),
    _Hh3cSysTrapCollectionPeriod_Type()
)
hh3cSysTrapCollectionPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSysTrapCollectionPeriod.setStatus("current")
if mibBuilder.loadTexts:
    hh3cSysTrapCollectionPeriod.setUnits("seconds")
_Hh3cSysSnmpPort_Type = Integer32
_Hh3cSysSnmpPort_Object = MibScalar
hh3cSysSnmpPort = _Hh3cSysSnmpPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 6, 11, 5),
    _Hh3cSysSnmpPort_Type()
)
hh3cSysSnmpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSysSnmpPort.setStatus("current")
_Hh3cSysSnmpTrapPort_Type = Integer32
_Hh3cSysSnmpTrapPort_Object = MibScalar
hh3cSysSnmpTrapPort = _Hh3cSysSnmpTrapPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 6, 11, 6),
    _Hh3cSysSnmpTrapPort_Type()
)
hh3cSysSnmpTrapPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSysSnmpTrapPort.setStatus("current")


class _Hh3cSysNetID_Type(OctetString):
    """Custom type hh3cSysNetID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cSysNetID_Type.__name__ = "OctetString"
_Hh3cSysNetID_Object = MibScalar
hh3cSysNetID = _Hh3cSysNetID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 6, 11, 7),
    _Hh3cSysNetID_Type()
)
hh3cSysNetID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSysNetID.setStatus("current")
_Hh3cSysLastSampleTime_Type = DateAndTime
_Hh3cSysLastSampleTime_Object = MibScalar
hh3cSysLastSampleTime = _Hh3cSysLastSampleTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 6, 11, 8),
    _Hh3cSysLastSampleTime_Type()
)
hh3cSysLastSampleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSysLastSampleTime.setStatus("current")

# Managed Objects groups


# Notification objects

hh3cWriteSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 6, 8, 1)
)
if mibBuilder.loadTexts:
    hh3cWriteSuccessTrap.setStatus(
        "current"
    )

hh3cWriteFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 6, 8, 2)
)
if mibBuilder.loadTexts:
    hh3cWriteFailureTrap.setStatus(
        "current"
    )

hh3cRebootSendTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 6, 8, 3)
)
if mibBuilder.loadTexts:
    hh3cRebootSendTrap.setStatus(
        "current"
    )

hh3cSysColdStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 6, 8, 4)
)
if mibBuilder.loadTexts:
    hh3cSysColdStartTrap.setStatus(
        "current"
    )

hh3cSysWarmStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 6, 8, 5)
)
if mibBuilder.loadTexts:
    hh3cSysWarmStartTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-COMMON-SYSTEM-MIB",
    **{"hh3cWriteConfig": hh3cWriteConfig,
       "hh3cStartFtpServer": hh3cStartFtpServer,
       "hh3cReboot": hh3cReboot,
       "hh3cSystemNotification": hh3cSystemNotification,
       "hh3cWriteSuccessTrap": hh3cWriteSuccessTrap,
       "hh3cWriteFailureTrap": hh3cWriteFailureTrap,
       "hh3cRebootSendTrap": hh3cRebootSendTrap,
       "hh3cSysColdStartTrap": hh3cSysColdStartTrap,
       "hh3cSysWarmStartTrap": hh3cSysWarmStartTrap,
       "hh3cSoftwareVersion": hh3cSoftwareVersion,
       "hh3cSysBootType": hh3cSysBootType,
       "hh3cSystemInfo": hh3cSystemInfo,
       "hh3cSysStatisticPeriod": hh3cSysStatisticPeriod,
       "hh3cSysSamplePeriod": hh3cSysSamplePeriod,
       "hh3cSysTrapResendPeriod": hh3cSysTrapResendPeriod,
       "hh3cSysTrapCollectionPeriod": hh3cSysTrapCollectionPeriod,
       "hh3cSysSnmpPort": hh3cSysSnmpPort,
       "hh3cSysSnmpTrapPort": hh3cSysSnmpTrapPort,
       "hh3cSysNetID": hh3cSysNetID,
       "hh3cSysLastSampleTime": hh3cSysLastSampleTime}
)
