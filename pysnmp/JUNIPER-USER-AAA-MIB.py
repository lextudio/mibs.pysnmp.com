# SNMP MIB module (JUNIPER-USER-AAA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-USER-AAA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:14:23 2024
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

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

(Ipv6Address,
 Ipv6AddressIfIdentifier,
 Ipv6AddressPrefix) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address",
    "Ipv6AddressIfIdentifier",
    "Ipv6AddressPrefix")

(EnabledStatus,) = mibBuilder.importSymbols(
    "JUNIPER-MIMSTP-MIB",
    "EnabledStatus")

(jnxUserAAAMibRoot,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxUserAAAMibRoot")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

jnxUserAAAMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1)
)
jnxUserAAAMib.setRevisions(
        ("2013-07-10 00:00",
         "2013-03-18 00:00",
         "2012-12-29 00:00",
         "2010-12-08 00:00",
         "2010-11-23 00:00",
         "2010-02-09 11:10",
         "2007-08-21 00:00",
         "2007-05-14 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JnxAuthenticateType(Integer32, TextualConvention):
    status = "current"
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
        *(("jsrc", 5),
          ("ldap", 3),
          ("local", 2),
          ("none", 0),
          ("radius", 1),
          ("securid", 4))
    )



class JnxAccountingType(Integer32, TextualConvention):
    status = "current"
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
        *(("jsrc", 5),
          ("ldap", 3),
          ("local", 2),
          ("none", 0),
          ("radius", 1),
          ("securid", 4))
    )



class JnxAuthorizationType(Integer32, TextualConvention):
    status = "current"
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
        *(("jsrc", 5),
          ("ldap", 3),
          ("local", 2),
          ("none", 0),
          ("radius", 1),
          ("securid", 4))
    )



class JnxProvisioningType(Integer32, TextualConvention):
    status = "current"
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
        *(("jsrc", 5),
          ("ldap", 3),
          ("local", 2),
          ("none", 0),
          ("radius", 1),
          ("securid", 4))
    )



# MIB Managed Objects in the order of their OIDs

_JnxUserAAANotifications_ObjectIdentity = ObjectIdentity
jnxUserAAANotifications = _JnxUserAAANotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 0)
)
_JnxUserAAAObjects_ObjectIdentity = ObjectIdentity
jnxUserAAAObjects = _JnxUserAAAObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1)
)
_JnxUserAAAGlobalStats_ObjectIdentity = ObjectIdentity
jnxUserAAAGlobalStats = _JnxUserAAAGlobalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 1)
)
_JnxTotalAuthenticationRequests_Type = Counter64
_JnxTotalAuthenticationRequests_Object = MibScalar
jnxTotalAuthenticationRequests = _JnxTotalAuthenticationRequests_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 1, 1),
    _JnxTotalAuthenticationRequests_Type()
)
jnxTotalAuthenticationRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTotalAuthenticationRequests.setStatus("current")
_JnxTotalAuthenticationResponses_Type = Counter64
_JnxTotalAuthenticationResponses_Object = MibScalar
jnxTotalAuthenticationResponses = _JnxTotalAuthenticationResponses_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 1, 2),
    _JnxTotalAuthenticationResponses_Type()
)
jnxTotalAuthenticationResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxTotalAuthenticationResponses.setStatus("current")
_JnxUserAAAAccessAuthStats_ObjectIdentity = ObjectIdentity
jnxUserAAAAccessAuthStats = _JnxUserAAAAccessAuthStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 2)
)
_JnxUserAAAStatTable_Object = MibTable
jnxUserAAAStatTable = _JnxUserAAAStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    jnxUserAAAStatTable.setStatus("current")
_JnxUserAAAStatEntry_Object = MibTableRow
jnxUserAAAStatEntry = _JnxUserAAAStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 2, 1, 1)
)
jnxUserAAAStatEntry.setIndexNames(
    (0, "JUNIPER-USER-AAA-MIB", "jnxUserAAAStatAuthType"),
)
if mibBuilder.loadTexts:
    jnxUserAAAStatEntry.setStatus("current")
_JnxUserAAAStatAuthType_Type = JnxAuthenticateType
_JnxUserAAAStatAuthType_Object = MibTableColumn
jnxUserAAAStatAuthType = _JnxUserAAAStatAuthType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 2, 1, 1, 1),
    _JnxUserAAAStatAuthType_Type()
)
jnxUserAAAStatAuthType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxUserAAAStatAuthType.setStatus("current")
_JnxUserAAAStatRequestReceived_Type = Counter64
_JnxUserAAAStatRequestReceived_Object = MibTableColumn
jnxUserAAAStatRequestReceived = _JnxUserAAAStatRequestReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 2, 1, 1, 2),
    _JnxUserAAAStatRequestReceived_Type()
)
jnxUserAAAStatRequestReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserAAAStatRequestReceived.setStatus("current")
_JnxUserAAAStatAccessAccepted_Type = Counter64
_JnxUserAAAStatAccessAccepted_Object = MibTableColumn
jnxUserAAAStatAccessAccepted = _JnxUserAAAStatAccessAccepted_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 2, 1, 1, 3),
    _JnxUserAAAStatAccessAccepted_Type()
)
jnxUserAAAStatAccessAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserAAAStatAccessAccepted.setStatus("current")
_JnxUserAAAStatAccessRejected_Type = Counter64
_JnxUserAAAStatAccessRejected_Object = MibTableColumn
jnxUserAAAStatAccessRejected = _JnxUserAAAStatAccessRejected_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 2, 1, 1, 4),
    _JnxUserAAAStatAccessRejected_Type()
)
jnxUserAAAStatAccessRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserAAAStatAccessRejected.setStatus("current")
_JnxUserAAATrapVars_ObjectIdentity = ObjectIdentity
jnxUserAAATrapVars = _JnxUserAAATrapVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 3)
)
_JnxUserAAAServerName_Type = DisplayString
_JnxUserAAAServerName_Object = MibScalar
jnxUserAAAServerName = _JnxUserAAAServerName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 3, 1),
    _JnxUserAAAServerName_Type()
)
jnxUserAAAServerName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxUserAAAServerName.setStatus("current")
_JnxUserAAAAddressPoolName_Type = DisplayString
_JnxUserAAAAddressPoolName_Object = MibScalar
jnxUserAAAAddressPoolName = _JnxUserAAAAddressPoolName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 3, 2),
    _JnxUserAAAAddressPoolName_Type()
)
jnxUserAAAAddressPoolName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxUserAAAAddressPoolName.setStatus("current")
_JnxUserAAAAccessPool_ObjectIdentity = ObjectIdentity
jnxUserAAAAccessPool = _JnxUserAAAAccessPool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 4)
)
_JnxUserAAAAccessPoolGeneral_ObjectIdentity = ObjectIdentity
jnxUserAAAAccessPoolGeneral = _JnxUserAAAAccessPoolGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 4, 1)
)
_JnxUserAAAAccessPoolTable_Object = MibTable
jnxUserAAAAccessPoolTable = _JnxUserAAAAccessPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    jnxUserAAAAccessPoolTable.setStatus("current")
_JnxUserAAAAccessPoolEntry_Object = MibTableRow
jnxUserAAAAccessPoolEntry = _JnxUserAAAAccessPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 4, 1, 1, 1)
)
jnxUserAAAAccessPoolEntry.setIndexNames(
    (0, "JUNIPER-USER-AAA-MIB", "jnxUserAAAAccessPoolIdent"),
)
if mibBuilder.loadTexts:
    jnxUserAAAAccessPoolEntry.setStatus("current")


