# SNMP MIB module (SNA-LLC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SNA-LLC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:55:44 2024
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
 NotificationType,
 TimeTicks,
 Unsigned32,
 experimental,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "experimental",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(DisplayString,
 RowStatus) = mibBuilder.importSymbols(
    "SNMPv2-TC-v1",
    "DisplayString",
    "RowStatus")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SnaDLCexp_ObjectIdentity = ObjectIdentity
snaDLCexp = _SnaDLCexp_ObjectIdentity(
    (1, 3, 6, 1, 3, 51)
)
_Llc_ObjectIdentity = ObjectIdentity
llc = _Llc_ObjectIdentity(
    (1, 3, 6, 1, 3, 51, 1)
)
_LlcPortGroup_ObjectIdentity = ObjectIdentity
llcPortGroup = _LlcPortGroup_ObjectIdentity(
    (1, 3, 6, 1, 3, 51, 1, 1)
)
_LlcPortAdminTable_Object = MibTable
llcPortAdminTable = _LlcPortAdminTable_Object(
    (1, 3, 6, 1, 3, 51, 1, 1, 1)
)
if mibBuilder.loadTexts:
    llcPortAdminTable.setStatus("mandatory")
_LlcPortAdminEntry_Object = MibTableRow
llcPortAdminEntry = _LlcPortAdminEntry_Object(
    (1, 3, 6, 1, 3, 51, 1, 1, 1, 1)
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
    (1, 3, 6, 1, 3, 51, 1, 1, 1, 1, 1),
    _LlcPortAdminName_Type()
)
llcPortAdminName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcPortAdminName.setStatus("mandatory")


class _LlcPortAdminState_Type(Integer32):
    """Custom type llcPortAdminState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_LlcPortAdminState_Type.__name__ = "Integer32"
_LlcPortAdminState_Object = MibTableColumn
llcPortAdminState = _LlcPortAdminState_Object(
    (1, 3, 6, 1, 3, 51, 1, 1, 1, 1, 2),
    _LlcPortAdminState_Type()
)
llcPortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcPortAdminState.setStatus("mandatory")
_LlcPortAdminMaxIPDUOctetsSend_Type = Integer32
_LlcPortAdminMaxIPDUOctetsSend_Object = MibTableColumn
llcPortAdminMaxIPDUOctetsSend = _LlcPortAdminMaxIPDUOctetsSend_Object(
    (1, 3, 6, 1, 3, 51, 1, 1, 1, 1, 3),
    _LlcPortAdminMaxIPDUOctetsSend_Type()
)
llcPortAdminMaxIPDUOctetsSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcPortAdminMaxIPDUOctetsSend.setStatus("mandatory")
_LlcPortAdminMaxIPDUOctetsRcv_Type = Integer32
_LlcPortAdminMaxIPDUOctetsRcv_Object = MibTableColumn
llcPortAdminMaxIPDUOctetsRcv = _LlcPortAdminMaxIPDUOctetsRcv_Object(
    (1, 3, 6, 1, 3, 51, 1, 1, 1, 1, 4),
    _LlcPortAdminMaxIPDUOctetsRcv_Type()
)
llcPortAdminMaxIPDUOctetsRcv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcPortAdminMaxIPDUOctetsRcv.setStatus("mandatory")


class _LlcPortAdminMaxUnackedIPDUsSend_Type(Integer32):
    """Custom type llcPortAdminMaxUnackedIPDUsSend based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_LlcPortAdminMaxUnackedIPDUsSend_Type.__name__ = "Integer32"
_LlcPortAdminMaxUnackedIPDUsSend_Object = MibTableColumn
llcPortAdminMaxUnackedIPDUsSend = _LlcPortAdminMaxUnackedIPDUsSend_Object(
    (1, 3, 6, 1, 3, 51, 1, 1, 1, 1, 5),
    _LlcPortAdminMaxUnackedIPDUsSend_Type()
)
llcPortAdminMaxUnackedIPDUsSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcPortAdminMaxUnackedIPDUsSend.setStatus("mandatory")


class _LlcPortAdminMaxUnackedIPDUsRcv_Type(Integer32):
    """Custom type llcPortAdminMaxUnackedIPDUsRcv based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_LlcPortAdminMaxUnackedIPDUsRcv_Type.__name__ = "Integer32"
_LlcPortAdminMaxUnackedIPDUsRcv_Object = MibTableColumn
llcPortAdminMaxUnackedIPDUsRcv = _LlcPortAdminMaxUnackedIPDUsRcv_Object(
    (1, 3, 6, 1, 3, 51, 1, 1, 1, 1, 6),
    _LlcPortAdminMaxUnackedIPDUsRcv_Type()
)
llcPortAdminMaxUnackedIPDUsRcv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcPortAdminMaxUnackedIPDUsRcv.setStatus("mandatory")


class _LlcPortAdminMaxRetransmits_Type(Integer32):
    """Custom type llcPortAdminMaxRetransmits based on Integer32"""
    defaultValue = 2


_LlcPortAdminMaxRetransmits_Object = MibTableColumn
llcPortAdminMaxRetransmits = _LlcPortAdminMaxRetransmits_Object(
    (1, 3, 6, 1, 3, 51, 1, 1, 1, 1, 7),
    _LlcPortAdminMaxRetransmits_Type()
)
llcPortAdminMaxRetransmits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcPortAdminMaxRetransmits.setStatus("mandatory")


class _LlcPortAdminAckTimer_Type(TimeTicks):
    """Custom type llcPortAdminAckTimer based on TimeTicks"""
    defaultValue = 1


_LlcPortAdminAckTimer_Object = MibTableColumn
llcPortAdminAckTimer = _LlcPortAdminAckTimer_Object(
    (1, 3, 6, 1, 3, 51, 1, 1, 1, 1, 8),
    _LlcPortAdminAckTimer_Type()
)
llcPortAdminAckTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcPortAdminAckTimer.setStatus("mandatory")


class _LlcPortAdminPbitTimer_Type(TimeTicks):
    """Custom type llcPortAdminPbitTimer based on TimeTicks"""
    defaultValue = 1


_LlcPortAdminPbitTimer_Object = MibTableColumn
llcPortAdminPbitTimer = _LlcPortAdminPbitTimer_Object(
    (1, 3, 6, 1, 3, 51, 1, 1, 1, 1, 9),
    _LlcPortAdminPbitTimer_Type()
)
llcPortAdminPbitTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcPortAdminPbitTimer.setStatus("mandatory")


class _LlcPortAdminRejTimer_Type(TimeTicks):
    """Custom type llcPortAdminRejTimer based on TimeTicks"""
    defaultValue = 1


_LlcPortAdminRejTimer_Object = MibTableColumn
llcPortAdminRejTimer = _LlcPortAdminRejTimer_Object(
    (1, 3, 6, 1, 3, 51, 1, 1, 1, 1, 10),
    _LlcPortAdminRejTimer_Type()
)
llcPortAdminRejTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcPortAdminRejTimer.setStatus("mandatory")


class _LlcPortAdminBusyTimer_Type(TimeTicks):
    """Custom type llcPortAdminBusyTimer based on TimeTicks"""
    defaultValue = 1


_LlcPortAdminBusyTimer_Object = MibTableColumn
llcPortAdminBusyTimer = _LlcPortAdminBusyTimer_Object(
    (1, 3, 6, 1, 3, 51, 1, 1, 1, 1, 11),
    _LlcPortAdminBusyTimer_Type()
)
llcPortAdminBusyTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcPortAdminBusyTimer.setStatus("mandatory")


class _LlcPortAdminInactTimer_Type(TimeTicks):
    """Custom type llcPortAdminInactTimer based on TimeTicks"""
    defaultValue = 1


_LlcPortAdminInactTimer_Object = MibTableColumn
llcPortAdminInactTimer = _LlcPortAdminInactTimer_Object(
    (1, 3, 6, 1, 3, 51, 1, 1, 1, 1, 12),
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
    (1, 3, 6, 1, 3, 51, 1, 1, 1, 1, 13),
    _LlcPortAdminDelayAckCount_Type()
)
llcPortAdminDelayAckCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcPortAdminDelayAckCount.setStatus("mandatory")
_LlcPortAdminDelayAckTimer_Type = TimeTicks
_LlcPortAdminDelayAckTimer_Object = MibTableColumn
llcPortAdminDelayAckTimer = _LlcPortAdminDelayAckTimer_Object(
    (1, 3, 6, 1, 3, 51, 1, 1, 1, 1, 14),
    _LlcPortAdminDelayAckTimer_Type()
)
llcPortAdminDelayAckTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcPortAdminDelayAckTimer.setStatus("mandatory")


class _LlcPortAdminSimRim_Type(Integer32):
    """Custom type llcPortAdminSimRim based on Integer32"""
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


_LlcPortAdminSimRim_Type.__name__ = "Integer32"
_LlcPortAdminSimRim_Object = MibTableColumn
llcPortAdminSimRim = _LlcPortAdminSimRim_Object(
    (1, 3, 6, 1, 3, 51, 1, 1, 1, 1, 15),
    _LlcPortAdminSimRim_Type()
)
llcPortAdminSimRim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcPortAdminSimRim.setStatus("mandatory")
_LlcPortOperTable_Object = MibTable
llcPortOperTable = _LlcPortOperTable_Object(
    (1, 3, 6, 1, 3, 51, 1, 1, 2)
)
if mibBuilder.loadTexts:
    llcPortOperTable.setStatus("mandatory")
_LlcPortOperEntry_Object = MibTableRow
llcPortOperEntry = _LlcPortOperEntry_Object(
    (1, 3, 6, 1, 3, 51, 1, 1, 2, 1)
)
llcPortOperEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    llcPortOperEntry.setStatus("mandatory")


class _LlcPortOperName_Type(DisplayString):
    """Custom type llcPortOperName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_LlcPortOperName_Type.__name__ = "DisplayString"
