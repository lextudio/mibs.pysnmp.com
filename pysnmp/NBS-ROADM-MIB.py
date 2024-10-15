# SNMP MIB module (NBS-ROADM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NBS-ROADM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:24:59 2024
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
 ifAlias) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifAlias")

(NbsTcMHz,
 NbsTcMilliDb,
 NbsTcStagingCommit,
 nbs) = mibBuilder.importSymbols(
    "NBS-MIB",
    "NbsTcMHz",
    "NbsTcMilliDb",
    "NbsTcStagingCommit",
    "nbs")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

nbsRoadmMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 629, 235)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NbsRoadmCommonGrp_ObjectIdentity = ObjectIdentity
nbsRoadmCommonGrp = _NbsRoadmCommonGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 235, 10)
)
if mibBuilder.loadTexts:
    nbsRoadmCommonGrp.setStatus("current")
_NbsRoadmCommonTableSize_Type = Unsigned32
_NbsRoadmCommonTableSize_Object = MibScalar
nbsRoadmCommonTableSize = _NbsRoadmCommonTableSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 235, 10, 1),
    _NbsRoadmCommonTableSize_Type()
)
nbsRoadmCommonTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsRoadmCommonTableSize.setStatus("current")
_NbsRoadmCommonTable_Object = MibTable
nbsRoadmCommonTable = _NbsRoadmCommonTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 235, 10, 2)
)
if mibBuilder.loadTexts:
    nbsRoadmCommonTable.setStatus("current")
_NbsRoadmCommonEntry_Object = MibTableRow
nbsRoadmCommonEntry = _NbsRoadmCommonEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 235, 10, 2, 1)
)
nbsRoadmCommonEntry.setIndexNames(
    (0, "NBS-ROADM-MIB", "nbsRoadmCommonIfIndex"),
)
if mibBuilder.loadTexts:
    nbsRoadmCommonEntry.setStatus("current")
_NbsRoadmCommonIfIndex_Type = InterfaceIndex
_NbsRoadmCommonIfIndex_Object = MibTableColumn
nbsRoadmCommonIfIndex = _NbsRoadmCommonIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 235, 10, 2, 1, 1),
    _NbsRoadmCommonIfIndex_Type()
)
nbsRoadmCommonIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsRoadmCommonIfIndex.setStatus("current")


class _NbsRoadmCommonStagingQuickCfg_Type(Integer32):
    """Custom type nbsRoadmCommonStagingQuickCfg based on Integer32"""
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
        *(("notSupported", 1),
          ("std100Ghz", 3),
          ("std50Ghz", 4),
          ("supported", 2))
    )


_NbsRoadmCommonStagingQuickCfg_Type.__name__ = "Integer32"
_NbsRoadmCommonStagingQuickCfg_Object = MibTableColumn
nbsRoadmCommonStagingQuickCfg = _NbsRoadmCommonStagingQuickCfg_Object(
    (1, 3, 6, 1, 4, 1, 629, 235, 10, 2, 1, 10),
    _NbsRoadmCommonStagingQuickCfg_Type()
)
nbsRoadmCommonStagingQuickCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsRoadmCommonStagingQuickCfg.setStatus("current")


class _NbsRoadmCommonStagingAddCaps_Type(Integer32):
    """Custom type nbsRoadmCommonStagingAddCaps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("capable", 2),
          ("notSupported", 1))
    )


_NbsRoadmCommonStagingAddCaps_Type.__name__ = "Integer32"
_NbsRoadmCommonStagingAddCaps_Object = MibTableColumn
nbsRoadmCommonStagingAddCaps = _NbsRoadmCommonStagingAddCaps_Object(
    (1, 3, 6, 1, 4, 1, 629, 235, 10, 2, 1, 13),
    _NbsRoadmCommonStagingAddCaps_Type()
)
nbsRoadmCommonStagingAddCaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsRoadmCommonStagingAddCaps.setStatus("current")


class _NbsRoadmCommonStagingDropCaps_Type(Integer32):
    """Custom type nbsRoadmCommonStagingDropCaps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("capable", 2),
          ("notSupported", 1))
    )


_NbsRoadmCommonStagingDropCaps_Type.__name__ = "Integer32"
_NbsRoadmCommonStagingDropCaps_Object = MibTableColumn
nbsRoadmCommonStagingDropCaps = _NbsRoadmCommonStagingDropCaps_Object(
    (1, 3, 6, 1, 4, 1, 629, 235, 10, 2, 1, 14),
    _NbsRoadmCommonStagingDropCaps_Type()
)
nbsRoadmCommonStagingDropCaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsRoadmCommonStagingDropCaps.setStatus("current")
_NbsRoadmCommonStagingCommit_Type = NbsTcStagingCommit
_NbsRoadmCommonStagingCommit_Object = MibTableColumn
nbsRoadmCommonStagingCommit = _NbsRoadmCommonStagingCommit_Object(
    (1, 3, 6, 1, 4, 1, 629, 235, 10, 2, 1, 20),
    _NbsRoadmCommonStagingCommit_Type()
)
nbsRoadmCommonStagingCommit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsRoadmCommonStagingCommit.setStatus("current")


