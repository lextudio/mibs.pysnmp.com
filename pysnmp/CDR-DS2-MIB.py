# SNMP MIB module (CDR-DS2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CDR-DS2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:53:55 2024
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
 NotificationType,
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
    "NotificationType",
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

cdrDS2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 7, 2)
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
_CdrDeviceServer_ObjectIdentity = ObjectIdentity
cdrDeviceServer = _CdrDeviceServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 7)
)
_CdrSystem_ObjectIdentity = ObjectIdentity
cdrSystem = _CdrSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 7, 2, 1)
)


class _CdrClient_Type(DisplayString):
    """Custom type cdrClient based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_CdrClient_Type.__name__ = "DisplayString"
_CdrClient_Object = MibScalar
cdrClient = _CdrClient_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 7, 2, 1, 1),
    _CdrClient_Type()
)
cdrClient.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cdrClient.setStatus("current")


class _CallState_Type(Integer32):
    """Custom type callState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CallState_Type.__name__ = "Integer32"
_CallState_Object = MibScalar
callState = _CallState_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 7, 2, 1, 2),
    _CallState_Type()
)
callState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    callState.setStatus("current")


class _FCAppID_Type(Integer32):
    """Custom type fCAppID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FCAppID_Type.__name__ = "Integer32"
_FCAppID_Object = MibScalar
fCAppID = _FCAppID_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 7, 2, 1, 3),
    _FCAppID_Type()
)
fCAppID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fCAppID.setStatus("current")


class _FCAppInstance_Type(Integer32):
    """Custom type fCAppInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FCAppInstance_Type.__name__ = "Integer32"
_FCAppInstance_Object = MibScalar
fCAppInstance = _FCAppInstance_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 7, 2, 1, 4),
    _FCAppInstance_Type()
)
fCAppInstance.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fCAppInstance.setStatus("current")


class _Severity_Type(Integer32):
    """Custom type severity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Severity_Type.__name__ = "Integer32"
_Severity_Object = MibScalar
severity = _Severity_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 7, 2, 1, 5),
    _Severity_Type()
)
severity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    severity.setStatus("current")


class _OriginationNumber_Type(DisplayString):
    """Custom type originationNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_OriginationNumber_Type.__name__ = "DisplayString"
_OriginationNumber_Object = MibScalar
originationNumber = _OriginationNumber_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 7, 2, 1, 6),
    _OriginationNumber_Type()
)
originationNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    originationNumber.setStatus("current")


class _DestinationNumber_Type(DisplayString):
    """Custom type destinationNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_DestinationNumber_Type.__name__ = "DisplayString"
_DestinationNumber_Object = MibScalar
destinationNumber = _DestinationNumber_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 7, 2, 1, 7),
    _DestinationNumber_Type()
)
destinationNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    destinationNumber.setStatus("current")


class _CallAnswerTime_Type(DisplayString):
    """Custom type callAnswerTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_CallAnswerTime_Type.__name__ = "DisplayString"
_CallAnswerTime_Object = MibScalar
callAnswerTime = _CallAnswerTime_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 7, 2, 1, 8),
    _CallAnswerTime_Type()
)
callAnswerTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    callAnswerTime.setStatus("current")


class _SwitchId_Type(DisplayString):
    """Custom type switchId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_SwitchId_Type.__name__ = "DisplayString"
_SwitchId_Object = MibScalar
switchId = _SwitchId_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 7, 2, 1, 9),
    _SwitchId_Type()
)
switchId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    switchId.setStatus("current")


class _CallId_Type(DisplayString):
    """Custom type callId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_CallId_Type.__name__ = "DisplayString"
_CallId_Object = MibScalar
callId = _CallId_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 7, 2, 1, 10),
    _CallId_Type()
)
callId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    callId.setStatus("current")


class _FullPercent_Type(Integer32):
    """Custom type fullPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FullPercent_Type.__name__ = "Integer32"
_FullPercent_Object = MibScalar
fullPercent = _FullPercent_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 7, 2, 1, 11),
    _FullPercent_Type()
)
fullPercent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fullPercent.setStatus("current")


class _FileSystem_Type(DisplayString):
    """Custom type fileSystem based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_FileSystem_Type.__name__ = "DisplayString"
_FileSystem_Object = MibScalar
fileSystem = _FileSystem_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 1198, 7, 2, 1, 12),
    _FileSystem_Type()
)
fileSystem.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fileSystem.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CDR-DS2-MIB",
    **{"lucent": lucent,
       "products": products,
       "softSwitch": softSwitch,
       "cdrDeviceServer": cdrDeviceServer,
       "cdrDS2": cdrDS2,
       "cdrSystem": cdrSystem,
       "cdrClient": cdrClient,
       "callState": callState,
       "fCAppID": fCAppID,
       "fCAppInstance": fCAppInstance,
       "severity": severity,
       "originationNumber": originationNumber,
       "destinationNumber": destinationNumber,
       "callAnswerTime": callAnswerTime,
       "switchId": switchId,
       "callId": callId,
       "fullPercent": fullPercent,
       "fileSystem": fileSystem}
)