_LlcPortOperName_Object = MibTableColumn
llcPortOperName = _LlcPortOperName_Object(
    (1, 3, 6, 1, 3, 51, 1, 1, 2, 1, 1),
    _LlcPortOperName_Type()
)
llcPortOperName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcPortOperName.setStatus("mandatory")


class _LlcPortOperISTATUS_Type(Integer32):
    """Custom type llcPortOperISTATUS based on Integer32"""
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


_LlcPortOperISTATUS_Type.__name__ = "Integer32"
_LlcPortOperISTATUS_Object = MibTableColumn
llcPortOperISTATUS = _LlcPortOperISTATUS_Object(
    (1, 3, 6, 1, 3, 51, 1, 1, 2, 1, 2),
    _LlcPortOperISTATUS_Type()
)
llcPortOperISTATUS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcPortOperISTATUS.setStatus("mandatory")
_LlcPortOperLastModifyTime_Type = TimeTicks
_LlcPortOperLastModifyTime_Object = MibTableColumn
llcPortOperLastModifyTime = _LlcPortOperLastModifyTime_Object(
    (1, 3, 6, 1, 3, 51, 1, 1, 2, 1, 3),
    _LlcPortOperLastModifyTime_Type()
)
llcPortOperLastModifyTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcPortOperLastModifyTime.setStatus("mandatory")
_LlcPortOperLastFailTime_Type = TimeTicks
_LlcPortOperLastFailTime_Object = MibTableColumn
llcPortOperLastFailTime = _LlcPortOperLastFailTime_Object(
    (1, 3, 6, 1, 3, 51, 1, 1, 2, 1, 4),
    _LlcPortOperLastFailTime_Type()
)
llcPortOperLastFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcPortOperLastFailTime.setStatus("mandatory")


class _LlcPortOperLastFailCause_Type(Integer32):
    """Custom type llcPortOperLastFailCause based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("physical", 2),
          ("undefined", 1))
    )


_LlcPortOperLastFailCause_Type.__name__ = "Integer32"
_LlcPortOperLastFailCause_Object = MibTableColumn
llcPortOperLastFailCause = _LlcPortOperLastFailCause_Object(
    (1, 3, 6, 1, 3, 51, 1, 1, 2, 1, 5),
    _LlcPortOperLastFailCause_Type()
)
llcPortOperLastFailCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcPortOperLastFailCause.setStatus("mandatory")
_LlcPortStatsTable_Object = MibTable
llcPortStatsTable = _LlcPortStatsTable_Object(
    (1, 3, 6, 1, 3, 51, 1, 1, 3)
)
if mibBuilder.loadTexts:
    llcPortStatsTable.setStatus("mandatory")
_LlcPortStatsEntry_Object = MibTableRow
llcPortStatsEntry = _LlcPortStatsEntry_Object(
    (1, 3, 6, 1, 3, 51, 1, 1, 3, 1)
)
llcPortStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    llcPortStatsEntry.setStatus("mandatory")
_LlcPortStatsPhysicalFailures_Type = Counter32
_LlcPortStatsPhysicalFailures_Object = MibTableColumn
llcPortStatsPhysicalFailures = _LlcPortStatsPhysicalFailures_Object(
    (1, 3, 6, 1, 3, 51, 1, 1, 3, 1, 1),
    _LlcPortStatsPhysicalFailures_Type()
)
llcPortStatsPhysicalFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcPortStatsPhysicalFailures.setStatus("mandatory")
_LlcPortStatsPollsIn_Type = Counter32
_LlcPortStatsPollsIn_Object = MibTableColumn
llcPortStatsPollsIn = _LlcPortStatsPollsIn_Object(
    (1, 3, 6, 1, 3, 51, 1, 1, 3, 1, 2),
    _LlcPortStatsPollsIn_Type()
)
llcPortStatsPollsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcPortStatsPollsIn.setStatus("mandatory")
_LlcPortStatsPollsOut_Type = Counter32
_LlcPortStatsPollsOut_Object = MibTableColumn
llcPortStatsPollsOut = _LlcPortStatsPollsOut_Object(
    (1, 3, 6, 1, 3, 51, 1, 1, 3, 1, 3),
    _LlcPortStatsPollsOut_Type()
)
llcPortStatsPollsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcPortStatsPollsOut.setStatus("mandatory")
_LlcPortStatsPollRspsIn_Type = Counter32
_LlcPortStatsPollRspsIn_Object = MibTableColumn
llcPortStatsPollRspsIn = _LlcPortStatsPollRspsIn_Object(
    (1, 3, 6, 1, 3, 51, 1, 1, 3, 1, 4),
    _LlcPortStatsPollRspsIn_Type()
)
llcPortStatsPollRspsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcPortStatsPollRspsIn.setStatus("mandatory")
_LlcPortStatsPollRspsOut_Type = Counter32
_LlcPortStatsPollRspsOut_Object = MibTableColumn
llcPortStatsPollRspsOut = _LlcPortStatsPollRspsOut_Object(
    (1, 3, 6, 1, 3, 51, 1, 1, 3, 1, 5),
    _LlcPortStatsPollRspsOut_Type()
)
llcPortStatsPollRspsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcPortStatsPollRspsOut.setStatus("mandatory")
_LlcPortStatsLocalBusies_Type = Counter32
_LlcPortStatsLocalBusies_Object = MibTableColumn
llcPortStatsLocalBusies = _LlcPortStatsLocalBusies_Object(
    (1, 3, 6, 1, 3, 51, 1, 1, 3, 1, 6),
    _LlcPortStatsLocalBusies_Type()
)
llcPortStatsLocalBusies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcPortStatsLocalBusies.setStatus("mandatory")
_LlcPortStatsRemoteBusies_Type = Counter32
_LlcPortStatsRemoteBusies_Object = MibTableColumn
llcPortStatsRemoteBusies = _LlcPortStatsRemoteBusies_Object(
    (1, 3, 6, 1, 3, 51, 1, 1, 3, 1, 7),
    _LlcPortStatsRemoteBusies_Type()
)
llcPortStatsRemoteBusies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcPortStatsRemoteBusies.setStatus("mandatory")
_LlcPortStatsIFramesIn_Type = Counter32
_LlcPortStatsIFramesIn_Object = MibTableColumn
llcPortStatsIFramesIn = _LlcPortStatsIFramesIn_Object(
    (1, 3, 6, 1, 3, 51, 1, 1, 3, 1, 8),
    _LlcPortStatsIFramesIn_Type()
)
llcPortStatsIFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcPortStatsIFramesIn.setStatus("mandatory")
_LlcPortStatsIFramesOut_Type = Counter32
_LlcPortStatsIFramesOut_Object = MibTableColumn
llcPortStatsIFramesOut = _LlcPortStatsIFramesOut_Object(
    (1, 3, 6, 1, 3, 51, 1, 1, 3, 1, 9),
    _LlcPortStatsIFramesOut_Type()
)
llcPortStatsIFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcPortStatsIFramesOut.setStatus("mandatory")
_LlcPortStatsOctetsIn_Type = Counter32
_LlcPortStatsOctetsIn_Object = MibTableColumn
llcPortStatsOctetsIn = _LlcPortStatsOctetsIn_Object(
    (1, 3, 6, 1, 3, 51, 1, 1, 3, 1, 10),
    _LlcPortStatsOctetsIn_Type()
)
llcPortStatsOctetsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcPortStatsOctetsIn.setStatus("mandatory")
_LlcPortStatsOctetsOut_Type = Counter32
_LlcPortStatsOctetsOut_Object = MibTableColumn
llcPortStatsOctetsOut = _LlcPortStatsOctetsOut_Object(
    (1, 3, 6, 1, 3, 51, 1, 1, 3, 1, 11),
    _LlcPortStatsOctetsOut_Type()
)
llcPortStatsOctetsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcPortStatsOctetsOut.setStatus("mandatory")
_LlcPortStatsProtocolErrs_Type = Counter32
_LlcPortStatsProtocolErrs_Object = MibTableColumn
llcPortStatsProtocolErrs = _LlcPortStatsProtocolErrs_Object(
    (1, 3, 6, 1, 3, 51, 1, 1, 3, 1, 12),
    _LlcPortStatsProtocolErrs_Type()
)
llcPortStatsProtocolErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcPortStatsProtocolErrs.setStatus("mandatory")
_LlcPortStatsActivityTOs_Type = Counter32
_LlcPortStatsActivityTOs_Object = MibTableColumn
llcPortStatsActivityTOs = _LlcPortStatsActivityTOs_Object(
    (1, 3, 6, 1, 3, 51, 1, 1, 3, 1, 13),
    _LlcPortStatsActivityTOs_Type()
)
llcPortStatsActivityTOs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcPortStatsActivityTOs.setStatus("mandatory")
_LlcPortStatsRetriesExps_Type = Counter32
_LlcPortStatsRetriesExps_Object = MibTableColumn
llcPortStatsRetriesExps = _LlcPortStatsRetriesExps_Object(
    (1, 3, 6, 1, 3, 51, 1, 1, 3, 1, 14),
    _LlcPortStatsRetriesExps_Type()
)
llcPortStatsRetriesExps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcPortStatsRetriesExps.setStatus("mandatory")
_LlcPortStatsRetransmitsIn_Type = Counter32
_LlcPortStatsRetransmitsIn_Object = MibTableColumn
llcPortStatsRetransmitsIn = _LlcPortStatsRetransmitsIn_Object(
    (1, 3, 6, 1, 3, 51, 1, 1, 3, 1, 15),
    _LlcPortStatsRetransmitsIn_Type()
)
llcPortStatsRetransmitsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcPortStatsRetransmitsIn.setStatus("mandatory")
_LlcPortStatsRetransmitsOut_Type = Counter32
_LlcPortStatsRetransmitsOut_Object = MibTableColumn
llcPortStatsRetransmitsOut = _LlcPortStatsRetransmitsOut_Object(
    (1, 3, 6, 1, 3, 51, 1, 1, 3, 1, 16),
    _LlcPortStatsRetransmitsOut_Type()
)
llcPortStatsRetransmitsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcPortStatsRetransmitsOut.setStatus("mandatory")
_LlcSapGroup_ObjectIdentity = ObjectIdentity
llcSapGroup = _LlcSapGroup_ObjectIdentity(
    (1, 3, 6, 1, 3, 51, 1, 2)
)
_LlcSapAdminTable_Object = MibTable
llcSapAdminTable = _LlcSapAdminTable_Object(
    (1, 3, 6, 1, 3, 51, 1, 2, 1)
)
if mibBuilder.loadTexts:
    llcSapAdminTable.setStatus("mandatory")
_LlcSapAdminEntry_Object = MibTableRow
llcSapAdminEntry = _LlcSapAdminEntry_Object(
    (1, 3, 6, 1, 3, 51, 1, 2, 1, 1)
)
llcSapAdminEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SNA-LLC-MIB", "llcSapNumber"),
)
if mibBuilder.loadTexts:
    llcSapAdminEntry.setStatus("mandatory")


class _LlcSapNumber_Type(Integer32):
    """Custom type llcSapNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_LlcSapNumber_Type.__name__ = "Integer32"
