# SNMP MIB module (A3COM-LIC-R1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-LIC-R1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:29:37 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_A3com_ObjectIdentity = ObjectIdentity
a3com = _A3com_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43)
)
_BrouterMIB_ObjectIdentity = ObjectIdentity
brouterMIB = _BrouterMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2)
)
_Llc_ObjectIdentity = ObjectIdentity
llc = _Llc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 26)
)
_LlcPortGroup_ObjectIdentity = ObjectIdentity
llcPortGroup = _LlcPortGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 1)
)
_LlcPortAdminTable_Object = MibTable
llcPortAdminTable = _LlcPortAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 1, 1)
)
if mibBuilder.loadTexts:
    llcPortAdminTable.setStatus("mandatory")
_LlcPortAdminEntry_Object = MibTableRow
llcPortAdminEntry = _LlcPortAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 1, 1, 1)
)
llcPortAdminEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    llcPortAdminEntry.setStatus("mandatory")


class _LlcPortAdminName_Type(DisplayString):
    """Custom type llcPortAdminName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_LlcPortAdminName_Type.__name__ = "DisplayString"
_LlcPortAdminName_Object = MibTableColumn
llcPortAdminName = _LlcPortAdminName_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 1, 1, 1, 1),
    _LlcPortAdminName_Type()
)
llcPortAdminName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcPortAdminName.setStatus("mandatory")
_LlcPortAdminMaxSaps_Type = Gauge32
_LlcPortAdminMaxSaps_Object = MibTableColumn
llcPortAdminMaxSaps = _LlcPortAdminMaxSaps_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 1, 1, 1, 2),
    _LlcPortAdminMaxSaps_Type()
)
llcPortAdminMaxSaps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcPortAdminMaxSaps.setStatus("mandatory")
_LlcPortAdminMaxCcs_Type = Gauge32
_LlcPortAdminMaxCcs_Object = MibTableColumn
llcPortAdminMaxCcs = _LlcPortAdminMaxCcs_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 1, 1, 1, 3),
    _LlcPortAdminMaxCcs_Type()
)
llcPortAdminMaxCcs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcPortAdminMaxCcs.setStatus("mandatory")
_LlcPortAdminMaxPDUOctets_Type = Integer32
_LlcPortAdminMaxPDUOctets_Object = MibTableColumn
llcPortAdminMaxPDUOctets = _LlcPortAdminMaxPDUOctets_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 1, 1, 1, 4),
    _LlcPortAdminMaxPDUOctets_Type()
)
llcPortAdminMaxPDUOctets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcPortAdminMaxPDUOctets.setStatus("mandatory")


class _LlcPortAdminMaxUnackedIPDUsSend_Type(Integer32):
    """Custom type llcPortAdminMaxUnackedIPDUsSend based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_LlcPortAdminMaxUnackedIPDUsSend_Type.__name__ = "Integer32"
_LlcPortAdminMaxUnackedIPDUsSend_Object = MibTableColumn
llcPortAdminMaxUnackedIPDUsSend = _LlcPortAdminMaxUnackedIPDUsSend_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 1, 1, 1, 5),
    _LlcPortAdminMaxUnackedIPDUsSend_Type()
)
llcPortAdminMaxUnackedIPDUsSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcPortAdminMaxUnackedIPDUsSend.setStatus("mandatory")


class _LlcPortAdminMaxUnackedIPDUsRcv_Type(Integer32):
    """Custom type llcPortAdminMaxUnackedIPDUsRcv based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_LlcPortAdminMaxUnackedIPDUsRcv_Type.__name__ = "Integer32"
_LlcPortAdminMaxUnackedIPDUsRcv_Object = MibTableColumn
llcPortAdminMaxUnackedIPDUsRcv = _LlcPortAdminMaxUnackedIPDUsRcv_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 1, 1, 1, 6),
    _LlcPortAdminMaxUnackedIPDUsRcv_Type()
)
llcPortAdminMaxUnackedIPDUsRcv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcPortAdminMaxUnackedIPDUsRcv.setStatus("mandatory")


class _LlcPortAdminMaxRetransmits_Type(Integer32):
    """Custom type llcPortAdminMaxRetransmits based on Integer32"""
    defaultValue = 7


_LlcPortAdminMaxRetransmits_Object = MibTableColumn
llcPortAdminMaxRetransmits = _LlcPortAdminMaxRetransmits_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 1, 1, 1, 7),
    _LlcPortAdminMaxRetransmits_Type()
)
llcPortAdminMaxRetransmits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcPortAdminMaxRetransmits.setStatus("mandatory")


class _LlcPortAdminAckTimer_Type(TimeTicks):
    """Custom type llcPortAdminAckTimer based on TimeTicks"""
    defaultValue = 300


_LlcPortAdminAckTimer_Object = MibTableColumn
llcPortAdminAckTimer = _LlcPortAdminAckTimer_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 1, 1, 1, 8),
    _LlcPortAdminAckTimer_Type()
)
llcPortAdminAckTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcPortAdminAckTimer.setStatus("mandatory")


class _LlcPortAdminPbitTimer_Type(TimeTicks):
    """Custom type llcPortAdminPbitTimer based on TimeTicks"""
    defaultValue = 300


_LlcPortAdminPbitTimer_Object = MibTableColumn
llcPortAdminPbitTimer = _LlcPortAdminPbitTimer_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 1, 1, 1, 9),
    _LlcPortAdminPbitTimer_Type()
)
llcPortAdminPbitTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcPortAdminPbitTimer.setStatus("mandatory")


class _LlcPortAdminRejTimer_Type(TimeTicks):
    """Custom type llcPortAdminRejTimer based on TimeTicks"""
    defaultValue = 300


_LlcPortAdminRejTimer_Object = MibTableColumn
llcPortAdminRejTimer = _LlcPortAdminRejTimer_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 1, 1, 1, 10),
    _LlcPortAdminRejTimer_Type()
)
llcPortAdminRejTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcPortAdminRejTimer.setStatus("mandatory")


class _LlcPortAdminBusyTimer_Type(TimeTicks):
    """Custom type llcPortAdminBusyTimer based on TimeTicks"""
    defaultValue = 30000


_LlcPortAdminBusyTimer_Object = MibTableColumn
llcPortAdminBusyTimer = _LlcPortAdminBusyTimer_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 1, 1, 1, 11),
    _LlcPortAdminBusyTimer_Type()
)
llcPortAdminBusyTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcPortAdminBusyTimer.setStatus("mandatory")


class _LlcPortAdminInactTimer_Type(TimeTicks):
    """Custom type llcPortAdminInactTimer based on TimeTicks"""
    defaultValue = 1500


_LlcPortAdminInactTimer_Object = MibTableColumn
llcPortAdminInactTimer = _LlcPortAdminInactTimer_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 1, 1, 1, 12),
    _LlcPortAdminInactTimer_Type()
)
llcPortAdminInactTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcPortAdminInactTimer.setStatus("mandatory")


class _LlcPortAdminDelayAckCount_Type(Integer32):
    """Custom type llcPortAdminDelayAckCount based on Integer32"""
    defaultValue = 1


_LlcPortAdminDelayAckCount_Object = MibTableColumn
llcPortAdminDelayAckCount = _LlcPortAdminDelayAckCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 1, 1, 1, 13),
    _LlcPortAdminDelayAckCount_Type()
)
llcPortAdminDelayAckCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcPortAdminDelayAckCount.setStatus("mandatory")


class _LlcPortAdminDelayAckTimer_Type(TimeTicks):
    """Custom type llcPortAdminDelayAckTimer based on TimeTicks"""
    defaultValue = 0


_LlcPortAdminDelayAckTimer_Object = MibTableColumn
llcPortAdminDelayAckTimer = _LlcPortAdminDelayAckTimer_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 1, 1, 1, 14),
    _LlcPortAdminDelayAckTimer_Type()
)
llcPortAdminDelayAckTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcPortAdminDelayAckTimer.setStatus("mandatory")


class _LlcPortAdminNw_Type(Integer32):
    """Custom type llcPortAdminNw based on Integer32"""
    defaultValue = 4


_LlcPortAdminNw_Object = MibTableColumn
llcPortAdminNw = _LlcPortAdminNw_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 1, 1, 1, 15),
    _LlcPortAdminNw_Type()
)
llcPortAdminNw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcPortAdminNw.setStatus("mandatory")
_LlcPortOperTable_Object = MibTable
llcPortOperTable = _LlcPortOperTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 1, 2)
)
if mibBuilder.loadTexts:
    llcPortOperTable.setStatus("mandatory")
_LlcPortOperEntry_Object = MibTableRow
llcPortOperEntry = _LlcPortOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 1, 2, 1)
)
llcPortOperEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    llcPortOperEntry.setStatus("mandatory")
_LlcPortOperNumSaps_Type = Gauge32
_LlcPortOperNumSaps_Object = MibTableColumn
llcPortOperNumSaps = _LlcPortOperNumSaps_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 1, 2, 1, 1),
    _LlcPortOperNumSaps_Type()
)
llcPortOperNumSaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcPortOperNumSaps.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 1, 2, 1, 2),
    _LlcPortOperSimRim_Type()
)
llcPortOperSimRim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcPortOperSimRim.setStatus("mandatory")
_LlcPortOperLastModifyTime_Type = TimeTicks
_LlcPortOperLastModifyTime_Object = MibTableColumn
llcPortOperLastModifyTime = _LlcPortOperLastModifyTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 1, 2, 1, 3),
    _LlcPortOperLastModifyTime_Type()
)
llcPortOperLastModifyTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcPortOperLastModifyTime.setStatus("mandatory")
_LlcSapGroup_ObjectIdentity = ObjectIdentity
llcSapGroup = _LlcSapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 2)
)
_LlcSapAdminTable_Object = MibTable
llcSapAdminTable = _LlcSapAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 2, 1)
)
if mibBuilder.loadTexts:
    llcSapAdminTable.setStatus("mandatory")
_LlcSapAdminEntry_Object = MibTableRow
llcSapAdminEntry = _LlcSapAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 2, 1, 1)
)
llcSapAdminEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "A3COM-LIC-R1-MIB", "llcSapNumber"),
)
if mibBuilder.loadTexts:
    llcSapAdminEntry.setStatus("mandatory")


class _LlcSapNumber_Type(Integer32):
    """Custom type llcSapNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_LlcSapNumber_Type.__name__ = "Integer32"
