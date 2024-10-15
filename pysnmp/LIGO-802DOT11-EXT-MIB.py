# SNMP MIB module (LIGO-802DOT11-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LIGO-802DOT11-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:18:09 2024
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

(InterfaceIndex,
 ifIndex,
 ifPhysAddress) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
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

ligo802dot11ExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 32750, 3, 5)
)
ligo802dot11ExtMIB.setRevisions(
        ("2010-03-31 00:00",
         "2009-05-15 00:00",
         "2008-12-12 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ligo802dot11ExtMIBObjects_ObjectIdentity = ObjectIdentity
ligo802dot11ExtMIBObjects = _Ligo802dot11ExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32750, 3, 5, 1)
)
_LigoDot11Notifs_ObjectIdentity = ObjectIdentity
ligoDot11Notifs = _LigoDot11Notifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 0)
)
_LigoDot11Info_ObjectIdentity = ObjectIdentity
ligoDot11Info = _LigoDot11Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 1)
)
_LigoDot11Conf_ObjectIdentity = ObjectIdentity
ligoDot11Conf = _LigoDot11Conf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 2)
)
_LigoDot11IfConfTable_Object = MibTable
ligoDot11IfConfTable = _LigoDot11IfConfTable_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ligoDot11IfConfTable.setStatus("current")
_LigoDot11IfConfEntry_Object = MibTableRow
ligoDot11IfConfEntry = _LigoDot11IfConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 2, 1, 1)
)
ligoDot11IfConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ligoDot11IfConfEntry.setStatus("current")
_LigoDot11IfParentIndex_Type = InterfaceIndex
_LigoDot11IfParentIndex_Object = MibTableColumn
ligoDot11IfParentIndex = _LigoDot11IfParentIndex_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 2, 1, 1, 1),
    _LigoDot11IfParentIndex_Type()
)
ligoDot11IfParentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoDot11IfParentIndex.setStatus("current")


class _LigoDot11IfProtocol_Type(OctetString):
    """Custom type ligoDot11IfProtocol based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_LigoDot11IfProtocol_Type.__name__ = "OctetString"
_LigoDot11IfProtocol_Object = MibTableColumn
ligoDot11IfProtocol = _LigoDot11IfProtocol_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 2, 1, 1, 2),
    _LigoDot11IfProtocol_Type()
)
ligoDot11IfProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoDot11IfProtocol.setStatus("current")


class _LigoDot11IfMode_Type(Integer32):
    """Custom type ligoDot11IfMode based on Integer32"""
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


_LigoDot11IfMode_Type.__name__ = "Integer32"
_LigoDot11IfMode_Object = MibTableColumn
ligoDot11IfMode = _LigoDot11IfMode_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 2, 1, 1, 3),
    _LigoDot11IfMode_Type()
)
ligoDot11IfMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoDot11IfMode.setStatus("current")


class _LigoDot11IfESSID_Type(OctetString):
    """Custom type ligoDot11IfESSID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LigoDot11IfESSID_Type.__name__ = "OctetString"
_LigoDot11IfESSID_Object = MibTableColumn
ligoDot11IfESSID = _LigoDot11IfESSID_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 2, 1, 1, 4),
    _LigoDot11IfESSID_Type()
)
ligoDot11IfESSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoDot11IfESSID.setStatus("current")
_LigoDot11IfAccessPoint_Type = MacAddress
_LigoDot11IfAccessPoint_Object = MibTableColumn
ligoDot11IfAccessPoint = _LigoDot11IfAccessPoint_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 2, 1, 1, 5),
    _LigoDot11IfAccessPoint_Type()
)
ligoDot11IfAccessPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoDot11IfAccessPoint.setStatus("current")
_LigoDot11IfCountryCode_Type = Integer32
_LigoDot11IfCountryCode_Object = MibTableColumn
ligoDot11IfCountryCode = _LigoDot11IfCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 2, 1, 1, 6),
    _LigoDot11IfCountryCode_Type()
)
ligoDot11IfCountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoDot11IfCountryCode.setStatus("current")
_LigoDot11IfFrequency_Type = Integer32
_LigoDot11IfFrequency_Object = MibTableColumn
ligoDot11IfFrequency = _LigoDot11IfFrequency_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 2, 1, 1, 7),
    _LigoDot11IfFrequency_Type()
)
ligoDot11IfFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoDot11IfFrequency.setStatus("current")
if mibBuilder.loadTexts:
    ligoDot11IfFrequency.setUnits("MHz")
