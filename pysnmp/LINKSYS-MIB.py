# SNMP MIB module (LINKSYS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LINKSYS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:18:23 2024
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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Linksys_ObjectIdentity = ObjectIdentity
linksys = _Linksys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3955)
)


class _DeviceId_Type(Integer32):
    """Custom type deviceId based on Integer32"""
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
        *(("isDualSpeedHub", 3),
          ("isEtherHub", 1),
          ("isFastEtherHub", 2),
          ("isNwayEtherSwitch", 4))
    )


_DeviceId_Type.__name__ = "Integer32"
_DeviceId_Object = MibScalar
deviceId = _DeviceId_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1),
    _DeviceId_Type()
)
deviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceId.setStatus("mandatory")
_EtherHub_ObjectIdentity = ObjectIdentity
etherHub = _EtherHub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3955, 5)
)
_EhHwVer_Type = Integer32
_EhHwVer_Object = MibScalar
ehHwVer = _EhHwVer_Object(
    (1, 3, 6, 1, 4, 1, 3955, 5, 2),
    _EhHwVer_Type()
)
ehHwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ehHwVer.setStatus("mandatory")
_EhSwVer_Type = Integer32
_EhSwVer_Object = MibScalar
ehSwVer = _EhSwVer_Object(
    (1, 3, 6, 1, 4, 1, 3955, 5, 3),
    _EhSwVer_Type()
)
ehSwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ehSwVer.setStatus("mandatory")
_EhNumber_Type = Integer32
_EhNumber_Object = MibScalar
ehNumber = _EhNumber_Object(
    (1, 3, 6, 1, 4, 1, 3955, 5, 4),
    _EhNumber_Type()
)
ehNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ehNumber.setStatus("mandatory")
_Sp2Hub_ObjectIdentity = ObjectIdentity
sp2Hub = _Sp2Hub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3955, 5, 5)
)
_Sp2Statistic_ObjectIdentity = ObjectIdentity
sp2Statistic = _Sp2Statistic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3955, 5, 5, 1)
)
_StatsOctets_Type = Counter64
_StatsOctets_Object = MibScalar
statsOctets = _StatsOctets_Object(
    (1, 3, 6, 1, 4, 1, 3955, 5, 5, 1, 1),
    _StatsOctets_Type()
)
statsOctets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    statsOctets.setStatus("mandatory")
_StatsPkts_Type = Integer32
_StatsPkts_Object = MibScalar
statsPkts = _StatsPkts_Object(
    (1, 3, 6, 1, 4, 1, 3955, 5, 5, 1, 2),
    _StatsPkts_Type()
)
statsPkts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    statsPkts.setStatus("mandatory")
_StatsBroadcastPkts_Type = Integer32
_StatsBroadcastPkts_Object = MibScalar
statsBroadcastPkts = _StatsBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3955, 5, 5, 1, 3),
    _StatsBroadcastPkts_Type()
)
statsBroadcastPkts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    statsBroadcastPkts.setStatus("mandatory")
_StatsMulticastPkts_Type = Integer32
_StatsMulticastPkts_Object = MibScalar
statsMulticastPkts = _StatsMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3955, 5, 5, 1, 4),
    _StatsMulticastPkts_Type()
)
statsMulticastPkts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    statsMulticastPkts.setStatus("mandatory")
_StatsCrcAlignErrors_Type = Integer32
_StatsCrcAlignErrors_Object = MibScalar
statsCrcAlignErrors = _StatsCrcAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 3955, 5, 5, 1, 5),
    _StatsCrcAlignErrors_Type()
)
statsCrcAlignErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    statsCrcAlignErrors.setStatus("mandatory")
_StatsUndersizePkts_Type = Integer32
_StatsUndersizePkts_Object = MibScalar
statsUndersizePkts = _StatsUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 3955, 5, 5, 1, 6),
    _StatsUndersizePkts_Type()
)
statsUndersizePkts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    statsUndersizePkts.setStatus("mandatory")
_StatsOversizePkts_Type = Integer32
_StatsOversizePkts_Object = MibScalar
statsOversizePkts = _StatsOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 3955, 5, 5, 1, 7),
    _StatsOversizePkts_Type()
)
statsOversizePkts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    statsOversizePkts.setStatus("mandatory")
_StatsFragments_Type = Integer32
_StatsFragments_Object = MibScalar
statsFragments = _StatsFragments_Object(
    (1, 3, 6, 1, 4, 1, 3955, 5, 5, 1, 8),
    _StatsFragments_Type()
)
statsFragments.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    statsFragments.setStatus("mandatory")
_StatsJabbers_Type = Integer32
_StatsJabbers_Object = MibScalar
statsJabbers = _StatsJabbers_Object(
    (1, 3, 6, 1, 4, 1, 3955, 5, 5, 1, 9),
    _StatsJabbers_Type()
)
statsJabbers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    statsJabbers.setStatus("mandatory")
_StatsCollisions_Type = Integer32
_StatsCollisions_Object = MibScalar
statsCollisions = _StatsCollisions_Object(
    (1, 3, 6, 1, 4, 1, 3955, 5, 5, 1, 10),
    _StatsCollisions_Type()
)
statsCollisions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    statsCollisions.setStatus("mandatory")
_StatsPkts64Octets_Type = Integer32
_StatsPkts64Octets_Object = MibScalar
statsPkts64Octets = _StatsPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 3955, 5, 5, 1, 11),
    _StatsPkts64Octets_Type()
)
statsPkts64Octets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    statsPkts64Octets.setStatus("mandatory")
_StatsPkts65to127Octets_Type = Integer32
_StatsPkts65to127Octets_Object = MibScalar
statsPkts65to127Octets = _StatsPkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 3955, 5, 5, 1, 12),
    _StatsPkts65to127Octets_Type()
)
statsPkts65to127Octets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    statsPkts65to127Octets.setStatus("mandatory")
_StatsPkts128to255Octets_Type = Integer32
_StatsPkts128to255Octets_Object = MibScalar
statsPkts128to255Octets = _StatsPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 3955, 5, 5, 1, 13),
    _StatsPkts128to255Octets_Type()
)
statsPkts128to255Octets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    statsPkts128to255Octets.setStatus("mandatory")
_StatsPkts256to511Octets_Type = Integer32
_StatsPkts256to511Octets_Object = MibScalar
statsPkts256to511Octets = _StatsPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 3955, 5, 5, 1, 14),
    _StatsPkts256to511Octets_Type()
)
statsPkts256to511Octets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    statsPkts256to511Octets.setStatus("mandatory")
_StatsPkts512to1023Octets_Type = Integer32
_StatsPkts512to1023Octets_Object = MibScalar
statsPkts512to1023Octets = _StatsPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 3955, 5, 5, 1, 15),
    _StatsPkts512to1023Octets_Type()
)
statsPkts512to1023Octets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    statsPkts512to1023Octets.setStatus("mandatory")
_StatsPkts1024to1518Octets_Type = Integer32
_StatsPkts1024to1518Octets_Object = MibScalar
statsPkts1024to1518Octets = _StatsPkts1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 3955, 5, 5, 1, 16),
    _StatsPkts1024to1518Octets_Type()
)
statsPkts1024to1518Octets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    statsPkts1024to1518Octets.setStatus("mandatory")
_StatsTotalValidOctets_Type = Counter64
_StatsTotalValidOctets_Object = MibScalar
statsTotalValidOctets = _StatsTotalValidOctets_Object(
    (1, 3, 6, 1, 4, 1, 3955, 5, 5, 1, 17),
    _StatsTotalValidOctets_Type()
)
statsTotalValidOctets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    statsTotalValidOctets.setStatus("mandatory")
_Sp2Control_Object = MibTable
sp2Control = _Sp2Control_Object(
    (1, 3, 6, 1, 4, 1, 3955, 5, 5, 2)
)
if mibBuilder.loadTexts:
    sp2Control.setStatus("mandatory")