_LlcSapNumber_Object = MibTableColumn
llcSapNumber = _LlcSapNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 2, 1, 1, 1),
    _LlcSapNumber_Type()
)
llcSapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapNumber.setStatus("mandatory")
_LlcSapOperTable_Object = MibTable
llcSapOperTable = _LlcSapOperTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 2, 2)
)
if mibBuilder.loadTexts:
    llcSapOperTable.setStatus("mandatory")
_LlcSapOperEntry_Object = MibTableRow
llcSapOperEntry = _LlcSapOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 2, 2, 1)
)
llcSapOperEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "A3COM-LIC-R1-MIB", "llcSapNumber"),
)
if mibBuilder.loadTexts:
    llcSapOperEntry.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 2, 2, 1, 1),
    _LlcSapOperStatus_Type()
)
llcSapOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapOperStatus.setStatus("mandatory")
_LlcSapOperNumCcs_Type = Integer32
_LlcSapOperNumCcs_Object = MibTableColumn
llcSapOperNumCcs = _LlcSapOperNumCcs_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 2, 2, 1, 2),
    _LlcSapOperNumCcs_Type()
)
llcSapOperNumCcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapOperNumCcs.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 2, 2, 1, 3),
    _LlcSapOperLlc2Support_Type()
)
llcSapOperLlc2Support.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapOperLlc2Support.setStatus("mandatory")
_LlcSapStatsTable_Object = MibTable
llcSapStatsTable = _LlcSapStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 2, 3)
)
if mibBuilder.loadTexts:
    llcSapStatsTable.setStatus("mandatory")
_LlcSapStatsEntry_Object = MibTableRow
llcSapStatsEntry = _LlcSapStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 2, 3, 1)
)
llcSapStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "A3COM-LIC-R1-MIB", "llcSapNumber"),
)
if mibBuilder.loadTexts:
    llcSapStatsEntry.setStatus("mandatory")
