# SNMP MIB module (GRF-ATMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GRF-ATMP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:48:52 2024
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

(grAtmp,) = mibBuilder.importSymbols(
    "NETSTAR-MIB",
    "grAtmp")

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


# Types definitions



class AtmpResultCode(Integer32):
    """Custom type AtmpResultCode based on Integer32"""
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
        *(("auth-failed", 2),
          ("general-error", 9),
          ("invalid-tunnel-id", 6),
          ("net-unreachable", 8),
          ("no-error", 1),
          ("not-enabled", 3),
          ("parameter-error", 5),
          ("timeout", 7),
          ("too-many", 4))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AtmpMIBVersion_ObjectIdentity = ObjectIdentity
atmpMIBVersion = _AtmpMIBVersion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 1)
)


class _AtmpMIBVersionMajor_Type(Integer32):
    """Custom type atmpMIBVersionMajor based on Integer32"""
    defaultValue = 1


_AtmpMIBVersionMajor_Object = MibScalar
atmpMIBVersionMajor = _AtmpMIBVersionMajor_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 1, 1),
    _AtmpMIBVersionMajor_Type()
)
atmpMIBVersionMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpMIBVersionMajor.setStatus("mandatory")


class _AtmpMIBVersionMinor_Type(Integer32):
    """Custom type atmpMIBVersionMinor based on Integer32"""
    defaultValue = 0


_AtmpMIBVersionMinor_Object = MibScalar
atmpMIBVersionMinor = _AtmpMIBVersionMinor_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 1, 2),
    _AtmpMIBVersionMinor_Type()
)
atmpMIBVersionMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpMIBVersionMinor.setStatus("mandatory")
_AtmpGeneralConfig_ObjectIdentity = ObjectIdentity
atmpGeneralConfig = _AtmpGeneralConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 2)
)
_AtmpUDPPort_Type = Integer32
_AtmpUDPPort_Object = MibScalar
atmpUDPPort = _AtmpUDPPort_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 2, 1),
    _AtmpUDPPort_Type()
)
atmpUDPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpUDPPort.setStatus("mandatory")


class _AtmpEnableAtmpTraps_Type(Integer32):
    """Custom type atmpEnableAtmpTraps based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_AtmpEnableAtmpTraps_Type.__name__ = "Integer32"
_AtmpEnableAtmpTraps_Object = MibScalar
atmpEnableAtmpTraps = _AtmpEnableAtmpTraps_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 2, 2),
    _AtmpEnableAtmpTraps_Type()
)
atmpEnableAtmpTraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpEnableAtmpTraps.setStatus("mandatory")
_AtmpNumberFAs_Type = Counter32
_AtmpNumberFAs_Object = MibScalar
atmpNumberFAs = _AtmpNumberFAs_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 2, 3),
    _AtmpNumberFAs_Type()
)
atmpNumberFAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpNumberFAs.setStatus("mandatory")
_AtmpNumberHNs_Type = Counter32
_AtmpNumberHNs_Object = MibScalar
atmpNumberHNs = _AtmpNumberHNs_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 2, 4),
    _AtmpNumberHNs_Type()
)
atmpNumberHNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpNumberHNs.setStatus("mandatory")
_AtmpMaxNumberHNs_Type = Integer32
_AtmpMaxNumberHNs_Object = MibScalar
atmpMaxNumberHNs = _AtmpMaxNumberHNs_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 2, 5),
    _AtmpMaxNumberHNs_Type()
)
atmpMaxNumberHNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpMaxNumberHNs.setStatus("mandatory")
_AtmpDFAConfig_ObjectIdentity = ObjectIdentity
atmpDFAConfig = _AtmpDFAConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 3)
)


class _AtmpDFAConfigured_Type(Integer32):
    """Custom type atmpDFAConfigured based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AtmpDFAConfigured_Type.__name__ = "Integer32"
_AtmpDFAConfigured_Object = MibScalar
atmpDFAConfigured = _AtmpDFAConfigured_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 3, 1),
    _AtmpDFAConfigured_Type()
)
atmpDFAConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpDFAConfigured.setStatus("mandatory")
_AtmpDFAWildcardIpAddress_Type = DisplayString
_AtmpDFAWildcardIpAddress_Object = MibScalar
atmpDFAWildcardIpAddress = _AtmpDFAWildcardIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 3, 2),
    _AtmpDFAWildcardIpAddress_Type()
)
atmpDFAWildcardIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpDFAWildcardIpAddress.setStatus("mandatory")


class _AtmpDFAPassword_Type(DisplayString):
    """Custom type atmpDFAPassword based on DisplayString"""
    defaultHexValue = ""


