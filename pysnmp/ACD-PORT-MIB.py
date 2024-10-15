# SNMP MIB module (ACD-PORT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACD-PORT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:33:22 2024
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

(acdMibs,) = mibBuilder.importSymbols(
    "ACCEDIAN-SMI",
    "acdMibs")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

acdPort = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9)
)
acdPort.setRevisions(
        ("2011-10-10 01:00",
         "2010-10-01 01:00",
         "2008-05-01 01:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AcdPortMIBObjects_ObjectIdentity = ObjectIdentity
acdPortMIBObjects = _AcdPortMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1)
)
_AcdPortConfig_ObjectIdentity = ObjectIdentity
acdPortConfig = _AcdPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 1)
)
_AcdPortConfigTable_Object = MibTable
acdPortConfigTable = _AcdPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 1, 1)
)
if mibBuilder.loadTexts:
    acdPortConfigTable.setStatus("current")
_AcdPortConfigEntry_Object = MibTableRow
acdPortConfigEntry = _AcdPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 1, 1, 1)
)
acdPortConfigEntry.setIndexNames(
    (0, "ACD-PORT-MIB", "acdPortConfigIndex"),
)
if mibBuilder.loadTexts:
    acdPortConfigEntry.setStatus("current")


class _AcdPortConfigIndex_Type(Unsigned32):
    """Custom type acdPortConfigIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AcdPortConfigIndex_Type.__name__ = "Unsigned32"
_AcdPortConfigIndex_Object = MibTableColumn
acdPortConfigIndex = _AcdPortConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 1, 1, 1, 1),
    _AcdPortConfigIndex_Type()
)
acdPortConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdPortConfigIndex.setStatus("current")


class _AcdPortConfigName_Type(DisplayString):
    """Custom type acdPortConfigName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AcdPortConfigName_Type.__name__ = "DisplayString"
_AcdPortConfigName_Object = MibTableColumn
acdPortConfigName = _AcdPortConfigName_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 1, 1, 1, 2),
    _AcdPortConfigName_Type()
)
acdPortConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPortConfigName.setStatus("current")


class _AcdPortConfigAlias_Type(DisplayString):
    """Custom type acdPortConfigAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_AcdPortConfigAlias_Type.__name__ = "DisplayString"
_AcdPortConfigAlias_Object = MibTableColumn
acdPortConfigAlias = _AcdPortConfigAlias_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 1, 1, 1, 3),
    _AcdPortConfigAlias_Type()
)
acdPortConfigAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPortConfigAlias.setStatus("current")
_AcdPortConfigMacAddress_Type = MacAddress
_AcdPortConfigMacAddress_Object = MibTableColumn
acdPortConfigMacAddress = _AcdPortConfigMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 1, 1, 1, 4),
    _AcdPortConfigMacAddress_Type()
)
acdPortConfigMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortConfigMacAddress.setStatus("current")
_AcdPortConfigConnectorId_Type = ObjectIdentifier
_AcdPortConfigConnectorId_Object = MibTableColumn
acdPortConfigConnectorId = _AcdPortConfigConnectorId_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 1, 1, 1, 5),
    _AcdPortConfigConnectorId_Type()
)
acdPortConfigConnectorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortConfigConnectorId.setStatus("current")
_AcdPortConfigState_Type = TruthValue
_AcdPortConfigState_Object = MibTableColumn
acdPortConfigState = _AcdPortConfigState_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 1, 1, 1, 6),
    _AcdPortConfigState_Type()
)
acdPortConfigState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPortConfigState.setStatus("current")
_AcdPortConfigMtu_Type = Unsigned32
_AcdPortConfigMtu_Object = MibTableColumn
acdPortConfigMtu = _AcdPortConfigMtu_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 1, 1, 1, 7),
    _AcdPortConfigMtu_Type()
)
acdPortConfigMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPortConfigMtu.setStatus("current")
_AcdPortConfigAutoNegoState_Type = TruthValue
_AcdPortConfigAutoNegoState_Object = MibTableColumn
acdPortConfigAutoNegoState = _AcdPortConfigAutoNegoState_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 1, 1, 1, 8),
    _AcdPortConfigAutoNegoState_Type()
)
acdPortConfigAutoNegoState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPortConfigAutoNegoState.setStatus("current")
_AcdPortConfigSpeed_Type = Unsigned32
_AcdPortConfigSpeed_Object = MibTableColumn
acdPortConfigSpeed = _AcdPortConfigSpeed_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 1, 1, 1, 9),
    _AcdPortConfigSpeed_Type()
)
acdPortConfigSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPortConfigSpeed.setStatus("current")


class _AcdPortConfigDuplex_Type(Integer32):
    """Custom type acdPortConfigDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fullDuplex", 2),
          ("halfDuplex", 1))
    )


_AcdPortConfigDuplex_Type.__name__ = "Integer32"
_AcdPortConfigDuplex_Object = MibTableColumn
acdPortConfigDuplex = _AcdPortConfigDuplex_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 1, 1, 1, 10),
    _AcdPortConfigDuplex_Type()
)
acdPortConfigDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPortConfigDuplex.setStatus("current")


class _AcdPortConfigMdi_Type(Integer32):
    """Custom type acdPortConfigMdi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autoMdi", 1),
          ("mdi", 2),
          ("mdix", 3))
    )


_AcdPortConfigMdi_Type.__name__ = "Integer32"
_AcdPortConfigMdi_Object = MibTableColumn
acdPortConfigMdi = _AcdPortConfigMdi_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 1, 1, 1, 11),
    _AcdPortConfigMdi_Type()
)
acdPortConfigMdi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPortConfigMdi.setStatus("current")


class _AcdPortConfigPauseMode_Type(Integer32):
    """Custom type acdPortConfigPauseMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("forward", 3),
          ("local", 2))
    )


_AcdPortConfigPauseMode_Type.__name__ = "Integer32"
_AcdPortConfigPauseMode_Object = MibTableColumn
acdPortConfigPauseMode = _AcdPortConfigPauseMode_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 1, 1, 1, 12),
    _AcdPortConfigPauseMode_Type()
)
acdPortConfigPauseMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPortConfigPauseMode.setStatus("current")


class _AcdPortConfigAdvertisement_Type(Bits):
    """Custom type acdPortConfigAdvertisement based on Bits"""
    namedValues = NamedValues(
        *(("bFullDuplex100Mbps", 3),
          ("bFullDuplex10Mbps", 1),
          ("bFullDuplex1Gbps", 5),
          ("bHalfDuplex100Mbps", 2),
          ("bHalfDuplex10Mbps", 0),
          ("bHalfDuplex1Gbps", 4),
          ("bPauseAsymmetric", 7),
          ("bPauseSymmetric", 6))
    )

_AcdPortConfigAdvertisement_Type.__name__ = "Bits"
_AcdPortConfigAdvertisement_Object = MibTableColumn
acdPortConfigAdvertisement = _AcdPortConfigAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 1, 1, 1, 13),
    _AcdPortConfigAdvertisement_Type()
)
acdPortConfigAdvertisement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdPortConfigAdvertisement.setStatus("current")
_AcdPortStatus_ObjectIdentity = ObjectIdentity
acdPortStatus = _AcdPortStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 2)
)
_AcdPortStatusTable_Object = MibTable
acdPortStatusTable = _AcdPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 2, 1)
)
if mibBuilder.loadTexts:
    acdPortStatusTable.setStatus("current")
_AcdPortStatusEntry_Object = MibTableRow
acdPortStatusEntry = _AcdPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 2, 1, 1)
)
acdPortStatusEntry.setIndexNames(
    (0, "ACD-PORT-MIB", "acdPortStatusIndex"),
)
if mibBuilder.loadTexts:
    acdPortStatusEntry.setStatus("current")


