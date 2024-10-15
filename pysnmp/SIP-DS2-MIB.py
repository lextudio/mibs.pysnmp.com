# SNMP MIB module (SIP-DS2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SIP-DS2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:52:22 2024
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
 ObjectName,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso,
 snmpModules) = mibBuilder.importSymbols(
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
    "ObjectName",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso",
    "snmpModules")

(DisplayString,
 RowStatus,
 TextualConvention,
 TestAndIncr,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

sipDS2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 5, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Lucent_ObjectIdentity = ObjectIdentity
lucent = _Lucent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1)
)
_SoftSwitch_ObjectIdentity = ObjectIdentity
softSwitch = _SoftSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198)
)
_SipDeviceServer_ObjectIdentity = ObjectIdentity
sipDeviceServer = _SipDeviceServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 5)
)
_SipSystem_ObjectIdentity = ObjectIdentity
sipSystem = _SipSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 5, 2, 1)
)


class _DsInfo_Type(DisplayString):
    """Custom type dsInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_DsInfo_Type.__name__ = "DisplayString"
_DsInfo_Object = MibScalar
dsInfo = _DsInfo_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 5, 2, 1, 1),
    _DsInfo_Type()
)
dsInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsInfo.setStatus("current")


class _DsProtocolInfo_Type(DisplayString):
    """Custom type dsProtocolInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_DsProtocolInfo_Type.__name__ = "DisplayString"
_DsProtocolInfo_Object = MibScalar
dsProtocolInfo = _DsProtocolInfo_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 5, 2, 1, 2),
    _DsProtocolInfo_Type()
)
dsProtocolInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsProtocolInfo.setStatus("current")


class _LogLevel_Type(Integer32):
    """Custom type logLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_LogLevel_Type.__name__ = "Integer32"
_LogLevel_Object = MibScalar
logLevel = _LogLevel_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 5, 2, 1, 3),
    _LogLevel_Type()
)
logLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logLevel.setStatus("current")


class _SucceededCalls_Type(Integer32):
    """Custom type succeededCalls based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SucceededCalls_Type.__name__ = "Integer32"
_SucceededCalls_Object = MibScalar
succeededCalls = _SucceededCalls_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 5, 2, 1, 4),
    _SucceededCalls_Type()
)
succeededCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    succeededCalls.setStatus("current")


class _ActiveCalls_Type(Integer32):
    """Custom type activeCalls based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ActiveCalls_Type.__name__ = "Integer32"
_ActiveCalls_Object = MibScalar
activeCalls = _ActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 5, 2, 1, 5),
    _ActiveCalls_Type()
)
activeCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeCalls.setStatus("current")


class _FailedCalls_Type(Integer32):
    """Custom type failedCalls based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FailedCalls_Type.__name__ = "Integer32"
_FailedCalls_Object = MibScalar
failedCalls = _FailedCalls_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 5, 2, 1, 6),
    _FailedCalls_Type()
)
failedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    failedCalls.setStatus("current")


class _ReloadConfig_Type(Integer32):
    """Custom type reloadConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ReloadConfig_Type.__name__ = "Integer32"
_ReloadConfig_Object = MibScalar
reloadConfig = _ReloadConfig_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 5, 2, 1, 7),
    _ReloadConfig_Type()
)
reloadConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reloadConfig.setStatus("current")


class _ResetLog_Type(Integer32):
    """Custom type resetLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ResetLog_Type.__name__ = "Integer32"
_ResetLog_Object = MibScalar
resetLog = _ResetLog_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 5, 2, 1, 8),
    _ResetLog_Type()
)
resetLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetLog.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SIP-DS2-MIB",
    **{"lucent": lucent,
       "products": products,
       "softSwitch": softSwitch,
       "sipDeviceServer": sipDeviceServer,
       "sipDS2": sipDS2,
       "sipSystem": sipSystem,
       "dsInfo": dsInfo,
       "dsProtocolInfo": dsProtocolInfo,
       "logLevel": logLevel,
       "succeededCalls": succeededCalls,
       "activeCalls": activeCalls,
       "failedCalls": failedCalls,
       "reloadConfig": reloadConfig,
       "resetLog": resetLog}
)
