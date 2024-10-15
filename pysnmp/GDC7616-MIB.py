# SNMP MIB module (GDC7616-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GDC7616-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:48:11 2024
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
_Uas7616_ObjectIdentity = ObjectIdentity
uas7616 = _Uas7616_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 4)
)


class _Uas7616MIBVersion_Type(DisplayString):
    """Custom type uas7616MIBVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_Uas7616MIBVersion_Type.__name__ = "DisplayString"
_Uas7616MIBVersion_Object = MibScalar
uas7616MIBVersion = _Uas7616MIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 1),
    _Uas7616MIBVersion_Type()
)
uas7616MIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7616MIBVersion.setStatus("mandatory")
_Uas7616WhatAreYouTable_Object = MibTable
uas7616WhatAreYouTable = _Uas7616WhatAreYouTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 2)
)
if mibBuilder.loadTexts:
    uas7616WhatAreYouTable.setStatus("mandatory")
_Uas7616WhatAreYouEntry_Object = MibTableRow
uas7616WhatAreYouEntry = _Uas7616WhatAreYouEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 2, 1)
)
uas7616WhatAreYouEntry.setIndexNames(
    (0, "GDC7616-MIB", "uas7616WhatAreYouIndex"),
)
if mibBuilder.loadTexts:
    uas7616WhatAreYouEntry.setStatus("mandatory")
_Uas7616WhatAreYouIndex_Type = SCinstance
_Uas7616WhatAreYouIndex_Object = MibTableColumn
uas7616WhatAreYouIndex = _Uas7616WhatAreYouIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 2, 1, 1),
    _Uas7616WhatAreYouIndex_Type()
)
uas7616WhatAreYouIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7616WhatAreYouIndex.setStatus("mandatory")


class _Uas7616CodeRev_Type(DisplayString):
    """Custom type uas7616CodeRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Uas7616CodeRev_Type.__name__ = "DisplayString"
_Uas7616CodeRev_Object = MibTableColumn
uas7616CodeRev = _Uas7616CodeRev_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 2, 1, 2),
    _Uas7616CodeRev_Type()
)
uas7616CodeRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7616CodeRev.setStatus("mandatory")


class _Uas7616AlarmStatus_Type(OctetString):
    """Custom type uas7616AlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Uas7616AlarmStatus_Type.__name__ = "OctetString"
_Uas7616AlarmStatus_Object = MibTableColumn
uas7616AlarmStatus = _Uas7616AlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 2, 1, 3),
    _Uas7616AlarmStatus_Type()
)
uas7616AlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7616AlarmStatus.setStatus("mandatory")


class _Uas7616SystemTimingGenStatus_Type(Integer32):
    """Custom type uas7616SystemTimingGenStatus based on Integer32"""
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
        *(("clk4mhz", 3),
          ("clk8khz", 2),
          ("clk8khzand4mhz", 4),
          ("none", 1))
    )


_Uas7616SystemTimingGenStatus_Type.__name__ = "Integer32"
_Uas7616SystemTimingGenStatus_Object = MibTableColumn
uas7616SystemTimingGenStatus = _Uas7616SystemTimingGenStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 2, 1, 4),
    _Uas7616SystemTimingGenStatus_Type()
)
uas7616SystemTimingGenStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7616SystemTimingGenStatus.setStatus("mandatory")
_Uas7616ConfigTable_Object = MibTable
uas7616ConfigTable = _Uas7616ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 3)
)
if mibBuilder.loadTexts:
    uas7616ConfigTable.setStatus("mandatory")
_Uas7616ConfigEntry_Object = MibTableRow
uas7616ConfigEntry = _Uas7616ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 3, 1)
)
uas7616ConfigEntry.setIndexNames(
    (0, "GDC7616-MIB", "uas7616ConfigIndex"),
)
if mibBuilder.loadTexts:
    uas7616ConfigEntry.setStatus("mandatory")
_Uas7616ConfigIndex_Type = SCinstance
_Uas7616ConfigIndex_Object = MibTableColumn
uas7616ConfigIndex = _Uas7616ConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 3, 1, 1),
    _Uas7616ConfigIndex_Type()
)
uas7616ConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7616ConfigIndex.setStatus("mandatory")


class _Uas7616TXClockSource_Type(Integer32):
    """Custom type uas7616TXClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("internal", 3),
          ("recovered", 2),
          ("system", 1))
    )


_Uas7616TXClockSource_Type.__name__ = "Integer32"
_Uas7616TXClockSource_Object = MibTableColumn
uas7616TXClockSource = _Uas7616TXClockSource_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 3, 1, 2),
    _Uas7616TXClockSource_Type()
)
uas7616TXClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7616TXClockSource.setStatus("mandatory")


class _Uas7616TerminationType_Type(Integer32):
    """Custom type uas7616TerminationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lt", 2),
          ("nt", 1))
    )


_Uas7616TerminationType_Type.__name__ = "Integer32"
_Uas7616TerminationType_Object = MibTableColumn
uas7616TerminationType = _Uas7616TerminationType_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 3, 1, 3),
    _Uas7616TerminationType_Type()
)
uas7616TerminationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7616TerminationType.setStatus("mandatory")


class _Uas7616ChADataRate_Type(Integer32):
    """Custom type uas7616ChADataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inhibit", 3),
          ("kbps128", 2),
          ("kbps64", 1))
    )


_Uas7616ChADataRate_Type.__name__ = "Integer32"
_Uas7616ChADataRate_Object = MibTableColumn
uas7616ChADataRate = _Uas7616ChADataRate_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 3, 1, 4),
    _Uas7616ChADataRate_Type()
)
uas7616ChADataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7616ChADataRate.setStatus("mandatory")


