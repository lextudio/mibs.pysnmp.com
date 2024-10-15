# SNMP MIB module (HH3C-PORT-SECURITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-PORT-SECURITY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:54:28 2024
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

(hh3cPortSecurity,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cPortSecurity")

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

hh3cPortSecurityMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 26, 1)
)
hh3cPortSecurityMIB.setRevisions(
        ("2004-11-24 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cPortSecurityLeaf_ObjectIdentity = ObjectIdentity
hh3cPortSecurityLeaf = _Hh3cPortSecurityLeaf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 26, 1, 1)
)


class _Hh3cSecurePortSecurityControl_Type(Integer32):
    """Custom type hh3cSecurePortSecurityControl based on Integer32"""
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


_Hh3cSecurePortSecurityControl_Type.__name__ = "Integer32"
_Hh3cSecurePortSecurityControl_Object = MibScalar
hh3cSecurePortSecurityControl = _Hh3cSecurePortSecurityControl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 26, 1, 1, 1),
    _Hh3cSecurePortSecurityControl_Type()
)
hh3cSecurePortSecurityControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSecurePortSecurityControl.setStatus("current")


class _Hh3cSecurePortVlanMembershipList_Type(DisplayString):
    """Custom type hh3cSecurePortVlanMembershipList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cSecurePortVlanMembershipList_Type.__name__ = "DisplayString"
_Hh3cSecurePortVlanMembershipList_Object = MibScalar
hh3cSecurePortVlanMembershipList = _Hh3cSecurePortVlanMembershipList_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 26, 1, 1, 2),
    _Hh3cSecurePortVlanMembershipList_Type()
)
hh3cSecurePortVlanMembershipList.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSecurePortVlanMembershipList.setStatus("current")
_Hh3cSecureRalmObjects_ObjectIdentity = ObjectIdentity
hh3cSecureRalmObjects = _Hh3cSecureRalmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 26, 1, 1, 4)
)


class _Hh3cSecureRalmDefaultSessionTime_Type(Integer32):
    """Custom type hh3cSecureRalmDefaultSessionTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_Hh3cSecureRalmDefaultSessionTime_Type.__name__ = "Integer32"
_Hh3cSecureRalmDefaultSessionTime_Object = MibScalar
hh3cSecureRalmDefaultSessionTime = _Hh3cSecureRalmDefaultSessionTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 26, 1, 1, 4, 1),
    _Hh3cSecureRalmDefaultSessionTime_Type()
)
hh3cSecureRalmDefaultSessionTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSecureRalmDefaultSessionTime.setStatus("current")


class _Hh3cSecureRalmHoldoffTime_Type(Integer32):
    """Custom type hh3cSecureRalmHoldoffTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_Hh3cSecureRalmHoldoffTime_Type.__name__ = "Integer32"
_Hh3cSecureRalmHoldoffTime_Object = MibScalar
hh3cSecureRalmHoldoffTime = _Hh3cSecureRalmHoldoffTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 26, 1, 1, 4, 2),
    _Hh3cSecureRalmHoldoffTime_Type()
)
hh3cSecureRalmHoldoffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSecureRalmHoldoffTime.setStatus("current")
_Hh3cSecureRalmReauthenticate_Type = MacAddress
_Hh3cSecureRalmReauthenticate_Object = MibScalar
hh3cSecureRalmReauthenticate = _Hh3cSecureRalmReauthenticate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 26, 1, 1, 4, 3),
    _Hh3cSecureRalmReauthenticate_Type()
)
hh3cSecureRalmReauthenticate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSecureRalmReauthenticate.setStatus("current")


class _Hh3cSecureRalmAuthMode_Type(Integer32):
    """Custom type hh3cSecureRalmAuthMode based on Integer32"""
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


_Hh3cSecureRalmAuthMode_Type.__name__ = "Integer32"
_Hh3cSecureRalmAuthMode_Object = MibScalar
hh3cSecureRalmAuthMode = _Hh3cSecureRalmAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 26, 1, 1, 4, 4),
    _Hh3cSecureRalmAuthMode_Type()
)
hh3cSecureRalmAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSecureRalmAuthMode.setStatus("current")


class _Hh3cSecureRalmAuthUsername_Type(DisplayString):
    """Custom type hh3cSecureRalmAuthUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_Hh3cSecureRalmAuthUsername_Type.__name__ = "DisplayString"
