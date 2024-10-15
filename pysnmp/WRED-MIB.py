# SNMP MIB module (WRED-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WRED-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:20 2024
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

(dlink_common_mgmt,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlink-common-mgmt")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

swWredMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 31)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwWredCtrl_ObjectIdentity = ObjectIdentity
swWredCtrl = _SwWredCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 31, 1)
)


class _SwWredGlobalState_Type(Integer32):
    """Custom type swWredGlobalState based on Integer32"""
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
          ("enabled", 3),
          ("other", 1))
    )


_SwWredGlobalState_Type.__name__ = "Integer32"
_SwWredGlobalState_Object = MibScalar
swWredGlobalState = _SwWredGlobalState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 31, 1, 1),
    _SwWredGlobalState_Type()
)
swWredGlobalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swWredGlobalState.setStatus("current")
_SwWredInfo_ObjectIdentity = ObjectIdentity
swWredInfo = _SwWredInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 31, 2)
)
_SwWredMgmt_ObjectIdentity = ObjectIdentity
swWredMgmt = _SwWredMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 31, 3)
)
_SwWredAverageTimeTable_Object = MibTable
swWredAverageTimeTable = _SwWredAverageTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 31, 3, 1)
)
if mibBuilder.loadTexts:
    swWredAverageTimeTable.setStatus("current")
_SwWredAverageTimeEntry_Object = MibTableRow
swWredAverageTimeEntry = _SwWredAverageTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 31, 3, 1, 1)
)
swWredAverageTimeEntry.setIndexNames(
    (0, "WRED-MIB", "swWredPortIndex"),
)
if mibBuilder.loadTexts:
    swWredAverageTimeEntry.setStatus("current")


class _SwWredPortIndex_Type(Integer32):
    """Custom type swWredPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwWredPortIndex_Type.__name__ = "Integer32"
_SwWredPortIndex_Object = MibTableColumn
swWredPortIndex = _SwWredPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 31, 3, 1, 1, 1),
    _SwWredPortIndex_Type()
)
swWredPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swWredPortIndex.setStatus("current")


class _SwWredAverageTime_Type(Integer32):
    """Custom type swWredAverageTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32768),
    )


_SwWredAverageTime_Type.__name__ = "Integer32"
_SwWredAverageTime_Object = MibTableColumn
swWredAverageTime = _SwWredAverageTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 31, 3, 1, 1, 2),
    _SwWredAverageTime_Type()
)
swWredAverageTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swWredAverageTime.setStatus("current")
_SwWredCtrlTable_Object = MibTable
swWredCtrlTable = _SwWredCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 31, 3, 2)
)
if mibBuilder.loadTexts:
    swWredCtrlTable.setStatus("current")
_SwWredCtrlEntry_Object = MibTableRow
swWredCtrlEntry = _SwWredCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 31, 3, 2, 1)
)
swWredCtrlEntry.setIndexNames(
    (0, "WRED-MIB", "swWredCtrlPortIndex"),
    (0, "WRED-MIB", "swWredCtrlClassIndex"),
)
if mibBuilder.loadTexts:
    swWredCtrlEntry.setStatus("current")


class _SwWredCtrlPortIndex_Type(Integer32):
    """Custom type swWredCtrlPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwWredCtrlPortIndex_Type.__name__ = "Integer32"
_SwWredCtrlPortIndex_Object = MibTableColumn
swWredCtrlPortIndex = _SwWredCtrlPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 31, 3, 2, 1, 1),
    _SwWredCtrlPortIndex_Type()
)
swWredCtrlPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swWredCtrlPortIndex.setStatus("current")


class _SwWredCtrlClassIndex_Type(Integer32):
    """Custom type swWredCtrlClassIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SwWredCtrlClassIndex_Type.__name__ = "Integer32"
_SwWredCtrlClassIndex_Object = MibTableColumn
swWredCtrlClassIndex = _SwWredCtrlClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 31, 3, 2, 1, 2),
    _SwWredCtrlClassIndex_Type()
)
swWredCtrlClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swWredCtrlClassIndex.setStatus("current")