class _Uas7616ChBDataRate_Type(Integer32):
    """Custom type uas7616ChBDataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inhibit", 2),
          ("kbps64", 1))
    )


_Uas7616ChBDataRate_Type.__name__ = "Integer32"
_Uas7616ChBDataRate_Object = MibTableColumn
uas7616ChBDataRate = _Uas7616ChBDataRate_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 3, 1, 5),
    _Uas7616ChBDataRate_Type()
)
uas7616ChBDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7616ChBDataRate.setStatus("mandatory")
_Uas7616ControlTable_Object = MibTable
uas7616ControlTable = _Uas7616ControlTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 5)
)
if mibBuilder.loadTexts:
    uas7616ControlTable.setStatus("mandatory")
_Uas7616ControlEntry_Object = MibTableRow
uas7616ControlEntry = _Uas7616ControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 5, 1)
)
uas7616ControlEntry.setIndexNames(
    (0, "GDC7616-MIB", "uas7616ControlIndex"),
)
if mibBuilder.loadTexts:
    uas7616ControlEntry.setStatus("mandatory")
_Uas7616ControlIndex_Type = SCinstance
_Uas7616ControlIndex_Object = MibTableColumn
uas7616ControlIndex = _Uas7616ControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 5, 1, 1),
    _Uas7616ControlIndex_Type()
)
uas7616ControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7616ControlIndex.setStatus("mandatory")


class _Uas7616SoftReset_Type(Integer32):
    """Custom type uas7616SoftReset based on Integer32"""
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


_Uas7616SoftReset_Type.__name__ = "Integer32"
_Uas7616SoftReset_Object = MibTableColumn
uas7616SoftReset = _Uas7616SoftReset_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 5, 1, 2),
    _Uas7616SoftReset_Type()
)
uas7616SoftReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7616SoftReset.setStatus("mandatory")


class _Uas7616EraseConfig_Type(Integer32):
    """Custom type uas7616EraseConfig based on Integer32"""
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


_Uas7616EraseConfig_Type.__name__ = "Integer32"
_Uas7616EraseConfig_Object = MibTableColumn
uas7616EraseConfig = _Uas7616EraseConfig_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 5, 1, 3),
    _Uas7616EraseConfig_Type()
)
uas7616EraseConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7616EraseConfig.setStatus("mandatory")


class _Uas7616LEDStatus_Type(OctetString):
    """Custom type uas7616LEDStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_Uas7616LEDStatus_Type.__name__ = "OctetString"
_Uas7616LEDStatus_Object = MibTableColumn
uas7616LEDStatus = _Uas7616LEDStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 5, 1, 4),
    _Uas7616LEDStatus_Type()
)
uas7616LEDStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7616LEDStatus.setStatus("mandatory")


class _Uas7616InterfaceType_Type(Integer32):
    """Custom type uas7616InterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("diu", 1),
          ("niu", 2),
          ("notAssigned", 3))
    )


_Uas7616InterfaceType_Type.__name__ = "Integer32"
_Uas7616InterfaceType_Object = MibTableColumn
uas7616InterfaceType = _Uas7616InterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 5, 1, 5),
    _Uas7616InterfaceType_Type()
)
uas7616InterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7616InterfaceType.setStatus("mandatory")


class _Uas7616SysTimingGen_Type(Integer32):
    """Custom type uas7616SysTimingGen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("primary", 2),
          ("secondary", 3))
    )


_Uas7616SysTimingGen_Type.__name__ = "Integer32"
_Uas7616SysTimingGen_Object = MibTableColumn
uas7616SysTimingGen = _Uas7616SysTimingGen_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 5, 1, 6),
    _Uas7616SysTimingGen_Type()
)
uas7616SysTimingGen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7616SysTimingGen.setStatus("mandatory")


class _Uas7616ResetIntervals_Type(Integer32):
    """Custom type uas7616ResetIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 2),
          ("reset", 1))
    )


_Uas7616ResetIntervals_Type.__name__ = "Integer32"
_Uas7616ResetIntervals_Object = MibTableColumn
uas7616ResetIntervals = _Uas7616ResetIntervals_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 5, 1, 7),
    _Uas7616ResetIntervals_Type()
)
uas7616ResetIntervals.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7616ResetIntervals.setStatus("mandatory")


class _Uas7616SysUpTime_Type(Integer32):
    """Custom type uas7616SysUpTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Uas7616SysUpTime_Type.__name__ = "Integer32"
_Uas7616SysUpTime_Object = MibTableColumn
uas7616SysUpTime = _Uas7616SysUpTime_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 5, 1, 8),
    _Uas7616SysUpTime_Type()
)
uas7616SysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7616SysUpTime.setStatus("mandatory")


class _Uas7616SetRealTime_Type(Integer32):
    """Custom type uas7616SetRealTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Uas7616SetRealTime_Type.__name__ = "Integer32"
_Uas7616SetRealTime_Object = MibTableColumn
uas7616SetRealTime = _Uas7616SetRealTime_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 5, 1, 9),
    _Uas7616SetRealTime_Type()
)
uas7616SetRealTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7616SetRealTime.setStatus("mandatory")


class _Uas7616ModuleClkSrc_Type(Integer32):
    """Custom type uas7616ModuleClkSrc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("internal", 2),
          ("recovered", 3),
          ("system", 1))
    )


_Uas7616ModuleClkSrc_Type.__name__ = "Integer32"
_Uas7616ModuleClkSrc_Object = MibTableColumn
uas7616ModuleClkSrc = _Uas7616ModuleClkSrc_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 5, 1, 10),
    _Uas7616ModuleClkSrc_Type()
)
uas7616ModuleClkSrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7616ModuleClkSrc.setStatus("mandatory")


class _Uas7616ResetMajorAlarm_Type(Integer32):
    """Custom type uas7616ResetMajorAlarm based on Integer32"""
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


_Uas7616ResetMajorAlarm_Type.__name__ = "Integer32"
_Uas7616ResetMajorAlarm_Object = MibTableColumn
uas7616ResetMajorAlarm = _Uas7616ResetMajorAlarm_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 5, 1, 11),
    _Uas7616ResetMajorAlarm_Type()
)
uas7616ResetMajorAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7616ResetMajorAlarm.setStatus("mandatory")


class _Uas7616ResetMinorAlarm_Type(Integer32):
    """Custom type uas7616ResetMinorAlarm based on Integer32"""
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


_Uas7616ResetMinorAlarm_Type.__name__ = "Integer32"
_Uas7616ResetMinorAlarm_Object = MibTableColumn
uas7616ResetMinorAlarm = _Uas7616ResetMinorAlarm_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 5, 1, 12),
    _Uas7616ResetMinorAlarm_Type()
)
uas7616ResetMinorAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7616ResetMinorAlarm.setStatus("mandatory")
_Uas7616DiagnosticTable_Object = MibTable
uas7616DiagnosticTable = _Uas7616DiagnosticTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 6)
)
if mibBuilder.loadTexts:
    uas7616DiagnosticTable.setStatus("mandatory")
_Uas7616DiagnosticEntry_Object = MibTableRow
uas7616DiagnosticEntry = _Uas7616DiagnosticEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 6, 1)
)
uas7616DiagnosticEntry.setIndexNames(
    (0, "GDC7616-MIB", "uas7616DiagnosticIndex"),
    (0, "GDC7616-MIB", "uas7616DiagnosticChnlIndex"),
)
if mibBuilder.loadTexts:
    uas7616DiagnosticEntry.setStatus("mandatory")
_Uas7616DiagnosticIndex_Type = SCinstance
_Uas7616DiagnosticIndex_Object = MibTableColumn
uas7616DiagnosticIndex = _Uas7616DiagnosticIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 6, 1, 1),
    _Uas7616DiagnosticIndex_Type()
)
uas7616DiagnosticIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7616DiagnosticIndex.setStatus("mandatory")


