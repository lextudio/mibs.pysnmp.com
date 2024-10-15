# SNMP MIB module (TERAWAVE-terads3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TERAWAVE-terads3-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:01:24 2024
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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Terawave_ObjectIdentity = ObjectIdentity
terawave = _Terawave_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513)
)
_TeraCDS3Group_ObjectIdentity = ObjectIdentity
teraCDS3Group = _TeraCDS3Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513, 8)
)
_TeraDSX3ConfigTable_Object = MibTable
teraDSX3ConfigTable = _TeraDSX3ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 1)
)
if mibBuilder.loadTexts:
    teraDSX3ConfigTable.setStatus("mandatory")
_TeraDSX3ConfigTableEntry_Object = MibTableRow
teraDSX3ConfigTableEntry = _TeraDSX3ConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 1, 1)
)
teraDSX3ConfigTableEntry.setIndexNames(
    (0, "TERAWAVE-terads3-MIB", "teraDs3LineIndex"),
)
if mibBuilder.loadTexts:
    teraDSX3ConfigTableEntry.setStatus("mandatory")
_TeraDs3LineIndex_Type = Integer32
_TeraDs3LineIndex_Object = MibTableColumn
teraDs3LineIndex = _TeraDs3LineIndex_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 1, 1, 1),
    _TeraDs3LineIndex_Type()
)
teraDs3LineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDs3LineIndex.setStatus("mandatory")


class _TeraDs3OOFCriteria_Type(Integer32):
    """Custom type teraDs3OOFCriteria based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bits3Of16", 2),
          ("bits3Of8", 1))
    )


_TeraDs3OOFCriteria_Type.__name__ = "Integer32"
_TeraDs3OOFCriteria_Object = MibTableColumn
teraDs3OOFCriteria = _TeraDs3OOFCriteria_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 1, 1, 2),
    _TeraDs3OOFCriteria_Type()
)
teraDs3OOFCriteria.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraDs3OOFCriteria.setStatus("mandatory")


class _TeraDs3AISBitsChkSchm_Type(Integer32):
    """Custom type teraDs3AISBitsChkSchm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("checkCbits", 1),
          ("ignoreBits", 2))
    )


_TeraDs3AISBitsChkSchm_Type.__name__ = "Integer32"
_TeraDs3AISBitsChkSchm_Object = MibTableColumn
teraDs3AISBitsChkSchm = _TeraDs3AISBitsChkSchm_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 1, 1, 3),
    _TeraDs3AISBitsChkSchm_Type()
)
teraDs3AISBitsChkSchm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraDs3AISBitsChkSchm.setStatus("mandatory")


class _TeraDs3RcvFEACCriteria_Type(Integer32):
    """Custom type teraDs3RcvFEACCriteria based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fEACCodes4Of5", 1),
          ("fEACCodes8Of16", 2))
    )


_TeraDs3RcvFEACCriteria_Type.__name__ = "Integer32"
_TeraDs3RcvFEACCriteria_Object = MibTableColumn
teraDs3RcvFEACCriteria = _TeraDs3RcvFEACCriteria_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 1, 1, 4),
    _TeraDs3RcvFEACCriteria_Type()
)
teraDs3RcvFEACCriteria.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraDs3RcvFEACCriteria.setStatus("mandatory")


class _TeraDs3FEACLoopCheck_Type(Integer32):
    """Custom type teraDs3FEACLoopCheck based on Integer32"""
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


_TeraDs3FEACLoopCheck_Type.__name__ = "Integer32"
_TeraDs3FEACLoopCheck_Object = MibTableColumn
teraDs3FEACLoopCheck = _TeraDs3FEACLoopCheck_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 1, 1, 5),
    _TeraDs3FEACLoopCheck_Type()
)
teraDs3FEACLoopCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraDs3FEACLoopCheck.setStatus("mandatory")


class _TeraDs3DS1FarEndLoopStatus_Type(Integer32):
    """Custom type teraDs3DS1FarEndLoopStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29)
        )
    )
    namedValues = NamedValues(
        *(("all-DS1", 29),
          ("dS1-1", 1),
          ("dS1-10", 10),
          ("dS1-11", 11),
          ("dS1-12", 12),
          ("dS1-13", 13),
          ("dS1-14", 14),
          ("dS1-15", 15),
          ("dS1-16", 16),
          ("dS1-17", 17),
          ("dS1-18", 18),
          ("dS1-19", 19),
          ("dS1-2", 2),
          ("dS1-20", 20),
          ("dS1-21", 21),
          ("dS1-22", 22),
          ("dS1-23", 23),
          ("dS1-24", 24),
          ("dS1-25", 25),
          ("dS1-26", 26),
          ("dS1-27", 27),
          ("dS1-28", 28),
          ("dS1-3", 3),
          ("dS1-4", 4),
          ("dS1-5", 5),
          ("dS1-6", 6),
          ("dS1-7", 7),
          ("dS1-8", 8),
          ("dS1-9", 9),
          ("none", 0))
    )


_TeraDs3DS1FarEndLoopStatus_Type.__name__ = "Integer32"
_TeraDs3DS1FarEndLoopStatus_Object = MibTableColumn
teraDs3DS1FarEndLoopStatus = _TeraDs3DS1FarEndLoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 1, 1, 6),
    _TeraDs3DS1FarEndLoopStatus_Type()
)
teraDs3DS1FarEndLoopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDs3DS1FarEndLoopStatus.setStatus("mandatory")


class _TeraDs3DS1NearEndLoopStatus_Type(Integer32):
    """Custom type teraDs3DS1NearEndLoopStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29)
        )
    )
    namedValues = NamedValues(
        *(("all-DS1", 29),
          ("dS1-1", 1),
          ("dS1-10", 10),
          ("dS1-11", 11),
          ("dS1-12", 12),
          ("dS1-13", 13),
          ("dS1-14", 14),
          ("dS1-15", 15),
          ("dS1-16", 16),
          ("dS1-17", 17),
          ("dS1-18", 18),
          ("dS1-19", 19),
          ("dS1-2", 2),
          ("dS1-20", 20),
          ("dS1-21", 21),
          ("dS1-22", 22),
          ("dS1-23", 23),
          ("dS1-24", 24),
          ("dS1-25", 25),
          ("dS1-26", 26),
          ("dS1-27", 27),
          ("dS1-28", 28),
          ("dS1-3", 3),
          ("dS1-4", 4),
          ("dS1-5", 5),
          ("dS1-6", 6),
          ("dS1-7", 7),
          ("dS1-8", 8),
          ("dS1-9", 9),
          ("none", 0))
    )


_TeraDs3DS1NearEndLoopStatus_Type.__name__ = "Integer32"
_TeraDs3DS1NearEndLoopStatus_Object = MibTableColumn
teraDs3DS1NearEndLoopStatus = _TeraDs3DS1NearEndLoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 1, 1, 7),
    _TeraDs3DS1NearEndLoopStatus_Type()
)
teraDs3DS1NearEndLoopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDs3DS1NearEndLoopStatus.setStatus("mandatory")


class _TeraDs37DayTotalTimeElapsed_Type(Integer32):
    """Custom type teraDs37DayTotalTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_TeraDs37DayTotalTimeElapsed_Type.__name__ = "Integer32"
