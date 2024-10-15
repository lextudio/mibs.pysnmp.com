# SNMP MIB module (SIP-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SIP-SERVER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:52:24 2024
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
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(applIndex,) = mibBuilder.importSymbols(
    "NETWORK-SERVICES-MIB",
    "applIndex")

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

(DateAndTime,
 DisplayString,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

sipServerMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 151)
)
sipServerMIB.setRevisions(
        ("2007-04-20 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SipServerMIBObjects_ObjectIdentity = ObjectIdentity
sipServerMIBObjects = _SipServerMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 151, 1)
)
_SipServerCfg_ObjectIdentity = ObjectIdentity
sipServerCfg = _SipServerCfg_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 151, 1, 1)
)
_SipServerCfgTable_Object = MibTable
sipServerCfgTable = _SipServerCfgTable_Object(
    (1, 3, 6, 1, 2, 1, 151, 1, 1, 1)
)
if mibBuilder.loadTexts:
    sipServerCfgTable.setStatus("current")
_SipServerCfgEntry_Object = MibTableRow
sipServerCfgEntry = _SipServerCfgEntry_Object(
    (1, 3, 6, 1, 2, 1, 151, 1, 1, 1, 1)
)
sipServerCfgEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
)
if mibBuilder.loadTexts:
    sipServerCfgEntry.setStatus("current")
_SipServerCfgHostAddressType_Type = InetAddressType
_SipServerCfgHostAddressType_Object = MibTableColumn
sipServerCfgHostAddressType = _SipServerCfgHostAddressType_Object(
    (1, 3, 6, 1, 2, 1, 151, 1, 1, 1, 1, 1),
    _SipServerCfgHostAddressType_Type()
)
sipServerCfgHostAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipServerCfgHostAddressType.setStatus("current")
_SipServerCfgHostAddress_Type = InetAddress
_SipServerCfgHostAddress_Object = MibTableColumn
sipServerCfgHostAddress = _SipServerCfgHostAddress_Object(
    (1, 3, 6, 1, 2, 1, 151, 1, 1, 1, 1, 2),
    _SipServerCfgHostAddress_Type()
)
sipServerCfgHostAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipServerCfgHostAddress.setStatus("current")
_SipServerProxyCfg_ObjectIdentity = ObjectIdentity
sipServerProxyCfg = _SipServerProxyCfg_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 151, 1, 3)
)
_SipServerProxyCfgTable_Object = MibTable
sipServerProxyCfgTable = _SipServerProxyCfgTable_Object(
    (1, 3, 6, 1, 2, 1, 151, 1, 3, 1)
)
if mibBuilder.loadTexts:
    sipServerProxyCfgTable.setStatus("current")
_SipServerProxyCfgEntry_Object = MibTableRow
sipServerProxyCfgEntry = _SipServerProxyCfgEntry_Object(
    (1, 3, 6, 1, 2, 1, 151, 1, 3, 1, 1)
)
sipServerProxyCfgEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
)
if mibBuilder.loadTexts:
    sipServerProxyCfgEntry.setStatus("current")