_Hh3cSecureRalmAuthUsername_Object = MibScalar
hh3cSecureRalmAuthUsername = _Hh3cSecureRalmAuthUsername_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 26, 1, 1, 4, 5),
    _Hh3cSecureRalmAuthUsername_Type()
)
hh3cSecureRalmAuthUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSecureRalmAuthUsername.setStatus("current")


class _Hh3cSecureRalmAuthPassword_Type(DisplayString):
    """Custom type hh3cSecureRalmAuthPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Hh3cSecureRalmAuthPassword_Type.__name__ = "DisplayString"
_Hh3cSecureRalmAuthPassword_Object = MibScalar
hh3cSecureRalmAuthPassword = _Hh3cSecureRalmAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 26, 1, 1, 4, 6),
    _Hh3cSecureRalmAuthPassword_Type()
)
hh3cSecureRalmAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSecureRalmAuthPassword.setStatus("current")


class _Hh3cSecureRalmAuthDomain_Type(DisplayString):
    """Custom type hh3cSecureRalmAuthDomain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_Hh3cSecureRalmAuthDomain_Type.__name__ = "DisplayString"
_Hh3cSecureRalmAuthDomain_Object = MibScalar
hh3cSecureRalmAuthDomain = _Hh3cSecureRalmAuthDomain_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 26, 1, 1, 4, 7),
    _Hh3cSecureRalmAuthDomain_Type()
)
hh3cSecureRalmAuthDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSecureRalmAuthDomain.setStatus("current")


class _Hh3cSecureRalmAuthOfflineTime_Type(Integer32):
    """Custom type hh3cSecureRalmAuthOfflineTime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cSecureRalmAuthOfflineTime_Type.__name__ = "Integer32"
_Hh3cSecureRalmAuthOfflineTime_Object = MibScalar
hh3cSecureRalmAuthOfflineTime = _Hh3cSecureRalmAuthOfflineTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 26, 1, 1, 4, 8),
    _Hh3cSecureRalmAuthOfflineTime_Type()
)
hh3cSecureRalmAuthOfflineTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSecureRalmAuthOfflineTime.setStatus("current")


class _Hh3cSecureRalmAuthServerTimeoutTime_Type(Integer32):
    """Custom type hh3cSecureRalmAuthServerTimeoutTime based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cSecureRalmAuthServerTimeoutTime_Type.__name__ = "Integer32"
_Hh3cSecureRalmAuthServerTimeoutTime_Object = MibScalar
hh3cSecureRalmAuthServerTimeoutTime = _Hh3cSecureRalmAuthServerTimeoutTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 26, 1, 1, 4, 9),
    _Hh3cSecureRalmAuthServerTimeoutTime_Type()
)
hh3cSecureRalmAuthServerTimeoutTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSecureRalmAuthServerTimeoutTime.setStatus("current")


class _Hh3cSecureMacControl_Type(Integer32):
    """Custom type hh3cSecureMacControl based on Integer32"""
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


_Hh3cSecureMacControl_Type.__name__ = "Integer32"
_Hh3cSecureMacControl_Object = MibScalar
hh3cSecureMacControl = _Hh3cSecureMacControl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 26, 1, 1, 4, 10),
    _Hh3cSecureMacControl_Type()
)
hh3cSecureMacControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSecureMacControl.setStatus("current")
_Hh3cPortSecurityTables_ObjectIdentity = ObjectIdentity
hh3cPortSecurityTables = _Hh3cPortSecurityTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 26, 1, 2)
)
_Hh3cSecurePortTable_Object = MibTable
hh3cSecurePortTable = _Hh3cSecurePortTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 26, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cSecurePortTable.setStatus("current")
_Hh3cSecurePortEntry_Object = MibTableRow
hh3cSecurePortEntry = _Hh3cSecurePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 26, 1, 2, 1, 1)
)
hh3cSecurePortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cSecurePortEntry.setStatus("current")