class _NbsRoadmCommonCommittedGridType_Type(Integer32):
    """Custom type nbsRoadmCommonCommittedGridType based on Integer32"""
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
        *(("customized", 3),
          ("notSupported", 1),
          ("reserved", 2),
          ("std100Ghz", 4),
          ("std50Ghz", 5))
    )


_NbsRoadmCommonCommittedGridType_Type.__name__ = "Integer32"
_NbsRoadmCommonCommittedGridType_Object = MibTableColumn
nbsRoadmCommonCommittedGridType = _NbsRoadmCommonCommittedGridType_Object(
    (1, 3, 6, 1, 4, 1, 629, 235, 10, 2, 1, 30),
    _NbsRoadmCommonCommittedGridType_Type()
)
nbsRoadmCommonCommittedGridType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsRoadmCommonCommittedGridType.setStatus("current")


class _NbsRoadmCommonCommittedChannels_Type(Integer32):
    """Custom type nbsRoadmCommonCommittedChannels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_NbsRoadmCommonCommittedChannels_Type.__name__ = "Integer32"
_NbsRoadmCommonCommittedChannels_Object = MibTableColumn
nbsRoadmCommonCommittedChannels = _NbsRoadmCommonCommittedChannels_Object(
    (1, 3, 6, 1, 4, 1, 629, 235, 10, 2, 1, 40),
    _NbsRoadmCommonCommittedChannels_Type()
)
nbsRoadmCommonCommittedChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsRoadmCommonCommittedChannels.setStatus("current")
_NbsRoadmFlexgridGrp_ObjectIdentity = ObjectIdentity
nbsRoadmFlexgridGrp = _NbsRoadmFlexgridGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 235, 20)
)
if mibBuilder.loadTexts:
    nbsRoadmFlexgridGrp.setStatus("current")
_NbsRoadmFlexgridTableSize_Type = Unsigned32
_NbsRoadmFlexgridTableSize_Object = MibScalar
nbsRoadmFlexgridTableSize = _NbsRoadmFlexgridTableSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 235, 20, 1),
    _NbsRoadmFlexgridTableSize_Type()
)
nbsRoadmFlexgridTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsRoadmFlexgridTableSize.setStatus("current")
_NbsRoadmFlexgridTable_Object = MibTable
nbsRoadmFlexgridTable = _NbsRoadmFlexgridTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 235, 20, 2)
)
if mibBuilder.loadTexts:
    nbsRoadmFlexgridTable.setStatus("current")
_NbsRoadmFlexgridEntry_Object = MibTableRow
nbsRoadmFlexgridEntry = _NbsRoadmFlexgridEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 235, 20, 2, 1)
)
nbsRoadmFlexgridEntry.setIndexNames(
    (0, "NBS-ROADM-MIB", "nbsRoadmFlexgridIfIndex"),
)
if mibBuilder.loadTexts:
    nbsRoadmFlexgridEntry.setStatus("current")
_NbsRoadmFlexgridIfIndex_Type = InterfaceIndex
_NbsRoadmFlexgridIfIndex_Object = MibTableColumn
nbsRoadmFlexgridIfIndex = _NbsRoadmFlexgridIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 235, 20, 2, 1, 1),
    _NbsRoadmFlexgridIfIndex_Type()
)
nbsRoadmFlexgridIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsRoadmFlexgridIfIndex.setStatus("current")


class _NbsRoadmFlexgridCenterlineMin_Type(NbsTcMHz):
    """Custom type nbsRoadmFlexgridCenterlineMin based on NbsTcMHz"""
    defaultValue = 190100000


_NbsRoadmFlexgridCenterlineMin_Object = MibTableColumn
nbsRoadmFlexgridCenterlineMin = _NbsRoadmFlexgridCenterlineMin_Object(
    (1, 3, 6, 1, 4, 1, 629, 235, 20, 2, 1, 21),
    _NbsRoadmFlexgridCenterlineMin_Type()
)
nbsRoadmFlexgridCenterlineMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsRoadmFlexgridCenterlineMin.setStatus("current")


class _NbsRoadmFlexgridCenterlineMax_Type(NbsTcMHz):
    """Custom type nbsRoadmFlexgridCenterlineMax based on NbsTcMHz"""
    defaultValue = 197250000


_NbsRoadmFlexgridCenterlineMax_Object = MibTableColumn
nbsRoadmFlexgridCenterlineMax = _NbsRoadmFlexgridCenterlineMax_Object(
    (1, 3, 6, 1, 4, 1, 629, 235, 20, 2, 1, 22),
    _NbsRoadmFlexgridCenterlineMax_Type()
)
nbsRoadmFlexgridCenterlineMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsRoadmFlexgridCenterlineMax.setStatus("current")


class _NbsRoadmFlexgridCenterlineIncr_Type(NbsTcMHz):
    """Custom type nbsRoadmFlexgridCenterlineIncr based on NbsTcMHz"""
    defaultValue = 12500


_NbsRoadmFlexgridCenterlineIncr_Object = MibTableColumn
nbsRoadmFlexgridCenterlineIncr = _NbsRoadmFlexgridCenterlineIncr_Object(
    (1, 3, 6, 1, 4, 1, 629, 235, 20, 2, 1, 23),
    _NbsRoadmFlexgridCenterlineIncr_Type()
)
nbsRoadmFlexgridCenterlineIncr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsRoadmFlexgridCenterlineIncr.setStatus("current")


class _NbsRoadmFlexgridBandwidthMin_Type(NbsTcMHz):
    """Custom type nbsRoadmFlexgridBandwidthMin based on NbsTcMHz"""
    defaultValue = 25000


_NbsRoadmFlexgridBandwidthMin_Object = MibTableColumn
nbsRoadmFlexgridBandwidthMin = _NbsRoadmFlexgridBandwidthMin_Object(
    (1, 3, 6, 1, 4, 1, 629, 235, 20, 2, 1, 31),
    _NbsRoadmFlexgridBandwidthMin_Type()
)
nbsRoadmFlexgridBandwidthMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsRoadmFlexgridBandwidthMin.setStatus("current")


class _NbsRoadmFlexgridBandwidthMax_Type(NbsTcMHz):
    """Custom type nbsRoadmFlexgridBandwidthMax based on NbsTcMHz"""
    defaultValue = 25000


_NbsRoadmFlexgridBandwidthMax_Object = MibTableColumn
nbsRoadmFlexgridBandwidthMax = _NbsRoadmFlexgridBandwidthMax_Object(
    (1, 3, 6, 1, 4, 1, 629, 235, 20, 2, 1, 32),
    _NbsRoadmFlexgridBandwidthMax_Type()
)
nbsRoadmFlexgridBandwidthMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsRoadmFlexgridBandwidthMax.setStatus("current")


class _NbsRoadmFlexgridBandwidthIncr_Type(NbsTcMHz):
    """Custom type nbsRoadmFlexgridBandwidthIncr based on NbsTcMHz"""
    defaultValue = 25000


_NbsRoadmFlexgridBandwidthIncr_Object = MibTableColumn
nbsRoadmFlexgridBandwidthIncr = _NbsRoadmFlexgridBandwidthIncr_Object(
    (1, 3, 6, 1, 4, 1, 629, 235, 20, 2, 1, 33),
    _NbsRoadmFlexgridBandwidthIncr_Type()
)
nbsRoadmFlexgridBandwidthIncr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsRoadmFlexgridBandwidthIncr.setStatus("current")
_NbsRoadmStagingGrp_ObjectIdentity = ObjectIdentity
nbsRoadmStagingGrp = _NbsRoadmStagingGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 235, 30)
)
if mibBuilder.loadTexts:
    nbsRoadmStagingGrp.setStatus("current")
_NbsRoadmStagingTableSize_Type = Unsigned32
_NbsRoadmStagingTableSize_Object = MibScalar
nbsRoadmStagingTableSize = _NbsRoadmStagingTableSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 235, 30, 1),
    _NbsRoadmStagingTableSize_Type()
)
nbsRoadmStagingTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsRoadmStagingTableSize.setStatus("current")
_NbsRoadmStagingTable_Object = MibTable
nbsRoadmStagingTable = _NbsRoadmStagingTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 235, 30, 2)
)
if mibBuilder.loadTexts:
    nbsRoadmStagingTable.setStatus("current")
_NbsRoadmStagingEntry_Object = MibTableRow
nbsRoadmStagingEntry = _NbsRoadmStagingEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 235, 30, 2, 1)
)
nbsRoadmStagingEntry.setIndexNames(
    (0, "NBS-ROADM-MIB", "nbsRoadmStagingIfIndex"),
    (0, "NBS-ROADM-MIB", "nbsRoadmStagingCenterline"),
)
if mibBuilder.loadTexts:
    nbsRoadmStagingEntry.setStatus("current")
_NbsRoadmStagingIfIndex_Type = InterfaceIndex
_NbsRoadmStagingIfIndex_Object = MibTableColumn
nbsRoadmStagingIfIndex = _NbsRoadmStagingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 235, 30, 2, 1, 1),
    _NbsRoadmStagingIfIndex_Type()
)
nbsRoadmStagingIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsRoadmStagingIfIndex.setStatus("current")
_NbsRoadmStagingCenterline_Type = NbsTcMHz
_NbsRoadmStagingCenterline_Object = MibTableColumn
nbsRoadmStagingCenterline = _NbsRoadmStagingCenterline_Object(
    (1, 3, 6, 1, 4, 1, 629, 235, 30, 2, 1, 2),
    _NbsRoadmStagingCenterline_Type()
)
nbsRoadmStagingCenterline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsRoadmStagingCenterline.setStatus("current")


class _NbsRoadmStagingBandwidth_Type(NbsTcMHz):
    """Custom type nbsRoadmStagingBandwidth based on NbsTcMHz"""
    defaultValue = 100000


_NbsRoadmStagingBandwidth_Object = MibTableColumn
nbsRoadmStagingBandwidth = _NbsRoadmStagingBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 629, 235, 30, 2, 1, 10),
    _NbsRoadmStagingBandwidth_Type()
)
nbsRoadmStagingBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nbsRoadmStagingBandwidth.setStatus("current")


class _NbsRoadmStagingChannelName_Type(DisplayString):
    """Custom type nbsRoadmStagingChannelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NbsRoadmStagingChannelName_Type.__name__ = "DisplayString"
