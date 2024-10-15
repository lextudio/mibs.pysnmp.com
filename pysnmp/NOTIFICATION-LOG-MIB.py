# SNMP MIB module (NOTIFICATION-LOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NOTIFICATION-LOG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:29:01 2024
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

(SnmpAdminString,
 SnmpEngineID) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString",
    "SnmpEngineID")

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
 Opaque,
 TimeTicks,
 Unsigned32,
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "Opaque",
    "TimeTicks",
    "Unsigned32",
    "iso",
    "mib-2")

(DateAndTime,
 DisplayString,
 RowStatus,
 StorageType,
 TAddress,
 TDomain,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TAddress",
    "TDomain",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

notificationLogMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 92)
)
notificationLogMIB.setRevisions(
        ("2000-11-27 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NotificationLogMIBObjects_ObjectIdentity = ObjectIdentity
notificationLogMIBObjects = _NotificationLogMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 92, 1)
)
_NlmConfig_ObjectIdentity = ObjectIdentity
nlmConfig = _NlmConfig_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 92, 1, 1)
)
_NlmConfigGlobalEntryLimit_Type = Unsigned32
_NlmConfigGlobalEntryLimit_Object = MibScalar
nlmConfigGlobalEntryLimit = _NlmConfigGlobalEntryLimit_Object(
    (1, 3, 6, 1, 2, 1, 92, 1, 1, 1),
    _NlmConfigGlobalEntryLimit_Type()
)
nlmConfigGlobalEntryLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlmConfigGlobalEntryLimit.setStatus("current")
_NlmConfigGlobalAgeOut_Type = Unsigned32
_NlmConfigGlobalAgeOut_Object = MibScalar
nlmConfigGlobalAgeOut = _NlmConfigGlobalAgeOut_Object(
    (1, 3, 6, 1, 2, 1, 92, 1, 1, 2),
    _NlmConfigGlobalAgeOut_Type()
)
nlmConfigGlobalAgeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nlmConfigGlobalAgeOut.setStatus("current")
if mibBuilder.loadTexts:
    nlmConfigGlobalAgeOut.setUnits("minutes")
_NlmConfigLogTable_Object = MibTable
nlmConfigLogTable = _NlmConfigLogTable_Object(
    (1, 3, 6, 1, 2, 1, 92, 1, 1, 3)
)
if mibBuilder.loadTexts:
    nlmConfigLogTable.setStatus("current")
_NlmConfigLogEntry_Object = MibTableRow
nlmConfigLogEntry = _NlmConfigLogEntry_Object(
    (1, 3, 6, 1, 2, 1, 92, 1, 1, 3, 1)
)
nlmConfigLogEntry.setIndexNames(
    (0, "NOTIFICATION-LOG-MIB", "nlmLogName"),
)
if mibBuilder.loadTexts:
    nlmConfigLogEntry.setStatus("current")


class _NlmLogName_Type(SnmpAdminString):
    """Custom type nlmLogName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NlmLogName_Type.__name__ = "SnmpAdminString"
_NlmLogName_Object = MibTableColumn
nlmLogName = _NlmLogName_Object(
    (1, 3, 6, 1, 2, 1, 92, 1, 1, 3, 1, 1),
    _NlmLogName_Type()
)
nlmLogName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nlmLogName.setStatus("current")


class _NlmConfigLogFilterName_Type(SnmpAdminString):
    """Custom type nlmConfigLogFilterName based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NlmConfigLogFilterName_Type.__name__ = "SnmpAdminString"
_NlmConfigLogFilterName_Object = MibTableColumn
nlmConfigLogFilterName = _NlmConfigLogFilterName_Object(
    (1, 3, 6, 1, 2, 1, 92, 1, 1, 3, 1, 2),
    _NlmConfigLogFilterName_Type()
)
nlmConfigLogFilterName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nlmConfigLogFilterName.setStatus("current")


class _NlmConfigLogEntryLimit_Type(Unsigned32):
    """Custom type nlmConfigLogEntryLimit based on Unsigned32"""
    defaultValue = 0


