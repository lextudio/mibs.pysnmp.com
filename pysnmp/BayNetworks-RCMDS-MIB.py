# SNMP MIB module (BayNetworks-RCMDS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BayNetworks-RCMDS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:50:22 2024
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

(wfRcmdsGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfRcmdsGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfRcmds_ObjectIdentity = ObjectIdentity
wfRcmds = _WfRcmds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 1)
)


class _WfRcmdsDelete_Type(Integer32):
    """Custom type wfRcmdsDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfRcmdsDelete_Type.__name__ = "Integer32"
_WfRcmdsDelete_Object = MibScalar
wfRcmdsDelete = _WfRcmdsDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 1, 1),
    _WfRcmdsDelete_Type()
)
wfRcmdsDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRcmdsDelete.setStatus("mandatory")


class _WfRcmdsDisable_Type(Integer32):
    """Custom type wfRcmdsDisable based on Integer32"""
    defaultValue = 1

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


_WfRcmdsDisable_Type.__name__ = "Integer32"
_WfRcmdsDisable_Object = MibScalar
wfRcmdsDisable = _WfRcmdsDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 1, 2),
    _WfRcmdsDisable_Type()
)
wfRcmdsDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRcmdsDisable.setStatus("mandatory")


class _WfRcmdsReservedPort_Type(Integer32):
    """Custom type wfRcmdsReservedPort based on Integer32"""
    defaultValue = 1023

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 1023),
    )


_WfRcmdsReservedPort_Type.__name__ = "Integer32"
_WfRcmdsReservedPort_Object = MibScalar
wfRcmdsReservedPort = _WfRcmdsReservedPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 1, 3),
    _WfRcmdsReservedPort_Type()
)
wfRcmdsReservedPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRcmdsReservedPort.setStatus("mandatory")
_WfRcmdsKerberosDefaultRealmName_Type = DisplayString
_WfRcmdsKerberosDefaultRealmName_Object = MibScalar
wfRcmdsKerberosDefaultRealmName = _WfRcmdsKerberosDefaultRealmName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 1, 4),
    _WfRcmdsKerberosDefaultRealmName_Type()
)
wfRcmdsKerberosDefaultRealmName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRcmdsKerberosDefaultRealmName.setStatus("mandatory")
_WfRcmdsKerberosKDCName_Type = DisplayString
_WfRcmdsKerberosKDCName_Object = MibScalar
wfRcmdsKerberosKDCName = _WfRcmdsKerberosKDCName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 1, 5),
    _WfRcmdsKerberosKDCName_Type()
)
wfRcmdsKerberosKDCName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRcmdsKerberosKDCName.setStatus("mandatory")
_WfRcmdsRouterHostName_Type = DisplayString
_WfRcmdsRouterHostName_Object = MibScalar
wfRcmdsRouterHostName = _WfRcmdsRouterHostName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 1, 6),
    _WfRcmdsRouterHostName_Type()
)
wfRcmdsRouterHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRcmdsRouterHostName.setStatus("mandatory")
_WfRcmdsKerberosHostServiceKey_Type = OctetString
_WfRcmdsKerberosHostServiceKey_Object = MibScalar
wfRcmdsKerberosHostServiceKey = _WfRcmdsKerberosHostServiceKey_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 1, 7),
    _WfRcmdsKerberosHostServiceKey_Type()
)
wfRcmdsKerberosHostServiceKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRcmdsKerberosHostServiceKey.setStatus("mandatory")
_WfRcmdsRlogind_ObjectIdentity = ObjectIdentity
wfRcmdsRlogind = _WfRcmdsRlogind_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 2)
)


class _WfRcmdsRlogindDelete_Type(Integer32):
    """Custom type wfRcmdsRlogindDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfRcmdsRlogindDelete_Type.__name__ = "Integer32"
_WfRcmdsRlogindDelete_Object = MibScalar
wfRcmdsRlogindDelete = _WfRcmdsRlogindDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 2, 1),
    _WfRcmdsRlogindDelete_Type()
)
wfRcmdsRlogindDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRcmdsRlogindDelete.setStatus("mandatory")


class _WfRcmdsRlogindDisable_Type(Integer32):
    """Custom type wfRcmdsRlogindDisable based on Integer32"""
    defaultValue = 1

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