_LlcSapStatsLocalBusies_Type = Counter32
_LlcSapStatsLocalBusies_Object = MibTableColumn
llcSapStatsLocalBusies = _LlcSapStatsLocalBusies_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 2, 3, 1, 1),
    _LlcSapStatsLocalBusies_Type()
)
llcSapStatsLocalBusies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapStatsLocalBusies.setStatus("mandatory")
_LlcSapStatsRemoteBusies_Type = Counter32
_LlcSapStatsRemoteBusies_Object = MibTableColumn
llcSapStatsRemoteBusies = _LlcSapStatsRemoteBusies_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 2, 3, 1, 2),
    _LlcSapStatsRemoteBusies_Type()
)
llcSapStatsRemoteBusies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapStatsRemoteBusies.setStatus("mandatory")
_LlcSapStatsIFramesIn_Type = Counter32
_LlcSapStatsIFramesIn_Object = MibTableColumn
llcSapStatsIFramesIn = _LlcSapStatsIFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 2, 3, 1, 3),
    _LlcSapStatsIFramesIn_Type()
)
llcSapStatsIFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapStatsIFramesIn.setStatus("mandatory")
_LlcSapStatsIFramesOut_Type = Counter32
_LlcSapStatsIFramesOut_Object = MibTableColumn
llcSapStatsIFramesOut = _LlcSapStatsIFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 2, 3, 1, 4),
    _LlcSapStatsIFramesOut_Type()
)
llcSapStatsIFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapStatsIFramesOut.setStatus("mandatory")
_LlcSapStatsIOctetsIn_Type = Counter32
_LlcSapStatsIOctetsIn_Object = MibTableColumn
llcSapStatsIOctetsIn = _LlcSapStatsIOctetsIn_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 2, 3, 1, 5),
    _LlcSapStatsIOctetsIn_Type()
)
llcSapStatsIOctetsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapStatsIOctetsIn.setStatus("mandatory")
_LlcSapStatsIOctetsOut_Type = Counter32
_LlcSapStatsIOctetsOut_Object = MibTableColumn
llcSapStatsIOctetsOut = _LlcSapStatsIOctetsOut_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 2, 3, 1, 6),
    _LlcSapStatsIOctetsOut_Type()
)
llcSapStatsIOctetsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapStatsIOctetsOut.setStatus("mandatory")
_LlcSapStatsSFramesIn_Type = Counter32
_LlcSapStatsSFramesIn_Object = MibTableColumn
llcSapStatsSFramesIn = _LlcSapStatsSFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 2, 3, 1, 7),
    _LlcSapStatsSFramesIn_Type()
)
llcSapStatsSFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapStatsSFramesIn.setStatus("mandatory")
_LlcSapStatsSFramesOut_Type = Counter32
_LlcSapStatsSFramesOut_Object = MibTableColumn
llcSapStatsSFramesOut = _LlcSapStatsSFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 2, 3, 1, 8),
    _LlcSapStatsSFramesOut_Type()
)
llcSapStatsSFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapStatsSFramesOut.setStatus("mandatory")
_LlcSapStatsRetransmitsOut_Type = Counter32
_LlcSapStatsRetransmitsOut_Object = MibTableColumn
llcSapStatsRetransmitsOut = _LlcSapStatsRetransmitsOut_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 2, 3, 1, 9),
    _LlcSapStatsRetransmitsOut_Type()
)
llcSapStatsRetransmitsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapStatsRetransmitsOut.setStatus("mandatory")
_LlcSapStatsREJsIn_Type = Counter32
_LlcSapStatsREJsIn_Object = MibTableColumn
llcSapStatsREJsIn = _LlcSapStatsREJsIn_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 2, 3, 1, 10),
    _LlcSapStatsREJsIn_Type()
)
llcSapStatsREJsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapStatsREJsIn.setStatus("mandatory")
_LlcSapStatsREJsOut_Type = Counter32
_LlcSapStatsREJsOut_Object = MibTableColumn
llcSapStatsREJsOut = _LlcSapStatsREJsOut_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 2, 3, 1, 11),
    _LlcSapStatsREJsOut_Type()
)
llcSapStatsREJsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapStatsREJsOut.setStatus("mandatory")
_LlcSapStatsWwCount_Type = Counter32
_LlcSapStatsWwCount_Object = MibTableColumn
llcSapStatsWwCount = _LlcSapStatsWwCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 2, 3, 1, 12),
    _LlcSapStatsWwCount_Type()
)
llcSapStatsWwCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapStatsWwCount.setStatus("mandatory")
_LlcSapStatsTESTCommandsIn_Type = Counter32
_LlcSapStatsTESTCommandsIn_Object = MibTableColumn
llcSapStatsTESTCommandsIn = _LlcSapStatsTESTCommandsIn_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 2, 3, 1, 13),
    _LlcSapStatsTESTCommandsIn_Type()
)
llcSapStatsTESTCommandsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapStatsTESTCommandsIn.setStatus("mandatory")
_LlcSapStatsTESTCommandsOut_Type = Counter32
_LlcSapStatsTESTCommandsOut_Object = MibTableColumn
llcSapStatsTESTCommandsOut = _LlcSapStatsTESTCommandsOut_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 2, 3, 1, 14),
    _LlcSapStatsTESTCommandsOut_Type()
)
llcSapStatsTESTCommandsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapStatsTESTCommandsOut.setStatus("mandatory")
_LlcSapStatsTESTResponsesIn_Type = Counter32
_LlcSapStatsTESTResponsesIn_Object = MibTableColumn
llcSapStatsTESTResponsesIn = _LlcSapStatsTESTResponsesIn_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 2, 3, 1, 15),
    _LlcSapStatsTESTResponsesIn_Type()
)
llcSapStatsTESTResponsesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapStatsTESTResponsesIn.setStatus("mandatory")
_LlcSapStatsTESTResponsesOut_Type = Counter32
_LlcSapStatsTESTResponsesOut_Object = MibTableColumn
llcSapStatsTESTResponsesOut = _LlcSapStatsTESTResponsesOut_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 2, 3, 1, 16),
    _LlcSapStatsTESTResponsesOut_Type()
)
llcSapStatsTESTResponsesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapStatsTESTResponsesOut.setStatus("mandatory")
_LlcSapStatsXIDCommandsIn_Type = Counter32
_LlcSapStatsXIDCommandsIn_Object = MibTableColumn
llcSapStatsXIDCommandsIn = _LlcSapStatsXIDCommandsIn_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 2, 3, 1, 17),
    _LlcSapStatsXIDCommandsIn_Type()
)
llcSapStatsXIDCommandsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapStatsXIDCommandsIn.setStatus("mandatory")
_LlcSapStatsXIDCommandsOut_Type = Counter32
_LlcSapStatsXIDCommandsOut_Object = MibTableColumn
llcSapStatsXIDCommandsOut = _LlcSapStatsXIDCommandsOut_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 2, 3, 1, 18),
    _LlcSapStatsXIDCommandsOut_Type()
)
llcSapStatsXIDCommandsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapStatsXIDCommandsOut.setStatus("mandatory")
_LlcSapStatsXIDResponsesIn_Type = Counter32
_LlcSapStatsXIDResponsesIn_Object = MibTableColumn
llcSapStatsXIDResponsesIn = _LlcSapStatsXIDResponsesIn_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 2, 3, 1, 19),
    _LlcSapStatsXIDResponsesIn_Type()
)
llcSapStatsXIDResponsesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapStatsXIDResponsesIn.setStatus("mandatory")
_LlcSapStatsXIDResponsesOut_Type = Counter32
_LlcSapStatsXIDResponsesOut_Object = MibTableColumn
llcSapStatsXIDResponsesOut = _LlcSapStatsXIDResponsesOut_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 2, 3, 1, 20),
    _LlcSapStatsXIDResponsesOut_Type()
)
llcSapStatsXIDResponsesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapStatsXIDResponsesOut.setStatus("mandatory")
_LlcSapStatsUIFramesIn_Type = Counter32
_LlcSapStatsUIFramesIn_Object = MibTableColumn
llcSapStatsUIFramesIn = _LlcSapStatsUIFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 2, 3, 1, 21),
    _LlcSapStatsUIFramesIn_Type()
)
llcSapStatsUIFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapStatsUIFramesIn.setStatus("mandatory")
_LlcSapStatsUIFramesOut_Type = Counter32
_LlcSapStatsUIFramesOut_Object = MibTableColumn
llcSapStatsUIFramesOut = _LlcSapStatsUIFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 2, 3, 1, 22),
    _LlcSapStatsUIFramesOut_Type()
)
llcSapStatsUIFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapStatsUIFramesOut.setStatus("mandatory")
_LlcSapStatsUIOctetsIn_Type = Counter32
_LlcSapStatsUIOctetsIn_Object = MibTableColumn
llcSapStatsUIOctetsIn = _LlcSapStatsUIOctetsIn_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 2, 3, 1, 23),
    _LlcSapStatsUIOctetsIn_Type()
)
llcSapStatsUIOctetsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapStatsUIOctetsIn.setStatus("mandatory")
_LlcSapStatsUIOctetsOut_Type = Counter32
_LlcSapStatsUIOctetsOut_Object = MibTableColumn
llcSapStatsUIOctetsOut = _LlcSapStatsUIOctetsOut_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 2, 3, 1, 24),
    _LlcSapStatsUIOctetsOut_Type()
)
llcSapStatsUIOctetsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapStatsUIOctetsOut.setStatus("mandatory")
_LlcSapStatsConnectOk_Type = Counter32
_LlcSapStatsConnectOk_Object = MibTableColumn
llcSapStatsConnectOk = _LlcSapStatsConnectOk_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 2, 3, 1, 25),
    _LlcSapStatsConnectOk_Type()
)
llcSapStatsConnectOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapStatsConnectOk.setStatus("mandatory")
_LlcSapStatsConnectFail_Type = Counter32
_LlcSapStatsConnectFail_Object = MibTableColumn
llcSapStatsConnectFail = _LlcSapStatsConnectFail_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 2, 3, 1, 26),
    _LlcSapStatsConnectFail_Type()
)
llcSapStatsConnectFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapStatsConnectFail.setStatus("mandatory")
_LlcSapStatsDisconnect_Type = Counter32
_LlcSapStatsDisconnect_Object = MibTableColumn
llcSapStatsDisconnect = _LlcSapStatsDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 2, 3, 1, 27),
    _LlcSapStatsDisconnect_Type()
)
llcSapStatsDisconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapStatsDisconnect.setStatus("mandatory")
_LlcSapStatsDisconnectFRMRSend_Type = Counter32
_LlcSapStatsDisconnectFRMRSend_Object = MibTableColumn
llcSapStatsDisconnectFRMRSend = _LlcSapStatsDisconnectFRMRSend_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 2, 3, 1, 28),
    _LlcSapStatsDisconnectFRMRSend_Type()
)
llcSapStatsDisconnectFRMRSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapStatsDisconnectFRMRSend.setStatus("mandatory")
_LlcSapStatsDisconnectFRMRRcv_Type = Counter32
_LlcSapStatsDisconnectFRMRRcv_Object = MibTableColumn
llcSapStatsDisconnectFRMRRcv = _LlcSapStatsDisconnectFRMRRcv_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 2, 3, 1, 29),
    _LlcSapStatsDisconnectFRMRRcv_Type()
)
llcSapStatsDisconnectFRMRRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapStatsDisconnectFRMRRcv.setStatus("mandatory")
_LlcSapStatsDisconnectTimer_Type = Counter32
_LlcSapStatsDisconnectTimer_Object = MibTableColumn
llcSapStatsDisconnectTimer = _LlcSapStatsDisconnectTimer_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 2, 3, 1, 30),
    _LlcSapStatsDisconnectTimer_Type()
)
llcSapStatsDisconnectTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapStatsDisconnectTimer.setStatus("mandatory")
_LlcSapStatsReset_Type = Counter32
_LlcSapStatsReset_Object = MibTableColumn
llcSapStatsReset = _LlcSapStatsReset_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 2, 3, 1, 31),
    _LlcSapStatsReset_Type()
)
llcSapStatsReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapStatsReset.setStatus("mandatory")
_LlcCcGroup_ObjectIdentity = ObjectIdentity
llcCcGroup = _LlcCcGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 3)
)
_LlcCcAdminTable_Object = MibTable
llcCcAdminTable = _LlcCcAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 3, 1)
)
if mibBuilder.loadTexts:
    llcCcAdminTable.setStatus("mandatory")
