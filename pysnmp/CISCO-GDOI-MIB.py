# SNMP MIB module (CISCO-GDOI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-GDOI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:00:46 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CiscoMilliSeconds,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoMilliSeconds")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoGdoiMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 759)
)
ciscoGdoiMIB.setRevisions(
        ("2015-07-17 00:00",
         "2010-08-31 00:00",
         "2010-07-20 12:40",
         "2010-06-02 12:45",
         "2010-02-25 05:45")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CgmGdoiKsStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("keyServerAlive", 1),
          ("keyServerDead", 2),
          ("keyServerUnknown", 3))
    )



class CgmGdoiKsRole(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("keyServerPrimary", 1),
          ("keyServerSecondary", 2),
          ("keyServerUnknown", 3))
    )



class CgmGdoiIdentificationType(Integer32, TextualConvention):
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
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("caDistinguishedName", 9),
          ("caGeneralName", 10),
          ("domainName", 2),
          ("groupNumber", 11),
          ("ipv4Address", 1),
          ("ipv4Range", 7),
          ("ipv4Subnet", 4),
          ("ipv6Address", 5),
          ("ipv6Range", 8),
          ("ipv6Subnet", 6),
          ("userName", 3))
    )



class CgmGdoiIdentificationValue(OctetString, TextualConvention):
    status = "current"
    displayHint = "255d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )



class CgmGdoiKekSPI(OctetString, TextualConvention):
    status = "current"
    displayHint = "16x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )



class CgmGdoiIpProtocolId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipProtocolTCP", 1),
          ("ipProtocolUDP", 2),
          ("ipProtocolUnknown", 0))
    )



class CgmGdoiKeyManagementAlgorithm(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("keyMgmtLkh", 1),
          ("keyMgmtNone", 0))
    )



class CgmGdoiEncryptionAlgorithm(Integer32, TextualConvention):
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
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              18,
              19,
              20,
              21,
              23,
              24,
              25,
              26,
              27,
              28)
        )
    )
    namedValues = NamedValues(
        *(("encrAlg3Des", 3),
          ("encrAlg3Idea", 8),
          ("encrAlgAesCbc", 12),
          ("encrAlgAesCcm12", 15),
          ("encrAlgAesCcm16", 16),
          ("encrAlgAesCcm8", 14),
          ("encrAlgAesCtr", 13),
          ("encrAlgAesGcm12", 19),
          ("encrAlgAesGcm16", 20),
          ("encrAlgAesGcm8", 18),
          ("encrAlgBlowfish", 7),
          ("encrAlgCamelliaCbc", 23),
          ("encrAlgCamelliaCcm1", 27),
          ("encrAlgCamelliaCcm12", 26),
          ("encrAlgCamelliaCcm8", 25),
          ("encrAlgCamelliaCtr", 24),
          ("encrAlgCast", 6),
          ("encrAlgDes", 2),
          ("encrAlgDes32", 9),
          ("encrAlgDes64", 1),
          ("encrAlgIdea", 5),
          ("encrAlgNone", 0),
          ("encrAlgNull", 11),
          ("encrAlgNullAuthAesGmac", 21),
          ("encrAlgRc4", 10),
          ("encrAlgRc5", 4),
          ("encrAlgSeedCbc", 28))
    )



class CgmGdoiPseudoRandomFunction(Integer32, TextualConvention):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("prfAes128Cmac", 8),
          ("prfAes128Xcbc", 4),
          ("prfMd5Hmac", 1),
          ("prfNone", 0),
          ("prfSha1Hmac", 2),
          ("prfSha2Hmac256", 5),
          ("prfSha2Hmac384", 6),
          ("prfSha2Hmac512", 7),
          ("prfTigerHmac", 3))
    )



class CgmGdoiIntegrityAlgorithm(Integer32, TextualConvention):
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
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("authAlgAes128Gmac", 9),
          ("authAlgAes192Gmac", 10),
          ("authAlgAes256Gmac", 11),
          ("authAlgAesCmac96", 8),
          ("authAlgAesXcbc96", 5),
          ("authAlgDesMac", 3),
          ("authAlgMd5Hmac128", 6),
          ("authAlgMd5Hmac96", 1),
          ("authAlgMd5Kpdk", 4),
          ("authAlgNone", 0),
          ("authAlgSha1Hmac160", 7),
          ("authAlgSha1Hmac96", 2),
          ("authAlgSha2Hmac256to128", 12),
          ("authAlgSha2Hmac384to192", 13),
          ("authAlgSha2Hmac512to256", 14))
    )



class CgmGdoiSignatureMethod(Integer32, TextualConvention):
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
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("sigDss", 3),
          ("sigEcdsa256", 9),
          ("sigEcdsa384", 10),
          ("sigEcdsa512", 11),
          ("sigEncryptRsa", 4),
          ("sigNone", 0),
          ("sigRevEncryptRsa", 5),
          ("sigRsa", 1),
          ("sigSharedKey", 2))
    )



class CgmGdoiDiffieHellmanGroup(Integer32, TextualConvention):
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
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26)
        )
    )
    namedValues = NamedValues(
        *(("dh1024Modp160", 22),
          ("dh1536Modp", 5),
          ("dh2048Modp", 14),
          ("dh2048Modp224", 23),
          ("dh2048Modp256", 24),
          ("dh3072Modp", 15),
          ("dh4096Modp", 16),
          ("dh6144Modp", 17),
          ("dh8192Modp", 18),
          ("dhEc2nGp155", 3),
          ("dhEc2nGp185", 4),
          ("dhEcp192", 25),
          ("dhEcp224", 26),
          ("dhEcp256", 19),
          ("dhEcp521", 21),
          ("dhEcp84", 20),
          ("dhGroup1", 1),
          ("dhGroup2", 2),
          ("dhNone", 0))
    )



class CgmGdoiEncapsulationMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("encapTransport", 2),
          ("encapTunnel", 1),
          ("encapUdpTransport", 4),
          ("encapUdpTunnel", 3),
          ("encapUnknown", 0))
    )



class CgmGdoiSecurityProtocol(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("secProtocolIpsecEsp", 1),
          ("secProtocolUnknown", 0))
    )



class CgmGdoiTekSPI(OctetString, TextualConvention):
    status = "current"
    displayHint = "4x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )



class CgmGdoiKekStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inUse", 1),
          ("new", 2),
          ("old", 3))
    )



class CgmGdoiTekStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("notInUse", 3),
          ("outbound", 2))
    )



class CgmGdoiUnsigned16(OctetString, TextualConvention):
    status = "current"
    displayHint = "2d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )



# MIB Managed Objects in the order of their OIDs

_CgmGdoiMIBNotifications_ObjectIdentity = ObjectIdentity
cgmGdoiMIBNotifications = _CgmGdoiMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 0)
)
_CgmGdoiMIBObjects_ObjectIdentity = ObjectIdentity
cgmGdoiMIBObjects = _CgmGdoiMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1)
)
_CgmGdoiGroupTable_Object = MibTable
cgmGdoiGroupTable = _CgmGdoiGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 1)
)
if mibBuilder.loadTexts:
    cgmGdoiGroupTable.setStatus("current")
_CgmGdoiGroupEntry_Object = MibTableRow
cgmGdoiGroupEntry = _CgmGdoiGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 1, 1)
)
cgmGdoiGroupEntry.setIndexNames(
    (0, "CISCO-GDOI-MIB", "cgmGdoiGroupIdType"),
    (0, "CISCO-GDOI-MIB", "cgmGdoiGroupIdValue"),
)
if mibBuilder.loadTexts:
    cgmGdoiGroupEntry.setStatus("current")
_CgmGdoiGroupIdType_Type = CgmGdoiIdentificationType
_CgmGdoiGroupIdType_Object = MibTableColumn
cgmGdoiGroupIdType = _CgmGdoiGroupIdType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 1, 1, 1),
    _CgmGdoiGroupIdType_Type()
)
cgmGdoiGroupIdType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgmGdoiGroupIdType.setStatus("current")
_CgmGdoiGroupIdLength_Type = Unsigned32
_CgmGdoiGroupIdLength_Object = MibTableColumn
cgmGdoiGroupIdLength = _CgmGdoiGroupIdLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 1, 1, 2),
    _CgmGdoiGroupIdLength_Type()
)
cgmGdoiGroupIdLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiGroupIdLength.setStatus("current")
if mibBuilder.loadTexts:
    cgmGdoiGroupIdLength.setUnits("Octets")
_CgmGdoiGroupIdValue_Type = CgmGdoiIdentificationValue
_CgmGdoiGroupIdValue_Object = MibTableColumn
cgmGdoiGroupIdValue = _CgmGdoiGroupIdValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 1, 1, 3),
    _CgmGdoiGroupIdValue_Type()
)
cgmGdoiGroupIdValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgmGdoiGroupIdValue.setStatus("current")
_CgmGdoiGroupName_Type = DisplayString
_CgmGdoiGroupName_Object = MibTableColumn
cgmGdoiGroupName = _CgmGdoiGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 1, 1, 4),
    _CgmGdoiGroupName_Type()
)
cgmGdoiGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiGroupName.setStatus("current")
_CgmGdoiGroupMemberCount_Type = Unsigned32
_CgmGdoiGroupMemberCount_Object = MibTableColumn
cgmGdoiGroupMemberCount = _CgmGdoiGroupMemberCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 1, 1, 5),
    _CgmGdoiGroupMemberCount_Type()
)
cgmGdoiGroupMemberCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiGroupMemberCount.setStatus("current")
_CgmGdoiGroupActivePeerKeyServerCount_Type = Unsigned32
_CgmGdoiGroupActivePeerKeyServerCount_Object = MibTableColumn
cgmGdoiGroupActivePeerKeyServerCount = _CgmGdoiGroupActivePeerKeyServerCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 1, 1, 6),
    _CgmGdoiGroupActivePeerKeyServerCount_Type()
)
cgmGdoiGroupActivePeerKeyServerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiGroupActivePeerKeyServerCount.setStatus("current")
_CgmGdoiGroupLastRekeyRetransmits_Type = Unsigned32
_CgmGdoiGroupLastRekeyRetransmits_Object = MibTableColumn
cgmGdoiGroupLastRekeyRetransmits = _CgmGdoiGroupLastRekeyRetransmits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 1, 1, 7),
    _CgmGdoiGroupLastRekeyRetransmits_Type()
)
cgmGdoiGroupLastRekeyRetransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiGroupLastRekeyRetransmits.setStatus("current")
_CgmGdoiGroupLastRekeyTimeTaken_Type = CiscoMilliSeconds
_CgmGdoiGroupLastRekeyTimeTaken_Object = MibTableColumn
cgmGdoiGroupLastRekeyTimeTaken = _CgmGdoiGroupLastRekeyTimeTaken_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 1, 1, 8),
    _CgmGdoiGroupLastRekeyTimeTaken_Type()
)
cgmGdoiGroupLastRekeyTimeTaken.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiGroupLastRekeyTimeTaken.setStatus("current")
_CgmGdoiPeers_ObjectIdentity = ObjectIdentity
cgmGdoiPeers = _CgmGdoiPeers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 2)
)
_CgmGdoiKeyServerTable_Object = MibTable
cgmGdoiKeyServerTable = _CgmGdoiKeyServerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cgmGdoiKeyServerTable.setStatus("current")
_CgmGdoiKeyServerEntry_Object = MibTableRow
cgmGdoiKeyServerEntry = _CgmGdoiKeyServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 2, 1, 1)
)
cgmGdoiKeyServerEntry.setIndexNames(
    (0, "CISCO-GDOI-MIB", "cgmGdoiGroupIdType"),
    (0, "CISCO-GDOI-MIB", "cgmGdoiGroupIdValue"),
    (0, "CISCO-GDOI-MIB", "cgmGdoiKeyServerIdType"),
    (0, "CISCO-GDOI-MIB", "cgmGdoiKeyServerIdValue"),
)
if mibBuilder.loadTexts:
    cgmGdoiKeyServerEntry.setStatus("current")
_CgmGdoiKeyServerIdType_Type = CgmGdoiIdentificationType
_CgmGdoiKeyServerIdType_Object = MibTableColumn
cgmGdoiKeyServerIdType = _CgmGdoiKeyServerIdType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 2, 1, 1, 1),
    _CgmGdoiKeyServerIdType_Type()
)
cgmGdoiKeyServerIdType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgmGdoiKeyServerIdType.setStatus("current")
_CgmGdoiKeyServerIdLength_Type = Unsigned32
_CgmGdoiKeyServerIdLength_Object = MibTableColumn
cgmGdoiKeyServerIdLength = _CgmGdoiKeyServerIdLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 2, 1, 1, 2),
    _CgmGdoiKeyServerIdLength_Type()
)
cgmGdoiKeyServerIdLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiKeyServerIdLength.setStatus("current")
if mibBuilder.loadTexts:
    cgmGdoiKeyServerIdLength.setUnits("Octets")
_CgmGdoiKeyServerIdValue_Type = CgmGdoiIdentificationValue
_CgmGdoiKeyServerIdValue_Object = MibTableColumn
cgmGdoiKeyServerIdValue = _CgmGdoiKeyServerIdValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 2, 1, 1, 3),
    _CgmGdoiKeyServerIdValue_Type()
)
cgmGdoiKeyServerIdValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgmGdoiKeyServerIdValue.setStatus("current")
_CgmGdoiKeyServerActiveKEK_Type = CgmGdoiKekSPI
_CgmGdoiKeyServerActiveKEK_Object = MibTableColumn
cgmGdoiKeyServerActiveKEK = _CgmGdoiKeyServerActiveKEK_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 2, 1, 1, 4),
    _CgmGdoiKeyServerActiveKEK_Type()
)
cgmGdoiKeyServerActiveKEK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiKeyServerActiveKEK.setStatus("current")
_CgmGdoiKeyServerRekeysPushed_Type = Counter32
_CgmGdoiKeyServerRekeysPushed_Object = MibTableColumn
cgmGdoiKeyServerRekeysPushed = _CgmGdoiKeyServerRekeysPushed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 2, 1, 1, 5),
    _CgmGdoiKeyServerRekeysPushed_Type()
)
cgmGdoiKeyServerRekeysPushed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiKeyServerRekeysPushed.setStatus("current")
if mibBuilder.loadTexts:
    cgmGdoiKeyServerRekeysPushed.setUnits("GROUPKEY-PUSH Messages")
_CgmGdoiKeyServerRole_Type = CgmGdoiKsRole
_CgmGdoiKeyServerRole_Object = MibTableColumn
cgmGdoiKeyServerRole = _CgmGdoiKeyServerRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 2, 1, 1, 6),
    _CgmGdoiKeyServerRole_Type()
)
cgmGdoiKeyServerRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiKeyServerRole.setStatus("current")
_CgmGdoiKeyServerRegisteredGMs_Type = Unsigned32
_CgmGdoiKeyServerRegisteredGMs_Object = MibTableColumn
cgmGdoiKeyServerRegisteredGMs = _CgmGdoiKeyServerRegisteredGMs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 2, 1, 1, 7),
    _CgmGdoiKeyServerRegisteredGMs_Type()
)
cgmGdoiKeyServerRegisteredGMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiKeyServerRegisteredGMs.setStatus("current")
_CgmGdoiGmTable_Object = MibTable
cgmGdoiGmTable = _CgmGdoiGmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cgmGdoiGmTable.setStatus("current")
_CgmGdoiGmEntry_Object = MibTableRow
cgmGdoiGmEntry = _CgmGdoiGmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 2, 2, 1)
)
cgmGdoiGmEntry.setIndexNames(
    (0, "CISCO-GDOI-MIB", "cgmGdoiGroupIdType"),
    (0, "CISCO-GDOI-MIB", "cgmGdoiGroupIdValue"),
    (0, "CISCO-GDOI-MIB", "cgmGdoiGmIdType"),
    (0, "CISCO-GDOI-MIB", "cgmGdoiGmIdValue"),
)
if mibBuilder.loadTexts:
    cgmGdoiGmEntry.setStatus("current")
