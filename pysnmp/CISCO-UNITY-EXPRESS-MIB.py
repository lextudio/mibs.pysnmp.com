# SNMP MIB module (CISCO-UNITY-EXPRESS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNITY-EXPRESS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:11:33 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoUnityExpressMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 420)
)
ciscoUnityExpressMIB.setRevisions(
        ("2007-01-08 00:00",
         "2005-09-02 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoUnityExpressMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoUnityExpressMIBNotifs = _CiscoUnityExpressMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 0)
)
_CiscoUnityExpressMIBObjects_ObjectIdentity = ObjectIdentity
ciscoUnityExpressMIBObjects = _CiscoUnityExpressMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1)
)
_CueSystem_ObjectIdentity = ObjectIdentity
cueSystem = _CueSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 1)
)
_CueSystemControl_ObjectIdentity = ObjectIdentity
cueSystemControl = _CueSystemControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 1, 1)
)
_CueShutdownRequest_Type = TruthValue
_CueShutdownRequest_Object = MibScalar
cueShutdownRequest = _CueShutdownRequest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 1, 1, 1),
    _CueShutdownRequest_Type()
)
cueShutdownRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cueShutdownRequest.setStatus("current")
_CueSystemScalars_ObjectIdentity = ObjectIdentity
cueSystemScalars = _CueSystemScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 1, 2)
)


class _CueAVTNumber_Type(SnmpAdminString):
    """Custom type cueAVTNumber based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_CueAVTNumber_Type.__name__ = "SnmpAdminString"
_CueAVTNumber_Object = MibScalar
cueAVTNumber = _CueAVTNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 1, 2, 1),
    _CueAVTNumber_Type()
)
cueAVTNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueAVTNumber.setStatus("current")


class _CueVoicemailNumber_Type(SnmpAdminString):
    """Custom type cueVoicemailNumber based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_CueVoicemailNumber_Type.__name__ = "SnmpAdminString"
_CueVoicemailNumber_Object = MibScalar
cueVoicemailNumber = _CueVoicemailNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 1, 2, 2),
    _CueVoicemailNumber_Type()
)
cueVoicemailNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueVoicemailNumber.setStatus("current")


class _CueAANumber_Type(SnmpAdminString):
    """Custom type cueAANumber based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_CueAANumber_Type.__name__ = "SnmpAdminString"
_CueAANumber_Object = MibScalar
cueAANumber = _CueAANumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 1, 2, 3),
    _CueAANumber_Type()
)
cueAANumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueAANumber.setStatus("current")


class _CueHardwareModuleType_Type(Integer32):
    """Custom type cueHardwareModuleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aim", 1),
          ("nm", 2),
          ("other", 3))
    )


_CueHardwareModuleType_Type.__name__ = "Integer32"
_CueHardwareModuleType_Object = MibScalar
cueHardwareModuleType = _CueHardwareModuleType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 1, 2, 4),
    _CueHardwareModuleType_Type()
)
cueHardwareModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueHardwareModuleType.setStatus("deprecated")


class _CueCallControlAgentType_Type(Integer32):
    """Custom type cueCallControlAgentType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ccm", 1),
          ("ccme", 2))
    )


_CueCallControlAgentType_Type.__name__ = "Integer32"
_CueCallControlAgentType_Object = MibScalar
cueCallControlAgentType = _CueCallControlAgentType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 1, 2, 5),
    _CueCallControlAgentType_Type()
)
cueCallControlAgentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueCallControlAgentType.setStatus("current")
_CueSIPInfo_ObjectIdentity = ObjectIdentity
cueSIPInfo = _CueSIPInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 1, 3)
)


class _CueSIPGatewayName_Type(SnmpAdminString):
    """Custom type cueSIPGatewayName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CueSIPGatewayName_Type.__name__ = "SnmpAdminString"
_CueSIPGatewayName_Object = MibScalar
cueSIPGatewayName = _CueSIPGatewayName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 1, 3, 1),
    _CueSIPGatewayName_Type()
)
cueSIPGatewayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueSIPGatewayName.setStatus("current")
_CueSIPGatewayIPType_Type = InetAddressType
_CueSIPGatewayIPType_Object = MibScalar
cueSIPGatewayIPType = _CueSIPGatewayIPType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 1, 3, 2),
    _CueSIPGatewayIPType_Type()
)
cueSIPGatewayIPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueSIPGatewayIPType.setStatus("current")
_CueSIPGatewayIP_Type = InetAddress
_CueSIPGatewayIP_Object = MibScalar
cueSIPGatewayIP = _CueSIPGatewayIP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 1, 3, 3),
    _CueSIPGatewayIP_Type()
)
cueSIPGatewayIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueSIPGatewayIP.setStatus("current")
_CueSIPPort_Type = InetPortNumber
_CueSIPPort_Object = MibScalar
cueSIPPort = _CueSIPPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 1, 3, 4),
    _CueSIPPort_Type()
)
cueSIPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueSIPPort.setStatus("current")
_CueJTAPIInfo_ObjectIdentity = ObjectIdentity
cueJTAPIInfo = _CueJTAPIInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 1, 4)
)
_CueJTAPIServerTable_Object = MibTable
cueJTAPIServerTable = _CueJTAPIServerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cueJTAPIServerTable.setStatus("current")
_CueJTAPIServerEntry_Object = MibTableRow
cueJTAPIServerEntry = _CueJTAPIServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 1, 4, 1, 1)
)
cueJTAPIServerEntry.setIndexNames(
    (0, "CISCO-UNITY-EXPRESS-MIB", "cueJTAPIServerIndex"),
)
if mibBuilder.loadTexts:
    cueJTAPIServerEntry.setStatus("current")


class _CueJTAPIServerIndex_Type(Unsigned32):
    """Custom type cueJTAPIServerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CueJTAPIServerIndex_Type.__name__ = "Unsigned32"
_CueJTAPIServerIndex_Object = MibTableColumn
cueJTAPIServerIndex = _CueJTAPIServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 1, 4, 1, 1, 1),
    _CueJTAPIServerIndex_Type()
)
cueJTAPIServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cueJTAPIServerIndex.setStatus("current")


class _CueJTAPIServerName_Type(SnmpAdminString):
    """Custom type cueJTAPIServerName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CueJTAPIServerName_Type.__name__ = "SnmpAdminString"
_CueJTAPIServerName_Object = MibTableColumn
cueJTAPIServerName = _CueJTAPIServerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 1, 4, 1, 1, 2),
    _CueJTAPIServerName_Type()
)
cueJTAPIServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueJTAPIServerName.setStatus("current")
_CueJTAPIServerIPType_Type = InetAddressType
_CueJTAPIServerIPType_Object = MibTableColumn
cueJTAPIServerIPType = _CueJTAPIServerIPType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 1, 4, 1, 1, 3),
    _CueJTAPIServerIPType_Type()
)
cueJTAPIServerIPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueJTAPIServerIPType.setStatus("current")
_CueJTAPIServerIP_Type = InetAddress
_CueJTAPIServerIP_Object = MibTableColumn
cueJTAPIServerIP = _CueJTAPIServerIP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 1, 4, 1, 1, 4),
    _CueJTAPIServerIP_Type()
)
cueJTAPIServerIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueJTAPIServerIP.setStatus("current")


