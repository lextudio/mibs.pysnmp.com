# SNMP MIB module (ACD-SMAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACD-SMAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:33:25 2024
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

(acdMibs,) = mibBuilder.importSymbols(
    "ACCEDIAN-SMI",
    "acdMibs")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

acdSmap = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8)
)
acdSmap.setRevisions(
        ("2008-10-01 01:00",
         "2008-06-15 01:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AcdSmapNotifications_ObjectIdentity = ObjectIdentity
acdSmapNotifications = _AcdSmapNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 0)
)
_AcdSmapMIBObjects_ObjectIdentity = ObjectIdentity
acdSmapMIBObjects = _AcdSmapMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 1)
)
_AcdSmapConfig_ObjectIdentity = ObjectIdentity
acdSmapConfig = _AcdSmapConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1)
)
_AcdSmapCoSProfTable_Object = MibTable
acdSmapCoSProfTable = _AcdSmapCoSProfTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 1)
)
if mibBuilder.loadTexts:
    acdSmapCoSProfTable.setStatus("current")
_AcdSmapCoSProfEntry_Object = MibTableRow
acdSmapCoSProfEntry = _AcdSmapCoSProfEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 1, 1)
)
acdSmapCoSProfEntry.setIndexNames(
    (0, "ACD-SMAP-MIB", "acdSmapCoSProfID"),
)
if mibBuilder.loadTexts:
    acdSmapCoSProfEntry.setStatus("current")
_AcdSmapCoSProfID_Type = Unsigned32
_AcdSmapCoSProfID_Object = MibTableColumn
acdSmapCoSProfID = _AcdSmapCoSProfID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 1, 1, 1),
    _AcdSmapCoSProfID_Type()
)
acdSmapCoSProfID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdSmapCoSProfID.setStatus("current")
_AcdSmapCoSProfRowStatus_Type = RowStatus
_AcdSmapCoSProfRowStatus_Object = MibTableColumn
acdSmapCoSProfRowStatus = _AcdSmapCoSProfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 1, 1, 2),
    _AcdSmapCoSProfRowStatus_Type()
)
acdSmapCoSProfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapCoSProfRowStatus.setStatus("current")


class _AcdSmapCoSProfName_Type(DisplayString):
    """Custom type acdSmapCoSProfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AcdSmapCoSProfName_Type.__name__ = "DisplayString"
_AcdSmapCoSProfName_Object = MibTableColumn
acdSmapCoSProfName = _AcdSmapCoSProfName_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 1, 1, 3),
    _AcdSmapCoSProfName_Type()
)
acdSmapCoSProfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapCoSProfName.setStatus("current")


class _AcdSmapCoSProfType_Type(Integer32):
    """Custom type acdSmapCoSProfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dscp", 2),
          ("pcp", 1),
          ("pre", 3))
    )


_AcdSmapCoSProfType_Type.__name__ = "Integer32"
_AcdSmapCoSProfType_Object = MibTableColumn
acdSmapCoSProfType = _AcdSmapCoSProfType_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 1, 1, 4),
    _AcdSmapCoSProfType_Type()
)
acdSmapCoSProfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapCoSProfType.setStatus("current")


class _AcdSmapCoSProfDecodeDropBit_Type(TruthValue):
    """Custom type acdSmapCoSProfDecodeDropBit based on TruthValue"""


_AcdSmapCoSProfDecodeDropBit_Object = MibTableColumn
acdSmapCoSProfDecodeDropBit = _AcdSmapCoSProfDecodeDropBit_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 1, 1, 5),
    _AcdSmapCoSProfDecodeDropBit_Type()
)
acdSmapCoSProfDecodeDropBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapCoSProfDecodeDropBit.setStatus("current")


class _AcdSmapCoSProfEncodeDropBit_Type(TruthValue):
    """Custom type acdSmapCoSProfEncodeDropBit based on TruthValue"""


_AcdSmapCoSProfEncodeDropBit_Object = MibTableColumn
acdSmapCoSProfEncodeDropBit = _AcdSmapCoSProfEncodeDropBit_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 1, 1, 6),
    _AcdSmapCoSProfEncodeDropBit_Type()
)
acdSmapCoSProfEncodeDropBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapCoSProfEncodeDropBit.setStatus("current")
_AcdSmapCoSProfCodePointTable_Object = MibTable
acdSmapCoSProfCodePointTable = _AcdSmapCoSProfCodePointTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 2)
)
if mibBuilder.loadTexts:
    acdSmapCoSProfCodePointTable.setStatus("current")
