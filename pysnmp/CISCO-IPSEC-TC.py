# SNMP MIB module (CISCO-IPSEC-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IPSEC-TC
# Produced by pysmi-1.5.4 at Mon Oct 14 20:59:23 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ciscoIPsecTc = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 422)
)
ciscoIPsecTc.setRevisions(
        ("2004-07-22 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CCryptoMD5Hash(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )



class CIKEIsakmpDoi(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("isakmpDoiCps", 5),
          ("isakmpDoiFcCtAuth", 6),
          ("isakmpDoiFcsp", 4),
          ("isakmpDoiIPsec", 3),
          ("isakmpDoiOther", 2),
          ("isakmpDoiUnknown", 1))
    )



class CIKELifetime(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )



class CIKELifesize(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2560, 4294967295),
    )



class CIPsecEncryptionKeySize(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class CIPsecControlProtocol(Integer32, TextualConvention):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("cpAll", 2),
          ("cpIkev1", 5),
          ("cpIkev2", 6),
          ("cpKink", 7),
          ("cpManual", 4),
          ("cpOther", 3),
          ("cpPhoturis", 8),
          ("cpUnknown", 1))
    )



class CIPsecProtocol(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ipsecProtAh", 2),
          ("ipsecProtEsp", 3),
          ("ipsecProtIPcomp", 4),
          ("ipsecProtUnknown", 1))
    )



class CIPsecPhase1PeerIdentityType(Integer32, TextualConvention):
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
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("idDerAsn1Gn", 11),
          ("idDn", 4),
          ("idFqdn", 3),
          ("idIpv4Addr", 2),
          ("idIpv4AddrRange", 9),
          ("idIpv4AddrSubnet", 7),
          ("idIpv6Addr", 5),
          ("idIpv6AddrRange", 10),
          ("idIpv6AddrSubnet", 8),
          ("idKeyId", 12),
          ("idOther", 1),
          ("idUserFqdn", 6),
          ("idWwn", 13))
    )



class CIPsecIkeNegoMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aggressiveMode", 2),
          ("mainMode", 1))
    )



class CIPsecIkeHashAlgorithm(Integer32, TextualConvention):
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("aesMac", 9),
          ("md5", 3),
          ("none", 1),
          ("other", 2),
          ("sha", 4),
          ("sha256", 6),
          ("sha384", 7),
          ("sha512", 8),
          ("tiger", 5))
    )



class CIPsecIkeAuthMethod(Integer32, TextualConvention):
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
        *(("dssSignature", 6),
          ("ecsdaSignature", 9),
          ("elGamalEncryption", 7),
          ("gssApiV1", 10),
          ("gssApiV2", 11),
          ("other", 1),
          ("preSharedKey", 2),
          ("revElGamalEncryption", 8),
          ("revRsaEncryption", 5),
          ("rsaEncryption", 4),
          ("rsaSignature", 3))
    )



class CIPsecDiffHellmanGrp(Integer32, TextualConvention):
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
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("ec2nGF163", 8),
          ("ec2nGF283", 9),
          ("ec2nGF409", 10),
          ("ec2nGF571", 11),
          ("ec2nGP155", 5),
          ("ec2nGP185", 6),
          ("modp1024", 4),
          ("modp1536", 7),
          ("modp2048", 12),
          ("modp768", 3),
          ("notDH", 2),
          ("other", 1))
    )



class CIPsecEncapMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("encapTransport", 2),
          ("encapTunnel", 1))
    )



