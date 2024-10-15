# SNMP MIB module (HPN-ICF-PORT-SECURITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-PORT-SECURITY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:01:27 2024
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

(hpnicfPortSecurity,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfPortSecurity")

(dot1xAuthSessionAuthenticMethod,
 dot1xAuthSessionTerminateCause,
 dot1xAuthSessionUserName,
 dot1xPaePortNumber) = mibBuilder.importSymbols(
    "IEEE8021-PAE-MIB",
    "dot1xAuthSessionAuthenticMethod",
    "dot1xAuthSessionTerminateCause",
    "dot1xAuthSessionUserName",
    "dot1xPaePortNumber")

(ifAdminStatus,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifAdminStatus",
    "ifIndex")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpnicfPortSecurityMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1)
)
hpnicfPortSecurityMIB.setRevisions(
        ("2004-11-24 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfPortSecurityLeaf_ObjectIdentity = ObjectIdentity
hpnicfPortSecurityLeaf = _HpnicfPortSecurityLeaf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 1)
)


class _HpnicfSecurePortSecurityControl_Type(Integer32):
    """Custom type hpnicfSecurePortSecurityControl based on Integer32"""
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


_HpnicfSecurePortSecurityControl_Type.__name__ = "Integer32"
_HpnicfSecurePortSecurityControl_Object = MibScalar
hpnicfSecurePortSecurityControl = _HpnicfSecurePortSecurityControl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 1, 1),
    _HpnicfSecurePortSecurityControl_Type()
)
hpnicfSecurePortSecurityControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSecurePortSecurityControl.setStatus("current")


class _HpnicfSecurePortVlanMembershipList_Type(DisplayString):
    """Custom type hpnicfSecurePortVlanMembershipList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfSecurePortVlanMembershipList_Type.__name__ = "DisplayString"
_HpnicfSecurePortVlanMembershipList_Object = MibScalar
hpnicfSecurePortVlanMembershipList = _HpnicfSecurePortVlanMembershipList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 1, 2),
    _HpnicfSecurePortVlanMembershipList_Type()
)
hpnicfSecurePortVlanMembershipList.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfSecurePortVlanMembershipList.setStatus("current")
_HpnicfSecureRalmObjects_ObjectIdentity = ObjectIdentity
hpnicfSecureRalmObjects = _HpnicfSecureRalmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 1, 4)
)


class _HpnicfSecureRalmDefaultSessionTime_Type(Integer32):
    """Custom type hpnicfSecureRalmDefaultSessionTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_HpnicfSecureRalmDefaultSessionTime_Type.__name__ = "Integer32"
_HpnicfSecureRalmDefaultSessionTime_Object = MibScalar
hpnicfSecureRalmDefaultSessionTime = _HpnicfSecureRalmDefaultSessionTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 1, 4, 1),
    _HpnicfSecureRalmDefaultSessionTime_Type()
)
hpnicfSecureRalmDefaultSessionTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSecureRalmDefaultSessionTime.setStatus("current")


class _HpnicfSecureRalmHoldoffTime_Type(Integer32):
    """Custom type hpnicfSecureRalmHoldoffTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_HpnicfSecureRalmHoldoffTime_Type.__name__ = "Integer32"
_HpnicfSecureRalmHoldoffTime_Object = MibScalar
hpnicfSecureRalmHoldoffTime = _HpnicfSecureRalmHoldoffTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 1, 4, 2),
    _HpnicfSecureRalmHoldoffTime_Type()
)
hpnicfSecureRalmHoldoffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSecureRalmHoldoffTime.setStatus("current")
_HpnicfSecureRalmReauthenticate_Type = MacAddress
_HpnicfSecureRalmReauthenticate_Object = MibScalar
hpnicfSecureRalmReauthenticate = _HpnicfSecureRalmReauthenticate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 1, 4, 3),
    _HpnicfSecureRalmReauthenticate_Type()
)
hpnicfSecureRalmReauthenticate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSecureRalmReauthenticate.setStatus("current")


class _HpnicfSecureRalmAuthMode_Type(Integer32):
    """Custom type hpnicfSecureRalmAuthMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("papUsernameAsMacAddress", 1),
          ("papUsernameFixed", 2))
    )


