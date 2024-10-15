# SNMP MIB module (NTWS-CLIENT-SESSION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NTWS-CLIENT-SESSION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:29:55 2024
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

(NtwsAccessType,
 NtwsApNum,
 NtwsApSerialNum,
 NtwsRadioNum,
 NtwsRadioRate,
 NtwsRssi) = mibBuilder.importSymbols(
    "NTWS-AP-TC",
    "NtwsAccessType",
    "NtwsApNum",
    "NtwsApSerialNum",
    "NtwsRadioNum",
    "NtwsRadioRate",
    "NtwsRssi")

(NtwsPhysPortNumberOrZero,) = mibBuilder.importSymbols(
    "NTWS-BASIC-TC",
    "NtwsPhysPortNumberOrZero")

(NtwsClientAccessMode,
 NtwsClientAuthenProtocolType,
 NtwsClientSessionState,
 NtwsUserAccessType) = mibBuilder.importSymbols(
    "NTWS-CLIENT-SESSION-TC",
    "NtwsClientAccessMode",
    "NtwsClientAuthenProtocolType",
    "NtwsClientSessionState",
    "NtwsUserAccessType")

(ntwsMibs,) = mibBuilder.importSymbols(
    "NTWS-ROOT-MIB",
    "ntwsMibs")

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


# MODULE-IDENTITY

ntwsClientSessionMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 4)
)
ntwsClientSessionMib.setRevisions(
        ("2008-10-23 00:56",
         "2008-05-23 00:55",
         "2007-11-01 00:54",
         "2007-10-09 00:51",
         "2007-08-16 00:44",
         "2006-11-16 00:43",
         "2006-10-17 00:42",
         "2006-09-26 00:32",
         "2006-07-29 00:21",
         "2006-06-06 00:10",
         "2006-03-30 00:08")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class NtwsEncryptionType(Integer32, TextualConvention):
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



class NtwsAuthMethod(Integer32, TextualConvention):
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



class NtwsSessState(Integer32, TextualConvention):
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

_NtwsClientSessionObjects_ObjectIdentity = ObjectIdentity
ntwsClientSessionObjects = _NtwsClientSessionObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 4, 1)
)
_NtwsClientSessionDataObjects_ObjectIdentity = ObjectIdentity
ntwsClientSessionDataObjects = _NtwsClientSessionDataObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 4, 1, 1)
)
_NtwsClSessClientSessionTable_Object = MibTable
ntwsClSessClientSessionTable = _NtwsClSessClientSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ntwsClSessClientSessionTable.setStatus("current")
_NtwsClSessClientSessionEntry_Object = MibTableRow
ntwsClSessClientSessionEntry = _NtwsClSessClientSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 4, 1, 1, 1, 1)
)
ntwsClSessClientSessionEntry.setIndexNames(
    (0, "NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessMacAddress"),
)
if mibBuilder.loadTexts:
    ntwsClSessClientSessionEntry.setStatus("current")
_NtwsClSessClientSessMacAddress_Type = MacAddress
_NtwsClSessClientSessMacAddress_Object = MibTableColumn
ntwsClSessClientSessMacAddress = _NtwsClSessClientSessMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 4, 1, 1, 1, 1, 1),
    _NtwsClSessClientSessMacAddress_Type()
)
ntwsClSessClientSessMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntwsClSessClientSessMacAddress.setStatus("current")


class _NtwsClSessClientSessSessionId_Type(DisplayString):
    """Custom type ntwsClSessClientSessSessionId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_NtwsClSessClientSessSessionId_Type.__name__ = "DisplayString"
_NtwsClSessClientSessSessionId_Object = MibTableColumn
ntwsClSessClientSessSessionId = _NtwsClSessClientSessSessionId_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 4, 1, 1, 1, 1, 2),
    _NtwsClSessClientSessSessionId_Type()
)
ntwsClSessClientSessSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsClSessClientSessSessionId.setStatus("current")


class _NtwsClSessClientSessUsername_Type(DisplayString):
    """Custom type ntwsClSessClientSessUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_NtwsClSessClientSessUsername_Type.__name__ = "DisplayString"
_NtwsClSessClientSessUsername_Object = MibTableColumn
ntwsClSessClientSessUsername = _NtwsClSessClientSessUsername_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 4, 1, 1, 1, 1, 3),
    _NtwsClSessClientSessUsername_Type()
)
ntwsClSessClientSessUsername.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsClSessClientSessUsername.setStatus("current")
_NtwsClSessClientSessIpAddress_Type = IpAddress
_NtwsClSessClientSessIpAddress_Object = MibTableColumn
ntwsClSessClientSessIpAddress = _NtwsClSessClientSessIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 4, 1, 1, 1, 1, 4),
    _NtwsClSessClientSessIpAddress_Type()
)
ntwsClSessClientSessIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsClSessClientSessIpAddress.setStatus("current")
_NtwsClSessClientSessEncryptionType_Type = NtwsEncryptionType
_NtwsClSessClientSessEncryptionType_Object = MibTableColumn
ntwsClSessClientSessEncryptionType = _NtwsClSessClientSessEncryptionType_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 4, 1, 1, 1, 1, 5),
    _NtwsClSessClientSessEncryptionType_Type()
)
ntwsClSessClientSessEncryptionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsClSessClientSessEncryptionType.setStatus("current")


