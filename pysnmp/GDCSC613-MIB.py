# SNMP MIB module (GDCSC613-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GDCSC613-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:48:20 2024
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

(SCinstance,) = mibBuilder.importSymbols(
    "GDCMACRO-MIB",
    "SCinstance")

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

_Gdc_ObjectIdentity = ObjectIdentity
gdc = _Gdc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498)
)
_Bql2_ObjectIdentity = ObjectIdentity
bql2 = _Bql2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12)
)
_Bql613_ObjectIdentity = ObjectIdentity
bql613 = _Bql613_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 1)
)


class _Bql613MIBVersion_Type(DisplayString):
    """Custom type bql613MIBVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_Bql613MIBVersion_Type.__name__ = "DisplayString"
_Bql613MIBVersion_Object = MibScalar
bql613MIBVersion = _Bql613MIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 1, 1),
    _Bql613MIBVersion_Type()
)
bql613MIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bql613MIBVersion.setStatus("mandatory")
_Bql613WhatAreYouTable_Object = MibTable
bql613WhatAreYouTable = _Bql613WhatAreYouTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 1, 2)
)
if mibBuilder.loadTexts:
    bql613WhatAreYouTable.setStatus("mandatory")
_Bql613WhatAreYouEntry_Object = MibTableRow
bql613WhatAreYouEntry = _Bql613WhatAreYouEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 1, 2, 1)
)
bql613WhatAreYouEntry.setIndexNames(
    (0, "GDCSC613-MIB", "bql613WhatAreYouIndex"),
)
if mibBuilder.loadTexts:
    bql613WhatAreYouEntry.setStatus("mandatory")
_Bql613WhatAreYouIndex_Type = SCinstance
_Bql613WhatAreYouIndex_Object = MibTableColumn
bql613WhatAreYouIndex = _Bql613WhatAreYouIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 1, 2, 1, 1),
    _Bql613WhatAreYouIndex_Type()
)
bql613WhatAreYouIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bql613WhatAreYouIndex.setStatus("mandatory")


class _Bql613CodeRev_Type(DisplayString):
    """Custom type bql613CodeRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Bql613CodeRev_Type.__name__ = "DisplayString"
_Bql613CodeRev_Object = MibTableColumn
bql613CodeRev = _Bql613CodeRev_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 1, 2, 1, 2),
    _Bql613CodeRev_Type()
)
bql613CodeRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bql613CodeRev.setStatus("mandatory")


class _Bql613AlarmStatus_Type(OctetString):
    """Custom type bql613AlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Bql613AlarmStatus_Type.__name__ = "OctetString"
_Bql613AlarmStatus_Object = MibTableColumn
bql613AlarmStatus = _Bql613AlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 1, 2, 1, 3),
    _Bql613AlarmStatus_Type()
)
bql613AlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bql613AlarmStatus.setStatus("mandatory")
_Bql613ConfigTable_Object = MibTable
bql613ConfigTable = _Bql613ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 1, 3)
)
if mibBuilder.loadTexts:
    bql613ConfigTable.setStatus("mandatory")
_Bql613ConfigEntry_Object = MibTableRow
bql613ConfigEntry = _Bql613ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 1, 3, 1)
)
bql613ConfigEntry.setIndexNames(
    (0, "GDCSC613-MIB", "bql613ConfigIndex"),
)
if mibBuilder.loadTexts:
    bql613ConfigEntry.setStatus("mandatory")
_Bql613ConfigIndex_Type = SCinstance
_Bql613ConfigIndex_Object = MibTableColumn
bql613ConfigIndex = _Bql613ConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 1, 3, 1, 1),
    _Bql613ConfigIndex_Type()
)
bql613ConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bql613ConfigIndex.setStatus("mandatory")


class _Bql613TestPattern_Type(Integer32):
    """Custom type bql613TestPattern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pattern2047", 1),
          ("pattern511", 2))
    )


_Bql613TestPattern_Type.__name__ = "Integer32"
_Bql613TestPattern_Object = MibTableColumn
bql613TestPattern = _Bql613TestPattern_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 1, 3, 1, 2),
    _Bql613TestPattern_Type()
)
bql613TestPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bql613TestPattern.setStatus("mandatory")