_NbsRoadmStagingChannelName_Object = MibTableColumn
nbsRoadmStagingChannelName = _NbsRoadmStagingChannelName_Object(
    (1, 3, 6, 1, 4, 1, 629, 235, 30, 2, 1, 30),
    _NbsRoadmStagingChannelName_Type()
)
nbsRoadmStagingChannelName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nbsRoadmStagingChannelName.setStatus("current")
_NbsRoadmStagingAddPort_Type = InterfaceIndex
_NbsRoadmStagingAddPort_Object = MibTableColumn
nbsRoadmStagingAddPort = _NbsRoadmStagingAddPort_Object(
    (1, 3, 6, 1, 4, 1, 629, 235, 30, 2, 1, 41),
    _NbsRoadmStagingAddPort_Type()
)
nbsRoadmStagingAddPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nbsRoadmStagingAddPort.setStatus("current")
_NbsRoadmStagingDropPort_Type = InterfaceIndex
_NbsRoadmStagingDropPort_Object = MibTableColumn
nbsRoadmStagingDropPort = _NbsRoadmStagingDropPort_Object(
    (1, 3, 6, 1, 4, 1, 629, 235, 30, 2, 1, 42),
    _NbsRoadmStagingDropPort_Type()
)
nbsRoadmStagingDropPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nbsRoadmStagingDropPort.setStatus("current")
_NbsRoadmStagingSecondaryPort_Type = InterfaceIndex
_NbsRoadmStagingSecondaryPort_Object = MibTableColumn
nbsRoadmStagingSecondaryPort = _NbsRoadmStagingSecondaryPort_Object(
    (1, 3, 6, 1, 4, 1, 629, 235, 30, 2, 1, 43),
    _NbsRoadmStagingSecondaryPort_Type()
)
nbsRoadmStagingSecondaryPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nbsRoadmStagingSecondaryPort.setStatus("current")


