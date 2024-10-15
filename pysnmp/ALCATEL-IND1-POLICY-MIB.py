# SNMP MIB module (ALCATEL-IND1-POLICY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://asn1/ALCATEL-IND1-POLICY-MIB
# Produced by pysmi-1.5.4 at Tue Oct 15 00:45:20 2024
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

(softentIND1Policy,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1Policy")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

alcatelIND1PolicyMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 14, 1)
)
alcatelIND1PolicyMIB.setRevisions(
        ("2010-05-13 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PolicyEventCodes(Integer32, TextualConvention):
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
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58)
        )
    )
    namedValues = NamedValues(
        *(("pyEvent48", 48),
          ("pyEvent49", 49),
          ("pyEvent50", 50),
          ("pyEvent51", 51),
          ("pyEvent52", 52),
          ("pyEvent53", 53),
          ("pyEvent54", 54),
          ("pyEvent55", 55),
          ("pyEvent56", 56),
          ("pyEvent57", 57),
          ("pyEventDebugMemoryAlloc", 21),
          ("pyEventDebugMemoryFree", 22),
          ("pyEventDispositionError", 45),
          ("pyEventInitLog", 1),
          ("pyEventInternalCodeError", 18),
          ("pyEventLdapInit", 2),
          ("pyEventLdapReferenceIPFilter", 35),
          ("pyEventLdapReferencePVP", 17),
          ("pyEventLdapReferenceTP", 16),
          ("pyEventLdapReferenceXYLAN", 20),
          ("pyEventLdapSearch", 3),
          ("pyEventLdapSelectError", 19),
          ("pyEventLdapServerDefined", 24),
          ("pyEventLdapServerDeleted", 27),
          ("pyEventLdapSetOption", 39),
          ("pyEventLdapSyntaxDPort", 15),
          ("pyEventLdapSyntaxDestAddr", 7),
          ("pyEventLdapSyntaxDestMACAddr", 26),
          ("pyEventLdapSyntaxInDSByte", 8),
          ("pyEventLdapSyntaxPVPDoW", 11),
          ("pyEventLdapSyntaxPVPMonth", 10),
          ("pyEventLdapSyntaxPVPTime", 13),
          ("pyEventLdapSyntaxPVPToD", 12),
          ("pyEventLdapSyntaxRecDSByte", 9),
          ("pyEventLdapSyntaxSPort", 14),
          ("pyEventLdapSyntaxSourceAddr", 6),
          ("pyEventLdapSyntaxSourceMACAddr", 25),
          ("pyEventLdapSyntaxTOSByte", 36),
          ("pyEventLdapTLSChannelInit", 40),
          ("pyEventLdapTLSParametersOK", 41),
          ("pyEventMaxPolicyCountReached", 42),
          ("pyEventMemoryError", 43),
          ("pyEventMonitorSocketError", 44),
          ("pyEventNameLengthError", 46),
          ("pyEventOptimizedPvpDoW", 29),
          ("pyEventOptimizedPvpMonth", 28),
          ("pyEventPolicyCacheFlushed", 23),
          ("pyEventPolicyCacheLoaded", 58),
          ("pyEventPolicyWillNeverBeValid", 38),
          ("pyEventRuleActivated", 33),
          ("pyEventRuleDeactivated", 34),
          ("pyEventRuleScope", 32),
          ("pyEventServerStateChange", 5),
          ("pyEventTableResize", 47),
          ("pyEventTimeChangeDetected", 37),
          ("pyEventTooManyRequests", 4),
          ("pyEventZeroPvpDoW", 31),
          ("pyEventZeroPvpMonth", 30))
    )



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1PolicyMIBNotifications_ObjectIdentity = ObjectIdentity
alcatelIND1PolicyMIBNotifications = _AlcatelIND1PolicyMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 14, 1, 0)
)
if mibBuilder.loadTexts:
    alcatelIND1PolicyMIBNotifications.setStatus("current")
_AlcatelIND1PolicyMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1PolicyMIBObjects = _AlcatelIND1PolicyMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 14, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1PolicyMIBObjects.setStatus("current")