class _Bql613RLTimeout_Type(Integer32):
    """Custom type bql613RLTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noTimeout", 1),
          ("timeoutAfter10Min", 2))
    )


_Bql613RLTimeout_Type.__name__ = "Integer32"
_Bql613RLTimeout_Object = MibTableColumn
bql613RLTimeout = _Bql613RLTimeout_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 1, 3, 1, 3),
    _Bql613RLTimeout_Type()
)
bql613RLTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bql613RLTimeout.setStatus("mandatory")


class _Bql613MasterTXClkSrc_Type(Integer32):
    """Custom type bql613MasterTXClkSrc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("internal", 1))
    )


_Bql613MasterTXClkSrc_Type.__name__ = "Integer32"
_Bql613MasterTXClkSrc_Object = MibTableColumn
bql613MasterTXClkSrc = _Bql613MasterTXClkSrc_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 1, 3, 1, 4),
    _Bql613MasterTXClkSrc_Type()
)
bql613MasterTXClkSrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bql613MasterTXClkSrc.setStatus("mandatory")


class _Bql613DTEDataRate_Type(Integer32):
    """Custom type bql613DTEDataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("kBps128000", 10),
          ("kBps64000", 9))
    )


_Bql613DTEDataRate_Type.__name__ = "Integer32"
_Bql613DTEDataRate_Object = MibTableColumn
bql613DTEDataRate = _Bql613DTEDataRate_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 1, 3, 1, 5),
    _Bql613DTEDataRate_Type()
)
bql613DTEDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bql613DTEDataRate.setStatus("mandatory")


class _Bql613RespRdl_Type(Integer32):
    """Custom type bql613RespRdl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_Bql613RespRdl_Type.__name__ = "Integer32"
_Bql613RespRdl_Object = MibTableColumn
bql613RespRdl = _Bql613RespRdl_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 1, 3, 1, 6),
    _Bql613RespRdl_Type()
)
bql613RespRdl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bql613RespRdl.setStatus("mandatory")
_Bql613DiagnosticTable_Object = MibTable
bql613DiagnosticTable = _Bql613DiagnosticTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 1, 4)
)
if mibBuilder.loadTexts:
    bql613DiagnosticTable.setStatus("mandatory")
_Bql613DiagnosticEntry_Object = MibTableRow
bql613DiagnosticEntry = _Bql613DiagnosticEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 1, 4, 1)
)
bql613DiagnosticEntry.setIndexNames(
    (0, "GDCSC613-MIB", "bql613DiagnosticIndex"),
)
if mibBuilder.loadTexts:
    bql613DiagnosticEntry.setStatus("mandatory")
_Bql613DiagnosticIndex_Type = SCinstance
_Bql613DiagnosticIndex_Object = MibTableColumn
bql613DiagnosticIndex = _Bql613DiagnosticIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 1, 4, 1, 1),
    _Bql613DiagnosticIndex_Type()
)
bql613DiagnosticIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bql613DiagnosticIndex.setStatus("mandatory")


class _Bql613DiagnosticTest_Type(Integer32):
    """Custom type bql613DiagnosticTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Bql613DiagnosticTest_Type.__name__ = "Integer32"
_Bql613DiagnosticTest_Object = MibTableColumn
bql613DiagnosticTest = _Bql613DiagnosticTest_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 1, 4, 1, 2),
    _Bql613DiagnosticTest_Type()
)
bql613DiagnosticTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bql613DiagnosticTest.setStatus("mandatory")


class _Bql613DiagnosticActive_Type(Integer32):
    """Custom type bql613DiagnosticActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("notActive", 1))
    )


_Bql613DiagnosticActive_Type.__name__ = "Integer32"
_Bql613DiagnosticActive_Object = MibTableColumn
bql613DiagnosticActive = _Bql613DiagnosticActive_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 1, 4, 1, 3),
    _Bql613DiagnosticActive_Type()
)
bql613DiagnosticActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bql613DiagnosticActive.setStatus("mandatory")


