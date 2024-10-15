# SNMP MIB module (RBTWS-CLIENT-SESSION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RBTWS-CLIENT-SESSION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:45:33 2024
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

(RbtwsAccessType,
 RbtwsApNum,
 RbtwsApSerialNum,
 RbtwsRadioNum,
 RbtwsRadioRate,
 RbtwsRssi) = mibBuilder.importSymbols(
    "RBTWS-AP-TC",
    "RbtwsAccessType",
    "RbtwsApNum",
    "RbtwsApSerialNum",
    "RbtwsRadioNum",
    "RbtwsRadioRate",
    "RbtwsRssi")

(RbtwsClientAccessMode,
 RbtwsClientAuthenProtocolType,
 RbtwsClientSessionState,
 RbtwsUserAccessType) = mibBuilder.importSymbols(
    "RBTWS-CLIENT-SESSION-TC",
    "RbtwsClientAccessMode",
    "RbtwsClientAuthenProtocolType",
    "RbtwsClientSessionState",
    "RbtwsUserAccessType")

(rbtwsMibs,) = mibBuilder.importSymbols(
    "RBTWS-ROOT-MIB",
    "rbtwsMibs")

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

rbtwsClientSessionMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 4)
)
rbtwsClientSessionMib.setRevisions(
        ("2008-05-23 00:55",
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



class RbtwsEncryptionType(Integer32, TextualConvention):
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



class RbtwsAuthMethod(Integer32, TextualConvention):
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



class RbtwsSessState(Integer32, TextualConvention):
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

_RbtwsClientSessionObjects_ObjectIdentity = ObjectIdentity
rbtwsClientSessionObjects = _RbtwsClientSessionObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 4, 1)
)
_RbtwsClientSessionDataObjects_ObjectIdentity = ObjectIdentity
rbtwsClientSessionDataObjects = _RbtwsClientSessionDataObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 4, 1, 1)
)
_RbtwsClSessClientSessionTable_Object = MibTable
rbtwsClSessClientSessionTable = _RbtwsClSessClientSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    rbtwsClSessClientSessionTable.setStatus("current")
_RbtwsClSessClientSessionEntry_Object = MibTableRow
rbtwsClSessClientSessionEntry = _RbtwsClSessClientSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 4, 1, 1, 1, 1)
)
rbtwsClSessClientSessionEntry.setIndexNames(
    (0, "RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessMacAddress"),
)
if mibBuilder.loadTexts:
    rbtwsClSessClientSessionEntry.setStatus("current")
_RbtwsClSessClientSessMacAddress_Type = MacAddress
_RbtwsClSessClientSessMacAddress_Object = MibTableColumn
rbtwsClSessClientSessMacAddress = _RbtwsClSessClientSessMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 4, 1, 1, 1, 1, 1),
    _RbtwsClSessClientSessMacAddress_Type()
)
rbtwsClSessClientSessMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbtwsClSessClientSessMacAddress.setStatus("current")


class _RbtwsClSessClientSessSessionId_Type(DisplayString):
    """Custom type rbtwsClSessClientSessSessionId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_RbtwsClSessClientSessSessionId_Type.__name__ = "DisplayString"
_RbtwsClSessClientSessSessionId_Object = MibTableColumn
rbtwsClSessClientSessSessionId = _RbtwsClSessClientSessSessionId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 4, 1, 1, 1, 1, 2),
    _RbtwsClSessClientSessSessionId_Type()
)
rbtwsClSessClientSessSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsClSessClientSessSessionId.setStatus("current")


class _RbtwsClSessClientSessUsername_Type(DisplayString):
    """Custom type rbtwsClSessClientSessUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RbtwsClSessClientSessUsername_Type.__name__ = "DisplayString"
_RbtwsClSessClientSessUsername_Object = MibTableColumn
rbtwsClSessClientSessUsername = _RbtwsClSessClientSessUsername_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 4, 1, 1, 1, 1, 3),
    _RbtwsClSessClientSessUsername_Type()
)
rbtwsClSessClientSessUsername.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsClSessClientSessUsername.setStatus("current")
_RbtwsClSessClientSessIpAddress_Type = IpAddress
_RbtwsClSessClientSessIpAddress_Object = MibTableColumn
rbtwsClSessClientSessIpAddress = _RbtwsClSessClientSessIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 4, 1, 1, 1, 1, 4),
    _RbtwsClSessClientSessIpAddress_Type()
)
rbtwsClSessClientSessIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsClSessClientSessIpAddress.setStatus("current")
_RbtwsClSessClientSessEncryptionType_Type = RbtwsEncryptionType
_RbtwsClSessClientSessEncryptionType_Object = MibTableColumn
rbtwsClSessClientSessEncryptionType = _RbtwsClSessClientSessEncryptionType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 4, 1, 1, 1, 1, 5),
    _RbtwsClSessClientSessEncryptionType_Type()
)
rbtwsClSessClientSessEncryptionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsClSessClientSessEncryptionType.setStatus("current")