_AtmpDFAPassword_Object = MibScalar
atmpDFAPassword = _AtmpDFAPassword_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 3, 3),
    _AtmpDFAPassword_Type()
)
atmpDFAPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpDFAPassword.setStatus("mandatory")
_AtmpGeneralStats_ObjectIdentity = ObjectIdentity
atmpGeneralStats = _AtmpGeneralStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 4)
)
_AtmpNumberTunnelsUp_Type = Integer32
_AtmpNumberTunnelsUp_Object = MibScalar
atmpNumberTunnelsUp = _AtmpNumberTunnelsUp_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 4, 1),
    _AtmpNumberTunnelsUp_Type()
)
atmpNumberTunnelsUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpNumberTunnelsUp.setStatus("mandatory")
_AtmpNumberTunnelsRegistering_Type = Integer32
_AtmpNumberTunnelsRegistering_Object = MibScalar
atmpNumberTunnelsRegistering = _AtmpNumberTunnelsRegistering_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 4, 2),
    _AtmpNumberTunnelsRegistering_Type()
)
atmpNumberTunnelsRegistering.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpNumberTunnelsRegistering.setStatus("mandatory")
_AtmpNumberFAFailingMatch_Type = Counter32
_AtmpNumberFAFailingMatch_Object = MibScalar
atmpNumberFAFailingMatch = _AtmpNumberFAFailingMatch_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 4, 3),
    _AtmpNumberFAFailingMatch_Type()
)
atmpNumberFAFailingMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpNumberFAFailingMatch.setStatus("mandatory")
_AtmpNumberFAPasswordRejects_Type = Counter32
_AtmpNumberFAPasswordRejects_Object = MibScalar
atmpNumberFAPasswordRejects = _AtmpNumberFAPasswordRejects_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 4, 4),
    _AtmpNumberFAPasswordRejects_Type()
)
atmpNumberFAPasswordRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpNumberFAPasswordRejects.setStatus("mandatory")
_AtmpNumberDFAMatch_Type = Counter32
_AtmpNumberDFAMatch_Object = MibScalar
atmpNumberDFAMatch = _AtmpNumberDFAMatch_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 4, 5),
    _AtmpNumberDFAMatch_Type()
)
atmpNumberDFAMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpNumberDFAMatch.setStatus("mandatory")
_AtmpProtocolStats_ObjectIdentity = ObjectIdentity
atmpProtocolStats = _AtmpProtocolStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 5)
)
_AtmpRxRegistrationRequestPkts_Type = Counter32
_AtmpRxRegistrationRequestPkts_Object = MibScalar
atmpRxRegistrationRequestPkts = _AtmpRxRegistrationRequestPkts_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 5, 1),
    _AtmpRxRegistrationRequestPkts_Type()
)
atmpRxRegistrationRequestPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpRxRegistrationRequestPkts.setStatus("mandatory")
_AtmpTxChallengeRequestPkts_Type = Counter32
_AtmpTxChallengeRequestPkts_Object = MibScalar
atmpTxChallengeRequestPkts = _AtmpTxChallengeRequestPkts_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 5, 2),
    _AtmpTxChallengeRequestPkts_Type()
)
atmpTxChallengeRequestPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpTxChallengeRequestPkts.setStatus("mandatory")
_AtmpRxChallengeReplyPkts_Type = Counter32
_AtmpRxChallengeReplyPkts_Object = MibScalar
atmpRxChallengeReplyPkts = _AtmpRxChallengeReplyPkts_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 5, 3),
    _AtmpRxChallengeReplyPkts_Type()
)
atmpRxChallengeReplyPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpRxChallengeReplyPkts.setStatus("mandatory")
_AtmpTxRegistrationReplyPkts_Type = Counter32
_AtmpTxRegistrationReplyPkts_Object = MibScalar
atmpTxRegistrationReplyPkts = _AtmpTxRegistrationReplyPkts_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 5, 4),
    _AtmpTxRegistrationReplyPkts_Type()
)
atmpTxRegistrationReplyPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpTxRegistrationReplyPkts.setStatus("mandatory")
_AtmpRxDeRegistrationRequestPkts_Type = Counter32
_AtmpRxDeRegistrationRequestPkts_Object = MibScalar
atmpRxDeRegistrationRequestPkts = _AtmpRxDeRegistrationRequestPkts_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 5, 5),
    _AtmpRxDeRegistrationRequestPkts_Type()
)
atmpRxDeRegistrationRequestPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpRxDeRegistrationRequestPkts.setStatus("mandatory")
_AtmpTxDeRegistrationReplyPkts_Type = Counter32
_AtmpTxDeRegistrationReplyPkts_Object = MibScalar
atmpTxDeRegistrationReplyPkts = _AtmpTxDeRegistrationReplyPkts_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 5, 6),
    _AtmpTxDeRegistrationReplyPkts_Type()
)
atmpTxDeRegistrationReplyPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpTxDeRegistrationReplyPkts.setStatus("mandatory")
_AtmpReceiveProtocolErrorStats_ObjectIdentity = ObjectIdentity
atmpReceiveProtocolErrorStats = _AtmpReceiveProtocolErrorStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 5, 7)
)
_AtmpRxErrorNotificationPkts_Type = Counter32
_AtmpRxErrorNotificationPkts_Object = MibScalar
atmpRxErrorNotificationPkts = _AtmpRxErrorNotificationPkts_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 5, 7, 1),
    _AtmpRxErrorNotificationPkts_Type()
)
atmpRxErrorNotificationPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpRxErrorNotificationPkts.setStatus("mandatory")
_AtmpRxNoErrorPkts_Type = Counter32
_AtmpRxNoErrorPkts_Object = MibScalar
atmpRxNoErrorPkts = _AtmpRxNoErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 5, 7, 2),
    _AtmpRxNoErrorPkts_Type()
)
atmpRxNoErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpRxNoErrorPkts.setStatus("mandatory")
_AtmpRxAuthFailedPkts_Type = Counter32
_AtmpRxAuthFailedPkts_Object = MibScalar
atmpRxAuthFailedPkts = _AtmpRxAuthFailedPkts_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 5, 7, 3),
    _AtmpRxAuthFailedPkts_Type()
)
atmpRxAuthFailedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpRxAuthFailedPkts.setStatus("mandatory")
_AtmpRxNotEnabledPkts_Type = Counter32
_AtmpRxNotEnabledPkts_Object = MibScalar
atmpRxNotEnabledPkts = _AtmpRxNotEnabledPkts_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 5, 7, 4),
    _AtmpRxNotEnabledPkts_Type()
)
atmpRxNotEnabledPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpRxNotEnabledPkts.setStatus("mandatory")
_AtmpRxTooManyPkts_Type = Counter32
_AtmpRxTooManyPkts_Object = MibScalar
atmpRxTooManyPkts = _AtmpRxTooManyPkts_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 5, 7, 5),
    _AtmpRxTooManyPkts_Type()
)
atmpRxTooManyPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpRxTooManyPkts.setStatus("mandatory")
_AtmpRxParameterErrorPkts_Type = Counter32
_AtmpRxParameterErrorPkts_Object = MibScalar
atmpRxParameterErrorPkts = _AtmpRxParameterErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 5, 7, 6),
    _AtmpRxParameterErrorPkts_Type()
)
atmpRxParameterErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpRxParameterErrorPkts.setStatus("mandatory")
_AtmpRxInvalidTunnelIdPkts_Type = Counter32
_AtmpRxInvalidTunnelIdPkts_Object = MibScalar
atmpRxInvalidTunnelIdPkts = _AtmpRxInvalidTunnelIdPkts_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 5, 7, 7),
    _AtmpRxInvalidTunnelIdPkts_Type()
)
atmpRxInvalidTunnelIdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpRxInvalidTunnelIdPkts.setStatus("mandatory")
_AtmpRxTimeoutPkts_Type = Counter32
_AtmpRxTimeoutPkts_Object = MibScalar
atmpRxTimeoutPkts = _AtmpRxTimeoutPkts_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 5, 7, 8),
    _AtmpRxTimeoutPkts_Type()
)
atmpRxTimeoutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpRxTimeoutPkts.setStatus("mandatory")
_AtmpRxNetUnreachablePkts_Type = Counter32
_AtmpRxNetUnreachablePkts_Object = MibScalar
atmpRxNetUnreachablePkts = _AtmpRxNetUnreachablePkts_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 5, 7, 9),
    _AtmpRxNetUnreachablePkts_Type()
)
atmpRxNetUnreachablePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpRxNetUnreachablePkts.setStatus("mandatory")
_AtmpRxGeneralErrorPkts_Type = Counter32
_AtmpRxGeneralErrorPkts_Object = MibScalar
atmpRxGeneralErrorPkts = _AtmpRxGeneralErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 5, 7, 10),
    _AtmpRxGeneralErrorPkts_Type()
)
atmpRxGeneralErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpRxGeneralErrorPkts.setStatus("mandatory")
_AtmpRxChallengeRequestPkts_Type = Counter32
_AtmpRxChallengeRequestPkts_Object = MibScalar
atmpRxChallengeRequestPkts = _AtmpRxChallengeRequestPkts_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 5, 7, 11),
    _AtmpRxChallengeRequestPkts_Type()
)
atmpRxChallengeRequestPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpRxChallengeRequestPkts.setStatus("mandatory")
_AtmpRxRegistrationReplyPkts_Type = Counter32
_AtmpRxRegistrationReplyPkts_Object = MibScalar
atmpRxRegistrationReplyPkts = _AtmpRxRegistrationReplyPkts_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 5, 7, 12),
    _AtmpRxRegistrationReplyPkts_Type()
)
atmpRxRegistrationReplyPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpRxRegistrationReplyPkts.setStatus("mandatory")
_AtmpRxDeRegistrationReplyPkts_Type = Counter32
_AtmpRxDeRegistrationReplyPkts_Object = MibScalar
atmpRxDeRegistrationReplyPkts = _AtmpRxDeRegistrationReplyPkts_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 5, 7, 13),
    _AtmpRxDeRegistrationReplyPkts_Type()
)
atmpRxDeRegistrationReplyPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpRxDeRegistrationReplyPkts.setStatus("mandatory")
_AtmpRxUndersizeLengthPkts_Type = Counter32
_AtmpRxUndersizeLengthPkts_Object = MibScalar
atmpRxUndersizeLengthPkts = _AtmpRxUndersizeLengthPkts_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 5, 7, 14),
    _AtmpRxUndersizeLengthPkts_Type()
)
atmpRxUndersizeLengthPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpRxUndersizeLengthPkts.setStatus("mandatory")
_AtmpRxBadVersionPkts_Type = Counter32
_AtmpRxBadVersionPkts_Object = MibScalar
atmpRxBadVersionPkts = _AtmpRxBadVersionPkts_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 5, 7, 15),
    _AtmpRxBadVersionPkts_Type()
)
atmpRxBadVersionPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpRxBadVersionPkts.setStatus("mandatory")
_AtmpRxBufferAllocFailPkts_Type = Counter32
_AtmpRxBufferAllocFailPkts_Object = MibScalar
atmpRxBufferAllocFailPkts = _AtmpRxBufferAllocFailPkts_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 5, 7, 16),
    _AtmpRxBufferAllocFailPkts_Type()
)
atmpRxBufferAllocFailPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpRxBufferAllocFailPkts.setStatus("mandatory")
_AtmpRxBadAtmpCodePkts_Type = Counter32
_AtmpRxBadAtmpCodePkts_Object = MibScalar
atmpRxBadAtmpCodePkts = _AtmpRxBadAtmpCodePkts_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 5, 7, 17),
    _AtmpRxBadAtmpCodePkts_Type()
)
atmpRxBadAtmpCodePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpRxBadAtmpCodePkts.setStatus("mandatory")
_AtmpRxNetworkErrors_Type = Counter32
_AtmpRxNetworkErrors_Object = MibScalar
atmpRxNetworkErrors = _AtmpRxNetworkErrors_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 5, 7, 18),
    _AtmpRxNetworkErrors_Type()
)
atmpRxNetworkErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpRxNetworkErrors.setStatus("mandatory")
_AtmpTransmitProtocolErrorStats_ObjectIdentity = ObjectIdentity
atmpTransmitProtocolErrorStats = _AtmpTransmitProtocolErrorStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 5, 8)
)
_AtmpTxErrorNotificationPkts_Type = Counter32
_AtmpTxErrorNotificationPkts_Object = MibScalar
atmpTxErrorNotificationPkts = _AtmpTxErrorNotificationPkts_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 5, 8, 1),
    _AtmpTxErrorNotificationPkts_Type()
)
atmpTxErrorNotificationPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpTxErrorNotificationPkts.setStatus("mandatory")
_AtmpTxNoErrorPkts_Type = Counter32
_AtmpTxNoErrorPkts_Object = MibScalar
atmpTxNoErrorPkts = _AtmpTxNoErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 5, 8, 2),
    _AtmpTxNoErrorPkts_Type()
)
atmpTxNoErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpTxNoErrorPkts.setStatus("mandatory")
_AtmpTxAuthFailedPkts_Type = Counter32
_AtmpTxAuthFailedPkts_Object = MibScalar
atmpTxAuthFailedPkts = _AtmpTxAuthFailedPkts_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 5, 8, 3),
    _AtmpTxAuthFailedPkts_Type()
)
atmpTxAuthFailedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpTxAuthFailedPkts.setStatus("mandatory")
_AtmpTxNotEnabledPkts_Type = Counter32
_AtmpTxNotEnabledPkts_Object = MibScalar
atmpTxNotEnabledPkts = _AtmpTxNotEnabledPkts_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 5, 8, 4),
    _AtmpTxNotEnabledPkts_Type()
)
atmpTxNotEnabledPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpTxNotEnabledPkts.setStatus("mandatory")
_AtmpTxTooManyPkts_Type = Counter32
_AtmpTxTooManyPkts_Object = MibScalar
atmpTxTooManyPkts = _AtmpTxTooManyPkts_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 5, 8, 5),
    _AtmpTxTooManyPkts_Type()
)
atmpTxTooManyPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpTxTooManyPkts.setStatus("mandatory")
_AtmpTxParameterErrorPkts_Type = Counter32
_AtmpTxParameterErrorPkts_Object = MibScalar
atmpTxParameterErrorPkts = _AtmpTxParameterErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 5, 8, 6),
    _AtmpTxParameterErrorPkts_Type()
)
atmpTxParameterErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpTxParameterErrorPkts.setStatus("mandatory")
_AtmpTxInvalidTunnelIdPkts_Type = Counter32
_AtmpTxInvalidTunnelIdPkts_Object = MibScalar
atmpTxInvalidTunnelIdPkts = _AtmpTxInvalidTunnelIdPkts_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 5, 8, 7),
    _AtmpTxInvalidTunnelIdPkts_Type()
)
atmpTxInvalidTunnelIdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpTxInvalidTunnelIdPkts.setStatus("mandatory")
_AtmpTxTimeoutPkts_Type = Counter32
_AtmpTxTimeoutPkts_Object = MibScalar
atmpTxTimeoutPkts = _AtmpTxTimeoutPkts_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 5, 8, 8),
    _AtmpTxTimeoutPkts_Type()
)
atmpTxTimeoutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpTxTimeoutPkts.setStatus("mandatory")
_AtmpTxNetUnreachablePkts_Type = Counter32
_AtmpTxNetUnreachablePkts_Object = MibScalar
atmpTxNetUnreachablePkts = _AtmpTxNetUnreachablePkts_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 5, 8, 9),
    _AtmpTxNetUnreachablePkts_Type()
)
atmpTxNetUnreachablePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpTxNetUnreachablePkts.setStatus("mandatory")
_AtmpTxGeneralErrorPkts_Type = Counter32
_AtmpTxGeneralErrorPkts_Object = MibScalar
atmpTxGeneralErrorPkts = _AtmpTxGeneralErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 5, 8, 10),
    _AtmpTxGeneralErrorPkts_Type()
)
atmpTxGeneralErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpTxGeneralErrorPkts.setStatus("mandatory")
_AtmpTxNetworkErrors_Type = Counter32
_AtmpTxNetworkErrors_Object = MibScalar
atmpTxNetworkErrors = _AtmpTxNetworkErrors_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 5, 8, 11),
    _AtmpTxNetworkErrors_Type()
)
atmpTxNetworkErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpTxNetworkErrors.setStatus("mandatory")
_AtmpTables_ObjectIdentity = ObjectIdentity
atmpTables = _AtmpTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6)
)
_AtmpFATable_Object = MibTable
atmpFATable = _AtmpFATable_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 1)
)
if mibBuilder.loadTexts:
    atmpFATable.setStatus("mandatory")