class _Bql613DiagnosticResults_Type(Integer32):
    """Custom type bql613DiagnosticResults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_Bql613DiagnosticResults_Type.__name__ = "Integer32"
_Bql613DiagnosticResults_Object = MibTableColumn
bql613DiagnosticResults = _Bql613DiagnosticResults_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 1, 4, 1, 4),
    _Bql613DiagnosticResults_Type()
)
bql613DiagnosticResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bql613DiagnosticResults.setStatus("mandatory")


class _Bql613DiagnosticErrorCount_Type(Integer32):
    """Custom type bql613DiagnosticErrorCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("reset", 2))
    )


_Bql613DiagnosticErrorCount_Type.__name__ = "Integer32"
_Bql613DiagnosticErrorCount_Object = MibTableColumn
bql613DiagnosticErrorCount = _Bql613DiagnosticErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 1, 4, 1, 5),
    _Bql613DiagnosticErrorCount_Type()
)
bql613DiagnosticErrorCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bql613DiagnosticErrorCount.setStatus("mandatory")
_Bql613ControlTable_Object = MibTable
bql613ControlTable = _Bql613ControlTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 1, 6)
)
if mibBuilder.loadTexts:
    bql613ControlTable.setStatus("mandatory")
_Bql613ControlEntry_Object = MibTableRow
bql613ControlEntry = _Bql613ControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 1, 6, 1)
)
bql613ControlEntry.setIndexNames(
    (0, "GDCSC613-MIB", "bql613ControlIndex"),
)
if mibBuilder.loadTexts:
    bql613ControlEntry.setStatus("mandatory")
_Bql613ControlIndex_Type = SCinstance
_Bql613ControlIndex_Object = MibTableColumn
bql613ControlIndex = _Bql613ControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 1, 6, 1, 1),
    _Bql613ControlIndex_Type()
)
bql613ControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bql613ControlIndex.setStatus("mandatory")


class _Bql613SoftReset_Type(Integer32):
    """Custom type bql613SoftReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("reset", 2))
    )


_Bql613SoftReset_Type.__name__ = "Integer32"
_Bql613SoftReset_Object = MibTableColumn
bql613SoftReset = _Bql613SoftReset_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 1, 6, 1, 2),
    _Bql613SoftReset_Type()
)
bql613SoftReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bql613SoftReset.setStatus("mandatory")


class _Bql613EraseConfig_Type(Integer32):
    """Custom type bql613EraseConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("erase", 2),
          ("normal", 1))
    )


_Bql613EraseConfig_Type.__name__ = "Integer32"
_Bql613EraseConfig_Object = MibTableColumn
bql613EraseConfig = _Bql613EraseConfig_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 1, 6, 1, 3),
    _Bql613EraseConfig_Type()
)
bql613EraseConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bql613EraseConfig.setStatus("mandatory")


class _Bql613FrontPanel_Type(Integer32):
    """Custom type bql613FrontPanel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_Bql613FrontPanel_Type.__name__ = "Integer32"
_Bql613FrontPanel_Object = MibTableColumn
bql613FrontPanel = _Bql613FrontPanel_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 1, 6, 1, 4),
    _Bql613FrontPanel_Type()
)
bql613FrontPanel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bql613FrontPanel.setStatus("mandatory")


class _Bql613LEDStatus_Type(OctetString):
    """Custom type bql613LEDStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_Bql613LEDStatus_Type.__name__ = "OctetString"
_Bql613LEDStatus_Object = MibTableColumn
bql613LEDStatus = _Bql613LEDStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 1, 6, 1, 5),
    _Bql613LEDStatus_Type()
)
bql613LEDStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bql613LEDStatus.setStatus("mandatory")
_Bql613CurrentTable_Object = MibTable
bql613CurrentTable = _Bql613CurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 1, 7)
)
if mibBuilder.loadTexts:
    bql613CurrentTable.setStatus("mandatory")
