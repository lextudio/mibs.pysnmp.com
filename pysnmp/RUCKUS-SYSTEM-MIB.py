# SNMP MIB module (RUCKUS-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RUCKUS-SYSTEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:48:44 2024
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

(ruckusCommonSystemModule,) = mibBuilder.importSymbols(
    "RUCKUS-ROOT-MIB",
    "ruckusCommonSystemModule")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ruckusSystemMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuckusSystemObjects_ObjectIdentity = ObjectIdentity
ruckusSystemObjects = _RuckusSystemObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1)
)
_RuckusSystemInfo_ObjectIdentity = ObjectIdentity
ruckusSystemInfo = _RuckusSystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 1)
)
_RuckusSystemCPUUtil_Type = Integer32
_RuckusSystemCPUUtil_Object = MibScalar
ruckusSystemCPUUtil = _RuckusSystemCPUUtil_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 1, 1),
    _RuckusSystemCPUUtil_Type()
)
ruckusSystemCPUUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSystemCPUUtil.setStatus("current")
_RuckusSystemMemoryUtil_Type = Integer32
_RuckusSystemMemoryUtil_Object = MibScalar
ruckusSystemMemoryUtil = _RuckusSystemMemoryUtil_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 1, 2),
    _RuckusSystemMemoryUtil_Type()
)
ruckusSystemMemoryUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSystemMemoryUtil.setStatus("current")
_RuckusSystemServices_ObjectIdentity = ObjectIdentity
ruckusSystemServices = _RuckusSystemServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 2)
)
_RuckusSystemHTTP_ObjectIdentity = ObjectIdentity
ruckusSystemHTTP = _RuckusSystemHTTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 2, 1)
)


class _RuckusSystemHTTPStatus_Type(TruthValue):
    """Custom type ruckusSystemHTTPStatus based on TruthValue"""


_RuckusSystemHTTPStatus_Object = MibScalar
ruckusSystemHTTPStatus = _RuckusSystemHTTPStatus_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 2, 1, 1),
    _RuckusSystemHTTPStatus_Type()
)
ruckusSystemHTTPStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusSystemHTTPStatus.setStatus("current")
_RuckusSystemHTTPS_ObjectIdentity = ObjectIdentity
ruckusSystemHTTPS = _RuckusSystemHTTPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 2, 2)
)


class _RuckusSystemHTTPSStatus_Type(TruthValue):
    """Custom type ruckusSystemHTTPSStatus based on TruthValue"""


_RuckusSystemHTTPSStatus_Object = MibScalar
ruckusSystemHTTPSStatus = _RuckusSystemHTTPSStatus_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 2, 2, 1),
    _RuckusSystemHTTPSStatus_Type()
)
ruckusSystemHTTPSStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusSystemHTTPSStatus.setStatus("current")
_RuckusSystemTelnet_ObjectIdentity = ObjectIdentity
ruckusSystemTelnet = _RuckusSystemTelnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 2, 3)
)


class _RuckusSystemTelnetStatus_Type(TruthValue):
    """Custom type ruckusSystemTelnetStatus based on TruthValue"""


_RuckusSystemTelnetStatus_Object = MibScalar
ruckusSystemTelnetStatus = _RuckusSystemTelnetStatus_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 2, 3, 1),
    _RuckusSystemTelnetStatus_Type()
)
ruckusSystemTelnetStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusSystemTelnetStatus.setStatus("current")
_RuckusSystemSSH_ObjectIdentity = ObjectIdentity
ruckusSystemSSH = _RuckusSystemSSH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 2, 4)
)


class _RuckusSystemSSHStatus_Type(TruthValue):
    """Custom type ruckusSystemSSHStatus based on TruthValue"""


_RuckusSystemSSHStatus_Object = MibScalar
ruckusSystemSSHStatus = _RuckusSystemSSHStatus_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 2, 4, 1),
    _RuckusSystemSSHStatus_Type()
)
ruckusSystemSSHStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusSystemSSHStatus.setStatus("current")
_RuckusSystemBonjour_ObjectIdentity = ObjectIdentity
ruckusSystemBonjour = _RuckusSystemBonjour_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 2, 5)
)


class _RuckusSystemBonjourStatus_Type(TruthValue):
    """Custom type ruckusSystemBonjourStatus based on TruthValue"""


