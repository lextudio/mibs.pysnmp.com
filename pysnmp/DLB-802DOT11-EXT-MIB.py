# SNMP MIB module (DLB-802DOT11-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DLB-802DOT11-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:29:33 2024
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

(dlbMgmt,) = mibBuilder.importSymbols(
    "DELIBERANT-MIB",
    "dlbMgmt")

(InterfaceIndex,
 ifIndex,
 ifPhysAddress) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex",
    "ifPhysAddress")

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

dlb802dot11ExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 32761, 3, 5)
)
dlb802dot11ExtMIB.setRevisions(
        ("2010-03-31 00:00",
         "2009-05-15 00:00",
         "2008-12-12 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dlb802dot11ExtMIBObjects_ObjectIdentity = ObjectIdentity
dlb802dot11ExtMIBObjects = _Dlb802dot11ExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32761, 3, 5, 1)
)
_DlbDot11Notifs_ObjectIdentity = ObjectIdentity
dlbDot11Notifs = _DlbDot11Notifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 0)
)
_DlbDot11Info_ObjectIdentity = ObjectIdentity
dlbDot11Info = _DlbDot11Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 1)
)
_DlbDot11Conf_ObjectIdentity = ObjectIdentity
dlbDot11Conf = _DlbDot11Conf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 2)
)
_DlbDot11IfConfTable_Object = MibTable
dlbDot11IfConfTable = _DlbDot11IfConfTable_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dlbDot11IfConfTable.setStatus("current")
_DlbDot11IfConfEntry_Object = MibTableRow
dlbDot11IfConfEntry = _DlbDot11IfConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 2, 1, 1)
)
dlbDot11IfConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dlbDot11IfConfEntry.setStatus("current")
_DlbDot11IfParentIndex_Type = InterfaceIndex
_DlbDot11IfParentIndex_Object = MibTableColumn
dlbDot11IfParentIndex = _DlbDot11IfParentIndex_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 2, 1, 1, 1),
    _DlbDot11IfParentIndex_Type()
)
dlbDot11IfParentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbDot11IfParentIndex.setStatus("current")


class _DlbDot11IfProtocol_Type(OctetString):
    """Custom type dlbDot11IfProtocol based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_DlbDot11IfProtocol_Type.__name__ = "OctetString"
_DlbDot11IfProtocol_Object = MibTableColumn
dlbDot11IfProtocol = _DlbDot11IfProtocol_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 2, 1, 1, 2),
    _DlbDot11IfProtocol_Type()
)
dlbDot11IfProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbDot11IfProtocol.setStatus("current")


class _DlbDot11IfMode_Type(Integer32):
    """Custom type dlbDot11IfMode based on Integer32"""
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


_DlbDot11IfMode_Type.__name__ = "Integer32"
_DlbDot11IfMode_Object = MibTableColumn
dlbDot11IfMode = _DlbDot11IfMode_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 2, 1, 1, 3),
    _DlbDot11IfMode_Type()
)
dlbDot11IfMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbDot11IfMode.setStatus("current")


class _DlbDot11IfESSID_Type(OctetString):
    """Custom type dlbDot11IfESSID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DlbDot11IfESSID_Type.__name__ = "OctetString"
_DlbDot11IfESSID_Object = MibTableColumn
dlbDot11IfESSID = _DlbDot11IfESSID_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 2, 1, 1, 4),
    _DlbDot11IfESSID_Type()
)
dlbDot11IfESSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbDot11IfESSID.setStatus("current")
_DlbDot11IfAccessPoint_Type = MacAddress
_DlbDot11IfAccessPoint_Object = MibTableColumn
dlbDot11IfAccessPoint = _DlbDot11IfAccessPoint_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 2, 1, 1, 5),
    _DlbDot11IfAccessPoint_Type()
)
dlbDot11IfAccessPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbDot11IfAccessPoint.setStatus("current")
_DlbDot11IfCountryCode_Type = Integer32
_DlbDot11IfCountryCode_Object = MibTableColumn
dlbDot11IfCountryCode = _DlbDot11IfCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 2, 1, 1, 6),
    _DlbDot11IfCountryCode_Type()
)
dlbDot11IfCountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbDot11IfCountryCode.setStatus("current")
_DlbDot11IfFrequency_Type = Integer32
_DlbDot11IfFrequency_Object = MibTableColumn
dlbDot11IfFrequency = _DlbDot11IfFrequency_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 2, 1, 1, 7),
    _DlbDot11IfFrequency_Type()
)
dlbDot11IfFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbDot11IfFrequency.setStatus("current")
if mibBuilder.loadTexts:
    dlbDot11IfFrequency.setUnits("MHz")