class _RbtwsClSessClientSessVlan_Type(DisplayString):
    """Custom type rbtwsClSessClientSessVlan based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RbtwsClSessClientSessVlan_Type.__name__ = "DisplayString"
_RbtwsClSessClientSessVlan_Object = MibTableColumn
rbtwsClSessClientSessVlan = _RbtwsClSessClientSessVlan_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 4, 1, 1, 1, 1, 6),
    _RbtwsClSessClientSessVlan_Type()
)
rbtwsClSessClientSessVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsClSessClientSessVlan.setStatus("current")
_RbtwsClSessClientSessApSerialNum_Type = RbtwsApSerialNum
_RbtwsClSessClientSessApSerialNum_Object = MibTableColumn
rbtwsClSessClientSessApSerialNum = _RbtwsClSessClientSessApSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 4, 1, 1, 1, 1, 7),
    _RbtwsClSessClientSessApSerialNum_Type()
)
rbtwsClSessClientSessApSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsClSessClientSessApSerialNum.setStatus("current")
_RbtwsClSessClientSessRadioNum_Type = RbtwsRadioNum
_RbtwsClSessClientSessRadioNum_Object = MibTableColumn
rbtwsClSessClientSessRadioNum = _RbtwsClSessClientSessRadioNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 4, 1, 1, 1, 1, 8),
    _RbtwsClSessClientSessRadioNum_Type()
)
rbtwsClSessClientSessRadioNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsClSessClientSessRadioNum.setStatus("current")
_RbtwsClSessClientSessAccessType_Type = RbtwsAccessType
_RbtwsClSessClientSessAccessType_Object = MibTableColumn
rbtwsClSessClientSessAccessType = _RbtwsClSessClientSessAccessType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 4, 1, 1, 1, 1, 9),
    _RbtwsClSessClientSessAccessType_Type()
)
rbtwsClSessClientSessAccessType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsClSessClientSessAccessType.setStatus("obsolete")
_RbtwsClSessClientSessAuthMethod_Type = RbtwsAuthMethod
_RbtwsClSessClientSessAuthMethod_Object = MibTableColumn
rbtwsClSessClientSessAuthMethod = _RbtwsClSessClientSessAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 4, 1, 1, 1, 1, 10),
    _RbtwsClSessClientSessAuthMethod_Type()
)
rbtwsClSessClientSessAuthMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsClSessClientSessAuthMethod.setStatus("deprecated")
_RbtwsClSessClientSessAuthServer_Type = IpAddress
_RbtwsClSessClientSessAuthServer_Object = MibTableColumn
rbtwsClSessClientSessAuthServer = _RbtwsClSessClientSessAuthServer_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 4, 1, 1, 1, 1, 11),
    _RbtwsClSessClientSessAuthServer_Type()
)
rbtwsClSessClientSessAuthServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsClSessClientSessAuthServer.setStatus("current")
_RbtwsClSessClientSessPortOrNum_Type = Unsigned32
_RbtwsClSessClientSessPortOrNum_Object = MibTableColumn
rbtwsClSessClientSessPortOrNum = _RbtwsClSessClientSessPortOrNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 4, 1, 1, 1, 1, 12),
    _RbtwsClSessClientSessPortOrNum_Type()
)
rbtwsClSessClientSessPortOrNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsClSessClientSessPortOrNum.setStatus("obsolete")
_RbtwsClSessClientSessVlanTag_Type = Unsigned32
_RbtwsClSessClientSessVlanTag_Object = MibTableColumn
rbtwsClSessClientSessVlanTag = _RbtwsClSessClientSessVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 4, 1, 1, 1, 1, 13),
    _RbtwsClSessClientSessVlanTag_Type()
)
rbtwsClSessClientSessVlanTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsClSessClientSessVlanTag.setStatus("current")
_RbtwsClSessClientSessTimeStamp_Type = TimeStamp
_RbtwsClSessClientSessTimeStamp_Object = MibTableColumn
rbtwsClSessClientSessTimeStamp = _RbtwsClSessClientSessTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 4, 1, 1, 1, 1, 14),
    _RbtwsClSessClientSessTimeStamp_Type()
)
rbtwsClSessClientSessTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsClSessClientSessTimeStamp.setStatus("current")


class _RbtwsClSessClientSessSsid_Type(DisplayString):
    """Custom type rbtwsClSessClientSessSsid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 33),
    )


