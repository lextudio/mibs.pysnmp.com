# SNMP MIB module (Juniper-IKE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-IKE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:15:28 2024
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

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

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

juniIkeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71)
)
juniIkeMIB.setRevisions(
        ("2005-11-22 16:15",
         "2004-01-23 15:12",
         "2004-04-06 22:26")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JuniIkeAuthenticationMethod(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3)
        )
    )
    namedValues = NamedValues(
        *(("preSharedKeys", 3),
          ("rsaSignature", 0))
    )



class JuniIkeEncryptionMethod(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("des", 0),
          ("tripleDes", 1))
    )



class JuniIkeGroup(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("group1", 0),
          ("group2", 1),
          ("group5", 4))
    )



class JuniIkeHashMethod(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("md5", 0),
          ("sha", 1))
    )



class JuniIkeNegotiationMode(Integer32, TextualConvention):
    status = "obsolete"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("aggressive", 0),
          ("main", 1))
    )



class JuniIkeNegotiationV2Mode(Integer32, TextualConvention):
    status = "current"
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
        *(("aggressiveAccepted", 0),
          ("aggressiveNotAllowed", 3),
          ("aggressiveRequested", 1),
          ("aggressiveRequired", 2))
    )



class JuniIpsecPhase1SaState(Integer32, TextualConvention):
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
        *(("amDoneR", 13),
          ("amFinalI", 12),
          ("amSaI", 10),
          ("amSaR", 11),
          ("deleted", 26),
          ("done", 25),
          ("mmDoneI", 9),
          ("mmFinalI", 7),
          ("mmFinalR", 8),
          ("mmKeI", 5),
          ("mmKeR", 6),
          ("mmSaI", 3),
          ("mmSaR", 4),
          ("ngmDoneI", 24),
          ("ngmHashSaI", 22),
          ("ngmHashSaR", 23),
          ("qmDoneR", 19),
          ("qmHashI", 18),
          ("qmHashSaI", 16),
          ("qmHashSaR", 17),
          ("reserved", 0),
          ("startNgmI", 20),
          ("startNgmR", 21),
          ("startQmI", 14),
          ("startQmR", 15),
          ("startSaNegotiationI", 1),
          ("startSaNegotiationR", 2))
    )



class JuniIpsecPhase1SaDirection(Integer32, TextualConvention):
    status = "obsolete"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("initiator", 0),
          ("responder", 1))
    )



# MIB Managed Objects in the order of their OIDs

_JuniIkeObjects_ObjectIdentity = ObjectIdentity
juniIkeObjects = _JuniIkeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1)
)
_JuniIke_ObjectIdentity = ObjectIdentity
juniIke = _JuniIke_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1)
)
_JuniIkePolicyRuleTable_Object = MibTable
juniIkePolicyRuleTable = _JuniIkePolicyRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 1)
)
if mibBuilder.loadTexts:
    juniIkePolicyRuleTable.setStatus("obsolete")
_JuniIkePolicyRuleEntry_Object = MibTableRow
juniIkePolicyRuleEntry = _JuniIkePolicyRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 1, 1)
)
juniIkePolicyRuleEntry.setIndexNames(
    (0, "Juniper-IKE-MIB", "juniIkePolicyRulePriority"),
)
if mibBuilder.loadTexts:
    juniIkePolicyRuleEntry.setStatus("obsolete")