_AtmpFAEntry_Object = MibTableRow
atmpFAEntry = _AtmpFAEntry_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 1, 1)
)
atmpFAEntry.setIndexNames(
    (0, "GRF-ATMP-MIB", "atmpFAIpAddress"),
)
if mibBuilder.loadTexts:
    atmpFAEntry.setStatus("mandatory")
_AtmpFAIpAddress_Type = IpAddress
_AtmpFAIpAddress_Object = MibTableColumn
atmpFAIpAddress = _AtmpFAIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 1, 1, 1),
    _AtmpFAIpAddress_Type()
)
atmpFAIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpFAIpAddress.setStatus("mandatory")


class _AtmpFAPassword_Type(DisplayString):
    """Custom type atmpFAPassword based on DisplayString"""
    defaultHexValue = ""


_AtmpFAPassword_Object = MibTableColumn
atmpFAPassword = _AtmpFAPassword_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 1, 1, 2),
    _AtmpFAPassword_Type()
)
atmpFAPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpFAPassword.setStatus("mandatory")
_AtmpFANumberTunnels_Type = Integer32
_AtmpFANumberTunnels_Object = MibTableColumn
atmpFANumberTunnels = _AtmpFANumberTunnels_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 1, 1, 3),
    _AtmpFANumberTunnels_Type()
)
atmpFANumberTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpFANumberTunnels.setStatus("mandatory")
_AtmpHNTable_Object = MibTable
atmpHNTable = _AtmpHNTable_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 2)
)
if mibBuilder.loadTexts:
    atmpHNTable.setStatus("mandatory")
