# SNMP MIB module (HPN-ICF-MPLSOAM-PS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-MPLSOAM-PS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:01:13 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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

hpnicfMplsOamPs = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 80)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfMplsOamPsScalarGroup_ObjectIdentity = ObjectIdentity
hpnicfMplsOamPsScalarGroup = _HpnicfMplsOamPsScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 80, 1)
)


class _HpnicfMplsOamPsTrapOpen_Type(TruthValue):
    """Custom type hpnicfMplsOamPsTrapOpen based on TruthValue"""


_HpnicfMplsOamPsTrapOpen_Object = MibScalar
hpnicfMplsOamPsTrapOpen = _HpnicfMplsOamPsTrapOpen_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 80, 1, 1),
    _HpnicfMplsOamPsTrapOpen_Type()
)
hpnicfMplsOamPsTrapOpen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfMplsOamPsTrapOpen.setStatus("current")
_HpnicfMplsOamPsTable_ObjectIdentity = ObjectIdentity
hpnicfMplsOamPsTable = _HpnicfMplsOamPsTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 80, 2)
)
_HpnicfMplsPsTable_Object = MibTable
hpnicfMplsPsTable = _HpnicfMplsPsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 80, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfMplsPsTable.setStatus("current")
_HpnicfMplsPsEntry_Object = MibTableRow
hpnicfMplsPsEntry = _HpnicfMplsPsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 80, 2, 1, 1)
)
hpnicfMplsPsEntry.setIndexNames(
    (0, "HPN-ICF-MPLSOAM-PS-MIB", "hpnicfMplsPsIndex"),
)
if mibBuilder.loadTexts:
    hpnicfMplsPsEntry.setStatus("current")
_HpnicfMplsPsIndex_Type = Integer32
_HpnicfMplsPsIndex_Object = MibTableColumn
hpnicfMplsPsIndex = _HpnicfMplsPsIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 80, 2, 1, 1, 1),
    _HpnicfMplsPsIndex_Type()
)
hpnicfMplsPsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfMplsPsIndex.setStatus("current")
_HpnicfMplsPsGroupID_Type = Integer32
_HpnicfMplsPsGroupID_Object = MibTableColumn
hpnicfMplsPsGroupID = _HpnicfMplsPsGroupID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 80, 2, 1, 1, 2),
    _HpnicfMplsPsGroupID_Type()
)
hpnicfMplsPsGroupID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsPsGroupID.setStatus("current")
_HpnicfMplsPsWorkLspName_Type = OctetString
_HpnicfMplsPsWorkLspName_Object = MibTableColumn
hpnicfMplsPsWorkLspName = _HpnicfMplsPsWorkLspName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 80, 2, 1, 1, 3),
    _HpnicfMplsPsWorkLspName_Type()
)
hpnicfMplsPsWorkLspName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsPsWorkLspName.setStatus("current")
_HpnicfMplsPsProtectLspName_Type = OctetString
_HpnicfMplsPsProtectLspName_Object = MibTableColumn
hpnicfMplsPsProtectLspName = _HpnicfMplsPsProtectLspName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 80, 2, 1, 1, 4),
    _HpnicfMplsPsProtectLspName_Type()
)
hpnicfMplsPsProtectLspName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsPsProtectLspName.setStatus("current")


class _HpnicfMplsPsRevertiveMode_Type(Integer32):
    """Custom type hpnicfMplsPsRevertiveMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_HpnicfMplsPsRevertiveMode_Type.__name__ = "Integer32"
_HpnicfMplsPsRevertiveMode_Object = MibTableColumn
hpnicfMplsPsRevertiveMode = _HpnicfMplsPsRevertiveMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 80, 2, 1, 1, 5),
    _HpnicfMplsPsRevertiveMode_Type()
)
hpnicfMplsPsRevertiveMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsPsRevertiveMode.setStatus("current")
_HpnicfMplsPsWTR_Type = Integer32
_HpnicfMplsPsWTR_Object = MibTableColumn
hpnicfMplsPsWTR = _HpnicfMplsPsWTR_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 80, 2, 1, 1, 6),
    _HpnicfMplsPsWTR_Type()
)
hpnicfMplsPsWTR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsPsWTR.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfMplsPsWTR.setUnits("30s")
_HpnicfMplsPsHoldOff_Type = Integer32
_HpnicfMplsPsHoldOff_Object = MibTableColumn
hpnicfMplsPsHoldOff = _HpnicfMplsPsHoldOff_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 80, 2, 1, 1, 7),
    _HpnicfMplsPsHoldOff_Type()
)
hpnicfMplsPsHoldOff.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsPsHoldOff.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfMplsPsHoldOff.setUnits("100ms")


class _HpnicfMplsPsSwitchCondition_Type(Integer32):
    """Custom type hpnicfMplsPsSwitchCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_HpnicfMplsPsSwitchCondition_Type.__name__ = "Integer32"
