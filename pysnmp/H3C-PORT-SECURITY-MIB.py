# SNMP MIB module (H3C-PORT-SECURITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H3C-PORT-SECURITY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:51:06 2024
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

(h3cPortSecurity,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cPortSecurity")

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

h3cPortSecurityMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 26, 1)
)
h3cPortSecurityMIB.setRevisions(
        ("2004-11-24 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cPortSecurityLeaf_ObjectIdentity = ObjectIdentity
h3cPortSecurityLeaf = _H3cPortSecurityLeaf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 26, 1, 1)
)


class _H3cSecurePortSecurityControl_Type(Integer32):
    """Custom type h3cSecurePortSecurityControl based on Integer32"""
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


_H3cSecurePortSecurityControl_Type.__name__ = "Integer32"
_H3cSecurePortSecurityControl_Object = MibScalar
h3cSecurePortSecurityControl = _H3cSecurePortSecurityControl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 26, 1, 1, 1),
    _H3cSecurePortSecurityControl_Type()
)
h3cSecurePortSecurityControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSecurePortSecurityControl.setStatus("current")


class _H3cSecurePortVlanMembershipList_Type(DisplayString):
    """Custom type h3cSecurePortVlanMembershipList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3cSecurePortVlanMembershipList_Type.__name__ = "DisplayString"
_H3cSecurePortVlanMembershipList_Object = MibScalar
h3cSecurePortVlanMembershipList = _H3cSecurePortVlanMembershipList_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 26, 1, 1, 2),
    _H3cSecurePortVlanMembershipList_Type()
)
h3cSecurePortVlanMembershipList.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cSecurePortVlanMembershipList.setStatus("current")
_H3cSecureRalmObjects_ObjectIdentity = ObjectIdentity
h3cSecureRalmObjects = _H3cSecureRalmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 26, 1, 1, 4)
)


class _H3cSecureRalmDefaultSessionTime_Type(Integer32):
    """Custom type h3cSecureRalmDefaultSessionTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_H3cSecureRalmDefaultSessionTime_Type.__name__ = "Integer32"
_H3cSecureRalmDefaultSessionTime_Object = MibScalar
h3cSecureRalmDefaultSessionTime = _H3cSecureRalmDefaultSessionTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 26, 1, 1, 4, 1),
    _H3cSecureRalmDefaultSessionTime_Type()
)
h3cSecureRalmDefaultSessionTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSecureRalmDefaultSessionTime.setStatus("current")


class _H3cSecureRalmHoldoffTime_Type(Integer32):
    """Custom type h3cSecureRalmHoldoffTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_H3cSecureRalmHoldoffTime_Type.__name__ = "Integer32"
_H3cSecureRalmHoldoffTime_Object = MibScalar
h3cSecureRalmHoldoffTime = _H3cSecureRalmHoldoffTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 26, 1, 1, 4, 2),
    _H3cSecureRalmHoldoffTime_Type()
)
h3cSecureRalmHoldoffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSecureRalmHoldoffTime.setStatus("current")
_H3cSecureRalmReauthenticate_Type = MacAddress
_H3cSecureRalmReauthenticate_Object = MibScalar
h3cSecureRalmReauthenticate = _H3cSecureRalmReauthenticate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 26, 1, 1, 4, 3),
    _H3cSecureRalmReauthenticate_Type()
)
h3cSecureRalmReauthenticate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSecureRalmReauthenticate.setStatus("current")


class _H3cSecureRalmAuthMode_Type(Integer32):
    """Custom type h3cSecureRalmAuthMode based on Integer32"""
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


_H3cSecureRalmAuthMode_Type.__name__ = "Integer32"
_H3cSecureRalmAuthMode_Object = MibScalar
h3cSecureRalmAuthMode = _H3cSecureRalmAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 26, 1, 1, 4, 4),
    _H3cSecureRalmAuthMode_Type()
)
h3cSecureRalmAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSecureRalmAuthMode.setStatus("current")


class _H3cSecureRalmAuthUsername_Type(DisplayString):
    """Custom type h3cSecureRalmAuthUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_H3cSecureRalmAuthUsername_Type.__name__ = "DisplayString"