class _Hh3cSecurePortMode_Type(Integer32):
    """Custom type hh3cSecurePortMode based on Integer32"""
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


_Hh3cSecurePortMode_Type.__name__ = "Integer32"
_Hh3cSecurePortMode_Object = MibTableColumn
hh3cSecurePortMode = _Hh3cSecurePortMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 26, 1, 2, 1, 1, 1),
    _Hh3cSecurePortMode_Type()
)
hh3cSecurePortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSecurePortMode.setStatus("current")


class _Hh3cSecureNeedToKnowMode_Type(Integer32):
    """Custom type hh3cSecureNeedToKnowMode based on Integer32"""
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


_Hh3cSecureNeedToKnowMode_Type.__name__ = "Integer32"
_Hh3cSecureNeedToKnowMode_Object = MibTableColumn
hh3cSecureNeedToKnowMode = _Hh3cSecureNeedToKnowMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 26, 1, 2, 1, 1, 2),
    _Hh3cSecureNeedToKnowMode_Type()
)
hh3cSecureNeedToKnowMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSecureNeedToKnowMode.setStatus("current")


class _Hh3cSecureIntrusionAction_Type(Integer32):
    """Custom type hh3cSecureIntrusionAction based on Integer32"""
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


_Hh3cSecureIntrusionAction_Type.__name__ = "Integer32"
_Hh3cSecureIntrusionAction_Object = MibTableColumn
hh3cSecureIntrusionAction = _Hh3cSecureIntrusionAction_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 26, 1, 2, 1, 1, 3),
    _Hh3cSecureIntrusionAction_Type()
)
hh3cSecureIntrusionAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSecureIntrusionAction.setStatus("current")
_Hh3cSecureNumberAddresses_Type = Integer32
_Hh3cSecureNumberAddresses_Object = MibTableColumn
hh3cSecureNumberAddresses = _Hh3cSecureNumberAddresses_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 26, 1, 2, 1, 1, 4),
    _Hh3cSecureNumberAddresses_Type()
)
hh3cSecureNumberAddresses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSecureNumberAddresses.setStatus("current")
_Hh3cSecureNumberAddressesStored_Type = Integer32
_Hh3cSecureNumberAddressesStored_Object = MibTableColumn
hh3cSecureNumberAddressesStored = _Hh3cSecureNumberAddressesStored_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 26, 1, 2, 1, 1, 5),
    _Hh3cSecureNumberAddressesStored_Type()
)
hh3cSecureNumberAddressesStored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSecureNumberAddressesStored.setStatus("current")
_Hh3cSecureMaximumAddresses_Type = Integer32
_Hh3cSecureMaximumAddresses_Object = MibTableColumn
hh3cSecureMaximumAddresses = _Hh3cSecureMaximumAddresses_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 26, 1, 2, 1, 1, 6),
    _Hh3cSecureMaximumAddresses_Type()
)
hh3cSecureMaximumAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSecureMaximumAddresses.setStatus("current")
_Hh3cSecureAddressTable_Object = MibTable
hh3cSecureAddressTable = _Hh3cSecureAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 26, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cSecureAddressTable.setStatus("current")
_Hh3cSecureAddressEntry_Object = MibTableRow
hh3cSecureAddressEntry = _Hh3cSecureAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 26, 1, 2, 2, 1)
)
hh3cSecureAddressEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-PORT-SECURITY-MIB", "hh3cSecureAddrMAC"),
    (0, "HH3C-PORT-SECURITY-MIB", "hh3cSecureAddrVlanID"),
)
if mibBuilder.loadTexts:
    hh3cSecureAddressEntry.setStatus("current")
_Hh3cSecureAddrMAC_Type = MacAddress
_Hh3cSecureAddrMAC_Object = MibTableColumn
hh3cSecureAddrMAC = _Hh3cSecureAddrMAC_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 26, 1, 2, 2, 1, 1),
    _Hh3cSecureAddrMAC_Type()
)
hh3cSecureAddrMAC.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSecureAddrMAC.setStatus("current")
_Hh3cSecureAddrVlanID_Type = Integer32
_Hh3cSecureAddrVlanID_Object = MibTableColumn
hh3cSecureAddrVlanID = _Hh3cSecureAddrVlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 26, 1, 2, 2, 1, 2),
    _Hh3cSecureAddrVlanID_Type()
)
hh3cSecureAddrVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSecureAddrVlanID.setStatus("current")


