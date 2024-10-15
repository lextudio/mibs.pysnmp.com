# SNMP MIB module (NMS-IF-THRESHOLD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NMS-IF-THRESHOLD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:27:56 2024
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(nmsMgmt,) = mibBuilder.importSymbols(
    "NMS-SMI",
    "nmsMgmt")

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

nmsIfThresholdMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 218)
)
nmsIfThresholdMIB.setRevisions(
        ("2003-10-16 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class NMSifthTemplateIndex(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )



class NMSifthTemplateIndexOrZero(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )



class NMSifthThresholdIndex(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )



class NMSifthThresholdList(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )



class NMSifthThresholdSeverity(Integer32, TextualConvention):
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



class NMSifthThresholdSeverityOrZero(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )



# MIB Managed Objects in the order of their OIDs

_NmsIfThresholdMIBObjects_ObjectIdentity = ObjectIdentity
nmsIfThresholdMIBObjects = _NmsIfThresholdMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1)
)
_NmsifthTemplateGroup_ObjectIdentity = ObjectIdentity
nmsifthTemplateGroup = _NmsifthTemplateGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 1)
)
_NmsifthTemplateIndexNext_Type = NMSifthTemplateIndexOrZero
_NmsifthTemplateIndexNext_Object = MibScalar
nmsifthTemplateIndexNext = _NmsifthTemplateIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 1, 1),
    _NmsifthTemplateIndexNext_Type()
)
nmsifthTemplateIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsifthTemplateIndexNext.setStatus("current")
_NmsifthTemplateLastChange_Type = TimeStamp
_NmsifthTemplateLastChange_Object = MibScalar
nmsifthTemplateLastChange = _NmsifthTemplateLastChange_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 1, 2),
    _NmsifthTemplateLastChange_Type()
)
nmsifthTemplateLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsifthTemplateLastChange.setStatus("current")
_NmsifthTemplateTable_Object = MibTable
nmsifthTemplateTable = _NmsifthTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 1, 3)
)
if mibBuilder.loadTexts:
    nmsifthTemplateTable.setStatus("current")
_NmsifthTemplateEntry_Object = MibTableRow
nmsifthTemplateEntry = _NmsifthTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 1, 3, 1)
)
nmsifthTemplateEntry.setIndexNames(
    (0, "NMS-IF-THRESHOLD-MIB", "nmsifthTemplateIndex"),
)
if mibBuilder.loadTexts:
    nmsifthTemplateEntry.setStatus("current")
_NmsifthTemplateIndex_Type = NMSifthTemplateIndex
_NmsifthTemplateIndex_Object = MibTableColumn
nmsifthTemplateIndex = _NmsifthTemplateIndex_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 1, 3, 1, 1),
    _NmsifthTemplateIndex_Type()
)
nmsifthTemplateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nmsifthTemplateIndex.setStatus("current")


class _NmsifthTemplateName_Type(SnmpAdminString):
    """Custom type nmsifthTemplateName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_NmsifthTemplateName_Type.__name__ = "SnmpAdminString"
_NmsifthTemplateName_Object = MibTableColumn
nmsifthTemplateName = _NmsifthTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 1, 3, 1, 2),
    _NmsifthTemplateName_Type()
)
nmsifthTemplateName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nmsifthTemplateName.setStatus("current")


class _NmsifthTemplateNotifyHoldDownType_Type(Integer32):
    """Custom type nmsifthTemplateNotifyHoldDownType based on Integer32"""
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


_NmsifthTemplateNotifyHoldDownType_Type.__name__ = "Integer32"
_NmsifthTemplateNotifyHoldDownType_Object = MibTableColumn
nmsifthTemplateNotifyHoldDownType = _NmsifthTemplateNotifyHoldDownType_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 1, 3, 1, 3),
    _NmsifthTemplateNotifyHoldDownType_Type()
)
nmsifthTemplateNotifyHoldDownType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nmsifthTemplateNotifyHoldDownType.setStatus("current")


class _NmsifthTemplateNotifyHoldDownTime_Type(Unsigned32):
    """Custom type nmsifthTemplateNotifyHoldDownTime based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_NmsifthTemplateNotifyHoldDownTime_Type.__name__ = "Unsigned32"
