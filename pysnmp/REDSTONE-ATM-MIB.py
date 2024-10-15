# SNMP MIB module (REDSTONE-ATM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/REDSTONE-ATM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:46:34 2024
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

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(rsMgmt,) = mibBuilder.importSymbols(
    "REDSTONE-SMI",
    "rsMgmt")

(RsNextIfIndex,) = mibBuilder.importSymbols(
    "REDSTONE-TC",
    "RsNextIfIndex")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

rsAtmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 8)
)
rsAtmMIB.setRevisions(
        ("1999-08-04 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RsAtmObjects_ObjectIdentity = ObjectIdentity
rsAtmObjects = _RsAtmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 8, 1)
)
_RsAtmIfLayer_ObjectIdentity = ObjectIdentity
rsAtmIfLayer = _RsAtmIfLayer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 8, 1, 1)
)
_RsAtmNextIfIndex_Type = RsNextIfIndex
_RsAtmNextIfIndex_Object = MibScalar
rsAtmNextIfIndex = _RsAtmNextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 8, 1, 1, 1),
    _RsAtmNextIfIndex_Type()
)
rsAtmNextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsAtmNextIfIndex.setStatus("current")
_RsAtmIfTable_Object = MibTable
rsAtmIfTable = _RsAtmIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 8, 1, 1, 2)
)
if mibBuilder.loadTexts:
    rsAtmIfTable.setStatus("current")
_RsAtmIfEntry_Object = MibTableRow
rsAtmIfEntry = _RsAtmIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 8, 1, 1, 2, 1)
)
rsAtmIfEntry.setIndexNames(
    (0, "REDSTONE-ATM-MIB", "rsAtmIfIndex"),
)
if mibBuilder.loadTexts:
    rsAtmIfEntry.setStatus("current")
_RsAtmIfIndex_Type = InterfaceIndex
_RsAtmIfIndex_Object = MibTableColumn
rsAtmIfIndex = _RsAtmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 8, 1, 1, 2, 1, 1),
    _RsAtmIfIndex_Type()
)
rsAtmIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rsAtmIfIndex.setStatus("current")
_RsAtmIfRowStatus_Type = RowStatus
_RsAtmIfRowStatus_Object = MibTableColumn
rsAtmIfRowStatus = _RsAtmIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 8, 1, 1, 2, 1, 2),
    _RsAtmIfRowStatus_Type()
)
rsAtmIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsAtmIfRowStatus.setStatus("current")
_RsAtmIfLowerIfIndex_Type = InterfaceIndexOrZero
_RsAtmIfLowerIfIndex_Object = MibTableColumn
rsAtmIfLowerIfIndex = _RsAtmIfLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 8, 1, 1, 2, 1, 3),
    _RsAtmIfLowerIfIndex_Type()
)
rsAtmIfLowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsAtmIfLowerIfIndex.setStatus("current")


class _RsAtmIfIlmiVpi_Type(Integer32):
    """Custom type rsAtmIfIlmiVpi based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RsAtmIfIlmiVpi_Type.__name__ = "Integer32"
_RsAtmIfIlmiVpi_Object = MibTableColumn
rsAtmIfIlmiVpi = _RsAtmIfIlmiVpi_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 8, 1, 1, 2, 1, 4),
    _RsAtmIfIlmiVpi_Type()
)
rsAtmIfIlmiVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsAtmIfIlmiVpi.setStatus("current")


class _RsAtmIfIlmiVci_Type(Integer32):
    """Custom type rsAtmIfIlmiVci based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RsAtmIfIlmiVci_Type.__name__ = "Integer32"
_RsAtmIfIlmiVci_Object = MibTableColumn
rsAtmIfIlmiVci = _RsAtmIfIlmiVci_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 8, 1, 1, 2, 1, 5),
    _RsAtmIfIlmiVci_Type()
)
rsAtmIfIlmiVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsAtmIfIlmiVci.setStatus("current")


