# SNMP MIB module (BAS-SONET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BAS-SONET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:33 2024
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

(basSonet,) = mibBuilder.importSymbols(
    "BAS-MIB",
    "basSonet")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

basSonetMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 20, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BasSonetObjects_ObjectIdentity = ObjectIdentity
basSonetObjects = _BasSonetObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 20, 1, 1)
)
_BasSonetPathTable_Object = MibTable
basSonetPathTable = _BasSonetPathTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 20, 1, 1, 1)
)
if mibBuilder.loadTexts:
    basSonetPathTable.setStatus("current")
_BasSonetPathEntry_Object = MibTableRow
basSonetPathEntry = _BasSonetPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 20, 1, 1, 1, 1)
)
basSonetPathEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    basSonetPathEntry.setStatus("current")
_BasSonetPathB3Err_Type = Counter32
_BasSonetPathB3Err_Object = MibTableColumn
basSonetPathB3Err = _BasSonetPathB3Err_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 20, 1, 1, 1, 1, 1),
    _BasSonetPathB3Err_Type()
)
basSonetPathB3Err.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basSonetPathB3Err.setStatus("current")
_BasSonetPathG1Err_Type = Counter32
_BasSonetPathG1Err_Object = MibTableColumn
basSonetPathG1Err = _BasSonetPathG1Err_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 20, 1, 1, 1, 1, 2),
    _BasSonetPathG1Err_Type()
)
basSonetPathG1Err.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basSonetPathG1Err.setStatus("current")
_BasSonetPathPais_Type = Counter32
_BasSonetPathPais_Object = MibTableColumn
basSonetPathPais = _BasSonetPathPais_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 20, 1, 1, 1, 1, 3),
    _BasSonetPathPais_Type()
)
basSonetPathPais.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basSonetPathPais.setStatus("current")
_BasSonetPathPrdi_Type = Counter32
_BasSonetPathPrdi_Object = MibTableColumn
basSonetPathPrdi = _BasSonetPathPrdi_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 20, 1, 1, 1, 1, 4),
    _BasSonetPathPrdi_Type()
)
basSonetPathPrdi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basSonetPathPrdi.setStatus("current")
_BasSonetPathPlop_Type = Counter32
_BasSonetPathPlop_Object = MibTableColumn
basSonetPathPlop = _BasSonetPathPlop_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 20, 1, 1, 1, 1, 5),
    _BasSonetPathPlop_Type()
)
basSonetPathPlop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basSonetPathPlop.setStatus("current")