_DlbDot11IfChannel_Type = Integer32
_DlbDot11IfChannel_Object = MibTableColumn
dlbDot11IfChannel = _DlbDot11IfChannel_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 2, 1, 1, 8),
    _DlbDot11IfChannel_Type()
)
dlbDot11IfChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbDot11IfChannel.setStatus("current")
_DlbDot11IfChannelBandwidth_Type = Integer32
_DlbDot11IfChannelBandwidth_Object = MibTableColumn
dlbDot11IfChannelBandwidth = _DlbDot11IfChannelBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 2, 1, 1, 9),
    _DlbDot11IfChannelBandwidth_Type()
)
dlbDot11IfChannelBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbDot11IfChannelBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    dlbDot11IfChannelBandwidth.setUnits("MHz")
_DlbDot11IfTxPower_Type = Gauge32
_DlbDot11IfTxPower_Object = MibTableColumn
dlbDot11IfTxPower = _DlbDot11IfTxPower_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 2, 1, 1, 10),
    _DlbDot11IfTxPower_Type()
)
dlbDot11IfTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbDot11IfTxPower.setStatus("current")
if mibBuilder.loadTexts:
    dlbDot11IfTxPower.setUnits("dBm")
_DlbDot11IfBitRate_Type = Gauge32
_DlbDot11IfBitRate_Object = MibTableColumn
dlbDot11IfBitRate = _DlbDot11IfBitRate_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 2, 1, 1, 11),
    _DlbDot11IfBitRate_Type()
)
dlbDot11IfBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbDot11IfBitRate.setStatus("current")
if mibBuilder.loadTexts:
    dlbDot11IfBitRate.setUnits("kbit/s")
_DlbDot11IfLinkQuality_Type = Gauge32
_DlbDot11IfLinkQuality_Object = MibTableColumn
dlbDot11IfLinkQuality = _DlbDot11IfLinkQuality_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 2, 1, 1, 12),
    _DlbDot11IfLinkQuality_Type()
)
dlbDot11IfLinkQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbDot11IfLinkQuality.setStatus("current")
_DlbDot11IfMaxLinkQuality_Type = Gauge32
_DlbDot11IfMaxLinkQuality_Object = MibTableColumn
dlbDot11IfMaxLinkQuality = _DlbDot11IfMaxLinkQuality_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 2, 1, 1, 13),
    _DlbDot11IfMaxLinkQuality_Type()
)
dlbDot11IfMaxLinkQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbDot11IfMaxLinkQuality.setStatus("current")
_DlbDot11IfSignalLevel_Type = Integer32
_DlbDot11IfSignalLevel_Object = MibTableColumn
dlbDot11IfSignalLevel = _DlbDot11IfSignalLevel_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 2, 1, 1, 14),
    _DlbDot11IfSignalLevel_Type()
)
dlbDot11IfSignalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbDot11IfSignalLevel.setStatus("current")
if mibBuilder.loadTexts:
    dlbDot11IfSignalLevel.setUnits("dBm")
_DlbDot11IfNoiseLevel_Type = Integer32
_DlbDot11IfNoiseLevel_Object = MibTableColumn
dlbDot11IfNoiseLevel = _DlbDot11IfNoiseLevel_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 2, 1, 1, 15),
    _DlbDot11IfNoiseLevel_Type()
)
dlbDot11IfNoiseLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbDot11IfNoiseLevel.setStatus("current")
if mibBuilder.loadTexts:
    dlbDot11IfNoiseLevel.setUnits("dBm")