class _Hh3cSecureAddrMACStatus_Type(Integer32):
    """Custom type hh3cSecureAddrMACStatus based on Integer32"""
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


_Hh3cSecureAddrMACStatus_Type.__name__ = "Integer32"
_Hh3cSecureAddrMACStatus_Object = MibTableColumn
hh3cSecureAddrMACStatus = _Hh3cSecureAddrMACStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 26, 1, 2, 2, 1, 3),
    _Hh3cSecureAddrMACStatus_Type()
)
hh3cSecureAddrMACStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSecureAddrMACStatus.setStatus("current")
_Hh3cSecureAddrRowStatus_Type = RowStatus
_Hh3cSecureAddrRowStatus_Object = MibTableColumn
hh3cSecureAddrRowStatus = _Hh3cSecureAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 26, 1, 2, 2, 1, 4),
    _Hh3cSecureAddrRowStatus_Type()
)
hh3cSecureAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSecureAddrRowStatus.setStatus("current")
_Hh3cSecureOUITable_Object = MibTable
hh3cSecureOUITable = _Hh3cSecureOUITable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 26, 1, 2, 3)
)
if mibBuilder.loadTexts:
    hh3cSecureOUITable.setStatus("current")
_Hh3cSecureOUIEntry_Object = MibTableRow
hh3cSecureOUIEntry = _Hh3cSecureOUIEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 26, 1, 2, 3, 1)
)
hh3cSecureOUIEntry.setIndexNames(
    (0, "HH3C-PORT-SECURITY-MIB", "hh3cSecureOUIIndex"),
)
if mibBuilder.loadTexts:
    hh3cSecureOUIEntry.setStatus("current")


class _Hh3cSecureOUIIndex_Type(Integer32):
    """Custom type hh3cSecureOUIIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Hh3cSecureOUIIndex_Type.__name__ = "Integer32"
_Hh3cSecureOUIIndex_Object = MibTableColumn
hh3cSecureOUIIndex = _Hh3cSecureOUIIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 26, 1, 2, 3, 1, 1),
    _Hh3cSecureOUIIndex_Type()
)
hh3cSecureOUIIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSecureOUIIndex.setStatus("current")


class _Hh3cSecureOUI_Type(OctetString):
    """Custom type hh3cSecureOUI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_Hh3cSecureOUI_Type.__name__ = "OctetString"
_Hh3cSecureOUI_Object = MibTableColumn
hh3cSecureOUI = _Hh3cSecureOUI_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 26, 1, 2, 3, 1, 2),
    _Hh3cSecureOUI_Type()
)
hh3cSecureOUI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSecureOUI.setStatus("current")
_Hh3cSecureOUIRowStatus_Type = RowStatus
_Hh3cSecureOUIRowStatus_Object = MibTableColumn
hh3cSecureOUIRowStatus = _Hh3cSecureOUIRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 26, 1, 2, 3, 1, 3),
    _Hh3cSecureOUIRowStatus_Type()
)
hh3cSecureOUIRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSecureOUIRowStatus.setStatus("current")
_Hh3cSecureBindingTable_Object = MibTable
hh3cSecureBindingTable = _Hh3cSecureBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 26, 1, 2, 4)
)
if mibBuilder.loadTexts:
    hh3cSecureBindingTable.setStatus("current")
_Hh3cSecureBindingEntry_Object = MibTableRow
hh3cSecureBindingEntry = _Hh3cSecureBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 26, 1, 2, 4, 1)
)
hh3cSecureBindingEntry.setIndexNames(
    (0, "HH3C-PORT-SECURITY-MIB", "hh3cSecureBindingIndex"),
)
if mibBuilder.loadTexts:
    hh3cSecureBindingEntry.setStatus("current")