_TeraDs37DayTotalTimeElapsed_Object = MibTableColumn
teraDs37DayTotalTimeElapsed = _TeraDs37DayTotalTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 1, 1, 8),
    _TeraDs37DayTotalTimeElapsed_Type()
)
teraDs37DayTotalTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDs37DayTotalTimeElapsed.setStatus("mandatory")


class _TeraDs3ExtendValidTotalIntervals_Type(Integer32):
    """Custom type teraDs3ExtendValidTotalIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TeraDs3ExtendValidTotalIntervals_Type.__name__ = "Integer32"
_TeraDs3ExtendValidTotalIntervals_Object = MibTableColumn
teraDs3ExtendValidTotalIntervals = _TeraDs3ExtendValidTotalIntervals_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 1, 1, 9),
    _TeraDs3ExtendValidTotalIntervals_Type()
)
teraDs3ExtendValidTotalIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDs3ExtendValidTotalIntervals.setStatus("mandatory")


class _TeraDs3ExtendInvalidTotalIntervals_Type(Integer32):
    """Custom type teraDs3ExtendInvalidTotalIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TeraDs3ExtendInvalidTotalIntervals_Type.__name__ = "Integer32"
_TeraDs3ExtendInvalidTotalIntervals_Object = MibTableColumn
teraDs3ExtendInvalidTotalIntervals = _TeraDs3ExtendInvalidTotalIntervals_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 1, 1, 10),
    _TeraDs3ExtendInvalidTotalIntervals_Type()
)
teraDs3ExtendInvalidTotalIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDs3ExtendInvalidTotalIntervals.setStatus("mandatory")
_TeraDSX37DayTotalTable_Object = MibTable
teraDSX37DayTotalTable = _TeraDSX37DayTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 2)
)
if mibBuilder.loadTexts:
    teraDSX37DayTotalTable.setStatus("mandatory")
_TeraDSX37DayTotalTableEntry_Object = MibTableRow
teraDSX37DayTotalTableEntry = _TeraDSX37DayTotalTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 2, 1)
)
teraDSX37DayTotalTableEntry.setIndexNames(
    (0, "TERAWAVE-terads3-MIB", "teraDS37DayTotalIndex"),
    (0, "TERAWAVE-terads3-MIB", "teraDS37DayTotalNumber"),
)
if mibBuilder.loadTexts:
    teraDSX37DayTotalTableEntry.setStatus("mandatory")
_TeraDS37DayTotalIndex_Type = Integer32
_TeraDS37DayTotalIndex_Object = MibTableColumn
teraDS37DayTotalIndex = _TeraDS37DayTotalIndex_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 2, 1, 1),
    _TeraDS37DayTotalIndex_Type()
)
teraDS37DayTotalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDS37DayTotalIndex.setStatus("mandatory")