_HpnicfMplsPsSwitchCondition_Object = MibTableColumn
hpnicfMplsPsSwitchCondition = _HpnicfMplsPsSwitchCondition_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 80, 2, 1, 1, 8),
    _HpnicfMplsPsSwitchCondition_Type()
)
hpnicfMplsPsSwitchCondition.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsPsSwitchCondition.setStatus("current")


class _HpnicfMplsPsWorkLspDetectState_Type(Integer32):
    """Custom type hpnicfMplsPsWorkLspDetectState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_HpnicfMplsPsWorkLspDetectState_Type.__name__ = "Integer32"
_HpnicfMplsPsWorkLspDetectState_Object = MibTableColumn
hpnicfMplsPsWorkLspDetectState = _HpnicfMplsPsWorkLspDetectState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 80, 2, 1, 1, 9),
    _HpnicfMplsPsWorkLspDetectState_Type()
)
hpnicfMplsPsWorkLspDetectState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMplsPsWorkLspDetectState.setStatus("current")


class _HpnicfMplsPsWorkLspUpDownState_Type(Integer32):
    """Custom type hpnicfMplsPsWorkLspUpDownState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_HpnicfMplsPsWorkLspUpDownState_Type.__name__ = "Integer32"
_HpnicfMplsPsWorkLspUpDownState_Object = MibTableColumn
hpnicfMplsPsWorkLspUpDownState = _HpnicfMplsPsWorkLspUpDownState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 80, 2, 1, 1, 10),
    _HpnicfMplsPsWorkLspUpDownState_Type()
)
hpnicfMplsPsWorkLspUpDownState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMplsPsWorkLspUpDownState.setStatus("current")


class _HpnicfMplsPsProtLspDetectState_Type(Integer32):
    """Custom type hpnicfMplsPsProtLspDetectState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_HpnicfMplsPsProtLspDetectState_Type.__name__ = "Integer32"
_HpnicfMplsPsProtLspDetectState_Object = MibTableColumn
hpnicfMplsPsProtLspDetectState = _HpnicfMplsPsProtLspDetectState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 80, 2, 1, 1, 11),
    _HpnicfMplsPsProtLspDetectState_Type()
)
hpnicfMplsPsProtLspDetectState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMplsPsProtLspDetectState.setStatus("current")


class _HpnicfMplsPsProtLspUpDownState_Type(Integer32):
    """Custom type hpnicfMplsPsProtLspUpDownState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_HpnicfMplsPsProtLspUpDownState_Type.__name__ = "Integer32"
_HpnicfMplsPsProtLspUpDownState_Object = MibTableColumn
hpnicfMplsPsProtLspUpDownState = _HpnicfMplsPsProtLspUpDownState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 80, 2, 1, 1, 12),
    _HpnicfMplsPsProtLspUpDownState_Type()
)
hpnicfMplsPsProtLspUpDownState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMplsPsProtLspUpDownState.setStatus("current")


