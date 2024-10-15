# SNMP MIB module (H3C-MPLSOAM-PS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H3C-MPLSOAM-PS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:50:58 2024
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

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

h3cMplsOamPs = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 80)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cMplsOamPsScalarGroup_ObjectIdentity = ObjectIdentity
h3cMplsOamPsScalarGroup = _H3cMplsOamPsScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 80, 1)
)


class _H3cMplsOamPsTrapOpen_Type(TruthValue):
    """Custom type h3cMplsOamPsTrapOpen based on TruthValue"""


_H3cMplsOamPsTrapOpen_Object = MibScalar
h3cMplsOamPsTrapOpen = _H3cMplsOamPsTrapOpen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 80, 1, 1),
    _H3cMplsOamPsTrapOpen_Type()
)
h3cMplsOamPsTrapOpen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cMplsOamPsTrapOpen.setStatus("current")
_H3cMplsOamPsTable_ObjectIdentity = ObjectIdentity
h3cMplsOamPsTable = _H3cMplsOamPsTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 80, 2)
)
_H3cMplsPsTable_Object = MibTable
h3cMplsPsTable = _H3cMplsPsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 80, 2, 1)
)
if mibBuilder.loadTexts:
    h3cMplsPsTable.setStatus("current")
_H3cMplsPsEntry_Object = MibTableRow
h3cMplsPsEntry = _H3cMplsPsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 80, 2, 1, 1)
)
h3cMplsPsEntry.setIndexNames(
    (0, "H3C-MPLSOAM-PS-MIB", "h3cMplsPsIndex"),
)
if mibBuilder.loadTexts:
    h3cMplsPsEntry.setStatus("current")
_H3cMplsPsIndex_Type = Integer32
_H3cMplsPsIndex_Object = MibTableColumn
h3cMplsPsIndex = _H3cMplsPsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 80, 2, 1, 1, 1),
    _H3cMplsPsIndex_Type()
)
h3cMplsPsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cMplsPsIndex.setStatus("current")
_H3cMplsPsGroupID_Type = Integer32
_H3cMplsPsGroupID_Object = MibTableColumn
h3cMplsPsGroupID = _H3cMplsPsGroupID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 80, 2, 1, 1, 2),
    _H3cMplsPsGroupID_Type()
)
h3cMplsPsGroupID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMplsPsGroupID.setStatus("current")
_H3cMplsPsWorkLspName_Type = OctetString
_H3cMplsPsWorkLspName_Object = MibTableColumn
h3cMplsPsWorkLspName = _H3cMplsPsWorkLspName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 80, 2, 1, 1, 3),
    _H3cMplsPsWorkLspName_Type()
)
h3cMplsPsWorkLspName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMplsPsWorkLspName.setStatus("current")
_H3cMplsPsProtectLspName_Type = OctetString
_H3cMplsPsProtectLspName_Object = MibTableColumn
h3cMplsPsProtectLspName = _H3cMplsPsProtectLspName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 80, 2, 1, 1, 4),
    _H3cMplsPsProtectLspName_Type()
)
h3cMplsPsProtectLspName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMplsPsProtectLspName.setStatus("current")


