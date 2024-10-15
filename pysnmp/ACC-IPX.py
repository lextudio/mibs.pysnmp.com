# SNMP MIB module (ACC-IPX) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-IPX
# Produced by pysmi-1.5.4 at Mon Oct 14 20:32:26 2024
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

(DisplayString,
 IfIndex,
 RowStatus,
 SmdsAddress,
 accBRG) = mibBuilder.importSymbols(
    "ACC-MIB",
    "DisplayString",
    "IfIndex",
    "RowStatus",
    "SmdsAddress",
    "accBRG")

(accTrapLogSeqNum,) = mibBuilder.importSymbols(
    "ACC-SYSTEM",
    "accTrapLogSeqNum")

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

_AccIpx_ObjectIdentity = ObjectIdentity
accIpx = _AccIpx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22)
)
_AccIpxParms_ObjectIdentity = ObjectIdentity
accIpxParms = _AccIpxParms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 1)
)


class _AccIpxAdStat_Type(Integer32):
    """Custom type accIpxAdStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AccIpxAdStat_Type.__name__ = "Integer32"
_AccIpxAdStat_Object = MibScalar
accIpxAdStat = _AccIpxAdStat_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 1, 1),
    _AccIpxAdStat_Type()
)
accIpxAdStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxAdStat.setStatus("mandatory")


class _AccIpxCkSum_Type(Integer32):
    """Custom type accIpxCkSum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("header", 3),
          ("off", 1),
          ("packet", 2))
    )


_AccIpxCkSum_Type.__name__ = "Integer32"
_AccIpxCkSum_Object = MibScalar
accIpxCkSum = _AccIpxCkSum_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 1, 2),
    _AccIpxCkSum_Type()
)
accIpxCkSum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxCkSum.setStatus("mandatory")


class _AccIpxSpltHorz_Type(Integer32):
    """Custom type accIpxSpltHorz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("poison", 3),
          ("simple", 2))
    )


_AccIpxSpltHorz_Type.__name__ = "Integer32"
_AccIpxSpltHorz_Object = MibScalar
accIpxSpltHorz = _AccIpxSpltHorz_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 1, 3),
    _AccIpxSpltHorz_Type()
)
accIpxSpltHorz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxSpltHorz.setStatus("mandatory")


class _AccIpxAllNets_Type(Integer32):
    """Custom type accIpxAllNets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AccIpxAllNets_Type.__name__ = "Integer32"
_AccIpxAllNets_Object = MibScalar
accIpxAllNets = _AccIpxAllNets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 1, 4),
    _AccIpxAllNets_Type()
)
accIpxAllNets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxAllNets.setStatus("mandatory")


class _AccIpxMode_Type(Integer32):
    """Custom type accIpxMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ipx", 1),
          ("repeat", 3),
          ("ub", 2))
    )


_AccIpxMode_Type.__name__ = "Integer32"
_AccIpxMode_Object = MibScalar
accIpxMode = _AccIpxMode_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 1, 5),
    _AccIpxMode_Type()
)
accIpxMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxMode.setStatus("mandatory")


class _AccIpxWdFilter_Type(Integer32):
    """Custom type accIpxWdFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_AccIpxWdFilter_Type.__name__ = "Integer32"
_AccIpxWdFilter_Object = MibScalar
accIpxWdFilter = _AccIpxWdFilter_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 1, 6),
    _AccIpxWdFilter_Type()
)
accIpxWdFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxWdFilter.setStatus("mandatory")


class _AccIpxTrigUpdates_Type(Integer32):
    """Custom type accIpxTrigUpdates based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AccIpxTrigUpdates_Type.__name__ = "Integer32"
_AccIpxTrigUpdates_Object = MibScalar
accIpxTrigUpdates = _AccIpxTrigUpdates_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 1, 7),
    _AccIpxTrigUpdates_Type()
)
accIpxTrigUpdates.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxTrigUpdates.setStatus("mandatory")
_AccIpxNetTable_Object = MibTable
accIpxNetTable = _AccIpxNetTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 2)
)
if mibBuilder.loadTexts:
    accIpxNetTable.setStatus("mandatory")
_AccIpxNetEntry_Object = MibTableRow
accIpxNetEntry = _AccIpxNetEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 2, 1)
)
accIpxNetEntry.setIndexNames(
    (0, "ACC-IPX", "accIpxNetPort"),
)
if mibBuilder.loadTexts:
    accIpxNetEntry.setStatus("mandatory")
_AccIpxNetPort_Type = Integer32
_AccIpxNetPort_Object = MibTableColumn
accIpxNetPort = _AccIpxNetPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 2, 1, 1),
    _AccIpxNetPort_Type()
)
accIpxNetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNetPort.setStatus("mandatory")
_AccIpxNetNumber_Type = OctetString
_AccIpxNetNumber_Object = MibTableColumn
accIpxNetNumber = _AccIpxNetNumber_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 2, 1, 2),
    _AccIpxNetNumber_Type()
)
accIpxNetNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNetNumber.setStatus("mandatory")


class _AccIpxNetType_Type(Integer32):
    """Custom type accIpxNetType based on Integer32"""
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
        *(("dial", 8),
          ("enet", 1),
          ("fddi", 7),
          ("frame-relay", 5),
          ("lapb", 3),
          ("multilink", 9),
          ("ppp", 6),
          ("token-ring", 2),
          ("x25", 4))
    )


_AccIpxNetType_Type.__name__ = "Integer32"
_AccIpxNetType_Object = MibTableColumn
accIpxNetType = _AccIpxNetType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 2, 1, 3),
    _AccIpxNetType_Type()
)
accIpxNetType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNetType.setStatus("mandatory")


class _AccIpxNetEncap_Type(Integer32):
    """Custom type accIpxNetEncap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("llc", 3),
          ("none", 0),
          ("raw", 2),
          ("snap", 4),
          ("v2", 1))
    )


_AccIpxNetEncap_Type.__name__ = "Integer32"
_AccIpxNetEncap_Object = MibTableColumn
accIpxNetEncap = _AccIpxNetEncap_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 2, 1, 4),
    _AccIpxNetEncap_Type()
)
accIpxNetEncap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNetEncap.setStatus("mandatory")


class _AccIpxNetSlot_Type(Integer32):
    """Custom type accIpxNetSlot based on Integer32"""
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
        *(("b1", 4),
          ("j1", 1),
          ("j2", 2),
          ("j3", 3))
    )


_AccIpxNetSlot_Type.__name__ = "Integer32"
_AccIpxNetSlot_Object = MibTableColumn
accIpxNetSlot = _AccIpxNetSlot_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 2, 1, 5),
    _AccIpxNetSlot_Type()
)
accIpxNetSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNetSlot.setStatus("mandatory")


class _AccIpxNetAdStat_Type(Integer32):
    """Custom type accIpxNetAdStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AccIpxNetAdStat_Type.__name__ = "Integer32"
_AccIpxNetAdStat_Object = MibTableColumn
accIpxNetAdStat = _AccIpxNetAdStat_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 2, 1, 6),
    _AccIpxNetAdStat_Type()
)
accIpxNetAdStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNetAdStat.setStatus("mandatory")


class _AccIpxNetMtu_Type(Integer32):
    """Custom type accIpxNetMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(576, 65535),
    )


_AccIpxNetMtu_Type.__name__ = "Integer32"
_AccIpxNetMtu_Object = MibTableColumn
accIpxNetMtu = _AccIpxNetMtu_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 2, 1, 7),
    _AccIpxNetMtu_Type()
)
accIpxNetMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNetMtu.setStatus("mandatory")


class _AccIpxNetUpdate_Type(TimeTicks):
    """Custom type accIpxNetUpdate based on TimeTicks"""
    defaultValue = 1500


_AccIpxNetUpdate_Object = MibTableColumn
accIpxNetUpdate = _AccIpxNetUpdate_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 2, 1, 8),
    _AccIpxNetUpdate_Type()
)
accIpxNetUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNetUpdate.setStatus("mandatory")


class _AccIpxNetHops_Type(Integer32):
    """Custom type accIpxNetHops based on Integer32"""
    defaultValue = 1


_AccIpxNetHops_Object = MibTableColumn
accIpxNetHops = _AccIpxNetHops_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 2, 1, 9),
    _AccIpxNetHops_Type()
)
accIpxNetHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNetHops.setStatus("mandatory")


class _AccIpxNetCost_Type(Integer32):
    """Custom type accIpxNetCost based on Integer32"""
    defaultValue = 1


_AccIpxNetCost_Object = MibTableColumn
accIpxNetCost = _AccIpxNetCost_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 2, 1, 10),
    _AccIpxNetCost_Type()
)
accIpxNetCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNetCost.setStatus("mandatory")
_AccIpxNetX25InOutAddr_Type = DisplayString
_AccIpxNetX25InOutAddr_Object = MibTableColumn
accIpxNetX25InOutAddr = _AccIpxNetX25InOutAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 2, 1, 11),
    _AccIpxNetX25InOutAddr_Type()
)
accIpxNetX25InOutAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNetX25InOutAddr.setStatus("mandatory")
_AccIpxNetX25InAddr_Type = DisplayString
_AccIpxNetX25InAddr_Object = MibTableColumn
accIpxNetX25InAddr = _AccIpxNetX25InAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 2, 1, 12),
    _AccIpxNetX25InAddr_Type()
)
accIpxNetX25InAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNetX25InAddr.setStatus("mandatory")


class _AccIpxNetX25Idle_Type(TimeTicks):
    """Custom type accIpxNetX25Idle based on TimeTicks"""
    defaultValue = 30000


_AccIpxNetX25Idle_Object = MibTableColumn
accIpxNetX25Idle = _AccIpxNetX25Idle_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 2, 1, 13),
    _AccIpxNetX25Idle_Type()
)
accIpxNetX25Idle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNetX25Idle.setStatus("mandatory")


class _AccIpxNetX25PktVal_Type(Integer32):
    """Custom type accIpxNetX25PktVal based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_AccIpxNetX25PktVal_Type.__name__ = "Integer32"
_AccIpxNetX25PktVal_Object = MibTableColumn
accIpxNetX25PktVal = _AccIpxNetX25PktVal_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 2, 1, 14),
    _AccIpxNetX25PktVal_Type()
)
accIpxNetX25PktVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNetX25PktVal.setStatus("mandatory")


class _AccIpxNetX25PktWin_Type(Integer32):
    """Custom type accIpxNetX25PktWin based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_AccIpxNetX25PktWin_Type.__name__ = "Integer32"
_AccIpxNetX25PktWin_Object = MibTableColumn
accIpxNetX25PktWin = _AccIpxNetX25PktWin_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 2, 1, 15),
    _AccIpxNetX25PktWin_Type()
)
accIpxNetX25PktWin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNetX25PktWin.setStatus("mandatory")


class _AccIpxNetEntryStat_Type(Integer32):
    """Custom type accIpxNetEntryStat based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("other", 1))
    )


_AccIpxNetEntryStat_Type.__name__ = "Integer32"
_AccIpxNetEntryStat_Object = MibTableColumn
accIpxNetEntryStat = _AccIpxNetEntryStat_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 2, 1, 16),
    _AccIpxNetEntryStat_Type()
)
accIpxNetEntryStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNetEntryStat.setStatus("mandatory")
_AccIpxNetFncAddr_Type = OctetString
_AccIpxNetFncAddr_Object = MibTableColumn
accIpxNetFncAddr = _AccIpxNetFncAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 2, 1, 17),
    _AccIpxNetFncAddr_Type()
)
accIpxNetFncAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNetFncAddr.setStatus("mandatory")


class _AccIpxNetSrMode_Type(Integer32):
    """Custom type accIpxNetSrMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ape", 1),
          ("off", 0),
          ("spe", 2))
    )


_AccIpxNetSrMode_Type.__name__ = "Integer32"
_AccIpxNetSrMode_Object = MibTableColumn
accIpxNetSrMode = _AccIpxNetSrMode_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 2, 1, 18),
    _AccIpxNetSrMode_Type()
)
accIpxNetSrMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNetSrMode.setStatus("mandatory")


class _AccIpxNetX25FacIndex_Type(Integer32):
    """Custom type accIpxNetX25FacIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AccIpxNetX25FacIndex_Type.__name__ = "Integer32"
_AccIpxNetX25FacIndex_Object = MibTableColumn
accIpxNetX25FacIndex = _AccIpxNetX25FacIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 2, 1, 19),
    _AccIpxNetX25FacIndex_Type()
)
accIpxNetX25FacIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNetX25FacIndex.setStatus("mandatory")
_AccIpxNetDlci_Type = Integer32
_AccIpxNetDlci_Object = MibTableColumn
accIpxNetDlci = _AccIpxNetDlci_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 2, 1, 20),
    _AccIpxNetDlci_Type()
)
accIpxNetDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNetDlci.setStatus("mandatory")


class _AccIpxNetWdState_Type(Integer32):
    """Custom type accIpxNetWdState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("discard", 2),
          ("proxy", 3))
    )


_AccIpxNetWdState_Type.__name__ = "Integer32"
_AccIpxNetWdState_Object = MibTableColumn
accIpxNetWdState = _AccIpxNetWdState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 2, 1, 21),
    _AccIpxNetWdState_Type()
)
accIpxNetWdState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNetWdState.setStatus("mandatory")


class _AccIpxNetRtgHldTmr_Type(Integer32):
    """Custom type accIpxNetRtgHldTmr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AccIpxNetRtgHldTmr_Type.__name__ = "Integer32"
_AccIpxNetRtgHldTmr_Object = MibTableColumn
accIpxNetRtgHldTmr = _AccIpxNetRtgHldTmr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 2, 1, 22),
    _AccIpxNetRtgHldTmr_Type()
)
accIpxNetRtgHldTmr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNetRtgHldTmr.setStatus("mandatory")


class _AccIpxNetRtgPollCnt_Type(Integer32):
    """Custom type accIpxNetRtgPollCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AccIpxNetRtgPollCnt_Type.__name__ = "Integer32"
_AccIpxNetRtgPollCnt_Object = MibTableColumn
accIpxNetRtgPollCnt = _AccIpxNetRtgPollCnt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 2, 1, 23),
    _AccIpxNetRtgPollCnt_Type()
)
accIpxNetRtgPollCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNetRtgPollCnt.setStatus("mandatory")


class _AccIpxNetRtgProtType_Type(Integer32):
    """Custom type accIpxNetRtgProtType based on Integer32"""
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
        *(("demand", 3),
          ("normal", 2),
          ("off", 1),
          ("snapshot", 4))
    )


_AccIpxNetRtgProtType_Type.__name__ = "Integer32"
_AccIpxNetRtgProtType_Object = MibTableColumn
accIpxNetRtgProtType = _AccIpxNetRtgProtType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 2, 1, 24),
    _AccIpxNetRtgProtType_Type()
)
accIpxNetRtgProtType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNetRtgProtType.setStatus("mandatory")


class _AccIpxNetRtgSettleTimer_Type(Integer32):
    """Custom type accIpxNetRtgSettleTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_AccIpxNetRtgSettleTimer_Type.__name__ = "Integer32"
_AccIpxNetRtgSettleTimer_Object = MibTableColumn
accIpxNetRtgSettleTimer = _AccIpxNetRtgSettleTimer_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 2, 1, 25),
    _AccIpxNetRtgSettleTimer_Type()
)
accIpxNetRtgSettleTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNetRtgSettleTimer.setStatus("mandatory")


class _AccIpxNetRtgQuietTimer_Type(Integer32):
    """Custom type accIpxNetRtgQuietTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AccIpxNetRtgQuietTimer_Type.__name__ = "Integer32"
_AccIpxNetRtgQuietTimer_Object = MibTableColumn
accIpxNetRtgQuietTimer = _AccIpxNetRtgQuietTimer_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 2, 1, 26),
    _AccIpxNetRtgQuietTimer_Type()
)
accIpxNetRtgQuietTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNetRtgQuietTimer.setStatus("mandatory")