class _JnxUserAAAAccessPoolIdent_Type(Unsigned32):
    """Custom type jnxUserAAAAccessPoolIdent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_JnxUserAAAAccessPoolIdent_Type.__name__ = "Unsigned32"
_JnxUserAAAAccessPoolIdent_Object = MibTableColumn
jnxUserAAAAccessPoolIdent = _JnxUserAAAAccessPoolIdent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 4, 1, 1, 1, 1),
    _JnxUserAAAAccessPoolIdent_Type()
)
jnxUserAAAAccessPoolIdent.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxUserAAAAccessPoolIdent.setStatus("current")


class _JnxUserAAAAccessPoolRoutingInstance_Type(DisplayString):
    """Custom type jnxUserAAAAccessPoolRoutingInstance based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_JnxUserAAAAccessPoolRoutingInstance_Type.__name__ = "DisplayString"
_JnxUserAAAAccessPoolRoutingInstance_Object = MibTableColumn
jnxUserAAAAccessPoolRoutingInstance = _JnxUserAAAAccessPoolRoutingInstance_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 4, 1, 1, 1, 2),
    _JnxUserAAAAccessPoolRoutingInstance_Type()
)
jnxUserAAAAccessPoolRoutingInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserAAAAccessPoolRoutingInstance.setStatus("current")


class _JnxUserAAAAccessPoolName_Type(DisplayString):
    """Custom type jnxUserAAAAccessPoolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_JnxUserAAAAccessPoolName_Type.__name__ = "DisplayString"
_JnxUserAAAAccessPoolName_Object = MibTableColumn
jnxUserAAAAccessPoolName = _JnxUserAAAAccessPoolName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 4, 1, 1, 1, 3),
    _JnxUserAAAAccessPoolName_Type()
)
jnxUserAAAAccessPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserAAAAccessPoolName.setStatus("current")


class _JnxUserAAAAccessPoolLinkName_Type(DisplayString):
    """Custom type jnxUserAAAAccessPoolLinkName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_JnxUserAAAAccessPoolLinkName_Type.__name__ = "DisplayString"
_JnxUserAAAAccessPoolLinkName_Object = MibTableColumn
jnxUserAAAAccessPoolLinkName = _JnxUserAAAAccessPoolLinkName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 4, 1, 1, 1, 4),
    _JnxUserAAAAccessPoolLinkName_Type()
)
jnxUserAAAAccessPoolLinkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserAAAAccessPoolLinkName.setStatus("current")
_JnxUserAAAAccessPoolFamilyType_Type = InetAddressType
_JnxUserAAAAccessPoolFamilyType_Object = MibTableColumn
jnxUserAAAAccessPoolFamilyType = _JnxUserAAAAccessPoolFamilyType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 4, 1, 1, 1, 5),
    _JnxUserAAAAccessPoolFamilyType_Type()
)
jnxUserAAAAccessPoolFamilyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserAAAAccessPoolFamilyType.setStatus("current")


class _JnxUserAAAAccessPoolInetNetwork_Type(InetAddress):
    """Custom type jnxUserAAAAccessPoolInetNetwork based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 48),
    )


_JnxUserAAAAccessPoolInetNetwork_Type.__name__ = "InetAddress"
_JnxUserAAAAccessPoolInetNetwork_Object = MibTableColumn
jnxUserAAAAccessPoolInetNetwork = _JnxUserAAAAccessPoolInetNetwork_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 4, 1, 1, 1, 6),
    _JnxUserAAAAccessPoolInetNetwork_Type()
)
jnxUserAAAAccessPoolInetNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserAAAAccessPoolInetNetwork.setStatus("current")
_JnxUserAAAAccessPoolInetPrefixLength_Type = InetAddressPrefixLength
_JnxUserAAAAccessPoolInetPrefixLength_Object = MibTableColumn
jnxUserAAAAccessPoolInetPrefixLength = _JnxUserAAAAccessPoolInetPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 4, 1, 1, 1, 7),
    _JnxUserAAAAccessPoolInetPrefixLength_Type()
)
jnxUserAAAAccessPoolInetPrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserAAAAccessPoolInetPrefixLength.setStatus("current")
_JnxUserAAAAccessPoolOutOfMemory_Type = Counter64
_JnxUserAAAAccessPoolOutOfMemory_Object = MibTableColumn
jnxUserAAAAccessPoolOutOfMemory = _JnxUserAAAAccessPoolOutOfMemory_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 4, 1, 1, 1, 8),
    _JnxUserAAAAccessPoolOutOfMemory_Type()
)
jnxUserAAAAccessPoolOutOfMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserAAAAccessPoolOutOfMemory.setStatus("current")
_JnxUserAAAAccessPoolOutOfAddresses_Type = Counter64
_JnxUserAAAAccessPoolOutOfAddresses_Object = MibTableColumn
jnxUserAAAAccessPoolOutOfAddresses = _JnxUserAAAAccessPoolOutOfAddresses_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 4, 1, 1, 1, 9),
    _JnxUserAAAAccessPoolOutOfAddresses_Type()
)
jnxUserAAAAccessPoolOutOfAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserAAAAccessPoolOutOfAddresses.setStatus("current")
_JnxUserAAAAccessPoolAddressTotal_Type = Counter64
_JnxUserAAAAccessPoolAddressTotal_Object = MibTableColumn
jnxUserAAAAccessPoolAddressTotal = _JnxUserAAAAccessPoolAddressTotal_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 4, 1, 1, 1, 10),
    _JnxUserAAAAccessPoolAddressTotal_Type()
)
jnxUserAAAAccessPoolAddressTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserAAAAccessPoolAddressTotal.setStatus("current")
_JnxUserAAAAccessPoolAddressesInUse_Type = Counter64
_JnxUserAAAAccessPoolAddressesInUse_Object = MibTableColumn
jnxUserAAAAccessPoolAddressesInUse = _JnxUserAAAAccessPoolAddressesInUse_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 4, 1, 1, 1, 11),
    _JnxUserAAAAccessPoolAddressesInUse_Type()
)
jnxUserAAAAccessPoolAddressesInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserAAAAccessPoolAddressesInUse.setStatus("current")
_JnxUserAAAAccessPoolAddressUsage_Type = Integer32
_JnxUserAAAAccessPoolAddressUsage_Object = MibTableColumn
jnxUserAAAAccessPoolAddressUsage = _JnxUserAAAAccessPoolAddressUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 4, 1, 1, 1, 12),
    _JnxUserAAAAccessPoolAddressUsage_Type()
)
jnxUserAAAAccessPoolAddressUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserAAAAccessPoolAddressUsage.setStatus("current")
_JnxUserAAAAccessPoolAddressUsageHigh_Type = Integer32
_JnxUserAAAAccessPoolAddressUsageHigh_Object = MibTableColumn
jnxUserAAAAccessPoolAddressUsageHigh = _JnxUserAAAAccessPoolAddressUsageHigh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 4, 1, 1, 1, 13),
    _JnxUserAAAAccessPoolAddressUsageHigh_Type()
)
jnxUserAAAAccessPoolAddressUsageHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserAAAAccessPoolAddressUsageHigh.setStatus("current")
_JnxUserAAAAccessPoolAddressUsageAbate_Type = Integer32
_JnxUserAAAAccessPoolAddressUsageAbate_Object = MibTableColumn
jnxUserAAAAccessPoolAddressUsageAbate = _JnxUserAAAAccessPoolAddressUsageAbate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 4, 1, 1, 1, 14),
    _JnxUserAAAAccessPoolAddressUsageAbate_Type()
)
jnxUserAAAAccessPoolAddressUsageAbate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserAAAAccessPoolAddressUsageAbate.setStatus("current")
_JnxUserAAAAssignment_ObjectIdentity = ObjectIdentity
jnxUserAAAAssignment = _JnxUserAAAAssignment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5)
)
_JnxUserAAAGeneral_ObjectIdentity = ObjectIdentity
jnxUserAAAGeneral = _JnxUserAAAGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 1)
)


class _JnxUserAAADomainDelimiters_Type(DisplayString):
    """Custom type jnxUserAAADomainDelimiters based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_JnxUserAAADomainDelimiters_Type.__name__ = "DisplayString"
