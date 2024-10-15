# SNMP MIB module (Fore-aal5-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Fore-aal5-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:47:21 2024
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

(frameInternetworking,) = mibBuilder.importSymbols(
    "Fore-Common-MIB",
    "frameInternetworking")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

aal5 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Aal5VccTable_Object = MibTable
aal5VccTable = _Aal5VccTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 1)
)
if mibBuilder.loadTexts:
    aal5VccTable.setStatus("current")
_Aal5VccEntry_Object = MibTableRow
aal5VccEntry = _Aal5VccEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 1, 1)
)
aal5VccEntry.setIndexNames(
    (0, "Fore-aal5-MIB", "aal5VccAtmFabServiceIfIndex"),
    (0, "Fore-aal5-MIB", "aal5VccFabVpi"),
    (0, "Fore-aal5-MIB", "aal5VccFabVci"),
)
if mibBuilder.loadTexts:
    aal5VccEntry.setStatus("current")
_Aal5VccAtmFabServiceIfIndex_Type = InterfaceIndex
_Aal5VccAtmFabServiceIfIndex_Object = MibTableColumn
aal5VccAtmFabServiceIfIndex = _Aal5VccAtmFabServiceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 1, 1, 1),
    _Aal5VccAtmFabServiceIfIndex_Type()
)
aal5VccAtmFabServiceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5VccAtmFabServiceIfIndex.setStatus("current")
_Aal5VccFabVpi_Type = Integer32
_Aal5VccFabVpi_Object = MibTableColumn
aal5VccFabVpi = _Aal5VccFabVpi_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 1, 1, 2),
    _Aal5VccFabVpi_Type()
)
aal5VccFabVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5VccFabVpi.setStatus("current")
_Aal5VccFabVci_Type = Integer32
_Aal5VccFabVci_Object = MibTableColumn
aal5VccFabVci = _Aal5VccFabVci_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 1, 1, 3),
    _Aal5VccFabVci_Type()
)
aal5VccFabVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5VccFabVci.setStatus("current")
_Aal5VccCrcErrs_Type = Counter32
_Aal5VccCrcErrs_Object = MibTableColumn
aal5VccCrcErrs = _Aal5VccCrcErrs_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 1, 1, 4),
    _Aal5VccCrcErrs_Type()
)
aal5VccCrcErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5VccCrcErrs.setStatus("current")
_Aal5VccSarTimeOuts_Type = Counter32
_Aal5VccSarTimeOuts_Object = MibTableColumn
aal5VccSarTimeOuts = _Aal5VccSarTimeOuts_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 1, 1, 5),
    _Aal5VccSarTimeOuts_Type()
)
aal5VccSarTimeOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5VccSarTimeOuts.setStatus("current")
_Aal5VccOverSizedPDUs_Type = Counter32
_Aal5VccOverSizedPDUs_Object = MibTableColumn
aal5VccOverSizedPDUs = _Aal5VccOverSizedPDUs_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 1, 1, 6),
    _Aal5VccOverSizedPDUs_Type()
)
aal5VccOverSizedPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5VccOverSizedPDUs.setStatus("current")
_Aal5VccLengthErrPDUs_Type = Counter32
_Aal5VccLengthErrPDUs_Object = MibTableColumn
aal5VccLengthErrPDUs = _Aal5VccLengthErrPDUs_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 1, 1, 7),
    _Aal5VccLengthErrPDUs_Type()
)
aal5VccLengthErrPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5VccLengthErrPDUs.setStatus("current")
_Aal5VccCPIErrs_Type = Counter32
_Aal5VccCPIErrs_Object = MibTableColumn
aal5VccCPIErrs = _Aal5VccCPIErrs_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 1, 1, 8),
    _Aal5VccCPIErrs_Type()
)
aal5VccCPIErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5VccCPIErrs.setStatus("current")
_Aal5VccInPDUs_Type = Counter32
_Aal5VccInPDUs_Object = MibTableColumn
aal5VccInPDUs = _Aal5VccInPDUs_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 1, 1, 9),
    _Aal5VccInPDUs_Type()
)
aal5VccInPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5VccInPDUs.setStatus("current")
_Aal5VccOutPDUs_Type = Counter32
_Aal5VccOutPDUs_Object = MibTableColumn
aal5VccOutPDUs = _Aal5VccOutPDUs_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 1, 1, 10),
    _Aal5VccOutPDUs_Type()
)
aal5VccOutPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5VccOutPDUs.setStatus("current")
_Aal5VccInOctets_Type = Counter32
_Aal5VccInOctets_Object = MibTableColumn
aal5VccInOctets = _Aal5VccInOctets_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 1, 1, 11),
    _Aal5VccInOctets_Type()
)
aal5VccInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5VccInOctets.setStatus("current")
_Aal5VccOutOctets_Type = Counter32
_Aal5VccOutOctets_Object = MibTableColumn
aal5VccOutOctets = _Aal5VccOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 1, 1, 12),
    _Aal5VccOutOctets_Type()
)
aal5VccOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5VccOutOctets.setStatus("current")
_Aal5CpcsCurrTable_Object = MibTable
aal5CpcsCurrTable = _Aal5CpcsCurrTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 2)
)
if mibBuilder.loadTexts:
    aal5CpcsCurrTable.setStatus("current")
