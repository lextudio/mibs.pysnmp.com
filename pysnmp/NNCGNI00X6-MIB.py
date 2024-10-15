# SNMP MIB module (NNCGNI00X6-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NNCGNI00X6-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:28:28 2024
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

(nncExtCodeSpace,
 nncExtDiag,
 nncExtEnvironmental,
 nncExtNVM,
 nncExtProbe,
 nncExtRestart,
 nncExtSystem) = mibBuilder.importSymbols(
    "NNCGNI00X1-SMI",
    "nncExtCodeSpace",
    "nncExtDiag",
    "nncExtEnvironmental",
    "nncExtNVM",
    "nncExtProbe",
    "nncExtRestart",
    "nncExtSystem")

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



class RestartCause(Integer32):
    """Custom type RestartCause based on Integer32"""
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
              15,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72)
        )
    )
    namedValues = NamedValues(
        *(("trbl-addresserror", 3),
          ("trbl-badflashconfig", 55),
          ("trbl-buserror", 2),
          ("trbl-chkfailure", 6),
          ("trbl-copyramtoflash", 53),
          ("trbl-cpureset", 71),
          ("trbl-dcmpdeath", 62),
          ("trbl-dnldaborted", 54),
          ("trbl-dspdead", 61),
          ("trbl-dspdiedontx", 60),
          ("trbl-dspdnldfailed", 58),
          ("trbl-dsppollfailed", 59),
          ("trbl-dspreset", 57),
          ("trbl-illegalinst", 4),
          ("trbl-intlevel-1", 25),
          ("trbl-intlevel-2", 26),
          ("trbl-intlevel-3", 27),
          ("trbl-intlevel-4", 28),
          ("trbl-intlevel-5", 29),
          ("trbl-intlevel-6", 30),
          ("trbl-intlevel-7", 31),
          ("trbl-line1010", 10),
          ("trbl-line1111", 11),
          ("trbl-ncireload", 69),
          ("trbl-ncireset", 49),
          ("trbl-ncirunminusone", 50),
          ("trbl-noproblem", 0),
          ("trbl-nvmreset", 56),
          ("trbl-panic", 51),
          ("trbl-privilege", 8),
          ("trbl-pushbutton", 70),
          ("trbl-rdsreset", 72),
          ("trbl-runbootprom", 52),
          ("trbl-runninglowcomms", 63),
          ("trbl-runninglowframe", 64),
          ("trbl-runninglowmgmt", 67),
          ("trbl-runninglowpoolunknown", 68),
          ("trbl-runninglowsonic", 66),
          ("trbl-runninglowsys", 65),
          ("trbl-spurious", 24),
          ("trbl-tracetrap", 9),
          ("trbl-trap-00", 32),
          ("trbl-trap-01", 33),
          ("trbl-trap-02", 34),
          ("trbl-trap-03", 35),
          ("trbl-trap-04", 36),
          ("trbl-trap-05", 37),
          ("trbl-trap-06", 38),
          ("trbl-trap-07", 39),
          ("trbl-trap-08", 40),
          ("trbl-trap-09", 41),
          ("trbl-trap-10", 42),
          ("trbl-trap-11", 43),
          ("trbl-trap-12", 44),
          ("trbl-trap-13", 45),
          ("trbl-trap-14", 46),
          ("trbl-trap-15", 47),
          ("trbl-trapvinst", 7),
          ("trbl-uninitialized", 15),
          ("trbl-unknown", 1),
          ("trbl-watchdog", 48),
          ("trbl-zerodivide", 5))
    )





class CodeSpaceIndex(Integer32):
    """Custom type CodeSpaceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )





class NVMPoolIndex(Integer32):
    """Custom type NVMPoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _NncExtSysProductName_Type(DisplayString):
    """Custom type nncExtSysProductName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_NncExtSysProductName_Type.__name__ = "DisplayString"
_NncExtSysProductName_Object = MibScalar
nncExtSysProductName = _NncExtSysProductName_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 1, 1),
    _NncExtSysProductName_Type()
)
nncExtSysProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSysProductName.setStatus("mandatory")


class _NncExtSysCurrentGeneric_Type(DisplayString):
    """Custom type nncExtSysCurrentGeneric based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_NncExtSysCurrentGeneric_Type.__name__ = "DisplayString"