_HpnicfSecureRalmAuthMode_Type.__name__ = "Integer32"
_HpnicfSecureRalmAuthMode_Object = MibScalar
hpnicfSecureRalmAuthMode = _HpnicfSecureRalmAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 1, 4, 4),
    _HpnicfSecureRalmAuthMode_Type()
)
hpnicfSecureRalmAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSecureRalmAuthMode.setStatus("current")


class _HpnicfSecureRalmAuthUsername_Type(DisplayString):
    """Custom type hpnicfSecureRalmAuthUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_HpnicfSecureRalmAuthUsername_Type.__name__ = "DisplayString"
_HpnicfSecureRalmAuthUsername_Object = MibScalar
hpnicfSecureRalmAuthUsername = _HpnicfSecureRalmAuthUsername_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 1, 4, 5),
    _HpnicfSecureRalmAuthUsername_Type()
)
hpnicfSecureRalmAuthUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSecureRalmAuthUsername.setStatus("current")


class _HpnicfSecureRalmAuthPassword_Type(DisplayString):
    """Custom type hpnicfSecureRalmAuthPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HpnicfSecureRalmAuthPassword_Type.__name__ = "DisplayString"
_HpnicfSecureRalmAuthPassword_Object = MibScalar
hpnicfSecureRalmAuthPassword = _HpnicfSecureRalmAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 1, 4, 6),
    _HpnicfSecureRalmAuthPassword_Type()
)
hpnicfSecureRalmAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSecureRalmAuthPassword.setStatus("current")


class _HpnicfSecureRalmAuthDomain_Type(DisplayString):
    """Custom type hpnicfSecureRalmAuthDomain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_HpnicfSecureRalmAuthDomain_Type.__name__ = "DisplayString"
_HpnicfSecureRalmAuthDomain_Object = MibScalar
hpnicfSecureRalmAuthDomain = _HpnicfSecureRalmAuthDomain_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 1, 4, 7),
    _HpnicfSecureRalmAuthDomain_Type()
)
hpnicfSecureRalmAuthDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSecureRalmAuthDomain.setStatus("current")


class _HpnicfSecureRalmAuthOfflineTime_Type(Integer32):
    """Custom type hpnicfSecureRalmAuthOfflineTime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 2147483647),
    )


_HpnicfSecureRalmAuthOfflineTime_Type.__name__ = "Integer32"
_HpnicfSecureRalmAuthOfflineTime_Object = MibScalar
hpnicfSecureRalmAuthOfflineTime = _HpnicfSecureRalmAuthOfflineTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 1, 4, 8),
    _HpnicfSecureRalmAuthOfflineTime_Type()
)
hpnicfSecureRalmAuthOfflineTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSecureRalmAuthOfflineTime.setStatus("current")


