# SNMP MIB module (ALC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:35:31 2024
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

(rs232PortIndex,) = mibBuilder.importSymbols(
    "RS-232-MIB",
    "rs232PortIndex")

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
 NotificationType,
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
    "NotificationType",
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



class NonNegativeInteger(Integer32):
    """Custom type NonNegativeInteger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )





class InterfaceIndex(Integer32):
    """Custom type InterfaceIndex based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ngcan_ObjectIdentity = ObjectIdentity
ngcan = _Ngcan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1978)
)
_Tiger_ObjectIdentity = ObjectIdentity
tiger = _Tiger_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1978, 2)
)
_AlcMIB_ObjectIdentity = ObjectIdentity
alcMIB = _AlcMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1978, 2, 10)
)
_AlcLine_ObjectIdentity = ObjectIdentity
alcLine = _AlcLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1978, 2, 10, 1)
)
_AlcNumLines_Type = NonNegativeInteger
_AlcNumLines_Object = MibScalar
alcNumLines = _AlcNumLines_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 10, 1, 1),
    _AlcNumLines_Type()
)
alcNumLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcNumLines.setStatus("mandatory")
_AlcLineTable_Object = MibTable
alcLineTable = _AlcLineTable_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 10, 1, 2)
)
if mibBuilder.loadTexts:
    alcLineTable.setStatus("mandatory")
_AlcLineEntry_Object = MibTableRow
alcLineEntry = _AlcLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 10, 1, 2, 1)
)
alcLineEntry.setIndexNames(
    (0, "ALC-MIB", "alcLineIfIndex"),
)
if mibBuilder.loadTexts:
    alcLineEntry.setStatus("mandatory")
_AlcLineIfIndex_Type = InterfaceIndex
_AlcLineIfIndex_Object = MibTableColumn
alcLineIfIndex = _AlcLineIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 10, 1, 2, 1, 1),
    _AlcLineIfIndex_Type()
)
alcLineIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alcLineIfIndex.setStatus("mandatory")


class _AlcLineStationType_Type(Integer32):
    """Custom type alcLineStationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondaryMultidrop", 3),
          ("secondaryPointtopoint", 2))
    )


_AlcLineStationType_Type.__name__ = "Integer32"
_AlcLineStationType_Object = MibTableColumn
alcLineStationType = _AlcLineStationType_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 10, 1, 2, 1, 2),
    _AlcLineStationType_Type()
)
alcLineStationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alcLineStationType.setStatus("mandatory")
_AlcNumCuConfiged_Type = NonNegativeInteger
_AlcNumCuConfiged_Object = MibTableColumn
alcNumCuConfiged = _AlcNumCuConfiged_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 10, 1, 2, 1, 3),
    _AlcNumCuConfiged_Type()
)
alcNumCuConfiged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcNumCuConfiged.setStatus("mandatory")


class _AlcDuplexOptions_Type(Integer32):
    """Custom type alcDuplexOptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("poll-immediate", 2))
    )


_AlcDuplexOptions_Type.__name__ = "Integer32"
_AlcDuplexOptions_Object = MibTableColumn
alcDuplexOptions = _AlcDuplexOptions_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 10, 1, 2, 1, 4),
    _AlcDuplexOptions_Type()
)
alcDuplexOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alcDuplexOptions.setStatus("mandatory")


class _AlcT3MinCycleTime_Type(Integer32):
    """Custom type alcT3MinCycleTime based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_AlcT3MinCycleTime_Type.__name__ = "Integer32"
_AlcT3MinCycleTime_Object = MibTableColumn
alcT3MinCycleTime = _AlcT3MinCycleTime_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 10, 1, 2, 1, 5),
    _AlcT3MinCycleTime_Type()
)
alcT3MinCycleTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alcT3MinCycleTime.setStatus("mandatory")


class _AlcT6SegmentedMsgTimer_Type(Integer32):
    """Custom type alcT6SegmentedMsgTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AlcT6SegmentedMsgTimer_Type.__name__ = "Integer32"
