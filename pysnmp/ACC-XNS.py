# SNMP MIB module (ACC-XNS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-XNS
# Produced by pysmi-1.5.4 at Mon Oct 14 20:33:14 2024
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
 NotificationType,
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
    "NotificationType",
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

_AccXns_ObjectIdentity = ObjectIdentity
accXns = _AccXns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21)
)
_AccXnsParms_ObjectIdentity = ObjectIdentity
accXnsParms = _AccXnsParms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 1)
)


class _AccXnsAdStat_Type(Integer32):
    """Custom type accXnsAdStat based on Integer32"""
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


_AccXnsAdStat_Type.__name__ = "Integer32"
_AccXnsAdStat_Object = MibScalar
accXnsAdStat = _AccXnsAdStat_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 1, 1),
    _AccXnsAdStat_Type()
)
accXnsAdStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsAdStat.setStatus("mandatory")


class _AccXnsCkSum_Type(Integer32):
    """Custom type accXnsCkSum based on Integer32"""
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


_AccXnsCkSum_Type.__name__ = "Integer32"
_AccXnsCkSum_Object = MibScalar
accXnsCkSum = _AccXnsCkSum_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 1, 2),
    _AccXnsCkSum_Type()
)
accXnsCkSum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsCkSum.setStatus("mandatory")


class _AccXnsSpltHorz_Type(Integer32):
    """Custom type accXnsSpltHorz based on Integer32"""
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


_AccXnsSpltHorz_Type.__name__ = "Integer32"
_AccXnsSpltHorz_Object = MibScalar
accXnsSpltHorz = _AccXnsSpltHorz_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 1, 3),
    _AccXnsSpltHorz_Type()
)
accXnsSpltHorz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsSpltHorz.setStatus("mandatory")


class _AccXnsAllNets_Type(Integer32):
    """Custom type accXnsAllNets based on Integer32"""
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


_AccXnsAllNets_Type.__name__ = "Integer32"
_AccXnsAllNets_Object = MibScalar
accXnsAllNets = _AccXnsAllNets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 1, 4),
    _AccXnsAllNets_Type()
)
accXnsAllNets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsAllNets.setStatus("mandatory")


class _AccXnsMode_Type(Integer32):
    """Custom type accXnsMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ub", 2),
          ("xns", 1))
    )


_AccXnsMode_Type.__name__ = "Integer32"
_AccXnsMode_Object = MibScalar
accXnsMode = _AccXnsMode_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 1, 5),
    _AccXnsMode_Type()
)
accXnsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsMode.setStatus("mandatory")
_AccXnsNetTable_Object = MibTable
accXnsNetTable = _AccXnsNetTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 2)
)
if mibBuilder.loadTexts:
    accXnsNetTable.setStatus("mandatory")
_AccXnsNetEntry_Object = MibTableRow
accXnsNetEntry = _AccXnsNetEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 2, 1)
)
accXnsNetEntry.setIndexNames(
    (0, "ACC-XNS", "accXnsNetPort"),
)
if mibBuilder.loadTexts:
    accXnsNetEntry.setStatus("mandatory")
_AccXnsNetPort_Type = Integer32
_AccXnsNetPort_Object = MibTableColumn
accXnsNetPort = _AccXnsNetPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 2, 1, 1),
    _AccXnsNetPort_Type()
)
accXnsNetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNetPort.setStatus("mandatory")
_AccXnsNetNumber_Type = OctetString
_AccXnsNetNumber_Object = MibTableColumn
accXnsNetNumber = _AccXnsNetNumber_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 2, 1, 2),
    _AccXnsNetNumber_Type()
)
accXnsNetNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNetNumber.setStatus("mandatory")


class _AccXnsNetType_Type(Integer32):
    """Custom type accXnsNetType based on Integer32"""
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
        *(("enet", 1),
          ("ffr", 5),
          ("lapb", 3),
          ("token-ring", 2),
          ("x25", 4))
    )


_AccXnsNetType_Type.__name__ = "Integer32"
_AccXnsNetType_Object = MibTableColumn
accXnsNetType = _AccXnsNetType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 2, 1, 3),
    _AccXnsNetType_Type()
)
accXnsNetType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNetType.setStatus("mandatory")


class _AccXnsNetEncap_Type(Integer32):
    """Custom type accXnsNetEncap based on Integer32"""
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


_AccXnsNetEncap_Type.__name__ = "Integer32"
_AccXnsNetEncap_Object = MibTableColumn
accXnsNetEncap = _AccXnsNetEncap_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 2, 1, 4),
    _AccXnsNetEncap_Type()
)
accXnsNetEncap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNetEncap.setStatus("mandatory")


class _AccXnsNetSlot_Type(Integer32):
    """Custom type accXnsNetSlot based on Integer32"""
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


_AccXnsNetSlot_Type.__name__ = "Integer32"
_AccXnsNetSlot_Object = MibTableColumn
accXnsNetSlot = _AccXnsNetSlot_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 2, 1, 5),
    _AccXnsNetSlot_Type()
)
accXnsNetSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNetSlot.setStatus("mandatory")


class _AccXnsNetAdStat_Type(Integer32):
    """Custom type accXnsNetAdStat based on Integer32"""
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


_AccXnsNetAdStat_Type.__name__ = "Integer32"
_AccXnsNetAdStat_Object = MibTableColumn
accXnsNetAdStat = _AccXnsNetAdStat_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 2, 1, 6),
    _AccXnsNetAdStat_Type()
)
accXnsNetAdStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNetAdStat.setStatus("mandatory")


class _AccXnsNetMtu_Type(Integer32):
    """Custom type accXnsNetMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(576, 65535),
    )


_AccXnsNetMtu_Type.__name__ = "Integer32"
_AccXnsNetMtu_Object = MibTableColumn
accXnsNetMtu = _AccXnsNetMtu_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 2, 1, 7),
    _AccXnsNetMtu_Type()
)
accXnsNetMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNetMtu.setStatus("mandatory")


class _AccXnsNetUpdate_Type(TimeTicks):
    """Custom type accXnsNetUpdate based on TimeTicks"""
    defaultValue = 1500


_AccXnsNetUpdate_Object = MibTableColumn
accXnsNetUpdate = _AccXnsNetUpdate_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 2, 1, 8),
    _AccXnsNetUpdate_Type()
)
accXnsNetUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNetUpdate.setStatus("mandatory")


class _AccXnsNetHops_Type(Integer32):
    """Custom type accXnsNetHops based on Integer32"""
    defaultValue = 1


_AccXnsNetHops_Object = MibTableColumn
accXnsNetHops = _AccXnsNetHops_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 2, 1, 9),
    _AccXnsNetHops_Type()
)
accXnsNetHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNetHops.setStatus("mandatory")
_AccXnsNetCost_Type = Integer32
_AccXnsNetCost_Object = MibTableColumn
accXnsNetCost = _AccXnsNetCost_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 2, 1, 10),
    _AccXnsNetCost_Type()
)
accXnsNetCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNetCost.setStatus("mandatory")
_AccXnsNetX25InOutAddr_Type = DisplayString
_AccXnsNetX25InOutAddr_Object = MibTableColumn
accXnsNetX25InOutAddr = _AccXnsNetX25InOutAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 2, 1, 11),
    _AccXnsNetX25InOutAddr_Type()
)
accXnsNetX25InOutAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNetX25InOutAddr.setStatus("mandatory")
_AccXnsNetX25InAddr_Type = DisplayString
_AccXnsNetX25InAddr_Object = MibTableColumn
accXnsNetX25InAddr = _AccXnsNetX25InAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 2, 1, 12),
    _AccXnsNetX25InAddr_Type()
)
accXnsNetX25InAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNetX25InAddr.setStatus("mandatory")


class _AccXnsNetX25Idle_Type(TimeTicks):
    """Custom type accXnsNetX25Idle based on TimeTicks"""
    defaultValue = 30000


_AccXnsNetX25Idle_Object = MibTableColumn
accXnsNetX25Idle = _AccXnsNetX25Idle_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 2, 1, 13),
    _AccXnsNetX25Idle_Type()
)
accXnsNetX25Idle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNetX25Idle.setStatus("mandatory")


class _AccXnsNetX25PktVal_Type(Integer32):
    """Custom type accXnsNetX25PktVal based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_AccXnsNetX25PktVal_Type.__name__ = "Integer32"
_AccXnsNetX25PktVal_Object = MibTableColumn
accXnsNetX25PktVal = _AccXnsNetX25PktVal_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 2, 1, 14),
    _AccXnsNetX25PktVal_Type()
)
accXnsNetX25PktVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNetX25PktVal.setStatus("mandatory")


class _AccXnsNetX25PktWin_Type(Integer32):
    """Custom type accXnsNetX25PktWin based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_AccXnsNetX25PktWin_Type.__name__ = "Integer32"
_AccXnsNetX25PktWin_Object = MibTableColumn
accXnsNetX25PktWin = _AccXnsNetX25PktWin_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 2, 1, 15),
    _AccXnsNetX25PktWin_Type()
)
accXnsNetX25PktWin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNetX25PktWin.setStatus("mandatory")


class _AccXnsNetEntryStat_Type(Integer32):
    """Custom type accXnsNetEntryStat based on Integer32"""
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


_AccXnsNetEntryStat_Type.__name__ = "Integer32"
_AccXnsNetEntryStat_Object = MibTableColumn
accXnsNetEntryStat = _AccXnsNetEntryStat_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 2, 1, 16),
    _AccXnsNetEntryStat_Type()
)
accXnsNetEntryStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNetEntryStat.setStatus("mandatory")
_AccXnsNetUbUpdate_Type = TimeTicks
_AccXnsNetUbUpdate_Object = MibTableColumn
accXnsNetUbUpdate = _AccXnsNetUbUpdate_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 2, 1, 17),
    _AccXnsNetUbUpdate_Type()
)
accXnsNetUbUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNetUbUpdate.setStatus("mandatory")


class _AccXnsNetUbTtl_Type(TimeTicks):
    """Custom type accXnsNetUbTtl based on TimeTicks"""
    defaultValue = 1500


_AccXnsNetUbTtl_Object = MibTableColumn
accXnsNetUbTtl = _AccXnsNetUbTtl_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 2, 1, 18),
    _AccXnsNetUbTtl_Type()
)
accXnsNetUbTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNetUbTtl.setStatus("mandatory")
_AccXnsNetUbQT1_Type = TimeTicks
_AccXnsNetUbQT1_Object = MibTableColumn
accXnsNetUbQT1 = _AccXnsNetUbQT1_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 2, 1, 19),
    _AccXnsNetUbQT1_Type()
)
accXnsNetUbQT1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNetUbQT1.setStatus("mandatory")
_AccXnsNetUbQT2_Type = TimeTicks
_AccXnsNetUbQT2_Object = MibTableColumn
accXnsNetUbQT2 = _AccXnsNetUbQT2_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 2, 1, 20),
    _AccXnsNetUbQT2_Type()
)
accXnsNetUbQT2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNetUbQT2.setStatus("mandatory")
_AccXnsNetFncAddr_Type = OctetString
_AccXnsNetFncAddr_Object = MibTableColumn
accXnsNetFncAddr = _AccXnsNetFncAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 2, 1, 21),
    _AccXnsNetFncAddr_Type()
)
accXnsNetFncAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNetFncAddr.setStatus("mandatory")


class _AccXnsNetSrMode_Type(Integer32):
    """Custom type accXnsNetSrMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ape", 2),
          ("off", 1),
          ("spe", 3))
    )


_AccXnsNetSrMode_Type.__name__ = "Integer32"
_AccXnsNetSrMode_Object = MibTableColumn
accXnsNetSrMode = _AccXnsNetSrMode_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 2, 1, 22),
    _AccXnsNetSrMode_Type()
)
accXnsNetSrMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNetSrMode.setStatus("mandatory")


class _AccXnsNetX25FacIndex_Type(Integer32):
    """Custom type accXnsNetX25FacIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AccXnsNetX25FacIndex_Type.__name__ = "Integer32"