_CgmGdoiGmIdType_Type = CgmGdoiIdentificationType
_CgmGdoiGmIdType_Object = MibTableColumn
cgmGdoiGmIdType = _CgmGdoiGmIdType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 2, 2, 1, 1),
    _CgmGdoiGmIdType_Type()
)
cgmGdoiGmIdType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgmGdoiGmIdType.setStatus("current")
_CgmGdoiGmIdLength_Type = Unsigned32
_CgmGdoiGmIdLength_Object = MibTableColumn
cgmGdoiGmIdLength = _CgmGdoiGmIdLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 2, 2, 1, 2),
    _CgmGdoiGmIdLength_Type()
)
cgmGdoiGmIdLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiGmIdLength.setStatus("current")
if mibBuilder.loadTexts:
    cgmGdoiGmIdLength.setUnits("Octets")
_CgmGdoiGmIdValue_Type = CgmGdoiIdentificationValue
_CgmGdoiGmIdValue_Object = MibTableColumn
cgmGdoiGmIdValue = _CgmGdoiGmIdValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 2, 2, 1, 3),
    _CgmGdoiGmIdValue_Type()
)
cgmGdoiGmIdValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgmGdoiGmIdValue.setStatus("current")
_CgmGdoiGmRegKeyServerIdType_Type = CgmGdoiIdentificationType
_CgmGdoiGmRegKeyServerIdType_Object = MibTableColumn
cgmGdoiGmRegKeyServerIdType = _CgmGdoiGmRegKeyServerIdType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 2, 2, 1, 4),
    _CgmGdoiGmRegKeyServerIdType_Type()
)
cgmGdoiGmRegKeyServerIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiGmRegKeyServerIdType.setStatus("current")
_CgmGdoiGmRegKeyServerIdLength_Type = Unsigned32
_CgmGdoiGmRegKeyServerIdLength_Object = MibTableColumn
cgmGdoiGmRegKeyServerIdLength = _CgmGdoiGmRegKeyServerIdLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 2, 2, 1, 5),
    _CgmGdoiGmRegKeyServerIdLength_Type()
)
cgmGdoiGmRegKeyServerIdLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiGmRegKeyServerIdLength.setStatus("current")
if mibBuilder.loadTexts:
    cgmGdoiGmRegKeyServerIdLength.setUnits("Octets")
_CgmGdoiGmRegKeyServerIdValue_Type = CgmGdoiIdentificationValue
_CgmGdoiGmRegKeyServerIdValue_Object = MibTableColumn
cgmGdoiGmRegKeyServerIdValue = _CgmGdoiGmRegKeyServerIdValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 2, 2, 1, 6),
    _CgmGdoiGmRegKeyServerIdValue_Type()
)
cgmGdoiGmRegKeyServerIdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiGmRegKeyServerIdValue.setStatus("current")
_CgmGdoiGmActiveKEK_Type = CgmGdoiKekSPI
_CgmGdoiGmActiveKEK_Object = MibTableColumn
cgmGdoiGmActiveKEK = _CgmGdoiGmActiveKEK_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 2, 2, 1, 7),
    _CgmGdoiGmActiveKEK_Type()
)
cgmGdoiGmActiveKEK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiGmActiveKEK.setStatus("current")
_CgmGdoiGmRekeysReceived_Type = Counter32
_CgmGdoiGmRekeysReceived_Object = MibTableColumn
cgmGdoiGmRekeysReceived = _CgmGdoiGmRekeysReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 2, 2, 1, 8),
    _CgmGdoiGmRekeysReceived_Type()
)
cgmGdoiGmRekeysReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiGmRekeysReceived.setStatus("current")
if mibBuilder.loadTexts:
    cgmGdoiGmRekeysReceived.setUnits("GROUPKEY-PUSH Messages")
_CgmGdoiGmActiveTEKNum_Type = Counter32
_CgmGdoiGmActiveTEKNum_Object = MibTableColumn
cgmGdoiGmActiveTEKNum = _CgmGdoiGmActiveTEKNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 2, 2, 1, 9),
    _CgmGdoiGmActiveTEKNum_Type()
)
cgmGdoiGmActiveTEKNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiGmActiveTEKNum.setStatus("current")
if mibBuilder.loadTexts:
    cgmGdoiGmActiveTEKNum.setUnits("Number of traffic encryption keys")
_CgmGdoiCoopPeerTable_Object = MibTable
cgmGdoiCoopPeerTable = _CgmGdoiCoopPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cgmGdoiCoopPeerTable.setStatus("current")
_CgmGdoiCoopPeerEntry_Object = MibTableRow
cgmGdoiCoopPeerEntry = _CgmGdoiCoopPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 2, 3, 1)
)
cgmGdoiCoopPeerEntry.setIndexNames(
    (0, "CISCO-GDOI-MIB", "cgmGdoiGroupIdType"),
    (0, "CISCO-GDOI-MIB", "cgmGdoiGroupIdValue"),
    (0, "CISCO-GDOI-MIB", "cgmGdoiCoopPeerIdType"),
    (0, "CISCO-GDOI-MIB", "cgmGdoiCoopPeerIdValue"),
)
if mibBuilder.loadTexts:
    cgmGdoiCoopPeerEntry.setStatus("current")
_CgmGdoiCoopPeerIdType_Type = CgmGdoiIdentificationType
_CgmGdoiCoopPeerIdType_Object = MibTableColumn
cgmGdoiCoopPeerIdType = _CgmGdoiCoopPeerIdType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 2, 3, 1, 1),
    _CgmGdoiCoopPeerIdType_Type()
)
cgmGdoiCoopPeerIdType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgmGdoiCoopPeerIdType.setStatus("current")
_CgmGdoiCoopPeerIdLength_Type = Unsigned32
_CgmGdoiCoopPeerIdLength_Object = MibTableColumn
cgmGdoiCoopPeerIdLength = _CgmGdoiCoopPeerIdLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 2, 3, 1, 2),
    _CgmGdoiCoopPeerIdLength_Type()
)
cgmGdoiCoopPeerIdLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiCoopPeerIdLength.setStatus("current")
_CgmGdoiCoopPeerIdValue_Type = CgmGdoiIdentificationValue
_CgmGdoiCoopPeerIdValue_Object = MibTableColumn
cgmGdoiCoopPeerIdValue = _CgmGdoiCoopPeerIdValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 2, 3, 1, 3),
    _CgmGdoiCoopPeerIdValue_Type()
)
cgmGdoiCoopPeerIdValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgmGdoiCoopPeerIdValue.setStatus("current")
_CgmGdoiCoopPeerRole_Type = CgmGdoiKsRole
_CgmGdoiCoopPeerRole_Object = MibTableColumn
cgmGdoiCoopPeerRole = _CgmGdoiCoopPeerRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 2, 3, 1, 4),
    _CgmGdoiCoopPeerRole_Type()
)
cgmGdoiCoopPeerRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiCoopPeerRole.setStatus("current")
_CgmGdoiCoopPeerStatus_Type = CgmGdoiKsStatus
_CgmGdoiCoopPeerStatus_Object = MibTableColumn
cgmGdoiCoopPeerStatus = _CgmGdoiCoopPeerStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 2, 3, 1, 5),
    _CgmGdoiCoopPeerStatus_Type()
)
cgmGdoiCoopPeerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiCoopPeerStatus.setStatus("current")
_CgmGdoiCoopPeerRegisteredGMs_Type = Unsigned32
_CgmGdoiCoopPeerRegisteredGMs_Object = MibTableColumn
cgmGdoiCoopPeerRegisteredGMs = _CgmGdoiCoopPeerRegisteredGMs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 2, 3, 1, 6),
    _CgmGdoiCoopPeerRegisteredGMs_Type()
)
cgmGdoiCoopPeerRegisteredGMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiCoopPeerRegisteredGMs.setStatus("current")
_CgmGdoiSecAssociations_ObjectIdentity = ObjectIdentity
cgmGdoiSecAssociations = _CgmGdoiSecAssociations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3)
)
_CgmGdoiKsKekTable_Object = MibTable
cgmGdoiKsKekTable = _CgmGdoiKsKekTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cgmGdoiKsKekTable.setStatus("current")
_CgmGdoiKsKekEntry_Object = MibTableRow
cgmGdoiKsKekEntry = _CgmGdoiKsKekEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 1, 1)
)
cgmGdoiKsKekEntry.setIndexNames(
    (0, "CISCO-GDOI-MIB", "cgmGdoiGroupIdType"),
    (0, "CISCO-GDOI-MIB", "cgmGdoiGroupIdValue"),
    (0, "CISCO-GDOI-MIB", "cgmGdoiKeyServerIdType"),
    (0, "CISCO-GDOI-MIB", "cgmGdoiKeyServerIdValue"),
    (0, "CISCO-GDOI-MIB", "cgmGdoiKsKekIndex"),
)
if mibBuilder.loadTexts:
    cgmGdoiKsKekEntry.setStatus("current")
_CgmGdoiKsKekIndex_Type = Unsigned32
_CgmGdoiKsKekIndex_Object = MibTableColumn
cgmGdoiKsKekIndex = _CgmGdoiKsKekIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 1, 1, 1),
    _CgmGdoiKsKekIndex_Type()
)
cgmGdoiKsKekIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgmGdoiKsKekIndex.setStatus("current")
_CgmGdoiKsKekSPI_Type = CgmGdoiKekSPI
_CgmGdoiKsKekSPI_Object = MibTableColumn
cgmGdoiKsKekSPI = _CgmGdoiKsKekSPI_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 1, 1, 2),
    _CgmGdoiKsKekSPI_Type()
)
cgmGdoiKsKekSPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiKsKekSPI.setStatus("current")
_CgmGdoiKsKekSrcIdType_Type = CgmGdoiIdentificationType
_CgmGdoiKsKekSrcIdType_Object = MibTableColumn
cgmGdoiKsKekSrcIdType = _CgmGdoiKsKekSrcIdType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 1, 1, 3),
    _CgmGdoiKsKekSrcIdType_Type()
)
cgmGdoiKsKekSrcIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiKsKekSrcIdType.setStatus("current")
_CgmGdoiKsKekSrcIdLength_Type = Unsigned32
_CgmGdoiKsKekSrcIdLength_Object = MibTableColumn
cgmGdoiKsKekSrcIdLength = _CgmGdoiKsKekSrcIdLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 1, 1, 4),
    _CgmGdoiKsKekSrcIdLength_Type()
)
cgmGdoiKsKekSrcIdLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiKsKekSrcIdLength.setStatus("current")
if mibBuilder.loadTexts:
    cgmGdoiKsKekSrcIdLength.setUnits("Octets")
_CgmGdoiKsKekSrcIdValue_Type = CgmGdoiIdentificationValue
_CgmGdoiKsKekSrcIdValue_Object = MibTableColumn
cgmGdoiKsKekSrcIdValue = _CgmGdoiKsKekSrcIdValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 1, 1, 5),
    _CgmGdoiKsKekSrcIdValue_Type()
)
cgmGdoiKsKekSrcIdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiKsKekSrcIdValue.setStatus("current")
_CgmGdoiKsKekSrcIdPort_Type = CgmGdoiUnsigned16
_CgmGdoiKsKekSrcIdPort_Object = MibTableColumn
cgmGdoiKsKekSrcIdPort = _CgmGdoiKsKekSrcIdPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 1, 1, 6),
    _CgmGdoiKsKekSrcIdPort_Type()
)
cgmGdoiKsKekSrcIdPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiKsKekSrcIdPort.setStatus("current")
_CgmGdoiKsKekDstIdType_Type = CgmGdoiIdentificationType
_CgmGdoiKsKekDstIdType_Object = MibTableColumn
cgmGdoiKsKekDstIdType = _CgmGdoiKsKekDstIdType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 1, 1, 7),
    _CgmGdoiKsKekDstIdType_Type()
)
cgmGdoiKsKekDstIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiKsKekDstIdType.setStatus("current")
_CgmGdoiKsKekDstIdLength_Type = Unsigned32
_CgmGdoiKsKekDstIdLength_Object = MibTableColumn
cgmGdoiKsKekDstIdLength = _CgmGdoiKsKekDstIdLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 1, 1, 8),
    _CgmGdoiKsKekDstIdLength_Type()
)
cgmGdoiKsKekDstIdLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiKsKekDstIdLength.setStatus("current")
if mibBuilder.loadTexts:
    cgmGdoiKsKekDstIdLength.setUnits("Octets")
_CgmGdoiKsKekDstIdValue_Type = CgmGdoiIdentificationValue
_CgmGdoiKsKekDstIdValue_Object = MibTableColumn
cgmGdoiKsKekDstIdValue = _CgmGdoiKsKekDstIdValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 1, 1, 9),
    _CgmGdoiKsKekDstIdValue_Type()
)
cgmGdoiKsKekDstIdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiKsKekDstIdValue.setStatus("current")
_CgmGdoiKsKekDstIdPort_Type = CgmGdoiUnsigned16
_CgmGdoiKsKekDstIdPort_Object = MibTableColumn
cgmGdoiKsKekDstIdPort = _CgmGdoiKsKekDstIdPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 1, 1, 10),
    _CgmGdoiKsKekDstIdPort_Type()
)
cgmGdoiKsKekDstIdPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiKsKekDstIdPort.setStatus("current")
_CgmGdoiKsKekIpProtocol_Type = CgmGdoiIpProtocolId
_CgmGdoiKsKekIpProtocol_Object = MibTableColumn
cgmGdoiKsKekIpProtocol = _CgmGdoiKsKekIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 1, 1, 11),
    _CgmGdoiKsKekIpProtocol_Type()
)
cgmGdoiKsKekIpProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiKsKekIpProtocol.setStatus("current")
_CgmGdoiKsKekMgmtAlg_Type = CgmGdoiKeyManagementAlgorithm
_CgmGdoiKsKekMgmtAlg_Object = MibTableColumn
cgmGdoiKsKekMgmtAlg = _CgmGdoiKsKekMgmtAlg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 1, 1, 12),
    _CgmGdoiKsKekMgmtAlg_Type()
)
cgmGdoiKsKekMgmtAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiKsKekMgmtAlg.setStatus("current")
_CgmGdoiKsKekEncryptAlg_Type = CgmGdoiEncryptionAlgorithm
_CgmGdoiKsKekEncryptAlg_Object = MibTableColumn
cgmGdoiKsKekEncryptAlg = _CgmGdoiKsKekEncryptAlg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 1, 1, 13),
    _CgmGdoiKsKekEncryptAlg_Type()
)
cgmGdoiKsKekEncryptAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiKsKekEncryptAlg.setStatus("current")
_CgmGdoiKsKekEncryptKeyLength_Type = Unsigned32
_CgmGdoiKsKekEncryptKeyLength_Object = MibTableColumn
cgmGdoiKsKekEncryptKeyLength = _CgmGdoiKsKekEncryptKeyLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 1, 1, 14),
    _CgmGdoiKsKekEncryptKeyLength_Type()
)
cgmGdoiKsKekEncryptKeyLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiKsKekEncryptKeyLength.setStatus("current")
if mibBuilder.loadTexts:
    cgmGdoiKsKekEncryptKeyLength.setUnits("Bits")
