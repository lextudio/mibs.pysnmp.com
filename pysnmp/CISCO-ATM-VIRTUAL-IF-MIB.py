# SNMP MIB module (CISCO-ATM-VIRTUAL-IF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ATM-VIRTUAL-IF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:56:09 2024
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

(AtmVpIdentifier,) = mibBuilder.importSymbols(
    "ATM-TC-MIB",
    "AtmVpIdentifier")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ciscoAtmVirtualIfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 129)
)
ciscoAtmVirtualIfMIB.setRevisions(
        ("2002-10-11 00:00",
         "2002-05-07 00:00",
         "2001-09-03 00:00",
         "2000-08-11 00:00",
         "2000-01-14 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoAtmVirtualIfMIBObjects_ObjectIdentity = ObjectIdentity
ciscoAtmVirtualIfMIBObjects = _CiscoAtmVirtualIfMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1)
)
_CaviConfig_ObjectIdentity = ObjectIdentity
caviConfig = _CaviConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 1)
)
_CaviTable_Object = MibTable
caviTable = _CaviTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 1, 1)
)
if mibBuilder.loadTexts:
    caviTable.setStatus("current")
_CaviEntry_Object = MibTableRow
caviEntry = _CaviEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 1, 1, 1)
)
caviEntry.setIndexNames(
    (0, "CISCO-ATM-VIRTUAL-IF-MIB", "caviIndex"),
)
if mibBuilder.loadTexts:
    caviEntry.setStatus("current")