_AlcT6SegmentedMsgTimer_Object = MibTableColumn
alcT6SegmentedMsgTimer = _AlcT6SegmentedMsgTimer_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 10, 1, 2, 1, 6),
    _AlcT6SegmentedMsgTimer_Type()
)
alcT6SegmentedMsgTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alcT6SegmentedMsgTimer.setStatus("mandatory")


class _AlcN5LiveDeadRatio_Type(Integer32):
    """Custom type alcN5LiveDeadRatio based on Integer32"""
    defaultValue = 25

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AlcN5LiveDeadRatio_Type.__name__ = "Integer32"
_AlcN5LiveDeadRatio_Object = MibTableColumn
alcN5LiveDeadRatio = _AlcN5LiveDeadRatio_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 10, 1, 2, 1, 7),
    _AlcN5LiveDeadRatio_Type()
)
alcN5LiveDeadRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alcN5LiveDeadRatio.setStatus("mandatory")


class _AlcSegmentOption_Type(Integer32):
    """Custom type alcSegmentOption based on Integer32"""
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


_AlcSegmentOption_Type.__name__ = "Integer32"
_AlcSegmentOption_Object = MibTableColumn
alcSegmentOption = _AlcSegmentOption_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 10, 1, 2, 1, 8),
    _AlcSegmentOption_Type()
)
alcSegmentOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alcSegmentOption.setStatus("mandatory")


class _AlcReassembleOption_Type(Integer32):
    """Custom type alcReassembleOption based on Integer32"""
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


_AlcReassembleOption_Type.__name__ = "Integer32"
_AlcReassembleOption_Object = MibTableColumn
alcReassembleOption = _AlcReassembleOption_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 10, 1, 2, 1, 9),
    _AlcReassembleOption_Type()
)
alcReassembleOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alcReassembleOption.setStatus("mandatory")


class _AlcWildIAPoll_Type(Integer32):
    """Custom type alcWildIAPoll based on Integer32"""
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


_AlcWildIAPoll_Type.__name__ = "Integer32"
_AlcWildIAPoll_Object = MibTableColumn
alcWildIAPoll = _AlcWildIAPoll_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 10, 1, 2, 1, 10),
    _AlcWildIAPoll_Type()
)
alcWildIAPoll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alcWildIAPoll.setStatus("mandatory")