_RbtwsClSessClientSessSsid_Type.__name__ = "DisplayString"
_RbtwsClSessClientSessSsid_Object = MibTableColumn
rbtwsClSessClientSessSsid = _RbtwsClSessClientSessSsid_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 4, 1, 1, 1, 1, 15),
    _RbtwsClSessClientSessSsid_Type()
)
rbtwsClSessClientSessSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsClSessClientSessSsid.setStatus("current")
_RbtwsClSessClientSessState_Type = RbtwsSessState
_RbtwsClSessClientSessState_Object = MibTableColumn
rbtwsClSessClientSessState = _RbtwsClSessClientSessState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 4, 1, 1, 1, 1, 16),
    _RbtwsClSessClientSessState_Type()
)
rbtwsClSessClientSessState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsClSessClientSessState.setStatus("deprecated")
_RbtwsClSessClientSessLoginType_Type = RbtwsUserAccessType
_RbtwsClSessClientSessLoginType_Object = MibTableColumn
rbtwsClSessClientSessLoginType = _RbtwsClSessClientSessLoginType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 4, 1, 1, 1, 1, 17),
    _RbtwsClSessClientSessLoginType_Type()
)
rbtwsClSessClientSessLoginType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsClSessClientSessLoginType.setStatus("current")
_RbtwsClSessClientSessDot1xAuthMethod_Type = RbtwsClientAuthenProtocolType
_RbtwsClSessClientSessDot1xAuthMethod_Object = MibTableColumn
rbtwsClSessClientSessDot1xAuthMethod = _RbtwsClSessClientSessDot1xAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 4, 1, 1, 1, 1, 18),
    _RbtwsClSessClientSessDot1xAuthMethod_Type()
)
rbtwsClSessClientSessDot1xAuthMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsClSessClientSessDot1xAuthMethod.setStatus("current")
_RbtwsClSessClientSessSessionState_Type = RbtwsClientSessionState
_RbtwsClSessClientSessSessionState_Object = MibTableColumn
rbtwsClSessClientSessSessionState = _RbtwsClSessClientSessSessionState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 4, 1, 1, 1, 1, 19),
    _RbtwsClSessClientSessSessionState_Type()
)
rbtwsClSessClientSessSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsClSessClientSessSessionState.setStatus("current")
_RbtwsClSessClientSessAccessMode_Type = RbtwsClientAccessMode
_RbtwsClSessClientSessAccessMode_Object = MibTableColumn
rbtwsClSessClientSessAccessMode = _RbtwsClSessClientSessAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 4, 1, 1, 1, 1, 20),
    _RbtwsClSessClientSessAccessMode_Type()
)
rbtwsClSessClientSessAccessMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsClSessClientSessAccessMode.setStatus("current")
_RbtwsClSessClientSessApNum_Type = RbtwsApNum
_RbtwsClSessClientSessApNum_Object = MibTableColumn
rbtwsClSessClientSessApNum = _RbtwsClSessClientSessApNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 4, 1, 1, 1, 1, 21),
    _RbtwsClSessClientSessApNum_Type()
)
rbtwsClSessClientSessApNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsClSessClientSessApNum.setStatus("current")


