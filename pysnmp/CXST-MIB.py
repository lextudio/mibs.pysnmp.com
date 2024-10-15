# SNMP MIB module (CXST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CXST-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:20:50 2024
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

(cxST,) = mibBuilder.importSymbols(
    "CXProduct-SMI",
    "cxST")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_StTable_Object = MibTable
stTable = _StTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 60, 10)
)
if mibBuilder.loadTexts:
    stTable.setStatus("mandatory")
_StEntry_Object = MibTableRow
stEntry = _StEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 60, 10, 1)
)
stEntry.setIndexNames(
    (0, "CXST-MIB", "stSlotNumberIndex"),
)
if mibBuilder.loadTexts:
    stEntry.setStatus("mandatory")


class _StSlotNumberIndex_Type(Integer32):
    """Custom type stSlotNumberIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_StSlotNumberIndex_Type.__name__ = "Integer32"
_StSlotNumberIndex_Object = MibTableColumn
stSlotNumberIndex = _StSlotNumberIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 60, 10, 1, 1),
    _StSlotNumberIndex_Type()
)
stSlotNumberIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stSlotNumberIndex.setStatus("mandatory")


class _StRowStatus_Type(Integer32):
    """Custom type stRowStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_StRowStatus_Type.__name__ = "Integer32"
_StRowStatus_Object = MibTableColumn
stRowStatus = _StRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 60, 10, 1, 2),
    _StRowStatus_Type()
)
stRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stRowStatus.setStatus("mandatory")


class _StPS1Detection_Type(Integer32):
    """Custom type stPS1Detection based on Integer32"""
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


_StPS1Detection_Type.__name__ = "Integer32"
_StPS1Detection_Object = MibTableColumn
stPS1Detection = _StPS1Detection_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 60, 10, 1, 10),
    _StPS1Detection_Type()
)
stPS1Detection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stPS1Detection.setStatus("mandatory")


class _StTimer1_Type(Integer32):
    """Custom type stTimer1 based on Integer32"""
    defaultValue = 15


_StTimer1_Object = MibTableColumn
stTimer1 = _StTimer1_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 60, 10, 1, 11),
    _StTimer1_Type()
)
stTimer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stTimer1.setStatus("mandatory")


class _StTimer3_Type(Integer32):
    """Custom type stTimer3 based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_StTimer3_Type.__name__ = "Integer32"
_StTimer3_Object = MibTableColumn
stTimer3 = _StTimer3_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 60, 10, 1, 12),
    _StTimer3_Type()
)
stTimer3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stTimer3.setStatus("mandatory")


class _StTest_Type(Integer32):
    """Custom type stTest based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("external", 4),
          ("internal2B", 3),
          ("internal2B1D", 2),
          ("stLpbk", 5),
          ("testSignal", 6))
    )


_StTest_Type.__name__ = "Integer32"
_StTest_Object = MibTableColumn
stTest = _StTest_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 60, 10, 1, 13),
    _StTest_Type()
)
stTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stTest.setStatus("mandatory")


class _StPortStatus_Type(Integer32):
    """Custom type stPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("portDown", 1),
          ("portUp", 2))
    )


_StPortStatus_Type.__name__ = "Integer32"
_StPortStatus_Object = MibTableColumn
stPortStatus = _StPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 60, 10, 1, 20),
    _StPortStatus_Type()
)
stPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stPortStatus.setStatus("mandatory")


class _StRxInfoState_Type(Integer32):
    """Custom type stRxInfoState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("info0", 1),
          ("info1", 2),
          ("info2", 3),
          ("info3", 4),
          ("info4", 5),
          ("infoX", 6))
    )


_StRxInfoState_Type.__name__ = "Integer32"
_StRxInfoState_Object = MibTableColumn
stRxInfoState = _StRxInfoState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 60, 10, 1, 21),
    _StRxInfoState_Type()
)
stRxInfoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stRxInfoState.setStatus("mandatory")


class _StTxInfoState_Type(Integer32):
    """Custom type stTxInfoState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("info0", 1),
          ("info1", 2),
          ("info2", 3),
          ("info3", 4),
          ("info4", 5),
          ("infoX", 6))
    )


_StTxInfoState_Type.__name__ = "Integer32"
_StTxInfoState_Object = MibTableColumn
stTxInfoState = _StTxInfoState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 60, 10, 1, 22),
    _StTxInfoState_Type()
)
stTxInfoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stTxInfoState.setStatus("mandatory")


class _StErrorIndicator_Type(Integer32):
    """Custom type stErrorIndicator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("errorDetected", 1),
          ("noError", 2))
    )