class _HpnicfSecureRalmAuthServerTimeoutTime_Type(Integer32):
    """Custom type hpnicfSecureRalmAuthServerTimeoutTime based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfSecureRalmAuthServerTimeoutTime_Type.__name__ = "Integer32"
_HpnicfSecureRalmAuthServerTimeoutTime_Object = MibScalar
hpnicfSecureRalmAuthServerTimeoutTime = _HpnicfSecureRalmAuthServerTimeoutTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 1, 4, 9),
    _HpnicfSecureRalmAuthServerTimeoutTime_Type()
)
hpnicfSecureRalmAuthServerTimeoutTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSecureRalmAuthServerTimeoutTime.setStatus("current")


class _HpnicfSecureMacControl_Type(Integer32):
    """Custom type hpnicfSecureMacControl based on Integer32"""
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


_HpnicfSecureMacControl_Type.__name__ = "Integer32"
_HpnicfSecureMacControl_Object = MibScalar
hpnicfSecureMacControl = _HpnicfSecureMacControl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 1, 4, 10),
    _HpnicfSecureMacControl_Type()
)
hpnicfSecureMacControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSecureMacControl.setStatus("current")
_HpnicfPortSecurityTables_ObjectIdentity = ObjectIdentity
hpnicfPortSecurityTables = _HpnicfPortSecurityTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 2)
)
_HpnicfSecurePortTable_Object = MibTable
hpnicfSecurePortTable = _HpnicfSecurePortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfSecurePortTable.setStatus("current")
_HpnicfSecurePortEntry_Object = MibTableRow
hpnicfSecurePortEntry = _HpnicfSecurePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 2, 1, 1)
)
hpnicfSecurePortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfSecurePortEntry.setStatus("current")


class _HpnicfSecurePortMode_Type(Integer32):
    """Custom type hpnicfSecurePortMode based on Integer32"""
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
        *(("autoLearn", 3),
          ("continuousLearning", 2),
          ("macAddressAndUserLoginSecure", 14),
          ("macAddressAndUserLoginSecureExt", 15),
          ("macAddressElseUserLoginSecure", 10),
          ("macAddressElseUserLoginSecureExt", 13),
          ("macAddressOrUserLoginSecure", 9),
          ("macAddressOrUserLoginSecureExt", 12),
          ("macAddressWithRadius", 8),
          ("noRestrictions", 1),
          ("secure", 4),
          ("userLogin", 5),
          ("userLoginSecure", 6),
          ("userLoginSecureExt", 11),
          ("userLoginWithOUI", 7))
    )


_HpnicfSecurePortMode_Type.__name__ = "Integer32"
_HpnicfSecurePortMode_Object = MibTableColumn
hpnicfSecurePortMode = _HpnicfSecurePortMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 2, 1, 1, 1),
    _HpnicfSecurePortMode_Type()
)
hpnicfSecurePortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSecurePortMode.setStatus("current")


class _HpnicfSecureNeedToKnowMode_Type(Integer32):
    """Custom type hpnicfSecureNeedToKnowMode based on Integer32"""
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
        *(("disabled", 2),
          ("needToKnowOnly", 3),
          ("needToKnowWithBroadcastsAllowed", 4),
          ("needToKnowWithMulticastsAllowed", 5),
          ("notAvailable", 1),
          ("permanentNeedToKnowOnly", 6),
          ("permanentNeedToKnowWithBroadcastsAllowed", 7),
          ("permanentNeedToKnowWithMulticastsAllowed", 8))
    )


_HpnicfSecureNeedToKnowMode_Type.__name__ = "Integer32"
_HpnicfSecureNeedToKnowMode_Object = MibTableColumn
hpnicfSecureNeedToKnowMode = _HpnicfSecureNeedToKnowMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 2, 1, 1, 2),
    _HpnicfSecureNeedToKnowMode_Type()
)
hpnicfSecureNeedToKnowMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSecureNeedToKnowMode.setStatus("current")


class _HpnicfSecureIntrusionAction_Type(Integer32):
    """Custom type hpnicfSecureIntrusionAction based on Integer32"""
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
        *(("allowDefaultAccess", 5),
          ("blockMacAddress", 6),
          ("disablePort", 3),
          ("disablePortTemporarily", 4),
          ("noAction", 2),
          ("notAvailable", 1))
    )


_HpnicfSecureIntrusionAction_Type.__name__ = "Integer32"
_HpnicfSecureIntrusionAction_Object = MibTableColumn
hpnicfSecureIntrusionAction = _HpnicfSecureIntrusionAction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 2, 1, 1, 3),
    _HpnicfSecureIntrusionAction_Type()
)
hpnicfSecureIntrusionAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSecureIntrusionAction.setStatus("current")
_HpnicfSecureNumberAddresses_Type = Integer32
_HpnicfSecureNumberAddresses_Object = MibTableColumn
hpnicfSecureNumberAddresses = _HpnicfSecureNumberAddresses_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 2, 1, 1, 4),
    _HpnicfSecureNumberAddresses_Type()
)
hpnicfSecureNumberAddresses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSecureNumberAddresses.setStatus("current")
_HpnicfSecureNumberAddressesStored_Type = Integer32
_HpnicfSecureNumberAddressesStored_Object = MibTableColumn
hpnicfSecureNumberAddressesStored = _HpnicfSecureNumberAddressesStored_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 2, 1, 1, 5),
    _HpnicfSecureNumberAddressesStored_Type()
)
hpnicfSecureNumberAddressesStored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSecureNumberAddressesStored.setStatus("current")
_HpnicfSecureMaximumAddresses_Type = Integer32
_HpnicfSecureMaximumAddresses_Object = MibTableColumn
hpnicfSecureMaximumAddresses = _HpnicfSecureMaximumAddresses_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 2, 1, 1, 6),
    _HpnicfSecureMaximumAddresses_Type()
)
hpnicfSecureMaximumAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSecureMaximumAddresses.setStatus("current")
_HpnicfSecureAddressTable_Object = MibTable
hpnicfSecureAddressTable = _HpnicfSecureAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hpnicfSecureAddressTable.setStatus("current")
_HpnicfSecureAddressEntry_Object = MibTableRow
hpnicfSecureAddressEntry = _HpnicfSecureAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 2, 2, 1)
)
hpnicfSecureAddressEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-PORT-SECURITY-MIB", "hpnicfSecureAddrMAC"),
    (0, "HPN-ICF-PORT-SECURITY-MIB", "hpnicfSecureAddrVlanID"),
)
if mibBuilder.loadTexts:
    hpnicfSecureAddressEntry.setStatus("current")
_HpnicfSecureAddrMAC_Type = MacAddress
_HpnicfSecureAddrMAC_Object = MibTableColumn
hpnicfSecureAddrMAC = _HpnicfSecureAddrMAC_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 2, 2, 1, 1),
    _HpnicfSecureAddrMAC_Type()
)
hpnicfSecureAddrMAC.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfSecureAddrMAC.setStatus("current")
_HpnicfSecureAddrVlanID_Type = Integer32
_HpnicfSecureAddrVlanID_Object = MibTableColumn
hpnicfSecureAddrVlanID = _HpnicfSecureAddrVlanID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 2, 2, 1, 2),
    _HpnicfSecureAddrVlanID_Type()
)
hpnicfSecureAddrVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSecureAddrVlanID.setStatus("current")


class _HpnicfSecureAddrMACStatus_Type(Integer32):
    """Custom type hpnicfSecureAddrMACStatus based on Integer32"""
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
        *(("addressBlackhole", 1),
          ("addressDot1xAuth", 3),
          ("addressRALM", 4),
          ("addressUserConfig", 2))
    )


_HpnicfSecureAddrMACStatus_Type.__name__ = "Integer32"
_HpnicfSecureAddrMACStatus_Object = MibTableColumn
hpnicfSecureAddrMACStatus = _HpnicfSecureAddrMACStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 2, 2, 1, 3),
    _HpnicfSecureAddrMACStatus_Type()
)
hpnicfSecureAddrMACStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSecureAddrMACStatus.setStatus("current")
_HpnicfSecureAddrRowStatus_Type = RowStatus
_HpnicfSecureAddrRowStatus_Object = MibTableColumn
hpnicfSecureAddrRowStatus = _HpnicfSecureAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 2, 2, 1, 4),
    _HpnicfSecureAddrRowStatus_Type()
)
hpnicfSecureAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSecureAddrRowStatus.setStatus("current")
_HpnicfSecureOUITable_Object = MibTable
hpnicfSecureOUITable = _HpnicfSecureOUITable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 2, 3)
)
if mibBuilder.loadTexts:
    hpnicfSecureOUITable.setStatus("current")
_HpnicfSecureOUIEntry_Object = MibTableRow
hpnicfSecureOUIEntry = _HpnicfSecureOUIEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 2, 3, 1)
)
hpnicfSecureOUIEntry.setIndexNames(
    (0, "HPN-ICF-PORT-SECURITY-MIB", "hpnicfSecureOUIIndex"),
)
if mibBuilder.loadTexts:
    hpnicfSecureOUIEntry.setStatus("current")


class _HpnicfSecureOUIIndex_Type(Integer32):
    """Custom type hpnicfSecureOUIIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_HpnicfSecureOUIIndex_Type.__name__ = "Integer32"
