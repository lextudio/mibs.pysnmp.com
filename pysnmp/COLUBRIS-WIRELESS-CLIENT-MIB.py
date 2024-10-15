# SNMP MIB module (COLUBRIS-WIRELESS-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/COLUBRIS-WIRELESS-CLIENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:16:32 2024
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

(colubrisMgmtV2,) = mibBuilder.importSymbols(
    "COLUBRIS-SMI",
    "colubrisMgmtV2")

(systemSerialNumber,) = mibBuilder.importSymbols(
    "COLUBRIS-SYSTEM-MIB",
    "systemSerialNumber")

(ColubrisNotificationEnable,
 ColubrisSSID) = mibBuilder.importSymbols(
    "COLUBRIS-TC",
    "ColubrisNotificationEnable",
    "ColubrisSSID")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

colubrisWirelessClientMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 20)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ColubrisWirelessClientMIBObjects_ObjectIdentity = ObjectIdentity
colubrisWirelessClientMIBObjects = _ColubrisWirelessClientMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 20, 1)
)
_ColubrisWirelessClientInfo_ObjectIdentity = ObjectIdentity
colubrisWirelessClientInfo = _ColubrisWirelessClientInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 1)
)


class _ColubrisWirelessClientState_Type(Integer32):
    """Custom type colubrisWirelessClientState based on Integer32"""
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
        *(("associated", 5),
          ("associating", 4),
          ("authenticating", 3),
          ("disconnected", 1),
          ("scanning", 2))
    )


_ColubrisWirelessClientState_Type.__name__ = "Integer32"
_ColubrisWirelessClientState_Object = MibScalar
colubrisWirelessClientState = _ColubrisWirelessClientState_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 1, 1),
    _ColubrisWirelessClientState_Type()
)
colubrisWirelessClientState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colubrisWirelessClientState.setStatus("current")
_ColubrisWirelessClientSSID_Type = ColubrisSSID
_ColubrisWirelessClientSSID_Object = MibScalar
colubrisWirelessClientSSID = _ColubrisWirelessClientSSID_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 1, 2),
    _ColubrisWirelessClientSSID_Type()
)
colubrisWirelessClientSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colubrisWirelessClientSSID.setStatus("current")
_ColubrisWirelessClientBSSID_Type = MacAddress
_ColubrisWirelessClientBSSID_Object = MibScalar
colubrisWirelessClientBSSID = _ColubrisWirelessClientBSSID_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 1, 3),
    _ColubrisWirelessClientBSSID_Type()
)
colubrisWirelessClientBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colubrisWirelessClientBSSID.setStatus("current")
_ColubrisWirelessClientSignalLevel_Type = Integer32
_ColubrisWirelessClientSignalLevel_Object = MibScalar
colubrisWirelessClientSignalLevel = _ColubrisWirelessClientSignalLevel_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 1, 4),
    _ColubrisWirelessClientSignalLevel_Type()
)
colubrisWirelessClientSignalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colubrisWirelessClientSignalLevel.setStatus("current")
_ColubrisWirelessClientNoiseLevel_Type = Integer32
_ColubrisWirelessClientNoiseLevel_Object = MibScalar
colubrisWirelessClientNoiseLevel = _ColubrisWirelessClientNoiseLevel_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 1, 5),
    _ColubrisWirelessClientNoiseLevel_Type()
)
colubrisWirelessClientNoiseLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colubrisWirelessClientNoiseLevel.setStatus("current")
_ColubrisWirelessClientSNR_Type = Integer32
_ColubrisWirelessClientSNR_Object = MibScalar
colubrisWirelessClientSNR = _ColubrisWirelessClientSNR_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 1, 6),
    _ColubrisWirelessClientSNR_Type()
)
colubrisWirelessClientSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colubrisWirelessClientSNR.setStatus("current")


class _ColubrisWirelessClientConnectionNotificationEnabled_Type(ColubrisNotificationEnable):
    """Custom type colubrisWirelessClientConnectionNotificationEnabled based on ColubrisNotificationEnable"""