_H3cSecureRalmAuthUsername_Object = MibScalar
h3cSecureRalmAuthUsername = _H3cSecureRalmAuthUsername_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 26, 1, 1, 4, 5),
    _H3cSecureRalmAuthUsername_Type()
)
h3cSecureRalmAuthUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSecureRalmAuthUsername.setStatus("current")


class _H3cSecureRalmAuthPassword_Type(DisplayString):
    """Custom type h3cSecureRalmAuthPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_H3cSecureRalmAuthPassword_Type.__name__ = "DisplayString"
_H3cSecureRalmAuthPassword_Object = MibScalar
h3cSecureRalmAuthPassword = _H3cSecureRalmAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 26, 1, 1, 4, 6),
    _H3cSecureRalmAuthPassword_Type()
)
h3cSecureRalmAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSecureRalmAuthPassword.setStatus("current")


class _H3cSecureRalmAuthDomain_Type(DisplayString):
    """Custom type h3cSecureRalmAuthDomain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_H3cSecureRalmAuthDomain_Type.__name__ = "DisplayString"
_H3cSecureRalmAuthDomain_Object = MibScalar
h3cSecureRalmAuthDomain = _H3cSecureRalmAuthDomain_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 26, 1, 1, 4, 7),
    _H3cSecureRalmAuthDomain_Type()
)
h3cSecureRalmAuthDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSecureRalmAuthDomain.setStatus("current")


class _H3cSecureRalmAuthOfflineTime_Type(Integer32):
    """Custom type h3cSecureRalmAuthOfflineTime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_H3cSecureRalmAuthOfflineTime_Type.__name__ = "Integer32"
_H3cSecureRalmAuthOfflineTime_Object = MibScalar
h3cSecureRalmAuthOfflineTime = _H3cSecureRalmAuthOfflineTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 26, 1, 1, 4, 8),
    _H3cSecureRalmAuthOfflineTime_Type()
)
h3cSecureRalmAuthOfflineTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSecureRalmAuthOfflineTime.setStatus("current")


class _H3cSecureRalmAuthServerTimeoutTime_Type(Integer32):
    """Custom type h3cSecureRalmAuthServerTimeoutTime based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_H3cSecureRalmAuthServerTimeoutTime_Type.__name__ = "Integer32"
_H3cSecureRalmAuthServerTimeoutTime_Object = MibScalar
h3cSecureRalmAuthServerTimeoutTime = _H3cSecureRalmAuthServerTimeoutTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 26, 1, 1, 4, 9),
    _H3cSecureRalmAuthServerTimeoutTime_Type()
)
h3cSecureRalmAuthServerTimeoutTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSecureRalmAuthServerTimeoutTime.setStatus("current")


class _H3cSecureMacControl_Type(Integer32):
    """Custom type h3cSecureMacControl based on Integer32"""
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


_H3cSecureMacControl_Type.__name__ = "Integer32"
_H3cSecureMacControl_Object = MibScalar
h3cSecureMacControl = _H3cSecureMacControl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 26, 1, 1, 4, 10),
    _H3cSecureMacControl_Type()
)
h3cSecureMacControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSecureMacControl.setStatus("current")
_H3cPortSecurityTables_ObjectIdentity = ObjectIdentity
h3cPortSecurityTables = _H3cPortSecurityTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 26, 1, 2)
)
_H3cSecurePortTable_Object = MibTable
h3cSecurePortTable = _H3cSecurePortTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 26, 1, 2, 1)
)
if mibBuilder.loadTexts:
    h3cSecurePortTable.setStatus("current")
_H3cSecurePortEntry_Object = MibTableRow
h3cSecurePortEntry = _H3cSecurePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 26, 1, 2, 1, 1)
)
h3cSecurePortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cSecurePortEntry.setStatus("current")


