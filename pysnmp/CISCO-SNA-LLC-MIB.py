# SNMP MIB module (CISCO-SNA-LLC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SNA-LLC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:57:26 2024
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

ciscoSnaLlcMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 8)
)
ciscoSnaLlcMIB.setRevisions(
        ("1995-05-10 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoSnaLlcMIBObjects_ObjectIdentity = ObjectIdentity
ciscoSnaLlcMIBObjects = _CiscoSnaLlcMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1)
)
_LlcPortGroup_ObjectIdentity = ObjectIdentity
llcPortGroup = _LlcPortGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 1)
)
_LlcPortAdminTable_Object = MibTable
llcPortAdminTable = _LlcPortAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 1, 1)
)
if mibBuilder.loadTexts:
    llcPortAdminTable.setStatus("current")
_LlcPortAdminEntry_Object = MibTableRow
llcPortAdminEntry = _LlcPortAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 1, 1, 1)
)
llcPortAdminEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-SNA-LLC-MIB", "llcPortVirtualIndex"),
)
if mibBuilder.loadTexts:
    llcPortAdminEntry.setStatus("current")


class _LlcPortVirtualIndex_Type(Integer32):
    """Custom type llcPortVirtualIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LlcPortVirtualIndex_Type.__name__ = "Integer32"
_LlcPortVirtualIndex_Object = MibTableColumn
llcPortVirtualIndex = _LlcPortVirtualIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 1, 1, 1, 1),
    _LlcPortVirtualIndex_Type()
)
llcPortVirtualIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    llcPortVirtualIndex.setStatus("current")


class _LlcPortAdminName_Type(DisplayString):
    """Custom type llcPortAdminName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_LlcPortAdminName_Type.__name__ = "DisplayString"
_LlcPortAdminName_Object = MibTableColumn
llcPortAdminName = _LlcPortAdminName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 1, 1, 1, 2),
    _LlcPortAdminName_Type()
)
llcPortAdminName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcPortAdminName.setStatus("current")
_LlcPortAdminMaxSaps_Type = Gauge32
_LlcPortAdminMaxSaps_Object = MibTableColumn
llcPortAdminMaxSaps = _LlcPortAdminMaxSaps_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 1, 1, 1, 3),
    _LlcPortAdminMaxSaps_Type()
)
llcPortAdminMaxSaps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcPortAdminMaxSaps.setStatus("current")
_LlcPortAdminMaxCcs_Type = Gauge32
_LlcPortAdminMaxCcs_Object = MibTableColumn
llcPortAdminMaxCcs = _LlcPortAdminMaxCcs_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 1, 1, 1, 4),
    _LlcPortAdminMaxCcs_Type()
)
llcPortAdminMaxCcs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcPortAdminMaxCcs.setStatus("current")
_LlcPortAdminMaxPDUOctets_Type = Integer32
_LlcPortAdminMaxPDUOctets_Object = MibTableColumn
llcPortAdminMaxPDUOctets = _LlcPortAdminMaxPDUOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 1, 1, 1, 5),
    _LlcPortAdminMaxPDUOctets_Type()
)
llcPortAdminMaxPDUOctets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcPortAdminMaxPDUOctets.setStatus("current")
if mibBuilder.loadTexts:
    llcPortAdminMaxPDUOctets.setUnits("octets")


class _LlcPortAdminMaxUnackedIPDUsSend_Type(Integer32):
    """Custom type llcPortAdminMaxUnackedIPDUsSend based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_LlcPortAdminMaxUnackedIPDUsSend_Type.__name__ = "Integer32"
_LlcPortAdminMaxUnackedIPDUsSend_Object = MibTableColumn
llcPortAdminMaxUnackedIPDUsSend = _LlcPortAdminMaxUnackedIPDUsSend_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 1, 1, 1, 6),
    _LlcPortAdminMaxUnackedIPDUsSend_Type()
)
llcPortAdminMaxUnackedIPDUsSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcPortAdminMaxUnackedIPDUsSend.setStatus("current")


class _LlcPortAdminMaxUnackedIPDUsRcv_Type(Integer32):
    """Custom type llcPortAdminMaxUnackedIPDUsRcv based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_LlcPortAdminMaxUnackedIPDUsRcv_Type.__name__ = "Integer32"
_LlcPortAdminMaxUnackedIPDUsRcv_Object = MibTableColumn
llcPortAdminMaxUnackedIPDUsRcv = _LlcPortAdminMaxUnackedIPDUsRcv_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 1, 1, 1, 7),
    _LlcPortAdminMaxUnackedIPDUsRcv_Type()
)
llcPortAdminMaxUnackedIPDUsRcv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcPortAdminMaxUnackedIPDUsRcv.setStatus("current")


class _LlcPortAdminMaxRetransmits_Type(Integer32):
    """Custom type llcPortAdminMaxRetransmits based on Integer32"""
    defaultValue = 2


_LlcPortAdminMaxRetransmits_Object = MibTableColumn
llcPortAdminMaxRetransmits = _LlcPortAdminMaxRetransmits_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 1, 1, 1, 8),
    _LlcPortAdminMaxRetransmits_Type()
)
llcPortAdminMaxRetransmits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcPortAdminMaxRetransmits.setStatus("current")


class _LlcPortAdminAckTimer_Type(TimeTicks):
    """Custom type llcPortAdminAckTimer based on TimeTicks"""
    defaultValue = 300


_LlcPortAdminAckTimer_Object = MibTableColumn
llcPortAdminAckTimer = _LlcPortAdminAckTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 1, 1, 1, 9),
    _LlcPortAdminAckTimer_Type()
)
llcPortAdminAckTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcPortAdminAckTimer.setStatus("current")


class _LlcPortAdminPbitTimer_Type(TimeTicks):
    """Custom type llcPortAdminPbitTimer based on TimeTicks"""
    defaultValue = 300


_LlcPortAdminPbitTimer_Object = MibTableColumn
llcPortAdminPbitTimer = _LlcPortAdminPbitTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 1, 1, 1, 10),
    _LlcPortAdminPbitTimer_Type()
)
llcPortAdminPbitTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcPortAdminPbitTimer.setStatus("current")


class _LlcPortAdminRejTimer_Type(TimeTicks):
    """Custom type llcPortAdminRejTimer based on TimeTicks"""
    defaultValue = 300


_LlcPortAdminRejTimer_Object = MibTableColumn
llcPortAdminRejTimer = _LlcPortAdminRejTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 1, 1, 1, 11),
    _LlcPortAdminRejTimer_Type()
)
llcPortAdminRejTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcPortAdminRejTimer.setStatus("current")


class _LlcPortAdminBusyTimer_Type(TimeTicks):
    """Custom type llcPortAdminBusyTimer based on TimeTicks"""
    defaultValue = 30000


_LlcPortAdminBusyTimer_Object = MibTableColumn
llcPortAdminBusyTimer = _LlcPortAdminBusyTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 1, 1, 1, 12),
    _LlcPortAdminBusyTimer_Type()
)
llcPortAdminBusyTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcPortAdminBusyTimer.setStatus("current")


class _LlcPortAdminInactTimer_Type(TimeTicks):
    """Custom type llcPortAdminInactTimer based on TimeTicks"""
    defaultValue = 3000


_LlcPortAdminInactTimer_Object = MibTableColumn
llcPortAdminInactTimer = _LlcPortAdminInactTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 1, 1, 1, 13),
    _LlcPortAdminInactTimer_Type()
)
llcPortAdminInactTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcPortAdminInactTimer.setStatus("current")


class _LlcPortAdminDelayAckCount_Type(Integer32):
    """Custom type llcPortAdminDelayAckCount based on Integer32"""
    defaultValue = 1


_LlcPortAdminDelayAckCount_Object = MibTableColumn
llcPortAdminDelayAckCount = _LlcPortAdminDelayAckCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 1, 1, 1, 14),
    _LlcPortAdminDelayAckCount_Type()
)
llcPortAdminDelayAckCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcPortAdminDelayAckCount.setStatus("current")


class _LlcPortAdminDelayAckTimer_Type(TimeTicks):
    """Custom type llcPortAdminDelayAckTimer based on TimeTicks"""
    defaultValue = 100


_LlcPortAdminDelayAckTimer_Object = MibTableColumn
llcPortAdminDelayAckTimer = _LlcPortAdminDelayAckTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 1, 1, 1, 15),
    _LlcPortAdminDelayAckTimer_Type()
)
llcPortAdminDelayAckTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcPortAdminDelayAckTimer.setStatus("current")


class _LlcPortAdminNw_Type(Integer32):
    """Custom type llcPortAdminNw based on Integer32"""
    defaultValue = 4


_LlcPortAdminNw_Object = MibTableColumn
llcPortAdminNw = _LlcPortAdminNw_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 1, 1, 1, 16),
    _LlcPortAdminNw_Type()
)
llcPortAdminNw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcPortAdminNw.setStatus("current")
_LlcPortOperTable_Object = MibTable
llcPortOperTable = _LlcPortOperTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 1, 2)
)
if mibBuilder.loadTexts:
    llcPortOperTable.setStatus("current")
_LlcPortOperEntry_Object = MibTableRow
llcPortOperEntry = _LlcPortOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 1, 2, 1)
)
llcPortOperEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-SNA-LLC-MIB", "llcPortVirtualIndex"),
)
if mibBuilder.loadTexts:
    llcPortOperEntry.setStatus("current")
_LlcPortOperMacAddress_Type = MacAddress
_LlcPortOperMacAddress_Object = MibTableColumn
llcPortOperMacAddress = _LlcPortOperMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 1, 2, 1, 1),
    _LlcPortOperMacAddress_Type()
)
llcPortOperMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcPortOperMacAddress.setStatus("current")
_LlcPortOperNumSaps_Type = Gauge32
_LlcPortOperNumSaps_Object = MibTableColumn
llcPortOperNumSaps = _LlcPortOperNumSaps_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 1, 2, 1, 2),
    _LlcPortOperNumSaps_Type()
)
llcPortOperNumSaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcPortOperNumSaps.setStatus("current")
_LlcPortOperHiWaterNumSaps_Type = Gauge32
_LlcPortOperHiWaterNumSaps_Object = MibTableColumn
llcPortOperHiWaterNumSaps = _LlcPortOperHiWaterNumSaps_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 1, 2, 1, 3),
    _LlcPortOperHiWaterNumSaps_Type()
)
llcPortOperHiWaterNumSaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcPortOperHiWaterNumSaps.setStatus("current")