class _NbsRoadmStagingSecondAttenu_Type(NbsTcMilliDb):
    """Custom type nbsRoadmStagingSecondAttenu based on NbsTcMilliDb"""
    defaultValue = -1000000


_NbsRoadmStagingSecondAttenu_Object = MibTableColumn
nbsRoadmStagingSecondAttenu = _NbsRoadmStagingSecondAttenu_Object(
    (1, 3, 6, 1, 4, 1, 629, 235, 30, 2, 1, 44),
    _NbsRoadmStagingSecondAttenu_Type()
)
nbsRoadmStagingSecondAttenu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nbsRoadmStagingSecondAttenu.setStatus("current")


class _NbsRoadmStagingAddAttenu_Type(NbsTcMilliDb):
    """Custom type nbsRoadmStagingAddAttenu based on NbsTcMilliDb"""
    defaultValue = -1000000


_NbsRoadmStagingAddAttenu_Object = MibTableColumn
nbsRoadmStagingAddAttenu = _NbsRoadmStagingAddAttenu_Object(
    (1, 3, 6, 1, 4, 1, 629, 235, 30, 2, 1, 51),
    _NbsRoadmStagingAddAttenu_Type()
)
nbsRoadmStagingAddAttenu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nbsRoadmStagingAddAttenu.setStatus("current")


class _NbsRoadmStagingDropAttenu_Type(NbsTcMilliDb):
    """Custom type nbsRoadmStagingDropAttenu based on NbsTcMilliDb"""
    defaultValue = -1000000


_NbsRoadmStagingDropAttenu_Object = MibTableColumn
nbsRoadmStagingDropAttenu = _NbsRoadmStagingDropAttenu_Object(
    (1, 3, 6, 1, 4, 1, 629, 235, 30, 2, 1, 52),
    _NbsRoadmStagingDropAttenu_Type()
)
nbsRoadmStagingDropAttenu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nbsRoadmStagingDropAttenu.setStatus("current")