class _ServerPolicyDecision_Type(Integer32):
    """Custom type serverPolicyDecision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flushPolicies", 0),
          ("recachePolicies", 1),
          ("recacheQMMACGroup", 2))
    )


_ServerPolicyDecision_Type.__name__ = "Integer32"
_ServerPolicyDecision_Object = MibScalar
serverPolicyDecision = _ServerPolicyDecision_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 14, 1, 1, 1),
    _ServerPolicyDecision_Type()
)
serverPolicyDecision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serverPolicyDecision.setStatus("current")


class _RsvpDefaultPolicy_Type(Integer32):
    """Custom type rsvpDefaultPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("deny", 2))
    )


_RsvpDefaultPolicy_Type.__name__ = "Integer32"
_RsvpDefaultPolicy_Object = MibScalar
rsvpDefaultPolicy = _RsvpDefaultPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 14, 1, 1, 2),
    _RsvpDefaultPolicy_Type()
)
rsvpDefaultPolicy.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rsvpDefaultPolicy.setStatus("deprecated")


class _PolicyManagerEventTableSize_Type(Integer32):
    """Custom type policyManagerEventTableSize based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PolicyManagerEventTableSize_Type.__name__ = "Integer32"
_PolicyManagerEventTableSize_Object = MibScalar
policyManagerEventTableSize = _PolicyManagerEventTableSize_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 14, 1, 1, 3),
    _PolicyManagerEventTableSize_Type()
)
policyManagerEventTableSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    policyManagerEventTableSize.setStatus("current")
_DirectoryServerTable_Object = MibTable
directoryServerTable = _DirectoryServerTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 14, 1, 1, 4)
)
if mibBuilder.loadTexts:
    directoryServerTable.setStatus("current")
_DirectoryServerEntry_Object = MibTableRow
directoryServerEntry = _DirectoryServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 14, 1, 1, 4, 1)
)
directoryServerEntry.setIndexNames(
    (0, "ALCATEL-IND1-POLICY-MIB", "directoryServerAddress"),
    (0, "ALCATEL-IND1-POLICY-MIB", "directoryServerPort"),
)
if mibBuilder.loadTexts:
    directoryServerEntry.setStatus("current")
_DirectoryServerAddress_Type = IpAddress
_DirectoryServerAddress_Object = MibTableColumn
directoryServerAddress = _DirectoryServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 14, 1, 1, 4, 1, 1),
    _DirectoryServerAddress_Type()
)
directoryServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    directoryServerAddress.setStatus("current")


class _DirectoryServerPort_Type(Integer32):
    """Custom type directoryServerPort based on Integer32"""
    defaultValue = 389

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DirectoryServerPort_Type.__name__ = "Integer32"
_DirectoryServerPort_Object = MibTableColumn
directoryServerPort = _DirectoryServerPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 14, 1, 1, 4, 1, 2),
    _DirectoryServerPort_Type()
)
directoryServerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    directoryServerPort.setStatus("current")


class _DirectoryServerPreference_Type(Integer32):
    """Custom type directoryServerPreference based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DirectoryServerPreference_Type.__name__ = "Integer32"
_DirectoryServerPreference_Object = MibTableColumn
directoryServerPreference = _DirectoryServerPreference_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 14, 1, 1, 4, 1, 3),
    _DirectoryServerPreference_Type()
)
directoryServerPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    directoryServerPreference.setStatus("current")


class _DirectoryServerAuthenticationType_Type(Integer32):
    """Custom type directoryServerAuthenticationType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("simplePassword", 1))
    )


_DirectoryServerAuthenticationType_Type.__name__ = "Integer32"
_DirectoryServerAuthenticationType_Object = MibTableColumn
directoryServerAuthenticationType = _DirectoryServerAuthenticationType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 14, 1, 1, 4, 1, 4),
    _DirectoryServerAuthenticationType_Type()
)
directoryServerAuthenticationType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    directoryServerAuthenticationType.setStatus("current")


class _DirectoryServerUserId_Type(SnmpAdminString):
    """Custom type directoryServerUserId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_DirectoryServerUserId_Type.__name__ = "SnmpAdminString"
_DirectoryServerUserId_Object = MibTableColumn
directoryServerUserId = _DirectoryServerUserId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 14, 1, 1, 4, 1, 5),
    _DirectoryServerUserId_Type()
)
directoryServerUserId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    directoryServerUserId.setStatus("current")