_LlcCcAdminEntry_Object = MibTableRow
llcCcAdminEntry = _LlcCcAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 3, 1, 1)
)
llcCcAdminEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "A3COM-LIC-R1-MIB", "llcCcLSap"),
    (0, "A3COM-LIC-R1-MIB", "llcCcRSap"),
    (0, "A3COM-LIC-R1-MIB", "llcCcRMac"),
    (0, "A3COM-LIC-R1-MIB", "llcCcLMac"),
)
if mibBuilder.loadTexts:
    llcCcAdminEntry.setStatus("mandatory")


class _LlcCcLSap_Type(Integer32):
    """Custom type llcCcLSap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_LlcCcLSap_Type.__name__ = "Integer32"
_LlcCcLSap_Object = MibTableColumn
llcCcLSap = _LlcCcLSap_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 3, 1, 1, 1),
    _LlcCcLSap_Type()
)
llcCcLSap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcLSap.setStatus("mandatory")


class _LlcCcRSap_Type(Integer32):
    """Custom type llcCcRSap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_LlcCcRSap_Type.__name__ = "Integer32"
_LlcCcRSap_Object = MibTableColumn
llcCcRSap = _LlcCcRSap_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 3, 1, 1, 2),
    _LlcCcRSap_Type()
)
llcCcRSap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcRSap.setStatus("mandatory")


class _LlcCcLMac_Type(OctetString):
    """Custom type llcCcLMac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_LlcCcLMac_Type.__name__ = "OctetString"
_LlcCcLMac_Object = MibTableColumn
llcCcLMac = _LlcCcLMac_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 3, 1, 1, 3),
    _LlcCcLMac_Type()
)
llcCcLMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcLMac.setStatus("mandatory")


class _LlcCcRMac_Type(OctetString):
    """Custom type llcCcRMac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_LlcCcRMac_Type.__name__ = "OctetString"
_LlcCcRMac_Object = MibTableColumn
llcCcRMac = _LlcCcRMac_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 3, 1, 1, 4),
    _LlcCcRMac_Type()
)
llcCcRMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcRMac.setStatus("mandatory")
_LlcCcOperTable_Object = MibTable
llcCcOperTable = _LlcCcOperTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 3, 2)
)
if mibBuilder.loadTexts:
    llcCcOperTable.setStatus("mandatory")