_ResetModule_Type = Integer32
_ResetModule_Object = MibScalar
resetModule = _ResetModule_Object(
    (1, 3, 6, 1, 4, 1, 3955, 5, 5, 2, 1),
    _ResetModule_Type()
)
resetModule.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    resetModule.setStatus("mandatory")
_Sp2CtlEntry_Object = MibTableRow
sp2CtlEntry = _Sp2CtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 3955, 5, 5, 2, 2)
)
sp2CtlEntry.setIndexNames(
    (0, "LINKSYS-MIB", "ctlHubIdx"),
    (0, "LINKSYS-MIB", "ctlPortIdx"),
)
if mibBuilder.loadTexts:
    sp2CtlEntry.setStatus("deprecated")
_CtlHubIdx_Type = Integer32
_CtlHubIdx_Object = MibTableColumn
ctlHubIdx = _CtlHubIdx_Object(
    (1, 3, 6, 1, 4, 1, 3955, 5, 5, 2, 2, 1),
    _CtlHubIdx_Type()
)
ctlHubIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlHubIdx.setStatus("deprecated")
_CtlPortIdx_Type = Integer32
_CtlPortIdx_Object = MibTableColumn
ctlPortIdx = _CtlPortIdx_Object(
    (1, 3, 6, 1, 4, 1, 3955, 5, 5, 2, 2, 2),
    _CtlPortIdx_Type()
)
ctlPortIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctlPortIdx.setStatus("deprecated")