_AcdSmapCoSProfCodePointEntry_Object = MibTableRow
acdSmapCoSProfCodePointEntry = _AcdSmapCoSProfCodePointEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 2, 1)
)
acdSmapCoSProfCodePointEntry.setIndexNames(
    (0, "ACD-SMAP-MIB", "acdSmapCoSProfID"),
    (0, "ACD-SMAP-MIB", "acdSmapCoSProfCodePointID"),
)
if mibBuilder.loadTexts:
    acdSmapCoSProfCodePointEntry.setStatus("current")


class _AcdSmapCoSProfCodePointID_Type(Unsigned32):
    """Custom type acdSmapCoSProfCodePointID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AcdSmapCoSProfCodePointID_Type.__name__ = "Unsigned32"
_AcdSmapCoSProfCodePointID_Object = MibTableColumn
acdSmapCoSProfCodePointID = _AcdSmapCoSProfCodePointID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 2, 1, 1),
    _AcdSmapCoSProfCodePointID_Type()
)
acdSmapCoSProfCodePointID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdSmapCoSProfCodePointID.setStatus("current")


class _AcdSmapCoSProfCodePointPreMarkingColor_Type(Integer32):
    """Custom type acdSmapCoSProfCodePointPreMarkingColor based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("green", 1),
          ("yellow", 2))
    )


_AcdSmapCoSProfCodePointPreMarkingColor_Type.__name__ = "Integer32"
_AcdSmapCoSProfCodePointPreMarkingColor_Object = MibTableColumn
acdSmapCoSProfCodePointPreMarkingColor = _AcdSmapCoSProfCodePointPreMarkingColor_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 2, 1, 2),
    _AcdSmapCoSProfCodePointPreMarkingColor_Type()
)
acdSmapCoSProfCodePointPreMarkingColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdSmapCoSProfCodePointPreMarkingColor.setStatus("current")


class _AcdSmapCoSProfCodePointGreenOut_Type(Unsigned32):
    """Custom type acdSmapCoSProfCodePointGreenOut based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AcdSmapCoSProfCodePointGreenOut_Type.__name__ = "Unsigned32"
_AcdSmapCoSProfCodePointGreenOut_Object = MibTableColumn
acdSmapCoSProfCodePointGreenOut = _AcdSmapCoSProfCodePointGreenOut_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 2, 1, 3),
    _AcdSmapCoSProfCodePointGreenOut_Type()
)
acdSmapCoSProfCodePointGreenOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdSmapCoSProfCodePointGreenOut.setStatus("current")


class _AcdSmapCoSProfCodePointYellowOut_Type(Unsigned32):
    """Custom type acdSmapCoSProfCodePointYellowOut based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AcdSmapCoSProfCodePointYellowOut_Type.__name__ = "Unsigned32"
_AcdSmapCoSProfCodePointYellowOut_Object = MibTableColumn
acdSmapCoSProfCodePointYellowOut = _AcdSmapCoSProfCodePointYellowOut_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 2, 1, 4),
    _AcdSmapCoSProfCodePointYellowOut_Type()
)
acdSmapCoSProfCodePointYellowOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdSmapCoSProfCodePointYellowOut.setStatus("current")
_AcdSmapRegSetTable_Object = MibTable
acdSmapRegSetTable = _AcdSmapRegSetTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 3)
)
if mibBuilder.loadTexts:
    acdSmapRegSetTable.setStatus("current")
_AcdSmapRegSetEntry_Object = MibTableRow
acdSmapRegSetEntry = _AcdSmapRegSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 3, 1)
)
acdSmapRegSetEntry.setIndexNames(
    (0, "ACD-SMAP-MIB", "acdSmapRegSetID"),
)
if mibBuilder.loadTexts:
    acdSmapRegSetEntry.setStatus("current")
_AcdSmapRegSetID_Type = Unsigned32
_AcdSmapRegSetID_Object = MibTableColumn
acdSmapRegSetID = _AcdSmapRegSetID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 3, 1, 1),
    _AcdSmapRegSetID_Type()
)
acdSmapRegSetID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdSmapRegSetID.setStatus("current")
_AcdSmapRegSetRowStatus_Type = RowStatus
_AcdSmapRegSetRowStatus_Object = MibTableColumn
acdSmapRegSetRowStatus = _AcdSmapRegSetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 3, 1, 2),
    _AcdSmapRegSetRowStatus_Type()
)
acdSmapRegSetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapRegSetRowStatus.setStatus("current")