class _JuniIkePolicyRulePriority_Type(Integer32):
    """Custom type juniIkePolicyRulePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_JuniIkePolicyRulePriority_Type.__name__ = "Integer32"
_JuniIkePolicyRulePriority_Object = MibTableColumn
juniIkePolicyRulePriority = _JuniIkePolicyRulePriority_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 1, 1, 1),
    _JuniIkePolicyRulePriority_Type()
)
juniIkePolicyRulePriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIkePolicyRulePriority.setStatus("obsolete")


class _JuniIkePolicyRuleAuthMethod_Type(JuniIkeAuthenticationMethod):
    """Custom type juniIkePolicyRuleAuthMethod based on JuniIkeAuthenticationMethod"""


_JuniIkePolicyRuleAuthMethod_Object = MibTableColumn
juniIkePolicyRuleAuthMethod = _JuniIkePolicyRuleAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 1, 1, 2),
    _JuniIkePolicyRuleAuthMethod_Type()
)
juniIkePolicyRuleAuthMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIkePolicyRuleAuthMethod.setStatus("obsolete")


class _JuniIkePolicyRuleEncryptMethod_Type(JuniIkeEncryptionMethod):
    """Custom type juniIkePolicyRuleEncryptMethod based on JuniIkeEncryptionMethod"""


_JuniIkePolicyRuleEncryptMethod_Object = MibTableColumn
juniIkePolicyRuleEncryptMethod = _JuniIkePolicyRuleEncryptMethod_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 1, 1, 3),
    _JuniIkePolicyRuleEncryptMethod_Type()
)
juniIkePolicyRuleEncryptMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIkePolicyRuleEncryptMethod.setStatus("obsolete")


class _JuniIkePolicyRulePfsGroup_Type(JuniIkeGroup):
    """Custom type juniIkePolicyRulePfsGroup based on JuniIkeGroup"""


_JuniIkePolicyRulePfsGroup_Object = MibTableColumn
juniIkePolicyRulePfsGroup = _JuniIkePolicyRulePfsGroup_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 1, 1, 4),
    _JuniIkePolicyRulePfsGroup_Type()
)
juniIkePolicyRulePfsGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIkePolicyRulePfsGroup.setStatus("obsolete")


class _JuniIkePolicyRuleHashMethod_Type(JuniIkeHashMethod):
    """Custom type juniIkePolicyRuleHashMethod based on JuniIkeHashMethod"""


_JuniIkePolicyRuleHashMethod_Object = MibTableColumn
juniIkePolicyRuleHashMethod = _JuniIkePolicyRuleHashMethod_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 1, 1, 5),
    _JuniIkePolicyRuleHashMethod_Type()
)
juniIkePolicyRuleHashMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIkePolicyRuleHashMethod.setStatus("obsolete")


class _JuniIkePolicyRuleLifetime_Type(Integer32):
    """Custom type juniIkePolicyRuleLifetime based on Integer32"""
    defaultValue = 28800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_JuniIkePolicyRuleLifetime_Type.__name__ = "Integer32"
_JuniIkePolicyRuleLifetime_Object = MibTableColumn
juniIkePolicyRuleLifetime = _JuniIkePolicyRuleLifetime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 1, 1, 6),
    _JuniIkePolicyRuleLifetime_Type()
)
juniIkePolicyRuleLifetime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIkePolicyRuleLifetime.setStatus("obsolete")


class _JuniIkePolicyRuleNegotiationMode_Type(JuniIkeNegotiationMode):
    """Custom type juniIkePolicyRuleNegotiationMode based on JuniIkeNegotiationMode"""


_JuniIkePolicyRuleNegotiationMode_Object = MibTableColumn
juniIkePolicyRuleNegotiationMode = _JuniIkePolicyRuleNegotiationMode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 1, 1, 7),
    _JuniIkePolicyRuleNegotiationMode_Type()
)
juniIkePolicyRuleNegotiationMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIkePolicyRuleNegotiationMode.setStatus("obsolete")
_JuniIkePolicyRuleRowStatus_Type = RowStatus
_JuniIkePolicyRuleRowStatus_Object = MibTableColumn
juniIkePolicyRuleRowStatus = _JuniIkePolicyRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 1, 1, 8),
    _JuniIkePolicyRuleRowStatus_Type()
)
juniIkePolicyRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIkePolicyRuleRowStatus.setStatus("obsolete")
_JuniIkeIpv4PresharedKeyTable_Object = MibTable
juniIkeIpv4PresharedKeyTable = _JuniIkeIpv4PresharedKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 2)
)
if mibBuilder.loadTexts:
    juniIkeIpv4PresharedKeyTable.setStatus("current")
_JuniIkeIpv4PresharedKeyEntry_Object = MibTableRow
juniIkeIpv4PresharedKeyEntry = _JuniIkeIpv4PresharedKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 2, 1)
)
juniIkeIpv4PresharedKeyEntry.setIndexNames(
    (0, "Juniper-IKE-MIB", "juniIkeIpv4PresharedRemoteIpAddr"),
    (0, "Juniper-IKE-MIB", "juniIkeIpv4PresharedRouterIdx"),
)
if mibBuilder.loadTexts:
    juniIkeIpv4PresharedKeyEntry.setStatus("current")
_JuniIkeIpv4PresharedRemoteIpAddr_Type = IpAddress
_JuniIkeIpv4PresharedRemoteIpAddr_Object = MibTableColumn
juniIkeIpv4PresharedRemoteIpAddr = _JuniIkeIpv4PresharedRemoteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 2, 1, 1),
    _JuniIkeIpv4PresharedRemoteIpAddr_Type()
)
juniIkeIpv4PresharedRemoteIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIkeIpv4PresharedRemoteIpAddr.setStatus("current")
_JuniIkeIpv4PresharedRouterIdx_Type = Unsigned32
_JuniIkeIpv4PresharedRouterIdx_Object = MibTableColumn
juniIkeIpv4PresharedRouterIdx = _JuniIkeIpv4PresharedRouterIdx_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 2, 1, 2),
    _JuniIkeIpv4PresharedRouterIdx_Type()
)
juniIkeIpv4PresharedRouterIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIkeIpv4PresharedRouterIdx.setStatus("current")


class _JuniIkeIpv4PresharedKeyStr_Type(DisplayString):
    """Custom type juniIkeIpv4PresharedKeyStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_JuniIkeIpv4PresharedKeyStr_Type.__name__ = "DisplayString"
_JuniIkeIpv4PresharedKeyStr_Object = MibTableColumn
juniIkeIpv4PresharedKeyStr = _JuniIkeIpv4PresharedKeyStr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 2, 1, 3),
    _JuniIkeIpv4PresharedKeyStr_Type()
)
juniIkeIpv4PresharedKeyStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIkeIpv4PresharedKeyStr.setStatus("current")