class _SipServerCfgProxyStatefulness_Type(Integer32):
    """Custom type sipServerCfgProxyStatefulness based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("callStateful", 3),
          ("stateless", 1),
          ("transactionStateful", 2))
    )


_SipServerCfgProxyStatefulness_Type.__name__ = "Integer32"
_SipServerCfgProxyStatefulness_Object = MibTableColumn
sipServerCfgProxyStatefulness = _SipServerCfgProxyStatefulness_Object(
    (1, 3, 6, 1, 2, 1, 151, 1, 3, 1, 1, 1),
    _SipServerCfgProxyStatefulness_Type()
)
sipServerCfgProxyStatefulness.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipServerCfgProxyStatefulness.setStatus("current")
_SipServerCfgProxyRecursion_Type = TruthValue
_SipServerCfgProxyRecursion_Object = MibTableColumn
sipServerCfgProxyRecursion = _SipServerCfgProxyRecursion_Object(
    (1, 3, 6, 1, 2, 1, 151, 1, 3, 1, 1, 2),
    _SipServerCfgProxyRecursion_Type()
)
sipServerCfgProxyRecursion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipServerCfgProxyRecursion.setStatus("current")
_SipServerCfgProxyRecordRoute_Type = TruthValue
_SipServerCfgProxyRecordRoute_Object = MibTableColumn
sipServerCfgProxyRecordRoute = _SipServerCfgProxyRecordRoute_Object(
    (1, 3, 6, 1, 2, 1, 151, 1, 3, 1, 1, 3),
    _SipServerCfgProxyRecordRoute_Type()
)
sipServerCfgProxyRecordRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipServerCfgProxyRecordRoute.setStatus("current")


class _SipServerCfgProxyAuthMethod_Type(Bits):
    """Custom type sipServerCfgProxyAuthMethod based on Bits"""
    namedValues = NamedValues(
        *(("digest", 2),
          ("none", 0),
          ("tls", 1))
    )

_SipServerCfgProxyAuthMethod_Type.__name__ = "Bits"
_SipServerCfgProxyAuthMethod_Object = MibTableColumn
sipServerCfgProxyAuthMethod = _SipServerCfgProxyAuthMethod_Object(
    (1, 3, 6, 1, 2, 1, 151, 1, 3, 1, 1, 4),
    _SipServerCfgProxyAuthMethod_Type()
)
sipServerCfgProxyAuthMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipServerCfgProxyAuthMethod.setStatus("current")
_SipServerCfgProxyAuthDefaultRealm_Type = SnmpAdminString
_SipServerCfgProxyAuthDefaultRealm_Object = MibTableColumn
sipServerCfgProxyAuthDefaultRealm = _SipServerCfgProxyAuthDefaultRealm_Object(
    (1, 3, 6, 1, 2, 1, 151, 1, 3, 1, 1, 5),
    _SipServerCfgProxyAuthDefaultRealm_Type()
)
sipServerCfgProxyAuthDefaultRealm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipServerCfgProxyAuthDefaultRealm.setStatus("current")
_SipServerProxyStats_ObjectIdentity = ObjectIdentity
sipServerProxyStats = _SipServerProxyStats_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 151, 1, 4)
)
_SipServerProxyStatsTable_Object = MibTable
sipServerProxyStatsTable = _SipServerProxyStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 151, 1, 4, 1)
)
if mibBuilder.loadTexts:
    sipServerProxyStatsTable.setStatus("current")
_SipServerProxyStatsEntry_Object = MibTableRow
sipServerProxyStatsEntry = _SipServerProxyStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 151, 1, 4, 1, 1)
)
sipServerProxyStatsEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
)
if mibBuilder.loadTexts:
    sipServerProxyStatsEntry.setStatus("current")
_SipServerProxyStatProxyReqFailures_Type = Counter32
_SipServerProxyStatProxyReqFailures_Object = MibTableColumn
sipServerProxyStatProxyReqFailures = _SipServerProxyStatProxyReqFailures_Object(
    (1, 3, 6, 1, 2, 1, 151, 1, 4, 1, 1, 1),
    _SipServerProxyStatProxyReqFailures_Type()
)
sipServerProxyStatProxyReqFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipServerProxyStatProxyReqFailures.setStatus("current")
_SipServerProxyStatsDisconTime_Type = TimeStamp
_SipServerProxyStatsDisconTime_Object = MibTableColumn
sipServerProxyStatsDisconTime = _SipServerProxyStatsDisconTime_Object(
    (1, 3, 6, 1, 2, 1, 151, 1, 4, 1, 1, 2),
    _SipServerProxyStatsDisconTime_Type()
)
sipServerProxyStatsDisconTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipServerProxyStatsDisconTime.setStatus("current")
_SipServerRegCfg_ObjectIdentity = ObjectIdentity
sipServerRegCfg = _SipServerRegCfg_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 151, 1, 5)
)
_SipServerRegCfgTable_Object = MibTable
sipServerRegCfgTable = _SipServerRegCfgTable_Object(
    (1, 3, 6, 1, 2, 1, 151, 1, 5, 1)
)
if mibBuilder.loadTexts:
    sipServerRegCfgTable.setStatus("current")
_SipServerRegCfgEntry_Object = MibTableRow
sipServerRegCfgEntry = _SipServerRegCfgEntry_Object(
    (1, 3, 6, 1, 2, 1, 151, 1, 5, 1, 1)
)
sipServerRegCfgEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
)
if mibBuilder.loadTexts:
    sipServerRegCfgEntry.setStatus("current")


class _SipServerRegMaxContactExpiryDuration_Type(Unsigned32):
    """Custom type sipServerRegMaxContactExpiryDuration based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SipServerRegMaxContactExpiryDuration_Type.__name__ = "Unsigned32"