_WfRcmdsRlogindDisable_Type.__name__ = "Integer32"
_WfRcmdsRlogindDisable_Object = MibScalar
wfRcmdsRlogindDisable = _WfRcmdsRlogindDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 2, 2),
    _WfRcmdsRlogindDisable_Type()
)
wfRcmdsRlogindDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRcmdsRlogindDisable.setStatus("mandatory")


class _WfRcmdsRlogindState_Type(Integer32):
    """Custom type wfRcmdsRlogindState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_WfRcmdsRlogindState_Type.__name__ = "Integer32"
_WfRcmdsRlogindState_Object = MibScalar
wfRcmdsRlogindState = _WfRcmdsRlogindState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 2, 3),
    _WfRcmdsRlogindState_Type()
)
wfRcmdsRlogindState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRcmdsRlogindState.setStatus("mandatory")


class _WfRcmdsRlogindMoreDisable_Type(Integer32):
    """Custom type wfRcmdsRlogindMoreDisable based on Integer32"""
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


_WfRcmdsRlogindMoreDisable_Type.__name__ = "Integer32"
_WfRcmdsRlogindMoreDisable_Object = MibScalar
wfRcmdsRlogindMoreDisable = _WfRcmdsRlogindMoreDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 2, 4),
    _WfRcmdsRlogindMoreDisable_Type()
)
wfRcmdsRlogindMoreDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRcmdsRlogindMoreDisable.setStatus("mandatory")
_WfRcmdsRlogindPrompt_Type = DisplayString
_WfRcmdsRlogindPrompt_Object = MibScalar
wfRcmdsRlogindPrompt = _WfRcmdsRlogindPrompt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 2, 5),
    _WfRcmdsRlogindPrompt_Type()
)
wfRcmdsRlogindPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRcmdsRlogindPrompt.setStatus("mandatory")


class _WfRcmdsRlogindLoginTimeOut_Type(Integer32):
    """Custom type wfRcmdsRlogindLoginTimeOut based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_WfRcmdsRlogindLoginTimeOut_Type.__name__ = "Integer32"
_WfRcmdsRlogindLoginTimeOut_Object = MibScalar
wfRcmdsRlogindLoginTimeOut = _WfRcmdsRlogindLoginTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 2, 6),
    _WfRcmdsRlogindLoginTimeOut_Type()
)
wfRcmdsRlogindLoginTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRcmdsRlogindLoginTimeOut.setStatus("mandatory")


class _WfRcmdsRlogindPasswordTimeOut_Type(Integer32):
    """Custom type wfRcmdsRlogindPasswordTimeOut based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_WfRcmdsRlogindPasswordTimeOut_Type.__name__ = "Integer32"
_WfRcmdsRlogindPasswordTimeOut_Object = MibScalar
wfRcmdsRlogindPasswordTimeOut = _WfRcmdsRlogindPasswordTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 2, 7),
    _WfRcmdsRlogindPasswordTimeOut_Type()
)
wfRcmdsRlogindPasswordTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRcmdsRlogindPasswordTimeOut.setStatus("mandatory")


class _WfRcmdsRlogindCommandTimeOut_Type(Integer32):
    """Custom type wfRcmdsRlogindCommandTimeOut based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_WfRcmdsRlogindCommandTimeOut_Type.__name__ = "Integer32"
_WfRcmdsRlogindCommandTimeOut_Object = MibScalar
wfRcmdsRlogindCommandTimeOut = _WfRcmdsRlogindCommandTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 2, 8),
    _WfRcmdsRlogindCommandTimeOut_Type()
)
wfRcmdsRlogindCommandTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRcmdsRlogindCommandTimeOut.setStatus("mandatory")