_LlcCcOperEntry_Object = MibTableRow
llcCcOperEntry = _LlcCcOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 3, 2, 1)
)
llcCcOperEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "A3COM-LIC-R1-MIB", "llcCcLSap"),
    (0, "A3COM-LIC-R1-MIB", "llcCcRSap"),
    (0, "A3COM-LIC-R1-MIB", "llcCcRMac"),
    (0, "A3COM-LIC-R1-MIB", "llcCcLMac"),
)
if mibBuilder.loadTexts:
    llcCcOperEntry.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 3, 2, 1, 1),
    _LlcCcOperState_Type()
)
llcCcOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcOperState.setStatus("mandatory")
_LlcCcOperMaxIPDUOctetsSend_Type = Integer32
_LlcCcOperMaxIPDUOctetsSend_Object = MibTableColumn
llcCcOperMaxIPDUOctetsSend = _LlcCcOperMaxIPDUOctetsSend_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 3, 2, 1, 2),
    _LlcCcOperMaxIPDUOctetsSend_Type()
)
llcCcOperMaxIPDUOctetsSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcOperMaxIPDUOctetsSend.setStatus("mandatory")
_LlcCcOperMaxIPDUOctetsRcv_Type = Integer32
_LlcCcOperMaxIPDUOctetsRcv_Object = MibTableColumn
llcCcOperMaxIPDUOctetsRcv = _LlcCcOperMaxIPDUOctetsRcv_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 3, 2, 1, 3),
    _LlcCcOperMaxIPDUOctetsRcv_Type()
)
llcCcOperMaxIPDUOctetsRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcOperMaxIPDUOctetsRcv.setStatus("mandatory")


class _LlcCcOperMaxUnackedIPDUsSend_Type(Integer32):
    """Custom type llcCcOperMaxUnackedIPDUsSend based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_LlcCcOperMaxUnackedIPDUsSend_Type.__name__ = "Integer32"
_LlcCcOperMaxUnackedIPDUsSend_Object = MibTableColumn
llcCcOperMaxUnackedIPDUsSend = _LlcCcOperMaxUnackedIPDUsSend_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 3, 2, 1, 4),
    _LlcCcOperMaxUnackedIPDUsSend_Type()
)
llcCcOperMaxUnackedIPDUsSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcOperMaxUnackedIPDUsSend.setStatus("mandatory")


class _LlcCcOperMaxUnackedIPDUsRcv_Type(Integer32):
    """Custom type llcCcOperMaxUnackedIPDUsRcv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_LlcCcOperMaxUnackedIPDUsRcv_Type.__name__ = "Integer32"
_LlcCcOperMaxUnackedIPDUsRcv_Object = MibTableColumn
llcCcOperMaxUnackedIPDUsRcv = _LlcCcOperMaxUnackedIPDUsRcv_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 3, 2, 1, 5),
    _LlcCcOperMaxUnackedIPDUsRcv_Type()
)
llcCcOperMaxUnackedIPDUsRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcOperMaxUnackedIPDUsRcv.setStatus("mandatory")
_LlcCcOperMaxRetransmits_Type = Integer32
_LlcCcOperMaxRetransmits_Object = MibTableColumn
llcCcOperMaxRetransmits = _LlcCcOperMaxRetransmits_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 3, 2, 1, 6),
    _LlcCcOperMaxRetransmits_Type()
)
llcCcOperMaxRetransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcOperMaxRetransmits.setStatus("mandatory")
_LlcCcOperAckTimer_Type = TimeTicks
_LlcCcOperAckTimer_Object = MibTableColumn
llcCcOperAckTimer = _LlcCcOperAckTimer_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 3, 2, 1, 7),
    _LlcCcOperAckTimer_Type()
)
llcCcOperAckTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcOperAckTimer.setStatus("mandatory")
_LlcCcOperPbitTimer_Type = TimeTicks
_LlcCcOperPbitTimer_Object = MibTableColumn
llcCcOperPbitTimer = _LlcCcOperPbitTimer_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 3, 2, 1, 8),
    _LlcCcOperPbitTimer_Type()
)
llcCcOperPbitTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcOperPbitTimer.setStatus("mandatory")
_LlcCcOperRejTimer_Type = TimeTicks
_LlcCcOperRejTimer_Object = MibTableColumn
llcCcOperRejTimer = _LlcCcOperRejTimer_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 3, 2, 1, 9),
    _LlcCcOperRejTimer_Type()
)
llcCcOperRejTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcOperRejTimer.setStatus("mandatory")
_LlcCcOperBusyTimer_Type = TimeTicks
_LlcCcOperBusyTimer_Object = MibTableColumn
llcCcOperBusyTimer = _LlcCcOperBusyTimer_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 3, 2, 1, 10),
    _LlcCcOperBusyTimer_Type()
)
llcCcOperBusyTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcOperBusyTimer.setStatus("mandatory")
_LlcCcOperInactTimer_Type = TimeTicks
_LlcCcOperInactTimer_Object = MibTableColumn
llcCcOperInactTimer = _LlcCcOperInactTimer_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 3, 2, 1, 11),
    _LlcCcOperInactTimer_Type()
)
llcCcOperInactTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcOperInactTimer.setStatus("mandatory")
_LlcCcOperDelayAckCount_Type = Integer32
_LlcCcOperDelayAckCount_Object = MibTableColumn
llcCcOperDelayAckCount = _LlcCcOperDelayAckCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 3, 2, 1, 12),
    _LlcCcOperDelayAckCount_Type()
)
llcCcOperDelayAckCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcOperDelayAckCount.setStatus("mandatory")
_LlcCcOperDelayAckTimer_Type = TimeTicks
_LlcCcOperDelayAckTimer_Object = MibTableColumn
llcCcOperDelayAckTimer = _LlcCcOperDelayAckTimer_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 3, 2, 1, 13),
    _LlcCcOperDelayAckTimer_Type()
)
llcCcOperDelayAckTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcOperDelayAckTimer.setStatus("mandatory")
_LlcCcOperNw_Type = Integer32
_LlcCcOperNw_Object = MibTableColumn
llcCcOperNw = _LlcCcOperNw_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 3, 2, 1, 14),
    _LlcCcOperNw_Type()
)
llcCcOperNw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcOperNw.setStatus("mandatory")


class _LlcCcOperWw_Type(Integer32):
    """Custom type llcCcOperWw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_LlcCcOperWw_Type.__name__ = "Integer32"
_LlcCcOperWw_Object = MibTableColumn
llcCcOperWw = _LlcCcOperWw_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 3, 2, 1, 15),
    _LlcCcOperWw_Type()
)
llcCcOperWw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcOperWw.setStatus("mandatory")
_LlcCcOperCreateTime_Type = TimeTicks
_LlcCcOperCreateTime_Object = MibTableColumn
llcCcOperCreateTime = _LlcCcOperCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 3, 2, 1, 16),
    _LlcCcOperCreateTime_Type()
)
llcCcOperCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcOperCreateTime.setStatus("mandatory")
_LlcCcOperLastModifyTime_Type = TimeTicks
_LlcCcOperLastModifyTime_Object = MibTableColumn
llcCcOperLastModifyTime = _LlcCcOperLastModifyTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 3, 2, 1, 17),
    _LlcCcOperLastModifyTime_Type()
)
llcCcOperLastModifyTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcOperLastModifyTime.setStatus("mandatory")
_LlcCcOperLastFailTime_Type = TimeTicks
_LlcCcOperLastFailTime_Object = MibTableColumn
llcCcOperLastFailTime = _LlcCcOperLastFailTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 3, 2, 1, 18),
    _LlcCcOperLastFailTime_Type()
)
llcCcOperLastFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcOperLastFailTime.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 3, 2, 1, 19),
    _LlcCcOperLastFailCause_Type()
)
llcCcOperLastFailCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcOperLastFailCause.setStatus("mandatory")


class _LlcCcOperLastFailFRMRInfo_Type(OctetString):
    """Custom type llcCcOperLastFailFRMRInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_LlcCcOperLastFailFRMRInfo_Type.__name__ = "OctetString"