_Bql613CurrentEntry_Object = MibTableRow
bql613CurrentEntry = _Bql613CurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 1, 7, 1)
)
bql613CurrentEntry.setIndexNames(
    (0, "GDCSC613-MIB", "bql613CurrentIndex"),
)
if mibBuilder.loadTexts:
    bql613CurrentEntry.setStatus("mandatory")
_Bql613CurrentIndex_Type = SCinstance
_Bql613CurrentIndex_Object = MibTableColumn
bql613CurrentIndex = _Bql613CurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 1, 7, 1, 1),
    _Bql613CurrentIndex_Type()
)
bql613CurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bql613CurrentIndex.setStatus("mandatory")


class _Bql613CurrentStats_Type(OctetString):
    """Custom type bql613CurrentStats based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_Bql613CurrentStats_Type.__name__ = "OctetString"
_Bql613CurrentStats_Object = MibTableColumn
bql613CurrentStats = _Bql613CurrentStats_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 1, 7, 1, 2),
    _Bql613CurrentStats_Type()
)
bql613CurrentStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bql613CurrentStats.setStatus("mandatory")
_Bql613IntervalTable_Object = MibTable
bql613IntervalTable = _Bql613IntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 1, 8)
)
if mibBuilder.loadTexts:
    bql613IntervalTable.setStatus("mandatory")
_Bql613IntervalEntry_Object = MibTableRow
bql613IntervalEntry = _Bql613IntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 1, 8, 1)
)
bql613IntervalEntry.setIndexNames(
    (0, "GDCSC613-MIB", "bql613IntervalIndex"),
    (0, "GDCSC613-MIB", "bql613IntervalNumber"),
)
if mibBuilder.loadTexts:
    bql613IntervalEntry.setStatus("mandatory")
_Bql613IntervalIndex_Type = SCinstance
_Bql613IntervalIndex_Object = MibTableColumn
bql613IntervalIndex = _Bql613IntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 1, 8, 1, 1),
    _Bql613IntervalIndex_Type()
)
bql613IntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bql613IntervalIndex.setStatus("mandatory")


class _Bql613IntervalNumber_Type(Integer32):
    """Custom type bql613IntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_Bql613IntervalNumber_Type.__name__ = "Integer32"
_Bql613IntervalNumber_Object = MibTableColumn
bql613IntervalNumber = _Bql613IntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 1, 8, 1, 2),
    _Bql613IntervalNumber_Type()
)
bql613IntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bql613IntervalNumber.setStatus("mandatory")


class _Bql613IntervalStats_Type(OctetString):
    """Custom type bql613IntervalStats based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_Bql613IntervalStats_Type.__name__ = "OctetString"
_Bql613IntervalStats_Object = MibTableColumn
bql613IntervalStats = _Bql613IntervalStats_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 1, 8, 1, 3),
    _Bql613IntervalStats_Type()
)
bql613IntervalStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bql613IntervalStats.setStatus("mandatory")
_Bql613TotalTable_Object = MibTable
bql613TotalTable = _Bql613TotalTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 1, 9)
)
if mibBuilder.loadTexts:
    bql613TotalTable.setStatus("mandatory")
_Bql613TotalEntry_Object = MibTableRow
bql613TotalEntry = _Bql613TotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 1, 9, 1)
)
bql613TotalEntry.setIndexNames(
    (0, "GDCSC613-MIB", "bql613TotalIndex"),
)
if mibBuilder.loadTexts:
    bql613TotalEntry.setStatus("mandatory")
_Bql613TotalIndex_Type = SCinstance
_Bql613TotalIndex_Object = MibTableColumn
bql613TotalIndex = _Bql613TotalIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 1, 9, 1, 1),
    _Bql613TotalIndex_Type()
)
bql613TotalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bql613TotalIndex.setStatus("mandatory")


class _Bql613TotalStats_Type(OctetString):
    """Custom type bql613TotalStats based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_Bql613TotalStats_Type.__name__ = "OctetString"