class _WfRcmdsRlogindLoginRetries_Type(Integer32):
    """Custom type wfRcmdsRlogindLoginRetries based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_WfRcmdsRlogindLoginRetries_Type.__name__ = "Integer32"
_WfRcmdsRlogindLoginRetries_Object = MibScalar
wfRcmdsRlogindLoginRetries = _WfRcmdsRlogindLoginRetries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 2, 9),
    _WfRcmdsRlogindLoginRetries_Type()
)
wfRcmdsRlogindLoginRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRcmdsRlogindLoginRetries.setStatus("mandatory")
_WfRcmdsRlogindTotalLogins_Type = Counter32
_WfRcmdsRlogindTotalLogins_Object = MibScalar
wfRcmdsRlogindTotalLogins = _WfRcmdsRlogindTotalLogins_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 2, 10),
    _WfRcmdsRlogindTotalLogins_Type()
)
wfRcmdsRlogindTotalLogins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRcmdsRlogindTotalLogins.setStatus("mandatory")
_WfRcmdsRlogindUserLoginErrors_Type = Counter32
_WfRcmdsRlogindUserLoginErrors_Object = MibScalar
wfRcmdsRlogindUserLoginErrors = _WfRcmdsRlogindUserLoginErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 2, 11),
    _WfRcmdsRlogindUserLoginErrors_Type()
)
wfRcmdsRlogindUserLoginErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRcmdsRlogindUserLoginErrors.setStatus("mandatory")
_WfRcmdsRlogindManagerLoginErrors_Type = Counter32
_WfRcmdsRlogindManagerLoginErrors_Object = MibScalar
wfRcmdsRlogindManagerLoginErrors = _WfRcmdsRlogindManagerLoginErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 2, 12),
    _WfRcmdsRlogindManagerLoginErrors_Type()
)
wfRcmdsRlogindManagerLoginErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRcmdsRlogindManagerLoginErrors.setStatus("mandatory")
_WfRcmdsRlogindOtherLoginErrors_Type = Counter32
_WfRcmdsRlogindOtherLoginErrors_Object = MibScalar
wfRcmdsRlogindOtherLoginErrors = _WfRcmdsRlogindOtherLoginErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 2, 13),
    _WfRcmdsRlogindOtherLoginErrors_Type()
)
wfRcmdsRlogindOtherLoginErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRcmdsRlogindOtherLoginErrors.setStatus("mandatory")
_WfRcmdsRlogindActiveSessions_Type = Gauge32
_WfRcmdsRlogindActiveSessions_Object = MibScalar
wfRcmdsRlogindActiveSessions = _WfRcmdsRlogindActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 2, 14),
    _WfRcmdsRlogindActiveSessions_Type()
)
wfRcmdsRlogindActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRcmdsRlogindActiveSessions.setStatus("mandatory")
_WfRcmdsRlogindManagerAutoScript_Type = DisplayString
_WfRcmdsRlogindManagerAutoScript_Object = MibScalar
wfRcmdsRlogindManagerAutoScript = _WfRcmdsRlogindManagerAutoScript_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 2, 15),
    _WfRcmdsRlogindManagerAutoScript_Type()
)
wfRcmdsRlogindManagerAutoScript.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRcmdsRlogindManagerAutoScript.setStatus("mandatory")
_WfRcmdsRlogindUserAutoScript_Type = DisplayString
_WfRcmdsRlogindUserAutoScript_Object = MibScalar
wfRcmdsRlogindUserAutoScript = _WfRcmdsRlogindUserAutoScript_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 2, 16),
    _WfRcmdsRlogindUserAutoScript_Type()
)
wfRcmdsRlogindUserAutoScript.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRcmdsRlogindUserAutoScript.setStatus("mandatory")


class _WfRcmdsRlogindUserAbortLogoutDisable_Type(Integer32):
    """Custom type wfRcmdsRlogindUserAbortLogoutDisable based on Integer32"""
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


_WfRcmdsRlogindUserAbortLogoutDisable_Type.__name__ = "Integer32"
_WfRcmdsRlogindUserAbortLogoutDisable_Object = MibScalar
wfRcmdsRlogindUserAbortLogoutDisable = _WfRcmdsRlogindUserAbortLogoutDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 2, 17),
    _WfRcmdsRlogindUserAbortLogoutDisable_Type()
)
wfRcmdsRlogindUserAbortLogoutDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRcmdsRlogindUserAbortLogoutDisable.setStatus("mandatory")


class _WfRcmdsRlogindHistoryDepth_Type(Integer32):
    """Custom type wfRcmdsRlogindHistoryDepth based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_WfRcmdsRlogindHistoryDepth_Type.__name__ = "Integer32"