class _HpnicfMplsPsSwitchResult_Type(Integer32):
    """Custom type hpnicfMplsPsSwitchResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_HpnicfMplsPsSwitchResult_Type.__name__ = "Integer32"
_HpnicfMplsPsSwitchResult_Object = MibTableColumn
hpnicfMplsPsSwitchResult = _HpnicfMplsPsSwitchResult_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 80, 2, 1, 1, 13),
    _HpnicfMplsPsSwitchResult_Type()
)
hpnicfMplsPsSwitchResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMplsPsSwitchResult.setStatus("current")
_HpnicfMplsPsRowStatus_Type = RowStatus
_HpnicfMplsPsRowStatus_Object = MibTableColumn
hpnicfMplsPsRowStatus = _HpnicfMplsPsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 80, 2, 1, 1, 14),
    _HpnicfMplsPsRowStatus_Type()
)
hpnicfMplsPsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsPsRowStatus.setStatus("current")
_HpnicfMplsOamPsNotifications_ObjectIdentity = ObjectIdentity
hpnicfMplsOamPsNotifications = _HpnicfMplsOamPsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 80, 3)
)

# Managed Objects groups


# Notification objects

hpnicfMplsPsSwitchPtoW = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 80, 3, 1)
)
hpnicfMplsPsSwitchPtoW.setObjects(
      *(("HPN-ICF-MPLSOAM-PS-MIB", "hpnicfMplsPsWorkLspName"),
        ("HPN-ICF-MPLSOAM-PS-MIB", "hpnicfMplsPsProtectLspName"),
        ("HPN-ICF-MPLSOAM-PS-MIB", "hpnicfMplsPsSwitchResult"))
)
if mibBuilder.loadTexts:
    hpnicfMplsPsSwitchPtoW.setStatus(
        "current"
    )

hpnicfMplsPsSwitchWtoP = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 80, 3, 2)
)
hpnicfMplsPsSwitchWtoP.setObjects(
      *(("HPN-ICF-MPLSOAM-PS-MIB", "hpnicfMplsPsWorkLspName"),
        ("HPN-ICF-MPLSOAM-PS-MIB", "hpnicfMplsPsProtectLspName"),
        ("HPN-ICF-MPLSOAM-PS-MIB", "hpnicfMplsPsSwitchResult"))
)
if mibBuilder.loadTexts:
    hpnicfMplsPsSwitchWtoP.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-MPLSOAM-PS-MIB",
    **{"hpnicfMplsOamPs": hpnicfMplsOamPs,
       "hpnicfMplsOamPsScalarGroup": hpnicfMplsOamPsScalarGroup,
       "hpnicfMplsOamPsTrapOpen": hpnicfMplsOamPsTrapOpen,
       "hpnicfMplsOamPsTable": hpnicfMplsOamPsTable,
       "hpnicfMplsPsTable": hpnicfMplsPsTable,
       "hpnicfMplsPsEntry": hpnicfMplsPsEntry,
       "hpnicfMplsPsIndex": hpnicfMplsPsIndex,
       "hpnicfMplsPsGroupID": hpnicfMplsPsGroupID,
       "hpnicfMplsPsWorkLspName": hpnicfMplsPsWorkLspName,
       "hpnicfMplsPsProtectLspName": hpnicfMplsPsProtectLspName,
       "hpnicfMplsPsRevertiveMode": hpnicfMplsPsRevertiveMode,
       "hpnicfMplsPsWTR": hpnicfMplsPsWTR,
       "hpnicfMplsPsHoldOff": hpnicfMplsPsHoldOff,
       "hpnicfMplsPsSwitchCondition": hpnicfMplsPsSwitchCondition,
       "hpnicfMplsPsWorkLspDetectState": hpnicfMplsPsWorkLspDetectState,
       "hpnicfMplsPsWorkLspUpDownState": hpnicfMplsPsWorkLspUpDownState,
       "hpnicfMplsPsProtLspDetectState": hpnicfMplsPsProtLspDetectState,
       "hpnicfMplsPsProtLspUpDownState": hpnicfMplsPsProtLspUpDownState,
       "hpnicfMplsPsSwitchResult": hpnicfMplsPsSwitchResult,
       "hpnicfMplsPsRowStatus": hpnicfMplsPsRowStatus,
       "hpnicfMplsOamPsNotifications": hpnicfMplsOamPsNotifications,
       "hpnicfMplsPsSwitchPtoW": hpnicfMplsPsSwitchPtoW,
       "hpnicfMplsPsSwitchWtoP": hpnicfMplsPsSwitchWtoP}
)