_CgmGdoiKsKekSigHashAlg_Type = CgmGdoiPseudoRandomFunction
_CgmGdoiKsKekSigHashAlg_Object = MibTableColumn
cgmGdoiKsKekSigHashAlg = _CgmGdoiKsKekSigHashAlg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 1, 1, 15),
    _CgmGdoiKsKekSigHashAlg_Type()
)
cgmGdoiKsKekSigHashAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiKsKekSigHashAlg.setStatus("current")
_CgmGdoiKsKekSigAlg_Type = CgmGdoiSignatureMethod
_CgmGdoiKsKekSigAlg_Object = MibTableColumn
cgmGdoiKsKekSigAlg = _CgmGdoiKsKekSigAlg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 1, 1, 16),
    _CgmGdoiKsKekSigAlg_Type()
)
cgmGdoiKsKekSigAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiKsKekSigAlg.setStatus("current")
_CgmGdoiKsKekSigKeyLength_Type = Unsigned32
_CgmGdoiKsKekSigKeyLength_Object = MibTableColumn
cgmGdoiKsKekSigKeyLength = _CgmGdoiKsKekSigKeyLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 1, 1, 17),
    _CgmGdoiKsKekSigKeyLength_Type()
)
cgmGdoiKsKekSigKeyLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiKsKekSigKeyLength.setStatus("current")
if mibBuilder.loadTexts:
    cgmGdoiKsKekSigKeyLength.setUnits("Bits")
_CgmGdoiKsKekOakleyGroup_Type = CgmGdoiDiffieHellmanGroup
_CgmGdoiKsKekOakleyGroup_Object = MibTableColumn
cgmGdoiKsKekOakleyGroup = _CgmGdoiKsKekOakleyGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 1, 1, 18),
    _CgmGdoiKsKekOakleyGroup_Type()
)
cgmGdoiKsKekOakleyGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiKsKekOakleyGroup.setStatus("current")
_CgmGdoiKsKekOriginalLifetime_Type = Unsigned32
_CgmGdoiKsKekOriginalLifetime_Object = MibTableColumn
cgmGdoiKsKekOriginalLifetime = _CgmGdoiKsKekOriginalLifetime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 1, 1, 19),
    _CgmGdoiKsKekOriginalLifetime_Type()
)
cgmGdoiKsKekOriginalLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiKsKekOriginalLifetime.setStatus("current")
if mibBuilder.loadTexts:
    cgmGdoiKsKekOriginalLifetime.setUnits("Seconds")
_CgmGdoiKsKekRemainingLifetime_Type = Unsigned32
_CgmGdoiKsKekRemainingLifetime_Object = MibTableColumn
cgmGdoiKsKekRemainingLifetime = _CgmGdoiKsKekRemainingLifetime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 1, 1, 20),
    _CgmGdoiKsKekRemainingLifetime_Type()
)
cgmGdoiKsKekRemainingLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiKsKekRemainingLifetime.setStatus("current")
if mibBuilder.loadTexts:
    cgmGdoiKsKekRemainingLifetime.setUnits("Seconds")
_CgmGdoiKsKekStatus_Type = CgmGdoiKekStatus
_CgmGdoiKsKekStatus_Object = MibTableColumn
cgmGdoiKsKekStatus = _CgmGdoiKsKekStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 1, 1, 21),
    _CgmGdoiKsKekStatus_Type()
)
cgmGdoiKsKekStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiKsKekStatus.setStatus("current")
_CgmGdoiGmKekTable_Object = MibTable
cgmGdoiGmKekTable = _CgmGdoiGmKekTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cgmGdoiGmKekTable.setStatus("current")
_CgmGdoiGmKekEntry_Object = MibTableRow
cgmGdoiGmKekEntry = _CgmGdoiGmKekEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 2, 1)
)
cgmGdoiGmKekEntry.setIndexNames(
    (0, "CISCO-GDOI-MIB", "cgmGdoiGroupIdType"),
    (0, "CISCO-GDOI-MIB", "cgmGdoiGroupIdValue"),
    (0, "CISCO-GDOI-MIB", "cgmGdoiGmIdType"),
    (0, "CISCO-GDOI-MIB", "cgmGdoiGmIdValue"),
    (0, "CISCO-GDOI-MIB", "cgmGdoiGmKekIndex"),
)
if mibBuilder.loadTexts:
    cgmGdoiGmKekEntry.setStatus("current")
_CgmGdoiGmKekIndex_Type = Unsigned32
_CgmGdoiGmKekIndex_Object = MibTableColumn
cgmGdoiGmKekIndex = _CgmGdoiGmKekIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 2, 1, 1),
    _CgmGdoiGmKekIndex_Type()
)
cgmGdoiGmKekIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgmGdoiGmKekIndex.setStatus("current")
_CgmGdoiGmKekSPI_Type = CgmGdoiKekSPI
_CgmGdoiGmKekSPI_Object = MibTableColumn
cgmGdoiGmKekSPI = _CgmGdoiGmKekSPI_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 2, 1, 2),
    _CgmGdoiGmKekSPI_Type()
)
cgmGdoiGmKekSPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiGmKekSPI.setStatus("current")
_CgmGdoiGmKekSrcIdType_Type = CgmGdoiIdentificationType
_CgmGdoiGmKekSrcIdType_Object = MibTableColumn
cgmGdoiGmKekSrcIdType = _CgmGdoiGmKekSrcIdType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 2, 1, 3),
    _CgmGdoiGmKekSrcIdType_Type()
)
cgmGdoiGmKekSrcIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiGmKekSrcIdType.setStatus("current")
_CgmGdoiGmKekSrcIdLength_Type = Unsigned32
_CgmGdoiGmKekSrcIdLength_Object = MibTableColumn
cgmGdoiGmKekSrcIdLength = _CgmGdoiGmKekSrcIdLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 2, 1, 4),
    _CgmGdoiGmKekSrcIdLength_Type()
)
cgmGdoiGmKekSrcIdLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiGmKekSrcIdLength.setStatus("current")
if mibBuilder.loadTexts:
    cgmGdoiGmKekSrcIdLength.setUnits("Octets")
_CgmGdoiGmKekSrcIdValue_Type = CgmGdoiIdentificationValue
_CgmGdoiGmKekSrcIdValue_Object = MibTableColumn
cgmGdoiGmKekSrcIdValue = _CgmGdoiGmKekSrcIdValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 2, 1, 5),
    _CgmGdoiGmKekSrcIdValue_Type()
)
cgmGdoiGmKekSrcIdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiGmKekSrcIdValue.setStatus("current")
_CgmGdoiGmKekSrcIdPort_Type = CgmGdoiUnsigned16
_CgmGdoiGmKekSrcIdPort_Object = MibTableColumn
cgmGdoiGmKekSrcIdPort = _CgmGdoiGmKekSrcIdPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 2, 1, 6),
    _CgmGdoiGmKekSrcIdPort_Type()
)
cgmGdoiGmKekSrcIdPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiGmKekSrcIdPort.setStatus("current")
_CgmGdoiGmKekDstIdType_Type = CgmGdoiIdentificationType
_CgmGdoiGmKekDstIdType_Object = MibTableColumn
cgmGdoiGmKekDstIdType = _CgmGdoiGmKekDstIdType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 2, 1, 7),
    _CgmGdoiGmKekDstIdType_Type()
)
cgmGdoiGmKekDstIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiGmKekDstIdType.setStatus("current")
_CgmGdoiGmKekDstIdLength_Type = Unsigned32
_CgmGdoiGmKekDstIdLength_Object = MibTableColumn
cgmGdoiGmKekDstIdLength = _CgmGdoiGmKekDstIdLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 2, 1, 8),
    _CgmGdoiGmKekDstIdLength_Type()
)
cgmGdoiGmKekDstIdLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiGmKekDstIdLength.setStatus("current")
if mibBuilder.loadTexts:
    cgmGdoiGmKekDstIdLength.setUnits("Octets")
_CgmGdoiGmKekDstIdValue_Type = CgmGdoiIdentificationValue
_CgmGdoiGmKekDstIdValue_Object = MibTableColumn
cgmGdoiGmKekDstIdValue = _CgmGdoiGmKekDstIdValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 2, 1, 9),
    _CgmGdoiGmKekDstIdValue_Type()
)
cgmGdoiGmKekDstIdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiGmKekDstIdValue.setStatus("current")
_CgmGdoiGmKekDstIdPort_Type = CgmGdoiUnsigned16
_CgmGdoiGmKekDstIdPort_Object = MibTableColumn
cgmGdoiGmKekDstIdPort = _CgmGdoiGmKekDstIdPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 2, 1, 10),
    _CgmGdoiGmKekDstIdPort_Type()
)
cgmGdoiGmKekDstIdPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiGmKekDstIdPort.setStatus("current")
_CgmGdoiGmKekIpProtocol_Type = CgmGdoiIpProtocolId
_CgmGdoiGmKekIpProtocol_Object = MibTableColumn
cgmGdoiGmKekIpProtocol = _CgmGdoiGmKekIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 2, 1, 11),
    _CgmGdoiGmKekIpProtocol_Type()
)
cgmGdoiGmKekIpProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiGmKekIpProtocol.setStatus("current")
_CgmGdoiGmKekMgmtAlg_Type = CgmGdoiKeyManagementAlgorithm
_CgmGdoiGmKekMgmtAlg_Object = MibTableColumn
cgmGdoiGmKekMgmtAlg = _CgmGdoiGmKekMgmtAlg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 2, 1, 12),
    _CgmGdoiGmKekMgmtAlg_Type()
)
cgmGdoiGmKekMgmtAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiGmKekMgmtAlg.setStatus("current")
_CgmGdoiGmKekEncryptAlg_Type = CgmGdoiEncryptionAlgorithm
_CgmGdoiGmKekEncryptAlg_Object = MibTableColumn
cgmGdoiGmKekEncryptAlg = _CgmGdoiGmKekEncryptAlg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 2, 1, 13),
    _CgmGdoiGmKekEncryptAlg_Type()
)
cgmGdoiGmKekEncryptAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiGmKekEncryptAlg.setStatus("current")
_CgmGdoiGmKekEncryptKeyLength_Type = Unsigned32
_CgmGdoiGmKekEncryptKeyLength_Object = MibTableColumn
cgmGdoiGmKekEncryptKeyLength = _CgmGdoiGmKekEncryptKeyLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 2, 1, 14),
    _CgmGdoiGmKekEncryptKeyLength_Type()
)
cgmGdoiGmKekEncryptKeyLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiGmKekEncryptKeyLength.setStatus("current")
if mibBuilder.loadTexts:
    cgmGdoiGmKekEncryptKeyLength.setUnits("Bits")
_CgmGdoiGmKekSigHashAlg_Type = CgmGdoiPseudoRandomFunction
_CgmGdoiGmKekSigHashAlg_Object = MibTableColumn
cgmGdoiGmKekSigHashAlg = _CgmGdoiGmKekSigHashAlg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 2, 1, 15),
    _CgmGdoiGmKekSigHashAlg_Type()
)
cgmGdoiGmKekSigHashAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiGmKekSigHashAlg.setStatus("current")
_CgmGdoiGmKekSigAlg_Type = CgmGdoiSignatureMethod
_CgmGdoiGmKekSigAlg_Object = MibTableColumn
cgmGdoiGmKekSigAlg = _CgmGdoiGmKekSigAlg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 2, 1, 16),
    _CgmGdoiGmKekSigAlg_Type()
)
cgmGdoiGmKekSigAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiGmKekSigAlg.setStatus("current")
_CgmGdoiGmKekSigKeyLength_Type = Unsigned32
_CgmGdoiGmKekSigKeyLength_Object = MibTableColumn
cgmGdoiGmKekSigKeyLength = _CgmGdoiGmKekSigKeyLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 2, 1, 17),
    _CgmGdoiGmKekSigKeyLength_Type()
)
cgmGdoiGmKekSigKeyLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiGmKekSigKeyLength.setStatus("current")
if mibBuilder.loadTexts:
    cgmGdoiGmKekSigKeyLength.setUnits("Bits")
_CgmGdoiGmKekOakleyGroup_Type = CgmGdoiDiffieHellmanGroup
_CgmGdoiGmKekOakleyGroup_Object = MibTableColumn
cgmGdoiGmKekOakleyGroup = _CgmGdoiGmKekOakleyGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 2, 1, 18),
    _CgmGdoiGmKekOakleyGroup_Type()
)
cgmGdoiGmKekOakleyGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiGmKekOakleyGroup.setStatus("current")
_CgmGdoiGmKekOriginalLifetime_Type = Unsigned32
_CgmGdoiGmKekOriginalLifetime_Object = MibTableColumn
cgmGdoiGmKekOriginalLifetime = _CgmGdoiGmKekOriginalLifetime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 2, 1, 19),
    _CgmGdoiGmKekOriginalLifetime_Type()
)
cgmGdoiGmKekOriginalLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiGmKekOriginalLifetime.setStatus("current")
if mibBuilder.loadTexts:
    cgmGdoiGmKekOriginalLifetime.setUnits("Seconds")
_CgmGdoiGmKekRemainingLifetime_Type = Unsigned32
_CgmGdoiGmKekRemainingLifetime_Object = MibTableColumn
cgmGdoiGmKekRemainingLifetime = _CgmGdoiGmKekRemainingLifetime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 2, 1, 20),
    _CgmGdoiGmKekRemainingLifetime_Type()
)
cgmGdoiGmKekRemainingLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiGmKekRemainingLifetime.setStatus("current")
if mibBuilder.loadTexts:
    cgmGdoiGmKekRemainingLifetime.setUnits("Seconds")
_CgmGdoiGmKekStatus_Type = CgmGdoiKekStatus
_CgmGdoiGmKekStatus_Object = MibTableColumn
cgmGdoiGmKekStatus = _CgmGdoiGmKekStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 2, 1, 21),
    _CgmGdoiGmKekStatus_Type()
)
cgmGdoiGmKekStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiGmKekStatus.setStatus("current")
_CgmGdoiKsTekSelectorTable_Object = MibTable
cgmGdoiKsTekSelectorTable = _CgmGdoiKsTekSelectorTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 3)
)
if mibBuilder.loadTexts:
    cgmGdoiKsTekSelectorTable.setStatus("current")
_CgmGdoiKsTekSelectorEntry_Object = MibTableRow
cgmGdoiKsTekSelectorEntry = _CgmGdoiKsTekSelectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 3, 1)
)
cgmGdoiKsTekSelectorEntry.setIndexNames(
    (0, "CISCO-GDOI-MIB", "cgmGdoiGroupIdType"),
    (0, "CISCO-GDOI-MIB", "cgmGdoiGroupIdValue"),
    (0, "CISCO-GDOI-MIB", "cgmGdoiKeyServerIdType"),
    (0, "CISCO-GDOI-MIB", "cgmGdoiKeyServerIdValue"),
    (0, "CISCO-GDOI-MIB", "cgmGdoiKsTekSelectorIndex"),
)
if mibBuilder.loadTexts:
    cgmGdoiKsTekSelectorEntry.setStatus("current")
_CgmGdoiKsTekSelectorIndex_Type = Unsigned32
_CgmGdoiKsTekSelectorIndex_Object = MibTableColumn
cgmGdoiKsTekSelectorIndex = _CgmGdoiKsTekSelectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 3, 1, 1),
    _CgmGdoiKsTekSelectorIndex_Type()
)
cgmGdoiKsTekSelectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgmGdoiKsTekSelectorIndex.setStatus("current")
_CgmGdoiKsTekSrcIdType_Type = CgmGdoiIdentificationType
_CgmGdoiKsTekSrcIdType_Object = MibTableColumn
cgmGdoiKsTekSrcIdType = _CgmGdoiKsTekSrcIdType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 3, 1, 2),
    _CgmGdoiKsTekSrcIdType_Type()
)
cgmGdoiKsTekSrcIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiKsTekSrcIdType.setStatus("current")
_CgmGdoiKsTekSrcIdLength_Type = Unsigned32
_CgmGdoiKsTekSrcIdLength_Object = MibTableColumn
cgmGdoiKsTekSrcIdLength = _CgmGdoiKsTekSrcIdLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 3, 1, 3),
    _CgmGdoiKsTekSrcIdLength_Type()
)
cgmGdoiKsTekSrcIdLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiKsTekSrcIdLength.setStatus("current")
if mibBuilder.loadTexts:
    cgmGdoiKsTekSrcIdLength.setUnits("Octets")