class _H3cSecurePortMode_Type(Integer32):
    """Custom type h3cSecurePortMode based on Integer32"""
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


_H3cSecurePortMode_Type.__name__ = "Integer32"
_H3cSecurePortMode_Object = MibTableColumn
h3cSecurePortMode = _H3cSecurePortMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 26, 1, 2, 1, 1, 1),
    _H3cSecurePortMode_Type()
)
h3cSecurePortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSecurePortMode.setStatus("current")


class _H3cSecureNeedToKnowMode_Type(Integer32):
    """Custom type h3cSecureNeedToKnowMode based on Integer32"""
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


_H3cSecureNeedToKnowMode_Type.__name__ = "Integer32"
_H3cSecureNeedToKnowMode_Object = MibTableColumn
h3cSecureNeedToKnowMode = _H3cSecureNeedToKnowMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 26, 1, 2, 1, 1, 2),
    _H3cSecureNeedToKnowMode_Type()
)
h3cSecureNeedToKnowMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSecureNeedToKnowMode.setStatus("current")


class _H3cSecureIntrusionAction_Type(Integer32):
    """Custom type h3cSecureIntrusionAction based on Integer32"""
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


_H3cSecureIntrusionAction_Type.__name__ = "Integer32"
_H3cSecureIntrusionAction_Object = MibTableColumn
h3cSecureIntrusionAction = _H3cSecureIntrusionAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 26, 1, 2, 1, 1, 3),
    _H3cSecureIntrusionAction_Type()
)
h3cSecureIntrusionAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSecureIntrusionAction.setStatus("current")
_H3cSecureNumberAddresses_Type = Integer32
_H3cSecureNumberAddresses_Object = MibTableColumn
h3cSecureNumberAddresses = _H3cSecureNumberAddresses_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 26, 1, 2, 1, 1, 4),
    _H3cSecureNumberAddresses_Type()
)
h3cSecureNumberAddresses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSecureNumberAddresses.setStatus("current")
_H3cSecureNumberAddressesStored_Type = Integer32
_H3cSecureNumberAddressesStored_Object = MibTableColumn
h3cSecureNumberAddressesStored = _H3cSecureNumberAddressesStored_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 26, 1, 2, 1, 1, 5),
    _H3cSecureNumberAddressesStored_Type()
)
h3cSecureNumberAddressesStored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSecureNumberAddressesStored.setStatus("current")
_H3cSecureMaximumAddresses_Type = Integer32
_H3cSecureMaximumAddresses_Object = MibTableColumn
h3cSecureMaximumAddresses = _H3cSecureMaximumAddresses_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 26, 1, 2, 1, 1, 6),
    _H3cSecureMaximumAddresses_Type()
)
h3cSecureMaximumAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSecureMaximumAddresses.setStatus("current")
_H3cSecureAddressTable_Object = MibTable
h3cSecureAddressTable = _H3cSecureAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 26, 1, 2, 2)
)
if mibBuilder.loadTexts:
    h3cSecureAddressTable.setStatus("current")
_H3cSecureAddressEntry_Object = MibTableRow
h3cSecureAddressEntry = _H3cSecureAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 26, 1, 2, 2, 1)
)
h3cSecureAddressEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "H3C-PORT-SECURITY-MIB", "h3cSecureAddrMAC"),
    (0, "H3C-PORT-SECURITY-MIB", "h3cSecureAddrVlanID"),
)
if mibBuilder.loadTexts:
    h3cSecureAddressEntry.setStatus("current")