class _AcdSmapRegSetName_Type(DisplayString):
    """Custom type acdSmapRegSetName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AcdSmapRegSetName_Type.__name__ = "DisplayString"
_AcdSmapRegSetName_Object = MibTableColumn
acdSmapRegSetName = _AcdSmapRegSetName_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 3, 1, 3),
    _AcdSmapRegSetName_Type()
)
acdSmapRegSetName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapRegSetName.setStatus("current")


class _AcdSmapRegSetType_Type(Integer32):
    """Custom type acdSmapRegSetType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dscp", 2),
          ("pcp", 1),
          ("pre", 3))
    )


_AcdSmapRegSetType_Type.__name__ = "Integer32"
_AcdSmapRegSetType_Object = MibTableColumn
acdSmapRegSetType = _AcdSmapRegSetType_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 3, 1, 4),
    _AcdSmapRegSetType_Type()
)
acdSmapRegSetType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acdSmapRegSetType.setStatus("current")
_AcdSmapRegSetCodePointTable_Object = MibTable
acdSmapRegSetCodePointTable = _AcdSmapRegSetCodePointTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 4)
)
if mibBuilder.loadTexts:
    acdSmapRegSetCodePointTable.setStatus("current")
_AcdSmapRegSetCodePointEntry_Object = MibTableRow
acdSmapRegSetCodePointEntry = _AcdSmapRegSetCodePointEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 4, 1)
)
acdSmapRegSetCodePointEntry.setIndexNames(
    (0, "ACD-SMAP-MIB", "acdSmapRegSetID"),
    (0, "ACD-SMAP-MIB", "acdSmapRegSetCodePointID"),
)
if mibBuilder.loadTexts:
    acdSmapRegSetCodePointEntry.setStatus("current")