class _H3cMplsPsRevertiveMode_Type(Integer32):
    """Custom type h3cMplsPsRevertiveMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_H3cMplsPsRevertiveMode_Type.__name__ = "Integer32"
_H3cMplsPsRevertiveMode_Object = MibTableColumn
h3cMplsPsRevertiveMode = _H3cMplsPsRevertiveMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 80, 2, 1, 1, 5),
    _H3cMplsPsRevertiveMode_Type()
)
h3cMplsPsRevertiveMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMplsPsRevertiveMode.setStatus("current")
_H3cMplsPsWTR_Type = Integer32
_H3cMplsPsWTR_Object = MibTableColumn
h3cMplsPsWTR = _H3cMplsPsWTR_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 80, 2, 1, 1, 6),
    _H3cMplsPsWTR_Type()
)
h3cMplsPsWTR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMplsPsWTR.setStatus("current")
if mibBuilder.loadTexts:
    h3cMplsPsWTR.setUnits("30s")
_H3cMplsPsHoldOff_Type = Integer32
_H3cMplsPsHoldOff_Object = MibTableColumn
h3cMplsPsHoldOff = _H3cMplsPsHoldOff_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 80, 2, 1, 1, 7),
    _H3cMplsPsHoldOff_Type()
)
h3cMplsPsHoldOff.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMplsPsHoldOff.setStatus("current")
if mibBuilder.loadTexts:
    h3cMplsPsHoldOff.setUnits("100ms")


class _H3cMplsPsSwitchCondition_Type(Integer32):
    """Custom type h3cMplsPsSwitchCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_H3cMplsPsSwitchCondition_Type.__name__ = "Integer32"
_H3cMplsPsSwitchCondition_Object = MibTableColumn
h3cMplsPsSwitchCondition = _H3cMplsPsSwitchCondition_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 80, 2, 1, 1, 8),
    _H3cMplsPsSwitchCondition_Type()
)
h3cMplsPsSwitchCondition.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMplsPsSwitchCondition.setStatus("current")


class _H3cMplsPsWorkLspDetectState_Type(Integer32):
    """Custom type h3cMplsPsWorkLspDetectState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_H3cMplsPsWorkLspDetectState_Type.__name__ = "Integer32"
_H3cMplsPsWorkLspDetectState_Object = MibTableColumn
h3cMplsPsWorkLspDetectState = _H3cMplsPsWorkLspDetectState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 80, 2, 1, 1, 9),
    _H3cMplsPsWorkLspDetectState_Type()
)
h3cMplsPsWorkLspDetectState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMplsPsWorkLspDetectState.setStatus("current")


class _H3cMplsPsWorkLspUpDownState_Type(Integer32):
    """Custom type h3cMplsPsWorkLspUpDownState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_H3cMplsPsWorkLspUpDownState_Type.__name__ = "Integer32"
_H3cMplsPsWorkLspUpDownState_Object = MibTableColumn
h3cMplsPsWorkLspUpDownState = _H3cMplsPsWorkLspUpDownState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 80, 2, 1, 1, 10),
    _H3cMplsPsWorkLspUpDownState_Type()
)
h3cMplsPsWorkLspUpDownState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMplsPsWorkLspUpDownState.setStatus("current")


class _H3cMplsPsProtLspDetectState_Type(Integer32):
    """Custom type h3cMplsPsProtLspDetectState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_H3cMplsPsProtLspDetectState_Type.__name__ = "Integer32"
_H3cMplsPsProtLspDetectState_Object = MibTableColumn
h3cMplsPsProtLspDetectState = _H3cMplsPsProtLspDetectState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 80, 2, 1, 1, 11),
    _H3cMplsPsProtLspDetectState_Type()
)
h3cMplsPsProtLspDetectState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMplsPsProtLspDetectState.setStatus("current")


class _H3cMplsPsProtLspUpDownState_Type(Integer32):
    """Custom type h3cMplsPsProtLspUpDownState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_H3cMplsPsProtLspUpDownState_Type.__name__ = "Integer32"
_H3cMplsPsProtLspUpDownState_Object = MibTableColumn
h3cMplsPsProtLspUpDownState = _H3cMplsPsProtLspUpDownState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 80, 2, 1, 1, 12),
    _H3cMplsPsProtLspUpDownState_Type()
)
h3cMplsPsProtLspUpDownState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMplsPsProtLspUpDownState.setStatus("current")