_SipServerRegMaxContactExpiryDuration_Object = MibTableColumn
sipServerRegMaxContactExpiryDuration = _SipServerRegMaxContactExpiryDuration_Object(
    (1, 3, 6, 1, 2, 1, 151, 1, 5, 1, 1, 1),
    _SipServerRegMaxContactExpiryDuration_Type()
)
sipServerRegMaxContactExpiryDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipServerRegMaxContactExpiryDuration.setStatus("current")
if mibBuilder.loadTexts:
    sipServerRegMaxContactExpiryDuration.setUnits("seconds")


class _SipServerRegMaxUsers_Type(Unsigned32):
    """Custom type sipServerRegMaxUsers based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SipServerRegMaxUsers_Type.__name__ = "Unsigned32"
_SipServerRegMaxUsers_Object = MibTableColumn
sipServerRegMaxUsers = _SipServerRegMaxUsers_Object(
    (1, 3, 6, 1, 2, 1, 151, 1, 5, 1, 1, 2),
    _SipServerRegMaxUsers_Type()
)
sipServerRegMaxUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipServerRegMaxUsers.setStatus("current")


class _SipServerRegCurrentUsers_Type(Gauge32):
    """Custom type sipServerRegCurrentUsers based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SipServerRegCurrentUsers_Type.__name__ = "Gauge32"
_SipServerRegCurrentUsers_Object = MibTableColumn
sipServerRegCurrentUsers = _SipServerRegCurrentUsers_Object(
    (1, 3, 6, 1, 2, 1, 151, 1, 5, 1, 1, 3),
    _SipServerRegCurrentUsers_Type()
)
sipServerRegCurrentUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipServerRegCurrentUsers.setStatus("current")


class _SipServerRegDfltRegActiveInterval_Type(Unsigned32):
    """Custom type sipServerRegDfltRegActiveInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SipServerRegDfltRegActiveInterval_Type.__name__ = "Unsigned32"
_SipServerRegDfltRegActiveInterval_Object = MibTableColumn
sipServerRegDfltRegActiveInterval = _SipServerRegDfltRegActiveInterval_Object(
    (1, 3, 6, 1, 2, 1, 151, 1, 5, 1, 1, 4),
    _SipServerRegDfltRegActiveInterval_Type()
)
sipServerRegDfltRegActiveInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipServerRegDfltRegActiveInterval.setStatus("current")
if mibBuilder.loadTexts:
    sipServerRegDfltRegActiveInterval.setUnits("seconds")
_SipServerRegUserTable_Object = MibTable
sipServerRegUserTable = _SipServerRegUserTable_Object(
    (1, 3, 6, 1, 2, 1, 151, 1, 5, 2)
)
if mibBuilder.loadTexts:
    sipServerRegUserTable.setStatus("current")
_SipServerRegUserEntry_Object = MibTableRow
sipServerRegUserEntry = _SipServerRegUserEntry_Object(
    (1, 3, 6, 1, 2, 1, 151, 1, 5, 2, 1)
)
sipServerRegUserEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
    (0, "SIP-SERVER-MIB", "sipServerRegUserIndex"),
)
if mibBuilder.loadTexts:
    sipServerRegUserEntry.setStatus("current")


class _SipServerRegUserIndex_Type(Unsigned32):
    """Custom type sipServerRegUserIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SipServerRegUserIndex_Type.__name__ = "Unsigned32"
