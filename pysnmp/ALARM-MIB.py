# SNMP MIB module (ALARM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALARM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:35:29 2024
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

(ZeroBasedCounter32,) = mibBuilder.importSymbols(
    "RMON2-MIB",
    "ZeroBasedCounter32")

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
 Opaque,
 TimeTicks,
 Unsigned32,
 iso,
 mib_2,
 zeroDotZero) = mibBuilder.importSymbols(
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
    "mib-2",
    "zeroDotZero")

(DateAndTime,
 DisplayString,
 RowPointer,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowPointer",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

alarmMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 118)
)
alarmMIB.setRevisions(
        ("2004-09-09 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ResourceId(ObjectIdentifier, TextualConvention):
    status = "current"


class LocalSnmpEngineOrZeroLenStr(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(5, 32),
    )



# MIB Managed Objects in the order of their OIDs

_AlarmNotifications_ObjectIdentity = ObjectIdentity
alarmNotifications = _AlarmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 118, 0)
)
_AlarmObjects_ObjectIdentity = ObjectIdentity
alarmObjects = _AlarmObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 118, 1)
)
_AlarmModel_ObjectIdentity = ObjectIdentity
alarmModel = _AlarmModel_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 118, 1, 1)
)
_AlarmModelLastChanged_Type = TimeTicks
_AlarmModelLastChanged_Object = MibScalar
alarmModelLastChanged = _AlarmModelLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 118, 1, 1, 1),
    _AlarmModelLastChanged_Type()
)
alarmModelLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmModelLastChanged.setStatus("current")
_AlarmModelTable_Object = MibTable
alarmModelTable = _AlarmModelTable_Object(
    (1, 3, 6, 1, 2, 1, 118, 1, 1, 2)
)
if mibBuilder.loadTexts:
    alarmModelTable.setStatus("current")
_AlarmModelEntry_Object = MibTableRow
alarmModelEntry = _AlarmModelEntry_Object(
    (1, 3, 6, 1, 2, 1, 118, 1, 1, 2, 1)
)
alarmModelEntry.setIndexNames(
    (0, "ALARM-MIB", "alarmListName"),
    (0, "ALARM-MIB", "alarmModelIndex"),
    (0, "ALARM-MIB", "alarmModelState"),
)
if mibBuilder.loadTexts:
    alarmModelEntry.setStatus("current")


class _AlarmModelIndex_Type(Unsigned32):
    """Custom type alarmModelIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_AlarmModelIndex_Type.__name__ = "Unsigned32"
_AlarmModelIndex_Object = MibTableColumn
alarmModelIndex = _AlarmModelIndex_Object(
    (1, 3, 6, 1, 2, 1, 118, 1, 1, 2, 1, 1),
    _AlarmModelIndex_Type()
)
alarmModelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alarmModelIndex.setStatus("current")


class _AlarmModelState_Type(Unsigned32):
    """Custom type alarmModelState based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_AlarmModelState_Type.__name__ = "Unsigned32"
_AlarmModelState_Object = MibTableColumn
alarmModelState = _AlarmModelState_Object(
    (1, 3, 6, 1, 2, 1, 118, 1, 1, 2, 1, 2),
    _AlarmModelState_Type()
)
alarmModelState.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alarmModelState.setStatus("current")


class _AlarmModelNotificationId_Type(ObjectIdentifier):
    """Custom type alarmModelNotificationId based on ObjectIdentifier"""
    defaultValue = (0, 0)


_AlarmModelNotificationId_Object = MibTableColumn
alarmModelNotificationId = _AlarmModelNotificationId_Object(
    (1, 3, 6, 1, 2, 1, 118, 1, 1, 2, 1, 3),
    _AlarmModelNotificationId_Type()
)
alarmModelNotificationId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alarmModelNotificationId.setStatus("current")


class _AlarmModelVarbindIndex_Type(Unsigned32):
    """Custom type alarmModelVarbindIndex based on Unsigned32"""
    defaultValue = 0


_AlarmModelVarbindIndex_Object = MibTableColumn
alarmModelVarbindIndex = _AlarmModelVarbindIndex_Object(
    (1, 3, 6, 1, 2, 1, 118, 1, 1, 2, 1, 4),
    _AlarmModelVarbindIndex_Type()
)
alarmModelVarbindIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alarmModelVarbindIndex.setStatus("current")


class _AlarmModelVarbindValue_Type(Integer32):
    """Custom type alarmModelVarbindValue based on Integer32"""
    defaultValue = 0


_AlarmModelVarbindValue_Object = MibTableColumn
alarmModelVarbindValue = _AlarmModelVarbindValue_Object(
    (1, 3, 6, 1, 2, 1, 118, 1, 1, 2, 1, 5),
    _AlarmModelVarbindValue_Type()
)
alarmModelVarbindValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alarmModelVarbindValue.setStatus("current")
_AlarmModelDescription_Type = SnmpAdminString
_AlarmModelDescription_Object = MibTableColumn
alarmModelDescription = _AlarmModelDescription_Object(
    (1, 3, 6, 1, 2, 1, 118, 1, 1, 2, 1, 6),
    _AlarmModelDescription_Type()
)
alarmModelDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alarmModelDescription.setStatus("current")