class _AccIpxNetRtgDiagLevel_Type(Integer32):
    """Custom type accIpxNetRtgDiagLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AccIpxNetRtgDiagLevel_Type.__name__ = "Integer32"
_AccIpxNetRtgDiagLevel_Object = MibTableColumn
accIpxNetRtgDiagLevel = _AccIpxNetRtgDiagLevel_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 2, 1, 27),
    _AccIpxNetRtgDiagLevel_Type()
)
accIpxNetRtgDiagLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNetRtgDiagLevel.setStatus("mandatory")


class _AccIpxNetDialProt_Type(Integer32):
    """Custom type accIpxNetDialProt based on Integer32"""
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
          ("ppp", 2),
          ("x25", 3))
    )


_AccIpxNetDialProt_Type.__name__ = "Integer32"
_AccIpxNetDialProt_Object = MibTableColumn
accIpxNetDialProt = _AccIpxNetDialProt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 2, 1, 28),
    _AccIpxNetDialProt_Type()
)
accIpxNetDialProt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNetDialProt.setStatus("mandatory")
_AccIpxRtTable_Object = MibTable
accIpxRtTable = _AccIpxRtTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 3)
)
if mibBuilder.loadTexts:
    accIpxRtTable.setStatus("mandatory")
_AccIpxRtEntry_Object = MibTableRow
accIpxRtEntry = _AccIpxRtEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 3, 1)
)
accIpxRtEntry.setIndexNames(
    (0, "ACC-IPX", "accIpxRtDest"),
)
if mibBuilder.loadTexts:
    accIpxRtEntry.setStatus("mandatory")
_AccIpxRtDest_Type = OctetString
_AccIpxRtDest_Object = MibTableColumn
accIpxRtDest = _AccIpxRtDest_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 3, 1, 1),
    _AccIpxRtDest_Type()
)
accIpxRtDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxRtDest.setStatus("mandatory")
_AccIpxRtNxtNet_Type = OctetString
_AccIpxRtNxtNet_Object = MibTableColumn
accIpxRtNxtNet = _AccIpxRtNxtNet_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 3, 1, 2),
    _AccIpxRtNxtNet_Type()
)
accIpxRtNxtNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxRtNxtNet.setStatus("mandatory")
_AccIpxRtRouter_Type = OctetString
_AccIpxRtRouter_Object = MibTableColumn
accIpxRtRouter = _AccIpxRtRouter_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 3, 1, 3),
    _AccIpxRtRouter_Type()
)
accIpxRtRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxRtRouter.setStatus("mandatory")
_AccIpxRtHops_Type = Integer32
_AccIpxRtHops_Object = MibTableColumn
accIpxRtHops = _AccIpxRtHops_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 3, 1, 4),
    _AccIpxRtHops_Type()
)
accIpxRtHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxRtHops.setStatus("mandatory")
_AccIpxRtCost_Type = Integer32
_AccIpxRtCost_Object = MibTableColumn
accIpxRtCost = _AccIpxRtCost_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 3, 1, 5),
    _AccIpxRtCost_Type()
)
accIpxRtCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxRtCost.setStatus("mandatory")


class _AccIpxRtType_Type(Integer32):
    """Custom type accIpxRtType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("direct", 2),
          ("public", 1),
          ("static", 3))
    )


_AccIpxRtType_Type.__name__ = "Integer32"
_AccIpxRtType_Object = MibTableColumn
accIpxRtType = _AccIpxRtType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 3, 1, 6),
    _AccIpxRtType_Type()
)
accIpxRtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxRtType.setStatus("mandatory")


class _AccIpxRtOwner_Type(Integer32):
    """Custom type accIpxRtOwner based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lli", 1),
          ("nms", 2),
          ("rip", 3))
    )


_AccIpxRtOwner_Type.__name__ = "Integer32"
_AccIpxRtOwner_Object = MibTableColumn
accIpxRtOwner = _AccIpxRtOwner_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 3, 1, 7),
    _AccIpxRtOwner_Type()
)
accIpxRtOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxRtOwner.setStatus("mandatory")
_AccIpxRtAge_Type = TimeTicks
_AccIpxRtAge_Object = MibTableColumn
accIpxRtAge = _AccIpxRtAge_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 3, 1, 8),
    _AccIpxRtAge_Type()
)
accIpxRtAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxRtAge.setStatus("mandatory")
_AccIpxRtPort_Type = Integer32
_AccIpxRtPort_Object = MibTableColumn
accIpxRtPort = _AccIpxRtPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 3, 1, 9),
    _AccIpxRtPort_Type()
)
accIpxRtPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxRtPort.setStatus("mandatory")
_AccIpxRipStat_ObjectIdentity = ObjectIdentity
accIpxRipStat = _AccIpxRipStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 4)
)
_AccIpxRipReqIns_Type = Counter32
_AccIpxRipReqIns_Object = MibScalar
accIpxRipReqIns = _AccIpxRipReqIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 4, 1),
    _AccIpxRipReqIns_Type()
)
accIpxRipReqIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxRipReqIns.setStatus("mandatory")
_AccIpxRipRespIns_Type = Counter32
_AccIpxRipRespIns_Object = MibScalar
accIpxRipRespIns = _AccIpxRipRespIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 4, 2),
    _AccIpxRipRespIns_Type()
)
accIpxRipRespIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxRipRespIns.setStatus("mandatory")
_AccIpxRipReqOuts_Type = Counter32
_AccIpxRipReqOuts_Object = MibScalar
accIpxRipReqOuts = _AccIpxRipReqOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 4, 3),
    _AccIpxRipReqOuts_Type()
)
accIpxRipReqOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxRipReqOuts.setStatus("mandatory")
_AccIpxRipRespOuts_Type = Counter32
_AccIpxRipRespOuts_Object = MibScalar
accIpxRipRespOuts = _AccIpxRipRespOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 4, 4),
    _AccIpxRipRespOuts_Type()
)
accIpxRipRespOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxRipRespOuts.setStatus("mandatory")
_AccIpxRipErrIns_Type = Counter32
_AccIpxRipErrIns_Object = MibScalar
accIpxRipErrIns = _AccIpxRipErrIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 4, 5),
    _AccIpxRipErrIns_Type()
)
accIpxRipErrIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxRipErrIns.setStatus("mandatory")
_AccIpxRipErrOuts_Type = Counter32
_AccIpxRipErrOuts_Object = MibScalar
accIpxRipErrOuts = _AccIpxRipErrOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 4, 6),
    _AccIpxRipErrOuts_Type()
)
accIpxRipErrOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxRipErrOuts.setStatus("mandatory")
_AccIpxRipDemandReqIns_Type = Counter32
_AccIpxRipDemandReqIns_Object = MibScalar
accIpxRipDemandReqIns = _AccIpxRipDemandReqIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 4, 7),
    _AccIpxRipDemandReqIns_Type()
)
accIpxRipDemandReqIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxRipDemandReqIns.setStatus("mandatory")
_AccIpxRipDemandRespIns_Type = Counter32
_AccIpxRipDemandRespIns_Object = MibScalar
accIpxRipDemandRespIns = _AccIpxRipDemandRespIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 4, 8),
    _AccIpxRipDemandRespIns_Type()
)
accIpxRipDemandRespIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxRipDemandRespIns.setStatus("mandatory")
_AccIpxRipDemandAckIns_Type = Counter32
_AccIpxRipDemandAckIns_Object = MibScalar
accIpxRipDemandAckIns = _AccIpxRipDemandAckIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 4, 9),
    _AccIpxRipDemandAckIns_Type()
)
accIpxRipDemandAckIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxRipDemandAckIns.setStatus("mandatory")
_AccIpxRipDemandReqOuts_Type = Counter32
_AccIpxRipDemandReqOuts_Object = MibScalar
accIpxRipDemandReqOuts = _AccIpxRipDemandReqOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 4, 10),
    _AccIpxRipDemandReqOuts_Type()
)
accIpxRipDemandReqOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxRipDemandReqOuts.setStatus("mandatory")
_AccIpxRipDemandRespOuts_Type = Counter32
_AccIpxRipDemandRespOuts_Object = MibScalar
accIpxRipDemandRespOuts = _AccIpxRipDemandRespOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 4, 11),
    _AccIpxRipDemandRespOuts_Type()
)
accIpxRipDemandRespOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxRipDemandRespOuts.setStatus("mandatory")
_AccIpxRipDemandAckOuts_Type = Counter32
_AccIpxRipDemandAckOuts_Object = MibScalar
accIpxRipDemandAckOuts = _AccIpxRipDemandAckOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 4, 12),
    _AccIpxRipDemandAckOuts_Type()
)
accIpxRipDemandAckOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxRipDemandAckOuts.setStatus("mandatory")
_AccIpxRipDemandInErrs_Type = Counter32
_AccIpxRipDemandInErrs_Object = MibScalar
accIpxRipDemandInErrs = _AccIpxRipDemandInErrs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 4, 13),
    _AccIpxRipDemandInErrs_Type()
)
accIpxRipDemandInErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxRipDemandInErrs.setStatus("mandatory")
_AccIpxRipDemandOutErrs_Type = Counter32
_AccIpxRipDemandOutErrs_Object = MibScalar
accIpxRipDemandOutErrs = _AccIpxRipDemandOutErrs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 4, 14),
    _AccIpxRipDemandOutErrs_Type()
)
accIpxRipDemandOutErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxRipDemandOutErrs.setStatus("mandatory")
_AccIpxNodeStat_ObjectIdentity = ObjectIdentity
accIpxNodeStat = _AccIpxNodeStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 5)
)
_AccIpxLocalIns_Type = Counter32
_AccIpxLocalIns_Object = MibScalar
accIpxLocalIns = _AccIpxLocalIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 5, 1),
    _AccIpxLocalIns_Type()
)
accIpxLocalIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxLocalIns.setStatus("mandatory")
_AccIpxLocalOuts_Type = Counter32
_AccIpxLocalOuts_Object = MibScalar
accIpxLocalOuts = _AccIpxLocalOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 5, 2),
    _AccIpxLocalOuts_Type()
)
accIpxLocalOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxLocalOuts.setStatus("mandatory")
_AccIpxNoSockets_Type = Counter32
_AccIpxNoSockets_Object = MibScalar
accIpxNoSockets = _AccIpxNoSockets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 5, 3),
    _AccIpxNoSockets_Type()
)
accIpxNoSockets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxNoSockets.setStatus("mandatory")
_AccIpxNoRoutes_Type = Counter32
_AccIpxNoRoutes_Object = MibScalar
accIpxNoRoutes = _AccIpxNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 5, 4),
    _AccIpxNoRoutes_Type()
)
accIpxNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxNoRoutes.setStatus("mandatory")
_AccIpxNodeInErrs_Type = Counter32
_AccIpxNodeInErrs_Object = MibScalar
accIpxNodeInErrs = _AccIpxNodeInErrs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 5, 5),
    _AccIpxNodeInErrs_Type()
)
accIpxNodeInErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxNodeInErrs.setStatus("mandatory")
_AccIpxOutErrs_Type = Counter32
_AccIpxOutErrs_Object = MibScalar
accIpxOutErrs = _AccIpxOutErrs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 5, 6),
    _AccIpxOutErrs_Type()
)
accIpxOutErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxOutErrs.setStatus("mandatory")
_AccIpxAllNetsIns_Type = Counter32
_AccIpxAllNetsIns_Object = MibScalar
accIpxAllNetsIns = _AccIpxAllNetsIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 5, 7),
    _AccIpxAllNetsIns_Type()
)
accIpxAllNetsIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxAllNetsIns.setStatus("mandatory")
_AccIpxAllNetsOuts_Type = Counter32
_AccIpxAllNetsOuts_Object = MibScalar
accIpxAllNetsOuts = _AccIpxAllNetsOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 5, 8),
    _AccIpxAllNetsOuts_Type()
)
accIpxAllNetsOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxAllNetsOuts.setStatus("mandatory")
_AccIpxAllNetsErrs_Type = Counter32
_AccIpxAllNetsErrs_Object = MibScalar
accIpxAllNetsErrs = _AccIpxAllNetsErrs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 5, 9),
    _AccIpxAllNetsErrs_Type()
)
accIpxAllNetsErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxAllNetsErrs.setStatus("mandatory")
_AccIpxPortStatTable_Object = MibTable
accIpxPortStatTable = _AccIpxPortStatTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 6)
)
if mibBuilder.loadTexts:
    accIpxPortStatTable.setStatus("mandatory")
_AccIpxPortStatEntry_Object = MibTableRow
accIpxPortStatEntry = _AccIpxPortStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 6, 1)
)
accIpxPortStatEntry.setIndexNames(
    (0, "ACC-IPX", "accIpxPortNumber"),
)
if mibBuilder.loadTexts:
    accIpxPortStatEntry.setStatus("mandatory")
_AccIpxPortNumber_Type = Integer32
_AccIpxPortNumber_Object = MibTableColumn
accIpxPortNumber = _AccIpxPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 6, 1, 1),
    _AccIpxPortNumber_Type()
)
accIpxPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxPortNumber.setStatus("mandatory")
_AccIpxPortTotalIns_Type = Counter32
_AccIpxPortTotalIns_Object = MibTableColumn
accIpxPortTotalIns = _AccIpxPortTotalIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 6, 1, 2),
    _AccIpxPortTotalIns_Type()
)
accIpxPortTotalIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxPortTotalIns.setStatus("mandatory")
_AccIpxPorFwdReqIns_Type = Counter32
_AccIpxPorFwdReqIns_Object = MibTableColumn
accIpxPorFwdReqIns = _AccIpxPorFwdReqIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 6, 1, 3),
    _AccIpxPorFwdReqIns_Type()
)
accIpxPorFwdReqIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxPorFwdReqIns.setStatus("mandatory")
_AccIpxPortNoFwdRts_Type = Counter32
_AccIpxPortNoFwdRts_Object = MibTableColumn
accIpxPortNoFwdRts = _AccIpxPortNoFwdRts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 6, 1, 4),
    _AccIpxPortNoFwdRts_Type()
)
accIpxPortNoFwdRts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxPortNoFwdRts.setStatus("mandatory")
_AccIpxPortTotalOuts_Type = Counter32
_AccIpxPortTotalOuts_Object = MibTableColumn
accIpxPortTotalOuts = _AccIpxPortTotalOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 6, 1, 5),
    _AccIpxPortTotalOuts_Type()
)
accIpxPortTotalOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxPortTotalOuts.setStatus("mandatory")
_AccIpxPortHopCnts_Type = Counter32
_AccIpxPortHopCnts_Object = MibTableColumn
accIpxPortHopCnts = _AccIpxPortHopCnts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 6, 1, 6),
    _AccIpxPortHopCnts_Type()
)
accIpxPortHopCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxPortHopCnts.setStatus("mandatory")
_AccIpxPortNotForMes_Type = Counter32
_AccIpxPortNotForMes_Object = MibTableColumn
accIpxPortNotForMes = _AccIpxPortNotForMes_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 6, 1, 7),
    _AccIpxPortNotForMes_Type()
)
accIpxPortNotForMes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxPortNotForMes.setStatus("mandatory")
_AccIpxPortFwdReqOuts_Type = Counter32
_AccIpxPortFwdReqOuts_Object = MibTableColumn
accIpxPortFwdReqOuts = _AccIpxPortFwdReqOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 6, 1, 8),
    _AccIpxPortFwdReqOuts_Type()
)
accIpxPortFwdReqOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxPortFwdReqOuts.setStatus("mandatory")
_AccIpxPortFwdErrs_Type = Counter32
_AccIpxPortFwdErrs_Object = MibTableColumn
accIpxPortFwdErrs = _AccIpxPortFwdErrs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 6, 1, 9),
    _AccIpxPortFwdErrs_Type()
)
accIpxPortFwdErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxPortFwdErrs.setStatus("mandatory")
_AccIpxPortInErrs_Type = Counter32
_AccIpxPortInErrs_Object = MibTableColumn
accIpxPortInErrs = _AccIpxPortInErrs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 6, 1, 10),
    _AccIpxPortInErrs_Type()
)
accIpxPortInErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxPortInErrs.setStatus("mandatory")
_AccIpxPortTooShorts_Type = Counter32
_AccIpxPortTooShorts_Object = MibTableColumn
accIpxPortTooShorts = _AccIpxPortTooShorts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 6, 1, 11),
    _AccIpxPortTooShorts_Type()
)
accIpxPortTooShorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxPortTooShorts.setStatus("mandatory")
_AccIpxPortCkSums_Type = Counter32
_AccIpxPortCkSums_Object = MibTableColumn
accIpxPortCkSums = _AccIpxPortCkSums_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 6, 1, 12),
    _AccIpxPortCkSums_Type()
)
accIpxPortCkSums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxPortCkSums.setStatus("mandatory")
_AccIpxPortTooLongs_Type = Counter32
_AccIpxPortTooLongs_Object = MibTableColumn
accIpxPortTooLongs = _AccIpxPortTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 6, 1, 13),
    _AccIpxPortTooLongs_Type()
)
accIpxPortTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxPortTooLongs.setStatus("mandatory")
_AccIpxPortOutErrs_Type = Counter32
_AccIpxPortOutErrs_Object = MibTableColumn
accIpxPortOutErrs = _AccIpxPortOutErrs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 6, 1, 14),
    _AccIpxPortOutErrs_Type()
)
accIpxPortOutErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxPortOutErrs.setStatus("mandatory")


class _AccIpxPortOpState_Type(Integer32):
    """Custom type accIpxPortOpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("off", 0),
          ("start", 2),
          ("stop", 3),
          ("up", 4))
    )


