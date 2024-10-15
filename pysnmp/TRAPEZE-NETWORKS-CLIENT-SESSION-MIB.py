# SNMP MIB module (TRAPEZE-NETWORKS-CLIENT-SESSION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TRAPEZE-NETWORKS-CLIENT-SESSION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:07:30 2024
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TimeStamp")

(TrpzAccessType,
 TrpzApNum,
 TrpzApSerialNum,
 TrpzRadioNum,
 TrpzRadioRate,
 TrpzRssi) = mibBuilder.importSymbols(
    "TRAPEZE-NETWORKS-AP-TC",
    "TrpzAccessType",
    "TrpzApNum",
    "TrpzApSerialNum",
    "TrpzRadioNum",
    "TrpzRadioRate",
    "TrpzRssi")

(TrpzPhysPortNumberOrZero,) = mibBuilder.importSymbols(
    "TRAPEZE-NETWORKS-BASIC-TC",
    "TrpzPhysPortNumberOrZero")

(TrpzClientAccessMode,
 TrpzClientAuthenProtocolType,
 TrpzClientDeviceGroupName,
 TrpzClientDeviceProfileName,
 TrpzClientDeviceType,
 TrpzClientSessionState,
 TrpzUserAccessType) = mibBuilder.importSymbols(
    "TRAPEZE-NETWORKS-CLIENT-SESSION-TC",
    "TrpzClientAccessMode",
    "TrpzClientAuthenProtocolType",
    "TrpzClientDeviceGroupName",
    "TrpzClientDeviceProfileName",
    "TrpzClientDeviceType",
    "TrpzClientSessionState",
    "TrpzUserAccessType")

(trpzMibs,) = mibBuilder.importSymbols(
    "TRAPEZE-NETWORKS-ROOT-MIB",
    "trpzMibs")


# MODULE-IDENTITY

trpzClientSessionMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4)
)
trpzClientSessionMib.setRevisions(
        ("2012-04-20 01:12",
         "2011-12-06 01:10",
         "2011-05-18 01:00",
         "2008-10-23 00:56",
         "2008-05-23 00:55",
         "2007-11-01 00:54",
         "2007-10-09 00:51",
         "2006-11-16 00:43",
         "2006-10-17 00:42",
         "2006-09-26 00:32",
         "2006-07-29 00:21",
         "2006-06-06 00:10",
         "2006-03-30 00:08")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TrpzEncryptionType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("aesCcm", 2),
          ("aesOcb", 3),
          ("none", 1),
          ("staticWep", 7),
          ("tkip", 4),
          ("wep104", 5),
          ("wep40", 6))
    )



class TrpzAuthMethod(Integer32, TextualConvention):
    status = "obsolete"
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
              14,
              18,
              22,
              26,
              27,
              34,
              255)
        )
    )
    namedValues = NamedValues(
        *(("eapExt", 34),
          ("identity", 2),
          ("leap", 18),
          ("md5", 5),
          ("msChapv2", 27),
          ("nak", 4),
          ("none", 1),
          ("notification", 3),
          ("otp", 6),
          ("passThru", 255),
          ("peap", 26),
          ("tls", 14),
          ("tokenCard", 7),
          ("ttls", 22))
    )



class TrpzSessState(Integer32, TextualConvention):
    status = "deprecated"
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
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("active", 13),
          ("activePortal", 14),
          ("assocAndAuth", 4),
          ("assocReqAndAuth", 3),
          ("authorized", 12),
          ("authorizing", 11),
          ("deassociated", 15),
          ("enforceSoda", 21),
          ("free", 20),
          ("initializing", 2),
          ("invalid", 1),
          ("killing", 19),
          ("roamedAway", 18),
          ("roamingAway", 16),
          ("updatedToRoam", 17),
          ("webLoginPh1", 6),
          ("webLoginPh1B", 7),
          ("webLoginPh1F", 8),
          ("webLoginPh2", 9),
          ("webPortalLogin", 10),
          ("wired", 5))
    )



# MIB Managed Objects in the order of their OIDs

_TrpzClientSessionObjects_ObjectIdentity = ObjectIdentity
trpzClientSessionObjects = _TrpzClientSessionObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1)
)
_TrpzClientSessionDataObjects_ObjectIdentity = ObjectIdentity
trpzClientSessionDataObjects = _TrpzClientSessionDataObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1)
)
_TrpzClSessClientSessionTable_Object = MibTable
trpzClSessClientSessionTable = _TrpzClSessClientSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    trpzClSessClientSessionTable.setStatus("current")
_TrpzClSessClientSessionEntry_Object = MibTableRow
trpzClSessClientSessionEntry = _TrpzClSessClientSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 1, 1)
)
trpzClSessClientSessionEntry.setIndexNames(
    (0, "TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessMacAddress"),
)
if mibBuilder.loadTexts:
    trpzClSessClientSessionEntry.setStatus("current")
_TrpzClSessClientSessMacAddress_Type = MacAddress
_TrpzClSessClientSessMacAddress_Object = MibTableColumn
trpzClSessClientSessMacAddress = _TrpzClSessClientSessMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 1, 1, 1),
    _TrpzClSessClientSessMacAddress_Type()
)
trpzClSessClientSessMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzClSessClientSessMacAddress.setStatus("current")