_LigoDot11IfChannel_Type = Integer32
_LigoDot11IfChannel_Object = MibTableColumn
ligoDot11IfChannel = _LigoDot11IfChannel_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 2, 1, 1, 8),
    _LigoDot11IfChannel_Type()
)
ligoDot11IfChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoDot11IfChannel.setStatus("current")
_LigoDot11IfChannelBandwidth_Type = Integer32
_LigoDot11IfChannelBandwidth_Object = MibTableColumn
ligoDot11IfChannelBandwidth = _LigoDot11IfChannelBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 2, 1, 1, 9),
    _LigoDot11IfChannelBandwidth_Type()
)
ligoDot11IfChannelBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoDot11IfChannelBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    ligoDot11IfChannelBandwidth.setUnits("MHz")
_LigoDot11IfTxPower_Type = Gauge32
_LigoDot11IfTxPower_Object = MibTableColumn
ligoDot11IfTxPower = _LigoDot11IfTxPower_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 2, 1, 1, 10),
    _LigoDot11IfTxPower_Type()
)
ligoDot11IfTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoDot11IfTxPower.setStatus("current")
if mibBuilder.loadTexts:
    ligoDot11IfTxPower.setUnits("dBm")
_LigoDot11IfBitRate_Type = Gauge32
_LigoDot11IfBitRate_Object = MibTableColumn
ligoDot11IfBitRate = _LigoDot11IfBitRate_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 2, 1, 1, 11),
    _LigoDot11IfBitRate_Type()
)
ligoDot11IfBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoDot11IfBitRate.setStatus("current")
if mibBuilder.loadTexts:
    ligoDot11IfBitRate.setUnits("kbit/s")
_LigoDot11IfLinkQuality_Type = Gauge32
_LigoDot11IfLinkQuality_Object = MibTableColumn
ligoDot11IfLinkQuality = _LigoDot11IfLinkQuality_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 2, 1, 1, 12),
    _LigoDot11IfLinkQuality_Type()
)
ligoDot11IfLinkQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoDot11IfLinkQuality.setStatus("current")
_LigoDot11IfMaxLinkQuality_Type = Gauge32
_LigoDot11IfMaxLinkQuality_Object = MibTableColumn
ligoDot11IfMaxLinkQuality = _LigoDot11IfMaxLinkQuality_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 2, 1, 1, 13),
    _LigoDot11IfMaxLinkQuality_Type()
)
ligoDot11IfMaxLinkQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoDot11IfMaxLinkQuality.setStatus("current")
_LigoDot11IfSignalLevel_Type = Integer32
_LigoDot11IfSignalLevel_Object = MibTableColumn
ligoDot11IfSignalLevel = _LigoDot11IfSignalLevel_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 2, 1, 1, 14),
    _LigoDot11IfSignalLevel_Type()
)
ligoDot11IfSignalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoDot11IfSignalLevel.setStatus("current")
if mibBuilder.loadTexts:
    ligoDot11IfSignalLevel.setUnits("dBm")
_LigoDot11IfNoiseLevel_Type = Integer32
_LigoDot11IfNoiseLevel_Object = MibTableColumn
ligoDot11IfNoiseLevel = _LigoDot11IfNoiseLevel_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 2, 1, 1, 15),
    _LigoDot11IfNoiseLevel_Type()
)
ligoDot11IfNoiseLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoDot11IfNoiseLevel.setStatus("current")
if mibBuilder.loadTexts:
    ligoDot11IfNoiseLevel.setUnits("dBm")