_CgmGdoiKsTekSrcIdValue_Type = CgmGdoiIdentificationValue
_CgmGdoiKsTekSrcIdValue_Object = MibTableColumn
cgmGdoiKsTekSrcIdValue = _CgmGdoiKsTekSrcIdValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 3, 1, 4),
    _CgmGdoiKsTekSrcIdValue_Type()
)
cgmGdoiKsTekSrcIdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiKsTekSrcIdValue.setStatus("current")
_CgmGdoiKsTekSrcIdPort_Type = CgmGdoiUnsigned16
_CgmGdoiKsTekSrcIdPort_Object = MibTableColumn
cgmGdoiKsTekSrcIdPort = _CgmGdoiKsTekSrcIdPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 3, 1, 5),
    _CgmGdoiKsTekSrcIdPort_Type()
)
cgmGdoiKsTekSrcIdPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiKsTekSrcIdPort.setStatus("current")
_CgmGdoiKsTekDstIdType_Type = CgmGdoiIdentificationType
_CgmGdoiKsTekDstIdType_Object = MibTableColumn
cgmGdoiKsTekDstIdType = _CgmGdoiKsTekDstIdType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 3, 1, 6),
    _CgmGdoiKsTekDstIdType_Type()
)
cgmGdoiKsTekDstIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiKsTekDstIdType.setStatus("current")
_CgmGdoiKsTekDstIdLength_Type = Unsigned32
_CgmGdoiKsTekDstIdLength_Object = MibTableColumn
cgmGdoiKsTekDstIdLength = _CgmGdoiKsTekDstIdLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 3, 1, 7),
    _CgmGdoiKsTekDstIdLength_Type()
)
cgmGdoiKsTekDstIdLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiKsTekDstIdLength.setStatus("current")
if mibBuilder.loadTexts:
    cgmGdoiKsTekDstIdLength.setUnits("Octets")
_CgmGdoiKsTekDstIdValue_Type = CgmGdoiIdentificationValue
_CgmGdoiKsTekDstIdValue_Object = MibTableColumn
cgmGdoiKsTekDstIdValue = _CgmGdoiKsTekDstIdValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 3, 1, 8),
    _CgmGdoiKsTekDstIdValue_Type()
)
cgmGdoiKsTekDstIdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiKsTekDstIdValue.setStatus("current")
_CgmGdoiKsTekDstIdPort_Type = CgmGdoiUnsigned16
_CgmGdoiKsTekDstIdPort_Object = MibTableColumn
cgmGdoiKsTekDstIdPort = _CgmGdoiKsTekDstIdPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 3, 1, 9),
    _CgmGdoiKsTekDstIdPort_Type()
)
cgmGdoiKsTekDstIdPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiKsTekDstIdPort.setStatus("current")
_CgmGdoiKsTekSecurityProtocol_Type = CgmGdoiSecurityProtocol
_CgmGdoiKsTekSecurityProtocol_Object = MibTableColumn
cgmGdoiKsTekSecurityProtocol = _CgmGdoiKsTekSecurityProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 3, 1, 10),
    _CgmGdoiKsTekSecurityProtocol_Type()
)
cgmGdoiKsTekSecurityProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiKsTekSecurityProtocol.setStatus("current")
_CgmGdoiKsTekPolicyTable_Object = MibTable
cgmGdoiKsTekPolicyTable = _CgmGdoiKsTekPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 4)
)
if mibBuilder.loadTexts:
    cgmGdoiKsTekPolicyTable.setStatus("current")
_CgmGdoiKsTekPolicyEntry_Object = MibTableRow
cgmGdoiKsTekPolicyEntry = _CgmGdoiKsTekPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 4, 1)
)
cgmGdoiKsTekPolicyEntry.setIndexNames(
    (0, "CISCO-GDOI-MIB", "cgmGdoiGroupIdType"),
    (0, "CISCO-GDOI-MIB", "cgmGdoiGroupIdValue"),
    (0, "CISCO-GDOI-MIB", "cgmGdoiKeyServerIdType"),
    (0, "CISCO-GDOI-MIB", "cgmGdoiKeyServerIdValue"),
    (0, "CISCO-GDOI-MIB", "cgmGdoiKsTekSelectorIndex"),
    (0, "CISCO-GDOI-MIB", "cgmGdoiKsTekPolicyIndex"),
)
if mibBuilder.loadTexts:
    cgmGdoiKsTekPolicyEntry.setStatus("current")
_CgmGdoiKsTekPolicyIndex_Type = Unsigned32
_CgmGdoiKsTekPolicyIndex_Object = MibTableColumn
cgmGdoiKsTekPolicyIndex = _CgmGdoiKsTekPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 4, 1, 1),
    _CgmGdoiKsTekPolicyIndex_Type()
)
cgmGdoiKsTekPolicyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgmGdoiKsTekPolicyIndex.setStatus("current")
_CgmGdoiKsTekSPI_Type = CgmGdoiTekSPI
_CgmGdoiKsTekSPI_Object = MibTableColumn
cgmGdoiKsTekSPI = _CgmGdoiKsTekSPI_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 4, 1, 2),
    _CgmGdoiKsTekSPI_Type()
)
cgmGdoiKsTekSPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiKsTekSPI.setStatus("current")
_CgmGdoiKsTekEncapsulationMode_Type = CgmGdoiEncapsulationMode
_CgmGdoiKsTekEncapsulationMode_Object = MibTableColumn
cgmGdoiKsTekEncapsulationMode = _CgmGdoiKsTekEncapsulationMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 4, 1, 3),
    _CgmGdoiKsTekEncapsulationMode_Type()
)
cgmGdoiKsTekEncapsulationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiKsTekEncapsulationMode.setStatus("current")
_CgmGdoiKsTekEncryptionAlgorithm_Type = CgmGdoiEncryptionAlgorithm
_CgmGdoiKsTekEncryptionAlgorithm_Object = MibTableColumn
cgmGdoiKsTekEncryptionAlgorithm = _CgmGdoiKsTekEncryptionAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 4, 1, 4),
    _CgmGdoiKsTekEncryptionAlgorithm_Type()
)
cgmGdoiKsTekEncryptionAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiKsTekEncryptionAlgorithm.setStatus("current")
_CgmGdoiKsTekEncryptionKeyLength_Type = Unsigned32
_CgmGdoiKsTekEncryptionKeyLength_Object = MibTableColumn
cgmGdoiKsTekEncryptionKeyLength = _CgmGdoiKsTekEncryptionKeyLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 4, 1, 5),
    _CgmGdoiKsTekEncryptionKeyLength_Type()
)
cgmGdoiKsTekEncryptionKeyLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiKsTekEncryptionKeyLength.setStatus("current")
if mibBuilder.loadTexts:
    cgmGdoiKsTekEncryptionKeyLength.setUnits("Bits")
_CgmGdoiKsTekIntegrityAlgorithm_Type = CgmGdoiIntegrityAlgorithm
_CgmGdoiKsTekIntegrityAlgorithm_Object = MibTableColumn
cgmGdoiKsTekIntegrityAlgorithm = _CgmGdoiKsTekIntegrityAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 4, 1, 6),
    _CgmGdoiKsTekIntegrityAlgorithm_Type()
)
cgmGdoiKsTekIntegrityAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiKsTekIntegrityAlgorithm.setStatus("current")
_CgmGdoiKsTekIntegrityKeyLength_Type = Unsigned32
_CgmGdoiKsTekIntegrityKeyLength_Object = MibTableColumn
cgmGdoiKsTekIntegrityKeyLength = _CgmGdoiKsTekIntegrityKeyLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 4, 1, 7),
    _CgmGdoiKsTekIntegrityKeyLength_Type()
)
cgmGdoiKsTekIntegrityKeyLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiKsTekIntegrityKeyLength.setStatus("current")
if mibBuilder.loadTexts:
    cgmGdoiKsTekIntegrityKeyLength.setUnits("Bits")
_CgmGdoiKsTekWindowSize_Type = Unsigned32
_CgmGdoiKsTekWindowSize_Object = MibTableColumn
cgmGdoiKsTekWindowSize = _CgmGdoiKsTekWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 4, 1, 8),
    _CgmGdoiKsTekWindowSize_Type()
)
cgmGdoiKsTekWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiKsTekWindowSize.setStatus("current")
if mibBuilder.loadTexts:
    cgmGdoiKsTekWindowSize.setUnits("GROUPKEY-PUSH Messages")
_CgmGdoiKsTekOriginalLifetime_Type = Unsigned32
_CgmGdoiKsTekOriginalLifetime_Object = MibTableColumn
cgmGdoiKsTekOriginalLifetime = _CgmGdoiKsTekOriginalLifetime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 4, 1, 9),
    _CgmGdoiKsTekOriginalLifetime_Type()
)
cgmGdoiKsTekOriginalLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiKsTekOriginalLifetime.setStatus("current")
if mibBuilder.loadTexts:
    cgmGdoiKsTekOriginalLifetime.setUnits("Seconds")
_CgmGdoiKsTekRemainingLifetime_Type = Unsigned32
_CgmGdoiKsTekRemainingLifetime_Object = MibTableColumn
cgmGdoiKsTekRemainingLifetime = _CgmGdoiKsTekRemainingLifetime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 4, 1, 10),
    _CgmGdoiKsTekRemainingLifetime_Type()
)
cgmGdoiKsTekRemainingLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiKsTekRemainingLifetime.setStatus("current")
if mibBuilder.loadTexts:
    cgmGdoiKsTekRemainingLifetime.setUnits("Seconds")
_CgmGdoiKsTekStatus_Type = CgmGdoiTekStatus
_CgmGdoiKsTekStatus_Object = MibTableColumn
cgmGdoiKsTekStatus = _CgmGdoiKsTekStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 4, 1, 11),
    _CgmGdoiKsTekStatus_Type()
)
cgmGdoiKsTekStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiKsTekStatus.setStatus("current")
_CgmGdoiGmTekSelectorTable_Object = MibTable
cgmGdoiGmTekSelectorTable = _CgmGdoiGmTekSelectorTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 5)
)
if mibBuilder.loadTexts:
    cgmGdoiGmTekSelectorTable.setStatus("current")
_CgmGdoiGmTekSelectorEntry_Object = MibTableRow
cgmGdoiGmTekSelectorEntry = _CgmGdoiGmTekSelectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 5, 1)
)
cgmGdoiGmTekSelectorEntry.setIndexNames(
    (0, "CISCO-GDOI-MIB", "cgmGdoiGroupIdType"),
    (0, "CISCO-GDOI-MIB", "cgmGdoiGroupIdValue"),
    (0, "CISCO-GDOI-MIB", "cgmGdoiGmIdType"),
    (0, "CISCO-GDOI-MIB", "cgmGdoiGmIdValue"),
    (0, "CISCO-GDOI-MIB", "cgmGdoiGmTekSelectorIndex"),
)
if mibBuilder.loadTexts:
    cgmGdoiGmTekSelectorEntry.setStatus("current")
_CgmGdoiGmTekSelectorIndex_Type = Unsigned32
_CgmGdoiGmTekSelectorIndex_Object = MibTableColumn
cgmGdoiGmTekSelectorIndex = _CgmGdoiGmTekSelectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 5, 1, 1),
    _CgmGdoiGmTekSelectorIndex_Type()
)
cgmGdoiGmTekSelectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgmGdoiGmTekSelectorIndex.setStatus("current")
_CgmGdoiGmTekSrcIdType_Type = CgmGdoiIdentificationType
_CgmGdoiGmTekSrcIdType_Object = MibTableColumn
cgmGdoiGmTekSrcIdType = _CgmGdoiGmTekSrcIdType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 5, 1, 2),
    _CgmGdoiGmTekSrcIdType_Type()
)
cgmGdoiGmTekSrcIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiGmTekSrcIdType.setStatus("current")
_CgmGdoiGmTekSrcIdLength_Type = Unsigned32
_CgmGdoiGmTekSrcIdLength_Object = MibTableColumn
cgmGdoiGmTekSrcIdLength = _CgmGdoiGmTekSrcIdLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 5, 1, 3),
    _CgmGdoiGmTekSrcIdLength_Type()
)
cgmGdoiGmTekSrcIdLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiGmTekSrcIdLength.setStatus("current")
if mibBuilder.loadTexts:
    cgmGdoiGmTekSrcIdLength.setUnits("Octets")
_CgmGdoiGmTekSrcIdValue_Type = CgmGdoiIdentificationValue
_CgmGdoiGmTekSrcIdValue_Object = MibTableColumn
cgmGdoiGmTekSrcIdValue = _CgmGdoiGmTekSrcIdValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 5, 1, 4),
    _CgmGdoiGmTekSrcIdValue_Type()
)
cgmGdoiGmTekSrcIdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiGmTekSrcIdValue.setStatus("current")
_CgmGdoiGmTekSrcIdPort_Type = CgmGdoiUnsigned16
_CgmGdoiGmTekSrcIdPort_Object = MibTableColumn
cgmGdoiGmTekSrcIdPort = _CgmGdoiGmTekSrcIdPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 5, 1, 5),
    _CgmGdoiGmTekSrcIdPort_Type()
)
cgmGdoiGmTekSrcIdPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiGmTekSrcIdPort.setStatus("current")
_CgmGdoiGmTekDstIdType_Type = CgmGdoiIdentificationType
_CgmGdoiGmTekDstIdType_Object = MibTableColumn
cgmGdoiGmTekDstIdType = _CgmGdoiGmTekDstIdType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 5, 1, 6),
    _CgmGdoiGmTekDstIdType_Type()
)
cgmGdoiGmTekDstIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiGmTekDstIdType.setStatus("current")
_CgmGdoiGmTekDstIdLength_Type = Unsigned32
_CgmGdoiGmTekDstIdLength_Object = MibTableColumn
cgmGdoiGmTekDstIdLength = _CgmGdoiGmTekDstIdLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 5, 1, 7),
    _CgmGdoiGmTekDstIdLength_Type()
)
cgmGdoiGmTekDstIdLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiGmTekDstIdLength.setStatus("current")
if mibBuilder.loadTexts:
    cgmGdoiGmTekDstIdLength.setUnits("Octets")
_CgmGdoiGmTekDstIdValue_Type = CgmGdoiIdentificationValue
_CgmGdoiGmTekDstIdValue_Object = MibTableColumn
cgmGdoiGmTekDstIdValue = _CgmGdoiGmTekDstIdValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 5, 1, 8),
    _CgmGdoiGmTekDstIdValue_Type()
)
cgmGdoiGmTekDstIdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiGmTekDstIdValue.setStatus("current")
_CgmGdoiGmTekDstIdPort_Type = CgmGdoiUnsigned16
_CgmGdoiGmTekDstIdPort_Object = MibTableColumn
cgmGdoiGmTekDstIdPort = _CgmGdoiGmTekDstIdPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 5, 1, 9),
    _CgmGdoiGmTekDstIdPort_Type()
)
cgmGdoiGmTekDstIdPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiGmTekDstIdPort.setStatus("current")
_CgmGdoiGmTekSecurityProtocol_Type = CgmGdoiSecurityProtocol
_CgmGdoiGmTekSecurityProtocol_Object = MibTableColumn
cgmGdoiGmTekSecurityProtocol = _CgmGdoiGmTekSecurityProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 5, 1, 10),
    _CgmGdoiGmTekSecurityProtocol_Type()
)
cgmGdoiGmTekSecurityProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiGmTekSecurityProtocol.setStatus("current")
_CgmGdoiGmTekPolicyTable_Object = MibTable
cgmGdoiGmTekPolicyTable = _CgmGdoiGmTekPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 6)
)
if mibBuilder.loadTexts:
    cgmGdoiGmTekPolicyTable.setStatus("current")