_LlcSapNumber_Object = MibTableColumn
llcSapNumber = _LlcSapNumber_Object(
    (1, 3, 6, 1, 3, 51, 1, 2, 1, 1, 1),
    _LlcSapNumber_Type()
)
llcSapNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcSapNumber.setStatus("mandatory")


class _LlcSapAdminState_Type(Integer32):
    """Custom type llcSapAdminState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_LlcSapAdminState_Type.__name__ = "Integer32"
_LlcSapAdminState_Object = MibTableColumn
llcSapAdminState = _LlcSapAdminState_Object(
    (1, 3, 6, 1, 3, 51, 1, 2, 1, 1, 2),
    _LlcSapAdminState_Type()
)
llcSapAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcSapAdminState.setStatus("mandatory")


class _LlcSapAdminMaxIPDUOctetsSend_Type(Integer32):
    """Custom type llcSapAdminMaxIPDUOctetsSend based on Integer32"""
    defaultValue = 0


_LlcSapAdminMaxIPDUOctetsSend_Object = MibTableColumn
llcSapAdminMaxIPDUOctetsSend = _LlcSapAdminMaxIPDUOctetsSend_Object(
    (1, 3, 6, 1, 3, 51, 1, 2, 1, 1, 3),
    _LlcSapAdminMaxIPDUOctetsSend_Type()
)
llcSapAdminMaxIPDUOctetsSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcSapAdminMaxIPDUOctetsSend.setStatus("mandatory")


class _LlcSapAdminMaxIPDUOctetsRcv_Type(Integer32):
    """Custom type llcSapAdminMaxIPDUOctetsRcv based on Integer32"""
    defaultValue = 0


_LlcSapAdminMaxIPDUOctetsRcv_Object = MibTableColumn
llcSapAdminMaxIPDUOctetsRcv = _LlcSapAdminMaxIPDUOctetsRcv_Object(
    (1, 3, 6, 1, 3, 51, 1, 2, 1, 1, 4),
    _LlcSapAdminMaxIPDUOctetsRcv_Type()
)
llcSapAdminMaxIPDUOctetsRcv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcSapAdminMaxIPDUOctetsRcv.setStatus("mandatory")


class _LlcSapAdminMaxUnackedIPDUsSend_Type(Integer32):
    """Custom type llcSapAdminMaxUnackedIPDUsSend based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_LlcSapAdminMaxUnackedIPDUsSend_Type.__name__ = "Integer32"
_LlcSapAdminMaxUnackedIPDUsSend_Object = MibTableColumn
llcSapAdminMaxUnackedIPDUsSend = _LlcSapAdminMaxUnackedIPDUsSend_Object(
    (1, 3, 6, 1, 3, 51, 1, 2, 1, 1, 5),
    _LlcSapAdminMaxUnackedIPDUsSend_Type()
)
llcSapAdminMaxUnackedIPDUsSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcSapAdminMaxUnackedIPDUsSend.setStatus("mandatory")