_AccXnsNetX25FacIndex_Object = MibTableColumn
accXnsNetX25FacIndex = _AccXnsNetX25FacIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 2, 1, 23),
    _AccXnsNetX25FacIndex_Type()
)
accXnsNetX25FacIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNetX25FacIndex.setStatus("mandatory")
_AccXnsNetDlci_Type = Integer32
_AccXnsNetDlci_Object = MibTableColumn
accXnsNetDlci = _AccXnsNetDlci_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 2, 1, 24),
    _AccXnsNetDlci_Type()
)
accXnsNetDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNetDlci.setStatus("mandatory")
_AccXnsRouteTable_Object = MibTable
accXnsRouteTable = _AccXnsRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 3)
)
if mibBuilder.loadTexts:
    accXnsRouteTable.setStatus("mandatory")
_AccXnsRouteEntry_Object = MibTableRow
accXnsRouteEntry = _AccXnsRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 3, 1)
)
accXnsRouteEntry.setIndexNames(
    (0, "ACC-XNS", "accXnsRtDest"),
)
if mibBuilder.loadTexts:
    accXnsRouteEntry.setStatus("mandatory")
_AccXnsRtDest_Type = OctetString
_AccXnsRtDest_Object = MibTableColumn
accXnsRtDest = _AccXnsRtDest_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 3, 1, 1),
    _AccXnsRtDest_Type()
)
accXnsRtDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsRtDest.setStatus("mandatory")
_AccXnsRtNxtNet_Type = OctetString
_AccXnsRtNxtNet_Object = MibTableColumn
accXnsRtNxtNet = _AccXnsRtNxtNet_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 3, 1, 2),
    _AccXnsRtNxtNet_Type()
)
accXnsRtNxtNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsRtNxtNet.setStatus("mandatory")
_AccXnsRtRouter_Type = OctetString
_AccXnsRtRouter_Object = MibTableColumn
accXnsRtRouter = _AccXnsRtRouter_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 3, 1, 3),
    _AccXnsRtRouter_Type()
)
accXnsRtRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsRtRouter.setStatus("mandatory")
_AccXnsRtHops_Type = Integer32
_AccXnsRtHops_Object = MibTableColumn
accXnsRtHops = _AccXnsRtHops_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 3, 1, 4),
    _AccXnsRtHops_Type()
)
accXnsRtHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsRtHops.setStatus("mandatory")
_AccXnsRtCost_Type = Integer32
_AccXnsRtCost_Object = MibTableColumn
accXnsRtCost = _AccXnsRtCost_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 3, 1, 5),
    _AccXnsRtCost_Type()
)
accXnsRtCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsRtCost.setStatus("mandatory")


class _AccXnsRtType_Type(Integer32):
    """Custom type accXnsRtType based on Integer32"""
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


_AccXnsRtType_Type.__name__ = "Integer32"
_AccXnsRtType_Object = MibTableColumn
accXnsRtType = _AccXnsRtType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 3, 1, 6),
    _AccXnsRtType_Type()
)
accXnsRtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsRtType.setStatus("mandatory")


class _AccXnsRtOwner_Type(Integer32):
    """Custom type accXnsRtOwner based on Integer32"""
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


_AccXnsRtOwner_Type.__name__ = "Integer32"
_AccXnsRtOwner_Object = MibTableColumn
accXnsRtOwner = _AccXnsRtOwner_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 3, 1, 7),
    _AccXnsRtOwner_Type()
)
accXnsRtOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsRtOwner.setStatus("mandatory")
_AccXnsRtAge_Type = TimeTicks
_AccXnsRtAge_Object = MibTableColumn
accXnsRtAge = _AccXnsRtAge_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 3, 1, 8),
    _AccXnsRtAge_Type()
)
accXnsRtAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsRtAge.setStatus("mandatory")
_AccXnsRtPort_Type = Integer32
_AccXnsRtPort_Object = MibTableColumn
accXnsRtPort = _AccXnsRtPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 3, 1, 9),
    _AccXnsRtPort_Type()
)
accXnsRtPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsRtPort.setStatus("mandatory")
_AccXnsRipStat_ObjectIdentity = ObjectIdentity
accXnsRipStat = _AccXnsRipStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 4)
)
_AccXnsRipReqIns_Type = Counter32
_AccXnsRipReqIns_Object = MibScalar
accXnsRipReqIns = _AccXnsRipReqIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 4, 1),
    _AccXnsRipReqIns_Type()
)
accXnsRipReqIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsRipReqIns.setStatus("mandatory")
_AccXnsRipRespIns_Type = Counter32
_AccXnsRipRespIns_Object = MibScalar
accXnsRipRespIns = _AccXnsRipRespIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 4, 2),
    _AccXnsRipRespIns_Type()
)
accXnsRipRespIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsRipRespIns.setStatus("mandatory")
_AccXnsRipReqOuts_Type = Counter32
_AccXnsRipReqOuts_Object = MibScalar
accXnsRipReqOuts = _AccXnsRipReqOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 4, 3),
    _AccXnsRipReqOuts_Type()
)
accXnsRipReqOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsRipReqOuts.setStatus("mandatory")
_AccXnsRipRespOuts_Type = Counter32
_AccXnsRipRespOuts_Object = MibScalar
accXnsRipRespOuts = _AccXnsRipRespOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 4, 4),
    _AccXnsRipRespOuts_Type()
)
accXnsRipRespOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsRipRespOuts.setStatus("mandatory")
_AccXnsRipInErrs_Type = Counter32
_AccXnsRipInErrs_Object = MibScalar
accXnsRipInErrs = _AccXnsRipInErrs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 4, 5),
    _AccXnsRipInErrs_Type()
)
accXnsRipInErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsRipInErrs.setStatus("mandatory")
_AccXnsRipOutErrs_Type = Counter32
_AccXnsRipOutErrs_Object = MibScalar
accXnsRipOutErrs = _AccXnsRipOutErrs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 4, 6),
    _AccXnsRipOutErrs_Type()
)
accXnsRipOutErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsRipOutErrs.setStatus("mandatory")
_AccXnsNodeStat_ObjectIdentity = ObjectIdentity
accXnsNodeStat = _AccXnsNodeStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 5)
)
_AccXnsLocalIns_Type = Counter32
_AccXnsLocalIns_Object = MibScalar
accXnsLocalIns = _AccXnsLocalIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 5, 1),
    _AccXnsLocalIns_Type()
)
accXnsLocalIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsLocalIns.setStatus("mandatory")
_AccXnsLocalOuts_Type = Counter32
_AccXnsLocalOuts_Object = MibScalar
accXnsLocalOuts = _AccXnsLocalOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 5, 2),
    _AccXnsLocalOuts_Type()
)
accXnsLocalOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsLocalOuts.setStatus("mandatory")
_AccXnsNoSockets_Type = Counter32
_AccXnsNoSockets_Object = MibScalar
accXnsNoSockets = _AccXnsNoSockets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 5, 3),
    _AccXnsNoSockets_Type()
)
accXnsNoSockets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsNoSockets.setStatus("mandatory")
_AccXnsNoRoutes_Type = Counter32
_AccXnsNoRoutes_Object = MibScalar
accXnsNoRoutes = _AccXnsNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 5, 4),
    _AccXnsNoRoutes_Type()
)
accXnsNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsNoRoutes.setStatus("mandatory")
_AccXnsNodeInErrs_Type = Counter32
_AccXnsNodeInErrs_Object = MibScalar
accXnsNodeInErrs = _AccXnsNodeInErrs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 5, 5),
    _AccXnsNodeInErrs_Type()
)
accXnsNodeInErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsNodeInErrs.setStatus("mandatory")
_AccXnsOutErrs_Type = Counter32
_AccXnsOutErrs_Object = MibScalar
accXnsOutErrs = _AccXnsOutErrs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 5, 6),
    _AccXnsOutErrs_Type()
)
accXnsOutErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsOutErrs.setStatus("mandatory")
_AccXnsAllNetsIns_Type = Counter32
_AccXnsAllNetsIns_Object = MibScalar
accXnsAllNetsIns = _AccXnsAllNetsIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 5, 7),
    _AccXnsAllNetsIns_Type()
)
accXnsAllNetsIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsAllNetsIns.setStatus("mandatory")
_AccXnsAllNetsOuts_Type = Counter32
_AccXnsAllNetsOuts_Object = MibScalar
accXnsAllNetsOuts = _AccXnsAllNetsOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 5, 8),
    _AccXnsAllNetsOuts_Type()
)
accXnsAllNetsOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsAllNetsOuts.setStatus("mandatory")
_AccXnsAllNetsErrs_Type = Counter32
_AccXnsAllNetsErrs_Object = MibScalar
accXnsAllNetsErrs = _AccXnsAllNetsErrs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 5, 9),
    _AccXnsAllNetsErrs_Type()
)
accXnsAllNetsErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsAllNetsErrs.setStatus("mandatory")
_AccXnsPortStatTable_Object = MibTable
accXnsPortStatTable = _AccXnsPortStatTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 6)
)
if mibBuilder.loadTexts:
    accXnsPortStatTable.setStatus("mandatory")
_AccXnsPortStatEntry_Object = MibTableRow
accXnsPortStatEntry = _AccXnsPortStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 6, 1)
)
accXnsPortStatEntry.setIndexNames(
    (0, "ACC-XNS", "accXnsPortNumber"),
)
if mibBuilder.loadTexts:
    accXnsPortStatEntry.setStatus("mandatory")