class _CaviIndex_Type(Integer32):
    """Custom type caviIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CaviIndex_Type.__name__ = "Integer32"
_CaviIndex_Object = MibTableColumn
caviIndex = _CaviIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 1, 1, 1, 1),
    _CaviIndex_Type()
)
caviIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caviIndex.setStatus("current")
_CaviPhyIfIndex_Type = InterfaceIndex
_CaviPhyIfIndex_Object = MibTableColumn
caviPhyIfIndex = _CaviPhyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 1, 1, 1, 2),
    _CaviPhyIfIndex_Type()
)
caviPhyIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caviPhyIfIndex.setStatus("current")
_CaviViIfIndex_Type = InterfaceIndex
_CaviViIfIndex_Object = MibTableColumn
caviViIfIndex = _CaviViIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 1, 1, 1, 3),
    _CaviViIfIndex_Type()
)
caviViIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviViIfIndex.setStatus("current")
_CaviMinRate_Type = Unsigned32
_CaviMinRate_Object = MibTableColumn
caviMinRate = _CaviMinRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 1, 1, 1, 4),
    _CaviMinRate_Type()
)
caviMinRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caviMinRate.setStatus("current")
if mibBuilder.loadTexts:
    caviMinRate.setUnits("cells-per-second")
_CaviMaxRate_Type = Unsigned32
_CaviMaxRate_Object = MibTableColumn
caviMaxRate = _CaviMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 1, 1, 1, 5),
    _CaviMaxRate_Type()
)
caviMaxRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caviMaxRate.setStatus("current")
if mibBuilder.loadTexts:
    caviMaxRate.setUnits("cells-per-second")


class _CaviFileId_Type(Unsigned32):
    """Custom type caviFileId based on Unsigned32"""
    defaultValue = 0


_CaviFileId_Object = MibTableColumn
caviFileId = _CaviFileId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 1, 1, 1, 6),
    _CaviFileId_Type()
)
caviFileId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caviFileId.setStatus("current")


class _CaviIfType_Type(Integer32):
    """Custom type caviIfType based on Integer32"""
    defaultValue = 1

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
        *(("evnni", 6),
          ("evuni", 5),
          ("nni", 2),
          ("uni", 1),
          ("vnni", 3),
          ("vuni", 4))
    )


_CaviIfType_Type.__name__ = "Integer32"
_CaviIfType_Object = MibTableColumn
caviIfType = _CaviIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 1, 1, 1, 7),
    _CaviIfType_Type()
)
caviIfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caviIfType.setStatus("current")


class _CaviVpiNum_Type(AtmVpIdentifier):
    """Custom type caviVpiNum based on AtmVpIdentifier"""
    defaultValue = 0


_CaviVpiNum_Object = MibTableColumn
caviVpiNum = _CaviVpiNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 1, 1, 1, 8),
    _CaviVpiNum_Type()
)
caviVpiNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caviVpiNum.setStatus("current")
_CaviRowStatus_Type = RowStatus
_CaviRowStatus_Object = MibTableColumn
caviRowStatus = _CaviRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 1, 1, 1, 9),
    _CaviRowStatus_Type()
)
caviRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caviRowStatus.setStatus("current")


class _CaviMinVpiNum_Type(AtmVpIdentifier):
    """Custom type caviMinVpiNum based on AtmVpIdentifier"""
    defaultValue = 0


_CaviMinVpiNum_Object = MibTableColumn
caviMinVpiNum = _CaviMinVpiNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 1, 1, 1, 10),
    _CaviMinVpiNum_Type()
)
caviMinVpiNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caviMinVpiNum.setStatus("current")
_CaviMaxVpiNum_Type = AtmVpIdentifier
_CaviMaxVpiNum_Object = MibTableColumn
caviMaxVpiNum = _CaviMaxVpiNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 1, 1, 1, 11),
    _CaviMaxVpiNum_Type()
)
caviMaxVpiNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    caviMaxVpiNum.setStatus("current")
_CaviStatistics_ObjectIdentity = ObjectIdentity
caviStatistics = _CaviStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2)
)
_CaviStatEgressTable_Object = MibTable
caviStatEgressTable = _CaviStatEgressTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 1)
)
if mibBuilder.loadTexts:
    caviStatEgressTable.setStatus("current")
_CaviStatEgressEntry_Object = MibTableRow
caviStatEgressEntry = _CaviStatEgressEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 1, 1)
)
caviStatEgressEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    caviStatEgressEntry.setStatus("current")
_CaviEgrRcvClp0Cells_Type = Counter32
_CaviEgrRcvClp0Cells_Object = MibTableColumn
caviEgrRcvClp0Cells = _CaviEgrRcvClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 1, 1, 1),
    _CaviEgrRcvClp0Cells_Type()
)
caviEgrRcvClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviEgrRcvClp0Cells.setStatus("current")
_CaviEgrRcvClp1Cells_Type = Counter32
_CaviEgrRcvClp1Cells_Object = MibTableColumn
caviEgrRcvClp1Cells = _CaviEgrRcvClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 1, 1, 2),
    _CaviEgrRcvClp1Cells_Type()
)
caviEgrRcvClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviEgrRcvClp1Cells.setStatus("current")
_CaviEgrClp0DiscCells_Type = Counter32
_CaviEgrClp0DiscCells_Object = MibTableColumn
caviEgrClp0DiscCells = _CaviEgrClp0DiscCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 1, 1, 3),
    _CaviEgrClp0DiscCells_Type()
)
caviEgrClp0DiscCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviEgrClp0DiscCells.setStatus("current")
_CaviEgrClp1DiscCells_Type = Counter32
_CaviEgrClp1DiscCells_Object = MibTableColumn
caviEgrClp1DiscCells = _CaviEgrClp1DiscCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 1, 1, 4),
    _CaviEgrClp1DiscCells_Type()
)
caviEgrClp1DiscCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviEgrClp1DiscCells.setStatus("current")
_CaviEgrXmtClp0Cells_Type = Counter32
_CaviEgrXmtClp0Cells_Object = MibTableColumn
caviEgrXmtClp0Cells = _CaviEgrXmtClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 1, 1, 5),
    _CaviEgrXmtClp0Cells_Type()
)
caviEgrXmtClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviEgrXmtClp0Cells.setStatus("current")
_CaviEgrXmtClp1Cells_Type = Counter32
_CaviEgrXmtClp1Cells_Object = MibTableColumn
caviEgrXmtClp1Cells = _CaviEgrXmtClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 1, 1, 6),
    _CaviEgrXmtClp1Cells_Type()
)
caviEgrXmtClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviEgrXmtClp1Cells.setStatus("current")
_CaviEgrRcvOAMCells_Type = Counter32
_CaviEgrRcvOAMCells_Object = MibTableColumn
caviEgrRcvOAMCells = _CaviEgrRcvOAMCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 1, 1, 7),
    _CaviEgrRcvOAMCells_Type()
)
caviEgrRcvOAMCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviEgrRcvOAMCells.setStatus("current")
_CaviEgrRMCells_Type = Counter32
_CaviEgrRMCells_Object = MibTableColumn
caviEgrRMCells = _CaviEgrRMCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 1, 1, 8),
    _CaviEgrRMCells_Type()
)
caviEgrRMCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviEgrRMCells.setStatus("current")
_CaviEgrXmtEFCICells_Type = Counter32
_CaviEgrXmtEFCICells_Object = MibTableColumn
caviEgrXmtEFCICells = _CaviEgrXmtEFCICells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 1, 1, 9),
    _CaviEgrXmtEFCICells_Type()
)
caviEgrXmtEFCICells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviEgrXmtEFCICells.setStatus("current")
_CaviEgrRcvEFCICells_Type = Counter32
_CaviEgrRcvEFCICells_Object = MibTableColumn
caviEgrRcvEFCICells = _CaviEgrRcvEFCICells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 1, 1, 10),
    _CaviEgrRcvEFCICells_Type()
)
caviEgrRcvEFCICells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviEgrRcvEFCICells.setStatus("current")
_CaviEgrXmtOAMCells_Type = Counter32
_CaviEgrXmtOAMCells_Object = MibTableColumn
caviEgrXmtOAMCells = _CaviEgrXmtOAMCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 1, 1, 11),
    _CaviEgrXmtOAMCells_Type()
)
caviEgrXmtOAMCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviEgrXmtOAMCells.setStatus("current")
_CaviHEgrXmtClp0Cells_Type = Counter64
_CaviHEgrXmtClp0Cells_Object = MibTableColumn
caviHEgrXmtClp0Cells = _CaviHEgrXmtClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 1, 1, 12),
    _CaviHEgrXmtClp0Cells_Type()
)
caviHEgrXmtClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviHEgrXmtClp0Cells.setStatus("current")
_CaviHEgrXmtClp1Cells_Type = Counter64
_CaviHEgrXmtClp1Cells_Object = MibTableColumn
caviHEgrXmtClp1Cells = _CaviHEgrXmtClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 1, 1, 13),
    _CaviHEgrXmtClp1Cells_Type()
)
caviHEgrXmtClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviHEgrXmtClp1Cells.setStatus("current")
_CaviHighEgrRcvClp0Cells_Type = Counter32
_CaviHighEgrRcvClp0Cells_Object = MibTableColumn
caviHighEgrRcvClp0Cells = _CaviHighEgrRcvClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 1, 1, 14),
    _CaviHighEgrRcvClp0Cells_Type()
)
caviHighEgrRcvClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviHighEgrRcvClp0Cells.setStatus("current")
_CaviHighEgrRcvClp1Cells_Type = Counter32
_CaviHighEgrRcvClp1Cells_Object = MibTableColumn
caviHighEgrRcvClp1Cells = _CaviHighEgrRcvClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 1, 1, 15),
    _CaviHighEgrRcvClp1Cells_Type()
)
caviHighEgrRcvClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviHighEgrRcvClp1Cells.setStatus("current")
_CaviHighEgrClp0DiscCells_Type = Counter32
_CaviHighEgrClp0DiscCells_Object = MibTableColumn
caviHighEgrClp0DiscCells = _CaviHighEgrClp0DiscCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 1, 1, 16),
    _CaviHighEgrClp0DiscCells_Type()
)
caviHighEgrClp0DiscCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviHighEgrClp0DiscCells.setStatus("current")
_CaviHighEgrClp1DiscCells_Type = Counter32
_CaviHighEgrClp1DiscCells_Object = MibTableColumn
caviHighEgrClp1DiscCells = _CaviHighEgrClp1DiscCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 1, 1, 17),
    _CaviHighEgrClp1DiscCells_Type()
)
caviHighEgrClp1DiscCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviHighEgrClp1DiscCells.setStatus("current")
_CaviHighEgrXmtClp0Cells_Type = Counter32
_CaviHighEgrXmtClp0Cells_Object = MibTableColumn
caviHighEgrXmtClp0Cells = _CaviHighEgrXmtClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 1, 1, 18),
    _CaviHighEgrXmtClp0Cells_Type()
)
caviHighEgrXmtClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviHighEgrXmtClp0Cells.setStatus("current")
_CaviHighEgrXmtClp1Cells_Type = Counter32
_CaviHighEgrXmtClp1Cells_Object = MibTableColumn
caviHighEgrXmtClp1Cells = _CaviHighEgrXmtClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 1, 1, 19),
    _CaviHighEgrXmtClp1Cells_Type()
)
caviHighEgrXmtClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviHighEgrXmtClp1Cells.setStatus("current")
_CaviHEgrRcvClp0Cells_Type = Counter64
_CaviHEgrRcvClp0Cells_Object = MibTableColumn
caviHEgrRcvClp0Cells = _CaviHEgrRcvClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 1, 1, 20),
    _CaviHEgrRcvClp0Cells_Type()
)
caviHEgrRcvClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviHEgrRcvClp0Cells.setStatus("current")
_CaviHEgrRcvClp1Cells_Type = Counter64
_CaviHEgrRcvClp1Cells_Object = MibTableColumn
caviHEgrRcvClp1Cells = _CaviHEgrRcvClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 1, 1, 21),
    _CaviHEgrRcvClp1Cells_Type()
)
caviHEgrRcvClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviHEgrRcvClp1Cells.setStatus("current")
_CaviHEgrClp0DiscCells_Type = Counter64
_CaviHEgrClp0DiscCells_Object = MibTableColumn
caviHEgrClp0DiscCells = _CaviHEgrClp0DiscCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 1, 1, 22),
    _CaviHEgrClp0DiscCells_Type()
)
caviHEgrClp0DiscCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviHEgrClp0DiscCells.setStatus("current")
_CaviHEgrClp1DiscCells_Type = Counter64
_CaviHEgrClp1DiscCells_Object = MibTableColumn
caviHEgrClp1DiscCells = _CaviHEgrClp1DiscCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 1, 1, 23),
    _CaviHEgrClp1DiscCells_Type()
)
caviHEgrClp1DiscCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviHEgrClp1DiscCells.setStatus("current")
_CaviEgressIntervalTable_Object = MibTable
caviEgressIntervalTable = _CaviEgressIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 2)
)
if mibBuilder.loadTexts:
    caviEgressIntervalTable.setStatus("current")
_CaviEgressIntervalEntry_Object = MibTableRow
caviEgressIntervalEntry = _CaviEgressIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 2, 1)
)
caviEgressIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-ATM-VIRTUAL-IF-MIB", "caviEgressIntervalNumber"),
)
if mibBuilder.loadTexts:
    caviEgressIntervalEntry.setStatus("current")


class _CaviEgressIntervalNumber_Type(Unsigned32):
    """Custom type caviEgressIntervalNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_CaviEgressIntervalNumber_Type.__name__ = "Unsigned32"
