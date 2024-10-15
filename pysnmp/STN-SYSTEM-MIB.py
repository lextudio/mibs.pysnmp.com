# SNMP MIB module (STN-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/STN-SYSTEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:58:18 2024
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

(stnSystems,) = mibBuilder.importSymbols(
    "SPRING-TIDE-NETWORKS-SMI",
    "stnSystems")


# MODULE-IDENTITY

stnSystemMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_StnSystemMIBObjects_ObjectIdentity = ObjectIdentity
stnSystemMIBObjects = _StnSystemMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 4, 1)
)
_StnSysTimeGroup_ObjectIdentity = ObjectIdentity
stnSysTimeGroup = _StnSysTimeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 4, 1, 1)
)


class _StnUTCOffset_Type(Unsigned32):
    """Custom type stnUTCOffset based on Unsigned32"""
    defaultValue = 0


_StnUTCOffset_Object = MibScalar
stnUTCOffset = _StnUTCOffset_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 4, 1, 1, 1),
    _StnUTCOffset_Type()
)
stnUTCOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnUTCOffset.setStatus("current")


class _StnDaylightTime_Type(TruthValue):
    """Custom type stnDaylightTime based on TruthValue"""
    defaultValue = 1


_StnDaylightTime_Object = MibScalar
stnDaylightTime = _StnDaylightTime_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 4, 1, 1, 2),
    _StnDaylightTime_Type()
)
stnDaylightTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnDaylightTime.setStatus("current")


class _StnTimeSource_Type(Integer32):
    """Custom type stnTimeSource based on Integer32"""
    defaultValue = 4

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
        *(("all", 4),
          ("external-NTP", 2),
          ("external-RC868", 3),
          ("internal", 1))
    )


_StnTimeSource_Type.__name__ = "Integer32"
_StnTimeSource_Object = MibScalar
stnTimeSource = _StnTimeSource_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 4, 1, 1, 3),
    _StnTimeSource_Type()
)
stnTimeSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnTimeSource.setStatus("current")
_StnRFC868Server_Type = IpAddress
_StnRFC868Server_Object = MibScalar
stnRFC868Server = _StnRFC868Server_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 4, 1, 1, 4),
    _StnRFC868Server_Type()
)
stnRFC868Server.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnRFC868Server.setStatus("current")
_StnNTPServer_Type = IpAddress
_StnNTPServer_Object = MibScalar
stnNTPServer = _StnNTPServer_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 4, 1, 1, 5),
    _StnNTPServer_Type()
)
stnNTPServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnNTPServer.setStatus("current")


class _StnQueryTime_Type(Integer32):
    """Custom type stnQueryTime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_StnQueryTime_Type.__name__ = "Integer32"
_StnQueryTime_Object = MibScalar
stnQueryTime = _StnQueryTime_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 4, 1, 1, 6),
    _StnQueryTime_Type()
)
stnQueryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnQueryTime.setStatus("current")
_StnSysAttrGroup_ObjectIdentity = ObjectIdentity
stnSysAttrGroup = _StnSysAttrGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 4, 1, 2)
)
_StnDeviceIPAddress_Type = IpAddress
_StnDeviceIPAddress_Object = MibScalar
stnDeviceIPAddress = _StnDeviceIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 4, 1, 2, 1),
    _StnDeviceIPAddress_Type()
)
stnDeviceIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnDeviceIPAddress.setStatus("current")
_StnDeviceSubnetMask_Type = IpAddress
_StnDeviceSubnetMask_Object = MibScalar
stnDeviceSubnetMask = _StnDeviceSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 4, 1, 2, 2),
    _StnDeviceSubnetMask_Type()
)
stnDeviceSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnDeviceSubnetMask.setStatus("current")


class _StnSocketDelay_Type(Integer32):
    """Custom type stnSocketDelay based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_StnSocketDelay_Type.__name__ = "Integer32"
_StnSocketDelay_Object = MibScalar
stnSocketDelay = _StnSocketDelay_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 4, 1, 2, 3),
    _StnSocketDelay_Type()
)
stnSocketDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSocketDelay.setStatus("current")


class _StnDumpMode_Type(Integer32):
    """Custom type stnDumpMode based on Integer32"""
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
        *(("context", 3),
          ("core", 2),
          ("log", 4),
          ("none", 1))
    )


_StnDumpMode_Type.__name__ = "Integer32"
_StnDumpMode_Object = MibScalar
stnDumpMode = _StnDumpMode_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 4, 1, 2, 4),
    _StnDumpMode_Type()
)
stnDumpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnDumpMode.setStatus("current")
_StnSysServersGroup_ObjectIdentity = ObjectIdentity
stnSysServersGroup = _StnSysServersGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 4, 1, 3)
)