class _TeraDS37DayTotalNumber_Type(Integer32):
    """Custom type teraDS37DayTotalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_TeraDS37DayTotalNumber_Type.__name__ = "Integer32"
_TeraDS37DayTotalNumber_Object = MibTableColumn
teraDS37DayTotalNumber = _TeraDS37DayTotalNumber_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 2, 1, 2),
    _TeraDS37DayTotalNumber_Type()
)
teraDS37DayTotalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDS37DayTotalNumber.setStatus("mandatory")
_TeraDS37DayTotalPESs_Type = Gauge32
_TeraDS37DayTotalPESs_Object = MibTableColumn
teraDS37DayTotalPESs = _TeraDS37DayTotalPESs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 2, 1, 3),
    _TeraDS37DayTotalPESs_Type()
)
teraDS37DayTotalPESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDS37DayTotalPESs.setStatus("mandatory")
_TeraDS37DayTotalPSESs_Type = Gauge32
_TeraDS37DayTotalPSESs_Object = MibTableColumn
teraDS37DayTotalPSESs = _TeraDS37DayTotalPSESs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 2, 1, 4),
    _TeraDS37DayTotalPSESs_Type()
)
teraDS37DayTotalPSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDS37DayTotalPSESs.setStatus("mandatory")
_TeraDS37DayTotalSEFSs_Type = Gauge32
_TeraDS37DayTotalSEFSs_Object = MibTableColumn
teraDS37DayTotalSEFSs = _TeraDS37DayTotalSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 2, 1, 5),
    _TeraDS37DayTotalSEFSs_Type()
)
teraDS37DayTotalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDS37DayTotalSEFSs.setStatus("mandatory")
_TeraDS37DayTotalUASs_Type = Gauge32
_TeraDS37DayTotalUASs_Object = MibTableColumn
teraDS37DayTotalUASs = _TeraDS37DayTotalUASs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 2, 1, 6),
    _TeraDS37DayTotalUASs_Type()
)
teraDS37DayTotalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDS37DayTotalUASs.setStatus("mandatory")
_TeraDS37DayTotalLCVs_Type = Gauge32
_TeraDS37DayTotalLCVs_Object = MibTableColumn
teraDS37DayTotalLCVs = _TeraDS37DayTotalLCVs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 2, 1, 7),
    _TeraDS37DayTotalLCVs_Type()
)
teraDS37DayTotalLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDS37DayTotalLCVs.setStatus("mandatory")
_TeraDS37DayTotalPCVs_Type = Gauge32
_TeraDS37DayTotalPCVs_Object = MibTableColumn
teraDS37DayTotalPCVs = _TeraDS37DayTotalPCVs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 2, 1, 8),
    _TeraDS37DayTotalPCVs_Type()
)
teraDS37DayTotalPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDS37DayTotalPCVs.setStatus("mandatory")
_TeraDS37DayTotalLESs_Type = Gauge32
_TeraDS37DayTotalLESs_Object = MibTableColumn
teraDS37DayTotalLESs = _TeraDS37DayTotalLESs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 2, 1, 9),
    _TeraDS37DayTotalLESs_Type()
)
teraDS37DayTotalLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDS37DayTotalLESs.setStatus("mandatory")
_TeraDS37DayTotalCCVs_Type = Gauge32
_TeraDS37DayTotalCCVs_Object = MibTableColumn
teraDS37DayTotalCCVs = _TeraDS37DayTotalCCVs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 2, 1, 10),
    _TeraDS37DayTotalCCVs_Type()
)
teraDS37DayTotalCCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDS37DayTotalCCVs.setStatus("mandatory")
_TeraDS37DayTotalCESs_Type = Gauge32
_TeraDS37DayTotalCESs_Object = MibTableColumn
teraDS37DayTotalCESs = _TeraDS37DayTotalCESs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 2, 1, 11),
    _TeraDS37DayTotalCESs_Type()
)
teraDS37DayTotalCESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDS37DayTotalCESs.setStatus("mandatory")
_TeraDS37DayTotalCSESs_Type = Gauge32
_TeraDS37DayTotalCSESs_Object = MibTableColumn
teraDS37DayTotalCSESs = _TeraDS37DayTotalCSESs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 2, 1, 12),
    _TeraDS37DayTotalCSESs_Type()
)
teraDS37DayTotalCSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDS37DayTotalCSESs.setStatus("mandatory")
_TeraDS37DayTotalValidData_Type = Integer32
_TeraDS37DayTotalValidData_Object = MibTableColumn
teraDS37DayTotalValidData = _TeraDS37DayTotalValidData_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 2, 1, 13),
    _TeraDS37DayTotalValidData_Type()
)
teraDS37DayTotalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDS37DayTotalValidData.setStatus("mandatory")
_TeraDSX3FarEnd7DayTotalTable_Object = MibTable
teraDSX3FarEnd7DayTotalTable = _TeraDSX3FarEnd7DayTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 3)
)
if mibBuilder.loadTexts:
    teraDSX3FarEnd7DayTotalTable.setStatus("mandatory")
_TeraDSX3FarEnd7DayTotalTableEntry_Object = MibTableRow
teraDSX3FarEnd7DayTotalTableEntry = _TeraDSX3FarEnd7DayTotalTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 3, 1)
)
teraDSX3FarEnd7DayTotalTableEntry.setIndexNames(
    (0, "TERAWAVE-terads3-MIB", "teraDSX3FarEnd7DayTotalIndex"),
    (0, "TERAWAVE-terads3-MIB", "teraDS3FarEnd7DayTotalNumber"),
)
if mibBuilder.loadTexts:
    teraDSX3FarEnd7DayTotalTableEntry.setStatus("mandatory")
_TeraDSX3FarEnd7DayTotalIndex_Type = Integer32
_TeraDSX3FarEnd7DayTotalIndex_Object = MibTableColumn
teraDSX3FarEnd7DayTotalIndex = _TeraDSX3FarEnd7DayTotalIndex_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 3, 1, 1),
    _TeraDSX3FarEnd7DayTotalIndex_Type()
)
teraDSX3FarEnd7DayTotalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDSX3FarEnd7DayTotalIndex.setStatus("mandatory")


class _TeraDS3FarEnd7DayTotalNumber_Type(Integer32):
    """Custom type teraDS3FarEnd7DayTotalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_TeraDS3FarEnd7DayTotalNumber_Type.__name__ = "Integer32"
_TeraDS3FarEnd7DayTotalNumber_Object = MibTableColumn
teraDS3FarEnd7DayTotalNumber = _TeraDS3FarEnd7DayTotalNumber_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 3, 1, 2),
    _TeraDS3FarEnd7DayTotalNumber_Type()
)
teraDS3FarEnd7DayTotalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDS3FarEnd7DayTotalNumber.setStatus("mandatory")
_TeraDS3FarEnd7DayTotalCESs_Type = Gauge32
_TeraDS3FarEnd7DayTotalCESs_Object = MibTableColumn
teraDS3FarEnd7DayTotalCESs = _TeraDS3FarEnd7DayTotalCESs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 3, 1, 3),
    _TeraDS3FarEnd7DayTotalCESs_Type()
)
teraDS3FarEnd7DayTotalCESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDS3FarEnd7DayTotalCESs.setStatus("mandatory")
_TeraDS3FarEnd7DayTotalCSESs_Type = Gauge32
_TeraDS3FarEnd7DayTotalCSESs_Object = MibTableColumn
teraDS3FarEnd7DayTotalCSESs = _TeraDS3FarEnd7DayTotalCSESs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 3, 1, 4),
    _TeraDS3FarEnd7DayTotalCSESs_Type()
)
teraDS3FarEnd7DayTotalCSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDS3FarEnd7DayTotalCSESs.setStatus("mandatory")
_TeraDS3FarEnd7DayTotalCCVs_Type = Gauge32
_TeraDS3FarEnd7DayTotalCCVs_Object = MibTableColumn
teraDS3FarEnd7DayTotalCCVs = _TeraDS3FarEnd7DayTotalCCVs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 3, 1, 5),
    _TeraDS3FarEnd7DayTotalCCVs_Type()
)
teraDS3FarEnd7DayTotalCCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDS3FarEnd7DayTotalCCVs.setStatus("mandatory")
_TeraDS3FarEnd7DayTotalUASs_Type = Gauge32
_TeraDS3FarEnd7DayTotalUASs_Object = MibTableColumn
teraDS3FarEnd7DayTotalUASs = _TeraDS3FarEnd7DayTotalUASs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 3, 1, 6),
    _TeraDS3FarEnd7DayTotalUASs_Type()
)
teraDS3FarEnd7DayTotalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDS3FarEnd7DayTotalUASs.setStatus("mandatory")
_TeraDS3FarEnd7DayTotalValidData_Type = Integer32
_TeraDS3FarEnd7DayTotalValidData_Object = MibTableColumn
teraDS3FarEnd7DayTotalValidData = _TeraDS3FarEnd7DayTotalValidData_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 3, 1, 7),
    _TeraDS3FarEnd7DayTotalValidData_Type()
)
teraDS3FarEnd7DayTotalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDS3FarEnd7DayTotalValidData.setStatus("mandatory")
_Teradsx3CurrentTable_Object = MibTable
teradsx3CurrentTable = _Teradsx3CurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 4)
)
if mibBuilder.loadTexts:
    teradsx3CurrentTable.setStatus("mandatory")