_CaviEgressIntervalNumber_Object = MibTableColumn
caviEgressIntervalNumber = _CaviEgressIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 2, 1, 1),
    _CaviEgressIntervalNumber_Type()
)
caviEgressIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviEgressIntervalNumber.setStatus("current")
_CaviIntEgrRcvClp0Cells_Type = Counter32
_CaviIntEgrRcvClp0Cells_Object = MibTableColumn
caviIntEgrRcvClp0Cells = _CaviIntEgrRcvClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 2, 1, 2),
    _CaviIntEgrRcvClp0Cells_Type()
)
caviIntEgrRcvClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviIntEgrRcvClp0Cells.setStatus("current")
_CaviIntEgrRcvClp1Cells_Type = Counter32
_CaviIntEgrRcvClp1Cells_Object = MibTableColumn
caviIntEgrRcvClp1Cells = _CaviIntEgrRcvClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 2, 1, 3),
    _CaviIntEgrRcvClp1Cells_Type()
)
caviIntEgrRcvClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviIntEgrRcvClp1Cells.setStatus("current")
_CaviIntEgrClp0DiscCells_Type = Counter32
_CaviIntEgrClp0DiscCells_Object = MibTableColumn
caviIntEgrClp0DiscCells = _CaviIntEgrClp0DiscCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 2, 1, 4),
    _CaviIntEgrClp0DiscCells_Type()
)
caviIntEgrClp0DiscCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviIntEgrClp0DiscCells.setStatus("current")
_CaviIntEgrClp1DiscCells_Type = Counter32
_CaviIntEgrClp1DiscCells_Object = MibTableColumn
caviIntEgrClp1DiscCells = _CaviIntEgrClp1DiscCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 2, 1, 5),
    _CaviIntEgrClp1DiscCells_Type()
)
caviIntEgrClp1DiscCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviIntEgrClp1DiscCells.setStatus("current")
_CaviIntEgrXmtClp0Cells_Type = Counter32
_CaviIntEgrXmtClp0Cells_Object = MibTableColumn
caviIntEgrXmtClp0Cells = _CaviIntEgrXmtClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 2, 1, 6),
    _CaviIntEgrXmtClp0Cells_Type()
)
caviIntEgrXmtClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviIntEgrXmtClp0Cells.setStatus("current")
_CaviIntEgrXmtClp1Cells_Type = Counter32
_CaviIntEgrXmtClp1Cells_Object = MibTableColumn
caviIntEgrXmtClp1Cells = _CaviIntEgrXmtClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 2, 1, 7),
    _CaviIntEgrXmtClp1Cells_Type()
)
caviIntEgrXmtClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviIntEgrXmtClp1Cells.setStatus("current")
_CaviIntEgrRcvOAMCells_Type = Counter32
_CaviIntEgrRcvOAMCells_Object = MibTableColumn
caviIntEgrRcvOAMCells = _CaviIntEgrRcvOAMCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 2, 1, 8),
    _CaviIntEgrRcvOAMCells_Type()
)
caviIntEgrRcvOAMCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviIntEgrRcvOAMCells.setStatus("current")
_CaviIntEgrRMCells_Type = Counter32
_CaviIntEgrRMCells_Object = MibTableColumn
caviIntEgrRMCells = _CaviIntEgrRMCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 2, 1, 9),
    _CaviIntEgrRMCells_Type()
)
caviIntEgrRMCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviIntEgrRMCells.setStatus("current")
_CaviIntEgrXmtEFCICells_Type = Counter32
_CaviIntEgrXmtEFCICells_Object = MibTableColumn
caviIntEgrXmtEFCICells = _CaviIntEgrXmtEFCICells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 2, 1, 10),
    _CaviIntEgrXmtEFCICells_Type()
)
caviIntEgrXmtEFCICells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviIntEgrXmtEFCICells.setStatus("current")
_CaviIntEgrRcvEFCICells_Type = Counter32
_CaviIntEgrRcvEFCICells_Object = MibTableColumn
caviIntEgrRcvEFCICells = _CaviIntEgrRcvEFCICells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 2, 1, 11),
    _CaviIntEgrRcvEFCICells_Type()
)
caviIntEgrRcvEFCICells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviIntEgrRcvEFCICells.setStatus("current")
_CaviIntEgrXmtOAMCells_Type = Counter32
_CaviIntEgrXmtOAMCells_Object = MibTableColumn
caviIntEgrXmtOAMCells = _CaviIntEgrXmtOAMCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 2, 1, 12),
    _CaviIntEgrXmtOAMCells_Type()
)
caviIntEgrXmtOAMCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviIntEgrXmtOAMCells.setStatus("current")
_CaviHighIntEgrRcvClp0Cells_Type = Counter32
_CaviHighIntEgrRcvClp0Cells_Object = MibTableColumn
caviHighIntEgrRcvClp0Cells = _CaviHighIntEgrRcvClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 2, 1, 13),
    _CaviHighIntEgrRcvClp0Cells_Type()
)
caviHighIntEgrRcvClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviHighIntEgrRcvClp0Cells.setStatus("current")
_CaviHighIntEgrRcvClp1Cells_Type = Counter32
_CaviHighIntEgrRcvClp1Cells_Object = MibTableColumn
caviHighIntEgrRcvClp1Cells = _CaviHighIntEgrRcvClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 2, 1, 14),
    _CaviHighIntEgrRcvClp1Cells_Type()
)
caviHighIntEgrRcvClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviHighIntEgrRcvClp1Cells.setStatus("current")
_CaviHighIntEgrClp0DiscCells_Type = Counter32
_CaviHighIntEgrClp0DiscCells_Object = MibTableColumn
caviHighIntEgrClp0DiscCells = _CaviHighIntEgrClp0DiscCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 2, 1, 15),
    _CaviHighIntEgrClp0DiscCells_Type()
)
caviHighIntEgrClp0DiscCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviHighIntEgrClp0DiscCells.setStatus("current")
_CaviHighIntEgrClp1DiscCells_Type = Counter32
_CaviHighIntEgrClp1DiscCells_Object = MibTableColumn
caviHighIntEgrClp1DiscCells = _CaviHighIntEgrClp1DiscCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 2, 1, 16),
    _CaviHighIntEgrClp1DiscCells_Type()
)
caviHighIntEgrClp1DiscCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviHighIntEgrClp1DiscCells.setStatus("current")
_CaviHighIntEgrXmtClp0Cells_Type = Counter32
_CaviHighIntEgrXmtClp0Cells_Object = MibTableColumn
caviHighIntEgrXmtClp0Cells = _CaviHighIntEgrXmtClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 2, 1, 17),
    _CaviHighIntEgrXmtClp0Cells_Type()
)
caviHighIntEgrXmtClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviHighIntEgrXmtClp0Cells.setStatus("current")
_CaviHighIntEgrXmtClp1Cells_Type = Counter32
_CaviHighIntEgrXmtClp1Cells_Object = MibTableColumn
caviHighIntEgrXmtClp1Cells = _CaviHighIntEgrXmtClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 2, 1, 18),
    _CaviHighIntEgrXmtClp1Cells_Type()
)
caviHighIntEgrXmtClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviHighIntEgrXmtClp1Cells.setStatus("current")
_CaviHIntEgrRcvClp0Cells_Type = Counter64
_CaviHIntEgrRcvClp0Cells_Object = MibTableColumn
caviHIntEgrRcvClp0Cells = _CaviHIntEgrRcvClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 2, 1, 19),
    _CaviHIntEgrRcvClp0Cells_Type()
)
caviHIntEgrRcvClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviHIntEgrRcvClp0Cells.setStatus("current")
_CaviHIntEgrRcvClp1Cells_Type = Counter64
_CaviHIntEgrRcvClp1Cells_Object = MibTableColumn
caviHIntEgrRcvClp1Cells = _CaviHIntEgrRcvClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 2, 1, 20),
    _CaviHIntEgrRcvClp1Cells_Type()
)
caviHIntEgrRcvClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviHIntEgrRcvClp1Cells.setStatus("current")
_CaviHIntEgrClp0DiscCells_Type = Counter64
_CaviHIntEgrClp0DiscCells_Object = MibTableColumn
caviHIntEgrClp0DiscCells = _CaviHIntEgrClp0DiscCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 2, 1, 21),
    _CaviHIntEgrClp0DiscCells_Type()
)
caviHIntEgrClp0DiscCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviHIntEgrClp0DiscCells.setStatus("current")
_CaviHIntEgrClp1DiscCells_Type = Counter64
_CaviHIntEgrClp1DiscCells_Object = MibTableColumn
caviHIntEgrClp1DiscCells = _CaviHIntEgrClp1DiscCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 2, 1, 22),
    _CaviHIntEgrClp1DiscCells_Type()
)
caviHIntEgrClp1DiscCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviHIntEgrClp1DiscCells.setStatus("current")
_CaviHIntEgrXmtClp0Cells_Type = Counter64
_CaviHIntEgrXmtClp0Cells_Object = MibTableColumn
caviHIntEgrXmtClp0Cells = _CaviHIntEgrXmtClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 2, 1, 23),
    _CaviHIntEgrXmtClp0Cells_Type()
)
caviHIntEgrXmtClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviHIntEgrXmtClp0Cells.setStatus("current")
_CaviHIntEgrXmtClp1Cells_Type = Counter64
_CaviHIntEgrXmtClp1Cells_Object = MibTableColumn
caviHIntEgrXmtClp1Cells = _CaviHIntEgrXmtClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 2, 1, 24),
    _CaviHIntEgrXmtClp1Cells_Type()
)
caviHIntEgrXmtClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviHIntEgrXmtClp1Cells.setStatus("current")
_CaviStatIngressTable_Object = MibTable
caviStatIngressTable = _CaviStatIngressTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 3)
)
if mibBuilder.loadTexts:
    caviStatIngressTable.setStatus("current")