class _StnTelnetServerEnabled_Type(TruthValue):
    """Custom type stnTelnetServerEnabled based on TruthValue"""


_StnTelnetServerEnabled_Object = MibScalar
stnTelnetServerEnabled = _StnTelnetServerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 4, 1, 3, 1),
    _StnTelnetServerEnabled_Type()
)
stnTelnetServerEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnTelnetServerEnabled.setStatus("current")


class _StnFTPServerEnabled_Type(TruthValue):
    """Custom type stnFTPServerEnabled based on TruthValue"""


_StnFTPServerEnabled_Object = MibScalar
stnFTPServerEnabled = _StnFTPServerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 4, 1, 3, 2),
    _StnFTPServerEnabled_Type()
)
stnFTPServerEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnFTPServerEnabled.setStatus("current")


class _StnDNSServerEnabled_Type(TruthValue):
    """Custom type stnDNSServerEnabled based on TruthValue"""


_StnDNSServerEnabled_Object = MibScalar
stnDNSServerEnabled = _StnDNSServerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 4, 1, 3, 3),
    _StnDNSServerEnabled_Type()
)
stnDNSServerEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnDNSServerEnabled.setStatus("current")
_StnSysCfgCtrlGroup_ObjectIdentity = ObjectIdentity
stnSysCfgCtrlGroup = _StnSysCfgCtrlGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 4, 1, 4)
)
_StnSysCfgCtrlNfsHost_Type = IpAddress
_StnSysCfgCtrlNfsHost_Object = MibScalar
stnSysCfgCtrlNfsHost = _StnSysCfgCtrlNfsHost_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 4, 1, 4, 1),
    _StnSysCfgCtrlNfsHost_Type()
)
stnSysCfgCtrlNfsHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSysCfgCtrlNfsHost.setStatus("current")


class _StnSysCfgCtrlNfsPath_Type(DisplayString):
    """Custom type stnSysCfgCtrlNfsPath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_StnSysCfgCtrlNfsPath_Type.__name__ = "DisplayString"
_StnSysCfgCtrlNfsPath_Object = MibScalar
stnSysCfgCtrlNfsPath = _StnSysCfgCtrlNfsPath_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 4, 1, 4, 2),
    _StnSysCfgCtrlNfsPath_Type()
)
stnSysCfgCtrlNfsPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSysCfgCtrlNfsPath.setStatus("current")


class _StnSysCfgCtrlCommitToFlashTimeout_Type(Integer32):
    """Custom type stnSysCfgCtrlCommitToFlashTimeout based on Integer32"""
    defaultValue = 20


_StnSysCfgCtrlCommitToFlashTimeout_Object = MibScalar
stnSysCfgCtrlCommitToFlashTimeout = _StnSysCfgCtrlCommitToFlashTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3551, 2, 4, 1, 4, 3),
    _StnSysCfgCtrlCommitToFlashTimeout_Type()
)
stnSysCfgCtrlCommitToFlashTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnSysCfgCtrlCommitToFlashTimeout.setStatus("current")
_StnSystemMIBConformance_ObjectIdentity = ObjectIdentity
stnSystemMIBConformance = _StnSystemMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 2, 4, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STN-SYSTEM-MIB",
    **{"stnSystemMIB": stnSystemMIB,
       "stnSystemMIBObjects": stnSystemMIBObjects,
       "stnSysTimeGroup": stnSysTimeGroup,
       "stnUTCOffset": stnUTCOffset,
       "stnDaylightTime": stnDaylightTime,
       "stnTimeSource": stnTimeSource,
       "stnRFC868Server": stnRFC868Server,
       "stnNTPServer": stnNTPServer,
       "stnQueryTime": stnQueryTime,
       "stnSysAttrGroup": stnSysAttrGroup,
       "stnDeviceIPAddress": stnDeviceIPAddress,
       "stnDeviceSubnetMask": stnDeviceSubnetMask,
       "stnSocketDelay": stnSocketDelay,
       "stnDumpMode": stnDumpMode,
       "stnSysServersGroup": stnSysServersGroup,
       "stnTelnetServerEnabled": stnTelnetServerEnabled,
       "stnFTPServerEnabled": stnFTPServerEnabled,
       "stnDNSServerEnabled": stnDNSServerEnabled,
       "stnSysCfgCtrlGroup": stnSysCfgCtrlGroup,
       "stnSysCfgCtrlNfsHost": stnSysCfgCtrlNfsHost,
       "stnSysCfgCtrlNfsPath": stnSysCfgCtrlNfsPath,
       "stnSysCfgCtrlCommitToFlashTimeout": stnSysCfgCtrlCommitToFlashTimeout,
       "stnSystemMIBConformance": stnSystemMIBConformance}
)