class _RbtwsClSessClientSessPhysPortNum_Type(Unsigned32):
    """Custom type rbtwsClSessClientSessPhysPortNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_RbtwsClSessClientSessPhysPortNum_Type.__name__ = "Unsigned32"
_RbtwsClSessClientSessPhysPortNum_Object = MibTableColumn
rbtwsClSessClientSessPhysPortNum = _RbtwsClSessClientSessPhysPortNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 4, 1, 1, 1, 1, 22),
    _RbtwsClSessClientSessPhysPortNum_Type()
)
rbtwsClSessClientSessPhysPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsClSessClientSessPhysPortNum.setStatus("current")
_RbtwsClSessRoamingHistoryTable_Object = MibTable
rbtwsClSessRoamingHistoryTable = _RbtwsClSessRoamingHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 4, 1, 1, 2)
)
if mibBuilder.loadTexts:
    rbtwsClSessRoamingHistoryTable.setStatus("current")
_RbtwsClSessRoamingHistoryEntry_Object = MibTableRow
rbtwsClSessRoamingHistoryEntry = _RbtwsClSessRoamingHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 4, 1, 1, 2, 1)
)
rbtwsClSessRoamingHistoryEntry.setIndexNames(
    (0, "RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessRoamHistMacAddress"),
    (0, "RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessRoamHistIndex"),
)
if mibBuilder.loadTexts:
    rbtwsClSessRoamingHistoryEntry.setStatus("current")
_RbtwsClSessRoamHistMacAddress_Type = MacAddress
_RbtwsClSessRoamHistMacAddress_Object = MibTableColumn
rbtwsClSessRoamHistMacAddress = _RbtwsClSessRoamHistMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 4, 1, 1, 2, 1, 1),
    _RbtwsClSessRoamHistMacAddress_Type()
)
rbtwsClSessRoamHistMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbtwsClSessRoamHistMacAddress.setStatus("current")
_RbtwsClSessRoamHistIndex_Type = Unsigned32
_RbtwsClSessRoamHistIndex_Object = MibTableColumn
rbtwsClSessRoamHistIndex = _RbtwsClSessRoamHistIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 4, 1, 1, 2, 1, 2),
    _RbtwsClSessRoamHistIndex_Type()
)
rbtwsClSessRoamHistIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbtwsClSessRoamHistIndex.setStatus("current")
_RbtwsClSessRoamHistApSerialNum_Type = RbtwsApSerialNum
_RbtwsClSessRoamHistApSerialNum_Object = MibTableColumn
rbtwsClSessRoamHistApSerialNum = _RbtwsClSessRoamHistApSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 4, 1, 1, 2, 1, 3),
    _RbtwsClSessRoamHistApSerialNum_Type()
)
rbtwsClSessRoamHistApSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsClSessRoamHistApSerialNum.setStatus("current")
_RbtwsClSessRoamHistRadioNum_Type = RbtwsRadioNum
_RbtwsClSessRoamHistRadioNum_Object = MibTableColumn
rbtwsClSessRoamHistRadioNum = _RbtwsClSessRoamHistRadioNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 4, 1, 1, 2, 1, 4),
    _RbtwsClSessRoamHistRadioNum_Type()
)
rbtwsClSessRoamHistRadioNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsClSessRoamHistRadioNum.setStatus("current")
_RbtwsClSessRoamHistAccessType_Type = RbtwsAccessType
_RbtwsClSessRoamHistAccessType_Object = MibTableColumn
rbtwsClSessRoamHistAccessType = _RbtwsClSessRoamHistAccessType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 4, 1, 1, 2, 1, 5),
    _RbtwsClSessRoamHistAccessType_Type()
)
rbtwsClSessRoamHistAccessType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsClSessRoamHistAccessType.setStatus("obsolete")
_RbtwsClSessRoamHistApNumOrPort_Type = Unsigned32
_RbtwsClSessRoamHistApNumOrPort_Object = MibTableColumn
rbtwsClSessRoamHistApNumOrPort = _RbtwsClSessRoamHistApNumOrPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 4, 1, 1, 2, 1, 6),
    _RbtwsClSessRoamHistApNumOrPort_Type()
)
rbtwsClSessRoamHistApNumOrPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsClSessRoamHistApNumOrPort.setStatus("obsolete")
_RbtwsClSessRoamHistIpAddress_Type = IpAddress
_RbtwsClSessRoamHistIpAddress_Object = MibTableColumn
rbtwsClSessRoamHistIpAddress = _RbtwsClSessRoamHistIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 4, 1, 1, 2, 1, 7),
    _RbtwsClSessRoamHistIpAddress_Type()
)
rbtwsClSessRoamHistIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsClSessRoamHistIpAddress.setStatus("current")
_RbtwsClSessRoamHistTimeStamp_Type = TimeStamp
_RbtwsClSessRoamHistTimeStamp_Object = MibTableColumn
rbtwsClSessRoamHistTimeStamp = _RbtwsClSessRoamHistTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 4, 1, 1, 2, 1, 8),
    _RbtwsClSessRoamHistTimeStamp_Type()
)
rbtwsClSessRoamHistTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsClSessRoamHistTimeStamp.setStatus("current")
_RbtwsClSessRoamHistAccessMode_Type = RbtwsClientAccessMode
_RbtwsClSessRoamHistAccessMode_Object = MibTableColumn
rbtwsClSessRoamHistAccessMode = _RbtwsClSessRoamHistAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 4, 1, 1, 2, 1, 9),
    _RbtwsClSessRoamHistAccessMode_Type()
)
rbtwsClSessRoamHistAccessMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsClSessRoamHistAccessMode.setStatus("current")
_RbtwsClSessRoamHistApNum_Type = RbtwsApNum
_RbtwsClSessRoamHistApNum_Object = MibTableColumn
rbtwsClSessRoamHistApNum = _RbtwsClSessRoamHistApNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 4, 1, 1, 2, 1, 10),
    _RbtwsClSessRoamHistApNum_Type()
)
rbtwsClSessRoamHistApNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsClSessRoamHistApNum.setStatus("current")


class _RbtwsClSessRoamHistPhysPortNum_Type(Unsigned32):
    """Custom type rbtwsClSessRoamHistPhysPortNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_RbtwsClSessRoamHistPhysPortNum_Type.__name__ = "Unsigned32"
_RbtwsClSessRoamHistPhysPortNum_Object = MibTableColumn
rbtwsClSessRoamHistPhysPortNum = _RbtwsClSessRoamHistPhysPortNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 4, 1, 1, 2, 1, 11),
    _RbtwsClSessRoamHistPhysPortNum_Type()
)
rbtwsClSessRoamHistPhysPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsClSessRoamHistPhysPortNum.setStatus("current")
_RbtwsClSessClientSessionStatisticsTable_Object = MibTable
rbtwsClSessClientSessionStatisticsTable = _RbtwsClSessClientSessionStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 4, 1, 1, 3)
)
if mibBuilder.loadTexts:
    rbtwsClSessClientSessionStatisticsTable.setStatus("current")
