# SNMP MIB module (CISCO-DMN-DSG-Cueing-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DMN-DSG-Cueing-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:58:18 2024
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

(ciscoDSGUtilities,) = mibBuilder.importSymbols(
    "CISCO-DMN-DSG-ROOT-MIB",
    "ciscoDSGUtilities")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ciscoDSGCueing = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 33)
)
ciscoDSGCueing.setRevisions(
        ("2010-08-30 08:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _CueingMode_Type(Integer32):
    """Custom type cueingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tone", 2),
          ("trigger", 1))
    )


_CueingMode_Type.__name__ = "Integer32"
_CueingMode_Object = MibScalar
cueingMode = _CueingMode_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 33, 1),
    _CueingMode_Type()
)
cueingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cueingMode.setStatus("current")


class _CueingTrigPol_Type(Integer32):
    """Custom type cueingTrigPol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("low", 1))
    )


_CueingTrigPol_Type.__name__ = "Integer32"
_CueingTrigPol_Object = MibScalar
cueingTrigPol = _CueingTrigPol_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 33, 2),
    _CueingTrigPol_Type()
)
cueingTrigPol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cueingTrigPol.setStatus("current")


class _CueingRepeatCnt_Type(Integer32):
    """Custom type cueingRepeatCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_CueingRepeatCnt_Type.__name__ = "Integer32"
_CueingRepeatCnt_Object = MibScalar
cueingRepeatCnt = _CueingRepeatCnt_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 33, 3),
    _CueingRepeatCnt_Type()
)
cueingRepeatCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cueingRepeatCnt.setStatus("current")


class _CueingTone_Type(Integer32):
    """Custom type cueingTone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 80),
    )


_CueingTone_Type.__name__ = "Integer32"
_CueingTone_Object = MibScalar
cueingTone = _CueingTone_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 33, 4),
    _CueingTone_Type()
)
cueingTone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cueingTone.setStatus("current")


class _CueingSilence_Type(Integer32):
    """Custom type cueingSilence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 80),
    )


_CueingSilence_Type.__name__ = "Integer32"
_CueingSilence_Object = MibScalar
cueingSilence = _CueingSilence_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 33, 5),
    _CueingSilence_Type()
)
cueingSilence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cueingSilence.setStatus("current")


class _CueingRelayMode_Type(Integer32):
    """Custom type cueingRelayMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("trigger", 2))
    )


_CueingRelayMode_Type.__name__ = "Integer32"
_CueingRelayMode_Object = MibScalar
cueingRelayMode = _CueingRelayMode_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 33, 6),
    _CueingRelayMode_Type()
)
cueingRelayMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cueingRelayMode.setStatus("current")


class _CueingRelayTrigBit_Type(Integer32):
    """Custom type cueingRelayTrigBit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CueingRelayTrigBit_Type.__name__ = "Integer32"
_CueingRelayTrigBit_Object = MibScalar
cueingRelayTrigBit = _CueingRelayTrigBit_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 33, 7),
    _CueingRelayTrigBit_Type()
)
cueingRelayTrigBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cueingRelayTrigBit.setStatus("current")


class _CueingTestToneSequence_Type(Integer32):
    """Custom type cueingTestToneSequence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_CueingTestToneSequence_Type.__name__ = "Integer32"
_CueingTestToneSequence_Object = MibScalar
cueingTestToneSequence = _CueingTestToneSequence_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 33, 8),
    _CueingTestToneSequence_Type()
)
cueingTestToneSequence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cueingTestToneSequence.setStatus("current")


class _CueingTestToneStartStop_Type(Integer32):
    """Custom type cueingTestToneStartStop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("stop", 2))
    )


_CueingTestToneStartStop_Type.__name__ = "Integer32"
_CueingTestToneStartStop_Object = MibScalar
cueingTestToneStartStop = _CueingTestToneStartStop_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 33, 9),
    _CueingTestToneStartStop_Type()
)
cueingTestToneStartStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cueingTestToneStartStop.setStatus("current")


class _CueingTestToneGo_Type(Integer32):
    """Custom type cueingTestToneGo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CueingTestToneGo_Type.__name__ = "Integer32"
