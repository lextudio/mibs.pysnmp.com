# SNMP MIB module (EXTREME-PORT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EXTREME-BASE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:41:19 2024
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

(ClientAuthType,
 extremeAgent) = mibBuilder.importSymbols(
    "EXTREME-BASE-MIB",
    "ClientAuthType",
    "extremeAgent")

(extremeVlanIfIndex,) = mibBuilder.importSymbols(
    "EXTREME-VLAN-MIB",
    "extremeVlanIfIndex")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 MacAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

extremePort = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ExtremePortLoadshareTable_Object = MibTable
extremePortLoadshareTable = _ExtremePortLoadshareTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 1)
)
if mibBuilder.loadTexts:
    extremePortLoadshareTable.setStatus("deprecated")
_ExtremePortLoadshareEntry_Object = MibTableRow
extremePortLoadshareEntry = _ExtremePortLoadshareEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 1, 1)
)
extremePortLoadshareEntry.setIndexNames(
    (0, "EXTREME-PORT-MIB", "extremePortLoadshareMasterIfIndex"),
    (0, "EXTREME-PORT-MIB", "extremePortLoadshareSlaveIfIndex"),
)
if mibBuilder.loadTexts:
    extremePortLoadshareEntry.setStatus("deprecated")
_ExtremePortLoadshareMasterIfIndex_Type = Integer32
_ExtremePortLoadshareMasterIfIndex_Object = MibTableColumn
extremePortLoadshareMasterIfIndex = _ExtremePortLoadshareMasterIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 1, 1, 1),
    _ExtremePortLoadshareMasterIfIndex_Type()
)
extremePortLoadshareMasterIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremePortLoadshareMasterIfIndex.setStatus("deprecated")
_ExtremePortLoadshareSlaveIfIndex_Type = Integer32
_ExtremePortLoadshareSlaveIfIndex_Object = MibTableColumn
extremePortLoadshareSlaveIfIndex = _ExtremePortLoadshareSlaveIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 1, 1, 2),
    _ExtremePortLoadshareSlaveIfIndex_Type()
)
extremePortLoadshareSlaveIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremePortLoadshareSlaveIfIndex.setStatus("deprecated")


class _ExtremePortLoadshareGrouping_Type(Integer32):
    """Custom type extremePortLoadshareGrouping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("pair", 2),
          ("quad", 4))
    )


_ExtremePortLoadshareGrouping_Type.__name__ = "Integer32"
_ExtremePortLoadshareGrouping_Object = MibTableColumn
extremePortLoadshareGrouping = _ExtremePortLoadshareGrouping_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 1, 1, 3),
    _ExtremePortLoadshareGrouping_Type()
)
extremePortLoadshareGrouping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremePortLoadshareGrouping.setStatus("deprecated")
_ExtremePortLoadshareStatus_Type = RowStatus
_ExtremePortLoadshareStatus_Object = MibTableColumn
extremePortLoadshareStatus = _ExtremePortLoadshareStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 1, 1, 4),
    _ExtremePortLoadshareStatus_Type()
)
extremePortLoadshareStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremePortLoadshareStatus.setStatus("deprecated")
_ExtremePortSummitlinkTable_Object = MibTable
extremePortSummitlinkTable = _ExtremePortSummitlinkTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 2)
)
if mibBuilder.loadTexts:
    extremePortSummitlinkTable.setStatus("deprecated")
_ExtremePortSummitlinkEntry_Object = MibTableRow
extremePortSummitlinkEntry = _ExtremePortSummitlinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 2, 1)
)
extremePortSummitlinkEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    extremePortSummitlinkEntry.setStatus("deprecated")


class _ExtremePortSummitlinkAdminMode_Type(Integer32):
    """Custom type extremePortSummitlinkAdminMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernetOnly", 1),
          ("summitlinkOnly", 2))
    )