_CgmGdoiGmTekPolicyEntry_Object = MibTableRow
cgmGdoiGmTekPolicyEntry = _CgmGdoiGmTekPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 6, 1)
)
cgmGdoiGmTekPolicyEntry.setIndexNames(
    (0, "CISCO-GDOI-MIB", "cgmGdoiGroupIdType"),
    (0, "CISCO-GDOI-MIB", "cgmGdoiGroupIdValue"),
    (0, "CISCO-GDOI-MIB", "cgmGdoiGmIdType"),
    (0, "CISCO-GDOI-MIB", "cgmGdoiGmIdValue"),
    (0, "CISCO-GDOI-MIB", "cgmGdoiGmTekSelectorIndex"),
    (0, "CISCO-GDOI-MIB", "cgmGdoiGmTekPolicyIndex"),
)
if mibBuilder.loadTexts:
    cgmGdoiGmTekPolicyEntry.setStatus("current")
_CgmGdoiGmTekPolicyIndex_Type = Unsigned32
_CgmGdoiGmTekPolicyIndex_Object = MibTableColumn
cgmGdoiGmTekPolicyIndex = _CgmGdoiGmTekPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 6, 1, 1),
    _CgmGdoiGmTekPolicyIndex_Type()
)
cgmGdoiGmTekPolicyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgmGdoiGmTekPolicyIndex.setStatus("current")
_CgmGdoiGmTekSPI_Type = CgmGdoiTekSPI
_CgmGdoiGmTekSPI_Object = MibTableColumn
cgmGdoiGmTekSPI = _CgmGdoiGmTekSPI_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 6, 1, 2),
    _CgmGdoiGmTekSPI_Type()
)
cgmGdoiGmTekSPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiGmTekSPI.setStatus("current")
_CgmGdoiGmTekEncapsulationMode_Type = CgmGdoiEncapsulationMode
_CgmGdoiGmTekEncapsulationMode_Object = MibTableColumn
cgmGdoiGmTekEncapsulationMode = _CgmGdoiGmTekEncapsulationMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 6, 1, 3),
    _CgmGdoiGmTekEncapsulationMode_Type()
)
cgmGdoiGmTekEncapsulationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiGmTekEncapsulationMode.setStatus("current")
_CgmGdoiGmTekEncryptionAlgorithm_Type = CgmGdoiEncryptionAlgorithm
_CgmGdoiGmTekEncryptionAlgorithm_Object = MibTableColumn
cgmGdoiGmTekEncryptionAlgorithm = _CgmGdoiGmTekEncryptionAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 6, 1, 4),
    _CgmGdoiGmTekEncryptionAlgorithm_Type()
)
cgmGdoiGmTekEncryptionAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiGmTekEncryptionAlgorithm.setStatus("current")
_CgmGdoiGmTekEncryptionKeyLength_Type = Unsigned32
_CgmGdoiGmTekEncryptionKeyLength_Object = MibTableColumn
cgmGdoiGmTekEncryptionKeyLength = _CgmGdoiGmTekEncryptionKeyLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 6, 1, 5),
    _CgmGdoiGmTekEncryptionKeyLength_Type()
)
cgmGdoiGmTekEncryptionKeyLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiGmTekEncryptionKeyLength.setStatus("current")
if mibBuilder.loadTexts:
    cgmGdoiGmTekEncryptionKeyLength.setUnits("Bits")
_CgmGdoiGmTekIntegrityAlgorithm_Type = CgmGdoiIntegrityAlgorithm
_CgmGdoiGmTekIntegrityAlgorithm_Object = MibTableColumn
cgmGdoiGmTekIntegrityAlgorithm = _CgmGdoiGmTekIntegrityAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 6, 1, 6),
    _CgmGdoiGmTekIntegrityAlgorithm_Type()
)
cgmGdoiGmTekIntegrityAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiGmTekIntegrityAlgorithm.setStatus("current")
_CgmGdoiGmTekIntegrityKeyLength_Type = Unsigned32
_CgmGdoiGmTekIntegrityKeyLength_Object = MibTableColumn
cgmGdoiGmTekIntegrityKeyLength = _CgmGdoiGmTekIntegrityKeyLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 6, 1, 7),
    _CgmGdoiGmTekIntegrityKeyLength_Type()
)
cgmGdoiGmTekIntegrityKeyLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiGmTekIntegrityKeyLength.setStatus("current")
if mibBuilder.loadTexts:
    cgmGdoiGmTekIntegrityKeyLength.setUnits("Bits")
_CgmGdoiGmTekWindowSize_Type = Unsigned32
_CgmGdoiGmTekWindowSize_Object = MibTableColumn
cgmGdoiGmTekWindowSize = _CgmGdoiGmTekWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 6, 1, 8),
    _CgmGdoiGmTekWindowSize_Type()
)
cgmGdoiGmTekWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiGmTekWindowSize.setStatus("current")
if mibBuilder.loadTexts:
    cgmGdoiGmTekWindowSize.setUnits("GROUPKEY-PUSH Messages")
_CgmGdoiGmTekOriginalLifetime_Type = Unsigned32
_CgmGdoiGmTekOriginalLifetime_Object = MibTableColumn
cgmGdoiGmTekOriginalLifetime = _CgmGdoiGmTekOriginalLifetime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 6, 1, 9),
    _CgmGdoiGmTekOriginalLifetime_Type()
)
cgmGdoiGmTekOriginalLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiGmTekOriginalLifetime.setStatus("current")
if mibBuilder.loadTexts:
    cgmGdoiGmTekOriginalLifetime.setUnits("Seconds")
_CgmGdoiGmTekRemainingLifetime_Type = Unsigned32
_CgmGdoiGmTekRemainingLifetime_Object = MibTableColumn
cgmGdoiGmTekRemainingLifetime = _CgmGdoiGmTekRemainingLifetime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 6, 1, 10),
    _CgmGdoiGmTekRemainingLifetime_Type()
)
cgmGdoiGmTekRemainingLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiGmTekRemainingLifetime.setStatus("current")
if mibBuilder.loadTexts:
    cgmGdoiGmTekRemainingLifetime.setUnits("Seconds")
_CgmGdoiGmTekStatus_Type = CgmGdoiTekStatus
_CgmGdoiGmTekStatus_Object = MibTableColumn
cgmGdoiGmTekStatus = _CgmGdoiGmTekStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 3, 6, 1, 11),
    _CgmGdoiGmTekStatus_Type()
)
cgmGdoiGmTekStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiGmTekStatus.setStatus("current")
_CgmGdoiNotifCntl_ObjectIdentity = ObjectIdentity
cgmGdoiNotifCntl = _CgmGdoiNotifCntl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 4)
)
_CgmGdoiKSNewRegNotifEnable_Type = TruthValue
_CgmGdoiKSNewRegNotifEnable_Object = MibScalar
cgmGdoiKSNewRegNotifEnable = _CgmGdoiKSNewRegNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 4, 1),
    _CgmGdoiKSNewRegNotifEnable_Type()
)
cgmGdoiKSNewRegNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgmGdoiKSNewRegNotifEnable.setStatus("current")
_CgmGdoiKSRegCompNotifEnable_Type = TruthValue
_CgmGdoiKSRegCompNotifEnable_Object = MibScalar
cgmGdoiKSRegCompNotifEnable = _CgmGdoiKSRegCompNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 4, 2),
    _CgmGdoiKSRegCompNotifEnable_Type()
)
cgmGdoiKSRegCompNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgmGdoiKSRegCompNotifEnable.setStatus("current")
_CgmGdoiKSRekeyPushNotifEnable_Type = TruthValue
_CgmGdoiKSRekeyPushNotifEnable_Object = MibScalar
cgmGdoiKSRekeyPushNotifEnable = _CgmGdoiKSRekeyPushNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 4, 3),
    _CgmGdoiKSRekeyPushNotifEnable_Type()
)
cgmGdoiKSRekeyPushNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgmGdoiKSRekeyPushNotifEnable.setStatus("current")
_CgmGdoiKSNoRSANotifEnable_Type = TruthValue
_CgmGdoiKSNoRSANotifEnable_Object = MibScalar
cgmGdoiKSNoRSANotifEnable = _CgmGdoiKSNoRSANotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 4, 4),
    _CgmGdoiKSNoRSANotifEnable_Type()
)
cgmGdoiKSNoRSANotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgmGdoiKSNoRSANotifEnable.setStatus("current")
_CgmGdoiGMRegNotifEnable_Type = TruthValue
_CgmGdoiGMRegNotifEnable_Object = MibScalar
cgmGdoiGMRegNotifEnable = _CgmGdoiGMRegNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 4, 5),
    _CgmGdoiGMRegNotifEnable_Type()
)
cgmGdoiGMRegNotifEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiGMRegNotifEnable.setStatus("current")
_CgmGdoiGmRegCompNotifEnable_Type = TruthValue
_CgmGdoiGmRegCompNotifEnable_Object = MibScalar
cgmGdoiGmRegCompNotifEnable = _CgmGdoiGmRegCompNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 4, 6),
    _CgmGdoiGmRegCompNotifEnable_Type()
)
cgmGdoiGmRegCompNotifEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiGmRegCompNotifEnable.setStatus("current")
_CgmGdoiGmReRegNotifEnable_Type = TruthValue
_CgmGdoiGmReRegNotifEnable_Object = MibScalar
cgmGdoiGmReRegNotifEnable = _CgmGdoiGmReRegNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 4, 7),
    _CgmGdoiGmReRegNotifEnable_Type()
)
cgmGdoiGmReRegNotifEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiGmReRegNotifEnable.setStatus("current")
_CgmGdoiGmRekeyRecNotifEnable_Type = TruthValue
_CgmGdoiGmRekeyRecNotifEnable_Object = MibScalar
cgmGdoiGmRekeyRecNotifEnable = _CgmGdoiGmRekeyRecNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 4, 8),
    _CgmGdoiGmRekeyRecNotifEnable_Type()
)
cgmGdoiGmRekeyRecNotifEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiGmRekeyRecNotifEnable.setStatus("current")
_CgmGdoiGmIncompCfgNotifEnable_Type = TruthValue
_CgmGdoiGmIncompCfgNotifEnable_Object = MibScalar
cgmGdoiGmIncompCfgNotifEnable = _CgmGdoiGmIncompCfgNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 4, 9),
    _CgmGdoiGmIncompCfgNotifEnable_Type()
)
cgmGdoiGmIncompCfgNotifEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiGmIncompCfgNotifEnable.setStatus("current")
_CgmGdoiGmNoIpSecFlowsNotifEnable_Type = TruthValue
_CgmGdoiGmNoIpSecFlowsNotifEnable_Object = MibScalar
cgmGdoiGmNoIpSecFlowsNotifEnable = _CgmGdoiGmNoIpSecFlowsNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 4, 10),
    _CgmGdoiGmNoIpSecFlowsNotifEnable_Type()
)
cgmGdoiGmNoIpSecFlowsNotifEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiGmNoIpSecFlowsNotifEnable.setStatus("current")
_CgmGdoiGmRekeyFailNotifEnable_Type = TruthValue
_CgmGdoiGmRekeyFailNotifEnable_Object = MibScalar
cgmGdoiGmRekeyFailNotifEnable = _CgmGdoiGmRekeyFailNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 4, 11),
    _CgmGdoiGmRekeyFailNotifEnable_Type()
)
cgmGdoiGmRekeyFailNotifEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiGmRekeyFailNotifEnable.setStatus("current")
_CgmGdoiKsRoleChangeNotifEnable_Type = TruthValue
_CgmGdoiKsRoleChangeNotifEnable_Object = MibScalar
cgmGdoiKsRoleChangeNotifEnable = _CgmGdoiKsRoleChangeNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 4, 12),
    _CgmGdoiKsRoleChangeNotifEnable_Type()
)
cgmGdoiKsRoleChangeNotifEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiKsRoleChangeNotifEnable.setStatus("current")
_CgmGdoiKsGmDeletedNotifEnable_Type = TruthValue
_CgmGdoiKsGmDeletedNotifEnable_Object = MibScalar
cgmGdoiKsGmDeletedNotifEnable = _CgmGdoiKsGmDeletedNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 4, 13),
    _CgmGdoiKsGmDeletedNotifEnable_Type()
)
cgmGdoiKsGmDeletedNotifEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiKsGmDeletedNotifEnable.setStatus("current")
_CgmGdoiKsPeerReachNotifEnable_Type = TruthValue
_CgmGdoiKsPeerReachNotifEnable_Object = MibScalar
cgmGdoiKsPeerReachNotifEnable = _CgmGdoiKsPeerReachNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 4, 14),
    _CgmGdoiKsPeerReachNotifEnable_Type()
)
cgmGdoiKsPeerReachNotifEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiKsPeerReachNotifEnable.setStatus("current")
_CgmGdoiKsPeerUnreachNotifEnable_Type = TruthValue
_CgmGdoiKsPeerUnreachNotifEnable_Object = MibScalar
cgmGdoiKsPeerUnreachNotifEnable = _CgmGdoiKsPeerUnreachNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 4, 15),
    _CgmGdoiKsPeerUnreachNotifEnable_Type()
)
cgmGdoiKsPeerUnreachNotifEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgmGdoiKsPeerUnreachNotifEnable.setStatus("current")
_CgmGdoiNotifVars_ObjectIdentity = ObjectIdentity
cgmGdoiNotifVars = _CgmGdoiNotifVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 5)
)
_CgmGdoiNotifGroupIdType_Type = CgmGdoiIdentificationType
_CgmGdoiNotifGroupIdType_Object = MibScalar
cgmGdoiNotifGroupIdType = _CgmGdoiNotifGroupIdType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 5, 1),
    _CgmGdoiNotifGroupIdType_Type()
)
cgmGdoiNotifGroupIdType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgmGdoiNotifGroupIdType.setStatus("current")
_CgmGdoiNotifGroupIdValue_Type = CgmGdoiIdentificationValue
_CgmGdoiNotifGroupIdValue_Object = MibScalar
cgmGdoiNotifGroupIdValue = _CgmGdoiNotifGroupIdValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 5, 2),
    _CgmGdoiNotifGroupIdValue_Type()
)
cgmGdoiNotifGroupIdValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgmGdoiNotifGroupIdValue.setStatus("current")
_CgmGdoiNotifGroupName_Type = DisplayString
_CgmGdoiNotifGroupName_Object = MibScalar
cgmGdoiNotifGroupName = _CgmGdoiNotifGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 5, 3),
    _CgmGdoiNotifGroupName_Type()
)
cgmGdoiNotifGroupName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgmGdoiNotifGroupName.setStatus("current")
_CgmGdoiNotifKeyServerIdType_Type = CgmGdoiIdentificationType
_CgmGdoiNotifKeyServerIdType_Object = MibScalar
cgmGdoiNotifKeyServerIdType = _CgmGdoiNotifKeyServerIdType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 5, 4),
    _CgmGdoiNotifKeyServerIdType_Type()
)
cgmGdoiNotifKeyServerIdType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgmGdoiNotifKeyServerIdType.setStatus("current")
_CgmGdoiNotifKeyServerIdValue_Type = CgmGdoiIdentificationValue
_CgmGdoiNotifKeyServerIdValue_Object = MibScalar
cgmGdoiNotifKeyServerIdValue = _CgmGdoiNotifKeyServerIdValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 5, 5),
    _CgmGdoiNotifKeyServerIdValue_Type()
)
cgmGdoiNotifKeyServerIdValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgmGdoiNotifKeyServerIdValue.setStatus("current")
_CgmGdoiNotifKeyServerRole_Type = CgmGdoiKsRole
_CgmGdoiNotifKeyServerRole_Object = MibScalar
cgmGdoiNotifKeyServerRole = _CgmGdoiNotifKeyServerRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 5, 6),
    _CgmGdoiNotifKeyServerRole_Type()
)
cgmGdoiNotifKeyServerRole.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgmGdoiNotifKeyServerRole.setStatus("current")
_CgmGdoiNotifGmIdType_Type = CgmGdoiIdentificationType
_CgmGdoiNotifGmIdType_Object = MibScalar
cgmGdoiNotifGmIdType = _CgmGdoiNotifGmIdType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 5, 7),
    _CgmGdoiNotifGmIdType_Type()
)
cgmGdoiNotifGmIdType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgmGdoiNotifGmIdType.setStatus("current")
_CgmGdoiNotifGmIdValue_Type = CgmGdoiIdentificationValue
_CgmGdoiNotifGmIdValue_Object = MibScalar
cgmGdoiNotifGmIdValue = _CgmGdoiNotifGmIdValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 5, 8),
    _CgmGdoiNotifGmIdValue_Type()
)
cgmGdoiNotifGmIdValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgmGdoiNotifGmIdValue.setStatus("current")
_CgmGdoiNotifPeerKsIdType_Type = CgmGdoiIdentificationType
_CgmGdoiNotifPeerKsIdType_Object = MibScalar
cgmGdoiNotifPeerKsIdType = _CgmGdoiNotifPeerKsIdType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 5, 9),
    _CgmGdoiNotifPeerKsIdType_Type()
)
cgmGdoiNotifPeerKsIdType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgmGdoiNotifPeerKsIdType.setStatus("current")
_CgmGdoiNotifPeerKsIdValue_Type = CgmGdoiIdentificationValue
_CgmGdoiNotifPeerKsIdValue_Object = MibScalar
cgmGdoiNotifPeerKsIdValue = _CgmGdoiNotifPeerKsIdValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 1, 5, 10),
    _CgmGdoiNotifPeerKsIdValue_Type()
)
cgmGdoiNotifPeerKsIdValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgmGdoiNotifPeerKsIdValue.setStatus("current")
_CgmGdoiMIBConformance_ObjectIdentity = ObjectIdentity
cgmGdoiMIBConformance = _CgmGdoiMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 2)
)
_CgmGdoiMIBGroups_ObjectIdentity = ObjectIdentity
cgmGdoiMIBGroups = _CgmGdoiMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 2, 1)
)
_CgmGdoiMIBCompliances_ObjectIdentity = ObjectIdentity
cgmGdoiMIBCompliances = _CgmGdoiMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 2, 2)
)