_NmsifthTemplateNotifyHoldDownTime_Object = MibTableColumn
nmsifthTemplateNotifyHoldDownTime = _NmsifthTemplateNotifyHoldDownTime_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 1, 3, 1, 4),
    _NmsifthTemplateNotifyHoldDownTime_Type()
)
nmsifthTemplateNotifyHoldDownTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nmsifthTemplateNotifyHoldDownTime.setStatus("current")
if mibBuilder.loadTexts:
    nmsifthTemplateNotifyHoldDownTime.setUnits("seconds")
_NmsifthTemplateRowStatus_Type = RowStatus
_NmsifthTemplateRowStatus_Object = MibTableColumn
nmsifthTemplateRowStatus = _NmsifthTemplateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 1, 3, 1, 5),
    _NmsifthTemplateRowStatus_Type()
)
nmsifthTemplateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nmsifthTemplateRowStatus.setStatus("current")
_NmsifthThresholdLastChange_Type = TimeStamp
_NmsifthThresholdLastChange_Object = MibScalar
nmsifthThresholdLastChange = _NmsifthThresholdLastChange_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 1, 4),
    _NmsifthThresholdLastChange_Type()
)
nmsifthThresholdLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsifthThresholdLastChange.setStatus("current")
_NmsifthThresholdTable_Object = MibTable
nmsifthThresholdTable = _NmsifthThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 1, 5)
)
if mibBuilder.loadTexts:
    nmsifthThresholdTable.setStatus("current")
_NmsifthThresholdEntry_Object = MibTableRow
nmsifthThresholdEntry = _NmsifthThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 1, 5, 1)
)
nmsifthThresholdEntry.setIndexNames(
    (0, "NMS-IF-THRESHOLD-MIB", "nmsifthTemplateIndex"),
    (0, "NMS-IF-THRESHOLD-MIB", "nmsifthThresholdIndex"),
)
if mibBuilder.loadTexts:
    nmsifthThresholdEntry.setStatus("current")
_NmsifthThresholdIndex_Type = NMSifthThresholdIndex
_NmsifthThresholdIndex_Object = MibTableColumn
nmsifthThresholdIndex = _NmsifthThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 1, 5, 1, 1),
    _NmsifthThresholdIndex_Type()
)
nmsifthThresholdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nmsifthThresholdIndex.setStatus("current")


class _NmsifthThresholdDescr_Type(SnmpAdminString):
    """Custom type nmsifthThresholdDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NmsifthThresholdDescr_Type.__name__ = "SnmpAdminString"
_NmsifthThresholdDescr_Object = MibTableColumn
nmsifthThresholdDescr = _NmsifthThresholdDescr_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 1, 5, 1, 2),
    _NmsifthThresholdDescr_Type()
)
nmsifthThresholdDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nmsifthThresholdDescr.setStatus("current")
_NmsifthThresholdObject_Type = ObjectIdentifier
_NmsifthThresholdObject_Object = MibTableColumn
nmsifthThresholdObject = _NmsifthThresholdObject_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 1, 5, 1, 3),
    _NmsifthThresholdObject_Type()
)
nmsifthThresholdObject.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nmsifthThresholdObject.setStatus("current")
_NmsifthThresholdSeverity_Type = NMSifthThresholdSeverity
_NmsifthThresholdSeverity_Object = MibTableColumn
nmsifthThresholdSeverity = _NmsifthThresholdSeverity_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 1, 5, 1, 4),
    _NmsifthThresholdSeverity_Type()
)
nmsifthThresholdSeverity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nmsifthThresholdSeverity.setStatus("current")


class _NmsifthThresholdType_Type(Integer32):
    """Custom type nmsifthThresholdType based on Integer32"""
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


_NmsifthThresholdType_Type.__name__ = "Integer32"
_NmsifthThresholdType_Object = MibTableColumn
nmsifthThresholdType = _NmsifthThresholdType_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 1, 5, 1, 5),
    _NmsifthThresholdType_Type()
)
nmsifthThresholdType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nmsifthThresholdType.setStatus("current")


class _NmsifthThresholdDirection_Type(Integer32):
    """Custom type nmsifthThresholdDirection based on Integer32"""
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


_NmsifthThresholdDirection_Type.__name__ = "Integer32"
_NmsifthThresholdDirection_Object = MibTableColumn
nmsifthThresholdDirection = _NmsifthThresholdDirection_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 1, 5, 1, 6),
    _NmsifthThresholdDirection_Type()
)
nmsifthThresholdDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nmsifthThresholdDirection.setStatus("current")


class _NmsifthThresholdFiredValue_Type(Integer32):
    """Custom type nmsifthThresholdFiredValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NmsifthThresholdFiredValue_Type.__name__ = "Integer32"