_AccIpxPortOpState_Type.__name__ = "Integer32"
_AccIpxPortOpState_Object = MibTableColumn
accIpxPortOpState = _AccIpxPortOpState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 6, 1, 15),
    _AccIpxPortOpState_Type()
)
accIpxPortOpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxPortOpState.setStatus("mandatory")
_AccIpxSapStat_ObjectIdentity = ObjectIdentity
accIpxSapStat = _AccIpxSapStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 7)
)
_AccIpxSapReqIns_Type = Counter32
_AccIpxSapReqIns_Object = MibScalar
accIpxSapReqIns = _AccIpxSapReqIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 7, 1),
    _AccIpxSapReqIns_Type()
)
accIpxSapReqIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxSapReqIns.setStatus("mandatory")
_AccIpxSapReqOuts_Type = Counter32
_AccIpxSapReqOuts_Object = MibScalar
accIpxSapReqOuts = _AccIpxSapReqOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 7, 2),
    _AccIpxSapReqOuts_Type()
)
accIpxSapReqOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxSapReqOuts.setStatus("mandatory")
_AccIpxSapRespIns_Type = Counter32
_AccIpxSapRespIns_Object = MibScalar
accIpxSapRespIns = _AccIpxSapRespIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 7, 3),
    _AccIpxSapRespIns_Type()
)
accIpxSapRespIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxSapRespIns.setStatus("mandatory")
_AccIpxSapRespOuts_Type = Counter32
_AccIpxSapRespOuts_Object = MibScalar
accIpxSapRespOuts = _AccIpxSapRespOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 7, 4),
    _AccIpxSapRespOuts_Type()
)
accIpxSapRespOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxSapRespOuts.setStatus("mandatory")
_AccIpxSapGetNearIns_Type = Counter32
_AccIpxSapGetNearIns_Object = MibScalar
accIpxSapGetNearIns = _AccIpxSapGetNearIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 7, 5),
    _AccIpxSapGetNearIns_Type()
)
accIpxSapGetNearIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxSapGetNearIns.setStatus("mandatory")
_AccIpxSapGetNearOuts_Type = Counter32
_AccIpxSapGetNearOuts_Object = MibScalar
accIpxSapGetNearOuts = _AccIpxSapGetNearOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 7, 6),
    _AccIpxSapGetNearOuts_Type()
)
accIpxSapGetNearOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxSapGetNearOuts.setStatus("mandatory")
_AccIpxSapNoRoutes_Type = Counter32
_AccIpxSapNoRoutes_Object = MibScalar
accIpxSapNoRoutes = _AccIpxSapNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 7, 7),
    _AccIpxSapNoRoutes_Type()
)
accIpxSapNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxSapNoRoutes.setStatus("mandatory")
_AccIpxSapNotBests_Type = Counter32
_AccIpxSapNotBests_Object = MibScalar
accIpxSapNotBests = _AccIpxSapNotBests_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 7, 8),
    _AccIpxSapNotBests_Type()
)
accIpxSapNotBests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxSapNotBests.setStatus("mandatory")
_AccIpxSapNoServers_Type = Counter32
_AccIpxSapNoServers_Object = MibScalar
accIpxSapNoServers = _AccIpxSapNoServers_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 7, 9),
    _AccIpxSapNoServers_Type()
)
accIpxSapNoServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxSapNoServers.setStatus("mandatory")
_AccIpxSapInErrs_Type = Counter32
_AccIpxSapInErrs_Object = MibScalar
accIpxSapInErrs = _AccIpxSapInErrs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 7, 10),
    _AccIpxSapInErrs_Type()
)
accIpxSapInErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxSapInErrs.setStatus("mandatory")
_AccIpxSapOutErrs_Type = Counter32
_AccIpxSapOutErrs_Object = MibScalar
accIpxSapOutErrs = _AccIpxSapOutErrs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 7, 11),
    _AccIpxSapOutErrs_Type()
)
accIpxSapOutErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxSapOutErrs.setStatus("mandatory")
_AccIpxSapDemandReqIns_Type = Counter32
_AccIpxSapDemandReqIns_Object = MibScalar
accIpxSapDemandReqIns = _AccIpxSapDemandReqIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 7, 12),
    _AccIpxSapDemandReqIns_Type()
)
accIpxSapDemandReqIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxSapDemandReqIns.setStatus("mandatory")
_AccIpxSapDemandReqOuts_Type = Counter32
_AccIpxSapDemandReqOuts_Object = MibScalar
accIpxSapDemandReqOuts = _AccIpxSapDemandReqOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 7, 13),
    _AccIpxSapDemandReqOuts_Type()
)
accIpxSapDemandReqOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxSapDemandReqOuts.setStatus("mandatory")
_AccIpxSapDemandRespIns_Type = Counter32
_AccIpxSapDemandRespIns_Object = MibScalar
accIpxSapDemandRespIns = _AccIpxSapDemandRespIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 7, 14),
    _AccIpxSapDemandRespIns_Type()
)
accIpxSapDemandRespIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxSapDemandRespIns.setStatus("mandatory")
_AccIpxSapDemandRespOuts_Type = Counter32
_AccIpxSapDemandRespOuts_Object = MibScalar
accIpxSapDemandRespOuts = _AccIpxSapDemandRespOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 7, 15),
    _AccIpxSapDemandRespOuts_Type()
)
accIpxSapDemandRespOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxSapDemandRespOuts.setStatus("mandatory")
_AccIpxSapDemandAckIns_Type = Counter32
_AccIpxSapDemandAckIns_Object = MibScalar
accIpxSapDemandAckIns = _AccIpxSapDemandAckIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 7, 16),
    _AccIpxSapDemandAckIns_Type()
)
accIpxSapDemandAckIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxSapDemandAckIns.setStatus("mandatory")
_AccIpxSapDemandAckOuts_Type = Counter32
_AccIpxSapDemandAckOuts_Object = MibScalar
accIpxSapDemandAckOuts = _AccIpxSapDemandAckOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 7, 17),
    _AccIpxSapDemandAckOuts_Type()
)
accIpxSapDemandAckOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxSapDemandAckOuts.setStatus("mandatory")
_AccIpxSapDemandInErrs_Type = Counter32
_AccIpxSapDemandInErrs_Object = MibScalar
accIpxSapDemandInErrs = _AccIpxSapDemandInErrs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 7, 18),
    _AccIpxSapDemandInErrs_Type()
)
accIpxSapDemandInErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxSapDemandInErrs.setStatus("mandatory")
_AccIpxSapDemandOutErrs_Type = Counter32
_AccIpxSapDemandOutErrs_Object = MibScalar
accIpxSapDemandOutErrs = _AccIpxSapDemandOutErrs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 7, 19),
    _AccIpxSapDemandOutErrs_Type()
)
accIpxSapDemandOutErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxSapDemandOutErrs.setStatus("mandatory")
_AccIpxSrvTable_Object = MibTable
accIpxSrvTable = _AccIpxSrvTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 8)
)
if mibBuilder.loadTexts:
    accIpxSrvTable.setStatus("mandatory")
_AccIpxSrvEntry_Object = MibTableRow
accIpxSrvEntry = _AccIpxSrvEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 8, 1)
)
accIpxSrvEntry.setIndexNames(
    (0, "ACC-IPX", "accIpxSrvType"),
    (0, "ACC-IPX", "accIpxSrvName"),
)
if mibBuilder.loadTexts:
    accIpxSrvEntry.setStatus("mandatory")
_AccIpxSrvName_Type = DisplayString
_AccIpxSrvName_Object = MibTableColumn
accIpxSrvName = _AccIpxSrvName_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 8, 1, 1),
    _AccIpxSrvName_Type()
)
accIpxSrvName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxSrvName.setStatus("mandatory")
_AccIpxSrvType_Type = OctetString
_AccIpxSrvType_Object = MibTableColumn
accIpxSrvType = _AccIpxSrvType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 8, 1, 2),
    _AccIpxSrvType_Type()
)
accIpxSrvType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxSrvType.setStatus("mandatory")
_AccIpxSrvHost_Type = OctetString
_AccIpxSrvHost_Object = MibTableColumn
accIpxSrvHost = _AccIpxSrvHost_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 8, 1, 3),
    _AccIpxSrvHost_Type()
)
accIpxSrvHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxSrvHost.setStatus("mandatory")
_AccIpxSrvHops_Type = Integer32
_AccIpxSrvHops_Object = MibTableColumn
accIpxSrvHops = _AccIpxSrvHops_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 8, 1, 4),
    _AccIpxSrvHops_Type()
)
accIpxSrvHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxSrvHops.setStatus("mandatory")


class _AccIpxSrvOwner_Type(Integer32):
    """Custom type accIpxSrvOwner based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nms", 1),
          ("sap", 2))
    )


_AccIpxSrvOwner_Type.__name__ = "Integer32"
_AccIpxSrvOwner_Object = MibTableColumn
accIpxSrvOwner = _AccIpxSrvOwner_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 8, 1, 5),
    _AccIpxSrvOwner_Type()
)
accIpxSrvOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxSrvOwner.setStatus("mandatory")
_AccIpxSrvAge_Type = TimeTicks
_AccIpxSrvAge_Object = MibTableColumn
accIpxSrvAge = _AccIpxSrvAge_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 8, 1, 6),
    _AccIpxSrvAge_Type()
)
accIpxSrvAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxSrvAge.setStatus("mandatory")
_AccIpxRouteFilters_ObjectIdentity = ObjectIdentity
accIpxRouteFilters = _AccIpxRouteFilters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 9)
)


class _AccIpxRteFltrDefaultAction_Type(Integer32):
    """Custom type accIpxRteFltrDefaultAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("reject", 2))
    )


_AccIpxRteFltrDefaultAction_Type.__name__ = "Integer32"
_AccIpxRteFltrDefaultAction_Object = MibScalar
accIpxRteFltrDefaultAction = _AccIpxRteFltrDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 9, 1),
    _AccIpxRteFltrDefaultAction_Type()
)
accIpxRteFltrDefaultAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxRteFltrDefaultAction.setStatus("deprecated")
_AccIpxRteNbrTable_Object = MibTable
accIpxRteNbrTable = _AccIpxRteNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 9, 2)
)
if mibBuilder.loadTexts:
    accIpxRteNbrTable.setStatus("deprecated")
_AccIpxRteNbrEntry_Object = MibTableRow
accIpxRteNbrEntry = _AccIpxRteNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 9, 2, 1)
)
accIpxRteNbrEntry.setIndexNames(
    (0, "ACC-IPX", "accIpxRteNbrId"),
)
if mibBuilder.loadTexts:
    accIpxRteNbrEntry.setStatus("deprecated")
_AccIpxRteNbrId_Type = OctetString
_AccIpxRteNbrId_Object = MibTableColumn
accIpxRteNbrId = _AccIpxRteNbrId_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 9, 2, 1, 1),
    _AccIpxRteNbrId_Type()
)
accIpxRteNbrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxRteNbrId.setStatus("deprecated")


class _AccIpxRteNbrAction_Type(Integer32):
    """Custom type accIpxRteNbrAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("reject", 2))
    )


_AccIpxRteNbrAction_Type.__name__ = "Integer32"
_AccIpxRteNbrAction_Object = MibTableColumn
accIpxRteNbrAction = _AccIpxRteNbrAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 9, 2, 1, 2),
    _AccIpxRteNbrAction_Type()
)
accIpxRteNbrAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxRteNbrAction.setStatus("deprecated")


class _AccIpxRteNbrStatus_Type(Integer32):
    """Custom type accIpxRteNbrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_AccIpxRteNbrStatus_Type.__name__ = "Integer32"
_AccIpxRteNbrStatus_Object = MibTableColumn
accIpxRteNbrStatus = _AccIpxRteNbrStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 9, 2, 1, 3),
    _AccIpxRteNbrStatus_Type()
)
accIpxRteNbrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxRteNbrStatus.setStatus("deprecated")
_AccIpxRteFltrTable_Object = MibTable
accIpxRteFltrTable = _AccIpxRteFltrTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 9, 3)
)
if mibBuilder.loadTexts:
    accIpxRteFltrTable.setStatus("deprecated")
_AccIpxRteFltrEntry_Object = MibTableRow
accIpxRteFltrEntry = _AccIpxRteFltrEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 9, 3, 1)
)
accIpxRteFltrEntry.setIndexNames(
    (0, "ACC-IPX", "accIpxRteFltrNeighbor"),
    (0, "ACC-IPX", "accIpxRteFltrNetwork"),
)
if mibBuilder.loadTexts:
    accIpxRteFltrEntry.setStatus("deprecated")
_AccIpxRteFltrNeighbor_Type = OctetString
_AccIpxRteFltrNeighbor_Object = MibTableColumn
accIpxRteFltrNeighbor = _AccIpxRteFltrNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 9, 3, 1, 1),
    _AccIpxRteFltrNeighbor_Type()
)
accIpxRteFltrNeighbor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxRteFltrNeighbor.setStatus("deprecated")
_AccIpxRteFltrNetwork_Type = OctetString
_AccIpxRteFltrNetwork_Object = MibTableColumn
accIpxRteFltrNetwork = _AccIpxRteFltrNetwork_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 9, 3, 1, 2),
    _AccIpxRteFltrNetwork_Type()
)
accIpxRteFltrNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxRteFltrNetwork.setStatus("deprecated")


class _AccIpxRteFltrAction_Type(Integer32):
    """Custom type accIpxRteFltrAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("reject", 2))
    )


_AccIpxRteFltrAction_Type.__name__ = "Integer32"
_AccIpxRteFltrAction_Object = MibTableColumn
accIpxRteFltrAction = _AccIpxRteFltrAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 9, 3, 1, 3),
    _AccIpxRteFltrAction_Type()
)
accIpxRteFltrAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxRteFltrAction.setStatus("deprecated")


class _AccIpxRteFltrStatus_Type(Integer32):
    """Custom type accIpxRteFltrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_AccIpxRteFltrStatus_Type.__name__ = "Integer32"
_AccIpxRteFltrStatus_Object = MibTableColumn
accIpxRteFltrStatus = _AccIpxRteFltrStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 9, 3, 1, 4),
    _AccIpxRteFltrStatus_Type()
)
accIpxRteFltrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxRteFltrStatus.setStatus("deprecated")
_AccIpxNetworkFilters_ObjectIdentity = ObjectIdentity
accIpxNetworkFilters = _AccIpxNetworkFilters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 10)
)


class _AccIpxNetFltrDefaultAction_Type(Integer32):
    """Custom type accIpxNetFltrDefaultAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discard", 0),
          ("highPriority", 3),
          ("lowPriority", 1),
          ("normalPriority", 2))
    )


_AccIpxNetFltrDefaultAction_Type.__name__ = "Integer32"
_AccIpxNetFltrDefaultAction_Object = MibScalar
accIpxNetFltrDefaultAction = _AccIpxNetFltrDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 10, 1),
    _AccIpxNetFltrDefaultAction_Type()
)
accIpxNetFltrDefaultAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNetFltrDefaultAction.setStatus("deprecated")
_OldIpxNetFltrTable_Object = MibTable
oldIpxNetFltrTable = _OldIpxNetFltrTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 10, 2)
)
if mibBuilder.loadTexts:
    oldIpxNetFltrTable.setStatus("deprecated")
_OldIpxNetFltrEntry_Object = MibTableRow
oldIpxNetFltrEntry = _OldIpxNetFltrEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 10, 2, 1)
)
oldIpxNetFltrEntry.setIndexNames(
    (0, "ACC-IPX", "oldIpxNetFltrDestination"),
    (0, "ACC-IPX", "oldIpxNetFltrSource"),
)
if mibBuilder.loadTexts:
    oldIpxNetFltrEntry.setStatus("deprecated")
_OldIpxNetFltrDestination_Type = OctetString
_OldIpxNetFltrDestination_Object = MibTableColumn
oldIpxNetFltrDestination = _OldIpxNetFltrDestination_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 10, 2, 1, 1),
    _OldIpxNetFltrDestination_Type()
)
oldIpxNetFltrDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oldIpxNetFltrDestination.setStatus("deprecated")
_OldIpxNetFltrSource_Type = OctetString
_OldIpxNetFltrSource_Object = MibTableColumn
oldIpxNetFltrSource = _OldIpxNetFltrSource_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 10, 2, 1, 2),
    _OldIpxNetFltrSource_Type()
)
oldIpxNetFltrSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oldIpxNetFltrSource.setStatus("deprecated")


class _OldIpxNetFltrAction_Type(Integer32):
    """Custom type oldIpxNetFltrAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discard", 0),
          ("highPriority", 3),
          ("lowPriority", 1),
          ("normalPriority", 2))
    )


_OldIpxNetFltrAction_Type.__name__ = "Integer32"
_OldIpxNetFltrAction_Object = MibTableColumn
oldIpxNetFltrAction = _OldIpxNetFltrAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 10, 2, 1, 3),
    _OldIpxNetFltrAction_Type()
)
oldIpxNetFltrAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oldIpxNetFltrAction.setStatus("deprecated")