class _AlcNumOfIdles_Type(Integer32):
    """Custom type alcNumOfIdles based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AlcNumOfIdles_Type.__name__ = "Integer32"
_AlcNumOfIdles_Object = MibTableColumn
alcNumOfIdles = _AlcNumOfIdles_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 10, 1, 2, 1, 11),
    _AlcNumOfIdles_Type()
)
alcNumOfIdles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alcNumOfIdles.setStatus("mandatory")


class _AlcInterMsgSync_Type(Integer32):
    """Custom type alcInterMsgSync based on Integer32"""
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


_AlcInterMsgSync_Type.__name__ = "Integer32"
_AlcInterMsgSync_Object = MibTableColumn
alcInterMsgSync = _AlcInterMsgSync_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 10, 1, 2, 1, 12),
    _AlcInterMsgSync_Type()
)
alcInterMsgSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alcInterMsgSync.setStatus("mandatory")


class _AlcNIA_Type(Integer32):
    """Custom type alcNIA based on Integer32"""
    defaultValue = 55

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_AlcNIA_Type.__name__ = "Integer32"
_AlcNIA_Object = MibTableColumn
alcNIA = _AlcNIA_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 10, 1, 2, 1, 13),
    _AlcNIA_Type()
)
alcNIA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alcNIA.setStatus("mandatory")
_AlcTxOverlengthFrames_Type = Counter32
_AlcTxOverlengthFrames_Object = MibTableColumn
alcTxOverlengthFrames = _AlcTxOverlengthFrames_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 10, 1, 2, 1, 14),
    _AlcTxOverlengthFrames_Type()
)
alcTxOverlengthFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcTxOverlengthFrames.setStatus("mandatory")
_AlcRxOverlengthFrames_Type = Counter32
_AlcRxOverlengthFrames_Object = MibTableColumn
alcRxOverlengthFrames = _AlcRxOverlengthFrames_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 10, 1, 2, 1, 15),
    _AlcRxOverlengthFrames_Type()
)
alcRxOverlengthFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcRxOverlengthFrames.setStatus("mandatory")
_AlcInvalidAddresses_Type = Counter32
_AlcInvalidAddresses_Object = MibTableColumn
alcInvalidAddresses = _AlcInvalidAddresses_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 10, 1, 2, 1, 16),
    _AlcInvalidAddresses_Type()
)
alcInvalidAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcInvalidAddresses.setStatus("mandatory")
_AlcRxT2Expireds_Type = Counter32
_AlcRxT2Expireds_Object = MibTableColumn
alcRxT2Expireds = _AlcRxT2Expireds_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 10, 1, 2, 1, 17),
    _AlcRxT2Expireds_Type()
)
alcRxT2Expireds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcRxT2Expireds.setStatus("mandatory")
_AlcDroppedMsgs_Type = Counter32
_AlcDroppedMsgs_Object = MibTableColumn
alcDroppedMsgs = _AlcDroppedMsgs_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 10, 1, 2, 1, 18),
    _AlcDroppedMsgs_Type()
)
alcDroppedMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcDroppedMsgs.setStatus("mandatory")
_AlcRxOverlengthFramesThres_Type = NonNegativeInteger
_AlcRxOverlengthFramesThres_Object = MibTableColumn
alcRxOverlengthFramesThres = _AlcRxOverlengthFramesThres_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 10, 1, 2, 1, 19),
    _AlcRxOverlengthFramesThres_Type()
)
alcRxOverlengthFramesThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alcRxOverlengthFramesThres.setStatus("mandatory")
_AlcInvalidAddressThres_Type = NonNegativeInteger
_AlcInvalidAddressThres_Object = MibTableColumn
alcInvalidAddressThres = _AlcInvalidAddressThres_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 10, 1, 2, 1, 20),
    _AlcInvalidAddressThres_Type()
)
alcInvalidAddressThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alcInvalidAddressThres.setStatus("mandatory")
_AlcRxT2ExpiredThres_Type = NonNegativeInteger
_AlcRxT2ExpiredThres_Object = MibTableColumn
alcRxT2ExpiredThres = _AlcRxT2ExpiredThres_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 10, 1, 2, 1, 21),
    _AlcRxT2ExpiredThres_Type()
)
alcRxT2ExpiredThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alcRxT2ExpiredThres.setStatus("mandatory")


class _AlcTrapReason_Type(Integer32):
    """Custom type alcTrapReason based on Integer32"""
    defaultValue = 1

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
        *(("invalid-address", 3),
          ("none", 1),
          ("rx-T2-expired", 4),
          ("rx-overlength-frames", 2))
    )


_AlcTrapReason_Type.__name__ = "Integer32"
_AlcTrapReason_Object = MibTableColumn
alcTrapReason = _AlcTrapReason_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 10, 1, 2, 1, 23),
    _AlcTrapReason_Type()
)
alcTrapReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcTrapReason.setStatus("mandatory")
_AlcErrData_Type = OctetString
_AlcErrData_Object = MibTableColumn
alcErrData = _AlcErrData_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 10, 1, 2, 1, 24),
    _AlcErrData_Type()
)
alcErrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcErrData.setStatus("mandatory")
_AlcCuTable_Object = MibTable
alcCuTable = _AlcCuTable_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 10, 1, 3)
)
if mibBuilder.loadTexts:
    alcCuTable.setStatus("mandatory")
_AlcCuEntry_Object = MibTableRow
alcCuEntry = _AlcCuEntry_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 10, 1, 3, 1)
)
alcCuEntry.setIndexNames(
    (0, "ALC-MIB", "alcCuIfIndex"),
    (0, "ALC-MIB", "alcCuIA"),
)
if mibBuilder.loadTexts:
    alcCuEntry.setStatus("mandatory")


class _AlcCuIfIndex_Type(Integer32):
    """Custom type alcCuIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AlcCuIfIndex_Type.__name__ = "Integer32"