class _LlcPortOperSimRim_Type(Integer32):
    """Custom type llcPortOperSimRim based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_LlcPortOperSimRim_Type.__name__ = "Integer32"
_LlcPortOperSimRim_Object = MibTableColumn
llcPortOperSimRim = _LlcPortOperSimRim_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 1, 2, 1, 4),
    _LlcPortOperSimRim_Type()
)
llcPortOperSimRim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcPortOperSimRim.setStatus("current")
_LlcPortOperLastModifyTime_Type = TimeStamp
_LlcPortOperLastModifyTime_Object = MibTableColumn
llcPortOperLastModifyTime = _LlcPortOperLastModifyTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 1, 2, 1, 5),
    _LlcPortOperLastModifyTime_Type()
)
llcPortOperLastModifyTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcPortOperLastModifyTime.setStatus("current")
_LlcPortStatsTable_Object = MibTable
llcPortStatsTable = _LlcPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 1, 3)
)
if mibBuilder.loadTexts:
    llcPortStatsTable.setStatus("current")
_LlcPortStatsEntry_Object = MibTableRow
llcPortStatsEntry = _LlcPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 1, 3, 1)
)
llcPortStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-SNA-LLC-MIB", "llcPortVirtualIndex"),
)
if mibBuilder.loadTexts:
    llcPortStatsEntry.setStatus("current")
_LlcPortStatsPDUsIn_Type = Counter32
_LlcPortStatsPDUsIn_Object = MibTableColumn
llcPortStatsPDUsIn = _LlcPortStatsPDUsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 1, 3, 1, 1),
    _LlcPortStatsPDUsIn_Type()
)
llcPortStatsPDUsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcPortStatsPDUsIn.setStatus("current")
_LlcPortStatsPDUsOut_Type = Counter32
_LlcPortStatsPDUsOut_Object = MibTableColumn
llcPortStatsPDUsOut = _LlcPortStatsPDUsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 1, 3, 1, 2),
    _LlcPortStatsPDUsOut_Type()
)
llcPortStatsPDUsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcPortStatsPDUsOut.setStatus("current")
_LlcPortStatsOctetsIn_Type = Counter32
_LlcPortStatsOctetsIn_Object = MibTableColumn
llcPortStatsOctetsIn = _LlcPortStatsOctetsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 1, 3, 1, 3),
    _LlcPortStatsOctetsIn_Type()
)
llcPortStatsOctetsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcPortStatsOctetsIn.setStatus("current")
if mibBuilder.loadTexts:
    llcPortStatsOctetsIn.setUnits("octets")
_LlcPortStatsOctetsOut_Type = Counter32
_LlcPortStatsOctetsOut_Object = MibTableColumn
llcPortStatsOctetsOut = _LlcPortStatsOctetsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 1, 3, 1, 4),
    _LlcPortStatsOctetsOut_Type()
)
llcPortStatsOctetsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcPortStatsOctetsOut.setStatus("current")
if mibBuilder.loadTexts:
    llcPortStatsOctetsOut.setUnits("octets")
_LlcPortStatsTESTCommandsIn_Type = Counter32
_LlcPortStatsTESTCommandsIn_Object = MibTableColumn
llcPortStatsTESTCommandsIn = _LlcPortStatsTESTCommandsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 1, 3, 1, 5),
    _LlcPortStatsTESTCommandsIn_Type()
)
llcPortStatsTESTCommandsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcPortStatsTESTCommandsIn.setStatus("current")
_LlcPortStatsTESTResponsesOut_Type = Counter32
_LlcPortStatsTESTResponsesOut_Object = MibTableColumn
llcPortStatsTESTResponsesOut = _LlcPortStatsTESTResponsesOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 1, 3, 1, 6),
    _LlcPortStatsTESTResponsesOut_Type()
)
llcPortStatsTESTResponsesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcPortStatsTESTResponsesOut.setStatus("current")
_LlcPortStatsLocalBusies_Type = Counter32
_LlcPortStatsLocalBusies_Object = MibTableColumn
llcPortStatsLocalBusies = _LlcPortStatsLocalBusies_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 1, 3, 1, 7),
    _LlcPortStatsLocalBusies_Type()
)
llcPortStatsLocalBusies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcPortStatsLocalBusies.setStatus("current")
_LlcPortStatsUnknownSaps_Type = Counter32
_LlcPortStatsUnknownSaps_Object = MibTableColumn
llcPortStatsUnknownSaps = _LlcPortStatsUnknownSaps_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 1, 3, 1, 8),
    _LlcPortStatsUnknownSaps_Type()
)
llcPortStatsUnknownSaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcPortStatsUnknownSaps.setStatus("current")
_LlcSapGroup_ObjectIdentity = ObjectIdentity
llcSapGroup = _LlcSapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 2)
)
_LlcSapAdminTable_Object = MibTable
llcSapAdminTable = _LlcSapAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 2, 1)
)
if mibBuilder.loadTexts:
    llcSapAdminTable.setStatus("current")
_LlcSapAdminEntry_Object = MibTableRow
llcSapAdminEntry = _LlcSapAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 2, 1, 1)
)
llcSapAdminEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-SNA-LLC-MIB", "llcPortVirtualIndex"),
    (0, "CISCO-SNA-LLC-MIB", "llcSapNumber"),
)
if mibBuilder.loadTexts:
    llcSapAdminEntry.setStatus("current")


class _LlcSapNumber_Type(Integer32):
    """Custom type llcSapNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_LlcSapNumber_Type.__name__ = "Integer32"
_LlcSapNumber_Object = MibTableColumn
llcSapNumber = _LlcSapNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 2, 1, 1, 1),
    _LlcSapNumber_Type()
)
llcSapNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    llcSapNumber.setStatus("current")


class _LlcSapAdminMaxPDUOctets_Type(Integer32):
    """Custom type llcSapAdminMaxPDUOctets based on Integer32"""
    defaultValue = 0


_LlcSapAdminMaxPDUOctets_Object = MibTableColumn
llcSapAdminMaxPDUOctets = _LlcSapAdminMaxPDUOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 2, 1, 1, 2),
    _LlcSapAdminMaxPDUOctets_Type()
)
llcSapAdminMaxPDUOctets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcSapAdminMaxPDUOctets.setStatus("current")
if mibBuilder.loadTexts:
    llcSapAdminMaxPDUOctets.setUnits("octets")


class _LlcSapAdminMaxUnackedIPDUsSend_Type(Integer32):
    """Custom type llcSapAdminMaxUnackedIPDUsSend based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_LlcSapAdminMaxUnackedIPDUsSend_Type.__name__ = "Integer32"
_LlcSapAdminMaxUnackedIPDUsSend_Object = MibTableColumn
llcSapAdminMaxUnackedIPDUsSend = _LlcSapAdminMaxUnackedIPDUsSend_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 2, 1, 1, 3),
    _LlcSapAdminMaxUnackedIPDUsSend_Type()
)
llcSapAdminMaxUnackedIPDUsSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcSapAdminMaxUnackedIPDUsSend.setStatus("current")


class _LlcSapAdminMaxUnackedIPDUsRcv_Type(Integer32):
    """Custom type llcSapAdminMaxUnackedIPDUsRcv based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_LlcSapAdminMaxUnackedIPDUsRcv_Type.__name__ = "Integer32"
_LlcSapAdminMaxUnackedIPDUsRcv_Object = MibTableColumn
llcSapAdminMaxUnackedIPDUsRcv = _LlcSapAdminMaxUnackedIPDUsRcv_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 2, 1, 1, 4),
    _LlcSapAdminMaxUnackedIPDUsRcv_Type()
)
llcSapAdminMaxUnackedIPDUsRcv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcSapAdminMaxUnackedIPDUsRcv.setStatus("current")


class _LlcSapAdminMaxRetransmits_Type(Integer32):
    """Custom type llcSapAdminMaxRetransmits based on Integer32"""
    defaultValue = 0


_LlcSapAdminMaxRetransmits_Object = MibTableColumn
llcSapAdminMaxRetransmits = _LlcSapAdminMaxRetransmits_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 2, 1, 1, 5),
    _LlcSapAdminMaxRetransmits_Type()
)
llcSapAdminMaxRetransmits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcSapAdminMaxRetransmits.setStatus("current")


class _LlcSapAdminAckTimer_Type(TimeTicks):
    """Custom type llcSapAdminAckTimer based on TimeTicks"""
    defaultValue = 0


_LlcSapAdminAckTimer_Object = MibTableColumn
llcSapAdminAckTimer = _LlcSapAdminAckTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 2, 1, 1, 6),
    _LlcSapAdminAckTimer_Type()
)
llcSapAdminAckTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcSapAdminAckTimer.setStatus("current")


class _LlcSapAdminPbitTimer_Type(TimeTicks):
    """Custom type llcSapAdminPbitTimer based on TimeTicks"""
    defaultValue = 0


_LlcSapAdminPbitTimer_Object = MibTableColumn
llcSapAdminPbitTimer = _LlcSapAdminPbitTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 2, 1, 1, 7),
    _LlcSapAdminPbitTimer_Type()
)
llcSapAdminPbitTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcSapAdminPbitTimer.setStatus("current")


class _LlcSapAdminRejTimer_Type(TimeTicks):
    """Custom type llcSapAdminRejTimer based on TimeTicks"""
    defaultValue = 0


_LlcSapAdminRejTimer_Object = MibTableColumn
llcSapAdminRejTimer = _LlcSapAdminRejTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 2, 1, 1, 8),
    _LlcSapAdminRejTimer_Type()
)
llcSapAdminRejTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcSapAdminRejTimer.setStatus("current")


class _LlcSapAdminBusyTimer_Type(TimeTicks):
    """Custom type llcSapAdminBusyTimer based on TimeTicks"""
    defaultValue = 0


_LlcSapAdminBusyTimer_Object = MibTableColumn
llcSapAdminBusyTimer = _LlcSapAdminBusyTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 2, 1, 1, 9),
    _LlcSapAdminBusyTimer_Type()
)
llcSapAdminBusyTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcSapAdminBusyTimer.setStatus("current")


class _LlcSapAdminInactTimer_Type(TimeTicks):
    """Custom type llcSapAdminInactTimer based on TimeTicks"""
    defaultValue = 0


_LlcSapAdminInactTimer_Object = MibTableColumn
llcSapAdminInactTimer = _LlcSapAdminInactTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 2, 1, 1, 10),
    _LlcSapAdminInactTimer_Type()
)
llcSapAdminInactTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcSapAdminInactTimer.setStatus("current")


class _LlcSapAdminDelayAckCount_Type(Integer32):
    """Custom type llcSapAdminDelayAckCount based on Integer32"""
    defaultValue = 0


_LlcSapAdminDelayAckCount_Object = MibTableColumn
llcSapAdminDelayAckCount = _LlcSapAdminDelayAckCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 2, 1, 1, 11),
    _LlcSapAdminDelayAckCount_Type()
)
llcSapAdminDelayAckCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcSapAdminDelayAckCount.setStatus("current")


class _LlcSapAdminDelayAckTimer_Type(TimeTicks):
    """Custom type llcSapAdminDelayAckTimer based on TimeTicks"""
    defaultValue = 0