_WfRcmdsRlogindHistoryDepth_Object = MibScalar
wfRcmdsRlogindHistoryDepth = _WfRcmdsRlogindHistoryDepth_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 2, 18),
    _WfRcmdsRlogindHistoryDepth_Type()
)
wfRcmdsRlogindHistoryDepth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRcmdsRlogindHistoryDepth.setStatus("mandatory")


class _WfRcmdsRlogindTcpPort_Type(Integer32):
    """Custom type wfRcmdsRlogindTcpPort based on Integer32"""
    defaultValue = 543


_WfRcmdsRlogindTcpPort_Object = MibScalar
wfRcmdsRlogindTcpPort = _WfRcmdsRlogindTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 2, 19),
    _WfRcmdsRlogindTcpPort_Type()
)
wfRcmdsRlogindTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRcmdsRlogindTcpPort.setStatus("mandatory")


class _WfRcmdsRlogindTrustedHostAuthentication_Type(Integer32):
    """Custom type wfRcmdsRlogindTrustedHostAuthentication based on Integer32"""
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


_WfRcmdsRlogindTrustedHostAuthentication_Type.__name__ = "Integer32"
_WfRcmdsRlogindTrustedHostAuthentication_Object = MibScalar
wfRcmdsRlogindTrustedHostAuthentication = _WfRcmdsRlogindTrustedHostAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 2, 20),
    _WfRcmdsRlogindTrustedHostAuthentication_Type()
)
wfRcmdsRlogindTrustedHostAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRcmdsRlogindTrustedHostAuthentication.setStatus("mandatory")


class _WfRcmdsRlogindKerberosAuthentication_Type(Integer32):
    """Custom type wfRcmdsRlogindKerberosAuthentication based on Integer32"""
    defaultValue = 1

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


_WfRcmdsRlogindKerberosAuthentication_Type.__name__ = "Integer32"
_WfRcmdsRlogindKerberosAuthentication_Object = MibScalar
wfRcmdsRlogindKerberosAuthentication = _WfRcmdsRlogindKerberosAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 2, 21),
    _WfRcmdsRlogindKerberosAuthentication_Type()
)
wfRcmdsRlogindKerberosAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRcmdsRlogindKerberosAuthentication.setStatus("mandatory")


class _WfRcmdsRlogindKerberosSessionTypeAllowed_Type(Integer32):
    """Custom type wfRcmdsRlogindKerberosSessionTypeAllowed based on Integer32"""
    defaultValue = 1

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
        *(("both", 1),
          ("encrypted", 2),
          ("none", 4),
          ("unencrypted", 3))
    )


_WfRcmdsRlogindKerberosSessionTypeAllowed_Type.__name__ = "Integer32"
_WfRcmdsRlogindKerberosSessionTypeAllowed_Object = MibScalar
wfRcmdsRlogindKerberosSessionTypeAllowed = _WfRcmdsRlogindKerberosSessionTypeAllowed_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 2, 22),
    _WfRcmdsRlogindKerberosSessionTypeAllowed_Type()
)
wfRcmdsRlogindKerberosSessionTypeAllowed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRcmdsRlogindKerberosSessionTypeAllowed.setStatus("mandatory")
_WfRcmdsRshd_ObjectIdentity = ObjectIdentity
wfRcmdsRshd = _WfRcmdsRshd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 3)
)


class _WfRcmdsRshdDelete_Type(Integer32):
    """Custom type wfRcmdsRshdDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfRcmdsRshdDelete_Type.__name__ = "Integer32"
_WfRcmdsRshdDelete_Object = MibScalar
wfRcmdsRshdDelete = _WfRcmdsRshdDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 3, 1),
    _WfRcmdsRshdDelete_Type()
)
wfRcmdsRshdDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRcmdsRshdDelete.setStatus("mandatory")


class _WfRcmdsRshdDisable_Type(Integer32):
    """Custom type wfRcmdsRshdDisable based on Integer32"""
    defaultValue = 1

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


_WfRcmdsRshdDisable_Type.__name__ = "Integer32"
_WfRcmdsRshdDisable_Object = MibScalar
wfRcmdsRshdDisable = _WfRcmdsRshdDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 3, 2),
    _WfRcmdsRshdDisable_Type()
)
wfRcmdsRshdDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRcmdsRshdDisable.setStatus("mandatory")


class _WfRcmdsRshdState_Type(Integer32):
    """Custom type wfRcmdsRshdState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_WfRcmdsRshdState_Type.__name__ = "Integer32"