class _JuniIkeIpv4PresharedMaskedKeyStr_Type(OctetString):
    """Custom type juniIkeIpv4PresharedMaskedKeyStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 300),
    )


_JuniIkeIpv4PresharedMaskedKeyStr_Type.__name__ = "OctetString"
_JuniIkeIpv4PresharedMaskedKeyStr_Object = MibTableColumn
juniIkeIpv4PresharedMaskedKeyStr = _JuniIkeIpv4PresharedMaskedKeyStr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 2, 1, 4),
    _JuniIkeIpv4PresharedMaskedKeyStr_Type()
)
juniIkeIpv4PresharedMaskedKeyStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIkeIpv4PresharedMaskedKeyStr.setStatus("current")
_JuniIkeIpv4PresharedKeyRowStatus_Type = RowStatus
_JuniIkeIpv4PresharedKeyRowStatus_Object = MibTableColumn
juniIkeIpv4PresharedKeyRowStatus = _JuniIkeIpv4PresharedKeyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 2, 1, 5),
    _JuniIkeIpv4PresharedKeyRowStatus_Type()
)
juniIkeIpv4PresharedKeyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIkeIpv4PresharedKeyRowStatus.setStatus("current")
_JuniIkeFqdnPresharedKeyTable_Object = MibTable
juniIkeFqdnPresharedKeyTable = _JuniIkeFqdnPresharedKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 3)
)
if mibBuilder.loadTexts:
    juniIkeFqdnPresharedKeyTable.setStatus("current")
_JuniIkeFqdnPresharedKeyEntry_Object = MibTableRow
juniIkeFqdnPresharedKeyEntry = _JuniIkeFqdnPresharedKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 3, 1)
)
juniIkeFqdnPresharedKeyEntry.setIndexNames(
    (0, "Juniper-IKE-MIB", "juniIkeFqdnPresharedRemote"),
    (0, "Juniper-IKE-MIB", "juniIkeFqdnPresharedRouterIndex"),
)
if mibBuilder.loadTexts:
    juniIkeFqdnPresharedKeyEntry.setStatus("current")


class _JuniIkeFqdnPresharedRemote_Type(DisplayString):
    """Custom type juniIkeFqdnPresharedRemote based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_JuniIkeFqdnPresharedRemote_Type.__name__ = "DisplayString"
_JuniIkeFqdnPresharedRemote_Object = MibTableColumn
juniIkeFqdnPresharedRemote = _JuniIkeFqdnPresharedRemote_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 3, 1, 1),
    _JuniIkeFqdnPresharedRemote_Type()
)
juniIkeFqdnPresharedRemote.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIkeFqdnPresharedRemote.setStatus("current")
_JuniIkeFqdnPresharedRouterIndex_Type = Unsigned32
_JuniIkeFqdnPresharedRouterIndex_Object = MibTableColumn
juniIkeFqdnPresharedRouterIndex = _JuniIkeFqdnPresharedRouterIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 3, 1, 2),
    _JuniIkeFqdnPresharedRouterIndex_Type()
)
juniIkeFqdnPresharedRouterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIkeFqdnPresharedRouterIndex.setStatus("current")


class _JuniIkeFqdnPresharedKeyStr_Type(DisplayString):
    """Custom type juniIkeFqdnPresharedKeyStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_JuniIkeFqdnPresharedKeyStr_Type.__name__ = "DisplayString"
_JuniIkeFqdnPresharedKeyStr_Object = MibTableColumn
juniIkeFqdnPresharedKeyStr = _JuniIkeFqdnPresharedKeyStr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 3, 1, 3),
    _JuniIkeFqdnPresharedKeyStr_Type()
)
juniIkeFqdnPresharedKeyStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIkeFqdnPresharedKeyStr.setStatus("current")


class _JuniIkeFqdnPresharedMaskedKeyStr_Type(OctetString):
    """Custom type juniIkeFqdnPresharedMaskedKeyStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 300),
    )


_JuniIkeFqdnPresharedMaskedKeyStr_Type.__name__ = "OctetString"
_JuniIkeFqdnPresharedMaskedKeyStr_Object = MibTableColumn
juniIkeFqdnPresharedMaskedKeyStr = _JuniIkeFqdnPresharedMaskedKeyStr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 3, 1, 4),
    _JuniIkeFqdnPresharedMaskedKeyStr_Type()
)
juniIkeFqdnPresharedMaskedKeyStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIkeFqdnPresharedMaskedKeyStr.setStatus("current")
_JuniIkeFqdnPresharedKeyRowStatus_Type = RowStatus
_JuniIkeFqdnPresharedKeyRowStatus_Object = MibTableColumn
juniIkeFqdnPresharedKeyRowStatus = _JuniIkeFqdnPresharedKeyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 3, 1, 5),
    _JuniIkeFqdnPresharedKeyRowStatus_Type()
)
juniIkeFqdnPresharedKeyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIkeFqdnPresharedKeyRowStatus.setStatus("current")
_JuniIkeSaTable_Object = MibTable
juniIkeSaTable = _JuniIkeSaTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 4)
)
if mibBuilder.loadTexts:
    juniIkeSaTable.setStatus("obsolete")
_JuniIkeSaEntry_Object = MibTableRow
juniIkeSaEntry = _JuniIkeSaEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 4, 1)
)
juniIkeSaEntry.setIndexNames(
    (0, "Juniper-IKE-MIB", "juniIkeSaRemoteIpAddr"),
    (0, "Juniper-IKE-MIB", "juniIkeSaLocalIpAddr"),
    (0, "Juniper-IKE-MIB", "juniIkeSaRouterIndex"),
    (0, "Juniper-IKE-MIB", "juniIkeSaDirection"),
)
if mibBuilder.loadTexts:
    juniIkeSaEntry.setStatus("obsolete")