_NlmConfigLogEntryLimit_Object = MibTableColumn
nlmConfigLogEntryLimit = _NlmConfigLogEntryLimit_Object(
    (1, 3, 6, 1, 2, 1, 92, 1, 1, 3, 1, 3),
    _NlmConfigLogEntryLimit_Type()
)
nlmConfigLogEntryLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nlmConfigLogEntryLimit.setStatus("current")


class _NlmConfigLogAdminStatus_Type(Integer32):
    """Custom type nlmConfigLogAdminStatus based on Integer32"""
    defaultValue = 1

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


_NlmConfigLogAdminStatus_Type.__name__ = "Integer32"
_NlmConfigLogAdminStatus_Object = MibTableColumn
nlmConfigLogAdminStatus = _NlmConfigLogAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 92, 1, 1, 3, 1, 4),
    _NlmConfigLogAdminStatus_Type()
)
nlmConfigLogAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nlmConfigLogAdminStatus.setStatus("current")


class _NlmConfigLogOperStatus_Type(Integer32):
    """Custom type nlmConfigLogOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("noFilter", 3),
          ("operational", 2))
    )


_NlmConfigLogOperStatus_Type.__name__ = "Integer32"
_NlmConfigLogOperStatus_Object = MibTableColumn
nlmConfigLogOperStatus = _NlmConfigLogOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 92, 1, 1, 3, 1, 5),
    _NlmConfigLogOperStatus_Type()
)
nlmConfigLogOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlmConfigLogOperStatus.setStatus("current")
_NlmConfigLogStorageType_Type = StorageType
_NlmConfigLogStorageType_Object = MibTableColumn
nlmConfigLogStorageType = _NlmConfigLogStorageType_Object(
    (1, 3, 6, 1, 2, 1, 92, 1, 1, 3, 1, 6),
    _NlmConfigLogStorageType_Type()
)
nlmConfigLogStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nlmConfigLogStorageType.setStatus("current")
_NlmConfigLogEntryStatus_Type = RowStatus
_NlmConfigLogEntryStatus_Object = MibTableColumn
nlmConfigLogEntryStatus = _NlmConfigLogEntryStatus_Object(
    (1, 3, 6, 1, 2, 1, 92, 1, 1, 3, 1, 7),
    _NlmConfigLogEntryStatus_Type()
)
nlmConfigLogEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nlmConfigLogEntryStatus.setStatus("current")
_NlmStats_ObjectIdentity = ObjectIdentity
nlmStats = _NlmStats_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 92, 1, 2)
)
_NlmStatsGlobalNotificationsLogged_Type = Counter32
_NlmStatsGlobalNotificationsLogged_Object = MibScalar
nlmStatsGlobalNotificationsLogged = _NlmStatsGlobalNotificationsLogged_Object(
    (1, 3, 6, 1, 2, 1, 92, 1, 2, 1),
    _NlmStatsGlobalNotificationsLogged_Type()
)
nlmStatsGlobalNotificationsLogged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlmStatsGlobalNotificationsLogged.setStatus("current")
if mibBuilder.loadTexts:
    nlmStatsGlobalNotificationsLogged.setUnits("notifications")
_NlmStatsGlobalNotificationsBumped_Type = Counter32
_NlmStatsGlobalNotificationsBumped_Object = MibScalar
nlmStatsGlobalNotificationsBumped = _NlmStatsGlobalNotificationsBumped_Object(
    (1, 3, 6, 1, 2, 1, 92, 1, 2, 2),
    _NlmStatsGlobalNotificationsBumped_Type()
)
nlmStatsGlobalNotificationsBumped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlmStatsGlobalNotificationsBumped.setStatus("current")
if mibBuilder.loadTexts:
    nlmStatsGlobalNotificationsBumped.setUnits("notifications")
_NlmStatsLogTable_Object = MibTable
nlmStatsLogTable = _NlmStatsLogTable_Object(
    (1, 3, 6, 1, 2, 1, 92, 1, 2, 3)
)
if mibBuilder.loadTexts:
    nlmStatsLogTable.setStatus("current")
_NlmStatsLogEntry_Object = MibTableRow
nlmStatsLogEntry = _NlmStatsLogEntry_Object(
    (1, 3, 6, 1, 2, 1, 92, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    nlmStatsLogEntry.setStatus("current")
_NlmStatsLogNotificationsLogged_Type = Counter32
_NlmStatsLogNotificationsLogged_Object = MibTableColumn
nlmStatsLogNotificationsLogged = _NlmStatsLogNotificationsLogged_Object(
    (1, 3, 6, 1, 2, 1, 92, 1, 2, 3, 1, 1),
    _NlmStatsLogNotificationsLogged_Type()
)
nlmStatsLogNotificationsLogged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlmStatsLogNotificationsLogged.setStatus("current")
if mibBuilder.loadTexts:
    nlmStatsLogNotificationsLogged.setUnits("notifications")
_NlmStatsLogNotificationsBumped_Type = Counter32
_NlmStatsLogNotificationsBumped_Object = MibTableColumn
nlmStatsLogNotificationsBumped = _NlmStatsLogNotificationsBumped_Object(
    (1, 3, 6, 1, 2, 1, 92, 1, 2, 3, 1, 2),
    _NlmStatsLogNotificationsBumped_Type()
)
nlmStatsLogNotificationsBumped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlmStatsLogNotificationsBumped.setStatus("current")
if mibBuilder.loadTexts:
    nlmStatsLogNotificationsBumped.setUnits("notifications")
_NlmLog_ObjectIdentity = ObjectIdentity
nlmLog = _NlmLog_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 92, 1, 3)
)
_NlmLogTable_Object = MibTable
nlmLogTable = _NlmLogTable_Object(
    (1, 3, 6, 1, 2, 1, 92, 1, 3, 1)
)
if mibBuilder.loadTexts:
    nlmLogTable.setStatus("current")
_NlmLogEntry_Object = MibTableRow
nlmLogEntry = _NlmLogEntry_Object(
    (1, 3, 6, 1, 2, 1, 92, 1, 3, 1, 1)
)
nlmLogEntry.setIndexNames(
    (0, "NOTIFICATION-LOG-MIB", "nlmLogName"),
    (0, "NOTIFICATION-LOG-MIB", "nlmLogIndex"),
)
if mibBuilder.loadTexts:
    nlmLogEntry.setStatus("current")


class _NlmLogIndex_Type(Unsigned32):
    """Custom type nlmLogIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_NlmLogIndex_Type.__name__ = "Unsigned32"