_AtmpHNEntry_Object = MibTableRow
atmpHNEntry = _AtmpHNEntry_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 2, 1)
)
atmpHNEntry.setIndexNames(
    (0, "GRF-ATMP-MIB", "atmpHAIpAddress"),
)
if mibBuilder.loadTexts:
    atmpHNEntry.setStatus("mandatory")
_AtmpHAIpAddress_Type = IpAddress
_AtmpHAIpAddress_Object = MibTableColumn
atmpHAIpAddress = _AtmpHAIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 2, 1, 1),
    _AtmpHAIpAddress_Type()
)
atmpHAIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpHAIpAddress.setStatus("mandatory")
_AtmpHNName_Type = DisplayString
_AtmpHNName_Object = MibTableColumn
atmpHNName = _AtmpHNName_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 2, 1, 2),
    _AtmpHNName_Type()
)
atmpHNName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpHNName.setStatus("mandatory")


class _AtmpHNMTULimit_Type(Integer32):
    """Custom type atmpHNMTULimit based on Integer32"""
    defaultValue = 0


_AtmpHNMTULimit_Object = MibTableColumn
atmpHNMTULimit = _AtmpHNMTULimit_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 2, 1, 3),
    _AtmpHNMTULimit_Type()
)
atmpHNMTULimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpHNMTULimit.setStatus("mandatory")


class _AtmpHNForceFragmentation_Type(Integer32):
    """Custom type atmpHNForceFragmentation based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AtmpHNForceFragmentation_Type.__name__ = "Integer32"
_AtmpHNForceFragmentation_Object = MibTableColumn
atmpHNForceFragmentation = _AtmpHNForceFragmentation_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 2, 1, 4),
    _AtmpHNForceFragmentation_Type()
)
atmpHNForceFragmentation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpHNForceFragmentation.setStatus("mandatory")


class _AtmpHNBadSourceNotification_Type(Integer32):
    """Custom type atmpHNBadSourceNotification based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 1))
    )


_AtmpHNBadSourceNotification_Type.__name__ = "Integer32"
_AtmpHNBadSourceNotification_Object = MibTableColumn
atmpHNBadSourceNotification = _AtmpHNBadSourceNotification_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 2, 1, 5),
    _AtmpHNBadSourceNotification_Type()
)
atmpHNBadSourceNotification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpHNBadSourceNotification.setStatus("mandatory")


class _AtmpHNMaxTunnels_Type(Integer32):
    """Custom type atmpHNMaxTunnels based on Integer32"""
    defaultValue = 0


_AtmpHNMaxTunnels_Object = MibTableColumn
atmpHNMaxTunnels = _AtmpHNMaxTunnels_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 2, 1, 6),
    _AtmpHNMaxTunnels_Type()
)
atmpHNMaxTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpHNMaxTunnels.setStatus("mandatory")


class _AtmpHNInactivityTimeout_Type(Integer32):
    """Custom type atmpHNInactivityTimeout based on Integer32"""
    defaultValue = 0


_AtmpHNInactivityTimeout_Object = MibTableColumn
atmpHNInactivityTimeout = _AtmpHNInactivityTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 2, 1, 7),
    _AtmpHNInactivityTimeout_Type()
)
atmpHNInactivityTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpHNInactivityTimeout.setStatus("mandatory")
_AtmpHNNumberTunnels_Type = Integer32
_AtmpHNNumberTunnels_Object = MibTableColumn
atmpHNNumberTunnels = _AtmpHNNumberTunnels_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 2, 1, 8),
    _AtmpHNNumberTunnels_Type()
)
atmpHNNumberTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpHNNumberTunnels.setStatus("mandatory")
_AtmpHNInactiveTunnelsRemoved_Type = Counter32
_AtmpHNInactiveTunnelsRemoved_Object = MibTableColumn
atmpHNInactiveTunnelsRemoved = _AtmpHNInactiveTunnelsRemoved_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 2, 1, 9),
    _AtmpHNInactiveTunnelsRemoved_Type()
)
atmpHNInactiveTunnelsRemoved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpHNInactiveTunnelsRemoved.setStatus("mandatory")
_AtmpHNTunnelsMaxRejected_Type = Counter32
_AtmpHNTunnelsMaxRejected_Object = MibTableColumn
atmpHNTunnelsMaxRejected = _AtmpHNTunnelsMaxRejected_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 2, 1, 10),
    _AtmpHNTunnelsMaxRejected_Type()
)
atmpHNTunnelsMaxRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpHNTunnelsMaxRejected.setStatus("mandatory")
_AtmpHNTunnelHighWater_Type = Integer32
_AtmpHNTunnelHighWater_Object = MibTableColumn
atmpHNTunnelHighWater = _AtmpHNTunnelHighWater_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 2, 1, 11),
    _AtmpHNTunnelHighWater_Type()
)
atmpHNTunnelHighWater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpHNTunnelHighWater.setStatus("mandatory")
_AtmpHNSwitchToStandbyInterface_Type = Counter32
_AtmpHNSwitchToStandbyInterface_Object = MibTableColumn
atmpHNSwitchToStandbyInterface = _AtmpHNSwitchToStandbyInterface_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 2, 1, 12),
    _AtmpHNSwitchToStandbyInterface_Type()
)
atmpHNSwitchToStandbyInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpHNSwitchToStandbyInterface.setStatus("mandatory")
_AtmpHNSwitchToPrimaryInterface_Type = Counter32
_AtmpHNSwitchToPrimaryInterface_Object = MibTableColumn
atmpHNSwitchToPrimaryInterface = _AtmpHNSwitchToPrimaryInterface_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 2, 1, 13),
    _AtmpHNSwitchToPrimaryInterface_Type()
)
atmpHNSwitchToPrimaryInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpHNSwitchToPrimaryInterface.setStatus("mandatory")
_AtmpHNRxErrorCount_Type = Counter32
_AtmpHNRxErrorCount_Object = MibTableColumn
atmpHNRxErrorCount = _AtmpHNRxErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 2, 1, 14),
    _AtmpHNRxErrorCount_Type()
)
atmpHNRxErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpHNRxErrorCount.setStatus("mandatory")
_AtmpHNTxErrorCount_Type = Counter32
_AtmpHNTxErrorCount_Object = MibTableColumn
atmpHNTxErrorCount = _AtmpHNTxErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 2, 1, 15),
    _AtmpHNTxErrorCount_Type()
)
atmpHNTxErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpHNTxErrorCount.setStatus("mandatory")
_AtmpHNInterfaceCount_Type = Integer32
_AtmpHNInterfaceCount_Object = MibTableColumn
atmpHNInterfaceCount = _AtmpHNInterfaceCount_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 2, 1, 16),
    _AtmpHNInterfaceCount_Type()
)
atmpHNInterfaceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpHNInterfaceCount.setStatus("mandatory")
_AtmpHNTxErrorTable_Object = MibTable
atmpHNTxErrorTable = _AtmpHNTxErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 3)
)
if mibBuilder.loadTexts:
    atmpHNTxErrorTable.setStatus("mandatory")
_AtmpHNTxErrorEntry_Object = MibTableRow
atmpHNTxErrorEntry = _AtmpHNTxErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 3, 1)
)
atmpHNTxErrorEntry.setIndexNames(
    (0, "GRF-ATMP-MIB", "atmpHAIpAddress"),
    (0, "GRF-ATMP-MIB", "atmpHNTxErrorIndex"),
)
if mibBuilder.loadTexts:
    atmpHNTxErrorEntry.setStatus("mandatory")
