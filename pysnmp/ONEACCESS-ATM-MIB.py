# SNMP MIB module (ONEACCESS-ATM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ONEACCESS-ATM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:34:48 2024
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

(AtmVcIdentifier,
 AtmVpIdentifier) = mibBuilder.importSymbols(
    "ATM-TC-MIB",
    "AtmVcIdentifier",
    "AtmVpIdentifier")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(oacExpIMAtmStatistics,
 oacMIBModules) = mibBuilder.importSymbols(
    "ONEACCESS-GLOBAL-REG",
    "oacExpIMAtmStatistics",
    "oacMIBModules")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

oacAtmMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 100, 667)
)
oacAtmMIBModule.setRevisions(
        ("2011-10-27 00:00",
         "2010-07-08 00:01")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OacAtmStatObjects_ObjectIdentity = ObjectIdentity
oacAtmStatObjects = _OacAtmStatObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 1, 1)
)
_OacAtmChannelTable_Object = MibTable
oacAtmChannelTable = _OacAtmChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    oacAtmChannelTable.setStatus("current")
_OacAtmChannelEntry_Object = MibTableRow
oacAtmChannelEntry = _OacAtmChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 1, 1, 1, 1)
)
oacAtmChannelEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ONEACCESS-ATM-MIB", "oacAtmChanVpi"),
    (0, "ONEACCESS-ATM-MIB", "oacAtmChanVci"),
)
if mibBuilder.loadTexts:
    oacAtmChannelEntry.setStatus("current")
_OacAtmChanVpi_Type = AtmVpIdentifier
_OacAtmChanVpi_Object = MibTableColumn
oacAtmChanVpi = _OacAtmChanVpi_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 1, 1, 1, 1, 1),
    _OacAtmChanVpi_Type()
)
oacAtmChanVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oacAtmChanVpi.setStatus("current")
_OacAtmChanVci_Type = AtmVcIdentifier
_OacAtmChanVci_Object = MibTableColumn
oacAtmChanVci = _OacAtmChanVci_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 1, 1, 1, 1, 2),
    _OacAtmChanVci_Type()
)
oacAtmChanVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oacAtmChanVci.setStatus("current")
_OacAtmChanTxBytes_Type = Counter32
_OacAtmChanTxBytes_Object = MibTableColumn
oacAtmChanTxBytes = _OacAtmChanTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 1, 1, 1, 1, 3),
    _OacAtmChanTxBytes_Type()
)
oacAtmChanTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAtmChanTxBytes.setStatus("current")
_OacAtmChanTxCells_Type = Counter32
_OacAtmChanTxCells_Object = MibTableColumn
oacAtmChanTxCells = _OacAtmChanTxCells_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 1, 1, 1, 1, 4),
    _OacAtmChanTxCells_Type()
)
oacAtmChanTxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAtmChanTxCells.setStatus("current")
_OacAtmChanRxBytes_Type = Counter32
_OacAtmChanRxBytes_Object = MibTableColumn
oacAtmChanRxBytes = _OacAtmChanRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 1, 1, 1, 1, 5),
    _OacAtmChanRxBytes_Type()
)
oacAtmChanRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAtmChanRxBytes.setStatus("current")
_OacAtmChanRxCells_Type = Counter32
_OacAtmChanRxCells_Object = MibTableColumn
oacAtmChanRxCells = _OacAtmChanRxCells_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 1, 1, 1, 1, 6),
    _OacAtmChanRxCells_Type()
)
oacAtmChanRxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAtmChanRxCells.setStatus("current")
_OacAtmChanRxErrors_Type = Counter32
_OacAtmChanRxErrors_Object = MibTableColumn
oacAtmChanRxErrors = _OacAtmChanRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 1, 1, 1, 1, 7),
    _OacAtmChanRxErrors_Type()
)
oacAtmChanRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAtmChanRxErrors.setStatus("current")
_OacAtmChanTxOverflows_Type = Counter32
_OacAtmChanTxOverflows_Object = MibTableColumn
oacAtmChanTxOverflows = _OacAtmChanTxOverflows_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 1, 1, 1, 1, 8),
    _OacAtmChanTxOverflows_Type()
)
oacAtmChanTxOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAtmChanTxOverflows.setStatus("current")
_OacAtmAal0ChannelGlobalStatTable_Object = MibTable
oacAtmAal0ChannelGlobalStatTable = _OacAtmAal0ChannelGlobalStatTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    oacAtmAal0ChannelGlobalStatTable.setStatus("current")
_OacAtmAal0ChannelGlobalStatEntry_Object = MibTableRow
oacAtmAal0ChannelGlobalStatEntry = _OacAtmAal0ChannelGlobalStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 1, 1, 2, 1)
)
oacAtmAal0ChannelGlobalStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ONEACCESS-ATM-MIB", "oacAtmChanVpi"),
    (0, "ONEACCESS-ATM-MIB", "oacAtmChanVci"),
)
if mibBuilder.loadTexts:
    oacAtmAal0ChannelGlobalStatEntry.setStatus("current")