class _RsAtmIfIlmiVcd_Type(Integer32):
    """Custom type rsAtmIfIlmiVcd based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RsAtmIfIlmiVcd_Type.__name__ = "Integer32"
_RsAtmIfIlmiVcd_Object = MibTableColumn
rsAtmIfIlmiVcd = _RsAtmIfIlmiVcd_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 8, 1, 1, 2, 1, 6),
    _RsAtmIfIlmiVcd_Type()
)
rsAtmIfIlmiVcd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsAtmIfIlmiVcd.setStatus("current")
_RsAtmIfIlmiPollFrequency_Type = Integer32
_RsAtmIfIlmiPollFrequency_Object = MibTableColumn
rsAtmIfIlmiPollFrequency = _RsAtmIfIlmiPollFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 8, 1, 1, 2, 1, 7),
    _RsAtmIfIlmiPollFrequency_Type()
)
rsAtmIfIlmiPollFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsAtmIfIlmiPollFrequency.setStatus("current")


class _RsAtmIfIlmiAdminState_Type(Integer32):
    """Custom type rsAtmIfIlmiAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_RsAtmIfIlmiAdminState_Type.__name__ = "Integer32"
_RsAtmIfIlmiAdminState_Object = MibTableColumn
rsAtmIfIlmiAdminState = _RsAtmIfIlmiAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 8, 1, 1, 2, 1, 8),
    _RsAtmIfIlmiAdminState_Type()
)
rsAtmIfIlmiAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsAtmIfIlmiAdminState.setStatus("current")


