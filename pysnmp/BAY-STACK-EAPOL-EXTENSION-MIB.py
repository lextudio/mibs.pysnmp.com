# SNMP MIB module (BAY-STACK-EAPOL-EXTENSION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BAY-STACK-EAPOL-EXTENSION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:54 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(VlanId,
 VlanIdOrAny,
 VlanIdOrNone) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId",
    "VlanIdOrAny",
    "VlanIdOrNone")

(LPortSet,) = mibBuilder.importSymbols(
    "RAPID-CITY",
    "LPortSet")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(bayStackMibs,) = mibBuilder.importSymbols(
    "SYNOPTICS-ROOT-MIB",
    "bayStackMibs")


# MODULE-IDENTITY

bayStackEapExtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 3)
)
bayStackEapExtMib.setRevisions(
        ("2015-09-10 00:00",
         "2015-08-05 00:00",
         "2015-07-20 00:00",
         "2015-03-31 00:00",
         "2014-12-22 00:00",
         "2014-09-01 00:00",
         "2013-03-04 00:00",
         "2013-02-08 00:00",
         "2013-01-17 00:00",
         "2012-11-27 00:00",
         "2012-11-05 00:00",
         "2012-08-01 00:00",
         "2012-05-23 00:00",
         "2012-03-01 00:00",
         "2011-10-06 00:00",
         "2011-07-22 00:00",
         "2011-06-26 00:00",
         "2010-09-07 00:00",
         "2010-01-25 00:00",
         "2010-01-11 00:00",
         "2008-11-11 00:00",
         "2008-07-03 00:00",
         "2008-06-30 00:00",
         "2008-04-14 00:00",
         "2008-03-28 00:00",
         "2007-11-09 00:00",
         "2006-11-01 00:00",
         "2006-05-24 00:00",
         "2005-06-27 00:00",
         "2005-03-10 00:00",
         "2005-02-17 00:00",
         "2004-11-11 00:00",
         "2004-08-31 00:00",
         "2004-07-20 00:00",
         "2003-09-18 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BseeObjects_ObjectIdentity = ObjectIdentity
bseeObjects = _BseeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 1)
)
_BseeUserBasedPoliciesEnabled_Type = TruthValue
_BseeUserBasedPoliciesEnabled_Object = MibScalar
bseeUserBasedPoliciesEnabled = _BseeUserBasedPoliciesEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 1, 1),
    _BseeUserBasedPoliciesEnabled_Type()
)
bseeUserBasedPoliciesEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bseeUserBasedPoliciesEnabled.setStatus("current")
_BseeGuestVlanId_Type = VlanId
_BseeGuestVlanId_Object = MibScalar
bseeGuestVlanId = _BseeGuestVlanId_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 1, 2),
    _BseeGuestVlanId_Type()
)
bseeGuestVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bseeGuestVlanId.setStatus("current")
_BseeRemediationVlanId_Type = VlanId
_BseeRemediationVlanId_Object = MibScalar
bseeRemediationVlanId = _BseeRemediationVlanId_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 1, 3),
    _BseeRemediationVlanId_Type()
)
bseeRemediationVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bseeRemediationVlanId.setStatus("current")


class _BseeMaximumEapClientMacs_Type(Integer32):
    """Custom type bseeMaximumEapClientMacs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 800),
    )


_BseeMaximumEapClientMacs_Type.__name__ = "Integer32"
_BseeMaximumEapClientMacs_Object = MibScalar
bseeMaximumEapClientMacs = _BseeMaximumEapClientMacs_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 1, 4),
    _BseeMaximumEapClientMacs_Type()
)
bseeMaximumEapClientMacs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bseeMaximumEapClientMacs.setStatus("current")


class _BseeMaximumNonEapClientMacs_Type(Integer32):
    """Custom type bseeMaximumNonEapClientMacs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 800),
    )


_BseeMaximumNonEapClientMacs_Type.__name__ = "Integer32"
_BseeMaximumNonEapClientMacs_Object = MibScalar
bseeMaximumNonEapClientMacs = _BseeMaximumNonEapClientMacs_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 1, 5),
    _BseeMaximumNonEapClientMacs_Type()
)
bseeMaximumNonEapClientMacs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bseeMaximumNonEapClientMacs.setStatus("current")
_BseeGuestVlanEnabled_Type = TruthValue
_BseeGuestVlanEnabled_Object = MibScalar
bseeGuestVlanEnabled = _BseeGuestVlanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 1, 6),
    _BseeGuestVlanEnabled_Type()
)
bseeGuestVlanEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bseeGuestVlanEnabled.setStatus("current")
_BseeRemediationVlanEnabled_Type = TruthValue
_BseeRemediationVlanEnabled_Object = MibScalar
bseeRemediationVlanEnabled = _BseeRemediationVlanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 1, 7),
    _BseeRemediationVlanEnabled_Type()
)
bseeRemediationVlanEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bseeRemediationVlanEnabled.setStatus("current")


class _BseeMultiHostAllowNonEapClient_Type(TruthValue):
    """Custom type bseeMultiHostAllowNonEapClient based on TruthValue"""


_BseeMultiHostAllowNonEapClient_Object = MibScalar
bseeMultiHostAllowNonEapClient = _BseeMultiHostAllowNonEapClient_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 1, 8),
    _BseeMultiHostAllowNonEapClient_Type()
)
bseeMultiHostAllowNonEapClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bseeMultiHostAllowNonEapClient.setStatus("current")


class _BseeMultiHostRadiusAuthNonEapClient_Type(TruthValue):
    """Custom type bseeMultiHostRadiusAuthNonEapClient based on TruthValue"""


_BseeMultiHostRadiusAuthNonEapClient_Object = MibScalar
bseeMultiHostRadiusAuthNonEapClient = _BseeMultiHostRadiusAuthNonEapClient_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 1, 9),
    _BseeMultiHostRadiusAuthNonEapClient_Type()
)
bseeMultiHostRadiusAuthNonEapClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bseeMultiHostRadiusAuthNonEapClient.setStatus("current")


class _BseeMultiHostSingleAuthEnabled_Type(TruthValue):
    """Custom type bseeMultiHostSingleAuthEnabled based on TruthValue"""


_BseeMultiHostSingleAuthEnabled_Object = MibScalar
bseeMultiHostSingleAuthEnabled = _BseeMultiHostSingleAuthEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 1, 10),
    _BseeMultiHostSingleAuthEnabled_Type()
)
bseeMultiHostSingleAuthEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bseeMultiHostSingleAuthEnabled.setStatus("current")
_BseeUserBasedPoliciesFilterOnMac_Type = TruthValue
_BseeUserBasedPoliciesFilterOnMac_Object = MibScalar
bseeUserBasedPoliciesFilterOnMac = _BseeUserBasedPoliciesFilterOnMac_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 1, 11),
    _BseeUserBasedPoliciesFilterOnMac_Type()
)
bseeUserBasedPoliciesFilterOnMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bseeUserBasedPoliciesFilterOnMac.setStatus("current")
_BseeMultiHostNonEapUserBasedPoliciesEnabled_Type = TruthValue
_BseeMultiHostNonEapUserBasedPoliciesEnabled_Object = MibScalar
bseeMultiHostNonEapUserBasedPoliciesEnabled = _BseeMultiHostNonEapUserBasedPoliciesEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 1, 12),
    _BseeMultiHostNonEapUserBasedPoliciesEnabled_Type()
)
bseeMultiHostNonEapUserBasedPoliciesEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bseeMultiHostNonEapUserBasedPoliciesEnabled.setStatus("current")
_BseeMultiHostNonEapUserBasedPoliciesFilterOnMac_Type = TruthValue
_BseeMultiHostNonEapUserBasedPoliciesFilterOnMac_Object = MibScalar
bseeMultiHostNonEapUserBasedPoliciesFilterOnMac = _BseeMultiHostNonEapUserBasedPoliciesFilterOnMac_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 1, 13),
    _BseeMultiHostNonEapUserBasedPoliciesFilterOnMac_Type()
)
bseeMultiHostNonEapUserBasedPoliciesFilterOnMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bseeMultiHostNonEapUserBasedPoliciesFilterOnMac.setStatus("current")


class _BseeMultihostNonEapRadiusPasswordAttributeFormat_Type(Bits):
    """Custom type bseeMultihostNonEapRadiusPasswordAttributeFormat based on Bits"""
    namedValues = NamedValues(
        *(("ipAddr", 0),
          ("key", 3),
          ("macAddr", 1),
          ("padding", 4),
          ("portNumber", 2))
    )

_BseeMultihostNonEapRadiusPasswordAttributeFormat_Type.__name__ = "Bits"
_BseeMultihostNonEapRadiusPasswordAttributeFormat_Object = MibScalar
bseeMultihostNonEapRadiusPasswordAttributeFormat = _BseeMultihostNonEapRadiusPasswordAttributeFormat_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 1, 14),
    _BseeMultihostNonEapRadiusPasswordAttributeFormat_Type()
)
bseeMultihostNonEapRadiusPasswordAttributeFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bseeMultihostNonEapRadiusPasswordAttributeFormat.setStatus("current")


class _BseeMultiHostAllowNonEapPhones_Type(TruthValue):
    """Custom type bseeMultiHostAllowNonEapPhones based on TruthValue"""


_BseeMultiHostAllowNonEapPhones_Object = MibScalar
bseeMultiHostAllowNonEapPhones = _BseeMultiHostAllowNonEapPhones_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 1, 15),
    _BseeMultiHostAllowNonEapPhones_Type()
)
bseeMultiHostAllowNonEapPhones.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bseeMultiHostAllowNonEapPhones.setStatus("current")