_ExtremePortSummitlinkAdminMode_Type.__name__ = "Integer32"
_ExtremePortSummitlinkAdminMode_Object = MibTableColumn
extremePortSummitlinkAdminMode = _ExtremePortSummitlinkAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 2, 1, 1),
    _ExtremePortSummitlinkAdminMode_Type()
)
extremePortSummitlinkAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremePortSummitlinkAdminMode.setStatus("deprecated")


class _ExtremePortSummitlinkOperMode_Type(Integer32):
    """Custom type extremePortSummitlinkOperMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernetOnly", 1),
          ("summitlinkOnly", 2))
    )


_ExtremePortSummitlinkOperMode_Type.__name__ = "Integer32"
_ExtremePortSummitlinkOperMode_Object = MibTableColumn
extremePortSummitlinkOperMode = _ExtremePortSummitlinkOperMode_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 2, 1, 2),
    _ExtremePortSummitlinkOperMode_Type()
)
extremePortSummitlinkOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortSummitlinkOperMode.setStatus("deprecated")


class _ExtremePortSummitlinkState_Type(Integer32):
    """Custom type extremePortSummitlinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_ExtremePortSummitlinkState_Type.__name__ = "Integer32"
_ExtremePortSummitlinkState_Object = MibTableColumn
extremePortSummitlinkState = _ExtremePortSummitlinkState_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 2, 1, 3),
    _ExtremePortSummitlinkState_Type()
)
extremePortSummitlinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortSummitlinkState.setStatus("deprecated")


class _ExtremePortSummitlinkRejectReason_Type(Integer32):
    """Custom type extremePortSummitlinkRejectReason based on Integer32"""
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
          ("other", 2),
          ("stackMisconnected", 3))
    )


_ExtremePortSummitlinkRejectReason_Type.__name__ = "Integer32"
_ExtremePortSummitlinkRejectReason_Object = MibTableColumn
extremePortSummitlinkRejectReason = _ExtremePortSummitlinkRejectReason_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 2, 1, 4),
    _ExtremePortSummitlinkRejectReason_Type()
)
extremePortSummitlinkRejectReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortSummitlinkRejectReason.setStatus("deprecated")
_ExtremePortLoadshare2Table_Object = MibTable
extremePortLoadshare2Table = _ExtremePortLoadshare2Table_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 3)
)
if mibBuilder.loadTexts:
    extremePortLoadshare2Table.setStatus("current")
_ExtremePortLoadshare2Entry_Object = MibTableRow
extremePortLoadshare2Entry = _ExtremePortLoadshare2Entry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 3, 1)
)
extremePortLoadshare2Entry.setIndexNames(
    (0, "EXTREME-PORT-MIB", "extremePortLoadshare2MasterIfIndex"),
    (0, "EXTREME-PORT-MIB", "extremePortLoadshare2SlaveIfIndex"),
)
if mibBuilder.loadTexts:
    extremePortLoadshare2Entry.setStatus("current")
_ExtremePortLoadshare2MasterIfIndex_Type = Integer32
_ExtremePortLoadshare2MasterIfIndex_Object = MibTableColumn
extremePortLoadshare2MasterIfIndex = _ExtremePortLoadshare2MasterIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 3, 1, 1),
    _ExtremePortLoadshare2MasterIfIndex_Type()
)
extremePortLoadshare2MasterIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremePortLoadshare2MasterIfIndex.setStatus("current")
_ExtremePortLoadshare2SlaveIfIndex_Type = Integer32
_ExtremePortLoadshare2SlaveIfIndex_Object = MibTableColumn
extremePortLoadshare2SlaveIfIndex = _ExtremePortLoadshare2SlaveIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 3, 1, 2),
    _ExtremePortLoadshare2SlaveIfIndex_Type()
)
extremePortLoadshare2SlaveIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremePortLoadshare2SlaveIfIndex.setStatus("current")