_Bql613TotalStats_Object = MibTableColumn
bql613TotalStats = _Bql613TotalStats_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 1, 9, 1, 2),
    _Bql613TotalStats_Type()
)
bql613TotalStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bql613TotalStats.setStatus("mandatory")
_Bql613IntervalMaintenanceTable_Object = MibTable
bql613IntervalMaintenanceTable = _Bql613IntervalMaintenanceTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 1, 10)
)
if mibBuilder.loadTexts:
    bql613IntervalMaintenanceTable.setStatus("mandatory")
_Bql613IntervalMaintenanceEntry_Object = MibTableRow
bql613IntervalMaintenanceEntry = _Bql613IntervalMaintenanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 1, 10, 1)
)
bql613IntervalMaintenanceEntry.setIndexNames(
    (0, "GDCSC613-MIB", "bql613IntervalMaintenanceIndex"),
)
if mibBuilder.loadTexts:
    bql613IntervalMaintenanceEntry.setStatus("mandatory")
_Bql613IntervalMaintenanceIndex_Type = SCinstance
_Bql613IntervalMaintenanceIndex_Object = MibTableColumn
bql613IntervalMaintenanceIndex = _Bql613IntervalMaintenanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 1, 10, 1, 1),
    _Bql613IntervalMaintenanceIndex_Type()
)
bql613IntervalMaintenanceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bql613IntervalMaintenanceIndex.setStatus("mandatory")


class _Bql613ResetIntervals_Type(Integer32):
    """Custom type bql613ResetIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("norm", 1),
          ("reset", 2))
    )


_Bql613ResetIntervals_Type.__name__ = "Integer32"
_Bql613ResetIntervals_Object = MibTableColumn
bql613ResetIntervals = _Bql613ResetIntervals_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 1, 10, 1, 2),
    _Bql613ResetIntervals_Type()
)
bql613ResetIntervals.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bql613ResetIntervals.setStatus("mandatory")


class _Bql613NumberofValidIntervals_Type(Integer32):
    """Custom type bql613NumberofValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_Bql613NumberofValidIntervals_Type.__name__ = "Integer32"
_Bql613NumberofValidIntervals_Object = MibTableColumn
bql613NumberofValidIntervals = _Bql613NumberofValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 1, 10, 1, 3),
    _Bql613NumberofValidIntervals_Type()
)
bql613NumberofValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bql613NumberofValidIntervals.setStatus("mandatory")


class _Bql613ResetMajorAlarm_Type(Integer32):
    """Custom type bql613ResetMajorAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("norm", 2),
          ("reset", 1))
    )


_Bql613ResetMajorAlarm_Type.__name__ = "Integer32"
_Bql613ResetMajorAlarm_Object = MibTableColumn
bql613ResetMajorAlarm = _Bql613ResetMajorAlarm_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 1, 10, 1, 4),
    _Bql613ResetMajorAlarm_Type()
)
bql613ResetMajorAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bql613ResetMajorAlarm.setStatus("mandatory")


class _Bql613ResetMinorAlarm_Type(Integer32):
    """Custom type bql613ResetMinorAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("norm", 2),
          ("reset", 1))
    )


