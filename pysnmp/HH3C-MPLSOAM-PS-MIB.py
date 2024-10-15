# SNMP MIB module (HH3C-MPLSOAM-PS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-MPLSOAM-PS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:54:13 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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

hh3cMplsOamPs = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 80)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cMplsOamPsScalarGroup_ObjectIdentity = ObjectIdentity
hh3cMplsOamPsScalarGroup = _Hh3cMplsOamPsScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 80, 1)
)


class _Hh3cMplsOamPsTrapOpen_Type(TruthValue):
    """Custom type hh3cMplsOamPsTrapOpen based on TruthValue"""


_Hh3cMplsOamPsTrapOpen_Object = MibScalar
hh3cMplsOamPsTrapOpen = _Hh3cMplsOamPsTrapOpen_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 80, 1, 1),
    _Hh3cMplsOamPsTrapOpen_Type()
)
hh3cMplsOamPsTrapOpen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMplsOamPsTrapOpen.setStatus("current")
_Hh3cMplsOamPsTable_ObjectIdentity = ObjectIdentity
hh3cMplsOamPsTable = _Hh3cMplsOamPsTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 80, 2)
)
_Hh3cMplsPsTable_Object = MibTable
hh3cMplsPsTable = _Hh3cMplsPsTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 80, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cMplsPsTable.setStatus("current")
_Hh3cMplsPsEntry_Object = MibTableRow
hh3cMplsPsEntry = _Hh3cMplsPsEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 80, 2, 1, 1)
)
hh3cMplsPsEntry.setIndexNames(
    (0, "HH3C-MPLSOAM-PS-MIB", "hh3cMplsPsIndex"),
)
if mibBuilder.loadTexts:
    hh3cMplsPsEntry.setStatus("current")
_Hh3cMplsPsIndex_Type = Integer32
_Hh3cMplsPsIndex_Object = MibTableColumn
hh3cMplsPsIndex = _Hh3cMplsPsIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 80, 2, 1, 1, 1),
    _Hh3cMplsPsIndex_Type()
)
hh3cMplsPsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMplsPsIndex.setStatus("current")
_Hh3cMplsPsGroupID_Type = Integer32
_Hh3cMplsPsGroupID_Object = MibTableColumn
hh3cMplsPsGroupID = _Hh3cMplsPsGroupID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 80, 2, 1, 1, 2),
    _Hh3cMplsPsGroupID_Type()
)
hh3cMplsPsGroupID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsPsGroupID.setStatus("current")
_Hh3cMplsPsWorkLspName_Type = OctetString
_Hh3cMplsPsWorkLspName_Object = MibTableColumn
hh3cMplsPsWorkLspName = _Hh3cMplsPsWorkLspName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 80, 2, 1, 1, 3),
    _Hh3cMplsPsWorkLspName_Type()
)
hh3cMplsPsWorkLspName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsPsWorkLspName.setStatus("current")
_Hh3cMplsPsProtectLspName_Type = OctetString
_Hh3cMplsPsProtectLspName_Object = MibTableColumn
hh3cMplsPsProtectLspName = _Hh3cMplsPsProtectLspName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 80, 2, 1, 1, 4),
    _Hh3cMplsPsProtectLspName_Type()
)
hh3cMplsPsProtectLspName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsPsProtectLspName.setStatus("current")