class _ExtremePortLoadshare2Algorithm_Type(Integer32):
    """Custom type extremePortLoadshare2Algorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hash", 2),
          ("ingressPortOffset", 1),
          ("roundRobin", 3))
    )


_ExtremePortLoadshare2Algorithm_Type.__name__ = "Integer32"
_ExtremePortLoadshare2Algorithm_Object = MibTableColumn
extremePortLoadshare2Algorithm = _ExtremePortLoadshare2Algorithm_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 3, 1, 3),
    _ExtremePortLoadshare2Algorithm_Type()
)
extremePortLoadshare2Algorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremePortLoadshare2Algorithm.setStatus("current")
_ExtremePortLoadshare2Status_Type = RowStatus
_ExtremePortLoadshare2Status_Object = MibTableColumn
extremePortLoadshare2Status = _ExtremePortLoadshare2Status_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 3, 1, 4),
    _ExtremePortLoadshare2Status_Type()
)
extremePortLoadshare2Status.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremePortLoadshare2Status.setStatus("current")
_ExtremePortRateShapeTable_Object = MibTable
extremePortRateShapeTable = _ExtremePortRateShapeTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 4)
)
if mibBuilder.loadTexts:
    extremePortRateShapeTable.setStatus("current")
_ExtremePortRateShapeEntry_Object = MibTableRow
extremePortRateShapeEntry = _ExtremePortRateShapeEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 4, 1)
)
extremePortRateShapeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "EXTREME-VLAN-MIB", "extremeVlanIfIndex"),
)
if mibBuilder.loadTexts:
    extremePortRateShapeEntry.setStatus("current")


class _ExtremePortRateShapePortType_Type(Integer32):
    """Custom type extremePortRateShapePortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loopBack", 2),
          ("rateLimited", 1))
    )


_ExtremePortRateShapePortType_Type.__name__ = "Integer32"
_ExtremePortRateShapePortType_Object = MibTableColumn
extremePortRateShapePortType = _ExtremePortRateShapePortType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 4, 1, 1),
    _ExtremePortRateShapePortType_Type()
)
extremePortRateShapePortType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremePortRateShapePortType.setStatus("current")