_CaviStatIngressEntry_Object = MibTableRow
caviStatIngressEntry = _CaviStatIngressEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 3, 1)
)
caviStatIngressEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    caviStatIngressEntry.setStatus("current")
_CaviIngRcvClp0Cells_Type = Counter32
_CaviIngRcvClp0Cells_Object = MibTableColumn
caviIngRcvClp0Cells = _CaviIngRcvClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 3, 1, 1),
    _CaviIngRcvClp0Cells_Type()
)
caviIngRcvClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviIngRcvClp0Cells.setStatus("current")
_CaviIngRcvClp1Cells_Type = Counter32
_CaviIngRcvClp1Cells_Object = MibTableColumn
caviIngRcvClp1Cells = _CaviIngRcvClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 3, 1, 2),
    _CaviIngRcvClp1Cells_Type()
)
caviIngRcvClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviIngRcvClp1Cells.setStatus("current")
_CaviIngClp0DiscCells_Type = Counter32
_CaviIngClp0DiscCells_Object = MibTableColumn
caviIngClp0DiscCells = _CaviIngClp0DiscCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 3, 1, 3),
    _CaviIngClp0DiscCells_Type()
)
caviIngClp0DiscCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviIngClp0DiscCells.setStatus("current")
_CaviIngClp1DiscCells_Type = Counter32
_CaviIngClp1DiscCells_Object = MibTableColumn
caviIngClp1DiscCells = _CaviIngClp1DiscCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 3, 1, 4),
    _CaviIngClp1DiscCells_Type()
)
caviIngClp1DiscCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviIngClp1DiscCells.setStatus("current")
_CaviIngXmtClp0Cells_Type = Counter32
_CaviIngXmtClp0Cells_Object = MibTableColumn
caviIngXmtClp0Cells = _CaviIngXmtClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 3, 1, 5),
    _CaviIngXmtClp0Cells_Type()
)
caviIngXmtClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviIngXmtClp0Cells.setStatus("current")
_CaviIngXmtClp1Cells_Type = Counter32
_CaviIngXmtClp1Cells_Object = MibTableColumn
caviIngXmtClp1Cells = _CaviIngXmtClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 3, 1, 6),
    _CaviIngXmtClp1Cells_Type()
)
caviIngXmtClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviIngXmtClp1Cells.setStatus("current")
_CaviIngRcvOAMCells_Type = Counter32
_CaviIngRcvOAMCells_Object = MibTableColumn
caviIngRcvOAMCells = _CaviIngRcvOAMCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 3, 1, 7),
    _CaviIngRcvOAMCells_Type()
)
caviIngRcvOAMCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviIngRcvOAMCells.setStatus("current")
_CaviIngRMCells_Type = Counter32
_CaviIngRMCells_Object = MibTableColumn
caviIngRMCells = _CaviIngRMCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 3, 1, 8),
    _CaviIngRMCells_Type()
)
caviIngRMCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviIngRMCells.setStatus("current")
_CaviIngXmtEFCICells_Type = Counter32
_CaviIngXmtEFCICells_Object = MibTableColumn
caviIngXmtEFCICells = _CaviIngXmtEFCICells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 3, 1, 9),
    _CaviIngXmtEFCICells_Type()
)
caviIngXmtEFCICells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviIngXmtEFCICells.setStatus("current")
_CaviIngRcvEFCICells_Type = Counter32
_CaviIngRcvEFCICells_Object = MibTableColumn
caviIngRcvEFCICells = _CaviIngRcvEFCICells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 3, 1, 10),
    _CaviIngRcvEFCICells_Type()
)
caviIngRcvEFCICells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviIngRcvEFCICells.setStatus("current")
_CaviIngXmtOAMCells_Type = Counter32
_CaviIngXmtOAMCells_Object = MibTableColumn
caviIngXmtOAMCells = _CaviIngXmtOAMCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 3, 1, 11),
    _CaviIngXmtOAMCells_Type()
)
caviIngXmtOAMCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviIngXmtOAMCells.setStatus("current")
_CaviHIngRcvClp0Cells_Type = Counter64
_CaviHIngRcvClp0Cells_Object = MibTableColumn
caviHIngRcvClp0Cells = _CaviHIngRcvClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 3, 1, 12),
    _CaviHIngRcvClp0Cells_Type()
)
caviHIngRcvClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviHIngRcvClp0Cells.setStatus("current")
_CaviHIngRcvClp1Cells_Type = Counter64
_CaviHIngRcvClp1Cells_Object = MibTableColumn
caviHIngRcvClp1Cells = _CaviHIngRcvClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 3, 1, 13),
    _CaviHIngRcvClp1Cells_Type()
)
caviHIngRcvClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviHIngRcvClp1Cells.setStatus("current")
_CaviHighIngRcvClp0Cells_Type = Counter32
_CaviHighIngRcvClp0Cells_Object = MibTableColumn
caviHighIngRcvClp0Cells = _CaviHighIngRcvClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 3, 1, 14),
    _CaviHighIngRcvClp0Cells_Type()
)
caviHighIngRcvClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviHighIngRcvClp0Cells.setStatus("current")
_CaviHighIngRcvClp1Cells_Type = Counter32
_CaviHighIngRcvClp1Cells_Object = MibTableColumn
caviHighIngRcvClp1Cells = _CaviHighIngRcvClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 3, 1, 15),
    _CaviHighIngRcvClp1Cells_Type()
)
caviHighIngRcvClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviHighIngRcvClp1Cells.setStatus("current")
_CaviHighIngClp0DiscCells_Type = Counter32
_CaviHighIngClp0DiscCells_Object = MibTableColumn
caviHighIngClp0DiscCells = _CaviHighIngClp0DiscCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 3, 1, 16),
    _CaviHighIngClp0DiscCells_Type()
)
caviHighIngClp0DiscCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviHighIngClp0DiscCells.setStatus("current")
_CaviHighIngClp1DiscCells_Type = Counter32
_CaviHighIngClp1DiscCells_Object = MibTableColumn
caviHighIngClp1DiscCells = _CaviHighIngClp1DiscCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 3, 1, 17),
    _CaviHighIngClp1DiscCells_Type()
)
caviHighIngClp1DiscCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviHighIngClp1DiscCells.setStatus("current")
_CaviHighIngXmtClp0Cells_Type = Counter32
_CaviHighIngXmtClp0Cells_Object = MibTableColumn
caviHighIngXmtClp0Cells = _CaviHighIngXmtClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 3, 1, 18),
    _CaviHighIngXmtClp0Cells_Type()
)
caviHighIngXmtClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviHighIngXmtClp0Cells.setStatus("current")
_CaviHighIngXmtClp1Cells_Type = Counter32
_CaviHighIngXmtClp1Cells_Object = MibTableColumn
caviHighIngXmtClp1Cells = _CaviHighIngXmtClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 3, 1, 19),
    _CaviHighIngXmtClp1Cells_Type()
)
caviHighIngXmtClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviHighIngXmtClp1Cells.setStatus("current")
_CaviHIngClp0DiscCells_Type = Counter64
_CaviHIngClp0DiscCells_Object = MibTableColumn
caviHIngClp0DiscCells = _CaviHIngClp0DiscCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 3, 1, 20),
    _CaviHIngClp0DiscCells_Type()
)
caviHIngClp0DiscCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviHIngClp0DiscCells.setStatus("current")
_CaviHIngClp1DiscCells_Type = Counter64
_CaviHIngClp1DiscCells_Object = MibTableColumn
caviHIngClp1DiscCells = _CaviHIngClp1DiscCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 3, 1, 21),
    _CaviHIngClp1DiscCells_Type()
)
caviHIngClp1DiscCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviHIngClp1DiscCells.setStatus("current")
_CaviHIngXmtClp0Cells_Type = Counter64
_CaviHIngXmtClp0Cells_Object = MibTableColumn
caviHIngXmtClp0Cells = _CaviHIngXmtClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 3, 1, 22),
    _CaviHIngXmtClp0Cells_Type()
)
caviHIngXmtClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviHIngXmtClp0Cells.setStatus("current")
_CaviHIngXmtClp1Cells_Type = Counter64
_CaviHIngXmtClp1Cells_Object = MibTableColumn
caviHIngXmtClp1Cells = _CaviHIngXmtClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 3, 1, 23),
    _CaviHIngXmtClp1Cells_Type()
)
caviHIngXmtClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviHIngXmtClp1Cells.setStatus("current")
_CaviIngressIntervalTable_Object = MibTable
caviIngressIntervalTable = _CaviIngressIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 4)
)
if mibBuilder.loadTexts:
    caviIngressIntervalTable.setStatus("current")