_NncExtSysCurrentGeneric_Object = MibScalar
nncExtSysCurrentGeneric = _NncExtSysCurrentGeneric_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 1, 2),
    _NncExtSysCurrentGeneric_Type()
)
nncExtSysCurrentGeneric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtSysCurrentGeneric.setStatus("mandatory")


class _NncExtEnvFanStatus_Type(Integer32):
    """Custom type nncExtEnvFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fanFailed", 2),
          ("fanOk", 1))
    )


_NncExtEnvFanStatus_Type.__name__ = "Integer32"
_NncExtEnvFanStatus_Object = MibScalar
nncExtEnvFanStatus = _NncExtEnvFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 2, 1),
    _NncExtEnvFanStatus_Type()
)
nncExtEnvFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtEnvFanStatus.setStatus("mandatory")


class _NncExtEnvTemperatureSensor_Type(Integer32):
    """Custom type nncExtEnvTemperatureSensor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("tooHot", 2))
    )


_NncExtEnvTemperatureSensor_Type.__name__ = "Integer32"
_NncExtEnvTemperatureSensor_Object = MibScalar
nncExtEnvTemperatureSensor = _NncExtEnvTemperatureSensor_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 2, 2),
    _NncExtEnvTemperatureSensor_Type()
)
nncExtEnvTemperatureSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtEnvTemperatureSensor.setStatus("mandatory")


class _NncExtEnvPlus12Status_Type(Integer32):
    """Custom type nncExtEnvPlus12Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("outOfSpec", 2))
    )


_NncExtEnvPlus12Status_Type.__name__ = "Integer32"
_NncExtEnvPlus12Status_Object = MibScalar
nncExtEnvPlus12Status = _NncExtEnvPlus12Status_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 2, 3),
    _NncExtEnvPlus12Status_Type()
)
nncExtEnvPlus12Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtEnvPlus12Status.setStatus("mandatory")


class _NncExtEnvMinus12Status_Type(Integer32):
    """Custom type nncExtEnvMinus12Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("outOfSpec", 2))
    )


_NncExtEnvMinus12Status_Type.__name__ = "Integer32"
_NncExtEnvMinus12Status_Object = MibScalar
nncExtEnvMinus12Status = _NncExtEnvMinus12Status_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 2, 4),
    _NncExtEnvMinus12Status_Type()
)
nncExtEnvMinus12Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtEnvMinus12Status.setStatus("mandatory")
_NncExtRestarts_Type = Counter32
_NncExtRestarts_Object = MibScalar
nncExtRestarts = _NncExtRestarts_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 3, 1),
    _NncExtRestarts_Type()
)
nncExtRestarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtRestarts.setStatus("mandatory")
_NncExtFaultInducedRestarts_Type = Counter32
_NncExtFaultInducedRestarts_Object = MibScalar
nncExtFaultInducedRestarts = _NncExtFaultInducedRestarts_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 3, 2),
    _NncExtFaultInducedRestarts_Type()
)
nncExtFaultInducedRestarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtFaultInducedRestarts.setStatus("mandatory")


class _NncExtLastFault_Type(Integer32):
    """Custom type nncExtLastFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NncExtLastFault_Type.__name__ = "Integer32"
_NncExtLastFault_Object = MibScalar
nncExtLastFault = _NncExtLastFault_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 3, 3),
    _NncExtLastFault_Type()
)
nncExtLastFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtLastFault.setStatus("mandatory")
_NncExtFaultRepetitions_Type = Counter32
_NncExtFaultRepetitions_Object = MibScalar
nncExtFaultRepetitions = _NncExtFaultRepetitions_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 3, 4),
    _NncExtFaultRepetitions_Type()
)
nncExtFaultRepetitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtFaultRepetitions.setStatus("mandatory")
_NncExtRestartTracebackTable_Object = MibTable
nncExtRestartTracebackTable = _NncExtRestartTracebackTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 3, 5)
)
if mibBuilder.loadTexts:
    nncExtRestartTracebackTable.setStatus("mandatory")
_NncExtRestartTracebackEntry_Object = MibTableRow
nncExtRestartTracebackEntry = _NncExtRestartTracebackEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 3, 5, 1)
)
nncExtRestartTracebackEntry.setIndexNames(
    (0, "NNCGNI00X6-MIB", "nncExtRestartTracebackIndex"),
)
if mibBuilder.loadTexts:
    nncExtRestartTracebackEntry.setStatus("mandatory")


class _NncExtRestartTracebackIndex_Type(Integer32):
    """Custom type nncExtRestartTracebackIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NncExtRestartTracebackIndex_Type.__name__ = "Integer32"