_WfRcmdsRshdState_Object = MibScalar
wfRcmdsRshdState = _WfRcmdsRshdState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 3, 3),
    _WfRcmdsRshdState_Type()
)
wfRcmdsRshdState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRcmdsRshdState.setStatus("mandatory")
_WfRcmdsRshdTotalSessions_Type = Counter32
_WfRcmdsRshdTotalSessions_Object = MibScalar
wfRcmdsRshdTotalSessions = _WfRcmdsRshdTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 3, 4),
    _WfRcmdsRshdTotalSessions_Type()
)
wfRcmdsRshdTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRcmdsRshdTotalSessions.setStatus("mandatory")


class _WfRcmdsRshdTcpPort_Type(Integer32):
    """Custom type wfRcmdsRshdTcpPort based on Integer32"""
    defaultValue = 544


_WfRcmdsRshdTcpPort_Object = MibScalar
wfRcmdsRshdTcpPort = _WfRcmdsRshdTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 3, 5),
    _WfRcmdsRshdTcpPort_Type()
)
wfRcmdsRshdTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRcmdsRshdTcpPort.setStatus("mandatory")


class _WfRcmdsRshdTrustedHostAuthentication_Type(Integer32):
    """Custom type wfRcmdsRshdTrustedHostAuthentication based on Integer32"""
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


_WfRcmdsRshdTrustedHostAuthentication_Type.__name__ = "Integer32"
_WfRcmdsRshdTrustedHostAuthentication_Object = MibScalar
wfRcmdsRshdTrustedHostAuthentication = _WfRcmdsRshdTrustedHostAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 3, 6),
    _WfRcmdsRshdTrustedHostAuthentication_Type()
)
wfRcmdsRshdTrustedHostAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRcmdsRshdTrustedHostAuthentication.setStatus("mandatory")


class _WfRcmdsRshdKerberosAuthentication_Type(Integer32):
    """Custom type wfRcmdsRshdKerberosAuthentication based on Integer32"""
    defaultValue = 1

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


_WfRcmdsRshdKerberosAuthentication_Type.__name__ = "Integer32"
_WfRcmdsRshdKerberosAuthentication_Object = MibScalar
wfRcmdsRshdKerberosAuthentication = _WfRcmdsRshdKerberosAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 3, 7),
    _WfRcmdsRshdKerberosAuthentication_Type()
)
wfRcmdsRshdKerberosAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRcmdsRshdKerberosAuthentication.setStatus("mandatory")


class _WfRcmdsRshdKerberosSessionTypeAllowed_Type(Integer32):
    """Custom type wfRcmdsRshdKerberosSessionTypeAllowed based on Integer32"""
    defaultValue = 1

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
        *(("both", 1),
          ("encrypted", 2),
          ("none", 4),
          ("unencrypted", 3))
    )


_WfRcmdsRshdKerberosSessionTypeAllowed_Type.__name__ = "Integer32"
_WfRcmdsRshdKerberosSessionTypeAllowed_Object = MibScalar
wfRcmdsRshdKerberosSessionTypeAllowed = _WfRcmdsRshdKerberosSessionTypeAllowed_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 3, 8),
    _WfRcmdsRshdKerberosSessionTypeAllowed_Type()
)
wfRcmdsRshdKerberosSessionTypeAllowed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRcmdsRshdKerberosSessionTypeAllowed.setStatus("mandatory")


class _WfRcmdsRshdRcpDefaultVolume_Type(Integer32):
    """Custom type wfRcmdsRshdRcpDefaultVolume based on Integer32"""
    defaultValue = 2

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
              65)
        )
    )
    namedValues = NamedValues(
        *(("volume1", 1),
          ("volume10", 10),
          ("volume11", 11),
          ("volume12", 12),
          ("volume13", 13),
          ("volume14", 14),
          ("volume2", 2),
          ("volume3", 3),
          ("volume4", 4),
          ("volume5", 5),
          ("volume6", 6),
          ("volume7", 7),
          ("volume8", 8),
          ("volume9", 9),
          ("volumea", 65))
    )