_HpnicfSecureOUIIndex_Object = MibTableColumn
hpnicfSecureOUIIndex = _HpnicfSecureOUIIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 2, 3, 1, 1),
    _HpnicfSecureOUIIndex_Type()
)
hpnicfSecureOUIIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfSecureOUIIndex.setStatus("current")


class _HpnicfSecureOUI_Type(OctetString):
    """Custom type hpnicfSecureOUI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_HpnicfSecureOUI_Type.__name__ = "OctetString"
_HpnicfSecureOUI_Object = MibTableColumn
hpnicfSecureOUI = _HpnicfSecureOUI_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 2, 3, 1, 2),
    _HpnicfSecureOUI_Type()
)
hpnicfSecureOUI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSecureOUI.setStatus("current")
_HpnicfSecureOUIRowStatus_Type = RowStatus
_HpnicfSecureOUIRowStatus_Object = MibTableColumn
hpnicfSecureOUIRowStatus = _HpnicfSecureOUIRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 2, 3, 1, 3),
    _HpnicfSecureOUIRowStatus_Type()
)
hpnicfSecureOUIRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSecureOUIRowStatus.setStatus("current")
_HpnicfSecureBindingTable_Object = MibTable
hpnicfSecureBindingTable = _HpnicfSecureBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 2, 4)
)
if mibBuilder.loadTexts:
    hpnicfSecureBindingTable.setStatus("current")
_HpnicfSecureBindingEntry_Object = MibTableRow
hpnicfSecureBindingEntry = _HpnicfSecureBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 2, 4, 1)
)
hpnicfSecureBindingEntry.setIndexNames(
    (0, "HPN-ICF-PORT-SECURITY-MIB", "hpnicfSecureBindingIndex"),
)
if mibBuilder.loadTexts:
    hpnicfSecureBindingEntry.setStatus("current")
_HpnicfSecureBindingIndex_Type = Integer32
_HpnicfSecureBindingIndex_Object = MibTableColumn
hpnicfSecureBindingIndex = _HpnicfSecureBindingIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 2, 4, 1, 1),
    _HpnicfSecureBindingIndex_Type()
)
hpnicfSecureBindingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfSecureBindingIndex.setStatus("current")
_HpnicfSecureBindingPort_Type = Integer32
_HpnicfSecureBindingPort_Object = MibTableColumn
hpnicfSecureBindingPort = _HpnicfSecureBindingPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 2, 4, 1, 2),
    _HpnicfSecureBindingPort_Type()
)
hpnicfSecureBindingPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSecureBindingPort.setStatus("current")
_HpnicfSecureBindingAddrMAC_Type = MacAddress
_HpnicfSecureBindingAddrMAC_Object = MibTableColumn
hpnicfSecureBindingAddrMAC = _HpnicfSecureBindingAddrMAC_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 2, 4, 1, 3),
    _HpnicfSecureBindingAddrMAC_Type()
)
hpnicfSecureBindingAddrMAC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSecureBindingAddrMAC.setStatus("current")
_HpnicfSecureBindingAddrIp_Type = IpAddress
_HpnicfSecureBindingAddrIp_Object = MibTableColumn
hpnicfSecureBindingAddrIp = _HpnicfSecureBindingAddrIp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 2, 4, 1, 4),
    _HpnicfSecureBindingAddrIp_Type()
)
hpnicfSecureBindingAddrIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSecureBindingAddrIp.setStatus("current")
_HpnicfSecureBindingRowStatus_Type = RowStatus
_HpnicfSecureBindingRowStatus_Object = MibTableColumn
hpnicfSecureBindingRowStatus = _HpnicfSecureBindingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 2, 4, 1, 5),
    _HpnicfSecureBindingRowStatus_Type()
)
hpnicfSecureBindingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSecureBindingRowStatus.setStatus("current")
_HpnicfSecureAssignTable_Object = MibTable
hpnicfSecureAssignTable = _HpnicfSecureAssignTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 2, 5)
)
if mibBuilder.loadTexts:
    hpnicfSecureAssignTable.setStatus("current")
_HpnicfSecureAssignEntry_Object = MibTableRow
hpnicfSecureAssignEntry = _HpnicfSecureAssignEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 2, 5, 1)
)
hpnicfSecureAssignEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfSecureAssignEntry.setStatus("current")


class _HpnicfSecureAssignEnable_Type(TruthValue):
    """Custom type hpnicfSecureAssignEnable based on TruthValue"""


_HpnicfSecureAssignEnable_Object = MibTableColumn
hpnicfSecureAssignEnable = _HpnicfSecureAssignEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 2, 5, 1, 1),
    _HpnicfSecureAssignEnable_Type()
)
hpnicfSecureAssignEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSecureAssignEnable.setStatus("current")


class _HpnicfSecureVlanAssignment_Type(OctetString):
    """Custom type hpnicfSecureVlanAssignment based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfSecureVlanAssignment_Type.__name__ = "OctetString"