_NmsifthThresholdFiredValue_Object = MibTableColumn
nmsifthThresholdFiredValue = _NmsifthThresholdFiredValue_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 1, 5, 1, 7),
    _NmsifthThresholdFiredValue_Type()
)
nmsifthThresholdFiredValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nmsifthThresholdFiredValue.setStatus("current")


class _NmsifthThresholdClearedValue_Type(Integer32):
    """Custom type nmsifthThresholdClearedValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NmsifthThresholdClearedValue_Type.__name__ = "Integer32"
_NmsifthThresholdClearedValue_Object = MibTableColumn
nmsifthThresholdClearedValue = _NmsifthThresholdClearedValue_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 1, 5, 1, 8),
    _NmsifthThresholdClearedValue_Type()
)
nmsifthThresholdClearedValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nmsifthThresholdClearedValue.setStatus("current")


class _NmsifthThresholdSampleInterval_Type(Unsigned32):
    """Custom type nmsifthThresholdSampleInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 900000),
    )


_NmsifthThresholdSampleInterval_Type.__name__ = "Unsigned32"
_NmsifthThresholdSampleInterval_Object = MibTableColumn
nmsifthThresholdSampleInterval = _NmsifthThresholdSampleInterval_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 1, 5, 1, 9),
    _NmsifthThresholdSampleInterval_Type()
)
nmsifthThresholdSampleInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nmsifthThresholdSampleInterval.setStatus("current")
if mibBuilder.loadTexts:
    nmsifthThresholdSampleInterval.setUnits("milliseconds")


class _NmsifthThresholdApsSwitchover_Type(TruthValue):
    """Custom type nmsifthThresholdApsSwitchover based on TruthValue"""


_NmsifthThresholdApsSwitchover_Object = MibTableColumn
nmsifthThresholdApsSwitchover = _NmsifthThresholdApsSwitchover_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 1, 5, 1, 10),
    _NmsifthThresholdApsSwitchover_Type()
)
nmsifthThresholdApsSwitchover.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nmsifthThresholdApsSwitchover.setStatus("current")
_NmsifthThresholdRowStatus_Type = RowStatus
_NmsifthThresholdRowStatus_Object = MibTableColumn
nmsifthThresholdRowStatus = _NmsifthThresholdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 1, 5, 1, 11),
    _NmsifthThresholdRowStatus_Type()
)
nmsifthThresholdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nmsifthThresholdRowStatus.setStatus("current")
_NmsifthTemplateIfAssignGroup_ObjectIdentity = ObjectIdentity
nmsifthTemplateIfAssignGroup = _NmsifthTemplateIfAssignGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 2)
)
_NmsifthTemplateIfLastChange_Type = TimeStamp
_NmsifthTemplateIfLastChange_Object = MibScalar
nmsifthTemplateIfLastChange = _NmsifthTemplateIfLastChange_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 2, 1),
    _NmsifthTemplateIfLastChange_Type()
)
nmsifthTemplateIfLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsifthTemplateIfLastChange.setStatus("current")
_NmsifthTemplateIfAssignTable_Object = MibTable
nmsifthTemplateIfAssignTable = _NmsifthTemplateIfAssignTable_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 2, 2)
)
if mibBuilder.loadTexts:
    nmsifthTemplateIfAssignTable.setStatus("current")
