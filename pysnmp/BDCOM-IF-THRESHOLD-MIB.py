# SNMP MIB module (BDCOM-IF-THRESHOLD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BDCOM-IF-THRESHOLD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:46:33 2024
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

(bdMgmt,) = mibBuilder.importSymbols(
    "BDCOM-SMI",
    "bdMgmt")

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

bdcomIfThresholdMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 9, 218)
)
bdcomIfThresholdMIB.setRevisions(
        ("2003-10-16 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class BdifthTemplateIndex(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )



class BdifthTemplateIndexOrZero(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )



class BdifthThresholdIndex(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )



class BdifthThresholdList(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )



class BdifthThresholdSeverity(Integer32, TextualConvention):
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



class BdifthThresholdSeverityOrZero(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )



# MIB Managed Objects in the order of their OIDs

_BdIfThresholdMIBObjects_ObjectIdentity = ObjectIdentity
bdIfThresholdMIBObjects = _BdIfThresholdMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 9, 218, 1)
)
_BdifthTemplateGroup_ObjectIdentity = ObjectIdentity
bdifthTemplateGroup = _BdifthTemplateGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 1)
)
_BdifthTemplateIndexNext_Type = BdifthTemplateIndexOrZero
_BdifthTemplateIndexNext_Object = MibScalar
bdifthTemplateIndexNext = _BdifthTemplateIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 1, 1),
    _BdifthTemplateIndexNext_Type()
)
bdifthTemplateIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdifthTemplateIndexNext.setStatus("current")
_BdifthTemplateLastChange_Type = TimeStamp
_BdifthTemplateLastChange_Object = MibScalar
bdifthTemplateLastChange = _BdifthTemplateLastChange_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 1, 2),
    _BdifthTemplateLastChange_Type()
)
bdifthTemplateLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdifthTemplateLastChange.setStatus("current")
_BdifthTemplateTable_Object = MibTable
bdifthTemplateTable = _BdifthTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 1, 3)
)
if mibBuilder.loadTexts:
    bdifthTemplateTable.setStatus("current")
_BdifthTemplateEntry_Object = MibTableRow
bdifthTemplateEntry = _BdifthTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 1, 3, 1)
)
bdifthTemplateEntry.setIndexNames(
    (0, "BDCOM-IF-THRESHOLD-MIB", "bdifthTemplateIndex"),
)
if mibBuilder.loadTexts:
    bdifthTemplateEntry.setStatus("current")
_BdifthTemplateIndex_Type = BdifthTemplateIndex
_BdifthTemplateIndex_Object = MibTableColumn
bdifthTemplateIndex = _BdifthTemplateIndex_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 1, 3, 1, 1),
    _BdifthTemplateIndex_Type()
)
bdifthTemplateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bdifthTemplateIndex.setStatus("current")


class _BdifthTemplateName_Type(SnmpAdminString):
    """Custom type bdifthTemplateName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_BdifthTemplateName_Type.__name__ = "SnmpAdminString"
_BdifthTemplateName_Object = MibTableColumn
bdifthTemplateName = _BdifthTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 1, 3, 1, 2),
    _BdifthTemplateName_Type()
)
bdifthTemplateName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bdifthTemplateName.setStatus("current")


class _BdifthTemplateNotifyHoldDownType_Type(Integer32):
    """Custom type bdifthTemplateNotifyHoldDownType based on Integer32"""
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


_BdifthTemplateNotifyHoldDownType_Type.__name__ = "Integer32"
_BdifthTemplateNotifyHoldDownType_Object = MibTableColumn
bdifthTemplateNotifyHoldDownType = _BdifthTemplateNotifyHoldDownType_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 1, 3, 1, 3),
    _BdifthTemplateNotifyHoldDownType_Type()
)
bdifthTemplateNotifyHoldDownType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bdifthTemplateNotifyHoldDownType.setStatus("current")


class _BdifthTemplateNotifyHoldDownTime_Type(Unsigned32):
    """Custom type bdifthTemplateNotifyHoldDownTime based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_BdifthTemplateNotifyHoldDownTime_Type.__name__ = "Unsigned32"