_NncExtRestartTracebackIndex_Object = MibTableColumn
nncExtRestartTracebackIndex = _NncExtRestartTracebackIndex_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 3, 5, 1, 1),
    _NncExtRestartTracebackIndex_Type()
)
nncExtRestartTracebackIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtRestartTracebackIndex.setStatus("mandatory")


class _NncExtRestartTracebackPCValue_Type(Integer32):
    """Custom type nncExtRestartTracebackPCValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NncExtRestartTracebackPCValue_Type.__name__ = "Integer32"
_NncExtRestartTracebackPCValue_Object = MibTableColumn
nncExtRestartTracebackPCValue = _NncExtRestartTracebackPCValue_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 3, 5, 1, 2),
    _NncExtRestartTracebackPCValue_Type()
)
nncExtRestartTracebackPCValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtRestartTracebackPCValue.setStatus("mandatory")
_NncExtRestartRegisterTable_Object = MibTable
nncExtRestartRegisterTable = _NncExtRestartRegisterTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 3, 6)
)
if mibBuilder.loadTexts:
    nncExtRestartRegisterTable.setStatus("mandatory")
_NncExtRestartRegisterEntry_Object = MibTableRow
nncExtRestartRegisterEntry = _NncExtRestartRegisterEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 3, 6, 1)
)
nncExtRestartRegisterEntry.setIndexNames(
    (0, "NNCGNI00X6-MIB", "nncExtRestartRegisterIndex"),
)
if mibBuilder.loadTexts:
    nncExtRestartRegisterEntry.setStatus("mandatory")


class _NncExtRestartRegisterIndex_Type(Integer32):
    """Custom type nncExtRestartRegisterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NncExtRestartRegisterIndex_Type.__name__ = "Integer32"
_NncExtRestartRegisterIndex_Object = MibTableColumn
nncExtRestartRegisterIndex = _NncExtRestartRegisterIndex_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 3, 6, 1, 1),
    _NncExtRestartRegisterIndex_Type()
)
nncExtRestartRegisterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtRestartRegisterIndex.setStatus("mandatory")


class _NncExtRestartRegisterValue_Type(Integer32):
    """Custom type nncExtRestartRegisterValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NncExtRestartRegisterValue_Type.__name__ = "Integer32"
_NncExtRestartRegisterValue_Object = MibTableColumn
nncExtRestartRegisterValue = _NncExtRestartRegisterValue_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 3, 6, 1, 2),
    _NncExtRestartRegisterValue_Type()
)
nncExtRestartRegisterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtRestartRegisterValue.setStatus("mandatory")


class _NncExtRestartForceToBoot_Type(Integer32):
    """Custom type nncExtRestartForceToBoot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 36000),
    )


_NncExtRestartForceToBoot_Type.__name__ = "Integer32"
_NncExtRestartForceToBoot_Object = MibScalar
nncExtRestartForceToBoot = _NncExtRestartForceToBoot_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 3, 7),
    _NncExtRestartForceToBoot_Type()
)
nncExtRestartForceToBoot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nncExtRestartForceToBoot.setStatus("mandatory")


