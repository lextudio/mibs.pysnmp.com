# SNMP MIB module (IPSEC-ISAKMP-IKE-DOI-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IPSEC-ISAKMP-IKE-DOI-TC
# Produced by pysmi-1.5.4 at Mon Oct 14 22:11:12 2024
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
 experimental,
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "experimental",
    "iso",
    "mib-2")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(watchguard,) = mibBuilder.importSymbols(
    "WATCHGUARD-MIB",
    "watchguard")


# MODULE-IDENTITY

ipsecIsakmpIkeDoiTC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 100)
)
ipsecIsakmpIkeDoiTC.setRevisions(
        ("1999-02-18 17:05",
         "1999-03-05 15:45",
         "1999-07-13 21:45",
         "1999-10-05 17:05",
         "1999-10-15 19:50")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class IpsecDoiSituation(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "x"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class IpsecDoiSecProtocolId(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
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
        *(("protoIpcomp", 4),
          ("protoIpsecAh", 2),
          ("protoIpsecEsp", 3),
          ("protoIsakmp", 1),
          ("reserved", 0))
    )



class IpsecDoiTransformIdent(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("keyIke", 1),
          ("reserved", 0))
    )



class IpsecDoiAhTransform(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
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
        *(("ahDes", 4),
          ("ahMd5", 2),
          ("ahSha", 3),
          ("reserved", 0),
          ("reserved1", 1))
    )



class IpsecDoiEspTransform(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("esp3Des", 3),
          ("esp3Idea", 8),
          ("espBlowfish", 7),
          ("espCast", 6),
          ("espDes", 2),
          ("espDesIv32", 9),
          ("espDesIv64", 1),
          ("espIdea", 5),
          ("espNull", 11),
          ("espRc4", 10),
          ("espRc5", 4),
          ("reserved", 0))
    )



class IpsecDoiAuthAlgorithm(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
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
        *(("desMac", 3),
          ("hmacMd5", 1),
          ("hmacSha", 2),
          ("kpdk", 4),
          ("reserved", 0))
    )



class IpsecDoiIpcompTransform(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
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
        *(("ipcompDeflate", 2),
          ("ipcompLzs", 3),
          ("ipcompOui", 1),
          ("reserved", 0))
    )



class IpsecDoiEncapsulationMode(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reserved", 0),
          ("transport", 2),
          ("tunnel", 1))
    )



class IpsecDoiIdentType(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("idDerAsn1Dn", 9),
          ("idDerAsn1Gn", 10),
          ("idFqdn", 2),
          ("idIpv4Addr", 1),
          ("idIpv4AddrRange", 7),
          ("idIpv4AddrSubnet", 4),
          ("idIpv6Addr", 5),
          ("idIpv6AddrRange", 8),
          ("idIpv6AddrSubnet", 6),
          ("idKeyId", 11),
          ("idUserFqdn", 3),
          ("reserved", 0))
    )



class IsakmpDOI(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ipsecDOI", 1),
          ("isakmp", 0))
    )



class IsakmpCertificateEncoding(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("arl", 8),
          ("crl", 7),
          ("dnsSignedKey", 3),
          ("kerberosTokens", 6),
          ("pgp", 2),
          ("pkcs7", 1),
          ("spki", 9),
          ("x509Attribute", 10),
          ("x509KeyExchange", 5),
          ("x509Signature", 4))
    )



class IsakmpExchangeType(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("aggressive", 4),
          ("authOnly", 3),
          ("base", 1),
          ("identityProtect", 2),
          ("informational", 5),
          ("reserved", 0))
    )



class IsakmpNotifyMessageType(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
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
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30)
        )
    )
    namedValues = NamedValues(
        *(("addressNotification", 26),
          ("attributesNotSupported", 13),
          ("authenticationFailed", 24),
          ("badProposalSyntax", 15),
          ("certTypeUnsupported", 21),
          ("certificateUnavailable", 28),
          ("doiNotSupported", 2),
          ("invalidCertAuthority", 22),
          ("invalidCertEncoding", 19),
          ("invalidCertificate", 20),
          ("invalidCookie", 4),
          ("invalidExchangeType", 7),
          ("invalidFlags", 8),
          ("invalidHashInformation", 23),
          ("invalidIdInformation", 18),
          ("invalidKeyInformation", 17),
          ("invalidMajorVersion", 5),
          ("invalidMessageId", 9),
          ("invalidMinorVersion", 6),
          ("invalidPayloadType", 1),
          ("invalidProtocolId", 10),
          ("invalidSignature", 25),
          ("invalidSpi", 11),
          ("invalidTransformId", 12),
          ("noProposalChosen", 14),
          ("notifySaLifetime", 27),
          ("payloadMalformed", 16),
          ("reserved", 0),
          ("situationNotSupported", 3),
          ("unequalPayloadLengths", 30),
          ("unsupportedExchangeType", 29))
    )