class _AcdPortStatusIndex_Type(Unsigned32):
    """Custom type acdPortStatusIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AcdPortStatusIndex_Type.__name__ = "Unsigned32"
_AcdPortStatusIndex_Object = MibTableColumn
acdPortStatusIndex = _AcdPortStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 2, 1, 1, 1),
    _AcdPortStatusIndex_Type()
)
acdPortStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdPortStatusIndex.setStatus("current")
_AcdPortStatusSpeed_Type = Unsigned32
_AcdPortStatusSpeed_Object = MibTableColumn
acdPortStatusSpeed = _AcdPortStatusSpeed_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 2, 1, 1, 2),
    _AcdPortStatusSpeed_Type()
)
acdPortStatusSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortStatusSpeed.setStatus("current")


class _AcdPortStatusDuplex_Type(Integer32):
    """Custom type acdPortStatusDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fullDuplex", 2),
          ("halfDuplex", 1))
    )


_AcdPortStatusDuplex_Type.__name__ = "Integer32"
_AcdPortStatusDuplex_Object = MibTableColumn
acdPortStatusDuplex = _AcdPortStatusDuplex_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 2, 1, 1, 3),
    _AcdPortStatusDuplex_Type()
)
acdPortStatusDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortStatusDuplex.setStatus("current")


class _AcdPortStatusMdi_Type(Integer32):
    """Custom type acdPortStatusMdi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mdi", 1),
          ("mdix", 2))
    )


_AcdPortStatusMdi_Type.__name__ = "Integer32"
_AcdPortStatusMdi_Object = MibTableColumn
acdPortStatusMdi = _AcdPortStatusMdi_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 2, 1, 1, 4),
    _AcdPortStatusMdi_Type()
)
acdPortStatusMdi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortStatusMdi.setStatus("current")
_AcdPortStatusTxPause_Type = TruthValue
_AcdPortStatusTxPause_Object = MibTableColumn
acdPortStatusTxPause = _AcdPortStatusTxPause_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 2, 1, 1, 5),
    _AcdPortStatusTxPause_Type()
)
acdPortStatusTxPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortStatusTxPause.setStatus("current")
_AcdPortStatusRxPause_Type = TruthValue
_AcdPortStatusRxPause_Object = MibTableColumn
acdPortStatusRxPause = _AcdPortStatusRxPause_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 2, 1, 1, 6),
    _AcdPortStatusRxPause_Type()
)
acdPortStatusRxPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortStatusRxPause.setStatus("current")


class _AcdPortStatusLinkPartnerAbility_Type(Bits):
    """Custom type acdPortStatusLinkPartnerAbility based on Bits"""
    namedValues = NamedValues(
        *(("bFullDuplex100Mbps", 3),
          ("bFullDuplex10Mbps", 1),
          ("bFullDuplex1Gbps", 5),
          ("bHalfDuplex100Mbps", 2),
          ("bHalfDuplex10Mbps", 0),
          ("bHalfDuplex1Gbps", 4),
          ("bPauseAsymmetric", 7),
          ("bPauseSymmetric", 6))
    )

_AcdPortStatusLinkPartnerAbility_Type.__name__ = "Bits"
_AcdPortStatusLinkPartnerAbility_Object = MibTableColumn
acdPortStatusLinkPartnerAbility = _AcdPortStatusLinkPartnerAbility_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 2, 1, 1, 7),
    _AcdPortStatusLinkPartnerAbility_Type()
)
acdPortStatusLinkPartnerAbility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortStatusLinkPartnerAbility.setStatus("current")
_AcdPortStatusLinkStatus_Type = TruthValue
_AcdPortStatusLinkStatus_Object = MibTableColumn
acdPortStatusLinkStatus = _AcdPortStatusLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 2, 1, 1, 8),
    _AcdPortStatusLinkStatus_Type()
)
acdPortStatusLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortStatusLinkStatus.setStatus("current")


class _AcdPortStatusMedia_Type(Bits):
    """Custom type acdPortStatusMedia based on Bits"""
    namedValues = NamedValues(
        *(("b1000baseCXFD", 28),
          ("b1000baseCXHD", 27),
          ("b1000baseLXFD", 24),
          ("b1000baseLXHD", 23),
          ("b1000baseSXFD", 26),
          ("b1000baseSXHD", 25),
          ("b1000baseTFD", 30),
          ("b1000baseTHD", 29),
          ("b1000baseXFD", 22),
          ("b1000baseXHD", 21),
          ("b100baseFXFD", 18),
          ("b100baseFXHD", 17),
          ("b100baseT2FD", 20),
          ("b100baseT2HD", 19),
          ("b100baseT4", 14),
          ("b100baseTXFD", 16),
          ("b100baseTXHD", 15),
          ("b10base2", 4),
          ("b10base5", 2),
          ("b10baseFB", 7),
          ("b10baseFL", 8),
          ("b10baseFLFD", 13),
          ("b10baseFLHD", 12),
          ("b10baseFP", 6),
          ("b10baseT", 5),
          ("b10baseTFD", 11),
          ("b10baseTHD", 10),
          ("b10broad36", 9),
          ("bAUI", 1),
          ("bFoirl", 3),
          ("bOther", 0))
    )

_AcdPortStatusMedia_Type.__name__ = "Bits"
_AcdPortStatusMedia_Object = MibTableColumn
acdPortStatusMedia = _AcdPortStatusMedia_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 2, 1, 1, 9),
    _AcdPortStatusMedia_Type()
)
acdPortStatusMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortStatusMedia.setStatus("current")
_AcdPortStatusIsMonitor_Type = TruthValue
_AcdPortStatusIsMonitor_Object = MibTableColumn
acdPortStatusIsMonitor = _AcdPortStatusIsMonitor_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 2, 1, 1, 10),
    _AcdPortStatusIsMonitor_Type()
)
acdPortStatusIsMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortStatusIsMonitor.setStatus("current")
_AcdPortStatusIsManagement_Type = TruthValue
_AcdPortStatusIsManagement_Object = MibTableColumn
acdPortStatusIsManagement = _AcdPortStatusIsManagement_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 2, 1, 1, 11),
    _AcdPortStatusIsManagement_Type()
)
acdPortStatusIsManagement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortStatusIsManagement.setStatus("current")
_AcdPortStatusIsSFP_Type = TruthValue
_AcdPortStatusIsSFP_Object = MibTableColumn
acdPortStatusIsSFP = _AcdPortStatusIsSFP_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 2, 1, 1, 12),
    _AcdPortStatusIsSFP_Type()
)
acdPortStatusIsSFP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortStatusIsSFP.setStatus("current")
_AcdPortStatusIsFiber_Type = TruthValue
_AcdPortStatusIsFiber_Object = MibTableColumn
acdPortStatusIsFiber = _AcdPortStatusIsFiber_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 2, 1, 1, 13),
    _AcdPortStatusIsFiber_Type()
)
acdPortStatusIsFiber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortStatusIsFiber.setStatus("current")
_AcdPortStats_ObjectIdentity = ObjectIdentity
acdPortStats = _AcdPortStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3)
)
_AcdPortTxStatsTable_Object = MibTable
acdPortTxStatsTable = _AcdPortTxStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 1)
)
if mibBuilder.loadTexts:
    acdPortTxStatsTable.setStatus("current")
_AcdPortTxStatsEntry_Object = MibTableRow
acdPortTxStatsEntry = _AcdPortTxStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 1, 1)
)
acdPortTxStatsEntry.setIndexNames(
    (0, "ACD-PORT-MIB", "acdPortTxStatsIndex"),
)
if mibBuilder.loadTexts:
    acdPortTxStatsEntry.setStatus("current")


class _AcdPortTxStatsIndex_Type(Unsigned32):
    """Custom type acdPortTxStatsIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AcdPortTxStatsIndex_Type.__name__ = "Unsigned32"
_AcdPortTxStatsIndex_Object = MibTableColumn
acdPortTxStatsIndex = _AcdPortTxStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 1, 1, 1),
    _AcdPortTxStatsIndex_Type()
)
acdPortTxStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdPortTxStatsIndex.setStatus("current")