class _BasSonetPathB3Threshold_Type(Integer32):
    """Custom type basSonetPathB3Threshold based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 9),
    )


_BasSonetPathB3Threshold_Type.__name__ = "Integer32"
_BasSonetPathB3Threshold_Object = MibTableColumn
basSonetPathB3Threshold = _BasSonetPathB3Threshold_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 20, 1, 1, 1, 1, 6),
    _BasSonetPathB3Threshold_Type()
)
basSonetPathB3Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basSonetPathB3Threshold.setStatus("current")
_BasSonetPathRxJ1_Type = Integer32
_BasSonetPathRxJ1_Object = MibTableColumn
basSonetPathRxJ1 = _BasSonetPathRxJ1_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 20, 1, 1, 1, 1, 7),
    _BasSonetPathRxJ1_Type()
)
basSonetPathRxJ1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basSonetPathRxJ1.setStatus("current")
_BasSonetPathRxC2_Type = Integer32
_BasSonetPathRxC2_Object = MibTableColumn
basSonetPathRxC2 = _BasSonetPathRxC2_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 20, 1, 1, 1, 1, 8),
    _BasSonetPathRxC2_Type()
)
basSonetPathRxC2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basSonetPathRxC2.setStatus("current")
_BasSonetPathRxG1_Type = Integer32
_BasSonetPathRxG1_Object = MibTableColumn
basSonetPathRxG1 = _BasSonetPathRxG1_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 20, 1, 1, 1, 1, 9),
    _BasSonetPathRxG1_Type()
)
basSonetPathRxG1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basSonetPathRxG1.setStatus("current")
_BasSonetLineTable_Object = MibTable
basSonetLineTable = _BasSonetLineTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 20, 1, 1, 2)
)
if mibBuilder.loadTexts:
    basSonetLineTable.setStatus("current")
_BasSonetLineEntry_Object = MibTableRow
basSonetLineEntry = _BasSonetLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 20, 1, 1, 2, 1)
)
basSonetLineEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    basSonetLineEntry.setStatus("current")
_BasSonetLineTxErr_Type = Counter32
_BasSonetLineTxErr_Object = MibTableColumn
basSonetLineTxErr = _BasSonetLineTxErr_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 20, 1, 1, 2, 1, 1),
    _BasSonetLineTxErr_Type()
)
basSonetLineTxErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basSonetLineTxErr.setStatus("current")
_BasSonetLineB1Err_Type = Counter32
_BasSonetLineB1Err_Object = MibTableColumn
basSonetLineB1Err = _BasSonetLineB1Err_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 20, 1, 1, 2, 1, 2),
    _BasSonetLineB1Err_Type()
)
basSonetLineB1Err.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basSonetLineB1Err.setStatus("current")
_BasSonetLineB2Err_Type = Counter32
_BasSonetLineB2Err_Object = MibTableColumn
basSonetLineB2Err = _BasSonetLineB2Err_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 20, 1, 1, 2, 1, 3),
    _BasSonetLineB2Err_Type()
)
basSonetLineB2Err.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basSonetLineB2Err.setStatus("current")
_BasSonetLineM1Err_Type = Counter32
_BasSonetLineM1Err_Object = MibTableColumn
basSonetLineM1Err = _BasSonetLineM1Err_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 20, 1, 1, 2, 1, 4),
    _BasSonetLineM1Err_Type()
)
basSonetLineM1Err.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basSonetLineM1Err.setStatus("current")
_BasSonetLineRxFifoOverflow_Type = Counter32
_BasSonetLineRxFifoOverflow_Object = MibTableColumn
basSonetLineRxFifoOverflow = _BasSonetLineRxFifoOverflow_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 20, 1, 1, 2, 1, 5),
    _BasSonetLineRxFifoOverflow_Type()
)
basSonetLineRxFifoOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basSonetLineRxFifoOverflow.setStatus("current")
_BasSonetLineRxAbort_Type = Counter32
_BasSonetLineRxAbort_Object = MibTableColumn
basSonetLineRxAbort = _BasSonetLineRxAbort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 20, 1, 1, 2, 1, 6),
    _BasSonetLineRxAbort_Type()
)
basSonetLineRxAbort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basSonetLineRxAbort.setStatus("current")
_BasSonetLineRxRunts_Type = Counter32
_BasSonetLineRxRunts_Object = MibTableColumn
basSonetLineRxRunts = _BasSonetLineRxRunts_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 20, 1, 1, 2, 1, 7),
    _BasSonetLineRxRunts_Type()
)
basSonetLineRxRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basSonetLineRxRunts.setStatus("current")
_BasSonetLineLoc_Type = Counter32
_BasSonetLineLoc_Object = MibTableColumn
basSonetLineLoc = _BasSonetLineLoc_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 20, 1, 1, 2, 1, 8),
    _BasSonetLineLoc_Type()
)
basSonetLineLoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basSonetLineLoc.setStatus("current")
_BasSonetLineLof_Type = Counter32
_BasSonetLineLof_Object = MibTableColumn
basSonetLineLof = _BasSonetLineLof_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 20, 1, 1, 2, 1, 9),
    _BasSonetLineLof_Type()
)
basSonetLineLof.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basSonetLineLof.setStatus("current")
_BasSonetLineLos_Type = Counter32
_BasSonetLineLos_Object = MibTableColumn
basSonetLineLos = _BasSonetLineLos_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 20, 1, 1, 2, 1, 10),
    _BasSonetLineLos_Type()
)
basSonetLineLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basSonetLineLos.setStatus("current")
_BasSonetLineLais_Type = Counter32
_BasSonetLineLais_Object = MibTableColumn
basSonetLineLais = _BasSonetLineLais_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 20, 1, 1, 2, 1, 11),
    _BasSonetLineLais_Type()
)
basSonetLineLais.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basSonetLineLais.setStatus("current")
_BasSonetLineLrdi_Type = Counter32
_BasSonetLineLrdi_Object = MibTableColumn
basSonetLineLrdi = _BasSonetLineLrdi_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 20, 1, 1, 2, 1, 12),
    _BasSonetLineLrdi_Type()
)
basSonetLineLrdi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basSonetLineLrdi.setStatus("current")


class _BasSonetLineB1Threshold_Type(Integer32):
    """Custom type basSonetLineB1Threshold based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 9),
    )


_BasSonetLineB1Threshold_Type.__name__ = "Integer32"
_BasSonetLineB1Threshold_Object = MibTableColumn
basSonetLineB1Threshold = _BasSonetLineB1Threshold_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 20, 1, 1, 2, 1, 13),
    _BasSonetLineB1Threshold_Type()
)
basSonetLineB1Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basSonetLineB1Threshold.setStatus("current")


class _BasSonetLineB2Threshold_Type(Integer32):
    """Custom type basSonetLineB2Threshold based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 9),
    )


_BasSonetLineB2Threshold_Type.__name__ = "Integer32"
_BasSonetLineB2Threshold_Object = MibTableColumn
basSonetLineB2Threshold = _BasSonetLineB2Threshold_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 20, 1, 1, 2, 1, 14),
    _BasSonetLineB2Threshold_Type()
)
basSonetLineB2Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basSonetLineB2Threshold.setStatus("current")


class _BasSonetLineSFThreshold_Type(Integer32):
    """Custom type basSonetLineSFThreshold based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 9),
    )