class _LlcSapAdminMaxUnackedIPDUsRcv_Type(Integer32):
    """Custom type llcSapAdminMaxUnackedIPDUsRcv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_LlcSapAdminMaxUnackedIPDUsRcv_Type.__name__ = "Integer32"
_LlcSapAdminMaxUnackedIPDUsRcv_Object = MibTableColumn
llcSapAdminMaxUnackedIPDUsRcv = _LlcSapAdminMaxUnackedIPDUsRcv_Object(
    (1, 3, 6, 1, 3, 51, 1, 2, 1, 1, 6),
    _LlcSapAdminMaxUnackedIPDUsRcv_Type()
)
llcSapAdminMaxUnackedIPDUsRcv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcSapAdminMaxUnackedIPDUsRcv.setStatus("mandatory")


class _LlcSapAdminMaxRetransmits_Type(Integer32):
    """Custom type llcSapAdminMaxRetransmits based on Integer32"""
    defaultValue = 0


_LlcSapAdminMaxRetransmits_Object = MibTableColumn
llcSapAdminMaxRetransmits = _LlcSapAdminMaxRetransmits_Object(
    (1, 3, 6, 1, 3, 51, 1, 2, 1, 1, 7),
    _LlcSapAdminMaxRetransmits_Type()
)
llcSapAdminMaxRetransmits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcSapAdminMaxRetransmits.setStatus("mandatory")


class _LlcSapAdminAckTimer_Type(TimeTicks):
    """Custom type llcSapAdminAckTimer based on TimeTicks"""
    defaultValue = 0


_LlcSapAdminAckTimer_Object = MibTableColumn
llcSapAdminAckTimer = _LlcSapAdminAckTimer_Object(
    (1, 3, 6, 1, 3, 51, 1, 2, 1, 1, 8),
    _LlcSapAdminAckTimer_Type()
)
llcSapAdminAckTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcSapAdminAckTimer.setStatus("mandatory")


class _LlcSapAdminPbitTimer_Type(TimeTicks):
    """Custom type llcSapAdminPbitTimer based on TimeTicks"""
    defaultValue = 0


_LlcSapAdminPbitTimer_Object = MibTableColumn
llcSapAdminPbitTimer = _LlcSapAdminPbitTimer_Object(
    (1, 3, 6, 1, 3, 51, 1, 2, 1, 1, 9),
    _LlcSapAdminPbitTimer_Type()
)
llcSapAdminPbitTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcSapAdminPbitTimer.setStatus("mandatory")


class _LlcSapAdminRejTimer_Type(TimeTicks):
    """Custom type llcSapAdminRejTimer based on TimeTicks"""
    defaultValue = 0


_LlcSapAdminRejTimer_Object = MibTableColumn
llcSapAdminRejTimer = _LlcSapAdminRejTimer_Object(
    (1, 3, 6, 1, 3, 51, 1, 2, 1, 1, 10),
    _LlcSapAdminRejTimer_Type()
)
llcSapAdminRejTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcSapAdminRejTimer.setStatus("mandatory")


class _LlcSapAdminBusyTimer_Type(TimeTicks):
    """Custom type llcSapAdminBusyTimer based on TimeTicks"""
    defaultValue = 0


_LlcSapAdminBusyTimer_Object = MibTableColumn
llcSapAdminBusyTimer = _LlcSapAdminBusyTimer_Object(
    (1, 3, 6, 1, 3, 51, 1, 2, 1, 1, 11),
    _LlcSapAdminBusyTimer_Type()
)
llcSapAdminBusyTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcSapAdminBusyTimer.setStatus("mandatory")


class _LlcSapAdminInactTimer_Type(TimeTicks):
    """Custom type llcSapAdminInactTimer based on TimeTicks"""
    defaultValue = 0


_LlcSapAdminInactTimer_Object = MibTableColumn
llcSapAdminInactTimer = _LlcSapAdminInactTimer_Object(
    (1, 3, 6, 1, 3, 51, 1, 2, 1, 1, 12),
    _LlcSapAdminInactTimer_Type()
)
llcSapAdminInactTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcSapAdminInactTimer.setStatus("mandatory")


class _LlcSapAdminDelayAckCount_Type(Integer32):
    """Custom type llcSapAdminDelayAckCount based on Integer32"""
    defaultValue = 0


_LlcSapAdminDelayAckCount_Object = MibTableColumn
llcSapAdminDelayAckCount = _LlcSapAdminDelayAckCount_Object(
    (1, 3, 6, 1, 3, 51, 1, 2, 1, 1, 13),
    _LlcSapAdminDelayAckCount_Type()
)
llcSapAdminDelayAckCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcSapAdminDelayAckCount.setStatus("mandatory")


class _LlcSapAdminDelayAckTimer_Type(TimeTicks):
    """Custom type llcSapAdminDelayAckTimer based on TimeTicks"""
    defaultValue = 0


_LlcSapAdminDelayAckTimer_Object = MibTableColumn
llcSapAdminDelayAckTimer = _LlcSapAdminDelayAckTimer_Object(
    (1, 3, 6, 1, 3, 51, 1, 2, 1, 1, 14),
    _LlcSapAdminDelayAckTimer_Type()
)
llcSapAdminDelayAckTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcSapAdminDelayAckTimer.setStatus("mandatory")
_LlcSapOperTable_Object = MibTable
llcSapOperTable = _LlcSapOperTable_Object(
    (1, 3, 6, 1, 3, 51, 1, 2, 2)
)
if mibBuilder.loadTexts:
    llcSapOperTable.setStatus("mandatory")
_LlcSapOperEntry_Object = MibTableRow
llcSapOperEntry = _LlcSapOperEntry_Object(
    (1, 3, 6, 1, 3, 51, 1, 2, 2, 1)
)
llcSapOperEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SNA-LLC-MIB", "llcSapNumber"),
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
    (1, 3, 6, 1, 3, 51, 1, 2, 2, 1, 1),
    _LlcSapOperStatus_Type()
)
llcSapOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapOperStatus.setStatus("mandatory")
_LlcSapStatsTable_Object = MibTable
llcSapStatsTable = _LlcSapStatsTable_Object(
    (1, 3, 6, 1, 3, 51, 1, 2, 3)
)
if mibBuilder.loadTexts:
    llcSapStatsTable.setStatus("mandatory")
_LlcSapStatsEntry_Object = MibTableRow
llcSapStatsEntry = _LlcSapStatsEntry_Object(
    (1, 3, 6, 1, 3, 51, 1, 2, 3, 1)
)
llcSapStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SNA-LLC-MIB", "llcSapNumber"),
)
if mibBuilder.loadTexts:
    llcSapStatsEntry.setStatus("mandatory")
_LlcSapStatsTESTsIn_Type = Counter32
_LlcSapStatsTESTsIn_Object = MibTableColumn
llcSapStatsTESTsIn = _LlcSapStatsTESTsIn_Object(
    (1, 3, 6, 1, 3, 51, 1, 2, 3, 1, 1),
    _LlcSapStatsTESTsIn_Type()
)
llcSapStatsTESTsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapStatsTESTsIn.setStatus("mandatory")
_LlcSapStatsTESTsOut_Type = Counter32
_LlcSapStatsTESTsOut_Object = MibTableColumn
llcSapStatsTESTsOut = _LlcSapStatsTESTsOut_Object(
    (1, 3, 6, 1, 3, 51, 1, 2, 3, 1, 2),
    _LlcSapStatsTESTsOut_Type()
)
llcSapStatsTESTsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapStatsTESTsOut.setStatus("mandatory")
_LlcSapStatsXIDsIn_Type = Counter32
_LlcSapStatsXIDsIn_Object = MibTableColumn
llcSapStatsXIDsIn = _LlcSapStatsXIDsIn_Object(
    (1, 3, 6, 1, 3, 51, 1, 2, 3, 1, 3),
    _LlcSapStatsXIDsIn_Type()
)
llcSapStatsXIDsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapStatsXIDsIn.setStatus("mandatory")
_LlcSapStatsXIDsOut_Type = Counter32
_LlcSapStatsXIDsOut_Object = MibTableColumn
llcSapStatsXIDsOut = _LlcSapStatsXIDsOut_Object(
    (1, 3, 6, 1, 3, 51, 1, 2, 3, 1, 4),
    _LlcSapStatsXIDsOut_Type()
)
llcSapStatsXIDsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapStatsXIDsOut.setStatus("mandatory")
_LlcSapStatsUIFramesIn_Type = Counter32
_LlcSapStatsUIFramesIn_Object = MibTableColumn
llcSapStatsUIFramesIn = _LlcSapStatsUIFramesIn_Object(
    (1, 3, 6, 1, 3, 51, 1, 2, 3, 1, 5),
    _LlcSapStatsUIFramesIn_Type()
)
llcSapStatsUIFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapStatsUIFramesIn.setStatus("mandatory")
_LlcSapStatsUIFramesOut_Type = Counter32
_LlcSapStatsUIFramesOut_Object = MibTableColumn
llcSapStatsUIFramesOut = _LlcSapStatsUIFramesOut_Object(
    (1, 3, 6, 1, 3, 51, 1, 2, 3, 1, 6),
    _LlcSapStatsUIFramesOut_Type()
)
llcSapStatsUIFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcSapStatsUIFramesOut.setStatus("mandatory")
_LlcCcGroup_ObjectIdentity = ObjectIdentity
llcCcGroup = _LlcCcGroup_ObjectIdentity(
    (1, 3, 6, 1, 3, 51, 1, 3)
)
_LlcCcAdminTable_Object = MibTable
llcCcAdminTable = _LlcCcAdminTable_Object(
    (1, 3, 6, 1, 3, 51, 1, 3, 1)
)
if mibBuilder.loadTexts:
    llcCcAdminTable.setStatus("mandatory")
_LlcCcAdminEntry_Object = MibTableRow
llcCcAdminEntry = _LlcCcAdminEntry_Object(
    (1, 3, 6, 1, 3, 51, 1, 3, 1, 1)
)
llcCcAdminEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SNA-LLC-MIB", "llcCcLSap"),
    (0, "SNA-LLC-MIB", "llcCcRSap"),
    (0, "SNA-LLC-MIB", "llcCcRMac"),
    (0, "SNA-LLC-MIB", "llcCcLMac"),
)
if mibBuilder.loadTexts:
    llcCcAdminEntry.setStatus("mandatory")


class _LlcCcLSap_Type(Integer32):
    """Custom type llcCcLSap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_LlcCcLSap_Type.__name__ = "Integer32"
_LlcCcLSap_Object = MibTableColumn
llcCcLSap = _LlcCcLSap_Object(
    (1, 3, 6, 1, 3, 51, 1, 3, 1, 1, 1),
    _LlcCcLSap_Type()
)
llcCcLSap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcCcLSap.setStatus("mandatory")


class _LlcCcRSap_Type(Integer32):
    """Custom type llcCcRSap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_LlcCcRSap_Type.__name__ = "Integer32"
_LlcCcRSap_Object = MibTableColumn
llcCcRSap = _LlcCcRSap_Object(
    (1, 3, 6, 1, 3, 51, 1, 3, 1, 1, 2),
    _LlcCcRSap_Type()
)
llcCcRSap.setMaxAccess("read-write")
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
    (1, 3, 6, 1, 3, 51, 1, 3, 1, 1, 3),
    _LlcCcLMac_Type()
)
llcCcLMac.setMaxAccess("read-write")
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
    (1, 3, 6, 1, 3, 51, 1, 3, 1, 1, 4),
    _LlcCcRMac_Type()
)
llcCcRMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcCcRMac.setStatus("mandatory")


class _LlcCcAdminState_Type(Integer32):
    """Custom type llcCcAdminState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_LlcCcAdminState_Type.__name__ = "Integer32"
_LlcCcAdminState_Object = MibTableColumn
llcCcAdminState = _LlcCcAdminState_Object(
    (1, 3, 6, 1, 3, 51, 1, 3, 1, 1, 5),
    _LlcCcAdminState_Type()
)
llcCcAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcCcAdminState.setStatus("mandatory")


class _LlcCcAdminMaxIPDUOctetsSend_Type(Integer32):
    """Custom type llcCcAdminMaxIPDUOctetsSend based on Integer32"""
    defaultValue = 0


_LlcCcAdminMaxIPDUOctetsSend_Object = MibTableColumn
llcCcAdminMaxIPDUOctetsSend = _LlcCcAdminMaxIPDUOctetsSend_Object(
    (1, 3, 6, 1, 3, 51, 1, 3, 1, 1, 6),
    _LlcCcAdminMaxIPDUOctetsSend_Type()
)
llcCcAdminMaxIPDUOctetsSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcCcAdminMaxIPDUOctetsSend.setStatus("mandatory")


class _LlcCcAdminMaxIPDUOctetsRcv_Type(Integer32):
    """Custom type llcCcAdminMaxIPDUOctetsRcv based on Integer32"""
    defaultValue = 0


_LlcCcAdminMaxIPDUOctetsRcv_Object = MibTableColumn
llcCcAdminMaxIPDUOctetsRcv = _LlcCcAdminMaxIPDUOctetsRcv_Object(
    (1, 3, 6, 1, 3, 51, 1, 3, 1, 1, 7),
    _LlcCcAdminMaxIPDUOctetsRcv_Type()
)
llcCcAdminMaxIPDUOctetsRcv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcCcAdminMaxIPDUOctetsRcv.setStatus("mandatory")


class _LlcCcAdminMaxUnackedIPDUsSend_Type(Integer32):
    """Custom type llcCcAdminMaxUnackedIPDUsSend based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_LlcCcAdminMaxUnackedIPDUsSend_Type.__name__ = "Integer32"
_LlcCcAdminMaxUnackedIPDUsSend_Object = MibTableColumn
llcCcAdminMaxUnackedIPDUsSend = _LlcCcAdminMaxUnackedIPDUsSend_Object(
    (1, 3, 6, 1, 3, 51, 1, 3, 1, 1, 8),
    _LlcCcAdminMaxUnackedIPDUsSend_Type()
)
llcCcAdminMaxUnackedIPDUsSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcCcAdminMaxUnackedIPDUsSend.setStatus("mandatory")


class _LlcCcAdminMaxUnackedIPDUsRcv_Type(Integer32):
    """Custom type llcCcAdminMaxUnackedIPDUsRcv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_LlcCcAdminMaxUnackedIPDUsRcv_Type.__name__ = "Integer32"