class _AlarmModelSpecificPointer_Type(RowPointer):
    """Custom type alarmModelSpecificPointer based on RowPointer"""
    defaultValue = (0, 0)


_AlarmModelSpecificPointer_Object = MibTableColumn
alarmModelSpecificPointer = _AlarmModelSpecificPointer_Object(
    (1, 3, 6, 1, 2, 1, 118, 1, 1, 2, 1, 7),
    _AlarmModelSpecificPointer_Type()
)
alarmModelSpecificPointer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alarmModelSpecificPointer.setStatus("current")


class _AlarmModelVarbindSubtree_Type(ObjectIdentifier):
    """Custom type alarmModelVarbindSubtree based on ObjectIdentifier"""
    defaultValue = (0, 0)


_AlarmModelVarbindSubtree_Object = MibTableColumn
alarmModelVarbindSubtree = _AlarmModelVarbindSubtree_Object(
    (1, 3, 6, 1, 2, 1, 118, 1, 1, 2, 1, 8),
    _AlarmModelVarbindSubtree_Type()
)
alarmModelVarbindSubtree.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alarmModelVarbindSubtree.setStatus("current")


class _AlarmModelResourcePrefix_Type(ObjectIdentifier):
    """Custom type alarmModelResourcePrefix based on ObjectIdentifier"""
    defaultValue = (0, 0)