_Teradsx3CurrentTableEntry_Object = MibTableRow
teradsx3CurrentTableEntry = _Teradsx3CurrentTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 4, 1)
)
teradsx3CurrentTableEntry.setIndexNames(
    (0, "TERAWAVE-terads3-MIB", "teradsx3CurrentIndex"),
)
if mibBuilder.loadTexts:
    teradsx3CurrentTableEntry.setStatus("mandatory")
_Teradsx3CurrentIndex_Type = Integer32
_Teradsx3CurrentIndex_Object = MibTableColumn
teradsx3CurrentIndex = _Teradsx3CurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 4, 1, 1),
    _Teradsx3CurrentIndex_Type()
)
teradsx3CurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx3CurrentIndex.setStatus("mandatory")
_Teradsx3ESB_L_Type = Integer32
_Teradsx3ESB_L_Object = MibScalar
teradsx3ESB_L = _Teradsx3ESB_L_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 4, 1, 2),
    _Teradsx3ESB_L_Type()
)
teradsx3ESB_L.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx3ESB_L.setStatus("mandatory")
_Teradsx3LOSS_L_Type = Gauge32
_Teradsx3LOSS_L_Object = MibScalar
teradsx3LOSS_L = _Teradsx3LOSS_L_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 4, 1, 3),
    _Teradsx3LOSS_L_Type()
)
teradsx3LOSS_L.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx3LOSS_L.setStatus("mandatory")
_Teradsx3ESB_P_Type = Gauge32
_Teradsx3ESB_P_Object = MibScalar
teradsx3ESB_P = _Teradsx3ESB_P_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 4, 1, 4),
    _Teradsx3ESB_P_Type()
)
teradsx3ESB_P.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx3ESB_P.setStatus("mandatory")
_Teradsx3SAS_P_Type = Gauge32
_Teradsx3SAS_P_Object = MibScalar
teradsx3SAS_P = _Teradsx3SAS_P_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 4, 1, 5),
    _Teradsx3SAS_P_Type()
)
teradsx3SAS_P.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx3SAS_P.setStatus("mandatory")
_Teradsx3AISS_P_Type = Gauge32
_Teradsx3AISS_P_Object = MibScalar
teradsx3AISS_P = _Teradsx3AISS_P_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 4, 1, 6),
    _Teradsx3AISS_P_Type()
)
teradsx3AISS_P.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx3AISS_P.setStatus("mandatory")
_Teradsx3UASP_P_Type = Gauge32
_Teradsx3UASP_P_Object = MibScalar
teradsx3UASP_P = _Teradsx3UASP_P_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 4, 1, 7),
    _Teradsx3UASP_P_Type()
)
teradsx3UASP_P.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx3UASP_P.setStatus("mandatory")
_Teradsx3ESCP_PFE_Type = Gauge32
_Teradsx3ESCP_PFE_Object = MibScalar
teradsx3ESCP_PFE = _Teradsx3ESCP_PFE_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 4, 1, 8),
    _Teradsx3ESCP_PFE_Type()
)
teradsx3ESCP_PFE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx3ESCP_PFE.setStatus("mandatory")
_Teradsx3ESBCP_PFE_Type = Gauge32
_Teradsx3ESBCP_PFE_Object = MibScalar
teradsx3ESBCP_PFE = _Teradsx3ESBCP_PFE_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 4, 1, 9),
    _Teradsx3ESBCP_PFE_Type()
)
teradsx3ESBCP_PFE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx3ESBCP_PFE.setStatus("mandatory")
_Teradsx3SASCP_PFE_Type = Gauge32
_Teradsx3SASCP_PFE_Object = MibScalar
teradsx3SASCP_PFE = _Teradsx3SASCP_PFE_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 4, 1, 10),
    _Teradsx3SASCP_PFE_Type()
)
teradsx3SASCP_PFE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teradsx3SASCP_PFE.setStatus("mandatory")
_Teradsx3IntervalTable_Object = MibTable
teradsx3IntervalTable = _Teradsx3IntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 5)
)
if mibBuilder.loadTexts:
    teradsx3IntervalTable.setStatus("mandatory")
_Teradsx3IntervalTableEntry_Object = MibTableRow
teradsx3IntervalTableEntry = _Teradsx3IntervalTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 5, 1)
)
teradsx3IntervalTableEntry.setIndexNames(
    (0, "TERAWAVE-terads3-MIB", "terads3IntervalIndex"),
    (0, "TERAWAVE-terads3-MIB", "terads3IntervalNumber"),
)
if mibBuilder.loadTexts:
    teradsx3IntervalTableEntry.setStatus("mandatory")
_Terads3IntervalIndex_Type = Integer32
_Terads3IntervalIndex_Object = MibTableColumn
terads3IntervalIndex = _Terads3IntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 5, 1, 1),
    _Terads3IntervalIndex_Type()
)
terads3IntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    terads3IntervalIndex.setStatus("mandatory")