class _OldIpxNetFltrStatus_Type(Integer32):
    """Custom type oldIpxNetFltrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_OldIpxNetFltrStatus_Type.__name__ = "Integer32"
_OldIpxNetFltrStatus_Object = MibTableColumn
oldIpxNetFltrStatus = _OldIpxNetFltrStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 10, 2, 1, 4),
    _OldIpxNetFltrStatus_Type()
)
oldIpxNetFltrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oldIpxNetFltrStatus.setStatus("deprecated")
_AccIpxNetFltrTable_Object = MibTable
accIpxNetFltrTable = _AccIpxNetFltrTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 10, 3)
)
if mibBuilder.loadTexts:
    accIpxNetFltrTable.setStatus("deprecated")
_AccIpxNetFltrEntry_Object = MibTableRow
accIpxNetFltrEntry = _AccIpxNetFltrEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 10, 3, 1)
)
accIpxNetFltrEntry.setIndexNames(
    (0, "ACC-IPX", "accIpxNetFltrDestination"),
    (0, "ACC-IPX", "accIpxNetFltrSource"),
    (0, "ACC-IPX", "accIpxNetFltrDestSkt"),
    (0, "ACC-IPX", "accIpxNetFltrSrcSkt"),
    (0, "ACC-IPX", "accIpxNetFltrPktType"),
)
if mibBuilder.loadTexts:
    accIpxNetFltrEntry.setStatus("deprecated")
_AccIpxNetFltrDestination_Type = OctetString
_AccIpxNetFltrDestination_Object = MibTableColumn
accIpxNetFltrDestination = _AccIpxNetFltrDestination_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 10, 3, 1, 1),
    _AccIpxNetFltrDestination_Type()
)
accIpxNetFltrDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNetFltrDestination.setStatus("deprecated")
_AccIpxNetFltrSource_Type = OctetString
_AccIpxNetFltrSource_Object = MibTableColumn
accIpxNetFltrSource = _AccIpxNetFltrSource_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 10, 3, 1, 2),
    _AccIpxNetFltrSource_Type()
)
accIpxNetFltrSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNetFltrSource.setStatus("deprecated")


class _AccIpxNetFltrAction_Type(Integer32):
    """Custom type accIpxNetFltrAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discard", 0),
          ("highPriority", 3),
          ("lowPriority", 1),
          ("normalPriority", 2))
    )


_AccIpxNetFltrAction_Type.__name__ = "Integer32"
_AccIpxNetFltrAction_Object = MibTableColumn
accIpxNetFltrAction = _AccIpxNetFltrAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 10, 3, 1, 3),
    _AccIpxNetFltrAction_Type()
)
accIpxNetFltrAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNetFltrAction.setStatus("deprecated")


class _AccIpxNetFltrStatus_Type(Integer32):
    """Custom type accIpxNetFltrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_AccIpxNetFltrStatus_Type.__name__ = "Integer32"
_AccIpxNetFltrStatus_Object = MibTableColumn
accIpxNetFltrStatus = _AccIpxNetFltrStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 10, 3, 1, 4),
    _AccIpxNetFltrStatus_Type()
)
accIpxNetFltrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNetFltrStatus.setStatus("deprecated")
_AccIpxNetFltrDestSkt_Type = OctetString
_AccIpxNetFltrDestSkt_Object = MibTableColumn
accIpxNetFltrDestSkt = _AccIpxNetFltrDestSkt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 10, 3, 1, 5),
    _AccIpxNetFltrDestSkt_Type()
)
accIpxNetFltrDestSkt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNetFltrDestSkt.setStatus("deprecated")
_AccIpxNetFltrSrcSkt_Type = OctetString
_AccIpxNetFltrSrcSkt_Object = MibTableColumn
accIpxNetFltrSrcSkt = _AccIpxNetFltrSrcSkt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 10, 3, 1, 6),
    _AccIpxNetFltrSrcSkt_Type()
)
accIpxNetFltrSrcSkt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNetFltrSrcSkt.setStatus("deprecated")
_AccIpxNetFltrPktType_Type = Integer32
_AccIpxNetFltrPktType_Object = MibTableColumn
accIpxNetFltrPktType = _AccIpxNetFltrPktType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 10, 3, 1, 7),
    _AccIpxNetFltrPktType_Type()
)
accIpxNetFltrPktType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNetFltrPktType.setStatus("deprecated")
_AccIpxHostFilters_ObjectIdentity = ObjectIdentity
accIpxHostFilters = _AccIpxHostFilters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 11)
)


class _AccIpxHostFltrDefaultAction_Type(Integer32):
    """Custom type accIpxHostFltrDefaultAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discard", 0),
          ("highPriority", 3),
          ("lowPriority", 1),
          ("normalPriority", 2))
    )


_AccIpxHostFltrDefaultAction_Type.__name__ = "Integer32"
_AccIpxHostFltrDefaultAction_Object = MibScalar
accIpxHostFltrDefaultAction = _AccIpxHostFltrDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 11, 1),
    _AccIpxHostFltrDefaultAction_Type()
)
accIpxHostFltrDefaultAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxHostFltrDefaultAction.setStatus("deprecated")
_AccIpxHostFltrTable_Object = MibTable
accIpxHostFltrTable = _AccIpxHostFltrTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 11, 2)
)
if mibBuilder.loadTexts:
    accIpxHostFltrTable.setStatus("deprecated")
_AccIpxHostFltrEntry_Object = MibTableRow
accIpxHostFltrEntry = _AccIpxHostFltrEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 11, 2, 1)
)
accIpxHostFltrEntry.setIndexNames(
    (0, "ACC-IPX", "accIpxHostFltrId"),
    (0, "ACC-IPX", "accIpxHostFltrSocket"),
    (0, "ACC-IPX", "accIpxHostFltrPepClient"),
)
if mibBuilder.loadTexts:
    accIpxHostFltrEntry.setStatus("deprecated")
_AccIpxHostFltrId_Type = OctetString
_AccIpxHostFltrId_Object = MibTableColumn
accIpxHostFltrId = _AccIpxHostFltrId_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 11, 2, 1, 1),
    _AccIpxHostFltrId_Type()
)
accIpxHostFltrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxHostFltrId.setStatus("deprecated")
_AccIpxHostFltrSocket_Type = OctetString
_AccIpxHostFltrSocket_Object = MibTableColumn
accIpxHostFltrSocket = _AccIpxHostFltrSocket_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 11, 2, 1, 2),
    _AccIpxHostFltrSocket_Type()
)
accIpxHostFltrSocket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxHostFltrSocket.setStatus("deprecated")
_AccIpxHostFltrPepClient_Type = OctetString
_AccIpxHostFltrPepClient_Object = MibTableColumn
accIpxHostFltrPepClient = _AccIpxHostFltrPepClient_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 11, 2, 1, 3),
    _AccIpxHostFltrPepClient_Type()
)
accIpxHostFltrPepClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxHostFltrPepClient.setStatus("deprecated")


class _AccIpxHostFltrAction_Type(Integer32):
    """Custom type accIpxHostFltrAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discard", 0),
          ("highPriority", 3),
          ("lowPriority", 1),
          ("normalPriority", 2))
    )


_AccIpxHostFltrAction_Type.__name__ = "Integer32"
_AccIpxHostFltrAction_Object = MibTableColumn
accIpxHostFltrAction = _AccIpxHostFltrAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 11, 2, 1, 4),
    _AccIpxHostFltrAction_Type()
)
accIpxHostFltrAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxHostFltrAction.setStatus("deprecated")


class _AccIpxHostFltrStatus_Type(Integer32):
    """Custom type accIpxHostFltrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_AccIpxHostFltrStatus_Type.__name__ = "Integer32"
_AccIpxHostFltrStatus_Object = MibTableColumn
accIpxHostFltrStatus = _AccIpxHostFltrStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 11, 2, 1, 5),
    _AccIpxHostFltrStatus_Type()
)
accIpxHostFltrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxHostFltrStatus.setStatus("deprecated")
_AccIpxSapFilters_ObjectIdentity = ObjectIdentity
accIpxSapFilters = _AccIpxSapFilters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 12)
)


class _AccIpxSapFltrDefault_Type(Integer32):
    """Custom type accIpxSapFltrDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("reject", 2))
    )


_AccIpxSapFltrDefault_Type.__name__ = "Integer32"
_AccIpxSapFltrDefault_Object = MibScalar
accIpxSapFltrDefault = _AccIpxSapFltrDefault_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 12, 1),
    _AccIpxSapFltrDefault_Type()
)
accIpxSapFltrDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxSapFltrDefault.setStatus("deprecated")
_AccIpxSapFltrTable_Object = MibTable
accIpxSapFltrTable = _AccIpxSapFltrTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 12, 2)
)
if mibBuilder.loadTexts:
    accIpxSapFltrTable.setStatus("deprecated")
_AccIpxSapFltrEntry_Object = MibTableRow
accIpxSapFltrEntry = _AccIpxSapFltrEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 12, 2, 1)
)
accIpxSapFltrEntry.setIndexNames(
    (0, "ACC-IPX", "accIpxSapFltrSrvType"),
    (0, "ACC-IPX", "accIpxSapFltrSrvName"),
)
if mibBuilder.loadTexts:
    accIpxSapFltrEntry.setStatus("deprecated")
_AccIpxSapFltrSrvType_Type = OctetString
_AccIpxSapFltrSrvType_Object = MibTableColumn
accIpxSapFltrSrvType = _AccIpxSapFltrSrvType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 12, 2, 1, 1),
    _AccIpxSapFltrSrvType_Type()
)
accIpxSapFltrSrvType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxSapFltrSrvType.setStatus("deprecated")
_AccIpxSapFltrSrvName_Type = OctetString
_AccIpxSapFltrSrvName_Object = MibTableColumn
accIpxSapFltrSrvName = _AccIpxSapFltrSrvName_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 12, 2, 1, 2),
    _AccIpxSapFltrSrvName_Type()
)
accIpxSapFltrSrvName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxSapFltrSrvName.setStatus("deprecated")


class _AccIpxSapFltrAction_Type(Integer32):
    """Custom type accIpxSapFltrAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("reject", 2))
    )


_AccIpxSapFltrAction_Type.__name__ = "Integer32"
_AccIpxSapFltrAction_Object = MibTableColumn
accIpxSapFltrAction = _AccIpxSapFltrAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 12, 2, 1, 3),
    _AccIpxSapFltrAction_Type()
)
accIpxSapFltrAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxSapFltrAction.setStatus("deprecated")


class _AccIpxSapFltrStatus_Type(Integer32):
    """Custom type accIpxSapFltrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_AccIpxSapFltrStatus_Type.__name__ = "Integer32"
_AccIpxSapFltrStatus_Object = MibTableColumn
accIpxSapFltrStatus = _AccIpxSapFltrStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 12, 2, 1, 4),
    _AccIpxSapFltrStatus_Type()
)
accIpxSapFltrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxSapFltrStatus.setStatus("deprecated")
_AccIpxNetWdParms_ObjectIdentity = ObjectIdentity
accIpxNetWdParms = _AccIpxNetWdParms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 13)
)


class _AccIpxWdProxyDuration_Type(Integer32):
    """Custom type accIpxWdProxyDuration based on Integer32"""
    defaultValue = 86400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_AccIpxWdProxyDuration_Type.__name__ = "Integer32"
_AccIpxWdProxyDuration_Object = MibScalar
accIpxWdProxyDuration = _AccIpxWdProxyDuration_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 13, 1),
    _AccIpxWdProxyDuration_Type()
)
accIpxWdProxyDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxWdProxyDuration.setStatus("mandatory")


class _AccIpxWdHoldPeriod_Type(Integer32):
    """Custom type accIpxWdHoldPeriod based on Integer32"""
    defaultValue = 960

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(960, 60600),
    )


_AccIpxWdHoldPeriod_Type.__name__ = "Integer32"
_AccIpxWdHoldPeriod_Object = MibScalar
accIpxWdHoldPeriod = _AccIpxWdHoldPeriod_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 13, 2),
    _AccIpxWdHoldPeriod_Type()
)
accIpxWdHoldPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxWdHoldPeriod.setStatus("mandatory")


class _AccIpxWdMaxSessions_Type(Integer32):
    """Custom type accIpxWdMaxSessions based on Integer32"""
    defaultValue = 1024

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_AccIpxWdMaxSessions_Type.__name__ = "Integer32"
_AccIpxWdMaxSessions_Object = MibScalar
accIpxWdMaxSessions = _AccIpxWdMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 13, 3),
    _AccIpxWdMaxSessions_Type()
)
accIpxWdMaxSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxWdMaxSessions.setStatus("mandatory")


class _AccIpxWdDiagLevel_Type(Integer32):
    """Custom type accIpxWdDiagLevel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AccIpxWdDiagLevel_Type.__name__ = "Integer32"
_AccIpxWdDiagLevel_Object = MibScalar
accIpxWdDiagLevel = _AccIpxWdDiagLevel_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 13, 4),
    _AccIpxWdDiagLevel_Type()
)
accIpxWdDiagLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxWdDiagLevel.setStatus("mandatory")
_AccIpxWdCurrentDropDead_Type = TimeTicks
_AccIpxWdCurrentDropDead_Object = MibScalar
accIpxWdCurrentDropDead = _AccIpxWdCurrentDropDead_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 13, 5),
    _AccIpxWdCurrentDropDead_Type()
)
accIpxWdCurrentDropDead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxWdCurrentDropDead.setStatus("mandatory")


class _AccIpxWdIpxSessionCnt_Type(Integer32):
    """Custom type accIpxWdIpxSessionCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AccIpxWdIpxSessionCnt_Type.__name__ = "Integer32"
_AccIpxWdIpxSessionCnt_Object = MibScalar
accIpxWdIpxSessionCnt = _AccIpxWdIpxSessionCnt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 13, 6),
    _AccIpxWdIpxSessionCnt_Type()
)
accIpxWdIpxSessionCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxWdIpxSessionCnt.setStatus("mandatory")


class _AccIpxWdSpxSessionCnt_Type(Integer32):
    """Custom type accIpxWdSpxSessionCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AccIpxWdSpxSessionCnt_Type.__name__ = "Integer32"
_AccIpxWdSpxSessionCnt_Object = MibScalar
accIpxWdSpxSessionCnt = _AccIpxWdSpxSessionCnt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 13, 7),
    _AccIpxWdSpxSessionCnt_Type()
)
accIpxWdSpxSessionCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxWdSpxSessionCnt.setStatus("mandatory")
_AccIpxWdSession_ObjectIdentity = ObjectIdentity
accIpxWdSession = _AccIpxWdSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 14)
)
_AccIpxWdSessTable_Object = MibTable
accIpxWdSessTable = _AccIpxWdSessTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 14, 1)
)
if mibBuilder.loadTexts:
    accIpxWdSessTable.setStatus("mandatory")
_AccIpxWdSessEntry_Object = MibTableRow
accIpxWdSessEntry = _AccIpxWdSessEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 14, 1, 1)
)
accIpxWdSessEntry.setIndexNames(
    (0, "ACC-IPX", "accIpxWdSessionId"),
)
if mibBuilder.loadTexts:
    accIpxWdSessEntry.setStatus("mandatory")


class _AccIpxWdSessionId_Type(Integer32):
    """Custom type accIpxWdSessionId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AccIpxWdSessionId_Type.__name__ = "Integer32"
_AccIpxWdSessionId_Object = MibTableColumn
accIpxWdSessionId = _AccIpxWdSessionId_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 14, 1, 1, 1),
    _AccIpxWdSessionId_Type()
)
accIpxWdSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxWdSessionId.setStatus("mandatory")


class _AccIpxWdState_Type(Integer32):
    """Custom type accIpxWdState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dead", 2),
          ("dying", 1),
          ("operational", 0))
    )