class _NtwsClSessClientSessVlan_Type(DisplayString):
    """Custom type ntwsClSessClientSessVlan based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_NtwsClSessClientSessVlan_Type.__name__ = "DisplayString"
_NtwsClSessClientSessVlan_Object = MibTableColumn
ntwsClSessClientSessVlan = _NtwsClSessClientSessVlan_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 4, 1, 1, 1, 1, 6),
    _NtwsClSessClientSessVlan_Type()
)
ntwsClSessClientSessVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsClSessClientSessVlan.setStatus("current")
_NtwsClSessClientSessApSerialNum_Type = NtwsApSerialNum
_NtwsClSessClientSessApSerialNum_Object = MibTableColumn
ntwsClSessClientSessApSerialNum = _NtwsClSessClientSessApSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 4, 1, 1, 1, 1, 7),
    _NtwsClSessClientSessApSerialNum_Type()
)
ntwsClSessClientSessApSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsClSessClientSessApSerialNum.setStatus("current")
_NtwsClSessClientSessRadioNum_Type = NtwsRadioNum
_NtwsClSessClientSessRadioNum_Object = MibTableColumn
ntwsClSessClientSessRadioNum = _NtwsClSessClientSessRadioNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 4, 1, 1, 1, 1, 8),
    _NtwsClSessClientSessRadioNum_Type()
)
ntwsClSessClientSessRadioNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsClSessClientSessRadioNum.setStatus("current")
_NtwsClSessClientSessAccessType_Type = NtwsAccessType
_NtwsClSessClientSessAccessType_Object = MibTableColumn
ntwsClSessClientSessAccessType = _NtwsClSessClientSessAccessType_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 4, 1, 1, 1, 1, 9),
    _NtwsClSessClientSessAccessType_Type()
)
ntwsClSessClientSessAccessType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsClSessClientSessAccessType.setStatus("obsolete")
_NtwsClSessClientSessAuthMethod_Type = NtwsAuthMethod
_NtwsClSessClientSessAuthMethod_Object = MibTableColumn
ntwsClSessClientSessAuthMethod = _NtwsClSessClientSessAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 4, 1, 1, 1, 1, 10),
    _NtwsClSessClientSessAuthMethod_Type()
)
ntwsClSessClientSessAuthMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsClSessClientSessAuthMethod.setStatus("deprecated")
_NtwsClSessClientSessAuthServer_Type = IpAddress
_NtwsClSessClientSessAuthServer_Object = MibTableColumn
ntwsClSessClientSessAuthServer = _NtwsClSessClientSessAuthServer_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 4, 1, 1, 1, 1, 11),
    _NtwsClSessClientSessAuthServer_Type()
)
ntwsClSessClientSessAuthServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsClSessClientSessAuthServer.setStatus("current")
_NtwsClSessClientSessPortOrNum_Type = Unsigned32
_NtwsClSessClientSessPortOrNum_Object = MibTableColumn
ntwsClSessClientSessPortOrNum = _NtwsClSessClientSessPortOrNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 4, 1, 1, 1, 1, 12),
    _NtwsClSessClientSessPortOrNum_Type()
)
ntwsClSessClientSessPortOrNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsClSessClientSessPortOrNum.setStatus("obsolete")
_NtwsClSessClientSessVlanTag_Type = Unsigned32
_NtwsClSessClientSessVlanTag_Object = MibTableColumn
ntwsClSessClientSessVlanTag = _NtwsClSessClientSessVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 4, 1, 1, 1, 1, 13),
    _NtwsClSessClientSessVlanTag_Type()
)
ntwsClSessClientSessVlanTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsClSessClientSessVlanTag.setStatus("current")
_NtwsClSessClientSessTimeStamp_Type = TimeStamp
_NtwsClSessClientSessTimeStamp_Object = MibTableColumn
ntwsClSessClientSessTimeStamp = _NtwsClSessClientSessTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 4, 1, 1, 1, 1, 14),
    _NtwsClSessClientSessTimeStamp_Type()
)
ntwsClSessClientSessTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsClSessClientSessTimeStamp.setStatus("current")


class _NtwsClSessClientSessSsid_Type(DisplayString):
    """Custom type ntwsClSessClientSessSsid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 33),
    )


