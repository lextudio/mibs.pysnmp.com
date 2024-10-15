# SNMP MIB module (HIPATH-WIRELESS-HWC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HIPATH-WIRELESS-HWC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:55:28 2024
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

(hiPathWirelessMgmt,
 hiPathWirelessModules) = mibBuilder.importSymbols(
    "HIPATH-WIRELESS-SMI",
    "hiPathWirelessMgmt",
    "hiPathWirelessModules")

(WEPKeytype,) = mibBuilder.importSymbols(
    "IEEE802dot11-MIB",
    "WEPKeytype")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

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

hiPathWirelessControllerMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 5, 2)
)
hiPathWirelessControllerMib.setRevisions(
        ("2016-04-13 13:55",
         "2016-03-09 16:41",
         "2015-10-06 17:31",
         "2015-06-12 12:05",
         "2015-03-17 10:31",
         "2014-11-28 17:31",
         "2014-06-17 15:29",
         "2014-04-16 14:29",
         "2014-01-27 14:29",
         "2013-11-18 10:29",
         "2013-08-28 11:17",
         "2013-08-01 15:55",
         "2013-07-12 16:50",
         "2013-04-18 15:55",
         "2012-10-18 11:50",
         "2012-09-27 11:10",
         "2012-09-10 14:10",
         "2012-02-13 19:33",
         "2011-08-17 14:18",
         "2011-06-13 13:10",
         "2011-04-29 16:06",
         "2011-01-13 13:25",
         "2010-04-29 17:44",
         "2010-04-08 16:45",
         "2010-02-23 15:17",
         "2009-08-18 12:00",
         "2009-07-23 12:47",
         "2009-04-23 17:14",
         "2009-01-19 13:49",
         "2008-08-13 14:31",
         "2007-11-26 16:15",
         "2007-08-11 16:15",
         "2007-01-15 13:38",
         "2005-10-28 13:12")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class LogEventSeverity(Integer32, TextualConvention):
    status = "current"
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
        *(("critical", 1),
          ("information", 4),
          ("major", 2),
          ("minor", 3),
          ("trace", 5))
    )



class HundredthOfGauge64(Counter64, TextualConvention):
    status = "current"
    displayHint = "d-2"


class HundredthOfGauge32(Gauge32, TextualConvention):
    status = "current"
    displayHint = "d-2"


class HundredthOfInt32(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-2"


# MIB Managed Objects in the order of their OIDs

_HiPathWirelessController_ObjectIdentity = ObjectIdentity
hiPathWirelessController = _HiPathWirelessController_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2)
)
_SystemObjects_ObjectIdentity = ObjectIdentity
systemObjects = _SystemObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 1)
)
_SysSoftwareVersion_Type = DisplayString
_SysSoftwareVersion_Object = MibScalar
sysSoftwareVersion = _SysSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 1, 1),
    _SysSoftwareVersion_Type()
)
sysSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSoftwareVersion.setStatus("current")
_SysLogLevel_Type = LogEventSeverity
_SysLogLevel_Object = MibScalar
sysLogLevel = _SysLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 1, 2),
    _SysLogLevel_Type()
)
sysLogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogLevel.setStatus("current")


class _SysSerialNo_Type(OctetString):
    """Custom type sysSerialNo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SysSerialNo_Type.__name__ = "OctetString"
_SysSerialNo_Object = MibScalar
sysSerialNo = _SysSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 1, 3),
    _SysSerialNo_Type()
)
sysSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSerialNo.setStatus("current")
_SysLogSupport_ObjectIdentity = ObjectIdentity
sysLogSupport = _SysLogSupport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 1, 4)
)


class _HiPathWirelessAppLogFacility_Type(Integer32):
    """Custom type hiPathWirelessAppLogFacility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("local0", 0),
          ("local1", 1),
          ("local2", 2),
          ("local3", 3),
          ("local4", 4),
          ("local5", 5),
          ("local6", 6))
    )


_HiPathWirelessAppLogFacility_Type.__name__ = "Integer32"
_HiPathWirelessAppLogFacility_Object = MibScalar
hiPathWirelessAppLogFacility = _HiPathWirelessAppLogFacility_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 1, 4, 1),
    _HiPathWirelessAppLogFacility_Type()
)
hiPathWirelessAppLogFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hiPathWirelessAppLogFacility.setStatus("current")


class _ServiceLogFacility_Type(Integer32):
    """Custom type serviceLogFacility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("local0", 0),
          ("local1", 1),
          ("local2", 2),
          ("local3", 3),
          ("local4", 4),
          ("local5", 5),
          ("local6", 6))
    )


_ServiceLogFacility_Type.__name__ = "Integer32"
_ServiceLogFacility_Object = MibScalar
serviceLogFacility = _ServiceLogFacility_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 1, 4, 2),
    _ServiceLogFacility_Type()
)
serviceLogFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serviceLogFacility.setStatus("current")
_IncludeAllServiceMessages_Type = TruthValue
_IncludeAllServiceMessages_Object = MibScalar
includeAllServiceMessages = _IncludeAllServiceMessages_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 1, 4, 3),
    _IncludeAllServiceMessages_Type()
)
includeAllServiceMessages.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    includeAllServiceMessages.setStatus("current")
_SysLogServersTable_Object = MibTable
sysLogServersTable = _SysLogServersTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 1, 4, 4)
)
if mibBuilder.loadTexts:
    sysLogServersTable.setStatus("current")
_SysLogServersEntry_Object = MibTableRow
sysLogServersEntry = _SysLogServersEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 1, 4, 4, 1)
)
sysLogServersEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-HWC-MIB", "sysLogServerIndex"),
)
if mibBuilder.loadTexts:
    sysLogServersEntry.setStatus("current")


class _SysLogServerIndex_Type(Integer32):
    """Custom type sysLogServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SysLogServerIndex_Type.__name__ = "Integer32"
_SysLogServerIndex_Object = MibTableColumn
sysLogServerIndex = _SysLogServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 1, 4, 4, 1, 1),
    _SysLogServerIndex_Type()
)
sysLogServerIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogServerIndex.setStatus("current")
_SysLogServerEnabled_Type = TruthValue
_SysLogServerEnabled_Object = MibTableColumn
sysLogServerEnabled = _SysLogServerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 1, 4, 4, 1, 2),
    _SysLogServerEnabled_Type()
)
sysLogServerEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogServerEnabled.setStatus("current")
_SysLogServerIP_Type = IpAddress
_SysLogServerIP_Object = MibTableColumn
sysLogServerIP = _SysLogServerIP_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 1, 4, 4, 1, 3),
    _SysLogServerIP_Type()
)
sysLogServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogServerIP.setStatus("current")
_SysLogServerPort_Type = Integer32
_SysLogServerPort_Object = MibTableColumn
sysLogServerPort = _SysLogServerPort_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 1, 4, 4, 1, 4),
    _SysLogServerPort_Type()
)
sysLogServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogServerPort.setStatus("current")
_SysLogServerRowStatus_Type = RowStatus
_SysLogServerRowStatus_Object = MibTableColumn
sysLogServerRowStatus = _SysLogServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 1, 4, 4, 1, 5),
    _SysLogServerRowStatus_Type()
)
sysLogServerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogServerRowStatus.setStatus("current")
_SysCPUType_Type = DisplayString
_SysCPUType_Object = MibScalar
sysCPUType = _SysCPUType_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 1, 5),
    _SysCPUType_Type()
)
sysCPUType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCPUType.setStatus("current")
_ApLogManagement_ObjectIdentity = ObjectIdentity
apLogManagement = _ApLogManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 1, 6)
)
_ApLogCollectionEnable_Type = TruthValue
_ApLogCollectionEnable_Object = MibScalar
apLogCollectionEnable = _ApLogCollectionEnable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 1, 6, 1),
    _ApLogCollectionEnable_Type()
)
apLogCollectionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLogCollectionEnable.setStatus("current")
_ApLogFrequency_Type = Integer32
_ApLogFrequency_Object = MibScalar
apLogFrequency = _ApLogFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 1, 6, 2),
    _ApLogFrequency_Type()
)
apLogFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLogFrequency.setStatus("current")


class _ApLogDestination_Type(Integer32):
    """Custom type apLogDestination based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flash", 1),
          ("local", 0),
          ("remote", 2))
    )


_ApLogDestination_Type.__name__ = "Integer32"
_ApLogDestination_Object = MibScalar
apLogDestination = _ApLogDestination_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 1, 6, 3),
    _ApLogDestination_Type()
)
apLogDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLogDestination.setStatus("current")


class _ApLogFTProtocol_Type(Integer32):
    """Custom type apLogFTProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 0),
          ("scp", 1))
    )


_ApLogFTProtocol_Type.__name__ = "Integer32"
_ApLogFTProtocol_Object = MibScalar
apLogFTProtocol = _ApLogFTProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 1, 6, 4),
    _ApLogFTProtocol_Type()
)
apLogFTProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLogFTProtocol.setStatus("current")
_ApLogServerIP_Type = IpAddress
_ApLogServerIP_Object = MibScalar
apLogServerIP = _ApLogServerIP_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 1, 6, 5),
    _ApLogServerIP_Type()
)
apLogServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLogServerIP.setStatus("current")
_ApLogUserId_Type = DisplayString
_ApLogUserId_Object = MibScalar
apLogUserId = _ApLogUserId_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 1, 6, 6),
    _ApLogUserId_Type()
)
apLogUserId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLogUserId.setStatus("current")
_ApLogPassword_Type = DisplayString
_ApLogPassword_Object = MibScalar
apLogPassword = _ApLogPassword_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 1, 6, 7),
    _ApLogPassword_Type()
)
apLogPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLogPassword.setStatus("current")
_ApLogDirectory_Type = DisplayString
_ApLogDirectory_Object = MibScalar
apLogDirectory = _ApLogDirectory_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 1, 6, 8),
    _ApLogDirectory_Type()
)
apLogDirectory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLogDirectory.setStatus("current")
_ApLogSelectedAPsTable_Object = MibTable
apLogSelectedAPsTable = _ApLogSelectedAPsTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 1, 6, 9)
)
if mibBuilder.loadTexts:
    apLogSelectedAPsTable.setStatus("current")
_ApLogSelectedAPsEntry_Object = MibTableRow
apLogSelectedAPsEntry = _ApLogSelectedAPsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 1, 6, 9, 1)
)
apLogSelectedAPsEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-HWC-MIB", "apSerialNo"),
)
if mibBuilder.loadTexts:
    apLogSelectedAPsEntry.setStatus("current")


class _ApSerialNo_Type(OctetString):
    """Custom type apSerialNo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_ApSerialNo_Type.__name__ = "OctetString"
_ApSerialNo_Object = MibTableColumn
apSerialNo = _ApSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 1, 6, 9, 1, 1),
    _ApSerialNo_Type()
)
apSerialNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apSerialNo.setStatus("current")
_Select_Type = TruthValue
_Select_Object = MibTableColumn
select = _Select_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 1, 6, 9, 1, 2),
    _Select_Type()
)
select.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    select.setStatus("current")


class _ApLogQuickSelectedOption_Type(Integer32):
    """Custom type apLogQuickSelectedOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("addAll", 1),
          ("addAllForeign", 3),
          ("addAllLocal", 2),
          ("removeAll", 4),
          ("removeAllForeign", 6),
          ("removeAllLocal", 5),
          ("unknown", 0))
    )


_ApLogQuickSelectedOption_Type.__name__ = "Integer32"
_ApLogQuickSelectedOption_Object = MibScalar
apLogQuickSelectedOption = _ApLogQuickSelectedOption_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 1, 6, 10),
    _ApLogQuickSelectedOption_Type()
)
apLogQuickSelectedOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLogQuickSelectedOption.setStatus("current")
_ApLogFileUtility_ObjectIdentity = ObjectIdentity
apLogFileUtility = _ApLogFileUtility_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 1, 7)
)


class _ApLogFileUtilityLimit_Type(Unsigned32):
    """Custom type apLogFileUtilityLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ApLogFileUtilityLimit_Type.__name__ = "Unsigned32"
_ApLogFileUtilityLimit_Object = MibScalar
apLogFileUtilityLimit = _ApLogFileUtilityLimit_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 1, 7, 1),
    _ApLogFileUtilityLimit_Type()
)
apLogFileUtilityLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLogFileUtilityLimit.setStatus("current")
_ApLogFileUtilityCurrent_Type = Gauge32
_ApLogFileUtilityCurrent_Object = MibScalar
apLogFileUtilityCurrent = _ApLogFileUtilityCurrent_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 1, 7, 2),
    _ApLogFileUtilityCurrent_Type()
)
apLogFileUtilityCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLogFileUtilityCurrent.setStatus("current")
_ApLogFileCopyTable_Object = MibTable
apLogFileCopyTable = _ApLogFileCopyTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 1, 7, 5)
)
if mibBuilder.loadTexts:
    apLogFileCopyTable.setStatus("current")
_ApLogFileCopyEntry_Object = MibTableRow
apLogFileCopyEntry = _ApLogFileCopyEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 1, 7, 5, 1)
)
apLogFileCopyEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-HWC-MIB", "apLogFileCopyIndex"),
)
if mibBuilder.loadTexts:
    apLogFileCopyEntry.setStatus("current")


class _ApLogFileCopyIndex_Type(Unsigned32):
    """Custom type apLogFileCopyIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_ApLogFileCopyIndex_Type.__name__ = "Unsigned32"
_ApLogFileCopyIndex_Object = MibTableColumn
apLogFileCopyIndex = _ApLogFileCopyIndex_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 1, 7, 5, 1, 1),
    _ApLogFileCopyIndex_Type()
)
apLogFileCopyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apLogFileCopyIndex.setStatus("current")


class _ApLogFileCopyDestination_Type(Integer32):
    """Custom type apLogFileCopyDestination based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flash", 1),
          ("remoteServer", 2))
    )


_ApLogFileCopyDestination_Type.__name__ = "Integer32"
_ApLogFileCopyDestination_Object = MibTableColumn
apLogFileCopyDestination = _ApLogFileCopyDestination_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 1, 7, 5, 1, 2),
    _ApLogFileCopyDestination_Type()
)
apLogFileCopyDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLogFileCopyDestination.setStatus("current")


class _ApLogFileCopyProtocol_Type(Integer32):
    """Custom type apLogFileCopyProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 0),
          ("scp", 1))
    )


_ApLogFileCopyProtocol_Type.__name__ = "Integer32"
_ApLogFileCopyProtocol_Object = MibTableColumn
apLogFileCopyProtocol = _ApLogFileCopyProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 1, 7, 5, 1, 3),
    _ApLogFileCopyProtocol_Type()
)
apLogFileCopyProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLogFileCopyProtocol.setStatus("current")
_ApLogFileCopyServerIP_Type = IpAddress
_ApLogFileCopyServerIP_Object = MibTableColumn
apLogFileCopyServerIP = _ApLogFileCopyServerIP_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 1, 7, 5, 1, 4),
    _ApLogFileCopyServerIP_Type()
)
apLogFileCopyServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLogFileCopyServerIP.setStatus("current")
_ApLogFileCopyUserID_Type = DisplayString
_ApLogFileCopyUserID_Object = MibTableColumn
apLogFileCopyUserID = _ApLogFileCopyUserID_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 1, 7, 5, 1, 5),
    _ApLogFileCopyUserID_Type()
)
apLogFileCopyUserID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLogFileCopyUserID.setStatus("current")
_ApLogFileCopyPassword_Type = DisplayString
_ApLogFileCopyPassword_Object = MibTableColumn
apLogFileCopyPassword = _ApLogFileCopyPassword_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 1, 7, 5, 1, 6),
    _ApLogFileCopyPassword_Type()
)
apLogFileCopyPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLogFileCopyPassword.setStatus("current")
_ApLogFileCopyServerDirectory_Type = DisplayString
_ApLogFileCopyServerDirectory_Object = MibTableColumn
apLogFileCopyServerDirectory = _ApLogFileCopyServerDirectory_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 1, 7, 5, 1, 7),
    _ApLogFileCopyServerDirectory_Type()
)
apLogFileCopyServerDirectory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLogFileCopyServerDirectory.setStatus("current")


class _ApLogFileCopyOperation_Type(Integer32):
    """Custom type apLogFileCopyOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("start", 1)
    )


_ApLogFileCopyOperation_Type.__name__ = "Integer32"
_ApLogFileCopyOperation_Object = MibTableColumn
apLogFileCopyOperation = _ApLogFileCopyOperation_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 1, 7, 5, 1, 8),
    _ApLogFileCopyOperation_Type()
)
apLogFileCopyOperation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apLogFileCopyOperation.setStatus("current")


class _ApLogFileCopyOperationStatus_Type(Integer32):
    """Custom type apLogFileCopyOperationStatus based on Integer32"""
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
        *(("failure", 5),
          ("inactive", 1),
          ("pending", 2),
          ("running", 3),
          ("success", 4))
    )


_ApLogFileCopyOperationStatus_Type.__name__ = "Integer32"
_ApLogFileCopyOperationStatus_Object = MibTableColumn
apLogFileCopyOperationStatus = _ApLogFileCopyOperationStatus_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 1, 7, 5, 1, 9),
    _ApLogFileCopyOperationStatus_Type()
)
apLogFileCopyOperationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLogFileCopyOperationStatus.setStatus("current")
_ApLogFileCopyRowStatus_Type = RowStatus
_ApLogFileCopyRowStatus_Object = MibTableColumn
apLogFileCopyRowStatus = _ApLogFileCopyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 1, 7, 5, 1, 10),
    _ApLogFileCopyRowStatus_Type()
)
apLogFileCopyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apLogFileCopyRowStatus.setStatus("current")
_DnsObjects_ObjectIdentity = ObjectIdentity
dnsObjects = _DnsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 2)
)
_PrimaryDNS_Type = IpAddress
_PrimaryDNS_Object = MibScalar
primaryDNS = _PrimaryDNS_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 2, 1),
    _PrimaryDNS_Type()
)
primaryDNS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    primaryDNS.setStatus("current")
_SecondaryDNS_Type = IpAddress
_SecondaryDNS_Object = MibScalar
secondaryDNS = _SecondaryDNS_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 2, 2),
    _SecondaryDNS_Type()
)
secondaryDNS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secondaryDNS.setStatus("current")
_TertiaryDNS_Type = IpAddress
_TertiaryDNS_Object = MibScalar
tertiaryDNS = _TertiaryDNS_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 2, 3),
    _TertiaryDNS_Type()
)
tertiaryDNS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tertiaryDNS.setStatus("current")
_MgmtPortObjects_ObjectIdentity = ObjectIdentity
mgmtPortObjects = _MgmtPortObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 3)
)
_MgmtPortIfIndex_Type = Integer32
_MgmtPortIfIndex_Object = MibScalar
mgmtPortIfIndex = _MgmtPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 3, 1),
    _MgmtPortIfIndex_Type()
)
mgmtPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmtPortIfIndex.setStatus("current")
_MgmtPortHostname_Type = DisplayString
_MgmtPortHostname_Object = MibScalar
mgmtPortHostname = _MgmtPortHostname_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 3, 2),
    _MgmtPortHostname_Type()
)
mgmtPortHostname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtPortHostname.setStatus("current")
_MgmtPortDomain_Type = DisplayString
_MgmtPortDomain_Object = MibScalar
mgmtPortDomain = _MgmtPortDomain_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 3, 5),
    _MgmtPortDomain_Type()
)
mgmtPortDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtPortDomain.setStatus("current")
_PhysicalPortObjects_ObjectIdentity = ObjectIdentity
physicalPortObjects = _PhysicalPortObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 4)
)
_PhysicalPortCount_Type = Integer32
_PhysicalPortCount_Object = MibScalar
physicalPortCount = _PhysicalPortCount_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 4, 1),
    _PhysicalPortCount_Type()
)
physicalPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalPortCount.setStatus("current")
_PhysicalPortsTable_Object = MibTable
physicalPortsTable = _PhysicalPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 4, 2)
)
if mibBuilder.loadTexts:
    physicalPortsTable.setStatus("deprecated")
_PhysicalPortsEntry_Object = MibTableRow
physicalPortsEntry = _PhysicalPortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 4, 2, 1)
)
physicalPortsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    physicalPortsEntry.setStatus("deprecated")
_PortMgmtTrafficEnable_Type = TruthValue
_PortMgmtTrafficEnable_Object = MibTableColumn
portMgmtTrafficEnable = _PortMgmtTrafficEnable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 4, 2, 1, 1),
    _PortMgmtTrafficEnable_Type()
)
portMgmtTrafficEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portMgmtTrafficEnable.setStatus("deprecated")


class _PortDuplexMode_Type(Integer32):
    """Custom type portDuplexMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("full", 1),
          ("half", 2))
    )


_PortDuplexMode_Type.__name__ = "Integer32"
_PortDuplexMode_Object = MibTableColumn
portDuplexMode = _PortDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 4, 2, 1, 2),
    _PortDuplexMode_Type()
)
portDuplexMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDuplexMode.setStatus("deprecated")


class _PortFunction_Type(Integer32):
    """Custom type portFunction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("host", 2),
          ("router", 1),
          ("thirdPartyAP", 3))
    )


_PortFunction_Type.__name__ = "Integer32"
_PortFunction_Object = MibTableColumn
portFunction = _PortFunction_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 4, 2, 1, 3),
    _PortFunction_Type()
)
portFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portFunction.setStatus("deprecated")


class _PortEnabled_Type(Integer32):
    """Custom type portEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_PortEnabled_Type.__name__ = "Integer32"
_PortEnabled_Object = MibTableColumn
portEnabled = _PortEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 4, 2, 1, 4),
    _PortEnabled_Type()
)
portEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portEnabled.setStatus("deprecated")
_PortName_Type = OctetString
_PortName_Object = MibTableColumn
portName = _PortName_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 4, 2, 1, 5),
    _PortName_Type()
)
portName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portName.setStatus("deprecated")
_PortIpAddress_Type = IpAddress
_PortIpAddress_Object = MibTableColumn
portIpAddress = _PortIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 4, 2, 1, 6),
    _PortIpAddress_Type()
)
portIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portIpAddress.setStatus("deprecated")
_PortMask_Type = IpAddress
_PortMask_Object = MibTableColumn
portMask = _PortMask_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 4, 2, 1, 7),
    _PortMask_Type()
)
portMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portMask.setStatus("deprecated")
_PortMacAddress_Type = MacAddress
_PortMacAddress_Object = MibTableColumn
portMacAddress = _PortMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 4, 2, 1, 8),
    _PortMacAddress_Type()
)
portMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMacAddress.setStatus("deprecated")


class _PortVlanID_Type(Integer32):
    """Custom type portVlanID based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 4094),
    )


_PortVlanID_Type.__name__ = "Integer32"
_PortVlanID_Object = MibTableColumn
portVlanID = _PortVlanID_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 4, 2, 1, 9),
    _PortVlanID_Type()
)
portVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portVlanID.setStatus("deprecated")
_PortDHCPEnable_Type = TruthValue
_PortDHCPEnable_Object = MibTableColumn
portDHCPEnable = _PortDHCPEnable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 4, 2, 1, 10),
    _PortDHCPEnable_Type()
)
portDHCPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDHCPEnable.setStatus("deprecated")
_PortDHCPGateway_Type = DisplayString
_PortDHCPGateway_Object = MibTableColumn
portDHCPGateway = _PortDHCPGateway_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 4, 2, 1, 11),
    _PortDHCPGateway_Type()
)
portDHCPGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDHCPGateway.setStatus("deprecated")
_PortDHCPDomain_Type = DisplayString
_PortDHCPDomain_Object = MibTableColumn
portDHCPDomain = _PortDHCPDomain_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 4, 2, 1, 12),
    _PortDHCPDomain_Type()
)
portDHCPDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDHCPDomain.setStatus("deprecated")
_PortDHCPDefaultLease_Type = Integer32
_PortDHCPDefaultLease_Object = MibTableColumn
portDHCPDefaultLease = _PortDHCPDefaultLease_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 4, 2, 1, 13),
    _PortDHCPDefaultLease_Type()
)
portDHCPDefaultLease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDHCPDefaultLease.setStatus("deprecated")
_PortDHCPMaxLease_Type = Integer32
_PortDHCPMaxLease_Object = MibTableColumn
portDHCPMaxLease = _PortDHCPMaxLease_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 4, 2, 1, 14),
    _PortDHCPMaxLease_Type()
)
portDHCPMaxLease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDHCPMaxLease.setStatus("deprecated")
_PortDHCPDnsServers_Type = DisplayString
_PortDHCPDnsServers_Object = MibTableColumn
portDHCPDnsServers = _PortDHCPDnsServers_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 4, 2, 1, 15),
    _PortDHCPDnsServers_Type()
)
portDHCPDnsServers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDHCPDnsServers.setStatus("deprecated")
_PortDHCPWins_Type = DisplayString
_PortDHCPWins_Object = MibTableColumn
portDHCPWins = _PortDHCPWins_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 4, 2, 1, 16),
    _PortDHCPWins_Type()
)
portDHCPWins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDHCPWins.setStatus("deprecated")


class _PhysicalPortsInternalVlanID_Type(Integer32):
    """Custom type physicalPortsInternalVlanID based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 4094),
    )


_PhysicalPortsInternalVlanID_Type.__name__ = "Integer32"
_PhysicalPortsInternalVlanID_Object = MibScalar
physicalPortsInternalVlanID = _PhysicalPortsInternalVlanID_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 4, 3),
    _PhysicalPortsInternalVlanID_Type()
)
physicalPortsInternalVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    physicalPortsInternalVlanID.setStatus("current")


class _PhysicalFlash_Type(Integer32):
    """Custom type physicalFlash based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mounted", 1),
          ("unmounted", 2))
    )


_PhysicalFlash_Type.__name__ = "Integer32"
_PhysicalFlash_Object = MibScalar
physicalFlash = _PhysicalFlash_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 4, 4),
    _PhysicalFlash_Type()
)
physicalFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalFlash.setStatus("current")
_PhyDHCPRangeTable_Object = MibTable
phyDHCPRangeTable = _PhyDHCPRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 4, 5)
)
if mibBuilder.loadTexts:
    phyDHCPRangeTable.setStatus("deprecated")
_PhyDHCPRangeEntry_Object = MibTableRow
phyDHCPRangeEntry = _PhyDHCPRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 4, 5, 1)
)
phyDHCPRangeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HIPATH-WIRELESS-HWC-MIB", "phyDHCPRangeIndex"),
)
if mibBuilder.loadTexts:
    phyDHCPRangeEntry.setStatus("deprecated")


class _PhyDHCPRangeIndex_Type(Integer32):
    """Custom type phyDHCPRangeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PhyDHCPRangeIndex_Type.__name__ = "Integer32"
_PhyDHCPRangeIndex_Object = MibTableColumn
phyDHCPRangeIndex = _PhyDHCPRangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 4, 5, 1, 1),
    _PhyDHCPRangeIndex_Type()
)
phyDHCPRangeIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phyDHCPRangeIndex.setStatus("deprecated")
_PhyDHCPRangeStart_Type = IpAddress
_PhyDHCPRangeStart_Object = MibTableColumn
phyDHCPRangeStart = _PhyDHCPRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 4, 5, 1, 2),
    _PhyDHCPRangeStart_Type()
)
phyDHCPRangeStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phyDHCPRangeStart.setStatus("deprecated")
_PhyDHCPRangeEnd_Type = IpAddress
_PhyDHCPRangeEnd_Object = MibTableColumn
phyDHCPRangeEnd = _PhyDHCPRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 4, 5, 1, 3),
    _PhyDHCPRangeEnd_Type()
)
phyDHCPRangeEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phyDHCPRangeEnd.setStatus("deprecated")


class _PhyDHCPRangeType_Type(Integer32):
    """Custom type phyDHCPRangeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exclusion", 2),
          ("inclusion", 1))
    )


_PhyDHCPRangeType_Type.__name__ = "Integer32"
_PhyDHCPRangeType_Object = MibTableColumn
phyDHCPRangeType = _PhyDHCPRangeType_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 4, 5, 1, 4),
    _PhyDHCPRangeType_Type()
)
phyDHCPRangeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phyDHCPRangeType.setStatus("deprecated")
_PhyDHCPRangeStatus_Type = RowStatus
_PhyDHCPRangeStatus_Object = MibTableColumn
phyDHCPRangeStatus = _PhyDHCPRangeStatus_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 4, 5, 1, 5),
    _PhyDHCPRangeStatus_Type()
)
phyDHCPRangeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    phyDHCPRangeStatus.setStatus("deprecated")
_LayerTwoPortTable_Object = MibTable
layerTwoPortTable = _LayerTwoPortTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 4, 6)
)
if mibBuilder.loadTexts:
    layerTwoPortTable.setStatus("current")
_LayerTwoPortEntry_Object = MibTableRow
layerTwoPortEntry = _LayerTwoPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 4, 6, 1)
)
layerTwoPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    layerTwoPortEntry.setStatus("current")


class _LayerTwoPortName_Type(DisplayString):
    """Custom type layerTwoPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_LayerTwoPortName_Type.__name__ = "DisplayString"
_LayerTwoPortName_Object = MibTableColumn
layerTwoPortName = _LayerTwoPortName_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 4, 6, 1, 1),
    _LayerTwoPortName_Type()
)
layerTwoPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layerTwoPortName.setStatus("current")


class _LayerTwoPortMgmtState_Type(Integer32):
    """Custom type layerTwoPortMgmtState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_LayerTwoPortMgmtState_Type.__name__ = "Integer32"
_LayerTwoPortMgmtState_Object = MibTableColumn
layerTwoPortMgmtState = _LayerTwoPortMgmtState_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 4, 6, 1, 2),
    _LayerTwoPortMgmtState_Type()
)
layerTwoPortMgmtState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    layerTwoPortMgmtState.setStatus("current")
_LayerTwoPortMacAddress_Type = MacAddress
_LayerTwoPortMacAddress_Object = MibTableColumn
layerTwoPortMacAddress = _LayerTwoPortMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 4, 6, 1, 3),
    _LayerTwoPortMacAddress_Type()
)
layerTwoPortMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    layerTwoPortMacAddress.setStatus("current")


class _JumboFrames_Type(Integer32):
    """Custom type jumboFrames based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_JumboFrames_Type.__name__ = "Integer32"
_JumboFrames_Object = MibScalar
jumboFrames = _JumboFrames_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 4, 7),
    _JumboFrames_Type()
)
jumboFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jumboFrames.setStatus("current")
_VnManagerObjects_ObjectIdentity = ObjectIdentity
vnManagerObjects = _VnManagerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 5)
)


class _VnRole_Type(Integer32):
    """Custom type vnRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("vnAgent", 3),
          ("vnMgr", 2))
    )


_VnRole_Type.__name__ = "Integer32"
_VnRole_Object = MibScalar
vnRole = _VnRole_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 5, 1),
    _VnRole_Type()
)
vnRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnRole.setStatus("current")
_VnIfIndex_Type = Integer32
_VnIfIndex_Object = MibScalar
vnIfIndex = _VnIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 5, 2),
    _VnIfIndex_Type()
)
vnIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnIfIndex.setStatus("current")
_VnHeartbeatInterval_Type = Integer32
_VnHeartbeatInterval_Object = MibScalar
vnHeartbeatInterval = _VnHeartbeatInterval_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 5, 3),
    _VnHeartbeatInterval_Type()
)
vnHeartbeatInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnHeartbeatInterval.setStatus("current")
_VnLocalClients_Type = Counter32
_VnLocalClients_Object = MibScalar
vnLocalClients = _VnLocalClients_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 5, 4),
    _VnLocalClients_Type()
)
vnLocalClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnLocalClients.setStatus("current")
_VnForeignClients_Type = Counter32
_VnForeignClients_Object = MibScalar
vnForeignClients = _VnForeignClients_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 5, 5),
    _VnForeignClients_Type()
)
vnForeignClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnForeignClients.setStatus("current")
_VnTotalClients_Type = Counter32
_VnTotalClients_Object = MibScalar
vnTotalClients = _VnTotalClients_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 5, 6),
    _VnTotalClients_Type()
)
vnTotalClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnTotalClients.setStatus("current")
_NtpObjects_ObjectIdentity = ObjectIdentity
ntpObjects = _NtpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 6)
)
_NtpEnabled_Type = TruthValue
_NtpEnabled_Object = MibScalar
ntpEnabled = _NtpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 6, 1),
    _NtpEnabled_Type()
)
ntpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpEnabled.setStatus("current")
_NtpTimezone_Type = DisplayString
_NtpTimezone_Object = MibScalar
ntpTimezone = _NtpTimezone_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 6, 2),
    _NtpTimezone_Type()
)
ntpTimezone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpTimezone.setStatus("current")
_NtpTimeServer1_Type = DisplayString
_NtpTimeServer1_Object = MibScalar
ntpTimeServer1 = _NtpTimeServer1_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 6, 3),
    _NtpTimeServer1_Type()
)
ntpTimeServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpTimeServer1.setStatus("current")
_NtpTimeServer2_Type = DisplayString
_NtpTimeServer2_Object = MibScalar
ntpTimeServer2 = _NtpTimeServer2_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 6, 4),
    _NtpTimeServer2_Type()
)
ntpTimeServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpTimeServer2.setStatus("current")
_NtpTimeServer3_Type = DisplayString
_NtpTimeServer3_Object = MibScalar
ntpTimeServer3 = _NtpTimeServer3_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 6, 5),
    _NtpTimeServer3_Type()
)
ntpTimeServer3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpTimeServer3.setStatus("current")
_NtpServerEnabled_Type = TruthValue
_NtpServerEnabled_Object = MibScalar
ntpServerEnabled = _NtpServerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 6, 6),
    _NtpServerEnabled_Type()
)
ntpServerEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpServerEnabled.setStatus("current")
_ControllerStats_ObjectIdentity = ObjectIdentity
controllerStats = _ControllerStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 7)
)
_TunnelsTxRxBytes_Type = Counter64
_TunnelsTxRxBytes_Object = MibScalar
tunnelsTxRxBytes = _TunnelsTxRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 7, 1),
    _TunnelsTxRxBytes_Type()
)
tunnelsTxRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelsTxRxBytes.setStatus("current")
_TunnelCount_Type = Integer32
_TunnelCount_Object = MibScalar
tunnelCount = _TunnelCount_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 7, 6),
    _TunnelCount_Type()
)
tunnelCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelCount.setStatus("current")
_TunnelStatsTable_Object = MibTable
tunnelStatsTable = _TunnelStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 7, 7)
)
if mibBuilder.loadTexts:
    tunnelStatsTable.setStatus("current")
_TunnelStatsEntry_Object = MibTableRow
tunnelStatsEntry = _TunnelStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 7, 7, 1)
)
tunnelStatsEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-HWC-MIB", "tunnelStartIP"),
    (0, "HIPATH-WIRELESS-HWC-MIB", "tunnelEndIP"),
)
if mibBuilder.loadTexts:
    tunnelStatsEntry.setStatus("current")
_TunnelStartIP_Type = IpAddress
_TunnelStartIP_Object = MibTableColumn
tunnelStartIP = _TunnelStartIP_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 7, 7, 1, 1),
    _TunnelStartIP_Type()
)
tunnelStartIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tunnelStartIP.setStatus("current")
_TunnelStartHWC_Type = OctetString
_TunnelStartHWC_Object = MibTableColumn
tunnelStartHWC = _TunnelStartHWC_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 7, 7, 1, 2),
    _TunnelStartHWC_Type()
)
tunnelStartHWC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tunnelStartHWC.setStatus("current")
_TunnelEndIP_Type = IpAddress
_TunnelEndIP_Object = MibTableColumn
tunnelEndIP = _TunnelEndIP_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 7, 7, 1, 3),
    _TunnelEndIP_Type()
)
tunnelEndIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tunnelEndIP.setStatus("current")
_TunnelEndHWC_Type = OctetString
_TunnelEndHWC_Object = MibTableColumn
tunnelEndHWC = _TunnelEndHWC_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 7, 7, 1, 4),
    _TunnelEndHWC_Type()
)
tunnelEndHWC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tunnelEndHWC.setStatus("current")


class _TunnelStatus_Type(Integer32):
    """Custom type tunnelStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connected", 2),
          ("disconnected", 1))
    )


_TunnelStatus_Type.__name__ = "Integer32"
_TunnelStatus_Object = MibTableColumn
tunnelStatus = _TunnelStatus_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 7, 7, 1, 5),
    _TunnelStatus_Type()
)
tunnelStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tunnelStatus.setStatus("current")
_TunnelStatsTxBytes_Type = Counter32
_TunnelStatsTxBytes_Object = MibTableColumn
tunnelStatsTxBytes = _TunnelStatsTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 7, 7, 1, 6),
    _TunnelStatsTxBytes_Type()
)
tunnelStatsTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatsTxBytes.setStatus("current")
_TunnelStatsRxBytes_Type = Counter32
_TunnelStatsRxBytes_Object = MibTableColumn
tunnelStatsRxBytes = _TunnelStatsRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 7, 7, 1, 7),
    _TunnelStatsRxBytes_Type()
)
tunnelStatsRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatsRxBytes.setStatus("current")
_TunnelStatsTxRxBytes_Type = Counter32
_TunnelStatsTxRxBytes_Object = MibTableColumn
tunnelStatsTxRxBytes = _TunnelStatsTxRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 7, 7, 1, 8),
    _TunnelStatsTxRxBytes_Type()
)
tunnelStatsTxRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelStatsTxRxBytes.setStatus("current")


class _ClearAccessRejectMsg_Type(Integer32):
    """Custom type clearAccessRejectMsg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_ClearAccessRejectMsg_Type.__name__ = "Integer32"
_ClearAccessRejectMsg_Object = MibScalar
clearAccessRejectMsg = _ClearAccessRejectMsg_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 7, 8),
    _ClearAccessRejectMsg_Type()
)
clearAccessRejectMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clearAccessRejectMsg.setStatus("current")
_AccessRejectMsgTable_Object = MibTable
accessRejectMsgTable = _AccessRejectMsgTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 7, 9)
)
if mibBuilder.loadTexts:
    accessRejectMsgTable.setStatus("current")
_AccessRejectMsgEntry_Object = MibTableRow
accessRejectMsgEntry = _AccessRejectMsgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 7, 9, 1)
)
accessRejectMsgEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-HWC-MIB", "armIndex"),
)
if mibBuilder.loadTexts:
    accessRejectMsgEntry.setStatus("current")


class _ArmIndex_Type(Integer32):
    """Custom type armIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_ArmIndex_Type.__name__ = "Integer32"
_ArmIndex_Object = MibTableColumn
armIndex = _ArmIndex_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 7, 9, 1, 1),
    _ArmIndex_Type()
)
armIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    armIndex.setStatus("current")
_ArmCount_Type = Counter64
_ArmCount_Object = MibTableColumn
armCount = _ArmCount_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 7, 9, 1, 2),
    _ArmCount_Type()
)
armCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    armCount.setStatus("current")
_ArmReplyMessage_Type = DisplayString
_ArmReplyMessage_Object = MibTableColumn
armReplyMessage = _ArmReplyMessage_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 7, 9, 1, 3),
    _ArmReplyMessage_Type()
)
armReplyMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    armReplyMessage.setStatus("current")
_Availability_ObjectIdentity = ObjectIdentity
availability = _Availability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 8)
)


class _AvailabilityStatus_Type(Integer32):
    """Custom type availabilityStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("paired", 1),
          ("standalone", 0))
    )


_AvailabilityStatus_Type.__name__ = "Integer32"
_AvailabilityStatus_Object = MibScalar
availabilityStatus = _AvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 8, 1),
    _AvailabilityStatus_Type()
)
availabilityStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    availabilityStatus.setStatus("current")
_PairIPAddress_Type = IpAddress
_PairIPAddress_Object = MibScalar
pairIPAddress = _PairIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 8, 2),
    _PairIPAddress_Type()
)
pairIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pairIPAddress.setStatus("current")


class _HwcAvailabilityRank_Type(Integer32):
    """Custom type hwcAvailabilityRank based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notConfigured", 0),
          ("primary", 2),
          ("secondary", 1))
    )


_HwcAvailabilityRank_Type.__name__ = "Integer32"
_HwcAvailabilityRank_Object = MibScalar
hwcAvailabilityRank = _HwcAvailabilityRank_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 8, 3),
    _HwcAvailabilityRank_Type()
)
hwcAvailabilityRank.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwcAvailabilityRank.setStatus("current")


class _FastFailover_Type(Integer32):
    """Custom type fastFailover based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_FastFailover_Type.__name__ = "Integer32"
_FastFailover_Object = MibScalar
fastFailover = _FastFailover_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 8, 4),
    _FastFailover_Type()
)
fastFailover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fastFailover.setStatus("current")


class _DetectLinkFailure_Type(Unsigned32):
    """Custom type detectLinkFailure based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 30),
    )


_DetectLinkFailure_Type.__name__ = "Unsigned32"
_DetectLinkFailure_Object = MibScalar
detectLinkFailure = _DetectLinkFailure_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 8, 5),
    _DetectLinkFailure_Type()
)
detectLinkFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    detectLinkFailure.setStatus("current")
if mibBuilder.loadTexts:
    detectLinkFailure.setUnits("seconds")
_SynchronizeSystemConfig_Type = TruthValue
_SynchronizeSystemConfig_Object = MibScalar
synchronizeSystemConfig = _SynchronizeSystemConfig_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 8, 6),
    _SynchronizeSystemConfig_Type()
)
synchronizeSystemConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    synchronizeSystemConfig.setStatus("current")
_SynchronizeGuestPort_Type = TruthValue
_SynchronizeGuestPort_Object = MibScalar
synchronizeGuestPort = _SynchronizeGuestPort_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 8, 7),
    _SynchronizeGuestPort_Type()
)
synchronizeGuestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    synchronizeGuestPort.setStatus("current")
_SecureConnection_ObjectIdentity = ObjectIdentity
secureConnection = _SecureConnection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 9)
)


class _WeakCipherEnable_Type(Integer32):
    """Custom type weakCipherEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_WeakCipherEnable_Type.__name__ = "Integer32"
_WeakCipherEnable_Object = MibScalar
weakCipherEnable = _WeakCipherEnable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 9, 1),
    _WeakCipherEnable_Type()
)
weakCipherEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    weakCipherEnable.setStatus("current")
_Dashboard_ObjectIdentity = ObjectIdentity
dashboard = _Dashboard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 10)
)
_LicensingInformation_ObjectIdentity = ObjectIdentity
licensingInformation = _LicensingInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 10, 1)
)
_LicenseRegulatoryDomain_Type = DisplayString
_LicenseRegulatoryDomain_Object = MibScalar
licenseRegulatoryDomain = _LicenseRegulatoryDomain_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 10, 1, 1),
    _LicenseRegulatoryDomain_Type()
)
licenseRegulatoryDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseRegulatoryDomain.setStatus("current")


class _LicenseType_Type(Integer32):
    """Custom type licenseType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permanent", 1),
          ("temporary", 2))
    )


_LicenseType_Type.__name__ = "Integer32"
_LicenseType_Object = MibScalar
licenseType = _LicenseType_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 10, 1, 2),
    _LicenseType_Type()
)
licenseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseType.setStatus("current")
_LicenseDaysRemaining_Type = Unsigned32
_LicenseDaysRemaining_Object = MibScalar
licenseDaysRemaining = _LicenseDaysRemaining_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 10, 1, 3),
    _LicenseDaysRemaining_Type()
)
licenseDaysRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseDaysRemaining.setStatus("current")
_LicenseAvailableAP_Type = Unsigned32
_LicenseAvailableAP_Object = MibScalar
licenseAvailableAP = _LicenseAvailableAP_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 10, 1, 4),
    _LicenseAvailableAP_Type()
)
licenseAvailableAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseAvailableAP.setStatus("current")
_LicenseInServiceRadarAP_Type = Unsigned32
_LicenseInServiceRadarAP_Object = MibScalar
licenseInServiceRadarAP = _LicenseInServiceRadarAP_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 10, 1, 5),
    _LicenseInServiceRadarAP_Type()
)
licenseInServiceRadarAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseInServiceRadarAP.setStatus("current")


class _LicenseMode_Type(Integer32):
    """Custom type licenseMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("availabilityPaired", 2),
          ("standAlone", 1))
    )


_LicenseMode_Type.__name__ = "Integer32"
_LicenseMode_Object = MibScalar
licenseMode = _LicenseMode_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 10, 1, 6),
    _LicenseMode_Type()
)
licenseMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseMode.setStatus("current")
_LicenseLocalAP_Type = Unsigned32
_LicenseLocalAP_Object = MibScalar
licenseLocalAP = _LicenseLocalAP_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 10, 1, 7),
    _LicenseLocalAP_Type()
)
licenseLocalAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseLocalAP.setStatus("current")
_LicenseForeignAP_Type = Unsigned32
_LicenseForeignAP_Object = MibScalar
licenseForeignAP = _LicenseForeignAP_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 10, 1, 8),
    _LicenseForeignAP_Type()
)
licenseForeignAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseForeignAP.setStatus("current")
_LicenseLocalRadarAP_Type = Unsigned32
_LicenseLocalRadarAP_Object = MibScalar
licenseLocalRadarAP = _LicenseLocalRadarAP_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 10, 1, 9),
    _LicenseLocalRadarAP_Type()
)
licenseLocalRadarAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseLocalRadarAP.setStatus("current")
_LicenseForeignRadarAP_Type = Unsigned32
_LicenseForeignRadarAP_Object = MibScalar
licenseForeignRadarAP = _LicenseForeignRadarAP_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 10, 1, 10),
    _LicenseForeignRadarAP_Type()
)
licenseForeignRadarAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseForeignRadarAP.setStatus("current")
_StationsByProtocol_ObjectIdentity = ObjectIdentity
stationsByProtocol = _StationsByProtocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 10, 2)
)
_StationsByProtocolA_Type = Unsigned32
_StationsByProtocolA_Object = MibScalar
stationsByProtocolA = _StationsByProtocolA_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 10, 2, 1),
    _StationsByProtocolA_Type()
)
stationsByProtocolA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stationsByProtocolA.setStatus("current")
_StationsByProtocolB_Type = Unsigned32
_StationsByProtocolB_Object = MibScalar
stationsByProtocolB = _StationsByProtocolB_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 10, 2, 2),
    _StationsByProtocolB_Type()
)
stationsByProtocolB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stationsByProtocolB.setStatus("current")
_StationsByProtocolG_Type = Unsigned32
_StationsByProtocolG_Object = MibScalar
stationsByProtocolG = _StationsByProtocolG_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 10, 2, 3),
    _StationsByProtocolG_Type()
)
stationsByProtocolG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stationsByProtocolG.setStatus("current")
_StationsByProtocolN24_Type = Unsigned32
_StationsByProtocolN24_Object = MibScalar
stationsByProtocolN24 = _StationsByProtocolN24_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 10, 2, 4),
    _StationsByProtocolN24_Type()
)
stationsByProtocolN24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stationsByProtocolN24.setStatus("current")
_StationsByProtocolN5_Type = Unsigned32
_StationsByProtocolN5_Object = MibScalar
stationsByProtocolN5 = _StationsByProtocolN5_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 10, 2, 5),
    _StationsByProtocolN5_Type()
)
stationsByProtocolN5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stationsByProtocolN5.setStatus("current")
_StationsByProtocolUnavailable_Type = Unsigned32
_StationsByProtocolUnavailable_Object = MibScalar
stationsByProtocolUnavailable = _StationsByProtocolUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 10, 2, 6),
    _StationsByProtocolUnavailable_Type()
)
stationsByProtocolUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stationsByProtocolUnavailable.setStatus("current")
_StationsByProtocolError_Type = Unsigned32
_StationsByProtocolError_Object = MibScalar
stationsByProtocolError = _StationsByProtocolError_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 10, 2, 7),
    _StationsByProtocolError_Type()
)
stationsByProtocolError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stationsByProtocolError.setStatus("current")
_StationsByProtocolAC_Type = Unsigned32
_StationsByProtocolAC_Object = MibScalar
stationsByProtocolAC = _StationsByProtocolAC_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 10, 2, 8),
    _StationsByProtocolAC_Type()
)
stationsByProtocolAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stationsByProtocolAC.setStatus("current")
_ApByChannelTable_Object = MibTable
apByChannelTable = _ApByChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 10, 3)
)
if mibBuilder.loadTexts:
    apByChannelTable.setStatus("current")
_ApByChannelEntry_Object = MibTableRow
apByChannelEntry = _ApByChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 10, 3, 1)
)
apByChannelEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-HWC-MIB", "apByChannelNumber"),
)
if mibBuilder.loadTexts:
    apByChannelEntry.setStatus("current")
_ApByChannelNumber_Type = Unsigned32
_ApByChannelNumber_Object = MibTableColumn
apByChannelNumber = _ApByChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 10, 3, 1, 1),
    _ApByChannelNumber_Type()
)
apByChannelNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apByChannelNumber.setStatus("current")
_ApByChannelAPs_Type = Unsigned32
_ApByChannelAPs_Object = MibTableColumn
apByChannelAPs = _ApByChannelAPs_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 2, 10, 3, 1, 2),
    _ApByChannelAPs_Type()
)
apByChannelAPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apByChannelAPs.setStatus("current")
_VirtualNetworks_ObjectIdentity = ObjectIdentity
virtualNetworks = _VirtualNetworks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3)
)
_VnsConfigObjects_ObjectIdentity = ObjectIdentity
vnsConfigObjects = _VnsConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1)
)
_VnsCount_Type = Integer32
_VnsCount_Object = MibScalar
vnsCount = _VnsCount_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 1),
    _VnsCount_Type()
)
vnsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnsCount.setStatus("current")
_VnsConfigTable_Object = MibTable
vnsConfigTable = _VnsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 2)
)
if mibBuilder.loadTexts:
    vnsConfigTable.setStatus("current")
_VnsConfigEntry_Object = MibTableRow
vnsConfigEntry = _VnsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 2, 1)
)
vnsConfigEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-HWC-MIB", "vnsIfIndex"),
)
if mibBuilder.loadTexts:
    vnsConfigEntry.setStatus("current")
_VnsDescription_Type = DisplayString
_VnsDescription_Object = MibTableColumn
vnsDescription = _VnsDescription_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 2, 1, 1),
    _VnsDescription_Type()
)
vnsDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsDescription.setStatus("current")


class _VnsAssignmentMode_Type(Integer32):
    """Custom type vnsAssignmentMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aaa", 2),
          ("ssid", 1))
    )


_VnsAssignmentMode_Type.__name__ = "Integer32"
_VnsAssignmentMode_Object = MibTableColumn
vnsAssignmentMode = _VnsAssignmentMode_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 2, 1, 2),
    _VnsAssignmentMode_Type()
)
vnsAssignmentMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsAssignmentMode.setStatus("obsolete")
_VnsMUSessionTimeout_Type = Integer32
_VnsMUSessionTimeout_Object = MibTableColumn
vnsMUSessionTimeout = _VnsMUSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 2, 1, 3),
    _VnsMUSessionTimeout_Type()
)
vnsMUSessionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsMUSessionTimeout.setStatus("current")
_VnsAllowMulticast_Type = TruthValue
_VnsAllowMulticast_Object = MibTableColumn
vnsAllowMulticast = _VnsAllowMulticast_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 2, 1, 4),
    _VnsAllowMulticast_Type()
)
vnsAllowMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsAllowMulticast.setStatus("current")
_VnsSSID_Type = DisplayString
_VnsSSID_Object = MibTableColumn
vnsSSID = _VnsSSID_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 2, 1, 5),
    _VnsSSID_Type()
)
vnsSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsSSID.setStatus("current")
_VnsDomain_Type = DisplayString
_VnsDomain_Object = MibTableColumn
vnsDomain = _VnsDomain_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 2, 1, 6),
    _VnsDomain_Type()
)
vnsDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsDomain.setStatus("current")
_VnsDNSServers_Type = DisplayString
_VnsDNSServers_Object = MibTableColumn
vnsDNSServers = _VnsDNSServers_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 2, 1, 7),
    _VnsDNSServers_Type()
)
vnsDNSServers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsDNSServers.setStatus("current")
_VnsWINSServers_Type = DisplayString
_VnsWINSServers_Object = MibTableColumn
vnsWINSServers = _VnsWINSServers_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 2, 1, 8),
    _VnsWINSServers_Type()
)
vnsWINSServers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsWINSServers.setStatus("current")


class _VnsAuthModel_Type(Integer32):
    """Custom type vnsAuthModel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("captivePortal", 2),
          ("dot1X", 3),
          ("none", 1))
    )


_VnsAuthModel_Type.__name__ = "Integer32"
_VnsAuthModel_Object = MibTableColumn
vnsAuthModel = _VnsAuthModel_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 2, 1, 9),
    _VnsAuthModel_Type()
)
vnsAuthModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsAuthModel.setStatus("current")
_VnsParentIfIndex_Type = Integer32
_VnsParentIfIndex_Object = MibTableColumn
vnsParentIfIndex = _VnsParentIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 2, 1, 10),
    _VnsParentIfIndex_Type()
)
vnsParentIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsParentIfIndex.setStatus("obsolete")
_VnsMgmtTrafficEnable_Type = TruthValue
_VnsMgmtTrafficEnable_Object = MibTableColumn
vnsMgmtTrafficEnable = _VnsMgmtTrafficEnable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 2, 1, 11),
    _VnsMgmtTrafficEnable_Type()
)
vnsMgmtTrafficEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsMgmtTrafficEnable.setStatus("current")


class _VnsUseDHCPRelay_Type(Integer32):
    """Custom type vnsUseDHCPRelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dhcpRelay", 1),
          ("localDhcp", 2),
          ("none", 0))
    )


_VnsUseDHCPRelay_Type.__name__ = "Integer32"
_VnsUseDHCPRelay_Object = MibTableColumn
vnsUseDHCPRelay = _VnsUseDHCPRelay_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 2, 1, 12),
    _VnsUseDHCPRelay_Type()
)
vnsUseDHCPRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsUseDHCPRelay.setStatus("current")
_Vns3rdPartyAP_Type = TruthValue
_Vns3rdPartyAP_Object = MibTableColumn
vns3rdPartyAP = _Vns3rdPartyAP_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 2, 1, 13),
    _Vns3rdPartyAP_Type()
)
vns3rdPartyAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vns3rdPartyAP.setStatus("current")
_VnsStatus_Type = RowStatus
_VnsStatus_Object = MibTableColumn
vnsStatus = _VnsStatus_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 2, 1, 14),
    _VnsStatus_Type()
)
vnsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsStatus.setStatus("current")


class _VnsMode_Type(Integer32):
    """Custom type vnsMode based on Integer32"""
    defaultValue = 1

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
        *(("bridgeAtAP", 3),
          ("bridgeAtController", 2),
          ("routed", 1),
          ("thirdParty", 5),
          ("wds", 4))
    )


_VnsMode_Type.__name__ = "Integer32"
_VnsMode_Object = MibTableColumn
vnsMode = _VnsMode_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 2, 1, 15),
    _VnsMode_Type()
)
vnsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsMode.setStatus("current")


class _VnsVlanID_Type(Integer32):
    """Custom type vnsVlanID based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 4094),
    )


_VnsVlanID_Type.__name__ = "Integer32"
_VnsVlanID_Object = MibTableColumn
vnsVlanID = _VnsVlanID_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 2, 1, 16),
    _VnsVlanID_Type()
)
vnsVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsVlanID.setStatus("current")
_VnsInterfaceName_Type = OctetString
_VnsInterfaceName_Object = MibTableColumn
vnsInterfaceName = _VnsInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 2, 1, 17),
    _VnsInterfaceName_Type()
)
vnsInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsInterfaceName.setStatus("current")
_VnsMgmIpAddress_Type = IpAddress
_VnsMgmIpAddress_Object = MibTableColumn
vnsMgmIpAddress = _VnsMgmIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 2, 1, 18),
    _VnsMgmIpAddress_Type()
)
vnsMgmIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsMgmIpAddress.setStatus("current")
_VnsSuppressSSID_Type = TruthValue
_VnsSuppressSSID_Object = MibTableColumn
vnsSuppressSSID = _VnsSuppressSSID_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 2, 1, 19),
    _VnsSuppressSSID_Type()
)
vnsSuppressSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsSuppressSSID.setStatus("current")
_VnsEnable11hSupport_Type = TruthValue
_VnsEnable11hSupport_Object = MibTableColumn
vnsEnable11hSupport = _VnsEnable11hSupport_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 2, 1, 20),
    _VnsEnable11hSupport_Type()
)
vnsEnable11hSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsEnable11hSupport.setStatus("current")
_VnsApplyPowerBackOff_Type = TruthValue
_VnsApplyPowerBackOff_Object = MibTableColumn
vnsApplyPowerBackOff = _VnsApplyPowerBackOff_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 2, 1, 21),
    _VnsApplyPowerBackOff_Type()
)
vnsApplyPowerBackOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsApplyPowerBackOff.setStatus("current")
_VnsProcessClientIEReq_Type = TruthValue
_VnsProcessClientIEReq_Object = MibTableColumn
vnsProcessClientIEReq = _VnsProcessClientIEReq_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 2, 1, 22),
    _VnsProcessClientIEReq_Type()
)
vnsProcessClientIEReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsProcessClientIEReq.setStatus("current")
_VnsDLSSupportEnable_Type = TruthValue
_VnsDLSSupportEnable_Object = MibTableColumn
vnsDLSSupportEnable = _VnsDLSSupportEnable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 2, 1, 23),
    _VnsDLSSupportEnable_Type()
)
vnsDLSSupportEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsDLSSupportEnable.setStatus("current")
_VnsDLSAddress_Type = DisplayString
_VnsDLSAddress_Object = MibTableColumn
vnsDLSAddress = _VnsDLSAddress_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 2, 1, 24),
    _VnsDLSAddress_Type()
)
vnsDLSAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsDLSAddress.setStatus("current")


class _VnsDLSPort_Type(Integer32):
    """Custom type vnsDLSPort based on Integer32"""
    defaultValue = 18443


_VnsDLSPort_Object = MibTableColumn
vnsDLSPort = _VnsDLSPort_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 2, 1, 25),
    _VnsDLSPort_Type()
)
vnsDLSPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsDLSPort.setStatus("current")
_VnsRateControlProfile_Type = DisplayString
_VnsRateControlProfile_Object = MibTableColumn
vnsRateControlProfile = _VnsRateControlProfile_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 2, 1, 26),
    _VnsRateControlProfile_Type()
)
vnsRateControlProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsRateControlProfile.setStatus("current")
_VnsSessionAvailabilityEnable_Type = TruthValue
_VnsSessionAvailabilityEnable_Object = MibTableColumn
vnsSessionAvailabilityEnable = _VnsSessionAvailabilityEnable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 2, 1, 27),
    _VnsSessionAvailabilityEnable_Type()
)
vnsSessionAvailabilityEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsSessionAvailabilityEnable.setStatus("current")


class _VnsEnabled_Type(Integer32):
    """Custom type vnsEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_VnsEnabled_Type.__name__ = "Integer32"
_VnsEnabled_Object = MibTableColumn
vnsEnabled = _VnsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 2, 1, 28),
    _VnsEnabled_Type()
)
vnsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsEnabled.setStatus("current")


class _VnsStrictSubnetAdherence_Type(Integer32):
    """Custom type vnsStrictSubnetAdherence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_VnsStrictSubnetAdherence_Type.__name__ = "Integer32"
_VnsStrictSubnetAdherence_Object = MibTableColumn
vnsStrictSubnetAdherence = _VnsStrictSubnetAdherence_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 2, 1, 29),
    _VnsStrictSubnetAdherence_Type()
)
vnsStrictSubnetAdherence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsStrictSubnetAdherence.setStatus("current")


class _VnsSLPEnabled_Type(Integer32):
    """Custom type vnsSLPEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_VnsSLPEnabled_Type.__name__ = "Integer32"
_VnsSLPEnabled_Object = MibTableColumn
vnsSLPEnabled = _VnsSLPEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 2, 1, 30),
    _VnsSLPEnabled_Type()
)
vnsSLPEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsSLPEnabled.setStatus("current")
_VnsConfigWLANID_Type = Unsigned32
_VnsConfigWLANID_Object = MibTableColumn
vnsConfigWLANID = _VnsConfigWLANID_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 2, 1, 31),
    _VnsConfigWLANID_Type()
)
vnsConfigWLANID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsConfigWLANID.setStatus("current")
_VnsDHCPRangeTable_Object = MibTable
vnsDHCPRangeTable = _VnsDHCPRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 3)
)
if mibBuilder.loadTexts:
    vnsDHCPRangeTable.setStatus("current")
_VnsDHCPRangeEntry_Object = MibTableRow
vnsDHCPRangeEntry = _VnsDHCPRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 3, 1)
)
vnsDHCPRangeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HIPATH-WIRELESS-HWC-MIB", "vnsDHCPRangeIndex"),
)
if mibBuilder.loadTexts:
    vnsDHCPRangeEntry.setStatus("current")


class _VnsDHCPRangeIndex_Type(Integer32):
    """Custom type vnsDHCPRangeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VnsDHCPRangeIndex_Type.__name__ = "Integer32"
_VnsDHCPRangeIndex_Object = MibTableColumn
vnsDHCPRangeIndex = _VnsDHCPRangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 3, 1, 1),
    _VnsDHCPRangeIndex_Type()
)
vnsDHCPRangeIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsDHCPRangeIndex.setStatus("current")
_VnsDHCPRangeStart_Type = IpAddress
_VnsDHCPRangeStart_Object = MibTableColumn
vnsDHCPRangeStart = _VnsDHCPRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 3, 1, 2),
    _VnsDHCPRangeStart_Type()
)
vnsDHCPRangeStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsDHCPRangeStart.setStatus("current")
_VnsDHCPRangeEnd_Type = IpAddress
_VnsDHCPRangeEnd_Object = MibTableColumn
vnsDHCPRangeEnd = _VnsDHCPRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 3, 1, 3),
    _VnsDHCPRangeEnd_Type()
)
vnsDHCPRangeEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsDHCPRangeEnd.setStatus("current")


class _VnsDHCPRangeType_Type(Integer32):
    """Custom type vnsDHCPRangeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exclusion", 2),
          ("inclusion", 1))
    )


_VnsDHCPRangeType_Type.__name__ = "Integer32"
_VnsDHCPRangeType_Object = MibTableColumn
vnsDHCPRangeType = _VnsDHCPRangeType_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 3, 1, 4),
    _VnsDHCPRangeType_Type()
)
vnsDHCPRangeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsDHCPRangeType.setStatus("current")
_VnsDHCPRangeStatus_Type = RowStatus
_VnsDHCPRangeStatus_Object = MibTableColumn
vnsDHCPRangeStatus = _VnsDHCPRangeStatus_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 3, 1, 5),
    _VnsDHCPRangeStatus_Type()
)
vnsDHCPRangeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsDHCPRangeStatus.setStatus("current")
_VnsCaptivePortalTable_Object = MibTable
vnsCaptivePortalTable = _VnsCaptivePortalTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 4)
)
if mibBuilder.loadTexts:
    vnsCaptivePortalTable.setStatus("current")
_VnsCaptivePortalEntry_Object = MibTableRow
vnsCaptivePortalEntry = _VnsCaptivePortalEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 4, 1)
)
vnsCaptivePortalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    vnsCaptivePortalEntry.setStatus("current")
_CpURL_Type = DisplayString
_CpURL_Object = MibTableColumn
cpURL = _CpURL_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 4, 1, 1),
    _CpURL_Type()
)
cpURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpURL.setStatus("current")
_CpLoginLabel_Type = DisplayString
_CpLoginLabel_Object = MibTableColumn
cpLoginLabel = _CpLoginLabel_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 4, 1, 2),
    _CpLoginLabel_Type()
)
cpLoginLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpLoginLabel.setStatus("deprecated")
_CpPasswordLabel_Type = DisplayString
_CpPasswordLabel_Object = MibTableColumn
cpPasswordLabel = _CpPasswordLabel_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 4, 1, 3),
    _CpPasswordLabel_Type()
)
cpPasswordLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpPasswordLabel.setStatus("deprecated")
_CpHeaderURL_Type = DisplayString
_CpHeaderURL_Object = MibTableColumn
cpHeaderURL = _CpHeaderURL_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 4, 1, 4),
    _CpHeaderURL_Type()
)
cpHeaderURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpHeaderURL.setStatus("deprecated")
_CpFooterURL_Type = DisplayString
_CpFooterURL_Object = MibTableColumn
cpFooterURL = _CpFooterURL_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 4, 1, 5),
    _CpFooterURL_Type()
)
cpFooterURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpFooterURL.setStatus("deprecated")
_CpMessage_Type = DisplayString
_CpMessage_Object = MibTableColumn
cpMessage = _CpMessage_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 4, 1, 6),
    _CpMessage_Type()
)
cpMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpMessage.setStatus("deprecated")
_CpReplaceGatewayWithFQDN_Type = DisplayString
_CpReplaceGatewayWithFQDN_Object = MibTableColumn
cpReplaceGatewayWithFQDN = _CpReplaceGatewayWithFQDN_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 4, 1, 7),
    _CpReplaceGatewayWithFQDN_Type()
)
cpReplaceGatewayWithFQDN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpReplaceGatewayWithFQDN.setStatus("current")
_CpDefaultRedirectionURL_Type = DisplayString
_CpDefaultRedirectionURL_Object = MibTableColumn
cpDefaultRedirectionURL = _CpDefaultRedirectionURL_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 4, 1, 8),
    _CpDefaultRedirectionURL_Type()
)
cpDefaultRedirectionURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpDefaultRedirectionURL.setStatus("current")
_CpConnectionIP_Type = IpAddress
_CpConnectionIP_Object = MibTableColumn
cpConnectionIP = _CpConnectionIP_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 4, 1, 9),
    _CpConnectionIP_Type()
)
cpConnectionIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpConnectionIP.setStatus("current")
_CpConnectionPort_Type = Integer32
_CpConnectionPort_Object = MibTableColumn
cpConnectionPort = _CpConnectionPort_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 4, 1, 10),
    _CpConnectionPort_Type()
)
cpConnectionPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpConnectionPort.setStatus("current")
_CpSharedSecret_Type = OctetString
_CpSharedSecret_Object = MibTableColumn
cpSharedSecret = _CpSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 4, 1, 11),
    _CpSharedSecret_Type()
)
cpSharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpSharedSecret.setStatus("current")


class _CpLogOff_Type(Integer32):
    """Custom type cpLogOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_CpLogOff_Type.__name__ = "Integer32"
_CpLogOff_Object = MibTableColumn
cpLogOff = _CpLogOff_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 4, 1, 12),
    _CpLogOff_Type()
)
cpLogOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpLogOff.setStatus("current")


class _CpStatusCheck_Type(Integer32):
    """Custom type cpStatusCheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_CpStatusCheck_Type.__name__ = "Integer32"
_CpStatusCheck_Object = MibTableColumn
cpStatusCheck = _CpStatusCheck_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 4, 1, 13),
    _CpStatusCheck_Type()
)
cpStatusCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpStatusCheck.setStatus("current")


class _CpType_Type(Integer32):
    """Custom type cpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("external", 4),
          ("guestPortal", 5),
          ("internal", 2),
          ("none", 1))
    )


_CpType_Type.__name__ = "Integer32"
_CpType_Object = MibTableColumn
cpType = _CpType_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 4, 1, 14),
    _CpType_Type()
)
cpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpType.setStatus("current")
_VnsRadiusServerTable_Object = MibTable
vnsRadiusServerTable = _VnsRadiusServerTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 5)
)
if mibBuilder.loadTexts:
    vnsRadiusServerTable.setStatus("current")
_VnsRadiusServerEntry_Object = MibTableRow
vnsRadiusServerEntry = _VnsRadiusServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 5, 1)
)
vnsRadiusServerEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HIPATH-WIRELESS-HWC-MIB", "vnsRadiusServerName"),
)
if mibBuilder.loadTexts:
    vnsRadiusServerEntry.setStatus("current")


class _VnsRadiusServerName_Type(DisplayString):
    """Custom type vnsRadiusServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_VnsRadiusServerName_Type.__name__ = "DisplayString"
_VnsRadiusServerName_Object = MibTableColumn
vnsRadiusServerName = _VnsRadiusServerName_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 5, 1, 1),
    _VnsRadiusServerName_Type()
)
vnsRadiusServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsRadiusServerName.setStatus("current")
_VnsRadiusServerPort_Type = Integer32
_VnsRadiusServerPort_Object = MibTableColumn
vnsRadiusServerPort = _VnsRadiusServerPort_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 5, 1, 2),
    _VnsRadiusServerPort_Type()
)
vnsRadiusServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsRadiusServerPort.setStatus("current")
_VnsRadiusServerRetries_Type = Integer32
_VnsRadiusServerRetries_Object = MibTableColumn
vnsRadiusServerRetries = _VnsRadiusServerRetries_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 5, 1, 3),
    _VnsRadiusServerRetries_Type()
)
vnsRadiusServerRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsRadiusServerRetries.setStatus("current")
_VnsRadiusServerTimeout_Type = Integer32
_VnsRadiusServerTimeout_Object = MibTableColumn
vnsRadiusServerTimeout = _VnsRadiusServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 5, 1, 4),
    _VnsRadiusServerTimeout_Type()
)
vnsRadiusServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsRadiusServerTimeout.setStatus("current")
_VnsRadiusServerSharedSecret_Type = DisplayString
_VnsRadiusServerSharedSecret_Object = MibTableColumn
vnsRadiusServerSharedSecret = _VnsRadiusServerSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 5, 1, 5),
    _VnsRadiusServerSharedSecret_Type()
)
vnsRadiusServerSharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsRadiusServerSharedSecret.setStatus("current")
_VnsRadiusServerNASIdentifier_Type = DisplayString
_VnsRadiusServerNASIdentifier_Object = MibTableColumn
vnsRadiusServerNASIdentifier = _VnsRadiusServerNASIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 5, 1, 6),
    _VnsRadiusServerNASIdentifier_Type()
)
vnsRadiusServerNASIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsRadiusServerNASIdentifier.setStatus("current")


class _VnsRadiusServerAuthType_Type(Integer32):
    """Custom type vnsRadiusServerAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("chap", 1),
          ("msChap", 2),
          ("msChapV2", 3),
          ("notApplicable", 4),
          ("pap", 0))
    )


_VnsRadiusServerAuthType_Type.__name__ = "Integer32"
_VnsRadiusServerAuthType_Object = MibTableColumn
vnsRadiusServerAuthType = _VnsRadiusServerAuthType_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 5, 1, 7),
    _VnsRadiusServerAuthType_Type()
)
vnsRadiusServerAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsRadiusServerAuthType.setStatus("current")
_VnsRadiusServerRowStatus_Type = RowStatus
_VnsRadiusServerRowStatus_Object = MibTableColumn
vnsRadiusServerRowStatus = _VnsRadiusServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 5, 1, 8),
    _VnsRadiusServerRowStatus_Type()
)
vnsRadiusServerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsRadiusServerRowStatus.setStatus("current")
_VnsRadiusServerNasAddress_Type = IpAddress
_VnsRadiusServerNasAddress_Object = MibTableColumn
vnsRadiusServerNasAddress = _VnsRadiusServerNasAddress_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 5, 1, 9),
    _VnsRadiusServerNasAddress_Type()
)
vnsRadiusServerNasAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsRadiusServerNasAddress.setStatus("current")
_VnsFilterIDTable_Object = MibTable
vnsFilterIDTable = _VnsFilterIDTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 6)
)
if mibBuilder.loadTexts:
    vnsFilterIDTable.setStatus("current")
_VnsFilterIDEntry_Object = MibTableRow
vnsFilterIDEntry = _VnsFilterIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 6, 1)
)
vnsFilterIDEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HIPATH-WIRELESS-HWC-MIB", "vnsFilterID"),
)
if mibBuilder.loadTexts:
    vnsFilterIDEntry.setStatus("current")
_VnsFilterID_Type = DisplayString
_VnsFilterID_Object = MibTableColumn
vnsFilterID = _VnsFilterID_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 6, 1, 1),
    _VnsFilterID_Type()
)
vnsFilterID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsFilterID.setStatus("current")
_VnsFilterIDStatus_Type = RowStatus
_VnsFilterIDStatus_Object = MibTableColumn
vnsFilterIDStatus = _VnsFilterIDStatus_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 6, 1, 2),
    _VnsFilterIDStatus_Type()
)
vnsFilterIDStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsFilterIDStatus.setStatus("current")
_VnsFilterRuleTable_Object = MibTable
vnsFilterRuleTable = _VnsFilterRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 7)
)
if mibBuilder.loadTexts:
    vnsFilterRuleTable.setStatus("current")
_VnsFilterRuleEntry_Object = MibTableRow
vnsFilterRuleEntry = _VnsFilterRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 7, 1)
)
vnsFilterRuleEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HIPATH-WIRELESS-HWC-MIB", "vnsFilterID"),
    (0, "HIPATH-WIRELESS-HWC-MIB", "vnsFilterRuleOrder"),
)
if mibBuilder.loadTexts:
    vnsFilterRuleEntry.setStatus("current")


class _VnsFilterRuleOrder_Type(Integer32):
    """Custom type vnsFilterRuleOrder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65532),
    )


_VnsFilterRuleOrder_Type.__name__ = "Integer32"
_VnsFilterRuleOrder_Object = MibTableColumn
vnsFilterRuleOrder = _VnsFilterRuleOrder_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 7, 1, 1),
    _VnsFilterRuleOrder_Type()
)
vnsFilterRuleOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsFilterRuleOrder.setStatus("current")


class _VnsFilterRuleDirection_Type(Integer32):
    """Custom type vnsFilterRuleDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("in", 1),
          ("none", 0),
          ("out", 2))
    )


_VnsFilterRuleDirection_Type.__name__ = "Integer32"
_VnsFilterRuleDirection_Object = MibTableColumn
vnsFilterRuleDirection = _VnsFilterRuleDirection_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 7, 1, 2),
    _VnsFilterRuleDirection_Type()
)
vnsFilterRuleDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsFilterRuleDirection.setStatus("current")


class _VnsFilterRuleAction_Type(Integer32):
    """Custom type vnsFilterRuleAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("disallow", 2))
    )


_VnsFilterRuleAction_Type.__name__ = "Integer32"
_VnsFilterRuleAction_Object = MibTableColumn
vnsFilterRuleAction = _VnsFilterRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 7, 1, 3),
    _VnsFilterRuleAction_Type()
)
vnsFilterRuleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsFilterRuleAction.setStatus("current")
_VnsFilterRuleIPAddress_Type = IpAddress
_VnsFilterRuleIPAddress_Object = MibTableColumn
vnsFilterRuleIPAddress = _VnsFilterRuleIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 7, 1, 4),
    _VnsFilterRuleIPAddress_Type()
)
vnsFilterRuleIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsFilterRuleIPAddress.setStatus("current")
_VnsFilterRulePortLow_Type = Integer32
_VnsFilterRulePortLow_Object = MibTableColumn
vnsFilterRulePortLow = _VnsFilterRulePortLow_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 7, 1, 5),
    _VnsFilterRulePortLow_Type()
)
vnsFilterRulePortLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsFilterRulePortLow.setStatus("current")
_VnsFilterRulePortHigh_Type = Integer32
_VnsFilterRulePortHigh_Object = MibTableColumn
vnsFilterRulePortHigh = _VnsFilterRulePortHigh_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 7, 1, 6),
    _VnsFilterRulePortHigh_Type()
)
vnsFilterRulePortHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsFilterRulePortHigh.setStatus("current")


class _VnsFilterRuleProtocol_Type(Integer32):
    """Custom type vnsFilterRuleProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("icmp", 4),
          ("ipsecAH", 6),
          ("ipsecESP", 5),
          ("none", 0),
          ("notApplicable", 1),
          ("tcp", 2),
          ("udp", 3))
    )


_VnsFilterRuleProtocol_Type.__name__ = "Integer32"
_VnsFilterRuleProtocol_Object = MibTableColumn
vnsFilterRuleProtocol = _VnsFilterRuleProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 7, 1, 7),
    _VnsFilterRuleProtocol_Type()
)
vnsFilterRuleProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsFilterRuleProtocol.setStatus("current")


class _VnsFilterRuleEtherType_Type(Integer32):
    """Custom type vnsFilterRuleEtherType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("arp", 2),
          ("ip", 1),
          ("none", 0),
          ("rarp", 3))
    )


_VnsFilterRuleEtherType_Type.__name__ = "Integer32"
_VnsFilterRuleEtherType_Object = MibTableColumn
vnsFilterRuleEtherType = _VnsFilterRuleEtherType_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 7, 1, 8),
    _VnsFilterRuleEtherType_Type()
)
vnsFilterRuleEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsFilterRuleEtherType.setStatus("current")
_VnsFilterRuleStatus_Type = RowStatus
_VnsFilterRuleStatus_Object = MibTableColumn
vnsFilterRuleStatus = _VnsFilterRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 7, 1, 9),
    _VnsFilterRuleStatus_Type()
)
vnsFilterRuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsFilterRuleStatus.setStatus("current")
_VnsPrivacyTable_Object = MibTable
vnsPrivacyTable = _VnsPrivacyTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 8)
)
if mibBuilder.loadTexts:
    vnsPrivacyTable.setStatus("current")
_VnsPrivacyEntry_Object = MibTableRow
vnsPrivacyEntry = _VnsPrivacyEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 8, 1)
)
vnsPrivacyEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    vnsPrivacyEntry.setStatus("current")


class _VnsPrivWEPKeyType_Type(Integer32):
    """Custom type vnsPrivWEPKeyType based on Integer32"""
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
        *(("dynamic", 4),
          ("none", 1),
          ("wepstatic", 2),
          ("wpa", 5),
          ("wpapsk", 3))
    )


_VnsPrivWEPKeyType_Type.__name__ = "Integer32"
_VnsPrivWEPKeyType_Object = MibTableColumn
vnsPrivWEPKeyType = _VnsPrivWEPKeyType_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 8, 1, 1),
    _VnsPrivWEPKeyType_Type()
)
vnsPrivWEPKeyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsPrivWEPKeyType.setStatus("current")
_VnsPrivDynamicRekeyFrequency_Type = Integer32
_VnsPrivDynamicRekeyFrequency_Object = MibTableColumn
vnsPrivDynamicRekeyFrequency = _VnsPrivDynamicRekeyFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 8, 1, 2),
    _VnsPrivDynamicRekeyFrequency_Type()
)
vnsPrivDynamicRekeyFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsPrivDynamicRekeyFrequency.setStatus("current")
_VnsPrivWEPKeyLength_Type = Integer32
_VnsPrivWEPKeyLength_Object = MibTableColumn
vnsPrivWEPKeyLength = _VnsPrivWEPKeyLength_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 8, 1, 3),
    _VnsPrivWEPKeyLength_Type()
)
vnsPrivWEPKeyLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsPrivWEPKeyLength.setStatus("current")
_VnsPrivWPA1Enabled_Type = TruthValue
_VnsPrivWPA1Enabled_Object = MibTableColumn
vnsPrivWPA1Enabled = _VnsPrivWPA1Enabled_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 8, 1, 4),
    _VnsPrivWPA1Enabled_Type()
)
vnsPrivWPA1Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsPrivWPA1Enabled.setStatus("current")
_VnsPrivUseSharedKey_Type = TruthValue
_VnsPrivUseSharedKey_Object = MibTableColumn
vnsPrivUseSharedKey = _VnsPrivUseSharedKey_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 8, 1, 5),
    _VnsPrivUseSharedKey_Type()
)
vnsPrivUseSharedKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsPrivUseSharedKey.setStatus("current")
_VnsPrivWPASharedKey_Type = DisplayString
_VnsPrivWPASharedKey_Object = MibTableColumn
vnsPrivWPASharedKey = _VnsPrivWPASharedKey_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 8, 1, 6),
    _VnsPrivWPASharedKey_Type()
)
vnsPrivWPASharedKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsPrivWPASharedKey.setStatus("current")
_VnsPrivWPA2Enabled_Type = TruthValue
_VnsPrivWPA2Enabled_Object = MibTableColumn
vnsPrivWPA2Enabled = _VnsPrivWPA2Enabled_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 8, 1, 7),
    _VnsPrivWPA2Enabled_Type()
)
vnsPrivWPA2Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsPrivWPA2Enabled.setStatus("current")
_VnsWEPKeyTable_Object = MibTable
vnsWEPKeyTable = _VnsWEPKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 9)
)
if mibBuilder.loadTexts:
    vnsWEPKeyTable.setStatus("current")
_VnsWEPKeyEntry_Object = MibTableRow
vnsWEPKeyEntry = _VnsWEPKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 9, 1)
)
vnsWEPKeyEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HIPATH-WIRELESS-HWC-MIB", "vnsWEPKeyIndex"),
)
if mibBuilder.loadTexts:
    vnsWEPKeyEntry.setStatus("current")


class _VnsWEPKeyIndex_Type(Integer32):
    """Custom type vnsWEPKeyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_VnsWEPKeyIndex_Type.__name__ = "Integer32"
_VnsWEPKeyIndex_Object = MibTableColumn
vnsWEPKeyIndex = _VnsWEPKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 9, 1, 1),
    _VnsWEPKeyIndex_Type()
)
vnsWEPKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsWEPKeyIndex.setStatus("current")
_VnsWEPKeyValue_Type = WEPKeytype
_VnsWEPKeyValue_Object = MibTableColumn
vnsWEPKeyValue = _VnsWEPKeyValue_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 9, 1, 2),
    _VnsWEPKeyValue_Type()
)
vnsWEPKeyValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsWEPKeyValue.setStatus("current")
_Vns3rdPartyAPTable_Object = MibTable
vns3rdPartyAPTable = _Vns3rdPartyAPTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 10)
)
if mibBuilder.loadTexts:
    vns3rdPartyAPTable.setStatus("current")
_Vns3rdPartyAPEntry_Object = MibTableRow
vns3rdPartyAPEntry = _Vns3rdPartyAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 10, 1)
)
vns3rdPartyAPEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HIPATH-WIRELESS-HWC-MIB", "apMacAddress"),
)
if mibBuilder.loadTexts:
    vns3rdPartyAPEntry.setStatus("current")
_ApMacAddress_Type = MacAddress
_ApMacAddress_Object = MibTableColumn
apMacAddress = _ApMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 10, 1, 1),
    _ApMacAddress_Type()
)
apMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apMacAddress.setStatus("current")
_ApIpAddress_Type = IpAddress
_ApIpAddress_Object = MibTableColumn
apIpAddress = _ApIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 10, 1, 2),
    _ApIpAddress_Type()
)
apIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpAddress.setStatus("current")
_VnsQoSTable_Object = MibTable
vnsQoSTable = _VnsQoSTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 11)
)
if mibBuilder.loadTexts:
    vnsQoSTable.setStatus("current")
_VnsQoSEntry_Object = MibTableRow
vnsQoSEntry = _VnsQoSEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 11, 1)
)
vnsQoSEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-HWC-MIB", "vnsIfIndex"),
)
if mibBuilder.loadTexts:
    vnsQoSEntry.setStatus("current")


class _VnsQoSWirelessLegacyFlag_Type(Integer32):
    """Custom type vnsQoSWirelessLegacyFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_VnsQoSWirelessLegacyFlag_Type.__name__ = "Integer32"
_VnsQoSWirelessLegacyFlag_Object = MibTableColumn
vnsQoSWirelessLegacyFlag = _VnsQoSWirelessLegacyFlag_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 11, 1, 1),
    _VnsQoSWirelessLegacyFlag_Type()
)
vnsQoSWirelessLegacyFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsQoSWirelessLegacyFlag.setStatus("current")


class _VnsQoSWirelessWMMFlag_Type(Integer32):
    """Custom type vnsQoSWirelessWMMFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_VnsQoSWirelessWMMFlag_Type.__name__ = "Integer32"
_VnsQoSWirelessWMMFlag_Object = MibTableColumn
vnsQoSWirelessWMMFlag = _VnsQoSWirelessWMMFlag_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 11, 1, 2),
    _VnsQoSWirelessWMMFlag_Type()
)
vnsQoSWirelessWMMFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsQoSWirelessWMMFlag.setStatus("current")


class _VnsQoSWireless80211eFlag_Type(Integer32):
    """Custom type vnsQoSWireless80211eFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_VnsQoSWireless80211eFlag_Type.__name__ = "Integer32"
_VnsQoSWireless80211eFlag_Object = MibTableColumn
vnsQoSWireless80211eFlag = _VnsQoSWireless80211eFlag_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 11, 1, 3),
    _VnsQoSWireless80211eFlag_Type()
)
vnsQoSWireless80211eFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsQoSWireless80211eFlag.setStatus("current")


class _VnsQoSWirelessTurboVoiceFlag_Type(Integer32):
    """Custom type vnsQoSWirelessTurboVoiceFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_VnsQoSWirelessTurboVoiceFlag_Type.__name__ = "Integer32"
_VnsQoSWirelessTurboVoiceFlag_Object = MibTableColumn
vnsQoSWirelessTurboVoiceFlag = _VnsQoSWirelessTurboVoiceFlag_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 11, 1, 4),
    _VnsQoSWirelessTurboVoiceFlag_Type()
)
vnsQoSWirelessTurboVoiceFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsQoSWirelessTurboVoiceFlag.setStatus("current")


class _VnsQoSPriorityOverrideFlag_Type(Integer32):
    """Custom type vnsQoSPriorityOverrideFlag based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_VnsQoSPriorityOverrideFlag_Type.__name__ = "Integer32"
_VnsQoSPriorityOverrideFlag_Object = MibTableColumn
vnsQoSPriorityOverrideFlag = _VnsQoSPriorityOverrideFlag_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 11, 1, 5),
    _VnsQoSPriorityOverrideFlag_Type()
)
vnsQoSPriorityOverrideFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsQoSPriorityOverrideFlag.setStatus("current")


class _VnsQoSPriorityOverrideSC_Type(Integer32):
    """Custom type vnsQoSPriorityOverrideSC based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("background", 0),
          ("bestEffort", 1),
          ("bronze", 2),
          ("gold", 4),
          ("networkControl", 7),
          ("platinum", 5),
          ("premiumVoice", 6),
          ("silver", 3))
    )


_VnsQoSPriorityOverrideSC_Type.__name__ = "Integer32"
_VnsQoSPriorityOverrideSC_Object = MibTableColumn
vnsQoSPriorityOverrideSC = _VnsQoSPriorityOverrideSC_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 11, 1, 6),
    _VnsQoSPriorityOverrideSC_Type()
)
vnsQoSPriorityOverrideSC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsQoSPriorityOverrideSC.setStatus("current")


class _VnsQoSPriorityOverrideDSCP_Type(Integer32):
    """Custom type vnsQoSPriorityOverrideDSCP based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_VnsQoSPriorityOverrideDSCP_Type.__name__ = "Integer32"
_VnsQoSPriorityOverrideDSCP_Object = MibTableColumn
vnsQoSPriorityOverrideDSCP = _VnsQoSPriorityOverrideDSCP_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 11, 1, 7),
    _VnsQoSPriorityOverrideDSCP_Type()
)
vnsQoSPriorityOverrideDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsQoSPriorityOverrideDSCP.setStatus("current")


class _VnsQoSClassificationServiceClass_Type(OctetString):
    """Custom type vnsQoSClassificationServiceClass based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_VnsQoSClassificationServiceClass_Type.__name__ = "OctetString"
_VnsQoSClassificationServiceClass_Object = MibTableColumn
vnsQoSClassificationServiceClass = _VnsQoSClassificationServiceClass_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 11, 1, 8),
    _VnsQoSClassificationServiceClass_Type()
)
vnsQoSClassificationServiceClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsQoSClassificationServiceClass.setStatus("current")


class _VnsQoSWirelessEnableUAPSD_Type(Integer32):
    """Custom type vnsQoSWirelessEnableUAPSD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_VnsQoSWirelessEnableUAPSD_Type.__name__ = "Integer32"
_VnsQoSWirelessEnableUAPSD_Object = MibTableColumn
vnsQoSWirelessEnableUAPSD = _VnsQoSWirelessEnableUAPSD_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 11, 1, 9),
    _VnsQoSWirelessEnableUAPSD_Type()
)
vnsQoSWirelessEnableUAPSD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsQoSWirelessEnableUAPSD.setStatus("current")


class _VnsQoSWirelessUseAdmControlVoice_Type(Integer32):
    """Custom type vnsQoSWirelessUseAdmControlVoice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_VnsQoSWirelessUseAdmControlVoice_Type.__name__ = "Integer32"
_VnsQoSWirelessUseAdmControlVoice_Object = MibTableColumn
vnsQoSWirelessUseAdmControlVoice = _VnsQoSWirelessUseAdmControlVoice_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 11, 1, 10),
    _VnsQoSWirelessUseAdmControlVoice_Type()
)
vnsQoSWirelessUseAdmControlVoice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsQoSWirelessUseAdmControlVoice.setStatus("current")


class _VnsQoSWirelessUseAdmControlVideo_Type(Integer32):
    """Custom type vnsQoSWirelessUseAdmControlVideo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_VnsQoSWirelessUseAdmControlVideo_Type.__name__ = "Integer32"
_VnsQoSWirelessUseAdmControlVideo_Object = MibTableColumn
vnsQoSWirelessUseAdmControlVideo = _VnsQoSWirelessUseAdmControlVideo_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 11, 1, 11),
    _VnsQoSWirelessUseAdmControlVideo_Type()
)
vnsQoSWirelessUseAdmControlVideo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsQoSWirelessUseAdmControlVideo.setStatus("current")


class _VnsQoSWirelessULPolicerAction_Type(Integer32):
    """Custom type vnsQoSWirelessULPolicerAction based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("doNothing", 0),
          ("sendDELTStoClient", 1))
    )


_VnsQoSWirelessULPolicerAction_Type.__name__ = "Integer32"
_VnsQoSWirelessULPolicerAction_Object = MibTableColumn
vnsQoSWirelessULPolicerAction = _VnsQoSWirelessULPolicerAction_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 11, 1, 12),
    _VnsQoSWirelessULPolicerAction_Type()
)
vnsQoSWirelessULPolicerAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsQoSWirelessULPolicerAction.setStatus("current")


class _VnsQoSWirelessDLPolicerAction_Type(Integer32):
    """Custom type vnsQoSWirelessDLPolicerAction based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doNothing", 0),
          ("downgrade", 1),
          ("drop", 2))
    )


_VnsQoSWirelessDLPolicerAction_Type.__name__ = "Integer32"
_VnsQoSWirelessDLPolicerAction_Object = MibTableColumn
vnsQoSWirelessDLPolicerAction = _VnsQoSWirelessDLPolicerAction_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 11, 1, 13),
    _VnsQoSWirelessDLPolicerAction_Type()
)
vnsQoSWirelessDLPolicerAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsQoSWirelessDLPolicerAction.setStatus("current")


class _VnsQoSWirelessUseAdmControlBestEffort_Type(Integer32):
    """Custom type vnsQoSWirelessUseAdmControlBestEffort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_VnsQoSWirelessUseAdmControlBestEffort_Type.__name__ = "Integer32"
_VnsQoSWirelessUseAdmControlBestEffort_Object = MibTableColumn
vnsQoSWirelessUseAdmControlBestEffort = _VnsQoSWirelessUseAdmControlBestEffort_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 11, 1, 14),
    _VnsQoSWirelessUseAdmControlBestEffort_Type()
)
vnsQoSWirelessUseAdmControlBestEffort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsQoSWirelessUseAdmControlBestEffort.setStatus("current")


class _VnsQoSWirelessUseAdmControlBackground_Type(Integer32):
    """Custom type vnsQoSWirelessUseAdmControlBackground based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_VnsQoSWirelessUseAdmControlBackground_Type.__name__ = "Integer32"
_VnsQoSWirelessUseAdmControlBackground_Object = MibTableColumn
vnsQoSWirelessUseAdmControlBackground = _VnsQoSWirelessUseAdmControlBackground_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 11, 1, 15),
    _VnsQoSWirelessUseAdmControlBackground_Type()
)
vnsQoSWirelessUseAdmControlBackground.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsQoSWirelessUseAdmControlBackground.setStatus("current")
_VnsWDSRFTable_Object = MibTable
vnsWDSRFTable = _VnsWDSRFTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 12)
)
if mibBuilder.loadTexts:
    vnsWDSRFTable.setStatus("obsolete")
_VnsWDSRFEntry_Object = MibTableRow
vnsWDSRFEntry = _VnsWDSRFEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 12, 1)
)
vnsWDSRFEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-HWC-MIB", "vnsIfIndex"),
    (0, "HIPATH-WIRELESS-HWC-MIB", "apIndex"),
)
if mibBuilder.loadTexts:
    vnsWDSRFEntry.setStatus("obsolete")
_VnsWDSRFAPName_Type = DisplayString
_VnsWDSRFAPName_Object = MibTableColumn
vnsWDSRFAPName = _VnsWDSRFAPName_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 12, 1, 1),
    _VnsWDSRFAPName_Type()
)
vnsWDSRFAPName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsWDSRFAPName.setStatus("obsolete")


class _VnsWDSRFbgService_Type(Integer32):
    """Custom type vnsWDSRFbgService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("both", 4),
          ("child", 2),
          ("none", 1),
          ("notAvailable", 0),
          ("parent", 3))
    )


_VnsWDSRFbgService_Type.__name__ = "Integer32"
_VnsWDSRFbgService_Object = MibTableColumn
vnsWDSRFbgService = _VnsWDSRFbgService_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 12, 1, 2),
    _VnsWDSRFbgService_Type()
)
vnsWDSRFbgService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsWDSRFbgService.setStatus("obsolete")


class _VnsWDSRFaService_Type(Integer32):
    """Custom type vnsWDSRFaService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("both", 4),
          ("child", 2),
          ("none", 1),
          ("notAvailable", 0),
          ("parent", 3))
    )


_VnsWDSRFaService_Type.__name__ = "Integer32"
_VnsWDSRFaService_Object = MibTableColumn
vnsWDSRFaService = _VnsWDSRFaService_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 12, 1, 3),
    _VnsWDSRFaService_Type()
)
vnsWDSRFaService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsWDSRFaService.setStatus("obsolete")
_VnsWDSRFPreferredParent_Type = DisplayString
_VnsWDSRFPreferredParent_Object = MibTableColumn
vnsWDSRFPreferredParent = _VnsWDSRFPreferredParent_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 12, 1, 4),
    _VnsWDSRFPreferredParent_Type()
)
vnsWDSRFPreferredParent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsWDSRFPreferredParent.setStatus("obsolete")
_VnsWDSRFBackupParent_Type = DisplayString
_VnsWDSRFBackupParent_Object = MibTableColumn
vnsWDSRFBackupParent = _VnsWDSRFBackupParent_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 12, 1, 5),
    _VnsWDSRFBackupParent_Type()
)
vnsWDSRFBackupParent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsWDSRFBackupParent.setStatus("obsolete")


class _VnsWDSRFBridge_Type(Integer32):
    """Custom type vnsWDSRFBridge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bridged", 1),
          ("notBridged", 2))
    )


_VnsWDSRFBridge_Type.__name__ = "Integer32"
_VnsWDSRFBridge_Object = MibTableColumn
vnsWDSRFBridge = _VnsWDSRFBridge_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 12, 1, 6),
    _VnsWDSRFBridge_Type()
)
vnsWDSRFBridge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsWDSRFBridge.setStatus("obsolete")
_VnsRateControlProfTable_Object = MibTable
vnsRateControlProfTable = _VnsRateControlProfTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 13)
)
if mibBuilder.loadTexts:
    vnsRateControlProfTable.setStatus("obsolete")
_VnsRateControlProfEntry_Object = MibTableRow
vnsRateControlProfEntry = _VnsRateControlProfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 13, 1)
)
vnsRateControlProfEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-HWC-MIB", "vnsRateControlProfInd"),
)
if mibBuilder.loadTexts:
    vnsRateControlProfEntry.setStatus("obsolete")
_VnsRateControlProfInd_Type = Unsigned32
_VnsRateControlProfInd_Object = MibTableColumn
vnsRateControlProfInd = _VnsRateControlProfInd_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 13, 1, 1),
    _VnsRateControlProfInd_Type()
)
vnsRateControlProfInd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsRateControlProfInd.setStatus("obsolete")
_VnsRateControlProfName_Type = DisplayString
_VnsRateControlProfName_Object = MibTableColumn
vnsRateControlProfName = _VnsRateControlProfName_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 13, 1, 2),
    _VnsRateControlProfName_Type()
)
vnsRateControlProfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsRateControlProfName.setStatus("obsolete")
_VnsRateControlCIR_Type = Unsigned32
_VnsRateControlCIR_Object = MibTableColumn
vnsRateControlCIR = _VnsRateControlCIR_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 13, 1, 3),
    _VnsRateControlCIR_Type()
)
vnsRateControlCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsRateControlCIR.setStatus("obsolete")
_VnsRateControlCBS_Type = Unsigned32
_VnsRateControlCBS_Object = MibTableColumn
vnsRateControlCBS = _VnsRateControlCBS_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 13, 1, 4),
    _VnsRateControlCBS_Type()
)
vnsRateControlCBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsRateControlCBS.setStatus("obsolete")
_VnsAPFilterTable_Object = MibTable
vnsAPFilterTable = _VnsAPFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 14)
)
if mibBuilder.loadTexts:
    vnsAPFilterTable.setStatus("current")
_VnsAPFilterEntry_Object = MibTableRow
vnsAPFilterEntry = _VnsAPFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 14, 1)
)
vnsAPFilterEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HIPATH-WIRELESS-HWC-MIB", "vnsFilterID"),
    (0, "HIPATH-WIRELESS-HWC-MIB", "vnsAPFilterRuleOrder"),
)
if mibBuilder.loadTexts:
    vnsAPFilterEntry.setStatus("current")


class _VnsAPFilterRuleOrder_Type(Integer32):
    """Custom type vnsAPFilterRuleOrder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VnsAPFilterRuleOrder_Type.__name__ = "Integer32"
_VnsAPFilterRuleOrder_Object = MibTableColumn
vnsAPFilterRuleOrder = _VnsAPFilterRuleOrder_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 14, 1, 1),
    _VnsAPFilterRuleOrder_Type()
)
vnsAPFilterRuleOrder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vnsAPFilterRuleOrder.setStatus("current")


class _VnsAPFilterRuleDirection_Type(Integer32):
    """Custom type vnsAPFilterRuleDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("in", 1),
          ("out", 2))
    )


_VnsAPFilterRuleDirection_Type.__name__ = "Integer32"
_VnsAPFilterRuleDirection_Object = MibTableColumn
vnsAPFilterRuleDirection = _VnsAPFilterRuleDirection_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 14, 1, 2),
    _VnsAPFilterRuleDirection_Type()
)
vnsAPFilterRuleDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vnsAPFilterRuleDirection.setStatus("current")
_VnsAPFilterAction_Type = Integer32
_VnsAPFilterAction_Object = MibTableColumn
vnsAPFilterAction = _VnsAPFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 14, 1, 3),
    _VnsAPFilterAction_Type()
)
vnsAPFilterAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vnsAPFilterAction.setStatus("current")
_VnsAPFilterIPAddress_Type = IpAddress
_VnsAPFilterIPAddress_Object = MibTableColumn
vnsAPFilterIPAddress = _VnsAPFilterIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 14, 1, 4),
    _VnsAPFilterIPAddress_Type()
)
vnsAPFilterIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vnsAPFilterIPAddress.setStatus("current")
_VnsAPFilterMask_Type = IpAddress
_VnsAPFilterMask_Object = MibTableColumn
vnsAPFilterMask = _VnsAPFilterMask_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 14, 1, 5),
    _VnsAPFilterMask_Type()
)
vnsAPFilterMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vnsAPFilterMask.setStatus("current")
_VnsAPFilterPortLow_Type = Integer32
_VnsAPFilterPortLow_Object = MibTableColumn
vnsAPFilterPortLow = _VnsAPFilterPortLow_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 14, 1, 6),
    _VnsAPFilterPortLow_Type()
)
vnsAPFilterPortLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vnsAPFilterPortLow.setStatus("current")
_VnsAPFilterPortHigh_Type = Integer32
_VnsAPFilterPortHigh_Object = MibTableColumn
vnsAPFilterPortHigh = _VnsAPFilterPortHigh_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 14, 1, 7),
    _VnsAPFilterPortHigh_Type()
)
vnsAPFilterPortHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vnsAPFilterPortHigh.setStatus("current")
_VnsAPFilterProtocol_Type = Integer32
_VnsAPFilterProtocol_Object = MibTableColumn
vnsAPFilterProtocol = _VnsAPFilterProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 14, 1, 8),
    _VnsAPFilterProtocol_Type()
)
vnsAPFilterProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vnsAPFilterProtocol.setStatus("current")


class _VnsAPFilterEtherType_Type(Integer32):
    """Custom type vnsAPFilterEtherType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("arp", 2),
          ("ip", 1),
          ("rarp", 3))
    )


_VnsAPFilterEtherType_Type.__name__ = "Integer32"
_VnsAPFilterEtherType_Object = MibTableColumn
vnsAPFilterEtherType = _VnsAPFilterEtherType_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 14, 1, 9),
    _VnsAPFilterEtherType_Type()
)
vnsAPFilterEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vnsAPFilterEtherType.setStatus("current")
_VnsAPFilterRowStatus_Type = Integer32
_VnsAPFilterRowStatus_Object = MibTableColumn
vnsAPFilterRowStatus = _VnsAPFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 1, 14, 1, 10),
    _VnsAPFilterRowStatus_Type()
)
vnsAPFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vnsAPFilterRowStatus.setStatus("current")
_VnsStatsObjects_ObjectIdentity = ObjectIdentity
vnsStatsObjects = _VnsStatsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 2)
)
_ActiveVNSSessionCount_Type = Integer32
_ActiveVNSSessionCount_Object = MibScalar
activeVNSSessionCount = _ActiveVNSSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 2, 1),
    _ActiveVNSSessionCount_Type()
)
activeVNSSessionCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    activeVNSSessionCount.setStatus("current")
_VnsStatTable_Object = MibTable
vnsStatTable = _VnsStatTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 2, 2)
)
if mibBuilder.loadTexts:
    vnsStatTable.setStatus("obsolete")
_VnsStatEntry_Object = MibTableRow
vnsStatEntry = _VnsStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 2, 2, 1)
)
vnsStatEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-HWC-MIB", "vnsIfIndex"),
)
if mibBuilder.loadTexts:
    vnsStatEntry.setStatus("obsolete")
_VnsStatName_Type = OctetString
_VnsStatName_Object = MibTableColumn
vnsStatName = _VnsStatName_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 2, 2, 1, 1),
    _VnsStatName_Type()
)
vnsStatName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsStatName.setStatus("obsolete")
_VnsStatTxPkts_Type = Counter64
_VnsStatTxPkts_Object = MibTableColumn
vnsStatTxPkts = _VnsStatTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 2, 2, 1, 2),
    _VnsStatTxPkts_Type()
)
vnsStatTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnsStatTxPkts.setStatus("obsolete")
_VnsStatRxPkts_Type = Counter64
_VnsStatRxPkts_Object = MibTableColumn
vnsStatRxPkts = _VnsStatRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 2, 2, 1, 3),
    _VnsStatRxPkts_Type()
)
vnsStatRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnsStatRxPkts.setStatus("obsolete")
_VnsStatTxOctects_Type = Counter64
_VnsStatTxOctects_Object = MibTableColumn
vnsStatTxOctects = _VnsStatTxOctects_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 2, 2, 1, 4),
    _VnsStatTxOctects_Type()
)
vnsStatTxOctects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnsStatTxOctects.setStatus("obsolete")
_VnsStatRxOctects_Type = Counter64
_VnsStatRxOctects_Object = MibTableColumn
vnsStatRxOctects = _VnsStatRxOctects_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 2, 2, 1, 5),
    _VnsStatRxOctects_Type()
)
vnsStatRxOctects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnsStatRxOctects.setStatus("obsolete")
_VnsStatMulticastTxPkts_Type = Counter64
_VnsStatMulticastTxPkts_Object = MibTableColumn
vnsStatMulticastTxPkts = _VnsStatMulticastTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 2, 2, 1, 6),
    _VnsStatMulticastTxPkts_Type()
)
vnsStatMulticastTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnsStatMulticastTxPkts.setStatus("obsolete")
_VnsStatMulticastRxPkts_Type = Counter64
_VnsStatMulticastRxPkts_Object = MibTableColumn
vnsStatMulticastRxPkts = _VnsStatMulticastRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 2, 2, 1, 7),
    _VnsStatMulticastRxPkts_Type()
)
vnsStatMulticastRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnsStatMulticastRxPkts.setStatus("obsolete")
_VnsStatBroadcastTxPkts_Type = Counter64
_VnsStatBroadcastTxPkts_Object = MibTableColumn
vnsStatBroadcastTxPkts = _VnsStatBroadcastTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 2, 2, 1, 8),
    _VnsStatBroadcastTxPkts_Type()
)
vnsStatBroadcastTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnsStatBroadcastTxPkts.setStatus("obsolete")
_VnsStatBroadcastRxPkts_Type = Counter64
_VnsStatBroadcastRxPkts_Object = MibTableColumn
vnsStatBroadcastRxPkts = _VnsStatBroadcastRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 2, 2, 1, 9),
    _VnsStatBroadcastRxPkts_Type()
)
vnsStatBroadcastRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnsStatBroadcastRxPkts.setStatus("obsolete")
_VnsStatRadiusTotRequests_Type = Counter64
_VnsStatRadiusTotRequests_Object = MibTableColumn
vnsStatRadiusTotRequests = _VnsStatRadiusTotRequests_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 2, 2, 1, 10),
    _VnsStatRadiusTotRequests_Type()
)
vnsStatRadiusTotRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnsStatRadiusTotRequests.setStatus("obsolete")
_VnsStatRadiusReqFailed_Type = Counter64
_VnsStatRadiusReqFailed_Object = MibTableColumn
vnsStatRadiusReqFailed = _VnsStatRadiusReqFailed_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 2, 2, 1, 11),
    _VnsStatRadiusReqFailed_Type()
)
vnsStatRadiusReqFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnsStatRadiusReqFailed.setStatus("obsolete")
_VnsStatRadiusReqRejected_Type = Counter64
_VnsStatRadiusReqRejected_Object = MibTableColumn
vnsStatRadiusReqRejected = _VnsStatRadiusReqRejected_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 2, 2, 1, 12),
    _VnsStatRadiusReqRejected_Type()
)
vnsStatRadiusReqRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnsStatRadiusReqRejected.setStatus("obsolete")
_VnsExceptionStatTable_Object = MibTable
vnsExceptionStatTable = _VnsExceptionStatTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 2, 3)
)
if mibBuilder.loadTexts:
    vnsExceptionStatTable.setStatus("obsolete")
_VnsExceptionStatEntry_Object = MibTableRow
vnsExceptionStatEntry = _VnsExceptionStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 2, 3, 1)
)
vnsExceptionStatEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-HWC-MIB", "vnsIfIndex"),
    (0, "HIPATH-WIRELESS-HWC-MIB", "vnsExceptionFiterName"),
)
if mibBuilder.loadTexts:
    vnsExceptionStatEntry.setStatus("obsolete")


class _VnsExceptionFiterName_Type(OctetString):
    """Custom type vnsExceptionFiterName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_VnsExceptionFiterName_Type.__name__ = "OctetString"
_VnsExceptionFiterName_Object = MibTableColumn
vnsExceptionFiterName = _VnsExceptionFiterName_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 2, 3, 1, 1),
    _VnsExceptionFiterName_Type()
)
vnsExceptionFiterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsExceptionFiterName.setStatus("obsolete")
_VnsExceptionStatPktsDenied_Type = Counter64
_VnsExceptionStatPktsDenied_Object = MibTableColumn
vnsExceptionStatPktsDenied = _VnsExceptionStatPktsDenied_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 2, 3, 1, 2),
    _VnsExceptionStatPktsDenied_Type()
)
vnsExceptionStatPktsDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnsExceptionStatPktsDenied.setStatus("obsolete")
_VnsExceptionStatPktsAllowed_Type = Counter64
_VnsExceptionStatPktsAllowed_Object = MibTableColumn
vnsExceptionStatPktsAllowed = _VnsExceptionStatPktsAllowed_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 2, 3, 1, 3),
    _VnsExceptionStatPktsAllowed_Type()
)
vnsExceptionStatPktsAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnsExceptionStatPktsAllowed.setStatus("obsolete")
_VnsWDSStatTable_Object = MibTable
vnsWDSStatTable = _VnsWDSStatTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 2, 4)
)
if mibBuilder.loadTexts:
    vnsWDSStatTable.setStatus("obsolete")
_VnsWDSStatEntry_Object = MibTableRow
vnsWDSStatEntry = _VnsWDSStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 2, 4, 1)
)
vnsWDSStatEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-HWC-MIB", "vnsIfIndex"),
    (0, "HIPATH-WIRELESS-HWC-MIB", "apIndex"),
)
if mibBuilder.loadTexts:
    vnsWDSStatEntry.setStatus("obsolete")
_VnsWDSStatAPName_Type = DisplayString
_VnsWDSStatAPName_Object = MibTableColumn
vnsWDSStatAPName = _VnsWDSStatAPName_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 2, 4, 1, 1),
    _VnsWDSStatAPName_Type()
)
vnsWDSStatAPName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsWDSStatAPName.setStatus("obsolete")


class _VnsWDSStatAPRole_Type(Integer32):
    """Custom type vnsWDSStatAPRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("repeater", 3),
          ("root", 2),
          ("satellite", 1),
          ("unknown", -1))
    )


_VnsWDSStatAPRole_Type.__name__ = "Integer32"
_VnsWDSStatAPRole_Object = MibTableColumn
vnsWDSStatAPRole = _VnsWDSStatAPRole_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 2, 4, 1, 2),
    _VnsWDSStatAPRole_Type()
)
vnsWDSStatAPRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsWDSStatAPRole.setStatus("obsolete")


class _VnsWDSStatAPRadio_Type(DisplayString):
    """Custom type vnsWDSStatAPRadio based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_VnsWDSStatAPRadio_Type.__name__ = "DisplayString"
_VnsWDSStatAPRadio_Object = MibTableColumn
vnsWDSStatAPRadio = _VnsWDSStatAPRadio_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 2, 4, 1, 3),
    _VnsWDSStatAPRadio_Type()
)
vnsWDSStatAPRadio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsWDSStatAPRadio.setStatus("obsolete")
_VnsWDSStatAPParent_Type = DisplayString
_VnsWDSStatAPParent_Object = MibTableColumn
vnsWDSStatAPParent = _VnsWDSStatAPParent_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 2, 4, 1, 4),
    _VnsWDSStatAPParent_Type()
)
vnsWDSStatAPParent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsWDSStatAPParent.setStatus("obsolete")


class _VnsWDSStatSSID_Type(DisplayString):
    """Custom type vnsWDSStatSSID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VnsWDSStatSSID_Type.__name__ = "DisplayString"
_VnsWDSStatSSID_Object = MibTableColumn
vnsWDSStatSSID = _VnsWDSStatSSID_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 2, 4, 1, 5),
    _VnsWDSStatSSID_Type()
)
vnsWDSStatSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsWDSStatSSID.setStatus("obsolete")
_VnsWDSStatRxFrame_Type = Counter64
_VnsWDSStatRxFrame_Object = MibTableColumn
vnsWDSStatRxFrame = _VnsWDSStatRxFrame_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 2, 4, 1, 6),
    _VnsWDSStatRxFrame_Type()
)
vnsWDSStatRxFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsWDSStatRxFrame.setStatus("obsolete")
_VnsWDSStatTxFrame_Type = Counter64
_VnsWDSStatTxFrame_Object = MibTableColumn
vnsWDSStatTxFrame = _VnsWDSStatTxFrame_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 2, 4, 1, 7),
    _VnsWDSStatTxFrame_Type()
)
vnsWDSStatTxFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsWDSStatTxFrame.setStatus("obsolete")
_VnsWDSStatRxError_Type = Counter64
_VnsWDSStatRxError_Object = MibTableColumn
vnsWDSStatRxError = _VnsWDSStatRxError_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 2, 4, 1, 8),
    _VnsWDSStatRxError_Type()
)
vnsWDSStatRxError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsWDSStatRxError.setStatus("obsolete")
_VnsWDSStatTxError_Type = Counter64
_VnsWDSStatTxError_Object = MibTableColumn
vnsWDSStatTxError = _VnsWDSStatTxError_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 2, 4, 1, 9),
    _VnsWDSStatTxError_Type()
)
vnsWDSStatTxError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsWDSStatTxError.setStatus("obsolete")


class _VnsWDSStatRxRSSI_Type(Integer32):
    """Custom type vnsWDSStatRxRSSI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_VnsWDSStatRxRSSI_Type.__name__ = "Integer32"
_VnsWDSStatRxRSSI_Object = MibTableColumn
vnsWDSStatRxRSSI = _VnsWDSStatRxRSSI_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 2, 4, 1, 10),
    _VnsWDSStatRxRSSI_Type()
)
vnsWDSStatRxRSSI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsWDSStatRxRSSI.setStatus("obsolete")
_VnsWDSStatRxRate_Type = Counter64
_VnsWDSStatRxRate_Object = MibTableColumn
vnsWDSStatRxRate = _VnsWDSStatRxRate_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 2, 4, 1, 11),
    _VnsWDSStatRxRate_Type()
)
vnsWDSStatRxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsWDSStatRxRate.setStatus("obsolete")
_VnsWDSStatTxRate_Type = Counter64
_VnsWDSStatTxRate_Object = MibTableColumn
vnsWDSStatTxRate = _VnsWDSStatTxRate_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 2, 4, 1, 12),
    _VnsWDSStatTxRate_Type()
)
vnsWDSStatTxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsWDSStatTxRate.setStatus("obsolete")
_VnsGlobalSetting_ObjectIdentity = ObjectIdentity
vnsGlobalSetting = _VnsGlobalSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 3)
)
_WirelessQoS_ObjectIdentity = ObjectIdentity
wirelessQoS = _WirelessQoS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 3, 1)
)


class _MaxVoiceBWforReassociation_Type(Integer32):
    """Custom type maxVoiceBWforReassociation based on Integer32"""
    defaultValue = 80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MaxVoiceBWforReassociation_Type.__name__ = "Integer32"
_MaxVoiceBWforReassociation_Object = MibScalar
maxVoiceBWforReassociation = _MaxVoiceBWforReassociation_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 3, 1, 1),
    _MaxVoiceBWforReassociation_Type()
)
maxVoiceBWforReassociation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxVoiceBWforReassociation.setStatus("current")


class _MaxVoiceBWforAssociation_Type(Integer32):
    """Custom type maxVoiceBWforAssociation based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MaxVoiceBWforAssociation_Type.__name__ = "Integer32"
_MaxVoiceBWforAssociation_Object = MibScalar
maxVoiceBWforAssociation = _MaxVoiceBWforAssociation_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 3, 1, 2),
    _MaxVoiceBWforAssociation_Type()
)
maxVoiceBWforAssociation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxVoiceBWforAssociation.setStatus("current")


class _MaxVideoBWforReassociation_Type(Integer32):
    """Custom type maxVideoBWforReassociation based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MaxVideoBWforReassociation_Type.__name__ = "Integer32"
_MaxVideoBWforReassociation_Object = MibScalar
maxVideoBWforReassociation = _MaxVideoBWforReassociation_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 3, 1, 3),
    _MaxVideoBWforReassociation_Type()
)
maxVideoBWforReassociation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxVideoBWforReassociation.setStatus("current")


class _MaxVideoBWforAssociation_Type(Integer32):
    """Custom type maxVideoBWforAssociation based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MaxVideoBWforAssociation_Type.__name__ = "Integer32"
_MaxVideoBWforAssociation_Object = MibScalar
maxVideoBWforAssociation = _MaxVideoBWforAssociation_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 3, 1, 4),
    _MaxVideoBWforAssociation_Type()
)
maxVideoBWforAssociation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxVideoBWforAssociation.setStatus("current")


class _MaxBestEffortBWforReassociation_Type(Integer32):
    """Custom type maxBestEffortBWforReassociation based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MaxBestEffortBWforReassociation_Type.__name__ = "Integer32"
_MaxBestEffortBWforReassociation_Object = MibScalar
maxBestEffortBWforReassociation = _MaxBestEffortBWforReassociation_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 3, 1, 5),
    _MaxBestEffortBWforReassociation_Type()
)
maxBestEffortBWforReassociation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxBestEffortBWforReassociation.setStatus("current")


class _MaxBestEffortBWforAssociation_Type(Integer32):
    """Custom type maxBestEffortBWforAssociation based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MaxBestEffortBWforAssociation_Type.__name__ = "Integer32"
_MaxBestEffortBWforAssociation_Object = MibScalar
maxBestEffortBWforAssociation = _MaxBestEffortBWforAssociation_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 3, 1, 6),
    _MaxBestEffortBWforAssociation_Type()
)
maxBestEffortBWforAssociation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxBestEffortBWforAssociation.setStatus("current")


class _MaxBackgroundBWforReassociation_Type(Integer32):
    """Custom type maxBackgroundBWforReassociation based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MaxBackgroundBWforReassociation_Type.__name__ = "Integer32"
_MaxBackgroundBWforReassociation_Object = MibScalar
maxBackgroundBWforReassociation = _MaxBackgroundBWforReassociation_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 3, 1, 7),
    _MaxBackgroundBWforReassociation_Type()
)
maxBackgroundBWforReassociation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxBackgroundBWforReassociation.setStatus("current")


class _MaxBackgroundBWforAssociation_Type(Integer32):
    """Custom type maxBackgroundBWforAssociation based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MaxBackgroundBWforAssociation_Type.__name__ = "Integer32"
_MaxBackgroundBWforAssociation_Object = MibScalar
maxBackgroundBWforAssociation = _MaxBackgroundBWforAssociation_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 3, 1, 8),
    _MaxBackgroundBWforAssociation_Type()
)
maxBackgroundBWforAssociation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxBackgroundBWforAssociation.setStatus("current")
_RadiusInfo_ObjectIdentity = ObjectIdentity
radiusInfo = _RadiusInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 3, 2)
)
_ExternalRadiusServerTable_Object = MibTable
externalRadiusServerTable = _ExternalRadiusServerTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 3, 2, 2)
)
if mibBuilder.loadTexts:
    externalRadiusServerTable.setStatus("obsolete")
_ExternalRadiusServerEntry_Object = MibTableRow
externalRadiusServerEntry = _ExternalRadiusServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 3, 2, 2, 1)
)
externalRadiusServerEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-HWC-MIB", "externalRadiusServerName"),
)
if mibBuilder.loadTexts:
    externalRadiusServerEntry.setStatus("obsolete")
_ExternalRadiusServerName_Type = DisplayString
_ExternalRadiusServerName_Object = MibTableColumn
externalRadiusServerName = _ExternalRadiusServerName_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 3, 2, 2, 1, 1),
    _ExternalRadiusServerName_Type()
)
externalRadiusServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalRadiusServerName.setStatus("obsolete")
_ExternalRadiusServerAddress_Type = DisplayString
_ExternalRadiusServerAddress_Object = MibTableColumn
externalRadiusServerAddress = _ExternalRadiusServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 3, 2, 2, 1, 2),
    _ExternalRadiusServerAddress_Type()
)
externalRadiusServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalRadiusServerAddress.setStatus("obsolete")


class _ExternalRadiusServerSharedSecret_Type(OctetString):
    """Custom type externalRadiusServerSharedSecret based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ExternalRadiusServerSharedSecret_Type.__name__ = "OctetString"
_ExternalRadiusServerSharedSecret_Object = MibTableColumn
externalRadiusServerSharedSecret = _ExternalRadiusServerSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 3, 2, 2, 1, 3),
    _ExternalRadiusServerSharedSecret_Type()
)
externalRadiusServerSharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalRadiusServerSharedSecret.setStatus("obsolete")
_ExternalRadiusServerRowStatus_Type = RowStatus
_ExternalRadiusServerRowStatus_Object = MibTableColumn
externalRadiusServerRowStatus = _ExternalRadiusServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 3, 2, 2, 1, 4),
    _ExternalRadiusServerRowStatus_Type()
)
externalRadiusServerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalRadiusServerRowStatus.setStatus("obsolete")
_DasInfo_ObjectIdentity = ObjectIdentity
dasInfo = _DasInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 3, 3)
)


class _DasPort_Type(Integer32):
    """Custom type dasPort based on Integer32"""
    defaultValue = 3799

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_DasPort_Type.__name__ = "Integer32"
_DasPort_Object = MibScalar
dasPort = _DasPort_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 3, 3, 1),
    _DasPort_Type()
)
dasPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dasPort.setStatus("current")


class _DasReplayInterval_Type(Integer32):
    """Custom type dasReplayInterval based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_DasReplayInterval_Type.__name__ = "Integer32"
_DasReplayInterval_Object = MibScalar
dasReplayInterval = _DasReplayInterval_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 3, 3, 2),
    _DasReplayInterval_Type()
)
dasReplayInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dasReplayInterval.setStatus("current")
if mibBuilder.loadTexts:
    dasReplayInterval.setUnits("seconds")


class _AdvancedFilteringMode_Type(Integer32):
    """Custom type advancedFilteringMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AdvancedFilteringMode_Type.__name__ = "Integer32"
_AdvancedFilteringMode_Object = MibScalar
advancedFilteringMode = _AdvancedFilteringMode_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 3, 4),
    _AdvancedFilteringMode_Type()
)
advancedFilteringMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    advancedFilteringMode.setStatus("current")


class _RadiusStrictMode_Type(Integer32):
    """Custom type radiusStrictMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("strictModeDisabled", 0),
          ("strictModeEnabled", 1))
    )


_RadiusStrictMode_Type.__name__ = "Integer32"
_RadiusStrictMode_Object = MibScalar
radiusStrictMode = _RadiusStrictMode_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 3, 5),
    _RadiusStrictMode_Type()
)
radiusStrictMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusStrictMode.setStatus("current")
_RadiusFastFailoverEvents_ObjectIdentity = ObjectIdentity
radiusFastFailoverEvents = _RadiusFastFailoverEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 3, 6)
)
_RadiusFastFailoverEventsTable_Object = MibTable
radiusFastFailoverEventsTable = _RadiusFastFailoverEventsTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 3, 6, 1)
)
if mibBuilder.loadTexts:
    radiusFastFailoverEventsTable.setStatus("current")
_RadiusFastFailoverEventsEntry_Object = MibTableRow
radiusFastFailoverEventsEntry = _RadiusFastFailoverEventsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 3, 6, 1, 1)
)
radiusFastFailoverEventsEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-HWC-MIB", "radiusFFOEid"),
)
if mibBuilder.loadTexts:
    radiusFastFailoverEventsEntry.setStatus("current")


class _RadiusFFOEid_Type(DisplayString):
    """Custom type radiusFFOEid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RadiusFFOEid_Type.__name__ = "DisplayString"
_RadiusFFOEid_Object = MibTableColumn
radiusFFOEid = _RadiusFFOEid_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 3, 6, 1, 1, 1),
    _RadiusFFOEid_Type()
)
radiusFFOEid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    radiusFFOEid.setStatus("current")


class _FastFailoverEvents_Type(Integer32):
    """Custom type fastFailoverEvents based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fastFailoverEventsDisabled", 0),
          ("fastFailoverEventsEnabled", 1))
    )


_FastFailoverEvents_Type.__name__ = "Integer32"
_FastFailoverEvents_Object = MibTableColumn
fastFailoverEvents = _FastFailoverEvents_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 3, 6, 1, 1, 2),
    _FastFailoverEvents_Type()
)
fastFailoverEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fastFailoverEvents.setStatus("current")
_DhcpRelayListeners_ObjectIdentity = ObjectIdentity
dhcpRelayListeners = _DhcpRelayListeners_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 3, 7)
)
_DhcpRelayListenersMaxEntries_Type = Unsigned32
_DhcpRelayListenersMaxEntries_Object = MibScalar
dhcpRelayListenersMaxEntries = _DhcpRelayListenersMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 3, 7, 1),
    _DhcpRelayListenersMaxEntries_Type()
)
dhcpRelayListenersMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRelayListenersMaxEntries.setStatus("current")
_DhcpRelayListenersNumEntries_Type = Unsigned32
_DhcpRelayListenersNumEntries_Object = MibScalar
dhcpRelayListenersNumEntries = _DhcpRelayListenersNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 3, 7, 2),
    _DhcpRelayListenersNumEntries_Type()
)
dhcpRelayListenersNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRelayListenersNumEntries.setStatus("current")
_DhcpRelayListenersNextIndex_Type = Integer32
_DhcpRelayListenersNextIndex_Object = MibScalar
dhcpRelayListenersNextIndex = _DhcpRelayListenersNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 3, 7, 3),
    _DhcpRelayListenersNextIndex_Type()
)
dhcpRelayListenersNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRelayListenersNextIndex.setStatus("current")
_DhcpRelayListenersTable_Object = MibTable
dhcpRelayListenersTable = _DhcpRelayListenersTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 3, 7, 4)
)
if mibBuilder.loadTexts:
    dhcpRelayListenersTable.setStatus("current")
_DhcpRelayListenersEntry_Object = MibTableRow
dhcpRelayListenersEntry = _DhcpRelayListenersEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 3, 7, 4, 1)
)
dhcpRelayListenersEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-HWC-MIB", "dhcpRelayListenersID"),
)
if mibBuilder.loadTexts:
    dhcpRelayListenersEntry.setStatus("current")
_DhcpRelayListenersID_Type = Unsigned32
_DhcpRelayListenersID_Object = MibTableColumn
dhcpRelayListenersID = _DhcpRelayListenersID_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 3, 7, 4, 1, 1),
    _DhcpRelayListenersID_Type()
)
dhcpRelayListenersID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpRelayListenersID.setStatus("current")
_DhcpRelayListenersRowStatus_Type = RowStatus
_DhcpRelayListenersRowStatus_Object = MibTableColumn
dhcpRelayListenersRowStatus = _DhcpRelayListenersRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 3, 7, 4, 1, 2),
    _DhcpRelayListenersRowStatus_Type()
)
dhcpRelayListenersRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpRelayListenersRowStatus.setStatus("current")
_DestinationName_Type = DisplayString
_DestinationName_Object = MibTableColumn
destinationName = _DestinationName_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 3, 7, 4, 1, 3),
    _DestinationName_Type()
)
destinationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    destinationName.setStatus("current")
_DestinationIP_Type = IpAddress
_DestinationIP_Object = MibTableColumn
destinationIP = _DestinationIP_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 3, 7, 4, 1, 4),
    _DestinationIP_Type()
)
destinationIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    destinationIP.setStatus("current")


class _ClientAutologinOption_Type(Integer32):
    """Custom type clientAutologinOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 2),
          ("hide", 0),
          ("redirect", 1))
    )


_ClientAutologinOption_Type.__name__ = "Integer32"
_ClientAutologinOption_Object = MibScalar
clientAutologinOption = _ClientAutologinOption_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 3, 8),
    _ClientAutologinOption_Type()
)
clientAutologinOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientAutologinOption.setStatus("current")
_AuthenticationAdvanced_ObjectIdentity = ObjectIdentity
authenticationAdvanced = _AuthenticationAdvanced_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 3, 9)
)


class _IncludeServiceType_Type(Integer32):
    """Custom type includeServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_IncludeServiceType_Type.__name__ = "Integer32"
_IncludeServiceType_Object = MibScalar
includeServiceType = _IncludeServiceType_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 3, 9, 1),
    _IncludeServiceType_Type()
)
includeServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    includeServiceType.setStatus("current")
_ClientMessageDelayTime_Type = Integer32
_ClientMessageDelayTime_Object = MibScalar
clientMessageDelayTime = _ClientMessageDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 3, 9, 2),
    _ClientMessageDelayTime_Type()
)
clientMessageDelayTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientMessageDelayTime.setStatus("current")


class _RadiusAccounting_Type(Integer32):
    """Custom type radiusAccounting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RadiusAccounting_Type.__name__ = "Integer32"
_RadiusAccounting_Object = MibScalar
radiusAccounting = _RadiusAccounting_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 3, 9, 3),
    _RadiusAccounting_Type()
)
radiusAccounting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAccounting.setStatus("current")


class _ServerUsageModel_Type(Integer32):
    """Custom type serverUsageModel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("primaryBackup", 1),
          ("roundRobin", 0))
    )


_ServerUsageModel_Type.__name__ = "Integer32"
_ServerUsageModel_Object = MibScalar
serverUsageModel = _ServerUsageModel_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 3, 9, 4),
    _ServerUsageModel_Type()
)
serverUsageModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serverUsageModel.setStatus("current")


class _RadacctStartOnIPAddr_Type(Integer32):
    """Custom type radacctStartOnIPAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RadacctStartOnIPAddr_Type.__name__ = "Integer32"
_RadacctStartOnIPAddr_Object = MibScalar
radacctStartOnIPAddr = _RadacctStartOnIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 3, 9, 5),
    _RadacctStartOnIPAddr_Type()
)
radacctStartOnIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radacctStartOnIPAddr.setStatus("current")


class _ClientServiceTypeLogin_Type(Integer32):
    """Custom type clientServiceTypeLogin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ClientServiceTypeLogin_Type.__name__ = "Integer32"
_ClientServiceTypeLogin_Object = MibScalar
clientServiceTypeLogin = _ClientServiceTypeLogin_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 3, 9, 6),
    _ClientServiceTypeLogin_Type()
)
clientServiceTypeLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientServiceTypeLogin.setStatus("current")


class _ApplyMacAddressFormat_Type(Integer32):
    """Custom type applyMacAddressFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ApplyMacAddressFormat_Type.__name__ = "Integer32"
_ApplyMacAddressFormat_Object = MibScalar
applyMacAddressFormat = _ApplyMacAddressFormat_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 3, 9, 7),
    _ApplyMacAddressFormat_Type()
)
applyMacAddressFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    applyMacAddressFormat.setStatus("current")
_RadiusExtnsSetting_ObjectIdentity = ObjectIdentity
radiusExtnsSetting = _RadiusExtnsSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 3, 10)
)
_RadiusExtnsSettingTable_Object = MibTable
radiusExtnsSettingTable = _RadiusExtnsSettingTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 3, 10, 1)
)
if mibBuilder.loadTexts:
    radiusExtnsSettingTable.setStatus("current")
_RadiusExtnsSettingEntry_Object = MibTableRow
radiusExtnsSettingEntry = _RadiusExtnsSettingEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 3, 10, 1, 1)
)
radiusExtnsSettingEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-HWC-MIB", "radiusExtnsIndex"),
)
if mibBuilder.loadTexts:
    radiusExtnsSettingEntry.setStatus("current")


class _RadiusExtnsIndex_Type(Integer32):
    """Custom type radiusExtnsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RadiusExtnsIndex_Type.__name__ = "Integer32"
_RadiusExtnsIndex_Object = MibTableColumn
radiusExtnsIndex = _RadiusExtnsIndex_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 3, 10, 1, 1, 1),
    _RadiusExtnsIndex_Type()
)
radiusExtnsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    radiusExtnsIndex.setStatus("current")


class _PollingMechanism_Type(Integer32):
    """Custom type pollingMechanism based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("authorizeAsActualUser", 0),
          ("useRFC5997StatusServerRequest", 1))
    )


_PollingMechanism_Type.__name__ = "Integer32"
_PollingMechanism_Object = MibTableColumn
pollingMechanism = _PollingMechanism_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 3, 10, 1, 1, 2),
    _PollingMechanism_Type()
)
pollingMechanism.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pollingMechanism.setStatus("current")
_ServerPollingInterval_Type = Integer32
_ServerPollingInterval_Object = MibTableColumn
serverPollingInterval = _ServerPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 3, 10, 1, 1, 3),
    _ServerPollingInterval_Type()
)
serverPollingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serverPollingInterval.setStatus("current")
_NetflowAndMirrorN_ObjectIdentity = ObjectIdentity
netflowAndMirrorN = _NetflowAndMirrorN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 3, 11)
)
_NetflowDestinationIP_Type = IpAddress
_NetflowDestinationIP_Object = MibScalar
netflowDestinationIP = _NetflowDestinationIP_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 3, 11, 1),
    _NetflowDestinationIP_Type()
)
netflowDestinationIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netflowDestinationIP.setStatus("current")


class _NetflowInterval_Type(Integer32):
    """Custom type netflowInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 360),
    )


_NetflowInterval_Type.__name__ = "Integer32"
_NetflowInterval_Object = MibScalar
netflowInterval = _NetflowInterval_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 3, 11, 2),
    _NetflowInterval_Type()
)
netflowInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netflowInterval.setStatus("current")


class _MirrorFirstN_Type(Integer32):
    """Custom type mirrorFirstN based on Integer32"""
    defaultValue = 15


_MirrorFirstN_Object = MibScalar
mirrorFirstN = _MirrorFirstN_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 3, 11, 3),
    _MirrorFirstN_Type()
)
mirrorFirstN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mirrorFirstN.setStatus("current")
_MirrorL2Ports_Type = OctetString
_MirrorL2Ports_Object = MibScalar
mirrorL2Ports = _MirrorL2Ports_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 3, 11, 4),
    _MirrorL2Ports_Type()
)
mirrorL2Ports.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mirrorL2Ports.setStatus("current")


class _RadiusMacAddressFormatOption_Type(Integer32):
    """Custom type radiusMacAddressFormatOption based on Integer32"""
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
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("option1", 1),
          ("option10", 10),
          ("option11", 11),
          ("option12", 12),
          ("option2", 2),
          ("option3", 3),
          ("option4", 4),
          ("option5", 5),
          ("option6", 6),
          ("option7", 7),
          ("option8", 9))
    )


_RadiusMacAddressFormatOption_Type.__name__ = "Integer32"
_RadiusMacAddressFormatOption_Object = MibScalar
radiusMacAddressFormatOption = _RadiusMacAddressFormatOption_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 3, 12),
    _RadiusMacAddressFormatOption_Type()
)
radiusMacAddressFormatOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusMacAddressFormatOption.setStatus("current")
_Wlan_ObjectIdentity = ObjectIdentity
wlan = _Wlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4)
)
_WlanMaxEntries_Type = Unsigned32
_WlanMaxEntries_Object = MibScalar
wlanMaxEntries = _WlanMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 1),
    _WlanMaxEntries_Type()
)
wlanMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanMaxEntries.setStatus("current")
_WlanNumEntries_Type = Unsigned32
_WlanNumEntries_Object = MibScalar
wlanNumEntries = _WlanNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 2),
    _WlanNumEntries_Type()
)
wlanNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanNumEntries.setStatus("current")
_WlanTableNextAvailableIndex_Type = Integer32
_WlanTableNextAvailableIndex_Object = MibScalar
wlanTableNextAvailableIndex = _WlanTableNextAvailableIndex_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 3),
    _WlanTableNextAvailableIndex_Type()
)
wlanTableNextAvailableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanTableNextAvailableIndex.setStatus("current")
_WlanTable_Object = MibTable
wlanTable = _WlanTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 4)
)
if mibBuilder.loadTexts:
    wlanTable.setStatus("current")
_WlanEntry_Object = MibTableRow
wlanEntry = _WlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 4, 1)
)
wlanEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-HWC-MIB", "wlanID"),
)
if mibBuilder.loadTexts:
    wlanEntry.setStatus("current")
_WlanID_Type = Unsigned32
_WlanID_Object = MibTableColumn
wlanID = _WlanID_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 4, 1, 1),
    _WlanID_Type()
)
wlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanID.setStatus("current")
_WlanRowStatus_Type = RowStatus
_WlanRowStatus_Object = MibTableColumn
wlanRowStatus = _WlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 4, 1, 2),
    _WlanRowStatus_Type()
)
wlanRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanRowStatus.setStatus("current")


class _WlanServiceType_Type(Integer32):
    """Custom type wlanServiceType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("mesh", 6),
          ("remote", 5),
          ("standard", 0),
          ("thirdParty", 4),
          ("wds", 3))
    )


_WlanServiceType_Type.__name__ = "Integer32"
_WlanServiceType_Object = MibTableColumn
wlanServiceType = _WlanServiceType_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 4, 1, 3),
    _WlanServiceType_Type()
)
wlanServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanServiceType.setStatus("current")
_WlanName_Type = DisplayString
_WlanName_Object = MibTableColumn
wlanName = _WlanName_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 4, 1, 4),
    _WlanName_Type()
)
wlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanName.setStatus("current")


class _WlanSSID_Type(DisplayString):
    """Custom type wlanSSID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WlanSSID_Type.__name__ = "DisplayString"
_WlanSSID_Object = MibTableColumn
wlanSSID = _WlanSSID_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 4, 1, 5),
    _WlanSSID_Type()
)
wlanSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanSSID.setStatus("current")


class _WlanSynchronize_Type(TruthValue):
    """Custom type wlanSynchronize based on TruthValue"""
    defaultValue = 1


_WlanSynchronize_Object = MibTableColumn
wlanSynchronize = _WlanSynchronize_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 4, 1, 6),
    _WlanSynchronize_Type()
)
wlanSynchronize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanSynchronize.setStatus("current")


class _WlanEnabled_Type(TruthValue):
    """Custom type wlanEnabled based on TruthValue"""
    defaultValue = 1


_WlanEnabled_Object = MibTableColumn
wlanEnabled = _WlanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 4, 1, 7),
    _WlanEnabled_Type()
)
wlanEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanEnabled.setStatus("current")


class _WlanDefaultTopologyID_Type(Integer32):
    """Custom type wlanDefaultTopologyID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 65535),
    )


_WlanDefaultTopologyID_Type.__name__ = "Integer32"
_WlanDefaultTopologyID_Object = MibTableColumn
wlanDefaultTopologyID = _WlanDefaultTopologyID_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 4, 1, 8),
    _WlanDefaultTopologyID_Type()
)
wlanDefaultTopologyID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanDefaultTopologyID.setStatus("current")


class _WlanSessionTimeout_Type(Unsigned32):
    """Custom type wlanSessionTimeout based on Unsigned32"""
    defaultValue = 0


_WlanSessionTimeout_Object = MibTableColumn
wlanSessionTimeout = _WlanSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 4, 1, 9),
    _WlanSessionTimeout_Type()
)
wlanSessionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanSessionTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wlanSessionTimeout.setUnits("minute")


class _WlanIdleTimeoutPreAuth_Type(Unsigned32):
    """Custom type wlanIdleTimeoutPreAuth based on Unsigned32"""
    defaultValue = 5


_WlanIdleTimeoutPreAuth_Object = MibTableColumn
wlanIdleTimeoutPreAuth = _WlanIdleTimeoutPreAuth_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 4, 1, 10),
    _WlanIdleTimeoutPreAuth_Type()
)
wlanIdleTimeoutPreAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanIdleTimeoutPreAuth.setStatus("current")
if mibBuilder.loadTexts:
    wlanIdleTimeoutPreAuth.setUnits("minute")


class _WlanIdleSessionPostAuth_Type(Unsigned32):
    """Custom type wlanIdleSessionPostAuth based on Unsigned32"""
    defaultValue = 30


_WlanIdleSessionPostAuth_Object = MibTableColumn
wlanIdleSessionPostAuth = _WlanIdleSessionPostAuth_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 4, 1, 11),
    _WlanIdleSessionPostAuth_Type()
)
wlanIdleSessionPostAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanIdleSessionPostAuth.setStatus("current")
if mibBuilder.loadTexts:
    wlanIdleSessionPostAuth.setUnits("minute")


class _WlanSupressSSID_Type(TruthValue):
    """Custom type wlanSupressSSID based on TruthValue"""
    defaultValue = 2


_WlanSupressSSID_Object = MibTableColumn
wlanSupressSSID = _WlanSupressSSID_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 4, 1, 12),
    _WlanSupressSSID_Type()
)
wlanSupressSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanSupressSSID.setStatus("current")


class _WlanDot11hSupport_Type(TruthValue):
    """Custom type wlanDot11hSupport based on TruthValue"""
    defaultValue = 2


_WlanDot11hSupport_Object = MibTableColumn
wlanDot11hSupport = _WlanDot11hSupport_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 4, 1, 13),
    _WlanDot11hSupport_Type()
)
wlanDot11hSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanDot11hSupport.setStatus("current")


class _WlanDot11hClientPowerReduction_Type(TruthValue):
    """Custom type wlanDot11hClientPowerReduction based on TruthValue"""
    defaultValue = 2


_WlanDot11hClientPowerReduction_Object = MibTableColumn
wlanDot11hClientPowerReduction = _WlanDot11hClientPowerReduction_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 4, 1, 14),
    _WlanDot11hClientPowerReduction_Type()
)
wlanDot11hClientPowerReduction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanDot11hClientPowerReduction.setStatus("current")


class _WlanProcessClientIE_Type(TruthValue):
    """Custom type wlanProcessClientIE based on TruthValue"""
    defaultValue = 2


_WlanProcessClientIE_Object = MibTableColumn
wlanProcessClientIE = _WlanProcessClientIE_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 4, 1, 15),
    _WlanProcessClientIE_Type()
)
wlanProcessClientIE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanProcessClientIE.setStatus("current")


class _WlanEngerySaveMode_Type(TruthValue):
    """Custom type wlanEngerySaveMode based on TruthValue"""
    defaultValue = 2


_WlanEngerySaveMode_Object = MibTableColumn
wlanEngerySaveMode = _WlanEngerySaveMode_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 4, 1, 16),
    _WlanEngerySaveMode_Type()
)
wlanEngerySaveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanEngerySaveMode.setStatus("current")


class _WlanBlockMuToMuTraffic_Type(TruthValue):
    """Custom type wlanBlockMuToMuTraffic based on TruthValue"""
    defaultValue = 2


_WlanBlockMuToMuTraffic_Object = MibTableColumn
wlanBlockMuToMuTraffic = _WlanBlockMuToMuTraffic_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 4, 1, 17),
    _WlanBlockMuToMuTraffic_Type()
)
wlanBlockMuToMuTraffic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanBlockMuToMuTraffic.setStatus("current")


class _WlanRemoteable_Type(TruthValue):
    """Custom type wlanRemoteable based on TruthValue"""
    defaultValue = 2


_WlanRemoteable_Object = MibTableColumn
wlanRemoteable = _WlanRemoteable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 4, 1, 18),
    _WlanRemoteable_Type()
)
wlanRemoteable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanRemoteable.setStatus("current")


class _WlanVNSID_Type(Unsigned32):
    """Custom type wlanVNSID based on Unsigned32"""
    defaultValue = 0


_WlanVNSID_Object = MibTableColumn
wlanVNSID = _WlanVNSID_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 4, 1, 19),
    _WlanVNSID_Type()
)
wlanVNSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanVNSID.setStatus("current")


class _WlanRadioManagement11k_Type(Integer32):
    """Custom type wlanRadioManagement11k based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_WlanRadioManagement11k_Type.__name__ = "Integer32"
_WlanRadioManagement11k_Object = MibTableColumn
wlanRadioManagement11k = _WlanRadioManagement11k_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 4, 1, 20),
    _WlanRadioManagement11k_Type()
)
wlanRadioManagement11k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanRadioManagement11k.setStatus("current")


class _WlanBeaconReport_Type(Integer32):
    """Custom type wlanBeaconReport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_WlanBeaconReport_Type.__name__ = "Integer32"
_WlanBeaconReport_Object = MibTableColumn
wlanBeaconReport = _WlanBeaconReport_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 4, 1, 21),
    _WlanBeaconReport_Type()
)
wlanBeaconReport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanBeaconReport.setStatus("current")


class _WlanQuietIE_Type(Integer32):
    """Custom type wlanQuietIE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_WlanQuietIE_Type.__name__ = "Integer32"
_WlanQuietIE_Object = MibTableColumn
wlanQuietIE = _WlanQuietIE_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 4, 1, 22),
    _WlanQuietIE_Type()
)
wlanQuietIE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanQuietIE.setStatus("current")


class _WlanMirrorN_Type(Integer32):
    """Custom type wlanMirrorN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bothDirection", 1),
          ("prohibited", 0),
          ("rxDirectionOnly", 2))
    )


_WlanMirrorN_Type.__name__ = "Integer32"
_WlanMirrorN_Object = MibTableColumn
wlanMirrorN = _WlanMirrorN_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 4, 1, 23),
    _WlanMirrorN_Type()
)
wlanMirrorN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanMirrorN.setStatus("current")


class _WlanNetFlow_Type(Integer32):
    """Custom type wlanNetFlow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_WlanNetFlow_Type.__name__ = "Integer32"
_WlanNetFlow_Object = MibTableColumn
wlanNetFlow = _WlanNetFlow_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 4, 1, 24),
    _WlanNetFlow_Type()
)
wlanNetFlow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanNetFlow.setStatus("current")


class _WlanAppVisibility_Type(Integer32):
    """Custom type wlanAppVisibility based on Integer32"""
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


_WlanAppVisibility_Type.__name__ = "Integer32"
_WlanAppVisibility_Object = MibTableColumn
wlanAppVisibility = _WlanAppVisibility_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 4, 1, 25),
    _WlanAppVisibility_Type()
)
wlanAppVisibility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanAppVisibility.setStatus("current")
_WlanStatsTable_Object = MibTable
wlanStatsTable = _WlanStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 5)
)
if mibBuilder.loadTexts:
    wlanStatsTable.setStatus("current")
_WlanStatsEntry_Object = MibTableRow
wlanStatsEntry = _WlanStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 5, 1)
)
wlanStatsEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-HWC-MIB", "wlanStatsID"),
)
if mibBuilder.loadTexts:
    wlanStatsEntry.setStatus("current")
_WlanStatsID_Type = Unsigned32
_WlanStatsID_Object = MibTableColumn
wlanStatsID = _WlanStatsID_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 5, 1, 1),
    _WlanStatsID_Type()
)
wlanStatsID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsID.setStatus("current")
_WlanStatsAssociatedClients_Type = Counter32
_WlanStatsAssociatedClients_Object = MibTableColumn
wlanStatsAssociatedClients = _WlanStatsAssociatedClients_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 5, 1, 2),
    _WlanStatsAssociatedClients_Type()
)
wlanStatsAssociatedClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsAssociatedClients.setStatus("current")
_WlanStatsRadiusTotRequests_Type = Counter32
_WlanStatsRadiusTotRequests_Object = MibTableColumn
wlanStatsRadiusTotRequests = _WlanStatsRadiusTotRequests_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 5, 1, 3),
    _WlanStatsRadiusTotRequests_Type()
)
wlanStatsRadiusTotRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsRadiusTotRequests.setStatus("current")
_WlanStatsRadiusReqFailed_Type = Counter32
_WlanStatsRadiusReqFailed_Object = MibTableColumn
wlanStatsRadiusReqFailed = _WlanStatsRadiusReqFailed_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 5, 1, 4),
    _WlanStatsRadiusReqFailed_Type()
)
wlanStatsRadiusReqFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsRadiusReqFailed.setStatus("current")
_WlanStatsRadiusReqRejected_Type = Counter32
_WlanStatsRadiusReqRejected_Object = MibTableColumn
wlanStatsRadiusReqRejected = _WlanStatsRadiusReqRejected_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 5, 1, 5),
    _WlanStatsRadiusReqRejected_Type()
)
wlanStatsRadiusReqRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanStatsRadiusReqRejected.setStatus("current")
_WlanPrivTable_Object = MibTable
wlanPrivTable = _WlanPrivTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 6)
)
if mibBuilder.loadTexts:
    wlanPrivTable.setStatus("current")
_WlanPrivEntry_Object = MibTableRow
wlanPrivEntry = _WlanPrivEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 6, 1)
)
wlanPrivEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-HWC-MIB", "wlanID"),
)
if mibBuilder.loadTexts:
    wlanPrivEntry.setStatus("current")


class _WlanPrivPrivacyType_Type(Integer32):
    """Custom type wlanPrivPrivacyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("dynamicWEP", 2),
          ("none", 0),
          ("staticWEP", 1),
          ("wpa", 3),
          ("wpaPSK", 4))
    )


_WlanPrivPrivacyType_Type.__name__ = "Integer32"
_WlanPrivPrivacyType_Object = MibTableColumn
wlanPrivPrivacyType = _WlanPrivPrivacyType_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 6, 1, 1),
    _WlanPrivPrivacyType_Type()
)
wlanPrivPrivacyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanPrivPrivacyType.setStatus("current")


class _WlanPrivWEPKeyIndex_Type(Integer32):
    """Custom type wlanPrivWEPKeyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_WlanPrivWEPKeyIndex_Type.__name__ = "Integer32"
_WlanPrivWEPKeyIndex_Object = MibTableColumn
wlanPrivWEPKeyIndex = _WlanPrivWEPKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 6, 1, 2),
    _WlanPrivWEPKeyIndex_Type()
)
wlanPrivWEPKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanPrivWEPKeyIndex.setStatus("current")


class _WlanPrivWEPKeyLength_Type(Integer32):
    """Custom type wlanPrivWEPKeyLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("oneHundred28Bits", 2),
          ("oneHundred52Bits", 3),
          ("sixtyFourBits", 1))
    )


_WlanPrivWEPKeyLength_Type.__name__ = "Integer32"
_WlanPrivWEPKeyLength_Object = MibTableColumn
wlanPrivWEPKeyLength = _WlanPrivWEPKeyLength_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 6, 1, 3),
    _WlanPrivWEPKeyLength_Type()
)
wlanPrivWEPKeyLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanPrivWEPKeyLength.setStatus("current")


class _WlanPrivWEPKey_Type(DisplayString):
    """Custom type wlanPrivWEPKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 19),
    )


_WlanPrivWEPKey_Type.__name__ = "DisplayString"
_WlanPrivWEPKey_Object = MibTableColumn
wlanPrivWEPKey = _WlanPrivWEPKey_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 6, 1, 4),
    _WlanPrivWEPKey_Type()
)
wlanPrivWEPKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanPrivWEPKey.setStatus("current")


class _WlanPrivWPAv1EncryptionType_Type(Integer32):
    """Custom type wlanPrivWPAv1EncryptionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("tkipOnly", 1),
          ("undefined", 0))
    )


_WlanPrivWPAv1EncryptionType_Type.__name__ = "Integer32"
_WlanPrivWPAv1EncryptionType_Object = MibTableColumn
wlanPrivWPAv1EncryptionType = _WlanPrivWPAv1EncryptionType_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 6, 1, 5),
    _WlanPrivWPAv1EncryptionType_Type()
)
wlanPrivWPAv1EncryptionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanPrivWPAv1EncryptionType.setStatus("current")


class _WlanPrivWPAv2EncryptionType_Type(Integer32):
    """Custom type wlanPrivWPAv2EncryptionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aesOnly", 3),
          ("auto", 2),
          ("undefined", 0))
    )


_WlanPrivWPAv2EncryptionType_Type.__name__ = "Integer32"
_WlanPrivWPAv2EncryptionType_Object = MibTableColumn
wlanPrivWPAv2EncryptionType = _WlanPrivWPAv2EncryptionType_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 6, 1, 6),
    _WlanPrivWPAv2EncryptionType_Type()
)
wlanPrivWPAv2EncryptionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanPrivWPAv2EncryptionType.setStatus("current")


class _WlanPrivKeyManagement_Type(Integer32):
    """Custom type wlanPrivKeyManagement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("none", 0),
          ("opportunisticKey", 1),
          ("preAuthentication", 2))
    )


_WlanPrivKeyManagement_Type.__name__ = "Integer32"
_WlanPrivKeyManagement_Object = MibTableColumn
wlanPrivKeyManagement = _WlanPrivKeyManagement_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 6, 1, 7),
    _WlanPrivKeyManagement_Type()
)
wlanPrivKeyManagement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanPrivKeyManagement.setStatus("current")
_WlanPrivBroadcastRekeying_Type = TruthValue
_WlanPrivBroadcastRekeying_Object = MibTableColumn
wlanPrivBroadcastRekeying = _WlanPrivBroadcastRekeying_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 6, 1, 8),
    _WlanPrivBroadcastRekeying_Type()
)
wlanPrivBroadcastRekeying.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanPrivBroadcastRekeying.setStatus("current")


class _WlanPrivRekeyInterval_Type(Unsigned32):
    """Custom type wlanPrivRekeyInterval based on Unsigned32"""
    defaultValue = 3600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 86400),
    )


_WlanPrivRekeyInterval_Type.__name__ = "Unsigned32"
_WlanPrivRekeyInterval_Object = MibTableColumn
wlanPrivRekeyInterval = _WlanPrivRekeyInterval_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 6, 1, 9),
    _WlanPrivRekeyInterval_Type()
)
wlanPrivRekeyInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanPrivRekeyInterval.setStatus("current")
if mibBuilder.loadTexts:
    wlanPrivRekeyInterval.setUnits("seconds")
_WlanPrivGroupKPSR_Type = TruthValue
_WlanPrivGroupKPSR_Object = MibTableColumn
wlanPrivGroupKPSR = _WlanPrivGroupKPSR_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 6, 1, 10),
    _WlanPrivGroupKPSR_Type()
)
wlanPrivGroupKPSR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanPrivGroupKPSR.setStatus("current")


class _WlanPrivWPAPSK_Type(OctetString):
    """Custom type wlanPrivWPAPSK based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 63),
    )


_WlanPrivWPAPSK_Type.__name__ = "OctetString"
_WlanPrivWPAPSK_Object = MibTableColumn
wlanPrivWPAPSK = _WlanPrivWPAPSK_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 6, 1, 11),
    _WlanPrivWPAPSK_Type()
)
wlanPrivWPAPSK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanPrivWPAPSK.setStatus("current")


class _WlanPrivWPAversion_Type(Integer32):
    """Custom type wlanPrivWPAversion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("wpaNone", 0),
          ("wpaV1", 1),
          ("wpaV1andV2", 3),
          ("wpaV2", 2))
    )


_WlanPrivWPAversion_Type.__name__ = "Integer32"
_WlanPrivWPAversion_Object = MibTableColumn
wlanPrivWPAversion = _WlanPrivWPAversion_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 6, 1, 12),
    _WlanPrivWPAversion_Type()
)
wlanPrivWPAversion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanPrivWPAversion.setStatus("current")


class _WlanPrivfastTransition_Type(Integer32):
    """Custom type wlanPrivfastTransition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_WlanPrivfastTransition_Type.__name__ = "Integer32"
_WlanPrivfastTransition_Object = MibTableColumn
wlanPrivfastTransition = _WlanPrivfastTransition_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 6, 1, 13),
    _WlanPrivfastTransition_Type()
)
wlanPrivfastTransition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanPrivfastTransition.setStatus("current")


class _WlanPrivManagementFrameProtection_Type(Integer32):
    """Custom type wlanPrivManagementFrameProtection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("require", 2))
    )


_WlanPrivManagementFrameProtection_Type.__name__ = "Integer32"
_WlanPrivManagementFrameProtection_Object = MibTableColumn
wlanPrivManagementFrameProtection = _WlanPrivManagementFrameProtection_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 6, 1, 14),
    _WlanPrivManagementFrameProtection_Type()
)
wlanPrivManagementFrameProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanPrivManagementFrameProtection.setStatus("current")
_WlanAuthTable_Object = MibTable
wlanAuthTable = _WlanAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 7)
)
if mibBuilder.loadTexts:
    wlanAuthTable.setStatus("current")
_WlanAuthEntry_Object = MibTableRow
wlanAuthEntry = _WlanAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 7, 1)
)
wlanAuthEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-HWC-MIB", "wlanID"),
)
if mibBuilder.loadTexts:
    wlanAuthEntry.setStatus("current")


class _WlanAuthType_Type(Integer32):
    """Custom type wlanAuthType based on Integer32"""
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
        *(("disabled", 1),
          ("dot1x", 3),
          ("easyGuestCP", 5),
          ("externalCP", 4),
          ("firewallFriendlyExCP", 7),
          ("guestSplash", 6),
          ("internalCP", 2))
    )


_WlanAuthType_Type.__name__ = "Integer32"
_WlanAuthType_Object = MibTableColumn
wlanAuthType = _WlanAuthType_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 7, 1, 1),
    _WlanAuthType_Type()
)
wlanAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanAuthType.setStatus("current")
_WlanAuthMacBasedAuth_Type = TruthValue
_WlanAuthMacBasedAuth_Object = MibTableColumn
wlanAuthMacBasedAuth = _WlanAuthMacBasedAuth_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 7, 1, 2),
    _WlanAuthMacBasedAuth_Type()
)
wlanAuthMacBasedAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanAuthMacBasedAuth.setStatus("current")
_WlanAuthMACBasedAuthOnRoam_Type = TruthValue
_WlanAuthMACBasedAuthOnRoam_Object = MibTableColumn
wlanAuthMACBasedAuthOnRoam = _WlanAuthMACBasedAuthOnRoam_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 7, 1, 3),
    _WlanAuthMACBasedAuthOnRoam_Type()
)
wlanAuthMACBasedAuthOnRoam.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanAuthMACBasedAuthOnRoam.setStatus("current")
_WlanAuthAutoAuthAuthorizedUser_Type = TruthValue
_WlanAuthAutoAuthAuthorizedUser_Object = MibTableColumn
wlanAuthAutoAuthAuthorizedUser = _WlanAuthAutoAuthAuthorizedUser_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 7, 1, 4),
    _WlanAuthAutoAuthAuthorizedUser_Type()
)
wlanAuthAutoAuthAuthorizedUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanAuthAutoAuthAuthorizedUser.setStatus("current")
_WlanAuthAllowUnauthorizedUser_Type = TruthValue
_WlanAuthAllowUnauthorizedUser_Object = MibTableColumn
wlanAuthAllowUnauthorizedUser = _WlanAuthAllowUnauthorizedUser_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 7, 1, 5),
    _WlanAuthAllowUnauthorizedUser_Type()
)
wlanAuthAllowUnauthorizedUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanAuthAllowUnauthorizedUser.setStatus("current")
_WlanAuthRadiusIncludeAP_Type = TruthValue
_WlanAuthRadiusIncludeAP_Object = MibTableColumn
wlanAuthRadiusIncludeAP = _WlanAuthRadiusIncludeAP_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 7, 1, 6),
    _WlanAuthRadiusIncludeAP_Type()
)
wlanAuthRadiusIncludeAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanAuthRadiusIncludeAP.setStatus("current")
_WlanAuthRadiusIncludeVNS_Type = TruthValue
_WlanAuthRadiusIncludeVNS_Object = MibTableColumn
wlanAuthRadiusIncludeVNS = _WlanAuthRadiusIncludeVNS_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 7, 1, 7),
    _WlanAuthRadiusIncludeVNS_Type()
)
wlanAuthRadiusIncludeVNS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanAuthRadiusIncludeVNS.setStatus("current")
_WlanAuthRadiusIncludeSSID_Type = TruthValue
_WlanAuthRadiusIncludeSSID_Object = MibTableColumn
wlanAuthRadiusIncludeSSID = _WlanAuthRadiusIncludeSSID_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 7, 1, 8),
    _WlanAuthRadiusIncludeSSID_Type()
)
wlanAuthRadiusIncludeSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanAuthRadiusIncludeSSID.setStatus("current")
_WlanAuthRadiusIncludePolicy_Type = TruthValue
_WlanAuthRadiusIncludePolicy_Object = MibTableColumn
wlanAuthRadiusIncludePolicy = _WlanAuthRadiusIncludePolicy_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 7, 1, 9),
    _WlanAuthRadiusIncludePolicy_Type()
)
wlanAuthRadiusIncludePolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanAuthRadiusIncludePolicy.setStatus("current")
_WlanAuthRadiusIncludeTopology_Type = TruthValue
_WlanAuthRadiusIncludeTopology_Object = MibTableColumn
wlanAuthRadiusIncludeTopology = _WlanAuthRadiusIncludeTopology_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 7, 1, 10),
    _WlanAuthRadiusIncludeTopology_Type()
)
wlanAuthRadiusIncludeTopology.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanAuthRadiusIncludeTopology.setStatus("current")
_WlanAuthRadiusIncludeIngressRC_Type = TruthValue
_WlanAuthRadiusIncludeIngressRC_Object = MibTableColumn
wlanAuthRadiusIncludeIngressRC = _WlanAuthRadiusIncludeIngressRC_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 7, 1, 11),
    _WlanAuthRadiusIncludeIngressRC_Type()
)
wlanAuthRadiusIncludeIngressRC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanAuthRadiusIncludeIngressRC.setStatus("current")
_WlanAuthRadiusIncludeEgressRC_Type = TruthValue
_WlanAuthRadiusIncludeEgressRC_Object = MibTableColumn
wlanAuthRadiusIncludeEgressRC = _WlanAuthRadiusIncludeEgressRC_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 7, 1, 12),
    _WlanAuthRadiusIncludeEgressRC_Type()
)
wlanAuthRadiusIncludeEgressRC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanAuthRadiusIncludeEgressRC.setStatus("current")
_WlanAuthCollectAcctInformation_Type = TruthValue
_WlanAuthCollectAcctInformation_Object = MibTableColumn
wlanAuthCollectAcctInformation = _WlanAuthCollectAcctInformation_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 7, 1, 13),
    _WlanAuthCollectAcctInformation_Type()
)
wlanAuthCollectAcctInformation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanAuthCollectAcctInformation.setStatus("current")
_WlanAuthReplaceCalledStationIDWithZone_Type = TruthValue
_WlanAuthReplaceCalledStationIDWithZone_Object = MibTableColumn
wlanAuthReplaceCalledStationIDWithZone = _WlanAuthReplaceCalledStationIDWithZone_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 7, 1, 14),
    _WlanAuthReplaceCalledStationIDWithZone_Type()
)
wlanAuthReplaceCalledStationIDWithZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanAuthReplaceCalledStationIDWithZone.setStatus("current")
_WlanAuthRadiusAcctAfterMacBaseAuthorization_Type = TruthValue
_WlanAuthRadiusAcctAfterMacBaseAuthorization_Object = MibTableColumn
wlanAuthRadiusAcctAfterMacBaseAuthorization = _WlanAuthRadiusAcctAfterMacBaseAuthorization_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 7, 1, 15),
    _WlanAuthRadiusAcctAfterMacBaseAuthorization_Type()
)
wlanAuthRadiusAcctAfterMacBaseAuthorization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanAuthRadiusAcctAfterMacBaseAuthorization.setStatus("current")
_WlanAuthRadiusTimeoutRole_Type = Integer32
_WlanAuthRadiusTimeoutRole_Object = MibTableColumn
wlanAuthRadiusTimeoutRole = _WlanAuthRadiusTimeoutRole_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 7, 1, 16),
    _WlanAuthRadiusTimeoutRole_Type()
)
wlanAuthRadiusTimeoutRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanAuthRadiusTimeoutRole.setStatus("current")


class _WlanAuthRadiusOperatorNameSpace_Type(Integer32):
    """Custom type wlanAuthRadiusOperatorNameSpace based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              48,
              49,
              50,
              51)
        )
    )
    namedValues = NamedValues(
        *(("disabled", -1),
          ("e212", 50),
          ("icc", 51),
          ("realm", 49),
          ("tadig", 48))
    )


_WlanAuthRadiusOperatorNameSpace_Type.__name__ = "Integer32"
_WlanAuthRadiusOperatorNameSpace_Object = MibTableColumn
wlanAuthRadiusOperatorNameSpace = _WlanAuthRadiusOperatorNameSpace_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 7, 1, 17),
    _WlanAuthRadiusOperatorNameSpace_Type()
)
wlanAuthRadiusOperatorNameSpace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanAuthRadiusOperatorNameSpace.setStatus("current")
_WlanAuthRadiusOperatorName_Type = DisplayString
_WlanAuthRadiusOperatorName_Object = MibTableColumn
wlanAuthRadiusOperatorName = _WlanAuthRadiusOperatorName_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 7, 1, 18),
    _WlanAuthRadiusOperatorName_Type()
)
wlanAuthRadiusOperatorName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanAuthRadiusOperatorName.setStatus("current")
_WlanAuthMACBasedAuthReAuthOnAreaRoam_Type = TruthValue
_WlanAuthMACBasedAuthReAuthOnAreaRoam_Object = MibTableColumn
wlanAuthMACBasedAuthReAuthOnAreaRoam = _WlanAuthMACBasedAuthReAuthOnAreaRoam_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 7, 1, 19),
    _WlanAuthMACBasedAuthReAuthOnAreaRoam_Type()
)
wlanAuthMACBasedAuthReAuthOnAreaRoam.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanAuthMACBasedAuthReAuthOnAreaRoam.setStatus("current")
_WlanRadiusTable_Object = MibTable
wlanRadiusTable = _WlanRadiusTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 8)
)
if mibBuilder.loadTexts:
    wlanRadiusTable.setStatus("current")
_WlanRadiusEntry_Object = MibTableRow
wlanRadiusEntry = _WlanRadiusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 8, 1)
)
wlanRadiusEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-HWC-MIB", "wlanID"),
    (0, "HIPATH-WIRELESS-HWC-MIB", "wlanRadiusIndex"),
)
if mibBuilder.loadTexts:
    wlanRadiusEntry.setStatus("current")
_WlanRadiusIndex_Type = Unsigned32
_WlanRadiusIndex_Object = MibTableColumn
wlanRadiusIndex = _WlanRadiusIndex_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 8, 1, 1),
    _WlanRadiusIndex_Type()
)
wlanRadiusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wlanRadiusIndex.setStatus("current")
_WlanRadiusName_Type = DisplayString
_WlanRadiusName_Object = MibTableColumn
wlanRadiusName = _WlanRadiusName_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 8, 1, 2),
    _WlanRadiusName_Type()
)
wlanRadiusName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanRadiusName.setStatus("current")


class _WlanRadiusUsage_Type(Integer32):
    """Custom type wlanRadiusUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("acc", 3),
          ("auth", 1),
          ("mac", 2))
    )


_WlanRadiusUsage_Type.__name__ = "Integer32"
_WlanRadiusUsage_Object = MibTableColumn
wlanRadiusUsage = _WlanRadiusUsage_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 8, 1, 3),
    _WlanRadiusUsage_Type()
)
wlanRadiusUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanRadiusUsage.setStatus("current")
_WlanRadiusPriority_Type = Integer32
_WlanRadiusPriority_Object = MibTableColumn
wlanRadiusPriority = _WlanRadiusPriority_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 8, 1, 4),
    _WlanRadiusPriority_Type()
)
wlanRadiusPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanRadiusPriority.setStatus("current")


class _WlanRadiusPort_Type(Unsigned32):
    """Custom type wlanRadiusPort based on Unsigned32"""
    defaultValue = 1812


_WlanRadiusPort_Object = MibTableColumn
wlanRadiusPort = _WlanRadiusPort_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 8, 1, 5),
    _WlanRadiusPort_Type()
)
wlanRadiusPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanRadiusPort.setStatus("current")


class _WlanRadiusRetries_Type(Unsigned32):
    """Custom type wlanRadiusRetries based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_WlanRadiusRetries_Type.__name__ = "Unsigned32"
_WlanRadiusRetries_Object = MibTableColumn
wlanRadiusRetries = _WlanRadiusRetries_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 8, 1, 6),
    _WlanRadiusRetries_Type()
)
wlanRadiusRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanRadiusRetries.setStatus("current")


class _WlanRadiusTimeout_Type(Unsigned32):
    """Custom type wlanRadiusTimeout based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 360),
    )


_WlanRadiusTimeout_Type.__name__ = "Unsigned32"
_WlanRadiusTimeout_Object = MibTableColumn
wlanRadiusTimeout = _WlanRadiusTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 8, 1, 7),
    _WlanRadiusTimeout_Type()
)
wlanRadiusTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanRadiusTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wlanRadiusTimeout.setUnits("seconds")
_WlanRadiusNASUseVnsIP_Type = TruthValue
_WlanRadiusNASUseVnsIP_Object = MibTableColumn
wlanRadiusNASUseVnsIP = _WlanRadiusNASUseVnsIP_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 8, 1, 8),
    _WlanRadiusNASUseVnsIP_Type()
)
wlanRadiusNASUseVnsIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanRadiusNASUseVnsIP.setStatus("current")
_WlanRadiusNASIP_Type = DisplayString
_WlanRadiusNASIP_Object = MibTableColumn
wlanRadiusNASIP = _WlanRadiusNASIP_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 8, 1, 9),
    _WlanRadiusNASIP_Type()
)
wlanRadiusNASIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanRadiusNASIP.setStatus("current")
_WlanRadiusNASIDUseVNSName_Type = TruthValue
_WlanRadiusNASIDUseVNSName_Object = MibTableColumn
wlanRadiusNASIDUseVNSName = _WlanRadiusNASIDUseVNSName_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 8, 1, 10),
    _WlanRadiusNASIDUseVNSName_Type()
)
wlanRadiusNASIDUseVNSName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanRadiusNASIDUseVNSName.setStatus("current")
_WlanRadiusNASID_Type = DisplayString
_WlanRadiusNASID_Object = MibTableColumn
wlanRadiusNASID = _WlanRadiusNASID_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 8, 1, 11),
    _WlanRadiusNASID_Type()
)
wlanRadiusNASID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanRadiusNASID.setStatus("current")


class _WlanRadiusAuthType_Type(Integer32):
    """Custom type wlanRadiusAuthType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("chap", 1),
          ("mschap", 2),
          ("mschap2", 3),
          ("pap", 0))
    )


_WlanRadiusAuthType_Type.__name__ = "Integer32"
_WlanRadiusAuthType_Object = MibTableColumn
wlanRadiusAuthType = _WlanRadiusAuthType_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 8, 1, 12),
    _WlanRadiusAuthType_Type()
)
wlanRadiusAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanRadiusAuthType.setStatus("current")
_WlanCPTable_Object = MibTable
wlanCPTable = _WlanCPTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 9)
)
if mibBuilder.loadTexts:
    wlanCPTable.setStatus("current")
_WlanCPEntry_Object = MibTableRow
wlanCPEntry = _WlanCPEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 9, 1)
)
wlanCPEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-HWC-MIB", "wlanID"),
)
if mibBuilder.loadTexts:
    wlanCPEntry.setStatus("current")


class _WlanCPAuthType_Type(Integer32):
    """Custom type wlanCPAuthType based on Integer32"""
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
        *(("disabled", 1),
          ("dot1x", 3),
          ("easyGuestCP", 5),
          ("externalCP", 4),
          ("firewallFriendlyExCP", 7),
          ("guestSplash", 6),
          ("internalCP", 2))
    )


_WlanCPAuthType_Type.__name__ = "Integer32"
_WlanCPAuthType_Object = MibTableColumn
wlanCPAuthType = _WlanCPAuthType_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 9, 1, 1),
    _WlanCPAuthType_Type()
)
wlanCPAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanCPAuthType.setStatus("current")
_WlanCP802HttpRedirect_Type = TruthValue
_WlanCP802HttpRedirect_Object = MibTableColumn
wlanCP802HttpRedirect = _WlanCP802HttpRedirect_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 9, 1, 2),
    _WlanCP802HttpRedirect_Type()
)
wlanCP802HttpRedirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanCP802HttpRedirect.setStatus("current")
_WlanCPExtConnection_Type = IpAddress
_WlanCPExtConnection_Object = MibTableColumn
wlanCPExtConnection = _WlanCPExtConnection_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 9, 1, 3),
    _WlanCPExtConnection_Type()
)
wlanCPExtConnection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanCPExtConnection.setStatus("current")


class _WlanCPExtPort_Type(Unsigned32):
    """Custom type wlanCPExtPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32768, 65535),
    )


_WlanCPExtPort_Type.__name__ = "Unsigned32"
_WlanCPExtPort_Object = MibTableColumn
wlanCPExtPort = _WlanCPExtPort_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 9, 1, 4),
    _WlanCPExtPort_Type()
)
wlanCPExtPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanCPExtPort.setStatus("current")
_WlanCPExtEnableHttps_Type = TruthValue
_WlanCPExtEnableHttps_Object = MibTableColumn
wlanCPExtEnableHttps = _WlanCPExtEnableHttps_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 9, 1, 5),
    _WlanCPExtEnableHttps_Type()
)
wlanCPExtEnableHttps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanCPExtEnableHttps.setStatus("current")


class _WlanCPExtEncryption_Type(Integer32):
    """Custom type wlanCPExtEncryption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aes", 2),
          ("legacy", 1),
          ("none", 0))
    )


_WlanCPExtEncryption_Type.__name__ = "Integer32"
_WlanCPExtEncryption_Object = MibTableColumn
wlanCPExtEncryption = _WlanCPExtEncryption_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 9, 1, 6),
    _WlanCPExtEncryption_Type()
)
wlanCPExtEncryption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanCPExtEncryption.setStatus("current")


class _WlanCPExtSharedSecret_Type(OctetString):
    """Custom type wlanCPExtSharedSecret based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 64),
    )


_WlanCPExtSharedSecret_Type.__name__ = "OctetString"
_WlanCPExtSharedSecret_Object = MibTableColumn
wlanCPExtSharedSecret = _WlanCPExtSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 9, 1, 7),
    _WlanCPExtSharedSecret_Type()
)
wlanCPExtSharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanCPExtSharedSecret.setStatus("current")


class _WlanCPExtTosOverride_Type(TruthValue):
    """Custom type wlanCPExtTosOverride based on TruthValue"""


_WlanCPExtTosOverride_Object = MibTableColumn
wlanCPExtTosOverride = _WlanCPExtTosOverride_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 9, 1, 8),
    _WlanCPExtTosOverride_Type()
)
wlanCPExtTosOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanCPExtTosOverride.setStatus("current")


class _WlanCPExtTosValue_Type(Unsigned32):
    """Custom type wlanCPExtTosValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WlanCPExtTosValue_Type.__name__ = "Unsigned32"
_WlanCPExtTosValue_Object = MibTableColumn
wlanCPExtTosValue = _WlanCPExtTosValue_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 9, 1, 9),
    _WlanCPExtTosValue_Type()
)
wlanCPExtTosValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanCPExtTosValue.setStatus("deprecated")
_WlanCPExtAddIPtoURL_Type = TruthValue
_WlanCPExtAddIPtoURL_Object = MibTableColumn
wlanCPExtAddIPtoURL = _WlanCPExtAddIPtoURL_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 9, 1, 10),
    _WlanCPExtAddIPtoURL_Type()
)
wlanCPExtAddIPtoURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanCPExtAddIPtoURL.setStatus("current")
_WlanCPIntLogoffButton_Type = TruthValue
_WlanCPIntLogoffButton_Object = MibTableColumn
wlanCPIntLogoffButton = _WlanCPIntLogoffButton_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 9, 1, 11),
    _WlanCPIntLogoffButton_Type()
)
wlanCPIntLogoffButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanCPIntLogoffButton.setStatus("current")
_WlanCPIntStatusCheckButton_Type = TruthValue
_WlanCPIntStatusCheckButton_Object = MibTableColumn
wlanCPIntStatusCheckButton = _WlanCPIntStatusCheckButton_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 9, 1, 12),
    _WlanCPIntStatusCheckButton_Type()
)
wlanCPIntStatusCheckButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanCPIntStatusCheckButton.setStatus("current")
_WlanCPReplaceIPwithFQDN_Type = DisplayString
_WlanCPReplaceIPwithFQDN_Object = MibTableColumn
wlanCPReplaceIPwithFQDN = _WlanCPReplaceIPwithFQDN_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 9, 1, 13),
    _WlanCPReplaceIPwithFQDN_Type()
)
wlanCPReplaceIPwithFQDN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanCPReplaceIPwithFQDN.setStatus("current")


class _WlanCPSendLoginTo_Type(Integer32):
    """Custom type wlanCPSendLoginTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cpSessionPage", 1),
          ("customURL", 2),
          ("originalDestination", 0))
    )


_WlanCPSendLoginTo_Type.__name__ = "Integer32"
_WlanCPSendLoginTo_Object = MibTableColumn
wlanCPSendLoginTo = _WlanCPSendLoginTo_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 9, 1, 14),
    _WlanCPSendLoginTo_Type()
)
wlanCPSendLoginTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanCPSendLoginTo.setStatus("current")
_WlanCPRedirectURL_Type = DisplayString
_WlanCPRedirectURL_Object = MibTableColumn
wlanCPRedirectURL = _WlanCPRedirectURL_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 9, 1, 15),
    _WlanCPRedirectURL_Type()
)
wlanCPRedirectURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanCPRedirectURL.setStatus("current")
_WlanCPGuestAccLifetime_Type = Unsigned32
_WlanCPGuestAccLifetime_Object = MibTableColumn
wlanCPGuestAccLifetime = _WlanCPGuestAccLifetime_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 9, 1, 16),
    _WlanCPGuestAccLifetime_Type()
)
wlanCPGuestAccLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanCPGuestAccLifetime.setStatus("current")
if mibBuilder.loadTexts:
    wlanCPGuestAccLifetime.setUnits("days")
_WlanCPGuestAllowedLifetimeAcct_Type = TruthValue
_WlanCPGuestAllowedLifetimeAcct_Object = MibTableColumn
wlanCPGuestAllowedLifetimeAcct = _WlanCPGuestAllowedLifetimeAcct_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 9, 1, 17),
    _WlanCPGuestAllowedLifetimeAcct_Type()
)
wlanCPGuestAllowedLifetimeAcct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanCPGuestAllowedLifetimeAcct.setStatus("current")
_WlanCPGuestSessionLifetime_Type = Unsigned32
_WlanCPGuestSessionLifetime_Object = MibTableColumn
wlanCPGuestSessionLifetime = _WlanCPGuestSessionLifetime_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 9, 1, 18),
    _WlanCPGuestSessionLifetime_Type()
)
wlanCPGuestSessionLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanCPGuestSessionLifetime.setStatus("current")
if mibBuilder.loadTexts:
    wlanCPGuestSessionLifetime.setUnits("hours")
_WlanCPGuestIDPrefix_Type = DisplayString
_WlanCPGuestIDPrefix_Object = MibTableColumn
wlanCPGuestIDPrefix = _WlanCPGuestIDPrefix_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 9, 1, 19),
    _WlanCPGuestIDPrefix_Type()
)
wlanCPGuestIDPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanCPGuestIDPrefix.setStatus("current")


class _WlanCPGuestMinPassLength_Type(Unsigned32):
    """Custom type wlanCPGuestMinPassLength based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_WlanCPGuestMinPassLength_Type.__name__ = "Unsigned32"
_WlanCPGuestMinPassLength_Object = MibTableColumn
wlanCPGuestMinPassLength = _WlanCPGuestMinPassLength_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 9, 1, 20),
    _WlanCPGuestMinPassLength_Type()
)
wlanCPGuestMinPassLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanCPGuestMinPassLength.setStatus("current")


class _WlanCPGuestMaxConcurrentSession_Type(Unsigned32):
    """Custom type wlanCPGuestMaxConcurrentSession based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_WlanCPGuestMaxConcurrentSession_Type.__name__ = "Unsigned32"
_WlanCPGuestMaxConcurrentSession_Object = MibTableColumn
wlanCPGuestMaxConcurrentSession = _WlanCPGuestMaxConcurrentSession_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 9, 1, 21),
    _WlanCPGuestMaxConcurrentSession_Type()
)
wlanCPGuestMaxConcurrentSession.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanCPGuestMaxConcurrentSession.setStatus("current")
_WlanCPUseHTTPSforConnection_Type = TruthValue
_WlanCPUseHTTPSforConnection_Object = MibTableColumn
wlanCPUseHTTPSforConnection = _WlanCPUseHTTPSforConnection_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 9, 1, 22),
    _WlanCPUseHTTPSforConnection_Type()
)
wlanCPUseHTTPSforConnection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanCPUseHTTPSforConnection.setStatus("current")
_WlanCPIdentity_Type = DisplayString
_WlanCPIdentity_Object = MibTableColumn
wlanCPIdentity = _WlanCPIdentity_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 9, 1, 23),
    _WlanCPIdentity_Type()
)
wlanCPIdentity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanCPIdentity.setStatus("current")
_WlanCPCustomSpecificURL_Type = DisplayString
_WlanCPCustomSpecificURL_Object = MibTableColumn
wlanCPCustomSpecificURL = _WlanCPCustomSpecificURL_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 9, 1, 24),
    _WlanCPCustomSpecificURL_Type()
)
wlanCPCustomSpecificURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanCPCustomSpecificURL.setStatus("current")


class _WlanCPSelectionOption_Type(Bits):
    """Custom type wlanCPSelectionOption based on Bits"""
    namedValues = NamedValues(
        *(("addEWCPortAndIP", 0),
          ("apNameAndSerial", 1),
          ("associatedBSSID", 2),
          ("containmentVLAN", 6),
          ("currentlyAssignedRole", 5),
          ("signature", 8),
          ("ssid", 9),
          ("timeStamp", 7),
          ("userMacAddress", 4),
          ("vnsName", 3))
    )

_WlanCPSelectionOption_Type.__name__ = "Bits"
_WlanCPSelectionOption_Object = MibTableColumn
wlanCPSelectionOption = _WlanCPSelectionOption_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 9, 1, 25),
    _WlanCPSelectionOption_Type()
)
wlanCPSelectionOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanCPSelectionOption.setStatus("current")
_WlanUnsecuredWlanCounts_Type = Counter32
_WlanUnsecuredWlanCounts_Object = MibScalar
wlanUnsecuredWlanCounts = _WlanUnsecuredWlanCounts_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 10),
    _WlanUnsecuredWlanCounts_Type()
)
wlanUnsecuredWlanCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanUnsecuredWlanCounts.setStatus("current")
_WlanSecurityReportTable_Object = MibTable
wlanSecurityReportTable = _WlanSecurityReportTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 11)
)
if mibBuilder.loadTexts:
    wlanSecurityReportTable.setStatus("current")
_WlanSecurityReportEntry_Object = MibTableRow
wlanSecurityReportEntry = _WlanSecurityReportEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 11, 1)
)
wlanSecurityReportEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-HWC-MIB", "wlanID"),
)
if mibBuilder.loadTexts:
    wlanSecurityReportEntry.setStatus("current")


class _WlanSecurityReportFlag_Type(Integer32):
    """Custom type wlanSecurityReportFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("secureSetting", 2),
          ("unsecureSetting", 1))
    )


_WlanSecurityReportFlag_Type.__name__ = "Integer32"
_WlanSecurityReportFlag_Object = MibTableColumn
wlanSecurityReportFlag = _WlanSecurityReportFlag_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 11, 1, 1),
    _WlanSecurityReportFlag_Type()
)
wlanSecurityReportFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanSecurityReportFlag.setStatus("current")


class _WlanSecurityReportUnsecureType_Type(Bits):
    """Custom type wlanSecurityReportUnsecureType based on Bits"""
    namedValues = NamedValues(
        *(("defaultSsid", 3),
          ("dictionaryWordKey", 6),
          ("dictionaryWordSubstring", 7),
          ("hotspotSsid", 4),
          ("open", 0),
          ("passwordTooShort", 8),
          ("rainbowSsid", 5),
          ("tkip", 2),
          ("wep", 1))
    )

_WlanSecurityReportUnsecureType_Type.__name__ = "Bits"
_WlanSecurityReportUnsecureType_Object = MibTableColumn
wlanSecurityReportUnsecureType = _WlanSecurityReportUnsecureType_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 11, 1, 2),
    _WlanSecurityReportUnsecureType_Type()
)
wlanSecurityReportUnsecureType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanSecurityReportUnsecureType.setStatus("current")
_WlanSecurityReportNotes_Type = DisplayString
_WlanSecurityReportNotes_Object = MibTableColumn
wlanSecurityReportNotes = _WlanSecurityReportNotes_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 11, 1, 3),
    _WlanSecurityReportNotes_Type()
)
wlanSecurityReportNotes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanSecurityReportNotes.setStatus("current")
_WlanRadiusServerTable_Object = MibTable
wlanRadiusServerTable = _WlanRadiusServerTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 12)
)
if mibBuilder.loadTexts:
    wlanRadiusServerTable.setStatus("current")
_WlanRadiusServerEntry_Object = MibTableRow
wlanRadiusServerEntry = _WlanRadiusServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 12, 1)
)
wlanRadiusServerEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-HWC-MIB", "wlanID"),
    (0, "HIPATH-WIRELESS-HWC-MIB", "radiusId"),
)
if mibBuilder.loadTexts:
    wlanRadiusServerEntry.setStatus("current")
_RadiusId_Type = Unsigned32
_RadiusId_Object = MibTableColumn
radiusId = _RadiusId_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 12, 1, 1),
    _RadiusId_Type()
)
radiusId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    radiusId.setStatus("current")
_WlanRadiusServerName_Type = DisplayString
_WlanRadiusServerName_Object = MibTableColumn
wlanRadiusServerName = _WlanRadiusServerName_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 12, 1, 2),
    _WlanRadiusServerName_Type()
)
wlanRadiusServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlanRadiusServerName.setStatus("current")


class _WlanRadiusServerUse_Type(Integer32):
    """Custom type wlanRadiusServerUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notUse", 0),
          ("use", 1))
    )


_WlanRadiusServerUse_Type.__name__ = "Integer32"
_WlanRadiusServerUse_Object = MibTableColumn
wlanRadiusServerUse = _WlanRadiusServerUse_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 12, 1, 3),
    _WlanRadiusServerUse_Type()
)
wlanRadiusServerUse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanRadiusServerUse.setStatus("current")


class _WlanRadiusServerUsage_Type(Bits):
    """Custom type wlanRadiusServerUsage based on Bits"""
    namedValues = NamedValues(
        *(("acct", 2),
          ("auth", 0),
          ("mac", 1))
    )

_WlanRadiusServerUsage_Type.__name__ = "Bits"
_WlanRadiusServerUsage_Object = MibTableColumn
wlanRadiusServerUsage = _WlanRadiusServerUsage_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 12, 1, 4),
    _WlanRadiusServerUsage_Type()
)
wlanRadiusServerUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanRadiusServerUsage.setStatus("current")
_WlanRadiusServerAuthUseVNSIPAddr_Type = TruthValue
_WlanRadiusServerAuthUseVNSIPAddr_Object = MibTableColumn
wlanRadiusServerAuthUseVNSIPAddr = _WlanRadiusServerAuthUseVNSIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 12, 1, 5),
    _WlanRadiusServerAuthUseVNSIPAddr_Type()
)
wlanRadiusServerAuthUseVNSIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanRadiusServerAuthUseVNSIPAddr.setStatus("current")
_WlanRadiusServerAuthNASIP_Type = DisplayString
_WlanRadiusServerAuthNASIP_Object = MibTableColumn
wlanRadiusServerAuthNASIP = _WlanRadiusServerAuthNASIP_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 12, 1, 6),
    _WlanRadiusServerAuthNASIP_Type()
)
wlanRadiusServerAuthNASIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanRadiusServerAuthNASIP.setStatus("current")
_WlanRadiusServerAuthUseVNSName_Type = TruthValue
_WlanRadiusServerAuthUseVNSName_Object = MibTableColumn
wlanRadiusServerAuthUseVNSName = _WlanRadiusServerAuthUseVNSName_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 12, 1, 7),
    _WlanRadiusServerAuthUseVNSName_Type()
)
wlanRadiusServerAuthUseVNSName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanRadiusServerAuthUseVNSName.setStatus("current")
_WlanRadiusServerAuthNASId_Type = DisplayString
_WlanRadiusServerAuthNASId_Object = MibTableColumn
wlanRadiusServerAuthNASId = _WlanRadiusServerAuthNASId_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 12, 1, 8),
    _WlanRadiusServerAuthNASId_Type()
)
wlanRadiusServerAuthNASId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanRadiusServerAuthNASId.setStatus("current")


class _WlanRadiusServerAuthAuthType_Type(Integer32):
    """Custom type wlanRadiusServerAuthAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("chap", 1),
          ("eap", 4),
          ("mschap", 2),
          ("mschap2", 3),
          ("pap", 0))
    )


_WlanRadiusServerAuthAuthType_Type.__name__ = "Integer32"
_WlanRadiusServerAuthAuthType_Object = MibTableColumn
wlanRadiusServerAuthAuthType = _WlanRadiusServerAuthAuthType_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 12, 1, 9),
    _WlanRadiusServerAuthAuthType_Type()
)
wlanRadiusServerAuthAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanRadiusServerAuthAuthType.setStatus("current")
_WlanRadiusServerAcctUseVNSIPAddr_Type = TruthValue
_WlanRadiusServerAcctUseVNSIPAddr_Object = MibTableColumn
wlanRadiusServerAcctUseVNSIPAddr = _WlanRadiusServerAcctUseVNSIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 12, 1, 10),
    _WlanRadiusServerAcctUseVNSIPAddr_Type()
)
wlanRadiusServerAcctUseVNSIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanRadiusServerAcctUseVNSIPAddr.setStatus("current")
_WlanRadiusServerAcctNASIP_Type = DisplayString
_WlanRadiusServerAcctNASIP_Object = MibTableColumn
wlanRadiusServerAcctNASIP = _WlanRadiusServerAcctNASIP_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 12, 1, 11),
    _WlanRadiusServerAcctNASIP_Type()
)
wlanRadiusServerAcctNASIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanRadiusServerAcctNASIP.setStatus("current")
_WlanRadiusServerAcctUseVNSName_Type = TruthValue
_WlanRadiusServerAcctUseVNSName_Object = MibTableColumn
wlanRadiusServerAcctUseVNSName = _WlanRadiusServerAcctUseVNSName_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 12, 1, 12),
    _WlanRadiusServerAcctUseVNSName_Type()
)
wlanRadiusServerAcctUseVNSName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanRadiusServerAcctUseVNSName.setStatus("current")
_WlanRadiusServerAcctNASId_Type = DisplayString
_WlanRadiusServerAcctNASId_Object = MibTableColumn
wlanRadiusServerAcctNASId = _WlanRadiusServerAcctNASId_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 12, 1, 13),
    _WlanRadiusServerAcctNASId_Type()
)
wlanRadiusServerAcctNASId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanRadiusServerAcctNASId.setStatus("current")
_WlanRadiusServerAcctSIAR_Type = TruthValue
_WlanRadiusServerAcctSIAR_Object = MibTableColumn
wlanRadiusServerAcctSIAR = _WlanRadiusServerAcctSIAR_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 12, 1, 14),
    _WlanRadiusServerAcctSIAR_Type()
)
wlanRadiusServerAcctSIAR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanRadiusServerAcctSIAR.setStatus("current")
_WlanRadiusServerMacUseVNSIPAddr_Type = TruthValue
_WlanRadiusServerMacUseVNSIPAddr_Object = MibTableColumn
wlanRadiusServerMacUseVNSIPAddr = _WlanRadiusServerMacUseVNSIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 12, 1, 15),
    _WlanRadiusServerMacUseVNSIPAddr_Type()
)
wlanRadiusServerMacUseVNSIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanRadiusServerMacUseVNSIPAddr.setStatus("current")
_WlanRadiusServerMacNASIP_Type = DisplayString
_WlanRadiusServerMacNASIP_Object = MibTableColumn
wlanRadiusServerMacNASIP = _WlanRadiusServerMacNASIP_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 12, 1, 16),
    _WlanRadiusServerMacNASIP_Type()
)
wlanRadiusServerMacNASIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanRadiusServerMacNASIP.setStatus("current")
_WlanRadiusServerMacUseVNSName_Type = TruthValue
_WlanRadiusServerMacUseVNSName_Object = MibTableColumn
wlanRadiusServerMacUseVNSName = _WlanRadiusServerMacUseVNSName_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 12, 1, 17),
    _WlanRadiusServerMacUseVNSName_Type()
)
wlanRadiusServerMacUseVNSName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanRadiusServerMacUseVNSName.setStatus("current")
_WlanRadiusServerMacNASId_Type = DisplayString
_WlanRadiusServerMacNASId_Object = MibTableColumn
wlanRadiusServerMacNASId = _WlanRadiusServerMacNASId_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 12, 1, 18),
    _WlanRadiusServerMacNASId_Type()
)
wlanRadiusServerMacNASId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanRadiusServerMacNASId.setStatus("current")


class _WlanRadiusServerMacAuthType_Type(Integer32):
    """Custom type wlanRadiusServerMacAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("chap", 1),
          ("mschap", 2),
          ("mschap2", 3),
          ("pap", 0))
    )


_WlanRadiusServerMacAuthType_Type.__name__ = "Integer32"
_WlanRadiusServerMacAuthType_Object = MibTableColumn
wlanRadiusServerMacAuthType = _WlanRadiusServerMacAuthType_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 12, 1, 19),
    _WlanRadiusServerMacAuthType_Type()
)
wlanRadiusServerMacAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanRadiusServerMacAuthType.setStatus("current")
_WlanRadiusServerMacPW_Type = DisplayString
_WlanRadiusServerMacPW_Object = MibTableColumn
wlanRadiusServerMacPW = _WlanRadiusServerMacPW_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 3, 4, 12, 1, 20),
    _WlanRadiusServerMacPW_Type()
)
wlanRadiusServerMacPW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wlanRadiusServerMacPW.setStatus("current")
_Topology_ObjectIdentity = ObjectIdentity
topology = _Topology_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4)
)
_TopologyConfig_ObjectIdentity = ObjectIdentity
topologyConfig = _TopologyConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 1)
)
_TopologyTable_Object = MibTable
topologyTable = _TopologyTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 1, 1)
)
if mibBuilder.loadTexts:
    topologyTable.setStatus("current")
_TopologyEntry_Object = MibTableRow
topologyEntry = _TopologyEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 1, 1, 1)
)
topologyEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-HWC-MIB", "topologyID"),
)
if mibBuilder.loadTexts:
    topologyEntry.setStatus("current")
_TopologyID_Type = Unsigned32
_TopologyID_Object = MibTableColumn
topologyID = _TopologyID_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 1, 1, 1, 1),
    _TopologyID_Type()
)
topologyID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    topologyID.setStatus("current")
_TopologyName_Type = DisplayString
_TopologyName_Object = MibTableColumn
topologyName = _TopologyName_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 1, 1, 1, 2),
    _TopologyName_Type()
)
topologyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    topologyName.setStatus("current")


class _TopologyMode_Type(Integer32):
    """Custom type topologyMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("bridgedAtAC", 2),
          ("bridgedAtAP", 1),
          ("management", 6),
          ("physical", 5),
          ("routed", 0),
          ("thirdPartyAP", 4),
          ("undefined", -1))
    )


_TopologyMode_Type.__name__ = "Integer32"
_TopologyMode_Object = MibTableColumn
topologyMode = _TopologyMode_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 1, 1, 1, 3),
    _TopologyMode_Type()
)
topologyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    topologyMode.setStatus("current")


class _TopologyTagged_Type(Integer32):
    """Custom type topologyTagged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tagged", 1),
          ("untagged", 2))
    )


_TopologyTagged_Type.__name__ = "Integer32"
_TopologyTagged_Object = MibTableColumn
topologyTagged = _TopologyTagged_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 1, 1, 1, 4),
    _TopologyTagged_Type()
)
topologyTagged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    topologyTagged.setStatus("current")


class _TopologyVlanID_Type(Integer32):
    """Custom type topologyVlanID based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 4095),
    )


_TopologyVlanID_Type.__name__ = "Integer32"
_TopologyVlanID_Object = MibTableColumn
topologyVlanID = _TopologyVlanID_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 1, 1, 1, 5),
    _TopologyVlanID_Type()
)
topologyVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    topologyVlanID.setStatus("current")


class _TopologyEgressPort_Type(OctetString):
    """Custom type topologyEgressPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_TopologyEgressPort_Type.__name__ = "OctetString"
_TopologyEgressPort_Object = MibTableColumn
topologyEgressPort = _TopologyEgressPort_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 1, 1, 1, 6),
    _TopologyEgressPort_Type()
)
topologyEgressPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    topologyEgressPort.setStatus("current")
_TopologyLayer3_Type = TruthValue
_TopologyLayer3_Object = MibTableColumn
topologyLayer3 = _TopologyLayer3_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 1, 1, 1, 7),
    _TopologyLayer3_Type()
)
topologyLayer3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    topologyLayer3.setStatus("current")
_TopologyIPAddress_Type = IpAddress
_TopologyIPAddress_Object = MibTableColumn
topologyIPAddress = _TopologyIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 1, 1, 1, 8),
    _TopologyIPAddress_Type()
)
topologyIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    topologyIPAddress.setStatus("current")
_TopologyIPMask_Type = IpAddress
_TopologyIPMask_Object = MibTableColumn
topologyIPMask = _TopologyIPMask_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 1, 1, 1, 9),
    _TopologyIPMask_Type()
)
topologyIPMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    topologyIPMask.setStatus("current")


class _TopologyMTUsize_Type(Unsigned32):
    """Custom type topologyMTUsize based on Unsigned32"""
    defaultValue = 1436


_TopologyMTUsize_Object = MibTableColumn
topologyMTUsize = _TopologyMTUsize_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 1, 1, 1, 10),
    _TopologyMTUsize_Type()
)
topologyMTUsize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    topologyMTUsize.setStatus("current")
_TopologyGateway_Type = IpAddress
_TopologyGateway_Object = MibTableColumn
topologyGateway = _TopologyGateway_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 1, 1, 1, 11),
    _TopologyGateway_Type()
)
topologyGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    topologyGateway.setStatus("current")


class _TopologyDHCPUsage_Type(Integer32):
    """Custom type topologyDHCPUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("localServer", 2),
          ("none", 0),
          ("useRelay", 1))
    )


_TopologyDHCPUsage_Type.__name__ = "Integer32"
_TopologyDHCPUsage_Object = MibTableColumn
topologyDHCPUsage = _TopologyDHCPUsage_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 1, 1, 1, 12),
    _TopologyDHCPUsage_Type()
)
topologyDHCPUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    topologyDHCPUsage.setStatus("current")
_TopologyAPRegistration_Type = TruthValue
_TopologyAPRegistration_Object = MibTableColumn
topologyAPRegistration = _TopologyAPRegistration_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 1, 1, 1, 13),
    _TopologyAPRegistration_Type()
)
topologyAPRegistration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    topologyAPRegistration.setStatus("current")
_TopologyManagementTraffic_Type = TruthValue
_TopologyManagementTraffic_Object = MibTableColumn
topologyManagementTraffic = _TopologyManagementTraffic_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 1, 1, 1, 14),
    _TopologyManagementTraffic_Type()
)
topologyManagementTraffic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    topologyManagementTraffic.setStatus("current")
_TopologySynchronize_Type = TruthValue
_TopologySynchronize_Object = MibTableColumn
topologySynchronize = _TopologySynchronize_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 1, 1, 1, 15),
    _TopologySynchronize_Type()
)
topologySynchronize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    topologySynchronize.setStatus("current")
_TopologySyncGateway_Type = IpAddress
_TopologySyncGateway_Object = MibTableColumn
topologySyncGateway = _TopologySyncGateway_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 1, 1, 1, 16),
    _TopologySyncGateway_Type()
)
topologySyncGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    topologySyncGateway.setStatus("current")
_TopologySyncMask_Type = IpAddress
_TopologySyncMask_Object = MibTableColumn
topologySyncMask = _TopologySyncMask_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 1, 1, 1, 17),
    _TopologySyncMask_Type()
)
topologySyncMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    topologySyncMask.setStatus("current")
_TopologySyncIPStart_Type = IpAddress
_TopologySyncIPStart_Object = MibTableColumn
topologySyncIPStart = _TopologySyncIPStart_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 1, 1, 1, 18),
    _TopologySyncIPStart_Type()
)
topologySyncIPStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    topologySyncIPStart.setStatus("current")
_TopologySyncIPEnd_Type = IpAddress
_TopologySyncIPEnd_Object = MibTableColumn
topologySyncIPEnd = _TopologySyncIPEnd_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 1, 1, 1, 19),
    _TopologySyncIPEnd_Type()
)
topologySyncIPEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    topologySyncIPEnd.setStatus("current")
_TopologyStaticIPv6Address_Type = DisplayString
_TopologyStaticIPv6Address_Object = MibTableColumn
topologyStaticIPv6Address = _TopologyStaticIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 1, 1, 1, 20),
    _TopologyStaticIPv6Address_Type()
)
topologyStaticIPv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    topologyStaticIPv6Address.setStatus("current")
_TopologyLinkLocalIPv6Address_Type = DisplayString
_TopologyLinkLocalIPv6Address_Object = MibTableColumn
topologyLinkLocalIPv6Address = _TopologyLinkLocalIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 1, 1, 1, 21),
    _TopologyLinkLocalIPv6Address_Type()
)
topologyLinkLocalIPv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topologyLinkLocalIPv6Address.setStatus("current")
_TopologyPreFixLength_Type = Unsigned32
_TopologyPreFixLength_Object = MibTableColumn
topologyPreFixLength = _TopologyPreFixLength_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 1, 1, 1, 22),
    _TopologyPreFixLength_Type()
)
topologyPreFixLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    topologyPreFixLength.setStatus("current")
_TopologyIPv6Gateway_Type = DisplayString
_TopologyIPv6Gateway_Object = MibTableColumn
topologyIPv6Gateway = _TopologyIPv6Gateway_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 1, 1, 1, 23),
    _TopologyIPv6Gateway_Type()
)
topologyIPv6Gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    topologyIPv6Gateway.setStatus("current")


class _TopologyDynamicEgress_Type(Integer32):
    """Custom type topologyDynamicEgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TopologyDynamicEgress_Type.__name__ = "Integer32"
_TopologyDynamicEgress_Object = MibTableColumn
topologyDynamicEgress = _TopologyDynamicEgress_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 1, 1, 1, 24),
    _TopologyDynamicEgress_Type()
)
topologyDynamicEgress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    topologyDynamicEgress.setStatus("current")


class _TopologyIsGroup_Type(Integer32):
    """Custom type topologyIsGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_TopologyIsGroup_Type.__name__ = "Integer32"
_TopologyIsGroup_Object = MibTableColumn
topologyIsGroup = _TopologyIsGroup_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 1, 1, 1, 25),
    _TopologyIsGroup_Type()
)
topologyIsGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    topologyIsGroup.setStatus("current")


class _TopologyGroupMembers_Type(OctetString):
    """Custom type topologyGroupMembers based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_TopologyGroupMembers_Type.__name__ = "OctetString"
_TopologyGroupMembers_Object = MibTableColumn
topologyGroupMembers = _TopologyGroupMembers_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 1, 1, 1, 26),
    _TopologyGroupMembers_Type()
)
topologyGroupMembers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    topologyGroupMembers.setStatus("current")
_TopologyMemberId_Type = Integer32
_TopologyMemberId_Object = MibTableColumn
topologyMemberId = _TopologyMemberId_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 1, 1, 1, 27),
    _TopologyMemberId_Type()
)
topologyMemberId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    topologyMemberId.setStatus("current")
_TopologyStat_ObjectIdentity = ObjectIdentity
topologyStat = _TopologyStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 2)
)
_TopoStatTable_Object = MibTable
topoStatTable = _TopoStatTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 2, 1)
)
if mibBuilder.loadTexts:
    topoStatTable.setStatus("current")
_TopoStatEntry_Object = MibTableRow
topoStatEntry = _TopoStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 2, 1, 1)
)
topoStatEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-HWC-MIB", "topologyID"),
)
if mibBuilder.loadTexts:
    topoStatEntry.setStatus("current")
_TopoStatName_Type = DisplayString
_TopoStatName_Object = MibTableColumn
topoStatName = _TopoStatName_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 2, 1, 1, 1),
    _TopoStatName_Type()
)
topoStatName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoStatName.setStatus("current")
_TopoStatTxPkts_Type = Counter64
_TopoStatTxPkts_Object = MibTableColumn
topoStatTxPkts = _TopoStatTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 2, 1, 1, 2),
    _TopoStatTxPkts_Type()
)
topoStatTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoStatTxPkts.setStatus("current")
_TopoStatRxPkts_Type = Counter64
_TopoStatRxPkts_Object = MibTableColumn
topoStatRxPkts = _TopoStatRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 2, 1, 1, 3),
    _TopoStatRxPkts_Type()
)
topoStatRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoStatRxPkts.setStatus("current")
_TopoStatTxOctets_Type = Counter64
_TopoStatTxOctets_Object = MibTableColumn
topoStatTxOctets = _TopoStatTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 2, 1, 1, 4),
    _TopoStatTxOctets_Type()
)
topoStatTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoStatTxOctets.setStatus("current")
_TopoStatRxOctets_Type = Counter64
_TopoStatRxOctets_Object = MibTableColumn
topoStatRxOctets = _TopoStatRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 2, 1, 1, 5),
    _TopoStatRxOctets_Type()
)
topoStatRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoStatRxOctets.setStatus("current")
_TopoStatMulticastTxPkts_Type = Counter64
_TopoStatMulticastTxPkts_Object = MibTableColumn
topoStatMulticastTxPkts = _TopoStatMulticastTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 2, 1, 1, 6),
    _TopoStatMulticastTxPkts_Type()
)
topoStatMulticastTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoStatMulticastTxPkts.setStatus("current")
_TopoStatMulticastRxPkts_Type = Counter64
_TopoStatMulticastRxPkts_Object = MibTableColumn
topoStatMulticastRxPkts = _TopoStatMulticastRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 2, 1, 1, 7),
    _TopoStatMulticastRxPkts_Type()
)
topoStatMulticastRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoStatMulticastRxPkts.setStatus("current")
_TopoStatBroadcastTxPkts_Type = Counter64
_TopoStatBroadcastTxPkts_Object = MibTableColumn
topoStatBroadcastTxPkts = _TopoStatBroadcastTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 2, 1, 1, 8),
    _TopoStatBroadcastTxPkts_Type()
)
topoStatBroadcastTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoStatBroadcastTxPkts.setStatus("current")
_TopoStatBroadcastRxPkts_Type = Counter64
_TopoStatBroadcastRxPkts_Object = MibTableColumn
topoStatBroadcastRxPkts = _TopoStatBroadcastRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 2, 1, 1, 9),
    _TopoStatBroadcastRxPkts_Type()
)
topoStatBroadcastRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoStatBroadcastRxPkts.setStatus("current")
_TopoStatFrameChkSeqErrors_Type = Counter64
_TopoStatFrameChkSeqErrors_Object = MibTableColumn
topoStatFrameChkSeqErrors = _TopoStatFrameChkSeqErrors_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 2, 1, 1, 10),
    _TopoStatFrameChkSeqErrors_Type()
)
topoStatFrameChkSeqErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoStatFrameChkSeqErrors.setStatus("current")
_TopoStatFrameTooLongErrors_Type = Counter64
_TopoStatFrameTooLongErrors_Object = MibTableColumn
topoStatFrameTooLongErrors = _TopoStatFrameTooLongErrors_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 2, 1, 1, 11),
    _TopoStatFrameTooLongErrors_Type()
)
topoStatFrameTooLongErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoStatFrameTooLongErrors.setStatus("current")
_TopoExceptionStatTable_Object = MibTable
topoExceptionStatTable = _TopoExceptionStatTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 2, 2)
)
if mibBuilder.loadTexts:
    topoExceptionStatTable.setStatus("current")
_TopoExceptionStatEntry_Object = MibTableRow
topoExceptionStatEntry = _TopoExceptionStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 2, 2, 1)
)
topoExceptionStatEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-HWC-MIB", "topologyID"),
)
if mibBuilder.loadTexts:
    topoExceptionStatEntry.setStatus("current")


class _TopoExceptionFiterName_Type(OctetString):
    """Custom type topoExceptionFiterName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_TopoExceptionFiterName_Type.__name__ = "OctetString"
_TopoExceptionFiterName_Object = MibTableColumn
topoExceptionFiterName = _TopoExceptionFiterName_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 2, 2, 1, 1),
    _TopoExceptionFiterName_Type()
)
topoExceptionFiterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    topoExceptionFiterName.setStatus("current")
_TopoExceptionStatPktsDenied_Type = Counter64
_TopoExceptionStatPktsDenied_Object = MibTableColumn
topoExceptionStatPktsDenied = _TopoExceptionStatPktsDenied_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 2, 2, 1, 2),
    _TopoExceptionStatPktsDenied_Type()
)
topoExceptionStatPktsDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoExceptionStatPktsDenied.setStatus("current")
_TopoExceptionStatPktsAllowed_Type = Counter64
_TopoExceptionStatPktsAllowed_Object = MibTableColumn
topoExceptionStatPktsAllowed = _TopoExceptionStatPktsAllowed_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 2, 2, 1, 3),
    _TopoExceptionStatPktsAllowed_Type()
)
topoExceptionStatPktsAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoExceptionStatPktsAllowed.setStatus("current")
_TopoWireStatTable_Object = MibTable
topoWireStatTable = _TopoWireStatTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 2, 3)
)
if mibBuilder.loadTexts:
    topoWireStatTable.setStatus("deprecated")
_TopoWireStatEntry_Object = MibTableRow
topoWireStatEntry = _TopoWireStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 2, 3, 1)
)
topoWireStatEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-HWC-MIB", "topologyID"),
)
if mibBuilder.loadTexts:
    topoWireStatEntry.setStatus("deprecated")
_TopoWireStatName_Type = DisplayString
_TopoWireStatName_Object = MibTableColumn
topoWireStatName = _TopoWireStatName_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 2, 3, 1, 1),
    _TopoWireStatName_Type()
)
topoWireStatName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoWireStatName.setStatus("deprecated")
_TopoWireStatTxPkts_Type = Counter64
_TopoWireStatTxPkts_Object = MibTableColumn
topoWireStatTxPkts = _TopoWireStatTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 2, 3, 1, 2),
    _TopoWireStatTxPkts_Type()
)
topoWireStatTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoWireStatTxPkts.setStatus("deprecated")
_TopoWireStatRxPkts_Type = Counter64
_TopoWireStatRxPkts_Object = MibTableColumn
topoWireStatRxPkts = _TopoWireStatRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 2, 3, 1, 3),
    _TopoWireStatRxPkts_Type()
)
topoWireStatRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoWireStatRxPkts.setStatus("deprecated")
_TopoWireStatTxOctets_Type = Counter64
_TopoWireStatTxOctets_Object = MibTableColumn
topoWireStatTxOctets = _TopoWireStatTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 2, 3, 1, 4),
    _TopoWireStatTxOctets_Type()
)
topoWireStatTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoWireStatTxOctets.setStatus("deprecated")
_TopoWireStatRxOctets_Type = Counter64
_TopoWireStatRxOctets_Object = MibTableColumn
topoWireStatRxOctets = _TopoWireStatRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 2, 3, 1, 5),
    _TopoWireStatRxOctets_Type()
)
topoWireStatRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoWireStatRxOctets.setStatus("deprecated")
_TopoWireStatMulticastTxPkts_Type = Counter64
_TopoWireStatMulticastTxPkts_Object = MibTableColumn
topoWireStatMulticastTxPkts = _TopoWireStatMulticastTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 2, 3, 1, 6),
    _TopoWireStatMulticastTxPkts_Type()
)
topoWireStatMulticastTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoWireStatMulticastTxPkts.setStatus("deprecated")
_TopoWireStatMulticastRxPkts_Type = Counter64
_TopoWireStatMulticastRxPkts_Object = MibTableColumn
topoWireStatMulticastRxPkts = _TopoWireStatMulticastRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 2, 3, 1, 7),
    _TopoWireStatMulticastRxPkts_Type()
)
topoWireStatMulticastRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoWireStatMulticastRxPkts.setStatus("deprecated")
_TopoWireStatBroadcastTxPkts_Type = Counter64
_TopoWireStatBroadcastTxPkts_Object = MibTableColumn
topoWireStatBroadcastTxPkts = _TopoWireStatBroadcastTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 2, 3, 1, 8),
    _TopoWireStatBroadcastTxPkts_Type()
)
topoWireStatBroadcastTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoWireStatBroadcastTxPkts.setStatus("deprecated")
_TopoWireStatBroadcastRxPkts_Type = Counter64
_TopoWireStatBroadcastRxPkts_Object = MibTableColumn
topoWireStatBroadcastRxPkts = _TopoWireStatBroadcastRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 2, 3, 1, 9),
    _TopoWireStatBroadcastRxPkts_Type()
)
topoWireStatBroadcastRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoWireStatBroadcastRxPkts.setStatus("deprecated")
_TopoWireStatFrameChkSeqErrors_Type = Counter64
_TopoWireStatFrameChkSeqErrors_Object = MibTableColumn
topoWireStatFrameChkSeqErrors = _TopoWireStatFrameChkSeqErrors_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 2, 3, 1, 10),
    _TopoWireStatFrameChkSeqErrors_Type()
)
topoWireStatFrameChkSeqErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoWireStatFrameChkSeqErrors.setStatus("deprecated")
_TopoWireStatFrameTooLongErrors_Type = Counter64
_TopoWireStatFrameTooLongErrors_Object = MibTableColumn
topoWireStatFrameTooLongErrors = _TopoWireStatFrameTooLongErrors_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 2, 3, 1, 11),
    _TopoWireStatFrameTooLongErrors_Type()
)
topoWireStatFrameTooLongErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoWireStatFrameTooLongErrors.setStatus("deprecated")
_TopoCompleteStatTable_Object = MibTable
topoCompleteStatTable = _TopoCompleteStatTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 2, 4)
)
if mibBuilder.loadTexts:
    topoCompleteStatTable.setStatus("current")
_TopoCompleteStatEntry_Object = MibTableRow
topoCompleteStatEntry = _TopoCompleteStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 2, 4, 1)
)
topoCompleteStatEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-HWC-MIB", "topologyID"),
)
if mibBuilder.loadTexts:
    topoCompleteStatEntry.setStatus("current")
_TopoCompleteStatName_Type = DisplayString
_TopoCompleteStatName_Object = MibTableColumn
topoCompleteStatName = _TopoCompleteStatName_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 2, 4, 1, 1),
    _TopoCompleteStatName_Type()
)
topoCompleteStatName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoCompleteStatName.setStatus("current")
_TopoCompleteStatTxPkts_Type = Counter64
_TopoCompleteStatTxPkts_Object = MibTableColumn
topoCompleteStatTxPkts = _TopoCompleteStatTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 2, 4, 1, 2),
    _TopoCompleteStatTxPkts_Type()
)
topoCompleteStatTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoCompleteStatTxPkts.setStatus("current")
_TopoCompleteStatRxPkts_Type = Counter64
_TopoCompleteStatRxPkts_Object = MibTableColumn
topoCompleteStatRxPkts = _TopoCompleteStatRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 2, 4, 1, 3),
    _TopoCompleteStatRxPkts_Type()
)
topoCompleteStatRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoCompleteStatRxPkts.setStatus("current")
_TopoCompleteStatTxOctets_Type = Counter64
_TopoCompleteStatTxOctets_Object = MibTableColumn
topoCompleteStatTxOctets = _TopoCompleteStatTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 2, 4, 1, 4),
    _TopoCompleteStatTxOctets_Type()
)
topoCompleteStatTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoCompleteStatTxOctets.setStatus("current")
_TopoCompleteStatRxOctets_Type = Counter64
_TopoCompleteStatRxOctets_Object = MibTableColumn
topoCompleteStatRxOctets = _TopoCompleteStatRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 2, 4, 1, 5),
    _TopoCompleteStatRxOctets_Type()
)
topoCompleteStatRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoCompleteStatRxOctets.setStatus("current")
_TopoCompleteStatMulticastTxPkts_Type = Counter64
_TopoCompleteStatMulticastTxPkts_Object = MibTableColumn
topoCompleteStatMulticastTxPkts = _TopoCompleteStatMulticastTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 2, 4, 1, 6),
    _TopoCompleteStatMulticastTxPkts_Type()
)
topoCompleteStatMulticastTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoCompleteStatMulticastTxPkts.setStatus("current")
_TopoCompleteStatMulticastRxPkts_Type = Counter64
_TopoCompleteStatMulticastRxPkts_Object = MibTableColumn
topoCompleteStatMulticastRxPkts = _TopoCompleteStatMulticastRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 2, 4, 1, 7),
    _TopoCompleteStatMulticastRxPkts_Type()
)
topoCompleteStatMulticastRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoCompleteStatMulticastRxPkts.setStatus("current")
_TopoCompleteStatBroadcastTxPkts_Type = Counter64
_TopoCompleteStatBroadcastTxPkts_Object = MibTableColumn
topoCompleteStatBroadcastTxPkts = _TopoCompleteStatBroadcastTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 2, 4, 1, 8),
    _TopoCompleteStatBroadcastTxPkts_Type()
)
topoCompleteStatBroadcastTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoCompleteStatBroadcastTxPkts.setStatus("current")
_TopoCompleteStatBroadcastRxPkts_Type = Counter64
_TopoCompleteStatBroadcastRxPkts_Object = MibTableColumn
topoCompleteStatBroadcastRxPkts = _TopoCompleteStatBroadcastRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 2, 4, 1, 9),
    _TopoCompleteStatBroadcastRxPkts_Type()
)
topoCompleteStatBroadcastRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoCompleteStatBroadcastRxPkts.setStatus("current")
_TopoCompleteStatFrameChkSeqErrors_Type = Counter64
_TopoCompleteStatFrameChkSeqErrors_Object = MibTableColumn
topoCompleteStatFrameChkSeqErrors = _TopoCompleteStatFrameChkSeqErrors_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 2, 4, 1, 10),
    _TopoCompleteStatFrameChkSeqErrors_Type()
)
topoCompleteStatFrameChkSeqErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoCompleteStatFrameChkSeqErrors.setStatus("current")
_TopoCompleteStatFrameTooLongErrors_Type = Counter64
_TopoCompleteStatFrameTooLongErrors_Object = MibTableColumn
topoCompleteStatFrameTooLongErrors = _TopoCompleteStatFrameTooLongErrors_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 4, 2, 4, 1, 11),
    _TopoCompleteStatFrameTooLongErrors_Type()
)
topoCompleteStatFrameTooLongErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topoCompleteStatFrameTooLongErrors.setStatus("current")
_AccessPoints_ObjectIdentity = ObjectIdentity
accessPoints = _AccessPoints_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5)
)
_ApConfigObjects_ObjectIdentity = ObjectIdentity
apConfigObjects = _ApConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 1)
)
_ApCount_Type = Integer32
_ApCount_Object = MibScalar
apCount = _ApCount_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 1, 1),
    _ApCount_Type()
)
apCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCount.setStatus("current")
_ApTable_Object = MibTable
apTable = _ApTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 1, 2)
)
if mibBuilder.loadTexts:
    apTable.setStatus("current")
_ApEntry_Object = MibTableRow
apEntry = _ApEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 1, 2, 1)
)
apEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-HWC-MIB", "apIndex"),
)
if mibBuilder.loadTexts:
    apEntry.setStatus("current")


class _ApIndex_Type(Integer32):
    """Custom type apIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ApIndex_Type.__name__ = "Integer32"
_ApIndex_Object = MibTableColumn
apIndex = _ApIndex_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 1, 2, 1, 1),
    _ApIndex_Type()
)
apIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIndex.setStatus("current")
_ApName_Type = DisplayString
_ApName_Object = MibTableColumn
apName = _ApName_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 1, 2, 1, 2),
    _ApName_Type()
)
apName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apName.setStatus("current")
_ApDesc_Type = DisplayString
_ApDesc_Object = MibTableColumn
apDesc = _ApDesc_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 1, 2, 1, 3),
    _ApDesc_Type()
)
apDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apDesc.setStatus("current")


class _ApSerialNumber_Type(OctetString):
    """Custom type apSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_ApSerialNumber_Type.__name__ = "OctetString"
_ApSerialNumber_Object = MibTableColumn
apSerialNumber = _ApSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 1, 2, 1, 4),
    _ApSerialNumber_Type()
)
apSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSerialNumber.setStatus("current")
_ApPortifIndex_Type = InterfaceIndex
_ApPortifIndex_Object = MibTableColumn
apPortifIndex = _ApPortifIndex_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 1, 2, 1, 5),
    _ApPortifIndex_Type()
)
apPortifIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apPortifIndex.setStatus("current")
_ApWiredIfIndex_Type = InterfaceIndex
_ApWiredIfIndex_Object = MibTableColumn
apWiredIfIndex = _ApWiredIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 1, 2, 1, 6),
    _ApWiredIfIndex_Type()
)
apWiredIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWiredIfIndex.setStatus("current")
_ApSoftwareVersion_Type = OctetString
_ApSoftwareVersion_Object = MibTableColumn
apSoftwareVersion = _ApSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 1, 2, 1, 7),
    _ApSoftwareVersion_Type()
)
apSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSoftwareVersion.setStatus("current")
_ApSpecific_Type = ObjectIdentifier
_ApSpecific_Object = MibTableColumn
apSpecific = _ApSpecific_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 1, 2, 1, 8),
    _ApSpecific_Type()
)
apSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSpecific.setStatus("current")
_ApBroadcastDisassociate_Type = TruthValue
_ApBroadcastDisassociate_Object = MibTableColumn
apBroadcastDisassociate = _ApBroadcastDisassociate_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 1, 2, 1, 9),
    _ApBroadcastDisassociate_Type()
)
apBroadcastDisassociate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBroadcastDisassociate.setStatus("current")
_ApRowStatus_Type = RowStatus
_ApRowStatus_Object = MibTableColumn
apRowStatus = _ApRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 1, 2, 1, 10),
    _ApRowStatus_Type()
)
apRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRowStatus.setStatus("current")


class _ApVlanID_Type(Integer32):
    """Custom type apVlanID based on Integer32"""
    defaultValue = -1


_ApVlanID_Object = MibTableColumn
apVlanID = _ApVlanID_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 1, 2, 1, 11),
    _ApVlanID_Type()
)
apVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apVlanID.setStatus("current")


class _ApIpAssignmentType_Type(Integer32):
    """Custom type apIpAssignmentType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dhcp", 1),
          ("static", 2))
    )


_ApIpAssignmentType_Type.__name__ = "Integer32"
_ApIpAssignmentType_Object = MibTableColumn
apIpAssignmentType = _ApIpAssignmentType_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 1, 2, 1, 12),
    _ApIpAssignmentType_Type()
)
apIpAssignmentType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIpAssignmentType.setStatus("current")
_ApIfMAC_Type = MacAddress
_ApIfMAC_Object = MibTableColumn
apIfMAC = _ApIfMAC_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 1, 2, 1, 13),
    _ApIfMAC_Type()
)
apIfMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIfMAC.setStatus("current")
_ApIPAddress_Type = IpAddress
_ApIPAddress_Object = MibTableColumn
apIPAddress = _ApIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 1, 2, 1, 14),
    _ApIPAddress_Type()
)
apIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIPAddress.setStatus("current")
_ApHwVersion_Type = DisplayString
_ApHwVersion_Object = MibTableColumn
apHwVersion = _ApHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 1, 2, 1, 17),
    _ApHwVersion_Type()
)
apHwVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apHwVersion.setStatus("current")
_ApSwVersion_Type = DisplayString
_ApSwVersion_Object = MibTableColumn
apSwVersion = _ApSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 1, 2, 1, 18),
    _ApSwVersion_Type()
)
apSwVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSwVersion.setStatus("current")


class _ApEnvironment_Type(Integer32):
    """Custom type apEnvironment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("indoor", 1),
          ("outdoor", 2))
    )


_ApEnvironment_Type.__name__ = "Integer32"
_ApEnvironment_Object = MibTableColumn
apEnvironment = _ApEnvironment_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 1, 2, 1, 19),
    _ApEnvironment_Type()
)
apEnvironment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apEnvironment.setStatus("current")


class _ApHome_Type(Integer32):
    """Custom type apHome based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("foreign", 2),
          ("local", 1))
    )


_ApHome_Type.__name__ = "Integer32"
_ApHome_Object = MibTableColumn
apHome = _ApHome_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 1, 2, 1, 20),
    _ApHome_Type()
)
apHome.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apHome.setStatus("current")


class _ApRole_Type(Integer32):
    """Custom type apRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accessPoint", 1),
          ("guardian", 3),
          ("sensor", 2))
    )


_ApRole_Type.__name__ = "Integer32"
_ApRole_Object = MibTableColumn
apRole = _ApRole_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 1, 2, 1, 21),
    _ApRole_Type()
)
apRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRole.setStatus("current")


class _ApState_Type(Integer32):
    """Custom type apState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_ApState_Type.__name__ = "Integer32"
_ApState_Object = MibTableColumn
apState = _ApState_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 1, 2, 1, 22),
    _ApState_Type()
)
apState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apState.setStatus("current")


class _ApStatus_Type(Integer32):
    """Custom type apStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("approved", 1),
          ("pending", 2))
    )


_ApStatus_Type.__name__ = "Integer32"
_ApStatus_Object = MibTableColumn
apStatus = _ApStatus_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 1, 2, 1, 23),
    _ApStatus_Type()
)
apStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apStatus.setStatus("current")


class _ApPollTimeout_Type(Gauge32):
    """Custom type apPollTimeout based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 3600),
    )


_ApPollTimeout_Type.__name__ = "Gauge32"
_ApPollTimeout_Object = MibTableColumn
apPollTimeout = _ApPollTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 1, 2, 1, 24),
    _ApPollTimeout_Type()
)
apPollTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apPollTimeout.setStatus("current")
_ApPollInterval_Type = Gauge32
_ApPollInterval_Object = MibTableColumn
apPollInterval = _ApPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 1, 2, 1, 25),
    _ApPollInterval_Type()
)
apPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apPollInterval.setStatus("current")


class _ApTelnetAccess_Type(Integer32):
    """Custom type apTelnetAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("na", 3))
    )


_ApTelnetAccess_Type.__name__ = "Integer32"
_ApTelnetAccess_Object = MibTableColumn
apTelnetAccess = _ApTelnetAccess_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 1, 2, 1, 26),
    _ApTelnetAccess_Type()
)
apTelnetAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apTelnetAccess.setStatus("current")
_ApMaintainClientSession_Type = TruthValue
_ApMaintainClientSession_Object = MibTableColumn
apMaintainClientSession = _ApMaintainClientSession_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 1, 2, 1, 27),
    _ApMaintainClientSession_Type()
)
apMaintainClientSession.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apMaintainClientSession.setStatus("current")
_ApRestartServiceContAbsent_Type = TruthValue
_ApRestartServiceContAbsent_Object = MibTableColumn
apRestartServiceContAbsent = _ApRestartServiceContAbsent_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 1, 2, 1, 28),
    _ApRestartServiceContAbsent_Type()
)
apRestartServiceContAbsent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRestartServiceContAbsent.setStatus("current")
_ApHostname_Type = DisplayString
_ApHostname_Object = MibTableColumn
apHostname = _ApHostname_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 1, 2, 1, 29),
    _ApHostname_Type()
)
apHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apHostname.setStatus("current")
_ApLocation_Type = DisplayString
_ApLocation_Object = MibTableColumn
apLocation = _ApLocation_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 1, 2, 1, 30),
    _ApLocation_Type()
)
apLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLocation.setStatus("current")


class _ApStaticMTUsize_Type(Unsigned32):
    """Custom type apStaticMTUsize based on Unsigned32"""
    defaultValue = 1500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 1500),
    )


_ApStaticMTUsize_Type.__name__ = "Unsigned32"
_ApStaticMTUsize_Object = MibTableColumn
apStaticMTUsize = _ApStaticMTUsize_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 1, 2, 1, 31),
    _ApStaticMTUsize_Type()
)
apStaticMTUsize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apStaticMTUsize.setStatus("current")


class _ApSiteID_Type(Integer32):
    """Custom type apSiteID based on Integer32"""
    defaultValue = -1


_ApSiteID_Object = MibTableColumn
apSiteID = _ApSiteID_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 1, 2, 1, 32),
    _ApSiteID_Type()
)
apSiteID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSiteID.setStatus("current")
_ApZone_Type = DisplayString
_ApZone_Object = MibTableColumn
apZone = _ApZone_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 1, 2, 1, 33),
    _ApZone_Type()
)
apZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apZone.setStatus("current")
_ApLLDP_Type = TruthValue
_ApLLDP_Object = MibTableColumn
apLLDP = _ApLLDP_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 1, 2, 1, 34),
    _ApLLDP_Type()
)
apLLDP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLLDP.setStatus("current")
_ApSSHAccess_Type = TruthValue
_ApSSHAccess_Object = MibTableColumn
apSSHAccess = _ApSSHAccess_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 1, 2, 1, 35),
    _ApSSHAccess_Type()
)
apSSHAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSSHAccess.setStatus("deprecated")


class _ApLEDMode_Type(Integer32):
    """Custom type apLEDMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("identify", 2),
          ("normal", 3),
          ("off", 0),
          ("wdsSignalStrength", 1))
    )


_ApLEDMode_Type.__name__ = "Integer32"
_ApLEDMode_Object = MibTableColumn
apLEDMode = _ApLEDMode_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 1, 2, 1, 36),
    _ApLEDMode_Type()
)
apLEDMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLEDMode.setStatus("current")
_ApLocationbasedService_Type = TruthValue
_ApLocationbasedService_Object = MibTableColumn
apLocationbasedService = _ApLocationbasedService_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 1, 2, 1, 37),
    _ApLocationbasedService_Type()
)
apLocationbasedService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLocationbasedService.setStatus("current")
_ApSecureTunnel_Type = TruthValue
_ApSecureTunnel_Object = MibTableColumn
apSecureTunnel = _ApSecureTunnel_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 1, 2, 1, 38),
    _ApSecureTunnel_Type()
)
apSecureTunnel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSecureTunnel.setStatus("current")
_ApEncryptCntTraffic_Type = TruthValue
_ApEncryptCntTraffic_Object = MibTableColumn
apEncryptCntTraffic = _ApEncryptCntTraffic_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 1, 2, 1, 39),
    _ApEncryptCntTraffic_Type()
)
apEncryptCntTraffic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apEncryptCntTraffic.setStatus("current")
_ApMICErrorWarning_Type = TruthValue
_ApMICErrorWarning_Object = MibTableColumn
apMICErrorWarning = _ApMICErrorWarning_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 1, 2, 1, 40),
    _ApMICErrorWarning_Type()
)
apMICErrorWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apMICErrorWarning.setStatus("current")


class _ApSecureDataTunnelType_Type(Integer32):
    """Custom type apSecureDataTunnelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("debugMode", 3),
          ("disable", 0),
          ("encryptControlDataTraffic", 2),
          ("encryptControlTraffic", 1))
    )


_ApSecureDataTunnelType_Type.__name__ = "Integer32"
_ApSecureDataTunnelType_Object = MibTableColumn
apSecureDataTunnelType = _ApSecureDataTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 1, 2, 1, 41),
    _ApSecureDataTunnelType_Type()
)
apSecureDataTunnelType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSecureDataTunnelType.setStatus("current")
_ApIPMulticastAssembly_Type = TruthValue
_ApIPMulticastAssembly_Object = MibTableColumn
apIPMulticastAssembly = _ApIPMulticastAssembly_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 1, 2, 1, 42),
    _ApIPMulticastAssembly_Type()
)
apIPMulticastAssembly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIPMulticastAssembly.setStatus("current")


class _ApSSHConnection_Type(Integer32):
    """Custom type apSSHConnection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("na", 3))
    )


_ApSSHConnection_Type.__name__ = "Integer32"
_ApSSHConnection_Object = MibTableColumn
apSSHConnection = _ApSSHConnection_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 1, 2, 1, 43),
    _ApSSHConnection_Type()
)
apSSHConnection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSSHConnection.setStatus("current")
_ApRadioTable_Object = MibTable
apRadioTable = _ApRadioTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 1, 3)
)
if mibBuilder.loadTexts:
    apRadioTable.setStatus("current")
_ApRadioEntry_Object = MibTableRow
apRadioEntry = _ApRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 1, 3, 1)
)
apRadioEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-HWC-MIB", "apIndex"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    apRadioEntry.setStatus("current")


class _ApRadioFrequency_Type(Integer32):
    """Custom type apRadioFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("freq24GHz", 2),
          ("freq50GHz", 1))
    )


_ApRadioFrequency_Type.__name__ = "Integer32"
_ApRadioFrequency_Object = MibTableColumn
apRadioFrequency = _ApRadioFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 1, 3, 1, 1),
    _ApRadioFrequency_Type()
)
apRadioFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadioFrequency.setStatus("current")
_ApRadioNumber_Type = Unsigned32
_ApRadioNumber_Object = MibTableColumn
apRadioNumber = _ApRadioNumber_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 1, 3, 1, 2),
    _ApRadioNumber_Type()
)
apRadioNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadioNumber.setStatus("current")


class _ApRadioType_Type(Integer32):
    """Custom type apRadioType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("dot11a", 1),
          ("dot11an", 2),
          ("dot11anStrict", 3),
          ("dot11anc", 11),
          ("dot11b", 4),
          ("dot11bg", 6),
          ("dot11bgn", 8),
          ("dot11cStrict", 12),
          ("dot11g", 5),
          ("dot11gn", 7),
          ("dot11gnStrict", 9),
          ("dot11j", 10),
          ("off", 0))
    )


_ApRadioType_Type.__name__ = "Integer32"
_ApRadioType_Object = MibTableColumn
apRadioType = _ApRadioType_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 1, 3, 1, 3),
    _ApRadioType_Type()
)
apRadioType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioType.setStatus("deprecated")


class _ApRadioProtocol_Type(Bits):
    """Custom type apRadioProtocol based on Bits"""
    namedValues = NamedValues(
        *(("dot1124b", 0),
          ("dot1124g", 1),
          ("dot1124n", 2),
          ("dot1150a", 3),
          ("dot1150ac", 4),
          ("dot1150j", 5),
          ("dot1150n", 6))
    )

_ApRadioProtocol_Type.__name__ = "Bits"
_ApRadioProtocol_Object = MibTableColumn
apRadioProtocol = _ApRadioProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 1, 3, 1, 4),
    _ApRadioProtocol_Type()
)
apRadioProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioProtocol.setStatus("current")
_RadioVNSTable_Object = MibTable
radioVNSTable = _RadioVNSTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 1, 4)
)
if mibBuilder.loadTexts:
    radioVNSTable.setStatus("current")
_RadioVNSEntry_Object = MibTableRow
radioVNSEntry = _RadioVNSEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 1, 4, 1)
)
radioVNSEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-HWC-MIB", "radioIfIndex"),
    (0, "HIPATH-WIRELESS-HWC-MIB", "vnsIfIndex"),
)
if mibBuilder.loadTexts:
    radioVNSEntry.setStatus("current")
_RadioIfIndex_Type = InterfaceIndex
_RadioIfIndex_Object = MibTableColumn
radioIfIndex = _RadioIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 1, 4, 1, 1),
    _RadioIfIndex_Type()
)
radioIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radioIfIndex.setStatus("current")
_VnsIfIndex_Type = InterfaceIndex
_VnsIfIndex_Object = MibTableColumn
vnsIfIndex = _VnsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 1, 4, 1, 2),
    _VnsIfIndex_Type()
)
vnsIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vnsIfIndex.setStatus("current")
_RadioVNSRowStatus_Type = RowStatus
_RadioVNSRowStatus_Object = MibTableColumn
radioVNSRowStatus = _RadioVNSRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 1, 4, 1, 3),
    _RadioVNSRowStatus_Type()
)
radioVNSRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radioVNSRowStatus.setStatus("current")
_ApFastFailoverEnable_Type = TruthValue
_ApFastFailoverEnable_Object = MibScalar
apFastFailoverEnable = _ApFastFailoverEnable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 1, 5),
    _ApFastFailoverEnable_Type()
)
apFastFailoverEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apFastFailoverEnable.setStatus("current")
_ApLinkTimeout_Type = Integer32
_ApLinkTimeout_Object = MibScalar
apLinkTimeout = _ApLinkTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 1, 6),
    _ApLinkTimeout_Type()
)
apLinkTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apLinkTimeout.setStatus("current")
_ApAntennaTable_Object = MibTable
apAntennaTable = _ApAntennaTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 1, 7)
)
if mibBuilder.loadTexts:
    apAntennaTable.setStatus("current")
_ApAntennaEntry_Object = MibTableRow
apAntennaEntry = _ApAntennaEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 1, 7, 1)
)
apAntennaEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-HWC-MIB", "apIndex"),
    (0, "HIPATH-WIRELESS-HWC-MIB", "apAntennaIndex"),
)
if mibBuilder.loadTexts:
    apAntennaEntry.setStatus("current")
_ApAntennaIndex_Type = Unsigned32
_ApAntennaIndex_Object = MibTableColumn
apAntennaIndex = _ApAntennaIndex_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 1, 7, 1, 1),
    _ApAntennaIndex_Type()
)
apAntennaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apAntennaIndex.setStatus("current")
_ApAntennanName_Type = DisplayString
_ApAntennanName_Object = MibTableColumn
apAntennanName = _ApAntennanName_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 1, 7, 1, 2),
    _ApAntennanName_Type()
)
apAntennanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAntennanName.setStatus("current")
_ApAntennaType_Type = DisplayString
_ApAntennaType_Object = MibTableColumn
apAntennaType = _ApAntennaType_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 1, 7, 1, 3),
    _ApAntennaType_Type()
)
apAntennaType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apAntennaType.setStatus("current")
_ApRadioAntennaTable_Object = MibTable
apRadioAntennaTable = _ApRadioAntennaTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 1, 8)
)
if mibBuilder.loadTexts:
    apRadioAntennaTable.setStatus("current")
_ApRadioAntennaEntry_Object = MibTableRow
apRadioAntennaEntry = _ApRadioAntennaEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 1, 8, 1)
)
apRadioAntennaEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-HWC-MIB", "apIndex"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    apRadioAntennaEntry.setStatus("current")
_ApRadioAntennaType_Type = DisplayString
_ApRadioAntennaType_Object = MibTableColumn
apRadioAntennaType = _ApRadioAntennaType_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 1, 8, 1, 3),
    _ApRadioAntennaType_Type()
)
apRadioAntennaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadioAntennaType.setStatus("current")
_ApRadioAntennaModel_Type = Unsigned32
_ApRadioAntennaModel_Object = MibTableColumn
apRadioAntennaModel = _ApRadioAntennaModel_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 1, 8, 1, 4),
    _ApRadioAntennaModel_Type()
)
apRadioAntennaModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadioAntennaModel.setStatus("current")
_ApRadioAttenuation_Type = Integer32
_ApRadioAttenuation_Object = MibTableColumn
apRadioAttenuation = _ApRadioAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 1, 8, 1, 5),
    _ApRadioAttenuation_Type()
)
apRadioAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRadioAttenuation.setStatus("current")
_ApStatsObjects_ObjectIdentity = ObjectIdentity
apStatsObjects = _ApStatsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2)
)
_ApActiveCount_Type = Integer32
_ApActiveCount_Object = MibScalar
apActiveCount = _ApActiveCount_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 1),
    _ApActiveCount_Type()
)
apActiveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apActiveCount.setStatus("current")
_ApStatsTable_Object = MibTable
apStatsTable = _ApStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 2)
)
if mibBuilder.loadTexts:
    apStatsTable.setStatus("current")
_ApStatsEntry_Object = MibTableRow
apStatsEntry = _ApStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 2, 1)
)
apStatsEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-HWC-MIB", "apIndex"),
)
if mibBuilder.loadTexts:
    apStatsEntry.setStatus("current")
_ApInUcastPkts_Type = Counter64
_ApInUcastPkts_Object = MibTableColumn
apInUcastPkts = _ApInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 2, 1, 1),
    _ApInUcastPkts_Type()
)
apInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInUcastPkts.setStatus("current")
_ApInNUcastPkts_Type = Counter64
_ApInNUcastPkts_Object = MibTableColumn
apInNUcastPkts = _ApInNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 2, 1, 2),
    _ApInNUcastPkts_Type()
)
apInNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInNUcastPkts.setStatus("current")
_ApInOctets_Type = Counter64
_ApInOctets_Object = MibTableColumn
apInOctets = _ApInOctets_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 2, 1, 3),
    _ApInOctets_Type()
)
apInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInOctets.setStatus("current")
_ApInErrors_Type = Counter64
_ApInErrors_Object = MibTableColumn
apInErrors = _ApInErrors_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 2, 1, 4),
    _ApInErrors_Type()
)
apInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInErrors.setStatus("current")
_ApInDiscards_Type = Counter64
_ApInDiscards_Object = MibTableColumn
apInDiscards = _ApInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 2, 1, 5),
    _ApInDiscards_Type()
)
apInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInDiscards.setStatus("current")
_ApOutUcastPkts_Type = Counter64
_ApOutUcastPkts_Object = MibTableColumn
apOutUcastPkts = _ApOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 2, 1, 6),
    _ApOutUcastPkts_Type()
)
apOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutUcastPkts.setStatus("current")
_ApOutNUcastPkts_Type = Counter64
_ApOutNUcastPkts_Object = MibTableColumn
apOutNUcastPkts = _ApOutNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 2, 1, 7),
    _ApOutNUcastPkts_Type()
)
apOutNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutNUcastPkts.setStatus("current")
_ApOutOctets_Type = Counter64
_ApOutOctets_Object = MibTableColumn
apOutOctets = _ApOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 2, 1, 8),
    _ApOutOctets_Type()
)
apOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutOctets.setStatus("current")
_ApOutErrors_Type = Counter64
_ApOutErrors_Object = MibTableColumn
apOutErrors = _ApOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 2, 1, 9),
    _ApOutErrors_Type()
)
apOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutErrors.setStatus("current")
_ApOutDiscards_Type = Counter64
_ApOutDiscards_Object = MibTableColumn
apOutDiscards = _ApOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 2, 1, 10),
    _ApOutDiscards_Type()
)
apOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apOutDiscards.setStatus("current")
_ApUpTime_Type = TimeTicks
_ApUpTime_Object = MibTableColumn
apUpTime = _ApUpTime_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 2, 1, 11),
    _ApUpTime_Type()
)
apUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apUpTime.setStatus("current")


class _ApCredentialType_Type(Integer32):
    """Custom type apCredentialType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 3),
          ("none", 0),
          ("peap", 2),
          ("tls", 1))
    )


_ApCredentialType_Type.__name__ = "Integer32"
_ApCredentialType_Object = MibTableColumn
apCredentialType = _ApCredentialType_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 2, 1, 12),
    _ApCredentialType_Type()
)
apCredentialType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCredentialType.setStatus("current")
_ApCertificateExpiry_Type = TimeTicks
_ApCertificateExpiry_Object = MibTableColumn
apCertificateExpiry = _ApCertificateExpiry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 2, 1, 13),
    _ApCertificateExpiry_Type()
)
apCertificateExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCertificateExpiry.setStatus("current")
_ApStatsMuCounts_Type = Unsigned32
_ApStatsMuCounts_Object = MibTableColumn
apStatsMuCounts = _ApStatsMuCounts_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 2, 1, 14),
    _ApStatsMuCounts_Type()
)
apStatsMuCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStatsMuCounts.setStatus("current")
_ApStatsSessionDuration_Type = TimeTicks
_ApStatsSessionDuration_Object = MibTableColumn
apStatsSessionDuration = _ApStatsSessionDuration_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 2, 1, 15),
    _ApStatsSessionDuration_Type()
)
apStatsSessionDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apStatsSessionDuration.setStatus("current")
_ApTotalStationsA_Type = Unsigned32
_ApTotalStationsA_Object = MibTableColumn
apTotalStationsA = _ApTotalStationsA_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 2, 1, 16),
    _ApTotalStationsA_Type()
)
apTotalStationsA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTotalStationsA.setStatus("current")
_ApTotalStationsB_Type = Unsigned32
_ApTotalStationsB_Object = MibTableColumn
apTotalStationsB = _ApTotalStationsB_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 2, 1, 17),
    _ApTotalStationsB_Type()
)
apTotalStationsB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTotalStationsB.setStatus("current")
_ApTotalStationsG_Type = Unsigned32
_ApTotalStationsG_Object = MibTableColumn
apTotalStationsG = _ApTotalStationsG_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 2, 1, 18),
    _ApTotalStationsG_Type()
)
apTotalStationsG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTotalStationsG.setStatus("current")
_ApTotalStationsN50_Type = Unsigned32
_ApTotalStationsN50_Object = MibTableColumn
apTotalStationsN50 = _ApTotalStationsN50_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 2, 1, 19),
    _ApTotalStationsN50_Type()
)
apTotalStationsN50.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTotalStationsN50.setStatus("current")
_ApTotalStationsN24_Type = Unsigned32
_ApTotalStationsN24_Object = MibTableColumn
apTotalStationsN24 = _ApTotalStationsN24_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 2, 1, 20),
    _ApTotalStationsN24_Type()
)
apTotalStationsN24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTotalStationsN24.setStatus("current")
_ApInvalidPolicyCount_Type = Unsigned32
_ApInvalidPolicyCount_Object = MibTableColumn
apInvalidPolicyCount = _ApInvalidPolicyCount_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 2, 1, 21),
    _ApInvalidPolicyCount_Type()
)
apInvalidPolicyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInvalidPolicyCount.setStatus("current")
_ApInterfaceMTU_Type = Unsigned32
_ApInterfaceMTU_Object = MibTableColumn
apInterfaceMTU = _ApInterfaceMTU_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 2, 1, 22),
    _ApInterfaceMTU_Type()
)
apInterfaceMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apInterfaceMTU.setStatus("current")
_ApEffectiveTunnelMTU_Type = Unsigned32
_ApEffectiveTunnelMTU_Object = MibTableColumn
apEffectiveTunnelMTU = _ApEffectiveTunnelMTU_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 2, 1, 23),
    _ApEffectiveTunnelMTU_Type()
)
apEffectiveTunnelMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEffectiveTunnelMTU.setStatus("current")
_ApTotalStationsAC_Type = Unsigned32
_ApTotalStationsAC_Object = MibTableColumn
apTotalStationsAC = _ApTotalStationsAC_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 2, 1, 24),
    _ApTotalStationsAC_Type()
)
apTotalStationsAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTotalStationsAC.setStatus("current")
_ApTotalStationsAInOctets_Type = Counter64
_ApTotalStationsAInOctets_Object = MibTableColumn
apTotalStationsAInOctets = _ApTotalStationsAInOctets_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 2, 1, 25),
    _ApTotalStationsAInOctets_Type()
)
apTotalStationsAInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTotalStationsAInOctets.setStatus("current")
_ApTotalStationsAOutOctets_Type = Counter64
_ApTotalStationsAOutOctets_Object = MibTableColumn
apTotalStationsAOutOctets = _ApTotalStationsAOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 2, 1, 26),
    _ApTotalStationsAOutOctets_Type()
)
apTotalStationsAOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTotalStationsAOutOctets.setStatus("current")
_ApTotalStationsBInOctets_Type = Counter64
_ApTotalStationsBInOctets_Object = MibTableColumn
apTotalStationsBInOctets = _ApTotalStationsBInOctets_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 2, 1, 27),
    _ApTotalStationsBInOctets_Type()
)
apTotalStationsBInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTotalStationsBInOctets.setStatus("current")
_ApTotalStationsBOutOctets_Type = Counter64
_ApTotalStationsBOutOctets_Object = MibTableColumn
apTotalStationsBOutOctets = _ApTotalStationsBOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 2, 1, 28),
    _ApTotalStationsBOutOctets_Type()
)
apTotalStationsBOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTotalStationsBOutOctets.setStatus("current")
_ApTotalStationsGInOctets_Type = Counter64
_ApTotalStationsGInOctets_Object = MibTableColumn
apTotalStationsGInOctets = _ApTotalStationsGInOctets_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 2, 1, 29),
    _ApTotalStationsGInOctets_Type()
)
apTotalStationsGInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTotalStationsGInOctets.setStatus("current")
_ApTotalStationsGOutOctets_Type = Counter64
_ApTotalStationsGOutOctets_Object = MibTableColumn
apTotalStationsGOutOctets = _ApTotalStationsGOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 2, 1, 30),
    _ApTotalStationsGOutOctets_Type()
)
apTotalStationsGOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTotalStationsGOutOctets.setStatus("current")
_ApTotalStationsN50InOctets_Type = Counter64
_ApTotalStationsN50InOctets_Object = MibTableColumn
apTotalStationsN50InOctets = _ApTotalStationsN50InOctets_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 2, 1, 31),
    _ApTotalStationsN50InOctets_Type()
)
apTotalStationsN50InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTotalStationsN50InOctets.setStatus("current")
_ApTotalStationsN50OutOctets_Type = Counter64
_ApTotalStationsN50OutOctets_Object = MibTableColumn
apTotalStationsN50OutOctets = _ApTotalStationsN50OutOctets_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 2, 1, 32),
    _ApTotalStationsN50OutOctets_Type()
)
apTotalStationsN50OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTotalStationsN50OutOctets.setStatus("current")
_ApTotalStationsN24InOctets_Type = Counter64
_ApTotalStationsN24InOctets_Object = MibTableColumn
apTotalStationsN24InOctets = _ApTotalStationsN24InOctets_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 2, 1, 33),
    _ApTotalStationsN24InOctets_Type()
)
apTotalStationsN24InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTotalStationsN24InOctets.setStatus("current")
_ApTotalStationsN24OutOctets_Type = Counter64
_ApTotalStationsN24OutOctets_Object = MibTableColumn
apTotalStationsN24OutOctets = _ApTotalStationsN24OutOctets_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 2, 1, 34),
    _ApTotalStationsN24OutOctets_Type()
)
apTotalStationsN24OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTotalStationsN24OutOctets.setStatus("current")
_ApTotalStationsACInOctets_Type = Counter64
_ApTotalStationsACInOctets_Object = MibTableColumn
apTotalStationsACInOctets = _ApTotalStationsACInOctets_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 2, 1, 35),
    _ApTotalStationsACInOctets_Type()
)
apTotalStationsACInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTotalStationsACInOctets.setStatus("current")
_ApTotalStationsACOutOctets_Type = Counter64
_ApTotalStationsACOutOctets_Object = MibTableColumn
apTotalStationsACOutOctets = _ApTotalStationsACOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 2, 1, 36),
    _ApTotalStationsACOutOctets_Type()
)
apTotalStationsACOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTotalStationsACOutOctets.setStatus("current")
_ApRegistrationRequests_Type = Counter32
_ApRegistrationRequests_Object = MibScalar
apRegistrationRequests = _ApRegistrationRequests_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 3),
    _ApRegistrationRequests_Type()
)
apRegistrationRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRegistrationRequests.setStatus("current")
_ApRadioStatusTable_Object = MibTable
apRadioStatusTable = _ApRadioStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 4)
)
if mibBuilder.loadTexts:
    apRadioStatusTable.setStatus("current")
_ApRadioStatusEntry_Object = MibTableRow
apRadioStatusEntry = _ApRadioStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 4, 1)
)
apRadioStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    apRadioStatusEntry.setStatus("current")
_ApRadioStatusChannel_Type = Unsigned32
_ApRadioStatusChannel_Object = MibTableColumn
apRadioStatusChannel = _ApRadioStatusChannel_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 4, 1, 1),
    _ApRadioStatusChannel_Type()
)
apRadioStatusChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadioStatusChannel.setStatus("current")


class _ApRadioStatusChannelWidth_Type(Integer32):
    """Custom type apRadioStatusChannelWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("width20Mhz", 1),
          ("width40Mhz", 2),
          ("width80Mhz", 4))
    )


_ApRadioStatusChannelWidth_Type.__name__ = "Integer32"
_ApRadioStatusChannelWidth_Object = MibTableColumn
apRadioStatusChannelWidth = _ApRadioStatusChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 4, 1, 2),
    _ApRadioStatusChannelWidth_Type()
)
apRadioStatusChannelWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadioStatusChannelWidth.setStatus("current")
_ApRadioStatusChannelOffset_Type = Unsigned32
_ApRadioStatusChannelOffset_Object = MibTableColumn
apRadioStatusChannelOffset = _ApRadioStatusChannelOffset_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 4, 1, 3),
    _ApRadioStatusChannelOffset_Type()
)
apRadioStatusChannelOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apRadioStatusChannelOffset.setStatus("current")
_ApPerformanceReportByRadioTable_Object = MibTable
apPerformanceReportByRadioTable = _ApPerformanceReportByRadioTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 5)
)
if mibBuilder.loadTexts:
    apPerformanceReportByRadioTable.setStatus("current")
_ApPerformanceReportByRadioEntry_Object = MibTableRow
apPerformanceReportByRadioEntry = _ApPerformanceReportByRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 5, 1)
)
apPerformanceReportByRadioEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-HWC-MIB", "apIndex"),
    (0, "HIPATH-WIRELESS-HWC-MIB", "apRadioIndex"),
)
if mibBuilder.loadTexts:
    apPerformanceReportByRadioEntry.setStatus("current")


class _ApRadioIndex_Type(Integer32):
    """Custom type apRadioIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_ApRadioIndex_Type.__name__ = "Integer32"
_ApRadioIndex_Object = MibTableColumn
apRadioIndex = _ApRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 5, 1, 1),
    _ApRadioIndex_Type()
)
apRadioIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apRadioIndex.setStatus("current")
_ApPerfRadioPrevPeakChannelUtilization_Type = Gauge32
_ApPerfRadioPrevPeakChannelUtilization_Object = MibTableColumn
apPerfRadioPrevPeakChannelUtilization = _ApPerfRadioPrevPeakChannelUtilization_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 5, 1, 2),
    _ApPerfRadioPrevPeakChannelUtilization_Type()
)
apPerfRadioPrevPeakChannelUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPerfRadioPrevPeakChannelUtilization.setStatus("current")
_ApPerfRadioCurPeakChannelUtilization_Type = Gauge32
_ApPerfRadioCurPeakChannelUtilization_Object = MibTableColumn
apPerfRadioCurPeakChannelUtilization = _ApPerfRadioCurPeakChannelUtilization_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 5, 1, 3),
    _ApPerfRadioCurPeakChannelUtilization_Type()
)
apPerfRadioCurPeakChannelUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPerfRadioCurPeakChannelUtilization.setStatus("current")
_ApPerfRadioAverageChannelUtilization_Type = HundredthOfGauge32
_ApPerfRadioAverageChannelUtilization_Object = MibTableColumn
apPerfRadioAverageChannelUtilization = _ApPerfRadioAverageChannelUtilization_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 5, 1, 4),
    _ApPerfRadioAverageChannelUtilization_Type()
)
apPerfRadioAverageChannelUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPerfRadioAverageChannelUtilization.setStatus("current")
_ApPerfRadioCurrentChannelUtilization_Type = Gauge32
_ApPerfRadioCurrentChannelUtilization_Object = MibTableColumn
apPerfRadioCurrentChannelUtilization = _ApPerfRadioCurrentChannelUtilization_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 5, 1, 5),
    _ApPerfRadioCurrentChannelUtilization_Type()
)
apPerfRadioCurrentChannelUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPerfRadioCurrentChannelUtilization.setStatus("current")
_ApPerfRadioPrevPeakRSS_Type = Gauge32
_ApPerfRadioPrevPeakRSS_Object = MibTableColumn
apPerfRadioPrevPeakRSS = _ApPerfRadioPrevPeakRSS_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 5, 1, 6),
    _ApPerfRadioPrevPeakRSS_Type()
)
apPerfRadioPrevPeakRSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPerfRadioPrevPeakRSS.setStatus("current")
_ApPerfRadioCurPeakRSS_Type = Gauge32
_ApPerfRadioCurPeakRSS_Object = MibTableColumn
apPerfRadioCurPeakRSS = _ApPerfRadioCurPeakRSS_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 5, 1, 7),
    _ApPerfRadioCurPeakRSS_Type()
)
apPerfRadioCurPeakRSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPerfRadioCurPeakRSS.setStatus("current")
_ApPerfRadioAverageRSS_Type = HundredthOfInt32
_ApPerfRadioAverageRSS_Object = MibTableColumn
apPerfRadioAverageRSS = _ApPerfRadioAverageRSS_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 5, 1, 8),
    _ApPerfRadioAverageRSS_Type()
)
apPerfRadioAverageRSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPerfRadioAverageRSS.setStatus("current")
_ApPerfRadioCurrentRSS_Type = Gauge32
_ApPerfRadioCurrentRSS_Object = MibTableColumn
apPerfRadioCurrentRSS = _ApPerfRadioCurrentRSS_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 5, 1, 9),
    _ApPerfRadioCurrentRSS_Type()
)
apPerfRadioCurrentRSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPerfRadioCurrentRSS.setStatus("current")
_ApPerfRadioPrevPeakSNR_Type = Gauge32
_ApPerfRadioPrevPeakSNR_Object = MibTableColumn
apPerfRadioPrevPeakSNR = _ApPerfRadioPrevPeakSNR_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 5, 1, 10),
    _ApPerfRadioPrevPeakSNR_Type()
)
apPerfRadioPrevPeakSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPerfRadioPrevPeakSNR.setStatus("current")
_ApPerfRadioCurPeakSNR_Type = Gauge32
_ApPerfRadioCurPeakSNR_Object = MibTableColumn
apPerfRadioCurPeakSNR = _ApPerfRadioCurPeakSNR_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 5, 1, 11),
    _ApPerfRadioCurPeakSNR_Type()
)
apPerfRadioCurPeakSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPerfRadioCurPeakSNR.setStatus("current")
_ApPerfRadioAverageSNR_Type = HundredthOfInt32
_ApPerfRadioAverageSNR_Object = MibTableColumn
apPerfRadioAverageSNR = _ApPerfRadioAverageSNR_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 5, 1, 12),
    _ApPerfRadioAverageSNR_Type()
)
apPerfRadioAverageSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPerfRadioAverageSNR.setStatus("current")
_ApPerfRadioCurrentSNR_Type = Gauge32
_ApPerfRadioCurrentSNR_Object = MibTableColumn
apPerfRadioCurrentSNR = _ApPerfRadioCurrentSNR_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 5, 1, 13),
    _ApPerfRadioCurrentSNR_Type()
)
apPerfRadioCurrentSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPerfRadioCurrentSNR.setStatus("current")
_ApPerfRadioPrevPeakPktRetx_Type = HundredthOfGauge64
_ApPerfRadioPrevPeakPktRetx_Object = MibTableColumn
apPerfRadioPrevPeakPktRetx = _ApPerfRadioPrevPeakPktRetx_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 5, 1, 14),
    _ApPerfRadioPrevPeakPktRetx_Type()
)
apPerfRadioPrevPeakPktRetx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPerfRadioPrevPeakPktRetx.setStatus("current")
_ApPerfRadioCurPeakPktRetx_Type = HundredthOfGauge64
_ApPerfRadioCurPeakPktRetx_Object = MibTableColumn
apPerfRadioCurPeakPktRetx = _ApPerfRadioCurPeakPktRetx_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 5, 1, 15),
    _ApPerfRadioCurPeakPktRetx_Type()
)
apPerfRadioCurPeakPktRetx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPerfRadioCurPeakPktRetx.setStatus("current")
_ApPerfRadioAveragePktRetx_Type = HundredthOfGauge64
_ApPerfRadioAveragePktRetx_Object = MibTableColumn
apPerfRadioAveragePktRetx = _ApPerfRadioAveragePktRetx_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 5, 1, 16),
    _ApPerfRadioAveragePktRetx_Type()
)
apPerfRadioAveragePktRetx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPerfRadioAveragePktRetx.setStatus("current")
_ApPerfRadioCurrentPktRetx_Type = HundredthOfGauge64
_ApPerfRadioCurrentPktRetx_Object = MibTableColumn
apPerfRadioCurrentPktRetx = _ApPerfRadioCurrentPktRetx_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 5, 1, 17),
    _ApPerfRadioCurrentPktRetx_Type()
)
apPerfRadioCurrentPktRetx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPerfRadioCurrentPktRetx.setStatus("current")
_ApPerfRadioPktRetx_Type = Counter64
_ApPerfRadioPktRetx_Object = MibTableColumn
apPerfRadioPktRetx = _ApPerfRadioPktRetx_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 5, 1, 18),
    _ApPerfRadioPktRetx_Type()
)
apPerfRadioPktRetx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPerfRadioPktRetx.setStatus("current")
_ApAccessibilityTable_Object = MibTable
apAccessibilityTable = _ApAccessibilityTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 6)
)
if mibBuilder.loadTexts:
    apAccessibilityTable.setStatus("current")
_ApAccessibilityEntry_Object = MibTableRow
apAccessibilityEntry = _ApAccessibilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 6, 1)
)
apAccessibilityEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-HWC-MIB", "apIndex"),
    (0, "HIPATH-WIRELESS-HWC-MIB", "apRadioIndex"),
)
if mibBuilder.loadTexts:
    apAccessibilityEntry.setStatus("current")
_ApAccPrevPeakAssocReqRx_Type = HundredthOfGauge64
_ApAccPrevPeakAssocReqRx_Object = MibTableColumn
apAccPrevPeakAssocReqRx = _ApAccPrevPeakAssocReqRx_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 6, 1, 1),
    _ApAccPrevPeakAssocReqRx_Type()
)
apAccPrevPeakAssocReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAccPrevPeakAssocReqRx.setStatus("current")
_ApAccCurPeakAssocReqRx_Type = HundredthOfGauge64
_ApAccCurPeakAssocReqRx_Object = MibTableColumn
apAccCurPeakAssocReqRx = _ApAccCurPeakAssocReqRx_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 6, 1, 2),
    _ApAccCurPeakAssocReqRx_Type()
)
apAccCurPeakAssocReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAccCurPeakAssocReqRx.setStatus("current")
_ApAccAverageAssocReqRx_Type = HundredthOfGauge64
_ApAccAverageAssocReqRx_Object = MibTableColumn
apAccAverageAssocReqRx = _ApAccAverageAssocReqRx_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 6, 1, 3),
    _ApAccAverageAssocReqRx_Type()
)
apAccAverageAssocReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAccAverageAssocReqRx.setStatus("current")
_ApAccCurrentAssocReqRx_Type = HundredthOfGauge64
_ApAccCurrentAssocReqRx_Object = MibTableColumn
apAccCurrentAssocReqRx = _ApAccCurrentAssocReqRx_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 6, 1, 4),
    _ApAccCurrentAssocReqRx_Type()
)
apAccCurrentAssocReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAccCurrentAssocReqRx.setStatus("current")
_ApAccAssocReqRx_Type = Counter64
_ApAccAssocReqRx_Object = MibTableColumn
apAccAssocReqRx = _ApAccAssocReqRx_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 6, 1, 5),
    _ApAccAssocReqRx_Type()
)
apAccAssocReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAccAssocReqRx.setStatus("current")
_ApAccPrevPeakReassocReqRx_Type = HundredthOfGauge64
_ApAccPrevPeakReassocReqRx_Object = MibTableColumn
apAccPrevPeakReassocReqRx = _ApAccPrevPeakReassocReqRx_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 6, 1, 6),
    _ApAccPrevPeakReassocReqRx_Type()
)
apAccPrevPeakReassocReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAccPrevPeakReassocReqRx.setStatus("current")
_ApAccCurPeakReassocReqRx_Type = HundredthOfGauge64
_ApAccCurPeakReassocReqRx_Object = MibTableColumn
apAccCurPeakReassocReqRx = _ApAccCurPeakReassocReqRx_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 6, 1, 7),
    _ApAccCurPeakReassocReqRx_Type()
)
apAccCurPeakReassocReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAccCurPeakReassocReqRx.setStatus("current")
_ApAccAverageReassocReqRx_Type = HundredthOfGauge64
_ApAccAverageReassocReqRx_Object = MibTableColumn
apAccAverageReassocReqRx = _ApAccAverageReassocReqRx_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 6, 1, 8),
    _ApAccAverageReassocReqRx_Type()
)
apAccAverageReassocReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAccAverageReassocReqRx.setStatus("current")
_ApAccCurrentReassocReqRx_Type = HundredthOfGauge64
_ApAccCurrentReassocReqRx_Object = MibTableColumn
apAccCurrentReassocReqRx = _ApAccCurrentReassocReqRx_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 6, 1, 9),
    _ApAccCurrentReassocReqRx_Type()
)
apAccCurrentReassocReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAccCurrentReassocReqRx.setStatus("current")
_ApAccReassocReqRx_Type = Counter64
_ApAccReassocReqRx_Object = MibTableColumn
apAccReassocReqRx = _ApAccReassocReqRx_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 6, 1, 10),
    _ApAccReassocReqRx_Type()
)
apAccReassocReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAccReassocReqRx.setStatus("current")
_ApAccPrevPeakDisassocDeauthReqTx_Type = HundredthOfGauge64
_ApAccPrevPeakDisassocDeauthReqTx_Object = MibTableColumn
apAccPrevPeakDisassocDeauthReqTx = _ApAccPrevPeakDisassocDeauthReqTx_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 6, 1, 11),
    _ApAccPrevPeakDisassocDeauthReqTx_Type()
)
apAccPrevPeakDisassocDeauthReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAccPrevPeakDisassocDeauthReqTx.setStatus("current")
_ApAccCurPeakDisassocDeauthReqTx_Type = HundredthOfGauge64
_ApAccCurPeakDisassocDeauthReqTx_Object = MibTableColumn
apAccCurPeakDisassocDeauthReqTx = _ApAccCurPeakDisassocDeauthReqTx_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 6, 1, 12),
    _ApAccCurPeakDisassocDeauthReqTx_Type()
)
apAccCurPeakDisassocDeauthReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAccCurPeakDisassocDeauthReqTx.setStatus("current")
_ApAccAverageDisassocDeauthReqTx_Type = HundredthOfGauge64
_ApAccAverageDisassocDeauthReqTx_Object = MibTableColumn
apAccAverageDisassocDeauthReqTx = _ApAccAverageDisassocDeauthReqTx_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 6, 1, 13),
    _ApAccAverageDisassocDeauthReqTx_Type()
)
apAccAverageDisassocDeauthReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAccAverageDisassocDeauthReqTx.setStatus("current")
_ApAccCurrentDisassocDeauthReqTx_Type = HundredthOfGauge64
_ApAccCurrentDisassocDeauthReqTx_Object = MibTableColumn
apAccCurrentDisassocDeauthReqTx = _ApAccCurrentDisassocDeauthReqTx_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 6, 1, 14),
    _ApAccCurrentDisassocDeauthReqTx_Type()
)
apAccCurrentDisassocDeauthReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAccCurrentDisassocDeauthReqTx.setStatus("current")
_ApAccDisassocDeauthReqTx_Type = Counter64
_ApAccDisassocDeauthReqTx_Object = MibTableColumn
apAccDisassocDeauthReqTx = _ApAccDisassocDeauthReqTx_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 6, 1, 15),
    _ApAccDisassocDeauthReqTx_Type()
)
apAccDisassocDeauthReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAccDisassocDeauthReqTx.setStatus("current")
_ApAccPrevPeakDisassocDeauthReqRx_Type = HundredthOfGauge64
_ApAccPrevPeakDisassocDeauthReqRx_Object = MibTableColumn
apAccPrevPeakDisassocDeauthReqRx = _ApAccPrevPeakDisassocDeauthReqRx_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 6, 1, 16),
    _ApAccPrevPeakDisassocDeauthReqRx_Type()
)
apAccPrevPeakDisassocDeauthReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAccPrevPeakDisassocDeauthReqRx.setStatus("current")
_ApAccCurPeakDisassocDeauthReqRx_Type = HundredthOfGauge64
_ApAccCurPeakDisassocDeauthReqRx_Object = MibTableColumn
apAccCurPeakDisassocDeauthReqRx = _ApAccCurPeakDisassocDeauthReqRx_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 6, 1, 17),
    _ApAccCurPeakDisassocDeauthReqRx_Type()
)
apAccCurPeakDisassocDeauthReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAccCurPeakDisassocDeauthReqRx.setStatus("current")
_ApAccAverageDisassocDeauthReqRx_Type = HundredthOfGauge64
_ApAccAverageDisassocDeauthReqRx_Object = MibTableColumn
apAccAverageDisassocDeauthReqRx = _ApAccAverageDisassocDeauthReqRx_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 6, 1, 18),
    _ApAccAverageDisassocDeauthReqRx_Type()
)
apAccAverageDisassocDeauthReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAccAverageDisassocDeauthReqRx.setStatus("current")
_ApAccCurrentDisassocDeauthReqRx_Type = HundredthOfGauge64
_ApAccCurrentDisassocDeauthReqRx_Object = MibTableColumn
apAccCurrentDisassocDeauthReqRx = _ApAccCurrentDisassocDeauthReqRx_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 6, 1, 19),
    _ApAccCurrentDisassocDeauthReqRx_Type()
)
apAccCurrentDisassocDeauthReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAccCurrentDisassocDeauthReqRx.setStatus("current")
_ApAccDisassocDeauthReqRx_Type = Counter64
_ApAccDisassocDeauthReqRx_Object = MibTableColumn
apAccDisassocDeauthReqRx = _ApAccDisassocDeauthReqRx_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 6, 1, 20),
    _ApAccDisassocDeauthReqRx_Type()
)
apAccDisassocDeauthReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAccDisassocDeauthReqRx.setStatus("current")
_ApPerformanceReportbyRadioAndWlanTable_Object = MibTable
apPerformanceReportbyRadioAndWlanTable = _ApPerformanceReportbyRadioAndWlanTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 7)
)
if mibBuilder.loadTexts:
    apPerformanceReportbyRadioAndWlanTable.setStatus("current")
_ApPerformanceReportbyRadioAndWlanEntry_Object = MibTableRow
apPerformanceReportbyRadioAndWlanEntry = _ApPerformanceReportbyRadioAndWlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 7, 1)
)
apPerformanceReportbyRadioAndWlanEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-HWC-MIB", "apIndex"),
    (0, "HIPATH-WIRELESS-HWC-MIB", "apRadioIndex"),
    (0, "HIPATH-WIRELESS-HWC-MIB", "wlanID"),
)
if mibBuilder.loadTexts:
    apPerformanceReportbyRadioAndWlanEntry.setStatus("current")
_ApPerfWlanPrevPeakClientsPerSec_Type = Gauge32
_ApPerfWlanPrevPeakClientsPerSec_Object = MibTableColumn
apPerfWlanPrevPeakClientsPerSec = _ApPerfWlanPrevPeakClientsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 7, 1, 1),
    _ApPerfWlanPrevPeakClientsPerSec_Type()
)
apPerfWlanPrevPeakClientsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPerfWlanPrevPeakClientsPerSec.setStatus("current")
_ApPerfWlanCurPeakClientsPerSec_Type = Gauge32
_ApPerfWlanCurPeakClientsPerSec_Object = MibTableColumn
apPerfWlanCurPeakClientsPerSec = _ApPerfWlanCurPeakClientsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 7, 1, 2),
    _ApPerfWlanCurPeakClientsPerSec_Type()
)
apPerfWlanCurPeakClientsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPerfWlanCurPeakClientsPerSec.setStatus("current")
_ApPerfWlanAverageClientsPerSec_Type = HundredthOfGauge32
_ApPerfWlanAverageClientsPerSec_Object = MibTableColumn
apPerfWlanAverageClientsPerSec = _ApPerfWlanAverageClientsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 7, 1, 3),
    _ApPerfWlanAverageClientsPerSec_Type()
)
apPerfWlanAverageClientsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPerfWlanAverageClientsPerSec.setStatus("current")
_ApPerfWlanCurrentClientsPerSec_Type = Gauge32
_ApPerfWlanCurrentClientsPerSec_Object = MibTableColumn
apPerfWlanCurrentClientsPerSec = _ApPerfWlanCurrentClientsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 7, 1, 4),
    _ApPerfWlanCurrentClientsPerSec_Type()
)
apPerfWlanCurrentClientsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPerfWlanCurrentClientsPerSec.setStatus("current")
_ApPerfWlanPrevPeakULOctetsPerSec_Type = HundredthOfGauge64
_ApPerfWlanPrevPeakULOctetsPerSec_Object = MibTableColumn
apPerfWlanPrevPeakULOctetsPerSec = _ApPerfWlanPrevPeakULOctetsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 7, 1, 5),
    _ApPerfWlanPrevPeakULOctetsPerSec_Type()
)
apPerfWlanPrevPeakULOctetsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPerfWlanPrevPeakULOctetsPerSec.setStatus("current")
_ApPerfWlanCurPeakULOctetsPerSec_Type = HundredthOfGauge64
_ApPerfWlanCurPeakULOctetsPerSec_Object = MibTableColumn
apPerfWlanCurPeakULOctetsPerSec = _ApPerfWlanCurPeakULOctetsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 7, 1, 6),
    _ApPerfWlanCurPeakULOctetsPerSec_Type()
)
apPerfWlanCurPeakULOctetsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPerfWlanCurPeakULOctetsPerSec.setStatus("current")
_ApPerfWlanAverageULOctetsPerSec_Type = HundredthOfGauge64
_ApPerfWlanAverageULOctetsPerSec_Object = MibTableColumn
apPerfWlanAverageULOctetsPerSec = _ApPerfWlanAverageULOctetsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 7, 1, 7),
    _ApPerfWlanAverageULOctetsPerSec_Type()
)
apPerfWlanAverageULOctetsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPerfWlanAverageULOctetsPerSec.setStatus("current")
_ApPerfWlanCurrentULOctetsPerSec_Type = HundredthOfGauge64
_ApPerfWlanCurrentULOctetsPerSec_Object = MibTableColumn
apPerfWlanCurrentULOctetsPerSec = _ApPerfWlanCurrentULOctetsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 7, 1, 8),
    _ApPerfWlanCurrentULOctetsPerSec_Type()
)
apPerfWlanCurrentULOctetsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPerfWlanCurrentULOctetsPerSec.setStatus("current")
_ApPerfWlanULOctets_Type = Counter64
_ApPerfWlanULOctets_Object = MibTableColumn
apPerfWlanULOctets = _ApPerfWlanULOctets_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 7, 1, 9),
    _ApPerfWlanULOctets_Type()
)
apPerfWlanULOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPerfWlanULOctets.setStatus("current")
_ApPerfWlanPrevPeakULPktsPerSec_Type = HundredthOfGauge64
_ApPerfWlanPrevPeakULPktsPerSec_Object = MibTableColumn
apPerfWlanPrevPeakULPktsPerSec = _ApPerfWlanPrevPeakULPktsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 7, 1, 10),
    _ApPerfWlanPrevPeakULPktsPerSec_Type()
)
apPerfWlanPrevPeakULPktsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPerfWlanPrevPeakULPktsPerSec.setStatus("current")
_ApPerfWlanCurPeakULPktsPerSec_Type = HundredthOfGauge64
_ApPerfWlanCurPeakULPktsPerSec_Object = MibTableColumn
apPerfWlanCurPeakULPktsPerSec = _ApPerfWlanCurPeakULPktsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 7, 1, 11),
    _ApPerfWlanCurPeakULPktsPerSec_Type()
)
apPerfWlanCurPeakULPktsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPerfWlanCurPeakULPktsPerSec.setStatus("current")
_ApPerfWlanAverageULPktsPerSec_Type = HundredthOfGauge64
_ApPerfWlanAverageULPktsPerSec_Object = MibTableColumn
apPerfWlanAverageULPktsPerSec = _ApPerfWlanAverageULPktsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 7, 1, 12),
    _ApPerfWlanAverageULPktsPerSec_Type()
)
apPerfWlanAverageULPktsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPerfWlanAverageULPktsPerSec.setStatus("current")
_ApPerfWlanCurrentULPktsPerSec_Type = HundredthOfGauge64
_ApPerfWlanCurrentULPktsPerSec_Object = MibTableColumn
apPerfWlanCurrentULPktsPerSec = _ApPerfWlanCurrentULPktsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 7, 1, 13),
    _ApPerfWlanCurrentULPktsPerSec_Type()
)
apPerfWlanCurrentULPktsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPerfWlanCurrentULPktsPerSec.setStatus("current")
_ApPerfWlanULPkts_Type = Counter64
_ApPerfWlanULPkts_Object = MibTableColumn
apPerfWlanULPkts = _ApPerfWlanULPkts_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 7, 1, 14),
    _ApPerfWlanULPkts_Type()
)
apPerfWlanULPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPerfWlanULPkts.setStatus("current")
_ApPerfWlanPrevPeakDLOctetsPerSec_Type = HundredthOfGauge64
_ApPerfWlanPrevPeakDLOctetsPerSec_Object = MibTableColumn
apPerfWlanPrevPeakDLOctetsPerSec = _ApPerfWlanPrevPeakDLOctetsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 7, 1, 15),
    _ApPerfWlanPrevPeakDLOctetsPerSec_Type()
)
apPerfWlanPrevPeakDLOctetsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPerfWlanPrevPeakDLOctetsPerSec.setStatus("current")
_ApPerfWlanCurPeakDLOctetsPerSec_Type = HundredthOfGauge64
_ApPerfWlanCurPeakDLOctetsPerSec_Object = MibTableColumn
apPerfWlanCurPeakDLOctetsPerSec = _ApPerfWlanCurPeakDLOctetsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 7, 1, 16),
    _ApPerfWlanCurPeakDLOctetsPerSec_Type()
)
apPerfWlanCurPeakDLOctetsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPerfWlanCurPeakDLOctetsPerSec.setStatus("current")
_ApPerfWlanAverageDLOctetsPerSec_Type = HundredthOfGauge64
_ApPerfWlanAverageDLOctetsPerSec_Object = MibTableColumn
apPerfWlanAverageDLOctetsPerSec = _ApPerfWlanAverageDLOctetsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 7, 1, 17),
    _ApPerfWlanAverageDLOctetsPerSec_Type()
)
apPerfWlanAverageDLOctetsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPerfWlanAverageDLOctetsPerSec.setStatus("current")
_ApPerfWlanCurrentDLOctetsPerSec_Type = HundredthOfGauge64
_ApPerfWlanCurrentDLOctetsPerSec_Object = MibTableColumn
apPerfWlanCurrentDLOctetsPerSec = _ApPerfWlanCurrentDLOctetsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 7, 1, 18),
    _ApPerfWlanCurrentDLOctetsPerSec_Type()
)
apPerfWlanCurrentDLOctetsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPerfWlanCurrentDLOctetsPerSec.setStatus("current")
_ApPerfWlanDLOctets_Type = Counter64
_ApPerfWlanDLOctets_Object = MibTableColumn
apPerfWlanDLOctets = _ApPerfWlanDLOctets_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 7, 1, 19),
    _ApPerfWlanDLOctets_Type()
)
apPerfWlanDLOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPerfWlanDLOctets.setStatus("current")
_ApPerfWlanPrevPeakDLPktsPerSec_Type = HundredthOfGauge64
_ApPerfWlanPrevPeakDLPktsPerSec_Object = MibTableColumn
apPerfWlanPrevPeakDLPktsPerSec = _ApPerfWlanPrevPeakDLPktsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 7, 1, 20),
    _ApPerfWlanPrevPeakDLPktsPerSec_Type()
)
apPerfWlanPrevPeakDLPktsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPerfWlanPrevPeakDLPktsPerSec.setStatus("current")
_ApPerfWlanCurPeakDLPktsPerSec_Type = HundredthOfGauge64
_ApPerfWlanCurPeakDLPktsPerSec_Object = MibTableColumn
apPerfWlanCurPeakDLPktsPerSec = _ApPerfWlanCurPeakDLPktsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 7, 1, 21),
    _ApPerfWlanCurPeakDLPktsPerSec_Type()
)
apPerfWlanCurPeakDLPktsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPerfWlanCurPeakDLPktsPerSec.setStatus("current")
_ApPerfWlanAverageDLPktsPerSec_Type = HundredthOfGauge64
_ApPerfWlanAverageDLPktsPerSec_Object = MibTableColumn
apPerfWlanAverageDLPktsPerSec = _ApPerfWlanAverageDLPktsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 7, 1, 22),
    _ApPerfWlanAverageDLPktsPerSec_Type()
)
apPerfWlanAverageDLPktsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPerfWlanAverageDLPktsPerSec.setStatus("current")
_ApPerfWlanCurrentDLPktsPerSec_Type = HundredthOfGauge64
_ApPerfWlanCurrentDLPktsPerSec_Object = MibTableColumn
apPerfWlanCurrentDLPktsPerSec = _ApPerfWlanCurrentDLPktsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 7, 1, 23),
    _ApPerfWlanCurrentDLPktsPerSec_Type()
)
apPerfWlanCurrentDLPktsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPerfWlanCurrentDLPktsPerSec.setStatus("current")
_ApPerfWlanDLPkts_Type = Counter64
_ApPerfWlanDLPkts_Object = MibTableColumn
apPerfWlanDLPkts = _ApPerfWlanDLPkts_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 7, 1, 24),
    _ApPerfWlanDLPkts_Type()
)
apPerfWlanDLPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apPerfWlanDLPkts.setStatus("current")
_ApChannelUtilizationTable_Object = MibTable
apChannelUtilizationTable = _ApChannelUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 8)
)
if mibBuilder.loadTexts:
    apChannelUtilizationTable.setStatus("current")
_ApChannelUtilizationEntry_Object = MibTableRow
apChannelUtilizationEntry = _ApChannelUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 8, 1)
)
apChannelUtilizationEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-HWC-MIB", "apIndex"),
    (0, "HIPATH-WIRELESS-HWC-MIB", "apRadioIndex"),
    (0, "HIPATH-WIRELESS-HWC-MIB", "channel"),
)
if mibBuilder.loadTexts:
    apChannelUtilizationEntry.setStatus("current")
_Channel_Type = Unsigned32
_Channel_Object = MibTableColumn
channel = _Channel_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 8, 1, 1),
    _Channel_Type()
)
channel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    channel.setStatus("current")
_ApChnlUtilPrevPeakUtilization_Type = Gauge32
_ApChnlUtilPrevPeakUtilization_Object = MibTableColumn
apChnlUtilPrevPeakUtilization = _ApChnlUtilPrevPeakUtilization_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 8, 1, 2),
    _ApChnlUtilPrevPeakUtilization_Type()
)
apChnlUtilPrevPeakUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChnlUtilPrevPeakUtilization.setStatus("current")
_ApChnlUtilCurPeakUtilization_Type = Gauge32
_ApChnlUtilCurPeakUtilization_Object = MibTableColumn
apChnlUtilCurPeakUtilization = _ApChnlUtilCurPeakUtilization_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 8, 1, 3),
    _ApChnlUtilCurPeakUtilization_Type()
)
apChnlUtilCurPeakUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChnlUtilCurPeakUtilization.setStatus("current")
_ApChnlUtilAverageUtilization_Type = HundredthOfGauge32
_ApChnlUtilAverageUtilization_Object = MibTableColumn
apChnlUtilAverageUtilization = _ApChnlUtilAverageUtilization_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 8, 1, 4),
    _ApChnlUtilAverageUtilization_Type()
)
apChnlUtilAverageUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChnlUtilAverageUtilization.setStatus("current")
_ApChnlUtilCurrentUtilization_Type = Gauge32
_ApChnlUtilCurrentUtilization_Object = MibTableColumn
apChnlUtilCurrentUtilization = _ApChnlUtilCurrentUtilization_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 8, 1, 5),
    _ApChnlUtilCurrentUtilization_Type()
)
apChnlUtilCurrentUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChnlUtilCurrentUtilization.setStatus("current")
_ApNeighboursTable_Object = MibTable
apNeighboursTable = _ApNeighboursTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 9)
)
if mibBuilder.loadTexts:
    apNeighboursTable.setStatus("current")
_ApNeighboursEntry_Object = MibTableRow
apNeighboursEntry = _ApNeighboursEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 9, 1)
)
apNeighboursEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-HWC-MIB", "apIndex"),
    (0, "IF-MIB", "ifIndex"),
    (0, "HIPATH-WIRELESS-HWC-MIB", "nearbyApIndex"),
)
if mibBuilder.loadTexts:
    apNeighboursEntry.setStatus("current")
_NearbyApIndex_Type = Unsigned32
_NearbyApIndex_Object = MibTableColumn
nearbyApIndex = _NearbyApIndex_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 9, 1, 1),
    _NearbyApIndex_Type()
)
nearbyApIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nearbyApIndex.setStatus("current")
_NearbyApInfo_Type = DisplayString
_NearbyApInfo_Object = MibTableColumn
nearbyApInfo = _NearbyApInfo_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 9, 1, 2),
    _NearbyApInfo_Type()
)
nearbyApInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nearbyApInfo.setStatus("current")


class _NearbyApBSSID_Type(OctetString):
    """Custom type nearbyApBSSID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(17, 17),
    )


_NearbyApBSSID_Type.__name__ = "OctetString"
_NearbyApBSSID_Object = MibTableColumn
nearbyApBSSID = _NearbyApBSSID_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 9, 1, 3),
    _NearbyApBSSID_Type()
)
nearbyApBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nearbyApBSSID.setStatus("current")
_NearbyApChannel_Type = DisplayString
_NearbyApChannel_Object = MibTableColumn
nearbyApChannel = _NearbyApChannel_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 9, 1, 4),
    _NearbyApChannel_Type()
)
nearbyApChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nearbyApChannel.setStatus("current")
_NearbyApRSS_Type = Integer32
_NearbyApRSS_Object = MibTableColumn
nearbyApRSS = _NearbyApRSS_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 2, 9, 1, 5),
    _NearbyApRSS_Type()
)
nearbyApRSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nearbyApRSS.setStatus("current")
_SensorManagement_ObjectIdentity = ObjectIdentity
sensorManagement = _SensorManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 3)
)
_TftpSever_Type = DisplayString
_TftpSever_Object = MibScalar
tftpSever = _TftpSever_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 3, 1),
    _TftpSever_Type()
)
tftpSever.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpSever.setStatus("current")
_ImagePath26xx_Type = DisplayString
_ImagePath26xx_Object = MibScalar
imagePath26xx = _ImagePath26xx_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 3, 2),
    _ImagePath26xx_Type()
)
imagePath26xx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imagePath26xx.setStatus("current")
_ImagePath36xx_Type = DisplayString
_ImagePath36xx_Object = MibScalar
imagePath36xx = _ImagePath36xx_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 3, 3),
    _ImagePath36xx_Type()
)
imagePath36xx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imagePath36xx.setStatus("current")
_ImageVersionOfap26xx_Type = DisplayString
_ImageVersionOfap26xx_Object = MibScalar
imageVersionOfap26xx = _ImageVersionOfap26xx_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 3, 4),
    _ImageVersionOfap26xx_Type()
)
imageVersionOfap26xx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imageVersionOfap26xx.setStatus("current")
_ImageVersionOfngap36xx_Type = DisplayString
_ImageVersionOfngap36xx_Object = MibScalar
imageVersionOfngap36xx = _ImageVersionOfngap36xx_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 3, 5),
    _ImageVersionOfngap36xx_Type()
)
imageVersionOfngap36xx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imageVersionOfngap36xx.setStatus("current")
_ApRegistration_ObjectIdentity = ObjectIdentity
apRegistration = _ApRegistration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 4)
)


class _ApRegSecurityMode_Type(Integer32):
    """Custom type apRegSecurityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allowAll", 1),
          ("allowApprovedOnes", 2))
    )


_ApRegSecurityMode_Type.__name__ = "Integer32"
_ApRegSecurityMode_Object = MibScalar
apRegSecurityMode = _ApRegSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 4, 1),
    _ApRegSecurityMode_Type()
)
apRegSecurityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRegSecurityMode.setStatus("current")


class _ApRegDiscoveryRetries_Type(Unsigned32):
    """Custom type apRegDiscoveryRetries based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ApRegDiscoveryRetries_Type.__name__ = "Unsigned32"
_ApRegDiscoveryRetries_Object = MibScalar
apRegDiscoveryRetries = _ApRegDiscoveryRetries_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 4, 2),
    _ApRegDiscoveryRetries_Type()
)
apRegDiscoveryRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRegDiscoveryRetries.setStatus("current")


class _ApRegDiscoveryInterval_Type(Unsigned32):
    """Custom type apRegDiscoveryInterval based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ApRegDiscoveryInterval_Type.__name__ = "Unsigned32"
_ApRegDiscoveryInterval_Object = MibScalar
apRegDiscoveryInterval = _ApRegDiscoveryInterval_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 4, 3),
    _ApRegDiscoveryInterval_Type()
)
apRegDiscoveryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRegDiscoveryInterval.setStatus("current")
if mibBuilder.loadTexts:
    apRegDiscoveryInterval.setUnits("seconds")
_ApRegTelnetPassword_Type = OctetString
_ApRegTelnetPassword_Object = MibScalar
apRegTelnetPassword = _ApRegTelnetPassword_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 4, 4),
    _ApRegTelnetPassword_Type()
)
apRegTelnetPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRegTelnetPassword.setStatus("current")
_ApRegSSHPassword_Type = OctetString
_ApRegSSHPassword_Object = MibScalar
apRegSSHPassword = _ApRegSSHPassword_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 4, 5),
    _ApRegSSHPassword_Type()
)
apRegSSHPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRegSSHPassword.setStatus("current")
_ApRegUseClusterEncryption_Type = TruthValue
_ApRegUseClusterEncryption_Object = MibScalar
apRegUseClusterEncryption = _ApRegUseClusterEncryption_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 4, 6),
    _ApRegUseClusterEncryption_Type()
)
apRegUseClusterEncryption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRegUseClusterEncryption.setStatus("current")
_ApRegClusterSharedSecret_Type = OctetString
_ApRegClusterSharedSecret_Object = MibScalar
apRegClusterSharedSecret = _ApRegClusterSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 4, 7),
    _ApRegClusterSharedSecret_Type()
)
apRegClusterSharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRegClusterSharedSecret.setStatus("current")
_LoadBalancing_ObjectIdentity = ObjectIdentity
loadBalancing = _LoadBalancing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 5)
)
_LoadGroupTable_Object = MibTable
loadGroupTable = _LoadGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 5, 1)
)
if mibBuilder.loadTexts:
    loadGroupTable.setStatus("current")
_LoadGroupEntry_Object = MibTableRow
loadGroupEntry = _LoadGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 5, 1, 1)
)
loadGroupEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-HWC-MIB", "loadGroupID"),
)
if mibBuilder.loadTexts:
    loadGroupEntry.setStatus("current")
_LoadGroupID_Type = Unsigned32
_LoadGroupID_Object = MibTableColumn
loadGroupID = _LoadGroupID_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 5, 1, 1, 1),
    _LoadGroupID_Type()
)
loadGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadGroupID.setStatus("current")


class _LoadGroupName_Type(DisplayString):
    """Custom type loadGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_LoadGroupName_Type.__name__ = "DisplayString"
_LoadGroupName_Object = MibTableColumn
loadGroupName = _LoadGroupName_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 5, 1, 1, 2),
    _LoadGroupName_Type()
)
loadGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadGroupName.setStatus("current")


class _LoadGroupType_Type(Integer32):
    """Custom type loadGroupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clientBalancing", 0),
          ("radioBalancing", 1))
    )


_LoadGroupType_Type.__name__ = "Integer32"
_LoadGroupType_Object = MibTableColumn
loadGroupType = _LoadGroupType_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 5, 1, 1, 3),
    _LoadGroupType_Type()
)
loadGroupType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadGroupType.setStatus("current")


class _LoadGroupBandPreference_Type(Integer32):
    """Custom type loadGroupBandPreference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_LoadGroupBandPreference_Type.__name__ = "Integer32"
_LoadGroupBandPreference_Object = MibTableColumn
loadGroupBandPreference = _LoadGroupBandPreference_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 5, 1, 1, 4),
    _LoadGroupBandPreference_Type()
)
loadGroupBandPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadGroupBandPreference.setStatus("current")


class _LoadGroupLoadControl_Type(Integer32):
    """Custom type loadGroupLoadControl based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_LoadGroupLoadControl_Type.__name__ = "Integer32"
_LoadGroupLoadControl_Object = MibTableColumn
loadGroupLoadControl = _LoadGroupLoadControl_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 5, 1, 1, 5),
    _LoadGroupLoadControl_Type()
)
loadGroupLoadControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadGroupLoadControl.setStatus("deprecated")


class _LoadGroupClientCountRadio1_Type(Unsigned32):
    """Custom type loadGroupClientCountRadio1 based on Unsigned32"""
    defaultValue = 121

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60),
        ValueRangeConstraint(121, 121),
    )


_LoadGroupClientCountRadio1_Type.__name__ = "Unsigned32"
_LoadGroupClientCountRadio1_Object = MibTableColumn
loadGroupClientCountRadio1 = _LoadGroupClientCountRadio1_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 5, 1, 1, 6),
    _LoadGroupClientCountRadio1_Type()
)
loadGroupClientCountRadio1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadGroupClientCountRadio1.setStatus("current")


class _LoadGroupClientCountRadio2_Type(Unsigned32):
    """Custom type loadGroupClientCountRadio2 based on Unsigned32"""
    defaultValue = 121

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60),
        ValueRangeConstraint(121, 121),
    )


_LoadGroupClientCountRadio2_Type.__name__ = "Unsigned32"
_LoadGroupClientCountRadio2_Object = MibTableColumn
loadGroupClientCountRadio2 = _LoadGroupClientCountRadio2_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 5, 1, 1, 7),
    _LoadGroupClientCountRadio2_Type()
)
loadGroupClientCountRadio2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadGroupClientCountRadio2.setStatus("current")


class _LoadGroupLoadControlEnableR1_Type(Integer32):
    """Custom type loadGroupLoadControlEnableR1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_LoadGroupLoadControlEnableR1_Type.__name__ = "Integer32"
_LoadGroupLoadControlEnableR1_Object = MibTableColumn
loadGroupLoadControlEnableR1 = _LoadGroupLoadControlEnableR1_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 5, 1, 1, 8),
    _LoadGroupLoadControlEnableR1_Type()
)
loadGroupLoadControlEnableR1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadGroupLoadControlEnableR1.setStatus("current")


class _LoadGroupLoadControlEnableR2_Type(Integer32):
    """Custom type loadGroupLoadControlEnableR2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_LoadGroupLoadControlEnableR2_Type.__name__ = "Integer32"
_LoadGroupLoadControlEnableR2_Object = MibTableColumn
loadGroupLoadControlEnableR2 = _LoadGroupLoadControlEnableR2_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 5, 1, 1, 9),
    _LoadGroupLoadControlEnableR2_Type()
)
loadGroupLoadControlEnableR2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadGroupLoadControlEnableR2.setStatus("current")


class _LoadGroupLoadControlStrictLimitR1_Type(Integer32):
    """Custom type loadGroupLoadControlStrictLimitR1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_LoadGroupLoadControlStrictLimitR1_Type.__name__ = "Integer32"
_LoadGroupLoadControlStrictLimitR1_Object = MibTableColumn
loadGroupLoadControlStrictLimitR1 = _LoadGroupLoadControlStrictLimitR1_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 5, 1, 1, 10),
    _LoadGroupLoadControlStrictLimitR1_Type()
)
loadGroupLoadControlStrictLimitR1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadGroupLoadControlStrictLimitR1.setStatus("current")


class _LoadGroupLoadControlStrictLimitR2_Type(Integer32):
    """Custom type loadGroupLoadControlStrictLimitR2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_LoadGroupLoadControlStrictLimitR2_Type.__name__ = "Integer32"
_LoadGroupLoadControlStrictLimitR2_Object = MibTableColumn
loadGroupLoadControlStrictLimitR2 = _LoadGroupLoadControlStrictLimitR2_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 5, 1, 1, 11),
    _LoadGroupLoadControlStrictLimitR2_Type()
)
loadGroupLoadControlStrictLimitR2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadGroupLoadControlStrictLimitR2.setStatus("current")
_LoadGrpRadiosTable_Object = MibTable
loadGrpRadiosTable = _LoadGrpRadiosTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 5, 2)
)
if mibBuilder.loadTexts:
    loadGrpRadiosTable.setStatus("current")
_LoadGrpRadiosEntry_Object = MibTableRow
loadGrpRadiosEntry = _LoadGrpRadiosEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 5, 2, 1)
)
loadGrpRadiosEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-HWC-MIB", "loadGroupID"),
    (0, "HIPATH-WIRELESS-HWC-MIB", "apIndex"),
)
if mibBuilder.loadTexts:
    loadGrpRadiosEntry.setStatus("current")


class _LoadGrpRadiosRadio1_Type(Integer32):
    """Custom type loadGrpRadiosRadio1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("assigned", 1),
          ("notApplicable", 0),
          ("unassigned", 2))
    )


_LoadGrpRadiosRadio1_Type.__name__ = "Integer32"
_LoadGrpRadiosRadio1_Object = MibTableColumn
loadGrpRadiosRadio1 = _LoadGrpRadiosRadio1_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 5, 2, 1, 2),
    _LoadGrpRadiosRadio1_Type()
)
loadGrpRadiosRadio1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadGrpRadiosRadio1.setStatus("current")


class _LoadGrpRadiosRadio2_Type(Integer32):
    """Custom type loadGrpRadiosRadio2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("assigned", 1),
          ("notApplicable", 0),
          ("unassigned", 2))
    )


_LoadGrpRadiosRadio2_Type.__name__ = "Integer32"
_LoadGrpRadiosRadio2_Object = MibTableColumn
loadGrpRadiosRadio2 = _LoadGrpRadiosRadio2_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 5, 2, 1, 3),
    _LoadGrpRadiosRadio2_Type()
)
loadGrpRadiosRadio2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadGrpRadiosRadio2.setStatus("current")
_LoadGrpWlanTable_Object = MibTable
loadGrpWlanTable = _LoadGrpWlanTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 5, 3)
)
if mibBuilder.loadTexts:
    loadGrpWlanTable.setStatus("current")
_LoadGrpWlanEntry_Object = MibTableRow
loadGrpWlanEntry = _LoadGrpWlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 5, 3, 1)
)
loadGrpWlanEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-HWC-MIB", "loadGroupID"),
    (0, "HIPATH-WIRELESS-HWC-MIB", "wlanID"),
)
if mibBuilder.loadTexts:
    loadGrpWlanEntry.setStatus("current")
_LoadGrpWlanAssigned_Type = TruthValue
_LoadGrpWlanAssigned_Object = MibTableColumn
loadGrpWlanAssigned = _LoadGrpWlanAssigned_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 5, 3, 1, 1),
    _LoadGrpWlanAssigned_Type()
)
loadGrpWlanAssigned.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadGrpWlanAssigned.setStatus("current")
_ApMaintenanceCycle_ObjectIdentity = ObjectIdentity
apMaintenanceCycle = _ApMaintenanceCycle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 6)
)


class _Schedule_Type(Integer32):
    """Custom type schedule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("daily", 1),
          ("monthly", 3),
          ("never", 0),
          ("weekly", 2))
    )


_Schedule_Type.__name__ = "Integer32"
_Schedule_Object = MibScalar
schedule = _Schedule_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 6, 1),
    _Schedule_Type()
)
schedule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schedule.setStatus("current")


class _StartHour_Type(Integer32):
    """Custom type startHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_StartHour_Type.__name__ = "Integer32"
_StartHour_Object = MibScalar
startHour = _StartHour_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 6, 2),
    _StartHour_Type()
)
startHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    startHour.setStatus("current")


class _StartMinute_Type(Integer32):
    """Custom type startMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_StartMinute_Type.__name__ = "Integer32"
_StartMinute_Object = MibScalar
startMinute = _StartMinute_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 6, 3),
    _StartMinute_Type()
)
startMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    startMinute.setStatus("current")


class _Duration_Type(Integer32):
    """Custom type duration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 23),
    )


_Duration_Type.__name__ = "Integer32"
_Duration_Object = MibScalar
duration = _Duration_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 6, 4),
    _Duration_Type()
)
duration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    duration.setStatus("current")


class _RecurrenceDaily_Type(Integer32):
    """Custom type recurrenceDaily based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("everyDay", 0),
          ("everyWeekday", 1),
          ("everyWeekend", 2))
    )


_RecurrenceDaily_Type.__name__ = "Integer32"
_RecurrenceDaily_Object = MibScalar
recurrenceDaily = _RecurrenceDaily_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 6, 5),
    _RecurrenceDaily_Type()
)
recurrenceDaily.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    recurrenceDaily.setStatus("current")


class _RecurrenceWeekly_Type(Bits):
    """Custom type recurrenceWeekly based on Bits"""
    namedValues = NamedValues(
        *(("friday", 5),
          ("monday", 1),
          ("saturday", 6),
          ("sunday", 0),
          ("thursday", 4),
          ("tuesday", 2),
          ("wednesday", 3))
    )

_RecurrenceWeekly_Type.__name__ = "Bits"
_RecurrenceWeekly_Object = MibScalar
recurrenceWeekly = _RecurrenceWeekly_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 6, 6),
    _RecurrenceWeekly_Type()
)
recurrenceWeekly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    recurrenceWeekly.setStatus("current")


class _RecurrenceMonthly_Type(Bits):
    """Custom type recurrenceMonthly based on Bits"""
    namedValues = NamedValues(
        *(("fifth", 4),
          ("first", 0),
          ("fourth", 3),
          ("friday", 10),
          ("monday", 6),
          ("saturday", 11),
          ("second", 1),
          ("sunday", 5),
          ("third", 2),
          ("thursday", 9),
          ("tuesday", 7),
          ("wednesday", 8))
    )

_RecurrenceMonthly_Type.__name__ = "Bits"
_RecurrenceMonthly_Object = MibScalar
recurrenceMonthly = _RecurrenceMonthly_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 6, 7),
    _RecurrenceMonthly_Type()
)
recurrenceMonthly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    recurrenceMonthly.setStatus("current")


class _ApPlatforms_Type(Bits):
    """Custom type apPlatforms based on Bits"""
    namedValues = NamedValues(
        *(("ap2600", 0),
          ("ap2605", 1),
          ("ap2650", 2),
          ("ap3705", 5),
          ("ap3710", 6),
          ("ap3715", 7),
          ("ap3765", 8),
          ("ap3767", 9),
          ("ap3801", 10),
          ("ap3805", 11),
          ("ap3825", 12),
          ("ap3865", 13),
          ("ap3935", 14),
          ("ap3965", 15),
          ("ap4102", 3),
          ("w786", 4),
          ("w78xc", 16),
          ("w78xcsfp", 17))
    )

_ApPlatforms_Type.__name__ = "Bits"
_ApPlatforms_Object = MibScalar
apPlatforms = _ApPlatforms_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 5, 6, 8),
    _ApPlatforms_Type()
)
apPlatforms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apPlatforms.setStatus("current")
_MobileUnits_ObjectIdentity = ObjectIdentity
mobileUnits = _MobileUnits_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 6)
)
_MobileUnitCount_Type = Integer32
_MobileUnitCount_Object = MibScalar
mobileUnitCount = _MobileUnitCount_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 6, 1),
    _MobileUnitCount_Type()
)
mobileUnitCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mobileUnitCount.setStatus("current")
_MuTable_Object = MibTable
muTable = _MuTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 6, 2)
)
if mibBuilder.loadTexts:
    muTable.setStatus("current")
_MuEntry_Object = MibTableRow
muEntry = _MuEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 6, 2, 1)
)
muEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-HWC-MIB", "muMACAddress"),
)
if mibBuilder.loadTexts:
    muEntry.setStatus("current")
_MuMACAddress_Type = MacAddress
_MuMACAddress_Object = MibTableColumn
muMACAddress = _MuMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 6, 2, 1, 1),
    _MuMACAddress_Type()
)
muMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muMACAddress.setStatus("current")
_MuIPAddress_Type = IpAddress
_MuIPAddress_Object = MibTableColumn
muIPAddress = _MuIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 6, 2, 1, 2),
    _MuIPAddress_Type()
)
muIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muIPAddress.setStatus("current")
_MuUser_Type = OctetString
_MuUser_Object = MibTableColumn
muUser = _MuUser_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 6, 2, 1, 3),
    _MuUser_Type()
)
muUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muUser.setStatus("current")
_MuState_Type = TruthValue
_MuState_Object = MibTableColumn
muState = _MuState_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 6, 2, 1, 4),
    _MuState_Type()
)
muState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muState.setStatus("current")
_MuAPSerialNo_Type = OctetString
_MuAPSerialNo_Object = MibTableColumn
muAPSerialNo = _MuAPSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 6, 2, 1, 5),
    _MuAPSerialNo_Type()
)
muAPSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muAPSerialNo.setStatus("current")
_MuVnsSSID_Type = OctetString
_MuVnsSSID_Object = MibTableColumn
muVnsSSID = _MuVnsSSID_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 6, 2, 1, 6),
    _MuVnsSSID_Type()
)
muVnsSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muVnsSSID.setStatus("current")
_MuTxPackets_Type = Counter64
_MuTxPackets_Object = MibTableColumn
muTxPackets = _MuTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 6, 2, 1, 7),
    _MuTxPackets_Type()
)
muTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muTxPackets.setStatus("current")
_MuRxPackets_Type = Counter64
_MuRxPackets_Object = MibTableColumn
muRxPackets = _MuRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 6, 2, 1, 8),
    _MuRxPackets_Type()
)
muRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muRxPackets.setStatus("current")
_MuTxOctets_Type = Counter64
_MuTxOctets_Object = MibTableColumn
muTxOctets = _MuTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 6, 2, 1, 9),
    _MuTxOctets_Type()
)
muTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muTxOctets.setStatus("current")
_MuRxOctets_Type = Counter64
_MuRxOctets_Object = MibTableColumn
muRxOctets = _MuRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 6, 2, 1, 10),
    _MuRxOctets_Type()
)
muRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muRxOctets.setStatus("current")
_MuDuration_Type = Counter64
_MuDuration_Object = MibTableColumn
muDuration = _MuDuration_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 6, 2, 1, 11),
    _MuDuration_Type()
)
muDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muDuration.setStatus("current")
_MuAPName_Type = DisplayString
_MuAPName_Object = MibTableColumn
muAPName = _MuAPName_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 6, 2, 1, 12),
    _MuAPName_Type()
)
muAPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muAPName.setStatus("current")
_MuTopologyName_Type = DisplayString
_MuTopologyName_Object = MibTableColumn
muTopologyName = _MuTopologyName_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 6, 2, 1, 13),
    _MuTopologyName_Type()
)
muTopologyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muTopologyName.setStatus("current")
_MuPolicyName_Type = DisplayString
_MuPolicyName_Object = MibTableColumn
muPolicyName = _MuPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 6, 2, 1, 14),
    _MuPolicyName_Type()
)
muPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muPolicyName.setStatus("current")
_MuDefaultCoS_Type = DisplayString
_MuDefaultCoS_Object = MibTableColumn
muDefaultCoS = _MuDefaultCoS_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 6, 2, 1, 15),
    _MuDefaultCoS_Type()
)
muDefaultCoS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muDefaultCoS.setStatus("current")


class _MuConnectionProtocol_Type(Integer32):
    """Custom type muConnectionProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("a", 1),
          ("ac", 6),
          ("b", 3),
          ("g", 2),
          ("n24", 5),
          ("n50", 4),
          ("unknown", 0))
    )


_MuConnectionProtocol_Type.__name__ = "Integer32"
_MuConnectionProtocol_Object = MibTableColumn
muConnectionProtocol = _MuConnectionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 6, 2, 1, 16),
    _MuConnectionProtocol_Type()
)
muConnectionProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muConnectionProtocol.setStatus("current")


class _MuConnectionCapability_Type(Integer32):
    """Custom type muConnectionCapability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("a", 1),
          ("abg", 3),
          ("an", 4),
          ("bg", 2),
          ("bgn", 5),
          ("unknown", 0))
    )


_MuConnectionCapability_Type.__name__ = "Integer32"
_MuConnectionCapability_Object = MibTableColumn
muConnectionCapability = _MuConnectionCapability_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 6, 2, 1, 17),
    _MuConnectionCapability_Type()
)
muConnectionCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muConnectionCapability.setStatus("deprecated")
_MuWLANID_Type = Unsigned32
_MuWLANID_Object = MibTableColumn
muWLANID = _MuWLANID_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 6, 2, 1, 18),
    _MuWLANID_Type()
)
muWLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muWLANID.setStatus("current")
_MuBSSIDMac_Type = MacAddress
_MuBSSIDMac_Object = MibTableColumn
muBSSIDMac = _MuBSSIDMac_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 6, 2, 1, 19),
    _MuBSSIDMac_Type()
)
muBSSIDMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muBSSIDMac.setStatus("current")


class _MuDot11ConnectionCapability_Type(Bits):
    """Custom type muDot11ConnectionCapability based on Bits"""
    namedValues = NamedValues(
        *(("dot1124", 1),
          ("dot1150", 0),
          ("fastTransition", 13),
          ("greenfield", 12),
          ("oneStream", 4),
          ("threeSteam", 6),
          ("twoStream", 5),
          ("uapsdBackground", 9),
          ("uapsdBesteffort", 10),
          ("uapsdVideo", 8),
          ("uapsdVoice", 7),
          ("wmm", 11),
          ("wpaV1", 2),
          ("wpaV2", 3))
    )

_MuDot11ConnectionCapability_Type.__name__ = "Bits"
_MuDot11ConnectionCapability_Object = MibTableColumn
muDot11ConnectionCapability = _MuDot11ConnectionCapability_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 6, 2, 1, 20),
    _MuDot11ConnectionCapability_Type()
)
muDot11ConnectionCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muDot11ConnectionCapability.setStatus("current")
_MuTSPECTable_Object = MibTable
muTSPECTable = _MuTSPECTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 6, 3)
)
if mibBuilder.loadTexts:
    muTSPECTable.setStatus("current")
_MuTSPECEntry_Object = MibTableRow
muTSPECEntry = _MuTSPECEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 6, 3, 1)
)
muTSPECEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-HWC-MIB", "apIndex"),
    (0, "HIPATH-WIRELESS-HWC-MIB", "muMACAddress"),
    (0, "HIPATH-WIRELESS-HWC-MIB", "tspecAC"),
    (0, "HIPATH-WIRELESS-HWC-MIB", "tspecDirection"),
)
if mibBuilder.loadTexts:
    muTSPECEntry.setStatus("current")
_TspecMuMACAddress_Type = MacAddress
_TspecMuMACAddress_Object = MibTableColumn
tspecMuMACAddress = _TspecMuMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 6, 3, 1, 1),
    _TspecMuMACAddress_Type()
)
tspecMuMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tspecMuMACAddress.setStatus("current")


class _TspecAC_Type(Integer32):
    """Custom type tspecAC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("be", 0),
          ("bk", 1),
          ("nwme", 5),
          ("tvo", 4),
          ("vi", 2),
          ("vo", 3))
    )


_TspecAC_Type.__name__ = "Integer32"
_TspecAC_Object = MibTableColumn
tspecAC = _TspecAC_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 6, 3, 1, 2),
    _TspecAC_Type()
)
tspecAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tspecAC.setStatus("current")


class _TspecDirection_Type(Integer32):
    """Custom type tspecDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bidir", 3),
          ("dnlink", 1),
          ("reserved", 2),
          ("uplink", 0))
    )


_TspecDirection_Type.__name__ = "Integer32"
_TspecDirection_Object = MibTableColumn
tspecDirection = _TspecDirection_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 6, 3, 1, 3),
    _TspecDirection_Type()
)
tspecDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tspecDirection.setStatus("current")
_TspecApSerialNumber_Type = OctetString
_TspecApSerialNumber_Object = MibTableColumn
tspecApSerialNumber = _TspecApSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 6, 3, 1, 4),
    _TspecApSerialNumber_Type()
)
tspecApSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tspecApSerialNumber.setStatus("current")
_TspecMuIPAddress_Type = IpAddress
_TspecMuIPAddress_Object = MibTableColumn
tspecMuIPAddress = _TspecMuIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 6, 3, 1, 5),
    _TspecMuIPAddress_Type()
)
tspecMuIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tspecMuIPAddress.setStatus("current")
_TspecBssMac_Type = MacAddress
_TspecBssMac_Object = MibTableColumn
tspecBssMac = _TspecBssMac_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 6, 3, 1, 6),
    _TspecBssMac_Type()
)
tspecBssMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tspecBssMac.setStatus("current")
_TspecSsid_Type = DisplayString
_TspecSsid_Object = MibTableColumn
tspecSsid = _TspecSsid_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 6, 3, 1, 7),
    _TspecSsid_Type()
)
tspecSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tspecSsid.setStatus("current")
_TspecMDR_Type = Unsigned32
_TspecMDR_Object = MibTableColumn
tspecMDR = _TspecMDR_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 6, 3, 1, 8),
    _TspecMDR_Type()
)
tspecMDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tspecMDR.setStatus("current")
_TspecNMS_Type = Unsigned32
_TspecNMS_Object = MibTableColumn
tspecNMS = _TspecNMS_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 6, 3, 1, 9),
    _TspecNMS_Type()
)
tspecNMS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tspecNMS.setStatus("current")
_TspecSBA_Type = Unsigned32
_TspecSBA_Object = MibTableColumn
tspecSBA = _TspecSBA_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 6, 3, 1, 10),
    _TspecSBA_Type()
)
tspecSBA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tspecSBA.setStatus("current")
_TspecDlRate_Type = DisplayString
_TspecDlRate_Object = MibTableColumn
tspecDlRate = _TspecDlRate_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 6, 3, 1, 11),
    _TspecDlRate_Type()
)
tspecDlRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tspecDlRate.setStatus("current")
_TspecUlRate_Type = DisplayString
_TspecUlRate_Object = MibTableColumn
tspecUlRate = _TspecUlRate_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 6, 3, 1, 12),
    _TspecUlRate_Type()
)
tspecUlRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tspecUlRate.setStatus("current")
_TspecDlViolations_Type = DisplayString
_TspecDlViolations_Object = MibTableColumn
tspecDlViolations = _TspecDlViolations_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 6, 3, 1, 13),
    _TspecDlViolations_Type()
)
tspecDlViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tspecDlViolations.setStatus("current")
_TspecUlViolations_Type = DisplayString
_TspecUlViolations_Object = MibTableColumn
tspecUlViolations = _TspecUlViolations_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 6, 3, 1, 14),
    _TspecUlViolations_Type()
)
tspecUlViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tspecUlViolations.setStatus("current")


class _TspecProtocol_Type(Integer32):
    """Custom type tspecProtocol based on Integer32"""
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
        *(("proto80211a", 1),
          ("proto80211an", 4),
          ("proto80211b", 3),
          ("proto80211bgn", 5),
          ("proto80211g", 2))
    )


_TspecProtocol_Type.__name__ = "Integer32"
_TspecProtocol_Object = MibTableColumn
tspecProtocol = _TspecProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 6, 3, 1, 15),
    _TspecProtocol_Type()
)
tspecProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tspecProtocol.setStatus("current")


class _MuACLType_Type(Integer32):
    """Custom type muACLType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blacklist", 1),
          ("whitelist", 2))
    )


_MuACLType_Type.__name__ = "Integer32"
_MuACLType_Object = MibScalar
muACLType = _MuACLType_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 6, 4),
    _MuACLType_Type()
)
muACLType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muACLType.setStatus("current")
_MuACLTable_Object = MibTable
muACLTable = _MuACLTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 6, 5)
)
if mibBuilder.loadTexts:
    muACLTable.setStatus("current")
_MuACLEntry_Object = MibTableRow
muACLEntry = _MuACLEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 6, 5, 1)
)
muACLEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-HWC-MIB", "muACLMACAddress"),
)
if mibBuilder.loadTexts:
    muACLEntry.setStatus("current")
_MuACLMACAddress_Type = MacAddress
_MuACLMACAddress_Object = MibTableColumn
muACLMACAddress = _MuACLMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 6, 5, 1, 1),
    _MuACLMACAddress_Type()
)
muACLMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muACLMACAddress.setStatus("current")
_MuACLRowStatus_Type = RowStatus
_MuACLRowStatus_Object = MibTableColumn
muACLRowStatus = _MuACLRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 6, 5, 1, 2),
    _MuACLRowStatus_Type()
)
muACLRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    muACLRowStatus.setStatus("current")
_MuAccessListTable_Object = MibTable
muAccessListTable = _MuAccessListTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 6, 6)
)
if mibBuilder.loadTexts:
    muAccessListTable.setStatus("current")
_MuAccessListEntry_Object = MibTableRow
muAccessListEntry = _MuAccessListEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 6, 6, 1)
)
muAccessListEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-HWC-MIB", "muAccessListMACAddress"),
)
if mibBuilder.loadTexts:
    muAccessListEntry.setStatus("current")
_MuAccessListMACAddress_Type = MacAddress
_MuAccessListMACAddress_Object = MibTableColumn
muAccessListMACAddress = _MuAccessListMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 6, 6, 1, 1),
    _MuAccessListMACAddress_Type()
)
muAccessListMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muAccessListMACAddress.setStatus("current")


class _MuAccessListBitmaskLength_Type(Integer32):
    """Custom type muAccessListBitmaskLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(24,
              36,
              48)
        )
    )
    namedValues = NamedValues(
        *(("bits24", 24),
          ("bits36", 36),
          ("bits48", 48))
    )


_MuAccessListBitmaskLength_Type.__name__ = "Integer32"
_MuAccessListBitmaskLength_Object = MibTableColumn
muAccessListBitmaskLength = _MuAccessListBitmaskLength_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 6, 6, 1, 2),
    _MuAccessListBitmaskLength_Type()
)
muAccessListBitmaskLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    muAccessListBitmaskLength.setStatus("current")
_MuAccessListRowStatus_Type = RowStatus
_MuAccessListRowStatus_Object = MibTableColumn
muAccessListRowStatus = _MuAccessListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 6, 6, 1, 3),
    _MuAccessListRowStatus_Type()
)
muAccessListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    muAccessListRowStatus.setStatus("current")
_Associations_ObjectIdentity = ObjectIdentity
associations = _Associations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 7)
)
_AssocCount_Type = Integer32
_AssocCount_Object = MibScalar
assocCount = _AssocCount_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 7, 1),
    _AssocCount_Type()
)
assocCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    assocCount.setStatus("current")
_AssocTable_Object = MibTable
assocTable = _AssocTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 7, 2)
)
if mibBuilder.loadTexts:
    assocTable.setStatus("current")
_AssocEntry_Object = MibTableRow
assocEntry = _AssocEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 7, 2, 1)
)
assocEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-HWC-MIB", "assocMUMacAddress"),
    (0, "HIPATH-WIRELESS-HWC-MIB", "apIndex"),
    (0, "HIPATH-WIRELESS-HWC-MIB", "assocStartSysUpTime"),
)
if mibBuilder.loadTexts:
    assocEntry.setStatus("current")
_AssocMUMacAddress_Type = MacAddress
_AssocMUMacAddress_Object = MibTableColumn
assocMUMacAddress = _AssocMUMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 7, 2, 1, 1),
    _AssocMUMacAddress_Type()
)
assocMUMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assocMUMacAddress.setStatus("current")
_AssocStartSysUpTime_Type = TimeTicks
_AssocStartSysUpTime_Object = MibTableColumn
assocStartSysUpTime = _AssocStartSysUpTime_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 7, 2, 1, 2),
    _AssocStartSysUpTime_Type()
)
assocStartSysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assocStartSysUpTime.setStatus("current")
_AssocTxPackets_Type = Counter64
_AssocTxPackets_Object = MibTableColumn
assocTxPackets = _AssocTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 7, 2, 1, 3),
    _AssocTxPackets_Type()
)
assocTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assocTxPackets.setStatus("current")
_AssocRxPackets_Type = Counter64
_AssocRxPackets_Object = MibTableColumn
assocRxPackets = _AssocRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 7, 2, 1, 4),
    _AssocRxPackets_Type()
)
assocRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assocRxPackets.setStatus("current")
_AssocTxOctets_Type = Counter64
_AssocTxOctets_Object = MibTableColumn
assocTxOctets = _AssocTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 7, 2, 1, 5),
    _AssocTxOctets_Type()
)
assocTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assocTxOctets.setStatus("current")
_AssocRxOctets_Type = Counter64
_AssocRxOctets_Object = MibTableColumn
assocRxOctets = _AssocRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 7, 2, 1, 6),
    _AssocRxOctets_Type()
)
assocRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assocRxOctets.setStatus("current")
_AssocDuration_Type = Integer32
_AssocDuration_Object = MibTableColumn
assocDuration = _AssocDuration_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 7, 2, 1, 7),
    _AssocDuration_Type()
)
assocDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    assocDuration.setStatus("current")
_AssocVnsIfIndex_Type = InterfaceIndex
_AssocVnsIfIndex_Object = MibTableColumn
assocVnsIfIndex = _AssocVnsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 7, 2, 1, 8),
    _AssocVnsIfIndex_Type()
)
assocVnsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assocVnsIfIndex.setStatus("current")
_Protocols_ObjectIdentity = ObjectIdentity
protocols = _Protocols_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 8)
)
_Wassp_ObjectIdentity = ObjectIdentity
wassp = _Wassp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 8, 1)
)
_LogNotifications_ObjectIdentity = ObjectIdentity
logNotifications = _LogNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 9)
)
_LogEventSeverityThreshold_Type = LogEventSeverity
_LogEventSeverityThreshold_Object = MibScalar
logEventSeverityThreshold = _LogEventSeverityThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 9, 1),
    _LogEventSeverityThreshold_Type()
)
logEventSeverityThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logEventSeverityThreshold.setStatus("current")
_LogEventSeverity_Type = LogEventSeverity
_LogEventSeverity_Object = MibScalar
logEventSeverity = _LogEventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 9, 3),
    _LogEventSeverity_Type()
)
logEventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logEventSeverity.setStatus("current")
_LogEventComponent_Type = OctetString
_LogEventComponent_Object = MibScalar
logEventComponent = _LogEventComponent_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 9, 4),
    _LogEventComponent_Type()
)
logEventComponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logEventComponent.setStatus("current")
_LogEventDescription_Type = OctetString
_LogEventDescription_Object = MibScalar
logEventDescription = _LogEventDescription_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 9, 5),
    _LogEventDescription_Type()
)
logEventDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logEventDescription.setStatus("current")
_Sites_ObjectIdentity = ObjectIdentity
sites = _Sites_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 10)
)
_SiteMaxEntries_Type = Unsigned32
_SiteMaxEntries_Object = MibScalar
siteMaxEntries = _SiteMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 10, 1),
    _SiteMaxEntries_Type()
)
siteMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteMaxEntries.setStatus("current")
_SiteNumEntries_Type = Unsigned32
_SiteNumEntries_Object = MibScalar
siteNumEntries = _SiteNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 10, 2),
    _SiteNumEntries_Type()
)
siteNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteNumEntries.setStatus("current")
_SiteTableNextAvailableIndex_Type = Unsigned32
_SiteTableNextAvailableIndex_Object = MibScalar
siteTableNextAvailableIndex = _SiteTableNextAvailableIndex_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 10, 3),
    _SiteTableNextAvailableIndex_Type()
)
siteTableNextAvailableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteTableNextAvailableIndex.setStatus("current")
_SiteTable_Object = MibTable
siteTable = _SiteTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 10, 4)
)
if mibBuilder.loadTexts:
    siteTable.setStatus("current")
_SiteEntry_Object = MibTableRow
siteEntry = _SiteEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 10, 4, 1)
)
siteEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-HWC-MIB", "siteID"),
)
if mibBuilder.loadTexts:
    siteEntry.setStatus("current")
_SiteID_Type = Unsigned32
_SiteID_Object = MibTableColumn
siteID = _SiteID_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 10, 4, 1, 1),
    _SiteID_Type()
)
siteID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteID.setStatus("current")
_SiteRowStatus_Type = RowStatus
_SiteRowStatus_Object = MibTableColumn
siteRowStatus = _SiteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 10, 4, 1, 2),
    _SiteRowStatus_Type()
)
siteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    siteRowStatus.setStatus("current")


class _SiteName_Type(DisplayString):
    """Custom type siteName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SiteName_Type.__name__ = "DisplayString"
_SiteName_Object = MibTableColumn
siteName = _SiteName_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 10, 4, 1, 3),
    _SiteName_Type()
)
siteName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    siteName.setStatus("current")
_SiteLocalRadiusAuthentication_Type = TruthValue
_SiteLocalRadiusAuthentication_Object = MibTableColumn
siteLocalRadiusAuthentication = _SiteLocalRadiusAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 10, 4, 1, 4),
    _SiteLocalRadiusAuthentication_Type()
)
siteLocalRadiusAuthentication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    siteLocalRadiusAuthentication.setStatus("current")


class _SiteDefaultDNSServer_Type(DisplayString):
    """Custom type siteDefaultDNSServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SiteDefaultDNSServer_Type.__name__ = "DisplayString"
_SiteDefaultDNSServer_Object = MibTableColumn
siteDefaultDNSServer = _SiteDefaultDNSServer_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 10, 4, 1, 5),
    _SiteDefaultDNSServer_Type()
)
siteDefaultDNSServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    siteDefaultDNSServer.setStatus("current")
_SiteEnableSecureTunnel_Type = TruthValue
_SiteEnableSecureTunnel_Object = MibTableColumn
siteEnableSecureTunnel = _SiteEnableSecureTunnel_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 10, 4, 1, 6),
    _SiteEnableSecureTunnel_Type()
)
siteEnableSecureTunnel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    siteEnableSecureTunnel.setStatus("current")
_SiteEncryptCommAPtoController_Type = TruthValue
_SiteEncryptCommAPtoController_Object = MibTableColumn
siteEncryptCommAPtoController = _SiteEncryptCommAPtoController_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 10, 4, 1, 7),
    _SiteEncryptCommAPtoController_Type()
)
siteEncryptCommAPtoController.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    siteEncryptCommAPtoController.setStatus("current")
_SiteEncryptCommBetweenAPs_Type = TruthValue
_SiteEncryptCommBetweenAPs_Object = MibTableColumn
siteEncryptCommBetweenAPs = _SiteEncryptCommBetweenAPs_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 10, 4, 1, 8),
    _SiteEncryptCommBetweenAPs_Type()
)
siteEncryptCommBetweenAPs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    siteEncryptCommBetweenAPs.setStatus("current")


class _SiteBandPreferenceEnable_Type(Integer32):
    """Custom type siteBandPreferenceEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SiteBandPreferenceEnable_Type.__name__ = "Integer32"
_SiteBandPreferenceEnable_Object = MibTableColumn
siteBandPreferenceEnable = _SiteBandPreferenceEnable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 10, 4, 1, 9),
    _SiteBandPreferenceEnable_Type()
)
siteBandPreferenceEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    siteBandPreferenceEnable.setStatus("current")


class _SiteLoadControlEnableR1_Type(Integer32):
    """Custom type siteLoadControlEnableR1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SiteLoadControlEnableR1_Type.__name__ = "Integer32"
_SiteLoadControlEnableR1_Object = MibTableColumn
siteLoadControlEnableR1 = _SiteLoadControlEnableR1_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 10, 4, 1, 10),
    _SiteLoadControlEnableR1_Type()
)
siteLoadControlEnableR1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    siteLoadControlEnableR1.setStatus("current")


class _SiteLoadControlEnableR2_Type(Integer32):
    """Custom type siteLoadControlEnableR2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SiteLoadControlEnableR2_Type.__name__ = "Integer32"
_SiteLoadControlEnableR2_Object = MibTableColumn
siteLoadControlEnableR2 = _SiteLoadControlEnableR2_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 10, 4, 1, 11),
    _SiteLoadControlEnableR2_Type()
)
siteLoadControlEnableR2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    siteLoadControlEnableR2.setStatus("current")


class _SiteMaxClientR1_Type(Unsigned32):
    """Custom type siteMaxClientR1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_SiteMaxClientR1_Type.__name__ = "Unsigned32"
_SiteMaxClientR1_Object = MibTableColumn
siteMaxClientR1 = _SiteMaxClientR1_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 10, 4, 1, 12),
    _SiteMaxClientR1_Type()
)
siteMaxClientR1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    siteMaxClientR1.setStatus("current")


class _SiteMaxClientR2_Type(Unsigned32):
    """Custom type siteMaxClientR2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_SiteMaxClientR2_Type.__name__ = "Unsigned32"
_SiteMaxClientR2_Object = MibTableColumn
siteMaxClientR2 = _SiteMaxClientR2_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 10, 4, 1, 13),
    _SiteMaxClientR2_Type()
)
siteMaxClientR2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    siteMaxClientR2.setStatus("current")


class _SiteStrictLimitEnableR1_Type(Integer32):
    """Custom type siteStrictLimitEnableR1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SiteStrictLimitEnableR1_Type.__name__ = "Integer32"
_SiteStrictLimitEnableR1_Object = MibTableColumn
siteStrictLimitEnableR1 = _SiteStrictLimitEnableR1_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 10, 4, 1, 14),
    _SiteStrictLimitEnableR1_Type()
)
siteStrictLimitEnableR1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    siteStrictLimitEnableR1.setStatus("current")


class _SiteStrictLimitEnableR2_Type(Integer32):
    """Custom type siteStrictLimitEnableR2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SiteStrictLimitEnableR2_Type.__name__ = "Integer32"
_SiteStrictLimitEnableR2_Object = MibTableColumn
siteStrictLimitEnableR2 = _SiteStrictLimitEnableR2_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 10, 4, 1, 15),
    _SiteStrictLimitEnableR2_Type()
)
siteStrictLimitEnableR2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    siteStrictLimitEnableR2.setStatus("current")
_SiteReplaceStnIDwithSiteName_Type = TruthValue
_SiteReplaceStnIDwithSiteName_Object = MibTableColumn
siteReplaceStnIDwithSiteName = _SiteReplaceStnIDwithSiteName_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 10, 4, 1, 16),
    _SiteReplaceStnIDwithSiteName_Type()
)
siteReplaceStnIDwithSiteName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    siteReplaceStnIDwithSiteName.setStatus("current")
_SitePolicyTable_Object = MibTable
sitePolicyTable = _SitePolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 10, 5)
)
if mibBuilder.loadTexts:
    sitePolicyTable.setStatus("current")
_SitePolicyEntry_Object = MibTableRow
sitePolicyEntry = _SitePolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 10, 5, 1)
)
sitePolicyEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-HWC-MIB", "siteID"),
    (0, "HIPATH-WIRELESS-HWC-MIB", "sitePolicyID"),
)
if mibBuilder.loadTexts:
    sitePolicyEntry.setStatus("current")
_SitePolicyID_Type = Unsigned32
_SitePolicyID_Object = MibTableColumn
sitePolicyID = _SitePolicyID_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 10, 5, 1, 1),
    _SitePolicyID_Type()
)
sitePolicyID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sitePolicyID.setStatus("current")


class _SitePolicyMember_Type(Integer32):
    """Custom type sitePolicyMember based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("isMember", 1),
          ("notMember", 0))
    )


_SitePolicyMember_Type.__name__ = "Integer32"
_SitePolicyMember_Object = MibTableColumn
sitePolicyMember = _SitePolicyMember_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 10, 5, 1, 2),
    _SitePolicyMember_Type()
)
sitePolicyMember.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sitePolicyMember.setStatus("current")
_SiteCosTable_Object = MibTable
siteCosTable = _SiteCosTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 10, 6)
)
if mibBuilder.loadTexts:
    siteCosTable.setStatus("current")
_SiteCosEntry_Object = MibTableRow
siteCosEntry = _SiteCosEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 10, 6, 1)
)
siteCosEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-HWC-MIB", "siteID"),
    (0, "HIPATH-WIRELESS-HWC-MIB", "siteCoSID"),
)
if mibBuilder.loadTexts:
    siteCosEntry.setStatus("current")
_SiteCoSID_Type = Unsigned32
_SiteCoSID_Object = MibTableColumn
siteCoSID = _SiteCoSID_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 10, 6, 1, 1),
    _SiteCoSID_Type()
)
siteCoSID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    siteCoSID.setStatus("current")


class _SiteCoSMember_Type(Integer32):
    """Custom type siteCoSMember based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("isMember", 1),
          ("notMember", 0))
    )


_SiteCoSMember_Type.__name__ = "Integer32"
_SiteCoSMember_Object = MibTableColumn
siteCoSMember = _SiteCoSMember_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 10, 6, 1, 2),
    _SiteCoSMember_Type()
)
siteCoSMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteCoSMember.setStatus("current")
_SiteAPTable_Object = MibTable
siteAPTable = _SiteAPTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 10, 7)
)
if mibBuilder.loadTexts:
    siteAPTable.setStatus("current")
_SiteAPEntry_Object = MibTableRow
siteAPEntry = _SiteAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 10, 7, 1)
)
siteAPEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-HWC-MIB", "siteID"),
    (0, "HIPATH-WIRELESS-HWC-MIB", "apIndex"),
)
if mibBuilder.loadTexts:
    siteAPEntry.setStatus("current")


class _SiteAPMember_Type(Integer32):
    """Custom type siteAPMember based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("isMember", 1),
          ("notMember", 0))
    )


_SiteAPMember_Type.__name__ = "Integer32"
_SiteAPMember_Object = MibTableColumn
siteAPMember = _SiteAPMember_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 10, 7, 1, 1),
    _SiteAPMember_Type()
)
siteAPMember.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteAPMember.setStatus("current")
_SiteWlanTable_Object = MibTable
siteWlanTable = _SiteWlanTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 10, 8)
)
if mibBuilder.loadTexts:
    siteWlanTable.setStatus("current")
_SiteWlanEntry_Object = MibTableRow
siteWlanEntry = _SiteWlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 10, 8, 1)
)
siteWlanEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-HWC-MIB", "siteID"),
    (0, "HIPATH-WIRELESS-HWC-MIB", "wlanID"),
    (0, "HIPATH-WIRELESS-HWC-MIB", "siteWlanApRadioIndex"),
)
if mibBuilder.loadTexts:
    siteWlanEntry.setStatus("current")


class _SiteWlanApRadioIndex_Type(Integer32):
    """Custom type siteWlanApRadioIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_SiteWlanApRadioIndex_Type.__name__ = "Integer32"
_SiteWlanApRadioIndex_Object = MibTableColumn
siteWlanApRadioIndex = _SiteWlanApRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 10, 8, 1, 1),
    _SiteWlanApRadioIndex_Type()
)
siteWlanApRadioIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    siteWlanApRadioIndex.setStatus("current")


class _SiteWlanApRadioAssigned_Type(Integer32):
    """Custom type siteWlanApRadioAssigned based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("assigned", 1),
          ("notAssigned", 0))
    )


_SiteWlanApRadioAssigned_Type.__name__ = "Integer32"
_SiteWlanApRadioAssigned_Object = MibTableColumn
siteWlanApRadioAssigned = _SiteWlanApRadioAssigned_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 10, 8, 1, 2),
    _SiteWlanApRadioAssigned_Type()
)
siteWlanApRadioAssigned.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteWlanApRadioAssigned.setStatus("current")
_WidsWips_ObjectIdentity = ObjectIdentity
widsWips = _WidsWips_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11)
)


class _MitigatorAnalysisEngine_Type(Integer32):
    """Custom type mitigatorAnalysisEngine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_MitigatorAnalysisEngine_Type.__name__ = "Integer32"
_MitigatorAnalysisEngine_Object = MibScalar
mitigatorAnalysisEngine = _MitigatorAnalysisEngine_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 1),
    _MitigatorAnalysisEngine_Type()
)
mitigatorAnalysisEngine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitigatorAnalysisEngine.setStatus("current")
_ScanGroupMaxEntries_Type = Unsigned32
_ScanGroupMaxEntries_Object = MibScalar
scanGroupMaxEntries = _ScanGroupMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 2),
    _ScanGroupMaxEntries_Type()
)
scanGroupMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanGroupMaxEntries.setStatus("current")
_ScanGroupsCurrentEntries_Type = Unsigned32
_ScanGroupsCurrentEntries_Object = MibScalar
scanGroupsCurrentEntries = _ScanGroupsCurrentEntries_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 3),
    _ScanGroupsCurrentEntries_Type()
)
scanGroupsCurrentEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanGroupsCurrentEntries.setStatus("current")
_ActiveThreatsCounts_Type = Unsigned32
_ActiveThreatsCounts_Object = MibScalar
activeThreatsCounts = _ActiveThreatsCounts_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 4),
    _ActiveThreatsCounts_Type()
)
activeThreatsCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeThreatsCounts.setStatus("current")
_FriendlyAPCounts_Type = Unsigned32
_FriendlyAPCounts_Object = MibScalar
friendlyAPCounts = _FriendlyAPCounts_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 5),
    _FriendlyAPCounts_Type()
)
friendlyAPCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friendlyAPCounts.setStatus("current")
_UncategorizedAPCounts_Type = Unsigned32
_UncategorizedAPCounts_Object = MibScalar
uncategorizedAPCounts = _UncategorizedAPCounts_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 6),
    _UncategorizedAPCounts_Type()
)
uncategorizedAPCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uncategorizedAPCounts.setStatus("current")
_WidsWipsEngineTable_Object = MibTable
widsWipsEngineTable = _WidsWipsEngineTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 11)
)
if mibBuilder.loadTexts:
    widsWipsEngineTable.setStatus("current")
_WidsWipsEngineEntry_Object = MibTableRow
widsWipsEngineEntry = _WidsWipsEngineEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 11, 1)
)
widsWipsEngineEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-HWC-MIB", "widsWipsEngineControllerIPAddress"),
)
if mibBuilder.loadTexts:
    widsWipsEngineEntry.setStatus("current")
_WidsWipsEngineRowStatus_Type = RowStatus
_WidsWipsEngineRowStatus_Object = MibTableColumn
widsWipsEngineRowStatus = _WidsWipsEngineRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 11, 1, 1),
    _WidsWipsEngineRowStatus_Type()
)
widsWipsEngineRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    widsWipsEngineRowStatus.setStatus("current")
_WidsWipsEngineControllerIPAddress_Type = IpAddress
_WidsWipsEngineControllerIPAddress_Object = MibTableColumn
widsWipsEngineControllerIPAddress = _WidsWipsEngineControllerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 11, 1, 2),
    _WidsWipsEngineControllerIPAddress_Type()
)
widsWipsEngineControllerIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    widsWipsEngineControllerIPAddress.setStatus("current")


class _WidsWipsEnginePollInterval_Type(Integer32):
    """Custom type widsWipsEnginePollInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 60),
    )


_WidsWipsEnginePollInterval_Type.__name__ = "Integer32"
_WidsWipsEnginePollInterval_Object = MibTableColumn
widsWipsEnginePollInterval = _WidsWipsEnginePollInterval_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 11, 1, 3),
    _WidsWipsEnginePollInterval_Type()
)
widsWipsEnginePollInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    widsWipsEnginePollInterval.setStatus("current")


class _WidsWipsEnginePollRetry_Type(Integer32):
    """Custom type widsWipsEnginePollRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_WidsWipsEnginePollRetry_Type.__name__ = "Integer32"
_WidsWipsEnginePollRetry_Object = MibTableColumn
widsWipsEnginePollRetry = _WidsWipsEnginePollRetry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 11, 1, 4),
    _WidsWipsEnginePollRetry_Type()
)
widsWipsEnginePollRetry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    widsWipsEnginePollRetry.setStatus("current")
_InServiceScanGroupTable_Object = MibTable
inServiceScanGroupTable = _InServiceScanGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 12)
)
if mibBuilder.loadTexts:
    inServiceScanGroupTable.setStatus("current")
_InServiceScanGroupEntry_Object = MibTableRow
inServiceScanGroupEntry = _InServiceScanGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 12, 1)
)
inServiceScanGroupEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-HWC-MIB", "scanGroupProfileID"),
)
if mibBuilder.loadTexts:
    inServiceScanGroupEntry.setStatus("current")
_ScanGroupProfileID_Type = Unsigned32
_ScanGroupProfileID_Object = MibTableColumn
scanGroupProfileID = _ScanGroupProfileID_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 12, 1, 1),
    _ScanGroupProfileID_Type()
)
scanGroupProfileID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scanGroupProfileID.setStatus("current")


class _InSrvScanGrpName_Type(DisplayString):
    """Custom type inSrvScanGrpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_InSrvScanGrpName_Type.__name__ = "DisplayString"
_InSrvScanGrpName_Object = MibTableColumn
inSrvScanGrpName = _InSrvScanGrpName_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 12, 1, 2),
    _InSrvScanGrpName_Type()
)
inSrvScanGrpName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    inSrvScanGrpName.setStatus("current")


class _InSrvScanGrpSecurityThreats_Type(Integer32):
    """Custom type inSrvScanGrpSecurityThreats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_InSrvScanGrpSecurityThreats_Type.__name__ = "Integer32"
_InSrvScanGrpSecurityThreats_Object = MibTableColumn
inSrvScanGrpSecurityThreats = _InSrvScanGrpSecurityThreats_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 12, 1, 3),
    _InSrvScanGrpSecurityThreats_Type()
)
inSrvScanGrpSecurityThreats.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    inSrvScanGrpSecurityThreats.setStatus("current")


class _InSrvScanGrpMaxConcurrentAttacksPerAP_Type(Integer32):
    """Custom type inSrvScanGrpMaxConcurrentAttacksPerAP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_InSrvScanGrpMaxConcurrentAttacksPerAP_Type.__name__ = "Integer32"
_InSrvScanGrpMaxConcurrentAttacksPerAP_Object = MibTableColumn
inSrvScanGrpMaxConcurrentAttacksPerAP = _InSrvScanGrpMaxConcurrentAttacksPerAP_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 12, 1, 4),
    _InSrvScanGrpMaxConcurrentAttacksPerAP_Type()
)
inSrvScanGrpMaxConcurrentAttacksPerAP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    inSrvScanGrpMaxConcurrentAttacksPerAP.setStatus("current")


class _InSrvScanGrpCounterMeasuresType_Type(Bits):
    """Custom type inSrvScanGrpCounterMeasuresType based on Bits"""
    namedValues = NamedValues(
        *(("adHocModeDevice", 6),
          ("dropFloodAttack", 4),
          ("externalHoneypotAPs", 0),
          ("internalHoneypotAPs", 2),
          ("removeDosAttack", 5),
          ("roamingToFriendlyAPs", 1),
          ("rogueAP", 7),
          ("spoofedAPs", 3))
    )

_InSrvScanGrpCounterMeasuresType_Type.__name__ = "Bits"
_InSrvScanGrpCounterMeasuresType_Object = MibTableColumn
inSrvScanGrpCounterMeasuresType = _InSrvScanGrpCounterMeasuresType_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 12, 1, 5),
    _InSrvScanGrpCounterMeasuresType_Type()
)
inSrvScanGrpCounterMeasuresType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    inSrvScanGrpCounterMeasuresType.setStatus("current")


class _InSrvScanGrpScan2400MHzSelection_Type(Bits):
    """Custom type inSrvScanGrpScan2400MHzSelection based on Bits"""
    namedValues = NamedValues(
        *(("frequency2412MHz", 0),
          ("frequency2417MHz", 1),
          ("frequency2422MHz", 2),
          ("frequency2427MHz", 3),
          ("frequency2432MHz", 4),
          ("frequency2437MHz", 5),
          ("frequency2442MHz", 6),
          ("frequency2447MHz", 7),
          ("frequency2452MHz", 8),
          ("frequency2457MHz", 9),
          ("frequency2462MHz", 10),
          ("frequency2467MHz", 11),
          ("frequency2472MHz", 12),
          ("frequency2484MHz", 13))
    )

_InSrvScanGrpScan2400MHzSelection_Type.__name__ = "Bits"
_InSrvScanGrpScan2400MHzSelection_Object = MibTableColumn
inSrvScanGrpScan2400MHzSelection = _InSrvScanGrpScan2400MHzSelection_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 12, 1, 6),
    _InSrvScanGrpScan2400MHzSelection_Type()
)
inSrvScanGrpScan2400MHzSelection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    inSrvScanGrpScan2400MHzSelection.setStatus("current")


class _InSrvScanGrpScan5GHzSelection_Type(Bits):
    """Custom type inSrvScanGrpScan5GHzSelection based on Bits"""
    namedValues = NamedValues(
        *(("frequency4920MHz", 27),
          ("frequency4940MHz", 28),
          ("frequency4960MHz", 29),
          ("frequency4980MHz", 30),
          ("frequency5040MHz", 0),
          ("frequency5060MHz", 1),
          ("frequency5080MHz", 2),
          ("frequency5180MHz", 3),
          ("frequency5200MHz", 4),
          ("frequency5220MHz", 5),
          ("frequency5240MHz", 6),
          ("frequency5260MHz", 7),
          ("frequency5280MHz", 8),
          ("frequency5300MHz", 9),
          ("frequency5320MHz", 10),
          ("frequency5500MHz", 11),
          ("frequency5520MHz", 12),
          ("frequency5540MHz", 13),
          ("frequency5560MHz", 14),
          ("frequency5580MHz", 15),
          ("frequency5600MHz", 16),
          ("frequency5620MHz", 17),
          ("frequency5640MHz", 18),
          ("frequency5660MHz", 19),
          ("frequency5680MHz", 20),
          ("frequency5700MHz", 21),
          ("frequency5745MHz", 22),
          ("frequency5765MHz", 23),
          ("frequency5785MHz", 24),
          ("frequency5805MHz", 25),
          ("frequency5825MHz", 26))
    )

_InSrvScanGrpScan5GHzSelection_Type.__name__ = "Bits"
_InSrvScanGrpScan5GHzSelection_Object = MibTableColumn
inSrvScanGrpScan5GHzSelection = _InSrvScanGrpScan5GHzSelection_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 12, 1, 7),
    _InSrvScanGrpScan5GHzSelection_Type()
)
inSrvScanGrpScan5GHzSelection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    inSrvScanGrpScan5GHzSelection.setStatus("current")
_InSrvScanGrpblockAdHocClientsPeriod_Type = Integer32
_InSrvScanGrpblockAdHocClientsPeriod_Object = MibTableColumn
inSrvScanGrpblockAdHocClientsPeriod = _InSrvScanGrpblockAdHocClientsPeriod_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 12, 1, 8),
    _InSrvScanGrpblockAdHocClientsPeriod_Type()
)
inSrvScanGrpblockAdHocClientsPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    inSrvScanGrpblockAdHocClientsPeriod.setStatus("current")


class _InSrvScanGrpClassifySourceIF_Type(Integer32):
    """Custom type inSrvScanGrpClassifySourceIF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_InSrvScanGrpClassifySourceIF_Type.__name__ = "Integer32"
_InSrvScanGrpClassifySourceIF_Object = MibTableColumn
inSrvScanGrpClassifySourceIF = _InSrvScanGrpClassifySourceIF_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 12, 1, 9),
    _InSrvScanGrpClassifySourceIF_Type()
)
inSrvScanGrpClassifySourceIF.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    inSrvScanGrpClassifySourceIF.setStatus("current")
_InSrvScanGrpRowStatus_Type = RowStatus
_InSrvScanGrpRowStatus_Object = MibTableColumn
inSrvScanGrpRowStatus = _InSrvScanGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 12, 1, 10),
    _InSrvScanGrpRowStatus_Type()
)
inSrvScanGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    inSrvScanGrpRowStatus.setStatus("current")


class _InSrvScanGrpDetectRogueAP_Type(Integer32):
    """Custom type inSrvScanGrpDetectRogueAP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_InSrvScanGrpDetectRogueAP_Type.__name__ = "Integer32"
_InSrvScanGrpDetectRogueAP_Object = MibTableColumn
inSrvScanGrpDetectRogueAP = _InSrvScanGrpDetectRogueAP_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 12, 1, 11),
    _InSrvScanGrpDetectRogueAP_Type()
)
inSrvScanGrpDetectRogueAP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    inSrvScanGrpDetectRogueAP.setStatus("current")
_InSrvScanGrpListeningPort_Type = Integer32
_InSrvScanGrpListeningPort_Object = MibTableColumn
inSrvScanGrpListeningPort = _InSrvScanGrpListeningPort_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 12, 1, 12),
    _InSrvScanGrpListeningPort_Type()
)
inSrvScanGrpListeningPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inSrvScanGrpListeningPort.setStatus("current")
_OutOfServiceScanGroupTable_Object = MibTable
outOfServiceScanGroupTable = _OutOfServiceScanGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 13)
)
if mibBuilder.loadTexts:
    outOfServiceScanGroupTable.setStatus("current")
_OutOfServiceScanGroupEntry_Object = MibTableRow
outOfServiceScanGroupEntry = _OutOfServiceScanGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 13, 1)
)
outOfServiceScanGroupEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-HWC-MIB", "scanGroupProfileID"),
)
if mibBuilder.loadTexts:
    outOfServiceScanGroupEntry.setStatus("current")


class _OutOfSrvScanGrpName_Type(DisplayString):
    """Custom type outOfSrvScanGrpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_OutOfSrvScanGrpName_Type.__name__ = "DisplayString"
_OutOfSrvScanGrpName_Object = MibTableColumn
outOfSrvScanGrpName = _OutOfSrvScanGrpName_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 13, 1, 1),
    _OutOfSrvScanGrpName_Type()
)
outOfSrvScanGrpName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    outOfSrvScanGrpName.setStatus("current")


class _OutOfSrvScanGrpRadio_Type(Integer32):
    """Custom type outOfSrvScanGrpRadio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("radio1", 1),
          ("radio2", 2))
    )


_OutOfSrvScanGrpRadio_Type.__name__ = "Integer32"
_OutOfSrvScanGrpRadio_Object = MibTableColumn
outOfSrvScanGrpRadio = _OutOfSrvScanGrpRadio_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 13, 1, 2),
    _OutOfSrvScanGrpRadio_Type()
)
outOfSrvScanGrpRadio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    outOfSrvScanGrpRadio.setStatus("current")


class _OutOfSrvScanGrpChannelList_Type(Integer32):
    """Custom type outOfSrvScanGrpChannelList based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              999)
        )
    )
    namedValues = NamedValues(
        *(("allChannel", 0),
          ("currentChannel", 999))
    )


_OutOfSrvScanGrpChannelList_Type.__name__ = "Integer32"
_OutOfSrvScanGrpChannelList_Object = MibTableColumn
outOfSrvScanGrpChannelList = _OutOfSrvScanGrpChannelList_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 13, 1, 3),
    _OutOfSrvScanGrpChannelList_Type()
)
outOfSrvScanGrpChannelList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    outOfSrvScanGrpChannelList.setStatus("current")


class _OutOfSrvScanGrpScanType_Type(Integer32):
    """Custom type outOfSrvScanGrpScanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 0),
          ("passive", 1))
    )


_OutOfSrvScanGrpScanType_Type.__name__ = "Integer32"
_OutOfSrvScanGrpScanType_Object = MibTableColumn
outOfSrvScanGrpScanType = _OutOfSrvScanGrpScanType_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 13, 1, 4),
    _OutOfSrvScanGrpScanType_Type()
)
outOfSrvScanGrpScanType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    outOfSrvScanGrpScanType.setStatus("current")


class _OutOfSrvScanGrpChannelDwellTime_Type(Integer32):
    """Custom type outOfSrvScanGrpChannelDwellTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 500),
    )


_OutOfSrvScanGrpChannelDwellTime_Type.__name__ = "Integer32"
_OutOfSrvScanGrpChannelDwellTime_Object = MibTableColumn
outOfSrvScanGrpChannelDwellTime = _OutOfSrvScanGrpChannelDwellTime_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 13, 1, 5),
    _OutOfSrvScanGrpChannelDwellTime_Type()
)
outOfSrvScanGrpChannelDwellTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    outOfSrvScanGrpChannelDwellTime.setStatus("current")


class _OutOfSrvScanGrpScanTimeInterval_Type(Integer32):
    """Custom type outOfSrvScanGrpScanTimeInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 120),
    )


_OutOfSrvScanGrpScanTimeInterval_Type.__name__ = "Integer32"
_OutOfSrvScanGrpScanTimeInterval_Object = MibTableColumn
outOfSrvScanGrpScanTimeInterval = _OutOfSrvScanGrpScanTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 13, 1, 6),
    _OutOfSrvScanGrpScanTimeInterval_Type()
)
outOfSrvScanGrpScanTimeInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    outOfSrvScanGrpScanTimeInterval.setStatus("current")


class _OutOfSrvScanGrpSecurityScan_Type(Integer32):
    """Custom type outOfSrvScanGrpSecurityScan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_OutOfSrvScanGrpSecurityScan_Type.__name__ = "Integer32"
_OutOfSrvScanGrpSecurityScan_Object = MibTableColumn
outOfSrvScanGrpSecurityScan = _OutOfSrvScanGrpSecurityScan_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 13, 1, 7),
    _OutOfSrvScanGrpSecurityScan_Type()
)
outOfSrvScanGrpSecurityScan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    outOfSrvScanGrpSecurityScan.setStatus("current")


class _OutOfSrvScanGrpScanActivity_Type(Integer32):
    """Custom type outOfSrvScanGrpScanActivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("stop", 0))
    )


_OutOfSrvScanGrpScanActivity_Type.__name__ = "Integer32"
_OutOfSrvScanGrpScanActivity_Object = MibTableColumn
outOfSrvScanGrpScanActivity = _OutOfSrvScanGrpScanActivity_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 13, 1, 8),
    _OutOfSrvScanGrpScanActivity_Type()
)
outOfSrvScanGrpScanActivity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    outOfSrvScanGrpScanActivity.setStatus("current")
_OutOfSrvScanGrpScanRowStatus_Type = Integer32
_OutOfSrvScanGrpScanRowStatus_Object = MibTableColumn
outOfSrvScanGrpScanRowStatus = _OutOfSrvScanGrpScanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 13, 1, 9),
    _OutOfSrvScanGrpScanRowStatus_Type()
)
outOfSrvScanGrpScanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    outOfSrvScanGrpScanRowStatus.setStatus("current")
_ScanGroupAPAssignmentTable_Object = MibTable
scanGroupAPAssignmentTable = _ScanGroupAPAssignmentTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 14)
)
if mibBuilder.loadTexts:
    scanGroupAPAssignmentTable.setStatus("current")
_ScanGroupAPAssignmentEntry_Object = MibTableRow
scanGroupAPAssignmentEntry = _ScanGroupAPAssignmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 14, 1)
)
scanGroupAPAssignmentEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-HWC-MIB", "scanGroupProfileID"),
    (0, "HIPATH-WIRELESS-HWC-MIB", "scanGroupAPAssignApSerial"),
    (0, "HIPATH-WIRELESS-HWC-MIB", "widsWipsEngineControllerIPAddress"),
)
if mibBuilder.loadTexts:
    scanGroupAPAssignmentEntry.setStatus("current")


class _ScanGroupAPAssignApSerial_Type(OctetString):
    """Custom type scanGroupAPAssignApSerial based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_ScanGroupAPAssignApSerial_Type.__name__ = "OctetString"
_ScanGroupAPAssignApSerial_Object = MibTableColumn
scanGroupAPAssignApSerial = _ScanGroupAPAssignApSerial_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 14, 1, 1),
    _ScanGroupAPAssignApSerial_Type()
)
scanGroupAPAssignApSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanGroupAPAssignApSerial.setStatus("current")


class _ScanGroupAPAssignGroupName_Type(DisplayString):
    """Custom type scanGroupAPAssignGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ScanGroupAPAssignGroupName_Type.__name__ = "DisplayString"
_ScanGroupAPAssignGroupName_Object = MibTableColumn
scanGroupAPAssignGroupName = _ScanGroupAPAssignGroupName_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 14, 1, 2),
    _ScanGroupAPAssignGroupName_Type()
)
scanGroupAPAssignGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanGroupAPAssignGroupName.setStatus("current")


class _ScanGroupAPAssignName_Type(DisplayString):
    """Custom type scanGroupAPAssignName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ScanGroupAPAssignName_Type.__name__ = "DisplayString"
_ScanGroupAPAssignName_Object = MibTableColumn
scanGroupAPAssignName = _ScanGroupAPAssignName_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 14, 1, 3),
    _ScanGroupAPAssignName_Type()
)
scanGroupAPAssignName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanGroupAPAssignName.setStatus("current")


class _ScanGroupAPAssignRadio1_Type(Integer32):
    """Custom type scanGroupAPAssignRadio1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              8,
              16,
              18,
              19,
              20,
              32,
              34,
              35,
              36)
        )
    )
    namedValues = NamedValues(
        *(("a", 4),
          ("an", 20),
          ("anStrict", 36),
          ("b", 1),
          ("bg", 3),
          ("bgn", 19),
          ("bgnStrict", 35),
          ("g", 2),
          ("gn", 18),
          ("gnStrict", 34),
          ("j", 8),
          ("n", 16),
          ("nStrict", 32),
          ("off", 0))
    )


_ScanGroupAPAssignRadio1_Type.__name__ = "Integer32"
_ScanGroupAPAssignRadio1_Object = MibTableColumn
scanGroupAPAssignRadio1 = _ScanGroupAPAssignRadio1_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 14, 1, 4),
    _ScanGroupAPAssignRadio1_Type()
)
scanGroupAPAssignRadio1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scanGroupAPAssignRadio1.setStatus("current")


class _ScanGroupAPAssignRadio2_Type(Integer32):
    """Custom type scanGroupAPAssignRadio2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              8,
              16,
              18,
              19,
              20,
              32,
              34,
              35,
              36)
        )
    )
    namedValues = NamedValues(
        *(("a", 4),
          ("an", 20),
          ("anStrict", 36),
          ("b", 1),
          ("bg", 3),
          ("bgn", 19),
          ("bgnStrict", 35),
          ("g", 2),
          ("gn", 18),
          ("gnStrict", 34),
          ("j", 8),
          ("n", 16),
          ("nStrict", 32),
          ("off", 0))
    )


_ScanGroupAPAssignRadio2_Type.__name__ = "Integer32"
_ScanGroupAPAssignRadio2_Object = MibTableColumn
scanGroupAPAssignRadio2 = _ScanGroupAPAssignRadio2_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 14, 1, 5),
    _ScanGroupAPAssignRadio2_Type()
)
scanGroupAPAssignRadio2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scanGroupAPAssignRadio2.setStatus("current")


class _ScanGroupAPAssignInactiveAP_Type(Integer32):
    """Custom type scanGroupAPAssignInactiveAP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_ScanGroupAPAssignInactiveAP_Type.__name__ = "Integer32"
_ScanGroupAPAssignInactiveAP_Object = MibTableColumn
scanGroupAPAssignInactiveAP = _ScanGroupAPAssignInactiveAP_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 14, 1, 6),
    _ScanGroupAPAssignInactiveAP_Type()
)
scanGroupAPAssignInactiveAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scanGroupAPAssignInactiveAP.setStatus("current")


class _ScanGroupAPAssignAllowScanning_Type(Integer32):
    """Custom type scanGroupAPAssignAllowScanning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("notAllow", 0))
    )


_ScanGroupAPAssignAllowScanning_Type.__name__ = "Integer32"
_ScanGroupAPAssignAllowScanning_Object = MibTableColumn
scanGroupAPAssignAllowScanning = _ScanGroupAPAssignAllowScanning_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 14, 1, 7),
    _ScanGroupAPAssignAllowScanning_Type()
)
scanGroupAPAssignAllowScanning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scanGroupAPAssignAllowScanning.setStatus("current")


class _ScanGroupAPAssignAllowSpectrumAnalysis_Type(Integer32):
    """Custom type scanGroupAPAssignAllowSpectrumAnalysis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("notAllow", 0))
    )


_ScanGroupAPAssignAllowSpectrumAnalysis_Type.__name__ = "Integer32"
_ScanGroupAPAssignAllowSpectrumAnalysis_Object = MibTableColumn
scanGroupAPAssignAllowSpectrumAnalysis = _ScanGroupAPAssignAllowSpectrumAnalysis_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 14, 1, 8),
    _ScanGroupAPAssignAllowSpectrumAnalysis_Type()
)
scanGroupAPAssignAllowSpectrumAnalysis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scanGroupAPAssignAllowSpectrumAnalysis.setStatus("current")
_ScanGroupAPAssignControllerIPAddress_Type = IpAddress
_ScanGroupAPAssignControllerIPAddress_Object = MibTableColumn
scanGroupAPAssignControllerIPAddress = _ScanGroupAPAssignControllerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 14, 1, 9),
    _ScanGroupAPAssignControllerIPAddress_Type()
)
scanGroupAPAssignControllerIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scanGroupAPAssignControllerIPAddress.setStatus("current")


class _ScanGroupAPAssignFordwardingService_Type(Bits):
    """Custom type scanGroupAPAssignFordwardingService based on Bits"""
    namedValues = NamedValues(
        *(("assignedToLoadGroup", 1),
          ("assignedToSite", 0),
          ("assignedToWlanService", 2))
    )

_ScanGroupAPAssignFordwardingService_Type.__name__ = "Bits"
_ScanGroupAPAssignFordwardingService_Object = MibTableColumn
scanGroupAPAssignFordwardingService = _ScanGroupAPAssignFordwardingService_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 14, 1, 10),
    _ScanGroupAPAssignFordwardingService_Type()
)
scanGroupAPAssignFordwardingService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanGroupAPAssignFordwardingService.setStatus("current")
_ScanAPTable_Object = MibTable
scanAPTable = _ScanAPTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 15)
)
if mibBuilder.loadTexts:
    scanAPTable.setStatus("current")
_ScanAPEntry_Object = MibTableRow
scanAPEntry = _ScanAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 15, 1)
)
scanAPEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-HWC-MIB", "scanAPControllerIPAddress"),
    (0, "HIPATH-WIRELESS-HWC-MIB", "scanAPSerialNumber"),
)
if mibBuilder.loadTexts:
    scanAPEntry.setStatus("current")
_ScanAPControllerIPAddress_Type = IpAddress
_ScanAPControllerIPAddress_Object = MibTableColumn
scanAPControllerIPAddress = _ScanAPControllerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 15, 1, 1),
    _ScanAPControllerIPAddress_Type()
)
scanAPControllerIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanAPControllerIPAddress.setStatus("current")


class _ScanAPSerialNumber_Type(OctetString):
    """Custom type scanAPSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_ScanAPSerialNumber_Type.__name__ = "OctetString"
_ScanAPSerialNumber_Object = MibTableColumn
scanAPSerialNumber = _ScanAPSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 15, 1, 2),
    _ScanAPSerialNumber_Type()
)
scanAPSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scanAPSerialNumber.setStatus("current")


class _ScanAPAcessPointName_Type(DisplayString):
    """Custom type scanAPAcessPointName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ScanAPAcessPointName_Type.__name__ = "DisplayString"
_ScanAPAcessPointName_Object = MibTableColumn
scanAPAcessPointName = _ScanAPAcessPointName_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 15, 1, 3),
    _ScanAPAcessPointName_Type()
)
scanAPAcessPointName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scanAPAcessPointName.setStatus("current")
_ScanAPRowStatus_Type = RowStatus
_ScanAPRowStatus_Object = MibTableColumn
scanAPRowStatus = _ScanAPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 15, 1, 4),
    _ScanAPRowStatus_Type()
)
scanAPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scanAPRowStatus.setStatus("current")


class _ScanAPProfileName_Type(DisplayString):
    """Custom type scanAPProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ScanAPProfileName_Type.__name__ = "DisplayString"
_ScanAPProfileName_Object = MibTableColumn
scanAPProfileName = _ScanAPProfileName_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 15, 1, 5),
    _ScanAPProfileName_Type()
)
scanAPProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scanAPProfileName.setStatus("current")


class _ScanAPProfileType_Type(Integer32):
    """Custom type scanAPProfileType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("guardianScan", 2),
          ("inServiceScan", 1),
          ("outOfServiceScan", 3))
    )


_ScanAPProfileType_Type.__name__ = "Integer32"
_ScanAPProfileType_Object = MibTableColumn
scanAPProfileType = _ScanAPProfileType_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 15, 1, 6),
    _ScanAPProfileType_Type()
)
scanAPProfileType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    scanAPProfileType.setStatus("current")
_FriendlyAPTable_Object = MibTable
friendlyAPTable = _FriendlyAPTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 16)
)
if mibBuilder.loadTexts:
    friendlyAPTable.setStatus("current")
_FriendlyAPEntry_Object = MibTableRow
friendlyAPEntry = _FriendlyAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 16, 1)
)
friendlyAPEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-HWC-MIB", "friendlyAPMacAddress"),
)
if mibBuilder.loadTexts:
    friendlyAPEntry.setStatus("current")
_FriendlyAPMacAddress_Type = MacAddress
_FriendlyAPMacAddress_Object = MibTableColumn
friendlyAPMacAddress = _FriendlyAPMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 16, 1, 1),
    _FriendlyAPMacAddress_Type()
)
friendlyAPMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friendlyAPMacAddress.setStatus("current")


class _FriendlyAPSSID_Type(DisplayString):
    """Custom type friendlyAPSSID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FriendlyAPSSID_Type.__name__ = "DisplayString"
_FriendlyAPSSID_Object = MibTableColumn
friendlyAPSSID = _FriendlyAPSSID_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 16, 1, 2),
    _FriendlyAPSSID_Type()
)
friendlyAPSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friendlyAPSSID.setStatus("current")


class _FriendlyAPDescription_Type(DisplayString):
    """Custom type friendlyAPDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_FriendlyAPDescription_Type.__name__ = "DisplayString"
_FriendlyAPDescription_Object = MibTableColumn
friendlyAPDescription = _FriendlyAPDescription_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 16, 1, 3),
    _FriendlyAPDescription_Type()
)
friendlyAPDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    friendlyAPDescription.setStatus("current")


class _FriendlyAPManufacturer_Type(DisplayString):
    """Custom type friendlyAPManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_FriendlyAPManufacturer_Type.__name__ = "DisplayString"
_FriendlyAPManufacturer_Object = MibTableColumn
friendlyAPManufacturer = _FriendlyAPManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 16, 1, 4),
    _FriendlyAPManufacturer_Type()
)
friendlyAPManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    friendlyAPManufacturer.setStatus("current")
_UncategorizedAPTable_Object = MibTable
uncategorizedAPTable = _UncategorizedAPTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 17)
)
if mibBuilder.loadTexts:
    uncategorizedAPTable.setStatus("current")
_UncategorizedAPEntry_Object = MibTableRow
uncategorizedAPEntry = _UncategorizedAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 17, 1)
)
uncategorizedAPEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-HWC-MIB", "uncategorizedAPMAC"),
)
if mibBuilder.loadTexts:
    uncategorizedAPEntry.setStatus("current")
_UncategorizedAPMAC_Type = MacAddress
_UncategorizedAPMAC_Object = MibTableColumn
uncategorizedAPMAC = _UncategorizedAPMAC_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 17, 1, 1),
    _UncategorizedAPMAC_Type()
)
uncategorizedAPMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uncategorizedAPMAC.setStatus("current")
_UncategorizedAPDescption_Type = DisplayString
_UncategorizedAPDescption_Object = MibTableColumn
uncategorizedAPDescption = _UncategorizedAPDescption_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 17, 1, 2),
    _UncategorizedAPDescption_Type()
)
uncategorizedAPDescption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uncategorizedAPDescption.setStatus("current")
_UncategorizedAPManufacturer_Type = DisplayString
_UncategorizedAPManufacturer_Object = MibTableColumn
uncategorizedAPManufacturer = _UncategorizedAPManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 17, 1, 3),
    _UncategorizedAPManufacturer_Type()
)
uncategorizedAPManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uncategorizedAPManufacturer.setStatus("current")


class _UncategorizedAPClassify_Type(Integer32):
    """Custom type uncategorizedAPClassify based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("clasifyAsAuthorized", 1),
          ("clasifyAsExternalHoneypotThreat", 5),
          ("clasifyAsInternalHoneypotThreat", 4),
          ("clasifyAsThreatForReport", 3),
          ("classifyAsFriendlyAP", 2),
          ("noAction", 0))
    )


_UncategorizedAPClassify_Type.__name__ = "Integer32"
_UncategorizedAPClassify_Object = MibTableColumn
uncategorizedAPClassify = _UncategorizedAPClassify_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 17, 1, 4),
    _UncategorizedAPClassify_Type()
)
uncategorizedAPClassify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uncategorizedAPClassify.setStatus("current")


class _UncategorizedAPSSID_Type(DisplayString):
    """Custom type uncategorizedAPSSID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_UncategorizedAPSSID_Type.__name__ = "DisplayString"
_UncategorizedAPSSID_Object = MibTableColumn
uncategorizedAPSSID = _UncategorizedAPSSID_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 17, 1, 5),
    _UncategorizedAPSSID_Type()
)
uncategorizedAPSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uncategorizedAPSSID.setStatus("current")
_AuthorizedAPTable_Object = MibTable
authorizedAPTable = _AuthorizedAPTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 18)
)
if mibBuilder.loadTexts:
    authorizedAPTable.setStatus("current")
_AuthorizedAPEntry_Object = MibTableRow
authorizedAPEntry = _AuthorizedAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 18, 1)
)
authorizedAPEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-HWC-MIB", "authorizedAPMAC"),
)
if mibBuilder.loadTexts:
    authorizedAPEntry.setStatus("current")
_AuthorizedAPMAC_Type = MacAddress
_AuthorizedAPMAC_Object = MibTableColumn
authorizedAPMAC = _AuthorizedAPMAC_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 18, 1, 1),
    _AuthorizedAPMAC_Type()
)
authorizedAPMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    authorizedAPMAC.setStatus("current")
_AuthorizedAPDescription_Type = DisplayString
_AuthorizedAPDescription_Object = MibTableColumn
authorizedAPDescription = _AuthorizedAPDescription_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 18, 1, 2),
    _AuthorizedAPDescription_Type()
)
authorizedAPDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    authorizedAPDescription.setStatus("current")
_AuthorizedAPManufacturer_Type = DisplayString
_AuthorizedAPManufacturer_Object = MibTableColumn
authorizedAPManufacturer = _AuthorizedAPManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 18, 1, 3),
    _AuthorizedAPManufacturer_Type()
)
authorizedAPManufacturer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    authorizedAPManufacturer.setStatus("current")


class _AuthorizedAPClassify_Type(Integer32):
    """Custom type authorizedAPClassify based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("classifyAsFriendlyAP", 1),
          ("noAction", 0))
    )


_AuthorizedAPClassify_Type.__name__ = "Integer32"
_AuthorizedAPClassify_Object = MibTableColumn
authorizedAPClassify = _AuthorizedAPClassify_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 18, 1, 4),
    _AuthorizedAPClassify_Type()
)
authorizedAPClassify.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    authorizedAPClassify.setStatus("current")
_AuthorizedAPRowStatus_Type = RowStatus
_AuthorizedAPRowStatus_Object = MibTableColumn
authorizedAPRowStatus = _AuthorizedAPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 18, 1, 5),
    _AuthorizedAPRowStatus_Type()
)
authorizedAPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    authorizedAPRowStatus.setStatus("current")
_ProhibitedAPTable_Object = MibTable
prohibitedAPTable = _ProhibitedAPTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 19)
)
if mibBuilder.loadTexts:
    prohibitedAPTable.setStatus("current")
_ProhibitedAPEntry_Object = MibTableRow
prohibitedAPEntry = _ProhibitedAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 19, 1)
)
prohibitedAPEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-HWC-MIB", "prohibitedAPMAC"),
)
if mibBuilder.loadTexts:
    prohibitedAPEntry.setStatus("current")
_ProhibitedAPMAC_Type = MacAddress
_ProhibitedAPMAC_Object = MibTableColumn
prohibitedAPMAC = _ProhibitedAPMAC_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 19, 1, 1),
    _ProhibitedAPMAC_Type()
)
prohibitedAPMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prohibitedAPMAC.setStatus("current")


class _ProhibitedAPCategory_Type(Integer32):
    """Custom type prohibitedAPCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              65529,
              65530,
              65531,
              65532,
              65533,
              65534)
        )
    )
    namedValues = NamedValues(
        *(("authorized", 65534),
          ("externalHoneyPot", 65530),
          ("friendly", 65532),
          ("internalHoneyPot", 65531),
          ("notAvailable", 0),
          ("perauthorized", 65533),
          ("reportPresenceOnly", 65529))
    )


_ProhibitedAPCategory_Type.__name__ = "Integer32"
_ProhibitedAPCategory_Object = MibTableColumn
prohibitedAPCategory = _ProhibitedAPCategory_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 19, 1, 2),
    _ProhibitedAPCategory_Type()
)
prohibitedAPCategory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prohibitedAPCategory.setStatus("current")
_ProhibitedAPDescription_Type = DisplayString
_ProhibitedAPDescription_Object = MibTableColumn
prohibitedAPDescription = _ProhibitedAPDescription_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 19, 1, 3),
    _ProhibitedAPDescription_Type()
)
prohibitedAPDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prohibitedAPDescription.setStatus("current")
_ProhibitedAPManufacturer_Type = DisplayString
_ProhibitedAPManufacturer_Object = MibTableColumn
prohibitedAPManufacturer = _ProhibitedAPManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 19, 1, 4),
    _ProhibitedAPManufacturer_Type()
)
prohibitedAPManufacturer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prohibitedAPManufacturer.setStatus("current")


class _ProhibitedAPClassify_Type(Integer32):
    """Custom type prohibitedAPClassify based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("classifyAsFriendlyAP", 1),
          ("noAction", 2))
    )


_ProhibitedAPClassify_Type.__name__ = "Integer32"
_ProhibitedAPClassify_Object = MibTableColumn
prohibitedAPClassify = _ProhibitedAPClassify_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 19, 1, 5),
    _ProhibitedAPClassify_Type()
)
prohibitedAPClassify.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prohibitedAPClassify.setStatus("current")
_ProhibitedAPRowStatus_Type = RowStatus
_ProhibitedAPRowStatus_Object = MibTableColumn
prohibitedAPRowStatus = _ProhibitedAPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 19, 1, 6),
    _ProhibitedAPRowStatus_Type()
)
prohibitedAPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prohibitedAPRowStatus.setStatus("current")
_DedicatedScanGroupTable_Object = MibTable
dedicatedScanGroupTable = _DedicatedScanGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 20)
)
if mibBuilder.loadTexts:
    dedicatedScanGroupTable.setStatus("current")
_DedicatedScanGroupEntry_Object = MibTableRow
dedicatedScanGroupEntry = _DedicatedScanGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 20, 1)
)
dedicatedScanGroupEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-HWC-MIB", "scanGroupProfileID"),
)
if mibBuilder.loadTexts:
    dedicatedScanGroupEntry.setStatus("current")


class _DedicatedScanGrpName_Type(DisplayString):
    """Custom type dedicatedScanGrpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_DedicatedScanGrpName_Type.__name__ = "DisplayString"
_DedicatedScanGrpName_Object = MibTableColumn
dedicatedScanGrpName = _DedicatedScanGrpName_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 20, 1, 1),
    _DedicatedScanGrpName_Type()
)
dedicatedScanGrpName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dedicatedScanGrpName.setStatus("current")


class _DedicatedScanGrpSecurityThreats_Type(Integer32):
    """Custom type dedicatedScanGrpSecurityThreats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_DedicatedScanGrpSecurityThreats_Type.__name__ = "Integer32"
_DedicatedScanGrpSecurityThreats_Object = MibTableColumn
dedicatedScanGrpSecurityThreats = _DedicatedScanGrpSecurityThreats_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 20, 1, 2),
    _DedicatedScanGrpSecurityThreats_Type()
)
dedicatedScanGrpSecurityThreats.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dedicatedScanGrpSecurityThreats.setStatus("current")


class _DedicatedScanGrpMaxConcurrentAttacksPerAP_Type(Integer32):
    """Custom type dedicatedScanGrpMaxConcurrentAttacksPerAP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_DedicatedScanGrpMaxConcurrentAttacksPerAP_Type.__name__ = "Integer32"
_DedicatedScanGrpMaxConcurrentAttacksPerAP_Object = MibTableColumn
dedicatedScanGrpMaxConcurrentAttacksPerAP = _DedicatedScanGrpMaxConcurrentAttacksPerAP_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 20, 1, 3),
    _DedicatedScanGrpMaxConcurrentAttacksPerAP_Type()
)
dedicatedScanGrpMaxConcurrentAttacksPerAP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dedicatedScanGrpMaxConcurrentAttacksPerAP.setStatus("current")


class _DedicatedScanGrpCounterMeasures_Type(Bits):
    """Custom type dedicatedScanGrpCounterMeasures based on Bits"""
    namedValues = NamedValues(
        *(("adHocModeDevice", 6),
          ("dropFloodAttack", 4),
          ("externalHoneypotAPs", 0),
          ("internalHoneypotAPs", 2),
          ("removeDosAttack", 5),
          ("roamingToFriendlyAPs", 1),
          ("rogueAP", 7),
          ("spoofedAPs", 3))
    )

_DedicatedScanGrpCounterMeasures_Type.__name__ = "Bits"
_DedicatedScanGrpCounterMeasures_Object = MibTableColumn
dedicatedScanGrpCounterMeasures = _DedicatedScanGrpCounterMeasures_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 20, 1, 4),
    _DedicatedScanGrpCounterMeasures_Type()
)
dedicatedScanGrpCounterMeasures.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dedicatedScanGrpCounterMeasures.setStatus("current")


class _DedicatedScanGrpScan2400MHzFreq_Type(Bits):
    """Custom type dedicatedScanGrpScan2400MHzFreq based on Bits"""
    namedValues = NamedValues(
        *(("frequency2412MHz", 0),
          ("frequency2417MHz", 1),
          ("frequency2422MHz", 2),
          ("frequency2427MHz", 3),
          ("frequency2432MHz", 4),
          ("frequency2437MHz", 5),
          ("frequency2442MHz", 6),
          ("frequency2447MHz", 7),
          ("frequency2452MHz", 8),
          ("frequency2457MHz", 9),
          ("frequency2462MHz", 10),
          ("frequency2467MHz", 11),
          ("frequency2472MHz", 12),
          ("frequency2484MHz", 13))
    )

_DedicatedScanGrpScan2400MHzFreq_Type.__name__ = "Bits"
_DedicatedScanGrpScan2400MHzFreq_Object = MibTableColumn
dedicatedScanGrpScan2400MHzFreq = _DedicatedScanGrpScan2400MHzFreq_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 20, 1, 5),
    _DedicatedScanGrpScan2400MHzFreq_Type()
)
dedicatedScanGrpScan2400MHzFreq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dedicatedScanGrpScan2400MHzFreq.setStatus("current")


class _DedicatedScanGrpScan5GHzFreq_Type(Bits):
    """Custom type dedicatedScanGrpScan5GHzFreq based on Bits"""
    namedValues = NamedValues(
        *(("frequency4920MHz", 27),
          ("frequency4940MHz", 28),
          ("frequency4960MHz", 29),
          ("frequency4980MHz", 30),
          ("frequency5040MHz", 0),
          ("frequency5060MHz", 1),
          ("frequency5080MHz", 2),
          ("frequency5180MHz", 3),
          ("frequency5200MHz", 4),
          ("frequency5220MHz", 5),
          ("frequency5240MHz", 6),
          ("frequency5260MHz", 7),
          ("frequency5280MHz", 8),
          ("frequency5300MHz", 9),
          ("frequency5320MHz", 10),
          ("frequency5500MHz", 11),
          ("frequency5520MHz", 12),
          ("frequency5540MHz", 13),
          ("frequency5560MHz", 14),
          ("frequency5580MHz", 15),
          ("frequency5600MHz", 16),
          ("frequency5620MHz", 17),
          ("frequency5640MHz", 18),
          ("frequency5660MHz", 19),
          ("frequency5680MHz", 20),
          ("frequency5700MHz", 21),
          ("frequency5745MHz", 22),
          ("frequency5765MHz", 23),
          ("frequency5785MHz", 24),
          ("frequency5805MHz", 25),
          ("frequency5825MHz", 26))
    )

_DedicatedScanGrpScan5GHzFreq_Type.__name__ = "Bits"
_DedicatedScanGrpScan5GHzFreq_Object = MibTableColumn
dedicatedScanGrpScan5GHzFreq = _DedicatedScanGrpScan5GHzFreq_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 20, 1, 6),
    _DedicatedScanGrpScan5GHzFreq_Type()
)
dedicatedScanGrpScan5GHzFreq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dedicatedScanGrpScan5GHzFreq.setStatus("current")
_DedicatedScanGrpBlockAdHocPeriod_Type = Integer32
_DedicatedScanGrpBlockAdHocPeriod_Object = MibTableColumn
dedicatedScanGrpBlockAdHocPeriod = _DedicatedScanGrpBlockAdHocPeriod_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 20, 1, 7),
    _DedicatedScanGrpBlockAdHocPeriod_Type()
)
dedicatedScanGrpBlockAdHocPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dedicatedScanGrpBlockAdHocPeriod.setStatus("current")


class _DedicatedScanGrpClassifySourceIF_Type(Integer32):
    """Custom type dedicatedScanGrpClassifySourceIF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_DedicatedScanGrpClassifySourceIF_Type.__name__ = "Integer32"
_DedicatedScanGrpClassifySourceIF_Object = MibTableColumn
dedicatedScanGrpClassifySourceIF = _DedicatedScanGrpClassifySourceIF_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 20, 1, 8),
    _DedicatedScanGrpClassifySourceIF_Type()
)
dedicatedScanGrpClassifySourceIF.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dedicatedScanGrpClassifySourceIF.setStatus("current")
_DedicatedScanGrpRowStatus_Type = RowStatus
_DedicatedScanGrpRowStatus_Object = MibTableColumn
dedicatedScanGrpRowStatus = _DedicatedScanGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 20, 1, 9),
    _DedicatedScanGrpRowStatus_Type()
)
dedicatedScanGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dedicatedScanGrpRowStatus.setStatus("current")


class _DedicatedScanGrpDetectRogueAP_Type(Integer32):
    """Custom type dedicatedScanGrpDetectRogueAP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_DedicatedScanGrpDetectRogueAP_Type.__name__ = "Integer32"
_DedicatedScanGrpDetectRogueAP_Object = MibTableColumn
dedicatedScanGrpDetectRogueAP = _DedicatedScanGrpDetectRogueAP_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 20, 1, 10),
    _DedicatedScanGrpDetectRogueAP_Type()
)
dedicatedScanGrpDetectRogueAP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dedicatedScanGrpDetectRogueAP.setStatus("current")
_DedicatedScanGrpListeningPort_Type = Integer32
_DedicatedScanGrpListeningPort_Object = MibTableColumn
dedicatedScanGrpListeningPort = _DedicatedScanGrpListeningPort_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 20, 1, 11),
    _DedicatedScanGrpListeningPort_Type()
)
dedicatedScanGrpListeningPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dedicatedScanGrpListeningPort.setStatus("current")
_WidsWipsReport_ObjectIdentity = ObjectIdentity
widsWipsReport = _WidsWipsReport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 30)
)
_ActiveThreatTable_Object = MibTable
activeThreatTable = _ActiveThreatTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 30, 1)
)
if mibBuilder.loadTexts:
    activeThreatTable.setStatus("current")
_ActiveThreatEntry_Object = MibTableRow
activeThreatEntry = _ActiveThreatEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 30, 1, 1)
)
activeThreatEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-HWC-MIB", "activeThreatIndex"),
)
if mibBuilder.loadTexts:
    activeThreatEntry.setStatus("current")
_ActiveThreatIndex_Type = Unsigned32
_ActiveThreatIndex_Object = MibTableColumn
activeThreatIndex = _ActiveThreatIndex_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 30, 1, 1, 1),
    _ActiveThreatIndex_Type()
)
activeThreatIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    activeThreatIndex.setStatus("current")
_ActiveThreatCategory_Type = DisplayString
_ActiveThreatCategory_Object = MibTableColumn
activeThreatCategory = _ActiveThreatCategory_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 30, 1, 1, 2),
    _ActiveThreatCategory_Type()
)
activeThreatCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeThreatCategory.setStatus("current")
_ActiveThreatDeviceMAC_Type = MacAddress
_ActiveThreatDeviceMAC_Object = MibTableColumn
activeThreatDeviceMAC = _ActiveThreatDeviceMAC_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 30, 1, 1, 3),
    _ActiveThreatDeviceMAC_Type()
)
activeThreatDeviceMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeThreatDeviceMAC.setStatus("current")
_ActiveThreatDateTime_Type = DisplayString
_ActiveThreatDateTime_Object = MibTableColumn
activeThreatDateTime = _ActiveThreatDateTime_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 30, 1, 1, 4),
    _ActiveThreatDateTime_Type()
)
activeThreatDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeThreatDateTime.setStatus("current")


class _ActiveThreatCounterMeasure_Type(Integer32):
    """Custom type activeThreatCounterMeasure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("blacklisted", 8),
          ("noCounterMeasure", 0),
          ("preventRoaming", 4),
          ("preventUse", 2),
          ("rateLimit", 1))
    )


_ActiveThreatCounterMeasure_Type.__name__ = "Integer32"
_ActiveThreatCounterMeasure_Object = MibTableColumn
activeThreatCounterMeasure = _ActiveThreatCounterMeasure_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 30, 1, 1, 5),
    _ActiveThreatCounterMeasure_Type()
)
activeThreatCounterMeasure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeThreatCounterMeasure.setStatus("current")
_ActiveThreatAPName_Type = DisplayString
_ActiveThreatAPName_Object = MibTableColumn
activeThreatAPName = _ActiveThreatAPName_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 30, 1, 1, 6),
    _ActiveThreatAPName_Type()
)
activeThreatAPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeThreatAPName.setStatus("current")
_ActiveThreatRSS_Type = DisplayString
_ActiveThreatRSS_Object = MibTableColumn
activeThreatRSS = _ActiveThreatRSS_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 30, 1, 1, 7),
    _ActiveThreatRSS_Type()
)
activeThreatRSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeThreatRSS.setStatus("current")
_ActiveThreatExtraDetails_Type = DisplayString
_ActiveThreatExtraDetails_Object = MibTableColumn
activeThreatExtraDetails = _ActiveThreatExtraDetails_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 30, 1, 1, 8),
    _ActiveThreatExtraDetails_Type()
)
activeThreatExtraDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeThreatExtraDetails.setStatus("current")
_ActiveThreatThreat_Type = DisplayString
_ActiveThreatThreat_Object = MibTableColumn
activeThreatThreat = _ActiveThreatThreat_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 30, 1, 1, 9),
    _ActiveThreatThreat_Type()
)
activeThreatThreat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeThreatThreat.setStatus("current")
_CountermeasureAPTable_Object = MibTable
countermeasureAPTable = _CountermeasureAPTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 30, 2)
)
if mibBuilder.loadTexts:
    countermeasureAPTable.setStatus("current")
_CountermeasureAPEntry_Object = MibTableRow
countermeasureAPEntry = _CountermeasureAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 30, 2, 1)
)
countermeasureAPEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-HWC-MIB", "countermeasureAPSerial"),
    (0, "HIPATH-WIRELESS-HWC-MIB", "countermeasureAPThreatIndex"),
)
if mibBuilder.loadTexts:
    countermeasureAPEntry.setStatus("current")
_CountermeasureAPThreatIndex_Type = Unsigned32
_CountermeasureAPThreatIndex_Object = MibTableColumn
countermeasureAPThreatIndex = _CountermeasureAPThreatIndex_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 30, 2, 1, 1),
    _CountermeasureAPThreatIndex_Type()
)
countermeasureAPThreatIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    countermeasureAPThreatIndex.setStatus("current")
_CountermeasureAPSerial_Type = DisplayString
_CountermeasureAPSerial_Object = MibTableColumn
countermeasureAPSerial = _CountermeasureAPSerial_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 30, 2, 1, 2),
    _CountermeasureAPSerial_Type()
)
countermeasureAPSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    countermeasureAPSerial.setStatus("current")
_CountermeasureAPName_Type = DisplayString
_CountermeasureAPName_Object = MibTableColumn
countermeasureAPName = _CountermeasureAPName_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 30, 2, 1, 3),
    _CountermeasureAPName_Type()
)
countermeasureAPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    countermeasureAPName.setStatus("current")
_CountermeasureAPThreatCategory_Type = DisplayString
_CountermeasureAPThreatCategory_Object = MibTableColumn
countermeasureAPThreatCategory = _CountermeasureAPThreatCategory_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 30, 2, 1, 4),
    _CountermeasureAPThreatCategory_Type()
)
countermeasureAPThreatCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    countermeasureAPThreatCategory.setStatus("current")
_CountermeasureAPCountermeasure_Type = DisplayString
_CountermeasureAPCountermeasure_Object = MibTableColumn
countermeasureAPCountermeasure = _CountermeasureAPCountermeasure_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 30, 2, 1, 5),
    _CountermeasureAPCountermeasure_Type()
)
countermeasureAPCountermeasure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    countermeasureAPCountermeasure.setStatus("current")
_CountermeasureAPTime_Type = DisplayString
_CountermeasureAPTime_Object = MibTableColumn
countermeasureAPTime = _CountermeasureAPTime_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 30, 2, 1, 6),
    _CountermeasureAPTime_Type()
)
countermeasureAPTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    countermeasureAPTime.setStatus("current")
_BlacklistedClientTable_Object = MibTable
blacklistedClientTable = _BlacklistedClientTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 30, 3)
)
if mibBuilder.loadTexts:
    blacklistedClientTable.setStatus("current")
_BlacklistedClientEntry_Object = MibTableRow
blacklistedClientEntry = _BlacklistedClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 30, 3, 1)
)
blacklistedClientEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-HWC-MIB", "blacklistedClientMAC"),
)
if mibBuilder.loadTexts:
    blacklistedClientEntry.setStatus("current")
_BlacklistedClientMAC_Type = MacAddress
_BlacklistedClientMAC_Object = MibTableColumn
blacklistedClientMAC = _BlacklistedClientMAC_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 30, 3, 1, 1),
    _BlacklistedClientMAC_Type()
)
blacklistedClientMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blacklistedClientMAC.setStatus("current")
_BlacklistedClientStatTime_Type = DisplayString
_BlacklistedClientStatTime_Object = MibTableColumn
blacklistedClientStatTime = _BlacklistedClientStatTime_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 30, 3, 1, 2),
    _BlacklistedClientStatTime_Type()
)
blacklistedClientStatTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blacklistedClientStatTime.setStatus("current")
_BlacklistedClientEndTime_Type = DisplayString
_BlacklistedClientEndTime_Object = MibTableColumn
blacklistedClientEndTime = _BlacklistedClientEndTime_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 30, 3, 1, 3),
    _BlacklistedClientEndTime_Type()
)
blacklistedClientEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blacklistedClientEndTime.setStatus("current")
_BlacklistedClientReason_Type = DisplayString
_BlacklistedClientReason_Object = MibTableColumn
blacklistedClientReason = _BlacklistedClientReason_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 30, 3, 1, 4),
    _BlacklistedClientReason_Type()
)
blacklistedClientReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blacklistedClientReason.setStatus("current")
_ThreatSummaryTable_Object = MibTable
threatSummaryTable = _ThreatSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 30, 4)
)
if mibBuilder.loadTexts:
    threatSummaryTable.setStatus("current")
_ThreatSummaryEntry_Object = MibTableRow
threatSummaryEntry = _ThreatSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 30, 4, 1)
)
threatSummaryEntry.setIndexNames(
    (0, "HIPATH-WIRELESS-HWC-MIB", "threatSummaryIndex"),
)
if mibBuilder.loadTexts:
    threatSummaryEntry.setStatus("current")
_ThreatSummaryIndex_Type = Unsigned32
_ThreatSummaryIndex_Object = MibTableColumn
threatSummaryIndex = _ThreatSummaryIndex_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 30, 4, 1, 1),
    _ThreatSummaryIndex_Type()
)
threatSummaryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    threatSummaryIndex.setStatus("current")
_ThreatSummaryCategory_Type = DisplayString
_ThreatSummaryCategory_Object = MibTableColumn
threatSummaryCategory = _ThreatSummaryCategory_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 30, 4, 1, 2),
    _ThreatSummaryCategory_Type()
)
threatSummaryCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    threatSummaryCategory.setStatus("current")
_ThreatSummaryActiveThreat_Type = Unsigned32
_ThreatSummaryActiveThreat_Object = MibTableColumn
threatSummaryActiveThreat = _ThreatSummaryActiveThreat_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 30, 4, 1, 3),
    _ThreatSummaryActiveThreat_Type()
)
threatSummaryActiveThreat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    threatSummaryActiveThreat.setStatus("current")
_ThreatSummaryHistoricalCounts_Type = Unsigned32
_ThreatSummaryHistoricalCounts_Object = MibTableColumn
threatSummaryHistoricalCounts = _ThreatSummaryHistoricalCounts_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 11, 30, 4, 1, 4),
    _ThreatSummaryHistoricalCounts_Type()
)
threatSummaryHistoricalCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    threatSummaryHistoricalCounts.setStatus("current")
_ApNotifications_ObjectIdentity = ObjectIdentity
apNotifications = _ApNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 19)
)


class _ApEventId_Type(Integer32):
    """Custom type apEventId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("apPollTimeout", 1),
          ("apRegister", 2))
    )


_ApEventId_Type.__name__ = "Integer32"
_ApEventId_Object = MibScalar
apEventId = _ApEventId_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 19, 1),
    _ApEventId_Type()
)
apEventId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apEventId.setStatus("current")
_ApEventDescription_Type = OctetString
_ApEventDescription_Object = MibScalar
apEventDescription = _ApEventDescription_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 19, 2),
    _ApEventDescription_Type()
)
apEventDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEventDescription.setStatus("current")


class _ApEventAPSerialNumber_Type(OctetString):
    """Custom type apEventAPSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_ApEventAPSerialNumber_Type.__name__ = "OctetString"
_ApEventAPSerialNumber_Object = MibScalar
apEventAPSerialNumber = _ApEventAPSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 19, 3),
    _ApEventAPSerialNumber_Type()
)
apEventAPSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apEventAPSerialNumber.setStatus("current")
_StationSessionNotifications_ObjectIdentity = ObjectIdentity
stationSessionNotifications = _StationSessionNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 20)
)


class _StationEventType_Type(Integer32):
    """Custom type stationEventType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("areaChange", 12),
          ("authentication", 9),
          ("authenticationFailed", 10),
          ("authorizationChanged", 8),
          ("deRegistration", 1),
          ("locationUpdate", 11),
          ("mbaAccepted", 6),
          ("mbaRejected", 7),
          ("mbaTimeout", 5),
          ("registration", 0),
          ("registrationFailed", 3),
          ("roam", 4),
          ("stateChange", 2))
    )


_StationEventType_Type.__name__ = "Integer32"
_StationEventType_Object = MibScalar
stationEventType = _StationEventType_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 20, 1),
    _StationEventType_Type()
)
stationEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stationEventType.setStatus("current")
_StationMacAddress_Type = MacAddress
_StationMacAddress_Object = MibScalar
stationMacAddress = _StationMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 20, 2),
    _StationMacAddress_Type()
)
stationMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stationMacAddress.setStatus("current")
_StationIPAddress_Type = IpAddress
_StationIPAddress_Object = MibScalar
stationIPAddress = _StationIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 20, 3),
    _StationIPAddress_Type()
)
stationIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stationIPAddress.setStatus("current")
_StationAPName_Type = DisplayString
_StationAPName_Object = MibScalar
stationAPName = _StationAPName_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 20, 4),
    _StationAPName_Type()
)
stationAPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stationAPName.setStatus("current")
_StationAPSSID_Type = DisplayString
_StationAPSSID_Object = MibScalar
stationAPSSID = _StationAPSSID_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 20, 5),
    _StationAPSSID_Type()
)
stationAPSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stationAPSSID.setStatus("current")
_StationDetailEvent_Type = DisplayString
_StationDetailEvent_Object = MibScalar
stationDetailEvent = _StationDetailEvent_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 20, 6),
    _StationDetailEvent_Type()
)
stationDetailEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stationDetailEvent.setStatus("current")
_StationRoamedAPName_Type = DisplayString
_StationRoamedAPName_Object = MibScalar
stationRoamedAPName = _StationRoamedAPName_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 20, 7),
    _StationRoamedAPName_Type()
)
stationRoamedAPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stationRoamedAPName.setStatus("current")
_StationName_Type = DisplayString
_StationName_Object = MibScalar
stationName = _StationName_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 20, 8),
    _StationName_Type()
)
stationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stationName.setStatus("current")
_StationBSSID_Type = DisplayString
_StationBSSID_Object = MibScalar
stationBSSID = _StationBSSID_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 20, 9),
    _StationBSSID_Type()
)
stationBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stationBSSID.setStatus("current")
_StationEventTimeStamp_Type = TimeTicks
_StationEventTimeStamp_Object = MibScalar
stationEventTimeStamp = _StationEventTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 20, 10),
    _StationEventTimeStamp_Type()
)
stationEventTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stationEventTimeStamp.setStatus("current")
_StationIPv6Address1_Type = Ipv6Address
_StationIPv6Address1_Object = MibScalar
stationIPv6Address1 = _StationIPv6Address1_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 20, 12),
    _StationIPv6Address1_Type()
)
stationIPv6Address1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stationIPv6Address1.setStatus("current")
_StationIPv6Address2_Type = Ipv6Address
_StationIPv6Address2_Object = MibScalar
stationIPv6Address2 = _StationIPv6Address2_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 20, 13),
    _StationIPv6Address2_Type()
)
stationIPv6Address2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stationIPv6Address2.setStatus("current")
_StationIPv6Address3_Type = Ipv6Address
_StationIPv6Address3_Object = MibScalar
stationIPv6Address3 = _StationIPv6Address3_Object(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 20, 14),
    _StationIPv6Address3_Type()
)
stationIPv6Address3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stationIPv6Address3.setStatus("current")
_HiPathWirelessHWCConformance_ObjectIdentity = ObjectIdentity
hiPathWirelessHWCConformance = _HiPathWirelessHWCConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 30)
)
_WirelessEWCGroups_ObjectIdentity = ObjectIdentity
wirelessEWCGroups = _WirelessEWCGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 30, 5)
)

# Managed Objects groups

hiPathWirelessHWCGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 30, 2)
)
hiPathWirelessHWCGroup.setObjects(
      *(("HIPATH-WIRELESS-HWC-MIB", "sysSoftwareVersion"),
        ("HIPATH-WIRELESS-HWC-MIB", "sysCPUType"),
        ("HIPATH-WIRELESS-HWC-MIB", "sysLogLevel"),
        ("HIPATH-WIRELESS-HWC-MIB", "logEventSeverityThreshold"),
        ("HIPATH-WIRELESS-HWC-MIB", "logEventSeverity"),
        ("HIPATH-WIRELESS-HWC-MIB", "logEventComponent"),
        ("HIPATH-WIRELESS-HWC-MIB", "apLogCollectionEnable"),
        ("HIPATH-WIRELESS-HWC-MIB", "apLogFrequency"),
        ("HIPATH-WIRELESS-HWC-MIB", "apLogDestination"),
        ("HIPATH-WIRELESS-HWC-MIB", "apLogUserId"),
        ("HIPATH-WIRELESS-HWC-MIB", "apLogServerIP"),
        ("HIPATH-WIRELESS-HWC-MIB", "apLogDirectory"),
        ("HIPATH-WIRELESS-HWC-MIB", "apLogPassword"),
        ("HIPATH-WIRELESS-HWC-MIB", "apLogFTProtocol"),
        ("HIPATH-WIRELESS-HWC-MIB", "select"),
        ("HIPATH-WIRELESS-HWC-MIB", "apLogQuickSelectedOption"),
        ("HIPATH-WIRELESS-HWC-MIB", "apLogFileCopyDestination"),
        ("HIPATH-WIRELESS-HWC-MIB", "apLogFileCopyProtocol"),
        ("HIPATH-WIRELESS-HWC-MIB", "apLogFileCopyServerIP"),
        ("HIPATH-WIRELESS-HWC-MIB", "apLogFileCopyUserID"),
        ("HIPATH-WIRELESS-HWC-MIB", "apLogFileCopyPassword"),
        ("HIPATH-WIRELESS-HWC-MIB", "apLogFileCopyServerDirectory"),
        ("HIPATH-WIRELESS-HWC-MIB", "apLogFileCopyOperation"),
        ("HIPATH-WIRELESS-HWC-MIB", "apLogFileCopyOperationStatus"),
        ("HIPATH-WIRELESS-HWC-MIB", "apLogFileCopyRowStatus"),
        ("HIPATH-WIRELESS-HWC-MIB", "apLogFileUtilityLimit"),
        ("HIPATH-WIRELESS-HWC-MIB", "apLogFileUtilityCurrent"),
        ("HIPATH-WIRELESS-HWC-MIB", "logEventDescription"),
        ("HIPATH-WIRELESS-HWC-MIB", "apEventId"),
        ("HIPATH-WIRELESS-HWC-MIB", "apEventDescription"),
        ("HIPATH-WIRELESS-HWC-MIB", "apEventAPSerialNumber"),
        ("HIPATH-WIRELESS-HWC-MIB", "assocTxPackets"),
        ("HIPATH-WIRELESS-HWC-MIB", "assocRxPackets"),
        ("HIPATH-WIRELESS-HWC-MIB", "assocTxOctets"),
        ("HIPATH-WIRELESS-HWC-MIB", "assocRxOctets"),
        ("HIPATH-WIRELESS-HWC-MIB", "assocDuration"),
        ("HIPATH-WIRELESS-HWC-MIB", "assocCount"),
        ("HIPATH-WIRELESS-HWC-MIB", "assocMUMacAddress"),
        ("HIPATH-WIRELESS-HWC-MIB", "assocStartSysUpTime"),
        ("HIPATH-WIRELESS-HWC-MIB", "mobileUnitCount"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsIfIndex"),
        ("HIPATH-WIRELESS-HWC-MIB", "radioVNSRowStatus"),
        ("HIPATH-WIRELESS-HWC-MIB", "radioIfIndex"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsFilterRulePortLow"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsFilterRulePortHigh"),
        ("HIPATH-WIRELESS-HWC-MIB", "cpURL"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsDHCPRangeIndex"),
        ("HIPATH-WIRELESS-HWC-MIB", "vns3rdPartyAP"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsUseDHCPRelay"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsMgmtTrafficEnable"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsAuthModel"),
        ("HIPATH-WIRELESS-HWC-MIB", "physicalPortCount"),
        ("HIPATH-WIRELESS-HWC-MIB", "mgmtPortIfIndex"),
        ("HIPATH-WIRELESS-HWC-MIB", "mgmtPortHostname"),
        ("HIPATH-WIRELESS-HWC-MIB", "mgmtPortDomain"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnRole"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnIfIndex"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnHeartbeatInterval"),
        ("HIPATH-WIRELESS-HWC-MIB", "ntpEnabled"),
        ("HIPATH-WIRELESS-HWC-MIB", "ntpTimezone"),
        ("HIPATH-WIRELESS-HWC-MIB", "ntpTimeServer1"),
        ("HIPATH-WIRELESS-HWC-MIB", "ntpTimeServer2"),
        ("HIPATH-WIRELESS-HWC-MIB", "ntpTimeServer3"),
        ("HIPATH-WIRELESS-HWC-MIB", "tunnelCount"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsCount"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsDescription"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsMUSessionTimeout"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsAllowMulticast"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsSSID"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsDomain"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsDNSServers"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsWINSServers"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsStatus"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsDHCPRangeStart"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsDHCPRangeEnd"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsDHCPRangeType"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsDHCPRangeStatus"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsRadiusServerPort"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsRadiusServerRetries"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsRadiusServerTimeout"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsRadiusServerSharedSecret"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsRadiusServerNASIdentifier"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsRadiusServerAuthType"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsRadiusServerRowStatus"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsFilterID"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsFilterIDStatus"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsFilterRuleOrder"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsFilterRuleDirection"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsFilterRuleAction"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsFilterRuleIPAddress"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsFilterRuleProtocol"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsFilterRuleEtherType"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsFilterRuleStatus"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsPrivWEPKeyType"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsPrivDynamicRekeyFrequency"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsPrivWEPKeyLength"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsPrivWPA1Enabled"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsPrivUseSharedKey"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsPrivWPASharedKey"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsWEPKeyIndex"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsWEPKeyValue"),
        ("HIPATH-WIRELESS-HWC-MIB", "activeVNSSessionCount"),
        ("HIPATH-WIRELESS-HWC-MIB", "apCount"),
        ("HIPATH-WIRELESS-HWC-MIB", "cpReplaceGatewayWithFQDN"),
        ("HIPATH-WIRELESS-HWC-MIB", "cpDefaultRedirectionURL"),
        ("HIPATH-WIRELESS-HWC-MIB", "cpConnectionIP"),
        ("HIPATH-WIRELESS-HWC-MIB", "cpConnectionPort"),
        ("HIPATH-WIRELESS-HWC-MIB", "cpSharedSecret"),
        ("HIPATH-WIRELESS-HWC-MIB", "cpLogOff"),
        ("HIPATH-WIRELESS-HWC-MIB", "cpStatusCheck"),
        ("HIPATH-WIRELESS-HWC-MIB", "cpType"),
        ("HIPATH-WIRELESS-HWC-MIB", "apMacAddress"),
        ("HIPATH-WIRELESS-HWC-MIB", "serviceLogFacility"),
        ("HIPATH-WIRELESS-HWC-MIB", "sysLogServerIP"),
        ("HIPATH-WIRELESS-HWC-MIB", "sysLogServerPort"),
        ("HIPATH-WIRELESS-HWC-MIB", "sysLogServerRowStatus"),
        ("HIPATH-WIRELESS-HWC-MIB", "sysLogServerIndex"),
        ("HIPATH-WIRELESS-HWC-MIB", "apActiveCount"),
        ("HIPATH-WIRELESS-HWC-MIB", "sysLogServerEnabled"),
        ("HIPATH-WIRELESS-HWC-MIB", "assocVnsIfIndex"),
        ("HIPATH-WIRELESS-HWC-MIB", "apRadioFrequency"),
        ("HIPATH-WIRELESS-HWC-MIB", "includeAllServiceMessages"),
        ("HIPATH-WIRELESS-HWC-MIB", "tunnelStartIP"),
        ("HIPATH-WIRELESS-HWC-MIB", "tunnelStartHWC"),
        ("HIPATH-WIRELESS-HWC-MIB", "tunnelEndIP"),
        ("HIPATH-WIRELESS-HWC-MIB", "tunnelEndHWC"),
        ("HIPATH-WIRELESS-HWC-MIB", "apBroadcastDisassociate"),
        ("HIPATH-WIRELESS-HWC-MIB", "sysSerialNo"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsPrivWPA2Enabled"),
        ("HIPATH-WIRELESS-HWC-MIB", "tunnelStatus"),
        ("HIPATH-WIRELESS-HWC-MIB", "hiPathWirelessAppLogFacility"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsVlanID"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsMgmIpAddress"),
        ("HIPATH-WIRELESS-HWC-MIB", "maxVoiceBWforReassociation"),
        ("HIPATH-WIRELESS-HWC-MIB", "maxVoiceBWforAssociation"),
        ("HIPATH-WIRELESS-HWC-MIB", "maxVideoBWforReassociation"),
        ("HIPATH-WIRELESS-HWC-MIB", "maxVideoBWforAssociation"),
        ("HIPATH-WIRELESS-HWC-MIB", "maxBestEffortBWforReassociation"),
        ("HIPATH-WIRELESS-HWC-MIB", "maxBestEffortBWforAssociation"),
        ("HIPATH-WIRELESS-HWC-MIB", "maxBackgroundBWforReassociation"),
        ("HIPATH-WIRELESS-HWC-MIB", "maxBackgroundBWforAssociation"),
        ("HIPATH-WIRELESS-HWC-MIB", "physicalPortsInternalVlanID"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsMode"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsQoSPriorityOverrideFlag"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsQoSPriorityOverrideSC"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsQoSPriorityOverrideDSCP"),
        ("HIPATH-WIRELESS-HWC-MIB", "netflowDestinationIP"),
        ("HIPATH-WIRELESS-HWC-MIB", "netflowInterval"),
        ("HIPATH-WIRELESS-HWC-MIB", "mirrorFirstN"),
        ("HIPATH-WIRELESS-HWC-MIB", "mirrorL2Ports"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsQoSClassificationServiceClass"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsQoSWirelessLegacyFlag"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsQoSWirelessWMMFlag"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsQoSWireless80211eFlag"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsQoSWirelessTurboVoiceFlag"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsQoSWirelessEnableUAPSD"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsQoSWirelessUseAdmControlVoice"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsSuppressSSID"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsEnable11hSupport"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsApplyPowerBackOff"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsProcessClientIEReq"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsQoSWirelessUseAdmControlVideo"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsInterfaceName"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsQoSWirelessULPolicerAction"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsQoSWirelessDLPolicerAction"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsQoSWirelessUseAdmControlBestEffort"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsQoSWirelessUseAdmControlBackground"),
        ("HIPATH-WIRELESS-HWC-MIB", "tspecMuMACAddress"),
        ("HIPATH-WIRELESS-HWC-MIB", "tspecAC"),
        ("HIPATH-WIRELESS-HWC-MIB", "tspecDirection"),
        ("HIPATH-WIRELESS-HWC-MIB", "tspecApSerialNumber"),
        ("HIPATH-WIRELESS-HWC-MIB", "tspecMuIPAddress"),
        ("HIPATH-WIRELESS-HWC-MIB", "tspecBssMac"),
        ("HIPATH-WIRELESS-HWC-MIB", "tspecSsid"),
        ("HIPATH-WIRELESS-HWC-MIB", "tspecMDR"),
        ("HIPATH-WIRELESS-HWC-MIB", "tspecNMS"),
        ("HIPATH-WIRELESS-HWC-MIB", "tspecSBA"),
        ("HIPATH-WIRELESS-HWC-MIB", "tspecDlRate"),
        ("HIPATH-WIRELESS-HWC-MIB", "tspecUlRate"),
        ("HIPATH-WIRELESS-HWC-MIB", "tspecDlViolations"),
        ("HIPATH-WIRELESS-HWC-MIB", "tspecUlViolations"),
        ("HIPATH-WIRELESS-HWC-MIB", "tspecProtocol"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsDLSSupportEnable"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsDLSAddress"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsDLSPort"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsSessionAvailabilityEnable"),
        ("HIPATH-WIRELESS-HWC-MIB", "ntpServerEnabled"),
        ("HIPATH-WIRELESS-HWC-MIB", "primaryDNS"),
        ("HIPATH-WIRELESS-HWC-MIB", "secondaryDNS"),
        ("HIPATH-WIRELESS-HWC-MIB", "tertiaryDNS"),
        ("HIPATH-WIRELESS-HWC-MIB", "physicalFlash"),
        ("HIPATH-WIRELESS-HWC-MIB", "jumboFrames"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsRadiusServerName"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsRadiusServerNasAddress"),
        ("HIPATH-WIRELESS-HWC-MIB", "dasReplayInterval"),
        ("HIPATH-WIRELESS-HWC-MIB", "dasPort"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsEnabled"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsAPFilterRuleOrder"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsAPFilterRuleDirection"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsAPFilterAction"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsAPFilterIPAddress"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsAPFilterMask"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsAPFilterPortLow"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsAPFilterPortHigh"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsAPFilterProtocol"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsAPFilterEtherType"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsAPFilterRowStatus"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsStrictSubnetAdherence"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsSLPEnabled"),
        ("HIPATH-WIRELESS-HWC-MIB", "imagePath36xx"),
        ("HIPATH-WIRELESS-HWC-MIB", "imagePath26xx"),
        ("HIPATH-WIRELESS-HWC-MIB", "tftpSever"),
        ("HIPATH-WIRELESS-HWC-MIB", "imageVersionOfap26xx"),
        ("HIPATH-WIRELESS-HWC-MIB", "imageVersionOfngap36xx"),
        ("HIPATH-WIRELESS-HWC-MIB", "topoExceptionFiterName"),
        ("HIPATH-WIRELESS-HWC-MIB", "topoExceptionStatPktsDenied"),
        ("HIPATH-WIRELESS-HWC-MIB", "topoExceptionStatPktsAllowed"),
        ("HIPATH-WIRELESS-HWC-MIB", "synchronizeSystemConfig"),
        ("HIPATH-WIRELESS-HWC-MIB", "availabilityStatus"),
        ("HIPATH-WIRELESS-HWC-MIB", "pairIPAddress"),
        ("HIPATH-WIRELESS-HWC-MIB", "hwcAvailabilityRank"),
        ("HIPATH-WIRELESS-HWC-MIB", "fastFailover"),
        ("HIPATH-WIRELESS-HWC-MIB", "synchronizeGuestPort"),
        ("HIPATH-WIRELESS-HWC-MIB", "tunnelStatsTxBytes"),
        ("HIPATH-WIRELESS-HWC-MIB", "apRegistrationRequests"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnForeignClients"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnLocalClients"),
        ("HIPATH-WIRELESS-HWC-MIB", "apStatsSessionDuration"),
        ("HIPATH-WIRELESS-HWC-MIB", "detectLinkFailure"),
        ("HIPATH-WIRELESS-HWC-MIB", "apRegUseClusterEncryption"),
        ("HIPATH-WIRELESS-HWC-MIB", "apRegClusterSharedSecret"),
        ("HIPATH-WIRELESS-HWC-MIB", "apRegDiscoveryRetries"),
        ("HIPATH-WIRELESS-HWC-MIB", "apRegDiscoveryInterval"),
        ("HIPATH-WIRELESS-HWC-MIB", "apRegTelnetPassword"),
        ("HIPATH-WIRELESS-HWC-MIB", "apRegSSHPassword"),
        ("HIPATH-WIRELESS-HWC-MIB", "apRegSecurityMode"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnTotalClients"),
        ("HIPATH-WIRELESS-HWC-MIB", "tunnelStatsRxBytes"),
        ("HIPATH-WIRELESS-HWC-MIB", "tunnelStatsTxRxBytes"),
        ("HIPATH-WIRELESS-HWC-MIB", "tunnelsTxRxBytes"),
        ("HIPATH-WIRELESS-HWC-MIB", "clearAccessRejectMsg"),
        ("HIPATH-WIRELESS-HWC-MIB", "armCount"),
        ("HIPATH-WIRELESS-HWC-MIB", "armReplyMessage"),
        ("HIPATH-WIRELESS-HWC-MIB", "apLinkTimeout"),
        ("HIPATH-WIRELESS-HWC-MIB", "apFastFailoverEnable"),
        ("HIPATH-WIRELESS-HWC-MIB", "topoStatFrameTooLongErrors"),
        ("HIPATH-WIRELESS-HWC-MIB", "topoStatFrameChkSeqErrors"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsConfigWLANID"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanVNSID"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanPrivPrivacyType"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanPrivWEPKeyIndex"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanPrivWEPKeyLength"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanPrivWEPKey"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanPrivWPAv1EncryptionType"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanPrivWPAv2EncryptionType"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanPrivKeyManagement"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanPrivBroadcastRekeying"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanPrivRekeyInterval"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanPrivGroupKPSR"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanPrivWPAPSK"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanPrivWPAversion"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanPrivfastTransition"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanPrivManagementFrameProtection"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanAuthType"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanAuthMacBasedAuth"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanAuthMACBasedAuthOnRoam"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanAuthAutoAuthAuthorizedUser"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanAuthAllowUnauthorizedUser"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanAuthRadiusIncludeAP"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanAuthRadiusIncludeVNS"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanAuthRadiusIncludeSSID"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanAuthRadiusIncludePolicy"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanAuthRadiusIncludeTopology"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanAuthRadiusIncludeIngressRC"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanAuthRadiusIncludeEgressRC"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanAuthCollectAcctInformation"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanAuthReplaceCalledStationIDWithZone"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanAuthRadiusAcctAfterMacBaseAuthorization"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanAuthRadiusTimeoutRole"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanAuthRadiusOperatorNameSpace"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanAuthRadiusOperatorName"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanAuthMACBasedAuthReAuthOnAreaRoam"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanRadiusName"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanRadiusUsage"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanRadiusPriority"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanRadiusPort"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanRadiusRetries"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanRadiusTimeout"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanRadiusNASUseVnsIP"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanRadiusNASIP"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanRadiusNASIDUseVNSName"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanRadiusNASID"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanRadiusAuthType"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanCPAuthType"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanCP802HttpRedirect"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanCPExtConnection"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanCPExtPort"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanCPExtEnableHttps"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanCPExtSharedSecret"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanCPExtTosOverride"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanCPExtTosValue"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanCPGuestAccLifetime"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanCPGuestSessionLifetime"),
        ("HIPATH-WIRELESS-HWC-MIB", "loadGrpRadiosRadio1"),
        ("HIPATH-WIRELESS-HWC-MIB", "loadGrpRadiosRadio2"),
        ("HIPATH-WIRELESS-HWC-MIB", "loadGrpWlanAssigned"),
        ("HIPATH-WIRELESS-HWC-MIB", "schedule"),
        ("HIPATH-WIRELESS-HWC-MIB", "startHour"),
        ("HIPATH-WIRELESS-HWC-MIB", "startMinute"),
        ("HIPATH-WIRELESS-HWC-MIB", "duration"),
        ("HIPATH-WIRELESS-HWC-MIB", "recurrenceDaily"),
        ("HIPATH-WIRELESS-HWC-MIB", "recurrenceWeekly"),
        ("HIPATH-WIRELESS-HWC-MIB", "recurrenceMonthly"),
        ("HIPATH-WIRELESS-HWC-MIB", "apPlatforms"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanCPIntLogoffButton"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanCPIntStatusCheckButton"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanCPRedirectURL"),
        ("HIPATH-WIRELESS-HWC-MIB", "apRadioProtocol"),
        ("HIPATH-WIRELESS-HWC-MIB", "apRadioNumber"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanCPReplaceIPwithFQDN"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanCPSendLoginTo"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanCPGuestAllowedLifetimeAcct"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanCPGuestIDPrefix"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanCPGuestMinPassLength"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanCPGuestMaxConcurrentSession"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanCPExtAddIPtoURL"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanCPUseHTTPSforConnection"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanCPIdentity"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanCPCustomSpecificURL"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanCPSelectionOption"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanCPExtEncryption"),
        ("HIPATH-WIRELESS-HWC-MIB", "radiusStrictMode"),
        ("HIPATH-WIRELESS-HWC-MIB", "advancedFilteringMode"),
        ("HIPATH-WIRELESS-HWC-MIB", "weakCipherEnable"),
        ("HIPATH-WIRELESS-HWC-MIB", "stationEventType"),
        ("HIPATH-WIRELESS-HWC-MIB", "stationMacAddress"),
        ("HIPATH-WIRELESS-HWC-MIB", "stationIPAddress"),
        ("HIPATH-WIRELESS-HWC-MIB", "stationAPName"),
        ("HIPATH-WIRELESS-HWC-MIB", "stationAPSSID"),
        ("HIPATH-WIRELESS-HWC-MIB", "stationDetailEvent"),
        ("HIPATH-WIRELESS-HWC-MIB", "stationRoamedAPName"),
        ("HIPATH-WIRELESS-HWC-MIB", "stationName"),
        ("HIPATH-WIRELESS-HWC-MIB", "stationBSSID"),
        ("HIPATH-WIRELESS-HWC-MIB", "stationEventTimeStamp"),
        ("HIPATH-WIRELESS-HWC-MIB", "stationIPv6Address1"),
        ("HIPATH-WIRELESS-HWC-MIB", "stationIPv6Address2"),
        ("HIPATH-WIRELESS-HWC-MIB", "stationIPv6Address3"),
        ("HIPATH-WIRELESS-HWC-MIB", "clientAutologinOption"),
        ("HIPATH-WIRELESS-HWC-MIB", "radiusMacAddressFormatOption"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanRadiusServerName"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanRadiusServerUse"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanRadiusServerUsage"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanRadiusServerAuthNASIP"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanRadiusServerAuthNASId"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanRadiusServerAuthAuthType"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanRadiusServerAcctNASIP"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanRadiusServerAcctNASId"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanRadiusServerAcctSIAR"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanRadiusServerMacNASIP"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanRadiusServerMacNASId"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanRadiusServerMacAuthType"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanRadiusServerMacPW"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanRadiusServerAuthUseVNSIPAddr"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanRadiusServerAuthUseVNSName"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanRadiusServerAcctUseVNSIPAddr"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanRadiusServerAcctUseVNSName"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanRadiusServerMacUseVNSIPAddr"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanRadiusServerMacUseVNSName"))
)
if mibBuilder.loadTexts:
    hiPathWirelessHWCGroup.setStatus("current")

hiPathWirelessHWCObsolete = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 30, 4)
)
hiPathWirelessHWCObsolete.setObjects(
      *(("HIPATH-WIRELESS-HWC-MIB", "vnsWDSRFAPName"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsWDSRFbgService"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsWDSRFaService"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsWDSRFPreferredParent"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsWDSRFBackupParent"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsWDSRFBridge"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsRateControlProfInd"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsRateControlProfName"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsRateControlCIR"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsRateControlCBS"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsExceptionFiterName"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsExceptionStatPktsDenied"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsExceptionStatPktsAllowed"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsWDSStatAPName"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsWDSStatAPRole"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsWDSStatAPRadio"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsWDSStatAPParent"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsWDSStatSSID"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsWDSStatRxFrame"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsWDSStatTxFrame"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsWDSStatRxError"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsWDSStatTxError"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsWDSStatRxRSSI"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsWDSStatRxRate"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsAssignmentMode"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsParentIfIndex"),
        ("HIPATH-WIRELESS-HWC-MIB", "externalRadiusServerName"),
        ("HIPATH-WIRELESS-HWC-MIB", "externalRadiusServerAddress"),
        ("HIPATH-WIRELESS-HWC-MIB", "externalRadiusServerSharedSecret"),
        ("HIPATH-WIRELESS-HWC-MIB", "externalRadiusServerRowStatus"),
        ("HIPATH-WIRELESS-HWC-MIB", "cpLoginLabel"),
        ("HIPATH-WIRELESS-HWC-MIB", "cpPasswordLabel"),
        ("HIPATH-WIRELESS-HWC-MIB", "cpHeaderURL"),
        ("HIPATH-WIRELESS-HWC-MIB", "cpFooterURL"),
        ("HIPATH-WIRELESS-HWC-MIB", "cpMessage"),
        ("HIPATH-WIRELESS-HWC-MIB", "cpURL"),
        ("HIPATH-WIRELESS-HWC-MIB", "loadGroupLoadControl"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsWDSStatTxRate"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsRateControlProfile"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsStatName"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsStatTxPkts"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsStatRxPkts"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsStatTxOctects"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsStatRxOctects"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsStatMulticastTxPkts"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsStatMulticastRxPkts"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsStatBroadcastTxPkts"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsStatBroadcastRxPkts"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsStatRadiusTotRequests"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsStatRadiusReqFailed"),
        ("HIPATH-WIRELESS-HWC-MIB", "vnsStatRadiusReqRejected"))
)
if mibBuilder.loadTexts:
    hiPathWirelessHWCObsolete.setStatus("obsolete")

physicalPortsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 30, 5, 1)
)
physicalPortsGroup.setObjects(
      *(("HIPATH-WIRELESS-HWC-MIB", "portMgmtTrafficEnable"),
        ("HIPATH-WIRELESS-HWC-MIB", "portDuplexMode"),
        ("HIPATH-WIRELESS-HWC-MIB", "portFunction"),
        ("HIPATH-WIRELESS-HWC-MIB", "portName"),
        ("HIPATH-WIRELESS-HWC-MIB", "portIpAddress"),
        ("HIPATH-WIRELESS-HWC-MIB", "portMask"),
        ("HIPATH-WIRELESS-HWC-MIB", "portVlanID"),
        ("HIPATH-WIRELESS-HWC-MIB", "portDHCPEnable"),
        ("HIPATH-WIRELESS-HWC-MIB", "portDHCPGateway"),
        ("HIPATH-WIRELESS-HWC-MIB", "portDHCPDomain"),
        ("HIPATH-WIRELESS-HWC-MIB", "portDHCPDefaultLease"),
        ("HIPATH-WIRELESS-HWC-MIB", "portDHCPMaxLease"),
        ("HIPATH-WIRELESS-HWC-MIB", "portDHCPDnsServers"),
        ("HIPATH-WIRELESS-HWC-MIB", "portDHCPWins"),
        ("HIPATH-WIRELESS-HWC-MIB", "portEnabled"),
        ("HIPATH-WIRELESS-HWC-MIB", "portMacAddress"))
)
if mibBuilder.loadTexts:
    physicalPortsGroup.setStatus("deprecated")

phyDHCPRangeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 30, 5, 2)
)
phyDHCPRangeGroup.setObjects(
      *(("HIPATH-WIRELESS-HWC-MIB", "phyDHCPRangeIndex"),
        ("HIPATH-WIRELESS-HWC-MIB", "phyDHCPRangeStart"),
        ("HIPATH-WIRELESS-HWC-MIB", "phyDHCPRangeEnd"),
        ("HIPATH-WIRELESS-HWC-MIB", "phyDHCPRangeType"),
        ("HIPATH-WIRELESS-HWC-MIB", "phyDHCPRangeStatus"))
)
if mibBuilder.loadTexts:
    phyDHCPRangeGroup.setStatus("deprecated")

layerTwoPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 30, 5, 3)
)
layerTwoPortGroup.setObjects(
      *(("HIPATH-WIRELESS-HWC-MIB", "layerTwoPortName"),
        ("HIPATH-WIRELESS-HWC-MIB", "layerTwoPortMacAddress"),
        ("HIPATH-WIRELESS-HWC-MIB", "layerTwoPortMgmtState"))
)
if mibBuilder.loadTexts:
    layerTwoPortGroup.setStatus("current")

muGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 30, 5, 4)
)
muGroup.setObjects(
      *(("HIPATH-WIRELESS-HWC-MIB", "muMACAddress"),
        ("HIPATH-WIRELESS-HWC-MIB", "muIPAddress"),
        ("HIPATH-WIRELESS-HWC-MIB", "muUser"),
        ("HIPATH-WIRELESS-HWC-MIB", "muState"),
        ("HIPATH-WIRELESS-HWC-MIB", "muAPSerialNo"),
        ("HIPATH-WIRELESS-HWC-MIB", "muVnsSSID"),
        ("HIPATH-WIRELESS-HWC-MIB", "muTxPackets"),
        ("HIPATH-WIRELESS-HWC-MIB", "muRxPackets"),
        ("HIPATH-WIRELESS-HWC-MIB", "muTxOctets"),
        ("HIPATH-WIRELESS-HWC-MIB", "muRxOctets"),
        ("HIPATH-WIRELESS-HWC-MIB", "muDuration"),
        ("HIPATH-WIRELESS-HWC-MIB", "muAPName"),
        ("HIPATH-WIRELESS-HWC-MIB", "muWLANID"),
        ("HIPATH-WIRELESS-HWC-MIB", "muConnectionProtocol"),
        ("HIPATH-WIRELESS-HWC-MIB", "muTopologyName"),
        ("HIPATH-WIRELESS-HWC-MIB", "muPolicyName"),
        ("HIPATH-WIRELESS-HWC-MIB", "muDefaultCoS"),
        ("HIPATH-WIRELESS-HWC-MIB", "muConnectionCapability"),
        ("HIPATH-WIRELESS-HWC-MIB", "muBSSIDMac"),
        ("HIPATH-WIRELESS-HWC-MIB", "muDot11ConnectionCapability"))
)
if mibBuilder.loadTexts:
    muGroup.setStatus("current")

apStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 30, 5, 5)
)
apStatsGroup.setObjects(
      *(("HIPATH-WIRELESS-HWC-MIB", "apInUcastPkts"),
        ("HIPATH-WIRELESS-HWC-MIB", "apInNUcastPkts"),
        ("HIPATH-WIRELESS-HWC-MIB", "apInOctets"),
        ("HIPATH-WIRELESS-HWC-MIB", "apInErrors"),
        ("HIPATH-WIRELESS-HWC-MIB", "apInDiscards"),
        ("HIPATH-WIRELESS-HWC-MIB", "apOutUcastPkts"),
        ("HIPATH-WIRELESS-HWC-MIB", "apOutNUcastPkts"),
        ("HIPATH-WIRELESS-HWC-MIB", "apOutOctets"),
        ("HIPATH-WIRELESS-HWC-MIB", "apOutErrors"),
        ("HIPATH-WIRELESS-HWC-MIB", "apOutDiscards"),
        ("HIPATH-WIRELESS-HWC-MIB", "apUpTime"),
        ("HIPATH-WIRELESS-HWC-MIB", "apCredentialType"),
        ("HIPATH-WIRELESS-HWC-MIB", "apCertificateExpiry"),
        ("HIPATH-WIRELESS-HWC-MIB", "apStatsMuCounts"),
        ("HIPATH-WIRELESS-HWC-MIB", "apStatsSessionDuration"),
        ("HIPATH-WIRELESS-HWC-MIB", "apTotalStationsA"),
        ("HIPATH-WIRELESS-HWC-MIB", "apTotalStationsB"),
        ("HIPATH-WIRELESS-HWC-MIB", "apTotalStationsG"),
        ("HIPATH-WIRELESS-HWC-MIB", "apTotalStationsN50"),
        ("HIPATH-WIRELESS-HWC-MIB", "apTotalStationsN24"),
        ("HIPATH-WIRELESS-HWC-MIB", "apInvalidPolicyCount"),
        ("HIPATH-WIRELESS-HWC-MIB", "apInterfaceMTU"),
        ("HIPATH-WIRELESS-HWC-MIB", "apEffectiveTunnelMTU"),
        ("HIPATH-WIRELESS-HWC-MIB", "apTotalStationsAC"),
        ("HIPATH-WIRELESS-HWC-MIB", "apTotalStationsAInOctets"),
        ("HIPATH-WIRELESS-HWC-MIB", "apTotalStationsAOutOctets"),
        ("HIPATH-WIRELESS-HWC-MIB", "apTotalStationsBInOctets"),
        ("HIPATH-WIRELESS-HWC-MIB", "apTotalStationsBOutOctets"),
        ("HIPATH-WIRELESS-HWC-MIB", "apTotalStationsGInOctets"),
        ("HIPATH-WIRELESS-HWC-MIB", "apTotalStationsGOutOctets"),
        ("HIPATH-WIRELESS-HWC-MIB", "apTotalStationsN50InOctets"),
        ("HIPATH-WIRELESS-HWC-MIB", "apTotalStationsN50OutOctets"),
        ("HIPATH-WIRELESS-HWC-MIB", "apTotalStationsN24InOctets"),
        ("HIPATH-WIRELESS-HWC-MIB", "apTotalStationsN24OutOctets"),
        ("HIPATH-WIRELESS-HWC-MIB", "apTotalStationsACInOctets"),
        ("HIPATH-WIRELESS-HWC-MIB", "apTotalStationsACOutOctets"),
        ("HIPATH-WIRELESS-HWC-MIB", "apRadioStatusChannel"),
        ("HIPATH-WIRELESS-HWC-MIB", "apRadioStatusChannelWidth"),
        ("HIPATH-WIRELESS-HWC-MIB", "apRadioStatusChannelOffset"),
        ("HIPATH-WIRELESS-HWC-MIB", "apPerfRadioPrevPeakChannelUtilization"),
        ("HIPATH-WIRELESS-HWC-MIB", "apPerfRadioCurPeakChannelUtilization"),
        ("HIPATH-WIRELESS-HWC-MIB", "apPerfRadioAverageChannelUtilization"),
        ("HIPATH-WIRELESS-HWC-MIB", "apPerfRadioCurrentChannelUtilization"),
        ("HIPATH-WIRELESS-HWC-MIB", "apPerfRadioPrevPeakRSS"),
        ("HIPATH-WIRELESS-HWC-MIB", "apPerfRadioCurPeakRSS"),
        ("HIPATH-WIRELESS-HWC-MIB", "apPerfRadioAverageRSS"),
        ("HIPATH-WIRELESS-HWC-MIB", "apPerfRadioCurrentRSS"),
        ("HIPATH-WIRELESS-HWC-MIB", "apPerfRadioPrevPeakSNR"),
        ("HIPATH-WIRELESS-HWC-MIB", "apPerfRadioCurPeakSNR"),
        ("HIPATH-WIRELESS-HWC-MIB", "apPerfRadioAverageSNR"),
        ("HIPATH-WIRELESS-HWC-MIB", "apPerfRadioCurrentSNR"),
        ("HIPATH-WIRELESS-HWC-MIB", "apPerfRadioPrevPeakPktRetx"),
        ("HIPATH-WIRELESS-HWC-MIB", "apPerfRadioCurPeakPktRetx"),
        ("HIPATH-WIRELESS-HWC-MIB", "apPerfRadioAveragePktRetx"),
        ("HIPATH-WIRELESS-HWC-MIB", "apPerfRadioCurrentPktRetx"),
        ("HIPATH-WIRELESS-HWC-MIB", "apPerfRadioPktRetx"),
        ("HIPATH-WIRELESS-HWC-MIB", "apAccPrevPeakAssocReqRx"),
        ("HIPATH-WIRELESS-HWC-MIB", "apAccCurPeakAssocReqRx"),
        ("HIPATH-WIRELESS-HWC-MIB", "apAccAverageAssocReqRx"),
        ("HIPATH-WIRELESS-HWC-MIB", "apAccCurrentAssocReqRx"),
        ("HIPATH-WIRELESS-HWC-MIB", "apAccAssocReqRx"),
        ("HIPATH-WIRELESS-HWC-MIB", "apAccPrevPeakReassocReqRx"),
        ("HIPATH-WIRELESS-HWC-MIB", "apAccCurPeakReassocReqRx"),
        ("HIPATH-WIRELESS-HWC-MIB", "apAccAverageReassocReqRx"),
        ("HIPATH-WIRELESS-HWC-MIB", "apAccCurrentReassocReqRx"),
        ("HIPATH-WIRELESS-HWC-MIB", "apAccReassocReqRx"),
        ("HIPATH-WIRELESS-HWC-MIB", "apAccPrevPeakDisassocDeauthReqTx"),
        ("HIPATH-WIRELESS-HWC-MIB", "apAccCurPeakDisassocDeauthReqTx"),
        ("HIPATH-WIRELESS-HWC-MIB", "apAccAverageDisassocDeauthReqTx"),
        ("HIPATH-WIRELESS-HWC-MIB", "apAccCurrentDisassocDeauthReqTx"),
        ("HIPATH-WIRELESS-HWC-MIB", "apAccDisassocDeauthReqTx"),
        ("HIPATH-WIRELESS-HWC-MIB", "apAccPrevPeakDisassocDeauthReqRx"),
        ("HIPATH-WIRELESS-HWC-MIB", "apAccCurPeakDisassocDeauthReqRx"),
        ("HIPATH-WIRELESS-HWC-MIB", "apAccAverageDisassocDeauthReqRx"),
        ("HIPATH-WIRELESS-HWC-MIB", "apAccCurrentDisassocDeauthReqRx"),
        ("HIPATH-WIRELESS-HWC-MIB", "apAccDisassocDeauthReqRx"),
        ("HIPATH-WIRELESS-HWC-MIB", "apPerfWlanPrevPeakClientsPerSec"),
        ("HIPATH-WIRELESS-HWC-MIB", "apPerfWlanCurPeakClientsPerSec"),
        ("HIPATH-WIRELESS-HWC-MIB", "apPerfWlanAverageClientsPerSec"),
        ("HIPATH-WIRELESS-HWC-MIB", "apPerfWlanCurrentClientsPerSec"),
        ("HIPATH-WIRELESS-HWC-MIB", "apPerfWlanPrevPeakULOctetsPerSec"),
        ("HIPATH-WIRELESS-HWC-MIB", "apPerfWlanCurPeakULOctetsPerSec"),
        ("HIPATH-WIRELESS-HWC-MIB", "apPerfWlanAverageULOctetsPerSec"),
        ("HIPATH-WIRELESS-HWC-MIB", "apPerfWlanCurrentULOctetsPerSec"),
        ("HIPATH-WIRELESS-HWC-MIB", "apPerfWlanULOctets"),
        ("HIPATH-WIRELESS-HWC-MIB", "apPerfWlanPrevPeakULPktsPerSec"),
        ("HIPATH-WIRELESS-HWC-MIB", "apPerfWlanCurPeakULPktsPerSec"),
        ("HIPATH-WIRELESS-HWC-MIB", "apPerfWlanAverageULPktsPerSec"),
        ("HIPATH-WIRELESS-HWC-MIB", "apPerfWlanCurrentULPktsPerSec"),
        ("HIPATH-WIRELESS-HWC-MIB", "apPerfWlanULPkts"),
        ("HIPATH-WIRELESS-HWC-MIB", "apPerfWlanPrevPeakDLOctetsPerSec"),
        ("HIPATH-WIRELESS-HWC-MIB", "apPerfWlanCurPeakDLOctetsPerSec"),
        ("HIPATH-WIRELESS-HWC-MIB", "apPerfWlanAverageDLOctetsPerSec"),
        ("HIPATH-WIRELESS-HWC-MIB", "apPerfWlanCurrentDLOctetsPerSec"),
        ("HIPATH-WIRELESS-HWC-MIB", "apPerfWlanDLOctets"),
        ("HIPATH-WIRELESS-HWC-MIB", "apPerfWlanPrevPeakDLPktsPerSec"),
        ("HIPATH-WIRELESS-HWC-MIB", "apPerfWlanCurPeakDLPktsPerSec"),
        ("HIPATH-WIRELESS-HWC-MIB", "apPerfWlanAverageDLPktsPerSec"),
        ("HIPATH-WIRELESS-HWC-MIB", "apPerfWlanCurrentDLPktsPerSec"),
        ("HIPATH-WIRELESS-HWC-MIB", "apPerfWlanDLPkts"),
        ("HIPATH-WIRELESS-HWC-MIB", "apChnlUtilPrevPeakUtilization"),
        ("HIPATH-WIRELESS-HWC-MIB", "apChnlUtilCurPeakUtilization"),
        ("HIPATH-WIRELESS-HWC-MIB", "apChnlUtilAverageUtilization"),
        ("HIPATH-WIRELESS-HWC-MIB", "apChnlUtilCurrentUtilization"),
        ("HIPATH-WIRELESS-HWC-MIB", "nearbyApInfo"),
        ("HIPATH-WIRELESS-HWC-MIB", "nearbyApBSSID"),
        ("HIPATH-WIRELESS-HWC-MIB", "nearbyApChannel"),
        ("HIPATH-WIRELESS-HWC-MIB", "nearbyApRSS"))
)
if mibBuilder.loadTexts:
    apStatsGroup.setStatus("current")

muACLGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 30, 5, 6)
)
muACLGroup.setObjects(
      *(("HIPATH-WIRELESS-HWC-MIB", "muACLRowStatus"),
        ("HIPATH-WIRELESS-HWC-MIB", "muACLMACAddress"),
        ("HIPATH-WIRELESS-HWC-MIB", "muACLType"))
)
if mibBuilder.loadTexts:
    muACLGroup.setStatus("current")

siteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 30, 5, 7)
)
siteGroup.setObjects(
      *(("HIPATH-WIRELESS-HWC-MIB", "siteID"),
        ("HIPATH-WIRELESS-HWC-MIB", "siteName"),
        ("HIPATH-WIRELESS-HWC-MIB", "siteLocalRadiusAuthentication"),
        ("HIPATH-WIRELESS-HWC-MIB", "siteDefaultDNSServer"),
        ("HIPATH-WIRELESS-HWC-MIB", "siteMaxEntries"),
        ("HIPATH-WIRELESS-HWC-MIB", "siteNumEntries"),
        ("HIPATH-WIRELESS-HWC-MIB", "siteTableNextAvailableIndex"),
        ("HIPATH-WIRELESS-HWC-MIB", "siteEnableSecureTunnel"),
        ("HIPATH-WIRELESS-HWC-MIB", "siteReplaceStnIDwithSiteName"),
        ("HIPATH-WIRELESS-HWC-MIB", "siteRowStatus"),
        ("HIPATH-WIRELESS-HWC-MIB", "siteEncryptCommAPtoController"),
        ("HIPATH-WIRELESS-HWC-MIB", "siteEncryptCommBetweenAPs"),
        ("HIPATH-WIRELESS-HWC-MIB", "siteBandPreferenceEnable"),
        ("HIPATH-WIRELESS-HWC-MIB", "siteLoadControlEnableR1"),
        ("HIPATH-WIRELESS-HWC-MIB", "siteLoadControlEnableR2"),
        ("HIPATH-WIRELESS-HWC-MIB", "siteMaxClientR1"),
        ("HIPATH-WIRELESS-HWC-MIB", "siteMaxClientR2"),
        ("HIPATH-WIRELESS-HWC-MIB", "siteStrictLimitEnableR1"),
        ("HIPATH-WIRELESS-HWC-MIB", "siteStrictLimitEnableR2"))
)
if mibBuilder.loadTexts:
    siteGroup.setStatus("current")

sitePolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 30, 5, 8)
)
sitePolicyGroup.setObjects(
    ("HIPATH-WIRELESS-HWC-MIB", "sitePolicyMember")
)
if mibBuilder.loadTexts:
    sitePolicyGroup.setStatus("current")

siteCosGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 30, 5, 9)
)
siteCosGroup.setObjects(
    ("HIPATH-WIRELESS-HWC-MIB", "siteCoSMember")
)
if mibBuilder.loadTexts:
    siteCosGroup.setStatus("current")

siteAPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 30, 5, 10)
)
siteAPGroup.setObjects(
    ("HIPATH-WIRELESS-HWC-MIB", "siteAPMember")
)
if mibBuilder.loadTexts:
    siteAPGroup.setStatus("current")

siteWlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 30, 5, 11)
)
siteWlanGroup.setObjects(
    ("HIPATH-WIRELESS-HWC-MIB", "siteWlanApRadioAssigned")
)
if mibBuilder.loadTexts:
    siteWlanGroup.setStatus("current")

apGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 30, 5, 12)
)
apGroup.setObjects(
      *(("HIPATH-WIRELESS-HWC-MIB", "apIndex"),
        ("HIPATH-WIRELESS-HWC-MIB", "apName"),
        ("HIPATH-WIRELESS-HWC-MIB", "apDesc"),
        ("HIPATH-WIRELESS-HWC-MIB", "apSerialNumber"),
        ("HIPATH-WIRELESS-HWC-MIB", "apPortifIndex"),
        ("HIPATH-WIRELESS-HWC-MIB", "apWiredIfIndex"),
        ("HIPATH-WIRELESS-HWC-MIB", "apSoftwareVersion"),
        ("HIPATH-WIRELESS-HWC-MIB", "apSpecific"),
        ("HIPATH-WIRELESS-HWC-MIB", "apBroadcastDisassociate"),
        ("HIPATH-WIRELESS-HWC-MIB", "apRowStatus"),
        ("HIPATH-WIRELESS-HWC-MIB", "apVlanID"),
        ("HIPATH-WIRELESS-HWC-MIB", "apIpAssignmentType"),
        ("HIPATH-WIRELESS-HWC-MIB", "apIfMAC"),
        ("HIPATH-WIRELESS-HWC-MIB", "apHwVersion"),
        ("HIPATH-WIRELESS-HWC-MIB", "apSwVersion"),
        ("HIPATH-WIRELESS-HWC-MIB", "apEnvironment"),
        ("HIPATH-WIRELESS-HWC-MIB", "apHome"),
        ("HIPATH-WIRELESS-HWC-MIB", "apRole"),
        ("HIPATH-WIRELESS-HWC-MIB", "apState"),
        ("HIPATH-WIRELESS-HWC-MIB", "apStatus"),
        ("HIPATH-WIRELESS-HWC-MIB", "apPollTimeout"),
        ("HIPATH-WIRELESS-HWC-MIB", "apPollInterval"),
        ("HIPATH-WIRELESS-HWC-MIB", "apTelnetAccess"),
        ("HIPATH-WIRELESS-HWC-MIB", "apMaintainClientSession"),
        ("HIPATH-WIRELESS-HWC-MIB", "apRestartServiceContAbsent"),
        ("HIPATH-WIRELESS-HWC-MIB", "apHostname"),
        ("HIPATH-WIRELESS-HWC-MIB", "apLocation"),
        ("HIPATH-WIRELESS-HWC-MIB", "apStaticMTUsize"),
        ("HIPATH-WIRELESS-HWC-MIB", "apSiteID"),
        ("HIPATH-WIRELESS-HWC-MIB", "apZone"),
        ("HIPATH-WIRELESS-HWC-MIB", "apLLDP"),
        ("HIPATH-WIRELESS-HWC-MIB", "apLEDMode"),
        ("HIPATH-WIRELESS-HWC-MIB", "apLocationbasedService"),
        ("HIPATH-WIRELESS-HWC-MIB", "apSecureTunnel"),
        ("HIPATH-WIRELESS-HWC-MIB", "apEncryptCntTraffic"),
        ("HIPATH-WIRELESS-HWC-MIB", "apIpAddress"),
        ("HIPATH-WIRELESS-HWC-MIB", "apMICErrorWarning"),
        ("HIPATH-WIRELESS-HWC-MIB", "apIPAddress"),
        ("HIPATH-WIRELESS-HWC-MIB", "apSecureDataTunnelType"),
        ("HIPATH-WIRELESS-HWC-MIB", "apIPMulticastAssembly"),
        ("HIPATH-WIRELESS-HWC-MIB", "apSSHConnection"))
)
if mibBuilder.loadTexts:
    apGroup.setStatus("current")

wlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 30, 5, 13)
)
wlanGroup.setObjects(
      *(("HIPATH-WIRELESS-HWC-MIB", "wlanID"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanRowStatus"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanServiceType"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanName"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanSSID"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanSynchronize"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanEnabled"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanDefaultTopologyID"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanSessionTimeout"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanIdleTimeoutPreAuth"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanIdleSessionPostAuth"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanSupressSSID"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanDot11hSupport"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanDot11hClientPowerReduction"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanProcessClientIE"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanEngerySaveMode"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanBlockMuToMuTraffic"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanRemoteable"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanVNSID"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanMaxEntries"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanRadioManagement11k"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanBeaconReport"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanQuietIE"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanMirrorN"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanNetFlow"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanAppVisibility"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanNumEntries"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanTableNextAvailableIndex"))
)
if mibBuilder.loadTexts:
    wlanGroup.setStatus("current")

wlanStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 30, 5, 14)
)
wlanStatsGroup.setObjects(
      *(("HIPATH-WIRELESS-HWC-MIB", "wlanStatsAssociatedClients"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanStatsRadiusTotRequests"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanStatsRadiusReqFailed"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanStatsRadiusReqRejected"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanStatsID"))
)
if mibBuilder.loadTexts:
    wlanStatsGroup.setStatus("current")

topologyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 30, 5, 15)
)
topologyGroup.setObjects(
      *(("HIPATH-WIRELESS-HWC-MIB", "topologyName"),
        ("HIPATH-WIRELESS-HWC-MIB", "topologyMode"),
        ("HIPATH-WIRELESS-HWC-MIB", "topologyTagged"),
        ("HIPATH-WIRELESS-HWC-MIB", "topologyVlanID"),
        ("HIPATH-WIRELESS-HWC-MIB", "topologyEgressPort"),
        ("HIPATH-WIRELESS-HWC-MIB", "topologyLayer3"),
        ("HIPATH-WIRELESS-HWC-MIB", "topologyIPAddress"),
        ("HIPATH-WIRELESS-HWC-MIB", "topologyIPMask"),
        ("HIPATH-WIRELESS-HWC-MIB", "topologyMTUsize"),
        ("HIPATH-WIRELESS-HWC-MIB", "topologyGateway"),
        ("HIPATH-WIRELESS-HWC-MIB", "topologyDHCPUsage"),
        ("HIPATH-WIRELESS-HWC-MIB", "topologyAPRegistration"),
        ("HIPATH-WIRELESS-HWC-MIB", "topologyManagementTraffic"),
        ("HIPATH-WIRELESS-HWC-MIB", "topologySynchronize"),
        ("HIPATH-WIRELESS-HWC-MIB", "topologySyncGateway"),
        ("HIPATH-WIRELESS-HWC-MIB", "topologySyncMask"),
        ("HIPATH-WIRELESS-HWC-MIB", "topologySyncIPStart"),
        ("HIPATH-WIRELESS-HWC-MIB", "topologySyncIPEnd"),
        ("HIPATH-WIRELESS-HWC-MIB", "topologyStaticIPv6Address"),
        ("HIPATH-WIRELESS-HWC-MIB", "topologyLinkLocalIPv6Address"),
        ("HIPATH-WIRELESS-HWC-MIB", "topologyPreFixLength"),
        ("HIPATH-WIRELESS-HWC-MIB", "topologyIPv6Gateway"),
        ("HIPATH-WIRELESS-HWC-MIB", "topologyDynamicEgress"),
        ("HIPATH-WIRELESS-HWC-MIB", "topologyIsGroup"),
        ("HIPATH-WIRELESS-HWC-MIB", "topologyGroupMembers"),
        ("HIPATH-WIRELESS-HWC-MIB", "topologyMemberId"))
)
if mibBuilder.loadTexts:
    topologyGroup.setStatus("current")

topologyStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 30, 5, 16)
)
topologyStatGroup.setObjects(
      *(("HIPATH-WIRELESS-HWC-MIB", "topologyName"),
        ("HIPATH-WIRELESS-HWC-MIB", "topoStatName"),
        ("HIPATH-WIRELESS-HWC-MIB", "topoStatTxPkts"),
        ("HIPATH-WIRELESS-HWC-MIB", "topoStatRxPkts"),
        ("HIPATH-WIRELESS-HWC-MIB", "topoStatTxOctets"),
        ("HIPATH-WIRELESS-HWC-MIB", "topoStatRxOctets"),
        ("HIPATH-WIRELESS-HWC-MIB", "topoStatMulticastTxPkts"),
        ("HIPATH-WIRELESS-HWC-MIB", "topoStatMulticastRxPkts"),
        ("HIPATH-WIRELESS-HWC-MIB", "topoStatBroadcastTxPkts"),
        ("HIPATH-WIRELESS-HWC-MIB", "topoStatBroadcastRxPkts"),
        ("HIPATH-WIRELESS-HWC-MIB", "topoStatFrameChkSeqErrors"),
        ("HIPATH-WIRELESS-HWC-MIB", "topoStatFrameTooLongErrors"),
        ("HIPATH-WIRELESS-HWC-MIB", "topoWireStatName"),
        ("HIPATH-WIRELESS-HWC-MIB", "topoWireStatTxPkts"),
        ("HIPATH-WIRELESS-HWC-MIB", "topoWireStatRxPkts"),
        ("HIPATH-WIRELESS-HWC-MIB", "topoWireStatTxOctets"),
        ("HIPATH-WIRELESS-HWC-MIB", "topoWireStatRxOctets"),
        ("HIPATH-WIRELESS-HWC-MIB", "topoWireStatMulticastTxPkts"),
        ("HIPATH-WIRELESS-HWC-MIB", "topoWireStatMulticastRxPkts"),
        ("HIPATH-WIRELESS-HWC-MIB", "topoWireStatBroadcastTxPkts"),
        ("HIPATH-WIRELESS-HWC-MIB", "topoWireStatBroadcastRxPkts"),
        ("HIPATH-WIRELESS-HWC-MIB", "topoWireStatFrameChkSeqErrors"),
        ("HIPATH-WIRELESS-HWC-MIB", "topoWireStatFrameTooLongErrors"),
        ("HIPATH-WIRELESS-HWC-MIB", "topoCompleteStatName"),
        ("HIPATH-WIRELESS-HWC-MIB", "topoCompleteStatTxPkts"),
        ("HIPATH-WIRELESS-HWC-MIB", "topoCompleteStatRxPkts"),
        ("HIPATH-WIRELESS-HWC-MIB", "topoCompleteStatTxOctets"),
        ("HIPATH-WIRELESS-HWC-MIB", "topoCompleteStatRxOctets"),
        ("HIPATH-WIRELESS-HWC-MIB", "topoCompleteStatMulticastTxPkts"),
        ("HIPATH-WIRELESS-HWC-MIB", "topoCompleteStatMulticastRxPkts"),
        ("HIPATH-WIRELESS-HWC-MIB", "topoCompleteStatBroadcastTxPkts"),
        ("HIPATH-WIRELESS-HWC-MIB", "topoCompleteStatBroadcastRxPkts"),
        ("HIPATH-WIRELESS-HWC-MIB", "topoCompleteStatFrameChkSeqErrors"),
        ("HIPATH-WIRELESS-HWC-MIB", "topoCompleteStatFrameTooLongErrors"))
)
if mibBuilder.loadTexts:
    topologyStatGroup.setStatus("current")

loadGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 30, 5, 17)
)
loadGroup.setObjects(
      *(("HIPATH-WIRELESS-HWC-MIB", "loadGroupID"),
        ("HIPATH-WIRELESS-HWC-MIB", "loadGroupName"),
        ("HIPATH-WIRELESS-HWC-MIB", "loadGroupType"),
        ("HIPATH-WIRELESS-HWC-MIB", "loadGroupBandPreference"),
        ("HIPATH-WIRELESS-HWC-MIB", "loadGroupClientCountRadio1"),
        ("HIPATH-WIRELESS-HWC-MIB", "loadGroupClientCountRadio2"),
        ("HIPATH-WIRELESS-HWC-MIB", "loadGroupLoadControlEnableR1"),
        ("HIPATH-WIRELESS-HWC-MIB", "loadGroupLoadControlEnableR2"),
        ("HIPATH-WIRELESS-HWC-MIB", "loadGroupLoadControlStrictLimitR1"),
        ("HIPATH-WIRELESS-HWC-MIB", "loadGroupLoadControlStrictLimitR2"))
)
if mibBuilder.loadTexts:
    loadGroup.setStatus("current")

widsWipsObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 30, 5, 18)
)
widsWipsObjectsGroup.setObjects(
      *(("HIPATH-WIRELESS-HWC-MIB", "mitigatorAnalysisEngine"),
        ("HIPATH-WIRELESS-HWC-MIB", "activeThreatsCounts"),
        ("HIPATH-WIRELESS-HWC-MIB", "uncategorizedAPCounts"),
        ("HIPATH-WIRELESS-HWC-MIB", "friendlyAPCounts"),
        ("HIPATH-WIRELESS-HWC-MIB", "scanGroupMaxEntries"),
        ("HIPATH-WIRELESS-HWC-MIB", "scanGroupsCurrentEntries"))
)
if mibBuilder.loadTexts:
    widsWipsObjectsGroup.setStatus("current")

widsWipsEngineGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 30, 5, 19)
)
widsWipsEngineGroup.setObjects(
      *(("HIPATH-WIRELESS-HWC-MIB", "widsWipsEngineRowStatus"),
        ("HIPATH-WIRELESS-HWC-MIB", "widsWipsEngineControllerIPAddress"),
        ("HIPATH-WIRELESS-HWC-MIB", "widsWipsEnginePollInterval"),
        ("HIPATH-WIRELESS-HWC-MIB", "widsWipsEnginePollRetry"))
)
if mibBuilder.loadTexts:
    widsWipsEngineGroup.setStatus("current")

outOfServiceScanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 30, 5, 20)
)
outOfServiceScanGroup.setObjects(
      *(("HIPATH-WIRELESS-HWC-MIB", "outOfSrvScanGrpName"),
        ("HIPATH-WIRELESS-HWC-MIB", "outOfSrvScanGrpRadio"),
        ("HIPATH-WIRELESS-HWC-MIB", "outOfSrvScanGrpChannelList"),
        ("HIPATH-WIRELESS-HWC-MIB", "outOfSrvScanGrpScanType"),
        ("HIPATH-WIRELESS-HWC-MIB", "outOfSrvScanGrpChannelDwellTime"),
        ("HIPATH-WIRELESS-HWC-MIB", "outOfSrvScanGrpScanTimeInterval"),
        ("HIPATH-WIRELESS-HWC-MIB", "outOfSrvScanGrpSecurityScan"),
        ("HIPATH-WIRELESS-HWC-MIB", "outOfSrvScanGrpScanActivity"),
        ("HIPATH-WIRELESS-HWC-MIB", "outOfSrvScanGrpScanRowStatus"))
)
if mibBuilder.loadTexts:
    outOfServiceScanGroup.setStatus("current")

inServiceScanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 30, 5, 21)
)
inServiceScanGroup.setObjects(
      *(("HIPATH-WIRELESS-HWC-MIB", "inSrvScanGrpName"),
        ("HIPATH-WIRELESS-HWC-MIB", "inSrvScanGrpMaxConcurrentAttacksPerAP"),
        ("HIPATH-WIRELESS-HWC-MIB", "inSrvScanGrpCounterMeasuresType"),
        ("HIPATH-WIRELESS-HWC-MIB", "inSrvScanGrpScan2400MHzSelection"),
        ("HIPATH-WIRELESS-HWC-MIB", "inSrvScanGrpScan5GHzSelection"),
        ("HIPATH-WIRELESS-HWC-MIB", "inSrvScanGrpRowStatus"),
        ("HIPATH-WIRELESS-HWC-MIB", "inSrvScanGrpSecurityThreats"),
        ("HIPATH-WIRELESS-HWC-MIB", "inSrvScanGrpblockAdHocClientsPeriod"),
        ("HIPATH-WIRELESS-HWC-MIB", "inSrvScanGrpClassifySourceIF"),
        ("HIPATH-WIRELESS-HWC-MIB", "inSrvScanGrpDetectRogueAP"),
        ("HIPATH-WIRELESS-HWC-MIB", "inSrvScanGrpListeningPort"))
)
if mibBuilder.loadTexts:
    inServiceScanGroup.setStatus("current")

scanGroupAPAssignmentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 30, 5, 22)
)
scanGroupAPAssignmentGroup.setObjects(
      *(("HIPATH-WIRELESS-HWC-MIB", "scanGroupAPAssignApSerial"),
        ("HIPATH-WIRELESS-HWC-MIB", "scanGroupAPAssignName"),
        ("HIPATH-WIRELESS-HWC-MIB", "scanGroupAPAssignRadio1"),
        ("HIPATH-WIRELESS-HWC-MIB", "scanGroupAPAssignRadio2"),
        ("HIPATH-WIRELESS-HWC-MIB", "scanGroupAPAssignInactiveAP"),
        ("HIPATH-WIRELESS-HWC-MIB", "scanGroupAPAssignAllowScanning"),
        ("HIPATH-WIRELESS-HWC-MIB", "scanGroupAPAssignGroupName"),
        ("HIPATH-WIRELESS-HWC-MIB", "scanGroupAPAssignAllowSpectrumAnalysis"),
        ("HIPATH-WIRELESS-HWC-MIB", "scanGroupAPAssignControllerIPAddress"),
        ("HIPATH-WIRELESS-HWC-MIB", "scanGroupAPAssignFordwardingService"))
)
if mibBuilder.loadTexts:
    scanGroupAPAssignmentGroup.setStatus("current")

scanAPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 30, 5, 23)
)
scanAPGroup.setObjects(
      *(("HIPATH-WIRELESS-HWC-MIB", "scanAPSerialNumber"),
        ("HIPATH-WIRELESS-HWC-MIB", "scanAPControllerIPAddress"),
        ("HIPATH-WIRELESS-HWC-MIB", "scanAPRowStatus"),
        ("HIPATH-WIRELESS-HWC-MIB", "scanAPAcessPointName"),
        ("HIPATH-WIRELESS-HWC-MIB", "scanAPProfileName"),
        ("HIPATH-WIRELESS-HWC-MIB", "scanAPProfileType"))
)
if mibBuilder.loadTexts:
    scanAPGroup.setStatus("current")

friendlyAPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 30, 5, 24)
)
friendlyAPGroup.setObjects(
      *(("HIPATH-WIRELESS-HWC-MIB", "friendlyAPMacAddress"),
        ("HIPATH-WIRELESS-HWC-MIB", "friendlyAPSSID"),
        ("HIPATH-WIRELESS-HWC-MIB", "friendlyAPDescription"),
        ("HIPATH-WIRELESS-HWC-MIB", "friendlyAPManufacturer"))
)
if mibBuilder.loadTexts:
    friendlyAPGroup.setStatus("current")

wlanSecurityReportGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 30, 5, 25)
)
wlanSecurityReportGroup.setObjects(
      *(("HIPATH-WIRELESS-HWC-MIB", "wlanSecurityReportFlag"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanSecurityReportUnsecureType"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanSecurityReportNotes"),
        ("HIPATH-WIRELESS-HWC-MIB", "wlanUnsecuredWlanCounts"))
)
if mibBuilder.loadTexts:
    wlanSecurityReportGroup.setStatus("current")

apAntennaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 30, 5, 26)
)
apAntennaGroup.setObjects(
      *(("HIPATH-WIRELESS-HWC-MIB", "apAntennanName"),
        ("HIPATH-WIRELESS-HWC-MIB", "apAntennaType"))
)
if mibBuilder.loadTexts:
    apAntennaGroup.setStatus("current")

muAccessListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 30, 5, 27)
)
muAccessListGroup.setObjects(
      *(("HIPATH-WIRELESS-HWC-MIB", "muAccessListMACAddress"),
        ("HIPATH-WIRELESS-HWC-MIB", "muAccessListBitmaskLength"),
        ("HIPATH-WIRELESS-HWC-MIB", "muAccessListRowStatus"))
)
if mibBuilder.loadTexts:
    muAccessListGroup.setStatus("current")

activeThreatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 30, 5, 28)
)
activeThreatGroup.setObjects(
      *(("HIPATH-WIRELESS-HWC-MIB", "activeThreatCategory"),
        ("HIPATH-WIRELESS-HWC-MIB", "activeThreatDeviceMAC"),
        ("HIPATH-WIRELESS-HWC-MIB", "activeThreatDateTime"),
        ("HIPATH-WIRELESS-HWC-MIB", "activeThreatCounterMeasure"),
        ("HIPATH-WIRELESS-HWC-MIB", "activeThreatAPName"),
        ("HIPATH-WIRELESS-HWC-MIB", "activeThreatRSS"),
        ("HIPATH-WIRELESS-HWC-MIB", "activeThreatExtraDetails"),
        ("HIPATH-WIRELESS-HWC-MIB", "activeThreatThreat"))
)
if mibBuilder.loadTexts:
    activeThreatGroup.setStatus("current")

countermeasureAPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 30, 5, 29)
)
countermeasureAPGroup.setObjects(
      *(("HIPATH-WIRELESS-HWC-MIB", "countermeasureAPName"),
        ("HIPATH-WIRELESS-HWC-MIB", "countermeasureAPThreatCategory"),
        ("HIPATH-WIRELESS-HWC-MIB", "countermeasureAPCountermeasure"),
        ("HIPATH-WIRELESS-HWC-MIB", "countermeasureAPTime"),
        ("HIPATH-WIRELESS-HWC-MIB", "countermeasureAPSerial"))
)
if mibBuilder.loadTexts:
    countermeasureAPGroup.setStatus("current")

blaclistedClientGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 30, 5, 30)
)
blaclistedClientGroup.setObjects(
      *(("HIPATH-WIRELESS-HWC-MIB", "blacklistedClientMAC"),
        ("HIPATH-WIRELESS-HWC-MIB", "blacklistedClientStatTime"),
        ("HIPATH-WIRELESS-HWC-MIB", "blacklistedClientEndTime"),
        ("HIPATH-WIRELESS-HWC-MIB", "blacklistedClientReason"))
)
if mibBuilder.loadTexts:
    blaclistedClientGroup.setStatus("current")

threatSummaryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 30, 5, 31)
)
threatSummaryGroup.setObjects(
      *(("HIPATH-WIRELESS-HWC-MIB", "threatSummaryCategory"),
        ("HIPATH-WIRELESS-HWC-MIB", "threatSummaryActiveThreat"),
        ("HIPATH-WIRELESS-HWC-MIB", "threatSummaryHistoricalCounts"))
)
if mibBuilder.loadTexts:
    threatSummaryGroup.setStatus("current")

licensingInformationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 30, 5, 32)
)
licensingInformationGroup.setObjects(
      *(("HIPATH-WIRELESS-HWC-MIB", "licenseRegulatoryDomain"),
        ("HIPATH-WIRELESS-HWC-MIB", "licenseType"),
        ("HIPATH-WIRELESS-HWC-MIB", "licenseDaysRemaining"),
        ("HIPATH-WIRELESS-HWC-MIB", "licenseAvailableAP"),
        ("HIPATH-WIRELESS-HWC-MIB", "licenseInServiceRadarAP"),
        ("HIPATH-WIRELESS-HWC-MIB", "licenseMode"),
        ("HIPATH-WIRELESS-HWC-MIB", "licenseLocalAP"),
        ("HIPATH-WIRELESS-HWC-MIB", "licenseForeignAP"),
        ("HIPATH-WIRELESS-HWC-MIB", "licenseLocalRadarAP"),
        ("HIPATH-WIRELESS-HWC-MIB", "licenseForeignRadarAP"))
)
if mibBuilder.loadTexts:
    licensingInformationGroup.setStatus("current")

stationsByProtocolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 30, 5, 33)
)
stationsByProtocolGroup.setObjects(
      *(("HIPATH-WIRELESS-HWC-MIB", "stationsByProtocolA"),
        ("HIPATH-WIRELESS-HWC-MIB", "stationsByProtocolB"),
        ("HIPATH-WIRELESS-HWC-MIB", "stationsByProtocolG"),
        ("HIPATH-WIRELESS-HWC-MIB", "stationsByProtocolN24"),
        ("HIPATH-WIRELESS-HWC-MIB", "stationsByProtocolN5"),
        ("HIPATH-WIRELESS-HWC-MIB", "stationsByProtocolUnavailable"),
        ("HIPATH-WIRELESS-HWC-MIB", "stationsByProtocolError"),
        ("HIPATH-WIRELESS-HWC-MIB", "stationsByProtocolAC"))
)
if mibBuilder.loadTexts:
    stationsByProtocolGroup.setStatus("current")

apByChannelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 30, 5, 34)
)
apByChannelGroup.setObjects(
    ("HIPATH-WIRELESS-HWC-MIB", "apByChannelAPs")
)
if mibBuilder.loadTexts:
    apByChannelGroup.setStatus("current")

uncategorizedAPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 30, 5, 35)
)
uncategorizedAPGroup.setObjects(
      *(("HIPATH-WIRELESS-HWC-MIB", "uncategorizedAPDescption"),
        ("HIPATH-WIRELESS-HWC-MIB", "uncategorizedAPManufacturer"),
        ("HIPATH-WIRELESS-HWC-MIB", "uncategorizedAPClassify"),
        ("HIPATH-WIRELESS-HWC-MIB", "uncategorizedAPSSID"))
)
if mibBuilder.loadTexts:
    uncategorizedAPGroup.setStatus("current")

authorizedAPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 30, 5, 36)
)
authorizedAPGroup.setObjects(
      *(("HIPATH-WIRELESS-HWC-MIB", "authorizedAPDescription"),
        ("HIPATH-WIRELESS-HWC-MIB", "authorizedAPManufacturer"),
        ("HIPATH-WIRELESS-HWC-MIB", "authorizedAPClassify"),
        ("HIPATH-WIRELESS-HWC-MIB", "authorizedAPRowStatus"))
)
if mibBuilder.loadTexts:
    authorizedAPGroup.setStatus("current")

prohibitedAPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 30, 5, 37)
)
prohibitedAPGroup.setObjects(
      *(("HIPATH-WIRELESS-HWC-MIB", "prohibitedAPCategory"),
        ("HIPATH-WIRELESS-HWC-MIB", "prohibitedAPDescription"),
        ("HIPATH-WIRELESS-HWC-MIB", "prohibitedAPManufacturer"),
        ("HIPATH-WIRELESS-HWC-MIB", "prohibitedAPClassify"),
        ("HIPATH-WIRELESS-HWC-MIB", "prohibitedAPRowStatus"))
)
if mibBuilder.loadTexts:
    prohibitedAPGroup.setStatus("current")

dedicatedScanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 30, 5, 38)
)
dedicatedScanGroup.setObjects(
      *(("HIPATH-WIRELESS-HWC-MIB", "dedicatedScanGrpName"),
        ("HIPATH-WIRELESS-HWC-MIB", "dedicatedScanGrpMaxConcurrentAttacksPerAP"),
        ("HIPATH-WIRELESS-HWC-MIB", "dedicatedScanGrpCounterMeasures"),
        ("HIPATH-WIRELESS-HWC-MIB", "dedicatedScanGrpScan2400MHzFreq"),
        ("HIPATH-WIRELESS-HWC-MIB", "dedicatedScanGrpScan5GHzFreq"),
        ("HIPATH-WIRELESS-HWC-MIB", "dedicatedScanGrpRowStatus"),
        ("HIPATH-WIRELESS-HWC-MIB", "dedicatedScanGrpSecurityThreats"),
        ("HIPATH-WIRELESS-HWC-MIB", "dedicatedScanGrpBlockAdHocPeriod"),
        ("HIPATH-WIRELESS-HWC-MIB", "dedicatedScanGrpClassifySourceIF"),
        ("HIPATH-WIRELESS-HWC-MIB", "dedicatedScanGrpDetectRogueAP"),
        ("HIPATH-WIRELESS-HWC-MIB", "dedicatedScanGrpListeningPort"))
)
if mibBuilder.loadTexts:
    dedicatedScanGroup.setStatus("current")

apRadioAntennaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 30, 5, 39)
)
apRadioAntennaGroup.setObjects(
      *(("HIPATH-WIRELESS-HWC-MIB", "apRadioAntennaType"),
        ("HIPATH-WIRELESS-HWC-MIB", "apRadioAntennaModel"),
        ("HIPATH-WIRELESS-HWC-MIB", "apRadioAttenuation"))
)
if mibBuilder.loadTexts:
    apRadioAntennaGroup.setStatus("current")

radiusFastFailoverEventsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 30, 5, 40)
)
radiusFastFailoverEventsGroup.setObjects(
    ("HIPATH-WIRELESS-HWC-MIB", "fastFailoverEvents")
)
if mibBuilder.loadTexts:
    radiusFastFailoverEventsGroup.setStatus("current")

dhcpRelayListenersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 30, 5, 41)
)
dhcpRelayListenersGroup.setObjects(
      *(("HIPATH-WIRELESS-HWC-MIB", "dhcpRelayListenersRowStatus"),
        ("HIPATH-WIRELESS-HWC-MIB", "destinationName"),
        ("HIPATH-WIRELESS-HWC-MIB", "destinationIP"),
        ("HIPATH-WIRELESS-HWC-MIB", "dhcpRelayListenersMaxEntries"),
        ("HIPATH-WIRELESS-HWC-MIB", "dhcpRelayListenersNextIndex"),
        ("HIPATH-WIRELESS-HWC-MIB", "dhcpRelayListenersNumEntries"))
)
if mibBuilder.loadTexts:
    dhcpRelayListenersGroup.setStatus("current")

authenticationAdvancedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 30, 5, 42)
)
authenticationAdvancedGroup.setObjects(
      *(("HIPATH-WIRELESS-HWC-MIB", "includeServiceType"),
        ("HIPATH-WIRELESS-HWC-MIB", "clientMessageDelayTime"),
        ("HIPATH-WIRELESS-HWC-MIB", "radiusAccounting"),
        ("HIPATH-WIRELESS-HWC-MIB", "serverUsageModel"),
        ("HIPATH-WIRELESS-HWC-MIB", "radacctStartOnIPAddr"),
        ("HIPATH-WIRELESS-HWC-MIB", "clientServiceTypeLogin"),
        ("HIPATH-WIRELESS-HWC-MIB", "applyMacAddressFormat"))
)
if mibBuilder.loadTexts:
    authenticationAdvancedGroup.setStatus("current")

radiusExtnsSettingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 30, 5, 43)
)
radiusExtnsSettingGroup.setObjects(
      *(("HIPATH-WIRELESS-HWC-MIB", "pollingMechanism"),
        ("HIPATH-WIRELESS-HWC-MIB", "serverPollingInterval"))
)
if mibBuilder.loadTexts:
    radiusExtnsSettingGroup.setStatus("current")


# Notification objects

hiPathWirelessLogAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 9, 6)
)
hiPathWirelessLogAlarm.setObjects(
      *(("HIPATH-WIRELESS-HWC-MIB", "logEventSeverity"),
        ("HIPATH-WIRELESS-HWC-MIB", "logEventComponent"),
        ("HIPATH-WIRELESS-HWC-MIB", "logEventDescription"))
)
if mibBuilder.loadTexts:
    hiPathWirelessLogAlarm.setStatus(
        "current"
    )

apTunnelAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 19, 4)
)
apTunnelAlarm.setObjects(
      *(("HIPATH-WIRELESS-HWC-MIB", "apEventId"),
        ("HIPATH-WIRELESS-HWC-MIB", "apEventDescription"),
        ("HIPATH-WIRELESS-HWC-MIB", "apEventAPSerialNumber"))
)
if mibBuilder.loadTexts:
    apTunnelAlarm.setStatus(
        "current"
    )

stationEventAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 20, 11)
)
stationEventAlarm.setObjects(
      *(("HIPATH-WIRELESS-HWC-MIB", "stationEventType"),
        ("HIPATH-WIRELESS-HWC-MIB", "stationMacAddress"),
        ("HIPATH-WIRELESS-HWC-MIB", "stationIPAddress"),
        ("HIPATH-WIRELESS-HWC-MIB", "stationAPName"),
        ("HIPATH-WIRELESS-HWC-MIB", "stationAPSSID"),
        ("HIPATH-WIRELESS-HWC-MIB", "stationDetailEvent"),
        ("HIPATH-WIRELESS-HWC-MIB", "stationRoamedAPName"),
        ("HIPATH-WIRELESS-HWC-MIB", "stationName"),
        ("HIPATH-WIRELESS-HWC-MIB", "stationBSSID"),
        ("HIPATH-WIRELESS-HWC-MIB", "stationEventTimeStamp"),
        ("HIPATH-WIRELESS-HWC-MIB", "stationIPv6Address1"),
        ("HIPATH-WIRELESS-HWC-MIB", "stationIPv6Address2"),
        ("HIPATH-WIRELESS-HWC-MIB", "stationIPv6Address3"))
)
if mibBuilder.loadTexts:
    stationEventAlarm.setStatus(
        "current"
    )


# Notifications groups

hiPathWirelessHWCAlarms = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 30, 3)
)
hiPathWirelessHWCAlarms.setObjects(
      *(("HIPATH-WIRELESS-HWC-MIB", "hiPathWirelessLogAlarm"),
        ("HIPATH-WIRELESS-HWC-MIB", "stationEventAlarm"),
        ("HIPATH-WIRELESS-HWC-MIB", "apTunnelAlarm"))
)
if mibBuilder.loadTexts:
    hiPathWirelessHWCAlarms.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hiPathWirelessHWCModule = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4329, 15, 3, 30, 1)
)
if mibBuilder.loadTexts:
    hiPathWirelessHWCModule.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HIPATH-WIRELESS-HWC-MIB",
    **{"LogEventSeverity": LogEventSeverity,
       "HundredthOfGauge64": HundredthOfGauge64,
       "HundredthOfGauge32": HundredthOfGauge32,
       "HundredthOfInt32": HundredthOfInt32,
       "hiPathWirelessController": hiPathWirelessController,
       "systemObjects": systemObjects,
       "sysSoftwareVersion": sysSoftwareVersion,
       "sysLogLevel": sysLogLevel,
       "sysSerialNo": sysSerialNo,
       "sysLogSupport": sysLogSupport,
       "hiPathWirelessAppLogFacility": hiPathWirelessAppLogFacility,
       "serviceLogFacility": serviceLogFacility,
       "includeAllServiceMessages": includeAllServiceMessages,
       "sysLogServersTable": sysLogServersTable,
       "sysLogServersEntry": sysLogServersEntry,
       "sysLogServerIndex": sysLogServerIndex,
       "sysLogServerEnabled": sysLogServerEnabled,
       "sysLogServerIP": sysLogServerIP,
       "sysLogServerPort": sysLogServerPort,
       "sysLogServerRowStatus": sysLogServerRowStatus,
       "sysCPUType": sysCPUType,
       "apLogManagement": apLogManagement,
       "apLogCollectionEnable": apLogCollectionEnable,
       "apLogFrequency": apLogFrequency,
       "apLogDestination": apLogDestination,
       "apLogFTProtocol": apLogFTProtocol,
       "apLogServerIP": apLogServerIP,
       "apLogUserId": apLogUserId,
       "apLogPassword": apLogPassword,
       "apLogDirectory": apLogDirectory,
       "apLogSelectedAPsTable": apLogSelectedAPsTable,
       "apLogSelectedAPsEntry": apLogSelectedAPsEntry,
       "apSerialNo": apSerialNo,
       "select": select,
       "apLogQuickSelectedOption": apLogQuickSelectedOption,
       "apLogFileUtility": apLogFileUtility,
       "apLogFileUtilityLimit": apLogFileUtilityLimit,
       "apLogFileUtilityCurrent": apLogFileUtilityCurrent,
       "apLogFileCopyTable": apLogFileCopyTable,
       "apLogFileCopyEntry": apLogFileCopyEntry,
       "apLogFileCopyIndex": apLogFileCopyIndex,
       "apLogFileCopyDestination": apLogFileCopyDestination,
       "apLogFileCopyProtocol": apLogFileCopyProtocol,
       "apLogFileCopyServerIP": apLogFileCopyServerIP,
       "apLogFileCopyUserID": apLogFileCopyUserID,
       "apLogFileCopyPassword": apLogFileCopyPassword,
       "apLogFileCopyServerDirectory": apLogFileCopyServerDirectory,
       "apLogFileCopyOperation": apLogFileCopyOperation,
       "apLogFileCopyOperationStatus": apLogFileCopyOperationStatus,
       "apLogFileCopyRowStatus": apLogFileCopyRowStatus,
       "dnsObjects": dnsObjects,
       "primaryDNS": primaryDNS,
       "secondaryDNS": secondaryDNS,
       "tertiaryDNS": tertiaryDNS,
       "mgmtPortObjects": mgmtPortObjects,
       "mgmtPortIfIndex": mgmtPortIfIndex,
       "mgmtPortHostname": mgmtPortHostname,
       "mgmtPortDomain": mgmtPortDomain,
       "physicalPortObjects": physicalPortObjects,
       "physicalPortCount": physicalPortCount,
       "physicalPortsTable": physicalPortsTable,
       "physicalPortsEntry": physicalPortsEntry,
       "portMgmtTrafficEnable": portMgmtTrafficEnable,
       "portDuplexMode": portDuplexMode,
       "portFunction": portFunction,
       "portEnabled": portEnabled,
       "portName": portName,
       "portIpAddress": portIpAddress,
       "portMask": portMask,
       "portMacAddress": portMacAddress,
       "portVlanID": portVlanID,
       "portDHCPEnable": portDHCPEnable,
       "portDHCPGateway": portDHCPGateway,
       "portDHCPDomain": portDHCPDomain,
       "portDHCPDefaultLease": portDHCPDefaultLease,
       "portDHCPMaxLease": portDHCPMaxLease,
       "portDHCPDnsServers": portDHCPDnsServers,
       "portDHCPWins": portDHCPWins,
       "physicalPortsInternalVlanID": physicalPortsInternalVlanID,
       "physicalFlash": physicalFlash,
       "phyDHCPRangeTable": phyDHCPRangeTable,
       "phyDHCPRangeEntry": phyDHCPRangeEntry,
       "phyDHCPRangeIndex": phyDHCPRangeIndex,
       "phyDHCPRangeStart": phyDHCPRangeStart,
       "phyDHCPRangeEnd": phyDHCPRangeEnd,
       "phyDHCPRangeType": phyDHCPRangeType,
       "phyDHCPRangeStatus": phyDHCPRangeStatus,
       "layerTwoPortTable": layerTwoPortTable,
       "layerTwoPortEntry": layerTwoPortEntry,
       "layerTwoPortName": layerTwoPortName,
       "layerTwoPortMgmtState": layerTwoPortMgmtState,
       "layerTwoPortMacAddress": layerTwoPortMacAddress,
       "jumboFrames": jumboFrames,
       "vnManagerObjects": vnManagerObjects,
       "vnRole": vnRole,
       "vnIfIndex": vnIfIndex,
       "vnHeartbeatInterval": vnHeartbeatInterval,
       "vnLocalClients": vnLocalClients,
       "vnForeignClients": vnForeignClients,
       "vnTotalClients": vnTotalClients,
       "ntpObjects": ntpObjects,
       "ntpEnabled": ntpEnabled,
       "ntpTimezone": ntpTimezone,
       "ntpTimeServer1": ntpTimeServer1,
       "ntpTimeServer2": ntpTimeServer2,
       "ntpTimeServer3": ntpTimeServer3,
       "ntpServerEnabled": ntpServerEnabled,
       "controllerStats": controllerStats,
       "tunnelsTxRxBytes": tunnelsTxRxBytes,
       "tunnelCount": tunnelCount,
       "tunnelStatsTable": tunnelStatsTable,
       "tunnelStatsEntry": tunnelStatsEntry,
       "tunnelStartIP": tunnelStartIP,
       "tunnelStartHWC": tunnelStartHWC,
       "tunnelEndIP": tunnelEndIP,
       "tunnelEndHWC": tunnelEndHWC,
       "tunnelStatus": tunnelStatus,
       "tunnelStatsTxBytes": tunnelStatsTxBytes,
       "tunnelStatsRxBytes": tunnelStatsRxBytes,
       "tunnelStatsTxRxBytes": tunnelStatsTxRxBytes,
       "clearAccessRejectMsg": clearAccessRejectMsg,
       "accessRejectMsgTable": accessRejectMsgTable,
       "accessRejectMsgEntry": accessRejectMsgEntry,
       "armIndex": armIndex,
       "armCount": armCount,
       "armReplyMessage": armReplyMessage,
       "availability": availability,
       "availabilityStatus": availabilityStatus,
       "pairIPAddress": pairIPAddress,
       "hwcAvailabilityRank": hwcAvailabilityRank,
       "fastFailover": fastFailover,
       "detectLinkFailure": detectLinkFailure,
       "synchronizeSystemConfig": synchronizeSystemConfig,
       "synchronizeGuestPort": synchronizeGuestPort,
       "secureConnection": secureConnection,
       "weakCipherEnable": weakCipherEnable,
       "dashboard": dashboard,
       "licensingInformation": licensingInformation,
       "licenseRegulatoryDomain": licenseRegulatoryDomain,
       "licenseType": licenseType,
       "licenseDaysRemaining": licenseDaysRemaining,
       "licenseAvailableAP": licenseAvailableAP,
       "licenseInServiceRadarAP": licenseInServiceRadarAP,
       "licenseMode": licenseMode,
       "licenseLocalAP": licenseLocalAP,
       "licenseForeignAP": licenseForeignAP,
       "licenseLocalRadarAP": licenseLocalRadarAP,
       "licenseForeignRadarAP": licenseForeignRadarAP,
       "stationsByProtocol": stationsByProtocol,
       "stationsByProtocolA": stationsByProtocolA,
       "stationsByProtocolB": stationsByProtocolB,
       "stationsByProtocolG": stationsByProtocolG,
       "stationsByProtocolN24": stationsByProtocolN24,
       "stationsByProtocolN5": stationsByProtocolN5,
       "stationsByProtocolUnavailable": stationsByProtocolUnavailable,
       "stationsByProtocolError": stationsByProtocolError,
       "stationsByProtocolAC": stationsByProtocolAC,
       "apByChannelTable": apByChannelTable,
       "apByChannelEntry": apByChannelEntry,
       "apByChannelNumber": apByChannelNumber,
       "apByChannelAPs": apByChannelAPs,
       "virtualNetworks": virtualNetworks,
       "vnsConfigObjects": vnsConfigObjects,
       "vnsCount": vnsCount,
       "vnsConfigTable": vnsConfigTable,
       "vnsConfigEntry": vnsConfigEntry,
       "vnsDescription": vnsDescription,
       "vnsAssignmentMode": vnsAssignmentMode,
       "vnsMUSessionTimeout": vnsMUSessionTimeout,
       "vnsAllowMulticast": vnsAllowMulticast,
       "vnsSSID": vnsSSID,
       "vnsDomain": vnsDomain,
       "vnsDNSServers": vnsDNSServers,
       "vnsWINSServers": vnsWINSServers,
       "vnsAuthModel": vnsAuthModel,
       "vnsParentIfIndex": vnsParentIfIndex,
       "vnsMgmtTrafficEnable": vnsMgmtTrafficEnable,
       "vnsUseDHCPRelay": vnsUseDHCPRelay,
       "vns3rdPartyAP": vns3rdPartyAP,
       "vnsStatus": vnsStatus,
       "vnsMode": vnsMode,
       "vnsVlanID": vnsVlanID,
       "vnsInterfaceName": vnsInterfaceName,
       "vnsMgmIpAddress": vnsMgmIpAddress,
       "vnsSuppressSSID": vnsSuppressSSID,
       "vnsEnable11hSupport": vnsEnable11hSupport,
       "vnsApplyPowerBackOff": vnsApplyPowerBackOff,
       "vnsProcessClientIEReq": vnsProcessClientIEReq,
       "vnsDLSSupportEnable": vnsDLSSupportEnable,
       "vnsDLSAddress": vnsDLSAddress,
       "vnsDLSPort": vnsDLSPort,
       "vnsRateControlProfile": vnsRateControlProfile,
       "vnsSessionAvailabilityEnable": vnsSessionAvailabilityEnable,
       "vnsEnabled": vnsEnabled,
       "vnsStrictSubnetAdherence": vnsStrictSubnetAdherence,
       "vnsSLPEnabled": vnsSLPEnabled,
       "vnsConfigWLANID": vnsConfigWLANID,
       "vnsDHCPRangeTable": vnsDHCPRangeTable,
       "vnsDHCPRangeEntry": vnsDHCPRangeEntry,
       "vnsDHCPRangeIndex": vnsDHCPRangeIndex,
       "vnsDHCPRangeStart": vnsDHCPRangeStart,
       "vnsDHCPRangeEnd": vnsDHCPRangeEnd,
       "vnsDHCPRangeType": vnsDHCPRangeType,
       "vnsDHCPRangeStatus": vnsDHCPRangeStatus,
       "vnsCaptivePortalTable": vnsCaptivePortalTable,
       "vnsCaptivePortalEntry": vnsCaptivePortalEntry,
       "cpURL": cpURL,
       "cpLoginLabel": cpLoginLabel,
       "cpPasswordLabel": cpPasswordLabel,
       "cpHeaderURL": cpHeaderURL,
       "cpFooterURL": cpFooterURL,
       "cpMessage": cpMessage,
       "cpReplaceGatewayWithFQDN": cpReplaceGatewayWithFQDN,
       "cpDefaultRedirectionURL": cpDefaultRedirectionURL,
       "cpConnectionIP": cpConnectionIP,
       "cpConnectionPort": cpConnectionPort,
       "cpSharedSecret": cpSharedSecret,
       "cpLogOff": cpLogOff,
       "cpStatusCheck": cpStatusCheck,
       "cpType": cpType,
       "vnsRadiusServerTable": vnsRadiusServerTable,
       "vnsRadiusServerEntry": vnsRadiusServerEntry,
       "vnsRadiusServerName": vnsRadiusServerName,
       "vnsRadiusServerPort": vnsRadiusServerPort,
       "vnsRadiusServerRetries": vnsRadiusServerRetries,
       "vnsRadiusServerTimeout": vnsRadiusServerTimeout,
       "vnsRadiusServerSharedSecret": vnsRadiusServerSharedSecret,
       "vnsRadiusServerNASIdentifier": vnsRadiusServerNASIdentifier,
       "vnsRadiusServerAuthType": vnsRadiusServerAuthType,
       "vnsRadiusServerRowStatus": vnsRadiusServerRowStatus,
       "vnsRadiusServerNasAddress": vnsRadiusServerNasAddress,
       "vnsFilterIDTable": vnsFilterIDTable,
       "vnsFilterIDEntry": vnsFilterIDEntry,
       "vnsFilterID": vnsFilterID,
       "vnsFilterIDStatus": vnsFilterIDStatus,
       "vnsFilterRuleTable": vnsFilterRuleTable,
       "vnsFilterRuleEntry": vnsFilterRuleEntry,
       "vnsFilterRuleOrder": vnsFilterRuleOrder,
       "vnsFilterRuleDirection": vnsFilterRuleDirection,
       "vnsFilterRuleAction": vnsFilterRuleAction,
       "vnsFilterRuleIPAddress": vnsFilterRuleIPAddress,
       "vnsFilterRulePortLow": vnsFilterRulePortLow,
       "vnsFilterRulePortHigh": vnsFilterRulePortHigh,
       "vnsFilterRuleProtocol": vnsFilterRuleProtocol,
       "vnsFilterRuleEtherType": vnsFilterRuleEtherType,
       "vnsFilterRuleStatus": vnsFilterRuleStatus,
       "vnsPrivacyTable": vnsPrivacyTable,
       "vnsPrivacyEntry": vnsPrivacyEntry,
       "vnsPrivWEPKeyType": vnsPrivWEPKeyType,
       "vnsPrivDynamicRekeyFrequency": vnsPrivDynamicRekeyFrequency,
       "vnsPrivWEPKeyLength": vnsPrivWEPKeyLength,
       "vnsPrivWPA1Enabled": vnsPrivWPA1Enabled,
       "vnsPrivUseSharedKey": vnsPrivUseSharedKey,
       "vnsPrivWPASharedKey": vnsPrivWPASharedKey,
       "vnsPrivWPA2Enabled": vnsPrivWPA2Enabled,
       "vnsWEPKeyTable": vnsWEPKeyTable,
       "vnsWEPKeyEntry": vnsWEPKeyEntry,
       "vnsWEPKeyIndex": vnsWEPKeyIndex,
       "vnsWEPKeyValue": vnsWEPKeyValue,
       "vns3rdPartyAPTable": vns3rdPartyAPTable,
       "vns3rdPartyAPEntry": vns3rdPartyAPEntry,
       "apMacAddress": apMacAddress,
       "apIpAddress": apIpAddress,
       "vnsQoSTable": vnsQoSTable,
       "vnsQoSEntry": vnsQoSEntry,
       "vnsQoSWirelessLegacyFlag": vnsQoSWirelessLegacyFlag,
       "vnsQoSWirelessWMMFlag": vnsQoSWirelessWMMFlag,
       "vnsQoSWireless80211eFlag": vnsQoSWireless80211eFlag,
       "vnsQoSWirelessTurboVoiceFlag": vnsQoSWirelessTurboVoiceFlag,
       "vnsQoSPriorityOverrideFlag": vnsQoSPriorityOverrideFlag,
       "vnsQoSPriorityOverrideSC": vnsQoSPriorityOverrideSC,
       "vnsQoSPriorityOverrideDSCP": vnsQoSPriorityOverrideDSCP,
       "vnsQoSClassificationServiceClass": vnsQoSClassificationServiceClass,
       "vnsQoSWirelessEnableUAPSD": vnsQoSWirelessEnableUAPSD,
       "vnsQoSWirelessUseAdmControlVoice": vnsQoSWirelessUseAdmControlVoice,
       "vnsQoSWirelessUseAdmControlVideo": vnsQoSWirelessUseAdmControlVideo,
       "vnsQoSWirelessULPolicerAction": vnsQoSWirelessULPolicerAction,
       "vnsQoSWirelessDLPolicerAction": vnsQoSWirelessDLPolicerAction,
       "vnsQoSWirelessUseAdmControlBestEffort": vnsQoSWirelessUseAdmControlBestEffort,
       "vnsQoSWirelessUseAdmControlBackground": vnsQoSWirelessUseAdmControlBackground,
       "vnsWDSRFTable": vnsWDSRFTable,
       "vnsWDSRFEntry": vnsWDSRFEntry,
       "vnsWDSRFAPName": vnsWDSRFAPName,
       "vnsWDSRFbgService": vnsWDSRFbgService,
       "vnsWDSRFaService": vnsWDSRFaService,
       "vnsWDSRFPreferredParent": vnsWDSRFPreferredParent,
       "vnsWDSRFBackupParent": vnsWDSRFBackupParent,
       "vnsWDSRFBridge": vnsWDSRFBridge,
       "vnsRateControlProfTable": vnsRateControlProfTable,
       "vnsRateControlProfEntry": vnsRateControlProfEntry,
       "vnsRateControlProfInd": vnsRateControlProfInd,
       "vnsRateControlProfName": vnsRateControlProfName,
       "vnsRateControlCIR": vnsRateControlCIR,
       "vnsRateControlCBS": vnsRateControlCBS,
       "vnsAPFilterTable": vnsAPFilterTable,
       "vnsAPFilterEntry": vnsAPFilterEntry,
       "vnsAPFilterRuleOrder": vnsAPFilterRuleOrder,
       "vnsAPFilterRuleDirection": vnsAPFilterRuleDirection,
       "vnsAPFilterAction": vnsAPFilterAction,
       "vnsAPFilterIPAddress": vnsAPFilterIPAddress,
       "vnsAPFilterMask": vnsAPFilterMask,
       "vnsAPFilterPortLow": vnsAPFilterPortLow,
       "vnsAPFilterPortHigh": vnsAPFilterPortHigh,
       "vnsAPFilterProtocol": vnsAPFilterProtocol,
       "vnsAPFilterEtherType": vnsAPFilterEtherType,
       "vnsAPFilterRowStatus": vnsAPFilterRowStatus,
       "vnsStatsObjects": vnsStatsObjects,
       "activeVNSSessionCount": activeVNSSessionCount,
       "vnsStatTable": vnsStatTable,
       "vnsStatEntry": vnsStatEntry,
       "vnsStatName": vnsStatName,
       "vnsStatTxPkts": vnsStatTxPkts,
       "vnsStatRxPkts": vnsStatRxPkts,
       "vnsStatTxOctects": vnsStatTxOctects,
       "vnsStatRxOctects": vnsStatRxOctects,
       "vnsStatMulticastTxPkts": vnsStatMulticastTxPkts,
       "vnsStatMulticastRxPkts": vnsStatMulticastRxPkts,
       "vnsStatBroadcastTxPkts": vnsStatBroadcastTxPkts,
       "vnsStatBroadcastRxPkts": vnsStatBroadcastRxPkts,
       "vnsStatRadiusTotRequests": vnsStatRadiusTotRequests,
       "vnsStatRadiusReqFailed": vnsStatRadiusReqFailed,
       "vnsStatRadiusReqRejected": vnsStatRadiusReqRejected,
       "vnsExceptionStatTable": vnsExceptionStatTable,
       "vnsExceptionStatEntry": vnsExceptionStatEntry,
       "vnsExceptionFiterName": vnsExceptionFiterName,
       "vnsExceptionStatPktsDenied": vnsExceptionStatPktsDenied,
       "vnsExceptionStatPktsAllowed": vnsExceptionStatPktsAllowed,
       "vnsWDSStatTable": vnsWDSStatTable,
       "vnsWDSStatEntry": vnsWDSStatEntry,
       "vnsWDSStatAPName": vnsWDSStatAPName,
       "vnsWDSStatAPRole": vnsWDSStatAPRole,
       "vnsWDSStatAPRadio": vnsWDSStatAPRadio,
       "vnsWDSStatAPParent": vnsWDSStatAPParent,
       "vnsWDSStatSSID": vnsWDSStatSSID,
       "vnsWDSStatRxFrame": vnsWDSStatRxFrame,
       "vnsWDSStatTxFrame": vnsWDSStatTxFrame,
       "vnsWDSStatRxError": vnsWDSStatRxError,
       "vnsWDSStatTxError": vnsWDSStatTxError,
       "vnsWDSStatRxRSSI": vnsWDSStatRxRSSI,
       "vnsWDSStatRxRate": vnsWDSStatRxRate,
       "vnsWDSStatTxRate": vnsWDSStatTxRate,
       "vnsGlobalSetting": vnsGlobalSetting,
       "wirelessQoS": wirelessQoS,
       "maxVoiceBWforReassociation": maxVoiceBWforReassociation,
       "maxVoiceBWforAssociation": maxVoiceBWforAssociation,
       "maxVideoBWforReassociation": maxVideoBWforReassociation,
       "maxVideoBWforAssociation": maxVideoBWforAssociation,
       "maxBestEffortBWforReassociation": maxBestEffortBWforReassociation,
       "maxBestEffortBWforAssociation": maxBestEffortBWforAssociation,
       "maxBackgroundBWforReassociation": maxBackgroundBWforReassociation,
       "maxBackgroundBWforAssociation": maxBackgroundBWforAssociation,
       "radiusInfo": radiusInfo,
       "externalRadiusServerTable": externalRadiusServerTable,
       "externalRadiusServerEntry": externalRadiusServerEntry,
       "externalRadiusServerName": externalRadiusServerName,
       "externalRadiusServerAddress": externalRadiusServerAddress,
       "externalRadiusServerSharedSecret": externalRadiusServerSharedSecret,
       "externalRadiusServerRowStatus": externalRadiusServerRowStatus,
       "dasInfo": dasInfo,
       "dasPort": dasPort,
       "dasReplayInterval": dasReplayInterval,
       "advancedFilteringMode": advancedFilteringMode,
       "radiusStrictMode": radiusStrictMode,
       "radiusFastFailoverEvents": radiusFastFailoverEvents,
       "radiusFastFailoverEventsTable": radiusFastFailoverEventsTable,
       "radiusFastFailoverEventsEntry": radiusFastFailoverEventsEntry,
       "radiusFFOEid": radiusFFOEid,
       "fastFailoverEvents": fastFailoverEvents,
       "dhcpRelayListeners": dhcpRelayListeners,
       "dhcpRelayListenersMaxEntries": dhcpRelayListenersMaxEntries,
       "dhcpRelayListenersNumEntries": dhcpRelayListenersNumEntries,
       "dhcpRelayListenersNextIndex": dhcpRelayListenersNextIndex,
       "dhcpRelayListenersTable": dhcpRelayListenersTable,
       "dhcpRelayListenersEntry": dhcpRelayListenersEntry,
       "dhcpRelayListenersID": dhcpRelayListenersID,
       "dhcpRelayListenersRowStatus": dhcpRelayListenersRowStatus,
       "destinationName": destinationName,
       "destinationIP": destinationIP,
       "clientAutologinOption": clientAutologinOption,
       "authenticationAdvanced": authenticationAdvanced,
       "includeServiceType": includeServiceType,
       "clientMessageDelayTime": clientMessageDelayTime,
       "radiusAccounting": radiusAccounting,
       "serverUsageModel": serverUsageModel,
       "radacctStartOnIPAddr": radacctStartOnIPAddr,
       "clientServiceTypeLogin": clientServiceTypeLogin,
       "applyMacAddressFormat": applyMacAddressFormat,
       "radiusExtnsSetting": radiusExtnsSetting,
       "radiusExtnsSettingTable": radiusExtnsSettingTable,
       "radiusExtnsSettingEntry": radiusExtnsSettingEntry,
       "radiusExtnsIndex": radiusExtnsIndex,
       "pollingMechanism": pollingMechanism,
       "serverPollingInterval": serverPollingInterval,
       "netflowAndMirrorN": netflowAndMirrorN,
       "netflowDestinationIP": netflowDestinationIP,
       "netflowInterval": netflowInterval,
       "mirrorFirstN": mirrorFirstN,
       "mirrorL2Ports": mirrorL2Ports,
       "radiusMacAddressFormatOption": radiusMacAddressFormatOption,
       "wlan": wlan,
       "wlanMaxEntries": wlanMaxEntries,
       "wlanNumEntries": wlanNumEntries,
       "wlanTableNextAvailableIndex": wlanTableNextAvailableIndex,
       "wlanTable": wlanTable,
       "wlanEntry": wlanEntry,
       "wlanID": wlanID,
       "wlanRowStatus": wlanRowStatus,
       "wlanServiceType": wlanServiceType,
       "wlanName": wlanName,
       "wlanSSID": wlanSSID,
       "wlanSynchronize": wlanSynchronize,
       "wlanEnabled": wlanEnabled,
       "wlanDefaultTopologyID": wlanDefaultTopologyID,
       "wlanSessionTimeout": wlanSessionTimeout,
       "wlanIdleTimeoutPreAuth": wlanIdleTimeoutPreAuth,
       "wlanIdleSessionPostAuth": wlanIdleSessionPostAuth,
       "wlanSupressSSID": wlanSupressSSID,
       "wlanDot11hSupport": wlanDot11hSupport,
       "wlanDot11hClientPowerReduction": wlanDot11hClientPowerReduction,
       "wlanProcessClientIE": wlanProcessClientIE,
       "wlanEngerySaveMode": wlanEngerySaveMode,
       "wlanBlockMuToMuTraffic": wlanBlockMuToMuTraffic,
       "wlanRemoteable": wlanRemoteable,
       "wlanVNSID": wlanVNSID,
       "wlanRadioManagement11k": wlanRadioManagement11k,
       "wlanBeaconReport": wlanBeaconReport,
       "wlanQuietIE": wlanQuietIE,
       "wlanMirrorN": wlanMirrorN,
       "wlanNetFlow": wlanNetFlow,
       "wlanAppVisibility": wlanAppVisibility,
       "wlanStatsTable": wlanStatsTable,
       "wlanStatsEntry": wlanStatsEntry,
       "wlanStatsID": wlanStatsID,
       "wlanStatsAssociatedClients": wlanStatsAssociatedClients,
       "wlanStatsRadiusTotRequests": wlanStatsRadiusTotRequests,
       "wlanStatsRadiusReqFailed": wlanStatsRadiusReqFailed,
       "wlanStatsRadiusReqRejected": wlanStatsRadiusReqRejected,
       "wlanPrivTable": wlanPrivTable,
       "wlanPrivEntry": wlanPrivEntry,
       "wlanPrivPrivacyType": wlanPrivPrivacyType,
       "wlanPrivWEPKeyIndex": wlanPrivWEPKeyIndex,
       "wlanPrivWEPKeyLength": wlanPrivWEPKeyLength,
       "wlanPrivWEPKey": wlanPrivWEPKey,
       "wlanPrivWPAv1EncryptionType": wlanPrivWPAv1EncryptionType,
       "wlanPrivWPAv2EncryptionType": wlanPrivWPAv2EncryptionType,
       "wlanPrivKeyManagement": wlanPrivKeyManagement,
       "wlanPrivBroadcastRekeying": wlanPrivBroadcastRekeying,
       "wlanPrivRekeyInterval": wlanPrivRekeyInterval,
       "wlanPrivGroupKPSR": wlanPrivGroupKPSR,
       "wlanPrivWPAPSK": wlanPrivWPAPSK,
       "wlanPrivWPAversion": wlanPrivWPAversion,
       "wlanPrivfastTransition": wlanPrivfastTransition,
       "wlanPrivManagementFrameProtection": wlanPrivManagementFrameProtection,
       "wlanAuthTable": wlanAuthTable,
       "wlanAuthEntry": wlanAuthEntry,
       "wlanAuthType": wlanAuthType,
       "wlanAuthMacBasedAuth": wlanAuthMacBasedAuth,
       "wlanAuthMACBasedAuthOnRoam": wlanAuthMACBasedAuthOnRoam,
       "wlanAuthAutoAuthAuthorizedUser": wlanAuthAutoAuthAuthorizedUser,
       "wlanAuthAllowUnauthorizedUser": wlanAuthAllowUnauthorizedUser,
       "wlanAuthRadiusIncludeAP": wlanAuthRadiusIncludeAP,
       "wlanAuthRadiusIncludeVNS": wlanAuthRadiusIncludeVNS,
       "wlanAuthRadiusIncludeSSID": wlanAuthRadiusIncludeSSID,
       "wlanAuthRadiusIncludePolicy": wlanAuthRadiusIncludePolicy,
       "wlanAuthRadiusIncludeTopology": wlanAuthRadiusIncludeTopology,
       "wlanAuthRadiusIncludeIngressRC": wlanAuthRadiusIncludeIngressRC,
       "wlanAuthRadiusIncludeEgressRC": wlanAuthRadiusIncludeEgressRC,
       "wlanAuthCollectAcctInformation": wlanAuthCollectAcctInformation,
       "wlanAuthReplaceCalledStationIDWithZone": wlanAuthReplaceCalledStationIDWithZone,
       "wlanAuthRadiusAcctAfterMacBaseAuthorization": wlanAuthRadiusAcctAfterMacBaseAuthorization,
       "wlanAuthRadiusTimeoutRole": wlanAuthRadiusTimeoutRole,
       "wlanAuthRadiusOperatorNameSpace": wlanAuthRadiusOperatorNameSpace,
       "wlanAuthRadiusOperatorName": wlanAuthRadiusOperatorName,
       "wlanAuthMACBasedAuthReAuthOnAreaRoam": wlanAuthMACBasedAuthReAuthOnAreaRoam,
       "wlanRadiusTable": wlanRadiusTable,
       "wlanRadiusEntry": wlanRadiusEntry,
       "wlanRadiusIndex": wlanRadiusIndex,
       "wlanRadiusName": wlanRadiusName,
       "wlanRadiusUsage": wlanRadiusUsage,
       "wlanRadiusPriority": wlanRadiusPriority,
       "wlanRadiusPort": wlanRadiusPort,
       "wlanRadiusRetries": wlanRadiusRetries,
       "wlanRadiusTimeout": wlanRadiusTimeout,
       "wlanRadiusNASUseVnsIP": wlanRadiusNASUseVnsIP,
       "wlanRadiusNASIP": wlanRadiusNASIP,
       "wlanRadiusNASIDUseVNSName": wlanRadiusNASIDUseVNSName,
       "wlanRadiusNASID": wlanRadiusNASID,
       "wlanRadiusAuthType": wlanRadiusAuthType,
       "wlanCPTable": wlanCPTable,
       "wlanCPEntry": wlanCPEntry,
       "wlanCPAuthType": wlanCPAuthType,
       "wlanCP802HttpRedirect": wlanCP802HttpRedirect,
       "wlanCPExtConnection": wlanCPExtConnection,
       "wlanCPExtPort": wlanCPExtPort,
       "wlanCPExtEnableHttps": wlanCPExtEnableHttps,
       "wlanCPExtEncryption": wlanCPExtEncryption,
       "wlanCPExtSharedSecret": wlanCPExtSharedSecret,
       "wlanCPExtTosOverride": wlanCPExtTosOverride,
       "wlanCPExtTosValue": wlanCPExtTosValue,
       "wlanCPExtAddIPtoURL": wlanCPExtAddIPtoURL,
       "wlanCPIntLogoffButton": wlanCPIntLogoffButton,
       "wlanCPIntStatusCheckButton": wlanCPIntStatusCheckButton,
       "wlanCPReplaceIPwithFQDN": wlanCPReplaceIPwithFQDN,
       "wlanCPSendLoginTo": wlanCPSendLoginTo,
       "wlanCPRedirectURL": wlanCPRedirectURL,
       "wlanCPGuestAccLifetime": wlanCPGuestAccLifetime,
       "wlanCPGuestAllowedLifetimeAcct": wlanCPGuestAllowedLifetimeAcct,
       "wlanCPGuestSessionLifetime": wlanCPGuestSessionLifetime,
       "wlanCPGuestIDPrefix": wlanCPGuestIDPrefix,
       "wlanCPGuestMinPassLength": wlanCPGuestMinPassLength,
       "wlanCPGuestMaxConcurrentSession": wlanCPGuestMaxConcurrentSession,
       "wlanCPUseHTTPSforConnection": wlanCPUseHTTPSforConnection,
       "wlanCPIdentity": wlanCPIdentity,
       "wlanCPCustomSpecificURL": wlanCPCustomSpecificURL,
       "wlanCPSelectionOption": wlanCPSelectionOption,
       "wlanUnsecuredWlanCounts": wlanUnsecuredWlanCounts,
       "wlanSecurityReportTable": wlanSecurityReportTable,
       "wlanSecurityReportEntry": wlanSecurityReportEntry,
       "wlanSecurityReportFlag": wlanSecurityReportFlag,
       "wlanSecurityReportUnsecureType": wlanSecurityReportUnsecureType,
       "wlanSecurityReportNotes": wlanSecurityReportNotes,
       "wlanRadiusServerTable": wlanRadiusServerTable,
       "wlanRadiusServerEntry": wlanRadiusServerEntry,
       "radiusId": radiusId,
       "wlanRadiusServerName": wlanRadiusServerName,
       "wlanRadiusServerUse": wlanRadiusServerUse,
       "wlanRadiusServerUsage": wlanRadiusServerUsage,
       "wlanRadiusServerAuthUseVNSIPAddr": wlanRadiusServerAuthUseVNSIPAddr,
       "wlanRadiusServerAuthNASIP": wlanRadiusServerAuthNASIP,
       "wlanRadiusServerAuthUseVNSName": wlanRadiusServerAuthUseVNSName,
       "wlanRadiusServerAuthNASId": wlanRadiusServerAuthNASId,
       "wlanRadiusServerAuthAuthType": wlanRadiusServerAuthAuthType,
       "wlanRadiusServerAcctUseVNSIPAddr": wlanRadiusServerAcctUseVNSIPAddr,
       "wlanRadiusServerAcctNASIP": wlanRadiusServerAcctNASIP,
       "wlanRadiusServerAcctUseVNSName": wlanRadiusServerAcctUseVNSName,
       "wlanRadiusServerAcctNASId": wlanRadiusServerAcctNASId,
       "wlanRadiusServerAcctSIAR": wlanRadiusServerAcctSIAR,
       "wlanRadiusServerMacUseVNSIPAddr": wlanRadiusServerMacUseVNSIPAddr,
       "wlanRadiusServerMacNASIP": wlanRadiusServerMacNASIP,
       "wlanRadiusServerMacUseVNSName": wlanRadiusServerMacUseVNSName,
       "wlanRadiusServerMacNASId": wlanRadiusServerMacNASId,
       "wlanRadiusServerMacAuthType": wlanRadiusServerMacAuthType,
       "wlanRadiusServerMacPW": wlanRadiusServerMacPW,
       "topology": topology,
       "topologyConfig": topologyConfig,
       "topologyTable": topologyTable,
       "topologyEntry": topologyEntry,
       "topologyID": topologyID,
       "topologyName": topologyName,
       "topologyMode": topologyMode,
       "topologyTagged": topologyTagged,
       "topologyVlanID": topologyVlanID,
       "topologyEgressPort": topologyEgressPort,
       "topologyLayer3": topologyLayer3,
       "topologyIPAddress": topologyIPAddress,
       "topologyIPMask": topologyIPMask,
       "topologyMTUsize": topologyMTUsize,
       "topologyGateway": topologyGateway,
       "topologyDHCPUsage": topologyDHCPUsage,
       "topologyAPRegistration": topologyAPRegistration,
       "topologyManagementTraffic": topologyManagementTraffic,
       "topologySynchronize": topologySynchronize,
       "topologySyncGateway": topologySyncGateway,
       "topologySyncMask": topologySyncMask,
       "topologySyncIPStart": topologySyncIPStart,
       "topologySyncIPEnd": topologySyncIPEnd,
       "topologyStaticIPv6Address": topologyStaticIPv6Address,
       "topologyLinkLocalIPv6Address": topologyLinkLocalIPv6Address,
       "topologyPreFixLength": topologyPreFixLength,
       "topologyIPv6Gateway": topologyIPv6Gateway,
       "topologyDynamicEgress": topologyDynamicEgress,
       "topologyIsGroup": topologyIsGroup,
       "topologyGroupMembers": topologyGroupMembers,
       "topologyMemberId": topologyMemberId,
       "topologyStat": topologyStat,
       "topoStatTable": topoStatTable,
       "topoStatEntry": topoStatEntry,
       "topoStatName": topoStatName,
       "topoStatTxPkts": topoStatTxPkts,
       "topoStatRxPkts": topoStatRxPkts,
       "topoStatTxOctets": topoStatTxOctets,
       "topoStatRxOctets": topoStatRxOctets,
       "topoStatMulticastTxPkts": topoStatMulticastTxPkts,
       "topoStatMulticastRxPkts": topoStatMulticastRxPkts,
       "topoStatBroadcastTxPkts": topoStatBroadcastTxPkts,
       "topoStatBroadcastRxPkts": topoStatBroadcastRxPkts,
       "topoStatFrameChkSeqErrors": topoStatFrameChkSeqErrors,
       "topoStatFrameTooLongErrors": topoStatFrameTooLongErrors,
       "topoExceptionStatTable": topoExceptionStatTable,
       "topoExceptionStatEntry": topoExceptionStatEntry,
       "topoExceptionFiterName": topoExceptionFiterName,
       "topoExceptionStatPktsDenied": topoExceptionStatPktsDenied,
       "topoExceptionStatPktsAllowed": topoExceptionStatPktsAllowed,
       "topoWireStatTable": topoWireStatTable,
       "topoWireStatEntry": topoWireStatEntry,
       "topoWireStatName": topoWireStatName,
       "topoWireStatTxPkts": topoWireStatTxPkts,
       "topoWireStatRxPkts": topoWireStatRxPkts,
       "topoWireStatTxOctets": topoWireStatTxOctets,
       "topoWireStatRxOctets": topoWireStatRxOctets,
       "topoWireStatMulticastTxPkts": topoWireStatMulticastTxPkts,
       "topoWireStatMulticastRxPkts": topoWireStatMulticastRxPkts,
       "topoWireStatBroadcastTxPkts": topoWireStatBroadcastTxPkts,
       "topoWireStatBroadcastRxPkts": topoWireStatBroadcastRxPkts,
       "topoWireStatFrameChkSeqErrors": topoWireStatFrameChkSeqErrors,
       "topoWireStatFrameTooLongErrors": topoWireStatFrameTooLongErrors,
       "topoCompleteStatTable": topoCompleteStatTable,
       "topoCompleteStatEntry": topoCompleteStatEntry,
       "topoCompleteStatName": topoCompleteStatName,
       "topoCompleteStatTxPkts": topoCompleteStatTxPkts,
       "topoCompleteStatRxPkts": topoCompleteStatRxPkts,
       "topoCompleteStatTxOctets": topoCompleteStatTxOctets,
       "topoCompleteStatRxOctets": topoCompleteStatRxOctets,
       "topoCompleteStatMulticastTxPkts": topoCompleteStatMulticastTxPkts,
       "topoCompleteStatMulticastRxPkts": topoCompleteStatMulticastRxPkts,
       "topoCompleteStatBroadcastTxPkts": topoCompleteStatBroadcastTxPkts,
       "topoCompleteStatBroadcastRxPkts": topoCompleteStatBroadcastRxPkts,
       "topoCompleteStatFrameChkSeqErrors": topoCompleteStatFrameChkSeqErrors,
       "topoCompleteStatFrameTooLongErrors": topoCompleteStatFrameTooLongErrors,
       "accessPoints": accessPoints,
       "apConfigObjects": apConfigObjects,
       "apCount": apCount,
       "apTable": apTable,
       "apEntry": apEntry,
       "apIndex": apIndex,
       "apName": apName,
       "apDesc": apDesc,
       "apSerialNumber": apSerialNumber,
       "apPortifIndex": apPortifIndex,
       "apWiredIfIndex": apWiredIfIndex,
       "apSoftwareVersion": apSoftwareVersion,
       "apSpecific": apSpecific,
       "apBroadcastDisassociate": apBroadcastDisassociate,
       "apRowStatus": apRowStatus,
       "apVlanID": apVlanID,
       "apIpAssignmentType": apIpAssignmentType,
       "apIfMAC": apIfMAC,
       "apIPAddress": apIPAddress,
       "apHwVersion": apHwVersion,
       "apSwVersion": apSwVersion,
       "apEnvironment": apEnvironment,
       "apHome": apHome,
       "apRole": apRole,
       "apState": apState,
       "apStatus": apStatus,
       "apPollTimeout": apPollTimeout,
       "apPollInterval": apPollInterval,
       "apTelnetAccess": apTelnetAccess,
       "apMaintainClientSession": apMaintainClientSession,
       "apRestartServiceContAbsent": apRestartServiceContAbsent,
       "apHostname": apHostname,
       "apLocation": apLocation,
       "apStaticMTUsize": apStaticMTUsize,
       "apSiteID": apSiteID,
       "apZone": apZone,
       "apLLDP": apLLDP,
       "apSSHAccess": apSSHAccess,
       "apLEDMode": apLEDMode,
       "apLocationbasedService": apLocationbasedService,
       "apSecureTunnel": apSecureTunnel,
       "apEncryptCntTraffic": apEncryptCntTraffic,
       "apMICErrorWarning": apMICErrorWarning,
       "apSecureDataTunnelType": apSecureDataTunnelType,
       "apIPMulticastAssembly": apIPMulticastAssembly,
       "apSSHConnection": apSSHConnection,
       "apRadioTable": apRadioTable,
       "apRadioEntry": apRadioEntry,
       "apRadioFrequency": apRadioFrequency,
       "apRadioNumber": apRadioNumber,
       "apRadioType": apRadioType,
       "apRadioProtocol": apRadioProtocol,
       "radioVNSTable": radioVNSTable,
       "radioVNSEntry": radioVNSEntry,
       "radioIfIndex": radioIfIndex,
       "vnsIfIndex": vnsIfIndex,
       "radioVNSRowStatus": radioVNSRowStatus,
       "apFastFailoverEnable": apFastFailoverEnable,
       "apLinkTimeout": apLinkTimeout,
       "apAntennaTable": apAntennaTable,
       "apAntennaEntry": apAntennaEntry,
       "apAntennaIndex": apAntennaIndex,
       "apAntennanName": apAntennanName,
       "apAntennaType": apAntennaType,
       "apRadioAntennaTable": apRadioAntennaTable,
       "apRadioAntennaEntry": apRadioAntennaEntry,
       "apRadioAntennaType": apRadioAntennaType,
       "apRadioAntennaModel": apRadioAntennaModel,
       "apRadioAttenuation": apRadioAttenuation,
       "apStatsObjects": apStatsObjects,
       "apActiveCount": apActiveCount,
       "apStatsTable": apStatsTable,
       "apStatsEntry": apStatsEntry,
       "apInUcastPkts": apInUcastPkts,
       "apInNUcastPkts": apInNUcastPkts,
       "apInOctets": apInOctets,
       "apInErrors": apInErrors,
       "apInDiscards": apInDiscards,
       "apOutUcastPkts": apOutUcastPkts,
       "apOutNUcastPkts": apOutNUcastPkts,
       "apOutOctets": apOutOctets,
       "apOutErrors": apOutErrors,
       "apOutDiscards": apOutDiscards,
       "apUpTime": apUpTime,
       "apCredentialType": apCredentialType,
       "apCertificateExpiry": apCertificateExpiry,
       "apStatsMuCounts": apStatsMuCounts,
       "apStatsSessionDuration": apStatsSessionDuration,
       "apTotalStationsA": apTotalStationsA,
       "apTotalStationsB": apTotalStationsB,
       "apTotalStationsG": apTotalStationsG,
       "apTotalStationsN50": apTotalStationsN50,
       "apTotalStationsN24": apTotalStationsN24,
       "apInvalidPolicyCount": apInvalidPolicyCount,
       "apInterfaceMTU": apInterfaceMTU,
       "apEffectiveTunnelMTU": apEffectiveTunnelMTU,
       "apTotalStationsAC": apTotalStationsAC,
       "apTotalStationsAInOctets": apTotalStationsAInOctets,
       "apTotalStationsAOutOctets": apTotalStationsAOutOctets,
       "apTotalStationsBInOctets": apTotalStationsBInOctets,
       "apTotalStationsBOutOctets": apTotalStationsBOutOctets,
       "apTotalStationsGInOctets": apTotalStationsGInOctets,
       "apTotalStationsGOutOctets": apTotalStationsGOutOctets,
       "apTotalStationsN50InOctets": apTotalStationsN50InOctets,
       "apTotalStationsN50OutOctets": apTotalStationsN50OutOctets,
       "apTotalStationsN24InOctets": apTotalStationsN24InOctets,
       "apTotalStationsN24OutOctets": apTotalStationsN24OutOctets,
       "apTotalStationsACInOctets": apTotalStationsACInOctets,
       "apTotalStationsACOutOctets": apTotalStationsACOutOctets,
       "apRegistrationRequests": apRegistrationRequests,
       "apRadioStatusTable": apRadioStatusTable,
       "apRadioStatusEntry": apRadioStatusEntry,
       "apRadioStatusChannel": apRadioStatusChannel,
       "apRadioStatusChannelWidth": apRadioStatusChannelWidth,
       "apRadioStatusChannelOffset": apRadioStatusChannelOffset,
       "apPerformanceReportByRadioTable": apPerformanceReportByRadioTable,
       "apPerformanceReportByRadioEntry": apPerformanceReportByRadioEntry,
       "apRadioIndex": apRadioIndex,
       "apPerfRadioPrevPeakChannelUtilization": apPerfRadioPrevPeakChannelUtilization,
       "apPerfRadioCurPeakChannelUtilization": apPerfRadioCurPeakChannelUtilization,
       "apPerfRadioAverageChannelUtilization": apPerfRadioAverageChannelUtilization,
       "apPerfRadioCurrentChannelUtilization": apPerfRadioCurrentChannelUtilization,
       "apPerfRadioPrevPeakRSS": apPerfRadioPrevPeakRSS,
       "apPerfRadioCurPeakRSS": apPerfRadioCurPeakRSS,
       "apPerfRadioAverageRSS": apPerfRadioAverageRSS,
       "apPerfRadioCurrentRSS": apPerfRadioCurrentRSS,
       "apPerfRadioPrevPeakSNR": apPerfRadioPrevPeakSNR,
       "apPerfRadioCurPeakSNR": apPerfRadioCurPeakSNR,
       "apPerfRadioAverageSNR": apPerfRadioAverageSNR,
       "apPerfRadioCurrentSNR": apPerfRadioCurrentSNR,
       "apPerfRadioPrevPeakPktRetx": apPerfRadioPrevPeakPktRetx,
       "apPerfRadioCurPeakPktRetx": apPerfRadioCurPeakPktRetx,
       "apPerfRadioAveragePktRetx": apPerfRadioAveragePktRetx,
       "apPerfRadioCurrentPktRetx": apPerfRadioCurrentPktRetx,
       "apPerfRadioPktRetx": apPerfRadioPktRetx,
       "apAccessibilityTable": apAccessibilityTable,
       "apAccessibilityEntry": apAccessibilityEntry,
       "apAccPrevPeakAssocReqRx": apAccPrevPeakAssocReqRx,
       "apAccCurPeakAssocReqRx": apAccCurPeakAssocReqRx,
       "apAccAverageAssocReqRx": apAccAverageAssocReqRx,
       "apAccCurrentAssocReqRx": apAccCurrentAssocReqRx,
       "apAccAssocReqRx": apAccAssocReqRx,
       "apAccPrevPeakReassocReqRx": apAccPrevPeakReassocReqRx,
       "apAccCurPeakReassocReqRx": apAccCurPeakReassocReqRx,
       "apAccAverageReassocReqRx": apAccAverageReassocReqRx,
       "apAccCurrentReassocReqRx": apAccCurrentReassocReqRx,
       "apAccReassocReqRx": apAccReassocReqRx,
       "apAccPrevPeakDisassocDeauthReqTx": apAccPrevPeakDisassocDeauthReqTx,
       "apAccCurPeakDisassocDeauthReqTx": apAccCurPeakDisassocDeauthReqTx,
       "apAccAverageDisassocDeauthReqTx": apAccAverageDisassocDeauthReqTx,
       "apAccCurrentDisassocDeauthReqTx": apAccCurrentDisassocDeauthReqTx,
       "apAccDisassocDeauthReqTx": apAccDisassocDeauthReqTx,
       "apAccPrevPeakDisassocDeauthReqRx": apAccPrevPeakDisassocDeauthReqRx,
       "apAccCurPeakDisassocDeauthReqRx": apAccCurPeakDisassocDeauthReqRx,
       "apAccAverageDisassocDeauthReqRx": apAccAverageDisassocDeauthReqRx,
       "apAccCurrentDisassocDeauthReqRx": apAccCurrentDisassocDeauthReqRx,
       "apAccDisassocDeauthReqRx": apAccDisassocDeauthReqRx,
       "apPerformanceReportbyRadioAndWlanTable": apPerformanceReportbyRadioAndWlanTable,
       "apPerformanceReportbyRadioAndWlanEntry": apPerformanceReportbyRadioAndWlanEntry,
       "apPerfWlanPrevPeakClientsPerSec": apPerfWlanPrevPeakClientsPerSec,
       "apPerfWlanCurPeakClientsPerSec": apPerfWlanCurPeakClientsPerSec,
       "apPerfWlanAverageClientsPerSec": apPerfWlanAverageClientsPerSec,
       "apPerfWlanCurrentClientsPerSec": apPerfWlanCurrentClientsPerSec,
       "apPerfWlanPrevPeakULOctetsPerSec": apPerfWlanPrevPeakULOctetsPerSec,
       "apPerfWlanCurPeakULOctetsPerSec": apPerfWlanCurPeakULOctetsPerSec,
       "apPerfWlanAverageULOctetsPerSec": apPerfWlanAverageULOctetsPerSec,
       "apPerfWlanCurrentULOctetsPerSec": apPerfWlanCurrentULOctetsPerSec,
       "apPerfWlanULOctets": apPerfWlanULOctets,
       "apPerfWlanPrevPeakULPktsPerSec": apPerfWlanPrevPeakULPktsPerSec,
       "apPerfWlanCurPeakULPktsPerSec": apPerfWlanCurPeakULPktsPerSec,
       "apPerfWlanAverageULPktsPerSec": apPerfWlanAverageULPktsPerSec,
       "apPerfWlanCurrentULPktsPerSec": apPerfWlanCurrentULPktsPerSec,
       "apPerfWlanULPkts": apPerfWlanULPkts,
       "apPerfWlanPrevPeakDLOctetsPerSec": apPerfWlanPrevPeakDLOctetsPerSec,
       "apPerfWlanCurPeakDLOctetsPerSec": apPerfWlanCurPeakDLOctetsPerSec,
       "apPerfWlanAverageDLOctetsPerSec": apPerfWlanAverageDLOctetsPerSec,
       "apPerfWlanCurrentDLOctetsPerSec": apPerfWlanCurrentDLOctetsPerSec,
       "apPerfWlanDLOctets": apPerfWlanDLOctets,
       "apPerfWlanPrevPeakDLPktsPerSec": apPerfWlanPrevPeakDLPktsPerSec,
       "apPerfWlanCurPeakDLPktsPerSec": apPerfWlanCurPeakDLPktsPerSec,
       "apPerfWlanAverageDLPktsPerSec": apPerfWlanAverageDLPktsPerSec,
       "apPerfWlanCurrentDLPktsPerSec": apPerfWlanCurrentDLPktsPerSec,
       "apPerfWlanDLPkts": apPerfWlanDLPkts,
       "apChannelUtilizationTable": apChannelUtilizationTable,
       "apChannelUtilizationEntry": apChannelUtilizationEntry,
       "channel": channel,
       "apChnlUtilPrevPeakUtilization": apChnlUtilPrevPeakUtilization,
       "apChnlUtilCurPeakUtilization": apChnlUtilCurPeakUtilization,
       "apChnlUtilAverageUtilization": apChnlUtilAverageUtilization,
       "apChnlUtilCurrentUtilization": apChnlUtilCurrentUtilization,
       "apNeighboursTable": apNeighboursTable,
       "apNeighboursEntry": apNeighboursEntry,
       "nearbyApIndex": nearbyApIndex,
       "nearbyApInfo": nearbyApInfo,
       "nearbyApBSSID": nearbyApBSSID,
       "nearbyApChannel": nearbyApChannel,
       "nearbyApRSS": nearbyApRSS,
       "sensorManagement": sensorManagement,
       "tftpSever": tftpSever,
       "imagePath26xx": imagePath26xx,
       "imagePath36xx": imagePath36xx,
       "imageVersionOfap26xx": imageVersionOfap26xx,
       "imageVersionOfngap36xx": imageVersionOfngap36xx,
       "apRegistration": apRegistration,
       "apRegSecurityMode": apRegSecurityMode,
       "apRegDiscoveryRetries": apRegDiscoveryRetries,
       "apRegDiscoveryInterval": apRegDiscoveryInterval,
       "apRegTelnetPassword": apRegTelnetPassword,
       "apRegSSHPassword": apRegSSHPassword,
       "apRegUseClusterEncryption": apRegUseClusterEncryption,
       "apRegClusterSharedSecret": apRegClusterSharedSecret,
       "loadBalancing": loadBalancing,
       "loadGroupTable": loadGroupTable,
       "loadGroupEntry": loadGroupEntry,
       "loadGroupID": loadGroupID,
       "loadGroupName": loadGroupName,
       "loadGroupType": loadGroupType,
       "loadGroupBandPreference": loadGroupBandPreference,
       "loadGroupLoadControl": loadGroupLoadControl,
       "loadGroupClientCountRadio1": loadGroupClientCountRadio1,
       "loadGroupClientCountRadio2": loadGroupClientCountRadio2,
       "loadGroupLoadControlEnableR1": loadGroupLoadControlEnableR1,
       "loadGroupLoadControlEnableR2": loadGroupLoadControlEnableR2,
       "loadGroupLoadControlStrictLimitR1": loadGroupLoadControlStrictLimitR1,
       "loadGroupLoadControlStrictLimitR2": loadGroupLoadControlStrictLimitR2,
       "loadGrpRadiosTable": loadGrpRadiosTable,
       "loadGrpRadiosEntry": loadGrpRadiosEntry,
       "loadGrpRadiosRadio1": loadGrpRadiosRadio1,
       "loadGrpRadiosRadio2": loadGrpRadiosRadio2,
       "loadGrpWlanTable": loadGrpWlanTable,
       "loadGrpWlanEntry": loadGrpWlanEntry,
       "loadGrpWlanAssigned": loadGrpWlanAssigned,
       "apMaintenanceCycle": apMaintenanceCycle,
       "schedule": schedule,
       "startHour": startHour,
       "startMinute": startMinute,
       "duration": duration,
       "recurrenceDaily": recurrenceDaily,
       "recurrenceWeekly": recurrenceWeekly,
       "recurrenceMonthly": recurrenceMonthly,
       "apPlatforms": apPlatforms,
       "mobileUnits": mobileUnits,
       "mobileUnitCount": mobileUnitCount,
       "muTable": muTable,
       "muEntry": muEntry,
       "muMACAddress": muMACAddress,
       "muIPAddress": muIPAddress,
       "muUser": muUser,
       "muState": muState,
       "muAPSerialNo": muAPSerialNo,
       "muVnsSSID": muVnsSSID,
       "muTxPackets": muTxPackets,
       "muRxPackets": muRxPackets,
       "muTxOctets": muTxOctets,
       "muRxOctets": muRxOctets,
       "muDuration": muDuration,
       "muAPName": muAPName,
       "muTopologyName": muTopologyName,
       "muPolicyName": muPolicyName,
       "muDefaultCoS": muDefaultCoS,
       "muConnectionProtocol": muConnectionProtocol,
       "muConnectionCapability": muConnectionCapability,
       "muWLANID": muWLANID,
       "muBSSIDMac": muBSSIDMac,
       "muDot11ConnectionCapability": muDot11ConnectionCapability,
       "muTSPECTable": muTSPECTable,
       "muTSPECEntry": muTSPECEntry,
       "tspecMuMACAddress": tspecMuMACAddress,
       "tspecAC": tspecAC,
       "tspecDirection": tspecDirection,
       "tspecApSerialNumber": tspecApSerialNumber,
       "tspecMuIPAddress": tspecMuIPAddress,
       "tspecBssMac": tspecBssMac,
       "tspecSsid": tspecSsid,
       "tspecMDR": tspecMDR,
       "tspecNMS": tspecNMS,
       "tspecSBA": tspecSBA,
       "tspecDlRate": tspecDlRate,
       "tspecUlRate": tspecUlRate,
       "tspecDlViolations": tspecDlViolations,
       "tspecUlViolations": tspecUlViolations,
       "tspecProtocol": tspecProtocol,
       "muACLType": muACLType,
       "muACLTable": muACLTable,
       "muACLEntry": muACLEntry,
       "muACLMACAddress": muACLMACAddress,
       "muACLRowStatus": muACLRowStatus,
       "muAccessListTable": muAccessListTable,
       "muAccessListEntry": muAccessListEntry,
       "muAccessListMACAddress": muAccessListMACAddress,
       "muAccessListBitmaskLength": muAccessListBitmaskLength,
       "muAccessListRowStatus": muAccessListRowStatus,
       "associations": associations,
       "assocCount": assocCount,
       "assocTable": assocTable,
       "assocEntry": assocEntry,
       "assocMUMacAddress": assocMUMacAddress,
       "assocStartSysUpTime": assocStartSysUpTime,
       "assocTxPackets": assocTxPackets,
       "assocRxPackets": assocRxPackets,
       "assocTxOctets": assocTxOctets,
       "assocRxOctets": assocRxOctets,
       "assocDuration": assocDuration,
       "assocVnsIfIndex": assocVnsIfIndex,
       "protocols": protocols,
       "wassp": wassp,
       "logNotifications": logNotifications,
       "logEventSeverityThreshold": logEventSeverityThreshold,
       "logEventSeverity": logEventSeverity,
       "logEventComponent": logEventComponent,
       "logEventDescription": logEventDescription,
       "hiPathWirelessLogAlarm": hiPathWirelessLogAlarm,
       "sites": sites,
       "siteMaxEntries": siteMaxEntries,
       "siteNumEntries": siteNumEntries,
       "siteTableNextAvailableIndex": siteTableNextAvailableIndex,
       "siteTable": siteTable,
       "siteEntry": siteEntry,
       "siteID": siteID,
       "siteRowStatus": siteRowStatus,
       "siteName": siteName,
       "siteLocalRadiusAuthentication": siteLocalRadiusAuthentication,
       "siteDefaultDNSServer": siteDefaultDNSServer,
       "siteEnableSecureTunnel": siteEnableSecureTunnel,
       "siteEncryptCommAPtoController": siteEncryptCommAPtoController,
       "siteEncryptCommBetweenAPs": siteEncryptCommBetweenAPs,
       "siteBandPreferenceEnable": siteBandPreferenceEnable,
       "siteLoadControlEnableR1": siteLoadControlEnableR1,
       "siteLoadControlEnableR2": siteLoadControlEnableR2,
       "siteMaxClientR1": siteMaxClientR1,
       "siteMaxClientR2": siteMaxClientR2,
       "siteStrictLimitEnableR1": siteStrictLimitEnableR1,
       "siteStrictLimitEnableR2": siteStrictLimitEnableR2,
       "siteReplaceStnIDwithSiteName": siteReplaceStnIDwithSiteName,
       "sitePolicyTable": sitePolicyTable,
       "sitePolicyEntry": sitePolicyEntry,
       "sitePolicyID": sitePolicyID,
       "sitePolicyMember": sitePolicyMember,
       "siteCosTable": siteCosTable,
       "siteCosEntry": siteCosEntry,
       "siteCoSID": siteCoSID,
       "siteCoSMember": siteCoSMember,
       "siteAPTable": siteAPTable,
       "siteAPEntry": siteAPEntry,
       "siteAPMember": siteAPMember,
       "siteWlanTable": siteWlanTable,
       "siteWlanEntry": siteWlanEntry,
       "siteWlanApRadioIndex": siteWlanApRadioIndex,
       "siteWlanApRadioAssigned": siteWlanApRadioAssigned,
       "widsWips": widsWips,
       "mitigatorAnalysisEngine": mitigatorAnalysisEngine,
       "scanGroupMaxEntries": scanGroupMaxEntries,
       "scanGroupsCurrentEntries": scanGroupsCurrentEntries,
       "activeThreatsCounts": activeThreatsCounts,
       "friendlyAPCounts": friendlyAPCounts,
       "uncategorizedAPCounts": uncategorizedAPCounts,
       "widsWipsEngineTable": widsWipsEngineTable,
       "widsWipsEngineEntry": widsWipsEngineEntry,
       "widsWipsEngineRowStatus": widsWipsEngineRowStatus,
       "widsWipsEngineControllerIPAddress": widsWipsEngineControllerIPAddress,
       "widsWipsEnginePollInterval": widsWipsEnginePollInterval,
       "widsWipsEnginePollRetry": widsWipsEnginePollRetry,
       "inServiceScanGroupTable": inServiceScanGroupTable,
       "inServiceScanGroupEntry": inServiceScanGroupEntry,
       "scanGroupProfileID": scanGroupProfileID,
       "inSrvScanGrpName": inSrvScanGrpName,
       "inSrvScanGrpSecurityThreats": inSrvScanGrpSecurityThreats,
       "inSrvScanGrpMaxConcurrentAttacksPerAP": inSrvScanGrpMaxConcurrentAttacksPerAP,
       "inSrvScanGrpCounterMeasuresType": inSrvScanGrpCounterMeasuresType,
       "inSrvScanGrpScan2400MHzSelection": inSrvScanGrpScan2400MHzSelection,
       "inSrvScanGrpScan5GHzSelection": inSrvScanGrpScan5GHzSelection,
       "inSrvScanGrpblockAdHocClientsPeriod": inSrvScanGrpblockAdHocClientsPeriod,
       "inSrvScanGrpClassifySourceIF": inSrvScanGrpClassifySourceIF,
       "inSrvScanGrpRowStatus": inSrvScanGrpRowStatus,
       "inSrvScanGrpDetectRogueAP": inSrvScanGrpDetectRogueAP,
       "inSrvScanGrpListeningPort": inSrvScanGrpListeningPort,
       "outOfServiceScanGroupTable": outOfServiceScanGroupTable,
       "outOfServiceScanGroupEntry": outOfServiceScanGroupEntry,
       "outOfSrvScanGrpName": outOfSrvScanGrpName,
       "outOfSrvScanGrpRadio": outOfSrvScanGrpRadio,
       "outOfSrvScanGrpChannelList": outOfSrvScanGrpChannelList,
       "outOfSrvScanGrpScanType": outOfSrvScanGrpScanType,
       "outOfSrvScanGrpChannelDwellTime": outOfSrvScanGrpChannelDwellTime,
       "outOfSrvScanGrpScanTimeInterval": outOfSrvScanGrpScanTimeInterval,
       "outOfSrvScanGrpSecurityScan": outOfSrvScanGrpSecurityScan,
       "outOfSrvScanGrpScanActivity": outOfSrvScanGrpScanActivity,
       "outOfSrvScanGrpScanRowStatus": outOfSrvScanGrpScanRowStatus,
       "scanGroupAPAssignmentTable": scanGroupAPAssignmentTable,
       "scanGroupAPAssignmentEntry": scanGroupAPAssignmentEntry,
       "scanGroupAPAssignApSerial": scanGroupAPAssignApSerial,
       "scanGroupAPAssignGroupName": scanGroupAPAssignGroupName,
       "scanGroupAPAssignName": scanGroupAPAssignName,
       "scanGroupAPAssignRadio1": scanGroupAPAssignRadio1,
       "scanGroupAPAssignRadio2": scanGroupAPAssignRadio2,
       "scanGroupAPAssignInactiveAP": scanGroupAPAssignInactiveAP,
       "scanGroupAPAssignAllowScanning": scanGroupAPAssignAllowScanning,
       "scanGroupAPAssignAllowSpectrumAnalysis": scanGroupAPAssignAllowSpectrumAnalysis,
       "scanGroupAPAssignControllerIPAddress": scanGroupAPAssignControllerIPAddress,
       "scanGroupAPAssignFordwardingService": scanGroupAPAssignFordwardingService,
       "scanAPTable": scanAPTable,
       "scanAPEntry": scanAPEntry,
       "scanAPControllerIPAddress": scanAPControllerIPAddress,
       "scanAPSerialNumber": scanAPSerialNumber,
       "scanAPAcessPointName": scanAPAcessPointName,
       "scanAPRowStatus": scanAPRowStatus,
       "scanAPProfileName": scanAPProfileName,
       "scanAPProfileType": scanAPProfileType,
       "friendlyAPTable": friendlyAPTable,
       "friendlyAPEntry": friendlyAPEntry,
       "friendlyAPMacAddress": friendlyAPMacAddress,
       "friendlyAPSSID": friendlyAPSSID,
       "friendlyAPDescription": friendlyAPDescription,
       "friendlyAPManufacturer": friendlyAPManufacturer,
       "uncategorizedAPTable": uncategorizedAPTable,
       "uncategorizedAPEntry": uncategorizedAPEntry,
       "uncategorizedAPMAC": uncategorizedAPMAC,
       "uncategorizedAPDescption": uncategorizedAPDescption,
       "uncategorizedAPManufacturer": uncategorizedAPManufacturer,
       "uncategorizedAPClassify": uncategorizedAPClassify,
       "uncategorizedAPSSID": uncategorizedAPSSID,
       "authorizedAPTable": authorizedAPTable,
       "authorizedAPEntry": authorizedAPEntry,
       "authorizedAPMAC": authorizedAPMAC,
       "authorizedAPDescription": authorizedAPDescription,
       "authorizedAPManufacturer": authorizedAPManufacturer,
       "authorizedAPClassify": authorizedAPClassify,
       "authorizedAPRowStatus": authorizedAPRowStatus,
       "prohibitedAPTable": prohibitedAPTable,
       "prohibitedAPEntry": prohibitedAPEntry,
       "prohibitedAPMAC": prohibitedAPMAC,
       "prohibitedAPCategory": prohibitedAPCategory,
       "prohibitedAPDescription": prohibitedAPDescription,
       "prohibitedAPManufacturer": prohibitedAPManufacturer,
       "prohibitedAPClassify": prohibitedAPClassify,
       "prohibitedAPRowStatus": prohibitedAPRowStatus,
       "dedicatedScanGroupTable": dedicatedScanGroupTable,
       "dedicatedScanGroupEntry": dedicatedScanGroupEntry,
       "dedicatedScanGrpName": dedicatedScanGrpName,
       "dedicatedScanGrpSecurityThreats": dedicatedScanGrpSecurityThreats,
       "dedicatedScanGrpMaxConcurrentAttacksPerAP": dedicatedScanGrpMaxConcurrentAttacksPerAP,
       "dedicatedScanGrpCounterMeasures": dedicatedScanGrpCounterMeasures,
       "dedicatedScanGrpScan2400MHzFreq": dedicatedScanGrpScan2400MHzFreq,
       "dedicatedScanGrpScan5GHzFreq": dedicatedScanGrpScan5GHzFreq,
       "dedicatedScanGrpBlockAdHocPeriod": dedicatedScanGrpBlockAdHocPeriod,
       "dedicatedScanGrpClassifySourceIF": dedicatedScanGrpClassifySourceIF,
       "dedicatedScanGrpRowStatus": dedicatedScanGrpRowStatus,
       "dedicatedScanGrpDetectRogueAP": dedicatedScanGrpDetectRogueAP,
       "dedicatedScanGrpListeningPort": dedicatedScanGrpListeningPort,
       "widsWipsReport": widsWipsReport,
       "activeThreatTable": activeThreatTable,
       "activeThreatEntry": activeThreatEntry,
       "activeThreatIndex": activeThreatIndex,
       "activeThreatCategory": activeThreatCategory,
       "activeThreatDeviceMAC": activeThreatDeviceMAC,
       "activeThreatDateTime": activeThreatDateTime,
       "activeThreatCounterMeasure": activeThreatCounterMeasure,
       "activeThreatAPName": activeThreatAPName,
       "activeThreatRSS": activeThreatRSS,
       "activeThreatExtraDetails": activeThreatExtraDetails,
       "activeThreatThreat": activeThreatThreat,
       "countermeasureAPTable": countermeasureAPTable,
       "countermeasureAPEntry": countermeasureAPEntry,
       "countermeasureAPThreatIndex": countermeasureAPThreatIndex,
       "countermeasureAPSerial": countermeasureAPSerial,
       "countermeasureAPName": countermeasureAPName,
       "countermeasureAPThreatCategory": countermeasureAPThreatCategory,
       "countermeasureAPCountermeasure": countermeasureAPCountermeasure,
       "countermeasureAPTime": countermeasureAPTime,
       "blacklistedClientTable": blacklistedClientTable,
       "blacklistedClientEntry": blacklistedClientEntry,
       "blacklistedClientMAC": blacklistedClientMAC,
       "blacklistedClientStatTime": blacklistedClientStatTime,
       "blacklistedClientEndTime": blacklistedClientEndTime,
       "blacklistedClientReason": blacklistedClientReason,
       "threatSummaryTable": threatSummaryTable,
       "threatSummaryEntry": threatSummaryEntry,
       "threatSummaryIndex": threatSummaryIndex,
       "threatSummaryCategory": threatSummaryCategory,
       "threatSummaryActiveThreat": threatSummaryActiveThreat,
       "threatSummaryHistoricalCounts": threatSummaryHistoricalCounts,
       "apNotifications": apNotifications,
       "apEventId": apEventId,
       "apEventDescription": apEventDescription,
       "apEventAPSerialNumber": apEventAPSerialNumber,
       "apTunnelAlarm": apTunnelAlarm,
       "stationSessionNotifications": stationSessionNotifications,
       "stationEventType": stationEventType,
       "stationMacAddress": stationMacAddress,
       "stationIPAddress": stationIPAddress,
       "stationAPName": stationAPName,
       "stationAPSSID": stationAPSSID,
       "stationDetailEvent": stationDetailEvent,
       "stationRoamedAPName": stationRoamedAPName,
       "stationName": stationName,
       "stationBSSID": stationBSSID,
       "stationEventTimeStamp": stationEventTimeStamp,
       "stationEventAlarm": stationEventAlarm,
       "stationIPv6Address1": stationIPv6Address1,
       "stationIPv6Address2": stationIPv6Address2,
       "stationIPv6Address3": stationIPv6Address3,
       "hiPathWirelessHWCConformance": hiPathWirelessHWCConformance,
       "hiPathWirelessHWCModule": hiPathWirelessHWCModule,
       "hiPathWirelessHWCGroup": hiPathWirelessHWCGroup,
       "hiPathWirelessHWCAlarms": hiPathWirelessHWCAlarms,
       "hiPathWirelessHWCObsolete": hiPathWirelessHWCObsolete,
       "wirelessEWCGroups": wirelessEWCGroups,
       "physicalPortsGroup": physicalPortsGroup,
       "phyDHCPRangeGroup": phyDHCPRangeGroup,
       "layerTwoPortGroup": layerTwoPortGroup,
       "muGroup": muGroup,
       "apStatsGroup": apStatsGroup,
       "muACLGroup": muACLGroup,
       "siteGroup": siteGroup,
       "sitePolicyGroup": sitePolicyGroup,
       "siteCosGroup": siteCosGroup,
       "siteAPGroup": siteAPGroup,
       "siteWlanGroup": siteWlanGroup,
       "apGroup": apGroup,
       "wlanGroup": wlanGroup,
       "wlanStatsGroup": wlanStatsGroup,
       "topologyGroup": topologyGroup,
       "topologyStatGroup": topologyStatGroup,
       "loadGroup": loadGroup,
       "widsWipsObjectsGroup": widsWipsObjectsGroup,
       "widsWipsEngineGroup": widsWipsEngineGroup,
       "outOfServiceScanGroup": outOfServiceScanGroup,
       "inServiceScanGroup": inServiceScanGroup,
       "scanGroupAPAssignmentGroup": scanGroupAPAssignmentGroup,
       "scanAPGroup": scanAPGroup,
       "friendlyAPGroup": friendlyAPGroup,
       "wlanSecurityReportGroup": wlanSecurityReportGroup,
       "apAntennaGroup": apAntennaGroup,
       "muAccessListGroup": muAccessListGroup,
       "activeThreatGroup": activeThreatGroup,
       "countermeasureAPGroup": countermeasureAPGroup,
       "blaclistedClientGroup": blaclistedClientGroup,
       "threatSummaryGroup": threatSummaryGroup,
       "licensingInformationGroup": licensingInformationGroup,
       "stationsByProtocolGroup": stationsByProtocolGroup,
       "apByChannelGroup": apByChannelGroup,
       "uncategorizedAPGroup": uncategorizedAPGroup,
       "authorizedAPGroup": authorizedAPGroup,
       "prohibitedAPGroup": prohibitedAPGroup,
       "dedicatedScanGroup": dedicatedScanGroup,
       "apRadioAntennaGroup": apRadioAntennaGroup,
       "radiusFastFailoverEventsGroup": radiusFastFailoverEventsGroup,
       "dhcpRelayListenersGroup": dhcpRelayListenersGroup,
       "authenticationAdvancedGroup": authenticationAdvancedGroup,
       "radiusExtnsSettingGroup": radiusExtnsSettingGroup,
       "hiPathWirelessControllerMib": hiPathWirelessControllerMib}
)