_AccIpxWdState_Type.__name__ = "Integer32"
_AccIpxWdState_Object = MibTableColumn
accIpxWdState = _AccIpxWdState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 14, 1, 1, 2),
    _AccIpxWdState_Type()
)
accIpxWdState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxWdState.setStatus("mandatory")
_AccIpxWdLastSeen_Type = TimeTicks
_AccIpxWdLastSeen_Object = MibTableColumn
accIpxWdLastSeen = _AccIpxWdLastSeen_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 14, 1, 1, 3),
    _AccIpxWdLastSeen_Type()
)
accIpxWdLastSeen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxWdLastSeen.setStatus("mandatory")
_AccIpxWdClientNet_Type = OctetString
_AccIpxWdClientNet_Object = MibTableColumn
accIpxWdClientNet = _AccIpxWdClientNet_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 14, 1, 1, 4),
    _AccIpxWdClientNet_Type()
)
accIpxWdClientNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxWdClientNet.setStatus("mandatory")
_AccIpxWdClientHost_Type = OctetString
_AccIpxWdClientHost_Object = MibTableColumn
accIpxWdClientHost = _AccIpxWdClientHost_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 14, 1, 1, 5),
    _AccIpxWdClientHost_Type()
)
accIpxWdClientHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxWdClientHost.setStatus("mandatory")
_AccIpxWdDropDead_Type = TimeTicks
_AccIpxWdDropDead_Object = MibTableColumn
accIpxWdDropDead = _AccIpxWdDropDead_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 14, 1, 1, 6),
    _AccIpxWdDropDead_Type()
)
accIpxWdDropDead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxWdDropDead.setStatus("mandatory")
_AccIpxWdServerNet_Type = OctetString
_AccIpxWdServerNet_Object = MibTableColumn
accIpxWdServerNet = _AccIpxWdServerNet_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 14, 1, 1, 7),
    _AccIpxWdServerNet_Type()
)
accIpxWdServerNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxWdServerNet.setStatus("mandatory")
_AccIpxWdServerHost_Type = OctetString
_AccIpxWdServerHost_Object = MibTableColumn
accIpxWdServerHost = _AccIpxWdServerHost_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 14, 1, 1, 8),
    _AccIpxWdServerHost_Type()
)
accIpxWdServerHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxWdServerHost.setStatus("mandatory")
_AccIpxSpxWdSession_ObjectIdentity = ObjectIdentity
accIpxSpxWdSession = _AccIpxSpxWdSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 15)
)
_AccIpxSpxWdSessTable_Object = MibTable
accIpxSpxWdSessTable = _AccIpxSpxWdSessTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 15, 1)
)
if mibBuilder.loadTexts:
    accIpxSpxWdSessTable.setStatus("mandatory")
_AccIpxSpxWdSessEntry_Object = MibTableRow
accIpxSpxWdSessEntry = _AccIpxSpxWdSessEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 15, 1, 1)
)
accIpxSpxWdSessEntry.setIndexNames(
    (0, "ACC-IPX", "accIpxSpxWdSrcSessionId"),
    (0, "ACC-IPX", "accIpxSpxWdDstSessionId"),
)
if mibBuilder.loadTexts:
    accIpxSpxWdSessEntry.setStatus("mandatory")


class _AccIpxSpxWdSrcSessionId_Type(Integer32):
    """Custom type accIpxSpxWdSrcSessionId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AccIpxSpxWdSrcSessionId_Type.__name__ = "Integer32"
_AccIpxSpxWdSrcSessionId_Object = MibTableColumn
accIpxSpxWdSrcSessionId = _AccIpxSpxWdSrcSessionId_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 15, 1, 1, 1),
    _AccIpxSpxWdSrcSessionId_Type()
)
accIpxSpxWdSrcSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxSpxWdSrcSessionId.setStatus("mandatory")


class _AccIpxSpxWdDstSessionId_Type(Integer32):
    """Custom type accIpxSpxWdDstSessionId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AccIpxSpxWdDstSessionId_Type.__name__ = "Integer32"
_AccIpxSpxWdDstSessionId_Object = MibTableColumn
accIpxSpxWdDstSessionId = _AccIpxSpxWdDstSessionId_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 15, 1, 1, 2),
    _AccIpxSpxWdDstSessionId_Type()
)
accIpxSpxWdDstSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxSpxWdDstSessionId.setStatus("mandatory")


class _AccIpxSpxWdState_Type(Integer32):
    """Custom type accIpxSpxWdState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("dead", 3),
          ("dying", 2),
          ("proxy", 0))
    )


_AccIpxSpxWdState_Type.__name__ = "Integer32"
_AccIpxSpxWdState_Object = MibTableColumn
accIpxSpxWdState = _AccIpxSpxWdState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 15, 1, 1, 3),
    _AccIpxSpxWdState_Type()
)
accIpxSpxWdState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxSpxWdState.setStatus("mandatory")
_AccIpxSpxWdClientNet_Type = OctetString
_AccIpxSpxWdClientNet_Object = MibTableColumn
accIpxSpxWdClientNet = _AccIpxSpxWdClientNet_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 15, 1, 1, 4),
    _AccIpxSpxWdClientNet_Type()
)
accIpxSpxWdClientNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxSpxWdClientNet.setStatus("mandatory")
_AccIpxSpxWdClientHost_Type = OctetString
_AccIpxSpxWdClientHost_Object = MibTableColumn
accIpxSpxWdClientHost = _AccIpxSpxWdClientHost_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 15, 1, 1, 5),
    _AccIpxSpxWdClientHost_Type()
)
accIpxSpxWdClientHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxSpxWdClientHost.setStatus("mandatory")
_AccIpxSpxWdLastSeen_Type = TimeTicks
_AccIpxSpxWdLastSeen_Object = MibTableColumn
accIpxSpxWdLastSeen = _AccIpxSpxWdLastSeen_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 15, 1, 1, 6),
    _AccIpxSpxWdLastSeen_Type()
)
accIpxSpxWdLastSeen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxSpxWdLastSeen.setStatus("mandatory")
_AccIpxSpxWdServerNet_Type = OctetString
_AccIpxSpxWdServerNet_Object = MibTableColumn
accIpxSpxWdServerNet = _AccIpxSpxWdServerNet_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 15, 1, 1, 7),
    _AccIpxSpxWdServerNet_Type()
)
accIpxSpxWdServerNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxSpxWdServerNet.setStatus("mandatory")
_AccIpxSpxWdServerHost_Type = OctetString
_AccIpxSpxWdServerHost_Object = MibTableColumn
accIpxSpxWdServerHost = _AccIpxSpxWdServerHost_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 15, 1, 1, 8),
    _AccIpxSpxWdServerHost_Type()
)
accIpxSpxWdServerHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxSpxWdServerHost.setStatus("mandatory")
_AccIpxSpxWdDropDead_Type = TimeTicks
_AccIpxSpxWdDropDead_Object = MibTableColumn
accIpxSpxWdDropDead = _AccIpxSpxWdDropDead_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 15, 1, 1, 9),
    _AccIpxSpxWdDropDead_Type()
)
accIpxSpxWdDropDead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxSpxWdDropDead.setStatus("mandatory")


class _AccIpxSpxWdSrcSeqNo_Type(Integer32):
    """Custom type accIpxSpxWdSrcSeqNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AccIpxSpxWdSrcSeqNo_Type.__name__ = "Integer32"
_AccIpxSpxWdSrcSeqNo_Object = MibTableColumn
accIpxSpxWdSrcSeqNo = _AccIpxSpxWdSrcSeqNo_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 15, 1, 1, 10),
    _AccIpxSpxWdSrcSeqNo_Type()
)
accIpxSpxWdSrcSeqNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxSpxWdSrcSeqNo.setStatus("mandatory")


class _AccIpxSpxWdDstSeqNo_Type(Integer32):
    """Custom type accIpxSpxWdDstSeqNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AccIpxSpxWdDstSeqNo_Type.__name__ = "Integer32"
_AccIpxSpxWdDstSeqNo_Object = MibTableColumn
accIpxSpxWdDstSeqNo = _AccIpxSpxWdDstSeqNo_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 15, 1, 1, 11),
    _AccIpxSpxWdDstSeqNo_Type()
)
accIpxSpxWdDstSeqNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxSpxWdDstSeqNo.setStatus("mandatory")


class _AccIpxSpxWdAckDiscards_Type(Integer32):
    """Custom type accIpxSpxWdAckDiscards based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AccIpxSpxWdAckDiscards_Type.__name__ = "Integer32"
_AccIpxSpxWdAckDiscards_Object = MibTableColumn
accIpxSpxWdAckDiscards = _AccIpxSpxWdAckDiscards_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 15, 1, 1, 12),
    _AccIpxSpxWdAckDiscards_Type()
)
accIpxSpxWdAckDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxSpxWdAckDiscards.setStatus("mandatory")


class _AccIpxSpxWdSrcAckNo_Type(Integer32):
    """Custom type accIpxSpxWdSrcAckNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AccIpxSpxWdSrcAckNo_Type.__name__ = "Integer32"
_AccIpxSpxWdSrcAckNo_Object = MibTableColumn
accIpxSpxWdSrcAckNo = _AccIpxSpxWdSrcAckNo_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 15, 1, 1, 13),
    _AccIpxSpxWdSrcAckNo_Type()
)
accIpxSpxWdSrcAckNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxSpxWdSrcAckNo.setStatus("mandatory")


class _AccIpxSpxWdDstAckNo_Type(Integer32):
    """Custom type accIpxSpxWdDstAckNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AccIpxSpxWdDstAckNo_Type.__name__ = "Integer32"
_AccIpxSpxWdDstAckNo_Object = MibTableColumn
accIpxSpxWdDstAckNo = _AccIpxSpxWdDstAckNo_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 15, 1, 1, 14),
    _AccIpxSpxWdDstAckNo_Type()
)
accIpxSpxWdDstAckNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxSpxWdDstAckNo.setStatus("mandatory")
_AccIpxNamedRteFilters_ObjectIdentity = ObjectIdentity
accIpxNamedRteFilters = _AccIpxNamedRteFilters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 16)
)


class _AccIpxNamedRteFltrDefaultAction_Type(Integer32):
    """Custom type accIpxNamedRteFltrDefaultAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("reject", 2))
    )


_AccIpxNamedRteFltrDefaultAction_Type.__name__ = "Integer32"
_AccIpxNamedRteFltrDefaultAction_Object = MibScalar
accIpxNamedRteFltrDefaultAction = _AccIpxNamedRteFltrDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 16, 1),
    _AccIpxNamedRteFltrDefaultAction_Type()
)
accIpxNamedRteFltrDefaultAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNamedRteFltrDefaultAction.setStatus("mandatory")
_AccIpxNamedRteFltrTable_Object = MibTable
accIpxNamedRteFltrTable = _AccIpxNamedRteFltrTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 16, 2)
)
if mibBuilder.loadTexts:
    accIpxNamedRteFltrTable.setStatus("mandatory")
_AccIpxNamedRteFltrEntry_Object = MibTableRow
accIpxNamedRteFltrEntry = _AccIpxNamedRteFltrEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 16, 2, 1)
)
accIpxNamedRteFltrEntry.setIndexNames(
    (0, "ACC-IPX", "accIpxNamedRteFltrName"),
)
if mibBuilder.loadTexts:
    accIpxNamedRteFltrEntry.setStatus("mandatory")
_AccIpxNamedRteFltrNeighbor_Type = OctetString
_AccIpxNamedRteFltrNeighbor_Object = MibTableColumn
accIpxNamedRteFltrNeighbor = _AccIpxNamedRteFltrNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 16, 2, 1, 1),
    _AccIpxNamedRteFltrNeighbor_Type()
)
accIpxNamedRteFltrNeighbor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNamedRteFltrNeighbor.setStatus("mandatory")
_AccIpxNamedRteFltrNetwork_Type = OctetString
_AccIpxNamedRteFltrNetwork_Object = MibTableColumn
accIpxNamedRteFltrNetwork = _AccIpxNamedRteFltrNetwork_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 16, 2, 1, 2),
    _AccIpxNamedRteFltrNetwork_Type()
)
accIpxNamedRteFltrNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNamedRteFltrNetwork.setStatus("mandatory")


class _AccIpxNamedRteFltrAction_Type(Integer32):
    """Custom type accIpxNamedRteFltrAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("reject", 2))
    )


_AccIpxNamedRteFltrAction_Type.__name__ = "Integer32"
_AccIpxNamedRteFltrAction_Object = MibTableColumn
accIpxNamedRteFltrAction = _AccIpxNamedRteFltrAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 16, 2, 1, 3),
    _AccIpxNamedRteFltrAction_Type()
)
accIpxNamedRteFltrAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNamedRteFltrAction.setStatus("mandatory")


class _AccIpxNamedRteFltrStatus_Type(Integer32):
    """Custom type accIpxNamedRteFltrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_AccIpxNamedRteFltrStatus_Type.__name__ = "Integer32"
_AccIpxNamedRteFltrStatus_Object = MibTableColumn
accIpxNamedRteFltrStatus = _AccIpxNamedRteFltrStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 16, 2, 1, 4),
    _AccIpxNamedRteFltrStatus_Type()
)
accIpxNamedRteFltrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNamedRteFltrStatus.setStatus("mandatory")
_AccIpxNamedRteFltrName_Type = OctetString
_AccIpxNamedRteFltrName_Object = MibTableColumn
accIpxNamedRteFltrName = _AccIpxNamedRteFltrName_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 16, 2, 1, 5),
    _AccIpxNamedRteFltrName_Type()
)
accIpxNamedRteFltrName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNamedRteFltrName.setStatus("mandatory")


class _AccIpxNamedRteFltrPktDir_Type(Integer32):
    """Custom type accIpxNamedRteFltrPktDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input", 1),
          ("output", 2))
    )


_AccIpxNamedRteFltrPktDir_Type.__name__ = "Integer32"
_AccIpxNamedRteFltrPktDir_Object = MibTableColumn
accIpxNamedRteFltrPktDir = _AccIpxNamedRteFltrPktDir_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 16, 2, 1, 6),
    _AccIpxNamedRteFltrPktDir_Type()
)
accIpxNamedRteFltrPktDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNamedRteFltrPktDir.setStatus("mandatory")
_AccIpxNamedRteFltrMatches_Type = Counter32
_AccIpxNamedRteFltrMatches_Object = MibTableColumn
accIpxNamedRteFltrMatches = _AccIpxNamedRteFltrMatches_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 16, 2, 1, 7),
    _AccIpxNamedRteFltrMatches_Type()
)
accIpxNamedRteFltrMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxNamedRteFltrMatches.setStatus("mandatory")
_AccIpxNamedRteFltrLastMatch_Type = TimeTicks
_AccIpxNamedRteFltrLastMatch_Object = MibTableColumn
accIpxNamedRteFltrLastMatch = _AccIpxNamedRteFltrLastMatch_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 16, 2, 1, 8),
    _AccIpxNamedRteFltrLastMatch_Type()
)
accIpxNamedRteFltrLastMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxNamedRteFltrLastMatch.setStatus("mandatory")
_AccIpxNamedRteFltrNetMask_Type = OctetString
_AccIpxNamedRteFltrNetMask_Object = MibTableColumn
accIpxNamedRteFltrNetMask = _AccIpxNamedRteFltrNetMask_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 16, 2, 1, 9),
    _AccIpxNamedRteFltrNetMask_Type()
)
accIpxNamedRteFltrNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNamedRteFltrNetMask.setStatus("mandatory")
_AccIpxRteFltrApplTable_Object = MibTable
accIpxRteFltrApplTable = _AccIpxRteFltrApplTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 16, 3)
)
if mibBuilder.loadTexts:
    accIpxRteFltrApplTable.setStatus("mandatory")
_AccIpxRteFltrApplEntry_Object = MibTableRow
accIpxRteFltrApplEntry = _AccIpxRteFltrApplEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 16, 3, 1)
)
accIpxRteFltrApplEntry.setIndexNames(
    (0, "ACC-IPX", "accIpxRteFltrApplIfIndex"),
    (0, "ACC-IPX", "accIpxRteFltrApplPktDir"),
    (0, "ACC-IPX", "accIpxRteFltrApplSeqNum"),
)
if mibBuilder.loadTexts:
    accIpxRteFltrApplEntry.setStatus("mandatory")
_AccIpxRteFltrApplIfIndex_Type = Integer32
_AccIpxRteFltrApplIfIndex_Object = MibTableColumn
accIpxRteFltrApplIfIndex = _AccIpxRteFltrApplIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 16, 3, 1, 1),
    _AccIpxRteFltrApplIfIndex_Type()
)
accIpxRteFltrApplIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxRteFltrApplIfIndex.setStatus("mandatory")