_NtwsClSessClientSessSsid_Type.__name__ = "DisplayString"
_NtwsClSessClientSessSsid_Object = MibTableColumn
ntwsClSessClientSessSsid = _NtwsClSessClientSessSsid_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 4, 1, 1, 1, 1, 15),
    _NtwsClSessClientSessSsid_Type()
)
ntwsClSessClientSessSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsClSessClientSessSsid.setStatus("current")
_NtwsClSessClientSessState_Type = NtwsSessState
_NtwsClSessClientSessState_Object = MibTableColumn
ntwsClSessClientSessState = _NtwsClSessClientSessState_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 4, 1, 1, 1, 1, 16),
    _NtwsClSessClientSessState_Type()
)
ntwsClSessClientSessState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsClSessClientSessState.setStatus("deprecated")
_NtwsClSessClientSessLoginType_Type = NtwsUserAccessType
_NtwsClSessClientSessLoginType_Object = MibTableColumn
ntwsClSessClientSessLoginType = _NtwsClSessClientSessLoginType_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 4, 1, 1, 1, 1, 17),
    _NtwsClSessClientSessLoginType_Type()
)
ntwsClSessClientSessLoginType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsClSessClientSessLoginType.setStatus("current")
_NtwsClSessClientSessDot1xAuthMethod_Type = NtwsClientAuthenProtocolType
_NtwsClSessClientSessDot1xAuthMethod_Object = MibTableColumn
ntwsClSessClientSessDot1xAuthMethod = _NtwsClSessClientSessDot1xAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 4, 1, 1, 1, 1, 18),
    _NtwsClSessClientSessDot1xAuthMethod_Type()
)
ntwsClSessClientSessDot1xAuthMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsClSessClientSessDot1xAuthMethod.setStatus("current")
_NtwsClSessClientSessSessionState_Type = NtwsClientSessionState
_NtwsClSessClientSessSessionState_Object = MibTableColumn
ntwsClSessClientSessSessionState = _NtwsClSessClientSessSessionState_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 4, 1, 1, 1, 1, 19),
    _NtwsClSessClientSessSessionState_Type()
)
ntwsClSessClientSessSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsClSessClientSessSessionState.setStatus("current")
_NtwsClSessClientSessAccessMode_Type = NtwsClientAccessMode
_NtwsClSessClientSessAccessMode_Object = MibTableColumn
ntwsClSessClientSessAccessMode = _NtwsClSessClientSessAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 4, 1, 1, 1, 1, 20),
    _NtwsClSessClientSessAccessMode_Type()
)
ntwsClSessClientSessAccessMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsClSessClientSessAccessMode.setStatus("current")
_NtwsClSessClientSessApNum_Type = NtwsApNum
_NtwsClSessClientSessApNum_Object = MibTableColumn
ntwsClSessClientSessApNum = _NtwsClSessClientSessApNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 4, 1, 1, 1, 1, 21),
    _NtwsClSessClientSessApNum_Type()
)
ntwsClSessClientSessApNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsClSessClientSessApNum.setStatus("current")
_NtwsClSessClientSessPhysPortNum_Type = NtwsPhysPortNumberOrZero
_NtwsClSessClientSessPhysPortNum_Object = MibTableColumn
ntwsClSessClientSessPhysPortNum = _NtwsClSessClientSessPhysPortNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 4, 1, 1, 1, 1, 22),
    _NtwsClSessClientSessPhysPortNum_Type()
)
ntwsClSessClientSessPhysPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsClSessClientSessPhysPortNum.setStatus("current")
_NtwsClSessRoamingHistoryTable_Object = MibTable
ntwsClSessRoamingHistoryTable = _NtwsClSessRoamingHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 4, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ntwsClSessRoamingHistoryTable.setStatus("current")
_NtwsClSessRoamingHistoryEntry_Object = MibTableRow
ntwsClSessRoamingHistoryEntry = _NtwsClSessRoamingHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 4, 1, 1, 2, 1)
)
ntwsClSessRoamingHistoryEntry.setIndexNames(
    (0, "NTWS-CLIENT-SESSION-MIB", "ntwsClSessRoamHistMacAddress"),
    (0, "NTWS-CLIENT-SESSION-MIB", "ntwsClSessRoamHistIndex"),
)
if mibBuilder.loadTexts:
    ntwsClSessRoamingHistoryEntry.setStatus("current")
