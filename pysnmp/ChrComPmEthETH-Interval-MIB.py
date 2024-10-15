# SNMP MIB module (ChrComPmEthETH-Interval-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ChrComPmEthETH-Interval-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:22:15 2024
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

(chrComIfifIndex,) = mibBuilder.importSymbols(
    "ChrComIfifTable-MIB",
    "chrComIfifIndex")

(TruthValue,) = mibBuilder.importSymbols(
    "ChrTyp-MIB",
    "TruthValue")

(chrComPmEth,) = mibBuilder.importSymbols(
    "Chromatis-MIB",
    "chrComPmEth")

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

_ChrComPmEthETH_IntervalTable_Object = MibTable
chrComPmEthETH_IntervalTable = _ChrComPmEthETH_IntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 12)
)
if mibBuilder.loadTexts:
    chrComPmEthETH_IntervalTable.setStatus("current")
_ChrComPmEthETH_IntervalEntry_Object = MibTableRow
chrComPmEthETH_IntervalEntry = _ChrComPmEthETH_IntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 12, 1)
)
chrComPmEthETH_IntervalEntry.setIndexNames(
    (0, "ChrComIfifTable-MIB", "chrComIfifIndex"),
    (0, "ChrComPmEthETH-Interval-MIB", "chrComPmEthIntervalNumber"),
)
if mibBuilder.loadTexts:
    chrComPmEthETH_IntervalEntry.setStatus("current")


class _ChrComPmEthIntervalNumber_Type(Unsigned32):
    """Custom type chrComPmEthIntervalNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_ChrComPmEthIntervalNumber_Type.__name__ = "Unsigned32"
_ChrComPmEthIntervalNumber_Object = MibTableColumn
chrComPmEthIntervalNumber = _ChrComPmEthIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 12, 1, 1),
    _ChrComPmEthIntervalNumber_Type()
)
chrComPmEthIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmEthIntervalNumber.setStatus("current")
_ChrComPmEthSuspectedInterval_Type = TruthValue
_ChrComPmEthSuspectedInterval_Object = MibTableColumn
chrComPmEthSuspectedInterval = _ChrComPmEthSuspectedInterval_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 12, 1, 2),
    _ChrComPmEthSuspectedInterval_Type()
)
chrComPmEthSuspectedInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmEthSuspectedInterval.setStatus("current")


class _ChrComPmEthElapsedTime_Type(Unsigned32):
    """Custom type chrComPmEthElapsedTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmEthElapsedTime_Type.__name__ = "Unsigned32"
_ChrComPmEthElapsedTime_Object = MibTableColumn
chrComPmEthElapsedTime = _ChrComPmEthElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 12, 1, 3),
    _ChrComPmEthElapsedTime_Type()
)
chrComPmEthElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmEthElapsedTime.setStatus("current")


class _ChrComPmEthSuppressedIntrvls_Type(Gauge32):
    """Custom type chrComPmEthSuppressedIntrvls based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmEthSuppressedIntrvls_Type.__name__ = "Gauge32"
_ChrComPmEthSuppressedIntrvls_Object = MibTableColumn
chrComPmEthSuppressedIntrvls = _ChrComPmEthSuppressedIntrvls_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 12, 1, 4),
    _ChrComPmEthSuppressedIntrvls_Type()
)
chrComPmEthSuppressedIntrvls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmEthSuppressedIntrvls.setStatus("current")


class _ChrComPmEthdot3StatsFCSErrors_Type(Gauge32):
    """Custom type chrComPmEthdot3StatsFCSErrors based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmEthdot3StatsFCSErrors_Type.__name__ = "Gauge32"
_ChrComPmEthdot3StatsFCSErrors_Object = MibTableColumn
chrComPmEthdot3StatsFCSErrors = _ChrComPmEthdot3StatsFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 12, 1, 5),
    _ChrComPmEthdot3StatsFCSErrors_Type()
)
chrComPmEthdot3StatsFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmEthdot3StatsFCSErrors.setStatus("current")