_AtmpHNTxErrorIndex_Type = Integer32
_AtmpHNTxErrorIndex_Object = MibTableColumn
atmpHNTxErrorIndex = _AtmpHNTxErrorIndex_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 3, 1, 1),
    _AtmpHNTxErrorIndex_Type()
)
atmpHNTxErrorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpHNTxErrorIndex.setStatus("mandatory")
_AtmpHNTxErrorCode_Type = AtmpResultCode
_AtmpHNTxErrorCode_Object = MibTableColumn
atmpHNTxErrorCode = _AtmpHNTxErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 3, 1, 2),
    _AtmpHNTxErrorCode_Type()
)
atmpHNTxErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpHNTxErrorCode.setStatus("mandatory")
_AtmpHNTxErrorFAIpAddress_Type = IpAddress
_AtmpHNTxErrorFAIpAddress_Object = MibTableColumn
atmpHNTxErrorFAIpAddress = _AtmpHNTxErrorFAIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 3, 1, 3),
    _AtmpHNTxErrorFAIpAddress_Type()
)
atmpHNTxErrorFAIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpHNTxErrorFAIpAddress.setStatus("mandatory")
_AtmpHNTxErrorTime_Type = DisplayString
_AtmpHNTxErrorTime_Object = MibTableColumn
atmpHNTxErrorTime = _AtmpHNTxErrorTime_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 3, 1, 4),
    _AtmpHNTxErrorTime_Type()
)
atmpHNTxErrorTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpHNTxErrorTime.setStatus("mandatory")
_AtmpHNRxErrorTable_Object = MibTable
atmpHNRxErrorTable = _AtmpHNRxErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 4)
)
if mibBuilder.loadTexts:
    atmpHNRxErrorTable.setStatus("mandatory")
_AtmpHNRxErrorEntry_Object = MibTableRow
atmpHNRxErrorEntry = _AtmpHNRxErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 4, 1)
)
atmpHNRxErrorEntry.setIndexNames(
    (0, "GRF-ATMP-MIB", "atmpHAIpAddress"),
    (0, "GRF-ATMP-MIB", "atmpHNRxErrorIndex"),
)
if mibBuilder.loadTexts:
    atmpHNRxErrorEntry.setStatus("mandatory")
_AtmpHNRxErrorIndex_Type = Integer32
_AtmpHNRxErrorIndex_Object = MibTableColumn
atmpHNRxErrorIndex = _AtmpHNRxErrorIndex_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 4, 1, 1),
    _AtmpHNRxErrorIndex_Type()
)
atmpHNRxErrorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpHNRxErrorIndex.setStatus("mandatory")
_AtmpHNRxErrorCode_Type = AtmpResultCode
_AtmpHNRxErrorCode_Object = MibTableColumn
atmpHNRxErrorCode = _AtmpHNRxErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 4, 1, 2),
    _AtmpHNRxErrorCode_Type()
)
atmpHNRxErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpHNRxErrorCode.setStatus("mandatory")
_AtmpHNRxErrorFAIpAddress_Type = IpAddress
_AtmpHNRxErrorFAIpAddress_Object = MibTableColumn
atmpHNRxErrorFAIpAddress = _AtmpHNRxErrorFAIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 4, 1, 3),
    _AtmpHNRxErrorFAIpAddress_Type()
)
atmpHNRxErrorFAIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpHNRxErrorFAIpAddress.setStatus("mandatory")
_AtmpHNRxErrorTime_Type = DisplayString
_AtmpHNRxErrorTime_Object = MibTableColumn
atmpHNRxErrorTime = _AtmpHNRxErrorTime_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 4, 1, 4),
    _AtmpHNRxErrorTime_Type()
)
atmpHNRxErrorTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpHNRxErrorTime.setStatus("mandatory")
_AtmpHNInterfaceTable_Object = MibTable
atmpHNInterfaceTable = _AtmpHNInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 5)
)
if mibBuilder.loadTexts:
    atmpHNInterfaceTable.setStatus("mandatory")
_AtmpHNInterfaceEntry_Object = MibTableRow
atmpHNInterfaceEntry = _AtmpHNInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 5, 1)
)
atmpHNInterfaceEntry.setIndexNames(
    (0, "GRF-ATMP-MIB", "atmpHAIpAddress"),
    (0, "GRF-ATMP-MIB", "atmpHNInterfacePriority"),
)
if mibBuilder.loadTexts:
    atmpHNInterfaceEntry.setStatus("mandatory")


class _AtmpHNInterfacePriority_Type(Integer32):
    """Custom type atmpHNInterfacePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_AtmpHNInterfacePriority_Type.__name__ = "Integer32"
_AtmpHNInterfacePriority_Object = MibTableColumn
atmpHNInterfacePriority = _AtmpHNInterfacePriority_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 5, 1, 1),
    _AtmpHNInterfacePriority_Type()
)
atmpHNInterfacePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpHNInterfacePriority.setStatus("mandatory")
_AtmpHNInterfaceName_Type = DisplayString
_AtmpHNInterfaceName_Object = MibTableColumn
atmpHNInterfaceName = _AtmpHNInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 5, 1, 2),
    _AtmpHNInterfaceName_Type()
)
atmpHNInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpHNInterfaceName.setStatus("mandatory")


class _AtmpHNInterfaceConfigType_Type(Integer32):
    """Custom type atmpHNInterfaceConfigType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("circuit", 2),
          ("interface", 1))
    )


_AtmpHNInterfaceConfigType_Type.__name__ = "Integer32"
_AtmpHNInterfaceConfigType_Object = MibTableColumn
atmpHNInterfaceConfigType = _AtmpHNInterfaceConfigType_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 5, 1, 3),
    _AtmpHNInterfaceConfigType_Type()
)
atmpHNInterfaceConfigType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpHNInterfaceConfigType.setStatus("mandatory")
_AtmpHNInterfaceCard_Type = Integer32
_AtmpHNInterfaceCard_Object = MibTableColumn
atmpHNInterfaceCard = _AtmpHNInterfaceCard_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 5, 1, 4),
    _AtmpHNInterfaceCard_Type()
)
atmpHNInterfaceCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpHNInterfaceCard.setStatus("mandatory")
_AtmpHNInterfacePort_Type = Integer32
_AtmpHNInterfacePort_Object = MibTableColumn
atmpHNInterfacePort = _AtmpHNInterfacePort_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 5, 1, 5),
    _AtmpHNInterfacePort_Type()
)
atmpHNInterfacePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpHNInterfacePort.setStatus("mandatory")
_AtmpHNInterfaceDcliOrVpi_Type = Integer32
_AtmpHNInterfaceDcliOrVpi_Object = MibTableColumn
atmpHNInterfaceDcliOrVpi = _AtmpHNInterfaceDcliOrVpi_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 5, 1, 6),
    _AtmpHNInterfaceDcliOrVpi_Type()
)
atmpHNInterfaceDcliOrVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpHNInterfaceDcliOrVpi.setStatus("mandatory")
_AtmpHNInterfaceVci_Type = Integer32
_AtmpHNInterfaceVci_Object = MibTableColumn
atmpHNInterfaceVci = _AtmpHNInterfaceVci_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 5, 1, 7),
    _AtmpHNInterfaceVci_Type()
)
atmpHNInterfaceVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpHNInterfaceVci.setStatus("mandatory")
_AtmpHNInterfaceVpnAddress_Type = IpAddress
_AtmpHNInterfaceVpnAddress_Object = MibTableColumn
atmpHNInterfaceVpnAddress = _AtmpHNInterfaceVpnAddress_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 5, 1, 8),
    _AtmpHNInterfaceVpnAddress_Type()
)
atmpHNInterfaceVpnAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpHNInterfaceVpnAddress.setStatus("mandatory")