class _Terads3IntervalNumber_Type(Integer32):
    """Custom type terads3IntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_Terads3IntervalNumber_Type.__name__ = "Integer32"
_Terads3IntervalNumber_Object = MibTableColumn
terads3IntervalNumber = _Terads3IntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 5, 1, 2),
    _Terads3IntervalNumber_Type()
)
terads3IntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    terads3IntervalNumber.setStatus("mandatory")
_Terads3Intervalteradsx3ESB_L_Type = Gauge32
_Terads3Intervalteradsx3ESB_L_Object = MibScalar
terads3Intervalteradsx3ESB_L = _Terads3Intervalteradsx3ESB_L_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 5, 1, 3),
    _Terads3Intervalteradsx3ESB_L_Type()
)
terads3Intervalteradsx3ESB_L.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    terads3Intervalteradsx3ESB_L.setStatus("mandatory")
_Terads3Intervalteradsx3LOSS_L_Type = Gauge32
_Terads3Intervalteradsx3LOSS_L_Object = MibScalar
terads3Intervalteradsx3LOSS_L = _Terads3Intervalteradsx3LOSS_L_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 5, 1, 4),
    _Terads3Intervalteradsx3LOSS_L_Type()
)
terads3Intervalteradsx3LOSS_L.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    terads3Intervalteradsx3LOSS_L.setStatus("mandatory")
_Terads3Intervalteradsx3ESB_P_Type = Gauge32
_Terads3Intervalteradsx3ESB_P_Object = MibScalar
terads3Intervalteradsx3ESB_P = _Terads3Intervalteradsx3ESB_P_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 5, 1, 5),
    _Terads3Intervalteradsx3ESB_P_Type()
)
terads3Intervalteradsx3ESB_P.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    terads3Intervalteradsx3ESB_P.setStatus("mandatory")
_Terads3Intervalteradsx3SAS_P_Type = Gauge32
_Terads3Intervalteradsx3SAS_P_Object = MibScalar
terads3Intervalteradsx3SAS_P = _Terads3Intervalteradsx3SAS_P_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 5, 1, 6),
    _Terads3Intervalteradsx3SAS_P_Type()
)
terads3Intervalteradsx3SAS_P.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    terads3Intervalteradsx3SAS_P.setStatus("mandatory")
_Terads3Intervalteradsx3AISS_P_Type = Gauge32
_Terads3Intervalteradsx3AISS_P_Object = MibScalar
terads3Intervalteradsx3AISS_P = _Terads3Intervalteradsx3AISS_P_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 5, 1, 7),
    _Terads3Intervalteradsx3AISS_P_Type()
)
terads3Intervalteradsx3AISS_P.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    terads3Intervalteradsx3AISS_P.setStatus("mandatory")
_Terads3Intervalteradsx3UASP_P_Type = Gauge32
_Terads3Intervalteradsx3UASP_P_Object = MibScalar
terads3Intervalteradsx3UASP_P = _Terads3Intervalteradsx3UASP_P_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 5, 1, 8),
    _Terads3Intervalteradsx3UASP_P_Type()
)
terads3Intervalteradsx3UASP_P.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    terads3Intervalteradsx3UASP_P.setStatus("mandatory")
_Terads3Intervalteradsx3ESCP_PFE_Type = Gauge32
_Terads3Intervalteradsx3ESCP_PFE_Object = MibScalar
terads3Intervalteradsx3ESCP_PFE = _Terads3Intervalteradsx3ESCP_PFE_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 5, 1, 9),
    _Terads3Intervalteradsx3ESCP_PFE_Type()
)
terads3Intervalteradsx3ESCP_PFE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    terads3Intervalteradsx3ESCP_PFE.setStatus("mandatory")
_Terads3Intervalteradsx3ESBCP_PFE_Type = Gauge32
_Terads3Intervalteradsx3ESBCP_PFE_Object = MibScalar
terads3Intervalteradsx3ESBCP_PFE = _Terads3Intervalteradsx3ESBCP_PFE_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 5, 1, 10),
    _Terads3Intervalteradsx3ESBCP_PFE_Type()
)
terads3Intervalteradsx3ESBCP_PFE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    terads3Intervalteradsx3ESBCP_PFE.setStatus("mandatory")
_Terads3Intervalteradsx3SASCP_PFE_Type = Gauge32
_Terads3Intervalteradsx3SASCP_PFE_Object = MibScalar
terads3Intervalteradsx3SASCP_PFE = _Terads3Intervalteradsx3SASCP_PFE_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 5, 1, 11),
    _Terads3Intervalteradsx3SASCP_PFE_Type()
)
terads3Intervalteradsx3SASCP_PFE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    terads3Intervalteradsx3SASCP_PFE.setStatus("mandatory")
_Terads3IntervalValidData_Type = Integer32
_Terads3IntervalValidData_Object = MibTableColumn
terads3IntervalValidData = _Terads3IntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 5, 1, 12),
    _Terads3IntervalValidData_Type()
)
terads3IntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    terads3IntervalValidData.setStatus("mandatory")
_Teradsx3TotalTable_Object = MibTable
teradsx3TotalTable = _Teradsx3TotalTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 6)
)
if mibBuilder.loadTexts:
    teradsx3TotalTable.setStatus("mandatory")
_Teradsx3TotalTableEntry_Object = MibTableRow
teradsx3TotalTableEntry = _Teradsx3TotalTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 6, 1)
)
teradsx3TotalTableEntry.setIndexNames(
    (0, "TERAWAVE-terads3-MIB", "terads3TotalIndex"),
)
if mibBuilder.loadTexts:
    teradsx3TotalTableEntry.setStatus("mandatory")
_Terads3TotalIndex_Type = Integer32
_Terads3TotalIndex_Object = MibTableColumn
terads3TotalIndex = _Terads3TotalIndex_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 6, 1, 1),
    _Terads3TotalIndex_Type()
)
terads3TotalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    terads3TotalIndex.setStatus("mandatory")
_Terads3Totalteradsx3ESB_L_Type = Gauge32
_Terads3Totalteradsx3ESB_L_Object = MibScalar
terads3Totalteradsx3ESB_L = _Terads3Totalteradsx3ESB_L_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 6, 1, 2),
    _Terads3Totalteradsx3ESB_L_Type()
)
terads3Totalteradsx3ESB_L.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    terads3Totalteradsx3ESB_L.setStatus("mandatory")
_Terads3Totalteradsx3LOSS_L_Type = Gauge32
_Terads3Totalteradsx3LOSS_L_Object = MibScalar
terads3Totalteradsx3LOSS_L = _Terads3Totalteradsx3LOSS_L_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 6, 1, 3),
    _Terads3Totalteradsx3LOSS_L_Type()
)
terads3Totalteradsx3LOSS_L.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    terads3Totalteradsx3LOSS_L.setStatus("mandatory")
_Terads3Totalteradsx3ESB_P_Type = Gauge32
_Terads3Totalteradsx3ESB_P_Object = MibScalar
terads3Totalteradsx3ESB_P = _Terads3Totalteradsx3ESB_P_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 6, 1, 4),
    _Terads3Totalteradsx3ESB_P_Type()
)
terads3Totalteradsx3ESB_P.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    terads3Totalteradsx3ESB_P.setStatus("mandatory")
_Terads3Totalteradsx3SAS_P_Type = Gauge32
_Terads3Totalteradsx3SAS_P_Object = MibScalar
terads3Totalteradsx3SAS_P = _Terads3Totalteradsx3SAS_P_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 6, 1, 5),
    _Terads3Totalteradsx3SAS_P_Type()
)
terads3Totalteradsx3SAS_P.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    terads3Totalteradsx3SAS_P.setStatus("mandatory")
_Terads3Totalteradsx3AISS_P_Type = Gauge32
_Terads3Totalteradsx3AISS_P_Object = MibScalar
terads3Totalteradsx3AISS_P = _Terads3Totalteradsx3AISS_P_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 6, 1, 6),
    _Terads3Totalteradsx3AISS_P_Type()
)
terads3Totalteradsx3AISS_P.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    terads3Totalteradsx3AISS_P.setStatus("mandatory")
_Terads3Totalteradsx3UASP_P_Type = Gauge32
_Terads3Totalteradsx3UASP_P_Object = MibScalar
terads3Totalteradsx3UASP_P = _Terads3Totalteradsx3UASP_P_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 6, 1, 7),
    _Terads3Totalteradsx3UASP_P_Type()
)
terads3Totalteradsx3UASP_P.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    terads3Totalteradsx3UASP_P.setStatus("mandatory")
_Terads3Totalteradsx3ESCP_PFE_Type = Gauge32
_Terads3Totalteradsx3ESCP_PFE_Object = MibScalar
terads3Totalteradsx3ESCP_PFE = _Terads3Totalteradsx3ESCP_PFE_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 6, 1, 8),
    _Terads3Totalteradsx3ESCP_PFE_Type()
)
terads3Totalteradsx3ESCP_PFE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    terads3Totalteradsx3ESCP_PFE.setStatus("mandatory")
_Terads3Totalteradsx3ESBCP_PFE_Type = Gauge32
_Terads3Totalteradsx3ESBCP_PFE_Object = MibScalar
terads3Totalteradsx3ESBCP_PFE = _Terads3Totalteradsx3ESBCP_PFE_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 6, 1, 9),
    _Terads3Totalteradsx3ESBCP_PFE_Type()
)
terads3Totalteradsx3ESBCP_PFE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    terads3Totalteradsx3ESBCP_PFE.setStatus("mandatory")
_Terads3Totalteradsx3SASCP_PFE_Type = Gauge32
_Terads3Totalteradsx3SASCP_PFE_Object = MibScalar
terads3Totalteradsx3SASCP_PFE = _Terads3Totalteradsx3SASCP_PFE_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 6, 1, 10),
    _Terads3Totalteradsx3SASCP_PFE_Type()
)
terads3Totalteradsx3SASCP_PFE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    terads3Totalteradsx3SASCP_PFE.setStatus("mandatory")


class _Terads3TotalPerfStat_Type(Integer32):
    """Custom type terads3TotalPerfStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("ok", 1))
    )