_CaviIngressIntervalEntry_Object = MibTableRow
caviIngressIntervalEntry = _CaviIngressIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 4, 1)
)
caviIngressIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-ATM-VIRTUAL-IF-MIB", "caviIngressIntervalNumber"),
)
if mibBuilder.loadTexts:
    caviIngressIntervalEntry.setStatus("current")


class _CaviIngressIntervalNumber_Type(Unsigned32):
    """Custom type caviIngressIntervalNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_CaviIngressIntervalNumber_Type.__name__ = "Unsigned32"
_CaviIngressIntervalNumber_Object = MibTableColumn
caviIngressIntervalNumber = _CaviIngressIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 4, 1, 1),
    _CaviIngressIntervalNumber_Type()
)
caviIngressIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    caviIngressIntervalNumber.setStatus("current")
_CaviIntIngRcvClp0Cells_Type = Counter32
_CaviIntIngRcvClp0Cells_Object = MibTableColumn
caviIntIngRcvClp0Cells = _CaviIntIngRcvClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 4, 1, 2),
    _CaviIntIngRcvClp0Cells_Type()
)
caviIntIngRcvClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviIntIngRcvClp0Cells.setStatus("current")
_CaviIntIngRcvClp1Cells_Type = Counter32
_CaviIntIngRcvClp1Cells_Object = MibTableColumn
caviIntIngRcvClp1Cells = _CaviIntIngRcvClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 4, 1, 3),
    _CaviIntIngRcvClp1Cells_Type()
)
caviIntIngRcvClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviIntIngRcvClp1Cells.setStatus("current")
_CaviIntIngClp0DiscCells_Type = Counter32
_CaviIntIngClp0DiscCells_Object = MibTableColumn
caviIntIngClp0DiscCells = _CaviIntIngClp0DiscCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 4, 1, 4),
    _CaviIntIngClp0DiscCells_Type()
)
caviIntIngClp0DiscCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviIntIngClp0DiscCells.setStatus("current")
_CaviIntIngClp1DiscCells_Type = Counter32
_CaviIntIngClp1DiscCells_Object = MibTableColumn
caviIntIngClp1DiscCells = _CaviIntIngClp1DiscCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 4, 1, 5),
    _CaviIntIngClp1DiscCells_Type()
)
caviIntIngClp1DiscCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviIntIngClp1DiscCells.setStatus("current")
_CaviIntIngXmtClp0Cells_Type = Counter32
_CaviIntIngXmtClp0Cells_Object = MibTableColumn
caviIntIngXmtClp0Cells = _CaviIntIngXmtClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 4, 1, 6),
    _CaviIntIngXmtClp0Cells_Type()
)
caviIntIngXmtClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviIntIngXmtClp0Cells.setStatus("current")
_CaviIntIngXmtClp1Cells_Type = Counter32
_CaviIntIngXmtClp1Cells_Object = MibTableColumn
caviIntIngXmtClp1Cells = _CaviIntIngXmtClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 4, 1, 7),
    _CaviIntIngXmtClp1Cells_Type()
)
caviIntIngXmtClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviIntIngXmtClp1Cells.setStatus("current")
_CaviIntIngRcvOAMCells_Type = Counter32
_CaviIntIngRcvOAMCells_Object = MibTableColumn
caviIntIngRcvOAMCells = _CaviIntIngRcvOAMCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 4, 1, 8),
    _CaviIntIngRcvOAMCells_Type()
)
caviIntIngRcvOAMCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviIntIngRcvOAMCells.setStatus("current")
_CaviIntIngRMCells_Type = Counter32
_CaviIntIngRMCells_Object = MibTableColumn
caviIntIngRMCells = _CaviIntIngRMCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 4, 1, 9),
    _CaviIntIngRMCells_Type()
)
caviIntIngRMCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviIntIngRMCells.setStatus("current")
_CaviIntIngXmtEFCICells_Type = Counter32
_CaviIntIngXmtEFCICells_Object = MibTableColumn
caviIntIngXmtEFCICells = _CaviIntIngXmtEFCICells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 4, 1, 10),
    _CaviIntIngXmtEFCICells_Type()
)
caviIntIngXmtEFCICells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviIntIngXmtEFCICells.setStatus("current")
_CaviIntIngRcvEFCICells_Type = Counter32
_CaviIntIngRcvEFCICells_Object = MibTableColumn
caviIntIngRcvEFCICells = _CaviIntIngRcvEFCICells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 4, 1, 11),
    _CaviIntIngRcvEFCICells_Type()
)
caviIntIngRcvEFCICells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviIntIngRcvEFCICells.setStatus("current")
_CaviIntIngXmtOAMCells_Type = Counter32
_CaviIntIngXmtOAMCells_Object = MibTableColumn
caviIntIngXmtOAMCells = _CaviIntIngXmtOAMCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 4, 1, 12),
    _CaviIntIngXmtOAMCells_Type()
)
caviIntIngXmtOAMCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviIntIngXmtOAMCells.setStatus("current")
_CaviHighIntIngRcvClp0Cells_Type = Counter32
_CaviHighIntIngRcvClp0Cells_Object = MibTableColumn
caviHighIntIngRcvClp0Cells = _CaviHighIntIngRcvClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 4, 1, 13),
    _CaviHighIntIngRcvClp0Cells_Type()
)
caviHighIntIngRcvClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviHighIntIngRcvClp0Cells.setStatus("current")
_CaviHighIntIngRcvClp1Cells_Type = Counter32
_CaviHighIntIngRcvClp1Cells_Object = MibTableColumn
caviHighIntIngRcvClp1Cells = _CaviHighIntIngRcvClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 4, 1, 14),
    _CaviHighIntIngRcvClp1Cells_Type()
)
caviHighIntIngRcvClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviHighIntIngRcvClp1Cells.setStatus("current")
_CaviHighIntIngClp0DiscCells_Type = Counter32
_CaviHighIntIngClp0DiscCells_Object = MibTableColumn
caviHighIntIngClp0DiscCells = _CaviHighIntIngClp0DiscCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 4, 1, 15),
    _CaviHighIntIngClp0DiscCells_Type()
)
caviHighIntIngClp0DiscCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviHighIntIngClp0DiscCells.setStatus("current")
_CaviHighIntIngClp1DiscCells_Type = Counter32
_CaviHighIntIngClp1DiscCells_Object = MibTableColumn
caviHighIntIngClp1DiscCells = _CaviHighIntIngClp1DiscCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 4, 1, 16),
    _CaviHighIntIngClp1DiscCells_Type()
)
caviHighIntIngClp1DiscCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviHighIntIngClp1DiscCells.setStatus("current")
_CaviHighIntIngXmtClp0Cells_Type = Counter32
_CaviHighIntIngXmtClp0Cells_Object = MibTableColumn
caviHighIntIngXmtClp0Cells = _CaviHighIntIngXmtClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 4, 1, 17),
    _CaviHighIntIngXmtClp0Cells_Type()
)
caviHighIntIngXmtClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviHighIntIngXmtClp0Cells.setStatus("current")
_CaviHighIntIngXmtClp1Cells_Type = Counter32
_CaviHighIntIngXmtClp1Cells_Object = MibTableColumn
caviHighIntIngXmtClp1Cells = _CaviHighIntIngXmtClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 4, 1, 18),
    _CaviHighIntIngXmtClp1Cells_Type()
)
caviHighIntIngXmtClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviHighIntIngXmtClp1Cells.setStatus("current")
_CaviHIntIngRcvClp0Cells_Type = Counter64
_CaviHIntIngRcvClp0Cells_Object = MibTableColumn
caviHIntIngRcvClp0Cells = _CaviHIntIngRcvClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 4, 1, 19),
    _CaviHIntIngRcvClp0Cells_Type()
)
caviHIntIngRcvClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviHIntIngRcvClp0Cells.setStatus("current")
_CaviHIntIngRcvClp1Cells_Type = Counter64
_CaviHIntIngRcvClp1Cells_Object = MibTableColumn
caviHIntIngRcvClp1Cells = _CaviHIntIngRcvClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 4, 1, 20),
    _CaviHIntIngRcvClp1Cells_Type()
)
caviHIntIngRcvClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviHIntIngRcvClp1Cells.setStatus("current")
_CaviHIntIngClp0DiscCells_Type = Counter64
_CaviHIntIngClp0DiscCells_Object = MibTableColumn
caviHIntIngClp0DiscCells = _CaviHIntIngClp0DiscCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 4, 1, 21),
    _CaviHIntIngClp0DiscCells_Type()
)
caviHIntIngClp0DiscCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviHIntIngClp0DiscCells.setStatus("current")
_CaviHIntIngClp1DiscCells_Type = Counter64
_CaviHIntIngClp1DiscCells_Object = MibTableColumn
caviHIntIngClp1DiscCells = _CaviHIntIngClp1DiscCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 4, 1, 22),
    _CaviHIntIngClp1DiscCells_Type()
)
caviHIntIngClp1DiscCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviHIntIngClp1DiscCells.setStatus("current")
_CaviHIntIngXmtClp0Cells_Type = Counter64
_CaviHIntIngXmtClp0Cells_Object = MibTableColumn
caviHIntIngXmtClp0Cells = _CaviHIntIngXmtClp0Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 4, 1, 23),
    _CaviHIntIngXmtClp0Cells_Type()
)
caviHIntIngXmtClp0Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviHIntIngXmtClp0Cells.setStatus("current")
_CaviHIntIngXmtClp1Cells_Type = Counter64
_CaviHIntIngXmtClp1Cells_Object = MibTableColumn
caviHIntIngXmtClp1Cells = _CaviHIntIngXmtClp1Cells_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 1, 2, 4, 1, 24),
    _CaviHIntIngXmtClp1Cells_Type()
)
caviHIntIngXmtClp1Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    caviHIntIngXmtClp1Cells.setStatus("current")
_CaviMIBConformance_ObjectIdentity = ObjectIdentity
caviMIBConformance = _CaviMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 3)
)
_CaviMIBCompliances_ObjectIdentity = ObjectIdentity
caviMIBCompliances = _CaviMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 3, 1)
)
_CaviMIBGroups_ObjectIdentity = ObjectIdentity
caviMIBGroups = _CaviMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 3, 2)
)

# Managed Objects groups

caviMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 3, 2, 1)
)
caviMIBGroup.setObjects(
      *(("CISCO-ATM-VIRTUAL-IF-MIB", "caviPhyIfIndex"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviViIfIndex"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviMinRate"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviMaxRate"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviFileId"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviIfType"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviVpiNum"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviRowStatus"))
)
if mibBuilder.loadTexts:
    caviMIBGroup.setStatus("deprecated")

caviEgressStatMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 3, 2, 2)
)
caviEgressStatMIBGroup.setObjects(
      *(("CISCO-ATM-VIRTUAL-IF-MIB", "caviEgrRcvClp0Cells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviEgrRcvClp1Cells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviEgrClp0DiscCells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviEgrClp1DiscCells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviEgrXmtClp0Cells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviEgrXmtClp1Cells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviEgrRcvOAMCells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviEgrRMCells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviEgrXmtEFCICells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviEgrRcvEFCICells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviEgrXmtOAMCells"))
)
if mibBuilder.loadTexts:
    caviEgressStatMIBGroup.setStatus("deprecated")

caviEgressHighSpeedStatMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 3, 2, 3)
)
caviEgressHighSpeedStatMIBGroup.setObjects(
      *(("CISCO-ATM-VIRTUAL-IF-MIB", "caviHEgrXmtClp0Cells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviHEgrXmtClp1Cells"))
)
if mibBuilder.loadTexts:
    caviEgressHighSpeedStatMIBGroup.setStatus("deprecated")

caviEgressIntervalMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 3, 2, 4)
)
caviEgressIntervalMIBGroup.setObjects(
      *(("CISCO-ATM-VIRTUAL-IF-MIB", "caviEgressIntervalNumber"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviIntEgrRcvClp0Cells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviIntEgrRcvClp1Cells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviIntEgrClp0DiscCells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviIntEgrClp1DiscCells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviIntEgrXmtClp0Cells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviIntEgrXmtClp1Cells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviIntEgrRcvOAMCells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviIntEgrRMCells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviIntEgrXmtEFCICells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviIntEgrRcvEFCICells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviIntEgrXmtOAMCells"))
)
if mibBuilder.loadTexts:
    caviEgressIntervalMIBGroup.setStatus("deprecated")

caviIngressStatMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 3, 2, 5)
)
caviIngressStatMIBGroup.setObjects(
      *(("CISCO-ATM-VIRTUAL-IF-MIB", "caviIngRcvClp0Cells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviIngRcvClp1Cells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviIngClp0DiscCells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviIngClp1DiscCells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviIngXmtClp0Cells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviIngXmtClp1Cells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviIngRcvOAMCells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviIngRMCells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviIngXmtEFCICells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviIngRcvEFCICells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviIngXmtOAMCells"))
)
if mibBuilder.loadTexts:
    caviIngressStatMIBGroup.setStatus("deprecated")

caviIngressHighSpeedStatMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 3, 2, 6)
)
caviIngressHighSpeedStatMIBGroup.setObjects(
      *(("CISCO-ATM-VIRTUAL-IF-MIB", "caviHIngRcvClp0Cells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviHIngRcvClp1Cells"))
)
if mibBuilder.loadTexts:
    caviIngressHighSpeedStatMIBGroup.setStatus("deprecated")

caviMIBGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 3, 2, 7)
)
caviMIBGroupRev1.setObjects(
      *(("CISCO-ATM-VIRTUAL-IF-MIB", "caviPhyIfIndex"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviViIfIndex"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviMinRate"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviMaxRate"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviFileId"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviIfType"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviVpiNum"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviRowStatus"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviMinVpiNum"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviMaxVpiNum"))
)
if mibBuilder.loadTexts:
    caviMIBGroupRev1.setStatus("current")

caviEgressStatMIBGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 3, 2, 8)
)
caviEgressStatMIBGroup1.setObjects(
      *(("CISCO-ATM-VIRTUAL-IF-MIB", "caviEgrRcvClp0Cells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviEgrRcvClp1Cells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviEgrClp0DiscCells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviEgrClp1DiscCells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviEgrXmtClp0Cells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviEgrXmtClp1Cells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviEgrRcvOAMCells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviEgrRMCells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviEgrXmtEFCICells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviEgrRcvEFCICells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviEgrXmtOAMCells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviHighEgrRcvClp0Cells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviHighEgrRcvClp1Cells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviHighEgrClp0DiscCells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviHighEgrClp1DiscCells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviHighEgrXmtClp0Cells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviHighEgrXmtClp1Cells"))
)
if mibBuilder.loadTexts:
    caviEgressStatMIBGroup1.setStatus("current")

caviEgressHighSpeedStatMIBGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 3, 2, 9)
)
caviEgressHighSpeedStatMIBGroup1.setObjects(
      *(("CISCO-ATM-VIRTUAL-IF-MIB", "caviHEgrXmtClp0Cells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviHEgrXmtClp1Cells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviHEgrRcvClp0Cells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviHEgrRcvClp1Cells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviHEgrClp0DiscCells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviHEgrClp1DiscCells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviHIntEgrRcvClp0Cells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviHIntEgrRcvClp1Cells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviHIntEgrClp0DiscCells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviHIntEgrClp1DiscCells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviHIntEgrXmtClp0Cells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviHIntEgrXmtClp1Cells"))
)
if mibBuilder.loadTexts:
    caviEgressHighSpeedStatMIBGroup1.setStatus("current")

caviEgressIntervalMIBGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 3, 2, 10)
)
caviEgressIntervalMIBGroup1.setObjects(
      *(("CISCO-ATM-VIRTUAL-IF-MIB", "caviEgressIntervalNumber"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviIntEgrRcvClp0Cells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviIntEgrRcvClp1Cells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviIntEgrClp0DiscCells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviIntEgrClp1DiscCells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviIntEgrXmtClp0Cells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviIntEgrXmtClp1Cells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviIntEgrRcvOAMCells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviIntEgrRMCells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviIntEgrXmtEFCICells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviIntEgrRcvEFCICells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviIntEgrXmtOAMCells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviHighIntEgrRcvClp0Cells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviHighIntEgrRcvClp1Cells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviHighIntEgrClp0DiscCells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviHighIntEgrClp1DiscCells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviHighIntEgrXmtClp0Cells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviHighIntEgrXmtClp1Cells"))
)
if mibBuilder.loadTexts:
    caviEgressIntervalMIBGroup1.setStatus("current")

caviIngressStatMIBGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 3, 2, 11)
)
caviIngressStatMIBGroup1.setObjects(
      *(("CISCO-ATM-VIRTUAL-IF-MIB", "caviIngRcvClp0Cells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviIngRcvClp1Cells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviIngClp0DiscCells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviIngClp1DiscCells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviIngXmtClp0Cells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviIngXmtClp1Cells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviIngRcvOAMCells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviIngRMCells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviIngXmtEFCICells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviIngRcvEFCICells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviIngXmtOAMCells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviHighIngRcvClp0Cells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviHighIngRcvClp1Cells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviHighIngClp0DiscCells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviHighIngClp1DiscCells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviHighIngXmtClp0Cells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviHighIngXmtClp1Cells"))
)
if mibBuilder.loadTexts:
    caviIngressStatMIBGroup1.setStatus("current")

caviIngHighSpeedStatMIBGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 3, 2, 12)
)
caviIngHighSpeedStatMIBGroup1.setObjects(
      *(("CISCO-ATM-VIRTUAL-IF-MIB", "caviHIngRcvClp0Cells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviHIngRcvClp1Cells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviHIngClp0DiscCells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviHIngClp1DiscCells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviHIngXmtClp0Cells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviHIngXmtClp1Cells"))
)
if mibBuilder.loadTexts:
    caviIngHighSpeedStatMIBGroup1.setStatus("deprecated")

caviIngressIntervalStatMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 3, 2, 13)
)
caviIngressIntervalStatMIBGroup.setObjects(
      *(("CISCO-ATM-VIRTUAL-IF-MIB", "caviIntIngRcvClp0Cells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviIntIngRcvClp1Cells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviIntIngClp0DiscCells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviIntIngClp1DiscCells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviIntIngXmtClp0Cells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviIntIngXmtClp1Cells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviIntIngRcvOAMCells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviIntIngRMCells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviIntIngXmtEFCICells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviIntIngRcvEFCICells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviIntIngXmtOAMCells"))
)
if mibBuilder.loadTexts:
    caviIngressIntervalStatMIBGroup.setStatus("current")

caviIngHighSpeedStatMIBGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 3, 2, 14)
)
caviIngHighSpeedStatMIBGroup2.setObjects(
      *(("CISCO-ATM-VIRTUAL-IF-MIB", "caviHighIntIngRcvClp0Cells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviHighIntIngRcvClp1Cells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviHighIntIngClp0DiscCells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviHighIntIngClp1DiscCells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviHighIntIngXmtClp0Cells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviHighIntIngXmtClp1Cells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviHIngRcvClp0Cells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviHIngRcvClp1Cells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviHIngClp0DiscCells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviHIngClp1DiscCells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviHIngXmtClp0Cells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviHIngXmtClp1Cells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviHIntIngRcvClp0Cells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviHIntIngRcvClp1Cells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviHIntIngClp0DiscCells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviHIntIngClp1DiscCells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviHIntIngXmtClp0Cells"),
        ("CISCO-ATM-VIRTUAL-IF-MIB", "caviHIntIngXmtClp1Cells"))
)
if mibBuilder.loadTexts:
    caviIngHighSpeedStatMIBGroup2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

caviMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 3, 1, 1)
)
if mibBuilder.loadTexts:
    caviMIBCompliance.setStatus(
        "deprecated"
    )

caviMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 3, 1, 2)
)
if mibBuilder.loadTexts:
    caviMIBComplianceRev1.setStatus(
        "deprecated"
    )

caviMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 3, 1, 3)
)
if mibBuilder.loadTexts:
    caviMIBComplianceRev2.setStatus(
        "deprecated"
    )

caviMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 129, 3, 1, 4)
)
if mibBuilder.loadTexts:
    caviMIBComplianceRev3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ATM-VIRTUAL-IF-MIB",
    **{"ciscoAtmVirtualIfMIB": ciscoAtmVirtualIfMIB,
       "ciscoAtmVirtualIfMIBObjects": ciscoAtmVirtualIfMIBObjects,
       "caviConfig": caviConfig,
       "caviTable": caviTable,
       "caviEntry": caviEntry,
       "caviIndex": caviIndex,
       "caviPhyIfIndex": caviPhyIfIndex,
       "caviViIfIndex": caviViIfIndex,
       "caviMinRate": caviMinRate,
       "caviMaxRate": caviMaxRate,
       "caviFileId": caviFileId,
       "caviIfType": caviIfType,
       "caviVpiNum": caviVpiNum,
       "caviRowStatus": caviRowStatus,
       "caviMinVpiNum": caviMinVpiNum,
       "caviMaxVpiNum": caviMaxVpiNum,
       "caviStatistics": caviStatistics,
       "caviStatEgressTable": caviStatEgressTable,
       "caviStatEgressEntry": caviStatEgressEntry,
       "caviEgrRcvClp0Cells": caviEgrRcvClp0Cells,
       "caviEgrRcvClp1Cells": caviEgrRcvClp1Cells,
       "caviEgrClp0DiscCells": caviEgrClp0DiscCells,
       "caviEgrClp1DiscCells": caviEgrClp1DiscCells,
       "caviEgrXmtClp0Cells": caviEgrXmtClp0Cells,
       "caviEgrXmtClp1Cells": caviEgrXmtClp1Cells,
       "caviEgrRcvOAMCells": caviEgrRcvOAMCells,
       "caviEgrRMCells": caviEgrRMCells,
       "caviEgrXmtEFCICells": caviEgrXmtEFCICells,
       "caviEgrRcvEFCICells": caviEgrRcvEFCICells,
       "caviEgrXmtOAMCells": caviEgrXmtOAMCells,
       "caviHEgrXmtClp0Cells": caviHEgrXmtClp0Cells,
       "caviHEgrXmtClp1Cells": caviHEgrXmtClp1Cells,
       "caviHighEgrRcvClp0Cells": caviHighEgrRcvClp0Cells,
       "caviHighEgrRcvClp1Cells": caviHighEgrRcvClp1Cells,
       "caviHighEgrClp0DiscCells": caviHighEgrClp0DiscCells,
       "caviHighEgrClp1DiscCells": caviHighEgrClp1DiscCells,
       "caviHighEgrXmtClp0Cells": caviHighEgrXmtClp0Cells,
       "caviHighEgrXmtClp1Cells": caviHighEgrXmtClp1Cells,
       "caviHEgrRcvClp0Cells": caviHEgrRcvClp0Cells,
       "caviHEgrRcvClp1Cells": caviHEgrRcvClp1Cells,
       "caviHEgrClp0DiscCells": caviHEgrClp0DiscCells,
       "caviHEgrClp1DiscCells": caviHEgrClp1DiscCells,
       "caviEgressIntervalTable": caviEgressIntervalTable,
       "caviEgressIntervalEntry": caviEgressIntervalEntry,
       "caviEgressIntervalNumber": caviEgressIntervalNumber,
       "caviIntEgrRcvClp0Cells": caviIntEgrRcvClp0Cells,
       "caviIntEgrRcvClp1Cells": caviIntEgrRcvClp1Cells,
       "caviIntEgrClp0DiscCells": caviIntEgrClp0DiscCells,
       "caviIntEgrClp1DiscCells": caviIntEgrClp1DiscCells,
       "caviIntEgrXmtClp0Cells": caviIntEgrXmtClp0Cells,
       "caviIntEgrXmtClp1Cells": caviIntEgrXmtClp1Cells,
       "caviIntEgrRcvOAMCells": caviIntEgrRcvOAMCells,
       "caviIntEgrRMCells": caviIntEgrRMCells,
       "caviIntEgrXmtEFCICells": caviIntEgrXmtEFCICells,
       "caviIntEgrRcvEFCICells": caviIntEgrRcvEFCICells,
       "caviIntEgrXmtOAMCells": caviIntEgrXmtOAMCells,
       "caviHighIntEgrRcvClp0Cells": caviHighIntEgrRcvClp0Cells,
       "caviHighIntEgrRcvClp1Cells": caviHighIntEgrRcvClp1Cells,
       "caviHighIntEgrClp0DiscCells": caviHighIntEgrClp0DiscCells,
       "caviHighIntEgrClp1DiscCells": caviHighIntEgrClp1DiscCells,
       "caviHighIntEgrXmtClp0Cells": caviHighIntEgrXmtClp0Cells,
       "caviHighIntEgrXmtClp1Cells": caviHighIntEgrXmtClp1Cells,
       "caviHIntEgrRcvClp0Cells": caviHIntEgrRcvClp0Cells,
       "caviHIntEgrRcvClp1Cells": caviHIntEgrRcvClp1Cells,
       "caviHIntEgrClp0DiscCells": caviHIntEgrClp0DiscCells,
       "caviHIntEgrClp1DiscCells": caviHIntEgrClp1DiscCells,
       "caviHIntEgrXmtClp0Cells": caviHIntEgrXmtClp0Cells,
       "caviHIntEgrXmtClp1Cells": caviHIntEgrXmtClp1Cells,
       "caviStatIngressTable": caviStatIngressTable,
       "caviStatIngressEntry": caviStatIngressEntry,
       "caviIngRcvClp0Cells": caviIngRcvClp0Cells,
       "caviIngRcvClp1Cells": caviIngRcvClp1Cells,
       "caviIngClp0DiscCells": caviIngClp0DiscCells,
       "caviIngClp1DiscCells": caviIngClp1DiscCells,
       "caviIngXmtClp0Cells": caviIngXmtClp0Cells,
       "caviIngXmtClp1Cells": caviIngXmtClp1Cells,
       "caviIngRcvOAMCells": caviIngRcvOAMCells,
       "caviIngRMCells": caviIngRMCells,
       "caviIngXmtEFCICells": caviIngXmtEFCICells,
       "caviIngRcvEFCICells": caviIngRcvEFCICells,
       "caviIngXmtOAMCells": caviIngXmtOAMCells,
       "caviHIngRcvClp0Cells": caviHIngRcvClp0Cells,
       "caviHIngRcvClp1Cells": caviHIngRcvClp1Cells,
       "caviHighIngRcvClp0Cells": caviHighIngRcvClp0Cells,
       "caviHighIngRcvClp1Cells": caviHighIngRcvClp1Cells,
       "caviHighIngClp0DiscCells": caviHighIngClp0DiscCells,
       "caviHighIngClp1DiscCells": caviHighIngClp1DiscCells,
       "caviHighIngXmtClp0Cells": caviHighIngXmtClp0Cells,
       "caviHighIngXmtClp1Cells": caviHighIngXmtClp1Cells,
       "caviHIngClp0DiscCells": caviHIngClp0DiscCells,
       "caviHIngClp1DiscCells": caviHIngClp1DiscCells,
       "caviHIngXmtClp0Cells": caviHIngXmtClp0Cells,
       "caviHIngXmtClp1Cells": caviHIngXmtClp1Cells,
       "caviIngressIntervalTable": caviIngressIntervalTable,
       "caviIngressIntervalEntry": caviIngressIntervalEntry,
       "caviIngressIntervalNumber": caviIngressIntervalNumber,
       "caviIntIngRcvClp0Cells": caviIntIngRcvClp0Cells,
       "caviIntIngRcvClp1Cells": caviIntIngRcvClp1Cells,
       "caviIntIngClp0DiscCells": caviIntIngClp0DiscCells,
       "caviIntIngClp1DiscCells": caviIntIngClp1DiscCells,
       "caviIntIngXmtClp0Cells": caviIntIngXmtClp0Cells,
       "caviIntIngXmtClp1Cells": caviIntIngXmtClp1Cells,
       "caviIntIngRcvOAMCells": caviIntIngRcvOAMCells,
       "caviIntIngRMCells": caviIntIngRMCells,
       "caviIntIngXmtEFCICells": caviIntIngXmtEFCICells,
       "caviIntIngRcvEFCICells": caviIntIngRcvEFCICells,
       "caviIntIngXmtOAMCells": caviIntIngXmtOAMCells,
       "caviHighIntIngRcvClp0Cells": caviHighIntIngRcvClp0Cells,
       "caviHighIntIngRcvClp1Cells": caviHighIntIngRcvClp1Cells,
       "caviHighIntIngClp0DiscCells": caviHighIntIngClp0DiscCells,
       "caviHighIntIngClp1DiscCells": caviHighIntIngClp1DiscCells,
       "caviHighIntIngXmtClp0Cells": caviHighIntIngXmtClp0Cells,
       "caviHighIntIngXmtClp1Cells": caviHighIntIngXmtClp1Cells,
       "caviHIntIngRcvClp0Cells": caviHIntIngRcvClp0Cells,
       "caviHIntIngRcvClp1Cells": caviHIntIngRcvClp1Cells,
       "caviHIntIngClp0DiscCells": caviHIntIngClp0DiscCells,
       "caviHIntIngClp1DiscCells": caviHIntIngClp1DiscCells,
       "caviHIntIngXmtClp0Cells": caviHIntIngXmtClp0Cells,
       "caviHIntIngXmtClp1Cells": caviHIntIngXmtClp1Cells,
       "caviMIBConformance": caviMIBConformance,
       "caviMIBCompliances": caviMIBCompliances,
       "caviMIBCompliance": caviMIBCompliance,
       "caviMIBComplianceRev1": caviMIBComplianceRev1,
       "caviMIBComplianceRev2": caviMIBComplianceRev2,
       "caviMIBComplianceRev3": caviMIBComplianceRev3,
       "caviMIBGroups": caviMIBGroups,
       "caviMIBGroup": caviMIBGroup,
       "caviEgressStatMIBGroup": caviEgressStatMIBGroup,
       "caviEgressHighSpeedStatMIBGroup": caviEgressHighSpeedStatMIBGroup,
       "caviEgressIntervalMIBGroup": caviEgressIntervalMIBGroup,
       "caviIngressStatMIBGroup": caviIngressStatMIBGroup,
       "caviIngressHighSpeedStatMIBGroup": caviIngressHighSpeedStatMIBGroup,
       "caviMIBGroupRev1": caviMIBGroupRev1,
       "caviEgressStatMIBGroup1": caviEgressStatMIBGroup1,
       "caviEgressHighSpeedStatMIBGroup1": caviEgressHighSpeedStatMIBGroup1,
       "caviEgressIntervalMIBGroup1": caviEgressIntervalMIBGroup1,
       "caviIngressStatMIBGroup1": caviIngressStatMIBGroup1,
       "caviIngHighSpeedStatMIBGroup1": caviIngHighSpeedStatMIBGroup1,
       "caviIngressIntervalStatMIBGroup": caviIngressIntervalStatMIBGroup,
       "caviIngHighSpeedStatMIBGroup2": caviIngHighSpeedStatMIBGroup2}
)