_BdifthTemplateNotifyHoldDownTime_Object = MibTableColumn
bdifthTemplateNotifyHoldDownTime = _BdifthTemplateNotifyHoldDownTime_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 1, 3, 1, 4),
    _BdifthTemplateNotifyHoldDownTime_Type()
)
bdifthTemplateNotifyHoldDownTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bdifthTemplateNotifyHoldDownTime.setStatus("current")
if mibBuilder.loadTexts:
    bdifthTemplateNotifyHoldDownTime.setUnits("seconds")
_BdifthTemplateRowStatus_Type = RowStatus
_BdifthTemplateRowStatus_Object = MibTableColumn
bdifthTemplateRowStatus = _BdifthTemplateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 1, 3, 1, 5),
    _BdifthTemplateRowStatus_Type()
)
bdifthTemplateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bdifthTemplateRowStatus.setStatus("current")
_BdifthThresholdLastChange_Type = TimeStamp
_BdifthThresholdLastChange_Object = MibScalar
bdifthThresholdLastChange = _BdifthThresholdLastChange_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 1, 4),
    _BdifthThresholdLastChange_Type()
)
bdifthThresholdLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdifthThresholdLastChange.setStatus("current")
_BdifthThresholdTable_Object = MibTable
bdifthThresholdTable = _BdifthThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 1, 5)
)
if mibBuilder.loadTexts:
    bdifthThresholdTable.setStatus("current")
_BdifthThresholdEntry_Object = MibTableRow
bdifthThresholdEntry = _BdifthThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 1, 5, 1)
)
bdifthThresholdEntry.setIndexNames(
    (0, "BDCOM-IF-THRESHOLD-MIB", "bdifthTemplateIndex"),
    (0, "BDCOM-IF-THRESHOLD-MIB", "bdifthThresholdIndex"),
)
if mibBuilder.loadTexts:
    bdifthThresholdEntry.setStatus("current")
_BdifthThresholdIndex_Type = BdifthThresholdIndex
_BdifthThresholdIndex_Object = MibTableColumn
bdifthThresholdIndex = _BdifthThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 1, 5, 1, 1),
    _BdifthThresholdIndex_Type()
)
bdifthThresholdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bdifthThresholdIndex.setStatus("current")


class _BdifthThresholdDescr_Type(SnmpAdminString):
    """Custom type bdifthThresholdDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BdifthThresholdDescr_Type.__name__ = "SnmpAdminString"
_BdifthThresholdDescr_Object = MibTableColumn
bdifthThresholdDescr = _BdifthThresholdDescr_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 1, 5, 1, 2),
    _BdifthThresholdDescr_Type()
)
bdifthThresholdDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bdifthThresholdDescr.setStatus("current")
_BdifthThresholdObject_Type = ObjectIdentifier
_BdifthThresholdObject_Object = MibTableColumn
bdifthThresholdObject = _BdifthThresholdObject_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 1, 5, 1, 3),
    _BdifthThresholdObject_Type()
)
bdifthThresholdObject.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bdifthThresholdObject.setStatus("current")
_BdifthThresholdSeverity_Type = BdifthThresholdSeverity
_BdifthThresholdSeverity_Object = MibTableColumn
bdifthThresholdSeverity = _BdifthThresholdSeverity_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 1, 5, 1, 4),
    _BdifthThresholdSeverity_Type()
)
bdifthThresholdSeverity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bdifthThresholdSeverity.setStatus("current")


class _BdifthThresholdType_Type(Integer32):
    """Custom type bdifthThresholdType based on Integer32"""
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


_BdifthThresholdType_Type.__name__ = "Integer32"
_BdifthThresholdType_Object = MibTableColumn
bdifthThresholdType = _BdifthThresholdType_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 1, 5, 1, 5),
    _BdifthThresholdType_Type()
)
bdifthThresholdType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bdifthThresholdType.setStatus("current")


class _BdifthThresholdDirection_Type(Integer32):
    """Custom type bdifthThresholdDirection based on Integer32"""
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


_BdifthThresholdDirection_Type.__name__ = "Integer32"
_BdifthThresholdDirection_Object = MibTableColumn
bdifthThresholdDirection = _BdifthThresholdDirection_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 1, 5, 1, 6),
    _BdifthThresholdDirection_Type()
)
bdifthThresholdDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bdifthThresholdDirection.setStatus("current")


class _BdifthThresholdFiredValue_Type(Integer32):
    """Custom type bdifthThresholdFiredValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_BdifthThresholdFiredValue_Type.__name__ = "Integer32"
