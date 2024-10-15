# SNMP MIB module (WWP-LEOS-FLOW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-LEOS-FLOW-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:53 2024
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

(wwpModulesLeos,) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModulesLeos")


# MODULE-IDENTITY

wwpLeosFlowMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6)
)
wwpLeosFlowMIB.setRevisions(
        ("2012-03-29 00:00",
         "2011-02-02 00:00",
         "2008-06-16 17:00",
         "2001-04-03 17:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PriorityMapping(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



# MIB Managed Objects in the order of their OIDs

_WwpLeosFlowMIBObjects_ObjectIdentity = ObjectIdentity
wwpLeosFlowMIBObjects = _WwpLeosFlowMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1)
)
_WwpLeosFlow_ObjectIdentity = ObjectIdentity
wwpLeosFlow = _WwpLeosFlow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1)
)


class _WwpLeosFlowAgeTime_Type(Integer32):
    """Custom type wwpLeosFlowAgeTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_WwpLeosFlowAgeTime_Type.__name__ = "Integer32"
_WwpLeosFlowAgeTime_Object = MibScalar
wwpLeosFlowAgeTime = _WwpLeosFlowAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 1),
    _WwpLeosFlowAgeTime_Type()
)
wwpLeosFlowAgeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowAgeTime.setStatus("current")


class _WwpLeosFlowAgeTimeState_Type(Integer32):
    """Custom type wwpLeosFlowAgeTimeState based on Integer32"""
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


_WwpLeosFlowAgeTimeState_Type.__name__ = "Integer32"
_WwpLeosFlowAgeTimeState_Object = MibScalar
wwpLeosFlowAgeTimeState = _WwpLeosFlowAgeTimeState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 2),
    _WwpLeosFlowAgeTimeState_Type()
)
wwpLeosFlowAgeTimeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowAgeTimeState.setStatus("current")
_WwpLeosFlowServiceLevelTable_Object = MibTable
wwpLeosFlowServiceLevelTable = _WwpLeosFlowServiceLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 3)
)
if mibBuilder.loadTexts:
    wwpLeosFlowServiceLevelTable.setStatus("current")
_WwpLeosFlowServiceLevelEntry_Object = MibTableRow
wwpLeosFlowServiceLevelEntry = _WwpLeosFlowServiceLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 3, 1)
)
wwpLeosFlowServiceLevelEntry.setIndexNames(
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowServiceLevelPort"),
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowServiceLevelId"),
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowServiceLevelDirection"),
)
if mibBuilder.loadTexts:
    wwpLeosFlowServiceLevelEntry.setStatus("current")


class _WwpLeosFlowServiceLevelDirection_Type(Integer32):
    """Custom type wwpLeosFlowServiceLevelDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("egress", 2),
          ("ingress", 1))
    )


_WwpLeosFlowServiceLevelDirection_Type.__name__ = "Integer32"
_WwpLeosFlowServiceLevelDirection_Object = MibTableColumn
wwpLeosFlowServiceLevelDirection = _WwpLeosFlowServiceLevelDirection_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 3, 1, 1),
    _WwpLeosFlowServiceLevelDirection_Type()
)
wwpLeosFlowServiceLevelDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowServiceLevelDirection.setStatus("current")


class _WwpLeosFlowServiceLevelPort_Type(Integer32):
    """Custom type wwpLeosFlowServiceLevelPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLeosFlowServiceLevelPort_Type.__name__ = "Integer32"
_WwpLeosFlowServiceLevelPort_Object = MibTableColumn
wwpLeosFlowServiceLevelPort = _WwpLeosFlowServiceLevelPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 3, 1, 2),
    _WwpLeosFlowServiceLevelPort_Type()
)
wwpLeosFlowServiceLevelPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowServiceLevelPort.setStatus("current")


class _WwpLeosFlowServiceLevelId_Type(Integer32):
    """Custom type wwpLeosFlowServiceLevelId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosFlowServiceLevelId_Type.__name__ = "Integer32"
_WwpLeosFlowServiceLevelId_Object = MibTableColumn
wwpLeosFlowServiceLevelId = _WwpLeosFlowServiceLevelId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 3, 1, 3),
    _WwpLeosFlowServiceLevelId_Type()
)
wwpLeosFlowServiceLevelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowServiceLevelId.setStatus("current")
_WwpLeosFlowServiceLevelName_Type = DisplayString
_WwpLeosFlowServiceLevelName_Object = MibTableColumn
wwpLeosFlowServiceLevelName = _WwpLeosFlowServiceLevelName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 3, 1, 4),
    _WwpLeosFlowServiceLevelName_Type()
)
wwpLeosFlowServiceLevelName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosFlowServiceLevelName.setStatus("current")


class _WwpLeosFlowServiceLevelPriority_Type(Integer32):
    """Custom type wwpLeosFlowServiceLevelPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosFlowServiceLevelPriority_Type.__name__ = "Integer32"
_WwpLeosFlowServiceLevelPriority_Object = MibTableColumn
wwpLeosFlowServiceLevelPriority = _WwpLeosFlowServiceLevelPriority_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 3, 1, 5),
    _WwpLeosFlowServiceLevelPriority_Type()
)
wwpLeosFlowServiceLevelPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosFlowServiceLevelPriority.setStatus("current")


class _WwpLeosFlowServiceLevelQueueSize_Type(Integer32):
    """Custom type wwpLeosFlowServiceLevelQueueSize based on Integer32"""
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
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("jumbo", 4),
          ("large", 3),
          ("medium", 2),
          ("size0KB", 0),
          ("size128KB", 12),
          ("size16KB", 9),
          ("size1MB", 15),
          ("size256KB", 13),
          ("size2MB", 16),
          ("size32KB", 10),
          ("size4MB", 17),
          ("size512KB", 14),
          ("size64KB", 11),
          ("small", 1),
          ("x5", 5),
          ("x6", 6),
          ("x7", 7),
          ("x8", 8))
    )


_WwpLeosFlowServiceLevelQueueSize_Type.__name__ = "Integer32"
_WwpLeosFlowServiceLevelQueueSize_Object = MibTableColumn
wwpLeosFlowServiceLevelQueueSize = _WwpLeosFlowServiceLevelQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 3, 1, 6),
    _WwpLeosFlowServiceLevelQueueSize_Type()
)
wwpLeosFlowServiceLevelQueueSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosFlowServiceLevelQueueSize.setStatus("current")


class _WwpLeosFlowServiceLevelDropEligibility_Type(Integer32):
    """Custom type wwpLeosFlowServiceLevelDropEligibility based on Integer32"""
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


_WwpLeosFlowServiceLevelDropEligibility_Type.__name__ = "Integer32"
_WwpLeosFlowServiceLevelDropEligibility_Object = MibTableColumn
wwpLeosFlowServiceLevelDropEligibility = _WwpLeosFlowServiceLevelDropEligibility_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 3, 1, 7),
    _WwpLeosFlowServiceLevelDropEligibility_Type()
)
wwpLeosFlowServiceLevelDropEligibility.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosFlowServiceLevelDropEligibility.setStatus("current")


class _WwpLeosFlowServiceLevelShareEligibility_Type(Integer32):
    """Custom type wwpLeosFlowServiceLevelShareEligibility based on Integer32"""
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


_WwpLeosFlowServiceLevelShareEligibility_Type.__name__ = "Integer32"
_WwpLeosFlowServiceLevelShareEligibility_Object = MibTableColumn
wwpLeosFlowServiceLevelShareEligibility = _WwpLeosFlowServiceLevelShareEligibility_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 3, 1, 8),
    _WwpLeosFlowServiceLevelShareEligibility_Type()
)
wwpLeosFlowServiceLevelShareEligibility.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosFlowServiceLevelShareEligibility.setStatus("current")


class _WwpLeosFlowServiceLevelCirBW_Type(Integer32):
    """Custom type wwpLeosFlowServiceLevelCirBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WwpLeosFlowServiceLevelCirBW_Type.__name__ = "Integer32"
_WwpLeosFlowServiceLevelCirBW_Object = MibTableColumn
wwpLeosFlowServiceLevelCirBW = _WwpLeosFlowServiceLevelCirBW_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 3, 1, 9),
    _WwpLeosFlowServiceLevelCirBW_Type()
)
wwpLeosFlowServiceLevelCirBW.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosFlowServiceLevelCirBW.setStatus("current")


class _WwpLeosFlowServiceLevelPirBW_Type(Integer32):
    """Custom type wwpLeosFlowServiceLevelPirBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WwpLeosFlowServiceLevelPirBW_Type.__name__ = "Integer32"
_WwpLeosFlowServiceLevelPirBW_Object = MibTableColumn
wwpLeosFlowServiceLevelPirBW = _WwpLeosFlowServiceLevelPirBW_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 3, 1, 10),
    _WwpLeosFlowServiceLevelPirBW_Type()
)
wwpLeosFlowServiceLevelPirBW.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosFlowServiceLevelPirBW.setStatus("current")
_WwpLeosFlowServiceStatus_Type = RowStatus
_WwpLeosFlowServiceStatus_Object = MibTableColumn
wwpLeosFlowServiceStatus = _WwpLeosFlowServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 3, 1, 11),
    _WwpLeosFlowServiceStatus_Type()
)
wwpLeosFlowServiceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosFlowServiceStatus.setStatus("current")


class _WwpLeosFlowServiceRedCurveId_Type(Unsigned32):
    """Custom type wwpLeosFlowServiceRedCurveId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 64),
    )


_WwpLeosFlowServiceRedCurveId_Type.__name__ = "Unsigned32"
_WwpLeosFlowServiceRedCurveId_Object = MibTableColumn
wwpLeosFlowServiceRedCurveId = _WwpLeosFlowServiceRedCurveId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 3, 1, 12),
    _WwpLeosFlowServiceRedCurveId_Type()
)
wwpLeosFlowServiceRedCurveId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosFlowServiceRedCurveId.setStatus("current")


class _WwpLeosFlowServiceLevelQueueSizeYellow_Type(Integer32):
    """Custom type wwpLeosFlowServiceLevelQueueSizeYellow based on Integer32"""
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
        *(("size128KB", 4),
          ("size16KB", 1),
          ("size32KB", 2),
          ("size64KB", 3))
    )


_WwpLeosFlowServiceLevelQueueSizeYellow_Type.__name__ = "Integer32"
_WwpLeosFlowServiceLevelQueueSizeYellow_Object = MibTableColumn
wwpLeosFlowServiceLevelQueueSizeYellow = _WwpLeosFlowServiceLevelQueueSizeYellow_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 3, 1, 13),
    _WwpLeosFlowServiceLevelQueueSizeYellow_Type()
)
wwpLeosFlowServiceLevelQueueSizeYellow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosFlowServiceLevelQueueSizeYellow.setStatus("current")


class _WwpLeosFlowServiceLevelQueueSizeRed_Type(Integer32):
    """Custom type wwpLeosFlowServiceLevelQueueSizeRed based on Integer32"""
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
        *(("size128KB", 4),
          ("size16KB", 1),
          ("size32KB", 2),
          ("size64KB", 3))
    )


_WwpLeosFlowServiceLevelQueueSizeRed_Type.__name__ = "Integer32"
_WwpLeosFlowServiceLevelQueueSizeRed_Object = MibTableColumn
wwpLeosFlowServiceLevelQueueSizeRed = _WwpLeosFlowServiceLevelQueueSizeRed_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 3, 1, 14),
    _WwpLeosFlowServiceLevelQueueSizeRed_Type()
)
wwpLeosFlowServiceLevelQueueSizeRed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosFlowServiceLevelQueueSizeRed.setStatus("current")


class _WwpLeosFlowServiceLevelFlowGroup_Type(Integer32):
    """Custom type wwpLeosFlowServiceLevelFlowGroup based on Integer32"""
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


_WwpLeosFlowServiceLevelFlowGroup_Type.__name__ = "Integer32"
_WwpLeosFlowServiceLevelFlowGroup_Object = MibTableColumn
wwpLeosFlowServiceLevelFlowGroup = _WwpLeosFlowServiceLevelFlowGroup_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 3, 1, 15),
    _WwpLeosFlowServiceLevelFlowGroup_Type()
)
wwpLeosFlowServiceLevelFlowGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosFlowServiceLevelFlowGroup.setStatus("current")
_WwpLeosFlowServiceMappingTable_Object = MibTable
wwpLeosFlowServiceMappingTable = _WwpLeosFlowServiceMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 4)
)
if mibBuilder.loadTexts:
    wwpLeosFlowServiceMappingTable.setStatus("deprecated")
_WwpLeosFlowServiceMappingEntry_Object = MibTableRow
wwpLeosFlowServiceMappingEntry = _WwpLeosFlowServiceMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 4, 1)
)
wwpLeosFlowServiceMappingEntry.setIndexNames(
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowServiceMapVid"),
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowServiceMapSrcPort"),
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowServiceMapSrcTag"),
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowServiceMapDstPort"),
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowServiceMapDstTag"),
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowServiceMapSrcPri"),
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowServiceMapProtocolType"),
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowServiceMapProtocolPortNum"),
)
if mibBuilder.loadTexts:
    wwpLeosFlowServiceMappingEntry.setStatus("deprecated")


class _WwpLeosFlowServiceMapVid_Type(Integer32):
    """Custom type wwpLeosFlowServiceMapVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24576),
    )


_WwpLeosFlowServiceMapVid_Type.__name__ = "Integer32"
_WwpLeosFlowServiceMapVid_Object = MibTableColumn
wwpLeosFlowServiceMapVid = _WwpLeosFlowServiceMapVid_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 4, 1, 1),
    _WwpLeosFlowServiceMapVid_Type()
)
wwpLeosFlowServiceMapVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowServiceMapVid.setStatus("deprecated")


class _WwpLeosFlowServiceMapSrcPort_Type(Integer32):
    """Custom type wwpLeosFlowServiceMapSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLeosFlowServiceMapSrcPort_Type.__name__ = "Integer32"
_WwpLeosFlowServiceMapSrcPort_Object = MibTableColumn
wwpLeosFlowServiceMapSrcPort = _WwpLeosFlowServiceMapSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 4, 1, 2),
    _WwpLeosFlowServiceMapSrcPort_Type()
)
wwpLeosFlowServiceMapSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowServiceMapSrcPort.setStatus("deprecated")


class _WwpLeosFlowServiceMapSrcTag_Type(Integer32):
    """Custom type wwpLeosFlowServiceMapSrcTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_WwpLeosFlowServiceMapSrcTag_Type.__name__ = "Integer32"
_WwpLeosFlowServiceMapSrcTag_Object = MibTableColumn
wwpLeosFlowServiceMapSrcTag = _WwpLeosFlowServiceMapSrcTag_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 4, 1, 3),
    _WwpLeosFlowServiceMapSrcTag_Type()
)
wwpLeosFlowServiceMapSrcTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowServiceMapSrcTag.setStatus("deprecated")


class _WwpLeosFlowServiceMapDstPort_Type(Integer32):
    """Custom type wwpLeosFlowServiceMapDstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLeosFlowServiceMapDstPort_Type.__name__ = "Integer32"
_WwpLeosFlowServiceMapDstPort_Object = MibTableColumn
wwpLeosFlowServiceMapDstPort = _WwpLeosFlowServiceMapDstPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 4, 1, 4),
    _WwpLeosFlowServiceMapDstPort_Type()
)
wwpLeosFlowServiceMapDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowServiceMapDstPort.setStatus("deprecated")


class _WwpLeosFlowServiceMapDstTag_Type(Integer32):
    """Custom type wwpLeosFlowServiceMapDstTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_WwpLeosFlowServiceMapDstTag_Type.__name__ = "Integer32"
_WwpLeosFlowServiceMapDstTag_Object = MibTableColumn
wwpLeosFlowServiceMapDstTag = _WwpLeosFlowServiceMapDstTag_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 4, 1, 5),
    _WwpLeosFlowServiceMapDstTag_Type()
)
wwpLeosFlowServiceMapDstTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowServiceMapDstTag.setStatus("deprecated")


class _WwpLeosFlowServiceMapSrcPri_Type(Integer32):
    """Custom type wwpLeosFlowServiceMapSrcPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WwpLeosFlowServiceMapSrcPri_Type.__name__ = "Integer32"
_WwpLeosFlowServiceMapSrcPri_Object = MibTableColumn
wwpLeosFlowServiceMapSrcPri = _WwpLeosFlowServiceMapSrcPri_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 4, 1, 6),
    _WwpLeosFlowServiceMapSrcPri_Type()
)
wwpLeosFlowServiceMapSrcPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowServiceMapSrcPri.setStatus("deprecated")


class _WwpLeosFlowServiceMapProtocolType_Type(Integer32):
    """Custom type wwpLeosFlowServiceMapProtocolType based on Integer32"""
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
          ("tcp", 2),
          ("udp", 3))
    )


_WwpLeosFlowServiceMapProtocolType_Type.__name__ = "Integer32"
_WwpLeosFlowServiceMapProtocolType_Object = MibTableColumn
wwpLeosFlowServiceMapProtocolType = _WwpLeosFlowServiceMapProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 4, 1, 7),
    _WwpLeosFlowServiceMapProtocolType_Type()
)
wwpLeosFlowServiceMapProtocolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowServiceMapProtocolType.setStatus("deprecated")


class _WwpLeosFlowServiceMapProtocolPortNum_Type(Integer32):
    """Custom type wwpLeosFlowServiceMapProtocolPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLeosFlowServiceMapProtocolPortNum_Type.__name__ = "Integer32"
_WwpLeosFlowServiceMapProtocolPortNum_Object = MibTableColumn
wwpLeosFlowServiceMapProtocolPortNum = _WwpLeosFlowServiceMapProtocolPortNum_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 4, 1, 8),
    _WwpLeosFlowServiceMapProtocolPortNum_Type()
)
wwpLeosFlowServiceMapProtocolPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowServiceMapProtocolPortNum.setStatus("deprecated")


class _WwpLeosFlowServiceMapDstSlidId_Type(Integer32):
    """Custom type wwpLeosFlowServiceMapDstSlidId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_WwpLeosFlowServiceMapDstSlidId_Type.__name__ = "Integer32"
_WwpLeosFlowServiceMapDstSlidId_Object = MibTableColumn
wwpLeosFlowServiceMapDstSlidId = _WwpLeosFlowServiceMapDstSlidId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 4, 1, 9),
    _WwpLeosFlowServiceMapDstSlidId_Type()
)
wwpLeosFlowServiceMapDstSlidId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowServiceMapDstSlidId.setStatus("deprecated")


class _WwpLeosFlowServiceMapSrcSlidId_Type(Integer32):
    """Custom type wwpLeosFlowServiceMapSrcSlidId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_WwpLeosFlowServiceMapSrcSlidId_Type.__name__ = "Integer32"
_WwpLeosFlowServiceMapSrcSlidId_Object = MibTableColumn
wwpLeosFlowServiceMapSrcSlidId = _WwpLeosFlowServiceMapSrcSlidId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 4, 1, 10),
    _WwpLeosFlowServiceMapSrcSlidId_Type()
)
wwpLeosFlowServiceMapSrcSlidId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowServiceMapSrcSlidId.setStatus("deprecated")
_WwpLeosFlowServiceMapPriRemarkStatus_Type = TruthValue
_WwpLeosFlowServiceMapPriRemarkStatus_Object = MibTableColumn
wwpLeosFlowServiceMapPriRemarkStatus = _WwpLeosFlowServiceMapPriRemarkStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 4, 1, 11),
    _WwpLeosFlowServiceMapPriRemarkStatus_Type()
)
wwpLeosFlowServiceMapPriRemarkStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowServiceMapPriRemarkStatus.setStatus("deprecated")


class _WwpLeosFlowServiceMapRemarkPri_Type(Integer32):
    """Custom type wwpLeosFlowServiceMapRemarkPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_WwpLeosFlowServiceMapRemarkPri_Type.__name__ = "Integer32"
_WwpLeosFlowServiceMapRemarkPri_Object = MibTableColumn
wwpLeosFlowServiceMapRemarkPri = _WwpLeosFlowServiceMapRemarkPri_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 4, 1, 12),
    _WwpLeosFlowServiceMapRemarkPri_Type()
)
wwpLeosFlowServiceMapRemarkPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowServiceMapRemarkPri.setStatus("deprecated")
_WwpLeosFlowServiceMapStatus_Type = RowStatus
_WwpLeosFlowServiceMapStatus_Object = MibTableColumn
wwpLeosFlowServiceMapStatus = _WwpLeosFlowServiceMapStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 4, 1, 13),
    _WwpLeosFlowServiceMapStatus_Type()
)
wwpLeosFlowServiceMapStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosFlowServiceMapStatus.setStatus("deprecated")
_WwpLeosFlowServiceACTable_Object = MibTable
wwpLeosFlowServiceACTable = _WwpLeosFlowServiceACTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 5)
)
if mibBuilder.loadTexts:
    wwpLeosFlowServiceACTable.setStatus("current")
_WwpLeosFlowServiceACEntry_Object = MibTableRow
wwpLeosFlowServiceACEntry = _WwpLeosFlowServiceACEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 5, 1)
)
wwpLeosFlowServiceACEntry.setIndexNames(
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowServiceACPortId"),
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowServiceACVid"),
)
if mibBuilder.loadTexts:
    wwpLeosFlowServiceACEntry.setStatus("current")


class _WwpLeosFlowServiceACPortId_Type(Integer32):
    """Custom type wwpLeosFlowServiceACPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosFlowServiceACPortId_Type.__name__ = "Integer32"
_WwpLeosFlowServiceACPortId_Object = MibTableColumn
wwpLeosFlowServiceACPortId = _WwpLeosFlowServiceACPortId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 5, 1, 1),
    _WwpLeosFlowServiceACPortId_Type()
)
wwpLeosFlowServiceACPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowServiceACPortId.setStatus("current")


class _WwpLeosFlowServiceACVid_Type(Integer32):
    """Custom type wwpLeosFlowServiceACVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24576),
    )


_WwpLeosFlowServiceACVid_Type.__name__ = "Integer32"
_WwpLeosFlowServiceACVid_Object = MibTableColumn
wwpLeosFlowServiceACVid = _WwpLeosFlowServiceACVid_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 5, 1, 2),
    _WwpLeosFlowServiceACVid_Type()
)
wwpLeosFlowServiceACVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowServiceACVid.setStatus("current")


class _WwpLeosFlowServiceACMaxDynamicMacCount_Type(Integer32):
    """Custom type wwpLeosFlowServiceACMaxDynamicMacCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WwpLeosFlowServiceACMaxDynamicMacCount_Type.__name__ = "Integer32"
_WwpLeosFlowServiceACMaxDynamicMacCount_Object = MibTableColumn
wwpLeosFlowServiceACMaxDynamicMacCount = _WwpLeosFlowServiceACMaxDynamicMacCount_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 5, 1, 3),
    _WwpLeosFlowServiceACMaxDynamicMacCount_Type()
)
wwpLeosFlowServiceACMaxDynamicMacCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosFlowServiceACMaxDynamicMacCount.setStatus("current")


class _WwpLeosFlowServiceACDynamicNonFilteredMacCount_Type(Integer32):
    """Custom type wwpLeosFlowServiceACDynamicNonFilteredMacCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WwpLeosFlowServiceACDynamicNonFilteredMacCount_Type.__name__ = "Integer32"
_WwpLeosFlowServiceACDynamicNonFilteredMacCount_Object = MibTableColumn
wwpLeosFlowServiceACDynamicNonFilteredMacCount = _WwpLeosFlowServiceACDynamicNonFilteredMacCount_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 5, 1, 4),
    _WwpLeosFlowServiceACDynamicNonFilteredMacCount_Type()
)
wwpLeosFlowServiceACDynamicNonFilteredMacCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowServiceACDynamicNonFilteredMacCount.setStatus("current")


class _WwpLeosFlowServiceACDynamicFilteredMacCount_Type(Integer32):
    """Custom type wwpLeosFlowServiceACDynamicFilteredMacCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WwpLeosFlowServiceACDynamicFilteredMacCount_Type.__name__ = "Integer32"
_WwpLeosFlowServiceACDynamicFilteredMacCount_Object = MibTableColumn
wwpLeosFlowServiceACDynamicFilteredMacCount = _WwpLeosFlowServiceACDynamicFilteredMacCount_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 5, 1, 5),
    _WwpLeosFlowServiceACDynamicFilteredMacCount_Type()
)
wwpLeosFlowServiceACDynamicFilteredMacCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowServiceACDynamicFilteredMacCount.setStatus("current")
_WwpLeosFlowServiceACStatus_Type = RowStatus
_WwpLeosFlowServiceACStatus_Object = MibTableColumn
wwpLeosFlowServiceACStatus = _WwpLeosFlowServiceACStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 5, 1, 7),
    _WwpLeosFlowServiceACStatus_Type()
)
wwpLeosFlowServiceACStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosFlowServiceACStatus.setStatus("current")


class _WwpLeosFlowServiceACForwardLearning_Type(Integer32):
    """Custom type wwpLeosFlowServiceACForwardLearning based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WwpLeosFlowServiceACForwardLearning_Type.__name__ = "Integer32"