class _CueJTAPISubsystemState_Type(Integer32):
    """Custom type cueJTAPISubsystemState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("inService", 3),
          ("initializing", 2),
          ("outOfService", 4),
          ("partialService", 7),
          ("shutDown", 6),
          ("shuttingDown", 5),
          ("unknown", 1))
    )


_CueJTAPISubsystemState_Type.__name__ = "Integer32"
_CueJTAPISubsystemState_Object = MibScalar
cueJTAPISubsystemState = _CueJTAPISubsystemState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 1, 4, 2),
    _CueJTAPISubsystemState_Type()
)
cueJTAPISubsystemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueJTAPISubsystemState.setStatus("current")


class _CueJTAPIUsername_Type(SnmpAdminString):
    """Custom type cueJTAPIUsername based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_CueJTAPIUsername_Type.__name__ = "SnmpAdminString"
_CueJTAPIUsername_Object = MibScalar
cueJTAPIUsername = _CueJTAPIUsername_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 1, 4, 3),
    _CueJTAPIUsername_Type()
)
cueJTAPIUsername.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueJTAPIUsername.setStatus("current")


class _CueJTAPISoftwareVersion_Type(SnmpAdminString):
    """Custom type cueJTAPISoftwareVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_CueJTAPISoftwareVersion_Type.__name__ = "SnmpAdminString"
_CueJTAPISoftwareVersion_Object = MibScalar
cueJTAPISoftwareVersion = _CueJTAPISoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 1, 4, 4),
    _CueJTAPISoftwareVersion_Type()
)
cueJTAPISoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueJTAPISoftwareVersion.setStatus("current")


class _CueJTAPIPortsRegistered_Type(Gauge32):
    """Custom type cueJTAPIPortsRegistered based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_CueJTAPIPortsRegistered_Type.__name__ = "Gauge32"
_CueJTAPIPortsRegistered_Object = MibScalar
cueJTAPIPortsRegistered = _CueJTAPIPortsRegistered_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 1, 4, 5),
    _CueJTAPIPortsRegistered_Type()
)
cueJTAPIPortsRegistered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueJTAPIPortsRegistered.setStatus("current")
_CueSystemDefaults_ObjectIdentity = ObjectIdentity
cueSystemDefaults = _CueSystemDefaults_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 1, 5)
)


class _CueDefaultMailboxSize_Type(Unsigned32):
    """Custom type cueDefaultMailboxSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CueDefaultMailboxSize_Type.__name__ = "Unsigned32"
_CueDefaultMailboxSize_Object = MibScalar
cueDefaultMailboxSize = _CueDefaultMailboxSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 1, 5, 1),
    _CueDefaultMailboxSize_Type()
)
cueDefaultMailboxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueDefaultMailboxSize.setStatus("current")
if mibBuilder.loadTexts:
    cueDefaultMailboxSize.setUnits("seconds")


class _CueDefaultGreetingSize_Type(Unsigned32):
    """Custom type cueDefaultGreetingSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CueDefaultGreetingSize_Type.__name__ = "Unsigned32"
_CueDefaultGreetingSize_Object = MibScalar
cueDefaultGreetingSize = _CueDefaultGreetingSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 1, 5, 2),
    _CueDefaultGreetingSize_Type()
)
cueDefaultGreetingSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueDefaultGreetingSize.setStatus("current")
if mibBuilder.loadTexts:
    cueDefaultGreetingSize.setUnits("seconds")


class _CueDefaultMessageSizeMax_Type(Unsigned32):
    """Custom type cueDefaultMessageSizeMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CueDefaultMessageSizeMax_Type.__name__ = "Unsigned32"
_CueDefaultMessageSizeMax_Object = MibScalar
cueDefaultMessageSizeMax = _CueDefaultMessageSizeMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 1, 5, 3),
    _CueDefaultMessageSizeMax_Type()
)
cueDefaultMessageSizeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueDefaultMessageSizeMax.setStatus("current")
if mibBuilder.loadTexts:
    cueDefaultMessageSizeMax.setUnits("seconds")


class _CueDefaultMessageExpiryTime_Type(Unsigned32):
    """Custom type cueDefaultMessageExpiryTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CueDefaultMessageExpiryTime_Type.__name__ = "Unsigned32"
_CueDefaultMessageExpiryTime_Object = MibScalar
cueDefaultMessageExpiryTime = _CueDefaultMessageExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 1, 5, 4),
    _CueDefaultMessageExpiryTime_Type()
)
cueDefaultMessageExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueDefaultMessageExpiryTime.setStatus("current")
if mibBuilder.loadTexts:
    cueDefaultMessageExpiryTime.setUnits("days")
_CueUsage_ObjectIdentity = ObjectIdentity
cueUsage = _CueUsage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2)
)
_CueUsageScalars_ObjectIdentity = ObjectIdentity
cueUsageScalars = _CueUsageScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 1)
)


class _CueLicensedPortsMax_Type(Unsigned32):
    """Custom type cueLicensedPortsMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_CueLicensedPortsMax_Type.__name__ = "Unsigned32"
_CueLicensedPortsMax_Object = MibScalar
cueLicensedPortsMax = _CueLicensedPortsMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 1, 1),
    _CueLicensedPortsMax_Type()
)
cueLicensedPortsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueLicensedPortsMax.setStatus("current")


class _CueActiveCalls_Type(Gauge32):
    """Custom type cueActiveCalls based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_CueActiveCalls_Type.__name__ = "Gauge32"
_CueActiveCalls_Object = MibScalar
cueActiveCalls = _CueActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 1, 2),
    _CueActiveCalls_Type()
)
cueActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueActiveCalls.setStatus("current")


class _CuePersonalMailboxes_Type(Gauge32):
    """Custom type cuePersonalMailboxes based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CuePersonalMailboxes_Type.__name__ = "Gauge32"
_CuePersonalMailboxes_Object = MibScalar
cuePersonalMailboxes = _CuePersonalMailboxes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 1, 3),
    _CuePersonalMailboxes_Type()
)
cuePersonalMailboxes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuePersonalMailboxes.setStatus("current")


class _CueGeneralDeliveryMailboxes_Type(Gauge32):
    """Custom type cueGeneralDeliveryMailboxes based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CueGeneralDeliveryMailboxes_Type.__name__ = "Gauge32"
_CueGeneralDeliveryMailboxes_Object = MibScalar
cueGeneralDeliveryMailboxes = _CueGeneralDeliveryMailboxes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 1, 4),
    _CueGeneralDeliveryMailboxes_Type()
)
cueGeneralDeliveryMailboxes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueGeneralDeliveryMailboxes.setStatus("current")