_Hh3cSecureBindingIndex_Type = Integer32
_Hh3cSecureBindingIndex_Object = MibTableColumn
hh3cSecureBindingIndex = _Hh3cSecureBindingIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 26, 1, 2, 4, 1, 1),
    _Hh3cSecureBindingIndex_Type()
)
hh3cSecureBindingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSecureBindingIndex.setStatus("current")
_Hh3cSecureBindingPort_Type = Integer32
_Hh3cSecureBindingPort_Object = MibTableColumn
hh3cSecureBindingPort = _Hh3cSecureBindingPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 26, 1, 2, 4, 1, 2),
    _Hh3cSecureBindingPort_Type()
)
hh3cSecureBindingPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSecureBindingPort.setStatus("current")
_Hh3cSecureBindingAddrMAC_Type = MacAddress
_Hh3cSecureBindingAddrMAC_Object = MibTableColumn
hh3cSecureBindingAddrMAC = _Hh3cSecureBindingAddrMAC_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 26, 1, 2, 4, 1, 3),
    _Hh3cSecureBindingAddrMAC_Type()
)
hh3cSecureBindingAddrMAC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSecureBindingAddrMAC.setStatus("current")
_Hh3cSecureBindingAddrIp_Type = IpAddress
_Hh3cSecureBindingAddrIp_Object = MibTableColumn
hh3cSecureBindingAddrIp = _Hh3cSecureBindingAddrIp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 26, 1, 2, 4, 1, 4),
    _Hh3cSecureBindingAddrIp_Type()
)
hh3cSecureBindingAddrIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSecureBindingAddrIp.setStatus("current")
_Hh3cSecureBindingRowStatus_Type = RowStatus
_Hh3cSecureBindingRowStatus_Object = MibTableColumn
hh3cSecureBindingRowStatus = _Hh3cSecureBindingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 26, 1, 2, 4, 1, 5),
    _Hh3cSecureBindingRowStatus_Type()
)
hh3cSecureBindingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cSecureBindingRowStatus.setStatus("current")
_Hh3cSecureAssignTable_Object = MibTable
hh3cSecureAssignTable = _Hh3cSecureAssignTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 26, 1, 2, 5)
)
if mibBuilder.loadTexts:
    hh3cSecureAssignTable.setStatus("current")
_Hh3cSecureAssignEntry_Object = MibTableRow
hh3cSecureAssignEntry = _Hh3cSecureAssignEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 26, 1, 2, 5, 1)
)
hh3cSecureAssignEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cSecureAssignEntry.setStatus("current")


class _Hh3cSecureAssignEnable_Type(TruthValue):
    """Custom type hh3cSecureAssignEnable based on TruthValue"""


_Hh3cSecureAssignEnable_Object = MibTableColumn
hh3cSecureAssignEnable = _Hh3cSecureAssignEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 26, 1, 2, 5, 1, 1),
    _Hh3cSecureAssignEnable_Type()
)
hh3cSecureAssignEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSecureAssignEnable.setStatus("current")