class _DirectoryServerPassword_Type(SnmpAdminString):
    """Custom type directoryServerPassword based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_DirectoryServerPassword_Type.__name__ = "SnmpAdminString"
_DirectoryServerPassword_Object = MibTableColumn
directoryServerPassword = _DirectoryServerPassword_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 14, 1, 1, 4, 1, 6),
    _DirectoryServerPassword_Type()
)
directoryServerPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    directoryServerPassword.setStatus("current")


class _DirectoryServerSearchbase_Type(SnmpAdminString):
    """Custom type directoryServerSearchbase based on SnmpAdminString"""
    defaultValue = OctetString("o=Alcatel IND, c=US")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_DirectoryServerSearchbase_Type.__name__ = "SnmpAdminString"
_DirectoryServerSearchbase_Object = MibTableColumn
directoryServerSearchbase = _DirectoryServerSearchbase_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 14, 1, 1, 4, 1, 7),
    _DirectoryServerSearchbase_Type()
)
directoryServerSearchbase.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    directoryServerSearchbase.setStatus("current")


class _DirectoryServerCacheChange_Type(Integer32):
    """Custom type directoryServerCacheChange based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("recachePolicy", 1))
    )


_DirectoryServerCacheChange_Type.__name__ = "Integer32"
_DirectoryServerCacheChange_Object = MibTableColumn
directoryServerCacheChange = _DirectoryServerCacheChange_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 14, 1, 1, 4, 1, 8),
    _DirectoryServerCacheChange_Type()
)
directoryServerCacheChange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    directoryServerCacheChange.setStatus("current")
_DirectoryServerLastChange_Type = TimeTicks
_DirectoryServerLastChange_Object = MibTableColumn
directoryServerLastChange = _DirectoryServerLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 14, 1, 1, 4, 1, 9),
    _DirectoryServerLastChange_Type()
)
directoryServerLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    directoryServerLastChange.setStatus("current")


class _DirectoryServerAdminStatus_Type(Integer32):
    """Custom type directoryServerAdminStatus based on Integer32"""
    defaultValue = 1

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


_DirectoryServerAdminStatus_Type.__name__ = "Integer32"
_DirectoryServerAdminStatus_Object = MibTableColumn
directoryServerAdminStatus = _DirectoryServerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 14, 1, 1, 4, 1, 10),
    _DirectoryServerAdminStatus_Type()
)
directoryServerAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    directoryServerAdminStatus.setStatus("current")


class _DirectoryServerOperStatus_Type(Integer32):
    """Custom type directoryServerOperStatus based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("unknown", 3),
          ("up", 1))
    )


_DirectoryServerOperStatus_Type.__name__ = "Integer32"
_DirectoryServerOperStatus_Object = MibTableColumn
directoryServerOperStatus = _DirectoryServerOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 14, 1, 1, 4, 1, 11),
    _DirectoryServerOperStatus_Type()
)
directoryServerOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    directoryServerOperStatus.setStatus("current")


class _DirectoryServerRowStatus_Type(RowStatus):
    """Custom type directoryServerRowStatus based on RowStatus"""


_DirectoryServerRowStatus_Object = MibTableColumn
directoryServerRowStatus = _DirectoryServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 14, 1, 1, 4, 1, 12),
    _DirectoryServerRowStatus_Type()
)
directoryServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    directoryServerRowStatus.setStatus("current")


class _DirectoryServerEnableSSL_Type(Integer32):
    """Custom type directoryServerEnableSSL based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disableSSL", 0),
          ("enableSSL", 1))
    )


_DirectoryServerEnableSSL_Type.__name__ = "Integer32"
_DirectoryServerEnableSSL_Object = MibTableColumn
directoryServerEnableSSL = _DirectoryServerEnableSSL_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 14, 1, 1, 4, 1, 13),
    _DirectoryServerEnableSSL_Type()
)
directoryServerEnableSSL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    directoryServerEnableSSL.setStatus("current")
_PolicyEventTable_Object = MibTable
policyEventTable = _PolicyEventTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 14, 1, 1, 5)
)
if mibBuilder.loadTexts:
    policyEventTable.setStatus("current")
