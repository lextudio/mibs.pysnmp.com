# SNMP MIB module (CISCO-SYSTEM-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SYSTEM-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:09:27 2024
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

(EntPhysicalIndexOrZero,
 TimeIntervalSec) = mibBuilder.importSymbols(
    "CISCO-TC",
    "EntPhysicalIndexOrZero",
    "TimeIntervalSec")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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

ciscoSystemExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 305)
)
ciscoSystemExtMIB.setRevisions(
        ("2016-07-19 00:00",
         "2016-06-07 00:00",
         "2015-08-19 00:00",
         "2007-08-06 00:00",
         "2006-11-29 00:00",
         "2006-09-25 00:00",
         "2005-11-09 00:00",
         "2005-06-14 00:00",
         "2004-04-19 00:00",
         "2003-05-02 00:00",
         "2003-03-02 00:00",
         "2002-11-19 00:00",
         "2002-10-04 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CseHaRestartReason(Integer32, TextualConvention):
    status = "current"
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
              8,
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("aborted", 9),
          ("configRemove", 7),
          ("configUpdate", 6),
          ("gracefulExit", 12),
          ("heartbeatFailure", 10),
          ("noCallHomeFailure", 13),
          ("otherSignal", 3),
          ("serviceTimeout", 14),
          ("shutdown", 8),
          ("sigterm", 4),
          ("softwareUpgrade", 5),
          ("ungracefulExit", 2),
          ("unknown", 1),
          ("userTerminate", 11))
    )



class CiscoMaintModeState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("maintenance", 2),
          ("normal", 1),
          ("unplannedMaint", 3))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoSystemExtMIBNotifsPrefix_ObjectIdentity = ObjectIdentity
ciscoSystemExtMIBNotifsPrefix = _CiscoSystemExtMIBNotifsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 0)
)
_CiscoSystemExtMIBObjects_ObjectIdentity = ObjectIdentity
ciscoSystemExtMIBObjects = _CiscoSystemExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 1)
)
_CiscoSysInfoGroup_ObjectIdentity = ObjectIdentity
ciscoSysInfoGroup = _CiscoSysInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 1)
)


class _CseSysCPUUtilization_Type(Gauge32):
    """Custom type cseSysCPUUtilization based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CseSysCPUUtilization_Type.__name__ = "Gauge32"
_CseSysCPUUtilization_Object = MibScalar
cseSysCPUUtilization = _CseSysCPUUtilization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 1, 1),
    _CseSysCPUUtilization_Type()
)
cseSysCPUUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseSysCPUUtilization.setStatus("current")
if mibBuilder.loadTexts:
    cseSysCPUUtilization.setUnits("%")


class _CseSysMemoryUtilization_Type(Gauge32):
    """Custom type cseSysMemoryUtilization based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CseSysMemoryUtilization_Type.__name__ = "Gauge32"
_CseSysMemoryUtilization_Object = MibScalar
cseSysMemoryUtilization = _CseSysMemoryUtilization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 1, 2),
    _CseSysMemoryUtilization_Type()
)
cseSysMemoryUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseSysMemoryUtilization.setStatus("current")
if mibBuilder.loadTexts:
    cseSysMemoryUtilization.setUnits("%")
_CseSysConfLastChange_Type = DateAndTime
_CseSysConfLastChange_Object = MibScalar
cseSysConfLastChange = _CseSysConfLastChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 1, 3),
    _CseSysConfLastChange_Type()
)
cseSysConfLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseSysConfLastChange.setStatus("current")


class _CseSysAutoSync_Type(Integer32):
    """Custom type cseSysAutoSync based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noSync", 2),
          ("sync", 1))
    )


_CseSysAutoSync_Type.__name__ = "Integer32"
_CseSysAutoSync_Object = MibScalar
cseSysAutoSync = _CseSysAutoSync_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 1, 4),
    _CseSysAutoSync_Type()
)
cseSysAutoSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cseSysAutoSync.setStatus("current")


class _CseSysAutoSyncState_Type(Integer32):
    """Custom type cseSysAutoSyncState based on Integer32"""
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
        *(("failed", 3),
          ("inProgress", 1),
          ("notStarted", 4),
          ("succeeded", 2))
    )


_CseSysAutoSyncState_Type.__name__ = "Integer32"
_CseSysAutoSyncState_Object = MibScalar
cseSysAutoSyncState = _CseSysAutoSyncState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 1, 5),
    _CseSysAutoSyncState_Type()
)
cseSysAutoSyncState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseSysAutoSyncState.setStatus("current")


class _CseWriteErase_Type(Integer32):
    """Custom type cseWriteErase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eraseAll", 2),
          ("noOp", 1))
    )


_CseWriteErase_Type.__name__ = "Integer32"
_CseWriteErase_Object = MibScalar
cseWriteErase = _CseWriteErase_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 1, 6),
    _CseWriteErase_Type()
)
cseWriteErase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cseWriteErase.setStatus("current")