_NlmLogIndex_Object = MibTableColumn
nlmLogIndex = _NlmLogIndex_Object(
    (1, 3, 6, 1, 2, 1, 92, 1, 3, 1, 1, 1),
    _NlmLogIndex_Type()
)
nlmLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nlmLogIndex.setStatus("current")
_NlmLogTime_Type = TimeStamp
_NlmLogTime_Object = MibTableColumn
nlmLogTime = _NlmLogTime_Object(
    (1, 3, 6, 1, 2, 1, 92, 1, 3, 1, 1, 2),
    _NlmLogTime_Type()
)
nlmLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlmLogTime.setStatus("current")
_NlmLogDateAndTime_Type = DateAndTime
_NlmLogDateAndTime_Object = MibTableColumn
nlmLogDateAndTime = _NlmLogDateAndTime_Object(
    (1, 3, 6, 1, 2, 1, 92, 1, 3, 1, 1, 3),
    _NlmLogDateAndTime_Type()
)
nlmLogDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlmLogDateAndTime.setStatus("current")
_NlmLogEngineID_Type = SnmpEngineID
_NlmLogEngineID_Object = MibTableColumn
nlmLogEngineID = _NlmLogEngineID_Object(
    (1, 3, 6, 1, 2, 1, 92, 1, 3, 1, 1, 4),
    _NlmLogEngineID_Type()
)
nlmLogEngineID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlmLogEngineID.setStatus("current")
_NlmLogEngineTAddress_Type = TAddress
_NlmLogEngineTAddress_Object = MibTableColumn
nlmLogEngineTAddress = _NlmLogEngineTAddress_Object(
    (1, 3, 6, 1, 2, 1, 92, 1, 3, 1, 1, 5),
    _NlmLogEngineTAddress_Type()
)
nlmLogEngineTAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlmLogEngineTAddress.setStatus("current")
_NlmLogEngineTDomain_Type = TDomain
_NlmLogEngineTDomain_Object = MibTableColumn
nlmLogEngineTDomain = _NlmLogEngineTDomain_Object(
    (1, 3, 6, 1, 2, 1, 92, 1, 3, 1, 1, 6),
    _NlmLogEngineTDomain_Type()
)
nlmLogEngineTDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlmLogEngineTDomain.setStatus("current")
_NlmLogContextEngineID_Type = SnmpEngineID
_NlmLogContextEngineID_Object = MibTableColumn
nlmLogContextEngineID = _NlmLogContextEngineID_Object(
    (1, 3, 6, 1, 2, 1, 92, 1, 3, 1, 1, 7),
    _NlmLogContextEngineID_Type()
)
nlmLogContextEngineID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlmLogContextEngineID.setStatus("current")
_NlmLogContextName_Type = SnmpAdminString
_NlmLogContextName_Object = MibTableColumn
nlmLogContextName = _NlmLogContextName_Object(
    (1, 3, 6, 1, 2, 1, 92, 1, 3, 1, 1, 8),
    _NlmLogContextName_Type()
)
nlmLogContextName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlmLogContextName.setStatus("current")
_NlmLogNotificationID_Type = ObjectIdentifier
_NlmLogNotificationID_Object = MibTableColumn
nlmLogNotificationID = _NlmLogNotificationID_Object(
    (1, 3, 6, 1, 2, 1, 92, 1, 3, 1, 1, 9),
    _NlmLogNotificationID_Type()
)
nlmLogNotificationID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlmLogNotificationID.setStatus("current")
_NlmLogVariableTable_Object = MibTable
nlmLogVariableTable = _NlmLogVariableTable_Object(
    (1, 3, 6, 1, 2, 1, 92, 1, 3, 2)
)
if mibBuilder.loadTexts:
    nlmLogVariableTable.setStatus("current")