_BdifthThresholdFiredValue_Object = MibTableColumn
bdifthThresholdFiredValue = _BdifthThresholdFiredValue_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 1, 5, 1, 7),
    _BdifthThresholdFiredValue_Type()
)
bdifthThresholdFiredValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bdifthThresholdFiredValue.setStatus("current")


class _BdifthThresholdClearedValue_Type(Integer32):
    """Custom type bdifthThresholdClearedValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_BdifthThresholdClearedValue_Type.__name__ = "Integer32"
_BdifthThresholdClearedValue_Object = MibTableColumn
bdifthThresholdClearedValue = _BdifthThresholdClearedValue_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 1, 5, 1, 8),
    _BdifthThresholdClearedValue_Type()
)
bdifthThresholdClearedValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bdifthThresholdClearedValue.setStatus("current")


class _BdifthThresholdSampleInterval_Type(Unsigned32):
    """Custom type bdifthThresholdSampleInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 900000),
    )


_BdifthThresholdSampleInterval_Type.__name__ = "Unsigned32"
_BdifthThresholdSampleInterval_Object = MibTableColumn
bdifthThresholdSampleInterval = _BdifthThresholdSampleInterval_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 1, 5, 1, 9),
    _BdifthThresholdSampleInterval_Type()
)
bdifthThresholdSampleInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bdifthThresholdSampleInterval.setStatus("current")
if mibBuilder.loadTexts:
    bdifthThresholdSampleInterval.setUnits("milliseconds")


class _BdifthThresholdApsSwitchover_Type(TruthValue):
    """Custom type bdifthThresholdApsSwitchover based on TruthValue"""


_BdifthThresholdApsSwitchover_Object = MibTableColumn
bdifthThresholdApsSwitchover = _BdifthThresholdApsSwitchover_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 1, 5, 1, 10),
    _BdifthThresholdApsSwitchover_Type()
)
bdifthThresholdApsSwitchover.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bdifthThresholdApsSwitchover.setStatus("current")
_BdifthThresholdRowStatus_Type = RowStatus
_BdifthThresholdRowStatus_Object = MibTableColumn
bdifthThresholdRowStatus = _BdifthThresholdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 1, 5, 1, 11),
    _BdifthThresholdRowStatus_Type()
)
bdifthThresholdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bdifthThresholdRowStatus.setStatus("current")
_BdifthTemplateIfAssignGroup_ObjectIdentity = ObjectIdentity
bdifthTemplateIfAssignGroup = _BdifthTemplateIfAssignGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 2)
)
_BdifthTemplateIfLastChange_Type = TimeStamp
_BdifthTemplateIfLastChange_Object = MibScalar
bdifthTemplateIfLastChange = _BdifthTemplateIfLastChange_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 2, 1),
    _BdifthTemplateIfLastChange_Type()
)
bdifthTemplateIfLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdifthTemplateIfLastChange.setStatus("current")
_BdifthTemplateIfAssignTable_Object = MibTable
bdifthTemplateIfAssignTable = _BdifthTemplateIfAssignTable_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 2, 2)
)
if mibBuilder.loadTexts:
    bdifthTemplateIfAssignTable.setStatus("current")