_OacAtmAal0ChanRxCellsDiscarded_Type = Counter32
_OacAtmAal0ChanRxCellsDiscarded_Object = MibTableColumn
oacAtmAal0ChanRxCellsDiscarded = _OacAtmAal0ChanRxCellsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 1, 1, 2, 1, 1),
    _OacAtmAal0ChanRxCellsDiscarded_Type()
)
oacAtmAal0ChanRxCellsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAtmAal0ChanRxCellsDiscarded.setStatus("current")
_OacAtmAal1ChannelGlobalStatTable_Object = MibTable
oacAtmAal1ChannelGlobalStatTable = _OacAtmAal1ChannelGlobalStatTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    oacAtmAal1ChannelGlobalStatTable.setStatus("current")
_OacAtmAal1ChannelGlobalStatEntry_Object = MibTableRow
oacAtmAal1ChannelGlobalStatEntry = _OacAtmAal1ChannelGlobalStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 1, 1, 3, 1)
)
oacAtmAal1ChannelGlobalStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ONEACCESS-ATM-MIB", "oacAtmChanVpi"),
    (0, "ONEACCESS-ATM-MIB", "oacAtmChanVci"),
)
if mibBuilder.loadTexts:
    oacAtmAal1ChannelGlobalStatEntry.setStatus("current")
_OacAtmAal1ChanTxUnderflows_Type = Counter32
_OacAtmAal1ChanTxUnderflows_Object = MibTableColumn
oacAtmAal1ChanTxUnderflows = _OacAtmAal1ChanTxUnderflows_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 1, 1, 3, 1, 1),
    _OacAtmAal1ChanTxUnderflows_Type()
)
oacAtmAal1ChanTxUnderflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAtmAal1ChanTxUnderflows.setStatus("current")
_OacAtmAal1ChanRxOverflows_Type = Counter32
_OacAtmAal1ChanRxOverflows_Object = MibTableColumn
oacAtmAal1ChanRxOverflows = _OacAtmAal1ChanRxOverflows_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 1, 1, 3, 1, 2),
    _OacAtmAal1ChanRxOverflows_Type()
)
oacAtmAal1ChanRxOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAtmAal1ChanRxOverflows.setStatus("current")
_OacAtmAal5ChannelGlobalStatTable_Object = MibTable
oacAtmAal5ChannelGlobalStatTable = _OacAtmAal5ChannelGlobalStatTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 1, 1, 4)
)
if mibBuilder.loadTexts:
    oacAtmAal5ChannelGlobalStatTable.setStatus("current")
_OacAtmAal5ChannelGlobalStatEntry_Object = MibTableRow
oacAtmAal5ChannelGlobalStatEntry = _OacAtmAal5ChannelGlobalStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 1, 1, 4, 1)
)
oacAtmAal5ChannelGlobalStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ONEACCESS-ATM-MIB", "oacAtmChanVpi"),
    (0, "ONEACCESS-ATM-MIB", "oacAtmChanVci"),
)
if mibBuilder.loadTexts:
    oacAtmAal5ChannelGlobalStatEntry.setStatus("current")