_NmsifthTemplateIfAssignEntry_Object = MibTableRow
nmsifthTemplateIfAssignEntry = _NmsifthTemplateIfAssignEntry_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 2, 2, 1)
)
nmsifthTemplateIfAssignEntry.setIndexNames(
    (0, "NMS-IF-THRESHOLD-MIB", "nmsifthTemplateIndex"),
    (0, "NMS-IF-THRESHOLD-MIB", "nmsifthTemplateIfAssignInterface"),
)
if mibBuilder.loadTexts:
    nmsifthTemplateIfAssignEntry.setStatus("current")
_NmsifthTemplateIfAssignInterface_Type = InterfaceIndex
_NmsifthTemplateIfAssignInterface_Object = MibTableColumn
nmsifthTemplateIfAssignInterface = _NmsifthTemplateIfAssignInterface_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 2, 2, 1, 1),
    _NmsifthTemplateIfAssignInterface_Type()
)
nmsifthTemplateIfAssignInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nmsifthTemplateIfAssignInterface.setStatus("current")


class _NmsifthTemplateIfAssignOperStatus_Type(Integer32):
    """Custom type nmsifthTemplateIfAssignOperStatus based on Integer32"""
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


_NmsifthTemplateIfAssignOperStatus_Type.__name__ = "Integer32"
_NmsifthTemplateIfAssignOperStatus_Object = MibTableColumn
nmsifthTemplateIfAssignOperStatus = _NmsifthTemplateIfAssignOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 2, 2, 1, 2),
    _NmsifthTemplateIfAssignOperStatus_Type()
)
nmsifthTemplateIfAssignOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsifthTemplateIfAssignOperStatus.setStatus("current")
_NmsifthTemplateIfAssignRowStatus_Type = RowStatus
_NmsifthTemplateIfAssignRowStatus_Object = MibTableColumn
nmsifthTemplateIfAssignRowStatus = _NmsifthTemplateIfAssignRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 2, 2, 1, 3),
    _NmsifthTemplateIfAssignRowStatus_Type()
)
nmsifthTemplateIfAssignRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nmsifthTemplateIfAssignRowStatus.setStatus("current")
_NmsifthIfThresholdFiredGroup_ObjectIdentity = ObjectIdentity
nmsifthIfThresholdFiredGroup = _NmsifthIfThresholdFiredGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 3)
)
_NmsifthThresholdFiredNotifyEnable_Type = NMSifthThresholdSeverityOrZero
_NmsifthThresholdFiredNotifyEnable_Object = MibScalar
nmsifthThresholdFiredNotifyEnable = _NmsifthThresholdFiredNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 3, 1),
    _NmsifthThresholdFiredNotifyEnable_Type()
)
nmsifthThresholdFiredNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsifthThresholdFiredNotifyEnable.setStatus("current")
_NmsifthThresholdFiredLastChange_Type = TimeStamp
_NmsifthThresholdFiredLastChange_Object = MibScalar
nmsifthThresholdFiredLastChange = _NmsifthThresholdFiredLastChange_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 3, 2),
    _NmsifthThresholdFiredLastChange_Type()
)
nmsifthThresholdFiredLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsifthThresholdFiredLastChange.setStatus("current")
_NmsifthIfThresholdFiredTable_Object = MibTable
nmsifthIfThresholdFiredTable = _NmsifthIfThresholdFiredTable_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 3, 3)
)
if mibBuilder.loadTexts:
    nmsifthIfThresholdFiredTable.setStatus("current")
_NmsifthIfThresholdFiredEntry_Object = MibTableRow
nmsifthIfThresholdFiredEntry = _NmsifthIfThresholdFiredEntry_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 3, 3, 1)
)
nmsifthIfThresholdFiredEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "NMS-IF-THRESHOLD-MIB", "nmsifthIfThresholdFiredTemplate"),
)
if mibBuilder.loadTexts:
    nmsifthIfThresholdFiredEntry.setStatus("current")
