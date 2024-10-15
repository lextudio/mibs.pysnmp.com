# SNMP MIB module (AH-INTERFACE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AH-INTERFACE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:34:59 2024
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

(AhInterfaceMode,
 AhInterfaceType,
 AhMACProtocol,
 AhNodeID,
 AhString,
 ahAPInterface) = mibBuilder.importSymbols(
    "AH-SMI-MIB",
    "AhInterfaceMode",
    "AhInterfaceType",
    "AhMACProtocol",
    "AhNodeID",
    "AhString",
    "ahAPInterface")

(ifEntry,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifEntry",
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ahInterface = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AhAuthenticationMethod(Integer32, TextualConvention):
    status = "current"
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
        *(("cwp", 0),
          ("dynamic-wep", 10),
          ("open", 1),
          ("wep-open", 2),
          ("wep-shared", 3),
          ("wpa-8021x", 6),
          ("wpa-auto-8021x", 9),
          ("wpa-auto-psk", 8),
          ("wpa-psk", 4),
          ("wpa2-8021X", 7),
          ("wpa2-psk", 5))
    )



class AhEncrytionMethod(Integer32, TextualConvention):
    status = "current"
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
        *(("AES", 0),
          ("Non", 3),
          ("TKIP", 1),
          ("WEP", 2))
    )



# MIB Managed Objects in the order of their OIDs

_AhXIfTable_Object = MibTable
ahXIfTable = _AhXIfTable_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ahXIfTable.setStatus("current")
_AhXIfEntry_Object = MibTableRow
ahXIfEntry = _AhXIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ahXIfEntry.setStatus("current")
_AhIfName_Type = AhString
_AhIfName_Object = MibTableColumn
ahIfName = _AhIfName_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 1, 1, 1),
    _AhIfName_Type()
)
ahIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahIfName.setStatus("current")
_AhSSIDName_Type = AhString
_AhSSIDName_Object = MibTableColumn
ahSSIDName = _AhSSIDName_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 1, 1, 2),
    _AhSSIDName_Type()
)
ahSSIDName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahSSIDName.setStatus("current")
_AhIfPromiscuous_Type = TruthValue
_AhIfPromiscuous_Object = MibTableColumn
ahIfPromiscuous = _AhIfPromiscuous_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 1, 1, 3),
    _AhIfPromiscuous_Type()
)
ahIfPromiscuous.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahIfPromiscuous.setStatus("current")
_AhIfType_Type = AhInterfaceType
_AhIfType_Object = MibTableColumn
ahIfType = _AhIfType_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 1, 1, 4),
    _AhIfType_Type()
)
ahIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahIfType.setStatus("current")
_AhIfMode_Type = AhInterfaceMode
_AhIfMode_Object = MibTableColumn
ahIfMode = _AhIfMode_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 1, 1, 5),
    _AhIfMode_Type()
)
ahIfMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahIfMode.setStatus("current")
_AhIfConfMode_Type = AhInterfaceMode
_AhIfConfMode_Object = MibTableColumn
ahIfConfMode = _AhIfConfMode_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 1, 1, 6),
    _AhIfConfMode_Type()
)
ahIfConfMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahIfConfMode.setStatus("current")
_AhAssociationTable_Object = MibTable
ahAssociationTable = _AhAssociationTable_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ahAssociationTable.setStatus("current")
_AhAssociationEntry_Object = MibTableRow
ahAssociationEntry = _AhAssociationEntry_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1)
)
ahAssociationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "AH-INTERFACE-MIB", "ahClientMac"),
)
if mibBuilder.loadTexts:
    ahAssociationEntry.setStatus("current")