class _Uas7616DiagnosticChnlIndex_Type(Integer32):
    """Custom type uas7616DiagnosticChnlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("channelA", 1),
          ("channelB", 2))
    )


_Uas7616DiagnosticChnlIndex_Type.__name__ = "Integer32"
_Uas7616DiagnosticChnlIndex_Object = MibTableColumn
uas7616DiagnosticChnlIndex = _Uas7616DiagnosticChnlIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 6, 1, 2),
    _Uas7616DiagnosticChnlIndex_Type()
)
uas7616DiagnosticChnlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7616DiagnosticChnlIndex.setStatus("mandatory")


class _Uas7616DiagnosticTest_Type(Integer32):
    """Custom type uas7616DiagnosticTest based on Integer32"""
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
        *(("digitalLoopback", 2),
          ("patternGenTest", 3),
          ("rdl", 5),
          ("rdlSelfTest", 6),
          ("stopTest", 1),
          ("unitTest", 4))
    )


_Uas7616DiagnosticTest_Type.__name__ = "Integer32"
_Uas7616DiagnosticTest_Object = MibTableColumn
uas7616DiagnosticTest = _Uas7616DiagnosticTest_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 6, 1, 3),
    _Uas7616DiagnosticTest_Type()
)
uas7616DiagnosticTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7616DiagnosticTest.setStatus("mandatory")


class _Uas7616DiagnosticResetErrorCount_Type(Integer32):
    """Custom type uas7616DiagnosticResetErrorCount based on Integer32"""
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


_Uas7616DiagnosticResetErrorCount_Type.__name__ = "Integer32"
_Uas7616DiagnosticResetErrorCount_Object = MibTableColumn
uas7616DiagnosticResetErrorCount = _Uas7616DiagnosticResetErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 6, 1, 4),
    _Uas7616DiagnosticResetErrorCount_Type()
)
uas7616DiagnosticResetErrorCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7616DiagnosticResetErrorCount.setStatus("mandatory")


class _Uas7616DiagnosticResults_Type(Integer32):
    """Custom type uas7616DiagnosticResults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2097153),
    )


_Uas7616DiagnosticResults_Type.__name__ = "Integer32"
_Uas7616DiagnosticResults_Object = MibTableColumn
uas7616DiagnosticResults = _Uas7616DiagnosticResults_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 6, 1, 5),
    _Uas7616DiagnosticResults_Type()
)
uas7616DiagnosticResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7616DiagnosticResults.setStatus("mandatory")
_Uas7616Current15MinTable_Object = MibTable
uas7616Current15MinTable = _Uas7616Current15MinTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 8)
)
if mibBuilder.loadTexts:
    uas7616Current15MinTable.setStatus("mandatory")
_Uas7616Current15MinEntry_Object = MibTableRow
uas7616Current15MinEntry = _Uas7616Current15MinEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 8, 1)
)
uas7616Current15MinEntry.setIndexNames(
    (0, "GDC7616-MIB", "uas7616Current15MinIndex"),
)
if mibBuilder.loadTexts:
    uas7616Current15MinEntry.setStatus("mandatory")
_Uas7616Current15MinIndex_Type = SCinstance
_Uas7616Current15MinIndex_Object = MibTableColumn
uas7616Current15MinIndex = _Uas7616Current15MinIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 8, 1, 1),
    _Uas7616Current15MinIndex_Type()
)
uas7616Current15MinIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7616Current15MinIndex.setStatus("mandatory")


class _Uas7616Current15MinStat_Type(OctetString):
    """Custom type uas7616Current15MinStat based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_Uas7616Current15MinStat_Type.__name__ = "OctetString"
_Uas7616Current15MinStat_Object = MibTableColumn
uas7616Current15MinStat = _Uas7616Current15MinStat_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 8, 1, 2),
    _Uas7616Current15MinStat_Type()
)
uas7616Current15MinStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7616Current15MinStat.setStatus("mandatory")
_Uas7616IntervalTable_Object = MibTable
uas7616IntervalTable = _Uas7616IntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 9)
)
if mibBuilder.loadTexts:
    uas7616IntervalTable.setStatus("mandatory")
_Uas7616IntervalEntry_Object = MibTableRow
uas7616IntervalEntry = _Uas7616IntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 9, 1)
)
uas7616IntervalEntry.setIndexNames(
    (0, "GDC7616-MIB", "uas7616IntervalIndex"),
    (0, "GDC7616-MIB", "uas7616IntervalNumber"),
)
if mibBuilder.loadTexts:
    uas7616IntervalEntry.setStatus("mandatory")
_Uas7616IntervalIndex_Type = SCinstance
_Uas7616IntervalIndex_Object = MibTableColumn
uas7616IntervalIndex = _Uas7616IntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 9, 1, 1),
    _Uas7616IntervalIndex_Type()
)
uas7616IntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7616IntervalIndex.setStatus("mandatory")


class _Uas7616IntervalNumber_Type(Integer32):
    """Custom type uas7616IntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Uas7616IntervalNumber_Type.__name__ = "Integer32"
_Uas7616IntervalNumber_Object = MibTableColumn
uas7616IntervalNumber = _Uas7616IntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 9, 1, 2),
    _Uas7616IntervalNumber_Type()
)
uas7616IntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7616IntervalNumber.setStatus("mandatory")


class _Uas7616IntervalStat_Type(OctetString):
    """Custom type uas7616IntervalStat based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )


_Uas7616IntervalStat_Type.__name__ = "OctetString"
_Uas7616IntervalStat_Object = MibTableColumn
uas7616IntervalStat = _Uas7616IntervalStat_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 9, 1, 3),
    _Uas7616IntervalStat_Type()
)
uas7616IntervalStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7616IntervalStat.setStatus("mandatory")
_Uas7616Current24HrTable_Object = MibTable
uas7616Current24HrTable = _Uas7616Current24HrTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 10)
)
if mibBuilder.loadTexts:
    uas7616Current24HrTable.setStatus("mandatory")
_Uas7616Current24HrEntry_Object = MibTableRow
uas7616Current24HrEntry = _Uas7616Current24HrEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 10, 1)
)
uas7616Current24HrEntry.setIndexNames(
    (0, "GDC7616-MIB", "uas7616Current24HrIndex"),
)
if mibBuilder.loadTexts:
    uas7616Current24HrEntry.setStatus("mandatory")
_Uas7616Current24HrIndex_Type = SCinstance
_Uas7616Current24HrIndex_Object = MibTableColumn
uas7616Current24HrIndex = _Uas7616Current24HrIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 10, 1, 1),
    _Uas7616Current24HrIndex_Type()
)
uas7616Current24HrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7616Current24HrIndex.setStatus("mandatory")


class _Uas7616Current24HrStat_Type(OctetString):
    """Custom type uas7616Current24HrStat based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(14, 14),
    )