_WfRcmdsRshdRcpDefaultVolume_Type.__name__ = "Integer32"
_WfRcmdsRshdRcpDefaultVolume_Object = MibScalar
wfRcmdsRshdRcpDefaultVolume = _WfRcmdsRshdRcpDefaultVolume_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 18, 3, 9),
    _WfRcmdsRshdRcpDefaultVolume_Type()
)
wfRcmdsRshdRcpDefaultVolume.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRcmdsRshdRcpDefaultVolume.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BayNetworks-RCMDS-MIB",
    **{"wfRcmds": wfRcmds,
       "wfRcmdsDelete": wfRcmdsDelete,
       "wfRcmdsDisable": wfRcmdsDisable,
       "wfRcmdsReservedPort": wfRcmdsReservedPort,
       "wfRcmdsKerberosDefaultRealmName": wfRcmdsKerberosDefaultRealmName,
       "wfRcmdsKerberosKDCName": wfRcmdsKerberosKDCName,
       "wfRcmdsRouterHostName": wfRcmdsRouterHostName,
       "wfRcmdsKerberosHostServiceKey": wfRcmdsKerberosHostServiceKey,
       "wfRcmdsRlogind": wfRcmdsRlogind,
       "wfRcmdsRlogindDelete": wfRcmdsRlogindDelete,
       "wfRcmdsRlogindDisable": wfRcmdsRlogindDisable,
       "wfRcmdsRlogindState": wfRcmdsRlogindState,
       "wfRcmdsRlogindMoreDisable": wfRcmdsRlogindMoreDisable,
       "wfRcmdsRlogindPrompt": wfRcmdsRlogindPrompt,
       "wfRcmdsRlogindLoginTimeOut": wfRcmdsRlogindLoginTimeOut,
       "wfRcmdsRlogindPasswordTimeOut": wfRcmdsRlogindPasswordTimeOut,
       "wfRcmdsRlogindCommandTimeOut": wfRcmdsRlogindCommandTimeOut,
       "wfRcmdsRlogindLoginRetries": wfRcmdsRlogindLoginRetries,
       "wfRcmdsRlogindTotalLogins": wfRcmdsRlogindTotalLogins,
       "wfRcmdsRlogindUserLoginErrors": wfRcmdsRlogindUserLoginErrors,
       "wfRcmdsRlogindManagerLoginErrors": wfRcmdsRlogindManagerLoginErrors,
       "wfRcmdsRlogindOtherLoginErrors": wfRcmdsRlogindOtherLoginErrors,
       "wfRcmdsRlogindActiveSessions": wfRcmdsRlogindActiveSessions,
       "wfRcmdsRlogindManagerAutoScript": wfRcmdsRlogindManagerAutoScript,
       "wfRcmdsRlogindUserAutoScript": wfRcmdsRlogindUserAutoScript,
       "wfRcmdsRlogindUserAbortLogoutDisable": wfRcmdsRlogindUserAbortLogoutDisable,
       "wfRcmdsRlogindHistoryDepth": wfRcmdsRlogindHistoryDepth,
       "wfRcmdsRlogindTcpPort": wfRcmdsRlogindTcpPort,
       "wfRcmdsRlogindTrustedHostAuthentication": wfRcmdsRlogindTrustedHostAuthentication,
       "wfRcmdsRlogindKerberosAuthentication": wfRcmdsRlogindKerberosAuthentication,
       "wfRcmdsRlogindKerberosSessionTypeAllowed": wfRcmdsRlogindKerberosSessionTypeAllowed,
       "wfRcmdsRshd": wfRcmdsRshd,
       "wfRcmdsRshdDelete": wfRcmdsRshdDelete,
       "wfRcmdsRshdDisable": wfRcmdsRshdDisable,
       "wfRcmdsRshdState": wfRcmdsRshdState,
       "wfRcmdsRshdTotalSessions": wfRcmdsRshdTotalSessions,
       "wfRcmdsRshdTcpPort": wfRcmdsRshdTcpPort,
       "wfRcmdsRshdTrustedHostAuthentication": wfRcmdsRshdTrustedHostAuthentication,
       "wfRcmdsRshdKerberosAuthentication": wfRcmdsRshdKerberosAuthentication,
       "wfRcmdsRshdKerberosSessionTypeAllowed": wfRcmdsRshdKerberosSessionTypeAllowed,
       "wfRcmdsRshdRcpDefaultVolume": wfRcmdsRshdRcpDefaultVolume}
)