class _Enable_Type(Integer32):
    """Custom type enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("na", -1))
    )


_Enable_Type.__name__ = "Integer32"
_Enable_Object = MibTableColumn
enable = _Enable_Object(
    (1, 3, 6, 1, 4, 1, 3955, 5, 5, 2, 2, 3),
    _Enable_Type()
)
enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enable.setStatus("mandatory")


class _LinkEn_Type(Integer32):
    """Custom type linkEn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("na", -1))
    )


_LinkEn_Type.__name__ = "Integer32"
_LinkEn_Object = MibTableColumn
linkEn = _LinkEn_Object(
    (1, 3, 6, 1, 4, 1, 3955, 5, 5, 2, 2, 4),
    _LinkEn_Type()
)
linkEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linkEn.setStatus("mandatory")


class _SpeedSet_Type(Integer32):
    """Custom type speedSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ether10", 1),
          ("ether100", 3),
          ("na", -1),
          ("nway", 0))
    )


_SpeedSet_Type.__name__ = "Integer32"
_SpeedSet_Object = MibTableColumn
speedSet = _SpeedSet_Object(
    (1, 3, 6, 1, 4, 1, 3955, 5, 5, 2, 2, 5),
    _SpeedSet_Type()
)
speedSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    speedSet.setStatus("mandatory")


class _NwayEn_Type(Integer32):
    """Custom type nwayEn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("na", -1))
    )


_NwayEn_Type.__name__ = "Integer32"
_NwayEn_Object = MibTableColumn
nwayEn = _NwayEn_Object(
    (1, 3, 6, 1, 4, 1, 3955, 5, 5, 2, 2, 6),
    _NwayEn_Type()
)
nwayEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwayEn.setStatus("mandatory")
_NwayRestart_Type = Integer32
_NwayRestart_Object = MibTableColumn
nwayRestart = _NwayRestart_Object(
    (1, 3, 6, 1, 4, 1, 3955, 5, 5, 2, 2, 7),
    _NwayRestart_Type()
)
nwayRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwayRestart.setStatus("mandatory")
_Sp2Status_Object = MibTable
sp2Status = _Sp2Status_Object(
    (1, 3, 6, 1, 4, 1, 3955, 5, 5, 3)
)
if mibBuilder.loadTexts:
    sp2Status.setStatus("mandatory")
_Sp2StEntry_Object = MibTableRow
sp2StEntry = _Sp2StEntry_Object(
    (1, 3, 6, 1, 4, 1, 3955, 5, 5, 3, 1)
)
sp2StEntry.setIndexNames(
    (0, "LINKSYS-MIB", "statHubIdx"),
    (0, "LINKSYS-MIB", "statPortIdx"),
)
if mibBuilder.loadTexts:
    sp2StEntry.setStatus("mandatory")