_ColubrisWirelessClientConnectionNotificationEnabled_Object = MibScalar
colubrisWirelessClientConnectionNotificationEnabled = _ColubrisWirelessClientConnectionNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 1, 7),
    _ColubrisWirelessClientConnectionNotificationEnabled_Type()
)
colubrisWirelessClientConnectionNotificationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    colubrisWirelessClientConnectionNotificationEnabled.setStatus("current")
_ColubrisWirelessClientConnectTime_Type = Counter32
_ColubrisWirelessClientConnectTime_Object = MibScalar
colubrisWirelessClientConnectTime = _ColubrisWirelessClientConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 1, 8),
    _ColubrisWirelessClientConnectTime_Type()
)
colubrisWirelessClientConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colubrisWirelessClientConnectTime.setStatus("current")
if mibBuilder.loadTexts:
    colubrisWirelessClientConnectTime.setUnits("seconds")


class _ColubrisWirelessClientAuthorizedState_Type(Integer32):
    """Custom type colubrisWirelessClientAuthorizedState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("authorized", 2),
          ("notAuthorized", 1))
    )


_ColubrisWirelessClientAuthorizedState_Type.__name__ = "Integer32"
_ColubrisWirelessClientAuthorizedState_Object = MibScalar
colubrisWirelessClientAuthorizedState = _ColubrisWirelessClientAuthorizedState_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 1, 9),
    _ColubrisWirelessClientAuthorizedState_Type()
)
colubrisWirelessClientAuthorizedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colubrisWirelessClientAuthorizedState.setStatus("current")


class _ColubrisWirelessClientEncryptionStatus_Type(Integer32):
    """Custom type colubrisWirelessClientEncryptionStatus based on Integer32"""
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
        *(("aes", 4),
          ("aesTkip", 5),
          ("none", 1),
          ("tkip", 3),
          ("wep", 2))
    )


_ColubrisWirelessClientEncryptionStatus_Type.__name__ = "Integer32"
_ColubrisWirelessClientEncryptionStatus_Object = MibScalar
colubrisWirelessClientEncryptionStatus = _ColubrisWirelessClientEncryptionStatus_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 1, 10),
    _ColubrisWirelessClientEncryptionStatus_Type()
)
colubrisWirelessClientEncryptionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colubrisWirelessClientEncryptionStatus.setStatus("current")
_ColubrisWirelessClientTransmitRate_Type = Unsigned32
_ColubrisWirelessClientTransmitRate_Object = MibScalar
colubrisWirelessClientTransmitRate = _ColubrisWirelessClientTransmitRate_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 1, 11),
    _ColubrisWirelessClientTransmitRate_Type()
)
colubrisWirelessClientTransmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colubrisWirelessClientTransmitRate.setStatus("current")
_ColubrisWirelessClientReceiveRate_Type = Unsigned32
_ColubrisWirelessClientReceiveRate_Object = MibScalar
colubrisWirelessClientReceiveRate = _ColubrisWirelessClientReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 1, 12),
    _ColubrisWirelessClientReceiveRate_Type()
)
colubrisWirelessClientReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colubrisWirelessClientReceiveRate.setStatus("current")
_ColubrisWirelessClientStats_ObjectIdentity = ObjectIdentity
colubrisWirelessClientStats = _ColubrisWirelessClientStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 2)
)
_ColubrisWirelessClientInPkts_Type = Counter32
_ColubrisWirelessClientInPkts_Object = MibScalar
colubrisWirelessClientInPkts = _ColubrisWirelessClientInPkts_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 2, 1),
    _ColubrisWirelessClientInPkts_Type()
)
colubrisWirelessClientInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colubrisWirelessClientInPkts.setStatus("current")
_ColubrisWirelessClientOutPkts_Type = Counter32
_ColubrisWirelessClientOutPkts_Object = MibScalar
colubrisWirelessClientOutPkts = _ColubrisWirelessClientOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 2, 2),
    _ColubrisWirelessClientOutPkts_Type()
)
colubrisWirelessClientOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colubrisWirelessClientOutPkts.setStatus("current")
_ColubrisWirelessClientInOctets_Type = Counter64
_ColubrisWirelessClientInOctets_Object = MibScalar
colubrisWirelessClientInOctets = _ColubrisWirelessClientInOctets_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 2, 3),
    _ColubrisWirelessClientInOctets_Type()
)
colubrisWirelessClientInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colubrisWirelessClientInOctets.setStatus("current")
_ColubrisWirelessClientOutOctets_Type = Counter64
_ColubrisWirelessClientOutOctets_Object = MibScalar
colubrisWirelessClientOutOctets = _ColubrisWirelessClientOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 2, 4),
    _ColubrisWirelessClientOutOctets_Type()
)
colubrisWirelessClientOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colubrisWirelessClientOutOctets.setStatus("current")
_ColubrisWirelessClientPktsTxRate1_Type = Counter32
_ColubrisWirelessClientPktsTxRate1_Object = MibScalar
colubrisWirelessClientPktsTxRate1 = _ColubrisWirelessClientPktsTxRate1_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 2, 5),
    _ColubrisWirelessClientPktsTxRate1_Type()
)
colubrisWirelessClientPktsTxRate1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colubrisWirelessClientPktsTxRate1.setStatus("current")
_ColubrisWirelessClientPktsTxRate2_Type = Counter32
_ColubrisWirelessClientPktsTxRate2_Object = MibScalar
colubrisWirelessClientPktsTxRate2 = _ColubrisWirelessClientPktsTxRate2_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 2, 6),
    _ColubrisWirelessClientPktsTxRate2_Type()
)
colubrisWirelessClientPktsTxRate2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colubrisWirelessClientPktsTxRate2.setStatus("current")
_ColubrisWirelessClientPktsTxRate5dot5_Type = Counter32
_ColubrisWirelessClientPktsTxRate5dot5_Object = MibScalar
colubrisWirelessClientPktsTxRate5dot5 = _ColubrisWirelessClientPktsTxRate5dot5_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 2, 7),
    _ColubrisWirelessClientPktsTxRate5dot5_Type()
)
colubrisWirelessClientPktsTxRate5dot5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colubrisWirelessClientPktsTxRate5dot5.setStatus("current")
_ColubrisWirelessClientPktsTxRate11_Type = Counter32
_ColubrisWirelessClientPktsTxRate11_Object = MibScalar
colubrisWirelessClientPktsTxRate11 = _ColubrisWirelessClientPktsTxRate11_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 2, 8),
    _ColubrisWirelessClientPktsTxRate11_Type()
)
colubrisWirelessClientPktsTxRate11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colubrisWirelessClientPktsTxRate11.setStatus("current")
_ColubrisWirelessClientPktsTxRate6_Type = Counter32
_ColubrisWirelessClientPktsTxRate6_Object = MibScalar
colubrisWirelessClientPktsTxRate6 = _ColubrisWirelessClientPktsTxRate6_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 2, 9),
    _ColubrisWirelessClientPktsTxRate6_Type()
)
colubrisWirelessClientPktsTxRate6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colubrisWirelessClientPktsTxRate6.setStatus("current")
_ColubrisWirelessClientPktsTxRate9_Type = Counter32
_ColubrisWirelessClientPktsTxRate9_Object = MibScalar
colubrisWirelessClientPktsTxRate9 = _ColubrisWirelessClientPktsTxRate9_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 2, 10),
    _ColubrisWirelessClientPktsTxRate9_Type()
)
colubrisWirelessClientPktsTxRate9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colubrisWirelessClientPktsTxRate9.setStatus("current")
_ColubrisWirelessClientPktsTxRate12_Type = Counter32
_ColubrisWirelessClientPktsTxRate12_Object = MibScalar
colubrisWirelessClientPktsTxRate12 = _ColubrisWirelessClientPktsTxRate12_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 2, 11),
    _ColubrisWirelessClientPktsTxRate12_Type()
)
colubrisWirelessClientPktsTxRate12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colubrisWirelessClientPktsTxRate12.setStatus("current")
_ColubrisWirelessClientPktsTxRate18_Type = Counter32
_ColubrisWirelessClientPktsTxRate18_Object = MibScalar
colubrisWirelessClientPktsTxRate18 = _ColubrisWirelessClientPktsTxRate18_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 2, 12),
    _ColubrisWirelessClientPktsTxRate18_Type()
)
colubrisWirelessClientPktsTxRate18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colubrisWirelessClientPktsTxRate18.setStatus("current")
_ColubrisWirelessClientPktsTxRate24_Type = Counter32
_ColubrisWirelessClientPktsTxRate24_Object = MibScalar
colubrisWirelessClientPktsTxRate24 = _ColubrisWirelessClientPktsTxRate24_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 2, 13),
    _ColubrisWirelessClientPktsTxRate24_Type()
)
colubrisWirelessClientPktsTxRate24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colubrisWirelessClientPktsTxRate24.setStatus("current")
_ColubrisWirelessClientPktsTxRate36_Type = Counter32
_ColubrisWirelessClientPktsTxRate36_Object = MibScalar
colubrisWirelessClientPktsTxRate36 = _ColubrisWirelessClientPktsTxRate36_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 2, 14),
    _ColubrisWirelessClientPktsTxRate36_Type()
)
colubrisWirelessClientPktsTxRate36.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colubrisWirelessClientPktsTxRate36.setStatus("current")
_ColubrisWirelessClientPktsTxRate48_Type = Counter32
_ColubrisWirelessClientPktsTxRate48_Object = MibScalar
colubrisWirelessClientPktsTxRate48 = _ColubrisWirelessClientPktsTxRate48_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 2, 15),
    _ColubrisWirelessClientPktsTxRate48_Type()
)
colubrisWirelessClientPktsTxRate48.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colubrisWirelessClientPktsTxRate48.setStatus("current")
_ColubrisWirelessClientPktsTxRate54_Type = Counter32
_ColubrisWirelessClientPktsTxRate54_Object = MibScalar
colubrisWirelessClientPktsTxRate54 = _ColubrisWirelessClientPktsTxRate54_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 2, 16),
    _ColubrisWirelessClientPktsTxRate54_Type()
)
colubrisWirelessClientPktsTxRate54.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colubrisWirelessClientPktsTxRate54.setStatus("current")
_ColubrisWirelessClientPktsRxRate1_Type = Counter32
_ColubrisWirelessClientPktsRxRate1_Object = MibScalar
colubrisWirelessClientPktsRxRate1 = _ColubrisWirelessClientPktsRxRate1_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 2, 17),
    _ColubrisWirelessClientPktsRxRate1_Type()
)
colubrisWirelessClientPktsRxRate1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colubrisWirelessClientPktsRxRate1.setStatus("current")
_ColubrisWirelessClientPktsRxRate2_Type = Counter32
_ColubrisWirelessClientPktsRxRate2_Object = MibScalar
colubrisWirelessClientPktsRxRate2 = _ColubrisWirelessClientPktsRxRate2_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 2, 18),
    _ColubrisWirelessClientPktsRxRate2_Type()
)
colubrisWirelessClientPktsRxRate2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colubrisWirelessClientPktsRxRate2.setStatus("current")
_ColubrisWirelessClientPktsRxRate5dot5_Type = Counter32
_ColubrisWirelessClientPktsRxRate5dot5_Object = MibScalar
colubrisWirelessClientPktsRxRate5dot5 = _ColubrisWirelessClientPktsRxRate5dot5_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 2, 19),
    _ColubrisWirelessClientPktsRxRate5dot5_Type()
)
colubrisWirelessClientPktsRxRate5dot5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colubrisWirelessClientPktsRxRate5dot5.setStatus("current")
_ColubrisWirelessClientPktsRxRate11_Type = Counter32
_ColubrisWirelessClientPktsRxRate11_Object = MibScalar
colubrisWirelessClientPktsRxRate11 = _ColubrisWirelessClientPktsRxRate11_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 2, 20),
    _ColubrisWirelessClientPktsRxRate11_Type()
)
colubrisWirelessClientPktsRxRate11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colubrisWirelessClientPktsRxRate11.setStatus("current")
_ColubrisWirelessClientPktsRxRate6_Type = Counter32
_ColubrisWirelessClientPktsRxRate6_Object = MibScalar
colubrisWirelessClientPktsRxRate6 = _ColubrisWirelessClientPktsRxRate6_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 2, 21),
    _ColubrisWirelessClientPktsRxRate6_Type()
)
colubrisWirelessClientPktsRxRate6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colubrisWirelessClientPktsRxRate6.setStatus("current")
_ColubrisWirelessClientPktsRxRate9_Type = Counter32
_ColubrisWirelessClientPktsRxRate9_Object = MibScalar
colubrisWirelessClientPktsRxRate9 = _ColubrisWirelessClientPktsRxRate9_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 2, 22),
    _ColubrisWirelessClientPktsRxRate9_Type()
)
colubrisWirelessClientPktsRxRate9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colubrisWirelessClientPktsRxRate9.setStatus("current")
_ColubrisWirelessClientPktsRxRate12_Type = Counter32
_ColubrisWirelessClientPktsRxRate12_Object = MibScalar
colubrisWirelessClientPktsRxRate12 = _ColubrisWirelessClientPktsRxRate12_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 2, 23),
    _ColubrisWirelessClientPktsRxRate12_Type()
)
colubrisWirelessClientPktsRxRate12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colubrisWirelessClientPktsRxRate12.setStatus("current")
_ColubrisWirelessClientPktsRxRate18_Type = Counter32
_ColubrisWirelessClientPktsRxRate18_Object = MibScalar
colubrisWirelessClientPktsRxRate18 = _ColubrisWirelessClientPktsRxRate18_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 2, 24),
    _ColubrisWirelessClientPktsRxRate18_Type()
)
colubrisWirelessClientPktsRxRate18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colubrisWirelessClientPktsRxRate18.setStatus("current")
_ColubrisWirelessClientPktsRxRate24_Type = Counter32
_ColubrisWirelessClientPktsRxRate24_Object = MibScalar
colubrisWirelessClientPktsRxRate24 = _ColubrisWirelessClientPktsRxRate24_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 2, 25),
    _ColubrisWirelessClientPktsRxRate24_Type()
)
colubrisWirelessClientPktsRxRate24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colubrisWirelessClientPktsRxRate24.setStatus("current")
_ColubrisWirelessClientPktsRxRate36_Type = Counter32
_ColubrisWirelessClientPktsRxRate36_Object = MibScalar
colubrisWirelessClientPktsRxRate36 = _ColubrisWirelessClientPktsRxRate36_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 2, 26),
    _ColubrisWirelessClientPktsRxRate36_Type()
)
colubrisWirelessClientPktsRxRate36.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colubrisWirelessClientPktsRxRate36.setStatus("current")
_ColubrisWirelessClientPktsRxRate48_Type = Counter32
_ColubrisWirelessClientPktsRxRate48_Object = MibScalar
colubrisWirelessClientPktsRxRate48 = _ColubrisWirelessClientPktsRxRate48_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 2, 27),
    _ColubrisWirelessClientPktsRxRate48_Type()
)
colubrisWirelessClientPktsRxRate48.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colubrisWirelessClientPktsRxRate48.setStatus("current")
_ColubrisWirelessClientPktsRxRate54_Type = Counter32
_ColubrisWirelessClientPktsRxRate54_Object = MibScalar
colubrisWirelessClientPktsRxRate54 = _ColubrisWirelessClientPktsRxRate54_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 20, 1, 2, 28),
    _ColubrisWirelessClientPktsRxRate54_Type()
)
colubrisWirelessClientPktsRxRate54.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colubrisWirelessClientPktsRxRate54.setStatus("current")
_ColubrisWirelessClientMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
colubrisWirelessClientMIBNotificationPrefix = _ColubrisWirelessClientMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 20, 2)
)
_ColubrisWirelessClientMIBNotifications_ObjectIdentity = ObjectIdentity
colubrisWirelessClientMIBNotifications = _ColubrisWirelessClientMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 20, 2, 0)
)
_ColubrisWirelessClientMIBConformance_ObjectIdentity = ObjectIdentity
colubrisWirelessClientMIBConformance = _ColubrisWirelessClientMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 20, 3)
)
_ColubrisWirelessClientMIBCompliances_ObjectIdentity = ObjectIdentity
colubrisWirelessClientMIBCompliances = _ColubrisWirelessClientMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 20, 3, 1)
)
_ColubrisWirelessClientMIBGroups_ObjectIdentity = ObjectIdentity
colubrisWirelessClientMIBGroups = _ColubrisWirelessClientMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 20, 3, 2)
)

# Managed Objects groups

colubrisWirelessClientMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 20, 3, 2, 1)
)
colubrisWirelessClientMIBGroup.setObjects(
      *(("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientState"),
        ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientSSID"),
        ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientBSSID"),
        ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientSignalLevel"),
        ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientNoiseLevel"),
        ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientSNR"),
        ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientConnectionNotificationEnabled"),
        ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientTransmitRate"),
        ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientReceiveRate"),
        ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientConnectTime"),
        ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientAuthorizedState"),
        ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientEncryptionStatus"))
)
if mibBuilder.loadTexts:
    colubrisWirelessClientMIBGroup.setStatus("current")

colubrisWirelessClientMIBGroupCounters = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 20, 3, 2, 3)
)
colubrisWirelessClientMIBGroupCounters.setObjects(
      *(("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientInPkts"),
        ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientOutPkts"),
        ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientInOctets"),
        ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientOutOctets"),
        ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientPktsTxRate1"),
        ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientPktsTxRate2"),
        ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientPktsTxRate5dot5"),
        ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientPktsTxRate11"),
        ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientPktsTxRate6"),
        ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientPktsTxRate9"),
        ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientPktsTxRate12"),
        ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientPktsTxRate18"),
        ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientPktsTxRate24"),
        ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientPktsTxRate36"),
        ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientPktsTxRate48"),
        ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientPktsTxRate54"),
        ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientPktsRxRate1"),
        ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientPktsRxRate2"),
        ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientPktsRxRate5dot5"),
        ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientPktsRxRate11"),
        ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientPktsRxRate6"),
        ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientPktsRxRate9"),
        ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientPktsRxRate12"),
        ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientPktsRxRate18"),
        ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientPktsRxRate24"),
        ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientPktsRxRate36"),
        ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientPktsRxRate48"),
        ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientPktsRxRate54"))
)
if mibBuilder.loadTexts:
    colubrisWirelessClientMIBGroupCounters.setStatus("current")


# Notification objects

colubrisWirelessClientConnectionNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 8744, 5, 20, 2, 0, 1)
)
colubrisWirelessClientConnectionNotification.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("COLUBRIS-SYSTEM-MIB", "systemSerialNumber"),
        ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientSSID"),
        ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientBSSID"))
)
if mibBuilder.loadTexts:
    colubrisWirelessClientConnectionNotification.setStatus(
        "current"
    )


# Notifications groups

colubrisWirelessClientNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 20, 3, 2, 2)
)
colubrisWirelessClientNotificationGroup.setObjects(
    ("COLUBRIS-WIRELESS-CLIENT-MIB", "colubrisWirelessClientConnectionNotification")
)
if mibBuilder.loadTexts:
    colubrisWirelessClientNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

colubrisWirelessClientMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8744, 5, 20, 3, 1, 1)
)
if mibBuilder.loadTexts:
    colubrisWirelessClientMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "COLUBRIS-WIRELESS-CLIENT-MIB",
    **{"colubrisWirelessClientMIB": colubrisWirelessClientMIB,
       "colubrisWirelessClientMIBObjects": colubrisWirelessClientMIBObjects,
       "colubrisWirelessClientInfo": colubrisWirelessClientInfo,
       "colubrisWirelessClientState": colubrisWirelessClientState,
       "colubrisWirelessClientSSID": colubrisWirelessClientSSID,
       "colubrisWirelessClientBSSID": colubrisWirelessClientBSSID,
       "colubrisWirelessClientSignalLevel": colubrisWirelessClientSignalLevel,
       "colubrisWirelessClientNoiseLevel": colubrisWirelessClientNoiseLevel,
       "colubrisWirelessClientSNR": colubrisWirelessClientSNR,
       "colubrisWirelessClientConnectionNotificationEnabled": colubrisWirelessClientConnectionNotificationEnabled,
       "colubrisWirelessClientConnectTime": colubrisWirelessClientConnectTime,
       "colubrisWirelessClientAuthorizedState": colubrisWirelessClientAuthorizedState,
       "colubrisWirelessClientEncryptionStatus": colubrisWirelessClientEncryptionStatus,
       "colubrisWirelessClientTransmitRate": colubrisWirelessClientTransmitRate,
       "colubrisWirelessClientReceiveRate": colubrisWirelessClientReceiveRate,
       "colubrisWirelessClientStats": colubrisWirelessClientStats,
       "colubrisWirelessClientInPkts": colubrisWirelessClientInPkts,
       "colubrisWirelessClientOutPkts": colubrisWirelessClientOutPkts,
       "colubrisWirelessClientInOctets": colubrisWirelessClientInOctets,
       "colubrisWirelessClientOutOctets": colubrisWirelessClientOutOctets,
       "colubrisWirelessClientPktsTxRate1": colubrisWirelessClientPktsTxRate1,
       "colubrisWirelessClientPktsTxRate2": colubrisWirelessClientPktsTxRate2,
       "colubrisWirelessClientPktsTxRate5dot5": colubrisWirelessClientPktsTxRate5dot5,
       "colubrisWirelessClientPktsTxRate11": colubrisWirelessClientPktsTxRate11,
       "colubrisWirelessClientPktsTxRate6": colubrisWirelessClientPktsTxRate6,
       "colubrisWirelessClientPktsTxRate9": colubrisWirelessClientPktsTxRate9,
       "colubrisWirelessClientPktsTxRate12": colubrisWirelessClientPktsTxRate12,
       "colubrisWirelessClientPktsTxRate18": colubrisWirelessClientPktsTxRate18,
       "colubrisWirelessClientPktsTxRate24": colubrisWirelessClientPktsTxRate24,
       "colubrisWirelessClientPktsTxRate36": colubrisWirelessClientPktsTxRate36,
       "colubrisWirelessClientPktsTxRate48": colubrisWirelessClientPktsTxRate48,
       "colubrisWirelessClientPktsTxRate54": colubrisWirelessClientPktsTxRate54,
       "colubrisWirelessClientPktsRxRate1": colubrisWirelessClientPktsRxRate1,
       "colubrisWirelessClientPktsRxRate2": colubrisWirelessClientPktsRxRate2,
       "colubrisWirelessClientPktsRxRate5dot5": colubrisWirelessClientPktsRxRate5dot5,
       "colubrisWirelessClientPktsRxRate11": colubrisWirelessClientPktsRxRate11,
       "colubrisWirelessClientPktsRxRate6": colubrisWirelessClientPktsRxRate6,
       "colubrisWirelessClientPktsRxRate9": colubrisWirelessClientPktsRxRate9,
       "colubrisWirelessClientPktsRxRate12": colubrisWirelessClientPktsRxRate12,
       "colubrisWirelessClientPktsRxRate18": colubrisWirelessClientPktsRxRate18,
       "colubrisWirelessClientPktsRxRate24": colubrisWirelessClientPktsRxRate24,
       "colubrisWirelessClientPktsRxRate36": colubrisWirelessClientPktsRxRate36,
       "colubrisWirelessClientPktsRxRate48": colubrisWirelessClientPktsRxRate48,
       "colubrisWirelessClientPktsRxRate54": colubrisWirelessClientPktsRxRate54,
       "colubrisWirelessClientMIBNotificationPrefix": colubrisWirelessClientMIBNotificationPrefix,
       "colubrisWirelessClientMIBNotifications": colubrisWirelessClientMIBNotifications,
       "colubrisWirelessClientConnectionNotification": colubrisWirelessClientConnectionNotification,
       "colubrisWirelessClientMIBConformance": colubrisWirelessClientMIBConformance,
       "colubrisWirelessClientMIBCompliances": colubrisWirelessClientMIBCompliances,
       "colubrisWirelessClientMIBCompliance": colubrisWirelessClientMIBCompliance,
       "colubrisWirelessClientMIBGroups": colubrisWirelessClientMIBGroups,
       "colubrisWirelessClientMIBGroup": colubrisWirelessClientMIBGroup,
       "colubrisWirelessClientNotificationGroup": colubrisWirelessClientNotificationGroup,
       "colubrisWirelessClientMIBGroupCounters": colubrisWirelessClientMIBGroupCounters}
)