_LlcCcAdminMaxUnackedIPDUsRcv_Object = MibTableColumn
llcCcAdminMaxUnackedIPDUsRcv = _LlcCcAdminMaxUnackedIPDUsRcv_Object(
    (1, 3, 6, 1, 3, 51, 1, 3, 1, 1, 9),
    _LlcCcAdminMaxUnackedIPDUsRcv_Type()
)
llcCcAdminMaxUnackedIPDUsRcv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcCcAdminMaxUnackedIPDUsRcv.setStatus("mandatory")


class _LlcCcAdminMaxRetransmits_Type(Integer32):
    """Custom type llcCcAdminMaxRetransmits based on Integer32"""
    defaultValue = 0


_LlcCcAdminMaxRetransmits_Object = MibTableColumn
llcCcAdminMaxRetransmits = _LlcCcAdminMaxRetransmits_Object(
    (1, 3, 6, 1, 3, 51, 1, 3, 1, 1, 10),
    _LlcCcAdminMaxRetransmits_Type()
)
llcCcAdminMaxRetransmits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcCcAdminMaxRetransmits.setStatus("mandatory")


class _LlcCcAdminAckTimer_Type(TimeTicks):
    """Custom type llcCcAdminAckTimer based on TimeTicks"""
    defaultValue = 0


_LlcCcAdminAckTimer_Object = MibTableColumn
llcCcAdminAckTimer = _LlcCcAdminAckTimer_Object(
    (1, 3, 6, 1, 3, 51, 1, 3, 1, 1, 11),
    _LlcCcAdminAckTimer_Type()
)
llcCcAdminAckTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcCcAdminAckTimer.setStatus("mandatory")


class _LlcCcAdminPbitTimer_Type(TimeTicks):
    """Custom type llcCcAdminPbitTimer based on TimeTicks"""
    defaultValue = 0


_LlcCcAdminPbitTimer_Object = MibTableColumn
llcCcAdminPbitTimer = _LlcCcAdminPbitTimer_Object(
    (1, 3, 6, 1, 3, 51, 1, 3, 1, 1, 12),
    _LlcCcAdminPbitTimer_Type()
)
llcCcAdminPbitTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcCcAdminPbitTimer.setStatus("mandatory")


class _LlcCcAdminRejTimer_Type(TimeTicks):
    """Custom type llcCcAdminRejTimer based on TimeTicks"""
    defaultValue = 0


_LlcCcAdminRejTimer_Object = MibTableColumn
llcCcAdminRejTimer = _LlcCcAdminRejTimer_Object(
    (1, 3, 6, 1, 3, 51, 1, 3, 1, 1, 13),
    _LlcCcAdminRejTimer_Type()
)
llcCcAdminRejTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcCcAdminRejTimer.setStatus("mandatory")


class _LlcCcAdminBusyTimer_Type(TimeTicks):
    """Custom type llcCcAdminBusyTimer based on TimeTicks"""
    defaultValue = 0


_LlcCcAdminBusyTimer_Object = MibTableColumn
llcCcAdminBusyTimer = _LlcCcAdminBusyTimer_Object(
    (1, 3, 6, 1, 3, 51, 1, 3, 1, 1, 14),
    _LlcCcAdminBusyTimer_Type()
)
llcCcAdminBusyTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcCcAdminBusyTimer.setStatus("mandatory")


class _LlcCcAdminInactTimer_Type(TimeTicks):
    """Custom type llcCcAdminInactTimer based on TimeTicks"""
    defaultValue = 0


_LlcCcAdminInactTimer_Object = MibTableColumn
llcCcAdminInactTimer = _LlcCcAdminInactTimer_Object(
    (1, 3, 6, 1, 3, 51, 1, 3, 1, 1, 15),
    _LlcCcAdminInactTimer_Type()
)
llcCcAdminInactTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcCcAdminInactTimer.setStatus("mandatory")


class _LlcCcAdminDelayAckCount_Type(Integer32):
    """Custom type llcCcAdminDelayAckCount based on Integer32"""
    defaultValue = 0


_LlcCcAdminDelayAckCount_Object = MibTableColumn
llcCcAdminDelayAckCount = _LlcCcAdminDelayAckCount_Object(
    (1, 3, 6, 1, 3, 51, 1, 3, 1, 1, 16),
    _LlcCcAdminDelayAckCount_Type()
)
llcCcAdminDelayAckCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcCcAdminDelayAckCount.setStatus("mandatory")


class _LlcCcAdminDelayAckTimer_Type(TimeTicks):
    """Custom type llcCcAdminDelayAckTimer based on TimeTicks"""
    defaultValue = 0


_LlcCcAdminDelayAckTimer_Object = MibTableColumn
llcCcAdminDelayAckTimer = _LlcCcAdminDelayAckTimer_Object(
    (1, 3, 6, 1, 3, 51, 1, 3, 1, 1, 17),
    _LlcCcAdminDelayAckTimer_Type()
)
llcCcAdminDelayAckTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcCcAdminDelayAckTimer.setStatus("mandatory")
_LlcCcAdminRowStatus_Type = RowStatus
_LlcCcAdminRowStatus_Object = MibTableColumn
llcCcAdminRowStatus = _LlcCcAdminRowStatus_Object(
    (1, 3, 6, 1, 3, 51, 1, 3, 1, 1, 18),
    _LlcCcAdminRowStatus_Type()
)
llcCcAdminRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcCcAdminRowStatus.setStatus("mandatory")
_LlcCcOperTable_Object = MibTable
llcCcOperTable = _LlcCcOperTable_Object(
    (1, 3, 6, 1, 3, 51, 1, 3, 2)
)
if mibBuilder.loadTexts:
    llcCcOperTable.setStatus("mandatory")
_LlcCcOperEntry_Object = MibTableRow
llcCcOperEntry = _LlcCcOperEntry_Object(
    (1, 3, 6, 1, 3, 51, 1, 3, 2, 1)
)
llcCcOperEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SNA-LLC-MIB", "llcCcLSap"),
    (0, "SNA-LLC-MIB", "llcCcRSap"),
    (0, "SNA-LLC-MIB", "llcCcRMac"),
    (0, "SNA-LLC-MIB", "llcCcLMac"),
)
if mibBuilder.loadTexts:
    llcCcOperEntry.setStatus("mandatory")