_AhClientMac_Type = AhNodeID
_AhClientMac_Object = MibTableColumn
ahClientMac = _AhClientMac_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 1),
    _AhClientMac_Type()
)
ahClientMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahClientMac.setStatus("current")
_AhClientIP_Type = IpAddress
_AhClientIP_Object = MibTableColumn
ahClientIP = _AhClientIP_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 2),
    _AhClientIP_Type()
)
ahClientIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahClientIP.setStatus("current")
_AhClientHostname_Type = AhString
_AhClientHostname_Object = MibTableColumn
ahClientHostname = _AhClientHostname_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 3),
    _AhClientHostname_Type()
)
ahClientHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahClientHostname.setStatus("current")
_AhClientRSSI_Type = Integer32
_AhClientRSSI_Object = MibTableColumn
ahClientRSSI = _AhClientRSSI_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 4),
    _AhClientRSSI_Type()
)
ahClientRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahClientRSSI.setStatus("current")
_AhClientLinkUptime_Type = Counter32
_AhClientLinkUptime_Object = MibTableColumn
ahClientLinkUptime = _AhClientLinkUptime_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 5),
    _AhClientLinkUptime_Type()
)
ahClientLinkUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahClientLinkUptime.setStatus("current")
_AhClientCWPUsed_Type = TruthValue
_AhClientCWPUsed_Object = MibTableColumn
ahClientCWPUsed = _AhClientCWPUsed_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 6),
    _AhClientCWPUsed_Type()
)
ahClientCWPUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahClientCWPUsed.setStatus("current")
_AhClientAuthMethod_Type = AhAuthenticationMethod
_AhClientAuthMethod_Object = MibTableColumn
ahClientAuthMethod = _AhClientAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 7),
    _AhClientAuthMethod_Type()
)
ahClientAuthMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahClientAuthMethod.setStatus("current")
_AhClientEncryptionMethod_Type = AhEncrytionMethod
_AhClientEncryptionMethod_Object = MibTableColumn
ahClientEncryptionMethod = _AhClientEncryptionMethod_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 8),
    _AhClientEncryptionMethod_Type()
)
ahClientEncryptionMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahClientEncryptionMethod.setStatus("current")
_AhClientMACProtocol_Type = AhMACProtocol
_AhClientMACProtocol_Object = MibTableColumn
ahClientMACProtocol = _AhClientMACProtocol_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 9),
    _AhClientMACProtocol_Type()
)
ahClientMACProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahClientMACProtocol.setStatus("current")
_AhClientSSID_Type = AhString
_AhClientSSID_Object = MibTableColumn
ahClientSSID = _AhClientSSID_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 10),
    _AhClientSSID_Type()
)
ahClientSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahClientSSID.setStatus("current")
_AhClientVLAN_Type = Integer32
_AhClientVLAN_Object = MibTableColumn
ahClientVLAN = _AhClientVLAN_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 11),
    _AhClientVLAN_Type()
)
ahClientVLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahClientVLAN.setStatus("current")
_AhClientUserProfId_Type = Integer32
_AhClientUserProfId_Object = MibTableColumn
ahClientUserProfId = _AhClientUserProfId_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 12),
    _AhClientUserProfId_Type()
)
ahClientUserProfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahClientUserProfId.setStatus("current")
_AhClientChannel_Type = Integer32
_AhClientChannel_Object = MibTableColumn
ahClientChannel = _AhClientChannel_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 13),
    _AhClientChannel_Type()
)
ahClientChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahClientChannel.setStatus("current")
_AhClientLastTxRate_Type = Integer32
_AhClientLastTxRate_Object = MibTableColumn
ahClientLastTxRate = _AhClientLastTxRate_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 14),
    _AhClientLastTxRate_Type()
)
ahClientLastTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahClientLastTxRate.setStatus("current")
_AhClientUsername_Type = AhString
_AhClientUsername_Object = MibTableColumn
ahClientUsername = _AhClientUsername_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 15),
    _AhClientUsername_Type()
)
ahClientUsername.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahClientUsername.setStatus("current")
_AhClientRxDataFrames_Type = Counter32
_AhClientRxDataFrames_Object = MibTableColumn
ahClientRxDataFrames = _AhClientRxDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 16),
    _AhClientRxDataFrames_Type()
)
ahClientRxDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahClientRxDataFrames.setStatus("current")
_AhClientRxDataOctets_Type = Counter32
_AhClientRxDataOctets_Object = MibTableColumn
ahClientRxDataOctets = _AhClientRxDataOctets_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 17),
    _AhClientRxDataOctets_Type()
)
ahClientRxDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahClientRxDataOctets.setStatus("current")
_AhClientRxMgtFrames_Type = Counter32
_AhClientRxMgtFrames_Object = MibTableColumn
ahClientRxMgtFrames = _AhClientRxMgtFrames_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 18),
    _AhClientRxMgtFrames_Type()
)
ahClientRxMgtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahClientRxMgtFrames.setStatus("current")
_AhClientRxUnicastFrames_Type = Counter32
_AhClientRxUnicastFrames_Object = MibTableColumn
ahClientRxUnicastFrames = _AhClientRxUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 19),
    _AhClientRxUnicastFrames_Type()
)
ahClientRxUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahClientRxUnicastFrames.setStatus("current")
_AhClientRxMulticastFrames_Type = Counter32
_AhClientRxMulticastFrames_Object = MibScalar
ahClientRxMulticastFrames = _AhClientRxMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 20),
    _AhClientRxMulticastFrames_Type()
)
ahClientRxMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahClientRxMulticastFrames.setStatus("current")
_AhClientRxBroadcastFrames_Type = Counter32
_AhClientRxBroadcastFrames_Object = MibScalar
ahClientRxBroadcastFrames = _AhClientRxBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 21),
    _AhClientRxBroadcastFrames_Type()
)
ahClientRxBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahClientRxBroadcastFrames.setStatus("current")
_AhClientRxMICFailures_Type = Counter32
_AhClientRxMICFailures_Object = MibTableColumn
ahClientRxMICFailures = _AhClientRxMICFailures_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 22),
    _AhClientRxMICFailures_Type()
)
ahClientRxMICFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahClientRxMICFailures.setStatus("current")
_AhClientTxDataFrames_Type = Counter32
_AhClientTxDataFrames_Object = MibTableColumn
ahClientTxDataFrames = _AhClientTxDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 23),
    _AhClientTxDataFrames_Type()
)
ahClientTxDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahClientTxDataFrames.setStatus("current")
_AhClientTxMgtFrames_Type = Counter32
_AhClientTxMgtFrames_Object = MibTableColumn
ahClientTxMgtFrames = _AhClientTxMgtFrames_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 24),
    _AhClientTxMgtFrames_Type()
)
ahClientTxMgtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahClientTxMgtFrames.setStatus("current")
_AhClientTxDataOctets_Type = Counter32
_AhClientTxDataOctets_Object = MibTableColumn
ahClientTxDataOctets = _AhClientTxDataOctets_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 25),
    _AhClientTxDataOctets_Type()
)
ahClientTxDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahClientTxDataOctets.setStatus("current")
_AhClientTxUnicastFrames_Type = Counter32
_AhClientTxUnicastFrames_Object = MibTableColumn
ahClientTxUnicastFrames = _AhClientTxUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 26),
    _AhClientTxUnicastFrames_Type()
)
ahClientTxUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahClientTxUnicastFrames.setStatus("current")
_AhClientTxMulticastFrames_Type = Counter32
_AhClientTxMulticastFrames_Object = MibTableColumn
ahClientTxMulticastFrames = _AhClientTxMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 27),
    _AhClientTxMulticastFrames_Type()
)
ahClientTxMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahClientTxMulticastFrames.setStatus("current")
_AhClientTxBroadcastFrames_Type = Counter32
_AhClientTxBroadcastFrames_Object = MibTableColumn
ahClientTxBroadcastFrames = _AhClientTxBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 28),
    _AhClientTxBroadcastFrames_Type()
)
ahClientTxBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahClientTxBroadcastFrames.setStatus("current")
_AhClientLastRxRate_Type = Integer32
_AhClientLastRxRate_Object = MibTableColumn
ahClientLastRxRate = _AhClientLastRxRate_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 29),
    _AhClientLastRxRate_Type()
)
ahClientLastRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahClientLastRxRate.setStatus("current")
_AhClientTxBeDataFrames_Type = Counter32
_AhClientTxBeDataFrames_Object = MibTableColumn
ahClientTxBeDataFrames = _AhClientTxBeDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 30),
    _AhClientTxBeDataFrames_Type()
)
ahClientTxBeDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahClientTxBeDataFrames.setStatus("current")
_AhClientTxBgDataFrames_Type = Counter32
_AhClientTxBgDataFrames_Object = MibTableColumn
ahClientTxBgDataFrames = _AhClientTxBgDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 31),
    _AhClientTxBgDataFrames_Type()
)
ahClientTxBgDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahClientTxBgDataFrames.setStatus("current")
_AhClientTxViDataFrames_Type = Counter32
_AhClientTxViDataFrames_Object = MibTableColumn
ahClientTxViDataFrames = _AhClientTxViDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 32),
    _AhClientTxViDataFrames_Type()
)
ahClientTxViDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahClientTxViDataFrames.setStatus("current")
_AhClientTxVoDataFrames_Type = Counter32
_AhClientTxVoDataFrames_Object = MibTableColumn
ahClientTxVoDataFrames = _AhClientTxVoDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 33),
    _AhClientTxVoDataFrames_Type()
)
ahClientTxVoDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahClientTxVoDataFrames.setStatus("current")
_AhClientTxAirtime_Type = Counter64
_AhClientTxAirtime_Object = MibTableColumn
ahClientTxAirtime = _AhClientTxAirtime_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 34),
    _AhClientTxAirtime_Type()
)
ahClientTxAirtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahClientTxAirtime.setStatus("current")
_AhClientRxAirtime_Type = Counter64
_AhClientRxAirtime_Object = MibTableColumn
ahClientRxAirtime = _AhClientRxAirtime_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 35),
    _AhClientRxAirtime_Type()
)
ahClientRxAirtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahClientRxAirtime.setStatus("current")
_AhClientAssociationTime_Type = Counter32
_AhClientAssociationTime_Object = MibTableColumn
ahClientAssociationTime = _AhClientAssociationTime_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 36),
    _AhClientAssociationTime_Type()
)
ahClientAssociationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahClientAssociationTime.setStatus("current")
_AhClientBSSID_Type = AhNodeID
_AhClientBSSID_Object = MibTableColumn
ahClientBSSID = _AhClientBSSID_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 2, 1, 37),
    _AhClientBSSID_Type()
)
ahClientBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahClientBSSID.setStatus("current")
_AhRadioStatsTable_Object = MibTable
ahRadioStatsTable = _AhRadioStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ahRadioStatsTable.setStatus("current")
_AhRadioStatsEntry_Object = MibTableRow
ahRadioStatsEntry = _AhRadioStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1)
)
ahRadioStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ahRadioStatsEntry.setStatus("current")
_AhRadioTxDataFrames_Type = Counter32
_AhRadioTxDataFrames_Object = MibTableColumn
ahRadioTxDataFrames = _AhRadioTxDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 1),
    _AhRadioTxDataFrames_Type()
)
ahRadioTxDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahRadioTxDataFrames.setStatus("current")
_AhRadioTxUnicastDataFrames_Type = Counter32
_AhRadioTxUnicastDataFrames_Object = MibTableColumn
ahRadioTxUnicastDataFrames = _AhRadioTxUnicastDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 2),
    _AhRadioTxUnicastDataFrames_Type()
)
ahRadioTxUnicastDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahRadioTxUnicastDataFrames.setStatus("current")
_AhRadioTxMulticastDataFrames_Type = Counter32
_AhRadioTxMulticastDataFrames_Object = MibTableColumn
ahRadioTxMulticastDataFrames = _AhRadioTxMulticastDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 3),
    _AhRadioTxMulticastDataFrames_Type()
)
ahRadioTxMulticastDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahRadioTxMulticastDataFrames.setStatus("current")
_AhRadioTxBroadcastDataFrames_Type = Counter32
_AhRadioTxBroadcastDataFrames_Object = MibTableColumn
ahRadioTxBroadcastDataFrames = _AhRadioTxBroadcastDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 4),
    _AhRadioTxBroadcastDataFrames_Type()
)
ahRadioTxBroadcastDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahRadioTxBroadcastDataFrames.setStatus("current")
_AhRadioTxNonBeaconMgtFrames_Type = Counter32
_AhRadioTxNonBeaconMgtFrames_Object = MibTableColumn
ahRadioTxNonBeaconMgtFrames = _AhRadioTxNonBeaconMgtFrames_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 5),
    _AhRadioTxNonBeaconMgtFrames_Type()
)
ahRadioTxNonBeaconMgtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahRadioTxNonBeaconMgtFrames.setStatus("current")
_AhRadioTxBeaconFrames_Type = Counter32
_AhRadioTxBeaconFrames_Object = MibTableColumn
ahRadioTxBeaconFrames = _AhRadioTxBeaconFrames_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 6),
    _AhRadioTxBeaconFrames_Type()
)
ahRadioTxBeaconFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahRadioTxBeaconFrames.setStatus("current")
_AhRadioTxTotalRetries_Type = Counter32
_AhRadioTxTotalRetries_Object = MibTableColumn
ahRadioTxTotalRetries = _AhRadioTxTotalRetries_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 7),
    _AhRadioTxTotalRetries_Type()
)
ahRadioTxTotalRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahRadioTxTotalRetries.setStatus("current")
_AhRadioTxTotalFramesDropped_Type = Counter32
_AhRadioTxTotalFramesDropped_Object = MibTableColumn
ahRadioTxTotalFramesDropped = _AhRadioTxTotalFramesDropped_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 8),
    _AhRadioTxTotalFramesDropped_Type()
)
ahRadioTxTotalFramesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahRadioTxTotalFramesDropped.setStatus("current")
_AhRadioTxTotalFrameErrors_Type = Counter32
_AhRadioTxTotalFrameErrors_Object = MibTableColumn
ahRadioTxTotalFrameErrors = _AhRadioTxTotalFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 9),
    _AhRadioTxTotalFrameErrors_Type()
)
ahRadioTxTotalFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahRadioTxTotalFrameErrors.setStatus("current")
_AhRadioTxFEForExcessiveHWRetries_Type = Counter32
_AhRadioTxFEForExcessiveHWRetries_Object = MibTableColumn
ahRadioTxFEForExcessiveHWRetries = _AhRadioTxFEForExcessiveHWRetries_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 10),
    _AhRadioTxFEForExcessiveHWRetries_Type()
)
ahRadioTxFEForExcessiveHWRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahRadioTxFEForExcessiveHWRetries.setStatus("current")
_AhRadioRxTotalDataFrames_Type = Counter32
_AhRadioRxTotalDataFrames_Object = MibTableColumn
ahRadioRxTotalDataFrames = _AhRadioRxTotalDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 11),
    _AhRadioRxTotalDataFrames_Type()
)
ahRadioRxTotalDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahRadioRxTotalDataFrames.setStatus("current")
_AhRadioRxUnicastDataFrames_Type = Counter32
_AhRadioRxUnicastDataFrames_Object = MibTableColumn
ahRadioRxUnicastDataFrames = _AhRadioRxUnicastDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 12),
    _AhRadioRxUnicastDataFrames_Type()
)
ahRadioRxUnicastDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahRadioRxUnicastDataFrames.setStatus("current")
_AhRadioRxMulticastDataFrames_Type = Counter32
_AhRadioRxMulticastDataFrames_Object = MibTableColumn
ahRadioRxMulticastDataFrames = _AhRadioRxMulticastDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 13),
    _AhRadioRxMulticastDataFrames_Type()
)
ahRadioRxMulticastDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahRadioRxMulticastDataFrames.setStatus("current")
_AhRadioRxBroadcastDataFrames_Type = Counter32
_AhRadioRxBroadcastDataFrames_Object = MibTableColumn
ahRadioRxBroadcastDataFrames = _AhRadioRxBroadcastDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 14),
    _AhRadioRxBroadcastDataFrames_Type()
)
ahRadioRxBroadcastDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahRadioRxBroadcastDataFrames.setStatus("current")
_AhRadioRxMgtFrames_Type = Counter32
_AhRadioRxMgtFrames_Object = MibTableColumn
ahRadioRxMgtFrames = _AhRadioRxMgtFrames_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 15),
    _AhRadioRxMgtFrames_Type()
)
ahRadioRxMgtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahRadioRxMgtFrames.setStatus("current")
_AhRadioRxTotalFrameDropped_Type = Counter32
_AhRadioRxTotalFrameDropped_Object = MibTableColumn
ahRadioRxTotalFrameDropped = _AhRadioRxTotalFrameDropped_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 16),
    _AhRadioRxTotalFrameDropped_Type()
)
ahRadioRxTotalFrameDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahRadioRxTotalFrameDropped.setStatus("current")
_AhRadioTxBeDataFrames_Type = Counter32
_AhRadioTxBeDataFrames_Object = MibTableColumn
ahRadioTxBeDataFrames = _AhRadioTxBeDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 17),
    _AhRadioTxBeDataFrames_Type()
)
ahRadioTxBeDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahRadioTxBeDataFrames.setStatus("current")
_AhRadioTxBgDataFrames_Type = Counter32
_AhRadioTxBgDataFrames_Object = MibTableColumn
ahRadioTxBgDataFrames = _AhRadioTxBgDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 18),
    _AhRadioTxBgDataFrames_Type()
)
ahRadioTxBgDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahRadioTxBgDataFrames.setStatus("current")
_AhRadioTxViDataFrames_Type = Counter32
_AhRadioTxViDataFrames_Object = MibTableColumn
ahRadioTxViDataFrames = _AhRadioTxViDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 19),
    _AhRadioTxViDataFrames_Type()
)
ahRadioTxViDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahRadioTxViDataFrames.setStatus("current")
_AhRadioTxVoDataFrames_Type = Counter32
_AhRadioTxVoDataFrames_Object = MibTableColumn
ahRadioTxVoDataFrames = _AhRadioTxVoDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 20),
    _AhRadioTxVoDataFrames_Type()
)
ahRadioTxVoDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahRadioTxVoDataFrames.setStatus("current")
_AhRadioTXRTSFailures_Type = Counter32
_AhRadioTXRTSFailures_Object = MibTableColumn
ahRadioTXRTSFailures = _AhRadioTXRTSFailures_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 21),
    _AhRadioTXRTSFailures_Type()
)
ahRadioTXRTSFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahRadioTXRTSFailures.setStatus("current")
_AhRadioTxAirtime_Type = Counter64
_AhRadioTxAirtime_Object = MibTableColumn
ahRadioTxAirtime = _AhRadioTxAirtime_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 22),
    _AhRadioTxAirtime_Type()
)
ahRadioTxAirtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahRadioTxAirtime.setStatus("current")
_AhRadioRxAirtime_Type = Counter64
_AhRadioRxAirtime_Object = MibTableColumn
ahRadioRxAirtime = _AhRadioRxAirtime_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 3, 1, 23),
    _AhRadioRxAirtime_Type()
)
ahRadioRxAirtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahRadioRxAirtime.setStatus("current")
_AhVIfStatsTable_Object = MibTable
ahVIfStatsTable = _AhVIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4)
)
if mibBuilder.loadTexts:
    ahVIfStatsTable.setStatus("current")