_DlbDot11IfAssocNodeCount_Type = Gauge32
_DlbDot11IfAssocNodeCount_Object = MibTableColumn
dlbDot11IfAssocNodeCount = _DlbDot11IfAssocNodeCount_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 2, 1, 1, 16),
    _DlbDot11IfAssocNodeCount_Type()
)
dlbDot11IfAssocNodeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbDot11IfAssocNodeCount.setStatus("current")
_DlbDot11Stats_ObjectIdentity = ObjectIdentity
dlbDot11Stats = _DlbDot11Stats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 3)
)
_DlbDot11IfErrStatsTable_Object = MibTable
dlbDot11IfErrStatsTable = _DlbDot11IfErrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dlbDot11IfErrStatsTable.setStatus("current")
_DlbDot11IfErrStatsEntry_Object = MibTableRow
dlbDot11IfErrStatsEntry = _DlbDot11IfErrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 3, 1, 1)
)
dlbDot11IfErrStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dlbDot11IfErrStatsEntry.setStatus("current")
_DlbDot11IfRxInvalidNWID_Type = Counter32
_DlbDot11IfRxInvalidNWID_Object = MibTableColumn
dlbDot11IfRxInvalidNWID = _DlbDot11IfRxInvalidNWID_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 3, 1, 1, 1),
    _DlbDot11IfRxInvalidNWID_Type()
)
dlbDot11IfRxInvalidNWID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbDot11IfRxInvalidNWID.setStatus("current")
_DlbDot11IfRxInvalidCrypt_Type = Counter32
_DlbDot11IfRxInvalidCrypt_Object = MibTableColumn
dlbDot11IfRxInvalidCrypt = _DlbDot11IfRxInvalidCrypt_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 3, 1, 1, 2),
    _DlbDot11IfRxInvalidCrypt_Type()
)
dlbDot11IfRxInvalidCrypt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbDot11IfRxInvalidCrypt.setStatus("current")
_DlbDot11IfRxInvalidFrag_Type = Counter32
_DlbDot11IfRxInvalidFrag_Object = MibTableColumn
dlbDot11IfRxInvalidFrag = _DlbDot11IfRxInvalidFrag_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 3, 1, 1, 3),
    _DlbDot11IfRxInvalidFrag_Type()
)
dlbDot11IfRxInvalidFrag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbDot11IfRxInvalidFrag.setStatus("current")
_DlbDot11IfTxExcessiveRetries_Type = Counter32
_DlbDot11IfTxExcessiveRetries_Object = MibTableColumn
dlbDot11IfTxExcessiveRetries = _DlbDot11IfTxExcessiveRetries_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 3, 1, 1, 4),
    _DlbDot11IfTxExcessiveRetries_Type()
)
dlbDot11IfTxExcessiveRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbDot11IfTxExcessiveRetries.setStatus("current")
_DlbDot11IfInvalidMisc_Type = Counter32
_DlbDot11IfInvalidMisc_Object = MibTableColumn
dlbDot11IfInvalidMisc = _DlbDot11IfInvalidMisc_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 3, 1, 1, 5),
    _DlbDot11IfInvalidMisc_Type()
)
dlbDot11IfInvalidMisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbDot11IfInvalidMisc.setStatus("current")
_DlbDot11IfMissedBeacons_Type = Counter32
_DlbDot11IfMissedBeacons_Object = MibTableColumn
dlbDot11IfMissedBeacons = _DlbDot11IfMissedBeacons_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 3, 1, 1, 6),
    _DlbDot11IfMissedBeacons_Type()
)
dlbDot11IfMissedBeacons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbDot11IfMissedBeacons.setStatus("current")
_DlbDot11RemoteNodeStatsTable_Object = MibTable
dlbDot11RemoteNodeStatsTable = _DlbDot11RemoteNodeStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 3, 2)
)
if mibBuilder.loadTexts:
    dlbDot11RemoteNodeStatsTable.setStatus("current")
_DlbDot11RemoteNodeStatsEntry_Object = MibTableRow
dlbDot11RemoteNodeStatsEntry = _DlbDot11RemoteNodeStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 3, 2, 1)
)
dlbDot11RemoteNodeStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DLB-802DOT11-EXT-MIB", "dlbDot11RmtNodeMacAddress"),
)
if mibBuilder.loadTexts:
    dlbDot11RemoteNodeStatsEntry.setStatus("current")