_H3cSecureAddrMAC_Type = MacAddress
_H3cSecureAddrMAC_Object = MibTableColumn
h3cSecureAddrMAC = _H3cSecureAddrMAC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 26, 1, 2, 2, 1, 1),
    _H3cSecureAddrMAC_Type()
)
h3cSecureAddrMAC.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cSecureAddrMAC.setStatus("current")
_H3cSecureAddrVlanID_Type = Integer32
_H3cSecureAddrVlanID_Object = MibTableColumn
h3cSecureAddrVlanID = _H3cSecureAddrVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 26, 1, 2, 2, 1, 2),
    _H3cSecureAddrVlanID_Type()
)
h3cSecureAddrVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSecureAddrVlanID.setStatus("current")


class _H3cSecureAddrMACStatus_Type(Integer32):
    """Custom type h3cSecureAddrMACStatus based on Integer32"""
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


_H3cSecureAddrMACStatus_Type.__name__ = "Integer32"
_H3cSecureAddrMACStatus_Object = MibTableColumn
h3cSecureAddrMACStatus = _H3cSecureAddrMACStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 26, 1, 2, 2, 1, 3),
    _H3cSecureAddrMACStatus_Type()
)
h3cSecureAddrMACStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSecureAddrMACStatus.setStatus("current")
_H3cSecureAddrRowStatus_Type = RowStatus
_H3cSecureAddrRowStatus_Object = MibTableColumn
h3cSecureAddrRowStatus = _H3cSecureAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 26, 1, 2, 2, 1, 4),
    _H3cSecureAddrRowStatus_Type()
)
h3cSecureAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSecureAddrRowStatus.setStatus("current")
_H3cSecureOUITable_Object = MibTable
h3cSecureOUITable = _H3cSecureOUITable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 26, 1, 2, 3)
)
if mibBuilder.loadTexts:
    h3cSecureOUITable.setStatus("current")
_H3cSecureOUIEntry_Object = MibTableRow
h3cSecureOUIEntry = _H3cSecureOUIEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 26, 1, 2, 3, 1)
)
h3cSecureOUIEntry.setIndexNames(
    (0, "H3C-PORT-SECURITY-MIB", "h3cSecureOUIIndex"),
)
if mibBuilder.loadTexts:
    h3cSecureOUIEntry.setStatus("current")


class _H3cSecureOUIIndex_Type(Integer32):
    """Custom type h3cSecureOUIIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_H3cSecureOUIIndex_Type.__name__ = "Integer32"
_H3cSecureOUIIndex_Object = MibTableColumn
h3cSecureOUIIndex = _H3cSecureOUIIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 26, 1, 2, 3, 1, 1),
    _H3cSecureOUIIndex_Type()
)
h3cSecureOUIIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cSecureOUIIndex.setStatus("current")


class _H3cSecureOUI_Type(OctetString):
    """Custom type h3cSecureOUI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_H3cSecureOUI_Type.__name__ = "OctetString"
_H3cSecureOUI_Object = MibTableColumn
h3cSecureOUI = _H3cSecureOUI_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 26, 1, 2, 3, 1, 2),
    _H3cSecureOUI_Type()
)
h3cSecureOUI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSecureOUI.setStatus("current")
_H3cSecureOUIRowStatus_Type = RowStatus
_H3cSecureOUIRowStatus_Object = MibTableColumn
h3cSecureOUIRowStatus = _H3cSecureOUIRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 26, 1, 2, 3, 1, 3),
    _H3cSecureOUIRowStatus_Type()
)
h3cSecureOUIRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSecureOUIRowStatus.setStatus("current")
_H3cSecureBindingTable_Object = MibTable
h3cSecureBindingTable = _H3cSecureBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 26, 1, 2, 4)
)
if mibBuilder.loadTexts:
    h3cSecureBindingTable.setStatus("current")
_H3cSecureBindingEntry_Object = MibTableRow
h3cSecureBindingEntry = _H3cSecureBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 26, 1, 2, 4, 1)
)
h3cSecureBindingEntry.setIndexNames(
    (0, "H3C-PORT-SECURITY-MIB", "h3cSecureBindingIndex"),
)
if mibBuilder.loadTexts:
    h3cSecureBindingEntry.setStatus("current")
