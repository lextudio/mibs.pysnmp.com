# SNMP MIB module (TIMETRA-SAS-LOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TIMETRA-SAS-LOG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:04:25 2024
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,
 SnmpMessageProcessingModel,
 SnmpSecurityLevel) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString",
    "SnmpMessageProcessingModel",
    "SnmpSecurityLevel")

(snmpNotifyEntry,) = mibBuilder.importSymbols(
    "SNMP-NOTIFICATION-MIB",
    "snmpNotifyEntry")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysDescr,
 sysObjectID) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysDescr",
    "sysObjectID")

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
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(TFilterAction,
 TFilterActionOrDefault) = mibBuilder.importSymbols(
    "TIMETRA-FILTER-MIB",
    "TFilterAction",
    "TFilterActionOrDefault")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(TmnxLogIdIndex,
 tmnxLogApEntry,
 tmnxSnmpTrapDestEntry) = mibBuilder.importSymbols(
    "TIMETRA-LOG-MIB",
    "TmnxLogIdIndex",
    "tmnxLogApEntry",
    "tmnxSnmpTrapDestEntry")

(timetraSASConfs,
 timetraSASModules,
 timetraSASNotifyPrefix,
 timetraSASObjs) = mibBuilder.importSymbols(
    "TIMETRA-SAS-GLOBAL-MIB",
    "timetraSASConfs",
    "timetraSASModules",
    "timetraSASNotifyPrefix",
    "timetraSASObjs")

(THsmdaCounterIdOrZero,
 THsmdaCounterIdOrZeroOrAll,
 TItemDescription,
 TNamedItem,
 TNamedItemOrEmpty,
 TQueueId,
 TQueueIdOrAll,
 TmnxAccPlcyAACounters,
 TmnxAccPlcyOECounters,
 TmnxAccPlcyOICounters,
 TmnxAccPlcyQECounters,
 TmnxAccPlcyQICounters,
 TmnxActionType,
 TmnxAdminState,
 TmnxOperState) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "THsmdaCounterIdOrZero",
    "THsmdaCounterIdOrZeroOrAll",
    "TItemDescription",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TQueueId",
    "TQueueIdOrAll",
    "TmnxAccPlcyAACounters",
    "TmnxAccPlcyOECounters",
    "TmnxAccPlcyOICounters",
    "TmnxAccPlcyQECounters",
    "TmnxAccPlcyQICounters",
    "TmnxActionType",
    "TmnxAdminState",
    "TmnxOperState")


# MODULE-IDENTITY

timetraSASLogMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 1, 14)
)
timetraSASLogMIBModule.setRevisions(
        ("1911-08-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TLogMemSize(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )



# MIB Managed Objects in the order of their OIDs

_TmnxSASLogConformance_ObjectIdentity = ObjectIdentity
tmnxSASLogConformance = _TmnxSASLogConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 9)
)
_TmnxSASLogGroups_ObjectIdentity = ObjectIdentity
tmnxSASLogGroups = _TmnxSASLogGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 9, 1)
)
_TmnxSASLogObjs_ObjectIdentity = ObjectIdentity
tmnxSASLogObjs = _TmnxSASLogObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 14)
)
_TmnxSASLogGlobObjs_ObjectIdentity = ObjectIdentity
tmnxSASLogGlobObjs = _TmnxSASLogGlobObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 14, 1)
)


class _TmnxDygGaspPriLogId_Type(Integer32):
    """Custom type tmnxDygGaspPriLogId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxDygGaspPriLogId_Type.__name__ = "Integer32"
_TmnxDygGaspPriLogId_Object = MibScalar
tmnxDygGaspPriLogId = _TmnxDygGaspPriLogId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 14, 1, 1),
    _TmnxDygGaspPriLogId_Type()
)
tmnxDygGaspPriLogId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxDygGaspPriLogId.setStatus("current")


class _TmnxDygGaspPriTgtName_Type(SnmpAdminString):
    """Custom type tmnxDygGaspPriTgtName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 28),
    )


_TmnxDygGaspPriTgtName_Type.__name__ = "SnmpAdminString"
_TmnxDygGaspPriTgtName_Object = MibScalar
tmnxDygGaspPriTgtName = _TmnxDygGaspPriTgtName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 14, 1, 2),
    _TmnxDygGaspPriTgtName_Type()
)
tmnxDygGaspPriTgtName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxDygGaspPriTgtName.setStatus("current")