_AlcCuIfIndex_Object = MibTableColumn
alcCuIfIndex = _AlcCuIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 10, 1, 3, 1, 1),
    _AlcCuIfIndex_Type()
)
alcCuIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alcCuIfIndex.setStatus("mandatory")


class _AlcCuDescr_Type(DisplayString):
    """Custom type alcCuDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AlcCuDescr_Type.__name__ = "DisplayString"
_AlcCuDescr_Object = MibTableColumn
alcCuDescr = _AlcCuDescr_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 10, 1, 3, 1, 2),
    _AlcCuDescr_Type()
)
alcCuDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alcCuDescr.setStatus("mandatory")


class _AlcCuIA_Type(Integer32):
    """Custom type alcCuIA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AlcCuIA_Type.__name__ = "Integer32"
_AlcCuIA_Object = MibTableColumn
alcCuIA = _AlcCuIA_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 10, 1, 3, 1, 3),
    _AlcCuIA_Type()
)
alcCuIA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alcCuIA.setStatus("mandatory")


class _AlcCuStatus_Type(Integer32):
    """Custom type alcCuStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabledDown", 3),
          ("enabledUp", 2))
    )


_AlcCuStatus_Type.__name__ = "Integer32"
_AlcCuStatus_Object = MibTableColumn
alcCuStatus = _AlcCuStatus_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 10, 1, 3, 1, 4),
    _AlcCuStatus_Type()
)
alcCuStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcCuStatus.setStatus("mandatory")


class _AlcCuPollCmd_Type(Integer32):
    """Custom type alcCuPollCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cascade", 3),
          ("disable", 2),
          ("enable", 1))
    )


_AlcCuPollCmd_Type.__name__ = "Integer32"
_AlcCuPollCmd_Object = MibTableColumn
alcCuPollCmd = _AlcCuPollCmd_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 10, 1, 3, 1, 5),
    _AlcCuPollCmd_Type()
)
alcCuPollCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alcCuPollCmd.setStatus("mandatory")


class _AlcCuOutQueueMsgSize_Type(Integer32):
    """Custom type alcCuOutQueueMsgSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AlcCuOutQueueMsgSize_Type.__name__ = "Integer32"
_AlcCuOutQueueMsgSize_Object = MibTableColumn
alcCuOutQueueMsgSize = _AlcCuOutQueueMsgSize_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 10, 1, 3, 1, 6),
    _AlcCuOutQueueMsgSize_Type()
)
alcCuOutQueueMsgSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alcCuOutQueueMsgSize.setStatus("mandatory")


class _AlcCuOutQueueCharSize_Type(Integer32):
    """Custom type alcCuOutQueueCharSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_AlcCuOutQueueCharSize_Type.__name__ = "Integer32"
_AlcCuOutQueueCharSize_Object = MibTableColumn
alcCuOutQueueCharSize = _AlcCuOutQueueCharSize_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 10, 1, 3, 1, 7),
    _AlcCuOutQueueCharSize_Type()
)
alcCuOutQueueCharSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alcCuOutQueueCharSize.setStatus("mandatory")


class _AlcCuN1MaxMsgSize_Type(Integer32):
    """Custom type alcCuN1MaxMsgSize based on Integer32"""
    defaultValue = 1920

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_AlcCuN1MaxMsgSize_Type.__name__ = "Integer32"
_AlcCuN1MaxMsgSize_Object = MibTableColumn
alcCuN1MaxMsgSize = _AlcCuN1MaxMsgSize_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 10, 1, 3, 1, 8),
    _AlcCuN1MaxMsgSize_Type()
)
alcCuN1MaxMsgSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alcCuN1MaxMsgSize.setStatus("mandatory")


class _AlcCuT1PollRspTimer_Type(Integer32):
    """Custom type alcCuT1PollRspTimer based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_AlcCuT1PollRspTimer_Type.__name__ = "Integer32"
_AlcCuT1PollRspTimer_Object = MibTableColumn
alcCuT1PollRspTimer = _AlcCuT1PollRspTimer_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 10, 1, 3, 1, 9),
    _AlcCuT1PollRspTimer_Type()
)
alcCuT1PollRspTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alcCuT1PollRspTimer.setStatus("mandatory")


class _AlcCuT2MaxRxTimer_Type(Integer32):
    """Custom type alcCuT2MaxRxTimer based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65),
    )