_BdifthTemplateIfAssignEntry_Object = MibTableRow
bdifthTemplateIfAssignEntry = _BdifthTemplateIfAssignEntry_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 2, 2, 1)
)
bdifthTemplateIfAssignEntry.setIndexNames(
    (0, "BDCOM-IF-THRESHOLD-MIB", "bdifthTemplateIndex"),
    (0, "BDCOM-IF-THRESHOLD-MIB", "bdifthTemplateIfAssignInterface"),
)
if mibBuilder.loadTexts:
    bdifthTemplateIfAssignEntry.setStatus("current")
_BdifthTemplateIfAssignInterface_Type = InterfaceIndex
_BdifthTemplateIfAssignInterface_Object = MibTableColumn
bdifthTemplateIfAssignInterface = _BdifthTemplateIfAssignInterface_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 2, 2, 1, 1),
    _BdifthTemplateIfAssignInterface_Type()
)
bdifthTemplateIfAssignInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bdifthTemplateIfAssignInterface.setStatus("current")


class _BdifthTemplateIfAssignOperStatus_Type(Integer32):
    """Custom type bdifthTemplateIfAssignOperStatus based on Integer32"""
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


_BdifthTemplateIfAssignOperStatus_Type.__name__ = "Integer32"
_BdifthTemplateIfAssignOperStatus_Object = MibTableColumn
bdifthTemplateIfAssignOperStatus = _BdifthTemplateIfAssignOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 2, 2, 1, 2),
    _BdifthTemplateIfAssignOperStatus_Type()
)
bdifthTemplateIfAssignOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdifthTemplateIfAssignOperStatus.setStatus("current")
_BdifthTemplateIfAssignRowStatus_Type = RowStatus
_BdifthTemplateIfAssignRowStatus_Object = MibTableColumn
bdifthTemplateIfAssignRowStatus = _BdifthTemplateIfAssignRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 2, 2, 1, 3),
    _BdifthTemplateIfAssignRowStatus_Type()
)
bdifthTemplateIfAssignRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bdifthTemplateIfAssignRowStatus.setStatus("current")
_BdifthIfThresholdFiredGroup_ObjectIdentity = ObjectIdentity
bdifthIfThresholdFiredGroup = _BdifthIfThresholdFiredGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 3)
)
_BdifthThresholdFiredNotifyEnable_Type = BdifthThresholdSeverityOrZero
_BdifthThresholdFiredNotifyEnable_Object = MibScalar
bdifthThresholdFiredNotifyEnable = _BdifthThresholdFiredNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 3, 1),
    _BdifthThresholdFiredNotifyEnable_Type()
)
bdifthThresholdFiredNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bdifthThresholdFiredNotifyEnable.setStatus("current")
_BdifthThresholdFiredLastChange_Type = TimeStamp
_BdifthThresholdFiredLastChange_Object = MibScalar
bdifthThresholdFiredLastChange = _BdifthThresholdFiredLastChange_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 3, 2),
    _BdifthThresholdFiredLastChange_Type()
)
bdifthThresholdFiredLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdifthThresholdFiredLastChange.setStatus("current")
_BdifthIfThresholdFiredTable_Object = MibTable
bdifthIfThresholdFiredTable = _BdifthIfThresholdFiredTable_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 3, 3)
)
if mibBuilder.loadTexts:
    bdifthIfThresholdFiredTable.setStatus("current")
_BdifthIfThresholdFiredEntry_Object = MibTableRow
bdifthIfThresholdFiredEntry = _BdifthIfThresholdFiredEntry_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 3, 3, 1)
)
bdifthIfThresholdFiredEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "BDCOM-IF-THRESHOLD-MIB", "bdifthIfThresholdFiredTemplate"),
)
if mibBuilder.loadTexts:
    bdifthIfThresholdFiredEntry.setStatus("current")
