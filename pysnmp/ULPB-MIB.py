# SNMP MIB module (ULPB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ULPB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:08:27 2024
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
 experimental,
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
    "experimental",
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

_Usr_ObjectIdentity = ObjectIdentity
usr = _Usr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429)
)
_Nas_ObjectIdentity = ObjectIdentity
nas = _Nas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1)
)
_Ulpb_ObjectIdentity = ObjectIdentity
ulpb = _Ulpb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 9)
)
_UlpbAdmnTable_Object = MibTable
ulpbAdmnTable = _UlpbAdmnTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 9, 1)
)
if mibBuilder.loadTexts:
    ulpbAdmnTable.setStatus("mandatory")
_UlpbAdmnEntry_Object = MibTableRow
ulpbAdmnEntry = _UlpbAdmnEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 9, 1, 1)
)
ulpbAdmnEntry.setIndexNames(
    (0, "ULPB-MIB", "ulpbAdmnIndex"),
)
if mibBuilder.loadTexts:
    ulpbAdmnEntry.setStatus("mandatory")
_UlpbAdmnIndex_Type = Integer32
_UlpbAdmnIndex_Object = MibTableColumn
ulpbAdmnIndex = _UlpbAdmnIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 9, 1, 1, 1),
    _UlpbAdmnIndex_Type()
)
ulpbAdmnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulpbAdmnIndex.setStatus("mandatory")


class _UlpbAdmnN2ReXmitVal_Type(Integer32):
    """Custom type ulpbAdmnN2ReXmitVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_UlpbAdmnN2ReXmitVal_Type.__name__ = "Integer32"
_UlpbAdmnN2ReXmitVal_Object = MibTableColumn
ulpbAdmnN2ReXmitVal = _UlpbAdmnN2ReXmitVal_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 9, 1, 1, 2),
    _UlpbAdmnN2ReXmitVal_Type()
)
ulpbAdmnN2ReXmitVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ulpbAdmnN2ReXmitVal.setStatus("mandatory")


class _UlpbAdmnT1AckTime_Type(Integer32):
    """Custom type ulpbAdmnT1AckTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3000),
    )


_UlpbAdmnT1AckTime_Type.__name__ = "Integer32"
_UlpbAdmnT1AckTime_Object = MibTableColumn
ulpbAdmnT1AckTime = _UlpbAdmnT1AckTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 9, 1, 1, 3),
    _UlpbAdmnT1AckTime_Type()
)
ulpbAdmnT1AckTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ulpbAdmnT1AckTime.setStatus("mandatory")


class _UlpbAdmnTpfVal_Type(Integer32):
    """Custom type ulpbAdmnTpfVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3000),
    )


_UlpbAdmnTpfVal_Type.__name__ = "Integer32"
_UlpbAdmnTpfVal_Object = MibTableColumn
ulpbAdmnTpfVal = _UlpbAdmnTpfVal_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 9, 1, 1, 4),
    _UlpbAdmnTpfVal_Type()
)
ulpbAdmnTpfVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ulpbAdmnTpfVal.setStatus("mandatory")


class _UlpbAdmnTrejVal_Type(Integer32):
    """Custom type ulpbAdmnTrejVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_UlpbAdmnTrejVal_Type.__name__ = "Integer32"
_UlpbAdmnTrejVal_Object = MibTableColumn
ulpbAdmnTrejVal = _UlpbAdmnTrejVal_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 9, 1, 1, 5),
    _UlpbAdmnTrejVal_Type()
)
ulpbAdmnTrejVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ulpbAdmnTrejVal.setStatus("mandatory")


class _UlpbAdmnTbusyVal_Type(Integer32):
    """Custom type ulpbAdmnTbusyVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30000),
    )


_UlpbAdmnTbusyVal_Type.__name__ = "Integer32"
_UlpbAdmnTbusyVal_Object = MibTableColumn
ulpbAdmnTbusyVal = _UlpbAdmnTbusyVal_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 9, 1, 1, 6),
    _UlpbAdmnTbusyVal_Type()
)
ulpbAdmnTbusyVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ulpbAdmnTbusyVal.setStatus("mandatory")


class _UlpbAdmnLinkIdleTime_Type(Integer32):
    """Custom type ulpbAdmnLinkIdleTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_UlpbAdmnLinkIdleTime_Type.__name__ = "Integer32"
_UlpbAdmnLinkIdleTime_Object = MibTableColumn
ulpbAdmnLinkIdleTime = _UlpbAdmnLinkIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 9, 1, 1, 7),
    _UlpbAdmnLinkIdleTime_Type()
)
ulpbAdmnLinkIdleTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ulpbAdmnLinkIdleTime.setStatus("mandatory")