_WwpLeosFlowServiceACForwardLearning_Object = MibTableColumn
wwpLeosFlowServiceACForwardLearning = _WwpLeosFlowServiceACForwardLearning_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 5, 1, 50),
    _WwpLeosFlowServiceACForwardLearning_Type()
)
wwpLeosFlowServiceACForwardLearning.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosFlowServiceACForwardLearning.setStatus("current")
_WwpLeosFlowStaticMacTable_Object = MibTable
wwpLeosFlowStaticMacTable = _WwpLeosFlowStaticMacTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 6)
)
if mibBuilder.loadTexts:
    wwpLeosFlowStaticMacTable.setStatus("current")
_WwpLeosFlowStaticMacEntry_Object = MibTableRow
wwpLeosFlowStaticMacEntry = _WwpLeosFlowStaticMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 6, 1)
)
wwpLeosFlowStaticMacEntry.setIndexNames(
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowSMVid"),
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowSMMacAddr"),
)
if mibBuilder.loadTexts:
    wwpLeosFlowStaticMacEntry.setStatus("current")


class _WwpLeosFlowSMVid_Type(Integer32):
    """Custom type wwpLeosFlowSMVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24576),
    )


_WwpLeosFlowSMVid_Type.__name__ = "Integer32"
_WwpLeosFlowSMVid_Object = MibTableColumn
wwpLeosFlowSMVid = _WwpLeosFlowSMVid_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 6, 1, 1),
    _WwpLeosFlowSMVid_Type()
)
wwpLeosFlowSMVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowSMVid.setStatus("current")
_WwpLeosFlowSMMacAddr_Type = MacAddress
_WwpLeosFlowSMMacAddr_Object = MibTableColumn
wwpLeosFlowSMMacAddr = _WwpLeosFlowSMMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 6, 1, 2),
    _WwpLeosFlowSMMacAddr_Type()
)
wwpLeosFlowSMMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowSMMacAddr.setStatus("current")


class _WwpLeosFlowSMPortId_Type(Integer32):
    """Custom type wwpLeosFlowSMPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosFlowSMPortId_Type.__name__ = "Integer32"
_WwpLeosFlowSMPortId_Object = MibTableColumn
wwpLeosFlowSMPortId = _WwpLeosFlowSMPortId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 6, 1, 3),
    _WwpLeosFlowSMPortId_Type()
)
wwpLeosFlowSMPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosFlowSMPortId.setStatus("current")


class _WwpLeosFlowSMTag_Type(Integer32):
    """Custom type wwpLeosFlowSMTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_WwpLeosFlowSMTag_Type.__name__ = "Integer32"
_WwpLeosFlowSMTag_Object = MibTableColumn
wwpLeosFlowSMTag = _WwpLeosFlowSMTag_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 6, 1, 4),
    _WwpLeosFlowSMTag_Type()
)
wwpLeosFlowSMTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosFlowSMTag.setStatus("current")
_WwpLeosFlowSMStatus_Type = RowStatus
_WwpLeosFlowSMStatus_Object = MibTableColumn
wwpLeosFlowSMStatus = _WwpLeosFlowSMStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 6, 1, 5),
    _WwpLeosFlowSMStatus_Type()
)
wwpLeosFlowSMStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosFlowSMStatus.setStatus("current")
_WwpLeosFlowLearnTable_Object = MibTable
wwpLeosFlowLearnTable = _WwpLeosFlowLearnTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 7)
)
if mibBuilder.loadTexts:
    wwpLeosFlowLearnTable.setStatus("current")
_WwpLeosFlowLearnEntry_Object = MibTableRow
wwpLeosFlowLearnEntry = _WwpLeosFlowLearnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 7, 1)
)
wwpLeosFlowLearnEntry.setIndexNames(
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowLearnVid"),
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowLearnAddr"),
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowLearnSrcPort"),
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowLearnSrcTag"),
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowLearnSrcPri"),
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowLearnAddrType"),
)
if mibBuilder.loadTexts:
    wwpLeosFlowLearnEntry.setStatus("current")


class _WwpLeosFlowLearnVid_Type(Integer32):
    """Custom type wwpLeosFlowLearnVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24576),
    )


_WwpLeosFlowLearnVid_Type.__name__ = "Integer32"
_WwpLeosFlowLearnVid_Object = MibTableColumn
wwpLeosFlowLearnVid = _WwpLeosFlowLearnVid_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 7, 1, 1),
    _WwpLeosFlowLearnVid_Type()
)
wwpLeosFlowLearnVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowLearnVid.setStatus("current")
_WwpLeosFlowLearnAddr_Type = MacAddress
_WwpLeosFlowLearnAddr_Object = MibTableColumn
wwpLeosFlowLearnAddr = _WwpLeosFlowLearnAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 7, 1, 2),
    _WwpLeosFlowLearnAddr_Type()
)
wwpLeosFlowLearnAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowLearnAddr.setStatus("current")


class _WwpLeosFlowLearnSrcPort_Type(Integer32):
    """Custom type wwpLeosFlowLearnSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosFlowLearnSrcPort_Type.__name__ = "Integer32"
_WwpLeosFlowLearnSrcPort_Object = MibTableColumn
wwpLeosFlowLearnSrcPort = _WwpLeosFlowLearnSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 7, 1, 3),
    _WwpLeosFlowLearnSrcPort_Type()
)
wwpLeosFlowLearnSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowLearnSrcPort.setStatus("current")


class _WwpLeosFlowLearnSrcTag_Type(Integer32):
    """Custom type wwpLeosFlowLearnSrcTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_WwpLeosFlowLearnSrcTag_Type.__name__ = "Integer32"
_WwpLeosFlowLearnSrcTag_Object = MibTableColumn
wwpLeosFlowLearnSrcTag = _WwpLeosFlowLearnSrcTag_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 7, 1, 4),
    _WwpLeosFlowLearnSrcTag_Type()
)
wwpLeosFlowLearnSrcTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowLearnSrcTag.setStatus("current")


class _WwpLeosFlowLearnSrcPri_Type(Integer32):
    """Custom type wwpLeosFlowLearnSrcPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosFlowLearnSrcPri_Type.__name__ = "Integer32"
_WwpLeosFlowLearnSrcPri_Object = MibTableColumn
wwpLeosFlowLearnSrcPri = _WwpLeosFlowLearnSrcPri_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 7, 1, 5),
    _WwpLeosFlowLearnSrcPri_Type()
)
wwpLeosFlowLearnSrcPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowLearnSrcPri.setStatus("current")


class _WwpLeosFlowLearnAddrType_Type(Integer32):
    """Custom type wwpLeosFlowLearnAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("layer2", 1),
          ("layer3", 2))
    )


_WwpLeosFlowLearnAddrType_Type.__name__ = "Integer32"
_WwpLeosFlowLearnAddrType_Object = MibTableColumn
wwpLeosFlowLearnAddrType = _WwpLeosFlowLearnAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 7, 1, 6),
    _WwpLeosFlowLearnAddrType_Type()
)
wwpLeosFlowLearnAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowLearnAddrType.setStatus("current")


class _WwpLeosFlowLearnDstPort_Type(Integer32):
    """Custom type wwpLeosFlowLearnDstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosFlowLearnDstPort_Type.__name__ = "Integer32"
_WwpLeosFlowLearnDstPort_Object = MibTableColumn
wwpLeosFlowLearnDstPort = _WwpLeosFlowLearnDstPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 7, 1, 7),
    _WwpLeosFlowLearnDstPort_Type()
)
wwpLeosFlowLearnDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowLearnDstPort.setStatus("current")


class _WwpLeosFlowLearnDstTag_Type(Integer32):
    """Custom type wwpLeosFlowLearnDstTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_WwpLeosFlowLearnDstTag_Type.__name__ = "Integer32"
_WwpLeosFlowLearnDstTag_Object = MibTableColumn
wwpLeosFlowLearnDstTag = _WwpLeosFlowLearnDstTag_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 7, 1, 8),
    _WwpLeosFlowLearnDstTag_Type()
)
wwpLeosFlowLearnDstTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowLearnDstTag.setStatus("current")


class _WwpLeosFlowLearnType_Type(Integer32):
    """Custom type wwpLeosFlowLearnType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 2))
    )


_WwpLeosFlowLearnType_Type.__name__ = "Integer32"
_WwpLeosFlowLearnType_Object = MibTableColumn
wwpLeosFlowLearnType = _WwpLeosFlowLearnType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 7, 1, 9),
    _WwpLeosFlowLearnType_Type()
)
wwpLeosFlowLearnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowLearnType.setStatus("current")
_WwpLeosFlowLearnIsFiltered_Type = TruthValue
_WwpLeosFlowLearnIsFiltered_Object = MibTableColumn
wwpLeosFlowLearnIsFiltered = _WwpLeosFlowLearnIsFiltered_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 7, 1, 10),
    _WwpLeosFlowLearnIsFiltered_Type()
)
wwpLeosFlowLearnIsFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowLearnIsFiltered.setStatus("current")
_WwpLeosFlowServiceStatsTable_Object = MibTable
wwpLeosFlowServiceStatsTable = _WwpLeosFlowServiceStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 8)
)
if mibBuilder.loadTexts:
    wwpLeosFlowServiceStatsTable.setStatus("deprecated")
_WwpLeosFlowServiceStatsEntry_Object = MibTableRow
wwpLeosFlowServiceStatsEntry = _WwpLeosFlowServiceStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 8, 1)
)
wwpLeosFlowServiceStatsEntry.setIndexNames(
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowServiceMapVid"),
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowServiceMapSrcPort"),
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowServiceMapSrcTag"),
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowServiceMapDstPort"),
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowServiceMapDstTag"),
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowServiceMapSrcPri"),
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowServiceMapProtocolType"),
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowServiceMapProtocolPortNum"),
)
if mibBuilder.loadTexts:
    wwpLeosFlowServiceStatsEntry.setStatus("deprecated")
_WwpLeosFlowServiceStatsRxHi_Type = Counter32
_WwpLeosFlowServiceStatsRxHi_Object = MibTableColumn
wwpLeosFlowServiceStatsRxHi = _WwpLeosFlowServiceStatsRxHi_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 8, 1, 1),
    _WwpLeosFlowServiceStatsRxHi_Type()
)
wwpLeosFlowServiceStatsRxHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowServiceStatsRxHi.setStatus("deprecated")
_WwpLeosFlowServiceStatsRxLo_Type = Counter32
_WwpLeosFlowServiceStatsRxLo_Object = MibTableColumn
wwpLeosFlowServiceStatsRxLo = _WwpLeosFlowServiceStatsRxLo_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 8, 1, 2),
    _WwpLeosFlowServiceStatsRxLo_Type()
)
wwpLeosFlowServiceStatsRxLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowServiceStatsRxLo.setStatus("deprecated")
_WwpLeosFlowServiceStatsTxHi_Type = Counter32
_WwpLeosFlowServiceStatsTxHi_Object = MibTableColumn
wwpLeosFlowServiceStatsTxHi = _WwpLeosFlowServiceStatsTxHi_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 8, 1, 3),
    _WwpLeosFlowServiceStatsTxHi_Type()
)
wwpLeosFlowServiceStatsTxHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowServiceStatsTxHi.setStatus("deprecated")
_WwpLeosFlowServiceStatsTxLo_Type = Counter32
_WwpLeosFlowServiceStatsTxLo_Object = MibTableColumn
wwpLeosFlowServiceStatsTxLo = _WwpLeosFlowServiceStatsTxLo_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 8, 1, 4),
    _WwpLeosFlowServiceStatsTxLo_Type()
)
wwpLeosFlowServiceStatsTxLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowServiceStatsTxLo.setStatus("deprecated")


class _WwpLeosFlowServiceStatsType_Type(Integer32):
    """Custom type wwpLeosFlowServiceStatsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 2),
          ("forward", 1))
    )


_WwpLeosFlowServiceStatsType_Type.__name__ = "Integer32"
_WwpLeosFlowServiceStatsType_Object = MibTableColumn
wwpLeosFlowServiceStatsType = _WwpLeosFlowServiceStatsType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 8, 1, 5),
    _WwpLeosFlowServiceStatsType_Type()
)
wwpLeosFlowServiceStatsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowServiceStatsType.setStatus("deprecated")
_WwpLeosFlowMacFindTable_Object = MibTable
wwpLeosFlowMacFindTable = _WwpLeosFlowMacFindTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 9)
)
if mibBuilder.loadTexts:
    wwpLeosFlowMacFindTable.setStatus("current")
_WwpLeosFlowMacFindEntry_Object = MibTableRow
wwpLeosFlowMacFindEntry = _WwpLeosFlowMacFindEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 9, 1)
)
wwpLeosFlowMacFindEntry.setIndexNames(
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowMacFindVlanId"),
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowMacFindMacAddr"),
)
if mibBuilder.loadTexts:
    wwpLeosFlowMacFindEntry.setStatus("current")
_WwpLeosFlowMacFindMacAddr_Type = MacAddress
_WwpLeosFlowMacFindMacAddr_Object = MibTableColumn
wwpLeosFlowMacFindMacAddr = _WwpLeosFlowMacFindMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 9, 1, 1),
    _WwpLeosFlowMacFindMacAddr_Type()
)
wwpLeosFlowMacFindMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowMacFindMacAddr.setStatus("current")


class _WwpLeosFlowMacFindVlanId_Type(Integer32):
    """Custom type wwpLeosFlowMacFindVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24576),
    )


_WwpLeosFlowMacFindVlanId_Type.__name__ = "Integer32"
_WwpLeosFlowMacFindVlanId_Object = MibTableColumn
wwpLeosFlowMacFindVlanId = _WwpLeosFlowMacFindVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 9, 1, 2),
    _WwpLeosFlowMacFindVlanId_Type()
)
wwpLeosFlowMacFindVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowMacFindVlanId.setStatus("current")


class _WwpLeosFlowMacFindPort_Type(Integer32):
    """Custom type wwpLeosFlowMacFindPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosFlowMacFindPort_Type.__name__ = "Integer32"
_WwpLeosFlowMacFindPort_Object = MibTableColumn
wwpLeosFlowMacFindPort = _WwpLeosFlowMacFindPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 9, 1, 3),
    _WwpLeosFlowMacFindPort_Type()
)
wwpLeosFlowMacFindPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowMacFindPort.setStatus("current")


class _WwpLeosFlowMacFindVlanTag_Type(Integer32):
    """Custom type wwpLeosFlowMacFindVlanTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24576),
    )


_WwpLeosFlowMacFindVlanTag_Type.__name__ = "Integer32"
_WwpLeosFlowMacFindVlanTag_Object = MibTableColumn
wwpLeosFlowMacFindVlanTag = _WwpLeosFlowMacFindVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 9, 1, 4),
    _WwpLeosFlowMacFindVlanTag_Type()
)
wwpLeosFlowMacFindVlanTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowMacFindVlanTag.setStatus("current")
_WwpLeosFlowPriRemapTable_Object = MibTable
wwpLeosFlowPriRemapTable = _WwpLeosFlowPriRemapTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 10)
)
if mibBuilder.loadTexts:
    wwpLeosFlowPriRemapTable.setStatus("current")
_WwpLeosFlowPriRemapEntry_Object = MibTableRow
wwpLeosFlowPriRemapEntry = _WwpLeosFlowPriRemapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 10, 1)
)
wwpLeosFlowPriRemapEntry.setIndexNames(
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowUserPri"),
)
if mibBuilder.loadTexts:
    wwpLeosFlowPriRemapEntry.setStatus("current")


class _WwpLeosFlowUserPri_Type(Integer32):
    """Custom type wwpLeosFlowUserPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosFlowUserPri_Type.__name__ = "Integer32"
_WwpLeosFlowUserPri_Object = MibTableColumn
wwpLeosFlowUserPri = _WwpLeosFlowUserPri_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 10, 1, 1),
    _WwpLeosFlowUserPri_Type()
)
wwpLeosFlowUserPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowUserPri.setStatus("current")


class _WwpLeosFlowRemappedPri_Type(Integer32):
    """Custom type wwpLeosFlowRemappedPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosFlowRemappedPri_Type.__name__ = "Integer32"
_WwpLeosFlowRemappedPri_Object = MibTableColumn
wwpLeosFlowRemappedPri = _WwpLeosFlowRemappedPri_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 10, 1, 2),
    _WwpLeosFlowRemappedPri_Type()
)
wwpLeosFlowRemappedPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowRemappedPri.setStatus("current")
_WwpLeosFlowSMappingTable_Object = MibTable
wwpLeosFlowSMappingTable = _WwpLeosFlowSMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 13)
)
if mibBuilder.loadTexts:
    wwpLeosFlowSMappingTable.setStatus("current")
_WwpLeosFlowSMappingEntry_Object = MibTableRow
wwpLeosFlowSMappingEntry = _WwpLeosFlowSMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 13, 1)
)
wwpLeosFlowSMappingEntry.setIndexNames(
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowSMappingNetType"),
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowSMappingNetValue"),
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowSMappingSrcType"),
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowSMappingSrcValue"),
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowSMappingDstType"),
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowSMappingDstValue"),
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowSMappingCosType"),
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowSMappingCosValue"),
)
if mibBuilder.loadTexts:
    wwpLeosFlowSMappingEntry.setStatus("current")


class _WwpLeosFlowSMappingNetType_Type(Integer32):
    """Custom type wwpLeosFlowSMappingNetType based on Integer32"""
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
        *(("none", 1),
          ("vlan", 2),
          ("vsi", 3),
          ("vsiMpls", 4))
    )


_WwpLeosFlowSMappingNetType_Type.__name__ = "Integer32"
_WwpLeosFlowSMappingNetType_Object = MibTableColumn
wwpLeosFlowSMappingNetType = _WwpLeosFlowSMappingNetType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 13, 1, 1),
    _WwpLeosFlowSMappingNetType_Type()
)
wwpLeosFlowSMappingNetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowSMappingNetType.setStatus("current")
_WwpLeosFlowSMappingNetValue_Type = Unsigned32
_WwpLeosFlowSMappingNetValue_Object = MibTableColumn
wwpLeosFlowSMappingNetValue = _WwpLeosFlowSMappingNetValue_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 13, 1, 2),
    _WwpLeosFlowSMappingNetValue_Type()
)
wwpLeosFlowSMappingNetValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowSMappingNetValue.setStatus("current")


class _WwpLeosFlowSMappingSrcType_Type(Integer32):
    """Custom type wwpLeosFlowSMappingSrcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mplsVc", 3),
          ("none", 1),
          ("port", 2))
    )


_WwpLeosFlowSMappingSrcType_Type.__name__ = "Integer32"
_WwpLeosFlowSMappingSrcType_Object = MibTableColumn
wwpLeosFlowSMappingSrcType = _WwpLeosFlowSMappingSrcType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 13, 1, 3),
    _WwpLeosFlowSMappingSrcType_Type()
)
wwpLeosFlowSMappingSrcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowSMappingSrcType.setStatus("current")
_WwpLeosFlowSMappingSrcValue_Type = Unsigned32
_WwpLeosFlowSMappingSrcValue_Object = MibTableColumn
wwpLeosFlowSMappingSrcValue = _WwpLeosFlowSMappingSrcValue_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 13, 1, 4),
    _WwpLeosFlowSMappingSrcValue_Type()
)
wwpLeosFlowSMappingSrcValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowSMappingSrcValue.setStatus("current")


class _WwpLeosFlowSMappingDstType_Type(Integer32):
    """Custom type wwpLeosFlowSMappingDstType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mplsVc", 3),
          ("none", 1),
          ("port", 2))
    )


_WwpLeosFlowSMappingDstType_Type.__name__ = "Integer32"
_WwpLeosFlowSMappingDstType_Object = MibTableColumn
wwpLeosFlowSMappingDstType = _WwpLeosFlowSMappingDstType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 13, 1, 5),
    _WwpLeosFlowSMappingDstType_Type()
)
wwpLeosFlowSMappingDstType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowSMappingDstType.setStatus("current")
_WwpLeosFlowSMappingDstValue_Type = Unsigned32
_WwpLeosFlowSMappingDstValue_Object = MibTableColumn
wwpLeosFlowSMappingDstValue = _WwpLeosFlowSMappingDstValue_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 13, 1, 6),
    _WwpLeosFlowSMappingDstValue_Type()
)
wwpLeosFlowSMappingDstValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowSMappingDstValue.setStatus("current")


class _WwpLeosFlowSMappingCosType_Type(Integer32):
    """Custom type wwpLeosFlowSMappingCosType based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("cvlan", 12),
          ("dot1dPri", 5),
          ("dscp", 3),
          ("ipPrec", 4),
          ("mplsExp", 6),
          ("none", 1),
          ("pcp", 11),
          ("phb", 2),
          ("tcpDstPort", 8),
          ("tcpSrcPort", 7),
          ("udpDstPort", 10),
          ("udpSrcPort", 9))
    )


_WwpLeosFlowSMappingCosType_Type.__name__ = "Integer32"
_WwpLeosFlowSMappingCosType_Object = MibTableColumn
wwpLeosFlowSMappingCosType = _WwpLeosFlowSMappingCosType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 13, 1, 7),
    _WwpLeosFlowSMappingCosType_Type()
)
wwpLeosFlowSMappingCosType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowSMappingCosType.setStatus("current")
_WwpLeosFlowSMappingCosValue_Type = Unsigned32
_WwpLeosFlowSMappingCosValue_Object = MibTableColumn
wwpLeosFlowSMappingCosValue = _WwpLeosFlowSMappingCosValue_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 13, 1, 8),
    _WwpLeosFlowSMappingCosValue_Type()
)
wwpLeosFlowSMappingCosValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowSMappingCosValue.setStatus("current")
_WwpLeosFlowSMappingDstSlid_Type = Unsigned32
_WwpLeosFlowSMappingDstSlid_Object = MibTableColumn
wwpLeosFlowSMappingDstSlid = _WwpLeosFlowSMappingDstSlid_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 13, 1, 9),
    _WwpLeosFlowSMappingDstSlid_Type()
)
wwpLeosFlowSMappingDstSlid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowSMappingDstSlid.setStatus("current")
_WwpLeosFlowSMappingSrcSlid_Type = Unsigned32
_WwpLeosFlowSMappingSrcSlid_Object = MibTableColumn
wwpLeosFlowSMappingSrcSlid = _WwpLeosFlowSMappingSrcSlid_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 13, 1, 10),
    _WwpLeosFlowSMappingSrcSlid_Type()
)
wwpLeosFlowSMappingSrcSlid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowSMappingSrcSlid.setStatus("current")
_WwpLeosFlowSMappingStatus_Type = RowStatus
_WwpLeosFlowSMappingStatus_Object = MibTableColumn
wwpLeosFlowSMappingStatus = _WwpLeosFlowSMappingStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 13, 1, 11),
    _WwpLeosFlowSMappingStatus_Type()
)
wwpLeosFlowSMappingStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosFlowSMappingStatus.setStatus("current")


