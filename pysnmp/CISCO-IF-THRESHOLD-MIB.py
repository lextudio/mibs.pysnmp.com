# SNMP MIB module (CISCO-IF-THRESHOLD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IF-THRESHOLD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:02:14 2024
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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

(DisplayString,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoIfThresholdMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 218)
)
ciscoIfThresholdMIB.setRevisions(
        ("2001-09-14 00:00",
         "2001-06-14 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CifthTemplateIndex(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )



class CifthTemplateIndexOrZero(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )



class CifthThresholdIndex(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )



class CifthThresholdList(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )



class CifthThresholdSeverity(Integer32, TextualConvention):
    status = "current"
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
        *(("degrade", 2),
          ("fail", 1),
          ("info", 3),
          ("other", 4))
    )



class CifthThresholdSeverityOrZero(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )



# MIB Managed Objects in the order of their OIDs

_CIfThresholdMIBObjects_ObjectIdentity = ObjectIdentity
cIfThresholdMIBObjects = _CIfThresholdMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 218, 1)
)
_CifthTemplateGroup_ObjectIdentity = ObjectIdentity
cifthTemplateGroup = _CifthTemplateGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 1)
)
_CifthTemplateIndexNext_Type = CifthTemplateIndexOrZero
_CifthTemplateIndexNext_Object = MibScalar
cifthTemplateIndexNext = _CifthTemplateIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 1, 1),
    _CifthTemplateIndexNext_Type()
)
cifthTemplateIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifthTemplateIndexNext.setStatus("current")
_CifthTemplateLastChange_Type = TimeStamp
_CifthTemplateLastChange_Object = MibScalar
cifthTemplateLastChange = _CifthTemplateLastChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 1, 2),
    _CifthTemplateLastChange_Type()
)
cifthTemplateLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifthTemplateLastChange.setStatus("current")
_CifthTemplateTable_Object = MibTable
cifthTemplateTable = _CifthTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cifthTemplateTable.setStatus("current")
_CifthTemplateEntry_Object = MibTableRow
cifthTemplateEntry = _CifthTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 1, 3, 1)
)
cifthTemplateEntry.setIndexNames(
    (0, "CISCO-IF-THRESHOLD-MIB", "cifthTemplateIndex"),
)
if mibBuilder.loadTexts:
    cifthTemplateEntry.setStatus("current")
_CifthTemplateIndex_Type = CifthTemplateIndex
_CifthTemplateIndex_Object = MibTableColumn
cifthTemplateIndex = _CifthTemplateIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 1, 3, 1, 1),
    _CifthTemplateIndex_Type()
)
cifthTemplateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cifthTemplateIndex.setStatus("current")


class _CifthTemplateName_Type(SnmpAdminString):
    """Custom type cifthTemplateName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CifthTemplateName_Type.__name__ = "SnmpAdminString"
_CifthTemplateName_Object = MibTableColumn
cifthTemplateName = _CifthTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 1, 3, 1, 2),
    _CifthTemplateName_Type()
)
cifthTemplateName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cifthTemplateName.setStatus("current")


class _CifthTemplateNotifyHoldDownType_Type(Integer32):
    """Custom type cifthTemplateNotifyHoldDownType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fireAndClearThresholds", 3),
          ("holdDownTimer", 2),
          ("other", 1))
    )


_CifthTemplateNotifyHoldDownType_Type.__name__ = "Integer32"
_CifthTemplateNotifyHoldDownType_Object = MibTableColumn
cifthTemplateNotifyHoldDownType = _CifthTemplateNotifyHoldDownType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 1, 3, 1, 3),
    _CifthTemplateNotifyHoldDownType_Type()
)
cifthTemplateNotifyHoldDownType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cifthTemplateNotifyHoldDownType.setStatus("current")