class _UlpbAdmnT2AckDelayTime_Type(Integer32):
    """Custom type ulpbAdmnT2AckDelayTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3000),
    )


_UlpbAdmnT2AckDelayTime_Type.__name__ = "Integer32"
_UlpbAdmnT2AckDelayTime_Object = MibTableColumn
ulpbAdmnT2AckDelayTime = _UlpbAdmnT2AckDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 9, 1, 1, 8),
    _UlpbAdmnT2AckDelayTime_Type()
)
ulpbAdmnT2AckDelayTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ulpbAdmnT2AckDelayTime.setStatus("mandatory")


class _UlpbAdmnRecKWindowSz_Type(Integer32):
    """Custom type ulpbAdmnRecKWindowSz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_UlpbAdmnRecKWindowSz_Type.__name__ = "Integer32"
_UlpbAdmnRecKWindowSz_Object = MibTableColumn
ulpbAdmnRecKWindowSz = _UlpbAdmnRecKWindowSz_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 9, 1, 1, 9),
    _UlpbAdmnRecKWindowSz_Type()
)
ulpbAdmnRecKWindowSz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ulpbAdmnRecKWindowSz.setStatus("mandatory")


class _UlpbAdmnXmitKWindowSz_Type(Integer32):
    """Custom type ulpbAdmnXmitKWindowSz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_UlpbAdmnXmitKWindowSz_Type.__name__ = "Integer32"
_UlpbAdmnXmitKWindowSz_Object = MibTableColumn
ulpbAdmnXmitKWindowSz = _UlpbAdmnXmitKWindowSz_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 9, 1, 1, 10),
    _UlpbAdmnXmitKWindowSz_Type()
)
ulpbAdmnXmitKWindowSz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ulpbAdmnXmitKWindowSz.setStatus("mandatory")


class _UlpbAdmnLocProbe_Type(Integer32):
    """Custom type ulpbAdmnLocProbe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_UlpbAdmnLocProbe_Type.__name__ = "Integer32"
_UlpbAdmnLocProbe_Object = MibTableColumn
ulpbAdmnLocProbe = _UlpbAdmnLocProbe_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 9, 1, 1, 11),
    _UlpbAdmnLocProbe_Type()
)
ulpbAdmnLocProbe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ulpbAdmnLocProbe.setStatus("mandatory")