_JnxUserAAADomainDelimiters_Object = MibScalar
jnxUserAAADomainDelimiters = _JnxUserAAADomainDelimiters_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 1, 1),
    _JnxUserAAADomainDelimiters_Type()
)
jnxUserAAADomainDelimiters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserAAADomainDelimiters.setStatus("current")


class _JnxUserAAADomainParseDirection_Type(Integer32):
    """Custom type jnxUserAAADomainParseDirection based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("leftToRight", 2),
          ("rightToLeft", 1))
    )


_JnxUserAAADomainParseDirection_Type.__name__ = "Integer32"
_JnxUserAAADomainParseDirection_Object = MibScalar
jnxUserAAADomainParseDirection = _JnxUserAAADomainParseDirection_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 1, 2),
    _JnxUserAAADomainParseDirection_Type()
)
jnxUserAAADomainParseDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserAAADomainParseDirection.setStatus("current")
_JnxUserAAADomain_ObjectIdentity = ObjectIdentity
jnxUserAAADomain = _JnxUserAAADomain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2)
)
_JnxUserAAADomainTable_Object = MibTable
jnxUserAAADomainTable = _JnxUserAAADomainTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    jnxUserAAADomainTable.setStatus("current")
_JnxUserAAADomainEntry_Object = MibTableRow
jnxUserAAADomainEntry = _JnxUserAAADomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 1, 1)
)
jnxUserAAADomainEntry.setIndexNames(
    (1, "JUNIPER-USER-AAA-MIB", "jnxUserAAADomainName"),
)
if mibBuilder.loadTexts:
    jnxUserAAADomainEntry.setStatus("current")


class _JnxUserAAADomainName_Type(DisplayString):
    """Custom type jnxUserAAADomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_JnxUserAAADomainName_Type.__name__ = "DisplayString"
_JnxUserAAADomainName_Object = MibTableColumn
jnxUserAAADomainName = _JnxUserAAADomainName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 1, 1, 1),
    _JnxUserAAADomainName_Type()
)
jnxUserAAADomainName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxUserAAADomainName.setStatus("current")


class _JnxUserAAADomainStripDomain_Type(TruthValue):
    """Custom type jnxUserAAADomainStripDomain based on TruthValue"""


_JnxUserAAADomainStripDomain_Object = MibTableColumn
jnxUserAAADomainStripDomain = _JnxUserAAADomainStripDomain_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 1, 1, 2),
    _JnxUserAAADomainStripDomain_Type()
)
jnxUserAAADomainStripDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserAAADomainStripDomain.setStatus("current")
_JnxUserAAADomainLogicalSystem_Type = DisplayString
_JnxUserAAADomainLogicalSystem_Object = MibTableColumn
jnxUserAAADomainLogicalSystem = _JnxUserAAADomainLogicalSystem_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 1, 1, 3),
    _JnxUserAAADomainLogicalSystem_Type()
)
jnxUserAAADomainLogicalSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserAAADomainLogicalSystem.setStatus("current")
_JnxUserAAADomainRoutingInstance_Type = DisplayString
_JnxUserAAADomainRoutingInstance_Object = MibTableColumn
jnxUserAAADomainRoutingInstance = _JnxUserAAADomainRoutingInstance_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 1, 1, 4),
    _JnxUserAAADomainRoutingInstance_Type()
)
jnxUserAAADomainRoutingInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserAAADomainRoutingInstance.setStatus("current")