class _CifthTemplateNotifyHoldDownTime_Type(Unsigned32):
    """Custom type cifthTemplateNotifyHoldDownTime based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_CifthTemplateNotifyHoldDownTime_Type.__name__ = "Unsigned32"
_CifthTemplateNotifyHoldDownTime_Object = MibTableColumn
cifthTemplateNotifyHoldDownTime = _CifthTemplateNotifyHoldDownTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 1, 3, 1, 4),
    _CifthTemplateNotifyHoldDownTime_Type()
)
cifthTemplateNotifyHoldDownTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cifthTemplateNotifyHoldDownTime.setStatus("current")
if mibBuilder.loadTexts:
    cifthTemplateNotifyHoldDownTime.setUnits("seconds")
_CifthTemplateRowStatus_Type = RowStatus
_CifthTemplateRowStatus_Object = MibTableColumn
cifthTemplateRowStatus = _CifthTemplateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 1, 3, 1, 5),
    _CifthTemplateRowStatus_Type()
)
cifthTemplateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cifthTemplateRowStatus.setStatus("current")
_CifthThresholdLastChange_Type = TimeStamp
_CifthThresholdLastChange_Object = MibScalar
cifthThresholdLastChange = _CifthThresholdLastChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 1, 4),
    _CifthThresholdLastChange_Type()
)
cifthThresholdLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifthThresholdLastChange.setStatus("current")
_CifthThresholdTable_Object = MibTable
cifthThresholdTable = _CifthThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 1, 5)
)
if mibBuilder.loadTexts:
    cifthThresholdTable.setStatus("current")
_CifthThresholdEntry_Object = MibTableRow
cifthThresholdEntry = _CifthThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 1, 5, 1)
)
cifthThresholdEntry.setIndexNames(
    (0, "CISCO-IF-THRESHOLD-MIB", "cifthTemplateIndex"),
    (0, "CISCO-IF-THRESHOLD-MIB", "cifthThresholdIndex"),
)
if mibBuilder.loadTexts:
    cifthThresholdEntry.setStatus("current")
_CifthThresholdIndex_Type = CifthThresholdIndex
_CifthThresholdIndex_Object = MibTableColumn
cifthThresholdIndex = _CifthThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 1, 5, 1, 1),
    _CifthThresholdIndex_Type()
)
cifthThresholdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cifthThresholdIndex.setStatus("current")


class _CifthThresholdDescr_Type(SnmpAdminString):
    """Custom type cifthThresholdDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CifthThresholdDescr_Type.__name__ = "SnmpAdminString"
_CifthThresholdDescr_Object = MibTableColumn
cifthThresholdDescr = _CifthThresholdDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 1, 5, 1, 2),
    _CifthThresholdDescr_Type()
)
cifthThresholdDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cifthThresholdDescr.setStatus("current")
_CifthThresholdObject_Type = ObjectIdentifier
_CifthThresholdObject_Object = MibTableColumn
cifthThresholdObject = _CifthThresholdObject_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 1, 5, 1, 3),
    _CifthThresholdObject_Type()
)
cifthThresholdObject.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cifthThresholdObject.setStatus("current")
_CifthThresholdSeverity_Type = CifthThresholdSeverity
_CifthThresholdSeverity_Object = MibTableColumn
cifthThresholdSeverity = _CifthThresholdSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 1, 5, 1, 4),
    _CifthThresholdSeverity_Type()
)
cifthThresholdSeverity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cifthThresholdSeverity.setStatus("current")


class _CifthThresholdType_Type(Integer32):
    """Custom type cifthThresholdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("absoluteValue", 1),
          ("deltaValue", 2),
          ("rateOfIncreaseExponentXIfSpeed", 3))
    )


_CifthThresholdType_Type.__name__ = "Integer32"
_CifthThresholdType_Object = MibTableColumn
cifthThresholdType = _CifthThresholdType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 1, 5, 1, 5),
    _CifthThresholdType_Type()
)
cifthThresholdType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cifthThresholdType.setStatus("current")


class _CifthThresholdDirection_Type(Integer32):
    """Custom type cifthThresholdDirection based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("falling", 2),
          ("rising", 1))
    )


_CifthThresholdDirection_Type.__name__ = "Integer32"
_CifthThresholdDirection_Object = MibTableColumn
cifthThresholdDirection = _CifthThresholdDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 1, 5, 1, 6),
    _CifthThresholdDirection_Type()
)
cifthThresholdDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cifthThresholdDirection.setStatus("current")