_NmsifthIfThresholdFiredTemplate_Type = NMSifthTemplateIndex
_NmsifthIfThresholdFiredTemplate_Object = MibTableColumn
nmsifthIfThresholdFiredTemplate = _NmsifthIfThresholdFiredTemplate_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 3, 3, 1, 1),
    _NmsifthIfThresholdFiredTemplate_Type()
)
nmsifthIfThresholdFiredTemplate.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nmsifthIfThresholdFiredTemplate.setStatus("current")
_NmsifthIfThresholdsFired_Type = NMSifthThresholdList
_NmsifthIfThresholdsFired_Object = MibTableColumn
nmsifthIfThresholdsFired = _NmsifthIfThresholdsFired_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 3, 3, 1, 2),
    _NmsifthIfThresholdsFired_Type()
)
nmsifthIfThresholdsFired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsifthIfThresholdsFired.setStatus("current")
_NmsifthIfLastThresholdFired_Type = NMSifthThresholdIndex
_NmsifthIfLastThresholdFired_Object = MibTableColumn
nmsifthIfLastThresholdFired = _NmsifthIfLastThresholdFired_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 3, 3, 1, 3),
    _NmsifthIfLastThresholdFired_Type()
)
nmsifthIfLastThresholdFired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsifthIfLastThresholdFired.setStatus("current")
_NmsifthIfThresholdFiredLstChange_Type = TimeStamp
_NmsifthIfThresholdFiredLstChange_Object = MibTableColumn
nmsifthIfThresholdFiredLstChange = _NmsifthIfThresholdFiredLstChange_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 3, 3, 1, 4),
    _NmsifthIfThresholdFiredLstChange_Type()
)
nmsifthIfThresholdFiredLstChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsifthIfThresholdFiredLstChange.setStatus("current")
_NmsifthIfThresholdFiredLstSeverity_Type = NMSifthThresholdSeverity
_NmsifthIfThresholdFiredLstSeverity_Object = MibTableColumn
nmsifthIfThresholdFiredLstSeverity = _NmsifthIfThresholdFiredLstSeverity_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 3, 3, 1, 5),
    _NmsifthIfThresholdFiredLstSeverity_Type()
)
nmsifthIfThresholdFiredLstSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsifthIfThresholdFiredLstSeverity.setStatus("current")
_NmsifthIfThresholdFiredMaxSeverity_Type = NMSifthThresholdSeverity
_NmsifthIfThresholdFiredMaxSeverity_Object = MibTableColumn
nmsifthIfThresholdFiredMaxSeverity = _NmsifthIfThresholdFiredMaxSeverity_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 1, 3, 3, 1, 6),
    _NmsifthIfThresholdFiredMaxSeverity_Type()
)
nmsifthIfThresholdFiredMaxSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsifthIfThresholdFiredMaxSeverity.setStatus("current")
_NmsIfThresholdMIBNotifications_ObjectIdentity = ObjectIdentity
nmsIfThresholdMIBNotifications = _NmsIfThresholdMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 2)
)
_NmsifthMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
nmsifthMIBNotificationsPrefix = _NmsifthMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 2, 0)
)
_NmsIfThresholdMIBConformance_ObjectIdentity = ObjectIdentity
nmsIfThresholdMIBConformance = _NmsIfThresholdMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 3)
)
_NmsIfThresholdMIBCompliances_ObjectIdentity = ObjectIdentity
nmsIfThresholdMIBCompliances = _NmsIfThresholdMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 3, 1)
)
_NmsIfThresholdMIBGroups_ObjectIdentity = ObjectIdentity
nmsIfThresholdMIBGroups = _NmsIfThresholdMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 3, 2)
)

# Managed Objects groups

nmsIfThresholdTemplateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 3, 2, 1)
)
nmsIfThresholdTemplateGroup.setObjects(
      *(("NMS-IF-THRESHOLD-MIB", "nmsifthTemplateIndexNext"),
        ("NMS-IF-THRESHOLD-MIB", "nmsifthTemplateLastChange"),
        ("NMS-IF-THRESHOLD-MIB", "nmsifthTemplateName"),
        ("NMS-IF-THRESHOLD-MIB", "nmsifthTemplateNotifyHoldDownType"),
        ("NMS-IF-THRESHOLD-MIB", "nmsifthTemplateRowStatus"),
        ("NMS-IF-THRESHOLD-MIB", "nmsifthThresholdLastChange"),
        ("NMS-IF-THRESHOLD-MIB", "nmsifthThresholdDescr"),
        ("NMS-IF-THRESHOLD-MIB", "nmsifthThresholdObject"),
        ("NMS-IF-THRESHOLD-MIB", "nmsifthThresholdSeverity"),
        ("NMS-IF-THRESHOLD-MIB", "nmsifthThresholdType"),
        ("NMS-IF-THRESHOLD-MIB", "nmsifthThresholdDirection"),
        ("NMS-IF-THRESHOLD-MIB", "nmsifthThresholdFiredValue"),
        ("NMS-IF-THRESHOLD-MIB", "nmsifthThresholdSampleInterval"),
        ("NMS-IF-THRESHOLD-MIB", "nmsifthThresholdRowStatus"),
        ("NMS-IF-THRESHOLD-MIB", "nmsifthTemplateIfLastChange"),
        ("NMS-IF-THRESHOLD-MIB", "nmsifthTemplateIfAssignOperStatus"),
        ("NMS-IF-THRESHOLD-MIB", "nmsifthTemplateIfAssignRowStatus"))
)
if mibBuilder.loadTexts:
    nmsIfThresholdTemplateGroup.setStatus("current")

nmsIfThresholdFiredGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 3, 2, 2)
)
nmsIfThresholdFiredGroup.setObjects(
      *(("NMS-IF-THRESHOLD-MIB", "nmsifthThresholdFiredNotifyEnable"),
        ("NMS-IF-THRESHOLD-MIB", "nmsifthThresholdFiredLastChange"),
        ("NMS-IF-THRESHOLD-MIB", "nmsifthIfThresholdsFired"),
        ("NMS-IF-THRESHOLD-MIB", "nmsifthIfLastThresholdFired"),
        ("NMS-IF-THRESHOLD-MIB", "nmsifthIfThresholdFiredLstChange"),
        ("NMS-IF-THRESHOLD-MIB", "nmsifthIfThresholdFiredLstSeverity"),
        ("NMS-IF-THRESHOLD-MIB", "nmsifthIfThresholdFiredMaxSeverity"))
)
if mibBuilder.loadTexts:
    nmsIfThresholdFiredGroup.setStatus("current")

nmsifthHoldDownTimerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 3, 2, 3)
)
nmsifthHoldDownTimerGroup.setObjects(
    ("NMS-IF-THRESHOLD-MIB", "nmsifthTemplateNotifyHoldDownTime")
)
if mibBuilder.loadTexts:
    nmsifthHoldDownTimerGroup.setStatus("current")

nmsifthHoldDownHysteresisGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 3, 2, 4)
)
nmsifthHoldDownHysteresisGroup.setObjects(
    ("NMS-IF-THRESHOLD-MIB", "nmsifthThresholdClearedValue")
)
if mibBuilder.loadTexts:
    nmsifthHoldDownHysteresisGroup.setStatus("current")

nmsifthApsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 3, 2, 5)
)
nmsifthApsGroup.setObjects(
    ("NMS-IF-THRESHOLD-MIB", "nmsifthThresholdApsSwitchover")
)
if mibBuilder.loadTexts:
    nmsifthApsGroup.setStatus("current")


# Notification objects