class _AccIpxRteFltrApplPktDir_Type(Integer32):
    """Custom type accIpxRteFltrApplPktDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("global", 3),
          ("input", 1),
          ("output", 2))
    )


_AccIpxRteFltrApplPktDir_Type.__name__ = "Integer32"
_AccIpxRteFltrApplPktDir_Object = MibTableColumn
accIpxRteFltrApplPktDir = _AccIpxRteFltrApplPktDir_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 16, 3, 1, 2),
    _AccIpxRteFltrApplPktDir_Type()
)
accIpxRteFltrApplPktDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxRteFltrApplPktDir.setStatus("mandatory")
_AccIpxRteFltrApplSeqNum_Type = Integer32
_AccIpxRteFltrApplSeqNum_Object = MibTableColumn
accIpxRteFltrApplSeqNum = _AccIpxRteFltrApplSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 16, 3, 1, 3),
    _AccIpxRteFltrApplSeqNum_Type()
)
accIpxRteFltrApplSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxRteFltrApplSeqNum.setStatus("mandatory")
_AccIpxRteFltrApplName_Type = DisplayString
_AccIpxRteFltrApplName_Object = MibTableColumn
accIpxRteFltrApplName = _AccIpxRteFltrApplName_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 16, 3, 1, 4),
    _AccIpxRteFltrApplName_Type()
)
accIpxRteFltrApplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxRteFltrApplName.setStatus("mandatory")
_AccIpxRteFltrApplMatches_Type = Counter32
_AccIpxRteFltrApplMatches_Object = MibTableColumn
accIpxRteFltrApplMatches = _AccIpxRteFltrApplMatches_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 16, 3, 1, 5),
    _AccIpxRteFltrApplMatches_Type()
)
accIpxRteFltrApplMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxRteFltrApplMatches.setStatus("mandatory")
_AccIpxRteFltrApplLastMatch_Type = TimeTicks
_AccIpxRteFltrApplLastMatch_Object = MibTableColumn
accIpxRteFltrApplLastMatch = _AccIpxRteFltrApplLastMatch_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 16, 3, 1, 6),
    _AccIpxRteFltrApplLastMatch_Type()
)
accIpxRteFltrApplLastMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxRteFltrApplLastMatch.setStatus("mandatory")
_AccIpxNamedNetFilters_ObjectIdentity = ObjectIdentity
accIpxNamedNetFilters = _AccIpxNamedNetFilters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 17)
)


class _AccIpxNamedNetFltrDefault_Type(Integer32):
    """Custom type accIpxNamedNetFltrDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discard", 0),
          ("highPriority", 3),
          ("lowPriority", 1),
          ("normalPriority", 2))
    )


_AccIpxNamedNetFltrDefault_Type.__name__ = "Integer32"
_AccIpxNamedNetFltrDefault_Object = MibScalar
accIpxNamedNetFltrDefault = _AccIpxNamedNetFltrDefault_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 17, 1),
    _AccIpxNamedNetFltrDefault_Type()
)
accIpxNamedNetFltrDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNamedNetFltrDefault.setStatus("mandatory")
_AccIpxNamedNetFltrTable_Object = MibTable
accIpxNamedNetFltrTable = _AccIpxNamedNetFltrTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 17, 2)
)
if mibBuilder.loadTexts:
    accIpxNamedNetFltrTable.setStatus("mandatory")
_AccIpxNamedNetFltrEntry_Object = MibTableRow
accIpxNamedNetFltrEntry = _AccIpxNamedNetFltrEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 17, 2, 1)
)
accIpxNamedNetFltrEntry.setIndexNames(
    (0, "ACC-IPX", "accIpxNamedNetFltrName"),
)
if mibBuilder.loadTexts:
    accIpxNamedNetFltrEntry.setStatus("mandatory")
_AccIpxNamedNetFltrDestination_Type = OctetString
_AccIpxNamedNetFltrDestination_Object = MibTableColumn
accIpxNamedNetFltrDestination = _AccIpxNamedNetFltrDestination_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 17, 2, 1, 1),
    _AccIpxNamedNetFltrDestination_Type()
)
accIpxNamedNetFltrDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNamedNetFltrDestination.setStatus("mandatory")
_AccIpxNamedNetFltrSource_Type = OctetString
_AccIpxNamedNetFltrSource_Object = MibTableColumn
accIpxNamedNetFltrSource = _AccIpxNamedNetFltrSource_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 17, 2, 1, 2),
    _AccIpxNamedNetFltrSource_Type()
)
accIpxNamedNetFltrSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNamedNetFltrSource.setStatus("mandatory")


class _AccIpxNamedNetFltrAction_Type(Integer32):
    """Custom type accIpxNamedNetFltrAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discard", 0),
          ("highPriority", 3),
          ("lowPriority", 1),
          ("normalPriority", 2))
    )


_AccIpxNamedNetFltrAction_Type.__name__ = "Integer32"
_AccIpxNamedNetFltrAction_Object = MibTableColumn
accIpxNamedNetFltrAction = _AccIpxNamedNetFltrAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 17, 2, 1, 3),
    _AccIpxNamedNetFltrAction_Type()
)
accIpxNamedNetFltrAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNamedNetFltrAction.setStatus("deprecated")


class _AccIpxNamedNetFltrStatus_Type(Integer32):
    """Custom type accIpxNamedNetFltrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_AccIpxNamedNetFltrStatus_Type.__name__ = "Integer32"
_AccIpxNamedNetFltrStatus_Object = MibTableColumn
accIpxNamedNetFltrStatus = _AccIpxNamedNetFltrStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 17, 2, 1, 4),
    _AccIpxNamedNetFltrStatus_Type()
)
accIpxNamedNetFltrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNamedNetFltrStatus.setStatus("mandatory")
_AccIpxNamedNetFltrDestSkt_Type = OctetString
_AccIpxNamedNetFltrDestSkt_Object = MibTableColumn
accIpxNamedNetFltrDestSkt = _AccIpxNamedNetFltrDestSkt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 17, 2, 1, 5),
    _AccIpxNamedNetFltrDestSkt_Type()
)
accIpxNamedNetFltrDestSkt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNamedNetFltrDestSkt.setStatus("mandatory")
_AccIpxNamedNetFltrSrcSkt_Type = OctetString
_AccIpxNamedNetFltrSrcSkt_Object = MibTableColumn
accIpxNamedNetFltrSrcSkt = _AccIpxNamedNetFltrSrcSkt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 17, 2, 1, 6),
    _AccIpxNamedNetFltrSrcSkt_Type()
)
accIpxNamedNetFltrSrcSkt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNamedNetFltrSrcSkt.setStatus("mandatory")
_AccIpxNamedNetFltrType_Type = Integer32
_AccIpxNamedNetFltrType_Object = MibTableColumn
accIpxNamedNetFltrType = _AccIpxNamedNetFltrType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 17, 2, 1, 7),
    _AccIpxNamedNetFltrType_Type()
)
accIpxNamedNetFltrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNamedNetFltrType.setStatus("mandatory")
_AccIpxNamedNetFltrName_Type = OctetString
_AccIpxNamedNetFltrName_Object = MibTableColumn
accIpxNamedNetFltrName = _AccIpxNamedNetFltrName_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 17, 2, 1, 8),
    _AccIpxNamedNetFltrName_Type()
)
accIpxNamedNetFltrName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNamedNetFltrName.setStatus("mandatory")


class _AccIpxNamedNetFltrPktDir_Type(Integer32):
    """Custom type accIpxNamedNetFltrPktDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input", 1),
          ("output", 2))
    )


_AccIpxNamedNetFltrPktDir_Type.__name__ = "Integer32"
_AccIpxNamedNetFltrPktDir_Object = MibTableColumn
accIpxNamedNetFltrPktDir = _AccIpxNamedNetFltrPktDir_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 17, 2, 1, 9),
    _AccIpxNamedNetFltrPktDir_Type()
)
accIpxNamedNetFltrPktDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNamedNetFltrPktDir.setStatus("mandatory")
_AccIpxNamedNetFltrMatches_Type = Counter32
_AccIpxNamedNetFltrMatches_Object = MibTableColumn
accIpxNamedNetFltrMatches = _AccIpxNamedNetFltrMatches_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 17, 2, 1, 10),
    _AccIpxNamedNetFltrMatches_Type()
)
accIpxNamedNetFltrMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxNamedNetFltrMatches.setStatus("mandatory")
_AccIpxNamedNetFltrLastMatch_Type = TimeTicks
_AccIpxNamedNetFltrLastMatch_Object = MibTableColumn
accIpxNamedNetFltrLastMatch = _AccIpxNamedNetFltrLastMatch_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 17, 2, 1, 11),
    _AccIpxNamedNetFltrLastMatch_Type()
)
accIpxNamedNetFltrLastMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxNamedNetFltrLastMatch.setStatus("mandatory")
_AccIpxNamedNetFltrDestMask_Type = OctetString
_AccIpxNamedNetFltrDestMask_Object = MibTableColumn
accIpxNamedNetFltrDestMask = _AccIpxNamedNetFltrDestMask_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 17, 2, 1, 12),
    _AccIpxNamedNetFltrDestMask_Type()
)
accIpxNamedNetFltrDestMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNamedNetFltrDestMask.setStatus("mandatory")
_AccIpxNamedNetFltrSrcMask_Type = OctetString
_AccIpxNamedNetFltrSrcMask_Object = MibTableColumn
accIpxNamedNetFltrSrcMask = _AccIpxNamedNetFltrSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 17, 2, 1, 13),
    _AccIpxNamedNetFltrSrcMask_Type()
)
accIpxNamedNetFltrSrcMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNamedNetFltrSrcMask.setStatus("mandatory")
_AccIpxNetFltrApplTable_Object = MibTable
accIpxNetFltrApplTable = _AccIpxNetFltrApplTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 17, 3)
)
if mibBuilder.loadTexts:
    accIpxNetFltrApplTable.setStatus("mandatory")
_AccIpxNetFltrApplEntry_Object = MibTableRow
accIpxNetFltrApplEntry = _AccIpxNetFltrApplEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 17, 3, 1)
)
accIpxNetFltrApplEntry.setIndexNames(
    (0, "ACC-IPX", "accIpxNetFltrApplIfIndex"),
    (0, "ACC-IPX", "accIpxNetFltrApplPktDir"),
    (0, "ACC-IPX", "accIpxNetFltrApplSeqNum"),
)
if mibBuilder.loadTexts:
    accIpxNetFltrApplEntry.setStatus("mandatory")
_AccIpxNetFltrApplIfIndex_Type = Integer32
_AccIpxNetFltrApplIfIndex_Object = MibTableColumn
accIpxNetFltrApplIfIndex = _AccIpxNetFltrApplIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 17, 3, 1, 1),
    _AccIpxNetFltrApplIfIndex_Type()
)
accIpxNetFltrApplIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxNetFltrApplIfIndex.setStatus("mandatory")


class _AccIpxNetFltrApplPktDir_Type(Integer32):
    """Custom type accIpxNetFltrApplPktDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("global", 3),
          ("input", 1),
          ("output", 2))
    )


_AccIpxNetFltrApplPktDir_Type.__name__ = "Integer32"
_AccIpxNetFltrApplPktDir_Object = MibTableColumn
accIpxNetFltrApplPktDir = _AccIpxNetFltrApplPktDir_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 17, 3, 1, 2),
    _AccIpxNetFltrApplPktDir_Type()
)
accIpxNetFltrApplPktDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxNetFltrApplPktDir.setStatus("mandatory")
_AccIpxNetFltrApplSeqNum_Type = Integer32
_AccIpxNetFltrApplSeqNum_Object = MibTableColumn
accIpxNetFltrApplSeqNum = _AccIpxNetFltrApplSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 17, 3, 1, 3),
    _AccIpxNetFltrApplSeqNum_Type()
)
accIpxNetFltrApplSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxNetFltrApplSeqNum.setStatus("mandatory")
_AccIpxNetFltrApplName_Type = DisplayString
_AccIpxNetFltrApplName_Object = MibTableColumn
accIpxNetFltrApplName = _AccIpxNetFltrApplName_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 17, 3, 1, 4),
    _AccIpxNetFltrApplName_Type()
)
accIpxNetFltrApplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxNetFltrApplName.setStatus("mandatory")
_AccIpxNetFltrApplMatches_Type = Counter32
_AccIpxNetFltrApplMatches_Object = MibTableColumn
accIpxNetFltrApplMatches = _AccIpxNetFltrApplMatches_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 17, 3, 1, 5),
    _AccIpxNetFltrApplMatches_Type()
)
accIpxNetFltrApplMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxNetFltrApplMatches.setStatus("mandatory")
_AccIpxNetFltrApplLastMatch_Type = TimeTicks
_AccIpxNetFltrApplLastMatch_Object = MibTableColumn
accIpxNetFltrApplLastMatch = _AccIpxNetFltrApplLastMatch_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 17, 3, 1, 6),
    _AccIpxNetFltrApplLastMatch_Type()
)
accIpxNetFltrApplLastMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxNetFltrApplLastMatch.setStatus("mandatory")
_AccIpxNamedHostFilters_ObjectIdentity = ObjectIdentity
accIpxNamedHostFilters = _AccIpxNamedHostFilters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 18)
)


class _AccIpxNamedHostFltrDefaultAction_Type(Integer32):
    """Custom type accIpxNamedHostFltrDefaultAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discard", 0),
          ("highPriority", 3),
          ("lowPriority", 1),
          ("normalPriority", 2))
    )


_AccIpxNamedHostFltrDefaultAction_Type.__name__ = "Integer32"
_AccIpxNamedHostFltrDefaultAction_Object = MibScalar
accIpxNamedHostFltrDefaultAction = _AccIpxNamedHostFltrDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 18, 1),
    _AccIpxNamedHostFltrDefaultAction_Type()
)
accIpxNamedHostFltrDefaultAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNamedHostFltrDefaultAction.setStatus("mandatory")
_AccIpxNamedHostFltrTable_Object = MibTable
accIpxNamedHostFltrTable = _AccIpxNamedHostFltrTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 18, 2)
)
if mibBuilder.loadTexts:
    accIpxNamedHostFltrTable.setStatus("mandatory")
_AccIpxNamedHostFltrEntry_Object = MibTableRow
accIpxNamedHostFltrEntry = _AccIpxNamedHostFltrEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 18, 2, 1)
)
accIpxNamedHostFltrEntry.setIndexNames(
    (0, "ACC-IPX", "accIpxNamedHostFltrName"),
)
if mibBuilder.loadTexts:
    accIpxNamedHostFltrEntry.setStatus("mandatory")
_AccIpxNamedHostFltrId_Type = OctetString
_AccIpxNamedHostFltrId_Object = MibTableColumn
accIpxNamedHostFltrId = _AccIpxNamedHostFltrId_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 18, 2, 1, 1),
    _AccIpxNamedHostFltrId_Type()
)
accIpxNamedHostFltrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNamedHostFltrId.setStatus("mandatory")
_AccIpxNamedHostFltrSocket_Type = OctetString
_AccIpxNamedHostFltrSocket_Object = MibTableColumn
accIpxNamedHostFltrSocket = _AccIpxNamedHostFltrSocket_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 18, 2, 1, 2),
    _AccIpxNamedHostFltrSocket_Type()
)
accIpxNamedHostFltrSocket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNamedHostFltrSocket.setStatus("mandatory")
_AccIpxNamedHostFltrPepClient_Type = OctetString
_AccIpxNamedHostFltrPepClient_Object = MibTableColumn
accIpxNamedHostFltrPepClient = _AccIpxNamedHostFltrPepClient_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 18, 2, 1, 3),
    _AccIpxNamedHostFltrPepClient_Type()
)
accIpxNamedHostFltrPepClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNamedHostFltrPepClient.setStatus("mandatory")


class _AccIpxNamedHostFltrAction_Type(Integer32):
    """Custom type accIpxNamedHostFltrAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discard", 0),
          ("highPriority", 3),
          ("lowPriority", 1),
          ("normalPriority", 2))
    )


_AccIpxNamedHostFltrAction_Type.__name__ = "Integer32"
_AccIpxNamedHostFltrAction_Object = MibTableColumn
accIpxNamedHostFltrAction = _AccIpxNamedHostFltrAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 18, 2, 1, 4),
    _AccIpxNamedHostFltrAction_Type()
)
accIpxNamedHostFltrAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNamedHostFltrAction.setStatus("mandatory")


class _AccIpxNamedHostFltrStatus_Type(Integer32):
    """Custom type accIpxNamedHostFltrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_AccIpxNamedHostFltrStatus_Type.__name__ = "Integer32"
_AccIpxNamedHostFltrStatus_Object = MibTableColumn
accIpxNamedHostFltrStatus = _AccIpxNamedHostFltrStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 18, 2, 1, 5),
    _AccIpxNamedHostFltrStatus_Type()
)
accIpxNamedHostFltrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNamedHostFltrStatus.setStatus("mandatory")
_AccIpxNamedHostFltrName_Type = OctetString
_AccIpxNamedHostFltrName_Object = MibTableColumn
accIpxNamedHostFltrName = _AccIpxNamedHostFltrName_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 18, 2, 1, 6),
    _AccIpxNamedHostFltrName_Type()
)
accIpxNamedHostFltrName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNamedHostFltrName.setStatus("mandatory")


class _AccIpxNamedHostFltrPktDir_Type(Integer32):
    """Custom type accIpxNamedHostFltrPktDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input", 1),
          ("output", 2))
    )


