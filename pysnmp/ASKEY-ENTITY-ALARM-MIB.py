# SNMP MIB module (ASKEY-ENTITY-ALARM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASKEY-ENTITY-ALARM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:49 2024
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

(AskeyVendorTypeEnum,
 ipDslam) = mibBuilder.importSymbols(
    "ASKEY-DSLAM-MIB",
    "AskeyVendorTypeEnum",
    "ipDslam")

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

(AutonomousType,
 DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

askeyEntityAlarmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12)
)
askeyEntityAlarmMIB.setRevisions(
        ("1904-11-22 15:41",
         "1904-10-13 14:00",
         "1904-08-10 16:10",
         "1904-08-10 10:10",
         "1904-07-30 14:10")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AskeyAlarmBit(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )



class AskeyAlarmSeverity(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              99)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("info", 5),
          ("major", 2),
          ("minor", 3),
          ("none", 99),
          ("warning", 4))
    )



class AskeyAlarmName(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class AskeyAlarmList(Unsigned32, TextualConvention):
    status = "current"


class AskeyAlarmAction(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("set", 1))
    )



# MIB Managed Objects in the order of their OIDs

_AskeyEntityAlarmMIBObjects_ObjectIdentity = ObjectIdentity
askeyEntityAlarmMIBObjects = _AskeyEntityAlarmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1)
)
_AeAlarmDefinition_ObjectIdentity = ObjectIdentity
aeAlarmDefinition = _AeAlarmDefinition_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 2)
)
_AeAlarmDefinitionTable_Object = MibTable
aeAlarmDefinitionTable = _AeAlarmDefinitionTable_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 2, 1)
)
if mibBuilder.loadTexts:
    aeAlarmDefinitionTable.setStatus("current")
_AeAlarmDefinitionEntry_Object = MibTableRow
aeAlarmDefinitionEntry = _AeAlarmDefinitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 2, 1, 1)
)
aeAlarmDefinitionEntry.setIndexNames(
    (0, "ASKEY-ENTITY-ALARM-MIB", "aeAlarmDefVendorTypeEnum"),
    (0, "ASKEY-ENTITY-ALARM-MIB", "aeAlarmDefType"),
)
if mibBuilder.loadTexts:
    aeAlarmDefinitionEntry.setStatus("current")
_AeAlarmDefVendorTypeEnum_Type = AskeyVendorTypeEnum
_AeAlarmDefVendorTypeEnum_Object = MibTableColumn
aeAlarmDefVendorTypeEnum = _AeAlarmDefVendorTypeEnum_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 2, 1, 1, 1),
    _AeAlarmDefVendorTypeEnum_Type()
)
aeAlarmDefVendorTypeEnum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aeAlarmDefVendorTypeEnum.setStatus("current")
_AeAlarmDefType_Type = AskeyAlarmBit
_AeAlarmDefType_Object = MibTableColumn
aeAlarmDefType = _AeAlarmDefType_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 2, 1, 1, 2),
    _AeAlarmDefType_Type()
)
aeAlarmDefType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aeAlarmDefType.setStatus("current")
_AeAlarmDefName_Type = AskeyAlarmName
_AeAlarmDefName_Object = MibTableColumn
aeAlarmDefName = _AeAlarmDefName_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 2, 1, 1, 3),
    _AeAlarmDefName_Type()
)
aeAlarmDefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aeAlarmDefName.setStatus("current")
_AeAlarmDefDescr_Type = DisplayString
_AeAlarmDefDescr_Object = MibTableColumn
aeAlarmDefDescr = _AeAlarmDefDescr_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 2, 1, 1, 4),
    _AeAlarmDefDescr_Type()
)
aeAlarmDefDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aeAlarmDefDescr.setStatus("current")


class _AeAlarmDefSeverity_Type(AskeyAlarmSeverity):
    """Custom type aeAlarmDefSeverity based on AskeyAlarmSeverity"""
    defaultValue = 4


_AeAlarmDefSeverity_Object = MibTableColumn
aeAlarmDefSeverity = _AeAlarmDefSeverity_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 2, 1, 1, 5),
    _AeAlarmDefSeverity_Type()
)
aeAlarmDefSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aeAlarmDefSeverity.setStatus("current")


class _AeAlarmDefFiltered_Type(TruthValue):
    """Custom type aeAlarmDefFiltered based on TruthValue"""
    defaultValue = 2


_AeAlarmDefFiltered_Object = MibTableColumn
aeAlarmDefFiltered = _AeAlarmDefFiltered_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 2, 1, 1, 6),
    _AeAlarmDefFiltered_Type()
)
aeAlarmDefFiltered.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aeAlarmDefFiltered.setStatus("current")