class _CueOrphanedMailboxes_Type(Gauge32):
    """Custom type cueOrphanedMailboxes based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CueOrphanedMailboxes_Type.__name__ = "Gauge32"
_CueOrphanedMailboxes_Object = MibScalar
cueOrphanedMailboxes = _CueOrphanedMailboxes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 1, 5),
    _CueOrphanedMailboxes_Type()
)
cueOrphanedMailboxes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueOrphanedMailboxes.setStatus("current")


class _CueCapacityOfVoicemail_Type(Unsigned32):
    """Custom type cueCapacityOfVoicemail based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CueCapacityOfVoicemail_Type.__name__ = "Unsigned32"
_CueCapacityOfVoicemail_Object = MibScalar
cueCapacityOfVoicemail = _CueCapacityOfVoicemail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 1, 6),
    _CueCapacityOfVoicemail_Type()
)
cueCapacityOfVoicemail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueCapacityOfVoicemail.setStatus("current")
if mibBuilder.loadTexts:
    cueCapacityOfVoicemail.setUnits("minutes")


class _CueAllocatedCapacity_Type(Unsigned32):
    """Custom type cueAllocatedCapacity based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CueAllocatedCapacity_Type.__name__ = "Unsigned32"
_CueAllocatedCapacity_Object = MibScalar
cueAllocatedCapacity = _CueAllocatedCapacity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 1, 7),
    _CueAllocatedCapacity_Type()
)
cueAllocatedCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueAllocatedCapacity.setStatus("current")
if mibBuilder.loadTexts:
    cueAllocatedCapacity.setUnits("minutes")


class _CueTotalTimeUsed_Type(Gauge32):
    """Custom type cueTotalTimeUsed based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CueTotalTimeUsed_Type.__name__ = "Gauge32"
_CueTotalTimeUsed_Object = MibScalar
cueTotalTimeUsed = _CueTotalTimeUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 1, 8),
    _CueTotalTimeUsed_Type()
)
cueTotalTimeUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueTotalTimeUsed.setStatus("current")
if mibBuilder.loadTexts:
    cueTotalTimeUsed.setUnits("minutes")


class _CuePercentTimeUsed_Type(Gauge32):
    """Custom type cuePercentTimeUsed based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CuePercentTimeUsed_Type.__name__ = "Gauge32"
_CuePercentTimeUsed_Object = MibScalar
cuePercentTimeUsed = _CuePercentTimeUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 1, 9),
    _CuePercentTimeUsed_Type()
)
cuePercentTimeUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuePercentTimeUsed.setStatus("current")
if mibBuilder.loadTexts:
    cuePercentTimeUsed.setUnits("percent")


class _CueMessageTimeUsed_Type(Gauge32):
    """Custom type cueMessageTimeUsed based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CueMessageTimeUsed_Type.__name__ = "Gauge32"
_CueMessageTimeUsed_Object = MibScalar
cueMessageTimeUsed = _CueMessageTimeUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 1, 10),
    _CueMessageTimeUsed_Type()
)
cueMessageTimeUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueMessageTimeUsed.setStatus("current")
if mibBuilder.loadTexts:
    cueMessageTimeUsed.setUnits("seconds")


class _CueMessageCount_Type(Gauge32):
    """Custom type cueMessageCount based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CueMessageCount_Type.__name__ = "Gauge32"
_CueMessageCount_Object = MibScalar
cueMessageCount = _CueMessageCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 1, 11),
    _CueMessageCount_Type()
)
cueMessageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueMessageCount.setStatus("current")


class _CueAverageMessageLength_Type(Gauge32):
    """Custom type cueAverageMessageLength based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CueAverageMessageLength_Type.__name__ = "Gauge32"
_CueAverageMessageLength_Object = MibScalar
cueAverageMessageLength = _CueAverageMessageLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 1, 12),
    _CueAverageMessageLength_Type()
)
cueAverageMessageLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueAverageMessageLength.setStatus("current")
if mibBuilder.loadTexts:
    cueAverageMessageLength.setUnits("seconds")


class _CueGreetingTimeUsed_Type(Gauge32):
    """Custom type cueGreetingTimeUsed based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CueGreetingTimeUsed_Type.__name__ = "Gauge32"
_CueGreetingTimeUsed_Object = MibScalar
cueGreetingTimeUsed = _CueGreetingTimeUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 1, 13),
    _CueGreetingTimeUsed_Type()
)
cueGreetingTimeUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueGreetingTimeUsed.setStatus("current")
if mibBuilder.loadTexts:
    cueGreetingTimeUsed.setUnits("seconds")


class _CueGreetingCount_Type(Gauge32):
    """Custom type cueGreetingCount based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CueGreetingCount_Type.__name__ = "Gauge32"
_CueGreetingCount_Object = MibScalar
cueGreetingCount = _CueGreetingCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 1, 14),
    _CueGreetingCount_Type()
)
cueGreetingCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueGreetingCount.setStatus("current")


class _CueAverageGreetingLength_Type(Gauge32):
    """Custom type cueAverageGreetingLength based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CueAverageGreetingLength_Type.__name__ = "Gauge32"
_CueAverageGreetingLength_Object = MibScalar
cueAverageGreetingLength = _CueAverageGreetingLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 1, 15),
    _CueAverageGreetingLength_Type()
)
cueAverageGreetingLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueAverageGreetingLength.setStatus("current")
if mibBuilder.loadTexts:
    cueAverageGreetingLength.setUnits("seconds")
_CueMessagesLeft_Type = Counter32
_CueMessagesLeft_Object = MibScalar
cueMessagesLeft = _CueMessagesLeft_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 1, 16),
    _CueMessagesLeft_Type()
)
cueMessagesLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueMessagesLeft.setStatus("current")
_CueMessagesRetrieved_Type = Counter32
_CueMessagesRetrieved_Object = MibScalar
cueMessagesRetrieved = _CueMessagesRetrieved_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 1, 17),
    _CueMessagesRetrieved_Type()
)
cueMessagesRetrieved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueMessagesRetrieved.setStatus("current")
_CueMessagesDeleted_Type = Counter32
_CueMessagesDeleted_Object = MibScalar
cueMessagesDeleted = _CueMessagesDeleted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 1, 18),
    _CueMessagesDeleted_Type()
)
cueMessagesDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueMessagesDeleted.setStatus("current")


class _CueLicensedMailboxesMax_Type(Unsigned32):
    """Custom type cueLicensedMailboxesMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CueLicensedMailboxesMax_Type.__name__ = "Unsigned32"
_CueLicensedMailboxesMax_Object = MibScalar
cueLicensedMailboxesMax = _CueLicensedMailboxesMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 1, 19),
    _CueLicensedMailboxesMax_Type()
)
cueLicensedMailboxesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueLicensedMailboxesMax.setStatus("current")


class _CueMailboxesAbove90PercentFull_Type(Unsigned32):
    """Custom type cueMailboxesAbove90PercentFull based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CueMailboxesAbove90PercentFull_Type.__name__ = "Unsigned32"
_CueMailboxesAbove90PercentFull_Object = MibScalar
cueMailboxesAbove90PercentFull = _CueMailboxesAbove90PercentFull_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 1, 20),
    _CueMailboxesAbove90PercentFull_Type()
)
cueMailboxesAbove90PercentFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueMailboxesAbove90PercentFull.setStatus("current")
_CueMboxTable_Object = MibTable
cueMboxTable = _CueMboxTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cueMboxTable.setStatus("current")
_CueMboxEntry_Object = MibTableRow
cueMboxEntry = _CueMboxEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 2, 1)
)
cueMboxEntry.setIndexNames(
    (0, "CISCO-UNITY-EXPRESS-MIB", "cueMboxIndex"),
)
if mibBuilder.loadTexts:
    cueMboxEntry.setStatus("current")


class _CueMboxIndex_Type(Unsigned32):
    """Custom type cueMboxIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CueMboxIndex_Type.__name__ = "Unsigned32"