nmsifthIfThresholdFired = NotificationType(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 2, 0, 1)
)
nmsifthIfThresholdFired.setObjects(
      *(("NMS-IF-THRESHOLD-MIB", "nmsifthIfLastThresholdFired"),
        ("NMS-IF-THRESHOLD-MIB", "nmsifthIfThresholdFiredLstChange"),
        ("NMS-IF-THRESHOLD-MIB", "nmsifthIfThresholdFiredLstSeverity"))
)
if mibBuilder.loadTexts:
    nmsifthIfThresholdFired.setStatus(
        "current"
    )

nmsifthIfThresholdCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 2, 0, 2)
)
nmsifthIfThresholdCleared.setObjects(
      *(("NMS-IF-THRESHOLD-MIB", "nmsifthIfLastThresholdFired"),
        ("NMS-IF-THRESHOLD-MIB", "nmsifthIfThresholdFiredLstChange"),
        ("NMS-IF-THRESHOLD-MIB", "nmsifthIfThresholdFiredLstSeverity"))
)
if mibBuilder.loadTexts:
    nmsifthIfThresholdCleared.setStatus(
        "current"
    )

nmsifthTemplateIfStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 2, 0, 3)
)
nmsifthTemplateIfStatusChange.setObjects(
    ("NMS-IF-THRESHOLD-MIB", "nmsifthTemplateIfAssignOperStatus")
)
if mibBuilder.loadTexts:
    nmsifthTemplateIfStatusChange.setStatus(
        "current"
    )


# Notifications groups

nmsIfThresholdNotifsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 3, 2, 6)
)
nmsIfThresholdNotifsGroup.setObjects(
      *(("NMS-IF-THRESHOLD-MIB", "nmsifthIfThresholdFired"),
        ("NMS-IF-THRESHOLD-MIB", "nmsifthIfThresholdCleared"))
)
if mibBuilder.loadTexts:
    nmsIfThresholdNotifsGroup.setStatus(
        "current"
    )

nmsifthTemplateIfNotifsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 3, 2, 7)
)
nmsifthTemplateIfNotifsGroup.setObjects(
    ("NMS-IF-THRESHOLD-MIB", "nmsifthTemplateIfStatusChange")
)
if mibBuilder.loadTexts:
    nmsifthTemplateIfNotifsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

nmsIfThresholdMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 218, 3, 1, 1)
)
if mibBuilder.loadTexts:
    nmsIfThresholdMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NMS-IF-THRESHOLD-MIB",
    **{"NMSifthTemplateIndex": NMSifthTemplateIndex,
       "NMSifthTemplateIndexOrZero": NMSifthTemplateIndexOrZero,
       "NMSifthThresholdIndex": NMSifthThresholdIndex,
       "NMSifthThresholdList": NMSifthThresholdList,
       "NMSifthThresholdSeverity": NMSifthThresholdSeverity,
       "NMSifthThresholdSeverityOrZero": NMSifthThresholdSeverityOrZero,
       "nmsIfThresholdMIB": nmsIfThresholdMIB,
       "nmsIfThresholdMIBObjects": nmsIfThresholdMIBObjects,
       "nmsifthTemplateGroup": nmsifthTemplateGroup,
       "nmsifthTemplateIndexNext": nmsifthTemplateIndexNext,
       "nmsifthTemplateLastChange": nmsifthTemplateLastChange,
       "nmsifthTemplateTable": nmsifthTemplateTable,
       "nmsifthTemplateEntry": nmsifthTemplateEntry,
       "nmsifthTemplateIndex": nmsifthTemplateIndex,
       "nmsifthTemplateName": nmsifthTemplateName,
       "nmsifthTemplateNotifyHoldDownType": nmsifthTemplateNotifyHoldDownType,
       "nmsifthTemplateNotifyHoldDownTime": nmsifthTemplateNotifyHoldDownTime,
       "nmsifthTemplateRowStatus": nmsifthTemplateRowStatus,
       "nmsifthThresholdLastChange": nmsifthThresholdLastChange,
       "nmsifthThresholdTable": nmsifthThresholdTable,
       "nmsifthThresholdEntry": nmsifthThresholdEntry,
       "nmsifthThresholdIndex": nmsifthThresholdIndex,
       "nmsifthThresholdDescr": nmsifthThresholdDescr,
       "nmsifthThresholdObject": nmsifthThresholdObject,
       "nmsifthThresholdSeverity": nmsifthThresholdSeverity,
       "nmsifthThresholdType": nmsifthThresholdType,
       "nmsifthThresholdDirection": nmsifthThresholdDirection,
       "nmsifthThresholdFiredValue": nmsifthThresholdFiredValue,
       "nmsifthThresholdClearedValue": nmsifthThresholdClearedValue,
       "nmsifthThresholdSampleInterval": nmsifthThresholdSampleInterval,
       "nmsifthThresholdApsSwitchover": nmsifthThresholdApsSwitchover,
       "nmsifthThresholdRowStatus": nmsifthThresholdRowStatus,
       "nmsifthTemplateIfAssignGroup": nmsifthTemplateIfAssignGroup,
       "nmsifthTemplateIfLastChange": nmsifthTemplateIfLastChange,
       "nmsifthTemplateIfAssignTable": nmsifthTemplateIfAssignTable,
       "nmsifthTemplateIfAssignEntry": nmsifthTemplateIfAssignEntry,
       "nmsifthTemplateIfAssignInterface": nmsifthTemplateIfAssignInterface,
       "nmsifthTemplateIfAssignOperStatus": nmsifthTemplateIfAssignOperStatus,
       "nmsifthTemplateIfAssignRowStatus": nmsifthTemplateIfAssignRowStatus,
       "nmsifthIfThresholdFiredGroup": nmsifthIfThresholdFiredGroup,
       "nmsifthThresholdFiredNotifyEnable": nmsifthThresholdFiredNotifyEnable,
       "nmsifthThresholdFiredLastChange": nmsifthThresholdFiredLastChange,
       "nmsifthIfThresholdFiredTable": nmsifthIfThresholdFiredTable,
       "nmsifthIfThresholdFiredEntry": nmsifthIfThresholdFiredEntry,
       "nmsifthIfThresholdFiredTemplate": nmsifthIfThresholdFiredTemplate,
       "nmsifthIfThresholdsFired": nmsifthIfThresholdsFired,
       "nmsifthIfLastThresholdFired": nmsifthIfLastThresholdFired,
       "nmsifthIfThresholdFiredLstChange": nmsifthIfThresholdFiredLstChange,
       "nmsifthIfThresholdFiredLstSeverity": nmsifthIfThresholdFiredLstSeverity,
       "nmsifthIfThresholdFiredMaxSeverity": nmsifthIfThresholdFiredMaxSeverity,
       "nmsIfThresholdMIBNotifications": nmsIfThresholdMIBNotifications,
       "nmsifthMIBNotificationsPrefix": nmsifthMIBNotificationsPrefix,
       "nmsifthIfThresholdFired": nmsifthIfThresholdFired,
       "nmsifthIfThresholdCleared": nmsifthIfThresholdCleared,
       "nmsifthTemplateIfStatusChange": nmsifthTemplateIfStatusChange,
       "nmsIfThresholdMIBConformance": nmsIfThresholdMIBConformance,
       "nmsIfThresholdMIBCompliances": nmsIfThresholdMIBCompliances,
       "nmsIfThresholdMIBCompliance": nmsIfThresholdMIBCompliance,
       "nmsIfThresholdMIBGroups": nmsIfThresholdMIBGroups,
       "nmsIfThresholdTemplateGroup": nmsIfThresholdTemplateGroup,
       "nmsIfThresholdFiredGroup": nmsIfThresholdFiredGroup,
       "nmsifthHoldDownTimerGroup": nmsifthHoldDownTimerGroup,
       "nmsifthHoldDownHysteresisGroup": nmsifthHoldDownHysteresisGroup,
       "nmsifthApsGroup": nmsifthApsGroup,
       "nmsIfThresholdNotifsGroup": nmsIfThresholdNotifsGroup,
       "nmsifthTemplateIfNotifsGroup": nmsifthTemplateIfNotifsGroup}
)