class _CifthThresholdFiredValue_Type(Integer32):
    """Custom type cifthThresholdFiredValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CifthThresholdFiredValue_Type.__name__ = "Integer32"
_CifthThresholdFiredValue_Object = MibTableColumn
cifthThresholdFiredValue = _CifthThresholdFiredValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 1, 5, 1, 7),
    _CifthThresholdFiredValue_Type()
)
cifthThresholdFiredValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cifthThresholdFiredValue.setStatus("current")


class _CifthThresholdClearedValue_Type(Integer32):
    """Custom type cifthThresholdClearedValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CifthThresholdClearedValue_Type.__name__ = "Integer32"
_CifthThresholdClearedValue_Object = MibTableColumn
cifthThresholdClearedValue = _CifthThresholdClearedValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 1, 5, 1, 8),
    _CifthThresholdClearedValue_Type()
)
cifthThresholdClearedValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cifthThresholdClearedValue.setStatus("current")


class _CifthThresholdSampleInterval_Type(Unsigned32):
    """Custom type cifthThresholdSampleInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 900000),
    )


_CifthThresholdSampleInterval_Type.__name__ = "Unsigned32"
_CifthThresholdSampleInterval_Object = MibTableColumn
cifthThresholdSampleInterval = _CifthThresholdSampleInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 1, 5, 1, 9),
    _CifthThresholdSampleInterval_Type()
)
cifthThresholdSampleInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cifthThresholdSampleInterval.setStatus("current")
if mibBuilder.loadTexts:
    cifthThresholdSampleInterval.setUnits("milliseconds")


class _CifthThresholdApsSwitchover_Type(TruthValue):
    """Custom type cifthThresholdApsSwitchover based on TruthValue"""


_CifthThresholdApsSwitchover_Object = MibTableColumn
cifthThresholdApsSwitchover = _CifthThresholdApsSwitchover_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 1, 5, 1, 10),
    _CifthThresholdApsSwitchover_Type()
)
cifthThresholdApsSwitchover.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cifthThresholdApsSwitchover.setStatus("current")
_CifthThresholdRowStatus_Type = RowStatus
_CifthThresholdRowStatus_Object = MibTableColumn
cifthThresholdRowStatus = _CifthThresholdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 1, 5, 1, 11),
    _CifthThresholdRowStatus_Type()
)
cifthThresholdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cifthThresholdRowStatus.setStatus("current")
_CifthTemplateIfAssignGroup_ObjectIdentity = ObjectIdentity
cifthTemplateIfAssignGroup = _CifthTemplateIfAssignGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 2)
)
_CifthTemplateIfLastChange_Type = TimeStamp
_CifthTemplateIfLastChange_Object = MibScalar
cifthTemplateIfLastChange = _CifthTemplateIfLastChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 2, 1),
    _CifthTemplateIfLastChange_Type()
)
cifthTemplateIfLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifthTemplateIfLastChange.setStatus("current")
_CifthTemplateIfAssignTable_Object = MibTable
cifthTemplateIfAssignTable = _CifthTemplateIfAssignTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cifthTemplateIfAssignTable.setStatus("current")
_CifthTemplateIfAssignEntry_Object = MibTableRow
cifthTemplateIfAssignEntry = _CifthTemplateIfAssignEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 2, 2, 1)
)
cifthTemplateIfAssignEntry.setIndexNames(
    (0, "CISCO-IF-THRESHOLD-MIB", "cifthTemplateIndex"),
    (0, "CISCO-IF-THRESHOLD-MIB", "cifthTemplateIfAssignInterface"),
)
if mibBuilder.loadTexts:
    cifthTemplateIfAssignEntry.setStatus("current")
_CifthTemplateIfAssignInterface_Type = InterfaceIndex
_CifthTemplateIfAssignInterface_Object = MibTableColumn
cifthTemplateIfAssignInterface = _CifthTemplateIfAssignInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 2, 2, 1, 1),
    _CifthTemplateIfAssignInterface_Type()
)
cifthTemplateIfAssignInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cifthTemplateIfAssignInterface.setStatus("current")


class _CifthTemplateIfAssignOperStatus_Type(Integer32):
    """Custom type cifthTemplateIfAssignOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_CifthTemplateIfAssignOperStatus_Type.__name__ = "Integer32"
