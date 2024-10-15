# SNMP MIB module (LIGO-WIRELESS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LIGO-WIRELESS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:18:14 2024
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

(ifIndex,
 ifPhysAddress) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex",
    "ifPhysAddress")

(ligoMgmt,) = mibBuilder.importSymbols(
    "LIGOWAVE-MIB",
    "ligoMgmt")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysLocation,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysLocation")

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

ligoWirelessMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 32750, 3, 10)
)
ligoWirelessMIB.setRevisions(
        ("2011-11-11 11:11",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LigoWirelessMIBObjects_ObjectIdentity = ObjectIdentity
ligoWirelessMIBObjects = _LigoWirelessMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32750, 3, 10, 1)
)
_LigoWiNotifs_ObjectIdentity = ObjectIdentity
ligoWiNotifs = _LigoWiNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32750, 3, 10, 1, 0)
)
_LigoWiInfo_ObjectIdentity = ObjectIdentity
ligoWiInfo = _LigoWiInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32750, 3, 10, 1, 1)
)
_LigoWiConf_ObjectIdentity = ObjectIdentity
ligoWiConf = _LigoWiConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32750, 3, 10, 1, 2)
)
_LigoWiIfConfTable_Object = MibTable
ligoWiIfConfTable = _LigoWiIfConfTable_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 10, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ligoWiIfConfTable.setStatus("current")
_LigoWiIfConfEntry_Object = MibTableRow
ligoWiIfConfEntry = _LigoWiIfConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 10, 1, 2, 1, 1)
)
ligoWiIfConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ligoWiIfConfEntry.setStatus("current")
_LigoWiIfMacAddress_Type = MacAddress
_LigoWiIfMacAddress_Object = MibTableColumn
ligoWiIfMacAddress = _LigoWiIfMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 10, 1, 2, 1, 1, 1),
    _LigoWiIfMacAddress_Type()
)
ligoWiIfMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoWiIfMacAddress.setStatus("current")


class _LigoWiIfProtocol_Type(OctetString):
    """Custom type ligoWiIfProtocol based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_LigoWiIfProtocol_Type.__name__ = "OctetString"
_LigoWiIfProtocol_Object = MibTableColumn
ligoWiIfProtocol = _LigoWiIfProtocol_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 10, 1, 2, 1, 1, 2),
    _LigoWiIfProtocol_Type()
)
ligoWiIfProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoWiIfProtocol.setStatus("current")


class _LigoWiIfMode_Type(Integer32):
    """Custom type ligoWiIfMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("adhoc", 1),
          ("auto", 0),
          ("managed", 2),
          ("master", 3),
          ("monitor", 6),
          ("repeater", 4),
          ("secondary", 5))
    )


_LigoWiIfMode_Type.__name__ = "Integer32"
_LigoWiIfMode_Object = MibTableColumn
ligoWiIfMode = _LigoWiIfMode_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 10, 1, 2, 1, 1, 3),
    _LigoWiIfMode_Type()
)
ligoWiIfMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoWiIfMode.setStatus("current")


class _LigoWiIfESSID_Type(OctetString):
    """Custom type ligoWiIfESSID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LigoWiIfESSID_Type.__name__ = "OctetString"
_LigoWiIfESSID_Object = MibTableColumn
ligoWiIfESSID = _LigoWiIfESSID_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 10, 1, 2, 1, 1, 4),
    _LigoWiIfESSID_Type()
)
ligoWiIfESSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoWiIfESSID.setStatus("current")


class _LigoWiIfCountryCode_Type(OctetString):
    """Custom type ligoWiIfCountryCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 3),
    )


_LigoWiIfCountryCode_Type.__name__ = "OctetString"
_LigoWiIfCountryCode_Object = MibTableColumn
ligoWiIfCountryCode = _LigoWiIfCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 10, 1, 2, 1, 1, 5),
    _LigoWiIfCountryCode_Type()
)
ligoWiIfCountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoWiIfCountryCode.setStatus("current")
_LigoWiIfFrequency_Type = Integer32
_LigoWiIfFrequency_Object = MibTableColumn
ligoWiIfFrequency = _LigoWiIfFrequency_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 10, 1, 2, 1, 1, 6),
    _LigoWiIfFrequency_Type()
)
ligoWiIfFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoWiIfFrequency.setStatus("current")
if mibBuilder.loadTexts:
    ligoWiIfFrequency.setUnits("MHz")