class _RsAtmIfUniVersion_Type(Integer32):
    """Custom type rsAtmIfUniVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("version3Dot0", 0),
          ("version3Dot1", 1),
          ("version4Dot0", 2))
    )


_RsAtmIfUniVersion_Type.__name__ = "Integer32"
_RsAtmIfUniVersion_Object = MibTableColumn
rsAtmIfUniVersion = _RsAtmIfUniVersion_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 8, 1, 1, 2, 1, 9),
    _RsAtmIfUniVersion_Type()
)
rsAtmIfUniVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsAtmIfUniVersion.setStatus("current")
_RsAtmAal5IfLayer_ObjectIdentity = ObjectIdentity
rsAtmAal5IfLayer = _RsAtmAal5IfLayer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 8, 1, 2)
)
_RsAtmAal5NextIfIndex_Type = RsNextIfIndex
_RsAtmAal5NextIfIndex_Object = MibScalar
rsAtmAal5NextIfIndex = _RsAtmAal5NextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 8, 1, 2, 1),
    _RsAtmAal5NextIfIndex_Type()
)
rsAtmAal5NextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsAtmAal5NextIfIndex.setStatus("current")
_RsAtmAal5IfTable_Object = MibTable
rsAtmAal5IfTable = _RsAtmAal5IfTable_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 8, 1, 2, 2)
)
if mibBuilder.loadTexts:
    rsAtmAal5IfTable.setStatus("current")
_RsAtmAal5IfEntry_Object = MibTableRow
rsAtmAal5IfEntry = _RsAtmAal5IfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 8, 1, 2, 2, 1)
)
rsAtmAal5IfEntry.setIndexNames(
    (0, "REDSTONE-ATM-MIB", "rsAtmAal5IfIndex"),
)
if mibBuilder.loadTexts:
    rsAtmAal5IfEntry.setStatus("current")
_RsAtmAal5IfIndex_Type = InterfaceIndex
_RsAtmAal5IfIndex_Object = MibTableColumn
rsAtmAal5IfIndex = _RsAtmAal5IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 8, 1, 2, 2, 1, 1),
    _RsAtmAal5IfIndex_Type()
)
rsAtmAal5IfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rsAtmAal5IfIndex.setStatus("current")
_RsAtmAal5IfRowStatus_Type = RowStatus
_RsAtmAal5IfRowStatus_Object = MibTableColumn
rsAtmAal5IfRowStatus = _RsAtmAal5IfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 8, 1, 2, 2, 1, 2),
    _RsAtmAal5IfRowStatus_Type()
)
rsAtmAal5IfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsAtmAal5IfRowStatus.setStatus("current")
_RsAtmAal5IfLowerIfIndex_Type = InterfaceIndexOrZero
_RsAtmAal5IfLowerIfIndex_Object = MibTableColumn
rsAtmAal5IfLowerIfIndex = _RsAtmAal5IfLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 8, 1, 2, 2, 1, 3),
    _RsAtmAal5IfLowerIfIndex_Type()
)
rsAtmAal5IfLowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsAtmAal5IfLowerIfIndex.setStatus("current")
_RsAtmSubIfLayer_ObjectIdentity = ObjectIdentity
rsAtmSubIfLayer = _RsAtmSubIfLayer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 8, 1, 3)
)
_RsAtmSubIfNextIfIndex_Type = RsNextIfIndex
_RsAtmSubIfNextIfIndex_Object = MibScalar
rsAtmSubIfNextIfIndex = _RsAtmSubIfNextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 8, 1, 3, 1),
    _RsAtmSubIfNextIfIndex_Type()
)
rsAtmSubIfNextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsAtmSubIfNextIfIndex.setStatus("current")
_RsAtmSubIfTable_Object = MibTable
rsAtmSubIfTable = _RsAtmSubIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 8, 1, 3, 2)
)
if mibBuilder.loadTexts:
    rsAtmSubIfTable.setStatus("current")
_RsAtmSubIfEntry_Object = MibTableRow
rsAtmSubIfEntry = _RsAtmSubIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 8, 1, 3, 2, 1)
)
rsAtmSubIfEntry.setIndexNames(
    (0, "REDSTONE-ATM-MIB", "rsAtmSubIfIndex"),
)
if mibBuilder.loadTexts:
    rsAtmSubIfEntry.setStatus("current")
_RsAtmSubIfIndex_Type = InterfaceIndex
_RsAtmSubIfIndex_Object = MibTableColumn
rsAtmSubIfIndex = _RsAtmSubIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 8, 1, 3, 2, 1, 1),
    _RsAtmSubIfIndex_Type()
)
rsAtmSubIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rsAtmSubIfIndex.setStatus("current")
_RsAtmSubIfRowStatus_Type = RowStatus
_RsAtmSubIfRowStatus_Object = MibTableColumn
rsAtmSubIfRowStatus = _RsAtmSubIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 8, 1, 3, 2, 1, 2),
    _RsAtmSubIfRowStatus_Type()
)
rsAtmSubIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsAtmSubIfRowStatus.setStatus("current")
_RsAtmSubIfDistinguisher_Type = Integer32
_RsAtmSubIfDistinguisher_Object = MibTableColumn
rsAtmSubIfDistinguisher = _RsAtmSubIfDistinguisher_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 8, 1, 3, 2, 1, 3),
    _RsAtmSubIfDistinguisher_Type()
)
rsAtmSubIfDistinguisher.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsAtmSubIfDistinguisher.setStatus("current")
_RsAtmSubIfLowerIfIndex_Type = InterfaceIndexOrZero
_RsAtmSubIfLowerIfIndex_Object = MibTableColumn
rsAtmSubIfLowerIfIndex = _RsAtmSubIfLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 8, 1, 3, 2, 1, 4),
    _RsAtmSubIfLowerIfIndex_Type()
)
rsAtmSubIfLowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsAtmSubIfLowerIfIndex.setStatus("current")
_RsAtmSubIfVccTable_Object = MibTable
rsAtmSubIfVccTable = _RsAtmSubIfVccTable_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 8, 1, 3, 3)
)
if mibBuilder.loadTexts:
    rsAtmSubIfVccTable.setStatus("current")
_RsAtmSubIfVccEntry_Object = MibTableRow
rsAtmSubIfVccEntry = _RsAtmSubIfVccEntry_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 8, 1, 3, 3, 1)
)
rsAtmSubIfVccEntry.setIndexNames(
    (0, "REDSTONE-ATM-MIB", "rsAtmSubIfIndex"),
    (0, "REDSTONE-ATM-MIB", "rsAtmSubIfVccVpi"),
    (0, "REDSTONE-ATM-MIB", "rsAtmSubIfVccVci"),
)
if mibBuilder.loadTexts:
    rsAtmSubIfVccEntry.setStatus("current")


class _RsAtmSubIfVccVpi_Type(Integer32):
    """Custom type rsAtmSubIfVccVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RsAtmSubIfVccVpi_Type.__name__ = "Integer32"