_AccXnsPortNumber_Type = Integer32
_AccXnsPortNumber_Object = MibTableColumn
accXnsPortNumber = _AccXnsPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 6, 1, 1),
    _AccXnsPortNumber_Type()
)
accXnsPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsPortNumber.setStatus("mandatory")
_AccXnsPortTotalIns_Type = Counter32
_AccXnsPortTotalIns_Object = MibTableColumn
accXnsPortTotalIns = _AccXnsPortTotalIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 6, 1, 2),
    _AccXnsPortTotalIns_Type()
)
accXnsPortTotalIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsPortTotalIns.setStatus("mandatory")
_AccXnsPorFwdReqIns_Type = Counter32
_AccXnsPorFwdReqIns_Object = MibTableColumn
accXnsPorFwdReqIns = _AccXnsPorFwdReqIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 6, 1, 3),
    _AccXnsPorFwdReqIns_Type()
)
accXnsPorFwdReqIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsPorFwdReqIns.setStatus("mandatory")
_AccXnsPortNoFwdRts_Type = Counter32
_AccXnsPortNoFwdRts_Object = MibTableColumn
accXnsPortNoFwdRts = _AccXnsPortNoFwdRts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 6, 1, 4),
    _AccXnsPortNoFwdRts_Type()
)
accXnsPortNoFwdRts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsPortNoFwdRts.setStatus("mandatory")
_AccXnsPortTotalOuts_Type = Counter32
_AccXnsPortTotalOuts_Object = MibTableColumn
accXnsPortTotalOuts = _AccXnsPortTotalOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 6, 1, 5),
    _AccXnsPortTotalOuts_Type()
)
accXnsPortTotalOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsPortTotalOuts.setStatus("mandatory")
_AccXnsPortHopCnts_Type = Counter32
_AccXnsPortHopCnts_Object = MibTableColumn
accXnsPortHopCnts = _AccXnsPortHopCnts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 6, 1, 6),
    _AccXnsPortHopCnts_Type()
)
accXnsPortHopCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsPortHopCnts.setStatus("mandatory")
_AccXnsPortNotForMes_Type = Counter32
_AccXnsPortNotForMes_Object = MibTableColumn
accXnsPortNotForMes = _AccXnsPortNotForMes_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 6, 1, 7),
    _AccXnsPortNotForMes_Type()
)
accXnsPortNotForMes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsPortNotForMes.setStatus("mandatory")
_AccXnsPortFwdReqOuts_Type = Counter32
_AccXnsPortFwdReqOuts_Object = MibTableColumn
accXnsPortFwdReqOuts = _AccXnsPortFwdReqOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 6, 1, 8),
    _AccXnsPortFwdReqOuts_Type()
)
accXnsPortFwdReqOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsPortFwdReqOuts.setStatus("mandatory")
_AccXnsPortFwdErrs_Type = Counter32
_AccXnsPortFwdErrs_Object = MibTableColumn
accXnsPortFwdErrs = _AccXnsPortFwdErrs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 6, 1, 9),
    _AccXnsPortFwdErrs_Type()
)
accXnsPortFwdErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsPortFwdErrs.setStatus("mandatory")
_AccXnsPortInErrs_Type = Counter32
_AccXnsPortInErrs_Object = MibTableColumn
accXnsPortInErrs = _AccXnsPortInErrs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 6, 1, 10),
    _AccXnsPortInErrs_Type()
)
accXnsPortInErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsPortInErrs.setStatus("mandatory")
_AccXnsPortTooShorts_Type = Counter32
_AccXnsPortTooShorts_Object = MibTableColumn
accXnsPortTooShorts = _AccXnsPortTooShorts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 6, 1, 11),
    _AccXnsPortTooShorts_Type()
)
accXnsPortTooShorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsPortTooShorts.setStatus("mandatory")
_AccXnsPortCkSums_Type = Counter32
_AccXnsPortCkSums_Object = MibTableColumn
accXnsPortCkSums = _AccXnsPortCkSums_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 6, 1, 12),
    _AccXnsPortCkSums_Type()
)
accXnsPortCkSums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsPortCkSums.setStatus("mandatory")
_AccXnsPortTooLongs_Type = Counter32
_AccXnsPortTooLongs_Object = MibTableColumn
accXnsPortTooLongs = _AccXnsPortTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 6, 1, 13),
    _AccXnsPortTooLongs_Type()
)
accXnsPortTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsPortTooLongs.setStatus("mandatory")
_AccXnsPortOutErrs_Type = Counter32
_AccXnsPortOutErrs_Object = MibTableColumn
accXnsPortOutErrs = _AccXnsPortOutErrs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 6, 1, 14),
    _AccXnsPortOutErrs_Type()
)
accXnsPortOutErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsPortOutErrs.setStatus("mandatory")


class _AccXnsPortOpState_Type(Integer32):
    """Custom type accXnsPortOpState based on Integer32"""
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


_AccXnsPortOpState_Type.__name__ = "Integer32"
_AccXnsPortOpState_Object = MibTableColumn
accXnsPortOpState = _AccXnsPortOpState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 6, 1, 15),
    _AccXnsPortOpState_Type()
)
accXnsPortOpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsPortOpState.setStatus("mandatory")
_AccXnsUbNbrTable_Object = MibTable
accXnsUbNbrTable = _AccXnsUbNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 7)
)
if mibBuilder.loadTexts:
    accXnsUbNbrTable.setStatus("mandatory")
_AccXnsUbNbrEntry_Object = MibTableRow
accXnsUbNbrEntry = _AccXnsUbNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 7, 1)
)
accXnsUbNbrEntry.setIndexNames(
    (0, "ACC-XNS", "accXnsUbnRmtNet"),
    (0, "ACC-XNS", "accXnsUbnLclNet"),
    (0, "ACC-XNS", "accXnsUbnRouter"),
)
if mibBuilder.loadTexts:
    accXnsUbNbrEntry.setStatus("mandatory")
_AccXnsUbnRmtNet_Type = OctetString
_AccXnsUbnRmtNet_Object = MibTableColumn
accXnsUbnRmtNet = _AccXnsUbnRmtNet_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 7, 1, 1),
    _AccXnsUbnRmtNet_Type()
)
accXnsUbnRmtNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsUbnRmtNet.setStatus("mandatory")
_AccXnsUbnLclNet_Type = OctetString
_AccXnsUbnLclNet_Object = MibTableColumn
accXnsUbnLclNet = _AccXnsUbnLclNet_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 7, 1, 2),
    _AccXnsUbnLclNet_Type()
)
accXnsUbnLclNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsUbnLclNet.setStatus("mandatory")
_AccXnsUbnRouter_Type = OctetString
_AccXnsUbnRouter_Object = MibTableColumn
accXnsUbnRouter = _AccXnsUbnRouter_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 7, 1, 3),
    _AccXnsUbnRouter_Type()
)
accXnsUbnRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsUbnRouter.setStatus("mandatory")
_AccXnsUbnHops_Type = Integer32
_AccXnsUbnHops_Object = MibTableColumn
accXnsUbnHops = _AccXnsUbnHops_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 7, 1, 4),
    _AccXnsUbnHops_Type()
)
accXnsUbnHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsUbnHops.setStatus("mandatory")
_AccXnsUbnCost_Type = Integer32
_AccXnsUbnCost_Object = MibTableColumn
accXnsUbnCost = _AccXnsUbnCost_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 7, 1, 5),
    _AccXnsUbnCost_Type()
)
accXnsUbnCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsUbnCost.setStatus("mandatory")


class _AccXnsUbnState_Type(Integer32):
    """Custom type accXnsUbnState based on Integer32"""
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
        *(("congested", 1),
          ("keepalive", 3),
          ("local", 0),
          ("uncongested", 2))
    )


_AccXnsUbnState_Type.__name__ = "Integer32"
_AccXnsUbnState_Object = MibTableColumn
accXnsUbnState = _AccXnsUbnState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 7, 1, 6),
    _AccXnsUbnState_Type()
)
accXnsUbnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsUbnState.setStatus("mandatory")
_AccXnsUbnTtl_Type = TimeTicks
_AccXnsUbnTtl_Object = MibTableColumn
accXnsUbnTtl = _AccXnsUbnTtl_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 7, 1, 7),
    _AccXnsUbnTtl_Type()
)
accXnsUbnTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsUbnTtl.setStatus("mandatory")
_AccXnsUbRip_ObjectIdentity = ObjectIdentity
accXnsUbRip = _AccXnsUbRip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 8)
)
_AccXnsUbRipRespIns_Type = Counter32
_AccXnsUbRipRespIns_Object = MibScalar
accXnsUbRipRespIns = _AccXnsUbRipRespIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 8, 1),
    _AccXnsUbRipRespIns_Type()
)
accXnsUbRipRespIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsUbRipRespIns.setStatus("mandatory")
_AccXnsUbRipHelloIns_Type = Counter32
_AccXnsUbRipHelloIns_Object = MibScalar
accXnsUbRipHelloIns = _AccXnsUbRipHelloIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 8, 2),
    _AccXnsUbRipHelloIns_Type()
)
accXnsUbRipHelloIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsUbRipHelloIns.setStatus("mandatory")
_AccXnsUbRipConHelIns_Type = Counter32
_AccXnsUbRipConHelIns_Object = MibScalar
accXnsUbRipConHelIns = _AccXnsUbRipConHelIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 8, 3),
    _AccXnsUbRipConHelIns_Type()
)
accXnsUbRipConHelIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsUbRipConHelIns.setStatus("mandatory")
_AccXnsUbRipUnConHelIns_Type = Counter32
_AccXnsUbRipUnConHelIns_Object = MibScalar
accXnsUbRipUnConHelIns = _AccXnsUbRipUnConHelIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 8, 4),
    _AccXnsUbRipUnConHelIns_Type()
)
accXnsUbRipUnConHelIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsUbRipUnConHelIns.setStatus("mandatory")
_AccXnsUbRipRedirIns_Type = Counter32
_AccXnsUbRipRedirIns_Object = MibScalar
accXnsUbRipRedirIns = _AccXnsUbRipRedirIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 8, 5),
    _AccXnsUbRipRedirIns_Type()
)
accXnsUbRipRedirIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsUbRipRedirIns.setStatus("mandatory")
_AccXnsUbRipRespOuts_Type = Counter32
_AccXnsUbRipRespOuts_Object = MibScalar
accXnsUbRipRespOuts = _AccXnsUbRipRespOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 8, 6),
    _AccXnsUbRipRespOuts_Type()
)
accXnsUbRipRespOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsUbRipRespOuts.setStatus("mandatory")
_AccXnsUbRipHelloOuts_Type = Counter32
_AccXnsUbRipHelloOuts_Object = MibScalar
accXnsUbRipHelloOuts = _AccXnsUbRipHelloOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 8, 7),
    _AccXnsUbRipHelloOuts_Type()
)
accXnsUbRipHelloOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsUbRipHelloOuts.setStatus("mandatory")
_AccXnsUbRipConHelOuts_Type = Counter32
_AccXnsUbRipConHelOuts_Object = MibScalar
accXnsUbRipConHelOuts = _AccXnsUbRipConHelOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 8, 8),
    _AccXnsUbRipConHelOuts_Type()
)
accXnsUbRipConHelOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsUbRipConHelOuts.setStatus("mandatory")
_AccXnsUbRipUnConHelOuts_Type = Counter32
_AccXnsUbRipUnConHelOuts_Object = MibScalar
accXnsUbRipUnConHelOuts = _AccXnsUbRipUnConHelOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 8, 9),
    _AccXnsUbRipUnConHelOuts_Type()
)
accXnsUbRipUnConHelOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsUbRipUnConHelOuts.setStatus("mandatory")
_AccXnsUbRipRedirOuts_Type = Counter32
_AccXnsUbRipRedirOuts_Object = MibScalar
accXnsUbRipRedirOuts = _AccXnsUbRipRedirOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 8, 10),
    _AccXnsUbRipRedirOuts_Type()
)
accXnsUbRipRedirOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsUbRipRedirOuts.setStatus("mandatory")
_AccXnsUbNoRoutes_Type = Counter32
_AccXnsUbNoRoutes_Object = MibScalar
accXnsUbNoRoutes = _AccXnsUbNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 8, 11),
    _AccXnsUbNoRoutes_Type()
)
accXnsUbNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsUbNoRoutes.setStatus("mandatory")
_AccXnsUbInErrs_Type = Counter32
_AccXnsUbInErrs_Object = MibScalar
accXnsUbInErrs = _AccXnsUbInErrs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 8, 12),
    _AccXnsUbInErrs_Type()
)
accXnsUbInErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsUbInErrs.setStatus("mandatory")
_AccXnsUbOutErrs_Type = Counter32
_AccXnsUbOutErrs_Object = MibScalar
accXnsUbOutErrs = _AccXnsUbOutErrs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 8, 13),
    _AccXnsUbOutErrs_Type()
)
accXnsUbOutErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsUbOutErrs.setStatus("mandatory")
_AccXnsRouteFilters_ObjectIdentity = ObjectIdentity
accXnsRouteFilters = _AccXnsRouteFilters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 9)
)


class _AccXnsRteFltrDefaultAction_Type(Integer32):
    """Custom type accXnsRteFltrDefaultAction based on Integer32"""
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


_AccXnsRteFltrDefaultAction_Type.__name__ = "Integer32"
_AccXnsRteFltrDefaultAction_Object = MibScalar
accXnsRteFltrDefaultAction = _AccXnsRteFltrDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 9, 1),
    _AccXnsRteFltrDefaultAction_Type()
)
accXnsRteFltrDefaultAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsRteFltrDefaultAction.setStatus("deprecated")
_AccXnsRteNbrTable_Object = MibTable
accXnsRteNbrTable = _AccXnsRteNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 9, 2)
)
if mibBuilder.loadTexts:
    accXnsRteNbrTable.setStatus("deprecated")