_NtwsClSessRoamHistMacAddress_Type = MacAddress
_NtwsClSessRoamHistMacAddress_Object = MibTableColumn
ntwsClSessRoamHistMacAddress = _NtwsClSessRoamHistMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 4, 1, 1, 2, 1, 1),
    _NtwsClSessRoamHistMacAddress_Type()
)
ntwsClSessRoamHistMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntwsClSessRoamHistMacAddress.setStatus("current")
_NtwsClSessRoamHistIndex_Type = Unsigned32
_NtwsClSessRoamHistIndex_Object = MibTableColumn
ntwsClSessRoamHistIndex = _NtwsClSessRoamHistIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 4, 1, 1, 2, 1, 2),
    _NtwsClSessRoamHistIndex_Type()
)
ntwsClSessRoamHistIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntwsClSessRoamHistIndex.setStatus("current")
_NtwsClSessRoamHistApSerialNum_Type = NtwsApSerialNum
_NtwsClSessRoamHistApSerialNum_Object = MibTableColumn
ntwsClSessRoamHistApSerialNum = _NtwsClSessRoamHistApSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 4, 1, 1, 2, 1, 3),
    _NtwsClSessRoamHistApSerialNum_Type()
)
ntwsClSessRoamHistApSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsClSessRoamHistApSerialNum.setStatus("current")
_NtwsClSessRoamHistRadioNum_Type = NtwsRadioNum
_NtwsClSessRoamHistRadioNum_Object = MibTableColumn
ntwsClSessRoamHistRadioNum = _NtwsClSessRoamHistRadioNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 4, 1, 1, 2, 1, 4),
    _NtwsClSessRoamHistRadioNum_Type()
)
ntwsClSessRoamHistRadioNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsClSessRoamHistRadioNum.setStatus("current")
_NtwsClSessRoamHistAccessType_Type = NtwsAccessType
_NtwsClSessRoamHistAccessType_Object = MibTableColumn
ntwsClSessRoamHistAccessType = _NtwsClSessRoamHistAccessType_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 4, 1, 1, 2, 1, 5),
    _NtwsClSessRoamHistAccessType_Type()
)
ntwsClSessRoamHistAccessType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsClSessRoamHistAccessType.setStatus("obsolete")
_NtwsClSessRoamHistApNumOrPort_Type = Unsigned32
_NtwsClSessRoamHistApNumOrPort_Object = MibTableColumn
ntwsClSessRoamHistApNumOrPort = _NtwsClSessRoamHistApNumOrPort_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 4, 1, 1, 2, 1, 6),
    _NtwsClSessRoamHistApNumOrPort_Type()
)
ntwsClSessRoamHistApNumOrPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsClSessRoamHistApNumOrPort.setStatus("obsolete")
_NtwsClSessRoamHistIpAddress_Type = IpAddress
_NtwsClSessRoamHistIpAddress_Object = MibTableColumn
ntwsClSessRoamHistIpAddress = _NtwsClSessRoamHistIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 4, 1, 1, 2, 1, 7),
    _NtwsClSessRoamHistIpAddress_Type()
)
ntwsClSessRoamHistIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsClSessRoamHistIpAddress.setStatus("current")
_NtwsClSessRoamHistTimeStamp_Type = TimeStamp
_NtwsClSessRoamHistTimeStamp_Object = MibTableColumn
ntwsClSessRoamHistTimeStamp = _NtwsClSessRoamHistTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 4, 1, 1, 2, 1, 8),
    _NtwsClSessRoamHistTimeStamp_Type()
)
ntwsClSessRoamHistTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsClSessRoamHistTimeStamp.setStatus("current")
_NtwsClSessRoamHistAccessMode_Type = NtwsClientAccessMode
_NtwsClSessRoamHistAccessMode_Object = MibTableColumn
ntwsClSessRoamHistAccessMode = _NtwsClSessRoamHistAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 4, 1, 1, 2, 1, 9),
    _NtwsClSessRoamHistAccessMode_Type()
)
ntwsClSessRoamHistAccessMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsClSessRoamHistAccessMode.setStatus("current")
_NtwsClSessRoamHistApNum_Type = NtwsApNum
_NtwsClSessRoamHistApNum_Object = MibTableColumn
ntwsClSessRoamHistApNum = _NtwsClSessRoamHistApNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 4, 1, 1, 2, 1, 10),
    _NtwsClSessRoamHistApNum_Type()
)
ntwsClSessRoamHistApNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsClSessRoamHistApNum.setStatus("current")
_NtwsClSessRoamHistPhysPortNum_Type = NtwsPhysPortNumberOrZero
_NtwsClSessRoamHistPhysPortNum_Object = MibTableColumn
ntwsClSessRoamHistPhysPortNum = _NtwsClSessRoamHistPhysPortNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 4, 1, 1, 2, 1, 11),
    _NtwsClSessRoamHistPhysPortNum_Type()
)
ntwsClSessRoamHistPhysPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsClSessRoamHistPhysPortNum.setStatus("current")
_NtwsClSessClientSessionStatisticsTable_Object = MibTable
ntwsClSessClientSessionStatisticsTable = _NtwsClSessClientSessionStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 4, 1, 1, 3)
)
if mibBuilder.loadTexts:
    ntwsClSessClientSessionStatisticsTable.setStatus("current")
