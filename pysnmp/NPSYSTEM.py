# SNMP MIB module (NPSYSTEM) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NPSYSTEM
# Produced by pysmi-1.5.4 at Mon Oct 14 22:29:07 2024
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

(DateAndTime,
 DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")

(zhoneWtn,) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneWtn")


# MODULE-IDENTITY

npsystem = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 11)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SystemObjects_ObjectIdentity = ObjectIdentity
systemObjects = _SystemObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 11, 1)
)
_SerialNumber_Type = DisplayString
_SerialNumber_Object = MibScalar
serialNumber = _SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 11, 1, 1),
    _SerialNumber_Type()
)
serialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNumber.setStatus("current")
_FirmwareVersion_Type = DisplayString
_FirmwareVersion_Object = MibScalar
firmwareVersion = _FirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 11, 1, 2),
    _FirmwareVersion_Type()
)
firmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareVersion.setStatus("current")
_SystemDate_Type = DisplayString
_SystemDate_Object = MibScalar
systemDate = _SystemDate_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 11, 1, 3),
    _SystemDate_Type()
)
systemDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemDate.setStatus("current")
_SystemTime_Type = DisplayString
_SystemTime_Object = MibScalar
systemTime = _SystemTime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 11, 1, 4),
    _SystemTime_Type()
)
systemTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemTime.setStatus("current")
_SystemUpTime_Type = DisplayString
_SystemUpTime_Object = MibScalar
systemUpTime = _SystemUpTime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 11, 1, 5),
    _SystemUpTime_Type()
)
systemUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemUpTime.setStatus("current")
_SystemReboot_Type = Integer32
_SystemReboot_Object = MibScalar
systemReboot = _SystemReboot_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 11, 1, 6),
    _SystemReboot_Type()
)
systemReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemReboot.setStatus("current")
_SystemHostName_Type = DisplayString
_SystemHostName_Object = MibScalar
systemHostName = _SystemHostName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 11, 1, 7),
    _SystemHostName_Type()
)
systemHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemHostName.setStatus("current")
_SystemDomainName_Type = DisplayString
_SystemDomainName_Object = MibScalar
systemDomainName = _SystemDomainName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 11, 1, 8),
    _SystemDomainName_Type()
)
systemDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemDomainName.setStatus("current")
_SystemPrimaryDnsServer_Type = IpAddress
_SystemPrimaryDnsServer_Object = MibScalar
systemPrimaryDnsServer = _SystemPrimaryDnsServer_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 11, 1, 9),
    _SystemPrimaryDnsServer_Type()
)
systemPrimaryDnsServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemPrimaryDnsServer.setStatus("current")
_SystemSecondaryDnsServer_Type = IpAddress
_SystemSecondaryDnsServer_Object = MibScalar
systemSecondaryDnsServer = _SystemSecondaryDnsServer_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 11, 1, 10),
    _SystemSecondaryDnsServer_Type()
)
systemSecondaryDnsServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSecondaryDnsServer.setStatus("current")
_SystemGateway_Type = IpAddress
_SystemGateway_Object = MibScalar
systemGateway = _SystemGateway_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 11, 1, 11),
    _SystemGateway_Type()
)
systemGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemGateway.setStatus("current")


class _SystemRemoteSyslogStatus_Type(Integer32):
    """Custom type systemRemoteSyslogStatus based on Integer32"""
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


_SystemRemoteSyslogStatus_Type.__name__ = "Integer32"
_SystemRemoteSyslogStatus_Object = MibScalar
systemRemoteSyslogStatus = _SystemRemoteSyslogStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 11, 1, 12),
    _SystemRemoteSyslogStatus_Type()
)
systemRemoteSyslogStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemRemoteSyslogStatus.setStatus("current")
_SystemRemoteSyslogServer_Type = DisplayString
_SystemRemoteSyslogServer_Object = MibScalar
systemRemoteSyslogServer = _SystemRemoteSyslogServer_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 11, 1, 13),
    _SystemRemoteSyslogServer_Type()
)
systemRemoteSyslogServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemRemoteSyslogServer.setStatus("current")


class _SystemSyslogLocalStatus_Type(Integer32):
    """Custom type systemSyslogLocalStatus based on Integer32"""
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


_SystemSyslogLocalStatus_Type.__name__ = "Integer32"
_SystemSyslogLocalStatus_Object = MibScalar
systemSyslogLocalStatus = _SystemSyslogLocalStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 11, 1, 14),
    _SystemSyslogLocalStatus_Type()
)
systemSyslogLocalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSyslogLocalStatus.setStatus("current")


class _SystemSyslogMaxSize_Type(Integer32):
    """Custom type systemSyslogMaxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500),
    )


_SystemSyslogMaxSize_Type.__name__ = "Integer32"
_SystemSyslogMaxSize_Object = MibScalar
systemSyslogMaxSize = _SystemSyslogMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 11, 1, 15),
    _SystemSyslogMaxSize_Type()
)
systemSyslogMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSyslogMaxSize.setStatus("current")


class _SystemSyslogRotateNum_Type(Integer32):
    """Custom type systemSyslogRotateNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_SystemSyslogRotateNum_Type.__name__ = "Integer32"