_Terads3TotalPerfStat_Type.__name__ = "Integer32"
_Terads3TotalPerfStat_Object = MibTableColumn
terads3TotalPerfStat = _Terads3TotalPerfStat_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 6, 1, 11),
    _Terads3TotalPerfStat_Type()
)
terads3TotalPerfStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    terads3TotalPerfStat.setStatus("mandatory")
_TeraDSX3tera7DayTotalTable_Object = MibTable
teraDSX3tera7DayTotalTable = _TeraDSX3tera7DayTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 7)
)
if mibBuilder.loadTexts:
    teraDSX3tera7DayTotalTable.setStatus("mandatory")
_TeraDSX3tera7DayTotalTableEntry_Object = MibTableRow
teraDSX3tera7DayTotalTableEntry = _TeraDSX3tera7DayTotalTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 7, 1)
)
teraDSX3tera7DayTotalTableEntry.setIndexNames(
    (0, "TERAWAVE-terads3-MIB", "teraDSX3tera7DayTotalIndex"),
    (0, "TERAWAVE-terads3-MIB", "teraDS3tera7DayTotalNumber"),
)
if mibBuilder.loadTexts:
    teraDSX3tera7DayTotalTableEntry.setStatus("mandatory")
_TeraDSX3tera7DayTotalIndex_Type = Integer32
_TeraDSX3tera7DayTotalIndex_Object = MibTableColumn
teraDSX3tera7DayTotalIndex = _TeraDSX3tera7DayTotalIndex_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 7, 1, 1),
    _TeraDSX3tera7DayTotalIndex_Type()
)
teraDSX3tera7DayTotalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDSX3tera7DayTotalIndex.setStatus("mandatory")