_Uas7616Current24HrStat_Type.__name__ = "OctetString"
_Uas7616Current24HrStat_Object = MibTableColumn
uas7616Current24HrStat = _Uas7616Current24HrStat_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 10, 1, 2),
    _Uas7616Current24HrStat_Type()
)
uas7616Current24HrStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7616Current24HrStat.setStatus("mandatory")
_Uas7616Recent24HrTable_Object = MibTable
uas7616Recent24HrTable = _Uas7616Recent24HrTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 11)
)
if mibBuilder.loadTexts:
    uas7616Recent24HrTable.setStatus("mandatory")
_Uas7616Recent24HrEntry_Object = MibTableRow
uas7616Recent24HrEntry = _Uas7616Recent24HrEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 11, 1)
)
uas7616Recent24HrEntry.setIndexNames(
    (0, "GDC7616-MIB", "uas7616Recent24HrIndex"),
)
if mibBuilder.loadTexts:
    uas7616Recent24HrEntry.setStatus("mandatory")
_Uas7616Recent24HrIndex_Type = SCinstance
_Uas7616Recent24HrIndex_Object = MibTableColumn
uas7616Recent24HrIndex = _Uas7616Recent24HrIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 11, 1, 1),
    _Uas7616Recent24HrIndex_Type()
)
uas7616Recent24HrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7616Recent24HrIndex.setStatus("mandatory")


class _Uas7616Recent24HrStat_Type(OctetString):
    """Custom type uas7616Recent24HrStat based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(14, 14),
    )


_Uas7616Recent24HrStat_Type.__name__ = "OctetString"
_Uas7616Recent24HrStat_Object = MibTableColumn
uas7616Recent24HrStat = _Uas7616Recent24HrStat_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 11, 1, 2),
    _Uas7616Recent24HrStat_Type()
)
uas7616Recent24HrStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7616Recent24HrStat.setStatus("mandatory")
_Uas7616UnavailableTimeRegTable_Object = MibTable
uas7616UnavailableTimeRegTable = _Uas7616UnavailableTimeRegTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 12)
)
if mibBuilder.loadTexts:
    uas7616UnavailableTimeRegTable.setStatus("mandatory")
_Uas7616UnavailableTimeRegEntry_Object = MibTableRow
uas7616UnavailableTimeRegEntry = _Uas7616UnavailableTimeRegEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 12, 1)
)
uas7616UnavailableTimeRegEntry.setIndexNames(
    (0, "GDC7616-MIB", "uas7616UnavailableTimeRegIndex"),
    (0, "GDC7616-MIB", "uas7616UnavailableTimeRegNumber"),
)
if mibBuilder.loadTexts:
    uas7616UnavailableTimeRegEntry.setStatus("mandatory")
_Uas7616UnavailableTimeRegIndex_Type = SCinstance
_Uas7616UnavailableTimeRegIndex_Object = MibTableColumn
uas7616UnavailableTimeRegIndex = _Uas7616UnavailableTimeRegIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 12, 1, 1),
    _Uas7616UnavailableTimeRegIndex_Type()
)
uas7616UnavailableTimeRegIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7616UnavailableTimeRegIndex.setStatus("mandatory")


class _Uas7616UnavailableTimeRegNumber_Type(Integer32):
    """Custom type uas7616UnavailableTimeRegNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Uas7616UnavailableTimeRegNumber_Type.__name__ = "Integer32"
_Uas7616UnavailableTimeRegNumber_Object = MibTableColumn
uas7616UnavailableTimeRegNumber = _Uas7616UnavailableTimeRegNumber_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 12, 1, 2),
    _Uas7616UnavailableTimeRegNumber_Type()
)
uas7616UnavailableTimeRegNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7616UnavailableTimeRegNumber.setStatus("mandatory")


class _Uas7616UnavailableTimeRegStart_Type(Integer32):
    """Custom type uas7616UnavailableTimeRegStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Uas7616UnavailableTimeRegStart_Type.__name__ = "Integer32"
_Uas7616UnavailableTimeRegStart_Object = MibTableColumn
uas7616UnavailableTimeRegStart = _Uas7616UnavailableTimeRegStart_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 12, 1, 3),
    _Uas7616UnavailableTimeRegStart_Type()
)
uas7616UnavailableTimeRegStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7616UnavailableTimeRegStart.setStatus("mandatory")


class _Uas7616UnavailableTimeRegStop_Type(Integer32):
    """Custom type uas7616UnavailableTimeRegStop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Uas7616UnavailableTimeRegStop_Type.__name__ = "Integer32"
_Uas7616UnavailableTimeRegStop_Object = MibTableColumn
uas7616UnavailableTimeRegStop = _Uas7616UnavailableTimeRegStop_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 12, 1, 4),
    _Uas7616UnavailableTimeRegStop_Type()
)
uas7616UnavailableTimeRegStop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7616UnavailableTimeRegStop.setStatus("mandatory")
_Uas7616IntervalMaintenanceTable_Object = MibTable
uas7616IntervalMaintenanceTable = _Uas7616IntervalMaintenanceTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 13)
)
if mibBuilder.loadTexts:
    uas7616IntervalMaintenanceTable.setStatus("mandatory")
_Uas7616IntervalMaintenanceEntry_Object = MibTableRow
uas7616IntervalMaintenanceEntry = _Uas7616IntervalMaintenanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 13, 1)
)
uas7616IntervalMaintenanceEntry.setIndexNames(
    (0, "GDC7616-MIB", "uas7616IntervalMaintenanceIndex"),
)
if mibBuilder.loadTexts:
    uas7616IntervalMaintenanceEntry.setStatus("mandatory")
_Uas7616IntervalMaintenanceIndex_Type = SCinstance
_Uas7616IntervalMaintenanceIndex_Object = MibTableColumn
uas7616IntervalMaintenanceIndex = _Uas7616IntervalMaintenanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 13, 1, 1),
    _Uas7616IntervalMaintenanceIndex_Type()
)
uas7616IntervalMaintenanceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7616IntervalMaintenanceIndex.setStatus("mandatory")