_AlcCuT2MaxRxTimer_Type.__name__ = "Integer32"
_AlcCuT2MaxRxTimer_Object = MibTableColumn
alcCuT2MaxRxTimer = _AlcCuT2MaxRxTimer_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 10, 1, 3, 1, 10),
    _AlcCuT2MaxRxTimer_Type()
)
alcCuT2MaxRxTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alcCuT2MaxRxTimer.setStatus("mandatory")


class _AlcCuT4NoPollTime_Type(Integer32):
    """Custom type alcCuT4NoPollTime based on Integer32"""
    defaultValue = 3000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_AlcCuT4NoPollTime_Type.__name__ = "Integer32"
_AlcCuT4NoPollTime_Object = MibTableColumn
alcCuT4NoPollTime = _AlcCuT4NoPollTime_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 10, 1, 3, 1, 11),
    _AlcCuT4NoPollTime_Type()
)
alcCuT4NoPollTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alcCuT4NoPollTime.setStatus("mandatory")


class _AlcCuC1UpCounter_Type(Integer32):
    """Custom type alcCuC1UpCounter based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AlcCuC1UpCounter_Type.__name__ = "Integer32"
_AlcCuC1UpCounter_Object = MibTableColumn
alcCuC1UpCounter = _AlcCuC1UpCounter_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 10, 1, 3, 1, 12),
    _AlcCuC1UpCounter_Type()
)
alcCuC1UpCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alcCuC1UpCounter.setStatus("mandatory")


class _AlcCuC2DownCounter_Type(Integer32):
    """Custom type alcCuC2DownCounter based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AlcCuC2DownCounter_Type.__name__ = "Integer32"
_AlcCuC2DownCounter_Object = MibTableColumn
alcCuC2DownCounter = _AlcCuC2DownCounter_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 10, 1, 3, 1, 13),
    _AlcCuC2DownCounter_Type()
)
alcCuC2DownCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alcCuC2DownCounter.setStatus("mandatory")


class _AlcCuN2MaxMsgPerPoll_Type(Integer32):
    """Custom type alcCuN2MaxMsgPerPoll based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AlcCuN2MaxMsgPerPoll_Type.__name__ = "Integer32"
_AlcCuN2MaxMsgPerPoll_Object = MibTableColumn
alcCuN2MaxMsgPerPoll = _AlcCuN2MaxMsgPerPoll_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 10, 1, 3, 1, 14),
    _AlcCuN2MaxMsgPerPoll_Type()
)
alcCuN2MaxMsgPerPoll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alcCuN2MaxMsgPerPoll.setStatus("mandatory")


class _AlcCuMaxCharPerPoll_Type(Integer32):
    """Custom type alcCuMaxCharPerPoll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_AlcCuMaxCharPerPoll_Type.__name__ = "Integer32"
_AlcCuMaxCharPerPoll_Object = MibTableColumn
alcCuMaxCharPerPoll = _AlcCuMaxCharPerPoll_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 10, 1, 3, 1, 15),
    _AlcCuMaxCharPerPoll_Type()
)
alcCuMaxCharPerPoll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alcCuMaxCharPerPoll.setStatus("mandatory")


class _AlcCuN3PollsTillAlive_Type(Integer32):
    """Custom type alcCuN3PollsTillAlive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AlcCuN3PollsTillAlive_Type.__name__ = "Integer32"
_AlcCuN3PollsTillAlive_Object = MibTableColumn
alcCuN3PollsTillAlive = _AlcCuN3PollsTillAlive_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 10, 1, 3, 1, 16),
    _AlcCuN3PollsTillAlive_Type()
)
alcCuN3PollsTillAlive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alcCuN3PollsTillAlive.setStatus("mandatory")


class _AlcCuN4PollsTillDead_Type(Integer32):
    """Custom type alcCuN4PollsTillDead based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AlcCuN4PollsTillDead_Type.__name__ = "Integer32"