class CIPsecTransform(Integer32, TextualConvention):
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
              31,
              32,
              33,
              34,
              35,
              36)
        )
    )
    namedValues = NamedValues(
        *(("xformAHAESXCbcMac", 36),
          ("xformAHDesMac", 30),
          ("xformAHHmacSha256", 31),
          ("xformAHHmacSha384", 32),
          ("xformAHHmacSha512", 33),
          ("xformAHRipemd", 34),
          ("xformAhMD5", 4),
          ("xformAhRFC1829", 3),
          ("xformAhSHA1", 5),
          ("xformCompLZS", 14),
          ("xformEsp3DES", 8),
          ("xformEsp3idea", 23),
          ("xformEspAES128", 9),
          ("xformEspAES192", 10),
          ("xformEspAES256", 11),
          ("xformEspAESCtr128", 15),
          ("xformEspAESCtr192", 16),
          ("xformEspAESCtr256", 17),
          ("xformEspAESXCbcMac", 35),
          ("xformEspBlowfish", 22),
          ("xformEspCast", 20),
          ("xformEspDES", 7),
          ("xformEspDesMac", 25),
          ("xformEspHmacSha256", 26),
          ("xformEspHmacSha384", 27),
          ("xformEspHmacSha512", 28),
          ("xformEspIdea", 19),
          ("xformEspMD5", 12),
          ("xformEspNULL", 6),
          ("xformEspRc4", 24),
          ("xformEspRc5", 18),
          ("xformEspRipemd", 29),
          ("xformEspSHA1", 13),
          ("xformEspTwofish", 21),
          ("xformNONE", 1),
          ("xformOTHER", 2))
    )



class CIPsecSecuritySuite(Integer32, TextualConvention):
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
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("suiteConfAh", 8),
          ("suiteConfAhComp", 9),
          ("suiteConfComp", 5),
          ("suiteConfEsp", 2),
          ("suiteConfIntegEsp", 12),
          ("suiteConfIntegEspAh", 14),
          ("suiteConfIntegEspAhComp", 15),
          ("suiteConfIntegEspComp", 13),
          ("suiteIntegAh", 4),
          ("suiteIntegAhComp", 7),
          ("suiteIntegEsp", 3),
          ("suiteIntegEspAh", 10),
          ("suiteIntegEspAhComp", 11),
          ("suiteIntegEspComp", 6),
          ("suiteOther", 1))
    )



class CIPsecNATTraversalMode(Integer32, TextualConvention):
    status = "current"
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
        *(("natEncapIPsecOverTcp", 4),
          ("natEncapIPsecOverUdp", 3),
          ("natEncapNATT", 5),
          ("natEncapNone", 1),
          ("natEncapOther", 2))
    )



class CIPsecEncryptAlgorithm(Integer32, TextualConvention):
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
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("esp3des", 4),
          ("esp3idea", 10),
          ("espAes128", 13),
          ("espAes192", 14),
          ("espAes256", 15),
          ("espAesCtr128", 16),
          ("espAesCtr192", 17),
          ("espAesCtr256", 18),
          ("espBlowfish", 9),
          ("espCast", 7),
          ("espDes", 3),
          ("espIdea", 6),
          ("espNull", 12),
          ("espRc4", 11),
          ("espRc5", 5),
          ("espTwofish", 8),
          ("none", 1),
          ("other", 2))
    )



class CIPsecSpi(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "x"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 4294967295),
    )



class CIPsecAuthAlgorithm(Integer32, TextualConvention):
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("desMac", 5),
          ("hmacMd5", 3),
          ("hmacSha", 4),
          ("hmacSha256", 6),
          ("hmacSha384", 7),
          ("hmacSha512", 8),
          ("none", 1),
          ("other", 2),
          ("ripemd", 9))
    )



class CIPsecCompAlgorithm(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("compDeflate", 4),
          ("compLzjh", 6),
          ("compLzs", 5),
          ("compOui", 3),
          ("none", 1),
          ("other", 2))
    )



class CIPsecEndPtType(Integer32, TextualConvention):
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
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("idDerAsn1Dn", 10),
          ("idDerAsn1Gn", 11),
          ("idFqdn", 5),
          ("idIpv4Addr", 2),
          ("idIpv4AddrRange", 3),
          ("idIpv4AddrSubnet", 4),
          ("idIpv6Addr", 7),
          ("idIpv6AddrRange", 8),
          ("idIpv6AddrSubnet", 9),
          ("idKeyId", 12),
          ("idUserFqdn", 6),
          ("other", 1))
    )



class CIPsecPhase2SaDirection(Integer32, TextualConvention):
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
        *(("saDirectionIn", 2),
          ("saDirectionOut", 3),
          ("saDirectionUnknown", 1))
    )