class _WwpLeosFlowSMappingRedCurveOffset_Type(Integer32):
    """Custom type wwpLeosFlowSMappingRedCurveOffset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_WwpLeosFlowSMappingRedCurveOffset_Type.__name__ = "Integer32"
_WwpLeosFlowSMappingRedCurveOffset_Object = MibTableColumn
wwpLeosFlowSMappingRedCurveOffset = _WwpLeosFlowSMappingRedCurveOffset_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 13, 1, 12),
    _WwpLeosFlowSMappingRedCurveOffset_Type()
)
wwpLeosFlowSMappingRedCurveOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosFlowSMappingRedCurveOffset.setStatus("current")


class _WwpLeosFlowSMappingCpuPort_Type(TruthValue):
    """Custom type wwpLeosFlowSMappingCpuPort based on TruthValue"""


_WwpLeosFlowSMappingCpuPort_Object = MibTableColumn
wwpLeosFlowSMappingCpuPort = _WwpLeosFlowSMappingCpuPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 13, 1, 13),
    _WwpLeosFlowSMappingCpuPort_Type()
)
wwpLeosFlowSMappingCpuPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosFlowSMappingCpuPort.setStatus("current")
_WwpLeosFlowSMappingStatsTable_Object = MibTable
wwpLeosFlowSMappingStatsTable = _WwpLeosFlowSMappingStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 14)
)
if mibBuilder.loadTexts:
    wwpLeosFlowSMappingStatsTable.setStatus("current")
_WwpLeosFlowSMappingStatsEntry_Object = MibTableRow
wwpLeosFlowSMappingStatsEntry = _WwpLeosFlowSMappingStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 14, 1)
)
wwpLeosFlowSMappingStatsEntry.setIndexNames(
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowSMappingNetType"),
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowSMappingNetValue"),
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowSMappingSrcType"),
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowSMappingSrcValue"),
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowSMappingDstType"),
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowSMappingDstValue"),
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowSMappingCosType"),
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowSMappingCosValue"),
)
if mibBuilder.loadTexts:
    wwpLeosFlowSMappingStatsEntry.setStatus("current")
_WwpLeosFlowSMappingStatsRxHi_Type = Counter32
_WwpLeosFlowSMappingStatsRxHi_Object = MibTableColumn
wwpLeosFlowSMappingStatsRxHi = _WwpLeosFlowSMappingStatsRxHi_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 14, 1, 1),
    _WwpLeosFlowSMappingStatsRxHi_Type()
)
wwpLeosFlowSMappingStatsRxHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowSMappingStatsRxHi.setStatus("current")
_WwpLeosFlowSMappingStatsRxLo_Type = Counter32
_WwpLeosFlowSMappingStatsRxLo_Object = MibTableColumn
wwpLeosFlowSMappingStatsRxLo = _WwpLeosFlowSMappingStatsRxLo_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 14, 1, 2),
    _WwpLeosFlowSMappingStatsRxLo_Type()
)
wwpLeosFlowSMappingStatsRxLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowSMappingStatsRxLo.setStatus("current")
_WwpLeosFlowSMappingStatsTxHi_Type = Counter32
_WwpLeosFlowSMappingStatsTxHi_Object = MibTableColumn
wwpLeosFlowSMappingStatsTxHi = _WwpLeosFlowSMappingStatsTxHi_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 14, 1, 3),
    _WwpLeosFlowSMappingStatsTxHi_Type()
)
wwpLeosFlowSMappingStatsTxHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowSMappingStatsTxHi.setStatus("current")
_WwpLeosFlowSMappingStatsTxLo_Type = Counter32
_WwpLeosFlowSMappingStatsTxLo_Object = MibTableColumn
wwpLeosFlowSMappingStatsTxLo = _WwpLeosFlowSMappingStatsTxLo_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 14, 1, 4),
    _WwpLeosFlowSMappingStatsTxLo_Type()
)
wwpLeosFlowSMappingStatsTxLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowSMappingStatsTxLo.setStatus("current")


class _WwpLeosFlowSMappingStatsType_Type(Integer32):
    """Custom type wwpLeosFlowSMappingStatsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 2),
          ("forward", 1))
    )


_WwpLeosFlowSMappingStatsType_Type.__name__ = "Integer32"
_WwpLeosFlowSMappingStatsType_Object = MibTableColumn
wwpLeosFlowSMappingStatsType = _WwpLeosFlowSMappingStatsType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 14, 1, 5),
    _WwpLeosFlowSMappingStatsType_Type()
)
wwpLeosFlowSMappingStatsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowSMappingStatsType.setStatus("current")
_WwpLeosFlowCosSync1dToExpTable_Object = MibTable
wwpLeosFlowCosSync1dToExpTable = _WwpLeosFlowCosSync1dToExpTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 15)
)
if mibBuilder.loadTexts:
    wwpLeosFlowCosSync1dToExpTable.setStatus("current")
_WwpLeosFlowCosSync1dToExpEntry_Object = MibTableRow
wwpLeosFlowCosSync1dToExpEntry = _WwpLeosFlowCosSync1dToExpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 15, 1)
)
wwpLeosFlowCosSync1dToExpEntry.setIndexNames(
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowCosSync1dToExpMapFrom"),
)
if mibBuilder.loadTexts:
    wwpLeosFlowCosSync1dToExpEntry.setStatus("current")


class _WwpLeosFlowCosSync1dToExpMapFrom_Type(Integer32):
    """Custom type wwpLeosFlowCosSync1dToExpMapFrom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosFlowCosSync1dToExpMapFrom_Type.__name__ = "Integer32"
_WwpLeosFlowCosSync1dToExpMapFrom_Object = MibTableColumn
wwpLeosFlowCosSync1dToExpMapFrom = _WwpLeosFlowCosSync1dToExpMapFrom_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 15, 1, 1),
    _WwpLeosFlowCosSync1dToExpMapFrom_Type()
)
wwpLeosFlowCosSync1dToExpMapFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCosSync1dToExpMapFrom.setStatus("current")


class _WwpLeosFlowCosSync1dToExpMapTo_Type(Integer32):
    """Custom type wwpLeosFlowCosSync1dToExpMapTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosFlowCosSync1dToExpMapTo_Type.__name__ = "Integer32"
_WwpLeosFlowCosSync1dToExpMapTo_Object = MibTableColumn
wwpLeosFlowCosSync1dToExpMapTo = _WwpLeosFlowCosSync1dToExpMapTo_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 15, 1, 2),
    _WwpLeosFlowCosSync1dToExpMapTo_Type()
)
wwpLeosFlowCosSync1dToExpMapTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowCosSync1dToExpMapTo.setStatus("current")
_WwpLeosFlowCosSyncExpTo1dTable_Object = MibTable
wwpLeosFlowCosSyncExpTo1dTable = _WwpLeosFlowCosSyncExpTo1dTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 16)
)
if mibBuilder.loadTexts:
    wwpLeosFlowCosSyncExpTo1dTable.setStatus("current")
_WwpLeosFlowCosSyncExpTo1dEntry_Object = MibTableRow
wwpLeosFlowCosSyncExpTo1dEntry = _WwpLeosFlowCosSyncExpTo1dEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 16, 1)
)
wwpLeosFlowCosSyncExpTo1dEntry.setIndexNames(
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowCosSyncExpTo1dMapFrom"),
)
if mibBuilder.loadTexts:
    wwpLeosFlowCosSyncExpTo1dEntry.setStatus("current")


class _WwpLeosFlowCosSyncExpTo1dMapFrom_Type(Integer32):
    """Custom type wwpLeosFlowCosSyncExpTo1dMapFrom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosFlowCosSyncExpTo1dMapFrom_Type.__name__ = "Integer32"
_WwpLeosFlowCosSyncExpTo1dMapFrom_Object = MibTableColumn
wwpLeosFlowCosSyncExpTo1dMapFrom = _WwpLeosFlowCosSyncExpTo1dMapFrom_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 16, 1, 1),
    _WwpLeosFlowCosSyncExpTo1dMapFrom_Type()
)
wwpLeosFlowCosSyncExpTo1dMapFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCosSyncExpTo1dMapFrom.setStatus("current")


class _WwpLeosFlowCosSyncExpTo1dMapTo_Type(Integer32):
    """Custom type wwpLeosFlowCosSyncExpTo1dMapTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosFlowCosSyncExpTo1dMapTo_Type.__name__ = "Integer32"
_WwpLeosFlowCosSyncExpTo1dMapTo_Object = MibTableColumn
wwpLeosFlowCosSyncExpTo1dMapTo = _WwpLeosFlowCosSyncExpTo1dMapTo_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 16, 1, 2),
    _WwpLeosFlowCosSyncExpTo1dMapTo_Type()
)
wwpLeosFlowCosSyncExpTo1dMapTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowCosSyncExpTo1dMapTo.setStatus("current")
_WwpLeosFlowCosSyncIpPrecTo1dTable_Object = MibTable
wwpLeosFlowCosSyncIpPrecTo1dTable = _WwpLeosFlowCosSyncIpPrecTo1dTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 17)
)
if mibBuilder.loadTexts:
    wwpLeosFlowCosSyncIpPrecTo1dTable.setStatus("current")
_WwpLeosFlowCosSyncIpPrecTo1dEntry_Object = MibTableRow
wwpLeosFlowCosSyncIpPrecTo1dEntry = _WwpLeosFlowCosSyncIpPrecTo1dEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 17, 1)
)
wwpLeosFlowCosSyncIpPrecTo1dEntry.setIndexNames(
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowCosSyncIpPrecTo1dMapFrom"),
)
if mibBuilder.loadTexts:
    wwpLeosFlowCosSyncIpPrecTo1dEntry.setStatus("current")


class _WwpLeosFlowCosSyncIpPrecTo1dMapFrom_Type(Integer32):
    """Custom type wwpLeosFlowCosSyncIpPrecTo1dMapFrom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosFlowCosSyncIpPrecTo1dMapFrom_Type.__name__ = "Integer32"
_WwpLeosFlowCosSyncIpPrecTo1dMapFrom_Object = MibTableColumn
wwpLeosFlowCosSyncIpPrecTo1dMapFrom = _WwpLeosFlowCosSyncIpPrecTo1dMapFrom_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 17, 1, 1),
    _WwpLeosFlowCosSyncIpPrecTo1dMapFrom_Type()
)
wwpLeosFlowCosSyncIpPrecTo1dMapFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCosSyncIpPrecTo1dMapFrom.setStatus("current")


class _WwpLeosFlowCosSyncIpPrecTo1dMapTo_Type(Integer32):
    """Custom type wwpLeosFlowCosSyncIpPrecTo1dMapTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosFlowCosSyncIpPrecTo1dMapTo_Type.__name__ = "Integer32"
_WwpLeosFlowCosSyncIpPrecTo1dMapTo_Object = MibTableColumn
wwpLeosFlowCosSyncIpPrecTo1dMapTo = _WwpLeosFlowCosSyncIpPrecTo1dMapTo_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 17, 1, 2),
    _WwpLeosFlowCosSyncIpPrecTo1dMapTo_Type()
)
wwpLeosFlowCosSyncIpPrecTo1dMapTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowCosSyncIpPrecTo1dMapTo.setStatus("current")
_WwpLeosFlowCosSyncStdPhbTo1dTable_Object = MibTable
wwpLeosFlowCosSyncStdPhbTo1dTable = _WwpLeosFlowCosSyncStdPhbTo1dTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 18)
)
if mibBuilder.loadTexts:
    wwpLeosFlowCosSyncStdPhbTo1dTable.setStatus("current")
_WwpLeosFlowCosSyncStdPhbTo1dEntry_Object = MibTableRow
wwpLeosFlowCosSyncStdPhbTo1dEntry = _WwpLeosFlowCosSyncStdPhbTo1dEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 18, 1)
)
wwpLeosFlowCosSyncStdPhbTo1dEntry.setIndexNames(
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowCosSyncStdPhbTo1dMapFrom"),
)
if mibBuilder.loadTexts:
    wwpLeosFlowCosSyncStdPhbTo1dEntry.setStatus("current")


class _WwpLeosFlowCosSyncStdPhbTo1dMapFrom_Type(Integer32):
    """Custom type wwpLeosFlowCosSyncStdPhbTo1dMapFrom based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("af1", 9),
          ("af2", 10),
          ("af3", 11),
          ("af4", 12),
          ("cs0", 1),
          ("cs1", 2),
          ("cs2", 3),
          ("cs3", 4),
          ("cs4", 5),
          ("cs5", 6),
          ("cs6", 7),
          ("cs7", 8),
          ("ef", 13))
    )


_WwpLeosFlowCosSyncStdPhbTo1dMapFrom_Type.__name__ = "Integer32"
_WwpLeosFlowCosSyncStdPhbTo1dMapFrom_Object = MibTableColumn
wwpLeosFlowCosSyncStdPhbTo1dMapFrom = _WwpLeosFlowCosSyncStdPhbTo1dMapFrom_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 18, 1, 1),
    _WwpLeosFlowCosSyncStdPhbTo1dMapFrom_Type()
)
wwpLeosFlowCosSyncStdPhbTo1dMapFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCosSyncStdPhbTo1dMapFrom.setStatus("current")


class _WwpLeosFlowCosSyncStdPhbTo1dMapTo_Type(Integer32):
    """Custom type wwpLeosFlowCosSyncStdPhbTo1dMapTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosFlowCosSyncStdPhbTo1dMapTo_Type.__name__ = "Integer32"
_WwpLeosFlowCosSyncStdPhbTo1dMapTo_Object = MibTableColumn
wwpLeosFlowCosSyncStdPhbTo1dMapTo = _WwpLeosFlowCosSyncStdPhbTo1dMapTo_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 18, 1, 2),
    _WwpLeosFlowCosSyncStdPhbTo1dMapTo_Type()
)
wwpLeosFlowCosSyncStdPhbTo1dMapTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowCosSyncStdPhbTo1dMapTo.setStatus("current")
_WwpLeosFlowL2SacTable_Object = MibTable
wwpLeosFlowL2SacTable = _WwpLeosFlowL2SacTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 19)
)
if mibBuilder.loadTexts:
    wwpLeosFlowL2SacTable.setStatus("current")
_WwpLeosFlowL2SacEntry_Object = MibTableRow
wwpLeosFlowL2SacEntry = _WwpLeosFlowL2SacEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 19, 1)
)
wwpLeosFlowL2SacEntry.setIndexNames(
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowL2SacPortId"),
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowL2SacNetType"),
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowSacNetValue"),
)
if mibBuilder.loadTexts:
    wwpLeosFlowL2SacEntry.setStatus("current")


class _WwpLeosFlowL2SacPortId_Type(Integer32):
    """Custom type wwpLeosFlowL2SacPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLeosFlowL2SacPortId_Type.__name__ = "Integer32"
_WwpLeosFlowL2SacPortId_Object = MibTableColumn
wwpLeosFlowL2SacPortId = _WwpLeosFlowL2SacPortId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 19, 1, 1),
    _WwpLeosFlowL2SacPortId_Type()
)
wwpLeosFlowL2SacPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowL2SacPortId.setStatus("current")


class _WwpLeosFlowL2SacNetType_Type(Integer32):
    """Custom type wwpLeosFlowL2SacNetType based on Integer32"""
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
        *(("none", 1),
          ("vlan", 2),
          ("vsiEth", 3),
          ("vsiMpls", 4))
    )


_WwpLeosFlowL2SacNetType_Type.__name__ = "Integer32"
_WwpLeosFlowL2SacNetType_Object = MibTableColumn
wwpLeosFlowL2SacNetType = _WwpLeosFlowL2SacNetType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 19, 1, 2),
    _WwpLeosFlowL2SacNetType_Type()
)
wwpLeosFlowL2SacNetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowL2SacNetType.setStatus("current")


class _WwpLeosFlowSacNetValue_Type(Integer32):
    """Custom type wwpLeosFlowSacNetValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosFlowSacNetValue_Type.__name__ = "Integer32"
_WwpLeosFlowSacNetValue_Object = MibTableColumn
wwpLeosFlowSacNetValue = _WwpLeosFlowSacNetValue_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 19, 1, 3),
    _WwpLeosFlowSacNetValue_Type()
)
wwpLeosFlowSacNetValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowSacNetValue.setStatus("current")


class _WwpLeosFlowL2SacLimit_Type(Integer32):
    """Custom type wwpLeosFlowL2SacLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WwpLeosFlowL2SacLimit_Type.__name__ = "Integer32"
_WwpLeosFlowL2SacLimit_Object = MibTableColumn
wwpLeosFlowL2SacLimit = _WwpLeosFlowL2SacLimit_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 19, 1, 4),
    _WwpLeosFlowL2SacLimit_Type()
)
wwpLeosFlowL2SacLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosFlowL2SacLimit.setStatus("current")
_WwpLeosFlowL2SacCurMac_Type = Counter32
_WwpLeosFlowL2SacCurMac_Object = MibTableColumn
wwpLeosFlowL2SacCurMac = _WwpLeosFlowL2SacCurMac_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 19, 1, 5),
    _WwpLeosFlowL2SacCurMac_Type()
)
wwpLeosFlowL2SacCurMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowL2SacCurMac.setStatus("current")
_WwpLeosFlowL2SacCurFilteredMac_Type = Counter32
_WwpLeosFlowL2SacCurFilteredMac_Object = MibTableColumn
wwpLeosFlowL2SacCurFilteredMac = _WwpLeosFlowL2SacCurFilteredMac_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 19, 1, 6),
    _WwpLeosFlowL2SacCurFilteredMac_Type()
)
wwpLeosFlowL2SacCurFilteredMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowL2SacCurFilteredMac.setStatus("current")


class _WwpLeosFlowL2SacOperState_Type(Integer32):
    """Custom type wwpLeosFlowL2SacOperState based on Integer32"""
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


_WwpLeosFlowL2SacOperState_Type.__name__ = "Integer32"
_WwpLeosFlowL2SacOperState_Object = MibTableColumn
wwpLeosFlowL2SacOperState = _WwpLeosFlowL2SacOperState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 19, 1, 7),
    _WwpLeosFlowL2SacOperState_Type()
)
wwpLeosFlowL2SacOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowL2SacOperState.setStatus("current")
_WwpLeosFlowL2SacRowStatus_Type = RowStatus
_WwpLeosFlowL2SacRowStatus_Object = MibTableColumn
wwpLeosFlowL2SacRowStatus = _WwpLeosFlowL2SacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 19, 1, 8),
    _WwpLeosFlowL2SacRowStatus_Type()
)
wwpLeosFlowL2SacRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosFlowL2SacRowStatus.setStatus("current")


class _WwpLeosFlowL2SacTrapState_Type(Integer32):
    """Custom type wwpLeosFlowL2SacTrapState based on Integer32"""
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


_WwpLeosFlowL2SacTrapState_Type.__name__ = "Integer32"
_WwpLeosFlowL2SacTrapState_Object = MibScalar
wwpLeosFlowL2SacTrapState = _WwpLeosFlowL2SacTrapState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 20),
    _WwpLeosFlowL2SacTrapState_Type()
)
wwpLeosFlowL2SacTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowL2SacTrapState.setStatus("current")


class _WwpLeosFlowStrictQueuingState_Type(Integer32):
    """Custom type wwpLeosFlowStrictQueuingState based on Integer32"""
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


_WwpLeosFlowStrictQueuingState_Type.__name__ = "Integer32"
_WwpLeosFlowStrictQueuingState_Object = MibScalar
wwpLeosFlowStrictQueuingState = _WwpLeosFlowStrictQueuingState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 21),
    _WwpLeosFlowStrictQueuingState_Type()
)
wwpLeosFlowStrictQueuingState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowStrictQueuingState.setStatus("current")


class _WwpLeosFlowBwCalcMode_Type(Integer32):
    """Custom type wwpLeosFlowBwCalcMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("payload", 2),
          ("transport", 1))
    )


_WwpLeosFlowBwCalcMode_Type.__name__ = "Integer32"
_WwpLeosFlowBwCalcMode_Object = MibScalar
wwpLeosFlowBwCalcMode = _WwpLeosFlowBwCalcMode_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 22),
    _WwpLeosFlowBwCalcMode_Type()
)
wwpLeosFlowBwCalcMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowBwCalcMode.setStatus("current")
_WwpLeosFlowGlobal_ObjectIdentity = ObjectIdentity
wwpLeosFlowGlobal = _WwpLeosFlowGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 23)
)


class _WwpLeosFlowServiceLevelFlowGroupState_Type(Integer32):
    """Custom type wwpLeosFlowServiceLevelFlowGroupState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_WwpLeosFlowServiceLevelFlowGroupState_Type.__name__ = "Integer32"
_WwpLeosFlowServiceLevelFlowGroupState_Object = MibScalar
wwpLeosFlowServiceLevelFlowGroupState = _WwpLeosFlowServiceLevelFlowGroupState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 23, 1),
    _WwpLeosFlowServiceLevelFlowGroupState_Type()
)
wwpLeosFlowServiceLevelFlowGroupState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowServiceLevelFlowGroupState.setStatus("current")


class _WwpLeosFlowServiceMappingCosRedMappingState_Type(Integer32):
    """Custom type wwpLeosFlowServiceMappingCosRedMappingState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_WwpLeosFlowServiceMappingCosRedMappingState_Type.__name__ = "Integer32"
_WwpLeosFlowServiceMappingCosRedMappingState_Object = MibScalar
wwpLeosFlowServiceMappingCosRedMappingState = _WwpLeosFlowServiceMappingCosRedMappingState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 23, 2),
    _WwpLeosFlowServiceMappingCosRedMappingState_Type()
)
wwpLeosFlowServiceMappingCosRedMappingState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowServiceMappingCosRedMappingState.setStatus("current")


class _WwpLeosFlowServiceAllRedCurveUnset_Type(TruthValue):
    """Custom type wwpLeosFlowServiceAllRedCurveUnset based on TruthValue"""


_WwpLeosFlowServiceAllRedCurveUnset_Object = MibScalar
wwpLeosFlowServiceAllRedCurveUnset = _WwpLeosFlowServiceAllRedCurveUnset_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 23, 3),
    _WwpLeosFlowServiceAllRedCurveUnset_Type()
)
wwpLeosFlowServiceAllRedCurveUnset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowServiceAllRedCurveUnset.setStatus("current")
_WwpLeosFlowServiceRedCurveTable_Object = MibTable
wwpLeosFlowServiceRedCurveTable = _WwpLeosFlowServiceRedCurveTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 24)
)
if mibBuilder.loadTexts:
    wwpLeosFlowServiceRedCurveTable.setStatus("current")
_WwpLeosFlowServiceRedCurveEntry_Object = MibTableRow
wwpLeosFlowServiceRedCurveEntry = _WwpLeosFlowServiceRedCurveEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 24, 1)
)
wwpLeosFlowServiceRedCurveEntry.setIndexNames(
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowServiceRedCurveIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosFlowServiceRedCurveEntry.setStatus("current")


class _WwpLeosFlowServiceRedCurveIndex_Type(Unsigned32):
    """Custom type wwpLeosFlowServiceRedCurveIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 64),
    )


_WwpLeosFlowServiceRedCurveIndex_Type.__name__ = "Unsigned32"
_WwpLeosFlowServiceRedCurveIndex_Object = MibTableColumn
wwpLeosFlowServiceRedCurveIndex = _WwpLeosFlowServiceRedCurveIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 24, 1, 1),
    _WwpLeosFlowServiceRedCurveIndex_Type()
)
wwpLeosFlowServiceRedCurveIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowServiceRedCurveIndex.setStatus("current")


class _WwpLeosFlowServiceRedCurveName_Type(DisplayString):
    """Custom type wwpLeosFlowServiceRedCurveName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_WwpLeosFlowServiceRedCurveName_Type.__name__ = "DisplayString"
_WwpLeosFlowServiceRedCurveName_Object = MibTableColumn
wwpLeosFlowServiceRedCurveName = _WwpLeosFlowServiceRedCurveName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 24, 1, 2),
    _WwpLeosFlowServiceRedCurveName_Type()
)
wwpLeosFlowServiceRedCurveName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowServiceRedCurveName.setStatus("current")


class _WwpLeosFlowServiceRedCurveState_Type(Integer32):
    """Custom type wwpLeosFlowServiceRedCurveState based on Integer32"""
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


_WwpLeosFlowServiceRedCurveState_Type.__name__ = "Integer32"
_WwpLeosFlowServiceRedCurveState_Object = MibTableColumn
wwpLeosFlowServiceRedCurveState = _WwpLeosFlowServiceRedCurveState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 24, 1, 3),
    _WwpLeosFlowServiceRedCurveState_Type()
)
wwpLeosFlowServiceRedCurveState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowServiceRedCurveState.setStatus("current")


class _WwpLeosFlowServiceRedCurveMinThreshold_Type(Unsigned32):
    """Custom type wwpLeosFlowServiceRedCurveMinThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLeosFlowServiceRedCurveMinThreshold_Type.__name__ = "Unsigned32"
_WwpLeosFlowServiceRedCurveMinThreshold_Object = MibTableColumn
wwpLeosFlowServiceRedCurveMinThreshold = _WwpLeosFlowServiceRedCurveMinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 24, 1, 4),
    _WwpLeosFlowServiceRedCurveMinThreshold_Type()
)
wwpLeosFlowServiceRedCurveMinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowServiceRedCurveMinThreshold.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosFlowServiceRedCurveMinThreshold.setUnits("kbps")


class _WwpLeosFlowServiceRedCurveMaxThreshold_Type(Unsigned32):
    """Custom type wwpLeosFlowServiceRedCurveMaxThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLeosFlowServiceRedCurveMaxThreshold_Type.__name__ = "Unsigned32"
_WwpLeosFlowServiceRedCurveMaxThreshold_Object = MibTableColumn
wwpLeosFlowServiceRedCurveMaxThreshold = _WwpLeosFlowServiceRedCurveMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 24, 1, 5),
    _WwpLeosFlowServiceRedCurveMaxThreshold_Type()
)
wwpLeosFlowServiceRedCurveMaxThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowServiceRedCurveMaxThreshold.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosFlowServiceRedCurveMaxThreshold.setUnits("kbps")