class _NncExtRestartCause_Type(Integer32):
    """Custom type nncExtRestartCause based on Integer32"""
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
              15,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72)
        )
    )
    namedValues = NamedValues(
        *(("trbl-addresserror", 3),
          ("trbl-badflashconfig", 55),
          ("trbl-buserror", 2),
          ("trbl-chkfailure", 6),
          ("trbl-copyramtoflash", 53),
          ("trbl-cpureset", 71),
          ("trbl-dcmpdeath", 62),
          ("trbl-dnldaborted", 54),
          ("trbl-dspdead", 61),
          ("trbl-dspdiedontx", 60),
          ("trbl-dspdnldfailed", 58),
          ("trbl-dsppollfailed", 59),
          ("trbl-dspreset", 57),
          ("trbl-illegalinst", 4),
          ("trbl-intlevel-1", 25),
          ("trbl-intlevel-2", 26),
          ("trbl-intlevel-3", 27),
          ("trbl-intlevel-4", 28),
          ("trbl-intlevel-5", 29),
          ("trbl-intlevel-6", 30),
          ("trbl-intlevel-7", 31),
          ("trbl-line1010", 10),
          ("trbl-line1111", 11),
          ("trbl-ncireload", 69),
          ("trbl-ncireset", 49),
          ("trbl-ncirunminusone", 50),
          ("trbl-noproblem", 0),
          ("trbl-nvmreset", 56),
          ("trbl-panic", 51),
          ("trbl-privilege", 8),
          ("trbl-pushbutton", 70),
          ("trbl-rdsreset", 72),
          ("trbl-runbootprom", 52),
          ("trbl-runninglowcomms", 63),
          ("trbl-runninglowframe", 64),
          ("trbl-runninglowmgmt", 67),
          ("trbl-runninglowpoolunknown", 68),
          ("trbl-runninglowsonic", 66),
          ("trbl-runninglowsys", 65),
          ("trbl-spurious", 24),
          ("trbl-tracetrap", 9),
          ("trbl-trap-00", 32),
          ("trbl-trap-01", 33),
          ("trbl-trap-02", 34),
          ("trbl-trap-03", 35),
          ("trbl-trap-04", 36),
          ("trbl-trap-05", 37),
          ("trbl-trap-06", 38),
          ("trbl-trap-07", 39),
          ("trbl-trap-08", 40),
          ("trbl-trap-09", 41),
          ("trbl-trap-10", 42),
          ("trbl-trap-11", 43),
          ("trbl-trap-12", 44),
          ("trbl-trap-13", 45),
          ("trbl-trap-14", 46),
          ("trbl-trap-15", 47),
          ("trbl-trapvinst", 7),
          ("trbl-uninitialized", 15),
          ("trbl-unknown", 1),
          ("trbl-watchdog", 48),
          ("trbl-zerodivide", 5))
    )


_NncExtRestartCause_Type.__name__ = "Integer32"
_NncExtRestartCause_Object = MibScalar
nncExtRestartCause = _NncExtRestartCause_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 3, 8),
    _NncExtRestartCause_Type()
)
nncExtRestartCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtRestartCause.setStatus("mandatory")
_NncExtCodeSpaceCurrentlyActive_Type = CodeSpaceIndex
_NncExtCodeSpaceCurrentlyActive_Object = MibScalar
nncExtCodeSpaceCurrentlyActive = _NncExtCodeSpaceCurrentlyActive_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 4, 1),
    _NncExtCodeSpaceCurrentlyActive_Type()
)
nncExtCodeSpaceCurrentlyActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtCodeSpaceCurrentlyActive.setStatus("mandatory")
_NncExtCodeSpaceNextActive_Type = CodeSpaceIndex
_NncExtCodeSpaceNextActive_Object = MibScalar
nncExtCodeSpaceNextActive = _NncExtCodeSpaceNextActive_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 4, 2),
    _NncExtCodeSpaceNextActive_Type()
)
nncExtCodeSpaceNextActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nncExtCodeSpaceNextActive.setStatus("mandatory")
_NncExtCodeSpaceNumber_Type = CodeSpaceIndex
_NncExtCodeSpaceNumber_Object = MibScalar
nncExtCodeSpaceNumber = _NncExtCodeSpaceNumber_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 4, 3),
    _NncExtCodeSpaceNumber_Type()
)
nncExtCodeSpaceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtCodeSpaceNumber.setStatus("mandatory")
_NncExtCodeSpaceTable_Object = MibTable
nncExtCodeSpaceTable = _NncExtCodeSpaceTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 4, 4)
)
if mibBuilder.loadTexts:
    nncExtCodeSpaceTable.setStatus("mandatory")
_NncExtCodeSpaceEntry_Object = MibTableRow
nncExtCodeSpaceEntry = _NncExtCodeSpaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 4, 4, 1)
)
nncExtCodeSpaceEntry.setIndexNames(
    (0, "NNCGNI00X6-MIB", "nncExtCodeSpaceIndex"),
)
if mibBuilder.loadTexts:
    nncExtCodeSpaceEntry.setStatus("mandatory")