_BdifthIfThresholdFiredTemplate_Type = BdifthTemplateIndex
_BdifthIfThresholdFiredTemplate_Object = MibTableColumn
bdifthIfThresholdFiredTemplate = _BdifthIfThresholdFiredTemplate_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 3, 3, 1, 1),
    _BdifthIfThresholdFiredTemplate_Type()
)
bdifthIfThresholdFiredTemplate.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bdifthIfThresholdFiredTemplate.setStatus("current")
_BdifthIfThresholdsFired_Type = BdifthThresholdList
_BdifthIfThresholdsFired_Object = MibTableColumn
bdifthIfThresholdsFired = _BdifthIfThresholdsFired_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 3, 3, 1, 2),
    _BdifthIfThresholdsFired_Type()
)
bdifthIfThresholdsFired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdifthIfThresholdsFired.setStatus("current")
_BdifthIfLastThresholdFired_Type = BdifthThresholdIndex
_BdifthIfLastThresholdFired_Object = MibTableColumn
bdifthIfLastThresholdFired = _BdifthIfLastThresholdFired_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 3, 3, 1, 3),
    _BdifthIfLastThresholdFired_Type()
)
bdifthIfLastThresholdFired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdifthIfLastThresholdFired.setStatus("current")
_BdifthIfThresholdFiredLstChange_Type = TimeStamp
_BdifthIfThresholdFiredLstChange_Object = MibTableColumn
bdifthIfThresholdFiredLstChange = _BdifthIfThresholdFiredLstChange_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 3, 3, 1, 4),
    _BdifthIfThresholdFiredLstChange_Type()
)
bdifthIfThresholdFiredLstChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdifthIfThresholdFiredLstChange.setStatus("current")
_BdifthIfThresholdFiredLstSeverity_Type = BdifthThresholdSeverity
_BdifthIfThresholdFiredLstSeverity_Object = MibTableColumn
bdifthIfThresholdFiredLstSeverity = _BdifthIfThresholdFiredLstSeverity_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 3, 3, 1, 5),
    _BdifthIfThresholdFiredLstSeverity_Type()
)
bdifthIfThresholdFiredLstSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdifthIfThresholdFiredLstSeverity.setStatus("current")
_BdifthIfThresholdFiredMaxSeverity_Type = BdifthThresholdSeverity
_BdifthIfThresholdFiredMaxSeverity_Object = MibTableColumn
bdifthIfThresholdFiredMaxSeverity = _BdifthIfThresholdFiredMaxSeverity_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 218, 1, 3, 3, 1, 6),
    _BdifthIfThresholdFiredMaxSeverity_Type()
)
bdifthIfThresholdFiredMaxSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdifthIfThresholdFiredMaxSeverity.setStatus("current")
_BdIfThresholdMIBNotifications_ObjectIdentity = ObjectIdentity
bdIfThresholdMIBNotifications = _BdIfThresholdMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 9, 218, 2)
)
_BdifthMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
bdifthMIBNotificationsPrefix = _BdifthMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 9, 218, 2, 0)
)
_BdIfThresholdMIBConformance_ObjectIdentity = ObjectIdentity
bdIfThresholdMIBConformance = _BdIfThresholdMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 9, 218, 3)
)
_BdIfThresholdMIBCompliances_ObjectIdentity = ObjectIdentity
bdIfThresholdMIBCompliances = _BdIfThresholdMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 9, 218, 3, 1)
)
_BdIfThresholdMIBGroups_ObjectIdentity = ObjectIdentity
bdIfThresholdMIBGroups = _BdIfThresholdMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 9, 218, 3, 2)
)

# Managed Objects groups

bdIfThresholdTemplateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3320, 9, 218, 3, 2, 1)
)
bdIfThresholdTemplateGroup.setObjects(
      *(("BDCOM-IF-THRESHOLD-MIB", "bdifthTemplateIndexNext"),
        ("BDCOM-IF-THRESHOLD-MIB", "bdifthTemplateLastChange"),
        ("BDCOM-IF-THRESHOLD-MIB", "bdifthTemplateName"),
        ("BDCOM-IF-THRESHOLD-MIB", "bdifthTemplateNotifyHoldDownType"),
        ("BDCOM-IF-THRESHOLD-MIB", "bdifthTemplateRowStatus"),
        ("BDCOM-IF-THRESHOLD-MIB", "bdifthThresholdLastChange"),
        ("BDCOM-IF-THRESHOLD-MIB", "bdifthThresholdDescr"),
        ("BDCOM-IF-THRESHOLD-MIB", "bdifthThresholdObject"),
        ("BDCOM-IF-THRESHOLD-MIB", "bdifthThresholdSeverity"),
        ("BDCOM-IF-THRESHOLD-MIB", "bdifthThresholdType"),
        ("BDCOM-IF-THRESHOLD-MIB", "bdifthThresholdDirection"),
        ("BDCOM-IF-THRESHOLD-MIB", "bdifthThresholdFiredValue"),
        ("BDCOM-IF-THRESHOLD-MIB", "bdifthThresholdSampleInterval"),
        ("BDCOM-IF-THRESHOLD-MIB", "bdifthThresholdRowStatus"),
        ("BDCOM-IF-THRESHOLD-MIB", "bdifthTemplateIfLastChange"),
        ("BDCOM-IF-THRESHOLD-MIB", "bdifthTemplateIfAssignOperStatus"),
        ("BDCOM-IF-THRESHOLD-MIB", "bdifthTemplateIfAssignRowStatus"))
)
if mibBuilder.loadTexts:
    bdIfThresholdTemplateGroup.setStatus("current")

bdIfThresholdFiredGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3320, 9, 218, 3, 2, 2)
)
bdIfThresholdFiredGroup.setObjects(
      *(("BDCOM-IF-THRESHOLD-MIB", "bdifthThresholdFiredNotifyEnable"),
        ("BDCOM-IF-THRESHOLD-MIB", "bdifthThresholdFiredLastChange"),
        ("BDCOM-IF-THRESHOLD-MIB", "bdifthIfThresholdsFired"),
        ("BDCOM-IF-THRESHOLD-MIB", "bdifthIfLastThresholdFired"),
        ("BDCOM-IF-THRESHOLD-MIB", "bdifthIfThresholdFiredLstChange"),
        ("BDCOM-IF-THRESHOLD-MIB", "bdifthIfThresholdFiredLstSeverity"),
        ("BDCOM-IF-THRESHOLD-MIB", "bdifthIfThresholdFiredMaxSeverity"))
)
if mibBuilder.loadTexts:
    bdIfThresholdFiredGroup.setStatus("current")

bdifthHoldDownTimerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3320, 9, 218, 3, 2, 3)
)
bdifthHoldDownTimerGroup.setObjects(
    ("BDCOM-IF-THRESHOLD-MIB", "bdifthTemplateNotifyHoldDownTime")
)
if mibBuilder.loadTexts:
    bdifthHoldDownTimerGroup.setStatus("current")

bdifthHoldDownHysteresisGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3320, 9, 218, 3, 2, 4)
)
bdifthHoldDownHysteresisGroup.setObjects(
    ("BDCOM-IF-THRESHOLD-MIB", "bdifthThresholdClearedValue")
)
if mibBuilder.loadTexts:
    bdifthHoldDownHysteresisGroup.setStatus("current")

bdifthApsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3320, 9, 218, 3, 2, 5)
)
bdifthApsGroup.setObjects(
    ("BDCOM-IF-THRESHOLD-MIB", "bdifthThresholdApsSwitchover")
)
if mibBuilder.loadTexts:
    bdifthApsGroup.setStatus("current")


# Notification objects