class _Hh3cMplsPsRevertiveMode_Type(Integer32):
    """Custom type hh3cMplsPsRevertiveMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Hh3cMplsPsRevertiveMode_Type.__name__ = "Integer32"
_Hh3cMplsPsRevertiveMode_Object = MibTableColumn
hh3cMplsPsRevertiveMode = _Hh3cMplsPsRevertiveMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 80, 2, 1, 1, 5),
    _Hh3cMplsPsRevertiveMode_Type()
)
hh3cMplsPsRevertiveMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsPsRevertiveMode.setStatus("current")
_Hh3cMplsPsWTR_Type = Integer32
_Hh3cMplsPsWTR_Object = MibTableColumn
hh3cMplsPsWTR = _Hh3cMplsPsWTR_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 80, 2, 1, 1, 6),
    _Hh3cMplsPsWTR_Type()
)
hh3cMplsPsWTR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsPsWTR.setStatus("current")
if mibBuilder.loadTexts:
    hh3cMplsPsWTR.setUnits("30s")
_Hh3cMplsPsHoldOff_Type = Integer32
_Hh3cMplsPsHoldOff_Object = MibTableColumn
hh3cMplsPsHoldOff = _Hh3cMplsPsHoldOff_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 80, 2, 1, 1, 7),
    _Hh3cMplsPsHoldOff_Type()
)
hh3cMplsPsHoldOff.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsPsHoldOff.setStatus("current")
if mibBuilder.loadTexts:
    hh3cMplsPsHoldOff.setUnits("100ms")


class _Hh3cMplsPsSwitchCondition_Type(Integer32):
    """Custom type hh3cMplsPsSwitchCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_Hh3cMplsPsSwitchCondition_Type.__name__ = "Integer32"
_Hh3cMplsPsSwitchCondition_Object = MibTableColumn
hh3cMplsPsSwitchCondition = _Hh3cMplsPsSwitchCondition_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 80, 2, 1, 1, 8),
    _Hh3cMplsPsSwitchCondition_Type()
)
hh3cMplsPsSwitchCondition.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsPsSwitchCondition.setStatus("current")


class _Hh3cMplsPsWorkLspDetectState_Type(Integer32):
    """Custom type hh3cMplsPsWorkLspDetectState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Hh3cMplsPsWorkLspDetectState_Type.__name__ = "Integer32"
_Hh3cMplsPsWorkLspDetectState_Object = MibTableColumn
hh3cMplsPsWorkLspDetectState = _Hh3cMplsPsWorkLspDetectState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 80, 2, 1, 1, 9),
    _Hh3cMplsPsWorkLspDetectState_Type()
)
hh3cMplsPsWorkLspDetectState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMplsPsWorkLspDetectState.setStatus("current")


class _Hh3cMplsPsWorkLspUpDownState_Type(Integer32):
    """Custom type hh3cMplsPsWorkLspUpDownState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Hh3cMplsPsWorkLspUpDownState_Type.__name__ = "Integer32"
_Hh3cMplsPsWorkLspUpDownState_Object = MibTableColumn
hh3cMplsPsWorkLspUpDownState = _Hh3cMplsPsWorkLspUpDownState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 80, 2, 1, 1, 10),
    _Hh3cMplsPsWorkLspUpDownState_Type()
)
hh3cMplsPsWorkLspUpDownState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMplsPsWorkLspUpDownState.setStatus("current")


class _Hh3cMplsPsProtLspDetectState_Type(Integer32):
    """Custom type hh3cMplsPsProtLspDetectState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Hh3cMplsPsProtLspDetectState_Type.__name__ = "Integer32"
_Hh3cMplsPsProtLspDetectState_Object = MibTableColumn
hh3cMplsPsProtLspDetectState = _Hh3cMplsPsProtLspDetectState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 80, 2, 1, 1, 11),
    _Hh3cMplsPsProtLspDetectState_Type()
)
hh3cMplsPsProtLspDetectState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMplsPsProtLspDetectState.setStatus("current")


class _Hh3cMplsPsProtLspUpDownState_Type(Integer32):
    """Custom type hh3cMplsPsProtLspUpDownState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Hh3cMplsPsProtLspUpDownState_Type.__name__ = "Integer32"
_Hh3cMplsPsProtLspUpDownState_Object = MibTableColumn
hh3cMplsPsProtLspUpDownState = _Hh3cMplsPsProtLspUpDownState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 80, 2, 1, 1, 12),
    _Hh3cMplsPsProtLspUpDownState_Type()
)
hh3cMplsPsProtLspUpDownState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMplsPsProtLspUpDownState.setStatus("current")