_NtwsClSessClientSessionStatisticsEntry_Object = MibTableRow
ntwsClSessClientSessionStatisticsEntry = _NtwsClSessClientSessionStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 4, 1, 1, 3, 1)
)
ntwsClSessClientSessionStatisticsEntry.setIndexNames(
    (0, "NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessStatsMacAddress"),
)
if mibBuilder.loadTexts:
    ntwsClSessClientSessionStatisticsEntry.setStatus("current")
_NtwsClSessClientSessStatsMacAddress_Type = MacAddress
_NtwsClSessClientSessStatsMacAddress_Object = MibTableColumn
ntwsClSessClientSessStatsMacAddress = _NtwsClSessClientSessStatsMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 4, 1, 1, 3, 1, 1),
    _NtwsClSessClientSessStatsMacAddress_Type()
)
ntwsClSessClientSessStatsMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntwsClSessClientSessStatsMacAddress.setStatus("current")
_NtwsClSessClientSessStatsUniPktIn_Type = Counter64
_NtwsClSessClientSessStatsUniPktIn_Object = MibTableColumn
ntwsClSessClientSessStatsUniPktIn = _NtwsClSessClientSessStatsUniPktIn_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 4, 1, 1, 3, 1, 2),
    _NtwsClSessClientSessStatsUniPktIn_Type()
)
ntwsClSessClientSessStatsUniPktIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsClSessClientSessStatsUniPktIn.setStatus("current")
_NtwsClSessClientSessStatsUniOctetIn_Type = Counter64
_NtwsClSessClientSessStatsUniOctetIn_Object = MibTableColumn
ntwsClSessClientSessStatsUniOctetIn = _NtwsClSessClientSessStatsUniOctetIn_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 4, 1, 1, 3, 1, 3),
    _NtwsClSessClientSessStatsUniOctetIn_Type()
)
ntwsClSessClientSessStatsUniOctetIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsClSessClientSessStatsUniOctetIn.setStatus("current")
_NtwsClSessClientSessStatsUniPktOut_Type = Counter64
_NtwsClSessClientSessStatsUniPktOut_Object = MibTableColumn
ntwsClSessClientSessStatsUniPktOut = _NtwsClSessClientSessStatsUniPktOut_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 4, 1, 1, 3, 1, 4),
    _NtwsClSessClientSessStatsUniPktOut_Type()
)
ntwsClSessClientSessStatsUniPktOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsClSessClientSessStatsUniPktOut.setStatus("current")
_NtwsClSessClientSessStatsUniOctetOut_Type = Counter64
_NtwsClSessClientSessStatsUniOctetOut_Object = MibTableColumn
ntwsClSessClientSessStatsUniOctetOut = _NtwsClSessClientSessStatsUniOctetOut_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 4, 1, 1, 3, 1, 5),
    _NtwsClSessClientSessStatsUniOctetOut_Type()
)
ntwsClSessClientSessStatsUniOctetOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsClSessClientSessStatsUniOctetOut.setStatus("current")
_NtwsClSessClientSessStatsMultiPktIn_Type = Counter64
_NtwsClSessClientSessStatsMultiPktIn_Object = MibTableColumn
ntwsClSessClientSessStatsMultiPktIn = _NtwsClSessClientSessStatsMultiPktIn_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 4, 1, 1, 3, 1, 6),
    _NtwsClSessClientSessStatsMultiPktIn_Type()
)
ntwsClSessClientSessStatsMultiPktIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsClSessClientSessStatsMultiPktIn.setStatus("current")
_NtwsClSessClientSessStatsMultiOctetIn_Type = Counter64
_NtwsClSessClientSessStatsMultiOctetIn_Object = MibTableColumn
ntwsClSessClientSessStatsMultiOctetIn = _NtwsClSessClientSessStatsMultiOctetIn_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 4, 1, 1, 3, 1, 7),
    _NtwsClSessClientSessStatsMultiOctetIn_Type()
)
ntwsClSessClientSessStatsMultiOctetIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsClSessClientSessStatsMultiOctetIn.setStatus("current")
_NtwsClSessClientSessStatsEncErrPkt_Type = Counter64
_NtwsClSessClientSessStatsEncErrPkt_Object = MibTableColumn
ntwsClSessClientSessStatsEncErrPkt = _NtwsClSessClientSessStatsEncErrPkt_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 4, 1, 1, 3, 1, 8),
    _NtwsClSessClientSessStatsEncErrPkt_Type()
)
ntwsClSessClientSessStatsEncErrPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsClSessClientSessStatsEncErrPkt.setStatus("current")
_NtwsClSessClientSessStatsEncErrOctet_Type = Counter64
_NtwsClSessClientSessStatsEncErrOctet_Object = MibTableColumn
ntwsClSessClientSessStatsEncErrOctet = _NtwsClSessClientSessStatsEncErrOctet_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 4, 1, 1, 3, 1, 9),
    _NtwsClSessClientSessStatsEncErrOctet_Type()
)
ntwsClSessClientSessStatsEncErrOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsClSessClientSessStatsEncErrOctet.setStatus("current")
_NtwsClSessClientSessStatsLastRate_Type = NtwsRadioRate
_NtwsClSessClientSessStatsLastRate_Object = MibTableColumn
ntwsClSessClientSessStatsLastRate = _NtwsClSessClientSessStatsLastRate_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 4, 1, 1, 3, 1, 10),
    _NtwsClSessClientSessStatsLastRate_Type()
)
ntwsClSessClientSessStatsLastRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsClSessClientSessStatsLastRate.setStatus("current")
_NtwsClSessClientSessStatsLastRssi_Type = NtwsRssi
_NtwsClSessClientSessStatsLastRssi_Object = MibTableColumn
ntwsClSessClientSessStatsLastRssi = _NtwsClSessClientSessStatsLastRssi_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 4, 1, 1, 3, 1, 11),
    _NtwsClSessClientSessStatsLastRssi_Type()
)
ntwsClSessClientSessStatsLastRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsClSessClientSessStatsLastRssi.setStatus("current")
_NtwsClSessClientSessStatsLastSNR_Type = Integer32
_NtwsClSessClientSessStatsLastSNR_Object = MibTableColumn
ntwsClSessClientSessStatsLastSNR = _NtwsClSessClientSessStatsLastSNR_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 4, 1, 1, 3, 1, 12),
    _NtwsClSessClientSessStatsLastSNR_Type()
)
ntwsClSessClientSessStatsLastSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsClSessClientSessStatsLastSNR.setStatus("current")
_NtwsClSessTotalSessions_Type = Unsigned32
_NtwsClSessTotalSessions_Object = MibScalar
ntwsClSessTotalSessions = _NtwsClSessTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 4, 1, 1, 4),
    _NtwsClSessTotalSessions_Type()
)
ntwsClSessTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsClSessTotalSessions.setStatus("current")
_NtwsClientSessionConformance_ObjectIdentity = ObjectIdentity
ntwsClientSessionConformance = _NtwsClientSessionConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 4, 1, 2)
)
_NtwsClientSessionCompliances_ObjectIdentity = ObjectIdentity
ntwsClientSessionCompliances = _NtwsClientSessionCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 4, 1, 2, 1)
)
_NtwsClientSessionGroups_ObjectIdentity = ObjectIdentity
ntwsClientSessionGroups = _NtwsClientSessionGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 4, 1, 2, 2)
)