class _ExtremePortRateShapeLoopbackTag_Type(Integer32):
    """Custom type extremePortRateShapeLoopbackTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4094),
    )


_ExtremePortRateShapeLoopbackTag_Type.__name__ = "Integer32"
_ExtremePortRateShapeLoopbackTag_Object = MibTableColumn
extremePortRateShapeLoopbackTag = _ExtremePortRateShapeLoopbackTag_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 4, 1, 2),
    _ExtremePortRateShapeLoopbackTag_Type()
)
extremePortRateShapeLoopbackTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremePortRateShapeLoopbackTag.setStatus("current")
_ExtremePortRateShapeStatus_Type = RowStatus
_ExtremePortRateShapeStatus_Object = MibTableColumn
extremePortRateShapeStatus = _ExtremePortRateShapeStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 4, 1, 3),
    _ExtremePortRateShapeStatus_Type()
)
extremePortRateShapeStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremePortRateShapeStatus.setStatus("current")
_ExtremePortUtilizationTable_Object = MibTable
extremePortUtilizationTable = _ExtremePortUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 5)
)
if mibBuilder.loadTexts:
    extremePortUtilizationTable.setStatus("current")
_ExtremePortUtilizationEntry_Object = MibTableRow
extremePortUtilizationEntry = _ExtremePortUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 5, 1)
)
extremePortUtilizationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    extremePortUtilizationEntry.setStatus("current")
_ExtremePortUtilizationAvgTxBw_Type = Integer32
_ExtremePortUtilizationAvgTxBw_Object = MibTableColumn
extremePortUtilizationAvgTxBw = _ExtremePortUtilizationAvgTxBw_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 5, 1, 1),
    _ExtremePortUtilizationAvgTxBw_Type()
)
extremePortUtilizationAvgTxBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortUtilizationAvgTxBw.setStatus("current")
_ExtremePortUtilizationAvgRxBw_Type = Integer32
_ExtremePortUtilizationAvgRxBw_Object = MibTableColumn
extremePortUtilizationAvgRxBw = _ExtremePortUtilizationAvgRxBw_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 5, 1, 2),
    _ExtremePortUtilizationAvgRxBw_Type()
)
extremePortUtilizationAvgRxBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortUtilizationAvgRxBw.setStatus("current")
_ExtremePortUtilizationPeakTxBw_Type = Integer32
_ExtremePortUtilizationPeakTxBw_Object = MibTableColumn
extremePortUtilizationPeakTxBw = _ExtremePortUtilizationPeakTxBw_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 5, 1, 3),
    _ExtremePortUtilizationPeakTxBw_Type()
)
extremePortUtilizationPeakTxBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortUtilizationPeakTxBw.setStatus("current")
_ExtremePortUtilizationPeakRxBw_Type = Integer32
_ExtremePortUtilizationPeakRxBw_Object = MibTableColumn
extremePortUtilizationPeakRxBw = _ExtremePortUtilizationPeakRxBw_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 5, 1, 4),
    _ExtremePortUtilizationPeakRxBw_Type()
)
extremePortUtilizationPeakRxBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortUtilizationPeakRxBw.setStatus("current")
_ExtremePortInfoTable_Object = MibTable
extremePortInfoTable = _ExtremePortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 6)
)
if mibBuilder.loadTexts:
    extremePortInfoTable.setStatus("current")
_ExtremePortInfoEntry_Object = MibTableRow
extremePortInfoEntry = _ExtremePortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 6, 1)
)
extremePortInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    extremePortInfoEntry.setStatus("current")
_ExtremePortInfoFilterUpCounter_Type = Counter32
_ExtremePortInfoFilterUpCounter_Object = MibTableColumn
extremePortInfoFilterUpCounter = _ExtremePortInfoFilterUpCounter_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 6, 1, 1),
    _ExtremePortInfoFilterUpCounter_Type()
)
extremePortInfoFilterUpCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremePortInfoFilterUpCounter.setStatus("current")
_ExtremePortInfoFilterDownCounter_Type = Counter32
_ExtremePortInfoFilterDownCounter_Object = MibTableColumn
extremePortInfoFilterDownCounter = _ExtremePortInfoFilterDownCounter_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 6, 1, 2),
    _ExtremePortInfoFilterDownCounter_Type()
)
extremePortInfoFilterDownCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremePortInfoFilterDownCounter.setStatus("current")
_ExtremePortXenpakVendorTable_Object = MibTable
extremePortXenpakVendorTable = _ExtremePortXenpakVendorTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 7)
)
if mibBuilder.loadTexts:
    extremePortXenpakVendorTable.setStatus("current")
_ExtremePortXenpakVendorEntry_Object = MibTableRow
extremePortXenpakVendorEntry = _ExtremePortXenpakVendorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 7, 1)
)
extremePortXenpakVendorEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    extremePortXenpakVendorEntry.setStatus("current")


class _ExtremePortXenpakVendorName_Type(DisplayString):
    """Custom type extremePortXenpakVendorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 22),
    )


_ExtremePortXenpakVendorName_Type.__name__ = "DisplayString"
_ExtremePortXenpakVendorName_Object = MibTableColumn
extremePortXenpakVendorName = _ExtremePortXenpakVendorName_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 7, 1, 1),
    _ExtremePortXenpakVendorName_Type()
)
extremePortXenpakVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortXenpakVendorName.setStatus("current")
_ExtremePortIngressStats_ObjectIdentity = ObjectIdentity
extremePortIngressStats = _ExtremePortIngressStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 8)
)
_ExtremePortIngressStatsPortTable_Object = MibTable
extremePortIngressStatsPortTable = _ExtremePortIngressStatsPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 8, 1)
)
if mibBuilder.loadTexts:
    extremePortIngressStatsPortTable.setStatus("current")