class _LlcCcOperRole_Type(Integer32):
    """Custom type llcCcOperRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2),
          ("undefined", 3))
    )


_LlcCcOperRole_Type.__name__ = "Integer32"
_LlcCcOperRole_Object = MibTableColumn
llcCcOperRole = _LlcCcOperRole_Object(
    (1, 3, 6, 1, 3, 51, 1, 3, 2, 1, 1),
    _LlcCcOperRole_Type()
)
llcCcOperRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcOperRole.setStatus("mandatory")


class _LlcCcOperState_Type(Integer32):
    """Custom type llcCcOperState based on Integer32"""
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
        *(("contactPending", 2),
          ("contacted", 3),
          ("discontactPending", 4),
          ("discontacted", 1))
    )


_LlcCcOperState_Type.__name__ = "Integer32"
_LlcCcOperState_Object = MibTableColumn
llcCcOperState = _LlcCcOperState_Object(
    (1, 3, 6, 1, 3, 51, 1, 3, 2, 1, 2),
    _LlcCcOperState_Type()
)
llcCcOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcOperState.setStatus("mandatory")
_LlcCcOperMaxIPDUOctetsSend_Type = Integer32
_LlcCcOperMaxIPDUOctetsSend_Object = MibTableColumn
llcCcOperMaxIPDUOctetsSend = _LlcCcOperMaxIPDUOctetsSend_Object(
    (1, 3, 6, 1, 3, 51, 1, 3, 2, 1, 3),
    _LlcCcOperMaxIPDUOctetsSend_Type()
)
llcCcOperMaxIPDUOctetsSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcCcOperMaxIPDUOctetsSend.setStatus("mandatory")
_LlcCcOperMaxIPDUOctetsRcv_Type = Integer32
_LlcCcOperMaxIPDUOctetsRcv_Object = MibTableColumn
llcCcOperMaxIPDUOctetsRcv = _LlcCcOperMaxIPDUOctetsRcv_Object(
    (1, 3, 6, 1, 3, 51, 1, 3, 2, 1, 4),
    _LlcCcOperMaxIPDUOctetsRcv_Type()
)
llcCcOperMaxIPDUOctetsRcv.setMaxAccess("read-write")
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
    (1, 3, 6, 1, 3, 51, 1, 3, 2, 1, 5),
    _LlcCcOperMaxUnackedIPDUsSend_Type()
)
llcCcOperMaxUnackedIPDUsSend.setMaxAccess("read-write")
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
    (1, 3, 6, 1, 3, 51, 1, 3, 2, 1, 6),
    _LlcCcOperMaxUnackedIPDUsRcv_Type()
)
llcCcOperMaxUnackedIPDUsRcv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcCcOperMaxUnackedIPDUsRcv.setStatus("mandatory")
_LlcCcOperMaxRetransmits_Type = Integer32
_LlcCcOperMaxRetransmits_Object = MibTableColumn
llcCcOperMaxRetransmits = _LlcCcOperMaxRetransmits_Object(
    (1, 3, 6, 1, 3, 51, 1, 3, 2, 1, 7),
    _LlcCcOperMaxRetransmits_Type()
)
llcCcOperMaxRetransmits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcCcOperMaxRetransmits.setStatus("mandatory")
_LlcCcOperAckTimer_Type = TimeTicks
_LlcCcOperAckTimer_Object = MibTableColumn
llcCcOperAckTimer = _LlcCcOperAckTimer_Object(
    (1, 3, 6, 1, 3, 51, 1, 3, 2, 1, 8),
    _LlcCcOperAckTimer_Type()
)
llcCcOperAckTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcCcOperAckTimer.setStatus("mandatory")
_LlcCcOperPbitTimer_Type = TimeTicks
_LlcCcOperPbitTimer_Object = MibTableColumn
llcCcOperPbitTimer = _LlcCcOperPbitTimer_Object(
    (1, 3, 6, 1, 3, 51, 1, 3, 2, 1, 9),
    _LlcCcOperPbitTimer_Type()
)
llcCcOperPbitTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcCcOperPbitTimer.setStatus("mandatory")
_LlcCcOperRejTimer_Type = TimeTicks
_LlcCcOperRejTimer_Object = MibTableColumn
llcCcOperRejTimer = _LlcCcOperRejTimer_Object(
    (1, 3, 6, 1, 3, 51, 1, 3, 2, 1, 10),
    _LlcCcOperRejTimer_Type()
)
llcCcOperRejTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcCcOperRejTimer.setStatus("mandatory")
_LlcCcOperBusyTimer_Type = TimeTicks
_LlcCcOperBusyTimer_Object = MibTableColumn
llcCcOperBusyTimer = _LlcCcOperBusyTimer_Object(
    (1, 3, 6, 1, 3, 51, 1, 3, 2, 1, 11),
    _LlcCcOperBusyTimer_Type()
)
llcCcOperBusyTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcCcOperBusyTimer.setStatus("mandatory")
_LlcCcOperInactTimer_Type = TimeTicks
_LlcCcOperInactTimer_Object = MibTableColumn
llcCcOperInactTimer = _LlcCcOperInactTimer_Object(
    (1, 3, 6, 1, 3, 51, 1, 3, 2, 1, 12),
    _LlcCcOperInactTimer_Type()
)
llcCcOperInactTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcCcOperInactTimer.setStatus("mandatory")
_LlcCcOperDelayAckCount_Type = Integer32
_LlcCcOperDelayAckCount_Object = MibTableColumn
llcCcOperDelayAckCount = _LlcCcOperDelayAckCount_Object(
    (1, 3, 6, 1, 3, 51, 1, 3, 2, 1, 13),
    _LlcCcOperDelayAckCount_Type()
)
llcCcOperDelayAckCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcCcOperDelayAckCount.setStatus("mandatory")
_LlcCcOperDelayAckTimer_Type = TimeTicks
_LlcCcOperDelayAckTimer_Object = MibTableColumn
llcCcOperDelayAckTimer = _LlcCcOperDelayAckTimer_Object(
    (1, 3, 6, 1, 3, 51, 1, 3, 2, 1, 14),
    _LlcCcOperDelayAckTimer_Type()
)
llcCcOperDelayAckTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcCcOperDelayAckTimer.setStatus("mandatory")
_LlcCcOperCreateTime_Type = TimeTicks
_LlcCcOperCreateTime_Object = MibTableColumn
llcCcOperCreateTime = _LlcCcOperCreateTime_Object(
    (1, 3, 6, 1, 3, 51, 1, 3, 2, 1, 15),
    _LlcCcOperCreateTime_Type()
)
llcCcOperCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcOperCreateTime.setStatus("mandatory")
_LlcCcOperLastModifyTime_Type = TimeTicks
_LlcCcOperLastModifyTime_Object = MibTableColumn
llcCcOperLastModifyTime = _LlcCcOperLastModifyTime_Object(
    (1, 3, 6, 1, 3, 51, 1, 3, 2, 1, 16),
    _LlcCcOperLastModifyTime_Type()
)
llcCcOperLastModifyTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcOperLastModifyTime.setStatus("mandatory")
_LlcCcOperLastFailTime_Type = TimeTicks
_LlcCcOperLastFailTime_Object = MibTableColumn
llcCcOperLastFailTime = _LlcCcOperLastFailTime_Object(
    (1, 3, 6, 1, 3, 51, 1, 3, 2, 1, 17),
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
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("discReceived", 7),
          ("dmReceived", 8),
          ("noActivity", 6),
          ("noResponse", 4),
          ("protocolErr", 5),
          ("retriesExpired", 9),
          ("rxFRMR", 2),
          ("txFRMR", 3),
          ("undefined", 1))
    )


_LlcCcOperLastFailCause_Type.__name__ = "Integer32"
_LlcCcOperLastFailCause_Object = MibTableColumn
llcCcOperLastFailCause = _LlcCcOperLastFailCause_Object(
    (1, 3, 6, 1, 3, 51, 1, 3, 2, 1, 18),
    _LlcCcOperLastFailCause_Type()
)
llcCcOperLastFailCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcOperLastFailCause.setStatus("mandatory")


class _LlcCcOperLastFailFRMRInfo_Type(OctetString):
    """Custom type llcCcOperLastFailFRMRInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_LlcCcOperLastFailFRMRInfo_Type.__name__ = "OctetString"
_LlcCcOperLastFailFRMRInfo_Object = MibTableColumn
llcCcOperLastFailFRMRInfo = _LlcCcOperLastFailFRMRInfo_Object(
    (1, 3, 6, 1, 3, 51, 1, 3, 2, 1, 19),
    _LlcCcOperLastFailFRMRInfo_Type()
)
llcCcOperLastFailFRMRInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcOperLastFailFRMRInfo.setStatus("mandatory")
_LlcCcStatsTable_Object = MibTable
llcCcStatsTable = _LlcCcStatsTable_Object(
    (1, 3, 6, 1, 3, 51, 1, 3, 3)
)
if mibBuilder.loadTexts:
    llcCcStatsTable.setStatus("mandatory")
_LlcCcStatsEntry_Object = MibTableRow
llcCcStatsEntry = _LlcCcStatsEntry_Object(
    (1, 3, 6, 1, 3, 51, 1, 3, 3, 1)
)
llcCcStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "SNA-LLC-MIB", "llcCcLSap"),
    (0, "SNA-LLC-MIB", "llcCcRSap"),
    (0, "SNA-LLC-MIB", "llcCcRMac"),
    (0, "SNA-LLC-MIB", "llcCcLMac"),
)
if mibBuilder.loadTexts:
    llcCcStatsEntry.setStatus("mandatory")