_AhVIfStatsEntry_Object = MibTableRow
ahVIfStatsEntry = _AhVIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1)
)
ahVIfStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ahVIfStatsEntry.setStatus("current")
_AhVIfRxDataFrames_Type = Counter32
_AhVIfRxDataFrames_Object = MibTableColumn
ahVIfRxDataFrames = _AhVIfRxDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 1),
    _AhVIfRxDataFrames_Type()
)
ahVIfRxDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahVIfRxDataFrames.setStatus("current")
_AhVIfRxUnicastDataFrames_Type = Counter32
_AhVIfRxUnicastDataFrames_Object = MibTableColumn
ahVIfRxUnicastDataFrames = _AhVIfRxUnicastDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 2),
    _AhVIfRxUnicastDataFrames_Type()
)
ahVIfRxUnicastDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahVIfRxUnicastDataFrames.setStatus("current")
_AhVIfRxMulticastDataFrames_Type = Counter32
_AhVIfRxMulticastDataFrames_Object = MibTableColumn
ahVIfRxMulticastDataFrames = _AhVIfRxMulticastDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 3),
    _AhVIfRxMulticastDataFrames_Type()
)
ahVIfRxMulticastDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahVIfRxMulticastDataFrames.setStatus("current")
_AhVIfRxBroadcastDataFrames_Type = Counter32
_AhVIfRxBroadcastDataFrames_Object = MibTableColumn
ahVIfRxBroadcastDataFrames = _AhVIfRxBroadcastDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 4),
    _AhVIfRxBroadcastDataFrames_Type()
)
ahVIfRxBroadcastDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahVIfRxBroadcastDataFrames.setStatus("current")
_AhVIfRxErrorFrames_Type = Counter32
_AhVIfRxErrorFrames_Object = MibTableColumn
ahVIfRxErrorFrames = _AhVIfRxErrorFrames_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 5),
    _AhVIfRxErrorFrames_Type()
)
ahVIfRxErrorFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahVIfRxErrorFrames.setStatus("current")
_AhVIfRxDroppedFrames_Type = Counter32
_AhVIfRxDroppedFrames_Object = MibTableColumn
ahVIfRxDroppedFrames = _AhVIfRxDroppedFrames_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 6),
    _AhVIfRxDroppedFrames_Type()
)
ahVIfRxDroppedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahVIfRxDroppedFrames.setStatus("current")
_AhVIfTxDataFrames_Type = Counter32
_AhVIfTxDataFrames_Object = MibTableColumn
ahVIfTxDataFrames = _AhVIfTxDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 7),
    _AhVIfTxDataFrames_Type()
)
ahVIfTxDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahVIfTxDataFrames.setStatus("current")
_AhVIfTxUnicastDataFrames_Type = Counter32
_AhVIfTxUnicastDataFrames_Object = MibTableColumn
ahVIfTxUnicastDataFrames = _AhVIfTxUnicastDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 8),
    _AhVIfTxUnicastDataFrames_Type()
)
ahVIfTxUnicastDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahVIfTxUnicastDataFrames.setStatus("current")
_AhVIfTxMulticastDataFrames_Type = Counter32
_AhVIfTxMulticastDataFrames_Object = MibTableColumn
ahVIfTxMulticastDataFrames = _AhVIfTxMulticastDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 9),
    _AhVIfTxMulticastDataFrames_Type()
)
ahVIfTxMulticastDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahVIfTxMulticastDataFrames.setStatus("current")
_AhVIfTxBroadcastDataFrames_Type = Counter32
_AhVIfTxBroadcastDataFrames_Object = MibTableColumn
ahVIfTxBroadcastDataFrames = _AhVIfTxBroadcastDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 10),
    _AhVIfTxBroadcastDataFrames_Type()
)
ahVIfTxBroadcastDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahVIfTxBroadcastDataFrames.setStatus("current")
_AhVIfTxErrorFrames_Type = Counter32
_AhVIfTxErrorFrames_Object = MibTableColumn
ahVIfTxErrorFrames = _AhVIfTxErrorFrames_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 11),
    _AhVIfTxErrorFrames_Type()
)
ahVIfTxErrorFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahVIfTxErrorFrames.setStatus("current")
_AhVIfTxDroppedFrames_Type = Counter32
_AhVIfTxDroppedFrames_Object = MibTableColumn
ahVIfTxDroppedFrames = _AhVIfTxDroppedFrames_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 12),
    _AhVIfTxDroppedFrames_Type()
)
ahVIfTxDroppedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahVIfTxDroppedFrames.setStatus("current")
_AhVIfTxBeDataFrames_Type = Counter32
_AhVIfTxBeDataFrames_Object = MibTableColumn
ahVIfTxBeDataFrames = _AhVIfTxBeDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 13),
    _AhVIfTxBeDataFrames_Type()
)
ahVIfTxBeDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahVIfTxBeDataFrames.setStatus("current")
_AhVIfTxBgDataFrames_Type = Counter32
_AhVIfTxBgDataFrames_Object = MibTableColumn
ahVIfTxBgDataFrames = _AhVIfTxBgDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 14),
    _AhVIfTxBgDataFrames_Type()
)
ahVIfTxBgDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahVIfTxBgDataFrames.setStatus("current")
_AhVIfTxViDataFrames_Type = Counter32
_AhVIfTxViDataFrames_Object = MibTableColumn
ahVIfTxViDataFrames = _AhVIfTxViDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 15),
    _AhVIfTxViDataFrames_Type()
)
ahVIfTxViDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahVIfTxViDataFrames.setStatus("current")
_AhVIfTxVoDataFrames_Type = Counter32
_AhVIfTxVoDataFrames_Object = MibTableColumn
ahVIfTxVoDataFrames = _AhVIfTxVoDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 16),
    _AhVIfTxVoDataFrames_Type()
)
ahVIfTxVoDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahVIfTxVoDataFrames.setStatus("current")
_AhVifTxAirtime_Type = Counter64
_AhVifTxAirtime_Object = MibTableColumn
ahVifTxAirtime = _AhVifTxAirtime_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 17),
    _AhVifTxAirtime_Type()
)
ahVifTxAirtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahVifTxAirtime.setStatus("current")
_AhVifRxAirtime_Type = Counter64
_AhVifRxAirtime_Object = MibTableColumn
ahVifRxAirtime = _AhVifRxAirtime_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 4, 1, 18),
    _AhVifRxAirtime_Type()
)
ahVifRxAirtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahVifRxAirtime.setStatus("current")
_AhRadioAttributeTable_Object = MibTable
ahRadioAttributeTable = _AhRadioAttributeTable_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 5)
)
if mibBuilder.loadTexts:
    ahRadioAttributeTable.setStatus("current")