_AlcCuN4PollsTillDead_Object = MibTableColumn
alcCuN4PollsTillDead = _AlcCuN4PollsTillDead_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 10, 1, 3, 1, 17),
    _AlcCuN4PollsTillDead_Type()
)
alcCuN4PollsTillDead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alcCuN4PollsTillDead.setStatus("mandatory")


class _AlcCuIAResetOption_Type(Integer32):
    """Custom type alcCuIAResetOption based on Integer32"""
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


_AlcCuIAResetOption_Type.__name__ = "Integer32"
_AlcCuIAResetOption_Object = MibTableColumn
alcCuIAResetOption = _AlcCuIAResetOption_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 10, 1, 3, 1, 18),
    _AlcCuIAResetOption_Type()
)
alcCuIAResetOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alcCuIAResetOption.setStatus("mandatory")


class _AlcCuIAValidationOption_Type(Integer32):
    """Custom type alcCuIAValidationOption based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("garbled", 3),
          ("none", 1),
          ("responding-stream", 2))
    )


_AlcCuIAValidationOption_Type.__name__ = "Integer32"
_AlcCuIAValidationOption_Object = MibTableColumn
alcCuIAValidationOption = _AlcCuIAValidationOption_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 10, 1, 3, 1, 19),
    _AlcCuIAValidationOption_Type()
)
alcCuIAValidationOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alcCuIAValidationOption.setStatus("mandatory")


class _AlcCuRxCCCOption_Type(DisplayString):
    """Custom type alcCuRxCCCOption based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AlcCuRxCCCOption_Type.__name__ = "DisplayString"
_AlcCuRxCCCOption_Object = MibTableColumn
alcCuRxCCCOption = _AlcCuRxCCCOption_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 10, 1, 3, 1, 20),
    _AlcCuRxCCCOption_Type()
)
alcCuRxCCCOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alcCuRxCCCOption.setStatus("mandatory")


class _AlcCuMaxFrame_Type(Integer32):
    """Custom type alcCuMaxFrame based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AlcCuMaxFrame_Type.__name__ = "Integer32"
_AlcCuMaxFrame_Object = MibTableColumn
alcCuMaxFrame = _AlcCuMaxFrame_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 10, 1, 3, 1, 21),
    _AlcCuMaxFrame_Type()
)
alcCuMaxFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alcCuMaxFrame.setStatus("mandatory")


class _AlcCuSvcMsgHeader_Type(DisplayString):
    """Custom type alcCuSvcMsgHeader based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AlcCuSvcMsgHeader_Type.__name__ = "DisplayString"
_AlcCuSvcMsgHeader_Object = MibTableColumn
alcCuSvcMsgHeader = _AlcCuSvcMsgHeader_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 10, 1, 3, 1, 22),
    _AlcCuSvcMsgHeader_Type()
)
alcCuSvcMsgHeader.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alcCuSvcMsgHeader.setStatus("mandatory")


class _AlcCuSvcMsgIndex_Type(Integer32):
    """Custom type alcCuSvcMsgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AlcCuSvcMsgIndex_Type.__name__ = "Integer32"
_AlcCuSvcMsgIndex_Object = MibTableColumn
alcCuSvcMsgIndex = _AlcCuSvcMsgIndex_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 10, 1, 3, 1, 23),
    _AlcCuSvcMsgIndex_Type()
)
alcCuSvcMsgIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alcCuSvcMsgIndex.setStatus("mandatory")


class _AlcCuSvcMsgTrailer_Type(DisplayString):
    """Custom type alcCuSvcMsgTrailer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AlcCuSvcMsgTrailer_Type.__name__ = "DisplayString"