_StatHubIdx_Type = Integer32
_StatHubIdx_Object = MibTableColumn
statHubIdx = _StatHubIdx_Object(
    (1, 3, 6, 1, 4, 1, 3955, 5, 5, 3, 1, 1),
    _StatHubIdx_Type()
)
statHubIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statHubIdx.setStatus("deprecated")
_StatPortIdx_Type = Integer32
_StatPortIdx_Object = MibTableColumn
statPortIdx = _StatPortIdx_Object(
    (1, 3, 6, 1, 4, 1, 3955, 5, 5, 3, 1, 2),
    _StatPortIdx_Type()
)
statPortIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statPortIdx.setStatus("deprecated")


class _LinkSt_Type(Integer32):
    """Custom type linkSt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fail", 0),
          ("good", 1),
          ("na", -1))
    )


_LinkSt_Type.__name__ = "Integer32"
_LinkSt_Object = MibTableColumn
linkSt = _LinkSt_Object(
    (1, 3, 6, 1, 4, 1, 3955, 5, 5, 3, 1, 3),
    _LinkSt_Type()
)
linkSt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkSt.setStatus("mandatory")


class _PolaritySt_Type(Integer32):
    """Custom type polaritySt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cross", 1),
          ("na", -1),
          ("straight", 0))
    )


_PolaritySt_Type.__name__ = "Integer32"
_PolaritySt_Object = MibTableColumn
polaritySt = _PolaritySt_Object(
    (1, 3, 6, 1, 4, 1, 3955, 5, 5, 3, 1, 4),
    _PolaritySt_Type()
)
polaritySt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    polaritySt.setStatus("mandatory")


class _PartitionSt_Type(Integer32):
    """Custom type partitionSt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("na", -1),
          ("no", 1),
          ("yes", 0))
    )


_PartitionSt_Type.__name__ = "Integer32"
_PartitionSt_Object = MibTableColumn
partitionSt = _PartitionSt_Object(
    (1, 3, 6, 1, 4, 1, 3955, 5, 5, 3, 1, 5),
    _PartitionSt_Type()
)
partitionSt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partitionSt.setStatus("mandatory")


class _SpeedSt_Type(Integer32):
    """Custom type speedSt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("is100M", 1),
          ("is10M", 0),
          ("na", -1))
    )


_SpeedSt_Type.__name__ = "Integer32"
_SpeedSt_Object = MibTableColumn
speedSt = _SpeedSt_Object(
    (1, 3, 6, 1, 4, 1, 3955, 5, 5, 3, 1, 6),
    _SpeedSt_Type()
)
speedSt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    speedSt.setStatus("mandatory")