class _BseeMultiHostAllowRadiusAssignedVlan_Type(TruthValue):
    """Custom type bseeMultiHostAllowRadiusAssignedVlan based on TruthValue"""


_BseeMultiHostAllowRadiusAssignedVlan_Object = MibScalar
bseeMultiHostAllowRadiusAssignedVlan = _BseeMultiHostAllowRadiusAssignedVlan_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 1, 16),
    _BseeMultiHostAllowRadiusAssignedVlan_Type()
)
bseeMultiHostAllowRadiusAssignedVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bseeMultiHostAllowRadiusAssignedVlan.setStatus("current")


class _BseeMultiHostEapPacketMode_Type(Integer32):
    """Custom type bseeMultiHostEapPacketMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multicast", 1),
          ("unicast", 2))
    )


_BseeMultiHostEapPacketMode_Type.__name__ = "Integer32"
_BseeMultiHostEapPacketMode_Object = MibScalar
bseeMultiHostEapPacketMode = _BseeMultiHostEapPacketMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 1, 17),
    _BseeMultiHostEapPacketMode_Type()
)
bseeMultiHostEapPacketMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bseeMultiHostEapPacketMode.setStatus("current")


class _BseeMultiHostEapRadiusTimeoutMode_Type(Integer32):
    """Custom type bseeMultiHostEapRadiusTimeoutMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doNotFail", 2),
          ("fail", 1))
    )


_BseeMultiHostEapRadiusTimeoutMode_Type.__name__ = "Integer32"
_BseeMultiHostEapRadiusTimeoutMode_Object = MibScalar
bseeMultiHostEapRadiusTimeoutMode = _BseeMultiHostEapRadiusTimeoutMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 1, 18),
    _BseeMultiHostEapRadiusTimeoutMode_Type()
)
bseeMultiHostEapRadiusTimeoutMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bseeMultiHostEapRadiusTimeoutMode.setStatus("current")


class _BseeMultiHostAllowNonEapRadiusAssignedVlan_Type(TruthValue):
    """Custom type bseeMultiHostAllowNonEapRadiusAssignedVlan based on TruthValue"""


_BseeMultiHostAllowNonEapRadiusAssignedVlan_Object = MibScalar
bseeMultiHostAllowNonEapRadiusAssignedVlan = _BseeMultiHostAllowNonEapRadiusAssignedVlan_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 1, 19),
    _BseeMultiHostAllowNonEapRadiusAssignedVlan_Type()
)
bseeMultiHostAllowNonEapRadiusAssignedVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bseeMultiHostAllowNonEapRadiusAssignedVlan.setStatus("current")


class _BseeMultiHostEapProtocolEnabled_Type(TruthValue):
    """Custom type bseeMultiHostEapProtocolEnabled based on TruthValue"""


_BseeMultiHostEapProtocolEnabled_Object = MibScalar
bseeMultiHostEapProtocolEnabled = _BseeMultiHostEapProtocolEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 1, 20),
    _BseeMultiHostEapProtocolEnabled_Type()
)
bseeMultiHostEapProtocolEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bseeMultiHostEapProtocolEnabled.setStatus("current")


class _BseeMultiHostUseMostRecentRadiusAssignedVlan_Type(TruthValue):
    """Custom type bseeMultiHostUseMostRecentRadiusAssignedVlan based on TruthValue"""


_BseeMultiHostUseMostRecentRadiusAssignedVlan_Object = MibScalar
bseeMultiHostUseMostRecentRadiusAssignedVlan = _BseeMultiHostUseMostRecentRadiusAssignedVlan_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 1, 21),
    _BseeMultiHostUseMostRecentRadiusAssignedVlan_Type()
)
bseeMultiHostUseMostRecentRadiusAssignedVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bseeMultiHostUseMostRecentRadiusAssignedVlan.setStatus("current")
_BseeMultiHostFailOpenVlanId_Type = VlanId
_BseeMultiHostFailOpenVlanId_Object = MibScalar
bseeMultiHostFailOpenVlanId = _BseeMultiHostFailOpenVlanId_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 1, 22),
    _BseeMultiHostFailOpenVlanId_Type()
)
bseeMultiHostFailOpenVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bseeMultiHostFailOpenVlanId.setStatus("current")
_BseeMultiHostFailOpenVlanEnabled_Type = TruthValue
_BseeMultiHostFailOpenVlanEnabled_Object = MibScalar
bseeMultiHostFailOpenVlanEnabled = _BseeMultiHostFailOpenVlanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 1, 23),
    _BseeMultiHostFailOpenVlanEnabled_Type()
)
bseeMultiHostFailOpenVlanEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bseeMultiHostFailOpenVlanEnabled.setStatus("current")
_BseeMultiHostMultiVlan_Type = TruthValue
_BseeMultiHostMultiVlan_Object = MibScalar
bseeMultiHostMultiVlan = _BseeMultiHostMultiVlan_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 1, 24),
    _BseeMultiHostMultiVlan_Type()
)
bseeMultiHostMultiVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bseeMultiHostMultiVlan.setStatus("current")
_BseeMultiHostNeapReauthenticationEnabled_Type = TruthValue
_BseeMultiHostNeapReauthenticationEnabled_Object = MibScalar
bseeMultiHostNeapReauthenticationEnabled = _BseeMultiHostNeapReauthenticationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 1, 25),
    _BseeMultiHostNeapReauthenticationEnabled_Type()
)
bseeMultiHostNeapReauthenticationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bseeMultiHostNeapReauthenticationEnabled.setStatus("current")


class _BseeMultiHostBlockDifferentVlanAuth_Type(TruthValue):
    """Custom type bseeMultiHostBlockDifferentVlanAuth based on TruthValue"""


_BseeMultiHostBlockDifferentVlanAuth_Object = MibScalar
bseeMultiHostBlockDifferentVlanAuth = _BseeMultiHostBlockDifferentVlanAuth_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 1, 26),
    _BseeMultiHostBlockDifferentVlanAuth_Type()
)
bseeMultiHostBlockDifferentVlanAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bseeMultiHostBlockDifferentVlanAuth.setStatus("current")
_BseeMultiHostAdacDummyRadiusRequests_Type = TruthValue
_BseeMultiHostAdacDummyRadiusRequests_Object = MibScalar
bseeMultiHostAdacDummyRadiusRequests = _BseeMultiHostAdacDummyRadiusRequests_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 1, 27),
    _BseeMultiHostAdacDummyRadiusRequests_Type()
)
bseeMultiHostAdacDummyRadiusRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bseeMultiHostAdacDummyRadiusRequests.setStatus("current")
_BseeAllowPortMirroringOnEap_Type = TruthValue
_BseeAllowPortMirroringOnEap_Object = MibScalar
bseeAllowPortMirroringOnEap = _BseeAllowPortMirroringOnEap_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 1, 28),
    _BseeAllowPortMirroringOnEap_Type()
)
bseeAllowPortMirroringOnEap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bseeAllowPortMirroringOnEap.setStatus("current")
_BseeMultiHostAdacNonEapEnabled_Type = TruthValue
_BseeMultiHostAdacNonEapEnabled_Object = MibScalar
bseeMultiHostAdacNonEapEnabled = _BseeMultiHostAdacNonEapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 1, 29),
    _BseeMultiHostAdacNonEapEnabled_Type()
)
bseeMultiHostAdacNonEapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bseeMultiHostAdacNonEapEnabled.setStatus("current")


class _BseeMultiHostFailOpenVlanContinuityModeEnabled_Type(TruthValue):
    """Custom type bseeMultiHostFailOpenVlanContinuityModeEnabled based on TruthValue"""


_BseeMultiHostFailOpenVlanContinuityModeEnabled_Object = MibScalar
bseeMultiHostFailOpenVlanContinuityModeEnabled = _BseeMultiHostFailOpenVlanContinuityModeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 1, 30),
    _BseeMultiHostFailOpenVlanContinuityModeEnabled_Type()
)
bseeMultiHostFailOpenVlanContinuityModeEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bseeMultiHostFailOpenVlanContinuityModeEnabled.setStatus("current")


class _BseeMultiHostNonEapRadiusPasswordFreeformKey_Type(OctetString):
    """Custom type bseeMultiHostNonEapRadiusPasswordFreeformKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BseeMultiHostNonEapRadiusPasswordFreeformKey_Type.__name__ = "OctetString"
_BseeMultiHostNonEapRadiusPasswordFreeformKey_Object = MibScalar
bseeMultiHostNonEapRadiusPasswordFreeformKey = _BseeMultiHostNonEapRadiusPasswordFreeformKey_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 1, 31),
    _BseeMultiHostNonEapRadiusPasswordFreeformKey_Type()
)
bseeMultiHostNonEapRadiusPasswordFreeformKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bseeMultiHostNonEapRadiusPasswordFreeformKey.setStatus("current")


class _BseeMultiHostFailOpenVlanDisableEapMode_Type(TruthValue):
    """Custom type bseeMultiHostFailOpenVlanDisableEapMode based on TruthValue"""


_BseeMultiHostFailOpenVlanDisableEapMode_Object = MibScalar
bseeMultiHostFailOpenVlanDisableEapMode = _BseeMultiHostFailOpenVlanDisableEapMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 1, 32),
    _BseeMultiHostFailOpenVlanDisableEapMode_Type()
)
bseeMultiHostFailOpenVlanDisableEapMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bseeMultiHostFailOpenVlanDisableEapMode.setStatus("current")


class _BseePaeSystemOperState_Type(Integer32):
    """Custom type bseePaeSystemOperState based on Integer32"""
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


_BseePaeSystemOperState_Type.__name__ = "Integer32"
_BseePaeSystemOperState_Object = MibScalar
bseePaeSystemOperState = _BseePaeSystemOperState_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 1, 33),
    _BseePaeSystemOperState_Type()
)
bseePaeSystemOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bseePaeSystemOperState.setStatus("current")


class _BseeDefaultEapAll_Type(TruthValue):
    """Custom type bseeDefaultEapAll based on TruthValue"""


_BseeDefaultEapAll_Object = MibScalar
bseeDefaultEapAll = _BseeDefaultEapAll_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 1, 34),
    _BseeDefaultEapAll_Type()
)
bseeDefaultEapAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bseeDefaultEapAll.setStatus("current")
_BseeAutoPortConfigModeSwitchToMHMV_Type = LPortSet
_BseeAutoPortConfigModeSwitchToMHMV_Object = MibScalar
bseeAutoPortConfigModeSwitchToMHMV = _BseeAutoPortConfigModeSwitchToMHMV_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 1, 35),
    _BseeAutoPortConfigModeSwitchToMHMV_Type()
)
bseeAutoPortConfigModeSwitchToMHMV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bseeAutoPortConfigModeSwitchToMHMV.setStatus("current")


class _BseeAutoPortConfigModeSwitchToMHMVAction_Type(Integer32):
    """Custom type bseeAutoPortConfigModeSwitchToMHMVAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("apply", 2),
          ("none", 1))
    )