class _Hh3cMplsPsSwitchResult_Type(Integer32):
    """Custom type hh3cMplsPsSwitchResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Hh3cMplsPsSwitchResult_Type.__name__ = "Integer32"
_Hh3cMplsPsSwitchResult_Object = MibTableColumn
hh3cMplsPsSwitchResult = _Hh3cMplsPsSwitchResult_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 80, 2, 1, 1, 13),
    _Hh3cMplsPsSwitchResult_Type()
)
hh3cMplsPsSwitchResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMplsPsSwitchResult.setStatus("current")
_Hh3cMplsPsRowStatus_Type = RowStatus
_Hh3cMplsPsRowStatus_Object = MibTableColumn
hh3cMplsPsRowStatus = _Hh3cMplsPsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 80, 2, 1, 1, 14),
    _Hh3cMplsPsRowStatus_Type()
)
hh3cMplsPsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsPsRowStatus.setStatus("current")
_Hh3cMplsOamPsNotifications_ObjectIdentity = ObjectIdentity
hh3cMplsOamPsNotifications = _Hh3cMplsOamPsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 80, 3)
)

# Managed Objects groups


# Notification objects

hh3cMplsPsSwitchPtoW = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 80, 3, 1)
)
hh3cMplsPsSwitchPtoW.setObjects(
      *(("HH3C-MPLSOAM-PS-MIB", "hh3cMplsPsWorkLspName"),
        ("HH3C-MPLSOAM-PS-MIB", "hh3cMplsPsProtectLspName"),
        ("HH3C-MPLSOAM-PS-MIB", "hh3cMplsPsSwitchResult"))
)
if mibBuilder.loadTexts:
    hh3cMplsPsSwitchPtoW.setStatus(
        "current"
    )

hh3cMplsPsSwitchWtoP = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 80, 3, 2)
)
hh3cMplsPsSwitchWtoP.setObjects(
      *(("HH3C-MPLSOAM-PS-MIB", "hh3cMplsPsWorkLspName"),
        ("HH3C-MPLSOAM-PS-MIB", "hh3cMplsPsProtectLspName"),
        ("HH3C-MPLSOAM-PS-MIB", "hh3cMplsPsSwitchResult"))
)
if mibBuilder.loadTexts:
    hh3cMplsPsSwitchWtoP.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-MPLSOAM-PS-MIB",
    **{"hh3cMplsOamPs": hh3cMplsOamPs,
       "hh3cMplsOamPsScalarGroup": hh3cMplsOamPsScalarGroup,
       "hh3cMplsOamPsTrapOpen": hh3cMplsOamPsTrapOpen,
       "hh3cMplsOamPsTable": hh3cMplsOamPsTable,
       "hh3cMplsPsTable": hh3cMplsPsTable,
       "hh3cMplsPsEntry": hh3cMplsPsEntry,
       "hh3cMplsPsIndex": hh3cMplsPsIndex,
       "hh3cMplsPsGroupID": hh3cMplsPsGroupID,
       "hh3cMplsPsWorkLspName": hh3cMplsPsWorkLspName,
       "hh3cMplsPsProtectLspName": hh3cMplsPsProtectLspName,
       "hh3cMplsPsRevertiveMode": hh3cMplsPsRevertiveMode,
       "hh3cMplsPsWTR": hh3cMplsPsWTR,
       "hh3cMplsPsHoldOff": hh3cMplsPsHoldOff,
       "hh3cMplsPsSwitchCondition": hh3cMplsPsSwitchCondition,
       "hh3cMplsPsWorkLspDetectState": hh3cMplsPsWorkLspDetectState,
       "hh3cMplsPsWorkLspUpDownState": hh3cMplsPsWorkLspUpDownState,
       "hh3cMplsPsProtLspDetectState": hh3cMplsPsProtLspDetectState,
       "hh3cMplsPsProtLspUpDownState": hh3cMplsPsProtLspUpDownState,
       "hh3cMplsPsSwitchResult": hh3cMplsPsSwitchResult,
       "hh3cMplsPsRowStatus": hh3cMplsPsRowStatus,
       "hh3cMplsOamPsNotifications": hh3cMplsOamPsNotifications,
       "hh3cMplsPsSwitchPtoW": hh3cMplsPsSwitchPtoW,
       "hh3cMplsPsSwitchWtoP": hh3cMplsPsSwitchWtoP}
)