_AccXnsRteNbrEntry_Object = MibTableRow
accXnsRteNbrEntry = _AccXnsRteNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 9, 2, 1)
)
accXnsRteNbrEntry.setIndexNames(
    (0, "ACC-XNS", "accXnsRteNbrId"),
)
if mibBuilder.loadTexts:
    accXnsRteNbrEntry.setStatus("deprecated")
_AccXnsRteNbrId_Type = OctetString
_AccXnsRteNbrId_Object = MibTableColumn
accXnsRteNbrId = _AccXnsRteNbrId_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 9, 2, 1, 1),
    _AccXnsRteNbrId_Type()
)
accXnsRteNbrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsRteNbrId.setStatus("deprecated")


class _AccXnsRteNbrAction_Type(Integer32):
    """Custom type accXnsRteNbrAction based on Integer32"""
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


_AccXnsRteNbrAction_Type.__name__ = "Integer32"
_AccXnsRteNbrAction_Object = MibTableColumn
accXnsRteNbrAction = _AccXnsRteNbrAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 9, 2, 1, 2),
    _AccXnsRteNbrAction_Type()
)
accXnsRteNbrAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsRteNbrAction.setStatus("deprecated")


class _AccXnsRteNbrStatus_Type(Integer32):
    """Custom type accXnsRteNbrStatus based on Integer32"""
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


_AccXnsRteNbrStatus_Type.__name__ = "Integer32"
_AccXnsRteNbrStatus_Object = MibTableColumn
accXnsRteNbrStatus = _AccXnsRteNbrStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 9, 2, 1, 3),
    _AccXnsRteNbrStatus_Type()
)
accXnsRteNbrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsRteNbrStatus.setStatus("deprecated")
_AccXnsRteFltrTable_Object = MibTable
accXnsRteFltrTable = _AccXnsRteFltrTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 9, 3)
)
if mibBuilder.loadTexts:
    accXnsRteFltrTable.setStatus("deprecated")
_AccXnsRteFltrEntry_Object = MibTableRow
accXnsRteFltrEntry = _AccXnsRteFltrEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 9, 3, 1)
)
accXnsRteFltrEntry.setIndexNames(
    (0, "ACC-XNS", "accXnsRteFltrNeighbor"),
    (0, "ACC-XNS", "accXnsRteFltrNetwork"),
)
if mibBuilder.loadTexts:
    accXnsRteFltrEntry.setStatus("deprecated")
_AccXnsRteFltrNeighbor_Type = OctetString
_AccXnsRteFltrNeighbor_Object = MibTableColumn
accXnsRteFltrNeighbor = _AccXnsRteFltrNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 9, 3, 1, 1),
    _AccXnsRteFltrNeighbor_Type()
)
accXnsRteFltrNeighbor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsRteFltrNeighbor.setStatus("deprecated")
_AccXnsRteFltrNetwork_Type = OctetString
_AccXnsRteFltrNetwork_Object = MibTableColumn
accXnsRteFltrNetwork = _AccXnsRteFltrNetwork_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 9, 3, 1, 2),
    _AccXnsRteFltrNetwork_Type()
)
accXnsRteFltrNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsRteFltrNetwork.setStatus("deprecated")


class _AccXnsRteFltrAction_Type(Integer32):
    """Custom type accXnsRteFltrAction based on Integer32"""
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


_AccXnsRteFltrAction_Type.__name__ = "Integer32"
_AccXnsRteFltrAction_Object = MibTableColumn
accXnsRteFltrAction = _AccXnsRteFltrAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 9, 3, 1, 3),
    _AccXnsRteFltrAction_Type()
)
accXnsRteFltrAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsRteFltrAction.setStatus("deprecated")


class _AccXnsRteFltrStatus_Type(Integer32):
    """Custom type accXnsRteFltrStatus based on Integer32"""
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


_AccXnsRteFltrStatus_Type.__name__ = "Integer32"
_AccXnsRteFltrStatus_Object = MibTableColumn
accXnsRteFltrStatus = _AccXnsRteFltrStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 9, 3, 1, 4),
    _AccXnsRteFltrStatus_Type()
)
accXnsRteFltrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsRteFltrStatus.setStatus("deprecated")
_AccXnsNetworkFilters_ObjectIdentity = ObjectIdentity
accXnsNetworkFilters = _AccXnsNetworkFilters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 10)
)


class _AccXnsNetFltrDefaultAction_Type(Integer32):
    """Custom type accXnsNetFltrDefaultAction based on Integer32"""
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


_AccXnsNetFltrDefaultAction_Type.__name__ = "Integer32"
_AccXnsNetFltrDefaultAction_Object = MibScalar
accXnsNetFltrDefaultAction = _AccXnsNetFltrDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 10, 1),
    _AccXnsNetFltrDefaultAction_Type()
)
accXnsNetFltrDefaultAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNetFltrDefaultAction.setStatus("deprecated")
_OldXnsNetFltrTable_Object = MibTable
oldXnsNetFltrTable = _OldXnsNetFltrTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 10, 2)
)
if mibBuilder.loadTexts:
    oldXnsNetFltrTable.setStatus("deprecated")
_OldXnsNetFltrEntry_Object = MibTableRow
oldXnsNetFltrEntry = _OldXnsNetFltrEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 10, 2, 1)
)
oldXnsNetFltrEntry.setIndexNames(
    (0, "ACC-XNS", "oldXnsNetFltrDestination"),
    (0, "ACC-XNS", "oldXnsNetFltrSource"),
)
if mibBuilder.loadTexts:
    oldXnsNetFltrEntry.setStatus("deprecated")
_OldXnsNetFltrDestination_Type = OctetString
_OldXnsNetFltrDestination_Object = MibTableColumn
oldXnsNetFltrDestination = _OldXnsNetFltrDestination_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 10, 2, 1, 1),
    _OldXnsNetFltrDestination_Type()
)
oldXnsNetFltrDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oldXnsNetFltrDestination.setStatus("deprecated")
_OldXnsNetFltrSource_Type = OctetString
_OldXnsNetFltrSource_Object = MibTableColumn
oldXnsNetFltrSource = _OldXnsNetFltrSource_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 10, 2, 1, 2),
    _OldXnsNetFltrSource_Type()
)
oldXnsNetFltrSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oldXnsNetFltrSource.setStatus("deprecated")


class _OldXnsNetFltrAction_Type(Integer32):
    """Custom type oldXnsNetFltrAction based on Integer32"""
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


_OldXnsNetFltrAction_Type.__name__ = "Integer32"
_OldXnsNetFltrAction_Object = MibTableColumn
oldXnsNetFltrAction = _OldXnsNetFltrAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 10, 2, 1, 3),
    _OldXnsNetFltrAction_Type()
)
oldXnsNetFltrAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oldXnsNetFltrAction.setStatus("deprecated")


class _OldXnsNetFltrStatus_Type(Integer32):
    """Custom type oldXnsNetFltrStatus based on Integer32"""
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


_OldXnsNetFltrStatus_Type.__name__ = "Integer32"
_OldXnsNetFltrStatus_Object = MibTableColumn
oldXnsNetFltrStatus = _OldXnsNetFltrStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 10, 2, 1, 4),
    _OldXnsNetFltrStatus_Type()
)
oldXnsNetFltrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oldXnsNetFltrStatus.setStatus("deprecated")
_AccXnsNetFltrTable_Object = MibTable
accXnsNetFltrTable = _AccXnsNetFltrTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 10, 3)
)
if mibBuilder.loadTexts:
    accXnsNetFltrTable.setStatus("deprecated")
_AccXnsNetFltrEntry_Object = MibTableRow
accXnsNetFltrEntry = _AccXnsNetFltrEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 10, 3, 1)
)
accXnsNetFltrEntry.setIndexNames(
    (0, "ACC-XNS", "accXnsNetFltrDestination"),
    (0, "ACC-XNS", "accXnsNetFltrSource"),
    (0, "ACC-XNS", "accXnsNetFltrDestSkt"),
    (0, "ACC-XNS", "accXnsNetFltrSrcSkt"),
    (0, "ACC-XNS", "accXnsNetFltrPktType"),
)
if mibBuilder.loadTexts:
    accXnsNetFltrEntry.setStatus("deprecated")
_AccXnsNetFltrDestination_Type = OctetString
_AccXnsNetFltrDestination_Object = MibTableColumn
accXnsNetFltrDestination = _AccXnsNetFltrDestination_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 10, 3, 1, 1),
    _AccXnsNetFltrDestination_Type()
)
accXnsNetFltrDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNetFltrDestination.setStatus("deprecated")
_AccXnsNetFltrSource_Type = OctetString
_AccXnsNetFltrSource_Object = MibTableColumn
accXnsNetFltrSource = _AccXnsNetFltrSource_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 10, 3, 1, 2),
    _AccXnsNetFltrSource_Type()
)
accXnsNetFltrSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNetFltrSource.setStatus("deprecated")


class _AccXnsNetFltrAction_Type(Integer32):
    """Custom type accXnsNetFltrAction based on Integer32"""
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


_AccXnsNetFltrAction_Type.__name__ = "Integer32"
_AccXnsNetFltrAction_Object = MibTableColumn
accXnsNetFltrAction = _AccXnsNetFltrAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 10, 3, 1, 3),
    _AccXnsNetFltrAction_Type()
)
accXnsNetFltrAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNetFltrAction.setStatus("deprecated")


class _AccXnsNetFltrStatus_Type(Integer32):
    """Custom type accXnsNetFltrStatus based on Integer32"""
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


_AccXnsNetFltrStatus_Type.__name__ = "Integer32"
_AccXnsNetFltrStatus_Object = MibTableColumn
accXnsNetFltrStatus = _AccXnsNetFltrStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 10, 3, 1, 4),
    _AccXnsNetFltrStatus_Type()
)
accXnsNetFltrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNetFltrStatus.setStatus("deprecated")
_AccXnsNetFltrDestSkt_Type = OctetString
_AccXnsNetFltrDestSkt_Object = MibTableColumn
accXnsNetFltrDestSkt = _AccXnsNetFltrDestSkt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 10, 3, 1, 5),
    _AccXnsNetFltrDestSkt_Type()
)
accXnsNetFltrDestSkt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNetFltrDestSkt.setStatus("deprecated")
_AccXnsNetFltrSrcSkt_Type = OctetString
_AccXnsNetFltrSrcSkt_Object = MibTableColumn
accXnsNetFltrSrcSkt = _AccXnsNetFltrSrcSkt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 10, 3, 1, 6),
    _AccXnsNetFltrSrcSkt_Type()
)
accXnsNetFltrSrcSkt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNetFltrSrcSkt.setStatus("deprecated")
_AccXnsNetFltrPktType_Type = Integer32
_AccXnsNetFltrPktType_Object = MibTableColumn
accXnsNetFltrPktType = _AccXnsNetFltrPktType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 10, 3, 1, 7),
    _AccXnsNetFltrPktType_Type()
)
accXnsNetFltrPktType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNetFltrPktType.setStatus("deprecated")
_AccXnsHostFilters_ObjectIdentity = ObjectIdentity
accXnsHostFilters = _AccXnsHostFilters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 11)
)


class _AccXnsHostFltrDefaultAction_Type(Integer32):
    """Custom type accXnsHostFltrDefaultAction based on Integer32"""
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