_RbtwsClSessClientSessionStatisticsEntry_Object = MibTableRow
rbtwsClSessClientSessionStatisticsEntry = _RbtwsClSessClientSessionStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 4, 1, 1, 3, 1)
)
rbtwsClSessClientSessionStatisticsEntry.setIndexNames(
    (0, "RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessStatsMacAddress"),
)
if mibBuilder.loadTexts:
    rbtwsClSessClientSessionStatisticsEntry.setStatus("current")
_RbtwsClSessClientSessStatsMacAddress_Type = MacAddress
_RbtwsClSessClientSessStatsMacAddress_Object = MibTableColumn
rbtwsClSessClientSessStatsMacAddress = _RbtwsClSessClientSessStatsMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 4, 1, 1, 3, 1, 1),
    _RbtwsClSessClientSessStatsMacAddress_Type()
)
rbtwsClSessClientSessStatsMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbtwsClSessClientSessStatsMacAddress.setStatus("current")
_RbtwsClSessClientSessStatsUniPktIn_Type = Counter64
_RbtwsClSessClientSessStatsUniPktIn_Object = MibTableColumn
rbtwsClSessClientSessStatsUniPktIn = _RbtwsClSessClientSessStatsUniPktIn_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 4, 1, 1, 3, 1, 2),
    _RbtwsClSessClientSessStatsUniPktIn_Type()
)
rbtwsClSessClientSessStatsUniPktIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsClSessClientSessStatsUniPktIn.setStatus("current")
_RbtwsClSessClientSessStatsUniOctetIn_Type = Counter64
_RbtwsClSessClientSessStatsUniOctetIn_Object = MibTableColumn
rbtwsClSessClientSessStatsUniOctetIn = _RbtwsClSessClientSessStatsUniOctetIn_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 4, 1, 1, 3, 1, 3),
    _RbtwsClSessClientSessStatsUniOctetIn_Type()
)
rbtwsClSessClientSessStatsUniOctetIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsClSessClientSessStatsUniOctetIn.setStatus("current")
_RbtwsClSessClientSessStatsUniPktOut_Type = Counter64
_RbtwsClSessClientSessStatsUniPktOut_Object = MibTableColumn
rbtwsClSessClientSessStatsUniPktOut = _RbtwsClSessClientSessStatsUniPktOut_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 4, 1, 1, 3, 1, 4),
    _RbtwsClSessClientSessStatsUniPktOut_Type()
)
rbtwsClSessClientSessStatsUniPktOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsClSessClientSessStatsUniPktOut.setStatus("current")
_RbtwsClSessClientSessStatsUniOctetOut_Type = Counter64
_RbtwsClSessClientSessStatsUniOctetOut_Object = MibTableColumn
rbtwsClSessClientSessStatsUniOctetOut = _RbtwsClSessClientSessStatsUniOctetOut_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 4, 1, 1, 3, 1, 5),
    _RbtwsClSessClientSessStatsUniOctetOut_Type()
)
rbtwsClSessClientSessStatsUniOctetOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsClSessClientSessStatsUniOctetOut.setStatus("current")
_RbtwsClSessClientSessStatsMultiPktIn_Type = Counter64
_RbtwsClSessClientSessStatsMultiPktIn_Object = MibTableColumn
rbtwsClSessClientSessStatsMultiPktIn = _RbtwsClSessClientSessStatsMultiPktIn_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 4, 1, 1, 3, 1, 6),
    _RbtwsClSessClientSessStatsMultiPktIn_Type()
)
rbtwsClSessClientSessStatsMultiPktIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsClSessClientSessStatsMultiPktIn.setStatus("current")
_RbtwsClSessClientSessStatsMultiOctetIn_Type = Counter64
_RbtwsClSessClientSessStatsMultiOctetIn_Object = MibTableColumn
rbtwsClSessClientSessStatsMultiOctetIn = _RbtwsClSessClientSessStatsMultiOctetIn_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 4, 1, 1, 3, 1, 7),
    _RbtwsClSessClientSessStatsMultiOctetIn_Type()
)
rbtwsClSessClientSessStatsMultiOctetIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsClSessClientSessStatsMultiOctetIn.setStatus("current")
_RbtwsClSessClientSessStatsEncErrPkt_Type = Counter64
_RbtwsClSessClientSessStatsEncErrPkt_Object = MibTableColumn
rbtwsClSessClientSessStatsEncErrPkt = _RbtwsClSessClientSessStatsEncErrPkt_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 4, 1, 1, 3, 1, 8),
    _RbtwsClSessClientSessStatsEncErrPkt_Type()
)
rbtwsClSessClientSessStatsEncErrPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsClSessClientSessStatsEncErrPkt.setStatus("current")
_RbtwsClSessClientSessStatsEncErrOctet_Type = Counter64
_RbtwsClSessClientSessStatsEncErrOctet_Object = MibTableColumn
rbtwsClSessClientSessStatsEncErrOctet = _RbtwsClSessClientSessStatsEncErrOctet_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 4, 1, 1, 3, 1, 9),
    _RbtwsClSessClientSessStatsEncErrOctet_Type()
)
rbtwsClSessClientSessStatsEncErrOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsClSessClientSessStatsEncErrOctet.setStatus("current")
_RbtwsClSessClientSessStatsLastRate_Type = RbtwsRadioRate
_RbtwsClSessClientSessStatsLastRate_Object = MibTableColumn
rbtwsClSessClientSessStatsLastRate = _RbtwsClSessClientSessStatsLastRate_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 4, 1, 1, 3, 1, 10),
    _RbtwsClSessClientSessStatsLastRate_Type()
)
rbtwsClSessClientSessStatsLastRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsClSessClientSessStatsLastRate.setStatus("current")
_RbtwsClSessClientSessStatsLastRssi_Type = RbtwsRssi
_RbtwsClSessClientSessStatsLastRssi_Object = MibTableColumn
rbtwsClSessClientSessStatsLastRssi = _RbtwsClSessClientSessStatsLastRssi_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 4, 1, 1, 3, 1, 11),
    _RbtwsClSessClientSessStatsLastRssi_Type()
)
rbtwsClSessClientSessStatsLastRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsClSessClientSessStatsLastRssi.setStatus("current")
_RbtwsClSessClientSessStatsLastSNR_Type = Integer32
_RbtwsClSessClientSessStatsLastSNR_Object = MibTableColumn
rbtwsClSessClientSessStatsLastSNR = _RbtwsClSessClientSessStatsLastSNR_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 4, 1, 1, 3, 1, 12),
    _RbtwsClSessClientSessStatsLastSNR_Type()
)
rbtwsClSessClientSessStatsLastSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsClSessClientSessStatsLastSNR.setStatus("current")
_RbtwsClSessTotalSessions_Type = Unsigned32
_RbtwsClSessTotalSessions_Object = MibScalar
rbtwsClSessTotalSessions = _RbtwsClSessTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 4, 1, 1, 4),
    _RbtwsClSessTotalSessions_Type()
)
rbtwsClSessTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsClSessTotalSessions.setStatus("current")
_RbtwsClientSessionConformance_ObjectIdentity = ObjectIdentity
rbtwsClientSessionConformance = _RbtwsClientSessionConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 4, 1, 2)
)
_RbtwsClientSessionCompliances_ObjectIdentity = ObjectIdentity
rbtwsClientSessionCompliances = _RbtwsClientSessionCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 4, 1, 2, 1)
)
_RbtwsClientSessionGroups_ObjectIdentity = ObjectIdentity
rbtwsClientSessionGroups = _RbtwsClientSessionGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 4, 1, 2, 2)
)