class _WwpLeosFlowServiceRedCurveDropProbability_Type(Unsigned32):
    """Custom type wwpLeosFlowServiceRedCurveDropProbability based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_WwpLeosFlowServiceRedCurveDropProbability_Type.__name__ = "Unsigned32"
_WwpLeosFlowServiceRedCurveDropProbability_Object = MibTableColumn
wwpLeosFlowServiceRedCurveDropProbability = _WwpLeosFlowServiceRedCurveDropProbability_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 24, 1, 6),
    _WwpLeosFlowServiceRedCurveDropProbability_Type()
)
wwpLeosFlowServiceRedCurveDropProbability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowServiceRedCurveDropProbability.setStatus("current")


class _WwpLeosFlowServiceRedCurveUnset_Type(TruthValue):
    """Custom type wwpLeosFlowServiceRedCurveUnset based on TruthValue"""


_WwpLeosFlowServiceRedCurveUnset_Object = MibTableColumn
wwpLeosFlowServiceRedCurveUnset = _WwpLeosFlowServiceRedCurveUnset_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 24, 1, 7),
    _WwpLeosFlowServiceRedCurveUnset_Type()
)
wwpLeosFlowServiceRedCurveUnset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowServiceRedCurveUnset.setStatus("current")
_WwpLeosFlowCos1dToRedCurveOffsetTable_Object = MibTable
wwpLeosFlowCos1dToRedCurveOffsetTable = _WwpLeosFlowCos1dToRedCurveOffsetTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 25)
)
if mibBuilder.loadTexts:
    wwpLeosFlowCos1dToRedCurveOffsetTable.setStatus("current")
_WwpLeosFlowCos1dToRedCurveOffsetEntry_Object = MibTableRow
wwpLeosFlowCos1dToRedCurveOffsetEntry = _WwpLeosFlowCos1dToRedCurveOffsetEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 25, 1)
)
wwpLeosFlowCos1dToRedCurveOffsetEntry.setIndexNames(
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowCos1dToRedCurveOffset1dValue"),
)
if mibBuilder.loadTexts:
    wwpLeosFlowCos1dToRedCurveOffsetEntry.setStatus("current")


class _WwpLeosFlowCos1dToRedCurveOffset1dValue_Type(Unsigned32):
    """Custom type wwpLeosFlowCos1dToRedCurveOffset1dValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosFlowCos1dToRedCurveOffset1dValue_Type.__name__ = "Unsigned32"
_WwpLeosFlowCos1dToRedCurveOffset1dValue_Object = MibTableColumn
wwpLeosFlowCos1dToRedCurveOffset1dValue = _WwpLeosFlowCos1dToRedCurveOffset1dValue_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 25, 1, 1),
    _WwpLeosFlowCos1dToRedCurveOffset1dValue_Type()
)
wwpLeosFlowCos1dToRedCurveOffset1dValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCos1dToRedCurveOffset1dValue.setStatus("current")


class _WwpLeosFlowCos1dToRedCurveOffsetValue_Type(Unsigned32):
    """Custom type wwpLeosFlowCos1dToRedCurveOffsetValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_WwpLeosFlowCos1dToRedCurveOffsetValue_Type.__name__ = "Unsigned32"
_WwpLeosFlowCos1dToRedCurveOffsetValue_Object = MibTableColumn
wwpLeosFlowCos1dToRedCurveOffsetValue = _WwpLeosFlowCos1dToRedCurveOffsetValue_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 25, 1, 2),
    _WwpLeosFlowCos1dToRedCurveOffsetValue_Type()
)
wwpLeosFlowCos1dToRedCurveOffsetValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowCos1dToRedCurveOffsetValue.setStatus("current")
_WwpLeosFlowCosMapPCPTo1dTable_Object = MibTable
wwpLeosFlowCosMapPCPTo1dTable = _WwpLeosFlowCosMapPCPTo1dTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 26)
)
if mibBuilder.loadTexts:
    wwpLeosFlowCosMapPCPTo1dTable.setStatus("current")
_WwpLeosFlowCosMapPCPTo1dEntry_Object = MibTableRow
wwpLeosFlowCosMapPCPTo1dEntry = _WwpLeosFlowCosMapPCPTo1dEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 26, 1)
)
wwpLeosFlowCosMapPCPTo1dEntry.setIndexNames(
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowCosMapPCPTo1dMapFrom"),
)
if mibBuilder.loadTexts:
    wwpLeosFlowCosMapPCPTo1dEntry.setStatus("current")


class _WwpLeosFlowCosMapPCPTo1dMapFrom_Type(Integer32):
    """Custom type wwpLeosFlowCosMapPCPTo1dMapFrom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosFlowCosMapPCPTo1dMapFrom_Type.__name__ = "Integer32"
_WwpLeosFlowCosMapPCPTo1dMapFrom_Object = MibTableColumn
wwpLeosFlowCosMapPCPTo1dMapFrom = _WwpLeosFlowCosMapPCPTo1dMapFrom_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 26, 1, 1),
    _WwpLeosFlowCosMapPCPTo1dMapFrom_Type()
)
wwpLeosFlowCosMapPCPTo1dMapFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCosMapPCPTo1dMapFrom.setStatus("current")


class _WwpLeosFlowCosMapPCPTo1dMapTo_Type(Integer32):
    """Custom type wwpLeosFlowCosMapPCPTo1dMapTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosFlowCosMapPCPTo1dMapTo_Type.__name__ = "Integer32"
_WwpLeosFlowCosMapPCPTo1dMapTo_Object = MibTableColumn
wwpLeosFlowCosMapPCPTo1dMapTo = _WwpLeosFlowCosMapPCPTo1dMapTo_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 26, 1, 2),
    _WwpLeosFlowCosMapPCPTo1dMapTo_Type()
)
wwpLeosFlowCosMapPCPTo1dMapTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowCosMapPCPTo1dMapTo.setStatus("current")
_WwpLeosFlowCosMap1dToPCPTable_Object = MibTable
wwpLeosFlowCosMap1dToPCPTable = _WwpLeosFlowCosMap1dToPCPTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 27)
)
if mibBuilder.loadTexts:
    wwpLeosFlowCosMap1dToPCPTable.setStatus("current")
_WwpLeosFlowCosMap1dToPCPEntry_Object = MibTableRow
wwpLeosFlowCosMap1dToPCPEntry = _WwpLeosFlowCosMap1dToPCPEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 27, 1)
)
wwpLeosFlowCosMap1dToPCPEntry.setIndexNames(
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowCosMap1dToPCPMapFrom"),
)
if mibBuilder.loadTexts:
    wwpLeosFlowCosMap1dToPCPEntry.setStatus("current")


class _WwpLeosFlowCosMap1dToPCPMapFrom_Type(Integer32):
    """Custom type wwpLeosFlowCosMap1dToPCPMapFrom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosFlowCosMap1dToPCPMapFrom_Type.__name__ = "Integer32"
_WwpLeosFlowCosMap1dToPCPMapFrom_Object = MibTableColumn
wwpLeosFlowCosMap1dToPCPMapFrom = _WwpLeosFlowCosMap1dToPCPMapFrom_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 27, 1, 1),
    _WwpLeosFlowCosMap1dToPCPMapFrom_Type()
)
wwpLeosFlowCosMap1dToPCPMapFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCosMap1dToPCPMapFrom.setStatus("current")


class _WwpLeosFlowCosMap1dToPCPMapTo_Type(Integer32):
    """Custom type wwpLeosFlowCosMap1dToPCPMapTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosFlowCosMap1dToPCPMapTo_Type.__name__ = "Integer32"
_WwpLeosFlowCosMap1dToPCPMapTo_Object = MibTableColumn
wwpLeosFlowCosMap1dToPCPMapTo = _WwpLeosFlowCosMap1dToPCPMapTo_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 27, 1, 2),
    _WwpLeosFlowCosMap1dToPCPMapTo_Type()
)
wwpLeosFlowCosMap1dToPCPMapTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowCosMap1dToPCPMapTo.setStatus("current")


class _WwpLeosFlowMacMotionEventsEnable_Type(Integer32):
    """Custom type wwpLeosFlowMacMotionEventsEnable based on Integer32"""
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


_WwpLeosFlowMacMotionEventsEnable_Type.__name__ = "Integer32"
_WwpLeosFlowMacMotionEventsEnable_Object = MibScalar
wwpLeosFlowMacMotionEventsEnable = _WwpLeosFlowMacMotionEventsEnable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 28),
    _WwpLeosFlowMacMotionEventsEnable_Type()
)
wwpLeosFlowMacMotionEventsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowMacMotionEventsEnable.setStatus("current")


class _WwpLeosFlowMacMotionEventsInterval_Type(Integer32):
    """Custom type wwpLeosFlowMacMotionEventsInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 300),
    )


_WwpLeosFlowMacMotionEventsInterval_Type.__name__ = "Integer32"
_WwpLeosFlowMacMotionEventsInterval_Object = MibScalar
wwpLeosFlowMacMotionEventsInterval = _WwpLeosFlowMacMotionEventsInterval_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 29),
    _WwpLeosFlowMacMotionEventsInterval_Type()
)
wwpLeosFlowMacMotionEventsInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowMacMotionEventsInterval.setStatus("current")


class _WwpLeosFlowCpuRateLimitsEnable_Type(Integer32):
    """Custom type wwpLeosFlowCpuRateLimitsEnable based on Integer32"""
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


_WwpLeosFlowCpuRateLimitsEnable_Type.__name__ = "Integer32"
_WwpLeosFlowCpuRateLimitsEnable_Object = MibScalar
wwpLeosFlowCpuRateLimitsEnable = _WwpLeosFlowCpuRateLimitsEnable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 30),
    _WwpLeosFlowCpuRateLimitsEnable_Type()
)
wwpLeosFlowCpuRateLimitsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitsEnable.setStatus("current")
_WwpLeosFlowCpuRateLimitTable_Object = MibTable
wwpLeosFlowCpuRateLimitTable = _WwpLeosFlowCpuRateLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 31)
)
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitTable.setStatus("current")
_WwpLeosFlowCpuRateLimitEntry_Object = MibTableRow
wwpLeosFlowCpuRateLimitEntry = _WwpLeosFlowCpuRateLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 31, 1)
)
wwpLeosFlowCpuRateLimitEntry.setIndexNames(
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowCpuRateLimitPort"),
)
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitEntry.setStatus("current")


class _WwpLeosFlowCpuRateLimitPort_Type(Integer32):
    """Custom type wwpLeosFlowCpuRateLimitPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_WwpLeosFlowCpuRateLimitPort_Type.__name__ = "Integer32"
_WwpLeosFlowCpuRateLimitPort_Object = MibTableColumn
wwpLeosFlowCpuRateLimitPort = _WwpLeosFlowCpuRateLimitPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 31, 1, 1),
    _WwpLeosFlowCpuRateLimitPort_Type()
)
wwpLeosFlowCpuRateLimitPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitPort.setStatus("current")


class _WwpLeosFlowCpuRateLimitEnable_Type(Integer32):
    """Custom type wwpLeosFlowCpuRateLimitEnable based on Integer32"""
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


_WwpLeosFlowCpuRateLimitEnable_Type.__name__ = "Integer32"
_WwpLeosFlowCpuRateLimitEnable_Object = MibTableColumn
wwpLeosFlowCpuRateLimitEnable = _WwpLeosFlowCpuRateLimitEnable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 31, 1, 2),
    _WwpLeosFlowCpuRateLimitEnable_Type()
)
wwpLeosFlowCpuRateLimitEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitEnable.setStatus("current")


class _WwpLeosFlowCpuRateLimitBootp_Type(Integer32):
    """Custom type wwpLeosFlowCpuRateLimitBootp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2500),
    )


_WwpLeosFlowCpuRateLimitBootp_Type.__name__ = "Integer32"
_WwpLeosFlowCpuRateLimitBootp_Object = MibTableColumn
wwpLeosFlowCpuRateLimitBootp = _WwpLeosFlowCpuRateLimitBootp_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 31, 1, 3),
    _WwpLeosFlowCpuRateLimitBootp_Type()
)
wwpLeosFlowCpuRateLimitBootp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitBootp.setStatus("current")


class _WwpLeosFlowCpuRateLimitCfm_Type(Integer32):
    """Custom type wwpLeosFlowCpuRateLimitCfm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2500),
    )


_WwpLeosFlowCpuRateLimitCfm_Type.__name__ = "Integer32"
_WwpLeosFlowCpuRateLimitCfm_Object = MibTableColumn
wwpLeosFlowCpuRateLimitCfm = _WwpLeosFlowCpuRateLimitCfm_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 31, 1, 4),
    _WwpLeosFlowCpuRateLimitCfm_Type()
)
wwpLeosFlowCpuRateLimitCfm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitCfm.setStatus("current")


class _WwpLeosFlowCpuRateLimitCft_Type(Integer32):
    """Custom type wwpLeosFlowCpuRateLimitCft based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2500),
    )


_WwpLeosFlowCpuRateLimitCft_Type.__name__ = "Integer32"
_WwpLeosFlowCpuRateLimitCft_Object = MibTableColumn
wwpLeosFlowCpuRateLimitCft = _WwpLeosFlowCpuRateLimitCft_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 31, 1, 5),
    _WwpLeosFlowCpuRateLimitCft_Type()
)
wwpLeosFlowCpuRateLimitCft.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitCft.setStatus("current")


class _WwpLeosFlowCpuRateLimitDot1x_Type(Integer32):
    """Custom type wwpLeosFlowCpuRateLimitDot1x based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2500),
    )


_WwpLeosFlowCpuRateLimitDot1x_Type.__name__ = "Integer32"
_WwpLeosFlowCpuRateLimitDot1x_Object = MibTableColumn
wwpLeosFlowCpuRateLimitDot1x = _WwpLeosFlowCpuRateLimitDot1x_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 31, 1, 6),
    _WwpLeosFlowCpuRateLimitDot1x_Type()
)
wwpLeosFlowCpuRateLimitDot1x.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitDot1x.setStatus("current")


class _WwpLeosFlowCpuRateLimitOam_Type(Integer32):
    """Custom type wwpLeosFlowCpuRateLimitOam based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2500),
    )


_WwpLeosFlowCpuRateLimitOam_Type.__name__ = "Integer32"
_WwpLeosFlowCpuRateLimitOam_Object = MibTableColumn
wwpLeosFlowCpuRateLimitOam = _WwpLeosFlowCpuRateLimitOam_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 31, 1, 7),
    _WwpLeosFlowCpuRateLimitOam_Type()
)
wwpLeosFlowCpuRateLimitOam.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitOam.setStatus("current")


class _WwpLeosFlowCpuRateLimitEprArp_Type(Integer32):
    """Custom type wwpLeosFlowCpuRateLimitEprArp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2500),
    )


_WwpLeosFlowCpuRateLimitEprArp_Type.__name__ = "Integer32"
_WwpLeosFlowCpuRateLimitEprArp_Object = MibTableColumn
wwpLeosFlowCpuRateLimitEprArp = _WwpLeosFlowCpuRateLimitEprArp_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 31, 1, 8),
    _WwpLeosFlowCpuRateLimitEprArp_Type()
)
wwpLeosFlowCpuRateLimitEprArp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitEprArp.setStatus("current")


class _WwpLeosFlowCpuRateLimitIgmp_Type(Integer32):
    """Custom type wwpLeosFlowCpuRateLimitIgmp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2500),
    )


_WwpLeosFlowCpuRateLimitIgmp_Type.__name__ = "Integer32"
_WwpLeosFlowCpuRateLimitIgmp_Object = MibTableColumn
wwpLeosFlowCpuRateLimitIgmp = _WwpLeosFlowCpuRateLimitIgmp_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 31, 1, 9),
    _WwpLeosFlowCpuRateLimitIgmp_Type()
)
wwpLeosFlowCpuRateLimitIgmp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitIgmp.setStatus("current")


class _WwpLeosFlowCpuRateLimitInet_Type(Integer32):
    """Custom type wwpLeosFlowCpuRateLimitInet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_WwpLeosFlowCpuRateLimitInet_Type.__name__ = "Integer32"
_WwpLeosFlowCpuRateLimitInet_Object = MibTableColumn
wwpLeosFlowCpuRateLimitInet = _WwpLeosFlowCpuRateLimitInet_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 31, 1, 10),
    _WwpLeosFlowCpuRateLimitInet_Type()
)
wwpLeosFlowCpuRateLimitInet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitInet.setStatus("current")


class _WwpLeosFlowCpuRateLimitLacp_Type(Integer32):
    """Custom type wwpLeosFlowCpuRateLimitLacp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2500),
    )


_WwpLeosFlowCpuRateLimitLacp_Type.__name__ = "Integer32"
_WwpLeosFlowCpuRateLimitLacp_Object = MibTableColumn
wwpLeosFlowCpuRateLimitLacp = _WwpLeosFlowCpuRateLimitLacp_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 31, 1, 11),
    _WwpLeosFlowCpuRateLimitLacp_Type()
)
wwpLeosFlowCpuRateLimitLacp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitLacp.setStatus("current")


class _WwpLeosFlowCpuRateLimitLldp_Type(Integer32):
    """Custom type wwpLeosFlowCpuRateLimitLldp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2500),
    )


_WwpLeosFlowCpuRateLimitLldp_Type.__name__ = "Integer32"
_WwpLeosFlowCpuRateLimitLldp_Object = MibTableColumn
wwpLeosFlowCpuRateLimitLldp = _WwpLeosFlowCpuRateLimitLldp_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 31, 1, 12),
    _WwpLeosFlowCpuRateLimitLldp_Type()
)
wwpLeosFlowCpuRateLimitLldp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitLldp.setStatus("current")


class _WwpLeosFlowCpuRateLimitMpls_Type(Integer32):
    """Custom type wwpLeosFlowCpuRateLimitMpls based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2500),
    )


_WwpLeosFlowCpuRateLimitMpls_Type.__name__ = "Integer32"
_WwpLeosFlowCpuRateLimitMpls_Object = MibTableColumn
wwpLeosFlowCpuRateLimitMpls = _WwpLeosFlowCpuRateLimitMpls_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 31, 1, 13),
    _WwpLeosFlowCpuRateLimitMpls_Type()
)
wwpLeosFlowCpuRateLimitMpls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitMpls.setStatus("current")


class _WwpLeosFlowCpuRateLimitMstp_Type(Integer32):
    """Custom type wwpLeosFlowCpuRateLimitMstp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_WwpLeosFlowCpuRateLimitMstp_Type.__name__ = "Integer32"
_WwpLeosFlowCpuRateLimitMstp_Object = MibTableColumn
wwpLeosFlowCpuRateLimitMstp = _WwpLeosFlowCpuRateLimitMstp_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 31, 1, 14),
    _WwpLeosFlowCpuRateLimitMstp_Type()
)
wwpLeosFlowCpuRateLimitMstp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitMstp.setStatus("current")


class _WwpLeosFlowCpuRateLimitPeArp_Type(Integer32):
    """Custom type wwpLeosFlowCpuRateLimitPeArp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2500),
    )


_WwpLeosFlowCpuRateLimitPeArp_Type.__name__ = "Integer32"
_WwpLeosFlowCpuRateLimitPeArp_Object = MibTableColumn
wwpLeosFlowCpuRateLimitPeArp = _WwpLeosFlowCpuRateLimitPeArp_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 31, 1, 15),
    _WwpLeosFlowCpuRateLimitPeArp_Type()
)
wwpLeosFlowCpuRateLimitPeArp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitPeArp.setStatus("current")


class _WwpLeosFlowCpuRateLimitPvst_Type(Integer32):
    """Custom type wwpLeosFlowCpuRateLimitPvst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2500),
    )


_WwpLeosFlowCpuRateLimitPvst_Type.__name__ = "Integer32"
_WwpLeosFlowCpuRateLimitPvst_Object = MibTableColumn
wwpLeosFlowCpuRateLimitPvst = _WwpLeosFlowCpuRateLimitPvst_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 31, 1, 16),
    _WwpLeosFlowCpuRateLimitPvst_Type()
)
wwpLeosFlowCpuRateLimitPvst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitPvst.setStatus("current")


class _WwpLeosFlowCpuRateLimitRstp_Type(Integer32):
    """Custom type wwpLeosFlowCpuRateLimitRstp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2500),
    )


_WwpLeosFlowCpuRateLimitRstp_Type.__name__ = "Integer32"
_WwpLeosFlowCpuRateLimitRstp_Object = MibTableColumn
wwpLeosFlowCpuRateLimitRstp = _WwpLeosFlowCpuRateLimitRstp_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 31, 1, 17),
    _WwpLeosFlowCpuRateLimitRstp_Type()
)
wwpLeosFlowCpuRateLimitRstp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitRstp.setStatus("current")


class _WwpLeosFlowCpuRateLimitLpbk_Type(Integer32):
    """Custom type wwpLeosFlowCpuRateLimitLpbk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2500),
    )


_WwpLeosFlowCpuRateLimitLpbk_Type.__name__ = "Integer32"
_WwpLeosFlowCpuRateLimitLpbk_Object = MibTableColumn
wwpLeosFlowCpuRateLimitLpbk = _WwpLeosFlowCpuRateLimitLpbk_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 31, 1, 18),
    _WwpLeosFlowCpuRateLimitLpbk_Type()
)
wwpLeosFlowCpuRateLimitLpbk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitLpbk.setStatus("current")


class _WwpLeosFlowCpuRateLimitRmtLpbk_Type(Integer32):
    """Custom type wwpLeosFlowCpuRateLimitRmtLpbk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2500),
    )


_WwpLeosFlowCpuRateLimitRmtLpbk_Type.__name__ = "Integer32"
_WwpLeosFlowCpuRateLimitRmtLpbk_Object = MibTableColumn
wwpLeosFlowCpuRateLimitRmtLpbk = _WwpLeosFlowCpuRateLimitRmtLpbk_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 31, 1, 19),
    _WwpLeosFlowCpuRateLimitRmtLpbk_Type()
)
wwpLeosFlowCpuRateLimitRmtLpbk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitRmtLpbk.setStatus("current")


class _WwpLeosFlowCpuRateLimitCxeRx_Type(Integer32):
    """Custom type wwpLeosFlowCpuRateLimitCxeRx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_WwpLeosFlowCpuRateLimitCxeRx_Type.__name__ = "Integer32"
_WwpLeosFlowCpuRateLimitCxeRx_Object = MibTableColumn
wwpLeosFlowCpuRateLimitCxeRx = _WwpLeosFlowCpuRateLimitCxeRx_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 31, 1, 20),
    _WwpLeosFlowCpuRateLimitCxeRx_Type()
)
wwpLeosFlowCpuRateLimitCxeRx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitCxeRx.setStatus("current")


class _WwpLeosFlowCpuRateLimitCxeTx_Type(Integer32):
    """Custom type wwpLeosFlowCpuRateLimitCxeTx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_WwpLeosFlowCpuRateLimitCxeTx_Type.__name__ = "Integer32"
_WwpLeosFlowCpuRateLimitCxeTx_Object = MibTableColumn
wwpLeosFlowCpuRateLimitCxeTx = _WwpLeosFlowCpuRateLimitCxeTx_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 31, 1, 21),
    _WwpLeosFlowCpuRateLimitCxeTx_Type()
)
wwpLeosFlowCpuRateLimitCxeTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitCxeTx.setStatus("current")


class _WwpLeosFlowCpuRateLimitTwamp_Type(Integer32):
    """Custom type wwpLeosFlowCpuRateLimitTwamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2500),
    )


_WwpLeosFlowCpuRateLimitTwamp_Type.__name__ = "Integer32"
_WwpLeosFlowCpuRateLimitTwamp_Object = MibTableColumn
wwpLeosFlowCpuRateLimitTwamp = _WwpLeosFlowCpuRateLimitTwamp_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 31, 1, 22),
    _WwpLeosFlowCpuRateLimitTwamp_Type()
)
wwpLeosFlowCpuRateLimitTwamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitTwamp.setStatus("current")


class _WwpLeosFlowCpuRateLimitDflt_Type(Integer32):
    """Custom type wwpLeosFlowCpuRateLimitDflt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_WwpLeosFlowCpuRateLimitDflt_Type.__name__ = "Integer32"
_WwpLeosFlowCpuRateLimitDflt_Object = MibTableColumn
wwpLeosFlowCpuRateLimitDflt = _WwpLeosFlowCpuRateLimitDflt_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 31, 1, 23),
    _WwpLeosFlowCpuRateLimitDflt_Type()
)
wwpLeosFlowCpuRateLimitDflt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitDflt.setStatus("current")


class _WwpLeosFlowCpuRateLimitTwampRsp_Type(Integer32):
    """Custom type wwpLeosFlowCpuRateLimitTwampRsp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2500),
    )


_WwpLeosFlowCpuRateLimitTwampRsp_Type.__name__ = "Integer32"
_WwpLeosFlowCpuRateLimitTwampRsp_Object = MibTableColumn
wwpLeosFlowCpuRateLimitTwampRsp = _WwpLeosFlowCpuRateLimitTwampRsp_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 31, 1, 24),
    _WwpLeosFlowCpuRateLimitTwampRsp_Type()
)
wwpLeosFlowCpuRateLimitTwampRsp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitTwampRsp.setStatus("current")


class _WwpLeosFlowCpuRateLimitMultiCast_Type(Integer32):
    """Custom type wwpLeosFlowCpuRateLimitMultiCast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_WwpLeosFlowCpuRateLimitMultiCast_Type.__name__ = "Integer32"
_WwpLeosFlowCpuRateLimitMultiCast_Object = MibTableColumn
wwpLeosFlowCpuRateLimitMultiCast = _WwpLeosFlowCpuRateLimitMultiCast_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 31, 1, 25),
    _WwpLeosFlowCpuRateLimitMultiCast_Type()
)
wwpLeosFlowCpuRateLimitMultiCast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitMultiCast.setStatus("current")