_AccXnsHostFltrDefaultAction_Type.__name__ = "Integer32"
_AccXnsHostFltrDefaultAction_Object = MibScalar
accXnsHostFltrDefaultAction = _AccXnsHostFltrDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 11, 1),
    _AccXnsHostFltrDefaultAction_Type()
)
accXnsHostFltrDefaultAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsHostFltrDefaultAction.setStatus("deprecated")
_AccXnsHostFltrTable_Object = MibTable
accXnsHostFltrTable = _AccXnsHostFltrTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 11, 2)
)
if mibBuilder.loadTexts:
    accXnsHostFltrTable.setStatus("deprecated")
_AccXnsHostFltrEntry_Object = MibTableRow
accXnsHostFltrEntry = _AccXnsHostFltrEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 11, 2, 1)
)
accXnsHostFltrEntry.setIndexNames(
    (0, "ACC-XNS", "accXnsHostFltrId"),
    (0, "ACC-XNS", "accXnsHostFltrSocket"),
    (0, "ACC-XNS", "accXnsHostFltrPepClient"),
)
if mibBuilder.loadTexts:
    accXnsHostFltrEntry.setStatus("deprecated")
_AccXnsHostFltrId_Type = OctetString
_AccXnsHostFltrId_Object = MibTableColumn
accXnsHostFltrId = _AccXnsHostFltrId_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 11, 2, 1, 1),
    _AccXnsHostFltrId_Type()
)
accXnsHostFltrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsHostFltrId.setStatus("deprecated")
_AccXnsHostFltrSocket_Type = OctetString
_AccXnsHostFltrSocket_Object = MibTableColumn
accXnsHostFltrSocket = _AccXnsHostFltrSocket_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 11, 2, 1, 2),
    _AccXnsHostFltrSocket_Type()
)
accXnsHostFltrSocket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsHostFltrSocket.setStatus("deprecated")
_AccXnsHostFltrPepClient_Type = OctetString
_AccXnsHostFltrPepClient_Object = MibTableColumn
accXnsHostFltrPepClient = _AccXnsHostFltrPepClient_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 11, 2, 1, 3),
    _AccXnsHostFltrPepClient_Type()
)
accXnsHostFltrPepClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsHostFltrPepClient.setStatus("deprecated")


class _AccXnsHostFltrAction_Type(Integer32):
    """Custom type accXnsHostFltrAction based on Integer32"""
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


_AccXnsHostFltrAction_Type.__name__ = "Integer32"
_AccXnsHostFltrAction_Object = MibTableColumn
accXnsHostFltrAction = _AccXnsHostFltrAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 11, 2, 1, 4),
    _AccXnsHostFltrAction_Type()
)
accXnsHostFltrAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsHostFltrAction.setStatus("deprecated")


class _AccXnsHostFltrStatus_Type(Integer32):
    """Custom type accXnsHostFltrStatus based on Integer32"""
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


_AccXnsHostFltrStatus_Type.__name__ = "Integer32"
_AccXnsHostFltrStatus_Object = MibTableColumn
accXnsHostFltrStatus = _AccXnsHostFltrStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 11, 2, 1, 5),
    _AccXnsHostFltrStatus_Type()
)
accXnsHostFltrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsHostFltrStatus.setStatus("deprecated")
_AccXnsNamedRteFilters_ObjectIdentity = ObjectIdentity
accXnsNamedRteFilters = _AccXnsNamedRteFilters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 12)
)


class _AccXnsNamedRteFltrDefaultAction_Type(Integer32):
    """Custom type accXnsNamedRteFltrDefaultAction based on Integer32"""
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


_AccXnsNamedRteFltrDefaultAction_Type.__name__ = "Integer32"
_AccXnsNamedRteFltrDefaultAction_Object = MibScalar
accXnsNamedRteFltrDefaultAction = _AccXnsNamedRteFltrDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 12, 1),
    _AccXnsNamedRteFltrDefaultAction_Type()
)
accXnsNamedRteFltrDefaultAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNamedRteFltrDefaultAction.setStatus("mandatory")
_AccXnsNamedRteFltrTable_Object = MibTable
accXnsNamedRteFltrTable = _AccXnsNamedRteFltrTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 12, 2)
)
if mibBuilder.loadTexts:
    accXnsNamedRteFltrTable.setStatus("mandatory")
_AccXnsNamedRteFltrEntry_Object = MibTableRow
accXnsNamedRteFltrEntry = _AccXnsNamedRteFltrEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 12, 2, 1)
)
accXnsNamedRteFltrEntry.setIndexNames(
    (0, "ACC-XNS", "accXnsNamedRteFltrName"),
)
if mibBuilder.loadTexts:
    accXnsNamedRteFltrEntry.setStatus("mandatory")
_AccXnsNamedRteFltrNeighbor_Type = OctetString
_AccXnsNamedRteFltrNeighbor_Object = MibTableColumn
accXnsNamedRteFltrNeighbor = _AccXnsNamedRteFltrNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 12, 2, 1, 1),
    _AccXnsNamedRteFltrNeighbor_Type()
)
accXnsNamedRteFltrNeighbor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNamedRteFltrNeighbor.setStatus("mandatory")
_AccXnsNamedRteFltrNetwork_Type = OctetString
_AccXnsNamedRteFltrNetwork_Object = MibTableColumn
accXnsNamedRteFltrNetwork = _AccXnsNamedRteFltrNetwork_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 12, 2, 1, 2),
    _AccXnsNamedRteFltrNetwork_Type()
)
accXnsNamedRteFltrNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNamedRteFltrNetwork.setStatus("mandatory")
_AccXnsNamedRteFltrNetMask_Type = OctetString
_AccXnsNamedRteFltrNetMask_Object = MibTableColumn
accXnsNamedRteFltrNetMask = _AccXnsNamedRteFltrNetMask_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 12, 2, 1, 3),
    _AccXnsNamedRteFltrNetMask_Type()
)
accXnsNamedRteFltrNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNamedRteFltrNetMask.setStatus("mandatory")


class _AccXnsNamedRteFltrAction_Type(Integer32):
    """Custom type accXnsNamedRteFltrAction based on Integer32"""
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


_AccXnsNamedRteFltrAction_Type.__name__ = "Integer32"
_AccXnsNamedRteFltrAction_Object = MibTableColumn
accXnsNamedRteFltrAction = _AccXnsNamedRteFltrAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 12, 2, 1, 4),
    _AccXnsNamedRteFltrAction_Type()
)
accXnsNamedRteFltrAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNamedRteFltrAction.setStatus("mandatory")


class _AccXnsNamedRteFltrStatus_Type(Integer32):
    """Custom type accXnsNamedRteFltrStatus based on Integer32"""
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


_AccXnsNamedRteFltrStatus_Type.__name__ = "Integer32"
_AccXnsNamedRteFltrStatus_Object = MibTableColumn
accXnsNamedRteFltrStatus = _AccXnsNamedRteFltrStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 12, 2, 1, 5),
    _AccXnsNamedRteFltrStatus_Type()
)
accXnsNamedRteFltrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNamedRteFltrStatus.setStatus("mandatory")
_AccXnsNamedRteFltrName_Type = OctetString
_AccXnsNamedRteFltrName_Object = MibTableColumn
accXnsNamedRteFltrName = _AccXnsNamedRteFltrName_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 12, 2, 1, 6),
    _AccXnsNamedRteFltrName_Type()
)
accXnsNamedRteFltrName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNamedRteFltrName.setStatus("mandatory")


class _AccXnsNamedRteFltrPktDir_Type(Integer32):
    """Custom type accXnsNamedRteFltrPktDir based on Integer32"""
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


_AccXnsNamedRteFltrPktDir_Type.__name__ = "Integer32"
_AccXnsNamedRteFltrPktDir_Object = MibTableColumn
accXnsNamedRteFltrPktDir = _AccXnsNamedRteFltrPktDir_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 12, 2, 1, 7),
    _AccXnsNamedRteFltrPktDir_Type()
)
accXnsNamedRteFltrPktDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNamedRteFltrPktDir.setStatus("mandatory")
_AccXnsNamedRteFltrMatches_Type = Counter32
_AccXnsNamedRteFltrMatches_Object = MibTableColumn
accXnsNamedRteFltrMatches = _AccXnsNamedRteFltrMatches_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 12, 2, 1, 8),
    _AccXnsNamedRteFltrMatches_Type()
)
accXnsNamedRteFltrMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsNamedRteFltrMatches.setStatus("mandatory")
_AccXnsNamedRteFltrLastMatch_Type = TimeTicks
_AccXnsNamedRteFltrLastMatch_Object = MibTableColumn
accXnsNamedRteFltrLastMatch = _AccXnsNamedRteFltrLastMatch_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 12, 2, 1, 9),
    _AccXnsNamedRteFltrLastMatch_Type()
)
accXnsNamedRteFltrLastMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsNamedRteFltrLastMatch.setStatus("mandatory")
_AccXnsRteFltrApplTable_Object = MibTable
accXnsRteFltrApplTable = _AccXnsRteFltrApplTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 12, 3)
)
if mibBuilder.loadTexts:
    accXnsRteFltrApplTable.setStatus("mandatory")
_AccXnsRteFltrApplEntry_Object = MibTableRow
accXnsRteFltrApplEntry = _AccXnsRteFltrApplEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 12, 3, 1)
)
accXnsRteFltrApplEntry.setIndexNames(
    (0, "ACC-XNS", "accXnsRteFltrApplIfIndex"),
    (0, "ACC-XNS", "accXnsRteFltrApplPktDir"),
    (0, "ACC-XNS", "accXnsRteFltrApplSeqNum"),
)
if mibBuilder.loadTexts:
    accXnsRteFltrApplEntry.setStatus("mandatory")
_AccXnsRteFltrApplIfIndex_Type = Integer32
_AccXnsRteFltrApplIfIndex_Object = MibTableColumn
accXnsRteFltrApplIfIndex = _AccXnsRteFltrApplIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 12, 3, 1, 1),
    _AccXnsRteFltrApplIfIndex_Type()
)
accXnsRteFltrApplIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsRteFltrApplIfIndex.setStatus("mandatory")


class _AccXnsRteFltrApplPktDir_Type(Integer32):
    """Custom type accXnsRteFltrApplPktDir based on Integer32"""
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


_AccXnsRteFltrApplPktDir_Type.__name__ = "Integer32"
_AccXnsRteFltrApplPktDir_Object = MibTableColumn
accXnsRteFltrApplPktDir = _AccXnsRteFltrApplPktDir_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 12, 3, 1, 2),
    _AccXnsRteFltrApplPktDir_Type()
)
accXnsRteFltrApplPktDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsRteFltrApplPktDir.setStatus("mandatory")
_AccXnsRteFltrApplSeqNum_Type = Integer32
_AccXnsRteFltrApplSeqNum_Object = MibTableColumn
accXnsRteFltrApplSeqNum = _AccXnsRteFltrApplSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 12, 3, 1, 3),
    _AccXnsRteFltrApplSeqNum_Type()
)
accXnsRteFltrApplSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsRteFltrApplSeqNum.setStatus("mandatory")
_AccXnsRteFltrApplName_Type = DisplayString
_AccXnsRteFltrApplName_Object = MibTableColumn
accXnsRteFltrApplName = _AccXnsRteFltrApplName_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 12, 3, 1, 4),
    _AccXnsRteFltrApplName_Type()
)
accXnsRteFltrApplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsRteFltrApplName.setStatus("mandatory")
_AccXnsRteFltrApplMatches_Type = Counter32
_AccXnsRteFltrApplMatches_Object = MibTableColumn
accXnsRteFltrApplMatches = _AccXnsRteFltrApplMatches_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 12, 3, 1, 5),
    _AccXnsRteFltrApplMatches_Type()
)
accXnsRteFltrApplMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsRteFltrApplMatches.setStatus("mandatory")
_AccXnsRteFltrApplLastMatch_Type = TimeTicks
_AccXnsRteFltrApplLastMatch_Object = MibTableColumn
accXnsRteFltrApplLastMatch = _AccXnsRteFltrApplLastMatch_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 12, 3, 1, 6),
    _AccXnsRteFltrApplLastMatch_Type()
)
accXnsRteFltrApplLastMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsRteFltrApplLastMatch.setStatus("mandatory")
_AccXnsNamedNetworkFilters_ObjectIdentity = ObjectIdentity
accXnsNamedNetworkFilters = _AccXnsNamedNetworkFilters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 13)
)