_AhRadioAttributeEntry_Object = MibTableRow
ahRadioAttributeEntry = _AhRadioAttributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 5, 1)
)
ahRadioAttributeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ahRadioAttributeEntry.setStatus("current")
_AhRadioChannel_Type = Integer32
_AhRadioChannel_Object = MibTableColumn
ahRadioChannel = _AhRadioChannel_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 5, 1, 1),
    _AhRadioChannel_Type()
)
ahRadioChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahRadioChannel.setStatus("current")
_AhRadioTxPower_Type = Integer32
_AhRadioTxPower_Object = MibTableColumn
ahRadioTxPower = _AhRadioTxPower_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 5, 1, 2),
    _AhRadioTxPower_Type()
)
ahRadioTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahRadioTxPower.setStatus("current")
_AhRadioNoiseFloor_Type = Integer32
_AhRadioNoiseFloor_Object = MibTableColumn
ahRadioNoiseFloor = _AhRadioNoiseFloor_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 2, 1, 5, 1, 3),
    _AhRadioNoiseFloor_Type()
)
ahRadioNoiseFloor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahRadioNoiseFloor.setStatus("current")
ifEntry.registerAugmentions(
    ("AH-INTERFACE-MIB",
     "ahXIfEntry")
)
ahXIfEntry.setIndexNames(*ifEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AH-INTERFACE-MIB",
    **{"AhAuthenticationMethod": AhAuthenticationMethod,
       "AhEncrytionMethod": AhEncrytionMethod,
       "ahInterface": ahInterface,
       "ahXIfTable": ahXIfTable,
       "ahXIfEntry": ahXIfEntry,
       "ahIfName": ahIfName,
       "ahSSIDName": ahSSIDName,
       "ahIfPromiscuous": ahIfPromiscuous,
       "ahIfType": ahIfType,
       "ahIfMode": ahIfMode,
       "ahIfConfMode": ahIfConfMode,
       "ahAssociationTable": ahAssociationTable,
       "ahAssociationEntry": ahAssociationEntry,
       "ahClientMac": ahClientMac,
       "ahClientIP": ahClientIP,
       "ahClientHostname": ahClientHostname,
       "ahClientRSSI": ahClientRSSI,
       "ahClientLinkUptime": ahClientLinkUptime,
       "ahClientCWPUsed": ahClientCWPUsed,
       "ahClientAuthMethod": ahClientAuthMethod,
       "ahClientEncryptionMethod": ahClientEncryptionMethod,
       "ahClientMACProtocol": ahClientMACProtocol,
       "ahClientSSID": ahClientSSID,
       "ahClientVLAN": ahClientVLAN,
       "ahClientUserProfId": ahClientUserProfId,
       "ahClientChannel": ahClientChannel,
       "ahClientLastTxRate": ahClientLastTxRate,
       "ahClientUsername": ahClientUsername,
       "ahClientRxDataFrames": ahClientRxDataFrames,
       "ahClientRxDataOctets": ahClientRxDataOctets,
       "ahClientRxMgtFrames": ahClientRxMgtFrames,
       "ahClientRxUnicastFrames": ahClientRxUnicastFrames,
       "ahClientRxMulticastFrames": ahClientRxMulticastFrames,
       "ahClientRxBroadcastFrames": ahClientRxBroadcastFrames,
       "ahClientRxMICFailures": ahClientRxMICFailures,
       "ahClientTxDataFrames": ahClientTxDataFrames,
       "ahClientTxMgtFrames": ahClientTxMgtFrames,
       "ahClientTxDataOctets": ahClientTxDataOctets,
       "ahClientTxUnicastFrames": ahClientTxUnicastFrames,
       "ahClientTxMulticastFrames": ahClientTxMulticastFrames,
       "ahClientTxBroadcastFrames": ahClientTxBroadcastFrames,
       "ahClientLastRxRate": ahClientLastRxRate,
       "ahClientTxBeDataFrames": ahClientTxBeDataFrames,
       "ahClientTxBgDataFrames": ahClientTxBgDataFrames,
       "ahClientTxViDataFrames": ahClientTxViDataFrames,
       "ahClientTxVoDataFrames": ahClientTxVoDataFrames,
       "ahClientTxAirtime": ahClientTxAirtime,
       "ahClientRxAirtime": ahClientRxAirtime,
       "ahClientAssociationTime": ahClientAssociationTime,
       "ahClientBSSID": ahClientBSSID,
       "ahRadioStatsTable": ahRadioStatsTable,
       "ahRadioStatsEntry": ahRadioStatsEntry,
       "ahRadioTxDataFrames": ahRadioTxDataFrames,
       "ahRadioTxUnicastDataFrames": ahRadioTxUnicastDataFrames,
       "ahRadioTxMulticastDataFrames": ahRadioTxMulticastDataFrames,
       "ahRadioTxBroadcastDataFrames": ahRadioTxBroadcastDataFrames,
       "ahRadioTxNonBeaconMgtFrames": ahRadioTxNonBeaconMgtFrames,
       "ahRadioTxBeaconFrames": ahRadioTxBeaconFrames,
       "ahRadioTxTotalRetries": ahRadioTxTotalRetries,
       "ahRadioTxTotalFramesDropped": ahRadioTxTotalFramesDropped,
       "ahRadioTxTotalFrameErrors": ahRadioTxTotalFrameErrors,
       "ahRadioTxFEForExcessiveHWRetries": ahRadioTxFEForExcessiveHWRetries,
       "ahRadioRxTotalDataFrames": ahRadioRxTotalDataFrames,
       "ahRadioRxUnicastDataFrames": ahRadioRxUnicastDataFrames,
       "ahRadioRxMulticastDataFrames": ahRadioRxMulticastDataFrames,
       "ahRadioRxBroadcastDataFrames": ahRadioRxBroadcastDataFrames,
       "ahRadioRxMgtFrames": ahRadioRxMgtFrames,
       "ahRadioRxTotalFrameDropped": ahRadioRxTotalFrameDropped,
       "ahRadioTxBeDataFrames": ahRadioTxBeDataFrames,
       "ahRadioTxBgDataFrames": ahRadioTxBgDataFrames,
       "ahRadioTxViDataFrames": ahRadioTxViDataFrames,
       "ahRadioTxVoDataFrames": ahRadioTxVoDataFrames,
       "ahRadioTXRTSFailures": ahRadioTXRTSFailures,
       "ahRadioTxAirtime": ahRadioTxAirtime,
       "ahRadioRxAirtime": ahRadioRxAirtime,
       "ahVIfStatsTable": ahVIfStatsTable,
       "ahVIfStatsEntry": ahVIfStatsEntry,
       "ahVIfRxDataFrames": ahVIfRxDataFrames,
       "ahVIfRxUnicastDataFrames": ahVIfRxUnicastDataFrames,
       "ahVIfRxMulticastDataFrames": ahVIfRxMulticastDataFrames,
       "ahVIfRxBroadcastDataFrames": ahVIfRxBroadcastDataFrames,
       "ahVIfRxErrorFrames": ahVIfRxErrorFrames,
       "ahVIfRxDroppedFrames": ahVIfRxDroppedFrames,
       "ahVIfTxDataFrames": ahVIfTxDataFrames,
       "ahVIfTxUnicastDataFrames": ahVIfTxUnicastDataFrames,
       "ahVIfTxMulticastDataFrames": ahVIfTxMulticastDataFrames,
       "ahVIfTxBroadcastDataFrames": ahVIfTxBroadcastDataFrames,
       "ahVIfTxErrorFrames": ahVIfTxErrorFrames,
       "ahVIfTxDroppedFrames": ahVIfTxDroppedFrames,
       "ahVIfTxBeDataFrames": ahVIfTxBeDataFrames,
       "ahVIfTxBgDataFrames": ahVIfTxBgDataFrames,
       "ahVIfTxViDataFrames": ahVIfTxViDataFrames,
       "ahVIfTxVoDataFrames": ahVIfTxVoDataFrames,
       "ahVifTxAirtime": ahVifTxAirtime,
       "ahVifRxAirtime": ahVifRxAirtime,
       "ahRadioAttributeTable": ahRadioAttributeTable,
       "ahRadioAttributeEntry": ahRadioAttributeEntry,
       "ahRadioChannel": ahRadioChannel,
       "ahRadioTxPower": ahRadioTxPower,
       "ahRadioNoiseFloor": ahRadioNoiseFloor}
)