class _Uas7616NumberofValidIntervals_Type(Integer32):
    """Custom type uas7616NumberofValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Uas7616NumberofValidIntervals_Type.__name__ = "Integer32"
_Uas7616NumberofValidIntervals_Object = MibTableColumn
uas7616NumberofValidIntervals = _Uas7616NumberofValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 13, 1, 2),
    _Uas7616NumberofValidIntervals_Type()
)
uas7616NumberofValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7616NumberofValidIntervals.setStatus("mandatory")
_Uas7616LocalAlarmConfigTable_Object = MibTable
uas7616LocalAlarmConfigTable = _Uas7616LocalAlarmConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 14)
)
if mibBuilder.loadTexts:
    uas7616LocalAlarmConfigTable.setStatus("mandatory")
_Uas7616LocalAlarmConfigEntry_Object = MibTableRow
uas7616LocalAlarmConfigEntry = _Uas7616LocalAlarmConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 14, 1)
)
uas7616LocalAlarmConfigEntry.setIndexNames(
    (0, "GDC7616-MIB", "uas7616LocalAlarmConfigIndex"),
)
if mibBuilder.loadTexts:
    uas7616LocalAlarmConfigEntry.setStatus("mandatory")
_Uas7616LocalAlarmConfigIndex_Type = SCinstance
_Uas7616LocalAlarmConfigIndex_Object = MibTableColumn
uas7616LocalAlarmConfigIndex = _Uas7616LocalAlarmConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 14, 1, 1),
    _Uas7616LocalAlarmConfigIndex_Type()
)
uas7616LocalAlarmConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7616LocalAlarmConfigIndex.setStatus("mandatory")


class _Uas7616LocalLossOfClock_Type(Integer32):
    """Custom type uas7616LocalLossOfClock based on Integer32"""
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
          ("enabledMajor", 2),
          ("enabledMinor", 3))
    )


_Uas7616LocalLossOfClock_Type.__name__ = "Integer32"
_Uas7616LocalLossOfClock_Object = MibTableColumn
uas7616LocalLossOfClock = _Uas7616LocalLossOfClock_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 14, 1, 2),
    _Uas7616LocalLossOfClock_Type()
)
uas7616LocalLossOfClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7616LocalLossOfClock.setStatus("mandatory")


class _Uas7616LocalUAS_Type(Integer32):
    """Custom type uas7616LocalUAS based on Integer32"""
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
          ("enabledMajor", 2),
          ("enabledMinor", 3))
    )


_Uas7616LocalUAS_Type.__name__ = "Integer32"
_Uas7616LocalUAS_Object = MibTableColumn
uas7616LocalUAS = _Uas7616LocalUAS_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 14, 1, 3),
    _Uas7616LocalUAS_Type()
)
uas7616LocalUAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7616LocalUAS.setStatus("mandatory")


class _Uas7616LocalSES_Type(Integer32):
    """Custom type uas7616LocalSES based on Integer32"""
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
          ("enabledMajor", 2),
          ("enabledMinor", 3))
    )


_Uas7616LocalSES_Type.__name__ = "Integer32"
_Uas7616LocalSES_Object = MibTableColumn
uas7616LocalSES = _Uas7616LocalSES_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 14, 1, 4),
    _Uas7616LocalSES_Type()
)
uas7616LocalSES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7616LocalSES.setStatus("mandatory")


class _Uas7616LocalES_Type(Integer32):
    """Custom type uas7616LocalES based on Integer32"""
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
          ("enabledMajor", 2),
          ("enabledMinor", 3))
    )


_Uas7616LocalES_Type.__name__ = "Integer32"
_Uas7616LocalES_Object = MibTableColumn
uas7616LocalES = _Uas7616LocalES_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 14, 1, 5),
    _Uas7616LocalES_Type()
)
uas7616LocalES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7616LocalES.setStatus("mandatory")


class _Uas7616LocalOutOfSync_Type(Integer32):
    """Custom type uas7616LocalOutOfSync based on Integer32"""
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
          ("enabledMajor", 2),
          ("enabledMinor", 3))
    )


_Uas7616LocalOutOfSync_Type.__name__ = "Integer32"
_Uas7616LocalOutOfSync_Object = MibTableColumn
uas7616LocalOutOfSync = _Uas7616LocalOutOfSync_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 14, 1, 6),
    _Uas7616LocalOutOfSync_Type()
)
uas7616LocalOutOfSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7616LocalOutOfSync.setStatus("mandatory")


class _Uas7616LocalNoSealingCurrent_Type(Integer32):
    """Custom type uas7616LocalNoSealingCurrent based on Integer32"""
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
          ("enabledMajor", 2),
          ("enabledMinor", 3))
    )


_Uas7616LocalNoSealingCurrent_Type.__name__ = "Integer32"
_Uas7616LocalNoSealingCurrent_Object = MibTableColumn
uas7616LocalNoSealingCurrent = _Uas7616LocalNoSealingCurrent_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 14, 1, 7),
    _Uas7616LocalNoSealingCurrent_Type()
)
uas7616LocalNoSealingCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7616LocalNoSealingCurrent.setStatus("mandatory")


class _Uas7616LPMajor_Type(Integer32):
    """Custom type uas7616LPMajor based on Integer32"""
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
          ("enabledMajor", 2),
          ("enabledMinor", 3))
    )


_Uas7616LPMajor_Type.__name__ = "Integer32"
_Uas7616LPMajor_Object = MibTableColumn
uas7616LPMajor = _Uas7616LPMajor_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 14, 1, 8),
    _Uas7616LPMajor_Type()
)
uas7616LPMajor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7616LPMajor.setStatus("mandatory")


class _Uas7616LPMinor_Type(Integer32):
    """Custom type uas7616LPMinor based on Integer32"""
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
          ("enabledMajor", 2),
          ("enabledMinor", 3))
    )


_Uas7616LPMinor_Type.__name__ = "Integer32"
_Uas7616LPMinor_Object = MibTableColumn
uas7616LPMinor = _Uas7616LPMinor_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 14, 1, 9),
    _Uas7616LPMinor_Type()
)
uas7616LPMinor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7616LPMinor.setStatus("mandatory")
_Uas7616TSAssignTable_Object = MibTable
uas7616TSAssignTable = _Uas7616TSAssignTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 15)
)
if mibBuilder.loadTexts:
    uas7616TSAssignTable.setStatus("mandatory")
_Uas7616TSAssignEntry_Object = MibTableRow
uas7616TSAssignEntry = _Uas7616TSAssignEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 15, 1)
)
uas7616TSAssignEntry.setIndexNames(
    (0, "GDC7616-MIB", "uas7616TSAssignIndex"),
    (0, "GDC7616-MIB", "uas7616ChannelIndex"),
)
if mibBuilder.loadTexts:
    uas7616TSAssignEntry.setStatus("mandatory")
_Uas7616TSAssignIndex_Type = SCinstance
_Uas7616TSAssignIndex_Object = MibTableColumn
uas7616TSAssignIndex = _Uas7616TSAssignIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 15, 1, 1),
    _Uas7616TSAssignIndex_Type()
)
uas7616TSAssignIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7616TSAssignIndex.setStatus("mandatory")


class _Uas7616ChannelIndex_Type(Integer32):
    """Custom type uas7616ChannelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("channelA", 1),
          ("channelB", 2))
    )


