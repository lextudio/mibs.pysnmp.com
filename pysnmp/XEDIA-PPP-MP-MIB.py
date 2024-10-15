# SNMP MIB module (XEDIA-PPP-MP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XEDIA-PPP-MP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:18:02 2024
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

(xediaMibs,) = mibBuilder.importSymbols(
    "XEDIA-REG",
    "xediaMibs")


# MODULE-IDENTITY

xediaPppMpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 21)
)


# Types definitions



class Unsigned32(Gauge32):
    """Custom type Unsigned32 based on Gauge32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XediaPppMpObjects_ObjectIdentity = ObjectIdentity
xediaPppMpObjects = _XediaPppMpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 21, 1)
)
_MpBundle_ObjectIdentity = ObjectIdentity
mpBundle = _MpBundle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1)
)
_MpBundleStatusTable_Object = MibTable
mpBundleStatusTable = _MpBundleStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 1)
)
if mibBuilder.loadTexts:
    mpBundleStatusTable.setStatus("current")
_MpBundleStatusEntry_Object = MibTableRow
mpBundleStatusEntry = _MpBundleStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 1, 1)
)
mpBundleStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    mpBundleStatusEntry.setStatus("current")
_MpBundleStatusPacketTooLongs_Type = Counter32
_MpBundleStatusPacketTooLongs_Object = MibTableColumn
mpBundleStatusPacketTooLongs = _MpBundleStatusPacketTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 1, 1, 1),
    _MpBundleStatusPacketTooLongs_Type()
)
mpBundleStatusPacketTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpBundleStatusPacketTooLongs.setStatus("current")


class _MpBundleStatusLocalMRRU_Type(Unsigned32):
    """Custom type mpBundleStatusLocalMRRU based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MpBundleStatusLocalMRRU_Type.__name__ = "Unsigned32"
_MpBundleStatusLocalMRRU_Object = MibTableColumn
mpBundleStatusLocalMRRU = _MpBundleStatusLocalMRRU_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 1, 1, 2),
    _MpBundleStatusLocalMRRU_Type()
)
mpBundleStatusLocalMRRU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpBundleStatusLocalMRRU.setStatus("current")


class _MpBundleStatusRemoteMRRU_Type(Unsigned32):
    """Custom type mpBundleStatusRemoteMRRU based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MpBundleStatusRemoteMRRU_Type.__name__ = "Unsigned32"
_MpBundleStatusRemoteMRRU_Object = MibTableColumn
mpBundleStatusRemoteMRRU = _MpBundleStatusRemoteMRRU_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 1, 1, 3),
    _MpBundleStatusRemoteMRRU_Type()
)
mpBundleStatusRemoteMRRU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpBundleStatusRemoteMRRU.setStatus("current")


class _MpBundleStatusLocalEndptDiscr_Type(OctetString):
    """Custom type mpBundleStatusLocalEndptDiscr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(21, 21),
    )


_MpBundleStatusLocalEndptDiscr_Type.__name__ = "OctetString"
_MpBundleStatusLocalEndptDiscr_Object = MibTableColumn
mpBundleStatusLocalEndptDiscr = _MpBundleStatusLocalEndptDiscr_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 1, 1, 4),
    _MpBundleStatusLocalEndptDiscr_Type()
)
mpBundleStatusLocalEndptDiscr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpBundleStatusLocalEndptDiscr.setStatus("current")


class _MpBundleStatusRemoteEndptDiscr_Type(OctetString):
    """Custom type mpBundleStatusRemoteEndptDiscr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_MpBundleStatusRemoteEndptDiscr_Type.__name__ = "OctetString"
_MpBundleStatusRemoteEndptDiscr_Object = MibTableColumn
mpBundleStatusRemoteEndptDiscr = _MpBundleStatusRemoteEndptDiscr_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 1, 1, 5),
    _MpBundleStatusRemoteEndptDiscr_Type()
)
mpBundleStatusRemoteEndptDiscr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpBundleStatusRemoteEndptDiscr.setStatus("current")


class _MpBundleStatusRcvShortSeq_Type(Integer32):
    """Custom type mpBundleStatusRcvShortSeq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_MpBundleStatusRcvShortSeq_Type.__name__ = "Integer32"