_HpnicfSecureVlanAssignment_Object = MibTableColumn
hpnicfSecureVlanAssignment = _HpnicfSecureVlanAssignment_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 2, 5, 1, 2),
    _HpnicfSecureVlanAssignment_Type()
)
hpnicfSecureVlanAssignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSecureVlanAssignment.setStatus("current")
_HpnicfPortSecurityNotifications_ObjectIdentity = ObjectIdentity
hpnicfPortSecurityNotifications = _HpnicfPortSecurityNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 3)
)

# Managed Objects groups


# Notification objects

hpnicfSecureAddressLearned = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 3, 1)
)
hpnicfSecureAddressLearned.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("HPN-ICF-PORT-SECURITY-MIB", "hpnicfSecureAddrMAC"))
)
if mibBuilder.loadTexts:
    hpnicfSecureAddressLearned.setStatus(
        "current"
    )

hpnicfSecureViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 3, 2)
)
hpnicfSecureViolation.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("HPN-ICF-PORT-SECURITY-MIB", "hpnicfSecureAddrMAC"),
        ("IF-MIB", "ifAdminStatus"))
)
if mibBuilder.loadTexts:
    hpnicfSecureViolation.setStatus(
        "current"
    )

hpnicfSecureLoginFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 3, 3)
)
hpnicfSecureLoginFailure.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("HPN-ICF-PORT-SECURITY-MIB", "hpnicfSecureAddrMAC"),
        ("IEEE8021-PAE-MIB", "dot1xAuthSessionUserName"))
)
if mibBuilder.loadTexts:
    hpnicfSecureLoginFailure.setStatus(
        "current"
    )