class _NbsRoadmStagingItuName_Type(DisplayString):
    """Custom type nbsRoadmStagingItuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NbsRoadmStagingItuName_Type.__name__ = "DisplayString"
_NbsRoadmStagingItuName_Object = MibTableColumn
nbsRoadmStagingItuName = _NbsRoadmStagingItuName_Object(
    (1, 3, 6, 1, 4, 1, 629, 235, 30, 2, 1, 53),
    _NbsRoadmStagingItuName_Type()
)
nbsRoadmStagingItuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsRoadmStagingItuName.setStatus("current")


class _NbsRoadmStagingRowStatus_Type(RowStatus):
    """Custom type nbsRoadmStagingRowStatus based on RowStatus"""


_NbsRoadmStagingRowStatus_Object = MibTableColumn
nbsRoadmStagingRowStatus = _NbsRoadmStagingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 235, 30, 2, 1, 99),
    _NbsRoadmStagingRowStatus_Type()
)
nbsRoadmStagingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nbsRoadmStagingRowStatus.setStatus("current")
_NbsRoadmCommittedGrp_ObjectIdentity = ObjectIdentity
nbsRoadmCommittedGrp = _NbsRoadmCommittedGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 235, 31)
)
if mibBuilder.loadTexts:
    nbsRoadmCommittedGrp.setStatus("current")
_NbsRoadmCommittedTableSize_Type = Unsigned32
_NbsRoadmCommittedTableSize_Object = MibScalar
nbsRoadmCommittedTableSize = _NbsRoadmCommittedTableSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 235, 31, 1),
    _NbsRoadmCommittedTableSize_Type()
)
nbsRoadmCommittedTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsRoadmCommittedTableSize.setStatus("current")
_NbsRoadmCommittedTable_Object = MibTable
nbsRoadmCommittedTable = _NbsRoadmCommittedTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 235, 31, 2)
)
if mibBuilder.loadTexts:
    nbsRoadmCommittedTable.setStatus("current")
_NbsRoadmCommittedEntry_Object = MibTableRow
nbsRoadmCommittedEntry = _NbsRoadmCommittedEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 235, 31, 2, 1)
)
nbsRoadmCommittedEntry.setIndexNames(
    (0, "NBS-ROADM-MIB", "nbsRoadmCommittedIfIndex"),
    (0, "NBS-ROADM-MIB", "nbsRoadmCommittedCenterline"),
)
if mibBuilder.loadTexts:
    nbsRoadmCommittedEntry.setStatus("current")
_NbsRoadmCommittedIfIndex_Type = InterfaceIndex
_NbsRoadmCommittedIfIndex_Object = MibTableColumn
nbsRoadmCommittedIfIndex = _NbsRoadmCommittedIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 235, 31, 2, 1, 1),
    _NbsRoadmCommittedIfIndex_Type()
)
nbsRoadmCommittedIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsRoadmCommittedIfIndex.setStatus("current")
_NbsRoadmCommittedCenterline_Type = NbsTcMHz
_NbsRoadmCommittedCenterline_Object = MibTableColumn
nbsRoadmCommittedCenterline = _NbsRoadmCommittedCenterline_Object(
    (1, 3, 6, 1, 4, 1, 629, 235, 31, 2, 1, 2),
    _NbsRoadmCommittedCenterline_Type()
)
nbsRoadmCommittedCenterline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsRoadmCommittedCenterline.setStatus("current")


class _NbsRoadmCommittedBandwidth_Type(NbsTcMHz):
    """Custom type nbsRoadmCommittedBandwidth based on NbsTcMHz"""
    defaultValue = 100000


_NbsRoadmCommittedBandwidth_Object = MibTableColumn
nbsRoadmCommittedBandwidth = _NbsRoadmCommittedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 629, 235, 31, 2, 1, 10),
    _NbsRoadmCommittedBandwidth_Type()
)
nbsRoadmCommittedBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsRoadmCommittedBandwidth.setStatus("current")


class _NbsRoadmCommittedChannelName_Type(DisplayString):
    """Custom type nbsRoadmCommittedChannelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NbsRoadmCommittedChannelName_Type.__name__ = "DisplayString"
_NbsRoadmCommittedChannelName_Object = MibTableColumn
nbsRoadmCommittedChannelName = _NbsRoadmCommittedChannelName_Object(
    (1, 3, 6, 1, 4, 1, 629, 235, 31, 2, 1, 30),
    _NbsRoadmCommittedChannelName_Type()
)
nbsRoadmCommittedChannelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsRoadmCommittedChannelName.setStatus("current")
_NbsRoadmCommittedAddPort_Type = InterfaceIndex
_NbsRoadmCommittedAddPort_Object = MibTableColumn
nbsRoadmCommittedAddPort = _NbsRoadmCommittedAddPort_Object(
    (1, 3, 6, 1, 4, 1, 629, 235, 31, 2, 1, 41),
    _NbsRoadmCommittedAddPort_Type()
)
nbsRoadmCommittedAddPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsRoadmCommittedAddPort.setStatus("current")
_NbsRoadmCommittedDropPort_Type = InterfaceIndex
_NbsRoadmCommittedDropPort_Object = MibTableColumn
nbsRoadmCommittedDropPort = _NbsRoadmCommittedDropPort_Object(
    (1, 3, 6, 1, 4, 1, 629, 235, 31, 2, 1, 42),
    _NbsRoadmCommittedDropPort_Type()
)
nbsRoadmCommittedDropPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsRoadmCommittedDropPort.setStatus("current")
_NbsRoadmCommittedSecondaryPort_Type = InterfaceIndex
_NbsRoadmCommittedSecondaryPort_Object = MibTableColumn
nbsRoadmCommittedSecondaryPort = _NbsRoadmCommittedSecondaryPort_Object(
    (1, 3, 6, 1, 4, 1, 629, 235, 31, 2, 1, 43),
    _NbsRoadmCommittedSecondaryPort_Type()
)
nbsRoadmCommittedSecondaryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsRoadmCommittedSecondaryPort.setStatus("current")
_NbsRoadmCommittedSecondAttenu_Type = NbsTcMilliDb
_NbsRoadmCommittedSecondAttenu_Object = MibTableColumn
nbsRoadmCommittedSecondAttenu = _NbsRoadmCommittedSecondAttenu_Object(
    (1, 3, 6, 1, 4, 1, 629, 235, 31, 2, 1, 44),
    _NbsRoadmCommittedSecondAttenu_Type()
)
nbsRoadmCommittedSecondAttenu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsRoadmCommittedSecondAttenu.setStatus("current")
_NbsRoadmCommittedAddAttenu_Type = NbsTcMilliDb
_NbsRoadmCommittedAddAttenu_Object = MibTableColumn
nbsRoadmCommittedAddAttenu = _NbsRoadmCommittedAddAttenu_Object(
    (1, 3, 6, 1, 4, 1, 629, 235, 31, 2, 1, 51),
    _NbsRoadmCommittedAddAttenu_Type()
)
nbsRoadmCommittedAddAttenu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsRoadmCommittedAddAttenu.setStatus("current")
_NbsRoadmCommittedDropAttenu_Type = NbsTcMilliDb
_NbsRoadmCommittedDropAttenu_Object = MibTableColumn
nbsRoadmCommittedDropAttenu = _NbsRoadmCommittedDropAttenu_Object(
    (1, 3, 6, 1, 4, 1, 629, 235, 31, 2, 1, 52),
    _NbsRoadmCommittedDropAttenu_Type()
)
nbsRoadmCommittedDropAttenu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsRoadmCommittedDropAttenu.setStatus("current")