_LlcCcStatsLocalBusies_Type = Counter32
_LlcCcStatsLocalBusies_Object = MibTableColumn
llcCcStatsLocalBusies = _LlcCcStatsLocalBusies_Object(
    (1, 3, 6, 1, 3, 51, 1, 3, 3, 1, 1),
    _LlcCcStatsLocalBusies_Type()
)
llcCcStatsLocalBusies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcStatsLocalBusies.setStatus("mandatory")
_LlcCcStatsRemoteBusies_Type = Counter32
_LlcCcStatsRemoteBusies_Object = MibTableColumn
llcCcStatsRemoteBusies = _LlcCcStatsRemoteBusies_Object(
    (1, 3, 6, 1, 3, 51, 1, 3, 3, 1, 2),
    _LlcCcStatsRemoteBusies_Type()
)
llcCcStatsRemoteBusies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcStatsRemoteBusies.setStatus("mandatory")
_LlcCcStatsIFramesIn_Type = Counter32
_LlcCcStatsIFramesIn_Object = MibTableColumn
llcCcStatsIFramesIn = _LlcCcStatsIFramesIn_Object(
    (1, 3, 6, 1, 3, 51, 1, 3, 3, 1, 3),
    _LlcCcStatsIFramesIn_Type()
)
llcCcStatsIFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcStatsIFramesIn.setStatus("mandatory")
_LlcCcStatsIFramesOut_Type = Counter32
_LlcCcStatsIFramesOut_Object = MibTableColumn
llcCcStatsIFramesOut = _LlcCcStatsIFramesOut_Object(
    (1, 3, 6, 1, 3, 51, 1, 3, 3, 1, 4),
    _LlcCcStatsIFramesOut_Type()
)
llcCcStatsIFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcStatsIFramesOut.setStatus("mandatory")
_LlcCcStatsIOctetsIn_Type = Counter32
_LlcCcStatsIOctetsIn_Object = MibTableColumn
llcCcStatsIOctetsIn = _LlcCcStatsIOctetsIn_Object(
    (1, 3, 6, 1, 3, 51, 1, 3, 3, 1, 5),
    _LlcCcStatsIOctetsIn_Type()
)
llcCcStatsIOctetsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcStatsIOctetsIn.setStatus("mandatory")
_LlcCcStatsIOctetsOut_Type = Counter32
_LlcCcStatsIOctetsOut_Object = MibTableColumn
llcCcStatsIOctetsOut = _LlcCcStatsIOctetsOut_Object(
    (1, 3, 6, 1, 3, 51, 1, 3, 3, 1, 6),
    _LlcCcStatsIOctetsOut_Type()
)
llcCcStatsIOctetsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcStatsIOctetsOut.setStatus("mandatory")
_LlcCcStatsREJsIn_Type = Counter32
_LlcCcStatsREJsIn_Object = MibTableColumn
llcCcStatsREJsIn = _LlcCcStatsREJsIn_Object(
    (1, 3, 6, 1, 3, 51, 1, 3, 3, 1, 7),
    _LlcCcStatsREJsIn_Type()
)
llcCcStatsREJsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcStatsREJsIn.setStatus("mandatory")
_LlcCcStatsREJsOut_Type = Counter32
_LlcCcStatsREJsOut_Object = MibTableColumn
llcCcStatsREJsOut = _LlcCcStatsREJsOut_Object(
    (1, 3, 6, 1, 3, 51, 1, 3, 3, 1, 8),
    _LlcCcStatsREJsOut_Type()
)
llcCcStatsREJsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcStatsREJsOut.setStatus("mandatory")
_LlcCcStatsRetransmitsIn_Type = Counter32
_LlcCcStatsRetransmitsIn_Object = MibTableColumn
llcCcStatsRetransmitsIn = _LlcCcStatsRetransmitsIn_Object(
    (1, 3, 6, 1, 3, 51, 1, 3, 3, 1, 9),
    _LlcCcStatsRetransmitsIn_Type()
)
llcCcStatsRetransmitsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcStatsRetransmitsIn.setStatus("mandatory")
_LlcCcStatsRetransmitsOut_Type = Counter32
_LlcCcStatsRetransmitsOut_Object = MibTableColumn
llcCcStatsRetransmitsOut = _LlcCcStatsRetransmitsOut_Object(
    (1, 3, 6, 1, 3, 51, 1, 3, 3, 1, 10),
    _LlcCcStatsRetransmitsOut_Type()
)
llcCcStatsRetransmitsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcStatsRetransmitsOut.setStatus("mandatory")
_LlcCcStatsFRMRsIn_Type = Counter32
_LlcCcStatsFRMRsIn_Object = MibTableColumn
llcCcStatsFRMRsIn = _LlcCcStatsFRMRsIn_Object(
    (1, 3, 6, 1, 3, 51, 1, 3, 3, 1, 11),
    _LlcCcStatsFRMRsIn_Type()
)
llcCcStatsFRMRsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcStatsFRMRsIn.setStatus("mandatory")
_LlcCcStatsFRMRsOut_Type = Counter32
_LlcCcStatsFRMRsOut_Object = MibTableColumn
llcCcStatsFRMRsOut = _LlcCcStatsFRMRsOut_Object(
    (1, 3, 6, 1, 3, 51, 1, 3, 3, 1, 12),
    _LlcCcStatsFRMRsOut_Type()
)
llcCcStatsFRMRsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcStatsFRMRsOut.setStatus("mandatory")
_LlcCcStatsDISCsIn_Type = Counter32
_LlcCcStatsDISCsIn_Object = MibTableColumn
llcCcStatsDISCsIn = _LlcCcStatsDISCsIn_Object(
    (1, 3, 6, 1, 3, 51, 1, 3, 3, 1, 13),
    _LlcCcStatsDISCsIn_Type()
)
llcCcStatsDISCsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcStatsDISCsIn.setStatus("mandatory")
_LlcCcStatsDISCsOut_Type = Counter32
_LlcCcStatsDISCsOut_Object = MibTableColumn
llcCcStatsDISCsOut = _LlcCcStatsDISCsOut_Object(
    (1, 3, 6, 1, 3, 51, 1, 3, 3, 1, 14),
    _LlcCcStatsDISCsOut_Type()
)
llcCcStatsDISCsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcStatsDISCsOut.setStatus("mandatory")
_LlcCcStatsUAsIn_Type = Counter32
_LlcCcStatsUAsIn_Object = MibTableColumn
llcCcStatsUAsIn = _LlcCcStatsUAsIn_Object(
    (1, 3, 6, 1, 3, 51, 1, 3, 3, 1, 15),
    _LlcCcStatsUAsIn_Type()
)
llcCcStatsUAsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcStatsUAsIn.setStatus("mandatory")
_LlcCcStatsUAsOut_Type = Counter32
_LlcCcStatsUAsOut_Object = MibTableColumn
llcCcStatsUAsOut = _LlcCcStatsUAsOut_Object(
    (1, 3, 6, 1, 3, 51, 1, 3, 3, 1, 16),
    _LlcCcStatsUAsOut_Type()
)
llcCcStatsUAsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcStatsUAsOut.setStatus("mandatory")
_LlcCcStatsDMsIn_Type = Counter32
_LlcCcStatsDMsIn_Object = MibTableColumn
llcCcStatsDMsIn = _LlcCcStatsDMsIn_Object(
    (1, 3, 6, 1, 3, 51, 1, 3, 3, 1, 17),
    _LlcCcStatsDMsIn_Type()
)
llcCcStatsDMsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcStatsDMsIn.setStatus("mandatory")
_LlcCcStatsDMsOut_Type = Counter32
_LlcCcStatsDMsOut_Object = MibTableColumn
llcCcStatsDMsOut = _LlcCcStatsDMsOut_Object(
    (1, 3, 6, 1, 3, 51, 1, 3, 3, 1, 18),
    _LlcCcStatsDMsOut_Type()
)
llcCcStatsDMsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcStatsDMsOut.setStatus("mandatory")
_LlcCcStatsSABMEsIn_Type = Counter32
_LlcCcStatsSABMEsIn_Object = MibTableColumn
llcCcStatsSABMEsIn = _LlcCcStatsSABMEsIn_Object(
    (1, 3, 6, 1, 3, 51, 1, 3, 3, 1, 19),
    _LlcCcStatsSABMEsIn_Type()
)
llcCcStatsSABMEsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcStatsSABMEsIn.setStatus("mandatory")
_LlcCcStatsSABMEsOut_Type = Counter32
_LlcCcStatsSABMEsOut_Object = MibTableColumn
llcCcStatsSABMEsOut = _LlcCcStatsSABMEsOut_Object(
    (1, 3, 6, 1, 3, 51, 1, 3, 3, 1, 20),
    _LlcCcStatsSABMEsOut_Type()
)
llcCcStatsSABMEsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcStatsSABMEsOut.setStatus("mandatory")
_LlcCcStatsProtocolErrs_Type = Counter32
_LlcCcStatsProtocolErrs_Object = MibTableColumn
llcCcStatsProtocolErrs = _LlcCcStatsProtocolErrs_Object(
    (1, 3, 6, 1, 3, 51, 1, 3, 3, 1, 21),
    _LlcCcStatsProtocolErrs_Type()
)
llcCcStatsProtocolErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcStatsProtocolErrs.setStatus("mandatory")
_LlcCcStatsActivityTOs_Type = Counter32
_LlcCcStatsActivityTOs_Object = MibTableColumn
llcCcStatsActivityTOs = _LlcCcStatsActivityTOs_Object(
    (1, 3, 6, 1, 3, 51, 1, 3, 3, 1, 22),
    _LlcCcStatsActivityTOs_Type()
)
llcCcStatsActivityTOs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcStatsActivityTOs.setStatus("mandatory")
_LlcCcStatsRetriesExps_Type = Counter32
_LlcCcStatsRetriesExps_Object = MibTableColumn
llcCcStatsRetriesExps = _LlcCcStatsRetriesExps_Object(
    (1, 3, 6, 1, 3, 51, 1, 3, 3, 1, 23),
    _LlcCcStatsRetriesExps_Type()
)
llcCcStatsRetriesExps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcCcStatsRetriesExps.setStatus("mandatory")
_LlcTraps_ObjectIdentity = ObjectIdentity
llcTraps = _LlcTraps_ObjectIdentity(
    (1, 3, 6, 1, 3, 51, 1, 4)
)
_LlcConformance_ObjectIdentity = ObjectIdentity
llcConformance = _LlcConformance_ObjectIdentity(
    (1, 3, 6, 1, 3, 51, 1, 5)
)
_LlcCompliances_ObjectIdentity = ObjectIdentity
llcCompliances = _LlcCompliances_ObjectIdentity(
    (1, 3, 6, 1, 3, 51, 1, 5, 1)
)
_LlcCoreCompliance_ObjectIdentity = ObjectIdentity
llcCoreCompliance = _LlcCoreCompliance_ObjectIdentity(
    (1, 3, 6, 1, 3, 51, 1, 5, 1, 1)
)
_LlcGroups_ObjectIdentity = ObjectIdentity
llcGroups = _LlcGroups_ObjectIdentity(
    (1, 3, 6, 1, 3, 51, 1, 5, 2)
)
_LlcCoreGroups_ObjectIdentity = ObjectIdentity
llcCoreGroups = _LlcCoreGroups_ObjectIdentity(
    (1, 3, 6, 1, 3, 51, 1, 5, 2, 1)
)
_LlcCorePortAdminGroup_ObjectIdentity = ObjectIdentity
llcCorePortAdminGroup = _LlcCorePortAdminGroup_ObjectIdentity(
    (1, 3, 6, 1, 3, 51, 1, 5, 2, 1, 1)
)
_LlcCorePortOperGroup_ObjectIdentity = ObjectIdentity
llcCorePortOperGroup = _LlcCorePortOperGroup_ObjectIdentity(
    (1, 3, 6, 1, 3, 51, 1, 5, 2, 1, 2)
)
_LlcCorePortStatsGroup_ObjectIdentity = ObjectIdentity
llcCorePortStatsGroup = _LlcCorePortStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 3, 51, 1, 5, 2, 1, 3)
)
_LlcCoreCcAdminGroup_ObjectIdentity = ObjectIdentity
llcCoreCcAdminGroup = _LlcCoreCcAdminGroup_ObjectIdentity(
    (1, 3, 6, 1, 3, 51, 1, 5, 2, 1, 4)
)
_LlcCoreCcOperGroup_ObjectIdentity = ObjectIdentity
llcCoreCcOperGroup = _LlcCoreCcOperGroup_ObjectIdentity(
    (1, 3, 6, 1, 3, 51, 1, 5, 2, 1, 5)
)
_LlcCoreCcStatsGroup_ObjectIdentity = ObjectIdentity
llcCoreCcStatsGroup = _LlcCoreCcStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 3, 51, 1, 5, 2, 1, 6)
)