_CueMboxIndex_Object = MibTableColumn
cueMboxIndex = _CueMboxIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 2, 1, 1),
    _CueMboxIndex_Type()
)
cueMboxIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cueMboxIndex.setStatus("current")


class _CueMboxOwner_Type(SnmpAdminString):
    """Custom type cueMboxOwner based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_CueMboxOwner_Type.__name__ = "SnmpAdminString"
_CueMboxOwner_Object = MibTableColumn
cueMboxOwner = _CueMboxOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 2, 1, 2),
    _CueMboxOwner_Type()
)
cueMboxOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueMboxOwner.setStatus("current")


class _CueMboxPrimaryExtension_Type(SnmpAdminString):
    """Custom type cueMboxPrimaryExtension based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_CueMboxPrimaryExtension_Type.__name__ = "SnmpAdminString"
_CueMboxPrimaryExtension_Object = MibTableColumn
cueMboxPrimaryExtension = _CueMboxPrimaryExtension_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 2, 1, 3),
    _CueMboxPrimaryExtension_Type()
)
cueMboxPrimaryExtension.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueMboxPrimaryExtension.setStatus("current")


class _CueMboxType_Type(Integer32):
    """Custom type cueMboxType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("generalDelivery", 2),
          ("personal", 1))
    )


_CueMboxType_Type.__name__ = "Integer32"
_CueMboxType_Object = MibTableColumn
cueMboxType = _CueMboxType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 2, 1, 4),
    _CueMboxType_Type()
)
cueMboxType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueMboxType.setStatus("current")
_CueMboxDescription_Type = SnmpAdminString
_CueMboxDescription_Object = MibTableColumn
cueMboxDescription = _CueMboxDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 2, 1, 5),
    _CueMboxDescription_Type()
)
cueMboxDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueMboxDescription.setStatus("current")


class _CueMboxSize_Type(Gauge32):
    """Custom type cueMboxSize based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CueMboxSize_Type.__name__ = "Gauge32"
_CueMboxSize_Object = MibTableColumn
cueMboxSize = _CueMboxSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 2, 1, 6),
    _CueMboxSize_Type()
)
cueMboxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueMboxSize.setStatus("current")
if mibBuilder.loadTexts:
    cueMboxSize.setUnits("seconds")


class _CueMboxTimeUsed_Type(Gauge32):
    """Custom type cueMboxTimeUsed based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CueMboxTimeUsed_Type.__name__ = "Gauge32"
_CueMboxTimeUsed_Object = MibTableColumn
cueMboxTimeUsed = _CueMboxTimeUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 2, 1, 7),
    _CueMboxTimeUsed_Type()
)
cueMboxTimeUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueMboxTimeUsed.setStatus("current")
if mibBuilder.loadTexts:
    cueMboxTimeUsed.setUnits("seconds")


class _CueMboxPercentTimeUsed_Type(Gauge32):
    """Custom type cueMboxPercentTimeUsed based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CueMboxPercentTimeUsed_Type.__name__ = "Gauge32"
_CueMboxPercentTimeUsed_Object = MibTableColumn
cueMboxPercentTimeUsed = _CueMboxPercentTimeUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 2, 1, 8),
    _CueMboxPercentTimeUsed_Type()
)
cueMboxPercentTimeUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueMboxPercentTimeUsed.setStatus("current")
if mibBuilder.loadTexts:
    cueMboxPercentTimeUsed.setUnits("percent")


class _CueMboxNumberOfMessages_Type(Gauge32):
    """Custom type cueMboxNumberOfMessages based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CueMboxNumberOfMessages_Type.__name__ = "Gauge32"
_CueMboxNumberOfMessages_Object = MibTableColumn
cueMboxNumberOfMessages = _CueMboxNumberOfMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 2, 1, 9),
    _CueMboxNumberOfMessages_Type()
)
cueMboxNumberOfMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueMboxNumberOfMessages.setStatus("current")


class _CueMboxNumberOfNewMessages_Type(Gauge32):
    """Custom type cueMboxNumberOfNewMessages based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CueMboxNumberOfNewMessages_Type.__name__ = "Gauge32"
_CueMboxNumberOfNewMessages_Object = MibTableColumn
cueMboxNumberOfNewMessages = _CueMboxNumberOfNewMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 2, 1, 10),
    _CueMboxNumberOfNewMessages_Type()
)
cueMboxNumberOfNewMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueMboxNumberOfNewMessages.setStatus("current")


class _CueMboxNumberOfSavedMessages_Type(Gauge32):
    """Custom type cueMboxNumberOfSavedMessages based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CueMboxNumberOfSavedMessages_Type.__name__ = "Gauge32"
_CueMboxNumberOfSavedMessages_Object = MibTableColumn
cueMboxNumberOfSavedMessages = _CueMboxNumberOfSavedMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 2, 1, 11),
    _CueMboxNumberOfSavedMessages_Type()
)
cueMboxNumberOfSavedMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueMboxNumberOfSavedMessages.setStatus("current")


class _CueMboxMessageSizeMax_Type(Unsigned32):
    """Custom type cueMboxMessageSizeMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CueMboxMessageSizeMax_Type.__name__ = "Unsigned32"
_CueMboxMessageSizeMax_Object = MibTableColumn
cueMboxMessageSizeMax = _CueMboxMessageSizeMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 2, 1, 12),
    _CueMboxMessageSizeMax_Type()
)
cueMboxMessageSizeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueMboxMessageSizeMax.setStatus("current")
if mibBuilder.loadTexts:
    cueMboxMessageSizeMax.setUnits("seconds")


class _CueMboxMessageExpiryTime_Type(Unsigned32):
    """Custom type cueMboxMessageExpiryTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CueMboxMessageExpiryTime_Type.__name__ = "Unsigned32"
_CueMboxMessageExpiryTime_Object = MibTableColumn
cueMboxMessageExpiryTime = _CueMboxMessageExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 2, 1, 13),
    _CueMboxMessageExpiryTime_Type()
)
cueMboxMessageExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueMboxMessageExpiryTime.setStatus("current")
if mibBuilder.loadTexts:
    cueMboxMessageExpiryTime.setUnits("days")
_CueMboxPlayTutorial_Type = TruthValue
_CueMboxPlayTutorial_Object = MibTableColumn
cueMboxPlayTutorial = _CueMboxPlayTutorial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 2, 1, 14),
    _CueMboxPlayTutorial_Type()
)
cueMboxPlayTutorial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueMboxPlayTutorial.setStatus("current")


class _CueMboxGreetingType_Type(Integer32):
    """Custom type cueMboxGreetingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alternate", 2),
          ("standard", 1))
    )