class _ChrComPmEthdot3StatsLateCollisions_Type(Gauge32):
    """Custom type chrComPmEthdot3StatsLateCollisions based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmEthdot3StatsLateCollisions_Type.__name__ = "Gauge32"
_ChrComPmEthdot3StatsLateCollisions_Object = MibTableColumn
chrComPmEthdot3StatsLateCollisions = _ChrComPmEthdot3StatsLateCollisions_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 12, 1, 6),
    _ChrComPmEthdot3StatsLateCollisions_Type()
)
chrComPmEthdot3StatsLateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmEthdot3StatsLateCollisions.setStatus("current")


class _ChrComPmEthdot3StatsFrameTooLongs_Type(Gauge32):
    """Custom type chrComPmEthdot3StatsFrameTooLongs based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmEthdot3StatsFrameTooLongs_Type.__name__ = "Gauge32"
_ChrComPmEthdot3StatsFrameTooLongs_Object = MibTableColumn
chrComPmEthdot3StatsFrameTooLongs = _ChrComPmEthdot3StatsFrameTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 12, 1, 7),
    _ChrComPmEthdot3StatsFrameTooLongs_Type()
)
chrComPmEthdot3StatsFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmEthdot3StatsFrameTooLongs.setStatus("current")


class _ChrComPmEthdot3StatsInternalMacReceiveErrors_Type(Gauge32):
    """Custom type chrComPmEthdot3StatsInternalMacReceiveErrors based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmEthdot3StatsInternalMacReceiveErrors_Type.__name__ = "Gauge32"
_ChrComPmEthdot3StatsInternalMacReceiveErrors_Object = MibTableColumn
chrComPmEthdot3StatsInternalMacReceiveErrors = _ChrComPmEthdot3StatsInternalMacReceiveErrors_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 12, 1, 8),
    _ChrComPmEthdot3StatsInternalMacReceiveErrors_Type()
)
chrComPmEthdot3StatsInternalMacReceiveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmEthdot3StatsInternalMacReceiveErrors.setStatus("current")


class _ChrComPmEthifInOctets_Type(Gauge32):
    """Custom type chrComPmEthifInOctets based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmEthifInOctets_Type.__name__ = "Gauge32"
_ChrComPmEthifInOctets_Object = MibTableColumn
chrComPmEthifInOctets = _ChrComPmEthifInOctets_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 12, 1, 9),
    _ChrComPmEthifInOctets_Type()
)
chrComPmEthifInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmEthifInOctets.setStatus("current")


class _ChrComPmEthifInUcastPkts_Type(Gauge32):
    """Custom type chrComPmEthifInUcastPkts based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmEthifInUcastPkts_Type.__name__ = "Gauge32"
_ChrComPmEthifInUcastPkts_Object = MibTableColumn
chrComPmEthifInUcastPkts = _ChrComPmEthifInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 12, 1, 10),
    _ChrComPmEthifInUcastPkts_Type()
)
chrComPmEthifInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmEthifInUcastPkts.setStatus("current")


class _ChrComPmEthifInDiscards_Type(Gauge32):
    """Custom type chrComPmEthifInDiscards based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmEthifInDiscards_Type.__name__ = "Gauge32"
_ChrComPmEthifInDiscards_Object = MibTableColumn
chrComPmEthifInDiscards = _ChrComPmEthifInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 12, 1, 11),
    _ChrComPmEthifInDiscards_Type()
)
chrComPmEthifInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmEthifInDiscards.setStatus("current")


class _ChrComPmEthifInErrors_Type(Gauge32):
    """Custom type chrComPmEthifInErrors based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmEthifInErrors_Type.__name__ = "Gauge32"
_ChrComPmEthifInErrors_Object = MibTableColumn
chrComPmEthifInErrors = _ChrComPmEthifInErrors_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 12, 1, 12),
    _ChrComPmEthifInErrors_Type()
)
chrComPmEthifInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmEthifInErrors.setStatus("current")


class _ChrComPmEthifOutOctets_Type(Gauge32):
    """Custom type chrComPmEthifOutOctets based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmEthifOutOctets_Type.__name__ = "Gauge32"
_ChrComPmEthifOutOctets_Object = MibTableColumn
chrComPmEthifOutOctets = _ChrComPmEthifOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 12, 1, 13),
    _ChrComPmEthifOutOctets_Type()
)
chrComPmEthifOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmEthifOutOctets.setStatus("current")


class _ChrComPmEthifOutUcastPkts_Type(Gauge32):
    """Custom type chrComPmEthifOutUcastPkts based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmEthifOutUcastPkts_Type.__name__ = "Gauge32"
_ChrComPmEthifOutUcastPkts_Object = MibTableColumn
chrComPmEthifOutUcastPkts = _ChrComPmEthifOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 12, 1, 14),
    _ChrComPmEthifOutUcastPkts_Type()
)
chrComPmEthifOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmEthifOutUcastPkts.setStatus("current")


class _ChrComPmEthifInMulticastPkts_Type(Gauge32):
    """Custom type chrComPmEthifInMulticastPkts based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmEthifInMulticastPkts_Type.__name__ = "Gauge32"