_MpBundleStatusRcvShortSeq_Object = MibTableColumn
mpBundleStatusRcvShortSeq = _MpBundleStatusRcvShortSeq_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 1, 1, 6),
    _MpBundleStatusRcvShortSeq_Type()
)
mpBundleStatusRcvShortSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpBundleStatusRcvShortSeq.setStatus("current")


class _MpBundleStatusXmtShortSeq_Type(Integer32):
    """Custom type mpBundleStatusXmtShortSeq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_MpBundleStatusXmtShortSeq_Type.__name__ = "Integer32"
_MpBundleStatusXmtShortSeq_Object = MibTableColumn
mpBundleStatusXmtShortSeq = _MpBundleStatusXmtShortSeq_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 1, 1, 7),
    _MpBundleStatusXmtShortSeq_Type()
)
mpBundleStatusXmtShortSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpBundleStatusXmtShortSeq.setStatus("current")


class _MpBundleStatusSmallPktMaxSize_Type(Unsigned32):
    """Custom type mpBundleStatusSmallPktMaxSize based on Unsigned32"""
    defaultValue = 12

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MpBundleStatusSmallPktMaxSize_Type.__name__ = "Unsigned32"
_MpBundleStatusSmallPktMaxSize_Object = MibTableColumn
mpBundleStatusSmallPktMaxSize = _MpBundleStatusSmallPktMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 1, 1, 8),
    _MpBundleStatusSmallPktMaxSize_Type()
)
mpBundleStatusSmallPktMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpBundleStatusSmallPktMaxSize.setStatus("current")


class _MpBundleStatusMediumPktMaxSize_Type(Unsigned32):
    """Custom type mpBundleStatusMediumPktMaxSize based on Unsigned32"""
    defaultValue = 64

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MpBundleStatusMediumPktMaxSize_Type.__name__ = "Unsigned32"
_MpBundleStatusMediumPktMaxSize_Object = MibTableColumn
mpBundleStatusMediumPktMaxSize = _MpBundleStatusMediumPktMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 1, 1, 9),
    _MpBundleStatusMediumPktMaxSize_Type()
)
mpBundleStatusMediumPktMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpBundleStatusMediumPktMaxSize.setStatus("current")
_MpBundleStatusSingleFragsRcvd_Type = Counter32
_MpBundleStatusSingleFragsRcvd_Object = MibTableColumn
mpBundleStatusSingleFragsRcvd = _MpBundleStatusSingleFragsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 1, 1, 10),
    _MpBundleStatusSingleFragsRcvd_Type()
)
mpBundleStatusSingleFragsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpBundleStatusSingleFragsRcvd.setStatus("current")
_MpBundleStatusReasmReqds_Type = Counter32
_MpBundleStatusReasmReqds_Object = MibTableColumn
mpBundleStatusReasmReqds = _MpBundleStatusReasmReqds_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 1, 1, 11),
    _MpBundleStatusReasmReqds_Type()
)
mpBundleStatusReasmReqds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpBundleStatusReasmReqds.setStatus("current")
_MpBundleStatusReasmFails_Type = Counter32
_MpBundleStatusReasmFails_Object = MibTableColumn
mpBundleStatusReasmFails = _MpBundleStatusReasmFails_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 1, 1, 12),
    _MpBundleStatusReasmFails_Type()
)
mpBundleStatusReasmFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpBundleStatusReasmFails.setStatus("current")
_MpBundleStatusReasmOks_Type = Counter32
_MpBundleStatusReasmOks_Object = MibTableColumn
mpBundleStatusReasmOks = _MpBundleStatusReasmOks_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 1, 1, 13),
    _MpBundleStatusReasmOks_Type()
)
mpBundleStatusReasmOks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpBundleStatusReasmOks.setStatus("current")
_MpBundleStatusRcvdFragsDiscarded_Type = Counter32
_MpBundleStatusRcvdFragsDiscarded_Object = MibTableColumn
mpBundleStatusRcvdFragsDiscarded = _MpBundleStatusRcvdFragsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 1, 1, 14),
    _MpBundleStatusRcvdFragsDiscarded_Type()
)
mpBundleStatusRcvdFragsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpBundleStatusRcvdFragsDiscarded.setStatus("current")
_MpBundleStatusDropTooManyFrags_Type = Counter32
_MpBundleStatusDropTooManyFrags_Object = MibTableColumn
mpBundleStatusDropTooManyFrags = _MpBundleStatusDropTooManyFrags_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 1, 1, 15),
    _MpBundleStatusDropTooManyFrags_Type()
)
mpBundleStatusDropTooManyFrags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpBundleStatusDropTooManyFrags.setStatus("current")
_MpBundleStatusSingleFragsSent_Type = Counter32
_MpBundleStatusSingleFragsSent_Object = MibTableColumn
mpBundleStatusSingleFragsSent = _MpBundleStatusSingleFragsSent_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 1, 1, 16),
    _MpBundleStatusSingleFragsSent_Type()
)
mpBundleStatusSingleFragsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpBundleStatusSingleFragsSent.setStatus("current")
_MpBundleStatusFragCreates_Type = Counter32
_MpBundleStatusFragCreates_Object = MibTableColumn
mpBundleStatusFragCreates = _MpBundleStatusFragCreates_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 1, 1, 17),
    _MpBundleStatusFragCreates_Type()
)
mpBundleStatusFragCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpBundleStatusFragCreates.setStatus("current")
_MpBundleStatusFragFails_Type = Counter32
_MpBundleStatusFragFails_Object = MibTableColumn
mpBundleStatusFragFails = _MpBundleStatusFragFails_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 1, 1, 18),
    _MpBundleStatusFragFails_Type()
)
mpBundleStatusFragFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpBundleStatusFragFails.setStatus("current")
_MpBundleStatusFragOks_Type = Counter32
_MpBundleStatusFragOks_Object = MibTableColumn
mpBundleStatusFragOks = _MpBundleStatusFragOks_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 1, 1, 19),
    _MpBundleStatusFragOks_Type()
)
mpBundleStatusFragOks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpBundleStatusFragOks.setStatus("current")
_MpBundleStatusRcvdFragsBuffered_Type = Counter32
_MpBundleStatusRcvdFragsBuffered_Object = MibTableColumn
mpBundleStatusRcvdFragsBuffered = _MpBundleStatusRcvdFragsBuffered_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 1, 1, 20),
    _MpBundleStatusRcvdFragsBuffered_Type()
)
mpBundleStatusRcvdFragsBuffered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpBundleStatusRcvdFragsBuffered.setStatus("current")
_MpBundleConfigTable_Object = MibTable
mpBundleConfigTable = _MpBundleConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 2)
)
if mibBuilder.loadTexts:
    mpBundleConfigTable.setStatus("current")
_MpBundleConfigEntry_Object = MibTableRow
mpBundleConfigEntry = _MpBundleConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 2, 1)
)
mpBundleConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    mpBundleConfigEntry.setStatus("current")


class _MpBundleConfigLocalMRRU_Type(Unsigned32):
    """Custom type mpBundleConfigLocalMRRU based on Unsigned32"""
    defaultValue = 1600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MpBundleConfigLocalMRRU_Type.__name__ = "Unsigned32"
_MpBundleConfigLocalMRRU_Object = MibTableColumn
mpBundleConfigLocalMRRU = _MpBundleConfigLocalMRRU_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 2, 1, 1),
    _MpBundleConfigLocalMRRU_Type()
)
mpBundleConfigLocalMRRU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpBundleConfigLocalMRRU.setStatus("current")


class _MpBundleConfigLocalEndptDiscr_Type(OctetString):
    """Custom type mpBundleConfigLocalEndptDiscr based on OctetString"""
    defaultHexValue = "0"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 21),
    )


_MpBundleConfigLocalEndptDiscr_Type.__name__ = "OctetString"
_MpBundleConfigLocalEndptDiscr_Object = MibTableColumn
mpBundleConfigLocalEndptDiscr = _MpBundleConfigLocalEndptDiscr_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 2, 1, 2),
    _MpBundleConfigLocalEndptDiscr_Type()
)
mpBundleConfigLocalEndptDiscr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpBundleConfigLocalEndptDiscr.setStatus("current")


class _MpBundleConfigRcvShortSeq_Type(Integer32):
    """Custom type mpBundleConfigRcvShortSeq based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_MpBundleConfigRcvShortSeq_Type.__name__ = "Integer32"