# Managed Objects groups

cgmGdoiGroupIdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 2, 1, 1)
)
cgmGdoiGroupIdGroup.setObjects(
      *(("CISCO-GDOI-MIB", "cgmGdoiGroupIdLength"),
        ("CISCO-GDOI-MIB", "cgmGdoiGroupName"))
)
if mibBuilder.loadTexts:
    cgmGdoiGroupIdGroup.setStatus("current")

cgmGdoiKeyServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 2, 1, 2)
)
cgmGdoiKeyServerGroup.setObjects(
      *(("CISCO-GDOI-MIB", "cgmGdoiKeyServerIdLength"),
        ("CISCO-GDOI-MIB", "cgmGdoiKeyServerActiveKEK"),
        ("CISCO-GDOI-MIB", "cgmGdoiKeyServerRekeysPushed"))
)
if mibBuilder.loadTexts:
    cgmGdoiKeyServerGroup.setStatus("current")

cgmGdoiGmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 2, 1, 3)
)
cgmGdoiGmGroup.setObjects(
      *(("CISCO-GDOI-MIB", "cgmGdoiGmIdLength"),
        ("CISCO-GDOI-MIB", "cgmGdoiGmRegKeyServerIdType"),
        ("CISCO-GDOI-MIB", "cgmGdoiGmRegKeyServerIdLength"),
        ("CISCO-GDOI-MIB", "cgmGdoiGmRegKeyServerIdValue"),
        ("CISCO-GDOI-MIB", "cgmGdoiGmActiveKEK"),
        ("CISCO-GDOI-MIB", "cgmGdoiGmRekeysReceived"))
)
if mibBuilder.loadTexts:
    cgmGdoiGmGroup.setStatus("current")

cgmGdoiKsSecurityAssociationsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 2, 1, 4)
)
cgmGdoiKsSecurityAssociationsGroup.setObjects(
      *(("CISCO-GDOI-MIB", "cgmGdoiKsKekSPI"),
        ("CISCO-GDOI-MIB", "cgmGdoiKsKekSrcIdType"),
        ("CISCO-GDOI-MIB", "cgmGdoiKsKekSrcIdLength"),
        ("CISCO-GDOI-MIB", "cgmGdoiKsKekSrcIdValue"),
        ("CISCO-GDOI-MIB", "cgmGdoiKsKekSrcIdPort"),
        ("CISCO-GDOI-MIB", "cgmGdoiKsKekDstIdType"),
        ("CISCO-GDOI-MIB", "cgmGdoiKsKekDstIdLength"),
        ("CISCO-GDOI-MIB", "cgmGdoiKsKekDstIdValue"),
        ("CISCO-GDOI-MIB", "cgmGdoiKsKekDstIdPort"),
        ("CISCO-GDOI-MIB", "cgmGdoiKsKekIpProtocol"),
        ("CISCO-GDOI-MIB", "cgmGdoiKsKekMgmtAlg"),
        ("CISCO-GDOI-MIB", "cgmGdoiKsKekEncryptAlg"),
        ("CISCO-GDOI-MIB", "cgmGdoiKsKekEncryptKeyLength"),
        ("CISCO-GDOI-MIB", "cgmGdoiKsKekSigHashAlg"),
        ("CISCO-GDOI-MIB", "cgmGdoiKsKekSigAlg"),
        ("CISCO-GDOI-MIB", "cgmGdoiKsKekSigKeyLength"),
        ("CISCO-GDOI-MIB", "cgmGdoiKsKekOakleyGroup"),
        ("CISCO-GDOI-MIB", "cgmGdoiKsKekOriginalLifetime"),
        ("CISCO-GDOI-MIB", "cgmGdoiKsKekRemainingLifetime"),
        ("CISCO-GDOI-MIB", "cgmGdoiKsKekStatus"),
        ("CISCO-GDOI-MIB", "cgmGdoiKsTekSrcIdType"),
        ("CISCO-GDOI-MIB", "cgmGdoiKsTekSrcIdLength"),
        ("CISCO-GDOI-MIB", "cgmGdoiKsTekSrcIdValue"),
        ("CISCO-GDOI-MIB", "cgmGdoiKsTekSrcIdPort"),
        ("CISCO-GDOI-MIB", "cgmGdoiKsTekDstIdType"),
        ("CISCO-GDOI-MIB", "cgmGdoiKsTekDstIdLength"),
        ("CISCO-GDOI-MIB", "cgmGdoiKsTekDstIdValue"),
        ("CISCO-GDOI-MIB", "cgmGdoiKsTekDstIdPort"),
        ("CISCO-GDOI-MIB", "cgmGdoiKsTekSecurityProtocol"),
        ("CISCO-GDOI-MIB", "cgmGdoiKsTekSPI"),
        ("CISCO-GDOI-MIB", "cgmGdoiKsTekEncapsulationMode"),
        ("CISCO-GDOI-MIB", "cgmGdoiKsTekEncryptionAlgorithm"),
        ("CISCO-GDOI-MIB", "cgmGdoiKsTekEncryptionKeyLength"),
        ("CISCO-GDOI-MIB", "cgmGdoiKsTekIntegrityAlgorithm"),
        ("CISCO-GDOI-MIB", "cgmGdoiKsTekIntegrityKeyLength"),
        ("CISCO-GDOI-MIB", "cgmGdoiKsTekWindowSize"),
        ("CISCO-GDOI-MIB", "cgmGdoiKsTekOriginalLifetime"),
        ("CISCO-GDOI-MIB", "cgmGdoiKsTekRemainingLifetime"),
        ("CISCO-GDOI-MIB", "cgmGdoiKsTekStatus"))
)
if mibBuilder.loadTexts:
    cgmGdoiKsSecurityAssociationsGroup.setStatus("current")

cgmGdoiGmSecurityAssociationsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 2, 1, 5)
)
cgmGdoiGmSecurityAssociationsGroup.setObjects(
      *(("CISCO-GDOI-MIB", "cgmGdoiGmKekSPI"),
        ("CISCO-GDOI-MIB", "cgmGdoiGmKekSrcIdType"),
        ("CISCO-GDOI-MIB", "cgmGdoiGmKekSrcIdLength"),
        ("CISCO-GDOI-MIB", "cgmGdoiGmKekSrcIdValue"),
        ("CISCO-GDOI-MIB", "cgmGdoiGmKekSrcIdPort"),
        ("CISCO-GDOI-MIB", "cgmGdoiGmKekDstIdType"),
        ("CISCO-GDOI-MIB", "cgmGdoiGmKekDstIdLength"),
        ("CISCO-GDOI-MIB", "cgmGdoiGmKekDstIdValue"),
        ("CISCO-GDOI-MIB", "cgmGdoiGmKekDstIdPort"),
        ("CISCO-GDOI-MIB", "cgmGdoiGmKekIpProtocol"),
        ("CISCO-GDOI-MIB", "cgmGdoiGmKekMgmtAlg"),
        ("CISCO-GDOI-MIB", "cgmGdoiGmKekEncryptAlg"),
        ("CISCO-GDOI-MIB", "cgmGdoiGmKekEncryptKeyLength"),
        ("CISCO-GDOI-MIB", "cgmGdoiGmKekSigHashAlg"),
        ("CISCO-GDOI-MIB", "cgmGdoiGmKekSigAlg"),
        ("CISCO-GDOI-MIB", "cgmGdoiGmKekSigKeyLength"),
        ("CISCO-GDOI-MIB", "cgmGdoiGmKekOakleyGroup"),
        ("CISCO-GDOI-MIB", "cgmGdoiGmKekOriginalLifetime"),
        ("CISCO-GDOI-MIB", "cgmGdoiGmKekRemainingLifetime"),
        ("CISCO-GDOI-MIB", "cgmGdoiGmKekStatus"),
        ("CISCO-GDOI-MIB", "cgmGdoiGmTekSrcIdType"),
        ("CISCO-GDOI-MIB", "cgmGdoiGmTekSrcIdLength"),
        ("CISCO-GDOI-MIB", "cgmGdoiGmTekSrcIdValue"),
        ("CISCO-GDOI-MIB", "cgmGdoiGmTekSrcIdPort"),
        ("CISCO-GDOI-MIB", "cgmGdoiGmTekDstIdType"),
        ("CISCO-GDOI-MIB", "cgmGdoiGmTekDstIdLength"),
        ("CISCO-GDOI-MIB", "cgmGdoiGmTekDstIdValue"),
        ("CISCO-GDOI-MIB", "cgmGdoiGmTekDstIdPort"),
        ("CISCO-GDOI-MIB", "cgmGdoiGmTekSecurityProtocol"),
        ("CISCO-GDOI-MIB", "cgmGdoiGmTekSPI"),
        ("CISCO-GDOI-MIB", "cgmGdoiGmTekEncapsulationMode"),
        ("CISCO-GDOI-MIB", "cgmGdoiGmTekEncryptionAlgorithm"),
        ("CISCO-GDOI-MIB", "cgmGdoiGmTekEncryptionKeyLength"),
        ("CISCO-GDOI-MIB", "cgmGdoiGmTekIntegrityAlgorithm"),
        ("CISCO-GDOI-MIB", "cgmGdoiGmTekIntegrityKeyLength"),
        ("CISCO-GDOI-MIB", "cgmGdoiGmTekWindowSize"),
        ("CISCO-GDOI-MIB", "cgmGdoiGmTekOriginalLifetime"),
        ("CISCO-GDOI-MIB", "cgmGdoiGmTekRemainingLifetime"),
        ("CISCO-GDOI-MIB", "cgmGdoiGmTekStatus"))
)
if mibBuilder.loadTexts:
    cgmGdoiGmSecurityAssociationsGroup.setStatus("current")

cgmGdoiNotificationControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 2, 1, 10)
)
cgmGdoiNotificationControlGroup.setObjects(
      *(("CISCO-GDOI-MIB", "cgmGdoiKSNewRegNotifEnable"),
        ("CISCO-GDOI-MIB", "cgmGdoiKSRegCompNotifEnable"),
        ("CISCO-GDOI-MIB", "cgmGdoiKSRekeyPushNotifEnable"),
        ("CISCO-GDOI-MIB", "cgmGdoiKSNoRSANotifEnable"),
        ("CISCO-GDOI-MIB", "cgmGdoiGMRegNotifEnable"),
        ("CISCO-GDOI-MIB", "cgmGdoiGmRegCompNotifEnable"),
        ("CISCO-GDOI-MIB", "cgmGdoiGmReRegNotifEnable"),
        ("CISCO-GDOI-MIB", "cgmGdoiGmRekeyRecNotifEnable"),
        ("CISCO-GDOI-MIB", "cgmGdoiGmIncompCfgNotifEnable"),
        ("CISCO-GDOI-MIB", "cgmGdoiGmNoIpSecFlowsNotifEnable"),
        ("CISCO-GDOI-MIB", "cgmGdoiGmRekeyFailNotifEnable"))
)
if mibBuilder.loadTexts:
    cgmGdoiNotificationControlGroup.setStatus("current")

cgmGdoiGroupIdGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 2, 1, 11)
)
cgmGdoiGroupIdGroupRev1.setObjects(
      *(("CISCO-GDOI-MIB", "cgmGdoiGroupMemberCount"),
        ("CISCO-GDOI-MIB", "cgmGdoiGroupActivePeerKeyServerCount"),
        ("CISCO-GDOI-MIB", "cgmGdoiGroupLastRekeyRetransmits"),
        ("CISCO-GDOI-MIB", "cgmGdoiGroupLastRekeyTimeTaken"))
)
if mibBuilder.loadTexts:
    cgmGdoiGroupIdGroupRev1.setStatus("current")

cgmGdoiKeyServerGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 2, 1, 12)
)
cgmGdoiKeyServerGroupRev1.setObjects(
      *(("CISCO-GDOI-MIB", "cgmGdoiKeyServerRole"),
        ("CISCO-GDOI-MIB", "cgmGdoiKeyServerRegisteredGMs"))
)
if mibBuilder.loadTexts:
    cgmGdoiKeyServerGroupRev1.setStatus("current")

cgmGdoiGmGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 2, 1, 13)
)
cgmGdoiGmGroupRev1.setObjects(
    ("CISCO-GDOI-MIB", "cgmGdoiGmActiveTEKNum")
)
if mibBuilder.loadTexts:
    cgmGdoiGmGroupRev1.setStatus("current")

cgmGdoiNotificationControlGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 2, 1, 15)
)
cgmGdoiNotificationControlGroupRev1.setObjects(
      *(("CISCO-GDOI-MIB", "cgmGdoiKsRoleChangeNotifEnable"),
        ("CISCO-GDOI-MIB", "cgmGdoiKsGmDeletedNotifEnable"),
        ("CISCO-GDOI-MIB", "cgmGdoiKsPeerReachNotifEnable"),
        ("CISCO-GDOI-MIB", "cgmGdoiKsPeerUnreachNotifEnable"))
)
if mibBuilder.loadTexts:
    cgmGdoiNotificationControlGroupRev1.setStatus("current")

cgmGdoiCoopPeerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 2, 1, 16)
)
cgmGdoiCoopPeerGroup.setObjects(
      *(("CISCO-GDOI-MIB", "cgmGdoiCoopPeerIdLength"),
        ("CISCO-GDOI-MIB", "cgmGdoiCoopPeerRole"),
        ("CISCO-GDOI-MIB", "cgmGdoiCoopPeerStatus"),
        ("CISCO-GDOI-MIB", "cgmGdoiCoopPeerRegisteredGMs"))
)
if mibBuilder.loadTexts:
    cgmGdoiCoopPeerGroup.setStatus("current")

cgmGdoiNotificationVariablesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 2, 1, 17)
)
cgmGdoiNotificationVariablesGroup.setObjects(
      *(("CISCO-GDOI-MIB", "cgmGdoiNotifGroupIdType"),
        ("CISCO-GDOI-MIB", "cgmGdoiNotifGroupIdValue"),
        ("CISCO-GDOI-MIB", "cgmGdoiNotifGroupName"),
        ("CISCO-GDOI-MIB", "cgmGdoiNotifKeyServerIdType"),
        ("CISCO-GDOI-MIB", "cgmGdoiNotifKeyServerIdValue"),
        ("CISCO-GDOI-MIB", "cgmGdoiNotifKeyServerRole"),
        ("CISCO-GDOI-MIB", "cgmGdoiNotifGmIdType"),
        ("CISCO-GDOI-MIB", "cgmGdoiNotifGmIdValue"),
        ("CISCO-GDOI-MIB", "cgmGdoiNotifPeerKsIdType"),
        ("CISCO-GDOI-MIB", "cgmGdoiNotifPeerKsIdValue"))
)
if mibBuilder.loadTexts:
    cgmGdoiNotificationVariablesGroup.setStatus("current")


# Notification objects

cgmGdoiKeyServerNewRegistration = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 0, 1)
)
if mibBuilder.loadTexts:
    cgmGdoiKeyServerNewRegistration.setStatus(
        "current"
    )

cgmGdoiKeyServerRegistrationComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 0, 2)
)
if mibBuilder.loadTexts:
    cgmGdoiKeyServerRegistrationComplete.setStatus(
        "current"
    )

cgmGdoiKeyServerRekeyPushed = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 0, 3)
)
cgmGdoiKeyServerRekeyPushed.setObjects(
    ("CISCO-GDOI-MIB", "cgmGdoiKeyServerRekeysPushed")
)
if mibBuilder.loadTexts:
    cgmGdoiKeyServerRekeyPushed.setStatus(
        "current"
    )

cgmGdoiKeyServerNoRsaKeys = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 0, 4)
)
if mibBuilder.loadTexts:
    cgmGdoiKeyServerNoRsaKeys.setStatus(
        "current"
    )

cgmGdoiGmRegister = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 0, 5)
)
cgmGdoiGmRegister.setObjects(
      *(("CISCO-GDOI-MIB", "cgmGdoiGmRegKeyServerIdType"),
        ("CISCO-GDOI-MIB", "cgmGdoiGmRegKeyServerIdValue"))
)
if mibBuilder.loadTexts:
    cgmGdoiGmRegister.setStatus(
        "current"
    )

cgmGdoiGmRegistrationComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 0, 6)
)
cgmGdoiGmRegistrationComplete.setObjects(
      *(("CISCO-GDOI-MIB", "cgmGdoiGmRegKeyServerIdType"),
        ("CISCO-GDOI-MIB", "cgmGdoiGmRegKeyServerIdValue"))
)
if mibBuilder.loadTexts:
    cgmGdoiGmRegistrationComplete.setStatus(
        "current"
    )

cgmGdoiGmReRegister = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 0, 7)
)
cgmGdoiGmReRegister.setObjects(
      *(("CISCO-GDOI-MIB", "cgmGdoiGmRegKeyServerIdType"),
        ("CISCO-GDOI-MIB", "cgmGdoiGmRegKeyServerIdValue"))
)
if mibBuilder.loadTexts:
    cgmGdoiGmReRegister.setStatus(
        "current"
    )

cgmGdoiGmRekeyReceived = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 0, 8)
)
cgmGdoiGmRekeyReceived.setObjects(
      *(("CISCO-GDOI-MIB", "cgmGdoiGmRegKeyServerIdType"),
        ("CISCO-GDOI-MIB", "cgmGdoiGmRegKeyServerIdValue"),
        ("CISCO-GDOI-MIB", "cgmGdoiGmRekeysReceived"))
)
if mibBuilder.loadTexts:
    cgmGdoiGmRekeyReceived.setStatus(
        "current"
    )

cgmGdoiGmIncompleteCfg = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 0, 9)
)
if mibBuilder.loadTexts:
    cgmGdoiGmIncompleteCfg.setStatus(
        "current"
    )

cgmGdoiGmNoIpSecFlows = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 0, 10)
)
if mibBuilder.loadTexts:
    cgmGdoiGmNoIpSecFlows.setStatus(
        "current"
    )

cgmGdoiGmRekeyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 0, 11)
)
cgmGdoiGmRekeyFailure.setObjects(
      *(("CISCO-GDOI-MIB", "cgmGdoiGmRegKeyServerIdType"),
        ("CISCO-GDOI-MIB", "cgmGdoiGmRegKeyServerIdValue"),
        ("CISCO-GDOI-MIB", "cgmGdoiGmRekeysReceived"))
)
if mibBuilder.loadTexts:
    cgmGdoiGmRekeyFailure.setStatus(
        "current"
    )

cgmGdoiKeyServerRoleChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 0, 12)
)
cgmGdoiKeyServerRoleChange.setObjects(
      *(("CISCO-GDOI-MIB", "cgmGdoiNotifGroupIdType"),
        ("CISCO-GDOI-MIB", "cgmGdoiNotifGroupIdValue"),
        ("CISCO-GDOI-MIB", "cgmGdoiNotifGroupName"),
        ("CISCO-GDOI-MIB", "cgmGdoiNotifKeyServerIdType"),
        ("CISCO-GDOI-MIB", "cgmGdoiNotifKeyServerIdValue"),
        ("CISCO-GDOI-MIB", "cgmGdoiNotifKeyServerRole"))
)
if mibBuilder.loadTexts:
    cgmGdoiKeyServerRoleChange.setStatus(
        "current"
    )

cgmGdoiKeyServerGmDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 0, 13)
)
cgmGdoiKeyServerGmDeleted.setObjects(
      *(("CISCO-GDOI-MIB", "cgmGdoiNotifGroupIdType"),
        ("CISCO-GDOI-MIB", "cgmGdoiNotifGroupIdValue"),
        ("CISCO-GDOI-MIB", "cgmGdoiNotifGroupName"),
        ("CISCO-GDOI-MIB", "cgmGdoiNotifKeyServerIdType"),
        ("CISCO-GDOI-MIB", "cgmGdoiNotifKeyServerIdValue"),
        ("CISCO-GDOI-MIB", "cgmGdoiNotifGmIdType"),
        ("CISCO-GDOI-MIB", "cgmGdoiNotifGmIdValue"))
)
if mibBuilder.loadTexts:
    cgmGdoiKeyServerGmDeleted.setStatus(
        "current"
    )

cgmGdoiKeyServerPeerReachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 0, 14)
)
cgmGdoiKeyServerPeerReachable.setObjects(
      *(("CISCO-GDOI-MIB", "cgmGdoiNotifGroupIdType"),
        ("CISCO-GDOI-MIB", "cgmGdoiNotifGroupIdValue"),
        ("CISCO-GDOI-MIB", "cgmGdoiNotifGroupName"),
        ("CISCO-GDOI-MIB", "cgmGdoiNotifKeyServerIdType"),
        ("CISCO-GDOI-MIB", "cgmGdoiNotifKeyServerIdValue"),
        ("CISCO-GDOI-MIB", "cgmGdoiNotifPeerKsIdType"),
        ("CISCO-GDOI-MIB", "cgmGdoiNotifPeerKsIdValue"))
)
if mibBuilder.loadTexts:
    cgmGdoiKeyServerPeerReachable.setStatus(
        "current"
    )

cgmGdoiKeyServerPeerUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 0, 15)
)
cgmGdoiKeyServerPeerUnreachable.setObjects(
      *(("CISCO-GDOI-MIB", "cgmGdoiNotifGroupIdType"),
        ("CISCO-GDOI-MIB", "cgmGdoiNotifGroupIdValue"),
        ("CISCO-GDOI-MIB", "cgmGdoiNotifGroupName"),
        ("CISCO-GDOI-MIB", "cgmGdoiNotifKeyServerIdType"),
        ("CISCO-GDOI-MIB", "cgmGdoiNotifKeyServerIdValue"),
        ("CISCO-GDOI-MIB", "cgmGdoiNotifPeerKsIdType"),
        ("CISCO-GDOI-MIB", "cgmGdoiNotifPeerKsIdValue"))
)
if mibBuilder.loadTexts:
    cgmGdoiKeyServerPeerUnreachable.setStatus(
        "current"
    )


# Notifications groups

cgmGdoiKeyServerNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 2, 1, 6)
)
cgmGdoiKeyServerNotificationGroup.setObjects(
      *(("CISCO-GDOI-MIB", "cgmGdoiKeyServerNewRegistration"),
        ("CISCO-GDOI-MIB", "cgmGdoiKeyServerRegistrationComplete"),
        ("CISCO-GDOI-MIB", "cgmGdoiKeyServerRekeyPushed"))
)
if mibBuilder.loadTexts:
    cgmGdoiKeyServerNotificationGroup.setStatus(
        "current"
    )

cgmGdoiKeyServerErrorNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 2, 1, 7)
)
cgmGdoiKeyServerErrorNotificationGroup.setObjects(
    ("CISCO-GDOI-MIB", "cgmGdoiKeyServerNoRsaKeys")
)
if mibBuilder.loadTexts:
    cgmGdoiKeyServerErrorNotificationGroup.setStatus(
        "current"
    )

cgmGdoiGmNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 2, 1, 8)
)
cgmGdoiGmNotificationGroup.setObjects(
      *(("CISCO-GDOI-MIB", "cgmGdoiGmRegister"),
        ("CISCO-GDOI-MIB", "cgmGdoiGmRegistrationComplete"),
        ("CISCO-GDOI-MIB", "cgmGdoiGmReRegister"),
        ("CISCO-GDOI-MIB", "cgmGdoiGmRekeyReceived"))
)
if mibBuilder.loadTexts:
    cgmGdoiGmNotificationGroup.setStatus(
        "current"
    )

cgmGdoiGmErrorNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 2, 1, 9)
)
cgmGdoiGmErrorNotificationGroup.setObjects(
      *(("CISCO-GDOI-MIB", "cgmGdoiGmIncompleteCfg"),
        ("CISCO-GDOI-MIB", "cgmGdoiGmNoIpSecFlows"),
        ("CISCO-GDOI-MIB", "cgmGdoiGmRekeyFailure"))
)
if mibBuilder.loadTexts:
    cgmGdoiGmErrorNotificationGroup.setStatus(
        "current"
    )

cgmGdoiKeyServerNotificationGroupRev1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 2, 1, 14)
)
cgmGdoiKeyServerNotificationGroupRev1.setObjects(
      *(("CISCO-GDOI-MIB", "cgmGdoiKeyServerRoleChange"),
        ("CISCO-GDOI-MIB", "cgmGdoiKeyServerGmDeleted"),
        ("CISCO-GDOI-MIB", "cgmGdoiKeyServerPeerReachable"),
        ("CISCO-GDOI-MIB", "cgmGdoiKeyServerPeerUnreachable"))
)
if mibBuilder.loadTexts:
    cgmGdoiKeyServerNotificationGroupRev1.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cgmGdoiMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cgmGdoiMIBCompliance.setStatus(
        "deprecated"
    )

cgmGdoiMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 759, 2, 2, 2)
)
if mibBuilder.loadTexts:
    cgmGdoiMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-GDOI-MIB",
    **{"CgmGdoiKsStatus": CgmGdoiKsStatus,
       "CgmGdoiKsRole": CgmGdoiKsRole,
       "CgmGdoiIdentificationType": CgmGdoiIdentificationType,
       "CgmGdoiIdentificationValue": CgmGdoiIdentificationValue,
       "CgmGdoiKekSPI": CgmGdoiKekSPI,
       "CgmGdoiIpProtocolId": CgmGdoiIpProtocolId,
       "CgmGdoiKeyManagementAlgorithm": CgmGdoiKeyManagementAlgorithm,
       "CgmGdoiEncryptionAlgorithm": CgmGdoiEncryptionAlgorithm,
       "CgmGdoiPseudoRandomFunction": CgmGdoiPseudoRandomFunction,
       "CgmGdoiIntegrityAlgorithm": CgmGdoiIntegrityAlgorithm,
       "CgmGdoiSignatureMethod": CgmGdoiSignatureMethod,
       "CgmGdoiDiffieHellmanGroup": CgmGdoiDiffieHellmanGroup,
       "CgmGdoiEncapsulationMode": CgmGdoiEncapsulationMode,
       "CgmGdoiSecurityProtocol": CgmGdoiSecurityProtocol,
       "CgmGdoiTekSPI": CgmGdoiTekSPI,
       "CgmGdoiKekStatus": CgmGdoiKekStatus,
       "CgmGdoiTekStatus": CgmGdoiTekStatus,
       "CgmGdoiUnsigned16": CgmGdoiUnsigned16,
       "ciscoGdoiMIB": ciscoGdoiMIB,
       "cgmGdoiMIBNotifications": cgmGdoiMIBNotifications,
       "cgmGdoiKeyServerNewRegistration": cgmGdoiKeyServerNewRegistration,
       "cgmGdoiKeyServerRegistrationComplete": cgmGdoiKeyServerRegistrationComplete,
       "cgmGdoiKeyServerRekeyPushed": cgmGdoiKeyServerRekeyPushed,
       "cgmGdoiKeyServerNoRsaKeys": cgmGdoiKeyServerNoRsaKeys,
       "cgmGdoiGmRegister": cgmGdoiGmRegister,
       "cgmGdoiGmRegistrationComplete": cgmGdoiGmRegistrationComplete,
       "cgmGdoiGmReRegister": cgmGdoiGmReRegister,
       "cgmGdoiGmRekeyReceived": cgmGdoiGmRekeyReceived,
       "cgmGdoiGmIncompleteCfg": cgmGdoiGmIncompleteCfg,
       "cgmGdoiGmNoIpSecFlows": cgmGdoiGmNoIpSecFlows,
       "cgmGdoiGmRekeyFailure": cgmGdoiGmRekeyFailure,
       "cgmGdoiKeyServerRoleChange": cgmGdoiKeyServerRoleChange,
       "cgmGdoiKeyServerGmDeleted": cgmGdoiKeyServerGmDeleted,
       "cgmGdoiKeyServerPeerReachable": cgmGdoiKeyServerPeerReachable,
       "cgmGdoiKeyServerPeerUnreachable": cgmGdoiKeyServerPeerUnreachable,
       "cgmGdoiMIBObjects": cgmGdoiMIBObjects,
       "cgmGdoiGroupTable": cgmGdoiGroupTable,
       "cgmGdoiGroupEntry": cgmGdoiGroupEntry,
       "cgmGdoiGroupIdType": cgmGdoiGroupIdType,
       "cgmGdoiGroupIdLength": cgmGdoiGroupIdLength,
       "cgmGdoiGroupIdValue": cgmGdoiGroupIdValue,
       "cgmGdoiGroupName": cgmGdoiGroupName,
       "cgmGdoiGroupMemberCount": cgmGdoiGroupMemberCount,
       "cgmGdoiGroupActivePeerKeyServerCount": cgmGdoiGroupActivePeerKeyServerCount,
       "cgmGdoiGroupLastRekeyRetransmits": cgmGdoiGroupLastRekeyRetransmits,
       "cgmGdoiGroupLastRekeyTimeTaken": cgmGdoiGroupLastRekeyTimeTaken,
       "cgmGdoiPeers": cgmGdoiPeers,
       "cgmGdoiKeyServerTable": cgmGdoiKeyServerTable,
       "cgmGdoiKeyServerEntry": cgmGdoiKeyServerEntry,
       "cgmGdoiKeyServerIdType": cgmGdoiKeyServerIdType,
       "cgmGdoiKeyServerIdLength": cgmGdoiKeyServerIdLength,
       "cgmGdoiKeyServerIdValue": cgmGdoiKeyServerIdValue,
       "cgmGdoiKeyServerActiveKEK": cgmGdoiKeyServerActiveKEK,
       "cgmGdoiKeyServerRekeysPushed": cgmGdoiKeyServerRekeysPushed,
       "cgmGdoiKeyServerRole": cgmGdoiKeyServerRole,
       "cgmGdoiKeyServerRegisteredGMs": cgmGdoiKeyServerRegisteredGMs,
       "cgmGdoiGmTable": cgmGdoiGmTable,
       "cgmGdoiGmEntry": cgmGdoiGmEntry,
       "cgmGdoiGmIdType": cgmGdoiGmIdType,
       "cgmGdoiGmIdLength": cgmGdoiGmIdLength,
       "cgmGdoiGmIdValue": cgmGdoiGmIdValue,
       "cgmGdoiGmRegKeyServerIdType": cgmGdoiGmRegKeyServerIdType,
       "cgmGdoiGmRegKeyServerIdLength": cgmGdoiGmRegKeyServerIdLength,
       "cgmGdoiGmRegKeyServerIdValue": cgmGdoiGmRegKeyServerIdValue,
       "cgmGdoiGmActiveKEK": cgmGdoiGmActiveKEK,
       "cgmGdoiGmRekeysReceived": cgmGdoiGmRekeysReceived,
       "cgmGdoiGmActiveTEKNum": cgmGdoiGmActiveTEKNum,
       "cgmGdoiCoopPeerTable": cgmGdoiCoopPeerTable,
       "cgmGdoiCoopPeerEntry": cgmGdoiCoopPeerEntry,
       "cgmGdoiCoopPeerIdType": cgmGdoiCoopPeerIdType,
       "cgmGdoiCoopPeerIdLength": cgmGdoiCoopPeerIdLength,
       "cgmGdoiCoopPeerIdValue": cgmGdoiCoopPeerIdValue,
       "cgmGdoiCoopPeerRole": cgmGdoiCoopPeerRole,
       "cgmGdoiCoopPeerStatus": cgmGdoiCoopPeerStatus,
       "cgmGdoiCoopPeerRegisteredGMs": cgmGdoiCoopPeerRegisteredGMs,
       "cgmGdoiSecAssociations": cgmGdoiSecAssociations,
       "cgmGdoiKsKekTable": cgmGdoiKsKekTable,
       "cgmGdoiKsKekEntry": cgmGdoiKsKekEntry,
       "cgmGdoiKsKekIndex": cgmGdoiKsKekIndex,
       "cgmGdoiKsKekSPI": cgmGdoiKsKekSPI,
       "cgmGdoiKsKekSrcIdType": cgmGdoiKsKekSrcIdType,
       "cgmGdoiKsKekSrcIdLength": cgmGdoiKsKekSrcIdLength,
       "cgmGdoiKsKekSrcIdValue": cgmGdoiKsKekSrcIdValue,
       "cgmGdoiKsKekSrcIdPort": cgmGdoiKsKekSrcIdPort,
       "cgmGdoiKsKekDstIdType": cgmGdoiKsKekDstIdType,
       "cgmGdoiKsKekDstIdLength": cgmGdoiKsKekDstIdLength,
       "cgmGdoiKsKekDstIdValue": cgmGdoiKsKekDstIdValue,
       "cgmGdoiKsKekDstIdPort": cgmGdoiKsKekDstIdPort,
       "cgmGdoiKsKekIpProtocol": cgmGdoiKsKekIpProtocol,
       "cgmGdoiKsKekMgmtAlg": cgmGdoiKsKekMgmtAlg,
       "cgmGdoiKsKekEncryptAlg": cgmGdoiKsKekEncryptAlg,
       "cgmGdoiKsKekEncryptKeyLength": cgmGdoiKsKekEncryptKeyLength,
       "cgmGdoiKsKekSigHashAlg": cgmGdoiKsKekSigHashAlg,
       "cgmGdoiKsKekSigAlg": cgmGdoiKsKekSigAlg,
       "cgmGdoiKsKekSigKeyLength": cgmGdoiKsKekSigKeyLength,
       "cgmGdoiKsKekOakleyGroup": cgmGdoiKsKekOakleyGroup,
       "cgmGdoiKsKekOriginalLifetime": cgmGdoiKsKekOriginalLifetime,
       "cgmGdoiKsKekRemainingLifetime": cgmGdoiKsKekRemainingLifetime,
       "cgmGdoiKsKekStatus": cgmGdoiKsKekStatus,
       "cgmGdoiGmKekTable": cgmGdoiGmKekTable,
       "cgmGdoiGmKekEntry": cgmGdoiGmKekEntry,
       "cgmGdoiGmKekIndex": cgmGdoiGmKekIndex,
       "cgmGdoiGmKekSPI": cgmGdoiGmKekSPI,
       "cgmGdoiGmKekSrcIdType": cgmGdoiGmKekSrcIdType,
       "cgmGdoiGmKekSrcIdLength": cgmGdoiGmKekSrcIdLength,
       "cgmGdoiGmKekSrcIdValue": cgmGdoiGmKekSrcIdValue,
       "cgmGdoiGmKekSrcIdPort": cgmGdoiGmKekSrcIdPort,
       "cgmGdoiGmKekDstIdType": cgmGdoiGmKekDstIdType,
       "cgmGdoiGmKekDstIdLength": cgmGdoiGmKekDstIdLength,
       "cgmGdoiGmKekDstIdValue": cgmGdoiGmKekDstIdValue,
       "cgmGdoiGmKekDstIdPort": cgmGdoiGmKekDstIdPort,
       "cgmGdoiGmKekIpProtocol": cgmGdoiGmKekIpProtocol,
       "cgmGdoiGmKekMgmtAlg": cgmGdoiGmKekMgmtAlg,
       "cgmGdoiGmKekEncryptAlg": cgmGdoiGmKekEncryptAlg,
       "cgmGdoiGmKekEncryptKeyLength": cgmGdoiGmKekEncryptKeyLength,
       "cgmGdoiGmKekSigHashAlg": cgmGdoiGmKekSigHashAlg,
       "cgmGdoiGmKekSigAlg": cgmGdoiGmKekSigAlg,
       "cgmGdoiGmKekSigKeyLength": cgmGdoiGmKekSigKeyLength,
       "cgmGdoiGmKekOakleyGroup": cgmGdoiGmKekOakleyGroup,
       "cgmGdoiGmKekOriginalLifetime": cgmGdoiGmKekOriginalLifetime,
       "cgmGdoiGmKekRemainingLifetime": cgmGdoiGmKekRemainingLifetime,
       "cgmGdoiGmKekStatus": cgmGdoiGmKekStatus,
       "cgmGdoiKsTekSelectorTable": cgmGdoiKsTekSelectorTable,
       "cgmGdoiKsTekSelectorEntry": cgmGdoiKsTekSelectorEntry,
       "cgmGdoiKsTekSelectorIndex": cgmGdoiKsTekSelectorIndex,
       "cgmGdoiKsTekSrcIdType": cgmGdoiKsTekSrcIdType,
       "cgmGdoiKsTekSrcIdLength": cgmGdoiKsTekSrcIdLength,
       "cgmGdoiKsTekSrcIdValue": cgmGdoiKsTekSrcIdValue,
       "cgmGdoiKsTekSrcIdPort": cgmGdoiKsTekSrcIdPort,
       "cgmGdoiKsTekDstIdType": cgmGdoiKsTekDstIdType,
       "cgmGdoiKsTekDstIdLength": cgmGdoiKsTekDstIdLength,
       "cgmGdoiKsTekDstIdValue": cgmGdoiKsTekDstIdValue,
       "cgmGdoiKsTekDstIdPort": cgmGdoiKsTekDstIdPort,
       "cgmGdoiKsTekSecurityProtocol": cgmGdoiKsTekSecurityProtocol,
       "cgmGdoiKsTekPolicyTable": cgmGdoiKsTekPolicyTable,
       "cgmGdoiKsTekPolicyEntry": cgmGdoiKsTekPolicyEntry,
       "cgmGdoiKsTekPolicyIndex": cgmGdoiKsTekPolicyIndex,
       "cgmGdoiKsTekSPI": cgmGdoiKsTekSPI,
       "cgmGdoiKsTekEncapsulationMode": cgmGdoiKsTekEncapsulationMode,
       "cgmGdoiKsTekEncryptionAlgorithm": cgmGdoiKsTekEncryptionAlgorithm,
       "cgmGdoiKsTekEncryptionKeyLength": cgmGdoiKsTekEncryptionKeyLength,
       "cgmGdoiKsTekIntegrityAlgorithm": cgmGdoiKsTekIntegrityAlgorithm,
       "cgmGdoiKsTekIntegrityKeyLength": cgmGdoiKsTekIntegrityKeyLength,
       "cgmGdoiKsTekWindowSize": cgmGdoiKsTekWindowSize,
       "cgmGdoiKsTekOriginalLifetime": cgmGdoiKsTekOriginalLifetime,
       "cgmGdoiKsTekRemainingLifetime": cgmGdoiKsTekRemainingLifetime,
       "cgmGdoiKsTekStatus": cgmGdoiKsTekStatus,
       "cgmGdoiGmTekSelectorTable": cgmGdoiGmTekSelectorTable,
       "cgmGdoiGmTekSelectorEntry": cgmGdoiGmTekSelectorEntry,
       "cgmGdoiGmTekSelectorIndex": cgmGdoiGmTekSelectorIndex,
       "cgmGdoiGmTekSrcIdType": cgmGdoiGmTekSrcIdType,
       "cgmGdoiGmTekSrcIdLength": cgmGdoiGmTekSrcIdLength,
       "cgmGdoiGmTekSrcIdValue": cgmGdoiGmTekSrcIdValue,
       "cgmGdoiGmTekSrcIdPort": cgmGdoiGmTekSrcIdPort,
       "cgmGdoiGmTekDstIdType": cgmGdoiGmTekDstIdType,
       "cgmGdoiGmTekDstIdLength": cgmGdoiGmTekDstIdLength,
       "cgmGdoiGmTekDstIdValue": cgmGdoiGmTekDstIdValue,
       "cgmGdoiGmTekDstIdPort": cgmGdoiGmTekDstIdPort,
       "cgmGdoiGmTekSecurityProtocol": cgmGdoiGmTekSecurityProtocol,
       "cgmGdoiGmTekPolicyTable": cgmGdoiGmTekPolicyTable,
       "cgmGdoiGmTekPolicyEntry": cgmGdoiGmTekPolicyEntry,
       "cgmGdoiGmTekPolicyIndex": cgmGdoiGmTekPolicyIndex,
       "cgmGdoiGmTekSPI": cgmGdoiGmTekSPI,
       "cgmGdoiGmTekEncapsulationMode": cgmGdoiGmTekEncapsulationMode,
       "cgmGdoiGmTekEncryptionAlgorithm": cgmGdoiGmTekEncryptionAlgorithm,
       "cgmGdoiGmTekEncryptionKeyLength": cgmGdoiGmTekEncryptionKeyLength,
       "cgmGdoiGmTekIntegrityAlgorithm": cgmGdoiGmTekIntegrityAlgorithm,
       "cgmGdoiGmTekIntegrityKeyLength": cgmGdoiGmTekIntegrityKeyLength,
       "cgmGdoiGmTekWindowSize": cgmGdoiGmTekWindowSize,
       "cgmGdoiGmTekOriginalLifetime": cgmGdoiGmTekOriginalLifetime,
       "cgmGdoiGmTekRemainingLifetime": cgmGdoiGmTekRemainingLifetime,
       "cgmGdoiGmTekStatus": cgmGdoiGmTekStatus,
       "cgmGdoiNotifCntl": cgmGdoiNotifCntl,
       "cgmGdoiKSNewRegNotifEnable": cgmGdoiKSNewRegNotifEnable,
       "cgmGdoiKSRegCompNotifEnable": cgmGdoiKSRegCompNotifEnable,
       "cgmGdoiKSRekeyPushNotifEnable": cgmGdoiKSRekeyPushNotifEnable,
       "cgmGdoiKSNoRSANotifEnable": cgmGdoiKSNoRSANotifEnable,
       "cgmGdoiGMRegNotifEnable": cgmGdoiGMRegNotifEnable,
       "cgmGdoiGmRegCompNotifEnable": cgmGdoiGmRegCompNotifEnable,
       "cgmGdoiGmReRegNotifEnable": cgmGdoiGmReRegNotifEnable,
       "cgmGdoiGmRekeyRecNotifEnable": cgmGdoiGmRekeyRecNotifEnable,
       "cgmGdoiGmIncompCfgNotifEnable": cgmGdoiGmIncompCfgNotifEnable,
       "cgmGdoiGmNoIpSecFlowsNotifEnable": cgmGdoiGmNoIpSecFlowsNotifEnable,
       "cgmGdoiGmRekeyFailNotifEnable": cgmGdoiGmRekeyFailNotifEnable,
       "cgmGdoiKsRoleChangeNotifEnable": cgmGdoiKsRoleChangeNotifEnable,
       "cgmGdoiKsGmDeletedNotifEnable": cgmGdoiKsGmDeletedNotifEnable,
       "cgmGdoiKsPeerReachNotifEnable": cgmGdoiKsPeerReachNotifEnable,
       "cgmGdoiKsPeerUnreachNotifEnable": cgmGdoiKsPeerUnreachNotifEnable,
       "cgmGdoiNotifVars": cgmGdoiNotifVars,
       "cgmGdoiNotifGroupIdType": cgmGdoiNotifGroupIdType,
       "cgmGdoiNotifGroupIdValue": cgmGdoiNotifGroupIdValue,
       "cgmGdoiNotifGroupName": cgmGdoiNotifGroupName,
       "cgmGdoiNotifKeyServerIdType": cgmGdoiNotifKeyServerIdType,
       "cgmGdoiNotifKeyServerIdValue": cgmGdoiNotifKeyServerIdValue,
       "cgmGdoiNotifKeyServerRole": cgmGdoiNotifKeyServerRole,
       "cgmGdoiNotifGmIdType": cgmGdoiNotifGmIdType,
       "cgmGdoiNotifGmIdValue": cgmGdoiNotifGmIdValue,
       "cgmGdoiNotifPeerKsIdType": cgmGdoiNotifPeerKsIdType,
       "cgmGdoiNotifPeerKsIdValue": cgmGdoiNotifPeerKsIdValue,
       "cgmGdoiMIBConformance": cgmGdoiMIBConformance,
       "cgmGdoiMIBGroups": cgmGdoiMIBGroups,
       "cgmGdoiGroupIdGroup": cgmGdoiGroupIdGroup,
       "cgmGdoiKeyServerGroup": cgmGdoiKeyServerGroup,
       "cgmGdoiGmGroup": cgmGdoiGmGroup,
       "cgmGdoiKsSecurityAssociationsGroup": cgmGdoiKsSecurityAssociationsGroup,
       "cgmGdoiGmSecurityAssociationsGroup": cgmGdoiGmSecurityAssociationsGroup,
       "cgmGdoiKeyServerNotificationGroup": cgmGdoiKeyServerNotificationGroup,
       "cgmGdoiKeyServerErrorNotificationGroup": cgmGdoiKeyServerErrorNotificationGroup,
       "cgmGdoiGmNotificationGroup": cgmGdoiGmNotificationGroup,
       "cgmGdoiGmErrorNotificationGroup": cgmGdoiGmErrorNotificationGroup,
       "cgmGdoiNotificationControlGroup": cgmGdoiNotificationControlGroup,
       "cgmGdoiGroupIdGroupRev1": cgmGdoiGroupIdGroupRev1,
       "cgmGdoiKeyServerGroupRev1": cgmGdoiKeyServerGroupRev1,
       "cgmGdoiGmGroupRev1": cgmGdoiGmGroupRev1,
       "cgmGdoiKeyServerNotificationGroupRev1": cgmGdoiKeyServerNotificationGroupRev1,
       "cgmGdoiNotificationControlGroupRev1": cgmGdoiNotificationControlGroupRev1,
       "cgmGdoiCoopPeerGroup": cgmGdoiCoopPeerGroup,
       "cgmGdoiNotificationVariablesGroup": cgmGdoiNotificationVariablesGroup,
       "cgmGdoiMIBCompliances": cgmGdoiMIBCompliances,
       "cgmGdoiMIBCompliance": cgmGdoiMIBCompliance,
       "cgmGdoiMIBComplianceRev1": cgmGdoiMIBComplianceRev1}
)