# Managed Objects groups

ntwsClientSessionCommonGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 4, 1, 2, 2, 1)
)
ntwsClientSessionCommonGroup.setObjects(
      *(("NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessSessionId"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessUsername"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessIpAddress"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessEncryptionType"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessVlan"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessApSerialNum"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessRadioNum"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessAccessType"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessAuthMethod"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessAuthServer"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessPortOrNum"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessVlanTag"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessTimeStamp"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessSsid"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessState"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessRoamHistApSerialNum"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessRoamHistRadioNum"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessRoamHistAccessType"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessRoamHistApNumOrPort"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessRoamHistIpAddress"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessRoamHistTimeStamp"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessStatsUniPktIn"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessStatsUniOctetIn"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessStatsUniPktOut"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessStatsUniOctetOut"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessStatsMultiPktIn"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessStatsMultiOctetIn"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessStatsEncErrPkt"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessStatsEncErrOctet"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessStatsLastRate"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessStatsLastRssi"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessStatsLastSNR"))
)
if mibBuilder.loadTexts:
    ntwsClientSessionCommonGroup.setStatus("obsolete")

ntwsClientSessScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 4, 1, 2, 2, 2)
)
ntwsClientSessScalarsGroup.setObjects(
    ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessTotalSessions")
)
if mibBuilder.loadTexts:
    ntwsClientSessScalarsGroup.setStatus("current")

ntwsClientSessClientSessionTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 4, 1, 2, 2, 3)
)
ntwsClientSessClientSessionTableGroup.setObjects(
      *(("NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessSessionId"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessUsername"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessIpAddress"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessEncryptionType"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessVlan"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessApSerialNum"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessRadioNum"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessAccessType"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessAuthServer"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessPortOrNum"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessVlanTag"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessTimeStamp"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessSsid"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessLoginType"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessDot1xAuthMethod"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessSessionState"))
)
if mibBuilder.loadTexts:
    ntwsClientSessClientSessionTableGroup.setStatus("obsolete")

ntwsClientSessRoamingHistoryTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 4, 1, 2, 2, 4)
)
ntwsClientSessRoamingHistoryTableGroup.setObjects(
      *(("NTWS-CLIENT-SESSION-MIB", "ntwsClSessRoamHistApSerialNum"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessRoamHistRadioNum"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessRoamHistAccessType"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessRoamHistApNumOrPort"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessRoamHistIpAddress"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessRoamHistTimeStamp"))
)
if mibBuilder.loadTexts:
    ntwsClientSessRoamingHistoryTableGroup.setStatus("obsolete")

ntwsClientSessClientSessionStatisticsTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 4, 1, 2, 2, 5)
)
ntwsClientSessClientSessionStatisticsTableGroup.setObjects(
      *(("NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessStatsUniPktIn"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessStatsUniOctetIn"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessStatsUniPktOut"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessStatsUniOctetOut"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessStatsMultiPktIn"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessStatsMultiOctetIn"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessStatsEncErrPkt"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessStatsEncErrOctet"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessStatsLastRate"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessStatsLastRssi"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessStatsLastSNR"))
)
if mibBuilder.loadTexts:
    ntwsClientSessClientSessionStatisticsTableGroup.setStatus("current")

ntwsClientSessClientSessionTableGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 4, 1, 2, 2, 6)
)
ntwsClientSessClientSessionTableGroupRev2.setObjects(
      *(("NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessSessionId"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessUsername"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessIpAddress"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessEncryptionType"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessVlan"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessApSerialNum"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessRadioNum"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessAuthServer"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessVlanTag"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessTimeStamp"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessSsid"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessLoginType"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessDot1xAuthMethod"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessSessionState"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessAccessMode"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessApNum"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessClientSessPhysPortNum"))
)
if mibBuilder.loadTexts:
    ntwsClientSessClientSessionTableGroupRev2.setStatus("current")

ntwsClientSessRoamingHistoryTableGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 4, 1, 2, 2, 7)
)
ntwsClientSessRoamingHistoryTableGroupRev2.setObjects(
      *(("NTWS-CLIENT-SESSION-MIB", "ntwsClSessRoamHistApSerialNum"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessRoamHistRadioNum"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessRoamHistIpAddress"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessRoamHistTimeStamp"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessRoamHistAccessMode"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessRoamHistApNum"),
        ("NTWS-CLIENT-SESSION-MIB", "ntwsClSessRoamHistPhysPortNum"))
)
if mibBuilder.loadTexts:
    ntwsClientSessRoamingHistoryTableGroupRev2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ntwsClientSessionCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 4, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ntwsClientSessionCompliance.setStatus(
        "obsolete"
    )

ntwsClientSessionComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 4, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ntwsClientSessionComplianceRev2.setStatus(
        "obsolete"
    )

ntwsClientSessionComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 4, 1, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ntwsClientSessionComplianceRev3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NTWS-CLIENT-SESSION-MIB",
    **{"NtwsEncryptionType": NtwsEncryptionType,
       "NtwsAuthMethod": NtwsAuthMethod,
       "NtwsSessState": NtwsSessState,
       "ntwsClientSessionMib": ntwsClientSessionMib,
       "ntwsClientSessionObjects": ntwsClientSessionObjects,
       "ntwsClientSessionDataObjects": ntwsClientSessionDataObjects,
       "ntwsClSessClientSessionTable": ntwsClSessClientSessionTable,
       "ntwsClSessClientSessionEntry": ntwsClSessClientSessionEntry,
       "ntwsClSessClientSessMacAddress": ntwsClSessClientSessMacAddress,
       "ntwsClSessClientSessSessionId": ntwsClSessClientSessSessionId,
       "ntwsClSessClientSessUsername": ntwsClSessClientSessUsername,
       "ntwsClSessClientSessIpAddress": ntwsClSessClientSessIpAddress,
       "ntwsClSessClientSessEncryptionType": ntwsClSessClientSessEncryptionType,
       "ntwsClSessClientSessVlan": ntwsClSessClientSessVlan,
       "ntwsClSessClientSessApSerialNum": ntwsClSessClientSessApSerialNum,
       "ntwsClSessClientSessRadioNum": ntwsClSessClientSessRadioNum,
       "ntwsClSessClientSessAccessType": ntwsClSessClientSessAccessType,
       "ntwsClSessClientSessAuthMethod": ntwsClSessClientSessAuthMethod,
       "ntwsClSessClientSessAuthServer": ntwsClSessClientSessAuthServer,
       "ntwsClSessClientSessPortOrNum": ntwsClSessClientSessPortOrNum,
       "ntwsClSessClientSessVlanTag": ntwsClSessClientSessVlanTag,
       "ntwsClSessClientSessTimeStamp": ntwsClSessClientSessTimeStamp,
       "ntwsClSessClientSessSsid": ntwsClSessClientSessSsid,
       "ntwsClSessClientSessState": ntwsClSessClientSessState,
       "ntwsClSessClientSessLoginType": ntwsClSessClientSessLoginType,
       "ntwsClSessClientSessDot1xAuthMethod": ntwsClSessClientSessDot1xAuthMethod,
       "ntwsClSessClientSessSessionState": ntwsClSessClientSessSessionState,
       "ntwsClSessClientSessAccessMode": ntwsClSessClientSessAccessMode,
       "ntwsClSessClientSessApNum": ntwsClSessClientSessApNum,
       "ntwsClSessClientSessPhysPortNum": ntwsClSessClientSessPhysPortNum,
       "ntwsClSessRoamingHistoryTable": ntwsClSessRoamingHistoryTable,
       "ntwsClSessRoamingHistoryEntry": ntwsClSessRoamingHistoryEntry,
       "ntwsClSessRoamHistMacAddress": ntwsClSessRoamHistMacAddress,
       "ntwsClSessRoamHistIndex": ntwsClSessRoamHistIndex,
       "ntwsClSessRoamHistApSerialNum": ntwsClSessRoamHistApSerialNum,
       "ntwsClSessRoamHistRadioNum": ntwsClSessRoamHistRadioNum,
       "ntwsClSessRoamHistAccessType": ntwsClSessRoamHistAccessType,
       "ntwsClSessRoamHistApNumOrPort": ntwsClSessRoamHistApNumOrPort,
       "ntwsClSessRoamHistIpAddress": ntwsClSessRoamHistIpAddress,
       "ntwsClSessRoamHistTimeStamp": ntwsClSessRoamHistTimeStamp,
       "ntwsClSessRoamHistAccessMode": ntwsClSessRoamHistAccessMode,
       "ntwsClSessRoamHistApNum": ntwsClSessRoamHistApNum,
       "ntwsClSessRoamHistPhysPortNum": ntwsClSessRoamHistPhysPortNum,
       "ntwsClSessClientSessionStatisticsTable": ntwsClSessClientSessionStatisticsTable,
       "ntwsClSessClientSessionStatisticsEntry": ntwsClSessClientSessionStatisticsEntry,
       "ntwsClSessClientSessStatsMacAddress": ntwsClSessClientSessStatsMacAddress,
       "ntwsClSessClientSessStatsUniPktIn": ntwsClSessClientSessStatsUniPktIn,
       "ntwsClSessClientSessStatsUniOctetIn": ntwsClSessClientSessStatsUniOctetIn,
       "ntwsClSessClientSessStatsUniPktOut": ntwsClSessClientSessStatsUniPktOut,
       "ntwsClSessClientSessStatsUniOctetOut": ntwsClSessClientSessStatsUniOctetOut,
       "ntwsClSessClientSessStatsMultiPktIn": ntwsClSessClientSessStatsMultiPktIn,
       "ntwsClSessClientSessStatsMultiOctetIn": ntwsClSessClientSessStatsMultiOctetIn,
       "ntwsClSessClientSessStatsEncErrPkt": ntwsClSessClientSessStatsEncErrPkt,
       "ntwsClSessClientSessStatsEncErrOctet": ntwsClSessClientSessStatsEncErrOctet,
       "ntwsClSessClientSessStatsLastRate": ntwsClSessClientSessStatsLastRate,
       "ntwsClSessClientSessStatsLastRssi": ntwsClSessClientSessStatsLastRssi,
       "ntwsClSessClientSessStatsLastSNR": ntwsClSessClientSessStatsLastSNR,
       "ntwsClSessTotalSessions": ntwsClSessTotalSessions,
       "ntwsClientSessionConformance": ntwsClientSessionConformance,
       "ntwsClientSessionCompliances": ntwsClientSessionCompliances,
       "ntwsClientSessionCompliance": ntwsClientSessionCompliance,
       "ntwsClientSessionComplianceRev2": ntwsClientSessionComplianceRev2,
       "ntwsClientSessionComplianceRev3": ntwsClientSessionComplianceRev3,
       "ntwsClientSessionGroups": ntwsClientSessionGroups,
       "ntwsClientSessionCommonGroup": ntwsClientSessionCommonGroup,
       "ntwsClientSessScalarsGroup": ntwsClientSessScalarsGroup,
       "ntwsClientSessClientSessionTableGroup": ntwsClientSessClientSessionTableGroup,
       "ntwsClientSessRoamingHistoryTableGroup": ntwsClientSessRoamingHistoryTableGroup,
       "ntwsClientSessClientSessionStatisticsTableGroup": ntwsClientSessClientSessionStatisticsTableGroup,
       "ntwsClientSessClientSessionTableGroupRev2": ntwsClientSessClientSessionTableGroupRev2,
       "ntwsClientSessRoamingHistoryTableGroupRev2": ntwsClientSessRoamingHistoryTableGroupRev2}
)