_NncExtCodeSpaceIndex_Type = CodeSpaceIndex
_NncExtCodeSpaceIndex_Object = MibTableColumn
nncExtCodeSpaceIndex = _NncExtCodeSpaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 4, 4, 1, 1),
    _NncExtCodeSpaceIndex_Type()
)
nncExtCodeSpaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtCodeSpaceIndex.setStatus("mandatory")


class _NncExtCodeSpaceSize_Type(Integer32):
    """Custom type nncExtCodeSpaceSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NncExtCodeSpaceSize_Type.__name__ = "Integer32"
_NncExtCodeSpaceSize_Object = MibTableColumn
nncExtCodeSpaceSize = _NncExtCodeSpaceSize_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 4, 4, 1, 2),
    _NncExtCodeSpaceSize_Type()
)
nncExtCodeSpaceSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtCodeSpaceSize.setStatus("mandatory")


class _NncExtCodeSpaceStatus_Type(Integer32):
    """Custom type nncExtCodeSpaceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_NncExtCodeSpaceStatus_Type.__name__ = "Integer32"
_NncExtCodeSpaceStatus_Object = MibTableColumn
nncExtCodeSpaceStatus = _NncExtCodeSpaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 4, 4, 1, 3),
    _NncExtCodeSpaceStatus_Type()
)
nncExtCodeSpaceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtCodeSpaceStatus.setStatus("mandatory")


class _NncExtCodeSpaceGeneric_Type(DisplayString):
    """Custom type nncExtCodeSpaceGeneric based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_NncExtCodeSpaceGeneric_Type.__name__ = "DisplayString"
_NncExtCodeSpaceGeneric_Object = MibTableColumn
nncExtCodeSpaceGeneric = _NncExtCodeSpaceGeneric_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 4, 4, 1, 4),
    _NncExtCodeSpaceGeneric_Type()
)
nncExtCodeSpaceGeneric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtCodeSpaceGeneric.setStatus("mandatory")


class _NncExtCodeSpaceDownloadDate_Type(DisplayString):
    """Custom type nncExtCodeSpaceDownloadDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(9, 9),
    )


_NncExtCodeSpaceDownloadDate_Type.__name__ = "DisplayString"
_NncExtCodeSpaceDownloadDate_Object = MibTableColumn
nncExtCodeSpaceDownloadDate = _NncExtCodeSpaceDownloadDate_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 4, 4, 1, 5),
    _NncExtCodeSpaceDownloadDate_Type()
)
nncExtCodeSpaceDownloadDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtCodeSpaceDownloadDate.setStatus("mandatory")


class _NncExtCodeSpaceDownloadTime_Type(DisplayString):
    """Custom type nncExtCodeSpaceDownloadTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_NncExtCodeSpaceDownloadTime_Type.__name__ = "DisplayString"
_NncExtCodeSpaceDownloadTime_Object = MibTableColumn
nncExtCodeSpaceDownloadTime = _NncExtCodeSpaceDownloadTime_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 4, 4, 1, 6),
    _NncExtCodeSpaceDownloadTime_Type()
)
nncExtCodeSpaceDownloadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtCodeSpaceDownloadTime.setStatus("mandatory")
_NncExtCodeSpaceDownloadServer_Type = DisplayString
_NncExtCodeSpaceDownloadServer_Object = MibTableColumn
nncExtCodeSpaceDownloadServer = _NncExtCodeSpaceDownloadServer_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 4, 4, 1, 7),
    _NncExtCodeSpaceDownloadServer_Type()
)
nncExtCodeSpaceDownloadServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtCodeSpaceDownloadServer.setStatus("mandatory")
_NncExtCodeSpaceDownloadRequestor_Type = DisplayString
_NncExtCodeSpaceDownloadRequestor_Object = MibTableColumn
nncExtCodeSpaceDownloadRequestor = _NncExtCodeSpaceDownloadRequestor_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 4, 4, 1, 8),
    _NncExtCodeSpaceDownloadRequestor_Type()
)
nncExtCodeSpaceDownloadRequestor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtCodeSpaceDownloadRequestor.setStatus("mandatory")


class _NncExtCodeSpaceCompressionType_Type(Integer32):
    """Custom type nncExtCodeSpaceCompressionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("c1", 2),
          ("c2", 3),
          ("none", 1))
    )