class _JnxUserAAADomainAddrPoolName_Type(DisplayString):
    """Custom type jnxUserAAADomainAddrPoolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_JnxUserAAADomainAddrPoolName_Type.__name__ = "DisplayString"
_JnxUserAAADomainAddrPoolName_Object = MibTableColumn
jnxUserAAADomainAddrPoolName = _JnxUserAAADomainAddrPoolName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 1, 1, 5),
    _JnxUserAAADomainAddrPoolName_Type()
)
jnxUserAAADomainAddrPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserAAADomainAddrPoolName.setStatus("current")
_JnxUserAAADomainDynamicPorfile_Type = DisplayString
_JnxUserAAADomainDynamicPorfile_Object = MibTableColumn
jnxUserAAADomainDynamicPorfile = _JnxUserAAADomainDynamicPorfile_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 1, 1, 6),
    _JnxUserAAADomainDynamicPorfile_Type()
)
jnxUserAAADomainDynamicPorfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserAAADomainDynamicPorfile.setStatus("deprecated")
_JnxUserAAADomainTargetLogicalSystem_Type = DisplayString
_JnxUserAAADomainTargetLogicalSystem_Object = MibTableColumn
jnxUserAAADomainTargetLogicalSystem = _JnxUserAAADomainTargetLogicalSystem_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 1, 1, 7),
    _JnxUserAAADomainTargetLogicalSystem_Type()
)
jnxUserAAADomainTargetLogicalSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserAAADomainTargetLogicalSystem.setStatus("current")
_JnxUserAAADomainTargetRoutingInstance_Type = DisplayString
_JnxUserAAADomainTargetRoutingInstance_Object = MibTableColumn
jnxUserAAADomainTargetRoutingInstance = _JnxUserAAADomainTargetRoutingInstance_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 1, 1, 8),
    _JnxUserAAADomainTargetRoutingInstance_Type()
)
jnxUserAAADomainTargetRoutingInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserAAADomainTargetRoutingInstance.setStatus("current")
_JnxUserAAADomainTunnelProfile_Type = DisplayString
_JnxUserAAADomainTunnelProfile_Object = MibTableColumn
jnxUserAAADomainTunnelProfile = _JnxUserAAADomainTunnelProfile_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 1, 1, 9),
    _JnxUserAAADomainTunnelProfile_Type()
)
jnxUserAAADomainTunnelProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserAAADomainTunnelProfile.setStatus("current")
_JnxUserAAADomainDynamicProfile_Type = DisplayString
_JnxUserAAADomainDynamicProfile_Object = MibTableColumn
jnxUserAAADomainDynamicProfile = _JnxUserAAADomainDynamicProfile_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 1, 1, 10),
    _JnxUserAAADomainDynamicProfile_Type()
)
jnxUserAAADomainDynamicProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserAAADomainDynamicProfile.setStatus("current")


class _JnxUserAAADomainStripUsername_Type(Integer32):
    """Custom type jnxUserAAADomainStripUsername based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("leftToRight", 1),
          ("rightToLeft", 2))
    )


_JnxUserAAADomainStripUsername_Type.__name__ = "Integer32"
_JnxUserAAADomainStripUsername_Object = MibTableColumn
jnxUserAAADomainStripUsername = _JnxUserAAADomainStripUsername_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 1, 1, 11),
    _JnxUserAAADomainStripUsername_Type()
)
jnxUserAAADomainStripUsername.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserAAADomainStripUsername.setStatus("current")


class _JnxUserAAADomainOverridePassword_Type(TruthValue):
    """Custom type jnxUserAAADomainOverridePassword based on TruthValue"""


_JnxUserAAADomainOverridePassword_Object = MibTableColumn
jnxUserAAADomainOverridePassword = _JnxUserAAADomainOverridePassword_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 1, 1, 12),
    _JnxUserAAADomainOverridePassword_Type()
)
jnxUserAAADomainOverridePassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserAAADomainOverridePassword.setStatus("current")
_JnxUserAAADomainTunnelTable_Object = MibTable
jnxUserAAADomainTunnelTable = _JnxUserAAADomainTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 2)
)
if mibBuilder.loadTexts:
    jnxUserAAADomainTunnelTable.setStatus("current")
_JnxUserAAADomainTunnelEntry_Object = MibTableRow
jnxUserAAADomainTunnelEntry = _JnxUserAAADomainTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 2, 1)
)
jnxUserAAADomainTunnelEntry.setIndexNames(
    (0, "JUNIPER-USER-AAA-MIB", "jnxUserAAADomainTunnelName"),
    (0, "JUNIPER-USER-AAA-MIB", "jnxUserAAADomainTunnelDefId"),
)
if mibBuilder.loadTexts:
    jnxUserAAADomainTunnelEntry.setStatus("current")


class _JnxUserAAADomainTunnelName_Type(OctetString):
    """Custom type jnxUserAAADomainTunnelName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_JnxUserAAADomainTunnelName_Type.__name__ = "OctetString"
_JnxUserAAADomainTunnelName_Object = MibTableColumn
jnxUserAAADomainTunnelName = _JnxUserAAADomainTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 2, 1, 1),
    _JnxUserAAADomainTunnelName_Type()
)
jnxUserAAADomainTunnelName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxUserAAADomainTunnelName.setStatus("current")


class _JnxUserAAADomainTunnelDefId_Type(Integer32):
    """Custom type jnxUserAAADomainTunnelDefId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_JnxUserAAADomainTunnelDefId_Type.__name__ = "Integer32"
_JnxUserAAADomainTunnelDefId_Object = MibTableColumn
jnxUserAAADomainTunnelDefId = _JnxUserAAADomainTunnelDefId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 2, 1, 2),
    _JnxUserAAADomainTunnelDefId_Type()
)
jnxUserAAADomainTunnelDefId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxUserAAADomainTunnelDefId.setStatus("current")


class _JnxUserAAADomainTunnelPreference_Type(Integer32):
    """Custom type jnxUserAAADomainTunnelPreference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_JnxUserAAADomainTunnelPreference_Type.__name__ = "Integer32"
_JnxUserAAADomainTunnelPreference_Object = MibTableColumn
jnxUserAAADomainTunnelPreference = _JnxUserAAADomainTunnelPreference_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 2, 1, 3),
    _JnxUserAAADomainTunnelPreference_Type()
)
jnxUserAAADomainTunnelPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserAAADomainTunnelPreference.setStatus("current")
_JnxUserAAADomainTunnelRemoteGwName_Type = DisplayString
_JnxUserAAADomainTunnelRemoteGwName_Object = MibTableColumn
jnxUserAAADomainTunnelRemoteGwName = _JnxUserAAADomainTunnelRemoteGwName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 2, 1, 4),
    _JnxUserAAADomainTunnelRemoteGwName_Type()
)
jnxUserAAADomainTunnelRemoteGwName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserAAADomainTunnelRemoteGwName.setStatus("current")
_JnxUserAAADomainTunnelRemoteGwAddress_Type = IpAddress
_JnxUserAAADomainTunnelRemoteGwAddress_Object = MibTableColumn
jnxUserAAADomainTunnelRemoteGwAddress = _JnxUserAAADomainTunnelRemoteGwAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 2, 1, 5),
    _JnxUserAAADomainTunnelRemoteGwAddress_Type()
)
jnxUserAAADomainTunnelRemoteGwAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserAAADomainTunnelRemoteGwAddress.setStatus("current")
_JnxUserAAADomainTunnelSourceGwName_Type = DisplayString
_JnxUserAAADomainTunnelSourceGwName_Object = MibTableColumn
jnxUserAAADomainTunnelSourceGwName = _JnxUserAAADomainTunnelSourceGwName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 2, 1, 6),
    _JnxUserAAADomainTunnelSourceGwName_Type()
)
jnxUserAAADomainTunnelSourceGwName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserAAADomainTunnelSourceGwName.setStatus("current")
_JnxUserAAADomainTunnelSourceGwAddress_Type = IpAddress
_JnxUserAAADomainTunnelSourceGwAddress_Object = MibTableColumn
jnxUserAAADomainTunnelSourceGwAddress = _JnxUserAAADomainTunnelSourceGwAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 2, 1, 7),
    _JnxUserAAADomainTunnelSourceGwAddress_Type()
)
jnxUserAAADomainTunnelSourceGwAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserAAADomainTunnelSourceGwAddress.setStatus("current")


class _JnxUserAAADomainTunnelSecret_Type(DisplayString):
    """Custom type jnxUserAAADomainTunnelSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JnxUserAAADomainTunnelSecret_Type.__name__ = "DisplayString"