_OacAtmAal5ChanTxFrames_Type = Counter32
_OacAtmAal5ChanTxFrames_Object = MibTableColumn
oacAtmAal5ChanTxFrames = _OacAtmAal5ChanTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 1, 1, 4, 1, 1),
    _OacAtmAal5ChanTxFrames_Type()
)
oacAtmAal5ChanTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAtmAal5ChanTxFrames.setStatus("current")
_OacAtmAal5ChanRxFrames_Type = Counter32
_OacAtmAal5ChanRxFrames_Object = MibTableColumn
oacAtmAal5ChanRxFrames = _OacAtmAal5ChanRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 1, 1, 4, 1, 2),
    _OacAtmAal5ChanRxFrames_Type()
)
oacAtmAal5ChanRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAtmAal5ChanRxFrames.setStatus("current")
_OacAtmAal5ChanRxFramesDiscarded_Type = Counter32
_OacAtmAal5ChanRxFramesDiscarded_Object = MibTableColumn
oacAtmAal5ChanRxFramesDiscarded = _OacAtmAal5ChanRxFramesDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 1, 1, 4, 1, 3),
    _OacAtmAal5ChanRxFramesDiscarded_Type()
)
oacAtmAal5ChanRxFramesDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAtmAal5ChanRxFramesDiscarded.setStatus("current")
_OacAtmAal5ChanCrc32Errors_Type = Counter32
_OacAtmAal5ChanCrc32Errors_Object = MibTableColumn
oacAtmAal5ChanCrc32Errors = _OacAtmAal5ChanCrc32Errors_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 1, 1, 4, 1, 4),
    _OacAtmAal5ChanCrc32Errors_Type()
)
oacAtmAal5ChanCrc32Errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAtmAal5ChanCrc32Errors.setStatus("current")
_OacAtmAal5ChanLengthErrors_Type = Counter32
_OacAtmAal5ChanLengthErrors_Object = MibTableColumn
oacAtmAal5ChanLengthErrors = _OacAtmAal5ChanLengthErrors_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 1, 1, 4, 1, 5),
    _OacAtmAal5ChanLengthErrors_Type()
)
oacAtmAal5ChanLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAtmAal5ChanLengthErrors.setStatus("current")
_OacAtmAal5ChanReassemblyTimeouts_Type = Counter32
_OacAtmAal5ChanReassemblyTimeouts_Object = MibTableColumn
oacAtmAal5ChanReassemblyTimeouts = _OacAtmAal5ChanReassemblyTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 1, 1, 4, 1, 6),
    _OacAtmAal5ChanReassemblyTimeouts_Type()
)
oacAtmAal5ChanReassemblyTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAtmAal5ChanReassemblyTimeouts.setStatus("current")
_OacAtmPortStatTable_Object = MibTable
oacAtmPortStatTable = _OacAtmPortStatTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 1, 1, 5)
)
if mibBuilder.loadTexts:
    oacAtmPortStatTable.setStatus("current")