class _SwWredCtrlDropStart_Type(Integer32):
    """Custom type swWredCtrlDropStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SwWredCtrlDropStart_Type.__name__ = "Integer32"
_SwWredCtrlDropStart_Object = MibTableColumn
swWredCtrlDropStart = _SwWredCtrlDropStart_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 31, 3, 2, 1, 3),
    _SwWredCtrlDropStart_Type()
)
swWredCtrlDropStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swWredCtrlDropStart.setStatus("current")


class _SwWredCtrlDropSlope_Type(Integer32):
    """Custom type swWredCtrlDropSlope based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 90),
    )


_SwWredCtrlDropSlope_Type.__name__ = "Integer32"
_SwWredCtrlDropSlope_Object = MibTableColumn
swWredCtrlDropSlope = _SwWredCtrlDropSlope_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 31, 3, 2, 1, 4),
    _SwWredCtrlDropSlope_Type()
)
swWredCtrlDropSlope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swWredCtrlDropSlope.setStatus("current")


class _SwWredAllPortAverageTime_Type(Integer32):
    """Custom type swWredAllPortAverageTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32768),
    )


_SwWredAllPortAverageTime_Type.__name__ = "Integer32"
_SwWredAllPortAverageTime_Object = MibScalar
swWredAllPortAverageTime = _SwWredAllPortAverageTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 31, 3, 3),
    _SwWredAllPortAverageTime_Type()
)
swWredAllPortAverageTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swWredAllPortAverageTime.setStatus("current")
_SwWredProfileTable_Object = MibTable
swWredProfileTable = _SwWredProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 31, 3, 4)
)
if mibBuilder.loadTexts:
    swWredProfileTable.setStatus("current")
_SwWredProfileEntry_Object = MibTableRow
swWredProfileEntry = _SwWredProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 31, 3, 4, 1)
)
swWredProfileEntry.setIndexNames(
    (0, "WRED-MIB", "swWredProfileIndex"),
)
if mibBuilder.loadTexts:
    swWredProfileEntry.setStatus("current")
_SwWredProfileIndex_Type = Integer32
_SwWredProfileIndex_Object = MibTableColumn
swWredProfileIndex = _SwWredProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 31, 3, 4, 1, 1),
    _SwWredProfileIndex_Type()
)
swWredProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swWredProfileIndex.setStatus("current")
_SwWredProfileName_Type = DisplayString
_SwWredProfileName_Object = MibTableColumn
swWredProfileName = _SwWredProfileName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 31, 3, 4, 1, 2),
    _SwWredProfileName_Type()
)
swWredProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swWredProfileName.setStatus("current")
_SwWredProfileRowStatus_Type = RowStatus
_SwWredProfileRowStatus_Object = MibTableColumn
swWredProfileRowStatus = _SwWredProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 31, 3, 4, 1, 3),
    _SwWredProfileRowStatus_Type()
)
swWredProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swWredProfileRowStatus.setStatus("current")
_SwWredProfileCfgTable_Object = MibTable
swWredProfileCfgTable = _SwWredProfileCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 31, 3, 5)
)
if mibBuilder.loadTexts:
    swWredProfileCfgTable.setStatus("current")
_SwWredProfileCfgEntry_Object = MibTableRow
swWredProfileCfgEntry = _SwWredProfileCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 31, 3, 5, 1)
)
swWredProfileCfgEntry.setIndexNames(
    (0, "WRED-MIB", "swWredProfileCfgIndex"),
    (0, "WRED-MIB", "swWredProfileCfgPacketType"),
    (0, "WRED-MIB", "swWredProfileCfgPacketColor"),
)
if mibBuilder.loadTexts:
    swWredProfileCfgEntry.setStatus("current")


class _SwWredProfileCfgIndex_Type(Integer32):
    """Custom type swWredProfileCfgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_SwWredProfileCfgIndex_Type.__name__ = "Integer32"