class _AeAlarmDefSuppressedby_Type(AskeyAlarmList):
    """Custom type aeAlarmDefSuppressedby based on AskeyAlarmList"""
    defaultValue = 0


_AeAlarmDefSuppressedby_Object = MibTableColumn
aeAlarmDefSuppressedby = _AeAlarmDefSuppressedby_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 2, 1, 1, 7),
    _AeAlarmDefSuppressedby_Type()
)
aeAlarmDefSuppressedby.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aeAlarmDefSuppressedby.setStatus("current")
_AeAlarmMonitoring_ObjectIdentity = ObjectIdentity
aeAlarmMonitoring = _AeAlarmMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 3)
)
_AeAlarmTable_Object = MibTable
aeAlarmTable = _AeAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 3, 1)
)
if mibBuilder.loadTexts:
    aeAlarmTable.setStatus("current")
_AeAlarmEntry_Object = MibTableRow
aeAlarmEntry = _AeAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 3, 1, 1)
)
aeAlarmEntry.setIndexNames(
    (0, "ASKEY-ENTITY-ALARM-MIB", "aeAlarmPhysicalIndex"),
)
if mibBuilder.loadTexts:
    aeAlarmEntry.setStatus("current")
_AeAlarmPhysicalIndex_Type = Unsigned32
_AeAlarmPhysicalIndex_Object = MibTableColumn
aeAlarmPhysicalIndex = _AeAlarmPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 3, 1, 1, 1),
    _AeAlarmPhysicalIndex_Type()
)
aeAlarmPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aeAlarmPhysicalIndex.setStatus("current")
_AeAlarmPlannedVendorTypeEnum_Type = AskeyVendorTypeEnum
_AeAlarmPlannedVendorTypeEnum_Object = MibTableColumn
aeAlarmPlannedVendorTypeEnum = _AeAlarmPlannedVendorTypeEnum_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 3, 1, 1, 2),
    _AeAlarmPlannedVendorTypeEnum_Type()
)
aeAlarmPlannedVendorTypeEnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aeAlarmPlannedVendorTypeEnum.setStatus("current")
_AeAlarmOnlineVendorTypeEnum_Type = AskeyVendorTypeEnum
_AeAlarmOnlineVendorTypeEnum_Object = MibTableColumn
aeAlarmOnlineVendorTypeEnum = _AeAlarmOnlineVendorTypeEnum_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 3, 1, 1, 3),
    _AeAlarmOnlineVendorTypeEnum_Type()
)
aeAlarmOnlineVendorTypeEnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aeAlarmOnlineVendorTypeEnum.setStatus("current")
_AeAlarmList_Type = AskeyAlarmList
_AeAlarmList_Object = MibTableColumn
aeAlarmList = _AeAlarmList_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 3, 1, 1, 4),
    _AeAlarmList_Type()
)
aeAlarmList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aeAlarmList.setStatus("current")
_AeAlarmLastChange_Type = Unsigned32
_AeAlarmLastChange_Object = MibTableColumn
aeAlarmLastChange = _AeAlarmLastChange_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 3, 1, 1, 5),
    _AeAlarmLastChange_Type()
)
aeAlarmLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aeAlarmLastChange.setStatus("current")
_AeAlarmSeverity_Type = AskeyAlarmSeverity
_AeAlarmSeverity_Object = MibTableColumn
aeAlarmSeverity = _AeAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 3, 1, 1, 6),
    _AeAlarmSeverity_Type()
)
aeAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aeAlarmSeverity.setStatus("current")
_AeAlarmHistory_ObjectIdentity = ObjectIdentity
aeAlarmHistory = _AeAlarmHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 4)
)
_AeHistoryAlarmTableSize_Type = Integer32
_AeHistoryAlarmTableSize_Object = MibScalar
aeHistoryAlarmTableSize = _AeHistoryAlarmTableSize_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 4, 1),
    _AeHistoryAlarmTableSize_Type()
)
aeHistoryAlarmTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aeHistoryAlarmTableSize.setStatus("current")
_AeHistoryAlarmTable_Object = MibTable
aeHistoryAlarmTable = _AeHistoryAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 4, 2)
)
if mibBuilder.loadTexts:
    aeHistoryAlarmTable.setStatus("current")
_AeHistoryAlarmEntry_Object = MibTableRow
aeHistoryAlarmEntry = _AeHistoryAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 4, 2, 1)
)
aeHistoryAlarmEntry.setIndexNames(
    (0, "ASKEY-ENTITY-ALARM-MIB", "aeHistoryAlarmIndex"),
)
if mibBuilder.loadTexts:
    aeHistoryAlarmEntry.setStatus("current")


