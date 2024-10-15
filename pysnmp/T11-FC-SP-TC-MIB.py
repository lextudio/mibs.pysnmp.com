# SNMP MIB module (T11-FC-SP-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/T11-FC-SP-TC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:00:34 2024
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
    "iso",
    "mib-2")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

t11FcTcMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 175)
)
t11FcTcMIB.setRevisions(
        ("2008-08-20 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class T11FcSpPolicyHashFormat(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )



class T11FcSpPolicyHashValue(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class T11FcSpHashCalculationStatus(Integer32, TextualConvention):
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
        *(("calculate", 1),
          ("correct", 2),
          ("stale", 3))
    )



class T11FcSpAuthRejectReasonCode(Integer32, TextualConvention):
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
        *(("authELSNotSupported", 5),
          ("authFailure", 1),
          ("authILSNotSupported", 4),
          ("logicalBusy", 3),
          ("logicalError", 2),
          ("notLoggedIn", 6))
    )



class T11FcSpAuthRejReasonCodeExp(Integer32, TextualConvention):
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("authConcatNotSupported", 9),
          ("authELSNotSupported", 13),
          ("authILSNotSupported", 12),
          ("authMechanismNotUsable", 1),
          ("authTransactionAlreadyStarted", 4),
          ("authenticationFailed", 5),
          ("dhGroupNotUsable", 2),
          ("hashFunctionNotUsable", 3),
          ("incorrectAuthProtocolMessage", 7),
          ("incorrectPayload", 6),
          ("logicalBusy", 11),
          ("notLoggedIn", 14),
          ("restartAuthProtocol", 8),
          ("unsupportedProtocolVersion", 10))
    )



class T11FcSpHashFunctions(Bits, TextualConvention):
    status = "current"


class T11FcSpSignFunctions(Bits, TextualConvention):
    status = "current"


class T11FcSpDhGroups(Bits, TextualConvention):
    status = "current"


class T11FcSpPolicyObjectType(Integer32, TextualConvention):
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
        *(("attribute", 6),
          ("ipMgmtList", 5),
          ("nodeMemberList", 3),
          ("summary", 1),
          ("switchConnectivity", 4),
          ("switchMemberList", 2))
    )



class T11FcSpPolicyNameType(Integer32, TextualConvention):
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
        *(("alphaNumericName", 7),
          ("ipv4AddressRange", 9),
          ("ipv6AddressRange", 8),
          ("nodeName", 1),
          ("portName", 3),
          ("restrictedNodeName", 2),
          ("restrictedPortName", 4),
          ("restrictedWildcard", 6),
          ("wildcard", 5))
    )



class T11FcSpPolicyName(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )



class T11FcSpAlphaNumName(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )



class T11FcSpAlphaNumNameOrAbsent(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class T11FcSaDirection(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("egress", 2),
          ("ingress", 1))
    )



class T11FcSpiIndex(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class T11FcSpPrecedence(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class T11FcRoutingControl(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )



class T11FcSpType(OctetString, TextualConvention):
    status = "current"
    displayHint = "2x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )



class T11FcSpTransforms(Bits, TextualConvention):
    status = "current"


class T11FcSpSecurityProtocolId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ctAuth", 2),
          ("espHeader", 1))
    )



class T11FcSpLifetimeLeft(Unsigned32, TextualConvention):
    status = "current"


class T11FcSpLifetimeLeftUnits(Integer32, TextualConvention):
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
        *(("exaBytes", 7),
          ("gigaBytes", 4),
          ("kiloBytes", 2),
          ("megaBytes", 3),
          ("petaBytes", 6),
          ("seconds", 1),
          ("teraBytes", 5),
          ("yottaBytes", 9),
          ("zettaBytes", 8))
    )



# MIB Managed Objects in the order of their OIDs

_T11FcSpIdentities_ObjectIdentity = ObjectIdentity
t11FcSpIdentities = _T11FcSpIdentities_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 175, 1)
)
_T11FcSpAlgorithms_ObjectIdentity = ObjectIdentity
t11FcSpAlgorithms = _T11FcSpAlgorithms_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 175, 1, 1)
)
_T11FcSpEncryptAlgorithms_ObjectIdentity = ObjectIdentity
t11FcSpEncryptAlgorithms = _T11FcSpEncryptAlgorithms_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 175, 1, 1, 1)
)
_T11FcSpEncrNull_ObjectIdentity = ObjectIdentity
t11FcSpEncrNull = _T11FcSpEncrNull_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 175, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    t11FcSpEncrNull.setStatus("current")
_T11FcSpEncrAesCbc_ObjectIdentity = ObjectIdentity
t11FcSpEncrAesCbc = _T11FcSpEncrAesCbc_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 175, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    t11FcSpEncrAesCbc.setStatus("current")
_T11FcSpEncrAesCtr_ObjectIdentity = ObjectIdentity
t11FcSpEncrAesCtr = _T11FcSpEncrAesCtr_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 175, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    t11FcSpEncrAesCtr.setStatus("current")
_T11FcSpEncrAesGcm_ObjectIdentity = ObjectIdentity
t11FcSpEncrAesGcm = _T11FcSpEncrAesGcm_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 175, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    t11FcSpEncrAesGcm.setStatus("current")
_T11FcSpEncr3Des_ObjectIdentity = ObjectIdentity
t11FcSpEncr3Des = _T11FcSpEncr3Des_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 175, 1, 1, 1, 5)
)
if mibBuilder.loadTexts:
    t11FcSpEncr3Des.setStatus("current")