_Uas7616ChannelIndex_Type.__name__ = "Integer32"
_Uas7616ChannelIndex_Object = MibTableColumn
uas7616ChannelIndex = _Uas7616ChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 15, 1, 2),
    _Uas7616ChannelIndex_Type()
)
uas7616ChannelIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7616ChannelIndex.setStatus("mandatory")


class _Uas7616Highway_Type(Integer32):
    """Custom type uas7616Highway based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("highway1", 2),
          ("highway2", 3),
          ("highway3", 4),
          ("highway4", 5),
          ("notAssigned", 1))
    )


_Uas7616Highway_Type.__name__ = "Integer32"
_Uas7616Highway_Object = MibTableColumn
uas7616Highway = _Uas7616Highway_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 15, 1, 3),
    _Uas7616Highway_Type()
)
uas7616Highway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7616Highway.setStatus("mandatory")


class _Uas7616TimeSlot_Type(Integer32):
    """Custom type uas7616TimeSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Uas7616TimeSlot_Type.__name__ = "Integer32"
_Uas7616TimeSlot_Object = MibTableColumn
uas7616TimeSlot = _Uas7616TimeSlot_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 15, 1, 4),
    _Uas7616TimeSlot_Type()
)
uas7616TimeSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7616TimeSlot.setStatus("mandatory")


class _Uas7616TSCircuitID_Type(DisplayString):
    """Custom type uas7616TSCircuitID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_Uas7616TSCircuitID_Type.__name__ = "DisplayString"
_Uas7616TSCircuitID_Object = MibTableColumn
uas7616TSCircuitID = _Uas7616TSCircuitID_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 4, 15, 1, 5),
    _Uas7616TSCircuitID_Type()
)
uas7616TSCircuitID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7616TSCircuitID.setStatus("mandatory")
_Uas7616Alarm_ObjectIdentity = ObjectIdentity
uas7616Alarm = _Uas7616Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 13)
)
_Uas7616AlarmData_ObjectIdentity = ObjectIdentity
uas7616AlarmData = _Uas7616AlarmData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 13, 1)
)
_Uas7616NoResponseAlm_ObjectIdentity = ObjectIdentity
uas7616NoResponseAlm = _Uas7616NoResponseAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 13, 1, 1)
)
_Uas7616DiagRxErrAlm_ObjectIdentity = ObjectIdentity
uas7616DiagRxErrAlm = _Uas7616DiagRxErrAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 13, 1, 2)
)
_Uas7616PowerUpAlm_ObjectIdentity = ObjectIdentity
uas7616PowerUpAlm = _Uas7616PowerUpAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 13, 1, 3)
)
_Uas7616LossOfClockAlm_ObjectIdentity = ObjectIdentity
uas7616LossOfClockAlm = _Uas7616LossOfClockAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 13, 1, 4)
)
_Uas7616LpOutofSyncAlm_ObjectIdentity = ObjectIdentity
uas7616LpOutofSyncAlm = _Uas7616LpOutofSyncAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 13, 1, 5)
)
_Uas7616LpSealingCurrentNoContinuityAlm_ObjectIdentity = ObjectIdentity
uas7616LpSealingCurrentNoContinuityAlm = _Uas7616LpSealingCurrentNoContinuityAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 13, 1, 6)
)
_Uas7616LpUnavailableSecondAlm_ObjectIdentity = ObjectIdentity
uas7616LpUnavailableSecondAlm = _Uas7616LpUnavailableSecondAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 13, 1, 7)
)
_Uas7616LpSeverelyErroredSecondAlm_ObjectIdentity = ObjectIdentity
uas7616LpSeverelyErroredSecondAlm = _Uas7616LpSeverelyErroredSecondAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 13, 1, 8)
)
_Uas7616LpErroredSecondAlm_ObjectIdentity = ObjectIdentity
uas7616LpErroredSecondAlm = _Uas7616LpErroredSecondAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 13, 1, 9)
)
_Uas7616AlarmConfigTable_Object = MibTable
uas7616AlarmConfigTable = _Uas7616AlarmConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 13, 2)
)
if mibBuilder.loadTexts:
    uas7616AlarmConfigTable.setStatus("mandatory")
_Uas7616AlarmConfigEntry_Object = MibTableRow
uas7616AlarmConfigEntry = _Uas7616AlarmConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 13, 2, 1)
)
uas7616AlarmConfigEntry.setIndexNames(
    (0, "GDC7616-MIB", "uas7616AlarmConfigIndex"),
    (0, "GDC7616-MIB", "uas7616AlarmConfigIdentifier"),
)
if mibBuilder.loadTexts:
    uas7616AlarmConfigEntry.setStatus("mandatory")
_Uas7616AlarmConfigIndex_Type = SCinstance
_Uas7616AlarmConfigIndex_Object = MibTableColumn
uas7616AlarmConfigIndex = _Uas7616AlarmConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 13, 2, 1, 1),
    _Uas7616AlarmConfigIndex_Type()
)
uas7616AlarmConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7616AlarmConfigIndex.setStatus("mandatory")
_Uas7616AlarmConfigIdentifier_Type = ObjectIdentifier
_Uas7616AlarmConfigIdentifier_Object = MibTableColumn
uas7616AlarmConfigIdentifier = _Uas7616AlarmConfigIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 13, 2, 1, 2),
    _Uas7616AlarmConfigIdentifier_Type()
)
uas7616AlarmConfigIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7616AlarmConfigIdentifier.setStatus("mandatory")


class _Uas7616AlarmCountWindow_Type(Integer32):
    """Custom type uas7616AlarmCountWindow based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("infinite", 9),
          ("last10secs", 3),
          ("last15min", 6),
          ("last1hr", 7),
          ("last1min", 5),
          ("last1sec", 2),
          ("last24hrs", 8),
          ("last30secs", 4))
    )


_Uas7616AlarmCountWindow_Type.__name__ = "Integer32"
_Uas7616AlarmCountWindow_Object = MibTableColumn
uas7616AlarmCountWindow = _Uas7616AlarmCountWindow_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 13, 2, 1, 3),
    _Uas7616AlarmCountWindow_Type()
)
uas7616AlarmCountWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7616AlarmCountWindow.setStatus("mandatory")


class _Uas7616AlarmCountThreshold_Type(Integer32):
    """Custom type uas7616AlarmCountThreshold based on Integer32"""
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
        *(("occurrence100x", 4),
          ("occurrence10Kx", 6),
          ("occurrence10x", 3),
          ("occurrence1Kx", 5),
          ("occurrence1x", 1),
          ("occurrence3x", 2))
    )