_Bql613ResetMinorAlarm_Type.__name__ = "Integer32"
_Bql613ResetMinorAlarm_Object = MibTableColumn
bql613ResetMinorAlarm = _Bql613ResetMinorAlarm_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 1, 10, 1, 5),
    _Bql613ResetMinorAlarm_Type()
)
bql613ResetMinorAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bql613ResetMinorAlarm.setStatus("mandatory")
_Bql613Alarm_ObjectIdentity = ObjectIdentity
bql613Alarm = _Bql613Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 7)
)
_Bql613AlarmData_ObjectIdentity = ObjectIdentity
bql613AlarmData = _Bql613AlarmData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 7, 1)
)
_Bql613NoResponseAlm_ObjectIdentity = ObjectIdentity
bql613NoResponseAlm = _Bql613NoResponseAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 7, 1, 1)
)
_Bql613DiagRxErrAlm_ObjectIdentity = ObjectIdentity
bql613DiagRxErrAlm = _Bql613DiagRxErrAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 7, 1, 2)
)
_Bql613PowerUpAlm_ObjectIdentity = ObjectIdentity
bql613PowerUpAlm = _Bql613PowerUpAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 7, 1, 3)
)
_Bql613Lp2B1QOutofSyncAlm_ObjectIdentity = ObjectIdentity
bql613Lp2B1QOutofSyncAlm = _Bql613Lp2B1QOutofSyncAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 7, 1, 4)
)
_Bql613LpTxClockOutOfTolerance_ObjectIdentity = ObjectIdentity
bql613LpTxClockOutOfTolerance = _Bql613LpTxClockOutOfTolerance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 7, 1, 5)
)
_Bql613LpExtTxClkAlm_ObjectIdentity = ObjectIdentity
bql613LpExtTxClkAlm = _Bql613LpExtTxClkAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 7, 1, 6)
)
_Bql613LpSealingCurrentNoContinuityAlm_ObjectIdentity = ObjectIdentity
bql613LpSealingCurrentNoContinuityAlm = _Bql613LpSealingCurrentNoContinuityAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 7, 1, 7)
)
_Bql613LpMajorBERAlm_ObjectIdentity = ObjectIdentity
bql613LpMajorBERAlm = _Bql613LpMajorBERAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 7, 1, 8)
)
_Bql613LpMinorBERAlm_ObjectIdentity = ObjectIdentity
bql613LpMinorBERAlm = _Bql613LpMinorBERAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 7, 1, 9)
)
_Bql613AlarmConfigTable_Object = MibTable
bql613AlarmConfigTable = _Bql613AlarmConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 7, 2)
)
if mibBuilder.loadTexts:
    bql613AlarmConfigTable.setStatus("mandatory")
_Bql613AlarmConfigEntry_Object = MibTableRow
bql613AlarmConfigEntry = _Bql613AlarmConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 7, 2, 1)
)
bql613AlarmConfigEntry.setIndexNames(
    (0, "GDCSC613-MIB", "bql613AlarmConfigIndex"),
    (0, "GDCSC613-MIB", "bql613AlarmConfigIdentifier"),
)
if mibBuilder.loadTexts:
    bql613AlarmConfigEntry.setStatus("mandatory")
_Bql613AlarmConfigIndex_Type = SCinstance
_Bql613AlarmConfigIndex_Object = MibTableColumn
bql613AlarmConfigIndex = _Bql613AlarmConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 7, 2, 1, 1),
    _Bql613AlarmConfigIndex_Type()
)
bql613AlarmConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bql613AlarmConfigIndex.setStatus("mandatory")
_Bql613AlarmConfigIdentifier_Type = ObjectIdentifier
_Bql613AlarmConfigIdentifier_Object = MibTableColumn
bql613AlarmConfigIdentifier = _Bql613AlarmConfigIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 7, 2, 1, 2),
    _Bql613AlarmConfigIdentifier_Type()
)
bql613AlarmConfigIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bql613AlarmConfigIdentifier.setStatus("mandatory")


class _Bql613AlarmThreshold_Type(Integer32):
    """Custom type bql613AlarmThreshold based on Integer32"""
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
        *(("thres10E03", 1),
          ("thres10E04", 2),
          ("thres10E05", 3),
          ("thres10E06", 4))
    )