_AccIpxNamedHostFltrPktDir_Type.__name__ = "Integer32"
_AccIpxNamedHostFltrPktDir_Object = MibTableColumn
accIpxNamedHostFltrPktDir = _AccIpxNamedHostFltrPktDir_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 18, 2, 1, 7),
    _AccIpxNamedHostFltrPktDir_Type()
)
accIpxNamedHostFltrPktDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNamedHostFltrPktDir.setStatus("mandatory")
_AccIpxNamedHostFltrMatches_Type = Counter32
_AccIpxNamedHostFltrMatches_Object = MibTableColumn
accIpxNamedHostFltrMatches = _AccIpxNamedHostFltrMatches_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 18, 2, 1, 8),
    _AccIpxNamedHostFltrMatches_Type()
)
accIpxNamedHostFltrMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxNamedHostFltrMatches.setStatus("mandatory")
_AccIpxNamedHostFltrLastMatch_Type = TimeTicks
_AccIpxNamedHostFltrLastMatch_Object = MibTableColumn
accIpxNamedHostFltrLastMatch = _AccIpxNamedHostFltrLastMatch_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 18, 2, 1, 9),
    _AccIpxNamedHostFltrLastMatch_Type()
)
accIpxNamedHostFltrLastMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxNamedHostFltrLastMatch.setStatus("mandatory")
_AccIpxHostFltrApplTable_Object = MibTable
accIpxHostFltrApplTable = _AccIpxHostFltrApplTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 18, 3)
)
if mibBuilder.loadTexts:
    accIpxHostFltrApplTable.setStatus("mandatory")
_AccIpxHostFltrApplEntry_Object = MibTableRow
accIpxHostFltrApplEntry = _AccIpxHostFltrApplEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 18, 3, 1)
)
accIpxHostFltrApplEntry.setIndexNames(
    (0, "ACC-IPX", "accIpxHostFltrApplIfIndex"),
    (0, "ACC-IPX", "accIpxHostFltrApplPktDir"),
    (0, "ACC-IPX", "accIpxHostFltrApplSeqNum"),
)
if mibBuilder.loadTexts:
    accIpxHostFltrApplEntry.setStatus("mandatory")
_AccIpxHostFltrApplIfIndex_Type = Integer32
_AccIpxHostFltrApplIfIndex_Object = MibTableColumn
accIpxHostFltrApplIfIndex = _AccIpxHostFltrApplIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 18, 3, 1, 1),
    _AccIpxHostFltrApplIfIndex_Type()
)
accIpxHostFltrApplIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxHostFltrApplIfIndex.setStatus("mandatory")


class _AccIpxHostFltrApplPktDir_Type(Integer32):
    """Custom type accIpxHostFltrApplPktDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("global", 3),
          ("input", 1),
          ("output", 2))
    )


_AccIpxHostFltrApplPktDir_Type.__name__ = "Integer32"
_AccIpxHostFltrApplPktDir_Object = MibTableColumn
accIpxHostFltrApplPktDir = _AccIpxHostFltrApplPktDir_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 18, 3, 1, 2),
    _AccIpxHostFltrApplPktDir_Type()
)
accIpxHostFltrApplPktDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxHostFltrApplPktDir.setStatus("mandatory")
_AccIpxHostFltrApplSeqNum_Type = Integer32
_AccIpxHostFltrApplSeqNum_Object = MibTableColumn
accIpxHostFltrApplSeqNum = _AccIpxHostFltrApplSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 18, 3, 1, 3),
    _AccIpxHostFltrApplSeqNum_Type()
)
accIpxHostFltrApplSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxHostFltrApplSeqNum.setStatus("mandatory")
_AccIpxHostFltrApplName_Type = DisplayString
_AccIpxHostFltrApplName_Object = MibTableColumn
accIpxHostFltrApplName = _AccIpxHostFltrApplName_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 18, 3, 1, 4),
    _AccIpxHostFltrApplName_Type()
)
accIpxHostFltrApplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxHostFltrApplName.setStatus("mandatory")
_AccIpxHostFltrApplMatches_Type = Counter32
_AccIpxHostFltrApplMatches_Object = MibTableColumn
accIpxHostFltrApplMatches = _AccIpxHostFltrApplMatches_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 18, 3, 1, 5),
    _AccIpxHostFltrApplMatches_Type()
)
accIpxHostFltrApplMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxHostFltrApplMatches.setStatus("mandatory")
_AccIpxHostFltrApplLastMatch_Type = TimeTicks
_AccIpxHostFltrApplLastMatch_Object = MibTableColumn
accIpxHostFltrApplLastMatch = _AccIpxHostFltrApplLastMatch_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 18, 3, 1, 6),
    _AccIpxHostFltrApplLastMatch_Type()
)
accIpxHostFltrApplLastMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxHostFltrApplLastMatch.setStatus("mandatory")
_AccIpxNamedSapFilters_ObjectIdentity = ObjectIdentity
accIpxNamedSapFilters = _AccIpxNamedSapFilters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 19)
)


class _AccIpxNamedSapFltrDefault_Type(Integer32):
    """Custom type accIpxNamedSapFltrDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("reject", 2))
    )


_AccIpxNamedSapFltrDefault_Type.__name__ = "Integer32"
_AccIpxNamedSapFltrDefault_Object = MibScalar
accIpxNamedSapFltrDefault = _AccIpxNamedSapFltrDefault_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 19, 1),
    _AccIpxNamedSapFltrDefault_Type()
)
accIpxNamedSapFltrDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNamedSapFltrDefault.setStatus("mandatory")
_AccIpxNamedSapFltrTable_Object = MibTable
accIpxNamedSapFltrTable = _AccIpxNamedSapFltrTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 19, 2)
)
if mibBuilder.loadTexts:
    accIpxNamedSapFltrTable.setStatus("mandatory")
_AccIpxNamedSapFltrEntry_Object = MibTableRow
accIpxNamedSapFltrEntry = _AccIpxNamedSapFltrEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 19, 2, 1)
)
accIpxNamedSapFltrEntry.setIndexNames(
    (0, "ACC-IPX", "accIpxNamedSapFltrName"),
)
if mibBuilder.loadTexts:
    accIpxNamedSapFltrEntry.setStatus("mandatory")
_AccIpxNamedSapFltrSrvType_Type = OctetString
_AccIpxNamedSapFltrSrvType_Object = MibTableColumn
accIpxNamedSapFltrSrvType = _AccIpxNamedSapFltrSrvType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 19, 2, 1, 1),
    _AccIpxNamedSapFltrSrvType_Type()
)
accIpxNamedSapFltrSrvType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNamedSapFltrSrvType.setStatus("mandatory")
_AccIpxNamedSapFltrSrvName_Type = OctetString
_AccIpxNamedSapFltrSrvName_Object = MibTableColumn
accIpxNamedSapFltrSrvName = _AccIpxNamedSapFltrSrvName_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 19, 2, 1, 2),
    _AccIpxNamedSapFltrSrvName_Type()
)
accIpxNamedSapFltrSrvName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNamedSapFltrSrvName.setStatus("mandatory")


class _AccIpxNamedSapFltrAction_Type(Integer32):
    """Custom type accIpxNamedSapFltrAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("reject", 2))
    )


_AccIpxNamedSapFltrAction_Type.__name__ = "Integer32"
_AccIpxNamedSapFltrAction_Object = MibTableColumn
accIpxNamedSapFltrAction = _AccIpxNamedSapFltrAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 19, 2, 1, 3),
    _AccIpxNamedSapFltrAction_Type()
)
accIpxNamedSapFltrAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNamedSapFltrAction.setStatus("mandatory")


class _AccIpxNamedSapFltrStatus_Type(Integer32):
    """Custom type accIpxNamedSapFltrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_AccIpxNamedSapFltrStatus_Type.__name__ = "Integer32"
_AccIpxNamedSapFltrStatus_Object = MibTableColumn
accIpxNamedSapFltrStatus = _AccIpxNamedSapFltrStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 19, 2, 1, 4),
    _AccIpxNamedSapFltrStatus_Type()
)
accIpxNamedSapFltrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNamedSapFltrStatus.setStatus("mandatory")
_AccIpxNamedSapFltrName_Type = OctetString
_AccIpxNamedSapFltrName_Object = MibTableColumn
accIpxNamedSapFltrName = _AccIpxNamedSapFltrName_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 19, 2, 1, 5),
    _AccIpxNamedSapFltrName_Type()
)
accIpxNamedSapFltrName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNamedSapFltrName.setStatus("mandatory")


class _AccIpxNamedSapFltrPktDir_Type(Integer32):
    """Custom type accIpxNamedSapFltrPktDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input", 1),
          ("output", 2))
    )


_AccIpxNamedSapFltrPktDir_Type.__name__ = "Integer32"
_AccIpxNamedSapFltrPktDir_Object = MibTableColumn
accIpxNamedSapFltrPktDir = _AccIpxNamedSapFltrPktDir_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 19, 2, 1, 6),
    _AccIpxNamedSapFltrPktDir_Type()
)
accIpxNamedSapFltrPktDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNamedSapFltrPktDir.setStatus("mandatory")
_AccIpxNamedSapFltrMatches_Type = Counter32
_AccIpxNamedSapFltrMatches_Object = MibTableColumn
accIpxNamedSapFltrMatches = _AccIpxNamedSapFltrMatches_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 19, 2, 1, 7),
    _AccIpxNamedSapFltrMatches_Type()
)
accIpxNamedSapFltrMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxNamedSapFltrMatches.setStatus("mandatory")
_AccIpxNamedSapFltrLastMatch_Type = TimeTicks
_AccIpxNamedSapFltrLastMatch_Object = MibTableColumn
accIpxNamedSapFltrLastMatch = _AccIpxNamedSapFltrLastMatch_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 19, 2, 1, 8),
    _AccIpxNamedSapFltrLastMatch_Type()
)
accIpxNamedSapFltrLastMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxNamedSapFltrLastMatch.setStatus("mandatory")
_AccIpxSapFltrApplTable_Object = MibTable
accIpxSapFltrApplTable = _AccIpxSapFltrApplTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 19, 3)
)
if mibBuilder.loadTexts:
    accIpxSapFltrApplTable.setStatus("mandatory")
_AccIpxSapFltrApplEntry_Object = MibTableRow
accIpxSapFltrApplEntry = _AccIpxSapFltrApplEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 19, 3, 1)
)
accIpxSapFltrApplEntry.setIndexNames(
    (0, "ACC-IPX", "accIpxSapFltrApplIfIndex"),
    (0, "ACC-IPX", "accIpxSapFltrApplPktDir"),
    (0, "ACC-IPX", "accIpxSapFltrApplSeqNum"),
)
if mibBuilder.loadTexts:
    accIpxSapFltrApplEntry.setStatus("mandatory")
_AccIpxSapFltrApplIfIndex_Type = Integer32
_AccIpxSapFltrApplIfIndex_Object = MibTableColumn
accIpxSapFltrApplIfIndex = _AccIpxSapFltrApplIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 19, 3, 1, 1),
    _AccIpxSapFltrApplIfIndex_Type()
)
accIpxSapFltrApplIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxSapFltrApplIfIndex.setStatus("mandatory")


class _AccIpxSapFltrApplPktDir_Type(Integer32):
    """Custom type accIpxSapFltrApplPktDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("global", 3),
          ("input", 1),
          ("output", 2))
    )