class _AcdPortTxStatsSupportBits_Type(Bits):
    """Custom type acdPortTxStatsSupportBits based on Bits"""
    namedValues = NamedValues(
        *(("bBroadcastPkts", 4),
          ("bBytesGood", 0),
          ("bBytesTotal", 1),
          ("bCRCErrors", 7),
          ("bDeferred", 8),
          ("bExcessiveCollisions", 12),
          ("bExcessiveDeferrals", 9),
          ("bFifoErrors", 15),
          ("bLateCollisions", 13),
          ("bMulticastPkts", 3),
          ("bMultipleCollisions", 11),
          ("bNormalCollisions", 14),
          ("bPauseFrames", 5),
          ("bPkts1024to1518", 21),
          ("bPkts128to255", 18),
          ("bPkts1519to2047", 22),
          ("bPkts2048to4095", 23),
          ("bPkts256to511", 19),
          ("bPkts4096to8191", 24),
          ("bPkts512to1023", 20),
          ("bPkts64", 16),
          ("bPkts65to127", 17),
          ("bPkts8192andMore", 25),
          ("bPktsLarge", 26),
          ("bSingleCollisions", 10),
          ("bTaggedFrames", 6),
          ("bUnicastPkts", 2))
    )

_AcdPortTxStatsSupportBits_Type.__name__ = "Bits"
_AcdPortTxStatsSupportBits_Object = MibTableColumn
acdPortTxStatsSupportBits = _AcdPortTxStatsSupportBits_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 1, 1, 2),
    _AcdPortTxStatsSupportBits_Type()
)
acdPortTxStatsSupportBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxStatsSupportBits.setStatus("current")
_AcdPortTxStatsBytesGood_Type = Counter64
_AcdPortTxStatsBytesGood_Object = MibTableColumn
acdPortTxStatsBytesGood = _AcdPortTxStatsBytesGood_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 1, 1, 3),
    _AcdPortTxStatsBytesGood_Type()
)
acdPortTxStatsBytesGood.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxStatsBytesGood.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxStatsBytesGood.setUnits("Octets")
_AcdPortTxStatsBytesTotal_Type = Counter64
_AcdPortTxStatsBytesTotal_Object = MibTableColumn
acdPortTxStatsBytesTotal = _AcdPortTxStatsBytesTotal_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 1, 1, 4),
    _AcdPortTxStatsBytesTotal_Type()
)
acdPortTxStatsBytesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxStatsBytesTotal.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxStatsBytesTotal.setUnits("Octets")
_AcdPortTxStatsUnicastPkts_Type = Counter64
_AcdPortTxStatsUnicastPkts_Object = MibTableColumn
acdPortTxStatsUnicastPkts = _AcdPortTxStatsUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 1, 1, 5),
    _AcdPortTxStatsUnicastPkts_Type()
)
acdPortTxStatsUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxStatsUnicastPkts.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxStatsUnicastPkts.setUnits("Packets")
_AcdPortTxStatsMulticastPkts_Type = Counter64
_AcdPortTxStatsMulticastPkts_Object = MibTableColumn
acdPortTxStatsMulticastPkts = _AcdPortTxStatsMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 1, 1, 6),
    _AcdPortTxStatsMulticastPkts_Type()
)
acdPortTxStatsMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxStatsMulticastPkts.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxStatsMulticastPkts.setUnits("Packets")
_AcdPortTxStatsBroadcastPkts_Type = Counter64
_AcdPortTxStatsBroadcastPkts_Object = MibTableColumn
acdPortTxStatsBroadcastPkts = _AcdPortTxStatsBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 1, 1, 7),
    _AcdPortTxStatsBroadcastPkts_Type()
)
acdPortTxStatsBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxStatsBroadcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxStatsBroadcastPkts.setUnits("Packets")
_AcdPortTxStatsPauseFrames_Type = Counter64
_AcdPortTxStatsPauseFrames_Object = MibTableColumn
acdPortTxStatsPauseFrames = _AcdPortTxStatsPauseFrames_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 1, 1, 8),
    _AcdPortTxStatsPauseFrames_Type()
)
acdPortTxStatsPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxStatsPauseFrames.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxStatsPauseFrames.setUnits("Packets")
_AcdPortTxStatsTaggedFrames_Type = Counter64
_AcdPortTxStatsTaggedFrames_Object = MibTableColumn
acdPortTxStatsTaggedFrames = _AcdPortTxStatsTaggedFrames_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 1, 1, 9),
    _AcdPortTxStatsTaggedFrames_Type()
)
acdPortTxStatsTaggedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxStatsTaggedFrames.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxStatsTaggedFrames.setUnits("Packets")
_AcdPortTxStatsCRCErrors_Type = Counter64
_AcdPortTxStatsCRCErrors_Object = MibTableColumn
acdPortTxStatsCRCErrors = _AcdPortTxStatsCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 1, 1, 10),
    _AcdPortTxStatsCRCErrors_Type()
)
acdPortTxStatsCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxStatsCRCErrors.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxStatsCRCErrors.setUnits("Packets")
_AcdPortTxStatsDeferred_Type = Counter64
_AcdPortTxStatsDeferred_Object = MibTableColumn
acdPortTxStatsDeferred = _AcdPortTxStatsDeferred_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 1, 1, 11),
    _AcdPortTxStatsDeferred_Type()
)
acdPortTxStatsDeferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxStatsDeferred.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxStatsDeferred.setUnits("Packets")
_AcdPortTxStatsExcessiveDeferrals_Type = Counter64
_AcdPortTxStatsExcessiveDeferrals_Object = MibTableColumn
acdPortTxStatsExcessiveDeferrals = _AcdPortTxStatsExcessiveDeferrals_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 1, 1, 12),
    _AcdPortTxStatsExcessiveDeferrals_Type()
)
acdPortTxStatsExcessiveDeferrals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxStatsExcessiveDeferrals.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxStatsExcessiveDeferrals.setUnits("Packets")
_AcdPortTxStatsSingleCollisions_Type = Counter64
_AcdPortTxStatsSingleCollisions_Object = MibTableColumn
acdPortTxStatsSingleCollisions = _AcdPortTxStatsSingleCollisions_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 1, 1, 13),
    _AcdPortTxStatsSingleCollisions_Type()
)
acdPortTxStatsSingleCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxStatsSingleCollisions.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxStatsSingleCollisions.setUnits("Packets")
_AcdPortTxStatsMultipleCollisions_Type = Counter64
_AcdPortTxStatsMultipleCollisions_Object = MibTableColumn
acdPortTxStatsMultipleCollisions = _AcdPortTxStatsMultipleCollisions_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 1, 1, 14),
    _AcdPortTxStatsMultipleCollisions_Type()
)
acdPortTxStatsMultipleCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxStatsMultipleCollisions.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxStatsMultipleCollisions.setUnits("Packets")
_AcdPortTxStatsExcessiveCollisions_Type = Counter64
_AcdPortTxStatsExcessiveCollisions_Object = MibTableColumn
acdPortTxStatsExcessiveCollisions = _AcdPortTxStatsExcessiveCollisions_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 1, 1, 15),
    _AcdPortTxStatsExcessiveCollisions_Type()
)
acdPortTxStatsExcessiveCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxStatsExcessiveCollisions.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxStatsExcessiveCollisions.setUnits("Packets")
_AcdPortTxStatsLateCollisions_Type = Counter64
_AcdPortTxStatsLateCollisions_Object = MibTableColumn
acdPortTxStatsLateCollisions = _AcdPortTxStatsLateCollisions_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 1, 1, 16),
    _AcdPortTxStatsLateCollisions_Type()
)
acdPortTxStatsLateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxStatsLateCollisions.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxStatsLateCollisions.setUnits("Packets")
_AcdPortTxStatsNormalCollisions_Type = Counter64
_AcdPortTxStatsNormalCollisions_Object = MibTableColumn
acdPortTxStatsNormalCollisions = _AcdPortTxStatsNormalCollisions_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 1, 1, 17),
    _AcdPortTxStatsNormalCollisions_Type()
)
acdPortTxStatsNormalCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxStatsNormalCollisions.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxStatsNormalCollisions.setUnits("Packets")
_AcdPortTxStatsFifoErrors_Type = Counter64
_AcdPortTxStatsFifoErrors_Object = MibTableColumn
acdPortTxStatsFifoErrors = _AcdPortTxStatsFifoErrors_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 1, 1, 18),
    _AcdPortTxStatsFifoErrors_Type()
)
acdPortTxStatsFifoErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxStatsFifoErrors.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxStatsFifoErrors.setUnits("Packets")
_AcdPortTxStatsPkts64_Type = Counter64
_AcdPortTxStatsPkts64_Object = MibTableColumn
acdPortTxStatsPkts64 = _AcdPortTxStatsPkts64_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 1, 1, 19),
    _AcdPortTxStatsPkts64_Type()
)
acdPortTxStatsPkts64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxStatsPkts64.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxStatsPkts64.setUnits("Packets")
_AcdPortTxStatsPkts65to127_Type = Counter64
_AcdPortTxStatsPkts65to127_Object = MibTableColumn
acdPortTxStatsPkts65to127 = _AcdPortTxStatsPkts65to127_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 1, 1, 20),
    _AcdPortTxStatsPkts65to127_Type()
)
acdPortTxStatsPkts65to127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxStatsPkts65to127.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxStatsPkts65to127.setUnits("Packets")
_AcdPortTxStatsPkts128to255_Type = Counter64
_AcdPortTxStatsPkts128to255_Object = MibTableColumn
acdPortTxStatsPkts128to255 = _AcdPortTxStatsPkts128to255_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 1, 1, 21),
    _AcdPortTxStatsPkts128to255_Type()
)
acdPortTxStatsPkts128to255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxStatsPkts128to255.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxStatsPkts128to255.setUnits("Packets")
_AcdPortTxStatsPkts256to511_Type = Counter64
_AcdPortTxStatsPkts256to511_Object = MibTableColumn
acdPortTxStatsPkts256to511 = _AcdPortTxStatsPkts256to511_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 1, 1, 22),
    _AcdPortTxStatsPkts256to511_Type()
)
acdPortTxStatsPkts256to511.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxStatsPkts256to511.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxStatsPkts256to511.setUnits("Packets")
_AcdPortTxStatsPkts512to1023_Type = Counter64
_AcdPortTxStatsPkts512to1023_Object = MibTableColumn
acdPortTxStatsPkts512to1023 = _AcdPortTxStatsPkts512to1023_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 1, 1, 23),
    _AcdPortTxStatsPkts512to1023_Type()
)
acdPortTxStatsPkts512to1023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxStatsPkts512to1023.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxStatsPkts512to1023.setUnits("Packets")
_AcdPortTxStatsPkts1024to1518_Type = Counter64
_AcdPortTxStatsPkts1024to1518_Object = MibTableColumn
acdPortTxStatsPkts1024to1518 = _AcdPortTxStatsPkts1024to1518_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 1, 1, 24),
    _AcdPortTxStatsPkts1024to1518_Type()
)
acdPortTxStatsPkts1024to1518.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxStatsPkts1024to1518.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxStatsPkts1024to1518.setUnits("Packets")
_AcdPortTxStatsPkts1519to2047_Type = Counter64
_AcdPortTxStatsPkts1519to2047_Object = MibTableColumn
acdPortTxStatsPkts1519to2047 = _AcdPortTxStatsPkts1519to2047_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 1, 1, 25),
    _AcdPortTxStatsPkts1519to2047_Type()
)
acdPortTxStatsPkts1519to2047.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxStatsPkts1519to2047.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxStatsPkts1519to2047.setUnits("Packets")
_AcdPortTxStatsPkts2048to4095_Type = Counter64
_AcdPortTxStatsPkts2048to4095_Object = MibTableColumn
acdPortTxStatsPkts2048to4095 = _AcdPortTxStatsPkts2048to4095_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 1, 1, 26),
    _AcdPortTxStatsPkts2048to4095_Type()
)
acdPortTxStatsPkts2048to4095.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxStatsPkts2048to4095.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxStatsPkts2048to4095.setUnits("Packets")
_AcdPortTxStatsPkts4096to8191_Type = Counter64
_AcdPortTxStatsPkts4096to8191_Object = MibTableColumn
acdPortTxStatsPkts4096to8191 = _AcdPortTxStatsPkts4096to8191_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 1, 1, 27),
    _AcdPortTxStatsPkts4096to8191_Type()
)
acdPortTxStatsPkts4096to8191.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxStatsPkts4096to8191.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxStatsPkts4096to8191.setUnits("Packets")
_AcdPortTxStatsPkts8192andMore_Type = Counter64
_AcdPortTxStatsPkts8192andMore_Object = MibTableColumn
acdPortTxStatsPkts8192andMore = _AcdPortTxStatsPkts8192andMore_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 1, 1, 28),
    _AcdPortTxStatsPkts8192andMore_Type()
)
acdPortTxStatsPkts8192andMore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxStatsPkts8192andMore.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxStatsPkts8192andMore.setUnits("Packets")
_AcdPortTxStatsPktsLarge_Type = Counter64
_AcdPortTxStatsPktsLarge_Object = MibTableColumn
acdPortTxStatsPktsLarge = _AcdPortTxStatsPktsLarge_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 1, 1, 29),
    _AcdPortTxStatsPktsLarge_Type()
)
acdPortTxStatsPktsLarge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortTxStatsPktsLarge.setStatus("current")
if mibBuilder.loadTexts:
    acdPortTxStatsPktsLarge.setUnits("Packets")