_LlcSapAdminDelayAckTimer_Object = MibTableColumn
llcSapAdminDelayAckTimer = _LlcSapAdminDelayAckTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 2, 1, 1, 12),
    _LlcSapAdminDelayAckTimer_Type()
)
llcSapAdminDelayAckTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcSapAdminDelayAckTimer.setStatus("current")
_LlcSapAdminNw_Type = Integer32
_LlcSapAdminNw_Object = MibTableColumn
llcSapAdminNw = _LlcSapAdminNw_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 2, 1, 1, 13),
    _LlcSapAdminNw_Type()
)
llcSapAdminNw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcSapAdminNw.setStatus("current")
_LlcSapOperTable_Object = MibTable
llcSapOperTable = _LlcSapOperTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 2, 2)
)
if mibBuilder.loadTexts:
    llcSapOperTable.setStatus("current")
_LlcSapOperEntry_Object = MibTableRow
llcSapOperEntry = _LlcSapOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 2, 2, 1)
)
llcSapOperEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-SNA-LLC-MIB", "llcPortVirtualIndex"),
    (0, "CISCO-SNA-LLC-MIB", "llcSapNumber"),
)
if mibBuilder.loadTexts:
    llcSapOperEntry.setStatus("current")


class _LlcSapOperStatus_Type(Integer32):
    """Custom type llcSapOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_LlcSapOperStatus_Type.__name__ = "Integer32"
_LlcSapOperStatus_Object = MibTableColumn
llcSapOperStatus = _LlcSapOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 2, 2, 1, 1),
    _LlcSapOperStatus_Type()
)
llcSapOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapOperStatus.setStatus("current")
_LlcSapOperNumCcs_Type = Integer32
_LlcSapOperNumCcs_Object = MibTableColumn
llcSapOperNumCcs = _LlcSapOperNumCcs_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 2, 2, 1, 2),
    _LlcSapOperNumCcs_Type()
)
llcSapOperNumCcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapOperNumCcs.setStatus("current")
_LlcSapOperHiWaterNumCcs_Type = Gauge32
_LlcSapOperHiWaterNumCcs_Object = MibTableColumn
llcSapOperHiWaterNumCcs = _LlcSapOperHiWaterNumCcs_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 2, 2, 1, 3),
    _LlcSapOperHiWaterNumCcs_Type()
)
llcSapOperHiWaterNumCcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapOperHiWaterNumCcs.setStatus("current")


class _LlcSapOperLlc2Support_Type(Integer32):
    """Custom type llcSapOperLlc2Support based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_LlcSapOperLlc2Support_Type.__name__ = "Integer32"
_LlcSapOperLlc2Support_Object = MibTableColumn
llcSapOperLlc2Support = _LlcSapOperLlc2Support_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 2, 2, 1, 4),
    _LlcSapOperLlc2Support_Type()
)
llcSapOperLlc2Support.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapOperLlc2Support.setStatus("current")
_LlcSapStatsTable_Object = MibTable
llcSapStatsTable = _LlcSapStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 2, 3)
)
if mibBuilder.loadTexts:
    llcSapStatsTable.setStatus("current")
_LlcSapStatsEntry_Object = MibTableRow
llcSapStatsEntry = _LlcSapStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 2, 3, 1)
)
llcSapStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-SNA-LLC-MIB", "llcPortVirtualIndex"),
    (0, "CISCO-SNA-LLC-MIB", "llcSapNumber"),
)
if mibBuilder.loadTexts:
    llcSapStatsEntry.setStatus("current")
_LlcSapStatsLocalBusies_Type = Counter32
_LlcSapStatsLocalBusies_Object = MibTableColumn
llcSapStatsLocalBusies = _LlcSapStatsLocalBusies_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 2, 3, 1, 1),
    _LlcSapStatsLocalBusies_Type()
)
llcSapStatsLocalBusies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapStatsLocalBusies.setStatus("current")
_LlcSapStatsRemoteBusies_Type = Counter32
_LlcSapStatsRemoteBusies_Object = MibTableColumn
llcSapStatsRemoteBusies = _LlcSapStatsRemoteBusies_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 2, 3, 1, 2),
    _LlcSapStatsRemoteBusies_Type()
)
llcSapStatsRemoteBusies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapStatsRemoteBusies.setStatus("current")
_LlcSapStatsIFramesIn_Type = Counter32
_LlcSapStatsIFramesIn_Object = MibTableColumn
llcSapStatsIFramesIn = _LlcSapStatsIFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 2, 3, 1, 3),
    _LlcSapStatsIFramesIn_Type()
)
llcSapStatsIFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapStatsIFramesIn.setStatus("current")
_LlcSapStatsIFramesOut_Type = Counter32
_LlcSapStatsIFramesOut_Object = MibTableColumn
llcSapStatsIFramesOut = _LlcSapStatsIFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 2, 3, 1, 4),
    _LlcSapStatsIFramesOut_Type()
)
llcSapStatsIFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapStatsIFramesOut.setStatus("current")
_LlcSapStatsIOctetsIn_Type = Counter32
_LlcSapStatsIOctetsIn_Object = MibTableColumn
llcSapStatsIOctetsIn = _LlcSapStatsIOctetsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 2, 3, 1, 5),
    _LlcSapStatsIOctetsIn_Type()
)
llcSapStatsIOctetsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapStatsIOctetsIn.setStatus("current")
_LlcSapStatsIOctetsOut_Type = Counter32
_LlcSapStatsIOctetsOut_Object = MibTableColumn
llcSapStatsIOctetsOut = _LlcSapStatsIOctetsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 2, 3, 1, 6),
    _LlcSapStatsIOctetsOut_Type()
)
llcSapStatsIOctetsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapStatsIOctetsOut.setStatus("current")
_LlcSapStatsSFramesIn_Type = Counter32
_LlcSapStatsSFramesIn_Object = MibTableColumn
llcSapStatsSFramesIn = _LlcSapStatsSFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 2, 3, 1, 7),
    _LlcSapStatsSFramesIn_Type()
)
llcSapStatsSFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapStatsSFramesIn.setStatus("current")
_LlcSapStatsSFramesOut_Type = Counter32
_LlcSapStatsSFramesOut_Object = MibTableColumn
llcSapStatsSFramesOut = _LlcSapStatsSFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 2, 3, 1, 8),
    _LlcSapStatsSFramesOut_Type()
)
llcSapStatsSFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapStatsSFramesOut.setStatus("current")
_LlcSapStatsRetransmitsOut_Type = Counter32
_LlcSapStatsRetransmitsOut_Object = MibTableColumn
llcSapStatsRetransmitsOut = _LlcSapStatsRetransmitsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 2, 3, 1, 9),
    _LlcSapStatsRetransmitsOut_Type()
)
llcSapStatsRetransmitsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapStatsRetransmitsOut.setStatus("current")
_LlcSapStatsREJsIn_Type = Counter32
_LlcSapStatsREJsIn_Object = MibTableColumn
llcSapStatsREJsIn = _LlcSapStatsREJsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 2, 3, 1, 10),
    _LlcSapStatsREJsIn_Type()
)
llcSapStatsREJsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapStatsREJsIn.setStatus("current")
_LlcSapStatsREJsOut_Type = Counter32
_LlcSapStatsREJsOut_Object = MibTableColumn
llcSapStatsREJsOut = _LlcSapStatsREJsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 2, 3, 1, 11),
    _LlcSapStatsREJsOut_Type()
)
llcSapStatsREJsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapStatsREJsOut.setStatus("current")
_LlcSapStatsWwCount_Type = Counter32
_LlcSapStatsWwCount_Object = MibTableColumn
llcSapStatsWwCount = _LlcSapStatsWwCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 2, 3, 1, 12),
    _LlcSapStatsWwCount_Type()
)
llcSapStatsWwCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapStatsWwCount.setStatus("current")
_LlcSapStatsTESTCommandsIn_Type = Counter32
_LlcSapStatsTESTCommandsIn_Object = MibTableColumn
llcSapStatsTESTCommandsIn = _LlcSapStatsTESTCommandsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 2, 3, 1, 13),
    _LlcSapStatsTESTCommandsIn_Type()
)
llcSapStatsTESTCommandsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapStatsTESTCommandsIn.setStatus("current")
_LlcSapStatsTESTCommandsOut_Type = Counter32
_LlcSapStatsTESTCommandsOut_Object = MibTableColumn
llcSapStatsTESTCommandsOut = _LlcSapStatsTESTCommandsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 2, 3, 1, 14),
    _LlcSapStatsTESTCommandsOut_Type()
)
llcSapStatsTESTCommandsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapStatsTESTCommandsOut.setStatus("current")
_LlcSapStatsTESTResponsesIn_Type = Counter32
_LlcSapStatsTESTResponsesIn_Object = MibTableColumn
llcSapStatsTESTResponsesIn = _LlcSapStatsTESTResponsesIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 2, 3, 1, 15),
    _LlcSapStatsTESTResponsesIn_Type()
)
llcSapStatsTESTResponsesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapStatsTESTResponsesIn.setStatus("current")
_LlcSapStatsTESTResponsesOut_Type = Counter32
_LlcSapStatsTESTResponsesOut_Object = MibTableColumn
llcSapStatsTESTResponsesOut = _LlcSapStatsTESTResponsesOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 2, 3, 1, 16),
    _LlcSapStatsTESTResponsesOut_Type()
)
llcSapStatsTESTResponsesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapStatsTESTResponsesOut.setStatus("current")
_LlcSapStatsXIDCommandsIn_Type = Counter32
_LlcSapStatsXIDCommandsIn_Object = MibTableColumn
llcSapStatsXIDCommandsIn = _LlcSapStatsXIDCommandsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 2, 3, 1, 17),
    _LlcSapStatsXIDCommandsIn_Type()
)
llcSapStatsXIDCommandsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapStatsXIDCommandsIn.setStatus("current")
_LlcSapStatsXIDCommandsOut_Type = Counter32
_LlcSapStatsXIDCommandsOut_Object = MibTableColumn
llcSapStatsXIDCommandsOut = _LlcSapStatsXIDCommandsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 2, 3, 1, 18),
    _LlcSapStatsXIDCommandsOut_Type()
)
llcSapStatsXIDCommandsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapStatsXIDCommandsOut.setStatus("current")
_LlcSapStatsXIDResponsesIn_Type = Counter32
_LlcSapStatsXIDResponsesIn_Object = MibTableColumn
llcSapStatsXIDResponsesIn = _LlcSapStatsXIDResponsesIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 2, 3, 1, 19),
    _LlcSapStatsXIDResponsesIn_Type()
)
llcSapStatsXIDResponsesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapStatsXIDResponsesIn.setStatus("current")
_LlcSapStatsXIDResponsesOut_Type = Counter32
_LlcSapStatsXIDResponsesOut_Object = MibTableColumn
llcSapStatsXIDResponsesOut = _LlcSapStatsXIDResponsesOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 2, 3, 1, 20),
    _LlcSapStatsXIDResponsesOut_Type()
)
llcSapStatsXIDResponsesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapStatsXIDResponsesOut.setStatus("current")
_LlcSapStatsUIFramesIn_Type = Counter32
_LlcSapStatsUIFramesIn_Object = MibTableColumn
llcSapStatsUIFramesIn = _LlcSapStatsUIFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 2, 3, 1, 21),
    _LlcSapStatsUIFramesIn_Type()
)
llcSapStatsUIFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapStatsUIFramesIn.setStatus("current")
_LlcSapStatsUIFramesOut_Type = Counter32
_LlcSapStatsUIFramesOut_Object = MibTableColumn
llcSapStatsUIFramesOut = _LlcSapStatsUIFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 2, 3, 1, 22),
    _LlcSapStatsUIFramesOut_Type()
)
llcSapStatsUIFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapStatsUIFramesOut.setStatus("current")
_LlcSapStatsUIOctetsIn_Type = Counter32
_LlcSapStatsUIOctetsIn_Object = MibTableColumn
llcSapStatsUIOctetsIn = _LlcSapStatsUIOctetsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 2, 3, 1, 23),
    _LlcSapStatsUIOctetsIn_Type()
)
llcSapStatsUIOctetsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapStatsUIOctetsIn.setStatus("current")
_LlcSapStatsUIOctetsOut_Type = Counter32
_LlcSapStatsUIOctetsOut_Object = MibTableColumn
llcSapStatsUIOctetsOut = _LlcSapStatsUIOctetsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 2, 3, 1, 24),
    _LlcSapStatsUIOctetsOut_Type()
)
llcSapStatsUIOctetsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapStatsUIOctetsOut.setStatus("current")
_LlcSapStatsConnectOk_Type = Counter32
_LlcSapStatsConnectOk_Object = MibTableColumn
llcSapStatsConnectOk = _LlcSapStatsConnectOk_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 2, 3, 1, 25),
    _LlcSapStatsConnectOk_Type()
)
llcSapStatsConnectOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapStatsConnectOk.setStatus("current")
_LlcSapStatsConnectFail_Type = Counter32
_LlcSapStatsConnectFail_Object = MibTableColumn
llcSapStatsConnectFail = _LlcSapStatsConnectFail_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 2, 3, 1, 26),
    _LlcSapStatsConnectFail_Type()
)
llcSapStatsConnectFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapStatsConnectFail.setStatus("current")
_LlcSapStatsDisconnect_Type = Counter32
_LlcSapStatsDisconnect_Object = MibTableColumn
llcSapStatsDisconnect = _LlcSapStatsDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 2, 3, 1, 27),
    _LlcSapStatsDisconnect_Type()
)
llcSapStatsDisconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapStatsDisconnect.setStatus("current")
_LlcSapStatsDisconnectFRMRSend_Type = Counter32
_LlcSapStatsDisconnectFRMRSend_Object = MibTableColumn
llcSapStatsDisconnectFRMRSend = _LlcSapStatsDisconnectFRMRSend_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 2, 3, 1, 28),
    _LlcSapStatsDisconnectFRMRSend_Type()
)
llcSapStatsDisconnectFRMRSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapStatsDisconnectFRMRSend.setStatus("current")
_LlcSapStatsDisconnectFRMRRcv_Type = Counter32
_LlcSapStatsDisconnectFRMRRcv_Object = MibTableColumn
llcSapStatsDisconnectFRMRRcv = _LlcSapStatsDisconnectFRMRRcv_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 2, 3, 1, 29),
    _LlcSapStatsDisconnectFRMRRcv_Type()
)
llcSapStatsDisconnectFRMRRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapStatsDisconnectFRMRRcv.setStatus("current")
_LlcSapStatsDisconnectTimer_Type = Counter32
_LlcSapStatsDisconnectTimer_Object = MibTableColumn
llcSapStatsDisconnectTimer = _LlcSapStatsDisconnectTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 2, 3, 1, 30),
    _LlcSapStatsDisconnectTimer_Type()
)
llcSapStatsDisconnectTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapStatsDisconnectTimer.setStatus("current")
_LlcSapStatsDMsInABM_Type = Counter32
_LlcSapStatsDMsInABM_Object = MibTableColumn
llcSapStatsDMsInABM = _LlcSapStatsDMsInABM_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 2, 3, 1, 31),
    _LlcSapStatsDMsInABM_Type()
)
llcSapStatsDMsInABM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapStatsDMsInABM.setStatus("current")
_LlcSapStatsSABMEsInABM_Type = Counter32
_LlcSapStatsSABMEsInABM_Object = MibTableColumn
llcSapStatsSABMEsInABM = _LlcSapStatsSABMEsInABM_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 2, 3, 1, 32),
    _LlcSapStatsSABMEsInABM_Type()
)
llcSapStatsSABMEsInABM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapStatsSABMEsInABM.setStatus("current")
_LlcCcGroup_ObjectIdentity = ObjectIdentity
llcCcGroup = _LlcCcGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 3)
)
_LlcCcAdminTable_Object = MibTable
llcCcAdminTable = _LlcCcAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 3, 1)
)
if mibBuilder.loadTexts:
    llcCcAdminTable.setStatus("current")