_DlbDot11RmtNodeMacAddress_Type = MacAddress
_DlbDot11RmtNodeMacAddress_Object = MibTableColumn
dlbDot11RmtNodeMacAddress = _DlbDot11RmtNodeMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 3, 2, 1, 1),
    _DlbDot11RmtNodeMacAddress_Type()
)
dlbDot11RmtNodeMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbDot11RmtNodeMacAddress.setStatus("current")
_DlbDot11RmtNodeAssociated_Type = TruthValue
_DlbDot11RmtNodeAssociated_Object = MibTableColumn
dlbDot11RmtNodeAssociated = _DlbDot11RmtNodeAssociated_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 3, 2, 1, 2),
    _DlbDot11RmtNodeAssociated_Type()
)
dlbDot11RmtNodeAssociated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbDot11RmtNodeAssociated.setStatus("current")
_DlbDot11RmtNodeTxBytes_Type = Counter32
_DlbDot11RmtNodeTxBytes_Object = MibTableColumn
dlbDot11RmtNodeTxBytes = _DlbDot11RmtNodeTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 3, 2, 1, 3),
    _DlbDot11RmtNodeTxBytes_Type()
)
dlbDot11RmtNodeTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbDot11RmtNodeTxBytes.setStatus("current")
if mibBuilder.loadTexts:
    dlbDot11RmtNodeTxBytes.setUnits("bytes")
_DlbDot11RmtNodeRxBytes_Type = Counter32
_DlbDot11RmtNodeRxBytes_Object = MibTableColumn
dlbDot11RmtNodeRxBytes = _DlbDot11RmtNodeRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 3, 2, 1, 4),
    _DlbDot11RmtNodeRxBytes_Type()
)
dlbDot11RmtNodeRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbDot11RmtNodeRxBytes.setStatus("current")
if mibBuilder.loadTexts:
    dlbDot11RmtNodeRxBytes.setUnits("bytes")
_DlbDot11RmtNodeAssocTime_Type = Integer32
_DlbDot11RmtNodeAssocTime_Object = MibTableColumn
dlbDot11RmtNodeAssocTime = _DlbDot11RmtNodeAssocTime_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 3, 2, 1, 5),
    _DlbDot11RmtNodeAssocTime_Type()
)
dlbDot11RmtNodeAssocTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbDot11RmtNodeAssocTime.setStatus("current")
_DlbDot11RmtNodeDisassocTime_Type = Integer32
_DlbDot11RmtNodeDisassocTime_Object = MibTableColumn
dlbDot11RmtNodeDisassocTime = _DlbDot11RmtNodeDisassocTime_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 3, 2, 1, 6),
    _DlbDot11RmtNodeDisassocTime_Type()
)
dlbDot11RmtNodeDisassocTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbDot11RmtNodeDisassocTime.setStatus("current")

# Managed Objects groups


# Notification objects

dlbFrequencyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 0, 1)
)
dlbFrequencyChange.setObjects(
      *(("SNMPv2-MIB", "sysLocation"),
        ("IF-MIB", "ifIndex"),
        ("DLB-802DOT11-EXT-MIB", "dlbDot11IfFrequency"))
)
if mibBuilder.loadTexts:
    dlbFrequencyChange.setStatus(
        "current"
    )

dlbNoiseThresholdReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 0, 2)
)
dlbNoiseThresholdReached.setObjects(
      *(("SNMPv2-MIB", "sysLocation"),
        ("IF-MIB", "ifIndex"),
        ("DLB-802DOT11-EXT-MIB", "dlbDot11IfNoiseLevel"))
)
if mibBuilder.loadTexts:
    dlbNoiseThresholdReached.setStatus(
        "current"
    )

dlbRemoteNodeConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 0, 3)
)
dlbRemoteNodeConnected.setObjects(
      *(("SNMPv2-MIB", "sysLocation"),
        ("IF-MIB", "ifPhysAddress"),
        ("IF-MIB", "ifIndex"),
        ("DLB-802DOT11-EXT-MIB", "dlbDot11RmtNodeMacAddress"))
)
if mibBuilder.loadTexts:
    dlbRemoteNodeConnected.setStatus(
        "current"
    )

dlbRemoteNodeDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 0, 4)
)
dlbRemoteNodeDisconnected.setObjects(
      *(("SNMPv2-MIB", "sysLocation"),
        ("IF-MIB", "ifPhysAddress"),
        ("IF-MIB", "ifIndex"),
        ("DLB-802DOT11-EXT-MIB", "dlbDot11RmtNodeMacAddress"))
)
if mibBuilder.loadTexts:
    dlbRemoteNodeDisconnected.setStatus(
        "current"
    )

dlbLinkQualThresholdReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 32761, 3, 5, 1, 0, 5)
)
dlbLinkQualThresholdReached.setObjects(
      *(("SNMPv2-MIB", "sysLocation"),
        ("IF-MIB", "ifIndex"),
        ("DLB-802DOT11-EXT-MIB", "dlbDot11IfLinkQuality"))
)
if mibBuilder.loadTexts:
    dlbLinkQualThresholdReached.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLB-802DOT11-EXT-MIB",
    **{"dlb802dot11ExtMIB": dlb802dot11ExtMIB,
       "dlb802dot11ExtMIBObjects": dlb802dot11ExtMIBObjects,
       "dlbDot11Notifs": dlbDot11Notifs,
       "dlbFrequencyChange": dlbFrequencyChange,
       "dlbNoiseThresholdReached": dlbNoiseThresholdReached,
       "dlbRemoteNodeConnected": dlbRemoteNodeConnected,
       "dlbRemoteNodeDisconnected": dlbRemoteNodeDisconnected,
       "dlbLinkQualThresholdReached": dlbLinkQualThresholdReached,
       "dlbDot11Info": dlbDot11Info,
       "dlbDot11Conf": dlbDot11Conf,
       "dlbDot11IfConfTable": dlbDot11IfConfTable,
       "dlbDot11IfConfEntry": dlbDot11IfConfEntry,
       "dlbDot11IfParentIndex": dlbDot11IfParentIndex,
       "dlbDot11IfProtocol": dlbDot11IfProtocol,
       "dlbDot11IfMode": dlbDot11IfMode,
       "dlbDot11IfESSID": dlbDot11IfESSID,
       "dlbDot11IfAccessPoint": dlbDot11IfAccessPoint,
       "dlbDot11IfCountryCode": dlbDot11IfCountryCode,
       "dlbDot11IfFrequency": dlbDot11IfFrequency,
       "dlbDot11IfChannel": dlbDot11IfChannel,
       "dlbDot11IfChannelBandwidth": dlbDot11IfChannelBandwidth,
       "dlbDot11IfTxPower": dlbDot11IfTxPower,
       "dlbDot11IfBitRate": dlbDot11IfBitRate,
       "dlbDot11IfLinkQuality": dlbDot11IfLinkQuality,
       "dlbDot11IfMaxLinkQuality": dlbDot11IfMaxLinkQuality,
       "dlbDot11IfSignalLevel": dlbDot11IfSignalLevel,
       "dlbDot11IfNoiseLevel": dlbDot11IfNoiseLevel,
       "dlbDot11IfAssocNodeCount": dlbDot11IfAssocNodeCount,
       "dlbDot11Stats": dlbDot11Stats,
       "dlbDot11IfErrStatsTable": dlbDot11IfErrStatsTable,
       "dlbDot11IfErrStatsEntry": dlbDot11IfErrStatsEntry,
       "dlbDot11IfRxInvalidNWID": dlbDot11IfRxInvalidNWID,
       "dlbDot11IfRxInvalidCrypt": dlbDot11IfRxInvalidCrypt,
       "dlbDot11IfRxInvalidFrag": dlbDot11IfRxInvalidFrag,
       "dlbDot11IfTxExcessiveRetries": dlbDot11IfTxExcessiveRetries,
       "dlbDot11IfInvalidMisc": dlbDot11IfInvalidMisc,
       "dlbDot11IfMissedBeacons": dlbDot11IfMissedBeacons,
       "dlbDot11RemoteNodeStatsTable": dlbDot11RemoteNodeStatsTable,
       "dlbDot11RemoteNodeStatsEntry": dlbDot11RemoteNodeStatsEntry,
       "dlbDot11RmtNodeMacAddress": dlbDot11RmtNodeMacAddress,
       "dlbDot11RmtNodeAssociated": dlbDot11RmtNodeAssociated,
       "dlbDot11RmtNodeTxBytes": dlbDot11RmtNodeTxBytes,
       "dlbDot11RmtNodeRxBytes": dlbDot11RmtNodeRxBytes,
       "dlbDot11RmtNodeAssocTime": dlbDot11RmtNodeAssocTime,
       "dlbDot11RmtNodeDisassocTime": dlbDot11RmtNodeDisassocTime}
)