_SwWredProfileCfgIndex_Object = MibTableColumn
swWredProfileCfgIndex = _SwWredProfileCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 31, 3, 5, 1, 1),
    _SwWredProfileCfgIndex_Type()
)
swWredProfileCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swWredProfileCfgIndex.setStatus("current")


class _SwWredProfileCfgPacketType_Type(Integer32):
    """Custom type swWredProfileCfgPacketType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonTcp", 2),
          ("tcp", 1))
    )


_SwWredProfileCfgPacketType_Type.__name__ = "Integer32"
_SwWredProfileCfgPacketType_Object = MibTableColumn
swWredProfileCfgPacketType = _SwWredProfileCfgPacketType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 31, 3, 5, 1, 2),
    _SwWredProfileCfgPacketType_Type()
)
swWredProfileCfgPacketType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swWredProfileCfgPacketType.setStatus("current")


class _SwWredProfileCfgPacketColor_Type(Integer32):
    """Custom type swWredProfileCfgPacketColor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("green", 1),
          ("red", 3),
          ("yellow", 2))
    )


_SwWredProfileCfgPacketColor_Type.__name__ = "Integer32"
_SwWredProfileCfgPacketColor_Object = MibTableColumn
swWredProfileCfgPacketColor = _SwWredProfileCfgPacketColor_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 31, 3, 5, 1, 3),
    _SwWredProfileCfgPacketColor_Type()
)
swWredProfileCfgPacketColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swWredProfileCfgPacketColor.setStatus("current")


class _SwWredProfileCfgMinThreshold_Type(Integer32):
    """Custom type swWredProfileCfgMinThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SwWredProfileCfgMinThreshold_Type.__name__ = "Integer32"
_SwWredProfileCfgMinThreshold_Object = MibTableColumn
swWredProfileCfgMinThreshold = _SwWredProfileCfgMinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 31, 3, 5, 1, 4),
    _SwWredProfileCfgMinThreshold_Type()
)
swWredProfileCfgMinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swWredProfileCfgMinThreshold.setStatus("current")


class _SwWredProfileCfgMaxThreshold_Type(Integer32):
    """Custom type swWredProfileCfgMaxThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SwWredProfileCfgMaxThreshold_Type.__name__ = "Integer32"
_SwWredProfileCfgMaxThreshold_Object = MibTableColumn
swWredProfileCfgMaxThreshold = _SwWredProfileCfgMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 31, 3, 5, 1, 5),
    _SwWredProfileCfgMaxThreshold_Type()
)
swWredProfileCfgMaxThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swWredProfileCfgMaxThreshold.setStatus("current")


class _SwWredProfileCfgMaxDropRate_Type(Integer32):
    """Custom type swWredProfileCfgMaxDropRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SwWredProfileCfgMaxDropRate_Type.__name__ = "Integer32"
_SwWredProfileCfgMaxDropRate_Object = MibTableColumn
swWredProfileCfgMaxDropRate = _SwWredProfileCfgMaxDropRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 31, 3, 5, 1, 6),
    _SwWredProfileCfgMaxDropRate_Type()
)
swWredProfileCfgMaxDropRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swWredProfileCfgMaxDropRate.setStatus("current")
_SwWredPortProfileTable_Object = MibTable
swWredPortProfileTable = _SwWredPortProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 31, 3, 6)
)
if mibBuilder.loadTexts:
    swWredPortProfileTable.setStatus("current")
_SwWredPortProfileEntry_Object = MibTableRow
swWredPortProfileEntry = _SwWredPortProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 31, 3, 6, 1)
)
swWredPortProfileEntry.setIndexNames(
    (0, "WRED-MIB", "swWredPortProfilePortIndex"),
    (0, "WRED-MIB", "swWredPortProfileClassIndex"),
)
if mibBuilder.loadTexts:
    swWredPortProfileEntry.setStatus("current")


class _SwWredPortProfilePortIndex_Type(Integer32):
    """Custom type swWredPortProfilePortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwWredPortProfilePortIndex_Type.__name__ = "Integer32"