_MpBundleConfigRcvShortSeq_Object = MibTableColumn
mpBundleConfigRcvShortSeq = _MpBundleConfigRcvShortSeq_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 2, 1, 3),
    _MpBundleConfigRcvShortSeq_Type()
)
mpBundleConfigRcvShortSeq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpBundleConfigRcvShortSeq.setStatus("current")


class _MpBundleConfigSmallPktMaxSize_Type(Unsigned32):
    """Custom type mpBundleConfigSmallPktMaxSize based on Unsigned32"""
    defaultValue = 12

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MpBundleConfigSmallPktMaxSize_Type.__name__ = "Unsigned32"
_MpBundleConfigSmallPktMaxSize_Object = MibTableColumn
mpBundleConfigSmallPktMaxSize = _MpBundleConfigSmallPktMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 2, 1, 4),
    _MpBundleConfigSmallPktMaxSize_Type()
)
mpBundleConfigSmallPktMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpBundleConfigSmallPktMaxSize.setStatus("current")


class _MpBundleConfigMediumPktMaxSize_Type(Unsigned32):
    """Custom type mpBundleConfigMediumPktMaxSize based on Unsigned32"""
    defaultValue = 64

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MpBundleConfigMediumPktMaxSize_Type.__name__ = "Unsigned32"
_MpBundleConfigMediumPktMaxSize_Object = MibTableColumn
mpBundleConfigMediumPktMaxSize = _MpBundleConfigMediumPktMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 838, 3, 21, 1, 1, 2, 1, 5),
    _MpBundleConfigMediumPktMaxSize_Type()
)
mpBundleConfigMediumPktMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpBundleConfigMediumPktMaxSize.setStatus("current")
_XediaPppMpConformance_ObjectIdentity = ObjectIdentity
xediaPppMpConformance = _XediaPppMpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 21, 2)
)
_MpCompliances_ObjectIdentity = ObjectIdentity
mpCompliances = _MpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 21, 2, 1)
)
_MpGroups_ObjectIdentity = ObjectIdentity
mpGroups = _MpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3, 21, 2, 2)
)