class _H3cMplsPsSwitchResult_Type(Integer32):
    """Custom type h3cMplsPsSwitchResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_H3cMplsPsSwitchResult_Type.__name__ = "Integer32"
_H3cMplsPsSwitchResult_Object = MibTableColumn
h3cMplsPsSwitchResult = _H3cMplsPsSwitchResult_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 80, 2, 1, 1, 13),
    _H3cMplsPsSwitchResult_Type()
)
h3cMplsPsSwitchResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMplsPsSwitchResult.setStatus("current")
_H3cMplsPsRowStatus_Type = RowStatus
_H3cMplsPsRowStatus_Object = MibTableColumn
h3cMplsPsRowStatus = _H3cMplsPsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 80, 2, 1, 1, 14),
    _H3cMplsPsRowStatus_Type()
)
h3cMplsPsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMplsPsRowStatus.setStatus("current")
_H3cMplsOamPsNotifications_ObjectIdentity = ObjectIdentity
h3cMplsOamPsNotifications = _H3cMplsOamPsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 80, 3)
)

# Managed Objects groups


# Notification objects

h3cMplsPsSwitchPtoW = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 80, 3, 1)
)
h3cMplsPsSwitchPtoW.setObjects(
      *(("H3C-MPLSOAM-PS-MIB", "h3cMplsPsWorkLspName"),
        ("H3C-MPLSOAM-PS-MIB", "h3cMplsPsProtectLspName"),
        ("H3C-MPLSOAM-PS-MIB", "h3cMplsPsSwitchResult"))
)
if mibBuilder.loadTexts:
    h3cMplsPsSwitchPtoW.setStatus(
        "current"
    )

h3cMplsPsSwitchWtoP = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 80, 3, 2)
)
h3cMplsPsSwitchWtoP.setObjects(
      *(("H3C-MPLSOAM-PS-MIB", "h3cMplsPsWorkLspName"),
        ("H3C-MPLSOAM-PS-MIB", "h3cMplsPsProtectLspName"),
        ("H3C-MPLSOAM-PS-MIB", "h3cMplsPsSwitchResult"))
)
if mibBuilder.loadTexts:
    h3cMplsPsSwitchWtoP.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-MPLSOAM-PS-MIB",
    **{"h3cMplsOamPs": h3cMplsOamPs,
       "h3cMplsOamPsScalarGroup": h3cMplsOamPsScalarGroup,
       "h3cMplsOamPsTrapOpen": h3cMplsOamPsTrapOpen,
       "h3cMplsOamPsTable": h3cMplsOamPsTable,
       "h3cMplsPsTable": h3cMplsPsTable,
       "h3cMplsPsEntry": h3cMplsPsEntry,
       "h3cMplsPsIndex": h3cMplsPsIndex,
       "h3cMplsPsGroupID": h3cMplsPsGroupID,
       "h3cMplsPsWorkLspName": h3cMplsPsWorkLspName,
       "h3cMplsPsProtectLspName": h3cMplsPsProtectLspName,
       "h3cMplsPsRevertiveMode": h3cMplsPsRevertiveMode,
       "h3cMplsPsWTR": h3cMplsPsWTR,
       "h3cMplsPsHoldOff": h3cMplsPsHoldOff,
       "h3cMplsPsSwitchCondition": h3cMplsPsSwitchCondition,
       "h3cMplsPsWorkLspDetectState": h3cMplsPsWorkLspDetectState,
       "h3cMplsPsWorkLspUpDownState": h3cMplsPsWorkLspUpDownState,
       "h3cMplsPsProtLspDetectState": h3cMplsPsProtLspDetectState,
       "h3cMplsPsProtLspUpDownState": h3cMplsPsProtLspUpDownState,
       "h3cMplsPsSwitchResult": h3cMplsPsSwitchResult,
       "h3cMplsPsRowStatus": h3cMplsPsRowStatus,
       "h3cMplsOamPsNotifications": h3cMplsOamPsNotifications,
       "h3cMplsPsSwitchPtoW": h3cMplsPsSwitchPtoW,
       "h3cMplsPsSwitchWtoP": h3cMplsPsSwitchWtoP}
)
