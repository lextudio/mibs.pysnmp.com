# SNMP MIB module (IPSEC-FLOW-MIB-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IPSEC-FLOW-MIB-TC
# Produced by pysmi-1.5.4 at Mon Oct 14 22:11:08 2024
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
    "experimental",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ipsecFlowMibTC = ModuleIdentity(
    (1, 3, 6, 1, 3, 170)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ControlProtocol(Integer32, TextualConvention):
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
        *(("cpIkev1", 2),
          ("cpIkev2", 3),
          ("cpKink", 4),
          ("cpNone", 1),
          ("cpOther", 5),
          ("reserved", 0))
    )



class Phase1PeerIdentityType(Integer32, TextualConvention):
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
        *(("idDerAsn1Gn", 10),
          ("idDn", 3),
          ("idFqdn", 2),
          ("idIpv4Addr", 1),
          ("idIpv4AddrRange", 8),
          ("idIpv4AddrSubnet", 6),
          ("idIpv6Addr", 4),
          ("idIpv6AddrRange", 9),
          ("idIpv6AddrSubnet", 7),
          ("idKeyId", 11),
          ("idUserFqdn", 5),
          ("reserved", 0))
    )



class IkeNegoMode(Integer32, TextualConvention):
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
        *(("aggressive", 2),
          ("main", 1),
          ("reserved", 0))
    )



class IkeHashAlgo(Integer32, TextualConvention):
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
        *(("md5", 1),
          ("reserved", 0),
          ("sha", 2),
          ("sha256", 4),
          ("sha384", 5),
          ("sha512", 6),
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
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("dssSignature", 2),
          ("ecsdaSignature", 8),
          ("elGamalEncryption", 6),
          ("gssApiV1", 9),
          ("gssApiV2", 10),
          ("preSharedKey", 1),
          ("reserved", 0),
          ("revElGamalEncryption", 7),
          ("revRsaEncryption", 5),
          ("rsaEncryption", 4),
          ("rsaSignature", 3))
    )



class DiffHellmanGrp(Integer32, TextualConvention):
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
              8,
              10,
              12)
        )
    )
    namedValues = NamedValues(
        *(("ec2nGF163", 6),
          ("ec2nGF283", 8),
          ("ec2nGF409", 10),
          ("ec2nGF571", 12),
          ("ec2nGP155", 3),
          ("ec2nGP185", 4),
          ("modp1024", 2),
          ("modp1536", 5),
          ("modp768", 1),
          ("reserved", 0))
    )



class EncapMode(Integer32, TextualConvention):
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



class EncryptAlgo(Integer32, TextualConvention):
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("esp3des", 2),
          ("esp3idea", 7),
          ("espAes", 10),
          ("espBlowfish", 6),
          ("espCast", 5),
          ("espDes", 1),
          ("espIdea", 4),
          ("espNull", 9),
          ("espRc4", 8),
          ("espRc5", 3),
          ("reserved", 0))
    )



class Spi(Integer32, TextualConvention):
    status = "current"
    displayHint = "x"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 4294967295),
    )



class AuthAlgo(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
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
        *(("desMac", 4),
          ("hmacMd5", 2),
          ("hmacSha", 3),
          ("hmacSha256", 5),
          ("hmacSha384", 6),
          ("hmacSha512", 7),
          ("reserved", 0),
          ("ripemd", 8))
    )



class CompAlgo(Integer32, TextualConvention):
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
        *(("compDeflate", 2),
          ("compLzjh", 4),
          ("compLzs", 3),
          ("compOui", 1),
          ("reserved", 0))
    )



class EndPtType(Integer32, TextualConvention):
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



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPSEC-FLOW-MIB-TC",
    **{"ControlProtocol": ControlProtocol,
       "Phase1PeerIdentityType": Phase1PeerIdentityType,
       "IkeNegoMode": IkeNegoMode,
       "IkeHashAlgo": IkeHashAlgo,
       "IkeAuthMethod": IkeAuthMethod,
       "DiffHellmanGrp": DiffHellmanGrp,
       "EncapMode": EncapMode,
       "EncryptAlgo": EncryptAlgo,
       "Spi": Spi,
       "AuthAlgo": AuthAlgo,
       "CompAlgo": CompAlgo,
       "EndPtType": EndPtType,
       "ipsecFlowMibTC": ipsecFlowMibTC}
)