_SipServerRegUserIndex_Object = MibTableColumn
sipServerRegUserIndex = _SipServerRegUserIndex_Object(
    (1, 3, 6, 1, 2, 1, 151, 1, 5, 2, 1, 1),
    _SipServerRegUserIndex_Type()
)
sipServerRegUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sipServerRegUserIndex.setStatus("current")
_SipServerRegUserUri_Type = SnmpAdminString
_SipServerRegUserUri_Object = MibTableColumn
sipServerRegUserUri = _SipServerRegUserUri_Object(
    (1, 3, 6, 1, 2, 1, 151, 1, 5, 2, 1, 2),
    _SipServerRegUserUri_Type()
)
sipServerRegUserUri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipServerRegUserUri.setStatus("current")
_SipServerRegUserAuthenticationFailures_Type = Counter32
_SipServerRegUserAuthenticationFailures_Object = MibTableColumn
sipServerRegUserAuthenticationFailures = _SipServerRegUserAuthenticationFailures_Object(
    (1, 3, 6, 1, 2, 1, 151, 1, 5, 2, 1, 3),
    _SipServerRegUserAuthenticationFailures_Type()
)
sipServerRegUserAuthenticationFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipServerRegUserAuthenticationFailures.setStatus("current")
_SipServerRegUserDisconTime_Type = TimeStamp
_SipServerRegUserDisconTime_Object = MibTableColumn
sipServerRegUserDisconTime = _SipServerRegUserDisconTime_Object(
    (1, 3, 6, 1, 2, 1, 151, 1, 5, 2, 1, 4),
    _SipServerRegUserDisconTime_Type()
)
sipServerRegUserDisconTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipServerRegUserDisconTime.setStatus("current")
_SipServerRegContactTable_Object = MibTable
sipServerRegContactTable = _SipServerRegContactTable_Object(
    (1, 3, 6, 1, 2, 1, 151, 1, 5, 3)
)
if mibBuilder.loadTexts:
    sipServerRegContactTable.setStatus("current")
_SipServerRegContactEntry_Object = MibTableRow
sipServerRegContactEntry = _SipServerRegContactEntry_Object(
    (1, 3, 6, 1, 2, 1, 151, 1, 5, 3, 1)
)
sipServerRegContactEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
    (0, "SIP-SERVER-MIB", "sipServerRegUserIndex"),
    (0, "SIP-SERVER-MIB", "sipServerRegContactIndex"),
)
if mibBuilder.loadTexts:
    sipServerRegContactEntry.setStatus("current")