_PolicyEventEntry_Object = MibTableRow
policyEventEntry = _PolicyEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 14, 1, 1, 5, 1)
)
policyEventEntry.setIndexNames(
    (0, "ALCATEL-IND1-POLICY-MIB", "policyEventIndex"),
)
if mibBuilder.loadTexts:
    policyEventEntry.setStatus("current")


class _PolicyEventIndex_Type(Integer32):
    """Custom type policyEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_PolicyEventIndex_Type.__name__ = "Integer32"
_PolicyEventIndex_Object = MibTableColumn
policyEventIndex = _PolicyEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 14, 1, 1, 5, 1, 1),
    _PolicyEventIndex_Type()
)
policyEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyEventIndex.setStatus("current")
_PolicyEventCode_Type = PolicyEventCodes
_PolicyEventCode_Object = MibTableColumn
policyEventCode = _PolicyEventCode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 14, 1, 1, 5, 1, 2),
    _PolicyEventCode_Type()
)
policyEventCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyEventCode.setStatus("current")


class _PolicyEventDetailString_Type(SnmpAdminString):
    """Custom type policyEventDetailString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PolicyEventDetailString_Type.__name__ = "SnmpAdminString"
_PolicyEventDetailString_Object = MibTableColumn
policyEventDetailString = _PolicyEventDetailString_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 14, 1, 1, 5, 1, 3),
    _PolicyEventDetailString_Type()
)
policyEventDetailString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyEventDetailString.setStatus("current")
_PolicyEventTime_Type = TimeTicks
_PolicyEventTime_Object = MibTableColumn
policyEventTime = _PolicyEventTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 14, 1, 1, 5, 1, 4),
    _PolicyEventTime_Type()
)
policyEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyEventTime.setStatus("current")
_PolicyRuleNamesTable_Object = MibTable
policyRuleNamesTable = _PolicyRuleNamesTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 14, 1, 1, 6)
)
if mibBuilder.loadTexts:
    policyRuleNamesTable.setStatus("current")
_PolicyRuleNamesEntry_Object = MibTableRow
policyRuleNamesEntry = _PolicyRuleNamesEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 14, 1, 1, 6, 1)
)
policyRuleNamesEntry.setIndexNames(
    (0, "ALCATEL-IND1-POLICY-MIB", "policyRuleNamesIndex"),
)
if mibBuilder.loadTexts:
    policyRuleNamesEntry.setStatus("current")


class _PolicyRuleNamesIndex_Type(Integer32):
    """Custom type policyRuleNamesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PolicyRuleNamesIndex_Type.__name__ = "Integer32"
_PolicyRuleNamesIndex_Object = MibTableColumn
policyRuleNamesIndex = _PolicyRuleNamesIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 14, 1, 1, 6, 1, 1),
    _PolicyRuleNamesIndex_Type()
)
policyRuleNamesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyRuleNamesIndex.setStatus("current")


class _PolicyRuleNamesName_Type(SnmpAdminString):
    """Custom type policyRuleNamesName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PolicyRuleNamesName_Type.__name__ = "SnmpAdminString"
_PolicyRuleNamesName_Object = MibTableColumn
policyRuleNamesName = _PolicyRuleNamesName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 14, 1, 1, 6, 1, 2),
    _PolicyRuleNamesName_Type()
)
policyRuleNamesName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyRuleNamesName.setStatus("current")


class _PolicyRuleNamesRowStatus_Type(RowStatus):
    """Custom type policyRuleNamesRowStatus based on RowStatus"""


_PolicyRuleNamesRowStatus_Object = MibTableColumn
policyRuleNamesRowStatus = _PolicyRuleNamesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 14, 1, 1, 6, 1, 3),
    _PolicyRuleNamesRowStatus_Type()
)
policyRuleNamesRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyRuleNamesRowStatus.setStatus("current")