class _WwpLeosFlowCpuRateLimitBroadCast_Type(Integer32):
    """Custom type wwpLeosFlowCpuRateLimitBroadCast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_WwpLeosFlowCpuRateLimitBroadCast_Type.__name__ = "Integer32"
_WwpLeosFlowCpuRateLimitBroadCast_Object = MibTableColumn
wwpLeosFlowCpuRateLimitBroadCast = _WwpLeosFlowCpuRateLimitBroadCast_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 31, 1, 26),
    _WwpLeosFlowCpuRateLimitBroadCast_Type()
)
wwpLeosFlowCpuRateLimitBroadCast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitBroadCast.setStatus("current")


class _WwpLeosFlowCpuRateLimitArp_Type(Integer32):
    """Custom type wwpLeosFlowCpuRateLimitArp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_WwpLeosFlowCpuRateLimitArp_Type.__name__ = "Integer32"
_WwpLeosFlowCpuRateLimitArp_Object = MibTableColumn
wwpLeosFlowCpuRateLimitArp = _WwpLeosFlowCpuRateLimitArp_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 31, 1, 27),
    _WwpLeosFlowCpuRateLimitArp_Type()
)
wwpLeosFlowCpuRateLimitArp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitArp.setStatus("current")


class _WwpLeosFlowCpuRateLimitIcmp_Type(Integer32):
    """Custom type wwpLeosFlowCpuRateLimitIcmp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_WwpLeosFlowCpuRateLimitIcmp_Type.__name__ = "Integer32"
_WwpLeosFlowCpuRateLimitIcmp_Object = MibTableColumn
wwpLeosFlowCpuRateLimitIcmp = _WwpLeosFlowCpuRateLimitIcmp_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 31, 1, 28),
    _WwpLeosFlowCpuRateLimitIcmp_Type()
)
wwpLeosFlowCpuRateLimitIcmp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitIcmp.setStatus("current")


class _WwpLeosFlowCpuRateLimitTcpSyn_Type(Integer32):
    """Custom type wwpLeosFlowCpuRateLimitTcpSyn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_WwpLeosFlowCpuRateLimitTcpSyn_Type.__name__ = "Integer32"
_WwpLeosFlowCpuRateLimitTcpSyn_Object = MibTableColumn
wwpLeosFlowCpuRateLimitTcpSyn = _WwpLeosFlowCpuRateLimitTcpSyn_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 31, 1, 29),
    _WwpLeosFlowCpuRateLimitTcpSyn_Type()
)
wwpLeosFlowCpuRateLimitTcpSyn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitTcpSyn.setStatus("current")


class _WwpLeosFlowCpuRateLimitRaps_Type(Integer32):
    """Custom type wwpLeosFlowCpuRateLimitRaps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2500),
    )


_WwpLeosFlowCpuRateLimitRaps_Type.__name__ = "Integer32"
_WwpLeosFlowCpuRateLimitRaps_Object = MibTableColumn
wwpLeosFlowCpuRateLimitRaps = _WwpLeosFlowCpuRateLimitRaps_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 31, 1, 30),
    _WwpLeosFlowCpuRateLimitRaps_Type()
)
wwpLeosFlowCpuRateLimitRaps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitRaps.setStatus("current")


class _WwpLeosFlowCpuRateLimitIpMgmt_Type(Integer32):
    """Custom type wwpLeosFlowCpuRateLimitIpMgmt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_WwpLeosFlowCpuRateLimitIpMgmt_Type.__name__ = "Integer32"
_WwpLeosFlowCpuRateLimitIpMgmt_Object = MibTableColumn
wwpLeosFlowCpuRateLimitIpMgmt = _WwpLeosFlowCpuRateLimitIpMgmt_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 31, 1, 31),
    _WwpLeosFlowCpuRateLimitIpMgmt_Type()
)
wwpLeosFlowCpuRateLimitIpMgmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitIpMgmt.setStatus("current")


class _WwpLeosFlowCpuRateLimitIpControl_Type(Integer32):
    """Custom type wwpLeosFlowCpuRateLimitIpControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_WwpLeosFlowCpuRateLimitIpControl_Type.__name__ = "Integer32"
_WwpLeosFlowCpuRateLimitIpControl_Object = MibTableColumn
wwpLeosFlowCpuRateLimitIpControl = _WwpLeosFlowCpuRateLimitIpControl_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 31, 1, 32),
    _WwpLeosFlowCpuRateLimitIpControl_Type()
)
wwpLeosFlowCpuRateLimitIpControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitIpControl.setStatus("current")


class _WwpLeosFlowCpuRateLimitIpV6Mgmt_Type(Integer32):
    """Custom type wwpLeosFlowCpuRateLimitIpV6Mgmt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_WwpLeosFlowCpuRateLimitIpV6Mgmt_Type.__name__ = "Integer32"
_WwpLeosFlowCpuRateLimitIpV6Mgmt_Object = MibTableColumn
wwpLeosFlowCpuRateLimitIpV6Mgmt = _WwpLeosFlowCpuRateLimitIpV6Mgmt_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 31, 1, 33),
    _WwpLeosFlowCpuRateLimitIpV6Mgmt_Type()
)
wwpLeosFlowCpuRateLimitIpV6Mgmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitIpV6Mgmt.setStatus("current")


class _WwpLeosFlowCpuRateLimitInet6_Type(Integer32):
    """Custom type wwpLeosFlowCpuRateLimitInet6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_WwpLeosFlowCpuRateLimitInet6_Type.__name__ = "Integer32"
_WwpLeosFlowCpuRateLimitInet6_Object = MibTableColumn
wwpLeosFlowCpuRateLimitInet6 = _WwpLeosFlowCpuRateLimitInet6_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 31, 1, 34),
    _WwpLeosFlowCpuRateLimitInet6_Type()
)
wwpLeosFlowCpuRateLimitInet6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitInet6.setStatus("current")
_WwpLeosFlowCpuRateLimitStatsTable_Object = MibTable
wwpLeosFlowCpuRateLimitStatsTable = _WwpLeosFlowCpuRateLimitStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 32)
)
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsTable.setStatus("current")
_WwpLeosFlowCpuRateLimitStatsEntry_Object = MibTableRow
wwpLeosFlowCpuRateLimitStatsEntry = _WwpLeosFlowCpuRateLimitStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 32, 1)
)
wwpLeosFlowCpuRateLimitStatsEntry.setIndexNames(
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowCpuRateLimitStatsPort"),
)
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsEntry.setStatus("current")


class _WwpLeosFlowCpuRateLimitStatsPort_Type(Integer32):
    """Custom type wwpLeosFlowCpuRateLimitStatsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_WwpLeosFlowCpuRateLimitStatsPort_Type.__name__ = "Integer32"
_WwpLeosFlowCpuRateLimitStatsPort_Object = MibTableColumn
wwpLeosFlowCpuRateLimitStatsPort = _WwpLeosFlowCpuRateLimitStatsPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 32, 1, 1),
    _WwpLeosFlowCpuRateLimitStatsPort_Type()
)
wwpLeosFlowCpuRateLimitStatsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsPort.setStatus("current")
_WwpLeosFlowCpuRateLimitStatsBootpPassed_Type = Gauge32
_WwpLeosFlowCpuRateLimitStatsBootpPassed_Object = MibTableColumn
wwpLeosFlowCpuRateLimitStatsBootpPassed = _WwpLeosFlowCpuRateLimitStatsBootpPassed_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 32, 1, 2),
    _WwpLeosFlowCpuRateLimitStatsBootpPassed_Type()
)
wwpLeosFlowCpuRateLimitStatsBootpPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsBootpPassed.setStatus("current")
_WwpLeosFlowCpuRateLimitStatsCfmPassed_Type = Gauge32
_WwpLeosFlowCpuRateLimitStatsCfmPassed_Object = MibTableColumn
wwpLeosFlowCpuRateLimitStatsCfmPassed = _WwpLeosFlowCpuRateLimitStatsCfmPassed_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 32, 1, 3),
    _WwpLeosFlowCpuRateLimitStatsCfmPassed_Type()
)
wwpLeosFlowCpuRateLimitStatsCfmPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsCfmPassed.setStatus("current")
_WwpLeosFlowCpuRateLimitStatsCftPassed_Type = Gauge32
_WwpLeosFlowCpuRateLimitStatsCftPassed_Object = MibTableColumn
wwpLeosFlowCpuRateLimitStatsCftPassed = _WwpLeosFlowCpuRateLimitStatsCftPassed_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 32, 1, 4),
    _WwpLeosFlowCpuRateLimitStatsCftPassed_Type()
)
wwpLeosFlowCpuRateLimitStatsCftPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsCftPassed.setStatus("current")
_WwpLeosFlowCpuRateLimitStatsDot1xPassed_Type = Gauge32
_WwpLeosFlowCpuRateLimitStatsDot1xPassed_Object = MibTableColumn
wwpLeosFlowCpuRateLimitStatsDot1xPassed = _WwpLeosFlowCpuRateLimitStatsDot1xPassed_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 32, 1, 5),
    _WwpLeosFlowCpuRateLimitStatsDot1xPassed_Type()
)
wwpLeosFlowCpuRateLimitStatsDot1xPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsDot1xPassed.setStatus("current")
_WwpLeosFlowCpuRateLimitStatsOamPassed_Type = Gauge32
_WwpLeosFlowCpuRateLimitStatsOamPassed_Object = MibTableColumn
wwpLeosFlowCpuRateLimitStatsOamPassed = _WwpLeosFlowCpuRateLimitStatsOamPassed_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 32, 1, 6),
    _WwpLeosFlowCpuRateLimitStatsOamPassed_Type()
)
wwpLeosFlowCpuRateLimitStatsOamPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsOamPassed.setStatus("current")
_WwpLeosFlowCpuRateLimitStatsEprArpPassed_Type = Gauge32
_WwpLeosFlowCpuRateLimitStatsEprArpPassed_Object = MibTableColumn
wwpLeosFlowCpuRateLimitStatsEprArpPassed = _WwpLeosFlowCpuRateLimitStatsEprArpPassed_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 32, 1, 7),
    _WwpLeosFlowCpuRateLimitStatsEprArpPassed_Type()
)
wwpLeosFlowCpuRateLimitStatsEprArpPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsEprArpPassed.setStatus("current")
_WwpLeosFlowCpuRateLimitStatsIgmpPassed_Type = Gauge32
_WwpLeosFlowCpuRateLimitStatsIgmpPassed_Object = MibTableColumn
wwpLeosFlowCpuRateLimitStatsIgmpPassed = _WwpLeosFlowCpuRateLimitStatsIgmpPassed_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 32, 1, 8),
    _WwpLeosFlowCpuRateLimitStatsIgmpPassed_Type()
)
wwpLeosFlowCpuRateLimitStatsIgmpPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsIgmpPassed.setStatus("current")
_WwpLeosFlowCpuRateLimitStatsInetPassed_Type = Gauge32
_WwpLeosFlowCpuRateLimitStatsInetPassed_Object = MibTableColumn
wwpLeosFlowCpuRateLimitStatsInetPassed = _WwpLeosFlowCpuRateLimitStatsInetPassed_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 32, 1, 9),
    _WwpLeosFlowCpuRateLimitStatsInetPassed_Type()
)
wwpLeosFlowCpuRateLimitStatsInetPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsInetPassed.setStatus("current")
_WwpLeosFlowCpuRateLimitStatsLacpPassed_Type = Gauge32
_WwpLeosFlowCpuRateLimitStatsLacpPassed_Object = MibTableColumn
wwpLeosFlowCpuRateLimitStatsLacpPassed = _WwpLeosFlowCpuRateLimitStatsLacpPassed_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 32, 1, 10),
    _WwpLeosFlowCpuRateLimitStatsLacpPassed_Type()
)
wwpLeosFlowCpuRateLimitStatsLacpPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsLacpPassed.setStatus("current")
_WwpLeosFlowCpuRateLimitStatsLldpPassed_Type = Gauge32
_WwpLeosFlowCpuRateLimitStatsLldpPassed_Object = MibTableColumn
wwpLeosFlowCpuRateLimitStatsLldpPassed = _WwpLeosFlowCpuRateLimitStatsLldpPassed_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 32, 1, 11),
    _WwpLeosFlowCpuRateLimitStatsLldpPassed_Type()
)
wwpLeosFlowCpuRateLimitStatsLldpPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsLldpPassed.setStatus("current")
_WwpLeosFlowCpuRateLimitStatsMplsPassed_Type = Gauge32
_WwpLeosFlowCpuRateLimitStatsMplsPassed_Object = MibTableColumn
wwpLeosFlowCpuRateLimitStatsMplsPassed = _WwpLeosFlowCpuRateLimitStatsMplsPassed_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 32, 1, 12),
    _WwpLeosFlowCpuRateLimitStatsMplsPassed_Type()
)
wwpLeosFlowCpuRateLimitStatsMplsPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsMplsPassed.setStatus("current")
_WwpLeosFlowCpuRateLimitStatsMstpPassed_Type = Gauge32
_WwpLeosFlowCpuRateLimitStatsMstpPassed_Object = MibTableColumn
wwpLeosFlowCpuRateLimitStatsMstpPassed = _WwpLeosFlowCpuRateLimitStatsMstpPassed_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 32, 1, 13),
    _WwpLeosFlowCpuRateLimitStatsMstpPassed_Type()
)
wwpLeosFlowCpuRateLimitStatsMstpPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsMstpPassed.setStatus("current")
_WwpLeosFlowCpuRateLimitStatsPeArpPassed_Type = Gauge32
_WwpLeosFlowCpuRateLimitStatsPeArpPassed_Object = MibTableColumn
wwpLeosFlowCpuRateLimitStatsPeArpPassed = _WwpLeosFlowCpuRateLimitStatsPeArpPassed_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 32, 1, 14),
    _WwpLeosFlowCpuRateLimitStatsPeArpPassed_Type()
)
wwpLeosFlowCpuRateLimitStatsPeArpPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsPeArpPassed.setStatus("current")
_WwpLeosFlowCpuRateLimitStatsPvstPassed_Type = Gauge32
_WwpLeosFlowCpuRateLimitStatsPvstPassed_Object = MibTableColumn
wwpLeosFlowCpuRateLimitStatsPvstPassed = _WwpLeosFlowCpuRateLimitStatsPvstPassed_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 32, 1, 15),
    _WwpLeosFlowCpuRateLimitStatsPvstPassed_Type()
)
wwpLeosFlowCpuRateLimitStatsPvstPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsPvstPassed.setStatus("current")
_WwpLeosFlowCpuRateLimitStatsRstpPassed_Type = Gauge32
_WwpLeosFlowCpuRateLimitStatsRstpPassed_Object = MibTableColumn
wwpLeosFlowCpuRateLimitStatsRstpPassed = _WwpLeosFlowCpuRateLimitStatsRstpPassed_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 32, 1, 16),
    _WwpLeosFlowCpuRateLimitStatsRstpPassed_Type()
)
wwpLeosFlowCpuRateLimitStatsRstpPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsRstpPassed.setStatus("current")
_WwpLeosFlowCpuRateLimitStatsLpbkPassed_Type = Gauge32
_WwpLeosFlowCpuRateLimitStatsLpbkPassed_Object = MibTableColumn
wwpLeosFlowCpuRateLimitStatsLpbkPassed = _WwpLeosFlowCpuRateLimitStatsLpbkPassed_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 32, 1, 17),
    _WwpLeosFlowCpuRateLimitStatsLpbkPassed_Type()
)
wwpLeosFlowCpuRateLimitStatsLpbkPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsLpbkPassed.setStatus("current")
_WwpLeosFlowCpuRateLimitStatsRmtLpbkPassed_Type = Gauge32
_WwpLeosFlowCpuRateLimitStatsRmtLpbkPassed_Object = MibTableColumn
wwpLeosFlowCpuRateLimitStatsRmtLpbkPassed = _WwpLeosFlowCpuRateLimitStatsRmtLpbkPassed_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 32, 1, 18),
    _WwpLeosFlowCpuRateLimitStatsRmtLpbkPassed_Type()
)
wwpLeosFlowCpuRateLimitStatsRmtLpbkPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsRmtLpbkPassed.setStatus("current")
_WwpLeosFlowCpuRateLimitStatsCxeRxPassed_Type = Gauge32
_WwpLeosFlowCpuRateLimitStatsCxeRxPassed_Object = MibTableColumn
wwpLeosFlowCpuRateLimitStatsCxeRxPassed = _WwpLeosFlowCpuRateLimitStatsCxeRxPassed_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 32, 1, 19),
    _WwpLeosFlowCpuRateLimitStatsCxeRxPassed_Type()
)
wwpLeosFlowCpuRateLimitStatsCxeRxPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsCxeRxPassed.setStatus("current")
_WwpLeosFlowCpuRateLimitStatsCxeTxPassed_Type = Gauge32
_WwpLeosFlowCpuRateLimitStatsCxeTxPassed_Object = MibTableColumn
wwpLeosFlowCpuRateLimitStatsCxeTxPassed = _WwpLeosFlowCpuRateLimitStatsCxeTxPassed_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 32, 1, 20),
    _WwpLeosFlowCpuRateLimitStatsCxeTxPassed_Type()
)
wwpLeosFlowCpuRateLimitStatsCxeTxPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsCxeTxPassed.setStatus("current")
_WwpLeosFlowCpuRateLimitStatsTwampPassed_Type = Gauge32
_WwpLeosFlowCpuRateLimitStatsTwampPassed_Object = MibTableColumn
wwpLeosFlowCpuRateLimitStatsTwampPassed = _WwpLeosFlowCpuRateLimitStatsTwampPassed_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 32, 1, 21),
    _WwpLeosFlowCpuRateLimitStatsTwampPassed_Type()
)
wwpLeosFlowCpuRateLimitStatsTwampPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsTwampPassed.setStatus("current")
_WwpLeosFlowCpuRateLimitStatsDfltPassed_Type = Gauge32
_WwpLeosFlowCpuRateLimitStatsDfltPassed_Object = MibTableColumn
wwpLeosFlowCpuRateLimitStatsDfltPassed = _WwpLeosFlowCpuRateLimitStatsDfltPassed_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 32, 1, 22),
    _WwpLeosFlowCpuRateLimitStatsDfltPassed_Type()
)
wwpLeosFlowCpuRateLimitStatsDfltPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsDfltPassed.setStatus("current")
_WwpLeosFlowCpuRateLimitStatsBootpDropped_Type = Gauge32
_WwpLeosFlowCpuRateLimitStatsBootpDropped_Object = MibTableColumn
wwpLeosFlowCpuRateLimitStatsBootpDropped = _WwpLeosFlowCpuRateLimitStatsBootpDropped_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 32, 1, 23),
    _WwpLeosFlowCpuRateLimitStatsBootpDropped_Type()
)
wwpLeosFlowCpuRateLimitStatsBootpDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsBootpDropped.setStatus("current")
_WwpLeosFlowCpuRateLimitStatsCfmDropped_Type = Gauge32
_WwpLeosFlowCpuRateLimitStatsCfmDropped_Object = MibTableColumn
wwpLeosFlowCpuRateLimitStatsCfmDropped = _WwpLeosFlowCpuRateLimitStatsCfmDropped_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 32, 1, 24),
    _WwpLeosFlowCpuRateLimitStatsCfmDropped_Type()
)
wwpLeosFlowCpuRateLimitStatsCfmDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsCfmDropped.setStatus("current")
_WwpLeosFlowCpuRateLimitStatsCftDropped_Type = Gauge32
_WwpLeosFlowCpuRateLimitStatsCftDropped_Object = MibTableColumn
wwpLeosFlowCpuRateLimitStatsCftDropped = _WwpLeosFlowCpuRateLimitStatsCftDropped_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 32, 1, 25),
    _WwpLeosFlowCpuRateLimitStatsCftDropped_Type()
)
wwpLeosFlowCpuRateLimitStatsCftDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsCftDropped.setStatus("current")
_WwpLeosFlowCpuRateLimitStatsDot1xDropped_Type = Gauge32
_WwpLeosFlowCpuRateLimitStatsDot1xDropped_Object = MibTableColumn
wwpLeosFlowCpuRateLimitStatsDot1xDropped = _WwpLeosFlowCpuRateLimitStatsDot1xDropped_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 32, 1, 26),
    _WwpLeosFlowCpuRateLimitStatsDot1xDropped_Type()
)
wwpLeosFlowCpuRateLimitStatsDot1xDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsDot1xDropped.setStatus("current")
_WwpLeosFlowCpuRateLimitStatsOamDropped_Type = Gauge32
_WwpLeosFlowCpuRateLimitStatsOamDropped_Object = MibTableColumn
wwpLeosFlowCpuRateLimitStatsOamDropped = _WwpLeosFlowCpuRateLimitStatsOamDropped_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 32, 1, 27),
    _WwpLeosFlowCpuRateLimitStatsOamDropped_Type()
)
wwpLeosFlowCpuRateLimitStatsOamDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsOamDropped.setStatus("current")
_WwpLeosFlowCpuRateLimitStatsEprArpDropped_Type = Gauge32
_WwpLeosFlowCpuRateLimitStatsEprArpDropped_Object = MibTableColumn
wwpLeosFlowCpuRateLimitStatsEprArpDropped = _WwpLeosFlowCpuRateLimitStatsEprArpDropped_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 32, 1, 28),
    _WwpLeosFlowCpuRateLimitStatsEprArpDropped_Type()
)
wwpLeosFlowCpuRateLimitStatsEprArpDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsEprArpDropped.setStatus("current")
_WwpLeosFlowCpuRateLimitStatsIgmpDropped_Type = Gauge32
_WwpLeosFlowCpuRateLimitStatsIgmpDropped_Object = MibTableColumn
wwpLeosFlowCpuRateLimitStatsIgmpDropped = _WwpLeosFlowCpuRateLimitStatsIgmpDropped_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 32, 1, 29),
    _WwpLeosFlowCpuRateLimitStatsIgmpDropped_Type()
)
wwpLeosFlowCpuRateLimitStatsIgmpDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsIgmpDropped.setStatus("current")
_WwpLeosFlowCpuRateLimitStatsInetDropped_Type = Gauge32
_WwpLeosFlowCpuRateLimitStatsInetDropped_Object = MibTableColumn
wwpLeosFlowCpuRateLimitStatsInetDropped = _WwpLeosFlowCpuRateLimitStatsInetDropped_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 32, 1, 30),
    _WwpLeosFlowCpuRateLimitStatsInetDropped_Type()
)
wwpLeosFlowCpuRateLimitStatsInetDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsInetDropped.setStatus("current")
_WwpLeosFlowCpuRateLimitStatsLacpDropped_Type = Gauge32
_WwpLeosFlowCpuRateLimitStatsLacpDropped_Object = MibTableColumn
wwpLeosFlowCpuRateLimitStatsLacpDropped = _WwpLeosFlowCpuRateLimitStatsLacpDropped_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 32, 1, 31),
    _WwpLeosFlowCpuRateLimitStatsLacpDropped_Type()
)
wwpLeosFlowCpuRateLimitStatsLacpDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsLacpDropped.setStatus("current")
_WwpLeosFlowCpuRateLimitStatsLldpDropped_Type = Gauge32
_WwpLeosFlowCpuRateLimitStatsLldpDropped_Object = MibTableColumn
wwpLeosFlowCpuRateLimitStatsLldpDropped = _WwpLeosFlowCpuRateLimitStatsLldpDropped_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 32, 1, 32),
    _WwpLeosFlowCpuRateLimitStatsLldpDropped_Type()
)
wwpLeosFlowCpuRateLimitStatsLldpDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsLldpDropped.setStatus("current")
_WwpLeosFlowCpuRateLimitStatsMplsDropped_Type = Gauge32
_WwpLeosFlowCpuRateLimitStatsMplsDropped_Object = MibTableColumn
wwpLeosFlowCpuRateLimitStatsMplsDropped = _WwpLeosFlowCpuRateLimitStatsMplsDropped_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 32, 1, 33),
    _WwpLeosFlowCpuRateLimitStatsMplsDropped_Type()
)
wwpLeosFlowCpuRateLimitStatsMplsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsMplsDropped.setStatus("current")
_WwpLeosFlowCpuRateLimitStatsMstpDropped_Type = Gauge32
_WwpLeosFlowCpuRateLimitStatsMstpDropped_Object = MibTableColumn
wwpLeosFlowCpuRateLimitStatsMstpDropped = _WwpLeosFlowCpuRateLimitStatsMstpDropped_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 32, 1, 34),
    _WwpLeosFlowCpuRateLimitStatsMstpDropped_Type()
)
wwpLeosFlowCpuRateLimitStatsMstpDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsMstpDropped.setStatus("current")
_WwpLeosFlowCpuRateLimitStatsPeArpDropped_Type = Gauge32
_WwpLeosFlowCpuRateLimitStatsPeArpDropped_Object = MibTableColumn
wwpLeosFlowCpuRateLimitStatsPeArpDropped = _WwpLeosFlowCpuRateLimitStatsPeArpDropped_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 32, 1, 35),
    _WwpLeosFlowCpuRateLimitStatsPeArpDropped_Type()
)
wwpLeosFlowCpuRateLimitStatsPeArpDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsPeArpDropped.setStatus("current")
_WwpLeosFlowCpuRateLimitStatsPvstDropped_Type = Gauge32
_WwpLeosFlowCpuRateLimitStatsPvstDropped_Object = MibTableColumn
wwpLeosFlowCpuRateLimitStatsPvstDropped = _WwpLeosFlowCpuRateLimitStatsPvstDropped_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 32, 1, 36),
    _WwpLeosFlowCpuRateLimitStatsPvstDropped_Type()
)
wwpLeosFlowCpuRateLimitStatsPvstDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsPvstDropped.setStatus("current")
_WwpLeosFlowCpuRateLimitStatsRstpDropped_Type = Gauge32
_WwpLeosFlowCpuRateLimitStatsRstpDropped_Object = MibTableColumn
wwpLeosFlowCpuRateLimitStatsRstpDropped = _WwpLeosFlowCpuRateLimitStatsRstpDropped_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 32, 1, 37),
    _WwpLeosFlowCpuRateLimitStatsRstpDropped_Type()
)
wwpLeosFlowCpuRateLimitStatsRstpDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsRstpDropped.setStatus("current")
_WwpLeosFlowCpuRateLimitStatsLpbkDropped_Type = Gauge32
_WwpLeosFlowCpuRateLimitStatsLpbkDropped_Object = MibTableColumn
wwpLeosFlowCpuRateLimitStatsLpbkDropped = _WwpLeosFlowCpuRateLimitStatsLpbkDropped_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 32, 1, 38),
    _WwpLeosFlowCpuRateLimitStatsLpbkDropped_Type()
)
wwpLeosFlowCpuRateLimitStatsLpbkDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsLpbkDropped.setStatus("current")
_WwpLeosFlowCpuRateLimitStatsRmtLpbkDropped_Type = Gauge32
_WwpLeosFlowCpuRateLimitStatsRmtLpbkDropped_Object = MibTableColumn
wwpLeosFlowCpuRateLimitStatsRmtLpbkDropped = _WwpLeosFlowCpuRateLimitStatsRmtLpbkDropped_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 32, 1, 39),
    _WwpLeosFlowCpuRateLimitStatsRmtLpbkDropped_Type()
)
wwpLeosFlowCpuRateLimitStatsRmtLpbkDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsRmtLpbkDropped.setStatus("current")
_WwpLeosFlowCpuRateLimitStatsCxeRxDropped_Type = Gauge32
_WwpLeosFlowCpuRateLimitStatsCxeRxDropped_Object = MibTableColumn
wwpLeosFlowCpuRateLimitStatsCxeRxDropped = _WwpLeosFlowCpuRateLimitStatsCxeRxDropped_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 32, 1, 40),
    _WwpLeosFlowCpuRateLimitStatsCxeRxDropped_Type()
)
wwpLeosFlowCpuRateLimitStatsCxeRxDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsCxeRxDropped.setStatus("current")
_WwpLeosFlowCpuRateLimitStatsCxeTxDropped_Type = Gauge32
_WwpLeosFlowCpuRateLimitStatsCxeTxDropped_Object = MibTableColumn
wwpLeosFlowCpuRateLimitStatsCxeTxDropped = _WwpLeosFlowCpuRateLimitStatsCxeTxDropped_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 32, 1, 41),
    _WwpLeosFlowCpuRateLimitStatsCxeTxDropped_Type()
)
wwpLeosFlowCpuRateLimitStatsCxeTxDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsCxeTxDropped.setStatus("current")
_WwpLeosFlowCpuRateLimitStatsTwampDropped_Type = Gauge32
_WwpLeosFlowCpuRateLimitStatsTwampDropped_Object = MibTableColumn
wwpLeosFlowCpuRateLimitStatsTwampDropped = _WwpLeosFlowCpuRateLimitStatsTwampDropped_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 32, 1, 42),
    _WwpLeosFlowCpuRateLimitStatsTwampDropped_Type()
)
wwpLeosFlowCpuRateLimitStatsTwampDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsTwampDropped.setStatus("current")
_WwpLeosFlowCpuRateLimitStatsDfltDropped_Type = Gauge32
_WwpLeosFlowCpuRateLimitStatsDfltDropped_Object = MibTableColumn
wwpLeosFlowCpuRateLimitStatsDfltDropped = _WwpLeosFlowCpuRateLimitStatsDfltDropped_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 32, 1, 43),
    _WwpLeosFlowCpuRateLimitStatsDfltDropped_Type()
)
wwpLeosFlowCpuRateLimitStatsDfltDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsDfltDropped.setStatus("current")
_WwpLeosFlowCpuRateLimitStatsTwampRspPassed_Type = Gauge32
_WwpLeosFlowCpuRateLimitStatsTwampRspPassed_Object = MibTableColumn
wwpLeosFlowCpuRateLimitStatsTwampRspPassed = _WwpLeosFlowCpuRateLimitStatsTwampRspPassed_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 32, 1, 44),
    _WwpLeosFlowCpuRateLimitStatsTwampRspPassed_Type()
)
wwpLeosFlowCpuRateLimitStatsTwampRspPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsTwampRspPassed.setStatus("current")
_WwpLeosFlowCpuRateLimitStatsTwampRspDropped_Type = Gauge32
_WwpLeosFlowCpuRateLimitStatsTwampRspDropped_Object = MibTableColumn
wwpLeosFlowCpuRateLimitStatsTwampRspDropped = _WwpLeosFlowCpuRateLimitStatsTwampRspDropped_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 32, 1, 45),
    _WwpLeosFlowCpuRateLimitStatsTwampRspDropped_Type()
)
wwpLeosFlowCpuRateLimitStatsTwampRspDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsTwampRspDropped.setStatus("current")
_WwpLeosFlowCpuRateLimitStatsMultiCastPassed_Type = Gauge32
_WwpLeosFlowCpuRateLimitStatsMultiCastPassed_Object = MibTableColumn
wwpLeosFlowCpuRateLimitStatsMultiCastPassed = _WwpLeosFlowCpuRateLimitStatsMultiCastPassed_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 32, 1, 46),
    _WwpLeosFlowCpuRateLimitStatsMultiCastPassed_Type()
)
wwpLeosFlowCpuRateLimitStatsMultiCastPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsMultiCastPassed.setStatus("current")
_WwpLeosFlowCpuRateLimitStatsMultiCastDropped_Type = Gauge32
_WwpLeosFlowCpuRateLimitStatsMultiCastDropped_Object = MibTableColumn
wwpLeosFlowCpuRateLimitStatsMultiCastDropped = _WwpLeosFlowCpuRateLimitStatsMultiCastDropped_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 32, 1, 47),
    _WwpLeosFlowCpuRateLimitStatsMultiCastDropped_Type()
)
wwpLeosFlowCpuRateLimitStatsMultiCastDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsMultiCastDropped.setStatus("current")
_WwpLeosFlowCpuRateLimitStatsBroadCastPassed_Type = Gauge32
_WwpLeosFlowCpuRateLimitStatsBroadCastPassed_Object = MibTableColumn
wwpLeosFlowCpuRateLimitStatsBroadCastPassed = _WwpLeosFlowCpuRateLimitStatsBroadCastPassed_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 32, 1, 48),
    _WwpLeosFlowCpuRateLimitStatsBroadCastPassed_Type()
)
wwpLeosFlowCpuRateLimitStatsBroadCastPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsBroadCastPassed.setStatus("current")
_WwpLeosFlowCpuRateLimitStatsBroadCastDropped_Type = Gauge32
_WwpLeosFlowCpuRateLimitStatsBroadCastDropped_Object = MibTableColumn
wwpLeosFlowCpuRateLimitStatsBroadCastDropped = _WwpLeosFlowCpuRateLimitStatsBroadCastDropped_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 32, 1, 49),
    _WwpLeosFlowCpuRateLimitStatsBroadCastDropped_Type()
)
wwpLeosFlowCpuRateLimitStatsBroadCastDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsBroadCastDropped.setStatus("current")
_WwpLeosFlowCpuRateLimitStatsArpPassed_Type = Gauge32
_WwpLeosFlowCpuRateLimitStatsArpPassed_Object = MibTableColumn
wwpLeosFlowCpuRateLimitStatsArpPassed = _WwpLeosFlowCpuRateLimitStatsArpPassed_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 32, 1, 50),
    _WwpLeosFlowCpuRateLimitStatsArpPassed_Type()
)
wwpLeosFlowCpuRateLimitStatsArpPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsArpPassed.setStatus("current")
_WwpLeosFlowCpuRateLimitStatsArpDropped_Type = Gauge32
_WwpLeosFlowCpuRateLimitStatsArpDropped_Object = MibTableColumn
wwpLeosFlowCpuRateLimitStatsArpDropped = _WwpLeosFlowCpuRateLimitStatsArpDropped_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 32, 1, 51),
    _WwpLeosFlowCpuRateLimitStatsArpDropped_Type()
)
wwpLeosFlowCpuRateLimitStatsArpDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsArpDropped.setStatus("current")
_WwpLeosFlowCpuRateLimitStatsIcmpPassed_Type = Gauge32
_WwpLeosFlowCpuRateLimitStatsIcmpPassed_Object = MibTableColumn
wwpLeosFlowCpuRateLimitStatsIcmpPassed = _WwpLeosFlowCpuRateLimitStatsIcmpPassed_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 32, 1, 52),
    _WwpLeosFlowCpuRateLimitStatsIcmpPassed_Type()
)
wwpLeosFlowCpuRateLimitStatsIcmpPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsIcmpPassed.setStatus("current")
_WwpLeosFlowCpuRateLimitStatsIcmpDropped_Type = Gauge32
_WwpLeosFlowCpuRateLimitStatsIcmpDropped_Object = MibTableColumn
wwpLeosFlowCpuRateLimitStatsIcmpDropped = _WwpLeosFlowCpuRateLimitStatsIcmpDropped_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 32, 1, 53),
    _WwpLeosFlowCpuRateLimitStatsIcmpDropped_Type()
)
wwpLeosFlowCpuRateLimitStatsIcmpDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsIcmpDropped.setStatus("current")
_WwpLeosFlowCpuRateLimitStatsTcpSynPassed_Type = Gauge32
_WwpLeosFlowCpuRateLimitStatsTcpSynPassed_Object = MibTableColumn
wwpLeosFlowCpuRateLimitStatsTcpSynPassed = _WwpLeosFlowCpuRateLimitStatsTcpSynPassed_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 32, 1, 54),
    _WwpLeosFlowCpuRateLimitStatsTcpSynPassed_Type()
)
wwpLeosFlowCpuRateLimitStatsTcpSynPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsTcpSynPassed.setStatus("current")
_WwpLeosFlowCpuRateLimitStatsTcpSynDropped_Type = Gauge32
_WwpLeosFlowCpuRateLimitStatsTcpSynDropped_Object = MibTableColumn
wwpLeosFlowCpuRateLimitStatsTcpSynDropped = _WwpLeosFlowCpuRateLimitStatsTcpSynDropped_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 32, 1, 55),
    _WwpLeosFlowCpuRateLimitStatsTcpSynDropped_Type()
)
wwpLeosFlowCpuRateLimitStatsTcpSynDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsTcpSynDropped.setStatus("current")
_WwpLeosFlowCpuRateLimitStatsRapsPassed_Type = Gauge32
_WwpLeosFlowCpuRateLimitStatsRapsPassed_Object = MibTableColumn
wwpLeosFlowCpuRateLimitStatsRapsPassed = _WwpLeosFlowCpuRateLimitStatsRapsPassed_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 32, 1, 56),
    _WwpLeosFlowCpuRateLimitStatsRapsPassed_Type()
)
wwpLeosFlowCpuRateLimitStatsRapsPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsRapsPassed.setStatus("current")
_WwpLeosFlowCpuRateLimitStatsRapsDropped_Type = Gauge32
_WwpLeosFlowCpuRateLimitStatsRapsDropped_Object = MibTableColumn
wwpLeosFlowCpuRateLimitStatsRapsDropped = _WwpLeosFlowCpuRateLimitStatsRapsDropped_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 32, 1, 57),
    _WwpLeosFlowCpuRateLimitStatsRapsDropped_Type()
)
wwpLeosFlowCpuRateLimitStatsRapsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsRapsDropped.setStatus("current")
_WwpLeosFlowCpuRateLimitStatsIpMgmtPassed_Type = Gauge32
_WwpLeosFlowCpuRateLimitStatsIpMgmtPassed_Object = MibTableColumn
wwpLeosFlowCpuRateLimitStatsIpMgmtPassed = _WwpLeosFlowCpuRateLimitStatsIpMgmtPassed_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 32, 1, 58),
    _WwpLeosFlowCpuRateLimitStatsIpMgmtPassed_Type()
)
wwpLeosFlowCpuRateLimitStatsIpMgmtPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsIpMgmtPassed.setStatus("current")
_WwpLeosFlowCpuRateLimitStatsIpMgmtDropped_Type = Gauge32
_WwpLeosFlowCpuRateLimitStatsIpMgmtDropped_Object = MibTableColumn
wwpLeosFlowCpuRateLimitStatsIpMgmtDropped = _WwpLeosFlowCpuRateLimitStatsIpMgmtDropped_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 32, 1, 59),
    _WwpLeosFlowCpuRateLimitStatsIpMgmtDropped_Type()
)
wwpLeosFlowCpuRateLimitStatsIpMgmtDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsIpMgmtDropped.setStatus("current")
_WwpLeosFlowCpuRateLimitStatsIpControlPassed_Type = Gauge32
_WwpLeosFlowCpuRateLimitStatsIpControlPassed_Object = MibTableColumn
wwpLeosFlowCpuRateLimitStatsIpControlPassed = _WwpLeosFlowCpuRateLimitStatsIpControlPassed_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 32, 1, 60),
    _WwpLeosFlowCpuRateLimitStatsIpControlPassed_Type()
)
wwpLeosFlowCpuRateLimitStatsIpControlPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsIpControlPassed.setStatus("current")
_WwpLeosFlowCpuRateLimitStatsIpControlDropped_Type = Gauge32
_WwpLeosFlowCpuRateLimitStatsIpControlDropped_Object = MibTableColumn
wwpLeosFlowCpuRateLimitStatsIpControlDropped = _WwpLeosFlowCpuRateLimitStatsIpControlDropped_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 32, 1, 61),
    _WwpLeosFlowCpuRateLimitStatsIpControlDropped_Type()
)
wwpLeosFlowCpuRateLimitStatsIpControlDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsIpControlDropped.setStatus("current")
_WwpLeosFlowCpuRateLimitStatsIpV6MgmtPassed_Type = Gauge32
_WwpLeosFlowCpuRateLimitStatsIpV6MgmtPassed_Object = MibTableColumn
wwpLeosFlowCpuRateLimitStatsIpV6MgmtPassed = _WwpLeosFlowCpuRateLimitStatsIpV6MgmtPassed_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 32, 1, 62),
    _WwpLeosFlowCpuRateLimitStatsIpV6MgmtPassed_Type()
)
wwpLeosFlowCpuRateLimitStatsIpV6MgmtPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsIpV6MgmtPassed.setStatus("current")
_WwpLeosFlowCpuRateLimitStatsIpV6MgmtDropped_Type = Gauge32
_WwpLeosFlowCpuRateLimitStatsIpV6MgmtDropped_Object = MibTableColumn
wwpLeosFlowCpuRateLimitStatsIpV6MgmtDropped = _WwpLeosFlowCpuRateLimitStatsIpV6MgmtDropped_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 32, 1, 63),
    _WwpLeosFlowCpuRateLimitStatsIpV6MgmtDropped_Type()
)
wwpLeosFlowCpuRateLimitStatsIpV6MgmtDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsIpV6MgmtDropped.setStatus("current")
_WwpLeosFlowCpuRateLimitStatsInet6Passed_Type = Gauge32
_WwpLeosFlowCpuRateLimitStatsInet6Passed_Object = MibTableColumn
wwpLeosFlowCpuRateLimitStatsInet6Passed = _WwpLeosFlowCpuRateLimitStatsInet6Passed_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 32, 1, 64),
    _WwpLeosFlowCpuRateLimitStatsInet6Passed_Type()
)
wwpLeosFlowCpuRateLimitStatsInet6Passed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsInet6Passed.setStatus("current")
_WwpLeosFlowCpuRateLimitStatsInet6Dropped_Type = Gauge32
_WwpLeosFlowCpuRateLimitStatsInet6Dropped_Object = MibTableColumn
wwpLeosFlowCpuRateLimitStatsInet6Dropped = _WwpLeosFlowCpuRateLimitStatsInet6Dropped_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 32, 1, 65),
    _WwpLeosFlowCpuRateLimitStatsInet6Dropped_Type()
)
wwpLeosFlowCpuRateLimitStatsInet6Dropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsInet6Dropped.setStatus("current")
_WwpLeosFlowCpuRateLimitStatsClearTable_Object = MibTable
wwpLeosFlowCpuRateLimitStatsClearTable = _WwpLeosFlowCpuRateLimitStatsClearTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 33)
)
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsClearTable.setStatus("current")
_WwpLeosFlowCpuRateLimitStatsClearEntry_Object = MibTableRow
wwpLeosFlowCpuRateLimitStatsClearEntry = _WwpLeosFlowCpuRateLimitStatsClearEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 33, 1)
)
wwpLeosFlowCpuRateLimitStatsClearEntry.setIndexNames(
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowCpuRateLimitStatsClearPort"),
)
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsClearEntry.setStatus("current")