_OacAtmPortStatEntry_Object = MibTableRow
oacAtmPortStatEntry = _OacAtmPortStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 1, 1, 5, 1)
)
oacAtmPortStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    oacAtmPortStatEntry.setStatus("current")
_OacAtmPortTxCells_Type = Counter32
_OacAtmPortTxCells_Object = MibTableColumn
oacAtmPortTxCells = _OacAtmPortTxCells_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 1, 1, 5, 1, 1),
    _OacAtmPortTxCells_Type()
)
oacAtmPortTxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAtmPortTxCells.setStatus("current")
_OacAtmPortRxCells_Type = Counter32
_OacAtmPortRxCells_Object = MibTableColumn
oacAtmPortRxCells = _OacAtmPortRxCells_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 1, 1, 5, 1, 2),
    _OacAtmPortRxCells_Type()
)
oacAtmPortRxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAtmPortRxCells.setStatus("current")
_OacAtmPortRxCellsDiscarded_Type = Counter32
_OacAtmPortRxCellsDiscarded_Object = MibTableColumn
oacAtmPortRxCellsDiscarded = _OacAtmPortRxCellsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 1, 1, 5, 1, 3),
    _OacAtmPortRxCellsDiscarded_Type()
)
oacAtmPortRxCellsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAtmPortRxCellsDiscarded.setStatus("current")
_OacAtmPortHecErrors_Type = Counter32
_OacAtmPortHecErrors_Object = MibTableColumn
oacAtmPortHecErrors = _OacAtmPortHecErrors_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 1, 1, 5, 1, 4),
    _OacAtmPortHecErrors_Type()
)
oacAtmPortHecErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAtmPortHecErrors.setStatus("current")
_OacAtmAal5PortStatTable_Object = MibTable
oacAtmAal5PortStatTable = _OacAtmAal5PortStatTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 1, 1, 6)
)
if mibBuilder.loadTexts:
    oacAtmAal5PortStatTable.setStatus("current")
_OacAtmAal5PortStatEntry_Object = MibTableRow
oacAtmAal5PortStatEntry = _OacAtmAal5PortStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 1, 1, 6, 1)
)
oacAtmAal5PortStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    oacAtmAal5PortStatEntry.setStatus("current")
_OacAtmAal5PortTxBytes_Type = Counter32
_OacAtmAal5PortTxBytes_Object = MibTableColumn
oacAtmAal5PortTxBytes = _OacAtmAal5PortTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 1, 1, 6, 1, 1),
    _OacAtmAal5PortTxBytes_Type()
)
oacAtmAal5PortTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAtmAal5PortTxBytes.setStatus("current")
_OacAtmAal5PortTxFrames_Type = Counter32
_OacAtmAal5PortTxFrames_Object = MibTableColumn
oacAtmAal5PortTxFrames = _OacAtmAal5PortTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 1, 1, 6, 1, 2),
    _OacAtmAal5PortTxFrames_Type()
)
oacAtmAal5PortTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAtmAal5PortTxFrames.setStatus("current")
_OacAtmAal5PortTxFramesDiscarded_Type = Counter32
_OacAtmAal5PortTxFramesDiscarded_Object = MibTableColumn
oacAtmAal5PortTxFramesDiscarded = _OacAtmAal5PortTxFramesDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 1, 1, 6, 1, 3),
    _OacAtmAal5PortTxFramesDiscarded_Type()
)
oacAtmAal5PortTxFramesDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAtmAal5PortTxFramesDiscarded.setStatus("current")
_OacAtmAal5PortRxBytes_Type = Counter32
_OacAtmAal5PortRxBytes_Object = MibTableColumn
oacAtmAal5PortRxBytes = _OacAtmAal5PortRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 1, 1, 6, 1, 4),
    _OacAtmAal5PortRxBytes_Type()
)
oacAtmAal5PortRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAtmAal5PortRxBytes.setStatus("current")
_OacAtmAal5PortRxFrames_Type = Counter32
_OacAtmAal5PortRxFrames_Object = MibTableColumn
oacAtmAal5PortRxFrames = _OacAtmAal5PortRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 1, 1, 6, 1, 5),
    _OacAtmAal5PortRxFrames_Type()
)
oacAtmAal5PortRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAtmAal5PortRxFrames.setStatus("current")
_OacAtmAal5PortRxErrors_Type = Counter32
_OacAtmAal5PortRxErrors_Object = MibTableColumn
oacAtmAal5PortRxErrors = _OacAtmAal5PortRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 1, 1, 6, 1, 6),
    _OacAtmAal5PortRxErrors_Type()
)
oacAtmAal5PortRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAtmAal5PortRxErrors.setStatus("current")
_OacAtmAal5PortRxFramesDiscarded_Type = Counter32
_OacAtmAal5PortRxFramesDiscarded_Object = MibTableColumn
oacAtmAal5PortRxFramesDiscarded = _OacAtmAal5PortRxFramesDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 1, 1, 6, 1, 7),
    _OacAtmAal5PortRxFramesDiscarded_Type()
)
oacAtmAal5PortRxFramesDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacAtmAal5PortRxFramesDiscarded.setStatus("current")
_OacAtmStatNotifications_ObjectIdentity = ObjectIdentity
oacAtmStatNotifications = _OacAtmStatNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 1, 2)
)
_OacAtmStatConformance_ObjectIdentity = ObjectIdentity
oacAtmStatConformance = _OacAtmStatConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 1, 3)
)
_OacAtmStatGroups_ObjectIdentity = ObjectIdentity
oacAtmStatGroups = _OacAtmStatGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 1, 3, 1)
)
_OacAtmStatCompliances_ObjectIdentity = ObjectIdentity
oacAtmStatCompliances = _OacAtmStatCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 1, 3, 2)
)

