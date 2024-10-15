# SNMP MIB module (EICON-MIB-TRACE) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EICON-MIB-TRACE
# Produced by pysmi-1.5.4 at Mon Oct 14 21:36:48 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class ActionState(Integer32):
    """Custom type ActionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("done", 1),
          ("failed", 2),
          ("in-progress", 3))
    )





class ControlOnOff(Integer32):
    """Custom type ControlOnOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 3),
          ("start", 2),
          ("stop", 1))
    )





class CardRef(Integer32):
    """Custom type CardRef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )





class PortRef(Integer32):
    """Custom type PortRef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )





class PositiveInteger(Integer32):
    """Custom type PositiveInteger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Eicon_ObjectIdentity = ObjectIdentity
eicon = _Eicon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 434)
)
_Management_ObjectIdentity = ObjectIdentity
management = _Management_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 434, 2)
)
_Mibv2_ObjectIdentity = ObjectIdentity
mibv2 = _Mibv2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 434, 2, 2)
)
_Module_ObjectIdentity = ObjectIdentity
module = _Module_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4)
)
_Trace_ObjectIdentity = ObjectIdentity
trace = _Trace_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 15)
)
_TraceFreeEntryIndex_Type = PositiveInteger
_TraceFreeEntryIndex_Object = MibScalar
traceFreeEntryIndex = _TraceFreeEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 15, 1),
    _TraceFreeEntryIndex_Type()
)
traceFreeEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceFreeEntryIndex.setStatus("mandatory")
_TraceControlTable_Object = MibTable
traceControlTable = _TraceControlTable_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 15, 2)
)
if mibBuilder.loadTexts:
    traceControlTable.setStatus("mandatory")
_TraceControlEntry_Object = MibTableRow
traceControlEntry = _TraceControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 15, 2, 1)
)
traceControlEntry.setIndexNames(
    (0, "EICON-MIB-TRACE", "traceCntrlIndex"),
)
if mibBuilder.loadTexts:
    traceControlEntry.setStatus("mandatory")
_TraceCntrlIndex_Type = PositiveInteger
_TraceCntrlIndex_Object = MibTableColumn
traceCntrlIndex = _TraceCntrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 15, 2, 1, 1),
    _TraceCntrlIndex_Type()
)
traceCntrlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceCntrlIndex.setStatus("mandatory")


class _TraceCntrlEntryStatus_Type(Integer32):
    """Custom type traceCntrlEntryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("create", 2),
          ("invalid", 1),
          ("valid", 3))
    )


_TraceCntrlEntryStatus_Type.__name__ = "Integer32"
_TraceCntrlEntryStatus_Object = MibTableColumn
traceCntrlEntryStatus = _TraceCntrlEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 15, 2, 1, 2),
    _TraceCntrlEntryStatus_Type()
)
traceCntrlEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traceCntrlEntryStatus.setStatus("mandatory")


class _TraceCntrlEntryOwner_Type(DisplayString):
    """Custom type traceCntrlEntryOwner based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TraceCntrlEntryOwner_Type.__name__ = "DisplayString"
_TraceCntrlEntryOwner_Object = MibTableColumn
traceCntrlEntryOwner = _TraceCntrlEntryOwner_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 15, 2, 1, 3),
    _TraceCntrlEntryOwner_Type()
)
traceCntrlEntryOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traceCntrlEntryOwner.setStatus("mandatory")


class _TraceCntrlProtocol_Type(Integer32):
    """Custom type traceCntrlProtocol based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("frelay", 3),
          ("hdlc", 4),
          ("llc", 7),
          ("ppp", 9),
          ("sdlc", 2),
          ("sna", 8),
          ("snafr", 10),
          ("x25", 1),
          ("xportiso", 5),
          ("xporttgx", 6))
    )


_TraceCntrlProtocol_Type.__name__ = "Integer32"
_TraceCntrlProtocol_Object = MibTableColumn
traceCntrlProtocol = _TraceCntrlProtocol_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 15, 2, 1, 4),
    _TraceCntrlProtocol_Type()
)
traceCntrlProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traceCntrlProtocol.setStatus("mandatory")
_TraceCntrlEntryReclaimTime_Type = TimeTicks
_TraceCntrlEntryReclaimTime_Object = MibTableColumn
traceCntrlEntryReclaimTime = _TraceCntrlEntryReclaimTime_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 15, 2, 1, 5),
    _TraceCntrlEntryReclaimTime_Type()
)
traceCntrlEntryReclaimTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traceCntrlEntryReclaimTime.setStatus("mandatory")


class _TraceCntrlOnOff_Type(Integer32):
    """Custom type traceCntrlOnOff based on Integer32"""
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
        *(("invalid", 4),
          ("read", 2),
          ("start", 1),
          ("stop", 3))
    )


_TraceCntrlOnOff_Type.__name__ = "Integer32"
_TraceCntrlOnOff_Object = MibTableColumn
traceCntrlOnOff = _TraceCntrlOnOff_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 15, 2, 1, 6),
    _TraceCntrlOnOff_Type()
)
traceCntrlOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traceCntrlOnOff.setStatus("mandatory")
_TraceCntrlActionState_Type = ActionState
_TraceCntrlActionState_Object = MibTableColumn
traceCntrlActionState = _TraceCntrlActionState_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 15, 2, 1, 7),
    _TraceCntrlActionState_Type()
)
traceCntrlActionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceCntrlActionState.setStatus("mandatory")