class _WwpLeosFlowCpuRateLimitStatsClearPort_Type(Integer32):
    """Custom type wwpLeosFlowCpuRateLimitStatsClearPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_WwpLeosFlowCpuRateLimitStatsClearPort_Type.__name__ = "Integer32"
_WwpLeosFlowCpuRateLimitStatsClearPort_Object = MibTableColumn
wwpLeosFlowCpuRateLimitStatsClearPort = _WwpLeosFlowCpuRateLimitStatsClearPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 33, 1, 1),
    _WwpLeosFlowCpuRateLimitStatsClearPort_Type()
)
wwpLeosFlowCpuRateLimitStatsClearPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsClearPort.setStatus("current")
_WwpLeosFlowCpuRateLimitStatsClear_Type = TruthValue
_WwpLeosFlowCpuRateLimitStatsClear_Object = MibTableColumn
wwpLeosFlowCpuRateLimitStatsClear = _WwpLeosFlowCpuRateLimitStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 33, 1, 2),
    _WwpLeosFlowCpuRateLimitStatsClear_Type()
)
wwpLeosFlowCpuRateLimitStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowCpuRateLimitStatsClear.setStatus("current")
_WwpLeosFlowServiceTotalStatsTable_Object = MibTable
wwpLeosFlowServiceTotalStatsTable = _WwpLeosFlowServiceTotalStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 34)
)
if mibBuilder.loadTexts:
    wwpLeosFlowServiceTotalStatsTable.setStatus("current")
_WwpLeosFlowServiceTotalStatsEntry_Object = MibTableRow
wwpLeosFlowServiceTotalStatsEntry = _WwpLeosFlowServiceTotalStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 34, 1)
)
wwpLeosFlowServiceTotalStatsEntry.setIndexNames(
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowSMappingNetType"),
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowSMappingNetValue"),
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowSMappingSrcType"),
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowSMappingSrcValue"),
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowSMappingDstType"),
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowSMappingDstValue"),
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowSMappingCosType"),
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowSMappingCosValue"),
)
if mibBuilder.loadTexts:
    wwpLeosFlowServiceTotalStatsEntry.setStatus("current")
_WwpLeosFlowServiceTotalStatsRxHi_Type = Counter32
_WwpLeosFlowServiceTotalStatsRxHi_Object = MibTableColumn
wwpLeosFlowServiceTotalStatsRxHi = _WwpLeosFlowServiceTotalStatsRxHi_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 34, 1, 1),
    _WwpLeosFlowServiceTotalStatsRxHi_Type()
)
wwpLeosFlowServiceTotalStatsRxHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowServiceTotalStatsRxHi.setStatus("current")
_WwpLeosFlowServiceTotalStatsRxLo_Type = Counter32
_WwpLeosFlowServiceTotalStatsRxLo_Object = MibTableColumn
wwpLeosFlowServiceTotalStatsRxLo = _WwpLeosFlowServiceTotalStatsRxLo_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 34, 1, 2),
    _WwpLeosFlowServiceTotalStatsRxLo_Type()
)
wwpLeosFlowServiceTotalStatsRxLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowServiceTotalStatsRxLo.setStatus("current")
_WwpLeosFlowServiceTotalStatsTxHi_Type = Counter32
_WwpLeosFlowServiceTotalStatsTxHi_Object = MibTableColumn
wwpLeosFlowServiceTotalStatsTxHi = _WwpLeosFlowServiceTotalStatsTxHi_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 34, 1, 3),
    _WwpLeosFlowServiceTotalStatsTxHi_Type()
)
wwpLeosFlowServiceTotalStatsTxHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowServiceTotalStatsTxHi.setStatus("current")
_WwpLeosFlowServiceTotalStatsTxLo_Type = Counter32
_WwpLeosFlowServiceTotalStatsTxLo_Object = MibTableColumn
wwpLeosFlowServiceTotalStatsTxLo = _WwpLeosFlowServiceTotalStatsTxLo_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 34, 1, 4),
    _WwpLeosFlowServiceTotalStatsTxLo_Type()
)
wwpLeosFlowServiceTotalStatsTxLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowServiceTotalStatsTxLo.setStatus("current")


class _WwpLeosFlowServiceTotalStatsType_Type(Integer32):
    """Custom type wwpLeosFlowServiceTotalStatsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 2),
          ("forward", 1))
    )


_WwpLeosFlowServiceTotalStatsType_Type.__name__ = "Integer32"
_WwpLeosFlowServiceTotalStatsType_Object = MibTableColumn
wwpLeosFlowServiceTotalStatsType = _WwpLeosFlowServiceTotalStatsType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 34, 1, 5),
    _WwpLeosFlowServiceTotalStatsType_Type()
)
wwpLeosFlowServiceTotalStatsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowServiceTotalStatsType.setStatus("current")
_WwpLeosFlowPortServiceLevelTable_Object = MibTable
wwpLeosFlowPortServiceLevelTable = _WwpLeosFlowPortServiceLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 40)
)
if mibBuilder.loadTexts:
    wwpLeosFlowPortServiceLevelTable.setStatus("current")
_WwpLeosFlowPortServiceLevelEntry_Object = MibTableRow
wwpLeosFlowPortServiceLevelEntry = _WwpLeosFlowPortServiceLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 40, 1)
)
wwpLeosFlowPortServiceLevelEntry.setIndexNames(
    (0, "WWP-LEOS-FLOW-MIB", "wwpLeosFlowPortServiceLevelPort"),
)
if mibBuilder.loadTexts:
    wwpLeosFlowPortServiceLevelEntry.setStatus("current")


class _WwpLeosFlowPortServiceLevelPort_Type(Integer32):
    """Custom type wwpLeosFlowPortServiceLevelPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLeosFlowPortServiceLevelPort_Type.__name__ = "Integer32"
_WwpLeosFlowPortServiceLevelPort_Object = MibTableColumn
wwpLeosFlowPortServiceLevelPort = _WwpLeosFlowPortServiceLevelPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 40, 1, 1),
    _WwpLeosFlowPortServiceLevelPort_Type()
)
wwpLeosFlowPortServiceLevelPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosFlowPortServiceLevelPort.setStatus("current")


class _WwpLeosFlowPortServiceLevelMaxBandwidth_Type(Integer32):
    """Custom type wwpLeosFlowPortServiceLevelMaxBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8000000),
    )


_WwpLeosFlowPortServiceLevelMaxBandwidth_Type.__name__ = "Integer32"
_WwpLeosFlowPortServiceLevelMaxBandwidth_Object = MibTableColumn
wwpLeosFlowPortServiceLevelMaxBandwidth = _WwpLeosFlowPortServiceLevelMaxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 40, 1, 2),
    _WwpLeosFlowPortServiceLevelMaxBandwidth_Type()
)
wwpLeosFlowPortServiceLevelMaxBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowPortServiceLevelMaxBandwidth.setStatus("current")