class _AccXnsNamedNetFltrDefaultAction_Type(Integer32):
    """Custom type accXnsNamedNetFltrDefaultAction based on Integer32"""
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


_AccXnsNamedNetFltrDefaultAction_Type.__name__ = "Integer32"
_AccXnsNamedNetFltrDefaultAction_Object = MibScalar
accXnsNamedNetFltrDefaultAction = _AccXnsNamedNetFltrDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 13, 1),
    _AccXnsNamedNetFltrDefaultAction_Type()
)
accXnsNamedNetFltrDefaultAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNamedNetFltrDefaultAction.setStatus("mandatory")
_AccXnsNamedNetFltrTable_Object = MibTable
accXnsNamedNetFltrTable = _AccXnsNamedNetFltrTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 13, 2)
)
if mibBuilder.loadTexts:
    accXnsNamedNetFltrTable.setStatus("mandatory")
_AccXnsNamedNetFltrEntry_Object = MibTableRow
accXnsNamedNetFltrEntry = _AccXnsNamedNetFltrEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 13, 2, 1)
)
accXnsNamedNetFltrEntry.setIndexNames(
    (0, "ACC-XNS", "accXnsNamedNetFltrName"),
)
if mibBuilder.loadTexts:
    accXnsNamedNetFltrEntry.setStatus("mandatory")
_AccXnsNamedNetFltrDestination_Type = OctetString
_AccXnsNamedNetFltrDestination_Object = MibTableColumn
accXnsNamedNetFltrDestination = _AccXnsNamedNetFltrDestination_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 13, 2, 1, 1),
    _AccXnsNamedNetFltrDestination_Type()
)
accXnsNamedNetFltrDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNamedNetFltrDestination.setStatus("mandatory")
_AccXnsNamedNetFltrSource_Type = OctetString
_AccXnsNamedNetFltrSource_Object = MibTableColumn
accXnsNamedNetFltrSource = _AccXnsNamedNetFltrSource_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 13, 2, 1, 2),
    _AccXnsNamedNetFltrSource_Type()
)
accXnsNamedNetFltrSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNamedNetFltrSource.setStatus("mandatory")


class _AccXnsNamedNetFltrAction_Type(Integer32):
    """Custom type accXnsNamedNetFltrAction based on Integer32"""
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


_AccXnsNamedNetFltrAction_Type.__name__ = "Integer32"
_AccXnsNamedNetFltrAction_Object = MibTableColumn
accXnsNamedNetFltrAction = _AccXnsNamedNetFltrAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 13, 2, 1, 3),
    _AccXnsNamedNetFltrAction_Type()
)
accXnsNamedNetFltrAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNamedNetFltrAction.setStatus("mandatory")


class _AccXnsNamedNetFltrStatus_Type(Integer32):
    """Custom type accXnsNamedNetFltrStatus based on Integer32"""
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


_AccXnsNamedNetFltrStatus_Type.__name__ = "Integer32"
_AccXnsNamedNetFltrStatus_Object = MibTableColumn
accXnsNamedNetFltrStatus = _AccXnsNamedNetFltrStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 13, 2, 1, 4),
    _AccXnsNamedNetFltrStatus_Type()
)
accXnsNamedNetFltrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNamedNetFltrStatus.setStatus("mandatory")
_AccXnsNamedNetFltrDestSkt_Type = OctetString
_AccXnsNamedNetFltrDestSkt_Object = MibTableColumn
accXnsNamedNetFltrDestSkt = _AccXnsNamedNetFltrDestSkt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 13, 2, 1, 5),
    _AccXnsNamedNetFltrDestSkt_Type()
)
accXnsNamedNetFltrDestSkt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNamedNetFltrDestSkt.setStatus("mandatory")
_AccXnsNamedNetFltrSrcSkt_Type = OctetString
_AccXnsNamedNetFltrSrcSkt_Object = MibTableColumn
accXnsNamedNetFltrSrcSkt = _AccXnsNamedNetFltrSrcSkt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 13, 2, 1, 6),
    _AccXnsNamedNetFltrSrcSkt_Type()
)
accXnsNamedNetFltrSrcSkt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNamedNetFltrSrcSkt.setStatus("mandatory")
_AccXnsNamedNetFltrType_Type = Integer32
_AccXnsNamedNetFltrType_Object = MibTableColumn
accXnsNamedNetFltrType = _AccXnsNamedNetFltrType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 13, 2, 1, 7),
    _AccXnsNamedNetFltrType_Type()
)
accXnsNamedNetFltrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNamedNetFltrType.setStatus("mandatory")
_AccXnsNamedNetFltrName_Type = OctetString
_AccXnsNamedNetFltrName_Object = MibTableColumn
accXnsNamedNetFltrName = _AccXnsNamedNetFltrName_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 13, 2, 1, 8),
    _AccXnsNamedNetFltrName_Type()
)
accXnsNamedNetFltrName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNamedNetFltrName.setStatus("mandatory")


class _AccXnsNamedNetFltrPktDir_Type(Integer32):
    """Custom type accXnsNamedNetFltrPktDir based on Integer32"""
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


_AccXnsNamedNetFltrPktDir_Type.__name__ = "Integer32"
_AccXnsNamedNetFltrPktDir_Object = MibTableColumn
accXnsNamedNetFltrPktDir = _AccXnsNamedNetFltrPktDir_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 13, 2, 1, 9),
    _AccXnsNamedNetFltrPktDir_Type()
)
accXnsNamedNetFltrPktDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNamedNetFltrPktDir.setStatus("mandatory")
_AccXnsNamedNetFltrMatches_Type = Counter32
_AccXnsNamedNetFltrMatches_Object = MibTableColumn
accXnsNamedNetFltrMatches = _AccXnsNamedNetFltrMatches_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 13, 2, 1, 10),
    _AccXnsNamedNetFltrMatches_Type()
)
accXnsNamedNetFltrMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsNamedNetFltrMatches.setStatus("mandatory")
_AccXnsNamedNetFltrLastMatch_Type = TimeTicks
_AccXnsNamedNetFltrLastMatch_Object = MibTableColumn
accXnsNamedNetFltrLastMatch = _AccXnsNamedNetFltrLastMatch_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 13, 2, 1, 11),
    _AccXnsNamedNetFltrLastMatch_Type()
)
accXnsNamedNetFltrLastMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsNamedNetFltrLastMatch.setStatus("mandatory")
_AccXnsNamedNetFltrDestMask_Type = OctetString
_AccXnsNamedNetFltrDestMask_Object = MibTableColumn
accXnsNamedNetFltrDestMask = _AccXnsNamedNetFltrDestMask_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 13, 2, 1, 12),
    _AccXnsNamedNetFltrDestMask_Type()
)
accXnsNamedNetFltrDestMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNamedNetFltrDestMask.setStatus("mandatory")
_AccXnsNamedNetFltrSrcMask_Type = OctetString
_AccXnsNamedNetFltrSrcMask_Object = MibTableColumn
accXnsNamedNetFltrSrcMask = _AccXnsNamedNetFltrSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 13, 2, 1, 13),
    _AccXnsNamedNetFltrSrcMask_Type()
)
accXnsNamedNetFltrSrcMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNamedNetFltrSrcMask.setStatus("mandatory")
_AccXnsNetFltrApplTable_Object = MibTable
accXnsNetFltrApplTable = _AccXnsNetFltrApplTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 13, 3)
)
if mibBuilder.loadTexts:
    accXnsNetFltrApplTable.setStatus("mandatory")
_AccXnsNetFltrApplEntry_Object = MibTableRow
accXnsNetFltrApplEntry = _AccXnsNetFltrApplEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 13, 3, 1)
)
accXnsNetFltrApplEntry.setIndexNames(
    (0, "ACC-XNS", "accXnsNetFltrApplIfIndex"),
    (0, "ACC-XNS", "accXnsNetFltrApplPktDir"),
    (0, "ACC-XNS", "accXnsNetFltrApplSeqNum"),
)
if mibBuilder.loadTexts:
    accXnsNetFltrApplEntry.setStatus("mandatory")
_AccXnsNetFltrApplIfIndex_Type = Integer32
_AccXnsNetFltrApplIfIndex_Object = MibTableColumn
accXnsNetFltrApplIfIndex = _AccXnsNetFltrApplIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 13, 3, 1, 1),
    _AccXnsNetFltrApplIfIndex_Type()
)
accXnsNetFltrApplIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsNetFltrApplIfIndex.setStatus("mandatory")


class _AccXnsNetFltrApplPktDir_Type(Integer32):
    """Custom type accXnsNetFltrApplPktDir based on Integer32"""
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


_AccXnsNetFltrApplPktDir_Type.__name__ = "Integer32"
_AccXnsNetFltrApplPktDir_Object = MibTableColumn
accXnsNetFltrApplPktDir = _AccXnsNetFltrApplPktDir_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 13, 3, 1, 2),
    _AccXnsNetFltrApplPktDir_Type()
)
accXnsNetFltrApplPktDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsNetFltrApplPktDir.setStatus("mandatory")
_AccXnsNetFltrApplSeqNum_Type = Integer32
_AccXnsNetFltrApplSeqNum_Object = MibTableColumn
accXnsNetFltrApplSeqNum = _AccXnsNetFltrApplSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 13, 3, 1, 3),
    _AccXnsNetFltrApplSeqNum_Type()
)
accXnsNetFltrApplSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsNetFltrApplSeqNum.setStatus("mandatory")
_AccXnsNetFltrApplName_Type = DisplayString
_AccXnsNetFltrApplName_Object = MibTableColumn
accXnsNetFltrApplName = _AccXnsNetFltrApplName_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 13, 3, 1, 4),
    _AccXnsNetFltrApplName_Type()
)
accXnsNetFltrApplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsNetFltrApplName.setStatus("mandatory")
_AccXnsNetFltrApplMatches_Type = Counter32
_AccXnsNetFltrApplMatches_Object = MibTableColumn
accXnsNetFltrApplMatches = _AccXnsNetFltrApplMatches_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 13, 3, 1, 5),
    _AccXnsNetFltrApplMatches_Type()
)
accXnsNetFltrApplMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsNetFltrApplMatches.setStatus("mandatory")
_AccXnsNetFltrApplLastMatch_Type = TimeTicks
_AccXnsNetFltrApplLastMatch_Object = MibTableColumn
accXnsNetFltrApplLastMatch = _AccXnsNetFltrApplLastMatch_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 13, 3, 1, 6),
    _AccXnsNetFltrApplLastMatch_Type()
)
accXnsNetFltrApplLastMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsNetFltrApplLastMatch.setStatus("mandatory")
_AccXnsNamedHostFilters_ObjectIdentity = ObjectIdentity
accXnsNamedHostFilters = _AccXnsNamedHostFilters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 14)
)


class _AccXnsNamedHostFltrDefaultAction_Type(Integer32):
    """Custom type accXnsNamedHostFltrDefaultAction based on Integer32"""
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