class _TraceCntrlActionError_Type(Integer32):
    """Custom type traceCntrlActionError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bad-param", 2),
          ("no-error", 1))
    )


_TraceCntrlActionError_Type.__name__ = "Integer32"
_TraceCntrlActionError_Object = MibTableColumn
traceCntrlActionError = _TraceCntrlActionError_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 15, 2, 1, 8),
    _TraceCntrlActionError_Type()
)
traceCntrlActionError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceCntrlActionError.setStatus("mandatory")


class _TraceCntrlFileName_Type(DisplayString):
    """Custom type traceCntrlFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_TraceCntrlFileName_Type.__name__ = "DisplayString"
_TraceCntrlFileName_Object = MibTableColumn
traceCntrlFileName = _TraceCntrlFileName_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 15, 2, 1, 9),
    _TraceCntrlFileName_Type()
)
traceCntrlFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traceCntrlFileName.setStatus("mandatory")
_TraceCntrlCardRef_Type = CardRef
_TraceCntrlCardRef_Object = MibTableColumn
traceCntrlCardRef = _TraceCntrlCardRef_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 15, 2, 1, 10),
    _TraceCntrlCardRef_Type()
)
traceCntrlCardRef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traceCntrlCardRef.setStatus("mandatory")
_TraceCntrlPortRef_Type = PortRef
_TraceCntrlPortRef_Object = MibTableColumn
traceCntrlPortRef = _TraceCntrlPortRef_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 15, 2, 1, 11),
    _TraceCntrlPortRef_Type()
)
traceCntrlPortRef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traceCntrlPortRef.setStatus("mandatory")
_TraceCntrlConnectionRef_Type = Integer32
_TraceCntrlConnectionRef_Object = MibTableColumn
traceCntrlConnectionRef = _TraceCntrlConnectionRef_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 15, 2, 1, 12),
    _TraceCntrlConnectionRef_Type()
)
traceCntrlConnectionRef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traceCntrlConnectionRef.setStatus("mandatory")


class _TraceCntrlPURef_Type(DisplayString):
    """Custom type traceCntrlPURef based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TraceCntrlPURef_Type.__name__ = "DisplayString"
_TraceCntrlPURef_Object = MibTableColumn
traceCntrlPURef = _TraceCntrlPURef_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 15, 2, 1, 13),
    _TraceCntrlPURef_Type()
)
traceCntrlPURef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traceCntrlPURef.setStatus("mandatory")


class _TraceCntrlModeRef_Type(DisplayString):
    """Custom type traceCntrlModeRef based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TraceCntrlModeRef_Type.__name__ = "DisplayString"
_TraceCntrlModeRef_Object = MibTableColumn
traceCntrlModeRef = _TraceCntrlModeRef_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 15, 2, 1, 14),
    _TraceCntrlModeRef_Type()
)
traceCntrlModeRef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traceCntrlModeRef.setStatus("mandatory")
_TraceCntrlLURef_Type = Integer32
_TraceCntrlLURef_Object = MibTableColumn
traceCntrlLURef = _TraceCntrlLURef_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 15, 2, 1, 15),
    _TraceCntrlLURef_Type()
)
traceCntrlLURef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traceCntrlLURef.setStatus("mandatory")
_TraceCntrlStationRef_Type = Integer32
_TraceCntrlStationRef_Object = MibTableColumn
traceCntrlStationRef = _TraceCntrlStationRef_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 15, 2, 1, 16),
    _TraceCntrlStationRef_Type()
)
traceCntrlStationRef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traceCntrlStationRef.setStatus("mandatory")


class _TraceCntrlLLURef_Type(DisplayString):
    """Custom type traceCntrlLLURef based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TraceCntrlLLURef_Type.__name__ = "DisplayString"
_TraceCntrlLLURef_Object = MibTableColumn
traceCntrlLLURef = _TraceCntrlLLURef_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 15, 2, 1, 17),
    _TraceCntrlLLURef_Type()
)
traceCntrlLLURef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traceCntrlLLURef.setStatus("mandatory")


class _TraceCntrlRLURef_Type(DisplayString):
    """Custom type traceCntrlRLURef based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TraceCntrlRLURef_Type.__name__ = "DisplayString"
_TraceCntrlRLURef_Object = MibTableColumn
traceCntrlRLURef = _TraceCntrlRLURef_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 15, 2, 1, 18),
    _TraceCntrlRLURef_Type()
)
traceCntrlRLURef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traceCntrlRLURef.setStatus("mandatory")