class _CseSysConsolePortStatus_Type(Integer32):
    """Custom type cseSysConsolePortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connected", 1),
          ("notConnected", 2))
    )


_CseSysConsolePortStatus_Type.__name__ = "Integer32"
_CseSysConsolePortStatus_Object = MibScalar
cseSysConsolePortStatus = _CseSysConsolePortStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 1, 7),
    _CseSysConsolePortStatus_Type()
)
cseSysConsolePortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseSysConsolePortStatus.setStatus("current")


class _CseSysTelnetServiceActivation_Type(TruthValue):
    """Custom type cseSysTelnetServiceActivation based on TruthValue"""


_CseSysTelnetServiceActivation_Object = MibScalar
cseSysTelnetServiceActivation = _CseSysTelnetServiceActivation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 1, 8),
    _CseSysTelnetServiceActivation_Type()
)
cseSysTelnetServiceActivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cseSysTelnetServiceActivation.setStatus("current")


class _CseSysFIPSModeActivation_Type(TruthValue):
    """Custom type cseSysFIPSModeActivation based on TruthValue"""


_CseSysFIPSModeActivation_Object = MibScalar
cseSysFIPSModeActivation = _CseSysFIPSModeActivation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 1, 9),
    _CseSysFIPSModeActivation_Type()
)
cseSysFIPSModeActivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cseSysFIPSModeActivation.setStatus("current")
_CseSysUpTime_Type = TimeIntervalSec
_CseSysUpTime_Object = MibScalar
cseSysUpTime = _CseSysUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 1, 10),
    _CseSysUpTime_Type()
)
cseSysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseSysUpTime.setStatus("current")
if mibBuilder.loadTexts:
    cseSysUpTime.setUnits("Seconds")
_CiscoSysErrorGroup_ObjectIdentity = ObjectIdentity
ciscoSysErrorGroup = _CiscoSysErrorGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 2)
)
_CseSnmpErrorTable_Object = MibTable
cseSnmpErrorTable = _CseSnmpErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cseSnmpErrorTable.setStatus("current")
_CseSnmpErrorEntry_Object = MibTableRow
cseSnmpErrorEntry = _CseSnmpErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 2, 1, 1)
)
cseSnmpErrorEntry.setIndexNames(
    (0, "CISCO-SYSTEM-EXT-MIB", "cseSnmpErrorAddressType"),
    (0, "CISCO-SYSTEM-EXT-MIB", "cseSnmpErrorAddress"),
    (0, "CISCO-SYSTEM-EXT-MIB", "cseSnmpErrorRequestId"),
)
if mibBuilder.loadTexts:
    cseSnmpErrorEntry.setStatus("current")
_CseSnmpErrorAddressType_Type = InetAddressType
_CseSnmpErrorAddressType_Object = MibTableColumn
cseSnmpErrorAddressType = _CseSnmpErrorAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 2, 1, 1, 1),
    _CseSnmpErrorAddressType_Type()
)
cseSnmpErrorAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cseSnmpErrorAddressType.setStatus("current")
_CseSnmpErrorAddress_Type = InetAddress
_CseSnmpErrorAddress_Object = MibTableColumn
cseSnmpErrorAddress = _CseSnmpErrorAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 2, 1, 1, 2),
    _CseSnmpErrorAddress_Type()
)
cseSnmpErrorAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cseSnmpErrorAddress.setStatus("current")
_CseSnmpErrorRequestId_Type = Unsigned32
_CseSnmpErrorRequestId_Object = MibTableColumn
cseSnmpErrorRequestId = _CseSnmpErrorRequestId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 2, 1, 1, 3),
    _CseSnmpErrorRequestId_Type()
)
cseSnmpErrorRequestId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cseSnmpErrorRequestId.setStatus("current")
_CseSnmpErrorCode_Type = Unsigned32
_CseSnmpErrorCode_Object = MibTableColumn
cseSnmpErrorCode = _CseSnmpErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 2, 1, 1, 4),
    _CseSnmpErrorCode_Type()
)
cseSnmpErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseSnmpErrorCode.setStatus("current")
_CseSnmpErrorDescription_Type = SnmpAdminString
_CseSnmpErrorDescription_Object = MibTableColumn
cseSnmpErrorDescription = _CseSnmpErrorDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 2, 1, 1, 5),
    _CseSnmpErrorDescription_Type()
)
cseSnmpErrorDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseSnmpErrorDescription.setStatus("current")
_CiscoHaGroup_ObjectIdentity = ObjectIdentity
ciscoHaGroup = _CiscoHaGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 3)
)
_CseHaRestartReason_Type = CseHaRestartReason
_CseHaRestartReason_Object = MibScalar
cseHaRestartReason = _CseHaRestartReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 3, 2),
    _CseHaRestartReason_Type()
)
cseHaRestartReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cseHaRestartReason.setStatus("current")
_CseHaRestartStateless_Type = TruthValue
_CseHaRestartStateless_Object = MibScalar
cseHaRestartStateless = _CseHaRestartStateless_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 3, 3),
    _CseHaRestartStateless_Type()
)
cseHaRestartStateless.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cseHaRestartStateless.setStatus("current")


class _CseHaRestartService_Type(SnmpAdminString):
    """Custom type cseHaRestartService based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CseHaRestartService_Type.__name__ = "SnmpAdminString"