class _AtmpHNInterfaceVpnNetmaskSize_Type(Integer32):
    """Custom type atmpHNInterfaceVpnNetmaskSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_AtmpHNInterfaceVpnNetmaskSize_Type.__name__ = "Integer32"
_AtmpHNInterfaceVpnNetmaskSize_Object = MibTableColumn
atmpHNInterfaceVpnNetmaskSize = _AtmpHNInterfaceVpnNetmaskSize_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 5, 1, 9),
    _AtmpHNInterfaceVpnNetmaskSize_Type()
)
atmpHNInterfaceVpnNetmaskSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpHNInterfaceVpnNetmaskSize.setStatus("mandatory")


class _AtmpHNInterfaceRipv2Enabled_Type(Integer32):
    """Custom type atmpHNInterfaceRipv2Enabled based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AtmpHNInterfaceRipv2Enabled_Type.__name__ = "Integer32"
_AtmpHNInterfaceRipv2Enabled_Object = MibTableColumn
atmpHNInterfaceRipv2Enabled = _AtmpHNInterfaceRipv2Enabled_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 5, 1, 10),
    _AtmpHNInterfaceRipv2Enabled_Type()
)
atmpHNInterfaceRipv2Enabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpHNInterfaceRipv2Enabled.setStatus("mandatory")
_AtmpHNInterfaceRipv2Metric_Type = Integer32
_AtmpHNInterfaceRipv2Metric_Object = MibTableColumn
atmpHNInterfaceRipv2Metric = _AtmpHNInterfaceRipv2Metric_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 5, 1, 11),
    _AtmpHNInterfaceRipv2Metric_Type()
)
atmpHNInterfaceRipv2Metric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpHNInterfaceRipv2Metric.setStatus("mandatory")
_AtmpHNInterfaceRipv2Pkts_Type = Counter32
_AtmpHNInterfaceRipv2Pkts_Object = MibTableColumn
atmpHNInterfaceRipv2Pkts = _AtmpHNInterfaceRipv2Pkts_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 5, 1, 12),
    _AtmpHNInterfaceRipv2Pkts_Type()
)
atmpHNInterfaceRipv2Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpHNInterfaceRipv2Pkts.setStatus("mandatory")


class _AtmpHNInterfaceCompleteness_Type(Integer32):
    """Custom type atmpHNInterfaceCompleteness based on Integer32"""
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
        *(("complete", 2),
          ("from-circuit-no-if", 5),
          ("from-if-no-if", 6),
          ("no-map-to-circuit", 4),
          ("no-map-to-if", 3),
          ("uninitialized", 1))
    )


_AtmpHNInterfaceCompleteness_Type.__name__ = "Integer32"
_AtmpHNInterfaceCompleteness_Object = MibTableColumn
atmpHNInterfaceCompleteness = _AtmpHNInterfaceCompleteness_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 5, 1, 13),
    _AtmpHNInterfaceCompleteness_Type()
)
atmpHNInterfaceCompleteness.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpHNInterfaceCompleteness.setStatus("mandatory")
_AtmpTunnelTable_Object = MibTable
atmpTunnelTable = _AtmpTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 6)
)
if mibBuilder.loadTexts:
    atmpTunnelTable.setStatus("mandatory")
_AtmpTunnelEntry_Object = MibTableRow
atmpTunnelEntry = _AtmpTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 6, 1)
)
atmpTunnelEntry.setIndexNames(
    (0, "GRF-ATMP-MIB", "atmpHAIpAddress"),
    (0, "GRF-ATMP-MIB", "atmpTunnelMnIpAddress"),
)
if mibBuilder.loadTexts:
    atmpTunnelEntry.setStatus("mandatory")


class _AtmpTunnelId_Type(Integer32):
    """Custom type atmpTunnelId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmpTunnelId_Type.__name__ = "Integer32"
_AtmpTunnelId_Object = MibTableColumn
atmpTunnelId = _AtmpTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 6, 1, 1),
    _AtmpTunnelId_Type()
)
atmpTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpTunnelId.setStatus("mandatory")


class _AtmpTunnelState_Type(Integer32):
    """Custom type atmpTunnelState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("registering", 1),
          ("up", 2))
    )


_AtmpTunnelState_Type.__name__ = "Integer32"
_AtmpTunnelState_Object = MibTableColumn
atmpTunnelState = _AtmpTunnelState_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 6, 1, 2),
    _AtmpTunnelState_Type()
)
atmpTunnelState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpTunnelState.setStatus("mandatory")


class _AtmpTunnelProtocol_Type(Integer32):
    """Custom type atmpTunnelProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ip", 1),
          ("ipx", 2))
    )


_AtmpTunnelProtocol_Type.__name__ = "Integer32"
_AtmpTunnelProtocol_Object = MibTableColumn
atmpTunnelProtocol = _AtmpTunnelProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 6, 1, 3),
    _AtmpTunnelProtocol_Type()
)
atmpTunnelProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpTunnelProtocol.setStatus("mandatory")
_AtmpTunnelFAIpAddress_Type = IpAddress
_AtmpTunnelFAIpAddress_Object = MibTableColumn
atmpTunnelFAIpAddress = _AtmpTunnelFAIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 6, 1, 4),
    _AtmpTunnelFAIpAddress_Type()
)
atmpTunnelFAIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpTunnelFAIpAddress.setStatus("mandatory")
_AtmpTunnelMnIpAddress_Type = IpAddress
_AtmpTunnelMnIpAddress_Object = MibTableColumn
atmpTunnelMnIpAddress = _AtmpTunnelMnIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 6, 1, 5),
    _AtmpTunnelMnIpAddress_Type()
)
atmpTunnelMnIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpTunnelMnIpAddress.setStatus("mandatory")
_AtmpTunnelMnNetmask_Type = IpAddress
_AtmpTunnelMnNetmask_Object = MibTableColumn
atmpTunnelMnNetmask = _AtmpTunnelMnNetmask_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 6, 1, 6),
    _AtmpTunnelMnNetmask_Type()
)
atmpTunnelMnNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpTunnelMnNetmask.setStatus("mandatory")


class _AtmpTunnelMnIpxNetAddress_Type(OctetString):
    """Custom type atmpTunnelMnIpxNetAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_AtmpTunnelMnIpxNetAddress_Type.__name__ = "OctetString"
_AtmpTunnelMnIpxNetAddress_Object = MibTableColumn
atmpTunnelMnIpxNetAddress = _AtmpTunnelMnIpxNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 6, 1, 7),
    _AtmpTunnelMnIpxNetAddress_Type()
)
atmpTunnelMnIpxNetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpTunnelMnIpxNetAddress.setStatus("mandatory")


class _AtmpTunnelMnIpxNodeAddress_Type(OctetString):
    """Custom type atmpTunnelMnIpxNodeAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_AtmpTunnelMnIpxNodeAddress_Type.__name__ = "OctetString"
_AtmpTunnelMnIpxNodeAddress_Object = MibTableColumn
atmpTunnelMnIpxNodeAddress = _AtmpTunnelMnIpxNodeAddress_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 6, 1, 8),
    _AtmpTunnelMnIpxNodeAddress_Type()
)
atmpTunnelMnIpxNodeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpTunnelMnIpxNodeAddress.setStatus("mandatory")


class _AtmpTunnelActive_Type(Integer32):
    """Custom type atmpTunnelActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_AtmpTunnelActive_Type.__name__ = "Integer32"