class _WwpLeosFlowPortServiceLevelQueueSize_Type(Integer32):
    """Custom type wwpLeosFlowPortServiceLevelQueueSize based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("size0KB", 0),
          ("size128KB", 4),
          ("size16KB", 1),
          ("size1MB", 7),
          ("size256KB", 5),
          ("size2MB", 8),
          ("size32KB", 2),
          ("size4MB", 9),
          ("size512KB", 6),
          ("size64KB", 3))
    )


_WwpLeosFlowPortServiceLevelQueueSize_Type.__name__ = "Integer32"
_WwpLeosFlowPortServiceLevelQueueSize_Object = MibTableColumn
wwpLeosFlowPortServiceLevelQueueSize = _WwpLeosFlowPortServiceLevelQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 40, 1, 3),
    _WwpLeosFlowPortServiceLevelQueueSize_Type()
)
wwpLeosFlowPortServiceLevelQueueSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowPortServiceLevelQueueSize.setStatus("current")


class _WwpLeosFlowPortServiceLevelQueueSizeYellow_Type(Integer32):
    """Custom type wwpLeosFlowPortServiceLevelQueueSizeYellow based on Integer32"""
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
        *(("size128KB", 4),
          ("size16KB", 1),
          ("size32KB", 2),
          ("size64KB", 3))
    )


_WwpLeosFlowPortServiceLevelQueueSizeYellow_Type.__name__ = "Integer32"
_WwpLeosFlowPortServiceLevelQueueSizeYellow_Object = MibTableColumn
wwpLeosFlowPortServiceLevelQueueSizeYellow = _WwpLeosFlowPortServiceLevelQueueSizeYellow_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 40, 1, 4),
    _WwpLeosFlowPortServiceLevelQueueSizeYellow_Type()
)
wwpLeosFlowPortServiceLevelQueueSizeYellow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowPortServiceLevelQueueSizeYellow.setStatus("current")


class _WwpLeosFlowPortServiceLevelQueueSizeRed_Type(Integer32):
    """Custom type wwpLeosFlowPortServiceLevelQueueSizeRed based on Integer32"""
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
        *(("size128KB", 4),
          ("size16KB", 1),
          ("size32KB", 2),
          ("size64KB", 3))
    )


_WwpLeosFlowPortServiceLevelQueueSizeRed_Type.__name__ = "Integer32"
_WwpLeosFlowPortServiceLevelQueueSizeRed_Object = MibTableColumn
wwpLeosFlowPortServiceLevelQueueSizeRed = _WwpLeosFlowPortServiceLevelQueueSizeRed_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 40, 1, 5),
    _WwpLeosFlowPortServiceLevelQueueSizeRed_Type()
)
wwpLeosFlowPortServiceLevelQueueSizeRed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowPortServiceLevelQueueSizeRed.setStatus("current")


class _WwpLeosFlowPortServiceLevelFlowGroup_Type(Integer32):
    """Custom type wwpLeosFlowPortServiceLevelFlowGroup based on Integer32"""
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


_WwpLeosFlowPortServiceLevelFlowGroup_Type.__name__ = "Integer32"
_WwpLeosFlowPortServiceLevelFlowGroup_Object = MibTableColumn
wwpLeosFlowPortServiceLevelFlowGroup = _WwpLeosFlowPortServiceLevelFlowGroup_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 40, 1, 6),
    _WwpLeosFlowPortServiceLevelFlowGroup_Type()
)
wwpLeosFlowPortServiceLevelFlowGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowPortServiceLevelFlowGroup.setStatus("current")


class _WwpLeosFlowPortServiceLevelRedCurve_Type(Unsigned32):
    """Custom type wwpLeosFlowPortServiceLevelRedCurve based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_WwpLeosFlowPortServiceLevelRedCurve_Type.__name__ = "Unsigned32"
_WwpLeosFlowPortServiceLevelRedCurve_Object = MibTableColumn
wwpLeosFlowPortServiceLevelRedCurve = _WwpLeosFlowPortServiceLevelRedCurve_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 40, 1, 7),
    _WwpLeosFlowPortServiceLevelRedCurve_Type()
)
wwpLeosFlowPortServiceLevelRedCurve.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosFlowPortServiceLevelRedCurve.setStatus("current")


class _WwpLeosFlowBurstConfigBacklogLimit_Type(Unsigned32):
    """Custom type wwpLeosFlowBurstConfigBacklogLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 131072),
    )


_WwpLeosFlowBurstConfigBacklogLimit_Type.__name__ = "Unsigned32"
_WwpLeosFlowBurstConfigBacklogLimit_Object = MibScalar
wwpLeosFlowBurstConfigBacklogLimit = _WwpLeosFlowBurstConfigBacklogLimit_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 41),
    _WwpLeosFlowBurstConfigBacklogLimit_Type()
)
wwpLeosFlowBurstConfigBacklogLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowBurstConfigBacklogLimit.setStatus("current")


class _WwpLeosFlowBurstConfigMulticastLimit_Type(Unsigned32):
    """Custom type wwpLeosFlowBurstConfigMulticastLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 131072),
    )


_WwpLeosFlowBurstConfigMulticastLimit_Type.__name__ = "Unsigned32"
_WwpLeosFlowBurstConfigMulticastLimit_Object = MibScalar
wwpLeosFlowBurstConfigMulticastLimit = _WwpLeosFlowBurstConfigMulticastLimit_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 42),
    _WwpLeosFlowBurstConfigMulticastLimit_Type()
)
wwpLeosFlowBurstConfigMulticastLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowBurstConfigMulticastLimit.setStatus("current")


class _WwpLeosFlowBurstConfigVlanPriFltrOnThld_Type(Integer32):
    """Custom type wwpLeosFlowBurstConfigVlanPriFltrOnThld based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WwpLeosFlowBurstConfigVlanPriFltrOnThld_Type.__name__ = "Integer32"
_WwpLeosFlowBurstConfigVlanPriFltrOnThld_Object = MibScalar
wwpLeosFlowBurstConfigVlanPriFltrOnThld = _WwpLeosFlowBurstConfigVlanPriFltrOnThld_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 43),
    _WwpLeosFlowBurstConfigVlanPriFltrOnThld_Type()
)
wwpLeosFlowBurstConfigVlanPriFltrOnThld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowBurstConfigVlanPriFltrOnThld.setStatus("current")


class _WwpLeosFlowBurstConfigVlanPriFltrOffThld_Type(Integer32):
    """Custom type wwpLeosFlowBurstConfigVlanPriFltrOffThld based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WwpLeosFlowBurstConfigVlanPriFltrOffThld_Type.__name__ = "Integer32"
_WwpLeosFlowBurstConfigVlanPriFltrOffThld_Object = MibScalar
wwpLeosFlowBurstConfigVlanPriFltrOffThld = _WwpLeosFlowBurstConfigVlanPriFltrOffThld_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 44),
    _WwpLeosFlowBurstConfigVlanPriFltrOffThld_Type()
)
wwpLeosFlowBurstConfigVlanPriFltrOffThld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowBurstConfigVlanPriFltrOffThld.setStatus("current")


class _WwpLeosFlowBurstConfigVlanPriFltrPriMatch_Type(Integer32):
    """Custom type wwpLeosFlowBurstConfigVlanPriFltrPriMatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosFlowBurstConfigVlanPriFltrPriMatch_Type.__name__ = "Integer32"
_WwpLeosFlowBurstConfigVlanPriFltrPriMatch_Object = MibScalar
wwpLeosFlowBurstConfigVlanPriFltrPriMatch = _WwpLeosFlowBurstConfigVlanPriFltrPriMatch_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 45),
    _WwpLeosFlowBurstConfigVlanPriFltrPriMatch_Type()
)
wwpLeosFlowBurstConfigVlanPriFltrPriMatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowBurstConfigVlanPriFltrPriMatch.setStatus("current")


class _WwpLeosFlowBurstConfigVlanPriFltrState_Type(Integer32):
    """Custom type wwpLeosFlowBurstConfigVlanPriFltrState based on Integer32"""
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


_WwpLeosFlowBurstConfigVlanPriFltrState_Type.__name__ = "Integer32"
_WwpLeosFlowBurstConfigVlanPriFltrState_Object = MibScalar
wwpLeosFlowBurstConfigVlanPriFltrState = _WwpLeosFlowBurstConfigVlanPriFltrState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 1, 46),
    _WwpLeosFlowBurstConfigVlanPriFltrState_Type()
)
wwpLeosFlowBurstConfigVlanPriFltrState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosFlowBurstConfigVlanPriFltrState.setStatus("current")
_WwpLeosFlowNotifAttrs_ObjectIdentity = ObjectIdentity
wwpLeosFlowNotifAttrs = _WwpLeosFlowNotifAttrs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 2)
)


class _WwpLeosFlowMacMotionAttrOldPort_Type(Integer32):
    """Custom type wwpLeosFlowMacMotionAttrOldPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_WwpLeosFlowMacMotionAttrOldPort_Type.__name__ = "Integer32"
_WwpLeosFlowMacMotionAttrOldPort_Object = MibScalar
wwpLeosFlowMacMotionAttrOldPort = _WwpLeosFlowMacMotionAttrOldPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 2, 1),
    _WwpLeosFlowMacMotionAttrOldPort_Type()
)
wwpLeosFlowMacMotionAttrOldPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wwpLeosFlowMacMotionAttrOldPort.setStatus("current")


class _WwpLeosFlowMacMotionAttrOldVlan_Type(Integer32):
    """Custom type wwpLeosFlowMacMotionAttrOldVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_WwpLeosFlowMacMotionAttrOldVlan_Type.__name__ = "Integer32"
_WwpLeosFlowMacMotionAttrOldVlan_Object = MibScalar
wwpLeosFlowMacMotionAttrOldVlan = _WwpLeosFlowMacMotionAttrOldVlan_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 2, 2),
    _WwpLeosFlowMacMotionAttrOldVlan_Type()
)
wwpLeosFlowMacMotionAttrOldVlan.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wwpLeosFlowMacMotionAttrOldVlan.setStatus("current")


class _WwpLeosFlowMacMotionAttrNewPort_Type(Integer32):
    """Custom type wwpLeosFlowMacMotionAttrNewPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_WwpLeosFlowMacMotionAttrNewPort_Type.__name__ = "Integer32"
_WwpLeosFlowMacMotionAttrNewPort_Object = MibScalar
wwpLeosFlowMacMotionAttrNewPort = _WwpLeosFlowMacMotionAttrNewPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 2, 3),
    _WwpLeosFlowMacMotionAttrNewPort_Type()
)
wwpLeosFlowMacMotionAttrNewPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wwpLeosFlowMacMotionAttrNewPort.setStatus("current")