_H3cSecureBindingIndex_Type = Integer32
_H3cSecureBindingIndex_Object = MibTableColumn
h3cSecureBindingIndex = _H3cSecureBindingIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 26, 1, 2, 4, 1, 1),
    _H3cSecureBindingIndex_Type()
)
h3cSecureBindingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cSecureBindingIndex.setStatus("current")
_H3cSecureBindingPort_Type = Integer32
_H3cSecureBindingPort_Object = MibTableColumn
h3cSecureBindingPort = _H3cSecureBindingPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 26, 1, 2, 4, 1, 2),
    _H3cSecureBindingPort_Type()
)
h3cSecureBindingPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSecureBindingPort.setStatus("current")
_H3cSecureBindingAddrMAC_Type = MacAddress
_H3cSecureBindingAddrMAC_Object = MibTableColumn
h3cSecureBindingAddrMAC = _H3cSecureBindingAddrMAC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 26, 1, 2, 4, 1, 3),
    _H3cSecureBindingAddrMAC_Type()
)
h3cSecureBindingAddrMAC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSecureBindingAddrMAC.setStatus("current")
_H3cSecureBindingAddrIp_Type = IpAddress
_H3cSecureBindingAddrIp_Object = MibTableColumn
h3cSecureBindingAddrIp = _H3cSecureBindingAddrIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 26, 1, 2, 4, 1, 4),
    _H3cSecureBindingAddrIp_Type()
)
h3cSecureBindingAddrIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSecureBindingAddrIp.setStatus("current")
_H3cSecureBindingRowStatus_Type = RowStatus
_H3cSecureBindingRowStatus_Object = MibTableColumn
h3cSecureBindingRowStatus = _H3cSecureBindingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 26, 1, 2, 4, 1, 5),
    _H3cSecureBindingRowStatus_Type()
)
h3cSecureBindingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cSecureBindingRowStatus.setStatus("current")
_H3cSecureAssignTable_Object = MibTable
h3cSecureAssignTable = _H3cSecureAssignTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 26, 1, 2, 5)
)
if mibBuilder.loadTexts:
    h3cSecureAssignTable.setStatus("current")
_H3cSecureAssignEntry_Object = MibTableRow
h3cSecureAssignEntry = _H3cSecureAssignEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 26, 1, 2, 5, 1)
)
h3cSecureAssignEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cSecureAssignEntry.setStatus("current")


class _H3cSecureAssignEnable_Type(TruthValue):
    """Custom type h3cSecureAssignEnable based on TruthValue"""


_H3cSecureAssignEnable_Object = MibTableColumn
h3cSecureAssignEnable = _H3cSecureAssignEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 26, 1, 2, 5, 1, 1),
    _H3cSecureAssignEnable_Type()
)
h3cSecureAssignEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSecureAssignEnable.setStatus("current")