_BseeAutoPortConfigModeSwitchToMHMVAction_Type.__name__ = "Integer32"
_BseeAutoPortConfigModeSwitchToMHMVAction_Object = MibScalar
bseeAutoPortConfigModeSwitchToMHMVAction = _BseeAutoPortConfigModeSwitchToMHMVAction_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 1, 36),
    _BseeAutoPortConfigModeSwitchToMHMVAction_Type()
)
bseeAutoPortConfigModeSwitchToMHMVAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bseeAutoPortConfigModeSwitchToMHMVAction.setStatus("current")


class _BseeAutoPortConfigModeSwitchToMHMVStatus_Type(Integer32):
    """Custom type bseeAutoPortConfigModeSwitchToMHMVStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 3),
          ("inProgress", 2),
          ("passed", 1))
    )


_BseeAutoPortConfigModeSwitchToMHMVStatus_Type.__name__ = "Integer32"
_BseeAutoPortConfigModeSwitchToMHMVStatus_Object = MibScalar
bseeAutoPortConfigModeSwitchToMHMVStatus = _BseeAutoPortConfigModeSwitchToMHMVStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 1, 37),
    _BseeAutoPortConfigModeSwitchToMHMVStatus_Type()
)
bseeAutoPortConfigModeSwitchToMHMVStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bseeAutoPortConfigModeSwitchToMHMVStatus.setStatus("current")
_BseeNotifications_ObjectIdentity = ObjectIdentity
bseeNotifications = _BseeNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 2)
)
_BseeNotifications0_ObjectIdentity = ObjectIdentity
bseeNotifications0 = _BseeNotifications0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 2, 0)
)
_BseePortConfigTable_Object = MibTable
bseePortConfigTable = _BseePortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 3)
)
if mibBuilder.loadTexts:
    bseePortConfigTable.setStatus("current")
_BseePortConfigEntry_Object = MibTableRow
bseePortConfigEntry = _BseePortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 3, 1)
)
bseePortConfigEntry.setIndexNames(
    (0, "BAY-STACK-EAPOL-EXTENSION-MIB", "bseePortConfigPortNumber"),
)
if mibBuilder.loadTexts:
    bseePortConfigEntry.setStatus("current")
_BseePortConfigPortNumber_Type = InterfaceIndex
_BseePortConfigPortNumber_Object = MibTableColumn
bseePortConfigPortNumber = _BseePortConfigPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 3, 1, 1),
    _BseePortConfigPortNumber_Type()
)
bseePortConfigPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bseePortConfigPortNumber.setStatus("current")


class _BseePortConfigGuestVlanId_Type(VlanIdOrNone):
    """Custom type bseePortConfigGuestVlanId based on VlanIdOrNone"""
    defaultValue = 0


_BseePortConfigGuestVlanId_Object = MibTableColumn
bseePortConfigGuestVlanId = _BseePortConfigGuestVlanId_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 3, 1, 2),
    _BseePortConfigGuestVlanId_Type()
)
bseePortConfigGuestVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bseePortConfigGuestVlanId.setStatus("current")


class _BseePortConfigMultiHostEnabled_Type(TruthValue):
    """Custom type bseePortConfigMultiHostEnabled based on TruthValue"""


_BseePortConfigMultiHostEnabled_Object = MibTableColumn
bseePortConfigMultiHostEnabled = _BseePortConfigMultiHostEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 3, 1, 3),
    _BseePortConfigMultiHostEnabled_Type()
)
bseePortConfigMultiHostEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bseePortConfigMultiHostEnabled.setStatus("current")


class _BseePortConfigMultiHostEapMaxNumMacs_Type(Integer32):
    """Custom type bseePortConfigMultiHostEapMaxNumMacs based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_BseePortConfigMultiHostEapMaxNumMacs_Type.__name__ = "Integer32"
_BseePortConfigMultiHostEapMaxNumMacs_Object = MibTableColumn
bseePortConfigMultiHostEapMaxNumMacs = _BseePortConfigMultiHostEapMaxNumMacs_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 3, 1, 4),
    _BseePortConfigMultiHostEapMaxNumMacs_Type()
)
bseePortConfigMultiHostEapMaxNumMacs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bseePortConfigMultiHostEapMaxNumMacs.setStatus("current")


class _BseePortConfigMultiHostAllowNonEapClient_Type(TruthValue):
    """Custom type bseePortConfigMultiHostAllowNonEapClient based on TruthValue"""


_BseePortConfigMultiHostAllowNonEapClient_Object = MibTableColumn
bseePortConfigMultiHostAllowNonEapClient = _BseePortConfigMultiHostAllowNonEapClient_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 3, 1, 5),
    _BseePortConfigMultiHostAllowNonEapClient_Type()
)
bseePortConfigMultiHostAllowNonEapClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bseePortConfigMultiHostAllowNonEapClient.setStatus("current")


class _BseePortConfigMultiHostNonEapMacSource_Type(Integer32):
    """Custom type bseePortConfigMultiHostNonEapMacSource based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autoLearn", 1),
          ("radius", 3),
          ("userConfig", 2))
    )


_BseePortConfigMultiHostNonEapMacSource_Type.__name__ = "Integer32"
_BseePortConfigMultiHostNonEapMacSource_Object = MibTableColumn
bseePortConfigMultiHostNonEapMacSource = _BseePortConfigMultiHostNonEapMacSource_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 3, 1, 6),
    _BseePortConfigMultiHostNonEapMacSource_Type()
)
bseePortConfigMultiHostNonEapMacSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bseePortConfigMultiHostNonEapMacSource.setStatus("deprecated")


class _BseePortConfigMultiHostNonEapMaxNumMacs_Type(Integer32):
    """Custom type bseePortConfigMultiHostNonEapMaxNumMacs based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_BseePortConfigMultiHostNonEapMaxNumMacs_Type.__name__ = "Integer32"
_BseePortConfigMultiHostNonEapMaxNumMacs_Object = MibTableColumn
bseePortConfigMultiHostNonEapMaxNumMacs = _BseePortConfigMultiHostNonEapMaxNumMacs_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 3, 1, 7),
    _BseePortConfigMultiHostNonEapMaxNumMacs_Type()
)
bseePortConfigMultiHostNonEapMaxNumMacs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bseePortConfigMultiHostNonEapMaxNumMacs.setStatus("current")


class _BseePortConfigGuestVlanEnabled_Type(TruthValue):
    """Custom type bseePortConfigGuestVlanEnabled based on TruthValue"""


_BseePortConfigGuestVlanEnabled_Object = MibTableColumn
bseePortConfigGuestVlanEnabled = _BseePortConfigGuestVlanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 3, 1, 8),
    _BseePortConfigGuestVlanEnabled_Type()
)
bseePortConfigGuestVlanEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bseePortConfigGuestVlanEnabled.setStatus("current")


class _BseePortConfigMultiHostRadiusAuthNonEapClient_Type(TruthValue):
    """Custom type bseePortConfigMultiHostRadiusAuthNonEapClient based on TruthValue"""


_BseePortConfigMultiHostRadiusAuthNonEapClient_Object = MibTableColumn
bseePortConfigMultiHostRadiusAuthNonEapClient = _BseePortConfigMultiHostRadiusAuthNonEapClient_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 3, 1, 9),
    _BseePortConfigMultiHostRadiusAuthNonEapClient_Type()
)
bseePortConfigMultiHostRadiusAuthNonEapClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bseePortConfigMultiHostRadiusAuthNonEapClient.setStatus("current")


class _BseePortConfigMultiHostSingleAuthEnabled_Type(TruthValue):
    """Custom type bseePortConfigMultiHostSingleAuthEnabled based on TruthValue"""


_BseePortConfigMultiHostSingleAuthEnabled_Object = MibTableColumn
bseePortConfigMultiHostSingleAuthEnabled = _BseePortConfigMultiHostSingleAuthEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 3, 1, 10),
    _BseePortConfigMultiHostSingleAuthEnabled_Type()
)
bseePortConfigMultiHostSingleAuthEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bseePortConfigMultiHostSingleAuthEnabled.setStatus("current")