_RuckusSystemBonjourStatus_Object = MibScalar
ruckusSystemBonjourStatus = _RuckusSystemBonjourStatus_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 2, 5, 1),
    _RuckusSystemBonjourStatus_Type()
)
ruckusSystemBonjourStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusSystemBonjourStatus.setStatus("current")
_RuckusSystemSyslog_ObjectIdentity = ObjectIdentity
ruckusSystemSyslog = _RuckusSystemSyslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 2, 6)
)


class _RuckusSystemSyslogStatus_Type(TruthValue):
    """Custom type ruckusSystemSyslogStatus based on TruthValue"""


_RuckusSystemSyslogStatus_Object = MibScalar
ruckusSystemSyslogStatus = _RuckusSystemSyslogStatus_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 2, 6, 1),
    _RuckusSystemSyslogStatus_Type()
)
ruckusSystemSyslogStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusSystemSyslogStatus.setStatus("current")


class _RuckusSystemSyslogServerIP_Type(OctetString):
    """Custom type ruckusSystemSyslogServerIP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 40),
    )


_RuckusSystemSyslogServerIP_Type.__name__ = "OctetString"
_RuckusSystemSyslogServerIP_Object = MibScalar
ruckusSystemSyslogServerIP = _RuckusSystemSyslogServerIP_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 2, 6, 2),
    _RuckusSystemSyslogServerIP_Type()
)
ruckusSystemSyslogServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusSystemSyslogServerIP.setStatus("current")
_RuckusSystemSyslogServerPort_Type = Integer32
_RuckusSystemSyslogServerPort_Object = MibScalar
ruckusSystemSyslogServerPort = _RuckusSystemSyslogServerPort_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 2, 6, 3),
    _RuckusSystemSyslogServerPort_Type()
)
ruckusSystemSyslogServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusSystemSyslogServerPort.setStatus("current")
_RuckusSystemNTP_ObjectIdentity = ObjectIdentity
ruckusSystemNTP = _RuckusSystemNTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 2, 7)
)


class _RuckusSystemNTPStatus_Type(TruthValue):
    """Custom type ruckusSystemNTPStatus based on TruthValue"""


_RuckusSystemNTPStatus_Object = MibScalar
ruckusSystemNTPStatus = _RuckusSystemNTPStatus_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 2, 7, 1),
    _RuckusSystemNTPStatus_Type()
)
ruckusSystemNTPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSystemNTPStatus.setStatus("current")
_RuckusSystemNTPGMTTime_Type = OctetString
_RuckusSystemNTPGMTTime_Object = MibScalar
ruckusSystemNTPGMTTime = _RuckusSystemNTPGMTTime_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 2, 7, 2),
    _RuckusSystemNTPGMTTime_Type()
)
ruckusSystemNTPGMTTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSystemNTPGMTTime.setStatus("current")


class _RuckusSystemNTPActiveServer_Type(OctetString):
    """Custom type ruckusSystemNTPActiveServer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_RuckusSystemNTPActiveServer_Type.__name__ = "OctetString"
_RuckusSystemNTPActiveServer_Object = MibScalar
ruckusSystemNTPActiveServer = _RuckusSystemNTPActiveServer_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 2, 7, 3),
    _RuckusSystemNTPActiveServer_Type()
)
ruckusSystemNTPActiveServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusSystemNTPActiveServer.setStatus("current")
_RuckusSystemNTPUpdate_Type = Integer32
_RuckusSystemNTPUpdate_Object = MibScalar
ruckusSystemNTPUpdate = _RuckusSystemNTPUpdate_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 2, 7, 4),
    _RuckusSystemNTPUpdate_Type()
)
ruckusSystemNTPUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusSystemNTPUpdate.setStatus("current")
_RuckusSystemFlexMaster_ObjectIdentity = ObjectIdentity
ruckusSystemFlexMaster = _RuckusSystemFlexMaster_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 2, 8)
)