class _SipServerRegContactIndex_Type(Unsigned32):
    """Custom type sipServerRegContactIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SipServerRegContactIndex_Type.__name__ = "Unsigned32"
_SipServerRegContactIndex_Object = MibTableColumn
sipServerRegContactIndex = _SipServerRegContactIndex_Object(
    (1, 3, 6, 1, 2, 1, 151, 1, 5, 3, 1, 1),
    _SipServerRegContactIndex_Type()
)
sipServerRegContactIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sipServerRegContactIndex.setStatus("current")
_SipServerRegContactDisplayName_Type = SnmpAdminString
_SipServerRegContactDisplayName_Object = MibTableColumn
sipServerRegContactDisplayName = _SipServerRegContactDisplayName_Object(
    (1, 3, 6, 1, 2, 1, 151, 1, 5, 3, 1, 2),
    _SipServerRegContactDisplayName_Type()
)
sipServerRegContactDisplayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipServerRegContactDisplayName.setStatus("current")
_SipServerRegContactURI_Type = SnmpAdminString
_SipServerRegContactURI_Object = MibTableColumn
sipServerRegContactURI = _SipServerRegContactURI_Object(
    (1, 3, 6, 1, 2, 1, 151, 1, 5, 3, 1, 3),
    _SipServerRegContactURI_Type()
)
sipServerRegContactURI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipServerRegContactURI.setStatus("current")
_SipServerRegContactLastUpdated_Type = TimeStamp
_SipServerRegContactLastUpdated_Object = MibTableColumn
sipServerRegContactLastUpdated = _SipServerRegContactLastUpdated_Object(
    (1, 3, 6, 1, 2, 1, 151, 1, 5, 3, 1, 4),
    _SipServerRegContactLastUpdated_Type()
)
sipServerRegContactLastUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipServerRegContactLastUpdated.setStatus("current")
_SipServerRegContactExpiry_Type = DateAndTime
_SipServerRegContactExpiry_Object = MibTableColumn
sipServerRegContactExpiry = _SipServerRegContactExpiry_Object(
    (1, 3, 6, 1, 2, 1, 151, 1, 5, 3, 1, 5),
    _SipServerRegContactExpiry_Type()
)
sipServerRegContactExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipServerRegContactExpiry.setStatus("current")
_SipServerRegContactPreference_Type = SnmpAdminString
_SipServerRegContactPreference_Object = MibTableColumn
sipServerRegContactPreference = _SipServerRegContactPreference_Object(
    (1, 3, 6, 1, 2, 1, 151, 1, 5, 3, 1, 6),
    _SipServerRegContactPreference_Type()
)
sipServerRegContactPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipServerRegContactPreference.setStatus("current")
_SipServerRegStats_ObjectIdentity = ObjectIdentity
sipServerRegStats = _SipServerRegStats_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 151, 1, 6)
)
_SipServerRegStatsTable_Object = MibTable
sipServerRegStatsTable = _SipServerRegStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 151, 1, 6, 1)
)
if mibBuilder.loadTexts:
    sipServerRegStatsTable.setStatus("current")
_SipServerRegStatsEntry_Object = MibTableRow
sipServerRegStatsEntry = _SipServerRegStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 151, 1, 6, 1, 1)
)
sipServerRegStatsEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
)
if mibBuilder.loadTexts:
    sipServerRegStatsEntry.setStatus("current")
_SipServerRegStatsAcceptedRegs_Type = Counter32
_SipServerRegStatsAcceptedRegs_Object = MibTableColumn
sipServerRegStatsAcceptedRegs = _SipServerRegStatsAcceptedRegs_Object(
    (1, 3, 6, 1, 2, 1, 151, 1, 6, 1, 1, 1),
    _SipServerRegStatsAcceptedRegs_Type()
)
sipServerRegStatsAcceptedRegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipServerRegStatsAcceptedRegs.setStatus("current")
_SipServerRegStatsRejectedRegs_Type = Counter32
_SipServerRegStatsRejectedRegs_Object = MibTableColumn
sipServerRegStatsRejectedRegs = _SipServerRegStatsRejectedRegs_Object(
    (1, 3, 6, 1, 2, 1, 151, 1, 6, 1, 1, 2),
    _SipServerRegStatsRejectedRegs_Type()
)
sipServerRegStatsRejectedRegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipServerRegStatsRejectedRegs.setStatus("current")
_SipServerRegStatsDisconTime_Type = TimeStamp
_SipServerRegStatsDisconTime_Object = MibTableColumn
sipServerRegStatsDisconTime = _SipServerRegStatsDisconTime_Object(
    (1, 3, 6, 1, 2, 1, 151, 1, 6, 1, 1, 3),
    _SipServerRegStatsDisconTime_Type()
)
sipServerRegStatsDisconTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sipServerRegStatsDisconTime.setStatus("current")
_SipServerMIBConformance_ObjectIdentity = ObjectIdentity
sipServerMIBConformance = _SipServerMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 151, 2)
)
_SipServerMIBCompliances_ObjectIdentity = ObjectIdentity
sipServerMIBCompliances = _SipServerMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 151, 2, 1)
)
_SipServerMIBGroups_ObjectIdentity = ObjectIdentity
sipServerMIBGroups = _SipServerMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 151, 2, 2)
)

# Managed Objects groups

sipServerConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 151, 2, 2, 1)
)
sipServerConfigGroup.setObjects(
      *(("SIP-SERVER-MIB", "sipServerCfgHostAddressType"),
        ("SIP-SERVER-MIB", "sipServerCfgHostAddress"))
)
if mibBuilder.loadTexts:
    sipServerConfigGroup.setStatus("current")

sipServerProxyConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 151, 2, 2, 2)
)
sipServerProxyConfigGroup.setObjects(
      *(("SIP-SERVER-MIB", "sipServerCfgProxyStatefulness"),
        ("SIP-SERVER-MIB", "sipServerCfgProxyRecursion"),
        ("SIP-SERVER-MIB", "sipServerCfgProxyRecordRoute"),
        ("SIP-SERVER-MIB", "sipServerCfgProxyAuthMethod"),
        ("SIP-SERVER-MIB", "sipServerCfgProxyAuthDefaultRealm"))
)
if mibBuilder.loadTexts:
    sipServerProxyConfigGroup.setStatus("current")

sipServerProxyStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 151, 2, 2, 3)
)
sipServerProxyStatsGroup.setObjects(
      *(("SIP-SERVER-MIB", "sipServerProxyStatProxyReqFailures"),
        ("SIP-SERVER-MIB", "sipServerProxyStatsDisconTime"))
)
if mibBuilder.loadTexts:
    sipServerProxyStatsGroup.setStatus("current")

sipServerRegistrarConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 151, 2, 2, 4)
)
sipServerRegistrarConfigGroup.setObjects(
      *(("SIP-SERVER-MIB", "sipServerRegMaxContactExpiryDuration"),
        ("SIP-SERVER-MIB", "sipServerRegMaxUsers"),
        ("SIP-SERVER-MIB", "sipServerRegCurrentUsers"),
        ("SIP-SERVER-MIB", "sipServerRegDfltRegActiveInterval"))
)
if mibBuilder.loadTexts:
    sipServerRegistrarConfigGroup.setStatus("current")

sipServerRegistrarStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 151, 2, 2, 5)
)
sipServerRegistrarStatsGroup.setObjects(
      *(("SIP-SERVER-MIB", "sipServerRegStatsAcceptedRegs"),
        ("SIP-SERVER-MIB", "sipServerRegStatsRejectedRegs"),
        ("SIP-SERVER-MIB", "sipServerRegStatsDisconTime"))
)
if mibBuilder.loadTexts:
    sipServerRegistrarStatsGroup.setStatus("current")

sipServerRegistrarUsersGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 151, 2, 2, 6)
)
sipServerRegistrarUsersGroup.setObjects(
      *(("SIP-SERVER-MIB", "sipServerRegUserUri"),
        ("SIP-SERVER-MIB", "sipServerRegUserAuthenticationFailures"),
        ("SIP-SERVER-MIB", "sipServerRegUserDisconTime"),
        ("SIP-SERVER-MIB", "sipServerRegContactDisplayName"),
        ("SIP-SERVER-MIB", "sipServerRegContactURI"),
        ("SIP-SERVER-MIB", "sipServerRegContactLastUpdated"),
        ("SIP-SERVER-MIB", "sipServerRegContactExpiry"),
        ("SIP-SERVER-MIB", "sipServerRegContactPreference"))
)
if mibBuilder.loadTexts:
    sipServerRegistrarUsersGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

sipServerProxyServerCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 151, 2, 1, 1)
)
if mibBuilder.loadTexts:
    sipServerProxyServerCompliance.setStatus(
        "current"
    )

sipRedirectServerCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 151, 2, 1, 2)
)
if mibBuilder.loadTexts:
    sipRedirectServerCompliance.setStatus(
        "current"
    )

sipServerRegistrarServerCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 151, 2, 1, 3)
)
if mibBuilder.loadTexts:
    sipServerRegistrarServerCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SIP-SERVER-MIB",
    **{"sipServerMIB": sipServerMIB,
       "sipServerMIBObjects": sipServerMIBObjects,
       "sipServerCfg": sipServerCfg,
       "sipServerCfgTable": sipServerCfgTable,
       "sipServerCfgEntry": sipServerCfgEntry,
       "sipServerCfgHostAddressType": sipServerCfgHostAddressType,
       "sipServerCfgHostAddress": sipServerCfgHostAddress,
       "sipServerProxyCfg": sipServerProxyCfg,
       "sipServerProxyCfgTable": sipServerProxyCfgTable,
       "sipServerProxyCfgEntry": sipServerProxyCfgEntry,
       "sipServerCfgProxyStatefulness": sipServerCfgProxyStatefulness,
       "sipServerCfgProxyRecursion": sipServerCfgProxyRecursion,
       "sipServerCfgProxyRecordRoute": sipServerCfgProxyRecordRoute,
       "sipServerCfgProxyAuthMethod": sipServerCfgProxyAuthMethod,
       "sipServerCfgProxyAuthDefaultRealm": sipServerCfgProxyAuthDefaultRealm,
       "sipServerProxyStats": sipServerProxyStats,
       "sipServerProxyStatsTable": sipServerProxyStatsTable,
       "sipServerProxyStatsEntry": sipServerProxyStatsEntry,
       "sipServerProxyStatProxyReqFailures": sipServerProxyStatProxyReqFailures,
       "sipServerProxyStatsDisconTime": sipServerProxyStatsDisconTime,
       "sipServerRegCfg": sipServerRegCfg,
       "sipServerRegCfgTable": sipServerRegCfgTable,
       "sipServerRegCfgEntry": sipServerRegCfgEntry,
       "sipServerRegMaxContactExpiryDuration": sipServerRegMaxContactExpiryDuration,
       "sipServerRegMaxUsers": sipServerRegMaxUsers,
       "sipServerRegCurrentUsers": sipServerRegCurrentUsers,
       "sipServerRegDfltRegActiveInterval": sipServerRegDfltRegActiveInterval,
       "sipServerRegUserTable": sipServerRegUserTable,
       "sipServerRegUserEntry": sipServerRegUserEntry,
       "sipServerRegUserIndex": sipServerRegUserIndex,
       "sipServerRegUserUri": sipServerRegUserUri,
       "sipServerRegUserAuthenticationFailures": sipServerRegUserAuthenticationFailures,
       "sipServerRegUserDisconTime": sipServerRegUserDisconTime,
       "sipServerRegContactTable": sipServerRegContactTable,
       "sipServerRegContactEntry": sipServerRegContactEntry,
       "sipServerRegContactIndex": sipServerRegContactIndex,
       "sipServerRegContactDisplayName": sipServerRegContactDisplayName,
       "sipServerRegContactURI": sipServerRegContactURI,
       "sipServerRegContactLastUpdated": sipServerRegContactLastUpdated,
       "sipServerRegContactExpiry": sipServerRegContactExpiry,
       "sipServerRegContactPreference": sipServerRegContactPreference,
       "sipServerRegStats": sipServerRegStats,
       "sipServerRegStatsTable": sipServerRegStatsTable,
       "sipServerRegStatsEntry": sipServerRegStatsEntry,
       "sipServerRegStatsAcceptedRegs": sipServerRegStatsAcceptedRegs,
       "sipServerRegStatsRejectedRegs": sipServerRegStatsRejectedRegs,
       "sipServerRegStatsDisconTime": sipServerRegStatsDisconTime,
       "sipServerMIBConformance": sipServerMIBConformance,
       "sipServerMIBCompliances": sipServerMIBCompliances,
       "sipServerProxyServerCompliance": sipServerProxyServerCompliance,
       "sipRedirectServerCompliance": sipRedirectServerCompliance,
       "sipServerRegistrarServerCompliance": sipServerRegistrarServerCompliance,
       "sipServerMIBGroups": sipServerMIBGroups,
       "sipServerConfigGroup": sipServerConfigGroup,
       "sipServerProxyConfigGroup": sipServerProxyConfigGroup,
       "sipServerProxyStatsGroup": sipServerProxyStatsGroup,
       "sipServerRegistrarConfigGroup": sipServerRegistrarConfigGroup,
       "sipServerRegistrarStatsGroup": sipServerRegistrarStatsGroup,
       "sipServerRegistrarUsersGroup": sipServerRegistrarUsersGroup}
)