_AlarmModelResourcePrefix_Object = MibTableColumn
alarmModelResourcePrefix = _AlarmModelResourcePrefix_Object(
    (1, 3, 6, 1, 2, 1, 118, 1, 1, 2, 1, 9),
    _AlarmModelResourcePrefix_Type()
)
alarmModelResourcePrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alarmModelResourcePrefix.setStatus("current")
_AlarmModelRowStatus_Type = RowStatus
_AlarmModelRowStatus_Object = MibTableColumn
alarmModelRowStatus = _AlarmModelRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 118, 1, 1, 2, 1, 10),
    _AlarmModelRowStatus_Type()
)
alarmModelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alarmModelRowStatus.setStatus("current")
_AlarmActive_ObjectIdentity = ObjectIdentity
alarmActive = _AlarmActive_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 118, 1, 2)
)
_AlarmActiveLastChanged_Type = TimeTicks
_AlarmActiveLastChanged_Object = MibScalar
alarmActiveLastChanged = _AlarmActiveLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 118, 1, 2, 1),
    _AlarmActiveLastChanged_Type()
)
alarmActiveLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmActiveLastChanged.setStatus("current")
_AlarmActiveTable_Object = MibTable
alarmActiveTable = _AlarmActiveTable_Object(
    (1, 3, 6, 1, 2, 1, 118, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alarmActiveTable.setStatus("current")
_AlarmActiveEntry_Object = MibTableRow
alarmActiveEntry = _AlarmActiveEntry_Object(
    (1, 3, 6, 1, 2, 1, 118, 1, 2, 2, 1)
)
alarmActiveEntry.setIndexNames(
    (0, "ALARM-MIB", "alarmListName"),
    (0, "ALARM-MIB", "alarmActiveDateAndTime"),
    (0, "ALARM-MIB", "alarmActiveIndex"),
)
if mibBuilder.loadTexts:
    alarmActiveEntry.setStatus("current")


class _AlarmListName_Type(SnmpAdminString):
    """Custom type alarmListName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlarmListName_Type.__name__ = "SnmpAdminString"
_AlarmListName_Object = MibTableColumn
alarmListName = _AlarmListName_Object(
    (1, 3, 6, 1, 2, 1, 118, 1, 2, 2, 1, 1),
    _AlarmListName_Type()
)
alarmListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alarmListName.setStatus("current")
_AlarmActiveDateAndTime_Type = DateAndTime
_AlarmActiveDateAndTime_Object = MibTableColumn
alarmActiveDateAndTime = _AlarmActiveDateAndTime_Object(
    (1, 3, 6, 1, 2, 1, 118, 1, 2, 2, 1, 2),
    _AlarmActiveDateAndTime_Type()
)
alarmActiveDateAndTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alarmActiveDateAndTime.setStatus("current")


class _AlarmActiveIndex_Type(Unsigned32):
    """Custom type alarmActiveIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_AlarmActiveIndex_Type.__name__ = "Unsigned32"
_AlarmActiveIndex_Object = MibTableColumn
alarmActiveIndex = _AlarmActiveIndex_Object(
    (1, 3, 6, 1, 2, 1, 118, 1, 2, 2, 1, 3),
    _AlarmActiveIndex_Type()
)
alarmActiveIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alarmActiveIndex.setStatus("current")
_AlarmActiveEngineID_Type = LocalSnmpEngineOrZeroLenStr
_AlarmActiveEngineID_Object = MibTableColumn
alarmActiveEngineID = _AlarmActiveEngineID_Object(
    (1, 3, 6, 1, 2, 1, 118, 1, 2, 2, 1, 4),
    _AlarmActiveEngineID_Type()
)
alarmActiveEngineID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmActiveEngineID.setStatus("current")
_AlarmActiveEngineAddressType_Type = InetAddressType
_AlarmActiveEngineAddressType_Object = MibTableColumn
alarmActiveEngineAddressType = _AlarmActiveEngineAddressType_Object(
    (1, 3, 6, 1, 2, 1, 118, 1, 2, 2, 1, 5),
    _AlarmActiveEngineAddressType_Type()
)
alarmActiveEngineAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmActiveEngineAddressType.setStatus("current")
_AlarmActiveEngineAddress_Type = InetAddress
_AlarmActiveEngineAddress_Object = MibTableColumn
alarmActiveEngineAddress = _AlarmActiveEngineAddress_Object(
    (1, 3, 6, 1, 2, 1, 118, 1, 2, 2, 1, 6),
    _AlarmActiveEngineAddress_Type()
)
alarmActiveEngineAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmActiveEngineAddress.setStatus("current")


class _AlarmActiveContextName_Type(SnmpAdminString):
    """Custom type alarmActiveContextName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlarmActiveContextName_Type.__name__ = "SnmpAdminString"
_AlarmActiveContextName_Object = MibTableColumn
alarmActiveContextName = _AlarmActiveContextName_Object(
    (1, 3, 6, 1, 2, 1, 118, 1, 2, 2, 1, 7),
    _AlarmActiveContextName_Type()
)
alarmActiveContextName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmActiveContextName.setStatus("current")
_AlarmActiveVariables_Type = Unsigned32
_AlarmActiveVariables_Object = MibTableColumn
alarmActiveVariables = _AlarmActiveVariables_Object(
    (1, 3, 6, 1, 2, 1, 118, 1, 2, 2, 1, 8),
    _AlarmActiveVariables_Type()
)
alarmActiveVariables.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmActiveVariables.setStatus("current")
_AlarmActiveNotificationID_Type = ObjectIdentifier
_AlarmActiveNotificationID_Object = MibTableColumn
alarmActiveNotificationID = _AlarmActiveNotificationID_Object(
    (1, 3, 6, 1, 2, 1, 118, 1, 2, 2, 1, 9),
    _AlarmActiveNotificationID_Type()
)
alarmActiveNotificationID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmActiveNotificationID.setStatus("current")
_AlarmActiveResourceId_Type = ResourceId
_AlarmActiveResourceId_Object = MibTableColumn
alarmActiveResourceId = _AlarmActiveResourceId_Object(
    (1, 3, 6, 1, 2, 1, 118, 1, 2, 2, 1, 10),
    _AlarmActiveResourceId_Type()
)
alarmActiveResourceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmActiveResourceId.setStatus("current")
_AlarmActiveDescription_Type = SnmpAdminString
_AlarmActiveDescription_Object = MibTableColumn
alarmActiveDescription = _AlarmActiveDescription_Object(
    (1, 3, 6, 1, 2, 1, 118, 1, 2, 2, 1, 11),
    _AlarmActiveDescription_Type()
)
alarmActiveDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmActiveDescription.setStatus("current")
_AlarmActiveLogPointer_Type = RowPointer
_AlarmActiveLogPointer_Object = MibTableColumn
alarmActiveLogPointer = _AlarmActiveLogPointer_Object(
    (1, 3, 6, 1, 2, 1, 118, 1, 2, 2, 1, 12),
    _AlarmActiveLogPointer_Type()
)
alarmActiveLogPointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmActiveLogPointer.setStatus("current")
_AlarmActiveModelPointer_Type = RowPointer
_AlarmActiveModelPointer_Object = MibTableColumn
alarmActiveModelPointer = _AlarmActiveModelPointer_Object(
    (1, 3, 6, 1, 2, 1, 118, 1, 2, 2, 1, 13),
    _AlarmActiveModelPointer_Type()
)
alarmActiveModelPointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmActiveModelPointer.setStatus("current")
_AlarmActiveSpecificPointer_Type = RowPointer
_AlarmActiveSpecificPointer_Object = MibTableColumn
alarmActiveSpecificPointer = _AlarmActiveSpecificPointer_Object(
    (1, 3, 6, 1, 2, 1, 118, 1, 2, 2, 1, 14),
    _AlarmActiveSpecificPointer_Type()
)
alarmActiveSpecificPointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmActiveSpecificPointer.setStatus("current")
_AlarmActiveVariableTable_Object = MibTable
alarmActiveVariableTable = _AlarmActiveVariableTable_Object(
    (1, 3, 6, 1, 2, 1, 118, 1, 2, 3)
)
if mibBuilder.loadTexts:
    alarmActiveVariableTable.setStatus("current")
_AlarmActiveVariableEntry_Object = MibTableRow
alarmActiveVariableEntry = _AlarmActiveVariableEntry_Object(
    (1, 3, 6, 1, 2, 1, 118, 1, 2, 3, 1)
)
alarmActiveVariableEntry.setIndexNames(
    (0, "ALARM-MIB", "alarmListName"),
    (0, "ALARM-MIB", "alarmActiveIndex"),
    (0, "ALARM-MIB", "alarmActiveVariableIndex"),
)
if mibBuilder.loadTexts:
    alarmActiveVariableEntry.setStatus("current")


class _AlarmActiveVariableIndex_Type(Unsigned32):
    """Custom type alarmActiveVariableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_AlarmActiveVariableIndex_Type.__name__ = "Unsigned32"
_AlarmActiveVariableIndex_Object = MibTableColumn
alarmActiveVariableIndex = _AlarmActiveVariableIndex_Object(
    (1, 3, 6, 1, 2, 1, 118, 1, 2, 3, 1, 1),
    _AlarmActiveVariableIndex_Type()
)
alarmActiveVariableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alarmActiveVariableIndex.setStatus("current")
_AlarmActiveVariableID_Type = ObjectIdentifier
_AlarmActiveVariableID_Object = MibTableColumn
alarmActiveVariableID = _AlarmActiveVariableID_Object(
    (1, 3, 6, 1, 2, 1, 118, 1, 2, 3, 1, 2),
    _AlarmActiveVariableID_Type()
)
alarmActiveVariableID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmActiveVariableID.setStatus("current")


class _AlarmActiveVariableValueType_Type(Integer32):
    """Custom type alarmActiveVariableValueType based on Integer32"""
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


_AlarmActiveVariableValueType_Type.__name__ = "Integer32"
_AlarmActiveVariableValueType_Object = MibTableColumn
alarmActiveVariableValueType = _AlarmActiveVariableValueType_Object(
    (1, 3, 6, 1, 2, 1, 118, 1, 2, 3, 1, 3),
    _AlarmActiveVariableValueType_Type()
)
alarmActiveVariableValueType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmActiveVariableValueType.setStatus("current")
_AlarmActiveVariableCounter32Val_Type = Counter32
_AlarmActiveVariableCounter32Val_Object = MibTableColumn
alarmActiveVariableCounter32Val = _AlarmActiveVariableCounter32Val_Object(
    (1, 3, 6, 1, 2, 1, 118, 1, 2, 3, 1, 4),
    _AlarmActiveVariableCounter32Val_Type()
)
alarmActiveVariableCounter32Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmActiveVariableCounter32Val.setStatus("current")
_AlarmActiveVariableUnsigned32Val_Type = Unsigned32
_AlarmActiveVariableUnsigned32Val_Object = MibTableColumn
alarmActiveVariableUnsigned32Val = _AlarmActiveVariableUnsigned32Val_Object(
    (1, 3, 6, 1, 2, 1, 118, 1, 2, 3, 1, 5),
    _AlarmActiveVariableUnsigned32Val_Type()
)
alarmActiveVariableUnsigned32Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmActiveVariableUnsigned32Val.setStatus("current")
_AlarmActiveVariableTimeTicksVal_Type = TimeTicks
_AlarmActiveVariableTimeTicksVal_Object = MibTableColumn
alarmActiveVariableTimeTicksVal = _AlarmActiveVariableTimeTicksVal_Object(
    (1, 3, 6, 1, 2, 1, 118, 1, 2, 3, 1, 6),
    _AlarmActiveVariableTimeTicksVal_Type()
)
alarmActiveVariableTimeTicksVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmActiveVariableTimeTicksVal.setStatus("current")
_AlarmActiveVariableInteger32Val_Type = Integer32
_AlarmActiveVariableInteger32Val_Object = MibTableColumn
alarmActiveVariableInteger32Val = _AlarmActiveVariableInteger32Val_Object(
    (1, 3, 6, 1, 2, 1, 118, 1, 2, 3, 1, 7),
    _AlarmActiveVariableInteger32Val_Type()
)
alarmActiveVariableInteger32Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmActiveVariableInteger32Val.setStatus("current")


class _AlarmActiveVariableOctetStringVal_Type(OctetString):
    """Custom type alarmActiveVariableOctetStringVal based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_AlarmActiveVariableOctetStringVal_Type.__name__ = "OctetString"
_AlarmActiveVariableOctetStringVal_Object = MibTableColumn
alarmActiveVariableOctetStringVal = _AlarmActiveVariableOctetStringVal_Object(
    (1, 3, 6, 1, 2, 1, 118, 1, 2, 3, 1, 8),
    _AlarmActiveVariableOctetStringVal_Type()
)
alarmActiveVariableOctetStringVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmActiveVariableOctetStringVal.setStatus("current")
_AlarmActiveVariableIpAddressVal_Type = IpAddress
_AlarmActiveVariableIpAddressVal_Object = MibTableColumn
alarmActiveVariableIpAddressVal = _AlarmActiveVariableIpAddressVal_Object(
    (1, 3, 6, 1, 2, 1, 118, 1, 2, 3, 1, 9),
    _AlarmActiveVariableIpAddressVal_Type()
)
alarmActiveVariableIpAddressVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmActiveVariableIpAddressVal.setStatus("current")
_AlarmActiveVariableOidVal_Type = ObjectIdentifier
_AlarmActiveVariableOidVal_Object = MibTableColumn
alarmActiveVariableOidVal = _AlarmActiveVariableOidVal_Object(
    (1, 3, 6, 1, 2, 1, 118, 1, 2, 3, 1, 10),
    _AlarmActiveVariableOidVal_Type()
)
alarmActiveVariableOidVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmActiveVariableOidVal.setStatus("current")
_AlarmActiveVariableCounter64Val_Type = Counter64
_AlarmActiveVariableCounter64Val_Object = MibTableColumn
alarmActiveVariableCounter64Val = _AlarmActiveVariableCounter64Val_Object(
    (1, 3, 6, 1, 2, 1, 118, 1, 2, 3, 1, 11),
    _AlarmActiveVariableCounter64Val_Type()
)
alarmActiveVariableCounter64Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmActiveVariableCounter64Val.setStatus("current")


class _AlarmActiveVariableOpaqueVal_Type(Opaque):
    """Custom type alarmActiveVariableOpaqueVal based on Opaque"""
    subtypeSpec = Opaque.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_AlarmActiveVariableOpaqueVal_Type.__name__ = "Opaque"
_AlarmActiveVariableOpaqueVal_Object = MibTableColumn
alarmActiveVariableOpaqueVal = _AlarmActiveVariableOpaqueVal_Object(
    (1, 3, 6, 1, 2, 1, 118, 1, 2, 3, 1, 12),
    _AlarmActiveVariableOpaqueVal_Type()
)
alarmActiveVariableOpaqueVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmActiveVariableOpaqueVal.setStatus("current")
_AlarmActiveStatsTable_Object = MibTable
alarmActiveStatsTable = _AlarmActiveStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 118, 1, 2, 4)
)
if mibBuilder.loadTexts:
    alarmActiveStatsTable.setStatus("current")
_AlarmActiveStatsEntry_Object = MibTableRow
alarmActiveStatsEntry = _AlarmActiveStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 118, 1, 2, 4, 1)
)
alarmActiveStatsEntry.setIndexNames(
    (0, "ALARM-MIB", "alarmListName"),
)
if mibBuilder.loadTexts:
    alarmActiveStatsEntry.setStatus("current")
_AlarmActiveStatsActiveCurrent_Type = Gauge32
_AlarmActiveStatsActiveCurrent_Object = MibTableColumn
alarmActiveStatsActiveCurrent = _AlarmActiveStatsActiveCurrent_Object(
    (1, 3, 6, 1, 2, 1, 118, 1, 2, 4, 1, 1),
    _AlarmActiveStatsActiveCurrent_Type()
)
alarmActiveStatsActiveCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmActiveStatsActiveCurrent.setStatus("current")
_AlarmActiveStatsActives_Type = ZeroBasedCounter32
_AlarmActiveStatsActives_Object = MibTableColumn
alarmActiveStatsActives = _AlarmActiveStatsActives_Object(
    (1, 3, 6, 1, 2, 1, 118, 1, 2, 4, 1, 2),
    _AlarmActiveStatsActives_Type()
)
alarmActiveStatsActives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmActiveStatsActives.setStatus("current")
_AlarmActiveStatsLastRaise_Type = TimeTicks
_AlarmActiveStatsLastRaise_Object = MibTableColumn
alarmActiveStatsLastRaise = _AlarmActiveStatsLastRaise_Object(
    (1, 3, 6, 1, 2, 1, 118, 1, 2, 4, 1, 3),
    _AlarmActiveStatsLastRaise_Type()
)
alarmActiveStatsLastRaise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmActiveStatsLastRaise.setStatus("current")
_AlarmActiveStatsLastClear_Type = TimeTicks
_AlarmActiveStatsLastClear_Object = MibTableColumn
alarmActiveStatsLastClear = _AlarmActiveStatsLastClear_Object(
    (1, 3, 6, 1, 2, 1, 118, 1, 2, 4, 1, 4),
    _AlarmActiveStatsLastClear_Type()
)
alarmActiveStatsLastClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmActiveStatsLastClear.setStatus("current")
_AlarmActiveOverflow_Type = Counter32
_AlarmActiveOverflow_Object = MibScalar
alarmActiveOverflow = _AlarmActiveOverflow_Object(
    (1, 3, 6, 1, 2, 1, 118, 1, 2, 5),
    _AlarmActiveOverflow_Type()
)
alarmActiveOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmActiveOverflow.setStatus("current")
if mibBuilder.loadTexts:
    alarmActiveOverflow.setUnits("active alarms")
_AlarmClear_ObjectIdentity = ObjectIdentity
alarmClear = _AlarmClear_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 118, 1, 3)
)
_AlarmClearMaximum_Type = Unsigned32
_AlarmClearMaximum_Object = MibScalar
alarmClearMaximum = _AlarmClearMaximum_Object(
    (1, 3, 6, 1, 2, 1, 118, 1, 3, 1),
    _AlarmClearMaximum_Type()
)
alarmClearMaximum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmClearMaximum.setStatus("current")
_AlarmClearTable_Object = MibTable
alarmClearTable = _AlarmClearTable_Object(
    (1, 3, 6, 1, 2, 1, 118, 1, 3, 2)
)
if mibBuilder.loadTexts:
    alarmClearTable.setStatus("current")
_AlarmClearEntry_Object = MibTableRow
alarmClearEntry = _AlarmClearEntry_Object(
    (1, 3, 6, 1, 2, 1, 118, 1, 3, 2, 1)
)
alarmClearEntry.setIndexNames(
    (0, "ALARM-MIB", "alarmListName"),
    (0, "ALARM-MIB", "alarmClearDateAndTime"),
    (0, "ALARM-MIB", "alarmClearIndex"),
)
if mibBuilder.loadTexts:
    alarmClearEntry.setStatus("current")


class _AlarmClearIndex_Type(Unsigned32):
    """Custom type alarmClearIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_AlarmClearIndex_Type.__name__ = "Unsigned32"
_AlarmClearIndex_Object = MibTableColumn
alarmClearIndex = _AlarmClearIndex_Object(
    (1, 3, 6, 1, 2, 1, 118, 1, 3, 2, 1, 1),
    _AlarmClearIndex_Type()
)
alarmClearIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alarmClearIndex.setStatus("current")
_AlarmClearDateAndTime_Type = DateAndTime
_AlarmClearDateAndTime_Object = MibTableColumn
alarmClearDateAndTime = _AlarmClearDateAndTime_Object(
    (1, 3, 6, 1, 2, 1, 118, 1, 3, 2, 1, 2),
    _AlarmClearDateAndTime_Type()
)
alarmClearDateAndTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alarmClearDateAndTime.setStatus("current")
_AlarmClearEngineID_Type = LocalSnmpEngineOrZeroLenStr
_AlarmClearEngineID_Object = MibTableColumn
alarmClearEngineID = _AlarmClearEngineID_Object(
    (1, 3, 6, 1, 2, 1, 118, 1, 3, 2, 1, 3),
    _AlarmClearEngineID_Type()
)
alarmClearEngineID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmClearEngineID.setStatus("current")
_AlarmClearEngineAddressType_Type = InetAddressType
_AlarmClearEngineAddressType_Object = MibTableColumn
alarmClearEngineAddressType = _AlarmClearEngineAddressType_Object(
    (1, 3, 6, 1, 2, 1, 118, 1, 3, 2, 1, 4),
    _AlarmClearEngineAddressType_Type()
)
alarmClearEngineAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmClearEngineAddressType.setStatus("current")
_AlarmClearEngineAddress_Type = InetAddress
_AlarmClearEngineAddress_Object = MibTableColumn
alarmClearEngineAddress = _AlarmClearEngineAddress_Object(
    (1, 3, 6, 1, 2, 1, 118, 1, 3, 2, 1, 5),
    _AlarmClearEngineAddress_Type()
)
alarmClearEngineAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmClearEngineAddress.setStatus("current")


class _AlarmClearContextName_Type(SnmpAdminString):
    """Custom type alarmClearContextName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlarmClearContextName_Type.__name__ = "SnmpAdminString"
_AlarmClearContextName_Object = MibTableColumn
alarmClearContextName = _AlarmClearContextName_Object(
    (1, 3, 6, 1, 2, 1, 118, 1, 3, 2, 1, 6),
    _AlarmClearContextName_Type()
)
alarmClearContextName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmClearContextName.setStatus("current")
_AlarmClearNotificationID_Type = ObjectIdentifier
_AlarmClearNotificationID_Object = MibTableColumn
alarmClearNotificationID = _AlarmClearNotificationID_Object(
    (1, 3, 6, 1, 2, 1, 118, 1, 3, 2, 1, 7),
    _AlarmClearNotificationID_Type()
)
alarmClearNotificationID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmClearNotificationID.setStatus("current")
_AlarmClearResourceId_Type = ResourceId
_AlarmClearResourceId_Object = MibTableColumn
alarmClearResourceId = _AlarmClearResourceId_Object(
    (1, 3, 6, 1, 2, 1, 118, 1, 3, 2, 1, 8),
    _AlarmClearResourceId_Type()
)
alarmClearResourceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmClearResourceId.setStatus("current")


class _AlarmClearLogIndex_Type(Unsigned32):
    """Custom type alarmClearLogIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AlarmClearLogIndex_Type.__name__ = "Unsigned32"
_AlarmClearLogIndex_Object = MibTableColumn
alarmClearLogIndex = _AlarmClearLogIndex_Object(
    (1, 3, 6, 1, 2, 1, 118, 1, 3, 2, 1, 9),
    _AlarmClearLogIndex_Type()
)
alarmClearLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmClearLogIndex.setStatus("current")
_AlarmClearModelPointer_Type = RowPointer
_AlarmClearModelPointer_Object = MibTableColumn
alarmClearModelPointer = _AlarmClearModelPointer_Object(
    (1, 3, 6, 1, 2, 1, 118, 1, 3, 2, 1, 10),
    _AlarmClearModelPointer_Type()
)
alarmClearModelPointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmClearModelPointer.setStatus("current")
_AlarmConformance_ObjectIdentity = ObjectIdentity
alarmConformance = _AlarmConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 118, 2)
)
_AlarmCompliances_ObjectIdentity = ObjectIdentity
alarmCompliances = _AlarmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 118, 2, 1)
)
_AlarmGroups_ObjectIdentity = ObjectIdentity
alarmGroups = _AlarmGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 118, 2, 2)
)