class _BseePortConfigMultiHostAllowNonEapPhones_Type(TruthValue):
    """Custom type bseePortConfigMultiHostAllowNonEapPhones based on TruthValue"""


_BseePortConfigMultiHostAllowNonEapPhones_Object = MibTableColumn
bseePortConfigMultiHostAllowNonEapPhones = _BseePortConfigMultiHostAllowNonEapPhones_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 3, 1, 11),
    _BseePortConfigMultiHostAllowNonEapPhones_Type()
)
bseePortConfigMultiHostAllowNonEapPhones.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bseePortConfigMultiHostAllowNonEapPhones.setStatus("current")


class _BseePortConfigMultiHostAllowRadiusAssignedVlan_Type(TruthValue):
    """Custom type bseePortConfigMultiHostAllowRadiusAssignedVlan based on TruthValue"""


_BseePortConfigMultiHostAllowRadiusAssignedVlan_Object = MibTableColumn
bseePortConfigMultiHostAllowRadiusAssignedVlan = _BseePortConfigMultiHostAllowRadiusAssignedVlan_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 3, 1, 12),
    _BseePortConfigMultiHostAllowRadiusAssignedVlan_Type()
)
bseePortConfigMultiHostAllowRadiusAssignedVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bseePortConfigMultiHostAllowRadiusAssignedVlan.setStatus("current")


class _BseePortConfigMultiHostEapPacketMode_Type(Integer32):
    """Custom type bseePortConfigMultiHostEapPacketMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multicast", 1),
          ("unicast", 2))
    )


_BseePortConfigMultiHostEapPacketMode_Type.__name__ = "Integer32"
_BseePortConfigMultiHostEapPacketMode_Object = MibTableColumn
bseePortConfigMultiHostEapPacketMode = _BseePortConfigMultiHostEapPacketMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 3, 1, 13),
    _BseePortConfigMultiHostEapPacketMode_Type()
)
bseePortConfigMultiHostEapPacketMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bseePortConfigMultiHostEapPacketMode.setStatus("current")


class _BseePortConfigMultiHostEapRadiusTimeoutMode_Type(Integer32):
    """Custom type bseePortConfigMultiHostEapRadiusTimeoutMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doNotFail", 2),
          ("fail", 1))
    )


_BseePortConfigMultiHostEapRadiusTimeoutMode_Type.__name__ = "Integer32"
_BseePortConfigMultiHostEapRadiusTimeoutMode_Object = MibTableColumn
bseePortConfigMultiHostEapRadiusTimeoutMode = _BseePortConfigMultiHostEapRadiusTimeoutMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 3, 1, 14),
    _BseePortConfigMultiHostEapRadiusTimeoutMode_Type()
)
bseePortConfigMultiHostEapRadiusTimeoutMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bseePortConfigMultiHostEapRadiusTimeoutMode.setStatus("current")


class _BseePortConfigMultiHostAllowNonEapRadiusAssignedVlan_Type(TruthValue):
    """Custom type bseePortConfigMultiHostAllowNonEapRadiusAssignedVlan based on TruthValue"""


_BseePortConfigMultiHostAllowNonEapRadiusAssignedVlan_Object = MibTableColumn
bseePortConfigMultiHostAllowNonEapRadiusAssignedVlan = _BseePortConfigMultiHostAllowNonEapRadiusAssignedVlan_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 3, 1, 15),
    _BseePortConfigMultiHostAllowNonEapRadiusAssignedVlan_Type()
)
bseePortConfigMultiHostAllowNonEapRadiusAssignedVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bseePortConfigMultiHostAllowNonEapRadiusAssignedVlan.setStatus("current")


class _BseePortConfigProcessRadiusRequestsServerPackets_Type(TruthValue):
    """Custom type bseePortConfigProcessRadiusRequestsServerPackets based on TruthValue"""


_BseePortConfigProcessRadiusRequestsServerPackets_Object = MibTableColumn
bseePortConfigProcessRadiusRequestsServerPackets = _BseePortConfigProcessRadiusRequestsServerPackets_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 3, 1, 16),
    _BseePortConfigProcessRadiusRequestsServerPackets_Type()
)
bseePortConfigProcessRadiusRequestsServerPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bseePortConfigProcessRadiusRequestsServerPackets.setStatus("current")


class _BseePortConfigEapProtocolEnabled_Type(TruthValue):
    """Custom type bseePortConfigEapProtocolEnabled based on TruthValue"""


_BseePortConfigEapProtocolEnabled_Object = MibTableColumn
bseePortConfigEapProtocolEnabled = _BseePortConfigEapProtocolEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 3, 1, 17),
    _BseePortConfigEapProtocolEnabled_Type()
)
bseePortConfigEapProtocolEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bseePortConfigEapProtocolEnabled.setStatus("current")


class _BseePortConfigMultiHostUseMostRecentRadiusAssignedVlan_Type(TruthValue):
    """Custom type bseePortConfigMultiHostUseMostRecentRadiusAssignedVlan based on TruthValue"""


_BseePortConfigMultiHostUseMostRecentRadiusAssignedVlan_Object = MibTableColumn
bseePortConfigMultiHostUseMostRecentRadiusAssignedVlan = _BseePortConfigMultiHostUseMostRecentRadiusAssignedVlan_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 3, 1, 18),
    _BseePortConfigMultiHostUseMostRecentRadiusAssignedVlan_Type()
)
bseePortConfigMultiHostUseMostRecentRadiusAssignedVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bseePortConfigMultiHostUseMostRecentRadiusAssignedVlan.setStatus("current")


class _BseePortConfigMultiHostClearNeap_Type(MacAddress):
    """Custom type bseePortConfigMultiHostClearNeap based on MacAddress"""
    defaultHexValue = "000000000000"


_BseePortConfigMultiHostClearNeap_Object = MibTableColumn
bseePortConfigMultiHostClearNeap = _BseePortConfigMultiHostClearNeap_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 3, 1, 19),
    _BseePortConfigMultiHostClearNeap_Type()
)
bseePortConfigMultiHostClearNeap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bseePortConfigMultiHostClearNeap.setStatus("current")


class _BseePortConfigMultiHostBlockDifferentVlanAuth_Type(TruthValue):
    """Custom type bseePortConfigMultiHostBlockDifferentVlanAuth based on TruthValue"""


_BseePortConfigMultiHostBlockDifferentVlanAuth_Object = MibTableColumn
bseePortConfigMultiHostBlockDifferentVlanAuth = _BseePortConfigMultiHostBlockDifferentVlanAuth_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 3, 1, 20),
    _BseePortConfigMultiHostBlockDifferentVlanAuth_Type()
)
bseePortConfigMultiHostBlockDifferentVlanAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bseePortConfigMultiHostBlockDifferentVlanAuth.setStatus("current")


class _BseePortConfigMultiHostAdacNonEapEnabled_Type(TruthValue):
    """Custom type bseePortConfigMultiHostAdacNonEapEnabled based on TruthValue"""


_BseePortConfigMultiHostAdacNonEapEnabled_Object = MibTableColumn
bseePortConfigMultiHostAdacNonEapEnabled = _BseePortConfigMultiHostAdacNonEapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 3, 1, 21),
    _BseePortConfigMultiHostAdacNonEapEnabled_Type()
)
bseePortConfigMultiHostAdacNonEapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bseePortConfigMultiHostAdacNonEapEnabled.setStatus("current")


class _BseePortConfigDefaultEapAll_Type(TruthValue):
    """Custom type bseePortConfigDefaultEapAll based on TruthValue"""


_BseePortConfigDefaultEapAll_Object = MibTableColumn
bseePortConfigDefaultEapAll = _BseePortConfigDefaultEapAll_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 3, 1, 22),
    _BseePortConfigDefaultEapAll_Type()
)
bseePortConfigDefaultEapAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bseePortConfigDefaultEapAll.setStatus("current")


class _BseePortConfigMultiHostMaxMacs_Type(Integer32):
    """Custom type bseePortConfigMultiHostMaxMacs based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_BseePortConfigMultiHostMaxMacs_Type.__name__ = "Integer32"
_BseePortConfigMultiHostMaxMacs_Object = MibTableColumn
bseePortConfigMultiHostMaxMacs = _BseePortConfigMultiHostMaxMacs_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 3, 1, 23),
    _BseePortConfigMultiHostMaxMacs_Type()
)
bseePortConfigMultiHostMaxMacs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bseePortConfigMultiHostMaxMacs.setStatus("current")


class _BseePortConfigMultiHostSingleAuthNoLimit_Type(TruthValue):
    """Custom type bseePortConfigMultiHostSingleAuthNoLimit based on TruthValue"""


_BseePortConfigMultiHostSingleAuthNoLimit_Object = MibTableColumn
bseePortConfigMultiHostSingleAuthNoLimit = _BseePortConfigMultiHostSingleAuthNoLimit_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 3, 1, 24),
    _BseePortConfigMultiHostSingleAuthNoLimit_Type()
)
bseePortConfigMultiHostSingleAuthNoLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bseePortConfigMultiHostSingleAuthNoLimit.setStatus("current")


class _BseePortConfigFailOpenVlanId_Type(Integer32):
    """Custom type bseePortConfigFailOpenVlanId based on Integer32"""
    defaultValue = 0


_BseePortConfigFailOpenVlanId_Object = MibTableColumn
bseePortConfigFailOpenVlanId = _BseePortConfigFailOpenVlanId_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 3, 1, 25),
    _BseePortConfigFailOpenVlanId_Type()
)
bseePortConfigFailOpenVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bseePortConfigFailOpenVlanId.setStatus("current")


class _BseePortConfigFailOpenVlanEnabled_Type(TruthValue):
    """Custom type bseePortConfigFailOpenVlanEnabled based on TruthValue"""


_BseePortConfigFailOpenVlanEnabled_Object = MibTableColumn
bseePortConfigFailOpenVlanEnabled = _BseePortConfigFailOpenVlanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 3, 1, 26),
    _BseePortConfigFailOpenVlanEnabled_Type()
)
bseePortConfigFailOpenVlanEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bseePortConfigFailOpenVlanEnabled.setStatus("current")


class _BseePortConfigFailOpenVlanUBP_Type(OctetString):
    """Custom type bseePortConfigFailOpenVlanUBP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BseePortConfigFailOpenVlanUBP_Type.__name__ = "OctetString"