_LlcCcOperLastFailFRMRInfo_Object = MibTableColumn
llcCcOperLastFailFRMRInfo = _LlcCcOperLastFailFRMRInfo_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 3, 2, 1, 20),
    _LlcCcOperLastFailFRMRInfo_Type()
)
llcCcOperLastFailFRMRInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcOperLastFailFRMRInfo.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 3, 2, 1, 21),
    _LlcCcOperLastWwCause_Type()
)
llcCcOperLastWwCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcOperLastWwCause.setStatus("mandatory")
_LlcCcStatsTable_Object = MibTable
llcCcStatsTable = _LlcCcStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 3, 3)
)
if mibBuilder.loadTexts:
    llcCcStatsTable.setStatus("mandatory")
_LlcCcStatsEntry_Object = MibTableRow
llcCcStatsEntry = _LlcCcStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 3, 3, 1)
)
llcCcStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "A3COM-LIC-R1-MIB", "llcCcLSap"),
    (0, "A3COM-LIC-R1-MIB", "llcCcRSap"),
    (0, "A3COM-LIC-R1-MIB", "llcCcRMac"),
    (0, "A3COM-LIC-R1-MIB", "llcCcLMac"),
)
if mibBuilder.loadTexts:
    llcCcStatsEntry.setStatus("mandatory")
_LlcCcStatsLocalBusies_Type = Counter32
_LlcCcStatsLocalBusies_Object = MibTableColumn
llcCcStatsLocalBusies = _LlcCcStatsLocalBusies_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 3, 3, 1, 1),
    _LlcCcStatsLocalBusies_Type()
)
llcCcStatsLocalBusies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcStatsLocalBusies.setStatus("mandatory")
_LlcCcStatsRemoteBusies_Type = Counter32
_LlcCcStatsRemoteBusies_Object = MibTableColumn
llcCcStatsRemoteBusies = _LlcCcStatsRemoteBusies_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 3, 3, 1, 2),
    _LlcCcStatsRemoteBusies_Type()
)
llcCcStatsRemoteBusies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcStatsRemoteBusies.setStatus("mandatory")
_LlcCcStatsIFramesIn_Type = Counter32
_LlcCcStatsIFramesIn_Object = MibTableColumn
llcCcStatsIFramesIn = _LlcCcStatsIFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 3, 3, 1, 3),
    _LlcCcStatsIFramesIn_Type()
)
llcCcStatsIFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcStatsIFramesIn.setStatus("mandatory")
_LlcCcStatsIFramesOut_Type = Counter32
_LlcCcStatsIFramesOut_Object = MibTableColumn
llcCcStatsIFramesOut = _LlcCcStatsIFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 3, 3, 1, 4),
    _LlcCcStatsIFramesOut_Type()
)
llcCcStatsIFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcStatsIFramesOut.setStatus("mandatory")
_LlcCcStatsIOctetsIn_Type = Counter32
_LlcCcStatsIOctetsIn_Object = MibTableColumn
llcCcStatsIOctetsIn = _LlcCcStatsIOctetsIn_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 3, 3, 1, 5),
    _LlcCcStatsIOctetsIn_Type()
)
llcCcStatsIOctetsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcStatsIOctetsIn.setStatus("mandatory")
_LlcCcStatsIOctetsOut_Type = Counter32
_LlcCcStatsIOctetsOut_Object = MibTableColumn
llcCcStatsIOctetsOut = _LlcCcStatsIOctetsOut_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 3, 3, 1, 6),
    _LlcCcStatsIOctetsOut_Type()
)
llcCcStatsIOctetsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcStatsIOctetsOut.setStatus("mandatory")
_LlcCcStatsSFramesIn_Type = Counter32
_LlcCcStatsSFramesIn_Object = MibTableColumn
llcCcStatsSFramesIn = _LlcCcStatsSFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 3, 3, 1, 7),
    _LlcCcStatsSFramesIn_Type()
)
llcCcStatsSFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcStatsSFramesIn.setStatus("mandatory")
_LlcCcStatsSFramesOut_Type = Counter32
_LlcCcStatsSFramesOut_Object = MibTableColumn
llcCcStatsSFramesOut = _LlcCcStatsSFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 3, 3, 1, 8),
    _LlcCcStatsSFramesOut_Type()
)
llcCcStatsSFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcStatsSFramesOut.setStatus("mandatory")
_LlcCcStatsRetransmitsOut_Type = Counter32
_LlcCcStatsRetransmitsOut_Object = MibTableColumn
llcCcStatsRetransmitsOut = _LlcCcStatsRetransmitsOut_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 3, 3, 1, 9),
    _LlcCcStatsRetransmitsOut_Type()
)
llcCcStatsRetransmitsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcStatsRetransmitsOut.setStatus("mandatory")
_LlcCcStatsREJsIn_Type = Counter32
_LlcCcStatsREJsIn_Object = MibTableColumn
llcCcStatsREJsIn = _LlcCcStatsREJsIn_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 3, 3, 1, 10),
    _LlcCcStatsREJsIn_Type()
)
llcCcStatsREJsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcStatsREJsIn.setStatus("mandatory")
_LlcCcStatsREJsOut_Type = Counter32
_LlcCcStatsREJsOut_Object = MibTableColumn
llcCcStatsREJsOut = _LlcCcStatsREJsOut_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 3, 3, 1, 11),
    _LlcCcStatsREJsOut_Type()
)
llcCcStatsREJsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcStatsREJsOut.setStatus("mandatory")
_LlcCcStatsWwCount_Type = Counter32
_LlcCcStatsWwCount_Object = MibTableColumn
llcCcStatsWwCount = _LlcCcStatsWwCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 3, 3, 1, 12),
    _LlcCcStatsWwCount_Type()
)
llcCcStatsWwCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcStatsWwCount.setStatus("mandatory")
_LlcTunnelGroup_ObjectIdentity = ObjectIdentity
llcTunnelGroup = _LlcTunnelGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 4)
)
_CcsLlcTunnelInfo_ObjectIdentity = ObjectIdentity
ccsLlcTunnelInfo = _CcsLlcTunnelInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 4, 1)
)