_StErrorIndicator_Type.__name__ = "Integer32"
_StErrorIndicator_Object = MibTableColumn
stErrorIndicator = _StErrorIndicator_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 60, 10, 1, 23),
    _StErrorIndicator_Type()
)
stErrorIndicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stErrorIndicator.setStatus("mandatory")


class _StFrameSync_Type(Integer32):
    """Custom type stFrameSync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noSync", 1),
          ("sync", 2))
    )


_StFrameSync_Type.__name__ = "Integer32"
_StFrameSync_Object = MibTableColumn
stFrameSync = _StFrameSync_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 60, 10, 1, 24),
    _StFrameSync_Type()
)
stFrameSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stFrameSync.setStatus("mandatory")


class _StPortMode_Type(Integer32):
    """Custom type stPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nt", 2),
          ("te", 1))
    )


_StPortMode_Type.__name__ = "Integer32"
_StPortMode_Object = MibTableColumn
stPortMode = _StPortMode_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 60, 10, 1, 25),
    _StPortMode_Type()
)
stPortMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stPortMode.setStatus("mandatory")
_StActivation_Type = Counter32
_StActivation_Object = MibTableColumn
stActivation = _StActivation_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 60, 10, 1, 40),
    _StActivation_Type()
)
stActivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stActivation.setStatus("mandatory")
_StDeactivation_Type = Counter32
_StDeactivation_Object = MibTableColumn
stDeactivation = _StDeactivation_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 60, 10, 1, 41),
    _StDeactivation_Type()
)
stDeactivation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stDeactivation.setStatus("mandatory")
_StTransition_Type = Counter32
_StTransition_Object = MibTableColumn
stTransition = _StTransition_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 60, 10, 1, 42),
    _StTransition_Type()
)
stTransition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stTransition.setStatus("mandatory")
_StNbErrors_Type = Counter32
_StNbErrors_Object = MibTableColumn
stNbErrors = _StNbErrors_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 60, 10, 1, 43),
    _StNbErrors_Type()
)
stNbErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stNbErrors.setStatus("mandatory")
_StFrameSyncLost_Type = Counter32
_StFrameSyncLost_Object = MibTableColumn
stFrameSyncLost = _StFrameSyncLost_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 60, 10, 1, 44),
    _StFrameSyncLost_Type()
)
stFrameSyncLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stFrameSyncLost.setStatus("mandatory")
_StMissingAMIViolation_Type = Integer32
_StMissingAMIViolation_Object = MibTableColumn
stMissingAMIViolation = _StMissingAMIViolation_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 60, 10, 1, 45),
    _StMissingAMIViolation_Type()
)
stMissingAMIViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stMissingAMIViolation.setStatus("mandatory")
_StUnbalancedFrame_Type = Integer32
_StUnbalancedFrame_Object = MibTableColumn
stUnbalancedFrame = _StUnbalancedFrame_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 60, 10, 1, 46),
    _StUnbalancedFrame_Type()
)
stUnbalancedFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stUnbalancedFrame.setStatus("mandatory")
_StClearStat_Type = Integer32
_StClearStat_Object = MibTableColumn
stClearStat = _StClearStat_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 60, 10, 1, 60),
    _StClearStat_Type()
)
stClearStat.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    stClearStat.setStatus("mandatory")


class _StPortCtrl_Type(Integer32):
    """Custom type stPortCtrl based on Integer32"""
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
        *(("openBChannels", 4),
          ("portDown", 1),
          ("portReset", 3),
          ("portUp", 2))
    )


_StPortCtrl_Type.__name__ = "Integer32"
_StPortCtrl_Object = MibTableColumn
stPortCtrl = _StPortCtrl_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 60, 10, 1, 61),
    _StPortCtrl_Type()
)
stPortCtrl.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    stPortCtrl.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CXST-MIB",
    **{"stTable": stTable,
       "stEntry": stEntry,
       "stSlotNumberIndex": stSlotNumberIndex,
       "stRowStatus": stRowStatus,
       "stPS1Detection": stPS1Detection,
       "stTimer1": stTimer1,
       "stTimer3": stTimer3,
       "stTest": stTest,
       "stPortStatus": stPortStatus,
       "stRxInfoState": stRxInfoState,
       "stTxInfoState": stTxInfoState,
       "stErrorIndicator": stErrorIndicator,
       "stFrameSync": stFrameSync,
       "stPortMode": stPortMode,
       "stActivation": stActivation,
       "stDeactivation": stDeactivation,
       "stTransition": stTransition,
       "stNbErrors": stNbErrors,
       "stFrameSyncLost": stFrameSyncLost,
       "stMissingAMIViolation": stMissingAMIViolation,
       "stUnbalancedFrame": stUnbalancedFrame,
       "stClearStat": stClearStat,
       "stPortCtrl": stPortCtrl}
)