class _UlpbAdmnMaxRecFrmSz_Type(Integer32):
    """Custom type ulpbAdmnMaxRecFrmSz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(133, 519),
    )


_UlpbAdmnMaxRecFrmSz_Type.__name__ = "Integer32"
_UlpbAdmnMaxRecFrmSz_Object = MibTableColumn
ulpbAdmnMaxRecFrmSz = _UlpbAdmnMaxRecFrmSz_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 9, 1, 1, 12),
    _UlpbAdmnMaxRecFrmSz_Type()
)
ulpbAdmnMaxRecFrmSz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ulpbAdmnMaxRecFrmSz.setStatus("mandatory")


class _UlpbAdmnIgnUaError_Type(Integer32):
    """Custom type ulpbAdmnIgnUaError based on Integer32"""
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


_UlpbAdmnIgnUaError_Type.__name__ = "Integer32"
_UlpbAdmnIgnUaError_Object = MibTableColumn
ulpbAdmnIgnUaError = _UlpbAdmnIgnUaError_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 9, 1, 1, 13),
    _UlpbAdmnIgnUaError_Type()
)
ulpbAdmnIgnUaError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ulpbAdmnIgnUaError.setStatus("mandatory")


class _UlpbAdmnFrmrFrmrError_Type(Integer32):
    """Custom type ulpbAdmnFrmrFrmrError based on Integer32"""
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


_UlpbAdmnFrmrFrmrError_Type.__name__ = "Integer32"
_UlpbAdmnFrmrFrmrError_Object = MibTableColumn
ulpbAdmnFrmrFrmrError = _UlpbAdmnFrmrFrmrError_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 9, 1, 1, 14),
    _UlpbAdmnFrmrFrmrError_Type()
)
ulpbAdmnFrmrFrmrError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ulpbAdmnFrmrFrmrError.setStatus("mandatory")


class _UlpbAdmnFrmrInvrspError_Type(Integer32):
    """Custom type ulpbAdmnFrmrInvrspError based on Integer32"""
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


_UlpbAdmnFrmrInvrspError_Type.__name__ = "Integer32"
_UlpbAdmnFrmrInvrspError_Object = MibTableColumn
ulpbAdmnFrmrInvrspError = _UlpbAdmnFrmrInvrspError_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 9, 1, 1, 15),
    _UlpbAdmnFrmrInvrspError_Type()
)
ulpbAdmnFrmrInvrspError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ulpbAdmnFrmrInvrspError.setStatus("mandatory")


class _UlpbAdmnSframePbit_Type(Integer32):
    """Custom type ulpbAdmnSframePbit based on Integer32"""
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


_UlpbAdmnSframePbit_Type.__name__ = "Integer32"
_UlpbAdmnSframePbit_Object = MibTableColumn
ulpbAdmnSframePbit = _UlpbAdmnSframePbit_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 9, 1, 1, 16),
    _UlpbAdmnSframePbit_Type()
)
ulpbAdmnSframePbit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ulpbAdmnSframePbit.setStatus("mandatory")


class _UlpbAdmnDmOnAdm_Type(Integer32):
    """Custom type ulpbAdmnDmOnAdm based on Integer32"""
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


_UlpbAdmnDmOnAdm_Type.__name__ = "Integer32"
_UlpbAdmnDmOnAdm_Object = MibTableColumn
ulpbAdmnDmOnAdm = _UlpbAdmnDmOnAdm_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 9, 1, 1, 17),
    _UlpbAdmnDmOnAdm_Type()
)
ulpbAdmnDmOnAdm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ulpbAdmnDmOnAdm.setStatus("mandatory")
_UlpbOperTable_Object = MibTable
ulpbOperTable = _UlpbOperTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 9, 2)
)
if mibBuilder.loadTexts:
    ulpbOperTable.setStatus("mandatory")
_UlpbOperEntry_Object = MibTableRow
ulpbOperEntry = _UlpbOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 9, 2, 1)
)
ulpbOperEntry.setIndexNames(
    (0, "ULPB-MIB", "ulpbOperIndex"),
)
if mibBuilder.loadTexts:
    ulpbOperEntry.setStatus("mandatory")
_UlpbOperIndex_Type = Integer32
_UlpbOperIndex_Object = MibTableColumn
ulpbOperIndex = _UlpbOperIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 9, 2, 1, 1),
    _UlpbOperIndex_Type()
)
ulpbOperIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulpbOperIndex.setStatus("mandatory")


class _UlpbOperN2ReXmitVal_Type(Integer32):
    """Custom type ulpbOperN2ReXmitVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_UlpbOperN2ReXmitVal_Type.__name__ = "Integer32"
_UlpbOperN2ReXmitVal_Object = MibTableColumn
ulpbOperN2ReXmitVal = _UlpbOperN2ReXmitVal_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 9, 2, 1, 2),
    _UlpbOperN2ReXmitVal_Type()
)
ulpbOperN2ReXmitVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulpbOperN2ReXmitVal.setStatus("mandatory")


class _UlpbOperT1AckTime_Type(Integer32):
    """Custom type ulpbOperT1AckTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3000),
    )


_UlpbOperT1AckTime_Type.__name__ = "Integer32"
_UlpbOperT1AckTime_Object = MibTableColumn
ulpbOperT1AckTime = _UlpbOperT1AckTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 9, 2, 1, 3),
    _UlpbOperT1AckTime_Type()
)
ulpbOperT1AckTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulpbOperT1AckTime.setStatus("mandatory")


class _UlpbOperTpfVal_Type(Integer32):
    """Custom type ulpbOperTpfVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3000),
    )


_UlpbOperTpfVal_Type.__name__ = "Integer32"
_UlpbOperTpfVal_Object = MibTableColumn
ulpbOperTpfVal = _UlpbOperTpfVal_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 9, 2, 1, 4),
    _UlpbOperTpfVal_Type()
)
ulpbOperTpfVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulpbOperTpfVal.setStatus("mandatory")


class _UlpbOperTrejVal_Type(Integer32):
    """Custom type ulpbOperTrejVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_UlpbOperTrejVal_Type.__name__ = "Integer32"
_UlpbOperTrejVal_Object = MibTableColumn
ulpbOperTrejVal = _UlpbOperTrejVal_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 9, 2, 1, 5),
    _UlpbOperTrejVal_Type()
)
ulpbOperTrejVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulpbOperTrejVal.setStatus("mandatory")


class _UlpbOperTbusyVal_Type(Integer32):
    """Custom type ulpbOperTbusyVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30000),
    )


_UlpbOperTbusyVal_Type.__name__ = "Integer32"
_UlpbOperTbusyVal_Object = MibTableColumn
ulpbOperTbusyVal = _UlpbOperTbusyVal_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 9, 2, 1, 6),
    _UlpbOperTbusyVal_Type()
)
ulpbOperTbusyVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulpbOperTbusyVal.setStatus("mandatory")