_NlmLogVariableEntry_Object = MibTableRow
nlmLogVariableEntry = _NlmLogVariableEntry_Object(
    (1, 3, 6, 1, 2, 1, 92, 1, 3, 2, 1)
)
nlmLogVariableEntry.setIndexNames(
    (0, "NOTIFICATION-LOG-MIB", "nlmLogName"),
    (0, "NOTIFICATION-LOG-MIB", "nlmLogIndex"),
    (0, "NOTIFICATION-LOG-MIB", "nlmLogVariableIndex"),
)
if mibBuilder.loadTexts:
    nlmLogVariableEntry.setStatus("current")


class _NlmLogVariableIndex_Type(Unsigned32):
    """Custom type nlmLogVariableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_NlmLogVariableIndex_Type.__name__ = "Unsigned32"
_NlmLogVariableIndex_Object = MibTableColumn
nlmLogVariableIndex = _NlmLogVariableIndex_Object(
    (1, 3, 6, 1, 2, 1, 92, 1, 3, 2, 1, 1),
    _NlmLogVariableIndex_Type()
)
nlmLogVariableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nlmLogVariableIndex.setStatus("current")
_NlmLogVariableID_Type = ObjectIdentifier
_NlmLogVariableID_Object = MibTableColumn
nlmLogVariableID = _NlmLogVariableID_Object(
    (1, 3, 6, 1, 2, 1, 92, 1, 3, 2, 1, 2),
    _NlmLogVariableID_Type()
)
nlmLogVariableID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlmLogVariableID.setStatus("current")


class _NlmLogVariableValueType_Type(Integer32):
    """Custom type nlmLogVariableValueType based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("counter32", 1),
          ("counter64", 8),
          ("integer32", 4),
          ("ipAddress", 5),
          ("objectId", 7),
          ("octetString", 6),
          ("opaque", 9),
          ("timeTicks", 3),
          ("unsigned32", 2))
    )