# Managed Objects groups

rbtwsClientSessionCommonGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 4, 1, 2, 2, 1)
)
rbtwsClientSessionCommonGroup.setObjects(
      *(("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessSessionId"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessUsername"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessIpAddress"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessEncryptionType"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessVlan"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessApSerialNum"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessRadioNum"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessAccessType"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessAuthMethod"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessAuthServer"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessPortOrNum"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessVlanTag"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessTimeStamp"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessSsid"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessState"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessRoamHistApSerialNum"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessRoamHistRadioNum"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessRoamHistAccessType"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessRoamHistApNumOrPort"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessRoamHistIpAddress"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessRoamHistTimeStamp"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessStatsUniPktIn"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessStatsUniOctetIn"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessStatsUniPktOut"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessStatsUniOctetOut"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessStatsMultiPktIn"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessStatsMultiOctetIn"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessStatsEncErrPkt"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessStatsEncErrOctet"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessStatsLastRate"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessStatsLastRssi"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessStatsLastSNR"))
)
if mibBuilder.loadTexts:
    rbtwsClientSessionCommonGroup.setStatus("obsolete")

rbtwsClientSessScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 4, 1, 2, 2, 2)
)
rbtwsClientSessScalarsGroup.setObjects(
    ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessTotalSessions")
)
if mibBuilder.loadTexts:
    rbtwsClientSessScalarsGroup.setStatus("current")

rbtwsClientSessClientSessionTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 4, 1, 2, 2, 3)
)
rbtwsClientSessClientSessionTableGroup.setObjects(
      *(("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessSessionId"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessUsername"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessIpAddress"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessEncryptionType"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessVlan"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessApSerialNum"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessRadioNum"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessAccessType"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessAuthServer"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessPortOrNum"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessVlanTag"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessTimeStamp"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessSsid"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessLoginType"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessDot1xAuthMethod"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessSessionState"))
)
if mibBuilder.loadTexts:
    rbtwsClientSessClientSessionTableGroup.setStatus("obsolete")

rbtwsClientSessRoamingHistoryTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 4, 1, 2, 2, 4)
)
rbtwsClientSessRoamingHistoryTableGroup.setObjects(
      *(("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessRoamHistApSerialNum"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessRoamHistRadioNum"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessRoamHistAccessType"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessRoamHistApNumOrPort"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessRoamHistIpAddress"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessRoamHistTimeStamp"))
)
if mibBuilder.loadTexts:
    rbtwsClientSessRoamingHistoryTableGroup.setStatus("obsolete")

rbtwsClientSessClientSessionStatisticsTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 4, 1, 2, 2, 5)
)
rbtwsClientSessClientSessionStatisticsTableGroup.setObjects(
      *(("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessStatsUniPktIn"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessStatsUniOctetIn"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessStatsUniPktOut"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessStatsUniOctetOut"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessStatsMultiPktIn"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessStatsMultiOctetIn"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessStatsEncErrPkt"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessStatsEncErrOctet"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessStatsLastRate"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessStatsLastRssi"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessStatsLastSNR"))
)
if mibBuilder.loadTexts:
    rbtwsClientSessClientSessionStatisticsTableGroup.setStatus("current")

rbtwsClientSessClientSessionTableGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 4, 1, 2, 2, 6)
)
rbtwsClientSessClientSessionTableGroupRev2.setObjects(
      *(("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessSessionId"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessUsername"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessIpAddress"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessEncryptionType"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessVlan"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessApSerialNum"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessRadioNum"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessAuthServer"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessVlanTag"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessTimeStamp"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessSsid"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessLoginType"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessDot1xAuthMethod"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessSessionState"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessAccessMode"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessApNum"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessClientSessPhysPortNum"))
)
if mibBuilder.loadTexts:
    rbtwsClientSessClientSessionTableGroupRev2.setStatus("current")

rbtwsClientSessRoamingHistoryTableGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 4, 1, 2, 2, 7)
)
rbtwsClientSessRoamingHistoryTableGroupRev2.setObjects(
      *(("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessRoamHistApSerialNum"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessRoamHistRadioNum"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessRoamHistIpAddress"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessRoamHistTimeStamp"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessRoamHistAccessMode"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessRoamHistApNum"),
        ("RBTWS-CLIENT-SESSION-MIB", "rbtwsClSessRoamHistPhysPortNum"))
)
if mibBuilder.loadTexts:
    rbtwsClientSessRoamingHistoryTableGroupRev2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rbtwsClientSessionCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 4, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rbtwsClientSessionCompliance.setStatus(
        "obsolete"
    )

rbtwsClientSessionComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 4, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    rbtwsClientSessionComplianceRev2.setStatus(
        "obsolete"
    )

rbtwsClientSessionComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 4, 1, 2, 1, 3)
)
if mibBuilder.loadTexts:
    rbtwsClientSessionComplianceRev3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBTWS-CLIENT-SESSION-MIB",
    **{"RbtwsEncryptionType": RbtwsEncryptionType,
       "RbtwsAuthMethod": RbtwsAuthMethod,
       "RbtwsSessState": RbtwsSessState,
       "rbtwsClientSessionMib": rbtwsClientSessionMib,
       "rbtwsClientSessionObjects": rbtwsClientSessionObjects,
       "rbtwsClientSessionDataObjects": rbtwsClientSessionDataObjects,
       "rbtwsClSessClientSessionTable": rbtwsClSessClientSessionTable,
       "rbtwsClSessClientSessionEntry": rbtwsClSessClientSessionEntry,
       "rbtwsClSessClientSessMacAddress": rbtwsClSessClientSessMacAddress,
       "rbtwsClSessClientSessSessionId": rbtwsClSessClientSessSessionId,
       "rbtwsClSessClientSessUsername": rbtwsClSessClientSessUsername,
       "rbtwsClSessClientSessIpAddress": rbtwsClSessClientSessIpAddress,
       "rbtwsClSessClientSessEncryptionType": rbtwsClSessClientSessEncryptionType,
       "rbtwsClSessClientSessVlan": rbtwsClSessClientSessVlan,
       "rbtwsClSessClientSessApSerialNum": rbtwsClSessClientSessApSerialNum,
       "rbtwsClSessClientSessRadioNum": rbtwsClSessClientSessRadioNum,
       "rbtwsClSessClientSessAccessType": rbtwsClSessClientSessAccessType,
       "rbtwsClSessClientSessAuthMethod": rbtwsClSessClientSessAuthMethod,
       "rbtwsClSessClientSessAuthServer": rbtwsClSessClientSessAuthServer,
       "rbtwsClSessClientSessPortOrNum": rbtwsClSessClientSessPortOrNum,
       "rbtwsClSessClientSessVlanTag": rbtwsClSessClientSessVlanTag,
       "rbtwsClSessClientSessTimeStamp": rbtwsClSessClientSessTimeStamp,
       "rbtwsClSessClientSessSsid": rbtwsClSessClientSessSsid,
       "rbtwsClSessClientSessState": rbtwsClSessClientSessState,
       "rbtwsClSessClientSessLoginType": rbtwsClSessClientSessLoginType,
       "rbtwsClSessClientSessDot1xAuthMethod": rbtwsClSessClientSessDot1xAuthMethod,
       "rbtwsClSessClientSessSessionState": rbtwsClSessClientSessSessionState,
       "rbtwsClSessClientSessAccessMode": rbtwsClSessClientSessAccessMode,
       "rbtwsClSessClientSessApNum": rbtwsClSessClientSessApNum,
       "rbtwsClSessClientSessPhysPortNum": rbtwsClSessClientSessPhysPortNum,
       "rbtwsClSessRoamingHistoryTable": rbtwsClSessRoamingHistoryTable,
       "rbtwsClSessRoamingHistoryEntry": rbtwsClSessRoamingHistoryEntry,
       "rbtwsClSessRoamHistMacAddress": rbtwsClSessRoamHistMacAddress,
       "rbtwsClSessRoamHistIndex": rbtwsClSessRoamHistIndex,
       "rbtwsClSessRoamHistApSerialNum": rbtwsClSessRoamHistApSerialNum,
       "rbtwsClSessRoamHistRadioNum": rbtwsClSessRoamHistRadioNum,
       "rbtwsClSessRoamHistAccessType": rbtwsClSessRoamHistAccessType,
       "rbtwsClSessRoamHistApNumOrPort": rbtwsClSessRoamHistApNumOrPort,
       "rbtwsClSessRoamHistIpAddress": rbtwsClSessRoamHistIpAddress,
       "rbtwsClSessRoamHistTimeStamp": rbtwsClSessRoamHistTimeStamp,
       "rbtwsClSessRoamHistAccessMode": rbtwsClSessRoamHistAccessMode,
       "rbtwsClSessRoamHistApNum": rbtwsClSessRoamHistApNum,
       "rbtwsClSessRoamHistPhysPortNum": rbtwsClSessRoamHistPhysPortNum,
       "rbtwsClSessClientSessionStatisticsTable": rbtwsClSessClientSessionStatisticsTable,
       "rbtwsClSessClientSessionStatisticsEntry": rbtwsClSessClientSessionStatisticsEntry,
       "rbtwsClSessClientSessStatsMacAddress": rbtwsClSessClientSessStatsMacAddress,
       "rbtwsClSessClientSessStatsUniPktIn": rbtwsClSessClientSessStatsUniPktIn,
       "rbtwsClSessClientSessStatsUniOctetIn": rbtwsClSessClientSessStatsUniOctetIn,
       "rbtwsClSessClientSessStatsUniPktOut": rbtwsClSessClientSessStatsUniPktOut,
       "rbtwsClSessClientSessStatsUniOctetOut": rbtwsClSessClientSessStatsUniOctetOut,
       "rbtwsClSessClientSessStatsMultiPktIn": rbtwsClSessClientSessStatsMultiPktIn,
       "rbtwsClSessClientSessStatsMultiOctetIn": rbtwsClSessClientSessStatsMultiOctetIn,
       "rbtwsClSessClientSessStatsEncErrPkt": rbtwsClSessClientSessStatsEncErrPkt,
       "rbtwsClSessClientSessStatsEncErrOctet": rbtwsClSessClientSessStatsEncErrOctet,
       "rbtwsClSessClientSessStatsLastRate": rbtwsClSessClientSessStatsLastRate,
       "rbtwsClSessClientSessStatsLastRssi": rbtwsClSessClientSessStatsLastRssi,
       "rbtwsClSessClientSessStatsLastSNR": rbtwsClSessClientSessStatsLastSNR,
       "rbtwsClSessTotalSessions": rbtwsClSessTotalSessions,
       "rbtwsClientSessionConformance": rbtwsClientSessionConformance,
       "rbtwsClientSessionCompliances": rbtwsClientSessionCompliances,
       "rbtwsClientSessionCompliance": rbtwsClientSessionCompliance,
       "rbtwsClientSessionComplianceRev2": rbtwsClientSessionComplianceRev2,
       "rbtwsClientSessionComplianceRev3": rbtwsClientSessionComplianceRev3,
       "rbtwsClientSessionGroups": rbtwsClientSessionGroups,
       "rbtwsClientSessionCommonGroup": rbtwsClientSessionCommonGroup,
       "rbtwsClientSessScalarsGroup": rbtwsClientSessScalarsGroup,
       "rbtwsClientSessClientSessionTableGroup": rbtwsClientSessClientSessionTableGroup,
       "rbtwsClientSessRoamingHistoryTableGroup": rbtwsClientSessRoamingHistoryTableGroup,
       "rbtwsClientSessClientSessionStatisticsTableGroup": rbtwsClientSessClientSessionStatisticsTableGroup,
       "rbtwsClientSessClientSessionTableGroupRev2": rbtwsClientSessClientSessionTableGroupRev2,
       "rbtwsClientSessRoamingHistoryTableGroupRev2": rbtwsClientSessRoamingHistoryTableGroupRev2}
)