_JnxUserAAADomainTunnelSecret_Object = MibTableColumn
jnxUserAAADomainTunnelSecret = _JnxUserAAADomainTunnelSecret_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 2, 1, 8),
    _JnxUserAAADomainTunnelSecret_Type()
)
jnxUserAAADomainTunnelSecret.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserAAADomainTunnelSecret.setStatus("current")
_JnxUserAAADomainTunnelLogicalSystems_Type = DisplayString
_JnxUserAAADomainTunnelLogicalSystems_Object = MibTableColumn
jnxUserAAADomainTunnelLogicalSystems = _JnxUserAAADomainTunnelLogicalSystems_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 2, 1, 9),
    _JnxUserAAADomainTunnelLogicalSystems_Type()
)
jnxUserAAADomainTunnelLogicalSystems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserAAADomainTunnelLogicalSystems.setStatus("current")
_JnxUserAAADomainTunnelRoutingInstance_Type = DisplayString
_JnxUserAAADomainTunnelRoutingInstance_Object = MibTableColumn
jnxUserAAADomainTunnelRoutingInstance = _JnxUserAAADomainTunnelRoutingInstance_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 2, 1, 10),
    _JnxUserAAADomainTunnelRoutingInstance_Type()
)
jnxUserAAADomainTunnelRoutingInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserAAADomainTunnelRoutingInstance.setStatus("current")


class _JnxUserAAADomainTunnelMedium_Type(Integer32):
    """Custom type jnxUserAAADomainTunnelMedium based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tunnelMediumIPv4", 1),
          ("tunnelMediumUnknown", 2))
    )


_JnxUserAAADomainTunnelMedium_Type.__name__ = "Integer32"
_JnxUserAAADomainTunnelMedium_Object = MibTableColumn
jnxUserAAADomainTunnelMedium = _JnxUserAAADomainTunnelMedium_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 2, 1, 11),
    _JnxUserAAADomainTunnelMedium_Type()
)
jnxUserAAADomainTunnelMedium.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserAAADomainTunnelMedium.setStatus("current")


class _JnxUserAAADomainTunnelType_Type(Integer32):
    """Custom type jnxUserAAADomainTunnelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tunnelL2f", 3),
          ("tunnelL2tp", 1),
          ("tunnelUnknown", 2))
    )


_JnxUserAAADomainTunnelType_Type.__name__ = "Integer32"
_JnxUserAAADomainTunnelType_Object = MibTableColumn
jnxUserAAADomainTunnelType = _JnxUserAAADomainTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 2, 1, 12),
    _JnxUserAAADomainTunnelType_Type()
)
jnxUserAAADomainTunnelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserAAADomainTunnelType.setStatus("current")


class _JnxUserAAADomainTunnelId_Type(DisplayString):
    """Custom type jnxUserAAADomainTunnelId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JnxUserAAADomainTunnelId_Type.__name__ = "DisplayString"
_JnxUserAAADomainTunnelId_Object = MibTableColumn
jnxUserAAADomainTunnelId = _JnxUserAAADomainTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 2, 1, 13),
    _JnxUserAAADomainTunnelId_Type()
)
jnxUserAAADomainTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserAAADomainTunnelId.setStatus("current")
_JnxUserAAADomainTunnelMaxSessions_Type = Unsigned32
_JnxUserAAADomainTunnelMaxSessions_Object = MibTableColumn
jnxUserAAADomainTunnelMaxSessions = _JnxUserAAADomainTunnelMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 2, 1, 14),
    _JnxUserAAADomainTunnelMaxSessions_Type()
)
jnxUserAAADomainTunnelMaxSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserAAADomainTunnelMaxSessions.setStatus("current")
_JnxUserAAADomainPadnTable_Object = MibTable
jnxUserAAADomainPadnTable = _JnxUserAAADomainPadnTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 3)
)
if mibBuilder.loadTexts:
    jnxUserAAADomainPadnTable.setStatus("current")
_JnxUserAAADomainPadnEntry_Object = MibTableRow
jnxUserAAADomainPadnEntry = _JnxUserAAADomainPadnEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 3, 1)
)
jnxUserAAADomainPadnEntry.setIndexNames(
    (0, "JUNIPER-USER-AAA-MIB", "jnxUserAAADomainName"),
    (0, "JUNIPER-USER-AAA-MIB", "jnxUserAAADomainPadnIpAddress"),
    (0, "JUNIPER-USER-AAA-MIB", "jnxUserAAADomainPadnIpMask"),
)
if mibBuilder.loadTexts:
    jnxUserAAADomainPadnEntry.setStatus("current")
_JnxUserAAADomainPadnIpAddress_Type = IpAddress
_JnxUserAAADomainPadnIpAddress_Object = MibTableColumn
jnxUserAAADomainPadnIpAddress = _JnxUserAAADomainPadnIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 3, 1, 1),
    _JnxUserAAADomainPadnIpAddress_Type()
)
jnxUserAAADomainPadnIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxUserAAADomainPadnIpAddress.setStatus("current")
_JnxUserAAADomainPadnIpMask_Type = IpAddress
_JnxUserAAADomainPadnIpMask_Object = MibTableColumn
jnxUserAAADomainPadnIpMask = _JnxUserAAADomainPadnIpMask_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 3, 1, 2),
    _JnxUserAAADomainPadnIpMask_Type()
)
jnxUserAAADomainPadnIpMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxUserAAADomainPadnIpMask.setStatus("current")


class _JnxUserAAADomainPadnDistance_Type(Integer32):
    """Custom type jnxUserAAADomainPadnDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JnxUserAAADomainPadnDistance_Type.__name__ = "Integer32"