_AccIpxSapFltrApplPktDir_Type.__name__ = "Integer32"
_AccIpxSapFltrApplPktDir_Object = MibTableColumn
accIpxSapFltrApplPktDir = _AccIpxSapFltrApplPktDir_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 19, 3, 1, 2),
    _AccIpxSapFltrApplPktDir_Type()
)
accIpxSapFltrApplPktDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxSapFltrApplPktDir.setStatus("mandatory")
_AccIpxSapFltrApplSeqNum_Type = Integer32
_AccIpxSapFltrApplSeqNum_Object = MibTableColumn
accIpxSapFltrApplSeqNum = _AccIpxSapFltrApplSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 19, 3, 1, 3),
    _AccIpxSapFltrApplSeqNum_Type()
)
accIpxSapFltrApplSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxSapFltrApplSeqNum.setStatus("mandatory")
_AccIpxSapFltrApplName_Type = DisplayString
_AccIpxSapFltrApplName_Object = MibTableColumn
accIpxSapFltrApplName = _AccIpxSapFltrApplName_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 19, 3, 1, 4),
    _AccIpxSapFltrApplName_Type()
)
accIpxSapFltrApplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxSapFltrApplName.setStatus("mandatory")
_AccIpxSapFltrApplMatches_Type = Counter32
_AccIpxSapFltrApplMatches_Object = MibTableColumn
accIpxSapFltrApplMatches = _AccIpxSapFltrApplMatches_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 19, 3, 1, 5),
    _AccIpxSapFltrApplMatches_Type()
)
accIpxSapFltrApplMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxSapFltrApplMatches.setStatus("mandatory")
_AccIpxSapFltrApplLastMatch_Type = TimeTicks
_AccIpxSapFltrApplLastMatch_Object = MibTableColumn
accIpxSapFltrApplLastMatch = _AccIpxSapFltrApplLastMatch_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 19, 3, 1, 6),
    _AccIpxSapFltrApplLastMatch_Type()
)
accIpxSapFltrApplLastMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxSapFltrApplLastMatch.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-IPX",
    **{"accIpx": accIpx,
       "accIpxParms": accIpxParms,
       "accIpxAdStat": accIpxAdStat,
       "accIpxCkSum": accIpxCkSum,
       "accIpxSpltHorz": accIpxSpltHorz,
       "accIpxAllNets": accIpxAllNets,
       "accIpxMode": accIpxMode,
       "accIpxWdFilter": accIpxWdFilter,
       "accIpxTrigUpdates": accIpxTrigUpdates,
       "accIpxNetTable": accIpxNetTable,
       "accIpxNetEntry": accIpxNetEntry,
       "accIpxNetPort": accIpxNetPort,
       "accIpxNetNumber": accIpxNetNumber,
       "accIpxNetType": accIpxNetType,
       "accIpxNetEncap": accIpxNetEncap,
       "accIpxNetSlot": accIpxNetSlot,
       "accIpxNetAdStat": accIpxNetAdStat,
       "accIpxNetMtu": accIpxNetMtu,
       "accIpxNetUpdate": accIpxNetUpdate,
       "accIpxNetHops": accIpxNetHops,
       "accIpxNetCost": accIpxNetCost,
       "accIpxNetX25InOutAddr": accIpxNetX25InOutAddr,
       "accIpxNetX25InAddr": accIpxNetX25InAddr,
       "accIpxNetX25Idle": accIpxNetX25Idle,
       "accIpxNetX25PktVal": accIpxNetX25PktVal,
       "accIpxNetX25PktWin": accIpxNetX25PktWin,
       "accIpxNetEntryStat": accIpxNetEntryStat,
       "accIpxNetFncAddr": accIpxNetFncAddr,
       "accIpxNetSrMode": accIpxNetSrMode,
       "accIpxNetX25FacIndex": accIpxNetX25FacIndex,
       "accIpxNetDlci": accIpxNetDlci,
       "accIpxNetWdState": accIpxNetWdState,
       "accIpxNetRtgHldTmr": accIpxNetRtgHldTmr,
       "accIpxNetRtgPollCnt": accIpxNetRtgPollCnt,
       "accIpxNetRtgProtType": accIpxNetRtgProtType,
       "accIpxNetRtgSettleTimer": accIpxNetRtgSettleTimer,
       "accIpxNetRtgQuietTimer": accIpxNetRtgQuietTimer,
       "accIpxNetRtgDiagLevel": accIpxNetRtgDiagLevel,
       "accIpxNetDialProt": accIpxNetDialProt,
       "accIpxRtTable": accIpxRtTable,
       "accIpxRtEntry": accIpxRtEntry,
       "accIpxRtDest": accIpxRtDest,
       "accIpxRtNxtNet": accIpxRtNxtNet,
       "accIpxRtRouter": accIpxRtRouter,
       "accIpxRtHops": accIpxRtHops,
       "accIpxRtCost": accIpxRtCost,
       "accIpxRtType": accIpxRtType,
       "accIpxRtOwner": accIpxRtOwner,
       "accIpxRtAge": accIpxRtAge,
       "accIpxRtPort": accIpxRtPort,
       "accIpxRipStat": accIpxRipStat,
       "accIpxRipReqIns": accIpxRipReqIns,
       "accIpxRipRespIns": accIpxRipRespIns,
       "accIpxRipReqOuts": accIpxRipReqOuts,
       "accIpxRipRespOuts": accIpxRipRespOuts,
       "accIpxRipErrIns": accIpxRipErrIns,
       "accIpxRipErrOuts": accIpxRipErrOuts,
       "accIpxRipDemandReqIns": accIpxRipDemandReqIns,
       "accIpxRipDemandRespIns": accIpxRipDemandRespIns,
       "accIpxRipDemandAckIns": accIpxRipDemandAckIns,
       "accIpxRipDemandReqOuts": accIpxRipDemandReqOuts,
       "accIpxRipDemandRespOuts": accIpxRipDemandRespOuts,
       "accIpxRipDemandAckOuts": accIpxRipDemandAckOuts,
       "accIpxRipDemandInErrs": accIpxRipDemandInErrs,
       "accIpxRipDemandOutErrs": accIpxRipDemandOutErrs,
       "accIpxNodeStat": accIpxNodeStat,
       "accIpxLocalIns": accIpxLocalIns,
       "accIpxLocalOuts": accIpxLocalOuts,
       "accIpxNoSockets": accIpxNoSockets,
       "accIpxNoRoutes": accIpxNoRoutes,
       "accIpxNodeInErrs": accIpxNodeInErrs,
       "accIpxOutErrs": accIpxOutErrs,
       "accIpxAllNetsIns": accIpxAllNetsIns,
       "accIpxAllNetsOuts": accIpxAllNetsOuts,
       "accIpxAllNetsErrs": accIpxAllNetsErrs,
       "accIpxPortStatTable": accIpxPortStatTable,
       "accIpxPortStatEntry": accIpxPortStatEntry,
       "accIpxPortNumber": accIpxPortNumber,
       "accIpxPortTotalIns": accIpxPortTotalIns,
       "accIpxPorFwdReqIns": accIpxPorFwdReqIns,
       "accIpxPortNoFwdRts": accIpxPortNoFwdRts,
       "accIpxPortTotalOuts": accIpxPortTotalOuts,
       "accIpxPortHopCnts": accIpxPortHopCnts,
       "accIpxPortNotForMes": accIpxPortNotForMes,
       "accIpxPortFwdReqOuts": accIpxPortFwdReqOuts,
       "accIpxPortFwdErrs": accIpxPortFwdErrs,
       "accIpxPortInErrs": accIpxPortInErrs,
       "accIpxPortTooShorts": accIpxPortTooShorts,
       "accIpxPortCkSums": accIpxPortCkSums,
       "accIpxPortTooLongs": accIpxPortTooLongs,
       "accIpxPortOutErrs": accIpxPortOutErrs,
       "accIpxPortOpState": accIpxPortOpState,
       "accIpxSapStat": accIpxSapStat,
       "accIpxSapReqIns": accIpxSapReqIns,
       "accIpxSapReqOuts": accIpxSapReqOuts,
       "accIpxSapRespIns": accIpxSapRespIns,
       "accIpxSapRespOuts": accIpxSapRespOuts,
       "accIpxSapGetNearIns": accIpxSapGetNearIns,
       "accIpxSapGetNearOuts": accIpxSapGetNearOuts,
       "accIpxSapNoRoutes": accIpxSapNoRoutes,
       "accIpxSapNotBests": accIpxSapNotBests,
       "accIpxSapNoServers": accIpxSapNoServers,
       "accIpxSapInErrs": accIpxSapInErrs,
       "accIpxSapOutErrs": accIpxSapOutErrs,
       "accIpxSapDemandReqIns": accIpxSapDemandReqIns,
       "accIpxSapDemandReqOuts": accIpxSapDemandReqOuts,
       "accIpxSapDemandRespIns": accIpxSapDemandRespIns,
       "accIpxSapDemandRespOuts": accIpxSapDemandRespOuts,
       "accIpxSapDemandAckIns": accIpxSapDemandAckIns,
       "accIpxSapDemandAckOuts": accIpxSapDemandAckOuts,
       "accIpxSapDemandInErrs": accIpxSapDemandInErrs,
       "accIpxSapDemandOutErrs": accIpxSapDemandOutErrs,
       "accIpxSrvTable": accIpxSrvTable,
       "accIpxSrvEntry": accIpxSrvEntry,
       "accIpxSrvName": accIpxSrvName,
       "accIpxSrvType": accIpxSrvType,
       "accIpxSrvHost": accIpxSrvHost,
       "accIpxSrvHops": accIpxSrvHops,
       "accIpxSrvOwner": accIpxSrvOwner,
       "accIpxSrvAge": accIpxSrvAge,
       "accIpxRouteFilters": accIpxRouteFilters,
       "accIpxRteFltrDefaultAction": accIpxRteFltrDefaultAction,
       "accIpxRteNbrTable": accIpxRteNbrTable,
       "accIpxRteNbrEntry": accIpxRteNbrEntry,
       "accIpxRteNbrId": accIpxRteNbrId,
       "accIpxRteNbrAction": accIpxRteNbrAction,
       "accIpxRteNbrStatus": accIpxRteNbrStatus,
       "accIpxRteFltrTable": accIpxRteFltrTable,
       "accIpxRteFltrEntry": accIpxRteFltrEntry,
       "accIpxRteFltrNeighbor": accIpxRteFltrNeighbor,
       "accIpxRteFltrNetwork": accIpxRteFltrNetwork,
       "accIpxRteFltrAction": accIpxRteFltrAction,
       "accIpxRteFltrStatus": accIpxRteFltrStatus,
       "accIpxNetworkFilters": accIpxNetworkFilters,
       "accIpxNetFltrDefaultAction": accIpxNetFltrDefaultAction,
       "oldIpxNetFltrTable": oldIpxNetFltrTable,
       "oldIpxNetFltrEntry": oldIpxNetFltrEntry,
       "oldIpxNetFltrDestination": oldIpxNetFltrDestination,
       "oldIpxNetFltrSource": oldIpxNetFltrSource,
       "oldIpxNetFltrAction": oldIpxNetFltrAction,
       "oldIpxNetFltrStatus": oldIpxNetFltrStatus,
       "accIpxNetFltrTable": accIpxNetFltrTable,
       "accIpxNetFltrEntry": accIpxNetFltrEntry,
       "accIpxNetFltrDestination": accIpxNetFltrDestination,
       "accIpxNetFltrSource": accIpxNetFltrSource,
       "accIpxNetFltrAction": accIpxNetFltrAction,
       "accIpxNetFltrStatus": accIpxNetFltrStatus,
       "accIpxNetFltrDestSkt": accIpxNetFltrDestSkt,
       "accIpxNetFltrSrcSkt": accIpxNetFltrSrcSkt,
       "accIpxNetFltrPktType": accIpxNetFltrPktType,
       "accIpxHostFilters": accIpxHostFilters,
       "accIpxHostFltrDefaultAction": accIpxHostFltrDefaultAction,
       "accIpxHostFltrTable": accIpxHostFltrTable,
       "accIpxHostFltrEntry": accIpxHostFltrEntry,
       "accIpxHostFltrId": accIpxHostFltrId,
       "accIpxHostFltrSocket": accIpxHostFltrSocket,
       "accIpxHostFltrPepClient": accIpxHostFltrPepClient,
       "accIpxHostFltrAction": accIpxHostFltrAction,
       "accIpxHostFltrStatus": accIpxHostFltrStatus,
       "accIpxSapFilters": accIpxSapFilters,
       "accIpxSapFltrDefault": accIpxSapFltrDefault,
       "accIpxSapFltrTable": accIpxSapFltrTable,
       "accIpxSapFltrEntry": accIpxSapFltrEntry,
       "accIpxSapFltrSrvType": accIpxSapFltrSrvType,
       "accIpxSapFltrSrvName": accIpxSapFltrSrvName,
       "accIpxSapFltrAction": accIpxSapFltrAction,
       "accIpxSapFltrStatus": accIpxSapFltrStatus,
       "accIpxNetWdParms": accIpxNetWdParms,
       "accIpxWdProxyDuration": accIpxWdProxyDuration,
       "accIpxWdHoldPeriod": accIpxWdHoldPeriod,
       "accIpxWdMaxSessions": accIpxWdMaxSessions,
       "accIpxWdDiagLevel": accIpxWdDiagLevel,
       "accIpxWdCurrentDropDead": accIpxWdCurrentDropDead,
       "accIpxWdIpxSessionCnt": accIpxWdIpxSessionCnt,
       "accIpxWdSpxSessionCnt": accIpxWdSpxSessionCnt,
       "accIpxWdSession": accIpxWdSession,
       "accIpxWdSessTable": accIpxWdSessTable,
       "accIpxWdSessEntry": accIpxWdSessEntry,
       "accIpxWdSessionId": accIpxWdSessionId,
       "accIpxWdState": accIpxWdState,
       "accIpxWdLastSeen": accIpxWdLastSeen,
       "accIpxWdClientNet": accIpxWdClientNet,
       "accIpxWdClientHost": accIpxWdClientHost,
       "accIpxWdDropDead": accIpxWdDropDead,
       "accIpxWdServerNet": accIpxWdServerNet,
       "accIpxWdServerHost": accIpxWdServerHost,
       "accIpxSpxWdSession": accIpxSpxWdSession,
       "accIpxSpxWdSessTable": accIpxSpxWdSessTable,
       "accIpxSpxWdSessEntry": accIpxSpxWdSessEntry,
       "accIpxSpxWdSrcSessionId": accIpxSpxWdSrcSessionId,
       "accIpxSpxWdDstSessionId": accIpxSpxWdDstSessionId,
       "accIpxSpxWdState": accIpxSpxWdState,
       "accIpxSpxWdClientNet": accIpxSpxWdClientNet,
       "accIpxSpxWdClientHost": accIpxSpxWdClientHost,
       "accIpxSpxWdLastSeen": accIpxSpxWdLastSeen,
       "accIpxSpxWdServerNet": accIpxSpxWdServerNet,
       "accIpxSpxWdServerHost": accIpxSpxWdServerHost,
       "accIpxSpxWdDropDead": accIpxSpxWdDropDead,
       "accIpxSpxWdSrcSeqNo": accIpxSpxWdSrcSeqNo,
       "accIpxSpxWdDstSeqNo": accIpxSpxWdDstSeqNo,
       "accIpxSpxWdAckDiscards": accIpxSpxWdAckDiscards,
       "accIpxSpxWdSrcAckNo": accIpxSpxWdSrcAckNo,
       "accIpxSpxWdDstAckNo": accIpxSpxWdDstAckNo,
       "accIpxNamedRteFilters": accIpxNamedRteFilters,
       "accIpxNamedRteFltrDefaultAction": accIpxNamedRteFltrDefaultAction,
       "accIpxNamedRteFltrTable": accIpxNamedRteFltrTable,
       "accIpxNamedRteFltrEntry": accIpxNamedRteFltrEntry,
       "accIpxNamedRteFltrNeighbor": accIpxNamedRteFltrNeighbor,
       "accIpxNamedRteFltrNetwork": accIpxNamedRteFltrNetwork,
       "accIpxNamedRteFltrAction": accIpxNamedRteFltrAction,
       "accIpxNamedRteFltrStatus": accIpxNamedRteFltrStatus,
       "accIpxNamedRteFltrName": accIpxNamedRteFltrName,
       "accIpxNamedRteFltrPktDir": accIpxNamedRteFltrPktDir,
       "accIpxNamedRteFltrMatches": accIpxNamedRteFltrMatches,
       "accIpxNamedRteFltrLastMatch": accIpxNamedRteFltrLastMatch,
       "accIpxNamedRteFltrNetMask": accIpxNamedRteFltrNetMask,
       "accIpxRteFltrApplTable": accIpxRteFltrApplTable,
       "accIpxRteFltrApplEntry": accIpxRteFltrApplEntry,
       "accIpxRteFltrApplIfIndex": accIpxRteFltrApplIfIndex,
       "accIpxRteFltrApplPktDir": accIpxRteFltrApplPktDir,
       "accIpxRteFltrApplSeqNum": accIpxRteFltrApplSeqNum,
       "accIpxRteFltrApplName": accIpxRteFltrApplName,
       "accIpxRteFltrApplMatches": accIpxRteFltrApplMatches,
       "accIpxRteFltrApplLastMatch": accIpxRteFltrApplLastMatch,
       "accIpxNamedNetFilters": accIpxNamedNetFilters,
       "accIpxNamedNetFltrDefault": accIpxNamedNetFltrDefault,
       "accIpxNamedNetFltrTable": accIpxNamedNetFltrTable,
       "accIpxNamedNetFltrEntry": accIpxNamedNetFltrEntry,
       "accIpxNamedNetFltrDestination": accIpxNamedNetFltrDestination,
       "accIpxNamedNetFltrSource": accIpxNamedNetFltrSource,
       "accIpxNamedNetFltrAction": accIpxNamedNetFltrAction,
       "accIpxNamedNetFltrStatus": accIpxNamedNetFltrStatus,
       "accIpxNamedNetFltrDestSkt": accIpxNamedNetFltrDestSkt,
       "accIpxNamedNetFltrSrcSkt": accIpxNamedNetFltrSrcSkt,
       "accIpxNamedNetFltrType": accIpxNamedNetFltrType,
       "accIpxNamedNetFltrName": accIpxNamedNetFltrName,
       "accIpxNamedNetFltrPktDir": accIpxNamedNetFltrPktDir,
       "accIpxNamedNetFltrMatches": accIpxNamedNetFltrMatches,
       "accIpxNamedNetFltrLastMatch": accIpxNamedNetFltrLastMatch,
       "accIpxNamedNetFltrDestMask": accIpxNamedNetFltrDestMask,
       "accIpxNamedNetFltrSrcMask": accIpxNamedNetFltrSrcMask,
       "accIpxNetFltrApplTable": accIpxNetFltrApplTable,
       "accIpxNetFltrApplEntry": accIpxNetFltrApplEntry,
       "accIpxNetFltrApplIfIndex": accIpxNetFltrApplIfIndex,
       "accIpxNetFltrApplPktDir": accIpxNetFltrApplPktDir,
       "accIpxNetFltrApplSeqNum": accIpxNetFltrApplSeqNum,
       "accIpxNetFltrApplName": accIpxNetFltrApplName,
       "accIpxNetFltrApplMatches": accIpxNetFltrApplMatches,
       "accIpxNetFltrApplLastMatch": accIpxNetFltrApplLastMatch,
       "accIpxNamedHostFilters": accIpxNamedHostFilters,
       "accIpxNamedHostFltrDefaultAction": accIpxNamedHostFltrDefaultAction,
       "accIpxNamedHostFltrTable": accIpxNamedHostFltrTable,
       "accIpxNamedHostFltrEntry": accIpxNamedHostFltrEntry,
       "accIpxNamedHostFltrId": accIpxNamedHostFltrId,
       "accIpxNamedHostFltrSocket": accIpxNamedHostFltrSocket,
       "accIpxNamedHostFltrPepClient": accIpxNamedHostFltrPepClient,
       "accIpxNamedHostFltrAction": accIpxNamedHostFltrAction,
       "accIpxNamedHostFltrStatus": accIpxNamedHostFltrStatus,
       "accIpxNamedHostFltrName": accIpxNamedHostFltrName,
       "accIpxNamedHostFltrPktDir": accIpxNamedHostFltrPktDir,
       "accIpxNamedHostFltrMatches": accIpxNamedHostFltrMatches,
       "accIpxNamedHostFltrLastMatch": accIpxNamedHostFltrLastMatch,
       "accIpxHostFltrApplTable": accIpxHostFltrApplTable,
       "accIpxHostFltrApplEntry": accIpxHostFltrApplEntry,
       "accIpxHostFltrApplIfIndex": accIpxHostFltrApplIfIndex,
       "accIpxHostFltrApplPktDir": accIpxHostFltrApplPktDir,
       "accIpxHostFltrApplSeqNum": accIpxHostFltrApplSeqNum,
       "accIpxHostFltrApplName": accIpxHostFltrApplName,
       "accIpxHostFltrApplMatches": accIpxHostFltrApplMatches,
       "accIpxHostFltrApplLastMatch": accIpxHostFltrApplLastMatch,
       "accIpxNamedSapFilters": accIpxNamedSapFilters,
       "accIpxNamedSapFltrDefault": accIpxNamedSapFltrDefault,
       "accIpxNamedSapFltrTable": accIpxNamedSapFltrTable,
       "accIpxNamedSapFltrEntry": accIpxNamedSapFltrEntry,
       "accIpxNamedSapFltrSrvType": accIpxNamedSapFltrSrvType,
       "accIpxNamedSapFltrSrvName": accIpxNamedSapFltrSrvName,
       "accIpxNamedSapFltrAction": accIpxNamedSapFltrAction,
       "accIpxNamedSapFltrStatus": accIpxNamedSapFltrStatus,
       "accIpxNamedSapFltrName": accIpxNamedSapFltrName,
       "accIpxNamedSapFltrPktDir": accIpxNamedSapFltrPktDir,
       "accIpxNamedSapFltrMatches": accIpxNamedSapFltrMatches,
       "accIpxNamedSapFltrLastMatch": accIpxNamedSapFltrLastMatch,
       "accIpxSapFltrApplTable": accIpxSapFltrApplTable,
       "accIpxSapFltrApplEntry": accIpxSapFltrApplEntry,
       "accIpxSapFltrApplIfIndex": accIpxSapFltrApplIfIndex,
       "accIpxSapFltrApplPktDir": accIpxSapFltrApplPktDir,
       "accIpxSapFltrApplSeqNum": accIpxSapFltrApplSeqNum,
       "accIpxSapFltrApplName": accIpxSapFltrApplName,
       "accIpxSapFltrApplMatches": accIpxSapFltrApplMatches,
       "accIpxSapFltrApplLastMatch": accIpxSapFltrApplLastMatch}
)