class _PolicyRuleOperStatus_Type(Integer32):
    """Custom type policyRuleOperStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("notReady", 3),
          ("up", 1))
    )


_PolicyRuleOperStatus_Type.__name__ = "Integer32"
_PolicyRuleOperStatus_Object = MibTableColumn
policyRuleOperStatus = _PolicyRuleOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 14, 1, 1, 6, 1, 4),
    _PolicyRuleOperStatus_Type()
)
policyRuleOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyRuleOperStatus.setStatus("current")
_PolicyStatsTable_Object = MibTable
policyStatsTable = _PolicyStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 14, 1, 1, 7)
)
if mibBuilder.loadTexts:
    policyStatsTable.setStatus("current")
_PolicyStatsEntry_Object = MibTableRow
policyStatsEntry = _PolicyStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 14, 1, 1, 7, 1)
)
policyStatsEntry.setIndexNames(
    (0, "ALCATEL-IND1-POLICY-MIB", "policyStatsAddress"),
    (0, "ALCATEL-IND1-POLICY-MIB", "policyStatsServerPort"),
)
if mibBuilder.loadTexts:
    policyStatsEntry.setStatus("current")
_PolicyStatsAddress_Type = IpAddress
_PolicyStatsAddress_Object = MibTableColumn
policyStatsAddress = _PolicyStatsAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 14, 1, 1, 7, 1, 1),
    _PolicyStatsAddress_Type()
)
policyStatsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyStatsAddress.setStatus("current")


class _PolicyStatsServerPort_Type(Integer32):
    """Custom type policyStatsServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PolicyStatsServerPort_Type.__name__ = "Integer32"
_PolicyStatsServerPort_Object = MibTableColumn
policyStatsServerPort = _PolicyStatsServerPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 14, 1, 1, 7, 1, 2),
    _PolicyStatsServerPort_Type()
)
policyStatsServerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyStatsServerPort.setStatus("current")
_PolicyStatsQueryCount_Type = Counter32
_PolicyStatsQueryCount_Object = MibTableColumn
policyStatsQueryCount = _PolicyStatsQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 14, 1, 1, 7, 1, 3),
    _PolicyStatsQueryCount_Type()
)
policyStatsQueryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyStatsQueryCount.setStatus("current")
_PolicyStatsAccessCount_Type = Counter32
_PolicyStatsAccessCount_Object = MibTableColumn
policyStatsAccessCount = _PolicyStatsAccessCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 14, 1, 1, 7, 1, 4),
    _PolicyStatsAccessCount_Type()
)
policyStatsAccessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyStatsAccessCount.setStatus("current")
_PolicyStatsSuccessAccessCount_Type = Counter32
_PolicyStatsSuccessAccessCount_Object = MibTableColumn
policyStatsSuccessAccessCount = _PolicyStatsSuccessAccessCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 14, 1, 1, 7, 1, 5),
    _PolicyStatsSuccessAccessCount_Type()
)
policyStatsSuccessAccessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyStatsSuccessAccessCount.setStatus("current")
_PolicyStatsNotFoundCount_Type = Counter32
_PolicyStatsNotFoundCount_Object = MibTableColumn
policyStatsNotFoundCount = _PolicyStatsNotFoundCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 14, 1, 1, 7, 1, 6),
    _PolicyStatsNotFoundCount_Type()
)
policyStatsNotFoundCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyStatsNotFoundCount.setStatus("current")
_PolicyNotificationTable_Object = MibTable
policyNotificationTable = _PolicyNotificationTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 14, 1, 1, 8)
)
if mibBuilder.loadTexts:
    policyNotificationTable.setStatus("current")
_PolicyNotificationEntry_Object = MibTableRow
policyNotificationEntry = _PolicyNotificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 14, 1, 1, 8, 1)
)
policyNotificationEntry.setIndexNames(
    (0, "ALCATEL-IND1-POLICY-MIB", "policyNotificationIndex"),
)
if mibBuilder.loadTexts:
    policyNotificationEntry.setStatus("current")
_PolicyNotificationIndex_Type = PolicyEventCodes
_PolicyNotificationIndex_Object = MibTableColumn
policyNotificationIndex = _PolicyNotificationIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 14, 1, 1, 8, 1, 1),
    _PolicyNotificationIndex_Type()
)
policyNotificationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyNotificationIndex.setStatus("current")


class _PolicyNotificationCode_Type(Integer32):
    """Custom type policyNotificationCode based on Integer32"""
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
        *(("logAndTrap", 3),
          ("noNotification", 0),
          ("sendTrap", 2),
          ("writeToLog", 1))
    )