# Managed Objects groups

mpAllGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 838, 3, 21, 2, 2, 1)
)
mpAllGroup.setObjects(
      *(("XEDIA-PPP-MP-MIB", "mpBundleStatusPacketTooLongs"),
        ("XEDIA-PPP-MP-MIB", "mpBundleStatusLocalMRRU"),
        ("XEDIA-PPP-MP-MIB", "mpBundleStatusRemoteMRRU"),
        ("XEDIA-PPP-MP-MIB", "mpBundleStatusLocalEndptDiscr"),
        ("XEDIA-PPP-MP-MIB", "mpBundleStatusRemoteEndptDiscr"),
        ("XEDIA-PPP-MP-MIB", "mpBundleStatusRcvShortSeq"),
        ("XEDIA-PPP-MP-MIB", "mpBundleStatusXmtShortSeq"),
        ("XEDIA-PPP-MP-MIB", "mpBundleStatusSmallPktMaxSize"),
        ("XEDIA-PPP-MP-MIB", "mpBundleStatusMediumPktMaxSize"),
        ("XEDIA-PPP-MP-MIB", "mpBundleStatusSingleFragsRcvd"),
        ("XEDIA-PPP-MP-MIB", "mpBundleStatusReasmReqds"),
        ("XEDIA-PPP-MP-MIB", "mpBundleStatusReasmFails"),
        ("XEDIA-PPP-MP-MIB", "mpBundleStatusReasmOks"),
        ("XEDIA-PPP-MP-MIB", "mpBundleStatusRcvdFragsDiscarded"),
        ("XEDIA-PPP-MP-MIB", "mpBundleStatusDropTooManyFrags"),
        ("XEDIA-PPP-MP-MIB", "mpBundleStatusSingleFragsSent"),
        ("XEDIA-PPP-MP-MIB", "mpBundleStatusFragCreates"),
        ("XEDIA-PPP-MP-MIB", "mpBundleStatusFragFails"),
        ("XEDIA-PPP-MP-MIB", "mpBundleStatusFragOks"),
        ("XEDIA-PPP-MP-MIB", "mpBundleStatusRcvdFragsBuffered"),
        ("XEDIA-PPP-MP-MIB", "mpBundleConfigLocalMRRU"),
        ("XEDIA-PPP-MP-MIB", "mpBundleConfigLocalEndptDiscr"),
        ("XEDIA-PPP-MP-MIB", "mpBundleConfigRcvShortSeq"),
        ("XEDIA-PPP-MP-MIB", "mpBundleConfigSmallPktMaxSize"),
        ("XEDIA-PPP-MP-MIB", "mpBundleConfigMediumPktMaxSize"))
)
if mibBuilder.loadTexts:
    mpAllGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

mpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 838, 3, 21, 2, 1, 1)
)
if mibBuilder.loadTexts:
    mpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XEDIA-PPP-MP-MIB",
    **{"Unsigned32": Unsigned32,
       "xediaPppMpMIB": xediaPppMpMIB,
       "xediaPppMpObjects": xediaPppMpObjects,
       "mpBundle": mpBundle,
       "mpBundleStatusTable": mpBundleStatusTable,
       "mpBundleStatusEntry": mpBundleStatusEntry,
       "mpBundleStatusPacketTooLongs": mpBundleStatusPacketTooLongs,
       "mpBundleStatusLocalMRRU": mpBundleStatusLocalMRRU,
       "mpBundleStatusRemoteMRRU": mpBundleStatusRemoteMRRU,
       "mpBundleStatusLocalEndptDiscr": mpBundleStatusLocalEndptDiscr,
       "mpBundleStatusRemoteEndptDiscr": mpBundleStatusRemoteEndptDiscr,
       "mpBundleStatusRcvShortSeq": mpBundleStatusRcvShortSeq,
       "mpBundleStatusXmtShortSeq": mpBundleStatusXmtShortSeq,
       "mpBundleStatusSmallPktMaxSize": mpBundleStatusSmallPktMaxSize,
       "mpBundleStatusMediumPktMaxSize": mpBundleStatusMediumPktMaxSize,
       "mpBundleStatusSingleFragsRcvd": mpBundleStatusSingleFragsRcvd,
       "mpBundleStatusReasmReqds": mpBundleStatusReasmReqds,
       "mpBundleStatusReasmFails": mpBundleStatusReasmFails,
       "mpBundleStatusReasmOks": mpBundleStatusReasmOks,
       "mpBundleStatusRcvdFragsDiscarded": mpBundleStatusRcvdFragsDiscarded,
       "mpBundleStatusDropTooManyFrags": mpBundleStatusDropTooManyFrags,
       "mpBundleStatusSingleFragsSent": mpBundleStatusSingleFragsSent,
       "mpBundleStatusFragCreates": mpBundleStatusFragCreates,
       "mpBundleStatusFragFails": mpBundleStatusFragFails,
       "mpBundleStatusFragOks": mpBundleStatusFragOks,
       "mpBundleStatusRcvdFragsBuffered": mpBundleStatusRcvdFragsBuffered,
       "mpBundleConfigTable": mpBundleConfigTable,
       "mpBundleConfigEntry": mpBundleConfigEntry,
       "mpBundleConfigLocalMRRU": mpBundleConfigLocalMRRU,
       "mpBundleConfigLocalEndptDiscr": mpBundleConfigLocalEndptDiscr,
       "mpBundleConfigRcvShortSeq": mpBundleConfigRcvShortSeq,
       "mpBundleConfigSmallPktMaxSize": mpBundleConfigSmallPktMaxSize,
       "mpBundleConfigMediumPktMaxSize": mpBundleConfigMediumPktMaxSize,
       "xediaPppMpConformance": xediaPppMpConformance,
       "mpCompliances": mpCompliances,
       "mpCompliance": mpCompliance,
       "mpGroups": mpGroups,
       "mpAllGroup": mpAllGroup}
)