_ExtremePortIngressPortStatsEntry_Object = MibTableRow
extremePortIngressPortStatsEntry = _ExtremePortIngressPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 8, 1, 1)
)
extremePortIngressPortStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    extremePortIngressPortStatsEntry.setStatus("current")


class _ExtremePortIngressStatsLinkStatus_Type(Integer32):
    """Custom type extremePortIngressStatsLinkStatus based on Integer32"""
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
        *(("active", 2),
          ("disabled", 3),
          ("notPresent", 4),
          ("ready", 1))
    )


_ExtremePortIngressStatsLinkStatus_Type.__name__ = "Integer32"
_ExtremePortIngressStatsLinkStatus_Object = MibTableColumn
extremePortIngressStatsLinkStatus = _ExtremePortIngressStatsLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 8, 1, 1, 1),
    _ExtremePortIngressStatsLinkStatus_Type()
)
extremePortIngressStatsLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortIngressStatsLinkStatus.setStatus("current")
_ExtremePortIngressStatsPortHighPriBytes_Type = Counter64
_ExtremePortIngressStatsPortHighPriBytes_Object = MibTableColumn
extremePortIngressStatsPortHighPriBytes = _ExtremePortIngressStatsPortHighPriBytes_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 8, 1, 1, 2),
    _ExtremePortIngressStatsPortHighPriBytes_Type()
)
extremePortIngressStatsPortHighPriBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortIngressStatsPortHighPriBytes.setStatus("current")
_ExtremePortIngressStatsPortLowPriBytes_Type = Counter64
_ExtremePortIngressStatsPortLowPriBytes_Object = MibTableColumn
extremePortIngressStatsPortLowPriBytes = _ExtremePortIngressStatsPortLowPriBytes_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 8, 1, 1, 3),
    _ExtremePortIngressStatsPortLowPriBytes_Type()
)
extremePortIngressStatsPortLowPriBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortIngressStatsPortLowPriBytes.setStatus("current")
_ExtremePortIngressStatsPortDroppedBytes_Type = Counter64
_ExtremePortIngressStatsPortDroppedBytes_Object = MibTableColumn
extremePortIngressStatsPortDroppedBytes = _ExtremePortIngressStatsPortDroppedBytes_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 8, 1, 1, 4),
    _ExtremePortIngressStatsPortDroppedBytes_Type()
)
extremePortIngressStatsPortDroppedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortIngressStatsPortDroppedBytes.setStatus("current")
_ExtremePortIngressStatsTxXoff_Type = Counter64
_ExtremePortIngressStatsTxXoff_Object = MibTableColumn
extremePortIngressStatsTxXoff = _ExtremePortIngressStatsTxXoff_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 8, 1, 1, 5),
    _ExtremePortIngressStatsTxXoff_Type()
)
extremePortIngressStatsTxXoff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortIngressStatsTxXoff.setStatus("current")
_ExtremePortIngressStatsQueueTable_Object = MibTable
extremePortIngressStatsQueueTable = _ExtremePortIngressStatsQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 8, 2)
)
if mibBuilder.loadTexts:
    extremePortIngressStatsQueueTable.setStatus("current")
_ExtremePortIngressQueueStatsEntry_Object = MibTableRow
extremePortIngressQueueStatsEntry = _ExtremePortIngressQueueStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 8, 2, 1)
)
extremePortIngressQueueStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "EXTREME-PORT-MIB", "extremePortIngressStatsQueueIndex"),
)
if mibBuilder.loadTexts:
    extremePortIngressQueueStatsEntry.setStatus("current")