_CifthTemplateIfAssignOperStatus_Object = MibTableColumn
cifthTemplateIfAssignOperStatus = _CifthTemplateIfAssignOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 2, 2, 1, 2),
    _CifthTemplateIfAssignOperStatus_Type()
)
cifthTemplateIfAssignOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifthTemplateIfAssignOperStatus.setStatus("current")
_CifthTemplateIfAssignRowStatus_Type = RowStatus
_CifthTemplateIfAssignRowStatus_Object = MibTableColumn
cifthTemplateIfAssignRowStatus = _CifthTemplateIfAssignRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 2, 2, 1, 3),
    _CifthTemplateIfAssignRowStatus_Type()
)
cifthTemplateIfAssignRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cifthTemplateIfAssignRowStatus.setStatus("current")
_CifthIfThresholdFiredGroup_ObjectIdentity = ObjectIdentity
cifthIfThresholdFiredGroup = _CifthIfThresholdFiredGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 3)
)
_CifthThresholdFiredNotifyEnable_Type = CifthThresholdSeverityOrZero
_CifthThresholdFiredNotifyEnable_Object = MibScalar
cifthThresholdFiredNotifyEnable = _CifthThresholdFiredNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 3, 1),
    _CifthThresholdFiredNotifyEnable_Type()
)
cifthThresholdFiredNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cifthThresholdFiredNotifyEnable.setStatus("current")
_CifthThresholdFiredLastChange_Type = TimeStamp
_CifthThresholdFiredLastChange_Object = MibScalar
cifthThresholdFiredLastChange = _CifthThresholdFiredLastChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 3, 2),
    _CifthThresholdFiredLastChange_Type()
)
cifthThresholdFiredLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifthThresholdFiredLastChange.setStatus("current")
_CifthIfThresholdFiredTable_Object = MibTable
cifthIfThresholdFiredTable = _CifthIfThresholdFiredTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 3, 3)
)
if mibBuilder.loadTexts:
    cifthIfThresholdFiredTable.setStatus("current")
_CifthIfThresholdFiredEntry_Object = MibTableRow
cifthIfThresholdFiredEntry = _CifthIfThresholdFiredEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 3, 3, 1)
)
cifthIfThresholdFiredEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-IF-THRESHOLD-MIB", "cifthIfThresholdFiredTemplate"),
)
if mibBuilder.loadTexts:
    cifthIfThresholdFiredEntry.setStatus("current")
_CifthIfThresholdFiredTemplate_Type = CifthTemplateIndex
_CifthIfThresholdFiredTemplate_Object = MibTableColumn
cifthIfThresholdFiredTemplate = _CifthIfThresholdFiredTemplate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 3, 3, 1, 1),
    _CifthIfThresholdFiredTemplate_Type()
)
cifthIfThresholdFiredTemplate.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cifthIfThresholdFiredTemplate.setStatus("current")
_CifthIfThresholdsFired_Type = CifthThresholdList
_CifthIfThresholdsFired_Object = MibTableColumn
cifthIfThresholdsFired = _CifthIfThresholdsFired_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 3, 3, 1, 2),
    _CifthIfThresholdsFired_Type()
)
cifthIfThresholdsFired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifthIfThresholdsFired.setStatus("current")
_CifthIfLastThresholdFired_Type = CifthThresholdIndex
_CifthIfLastThresholdFired_Object = MibTableColumn
cifthIfLastThresholdFired = _CifthIfLastThresholdFired_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 3, 3, 1, 3),
    _CifthIfLastThresholdFired_Type()
)
cifthIfLastThresholdFired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifthIfLastThresholdFired.setStatus("current")
_CifthIfThresholdFiredLstChange_Type = TimeStamp
_CifthIfThresholdFiredLstChange_Object = MibTableColumn
cifthIfThresholdFiredLstChange = _CifthIfThresholdFiredLstChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 3, 3, 1, 4),
    _CifthIfThresholdFiredLstChange_Type()
)
cifthIfThresholdFiredLstChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifthIfThresholdFiredLstChange.setStatus("current")
_CifthIfThresholdFiredLstSeverity_Type = CifthThresholdSeverity
_CifthIfThresholdFiredLstSeverity_Object = MibTableColumn
cifthIfThresholdFiredLstSeverity = _CifthIfThresholdFiredLstSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 3, 3, 1, 5),
    _CifthIfThresholdFiredLstSeverity_Type()
)
cifthIfThresholdFiredLstSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifthIfThresholdFiredLstSeverity.setStatus("current")
_CifthIfThresholdFiredMaxSeverity_Type = CifthThresholdSeverity
_CifthIfThresholdFiredMaxSeverity_Object = MibTableColumn
cifthIfThresholdFiredMaxSeverity = _CifthIfThresholdFiredMaxSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 218, 1, 3, 3, 1, 6),
    _CifthIfThresholdFiredMaxSeverity_Type()
)
cifthIfThresholdFiredMaxSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cifthIfThresholdFiredMaxSeverity.setStatus("current")
_CIfThresholdMIBNotifications_ObjectIdentity = ObjectIdentity
cIfThresholdMIBNotifications = _CIfThresholdMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 218, 2)
)
_CifthMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
cifthMIBNotificationsPrefix = _CifthMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 218, 2, 0)
)
_CIfThresholdMIBConformance_ObjectIdentity = ObjectIdentity
cIfThresholdMIBConformance = _CIfThresholdMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 218, 3)
)
_CIfThresholdMIBCompliances_ObjectIdentity = ObjectIdentity
cIfThresholdMIBCompliances = _CIfThresholdMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 218, 3, 1)
)
_CIfThresholdMIBGroups_ObjectIdentity = ObjectIdentity
cIfThresholdMIBGroups = _CIfThresholdMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 218, 3, 2)
)