class _H3cSecureVlanAssignment_Type(OctetString):
    """Custom type h3cSecureVlanAssignment based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3cSecureVlanAssignment_Type.__name__ = "OctetString"
_H3cSecureVlanAssignment_Object = MibTableColumn
h3cSecureVlanAssignment = _H3cSecureVlanAssignment_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 26, 1, 2, 5, 1, 2),
    _H3cSecureVlanAssignment_Type()
)
h3cSecureVlanAssignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSecureVlanAssignment.setStatus("current")
_H3cPortSecurityNotifications_ObjectIdentity = ObjectIdentity
h3cPortSecurityNotifications = _H3cPortSecurityNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 26, 1, 3)
)

# Managed Objects groups


# Notification objects

h3cSecureAddressLearned = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 26, 1, 3, 1)
)
h3cSecureAddressLearned.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("H3C-PORT-SECURITY-MIB", "h3cSecureAddrMAC"))
)
if mibBuilder.loadTexts:
    h3cSecureAddressLearned.setStatus(
        "current"
    )

h3cSecureViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 26, 1, 3, 2)
)
h3cSecureViolation.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("H3C-PORT-SECURITY-MIB", "h3cSecureAddrMAC"),
        ("IF-MIB", "ifAdminStatus"))
)
if mibBuilder.loadTexts:
    h3cSecureViolation.setStatus(
        "current"
    )

h3cSecureLoginFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 26, 1, 3, 3)
)
h3cSecureLoginFailure.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("H3C-PORT-SECURITY-MIB", "h3cSecureAddrMAC"),
        ("IEEE8021-PAE-MIB", "dot1xAuthSessionUserName"))
)
if mibBuilder.loadTexts:
    h3cSecureLoginFailure.setStatus(
        "current"
    )

h3cSecureLogon = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 26, 1, 3, 4)
)
h3cSecureLogon.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("H3C-PORT-SECURITY-MIB", "h3cSecureAddrMAC"),
        ("IEEE8021-PAE-MIB", "dot1xAuthSessionUserName"),
        ("IEEE8021-PAE-MIB", "dot1xAuthSessionAuthenticMethod"),
        ("H3C-PORT-SECURITY-MIB", "h3cSecurePortVlanMembershipList"))
)
if mibBuilder.loadTexts:
    h3cSecureLogon.setStatus(
        "current"
    )

h3cSecureLogoff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 26, 1, 3, 5)
)
h3cSecureLogoff.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("H3C-PORT-SECURITY-MIB", "h3cSecureAddrMAC"),
        ("IEEE8021-PAE-MIB", "dot1xAuthSessionUserName"),
        ("IEEE8021-PAE-MIB", "dot1xAuthSessionTerminateCause"),
        ("H3C-PORT-SECURITY-MIB", "h3cSecurePortVlanMembershipList"))
)
if mibBuilder.loadTexts:
    h3cSecureLogoff.setStatus(
        "current"
    )

h3cSecureRalmLoginFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 26, 1, 3, 6)
)
h3cSecureRalmLoginFailure.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("H3C-PORT-SECURITY-MIB", "h3cSecureAddrMAC"),
        ("H3C-PORT-SECURITY-MIB", "h3cSecureRalmAuthMode"),
        ("H3C-PORT-SECURITY-MIB", "h3cSecureRalmAuthUsername"))
)
if mibBuilder.loadTexts:
    h3cSecureRalmLoginFailure.setStatus(
        "current"
    )

h3cSecureRalmLogon = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 26, 1, 3, 7)
)
h3cSecureRalmLogon.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("H3C-PORT-SECURITY-MIB", "h3cSecureAddrMAC"),
        ("H3C-PORT-SECURITY-MIB", "h3cSecureRalmAuthMode"),
        ("H3C-PORT-SECURITY-MIB", "h3cSecureRalmAuthUsername"),
        ("H3C-PORT-SECURITY-MIB", "h3cSecurePortVlanMembershipList"))
)
if mibBuilder.loadTexts:
    h3cSecureRalmLogon.setStatus(
        "current"
    )

h3cSecureRalmLogoff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 26, 1, 3, 8)
)
h3cSecureRalmLogoff.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("H3C-PORT-SECURITY-MIB", "h3cSecureAddrMAC"),
        ("H3C-PORT-SECURITY-MIB", "h3cSecureRalmAuthMode"),
        ("H3C-PORT-SECURITY-MIB", "h3cSecureRalmAuthUsername"),
        ("H3C-PORT-SECURITY-MIB", "h3cSecurePortVlanMembershipList"))
)
if mibBuilder.loadTexts:
    h3cSecureRalmLogoff.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-PORT-SECURITY-MIB",
    **{"h3cPortSecurityMIB": h3cPortSecurityMIB,
       "h3cPortSecurityLeaf": h3cPortSecurityLeaf,
       "h3cSecurePortSecurityControl": h3cSecurePortSecurityControl,
       "h3cSecurePortVlanMembershipList": h3cSecurePortVlanMembershipList,
       "h3cSecureRalmObjects": h3cSecureRalmObjects,
       "h3cSecureRalmDefaultSessionTime": h3cSecureRalmDefaultSessionTime,
       "h3cSecureRalmHoldoffTime": h3cSecureRalmHoldoffTime,
       "h3cSecureRalmReauthenticate": h3cSecureRalmReauthenticate,
       "h3cSecureRalmAuthMode": h3cSecureRalmAuthMode,
       "h3cSecureRalmAuthUsername": h3cSecureRalmAuthUsername,
       "h3cSecureRalmAuthPassword": h3cSecureRalmAuthPassword,
       "h3cSecureRalmAuthDomain": h3cSecureRalmAuthDomain,
       "h3cSecureRalmAuthOfflineTime": h3cSecureRalmAuthOfflineTime,
       "h3cSecureRalmAuthServerTimeoutTime": h3cSecureRalmAuthServerTimeoutTime,
       "h3cSecureMacControl": h3cSecureMacControl,
       "h3cPortSecurityTables": h3cPortSecurityTables,
       "h3cSecurePortTable": h3cSecurePortTable,
       "h3cSecurePortEntry": h3cSecurePortEntry,
       "h3cSecurePortMode": h3cSecurePortMode,
       "h3cSecureNeedToKnowMode": h3cSecureNeedToKnowMode,
       "h3cSecureIntrusionAction": h3cSecureIntrusionAction,
       "h3cSecureNumberAddresses": h3cSecureNumberAddresses,
       "h3cSecureNumberAddressesStored": h3cSecureNumberAddressesStored,
       "h3cSecureMaximumAddresses": h3cSecureMaximumAddresses,
       "h3cSecureAddressTable": h3cSecureAddressTable,
       "h3cSecureAddressEntry": h3cSecureAddressEntry,
       "h3cSecureAddrMAC": h3cSecureAddrMAC,
       "h3cSecureAddrVlanID": h3cSecureAddrVlanID,
       "h3cSecureAddrMACStatus": h3cSecureAddrMACStatus,
       "h3cSecureAddrRowStatus": h3cSecureAddrRowStatus,
       "h3cSecureOUITable": h3cSecureOUITable,
       "h3cSecureOUIEntry": h3cSecureOUIEntry,
       "h3cSecureOUIIndex": h3cSecureOUIIndex,
       "h3cSecureOUI": h3cSecureOUI,
       "h3cSecureOUIRowStatus": h3cSecureOUIRowStatus,
       "h3cSecureBindingTable": h3cSecureBindingTable,
       "h3cSecureBindingEntry": h3cSecureBindingEntry,
       "h3cSecureBindingIndex": h3cSecureBindingIndex,
       "h3cSecureBindingPort": h3cSecureBindingPort,
       "h3cSecureBindingAddrMAC": h3cSecureBindingAddrMAC,
       "h3cSecureBindingAddrIp": h3cSecureBindingAddrIp,
       "h3cSecureBindingRowStatus": h3cSecureBindingRowStatus,
       "h3cSecureAssignTable": h3cSecureAssignTable,
       "h3cSecureAssignEntry": h3cSecureAssignEntry,
       "h3cSecureAssignEnable": h3cSecureAssignEnable,
       "h3cSecureVlanAssignment": h3cSecureVlanAssignment,
       "h3cPortSecurityNotifications": h3cPortSecurityNotifications,
       "h3cSecureAddressLearned": h3cSecureAddressLearned,
       "h3cSecureViolation": h3cSecureViolation,
       "h3cSecureLoginFailure": h3cSecureLoginFailure,
       "h3cSecureLogon": h3cSecureLogon,
       "h3cSecureLogoff": h3cSecureLogoff,
       "h3cSecureRalmLoginFailure": h3cSecureRalmLoginFailure,
       "h3cSecureRalmLogon": h3cSecureRalmLogon,
       "h3cSecureRalmLogoff": h3cSecureRalmLogoff}
)