class _CcsLlcTunnelVirtualRing_Type(Integer32):
    """Custom type ccsLlcTunnelVirtualRing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_CcsLlcTunnelVirtualRing_Type.__name__ = "Integer32"
_CcsLlcTunnelVirtualRing_Object = MibScalar
ccsLlcTunnelVirtualRing = _CcsLlcTunnelVirtualRing_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 4, 1, 1),
    _CcsLlcTunnelVirtualRing_Type()
)
ccsLlcTunnelVirtualRing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccsLlcTunnelVirtualRing.setStatus("mandatory")


class _CcsLlcTunnelMode_Type(Integer32):
    """Custom type ccsLlcTunnelMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              8,
              16,
              20,
              24,
              32,
              36,
              40)
        )
    )
    namedValues = NamedValues(
        *(("qTunnelDisable", 8),
          ("qTunnelDisableNonSecure", 40),
          ("qTunnelDisableSecure", 24),
          ("qTunnelEnable", 4),
          ("qTunnelEnableNonSecure", 36),
          ("qTunnelEnableSecure", 20),
          ("qTunnelNonSecure", 32),
          ("qTunnelSecure", 16))
    )


_CcsLlcTunnelMode_Type.__name__ = "Integer32"
_CcsLlcTunnelMode_Object = MibScalar
ccsLlcTunnelMode = _CcsLlcTunnelMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 4, 1, 2),
    _CcsLlcTunnelMode_Type()
)
ccsLlcTunnelMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccsLlcTunnelMode.setStatus("mandatory")


class _CcsLlcTunnelSNAPriority_Type(Integer32):
    """Custom type ccsLlcTunnelSNAPriority based on Integer32"""
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
        *(("qPrioDefault", 1),
          ("qPrioHigh", 2),
          ("qPrioLow", 4),
          ("qPrioMedium", 3))
    )


_CcsLlcTunnelSNAPriority_Type.__name__ = "Integer32"
_CcsLlcTunnelSNAPriority_Object = MibScalar
ccsLlcTunnelSNAPriority = _CcsLlcTunnelSNAPriority_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 4, 1, 3),
    _CcsLlcTunnelSNAPriority_Type()
)
ccsLlcTunnelSNAPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccsLlcTunnelSNAPriority.setStatus("mandatory")
_CcsLlcTunnelRouterTable_Object = MibTable
ccsLlcTunnelRouterTable = _CcsLlcTunnelRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 4, 2)
)
if mibBuilder.loadTexts:
    ccsLlcTunnelRouterTable.setStatus("mandatory")
_CcsLlcTunnelRouterEntry_Object = MibTableRow
ccsLlcTunnelRouterEntry = _CcsLlcTunnelRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 4, 2, 1)
)
ccsLlcTunnelRouterEntry.setIndexNames(
    (0, "A3COM-LIC-R1-MIB", "ccsLlcTunnelId"),
)
if mibBuilder.loadTexts:
    ccsLlcTunnelRouterEntry.setStatus("mandatory")
_CcsLlcPeerAddress_Type = IpAddress
_CcsLlcPeerAddress_Object = MibTableColumn
ccsLlcPeerAddress = _CcsLlcPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 4, 2, 1, 1),
    _CcsLlcPeerAddress_Type()
)
ccsLlcPeerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccsLlcPeerAddress.setStatus("mandatory")
_CcsLlcLocalAddress_Type = IpAddress
_CcsLlcLocalAddress_Object = MibTableColumn
ccsLlcLocalAddress = _CcsLlcLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 4, 2, 1, 2),
    _CcsLlcLocalAddress_Type()
)
ccsLlcLocalAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccsLlcLocalAddress.setStatus("mandatory")


class _CcsLlcTunnelId_Type(Integer32):
    """Custom type ccsLlcTunnelId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_CcsLlcTunnelId_Type.__name__ = "Integer32"
_CcsLlcTunnelId_Object = MibTableColumn
ccsLlcTunnelId = _CcsLlcTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 4, 2, 1, 3),
    _CcsLlcTunnelId_Type()
)
ccsLlcTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLlcTunnelId.setStatus("mandatory")


class _CcsLlcRouterEnable_Type(Integer32):
    """Custom type ccsLlcRouterEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("qTunEnable", 1),
          ("qtunDisable", 2))
    )


_CcsLlcRouterEnable_Type.__name__ = "Integer32"
_CcsLlcRouterEnable_Object = MibTableColumn
ccsLlcRouterEnable = _CcsLlcRouterEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 4, 2, 1, 4),
    _CcsLlcRouterEnable_Type()
)
ccsLlcRouterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccsLlcRouterEnable.setStatus("mandatory")


class _CcsLlcRouterMode_Type(Integer32):
    """Custom type ccsLlcRouterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("qLocalTerm", 3),
          ("qSpecificTerm", 2),
          ("qTransparent", 1))
    )


_CcsLlcRouterMode_Type.__name__ = "Integer32"
_CcsLlcRouterMode_Object = MibTableColumn
ccsLlcRouterMode = _CcsLlcRouterMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 4, 2, 1, 5),
    _CcsLlcRouterMode_Type()
)
ccsLlcRouterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccsLlcRouterMode.setStatus("mandatory")


class _CcsLlcRouterTunnelTransport_Type(Integer32):
    """Custom type ccsLlcRouterTunnelTransport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("qTcp", 2)
    )


_CcsLlcRouterTunnelTransport_Type.__name__ = "Integer32"
_CcsLlcRouterTunnelTransport_Object = MibTableColumn
ccsLlcRouterTunnelTransport = _CcsLlcRouterTunnelTransport_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 4, 2, 1, 6),
    _CcsLlcRouterTunnelTransport_Type()
)
ccsLlcRouterTunnelTransport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccsLlcRouterTunnelTransport.setStatus("mandatory")


class _CcsLlcRouterTunnelPort_Type(Integer32):
    """Custom type ccsLlcRouterTunnelPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_CcsLlcRouterTunnelPort_Type.__name__ = "Integer32"
_CcsLlcRouterTunnelPort_Object = MibTableColumn
ccsLlcRouterTunnelPort = _CcsLlcRouterTunnelPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 4, 2, 1, 7),
    _CcsLlcRouterTunnelPort_Type()
)
ccsLlcRouterTunnelPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccsLlcRouterTunnelPort.setStatus("mandatory")


class _CcsLlcRouterPeerString_Type(DisplayString):
    """Custom type ccsLlcRouterPeerString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CcsLlcRouterPeerString_Type.__name__ = "DisplayString"