class CIPsecPhase1TunnelIndex(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class CIPsecPhase1TunnelIndexOrZero(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class CIPsecPhase2TunnelIndex(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class CIPsecPmtu(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(68, 1500),
    )



class CIPsecLifetime(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(120, 86400),
    )



class CIPsecLifesize(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2560, 4294967295),
    )



class CIPsecTunnelIdleTime(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 86400),
    )



class CIPsecNumCryptoMaps(Gauge32, TextualConvention):
    status = "current"
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class CIPsecTunnelStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 4),
          ("awaitCommit", 3),
          ("awaitXauth", 2),
          ("destroy", 5),
          ("initializePhase1", 1),
          ("rekey", 6))
    )



class CIPsecCryptomapType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("cryptomapTypeCET", 4),
          ("cryptomapTypeDYNAMIC", 5),
          ("cryptomapTypeDYNAMICDISCOVERY", 6),
          ("cryptomapTypeISAKMP", 3),
          ("cryptomapTypeMANUAL", 2),
          ("cryptomapTypeNONE", 1))
    )



class CIPsecCryptomapSetBindStatus(Integer32, TextualConvention):
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
        *(("attached", 2),
          ("detached", 3),
          ("unknown", 1))
    )



class CIPsecIkePRFAlgorithm(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("other", 2),
          ("prfHmacMd5", 3),
          ("prfHmacSha1", 4))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IPSEC-TC",
    **{"CCryptoMD5Hash": CCryptoMD5Hash,
       "CIKEIsakmpDoi": CIKEIsakmpDoi,
       "CIKELifetime": CIKELifetime,
       "CIKELifesize": CIKELifesize,
       "CIPsecEncryptionKeySize": CIPsecEncryptionKeySize,
       "CIPsecControlProtocol": CIPsecControlProtocol,
       "CIPsecProtocol": CIPsecProtocol,
       "CIPsecPhase1PeerIdentityType": CIPsecPhase1PeerIdentityType,
       "CIPsecIkeNegoMode": CIPsecIkeNegoMode,
       "CIPsecIkeHashAlgorithm": CIPsecIkeHashAlgorithm,
       "CIPsecIkeAuthMethod": CIPsecIkeAuthMethod,
       "CIPsecDiffHellmanGrp": CIPsecDiffHellmanGrp,
       "CIPsecEncapMode": CIPsecEncapMode,
       "CIPsecTransform": CIPsecTransform,
       "CIPsecSecuritySuite": CIPsecSecuritySuite,
       "CIPsecNATTraversalMode": CIPsecNATTraversalMode,
       "CIPsecEncryptAlgorithm": CIPsecEncryptAlgorithm,
       "CIPsecSpi": CIPsecSpi,
       "CIPsecAuthAlgorithm": CIPsecAuthAlgorithm,
       "CIPsecCompAlgorithm": CIPsecCompAlgorithm,
       "CIPsecEndPtType": CIPsecEndPtType,
       "CIPsecPhase2SaDirection": CIPsecPhase2SaDirection,
       "CIPsecPhase1TunnelIndex": CIPsecPhase1TunnelIndex,
       "CIPsecPhase1TunnelIndexOrZero": CIPsecPhase1TunnelIndexOrZero,
       "CIPsecPhase2TunnelIndex": CIPsecPhase2TunnelIndex,
       "CIPsecPmtu": CIPsecPmtu,
       "CIPsecLifetime": CIPsecLifetime,
       "CIPsecLifesize": CIPsecLifesize,
       "CIPsecTunnelIdleTime": CIPsecTunnelIdleTime,
       "CIPsecNumCryptoMaps": CIPsecNumCryptoMaps,
       "CIPsecTunnelStatus": CIPsecTunnelStatus,
       "CIPsecCryptomapType": CIPsecCryptomapType,
       "CIPsecCryptomapSetBindStatus": CIPsecCryptomapSetBindStatus,
       "CIPsecIkePRFAlgorithm": CIPsecIkePRFAlgorithm,
       "ciscoIPsecTc": ciscoIPsecTc}
)