class _AeHistoryAlarmIndex_Type(Integer32):
    """Custom type aeHistoryAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2146483647),
    )


_AeHistoryAlarmIndex_Type.__name__ = "Integer32"
_AeHistoryAlarmIndex_Object = MibTableColumn
aeHistoryAlarmIndex = _AeHistoryAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 4, 2, 1, 1),
    _AeHistoryAlarmIndex_Type()
)
aeHistoryAlarmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aeHistoryAlarmIndex.setStatus("current")
_AeHistoryAlarmPhysicalIndex_Type = Unsigned32
_AeHistoryAlarmPhysicalIndex_Object = MibTableColumn
aeHistoryAlarmPhysicalIndex = _AeHistoryAlarmPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 4, 2, 1, 2),
    _AeHistoryAlarmPhysicalIndex_Type()
)
aeHistoryAlarmPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aeHistoryAlarmPhysicalIndex.setStatus("current")
_AeHistoryAlarmPlannedVendorTypeEnum_Type = AskeyVendorTypeEnum
_AeHistoryAlarmPlannedVendorTypeEnum_Object = MibTableColumn
aeHistoryAlarmPlannedVendorTypeEnum = _AeHistoryAlarmPlannedVendorTypeEnum_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 4, 2, 1, 3),
    _AeHistoryAlarmPlannedVendorTypeEnum_Type()
)
aeHistoryAlarmPlannedVendorTypeEnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aeHistoryAlarmPlannedVendorTypeEnum.setStatus("current")
_AeHistoryAlarmOnlineVendorTypeEnum_Type = AskeyVendorTypeEnum
_AeHistoryAlarmOnlineVendorTypeEnum_Object = MibTableColumn
aeHistoryAlarmOnlineVendorTypeEnum = _AeHistoryAlarmOnlineVendorTypeEnum_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 4, 2, 1, 4),
    _AeHistoryAlarmOnlineVendorTypeEnum_Type()
)
aeHistoryAlarmOnlineVendorTypeEnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aeHistoryAlarmOnlineVendorTypeEnum.setStatus("current")
_AeHistoryAlarmType_Type = AskeyAlarmBit
_AeHistoryAlarmType_Object = MibTableColumn
aeHistoryAlarmType = _AeHistoryAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 4, 2, 1, 5),
    _AeHistoryAlarmType_Type()
)
aeHistoryAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aeHistoryAlarmType.setStatus("current")
_AeHistoryAlarmTime_Type = Unsigned32
_AeHistoryAlarmTime_Object = MibTableColumn
aeHistoryAlarmTime = _AeHistoryAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 4, 2, 1, 6),
    _AeHistoryAlarmTime_Type()
)
aeHistoryAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aeHistoryAlarmTime.setStatus("current")
_AeHistoryAlarmAction_Type = AskeyAlarmAction
_AeHistoryAlarmAction_Object = MibTableColumn
aeHistoryAlarmAction = _AeHistoryAlarmAction_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 4, 2, 1, 7),
    _AeHistoryAlarmAction_Type()
)
aeHistoryAlarmAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aeHistoryAlarmAction.setStatus("current")
_AeRelayInTable_Object = MibTable
aeRelayInTable = _AeRelayInTable_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 5)
)
if mibBuilder.loadTexts:
    aeRelayInTable.setStatus("current")
_AeRelayInEntry_Object = MibTableRow
aeRelayInEntry = _AeRelayInEntry_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 5, 1)
)
aeRelayInEntry.setIndexNames(
    (0, "ASKEY-ENTITY-ALARM-MIB", "aeRelayInPhysicalIndex"),
)
if mibBuilder.loadTexts:
    aeRelayInEntry.setStatus("current")
_AeRelayInPhysicalIndex_Type = Unsigned32
_AeRelayInPhysicalIndex_Object = MibTableColumn
aeRelayInPhysicalIndex = _AeRelayInPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 5, 1, 1),
    _AeRelayInPhysicalIndex_Type()
)
aeRelayInPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aeRelayInPhysicalIndex.setStatus("current")


class _AeRelayInName_Type(DisplayString):
    """Custom type aeRelayInName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AeRelayInName_Type.__name__ = "DisplayString"
_AeRelayInName_Object = MibTableColumn
aeRelayInName = _AeRelayInName_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 5, 1, 2),
    _AeRelayInName_Type()
)
aeRelayInName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aeRelayInName.setStatus("current")