_NncExtCodeSpaceCompressionType_Type.__name__ = "Integer32"
_NncExtCodeSpaceCompressionType_Object = MibTableColumn
nncExtCodeSpaceCompressionType = _NncExtCodeSpaceCompressionType_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 4, 4, 1, 9),
    _NncExtCodeSpaceCompressionType_Type()
)
nncExtCodeSpaceCompressionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtCodeSpaceCompressionType.setStatus("mandatory")


class _NncExtCodeSpaceLoadSize_Type(Integer32):
    """Custom type nncExtCodeSpaceLoadSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NncExtCodeSpaceLoadSize_Type.__name__ = "Integer32"
_NncExtCodeSpaceLoadSize_Object = MibTableColumn
nncExtCodeSpaceLoadSize = _NncExtCodeSpaceLoadSize_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 4, 4, 1, 10),
    _NncExtCodeSpaceLoadSize_Type()
)
nncExtCodeSpaceLoadSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtCodeSpaceLoadSize.setStatus("mandatory")
_NncExtNVMUsageTable_Object = MibTable
nncExtNVMUsageTable = _NncExtNVMUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 5, 1)
)
if mibBuilder.loadTexts:
    nncExtNVMUsageTable.setStatus("mandatory")
_NncExtNVMUsageEntry_Object = MibTableRow
nncExtNVMUsageEntry = _NncExtNVMUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 5, 1, 1)
)
nncExtNVMUsageEntry.setIndexNames(
    (0, "NNCGNI00X6-MIB", "nncExtNVMPoolIndex"),
)
if mibBuilder.loadTexts:
    nncExtNVMUsageEntry.setStatus("mandatory")
_NncExtNVMPoolIndex_Type = NVMPoolIndex
_NncExtNVMPoolIndex_Object = MibTableColumn
nncExtNVMPoolIndex = _NncExtNVMPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 5, 1, 1, 1),
    _NncExtNVMPoolIndex_Type()
)
nncExtNVMPoolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtNVMPoolIndex.setStatus("mandatory")


class _NncExtNVMPoolSize_Type(Integer32):
    """Custom type nncExtNVMPoolSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NncExtNVMPoolSize_Type.__name__ = "Integer32"
_NncExtNVMPoolSize_Object = MibTableColumn
nncExtNVMPoolSize = _NncExtNVMPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 5, 1, 1, 2),
    _NncExtNVMPoolSize_Type()
)
nncExtNVMPoolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtNVMPoolSize.setStatus("mandatory")


class _NncExtNVMPoolBytesUsed_Type(Integer32):
    """Custom type nncExtNVMPoolBytesUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NncExtNVMPoolBytesUsed_Type.__name__ = "Integer32"
_NncExtNVMPoolBytesUsed_Object = MibTableColumn
nncExtNVMPoolBytesUsed = _NncExtNVMPoolBytesUsed_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 5, 1, 1, 3),
    _NncExtNVMPoolBytesUsed_Type()
)
nncExtNVMPoolBytesUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtNVMPoolBytesUsed.setStatus("mandatory")


class _NncExtNVMLastRepair_Type(OctetString):
    """Custom type nncExtNVMLastRepair based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(31, 31),
    )


_NncExtNVMLastRepair_Type.__name__ = "OctetString"
_NncExtNVMLastRepair_Object = MibScalar
nncExtNVMLastRepair = _NncExtNVMLastRepair_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 5, 2),
    _NncExtNVMLastRepair_Type()
)
nncExtNVMLastRepair.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nncExtNVMLastRepair.setStatus("mandatory")
_NncExtProbeMPLTable_Object = MibTable
nncExtProbeMPLTable = _NncExtProbeMPLTable_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 12, 1)
)
if mibBuilder.loadTexts:
    nncExtProbeMPLTable.setStatus("mandatory")
_NncExtProbeMPLEntry_Object = MibTableRow
nncExtProbeMPLEntry = _NncExtProbeMPLEntry_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 12, 1, 1)
)
if mibBuilder.loadTexts:
    nncExtProbeMPLEntry.setStatus("mandatory")


class _NncExtProbeMPL_Type(OctetString):
    """Custom type nncExtProbeMPL based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NncExtProbeMPL_Type.__name__ = "OctetString"
_NncExtProbeMPL_Object = MibTableColumn
nncExtProbeMPL = _NncExtProbeMPL_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 12, 1, 1, 1),
    _NncExtProbeMPL_Type()
)
nncExtProbeMPL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nncExtProbeMPL.setStatus("mandatory")


class _NncDiagUndoAll_Type(Integer32):
    """Custom type nncDiagUndoAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("undo", 1)
    )