class _TrpzClSessClientSessSessionId_Type(DisplayString):
    """Custom type trpzClSessClientSessSessionId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_TrpzClSessClientSessSessionId_Type.__name__ = "DisplayString"
_TrpzClSessClientSessSessionId_Object = MibTableColumn
trpzClSessClientSessSessionId = _TrpzClSessClientSessSessionId_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 1, 1, 2),
    _TrpzClSessClientSessSessionId_Type()
)
trpzClSessClientSessSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzClSessClientSessSessionId.setStatus("current")


class _TrpzClSessClientSessUsername_Type(DisplayString):
    """Custom type trpzClSessClientSessUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_TrpzClSessClientSessUsername_Type.__name__ = "DisplayString"
_TrpzClSessClientSessUsername_Object = MibTableColumn
trpzClSessClientSessUsername = _TrpzClSessClientSessUsername_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 1, 1, 3),
    _TrpzClSessClientSessUsername_Type()
)
trpzClSessClientSessUsername.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzClSessClientSessUsername.setStatus("current")
_TrpzClSessClientSessIpAddress_Type = IpAddress
_TrpzClSessClientSessIpAddress_Object = MibTableColumn
trpzClSessClientSessIpAddress = _TrpzClSessClientSessIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 1, 1, 4),
    _TrpzClSessClientSessIpAddress_Type()
)
trpzClSessClientSessIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzClSessClientSessIpAddress.setStatus("current")
_TrpzClSessClientSessEncryptionType_Type = TrpzEncryptionType
_TrpzClSessClientSessEncryptionType_Object = MibTableColumn
trpzClSessClientSessEncryptionType = _TrpzClSessClientSessEncryptionType_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 1, 1, 5),
    _TrpzClSessClientSessEncryptionType_Type()
)
trpzClSessClientSessEncryptionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzClSessClientSessEncryptionType.setStatus("current")


class _TrpzClSessClientSessVlan_Type(DisplayString):
    """Custom type trpzClSessClientSessVlan based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_TrpzClSessClientSessVlan_Type.__name__ = "DisplayString"
_TrpzClSessClientSessVlan_Object = MibTableColumn
trpzClSessClientSessVlan = _TrpzClSessClientSessVlan_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 1, 1, 6),
    _TrpzClSessClientSessVlan_Type()
)
trpzClSessClientSessVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzClSessClientSessVlan.setStatus("current")
_TrpzClSessClientSessApSerialNum_Type = TrpzApSerialNum
_TrpzClSessClientSessApSerialNum_Object = MibTableColumn
trpzClSessClientSessApSerialNum = _TrpzClSessClientSessApSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 1, 1, 7),
    _TrpzClSessClientSessApSerialNum_Type()
)
trpzClSessClientSessApSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzClSessClientSessApSerialNum.setStatus("current")
_TrpzClSessClientSessRadioNum_Type = TrpzRadioNum
_TrpzClSessClientSessRadioNum_Object = MibTableColumn
trpzClSessClientSessRadioNum = _TrpzClSessClientSessRadioNum_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 1, 1, 8),
    _TrpzClSessClientSessRadioNum_Type()
)
trpzClSessClientSessRadioNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzClSessClientSessRadioNum.setStatus("current")
_TrpzClSessClientSessAccessType_Type = TrpzAccessType
_TrpzClSessClientSessAccessType_Object = MibTableColumn
trpzClSessClientSessAccessType = _TrpzClSessClientSessAccessType_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 1, 1, 9),
    _TrpzClSessClientSessAccessType_Type()
)
trpzClSessClientSessAccessType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzClSessClientSessAccessType.setStatus("obsolete")
_TrpzClSessClientSessAuthMethod_Type = TrpzAuthMethod
_TrpzClSessClientSessAuthMethod_Object = MibTableColumn
trpzClSessClientSessAuthMethod = _TrpzClSessClientSessAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 1, 1, 10),
    _TrpzClSessClientSessAuthMethod_Type()
)
trpzClSessClientSessAuthMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzClSessClientSessAuthMethod.setStatus("obsolete")
_TrpzClSessClientSessAuthServer_Type = IpAddress
_TrpzClSessClientSessAuthServer_Object = MibTableColumn
trpzClSessClientSessAuthServer = _TrpzClSessClientSessAuthServer_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 1, 1, 11),
    _TrpzClSessClientSessAuthServer_Type()
)
trpzClSessClientSessAuthServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzClSessClientSessAuthServer.setStatus("current")
_TrpzClSessClientSessPortOrNum_Type = Unsigned32
_TrpzClSessClientSessPortOrNum_Object = MibTableColumn
trpzClSessClientSessPortOrNum = _TrpzClSessClientSessPortOrNum_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 1, 1, 12),
    _TrpzClSessClientSessPortOrNum_Type()
)
trpzClSessClientSessPortOrNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzClSessClientSessPortOrNum.setStatus("obsolete")
_TrpzClSessClientSessVlanTag_Type = Unsigned32
_TrpzClSessClientSessVlanTag_Object = MibTableColumn
trpzClSessClientSessVlanTag = _TrpzClSessClientSessVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 1, 1, 13),
    _TrpzClSessClientSessVlanTag_Type()
)
trpzClSessClientSessVlanTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzClSessClientSessVlanTag.setStatus("current")
_TrpzClSessClientSessTimeStamp_Type = TimeStamp
_TrpzClSessClientSessTimeStamp_Object = MibTableColumn
trpzClSessClientSessTimeStamp = _TrpzClSessClientSessTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 1, 1, 14),
    _TrpzClSessClientSessTimeStamp_Type()
)
trpzClSessClientSessTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzClSessClientSessTimeStamp.setStatus("current")


class _TrpzClSessClientSessSsid_Type(DisplayString):
    """Custom type trpzClSessClientSessSsid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 33),
    )