hpnicfSecureLogon = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 3, 4)
)
hpnicfSecureLogon.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("HPN-ICF-PORT-SECURITY-MIB", "hpnicfSecureAddrMAC"),
        ("IEEE8021-PAE-MIB", "dot1xAuthSessionUserName"),
        ("IEEE8021-PAE-MIB", "dot1xAuthSessionAuthenticMethod"),
        ("HPN-ICF-PORT-SECURITY-MIB", "hpnicfSecurePortVlanMembershipList"))
)
if mibBuilder.loadTexts:
    hpnicfSecureLogon.setStatus(
        "current"
    )

hpnicfSecureLogoff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 3, 5)
)
hpnicfSecureLogoff.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("HPN-ICF-PORT-SECURITY-MIB", "hpnicfSecureAddrMAC"),
        ("IEEE8021-PAE-MIB", "dot1xAuthSessionUserName"),
        ("IEEE8021-PAE-MIB", "dot1xAuthSessionTerminateCause"),
        ("HPN-ICF-PORT-SECURITY-MIB", "hpnicfSecurePortVlanMembershipList"))
)
if mibBuilder.loadTexts:
    hpnicfSecureLogoff.setStatus(
        "current"
    )

hpnicfSecureRalmLoginFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 3, 6)
)
hpnicfSecureRalmLoginFailure.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("HPN-ICF-PORT-SECURITY-MIB", "hpnicfSecureAddrMAC"),
        ("HPN-ICF-PORT-SECURITY-MIB", "hpnicfSecureRalmAuthMode"),
        ("HPN-ICF-PORT-SECURITY-MIB", "hpnicfSecureRalmAuthUsername"))
)
if mibBuilder.loadTexts:
    hpnicfSecureRalmLoginFailure.setStatus(
        "current"
    )