class _AcdSmapRegSetCodePointID_Type(Unsigned32):
    """Custom type acdSmapRegSetCodePointID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AcdSmapRegSetCodePointID_Type.__name__ = "Unsigned32"
_AcdSmapRegSetCodePointID_Object = MibTableColumn
acdSmapRegSetCodePointID = _AcdSmapRegSetCodePointID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 4, 1, 1),
    _AcdSmapRegSetCodePointID_Type()
)
acdSmapRegSetCodePointID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdSmapRegSetCodePointID.setStatus("current")


class _AcdSmapRegSetCodePointRegulatorID_Type(Unsigned32):
    """Custom type acdSmapRegSetCodePointRegulatorID based on Unsigned32"""
    defaultValue = 0


_AcdSmapRegSetCodePointRegulatorID_Object = MibTableColumn
acdSmapRegSetCodePointRegulatorID = _AcdSmapRegSetCodePointRegulatorID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 4, 1, 2),
    _AcdSmapRegSetCodePointRegulatorID_Type()
)
acdSmapRegSetCodePointRegulatorID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdSmapRegSetCodePointRegulatorID.setStatus("current")


class _AcdSmapRegSetCodePointRegulatorEnable_Type(TruthValue):
    """Custom type acdSmapRegSetCodePointRegulatorEnable based on TruthValue"""


_AcdSmapRegSetCodePointRegulatorEnable_Object = MibTableColumn
acdSmapRegSetCodePointRegulatorEnable = _AcdSmapRegSetCodePointRegulatorEnable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 4, 1, 3),
    _AcdSmapRegSetCodePointRegulatorEnable_Type()
)
acdSmapRegSetCodePointRegulatorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdSmapRegSetCodePointRegulatorEnable.setStatus("current")
_AcdSmapConformance_ObjectIdentity = ObjectIdentity
acdSmapConformance = _AcdSmapConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 2)
)
_AcdSmapCompliances_ObjectIdentity = ObjectIdentity
acdSmapCompliances = _AcdSmapCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 2, 1)
)
_AcdSmapGroups_ObjectIdentity = ObjectIdentity
acdSmapGroups = _AcdSmapGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 2, 2)
)

# Managed Objects groups

acdSmapCoSProfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 2, 2, 1)
)
acdSmapCoSProfGroup.setObjects(
      *(("ACD-SMAP-MIB", "acdSmapCoSProfRowStatus"),
        ("ACD-SMAP-MIB", "acdSmapCoSProfName"),
        ("ACD-SMAP-MIB", "acdSmapCoSProfType"),
        ("ACD-SMAP-MIB", "acdSmapCoSProfDecodeDropBit"),
        ("ACD-SMAP-MIB", "acdSmapCoSProfEncodeDropBit"))
)
if mibBuilder.loadTexts:
    acdSmapCoSProfGroup.setStatus("current")

acdSmapCoSProfCodePointGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 2, 2, 2)
)
acdSmapCoSProfCodePointGroup.setObjects(
      *(("ACD-SMAP-MIB", "acdSmapCoSProfCodePointPreMarkingColor"),
        ("ACD-SMAP-MIB", "acdSmapCoSProfCodePointGreenOut"),
        ("ACD-SMAP-MIB", "acdSmapCoSProfCodePointYellowOut"))
)
if mibBuilder.loadTexts:
    acdSmapCoSProfCodePointGroup.setStatus("current")

acdSmapRegSetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 2, 2, 3)
)
acdSmapRegSetGroup.setObjects(
      *(("ACD-SMAP-MIB", "acdSmapRegSetRowStatus"),
        ("ACD-SMAP-MIB", "acdSmapRegSetName"),
        ("ACD-SMAP-MIB", "acdSmapRegSetType"))
)
if mibBuilder.loadTexts:
    acdSmapRegSetGroup.setStatus("current")

acdSmapRegSetCodePointGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 2, 2, 4)
)
acdSmapRegSetCodePointGroup.setObjects(
      *(("ACD-SMAP-MIB", "acdSmapRegSetCodePointRegulatorID"),
        ("ACD-SMAP-MIB", "acdSmapRegSetCodePointRegulatorEnable"))
)
if mibBuilder.loadTexts:
    acdSmapRegSetCodePointGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

acdSmapCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 22420, 2, 8, 2, 1, 1)
)
if mibBuilder.loadTexts:
    acdSmapCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACD-SMAP-MIB",
    **{"acdSmap": acdSmap,
       "acdSmapNotifications": acdSmapNotifications,
       "acdSmapMIBObjects": acdSmapMIBObjects,
       "acdSmapConfig": acdSmapConfig,
       "acdSmapCoSProfTable": acdSmapCoSProfTable,
       "acdSmapCoSProfEntry": acdSmapCoSProfEntry,
       "acdSmapCoSProfID": acdSmapCoSProfID,
       "acdSmapCoSProfRowStatus": acdSmapCoSProfRowStatus,
       "acdSmapCoSProfName": acdSmapCoSProfName,
       "acdSmapCoSProfType": acdSmapCoSProfType,
       "acdSmapCoSProfDecodeDropBit": acdSmapCoSProfDecodeDropBit,
       "acdSmapCoSProfEncodeDropBit": acdSmapCoSProfEncodeDropBit,
       "acdSmapCoSProfCodePointTable": acdSmapCoSProfCodePointTable,
       "acdSmapCoSProfCodePointEntry": acdSmapCoSProfCodePointEntry,
       "acdSmapCoSProfCodePointID": acdSmapCoSProfCodePointID,
       "acdSmapCoSProfCodePointPreMarkingColor": acdSmapCoSProfCodePointPreMarkingColor,
       "acdSmapCoSProfCodePointGreenOut": acdSmapCoSProfCodePointGreenOut,
       "acdSmapCoSProfCodePointYellowOut": acdSmapCoSProfCodePointYellowOut,
       "acdSmapRegSetTable": acdSmapRegSetTable,
       "acdSmapRegSetEntry": acdSmapRegSetEntry,
       "acdSmapRegSetID": acdSmapRegSetID,
       "acdSmapRegSetRowStatus": acdSmapRegSetRowStatus,
       "acdSmapRegSetName": acdSmapRegSetName,
       "acdSmapRegSetType": acdSmapRegSetType,
       "acdSmapRegSetCodePointTable": acdSmapRegSetCodePointTable,
       "acdSmapRegSetCodePointEntry": acdSmapRegSetCodePointEntry,
       "acdSmapRegSetCodePointID": acdSmapRegSetCodePointID,
       "acdSmapRegSetCodePointRegulatorID": acdSmapRegSetCodePointRegulatorID,
       "acdSmapRegSetCodePointRegulatorEnable": acdSmapRegSetCodePointRegulatorEnable,
       "acdSmapConformance": acdSmapConformance,
       "acdSmapCompliances": acdSmapCompliances,
       "acdSmapCompliance": acdSmapCompliance,
       "acdSmapGroups": acdSmapGroups,
       "acdSmapCoSProfGroup": acdSmapCoSProfGroup,
       "acdSmapCoSProfCodePointGroup": acdSmapCoSProfCodePointGroup,
       "acdSmapRegSetGroup": acdSmapRegSetGroup,
       "acdSmapRegSetCodePointGroup": acdSmapRegSetCodePointGroup}
)