_ChrComPmEthifInMulticastPkts_Object = MibTableColumn
chrComPmEthifInMulticastPkts = _ChrComPmEthifInMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 12, 1, 15),
    _ChrComPmEthifInMulticastPkts_Type()
)
chrComPmEthifInMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmEthifInMulticastPkts.setStatus("current")


class _ChrComPmEthifInBroadcastPkts_Type(Gauge32):
    """Custom type chrComPmEthifInBroadcastPkts based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmEthifInBroadcastPkts_Type.__name__ = "Gauge32"
_ChrComPmEthifInBroadcastPkts_Object = MibTableColumn
chrComPmEthifInBroadcastPkts = _ChrComPmEthifInBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 12, 1, 16),
    _ChrComPmEthifInBroadcastPkts_Type()
)
chrComPmEthifInBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmEthifInBroadcastPkts.setStatus("current")


class _ChrComPmEthifOutMulticastPkts_Type(Gauge32):
    """Custom type chrComPmEthifOutMulticastPkts based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmEthifOutMulticastPkts_Type.__name__ = "Gauge32"
_ChrComPmEthifOutMulticastPkts_Object = MibTableColumn
chrComPmEthifOutMulticastPkts = _ChrComPmEthifOutMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 12, 1, 17),
    _ChrComPmEthifOutMulticastPkts_Type()
)
chrComPmEthifOutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmEthifOutMulticastPkts.setStatus("current")


class _ChrComPmEthifOutBroadcastPkts_Type(Gauge32):
    """Custom type chrComPmEthifOutBroadcastPkts based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmEthifOutBroadcastPkts_Type.__name__ = "Gauge32"
_ChrComPmEthifOutBroadcastPkts_Object = MibTableColumn
chrComPmEthifOutBroadcastPkts = _ChrComPmEthifOutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 12, 1, 18),
    _ChrComPmEthifOutBroadcastPkts_Type()
)
chrComPmEthifOutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmEthifOutBroadcastPkts.setStatus("current")


class _ChrComPmEthchrFrames64Bytes_Type(Gauge32):
    """Custom type chrComPmEthchrFrames64Bytes based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmEthchrFrames64Bytes_Type.__name__ = "Gauge32"
_ChrComPmEthchrFrames64Bytes_Object = MibTableColumn
chrComPmEthchrFrames64Bytes = _ChrComPmEthchrFrames64Bytes_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 12, 1, 19),
    _ChrComPmEthchrFrames64Bytes_Type()
)
chrComPmEthchrFrames64Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmEthchrFrames64Bytes.setStatus("current")


class _ChrComPmEthchrFrames65to127Bytes_Type(Gauge32):
    """Custom type chrComPmEthchrFrames65to127Bytes based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmEthchrFrames65to127Bytes_Type.__name__ = "Gauge32"
_ChrComPmEthchrFrames65to127Bytes_Object = MibTableColumn
chrComPmEthchrFrames65to127Bytes = _ChrComPmEthchrFrames65to127Bytes_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 12, 1, 20),
    _ChrComPmEthchrFrames65to127Bytes_Type()
)
chrComPmEthchrFrames65to127Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmEthchrFrames65to127Bytes.setStatus("current")


class _ChrComPmEthchrFrames128to256Bytes_Type(Gauge32):
    """Custom type chrComPmEthchrFrames128to256Bytes based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmEthchrFrames128to256Bytes_Type.__name__ = "Gauge32"
_ChrComPmEthchrFrames128to256Bytes_Object = MibTableColumn
chrComPmEthchrFrames128to256Bytes = _ChrComPmEthchrFrames128to256Bytes_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 12, 1, 21),
    _ChrComPmEthchrFrames128to256Bytes_Type()
)
chrComPmEthchrFrames128to256Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmEthchrFrames128to256Bytes.setStatus("current")