_JnxUserAAADomainPadnDistance_Object = MibTableColumn
jnxUserAAADomainPadnDistance = _JnxUserAAADomainPadnDistance_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 5, 2, 3, 1, 3),
    _JnxUserAAADomainPadnDistance_Type()
)
jnxUserAAADomainPadnDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserAAADomainPadnDistance.setStatus("current")
_JnxUserAAAAccessProfile_ObjectIdentity = ObjectIdentity
jnxUserAAAAccessProfile = _JnxUserAAAAccessProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 6)
)
_JnxUserAAAAccessProfileGeneral_ObjectIdentity = ObjectIdentity
jnxUserAAAAccessProfileGeneral = _JnxUserAAAAccessProfileGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 6, 1)
)
_JnxUserAAAAccessProfileTable_Object = MibTable
jnxUserAAAAccessProfileTable = _JnxUserAAAAccessProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 6, 1, 1)
)
if mibBuilder.loadTexts:
    jnxUserAAAAccessProfileTable.setStatus("current")
_JnxUserAAAAccessProfileEntry_Object = MibTableRow
jnxUserAAAAccessProfileEntry = _JnxUserAAAAccessProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 6, 1, 1, 1)
)
jnxUserAAAAccessProfileEntry.setIndexNames(
    (1, "JUNIPER-USER-AAA-MIB", "jnxUserAAAAccessProfileName"),
)
if mibBuilder.loadTexts:
    jnxUserAAAAccessProfileEntry.setStatus("current")


class _JnxUserAAAAccessProfileName_Type(DisplayString):
    """Custom type jnxUserAAAAccessProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_JnxUserAAAAccessProfileName_Type.__name__ = "DisplayString"
_JnxUserAAAAccessProfileName_Object = MibTableColumn
jnxUserAAAAccessProfileName = _JnxUserAAAAccessProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 6, 1, 1, 1, 1),
    _JnxUserAAAAccessProfileName_Type()
)
jnxUserAAAAccessProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxUserAAAAccessProfileName.setStatus("current")


class _JnxUserAAAAccessProfileAuthenticationOrder_Type(OctetString):
    """Custom type jnxUserAAAAccessProfileAuthenticationOrder based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_JnxUserAAAAccessProfileAuthenticationOrder_Type.__name__ = "OctetString"
_JnxUserAAAAccessProfileAuthenticationOrder_Object = MibTableColumn
jnxUserAAAAccessProfileAuthenticationOrder = _JnxUserAAAAccessProfileAuthenticationOrder_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 6, 1, 1, 1, 2),
    _JnxUserAAAAccessProfileAuthenticationOrder_Type()
)
jnxUserAAAAccessProfileAuthenticationOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserAAAAccessProfileAuthenticationOrder.setStatus("current")


class _JnxUserAAAAccessProfileAccountingOrder_Type(OctetString):
    """Custom type jnxUserAAAAccessProfileAccountingOrder based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_JnxUserAAAAccessProfileAccountingOrder_Type.__name__ = "OctetString"
_JnxUserAAAAccessProfileAccountingOrder_Object = MibTableColumn
jnxUserAAAAccessProfileAccountingOrder = _JnxUserAAAAccessProfileAccountingOrder_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 6, 1, 1, 1, 3),
    _JnxUserAAAAccessProfileAccountingOrder_Type()
)
jnxUserAAAAccessProfileAccountingOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserAAAAccessProfileAccountingOrder.setStatus("current")


class _JnxUserAAAAccessProfileAuthorizationOrder_Type(OctetString):
    """Custom type jnxUserAAAAccessProfileAuthorizationOrder based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_JnxUserAAAAccessProfileAuthorizationOrder_Type.__name__ = "OctetString"
_JnxUserAAAAccessProfileAuthorizationOrder_Object = MibTableColumn
jnxUserAAAAccessProfileAuthorizationOrder = _JnxUserAAAAccessProfileAuthorizationOrder_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 6, 1, 1, 1, 4),
    _JnxUserAAAAccessProfileAuthorizationOrder_Type()
)
jnxUserAAAAccessProfileAuthorizationOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserAAAAccessProfileAuthorizationOrder.setStatus("current")


class _JnxUserAAAAccessProfileProvisioningOrder_Type(OctetString):
    """Custom type jnxUserAAAAccessProfileProvisioningOrder based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_JnxUserAAAAccessProfileProvisioningOrder_Type.__name__ = "OctetString"
_JnxUserAAAAccessProfileProvisioningOrder_Object = MibTableColumn
jnxUserAAAAccessProfileProvisioningOrder = _JnxUserAAAAccessProfileProvisioningOrder_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 6, 1, 1, 1, 5),
    _JnxUserAAAAccessProfileProvisioningOrder_Type()
)
jnxUserAAAAccessProfileProvisioningOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserAAAAccessProfileProvisioningOrder.setStatus("current")
_JnxUserAAAAccessProfileAccStopOnFailure_Type = TruthValue
_JnxUserAAAAccessProfileAccStopOnFailure_Object = MibTableColumn
jnxUserAAAAccessProfileAccStopOnFailure = _JnxUserAAAAccessProfileAccStopOnFailure_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 6, 1, 1, 1, 6),
    _JnxUserAAAAccessProfileAccStopOnFailure_Type()
)
jnxUserAAAAccessProfileAccStopOnFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserAAAAccessProfileAccStopOnFailure.setStatus("current")
_JnxUserAAAAccessProfileAccStopOnDeny_Type = TruthValue
_JnxUserAAAAccessProfileAccStopOnDeny_Object = MibTableColumn
jnxUserAAAAccessProfileAccStopOnDeny = _JnxUserAAAAccessProfileAccStopOnDeny_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 6, 1, 1, 1, 7),
    _JnxUserAAAAccessProfileAccStopOnDeny_Type()
)
jnxUserAAAAccessProfileAccStopOnDeny.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserAAAAccessProfileAccStopOnDeny.setStatus("current")
_JnxUserAAAAccessProfileImmediateUpdate_Type = TruthValue
_JnxUserAAAAccessProfileImmediateUpdate_Object = MibTableColumn
jnxUserAAAAccessProfileImmediateUpdate = _JnxUserAAAAccessProfileImmediateUpdate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 6, 1, 1, 1, 8),
    _JnxUserAAAAccessProfileImmediateUpdate_Type()
)
jnxUserAAAAccessProfileImmediateUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserAAAAccessProfileImmediateUpdate.setStatus("current")
_JnxUserAAAAccessProfileCoaImmediateUpdate_Type = TruthValue
_JnxUserAAAAccessProfileCoaImmediateUpdate_Object = MibTableColumn
jnxUserAAAAccessProfileCoaImmediateUpdate = _JnxUserAAAAccessProfileCoaImmediateUpdate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 6, 1, 1, 1, 9),
    _JnxUserAAAAccessProfileCoaImmediateUpdate_Type()
)
jnxUserAAAAccessProfileCoaImmediateUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserAAAAccessProfileCoaImmediateUpdate.setStatus("current")
_JnxUserAAAAccessProfileInterval_Type = Integer32
_JnxUserAAAAccessProfileInterval_Object = MibTableColumn
jnxUserAAAAccessProfileInterval = _JnxUserAAAAccessProfileInterval_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 6, 1, 1, 1, 10),
    _JnxUserAAAAccessProfileInterval_Type()
)
jnxUserAAAAccessProfileInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserAAAAccessProfileInterval.setStatus("current")
if mibBuilder.loadTexts:
    jnxUserAAAAccessProfileInterval.setUnits("minutes")


class _JnxUserAAAAccessProfileStatType_Type(Integer32):
    """Custom type jnxUserAAAAccessProfileStatType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("time", 0),
          ("volume-time", 1))
    )