_CueMboxGreetingType_Type.__name__ = "Integer32"
_CueMboxGreetingType_Object = MibTableColumn
cueMboxGreetingType = _CueMboxGreetingType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 2, 1, 15),
    _CueMboxGreetingType_Type()
)
cueMboxGreetingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueMboxGreetingType.setStatus("current")
_CueMboxEnabled_Type = TruthValue
_CueMboxEnabled_Object = MibTableColumn
cueMboxEnabled = _CueMboxEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 2, 1, 16),
    _CueMboxEnabled_Type()
)
cueMboxEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueMboxEnabled.setStatus("current")
_CueMboxBusy_Type = TruthValue
_CueMboxBusy_Object = MibTableColumn
cueMboxBusy = _CueMboxBusy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 2, 1, 17),
    _CueMboxBusy_Type()
)
cueMboxBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueMboxBusy.setStatus("current")
_CueMboxMWIState_Type = TruthValue
_CueMboxMWIState_Object = MibTableColumn
cueMboxMWIState = _CueMboxMWIState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 2, 2, 1, 18),
    _CueMboxMWIState_Type()
)
cueMboxMWIState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueMboxMWIState.setStatus("current")
_CueSecurity_ObjectIdentity = ObjectIdentity
cueSecurity = _CueSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 3)
)
_CueLoginInfo_ObjectIdentity = ObjectIdentity
cueLoginInfo = _CueLoginInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 3, 1)
)
_CueLoginAttempts_Type = Counter32
_CueLoginAttempts_Object = MibScalar
cueLoginAttempts = _CueLoginAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 3, 1, 1),
    _CueLoginAttempts_Type()
)
cueLoginAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueLoginAttempts.setStatus("current")
_CueLoginUsernameFailures_Type = Counter32
_CueLoginUsernameFailures_Object = MibScalar
cueLoginUsernameFailures = _CueLoginUsernameFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 3, 1, 2),
    _CueLoginUsernameFailures_Type()
)
cueLoginUsernameFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueLoginUsernameFailures.setStatus("current")
_CueLoginPasswordFailures_Type = Counter32
_CueLoginPasswordFailures_Object = MibScalar
cueLoginPasswordFailures = _CueLoginPasswordFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 3, 1, 3),
    _CueLoginPasswordFailures_Type()
)
cueLoginPasswordFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueLoginPasswordFailures.setStatus("current")
_CuePINInfo_ObjectIdentity = ObjectIdentity
cuePINInfo = _CuePINInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 3, 2)
)
_CuePINAttempts_Type = Counter32
_CuePINAttempts_Object = MibScalar
cuePINAttempts = _CuePINAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 3, 2, 1),
    _CuePINAttempts_Type()
)
cuePINAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuePINAttempts.setStatus("current")
_CuePINResets_Type = Counter32
_CuePINResets_Object = MibScalar
cuePINResets = _CuePINResets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 3, 2, 2),
    _CuePINResets_Type()
)
cuePINResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuePINResets.setStatus("current")
_CuePINUidFailures_Type = Counter32
_CuePINUidFailures_Object = MibScalar
cuePINUidFailures = _CuePINUidFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 3, 2, 3),
    _CuePINUidFailures_Type()
)
cuePINUidFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuePINUidFailures.setStatus("current")
_CuePINPasswordFailures_Type = Counter32
_CuePINPasswordFailures_Object = MibScalar
cuePINPasswordFailures = _CuePINPasswordFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 3, 2, 4),
    _CuePINPasswordFailures_Type()
)
cuePINPasswordFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuePINPasswordFailures.setStatus("current")
_CueNotif_ObjectIdentity = ObjectIdentity
cueNotif = _CueNotif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 4)
)
_CueNotifConfig_ObjectIdentity = ObjectIdentity
cueNotifConfig = _CueNotifConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 4, 1)
)


class _CueNotifEnable_Type(TruthValue):
    """Custom type cueNotifEnable based on TruthValue"""


_CueNotifEnable_Object = MibScalar
cueNotifEnable = _CueNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 4, 1, 1),
    _CueNotifEnable_Type()
)
cueNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cueNotifEnable.setStatus("current")
_CueNotifInfo_ObjectIdentity = ObjectIdentity
cueNotifInfo = _CueNotifInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 4, 2)
)


class _CueNotifSeverity_Type(Integer32):
    """Custom type cueNotifSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("error", 1),
          ("informational", 3),
          ("warning", 2))
    )


_CueNotifSeverity_Type.__name__ = "Integer32"
_CueNotifSeverity_Object = MibScalar
cueNotifSeverity = _CueNotifSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 4, 2, 1),
    _CueNotifSeverity_Type()
)
cueNotifSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cueNotifSeverity.setStatus("current")
_CueNotifDate_Type = DateAndTime
_CueNotifDate_Object = MibScalar
cueNotifDate = _CueNotifDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 4, 2, 2),
    _CueNotifDate_Type()
)
cueNotifDate.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cueNotifDate.setStatus("current")
_CueNotifDescription_Type = SnmpAdminString
_CueNotifDescription_Object = MibScalar
cueNotifDescription = _CueNotifDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 4, 2, 3),
    _CueNotifDescription_Type()
)
cueNotifDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cueNotifDescription.setStatus("current")
_CueNotifDetail_Type = SnmpAdminString
_CueNotifDetail_Object = MibScalar
cueNotifDetail = _CueNotifDetail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 4, 2, 4),
    _CueNotifDetail_Type()
)
cueNotifDetail.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cueNotifDetail.setStatus("current")
_CueNotifSecurity_ObjectIdentity = ObjectIdentity
cueNotifSecurity = _CueNotifSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 4, 3)
)


class _CueLoginUsernameThresh_Type(Unsigned32):
    """Custom type cueLoginUsernameThresh based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CueLoginUsernameThresh_Type.__name__ = "Unsigned32"
_CueLoginUsernameThresh_Object = MibScalar
cueLoginUsernameThresh = _CueLoginUsernameThresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 4, 3, 1),
    _CueLoginUsernameThresh_Type()
)
cueLoginUsernameThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueLoginUsernameThresh.setStatus("current")


class _CueLoginPasswordThresh_Type(Unsigned32):
    """Custom type cueLoginPasswordThresh based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CueLoginPasswordThresh_Type.__name__ = "Unsigned32"
_CueLoginPasswordThresh_Object = MibScalar
cueLoginPasswordThresh = _CueLoginPasswordThresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 4, 3, 2),
    _CueLoginPasswordThresh_Type()
)
cueLoginPasswordThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueLoginPasswordThresh.setStatus("current")


class _CuePINUidThresh_Type(Unsigned32):
    """Custom type cuePINUidThresh based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CuePINUidThresh_Type.__name__ = "Unsigned32"
_CuePINUidThresh_Object = MibScalar
cuePINUidThresh = _CuePINUidThresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 4, 3, 3),
    _CuePINUidThresh_Type()
)
cuePINUidThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuePINUidThresh.setStatus("current")