_PolicyNotificationCode_Type.__name__ = "Integer32"
_PolicyNotificationCode_Object = MibTableColumn
policyNotificationCode = _PolicyNotificationCode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 14, 1, 1, 8, 1, 2),
    _PolicyNotificationCode_Type()
)
policyNotificationCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    policyNotificationCode.setStatus("current")
_PolicyEventCount_Type = Counter32
_PolicyEventCount_Object = MibTableColumn
policyEventCount = _PolicyEventCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 14, 1, 1, 8, 1, 3),
    _PolicyEventCount_Type()
)
policyEventCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyEventCount.setStatus("current")


class _PolicyManagerSwitchIdentifier_Type(SnmpAdminString):
    """Custom type policyManagerSwitchIdentifier based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_PolicyManagerSwitchIdentifier_Type.__name__ = "SnmpAdminString"
_PolicyManagerSwitchIdentifier_Object = MibScalar
policyManagerSwitchIdentifier = _PolicyManagerSwitchIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 14, 1, 1, 9),
    _PolicyManagerSwitchIdentifier_Type()
)
policyManagerSwitchIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    policyManagerSwitchIdentifier.setStatus("current")
_PolicyManagerTrapObjs_ObjectIdentity = ObjectIdentity
policyManagerTrapObjs = _PolicyManagerTrapObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 14, 1, 1, 10)
)


class _PolicyTrapEventDetailString_Type(SnmpAdminString):
    """Custom type policyTrapEventDetailString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PolicyTrapEventDetailString_Type.__name__ = "SnmpAdminString"
_PolicyTrapEventDetailString_Object = MibScalar
policyTrapEventDetailString = _PolicyTrapEventDetailString_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 14, 1, 1, 10, 1),
    _PolicyTrapEventDetailString_Type()
)
policyTrapEventDetailString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyTrapEventDetailString.setStatus("current")
_PolicyTrapEventCode_Type = PolicyEventCodes
_PolicyTrapEventCode_Object = MibScalar
policyTrapEventCode = _PolicyTrapEventCode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 14, 1, 1, 10, 2),
    _PolicyTrapEventCode_Type()
)
policyTrapEventCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    policyTrapEventCode.setStatus("current")
_AlcatelIND1PolicyMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1PolicyMIBConformance = _AlcatelIND1PolicyMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 14, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1PolicyMIBConformance.setStatus("current")
_AlcatelIND1PolicyMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1PolicyMIBGroups = _AlcatelIND1PolicyMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 14, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1PolicyMIBGroups.setStatus("current")
_AlcatelIND1PolicyMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1PolicyMIBCompliances = _AlcatelIND1PolicyMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 14, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1PolicyMIBCompliances.setStatus("current")

# Managed Objects groups

policyMIBGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 14, 1, 2, 1, 1)
)
policyMIBGlobalGroup.setObjects(
      *(("ALCATEL-IND1-POLICY-MIB", "serverPolicyDecision"),
        ("ALCATEL-IND1-POLICY-MIB", "policyManagerEventTableSize"),
        ("ALCATEL-IND1-POLICY-MIB", "policyManagerSwitchIdentifier"))
)
if mibBuilder.loadTexts:
    policyMIBGlobalGroup.setStatus("current")

policyMIBDirectoryServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 14, 1, 2, 1, 2)
)
policyMIBDirectoryServerGroup.setObjects(
      *(("ALCATEL-IND1-POLICY-MIB", "directoryServerAddress"),
        ("ALCATEL-IND1-POLICY-MIB", "directoryServerPort"),
        ("ALCATEL-IND1-POLICY-MIB", "directoryServerPreference"),
        ("ALCATEL-IND1-POLICY-MIB", "directoryServerAuthenticationType"),
        ("ALCATEL-IND1-POLICY-MIB", "directoryServerUserId"),
        ("ALCATEL-IND1-POLICY-MIB", "directoryServerPassword"),
        ("ALCATEL-IND1-POLICY-MIB", "directoryServerSearchbase"),
        ("ALCATEL-IND1-POLICY-MIB", "directoryServerCacheChange"),
        ("ALCATEL-IND1-POLICY-MIB", "directoryServerLastChange"),
        ("ALCATEL-IND1-POLICY-MIB", "directoryServerAdminStatus"),
        ("ALCATEL-IND1-POLICY-MIB", "directoryServerOperStatus"),
        ("ALCATEL-IND1-POLICY-MIB", "directoryServerRowStatus"),
        ("ALCATEL-IND1-POLICY-MIB", "directoryServerEnableSSL"))
)
if mibBuilder.loadTexts:
    policyMIBDirectoryServerGroup.setStatus("current")

policyMIBEventTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 14, 1, 2, 1, 3)
)
policyMIBEventTableGroup.setObjects(
      *(("ALCATEL-IND1-POLICY-MIB", "policyEventIndex"),
        ("ALCATEL-IND1-POLICY-MIB", "policyEventCode"),
        ("ALCATEL-IND1-POLICY-MIB", "policyEventDetailString"),
        ("ALCATEL-IND1-POLICY-MIB", "policyEventTime"))
)
if mibBuilder.loadTexts:
    policyMIBEventTableGroup.setStatus("current")

policyMIBRuleNamesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 14, 1, 2, 1, 4)
)
policyMIBRuleNamesGroup.setObjects(
      *(("ALCATEL-IND1-POLICY-MIB", "policyRuleNamesIndex"),
        ("ALCATEL-IND1-POLICY-MIB", "policyRuleNamesName"),
        ("ALCATEL-IND1-POLICY-MIB", "policyRuleNamesRowStatus"),
        ("ALCATEL-IND1-POLICY-MIB", "policyRuleOperStatus"))
)
if mibBuilder.loadTexts:
    policyMIBRuleNamesGroup.setStatus("current")

policyMIBStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 14, 1, 2, 1, 5)
)
policyMIBStatsGroup.setObjects(
      *(("ALCATEL-IND1-POLICY-MIB", "policyStatsAddress"),
        ("ALCATEL-IND1-POLICY-MIB", "policyStatsServerPort"),
        ("ALCATEL-IND1-POLICY-MIB", "policyStatsAccessCount"),
        ("ALCATEL-IND1-POLICY-MIB", "policyStatsSuccessAccessCount"),
        ("ALCATEL-IND1-POLICY-MIB", "policyStatsNotFoundCount"),
        ("ALCATEL-IND1-POLICY-MIB", "policyStatsQueryCount"))
)
if mibBuilder.loadTexts:
    policyMIBStatsGroup.setStatus("current")

policyMIBNotificationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 14, 1, 2, 1, 6)
)
policyMIBNotificationGroup.setObjects(
      *(("ALCATEL-IND1-POLICY-MIB", "policyNotificationIndex"),
        ("ALCATEL-IND1-POLICY-MIB", "policyNotificationCode"),
        ("ALCATEL-IND1-POLICY-MIB", "policyEventCount"),
        ("ALCATEL-IND1-POLICY-MIB", "policyTrapEventDetailString"),
        ("ALCATEL-IND1-POLICY-MIB", "policyTrapEventCode"))
)
if mibBuilder.loadTexts:
    policyMIBNotificationGroup.setStatus("current")

policyMIBTrapEventGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 14, 1, 2, 1, 7)
)
policyMIBTrapEventGroup.setObjects(
      *(("ALCATEL-IND1-POLICY-MIB", "policyTrapEventDetailString"),
        ("ALCATEL-IND1-POLICY-MIB", "policyTrapEventCode"))
)
if mibBuilder.loadTexts:
    policyMIBTrapEventGroup.setStatus("current")


# Notification objects

policyEventNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 14, 1, 0, 1)
)
policyEventNotification.setObjects(
      *(("ALCATEL-IND1-POLICY-MIB", "policyTrapEventDetailString"),
        ("ALCATEL-IND1-POLICY-MIB", "policyTrapEventCode"))
)
if mibBuilder.loadTexts:
    policyEventNotification.setStatus(
        "current"
    )


# Notifications groups

policyMIBTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 14, 1, 2, 1, 8)
)
policyMIBTrapsGroup.setObjects(
    ("ALCATEL-IND1-POLICY-MIB", "policyEventNotification")
)
if mibBuilder.loadTexts:
    policyMIBTrapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alcatelIND1PolicyMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 14, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1PolicyMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-POLICY-MIB",
    **{"PolicyEventCodes": PolicyEventCodes,
       "alcatelIND1PolicyMIB": alcatelIND1PolicyMIB,
       "alcatelIND1PolicyMIBNotifications": alcatelIND1PolicyMIBNotifications,
       "policyEventNotification": policyEventNotification,
       "alcatelIND1PolicyMIBObjects": alcatelIND1PolicyMIBObjects,
       "serverPolicyDecision": serverPolicyDecision,
       "rsvpDefaultPolicy": rsvpDefaultPolicy,
       "policyManagerEventTableSize": policyManagerEventTableSize,
       "directoryServerTable": directoryServerTable,
       "directoryServerEntry": directoryServerEntry,
       "directoryServerAddress": directoryServerAddress,
       "directoryServerPort": directoryServerPort,
       "directoryServerPreference": directoryServerPreference,
       "directoryServerAuthenticationType": directoryServerAuthenticationType,
       "directoryServerUserId": directoryServerUserId,
       "directoryServerPassword": directoryServerPassword,
       "directoryServerSearchbase": directoryServerSearchbase,
       "directoryServerCacheChange": directoryServerCacheChange,
       "directoryServerLastChange": directoryServerLastChange,
       "directoryServerAdminStatus": directoryServerAdminStatus,
       "directoryServerOperStatus": directoryServerOperStatus,
       "directoryServerRowStatus": directoryServerRowStatus,
       "directoryServerEnableSSL": directoryServerEnableSSL,
       "policyEventTable": policyEventTable,
       "policyEventEntry": policyEventEntry,
       "policyEventIndex": policyEventIndex,
       "policyEventCode": policyEventCode,
       "policyEventDetailString": policyEventDetailString,
       "policyEventTime": policyEventTime,
       "policyRuleNamesTable": policyRuleNamesTable,
       "policyRuleNamesEntry": policyRuleNamesEntry,
       "policyRuleNamesIndex": policyRuleNamesIndex,
       "policyRuleNamesName": policyRuleNamesName,
       "policyRuleNamesRowStatus": policyRuleNamesRowStatus,
       "policyRuleOperStatus": policyRuleOperStatus,
       "policyStatsTable": policyStatsTable,
       "policyStatsEntry": policyStatsEntry,
       "policyStatsAddress": policyStatsAddress,
       "policyStatsServerPort": policyStatsServerPort,
       "policyStatsQueryCount": policyStatsQueryCount,
       "policyStatsAccessCount": policyStatsAccessCount,
       "policyStatsSuccessAccessCount": policyStatsSuccessAccessCount,
       "policyStatsNotFoundCount": policyStatsNotFoundCount,
       "policyNotificationTable": policyNotificationTable,
       "policyNotificationEntry": policyNotificationEntry,
       "policyNotificationIndex": policyNotificationIndex,
       "policyNotificationCode": policyNotificationCode,
       "policyEventCount": policyEventCount,
       "policyManagerSwitchIdentifier": policyManagerSwitchIdentifier,
       "policyManagerTrapObjs": policyManagerTrapObjs,
       "policyTrapEventDetailString": policyTrapEventDetailString,
       "policyTrapEventCode": policyTrapEventCode,
       "alcatelIND1PolicyMIBConformance": alcatelIND1PolicyMIBConformance,
       "alcatelIND1PolicyMIBGroups": alcatelIND1PolicyMIBGroups,
       "policyMIBGlobalGroup": policyMIBGlobalGroup,
       "policyMIBDirectoryServerGroup": policyMIBDirectoryServerGroup,
       "policyMIBEventTableGroup": policyMIBEventTableGroup,
       "policyMIBRuleNamesGroup": policyMIBRuleNamesGroup,
       "policyMIBStatsGroup": policyMIBStatsGroup,
       "policyMIBNotificationGroup": policyMIBNotificationGroup,
       "policyMIBTrapEventGroup": policyMIBTrapEventGroup,
       "policyMIBTrapsGroup": policyMIBTrapsGroup,
       "alcatelIND1PolicyMIBCompliances": alcatelIND1PolicyMIBCompliances,
       "alcatelIND1PolicyMIBCompliance": alcatelIND1PolicyMIBCompliance}
)
