# SNMP MIB module (ChrComPmAtmATM-VC-Current-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ChrComPmAtmATM-VC-Current-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:22:01 2024
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

(atmVclVci,
 atmVclVpi) = mibBuilder.importSymbols(
    "ATM-MIB",
    "atmVclVci",
    "atmVclVpi")

(chrComIfifIndex,) = mibBuilder.importSymbols(
    "ChrComIfifTable-MIB",
    "chrComIfifIndex")

(TruthValue,) = mibBuilder.importSymbols(
    "ChrTyp-MIB",
    "TruthValue")

(chrComPmAtm,) = mibBuilder.importSymbols(
    "Chromatis-MIB",
    "chrComPmAtm")

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

_ChrComPmAtmATM_VC_CurrentTable_Object = MibTable
chrComPmAtmATM_VC_CurrentTable = _ChrComPmAtmATM_VC_CurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 7)
)
if mibBuilder.loadTexts:
    chrComPmAtmATM_VC_CurrentTable.setStatus("current")
_ChrComPmAtmATM_VC_CurrentEntry_Object = MibTableRow
chrComPmAtmATM_VC_CurrentEntry = _ChrComPmAtmATM_VC_CurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 7, 1)
)
chrComPmAtmATM_VC_CurrentEntry.setIndexNames(
    (0, "ChrComIfifTable-MIB", "chrComIfifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "ATM-MIB", "atmVclVci"),
)
if mibBuilder.loadTexts:
    chrComPmAtmATM_VC_CurrentEntry.setStatus("current")
_ChrComPmAtmSuspectedInterval_Type = TruthValue
_ChrComPmAtmSuspectedInterval_Object = MibTableColumn
chrComPmAtmSuspectedInterval = _ChrComPmAtmSuspectedInterval_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 7, 1, 1),
    _ChrComPmAtmSuspectedInterval_Type()
)
chrComPmAtmSuspectedInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmAtmSuspectedInterval.setStatus("current")


class _ChrComPmAtmElapsedTime_Type(Unsigned32):
    """Custom type chrComPmAtmElapsedTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmAtmElapsedTime_Type.__name__ = "Unsigned32"
_ChrComPmAtmElapsedTime_Object = MibTableColumn
chrComPmAtmElapsedTime = _ChrComPmAtmElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 7, 1, 2),
    _ChrComPmAtmElapsedTime_Type()
)
chrComPmAtmElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmAtmElapsedTime.setStatus("current")


class _ChrComPmAtmSuppressedIntrvls_Type(Gauge32):
    """Custom type chrComPmAtmSuppressedIntrvls based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmAtmSuppressedIntrvls_Type.__name__ = "Gauge32"
_ChrComPmAtmSuppressedIntrvls_Object = MibTableColumn
chrComPmAtmSuppressedIntrvls = _ChrComPmAtmSuppressedIntrvls_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 7, 1, 3),
    _ChrComPmAtmSuppressedIntrvls_Type()
)
chrComPmAtmSuppressedIntrvls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmAtmSuppressedIntrvls.setStatus("current")


class _ChrComPmAtmReceivedCells_Type(Gauge32):
    """Custom type chrComPmAtmReceivedCells based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmAtmReceivedCells_Type.__name__ = "Gauge32"
_ChrComPmAtmReceivedCells_Object = MibTableColumn
chrComPmAtmReceivedCells = _ChrComPmAtmReceivedCells_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 7, 1, 4),
    _ChrComPmAtmReceivedCells_Type()
)
chrComPmAtmReceivedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmAtmReceivedCells.setStatus("current")


class _ChrComPmAtmTransmittedCells_Type(Gauge32):
    """Custom type chrComPmAtmTransmittedCells based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmAtmTransmittedCells_Type.__name__ = "Gauge32"
_ChrComPmAtmTransmittedCells_Object = MibTableColumn
chrComPmAtmTransmittedCells = _ChrComPmAtmTransmittedCells_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 7, 1, 5),
    _ChrComPmAtmTransmittedCells_Type()
)
chrComPmAtmTransmittedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmAtmTransmittedCells.setStatus("current")


class _ChrComPmAtmThresholdProfIndex_Type(Unsigned32):
    """Custom type chrComPmAtmThresholdProfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmAtmThresholdProfIndex_Type.__name__ = "Unsigned32"
_ChrComPmAtmThresholdProfIndex_Object = MibTableColumn
chrComPmAtmThresholdProfIndex = _ChrComPmAtmThresholdProfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 7, 1, 6),
    _ChrComPmAtmThresholdProfIndex_Type()
)
chrComPmAtmThresholdProfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chrComPmAtmThresholdProfIndex.setStatus("current")
_ChrComPmAtmResetPmCountersAction_Type = TruthValue
_ChrComPmAtmResetPmCountersAction_Object = MibTableColumn
chrComPmAtmResetPmCountersAction = _ChrComPmAtmResetPmCountersAction_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 4, 7, 1, 7),
    _ChrComPmAtmResetPmCountersAction_Type()
)
chrComPmAtmResetPmCountersAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chrComPmAtmResetPmCountersAction.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ChrComPmAtmATM-VC-Current-MIB",
    **{"chrComPmAtmATM-VC-CurrentTable": chrComPmAtmATM_VC_CurrentTable,
       "chrComPmAtmATM-VC-CurrentEntry": chrComPmAtmATM_VC_CurrentEntry,
       "chrComPmAtmSuspectedInterval": chrComPmAtmSuspectedInterval,
       "chrComPmAtmElapsedTime": chrComPmAtmElapsedTime,
       "chrComPmAtmSuppressedIntrvls": chrComPmAtmSuppressedIntrvls,
       "chrComPmAtmReceivedCells": chrComPmAtmReceivedCells,
       "chrComPmAtmTransmittedCells": chrComPmAtmTransmittedCells,
       "chrComPmAtmThresholdProfIndex": chrComPmAtmThresholdProfIndex,
       "chrComPmAtmResetPmCountersAction": chrComPmAtmResetPmCountersAction}
)