_SystemSyslogRotateNum_Object = MibScalar
systemSyslogRotateNum = _SystemSyslogRotateNum_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 11, 1, 16),
    _SystemSyslogRotateNum_Type()
)
systemSyslogRotateNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSyslogRotateNum.setStatus("current")
_SystemTimezone_Type = DisplayString
_SystemTimezone_Object = MibScalar
systemTimezone = _SystemTimezone_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 11, 1, 17),
    _SystemTimezone_Type()
)
systemTimezone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemTimezone.setStatus("current")


class _SystemDaylightSavingStatus_Type(Integer32):
    """Custom type systemDaylightSavingStatus based on Integer32"""
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


_SystemDaylightSavingStatus_Type.__name__ = "Integer32"
_SystemDaylightSavingStatus_Object = MibScalar
systemDaylightSavingStatus = _SystemDaylightSavingStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 11, 1, 18),
    _SystemDaylightSavingStatus_Type()
)
systemDaylightSavingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemDaylightSavingStatus.setStatus("current")
_SystemNtpServer_Type = DisplayString
_SystemNtpServer_Object = MibScalar
systemNtpServer = _SystemNtpServer_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 11, 1, 19),
    _SystemNtpServer_Type()
)
systemNtpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemNtpServer.setStatus("current")


class _SystemNtpStatus_Type(Integer32):
    """Custom type systemNtpStatus based on Integer32"""
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


_SystemNtpStatus_Type.__name__ = "Integer32"
_SystemNtpStatus_Object = MibScalar
systemNtpStatus = _SystemNtpStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 11, 1, 20),
    _SystemNtpStatus_Type()
)
systemNtpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemNtpStatus.setStatus("current")
_SystemAction_Type = RowStatus
_SystemAction_Object = MibScalar
systemAction = _SystemAction_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 11, 1, 21),
    _SystemAction_Type()
)
systemAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemAction.setStatus("current")
_SystemRemoteSyslogServerPort_Type = Integer32
_SystemRemoteSyslogServerPort_Object = MibScalar
systemRemoteSyslogServerPort = _SystemRemoteSyslogServerPort_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 11, 1, 22),
    _SystemRemoteSyslogServerPort_Type()
)
systemRemoteSyslogServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemRemoteSyslogServerPort.setStatus("current")
_SystemServicesTable_Object = MibTable
systemServicesTable = _SystemServicesTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 11, 1, 23)
)
if mibBuilder.loadTexts:
    systemServicesTable.setStatus("current")
_SystemServicesTableEntry_Object = MibTableRow
systemServicesTableEntry = _SystemServicesTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 11, 1, 23, 1)
)
systemServicesTableEntry.setIndexNames(
    (0, "NPSYSTEM", "serviceName"),
)
if mibBuilder.loadTexts:
    systemServicesTableEntry.setStatus("current")
_ServiceName_Type = DisplayString
_ServiceName_Object = MibTableColumn
serviceName = _ServiceName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 11, 1, 23, 1, 1),
    _ServiceName_Type()
)
serviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serviceName.setStatus("current")


class _ServiceStatus_Type(Integer32):
    """Custom type serviceStatus based on Integer32"""
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


_ServiceStatus_Type.__name__ = "Integer32"
_ServiceStatus_Object = MibTableColumn
serviceStatus = _ServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 11, 1, 23, 1, 2),
    _ServiceStatus_Type()
)
serviceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serviceStatus.setStatus("current")
_ServiceAction_Type = RowStatus
_ServiceAction_Object = MibTableColumn
serviceAction = _ServiceAction_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 11, 1, 23, 1, 3),
    _ServiceAction_Type()
)
serviceAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serviceAction.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NPSYSTEM",
    **{"npsystem": npsystem,
       "systemObjects": systemObjects,
       "serialNumber": serialNumber,
       "firmwareVersion": firmwareVersion,
       "systemDate": systemDate,
       "systemTime": systemTime,
       "systemUpTime": systemUpTime,
       "systemReboot": systemReboot,
       "systemHostName": systemHostName,
       "systemDomainName": systemDomainName,
       "systemPrimaryDnsServer": systemPrimaryDnsServer,
       "systemSecondaryDnsServer": systemSecondaryDnsServer,
       "systemGateway": systemGateway,
       "systemRemoteSyslogStatus": systemRemoteSyslogStatus,
       "systemRemoteSyslogServer": systemRemoteSyslogServer,
       "systemSyslogLocalStatus": systemSyslogLocalStatus,
       "systemSyslogMaxSize": systemSyslogMaxSize,
       "systemSyslogRotateNum": systemSyslogRotateNum,
       "systemTimezone": systemTimezone,
       "systemDaylightSavingStatus": systemDaylightSavingStatus,
       "systemNtpServer": systemNtpServer,
       "systemNtpStatus": systemNtpStatus,
       "systemAction": systemAction,
       "systemRemoteSyslogServerPort": systemRemoteSyslogServerPort,
       "systemServicesTable": systemServicesTable,
       "systemServicesTableEntry": systemServicesTableEntry,
       "serviceName": serviceName,
       "serviceStatus": serviceStatus,
       "serviceAction": serviceAction}
)