# Managed Objects groups

oacAtmStatGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 1, 3, 1, 1)
)
oacAtmStatGeneralGroup.setObjects(
      *(("ONEACCESS-ATM-MIB", "oacAtmChanTxBytes"),
        ("ONEACCESS-ATM-MIB", "oacAtmChanTxCells"),
        ("ONEACCESS-ATM-MIB", "oacAtmChanRxBytes"),
        ("ONEACCESS-ATM-MIB", "oacAtmChanRxCells"),
        ("ONEACCESS-ATM-MIB", "oacAtmChanRxErrors"),
        ("ONEACCESS-ATM-MIB", "oacAtmChanTxOverflows"),
        ("ONEACCESS-ATM-MIB", "oacAtmAal0ChanRxCellsDiscarded"),
        ("ONEACCESS-ATM-MIB", "oacAtmAal1ChanTxUnderflows"),
        ("ONEACCESS-ATM-MIB", "oacAtmAal1ChanRxOverflows"),
        ("ONEACCESS-ATM-MIB", "oacAtmAal5ChanTxFrames"),
        ("ONEACCESS-ATM-MIB", "oacAtmAal5ChanRxFrames"),
        ("ONEACCESS-ATM-MIB", "oacAtmAal5ChanRxFramesDiscarded"),
        ("ONEACCESS-ATM-MIB", "oacAtmAal5ChanCrc32Errors"),
        ("ONEACCESS-ATM-MIB", "oacAtmAal5ChanLengthErrors"),
        ("ONEACCESS-ATM-MIB", "oacAtmAal5ChanReassemblyTimeouts"),
        ("ONEACCESS-ATM-MIB", "oacAtmPortTxCells"),
        ("ONEACCESS-ATM-MIB", "oacAtmPortRxCells"),
        ("ONEACCESS-ATM-MIB", "oacAtmPortRxCellsDiscarded"),
        ("ONEACCESS-ATM-MIB", "oacAtmPortHecErrors"),
        ("ONEACCESS-ATM-MIB", "oacAtmAal5PortTxBytes"),
        ("ONEACCESS-ATM-MIB", "oacAtmAal5PortTxFrames"),
        ("ONEACCESS-ATM-MIB", "oacAtmAal5PortTxFramesDiscarded"),
        ("ONEACCESS-ATM-MIB", "oacAtmAal5PortRxBytes"),
        ("ONEACCESS-ATM-MIB", "oacAtmAal5PortRxFrames"),
        ("ONEACCESS-ATM-MIB", "oacAtmAal5PortRxErrors"),
        ("ONEACCESS-ATM-MIB", "oacAtmAal5PortRxFramesDiscarded"))
)
if mibBuilder.loadTexts:
    oacAtmStatGeneralGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

oacAtmStatCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 2, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    oacAtmStatCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ONEACCESS-ATM-MIB",
    **{"oacAtmMIBModule": oacAtmMIBModule,
       "oacAtmStatObjects": oacAtmStatObjects,
       "oacAtmChannelTable": oacAtmChannelTable,
       "oacAtmChannelEntry": oacAtmChannelEntry,
       "oacAtmChanVpi": oacAtmChanVpi,
       "oacAtmChanVci": oacAtmChanVci,
       "oacAtmChanTxBytes": oacAtmChanTxBytes,
       "oacAtmChanTxCells": oacAtmChanTxCells,
       "oacAtmChanRxBytes": oacAtmChanRxBytes,
       "oacAtmChanRxCells": oacAtmChanRxCells,
       "oacAtmChanRxErrors": oacAtmChanRxErrors,
       "oacAtmChanTxOverflows": oacAtmChanTxOverflows,
       "oacAtmAal0ChannelGlobalStatTable": oacAtmAal0ChannelGlobalStatTable,
       "oacAtmAal0ChannelGlobalStatEntry": oacAtmAal0ChannelGlobalStatEntry,
       "oacAtmAal0ChanRxCellsDiscarded": oacAtmAal0ChanRxCellsDiscarded,
       "oacAtmAal1ChannelGlobalStatTable": oacAtmAal1ChannelGlobalStatTable,
       "oacAtmAal1ChannelGlobalStatEntry": oacAtmAal1ChannelGlobalStatEntry,
       "oacAtmAal1ChanTxUnderflows": oacAtmAal1ChanTxUnderflows,
       "oacAtmAal1ChanRxOverflows": oacAtmAal1ChanRxOverflows,
       "oacAtmAal5ChannelGlobalStatTable": oacAtmAal5ChannelGlobalStatTable,
       "oacAtmAal5ChannelGlobalStatEntry": oacAtmAal5ChannelGlobalStatEntry,
       "oacAtmAal5ChanTxFrames": oacAtmAal5ChanTxFrames,
       "oacAtmAal5ChanRxFrames": oacAtmAal5ChanRxFrames,
       "oacAtmAal5ChanRxFramesDiscarded": oacAtmAal5ChanRxFramesDiscarded,
       "oacAtmAal5ChanCrc32Errors": oacAtmAal5ChanCrc32Errors,
       "oacAtmAal5ChanLengthErrors": oacAtmAal5ChanLengthErrors,
       "oacAtmAal5ChanReassemblyTimeouts": oacAtmAal5ChanReassemblyTimeouts,
       "oacAtmPortStatTable": oacAtmPortStatTable,
       "oacAtmPortStatEntry": oacAtmPortStatEntry,
       "oacAtmPortTxCells": oacAtmPortTxCells,
       "oacAtmPortRxCells": oacAtmPortRxCells,
       "oacAtmPortRxCellsDiscarded": oacAtmPortRxCellsDiscarded,
       "oacAtmPortHecErrors": oacAtmPortHecErrors,
       "oacAtmAal5PortStatTable": oacAtmAal5PortStatTable,
       "oacAtmAal5PortStatEntry": oacAtmAal5PortStatEntry,
       "oacAtmAal5PortTxBytes": oacAtmAal5PortTxBytes,
       "oacAtmAal5PortTxFrames": oacAtmAal5PortTxFrames,
       "oacAtmAal5PortTxFramesDiscarded": oacAtmAal5PortTxFramesDiscarded,
       "oacAtmAal5PortRxBytes": oacAtmAal5PortRxBytes,
       "oacAtmAal5PortRxFrames": oacAtmAal5PortRxFrames,
       "oacAtmAal5PortRxErrors": oacAtmAal5PortRxErrors,
       "oacAtmAal5PortRxFramesDiscarded": oacAtmAal5PortRxFramesDiscarded,
       "oacAtmStatNotifications": oacAtmStatNotifications,
       "oacAtmStatConformance": oacAtmStatConformance,
       "oacAtmStatGroups": oacAtmStatGroups,
       "oacAtmStatGeneralGroup": oacAtmStatGeneralGroup,
       "oacAtmStatCompliances": oacAtmStatCompliances,
       "oacAtmStatCompliance": oacAtmStatCompliance}
)