_NlmLogVariableValueType_Type.__name__ = "Integer32"
_NlmLogVariableValueType_Object = MibTableColumn
nlmLogVariableValueType = _NlmLogVariableValueType_Object(
    (1, 3, 6, 1, 2, 1, 92, 1, 3, 2, 1, 3),
    _NlmLogVariableValueType_Type()
)
nlmLogVariableValueType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlmLogVariableValueType.setStatus("current")
_NlmLogVariableCounter32Val_Type = Counter32
_NlmLogVariableCounter32Val_Object = MibTableColumn
nlmLogVariableCounter32Val = _NlmLogVariableCounter32Val_Object(
    (1, 3, 6, 1, 2, 1, 92, 1, 3, 2, 1, 4),
    _NlmLogVariableCounter32Val_Type()
)
nlmLogVariableCounter32Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlmLogVariableCounter32Val.setStatus("current")
_NlmLogVariableUnsigned32Val_Type = Unsigned32
_NlmLogVariableUnsigned32Val_Object = MibTableColumn
nlmLogVariableUnsigned32Val = _NlmLogVariableUnsigned32Val_Object(
    (1, 3, 6, 1, 2, 1, 92, 1, 3, 2, 1, 5),
    _NlmLogVariableUnsigned32Val_Type()
)
nlmLogVariableUnsigned32Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlmLogVariableUnsigned32Val.setStatus("current")
_NlmLogVariableTimeTicksVal_Type = TimeTicks
_NlmLogVariableTimeTicksVal_Object = MibTableColumn
nlmLogVariableTimeTicksVal = _NlmLogVariableTimeTicksVal_Object(
    (1, 3, 6, 1, 2, 1, 92, 1, 3, 2, 1, 6),
    _NlmLogVariableTimeTicksVal_Type()
)
nlmLogVariableTimeTicksVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlmLogVariableTimeTicksVal.setStatus("current")
_NlmLogVariableInteger32Val_Type = Integer32
_NlmLogVariableInteger32Val_Object = MibTableColumn
nlmLogVariableInteger32Val = _NlmLogVariableInteger32Val_Object(
    (1, 3, 6, 1, 2, 1, 92, 1, 3, 2, 1, 7),
    _NlmLogVariableInteger32Val_Type()
)
nlmLogVariableInteger32Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlmLogVariableInteger32Val.setStatus("current")
_NlmLogVariableOctetStringVal_Type = OctetString
_NlmLogVariableOctetStringVal_Object = MibTableColumn
nlmLogVariableOctetStringVal = _NlmLogVariableOctetStringVal_Object(
    (1, 3, 6, 1, 2, 1, 92, 1, 3, 2, 1, 8),
    _NlmLogVariableOctetStringVal_Type()
)
nlmLogVariableOctetStringVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlmLogVariableOctetStringVal.setStatus("current")
_NlmLogVariableIpAddressVal_Type = IpAddress
_NlmLogVariableIpAddressVal_Object = MibTableColumn
nlmLogVariableIpAddressVal = _NlmLogVariableIpAddressVal_Object(
    (1, 3, 6, 1, 2, 1, 92, 1, 3, 2, 1, 9),
    _NlmLogVariableIpAddressVal_Type()
)
nlmLogVariableIpAddressVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlmLogVariableIpAddressVal.setStatus("current")
_NlmLogVariableOidVal_Type = ObjectIdentifier
_NlmLogVariableOidVal_Object = MibTableColumn
nlmLogVariableOidVal = _NlmLogVariableOidVal_Object(
    (1, 3, 6, 1, 2, 1, 92, 1, 3, 2, 1, 10),
    _NlmLogVariableOidVal_Type()
)
nlmLogVariableOidVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlmLogVariableOidVal.setStatus("current")
_NlmLogVariableCounter64Val_Type = Counter64
_NlmLogVariableCounter64Val_Object = MibTableColumn
nlmLogVariableCounter64Val = _NlmLogVariableCounter64Val_Object(
    (1, 3, 6, 1, 2, 1, 92, 1, 3, 2, 1, 11),
    _NlmLogVariableCounter64Val_Type()
)
nlmLogVariableCounter64Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlmLogVariableCounter64Val.setStatus("current")
_NlmLogVariableOpaqueVal_Type = Opaque
_NlmLogVariableOpaqueVal_Object = MibTableColumn
nlmLogVariableOpaqueVal = _NlmLogVariableOpaqueVal_Object(
    (1, 3, 6, 1, 2, 1, 92, 1, 3, 2, 1, 12),
    _NlmLogVariableOpaqueVal_Type()
)
nlmLogVariableOpaqueVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nlmLogVariableOpaqueVal.setStatus("current")
_NotificationLogMIBConformance_ObjectIdentity = ObjectIdentity
notificationLogMIBConformance = _NotificationLogMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 92, 3)
)
_NotificationLogMIBCompliances_ObjectIdentity = ObjectIdentity
notificationLogMIBCompliances = _NotificationLogMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 92, 3, 1)
)
_NotificationLogMIBGroups_ObjectIdentity = ObjectIdentity
notificationLogMIBGroups = _NotificationLogMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 92, 3, 2)
)
nlmConfigLogEntry.registerAugmentions(
    ("NOTIFICATION-LOG-MIB",
     "nlmStatsLogEntry")
)
nlmStatsLogEntry.setIndexNames(*nlmConfigLogEntry.getIndexNames())