class _ChrComPmEthchrFrames257to512Bytes_Type(Gauge32):
    """Custom type chrComPmEthchrFrames257to512Bytes based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmEthchrFrames257to512Bytes_Type.__name__ = "Gauge32"
_ChrComPmEthchrFrames257to512Bytes_Object = MibTableColumn
chrComPmEthchrFrames257to512Bytes = _ChrComPmEthchrFrames257to512Bytes_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 12, 1, 22),
    _ChrComPmEthchrFrames257to512Bytes_Type()
)
chrComPmEthchrFrames257to512Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmEthchrFrames257to512Bytes.setStatus("current")


class _ChrComPmEthchrFrames513to1024Bytes_Type(Gauge32):
    """Custom type chrComPmEthchrFrames513to1024Bytes based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmEthchrFrames513to1024Bytes_Type.__name__ = "Gauge32"
_ChrComPmEthchrFrames513to1024Bytes_Object = MibTableColumn
chrComPmEthchrFrames513to1024Bytes = _ChrComPmEthchrFrames513to1024Bytes_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 12, 1, 23),
    _ChrComPmEthchrFrames513to1024Bytes_Type()
)
chrComPmEthchrFrames513to1024Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmEthchrFrames513to1024Bytes.setStatus("current")


class _ChrComPmEthchrFrames1024toMaxBytes_Type(Gauge32):
    """Custom type chrComPmEthchrFrames1024toMaxBytes based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ChrComPmEthchrFrames1024toMaxBytes_Type.__name__ = "Gauge32"
_ChrComPmEthchrFrames1024toMaxBytes_Object = MibTableColumn
chrComPmEthchrFrames1024toMaxBytes = _ChrComPmEthchrFrames1024toMaxBytes_Object(
    (1, 3, 6, 1, 4, 1, 3695, 1, 10, 5, 12, 1, 24),
    _ChrComPmEthchrFrames1024toMaxBytes_Type()
)
chrComPmEthchrFrames1024toMaxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chrComPmEthchrFrames1024toMaxBytes.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ChrComPmEthETH-Interval-MIB",
    **{"chrComPmEthETH-IntervalTable": chrComPmEthETH_IntervalTable,
       "chrComPmEthETH-IntervalEntry": chrComPmEthETH_IntervalEntry,
       "chrComPmEthIntervalNumber": chrComPmEthIntervalNumber,
       "chrComPmEthSuspectedInterval": chrComPmEthSuspectedInterval,
       "chrComPmEthElapsedTime": chrComPmEthElapsedTime,
       "chrComPmEthSuppressedIntrvls": chrComPmEthSuppressedIntrvls,
       "chrComPmEthdot3StatsFCSErrors": chrComPmEthdot3StatsFCSErrors,
       "chrComPmEthdot3StatsLateCollisions": chrComPmEthdot3StatsLateCollisions,
       "chrComPmEthdot3StatsFrameTooLongs": chrComPmEthdot3StatsFrameTooLongs,
       "chrComPmEthdot3StatsInternalMacReceiveErrors": chrComPmEthdot3StatsInternalMacReceiveErrors,
       "chrComPmEthifInOctets": chrComPmEthifInOctets,
       "chrComPmEthifInUcastPkts": chrComPmEthifInUcastPkts,
       "chrComPmEthifInDiscards": chrComPmEthifInDiscards,
       "chrComPmEthifInErrors": chrComPmEthifInErrors,
       "chrComPmEthifOutOctets": chrComPmEthifOutOctets,
       "chrComPmEthifOutUcastPkts": chrComPmEthifOutUcastPkts,
       "chrComPmEthifInMulticastPkts": chrComPmEthifInMulticastPkts,
       "chrComPmEthifInBroadcastPkts": chrComPmEthifInBroadcastPkts,
       "chrComPmEthifOutMulticastPkts": chrComPmEthifOutMulticastPkts,
       "chrComPmEthifOutBroadcastPkts": chrComPmEthifOutBroadcastPkts,
       "chrComPmEthchrFrames64Bytes": chrComPmEthchrFrames64Bytes,
       "chrComPmEthchrFrames65to127Bytes": chrComPmEthchrFrames65to127Bytes,
       "chrComPmEthchrFrames128to256Bytes": chrComPmEthchrFrames128to256Bytes,
       "chrComPmEthchrFrames257to512Bytes": chrComPmEthchrFrames257to512Bytes,
       "chrComPmEthchrFrames513to1024Bytes": chrComPmEthchrFrames513to1024Bytes,
       "chrComPmEthchrFrames1024toMaxBytes": chrComPmEthchrFrames1024toMaxBytes}
)