_JnxUserAAAAccessProfileStatType_Type.__name__ = "Integer32"
_JnxUserAAAAccessProfileStatType_Object = MibTableColumn
jnxUserAAAAccessProfileStatType = _JnxUserAAAAccessProfileStatType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 1, 6, 1, 1, 1, 11),
    _JnxUserAAAAccessProfileStatType_Type()
)
jnxUserAAAAccessProfileStatType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxUserAAAAccessProfileStatType.setStatus("current")

# Managed Objects groups


# Notification objects

jnxAccessAuthServiceUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 0, 1)
)
if mibBuilder.loadTexts:
    jnxAccessAuthServiceUp.setStatus(
        "current"
    )

jnxAccessAuthServiceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 0, 2)
)
if mibBuilder.loadTexts:
    jnxAccessAuthServiceDown.setStatus(
        "current"
    )

jnxAccessAuthServerDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 0, 3)
)
jnxAccessAuthServerDisabled.setObjects(
    ("JUNIPER-USER-AAA-MIB", "jnxUserAAAServerName")
)
if mibBuilder.loadTexts:
    jnxAccessAuthServerDisabled.setStatus(
        "current"
    )

jnxAccessAuthServerEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 0, 4)
)
jnxAccessAuthServerEnabled.setObjects(
    ("JUNIPER-USER-AAA-MIB", "jnxUserAAAServerName")
)
if mibBuilder.loadTexts:
    jnxAccessAuthServerEnabled.setStatus(
        "current"
    )

jnxAccessAuthAddressPoolHighThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 0, 5)
)
jnxAccessAuthAddressPoolHighThreshold.setObjects(
    ("JUNIPER-USER-AAA-MIB", "jnxUserAAAAddressPoolName")
)
if mibBuilder.loadTexts:
    jnxAccessAuthAddressPoolHighThreshold.setStatus(
        "current"
    )

jnxAccessAuthAddressPoolAbateThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 0, 6)
)
jnxAccessAuthAddressPoolAbateThreshold.setObjects(
    ("JUNIPER-USER-AAA-MIB", "jnxUserAAAAddressPoolName")
)
if mibBuilder.loadTexts:
    jnxAccessAuthAddressPoolAbateThreshold.setStatus(
        "current"
    )

jnxAccessAuthAddressPoolOutOfAddresses = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 0, 7)
)
jnxAccessAuthAddressPoolOutOfAddresses.setObjects(
    ("JUNIPER-USER-AAA-MIB", "jnxUserAAAAddressPoolName")
)
if mibBuilder.loadTexts:
    jnxAccessAuthAddressPoolOutOfAddresses.setStatus(
        "current"
    )