_ExtremePortIngressStatsQueueIndex_Type = Integer32
_ExtremePortIngressStatsQueueIndex_Object = MibTableColumn
extremePortIngressStatsQueueIndex = _ExtremePortIngressStatsQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 8, 2, 1, 1),
    _ExtremePortIngressStatsQueueIndex_Type()
)
extremePortIngressStatsQueueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortIngressStatsQueueIndex.setStatus("current")
_ExtremePortIngressStatsQueueHighPriBytes_Type = Counter64
_ExtremePortIngressStatsQueueHighPriBytes_Object = MibTableColumn
extremePortIngressStatsQueueHighPriBytes = _ExtremePortIngressStatsQueueHighPriBytes_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 8, 2, 1, 2),
    _ExtremePortIngressStatsQueueHighPriBytes_Type()
)
extremePortIngressStatsQueueHighPriBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortIngressStatsQueueHighPriBytes.setStatus("current")
_ExtremePortIngressStatsQueueLowPriBytes_Type = Counter64
_ExtremePortIngressStatsQueueLowPriBytes_Object = MibTableColumn
extremePortIngressStatsQueueLowPriBytes = _ExtremePortIngressStatsQueueLowPriBytes_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 8, 2, 1, 3),
    _ExtremePortIngressStatsQueueLowPriBytes_Type()
)
extremePortIngressStatsQueueLowPriBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortIngressStatsQueueLowPriBytes.setStatus("current")
_ExtremePortIngressStatsQueuePercentDropped_Type = Integer32
_ExtremePortIngressStatsQueuePercentDropped_Object = MibTableColumn
extremePortIngressStatsQueuePercentDropped = _ExtremePortIngressStatsQueuePercentDropped_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 8, 2, 1, 4),
    _ExtremePortIngressStatsQueuePercentDropped_Type()
)
extremePortIngressStatsQueuePercentDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortIngressStatsQueuePercentDropped.setStatus("current")
_ExtremePortEgressRateLimitTable_Object = MibTable
extremePortEgressRateLimitTable = _ExtremePortEgressRateLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 9)
)
if mibBuilder.loadTexts:
    extremePortEgressRateLimitTable.setStatus("current")
_ExtremePortEgressRateLimitEntry_Object = MibTableRow
extremePortEgressRateLimitEntry = _ExtremePortEgressRateLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 9, 1)
)
extremePortEgressRateLimitEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    extremePortEgressRateLimitEntry.setStatus("current")


class _ExtremePortEgressRateLimitType_Type(Integer32):
    """Custom type extremePortEgressRateLimitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("kbps", 2),
          ("mbps", 3),
          ("percentage", 1))
    )


_ExtremePortEgressRateLimitType_Type.__name__ = "Integer32"
_ExtremePortEgressRateLimitType_Object = MibTableColumn
extremePortEgressRateLimitType = _ExtremePortEgressRateLimitType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 9, 1, 1),
    _ExtremePortEgressRateLimitType_Type()
)
extremePortEgressRateLimitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortEgressRateLimitType.setStatus("current")
_ExtremePortEgressRateLimitValue_Type = Integer32
_ExtremePortEgressRateLimitValue_Object = MibTableColumn
extremePortEgressRateLimitValue = _ExtremePortEgressRateLimitValue_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 9, 1, 2),
    _ExtremePortEgressRateLimitValue_Type()
)
extremePortEgressRateLimitValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremePortEgressRateLimitValue.setStatus("current")
_ExtremeWiredClientTable_Object = MibTable
extremeWiredClientTable = _ExtremeWiredClientTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 10)
)
if mibBuilder.loadTexts:
    extremeWiredClientTable.setStatus("current")
_ExtremeWiredClientEntry_Object = MibTableRow
extremeWiredClientEntry = _ExtremeWiredClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 10, 1)
)
extremeWiredClientEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "EXTREME-PORT-MIB", "extremeWiredClientID"),
)
if mibBuilder.loadTexts:
    extremeWiredClientEntry.setStatus("current")
_ExtremeWiredClientID_Type = MacAddress
_ExtremeWiredClientID_Object = MibTableColumn
extremeWiredClientID = _ExtremeWiredClientID_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 10, 1, 1),
    _ExtremeWiredClientID_Type()
)
extremeWiredClientID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWiredClientID.setStatus("current")


class _ExtremeWiredClientState_Type(Integer32):
    """Custom type extremeWiredClientState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("authenticated", 1),
          ("unauthenticated", 2))
    )