class _RuckusSystemFlexMasterURL_Type(OctetString):
    """Custom type ruckusSystemFlexMasterURL based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_RuckusSystemFlexMasterURL_Type.__name__ = "OctetString"
_RuckusSystemFlexMasterURL_Object = MibScalar
ruckusSystemFlexMasterURL = _RuckusSystemFlexMasterURL_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 2, 8, 1),
    _RuckusSystemFlexMasterURL_Type()
)
ruckusSystemFlexMasterURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusSystemFlexMasterURL.setStatus("current")
_RuckusSystemCommands_ObjectIdentity = ObjectIdentity
ruckusSystemCommands = _RuckusSystemCommands_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 3)
)


class _RuckusSystemReboot_Type(TruthValue):
    """Custom type ruckusSystemReboot based on TruthValue"""


_RuckusSystemReboot_Object = MibScalar
ruckusSystemReboot = _RuckusSystemReboot_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 3, 1),
    _RuckusSystemReboot_Type()
)
ruckusSystemReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusSystemReboot.setStatus("current")


class _RuckusSystemSetFactory_Type(TruthValue):
    """Custom type ruckusSystemSetFactory based on TruthValue"""


_RuckusSystemSetFactory_Object = MibScalar
ruckusSystemSetFactory = _RuckusSystemSetFactory_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 3, 2),
    _RuckusSystemSetFactory_Type()
)
ruckusSystemSetFactory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusSystemSetFactory.setStatus("current")


class _RuckusSystemDHCPRenew_Type(TruthValue):
    """Custom type ruckusSystemDHCPRenew based on TruthValue"""


_RuckusSystemDHCPRenew_Object = MibScalar
ruckusSystemDHCPRenew = _RuckusSystemDHCPRenew_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 1, 3, 3),
    _RuckusSystemDHCPRenew_Type()
)
ruckusSystemDHCPRenew.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusSystemDHCPRenew.setStatus("current")
_RuckusSystemEvents_ObjectIdentity = ObjectIdentity
ruckusSystemEvents = _RuckusSystemEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 11, 1, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUCKUS-SYSTEM-MIB",
    **{"ruckusSystemMIB": ruckusSystemMIB,
       "ruckusSystemObjects": ruckusSystemObjects,
       "ruckusSystemInfo": ruckusSystemInfo,
       "ruckusSystemCPUUtil": ruckusSystemCPUUtil,
       "ruckusSystemMemoryUtil": ruckusSystemMemoryUtil,
       "ruckusSystemServices": ruckusSystemServices,
       "ruckusSystemHTTP": ruckusSystemHTTP,
       "ruckusSystemHTTPStatus": ruckusSystemHTTPStatus,
       "ruckusSystemHTTPS": ruckusSystemHTTPS,
       "ruckusSystemHTTPSStatus": ruckusSystemHTTPSStatus,
       "ruckusSystemTelnet": ruckusSystemTelnet,
       "ruckusSystemTelnetStatus": ruckusSystemTelnetStatus,
       "ruckusSystemSSH": ruckusSystemSSH,
       "ruckusSystemSSHStatus": ruckusSystemSSHStatus,
       "ruckusSystemBonjour": ruckusSystemBonjour,
       "ruckusSystemBonjourStatus": ruckusSystemBonjourStatus,
       "ruckusSystemSyslog": ruckusSystemSyslog,
       "ruckusSystemSyslogStatus": ruckusSystemSyslogStatus,
       "ruckusSystemSyslogServerIP": ruckusSystemSyslogServerIP,
       "ruckusSystemSyslogServerPort": ruckusSystemSyslogServerPort,
       "ruckusSystemNTP": ruckusSystemNTP,
       "ruckusSystemNTPStatus": ruckusSystemNTPStatus,
       "ruckusSystemNTPGMTTime": ruckusSystemNTPGMTTime,
       "ruckusSystemNTPActiveServer": ruckusSystemNTPActiveServer,
       "ruckusSystemNTPUpdate": ruckusSystemNTPUpdate,
       "ruckusSystemFlexMaster": ruckusSystemFlexMaster,
       "ruckusSystemFlexMasterURL": ruckusSystemFlexMasterURL,
       "ruckusSystemCommands": ruckusSystemCommands,
       "ruckusSystemReboot": ruckusSystemReboot,
       "ruckusSystemSetFactory": ruckusSystemSetFactory,
       "ruckusSystemDHCPRenew": ruckusSystemDHCPRenew,
       "ruckusSystemEvents": ruckusSystemEvents}
)