_NncDiagUndoAll_Type.__name__ = "Integer32"
_NncDiagUndoAll_Object = MibScalar
nncDiagUndoAll = _NncDiagUndoAll_Object(
    (1, 3, 6, 1, 4, 1, 123, 3, 13, 1),
    _NncDiagUndoAll_Type()
)
nncDiagUndoAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nncDiagUndoAll.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NNCGNI00X6-MIB",
    **{"RestartCause": RestartCause,
       "CodeSpaceIndex": CodeSpaceIndex,
       "NVMPoolIndex": NVMPoolIndex,
       "nncExtSysProductName": nncExtSysProductName,
       "nncExtSysCurrentGeneric": nncExtSysCurrentGeneric,
       "nncExtEnvFanStatus": nncExtEnvFanStatus,
       "nncExtEnvTemperatureSensor": nncExtEnvTemperatureSensor,
       "nncExtEnvPlus12Status": nncExtEnvPlus12Status,
       "nncExtEnvMinus12Status": nncExtEnvMinus12Status,
       "nncExtRestarts": nncExtRestarts,
       "nncExtFaultInducedRestarts": nncExtFaultInducedRestarts,
       "nncExtLastFault": nncExtLastFault,
       "nncExtFaultRepetitions": nncExtFaultRepetitions,
       "nncExtRestartTracebackTable": nncExtRestartTracebackTable,
       "nncExtRestartTracebackEntry": nncExtRestartTracebackEntry,
       "nncExtRestartTracebackIndex": nncExtRestartTracebackIndex,
       "nncExtRestartTracebackPCValue": nncExtRestartTracebackPCValue,
       "nncExtRestartRegisterTable": nncExtRestartRegisterTable,
       "nncExtRestartRegisterEntry": nncExtRestartRegisterEntry,
       "nncExtRestartRegisterIndex": nncExtRestartRegisterIndex,
       "nncExtRestartRegisterValue": nncExtRestartRegisterValue,
       "nncExtRestartForceToBoot": nncExtRestartForceToBoot,
       "nncExtRestartCause": nncExtRestartCause,
       "nncExtCodeSpaceCurrentlyActive": nncExtCodeSpaceCurrentlyActive,
       "nncExtCodeSpaceNextActive": nncExtCodeSpaceNextActive,
       "nncExtCodeSpaceNumber": nncExtCodeSpaceNumber,
       "nncExtCodeSpaceTable": nncExtCodeSpaceTable,
       "nncExtCodeSpaceEntry": nncExtCodeSpaceEntry,
       "nncExtCodeSpaceIndex": nncExtCodeSpaceIndex,
       "nncExtCodeSpaceSize": nncExtCodeSpaceSize,
       "nncExtCodeSpaceStatus": nncExtCodeSpaceStatus,
       "nncExtCodeSpaceGeneric": nncExtCodeSpaceGeneric,
       "nncExtCodeSpaceDownloadDate": nncExtCodeSpaceDownloadDate,
       "nncExtCodeSpaceDownloadTime": nncExtCodeSpaceDownloadTime,
       "nncExtCodeSpaceDownloadServer": nncExtCodeSpaceDownloadServer,
       "nncExtCodeSpaceDownloadRequestor": nncExtCodeSpaceDownloadRequestor,
       "nncExtCodeSpaceCompressionType": nncExtCodeSpaceCompressionType,
       "nncExtCodeSpaceLoadSize": nncExtCodeSpaceLoadSize,
       "nncExtNVMUsageTable": nncExtNVMUsageTable,
       "nncExtNVMUsageEntry": nncExtNVMUsageEntry,
       "nncExtNVMPoolIndex": nncExtNVMPoolIndex,
       "nncExtNVMPoolSize": nncExtNVMPoolSize,
       "nncExtNVMPoolBytesUsed": nncExtNVMPoolBytesUsed,
       "nncExtNVMLastRepair": nncExtNVMLastRepair,
       "nncExtProbeMPLTable": nncExtProbeMPLTable,
       "nncExtProbeMPLEntry": nncExtProbeMPLEntry,
       "nncExtProbeMPL": nncExtProbeMPL,
       "nncDiagUndoAll": nncDiagUndoAll}
)