_AlcCuSvcMsgTrailer_Object = MibTableColumn
alcCuSvcMsgTrailer = _AlcCuSvcMsgTrailer_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 10, 1, 3, 1, 24),
    _AlcCuSvcMsgTrailer_Type()
)
alcCuSvcMsgTrailer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alcCuSvcMsgTrailer.setStatus("mandatory")
_AlcCuStatusChanges_Type = Counter32
_AlcCuStatusChanges_Object = MibTableColumn
alcCuStatusChanges = _AlcCuStatusChanges_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 10, 1, 3, 1, 25),
    _AlcCuStatusChanges_Type()
)
alcCuStatusChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcCuStatusChanges.setStatus("mandatory")
_AlcCuRxFrames_Type = Counter32
_AlcCuRxFrames_Object = MibTableColumn
alcCuRxFrames = _AlcCuRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 10, 1, 3, 1, 26),
    _AlcCuRxFrames_Type()
)
alcCuRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcCuRxFrames.setStatus("mandatory")
_AlcCuTxFrames_Type = Counter32
_AlcCuTxFrames_Object = MibTableColumn
alcCuTxFrames = _AlcCuTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 10, 1, 3, 1, 27),
    _AlcCuTxFrames_Type()
)
alcCuTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcCuTxFrames.setStatus("mandatory")
_AlcCuRxChars_Type = Counter32
_AlcCuRxChars_Object = MibTableColumn
alcCuRxChars = _AlcCuRxChars_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 10, 1, 3, 1, 28),
    _AlcCuRxChars_Type()
)
alcCuRxChars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcCuRxChars.setStatus("mandatory")
_AlcCuTxChars_Type = Counter32
_AlcCuTxChars_Object = MibTableColumn
alcCuTxChars = _AlcCuTxChars_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 10, 1, 3, 1, 29),
    _AlcCuTxChars_Type()
)
alcCuTxChars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcCuTxChars.setStatus("mandatory")


class _AlcCuStatusTrapControl_Type(Integer32):
    """Custom type alcCuStatusTrapControl based on Integer32"""
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


_AlcCuStatusTrapControl_Type.__name__ = "Integer32"
_AlcCuStatusTrapControl_Object = MibTableColumn
alcCuStatusTrapControl = _AlcCuStatusTrapControl_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 10, 1, 3, 1, 30),
    _AlcCuStatusTrapControl_Type()
)
alcCuStatusTrapControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alcCuStatusTrapControl.setStatus("mandatory")
_AlcCuDropped_Type = Counter32
_AlcCuDropped_Object = MibTableColumn
alcCuDropped = _AlcCuDropped_Object(
    (1, 3, 6, 1, 4, 1, 1978, 2, 10, 1, 3, 1, 31),
    _AlcCuDropped_Type()
)
alcCuDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alcCuDropped.setStatus("mandatory")
_AlcTraps_ObjectIdentity = ObjectIdentity
alcTraps = _AlcTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1978, 2, 10, 2)
)
_AlcLineTraps_ObjectIdentity = ObjectIdentity
alcLineTraps = _AlcLineTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1978, 2, 10, 2, 1)
)
_AlcCuTraps_ObjectIdentity = ObjectIdentity
alcCuTraps = _AlcCuTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1978, 2, 10, 2, 2)
)

# Managed Objects groups


# Notification objects

alcLineError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1978, 2, 10, 2, 1, 0, 1)
)
alcLineError.setObjects(
      *(("ALC-MIB", "alcLineIfIndex"),
        ("ALC-MIB", "alcTrapReason"),
        ("RS-232-MIB", "rs232PortIndex"))
)
if mibBuilder.loadTexts:
    alcLineError.setStatus(
        ""
    )