# Managed Objects groups

notificationLogConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 92, 3, 2, 1)
)
notificationLogConfigGroup.setObjects(
      *(("NOTIFICATION-LOG-MIB", "nlmConfigGlobalEntryLimit"),
        ("NOTIFICATION-LOG-MIB", "nlmConfigGlobalAgeOut"),
        ("NOTIFICATION-LOG-MIB", "nlmConfigLogFilterName"),
        ("NOTIFICATION-LOG-MIB", "nlmConfigLogEntryLimit"),
        ("NOTIFICATION-LOG-MIB", "nlmConfigLogAdminStatus"),
        ("NOTIFICATION-LOG-MIB", "nlmConfigLogOperStatus"),
        ("NOTIFICATION-LOG-MIB", "nlmConfigLogStorageType"),
        ("NOTIFICATION-LOG-MIB", "nlmConfigLogEntryStatus"))
)
if mibBuilder.loadTexts:
    notificationLogConfigGroup.setStatus("current")

notificationLogStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 92, 3, 2, 2)
)
notificationLogStatsGroup.setObjects(
      *(("NOTIFICATION-LOG-MIB", "nlmStatsGlobalNotificationsLogged"),
        ("NOTIFICATION-LOG-MIB", "nlmStatsGlobalNotificationsBumped"),
        ("NOTIFICATION-LOG-MIB", "nlmStatsLogNotificationsLogged"),
        ("NOTIFICATION-LOG-MIB", "nlmStatsLogNotificationsBumped"))
)
if mibBuilder.loadTexts:
    notificationLogStatsGroup.setStatus("current")

notificationLogLogGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 92, 3, 2, 3)
)
notificationLogLogGroup.setObjects(
      *(("NOTIFICATION-LOG-MIB", "nlmLogTime"),
        ("NOTIFICATION-LOG-MIB", "nlmLogEngineID"),
        ("NOTIFICATION-LOG-MIB", "nlmLogEngineTAddress"),
        ("NOTIFICATION-LOG-MIB", "nlmLogEngineTDomain"),
        ("NOTIFICATION-LOG-MIB", "nlmLogContextEngineID"),
        ("NOTIFICATION-LOG-MIB", "nlmLogContextName"),
        ("NOTIFICATION-LOG-MIB", "nlmLogNotificationID"),
        ("NOTIFICATION-LOG-MIB", "nlmLogVariableID"),
        ("NOTIFICATION-LOG-MIB", "nlmLogVariableValueType"),
        ("NOTIFICATION-LOG-MIB", "nlmLogVariableCounter32Val"),
        ("NOTIFICATION-LOG-MIB", "nlmLogVariableUnsigned32Val"),
        ("NOTIFICATION-LOG-MIB", "nlmLogVariableTimeTicksVal"),
        ("NOTIFICATION-LOG-MIB", "nlmLogVariableInteger32Val"),
        ("NOTIFICATION-LOG-MIB", "nlmLogVariableOctetStringVal"),
        ("NOTIFICATION-LOG-MIB", "nlmLogVariableIpAddressVal"),
        ("NOTIFICATION-LOG-MIB", "nlmLogVariableOidVal"),
        ("NOTIFICATION-LOG-MIB", "nlmLogVariableCounter64Val"),
        ("NOTIFICATION-LOG-MIB", "nlmLogVariableOpaqueVal"))
)
if mibBuilder.loadTexts:
    notificationLogLogGroup.setStatus("current")

notificationLogDateGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 92, 3, 2, 4)
)
notificationLogDateGroup.setObjects(
    ("NOTIFICATION-LOG-MIB", "nlmLogDateAndTime")
)
if mibBuilder.loadTexts:
    notificationLogDateGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

notificationLogMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 92, 3, 1, 1)
)
if mibBuilder.loadTexts:
    notificationLogMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NOTIFICATION-LOG-MIB",
    **{"notificationLogMIB": notificationLogMIB,
       "notificationLogMIBObjects": notificationLogMIBObjects,
       "nlmConfig": nlmConfig,
       "nlmConfigGlobalEntryLimit": nlmConfigGlobalEntryLimit,
       "nlmConfigGlobalAgeOut": nlmConfigGlobalAgeOut,
       "nlmConfigLogTable": nlmConfigLogTable,
       "nlmConfigLogEntry": nlmConfigLogEntry,
       "nlmLogName": nlmLogName,
       "nlmConfigLogFilterName": nlmConfigLogFilterName,
       "nlmConfigLogEntryLimit": nlmConfigLogEntryLimit,
       "nlmConfigLogAdminStatus": nlmConfigLogAdminStatus,
       "nlmConfigLogOperStatus": nlmConfigLogOperStatus,
       "nlmConfigLogStorageType": nlmConfigLogStorageType,
       "nlmConfigLogEntryStatus": nlmConfigLogEntryStatus,
       "nlmStats": nlmStats,
       "nlmStatsGlobalNotificationsLogged": nlmStatsGlobalNotificationsLogged,
       "nlmStatsGlobalNotificationsBumped": nlmStatsGlobalNotificationsBumped,
       "nlmStatsLogTable": nlmStatsLogTable,
       "nlmStatsLogEntry": nlmStatsLogEntry,
       "nlmStatsLogNotificationsLogged": nlmStatsLogNotificationsLogged,
       "nlmStatsLogNotificationsBumped": nlmStatsLogNotificationsBumped,
       "nlmLog": nlmLog,
       "nlmLogTable": nlmLogTable,
       "nlmLogEntry": nlmLogEntry,
       "nlmLogIndex": nlmLogIndex,
       "nlmLogTime": nlmLogTime,
       "nlmLogDateAndTime": nlmLogDateAndTime,
       "nlmLogEngineID": nlmLogEngineID,
       "nlmLogEngineTAddress": nlmLogEngineTAddress,
       "nlmLogEngineTDomain": nlmLogEngineTDomain,
       "nlmLogContextEngineID": nlmLogContextEngineID,
       "nlmLogContextName": nlmLogContextName,
       "nlmLogNotificationID": nlmLogNotificationID,
       "nlmLogVariableTable": nlmLogVariableTable,
       "nlmLogVariableEntry": nlmLogVariableEntry,
       "nlmLogVariableIndex": nlmLogVariableIndex,
       "nlmLogVariableID": nlmLogVariableID,
       "nlmLogVariableValueType": nlmLogVariableValueType,
       "nlmLogVariableCounter32Val": nlmLogVariableCounter32Val,
       "nlmLogVariableUnsigned32Val": nlmLogVariableUnsigned32Val,
       "nlmLogVariableTimeTicksVal": nlmLogVariableTimeTicksVal,
       "nlmLogVariableInteger32Val": nlmLogVariableInteger32Val,
       "nlmLogVariableOctetStringVal": nlmLogVariableOctetStringVal,
       "nlmLogVariableIpAddressVal": nlmLogVariableIpAddressVal,
       "nlmLogVariableOidVal": nlmLogVariableOidVal,
       "nlmLogVariableCounter64Val": nlmLogVariableCounter64Val,
       "nlmLogVariableOpaqueVal": nlmLogVariableOpaqueVal,
       "notificationLogMIBConformance": notificationLogMIBConformance,
       "notificationLogMIBCompliances": notificationLogMIBCompliances,
       "notificationLogMIBCompliance": notificationLogMIBCompliance,
       "notificationLogMIBGroups": notificationLogMIBGroups,
       "notificationLogConfigGroup": notificationLogConfigGroup,
       "notificationLogStatsGroup": notificationLogStatsGroup,
       "notificationLogLogGroup": notificationLogLogGroup,
       "notificationLogDateGroup": notificationLogDateGroup}
)