jnxAccessAuthAddressPoolOutOfMemory = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 51, 1, 0, 8)
)
jnxAccessAuthAddressPoolOutOfMemory.setObjects(
    ("JUNIPER-USER-AAA-MIB", "jnxUserAAAAddressPoolName")
)
if mibBuilder.loadTexts:
    jnxAccessAuthAddressPoolOutOfMemory.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-USER-AAA-MIB",
    **{"JnxAuthenticateType": JnxAuthenticateType,
       "JnxAccountingType": JnxAccountingType,
       "JnxAuthorizationType": JnxAuthorizationType,
       "JnxProvisioningType": JnxProvisioningType,
       "jnxUserAAAMib": jnxUserAAAMib,
       "jnxUserAAANotifications": jnxUserAAANotifications,
       "jnxAccessAuthServiceUp": jnxAccessAuthServiceUp,
       "jnxAccessAuthServiceDown": jnxAccessAuthServiceDown,
       "jnxAccessAuthServerDisabled": jnxAccessAuthServerDisabled,
       "jnxAccessAuthServerEnabled": jnxAccessAuthServerEnabled,
       "jnxAccessAuthAddressPoolHighThreshold": jnxAccessAuthAddressPoolHighThreshold,
       "jnxAccessAuthAddressPoolAbateThreshold": jnxAccessAuthAddressPoolAbateThreshold,
       "jnxAccessAuthAddressPoolOutOfAddresses": jnxAccessAuthAddressPoolOutOfAddresses,
       "jnxAccessAuthAddressPoolOutOfMemory": jnxAccessAuthAddressPoolOutOfMemory,
       "jnxUserAAAObjects": jnxUserAAAObjects,
       "jnxUserAAAGlobalStats": jnxUserAAAGlobalStats,
       "jnxTotalAuthenticationRequests": jnxTotalAuthenticationRequests,
       "jnxTotalAuthenticationResponses": jnxTotalAuthenticationResponses,
       "jnxUserAAAAccessAuthStats": jnxUserAAAAccessAuthStats,
       "jnxUserAAAStatTable": jnxUserAAAStatTable,
       "jnxUserAAAStatEntry": jnxUserAAAStatEntry,
       "jnxUserAAAStatAuthType": jnxUserAAAStatAuthType,
       "jnxUserAAAStatRequestReceived": jnxUserAAAStatRequestReceived,
       "jnxUserAAAStatAccessAccepted": jnxUserAAAStatAccessAccepted,
       "jnxUserAAAStatAccessRejected": jnxUserAAAStatAccessRejected,
       "jnxUserAAATrapVars": jnxUserAAATrapVars,
       "jnxUserAAAServerName": jnxUserAAAServerName,
       "jnxUserAAAAddressPoolName": jnxUserAAAAddressPoolName,
       "jnxUserAAAAccessPool": jnxUserAAAAccessPool,
       "jnxUserAAAAccessPoolGeneral": jnxUserAAAAccessPoolGeneral,
       "jnxUserAAAAccessPoolTable": jnxUserAAAAccessPoolTable,
       "jnxUserAAAAccessPoolEntry": jnxUserAAAAccessPoolEntry,
       "jnxUserAAAAccessPoolIdent": jnxUserAAAAccessPoolIdent,
       "jnxUserAAAAccessPoolRoutingInstance": jnxUserAAAAccessPoolRoutingInstance,
       "jnxUserAAAAccessPoolName": jnxUserAAAAccessPoolName,
       "jnxUserAAAAccessPoolLinkName": jnxUserAAAAccessPoolLinkName,
       "jnxUserAAAAccessPoolFamilyType": jnxUserAAAAccessPoolFamilyType,
       "jnxUserAAAAccessPoolInetNetwork": jnxUserAAAAccessPoolInetNetwork,
       "jnxUserAAAAccessPoolInetPrefixLength": jnxUserAAAAccessPoolInetPrefixLength,
       "jnxUserAAAAccessPoolOutOfMemory": jnxUserAAAAccessPoolOutOfMemory,
       "jnxUserAAAAccessPoolOutOfAddresses": jnxUserAAAAccessPoolOutOfAddresses,
       "jnxUserAAAAccessPoolAddressTotal": jnxUserAAAAccessPoolAddressTotal,
       "jnxUserAAAAccessPoolAddressesInUse": jnxUserAAAAccessPoolAddressesInUse,
       "jnxUserAAAAccessPoolAddressUsage": jnxUserAAAAccessPoolAddressUsage,
       "jnxUserAAAAccessPoolAddressUsageHigh": jnxUserAAAAccessPoolAddressUsageHigh,
       "jnxUserAAAAccessPoolAddressUsageAbate": jnxUserAAAAccessPoolAddressUsageAbate,
       "jnxUserAAAAssignment": jnxUserAAAAssignment,
       "jnxUserAAAGeneral": jnxUserAAAGeneral,
       "jnxUserAAADomainDelimiters": jnxUserAAADomainDelimiters,
       "jnxUserAAADomainParseDirection": jnxUserAAADomainParseDirection,
       "jnxUserAAADomain": jnxUserAAADomain,
       "jnxUserAAADomainTable": jnxUserAAADomainTable,
       "jnxUserAAADomainEntry": jnxUserAAADomainEntry,
       "jnxUserAAADomainName": jnxUserAAADomainName,
       "jnxUserAAADomainStripDomain": jnxUserAAADomainStripDomain,
       "jnxUserAAADomainLogicalSystem": jnxUserAAADomainLogicalSystem,
       "jnxUserAAADomainRoutingInstance": jnxUserAAADomainRoutingInstance,
       "jnxUserAAADomainAddrPoolName": jnxUserAAADomainAddrPoolName,
       "jnxUserAAADomainDynamicPorfile": jnxUserAAADomainDynamicPorfile,
       "jnxUserAAADomainTargetLogicalSystem": jnxUserAAADomainTargetLogicalSystem,
       "jnxUserAAADomainTargetRoutingInstance": jnxUserAAADomainTargetRoutingInstance,
       "jnxUserAAADomainTunnelProfile": jnxUserAAADomainTunnelProfile,
       "jnxUserAAADomainDynamicProfile": jnxUserAAADomainDynamicProfile,
       "jnxUserAAADomainStripUsername": jnxUserAAADomainStripUsername,
       "jnxUserAAADomainOverridePassword": jnxUserAAADomainOverridePassword,
       "jnxUserAAADomainTunnelTable": jnxUserAAADomainTunnelTable,
       "jnxUserAAADomainTunnelEntry": jnxUserAAADomainTunnelEntry,
       "jnxUserAAADomainTunnelName": jnxUserAAADomainTunnelName,
       "jnxUserAAADomainTunnelDefId": jnxUserAAADomainTunnelDefId,
       "jnxUserAAADomainTunnelPreference": jnxUserAAADomainTunnelPreference,
       "jnxUserAAADomainTunnelRemoteGwName": jnxUserAAADomainTunnelRemoteGwName,
       "jnxUserAAADomainTunnelRemoteGwAddress": jnxUserAAADomainTunnelRemoteGwAddress,
       "jnxUserAAADomainTunnelSourceGwName": jnxUserAAADomainTunnelSourceGwName,
       "jnxUserAAADomainTunnelSourceGwAddress": jnxUserAAADomainTunnelSourceGwAddress,
       "jnxUserAAADomainTunnelSecret": jnxUserAAADomainTunnelSecret,
       "jnxUserAAADomainTunnelLogicalSystems": jnxUserAAADomainTunnelLogicalSystems,
       "jnxUserAAADomainTunnelRoutingInstance": jnxUserAAADomainTunnelRoutingInstance,
       "jnxUserAAADomainTunnelMedium": jnxUserAAADomainTunnelMedium,
       "jnxUserAAADomainTunnelType": jnxUserAAADomainTunnelType,
       "jnxUserAAADomainTunnelId": jnxUserAAADomainTunnelId,
       "jnxUserAAADomainTunnelMaxSessions": jnxUserAAADomainTunnelMaxSessions,
       "jnxUserAAADomainPadnTable": jnxUserAAADomainPadnTable,
       "jnxUserAAADomainPadnEntry": jnxUserAAADomainPadnEntry,
       "jnxUserAAADomainPadnIpAddress": jnxUserAAADomainPadnIpAddress,
       "jnxUserAAADomainPadnIpMask": jnxUserAAADomainPadnIpMask,
       "jnxUserAAADomainPadnDistance": jnxUserAAADomainPadnDistance,
       "jnxUserAAAAccessProfile": jnxUserAAAAccessProfile,
       "jnxUserAAAAccessProfileGeneral": jnxUserAAAAccessProfileGeneral,
       "jnxUserAAAAccessProfileTable": jnxUserAAAAccessProfileTable,
       "jnxUserAAAAccessProfileEntry": jnxUserAAAAccessProfileEntry,
       "jnxUserAAAAccessProfileName": jnxUserAAAAccessProfileName,
       "jnxUserAAAAccessProfileAuthenticationOrder": jnxUserAAAAccessProfileAuthenticationOrder,
       "jnxUserAAAAccessProfileAccountingOrder": jnxUserAAAAccessProfileAccountingOrder,
       "jnxUserAAAAccessProfileAuthorizationOrder": jnxUserAAAAccessProfileAuthorizationOrder,
       "jnxUserAAAAccessProfileProvisioningOrder": jnxUserAAAAccessProfileProvisioningOrder,
       "jnxUserAAAAccessProfileAccStopOnFailure": jnxUserAAAAccessProfileAccStopOnFailure,
       "jnxUserAAAAccessProfileAccStopOnDeny": jnxUserAAAAccessProfileAccStopOnDeny,
       "jnxUserAAAAccessProfileImmediateUpdate": jnxUserAAAAccessProfileImmediateUpdate,
       "jnxUserAAAAccessProfileCoaImmediateUpdate": jnxUserAAAAccessProfileCoaImmediateUpdate,
       "jnxUserAAAAccessProfileInterval": jnxUserAAAAccessProfileInterval,
       "jnxUserAAAAccessProfileStatType": jnxUserAAAAccessProfileStatType}
)