_RsAtmSubIfVccVpi_Object = MibTableColumn
rsAtmSubIfVccVpi = _RsAtmSubIfVccVpi_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 8, 1, 3, 3, 1, 1),
    _RsAtmSubIfVccVpi_Type()
)
rsAtmSubIfVccVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rsAtmSubIfVccVpi.setStatus("current")


class _RsAtmSubIfVccVci_Type(Integer32):
    """Custom type rsAtmSubIfVccVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RsAtmSubIfVccVci_Type.__name__ = "Integer32"
_RsAtmSubIfVccVci_Object = MibTableColumn
rsAtmSubIfVccVci = _RsAtmSubIfVccVci_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 8, 1, 3, 3, 1, 2),
    _RsAtmSubIfVccVci_Type()
)
rsAtmSubIfVccVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rsAtmSubIfVccVci.setStatus("current")
_RsAtmSubIfVccRowStatus_Type = RowStatus
_RsAtmSubIfVccRowStatus_Object = MibTableColumn
rsAtmSubIfVccRowStatus = _RsAtmSubIfVccRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 8, 1, 3, 3, 1, 3),
    _RsAtmSubIfVccRowStatus_Type()
)
rsAtmSubIfVccRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsAtmSubIfVccRowStatus.setStatus("current")


class _RsAtmSubIfVccVcd_Type(Integer32):
    """Custom type rsAtmSubIfVccVcd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RsAtmSubIfVccVcd_Type.__name__ = "Integer32"
_RsAtmSubIfVccVcd_Object = MibTableColumn
rsAtmSubIfVccVcd = _RsAtmSubIfVccVcd_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 8, 1, 3, 3, 1, 4),
    _RsAtmSubIfVccVcd_Type()
)
rsAtmSubIfVccVcd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsAtmSubIfVccVcd.setStatus("current")


class _RsAtmSubIfVccType_Type(Integer32):
    """Custom type rsAtmSubIfVccType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("rfc1483Llc", 1),
          ("rfc1483VcMux", 0))
    )


_RsAtmSubIfVccType_Type.__name__ = "Integer32"
_RsAtmSubIfVccType_Object = MibTableColumn
rsAtmSubIfVccType = _RsAtmSubIfVccType_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 8, 1, 3, 3, 1, 5),
    _RsAtmSubIfVccType_Type()
)
rsAtmSubIfVccType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsAtmSubIfVccType.setStatus("current")


class _RsAtmSubIfVccServiceCategory_Type(Integer32):
    """Custom type rsAtmSubIfVccServiceCategory based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nrtVbr", 2),
          ("ubr", 0),
          ("ubrPcr", 1))
    )


_RsAtmSubIfVccServiceCategory_Type.__name__ = "Integer32"
_RsAtmSubIfVccServiceCategory_Object = MibTableColumn
rsAtmSubIfVccServiceCategory = _RsAtmSubIfVccServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 8, 1, 3, 3, 1, 6),
    _RsAtmSubIfVccServiceCategory_Type()
)
rsAtmSubIfVccServiceCategory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsAtmSubIfVccServiceCategory.setStatus("current")


class _RsAtmSubIfVccPcr_Type(Integer32):
    """Custom type rsAtmSubIfVccPcr based on Integer32"""
    defaultValue = 0