_LigoDot11IfAssocNodeCount_Type = Gauge32
_LigoDot11IfAssocNodeCount_Object = MibTableColumn
ligoDot11IfAssocNodeCount = _LigoDot11IfAssocNodeCount_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 2, 1, 1, 16),
    _LigoDot11IfAssocNodeCount_Type()
)
ligoDot11IfAssocNodeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoDot11IfAssocNodeCount.setStatus("current")
_LigoDot11Stats_ObjectIdentity = ObjectIdentity
ligoDot11Stats = _LigoDot11Stats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 3)
)
_LigoDot11IfErrStatsTable_Object = MibTable
ligoDot11IfErrStatsTable = _LigoDot11IfErrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ligoDot11IfErrStatsTable.setStatus("current")
_LigoDot11IfErrStatsEntry_Object = MibTableRow
ligoDot11IfErrStatsEntry = _LigoDot11IfErrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 3, 1, 1)
)
ligoDot11IfErrStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ligoDot11IfErrStatsEntry.setStatus("current")
_LigoDot11IfRxInvalidNWID_Type = Counter32
_LigoDot11IfRxInvalidNWID_Object = MibTableColumn
ligoDot11IfRxInvalidNWID = _LigoDot11IfRxInvalidNWID_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 3, 1, 1, 1),
    _LigoDot11IfRxInvalidNWID_Type()
)
ligoDot11IfRxInvalidNWID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoDot11IfRxInvalidNWID.setStatus("current")
_LigoDot11IfRxInvalidCrypt_Type = Counter32
_LigoDot11IfRxInvalidCrypt_Object = MibTableColumn
ligoDot11IfRxInvalidCrypt = _LigoDot11IfRxInvalidCrypt_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 3, 1, 1, 2),
    _LigoDot11IfRxInvalidCrypt_Type()
)
ligoDot11IfRxInvalidCrypt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoDot11IfRxInvalidCrypt.setStatus("current")
_LigoDot11IfRxInvalidFrag_Type = Counter32
_LigoDot11IfRxInvalidFrag_Object = MibTableColumn
ligoDot11IfRxInvalidFrag = _LigoDot11IfRxInvalidFrag_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 3, 1, 1, 3),
    _LigoDot11IfRxInvalidFrag_Type()
)
ligoDot11IfRxInvalidFrag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoDot11IfRxInvalidFrag.setStatus("current")
_LigoDot11IfTxExcessiveRetries_Type = Counter32
_LigoDot11IfTxExcessiveRetries_Object = MibTableColumn
ligoDot11IfTxExcessiveRetries = _LigoDot11IfTxExcessiveRetries_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 3, 1, 1, 4),
    _LigoDot11IfTxExcessiveRetries_Type()
)
ligoDot11IfTxExcessiveRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoDot11IfTxExcessiveRetries.setStatus("current")
_LigoDot11IfInvalidMisc_Type = Counter32
_LigoDot11IfInvalidMisc_Object = MibTableColumn
ligoDot11IfInvalidMisc = _LigoDot11IfInvalidMisc_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 3, 1, 1, 5),
    _LigoDot11IfInvalidMisc_Type()
)
ligoDot11IfInvalidMisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoDot11IfInvalidMisc.setStatus("current")
_LigoDot11IfMissedBeacons_Type = Counter32
_LigoDot11IfMissedBeacons_Object = MibTableColumn
ligoDot11IfMissedBeacons = _LigoDot11IfMissedBeacons_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 3, 1, 1, 6),
    _LigoDot11IfMissedBeacons_Type()
)
ligoDot11IfMissedBeacons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoDot11IfMissedBeacons.setStatus("current")
_LigoDot11RemoteNodeStatsTable_Object = MibTable
ligoDot11RemoteNodeStatsTable = _LigoDot11RemoteNodeStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 3, 2)
)
if mibBuilder.loadTexts:
    ligoDot11RemoteNodeStatsTable.setStatus("current")
_LigoDot11RemoteNodeStatsEntry_Object = MibTableRow
ligoDot11RemoteNodeStatsEntry = _LigoDot11RemoteNodeStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 3, 2, 1)
)
ligoDot11RemoteNodeStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "LIGO-802DOT11-EXT-MIB", "ligoDot11RmtNodeMacAddress"),
)
if mibBuilder.loadTexts:
    ligoDot11RemoteNodeStatsEntry.setStatus("current")