_TrpzClSessClientSessSsid_Type.__name__ = "DisplayString"
_TrpzClSessClientSessSsid_Object = MibTableColumn
trpzClSessClientSessSsid = _TrpzClSessClientSessSsid_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 1, 1, 15),
    _TrpzClSessClientSessSsid_Type()
)
trpzClSessClientSessSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzClSessClientSessSsid.setStatus("current")
_TrpzClSessClientSessState_Type = TrpzSessState
_TrpzClSessClientSessState_Object = MibTableColumn
trpzClSessClientSessState = _TrpzClSessClientSessState_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 1, 1, 16),
    _TrpzClSessClientSessState_Type()
)
trpzClSessClientSessState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzClSessClientSessState.setStatus("deprecated")
_TrpzClSessClientSessLoginType_Type = TrpzUserAccessType
_TrpzClSessClientSessLoginType_Object = MibTableColumn
trpzClSessClientSessLoginType = _TrpzClSessClientSessLoginType_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 1, 1, 17),
    _TrpzClSessClientSessLoginType_Type()
)
trpzClSessClientSessLoginType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzClSessClientSessLoginType.setStatus("current")
_TrpzClSessClientSessDot1xAuthMethod_Type = TrpzClientAuthenProtocolType
_TrpzClSessClientSessDot1xAuthMethod_Object = MibTableColumn
trpzClSessClientSessDot1xAuthMethod = _TrpzClSessClientSessDot1xAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 1, 1, 18),
    _TrpzClSessClientSessDot1xAuthMethod_Type()
)
trpzClSessClientSessDot1xAuthMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzClSessClientSessDot1xAuthMethod.setStatus("current")
_TrpzClSessClientSessSessionState_Type = TrpzClientSessionState
_TrpzClSessClientSessSessionState_Object = MibTableColumn
trpzClSessClientSessSessionState = _TrpzClSessClientSessSessionState_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 1, 1, 19),
    _TrpzClSessClientSessSessionState_Type()
)
trpzClSessClientSessSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzClSessClientSessSessionState.setStatus("current")
_TrpzClSessClientSessAccessMode_Type = TrpzClientAccessMode
_TrpzClSessClientSessAccessMode_Object = MibTableColumn
trpzClSessClientSessAccessMode = _TrpzClSessClientSessAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 1, 1, 20),
    _TrpzClSessClientSessAccessMode_Type()
)
trpzClSessClientSessAccessMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzClSessClientSessAccessMode.setStatus("current")
_TrpzClSessClientSessApNum_Type = TrpzApNum
_TrpzClSessClientSessApNum_Object = MibTableColumn
trpzClSessClientSessApNum = _TrpzClSessClientSessApNum_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 1, 1, 21),
    _TrpzClSessClientSessApNum_Type()
)
trpzClSessClientSessApNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzClSessClientSessApNum.setStatus("current")
_TrpzClSessClientSessPhysPortNum_Type = TrpzPhysPortNumberOrZero
_TrpzClSessClientSessPhysPortNum_Object = MibTableColumn
trpzClSessClientSessPhysPortNum = _TrpzClSessClientSessPhysPortNum_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 1, 1, 22),
    _TrpzClSessClientSessPhysPortNum_Type()
)
trpzClSessClientSessPhysPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzClSessClientSessPhysPortNum.setStatus("current")
_TrpzClSessClientSessDeviceType_Type = TrpzClientDeviceType
_TrpzClSessClientSessDeviceType_Object = MibTableColumn
trpzClSessClientSessDeviceType = _TrpzClSessClientSessDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 1, 1, 23),
    _TrpzClSessClientSessDeviceType_Type()
)
trpzClSessClientSessDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzClSessClientSessDeviceType.setStatus("current")
_TrpzClSessClientSessDeviceGroup_Type = TrpzClientDeviceGroupName
_TrpzClSessClientSessDeviceGroup_Object = MibTableColumn
trpzClSessClientSessDeviceGroup = _TrpzClSessClientSessDeviceGroup_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 1, 1, 24),
    _TrpzClSessClientSessDeviceGroup_Type()
)
trpzClSessClientSessDeviceGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzClSessClientSessDeviceGroup.setStatus("current")
_TrpzClSessClientSessDeviceProfileName_Type = TrpzClientDeviceProfileName
_TrpzClSessClientSessDeviceProfileName_Object = MibTableColumn
trpzClSessClientSessDeviceProfileName = _TrpzClSessClientSessDeviceProfileName_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 1, 1, 25),
    _TrpzClSessClientSessDeviceProfileName_Type()
)
trpzClSessClientSessDeviceProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzClSessClientSessDeviceProfileName.setStatus("current")
_TrpzClSessRoamingHistoryTable_Object = MibTable
trpzClSessRoamingHistoryTable = _TrpzClSessRoamingHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 2)
)
if mibBuilder.loadTexts:
    trpzClSessRoamingHistoryTable.setStatus("current")
_TrpzClSessRoamingHistoryEntry_Object = MibTableRow
trpzClSessRoamingHistoryEntry = _TrpzClSessRoamingHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 2, 1)
)
trpzClSessRoamingHistoryEntry.setIndexNames(
    (0, "TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessRoamHistMacAddress"),
    (0, "TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessRoamHistIndex"),
)
if mibBuilder.loadTexts:
    trpzClSessRoamingHistoryEntry.setStatus("current")