class _UlpbOperLinkIdleTime_Type(Integer32):
    """Custom type ulpbOperLinkIdleTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_UlpbOperLinkIdleTime_Type.__name__ = "Integer32"
_UlpbOperLinkIdleTime_Object = MibTableColumn
ulpbOperLinkIdleTime = _UlpbOperLinkIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 9, 2, 1, 7),
    _UlpbOperLinkIdleTime_Type()
)
ulpbOperLinkIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulpbOperLinkIdleTime.setStatus("mandatory")


class _UlpbOperT2AckDelayTime_Type(Integer32):
    """Custom type ulpbOperT2AckDelayTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3000),
    )


_UlpbOperT2AckDelayTime_Type.__name__ = "Integer32"
_UlpbOperT2AckDelayTime_Object = MibTableColumn
ulpbOperT2AckDelayTime = _UlpbOperT2AckDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 9, 2, 1, 8),
    _UlpbOperT2AckDelayTime_Type()
)
ulpbOperT2AckDelayTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulpbOperT2AckDelayTime.setStatus("mandatory")


class _UlpbOperRecKWindowSz_Type(Integer32):
    """Custom type ulpbOperRecKWindowSz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_UlpbOperRecKWindowSz_Type.__name__ = "Integer32"
_UlpbOperRecKWindowSz_Object = MibTableColumn
ulpbOperRecKWindowSz = _UlpbOperRecKWindowSz_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 9, 2, 1, 9),
    _UlpbOperRecKWindowSz_Type()
)
ulpbOperRecKWindowSz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulpbOperRecKWindowSz.setStatus("mandatory")


class _UlpbOperXmitKWindowSz_Type(Integer32):
    """Custom type ulpbOperXmitKWindowSz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_UlpbOperXmitKWindowSz_Type.__name__ = "Integer32"
_UlpbOperXmitKWindowSz_Object = MibTableColumn
ulpbOperXmitKWindowSz = _UlpbOperXmitKWindowSz_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 9, 2, 1, 10),
    _UlpbOperXmitKWindowSz_Type()
)
ulpbOperXmitKWindowSz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulpbOperXmitKWindowSz.setStatus("mandatory")


class _UlpbOperLocProbe_Type(Integer32):
    """Custom type ulpbOperLocProbe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_UlpbOperLocProbe_Type.__name__ = "Integer32"
_UlpbOperLocProbe_Object = MibTableColumn
ulpbOperLocProbe = _UlpbOperLocProbe_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 9, 2, 1, 11),
    _UlpbOperLocProbe_Type()
)
ulpbOperLocProbe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulpbOperLocProbe.setStatus("mandatory")


class _UlpbOperMaxRecFrmSz_Type(Integer32):
    """Custom type ulpbOperMaxRecFrmSz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(133, 519),
    )


_UlpbOperMaxRecFrmSz_Type.__name__ = "Integer32"
_UlpbOperMaxRecFrmSz_Object = MibTableColumn
ulpbOperMaxRecFrmSz = _UlpbOperMaxRecFrmSz_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 9, 2, 1, 12),
    _UlpbOperMaxRecFrmSz_Type()
)
ulpbOperMaxRecFrmSz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulpbOperMaxRecFrmSz.setStatus("mandatory")


class _UlpbOperIgnUaError_Type(Integer32):
    """Custom type ulpbOperIgnUaError based on Integer32"""
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


_UlpbOperIgnUaError_Type.__name__ = "Integer32"
_UlpbOperIgnUaError_Object = MibTableColumn
ulpbOperIgnUaError = _UlpbOperIgnUaError_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 9, 2, 1, 13),
    _UlpbOperIgnUaError_Type()
)
ulpbOperIgnUaError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulpbOperIgnUaError.setStatus("mandatory")


class _UlpbOperFrmrFrmrError_Type(Integer32):
    """Custom type ulpbOperFrmrFrmrError based on Integer32"""
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


_UlpbOperFrmrFrmrError_Type.__name__ = "Integer32"
_UlpbOperFrmrFrmrError_Object = MibTableColumn
ulpbOperFrmrFrmrError = _UlpbOperFrmrFrmrError_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 9, 2, 1, 14),
    _UlpbOperFrmrFrmrError_Type()
)
ulpbOperFrmrFrmrError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulpbOperFrmrFrmrError.setStatus("mandatory")


class _UlpbOperFrmrInvrspError_Type(Integer32):
    """Custom type ulpbOperFrmrInvrspError based on Integer32"""
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