bdifthIfThresholdFired = NotificationType(
    (1, 3, 6, 1, 4, 1, 3320, 9, 218, 2, 0, 1)
)
bdifthIfThresholdFired.setObjects(
      *(("BDCOM-IF-THRESHOLD-MIB", "bdifthIfLastThresholdFired"),
        ("BDCOM-IF-THRESHOLD-MIB", "bdifthIfThresholdFiredLstChange"),
        ("BDCOM-IF-THRESHOLD-MIB", "bdifthIfThresholdFiredLstSeverity"))
)
if mibBuilder.loadTexts:
    bdifthIfThresholdFired.setStatus(
        "current"
    )

bdifthIfThresholdCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 3320, 9, 218, 2, 0, 2)
)
bdifthIfThresholdCleared.setObjects(
      *(("BDCOM-IF-THRESHOLD-MIB", "bdifthIfLastThresholdFired"),
        ("BDCOM-IF-THRESHOLD-MIB", "bdifthIfThresholdFiredLstChange"),
        ("BDCOM-IF-THRESHOLD-MIB", "bdifthIfThresholdFiredLstSeverity"))
)
if mibBuilder.loadTexts:
    bdifthIfThresholdCleared.setStatus(
        "current"
    )

bdifthTemplateIfStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 3320, 9, 218, 2, 0, 3)
)
bdifthTemplateIfStatusChange.setObjects(
    ("BDCOM-IF-THRESHOLD-MIB", "bdifthTemplateIfAssignOperStatus")
)
if mibBuilder.loadTexts:
    bdifthTemplateIfStatusChange.setStatus(
        "current"
    )


# Notifications groups

bdIfThresholdNotifsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 3320, 9, 218, 3, 2, 6)
)
bdIfThresholdNotifsGroup.setObjects(
      *(("BDCOM-IF-THRESHOLD-MIB", "bdifthIfThresholdFired"),
        ("BDCOM-IF-THRESHOLD-MIB", "bdifthIfThresholdCleared"))
)
if mibBuilder.loadTexts:
    bdIfThresholdNotifsGroup.setStatus(
        "current"
    )

bdifthTemplateIfNotifsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 3320, 9, 218, 3, 2, 7)
)
bdifthTemplateIfNotifsGroup.setObjects(
    ("BDCOM-IF-THRESHOLD-MIB", "bdifthTemplateIfStatusChange")
)
if mibBuilder.loadTexts:
    bdifthTemplateIfNotifsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

bdIfThresholdMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3320, 9, 218, 3, 1, 1)
)
if mibBuilder.loadTexts:
    bdIfThresholdMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BDCOM-IF-THRESHOLD-MIB",
    **{"BdifthTemplateIndex": BdifthTemplateIndex,
       "BdifthTemplateIndexOrZero": BdifthTemplateIndexOrZero,
       "BdifthThresholdIndex": BdifthThresholdIndex,
       "BdifthThresholdList": BdifthThresholdList,
       "BdifthThresholdSeverity": BdifthThresholdSeverity,
       "BdifthThresholdSeverityOrZero": BdifthThresholdSeverityOrZero,
       "bdcomIfThresholdMIB": bdcomIfThresholdMIB,
       "bdIfThresholdMIBObjects": bdIfThresholdMIBObjects,
       "bdifthTemplateGroup": bdifthTemplateGroup,
       "bdifthTemplateIndexNext": bdifthTemplateIndexNext,
       "bdifthTemplateLastChange": bdifthTemplateLastChange,
       "bdifthTemplateTable": bdifthTemplateTable,
       "bdifthTemplateEntry": bdifthTemplateEntry,
       "bdifthTemplateIndex": bdifthTemplateIndex,
       "bdifthTemplateName": bdifthTemplateName,
       "bdifthTemplateNotifyHoldDownType": bdifthTemplateNotifyHoldDownType,
       "bdifthTemplateNotifyHoldDownTime": bdifthTemplateNotifyHoldDownTime,
       "bdifthTemplateRowStatus": bdifthTemplateRowStatus,
       "bdifthThresholdLastChange": bdifthThresholdLastChange,
       "bdifthThresholdTable": bdifthThresholdTable,
       "bdifthThresholdEntry": bdifthThresholdEntry,
       "bdifthThresholdIndex": bdifthThresholdIndex,
       "bdifthThresholdDescr": bdifthThresholdDescr,
       "bdifthThresholdObject": bdifthThresholdObject,
       "bdifthThresholdSeverity": bdifthThresholdSeverity,
       "bdifthThresholdType": bdifthThresholdType,
       "bdifthThresholdDirection": bdifthThresholdDirection,
       "bdifthThresholdFiredValue": bdifthThresholdFiredValue,
       "bdifthThresholdClearedValue": bdifthThresholdClearedValue,
       "bdifthThresholdSampleInterval": bdifthThresholdSampleInterval,
       "bdifthThresholdApsSwitchover": bdifthThresholdApsSwitchover,
       "bdifthThresholdRowStatus": bdifthThresholdRowStatus,
       "bdifthTemplateIfAssignGroup": bdifthTemplateIfAssignGroup,
       "bdifthTemplateIfLastChange": bdifthTemplateIfLastChange,
       "bdifthTemplateIfAssignTable": bdifthTemplateIfAssignTable,
       "bdifthTemplateIfAssignEntry": bdifthTemplateIfAssignEntry,
       "bdifthTemplateIfAssignInterface": bdifthTemplateIfAssignInterface,
       "bdifthTemplateIfAssignOperStatus": bdifthTemplateIfAssignOperStatus,
       "bdifthTemplateIfAssignRowStatus": bdifthTemplateIfAssignRowStatus,
       "bdifthIfThresholdFiredGroup": bdifthIfThresholdFiredGroup,
       "bdifthThresholdFiredNotifyEnable": bdifthThresholdFiredNotifyEnable,
       "bdifthThresholdFiredLastChange": bdifthThresholdFiredLastChange,
       "bdifthIfThresholdFiredTable": bdifthIfThresholdFiredTable,
       "bdifthIfThresholdFiredEntry": bdifthIfThresholdFiredEntry,
       "bdifthIfThresholdFiredTemplate": bdifthIfThresholdFiredTemplate,
       "bdifthIfThresholdsFired": bdifthIfThresholdsFired,
       "bdifthIfLastThresholdFired": bdifthIfLastThresholdFired,
       "bdifthIfThresholdFiredLstChange": bdifthIfThresholdFiredLstChange,
       "bdifthIfThresholdFiredLstSeverity": bdifthIfThresholdFiredLstSeverity,
       "bdifthIfThresholdFiredMaxSeverity": bdifthIfThresholdFiredMaxSeverity,
       "bdIfThresholdMIBNotifications": bdIfThresholdMIBNotifications,
       "bdifthMIBNotificationsPrefix": bdifthMIBNotificationsPrefix,
       "bdifthIfThresholdFired": bdifthIfThresholdFired,
       "bdifthIfThresholdCleared": bdifthIfThresholdCleared,
       "bdifthTemplateIfStatusChange": bdifthTemplateIfStatusChange,
       "bdIfThresholdMIBConformance": bdIfThresholdMIBConformance,
       "bdIfThresholdMIBCompliances": bdIfThresholdMIBCompliances,
       "bdIfThresholdMIBCompliance": bdIfThresholdMIBCompliance,
       "bdIfThresholdMIBGroups": bdIfThresholdMIBGroups,
       "bdIfThresholdTemplateGroup": bdIfThresholdTemplateGroup,
       "bdIfThresholdFiredGroup": bdIfThresholdFiredGroup,
       "bdifthHoldDownTimerGroup": bdifthHoldDownTimerGroup,
       "bdifthHoldDownHysteresisGroup": bdifthHoldDownHysteresisGroup,
       "bdifthApsGroup": bdifthApsGroup,
       "bdIfThresholdNotifsGroup": bdIfThresholdNotifsGroup,
       "bdifthTemplateIfNotifsGroup": bdifthTemplateIfNotifsGroup}
)