_TrpzClSessRoamHistMacAddress_Type = MacAddress
_TrpzClSessRoamHistMacAddress_Object = MibTableColumn
trpzClSessRoamHistMacAddress = _TrpzClSessRoamHistMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 2, 1, 1),
    _TrpzClSessRoamHistMacAddress_Type()
)
trpzClSessRoamHistMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzClSessRoamHistMacAddress.setStatus("current")
_TrpzClSessRoamHistIndex_Type = Unsigned32
_TrpzClSessRoamHistIndex_Object = MibTableColumn
trpzClSessRoamHistIndex = _TrpzClSessRoamHistIndex_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 2, 1, 2),
    _TrpzClSessRoamHistIndex_Type()
)
trpzClSessRoamHistIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzClSessRoamHistIndex.setStatus("current")
_TrpzClSessRoamHistApSerialNum_Type = TrpzApSerialNum
_TrpzClSessRoamHistApSerialNum_Object = MibTableColumn
trpzClSessRoamHistApSerialNum = _TrpzClSessRoamHistApSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 2, 1, 3),
    _TrpzClSessRoamHistApSerialNum_Type()
)
trpzClSessRoamHistApSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzClSessRoamHistApSerialNum.setStatus("current")
_TrpzClSessRoamHistRadioNum_Type = TrpzRadioNum
_TrpzClSessRoamHistRadioNum_Object = MibTableColumn
trpzClSessRoamHistRadioNum = _TrpzClSessRoamHistRadioNum_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 2, 1, 4),
    _TrpzClSessRoamHistRadioNum_Type()
)
trpzClSessRoamHistRadioNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzClSessRoamHistRadioNum.setStatus("current")
_TrpzClSessRoamHistAccessType_Type = TrpzAccessType
_TrpzClSessRoamHistAccessType_Object = MibTableColumn
trpzClSessRoamHistAccessType = _TrpzClSessRoamHistAccessType_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 2, 1, 5),
    _TrpzClSessRoamHistAccessType_Type()
)
trpzClSessRoamHistAccessType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzClSessRoamHistAccessType.setStatus("obsolete")
_TrpzClSessRoamHistApNumOrPort_Type = Unsigned32
_TrpzClSessRoamHistApNumOrPort_Object = MibTableColumn
trpzClSessRoamHistApNumOrPort = _TrpzClSessRoamHistApNumOrPort_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 2, 1, 6),
    _TrpzClSessRoamHistApNumOrPort_Type()
)
trpzClSessRoamHistApNumOrPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzClSessRoamHistApNumOrPort.setStatus("obsolete")
_TrpzClSessRoamHistIpAddress_Type = IpAddress
_TrpzClSessRoamHistIpAddress_Object = MibTableColumn
trpzClSessRoamHistIpAddress = _TrpzClSessRoamHistIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 2, 1, 7),
    _TrpzClSessRoamHistIpAddress_Type()
)
trpzClSessRoamHistIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzClSessRoamHistIpAddress.setStatus("current")
_TrpzClSessRoamHistTimeStamp_Type = TimeStamp
_TrpzClSessRoamHistTimeStamp_Object = MibTableColumn
trpzClSessRoamHistTimeStamp = _TrpzClSessRoamHistTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 2, 1, 8),
    _TrpzClSessRoamHistTimeStamp_Type()
)
trpzClSessRoamHistTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzClSessRoamHistTimeStamp.setStatus("current")
_TrpzClSessRoamHistAccessMode_Type = TrpzClientAccessMode
_TrpzClSessRoamHistAccessMode_Object = MibTableColumn
trpzClSessRoamHistAccessMode = _TrpzClSessRoamHistAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 2, 1, 9),
    _TrpzClSessRoamHistAccessMode_Type()
)
trpzClSessRoamHistAccessMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzClSessRoamHistAccessMode.setStatus("current")
_TrpzClSessRoamHistApNum_Type = TrpzApNum
_TrpzClSessRoamHistApNum_Object = MibTableColumn
trpzClSessRoamHistApNum = _TrpzClSessRoamHistApNum_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 2, 1, 10),
    _TrpzClSessRoamHistApNum_Type()
)
trpzClSessRoamHistApNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzClSessRoamHistApNum.setStatus("current")
_TrpzClSessRoamHistPhysPortNum_Type = TrpzPhysPortNumberOrZero
_TrpzClSessRoamHistPhysPortNum_Object = MibTableColumn
trpzClSessRoamHistPhysPortNum = _TrpzClSessRoamHistPhysPortNum_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 2, 1, 11),
    _TrpzClSessRoamHistPhysPortNum_Type()
)
trpzClSessRoamHistPhysPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzClSessRoamHistPhysPortNum.setStatus("current")
_TrpzClSessClientSessionStatisticsTable_Object = MibTable
trpzClSessClientSessionStatisticsTable = _TrpzClSessClientSessionStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 3)
)
if mibBuilder.loadTexts:
    trpzClSessClientSessionStatisticsTable.setStatus("current")
_TrpzClSessClientSessionStatisticsEntry_Object = MibTableRow
trpzClSessClientSessionStatisticsEntry = _TrpzClSessClientSessionStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 3, 1)
)
trpzClSessClientSessionStatisticsEntry.setIndexNames(
    (0, "TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessStatsMacAddress"),
)
if mibBuilder.loadTexts:
    trpzClSessClientSessionStatisticsEntry.setStatus("current")