_LlcCcAdminEntry_Object = MibTableRow
llcCcAdminEntry = _LlcCcAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 3, 1, 1)
)
llcCcAdminEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-SNA-LLC-MIB", "llcPortVirtualIndex"),
    (0, "CISCO-SNA-LLC-MIB", "llcSapNumber"),
    (0, "CISCO-SNA-LLC-MIB", "llcCcRMac"),
    (0, "CISCO-SNA-LLC-MIB", "llcCcRSap"),
)
if mibBuilder.loadTexts:
    llcCcAdminEntry.setStatus("current")
_LlcCcRMac_Type = MacAddress
_LlcCcRMac_Object = MibTableColumn
llcCcRMac = _LlcCcRMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 3, 1, 1, 1),
    _LlcCcRMac_Type()
)
llcCcRMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    llcCcRMac.setStatus("current")


class _LlcCcRSap_Type(Integer32):
    """Custom type llcCcRSap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_LlcCcRSap_Type.__name__ = "Integer32"
_LlcCcRSap_Object = MibTableColumn
llcCcRSap = _LlcCcRSap_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 3, 1, 1, 2),
    _LlcCcRSap_Type()
)
llcCcRSap.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    llcCcRSap.setStatus("current")


class _LlcCcAdminBounce_Type(Integer32):
    """Custom type llcCcAdminBounce based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_LlcCcAdminBounce_Type.__name__ = "Integer32"
_LlcCcAdminBounce_Object = MibTableColumn
llcCcAdminBounce = _LlcCcAdminBounce_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 3, 1, 1, 3),
    _LlcCcAdminBounce_Type()
)
llcCcAdminBounce.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    llcCcAdminBounce.setStatus("current")


class _LlcCcAdminMaxPDUOctets_Type(Integer32):
    """Custom type llcCcAdminMaxPDUOctets based on Integer32"""
    defaultValue = 0


_LlcCcAdminMaxPDUOctets_Object = MibTableColumn
llcCcAdminMaxPDUOctets = _LlcCcAdminMaxPDUOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 3, 1, 1, 4),
    _LlcCcAdminMaxPDUOctets_Type()
)
llcCcAdminMaxPDUOctets.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    llcCcAdminMaxPDUOctets.setStatus("current")
if mibBuilder.loadTexts:
    llcCcAdminMaxPDUOctets.setUnits("octets")


class _LlcCcAdminMaxUnackedIPDUsSend_Type(Integer32):
    """Custom type llcCcAdminMaxUnackedIPDUsSend based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_LlcCcAdminMaxUnackedIPDUsSend_Type.__name__ = "Integer32"
_LlcCcAdminMaxUnackedIPDUsSend_Object = MibTableColumn
llcCcAdminMaxUnackedIPDUsSend = _LlcCcAdminMaxUnackedIPDUsSend_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 3, 1, 1, 5),
    _LlcCcAdminMaxUnackedIPDUsSend_Type()
)
llcCcAdminMaxUnackedIPDUsSend.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    llcCcAdminMaxUnackedIPDUsSend.setStatus("current")


class _LlcCcAdminMaxUnackedIPDUsRcv_Type(Integer32):
    """Custom type llcCcAdminMaxUnackedIPDUsRcv based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_LlcCcAdminMaxUnackedIPDUsRcv_Type.__name__ = "Integer32"
_LlcCcAdminMaxUnackedIPDUsRcv_Object = MibTableColumn
llcCcAdminMaxUnackedIPDUsRcv = _LlcCcAdminMaxUnackedIPDUsRcv_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 3, 1, 1, 6),
    _LlcCcAdminMaxUnackedIPDUsRcv_Type()
)
llcCcAdminMaxUnackedIPDUsRcv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    llcCcAdminMaxUnackedIPDUsRcv.setStatus("current")


class _LlcCcAdminMaxRetransmits_Type(Integer32):
    """Custom type llcCcAdminMaxRetransmits based on Integer32"""
    defaultValue = 0


_LlcCcAdminMaxRetransmits_Object = MibTableColumn
llcCcAdminMaxRetransmits = _LlcCcAdminMaxRetransmits_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 3, 1, 1, 7),
    _LlcCcAdminMaxRetransmits_Type()
)
llcCcAdminMaxRetransmits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    llcCcAdminMaxRetransmits.setStatus("current")


class _LlcCcAdminAckTimer_Type(TimeTicks):
    """Custom type llcCcAdminAckTimer based on TimeTicks"""
    defaultValue = 0


_LlcCcAdminAckTimer_Object = MibTableColumn
llcCcAdminAckTimer = _LlcCcAdminAckTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 3, 1, 1, 8),
    _LlcCcAdminAckTimer_Type()
)
llcCcAdminAckTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    llcCcAdminAckTimer.setStatus("current")


class _LlcCcAdminPbitTimer_Type(TimeTicks):
    """Custom type llcCcAdminPbitTimer based on TimeTicks"""
    defaultValue = 0


_LlcCcAdminPbitTimer_Object = MibTableColumn
llcCcAdminPbitTimer = _LlcCcAdminPbitTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 3, 1, 1, 9),
    _LlcCcAdminPbitTimer_Type()
)
llcCcAdminPbitTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    llcCcAdminPbitTimer.setStatus("current")


class _LlcCcAdminRejTimer_Type(TimeTicks):
    """Custom type llcCcAdminRejTimer based on TimeTicks"""
    defaultValue = 0


_LlcCcAdminRejTimer_Object = MibTableColumn
llcCcAdminRejTimer = _LlcCcAdminRejTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 3, 1, 1, 10),
    _LlcCcAdminRejTimer_Type()
)
llcCcAdminRejTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    llcCcAdminRejTimer.setStatus("current")


class _LlcCcAdminBusyTimer_Type(TimeTicks):
    """Custom type llcCcAdminBusyTimer based on TimeTicks"""
    defaultValue = 0