# Managed Objects groups

alarmModelGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 118, 2, 2, 1)
)
alarmModelGroup.setObjects(
      *(("ALARM-MIB", "alarmModelLastChanged"),
        ("ALARM-MIB", "alarmModelNotificationId"),
        ("ALARM-MIB", "alarmModelVarbindIndex"),
        ("ALARM-MIB", "alarmModelVarbindValue"),
        ("ALARM-MIB", "alarmModelDescription"),
        ("ALARM-MIB", "alarmModelSpecificPointer"),
        ("ALARM-MIB", "alarmModelVarbindSubtree"),
        ("ALARM-MIB", "alarmModelResourcePrefix"),
        ("ALARM-MIB", "alarmModelRowStatus"))
)
if mibBuilder.loadTexts:
    alarmModelGroup.setStatus("current")

alarmActiveGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 118, 2, 2, 2)
)
alarmActiveGroup.setObjects(
      *(("ALARM-MIB", "alarmActiveLastChanged"),
        ("ALARM-MIB", "alarmActiveOverflow"),
        ("ALARM-MIB", "alarmActiveEngineID"),
        ("ALARM-MIB", "alarmActiveEngineAddressType"),
        ("ALARM-MIB", "alarmActiveEngineAddress"),
        ("ALARM-MIB", "alarmActiveContextName"),
        ("ALARM-MIB", "alarmActiveVariables"),
        ("ALARM-MIB", "alarmActiveNotificationID"),
        ("ALARM-MIB", "alarmActiveResourceId"),
        ("ALARM-MIB", "alarmActiveDescription"),
        ("ALARM-MIB", "alarmActiveLogPointer"),
        ("ALARM-MIB", "alarmActiveModelPointer"),
        ("ALARM-MIB", "alarmActiveSpecificPointer"),
        ("ALARM-MIB", "alarmActiveVariableID"),
        ("ALARM-MIB", "alarmActiveVariableValueType"),
        ("ALARM-MIB", "alarmActiveVariableCounter32Val"),
        ("ALARM-MIB", "alarmActiveVariableUnsigned32Val"),
        ("ALARM-MIB", "alarmActiveVariableTimeTicksVal"),
        ("ALARM-MIB", "alarmActiveVariableInteger32Val"),
        ("ALARM-MIB", "alarmActiveVariableOctetStringVal"),
        ("ALARM-MIB", "alarmActiveVariableIpAddressVal"),
        ("ALARM-MIB", "alarmActiveVariableOidVal"),
        ("ALARM-MIB", "alarmActiveVariableCounter64Val"),
        ("ALARM-MIB", "alarmActiveVariableOpaqueVal"))
)
if mibBuilder.loadTexts:
    alarmActiveGroup.setStatus("current")

alarmActiveStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 118, 2, 2, 3)
)
alarmActiveStatsGroup.setObjects(
      *(("ALARM-MIB", "alarmActiveStatsActives"),
        ("ALARM-MIB", "alarmActiveStatsActiveCurrent"),
        ("ALARM-MIB", "alarmActiveStatsLastRaise"),
        ("ALARM-MIB", "alarmActiveStatsLastClear"))
)
if mibBuilder.loadTexts:
    alarmActiveStatsGroup.setStatus("current")

alarmClearGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 118, 2, 2, 4)
)
alarmClearGroup.setObjects(
      *(("ALARM-MIB", "alarmClearMaximum"),
        ("ALARM-MIB", "alarmClearEngineID"),
        ("ALARM-MIB", "alarmClearEngineAddressType"),
        ("ALARM-MIB", "alarmClearEngineAddress"),
        ("ALARM-MIB", "alarmClearContextName"),
        ("ALARM-MIB", "alarmClearNotificationID"),
        ("ALARM-MIB", "alarmClearResourceId"),
        ("ALARM-MIB", "alarmClearLogIndex"),
        ("ALARM-MIB", "alarmClearModelPointer"))
)
if mibBuilder.loadTexts:
    alarmClearGroup.setStatus("current")


# Notification objects