class _Hh3cSecureVlanAssignment_Type(OctetString):
    """Custom type hh3cSecureVlanAssignment based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cSecureVlanAssignment_Type.__name__ = "OctetString"
_Hh3cSecureVlanAssignment_Object = MibTableColumn
hh3cSecureVlanAssignment = _Hh3cSecureVlanAssignment_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 26, 1, 2, 5, 1, 2),
    _Hh3cSecureVlanAssignment_Type()
)
hh3cSecureVlanAssignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSecureVlanAssignment.setStatus("current")
_Hh3cPortSecurityNotifications_ObjectIdentity = ObjectIdentity
hh3cPortSecurityNotifications = _Hh3cPortSecurityNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 26, 1, 3)
)

# Managed Objects groups


# Notification objects

hh3cSecureAddressLearned = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 26, 1, 3, 1)
)
hh3cSecureAddressLearned.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("HH3C-PORT-SECURITY-MIB", "hh3cSecureAddrMAC"))
)
if mibBuilder.loadTexts:
    hh3cSecureAddressLearned.setStatus(
        "current"
    )

hh3cSecureViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 26, 1, 3, 2)
)
hh3cSecureViolation.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("HH3C-PORT-SECURITY-MIB", "hh3cSecureAddrMAC"),
        ("IF-MIB", "ifAdminStatus"))
)
if mibBuilder.loadTexts:
    hh3cSecureViolation.setStatus(
        "current"
    )

hh3cSecureLoginFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 26, 1, 3, 3)
)
hh3cSecureLoginFailure.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("HH3C-PORT-SECURITY-MIB", "hh3cSecureAddrMAC"),
        ("IEEE8021-PAE-MIB", "dot1xAuthSessionUserName"))
)
if mibBuilder.loadTexts:
    hh3cSecureLoginFailure.setStatus(
        "current"
    )

hh3cSecureLogon = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 26, 1, 3, 4)
)
hh3cSecureLogon.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("HH3C-PORT-SECURITY-MIB", "hh3cSecureAddrMAC"),
        ("IEEE8021-PAE-MIB", "dot1xAuthSessionUserName"),
        ("IEEE8021-PAE-MIB", "dot1xAuthSessionAuthenticMethod"),
        ("HH3C-PORT-SECURITY-MIB", "hh3cSecurePortVlanMembershipList"))
)
if mibBuilder.loadTexts:
    hh3cSecureLogon.setStatus(
        "current"
    )

hh3cSecureLogoff = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 26, 1, 3, 5)
)
hh3cSecureLogoff.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("HH3C-PORT-SECURITY-MIB", "hh3cSecureAddrMAC"),
        ("IEEE8021-PAE-MIB", "dot1xAuthSessionUserName"),
        ("IEEE8021-PAE-MIB", "dot1xAuthSessionTerminateCause"),
        ("HH3C-PORT-SECURITY-MIB", "hh3cSecurePortVlanMembershipList"))
)
if mibBuilder.loadTexts:
    hh3cSecureLogoff.setStatus(
        "current"
    )

hh3cSecureRalmLoginFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 26, 1, 3, 6)
)
hh3cSecureRalmLoginFailure.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("HH3C-PORT-SECURITY-MIB", "hh3cSecureAddrMAC"),
        ("HH3C-PORT-SECURITY-MIB", "hh3cSecureRalmAuthMode"),
        ("HH3C-PORT-SECURITY-MIB", "hh3cSecureRalmAuthUsername"))
)
if mibBuilder.loadTexts:
    hh3cSecureRalmLoginFailure.setStatus(
        "current"
    )

hh3cSecureRalmLogon = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 26, 1, 3, 7)
)
hh3cSecureRalmLogon.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("HH3C-PORT-SECURITY-MIB", "hh3cSecureAddrMAC"),
        ("HH3C-PORT-SECURITY-MIB", "hh3cSecureRalmAuthMode"),
        ("HH3C-PORT-SECURITY-MIB", "hh3cSecureRalmAuthUsername"),
        ("HH3C-PORT-SECURITY-MIB", "hh3cSecurePortVlanMembershipList"))
)
if mibBuilder.loadTexts:
    hh3cSecureRalmLogon.setStatus(
        "current"
    )

hh3cSecureRalmLogoff = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 26, 1, 3, 8)
)
hh3cSecureRalmLogoff.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("HH3C-PORT-SECURITY-MIB", "hh3cSecureAddrMAC"),
        ("HH3C-PORT-SECURITY-MIB", "hh3cSecureRalmAuthMode"),
        ("HH3C-PORT-SECURITY-MIB", "hh3cSecureRalmAuthUsername"),
        ("HH3C-PORT-SECURITY-MIB", "hh3cSecurePortVlanMembershipList"))
)
if mibBuilder.loadTexts:
    hh3cSecureRalmLogoff.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-PORT-SECURITY-MIB",
    **{"hh3cPortSecurityMIB": hh3cPortSecurityMIB,
       "hh3cPortSecurityLeaf": hh3cPortSecurityLeaf,
       "hh3cSecurePortSecurityControl": hh3cSecurePortSecurityControl,
       "hh3cSecurePortVlanMembershipList": hh3cSecurePortVlanMembershipList,
       "hh3cSecureRalmObjects": hh3cSecureRalmObjects,
       "hh3cSecureRalmDefaultSessionTime": hh3cSecureRalmDefaultSessionTime,
       "hh3cSecureRalmHoldoffTime": hh3cSecureRalmHoldoffTime,
       "hh3cSecureRalmReauthenticate": hh3cSecureRalmReauthenticate,
       "hh3cSecureRalmAuthMode": hh3cSecureRalmAuthMode,
       "hh3cSecureRalmAuthUsername": hh3cSecureRalmAuthUsername,
       "hh3cSecureRalmAuthPassword": hh3cSecureRalmAuthPassword,
       "hh3cSecureRalmAuthDomain": hh3cSecureRalmAuthDomain,
       "hh3cSecureRalmAuthOfflineTime": hh3cSecureRalmAuthOfflineTime,
       "hh3cSecureRalmAuthServerTimeoutTime": hh3cSecureRalmAuthServerTimeoutTime,
       "hh3cSecureMacControl": hh3cSecureMacControl,
       "hh3cPortSecurityTables": hh3cPortSecurityTables,
       "hh3cSecurePortTable": hh3cSecurePortTable,
       "hh3cSecurePortEntry": hh3cSecurePortEntry,
       "hh3cSecurePortMode": hh3cSecurePortMode,
       "hh3cSecureNeedToKnowMode": hh3cSecureNeedToKnowMode,
       "hh3cSecureIntrusionAction": hh3cSecureIntrusionAction,
       "hh3cSecureNumberAddresses": hh3cSecureNumberAddresses,
       "hh3cSecureNumberAddressesStored": hh3cSecureNumberAddressesStored,
       "hh3cSecureMaximumAddresses": hh3cSecureMaximumAddresses,
       "hh3cSecureAddressTable": hh3cSecureAddressTable,
       "hh3cSecureAddressEntry": hh3cSecureAddressEntry,
       "hh3cSecureAddrMAC": hh3cSecureAddrMAC,
       "hh3cSecureAddrVlanID": hh3cSecureAddrVlanID,
       "hh3cSecureAddrMACStatus": hh3cSecureAddrMACStatus,
       "hh3cSecureAddrRowStatus": hh3cSecureAddrRowStatus,
       "hh3cSecureOUITable": hh3cSecureOUITable,
       "hh3cSecureOUIEntry": hh3cSecureOUIEntry,
       "hh3cSecureOUIIndex": hh3cSecureOUIIndex,
       "hh3cSecureOUI": hh3cSecureOUI,
       "hh3cSecureOUIRowStatus": hh3cSecureOUIRowStatus,
       "hh3cSecureBindingTable": hh3cSecureBindingTable,
       "hh3cSecureBindingEntry": hh3cSecureBindingEntry,
       "hh3cSecureBindingIndex": hh3cSecureBindingIndex,
       "hh3cSecureBindingPort": hh3cSecureBindingPort,
       "hh3cSecureBindingAddrMAC": hh3cSecureBindingAddrMAC,
       "hh3cSecureBindingAddrIp": hh3cSecureBindingAddrIp,
       "hh3cSecureBindingRowStatus": hh3cSecureBindingRowStatus,
       "hh3cSecureAssignTable": hh3cSecureAssignTable,
       "hh3cSecureAssignEntry": hh3cSecureAssignEntry,
       "hh3cSecureAssignEnable": hh3cSecureAssignEnable,
       "hh3cSecureVlanAssignment": hh3cSecureVlanAssignment,
       "hh3cPortSecurityNotifications": hh3cPortSecurityNotifications,
       "hh3cSecureAddressLearned": hh3cSecureAddressLearned,
       "hh3cSecureViolation": hh3cSecureViolation,
       "hh3cSecureLoginFailure": hh3cSecureLoginFailure,
       "hh3cSecureLogon": hh3cSecureLogon,
       "hh3cSecureLogoff": hh3cSecureLogoff,
       "hh3cSecureRalmLoginFailure": hh3cSecureRalmLoginFailure,
       "hh3cSecureRalmLogon": hh3cSecureRalmLogon,
       "hh3cSecureRalmLogoff": hh3cSecureRalmLogoff}
)