_BseePortConfigFailOpenVlanUBP_Object = MibTableColumn
bseePortConfigFailOpenVlanUBP = _BseePortConfigFailOpenVlanUBP_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 3, 1, 27),
    _BseePortConfigFailOpenVlanUBP_Type()
)
bseePortConfigFailOpenVlanUBP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bseePortConfigFailOpenVlanUBP.setStatus("current")
_BseeMultiHostStatusTable_Object = MibTable
bseeMultiHostStatusTable = _BseeMultiHostStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 4)
)
if mibBuilder.loadTexts:
    bseeMultiHostStatusTable.setStatus("current")
_BseeMultiHostStatusEntry_Object = MibTableRow
bseeMultiHostStatusEntry = _BseeMultiHostStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 4, 1)
)
bseeMultiHostStatusEntry.setIndexNames(
    (0, "BAY-STACK-EAPOL-EXTENSION-MIB", "bseeMultiHostStatusPortNumber"),
    (0, "BAY-STACK-EAPOL-EXTENSION-MIB", "bseeMultiHostStatusClientMACAddr"),
)
if mibBuilder.loadTexts:
    bseeMultiHostStatusEntry.setStatus("current")
_BseeMultiHostStatusPortNumber_Type = InterfaceIndex
_BseeMultiHostStatusPortNumber_Object = MibTableColumn
bseeMultiHostStatusPortNumber = _BseeMultiHostStatusPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 4, 1, 1),
    _BseeMultiHostStatusPortNumber_Type()
)
bseeMultiHostStatusPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bseeMultiHostStatusPortNumber.setStatus("current")
_BseeMultiHostStatusClientMACAddr_Type = MacAddress
_BseeMultiHostStatusClientMACAddr_Object = MibTableColumn
bseeMultiHostStatusClientMACAddr = _BseeMultiHostStatusClientMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 4, 1, 2),
    _BseeMultiHostStatusClientMACAddr_Type()
)
bseeMultiHostStatusClientMACAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bseeMultiHostStatusClientMACAddr.setStatus("current")


class _BseeMultiHostStatusPaeState_Type(Integer32):
    """Custom type bseeMultiHostStatusPaeState based on Integer32"""
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
        *(("aborting", 6),
          ("authenticated", 5),
          ("authenticating", 4),
          ("connecting", 3),
          ("disconnected", 2),
          ("forceAuth", 8),
          ("forceUnauth", 9),
          ("held", 7),
          ("initialize", 1))
    )


_BseeMultiHostStatusPaeState_Type.__name__ = "Integer32"
_BseeMultiHostStatusPaeState_Object = MibTableColumn
bseeMultiHostStatusPaeState = _BseeMultiHostStatusPaeState_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 4, 1, 3),
    _BseeMultiHostStatusPaeState_Type()
)
bseeMultiHostStatusPaeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bseeMultiHostStatusPaeState.setStatus("current")


class _BseeMultiHostStatusBackendAuthState_Type(Integer32):
    """Custom type bseeMultiHostStatusBackendAuthState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("fail", 4),
          ("idle", 6),
          ("initialize", 7),
          ("request", 1),
          ("response", 2),
          ("success", 3),
          ("timeout", 5))
    )


_BseeMultiHostStatusBackendAuthState_Type.__name__ = "Integer32"
_BseeMultiHostStatusBackendAuthState_Object = MibTableColumn
bseeMultiHostStatusBackendAuthState = _BseeMultiHostStatusBackendAuthState_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 4, 1, 4),
    _BseeMultiHostStatusBackendAuthState_Type()
)
bseeMultiHostStatusBackendAuthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bseeMultiHostStatusBackendAuthState.setStatus("current")


class _BseeMultiHostStatusReauthenticate_Type(Integer32):
    """Custom type bseeMultiHostStatusReauthenticate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("reauthenticate", 2))
    )


_BseeMultiHostStatusReauthenticate_Type.__name__ = "Integer32"
_BseeMultiHostStatusReauthenticate_Object = MibTableColumn
bseeMultiHostStatusReauthenticate = _BseeMultiHostStatusReauthenticate_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 4, 1, 5),
    _BseeMultiHostStatusReauthenticate_Type()
)
bseeMultiHostStatusReauthenticate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bseeMultiHostStatusReauthenticate.setStatus("current")
_BseeMultiHostStatusVid_Type = VlanIdOrAny
_BseeMultiHostStatusVid_Object = MibTableColumn
bseeMultiHostStatusVid = _BseeMultiHostStatusVid_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 4, 1, 6),
    _BseeMultiHostStatusVid_Type()
)
bseeMultiHostStatusVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bseeMultiHostStatusVid.setStatus("current")


class _BseeMultiHostStatusPri_Type(Integer32):
    """Custom type bseeMultiHostStatusPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_BseeMultiHostStatusPri_Type.__name__ = "Integer32"
_BseeMultiHostStatusPri_Object = MibTableColumn
bseeMultiHostStatusPri = _BseeMultiHostStatusPri_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 4, 1, 7),
    _BseeMultiHostStatusPri_Type()
)
bseeMultiHostStatusPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bseeMultiHostStatusPri.setStatus("current")


class _BseeMultiHostStatusFaBindings_Type(OctetString):
    """Custom type bseeMultiHostStatusFaBindings based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 96),
    )


_BseeMultiHostStatusFaBindings_Type.__name__ = "OctetString"
_BseeMultiHostStatusFaBindings_Object = MibTableColumn
bseeMultiHostStatusFaBindings = _BseeMultiHostStatusFaBindings_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 4, 1, 8),
    _BseeMultiHostStatusFaBindings_Type()
)
bseeMultiHostStatusFaBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bseeMultiHostStatusFaBindings.setStatus("current")
_BseeMultiHostSessionStatsTable_Object = MibTable
bseeMultiHostSessionStatsTable = _BseeMultiHostSessionStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 5)
)
if mibBuilder.loadTexts:
    bseeMultiHostSessionStatsTable.setStatus("current")
_BseeMultiHostSessionStatsEntry_Object = MibTableRow
bseeMultiHostSessionStatsEntry = _BseeMultiHostSessionStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 5, 1)
)
bseeMultiHostSessionStatsEntry.setIndexNames(
    (0, "BAY-STACK-EAPOL-EXTENSION-MIB", "bseeMultiHostSessionStatsPortNumber"),
    (0, "BAY-STACK-EAPOL-EXTENSION-MIB", "bseeMultiHostSessionStatsClientMACAddr"),
)
if mibBuilder.loadTexts:
    bseeMultiHostSessionStatsEntry.setStatus("current")
_BseeMultiHostSessionStatsPortNumber_Type = InterfaceIndex
_BseeMultiHostSessionStatsPortNumber_Object = MibTableColumn
bseeMultiHostSessionStatsPortNumber = _BseeMultiHostSessionStatsPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 5, 1, 1),
    _BseeMultiHostSessionStatsPortNumber_Type()
)
bseeMultiHostSessionStatsPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bseeMultiHostSessionStatsPortNumber.setStatus("current")
_BseeMultiHostSessionStatsClientMACAddr_Type = MacAddress
_BseeMultiHostSessionStatsClientMACAddr_Object = MibTableColumn
bseeMultiHostSessionStatsClientMACAddr = _BseeMultiHostSessionStatsClientMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 5, 1, 2),
    _BseeMultiHostSessionStatsClientMACAddr_Type()
)
bseeMultiHostSessionStatsClientMACAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bseeMultiHostSessionStatsClientMACAddr.setStatus("current")
_BseeMultiHostSessionId_Type = SnmpAdminString
_BseeMultiHostSessionId_Object = MibTableColumn
bseeMultiHostSessionId = _BseeMultiHostSessionId_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 5, 1, 3),
    _BseeMultiHostSessionId_Type()
)
bseeMultiHostSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bseeMultiHostSessionId.setStatus("current")