_BasSonetLineSFThreshold_Type.__name__ = "Integer32"
_BasSonetLineSFThreshold_Object = MibTableColumn
basSonetLineSFThreshold = _BasSonetLineSFThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 20, 1, 1, 2, 1, 15),
    _BasSonetLineSFThreshold_Type()
)
basSonetLineSFThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basSonetLineSFThreshold.setStatus("current")


class _BasSonetLineSDThreshold_Type(Integer32):
    """Custom type basSonetLineSDThreshold based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 9),
    )


_BasSonetLineSDThreshold_Type.__name__ = "Integer32"
_BasSonetLineSDThreshold_Object = MibTableColumn
basSonetLineSDThreshold = _BasSonetLineSDThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 20, 1, 1, 2, 1, 16),
    _BasSonetLineSDThreshold_Type()
)
basSonetLineSDThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basSonetLineSDThreshold.setStatus("current")
_BasSonetLineLastCleared_Type = TimeStamp
_BasSonetLineLastCleared_Object = MibTableColumn
basSonetLineLastCleared = _BasSonetLineLastCleared_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 20, 1, 1, 2, 1, 17),
    _BasSonetLineLastCleared_Type()
)
basSonetLineLastCleared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basSonetLineLastCleared.setStatus("current")
_BasSonetLineRxK1_Type = Integer32
_BasSonetLineRxK1_Object = MibTableColumn
basSonetLineRxK1 = _BasSonetLineRxK1_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 20, 1, 1, 2, 1, 18),
    _BasSonetLineRxK1_Type()
)
basSonetLineRxK1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basSonetLineRxK1.setStatus("current")
_BasSonetLineRxK2_Type = Integer32
_BasSonetLineRxK2_Object = MibTableColumn
basSonetLineRxK2 = _BasSonetLineRxK2_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 20, 1, 1, 2, 1, 19),
    _BasSonetLineRxK2_Type()
)
basSonetLineRxK2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basSonetLineRxK2.setStatus("current")
_BasSonetLineRxGiants_Type = Counter32
_BasSonetLineRxGiants_Object = MibTableColumn
basSonetLineRxGiants = _BasSonetLineRxGiants_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 20, 1, 1, 2, 1, 20),
    _BasSonetLineRxGiants_Type()
)
basSonetLineRxGiants.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basSonetLineRxGiants.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BAS-SONET-MIB",
    **{"basSonetMib": basSonetMib,
       "basSonetObjects": basSonetObjects,
       "basSonetPathTable": basSonetPathTable,
       "basSonetPathEntry": basSonetPathEntry,
       "basSonetPathB3Err": basSonetPathB3Err,
       "basSonetPathG1Err": basSonetPathG1Err,
       "basSonetPathPais": basSonetPathPais,
       "basSonetPathPrdi": basSonetPathPrdi,
       "basSonetPathPlop": basSonetPathPlop,
       "basSonetPathB3Threshold": basSonetPathB3Threshold,
       "basSonetPathRxJ1": basSonetPathRxJ1,
       "basSonetPathRxC2": basSonetPathRxC2,
       "basSonetPathRxG1": basSonetPathRxG1,
       "basSonetLineTable": basSonetLineTable,
       "basSonetLineEntry": basSonetLineEntry,
       "basSonetLineTxErr": basSonetLineTxErr,
       "basSonetLineB1Err": basSonetLineB1Err,
       "basSonetLineB2Err": basSonetLineB2Err,
       "basSonetLineM1Err": basSonetLineM1Err,
       "basSonetLineRxFifoOverflow": basSonetLineRxFifoOverflow,
       "basSonetLineRxAbort": basSonetLineRxAbort,
       "basSonetLineRxRunts": basSonetLineRxRunts,
       "basSonetLineLoc": basSonetLineLoc,
       "basSonetLineLof": basSonetLineLof,
       "basSonetLineLos": basSonetLineLos,
       "basSonetLineLais": basSonetLineLais,
       "basSonetLineLrdi": basSonetLineLrdi,
       "basSonetLineB1Threshold": basSonetLineB1Threshold,
       "basSonetLineB2Threshold": basSonetLineB2Threshold,
       "basSonetLineSFThreshold": basSonetLineSFThreshold,
       "basSonetLineSDThreshold": basSonetLineSDThreshold,
       "basSonetLineLastCleared": basSonetLineLastCleared,
       "basSonetLineRxK1": basSonetLineRxK1,
       "basSonetLineRxK2": basSonetLineRxK2,
       "basSonetLineRxGiants": basSonetLineRxGiants}
)