_LigoDot11RmtNodeMacAddress_Type = MacAddress
_LigoDot11RmtNodeMacAddress_Object = MibTableColumn
ligoDot11RmtNodeMacAddress = _LigoDot11RmtNodeMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 3, 2, 1, 1),
    _LigoDot11RmtNodeMacAddress_Type()
)
ligoDot11RmtNodeMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoDot11RmtNodeMacAddress.setStatus("current")
_LigoDot11RmtNodeAssociated_Type = TruthValue
_LigoDot11RmtNodeAssociated_Object = MibTableColumn
ligoDot11RmtNodeAssociated = _LigoDot11RmtNodeAssociated_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 3, 2, 1, 2),
    _LigoDot11RmtNodeAssociated_Type()
)
ligoDot11RmtNodeAssociated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoDot11RmtNodeAssociated.setStatus("current")
_LigoDot11RmtNodeTxBytes_Type = Counter32
_LigoDot11RmtNodeTxBytes_Object = MibTableColumn
ligoDot11RmtNodeTxBytes = _LigoDot11RmtNodeTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 3, 2, 1, 3),
    _LigoDot11RmtNodeTxBytes_Type()
)
ligoDot11RmtNodeTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoDot11RmtNodeTxBytes.setStatus("current")
if mibBuilder.loadTexts:
    ligoDot11RmtNodeTxBytes.setUnits("bytes")
_LigoDot11RmtNodeRxBytes_Type = Counter32
_LigoDot11RmtNodeRxBytes_Object = MibTableColumn
ligoDot11RmtNodeRxBytes = _LigoDot11RmtNodeRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 3, 2, 1, 4),
    _LigoDot11RmtNodeRxBytes_Type()
)
ligoDot11RmtNodeRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoDot11RmtNodeRxBytes.setStatus("current")
if mibBuilder.loadTexts:
    ligoDot11RmtNodeRxBytes.setUnits("bytes")
_LigoDot11RmtNodeAssocTime_Type = Integer32
_LigoDot11RmtNodeAssocTime_Object = MibTableColumn
ligoDot11RmtNodeAssocTime = _LigoDot11RmtNodeAssocTime_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 3, 2, 1, 5),
    _LigoDot11RmtNodeAssocTime_Type()
)
ligoDot11RmtNodeAssocTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoDot11RmtNodeAssocTime.setStatus("current")
_LigoDot11RmtNodeDisassocTime_Type = Integer32
_LigoDot11RmtNodeDisassocTime_Object = MibTableColumn
ligoDot11RmtNodeDisassocTime = _LigoDot11RmtNodeDisassocTime_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 3, 2, 1, 6),
    _LigoDot11RmtNodeDisassocTime_Type()
)
ligoDot11RmtNodeDisassocTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoDot11RmtNodeDisassocTime.setStatus("current")

# Managed Objects groups


# Notification objects

ligoFrequencyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 0, 1)
)
ligoFrequencyChange.setObjects(
      *(("SNMPv2-MIB", "sysLocation"),
        ("IF-MIB", "ifIndex"),
        ("LIGO-802DOT11-EXT-MIB", "ligoDot11IfFrequency"))
)
if mibBuilder.loadTexts:
    ligoFrequencyChange.setStatus(
        "current"
    )

ligoNoiseThresholdReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 0, 2)
)
ligoNoiseThresholdReached.setObjects(
      *(("SNMPv2-MIB", "sysLocation"),
        ("IF-MIB", "ifIndex"),
        ("LIGO-802DOT11-EXT-MIB", "ligoDot11IfNoiseLevel"))
)
if mibBuilder.loadTexts:
    ligoNoiseThresholdReached.setStatus(
        "current"
    )

ligoRemoteNodeConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 0, 3)
)
ligoRemoteNodeConnected.setObjects(
      *(("SNMPv2-MIB", "sysLocation"),
        ("IF-MIB", "ifPhysAddress"),
        ("IF-MIB", "ifIndex"),
        ("LIGO-802DOT11-EXT-MIB", "ligoDot11RmtNodeMacAddress"))
)
if mibBuilder.loadTexts:
    ligoRemoteNodeConnected.setStatus(
        "current"
    )

ligoRemoteNodeDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 0, 4)
)
ligoRemoteNodeDisconnected.setObjects(
      *(("SNMPv2-MIB", "sysLocation"),
        ("IF-MIB", "ifPhysAddress"),
        ("IF-MIB", "ifIndex"),
        ("LIGO-802DOT11-EXT-MIB", "ligoDot11RmtNodeMacAddress"))
)
if mibBuilder.loadTexts:
    ligoRemoteNodeDisconnected.setStatus(
        "current"
    )

ligoLinkQualThresholdReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 32750, 3, 5, 1, 0, 5)
)
ligoLinkQualThresholdReached.setObjects(
      *(("SNMPv2-MIB", "sysLocation"),
        ("IF-MIB", "ifIndex"),
        ("LIGO-802DOT11-EXT-MIB", "ligoDot11IfLinkQuality"))
)
if mibBuilder.loadTexts:
    ligoLinkQualThresholdReached.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LIGO-802DOT11-EXT-MIB",
    **{"ligo802dot11ExtMIB": ligo802dot11ExtMIB,
       "ligo802dot11ExtMIBObjects": ligo802dot11ExtMIBObjects,
       "ligoDot11Notifs": ligoDot11Notifs,
       "ligoFrequencyChange": ligoFrequencyChange,
       "ligoNoiseThresholdReached": ligoNoiseThresholdReached,
       "ligoRemoteNodeConnected": ligoRemoteNodeConnected,
       "ligoRemoteNodeDisconnected": ligoRemoteNodeDisconnected,
       "ligoLinkQualThresholdReached": ligoLinkQualThresholdReached,
       "ligoDot11Info": ligoDot11Info,
       "ligoDot11Conf": ligoDot11Conf,
       "ligoDot11IfConfTable": ligoDot11IfConfTable,
       "ligoDot11IfConfEntry": ligoDot11IfConfEntry,
       "ligoDot11IfParentIndex": ligoDot11IfParentIndex,
       "ligoDot11IfProtocol": ligoDot11IfProtocol,
       "ligoDot11IfMode": ligoDot11IfMode,
       "ligoDot11IfESSID": ligoDot11IfESSID,
       "ligoDot11IfAccessPoint": ligoDot11IfAccessPoint,
       "ligoDot11IfCountryCode": ligoDot11IfCountryCode,
       "ligoDot11IfFrequency": ligoDot11IfFrequency,
       "ligoDot11IfChannel": ligoDot11IfChannel,
       "ligoDot11IfChannelBandwidth": ligoDot11IfChannelBandwidth,
       "ligoDot11IfTxPower": ligoDot11IfTxPower,
       "ligoDot11IfBitRate": ligoDot11IfBitRate,
       "ligoDot11IfLinkQuality": ligoDot11IfLinkQuality,
       "ligoDot11IfMaxLinkQuality": ligoDot11IfMaxLinkQuality,
       "ligoDot11IfSignalLevel": ligoDot11IfSignalLevel,
       "ligoDot11IfNoiseLevel": ligoDot11IfNoiseLevel,
       "ligoDot11IfAssocNodeCount": ligoDot11IfAssocNodeCount,
       "ligoDot11Stats": ligoDot11Stats,
       "ligoDot11IfErrStatsTable": ligoDot11IfErrStatsTable,
       "ligoDot11IfErrStatsEntry": ligoDot11IfErrStatsEntry,
       "ligoDot11IfRxInvalidNWID": ligoDot11IfRxInvalidNWID,
       "ligoDot11IfRxInvalidCrypt": ligoDot11IfRxInvalidCrypt,
       "ligoDot11IfRxInvalidFrag": ligoDot11IfRxInvalidFrag,
       "ligoDot11IfTxExcessiveRetries": ligoDot11IfTxExcessiveRetries,
       "ligoDot11IfInvalidMisc": ligoDot11IfInvalidMisc,
       "ligoDot11IfMissedBeacons": ligoDot11IfMissedBeacons,
       "ligoDot11RemoteNodeStatsTable": ligoDot11RemoteNodeStatsTable,
       "ligoDot11RemoteNodeStatsEntry": ligoDot11RemoteNodeStatsEntry,
       "ligoDot11RmtNodeMacAddress": ligoDot11RmtNodeMacAddress,
       "ligoDot11RmtNodeAssociated": ligoDot11RmtNodeAssociated,
       "ligoDot11RmtNodeTxBytes": ligoDot11RmtNodeTxBytes,
       "ligoDot11RmtNodeRxBytes": ligoDot11RmtNodeRxBytes,
       "ligoDot11RmtNodeAssocTime": ligoDot11RmtNodeAssocTime,
       "ligoDot11RmtNodeDisassocTime": ligoDot11RmtNodeDisassocTime}
)