class _CuePINPasswordThresh_Type(Unsigned32):
    """Custom type cuePINPasswordThresh based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CuePINPasswordThresh_Type.__name__ = "Unsigned32"
_CuePINPasswordThresh_Object = MibScalar
cuePINPasswordThresh = _CuePINPasswordThresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 4, 3, 4),
    _CuePINPasswordThresh_Type()
)
cuePINPasswordThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuePINPasswordThresh.setStatus("current")


class _CuePINResetThresh_Type(Unsigned32):
    """Custom type cuePINResetThresh based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CuePINResetThresh_Type.__name__ = "Unsigned32"
_CuePINResetThresh_Object = MibScalar
cuePINResetThresh = _CuePINResetThresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 4, 3, 5),
    _CuePINResetThresh_Type()
)
cuePINResetThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuePINResetThresh.setStatus("current")
_CueBackupRestore_ObjectIdentity = ObjectIdentity
cueBackupRestore = _CueBackupRestore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 5)
)
_CueBRHistoryTable_Object = MibTable
cueBRHistoryTable = _CueBRHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cueBRHistoryTable.setStatus("current")
_CueBRHistoryEntry_Object = MibTableRow
cueBRHistoryEntry = _CueBRHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 5, 1, 1)
)
cueBRHistoryEntry.setIndexNames(
    (0, "CISCO-UNITY-EXPRESS-MIB", "cueBRHistoryIndex"),
)
if mibBuilder.loadTexts:
    cueBRHistoryEntry.setStatus("current")


class _CueBRHistoryIndex_Type(Unsigned32):
    """Custom type cueBRHistoryIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CueBRHistoryIndex_Type.__name__ = "Unsigned32"
_CueBRHistoryIndex_Object = MibTableColumn
cueBRHistoryIndex = _CueBRHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 5, 1, 1, 1),
    _CueBRHistoryIndex_Type()
)
cueBRHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cueBRHistoryIndex.setStatus("current")


class _CueBRHistoryOperation_Type(Integer32):
    """Custom type cueBRHistoryOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backup", 1),
          ("restore", 2))
    )


_CueBRHistoryOperation_Type.__name__ = "Integer32"
_CueBRHistoryOperation_Object = MibTableColumn
cueBRHistoryOperation = _CueBRHistoryOperation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 5, 1, 1, 2),
    _CueBRHistoryOperation_Type()
)
cueBRHistoryOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueBRHistoryOperation.setStatus("current")
_CueBRHistoryDate_Type = DateAndTime
_CueBRHistoryDate_Object = MibTableColumn
cueBRHistoryDate = _CueBRHistoryDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 5, 1, 1, 3),
    _CueBRHistoryDate_Type()
)
cueBRHistoryDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueBRHistoryDate.setStatus("current")