class _TmnxDygGaspSecLogId_Type(Integer32):
    """Custom type tmnxDygGaspSecLogId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxDygGaspSecLogId_Type.__name__ = "Integer32"
_TmnxDygGaspSecLogId_Object = MibScalar
tmnxDygGaspSecLogId = _TmnxDygGaspSecLogId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 14, 1, 3),
    _TmnxDygGaspSecLogId_Type()
)
tmnxDygGaspSecLogId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxDygGaspSecLogId.setStatus("current")


class _TmnxDygGaspSecTgtName_Type(SnmpAdminString):
    """Custom type tmnxDygGaspSecTgtName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 28),
    )


_TmnxDygGaspSecTgtName_Type.__name__ = "SnmpAdminString"
_TmnxDygGaspSecTgtName_Object = MibScalar
tmnxDygGaspSecTgtName = _TmnxDygGaspSecTgtName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 14, 1, 4),
    _TmnxDygGaspSecTgtName_Type()
)
tmnxDygGaspSecTgtName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxDygGaspSecTgtName.setStatus("current")


class _TmnxDygGaspTerLogId_Type(Integer32):
    """Custom type tmnxDygGaspTerLogId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TmnxDygGaspTerLogId_Type.__name__ = "Integer32"
_TmnxDygGaspTerLogId_Object = MibScalar
tmnxDygGaspTerLogId = _TmnxDygGaspTerLogId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 14, 1, 5),
    _TmnxDygGaspTerLogId_Type()
)
tmnxDygGaspTerLogId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxDygGaspTerLogId.setStatus("current")


class _TmnxDygGaspTerTgtName_Type(SnmpAdminString):
    """Custom type tmnxDygGaspTerTgtName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 28),
    )


_TmnxDygGaspTerTgtName_Type.__name__ = "SnmpAdminString"
_TmnxDygGaspTerTgtName_Object = MibScalar
tmnxDygGaspTerTgtName = _TmnxDygGaspTerTgtName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 14, 1, 6),
    _TmnxDygGaspTerTgtName_Type()
)
tmnxDygGaspTerTgtName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxDygGaspTerTgtName.setStatus("current")
_TmnxLogApExtnTable_Object = MibTable
tmnxLogApExtnTable = _TmnxLogApExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 14, 1, 7)
)
if mibBuilder.loadTexts:
    tmnxLogApExtnTable.setStatus("current")
_TmnxLogApExtnEntry_Object = MibTableRow
tmnxLogApExtnEntry = _TmnxLogApExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 14, 1, 7, 1)
)
if mibBuilder.loadTexts:
    tmnxLogApExtnEntry.setStatus("current")


class _TmnxLogApLogMemory_Type(TruthValue):
    """Custom type tmnxLogApLogMemory based on TruthValue"""


_TmnxLogApLogMemory_Object = MibTableColumn
tmnxLogApLogMemory = _TmnxLogApLogMemory_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 14, 1, 7, 1, 1),
    _TmnxLogApLogMemory_Type()
)
tmnxLogApLogMemory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxLogApLogMemory.setStatus("current")
_TmnxLogApLogMemSize_Type = TLogMemSize
_TmnxLogApLogMemSize_Object = MibTableColumn
tmnxLogApLogMemSize = _TmnxLogApLogMemSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 14, 1, 7, 1, 2),
    _TmnxLogApLogMemSize_Type()
)
tmnxLogApLogMemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxLogApLogMemSize.setStatus("current")
tmnxLogApEntry.registerAugmentions(
    ("TIMETRA-SAS-LOG-MIB",
     "tmnxLogApExtnEntry")
)
tmnxLogApExtnEntry.setIndexNames(*tmnxLogApEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-SAS-LOG-MIB",
    **{"TLogMemSize": TLogMemSize,
       "timetraSASLogMIBModule": timetraSASLogMIBModule,
       "tmnxSASLogConformance": tmnxSASLogConformance,
       "tmnxSASLogGroups": tmnxSASLogGroups,
       "tmnxSASLogObjs": tmnxSASLogObjs,
       "tmnxSASLogGlobObjs": tmnxSASLogGlobObjs,
       "tmnxDygGaspPriLogId": tmnxDygGaspPriLogId,
       "tmnxDygGaspPriTgtName": tmnxDygGaspPriTgtName,
       "tmnxDygGaspSecLogId": tmnxDygGaspSecLogId,
       "tmnxDygGaspSecTgtName": tmnxDygGaspSecTgtName,
       "tmnxDygGaspTerLogId": tmnxDygGaspTerLogId,
       "tmnxDygGaspTerTgtName": tmnxDygGaspTerTgtName,
       "tmnxLogApExtnTable": tmnxLogApExtnTable,
       "tmnxLogApExtnEntry": tmnxLogApExtnEntry,
       "tmnxLogApLogMemory": tmnxLogApLogMemory,
       "tmnxLogApLogMemSize": tmnxLogApLogMemSize}
)