class _TeraDS3tera7DayTotalNumber_Type(Integer32):
    """Custom type teraDS3tera7DayTotalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_TeraDS3tera7DayTotalNumber_Type.__name__ = "Integer32"
_TeraDS3tera7DayTotalNumber_Object = MibTableColumn
teraDS3tera7DayTotalNumber = _TeraDS3tera7DayTotalNumber_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 7, 1, 2),
    _TeraDS3tera7DayTotalNumber_Type()
)
teraDS3tera7DayTotalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDS3tera7DayTotalNumber.setStatus("mandatory")
_TeraDS3tera7DayTotalteradsx3ESB_L_Type = Gauge32
_TeraDS3tera7DayTotalteradsx3ESB_L_Object = MibScalar
teraDS3tera7DayTotalteradsx3ESB_L = _TeraDS3tera7DayTotalteradsx3ESB_L_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 7, 1, 3),
    _TeraDS3tera7DayTotalteradsx3ESB_L_Type()
)
teraDS3tera7DayTotalteradsx3ESB_L.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDS3tera7DayTotalteradsx3ESB_L.setStatus("mandatory")
_TeraDS3tera7DayTotalteradsx3LOSS_L_Type = Gauge32
_TeraDS3tera7DayTotalteradsx3LOSS_L_Object = MibScalar
teraDS3tera7DayTotalteradsx3LOSS_L = _TeraDS3tera7DayTotalteradsx3LOSS_L_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 7, 1, 4),
    _TeraDS3tera7DayTotalteradsx3LOSS_L_Type()
)
teraDS3tera7DayTotalteradsx3LOSS_L.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDS3tera7DayTotalteradsx3LOSS_L.setStatus("mandatory")
_TeraDS3tera7DayTotalteradsx3ESB_P_Type = Gauge32
_TeraDS3tera7DayTotalteradsx3ESB_P_Object = MibScalar
teraDS3tera7DayTotalteradsx3ESB_P = _TeraDS3tera7DayTotalteradsx3ESB_P_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 7, 1, 5),
    _TeraDS3tera7DayTotalteradsx3ESB_P_Type()
)
teraDS3tera7DayTotalteradsx3ESB_P.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDS3tera7DayTotalteradsx3ESB_P.setStatus("mandatory")
_TeraDS3tera7DayTotalteradsx3SAS_P_Type = Gauge32
_TeraDS3tera7DayTotalteradsx3SAS_P_Object = MibScalar
teraDS3tera7DayTotalteradsx3SAS_P = _TeraDS3tera7DayTotalteradsx3SAS_P_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 7, 1, 6),
    _TeraDS3tera7DayTotalteradsx3SAS_P_Type()
)
teraDS3tera7DayTotalteradsx3SAS_P.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDS3tera7DayTotalteradsx3SAS_P.setStatus("mandatory")
_TeraDS3tera7DayTotalteradsx3AISS_P_Type = Gauge32
_TeraDS3tera7DayTotalteradsx3AISS_P_Object = MibScalar
teraDS3tera7DayTotalteradsx3AISS_P = _TeraDS3tera7DayTotalteradsx3AISS_P_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 7, 1, 7),
    _TeraDS3tera7DayTotalteradsx3AISS_P_Type()
)
teraDS3tera7DayTotalteradsx3AISS_P.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDS3tera7DayTotalteradsx3AISS_P.setStatus("mandatory")
_TeraDS3tera7DayTotalteradsx3UASP_P_Type = Gauge32
_TeraDS3tera7DayTotalteradsx3UASP_P_Object = MibScalar
teraDS3tera7DayTotalteradsx3UASP_P = _TeraDS3tera7DayTotalteradsx3UASP_P_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 7, 1, 8),
    _TeraDS3tera7DayTotalteradsx3UASP_P_Type()
)
teraDS3tera7DayTotalteradsx3UASP_P.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDS3tera7DayTotalteradsx3UASP_P.setStatus("mandatory")
_TeraDS3tera7DayTotalteradsx3ESCP_PFE_Type = Gauge32
_TeraDS3tera7DayTotalteradsx3ESCP_PFE_Object = MibScalar
teraDS3tera7DayTotalteradsx3ESCP_PFE = _TeraDS3tera7DayTotalteradsx3ESCP_PFE_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 7, 1, 9),
    _TeraDS3tera7DayTotalteradsx3ESCP_PFE_Type()
)
teraDS3tera7DayTotalteradsx3ESCP_PFE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDS3tera7DayTotalteradsx3ESCP_PFE.setStatus("mandatory")
_TeraDS3tera7DayTotalteradsx3ESBCP_PFE_Type = Gauge32
_TeraDS3tera7DayTotalteradsx3ESBCP_PFE_Object = MibScalar
teraDS3tera7DayTotalteradsx3ESBCP_PFE = _TeraDS3tera7DayTotalteradsx3ESBCP_PFE_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 7, 1, 10),
    _TeraDS3tera7DayTotalteradsx3ESBCP_PFE_Type()
)
teraDS3tera7DayTotalteradsx3ESBCP_PFE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDS3tera7DayTotalteradsx3ESBCP_PFE.setStatus("mandatory")
_TeraDS3tera7DayTotalteradsx3SASCP_PFE_Type = Gauge32
_TeraDS3tera7DayTotalteradsx3SASCP_PFE_Object = MibScalar
teraDS3tera7DayTotalteradsx3SASCP_PFE = _TeraDS3tera7DayTotalteradsx3SASCP_PFE_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 7, 1, 11),
    _TeraDS3tera7DayTotalteradsx3SASCP_PFE_Type()
)
teraDS3tera7DayTotalteradsx3SASCP_PFE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDS3tera7DayTotalteradsx3SASCP_PFE.setStatus("mandatory")
_TeraDS3tera7DayTotalValidData_Type = Integer32
_TeraDS3tera7DayTotalValidData_Object = MibTableColumn
teraDS3tera7DayTotalValidData = _TeraDS3tera7DayTotalValidData_Object(
    (1, 3, 6, 1, 4, 1, 4513, 8, 7, 1, 12),
    _TeraDS3tera7DayTotalValidData_Type()
)
teraDS3tera7DayTotalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraDS3tera7DayTotalValidData.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TERAWAVE-terads3-MIB",
    **{"terawave": terawave,
       "teraCDS3Group": teraCDS3Group,
       "teraDSX3ConfigTable": teraDSX3ConfigTable,
       "teraDSX3ConfigTableEntry": teraDSX3ConfigTableEntry,
       "teraDs3LineIndex": teraDs3LineIndex,
       "teraDs3OOFCriteria": teraDs3OOFCriteria,
       "teraDs3AISBitsChkSchm": teraDs3AISBitsChkSchm,
       "teraDs3RcvFEACCriteria": teraDs3RcvFEACCriteria,
       "teraDs3FEACLoopCheck": teraDs3FEACLoopCheck,
       "teraDs3DS1FarEndLoopStatus": teraDs3DS1FarEndLoopStatus,
       "teraDs3DS1NearEndLoopStatus": teraDs3DS1NearEndLoopStatus,
       "teraDs37DayTotalTimeElapsed": teraDs37DayTotalTimeElapsed,
       "teraDs3ExtendValidTotalIntervals": teraDs3ExtendValidTotalIntervals,
       "teraDs3ExtendInvalidTotalIntervals": teraDs3ExtendInvalidTotalIntervals,
       "teraDSX37DayTotalTable": teraDSX37DayTotalTable,
       "teraDSX37DayTotalTableEntry": teraDSX37DayTotalTableEntry,
       "teraDS37DayTotalIndex": teraDS37DayTotalIndex,
       "teraDS37DayTotalNumber": teraDS37DayTotalNumber,
       "teraDS37DayTotalPESs": teraDS37DayTotalPESs,
       "teraDS37DayTotalPSESs": teraDS37DayTotalPSESs,
       "teraDS37DayTotalSEFSs": teraDS37DayTotalSEFSs,
       "teraDS37DayTotalUASs": teraDS37DayTotalUASs,
       "teraDS37DayTotalLCVs": teraDS37DayTotalLCVs,
       "teraDS37DayTotalPCVs": teraDS37DayTotalPCVs,
       "teraDS37DayTotalLESs": teraDS37DayTotalLESs,
       "teraDS37DayTotalCCVs": teraDS37DayTotalCCVs,
       "teraDS37DayTotalCESs": teraDS37DayTotalCESs,
       "teraDS37DayTotalCSESs": teraDS37DayTotalCSESs,
       "teraDS37DayTotalValidData": teraDS37DayTotalValidData,
       "teraDSX3FarEnd7DayTotalTable": teraDSX3FarEnd7DayTotalTable,
       "teraDSX3FarEnd7DayTotalTableEntry": teraDSX3FarEnd7DayTotalTableEntry,
       "teraDSX3FarEnd7DayTotalIndex": teraDSX3FarEnd7DayTotalIndex,
       "teraDS3FarEnd7DayTotalNumber": teraDS3FarEnd7DayTotalNumber,
       "teraDS3FarEnd7DayTotalCESs": teraDS3FarEnd7DayTotalCESs,
       "teraDS3FarEnd7DayTotalCSESs": teraDS3FarEnd7DayTotalCSESs,
       "teraDS3FarEnd7DayTotalCCVs": teraDS3FarEnd7DayTotalCCVs,
       "teraDS3FarEnd7DayTotalUASs": teraDS3FarEnd7DayTotalUASs,
       "teraDS3FarEnd7DayTotalValidData": teraDS3FarEnd7DayTotalValidData,
       "teradsx3CurrentTable": teradsx3CurrentTable,
       "teradsx3CurrentTableEntry": teradsx3CurrentTableEntry,
       "teradsx3CurrentIndex": teradsx3CurrentIndex,
       "teradsx3ESB-L": teradsx3ESB_L,
       "teradsx3LOSS-L": teradsx3LOSS_L,
       "teradsx3ESB-P": teradsx3ESB_P,
       "teradsx3SAS-P": teradsx3SAS_P,
       "teradsx3AISS-P": teradsx3AISS_P,
       "teradsx3UASP-P": teradsx3UASP_P,
       "teradsx3ESCP-PFE": teradsx3ESCP_PFE,
       "teradsx3ESBCP-PFE": teradsx3ESBCP_PFE,
       "teradsx3SASCP-PFE": teradsx3SASCP_PFE,
       "teradsx3IntervalTable": teradsx3IntervalTable,
       "teradsx3IntervalTableEntry": teradsx3IntervalTableEntry,
       "terads3IntervalIndex": terads3IntervalIndex,
       "terads3IntervalNumber": terads3IntervalNumber,
       "terads3Intervalteradsx3ESB-L": terads3Intervalteradsx3ESB_L,
       "terads3Intervalteradsx3LOSS-L": terads3Intervalteradsx3LOSS_L,
       "terads3Intervalteradsx3ESB-P": terads3Intervalteradsx3ESB_P,
       "terads3Intervalteradsx3SAS-P": terads3Intervalteradsx3SAS_P,
       "terads3Intervalteradsx3AISS-P": terads3Intervalteradsx3AISS_P,
       "terads3Intervalteradsx3UASP-P": terads3Intervalteradsx3UASP_P,
       "terads3Intervalteradsx3ESCP-PFE": terads3Intervalteradsx3ESCP_PFE,
       "terads3Intervalteradsx3ESBCP-PFE": terads3Intervalteradsx3ESBCP_PFE,
       "terads3Intervalteradsx3SASCP-PFE": terads3Intervalteradsx3SASCP_PFE,
       "terads3IntervalValidData": terads3IntervalValidData,
       "teradsx3TotalTable": teradsx3TotalTable,
       "teradsx3TotalTableEntry": teradsx3TotalTableEntry,
       "terads3TotalIndex": terads3TotalIndex,
       "terads3Totalteradsx3ESB-L": terads3Totalteradsx3ESB_L,
       "terads3Totalteradsx3LOSS-L": terads3Totalteradsx3LOSS_L,
       "terads3Totalteradsx3ESB-P": terads3Totalteradsx3ESB_P,
       "terads3Totalteradsx3SAS-P": terads3Totalteradsx3SAS_P,
       "terads3Totalteradsx3AISS-P": terads3Totalteradsx3AISS_P,
       "terads3Totalteradsx3UASP-P": terads3Totalteradsx3UASP_P,
       "terads3Totalteradsx3ESCP-PFE": terads3Totalteradsx3ESCP_PFE,
       "terads3Totalteradsx3ESBCP-PFE": terads3Totalteradsx3ESBCP_PFE,
       "terads3Totalteradsx3SASCP-PFE": terads3Totalteradsx3SASCP_PFE,
       "terads3TotalPerfStat": terads3TotalPerfStat,
       "teraDSX3tera7DayTotalTable": teraDSX3tera7DayTotalTable,
       "teraDSX3tera7DayTotalTableEntry": teraDSX3tera7DayTotalTableEntry,
       "teraDSX3tera7DayTotalIndex": teraDSX3tera7DayTotalIndex,
       "teraDS3tera7DayTotalNumber": teraDS3tera7DayTotalNumber,
       "teraDS3tera7DayTotalteradsx3ESB-L": teraDS3tera7DayTotalteradsx3ESB_L,
       "teraDS3tera7DayTotalteradsx3LOSS-L": teraDS3tera7DayTotalteradsx3LOSS_L,
       "teraDS3tera7DayTotalteradsx3ESB-P": teraDS3tera7DayTotalteradsx3ESB_P,
       "teraDS3tera7DayTotalteradsx3SAS-P": teraDS3tera7DayTotalteradsx3SAS_P,
       "teraDS3tera7DayTotalteradsx3AISS-P": teraDS3tera7DayTotalteradsx3AISS_P,
       "teraDS3tera7DayTotalteradsx3UASP-P": teraDS3tera7DayTotalteradsx3UASP_P,
       "teraDS3tera7DayTotalteradsx3ESCP-PFE": teraDS3tera7DayTotalteradsx3ESCP_PFE,
       "teraDS3tera7DayTotalteradsx3ESBCP-PFE": teraDS3tera7DayTotalteradsx3ESBCP_PFE,
       "teraDS3tera7DayTotalteradsx3SASCP-PFE": teraDS3tera7DayTotalteradsx3SASCP_PFE,
       "teraDS3tera7DayTotalValidData": teraDS3tera7DayTotalValidData}
)