_UlpbOperFrmrInvrspError_Type.__name__ = "Integer32"
_UlpbOperFrmrInvrspError_Object = MibTableColumn
ulpbOperFrmrInvrspError = _UlpbOperFrmrInvrspError_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 9, 2, 1, 15),
    _UlpbOperFrmrInvrspError_Type()
)
ulpbOperFrmrInvrspError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulpbOperFrmrInvrspError.setStatus("mandatory")


class _UlpbOperSframePbit_Type(Integer32):
    """Custom type ulpbOperSframePbit based on Integer32"""
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


_UlpbOperSframePbit_Type.__name__ = "Integer32"
_UlpbOperSframePbit_Object = MibTableColumn
ulpbOperSframePbit = _UlpbOperSframePbit_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 9, 2, 1, 16),
    _UlpbOperSframePbit_Type()
)
ulpbOperSframePbit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulpbOperSframePbit.setStatus("mandatory")


class _UlpbOperDmOnAdm_Type(Integer32):
    """Custom type ulpbOperDmOnAdm based on Integer32"""
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


_UlpbOperDmOnAdm_Type.__name__ = "Integer32"
_UlpbOperDmOnAdm_Object = MibTableColumn
ulpbOperDmOnAdm = _UlpbOperDmOnAdm_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 9, 2, 1, 17),
    _UlpbOperDmOnAdm_Type()
)
ulpbOperDmOnAdm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulpbOperDmOnAdm.setStatus("mandatory")
_UlpbStatTable_Object = MibTable
ulpbStatTable = _UlpbStatTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 9, 3)
)
if mibBuilder.loadTexts:
    ulpbStatTable.setStatus("mandatory")
_UlpbStatEntry_Object = MibTableRow
ulpbStatEntry = _UlpbStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 9, 3, 1)
)
ulpbStatEntry.setIndexNames(
    (0, "ULPB-MIB", "ulpbStatIndex"),
)
if mibBuilder.loadTexts:
    ulpbStatEntry.setStatus("mandatory")