# Managed Objects groups

cIfThresholdTemplateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 218, 3, 2, 1)
)
cIfThresholdTemplateGroup.setObjects(
      *(("CISCO-IF-THRESHOLD-MIB", "cifthTemplateIndexNext"),
        ("CISCO-IF-THRESHOLD-MIB", "cifthTemplateLastChange"),
        ("CISCO-IF-THRESHOLD-MIB", "cifthTemplateName"),
        ("CISCO-IF-THRESHOLD-MIB", "cifthTemplateNotifyHoldDownType"),
        ("CISCO-IF-THRESHOLD-MIB", "cifthTemplateRowStatus"),
        ("CISCO-IF-THRESHOLD-MIB", "cifthThresholdLastChange"),
        ("CISCO-IF-THRESHOLD-MIB", "cifthThresholdDescr"),
        ("CISCO-IF-THRESHOLD-MIB", "cifthThresholdObject"),
        ("CISCO-IF-THRESHOLD-MIB", "cifthThresholdSeverity"),
        ("CISCO-IF-THRESHOLD-MIB", "cifthThresholdType"),
        ("CISCO-IF-THRESHOLD-MIB", "cifthThresholdDirection"),
        ("CISCO-IF-THRESHOLD-MIB", "cifthThresholdFiredValue"),
        ("CISCO-IF-THRESHOLD-MIB", "cifthThresholdSampleInterval"),
        ("CISCO-IF-THRESHOLD-MIB", "cifthThresholdRowStatus"),
        ("CISCO-IF-THRESHOLD-MIB", "cifthTemplateIfLastChange"),
        ("CISCO-IF-THRESHOLD-MIB", "cifthTemplateIfAssignOperStatus"),
        ("CISCO-IF-THRESHOLD-MIB", "cifthTemplateIfAssignRowStatus"))
)
if mibBuilder.loadTexts:
    cIfThresholdTemplateGroup.setStatus("current")

cIfThresholdFiredGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 218, 3, 2, 2)
)
cIfThresholdFiredGroup.setObjects(
      *(("CISCO-IF-THRESHOLD-MIB", "cifthThresholdFiredNotifyEnable"),
        ("CISCO-IF-THRESHOLD-MIB", "cifthThresholdFiredLastChange"),
        ("CISCO-IF-THRESHOLD-MIB", "cifthIfThresholdsFired"),
        ("CISCO-IF-THRESHOLD-MIB", "cifthIfLastThresholdFired"),
        ("CISCO-IF-THRESHOLD-MIB", "cifthIfThresholdFiredLstChange"),
        ("CISCO-IF-THRESHOLD-MIB", "cifthIfThresholdFiredLstSeverity"),
        ("CISCO-IF-THRESHOLD-MIB", "cifthIfThresholdFiredMaxSeverity"))
)
if mibBuilder.loadTexts:
    cIfThresholdFiredGroup.setStatus("current")

cifthHoldDownTimerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 218, 3, 2, 3)
)
cifthHoldDownTimerGroup.setObjects(
    ("CISCO-IF-THRESHOLD-MIB", "cifthTemplateNotifyHoldDownTime")
)
if mibBuilder.loadTexts:
    cifthHoldDownTimerGroup.setStatus("current")

cifthHoldDownHysteresisGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 218, 3, 2, 4)
)
cifthHoldDownHysteresisGroup.setObjects(
    ("CISCO-IF-THRESHOLD-MIB", "cifthThresholdClearedValue")
)
if mibBuilder.loadTexts:
    cifthHoldDownHysteresisGroup.setStatus("current")

cifthApsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 218, 3, 2, 5)
)
cifthApsGroup.setObjects(
    ("CISCO-IF-THRESHOLD-MIB", "cifthThresholdApsSwitchover")
)
if mibBuilder.loadTexts:
    cifthApsGroup.setStatus("current")


# Notification objects

cifthIfThresholdFired = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 218, 2, 0, 1)
)
cifthIfThresholdFired.setObjects(
      *(("CISCO-IF-THRESHOLD-MIB", "cifthIfLastThresholdFired"),
        ("CISCO-IF-THRESHOLD-MIB", "cifthIfThresholdFiredLstChange"),
        ("CISCO-IF-THRESHOLD-MIB", "cifthIfThresholdFiredLstSeverity"))
)
if mibBuilder.loadTexts:
    cifthIfThresholdFired.setStatus(
        "current"
    )

cifthIfThresholdCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 218, 2, 0, 2)
)
cifthIfThresholdCleared.setObjects(
      *(("CISCO-IF-THRESHOLD-MIB", "cifthIfLastThresholdFired"),
        ("CISCO-IF-THRESHOLD-MIB", "cifthIfThresholdFiredLstChange"),
        ("CISCO-IF-THRESHOLD-MIB", "cifthIfThresholdFiredLstSeverity"))
)
if mibBuilder.loadTexts:
    cifthIfThresholdCleared.setStatus(
        "current"
    )

cifthTemplateIfStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 218, 2, 0, 3)
)
cifthTemplateIfStatusChange.setObjects(
    ("CISCO-IF-THRESHOLD-MIB", "cifthTemplateIfAssignOperStatus")
)
if mibBuilder.loadTexts:
    cifthTemplateIfStatusChange.setStatus(
        "current"
    )


# Notifications groups

cIfThresholdNotifsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 218, 3, 2, 6)
)
cIfThresholdNotifsGroup.setObjects(
      *(("CISCO-IF-THRESHOLD-MIB", "cifthIfThresholdFired"),
        ("CISCO-IF-THRESHOLD-MIB", "cifthIfThresholdCleared"))
)
if mibBuilder.loadTexts:
    cIfThresholdNotifsGroup.setStatus(
        "current"
    )

cifthTemplateIfNotifsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 218, 3, 2, 7)
)
cifthTemplateIfNotifsGroup.setObjects(
    ("CISCO-IF-THRESHOLD-MIB", "cifthTemplateIfStatusChange")
)
if mibBuilder.loadTexts:
    cifthTemplateIfNotifsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cIfThresholdMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 218, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cIfThresholdMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IF-THRESHOLD-MIB",
    **{"CifthTemplateIndex": CifthTemplateIndex,
       "CifthTemplateIndexOrZero": CifthTemplateIndexOrZero,
       "CifthThresholdIndex": CifthThresholdIndex,
       "CifthThresholdList": CifthThresholdList,
       "CifthThresholdSeverity": CifthThresholdSeverity,
       "CifthThresholdSeverityOrZero": CifthThresholdSeverityOrZero,
       "ciscoIfThresholdMIB": ciscoIfThresholdMIB,
       "cIfThresholdMIBObjects": cIfThresholdMIBObjects,
       "cifthTemplateGroup": cifthTemplateGroup,
       "cifthTemplateIndexNext": cifthTemplateIndexNext,
       "cifthTemplateLastChange": cifthTemplateLastChange,
       "cifthTemplateTable": cifthTemplateTable,
       "cifthTemplateEntry": cifthTemplateEntry,
       "cifthTemplateIndex": cifthTemplateIndex,
       "cifthTemplateName": cifthTemplateName,
       "cifthTemplateNotifyHoldDownType": cifthTemplateNotifyHoldDownType,
       "cifthTemplateNotifyHoldDownTime": cifthTemplateNotifyHoldDownTime,
       "cifthTemplateRowStatus": cifthTemplateRowStatus,
       "cifthThresholdLastChange": cifthThresholdLastChange,
       "cifthThresholdTable": cifthThresholdTable,
       "cifthThresholdEntry": cifthThresholdEntry,
       "cifthThresholdIndex": cifthThresholdIndex,
       "cifthThresholdDescr": cifthThresholdDescr,
       "cifthThresholdObject": cifthThresholdObject,
       "cifthThresholdSeverity": cifthThresholdSeverity,
       "cifthThresholdType": cifthThresholdType,
       "cifthThresholdDirection": cifthThresholdDirection,
       "cifthThresholdFiredValue": cifthThresholdFiredValue,
       "cifthThresholdClearedValue": cifthThresholdClearedValue,
       "cifthThresholdSampleInterval": cifthThresholdSampleInterval,
       "cifthThresholdApsSwitchover": cifthThresholdApsSwitchover,
       "cifthThresholdRowStatus": cifthThresholdRowStatus,
       "cifthTemplateIfAssignGroup": cifthTemplateIfAssignGroup,
       "cifthTemplateIfLastChange": cifthTemplateIfLastChange,
       "cifthTemplateIfAssignTable": cifthTemplateIfAssignTable,
       "cifthTemplateIfAssignEntry": cifthTemplateIfAssignEntry,
       "cifthTemplateIfAssignInterface": cifthTemplateIfAssignInterface,
       "cifthTemplateIfAssignOperStatus": cifthTemplateIfAssignOperStatus,
       "cifthTemplateIfAssignRowStatus": cifthTemplateIfAssignRowStatus,
       "cifthIfThresholdFiredGroup": cifthIfThresholdFiredGroup,
       "cifthThresholdFiredNotifyEnable": cifthThresholdFiredNotifyEnable,
       "cifthThresholdFiredLastChange": cifthThresholdFiredLastChange,
       "cifthIfThresholdFiredTable": cifthIfThresholdFiredTable,
       "cifthIfThresholdFiredEntry": cifthIfThresholdFiredEntry,
       "cifthIfThresholdFiredTemplate": cifthIfThresholdFiredTemplate,
       "cifthIfThresholdsFired": cifthIfThresholdsFired,
       "cifthIfLastThresholdFired": cifthIfLastThresholdFired,
       "cifthIfThresholdFiredLstChange": cifthIfThresholdFiredLstChange,
       "cifthIfThresholdFiredLstSeverity": cifthIfThresholdFiredLstSeverity,
       "cifthIfThresholdFiredMaxSeverity": cifthIfThresholdFiredMaxSeverity,
       "cIfThresholdMIBNotifications": cIfThresholdMIBNotifications,
       "cifthMIBNotificationsPrefix": cifthMIBNotificationsPrefix,
       "cifthIfThresholdFired": cifthIfThresholdFired,
       "cifthIfThresholdCleared": cifthIfThresholdCleared,
       "cifthTemplateIfStatusChange": cifthTemplateIfStatusChange,
       "cIfThresholdMIBConformance": cIfThresholdMIBConformance,
       "cIfThresholdMIBCompliances": cIfThresholdMIBCompliances,
       "cIfThresholdMIBCompliance": cIfThresholdMIBCompliance,
       "cIfThresholdMIBGroups": cIfThresholdMIBGroups,
       "cIfThresholdTemplateGroup": cIfThresholdTemplateGroup,
       "cIfThresholdFiredGroup": cIfThresholdFiredGroup,
       "cifthHoldDownTimerGroup": cifthHoldDownTimerGroup,
       "cifthHoldDownHysteresisGroup": cifthHoldDownHysteresisGroup,
       "cifthApsGroup": cifthApsGroup,
       "cIfThresholdNotifsGroup": cIfThresholdNotifsGroup,
       "cifthTemplateIfNotifsGroup": cifthTemplateIfNotifsGroup}
)