_Uas7616AlarmCountThreshold_Type.__name__ = "Integer32"
_Uas7616AlarmCountThreshold_Object = MibTableColumn
uas7616AlarmCountThreshold = _Uas7616AlarmCountThreshold_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 13, 2, 1, 4),
    _Uas7616AlarmCountThreshold_Type()
)
uas7616AlarmCountThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7616AlarmCountThreshold.setStatus("mandatory")
_Uas7616mAlarm_ObjectIdentity = ObjectIdentity
uas7616mAlarm = _Uas7616mAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 14)
)
_Uas7616mAlarmData_ObjectIdentity = ObjectIdentity
uas7616mAlarmData = _Uas7616mAlarmData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 14, 1)
)
_Uas7616mNoResponseAlm_ObjectIdentity = ObjectIdentity
uas7616mNoResponseAlm = _Uas7616mNoResponseAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 14, 1, 1)
)
_Uas7616mDiagRxErrAlm_ObjectIdentity = ObjectIdentity
uas7616mDiagRxErrAlm = _Uas7616mDiagRxErrAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 14, 1, 2)
)
_Uas7616mPowerUpAlm_ObjectIdentity = ObjectIdentity
uas7616mPowerUpAlm = _Uas7616mPowerUpAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 14, 1, 3)
)
_Uas7616mLossOfClockAlm_ObjectIdentity = ObjectIdentity
uas7616mLossOfClockAlm = _Uas7616mLossOfClockAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 14, 1, 4)
)
_Uas7616mLpOutofSyncAlm_ObjectIdentity = ObjectIdentity
uas7616mLpOutofSyncAlm = _Uas7616mLpOutofSyncAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 14, 1, 5)
)
_Uas7616mLpSealingCurrentNoContinuityAlm_ObjectIdentity = ObjectIdentity
uas7616mLpSealingCurrentNoContinuityAlm = _Uas7616mLpSealingCurrentNoContinuityAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 14, 1, 6)
)
_Uas7616mLpUnavailableSecondAlm_ObjectIdentity = ObjectIdentity
uas7616mLpUnavailableSecondAlm = _Uas7616mLpUnavailableSecondAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 14, 1, 7)
)
_Uas7616mLpErroredSecondAlm_ObjectIdentity = ObjectIdentity
uas7616mLpErroredSecondAlm = _Uas7616mLpErroredSecondAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 14, 1, 8)
)
_Uas7616mLPMajorAlm_ObjectIdentity = ObjectIdentity
uas7616mLPMajorAlm = _Uas7616mLPMajorAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 14, 1, 9)
)
_Uas7616mLPMinorAlm_ObjectIdentity = ObjectIdentity
uas7616mLPMinorAlm = _Uas7616mLPMinorAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 12, 14, 1, 10)
)
_Uas7616mAlarmConfigTable_Object = MibTable
uas7616mAlarmConfigTable = _Uas7616mAlarmConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 14, 2)
)
if mibBuilder.loadTexts:
    uas7616mAlarmConfigTable.setStatus("mandatory")
_Uas7616mAlarmConfigEntry_Object = MibTableRow
uas7616mAlarmConfigEntry = _Uas7616mAlarmConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 14, 2, 1)
)
uas7616mAlarmConfigEntry.setIndexNames(
    (0, "GDC7616-MIB", "uas7616mAlarmConfigIndex"),
    (0, "GDC7616-MIB", "uas7616mAlarmConfigIdentifier"),
)
if mibBuilder.loadTexts:
    uas7616mAlarmConfigEntry.setStatus("mandatory")
_Uas7616mAlarmConfigIndex_Type = SCinstance
_Uas7616mAlarmConfigIndex_Object = MibTableColumn
uas7616mAlarmConfigIndex = _Uas7616mAlarmConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 14, 2, 1, 1),
    _Uas7616mAlarmConfigIndex_Type()
)
uas7616mAlarmConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7616mAlarmConfigIndex.setStatus("mandatory")
_Uas7616mAlarmConfigIdentifier_Type = ObjectIdentifier
_Uas7616mAlarmConfigIdentifier_Object = MibTableColumn
uas7616mAlarmConfigIdentifier = _Uas7616mAlarmConfigIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 14, 2, 1, 2),
    _Uas7616mAlarmConfigIdentifier_Type()
)
uas7616mAlarmConfigIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uas7616mAlarmConfigIdentifier.setStatus("mandatory")


class _Uas7616mAlarmCountThreshold_Type(Integer32):
    """Custom type uas7616mAlarmCountThreshold based on Integer32"""
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