class _NbsRoadmCommittedItuName_Type(DisplayString):
    """Custom type nbsRoadmCommittedItuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_NbsRoadmCommittedItuName_Type.__name__ = "DisplayString"
_NbsRoadmCommittedItuName_Object = MibTableColumn
nbsRoadmCommittedItuName = _NbsRoadmCommittedItuName_Object(
    (1, 3, 6, 1, 4, 1, 629, 235, 31, 2, 1, 60),
    _NbsRoadmCommittedItuName_Type()
)
nbsRoadmCommittedItuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsRoadmCommittedItuName.setStatus("current")
_NbsRoadmRedundantGrp_ObjectIdentity = ObjectIdentity
nbsRoadmRedundantGrp = _NbsRoadmRedundantGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 235, 32)
)
if mibBuilder.loadTexts:
    nbsRoadmRedundantGrp.setStatus("current")
_NbsRoadmRedundantTableSize_Type = Unsigned32
_NbsRoadmRedundantTableSize_Object = MibScalar
nbsRoadmRedundantTableSize = _NbsRoadmRedundantTableSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 235, 32, 1),
    _NbsRoadmRedundantTableSize_Type()
)
nbsRoadmRedundantTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsRoadmRedundantTableSize.setStatus("current")
_NbsRoadmRedundantTable_Object = MibTable
nbsRoadmRedundantTable = _NbsRoadmRedundantTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 235, 32, 2)
)
if mibBuilder.loadTexts:
    nbsRoadmRedundantTable.setStatus("current")
_NbsRoadmRedundantEntry_Object = MibTableRow
nbsRoadmRedundantEntry = _NbsRoadmRedundantEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 235, 32, 2, 1)
)
nbsRoadmRedundantEntry.setIndexNames(
    (0, "NBS-ROADM-MIB", "nbsRoadmRedundantIfIndex"),
    (0, "NBS-ROADM-MIB", "nbsRoadmRedundantCenterline"),
)
if mibBuilder.loadTexts:
    nbsRoadmRedundantEntry.setStatus("current")
_NbsRoadmRedundantIfIndex_Type = InterfaceIndex
_NbsRoadmRedundantIfIndex_Object = MibTableColumn
nbsRoadmRedundantIfIndex = _NbsRoadmRedundantIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 235, 32, 2, 1, 1),
    _NbsRoadmRedundantIfIndex_Type()
)
nbsRoadmRedundantIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsRoadmRedundantIfIndex.setStatus("current")
_NbsRoadmRedundantCenterline_Type = NbsTcMHz
_NbsRoadmRedundantCenterline_Object = MibTableColumn
nbsRoadmRedundantCenterline = _NbsRoadmRedundantCenterline_Object(
    (1, 3, 6, 1, 4, 1, 629, 235, 32, 2, 1, 2),
    _NbsRoadmRedundantCenterline_Type()
)
nbsRoadmRedundantCenterline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsRoadmRedundantCenterline.setStatus("current")


class _NbsRoadmRedundantItuName_Type(DisplayString):
    """Custom type nbsRoadmRedundantItuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NbsRoadmRedundantItuName_Type.__name__ = "DisplayString"
_NbsRoadmRedundantItuName_Object = MibTableColumn
nbsRoadmRedundantItuName = _NbsRoadmRedundantItuName_Object(
    (1, 3, 6, 1, 4, 1, 629, 235, 32, 2, 1, 10),
    _NbsRoadmRedundantItuName_Type()
)
nbsRoadmRedundantItuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsRoadmRedundantItuName.setStatus("current")