_TrpzClSessClientSessStatsMacAddress_Type = MacAddress
_TrpzClSessClientSessStatsMacAddress_Object = MibTableColumn
trpzClSessClientSessStatsMacAddress = _TrpzClSessClientSessStatsMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 3, 1, 1),
    _TrpzClSessClientSessStatsMacAddress_Type()
)
trpzClSessClientSessStatsMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzClSessClientSessStatsMacAddress.setStatus("current")
_TrpzClSessClientSessStatsUniPktIn_Type = Counter64
_TrpzClSessClientSessStatsUniPktIn_Object = MibTableColumn
trpzClSessClientSessStatsUniPktIn = _TrpzClSessClientSessStatsUniPktIn_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 3, 1, 2),
    _TrpzClSessClientSessStatsUniPktIn_Type()
)
trpzClSessClientSessStatsUniPktIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzClSessClientSessStatsUniPktIn.setStatus("current")
_TrpzClSessClientSessStatsUniOctetIn_Type = Counter64
_TrpzClSessClientSessStatsUniOctetIn_Object = MibTableColumn
trpzClSessClientSessStatsUniOctetIn = _TrpzClSessClientSessStatsUniOctetIn_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 3, 1, 3),
    _TrpzClSessClientSessStatsUniOctetIn_Type()
)
trpzClSessClientSessStatsUniOctetIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzClSessClientSessStatsUniOctetIn.setStatus("current")
_TrpzClSessClientSessStatsUniPktOut_Type = Counter64
_TrpzClSessClientSessStatsUniPktOut_Object = MibTableColumn
trpzClSessClientSessStatsUniPktOut = _TrpzClSessClientSessStatsUniPktOut_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 3, 1, 4),
    _TrpzClSessClientSessStatsUniPktOut_Type()
)
trpzClSessClientSessStatsUniPktOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzClSessClientSessStatsUniPktOut.setStatus("current")
_TrpzClSessClientSessStatsUniOctetOut_Type = Counter64
_TrpzClSessClientSessStatsUniOctetOut_Object = MibTableColumn
trpzClSessClientSessStatsUniOctetOut = _TrpzClSessClientSessStatsUniOctetOut_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 3, 1, 5),
    _TrpzClSessClientSessStatsUniOctetOut_Type()
)
trpzClSessClientSessStatsUniOctetOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzClSessClientSessStatsUniOctetOut.setStatus("current")
_TrpzClSessClientSessStatsMultiPktIn_Type = Counter64
_TrpzClSessClientSessStatsMultiPktIn_Object = MibTableColumn
trpzClSessClientSessStatsMultiPktIn = _TrpzClSessClientSessStatsMultiPktIn_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 3, 1, 6),
    _TrpzClSessClientSessStatsMultiPktIn_Type()
)
trpzClSessClientSessStatsMultiPktIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzClSessClientSessStatsMultiPktIn.setStatus("current")
_TrpzClSessClientSessStatsMultiOctetIn_Type = Counter64
_TrpzClSessClientSessStatsMultiOctetIn_Object = MibTableColumn
trpzClSessClientSessStatsMultiOctetIn = _TrpzClSessClientSessStatsMultiOctetIn_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 3, 1, 7),
    _TrpzClSessClientSessStatsMultiOctetIn_Type()
)
trpzClSessClientSessStatsMultiOctetIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzClSessClientSessStatsMultiOctetIn.setStatus("current")
_TrpzClSessClientSessStatsEncErrPkt_Type = Counter64
_TrpzClSessClientSessStatsEncErrPkt_Object = MibTableColumn
trpzClSessClientSessStatsEncErrPkt = _TrpzClSessClientSessStatsEncErrPkt_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 3, 1, 8),
    _TrpzClSessClientSessStatsEncErrPkt_Type()
)
trpzClSessClientSessStatsEncErrPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzClSessClientSessStatsEncErrPkt.setStatus("current")
_TrpzClSessClientSessStatsEncErrOctet_Type = Counter64
_TrpzClSessClientSessStatsEncErrOctet_Object = MibTableColumn
trpzClSessClientSessStatsEncErrOctet = _TrpzClSessClientSessStatsEncErrOctet_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 3, 1, 9),
    _TrpzClSessClientSessStatsEncErrOctet_Type()
)
trpzClSessClientSessStatsEncErrOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzClSessClientSessStatsEncErrOctet.setStatus("current")
_TrpzClSessClientSessStatsLastRate_Type = TrpzRadioRate
_TrpzClSessClientSessStatsLastRate_Object = MibTableColumn
trpzClSessClientSessStatsLastRate = _TrpzClSessClientSessStatsLastRate_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 3, 1, 10),
    _TrpzClSessClientSessStatsLastRate_Type()
)
trpzClSessClientSessStatsLastRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzClSessClientSessStatsLastRate.setStatus("current")
_TrpzClSessClientSessStatsLastRssi_Type = TrpzRssi
_TrpzClSessClientSessStatsLastRssi_Object = MibTableColumn
trpzClSessClientSessStatsLastRssi = _TrpzClSessClientSessStatsLastRssi_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 3, 1, 11),
    _TrpzClSessClientSessStatsLastRssi_Type()
)
trpzClSessClientSessStatsLastRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzClSessClientSessStatsLastRssi.setStatus("current")
_TrpzClSessClientSessStatsLastSNR_Type = Integer32
_TrpzClSessClientSessStatsLastSNR_Object = MibTableColumn
trpzClSessClientSessStatsLastSNR = _TrpzClSessClientSessStatsLastSNR_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 3, 1, 12),
    _TrpzClSessClientSessStatsLastSNR_Type()
)
trpzClSessClientSessStatsLastSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzClSessClientSessStatsLastSNR.setStatus("current")
_TrpzClSessTotalSessions_Type = Unsigned32
_TrpzClSessTotalSessions_Object = MibScalar
trpzClSessTotalSessions = _TrpzClSessTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 4),
    _TrpzClSessTotalSessions_Type()
)
trpzClSessTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzClSessTotalSessions.setStatus("current")
_TrpzClSessClientAddressTable_Object = MibTable
trpzClSessClientAddressTable = _TrpzClSessClientAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 5)
)
if mibBuilder.loadTexts:
    trpzClSessClientAddressTable.setStatus("current")