alcCuState = NotificationType(
    (1, 3, 6, 1, 4, 1, 1978, 2, 10, 2, 2, 0, 1)
)
alcCuState.setObjects(
      *(("ALC-MIB", "alcCuIfIndex"),
        ("ALC-MIB", "alcCuIA"),
        ("ALC-MIB", "alcCuStatus"),
        ("RS-232-MIB", "rs232PortIndex"))
)
if mibBuilder.loadTexts:
    alcCuState.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALC-MIB",
    **{"NonNegativeInteger": NonNegativeInteger,
       "InterfaceIndex": InterfaceIndex,
       "ngcan": ngcan,
       "tiger": tiger,
       "alcMIB": alcMIB,
       "alcLine": alcLine,
       "alcNumLines": alcNumLines,
       "alcLineTable": alcLineTable,
       "alcLineEntry": alcLineEntry,
       "alcLineIfIndex": alcLineIfIndex,
       "alcLineStationType": alcLineStationType,
       "alcNumCuConfiged": alcNumCuConfiged,
       "alcDuplexOptions": alcDuplexOptions,
       "alcT3MinCycleTime": alcT3MinCycleTime,
       "alcT6SegmentedMsgTimer": alcT6SegmentedMsgTimer,
       "alcN5LiveDeadRatio": alcN5LiveDeadRatio,
       "alcSegmentOption": alcSegmentOption,
       "alcReassembleOption": alcReassembleOption,
       "alcWildIAPoll": alcWildIAPoll,
       "alcNumOfIdles": alcNumOfIdles,
       "alcInterMsgSync": alcInterMsgSync,
       "alcNIA": alcNIA,
       "alcTxOverlengthFrames": alcTxOverlengthFrames,
       "alcRxOverlengthFrames": alcRxOverlengthFrames,
       "alcInvalidAddresses": alcInvalidAddresses,
       "alcRxT2Expireds": alcRxT2Expireds,
       "alcDroppedMsgs": alcDroppedMsgs,
       "alcRxOverlengthFramesThres": alcRxOverlengthFramesThres,
       "alcInvalidAddressThres": alcInvalidAddressThres,
       "alcRxT2ExpiredThres": alcRxT2ExpiredThres,
       "alcTrapReason": alcTrapReason,
       "alcErrData": alcErrData,
       "alcCuTable": alcCuTable,
       "alcCuEntry": alcCuEntry,
       "alcCuIfIndex": alcCuIfIndex,
       "alcCuDescr": alcCuDescr,
       "alcCuIA": alcCuIA,
       "alcCuStatus": alcCuStatus,
       "alcCuPollCmd": alcCuPollCmd,
       "alcCuOutQueueMsgSize": alcCuOutQueueMsgSize,
       "alcCuOutQueueCharSize": alcCuOutQueueCharSize,
       "alcCuN1MaxMsgSize": alcCuN1MaxMsgSize,
       "alcCuT1PollRspTimer": alcCuT1PollRspTimer,
       "alcCuT2MaxRxTimer": alcCuT2MaxRxTimer,
       "alcCuT4NoPollTime": alcCuT4NoPollTime,
       "alcCuC1UpCounter": alcCuC1UpCounter,
       "alcCuC2DownCounter": alcCuC2DownCounter,
       "alcCuN2MaxMsgPerPoll": alcCuN2MaxMsgPerPoll,
       "alcCuMaxCharPerPoll": alcCuMaxCharPerPoll,
       "alcCuN3PollsTillAlive": alcCuN3PollsTillAlive,
       "alcCuN4PollsTillDead": alcCuN4PollsTillDead,
       "alcCuIAResetOption": alcCuIAResetOption,
       "alcCuIAValidationOption": alcCuIAValidationOption,
       "alcCuRxCCCOption": alcCuRxCCCOption,
       "alcCuMaxFrame": alcCuMaxFrame,
       "alcCuSvcMsgHeader": alcCuSvcMsgHeader,
       "alcCuSvcMsgIndex": alcCuSvcMsgIndex,
       "alcCuSvcMsgTrailer": alcCuSvcMsgTrailer,
       "alcCuStatusChanges": alcCuStatusChanges,
       "alcCuRxFrames": alcCuRxFrames,
       "alcCuTxFrames": alcCuTxFrames,
       "alcCuRxChars": alcCuRxChars,
       "alcCuTxChars": alcCuTxChars,
       "alcCuStatusTrapControl": alcCuStatusTrapControl,
       "alcCuDropped": alcCuDropped,
       "alcTraps": alcTraps,
       "alcLineTraps": alcLineTraps,
       "alcLineError": alcLineError,
       "alcCuTraps": alcCuTraps,
       "alcCuState": alcCuState}
)