_Aal5CpcsCurrEntry_Object = MibTableRow
aal5CpcsCurrEntry = _Aal5CpcsCurrEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 2, 1)
)
aal5CpcsCurrEntry.setIndexNames(
    (0, "Fore-aal5-MIB", "aal5CpcsFabServiceIfIndex"),
)
if mibBuilder.loadTexts:
    aal5CpcsCurrEntry.setStatus("current")
_Aal5CpcsFabServiceIfIndex_Type = InterfaceIndex
_Aal5CpcsFabServiceIfIndex_Object = MibTableColumn
aal5CpcsFabServiceIfIndex = _Aal5CpcsFabServiceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 2, 1, 1),
    _Aal5CpcsFabServiceIfIndex_Type()
)
aal5CpcsFabServiceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5CpcsFabServiceIfIndex.setStatus("current")
_Aal5CpcsCurrCRCErrs_Type = Counter32
_Aal5CpcsCurrCRCErrs_Object = MibTableColumn
aal5CpcsCurrCRCErrs = _Aal5CpcsCurrCRCErrs_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 2, 1, 2),
    _Aal5CpcsCurrCRCErrs_Type()
)
aal5CpcsCurrCRCErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5CpcsCurrCRCErrs.setStatus("current")
_Aal5CpcsCurrSarTimeOuts_Type = Counter32
_Aal5CpcsCurrSarTimeOuts_Object = MibTableColumn
aal5CpcsCurrSarTimeOuts = _Aal5CpcsCurrSarTimeOuts_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 2, 1, 3),
    _Aal5CpcsCurrSarTimeOuts_Type()
)
aal5CpcsCurrSarTimeOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5CpcsCurrSarTimeOuts.setStatus("current")
_Aal5CpcsCurrOverSizedPDUs_Type = Counter32
_Aal5CpcsCurrOverSizedPDUs_Object = MibTableColumn
aal5CpcsCurrOverSizedPDUs = _Aal5CpcsCurrOverSizedPDUs_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 2, 1, 4),
    _Aal5CpcsCurrOverSizedPDUs_Type()
)
aal5CpcsCurrOverSizedPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5CpcsCurrOverSizedPDUs.setStatus("current")
_Aal5CpcsCurrLengthErrs_Type = Counter32
_Aal5CpcsCurrLengthErrs_Object = MibTableColumn
aal5CpcsCurrLengthErrs = _Aal5CpcsCurrLengthErrs_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 2, 1, 5),
    _Aal5CpcsCurrLengthErrs_Type()
)
aal5CpcsCurrLengthErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5CpcsCurrLengthErrs.setStatus("current")
_Aal5CpcsCurrCPIErrs_Type = Counter32
_Aal5CpcsCurrCPIErrs_Object = MibTableColumn
aal5CpcsCurrCPIErrs = _Aal5CpcsCurrCPIErrs_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 2, 1, 6),
    _Aal5CpcsCurrCPIErrs_Type()
)
aal5CpcsCurrCPIErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5CpcsCurrCPIErrs.setStatus("current")
_Aal5CpcsIntvlTable_Object = MibTable
aal5CpcsIntvlTable = _Aal5CpcsIntvlTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 3)
)
if mibBuilder.loadTexts:
    aal5CpcsIntvlTable.setStatus("current")