_AtmpTunnelActive_Object = MibTableColumn
atmpTunnelActive = _AtmpTunnelActive_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 6, 1, 9),
    _AtmpTunnelActive_Type()
)
atmpTunnelActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpTunnelActive.setStatus("mandatory")
_AtmpTunnelInPkts_Type = Counter32
_AtmpTunnelInPkts_Object = MibTableColumn
atmpTunnelInPkts = _AtmpTunnelInPkts_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 6, 1, 10),
    _AtmpTunnelInPkts_Type()
)
atmpTunnelInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpTunnelInPkts.setStatus("mandatory")
_AtmpTunnelInOctets_Type = Counter32
_AtmpTunnelInOctets_Object = MibTableColumn
atmpTunnelInOctets = _AtmpTunnelInOctets_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 6, 1, 11),
    _AtmpTunnelInOctets_Type()
)
atmpTunnelInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpTunnelInOctets.setStatus("mandatory")
_AtmpTunnelInErrPkts_Type = Counter32
_AtmpTunnelInErrPkts_Object = MibTableColumn
atmpTunnelInErrPkts = _AtmpTunnelInErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 6, 1, 12),
    _AtmpTunnelInErrPkts_Type()
)
atmpTunnelInErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpTunnelInErrPkts.setStatus("mandatory")
_AtmpTunnelOutPkts_Type = Counter32
_AtmpTunnelOutPkts_Object = MibTableColumn
atmpTunnelOutPkts = _AtmpTunnelOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 6, 1, 13),
    _AtmpTunnelOutPkts_Type()
)
atmpTunnelOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpTunnelOutPkts.setStatus("mandatory")
_AtmpTunnelOutOctets_Type = Counter32
_AtmpTunnelOutOctets_Object = MibTableColumn
atmpTunnelOutOctets = _AtmpTunnelOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 6, 1, 14),
    _AtmpTunnelOutOctets_Type()
)
atmpTunnelOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpTunnelOutOctets.setStatus("mandatory")
_AtmpTunnelOutErrPkts_Type = Counter32
_AtmpTunnelOutErrPkts_Object = MibTableColumn
atmpTunnelOutErrPkts = _AtmpTunnelOutErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 6, 1, 15),
    _AtmpTunnelOutErrPkts_Type()
)
atmpTunnelOutErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpTunnelOutErrPkts.setStatus("mandatory")
_AtmpTunnelInOctetRate_Type = Integer32
_AtmpTunnelInOctetRate_Object = MibTableColumn
atmpTunnelInOctetRate = _AtmpTunnelInOctetRate_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 6, 1, 16),
    _AtmpTunnelInOctetRate_Type()
)
atmpTunnelInOctetRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpTunnelInOctetRate.setStatus("mandatory")
_AtmpTunnelInOctetSampleRate_Type = Integer32
_AtmpTunnelInOctetSampleRate_Object = MibTableColumn
atmpTunnelInOctetSampleRate = _AtmpTunnelInOctetSampleRate_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 6, 1, 17),
    _AtmpTunnelInOctetSampleRate_Type()
)
atmpTunnelInOctetSampleRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpTunnelInOctetSampleRate.setStatus("mandatory")
_AtmpTunnelOutOctetRate_Type = Integer32
_AtmpTunnelOutOctetRate_Object = MibTableColumn
atmpTunnelOutOctetRate = _AtmpTunnelOutOctetRate_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 6, 1, 18),
    _AtmpTunnelOutOctetRate_Type()
)
atmpTunnelOutOctetRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpTunnelOutOctetRate.setStatus("mandatory")
_AtmpTunnelOutOctetSampleRate_Type = Integer32
_AtmpTunnelOutOctetSampleRate_Object = MibTableColumn
atmpTunnelOutOctetSampleRate = _AtmpTunnelOutOctetSampleRate_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 6, 1, 19),
    _AtmpTunnelOutOctetSampleRate_Type()
)
atmpTunnelOutOctetSampleRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpTunnelOutOctetSampleRate.setStatus("mandatory")
_AtmpTunnelForcedToFragmentPkts_Type = Counter32
_AtmpTunnelForcedToFragmentPkts_Object = MibTableColumn
atmpTunnelForcedToFragmentPkts = _AtmpTunnelForcedToFragmentPkts_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 6, 1, 20),
    _AtmpTunnelForcedToFragmentPkts_Type()
)
atmpTunnelForcedToFragmentPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpTunnelForcedToFragmentPkts.setStatus("mandatory")
_AtmpTunnelFailedToFragmentPkts_Type = Counter32
_AtmpTunnelFailedToFragmentPkts_Object = MibTableColumn
atmpTunnelFailedToFragmentPkts = _AtmpTunnelFailedToFragmentPkts_Object(
    (1, 3, 6, 1, 4, 1, 1080, 1, 1, 8, 6, 6, 1, 21),
    _AtmpTunnelFailedToFragmentPkts_Type()
)
atmpTunnelFailedToFragmentPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmpTunnelFailedToFragmentPkts.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GRF-ATMP-MIB",
    **{"AtmpResultCode": AtmpResultCode,
       "atmpMIBVersion": atmpMIBVersion,
       "atmpMIBVersionMajor": atmpMIBVersionMajor,
       "atmpMIBVersionMinor": atmpMIBVersionMinor,
       "atmpGeneralConfig": atmpGeneralConfig,
       "atmpUDPPort": atmpUDPPort,
       "atmpEnableAtmpTraps": atmpEnableAtmpTraps,
       "atmpNumberFAs": atmpNumberFAs,
       "atmpNumberHNs": atmpNumberHNs,
       "atmpMaxNumberHNs": atmpMaxNumberHNs,
       "atmpDFAConfig": atmpDFAConfig,
       "atmpDFAConfigured": atmpDFAConfigured,
       "atmpDFAWildcardIpAddress": atmpDFAWildcardIpAddress,
       "atmpDFAPassword": atmpDFAPassword,
       "atmpGeneralStats": atmpGeneralStats,
       "atmpNumberTunnelsUp": atmpNumberTunnelsUp,
       "atmpNumberTunnelsRegistering": atmpNumberTunnelsRegistering,
       "atmpNumberFAFailingMatch": atmpNumberFAFailingMatch,
       "atmpNumberFAPasswordRejects": atmpNumberFAPasswordRejects,
       "atmpNumberDFAMatch": atmpNumberDFAMatch,
       "atmpProtocolStats": atmpProtocolStats,
       "atmpRxRegistrationRequestPkts": atmpRxRegistrationRequestPkts,
       "atmpTxChallengeRequestPkts": atmpTxChallengeRequestPkts,
       "atmpRxChallengeReplyPkts": atmpRxChallengeReplyPkts,
       "atmpTxRegistrationReplyPkts": atmpTxRegistrationReplyPkts,
       "atmpRxDeRegistrationRequestPkts": atmpRxDeRegistrationRequestPkts,
       "atmpTxDeRegistrationReplyPkts": atmpTxDeRegistrationReplyPkts,
       "atmpReceiveProtocolErrorStats": atmpReceiveProtocolErrorStats,
       "atmpRxErrorNotificationPkts": atmpRxErrorNotificationPkts,
       "atmpRxNoErrorPkts": atmpRxNoErrorPkts,
       "atmpRxAuthFailedPkts": atmpRxAuthFailedPkts,
       "atmpRxNotEnabledPkts": atmpRxNotEnabledPkts,
       "atmpRxTooManyPkts": atmpRxTooManyPkts,
       "atmpRxParameterErrorPkts": atmpRxParameterErrorPkts,
       "atmpRxInvalidTunnelIdPkts": atmpRxInvalidTunnelIdPkts,
       "atmpRxTimeoutPkts": atmpRxTimeoutPkts,
       "atmpRxNetUnreachablePkts": atmpRxNetUnreachablePkts,
       "atmpRxGeneralErrorPkts": atmpRxGeneralErrorPkts,
       "atmpRxChallengeRequestPkts": atmpRxChallengeRequestPkts,
       "atmpRxRegistrationReplyPkts": atmpRxRegistrationReplyPkts,
       "atmpRxDeRegistrationReplyPkts": atmpRxDeRegistrationReplyPkts,
       "atmpRxUndersizeLengthPkts": atmpRxUndersizeLengthPkts,
       "atmpRxBadVersionPkts": atmpRxBadVersionPkts,
       "atmpRxBufferAllocFailPkts": atmpRxBufferAllocFailPkts,
       "atmpRxBadAtmpCodePkts": atmpRxBadAtmpCodePkts,
       "atmpRxNetworkErrors": atmpRxNetworkErrors,
       "atmpTransmitProtocolErrorStats": atmpTransmitProtocolErrorStats,
       "atmpTxErrorNotificationPkts": atmpTxErrorNotificationPkts,
       "atmpTxNoErrorPkts": atmpTxNoErrorPkts,
       "atmpTxAuthFailedPkts": atmpTxAuthFailedPkts,
       "atmpTxNotEnabledPkts": atmpTxNotEnabledPkts,
       "atmpTxTooManyPkts": atmpTxTooManyPkts,
       "atmpTxParameterErrorPkts": atmpTxParameterErrorPkts,
       "atmpTxInvalidTunnelIdPkts": atmpTxInvalidTunnelIdPkts,
       "atmpTxTimeoutPkts": atmpTxTimeoutPkts,
       "atmpTxNetUnreachablePkts": atmpTxNetUnreachablePkts,
       "atmpTxGeneralErrorPkts": atmpTxGeneralErrorPkts,
       "atmpTxNetworkErrors": atmpTxNetworkErrors,
       "atmpTables": atmpTables,
       "atmpFATable": atmpFATable,
       "atmpFAEntry": atmpFAEntry,
       "atmpFAIpAddress": atmpFAIpAddress,
       "atmpFAPassword": atmpFAPassword,
       "atmpFANumberTunnels": atmpFANumberTunnels,
       "atmpHNTable": atmpHNTable,
       "atmpHNEntry": atmpHNEntry,
       "atmpHAIpAddress": atmpHAIpAddress,
       "atmpHNName": atmpHNName,
       "atmpHNMTULimit": atmpHNMTULimit,
       "atmpHNForceFragmentation": atmpHNForceFragmentation,
       "atmpHNBadSourceNotification": atmpHNBadSourceNotification,
       "atmpHNMaxTunnels": atmpHNMaxTunnels,
       "atmpHNInactivityTimeout": atmpHNInactivityTimeout,
       "atmpHNNumberTunnels": atmpHNNumberTunnels,
       "atmpHNInactiveTunnelsRemoved": atmpHNInactiveTunnelsRemoved,
       "atmpHNTunnelsMaxRejected": atmpHNTunnelsMaxRejected,
       "atmpHNTunnelHighWater": atmpHNTunnelHighWater,
       "atmpHNSwitchToStandbyInterface": atmpHNSwitchToStandbyInterface,
       "atmpHNSwitchToPrimaryInterface": atmpHNSwitchToPrimaryInterface,
       "atmpHNRxErrorCount": atmpHNRxErrorCount,
       "atmpHNTxErrorCount": atmpHNTxErrorCount,
       "atmpHNInterfaceCount": atmpHNInterfaceCount,
       "atmpHNTxErrorTable": atmpHNTxErrorTable,
       "atmpHNTxErrorEntry": atmpHNTxErrorEntry,
       "atmpHNTxErrorIndex": atmpHNTxErrorIndex,
       "atmpHNTxErrorCode": atmpHNTxErrorCode,
       "atmpHNTxErrorFAIpAddress": atmpHNTxErrorFAIpAddress,
       "atmpHNTxErrorTime": atmpHNTxErrorTime,
       "atmpHNRxErrorTable": atmpHNRxErrorTable,
       "atmpHNRxErrorEntry": atmpHNRxErrorEntry,
       "atmpHNRxErrorIndex": atmpHNRxErrorIndex,
       "atmpHNRxErrorCode": atmpHNRxErrorCode,
       "atmpHNRxErrorFAIpAddress": atmpHNRxErrorFAIpAddress,
       "atmpHNRxErrorTime": atmpHNRxErrorTime,
       "atmpHNInterfaceTable": atmpHNInterfaceTable,
       "atmpHNInterfaceEntry": atmpHNInterfaceEntry,
       "atmpHNInterfacePriority": atmpHNInterfacePriority,
       "atmpHNInterfaceName": atmpHNInterfaceName,
       "atmpHNInterfaceConfigType": atmpHNInterfaceConfigType,
       "atmpHNInterfaceCard": atmpHNInterfaceCard,
       "atmpHNInterfacePort": atmpHNInterfacePort,
       "atmpHNInterfaceDcliOrVpi": atmpHNInterfaceDcliOrVpi,
       "atmpHNInterfaceVci": atmpHNInterfaceVci,
       "atmpHNInterfaceVpnAddress": atmpHNInterfaceVpnAddress,
       "atmpHNInterfaceVpnNetmaskSize": atmpHNInterfaceVpnNetmaskSize,
       "atmpHNInterfaceRipv2Enabled": atmpHNInterfaceRipv2Enabled,
       "atmpHNInterfaceRipv2Metric": atmpHNInterfaceRipv2Metric,
       "atmpHNInterfaceRipv2Pkts": atmpHNInterfaceRipv2Pkts,
       "atmpHNInterfaceCompleteness": atmpHNInterfaceCompleteness,
       "atmpTunnelTable": atmpTunnelTable,
       "atmpTunnelEntry": atmpTunnelEntry,
       "atmpTunnelId": atmpTunnelId,
       "atmpTunnelState": atmpTunnelState,
       "atmpTunnelProtocol": atmpTunnelProtocol,
       "atmpTunnelFAIpAddress": atmpTunnelFAIpAddress,
       "atmpTunnelMnIpAddress": atmpTunnelMnIpAddress,
       "atmpTunnelMnNetmask": atmpTunnelMnNetmask,
       "atmpTunnelMnIpxNetAddress": atmpTunnelMnIpxNetAddress,
       "atmpTunnelMnIpxNodeAddress": atmpTunnelMnIpxNodeAddress,
       "atmpTunnelActive": atmpTunnelActive,
       "atmpTunnelInPkts": atmpTunnelInPkts,
       "atmpTunnelInOctets": atmpTunnelInOctets,
       "atmpTunnelInErrPkts": atmpTunnelInErrPkts,
       "atmpTunnelOutPkts": atmpTunnelOutPkts,
       "atmpTunnelOutOctets": atmpTunnelOutOctets,
       "atmpTunnelOutErrPkts": atmpTunnelOutErrPkts,
       "atmpTunnelInOctetRate": atmpTunnelInOctetRate,
       "atmpTunnelInOctetSampleRate": atmpTunnelInOctetSampleRate,
       "atmpTunnelOutOctetRate": atmpTunnelOutOctetRate,
       "atmpTunnelOutOctetSampleRate": atmpTunnelOutOctetSampleRate,
       "atmpTunnelForcedToFragmentPkts": atmpTunnelForcedToFragmentPkts,
       "atmpTunnelFailedToFragmentPkts": atmpTunnelFailedToFragmentPkts}
)