class _AeRelayInNormalStatus_Type(Integer32):
    """Custom type aeRelayInNormalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("close", 2),
          ("disable", 3),
          ("open", 1))
    )


_AeRelayInNormalStatus_Type.__name__ = "Integer32"
_AeRelayInNormalStatus_Object = MibTableColumn
aeRelayInNormalStatus = _AeRelayInNormalStatus_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 5, 1, 3),
    _AeRelayInNormalStatus_Type()
)
aeRelayInNormalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aeRelayInNormalStatus.setStatus("current")


class _AeRelayInCurrentStatus_Type(Integer32):
    """Custom type aeRelayInCurrentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("close", 2),
          ("disable", 3),
          ("open", 1))
    )


_AeRelayInCurrentStatus_Type.__name__ = "Integer32"
_AeRelayInCurrentStatus_Object = MibTableColumn
aeRelayInCurrentStatus = _AeRelayInCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 1, 5, 1, 4),
    _AeRelayInCurrentStatus_Type()
)
aeRelayInCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aeRelayInCurrentStatus.setStatus("current")
_AskeyEntityAlarmMIBTraps_ObjectIdentity = ObjectIdentity
askeyEntityAlarmMIBTraps = _AskeyEntityAlarmMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 2)
)
_AskeyEntityMIBTrapPrefix_ObjectIdentity = ObjectIdentity
askeyEntityMIBTrapPrefix = _AskeyEntityMIBTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 2, 0)
)
_AskeyEntityAlarmConformance_ObjectIdentity = ObjectIdentity
askeyEntityAlarmConformance = _AskeyEntityAlarmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 3)
)
_AskeyEntityAlarmCompliances_ObjectIdentity = ObjectIdentity
askeyEntityAlarmCompliances = _AskeyEntityAlarmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 3, 1)
)
_AskeyEntityAlarmGroups_ObjectIdentity = ObjectIdentity
askeyEntityAlarmGroups = _AskeyEntityAlarmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 3, 2)
)

# Managed Objects groups

askeyEntityAlarmDefinitionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 3, 2, 2)
)
askeyEntityAlarmDefinitionGroup.setObjects(
      *(("ASKEY-ENTITY-ALARM-MIB", "aeAlarmDefType"),
        ("ASKEY-ENTITY-ALARM-MIB", "aeAlarmDefName"),
        ("ASKEY-ENTITY-ALARM-MIB", "aeAlarmDefDescr"),
        ("ASKEY-ENTITY-ALARM-MIB", "aeAlarmDefSeverity"),
        ("ASKEY-ENTITY-ALARM-MIB", "aeAlarmDefFiltered"),
        ("ASKEY-ENTITY-ALARM-MIB", "aeAlarmDefSuppressedby"))
)
if mibBuilder.loadTexts:
    askeyEntityAlarmDefinitionGroup.setStatus("current")

askeyEntityAlarmMonitoringGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 3, 2, 3)
)
askeyEntityAlarmMonitoringGroup.setObjects(
      *(("ASKEY-ENTITY-ALARM-MIB", "aeAlarmPlannedVendorTypeEnum"),
        ("ASKEY-ENTITY-ALARM-MIB", "aeAlarmOnlineVendorTypeEnum"),
        ("ASKEY-ENTITY-ALARM-MIB", "aeAlarmList"),
        ("ASKEY-ENTITY-ALARM-MIB", "aeAlarmLastChange"),
        ("ASKEY-ENTITY-ALARM-MIB", "aeAlarmSeverity"))
)
if mibBuilder.loadTexts:
    askeyEntityAlarmMonitoringGroup.setStatus("current")


# Notification objects

askeyEntityAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 2, 0, 1)
)
askeyEntityAlarmTrap.setObjects(
      *(("ASKEY-ENTITY-ALARM-MIB", "aeAlarmPhysicalIndex"),
        ("ASKEY-ENTITY-ALARM-MIB", "aeAlarmPlannedVendorTypeEnum"),
        ("ASKEY-ENTITY-ALARM-MIB", "aeAlarmOnlineVendorTypeEnum"),
        ("ASKEY-ENTITY-ALARM-MIB", "aeAlarmList"),
        ("ASKEY-ENTITY-ALARM-MIB", "aeAlarmLastChange"),
        ("ASKEY-ENTITY-ALARM-MIB", "aeAlarmSeverity"))
)
if mibBuilder.loadTexts:
    askeyEntityAlarmTrap.setStatus(
        "current"
    )


# Notifications groups

askeyEntityAlarmNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 3, 2, 4)
)
askeyEntityAlarmNotificationsGroup.setObjects(
    ("ASKEY-ENTITY-ALARM-MIB", "askeyEntityAlarmTrap")
)
if mibBuilder.loadTexts:
    askeyEntityAlarmNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

askeyEntityAlarmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 12, 3, 1, 1)
)
if mibBuilder.loadTexts:
    askeyEntityAlarmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASKEY-ENTITY-ALARM-MIB",
    **{"AskeyAlarmBit": AskeyAlarmBit,
       "AskeyAlarmSeverity": AskeyAlarmSeverity,
       "AskeyAlarmName": AskeyAlarmName,
       "AskeyAlarmList": AskeyAlarmList,
       "AskeyAlarmAction": AskeyAlarmAction,
       "askeyEntityAlarmMIB": askeyEntityAlarmMIB,
       "askeyEntityAlarmMIBObjects": askeyEntityAlarmMIBObjects,
       "aeAlarmDefinition": aeAlarmDefinition,
       "aeAlarmDefinitionTable": aeAlarmDefinitionTable,
       "aeAlarmDefinitionEntry": aeAlarmDefinitionEntry,
       "aeAlarmDefVendorTypeEnum": aeAlarmDefVendorTypeEnum,
       "aeAlarmDefType": aeAlarmDefType,
       "aeAlarmDefName": aeAlarmDefName,
       "aeAlarmDefDescr": aeAlarmDefDescr,
       "aeAlarmDefSeverity": aeAlarmDefSeverity,
       "aeAlarmDefFiltered": aeAlarmDefFiltered,
       "aeAlarmDefSuppressedby": aeAlarmDefSuppressedby,
       "aeAlarmMonitoring": aeAlarmMonitoring,
       "aeAlarmTable": aeAlarmTable,
       "aeAlarmEntry": aeAlarmEntry,
       "aeAlarmPhysicalIndex": aeAlarmPhysicalIndex,
       "aeAlarmPlannedVendorTypeEnum": aeAlarmPlannedVendorTypeEnum,
       "aeAlarmOnlineVendorTypeEnum": aeAlarmOnlineVendorTypeEnum,
       "aeAlarmList": aeAlarmList,
       "aeAlarmLastChange": aeAlarmLastChange,
       "aeAlarmSeverity": aeAlarmSeverity,
       "aeAlarmHistory": aeAlarmHistory,
       "aeHistoryAlarmTableSize": aeHistoryAlarmTableSize,
       "aeHistoryAlarmTable": aeHistoryAlarmTable,
       "aeHistoryAlarmEntry": aeHistoryAlarmEntry,
       "aeHistoryAlarmIndex": aeHistoryAlarmIndex,
       "aeHistoryAlarmPhysicalIndex": aeHistoryAlarmPhysicalIndex,
       "aeHistoryAlarmPlannedVendorTypeEnum": aeHistoryAlarmPlannedVendorTypeEnum,
       "aeHistoryAlarmOnlineVendorTypeEnum": aeHistoryAlarmOnlineVendorTypeEnum,
       "aeHistoryAlarmType": aeHistoryAlarmType,
       "aeHistoryAlarmTime": aeHistoryAlarmTime,
       "aeHistoryAlarmAction": aeHistoryAlarmAction,
       "aeRelayInTable": aeRelayInTable,
       "aeRelayInEntry": aeRelayInEntry,
       "aeRelayInPhysicalIndex": aeRelayInPhysicalIndex,
       "aeRelayInName": aeRelayInName,
       "aeRelayInNormalStatus": aeRelayInNormalStatus,
       "aeRelayInCurrentStatus": aeRelayInCurrentStatus,
       "askeyEntityAlarmMIBTraps": askeyEntityAlarmMIBTraps,
       "askeyEntityMIBTrapPrefix": askeyEntityMIBTrapPrefix,
       "askeyEntityAlarmTrap": askeyEntityAlarmTrap,
       "askeyEntityAlarmConformance": askeyEntityAlarmConformance,
       "askeyEntityAlarmCompliances": askeyEntityAlarmCompliances,
       "askeyEntityAlarmCompliance": askeyEntityAlarmCompliance,
       "askeyEntityAlarmGroups": askeyEntityAlarmGroups,
       "askeyEntityAlarmDefinitionGroup": askeyEntityAlarmDefinitionGroup,
       "askeyEntityAlarmMonitoringGroup": askeyEntityAlarmMonitoringGroup,
       "askeyEntityAlarmNotificationsGroup": askeyEntityAlarmNotificationsGroup}
)