_CueingTestToneGo_Object = MibScalar
cueingTestToneGo = _CueingTestToneGo_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 33, 10),
    _CueingTestToneGo_Type()
)
cueingTestToneGo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cueingTestToneGo.setStatus("current")
_CueingTable_ObjectIdentity = ObjectIdentity
cueingTable = _CueingTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 33, 11)
)
_CueingToneSeqTable_Object = MibTable
cueingToneSeqTable = _CueingToneSeqTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 33, 11, 1)
)
if mibBuilder.loadTexts:
    cueingToneSeqTable.setStatus("current")
_CueingToneSeqEntry_Object = MibTableRow
cueingToneSeqEntry = _CueingToneSeqEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 33, 11, 1, 1)
)
cueingToneSeqEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-Cueing-MIB", "cueingToneSeqNum"),
)
if mibBuilder.loadTexts:
    cueingToneSeqEntry.setStatus("current")


class _CueingToneSeqNum_Type(Integer32):
    """Custom type cueingToneSeqNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_CueingToneSeqNum_Type.__name__ = "Integer32"
_CueingToneSeqNum_Object = MibTableColumn
cueingToneSeqNum = _CueingToneSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 33, 11, 1, 1, 1),
    _CueingToneSeqNum_Type()
)
cueingToneSeqNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cueingToneSeqNum.setStatus("current")


class _CueingToneSeqState_Type(Integer32):
    """Custom type cueingToneSeqState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CueingToneSeqState_Type.__name__ = "Integer32"
_CueingToneSeqState_Object = MibTableColumn
cueingToneSeqState = _CueingToneSeqState_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 33, 11, 1, 1, 2),
    _CueingToneSeqState_Type()
)
cueingToneSeqState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cueingToneSeqState.setStatus("current")


class _CueingToneSeqTones_Type(Integer32):
    """Custom type cueingToneSeqTones based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_CueingToneSeqTones_Type.__name__ = "Integer32"
_CueingToneSeqTones_Object = MibTableColumn
cueingToneSeqTones = _CueingToneSeqTones_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 33, 11, 1, 1, 3),
    _CueingToneSeqTones_Type()
)
cueingToneSeqTones.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cueingToneSeqTones.setStatus("current")


class _CueingToneSeqMode_Type(Integer32):
    """Custom type cueingToneSeqMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("start", 1),
          ("stop", 2))
    )


_CueingToneSeqMode_Type.__name__ = "Integer32"
_CueingToneSeqMode_Object = MibTableColumn
cueingToneSeqMode = _CueingToneSeqMode_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 33, 11, 1, 1, 4),
    _CueingToneSeqMode_Type()
)
cueingToneSeqMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cueingToneSeqMode.setStatus("current")


class _CueingToneSeqDelay_Type(Integer32):
    """Custom type cueingToneSeqDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CueingToneSeqDelay_Type.__name__ = "Integer32"
_CueingToneSeqDelay_Object = MibTableColumn
cueingToneSeqDelay = _CueingToneSeqDelay_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 33, 11, 1, 1, 5),
    _CueingToneSeqDelay_Type()
)
cueingToneSeqDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cueingToneSeqDelay.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DMN-DSG-Cueing-MIB",
    **{"ciscoDSGCueing": ciscoDSGCueing,
       "cueingMode": cueingMode,
       "cueingTrigPol": cueingTrigPol,
       "cueingRepeatCnt": cueingRepeatCnt,
       "cueingTone": cueingTone,
       "cueingSilence": cueingSilence,
       "cueingRelayMode": cueingRelayMode,
       "cueingRelayTrigBit": cueingRelayTrigBit,
       "cueingTestToneSequence": cueingTestToneSequence,
       "cueingTestToneStartStop": cueingTestToneStartStop,
       "cueingTestToneGo": cueingTestToneGo,
       "cueingTable": cueingTable,
       "cueingToneSeqTable": cueingToneSeqTable,
       "cueingToneSeqEntry": cueingToneSeqEntry,
       "cueingToneSeqNum": cueingToneSeqNum,
       "cueingToneSeqState": cueingToneSeqState,
       "cueingToneSeqTones": cueingToneSeqTones,
       "cueingToneSeqMode": cueingToneSeqMode,
       "cueingToneSeqDelay": cueingToneSeqDelay}
)