_AcdPortRxStatsTable_Object = MibTable
acdPortRxStatsTable = _AcdPortRxStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2)
)
if mibBuilder.loadTexts:
    acdPortRxStatsTable.setStatus("current")
_AcdPortRxStatsEntry_Object = MibTableRow
acdPortRxStatsEntry = _AcdPortRxStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1)
)
acdPortRxStatsEntry.setIndexNames(
    (0, "ACD-PORT-MIB", "acdPortRxStatsIndex"),
)
if mibBuilder.loadTexts:
    acdPortRxStatsEntry.setStatus("current")


class _AcdPortRxStatsIndex_Type(Unsigned32):
    """Custom type acdPortRxStatsIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AcdPortRxStatsIndex_Type.__name__ = "Unsigned32"
_AcdPortRxStatsIndex_Object = MibTableColumn
acdPortRxStatsIndex = _AcdPortRxStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1, 1),
    _AcdPortRxStatsIndex_Type()
)
acdPortRxStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdPortRxStatsIndex.setStatus("current")


class _AcdPortRxStatsSupportBits_Type(Bits):
    """Custom type acdPortRxStatsSupportBits based on Bits"""
    namedValues = NamedValues(
        *(("bAlignErrors", 12),
          ("bBadOpcode", 19),
          ("bBroadcastPkts", 8),
          ("bBytesGood", 0),
          ("bBytesTotal", 1),
          ("bCRCErrors", 11),
          ("bFalseCRS", 15),
          ("bFifoErrors", 17),
          ("bIgnored", 18),
          ("bLengthErrors", 14),
          ("bMulticastPkts", 7),
          ("bPauseFrames", 9),
          ("bPhyErrors", 16),
          ("bPkts1024to1518", 25),
          ("bPkts128to255", 22),
          ("bPkts1519to2047", 26),
          ("bPkts2048to4095", 27),
          ("bPkts256to511", 23),
          ("bPkts4096to8191", 28),
          ("bPkts512to1023", 24),
          ("bPkts64", 20),
          ("bPkts65to127", 21),
          ("bPkts8192andMore", 29),
          ("bPktsLarge", 30),
          ("bRuntFrames", 13),
          ("bRxStatsLongBad", 5),
          ("bRxStatsLongOk", 4),
          ("bRxStatsShortBad", 3),
          ("bRxStatsShortOk", 2),
          ("bTaggedFrames", 10),
          ("bUnicastPkts", 6))
    )

_AcdPortRxStatsSupportBits_Type.__name__ = "Bits"
_AcdPortRxStatsSupportBits_Object = MibTableColumn
acdPortRxStatsSupportBits = _AcdPortRxStatsSupportBits_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1, 2),
    _AcdPortRxStatsSupportBits_Type()
)
acdPortRxStatsSupportBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxStatsSupportBits.setStatus("current")
_AcdPortRxStatsBytesGood_Type = Counter64
_AcdPortRxStatsBytesGood_Object = MibTableColumn
acdPortRxStatsBytesGood = _AcdPortRxStatsBytesGood_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1, 3),
    _AcdPortRxStatsBytesGood_Type()
)
acdPortRxStatsBytesGood.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxStatsBytesGood.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxStatsBytesGood.setUnits("Octets")
_AcdPortRxStatsBytesTotal_Type = Counter64
_AcdPortRxStatsBytesTotal_Object = MibTableColumn
acdPortRxStatsBytesTotal = _AcdPortRxStatsBytesTotal_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1, 4),
    _AcdPortRxStatsBytesTotal_Type()
)
acdPortRxStatsBytesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxStatsBytesTotal.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxStatsBytesTotal.setUnits("Octets")
_AcdPortRxStatsShortOk_Type = Counter64
_AcdPortRxStatsShortOk_Object = MibTableColumn
acdPortRxStatsShortOk = _AcdPortRxStatsShortOk_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1, 5),
    _AcdPortRxStatsShortOk_Type()
)
acdPortRxStatsShortOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxStatsShortOk.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxStatsShortOk.setUnits("Packets")
_AcdPortRxStatsShortBad_Type = Counter64
_AcdPortRxStatsShortBad_Object = MibTableColumn
acdPortRxStatsShortBad = _AcdPortRxStatsShortBad_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1, 6),
    _AcdPortRxStatsShortBad_Type()
)
acdPortRxStatsShortBad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxStatsShortBad.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxStatsShortBad.setUnits("Packets")
_AcdPortRxStatsLongOk_Type = Counter64
_AcdPortRxStatsLongOk_Object = MibTableColumn
acdPortRxStatsLongOk = _AcdPortRxStatsLongOk_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1, 7),
    _AcdPortRxStatsLongOk_Type()
)
acdPortRxStatsLongOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxStatsLongOk.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxStatsLongOk.setUnits("Packets")
_AcdPortRxStatsLongBad_Type = Counter64
_AcdPortRxStatsLongBad_Object = MibTableColumn
acdPortRxStatsLongBad = _AcdPortRxStatsLongBad_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1, 8),
    _AcdPortRxStatsLongBad_Type()
)
acdPortRxStatsLongBad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxStatsLongBad.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxStatsLongBad.setUnits("Packets")
_AcdPortRxStatsUnicastPkts_Type = Counter64
_AcdPortRxStatsUnicastPkts_Object = MibTableColumn
acdPortRxStatsUnicastPkts = _AcdPortRxStatsUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1, 9),
    _AcdPortRxStatsUnicastPkts_Type()
)
acdPortRxStatsUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxStatsUnicastPkts.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxStatsUnicastPkts.setUnits("Packets")
_AcdPortRxStatsMulticastPkts_Type = Counter64
_AcdPortRxStatsMulticastPkts_Object = MibTableColumn
acdPortRxStatsMulticastPkts = _AcdPortRxStatsMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1, 10),
    _AcdPortRxStatsMulticastPkts_Type()
)
acdPortRxStatsMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxStatsMulticastPkts.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxStatsMulticastPkts.setUnits("Packets")
_AcdPortRxStatsBroadcastPkts_Type = Counter64
_AcdPortRxStatsBroadcastPkts_Object = MibTableColumn
acdPortRxStatsBroadcastPkts = _AcdPortRxStatsBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1, 11),
    _AcdPortRxStatsBroadcastPkts_Type()
)
acdPortRxStatsBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxStatsBroadcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxStatsBroadcastPkts.setUnits("Packets")
_AcdPortRxStatsPauseFrames_Type = Counter64
_AcdPortRxStatsPauseFrames_Object = MibTableColumn
acdPortRxStatsPauseFrames = _AcdPortRxStatsPauseFrames_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1, 12),
    _AcdPortRxStatsPauseFrames_Type()
)
acdPortRxStatsPauseFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxStatsPauseFrames.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxStatsPauseFrames.setUnits("Packets")
_AcdPortRxStatsTaggedFrames_Type = Counter64
_AcdPortRxStatsTaggedFrames_Object = MibTableColumn
acdPortRxStatsTaggedFrames = _AcdPortRxStatsTaggedFrames_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1, 13),
    _AcdPortRxStatsTaggedFrames_Type()
)
acdPortRxStatsTaggedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxStatsTaggedFrames.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxStatsTaggedFrames.setUnits("Packets")
_AcdPortRxStatsCRCErrors_Type = Counter64
_AcdPortRxStatsCRCErrors_Object = MibTableColumn
acdPortRxStatsCRCErrors = _AcdPortRxStatsCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1, 14),
    _AcdPortRxStatsCRCErrors_Type()
)
acdPortRxStatsCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxStatsCRCErrors.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxStatsCRCErrors.setUnits("Packets")
_AcdPortRxStatsAlignErrors_Type = Counter64
_AcdPortRxStatsAlignErrors_Object = MibTableColumn
acdPortRxStatsAlignErrors = _AcdPortRxStatsAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1, 15),
    _AcdPortRxStatsAlignErrors_Type()
)
acdPortRxStatsAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxStatsAlignErrors.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxStatsAlignErrors.setUnits("Packets")
_AcdPortRxStatsRuntFrames_Type = Counter64
_AcdPortRxStatsRuntFrames_Object = MibTableColumn
acdPortRxStatsRuntFrames = _AcdPortRxStatsRuntFrames_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1, 16),
    _AcdPortRxStatsRuntFrames_Type()
)
acdPortRxStatsRuntFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxStatsRuntFrames.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxStatsRuntFrames.setUnits("Packets")
_AcdPortRxStatsLengthErrors_Type = Counter64
_AcdPortRxStatsLengthErrors_Object = MibTableColumn
acdPortRxStatsLengthErrors = _AcdPortRxStatsLengthErrors_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1, 17),
    _AcdPortRxStatsLengthErrors_Type()
)
acdPortRxStatsLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxStatsLengthErrors.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxStatsLengthErrors.setUnits("Packets")
_AcdPortRxStatsFalseCRS_Type = Counter64
_AcdPortRxStatsFalseCRS_Object = MibTableColumn
acdPortRxStatsFalseCRS = _AcdPortRxStatsFalseCRS_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1, 18),
    _AcdPortRxStatsFalseCRS_Type()
)
acdPortRxStatsFalseCRS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxStatsFalseCRS.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxStatsFalseCRS.setUnits("Packets")
_AcdPortRxStatsPhyErrors_Type = Counter64
_AcdPortRxStatsPhyErrors_Object = MibTableColumn
acdPortRxStatsPhyErrors = _AcdPortRxStatsPhyErrors_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1, 19),
    _AcdPortRxStatsPhyErrors_Type()
)
acdPortRxStatsPhyErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxStatsPhyErrors.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxStatsPhyErrors.setUnits("Packets")
_AcdPortRxStatsFifoErrors_Type = Counter64
_AcdPortRxStatsFifoErrors_Object = MibTableColumn
acdPortRxStatsFifoErrors = _AcdPortRxStatsFifoErrors_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1, 20),
    _AcdPortRxStatsFifoErrors_Type()
)
acdPortRxStatsFifoErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxStatsFifoErrors.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxStatsFifoErrors.setUnits("Packets")
_AcdPortRxStatsIgnored_Type = Counter64
_AcdPortRxStatsIgnored_Object = MibTableColumn
acdPortRxStatsIgnored = _AcdPortRxStatsIgnored_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1, 21),
    _AcdPortRxStatsIgnored_Type()
)
acdPortRxStatsIgnored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxStatsIgnored.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxStatsIgnored.setUnits("Packets")
_AcdPortRxStatsBadOpcode_Type = Counter64
_AcdPortRxStatsBadOpcode_Object = MibTableColumn
acdPortRxStatsBadOpcode = _AcdPortRxStatsBadOpcode_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1, 22),
    _AcdPortRxStatsBadOpcode_Type()
)
acdPortRxStatsBadOpcode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxStatsBadOpcode.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxStatsBadOpcode.setUnits("Packets")
_AcdPortRxStatsPkts64_Type = Counter64
_AcdPortRxStatsPkts64_Object = MibTableColumn
acdPortRxStatsPkts64 = _AcdPortRxStatsPkts64_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1, 23),
    _AcdPortRxStatsPkts64_Type()
)
acdPortRxStatsPkts64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxStatsPkts64.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxStatsPkts64.setUnits("Packets")
_AcdPortRxStatsPkts65to127_Type = Counter64
_AcdPortRxStatsPkts65to127_Object = MibTableColumn
acdPortRxStatsPkts65to127 = _AcdPortRxStatsPkts65to127_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1, 24),
    _AcdPortRxStatsPkts65to127_Type()
)
acdPortRxStatsPkts65to127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxStatsPkts65to127.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxStatsPkts65to127.setUnits("Packets")
_AcdPortRxStatsPkts128to255_Type = Counter64
_AcdPortRxStatsPkts128to255_Object = MibTableColumn
acdPortRxStatsPkts128to255 = _AcdPortRxStatsPkts128to255_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1, 25),
    _AcdPortRxStatsPkts128to255_Type()
)
acdPortRxStatsPkts128to255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxStatsPkts128to255.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxStatsPkts128to255.setUnits("Packets")
_AcdPortRxStatsPkts256to511_Type = Counter64
_AcdPortRxStatsPkts256to511_Object = MibTableColumn
acdPortRxStatsPkts256to511 = _AcdPortRxStatsPkts256to511_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1, 26),
    _AcdPortRxStatsPkts256to511_Type()
)
acdPortRxStatsPkts256to511.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxStatsPkts256to511.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxStatsPkts256to511.setUnits("Packets")
_AcdPortRxStatsPkts512to1023_Type = Counter64
_AcdPortRxStatsPkts512to1023_Object = MibTableColumn
acdPortRxStatsPkts512to1023 = _AcdPortRxStatsPkts512to1023_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1, 27),
    _AcdPortRxStatsPkts512to1023_Type()
)
acdPortRxStatsPkts512to1023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxStatsPkts512to1023.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxStatsPkts512to1023.setUnits("Packets")
_AcdPortRxStatsPkts1024to1518_Type = Counter64
_AcdPortRxStatsPkts1024to1518_Object = MibTableColumn
acdPortRxStatsPkts1024to1518 = _AcdPortRxStatsPkts1024to1518_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1, 28),
    _AcdPortRxStatsPkts1024to1518_Type()
)
acdPortRxStatsPkts1024to1518.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxStatsPkts1024to1518.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxStatsPkts1024to1518.setUnits("Packets")
_AcdPortRxStatsPkts1519to2047_Type = Counter64
_AcdPortRxStatsPkts1519to2047_Object = MibTableColumn
acdPortRxStatsPkts1519to2047 = _AcdPortRxStatsPkts1519to2047_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1, 29),
    _AcdPortRxStatsPkts1519to2047_Type()
)
acdPortRxStatsPkts1519to2047.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxStatsPkts1519to2047.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxStatsPkts1519to2047.setUnits("Packets")
_AcdPortRxStatsPkts2048to4095_Type = Counter64
_AcdPortRxStatsPkts2048to4095_Object = MibTableColumn
acdPortRxStatsPkts2048to4095 = _AcdPortRxStatsPkts2048to4095_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1, 30),
    _AcdPortRxStatsPkts2048to4095_Type()
)
acdPortRxStatsPkts2048to4095.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxStatsPkts2048to4095.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxStatsPkts2048to4095.setUnits("Packets")
_AcdPortRxStatsPkts4096to8191_Type = Counter64
_AcdPortRxStatsPkts4096to8191_Object = MibTableColumn
acdPortRxStatsPkts4096to8191 = _AcdPortRxStatsPkts4096to8191_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1, 31),
    _AcdPortRxStatsPkts4096to8191_Type()
)
acdPortRxStatsPkts4096to8191.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxStatsPkts4096to8191.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxStatsPkts4096to8191.setUnits("Packets")
_AcdPortRxStatsPkts8192andMore_Type = Counter64
_AcdPortRxStatsPkts8192andMore_Object = MibTableColumn
acdPortRxStatsPkts8192andMore = _AcdPortRxStatsPkts8192andMore_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1, 32),
    _AcdPortRxStatsPkts8192andMore_Type()
)
acdPortRxStatsPkts8192andMore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxStatsPkts8192andMore.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxStatsPkts8192andMore.setUnits("Packets")
_AcdPortRxStatsPktsLarge_Type = Counter64
_AcdPortRxStatsPktsLarge_Object = MibTableColumn
acdPortRxStatsPktsLarge = _AcdPortRxStatsPktsLarge_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 3, 2, 1, 33),
    _AcdPortRxStatsPktsLarge_Type()
)
acdPortRxStatsPktsLarge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortRxStatsPktsLarge.setStatus("current")
if mibBuilder.loadTexts:
    acdPortRxStatsPktsLarge.setUnits("Packets")
_AcdPortTableTid_ObjectIdentity = ObjectIdentity
acdPortTableTid = _AcdPortTableTid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 4)
)
_AcdPortConfigTableLastChangeTid_Type = Unsigned32
_AcdPortConfigTableLastChangeTid_Object = MibScalar
acdPortConfigTableLastChangeTid = _AcdPortConfigTableLastChangeTid_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 1, 4, 1),
    _AcdPortConfigTableLastChangeTid_Type()
)
acdPortConfigTableLastChangeTid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdPortConfigTableLastChangeTid.setStatus("current")
_AcdPortConformance_ObjectIdentity = ObjectIdentity
acdPortConformance = _AcdPortConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 2)
)
_AcdPortCompliances_ObjectIdentity = ObjectIdentity
acdPortCompliances = _AcdPortCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 2, 1)
)
_AcdPortGroups_ObjectIdentity = ObjectIdentity
acdPortGroups = _AcdPortGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 2, 2)
)

# Managed Objects groups

acdPortConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 2, 2, 1)
)
acdPortConfigGroup.setObjects(
      *(("ACD-PORT-MIB", "acdPortConfigName"),
        ("ACD-PORT-MIB", "acdPortConfigAlias"),
        ("ACD-PORT-MIB", "acdPortConfigMacAddress"),
        ("ACD-PORT-MIB", "acdPortConfigConnectorId"),
        ("ACD-PORT-MIB", "acdPortConfigState"),
        ("ACD-PORT-MIB", "acdPortConfigMtu"),
        ("ACD-PORT-MIB", "acdPortConfigAutoNegoState"),
        ("ACD-PORT-MIB", "acdPortConfigSpeed"),
        ("ACD-PORT-MIB", "acdPortConfigDuplex"),
        ("ACD-PORT-MIB", "acdPortConfigMdi"),
        ("ACD-PORT-MIB", "acdPortConfigPauseMode"),
        ("ACD-PORT-MIB", "acdPortConfigAdvertisement"))
)
if mibBuilder.loadTexts:
    acdPortConfigGroup.setStatus("current")

acdPortStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 2, 2, 2)
)
acdPortStatusGroup.setObjects(
      *(("ACD-PORT-MIB", "acdPortStatusSpeed"),
        ("ACD-PORT-MIB", "acdPortStatusDuplex"),
        ("ACD-PORT-MIB", "acdPortStatusMdi"),
        ("ACD-PORT-MIB", "acdPortStatusTxPause"),
        ("ACD-PORT-MIB", "acdPortStatusRxPause"),
        ("ACD-PORT-MIB", "acdPortStatusLinkPartnerAbility"),
        ("ACD-PORT-MIB", "acdPortStatusLinkStatus"),
        ("ACD-PORT-MIB", "acdPortStatusMedia"),
        ("ACD-PORT-MIB", "acdPortStatusIsMonitor"),
        ("ACD-PORT-MIB", "acdPortStatusIsManagement"),
        ("ACD-PORT-MIB", "acdPortStatusIsSFP"),
        ("ACD-PORT-MIB", "acdPortStatusIsFiber"))
)
if mibBuilder.loadTexts:
    acdPortStatusGroup.setStatus("current")

acdPortTxStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 2, 2, 3)
)
acdPortTxStatsGroup.setObjects(
      *(("ACD-PORT-MIB", "acdPortTxStatsSupportBits"),
        ("ACD-PORT-MIB", "acdPortTxStatsBytesGood"),
        ("ACD-PORT-MIB", "acdPortTxStatsBytesTotal"),
        ("ACD-PORT-MIB", "acdPortTxStatsUnicastPkts"),
        ("ACD-PORT-MIB", "acdPortTxStatsMulticastPkts"),
        ("ACD-PORT-MIB", "acdPortTxStatsBroadcastPkts"),
        ("ACD-PORT-MIB", "acdPortTxStatsPauseFrames"),
        ("ACD-PORT-MIB", "acdPortTxStatsTaggedFrames"),
        ("ACD-PORT-MIB", "acdPortTxStatsCRCErrors"),
        ("ACD-PORT-MIB", "acdPortTxStatsDeferred"),
        ("ACD-PORT-MIB", "acdPortTxStatsExcessiveDeferrals"),
        ("ACD-PORT-MIB", "acdPortTxStatsSingleCollisions"),
        ("ACD-PORT-MIB", "acdPortTxStatsMultipleCollisions"),
        ("ACD-PORT-MIB", "acdPortTxStatsExcessiveCollisions"),
        ("ACD-PORT-MIB", "acdPortTxStatsLateCollisions"),
        ("ACD-PORT-MIB", "acdPortTxStatsNormalCollisions"),
        ("ACD-PORT-MIB", "acdPortTxStatsFifoErrors"),
        ("ACD-PORT-MIB", "acdPortTxStatsPkts64"),
        ("ACD-PORT-MIB", "acdPortTxStatsPkts65to127"),
        ("ACD-PORT-MIB", "acdPortTxStatsPkts128to255"),
        ("ACD-PORT-MIB", "acdPortTxStatsPkts256to511"),
        ("ACD-PORT-MIB", "acdPortTxStatsPkts512to1023"),
        ("ACD-PORT-MIB", "acdPortTxStatsPkts1024to1518"),
        ("ACD-PORT-MIB", "acdPortTxStatsPkts1519to2047"),
        ("ACD-PORT-MIB", "acdPortTxStatsPkts2048to4095"),
        ("ACD-PORT-MIB", "acdPortTxStatsPkts4096to8191"),
        ("ACD-PORT-MIB", "acdPortTxStatsPkts8192andMore"),
        ("ACD-PORT-MIB", "acdPortTxStatsPktsLarge"))
)
if mibBuilder.loadTexts:
    acdPortTxStatsGroup.setStatus("current")

acdPortRxStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 2, 2, 4)
)
acdPortRxStatsGroup.setObjects(
      *(("ACD-PORT-MIB", "acdPortRxStatsSupportBits"),
        ("ACD-PORT-MIB", "acdPortRxStatsBytesGood"),
        ("ACD-PORT-MIB", "acdPortRxStatsBytesTotal"),
        ("ACD-PORT-MIB", "acdPortRxStatsShortOk"),
        ("ACD-PORT-MIB", "acdPortRxStatsShortBad"),
        ("ACD-PORT-MIB", "acdPortRxStatsLongOk"),
        ("ACD-PORT-MIB", "acdPortRxStatsLongBad"),
        ("ACD-PORT-MIB", "acdPortRxStatsUnicastPkts"),
        ("ACD-PORT-MIB", "acdPortRxStatsMulticastPkts"),
        ("ACD-PORT-MIB", "acdPortRxStatsBroadcastPkts"),
        ("ACD-PORT-MIB", "acdPortRxStatsPauseFrames"),
        ("ACD-PORT-MIB", "acdPortRxStatsTaggedFrames"),
        ("ACD-PORT-MIB", "acdPortRxStatsCRCErrors"),
        ("ACD-PORT-MIB", "acdPortRxStatsAlignErrors"),
        ("ACD-PORT-MIB", "acdPortRxStatsRuntFrames"),
        ("ACD-PORT-MIB", "acdPortRxStatsLengthErrors"),
        ("ACD-PORT-MIB", "acdPortRxStatsFalseCRS"),
        ("ACD-PORT-MIB", "acdPortRxStatsPhyErrors"),
        ("ACD-PORT-MIB", "acdPortRxStatsFifoErrors"),
        ("ACD-PORT-MIB", "acdPortRxStatsIgnored"),
        ("ACD-PORT-MIB", "acdPortRxStatsBadOpcode"),
        ("ACD-PORT-MIB", "acdPortRxStatsPkts64"),
        ("ACD-PORT-MIB", "acdPortRxStatsPkts65to127"),
        ("ACD-PORT-MIB", "acdPortRxStatsPkts128to255"),
        ("ACD-PORT-MIB", "acdPortRxStatsPkts256to511"),
        ("ACD-PORT-MIB", "acdPortRxStatsPkts512to1023"),
        ("ACD-PORT-MIB", "acdPortRxStatsPkts1024to1518"),
        ("ACD-PORT-MIB", "acdPortRxStatsPkts1519to2047"),
        ("ACD-PORT-MIB", "acdPortRxStatsPkts2048to4095"),
        ("ACD-PORT-MIB", "acdPortRxStatsPkts4096to8191"),
        ("ACD-PORT-MIB", "acdPortRxStatsPkts8192andMore"),
        ("ACD-PORT-MIB", "acdPortRxStatsPktsLarge"))
)
if mibBuilder.loadTexts:
    acdPortRxStatsGroup.setStatus("current")

acdPortTidGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 2, 2, 5)
)
acdPortTidGroup.setObjects(
    ("ACD-PORT-MIB", "acdPortConfigTableLastChangeTid")
)
if mibBuilder.loadTexts:
    acdPortTidGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

acdPortCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 22420, 2, 9, 2, 1, 1)
)
if mibBuilder.loadTexts:
    acdPortCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACD-PORT-MIB",
    **{"acdPort": acdPort,
       "acdPortMIBObjects": acdPortMIBObjects,
       "acdPortConfig": acdPortConfig,
       "acdPortConfigTable": acdPortConfigTable,
       "acdPortConfigEntry": acdPortConfigEntry,
       "acdPortConfigIndex": acdPortConfigIndex,
       "acdPortConfigName": acdPortConfigName,
       "acdPortConfigAlias": acdPortConfigAlias,
       "acdPortConfigMacAddress": acdPortConfigMacAddress,
       "acdPortConfigConnectorId": acdPortConfigConnectorId,
       "acdPortConfigState": acdPortConfigState,
       "acdPortConfigMtu": acdPortConfigMtu,
       "acdPortConfigAutoNegoState": acdPortConfigAutoNegoState,
       "acdPortConfigSpeed": acdPortConfigSpeed,
       "acdPortConfigDuplex": acdPortConfigDuplex,
       "acdPortConfigMdi": acdPortConfigMdi,
       "acdPortConfigPauseMode": acdPortConfigPauseMode,
       "acdPortConfigAdvertisement": acdPortConfigAdvertisement,
       "acdPortStatus": acdPortStatus,
       "acdPortStatusTable": acdPortStatusTable,
       "acdPortStatusEntry": acdPortStatusEntry,
       "acdPortStatusIndex": acdPortStatusIndex,
       "acdPortStatusSpeed": acdPortStatusSpeed,
       "acdPortStatusDuplex": acdPortStatusDuplex,
       "acdPortStatusMdi": acdPortStatusMdi,
       "acdPortStatusTxPause": acdPortStatusTxPause,
       "acdPortStatusRxPause": acdPortStatusRxPause,
       "acdPortStatusLinkPartnerAbility": acdPortStatusLinkPartnerAbility,
       "acdPortStatusLinkStatus": acdPortStatusLinkStatus,
       "acdPortStatusMedia": acdPortStatusMedia,
       "acdPortStatusIsMonitor": acdPortStatusIsMonitor,
       "acdPortStatusIsManagement": acdPortStatusIsManagement,
       "acdPortStatusIsSFP": acdPortStatusIsSFP,
       "acdPortStatusIsFiber": acdPortStatusIsFiber,
       "acdPortStats": acdPortStats,
       "acdPortTxStatsTable": acdPortTxStatsTable,
       "acdPortTxStatsEntry": acdPortTxStatsEntry,
       "acdPortTxStatsIndex": acdPortTxStatsIndex,
       "acdPortTxStatsSupportBits": acdPortTxStatsSupportBits,
       "acdPortTxStatsBytesGood": acdPortTxStatsBytesGood,
       "acdPortTxStatsBytesTotal": acdPortTxStatsBytesTotal,
       "acdPortTxStatsUnicastPkts": acdPortTxStatsUnicastPkts,
       "acdPortTxStatsMulticastPkts": acdPortTxStatsMulticastPkts,
       "acdPortTxStatsBroadcastPkts": acdPortTxStatsBroadcastPkts,
       "acdPortTxStatsPauseFrames": acdPortTxStatsPauseFrames,
       "acdPortTxStatsTaggedFrames": acdPortTxStatsTaggedFrames,
       "acdPortTxStatsCRCErrors": acdPortTxStatsCRCErrors,
       "acdPortTxStatsDeferred": acdPortTxStatsDeferred,
       "acdPortTxStatsExcessiveDeferrals": acdPortTxStatsExcessiveDeferrals,
       "acdPortTxStatsSingleCollisions": acdPortTxStatsSingleCollisions,
       "acdPortTxStatsMultipleCollisions": acdPortTxStatsMultipleCollisions,
       "acdPortTxStatsExcessiveCollisions": acdPortTxStatsExcessiveCollisions,
       "acdPortTxStatsLateCollisions": acdPortTxStatsLateCollisions,
       "acdPortTxStatsNormalCollisions": acdPortTxStatsNormalCollisions,
       "acdPortTxStatsFifoErrors": acdPortTxStatsFifoErrors,
       "acdPortTxStatsPkts64": acdPortTxStatsPkts64,
       "acdPortTxStatsPkts65to127": acdPortTxStatsPkts65to127,
       "acdPortTxStatsPkts128to255": acdPortTxStatsPkts128to255,
       "acdPortTxStatsPkts256to511": acdPortTxStatsPkts256to511,
       "acdPortTxStatsPkts512to1023": acdPortTxStatsPkts512to1023,
       "acdPortTxStatsPkts1024to1518": acdPortTxStatsPkts1024to1518,
       "acdPortTxStatsPkts1519to2047": acdPortTxStatsPkts1519to2047,
       "acdPortTxStatsPkts2048to4095": acdPortTxStatsPkts2048to4095,
       "acdPortTxStatsPkts4096to8191": acdPortTxStatsPkts4096to8191,
       "acdPortTxStatsPkts8192andMore": acdPortTxStatsPkts8192andMore,
       "acdPortTxStatsPktsLarge": acdPortTxStatsPktsLarge,
       "acdPortRxStatsTable": acdPortRxStatsTable,
       "acdPortRxStatsEntry": acdPortRxStatsEntry,
       "acdPortRxStatsIndex": acdPortRxStatsIndex,
       "acdPortRxStatsSupportBits": acdPortRxStatsSupportBits,
       "acdPortRxStatsBytesGood": acdPortRxStatsBytesGood,
       "acdPortRxStatsBytesTotal": acdPortRxStatsBytesTotal,
       "acdPortRxStatsShortOk": acdPortRxStatsShortOk,
       "acdPortRxStatsShortBad": acdPortRxStatsShortBad,
       "acdPortRxStatsLongOk": acdPortRxStatsLongOk,
       "acdPortRxStatsLongBad": acdPortRxStatsLongBad,
       "acdPortRxStatsUnicastPkts": acdPortRxStatsUnicastPkts,
       "acdPortRxStatsMulticastPkts": acdPortRxStatsMulticastPkts,
       "acdPortRxStatsBroadcastPkts": acdPortRxStatsBroadcastPkts,
       "acdPortRxStatsPauseFrames": acdPortRxStatsPauseFrames,
       "acdPortRxStatsTaggedFrames": acdPortRxStatsTaggedFrames,
       "acdPortRxStatsCRCErrors": acdPortRxStatsCRCErrors,
       "acdPortRxStatsAlignErrors": acdPortRxStatsAlignErrors,
       "acdPortRxStatsRuntFrames": acdPortRxStatsRuntFrames,
       "acdPortRxStatsLengthErrors": acdPortRxStatsLengthErrors,
       "acdPortRxStatsFalseCRS": acdPortRxStatsFalseCRS,
       "acdPortRxStatsPhyErrors": acdPortRxStatsPhyErrors,
       "acdPortRxStatsFifoErrors": acdPortRxStatsFifoErrors,
       "acdPortRxStatsIgnored": acdPortRxStatsIgnored,
       "acdPortRxStatsBadOpcode": acdPortRxStatsBadOpcode,
       "acdPortRxStatsPkts64": acdPortRxStatsPkts64,
       "acdPortRxStatsPkts65to127": acdPortRxStatsPkts65to127,
       "acdPortRxStatsPkts128to255": acdPortRxStatsPkts128to255,
       "acdPortRxStatsPkts256to511": acdPortRxStatsPkts256to511,
       "acdPortRxStatsPkts512to1023": acdPortRxStatsPkts512to1023,
       "acdPortRxStatsPkts1024to1518": acdPortRxStatsPkts1024to1518,
       "acdPortRxStatsPkts1519to2047": acdPortRxStatsPkts1519to2047,
       "acdPortRxStatsPkts2048to4095": acdPortRxStatsPkts2048to4095,
       "acdPortRxStatsPkts4096to8191": acdPortRxStatsPkts4096to8191,
       "acdPortRxStatsPkts8192andMore": acdPortRxStatsPkts8192andMore,
       "acdPortRxStatsPktsLarge": acdPortRxStatsPktsLarge,
       "acdPortTableTid": acdPortTableTid,
       "acdPortConfigTableLastChangeTid": acdPortConfigTableLastChangeTid,
       "acdPortConformance": acdPortConformance,
       "acdPortCompliances": acdPortCompliances,
       "acdPortCompliance": acdPortCompliance,
       "acdPortGroups": acdPortGroups,
       "acdPortConfigGroup": acdPortConfigGroup,
       "acdPortStatusGroup": acdPortStatusGroup,
       "acdPortTxStatsGroup": acdPortTxStatsGroup,
       "acdPortRxStatsGroup": acdPortRxStatsGroup,
       "acdPortTidGroup": acdPortTidGroup}
)