# Managed Objects groups


# Notification objects

llcPortStatusChange = NotificationType(
    (1, 3, 6, 1, 3, 51, 1, 4, 0, 1)
)
llcPortStatusChange.setObjects(
      *(("SNA-LLC-MIB", "llcPortOperLastFailTime"),
        ("SNA-LLC-MIB", "llcPortOperLastFailCause"))
)
if mibBuilder.loadTexts:
    llcPortStatusChange.setStatus(
        ""
    )

llcCcStatusChange = NotificationType(
    (1, 3, 6, 1, 3, 51, 1, 4, 0, 2)
)
llcCcStatusChange.setObjects(
      *(("SNA-LLC-MIB", "llcCcOperState"),
        ("SNA-LLC-MIB", "llcCcAdminState"),
        ("SNA-LLC-MIB", "llcCcOperLastFailTime"),
        ("SNA-LLC-MIB", "llcCcOperLastFailCause"),
        ("SNA-LLC-MIB", "llcCcOperLastFailFRMRInfo"))
)
if mibBuilder.loadTexts:
    llcCcStatusChange.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SNA-LLC-MIB",
    **{"snaDLCexp": snaDLCexp,
       "llc": llc,
       "llcPortGroup": llcPortGroup,
       "llcPortAdminTable": llcPortAdminTable,
       "llcPortAdminEntry": llcPortAdminEntry,
       "llcPortAdminName": llcPortAdminName,
       "llcPortAdminState": llcPortAdminState,
       "llcPortAdminMaxIPDUOctetsSend": llcPortAdminMaxIPDUOctetsSend,
       "llcPortAdminMaxIPDUOctetsRcv": llcPortAdminMaxIPDUOctetsRcv,
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
       "llcPortAdminSimRim": llcPortAdminSimRim,
       "llcPortOperTable": llcPortOperTable,
       "llcPortOperEntry": llcPortOperEntry,
       "llcPortOperName": llcPortOperName,
       "llcPortOperISTATUS": llcPortOperISTATUS,
       "llcPortOperLastModifyTime": llcPortOperLastModifyTime,
       "llcPortOperLastFailTime": llcPortOperLastFailTime,
       "llcPortOperLastFailCause": llcPortOperLastFailCause,
       "llcPortStatsTable": llcPortStatsTable,
       "llcPortStatsEntry": llcPortStatsEntry,
       "llcPortStatsPhysicalFailures": llcPortStatsPhysicalFailures,
       "llcPortStatsPollsIn": llcPortStatsPollsIn,
       "llcPortStatsPollsOut": llcPortStatsPollsOut,
       "llcPortStatsPollRspsIn": llcPortStatsPollRspsIn,
       "llcPortStatsPollRspsOut": llcPortStatsPollRspsOut,
       "llcPortStatsLocalBusies": llcPortStatsLocalBusies,
       "llcPortStatsRemoteBusies": llcPortStatsRemoteBusies,
       "llcPortStatsIFramesIn": llcPortStatsIFramesIn,
       "llcPortStatsIFramesOut": llcPortStatsIFramesOut,
       "llcPortStatsOctetsIn": llcPortStatsOctetsIn,
       "llcPortStatsOctetsOut": llcPortStatsOctetsOut,
       "llcPortStatsProtocolErrs": llcPortStatsProtocolErrs,
       "llcPortStatsActivityTOs": llcPortStatsActivityTOs,
       "llcPortStatsRetriesExps": llcPortStatsRetriesExps,
       "llcPortStatsRetransmitsIn": llcPortStatsRetransmitsIn,
       "llcPortStatsRetransmitsOut": llcPortStatsRetransmitsOut,
       "llcSapGroup": llcSapGroup,
       "llcSapAdminTable": llcSapAdminTable,
       "llcSapAdminEntry": llcSapAdminEntry,
       "llcSapNumber": llcSapNumber,
       "llcSapAdminState": llcSapAdminState,
       "llcSapAdminMaxIPDUOctetsSend": llcSapAdminMaxIPDUOctetsSend,
       "llcSapAdminMaxIPDUOctetsRcv": llcSapAdminMaxIPDUOctetsRcv,
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
       "llcSapOperTable": llcSapOperTable,
       "llcSapOperEntry": llcSapOperEntry,
       "llcSapOperStatus": llcSapOperStatus,
       "llcSapStatsTable": llcSapStatsTable,
       "llcSapStatsEntry": llcSapStatsEntry,
       "llcSapStatsTESTsIn": llcSapStatsTESTsIn,
       "llcSapStatsTESTsOut": llcSapStatsTESTsOut,
       "llcSapStatsXIDsIn": llcSapStatsXIDsIn,
       "llcSapStatsXIDsOut": llcSapStatsXIDsOut,
       "llcSapStatsUIFramesIn": llcSapStatsUIFramesIn,
       "llcSapStatsUIFramesOut": llcSapStatsUIFramesOut,
       "llcCcGroup": llcCcGroup,
       "llcCcAdminTable": llcCcAdminTable,
       "llcCcAdminEntry": llcCcAdminEntry,
       "llcCcLSap": llcCcLSap,
       "llcCcRSap": llcCcRSap,
       "llcCcLMac": llcCcLMac,
       "llcCcRMac": llcCcRMac,
       "llcCcAdminState": llcCcAdminState,
       "llcCcAdminMaxIPDUOctetsSend": llcCcAdminMaxIPDUOctetsSend,
       "llcCcAdminMaxIPDUOctetsRcv": llcCcAdminMaxIPDUOctetsRcv,
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
       "llcCcAdminRowStatus": llcCcAdminRowStatus,
       "llcCcOperTable": llcCcOperTable,
       "llcCcOperEntry": llcCcOperEntry,
       "llcCcOperRole": llcCcOperRole,
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
       "llcCcOperCreateTime": llcCcOperCreateTime,
       "llcCcOperLastModifyTime": llcCcOperLastModifyTime,
       "llcCcOperLastFailTime": llcCcOperLastFailTime,
       "llcCcOperLastFailCause": llcCcOperLastFailCause,
       "llcCcOperLastFailFRMRInfo": llcCcOperLastFailFRMRInfo,
       "llcCcStatsTable": llcCcStatsTable,
       "llcCcStatsEntry": llcCcStatsEntry,
       "llcCcStatsLocalBusies": llcCcStatsLocalBusies,
       "llcCcStatsRemoteBusies": llcCcStatsRemoteBusies,
       "llcCcStatsIFramesIn": llcCcStatsIFramesIn,
       "llcCcStatsIFramesOut": llcCcStatsIFramesOut,
       "llcCcStatsIOctetsIn": llcCcStatsIOctetsIn,
       "llcCcStatsIOctetsOut": llcCcStatsIOctetsOut,
       "llcCcStatsREJsIn": llcCcStatsREJsIn,
       "llcCcStatsREJsOut": llcCcStatsREJsOut,
       "llcCcStatsRetransmitsIn": llcCcStatsRetransmitsIn,
       "llcCcStatsRetransmitsOut": llcCcStatsRetransmitsOut,
       "llcCcStatsFRMRsIn": llcCcStatsFRMRsIn,
       "llcCcStatsFRMRsOut": llcCcStatsFRMRsOut,
       "llcCcStatsDISCsIn": llcCcStatsDISCsIn,
       "llcCcStatsDISCsOut": llcCcStatsDISCsOut,
       "llcCcStatsUAsIn": llcCcStatsUAsIn,
       "llcCcStatsUAsOut": llcCcStatsUAsOut,
       "llcCcStatsDMsIn": llcCcStatsDMsIn,
       "llcCcStatsDMsOut": llcCcStatsDMsOut,
       "llcCcStatsSABMEsIn": llcCcStatsSABMEsIn,
       "llcCcStatsSABMEsOut": llcCcStatsSABMEsOut,
       "llcCcStatsProtocolErrs": llcCcStatsProtocolErrs,
       "llcCcStatsActivityTOs": llcCcStatsActivityTOs,
       "llcCcStatsRetriesExps": llcCcStatsRetriesExps,
       "llcTraps": llcTraps,
       "llcPortStatusChange": llcPortStatusChange,
       "llcCcStatusChange": llcCcStatusChange,
       "llcConformance": llcConformance,
       "llcCompliances": llcCompliances,
       "llcCoreCompliance": llcCoreCompliance,
       "llcGroups": llcGroups,
       "llcCoreGroups": llcCoreGroups,
       "llcCorePortAdminGroup": llcCorePortAdminGroup,
       "llcCorePortOperGroup": llcCorePortOperGroup,
       "llcCorePortStatsGroup": llcCorePortStatsGroup,
       "llcCoreCcAdminGroup": llcCoreCcAdminGroup,
       "llcCoreCcOperGroup": llcCoreCcOperGroup,
       "llcCoreCcStatsGroup": llcCoreCcStatsGroup}
)