class _BseeMultiHostSessionAuthenticMethod_Type(Integer32):
    """Custom type bseeMultiHostSessionAuthenticMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("localAuthServer", 2),
          ("remoteAuthServer", 1))
    )


_BseeMultiHostSessionAuthenticMethod_Type.__name__ = "Integer32"
_BseeMultiHostSessionAuthenticMethod_Object = MibTableColumn
bseeMultiHostSessionAuthenticMethod = _BseeMultiHostSessionAuthenticMethod_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 5, 1, 4),
    _BseeMultiHostSessionAuthenticMethod_Type()
)
bseeMultiHostSessionAuthenticMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bseeMultiHostSessionAuthenticMethod.setStatus("current")
_BseeMultiHostSessionTime_Type = TimeTicks
_BseeMultiHostSessionTime_Object = MibTableColumn
bseeMultiHostSessionTime = _BseeMultiHostSessionTime_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 5, 1, 5),
    _BseeMultiHostSessionTime_Type()
)
bseeMultiHostSessionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bseeMultiHostSessionTime.setStatus("current")


class _BseeMultiHostSessionTerminateCause_Type(Integer32):
    """Custom type bseeMultiHostSessionTerminateCause based on Integer32"""
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
              999)
        )
    )
    namedValues = NamedValues(
        *(("authControlForceUnauth", 5),
          ("notTerminatedYet", 999),
          ("portAdminDisabled", 7),
          ("portFailure", 2),
          ("portReInit", 6),
          ("reauthFailed", 4),
          ("supplicantLogoff", 1),
          ("supplicantRestart", 3))
    )


_BseeMultiHostSessionTerminateCause_Type.__name__ = "Integer32"
_BseeMultiHostSessionTerminateCause_Object = MibTableColumn
bseeMultiHostSessionTerminateCause = _BseeMultiHostSessionTerminateCause_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 5, 1, 6),
    _BseeMultiHostSessionTerminateCause_Type()
)
bseeMultiHostSessionTerminateCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bseeMultiHostSessionTerminateCause.setStatus("current")
_BseeMultiHostSessionUserName_Type = SnmpAdminString
_BseeMultiHostSessionUserName_Object = MibTableColumn
bseeMultiHostSessionUserName = _BseeMultiHostSessionUserName_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 5, 1, 7),
    _BseeMultiHostSessionUserName_Type()
)
bseeMultiHostSessionUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bseeMultiHostSessionUserName.setStatus("current")
_BseeMultiHostNonEapMacTable_Object = MibTable
bseeMultiHostNonEapMacTable = _BseeMultiHostNonEapMacTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 6)
)
if mibBuilder.loadTexts:
    bseeMultiHostNonEapMacTable.setStatus("current")
_BseeMultiHostNonEapMacEntry_Object = MibTableRow
bseeMultiHostNonEapMacEntry = _BseeMultiHostNonEapMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 6, 1)
)
bseeMultiHostNonEapMacEntry.setIndexNames(
    (0, "BAY-STACK-EAPOL-EXTENSION-MIB", "bseeMultiHostNonEapMacPortNumber"),
    (0, "BAY-STACK-EAPOL-EXTENSION-MIB", "bseeMultiHostNonEapMacClientMACAddr"),
)
if mibBuilder.loadTexts:
    bseeMultiHostNonEapMacEntry.setStatus("current")
_BseeMultiHostNonEapMacPortNumber_Type = InterfaceIndex
_BseeMultiHostNonEapMacPortNumber_Object = MibTableColumn
bseeMultiHostNonEapMacPortNumber = _BseeMultiHostNonEapMacPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 6, 1, 1),
    _BseeMultiHostNonEapMacPortNumber_Type()
)
bseeMultiHostNonEapMacPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bseeMultiHostNonEapMacPortNumber.setStatus("current")
_BseeMultiHostNonEapMacClientMACAddr_Type = MacAddress
_BseeMultiHostNonEapMacClientMACAddr_Object = MibTableColumn
bseeMultiHostNonEapMacClientMACAddr = _BseeMultiHostNonEapMacClientMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 6, 1, 2),
    _BseeMultiHostNonEapMacClientMACAddr_Type()
)
bseeMultiHostNonEapMacClientMACAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bseeMultiHostNonEapMacClientMACAddr.setStatus("current")
_BseeMultiHostNonEapMacRowStatus_Type = RowStatus
_BseeMultiHostNonEapMacRowStatus_Object = MibTableColumn
bseeMultiHostNonEapMacRowStatus = _BseeMultiHostNonEapMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 6, 1, 3),
    _BseeMultiHostNonEapMacRowStatus_Type()
)
bseeMultiHostNonEapMacRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bseeMultiHostNonEapMacRowStatus.setStatus("current")
_BseeMultiHostNonEapStatusTable_Object = MibTable
bseeMultiHostNonEapStatusTable = _BseeMultiHostNonEapStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 7)
)
if mibBuilder.loadTexts:
    bseeMultiHostNonEapStatusTable.setStatus("current")
_BseeMultiHostNonEapStatusEntry_Object = MibTableRow
bseeMultiHostNonEapStatusEntry = _BseeMultiHostNonEapStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 7, 1)
)
bseeMultiHostNonEapStatusEntry.setIndexNames(
    (0, "BAY-STACK-EAPOL-EXTENSION-MIB", "bseeMultiHostNonEapStatusPortNumber"),
    (0, "BAY-STACK-EAPOL-EXTENSION-MIB", "bseeMultiHostNonEapStatusClientMACAddr"),
)
if mibBuilder.loadTexts:
    bseeMultiHostNonEapStatusEntry.setStatus("current")
_BseeMultiHostNonEapStatusPortNumber_Type = InterfaceIndex
_BseeMultiHostNonEapStatusPortNumber_Object = MibTableColumn
bseeMultiHostNonEapStatusPortNumber = _BseeMultiHostNonEapStatusPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 7, 1, 1),
    _BseeMultiHostNonEapStatusPortNumber_Type()
)
bseeMultiHostNonEapStatusPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bseeMultiHostNonEapStatusPortNumber.setStatus("current")
_BseeMultiHostNonEapStatusClientMACAddr_Type = MacAddress
_BseeMultiHostNonEapStatusClientMACAddr_Object = MibTableColumn
bseeMultiHostNonEapStatusClientMACAddr = _BseeMultiHostNonEapStatusClientMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 7, 1, 2),
    _BseeMultiHostNonEapStatusClientMACAddr_Type()
)
bseeMultiHostNonEapStatusClientMACAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bseeMultiHostNonEapStatusClientMACAddr.setStatus("current")


class _BseeMultiHostNonEapStatusState_Type(Integer32):
    """Custom type bseeMultiHostNonEapStatusState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("adacAuthenticated", 5),
          ("lldpAuthenticated", 7),
          ("locallyAuthenticated", 2),
          ("mhsaAuthenticated", 6),
          ("radiusAuthenticated", 4),
          ("radiusPending", 3),
          ("rejected", 1))
    )


_BseeMultiHostNonEapStatusState_Type.__name__ = "Integer32"
_BseeMultiHostNonEapStatusState_Object = MibTableColumn
bseeMultiHostNonEapStatusState = _BseeMultiHostNonEapStatusState_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 7, 1, 3),
    _BseeMultiHostNonEapStatusState_Type()
)
bseeMultiHostNonEapStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bseeMultiHostNonEapStatusState.setStatus("current")


class _BseeMultiHostNonEapStatusReauthenticate_Type(Integer32):
    """Custom type bseeMultiHostNonEapStatusReauthenticate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("reauthenticate", 2))
    )


_BseeMultiHostNonEapStatusReauthenticate_Type.__name__ = "Integer32"
_BseeMultiHostNonEapStatusReauthenticate_Object = MibTableColumn
bseeMultiHostNonEapStatusReauthenticate = _BseeMultiHostNonEapStatusReauthenticate_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 7, 1, 4),
    _BseeMultiHostNonEapStatusReauthenticate_Type()
)
bseeMultiHostNonEapStatusReauthenticate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bseeMultiHostNonEapStatusReauthenticate.setStatus("current")
_BseeMultiHostNonEapStatusVid_Type = VlanIdOrAny
_BseeMultiHostNonEapStatusVid_Object = MibTableColumn
bseeMultiHostNonEapStatusVid = _BseeMultiHostNonEapStatusVid_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 7, 1, 5),
    _BseeMultiHostNonEapStatusVid_Type()
)
bseeMultiHostNonEapStatusVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bseeMultiHostNonEapStatusVid.setStatus("current")


class _BseeMultiHostNonEapStatusPri_Type(Integer32):
    """Custom type bseeMultiHostNonEapStatusPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_BseeMultiHostNonEapStatusPri_Type.__name__ = "Integer32"
_BseeMultiHostNonEapStatusPri_Object = MibTableColumn
bseeMultiHostNonEapStatusPri = _BseeMultiHostNonEapStatusPri_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 7, 1, 6),
    _BseeMultiHostNonEapStatusPri_Type()
)
bseeMultiHostNonEapStatusPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bseeMultiHostNonEapStatusPri.setStatus("current")


class _BseeMultiHostNonEapStatusFaBindings_Type(OctetString):
    """Custom type bseeMultiHostNonEapStatusFaBindings based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 96),
    )


_BseeMultiHostNonEapStatusFaBindings_Type.__name__ = "OctetString"
_BseeMultiHostNonEapStatusFaBindings_Object = MibTableColumn
bseeMultiHostNonEapStatusFaBindings = _BseeMultiHostNonEapStatusFaBindings_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 7, 1, 7),
    _BseeMultiHostNonEapStatusFaBindings_Type()
)
bseeMultiHostNonEapStatusFaBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bseeMultiHostNonEapStatusFaBindings.setStatus("current")
_BseeSupplicantObjects_ObjectIdentity = ObjectIdentity
bseeSupplicantObjects = _BseeSupplicantObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 8)
)
_BseeSupplicantEnabled_Type = TruthValue
_BseeSupplicantEnabled_Object = MibScalar
bseeSupplicantEnabled = _BseeSupplicantEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 8, 1),
    _BseeSupplicantEnabled_Type()
)
bseeSupplicantEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bseeSupplicantEnabled.setStatus("current")
_BseeSupplicantUserTable_Object = MibTable
bseeSupplicantUserTable = _BseeSupplicantUserTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 9)
)
if mibBuilder.loadTexts:
    bseeSupplicantUserTable.setStatus("current")
_BseeSupplicantUserEntry_Object = MibTableRow
bseeSupplicantUserEntry = _BseeSupplicantUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 9, 1)
)
bseeSupplicantUserEntry.setIndexNames(
    (0, "BAY-STACK-EAPOL-EXTENSION-MIB", "bseeSupplicantPortNumber"),
)
if mibBuilder.loadTexts:
    bseeSupplicantUserEntry.setStatus("current")
_BseeSupplicantPortNumber_Type = InterfaceIndex
_BseeSupplicantPortNumber_Object = MibTableColumn
bseeSupplicantPortNumber = _BseeSupplicantPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 9, 1, 1),
    _BseeSupplicantPortNumber_Type()
)
bseeSupplicantPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bseeSupplicantPortNumber.setStatus("current")


class _BseeSupplicantUserName_Type(SnmpAdminString):
    """Custom type bseeSupplicantUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_BseeSupplicantUserName_Type.__name__ = "SnmpAdminString"