_AccXnsNamedHostFltrDefaultAction_Type.__name__ = "Integer32"
_AccXnsNamedHostFltrDefaultAction_Object = MibScalar
accXnsNamedHostFltrDefaultAction = _AccXnsNamedHostFltrDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 14, 1),
    _AccXnsNamedHostFltrDefaultAction_Type()
)
accXnsNamedHostFltrDefaultAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNamedHostFltrDefaultAction.setStatus("mandatory")
_AccXnsNamedHostFltrTable_Object = MibTable
accXnsNamedHostFltrTable = _AccXnsNamedHostFltrTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 14, 2)
)
if mibBuilder.loadTexts:
    accXnsNamedHostFltrTable.setStatus("mandatory")
_AccXnsNamedHostFltrEntry_Object = MibTableRow
accXnsNamedHostFltrEntry = _AccXnsNamedHostFltrEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 14, 2, 1)
)
accXnsNamedHostFltrEntry.setIndexNames(
    (0, "ACC-XNS", "accXnsNamedHostFltrName"),
)
if mibBuilder.loadTexts:
    accXnsNamedHostFltrEntry.setStatus("mandatory")
_AccXnsNamedHostFltrId_Type = OctetString
_AccXnsNamedHostFltrId_Object = MibTableColumn
accXnsNamedHostFltrId = _AccXnsNamedHostFltrId_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 14, 2, 1, 1),
    _AccXnsNamedHostFltrId_Type()
)
accXnsNamedHostFltrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNamedHostFltrId.setStatus("mandatory")
_AccXnsNamedHostFltrSocket_Type = OctetString
_AccXnsNamedHostFltrSocket_Object = MibTableColumn
accXnsNamedHostFltrSocket = _AccXnsNamedHostFltrSocket_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 14, 2, 1, 2),
    _AccXnsNamedHostFltrSocket_Type()
)
accXnsNamedHostFltrSocket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNamedHostFltrSocket.setStatus("mandatory")
_AccXnsNamedHostFltrPepClient_Type = OctetString
_AccXnsNamedHostFltrPepClient_Object = MibTableColumn
accXnsNamedHostFltrPepClient = _AccXnsNamedHostFltrPepClient_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 14, 2, 1, 3),
    _AccXnsNamedHostFltrPepClient_Type()
)
accXnsNamedHostFltrPepClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNamedHostFltrPepClient.setStatus("mandatory")


class _AccXnsNamedHostFltrAction_Type(Integer32):
    """Custom type accXnsNamedHostFltrAction based on Integer32"""
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


_AccXnsNamedHostFltrAction_Type.__name__ = "Integer32"
_AccXnsNamedHostFltrAction_Object = MibTableColumn
accXnsNamedHostFltrAction = _AccXnsNamedHostFltrAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 14, 2, 1, 4),
    _AccXnsNamedHostFltrAction_Type()
)
accXnsNamedHostFltrAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNamedHostFltrAction.setStatus("mandatory")


class _AccXnsNamedHostFltrStatus_Type(Integer32):
    """Custom type accXnsNamedHostFltrStatus based on Integer32"""
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


_AccXnsNamedHostFltrStatus_Type.__name__ = "Integer32"
_AccXnsNamedHostFltrStatus_Object = MibTableColumn
accXnsNamedHostFltrStatus = _AccXnsNamedHostFltrStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 14, 2, 1, 5),
    _AccXnsNamedHostFltrStatus_Type()
)
accXnsNamedHostFltrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNamedHostFltrStatus.setStatus("mandatory")
_AccXnsNamedHostFltrName_Type = OctetString
_AccXnsNamedHostFltrName_Object = MibTableColumn
accXnsNamedHostFltrName = _AccXnsNamedHostFltrName_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 14, 2, 1, 6),
    _AccXnsNamedHostFltrName_Type()
)
accXnsNamedHostFltrName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNamedHostFltrName.setStatus("mandatory")


class _AccXnsNamedHostFltrPktDir_Type(Integer32):
    """Custom type accXnsNamedHostFltrPktDir based on Integer32"""
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


_AccXnsNamedHostFltrPktDir_Type.__name__ = "Integer32"
_AccXnsNamedHostFltrPktDir_Object = MibTableColumn
accXnsNamedHostFltrPktDir = _AccXnsNamedHostFltrPktDir_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 14, 2, 1, 7),
    _AccXnsNamedHostFltrPktDir_Type()
)
accXnsNamedHostFltrPktDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNamedHostFltrPktDir.setStatus("mandatory")
_AccXnsNamedHostFltrMatches_Type = Counter32
_AccXnsNamedHostFltrMatches_Object = MibTableColumn
accXnsNamedHostFltrMatches = _AccXnsNamedHostFltrMatches_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 14, 2, 1, 8),
    _AccXnsNamedHostFltrMatches_Type()
)
accXnsNamedHostFltrMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsNamedHostFltrMatches.setStatus("mandatory")
_AccXnsNamedHostFltrLastMatch_Type = TimeTicks
_AccXnsNamedHostFltrLastMatch_Object = MibTableColumn
accXnsNamedHostFltrLastMatch = _AccXnsNamedHostFltrLastMatch_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 14, 2, 1, 9),
    _AccXnsNamedHostFltrLastMatch_Type()
)
accXnsNamedHostFltrLastMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsNamedHostFltrLastMatch.setStatus("mandatory")
_AccXnsHostFltrApplTable_Object = MibTable
accXnsHostFltrApplTable = _AccXnsHostFltrApplTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 14, 3)
)
if mibBuilder.loadTexts:
    accXnsHostFltrApplTable.setStatus("mandatory")
_AccXnsHostFltrApplEntry_Object = MibTableRow
accXnsHostFltrApplEntry = _AccXnsHostFltrApplEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 14, 3, 1)
)
accXnsHostFltrApplEntry.setIndexNames(
    (0, "ACC-XNS", "accXnsHostFltrApplIfIndex"),
    (0, "ACC-XNS", "accXnsHostFltrApplPktDir"),
    (0, "ACC-XNS", "accXnsHostFltrApplSeqNum"),
)
if mibBuilder.loadTexts:
    accXnsHostFltrApplEntry.setStatus("mandatory")
_AccXnsHostFltrApplIfIndex_Type = Integer32
_AccXnsHostFltrApplIfIndex_Object = MibTableColumn
accXnsHostFltrApplIfIndex = _AccXnsHostFltrApplIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 14, 3, 1, 1),
    _AccXnsHostFltrApplIfIndex_Type()
)
accXnsHostFltrApplIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsHostFltrApplIfIndex.setStatus("mandatory")


class _AccXnsHostFltrApplPktDir_Type(Integer32):
    """Custom type accXnsHostFltrApplPktDir based on Integer32"""
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