alarmActiveState = NotificationType(
    (1, 3, 6, 1, 2, 1, 118, 0, 2)
)
alarmActiveState.setObjects(
      *(("ALARM-MIB", "alarmActiveModelPointer"),
        ("ALARM-MIB", "alarmActiveResourceId"))
)
if mibBuilder.loadTexts:
    alarmActiveState.setStatus(
        "current"
    )

alarmClearState = NotificationType(
    (1, 3, 6, 1, 2, 1, 118, 0, 3)
)
alarmClearState.setObjects(
      *(("ALARM-MIB", "alarmActiveModelPointer"),
        ("ALARM-MIB", "alarmActiveResourceId"))
)
if mibBuilder.loadTexts:
    alarmClearState.setStatus(
        "current"
    )


# Notifications groups

alarmNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 118, 2, 2, 6)
)
alarmNotificationsGroup.setObjects(
      *(("ALARM-MIB", "alarmActiveState"),
        ("ALARM-MIB", "alarmClearState"))
)
if mibBuilder.loadTexts:
    alarmNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alarmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 118, 2, 1, 1)
)
if mibBuilder.loadTexts:
    alarmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALARM-MIB",
    **{"ResourceId": ResourceId,
       "LocalSnmpEngineOrZeroLenStr": LocalSnmpEngineOrZeroLenStr,
       "alarmMIB": alarmMIB,
       "alarmNotifications": alarmNotifications,
       "alarmActiveState": alarmActiveState,
       "alarmClearState": alarmClearState,
       "alarmObjects": alarmObjects,
       "alarmModel": alarmModel,
       "alarmModelLastChanged": alarmModelLastChanged,
       "alarmModelTable": alarmModelTable,
       "alarmModelEntry": alarmModelEntry,
       "alarmModelIndex": alarmModelIndex,
       "alarmModelState": alarmModelState,
       "alarmModelNotificationId": alarmModelNotificationId,
       "alarmModelVarbindIndex": alarmModelVarbindIndex,
       "alarmModelVarbindValue": alarmModelVarbindValue,
       "alarmModelDescription": alarmModelDescription,
       "alarmModelSpecificPointer": alarmModelSpecificPointer,
       "alarmModelVarbindSubtree": alarmModelVarbindSubtree,
       "alarmModelResourcePrefix": alarmModelResourcePrefix,
       "alarmModelRowStatus": alarmModelRowStatus,
       "alarmActive": alarmActive,
       "alarmActiveLastChanged": alarmActiveLastChanged,
       "alarmActiveTable": alarmActiveTable,
       "alarmActiveEntry": alarmActiveEntry,
       "alarmListName": alarmListName,
       "alarmActiveDateAndTime": alarmActiveDateAndTime,
       "alarmActiveIndex": alarmActiveIndex,
       "alarmActiveEngineID": alarmActiveEngineID,
       "alarmActiveEngineAddressType": alarmActiveEngineAddressType,
       "alarmActiveEngineAddress": alarmActiveEngineAddress,
       "alarmActiveContextName": alarmActiveContextName,
       "alarmActiveVariables": alarmActiveVariables,
       "alarmActiveNotificationID": alarmActiveNotificationID,
       "alarmActiveResourceId": alarmActiveResourceId,
       "alarmActiveDescription": alarmActiveDescription,
       "alarmActiveLogPointer": alarmActiveLogPointer,
       "alarmActiveModelPointer": alarmActiveModelPointer,
       "alarmActiveSpecificPointer": alarmActiveSpecificPointer,
       "alarmActiveVariableTable": alarmActiveVariableTable,
       "alarmActiveVariableEntry": alarmActiveVariableEntry,
       "alarmActiveVariableIndex": alarmActiveVariableIndex,
       "alarmActiveVariableID": alarmActiveVariableID,
       "alarmActiveVariableValueType": alarmActiveVariableValueType,
       "alarmActiveVariableCounter32Val": alarmActiveVariableCounter32Val,
       "alarmActiveVariableUnsigned32Val": alarmActiveVariableUnsigned32Val,
       "alarmActiveVariableTimeTicksVal": alarmActiveVariableTimeTicksVal,
       "alarmActiveVariableInteger32Val": alarmActiveVariableInteger32Val,
       "alarmActiveVariableOctetStringVal": alarmActiveVariableOctetStringVal,
       "alarmActiveVariableIpAddressVal": alarmActiveVariableIpAddressVal,
       "alarmActiveVariableOidVal": alarmActiveVariableOidVal,
       "alarmActiveVariableCounter64Val": alarmActiveVariableCounter64Val,
       "alarmActiveVariableOpaqueVal": alarmActiveVariableOpaqueVal,
       "alarmActiveStatsTable": alarmActiveStatsTable,
       "alarmActiveStatsEntry": alarmActiveStatsEntry,
       "alarmActiveStatsActiveCurrent": alarmActiveStatsActiveCurrent,
       "alarmActiveStatsActives": alarmActiveStatsActives,
       "alarmActiveStatsLastRaise": alarmActiveStatsLastRaise,
       "alarmActiveStatsLastClear": alarmActiveStatsLastClear,
       "alarmActiveOverflow": alarmActiveOverflow,
       "alarmClear": alarmClear,
       "alarmClearMaximum": alarmClearMaximum,
       "alarmClearTable": alarmClearTable,
       "alarmClearEntry": alarmClearEntry,
       "alarmClearIndex": alarmClearIndex,
       "alarmClearDateAndTime": alarmClearDateAndTime,
       "alarmClearEngineID": alarmClearEngineID,
       "alarmClearEngineAddressType": alarmClearEngineAddressType,
       "alarmClearEngineAddress": alarmClearEngineAddress,
       "alarmClearContextName": alarmClearContextName,
       "alarmClearNotificationID": alarmClearNotificationID,
       "alarmClearResourceId": alarmClearResourceId,
       "alarmClearLogIndex": alarmClearLogIndex,
       "alarmClearModelPointer": alarmClearModelPointer,
       "alarmConformance": alarmConformance,
       "alarmCompliances": alarmCompliances,
       "alarmCompliance": alarmCompliance,
       "alarmGroups": alarmGroups,
       "alarmModelGroup": alarmModelGroup,
       "alarmActiveGroup": alarmActiveGroup,
       "alarmActiveStatsGroup": alarmActiveStatsGroup,
       "alarmClearGroup": alarmClearGroup,
       "alarmNotificationsGroup": alarmNotificationsGroup}
)