hpnicfSecureRalmLogon = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 3, 7)
)
hpnicfSecureRalmLogon.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("HPN-ICF-PORT-SECURITY-MIB", "hpnicfSecureAddrMAC"),
        ("HPN-ICF-PORT-SECURITY-MIB", "hpnicfSecureRalmAuthMode"),
        ("HPN-ICF-PORT-SECURITY-MIB", "hpnicfSecureRalmAuthUsername"),
        ("HPN-ICF-PORT-SECURITY-MIB", "hpnicfSecurePortVlanMembershipList"))
)
if mibBuilder.loadTexts:
    hpnicfSecureRalmLogon.setStatus(
        "current"
    )

hpnicfSecureRalmLogoff = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 26, 1, 3, 8)
)
hpnicfSecureRalmLogoff.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("HPN-ICF-PORT-SECURITY-MIB", "hpnicfSecureAddrMAC"),
        ("HPN-ICF-PORT-SECURITY-MIB", "hpnicfSecureRalmAuthMode"),
        ("HPN-ICF-PORT-SECURITY-MIB", "hpnicfSecureRalmAuthUsername"),
        ("HPN-ICF-PORT-SECURITY-MIB", "hpnicfSecurePortVlanMembershipList"))
)
if mibBuilder.loadTexts:
    hpnicfSecureRalmLogoff.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-PORT-SECURITY-MIB",
    **{"hpnicfPortSecurityMIB": hpnicfPortSecurityMIB,
       "hpnicfPortSecurityLeaf": hpnicfPortSecurityLeaf,
       "hpnicfSecurePortSecurityControl": hpnicfSecurePortSecurityControl,
       "hpnicfSecurePortVlanMembershipList": hpnicfSecurePortVlanMembershipList,
       "hpnicfSecureRalmObjects": hpnicfSecureRalmObjects,
       "hpnicfSecureRalmDefaultSessionTime": hpnicfSecureRalmDefaultSessionTime,
       "hpnicfSecureRalmHoldoffTime": hpnicfSecureRalmHoldoffTime,
       "hpnicfSecureRalmReauthenticate": hpnicfSecureRalmReauthenticate,
       "hpnicfSecureRalmAuthMode": hpnicfSecureRalmAuthMode,
       "hpnicfSecureRalmAuthUsername": hpnicfSecureRalmAuthUsername,
       "hpnicfSecureRalmAuthPassword": hpnicfSecureRalmAuthPassword,
       "hpnicfSecureRalmAuthDomain": hpnicfSecureRalmAuthDomain,
       "hpnicfSecureRalmAuthOfflineTime": hpnicfSecureRalmAuthOfflineTime,
       "hpnicfSecureRalmAuthServerTimeoutTime": hpnicfSecureRalmAuthServerTimeoutTime,
       "hpnicfSecureMacControl": hpnicfSecureMacControl,
       "hpnicfPortSecurityTables": hpnicfPortSecurityTables,
       "hpnicfSecurePortTable": hpnicfSecurePortTable,
       "hpnicfSecurePortEntry": hpnicfSecurePortEntry,
       "hpnicfSecurePortMode": hpnicfSecurePortMode,
       "hpnicfSecureNeedToKnowMode": hpnicfSecureNeedToKnowMode,
       "hpnicfSecureIntrusionAction": hpnicfSecureIntrusionAction,
       "hpnicfSecureNumberAddresses": hpnicfSecureNumberAddresses,
       "hpnicfSecureNumberAddressesStored": hpnicfSecureNumberAddressesStored,
       "hpnicfSecureMaximumAddresses": hpnicfSecureMaximumAddresses,
       "hpnicfSecureAddressTable": hpnicfSecureAddressTable,
       "hpnicfSecureAddressEntry": hpnicfSecureAddressEntry,
       "hpnicfSecureAddrMAC": hpnicfSecureAddrMAC,
       "hpnicfSecureAddrVlanID": hpnicfSecureAddrVlanID,
       "hpnicfSecureAddrMACStatus": hpnicfSecureAddrMACStatus,
       "hpnicfSecureAddrRowStatus": hpnicfSecureAddrRowStatus,
       "hpnicfSecureOUITable": hpnicfSecureOUITable,
       "hpnicfSecureOUIEntry": hpnicfSecureOUIEntry,
       "hpnicfSecureOUIIndex": hpnicfSecureOUIIndex,
       "hpnicfSecureOUI": hpnicfSecureOUI,
       "hpnicfSecureOUIRowStatus": hpnicfSecureOUIRowStatus,
       "hpnicfSecureBindingTable": hpnicfSecureBindingTable,
       "hpnicfSecureBindingEntry": hpnicfSecureBindingEntry,
       "hpnicfSecureBindingIndex": hpnicfSecureBindingIndex,
       "hpnicfSecureBindingPort": hpnicfSecureBindingPort,
       "hpnicfSecureBindingAddrMAC": hpnicfSecureBindingAddrMAC,
       "hpnicfSecureBindingAddrIp": hpnicfSecureBindingAddrIp,
       "hpnicfSecureBindingRowStatus": hpnicfSecureBindingRowStatus,
       "hpnicfSecureAssignTable": hpnicfSecureAssignTable,
       "hpnicfSecureAssignEntry": hpnicfSecureAssignEntry,
       "hpnicfSecureAssignEnable": hpnicfSecureAssignEnable,
       "hpnicfSecureVlanAssignment": hpnicfSecureVlanAssignment,
       "hpnicfPortSecurityNotifications": hpnicfPortSecurityNotifications,
       "hpnicfSecureAddressLearned": hpnicfSecureAddressLearned,
       "hpnicfSecureViolation": hpnicfSecureViolation,
       "hpnicfSecureLoginFailure": hpnicfSecureLoginFailure,
       "hpnicfSecureLogon": hpnicfSecureLogon,
       "hpnicfSecureLogoff": hpnicfSecureLogoff,
       "hpnicfSecureRalmLoginFailure": hpnicfSecureRalmLoginFailure,
       "hpnicfSecureRalmLogon": hpnicfSecureRalmLogon,
       "hpnicfSecureRalmLogoff": hpnicfSecureRalmLogoff}
)