class _TraceCntrlOption_Type(Integer32):
    """Custom type traceCntrlOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("append", 1),
          ("clear", 2))
    )


_TraceCntrlOption_Type.__name__ = "Integer32"
_TraceCntrlOption_Object = MibTableColumn
traceCntrlOption = _TraceCntrlOption_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 15, 2, 1, 19),
    _TraceCntrlOption_Type()
)
traceCntrlOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traceCntrlOption.setStatus("mandatory")
_TraceCntrlPeriod_Type = Integer32
_TraceCntrlPeriod_Object = MibTableColumn
traceCntrlPeriod = _TraceCntrlPeriod_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 15, 2, 1, 20),
    _TraceCntrlPeriod_Type()
)
traceCntrlPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traceCntrlPeriod.setStatus("mandatory")
_TraceCntrlMask_Type = Integer32
_TraceCntrlMask_Object = MibTableColumn
traceCntrlMask = _TraceCntrlMask_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 15, 2, 1, 21),
    _TraceCntrlMask_Type()
)
traceCntrlMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traceCntrlMask.setStatus("mandatory")
_TraceCntrlBufSize_Type = Integer32
_TraceCntrlBufSize_Object = MibTableColumn
traceCntrlBufSize = _TraceCntrlBufSize_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 15, 2, 1, 22),
    _TraceCntrlBufSize_Type()
)
traceCntrlBufSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traceCntrlBufSize.setStatus("mandatory")
_TraceCntrlEntrySize_Type = Integer32
_TraceCntrlEntrySize_Object = MibTableColumn
traceCntrlEntrySize = _TraceCntrlEntrySize_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 15, 2, 1, 23),
    _TraceCntrlEntrySize_Type()
)
traceCntrlEntrySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traceCntrlEntrySize.setStatus("mandatory")


class _TraceCntrlBufFullAction_Type(Integer32):
    """Custom type traceCntrlBufFullAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("stop", 2),
          ("stopAndAlarm", 3),
          ("wrap", 1))
    )


_TraceCntrlBufFullAction_Type.__name__ = "Integer32"
_TraceCntrlBufFullAction_Object = MibTableColumn
traceCntrlBufFullAction = _TraceCntrlBufFullAction_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 15, 2, 1, 24),
    _TraceCntrlBufFullAction_Type()
)
traceCntrlBufFullAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traceCntrlBufFullAction.setStatus("mandatory")
_TraceCntrlReadFromEntryIndex_Type = Integer32
_TraceCntrlReadFromEntryIndex_Object = MibTableColumn
traceCntrlReadFromEntryIndex = _TraceCntrlReadFromEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 15, 2, 1, 25),
    _TraceCntrlReadFromEntryIndex_Type()
)
traceCntrlReadFromEntryIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traceCntrlReadFromEntryIndex.setStatus("mandatory")


class _TraceCntrlFileType_Type(Integer32):
    """Custom type traceCntrlFileType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 1),
          ("ebcdic", 2))
    )


_TraceCntrlFileType_Type.__name__ = "Integer32"
_TraceCntrlFileType_Object = MibTableColumn
traceCntrlFileType = _TraceCntrlFileType_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 15, 2, 1, 26),
    _TraceCntrlFileType_Type()
)
traceCntrlFileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traceCntrlFileType.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EICON-MIB-TRACE",
    **{"ActionState": ActionState,
       "ControlOnOff": ControlOnOff,
       "CardRef": CardRef,
       "PortRef": PortRef,
       "PositiveInteger": PositiveInteger,
       "eicon": eicon,
       "management": management,
       "mibv2": mibv2,
       "module": module,
       "trace": trace,
       "traceFreeEntryIndex": traceFreeEntryIndex,
       "traceControlTable": traceControlTable,
       "traceControlEntry": traceControlEntry,
       "traceCntrlIndex": traceCntrlIndex,
       "traceCntrlEntryStatus": traceCntrlEntryStatus,
       "traceCntrlEntryOwner": traceCntrlEntryOwner,
       "traceCntrlProtocol": traceCntrlProtocol,
       "traceCntrlEntryReclaimTime": traceCntrlEntryReclaimTime,
       "traceCntrlOnOff": traceCntrlOnOff,
       "traceCntrlActionState": traceCntrlActionState,
       "traceCntrlActionError": traceCntrlActionError,
       "traceCntrlFileName": traceCntrlFileName,
       "traceCntrlCardRef": traceCntrlCardRef,
       "traceCntrlPortRef": traceCntrlPortRef,
       "traceCntrlConnectionRef": traceCntrlConnectionRef,
       "traceCntrlPURef": traceCntrlPURef,
       "traceCntrlModeRef": traceCntrlModeRef,
       "traceCntrlLURef": traceCntrlLURef,
       "traceCntrlStationRef": traceCntrlStationRef,
       "traceCntrlLLURef": traceCntrlLLURef,
       "traceCntrlRLURef": traceCntrlRLURef,
       "traceCntrlOption": traceCntrlOption,
       "traceCntrlPeriod": traceCntrlPeriod,
       "traceCntrlMask": traceCntrlMask,
       "traceCntrlBufSize": traceCntrlBufSize,
       "traceCntrlEntrySize": traceCntrlEntrySize,
       "traceCntrlBufFullAction": traceCntrlBufFullAction,
       "traceCntrlReadFromEntryIndex": traceCntrlReadFromEntryIndex,
       "traceCntrlFileType": traceCntrlFileType}
)