_BseeSupplicantUserName_Object = MibTableColumn
bseeSupplicantUserName = _BseeSupplicantUserName_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 9, 1, 2),
    _BseeSupplicantUserName_Type()
)
bseeSupplicantUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bseeSupplicantUserName.setStatus("current")


class _BseeSupplicantPassword_Type(SnmpAdminString):
    """Custom type bseeSupplicantPassword based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_BseeSupplicantPassword_Type.__name__ = "SnmpAdminString"
_BseeSupplicantPassword_Object = MibTableColumn
bseeSupplicantPassword = _BseeSupplicantPassword_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 9, 1, 3),
    _BseeSupplicantPassword_Type()
)
bseeSupplicantPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bseeSupplicantPassword.setStatus("current")


class _BseeSupplicantUserState_Type(Integer32):
    """Custom type bseeSupplicantUserState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1),
          ("logoff", 3))
    )


_BseeSupplicantUserState_Type.__name__ = "Integer32"
_BseeSupplicantUserState_Object = MibTableColumn
bseeSupplicantUserState = _BseeSupplicantUserState_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 9, 1, 4),
    _BseeSupplicantUserState_Type()
)
bseeSupplicantUserState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bseeSupplicantUserState.setStatus("current")
_BseeMultiHostVoipVlanTable_Object = MibTable
bseeMultiHostVoipVlanTable = _BseeMultiHostVoipVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 10)
)
if mibBuilder.loadTexts:
    bseeMultiHostVoipVlanTable.setStatus("current")
_BseeMultiHostVoipVlanEntry_Object = MibTableRow
bseeMultiHostVoipVlanEntry = _BseeMultiHostVoipVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 10, 1)
)
bseeMultiHostVoipVlanEntry.setIndexNames(
    (0, "BAY-STACK-EAPOL-EXTENSION-MIB", "bseeMultiHostVoipVlanIndex"),
)
if mibBuilder.loadTexts:
    bseeMultiHostVoipVlanEntry.setStatus("current")


class _BseeMultiHostVoipVlanIndex_Type(Integer32):
    """Custom type bseeMultiHostVoipVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_BseeMultiHostVoipVlanIndex_Type.__name__ = "Integer32"
_BseeMultiHostVoipVlanIndex_Object = MibTableColumn
bseeMultiHostVoipVlanIndex = _BseeMultiHostVoipVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 10, 1, 1),
    _BseeMultiHostVoipVlanIndex_Type()
)
bseeMultiHostVoipVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bseeMultiHostVoipVlanIndex.setStatus("current")
_BseeMultiHostVoipVlanId_Type = VlanId
_BseeMultiHostVoipVlanId_Object = MibTableColumn
bseeMultiHostVoipVlanId = _BseeMultiHostVoipVlanId_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 10, 1, 2),
    _BseeMultiHostVoipVlanId_Type()
)
bseeMultiHostVoipVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bseeMultiHostVoipVlanId.setStatus("current")
_BseeMultiHostVoipVlanEnabled_Type = TruthValue
_BseeMultiHostVoipVlanEnabled_Object = MibTableColumn
bseeMultiHostVoipVlanEnabled = _BseeMultiHostVoipVlanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 10, 1, 3),
    _BseeMultiHostVoipVlanEnabled_Type()
)
bseeMultiHostVoipVlanEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bseeMultiHostVoipVlanEnabled.setStatus("current")
_BseeMultiHostDhcpAuthPhoneTable_Object = MibTable
bseeMultiHostDhcpAuthPhoneTable = _BseeMultiHostDhcpAuthPhoneTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 11)
)
if mibBuilder.loadTexts:
    bseeMultiHostDhcpAuthPhoneTable.setStatus("current")
_BseeMultiHostDhcpAuthPhoneEntry_Object = MibTableRow
bseeMultiHostDhcpAuthPhoneEntry = _BseeMultiHostDhcpAuthPhoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 11, 1)
)
bseeMultiHostDhcpAuthPhoneEntry.setIndexNames(
    (0, "BAY-STACK-EAPOL-EXTENSION-MIB", "bseeMultiHostDhcpAuthPhonePortNumber"),
    (0, "BAY-STACK-EAPOL-EXTENSION-MIB", "bseeMultiHostDhcpAuthPhoneClientMACAddr"),
)
if mibBuilder.loadTexts:
    bseeMultiHostDhcpAuthPhoneEntry.setStatus("current")
_BseeMultiHostDhcpAuthPhonePortNumber_Type = InterfaceIndex
_BseeMultiHostDhcpAuthPhonePortNumber_Object = MibTableColumn
bseeMultiHostDhcpAuthPhonePortNumber = _BseeMultiHostDhcpAuthPhonePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 11, 1, 1),
    _BseeMultiHostDhcpAuthPhonePortNumber_Type()
)
bseeMultiHostDhcpAuthPhonePortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bseeMultiHostDhcpAuthPhonePortNumber.setStatus("current")
_BseeMultiHostDhcpAuthPhoneClientMACAddr_Type = MacAddress
_BseeMultiHostDhcpAuthPhoneClientMACAddr_Object = MibTableColumn
bseeMultiHostDhcpAuthPhoneClientMACAddr = _BseeMultiHostDhcpAuthPhoneClientMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 11, 1, 2),
    _BseeMultiHostDhcpAuthPhoneClientMACAddr_Type()
)
bseeMultiHostDhcpAuthPhoneClientMACAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bseeMultiHostDhcpAuthPhoneClientMACAddr.setStatus("current")


class _BseeMultiHostDhcpAuthPhoneUserName_Type(SnmpAdminString):
    """Custom type bseeMultiHostDhcpAuthPhoneUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BseeMultiHostDhcpAuthPhoneUserName_Type.__name__ = "SnmpAdminString"