_AccXnsHostFltrApplPktDir_Type.__name__ = "Integer32"
_AccXnsHostFltrApplPktDir_Object = MibTableColumn
accXnsHostFltrApplPktDir = _AccXnsHostFltrApplPktDir_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 14, 3, 1, 2),
    _AccXnsHostFltrApplPktDir_Type()
)
accXnsHostFltrApplPktDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsHostFltrApplPktDir.setStatus("mandatory")
_AccXnsHostFltrApplSeqNum_Type = Integer32
_AccXnsHostFltrApplSeqNum_Object = MibTableColumn
accXnsHostFltrApplSeqNum = _AccXnsHostFltrApplSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 14, 3, 1, 3),
    _AccXnsHostFltrApplSeqNum_Type()
)
accXnsHostFltrApplSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsHostFltrApplSeqNum.setStatus("mandatory")
_AccXnsHostFltrApplName_Type = DisplayString
_AccXnsHostFltrApplName_Object = MibTableColumn
accXnsHostFltrApplName = _AccXnsHostFltrApplName_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 14, 3, 1, 4),
    _AccXnsHostFltrApplName_Type()
)
accXnsHostFltrApplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsHostFltrApplName.setStatus("mandatory")
_AccXnsHostFltrApplMatches_Type = Counter32
_AccXnsHostFltrApplMatches_Object = MibTableColumn
accXnsHostFltrApplMatches = _AccXnsHostFltrApplMatches_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 14, 3, 1, 5),
    _AccXnsHostFltrApplMatches_Type()
)
accXnsHostFltrApplMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsHostFltrApplMatches.setStatus("mandatory")
_AccXnsHostFltrApplLastMatch_Type = TimeTicks
_AccXnsHostFltrApplLastMatch_Object = MibTableColumn
accXnsHostFltrApplLastMatch = _AccXnsHostFltrApplLastMatch_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 14, 3, 1, 6),
    _AccXnsHostFltrApplLastMatch_Type()
)
accXnsHostFltrApplLastMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsHostFltrApplLastMatch.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-XNS",
    **{"accXns": accXns,
       "accXnsParms": accXnsParms,
       "accXnsAdStat": accXnsAdStat,
       "accXnsCkSum": accXnsCkSum,
       "accXnsSpltHorz": accXnsSpltHorz,
       "accXnsAllNets": accXnsAllNets,
       "accXnsMode": accXnsMode,
       "accXnsNetTable": accXnsNetTable,
       "accXnsNetEntry": accXnsNetEntry,
       "accXnsNetPort": accXnsNetPort,
       "accXnsNetNumber": accXnsNetNumber,
       "accXnsNetType": accXnsNetType,
       "accXnsNetEncap": accXnsNetEncap,
       "accXnsNetSlot": accXnsNetSlot,
       "accXnsNetAdStat": accXnsNetAdStat,
       "accXnsNetMtu": accXnsNetMtu,
       "accXnsNetUpdate": accXnsNetUpdate,
       "accXnsNetHops": accXnsNetHops,
       "accXnsNetCost": accXnsNetCost,
       "accXnsNetX25InOutAddr": accXnsNetX25InOutAddr,
       "accXnsNetX25InAddr": accXnsNetX25InAddr,
       "accXnsNetX25Idle": accXnsNetX25Idle,
       "accXnsNetX25PktVal": accXnsNetX25PktVal,
       "accXnsNetX25PktWin": accXnsNetX25PktWin,
       "accXnsNetEntryStat": accXnsNetEntryStat,
       "accXnsNetUbUpdate": accXnsNetUbUpdate,
       "accXnsNetUbTtl": accXnsNetUbTtl,
       "accXnsNetUbQT1": accXnsNetUbQT1,
       "accXnsNetUbQT2": accXnsNetUbQT2,
       "accXnsNetFncAddr": accXnsNetFncAddr,
       "accXnsNetSrMode": accXnsNetSrMode,
       "accXnsNetX25FacIndex": accXnsNetX25FacIndex,
       "accXnsNetDlci": accXnsNetDlci,
       "accXnsRouteTable": accXnsRouteTable,
       "accXnsRouteEntry": accXnsRouteEntry,
       "accXnsRtDest": accXnsRtDest,
       "accXnsRtNxtNet": accXnsRtNxtNet,
       "accXnsRtRouter": accXnsRtRouter,
       "accXnsRtHops": accXnsRtHops,
       "accXnsRtCost": accXnsRtCost,
       "accXnsRtType": accXnsRtType,
       "accXnsRtOwner": accXnsRtOwner,
       "accXnsRtAge": accXnsRtAge,
       "accXnsRtPort": accXnsRtPort,
       "accXnsRipStat": accXnsRipStat,
       "accXnsRipReqIns": accXnsRipReqIns,
       "accXnsRipRespIns": accXnsRipRespIns,
       "accXnsRipReqOuts": accXnsRipReqOuts,
       "accXnsRipRespOuts": accXnsRipRespOuts,
       "accXnsRipInErrs": accXnsRipInErrs,
       "accXnsRipOutErrs": accXnsRipOutErrs,
       "accXnsNodeStat": accXnsNodeStat,
       "accXnsLocalIns": accXnsLocalIns,
       "accXnsLocalOuts": accXnsLocalOuts,
       "accXnsNoSockets": accXnsNoSockets,
       "accXnsNoRoutes": accXnsNoRoutes,
       "accXnsNodeInErrs": accXnsNodeInErrs,
       "accXnsOutErrs": accXnsOutErrs,
       "accXnsAllNetsIns": accXnsAllNetsIns,
       "accXnsAllNetsOuts": accXnsAllNetsOuts,
       "accXnsAllNetsErrs": accXnsAllNetsErrs,
       "accXnsPortStatTable": accXnsPortStatTable,
       "accXnsPortStatEntry": accXnsPortStatEntry,
       "accXnsPortNumber": accXnsPortNumber,
       "accXnsPortTotalIns": accXnsPortTotalIns,
       "accXnsPorFwdReqIns": accXnsPorFwdReqIns,
       "accXnsPortNoFwdRts": accXnsPortNoFwdRts,
       "accXnsPortTotalOuts": accXnsPortTotalOuts,
       "accXnsPortHopCnts": accXnsPortHopCnts,
       "accXnsPortNotForMes": accXnsPortNotForMes,
       "accXnsPortFwdReqOuts": accXnsPortFwdReqOuts,
       "accXnsPortFwdErrs": accXnsPortFwdErrs,
       "accXnsPortInErrs": accXnsPortInErrs,
       "accXnsPortTooShorts": accXnsPortTooShorts,
       "accXnsPortCkSums": accXnsPortCkSums,
       "accXnsPortTooLongs": accXnsPortTooLongs,
       "accXnsPortOutErrs": accXnsPortOutErrs,
       "accXnsPortOpState": accXnsPortOpState,
       "accXnsUbNbrTable": accXnsUbNbrTable,
       "accXnsUbNbrEntry": accXnsUbNbrEntry,
       "accXnsUbnRmtNet": accXnsUbnRmtNet,
       "accXnsUbnLclNet": accXnsUbnLclNet,
       "accXnsUbnRouter": accXnsUbnRouter,
       "accXnsUbnHops": accXnsUbnHops,
       "accXnsUbnCost": accXnsUbnCost,
       "accXnsUbnState": accXnsUbnState,
       "accXnsUbnTtl": accXnsUbnTtl,
       "accXnsUbRip": accXnsUbRip,
       "accXnsUbRipRespIns": accXnsUbRipRespIns,
       "accXnsUbRipHelloIns": accXnsUbRipHelloIns,
       "accXnsUbRipConHelIns": accXnsUbRipConHelIns,
       "accXnsUbRipUnConHelIns": accXnsUbRipUnConHelIns,
       "accXnsUbRipRedirIns": accXnsUbRipRedirIns,
       "accXnsUbRipRespOuts": accXnsUbRipRespOuts,
       "accXnsUbRipHelloOuts": accXnsUbRipHelloOuts,
       "accXnsUbRipConHelOuts": accXnsUbRipConHelOuts,
       "accXnsUbRipUnConHelOuts": accXnsUbRipUnConHelOuts,
       "accXnsUbRipRedirOuts": accXnsUbRipRedirOuts,
       "accXnsUbNoRoutes": accXnsUbNoRoutes,
       "accXnsUbInErrs": accXnsUbInErrs,
       "accXnsUbOutErrs": accXnsUbOutErrs,
       "accXnsRouteFilters": accXnsRouteFilters,
       "accXnsRteFltrDefaultAction": accXnsRteFltrDefaultAction,
       "accXnsRteNbrTable": accXnsRteNbrTable,
       "accXnsRteNbrEntry": accXnsRteNbrEntry,
       "accXnsRteNbrId": accXnsRteNbrId,
       "accXnsRteNbrAction": accXnsRteNbrAction,
       "accXnsRteNbrStatus": accXnsRteNbrStatus,
       "accXnsRteFltrTable": accXnsRteFltrTable,
       "accXnsRteFltrEntry": accXnsRteFltrEntry,
       "accXnsRteFltrNeighbor": accXnsRteFltrNeighbor,
       "accXnsRteFltrNetwork": accXnsRteFltrNetwork,
       "accXnsRteFltrAction": accXnsRteFltrAction,
       "accXnsRteFltrStatus": accXnsRteFltrStatus,
       "accXnsNetworkFilters": accXnsNetworkFilters,
       "accXnsNetFltrDefaultAction": accXnsNetFltrDefaultAction,
       "oldXnsNetFltrTable": oldXnsNetFltrTable,
       "oldXnsNetFltrEntry": oldXnsNetFltrEntry,
       "oldXnsNetFltrDestination": oldXnsNetFltrDestination,
       "oldXnsNetFltrSource": oldXnsNetFltrSource,
       "oldXnsNetFltrAction": oldXnsNetFltrAction,
       "oldXnsNetFltrStatus": oldXnsNetFltrStatus,
       "accXnsNetFltrTable": accXnsNetFltrTable,
       "accXnsNetFltrEntry": accXnsNetFltrEntry,
       "accXnsNetFltrDestination": accXnsNetFltrDestination,
       "accXnsNetFltrSource": accXnsNetFltrSource,
       "accXnsNetFltrAction": accXnsNetFltrAction,
       "accXnsNetFltrStatus": accXnsNetFltrStatus,
       "accXnsNetFltrDestSkt": accXnsNetFltrDestSkt,
       "accXnsNetFltrSrcSkt": accXnsNetFltrSrcSkt,
       "accXnsNetFltrPktType": accXnsNetFltrPktType,
       "accXnsHostFilters": accXnsHostFilters,
       "accXnsHostFltrDefaultAction": accXnsHostFltrDefaultAction,
       "accXnsHostFltrTable": accXnsHostFltrTable,
       "accXnsHostFltrEntry": accXnsHostFltrEntry,
       "accXnsHostFltrId": accXnsHostFltrId,
       "accXnsHostFltrSocket": accXnsHostFltrSocket,
       "accXnsHostFltrPepClient": accXnsHostFltrPepClient,
       "accXnsHostFltrAction": accXnsHostFltrAction,
       "accXnsHostFltrStatus": accXnsHostFltrStatus,
       "accXnsNamedRteFilters": accXnsNamedRteFilters,
       "accXnsNamedRteFltrDefaultAction": accXnsNamedRteFltrDefaultAction,
       "accXnsNamedRteFltrTable": accXnsNamedRteFltrTable,
       "accXnsNamedRteFltrEntry": accXnsNamedRteFltrEntry,
       "accXnsNamedRteFltrNeighbor": accXnsNamedRteFltrNeighbor,
       "accXnsNamedRteFltrNetwork": accXnsNamedRteFltrNetwork,
       "accXnsNamedRteFltrNetMask": accXnsNamedRteFltrNetMask,
       "accXnsNamedRteFltrAction": accXnsNamedRteFltrAction,
       "accXnsNamedRteFltrStatus": accXnsNamedRteFltrStatus,
       "accXnsNamedRteFltrName": accXnsNamedRteFltrName,
       "accXnsNamedRteFltrPktDir": accXnsNamedRteFltrPktDir,
       "accXnsNamedRteFltrMatches": accXnsNamedRteFltrMatches,
       "accXnsNamedRteFltrLastMatch": accXnsNamedRteFltrLastMatch,
       "accXnsRteFltrApplTable": accXnsRteFltrApplTable,
       "accXnsRteFltrApplEntry": accXnsRteFltrApplEntry,
       "accXnsRteFltrApplIfIndex": accXnsRteFltrApplIfIndex,
       "accXnsRteFltrApplPktDir": accXnsRteFltrApplPktDir,
       "accXnsRteFltrApplSeqNum": accXnsRteFltrApplSeqNum,
       "accXnsRteFltrApplName": accXnsRteFltrApplName,
       "accXnsRteFltrApplMatches": accXnsRteFltrApplMatches,
       "accXnsRteFltrApplLastMatch": accXnsRteFltrApplLastMatch,
       "accXnsNamedNetworkFilters": accXnsNamedNetworkFilters,
       "accXnsNamedNetFltrDefaultAction": accXnsNamedNetFltrDefaultAction,
       "accXnsNamedNetFltrTable": accXnsNamedNetFltrTable,
       "accXnsNamedNetFltrEntry": accXnsNamedNetFltrEntry,
       "accXnsNamedNetFltrDestination": accXnsNamedNetFltrDestination,
       "accXnsNamedNetFltrSource": accXnsNamedNetFltrSource,
       "accXnsNamedNetFltrAction": accXnsNamedNetFltrAction,
       "accXnsNamedNetFltrStatus": accXnsNamedNetFltrStatus,
       "accXnsNamedNetFltrDestSkt": accXnsNamedNetFltrDestSkt,
       "accXnsNamedNetFltrSrcSkt": accXnsNamedNetFltrSrcSkt,
       "accXnsNamedNetFltrType": accXnsNamedNetFltrType,
       "accXnsNamedNetFltrName": accXnsNamedNetFltrName,
       "accXnsNamedNetFltrPktDir": accXnsNamedNetFltrPktDir,
       "accXnsNamedNetFltrMatches": accXnsNamedNetFltrMatches,
       "accXnsNamedNetFltrLastMatch": accXnsNamedNetFltrLastMatch,
       "accXnsNamedNetFltrDestMask": accXnsNamedNetFltrDestMask,
       "accXnsNamedNetFltrSrcMask": accXnsNamedNetFltrSrcMask,
       "accXnsNetFltrApplTable": accXnsNetFltrApplTable,
       "accXnsNetFltrApplEntry": accXnsNetFltrApplEntry,
       "accXnsNetFltrApplIfIndex": accXnsNetFltrApplIfIndex,
       "accXnsNetFltrApplPktDir": accXnsNetFltrApplPktDir,
       "accXnsNetFltrApplSeqNum": accXnsNetFltrApplSeqNum,
       "accXnsNetFltrApplName": accXnsNetFltrApplName,
       "accXnsNetFltrApplMatches": accXnsNetFltrApplMatches,
       "accXnsNetFltrApplLastMatch": accXnsNetFltrApplLastMatch,
       "accXnsNamedHostFilters": accXnsNamedHostFilters,
       "accXnsNamedHostFltrDefaultAction": accXnsNamedHostFltrDefaultAction,
       "accXnsNamedHostFltrTable": accXnsNamedHostFltrTable,
       "accXnsNamedHostFltrEntry": accXnsNamedHostFltrEntry,
       "accXnsNamedHostFltrId": accXnsNamedHostFltrId,
       "accXnsNamedHostFltrSocket": accXnsNamedHostFltrSocket,
       "accXnsNamedHostFltrPepClient": accXnsNamedHostFltrPepClient,
       "accXnsNamedHostFltrAction": accXnsNamedHostFltrAction,
       "accXnsNamedHostFltrStatus": accXnsNamedHostFltrStatus,
       "accXnsNamedHostFltrName": accXnsNamedHostFltrName,
       "accXnsNamedHostFltrPktDir": accXnsNamedHostFltrPktDir,
       "accXnsNamedHostFltrMatches": accXnsNamedHostFltrMatches,
       "accXnsNamedHostFltrLastMatch": accXnsNamedHostFltrLastMatch,
       "accXnsHostFltrApplTable": accXnsHostFltrApplTable,
       "accXnsHostFltrApplEntry": accXnsHostFltrApplEntry,
       "accXnsHostFltrApplIfIndex": accXnsHostFltrApplIfIndex,
       "accXnsHostFltrApplPktDir": accXnsHostFltrApplPktDir,
       "accXnsHostFltrApplSeqNum": accXnsHostFltrApplSeqNum,
       "accXnsHostFltrApplName": accXnsHostFltrApplName,
       "accXnsHostFltrApplMatches": accXnsHostFltrApplMatches,
       "accXnsHostFltrApplLastMatch": accXnsHostFltrApplLastMatch}
)