_RsAtmSubIfVccPcr_Object = MibTableColumn
rsAtmSubIfVccPcr = _RsAtmSubIfVccPcr_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 8, 1, 3, 3, 1, 7),
    _RsAtmSubIfVccPcr_Type()
)
rsAtmSubIfVccPcr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsAtmSubIfVccPcr.setStatus("current")
if mibBuilder.loadTexts:
    rsAtmSubIfVccPcr.setUnits("cells per second")


class _RsAtmSubIfVccScr_Type(Integer32):
    """Custom type rsAtmSubIfVccScr based on Integer32"""
    defaultValue = 0


_RsAtmSubIfVccScr_Object = MibTableColumn
rsAtmSubIfVccScr = _RsAtmSubIfVccScr_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 8, 1, 3, 3, 1, 8),
    _RsAtmSubIfVccScr_Type()
)
rsAtmSubIfVccScr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsAtmSubIfVccScr.setStatus("current")
if mibBuilder.loadTexts:
    rsAtmSubIfVccScr.setUnits("cells per second")


class _RsAtmSubIfVccMbs_Type(Integer32):
    """Custom type rsAtmSubIfVccMbs based on Integer32"""
    defaultValue = 0


_RsAtmSubIfVccMbs_Object = MibTableColumn
rsAtmSubIfVccMbs = _RsAtmSubIfVccMbs_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 8, 1, 3, 3, 1, 9),
    _RsAtmSubIfVccMbs_Type()
)
rsAtmSubIfVccMbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsAtmSubIfVccMbs.setStatus("current")
if mibBuilder.loadTexts:
    rsAtmSubIfVccMbs.setUnits("cells")
_RsAtmConformance_ObjectIdentity = ObjectIdentity
rsAtmConformance = _RsAtmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 8, 4)
)
_RsAtmCompliances_ObjectIdentity = ObjectIdentity
rsAtmCompliances = _RsAtmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 8, 4, 1)
)
_RsAtmGroups_ObjectIdentity = ObjectIdentity
rsAtmGroups = _RsAtmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 8, 4, 2)
)

# Managed Objects groups

rsAtmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2773, 2, 8, 4, 2, 1)
)
rsAtmGroup.setObjects(
      *(("REDSTONE-ATM-MIB", "rsAtmNextIfIndex"),
        ("REDSTONE-ATM-MIB", "rsAtmIfRowStatus"),
        ("REDSTONE-ATM-MIB", "rsAtmIfLowerIfIndex"))
)
if mibBuilder.loadTexts:
    rsAtmGroup.setStatus("current")

rsAtmAal5Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2773, 2, 8, 4, 2, 2)
)
rsAtmAal5Group.setObjects(
      *(("REDSTONE-ATM-MIB", "rsAtmAal5NextIfIndex"),
        ("REDSTONE-ATM-MIB", "rsAtmAal5IfRowStatus"),
        ("REDSTONE-ATM-MIB", "rsAtmAal5IfLowerIfIndex"))
)
if mibBuilder.loadTexts:
    rsAtmAal5Group.setStatus("current")

rsAtmSubIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2773, 2, 8, 4, 2, 3)
)
rsAtmSubIfGroup.setObjects(
      *(("REDSTONE-ATM-MIB", "rsAtmSubIfNextIfIndex"),
        ("REDSTONE-ATM-MIB", "rsAtmSubIfRowStatus"),
        ("REDSTONE-ATM-MIB", "rsAtmSubIfLowerIfIndex"),
        ("REDSTONE-ATM-MIB", "rsAtmSubIfVccRowStatus"),
        ("REDSTONE-ATM-MIB", "rsAtmSubIfVccVcd"),
        ("REDSTONE-ATM-MIB", "rsAtmSubIfVccType"),
        ("REDSTONE-ATM-MIB", "rsAtmSubIfVccServiceCategory"),
        ("REDSTONE-ATM-MIB", "rsAtmSubIfVccPcr"),
        ("REDSTONE-ATM-MIB", "rsAtmSubIfVccScr"),
        ("REDSTONE-ATM-MIB", "rsAtmSubIfVccMbs"))
)
if mibBuilder.loadTexts:
    rsAtmSubIfGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rsAtmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2773, 2, 8, 4, 1, 1)
)
if mibBuilder.loadTexts:
    rsAtmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "REDSTONE-ATM-MIB",
    **{"rsAtmMIB": rsAtmMIB,
       "rsAtmObjects": rsAtmObjects,
       "rsAtmIfLayer": rsAtmIfLayer,
       "rsAtmNextIfIndex": rsAtmNextIfIndex,
       "rsAtmIfTable": rsAtmIfTable,
       "rsAtmIfEntry": rsAtmIfEntry,
       "rsAtmIfIndex": rsAtmIfIndex,
       "rsAtmIfRowStatus": rsAtmIfRowStatus,
       "rsAtmIfLowerIfIndex": rsAtmIfLowerIfIndex,
       "rsAtmIfIlmiVpi": rsAtmIfIlmiVpi,
       "rsAtmIfIlmiVci": rsAtmIfIlmiVci,
       "rsAtmIfIlmiVcd": rsAtmIfIlmiVcd,
       "rsAtmIfIlmiPollFrequency": rsAtmIfIlmiPollFrequency,
       "rsAtmIfIlmiAdminState": rsAtmIfIlmiAdminState,
       "rsAtmIfUniVersion": rsAtmIfUniVersion,
       "rsAtmAal5IfLayer": rsAtmAal5IfLayer,
       "rsAtmAal5NextIfIndex": rsAtmAal5NextIfIndex,
       "rsAtmAal5IfTable": rsAtmAal5IfTable,
       "rsAtmAal5IfEntry": rsAtmAal5IfEntry,
       "rsAtmAal5IfIndex": rsAtmAal5IfIndex,
       "rsAtmAal5IfRowStatus": rsAtmAal5IfRowStatus,
       "rsAtmAal5IfLowerIfIndex": rsAtmAal5IfLowerIfIndex,
       "rsAtmSubIfLayer": rsAtmSubIfLayer,
       "rsAtmSubIfNextIfIndex": rsAtmSubIfNextIfIndex,
       "rsAtmSubIfTable": rsAtmSubIfTable,
       "rsAtmSubIfEntry": rsAtmSubIfEntry,
       "rsAtmSubIfIndex": rsAtmSubIfIndex,
       "rsAtmSubIfRowStatus": rsAtmSubIfRowStatus,
       "rsAtmSubIfDistinguisher": rsAtmSubIfDistinguisher,
       "rsAtmSubIfLowerIfIndex": rsAtmSubIfLowerIfIndex,
       "rsAtmSubIfVccTable": rsAtmSubIfVccTable,
       "rsAtmSubIfVccEntry": rsAtmSubIfVccEntry,
       "rsAtmSubIfVccVpi": rsAtmSubIfVccVpi,
       "rsAtmSubIfVccVci": rsAtmSubIfVccVci,
       "rsAtmSubIfVccRowStatus": rsAtmSubIfVccRowStatus,
       "rsAtmSubIfVccVcd": rsAtmSubIfVccVcd,
       "rsAtmSubIfVccType": rsAtmSubIfVccType,
       "rsAtmSubIfVccServiceCategory": rsAtmSubIfVccServiceCategory,
       "rsAtmSubIfVccPcr": rsAtmSubIfVccPcr,
       "rsAtmSubIfVccScr": rsAtmSubIfVccScr,
       "rsAtmSubIfVccMbs": rsAtmSubIfVccMbs,
       "rsAtmConformance": rsAtmConformance,
       "rsAtmCompliances": rsAtmCompliances,
       "rsAtmCompliance": rsAtmCompliance,
       "rsAtmGroups": rsAtmGroups,
       "rsAtmGroup": rsAtmGroup,
       "rsAtmAal5Group": rsAtmAal5Group,
       "rsAtmSubIfGroup": rsAtmSubIfGroup}
)