_Uas7616mAlarmCountThreshold_Type.__name__ = "Integer32"
_Uas7616mAlarmCountThreshold_Object = MibTableColumn
uas7616mAlarmCountThreshold = _Uas7616mAlarmCountThreshold_Object(
    (1, 3, 6, 1, 4, 1, 498, 12, 14, 2, 1, 3),
    _Uas7616mAlarmCountThreshold_Type()
)
uas7616mAlarmCountThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uas7616mAlarmCountThreshold.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GDC7616-MIB",
    **{"gdc": gdc,
       "bql2": bql2,
       "uas7616": uas7616,
       "uas7616MIBVersion": uas7616MIBVersion,
       "uas7616WhatAreYouTable": uas7616WhatAreYouTable,
       "uas7616WhatAreYouEntry": uas7616WhatAreYouEntry,
       "uas7616WhatAreYouIndex": uas7616WhatAreYouIndex,
       "uas7616CodeRev": uas7616CodeRev,
       "uas7616AlarmStatus": uas7616AlarmStatus,
       "uas7616SystemTimingGenStatus": uas7616SystemTimingGenStatus,
       "uas7616ConfigTable": uas7616ConfigTable,
       "uas7616ConfigEntry": uas7616ConfigEntry,
       "uas7616ConfigIndex": uas7616ConfigIndex,
       "uas7616TXClockSource": uas7616TXClockSource,
       "uas7616TerminationType": uas7616TerminationType,
       "uas7616ChADataRate": uas7616ChADataRate,
       "uas7616ChBDataRate": uas7616ChBDataRate,
       "uas7616ControlTable": uas7616ControlTable,
       "uas7616ControlEntry": uas7616ControlEntry,
       "uas7616ControlIndex": uas7616ControlIndex,
       "uas7616SoftReset": uas7616SoftReset,
       "uas7616EraseConfig": uas7616EraseConfig,
       "uas7616LEDStatus": uas7616LEDStatus,
       "uas7616InterfaceType": uas7616InterfaceType,
       "uas7616SysTimingGen": uas7616SysTimingGen,
       "uas7616ResetIntervals": uas7616ResetIntervals,
       "uas7616SysUpTime": uas7616SysUpTime,
       "uas7616SetRealTime": uas7616SetRealTime,
       "uas7616ModuleClkSrc": uas7616ModuleClkSrc,
       "uas7616ResetMajorAlarm": uas7616ResetMajorAlarm,
       "uas7616ResetMinorAlarm": uas7616ResetMinorAlarm,
       "uas7616DiagnosticTable": uas7616DiagnosticTable,
       "uas7616DiagnosticEntry": uas7616DiagnosticEntry,
       "uas7616DiagnosticIndex": uas7616DiagnosticIndex,
       "uas7616DiagnosticChnlIndex": uas7616DiagnosticChnlIndex,
       "uas7616DiagnosticTest": uas7616DiagnosticTest,
       "uas7616DiagnosticResetErrorCount": uas7616DiagnosticResetErrorCount,
       "uas7616DiagnosticResults": uas7616DiagnosticResults,
       "uas7616Current15MinTable": uas7616Current15MinTable,
       "uas7616Current15MinEntry": uas7616Current15MinEntry,
       "uas7616Current15MinIndex": uas7616Current15MinIndex,
       "uas7616Current15MinStat": uas7616Current15MinStat,
       "uas7616IntervalTable": uas7616IntervalTable,
       "uas7616IntervalEntry": uas7616IntervalEntry,
       "uas7616IntervalIndex": uas7616IntervalIndex,
       "uas7616IntervalNumber": uas7616IntervalNumber,
       "uas7616IntervalStat": uas7616IntervalStat,
       "uas7616Current24HrTable": uas7616Current24HrTable,
       "uas7616Current24HrEntry": uas7616Current24HrEntry,
       "uas7616Current24HrIndex": uas7616Current24HrIndex,
       "uas7616Current24HrStat": uas7616Current24HrStat,
       "uas7616Recent24HrTable": uas7616Recent24HrTable,
       "uas7616Recent24HrEntry": uas7616Recent24HrEntry,
       "uas7616Recent24HrIndex": uas7616Recent24HrIndex,
       "uas7616Recent24HrStat": uas7616Recent24HrStat,
       "uas7616UnavailableTimeRegTable": uas7616UnavailableTimeRegTable,
       "uas7616UnavailableTimeRegEntry": uas7616UnavailableTimeRegEntry,
       "uas7616UnavailableTimeRegIndex": uas7616UnavailableTimeRegIndex,
       "uas7616UnavailableTimeRegNumber": uas7616UnavailableTimeRegNumber,
       "uas7616UnavailableTimeRegStart": uas7616UnavailableTimeRegStart,
       "uas7616UnavailableTimeRegStop": uas7616UnavailableTimeRegStop,
       "uas7616IntervalMaintenanceTable": uas7616IntervalMaintenanceTable,
       "uas7616IntervalMaintenanceEntry": uas7616IntervalMaintenanceEntry,
       "uas7616IntervalMaintenanceIndex": uas7616IntervalMaintenanceIndex,
       "uas7616NumberofValidIntervals": uas7616NumberofValidIntervals,
       "uas7616LocalAlarmConfigTable": uas7616LocalAlarmConfigTable,
       "uas7616LocalAlarmConfigEntry": uas7616LocalAlarmConfigEntry,
       "uas7616LocalAlarmConfigIndex": uas7616LocalAlarmConfigIndex,
       "uas7616LocalLossOfClock": uas7616LocalLossOfClock,
       "uas7616LocalUAS": uas7616LocalUAS,
       "uas7616LocalSES": uas7616LocalSES,
       "uas7616LocalES": uas7616LocalES,
       "uas7616LocalOutOfSync": uas7616LocalOutOfSync,
       "uas7616LocalNoSealingCurrent": uas7616LocalNoSealingCurrent,
       "uas7616LPMajor": uas7616LPMajor,
       "uas7616LPMinor": uas7616LPMinor,
       "uas7616TSAssignTable": uas7616TSAssignTable,
       "uas7616TSAssignEntry": uas7616TSAssignEntry,
       "uas7616TSAssignIndex": uas7616TSAssignIndex,
       "uas7616ChannelIndex": uas7616ChannelIndex,
       "uas7616Highway": uas7616Highway,
       "uas7616TimeSlot": uas7616TimeSlot,
       "uas7616TSCircuitID": uas7616TSCircuitID,
       "uas7616Alarm": uas7616Alarm,
       "uas7616AlarmData": uas7616AlarmData,
       "uas7616NoResponseAlm": uas7616NoResponseAlm,
       "uas7616DiagRxErrAlm": uas7616DiagRxErrAlm,
       "uas7616PowerUpAlm": uas7616PowerUpAlm,
       "uas7616LossOfClockAlm": uas7616LossOfClockAlm,
       "uas7616LpOutofSyncAlm": uas7616LpOutofSyncAlm,
       "uas7616LpSealingCurrentNoContinuityAlm": uas7616LpSealingCurrentNoContinuityAlm,
       "uas7616LpUnavailableSecondAlm": uas7616LpUnavailableSecondAlm,
       "uas7616LpSeverelyErroredSecondAlm": uas7616LpSeverelyErroredSecondAlm,
       "uas7616LpErroredSecondAlm": uas7616LpErroredSecondAlm,
       "uas7616AlarmConfigTable": uas7616AlarmConfigTable,
       "uas7616AlarmConfigEntry": uas7616AlarmConfigEntry,
       "uas7616AlarmConfigIndex": uas7616AlarmConfigIndex,
       "uas7616AlarmConfigIdentifier": uas7616AlarmConfigIdentifier,
       "uas7616AlarmCountWindow": uas7616AlarmCountWindow,
       "uas7616AlarmCountThreshold": uas7616AlarmCountThreshold,
       "uas7616mAlarm": uas7616mAlarm,
       "uas7616mAlarmData": uas7616mAlarmData,
       "uas7616mNoResponseAlm": uas7616mNoResponseAlm,
       "uas7616mDiagRxErrAlm": uas7616mDiagRxErrAlm,
       "uas7616mPowerUpAlm": uas7616mPowerUpAlm,
       "uas7616mLossOfClockAlm": uas7616mLossOfClockAlm,
       "uas7616mLpOutofSyncAlm": uas7616mLpOutofSyncAlm,
       "uas7616mLpSealingCurrentNoContinuityAlm": uas7616mLpSealingCurrentNoContinuityAlm,
       "uas7616mLpUnavailableSecondAlm": uas7616mLpUnavailableSecondAlm,
       "uas7616mLpErroredSecondAlm": uas7616mLpErroredSecondAlm,
       "uas7616mLPMajorAlm": uas7616mLPMajorAlm,
       "uas7616mLPMinorAlm": uas7616mLPMinorAlm,
       "uas7616mAlarmConfigTable": uas7616mAlarmConfigTable,
       "uas7616mAlarmConfigEntry": uas7616mAlarmConfigEntry,
       "uas7616mAlarmConfigIndex": uas7616mAlarmConfigIndex,
       "uas7616mAlarmConfigIdentifier": uas7616mAlarmConfigIdentifier,
       "uas7616mAlarmCountThreshold": uas7616mAlarmCountThreshold}
)