_Aal5CpcsIntvlEntry_Object = MibTableRow
aal5CpcsIntvlEntry = _Aal5CpcsIntvlEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 3, 1)
)
aal5CpcsIntvlEntry.setIndexNames(
    (0, "Fore-aal5-MIB", "aal5CpcsIntvlFabServiceIfIndex"),
    (0, "Fore-aal5-MIB", "aal5CpcsIntvlNumber"),
)
if mibBuilder.loadTexts:
    aal5CpcsIntvlEntry.setStatus("current")
_Aal5CpcsIntvlFabServiceIfIndex_Type = InterfaceIndex
_Aal5CpcsIntvlFabServiceIfIndex_Object = MibTableColumn
aal5CpcsIntvlFabServiceIfIndex = _Aal5CpcsIntvlFabServiceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 3, 1, 1),
    _Aal5CpcsIntvlFabServiceIfIndex_Type()
)
aal5CpcsIntvlFabServiceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5CpcsIntvlFabServiceIfIndex.setStatus("current")


class _Aal5CpcsIntvlNumber_Type(Integer32):
    """Custom type aal5CpcsIntvlNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Aal5CpcsIntvlNumber_Type.__name__ = "Integer32"
_Aal5CpcsIntvlNumber_Object = MibTableColumn
aal5CpcsIntvlNumber = _Aal5CpcsIntvlNumber_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 3, 1, 2),
    _Aal5CpcsIntvlNumber_Type()
)
aal5CpcsIntvlNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5CpcsIntvlNumber.setStatus("current")
_Aal5CpcsIntvlCRCErrs_Type = Counter32
_Aal5CpcsIntvlCRCErrs_Object = MibTableColumn
aal5CpcsIntvlCRCErrs = _Aal5CpcsIntvlCRCErrs_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 3, 1, 3),
    _Aal5CpcsIntvlCRCErrs_Type()
)
aal5CpcsIntvlCRCErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5CpcsIntvlCRCErrs.setStatus("current")
_Aal5CpcsIntvlSarTimeOuts_Type = Counter32
_Aal5CpcsIntvlSarTimeOuts_Object = MibTableColumn
aal5CpcsIntvlSarTimeOuts = _Aal5CpcsIntvlSarTimeOuts_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 3, 1, 4),
    _Aal5CpcsIntvlSarTimeOuts_Type()
)
aal5CpcsIntvlSarTimeOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5CpcsIntvlSarTimeOuts.setStatus("current")
_Aal5CpcsIntvlOverSizedPDUs_Type = Counter32
_Aal5CpcsIntvlOverSizedPDUs_Object = MibTableColumn
aal5CpcsIntvlOverSizedPDUs = _Aal5CpcsIntvlOverSizedPDUs_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 3, 1, 5),
    _Aal5CpcsIntvlOverSizedPDUs_Type()
)
aal5CpcsIntvlOverSizedPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5CpcsIntvlOverSizedPDUs.setStatus("current")
_Aal5CpcsIntvlLengthErrs_Type = Counter32
_Aal5CpcsIntvlLengthErrs_Object = MibTableColumn
aal5CpcsIntvlLengthErrs = _Aal5CpcsIntvlLengthErrs_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 3, 1, 6),
    _Aal5CpcsIntvlLengthErrs_Type()
)
aal5CpcsIntvlLengthErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5CpcsIntvlLengthErrs.setStatus("current")
_Aal5CpcsIntvlCPIErrs_Type = Counter32
_Aal5CpcsIntvlCPIErrs_Object = MibTableColumn
aal5CpcsIntvlCPIErrs = _Aal5CpcsIntvlCPIErrs_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 3, 1, 7),
    _Aal5CpcsIntvlCPIErrs_Type()
)
aal5CpcsIntvlCPIErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5CpcsIntvlCPIErrs.setStatus("current")
_Aal5CpcsTotalTable_Object = MibTable
aal5CpcsTotalTable = _Aal5CpcsTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 4)
)
if mibBuilder.loadTexts:
    aal5CpcsTotalTable.setStatus("current")
_Aal5CpcsTotalEntry_Object = MibTableRow
aal5CpcsTotalEntry = _Aal5CpcsTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 4, 1)
)
aal5CpcsTotalEntry.setIndexNames(
    (0, "Fore-aal5-MIB", "aal5CpcsTotalFabServiceIfIndex"),
)
if mibBuilder.loadTexts:
    aal5CpcsTotalEntry.setStatus("current")
_Aal5CpcsTotalFabServiceIfIndex_Type = InterfaceIndex
_Aal5CpcsTotalFabServiceIfIndex_Object = MibTableColumn
aal5CpcsTotalFabServiceIfIndex = _Aal5CpcsTotalFabServiceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 4, 1, 1),
    _Aal5CpcsTotalFabServiceIfIndex_Type()
)
aal5CpcsTotalFabServiceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5CpcsTotalFabServiceIfIndex.setStatus("current")
_Aal5CpcsTotalValidIntervals_Type = Integer32
_Aal5CpcsTotalValidIntervals_Object = MibTableColumn
aal5CpcsTotalValidIntervals = _Aal5CpcsTotalValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 4, 1, 2),
    _Aal5CpcsTotalValidIntervals_Type()
)
aal5CpcsTotalValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5CpcsTotalValidIntervals.setStatus("current")
_Aal5CpcsTotalCRCErrs_Type = Counter32
_Aal5CpcsTotalCRCErrs_Object = MibTableColumn
aal5CpcsTotalCRCErrs = _Aal5CpcsTotalCRCErrs_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 4, 1, 3),
    _Aal5CpcsTotalCRCErrs_Type()
)
aal5CpcsTotalCRCErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5CpcsTotalCRCErrs.setStatus("current")
_Aal5CpcsTotalSarTimeOuts_Type = Counter32
_Aal5CpcsTotalSarTimeOuts_Object = MibTableColumn
aal5CpcsTotalSarTimeOuts = _Aal5CpcsTotalSarTimeOuts_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 4, 1, 4),
    _Aal5CpcsTotalSarTimeOuts_Type()
)
aal5CpcsTotalSarTimeOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5CpcsTotalSarTimeOuts.setStatus("current")
_Aal5CpcsTotalOverSizedPDUs_Type = Counter32
_Aal5CpcsTotalOverSizedPDUs_Object = MibTableColumn
aal5CpcsTotalOverSizedPDUs = _Aal5CpcsTotalOverSizedPDUs_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 4, 1, 5),
    _Aal5CpcsTotalOverSizedPDUs_Type()
)
aal5CpcsTotalOverSizedPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5CpcsTotalOverSizedPDUs.setStatus("current")
_Aal5CpcsTotalLengthErrs_Type = Counter32
_Aal5CpcsTotalLengthErrs_Object = MibTableColumn
aal5CpcsTotalLengthErrs = _Aal5CpcsTotalLengthErrs_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 4, 1, 6),
    _Aal5CpcsTotalLengthErrs_Type()
)
aal5CpcsTotalLengthErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5CpcsTotalLengthErrs.setStatus("current")
_Aal5CpcsTotalCPIErrs_Type = Counter32
_Aal5CpcsTotalCPIErrs_Object = MibTableColumn
aal5CpcsTotalCPIErrs = _Aal5CpcsTotalCPIErrs_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 4, 1, 7),
    _Aal5CpcsTotalCPIErrs_Type()
)
aal5CpcsTotalCPIErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5CpcsTotalCPIErrs.setStatus("current")
_Aal5EpdPpdVccTable_Object = MibTable
aal5EpdPpdVccTable = _Aal5EpdPpdVccTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 5)
)
if mibBuilder.loadTexts:
    aal5EpdPpdVccTable.setStatus("current")
_Aal5EpdPpdVccEntry_Object = MibTableRow
aal5EpdPpdVccEntry = _Aal5EpdPpdVccEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 5, 1)
)
aal5EpdPpdVccEntry.setIndexNames(
    (0, "Fore-aal5-MIB", "aal5EpdPpdAtmFabServiceIfIndex"),
    (0, "Fore-aal5-MIB", "aal5EpdPpdVccFabVpi"),
    (0, "Fore-aal5-MIB", "aal5EpdPpdVccFabVci"),
)
if mibBuilder.loadTexts:
    aal5EpdPpdVccEntry.setStatus("current")
_Aal5EpdPpdAtmFabServiceIfIndex_Type = InterfaceIndex
_Aal5EpdPpdAtmFabServiceIfIndex_Object = MibTableColumn
aal5EpdPpdAtmFabServiceIfIndex = _Aal5EpdPpdAtmFabServiceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 5, 1, 1),
    _Aal5EpdPpdAtmFabServiceIfIndex_Type()
)
aal5EpdPpdAtmFabServiceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5EpdPpdAtmFabServiceIfIndex.setStatus("current")
_Aal5EpdPpdVccFabVpi_Type = Integer32
_Aal5EpdPpdVccFabVpi_Object = MibTableColumn
aal5EpdPpdVccFabVpi = _Aal5EpdPpdVccFabVpi_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 5, 1, 2),
    _Aal5EpdPpdVccFabVpi_Type()
)
aal5EpdPpdVccFabVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5EpdPpdVccFabVpi.setStatus("current")
_Aal5EpdPpdVccFabVci_Type = Integer32
_Aal5EpdPpdVccFabVci_Object = MibTableColumn
aal5EpdPpdVccFabVci = _Aal5EpdPpdVccFabVci_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 5, 1, 3),
    _Aal5EpdPpdVccFabVci_Type()
)
aal5EpdPpdVccFabVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5EpdPpdVccFabVci.setStatus("current")
_Aal5EpdPpdVccDroppedCellsClp1_Type = Counter32
_Aal5EpdPpdVccDroppedCellsClp1_Object = MibTableColumn
aal5EpdPpdVccDroppedCellsClp1 = _Aal5EpdPpdVccDroppedCellsClp1_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 5, 1, 4),
    _Aal5EpdPpdVccDroppedCellsClp1_Type()
)
aal5EpdPpdVccDroppedCellsClp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5EpdPpdVccDroppedCellsClp1.setStatus("current")
_Aal5EpdPpdVccForwardedCellsClp1_Type = Counter32
_Aal5EpdPpdVccForwardedCellsClp1_Object = MibTableColumn
aal5EpdPpdVccForwardedCellsClp1 = _Aal5EpdPpdVccForwardedCellsClp1_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 5, 1, 5),
    _Aal5EpdPpdVccForwardedCellsClp1_Type()
)
aal5EpdPpdVccForwardedCellsClp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5EpdPpdVccForwardedCellsClp1.setStatus("current")
_Aal5EpdPpdVccDroppedCellsClp0_Type = Counter32
_Aal5EpdPpdVccDroppedCellsClp0_Object = MibTableColumn
aal5EpdPpdVccDroppedCellsClp0 = _Aal5EpdPpdVccDroppedCellsClp0_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 5, 1, 6),
    _Aal5EpdPpdVccDroppedCellsClp0_Type()
)
aal5EpdPpdVccDroppedCellsClp0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5EpdPpdVccDroppedCellsClp0.setStatus("current")
_Aal5EpdPpdVccForwardedCellsClp0_Type = Counter32
_Aal5EpdPpdVccForwardedCellsClp0_Object = MibTableColumn
aal5EpdPpdVccForwardedCellsClp0 = _Aal5EpdPpdVccForwardedCellsClp0_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 16, 5, 5, 1, 7),
    _Aal5EpdPpdVccForwardedCellsClp0_Type()
)
aal5EpdPpdVccForwardedCellsClp0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aal5EpdPpdVccForwardedCellsClp0.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Fore-aal5-MIB",
    **{"aal5": aal5,
       "aal5VccTable": aal5VccTable,
       "aal5VccEntry": aal5VccEntry,
       "aal5VccAtmFabServiceIfIndex": aal5VccAtmFabServiceIfIndex,
       "aal5VccFabVpi": aal5VccFabVpi,
       "aal5VccFabVci": aal5VccFabVci,
       "aal5VccCrcErrs": aal5VccCrcErrs,
       "aal5VccSarTimeOuts": aal5VccSarTimeOuts,
       "aal5VccOverSizedPDUs": aal5VccOverSizedPDUs,
       "aal5VccLengthErrPDUs": aal5VccLengthErrPDUs,
       "aal5VccCPIErrs": aal5VccCPIErrs,
       "aal5VccInPDUs": aal5VccInPDUs,
       "aal5VccOutPDUs": aal5VccOutPDUs,
       "aal5VccInOctets": aal5VccInOctets,
       "aal5VccOutOctets": aal5VccOutOctets,
       "aal5CpcsCurrTable": aal5CpcsCurrTable,
       "aal5CpcsCurrEntry": aal5CpcsCurrEntry,
       "aal5CpcsFabServiceIfIndex": aal5CpcsFabServiceIfIndex,
       "aal5CpcsCurrCRCErrs": aal5CpcsCurrCRCErrs,
       "aal5CpcsCurrSarTimeOuts": aal5CpcsCurrSarTimeOuts,
       "aal5CpcsCurrOverSizedPDUs": aal5CpcsCurrOverSizedPDUs,
       "aal5CpcsCurrLengthErrs": aal5CpcsCurrLengthErrs,
       "aal5CpcsCurrCPIErrs": aal5CpcsCurrCPIErrs,
       "aal5CpcsIntvlTable": aal5CpcsIntvlTable,
       "aal5CpcsIntvlEntry": aal5CpcsIntvlEntry,
       "aal5CpcsIntvlFabServiceIfIndex": aal5CpcsIntvlFabServiceIfIndex,
       "aal5CpcsIntvlNumber": aal5CpcsIntvlNumber,
       "aal5CpcsIntvlCRCErrs": aal5CpcsIntvlCRCErrs,
       "aal5CpcsIntvlSarTimeOuts": aal5CpcsIntvlSarTimeOuts,
       "aal5CpcsIntvlOverSizedPDUs": aal5CpcsIntvlOverSizedPDUs,
       "aal5CpcsIntvlLengthErrs": aal5CpcsIntvlLengthErrs,
       "aal5CpcsIntvlCPIErrs": aal5CpcsIntvlCPIErrs,
       "aal5CpcsTotalTable": aal5CpcsTotalTable,
       "aal5CpcsTotalEntry": aal5CpcsTotalEntry,
       "aal5CpcsTotalFabServiceIfIndex": aal5CpcsTotalFabServiceIfIndex,
       "aal5CpcsTotalValidIntervals": aal5CpcsTotalValidIntervals,
       "aal5CpcsTotalCRCErrs": aal5CpcsTotalCRCErrs,
       "aal5CpcsTotalSarTimeOuts": aal5CpcsTotalSarTimeOuts,
       "aal5CpcsTotalOverSizedPDUs": aal5CpcsTotalOverSizedPDUs,
       "aal5CpcsTotalLengthErrs": aal5CpcsTotalLengthErrs,
       "aal5CpcsTotalCPIErrs": aal5CpcsTotalCPIErrs,
       "aal5EpdPpdVccTable": aal5EpdPpdVccTable,
       "aal5EpdPpdVccEntry": aal5EpdPpdVccEntry,
       "aal5EpdPpdAtmFabServiceIfIndex": aal5EpdPpdAtmFabServiceIfIndex,
       "aal5EpdPpdVccFabVpi": aal5EpdPpdVccFabVpi,
       "aal5EpdPpdVccFabVci": aal5EpdPpdVccFabVci,
       "aal5EpdPpdVccDroppedCellsClp1": aal5EpdPpdVccDroppedCellsClp1,
       "aal5EpdPpdVccForwardedCellsClp1": aal5EpdPpdVccForwardedCellsClp1,
       "aal5EpdPpdVccDroppedCellsClp0": aal5EpdPpdVccDroppedCellsClp0,
       "aal5EpdPpdVccForwardedCellsClp0": aal5EpdPpdVccForwardedCellsClp0}
)