class _NwayPartner_Type(Integer32):
    """Custom type nwayPartner based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("na", -1),
          ("no", 0),
          ("yes", 1))
    )


_NwayPartner_Type.__name__ = "Integer32"
_NwayPartner_Object = MibTableColumn
nwayPartner = _NwayPartner_Object(
    (1, 3, 6, 1, 4, 1, 3955, 5, 5, 3, 1, 7),
    _NwayPartner_Type()
)
nwayPartner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwayPartner.setStatus("mandatory")
_Sp2Ports_Object = MibTable
sp2Ports = _Sp2Ports_Object(
    (1, 3, 6, 1, 4, 1, 3955, 5, 5, 4)
)
if mibBuilder.loadTexts:
    sp2Ports.setStatus("mandatory")
_CounterEntry_Object = MibTableRow
counterEntry = _CounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 3955, 5, 5, 4, 1)
)
counterEntry.setIndexNames(
    (0, "LINKSYS-MIB", "cntHubIdx"),
    (0, "LINKSYS-MIB", "cntPortIdx"),
)
if mibBuilder.loadTexts:
    counterEntry.setStatus("mandatory")
_CntHubIdx_Type = Integer32
_CntHubIdx_Object = MibTableColumn
cntHubIdx = _CntHubIdx_Object(
    (1, 3, 6, 1, 4, 1, 3955, 5, 5, 4, 1, 1),
    _CntHubIdx_Type()
)
cntHubIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntHubIdx.setStatus("deprecated")
_CntPortIdx_Type = Integer32
_CntPortIdx_Object = MibTableColumn
cntPortIdx = _CntPortIdx_Object(
    (1, 3, 6, 1, 4, 1, 3955, 5, 5, 4, 1, 2),
    _CntPortIdx_Type()
)
cntPortIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntPortIdx.setStatus("mandatory")
_PortReadableFrames_Type = Counter32
_PortReadableFrames_Object = MibTableColumn
portReadableFrames = _PortReadableFrames_Object(
    (1, 3, 6, 1, 4, 1, 3955, 5, 5, 4, 1, 3),
    _PortReadableFrames_Type()
)
portReadableFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portReadableFrames.setStatus("mandatory")
_PortReadableOctets_Type = Counter64
_PortReadableOctets_Object = MibTableColumn
portReadableOctets = _PortReadableOctets_Object(
    (1, 3, 6, 1, 4, 1, 3955, 5, 5, 4, 1, 4),
    _PortReadableOctets_Type()
)
portReadableOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portReadableOctets.setStatus("mandatory")
_PortFrameCheckSequence_Type = Counter32
_PortFrameCheckSequence_Object = MibTableColumn
portFrameCheckSequence = _PortFrameCheckSequence_Object(
    (1, 3, 6, 1, 4, 1, 3955, 5, 5, 4, 1, 5),
    _PortFrameCheckSequence_Type()
)
portFrameCheckSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portFrameCheckSequence.setStatus("mandatory")
_PortAlignmentErrors_Type = Counter32
_PortAlignmentErrors_Object = MibTableColumn
portAlignmentErrors = _PortAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 3955, 5, 5, 4, 1, 6),
    _PortAlignmentErrors_Type()
)
portAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portAlignmentErrors.setStatus("mandatory")
_PortFramesTooLong_Type = Counter32
_PortFramesTooLong_Object = MibTableColumn
portFramesTooLong = _PortFramesTooLong_Object(
    (1, 3, 6, 1, 4, 1, 3955, 5, 5, 4, 1, 7),
    _PortFramesTooLong_Type()
)
portFramesTooLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portFramesTooLong.setStatus("mandatory")
_PortShortEvents_Type = Counter32
_PortShortEvents_Object = MibTableColumn
portShortEvents = _PortShortEvents_Object(
    (1, 3, 6, 1, 4, 1, 3955, 5, 5, 4, 1, 8),
    _PortShortEvents_Type()
)
portShortEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portShortEvents.setStatus("mandatory")
_PortRunts_Type = Counter32
_PortRunts_Object = MibTableColumn
portRunts = _PortRunts_Object(
    (1, 3, 6, 1, 4, 1, 3955, 5, 5, 4, 1, 9),
    _PortRunts_Type()
)
portRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portRunts.setStatus("mandatory")
_PortCollisions_Type = Counter32
_PortCollisions_Object = MibTableColumn
portCollisions = _PortCollisions_Object(
    (1, 3, 6, 1, 4, 1, 3955, 5, 5, 4, 1, 10),
    _PortCollisions_Type()
)
portCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCollisions.setStatus("mandatory")
_PortLateEvents_Type = Counter32
_PortLateEvents_Object = MibTableColumn
portLateEvents = _PortLateEvents_Object(
    (1, 3, 6, 1, 4, 1, 3955, 5, 5, 4, 1, 11),
    _PortLateEvents_Type()
)
portLateEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portLateEvents.setStatus("mandatory")
_PortVeryLongEvents_Type = Counter32
_PortVeryLongEvents_Object = MibTableColumn
portVeryLongEvents = _PortVeryLongEvents_Object(
    (1, 3, 6, 1, 4, 1, 3955, 5, 5, 4, 1, 12),
    _PortVeryLongEvents_Type()
)
portVeryLongEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portVeryLongEvents.setStatus("mandatory")
_PortDataRateMismatches_Type = Counter32
_PortDataRateMismatches_Object = MibTableColumn
portDataRateMismatches = _PortDataRateMismatches_Object(
    (1, 3, 6, 1, 4, 1, 3955, 5, 5, 4, 1, 13),
    _PortDataRateMismatches_Type()
)
portDataRateMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDataRateMismatches.setStatus("mandatory")
_PortAutoPartitions_Type = Counter32
_PortAutoPartitions_Object = MibTableColumn
portAutoPartitions = _PortAutoPartitions_Object(
    (1, 3, 6, 1, 4, 1, 3955, 5, 5, 4, 1, 14),
    _PortAutoPartitions_Type()
)
portAutoPartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portAutoPartitions.setStatus("mandatory")
_PortTrackSrcAddrChanges_Type = Counter32
_PortTrackSrcAddrChanges_Object = MibTableColumn
portTrackSrcAddrChanges = _PortTrackSrcAddrChanges_Object(
    (1, 3, 6, 1, 4, 1, 3955, 5, 5, 4, 1, 15),
    _PortTrackSrcAddrChanges_Type()
)
portTrackSrcAddrChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTrackSrcAddrChanges.setStatus("mandatory")
_PortBroadcastPkts_Type = Counter32
_PortBroadcastPkts_Object = MibTableColumn
portBroadcastPkts = _PortBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3955, 5, 5, 4, 1, 16),
    _PortBroadcastPkts_Type()
)
portBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portBroadcastPkts.setStatus("mandatory")
_PortMulticastPkts_Type = Counter32
_PortMulticastPkts_Object = MibTableColumn
portMulticastPkts = _PortMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3955, 5, 5, 4, 1, 17),
    _PortMulticastPkts_Type()
)
portMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMulticastPkts.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LINKSYS-MIB",
    **{"linksys": linksys,
       "deviceId": deviceId,
       "etherHub": etherHub,
       "ehHwVer": ehHwVer,
       "ehSwVer": ehSwVer,
       "ehNumber": ehNumber,
       "sp2Hub": sp2Hub,
       "sp2Statistic": sp2Statistic,
       "statsOctets": statsOctets,
       "statsPkts": statsPkts,
       "statsBroadcastPkts": statsBroadcastPkts,
       "statsMulticastPkts": statsMulticastPkts,
       "statsCrcAlignErrors": statsCrcAlignErrors,
       "statsUndersizePkts": statsUndersizePkts,
       "statsOversizePkts": statsOversizePkts,
       "statsFragments": statsFragments,
       "statsJabbers": statsJabbers,
       "statsCollisions": statsCollisions,
       "statsPkts64Octets": statsPkts64Octets,
       "statsPkts65to127Octets": statsPkts65to127Octets,
       "statsPkts128to255Octets": statsPkts128to255Octets,
       "statsPkts256to511Octets": statsPkts256to511Octets,
       "statsPkts512to1023Octets": statsPkts512to1023Octets,
       "statsPkts1024to1518Octets": statsPkts1024to1518Octets,
       "statsTotalValidOctets": statsTotalValidOctets,
       "sp2Control": sp2Control,
       "resetModule": resetModule,
       "sp2CtlEntry": sp2CtlEntry,
       "ctlHubIdx": ctlHubIdx,
       "ctlPortIdx": ctlPortIdx,
       "enable": enable,
       "linkEn": linkEn,
       "speedSet": speedSet,
       "nwayEn": nwayEn,
       "nwayRestart": nwayRestart,
       "sp2Status": sp2Status,
       "sp2StEntry": sp2StEntry,
       "statHubIdx": statHubIdx,
       "statPortIdx": statPortIdx,
       "linkSt": linkSt,
       "polaritySt": polaritySt,
       "partitionSt": partitionSt,
       "speedSt": speedSt,
       "nwayPartner": nwayPartner,
       "sp2Ports": sp2Ports,
       "counterEntry": counterEntry,
       "cntHubIdx": cntHubIdx,
       "cntPortIdx": cntPortIdx,
       "portReadableFrames": portReadableFrames,
       "portReadableOctets": portReadableOctets,
       "portFrameCheckSequence": portFrameCheckSequence,
       "portAlignmentErrors": portAlignmentErrors,
       "portFramesTooLong": portFramesTooLong,
       "portShortEvents": portShortEvents,
       "portRunts": portRunts,
       "portCollisions": portCollisions,
       "portLateEvents": portLateEvents,
       "portVeryLongEvents": portVeryLongEvents,
       "portDataRateMismatches": portDataRateMismatches,
       "portAutoPartitions": portAutoPartitions,
       "portTrackSrcAddrChanges": portTrackSrcAddrChanges,
       "portBroadcastPkts": portBroadcastPkts,
       "portMulticastPkts": portMulticastPkts}
)