_LigoWiIfChannel_Type = Integer32
_LigoWiIfChannel_Object = MibTableColumn
ligoWiIfChannel = _LigoWiIfChannel_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 10, 1, 2, 1, 1, 7),
    _LigoWiIfChannel_Type()
)
ligoWiIfChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoWiIfChannel.setStatus("current")
_LigoWiIfChannelBandwidth_Type = Integer32
_LigoWiIfChannelBandwidth_Object = MibTableColumn
ligoWiIfChannelBandwidth = _LigoWiIfChannelBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 10, 1, 2, 1, 1, 8),
    _LigoWiIfChannelBandwidth_Type()
)
ligoWiIfChannelBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoWiIfChannelBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    ligoWiIfChannelBandwidth.setUnits("MHz")


class _LigoWiIfEncryption_Type(Integer32):
    """Custom type ligoWiIfEncryption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("enterpriseWpa", 5),
          ("enterpriseWpa2", 7),
          ("enterpriseWpaOrWpa2", 9),
          ("open", 1),
          ("personalWpa", 6),
          ("personalWpa2", 8),
          ("personalWpaOrWpa2", 10),
          ("unknown", 0),
          ("wep", 4),
          ("wep128bit", 3),
          ("wep64bit", 2))
    )


_LigoWiIfEncryption_Type.__name__ = "Integer32"
_LigoWiIfEncryption_Object = MibTableColumn
ligoWiIfEncryption = _LigoWiIfEncryption_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 10, 1, 2, 1, 1, 9),
    _LigoWiIfEncryption_Type()
)
ligoWiIfEncryption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoWiIfEncryption.setStatus("current")
_LigoWiIfTxPower_Type = Gauge32
_LigoWiIfTxPower_Object = MibTableColumn
ligoWiIfTxPower = _LigoWiIfTxPower_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 10, 1, 2, 1, 1, 10),
    _LigoWiIfTxPower_Type()
)
ligoWiIfTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoWiIfTxPower.setStatus("current")
if mibBuilder.loadTexts:
    ligoWiIfTxPower.setUnits("dBm")
_LigoWiIfBitRate_Type = Gauge32
_LigoWiIfBitRate_Object = MibTableColumn
ligoWiIfBitRate = _LigoWiIfBitRate_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 10, 1, 2, 1, 1, 11),
    _LigoWiIfBitRate_Type()
)
ligoWiIfBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoWiIfBitRate.setStatus("current")
if mibBuilder.loadTexts:
    ligoWiIfBitRate.setUnits("kbit/s")
_LigoWiIfLinkQuality_Type = Gauge32
_LigoWiIfLinkQuality_Object = MibTableColumn
ligoWiIfLinkQuality = _LigoWiIfLinkQuality_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 10, 1, 2, 1, 1, 12),
    _LigoWiIfLinkQuality_Type()
)
ligoWiIfLinkQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoWiIfLinkQuality.setStatus("current")
_LigoWiIfMaxLinkQuality_Type = Gauge32
_LigoWiIfMaxLinkQuality_Object = MibTableColumn
ligoWiIfMaxLinkQuality = _LigoWiIfMaxLinkQuality_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 10, 1, 2, 1, 1, 13),
    _LigoWiIfMaxLinkQuality_Type()
)
ligoWiIfMaxLinkQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoWiIfMaxLinkQuality.setStatus("current")
_LigoWiIfSignalLevel_Type = Integer32
_LigoWiIfSignalLevel_Object = MibTableColumn
ligoWiIfSignalLevel = _LigoWiIfSignalLevel_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 10, 1, 2, 1, 1, 14),
    _LigoWiIfSignalLevel_Type()
)
ligoWiIfSignalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoWiIfSignalLevel.setStatus("current")
if mibBuilder.loadTexts:
    ligoWiIfSignalLevel.setUnits("dBm")
_LigoWiIfNoiseLevel_Type = Integer32
_LigoWiIfNoiseLevel_Object = MibTableColumn
ligoWiIfNoiseLevel = _LigoWiIfNoiseLevel_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 10, 1, 2, 1, 1, 15),
    _LigoWiIfNoiseLevel_Type()
)
ligoWiIfNoiseLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoWiIfNoiseLevel.setStatus("current")
if mibBuilder.loadTexts:
    ligoWiIfNoiseLevel.setUnits("dBm")
_LigoWiIfAssocNodeCount_Type = Gauge32
_LigoWiIfAssocNodeCount_Object = MibTableColumn
ligoWiIfAssocNodeCount = _LigoWiIfAssocNodeCount_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 10, 1, 2, 1, 1, 16),
    _LigoWiIfAssocNodeCount_Type()
)
ligoWiIfAssocNodeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoWiIfAssocNodeCount.setStatus("current")
_LigoWiStats_ObjectIdentity = ObjectIdentity
ligoWiStats = _LigoWiStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32750, 3, 10, 1, 3)
)
_LigoWiIfStatsTable_Object = MibTable
ligoWiIfStatsTable = _LigoWiIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 10, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ligoWiIfStatsTable.setStatus("current")
_LigoWiIfStatsEntry_Object = MibTableRow
ligoWiIfStatsEntry = _LigoWiIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 10, 1, 3, 1, 1)
)
ligoWiIfStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ligoWiIfStatsEntry.setStatus("current")
_LigoWiIfRxTotal_Type = Counter32
_LigoWiIfRxTotal_Object = MibTableColumn
ligoWiIfRxTotal = _LigoWiIfRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 10, 1, 3, 1, 1, 1),
    _LigoWiIfRxTotal_Type()
)
ligoWiIfRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoWiIfRxTotal.setStatus("current")
_LigoWiIfRxErrors_Type = Counter32
_LigoWiIfRxErrors_Object = MibTableColumn
ligoWiIfRxErrors = _LigoWiIfRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 10, 1, 3, 1, 1, 2),
    _LigoWiIfRxErrors_Type()
)
ligoWiIfRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoWiIfRxErrors.setStatus("current")
_LigoWiIfTxTotal_Type = Counter32
_LigoWiIfTxTotal_Object = MibTableColumn
ligoWiIfTxTotal = _LigoWiIfTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 10, 1, 3, 1, 1, 3),
    _LigoWiIfTxTotal_Type()
)
ligoWiIfTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoWiIfTxTotal.setStatus("current")
_LigoWiIfTxRetries_Type = Counter32
_LigoWiIfTxRetries_Object = MibTableColumn
ligoWiIfTxRetries = _LigoWiIfTxRetries_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 10, 1, 3, 1, 1, 4),
    _LigoWiIfTxRetries_Type()
)
ligoWiIfTxRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoWiIfTxRetries.setStatus("current")
_LigoWiRemoteNodeStatsTable_Object = MibTable
ligoWiRemoteNodeStatsTable = _LigoWiRemoteNodeStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 10, 1, 3, 2)
)
if mibBuilder.loadTexts:
    ligoWiRemoteNodeStatsTable.setStatus("current")
_LigoWiRemoteNodeStatsEntry_Object = MibTableRow
ligoWiRemoteNodeStatsEntry = _LigoWiRemoteNodeStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 10, 1, 3, 2, 1)
)
ligoWiRemoteNodeStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "LIGO-WIRELESS-MIB", "ligoWiRmtNodeMacAddress"),
)
if mibBuilder.loadTexts:
    ligoWiRemoteNodeStatsEntry.setStatus("current")
_LigoWiRmtNodeMacAddress_Type = MacAddress
_LigoWiRmtNodeMacAddress_Object = MibTableColumn
ligoWiRmtNodeMacAddress = _LigoWiRmtNodeMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 10, 1, 3, 2, 1, 1),
    _LigoWiRmtNodeMacAddress_Type()
)
ligoWiRmtNodeMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoWiRmtNodeMacAddress.setStatus("current")
_LigoWiRmtNodeAssociated_Type = TruthValue
_LigoWiRmtNodeAssociated_Object = MibTableColumn
ligoWiRmtNodeAssociated = _LigoWiRmtNodeAssociated_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 10, 1, 3, 2, 1, 2),
    _LigoWiRmtNodeAssociated_Type()
)
ligoWiRmtNodeAssociated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoWiRmtNodeAssociated.setStatus("current")
_LigoWiRmtNodeTxBytes_Type = Counter32
_LigoWiRmtNodeTxBytes_Object = MibTableColumn
ligoWiRmtNodeTxBytes = _LigoWiRmtNodeTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 10, 1, 3, 2, 1, 3),
    _LigoWiRmtNodeTxBytes_Type()
)
ligoWiRmtNodeTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoWiRmtNodeTxBytes.setStatus("current")
if mibBuilder.loadTexts:
    ligoWiRmtNodeTxBytes.setUnits("bytes")
_LigoWiRmtNodeRxBytes_Type = Counter32
_LigoWiRmtNodeRxBytes_Object = MibTableColumn
ligoWiRmtNodeRxBytes = _LigoWiRmtNodeRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 10, 1, 3, 2, 1, 4),
    _LigoWiRmtNodeRxBytes_Type()
)
ligoWiRmtNodeRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoWiRmtNodeRxBytes.setStatus("current")
if mibBuilder.loadTexts:
    ligoWiRmtNodeRxBytes.setUnits("bytes")
_LigoWiRmtNodeSignalLevel_Type = Integer32
_LigoWiRmtNodeSignalLevel_Object = MibTableColumn
ligoWiRmtNodeSignalLevel = _LigoWiRmtNodeSignalLevel_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 10, 1, 3, 2, 1, 5),
    _LigoWiRmtNodeSignalLevel_Type()
)
ligoWiRmtNodeSignalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoWiRmtNodeSignalLevel.setStatus("current")
if mibBuilder.loadTexts:
    ligoWiRmtNodeSignalLevel.setUnits("dBm")
_LigoWiRmtNodeNoiseLevel_Type = Integer32
_LigoWiRmtNodeNoiseLevel_Object = MibTableColumn
ligoWiRmtNodeNoiseLevel = _LigoWiRmtNodeNoiseLevel_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 10, 1, 3, 2, 1, 6),
    _LigoWiRmtNodeNoiseLevel_Type()
)
ligoWiRmtNodeNoiseLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoWiRmtNodeNoiseLevel.setStatus("current")
if mibBuilder.loadTexts:
    ligoWiRmtNodeNoiseLevel.setUnits("dBm")

# Managed Objects groups


# Notification objects

ligoWiFrequencyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 32750, 3, 10, 1, 0, 1)
)
ligoWiFrequencyChange.setObjects(
      *(("SNMPv2-MIB", "sysLocation"),
        ("IF-MIB", "ifIndex"),
        ("LIGO-WIRELESS-MIB", "ligoWiIfFrequency"))
)
if mibBuilder.loadTexts:
    ligoWiFrequencyChange.setStatus(
        "current"
    )

ligoWiNoiseThresholdReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 32750, 3, 10, 1, 0, 2)
)
ligoWiNoiseThresholdReached.setObjects(
      *(("SNMPv2-MIB", "sysLocation"),
        ("IF-MIB", "ifIndex"),
        ("LIGO-WIRELESS-MIB", "ligoWiIfNoiseLevel"))
)
if mibBuilder.loadTexts:
    ligoWiNoiseThresholdReached.setStatus(
        "current"
    )

ligoWiRemoteNodeConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 32750, 3, 10, 1, 0, 3)
)
ligoWiRemoteNodeConnected.setObjects(
      *(("SNMPv2-MIB", "sysLocation"),
        ("IF-MIB", "ifPhysAddress"),
        ("IF-MIB", "ifIndex"),
        ("LIGO-WIRELESS-MIB", "ligoWiRmtNodeMacAddress"))
)
if mibBuilder.loadTexts:
    ligoWiRemoteNodeConnected.setStatus(
        "current"
    )

ligoWiRemoteNodeDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 32750, 3, 10, 1, 0, 4)
)
ligoWiRemoteNodeDisconnected.setObjects(
      *(("SNMPv2-MIB", "sysLocation"),
        ("IF-MIB", "ifPhysAddress"),
        ("IF-MIB", "ifIndex"),
        ("LIGO-WIRELESS-MIB", "ligoWiRmtNodeMacAddress"))
)
if mibBuilder.loadTexts:
    ligoWiRemoteNodeDisconnected.setStatus(
        "current"
    )

ligoWiLinkQualThresholdReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 32750, 3, 10, 1, 0, 5)
)
ligoWiLinkQualThresholdReached.setObjects(
      *(("SNMPv2-MIB", "sysLocation"),
        ("IF-MIB", "ifIndex"),
        ("LIGO-WIRELESS-MIB", "ligoWiIfLinkQuality"))
)
if mibBuilder.loadTexts:
    ligoWiLinkQualThresholdReached.setStatus(
        "current"
    )

ligoWiRxErrorsThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 32750, 3, 10, 1, 0, 6)
)
ligoWiRxErrorsThreshold.setObjects(
      *(("SNMPv2-MIB", "sysLocation"),
        ("IF-MIB", "ifIndex"),
        ("LIGO-WIRELESS-MIB", "ligoWiIfMacAddress"),
        ("LIGO-WIRELESS-MIB", "ligoWiIfRxErrors"))
)
if mibBuilder.loadTexts:
    ligoWiRxErrorsThreshold.setStatus(
        "current"
    )

ligoWiTxRetriesThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 32750, 3, 10, 1, 0, 7)
)
ligoWiTxRetriesThreshold.setObjects(
      *(("SNMPv2-MIB", "sysLocation"),
        ("IF-MIB", "ifIndex"),
        ("LIGO-WIRELESS-MIB", "ligoWiIfMacAddress"),
        ("LIGO-WIRELESS-MIB", "ligoWiIfTxRetries"))
)
if mibBuilder.loadTexts:
    ligoWiTxRetriesThreshold.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LIGO-WIRELESS-MIB",
    **{"ligoWirelessMIB": ligoWirelessMIB,
       "ligoWirelessMIBObjects": ligoWirelessMIBObjects,
       "ligoWiNotifs": ligoWiNotifs,
       "ligoWiFrequencyChange": ligoWiFrequencyChange,
       "ligoWiNoiseThresholdReached": ligoWiNoiseThresholdReached,
       "ligoWiRemoteNodeConnected": ligoWiRemoteNodeConnected,
       "ligoWiRemoteNodeDisconnected": ligoWiRemoteNodeDisconnected,
       "ligoWiLinkQualThresholdReached": ligoWiLinkQualThresholdReached,
       "ligoWiRxErrorsThreshold": ligoWiRxErrorsThreshold,
       "ligoWiTxRetriesThreshold": ligoWiTxRetriesThreshold,
       "ligoWiInfo": ligoWiInfo,
       "ligoWiConf": ligoWiConf,
       "ligoWiIfConfTable": ligoWiIfConfTable,
       "ligoWiIfConfEntry": ligoWiIfConfEntry,
       "ligoWiIfMacAddress": ligoWiIfMacAddress,
       "ligoWiIfProtocol": ligoWiIfProtocol,
       "ligoWiIfMode": ligoWiIfMode,
       "ligoWiIfESSID": ligoWiIfESSID,
       "ligoWiIfCountryCode": ligoWiIfCountryCode,
       "ligoWiIfFrequency": ligoWiIfFrequency,
       "ligoWiIfChannel": ligoWiIfChannel,
       "ligoWiIfChannelBandwidth": ligoWiIfChannelBandwidth,
       "ligoWiIfEncryption": ligoWiIfEncryption,
       "ligoWiIfTxPower": ligoWiIfTxPower,
       "ligoWiIfBitRate": ligoWiIfBitRate,
       "ligoWiIfLinkQuality": ligoWiIfLinkQuality,
       "ligoWiIfMaxLinkQuality": ligoWiIfMaxLinkQuality,
       "ligoWiIfSignalLevel": ligoWiIfSignalLevel,
       "ligoWiIfNoiseLevel": ligoWiIfNoiseLevel,
       "ligoWiIfAssocNodeCount": ligoWiIfAssocNodeCount,
       "ligoWiStats": ligoWiStats,
       "ligoWiIfStatsTable": ligoWiIfStatsTable,
       "ligoWiIfStatsEntry": ligoWiIfStatsEntry,
       "ligoWiIfRxTotal": ligoWiIfRxTotal,
       "ligoWiIfRxErrors": ligoWiIfRxErrors,
       "ligoWiIfTxTotal": ligoWiIfTxTotal,
       "ligoWiIfTxRetries": ligoWiIfTxRetries,
       "ligoWiRemoteNodeStatsTable": ligoWiRemoteNodeStatsTable,
       "ligoWiRemoteNodeStatsEntry": ligoWiRemoteNodeStatsEntry,
       "ligoWiRmtNodeMacAddress": ligoWiRmtNodeMacAddress,
       "ligoWiRmtNodeAssociated": ligoWiRmtNodeAssociated,
       "ligoWiRmtNodeTxBytes": ligoWiRmtNodeTxBytes,
       "ligoWiRmtNodeRxBytes": ligoWiRmtNodeRxBytes,
       "ligoWiRmtNodeSignalLevel": ligoWiRmtNodeSignalLevel,
       "ligoWiRmtNodeNoiseLevel": ligoWiRmtNodeNoiseLevel}
)