_LlcCcAdminBusyTimer_Object = MibTableColumn
llcCcAdminBusyTimer = _LlcCcAdminBusyTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 3, 1, 1, 11),
    _LlcCcAdminBusyTimer_Type()
)
llcCcAdminBusyTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    llcCcAdminBusyTimer.setStatus("current")


class _LlcCcAdminInactTimer_Type(TimeTicks):
    """Custom type llcCcAdminInactTimer based on TimeTicks"""
    defaultValue = 0


_LlcCcAdminInactTimer_Object = MibTableColumn
llcCcAdminInactTimer = _LlcCcAdminInactTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 3, 1, 1, 12),
    _LlcCcAdminInactTimer_Type()
)
llcCcAdminInactTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    llcCcAdminInactTimer.setStatus("current")


class _LlcCcAdminDelayAckCount_Type(Integer32):
    """Custom type llcCcAdminDelayAckCount based on Integer32"""
    defaultValue = 0


_LlcCcAdminDelayAckCount_Object = MibTableColumn
llcCcAdminDelayAckCount = _LlcCcAdminDelayAckCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 3, 1, 1, 13),
    _LlcCcAdminDelayAckCount_Type()
)
llcCcAdminDelayAckCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    llcCcAdminDelayAckCount.setStatus("current")


class _LlcCcAdminDelayAckTimer_Type(TimeTicks):
    """Custom type llcCcAdminDelayAckTimer based on TimeTicks"""
    defaultValue = 0


_LlcCcAdminDelayAckTimer_Object = MibTableColumn
llcCcAdminDelayAckTimer = _LlcCcAdminDelayAckTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 3, 1, 1, 14),
    _LlcCcAdminDelayAckTimer_Type()
)
llcCcAdminDelayAckTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    llcCcAdminDelayAckTimer.setStatus("current")
_LlcCcAdminNw_Type = Integer32
_LlcCcAdminNw_Object = MibTableColumn
llcCcAdminNw = _LlcCcAdminNw_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 3, 1, 1, 15),
    _LlcCcAdminNw_Type()
)
llcCcAdminNw.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    llcCcAdminNw.setStatus("current")
_LlcCcAdminRowStatus_Type = RowStatus
_LlcCcAdminRowStatus_Object = MibTableColumn
llcCcAdminRowStatus = _LlcCcAdminRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 3, 1, 1, 16),
    _LlcCcAdminRowStatus_Type()
)
llcCcAdminRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    llcCcAdminRowStatus.setStatus("current")
_LlcCcOperTable_Object = MibTable
llcCcOperTable = _LlcCcOperTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 3, 2)
)
if mibBuilder.loadTexts:
    llcCcOperTable.setStatus("current")
_LlcCcOperEntry_Object = MibTableRow
llcCcOperEntry = _LlcCcOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 3, 2, 1)
)
llcCcOperEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-SNA-LLC-MIB", "llcPortVirtualIndex"),
    (0, "CISCO-SNA-LLC-MIB", "llcSapNumber"),
    (0, "CISCO-SNA-LLC-MIB", "llcCcRMac"),
    (0, "CISCO-SNA-LLC-MIB", "llcCcRSap"),
)
if mibBuilder.loadTexts:
    llcCcOperEntry.setStatus("current")


class _LlcCcOperState_Type(Integer32):
    """Custom type llcCcOperState based on Integer32"""
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
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("aDM", 1),
          ("await", 6),
          ("awaitBusy", 7),
          ("awaitReject", 8),
          ("busy", 4),
          ("conn", 12),
          ("dConn", 9),
          ("error", 11),
          ("normal", 3),
          ("reject", 5),
          ("reset", 10),
          ("resetCheck", 13),
          ("resetWait", 14),
          ("setup", 2))
    )


_LlcCcOperState_Type.__name__ = "Integer32"
_LlcCcOperState_Object = MibTableColumn
llcCcOperState = _LlcCcOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 3, 2, 1, 1),
    _LlcCcOperState_Type()
)
llcCcOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcOperState.setStatus("current")
_LlcCcOperMaxIPDUOctetsSend_Type = Integer32
_LlcCcOperMaxIPDUOctetsSend_Object = MibTableColumn
llcCcOperMaxIPDUOctetsSend = _LlcCcOperMaxIPDUOctetsSend_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 3, 2, 1, 2),
    _LlcCcOperMaxIPDUOctetsSend_Type()
)
llcCcOperMaxIPDUOctetsSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcOperMaxIPDUOctetsSend.setStatus("current")
_LlcCcOperMaxIPDUOctetsRcv_Type = Integer32
_LlcCcOperMaxIPDUOctetsRcv_Object = MibTableColumn
llcCcOperMaxIPDUOctetsRcv = _LlcCcOperMaxIPDUOctetsRcv_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 3, 2, 1, 3),
    _LlcCcOperMaxIPDUOctetsRcv_Type()
)
llcCcOperMaxIPDUOctetsRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcOperMaxIPDUOctetsRcv.setStatus("current")


class _LlcCcOperMaxUnackedIPDUsSend_Type(Integer32):
    """Custom type llcCcOperMaxUnackedIPDUsSend based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_LlcCcOperMaxUnackedIPDUsSend_Type.__name__ = "Integer32"
_LlcCcOperMaxUnackedIPDUsSend_Object = MibTableColumn
llcCcOperMaxUnackedIPDUsSend = _LlcCcOperMaxUnackedIPDUsSend_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 3, 2, 1, 4),
    _LlcCcOperMaxUnackedIPDUsSend_Type()
)
llcCcOperMaxUnackedIPDUsSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcOperMaxUnackedIPDUsSend.setStatus("current")


class _LlcCcOperMaxUnackedIPDUsRcv_Type(Integer32):
    """Custom type llcCcOperMaxUnackedIPDUsRcv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_LlcCcOperMaxUnackedIPDUsRcv_Type.__name__ = "Integer32"
_LlcCcOperMaxUnackedIPDUsRcv_Object = MibTableColumn
llcCcOperMaxUnackedIPDUsRcv = _LlcCcOperMaxUnackedIPDUsRcv_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 3, 2, 1, 5),
    _LlcCcOperMaxUnackedIPDUsRcv_Type()
)
llcCcOperMaxUnackedIPDUsRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcOperMaxUnackedIPDUsRcv.setStatus("current")
_LlcCcOperMaxRetransmits_Type = Integer32
_LlcCcOperMaxRetransmits_Object = MibTableColumn
llcCcOperMaxRetransmits = _LlcCcOperMaxRetransmits_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 3, 2, 1, 6),
    _LlcCcOperMaxRetransmits_Type()
)
llcCcOperMaxRetransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcOperMaxRetransmits.setStatus("current")
_LlcCcOperAckTimer_Type = TimeTicks
_LlcCcOperAckTimer_Object = MibTableColumn
llcCcOperAckTimer = _LlcCcOperAckTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 3, 2, 1, 7),
    _LlcCcOperAckTimer_Type()
)
llcCcOperAckTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcOperAckTimer.setStatus("current")
_LlcCcOperPbitTimer_Type = TimeTicks
_LlcCcOperPbitTimer_Object = MibTableColumn
llcCcOperPbitTimer = _LlcCcOperPbitTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 3, 2, 1, 8),
    _LlcCcOperPbitTimer_Type()
)
llcCcOperPbitTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcOperPbitTimer.setStatus("current")
_LlcCcOperRejTimer_Type = TimeTicks
_LlcCcOperRejTimer_Object = MibTableColumn
llcCcOperRejTimer = _LlcCcOperRejTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 3, 2, 1, 9),
    _LlcCcOperRejTimer_Type()
)
llcCcOperRejTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcOperRejTimer.setStatus("current")
_LlcCcOperBusyTimer_Type = TimeTicks
_LlcCcOperBusyTimer_Object = MibTableColumn
llcCcOperBusyTimer = _LlcCcOperBusyTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 3, 2, 1, 10),
    _LlcCcOperBusyTimer_Type()
)
llcCcOperBusyTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcOperBusyTimer.setStatus("current")
_LlcCcOperInactTimer_Type = TimeTicks
_LlcCcOperInactTimer_Object = MibTableColumn
llcCcOperInactTimer = _LlcCcOperInactTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 3, 2, 1, 11),
    _LlcCcOperInactTimer_Type()
)
llcCcOperInactTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcOperInactTimer.setStatus("current")
_LlcCcOperDelayAckCount_Type = Integer32
_LlcCcOperDelayAckCount_Object = MibTableColumn
llcCcOperDelayAckCount = _LlcCcOperDelayAckCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 3, 2, 1, 12),
    _LlcCcOperDelayAckCount_Type()
)
llcCcOperDelayAckCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcOperDelayAckCount.setStatus("current")
_LlcCcOperDelayAckTimer_Type = TimeTicks
_LlcCcOperDelayAckTimer_Object = MibTableColumn
llcCcOperDelayAckTimer = _LlcCcOperDelayAckTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 3, 2, 1, 13),
    _LlcCcOperDelayAckTimer_Type()
)
llcCcOperDelayAckTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcOperDelayAckTimer.setStatus("current")
_LlcCcOperNw_Type = Integer32
_LlcCcOperNw_Object = MibTableColumn
llcCcOperNw = _LlcCcOperNw_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 3, 2, 1, 14),
    _LlcCcOperNw_Type()
)
llcCcOperNw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcOperNw.setStatus("current")


class _LlcCcOperWw_Type(Integer32):
    """Custom type llcCcOperWw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_LlcCcOperWw_Type.__name__ = "Integer32"
_LlcCcOperWw_Object = MibTableColumn
llcCcOperWw = _LlcCcOperWw_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 3, 2, 1, 15),
    _LlcCcOperWw_Type()
)
llcCcOperWw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcOperWw.setStatus("current")
_LlcCcOperCreateTime_Type = TimeStamp
_LlcCcOperCreateTime_Object = MibTableColumn
llcCcOperCreateTime = _LlcCcOperCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 3, 2, 1, 16),
    _LlcCcOperCreateTime_Type()
)
llcCcOperCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcOperCreateTime.setStatus("current")
_LlcCcOperLastModifyTime_Type = TimeStamp
_LlcCcOperLastModifyTime_Object = MibTableColumn
llcCcOperLastModifyTime = _LlcCcOperLastModifyTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 3, 2, 1, 17),
    _LlcCcOperLastModifyTime_Type()
)
llcCcOperLastModifyTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcOperLastModifyTime.setStatus("current")
_LlcCcOperLastFailTime_Type = TimeStamp
_LlcCcOperLastFailTime_Object = MibTableColumn
llcCcOperLastFailTime = _LlcCcOperLastFailTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 3, 2, 1, 18),
    _LlcCcOperLastFailTime_Type()
)
llcCcOperLastFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcOperLastFailTime.setStatus("current")


class _LlcCcOperLastFailCause_Type(Integer32):
    """Custom type llcCcOperLastFailCause based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("discReceived", 4),
          ("discSent", 5),
          ("forcedShutdown", 7),
          ("retriesExpired", 6),
          ("rxFRMR", 2),
          ("txFRMR", 3),
          ("undefined", 1))
    )