_BseeMultiHostDhcpAuthPhoneUserName_Object = MibTableColumn
bseeMultiHostDhcpAuthPhoneUserName = _BseeMultiHostDhcpAuthPhoneUserName_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 3, 11, 1, 3),
    _BseeMultiHostDhcpAuthPhoneUserName_Type()
)
bseeMultiHostDhcpAuthPhoneUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bseeMultiHostDhcpAuthPhoneUserName.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BAY-STACK-EAPOL-EXTENSION-MIB",
    **{"bayStackEapExtMib": bayStackEapExtMib,
       "bseeObjects": bseeObjects,
       "bseeUserBasedPoliciesEnabled": bseeUserBasedPoliciesEnabled,
       "bseeGuestVlanId": bseeGuestVlanId,
       "bseeRemediationVlanId": bseeRemediationVlanId,
       "bseeMaximumEapClientMacs": bseeMaximumEapClientMacs,
       "bseeMaximumNonEapClientMacs": bseeMaximumNonEapClientMacs,
       "bseeGuestVlanEnabled": bseeGuestVlanEnabled,
       "bseeRemediationVlanEnabled": bseeRemediationVlanEnabled,
       "bseeMultiHostAllowNonEapClient": bseeMultiHostAllowNonEapClient,
       "bseeMultiHostRadiusAuthNonEapClient": bseeMultiHostRadiusAuthNonEapClient,
       "bseeMultiHostSingleAuthEnabled": bseeMultiHostSingleAuthEnabled,
       "bseeUserBasedPoliciesFilterOnMac": bseeUserBasedPoliciesFilterOnMac,
       "bseeMultiHostNonEapUserBasedPoliciesEnabled": bseeMultiHostNonEapUserBasedPoliciesEnabled,
       "bseeMultiHostNonEapUserBasedPoliciesFilterOnMac": bseeMultiHostNonEapUserBasedPoliciesFilterOnMac,
       "bseeMultihostNonEapRadiusPasswordAttributeFormat": bseeMultihostNonEapRadiusPasswordAttributeFormat,
       "bseeMultiHostAllowNonEapPhones": bseeMultiHostAllowNonEapPhones,
       "bseeMultiHostAllowRadiusAssignedVlan": bseeMultiHostAllowRadiusAssignedVlan,
       "bseeMultiHostEapPacketMode": bseeMultiHostEapPacketMode,
       "bseeMultiHostEapRadiusTimeoutMode": bseeMultiHostEapRadiusTimeoutMode,
       "bseeMultiHostAllowNonEapRadiusAssignedVlan": bseeMultiHostAllowNonEapRadiusAssignedVlan,
       "bseeMultiHostEapProtocolEnabled": bseeMultiHostEapProtocolEnabled,
       "bseeMultiHostUseMostRecentRadiusAssignedVlan": bseeMultiHostUseMostRecentRadiusAssignedVlan,
       "bseeMultiHostFailOpenVlanId": bseeMultiHostFailOpenVlanId,
       "bseeMultiHostFailOpenVlanEnabled": bseeMultiHostFailOpenVlanEnabled,
       "bseeMultiHostMultiVlan": bseeMultiHostMultiVlan,
       "bseeMultiHostNeapReauthenticationEnabled": bseeMultiHostNeapReauthenticationEnabled,
       "bseeMultiHostBlockDifferentVlanAuth": bseeMultiHostBlockDifferentVlanAuth,
       "bseeMultiHostAdacDummyRadiusRequests": bseeMultiHostAdacDummyRadiusRequests,
       "bseeAllowPortMirroringOnEap": bseeAllowPortMirroringOnEap,
       "bseeMultiHostAdacNonEapEnabled": bseeMultiHostAdacNonEapEnabled,
       "bseeMultiHostFailOpenVlanContinuityModeEnabled": bseeMultiHostFailOpenVlanContinuityModeEnabled,
       "bseeMultiHostNonEapRadiusPasswordFreeformKey": bseeMultiHostNonEapRadiusPasswordFreeformKey,
       "bseeMultiHostFailOpenVlanDisableEapMode": bseeMultiHostFailOpenVlanDisableEapMode,
       "bseePaeSystemOperState": bseePaeSystemOperState,
       "bseeDefaultEapAll": bseeDefaultEapAll,
       "bseeAutoPortConfigModeSwitchToMHMV": bseeAutoPortConfigModeSwitchToMHMV,
       "bseeAutoPortConfigModeSwitchToMHMVAction": bseeAutoPortConfigModeSwitchToMHMVAction,
       "bseeAutoPortConfigModeSwitchToMHMVStatus": bseeAutoPortConfigModeSwitchToMHMVStatus,
       "bseeNotifications": bseeNotifications,
       "bseeNotifications0": bseeNotifications0,
       "bseePortConfigTable": bseePortConfigTable,
       "bseePortConfigEntry": bseePortConfigEntry,
       "bseePortConfigPortNumber": bseePortConfigPortNumber,
       "bseePortConfigGuestVlanId": bseePortConfigGuestVlanId,
       "bseePortConfigMultiHostEnabled": bseePortConfigMultiHostEnabled,
       "bseePortConfigMultiHostEapMaxNumMacs": bseePortConfigMultiHostEapMaxNumMacs,
       "bseePortConfigMultiHostAllowNonEapClient": bseePortConfigMultiHostAllowNonEapClient,
       "bseePortConfigMultiHostNonEapMacSource": bseePortConfigMultiHostNonEapMacSource,
       "bseePortConfigMultiHostNonEapMaxNumMacs": bseePortConfigMultiHostNonEapMaxNumMacs,
       "bseePortConfigGuestVlanEnabled": bseePortConfigGuestVlanEnabled,
       "bseePortConfigMultiHostRadiusAuthNonEapClient": bseePortConfigMultiHostRadiusAuthNonEapClient,
       "bseePortConfigMultiHostSingleAuthEnabled": bseePortConfigMultiHostSingleAuthEnabled,
       "bseePortConfigMultiHostAllowNonEapPhones": bseePortConfigMultiHostAllowNonEapPhones,
       "bseePortConfigMultiHostAllowRadiusAssignedVlan": bseePortConfigMultiHostAllowRadiusAssignedVlan,
       "bseePortConfigMultiHostEapPacketMode": bseePortConfigMultiHostEapPacketMode,
       "bseePortConfigMultiHostEapRadiusTimeoutMode": bseePortConfigMultiHostEapRadiusTimeoutMode,
       "bseePortConfigMultiHostAllowNonEapRadiusAssignedVlan": bseePortConfigMultiHostAllowNonEapRadiusAssignedVlan,
       "bseePortConfigProcessRadiusRequestsServerPackets": bseePortConfigProcessRadiusRequestsServerPackets,
       "bseePortConfigEapProtocolEnabled": bseePortConfigEapProtocolEnabled,
       "bseePortConfigMultiHostUseMostRecentRadiusAssignedVlan": bseePortConfigMultiHostUseMostRecentRadiusAssignedVlan,
       "bseePortConfigMultiHostClearNeap": bseePortConfigMultiHostClearNeap,
       "bseePortConfigMultiHostBlockDifferentVlanAuth": bseePortConfigMultiHostBlockDifferentVlanAuth,
       "bseePortConfigMultiHostAdacNonEapEnabled": bseePortConfigMultiHostAdacNonEapEnabled,
       "bseePortConfigDefaultEapAll": bseePortConfigDefaultEapAll,
       "bseePortConfigMultiHostMaxMacs": bseePortConfigMultiHostMaxMacs,
       "bseePortConfigMultiHostSingleAuthNoLimit": bseePortConfigMultiHostSingleAuthNoLimit,
       "bseePortConfigFailOpenVlanId": bseePortConfigFailOpenVlanId,
       "bseePortConfigFailOpenVlanEnabled": bseePortConfigFailOpenVlanEnabled,
       "bseePortConfigFailOpenVlanUBP": bseePortConfigFailOpenVlanUBP,
       "bseeMultiHostStatusTable": bseeMultiHostStatusTable,
       "bseeMultiHostStatusEntry": bseeMultiHostStatusEntry,
       "bseeMultiHostStatusPortNumber": bseeMultiHostStatusPortNumber,
       "bseeMultiHostStatusClientMACAddr": bseeMultiHostStatusClientMACAddr,
       "bseeMultiHostStatusPaeState": bseeMultiHostStatusPaeState,
       "bseeMultiHostStatusBackendAuthState": bseeMultiHostStatusBackendAuthState,
       "bseeMultiHostStatusReauthenticate": bseeMultiHostStatusReauthenticate,
       "bseeMultiHostStatusVid": bseeMultiHostStatusVid,
       "bseeMultiHostStatusPri": bseeMultiHostStatusPri,
       "bseeMultiHostStatusFaBindings": bseeMultiHostStatusFaBindings,
       "bseeMultiHostSessionStatsTable": bseeMultiHostSessionStatsTable,
       "bseeMultiHostSessionStatsEntry": bseeMultiHostSessionStatsEntry,
       "bseeMultiHostSessionStatsPortNumber": bseeMultiHostSessionStatsPortNumber,
       "bseeMultiHostSessionStatsClientMACAddr": bseeMultiHostSessionStatsClientMACAddr,
       "bseeMultiHostSessionId": bseeMultiHostSessionId,
       "bseeMultiHostSessionAuthenticMethod": bseeMultiHostSessionAuthenticMethod,
       "bseeMultiHostSessionTime": bseeMultiHostSessionTime,
       "bseeMultiHostSessionTerminateCause": bseeMultiHostSessionTerminateCause,
       "bseeMultiHostSessionUserName": bseeMultiHostSessionUserName,
       "bseeMultiHostNonEapMacTable": bseeMultiHostNonEapMacTable,
       "bseeMultiHostNonEapMacEntry": bseeMultiHostNonEapMacEntry,
       "bseeMultiHostNonEapMacPortNumber": bseeMultiHostNonEapMacPortNumber,
       "bseeMultiHostNonEapMacClientMACAddr": bseeMultiHostNonEapMacClientMACAddr,
       "bseeMultiHostNonEapMacRowStatus": bseeMultiHostNonEapMacRowStatus,
       "bseeMultiHostNonEapStatusTable": bseeMultiHostNonEapStatusTable,
       "bseeMultiHostNonEapStatusEntry": bseeMultiHostNonEapStatusEntry,
       "bseeMultiHostNonEapStatusPortNumber": bseeMultiHostNonEapStatusPortNumber,
       "bseeMultiHostNonEapStatusClientMACAddr": bseeMultiHostNonEapStatusClientMACAddr,
       "bseeMultiHostNonEapStatusState": bseeMultiHostNonEapStatusState,
       "bseeMultiHostNonEapStatusReauthenticate": bseeMultiHostNonEapStatusReauthenticate,
       "bseeMultiHostNonEapStatusVid": bseeMultiHostNonEapStatusVid,
       "bseeMultiHostNonEapStatusPri": bseeMultiHostNonEapStatusPri,
       "bseeMultiHostNonEapStatusFaBindings": bseeMultiHostNonEapStatusFaBindings,
       "bseeSupplicantObjects": bseeSupplicantObjects,
       "bseeSupplicantEnabled": bseeSupplicantEnabled,
       "bseeSupplicantUserTable": bseeSupplicantUserTable,
       "bseeSupplicantUserEntry": bseeSupplicantUserEntry,
       "bseeSupplicantPortNumber": bseeSupplicantPortNumber,
       "bseeSupplicantUserName": bseeSupplicantUserName,
       "bseeSupplicantPassword": bseeSupplicantPassword,
       "bseeSupplicantUserState": bseeSupplicantUserState,
       "bseeMultiHostVoipVlanTable": bseeMultiHostVoipVlanTable,
       "bseeMultiHostVoipVlanEntry": bseeMultiHostVoipVlanEntry,
       "bseeMultiHostVoipVlanIndex": bseeMultiHostVoipVlanIndex,
       "bseeMultiHostVoipVlanId": bseeMultiHostVoipVlanId,
       "bseeMultiHostVoipVlanEnabled": bseeMultiHostVoipVlanEnabled,
       "bseeMultiHostDhcpAuthPhoneTable": bseeMultiHostDhcpAuthPhoneTable,
       "bseeMultiHostDhcpAuthPhoneEntry": bseeMultiHostDhcpAuthPhoneEntry,
       "bseeMultiHostDhcpAuthPhonePortNumber": bseeMultiHostDhcpAuthPhonePortNumber,
       "bseeMultiHostDhcpAuthPhoneClientMACAddr": bseeMultiHostDhcpAuthPhoneClientMACAddr,
       "bseeMultiHostDhcpAuthPhoneUserName": bseeMultiHostDhcpAuthPhoneUserName}
)