class _CueBRHistoryResult_Type(Integer32):
    """Custom type cueBRHistoryResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failure", 2),
          ("success", 1))
    )


_CueBRHistoryResult_Type.__name__ = "Integer32"
_CueBRHistoryResult_Object = MibTableColumn
cueBRHistoryResult = _CueBRHistoryResult_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 1, 5, 1, 1, 4),
    _CueBRHistoryResult_Type()
)
cueBRHistoryResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cueBRHistoryResult.setStatus("current")
_CiscoUnityExpressMIBConform_ObjectIdentity = ObjectIdentity
ciscoUnityExpressMIBConform = _CiscoUnityExpressMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 2)
)
_CiscoUnityExpressMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoUnityExpressMIBCompliances = _CiscoUnityExpressMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 2, 1)
)
_CiscoUnityExpressMIBGroups_ObjectIdentity = ObjectIdentity
ciscoUnityExpressMIBGroups = _CiscoUnityExpressMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 2, 2)
)

# Managed Objects groups

cueSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 2, 2, 1)
)
cueSystemGroup.setObjects(
      *(("CISCO-UNITY-EXPRESS-MIB", "cueShutdownRequest"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueAVTNumber"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueVoicemailNumber"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueAANumber"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueHardwareModuleType"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueCallControlAgentType"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueSIPGatewayName"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueSIPGatewayIPType"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueSIPGatewayIP"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueSIPPort"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueJTAPIServerName"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueJTAPIServerIPType"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueJTAPIServerIP"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueJTAPISubsystemState"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueJTAPIUsername"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueJTAPISoftwareVersion"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueJTAPIPortsRegistered"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueDefaultMailboxSize"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueDefaultGreetingSize"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueDefaultMessageSizeMax"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueDefaultMessageExpiryTime"))
)
if mibBuilder.loadTexts:
    cueSystemGroup.setStatus("deprecated")

cueUsageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 2, 2, 2)
)
cueUsageGroup.setObjects(
      *(("CISCO-UNITY-EXPRESS-MIB", "cueLicensedPortsMax"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueActiveCalls"),
        ("CISCO-UNITY-EXPRESS-MIB", "cuePersonalMailboxes"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueGeneralDeliveryMailboxes"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueOrphanedMailboxes"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueCapacityOfVoicemail"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueAllocatedCapacity"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueTotalTimeUsed"),
        ("CISCO-UNITY-EXPRESS-MIB", "cuePercentTimeUsed"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueMessageTimeUsed"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueMessageCount"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueAverageMessageLength"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueGreetingTimeUsed"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueGreetingCount"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueAverageGreetingLength"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueMboxOwner"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueMboxPrimaryExtension"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueMboxType"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueMboxDescription"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueMboxSize"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueMboxTimeUsed"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueMboxPercentTimeUsed"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueMboxNumberOfMessages"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueMboxNumberOfNewMessages"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueMboxNumberOfSavedMessages"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueMboxMessageSizeMax"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueMboxMessageExpiryTime"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueMboxPlayTutorial"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueMboxGreetingType"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueMboxEnabled"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueMboxBusy"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueMboxMWIState"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueMessagesLeft"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueMessagesRetrieved"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueMessagesDeleted"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueLicensedMailboxesMax"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueMailboxesAbove90PercentFull"))
)
if mibBuilder.loadTexts:
    cueUsageGroup.setStatus("current")

cueSecurityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 2, 2, 3)
)
cueSecurityGroup.setObjects(
      *(("CISCO-UNITY-EXPRESS-MIB", "cueLoginAttempts"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueLoginUsernameFailures"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueLoginPasswordFailures"),
        ("CISCO-UNITY-EXPRESS-MIB", "cuePINAttempts"),
        ("CISCO-UNITY-EXPRESS-MIB", "cuePINResets"),
        ("CISCO-UNITY-EXPRESS-MIB", "cuePINUidFailures"),
        ("CISCO-UNITY-EXPRESS-MIB", "cuePINPasswordFailures"))
)
if mibBuilder.loadTexts:
    cueSecurityGroup.setStatus("current")

cueNotifGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 2, 2, 4)
)
cueNotifGroup.setObjects(
      *(("CISCO-UNITY-EXPRESS-MIB", "cueNotifEnable"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueNotifSeverity"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueNotifDate"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueNotifDescription"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueNotifDetail"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueLoginUsernameThresh"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueLoginPasswordThresh"),
        ("CISCO-UNITY-EXPRESS-MIB", "cuePINUidThresh"),
        ("CISCO-UNITY-EXPRESS-MIB", "cuePINPasswordThresh"),
        ("CISCO-UNITY-EXPRESS-MIB", "cuePINResetThresh"))
)
if mibBuilder.loadTexts:
    cueNotifGroup.setStatus("current")

cueBackupRestoreGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 2, 2, 6)
)
cueBackupRestoreGroup.setObjects(
      *(("CISCO-UNITY-EXPRESS-MIB", "cueBRHistoryOperation"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueBRHistoryDate"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueBRHistoryResult"))
)
if mibBuilder.loadTexts:
    cueBackupRestoreGroup.setStatus("current")

cueSystemGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 2, 2, 7)
)
cueSystemGroupRev1.setObjects(
      *(("CISCO-UNITY-EXPRESS-MIB", "cueShutdownRequest"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueAVTNumber"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueVoicemailNumber"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueAANumber"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueCallControlAgentType"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueSIPGatewayName"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueSIPGatewayIPType"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueSIPGatewayIP"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueSIPPort"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueJTAPIServerName"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueJTAPIServerIPType"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueJTAPIServerIP"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueJTAPISubsystemState"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueJTAPIUsername"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueJTAPISoftwareVersion"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueJTAPIPortsRegistered"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueDefaultMailboxSize"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueDefaultGreetingSize"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueDefaultMessageSizeMax"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueDefaultMessageExpiryTime"))
)
if mibBuilder.loadTexts:
    cueSystemGroupRev1.setStatus("current")


# Notification objects

ciscoUnityExpressApplAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 0, 1)
)
ciscoUnityExpressApplAlert.setObjects(
      *(("CISCO-UNITY-EXPRESS-MIB", "cueNotifSeverity"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueNotifDate"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueNotifDescription"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueNotifDetail"))
)
if mibBuilder.loadTexts:
    ciscoUnityExpressApplAlert.setStatus(
        "current"
    )

ciscoUnityExpressStorageAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 0, 2)
)
ciscoUnityExpressStorageAlert.setObjects(
      *(("CISCO-UNITY-EXPRESS-MIB", "cueNotifSeverity"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueNotifDate"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueNotifDescription"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueNotifDetail"))
)
if mibBuilder.loadTexts:
    ciscoUnityExpressStorageAlert.setStatus(
        "current"
    )

ciscoUnityExpressSecurityAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 0, 3)
)
ciscoUnityExpressSecurityAlert.setObjects(
      *(("CISCO-UNITY-EXPRESS-MIB", "cueNotifSeverity"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueNotifDate"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueNotifDescription"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueNotifDetail"))
)
if mibBuilder.loadTexts:
    ciscoUnityExpressSecurityAlert.setStatus(
        "current"
    )

ciscoUnityExpressCallMgrAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 0, 4)
)
ciscoUnityExpressCallMgrAlert.setObjects(
      *(("CISCO-UNITY-EXPRESS-MIB", "cueNotifSeverity"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueNotifDate"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueNotifDescription"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueNotifDetail"))
)
if mibBuilder.loadTexts:
    ciscoUnityExpressCallMgrAlert.setStatus(
        "current"
    )

ciscoUnityExpressRescExhausted = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 0, 5)
)
ciscoUnityExpressRescExhausted.setObjects(
      *(("CISCO-UNITY-EXPRESS-MIB", "cueNotifSeverity"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueNotifDate"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueNotifDescription"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueNotifDetail"))
)
if mibBuilder.loadTexts:
    ciscoUnityExpressRescExhausted.setStatus(
        "current"
    )

ciscoUnityExpressBackupAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 0, 6)
)
ciscoUnityExpressBackupAlert.setObjects(
      *(("CISCO-UNITY-EXPRESS-MIB", "cueNotifSeverity"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueNotifDate"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueNotifDescription"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueNotifDetail"))
)
if mibBuilder.loadTexts:
    ciscoUnityExpressBackupAlert.setStatus(
        "current"
    )

ciscoUnityExpressNTPAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 0, 7)
)
ciscoUnityExpressNTPAlert.setObjects(
      *(("CISCO-UNITY-EXPRESS-MIB", "cueNotifSeverity"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueNotifDate"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueNotifDescription"),
        ("CISCO-UNITY-EXPRESS-MIB", "cueNotifDetail"))
)
if mibBuilder.loadTexts:
    ciscoUnityExpressNTPAlert.setStatus(
        "current"
    )


# Notifications groups

ciscoUnityExpressMIBNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 2, 2, 5)
)
ciscoUnityExpressMIBNotificationsGroup.setObjects(
      *(("CISCO-UNITY-EXPRESS-MIB", "ciscoUnityExpressApplAlert"),
        ("CISCO-UNITY-EXPRESS-MIB", "ciscoUnityExpressStorageAlert"),
        ("CISCO-UNITY-EXPRESS-MIB", "ciscoUnityExpressSecurityAlert"),
        ("CISCO-UNITY-EXPRESS-MIB", "ciscoUnityExpressCallMgrAlert"),
        ("CISCO-UNITY-EXPRESS-MIB", "ciscoUnityExpressRescExhausted"),
        ("CISCO-UNITY-EXPRESS-MIB", "ciscoUnityExpressBackupAlert"),
        ("CISCO-UNITY-EXPRESS-MIB", "ciscoUnityExpressNTPAlert"))
)
if mibBuilder.loadTexts:
    ciscoUnityExpressMIBNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoUnityExpressMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoUnityExpressMIBCompliance.setStatus(
        "current"
    )

ciscoUnityExpressMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 420, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoUnityExpressMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNITY-EXPRESS-MIB",
    **{"ciscoUnityExpressMIB": ciscoUnityExpressMIB,
       "ciscoUnityExpressMIBNotifs": ciscoUnityExpressMIBNotifs,
       "ciscoUnityExpressApplAlert": ciscoUnityExpressApplAlert,
       "ciscoUnityExpressStorageAlert": ciscoUnityExpressStorageAlert,
       "ciscoUnityExpressSecurityAlert": ciscoUnityExpressSecurityAlert,
       "ciscoUnityExpressCallMgrAlert": ciscoUnityExpressCallMgrAlert,
       "ciscoUnityExpressRescExhausted": ciscoUnityExpressRescExhausted,
       "ciscoUnityExpressBackupAlert": ciscoUnityExpressBackupAlert,
       "ciscoUnityExpressNTPAlert": ciscoUnityExpressNTPAlert,
       "ciscoUnityExpressMIBObjects": ciscoUnityExpressMIBObjects,
       "cueSystem": cueSystem,
       "cueSystemControl": cueSystemControl,
       "cueShutdownRequest": cueShutdownRequest,
       "cueSystemScalars": cueSystemScalars,
       "cueAVTNumber": cueAVTNumber,
       "cueVoicemailNumber": cueVoicemailNumber,
       "cueAANumber": cueAANumber,
       "cueHardwareModuleType": cueHardwareModuleType,
       "cueCallControlAgentType": cueCallControlAgentType,
       "cueSIPInfo": cueSIPInfo,
       "cueSIPGatewayName": cueSIPGatewayName,
       "cueSIPGatewayIPType": cueSIPGatewayIPType,
       "cueSIPGatewayIP": cueSIPGatewayIP,
       "cueSIPPort": cueSIPPort,
       "cueJTAPIInfo": cueJTAPIInfo,
       "cueJTAPIServerTable": cueJTAPIServerTable,
       "cueJTAPIServerEntry": cueJTAPIServerEntry,
       "cueJTAPIServerIndex": cueJTAPIServerIndex,
       "cueJTAPIServerName": cueJTAPIServerName,
       "cueJTAPIServerIPType": cueJTAPIServerIPType,
       "cueJTAPIServerIP": cueJTAPIServerIP,
       "cueJTAPISubsystemState": cueJTAPISubsystemState,
       "cueJTAPIUsername": cueJTAPIUsername,
       "cueJTAPISoftwareVersion": cueJTAPISoftwareVersion,
       "cueJTAPIPortsRegistered": cueJTAPIPortsRegistered,
       "cueSystemDefaults": cueSystemDefaults,
       "cueDefaultMailboxSize": cueDefaultMailboxSize,
       "cueDefaultGreetingSize": cueDefaultGreetingSize,
       "cueDefaultMessageSizeMax": cueDefaultMessageSizeMax,
       "cueDefaultMessageExpiryTime": cueDefaultMessageExpiryTime,
       "cueUsage": cueUsage,
       "cueUsageScalars": cueUsageScalars,
       "cueLicensedPortsMax": cueLicensedPortsMax,
       "cueActiveCalls": cueActiveCalls,
       "cuePersonalMailboxes": cuePersonalMailboxes,
       "cueGeneralDeliveryMailboxes": cueGeneralDeliveryMailboxes,
       "cueOrphanedMailboxes": cueOrphanedMailboxes,
       "cueCapacityOfVoicemail": cueCapacityOfVoicemail,
       "cueAllocatedCapacity": cueAllocatedCapacity,
       "cueTotalTimeUsed": cueTotalTimeUsed,
       "cuePercentTimeUsed": cuePercentTimeUsed,
       "cueMessageTimeUsed": cueMessageTimeUsed,
       "cueMessageCount": cueMessageCount,
       "cueAverageMessageLength": cueAverageMessageLength,
       "cueGreetingTimeUsed": cueGreetingTimeUsed,
       "cueGreetingCount": cueGreetingCount,
       "cueAverageGreetingLength": cueAverageGreetingLength,
       "cueMessagesLeft": cueMessagesLeft,
       "cueMessagesRetrieved": cueMessagesRetrieved,
       "cueMessagesDeleted": cueMessagesDeleted,
       "cueLicensedMailboxesMax": cueLicensedMailboxesMax,
       "cueMailboxesAbove90PercentFull": cueMailboxesAbove90PercentFull,
       "cueMboxTable": cueMboxTable,
       "cueMboxEntry": cueMboxEntry,
       "cueMboxIndex": cueMboxIndex,
       "cueMboxOwner": cueMboxOwner,
       "cueMboxPrimaryExtension": cueMboxPrimaryExtension,
       "cueMboxType": cueMboxType,
       "cueMboxDescription": cueMboxDescription,
       "cueMboxSize": cueMboxSize,
       "cueMboxTimeUsed": cueMboxTimeUsed,
       "cueMboxPercentTimeUsed": cueMboxPercentTimeUsed,
       "cueMboxNumberOfMessages": cueMboxNumberOfMessages,
       "cueMboxNumberOfNewMessages": cueMboxNumberOfNewMessages,
       "cueMboxNumberOfSavedMessages": cueMboxNumberOfSavedMessages,
       "cueMboxMessageSizeMax": cueMboxMessageSizeMax,
       "cueMboxMessageExpiryTime": cueMboxMessageExpiryTime,
       "cueMboxPlayTutorial": cueMboxPlayTutorial,
       "cueMboxGreetingType": cueMboxGreetingType,
       "cueMboxEnabled": cueMboxEnabled,
       "cueMboxBusy": cueMboxBusy,
       "cueMboxMWIState": cueMboxMWIState,
       "cueSecurity": cueSecurity,
       "cueLoginInfo": cueLoginInfo,
       "cueLoginAttempts": cueLoginAttempts,
       "cueLoginUsernameFailures": cueLoginUsernameFailures,
       "cueLoginPasswordFailures": cueLoginPasswordFailures,
       "cuePINInfo": cuePINInfo,
       "cuePINAttempts": cuePINAttempts,
       "cuePINResets": cuePINResets,
       "cuePINUidFailures": cuePINUidFailures,
       "cuePINPasswordFailures": cuePINPasswordFailures,
       "cueNotif": cueNotif,
       "cueNotifConfig": cueNotifConfig,
       "cueNotifEnable": cueNotifEnable,
       "cueNotifInfo": cueNotifInfo,
       "cueNotifSeverity": cueNotifSeverity,
       "cueNotifDate": cueNotifDate,
       "cueNotifDescription": cueNotifDescription,
       "cueNotifDetail": cueNotifDetail,
       "cueNotifSecurity": cueNotifSecurity,
       "cueLoginUsernameThresh": cueLoginUsernameThresh,
       "cueLoginPasswordThresh": cueLoginPasswordThresh,
       "cuePINUidThresh": cuePINUidThresh,
       "cuePINPasswordThresh": cuePINPasswordThresh,
       "cuePINResetThresh": cuePINResetThresh,
       "cueBackupRestore": cueBackupRestore,
       "cueBRHistoryTable": cueBRHistoryTable,
       "cueBRHistoryEntry": cueBRHistoryEntry,
       "cueBRHistoryIndex": cueBRHistoryIndex,
       "cueBRHistoryOperation": cueBRHistoryOperation,
       "cueBRHistoryDate": cueBRHistoryDate,
       "cueBRHistoryResult": cueBRHistoryResult,
       "ciscoUnityExpressMIBConform": ciscoUnityExpressMIBConform,
       "ciscoUnityExpressMIBCompliances": ciscoUnityExpressMIBCompliances,
       "ciscoUnityExpressMIBCompliance": ciscoUnityExpressMIBCompliance,
       "ciscoUnityExpressMIBComplianceRev1": ciscoUnityExpressMIBComplianceRev1,
       "ciscoUnityExpressMIBGroups": ciscoUnityExpressMIBGroups,
       "cueSystemGroup": cueSystemGroup,
       "cueUsageGroup": cueUsageGroup,
       "cueSecurityGroup": cueSecurityGroup,
       "cueNotifGroup": cueNotifGroup,
       "ciscoUnityExpressMIBNotificationsGroup": ciscoUnityExpressMIBNotificationsGroup,
       "cueBackupRestoreGroup": cueBackupRestoreGroup,
       "cueSystemGroupRev1": cueSystemGroupRev1}
)