class _WwpLeosFlowMacMotionAttrNewVlan_Type(Integer32):
    """Custom type wwpLeosFlowMacMotionAttrNewVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_WwpLeosFlowMacMotionAttrNewVlan_Type.__name__ = "Integer32"
_WwpLeosFlowMacMotionAttrNewVlan_Object = MibScalar
wwpLeosFlowMacMotionAttrNewVlan = _WwpLeosFlowMacMotionAttrNewVlan_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 2, 4),
    _WwpLeosFlowMacMotionAttrNewVlan_Type()
)
wwpLeosFlowMacMotionAttrNewVlan.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wwpLeosFlowMacMotionAttrNewVlan.setStatus("current")
_WwpLeosFlowMacMotionAttrMacAddr_Type = MacAddress
_WwpLeosFlowMacMotionAttrMacAddr_Object = MibScalar
wwpLeosFlowMacMotionAttrMacAddr = _WwpLeosFlowMacMotionAttrMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 1, 2, 5),
    _WwpLeosFlowMacMotionAttrMacAddr_Type()
)
wwpLeosFlowMacMotionAttrMacAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wwpLeosFlowMacMotionAttrMacAddr.setStatus("current")
_WwpLeosFlowNotificationPrefix_ObjectIdentity = ObjectIdentity
wwpLeosFlowNotificationPrefix = _WwpLeosFlowNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 2)
)
_WwpLeosFlowNotifications_ObjectIdentity = ObjectIdentity
wwpLeosFlowNotifications = _WwpLeosFlowNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 2, 0)
)
_WwpLeosFlowMIBConformance_ObjectIdentity = ObjectIdentity
wwpLeosFlowMIBConformance = _WwpLeosFlowMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 3)
)
_WwpLeosFlowMIBCompliances_ObjectIdentity = ObjectIdentity
wwpLeosFlowMIBCompliances = _WwpLeosFlowMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 3, 1)
)
_WwpLeosFlowMIBGroups_ObjectIdentity = ObjectIdentity
wwpLeosFlowMIBGroups = _WwpLeosFlowMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 3, 2)
)

# Managed Objects groups


# Notification objects

wwpLeosFlowServiceLevelPortOverProvisionedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 2, 0, 1)
)
wwpLeosFlowServiceLevelPortOverProvisionedTrap.setObjects(
    ("WWP-LEOS-FLOW-MIB", "wwpLeosFlowServiceLevelPort")
)
if mibBuilder.loadTexts:
    wwpLeosFlowServiceLevelPortOverProvisionedTrap.setStatus(
        "current"
    )

wwpLeosFlowServiceLevelPortUnderProvisionedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 2, 0, 2)
)
wwpLeosFlowServiceLevelPortUnderProvisionedTrap.setObjects(
    ("WWP-LEOS-FLOW-MIB", "wwpLeosFlowServiceLevelPort")
)
if mibBuilder.loadTexts:
    wwpLeosFlowServiceLevelPortUnderProvisionedTrap.setStatus(
        "current"
    )

wwpLeosFlowL2SacHighThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 2, 0, 3)
)
wwpLeosFlowL2SacHighThreshold.setObjects(
      *(("WWP-LEOS-FLOW-MIB", "wwpLeosFlowL2SacPortId"),
        ("WWP-LEOS-FLOW-MIB", "wwpLeosFlowL2SacNetType"),
        ("WWP-LEOS-FLOW-MIB", "wwpLeosFlowSacNetValue"))
)
if mibBuilder.loadTexts:
    wwpLeosFlowL2SacHighThreshold.setStatus(
        "current"
    )

wwpLeosFlowL2SacNormalThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 2, 0, 4)
)
wwpLeosFlowL2SacNormalThreshold.setObjects(
      *(("WWP-LEOS-FLOW-MIB", "wwpLeosFlowL2SacPortId"),
        ("WWP-LEOS-FLOW-MIB", "wwpLeosFlowL2SacNetType"),
        ("WWP-LEOS-FLOW-MIB", "wwpLeosFlowSacNetValue"))
)
if mibBuilder.loadTexts:
    wwpLeosFlowL2SacNormalThreshold.setStatus(
        "current"
    )

wwpLeosFlowMacMotionNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 6, 2, 0, 5)
)
wwpLeosFlowMacMotionNotification.setObjects(
      *(("WWP-LEOS-FLOW-MIB", "wwpLeosFlowMacMotionAttrOldPort"),
        ("WWP-LEOS-FLOW-MIB", "wwpLeosFlowMacMotionAttrOldVlan"),
        ("WWP-LEOS-FLOW-MIB", "wwpLeosFlowMacMotionAttrNewPort"),
        ("WWP-LEOS-FLOW-MIB", "wwpLeosFlowMacMotionAttrNewVlan"),
        ("WWP-LEOS-FLOW-MIB", "wwpLeosFlowMacMotionAttrMacAddr"))
)
if mibBuilder.loadTexts:
    wwpLeosFlowMacMotionNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-LEOS-FLOW-MIB",
    **{"PriorityMapping": PriorityMapping,
       "wwpLeosFlowMIB": wwpLeosFlowMIB,
       "wwpLeosFlowMIBObjects": wwpLeosFlowMIBObjects,
       "wwpLeosFlow": wwpLeosFlow,
       "wwpLeosFlowAgeTime": wwpLeosFlowAgeTime,
       "wwpLeosFlowAgeTimeState": wwpLeosFlowAgeTimeState,
       "wwpLeosFlowServiceLevelTable": wwpLeosFlowServiceLevelTable,
       "wwpLeosFlowServiceLevelEntry": wwpLeosFlowServiceLevelEntry,
       "wwpLeosFlowServiceLevelDirection": wwpLeosFlowServiceLevelDirection,
       "wwpLeosFlowServiceLevelPort": wwpLeosFlowServiceLevelPort,
       "wwpLeosFlowServiceLevelId": wwpLeosFlowServiceLevelId,
       "wwpLeosFlowServiceLevelName": wwpLeosFlowServiceLevelName,
       "wwpLeosFlowServiceLevelPriority": wwpLeosFlowServiceLevelPriority,
       "wwpLeosFlowServiceLevelQueueSize": wwpLeosFlowServiceLevelQueueSize,
       "wwpLeosFlowServiceLevelDropEligibility": wwpLeosFlowServiceLevelDropEligibility,
       "wwpLeosFlowServiceLevelShareEligibility": wwpLeosFlowServiceLevelShareEligibility,
       "wwpLeosFlowServiceLevelCirBW": wwpLeosFlowServiceLevelCirBW,
       "wwpLeosFlowServiceLevelPirBW": wwpLeosFlowServiceLevelPirBW,
       "wwpLeosFlowServiceStatus": wwpLeosFlowServiceStatus,
       "wwpLeosFlowServiceRedCurveId": wwpLeosFlowServiceRedCurveId,
       "wwpLeosFlowServiceLevelQueueSizeYellow": wwpLeosFlowServiceLevelQueueSizeYellow,
       "wwpLeosFlowServiceLevelQueueSizeRed": wwpLeosFlowServiceLevelQueueSizeRed,
       "wwpLeosFlowServiceLevelFlowGroup": wwpLeosFlowServiceLevelFlowGroup,
       "wwpLeosFlowServiceMappingTable": wwpLeosFlowServiceMappingTable,
       "wwpLeosFlowServiceMappingEntry": wwpLeosFlowServiceMappingEntry,
       "wwpLeosFlowServiceMapVid": wwpLeosFlowServiceMapVid,
       "wwpLeosFlowServiceMapSrcPort": wwpLeosFlowServiceMapSrcPort,
       "wwpLeosFlowServiceMapSrcTag": wwpLeosFlowServiceMapSrcTag,
       "wwpLeosFlowServiceMapDstPort": wwpLeosFlowServiceMapDstPort,
       "wwpLeosFlowServiceMapDstTag": wwpLeosFlowServiceMapDstTag,
       "wwpLeosFlowServiceMapSrcPri": wwpLeosFlowServiceMapSrcPri,
       "wwpLeosFlowServiceMapProtocolType": wwpLeosFlowServiceMapProtocolType,
       "wwpLeosFlowServiceMapProtocolPortNum": wwpLeosFlowServiceMapProtocolPortNum,
       "wwpLeosFlowServiceMapDstSlidId": wwpLeosFlowServiceMapDstSlidId,
       "wwpLeosFlowServiceMapSrcSlidId": wwpLeosFlowServiceMapSrcSlidId,
       "wwpLeosFlowServiceMapPriRemarkStatus": wwpLeosFlowServiceMapPriRemarkStatus,
       "wwpLeosFlowServiceMapRemarkPri": wwpLeosFlowServiceMapRemarkPri,
       "wwpLeosFlowServiceMapStatus": wwpLeosFlowServiceMapStatus,
       "wwpLeosFlowServiceACTable": wwpLeosFlowServiceACTable,
       "wwpLeosFlowServiceACEntry": wwpLeosFlowServiceACEntry,
       "wwpLeosFlowServiceACPortId": wwpLeosFlowServiceACPortId,
       "wwpLeosFlowServiceACVid": wwpLeosFlowServiceACVid,
       "wwpLeosFlowServiceACMaxDynamicMacCount": wwpLeosFlowServiceACMaxDynamicMacCount,
       "wwpLeosFlowServiceACDynamicNonFilteredMacCount": wwpLeosFlowServiceACDynamicNonFilteredMacCount,
       "wwpLeosFlowServiceACDynamicFilteredMacCount": wwpLeosFlowServiceACDynamicFilteredMacCount,
       "wwpLeosFlowServiceACStatus": wwpLeosFlowServiceACStatus,
       "wwpLeosFlowServiceACForwardLearning": wwpLeosFlowServiceACForwardLearning,
       "wwpLeosFlowStaticMacTable": wwpLeosFlowStaticMacTable,
       "wwpLeosFlowStaticMacEntry": wwpLeosFlowStaticMacEntry,
       "wwpLeosFlowSMVid": wwpLeosFlowSMVid,
       "wwpLeosFlowSMMacAddr": wwpLeosFlowSMMacAddr,
       "wwpLeosFlowSMPortId": wwpLeosFlowSMPortId,
       "wwpLeosFlowSMTag": wwpLeosFlowSMTag,
       "wwpLeosFlowSMStatus": wwpLeosFlowSMStatus,
       "wwpLeosFlowLearnTable": wwpLeosFlowLearnTable,
       "wwpLeosFlowLearnEntry": wwpLeosFlowLearnEntry,
       "wwpLeosFlowLearnVid": wwpLeosFlowLearnVid,
       "wwpLeosFlowLearnAddr": wwpLeosFlowLearnAddr,
       "wwpLeosFlowLearnSrcPort": wwpLeosFlowLearnSrcPort,
       "wwpLeosFlowLearnSrcTag": wwpLeosFlowLearnSrcTag,
       "wwpLeosFlowLearnSrcPri": wwpLeosFlowLearnSrcPri,
       "wwpLeosFlowLearnAddrType": wwpLeosFlowLearnAddrType,
       "wwpLeosFlowLearnDstPort": wwpLeosFlowLearnDstPort,
       "wwpLeosFlowLearnDstTag": wwpLeosFlowLearnDstTag,
       "wwpLeosFlowLearnType": wwpLeosFlowLearnType,
       "wwpLeosFlowLearnIsFiltered": wwpLeosFlowLearnIsFiltered,
       "wwpLeosFlowServiceStatsTable": wwpLeosFlowServiceStatsTable,
       "wwpLeosFlowServiceStatsEntry": wwpLeosFlowServiceStatsEntry,
       "wwpLeosFlowServiceStatsRxHi": wwpLeosFlowServiceStatsRxHi,
       "wwpLeosFlowServiceStatsRxLo": wwpLeosFlowServiceStatsRxLo,
       "wwpLeosFlowServiceStatsTxHi": wwpLeosFlowServiceStatsTxHi,
       "wwpLeosFlowServiceStatsTxLo": wwpLeosFlowServiceStatsTxLo,
       "wwpLeosFlowServiceStatsType": wwpLeosFlowServiceStatsType,
       "wwpLeosFlowMacFindTable": wwpLeosFlowMacFindTable,
       "wwpLeosFlowMacFindEntry": wwpLeosFlowMacFindEntry,
       "wwpLeosFlowMacFindMacAddr": wwpLeosFlowMacFindMacAddr,
       "wwpLeosFlowMacFindVlanId": wwpLeosFlowMacFindVlanId,
       "wwpLeosFlowMacFindPort": wwpLeosFlowMacFindPort,
       "wwpLeosFlowMacFindVlanTag": wwpLeosFlowMacFindVlanTag,
       "wwpLeosFlowPriRemapTable": wwpLeosFlowPriRemapTable,
       "wwpLeosFlowPriRemapEntry": wwpLeosFlowPriRemapEntry,
       "wwpLeosFlowUserPri": wwpLeosFlowUserPri,
       "wwpLeosFlowRemappedPri": wwpLeosFlowRemappedPri,
       "wwpLeosFlowSMappingTable": wwpLeosFlowSMappingTable,
       "wwpLeosFlowSMappingEntry": wwpLeosFlowSMappingEntry,
       "wwpLeosFlowSMappingNetType": wwpLeosFlowSMappingNetType,
       "wwpLeosFlowSMappingNetValue": wwpLeosFlowSMappingNetValue,
       "wwpLeosFlowSMappingSrcType": wwpLeosFlowSMappingSrcType,
       "wwpLeosFlowSMappingSrcValue": wwpLeosFlowSMappingSrcValue,
       "wwpLeosFlowSMappingDstType": wwpLeosFlowSMappingDstType,
       "wwpLeosFlowSMappingDstValue": wwpLeosFlowSMappingDstValue,
       "wwpLeosFlowSMappingCosType": wwpLeosFlowSMappingCosType,
       "wwpLeosFlowSMappingCosValue": wwpLeosFlowSMappingCosValue,
       "wwpLeosFlowSMappingDstSlid": wwpLeosFlowSMappingDstSlid,
       "wwpLeosFlowSMappingSrcSlid": wwpLeosFlowSMappingSrcSlid,
       "wwpLeosFlowSMappingStatus": wwpLeosFlowSMappingStatus,
       "wwpLeosFlowSMappingRedCurveOffset": wwpLeosFlowSMappingRedCurveOffset,
       "wwpLeosFlowSMappingCpuPort": wwpLeosFlowSMappingCpuPort,
       "wwpLeosFlowSMappingStatsTable": wwpLeosFlowSMappingStatsTable,
       "wwpLeosFlowSMappingStatsEntry": wwpLeosFlowSMappingStatsEntry,
       "wwpLeosFlowSMappingStatsRxHi": wwpLeosFlowSMappingStatsRxHi,
       "wwpLeosFlowSMappingStatsRxLo": wwpLeosFlowSMappingStatsRxLo,
       "wwpLeosFlowSMappingStatsTxHi": wwpLeosFlowSMappingStatsTxHi,
       "wwpLeosFlowSMappingStatsTxLo": wwpLeosFlowSMappingStatsTxLo,
       "wwpLeosFlowSMappingStatsType": wwpLeosFlowSMappingStatsType,
       "wwpLeosFlowCosSync1dToExpTable": wwpLeosFlowCosSync1dToExpTable,
       "wwpLeosFlowCosSync1dToExpEntry": wwpLeosFlowCosSync1dToExpEntry,
       "wwpLeosFlowCosSync1dToExpMapFrom": wwpLeosFlowCosSync1dToExpMapFrom,
       "wwpLeosFlowCosSync1dToExpMapTo": wwpLeosFlowCosSync1dToExpMapTo,
       "wwpLeosFlowCosSyncExpTo1dTable": wwpLeosFlowCosSyncExpTo1dTable,
       "wwpLeosFlowCosSyncExpTo1dEntry": wwpLeosFlowCosSyncExpTo1dEntry,
       "wwpLeosFlowCosSyncExpTo1dMapFrom": wwpLeosFlowCosSyncExpTo1dMapFrom,
       "wwpLeosFlowCosSyncExpTo1dMapTo": wwpLeosFlowCosSyncExpTo1dMapTo,
       "wwpLeosFlowCosSyncIpPrecTo1dTable": wwpLeosFlowCosSyncIpPrecTo1dTable,
       "wwpLeosFlowCosSyncIpPrecTo1dEntry": wwpLeosFlowCosSyncIpPrecTo1dEntry,
       "wwpLeosFlowCosSyncIpPrecTo1dMapFrom": wwpLeosFlowCosSyncIpPrecTo1dMapFrom,
       "wwpLeosFlowCosSyncIpPrecTo1dMapTo": wwpLeosFlowCosSyncIpPrecTo1dMapTo,
       "wwpLeosFlowCosSyncStdPhbTo1dTable": wwpLeosFlowCosSyncStdPhbTo1dTable,
       "wwpLeosFlowCosSyncStdPhbTo1dEntry": wwpLeosFlowCosSyncStdPhbTo1dEntry,
       "wwpLeosFlowCosSyncStdPhbTo1dMapFrom": wwpLeosFlowCosSyncStdPhbTo1dMapFrom,
       "wwpLeosFlowCosSyncStdPhbTo1dMapTo": wwpLeosFlowCosSyncStdPhbTo1dMapTo,
       "wwpLeosFlowL2SacTable": wwpLeosFlowL2SacTable,
       "wwpLeosFlowL2SacEntry": wwpLeosFlowL2SacEntry,
       "wwpLeosFlowL2SacPortId": wwpLeosFlowL2SacPortId,
       "wwpLeosFlowL2SacNetType": wwpLeosFlowL2SacNetType,
       "wwpLeosFlowSacNetValue": wwpLeosFlowSacNetValue,
       "wwpLeosFlowL2SacLimit": wwpLeosFlowL2SacLimit,
       "wwpLeosFlowL2SacCurMac": wwpLeosFlowL2SacCurMac,
       "wwpLeosFlowL2SacCurFilteredMac": wwpLeosFlowL2SacCurFilteredMac,
       "wwpLeosFlowL2SacOperState": wwpLeosFlowL2SacOperState,
       "wwpLeosFlowL2SacRowStatus": wwpLeosFlowL2SacRowStatus,
       "wwpLeosFlowL2SacTrapState": wwpLeosFlowL2SacTrapState,
       "wwpLeosFlowStrictQueuingState": wwpLeosFlowStrictQueuingState,
       "wwpLeosFlowBwCalcMode": wwpLeosFlowBwCalcMode,
       "wwpLeosFlowGlobal": wwpLeosFlowGlobal,
       "wwpLeosFlowServiceLevelFlowGroupState": wwpLeosFlowServiceLevelFlowGroupState,
       "wwpLeosFlowServiceMappingCosRedMappingState": wwpLeosFlowServiceMappingCosRedMappingState,
       "wwpLeosFlowServiceAllRedCurveUnset": wwpLeosFlowServiceAllRedCurveUnset,
       "wwpLeosFlowServiceRedCurveTable": wwpLeosFlowServiceRedCurveTable,
       "wwpLeosFlowServiceRedCurveEntry": wwpLeosFlowServiceRedCurveEntry,
       "wwpLeosFlowServiceRedCurveIndex": wwpLeosFlowServiceRedCurveIndex,
       "wwpLeosFlowServiceRedCurveName": wwpLeosFlowServiceRedCurveName,
       "wwpLeosFlowServiceRedCurveState": wwpLeosFlowServiceRedCurveState,
       "wwpLeosFlowServiceRedCurveMinThreshold": wwpLeosFlowServiceRedCurveMinThreshold,
       "wwpLeosFlowServiceRedCurveMaxThreshold": wwpLeosFlowServiceRedCurveMaxThreshold,
       "wwpLeosFlowServiceRedCurveDropProbability": wwpLeosFlowServiceRedCurveDropProbability,
       "wwpLeosFlowServiceRedCurveUnset": wwpLeosFlowServiceRedCurveUnset,
       "wwpLeosFlowCos1dToRedCurveOffsetTable": wwpLeosFlowCos1dToRedCurveOffsetTable,
       "wwpLeosFlowCos1dToRedCurveOffsetEntry": wwpLeosFlowCos1dToRedCurveOffsetEntry,
       "wwpLeosFlowCos1dToRedCurveOffset1dValue": wwpLeosFlowCos1dToRedCurveOffset1dValue,
       "wwpLeosFlowCos1dToRedCurveOffsetValue": wwpLeosFlowCos1dToRedCurveOffsetValue,
       "wwpLeosFlowCosMapPCPTo1dTable": wwpLeosFlowCosMapPCPTo1dTable,
       "wwpLeosFlowCosMapPCPTo1dEntry": wwpLeosFlowCosMapPCPTo1dEntry,
       "wwpLeosFlowCosMapPCPTo1dMapFrom": wwpLeosFlowCosMapPCPTo1dMapFrom,
       "wwpLeosFlowCosMapPCPTo1dMapTo": wwpLeosFlowCosMapPCPTo1dMapTo,
       "wwpLeosFlowCosMap1dToPCPTable": wwpLeosFlowCosMap1dToPCPTable,
       "wwpLeosFlowCosMap1dToPCPEntry": wwpLeosFlowCosMap1dToPCPEntry,
       "wwpLeosFlowCosMap1dToPCPMapFrom": wwpLeosFlowCosMap1dToPCPMapFrom,
       "wwpLeosFlowCosMap1dToPCPMapTo": wwpLeosFlowCosMap1dToPCPMapTo,
       "wwpLeosFlowMacMotionEventsEnable": wwpLeosFlowMacMotionEventsEnable,
       "wwpLeosFlowMacMotionEventsInterval": wwpLeosFlowMacMotionEventsInterval,
       "wwpLeosFlowCpuRateLimitsEnable": wwpLeosFlowCpuRateLimitsEnable,
       "wwpLeosFlowCpuRateLimitTable": wwpLeosFlowCpuRateLimitTable,
       "wwpLeosFlowCpuRateLimitEntry": wwpLeosFlowCpuRateLimitEntry,
       "wwpLeosFlowCpuRateLimitPort": wwpLeosFlowCpuRateLimitPort,
       "wwpLeosFlowCpuRateLimitEnable": wwpLeosFlowCpuRateLimitEnable,
       "wwpLeosFlowCpuRateLimitBootp": wwpLeosFlowCpuRateLimitBootp,
       "wwpLeosFlowCpuRateLimitCfm": wwpLeosFlowCpuRateLimitCfm,
       "wwpLeosFlowCpuRateLimitCft": wwpLeosFlowCpuRateLimitCft,
       "wwpLeosFlowCpuRateLimitDot1x": wwpLeosFlowCpuRateLimitDot1x,
       "wwpLeosFlowCpuRateLimitOam": wwpLeosFlowCpuRateLimitOam,
       "wwpLeosFlowCpuRateLimitEprArp": wwpLeosFlowCpuRateLimitEprArp,
       "wwpLeosFlowCpuRateLimitIgmp": wwpLeosFlowCpuRateLimitIgmp,
       "wwpLeosFlowCpuRateLimitInet": wwpLeosFlowCpuRateLimitInet,
       "wwpLeosFlowCpuRateLimitLacp": wwpLeosFlowCpuRateLimitLacp,
       "wwpLeosFlowCpuRateLimitLldp": wwpLeosFlowCpuRateLimitLldp,
       "wwpLeosFlowCpuRateLimitMpls": wwpLeosFlowCpuRateLimitMpls,
       "wwpLeosFlowCpuRateLimitMstp": wwpLeosFlowCpuRateLimitMstp,
       "wwpLeosFlowCpuRateLimitPeArp": wwpLeosFlowCpuRateLimitPeArp,
       "wwpLeosFlowCpuRateLimitPvst": wwpLeosFlowCpuRateLimitPvst,
       "wwpLeosFlowCpuRateLimitRstp": wwpLeosFlowCpuRateLimitRstp,
       "wwpLeosFlowCpuRateLimitLpbk": wwpLeosFlowCpuRateLimitLpbk,
       "wwpLeosFlowCpuRateLimitRmtLpbk": wwpLeosFlowCpuRateLimitRmtLpbk,
       "wwpLeosFlowCpuRateLimitCxeRx": wwpLeosFlowCpuRateLimitCxeRx,
       "wwpLeosFlowCpuRateLimitCxeTx": wwpLeosFlowCpuRateLimitCxeTx,
       "wwpLeosFlowCpuRateLimitTwamp": wwpLeosFlowCpuRateLimitTwamp,
       "wwpLeosFlowCpuRateLimitDflt": wwpLeosFlowCpuRateLimitDflt,
       "wwpLeosFlowCpuRateLimitTwampRsp": wwpLeosFlowCpuRateLimitTwampRsp,
       "wwpLeosFlowCpuRateLimitMultiCast": wwpLeosFlowCpuRateLimitMultiCast,
       "wwpLeosFlowCpuRateLimitBroadCast": wwpLeosFlowCpuRateLimitBroadCast,
       "wwpLeosFlowCpuRateLimitArp": wwpLeosFlowCpuRateLimitArp,
       "wwpLeosFlowCpuRateLimitIcmp": wwpLeosFlowCpuRateLimitIcmp,
       "wwpLeosFlowCpuRateLimitTcpSyn": wwpLeosFlowCpuRateLimitTcpSyn,
       "wwpLeosFlowCpuRateLimitRaps": wwpLeosFlowCpuRateLimitRaps,
       "wwpLeosFlowCpuRateLimitIpMgmt": wwpLeosFlowCpuRateLimitIpMgmt,
       "wwpLeosFlowCpuRateLimitIpControl": wwpLeosFlowCpuRateLimitIpControl,
       "wwpLeosFlowCpuRateLimitIpV6Mgmt": wwpLeosFlowCpuRateLimitIpV6Mgmt,
       "wwpLeosFlowCpuRateLimitInet6": wwpLeosFlowCpuRateLimitInet6,
       "wwpLeosFlowCpuRateLimitStatsTable": wwpLeosFlowCpuRateLimitStatsTable,
       "wwpLeosFlowCpuRateLimitStatsEntry": wwpLeosFlowCpuRateLimitStatsEntry,
       "wwpLeosFlowCpuRateLimitStatsPort": wwpLeosFlowCpuRateLimitStatsPort,
       "wwpLeosFlowCpuRateLimitStatsBootpPassed": wwpLeosFlowCpuRateLimitStatsBootpPassed,
       "wwpLeosFlowCpuRateLimitStatsCfmPassed": wwpLeosFlowCpuRateLimitStatsCfmPassed,
       "wwpLeosFlowCpuRateLimitStatsCftPassed": wwpLeosFlowCpuRateLimitStatsCftPassed,
       "wwpLeosFlowCpuRateLimitStatsDot1xPassed": wwpLeosFlowCpuRateLimitStatsDot1xPassed,
       "wwpLeosFlowCpuRateLimitStatsOamPassed": wwpLeosFlowCpuRateLimitStatsOamPassed,
       "wwpLeosFlowCpuRateLimitStatsEprArpPassed": wwpLeosFlowCpuRateLimitStatsEprArpPassed,
       "wwpLeosFlowCpuRateLimitStatsIgmpPassed": wwpLeosFlowCpuRateLimitStatsIgmpPassed,
       "wwpLeosFlowCpuRateLimitStatsInetPassed": wwpLeosFlowCpuRateLimitStatsInetPassed,
       "wwpLeosFlowCpuRateLimitStatsLacpPassed": wwpLeosFlowCpuRateLimitStatsLacpPassed,
       "wwpLeosFlowCpuRateLimitStatsLldpPassed": wwpLeosFlowCpuRateLimitStatsLldpPassed,
       "wwpLeosFlowCpuRateLimitStatsMplsPassed": wwpLeosFlowCpuRateLimitStatsMplsPassed,
       "wwpLeosFlowCpuRateLimitStatsMstpPassed": wwpLeosFlowCpuRateLimitStatsMstpPassed,
       "wwpLeosFlowCpuRateLimitStatsPeArpPassed": wwpLeosFlowCpuRateLimitStatsPeArpPassed,
       "wwpLeosFlowCpuRateLimitStatsPvstPassed": wwpLeosFlowCpuRateLimitStatsPvstPassed,
       "wwpLeosFlowCpuRateLimitStatsRstpPassed": wwpLeosFlowCpuRateLimitStatsRstpPassed,
       "wwpLeosFlowCpuRateLimitStatsLpbkPassed": wwpLeosFlowCpuRateLimitStatsLpbkPassed,
       "wwpLeosFlowCpuRateLimitStatsRmtLpbkPassed": wwpLeosFlowCpuRateLimitStatsRmtLpbkPassed,
       "wwpLeosFlowCpuRateLimitStatsCxeRxPassed": wwpLeosFlowCpuRateLimitStatsCxeRxPassed,
       "wwpLeosFlowCpuRateLimitStatsCxeTxPassed": wwpLeosFlowCpuRateLimitStatsCxeTxPassed,
       "wwpLeosFlowCpuRateLimitStatsTwampPassed": wwpLeosFlowCpuRateLimitStatsTwampPassed,
       "wwpLeosFlowCpuRateLimitStatsDfltPassed": wwpLeosFlowCpuRateLimitStatsDfltPassed,
       "wwpLeosFlowCpuRateLimitStatsBootpDropped": wwpLeosFlowCpuRateLimitStatsBootpDropped,
       "wwpLeosFlowCpuRateLimitStatsCfmDropped": wwpLeosFlowCpuRateLimitStatsCfmDropped,
       "wwpLeosFlowCpuRateLimitStatsCftDropped": wwpLeosFlowCpuRateLimitStatsCftDropped,
       "wwpLeosFlowCpuRateLimitStatsDot1xDropped": wwpLeosFlowCpuRateLimitStatsDot1xDropped,
       "wwpLeosFlowCpuRateLimitStatsOamDropped": wwpLeosFlowCpuRateLimitStatsOamDropped,
       "wwpLeosFlowCpuRateLimitStatsEprArpDropped": wwpLeosFlowCpuRateLimitStatsEprArpDropped,
       "wwpLeosFlowCpuRateLimitStatsIgmpDropped": wwpLeosFlowCpuRateLimitStatsIgmpDropped,
       "wwpLeosFlowCpuRateLimitStatsInetDropped": wwpLeosFlowCpuRateLimitStatsInetDropped,
       "wwpLeosFlowCpuRateLimitStatsLacpDropped": wwpLeosFlowCpuRateLimitStatsLacpDropped,
       "wwpLeosFlowCpuRateLimitStatsLldpDropped": wwpLeosFlowCpuRateLimitStatsLldpDropped,
       "wwpLeosFlowCpuRateLimitStatsMplsDropped": wwpLeosFlowCpuRateLimitStatsMplsDropped,
       "wwpLeosFlowCpuRateLimitStatsMstpDropped": wwpLeosFlowCpuRateLimitStatsMstpDropped,
       "wwpLeosFlowCpuRateLimitStatsPeArpDropped": wwpLeosFlowCpuRateLimitStatsPeArpDropped,
       "wwpLeosFlowCpuRateLimitStatsPvstDropped": wwpLeosFlowCpuRateLimitStatsPvstDropped,
       "wwpLeosFlowCpuRateLimitStatsRstpDropped": wwpLeosFlowCpuRateLimitStatsRstpDropped,
       "wwpLeosFlowCpuRateLimitStatsLpbkDropped": wwpLeosFlowCpuRateLimitStatsLpbkDropped,
       "wwpLeosFlowCpuRateLimitStatsRmtLpbkDropped": wwpLeosFlowCpuRateLimitStatsRmtLpbkDropped,
       "wwpLeosFlowCpuRateLimitStatsCxeRxDropped": wwpLeosFlowCpuRateLimitStatsCxeRxDropped,
       "wwpLeosFlowCpuRateLimitStatsCxeTxDropped": wwpLeosFlowCpuRateLimitStatsCxeTxDropped,
       "wwpLeosFlowCpuRateLimitStatsTwampDropped": wwpLeosFlowCpuRateLimitStatsTwampDropped,
       "wwpLeosFlowCpuRateLimitStatsDfltDropped": wwpLeosFlowCpuRateLimitStatsDfltDropped,
       "wwpLeosFlowCpuRateLimitStatsTwampRspPassed": wwpLeosFlowCpuRateLimitStatsTwampRspPassed,
       "wwpLeosFlowCpuRateLimitStatsTwampRspDropped": wwpLeosFlowCpuRateLimitStatsTwampRspDropped,
       "wwpLeosFlowCpuRateLimitStatsMultiCastPassed": wwpLeosFlowCpuRateLimitStatsMultiCastPassed,
       "wwpLeosFlowCpuRateLimitStatsMultiCastDropped": wwpLeosFlowCpuRateLimitStatsMultiCastDropped,
       "wwpLeosFlowCpuRateLimitStatsBroadCastPassed": wwpLeosFlowCpuRateLimitStatsBroadCastPassed,
       "wwpLeosFlowCpuRateLimitStatsBroadCastDropped": wwpLeosFlowCpuRateLimitStatsBroadCastDropped,
       "wwpLeosFlowCpuRateLimitStatsArpPassed": wwpLeosFlowCpuRateLimitStatsArpPassed,
       "wwpLeosFlowCpuRateLimitStatsArpDropped": wwpLeosFlowCpuRateLimitStatsArpDropped,
       "wwpLeosFlowCpuRateLimitStatsIcmpPassed": wwpLeosFlowCpuRateLimitStatsIcmpPassed,
       "wwpLeosFlowCpuRateLimitStatsIcmpDropped": wwpLeosFlowCpuRateLimitStatsIcmpDropped,
       "wwpLeosFlowCpuRateLimitStatsTcpSynPassed": wwpLeosFlowCpuRateLimitStatsTcpSynPassed,
       "wwpLeosFlowCpuRateLimitStatsTcpSynDropped": wwpLeosFlowCpuRateLimitStatsTcpSynDropped,
       "wwpLeosFlowCpuRateLimitStatsRapsPassed": wwpLeosFlowCpuRateLimitStatsRapsPassed,
       "wwpLeosFlowCpuRateLimitStatsRapsDropped": wwpLeosFlowCpuRateLimitStatsRapsDropped,
       "wwpLeosFlowCpuRateLimitStatsIpMgmtPassed": wwpLeosFlowCpuRateLimitStatsIpMgmtPassed,
       "wwpLeosFlowCpuRateLimitStatsIpMgmtDropped": wwpLeosFlowCpuRateLimitStatsIpMgmtDropped,
       "wwpLeosFlowCpuRateLimitStatsIpControlPassed": wwpLeosFlowCpuRateLimitStatsIpControlPassed,
       "wwpLeosFlowCpuRateLimitStatsIpControlDropped": wwpLeosFlowCpuRateLimitStatsIpControlDropped,
       "wwpLeosFlowCpuRateLimitStatsIpV6MgmtPassed": wwpLeosFlowCpuRateLimitStatsIpV6MgmtPassed,
       "wwpLeosFlowCpuRateLimitStatsIpV6MgmtDropped": wwpLeosFlowCpuRateLimitStatsIpV6MgmtDropped,
       "wwpLeosFlowCpuRateLimitStatsInet6Passed": wwpLeosFlowCpuRateLimitStatsInet6Passed,
       "wwpLeosFlowCpuRateLimitStatsInet6Dropped": wwpLeosFlowCpuRateLimitStatsInet6Dropped,
       "wwpLeosFlowCpuRateLimitStatsClearTable": wwpLeosFlowCpuRateLimitStatsClearTable,
       "wwpLeosFlowCpuRateLimitStatsClearEntry": wwpLeosFlowCpuRateLimitStatsClearEntry,
       "wwpLeosFlowCpuRateLimitStatsClearPort": wwpLeosFlowCpuRateLimitStatsClearPort,
       "wwpLeosFlowCpuRateLimitStatsClear": wwpLeosFlowCpuRateLimitStatsClear,
       "wwpLeosFlowServiceTotalStatsTable": wwpLeosFlowServiceTotalStatsTable,
       "wwpLeosFlowServiceTotalStatsEntry": wwpLeosFlowServiceTotalStatsEntry,
       "wwpLeosFlowServiceTotalStatsRxHi": wwpLeosFlowServiceTotalStatsRxHi,
       "wwpLeosFlowServiceTotalStatsRxLo": wwpLeosFlowServiceTotalStatsRxLo,
       "wwpLeosFlowServiceTotalStatsTxHi": wwpLeosFlowServiceTotalStatsTxHi,
       "wwpLeosFlowServiceTotalStatsTxLo": wwpLeosFlowServiceTotalStatsTxLo,
       "wwpLeosFlowServiceTotalStatsType": wwpLeosFlowServiceTotalStatsType,
       "wwpLeosFlowPortServiceLevelTable": wwpLeosFlowPortServiceLevelTable,
       "wwpLeosFlowPortServiceLevelEntry": wwpLeosFlowPortServiceLevelEntry,
       "wwpLeosFlowPortServiceLevelPort": wwpLeosFlowPortServiceLevelPort,
       "wwpLeosFlowPortServiceLevelMaxBandwidth": wwpLeosFlowPortServiceLevelMaxBandwidth,
       "wwpLeosFlowPortServiceLevelQueueSize": wwpLeosFlowPortServiceLevelQueueSize,
       "wwpLeosFlowPortServiceLevelQueueSizeYellow": wwpLeosFlowPortServiceLevelQueueSizeYellow,
       "wwpLeosFlowPortServiceLevelQueueSizeRed": wwpLeosFlowPortServiceLevelQueueSizeRed,
       "wwpLeosFlowPortServiceLevelFlowGroup": wwpLeosFlowPortServiceLevelFlowGroup,
       "wwpLeosFlowPortServiceLevelRedCurve": wwpLeosFlowPortServiceLevelRedCurve,
       "wwpLeosFlowBurstConfigBacklogLimit": wwpLeosFlowBurstConfigBacklogLimit,
       "wwpLeosFlowBurstConfigMulticastLimit": wwpLeosFlowBurstConfigMulticastLimit,
       "wwpLeosFlowBurstConfigVlanPriFltrOnThld": wwpLeosFlowBurstConfigVlanPriFltrOnThld,
       "wwpLeosFlowBurstConfigVlanPriFltrOffThld": wwpLeosFlowBurstConfigVlanPriFltrOffThld,
       "wwpLeosFlowBurstConfigVlanPriFltrPriMatch": wwpLeosFlowBurstConfigVlanPriFltrPriMatch,
       "wwpLeosFlowBurstConfigVlanPriFltrState": wwpLeosFlowBurstConfigVlanPriFltrState,
       "wwpLeosFlowNotifAttrs": wwpLeosFlowNotifAttrs,
       "wwpLeosFlowMacMotionAttrOldPort": wwpLeosFlowMacMotionAttrOldPort,
       "wwpLeosFlowMacMotionAttrOldVlan": wwpLeosFlowMacMotionAttrOldVlan,
       "wwpLeosFlowMacMotionAttrNewPort": wwpLeosFlowMacMotionAttrNewPort,
       "wwpLeosFlowMacMotionAttrNewVlan": wwpLeosFlowMacMotionAttrNewVlan,
       "wwpLeosFlowMacMotionAttrMacAddr": wwpLeosFlowMacMotionAttrMacAddr,
       "wwpLeosFlowNotificationPrefix": wwpLeosFlowNotificationPrefix,
       "wwpLeosFlowNotifications": wwpLeosFlowNotifications,
       "wwpLeosFlowServiceLevelPortOverProvisionedTrap": wwpLeosFlowServiceLevelPortOverProvisionedTrap,
       "wwpLeosFlowServiceLevelPortUnderProvisionedTrap": wwpLeosFlowServiceLevelPortUnderProvisionedTrap,
       "wwpLeosFlowL2SacHighThreshold": wwpLeosFlowL2SacHighThreshold,
       "wwpLeosFlowL2SacNormalThreshold": wwpLeosFlowL2SacNormalThreshold,
       "wwpLeosFlowMacMotionNotification": wwpLeosFlowMacMotionNotification,
       "wwpLeosFlowMIBConformance": wwpLeosFlowMIBConformance,
       "wwpLeosFlowMIBCompliances": wwpLeosFlowMIBCompliances,
       "wwpLeosFlowMIBGroups": wwpLeosFlowMIBGroups}
)