class _NbsRoadmRedundantChannelName_Type(DisplayString):
    """Custom type nbsRoadmRedundantChannelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NbsRoadmRedundantChannelName_Type.__name__ = "DisplayString"
_NbsRoadmRedundantChannelName_Object = MibTableColumn
nbsRoadmRedundantChannelName = _NbsRoadmRedundantChannelName_Object(
    (1, 3, 6, 1, 4, 1, 629, 235, 32, 2, 1, 20),
    _NbsRoadmRedundantChannelName_Type()
)
nbsRoadmRedundantChannelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsRoadmRedundantChannelName.setStatus("current")
_NbsRoadmRedundantMapPort_Type = InterfaceIndex
_NbsRoadmRedundantMapPort_Object = MibTableColumn
nbsRoadmRedundantMapPort = _NbsRoadmRedundantMapPort_Object(
    (1, 3, 6, 1, 4, 1, 629, 235, 32, 2, 1, 29),
    _NbsRoadmRedundantMapPort_Type()
)
nbsRoadmRedundantMapPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsRoadmRedundantMapPort.setStatus("current")
_NbsRoadmRedundantSecondaryPort_Type = InterfaceIndex
_NbsRoadmRedundantSecondaryPort_Object = MibTableColumn
nbsRoadmRedundantSecondaryPort = _NbsRoadmRedundantSecondaryPort_Object(
    (1, 3, 6, 1, 4, 1, 629, 235, 32, 2, 1, 30),
    _NbsRoadmRedundantSecondaryPort_Type()
)
nbsRoadmRedundantSecondaryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsRoadmRedundantSecondaryPort.setStatus("current")
_NbsRoadmRedundantCurPort_Type = InterfaceIndex
_NbsRoadmRedundantCurPort_Object = MibTableColumn
nbsRoadmRedundantCurPort = _NbsRoadmRedundantCurPort_Object(
    (1, 3, 6, 1, 4, 1, 629, 235, 32, 2, 1, 40),
    _NbsRoadmRedundantCurPort_Type()
)
nbsRoadmRedundantCurPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsRoadmRedundantCurPort.setStatus("current")
_NbsRoadmRedundantCurAttenu_Type = NbsTcMilliDb
_NbsRoadmRedundantCurAttenu_Object = MibTableColumn
nbsRoadmRedundantCurAttenu = _NbsRoadmRedundantCurAttenu_Object(
    (1, 3, 6, 1, 4, 1, 629, 235, 32, 2, 1, 41),
    _NbsRoadmRedundantCurAttenu_Type()
)
nbsRoadmRedundantCurAttenu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsRoadmRedundantCurAttenu.setStatus("current")


class _NbsRoadmRedundantCurState_Type(Integer32):
    """Custom type nbsRoadmRedundantCurState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("switching", 1))
    )


_NbsRoadmRedundantCurState_Type.__name__ = "Integer32"
_NbsRoadmRedundantCurState_Object = MibTableColumn
nbsRoadmRedundantCurState = _NbsRoadmRedundantCurState_Object(
    (1, 3, 6, 1, 4, 1, 629, 235, 32, 2, 1, 50),
    _NbsRoadmRedundantCurState_Type()
)
nbsRoadmRedundantCurState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsRoadmRedundantCurState.setStatus("current")
_NbsRoadmTraps_ObjectIdentity = ObjectIdentity
nbsRoadmTraps = _NbsRoadmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 235, 100)
)
if mibBuilder.loadTexts:
    nbsRoadmTraps.setStatus("current")
_NbsRoadmEvent_ObjectIdentity = ObjectIdentity
nbsRoadmEvent = _NbsRoadmEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 235, 100, 0)
)
if mibBuilder.loadTexts:
    nbsRoadmEvent.setStatus("current")

# Managed Objects groups


# Notification objects

nbsRoadmEventStageAreaCommitted = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 235, 100, 0, 10)
)
nbsRoadmEventStageAreaCommitted.setObjects(
      *(("NBS-ROADM-MIB", "nbsRoadmCommonIfIndex"),
        ("IF-MIB", "ifAlias"),
        ("NBS-ROADM-MIB", "nbsRoadmCommonCommittedGridType"),
        ("NBS-ROADM-MIB", "nbsRoadmCommonCommittedChannels"))
)
if mibBuilder.loadTexts:
    nbsRoadmEventStageAreaCommitted.setStatus(
        "current"
    )