class IkeExchangeType(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              32,
              33,
              34)
        )
    )
    namedValues = NamedValues(
        *(("acknowledgedInfo", 34),
          ("aggressive", 4),
          ("authOnly", 3),
          ("base", 1),
          ("informational", 5),
          ("mainMode", 2),
          ("newGroupMode", 33),
          ("quickMode", 32),
          ("reserved", 0))
    )



class IkeEncryptionAlgorithm(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
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
        *(("blowfishCbc", 3),
          ("castCbc", 6),
          ("desCbc", 1),
          ("ideaCbc", 2),
          ("rc5R16B64Cbc", 4),
          ("reserved", 0),
          ("tripleDesCbc", 5))
    )



class IkeHashAlgorithm(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
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
        *(("md5", 1),
          ("reserved", 0),
          ("sha", 2),
          ("tiger", 3))
    )



class IkeAuthMethod(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("dssSignatures", 2),
          ("encryptionWithElGamal", 6),
          ("encryptionWithRsa", 4),
          ("preSharedKey", 1),
          ("reserved", 0),
          ("revisedEncryptionWithElGamal", 7),
          ("revisedEncryptionWithRsa", 5),
          ("rsaSignatures", 3))
    )



class IkeGroupDescription(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ec2nGalois2P155", 3),
          ("ec2nGalois2P185", 4),
          ("modp1024", 2),
          ("modp1536", 5),
          ("modp768", 1),
          ("reserved", 0))
    )



class IkeGroupType(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
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
        *(("ec2n", 3),
          ("ecp", 2),
          ("modp", 1),
          ("reserved", 0))
    )



class IkePrf(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class IkeNotifyMessageType(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
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
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              24576,
              24577,
              24578)
        )
    )
    namedValues = NamedValues(
        *(("addressNotification", 26),
          ("attributesNotSupported", 13),
          ("authenticationFailed", 24),
          ("badProposalSyntax", 15),
          ("certTypeUnsupported", 21),
          ("certificateUnavailable", 28),
          ("doiNotSupported", 2),
          ("initialContact", 24578),
          ("invalidCertAuthority", 22),
          ("invalidCertEncoding", 19),
          ("invalidCertificate", 20),
          ("invalidCookie", 4),
          ("invalidExchangeType", 7),
          ("invalidFlags", 8),
          ("invalidHashInformation", 23),
          ("invalidIdInformation", 18),
          ("invalidKeyInformation", 17),
          ("invalidMajorVersion", 5),
          ("invalidMessageId", 9),
          ("invalidMinorVersion", 6),
          ("invalidPayloadType", 1),
          ("invalidProtocolId", 10),
          ("invalidSignature", 25),
          ("invalidSpi", 11),
          ("invalidTransformId", 12),
          ("noProposalChosen", 14),
          ("notifySaLifetime", 27),
          ("payloadMalformed", 16),
          ("replayStatus", 24577),
          ("reserved", 0),
          ("responderLifetime", 24576),
          ("situationNotSupported", 3),
          ("unequalPayloadLengths", 30),
          ("unsupportedExchangeType", 29))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPSEC-ISAKMP-IKE-DOI-TC",
    **{"IpsecDoiSituation": IpsecDoiSituation,
       "IpsecDoiSecProtocolId": IpsecDoiSecProtocolId,
       "IpsecDoiTransformIdent": IpsecDoiTransformIdent,
       "IpsecDoiAhTransform": IpsecDoiAhTransform,
       "IpsecDoiEspTransform": IpsecDoiEspTransform,
       "IpsecDoiAuthAlgorithm": IpsecDoiAuthAlgorithm,
       "IpsecDoiIpcompTransform": IpsecDoiIpcompTransform,
       "IpsecDoiEncapsulationMode": IpsecDoiEncapsulationMode,
       "IpsecDoiIdentType": IpsecDoiIdentType,
       "IsakmpDOI": IsakmpDOI,
       "IsakmpCertificateEncoding": IsakmpCertificateEncoding,
       "IsakmpExchangeType": IsakmpExchangeType,
       "IsakmpNotifyMessageType": IsakmpNotifyMessageType,
       "IkeExchangeType": IkeExchangeType,
       "IkeEncryptionAlgorithm": IkeEncryptionAlgorithm,
       "IkeHashAlgorithm": IkeHashAlgorithm,
       "IkeAuthMethod": IkeAuthMethod,
       "IkeGroupDescription": IkeGroupDescription,
       "IkeGroupType": IkeGroupType,
       "IkePrf": IkePrf,
       "IkeNotifyMessageType": IkeNotifyMessageType,
       "ipsecIsakmpIkeDoiTC": ipsecIsakmpIkeDoiTC}
)