_LlcCcOperLastFailCause_Type.__name__ = "Integer32"
_LlcCcOperLastFailCause_Object = MibTableColumn
llcCcOperLastFailCause = _LlcCcOperLastFailCause_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 3, 2, 1, 19),
    _LlcCcOperLastFailCause_Type()
)
llcCcOperLastFailCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcOperLastFailCause.setStatus("current")


class _LlcCcOperLastFailFRMRInfo_Type(OctetString):
    """Custom type llcCcOperLastFailFRMRInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_LlcCcOperLastFailFRMRInfo_Type.__name__ = "OctetString"
_LlcCcOperLastFailFRMRInfo_Object = MibTableColumn
llcCcOperLastFailFRMRInfo = _LlcCcOperLastFailFRMRInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 3, 2, 1, 20),
    _LlcCcOperLastFailFRMRInfo_Type()
)
llcCcOperLastFailFRMRInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcOperLastFailFRMRInfo.setStatus("current")


class _LlcCcOperLastWwCause_Type(Integer32):
    """Custom type llcCcOperLastWwCause based on Integer32"""
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
        *(("lostData", 2),
          ("macLayerCongestion", 3),
          ("neverInvoked", 1),
          ("other", 4))
    )


_LlcCcOperLastWwCause_Type.__name__ = "Integer32"
_LlcCcOperLastWwCause_Object = MibTableColumn
llcCcOperLastWwCause = _LlcCcOperLastWwCause_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 3, 2, 1, 21),
    _LlcCcOperLastWwCause_Type()
)
llcCcOperLastWwCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcOperLastWwCause.setStatus("current")
_LlcCcStatsTable_Object = MibTable
llcCcStatsTable = _LlcCcStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 3, 3)
)
if mibBuilder.loadTexts:
    llcCcStatsTable.setStatus("current")
_LlcCcStatsEntry_Object = MibTableRow
llcCcStatsEntry = _LlcCcStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 3, 3, 1)
)
llcCcStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-SNA-LLC-MIB", "llcPortVirtualIndex"),
    (0, "CISCO-SNA-LLC-MIB", "llcSapNumber"),
    (0, "CISCO-SNA-LLC-MIB", "llcCcRMac"),
    (0, "CISCO-SNA-LLC-MIB", "llcCcRSap"),
)
if mibBuilder.loadTexts:
    llcCcStatsEntry.setStatus("current")
_LlcCcStatsLocalBusies_Type = Counter32
_LlcCcStatsLocalBusies_Object = MibTableColumn
llcCcStatsLocalBusies = _LlcCcStatsLocalBusies_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 3, 3, 1, 1),
    _LlcCcStatsLocalBusies_Type()
)
llcCcStatsLocalBusies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcStatsLocalBusies.setStatus("current")
_LlcCcStatsRemoteBusies_Type = Counter32
_LlcCcStatsRemoteBusies_Object = MibTableColumn
llcCcStatsRemoteBusies = _LlcCcStatsRemoteBusies_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 3, 3, 1, 2),
    _LlcCcStatsRemoteBusies_Type()
)
llcCcStatsRemoteBusies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcStatsRemoteBusies.setStatus("current")
_LlcCcStatsIFramesIn_Type = Counter32
_LlcCcStatsIFramesIn_Object = MibTableColumn
llcCcStatsIFramesIn = _LlcCcStatsIFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 3, 3, 1, 3),
    _LlcCcStatsIFramesIn_Type()
)
llcCcStatsIFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcStatsIFramesIn.setStatus("current")
_LlcCcStatsIFramesOut_Type = Counter32
_LlcCcStatsIFramesOut_Object = MibTableColumn
llcCcStatsIFramesOut = _LlcCcStatsIFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 3, 3, 1, 4),
    _LlcCcStatsIFramesOut_Type()
)
llcCcStatsIFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcStatsIFramesOut.setStatus("current")
_LlcCcStatsIOctetsIn_Type = Counter32
_LlcCcStatsIOctetsIn_Object = MibTableColumn
llcCcStatsIOctetsIn = _LlcCcStatsIOctetsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 3, 3, 1, 5),
    _LlcCcStatsIOctetsIn_Type()
)
llcCcStatsIOctetsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcStatsIOctetsIn.setStatus("current")
_LlcCcStatsIOctetsOut_Type = Counter32
_LlcCcStatsIOctetsOut_Object = MibTableColumn
llcCcStatsIOctetsOut = _LlcCcStatsIOctetsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 3, 3, 1, 6),
    _LlcCcStatsIOctetsOut_Type()
)
llcCcStatsIOctetsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcStatsIOctetsOut.setStatus("current")
_LlcCcStatsSFramesIn_Type = Counter32
_LlcCcStatsSFramesIn_Object = MibTableColumn
llcCcStatsSFramesIn = _LlcCcStatsSFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 3, 3, 1, 7),
    _LlcCcStatsSFramesIn_Type()
)
llcCcStatsSFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcStatsSFramesIn.setStatus("current")
_LlcCcStatsSFramesOut_Type = Counter32
_LlcCcStatsSFramesOut_Object = MibTableColumn
llcCcStatsSFramesOut = _LlcCcStatsSFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 3, 3, 1, 8),
    _LlcCcStatsSFramesOut_Type()
)
llcCcStatsSFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcStatsSFramesOut.setStatus("current")
_LlcCcStatsRetransmitsOut_Type = Counter32
_LlcCcStatsRetransmitsOut_Object = MibTableColumn
llcCcStatsRetransmitsOut = _LlcCcStatsRetransmitsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 3, 3, 1, 9),
    _LlcCcStatsRetransmitsOut_Type()
)
llcCcStatsRetransmitsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcStatsRetransmitsOut.setStatus("current")
_LlcCcStatsREJsIn_Type = Counter32
_LlcCcStatsREJsIn_Object = MibTableColumn
llcCcStatsREJsIn = _LlcCcStatsREJsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 3, 3, 1, 10),
    _LlcCcStatsREJsIn_Type()
)
llcCcStatsREJsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcStatsREJsIn.setStatus("current")
_LlcCcStatsREJsOut_Type = Counter32
_LlcCcStatsREJsOut_Object = MibTableColumn
llcCcStatsREJsOut = _LlcCcStatsREJsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 3, 3, 1, 11),
    _LlcCcStatsREJsOut_Type()
)
llcCcStatsREJsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcStatsREJsOut.setStatus("current")
_LlcCcStatsWwCount_Type = Counter32
_LlcCcStatsWwCount_Object = MibTableColumn
llcCcStatsWwCount = _LlcCcStatsWwCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 1, 3, 3, 1, 12),
    _LlcCcStatsWwCount_Type()
)
llcCcStatsWwCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcStatsWwCount.setStatus("current")
_SnaLlcMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
snaLlcMIBNotificationPrefix = _SnaLlcMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 2)
)
_SnaLlcMIBNotifications_ObjectIdentity = ObjectIdentity
snaLlcMIBNotifications = _SnaLlcMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 2, 0)
)
_SnaLlcMIBConformance_ObjectIdentity = ObjectIdentity
snaLlcMIBConformance = _SnaLlcMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 3)
)
_SnaLlcMIBCompliances_ObjectIdentity = ObjectIdentity
snaLlcMIBCompliances = _SnaLlcMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 3, 1)
)
_SnaLlcMIBGroups_ObjectIdentity = ObjectIdentity
snaLlcMIBGroups = _SnaLlcMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 3, 2)
)

# Managed Objects groups

llcCorePortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 3, 2, 1)
)
llcCorePortGroup.setObjects(
      *(("CISCO-SNA-LLC-MIB", "llcPortAdminName"),
        ("CISCO-SNA-LLC-MIB", "llcPortAdminMaxSaps"),
        ("CISCO-SNA-LLC-MIB", "llcPortAdminMaxCcs"),
        ("CISCO-SNA-LLC-MIB", "llcPortAdminMaxPDUOctets"),
        ("CISCO-SNA-LLC-MIB", "llcPortAdminMaxUnackedIPDUsSend"),
        ("CISCO-SNA-LLC-MIB", "llcPortAdminMaxUnackedIPDUsRcv"),
        ("CISCO-SNA-LLC-MIB", "llcPortAdminMaxRetransmits"),
        ("CISCO-SNA-LLC-MIB", "llcPortAdminAckTimer"),
        ("CISCO-SNA-LLC-MIB", "llcPortAdminPbitTimer"),
        ("CISCO-SNA-LLC-MIB", "llcPortAdminRejTimer"),
        ("CISCO-SNA-LLC-MIB", "llcPortAdminBusyTimer"),
        ("CISCO-SNA-LLC-MIB", "llcPortAdminInactTimer"),
        ("CISCO-SNA-LLC-MIB", "llcPortAdminDelayAckCount"),
        ("CISCO-SNA-LLC-MIB", "llcPortAdminDelayAckTimer"),
        ("CISCO-SNA-LLC-MIB", "llcPortAdminNw"),
        ("CISCO-SNA-LLC-MIB", "llcPortOperMacAddress"),
        ("CISCO-SNA-LLC-MIB", "llcPortOperNumSaps"),
        ("CISCO-SNA-LLC-MIB", "llcPortOperHiWaterNumSaps"),
        ("CISCO-SNA-LLC-MIB", "llcPortOperSimRim"),
        ("CISCO-SNA-LLC-MIB", "llcPortOperLastModifyTime"),
        ("CISCO-SNA-LLC-MIB", "llcPortStatsPDUsIn"),
        ("CISCO-SNA-LLC-MIB", "llcPortStatsPDUsOut"),
        ("CISCO-SNA-LLC-MIB", "llcPortStatsOctetsIn"),
        ("CISCO-SNA-LLC-MIB", "llcPortStatsOctetsOut"),
        ("CISCO-SNA-LLC-MIB", "llcPortStatsTESTCommandsIn"),
        ("CISCO-SNA-LLC-MIB", "llcPortStatsTESTResponsesOut"),
        ("CISCO-SNA-LLC-MIB", "llcPortStatsLocalBusies"),
        ("CISCO-SNA-LLC-MIB", "llcPortStatsUnknownSaps"))
)
if mibBuilder.loadTexts:
    llcCorePortGroup.setStatus("current")

llcCoreSapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 3, 2, 2)
)
llcCoreSapGroup.setObjects(
      *(("CISCO-SNA-LLC-MIB", "llcSapAdminMaxPDUOctets"),
        ("CISCO-SNA-LLC-MIB", "llcSapAdminMaxUnackedIPDUsSend"),
        ("CISCO-SNA-LLC-MIB", "llcSapAdminMaxUnackedIPDUsRcv"),
        ("CISCO-SNA-LLC-MIB", "llcSapAdminMaxRetransmits"),
        ("CISCO-SNA-LLC-MIB", "llcSapAdminAckTimer"),
        ("CISCO-SNA-LLC-MIB", "llcSapAdminPbitTimer"),
        ("CISCO-SNA-LLC-MIB", "llcSapAdminRejTimer"),
        ("CISCO-SNA-LLC-MIB", "llcSapAdminBusyTimer"),
        ("CISCO-SNA-LLC-MIB", "llcSapAdminInactTimer"),
        ("CISCO-SNA-LLC-MIB", "llcSapAdminDelayAckCount"),
        ("CISCO-SNA-LLC-MIB", "llcSapAdminDelayAckTimer"),
        ("CISCO-SNA-LLC-MIB", "llcSapAdminNw"),
        ("CISCO-SNA-LLC-MIB", "llcSapOperStatus"),
        ("CISCO-SNA-LLC-MIB", "llcSapOperNumCcs"),
        ("CISCO-SNA-LLC-MIB", "llcSapOperHiWaterNumCcs"),
        ("CISCO-SNA-LLC-MIB", "llcSapOperLlc2Support"),
        ("CISCO-SNA-LLC-MIB", "llcSapStatsLocalBusies"),
        ("CISCO-SNA-LLC-MIB", "llcSapStatsRemoteBusies"),
        ("CISCO-SNA-LLC-MIB", "llcSapStatsIFramesIn"),
        ("CISCO-SNA-LLC-MIB", "llcSapStatsIFramesOut"),
        ("CISCO-SNA-LLC-MIB", "llcSapStatsIOctetsIn"),
        ("CISCO-SNA-LLC-MIB", "llcSapStatsIOctetsOut"),
        ("CISCO-SNA-LLC-MIB", "llcSapStatsSFramesIn"),
        ("CISCO-SNA-LLC-MIB", "llcSapStatsSFramesOut"),
        ("CISCO-SNA-LLC-MIB", "llcSapStatsRetransmitsOut"),
        ("CISCO-SNA-LLC-MIB", "llcSapStatsREJsIn"),
        ("CISCO-SNA-LLC-MIB", "llcSapStatsREJsOut"),
        ("CISCO-SNA-LLC-MIB", "llcSapStatsWwCount"),
        ("CISCO-SNA-LLC-MIB", "llcSapStatsTESTCommandsIn"),
        ("CISCO-SNA-LLC-MIB", "llcSapStatsTESTCommandsOut"),
        ("CISCO-SNA-LLC-MIB", "llcSapStatsTESTResponsesIn"),
        ("CISCO-SNA-LLC-MIB", "llcSapStatsTESTResponsesOut"),
        ("CISCO-SNA-LLC-MIB", "llcSapStatsXIDCommandsIn"),
        ("CISCO-SNA-LLC-MIB", "llcSapStatsXIDCommandsOut"),
        ("CISCO-SNA-LLC-MIB", "llcSapStatsXIDResponsesIn"),
        ("CISCO-SNA-LLC-MIB", "llcSapStatsXIDResponsesOut"),
        ("CISCO-SNA-LLC-MIB", "llcSapStatsUIFramesIn"),
        ("CISCO-SNA-LLC-MIB", "llcSapStatsUIFramesOut"),
        ("CISCO-SNA-LLC-MIB", "llcSapStatsUIOctetsIn"),
        ("CISCO-SNA-LLC-MIB", "llcSapStatsUIOctetsOut"),
        ("CISCO-SNA-LLC-MIB", "llcSapStatsConnectOk"),
        ("CISCO-SNA-LLC-MIB", "llcSapStatsConnectFail"),
        ("CISCO-SNA-LLC-MIB", "llcSapStatsDisconnect"),
        ("CISCO-SNA-LLC-MIB", "llcSapStatsDisconnectFRMRSend"),
        ("CISCO-SNA-LLC-MIB", "llcSapStatsDisconnectFRMRRcv"),
        ("CISCO-SNA-LLC-MIB", "llcSapStatsDisconnectTimer"),
        ("CISCO-SNA-LLC-MIB", "llcSapStatsDMsInABM"),
        ("CISCO-SNA-LLC-MIB", "llcSapStatsSABMEsInABM"))
)
if mibBuilder.loadTexts:
    llcCoreSapGroup.setStatus("current")

llcCoreCcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 3, 2, 3)
)
llcCoreCcGroup.setObjects(
      *(("CISCO-SNA-LLC-MIB", "llcCcAdminBounce"),
        ("CISCO-SNA-LLC-MIB", "llcCcAdminMaxPDUOctets"),
        ("CISCO-SNA-LLC-MIB", "llcCcAdminMaxUnackedIPDUsSend"),
        ("CISCO-SNA-LLC-MIB", "llcCcAdminMaxUnackedIPDUsRcv"),
        ("CISCO-SNA-LLC-MIB", "llcCcAdminMaxRetransmits"),
        ("CISCO-SNA-LLC-MIB", "llcCcAdminAckTimer"),
        ("CISCO-SNA-LLC-MIB", "llcCcAdminPbitTimer"),
        ("CISCO-SNA-LLC-MIB", "llcCcAdminRejTimer"),
        ("CISCO-SNA-LLC-MIB", "llcCcAdminBusyTimer"),
        ("CISCO-SNA-LLC-MIB", "llcCcAdminInactTimer"),
        ("CISCO-SNA-LLC-MIB", "llcCcAdminDelayAckCount"),
        ("CISCO-SNA-LLC-MIB", "llcCcAdminDelayAckTimer"),
        ("CISCO-SNA-LLC-MIB", "llcCcAdminNw"),
        ("CISCO-SNA-LLC-MIB", "llcCcAdminRowStatus"),
        ("CISCO-SNA-LLC-MIB", "llcCcOperState"),
        ("CISCO-SNA-LLC-MIB", "llcCcOperMaxIPDUOctetsSend"),
        ("CISCO-SNA-LLC-MIB", "llcCcOperMaxIPDUOctetsRcv"),
        ("CISCO-SNA-LLC-MIB", "llcCcOperMaxUnackedIPDUsSend"),
        ("CISCO-SNA-LLC-MIB", "llcCcOperMaxUnackedIPDUsRcv"),
        ("CISCO-SNA-LLC-MIB", "llcCcOperMaxRetransmits"),
        ("CISCO-SNA-LLC-MIB", "llcCcOperAckTimer"),
        ("CISCO-SNA-LLC-MIB", "llcCcOperPbitTimer"),
        ("CISCO-SNA-LLC-MIB", "llcCcOperRejTimer"),
        ("CISCO-SNA-LLC-MIB", "llcCcOperBusyTimer"),
        ("CISCO-SNA-LLC-MIB", "llcCcOperInactTimer"),
        ("CISCO-SNA-LLC-MIB", "llcCcOperDelayAckCount"),
        ("CISCO-SNA-LLC-MIB", "llcCcOperDelayAckTimer"),
        ("CISCO-SNA-LLC-MIB", "llcCcOperNw"),
        ("CISCO-SNA-LLC-MIB", "llcCcOperWw"),
        ("CISCO-SNA-LLC-MIB", "llcCcOperCreateTime"),
        ("CISCO-SNA-LLC-MIB", "llcCcOperLastModifyTime"),
        ("CISCO-SNA-LLC-MIB", "llcCcOperLastFailTime"),
        ("CISCO-SNA-LLC-MIB", "llcCcOperLastFailCause"),
        ("CISCO-SNA-LLC-MIB", "llcCcOperLastFailFRMRInfo"),
        ("CISCO-SNA-LLC-MIB", "llcCcOperLastWwCause"),
        ("CISCO-SNA-LLC-MIB", "llcCcStatsLocalBusies"),
        ("CISCO-SNA-LLC-MIB", "llcCcStatsRemoteBusies"),
        ("CISCO-SNA-LLC-MIB", "llcCcStatsIFramesIn"),
        ("CISCO-SNA-LLC-MIB", "llcCcStatsIFramesOut"),
        ("CISCO-SNA-LLC-MIB", "llcCcStatsIOctetsIn"),
        ("CISCO-SNA-LLC-MIB", "llcCcStatsIOctetsOut"),
        ("CISCO-SNA-LLC-MIB", "llcCcStatsSFramesIn"),
        ("CISCO-SNA-LLC-MIB", "llcCcStatsSFramesOut"),
        ("CISCO-SNA-LLC-MIB", "llcCcStatsRetransmitsOut"),
        ("CISCO-SNA-LLC-MIB", "llcCcStatsREJsIn"),
        ("CISCO-SNA-LLC-MIB", "llcCcStatsREJsOut"),
        ("CISCO-SNA-LLC-MIB", "llcCcStatsWwCount"))
)
if mibBuilder.loadTexts:
    llcCoreCcGroup.setStatus("current")


# Notification objects

llcCcStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 2, 0, 1)
)
llcCcStatusChange.setObjects(
      *(("CISCO-SNA-LLC-MIB", "llcCcOperState"),
        ("CISCO-SNA-LLC-MIB", "llcCcOperLastFailTime"),
        ("CISCO-SNA-LLC-MIB", "llcCcOperLastFailCause"),
        ("CISCO-SNA-LLC-MIB", "llcCcOperLastFailFRMRInfo"))
)
if mibBuilder.loadTexts:
    llcCcStatusChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

llcCoreCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 8, 3, 1, 1)
)
if mibBuilder.loadTexts:
    llcCoreCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SNA-LLC-MIB",
    **{"ciscoSnaLlcMIB": ciscoSnaLlcMIB,
       "ciscoSnaLlcMIBObjects": ciscoSnaLlcMIBObjects,
       "llcPortGroup": llcPortGroup,
       "llcPortAdminTable": llcPortAdminTable,
       "llcPortAdminEntry": llcPortAdminEntry,
       "llcPortVirtualIndex": llcPortVirtualIndex,
       "llcPortAdminName": llcPortAdminName,
       "llcPortAdminMaxSaps": llcPortAdminMaxSaps,
       "llcPortAdminMaxCcs": llcPortAdminMaxCcs,
       "llcPortAdminMaxPDUOctets": llcPortAdminMaxPDUOctets,
       "llcPortAdminMaxUnackedIPDUsSend": llcPortAdminMaxUnackedIPDUsSend,
       "llcPortAdminMaxUnackedIPDUsRcv": llcPortAdminMaxUnackedIPDUsRcv,
       "llcPortAdminMaxRetransmits": llcPortAdminMaxRetransmits,
       "llcPortAdminAckTimer": llcPortAdminAckTimer,
       "llcPortAdminPbitTimer": llcPortAdminPbitTimer,
       "llcPortAdminRejTimer": llcPortAdminRejTimer,
       "llcPortAdminBusyTimer": llcPortAdminBusyTimer,
       "llcPortAdminInactTimer": llcPortAdminInactTimer,
       "llcPortAdminDelayAckCount": llcPortAdminDelayAckCount,
       "llcPortAdminDelayAckTimer": llcPortAdminDelayAckTimer,
       "llcPortAdminNw": llcPortAdminNw,
       "llcPortOperTable": llcPortOperTable,
       "llcPortOperEntry": llcPortOperEntry,
       "llcPortOperMacAddress": llcPortOperMacAddress,
       "llcPortOperNumSaps": llcPortOperNumSaps,
       "llcPortOperHiWaterNumSaps": llcPortOperHiWaterNumSaps,
       "llcPortOperSimRim": llcPortOperSimRim,
       "llcPortOperLastModifyTime": llcPortOperLastModifyTime,
       "llcPortStatsTable": llcPortStatsTable,
       "llcPortStatsEntry": llcPortStatsEntry,
       "llcPortStatsPDUsIn": llcPortStatsPDUsIn,
       "llcPortStatsPDUsOut": llcPortStatsPDUsOut,
       "llcPortStatsOctetsIn": llcPortStatsOctetsIn,
       "llcPortStatsOctetsOut": llcPortStatsOctetsOut,
       "llcPortStatsTESTCommandsIn": llcPortStatsTESTCommandsIn,
       "llcPortStatsTESTResponsesOut": llcPortStatsTESTResponsesOut,
       "llcPortStatsLocalBusies": llcPortStatsLocalBusies,
       "llcPortStatsUnknownSaps": llcPortStatsUnknownSaps,
       "llcSapGroup": llcSapGroup,
       "llcSapAdminTable": llcSapAdminTable,
       "llcSapAdminEntry": llcSapAdminEntry,
       "llcSapNumber": llcSapNumber,
       "llcSapAdminMaxPDUOctets": llcSapAdminMaxPDUOctets,
       "llcSapAdminMaxUnackedIPDUsSend": llcSapAdminMaxUnackedIPDUsSend,
       "llcSapAdminMaxUnackedIPDUsRcv": llcSapAdminMaxUnackedIPDUsRcv,
       "llcSapAdminMaxRetransmits": llcSapAdminMaxRetransmits,
       "llcSapAdminAckTimer": llcSapAdminAckTimer,
       "llcSapAdminPbitTimer": llcSapAdminPbitTimer,
       "llcSapAdminRejTimer": llcSapAdminRejTimer,
       "llcSapAdminBusyTimer": llcSapAdminBusyTimer,
       "llcSapAdminInactTimer": llcSapAdminInactTimer,
       "llcSapAdminDelayAckCount": llcSapAdminDelayAckCount,
       "llcSapAdminDelayAckTimer": llcSapAdminDelayAckTimer,
       "llcSapAdminNw": llcSapAdminNw,
       "llcSapOperTable": llcSapOperTable,
       "llcSapOperEntry": llcSapOperEntry,
       "llcSapOperStatus": llcSapOperStatus,
       "llcSapOperNumCcs": llcSapOperNumCcs,
       "llcSapOperHiWaterNumCcs": llcSapOperHiWaterNumCcs,
       "llcSapOperLlc2Support": llcSapOperLlc2Support,
       "llcSapStatsTable": llcSapStatsTable,
       "llcSapStatsEntry": llcSapStatsEntry,
       "llcSapStatsLocalBusies": llcSapStatsLocalBusies,
       "llcSapStatsRemoteBusies": llcSapStatsRemoteBusies,
       "llcSapStatsIFramesIn": llcSapStatsIFramesIn,
       "llcSapStatsIFramesOut": llcSapStatsIFramesOut,
       "llcSapStatsIOctetsIn": llcSapStatsIOctetsIn,
       "llcSapStatsIOctetsOut": llcSapStatsIOctetsOut,
       "llcSapStatsSFramesIn": llcSapStatsSFramesIn,
       "llcSapStatsSFramesOut": llcSapStatsSFramesOut,
       "llcSapStatsRetransmitsOut": llcSapStatsRetransmitsOut,
       "llcSapStatsREJsIn": llcSapStatsREJsIn,
       "llcSapStatsREJsOut": llcSapStatsREJsOut,
       "llcSapStatsWwCount": llcSapStatsWwCount,
       "llcSapStatsTESTCommandsIn": llcSapStatsTESTCommandsIn,
       "llcSapStatsTESTCommandsOut": llcSapStatsTESTCommandsOut,
       "llcSapStatsTESTResponsesIn": llcSapStatsTESTResponsesIn,
       "llcSapStatsTESTResponsesOut": llcSapStatsTESTResponsesOut,
       "llcSapStatsXIDCommandsIn": llcSapStatsXIDCommandsIn,
       "llcSapStatsXIDCommandsOut": llcSapStatsXIDCommandsOut,
       "llcSapStatsXIDResponsesIn": llcSapStatsXIDResponsesIn,
       "llcSapStatsXIDResponsesOut": llcSapStatsXIDResponsesOut,
       "llcSapStatsUIFramesIn": llcSapStatsUIFramesIn,
       "llcSapStatsUIFramesOut": llcSapStatsUIFramesOut,
       "llcSapStatsUIOctetsIn": llcSapStatsUIOctetsIn,
       "llcSapStatsUIOctetsOut": llcSapStatsUIOctetsOut,
       "llcSapStatsConnectOk": llcSapStatsConnectOk,
       "llcSapStatsConnectFail": llcSapStatsConnectFail,
       "llcSapStatsDisconnect": llcSapStatsDisconnect,
       "llcSapStatsDisconnectFRMRSend": llcSapStatsDisconnectFRMRSend,
       "llcSapStatsDisconnectFRMRRcv": llcSapStatsDisconnectFRMRRcv,
       "llcSapStatsDisconnectTimer": llcSapStatsDisconnectTimer,
       "llcSapStatsDMsInABM": llcSapStatsDMsInABM,
       "llcSapStatsSABMEsInABM": llcSapStatsSABMEsInABM,
       "llcCcGroup": llcCcGroup,
       "llcCcAdminTable": llcCcAdminTable,
       "llcCcAdminEntry": llcCcAdminEntry,
       "llcCcRMac": llcCcRMac,
       "llcCcRSap": llcCcRSap,
       "llcCcAdminBounce": llcCcAdminBounce,
       "llcCcAdminMaxPDUOctets": llcCcAdminMaxPDUOctets,
       "llcCcAdminMaxUnackedIPDUsSend": llcCcAdminMaxUnackedIPDUsSend,
       "llcCcAdminMaxUnackedIPDUsRcv": llcCcAdminMaxUnackedIPDUsRcv,
       "llcCcAdminMaxRetransmits": llcCcAdminMaxRetransmits,
       "llcCcAdminAckTimer": llcCcAdminAckTimer,
       "llcCcAdminPbitTimer": llcCcAdminPbitTimer,
       "llcCcAdminRejTimer": llcCcAdminRejTimer,
       "llcCcAdminBusyTimer": llcCcAdminBusyTimer,
       "llcCcAdminInactTimer": llcCcAdminInactTimer,
       "llcCcAdminDelayAckCount": llcCcAdminDelayAckCount,
       "llcCcAdminDelayAckTimer": llcCcAdminDelayAckTimer,
       "llcCcAdminNw": llcCcAdminNw,
       "llcCcAdminRowStatus": llcCcAdminRowStatus,
       "llcCcOperTable": llcCcOperTable,
       "llcCcOperEntry": llcCcOperEntry,
       "llcCcOperState": llcCcOperState,
       "llcCcOperMaxIPDUOctetsSend": llcCcOperMaxIPDUOctetsSend,
       "llcCcOperMaxIPDUOctetsRcv": llcCcOperMaxIPDUOctetsRcv,
       "llcCcOperMaxUnackedIPDUsSend": llcCcOperMaxUnackedIPDUsSend,
       "llcCcOperMaxUnackedIPDUsRcv": llcCcOperMaxUnackedIPDUsRcv,
       "llcCcOperMaxRetransmits": llcCcOperMaxRetransmits,
       "llcCcOperAckTimer": llcCcOperAckTimer,
       "llcCcOperPbitTimer": llcCcOperPbitTimer,
       "llcCcOperRejTimer": llcCcOperRejTimer,
       "llcCcOperBusyTimer": llcCcOperBusyTimer,
       "llcCcOperInactTimer": llcCcOperInactTimer,
       "llcCcOperDelayAckCount": llcCcOperDelayAckCount,
       "llcCcOperDelayAckTimer": llcCcOperDelayAckTimer,
       "llcCcOperNw": llcCcOperNw,
       "llcCcOperWw": llcCcOperWw,
       "llcCcOperCreateTime": llcCcOperCreateTime,
       "llcCcOperLastModifyTime": llcCcOperLastModifyTime,
       "llcCcOperLastFailTime": llcCcOperLastFailTime,
       "llcCcOperLastFailCause": llcCcOperLastFailCause,
       "llcCcOperLastFailFRMRInfo": llcCcOperLastFailFRMRInfo,
       "llcCcOperLastWwCause": llcCcOperLastWwCause,
       "llcCcStatsTable": llcCcStatsTable,
       "llcCcStatsEntry": llcCcStatsEntry,
       "llcCcStatsLocalBusies": llcCcStatsLocalBusies,
       "llcCcStatsRemoteBusies": llcCcStatsRemoteBusies,
       "llcCcStatsIFramesIn": llcCcStatsIFramesIn,
       "llcCcStatsIFramesOut": llcCcStatsIFramesOut,
       "llcCcStatsIOctetsIn": llcCcStatsIOctetsIn,
       "llcCcStatsIOctetsOut": llcCcStatsIOctetsOut,
       "llcCcStatsSFramesIn": llcCcStatsSFramesIn,
       "llcCcStatsSFramesOut": llcCcStatsSFramesOut,
       "llcCcStatsRetransmitsOut": llcCcStatsRetransmitsOut,
       "llcCcStatsREJsIn": llcCcStatsREJsIn,
       "llcCcStatsREJsOut": llcCcStatsREJsOut,
       "llcCcStatsWwCount": llcCcStatsWwCount,
       "snaLlcMIBNotificationPrefix": snaLlcMIBNotificationPrefix,
       "snaLlcMIBNotifications": snaLlcMIBNotifications,
       "llcCcStatusChange": llcCcStatusChange,
       "snaLlcMIBConformance": snaLlcMIBConformance,
       "snaLlcMIBCompliances": snaLlcMIBCompliances,
       "llcCoreCompliance": llcCoreCompliance,
       "snaLlcMIBGroups": snaLlcMIBGroups,
       "llcCorePortGroup": llcCorePortGroup,
       "llcCoreSapGroup": llcCoreSapGroup,
       "llcCoreCcGroup": llcCoreCcGroup}
)