_CcsLlcRouterPeerString_Object = MibTableColumn
ccsLlcRouterPeerString = _CcsLlcRouterPeerString_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 4, 2, 1, 8),
    _CcsLlcRouterPeerString_Type()
)
ccsLlcRouterPeerString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccsLlcRouterPeerString.setStatus("mandatory")
_CcsLlcTunnelDefaultDestTable_Object = MibTable
ccsLlcTunnelDefaultDestTable = _CcsLlcTunnelDefaultDestTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 4, 3)
)
if mibBuilder.loadTexts:
    ccsLlcTunnelDefaultDestTable.setStatus("mandatory")
_CcsLlcTunnelDefaultDestEntry_Object = MibTableRow
ccsLlcTunnelDefaultDestEntry = _CcsLlcTunnelDefaultDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 4, 3, 1)
)
ccsLlcTunnelDefaultDestEntry.setIndexNames(
    (0, "A3COM-LIC-R1-MIB", "pysmiFakeCol1"),
)
if mibBuilder.loadTexts:
    ccsLlcTunnelDefaultDestEntry.setStatus("mandatory")


class _CcsLlcDestTunnelId_Type(Integer32):
    """Custom type ccsLlcDestTunnelId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_CcsLlcDestTunnelId_Type.__name__ = "Integer32"
_CcsLlcDestTunnelId_Object = MibTableColumn
ccsLlcDestTunnelId = _CcsLlcDestTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 4, 3, 1, 1),
    _CcsLlcDestTunnelId_Type()
)
ccsLlcDestTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsLlcDestTunnelId.setStatus("mandatory")
_CcsLlcRemoteMacAddress_Type = MacAddress
_CcsLlcRemoteMacAddress_Object = MibTableColumn
ccsLlcRemoteMacAddress = _CcsLlcRemoteMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 4, 3, 1, 2),
    _CcsLlcRemoteMacAddress_Type()
)
ccsLlcRemoteMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccsLlcRemoteMacAddress.setStatus("mandatory")


class _CcsLlcRemoteSap_Type(Integer32):
    """Custom type ccsLlcRemoteSap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CcsLlcRemoteSap_Type.__name__ = "Integer32"
_CcsLlcRemoteSap_Object = MibTableColumn
ccsLlcRemoteSap = _CcsLlcRemoteSap_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 4, 3, 1, 3),
    _CcsLlcRemoteSap_Type()
)
ccsLlcRemoteSap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccsLlcRemoteSap.setStatus("mandatory")


class _CcsLlcRemoteSapLowRange_Type(Integer32):
    """Custom type ccsLlcRemoteSapLowRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CcsLlcRemoteSapLowRange_Type.__name__ = "Integer32"
_CcsLlcRemoteSapLowRange_Object = MibTableColumn
ccsLlcRemoteSapLowRange = _CcsLlcRemoteSapLowRange_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 4, 3, 1, 4),
    _CcsLlcRemoteSapLowRange_Type()
)
ccsLlcRemoteSapLowRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccsLlcRemoteSapLowRange.setStatus("mandatory")


class _CcsLlcRemoteSapHighRange_Type(Integer32):
    """Custom type ccsLlcRemoteSapHighRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CcsLlcRemoteSapHighRange_Type.__name__ = "Integer32"
_CcsLlcRemoteSapHighRange_Object = MibTableColumn
ccsLlcRemoteSapHighRange = _CcsLlcRemoteSapHighRange_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 4, 3, 1, 5),
    _CcsLlcRemoteSapHighRange_Type()
)
ccsLlcRemoteSapHighRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccsLlcRemoteSapHighRange.setStatus("mandatory")
_PysmiFakeCol1_Type = Integer32
_PysmiFakeCol1_Object = MibTableColumn
pysmiFakeCol1 = _PysmiFakeCol1_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 26, 4, 3, 1, 4294967295),
    _PysmiFakeCol1_Type()
)
pysmiFakeCol1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol1.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-LIC-R1-MIB",
    **{"MacAddress": MacAddress,
       "a3com": a3com,
       "brouterMIB": brouterMIB,
       "llc": llc,
       "llcPortGroup": llcPortGroup,
       "llcPortAdminTable": llcPortAdminTable,
       "llcPortAdminEntry": llcPortAdminEntry,
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
       "llcPortOperNumSaps": llcPortOperNumSaps,
       "llcPortOperSimRim": llcPortOperSimRim,
       "llcPortOperLastModifyTime": llcPortOperLastModifyTime,
       "llcSapGroup": llcSapGroup,
       "llcSapAdminTable": llcSapAdminTable,
       "llcSapAdminEntry": llcSapAdminEntry,
       "llcSapNumber": llcSapNumber,
       "llcSapOperTable": llcSapOperTable,
       "llcSapOperEntry": llcSapOperEntry,
       "llcSapOperStatus": llcSapOperStatus,
       "llcSapOperNumCcs": llcSapOperNumCcs,
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
       "llcSapStatsReset": llcSapStatsReset,
       "llcCcGroup": llcCcGroup,
       "llcCcAdminTable": llcCcAdminTable,
       "llcCcAdminEntry": llcCcAdminEntry,
       "llcCcLSap": llcCcLSap,
       "llcCcRSap": llcCcRSap,
       "llcCcLMac": llcCcLMac,
       "llcCcRMac": llcCcRMac,
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
       "llcTunnelGroup": llcTunnelGroup,
       "ccsLlcTunnelInfo": ccsLlcTunnelInfo,
       "ccsLlcTunnelVirtualRing": ccsLlcTunnelVirtualRing,
       "ccsLlcTunnelMode": ccsLlcTunnelMode,
       "ccsLlcTunnelSNAPriority": ccsLlcTunnelSNAPriority,
       "ccsLlcTunnelRouterTable": ccsLlcTunnelRouterTable,
       "ccsLlcTunnelRouterEntry": ccsLlcTunnelRouterEntry,
       "ccsLlcPeerAddress": ccsLlcPeerAddress,
       "ccsLlcLocalAddress": ccsLlcLocalAddress,
       "ccsLlcTunnelId": ccsLlcTunnelId,
       "ccsLlcRouterEnable": ccsLlcRouterEnable,
       "ccsLlcRouterMode": ccsLlcRouterMode,
       "ccsLlcRouterTunnelTransport": ccsLlcRouterTunnelTransport,
       "ccsLlcRouterTunnelPort": ccsLlcRouterTunnelPort,
       "ccsLlcRouterPeerString": ccsLlcRouterPeerString,
       "ccsLlcTunnelDefaultDestTable": ccsLlcTunnelDefaultDestTable,
       "ccsLlcTunnelDefaultDestEntry": ccsLlcTunnelDefaultDestEntry,
       "ccsLlcDestTunnelId": ccsLlcDestTunnelId,
       "ccsLlcRemoteMacAddress": ccsLlcRemoteMacAddress,
       "ccsLlcRemoteSap": ccsLlcRemoteSap,
       "ccsLlcRemoteSapLowRange": ccsLlcRemoteSapLowRange,
       "ccsLlcRemoteSapHighRange": ccsLlcRemoteSapHighRange,
       "pysmiFakeCol1": pysmiFakeCol1}
)