_CseHaRestartService_Object = MibScalar
cseHaRestartService = _CseHaRestartService_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 3, 4),
    _CseHaRestartService_Type()
)
cseHaRestartService.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cseHaRestartService.setStatus("current")
_CseHaNotification_ObjectIdentity = ObjectIdentity
cseHaNotification = _CseHaNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 3, 5)
)
_CseHaNotificationPrefix_ObjectIdentity = ObjectIdentity
cseHaNotificationPrefix = _CseHaNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 3, 5, 0)
)


class _CseHaShutDownReason_Type(SnmpAdminString):
    """Custom type cseHaShutDownReason based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CseHaShutDownReason_Type.__name__ = "SnmpAdminString"
_CseHaShutDownReason_Object = MibScalar
cseHaShutDownReason = _CseHaShutDownReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 3, 6),
    _CseHaShutDownReason_Type()
)
cseHaShutDownReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cseHaShutDownReason.setStatus("current")
_CiscoSwFailureGroup_ObjectIdentity = ObjectIdentity
ciscoSwFailureGroup = _CiscoSwFailureGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 4)
)


class _CseSwCorePath_Type(SnmpAdminString):
    """Custom type cseSwCorePath based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CseSwCorePath_Type.__name__ = "SnmpAdminString"
_CseSwCorePath_Object = MibScalar
cseSwCorePath = _CseSwCorePath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 4, 1),
    _CseSwCorePath_Type()
)
cseSwCorePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseSwCorePath.setStatus("current")
_CseSwCoresTable_Object = MibTable
cseSwCoresTable = _CseSwCoresTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 4, 2)
)
if mibBuilder.loadTexts:
    cseSwCoresTable.setStatus("current")
_CseSwCoresEntry_Object = MibTableRow
cseSwCoresEntry = _CseSwCoresEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 4, 2, 1)
)
cseSwCoresEntry.setIndexNames(
    (0, "CISCO-SYSTEM-EXT-MIB", "cseSwCoresModule"),
    (0, "CISCO-SYSTEM-EXT-MIB", "cseSwCoresProcName"),
    (0, "CISCO-SYSTEM-EXT-MIB", "cseSwCoresInstance"),
)
if mibBuilder.loadTexts:
    cseSwCoresEntry.setStatus("current")
_CseSwCoresModule_Type = EntPhysicalIndexOrZero
_CseSwCoresModule_Object = MibTableColumn
cseSwCoresModule = _CseSwCoresModule_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 4, 2, 1, 1),
    _CseSwCoresModule_Type()
)
cseSwCoresModule.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cseSwCoresModule.setStatus("current")