_T11FcSpEncrNullAuthAesGmac_ObjectIdentity = ObjectIdentity
t11FcSpEncrNullAuthAesGmac = _T11FcSpEncrNullAuthAesGmac_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 175, 1, 1, 1, 6)
)
if mibBuilder.loadTexts:
    t11FcSpEncrNullAuthAesGmac.setStatus("current")
_T11FcSpAuthAlgorithms_ObjectIdentity = ObjectIdentity
t11FcSpAuthAlgorithms = _T11FcSpAuthAlgorithms_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 175, 1, 1, 2)
)
_T11FcSpAuthNull_ObjectIdentity = ObjectIdentity
t11FcSpAuthNull = _T11FcSpAuthNull_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 175, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    t11FcSpAuthNull.setStatus("current")
_T11FcSpAuthHmacMd5L96_ObjectIdentity = ObjectIdentity
t11FcSpAuthHmacMd5L96 = _T11FcSpAuthHmacMd5L96_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 175, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    t11FcSpAuthHmacMd5L96.setStatus("current")
_T11FcSpAuthHmacSha1L96_ObjectIdentity = ObjectIdentity
t11FcSpAuthHmacSha1L96 = _T11FcSpAuthHmacSha1L96_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 175, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    t11FcSpAuthHmacSha1L96.setStatus("current")
_T11FcSpAuthHmacMd5L128_ObjectIdentity = ObjectIdentity
t11FcSpAuthHmacMd5L128 = _T11FcSpAuthHmacMd5L128_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 175, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    t11FcSpAuthHmacMd5L128.setStatus("current")
_T11FcSpAuthHmacSha1L160_ObjectIdentity = ObjectIdentity
t11FcSpAuthHmacSha1L160 = _T11FcSpAuthHmacSha1L160_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 175, 1, 1, 2, 5)
)
if mibBuilder.loadTexts:
    t11FcSpAuthHmacSha1L160.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "T11-FC-SP-TC-MIB",
    **{"T11FcSpPolicyHashFormat": T11FcSpPolicyHashFormat,
       "T11FcSpPolicyHashValue": T11FcSpPolicyHashValue,
       "T11FcSpHashCalculationStatus": T11FcSpHashCalculationStatus,
       "T11FcSpAuthRejectReasonCode": T11FcSpAuthRejectReasonCode,
       "T11FcSpAuthRejReasonCodeExp": T11FcSpAuthRejReasonCodeExp,
       "T11FcSpHashFunctions": T11FcSpHashFunctions,
       "T11FcSpSignFunctions": T11FcSpSignFunctions,
       "T11FcSpDhGroups": T11FcSpDhGroups,
       "T11FcSpPolicyObjectType": T11FcSpPolicyObjectType,
       "T11FcSpPolicyNameType": T11FcSpPolicyNameType,
       "T11FcSpPolicyName": T11FcSpPolicyName,
       "T11FcSpAlphaNumName": T11FcSpAlphaNumName,
       "T11FcSpAlphaNumNameOrAbsent": T11FcSpAlphaNumNameOrAbsent,
       "T11FcSaDirection": T11FcSaDirection,
       "T11FcSpiIndex": T11FcSpiIndex,
       "T11FcSpPrecedence": T11FcSpPrecedence,
       "T11FcRoutingControl": T11FcRoutingControl,
       "T11FcSpType": T11FcSpType,
       "T11FcSpTransforms": T11FcSpTransforms,
       "T11FcSpSecurityProtocolId": T11FcSpSecurityProtocolId,
       "T11FcSpLifetimeLeft": T11FcSpLifetimeLeft,
       "T11FcSpLifetimeLeftUnits": T11FcSpLifetimeLeftUnits,
       "t11FcTcMIB": t11FcTcMIB,
       "t11FcSpIdentities": t11FcSpIdentities,
       "t11FcSpAlgorithms": t11FcSpAlgorithms,
       "t11FcSpEncryptAlgorithms": t11FcSpEncryptAlgorithms,
       "t11FcSpEncrNull": t11FcSpEncrNull,
       "t11FcSpEncrAesCbc": t11FcSpEncrAesCbc,
       "t11FcSpEncrAesCtr": t11FcSpEncrAesCtr,
       "t11FcSpEncrAesGcm": t11FcSpEncrAesGcm,
       "t11FcSpEncr3Des": t11FcSpEncr3Des,
       "t11FcSpEncrNullAuthAesGmac": t11FcSpEncrNullAuthAesGmac,
       "t11FcSpAuthAlgorithms": t11FcSpAuthAlgorithms,
       "t11FcSpAuthNull": t11FcSpAuthNull,
       "t11FcSpAuthHmacMd5L96": t11FcSpAuthHmacMd5L96,
       "t11FcSpAuthHmacSha1L96": t11FcSpAuthHmacSha1L96,
       "t11FcSpAuthHmacMd5L128": t11FcSpAuthHmacMd5L128,
       "t11FcSpAuthHmacSha1L160": t11FcSpAuthHmacSha1L160}
)