_JuniIkeSaRemoteIpAddr_Type = IpAddress
_JuniIkeSaRemoteIpAddr_Object = MibTableColumn
juniIkeSaRemoteIpAddr = _JuniIkeSaRemoteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 4, 1, 1),
    _JuniIkeSaRemoteIpAddr_Type()
)
juniIkeSaRemoteIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIkeSaRemoteIpAddr.setStatus("obsolete")
_JuniIkeSaLocalIpAddr_Type = IpAddress
_JuniIkeSaLocalIpAddr_Object = MibTableColumn
juniIkeSaLocalIpAddr = _JuniIkeSaLocalIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 4, 1, 2),
    _JuniIkeSaLocalIpAddr_Type()
)
juniIkeSaLocalIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIkeSaLocalIpAddr.setStatus("obsolete")
_JuniIkeSaRouterIndex_Type = Unsigned32
_JuniIkeSaRouterIndex_Object = MibTableColumn
juniIkeSaRouterIndex = _JuniIkeSaRouterIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 4, 1, 3),
    _JuniIkeSaRouterIndex_Type()
)
juniIkeSaRouterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIkeSaRouterIndex.setStatus("obsolete")
_JuniIkeSaDirection_Type = JuniIpsecPhase1SaDirection
_JuniIkeSaDirection_Object = MibTableColumn
juniIkeSaDirection = _JuniIkeSaDirection_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 4, 1, 4),
    _JuniIkeSaDirection_Type()
)
juniIkeSaDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIkeSaDirection.setStatus("obsolete")
_JuniIkeSaState_Type = JuniIpsecPhase1SaState
_JuniIkeSaState_Object = MibTableColumn
juniIkeSaState = _JuniIkeSaState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 4, 1, 5),
    _JuniIkeSaState_Type()
)
juniIkeSaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIkeSaState.setStatus("obsolete")


class _JuniIkeSaRemaining_Type(Unsigned32):
    """Custom type juniIkeSaRemaining based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_JuniIkeSaRemaining_Type.__name__ = "Unsigned32"
_JuniIkeSaRemaining_Object = MibTableColumn
juniIkeSaRemaining = _JuniIkeSaRemaining_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 4, 1, 6),
    _JuniIkeSaRemaining_Type()
)
juniIkeSaRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIkeSaRemaining.setStatus("obsolete")
if mibBuilder.loadTexts:
    juniIkeSaRemaining.setUnits("seconds")
_JuniIkeSa2Table_Object = MibTable
juniIkeSa2Table = _JuniIkeSa2Table_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 5)
)
if mibBuilder.loadTexts:
    juniIkeSa2Table.setStatus("current")
_JuniIkeSa2Entry_Object = MibTableRow
juniIkeSa2Entry = _JuniIkeSa2Entry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 5, 1)
)
juniIkeSa2Entry.setIndexNames(
    (0, "Juniper-IKE-MIB", "juniIkeSa2RemoteIpAddr"),
    (0, "Juniper-IKE-MIB", "juniIkeSaRemotePort"),
    (0, "Juniper-IKE-MIB", "juniIkeSa2LocalIpAddr"),
    (0, "Juniper-IKE-MIB", "juniIkeSaLocalPort"),
    (0, "Juniper-IKE-MIB", "juniIkeSa2RouterIndex"),
    (0, "Juniper-IKE-MIB", "juniIkeSa2Direction"),
    (0, "Juniper-IKE-MIB", "juniIkeSaNegotiationDone"),
)
if mibBuilder.loadTexts:
    juniIkeSa2Entry.setStatus("current")
_JuniIkeSa2RemoteIpAddr_Type = IpAddress
_JuniIkeSa2RemoteIpAddr_Object = MibTableColumn
juniIkeSa2RemoteIpAddr = _JuniIkeSa2RemoteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 5, 1, 1),
    _JuniIkeSa2RemoteIpAddr_Type()
)
juniIkeSa2RemoteIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIkeSa2RemoteIpAddr.setStatus("current")
_JuniIkeSaRemotePort_Type = Unsigned32
_JuniIkeSaRemotePort_Object = MibTableColumn
juniIkeSaRemotePort = _JuniIkeSaRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 5, 1, 2),
    _JuniIkeSaRemotePort_Type()
)
juniIkeSaRemotePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIkeSaRemotePort.setStatus("current")
_JuniIkeSa2LocalIpAddr_Type = IpAddress
_JuniIkeSa2LocalIpAddr_Object = MibTableColumn
juniIkeSa2LocalIpAddr = _JuniIkeSa2LocalIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 5, 1, 3),
    _JuniIkeSa2LocalIpAddr_Type()
)
juniIkeSa2LocalIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIkeSa2LocalIpAddr.setStatus("current")
_JuniIkeSaLocalPort_Type = Unsigned32
_JuniIkeSaLocalPort_Object = MibTableColumn
juniIkeSaLocalPort = _JuniIkeSaLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 5, 1, 4),
    _JuniIkeSaLocalPort_Type()
)
juniIkeSaLocalPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIkeSaLocalPort.setStatus("current")
_JuniIkeSa2RouterIndex_Type = Unsigned32
_JuniIkeSa2RouterIndex_Object = MibTableColumn
juniIkeSa2RouterIndex = _JuniIkeSa2RouterIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 5, 1, 5),
    _JuniIkeSa2RouterIndex_Type()
)
juniIkeSa2RouterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIkeSa2RouterIndex.setStatus("current")


class _JuniIkeSa2Direction_Type(Integer32):
    """Custom type juniIkeSa2Direction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("initiator", 1),
          ("responder", 0))
    )