nbsRoadmEventRedundancyTriggered = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 235, 100, 0, 20)
)
nbsRoadmEventRedundancyTriggered.setObjects(
      *(("NBS-ROADM-MIB", "nbsRoadmRedundantIfIndex"),
        ("NBS-ROADM-MIB", "nbsRoadmRedundantCenterline"))
)
if mibBuilder.loadTexts:
    nbsRoadmEventRedundancyTriggered.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NBS-ROADM-MIB",
    **{"nbsRoadmMib": nbsRoadmMib,
       "nbsRoadmCommonGrp": nbsRoadmCommonGrp,
       "nbsRoadmCommonTableSize": nbsRoadmCommonTableSize,
       "nbsRoadmCommonTable": nbsRoadmCommonTable,
       "nbsRoadmCommonEntry": nbsRoadmCommonEntry,
       "nbsRoadmCommonIfIndex": nbsRoadmCommonIfIndex,
       "nbsRoadmCommonStagingQuickCfg": nbsRoadmCommonStagingQuickCfg,
       "nbsRoadmCommonStagingAddCaps": nbsRoadmCommonStagingAddCaps,
       "nbsRoadmCommonStagingDropCaps": nbsRoadmCommonStagingDropCaps,
       "nbsRoadmCommonStagingCommit": nbsRoadmCommonStagingCommit,
       "nbsRoadmCommonCommittedGridType": nbsRoadmCommonCommittedGridType,
       "nbsRoadmCommonCommittedChannels": nbsRoadmCommonCommittedChannels,
       "nbsRoadmFlexgridGrp": nbsRoadmFlexgridGrp,
       "nbsRoadmFlexgridTableSize": nbsRoadmFlexgridTableSize,
       "nbsRoadmFlexgridTable": nbsRoadmFlexgridTable,
       "nbsRoadmFlexgridEntry": nbsRoadmFlexgridEntry,
       "nbsRoadmFlexgridIfIndex": nbsRoadmFlexgridIfIndex,
       "nbsRoadmFlexgridCenterlineMin": nbsRoadmFlexgridCenterlineMin,
       "nbsRoadmFlexgridCenterlineMax": nbsRoadmFlexgridCenterlineMax,
       "nbsRoadmFlexgridCenterlineIncr": nbsRoadmFlexgridCenterlineIncr,
       "nbsRoadmFlexgridBandwidthMin": nbsRoadmFlexgridBandwidthMin,
       "nbsRoadmFlexgridBandwidthMax": nbsRoadmFlexgridBandwidthMax,
       "nbsRoadmFlexgridBandwidthIncr": nbsRoadmFlexgridBandwidthIncr,
       "nbsRoadmStagingGrp": nbsRoadmStagingGrp,
       "nbsRoadmStagingTableSize": nbsRoadmStagingTableSize,
       "nbsRoadmStagingTable": nbsRoadmStagingTable,
       "nbsRoadmStagingEntry": nbsRoadmStagingEntry,
       "nbsRoadmStagingIfIndex": nbsRoadmStagingIfIndex,
       "nbsRoadmStagingCenterline": nbsRoadmStagingCenterline,
       "nbsRoadmStagingBandwidth": nbsRoadmStagingBandwidth,
       "nbsRoadmStagingChannelName": nbsRoadmStagingChannelName,
       "nbsRoadmStagingAddPort": nbsRoadmStagingAddPort,
       "nbsRoadmStagingDropPort": nbsRoadmStagingDropPort,
       "nbsRoadmStagingSecondaryPort": nbsRoadmStagingSecondaryPort,
       "nbsRoadmStagingSecondAttenu": nbsRoadmStagingSecondAttenu,
       "nbsRoadmStagingAddAttenu": nbsRoadmStagingAddAttenu,
       "nbsRoadmStagingDropAttenu": nbsRoadmStagingDropAttenu,
       "nbsRoadmStagingItuName": nbsRoadmStagingItuName,
       "nbsRoadmStagingRowStatus": nbsRoadmStagingRowStatus,
       "nbsRoadmCommittedGrp": nbsRoadmCommittedGrp,
       "nbsRoadmCommittedTableSize": nbsRoadmCommittedTableSize,
       "nbsRoadmCommittedTable": nbsRoadmCommittedTable,
       "nbsRoadmCommittedEntry": nbsRoadmCommittedEntry,
       "nbsRoadmCommittedIfIndex": nbsRoadmCommittedIfIndex,
       "nbsRoadmCommittedCenterline": nbsRoadmCommittedCenterline,
       "nbsRoadmCommittedBandwidth": nbsRoadmCommittedBandwidth,
       "nbsRoadmCommittedChannelName": nbsRoadmCommittedChannelName,
       "nbsRoadmCommittedAddPort": nbsRoadmCommittedAddPort,
       "nbsRoadmCommittedDropPort": nbsRoadmCommittedDropPort,
       "nbsRoadmCommittedSecondaryPort": nbsRoadmCommittedSecondaryPort,
       "nbsRoadmCommittedSecondAttenu": nbsRoadmCommittedSecondAttenu,
       "nbsRoadmCommittedAddAttenu": nbsRoadmCommittedAddAttenu,
       "nbsRoadmCommittedDropAttenu": nbsRoadmCommittedDropAttenu,
       "nbsRoadmCommittedItuName": nbsRoadmCommittedItuName,
       "nbsRoadmRedundantGrp": nbsRoadmRedundantGrp,
       "nbsRoadmRedundantTableSize": nbsRoadmRedundantTableSize,
       "nbsRoadmRedundantTable": nbsRoadmRedundantTable,
       "nbsRoadmRedundantEntry": nbsRoadmRedundantEntry,
       "nbsRoadmRedundantIfIndex": nbsRoadmRedundantIfIndex,
       "nbsRoadmRedundantCenterline": nbsRoadmRedundantCenterline,
       "nbsRoadmRedundantItuName": nbsRoadmRedundantItuName,
       "nbsRoadmRedundantChannelName": nbsRoadmRedundantChannelName,
       "nbsRoadmRedundantMapPort": nbsRoadmRedundantMapPort,
       "nbsRoadmRedundantSecondaryPort": nbsRoadmRedundantSecondaryPort,
       "nbsRoadmRedundantCurPort": nbsRoadmRedundantCurPort,
       "nbsRoadmRedundantCurAttenu": nbsRoadmRedundantCurAttenu,
       "nbsRoadmRedundantCurState": nbsRoadmRedundantCurState,
       "nbsRoadmTraps": nbsRoadmTraps,
       "nbsRoadmEvent": nbsRoadmEvent,
       "nbsRoadmEventStageAreaCommitted": nbsRoadmEventStageAreaCommitted,
       "nbsRoadmEventRedundancyTriggered": nbsRoadmEventRedundancyTriggered}
)