_SwWredPortProfilePortIndex_Object = MibTableColumn
swWredPortProfilePortIndex = _SwWredPortProfilePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 31, 3, 6, 1, 1),
    _SwWredPortProfilePortIndex_Type()
)
swWredPortProfilePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swWredPortProfilePortIndex.setStatus("current")


class _SwWredPortProfileClassIndex_Type(Integer32):
    """Custom type swWredPortProfileClassIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SwWredPortProfileClassIndex_Type.__name__ = "Integer32"
_SwWredPortProfileClassIndex_Object = MibTableColumn
swWredPortProfileClassIndex = _SwWredPortProfileClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 31, 3, 6, 1, 2),
    _SwWredPortProfileClassIndex_Type()
)
swWredPortProfileClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swWredPortProfileClassIndex.setStatus("current")
_SwWredPortProfileId_Type = Integer32
_SwWredPortProfileId_Object = MibTableColumn
swWredPortProfileId = _SwWredPortProfileId_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 31, 3, 6, 1, 3),
    _SwWredPortProfileId_Type()
)
swWredPortProfileId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swWredPortProfileId.setStatus("current")
_SwWredPortWeightNum_Type = Integer32
_SwWredPortWeightNum_Object = MibTableColumn
swWredPortWeightNum = _SwWredPortWeightNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 31, 3, 6, 1, 4),
    _SwWredPortWeightNum_Type()
)
swWredPortWeightNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swWredPortWeightNum.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WRED-MIB",
    **{"swWredMIB": swWredMIB,
       "swWredCtrl": swWredCtrl,
       "swWredGlobalState": swWredGlobalState,
       "swWredInfo": swWredInfo,
       "swWredMgmt": swWredMgmt,
       "swWredAverageTimeTable": swWredAverageTimeTable,
       "swWredAverageTimeEntry": swWredAverageTimeEntry,
       "swWredPortIndex": swWredPortIndex,
       "swWredAverageTime": swWredAverageTime,
       "swWredCtrlTable": swWredCtrlTable,
       "swWredCtrlEntry": swWredCtrlEntry,
       "swWredCtrlPortIndex": swWredCtrlPortIndex,
       "swWredCtrlClassIndex": swWredCtrlClassIndex,
       "swWredCtrlDropStart": swWredCtrlDropStart,
       "swWredCtrlDropSlope": swWredCtrlDropSlope,
       "swWredAllPortAverageTime": swWredAllPortAverageTime,
       "swWredProfileTable": swWredProfileTable,
       "swWredProfileEntry": swWredProfileEntry,
       "swWredProfileIndex": swWredProfileIndex,
       "swWredProfileName": swWredProfileName,
       "swWredProfileRowStatus": swWredProfileRowStatus,
       "swWredProfileCfgTable": swWredProfileCfgTable,
       "swWredProfileCfgEntry": swWredProfileCfgEntry,
       "swWredProfileCfgIndex": swWredProfileCfgIndex,
       "swWredProfileCfgPacketType": swWredProfileCfgPacketType,
       "swWredProfileCfgPacketColor": swWredProfileCfgPacketColor,
       "swWredProfileCfgMinThreshold": swWredProfileCfgMinThreshold,
       "swWredProfileCfgMaxThreshold": swWredProfileCfgMaxThreshold,
       "swWredProfileCfgMaxDropRate": swWredProfileCfgMaxDropRate,
       "swWredPortProfileTable": swWredPortProfileTable,
       "swWredPortProfileEntry": swWredPortProfileEntry,
       "swWredPortProfilePortIndex": swWredPortProfilePortIndex,
       "swWredPortProfileClassIndex": swWredPortProfileClassIndex,
       "swWredPortProfileId": swWredPortProfileId,
       "swWredPortWeightNum": swWredPortWeightNum}
)