_Bql613AlarmThreshold_Type.__name__ = "Integer32"
_Bql613AlarmThreshold_Object = MibTableColumn
bql613AlarmThreshold = _Bql613AlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 7, 2, 1, 3),
    _Bql613AlarmThreshold_Type()
)
bql613AlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bql613AlarmThreshold.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GDCSC613-MIB",
    **{"gdc": gdc,
       "bql2": bql2,
       "bql613": bql613,
       "bql613MIBVersion": bql613MIBVersion,
       "bql613WhatAreYouTable": bql613WhatAreYouTable,
       "bql613WhatAreYouEntry": bql613WhatAreYouEntry,
       "bql613WhatAreYouIndex": bql613WhatAreYouIndex,
       "bql613CodeRev": bql613CodeRev,
       "bql613AlarmStatus": bql613AlarmStatus,
       "bql613ConfigTable": bql613ConfigTable,
       "bql613ConfigEntry": bql613ConfigEntry,
       "bql613ConfigIndex": bql613ConfigIndex,
       "bql613TestPattern": bql613TestPattern,
       "bql613RLTimeout": bql613RLTimeout,
       "bql613MasterTXClkSrc": bql613MasterTXClkSrc,
       "bql613DTEDataRate": bql613DTEDataRate,
       "bql613RespRdl": bql613RespRdl,
       "bql613DiagnosticTable": bql613DiagnosticTable,
       "bql613DiagnosticEntry": bql613DiagnosticEntry,
       "bql613DiagnosticIndex": bql613DiagnosticIndex,
       "bql613DiagnosticTest": bql613DiagnosticTest,
       "bql613DiagnosticActive": bql613DiagnosticActive,
       "bql613DiagnosticResults": bql613DiagnosticResults,
       "bql613DiagnosticErrorCount": bql613DiagnosticErrorCount,
       "bql613ControlTable": bql613ControlTable,
       "bql613ControlEntry": bql613ControlEntry,
       "bql613ControlIndex": bql613ControlIndex,
       "bql613SoftReset": bql613SoftReset,
       "bql613EraseConfig": bql613EraseConfig,
       "bql613FrontPanel": bql613FrontPanel,
       "bql613LEDStatus": bql613LEDStatus,
       "bql613CurrentTable": bql613CurrentTable,
       "bql613CurrentEntry": bql613CurrentEntry,
       "bql613CurrentIndex": bql613CurrentIndex,
       "bql613CurrentStats": bql613CurrentStats,
       "bql613IntervalTable": bql613IntervalTable,
       "bql613IntervalEntry": bql613IntervalEntry,
       "bql613IntervalIndex": bql613IntervalIndex,
       "bql613IntervalNumber": bql613IntervalNumber,
       "bql613IntervalStats": bql613IntervalStats,
       "bql613TotalTable": bql613TotalTable,
       "bql613TotalEntry": bql613TotalEntry,
       "bql613TotalIndex": bql613TotalIndex,
       "bql613TotalStats": bql613TotalStats,
       "bql613IntervalMaintenanceTable": bql613IntervalMaintenanceTable,
       "bql613IntervalMaintenanceEntry": bql613IntervalMaintenanceEntry,
       "bql613IntervalMaintenanceIndex": bql613IntervalMaintenanceIndex,
       "bql613ResetIntervals": bql613ResetIntervals,
       "bql613NumberofValidIntervals": bql613NumberofValidIntervals,
       "bql613ResetMajorAlarm": bql613ResetMajorAlarm,
       "bql613ResetMinorAlarm": bql613ResetMinorAlarm,
       "bql613Alarm": bql613Alarm,
       "bql613AlarmData": bql613AlarmData,
       "bql613NoResponseAlm": bql613NoResponseAlm,
       "bql613DiagRxErrAlm": bql613DiagRxErrAlm,
       "bql613PowerUpAlm": bql613PowerUpAlm,
       "bql613Lp2B1QOutofSyncAlm": bql613Lp2B1QOutofSyncAlm,
       "bql613LpTxClockOutOfTolerance": bql613LpTxClockOutOfTolerance,
       "bql613LpExtTxClkAlm": bql613LpExtTxClkAlm,
       "bql613LpSealingCurrentNoContinuityAlm": bql613LpSealingCurrentNoContinuityAlm,
       "bql613LpMajorBERAlm": bql613LpMajorBERAlm,
       "bql613LpMinorBERAlm": bql613LpMinorBERAlm,
       "bql613AlarmConfigTable": bql613AlarmConfigTable,
       "bql613AlarmConfigEntry": bql613AlarmConfigEntry,
       "bql613AlarmConfigIndex": bql613AlarmConfigIndex,
       "bql613AlarmConfigIdentifier": bql613AlarmConfigIdentifier,
       "bql613AlarmThreshold": bql613AlarmThreshold}
)