_ExtremeWiredClientState_Type.__name__ = "Integer32"
_ExtremeWiredClientState_Object = MibTableColumn
extremeWiredClientState = _ExtremeWiredClientState_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 10, 1, 2),
    _ExtremeWiredClientState_Type()
)
extremeWiredClientState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWiredClientState.setStatus("current")
_ExtremeWiredClientVLAN_Type = Integer32
_ExtremeWiredClientVLAN_Object = MibTableColumn
extremeWiredClientVLAN = _ExtremeWiredClientVLAN_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 10, 1, 3),
    _ExtremeWiredClientVLAN_Type()
)
extremeWiredClientVLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWiredClientVLAN.setStatus("current")
_ExtremeWiredClientPriority_Type = Integer32
_ExtremeWiredClientPriority_Object = MibTableColumn
extremeWiredClientPriority = _ExtremeWiredClientPriority_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 10, 1, 4),
    _ExtremeWiredClientPriority_Type()
)
extremeWiredClientPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWiredClientPriority.setStatus("current")
_ExtremeWiredClientAuthType_Type = ClientAuthType
_ExtremeWiredClientAuthType_Object = MibTableColumn
extremeWiredClientAuthType = _ExtremeWiredClientAuthType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 10, 1, 5),
    _ExtremeWiredClientAuthType_Type()
)
extremeWiredClientAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWiredClientAuthType.setStatus("current")
_ExtremeWiredClientLastStateChangeTime_Type = TimeTicks
_ExtremeWiredClientLastStateChangeTime_Object = MibTableColumn
extremeWiredClientLastStateChangeTime = _ExtremeWiredClientLastStateChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 10, 1, 6),
    _ExtremeWiredClientLastStateChangeTime_Type()
)
extremeWiredClientLastStateChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWiredClientLastStateChangeTime.setStatus("current")
_ExtremeWiredClientIP_Type = IpAddress
_ExtremeWiredClientIP_Object = MibTableColumn
extremeWiredClientIP = _ExtremeWiredClientIP_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 4, 10, 1, 7),
    _ExtremeWiredClientIP_Type()
)
extremeWiredClientIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeWiredClientIP.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTREME-PORT-MIB",
    **{"extremePort": extremePort,
       "extremePortLoadshareTable": extremePortLoadshareTable,
       "extremePortLoadshareEntry": extremePortLoadshareEntry,
       "extremePortLoadshareMasterIfIndex": extremePortLoadshareMasterIfIndex,
       "extremePortLoadshareSlaveIfIndex": extremePortLoadshareSlaveIfIndex,
       "extremePortLoadshareGrouping": extremePortLoadshareGrouping,
       "extremePortLoadshareStatus": extremePortLoadshareStatus,
       "extremePortSummitlinkTable": extremePortSummitlinkTable,
       "extremePortSummitlinkEntry": extremePortSummitlinkEntry,
       "extremePortSummitlinkAdminMode": extremePortSummitlinkAdminMode,
       "extremePortSummitlinkOperMode": extremePortSummitlinkOperMode,
       "extremePortSummitlinkState": extremePortSummitlinkState,
       "extremePortSummitlinkRejectReason": extremePortSummitlinkRejectReason,
       "extremePortLoadshare2Table": extremePortLoadshare2Table,
       "extremePortLoadshare2Entry": extremePortLoadshare2Entry,
       "extremePortLoadshare2MasterIfIndex": extremePortLoadshare2MasterIfIndex,
       "extremePortLoadshare2SlaveIfIndex": extremePortLoadshare2SlaveIfIndex,
       "extremePortLoadshare2Algorithm": extremePortLoadshare2Algorithm,
       "extremePortLoadshare2Status": extremePortLoadshare2Status,
       "extremePortRateShapeTable": extremePortRateShapeTable,
       "extremePortRateShapeEntry": extremePortRateShapeEntry,
       "extremePortRateShapePortType": extremePortRateShapePortType,
       "extremePortRateShapeLoopbackTag": extremePortRateShapeLoopbackTag,
       "extremePortRateShapeStatus": extremePortRateShapeStatus,
       "extremePortUtilizationTable": extremePortUtilizationTable,
       "extremePortUtilizationEntry": extremePortUtilizationEntry,
       "extremePortUtilizationAvgTxBw": extremePortUtilizationAvgTxBw,
       "extremePortUtilizationAvgRxBw": extremePortUtilizationAvgRxBw,
       "extremePortUtilizationPeakTxBw": extremePortUtilizationPeakTxBw,
       "extremePortUtilizationPeakRxBw": extremePortUtilizationPeakRxBw,
       "extremePortInfoTable": extremePortInfoTable,
       "extremePortInfoEntry": extremePortInfoEntry,
       "extremePortInfoFilterUpCounter": extremePortInfoFilterUpCounter,
       "extremePortInfoFilterDownCounter": extremePortInfoFilterDownCounter,
       "extremePortXenpakVendorTable": extremePortXenpakVendorTable,
       "extremePortXenpakVendorEntry": extremePortXenpakVendorEntry,
       "extremePortXenpakVendorName": extremePortXenpakVendorName,
       "extremePortIngressStats": extremePortIngressStats,
       "extremePortIngressStatsPortTable": extremePortIngressStatsPortTable,
       "extremePortIngressPortStatsEntry": extremePortIngressPortStatsEntry,
       "extremePortIngressStatsLinkStatus": extremePortIngressStatsLinkStatus,
       "extremePortIngressStatsPortHighPriBytes": extremePortIngressStatsPortHighPriBytes,
       "extremePortIngressStatsPortLowPriBytes": extremePortIngressStatsPortLowPriBytes,
       "extremePortIngressStatsPortDroppedBytes": extremePortIngressStatsPortDroppedBytes,
       "extremePortIngressStatsTxXoff": extremePortIngressStatsTxXoff,
       "extremePortIngressStatsQueueTable": extremePortIngressStatsQueueTable,
       "extremePortIngressQueueStatsEntry": extremePortIngressQueueStatsEntry,
       "extremePortIngressStatsQueueIndex": extremePortIngressStatsQueueIndex,
       "extremePortIngressStatsQueueHighPriBytes": extremePortIngressStatsQueueHighPriBytes,
       "extremePortIngressStatsQueueLowPriBytes": extremePortIngressStatsQueueLowPriBytes,
       "extremePortIngressStatsQueuePercentDropped": extremePortIngressStatsQueuePercentDropped,
       "extremePortEgressRateLimitTable": extremePortEgressRateLimitTable,
       "extremePortEgressRateLimitEntry": extremePortEgressRateLimitEntry,
       "extremePortEgressRateLimitType": extremePortEgressRateLimitType,
       "extremePortEgressRateLimitValue": extremePortEgressRateLimitValue,
       "extremeWiredClientTable": extremeWiredClientTable,
       "extremeWiredClientEntry": extremeWiredClientEntry,
       "extremeWiredClientID": extremeWiredClientID,
       "extremeWiredClientState": extremeWiredClientState,
       "extremeWiredClientVLAN": extremeWiredClientVLAN,
       "extremeWiredClientPriority": extremeWiredClientPriority,
       "extremeWiredClientAuthType": extremeWiredClientAuthType,
       "extremeWiredClientLastStateChangeTime": extremeWiredClientLastStateChangeTime,
       "extremeWiredClientIP": extremeWiredClientIP}
)