_JuniIkeSa2Direction_Type.__name__ = "Integer32"
_JuniIkeSa2Direction_Object = MibTableColumn
juniIkeSa2Direction = _JuniIkeSa2Direction_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 5, 1, 6),
    _JuniIkeSa2Direction_Type()
)
juniIkeSa2Direction.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIkeSa2Direction.setStatus("current")


class _JuniIkeSaNegotiationDone_Type(Integer32):
    """Custom type juniIkeSaNegotiationDone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("negotiationDone", 1),
          ("negotiationNotDone", 0))
    )


_JuniIkeSaNegotiationDone_Type.__name__ = "Integer32"
_JuniIkeSaNegotiationDone_Object = MibTableColumn
juniIkeSaNegotiationDone = _JuniIkeSaNegotiationDone_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 5, 1, 7),
    _JuniIkeSaNegotiationDone_Type()
)
juniIkeSaNegotiationDone.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIkeSaNegotiationDone.setStatus("current")
_JuniIkeSa2State_Type = JuniIpsecPhase1SaState
_JuniIkeSa2State_Object = MibTableColumn
juniIkeSa2State = _JuniIkeSa2State_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 5, 1, 8),
    _JuniIkeSa2State_Type()
)
juniIkeSa2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIkeSa2State.setStatus("current")


class _JuniIkeSa2Remaining_Type(Unsigned32):
    """Custom type juniIkeSa2Remaining based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_JuniIkeSa2Remaining_Type.__name__ = "Unsigned32"
_JuniIkeSa2Remaining_Object = MibTableColumn
juniIkeSa2Remaining = _JuniIkeSa2Remaining_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 5, 1, 9),
    _JuniIkeSa2Remaining_Type()
)
juniIkeSa2Remaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIkeSa2Remaining.setStatus("current")
if mibBuilder.loadTexts:
    juniIkeSa2Remaining.setUnits("seconds")


class _JuniRemoteCookie_Type(OctetString):
    """Custom type juniRemoteCookie based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_JuniRemoteCookie_Type.__name__ = "OctetString"
_JuniRemoteCookie_Object = MibTableColumn
juniRemoteCookie = _JuniRemoteCookie_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 5, 1, 10),
    _JuniRemoteCookie_Type()
)
juniRemoteCookie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRemoteCookie.setStatus("current")


class _JuniLocalCookie_Type(OctetString):
    """Custom type juniLocalCookie based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_JuniLocalCookie_Type.__name__ = "OctetString"
_JuniLocalCookie_Object = MibTableColumn
juniLocalCookie = _JuniLocalCookie_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 5, 1, 11),
    _JuniLocalCookie_Type()
)
juniLocalCookie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniLocalCookie.setStatus("current")
_JuniIkePolicyRuleV2Table_Object = MibTable
juniIkePolicyRuleV2Table = _JuniIkePolicyRuleV2Table_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 6)
)
if mibBuilder.loadTexts:
    juniIkePolicyRuleV2Table.setStatus("current")
_JuniIkePolicyRuleV2Entry_Object = MibTableRow
juniIkePolicyRuleV2Entry = _JuniIkePolicyRuleV2Entry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 6, 1)
)
juniIkePolicyRuleV2Entry.setIndexNames(
    (0, "Juniper-IKE-MIB", "juniIkePolicyRuleV2Priority"),
)
if mibBuilder.loadTexts:
    juniIkePolicyRuleV2Entry.setStatus("current")