class _CseSwCoresProcName_Type(SnmpAdminString):
    """Custom type cseSwCoresProcName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CseSwCoresProcName_Type.__name__ = "SnmpAdminString"
_CseSwCoresProcName_Object = MibTableColumn
cseSwCoresProcName = _CseSwCoresProcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 4, 2, 1, 2),
    _CseSwCoresProcName_Type()
)
cseSwCoresProcName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cseSwCoresProcName.setStatus("current")
_CseSwCoresInstance_Type = Unsigned32
_CseSwCoresInstance_Object = MibTableColumn
cseSwCoresInstance = _CseSwCoresInstance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 4, 2, 1, 3),
    _CseSwCoresInstance_Type()
)
cseSwCoresInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cseSwCoresInstance.setStatus("current")
_CseSwCoresPID_Type = Unsigned32
_CseSwCoresPID_Object = MibTableColumn
cseSwCoresPID = _CseSwCoresPID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 4, 2, 1, 4),
    _CseSwCoresPID_Type()
)
cseSwCoresPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseSwCoresPID.setStatus("current")
_CseSwCoresTimeCreated_Type = DateAndTime
_CseSwCoresTimeCreated_Object = MibTableColumn
cseSwCoresTimeCreated = _CseSwCoresTimeCreated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 4, 2, 1, 5),
    _CseSwCoresTimeCreated_Type()
)
cseSwCoresTimeCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseSwCoresTimeCreated.setStatus("current")
_CseSwCoresSlotNum_Type = Unsigned32
_CseSwCoresSlotNum_Object = MibTableColumn
cseSwCoresSlotNum = _CseSwCoresSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 4, 2, 1, 6),
    _CseSwCoresSlotNum_Type()
)
cseSwCoresSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseSwCoresSlotNum.setStatus("current")
_CseSwCoresFileName_Type = SnmpAdminString
_CseSwCoresFileName_Object = MibTableColumn
cseSwCoresFileName = _CseSwCoresFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 4, 2, 1, 7),
    _CseSwCoresFileName_Type()
)
cseSwCoresFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseSwCoresFileName.setStatus("current")
_CseFailNotification_ObjectIdentity = ObjectIdentity
cseFailNotification = _CseFailNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 4, 3)
)
_CseFailNotificationPrefix_ObjectIdentity = ObjectIdentity
cseFailNotificationPrefix = _CseFailNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 4, 3, 0)
)
_CiscoSwFailureNotifControl_ObjectIdentity = ObjectIdentity
ciscoSwFailureNotifControl = _CiscoSwFailureNotifControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 5)
)


class _CiscoSwFailureNotifEnable_Type(TruthValue):
    """Custom type ciscoSwFailureNotifEnable based on TruthValue"""


_CiscoSwFailureNotifEnable_Object = MibScalar
ciscoSwFailureNotifEnable = _CiscoSwFailureNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 5, 1),
    _CiscoSwFailureNotifEnable_Type()
)
ciscoSwFailureNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoSwFailureNotifEnable.setStatus("current")
_CiscoSystemSwitchingModeGroup_ObjectIdentity = ObjectIdentity
ciscoSystemSwitchingModeGroup = _CiscoSystemSwitchingModeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 6)
)


class _CiscoSystemSwitchingModeAdmin_Type(Integer32):
    """Custom type ciscoSystemSwitchingModeAdmin based on Integer32"""
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
        *(("nexus3000", 3),
          ("nexus9000", 4),
          ("notApplicable", 2),
          ("other", 1))
    )


_CiscoSystemSwitchingModeAdmin_Type.__name__ = "Integer32"
_CiscoSystemSwitchingModeAdmin_Object = MibScalar
ciscoSystemSwitchingModeAdmin = _CiscoSystemSwitchingModeAdmin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 6, 1),
    _CiscoSystemSwitchingModeAdmin_Type()
)
ciscoSystemSwitchingModeAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoSystemSwitchingModeAdmin.setStatus("current")


class _CiscoSystemSwitchingModeOper_Type(Integer32):
    """Custom type ciscoSystemSwitchingModeOper based on Integer32"""
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
        *(("nexus3000", 3),
          ("nexus9000", 4),
          ("notApplicable", 2),
          ("other", 1))
    )


_CiscoSystemSwitchingModeOper_Type.__name__ = "Integer32"
_CiscoSystemSwitchingModeOper_Object = MibScalar
ciscoSystemSwitchingModeOper = _CiscoSystemSwitchingModeOper_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 6, 2),
    _CiscoSystemSwitchingModeOper_Type()
)
ciscoSystemSwitchingModeOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoSystemSwitchingModeOper.setStatus("current")
_CiscoSystemMaintModeGroup_ObjectIdentity = ObjectIdentity
ciscoSystemMaintModeGroup = _CiscoSystemMaintModeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 7)
)
_CseMaintModeState_Type = CiscoMaintModeState
_CseMaintModeState_Object = MibScalar
cseMaintModeState = _CseMaintModeState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 7, 1),
    _CseMaintModeState_Type()
)
cseMaintModeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseMaintModeState.setStatus("current")
_CseMaintModeNotification_ObjectIdentity = ObjectIdentity
cseMaintModeNotification = _CseMaintModeNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 7, 2)
)
_CseMaintModeNotificationPrefix_ObjectIdentity = ObjectIdentity
cseMaintModeNotificationPrefix = _CseMaintModeNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 7, 2, 0)
)
_CiscoSystemMaintModeNotifControl_ObjectIdentity = ObjectIdentity
ciscoSystemMaintModeNotifControl = _CiscoSystemMaintModeNotifControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 8)
)


class _CiscoSystemNormalModeNotifEnable_Type(TruthValue):
    """Custom type ciscoSystemNormalModeNotifEnable based on TruthValue"""


_CiscoSystemNormalModeNotifEnable_Object = MibScalar
ciscoSystemNormalModeNotifEnable = _CiscoSystemNormalModeNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 8, 1),
    _CiscoSystemNormalModeNotifEnable_Type()
)
ciscoSystemNormalModeNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoSystemNormalModeNotifEnable.setStatus("current")


class _CiscoSystemMaintModeNotifEnable_Type(TruthValue):
    """Custom type ciscoSystemMaintModeNotifEnable based on TruthValue"""


_CiscoSystemMaintModeNotifEnable_Object = MibScalar
ciscoSystemMaintModeNotifEnable = _CiscoSystemMaintModeNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 8, 2),
    _CiscoSystemMaintModeNotifEnable_Type()
)
ciscoSystemMaintModeNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoSystemMaintModeNotifEnable.setStatus("current")
_CiscoSystemReloadGroup_ObjectIdentity = ObjectIdentity
ciscoSystemReloadGroup = _CiscoSystemReloadGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 9)
)
_CseSystemReloadPending_Type = TruthValue
_CseSystemReloadPending_Object = MibScalar
cseSystemReloadPending = _CseSystemReloadPending_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 9, 1),
    _CseSystemReloadPending_Type()
)
cseSystemReloadPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cseSystemReloadPending.setStatus("current")
_CiscoSystemExtMIBConformance_ObjectIdentity = ObjectIdentity
ciscoSystemExtMIBConformance = _CiscoSystemExtMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 2)
)
_CiscoSystemExtMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoSystemExtMIBCompliances = _CiscoSystemExtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 1)
)
_CiscoSystemExtMIBGroups_ObjectIdentity = ObjectIdentity
ciscoSystemExtMIBGroups = _CiscoSystemExtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 2)
)

# Managed Objects groups

ciscoSystemExtInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 2, 1)
)
ciscoSystemExtInfoGroup.setObjects(
      *(("CISCO-SYSTEM-EXT-MIB", "cseSysCPUUtilization"),
        ("CISCO-SYSTEM-EXT-MIB", "cseSysMemoryUtilization"),
        ("CISCO-SYSTEM-EXT-MIB", "cseSysConfLastChange"))
)
if mibBuilder.loadTexts:
    ciscoSystemExtInfoGroup.setStatus("deprecated")

ciscoSystemExtErrorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 2, 2)
)
ciscoSystemExtErrorGroup.setObjects(
      *(("CISCO-SYSTEM-EXT-MIB", "cseSnmpErrorCode"),
        ("CISCO-SYSTEM-EXT-MIB", "cseSnmpErrorDescription"))
)
if mibBuilder.loadTexts:
    ciscoSystemExtErrorGroup.setStatus("current")

ciscoSystemExtHaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 2, 3)
)
ciscoSystemExtHaGroup.setObjects(
      *(("CISCO-SYSTEM-EXT-MIB", "cseHaRestartReason"),
        ("CISCO-SYSTEM-EXT-MIB", "cseHaRestartService"),
        ("CISCO-SYSTEM-EXT-MIB", "cseHaRestartStateless"))
)
if mibBuilder.loadTexts:
    ciscoSystemExtHaGroup.setStatus("current")

ciscoSystemExtInfoGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 2, 5)
)
ciscoSystemExtInfoGroupRev1.setObjects(
      *(("CISCO-SYSTEM-EXT-MIB", "cseSysCPUUtilization"),
        ("CISCO-SYSTEM-EXT-MIB", "cseSysMemoryUtilization"),
        ("CISCO-SYSTEM-EXT-MIB", "cseSysConfLastChange"),
        ("CISCO-SYSTEM-EXT-MIB", "cseSysAutoSync"),
        ("CISCO-SYSTEM-EXT-MIB", "cseSysAutoSyncState"))
)
if mibBuilder.loadTexts:
    ciscoSystemExtInfoGroupRev1.setStatus("deprecated")

ciscoSystemExtInfoGroupOptional = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 2, 6)
)
ciscoSystemExtInfoGroupOptional.setObjects(
    ("CISCO-SYSTEM-EXT-MIB", "cseWriteErase")
)
if mibBuilder.loadTexts:
    ciscoSystemExtInfoGroupOptional.setStatus("current")

ciscoSystemExtSwFailureGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 2, 7)
)
ciscoSystemExtSwFailureGroup.setObjects(
    ("CISCO-SYSTEM-EXT-MIB", "cseSwCorePath")
)
if mibBuilder.loadTexts:
    ciscoSystemExtSwFailureGroup.setStatus("current")

ciscoSystemExtInfoGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 2, 8)
)
ciscoSystemExtInfoGroupRev2.setObjects(
    ("CISCO-SYSTEM-EXT-MIB", "cseSysConsolePortStatus")
)
if mibBuilder.loadTexts:
    ciscoSystemExtInfoGroupRev2.setStatus("current")

ciscoSystemExtSwFailureGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 2, 9)
)
ciscoSystemExtSwFailureGroup2.setObjects(
      *(("CISCO-SYSTEM-EXT-MIB", "cseSwCoresPID"),
        ("CISCO-SYSTEM-EXT-MIB", "cseSwCoresTimeCreated"),
        ("CISCO-SYSTEM-EXT-MIB", "cseSwCoresSlotNum"))
)
if mibBuilder.loadTexts:
    ciscoSystemExtSwFailureGroup2.setStatus("current")

ciscoSystemExtHaGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 2, 11)
)
ciscoSystemExtHaGroupRev1.setObjects(
    ("CISCO-SYSTEM-EXT-MIB", "cseHaShutDownReason")
)
if mibBuilder.loadTexts:
    ciscoSystemExtHaGroupRev1.setStatus("current")

ciscoSystemExtInfoTelnetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 2, 12)
)
ciscoSystemExtInfoTelnetGroup.setObjects(
    ("CISCO-SYSTEM-EXT-MIB", "cseSysTelnetServiceActivation")
)
if mibBuilder.loadTexts:
    ciscoSystemExtInfoTelnetGroup.setStatus("current")

ciscoSystemExtSwFailureGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 2, 14)
)
ciscoSystemExtSwFailureGroup3.setObjects(
    ("CISCO-SYSTEM-EXT-MIB", "cseSwCoresFileName")
)
if mibBuilder.loadTexts:
    ciscoSystemExtSwFailureGroup3.setStatus("current")

ciscoSystemExtSwFailureControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 2, 15)
)
ciscoSystemExtSwFailureControlGroup.setObjects(
    ("CISCO-SYSTEM-EXT-MIB", "ciscoSwFailureNotifEnable")
)
if mibBuilder.loadTexts:
    ciscoSystemExtSwFailureControlGroup.setStatus("current")

ciscoSystemExtInfoFIPSGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 2, 16)
)
ciscoSystemExtInfoFIPSGroup.setObjects(
    ("CISCO-SYSTEM-EXT-MIB", "cseSysFIPSModeActivation")
)
if mibBuilder.loadTexts:
    ciscoSystemExtInfoFIPSGroup.setStatus("current")

ciscoSystemExtInfoGroupRev3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 2, 17)
)
ciscoSystemExtInfoGroupRev3.setObjects(
      *(("CISCO-SYSTEM-EXT-MIB", "cseSysCPUUtilization"),
        ("CISCO-SYSTEM-EXT-MIB", "cseSysMemoryUtilization"),
        ("CISCO-SYSTEM-EXT-MIB", "cseSysConfLastChange"),
        ("CISCO-SYSTEM-EXT-MIB", "cseSysAutoSync"),
        ("CISCO-SYSTEM-EXT-MIB", "cseSysAutoSyncState"),
        ("CISCO-SYSTEM-EXT-MIB", "cseSysUpTime"))
)
if mibBuilder.loadTexts:
    ciscoSystemExtInfoGroupRev3.setStatus("current")

ciscoSystemSwitchingModeObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 2, 18)
)
ciscoSystemSwitchingModeObjectsGroup.setObjects(
      *(("CISCO-SYSTEM-EXT-MIB", "ciscoSystemSwitchingModeAdmin"),
        ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemSwitchingModeOper"))
)
if mibBuilder.loadTexts:
    ciscoSystemSwitchingModeObjectsGroup.setStatus("current")

ciscoSystemMaintModeObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 2, 19)
)
ciscoSystemMaintModeObjectsGroup.setObjects(
      *(("CISCO-SYSTEM-EXT-MIB", "cseMaintModeState"),
        ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemNormalModeNotifEnable"),
        ("CISCO-SYSTEM-EXT-MIB", "ciscoSystemMaintModeNotifEnable"))
)
if mibBuilder.loadTexts:
    ciscoSystemMaintModeObjectsGroup.setStatus("current")

ciscoSystemReloadObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 2, 21)
)
ciscoSystemReloadObjectsGroup.setObjects(
    ("CISCO-SYSTEM-EXT-MIB", "cseSystemReloadPending")
)
if mibBuilder.loadTexts:
    ciscoSystemReloadObjectsGroup.setStatus("current")


# Notification objects

cseHaRestartNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 3, 5, 0, 1)
)
cseHaRestartNotify.setObjects(
      *(("CISCO-SYSTEM-EXT-MIB", "cseHaRestartReason"),
        ("CISCO-SYSTEM-EXT-MIB", "cseHaRestartService"),
        ("CISCO-SYSTEM-EXT-MIB", "cseHaRestartStateless"))
)
if mibBuilder.loadTexts:
    cseHaRestartNotify.setStatus(
        "current"
    )

cseShutDownNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 3, 5, 0, 2)
)
cseShutDownNotify.setObjects(
    ("CISCO-SYSTEM-EXT-MIB", "cseHaShutDownReason")
)
if mibBuilder.loadTexts:
    cseShutDownNotify.setStatus(
        "current"
    )

cseFailSwCoreNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 4, 3, 0, 1)
)
if mibBuilder.loadTexts:
    cseFailSwCoreNotify.setStatus(
        "current"
    )

cseFailSwCoreNotifyExtended = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 4, 3, 0, 2)
)
cseFailSwCoreNotifyExtended.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CISCO-SYSTEM-EXT-MIB", "cseSwCoresFileName"),
        ("CISCO-SYSTEM-EXT-MIB", "cseSwCorePath"),
        ("CISCO-SYSTEM-EXT-MIB", "cseSwCoresPID"))
)
if mibBuilder.loadTexts:
    cseFailSwCoreNotifyExtended.setStatus(
        "current"
    )

cseNormalModeChangeNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 7, 2, 0, 1)
)
cseNormalModeChangeNotify.setObjects(
    ("CISCO-SYSTEM-EXT-MIB", "cseMaintModeState")
)
if mibBuilder.loadTexts:
    cseNormalModeChangeNotify.setStatus(
        "current"
    )

cseMaintModeChangeNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 1, 7, 2, 0, 2)
)
cseMaintModeChangeNotify.setObjects(
    ("CISCO-SYSTEM-EXT-MIB", "cseMaintModeState")
)
if mibBuilder.loadTexts:
    cseMaintModeChangeNotify.setStatus(
        "current"
    )


# Notifications groups

ciscoSystemExtNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 2, 4)
)
ciscoSystemExtNotificationGroup.setObjects(
    ("CISCO-SYSTEM-EXT-MIB", "cseHaRestartNotify")
)
if mibBuilder.loadTexts:
    ciscoSystemExtNotificationGroup.setStatus(
        "current"
    )

ciscoSystemExtNotificationGroupSup1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 2, 10)
)
ciscoSystemExtNotificationGroupSup1.setObjects(
      *(("CISCO-SYSTEM-EXT-MIB", "cseShutDownNotify"),
        ("CISCO-SYSTEM-EXT-MIB", "cseFailSwCoreNotify"))
)
if mibBuilder.loadTexts:
    ciscoSystemExtNotificationGroupSup1.setStatus(
        "current"
    )

ciscoSystemExtNotificationGroupSup2 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 2, 13)
)
ciscoSystemExtNotificationGroupSup2.setObjects(
    ("CISCO-SYSTEM-EXT-MIB", "cseFailSwCoreNotifyExtended")
)
if mibBuilder.loadTexts:
    ciscoSystemExtNotificationGroupSup2.setStatus(
        "current"
    )

ciscoSystemMaintModeNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 2, 20)
)
ciscoSystemMaintModeNotificationGroup.setObjects(
      *(("CISCO-SYSTEM-EXT-MIB", "cseNormalModeChangeNotify"),
        ("CISCO-SYSTEM-EXT-MIB", "cseMaintModeChangeNotify"))
)
if mibBuilder.loadTexts:
    ciscoSystemMaintModeNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoSystemExtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoSystemExtMIBCompliance.setStatus(
        "deprecated"
    )

ciscoSystemExtMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoSystemExtMIBComplianceRev1.setStatus(
        "deprecated"
    )

ciscoSystemExtMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoSystemExtMIBComplianceRev2.setStatus(
        "deprecated"
    )

ciscoSystemExtMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoSystemExtMIBComplianceRev3.setStatus(
        "deprecated"
    )

ciscoSystemExtMIBComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 1, 5)
)
if mibBuilder.loadTexts:
    ciscoSystemExtMIBComplianceRev4.setStatus(
        "deprecated"
    )

ciscoSystemExtMIBComplianceRev5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 1, 6)
)
if mibBuilder.loadTexts:
    ciscoSystemExtMIBComplianceRev5.setStatus(
        "deprecated"
    )

ciscoSystemExtMIBComplianceRev6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 1, 7)
)
if mibBuilder.loadTexts:
    ciscoSystemExtMIBComplianceRev6.setStatus(
        "deprecated"
    )

ciscoSystemExtMIBComplianceRev7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 1, 8)
)
if mibBuilder.loadTexts:
    ciscoSystemExtMIBComplianceRev7.setStatus(
        "deprecated"
    )

ciscoSystemExtMIBComplianceRev8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 1, 9)
)
if mibBuilder.loadTexts:
    ciscoSystemExtMIBComplianceRev8.setStatus(
        "deprecated"
    )

ciscoSystemExtMIBComplianceRev9 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 1, 11)
)
if mibBuilder.loadTexts:
    ciscoSystemExtMIBComplianceRev9.setStatus(
        "deprecated"
    )

ciscoSystemExtMIBComplianceRev10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 305, 2, 1, 12)
)
if mibBuilder.loadTexts:
    ciscoSystemExtMIBComplianceRev10.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SYSTEM-EXT-MIB",
    **{"CseHaRestartReason": CseHaRestartReason,
       "CiscoMaintModeState": CiscoMaintModeState,
       "ciscoSystemExtMIB": ciscoSystemExtMIB,
       "ciscoSystemExtMIBNotifsPrefix": ciscoSystemExtMIBNotifsPrefix,
       "ciscoSystemExtMIBObjects": ciscoSystemExtMIBObjects,
       "ciscoSysInfoGroup": ciscoSysInfoGroup,
       "cseSysCPUUtilization": cseSysCPUUtilization,
       "cseSysMemoryUtilization": cseSysMemoryUtilization,
       "cseSysConfLastChange": cseSysConfLastChange,
       "cseSysAutoSync": cseSysAutoSync,
       "cseSysAutoSyncState": cseSysAutoSyncState,
       "cseWriteErase": cseWriteErase,
       "cseSysConsolePortStatus": cseSysConsolePortStatus,
       "cseSysTelnetServiceActivation": cseSysTelnetServiceActivation,
       "cseSysFIPSModeActivation": cseSysFIPSModeActivation,
       "cseSysUpTime": cseSysUpTime,
       "ciscoSysErrorGroup": ciscoSysErrorGroup,
       "cseSnmpErrorTable": cseSnmpErrorTable,
       "cseSnmpErrorEntry": cseSnmpErrorEntry,
       "cseSnmpErrorAddressType": cseSnmpErrorAddressType,
       "cseSnmpErrorAddress": cseSnmpErrorAddress,
       "cseSnmpErrorRequestId": cseSnmpErrorRequestId,
       "cseSnmpErrorCode": cseSnmpErrorCode,
       "cseSnmpErrorDescription": cseSnmpErrorDescription,
       "ciscoHaGroup": ciscoHaGroup,
       "cseHaRestartReason": cseHaRestartReason,
       "cseHaRestartStateless": cseHaRestartStateless,
       "cseHaRestartService": cseHaRestartService,
       "cseHaNotification": cseHaNotification,
       "cseHaNotificationPrefix": cseHaNotificationPrefix,
       "cseHaRestartNotify": cseHaRestartNotify,
       "cseShutDownNotify": cseShutDownNotify,
       "cseHaShutDownReason": cseHaShutDownReason,
       "ciscoSwFailureGroup": ciscoSwFailureGroup,
       "cseSwCorePath": cseSwCorePath,
       "cseSwCoresTable": cseSwCoresTable,
       "cseSwCoresEntry": cseSwCoresEntry,
       "cseSwCoresModule": cseSwCoresModule,
       "cseSwCoresProcName": cseSwCoresProcName,
       "cseSwCoresInstance": cseSwCoresInstance,
       "cseSwCoresPID": cseSwCoresPID,
       "cseSwCoresTimeCreated": cseSwCoresTimeCreated,
       "cseSwCoresSlotNum": cseSwCoresSlotNum,
       "cseSwCoresFileName": cseSwCoresFileName,
       "cseFailNotification": cseFailNotification,
       "cseFailNotificationPrefix": cseFailNotificationPrefix,
       "cseFailSwCoreNotify": cseFailSwCoreNotify,
       "cseFailSwCoreNotifyExtended": cseFailSwCoreNotifyExtended,
       "ciscoSwFailureNotifControl": ciscoSwFailureNotifControl,
       "ciscoSwFailureNotifEnable": ciscoSwFailureNotifEnable,
       "ciscoSystemSwitchingModeGroup": ciscoSystemSwitchingModeGroup,
       "ciscoSystemSwitchingModeAdmin": ciscoSystemSwitchingModeAdmin,
       "ciscoSystemSwitchingModeOper": ciscoSystemSwitchingModeOper,
       "ciscoSystemMaintModeGroup": ciscoSystemMaintModeGroup,
       "cseMaintModeState": cseMaintModeState,
       "cseMaintModeNotification": cseMaintModeNotification,
       "cseMaintModeNotificationPrefix": cseMaintModeNotificationPrefix,
       "cseNormalModeChangeNotify": cseNormalModeChangeNotify,
       "cseMaintModeChangeNotify": cseMaintModeChangeNotify,
       "ciscoSystemMaintModeNotifControl": ciscoSystemMaintModeNotifControl,
       "ciscoSystemNormalModeNotifEnable": ciscoSystemNormalModeNotifEnable,
       "ciscoSystemMaintModeNotifEnable": ciscoSystemMaintModeNotifEnable,
       "ciscoSystemReloadGroup": ciscoSystemReloadGroup,
       "cseSystemReloadPending": cseSystemReloadPending,
       "ciscoSystemExtMIBConformance": ciscoSystemExtMIBConformance,
       "ciscoSystemExtMIBCompliances": ciscoSystemExtMIBCompliances,
       "ciscoSystemExtMIBCompliance": ciscoSystemExtMIBCompliance,
       "ciscoSystemExtMIBComplianceRev1": ciscoSystemExtMIBComplianceRev1,
       "ciscoSystemExtMIBComplianceRev2": ciscoSystemExtMIBComplianceRev2,
       "ciscoSystemExtMIBComplianceRev3": ciscoSystemExtMIBComplianceRev3,
       "ciscoSystemExtMIBComplianceRev4": ciscoSystemExtMIBComplianceRev4,
       "ciscoSystemExtMIBComplianceRev5": ciscoSystemExtMIBComplianceRev5,
       "ciscoSystemExtMIBComplianceRev6": ciscoSystemExtMIBComplianceRev6,
       "ciscoSystemExtMIBComplianceRev7": ciscoSystemExtMIBComplianceRev7,
       "ciscoSystemExtMIBComplianceRev8": ciscoSystemExtMIBComplianceRev8,
       "ciscoSystemExtMIBComplianceRev9": ciscoSystemExtMIBComplianceRev9,
       "ciscoSystemExtMIBComplianceRev10": ciscoSystemExtMIBComplianceRev10,
       "ciscoSystemExtMIBGroups": ciscoSystemExtMIBGroups,
       "ciscoSystemExtInfoGroup": ciscoSystemExtInfoGroup,
       "ciscoSystemExtErrorGroup": ciscoSystemExtErrorGroup,
       "ciscoSystemExtHaGroup": ciscoSystemExtHaGroup,
       "ciscoSystemExtNotificationGroup": ciscoSystemExtNotificationGroup,
       "ciscoSystemExtInfoGroupRev1": ciscoSystemExtInfoGroupRev1,
       "ciscoSystemExtInfoGroupOptional": ciscoSystemExtInfoGroupOptional,
       "ciscoSystemExtSwFailureGroup": ciscoSystemExtSwFailureGroup,
       "ciscoSystemExtInfoGroupRev2": ciscoSystemExtInfoGroupRev2,
       "ciscoSystemExtSwFailureGroup2": ciscoSystemExtSwFailureGroup2,
       "ciscoSystemExtNotificationGroupSup1": ciscoSystemExtNotificationGroupSup1,
       "ciscoSystemExtHaGroupRev1": ciscoSystemExtHaGroupRev1,
       "ciscoSystemExtInfoTelnetGroup": ciscoSystemExtInfoTelnetGroup,
       "ciscoSystemExtNotificationGroupSup2": ciscoSystemExtNotificationGroupSup2,
       "ciscoSystemExtSwFailureGroup3": ciscoSystemExtSwFailureGroup3,
       "ciscoSystemExtSwFailureControlGroup": ciscoSystemExtSwFailureControlGroup,
       "ciscoSystemExtInfoFIPSGroup": ciscoSystemExtInfoFIPSGroup,
       "ciscoSystemExtInfoGroupRev3": ciscoSystemExtInfoGroupRev3,
       "ciscoSystemSwitchingModeObjectsGroup": ciscoSystemSwitchingModeObjectsGroup,
       "ciscoSystemMaintModeObjectsGroup": ciscoSystemMaintModeObjectsGroup,
       "ciscoSystemMaintModeNotificationGroup": ciscoSystemMaintModeNotificationGroup,
       "ciscoSystemReloadObjectsGroup": ciscoSystemReloadObjectsGroup}
)