_TrpzClSessClientAddressEntry_Object = MibTableRow
trpzClSessClientAddressEntry = _TrpzClSessClientAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 5, 1)
)
trpzClSessClientAddressEntry.setIndexNames(
    (0, "TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessMacAddress"),
    (0, "TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientAddressIndex"),
)
if mibBuilder.loadTexts:
    trpzClSessClientAddressEntry.setStatus("current")
_TrpzClSessClientAddressIndex_Type = Unsigned32
_TrpzClSessClientAddressIndex_Object = MibTableColumn
trpzClSessClientAddressIndex = _TrpzClSessClientAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 5, 1, 1),
    _TrpzClSessClientAddressIndex_Type()
)
trpzClSessClientAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trpzClSessClientAddressIndex.setStatus("current")
_TrpzClSessClientAddressType_Type = InetAddressType
_TrpzClSessClientAddressType_Object = MibTableColumn
trpzClSessClientAddressType = _TrpzClSessClientAddressType_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 5, 1, 2),
    _TrpzClSessClientAddressType_Type()
)
trpzClSessClientAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzClSessClientAddressType.setStatus("current")
_TrpzClSessClientAddressValue_Type = InetAddress
_TrpzClSessClientAddressValue_Object = MibTableColumn
trpzClSessClientAddressValue = _TrpzClSessClientAddressValue_Object(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 1, 5, 1, 3),
    _TrpzClSessClientAddressValue_Type()
)
trpzClSessClientAddressValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trpzClSessClientAddressValue.setStatus("current")
_TrpzClientSessionConformance_ObjectIdentity = ObjectIdentity
trpzClientSessionConformance = _TrpzClientSessionConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 2)
)
_TrpzClientSessionCompliances_ObjectIdentity = ObjectIdentity
trpzClientSessionCompliances = _TrpzClientSessionCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 2, 1)
)
_TrpzClientSessionGroups_ObjectIdentity = ObjectIdentity
trpzClientSessionGroups = _TrpzClientSessionGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 2, 2)
)

# Managed Objects groups

trpzClientSessionCommonGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 2, 2, 1)
)
trpzClientSessionCommonGroup.setObjects(
      *(("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessSessionId"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessUsername"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessIpAddress"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessEncryptionType"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessVlan"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessApSerialNum"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessRadioNum"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessAccessType"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessAuthMethod"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessAuthServer"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessPortOrNum"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessVlanTag"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessTimeStamp"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessSsid"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessState"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessRoamHistApSerialNum"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessRoamHistRadioNum"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessRoamHistAccessType"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessRoamHistApNumOrPort"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessRoamHistIpAddress"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessRoamHistTimeStamp"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessStatsUniPktIn"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessStatsUniOctetIn"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessStatsUniPktOut"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessStatsUniOctetOut"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessStatsMultiPktIn"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessStatsMultiOctetIn"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessStatsEncErrPkt"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessStatsEncErrOctet"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessStatsLastRate"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessStatsLastRssi"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessStatsLastSNR"))
)
if mibBuilder.loadTexts:
    trpzClientSessionCommonGroup.setStatus("obsolete")

trpzClientSessScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 2, 2, 2)
)
trpzClientSessScalarsGroup.setObjects(
    ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessTotalSessions")
)
if mibBuilder.loadTexts:
    trpzClientSessScalarsGroup.setStatus("current")

trpzClientSessClientSessionTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 2, 2, 3)
)
trpzClientSessClientSessionTableGroup.setObjects(
      *(("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessSessionId"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessUsername"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessIpAddress"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessEncryptionType"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessVlan"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessApSerialNum"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessRadioNum"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessAccessType"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessAuthServer"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessPortOrNum"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessVlanTag"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessTimeStamp"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessSsid"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessLoginType"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessDot1xAuthMethod"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessSessionState"))
)
if mibBuilder.loadTexts:
    trpzClientSessClientSessionTableGroup.setStatus("obsolete")

trpzClientSessRoamingHistoryTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 2, 2, 4)
)
trpzClientSessRoamingHistoryTableGroup.setObjects(
      *(("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessRoamHistApSerialNum"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessRoamHistRadioNum"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessRoamHistAccessType"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessRoamHistApNumOrPort"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessRoamHistIpAddress"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessRoamHistTimeStamp"))
)
if mibBuilder.loadTexts:
    trpzClientSessRoamingHistoryTableGroup.setStatus("obsolete")

trpzClientSessClientSessionStatisticsTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 2, 2, 5)
)
trpzClientSessClientSessionStatisticsTableGroup.setObjects(
      *(("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessStatsUniPktIn"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessStatsUniOctetIn"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessStatsUniPktOut"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessStatsUniOctetOut"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessStatsMultiPktIn"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessStatsMultiOctetIn"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessStatsEncErrPkt"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessStatsEncErrOctet"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessStatsLastRate"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessStatsLastRssi"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessStatsLastSNR"))
)
if mibBuilder.loadTexts:
    trpzClientSessClientSessionStatisticsTableGroup.setStatus("current")

trpzClientSessClientSessionTableGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 2, 2, 6)
)
trpzClientSessClientSessionTableGroupRev2.setObjects(
      *(("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessSessionId"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessUsername"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessIpAddress"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessEncryptionType"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessVlan"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessApSerialNum"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessRadioNum"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessAuthServer"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessVlanTag"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessTimeStamp"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessSsid"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessLoginType"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessDot1xAuthMethod"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessSessionState"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessAccessMode"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessApNum"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessPhysPortNum"))
)
if mibBuilder.loadTexts:
    trpzClientSessClientSessionTableGroupRev2.setStatus("obsolete")

trpzClientSessRoamingHistoryTableGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 2, 2, 7)
)
trpzClientSessRoamingHistoryTableGroupRev2.setObjects(
      *(("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessRoamHistApSerialNum"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessRoamHistRadioNum"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessRoamHistIpAddress"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessRoamHistTimeStamp"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessRoamHistAccessMode"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessRoamHistApNum"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessRoamHistPhysPortNum"))
)
if mibBuilder.loadTexts:
    trpzClientSessRoamingHistoryTableGroupRev2.setStatus("current")

trpzClSessClientAddressTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 2, 2, 8)
)
trpzClSessClientAddressTableGroup.setObjects(
      *(("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientAddressType"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientAddressValue"))
)
if mibBuilder.loadTexts:
    trpzClSessClientAddressTableGroup.setStatus("current")

trpzClientSessClientSessionTableGroupRev3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 2, 2, 9)
)
trpzClientSessClientSessionTableGroupRev3.setObjects(
      *(("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessSessionId"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessUsername"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessIpAddress"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessEncryptionType"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessVlan"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessApSerialNum"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessRadioNum"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessAuthServer"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessVlanTag"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessTimeStamp"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessSsid"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessLoginType"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessDot1xAuthMethod"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessSessionState"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessAccessMode"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessApNum"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessPhysPortNum"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessDeviceType"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessDeviceGroup"),
        ("TRAPEZE-NETWORKS-CLIENT-SESSION-MIB", "trpzClSessClientSessDeviceProfileName"))
)
if mibBuilder.loadTexts:
    trpzClientSessClientSessionTableGroupRev3.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

trpzClientSessionCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    trpzClientSessionCompliance.setStatus(
        "obsolete"
    )

trpzClientSessionComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    trpzClientSessionComplianceRev2.setStatus(
        "obsolete"
    )

trpzClientSessionComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 2, 1, 3)
)
if mibBuilder.loadTexts:
    trpzClientSessionComplianceRev3.setStatus(
        "obsolete"
    )

trpzClientSessionComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 14525, 4, 4, 1, 2, 1, 4)
)
if mibBuilder.loadTexts:
    trpzClientSessionComplianceRev4.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TRAPEZE-NETWORKS-CLIENT-SESSION-MIB",
    **{"TrpzEncryptionType": TrpzEncryptionType,
       "TrpzAuthMethod": TrpzAuthMethod,
       "TrpzSessState": TrpzSessState,
       "trpzClientSessionMib": trpzClientSessionMib,
       "trpzClientSessionObjects": trpzClientSessionObjects,
       "trpzClientSessionDataObjects": trpzClientSessionDataObjects,
       "trpzClSessClientSessionTable": trpzClSessClientSessionTable,
       "trpzClSessClientSessionEntry": trpzClSessClientSessionEntry,
       "trpzClSessClientSessMacAddress": trpzClSessClientSessMacAddress,
       "trpzClSessClientSessSessionId": trpzClSessClientSessSessionId,
       "trpzClSessClientSessUsername": trpzClSessClientSessUsername,
       "trpzClSessClientSessIpAddress": trpzClSessClientSessIpAddress,
       "trpzClSessClientSessEncryptionType": trpzClSessClientSessEncryptionType,
       "trpzClSessClientSessVlan": trpzClSessClientSessVlan,
       "trpzClSessClientSessApSerialNum": trpzClSessClientSessApSerialNum,
       "trpzClSessClientSessRadioNum": trpzClSessClientSessRadioNum,
       "trpzClSessClientSessAccessType": trpzClSessClientSessAccessType,
       "trpzClSessClientSessAuthMethod": trpzClSessClientSessAuthMethod,
       "trpzClSessClientSessAuthServer": trpzClSessClientSessAuthServer,
       "trpzClSessClientSessPortOrNum": trpzClSessClientSessPortOrNum,
       "trpzClSessClientSessVlanTag": trpzClSessClientSessVlanTag,
       "trpzClSessClientSessTimeStamp": trpzClSessClientSessTimeStamp,
       "trpzClSessClientSessSsid": trpzClSessClientSessSsid,
       "trpzClSessClientSessState": trpzClSessClientSessState,
       "trpzClSessClientSessLoginType": trpzClSessClientSessLoginType,
       "trpzClSessClientSessDot1xAuthMethod": trpzClSessClientSessDot1xAuthMethod,
       "trpzClSessClientSessSessionState": trpzClSessClientSessSessionState,
       "trpzClSessClientSessAccessMode": trpzClSessClientSessAccessMode,
       "trpzClSessClientSessApNum": trpzClSessClientSessApNum,
       "trpzClSessClientSessPhysPortNum": trpzClSessClientSessPhysPortNum,
       "trpzClSessClientSessDeviceType": trpzClSessClientSessDeviceType,
       "trpzClSessClientSessDeviceGroup": trpzClSessClientSessDeviceGroup,
       "trpzClSessClientSessDeviceProfileName": trpzClSessClientSessDeviceProfileName,
       "trpzClSessRoamingHistoryTable": trpzClSessRoamingHistoryTable,
       "trpzClSessRoamingHistoryEntry": trpzClSessRoamingHistoryEntry,
       "trpzClSessRoamHistMacAddress": trpzClSessRoamHistMacAddress,
       "trpzClSessRoamHistIndex": trpzClSessRoamHistIndex,
       "trpzClSessRoamHistApSerialNum": trpzClSessRoamHistApSerialNum,
       "trpzClSessRoamHistRadioNum": trpzClSessRoamHistRadioNum,
       "trpzClSessRoamHistAccessType": trpzClSessRoamHistAccessType,
       "trpzClSessRoamHistApNumOrPort": trpzClSessRoamHistApNumOrPort,
       "trpzClSessRoamHistIpAddress": trpzClSessRoamHistIpAddress,
       "trpzClSessRoamHistTimeStamp": trpzClSessRoamHistTimeStamp,
       "trpzClSessRoamHistAccessMode": trpzClSessRoamHistAccessMode,
       "trpzClSessRoamHistApNum": trpzClSessRoamHistApNum,
       "trpzClSessRoamHistPhysPortNum": trpzClSessRoamHistPhysPortNum,
       "trpzClSessClientSessionStatisticsTable": trpzClSessClientSessionStatisticsTable,
       "trpzClSessClientSessionStatisticsEntry": trpzClSessClientSessionStatisticsEntry,
       "trpzClSessClientSessStatsMacAddress": trpzClSessClientSessStatsMacAddress,
       "trpzClSessClientSessStatsUniPktIn": trpzClSessClientSessStatsUniPktIn,
       "trpzClSessClientSessStatsUniOctetIn": trpzClSessClientSessStatsUniOctetIn,
       "trpzClSessClientSessStatsUniPktOut": trpzClSessClientSessStatsUniPktOut,
       "trpzClSessClientSessStatsUniOctetOut": trpzClSessClientSessStatsUniOctetOut,
       "trpzClSessClientSessStatsMultiPktIn": trpzClSessClientSessStatsMultiPktIn,
       "trpzClSessClientSessStatsMultiOctetIn": trpzClSessClientSessStatsMultiOctetIn,
       "trpzClSessClientSessStatsEncErrPkt": trpzClSessClientSessStatsEncErrPkt,
       "trpzClSessClientSessStatsEncErrOctet": trpzClSessClientSessStatsEncErrOctet,
       "trpzClSessClientSessStatsLastRate": trpzClSessClientSessStatsLastRate,
       "trpzClSessClientSessStatsLastRssi": trpzClSessClientSessStatsLastRssi,
       "trpzClSessClientSessStatsLastSNR": trpzClSessClientSessStatsLastSNR,
       "trpzClSessTotalSessions": trpzClSessTotalSessions,
       "trpzClSessClientAddressTable": trpzClSessClientAddressTable,
       "trpzClSessClientAddressEntry": trpzClSessClientAddressEntry,
       "trpzClSessClientAddressIndex": trpzClSessClientAddressIndex,
       "trpzClSessClientAddressType": trpzClSessClientAddressType,
       "trpzClSessClientAddressValue": trpzClSessClientAddressValue,
       "trpzClientSessionConformance": trpzClientSessionConformance,
       "trpzClientSessionCompliances": trpzClientSessionCompliances,
       "trpzClientSessionCompliance": trpzClientSessionCompliance,
       "trpzClientSessionComplianceRev2": trpzClientSessionComplianceRev2,
       "trpzClientSessionComplianceRev3": trpzClientSessionComplianceRev3,
       "trpzClientSessionComplianceRev4": trpzClientSessionComplianceRev4,
       "trpzClientSessionGroups": trpzClientSessionGroups,
       "trpzClientSessionCommonGroup": trpzClientSessionCommonGroup,
       "trpzClientSessScalarsGroup": trpzClientSessScalarsGroup,
       "trpzClientSessClientSessionTableGroup": trpzClientSessClientSessionTableGroup,
       "trpzClientSessRoamingHistoryTableGroup": trpzClientSessRoamingHistoryTableGroup,
       "trpzClientSessClientSessionStatisticsTableGroup": trpzClientSessClientSessionStatisticsTableGroup,
       "trpzClientSessClientSessionTableGroupRev2": trpzClientSessClientSessionTableGroupRev2,
       "trpzClientSessRoamingHistoryTableGroupRev2": trpzClientSessRoamingHistoryTableGroupRev2,
       "trpzClSessClientAddressTableGroup": trpzClSessClientAddressTableGroup,
       "trpzClientSessClientSessionTableGroupRev3": trpzClientSessClientSessionTableGroupRev3}
)