class _JuniIkePolicyRuleV2Priority_Type(Integer32):
    """Custom type juniIkePolicyRuleV2Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_JuniIkePolicyRuleV2Priority_Type.__name__ = "Integer32"
_JuniIkePolicyRuleV2Priority_Object = MibTableColumn
juniIkePolicyRuleV2Priority = _JuniIkePolicyRuleV2Priority_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 6, 1, 1),
    _JuniIkePolicyRuleV2Priority_Type()
)
juniIkePolicyRuleV2Priority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIkePolicyRuleV2Priority.setStatus("current")


class _JuniIkePolicyRuleV2AuthMethod_Type(JuniIkeAuthenticationMethod):
    """Custom type juniIkePolicyRuleV2AuthMethod based on JuniIkeAuthenticationMethod"""


_JuniIkePolicyRuleV2AuthMethod_Object = MibTableColumn
juniIkePolicyRuleV2AuthMethod = _JuniIkePolicyRuleV2AuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 6, 1, 2),
    _JuniIkePolicyRuleV2AuthMethod_Type()
)
juniIkePolicyRuleV2AuthMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIkePolicyRuleV2AuthMethod.setStatus("current")


class _JuniIkePolicyRuleV2EncryptMethod_Type(JuniIkeEncryptionMethod):
    """Custom type juniIkePolicyRuleV2EncryptMethod based on JuniIkeEncryptionMethod"""


_JuniIkePolicyRuleV2EncryptMethod_Object = MibTableColumn
juniIkePolicyRuleV2EncryptMethod = _JuniIkePolicyRuleV2EncryptMethod_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 6, 1, 3),
    _JuniIkePolicyRuleV2EncryptMethod_Type()
)
juniIkePolicyRuleV2EncryptMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIkePolicyRuleV2EncryptMethod.setStatus("current")


class _JuniIkePolicyRuleV2PfsGroup_Type(JuniIkeGroup):
    """Custom type juniIkePolicyRuleV2PfsGroup based on JuniIkeGroup"""


_JuniIkePolicyRuleV2PfsGroup_Object = MibTableColumn
juniIkePolicyRuleV2PfsGroup = _JuniIkePolicyRuleV2PfsGroup_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 6, 1, 4),
    _JuniIkePolicyRuleV2PfsGroup_Type()
)
juniIkePolicyRuleV2PfsGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIkePolicyRuleV2PfsGroup.setStatus("current")


class _JuniIkePolicyRuleV2HashMethod_Type(JuniIkeHashMethod):
    """Custom type juniIkePolicyRuleV2HashMethod based on JuniIkeHashMethod"""


_JuniIkePolicyRuleV2HashMethod_Object = MibTableColumn
juniIkePolicyRuleV2HashMethod = _JuniIkePolicyRuleV2HashMethod_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 6, 1, 5),
    _JuniIkePolicyRuleV2HashMethod_Type()
)
juniIkePolicyRuleV2HashMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIkePolicyRuleV2HashMethod.setStatus("current")


class _JuniIkePolicyRuleV2Lifetime_Type(Integer32):
    """Custom type juniIkePolicyRuleV2Lifetime based on Integer32"""
    defaultValue = 28800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_JuniIkePolicyRuleV2Lifetime_Type.__name__ = "Integer32"
_JuniIkePolicyRuleV2Lifetime_Object = MibTableColumn
juniIkePolicyRuleV2Lifetime = _JuniIkePolicyRuleV2Lifetime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 6, 1, 6),
    _JuniIkePolicyRuleV2Lifetime_Type()
)
juniIkePolicyRuleV2Lifetime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIkePolicyRuleV2Lifetime.setStatus("current")


class _JuniIkePolicyRuleV2NegotiationMode_Type(JuniIkeNegotiationV2Mode):
    """Custom type juniIkePolicyRuleV2NegotiationMode based on JuniIkeNegotiationV2Mode"""


_JuniIkePolicyRuleV2NegotiationMode_Object = MibTableColumn
juniIkePolicyRuleV2NegotiationMode = _JuniIkePolicyRuleV2NegotiationMode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 6, 1, 7),
    _JuniIkePolicyRuleV2NegotiationMode_Type()
)
juniIkePolicyRuleV2NegotiationMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIkePolicyRuleV2NegotiationMode.setStatus("current")
_JuniIkePolicyRuleV2IpAddress_Type = IpAddress
_JuniIkePolicyRuleV2IpAddress_Object = MibTableColumn
juniIkePolicyRuleV2IpAddress = _JuniIkePolicyRuleV2IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 6, 1, 8),
    _JuniIkePolicyRuleV2IpAddress_Type()
)
juniIkePolicyRuleV2IpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIkePolicyRuleV2IpAddress.setStatus("current")
_JuniIkePolicyRuleV2RouterIndex_Type = Unsigned32
_JuniIkePolicyRuleV2RouterIndex_Object = MibTableColumn
juniIkePolicyRuleV2RouterIndex = _JuniIkePolicyRuleV2RouterIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 6, 1, 9),
    _JuniIkePolicyRuleV2RouterIndex_Type()
)
juniIkePolicyRuleV2RouterIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIkePolicyRuleV2RouterIndex.setStatus("current")
_JuniIkePolicyRuleV2RowStatus_Type = RowStatus
_JuniIkePolicyRuleV2RowStatus_Object = MibTableColumn
juniIkePolicyRuleV2RowStatus = _JuniIkePolicyRuleV2RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 6, 1, 10),
    _JuniIkePolicyRuleV2RowStatus_Type()
)
juniIkePolicyRuleV2RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniIkePolicyRuleV2RowStatus.setStatus("current")
_JuniIkeMIBConformance_ObjectIdentity = ObjectIdentity
juniIkeMIBConformance = _JuniIkeMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 2)
)
_JuniIkeMIBCompliances_ObjectIdentity = ObjectIdentity
juniIkeMIBCompliances = _JuniIkeMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 2, 1)
)
_JuniIkeMIBGroups_ObjectIdentity = ObjectIdentity
juniIkeMIBGroups = _JuniIkeMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 2, 2)
)

# Managed Objects groups

juniIkePolicyRuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 2, 2, 1)
)
juniIkePolicyRuleGroup.setObjects(
      *(("Juniper-IKE-MIB", "juniIkePolicyRuleAuthMethod"),
        ("Juniper-IKE-MIB", "juniIkePolicyRuleEncryptMethod"),
        ("Juniper-IKE-MIB", "juniIkePolicyRulePfsGroup"),
        ("Juniper-IKE-MIB", "juniIkePolicyRuleHashMethod"),
        ("Juniper-IKE-MIB", "juniIkePolicyRuleLifetime"),
        ("Juniper-IKE-MIB", "juniIkePolicyRuleNegotiationMode"),
        ("Juniper-IKE-MIB", "juniIkePolicyRuleRowStatus"))
)
if mibBuilder.loadTexts:
    juniIkePolicyRuleGroup.setStatus("obsolete")

juniIkeIpv4PreSharedKeyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 2, 2, 2)
)
juniIkeIpv4PreSharedKeyGroup.setObjects(
      *(("Juniper-IKE-MIB", "juniIkeIpv4PresharedKeyStr"),
        ("Juniper-IKE-MIB", "juniIkeIpv4PresharedMaskedKeyStr"),
        ("Juniper-IKE-MIB", "juniIkeIpv4PresharedKeyRowStatus"))
)
if mibBuilder.loadTexts:
    juniIkeIpv4PreSharedKeyGroup.setStatus("current")

juniIkeFqdnPreSharedKeyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 2, 2, 3)
)
juniIkeFqdnPreSharedKeyGroup.setObjects(
      *(("Juniper-IKE-MIB", "juniIkeFqdnPresharedKeyStr"),
        ("Juniper-IKE-MIB", "juniIkeFqdnPresharedMaskedKeyStr"),
        ("Juniper-IKE-MIB", "juniIkeFqdnPresharedKeyRowStatus"))
)
if mibBuilder.loadTexts:
    juniIkeFqdnPreSharedKeyGroup.setStatus("current")

juniIkeSaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 2, 2, 4)
)
juniIkeSaGroup.setObjects(
      *(("Juniper-IKE-MIB", "juniIkeSaState"),
        ("Juniper-IKE-MIB", "juniIkeSaRemaining"))
)
if mibBuilder.loadTexts:
    juniIkeSaGroup.setStatus("obsolete")

juniIkeSa2Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 2, 2, 5)
)
juniIkeSa2Group.setObjects(
      *(("Juniper-IKE-MIB", "juniIkeSa2State"),
        ("Juniper-IKE-MIB", "juniIkeSa2Remaining"),
        ("Juniper-IKE-MIB", "juniRemoteCookie"),
        ("Juniper-IKE-MIB", "juniLocalCookie"))
)
if mibBuilder.loadTexts:
    juniIkeSa2Group.setStatus("current")

juniIkePolicyRuleV2Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 2, 2, 6)
)
juniIkePolicyRuleV2Group.setObjects(
      *(("Juniper-IKE-MIB", "juniIkePolicyRuleV2AuthMethod"),
        ("Juniper-IKE-MIB", "juniIkePolicyRuleV2EncryptMethod"),
        ("Juniper-IKE-MIB", "juniIkePolicyRuleV2PfsGroup"),
        ("Juniper-IKE-MIB", "juniIkePolicyRuleV2HashMethod"),
        ("Juniper-IKE-MIB", "juniIkePolicyRuleV2Lifetime"),
        ("Juniper-IKE-MIB", "juniIkePolicyRuleV2NegotiationMode"),
        ("Juniper-IKE-MIB", "juniIkePolicyRuleV2IpAddress"),
        ("Juniper-IKE-MIB", "juniIkePolicyRuleV2RouterIndex"),
        ("Juniper-IKE-MIB", "juniIkePolicyRuleV2RowStatus"))
)
if mibBuilder.loadTexts:
    juniIkePolicyRuleV2Group.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

juniIkeCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 2, 1, 1)
)
if mibBuilder.loadTexts:
    juniIkeCompliance.setStatus(
        "obsolete"
    )

juniIkeCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 2, 1, 2)
)
if mibBuilder.loadTexts:
    juniIkeCompliance2.setStatus(
        "obsolete"
    )

juniIkeCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 2, 1, 3)
)
if mibBuilder.loadTexts:
    juniIkeCompliance3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-IKE-MIB",
    **{"JuniIkeAuthenticationMethod": JuniIkeAuthenticationMethod,
       "JuniIkeEncryptionMethod": JuniIkeEncryptionMethod,
       "JuniIkeGroup": JuniIkeGroup,
       "JuniIkeHashMethod": JuniIkeHashMethod,
       "JuniIkeNegotiationMode": JuniIkeNegotiationMode,
       "JuniIkeNegotiationV2Mode": JuniIkeNegotiationV2Mode,
       "JuniIpsecPhase1SaState": JuniIpsecPhase1SaState,
       "JuniIpsecPhase1SaDirection": JuniIpsecPhase1SaDirection,
       "juniIkeMIB": juniIkeMIB,
       "juniIkeObjects": juniIkeObjects,
       "juniIke": juniIke,
       "juniIkePolicyRuleTable": juniIkePolicyRuleTable,
       "juniIkePolicyRuleEntry": juniIkePolicyRuleEntry,
       "juniIkePolicyRulePriority": juniIkePolicyRulePriority,
       "juniIkePolicyRuleAuthMethod": juniIkePolicyRuleAuthMethod,
       "juniIkePolicyRuleEncryptMethod": juniIkePolicyRuleEncryptMethod,
       "juniIkePolicyRulePfsGroup": juniIkePolicyRulePfsGroup,
       "juniIkePolicyRuleHashMethod": juniIkePolicyRuleHashMethod,
       "juniIkePolicyRuleLifetime": juniIkePolicyRuleLifetime,
       "juniIkePolicyRuleNegotiationMode": juniIkePolicyRuleNegotiationMode,
       "juniIkePolicyRuleRowStatus": juniIkePolicyRuleRowStatus,
       "juniIkeIpv4PresharedKeyTable": juniIkeIpv4PresharedKeyTable,
       "juniIkeIpv4PresharedKeyEntry": juniIkeIpv4PresharedKeyEntry,
       "juniIkeIpv4PresharedRemoteIpAddr": juniIkeIpv4PresharedRemoteIpAddr,
       "juniIkeIpv4PresharedRouterIdx": juniIkeIpv4PresharedRouterIdx,
       "juniIkeIpv4PresharedKeyStr": juniIkeIpv4PresharedKeyStr,
       "juniIkeIpv4PresharedMaskedKeyStr": juniIkeIpv4PresharedMaskedKeyStr,
       "juniIkeIpv4PresharedKeyRowStatus": juniIkeIpv4PresharedKeyRowStatus,
       "juniIkeFqdnPresharedKeyTable": juniIkeFqdnPresharedKeyTable,
       "juniIkeFqdnPresharedKeyEntry": juniIkeFqdnPresharedKeyEntry,
       "juniIkeFqdnPresharedRemote": juniIkeFqdnPresharedRemote,
       "juniIkeFqdnPresharedRouterIndex": juniIkeFqdnPresharedRouterIndex,
       "juniIkeFqdnPresharedKeyStr": juniIkeFqdnPresharedKeyStr,
       "juniIkeFqdnPresharedMaskedKeyStr": juniIkeFqdnPresharedMaskedKeyStr,
       "juniIkeFqdnPresharedKeyRowStatus": juniIkeFqdnPresharedKeyRowStatus,
       "juniIkeSaTable": juniIkeSaTable,
       "juniIkeSaEntry": juniIkeSaEntry,
       "juniIkeSaRemoteIpAddr": juniIkeSaRemoteIpAddr,
       "juniIkeSaLocalIpAddr": juniIkeSaLocalIpAddr,
       "juniIkeSaRouterIndex": juniIkeSaRouterIndex,
       "juniIkeSaDirection": juniIkeSaDirection,
       "juniIkeSaState": juniIkeSaState,
       "juniIkeSaRemaining": juniIkeSaRemaining,
       "juniIkeSa2Table": juniIkeSa2Table,
       "juniIkeSa2Entry": juniIkeSa2Entry,
       "juniIkeSa2RemoteIpAddr": juniIkeSa2RemoteIpAddr,
       "juniIkeSaRemotePort": juniIkeSaRemotePort,
       "juniIkeSa2LocalIpAddr": juniIkeSa2LocalIpAddr,
       "juniIkeSaLocalPort": juniIkeSaLocalPort,
       "juniIkeSa2RouterIndex": juniIkeSa2RouterIndex,
       "juniIkeSa2Direction": juniIkeSa2Direction,
       "juniIkeSaNegotiationDone": juniIkeSaNegotiationDone,
       "juniIkeSa2State": juniIkeSa2State,
       "juniIkeSa2Remaining": juniIkeSa2Remaining,
       "juniRemoteCookie": juniRemoteCookie,
       "juniLocalCookie": juniLocalCookie,
       "juniIkePolicyRuleV2Table": juniIkePolicyRuleV2Table,
       "juniIkePolicyRuleV2Entry": juniIkePolicyRuleV2Entry,
       "juniIkePolicyRuleV2Priority": juniIkePolicyRuleV2Priority,
       "juniIkePolicyRuleV2AuthMethod": juniIkePolicyRuleV2AuthMethod,
       "juniIkePolicyRuleV2EncryptMethod": juniIkePolicyRuleV2EncryptMethod,
       "juniIkePolicyRuleV2PfsGroup": juniIkePolicyRuleV2PfsGroup,
       "juniIkePolicyRuleV2HashMethod": juniIkePolicyRuleV2HashMethod,
       "juniIkePolicyRuleV2Lifetime": juniIkePolicyRuleV2Lifetime,
       "juniIkePolicyRuleV2NegotiationMode": juniIkePolicyRuleV2NegotiationMode,
       "juniIkePolicyRuleV2IpAddress": juniIkePolicyRuleV2IpAddress,
       "juniIkePolicyRuleV2RouterIndex": juniIkePolicyRuleV2RouterIndex,
       "juniIkePolicyRuleV2RowStatus": juniIkePolicyRuleV2RowStatus,
       "juniIkeMIBConformance": juniIkeMIBConformance,
       "juniIkeMIBCompliances": juniIkeMIBCompliances,
       "juniIkeCompliance": juniIkeCompliance,
       "juniIkeCompliance2": juniIkeCompliance2,
       "juniIkeCompliance3": juniIkeCompliance3,
       "juniIkeMIBGroups": juniIkeMIBGroups,
       "juniIkePolicyRuleGroup": juniIkePolicyRuleGroup,
       "juniIkeIpv4PreSharedKeyGroup": juniIkeIpv4PreSharedKeyGroup,
       "juniIkeFqdnPreSharedKeyGroup": juniIkeFqdnPreSharedKeyGroup,
       "juniIkeSaGroup": juniIkeSaGroup,
       "juniIkeSa2Group": juniIkeSa2Group,
       "juniIkePolicyRuleV2Group": juniIkePolicyRuleV2Group}
)