_UlpbStatIndex_Type = Integer32
_UlpbStatIndex_Object = MibTableColumn
ulpbStatIndex = _UlpbStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 9, 3, 1, 1),
    _UlpbStatIndex_Type()
)
ulpbStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulpbStatIndex.setStatus("mandatory")
_UlpbStatRRCmdsRcvd_Type = Integer32
_UlpbStatRRCmdsRcvd_Object = MibTableColumn
ulpbStatRRCmdsRcvd = _UlpbStatRRCmdsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 9, 3, 1, 2),
    _UlpbStatRRCmdsRcvd_Type()
)
ulpbStatRRCmdsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulpbStatRRCmdsRcvd.setStatus("mandatory")
_UlpbStatRRCmdsTrnsmt_Type = Integer32
_UlpbStatRRCmdsTrnsmt_Object = MibTableColumn
ulpbStatRRCmdsTrnsmt = _UlpbStatRRCmdsTrnsmt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 9, 3, 1, 3),
    _UlpbStatRRCmdsTrnsmt_Type()
)
ulpbStatRRCmdsTrnsmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulpbStatRRCmdsTrnsmt.setStatus("mandatory")
_UlpbStatRRRspsRcvd_Type = Integer32
_UlpbStatRRRspsRcvd_Object = MibTableColumn
ulpbStatRRRspsRcvd = _UlpbStatRRRspsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 9, 3, 1, 4),
    _UlpbStatRRRspsRcvd_Type()
)
ulpbStatRRRspsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulpbStatRRRspsRcvd.setStatus("mandatory")
_UlpbStatRRRspsTrnsmt_Type = Integer32
_UlpbStatRRRspsTrnsmt_Object = MibTableColumn
ulpbStatRRRspsTrnsmt = _UlpbStatRRRspsTrnsmt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 9, 3, 1, 5),
    _UlpbStatRRRspsTrnsmt_Type()
)
ulpbStatRRRspsTrnsmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulpbStatRRRspsTrnsmt.setStatus("mandatory")
_UlpbStatRNRCmdsRcvd_Type = Integer32
_UlpbStatRNRCmdsRcvd_Object = MibTableColumn
ulpbStatRNRCmdsRcvd = _UlpbStatRNRCmdsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 9, 3, 1, 6),
    _UlpbStatRNRCmdsRcvd_Type()
)
ulpbStatRNRCmdsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulpbStatRNRCmdsRcvd.setStatus("mandatory")
_UlpbStatRNRCmdsTrnsmt_Type = Integer32
_UlpbStatRNRCmdsTrnsmt_Object = MibTableColumn
ulpbStatRNRCmdsTrnsmt = _UlpbStatRNRCmdsTrnsmt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 9, 3, 1, 7),
    _UlpbStatRNRCmdsTrnsmt_Type()
)
ulpbStatRNRCmdsTrnsmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulpbStatRNRCmdsTrnsmt.setStatus("mandatory")
_UlpbStatRNRRspsRcvd_Type = Integer32
_UlpbStatRNRRspsRcvd_Object = MibTableColumn
ulpbStatRNRRspsRcvd = _UlpbStatRNRRspsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 9, 3, 1, 8),
    _UlpbStatRNRRspsRcvd_Type()
)
ulpbStatRNRRspsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulpbStatRNRRspsRcvd.setStatus("mandatory")
_UlpbStatRNRRspsTrnsmt_Type = Integer32
_UlpbStatRNRRspsTrnsmt_Object = MibTableColumn
ulpbStatRNRRspsTrnsmt = _UlpbStatRNRRspsTrnsmt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 9, 3, 1, 9),
    _UlpbStatRNRRspsTrnsmt_Type()
)
ulpbStatRNRRspsTrnsmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulpbStatRNRRspsTrnsmt.setStatus("mandatory")
_UlpbStatREJCmdsRcvd_Type = Integer32
_UlpbStatREJCmdsRcvd_Object = MibTableColumn
ulpbStatREJCmdsRcvd = _UlpbStatREJCmdsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 9, 3, 1, 10),
    _UlpbStatREJCmdsRcvd_Type()
)
ulpbStatREJCmdsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulpbStatREJCmdsRcvd.setStatus("mandatory")
_UlpbStatREJCmdsTrnsmt_Type = Integer32
_UlpbStatREJCmdsTrnsmt_Object = MibTableColumn
ulpbStatREJCmdsTrnsmt = _UlpbStatREJCmdsTrnsmt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 9, 3, 1, 11),
    _UlpbStatREJCmdsTrnsmt_Type()
)
ulpbStatREJCmdsTrnsmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulpbStatREJCmdsTrnsmt.setStatus("mandatory")
_UlpbStatREJRspsRcvd_Type = Integer32
_UlpbStatREJRspsRcvd_Object = MibTableColumn
ulpbStatREJRspsRcvd = _UlpbStatREJRspsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 9, 3, 1, 12),
    _UlpbStatREJRspsRcvd_Type()
)
ulpbStatREJRspsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulpbStatREJRspsRcvd.setStatus("mandatory")
_UlpbStatREJRspsTrnsmt_Type = Integer32
_UlpbStatREJRspsTrnsmt_Object = MibTableColumn
ulpbStatREJRspsTrnsmt = _UlpbStatREJRspsTrnsmt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 9, 3, 1, 13),
    _UlpbStatREJRspsTrnsmt_Type()
)
ulpbStatREJRspsTrnsmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulpbStatREJRspsTrnsmt.setStatus("mandatory")
_UlpbStatSABMCmdsRcvd_Type = Integer32
_UlpbStatSABMCmdsRcvd_Object = MibTableColumn
ulpbStatSABMCmdsRcvd = _UlpbStatSABMCmdsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 9, 3, 1, 14),
    _UlpbStatSABMCmdsRcvd_Type()
)
ulpbStatSABMCmdsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulpbStatSABMCmdsRcvd.setStatus("mandatory")
_UlpbStatSABMCmdsTrnsmt_Type = Integer32
_UlpbStatSABMCmdsTrnsmt_Object = MibTableColumn
ulpbStatSABMCmdsTrnsmt = _UlpbStatSABMCmdsTrnsmt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 9, 3, 1, 15),
    _UlpbStatSABMCmdsTrnsmt_Type()
)
ulpbStatSABMCmdsTrnsmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulpbStatSABMCmdsTrnsmt.setStatus("mandatory")
_UlpbStatDISCCmdsRcvd_Type = Integer32
_UlpbStatDISCCmdsRcvd_Object = MibTableColumn
ulpbStatDISCCmdsRcvd = _UlpbStatDISCCmdsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 9, 3, 1, 16),
    _UlpbStatDISCCmdsRcvd_Type()
)
ulpbStatDISCCmdsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulpbStatDISCCmdsRcvd.setStatus("mandatory")
_UlpbStatDISCCmdsTrnsmt_Type = Integer32
_UlpbStatDISCCmdsTrnsmt_Object = MibTableColumn
ulpbStatDISCCmdsTrnsmt = _UlpbStatDISCCmdsTrnsmt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 9, 3, 1, 17),
    _UlpbStatDISCCmdsTrnsmt_Type()
)
ulpbStatDISCCmdsTrnsmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulpbStatDISCCmdsTrnsmt.setStatus("mandatory")
_UlpbStatDMRspsRcvd_Type = Integer32
_UlpbStatDMRspsRcvd_Object = MibTableColumn
ulpbStatDMRspsRcvd = _UlpbStatDMRspsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 9, 3, 1, 18),
    _UlpbStatDMRspsRcvd_Type()
)
ulpbStatDMRspsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulpbStatDMRspsRcvd.setStatus("mandatory")
_UlpbStatDMRspsTrnsmt_Type = Integer32
_UlpbStatDMRspsTrnsmt_Object = MibTableColumn
ulpbStatDMRspsTrnsmt = _UlpbStatDMRspsTrnsmt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 9, 3, 1, 19),
    _UlpbStatDMRspsTrnsmt_Type()
)
ulpbStatDMRspsTrnsmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulpbStatDMRspsTrnsmt.setStatus("mandatory")
_UlpbStatUARspsRcvd_Type = Integer32
_UlpbStatUARspsRcvd_Object = MibTableColumn
ulpbStatUARspsRcvd = _UlpbStatUARspsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 9, 3, 1, 20),
    _UlpbStatUARspsRcvd_Type()
)
ulpbStatUARspsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulpbStatUARspsRcvd.setStatus("mandatory")
_UlpbStatUARspsTrnsmt_Type = Integer32
_UlpbStatUARspsTrnsmt_Object = MibTableColumn
ulpbStatUARspsTrnsmt = _UlpbStatUARspsTrnsmt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 9, 3, 1, 21),
    _UlpbStatUARspsTrnsmt_Type()
)
ulpbStatUARspsTrnsmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulpbStatUARspsTrnsmt.setStatus("mandatory")
_UlpbStatFRMRRspsRcvd_Type = Integer32
_UlpbStatFRMRRspsRcvd_Object = MibTableColumn
ulpbStatFRMRRspsRcvd = _UlpbStatFRMRRspsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 9, 3, 1, 22),
    _UlpbStatFRMRRspsRcvd_Type()
)
ulpbStatFRMRRspsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulpbStatFRMRRspsRcvd.setStatus("mandatory")
_UlpbStatFRMRRspsTrnsmt_Type = Integer32
_UlpbStatFRMRRspsTrnsmt_Object = MibTableColumn
ulpbStatFRMRRspsTrnsmt = _UlpbStatFRMRRspsTrnsmt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 9, 3, 1, 23),
    _UlpbStatFRMRRspsTrnsmt_Type()
)
ulpbStatFRMRRspsTrnsmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulpbStatFRMRRspsTrnsmt.setStatus("mandatory")
_UlpbStatIFrameCmdsRcvd_Type = Integer32
_UlpbStatIFrameCmdsRcvd_Object = MibTableColumn
ulpbStatIFrameCmdsRcvd = _UlpbStatIFrameCmdsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 9, 3, 1, 24),
    _UlpbStatIFrameCmdsRcvd_Type()
)
ulpbStatIFrameCmdsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulpbStatIFrameCmdsRcvd.setStatus("mandatory")
_UlpbStatIFrameCmdsTrnsmt_Type = Integer32
_UlpbStatIFrameCmdsTrnsmt_Object = MibTableColumn
ulpbStatIFrameCmdsTrnsmt = _UlpbStatIFrameCmdsTrnsmt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 9, 3, 1, 25),
    _UlpbStatIFrameCmdsTrnsmt_Type()
)
ulpbStatIFrameCmdsTrnsmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ulpbStatIFrameCmdsTrnsmt.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ULPB-MIB",
    **{"usr": usr,
       "nas": nas,
       "ulpb": ulpb,
       "ulpbAdmnTable": ulpbAdmnTable,
       "ulpbAdmnEntry": ulpbAdmnEntry,
       "ulpbAdmnIndex": ulpbAdmnIndex,
       "ulpbAdmnN2ReXmitVal": ulpbAdmnN2ReXmitVal,
       "ulpbAdmnT1AckTime": ulpbAdmnT1AckTime,
       "ulpbAdmnTpfVal": ulpbAdmnTpfVal,
       "ulpbAdmnTrejVal": ulpbAdmnTrejVal,
       "ulpbAdmnTbusyVal": ulpbAdmnTbusyVal,
       "ulpbAdmnLinkIdleTime": ulpbAdmnLinkIdleTime,
       "ulpbAdmnT2AckDelayTime": ulpbAdmnT2AckDelayTime,
       "ulpbAdmnRecKWindowSz": ulpbAdmnRecKWindowSz,
       "ulpbAdmnXmitKWindowSz": ulpbAdmnXmitKWindowSz,
       "ulpbAdmnLocProbe": ulpbAdmnLocProbe,
       "ulpbAdmnMaxRecFrmSz": ulpbAdmnMaxRecFrmSz,
       "ulpbAdmnIgnUaError": ulpbAdmnIgnUaError,
       "ulpbAdmnFrmrFrmrError": ulpbAdmnFrmrFrmrError,
       "ulpbAdmnFrmrInvrspError": ulpbAdmnFrmrInvrspError,
       "ulpbAdmnSframePbit": ulpbAdmnSframePbit,
       "ulpbAdmnDmOnAdm": ulpbAdmnDmOnAdm,
       "ulpbOperTable": ulpbOperTable,
       "ulpbOperEntry": ulpbOperEntry,
       "ulpbOperIndex": ulpbOperIndex,
       "ulpbOperN2ReXmitVal": ulpbOperN2ReXmitVal,
       "ulpbOperT1AckTime": ulpbOperT1AckTime,
       "ulpbOperTpfVal": ulpbOperTpfVal,
       "ulpbOperTrejVal": ulpbOperTrejVal,
       "ulpbOperTbusyVal": ulpbOperTbusyVal,
       "ulpbOperLinkIdleTime": ulpbOperLinkIdleTime,
       "ulpbOperT2AckDelayTime": ulpbOperT2AckDelayTime,
       "ulpbOperRecKWindowSz": ulpbOperRecKWindowSz,
       "ulpbOperXmitKWindowSz": ulpbOperXmitKWindowSz,
       "ulpbOperLocProbe": ulpbOperLocProbe,
       "ulpbOperMaxRecFrmSz": ulpbOperMaxRecFrmSz,
       "ulpbOperIgnUaError": ulpbOperIgnUaError,
       "ulpbOperFrmrFrmrError": ulpbOperFrmrFrmrError,
       "ulpbOperFrmrInvrspError": ulpbOperFrmrInvrspError,
       "ulpbOperSframePbit": ulpbOperSframePbit,
       "ulpbOperDmOnAdm": ulpbOperDmOnAdm,
       "ulpbStatTable": ulpbStatTable,
       "ulpbStatEntry": ulpbStatEntry,
       "ulpbStatIndex": ulpbStatIndex,
       "ulpbStatRRCmdsRcvd": ulpbStatRRCmdsRcvd,
       "ulpbStatRRCmdsTrnsmt": ulpbStatRRCmdsTrnsmt,
       "ulpbStatRRRspsRcvd": ulpbStatRRRspsRcvd,
       "ulpbStatRRRspsTrnsmt": ulpbStatRRRspsTrnsmt,
       "ulpbStatRNRCmdsRcvd": ulpbStatRNRCmdsRcvd,
       "ulpbStatRNRCmdsTrnsmt": ulpbStatRNRCmdsTrnsmt,
       "ulpbStatRNRRspsRcvd": ulpbStatRNRRspsRcvd,
       "ulpbStatRNRRspsTrnsmt": ulpbStatRNRRspsTrnsmt,
       "ulpbStatREJCmdsRcvd": ulpbStatREJCmdsRcvd,
       "ulpbStatREJCmdsTrnsmt": ulpbStatREJCmdsTrnsmt,
       "ulpbStatREJRspsRcvd": ulpbStatREJRspsRcvd,
       "ulpbStatREJRspsTrnsmt": ulpbStatREJRspsTrnsmt,
       "ulpbStatSABMCmdsRcvd": ulpbStatSABMCmdsRcvd,
       "ulpbStatSABMCmdsTrnsmt": ulpbStatSABMCmdsTrnsmt,
       "ulpbStatDISCCmdsRcvd": ulpbStatDISCCmdsRcvd,
       "ulpbStatDISCCmdsTrnsmt": ulpbStatDISCCmdsTrnsmt,
       "ulpbStatDMRspsRcvd": ulpbStatDMRspsRcvd,
       "ulpbStatDMRspsTrnsmt": ulpbStatDMRspsTrnsmt,
       "ulpbStatUARspsRcvd": ulpbStatUARspsRcvd,
       "ulpbStatUARspsTrnsmt": ulpbStatUARspsTrnsmt,
       "ulpbStatFRMRRspsRcvd": ulpbStatFRMRRspsRcvd,
       "ulpbStatFRMRRspsTrnsmt": ulpbStatFRMRRspsTrnsmt,
       "ulpbStatIFrameCmdsRcvd": ulpbStatIFrameCmdsRcvd,
       "ulpbStatIFrameCmdsTrnsmt": ulpbStatIFrameCmdsTrnsmt}
)
