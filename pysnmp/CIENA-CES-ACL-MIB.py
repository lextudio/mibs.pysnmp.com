# SNMP MIB module (CIENA-CES-ACL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CIENA-CES-ACL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:54:52 2024
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

(cienaCesConfig,) = mibBuilder.importSymbols(
    "CIENA-SMI",
    "cienaCesConfig")

(CienaGlobalState,) = mibBuilder.importSymbols(
    "CIENA-TC",
    "CienaGlobalState")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

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

cienaCesAclMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 25)
)
cienaCesAclMIB.setRevisions(
        ("2012-11-21 00:00",
         "2012-05-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CienaCesAclMIBObjects_ObjectIdentity = ObjectIdentity
cienaCesAclMIBObjects = _CienaCesAclMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 25, 1)
)
_CienaCesAclGlobal_ObjectIdentity = ObjectIdentity
cienaCesAclGlobal = _CienaCesAclGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 25, 1, 1)
)
_CienaCesAclAdminState_Type = CienaGlobalState
_CienaCesAclAdminState_Object = MibScalar
cienaCesAclAdminState = _CienaCesAclAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 25, 1, 1, 1),
    _CienaCesAclAdminState_Type()
)
cienaCesAclAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclAdminState.setStatus("current")
_CienaCesAclCacheHit_Type = Counter32
_CienaCesAclCacheHit_Object = MibScalar
cienaCesAclCacheHit = _CienaCesAclCacheHit_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 25, 1, 1, 2),
    _CienaCesAclCacheHit_Type()
)
cienaCesAclCacheHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclCacheHit.setStatus("current")
_CienaCesAclNoHit_Type = Counter32
_CienaCesAclNoHit_Object = MibScalar
cienaCesAclNoHit = _CienaCesAclNoHit_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 25, 1, 1, 3),
    _CienaCesAclNoHit_Type()
)
cienaCesAclNoHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclNoHit.setStatus("current")
_CienaCesAclBadPort_Type = Counter32
_CienaCesAclBadPort_Object = MibScalar
cienaCesAclBadPort = _CienaCesAclBadPort_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 25, 1, 1, 4),
    _CienaCesAclBadPort_Type()
)
cienaCesAclBadPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclBadPort.setStatus("current")
_CienaCesAclBadDscp_Type = Counter32
_CienaCesAclBadDscp_Object = MibScalar
cienaCesAclBadDscp = _CienaCesAclBadDscp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 25, 1, 1, 5),
    _CienaCesAclBadDscp_Type()
)
cienaCesAclBadDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclBadDscp.setStatus("current")
_CienaCesAclOperState_Type = CienaGlobalState
_CienaCesAclOperState_Object = MibScalar
cienaCesAclOperState = _CienaCesAclOperState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 25, 1, 1, 6),
    _CienaCesAclOperState_Type()
)
cienaCesAclOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclOperState.setStatus("current")
_CienaCesAclInUseEntries_Type = Counter32
_CienaCesAclInUseEntries_Object = MibScalar
cienaCesAclInUseEntries = _CienaCesAclInUseEntries_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 25, 1, 1, 7),
    _CienaCesAclInUseEntries_Type()
)
cienaCesAclInUseEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclInUseEntries.setStatus("current")
_CienaCesAclMaxEntries_Type = Counter32
_CienaCesAclMaxEntries_Object = MibScalar
cienaCesAclMaxEntries = _CienaCesAclMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 25, 1, 1, 8),
    _CienaCesAclMaxEntries_Type()
)
cienaCesAclMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclMaxEntries.setStatus("current")
_CienaCesAclBadProtocol_Type = Counter32
_CienaCesAclBadProtocol_Object = MibScalar
cienaCesAclBadProtocol = _CienaCesAclBadProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 25, 1, 1, 9),
    _CienaCesAclBadProtocol_Type()
)
cienaCesAclBadProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclBadProtocol.setStatus("current")
_CienaCesAclRules_ObjectIdentity = ObjectIdentity
cienaCesAclRules = _CienaCesAclRules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 25, 1, 2)
)
_CienaCesAclTable_Object = MibTable
cienaCesAclTable = _CienaCesAclTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 25, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cienaCesAclTable.setStatus("deprecated")
_CienaCesAclEntry_Object = MibTableRow
cienaCesAclEntry = _CienaCesAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 25, 1, 2, 1, 1)
)
cienaCesAclEntry.setIndexNames(
    (0, "CIENA-CES-ACL-MIB", "cienaCesAclEntryInetAddrType"),
    (0, "CIENA-CES-ACL-MIB", "cienaCesAclEntryInetAddr"),
    (0, "CIENA-CES-ACL-MIB", "cienaCesAclEntryInetPrefixLength"),
)
if mibBuilder.loadTexts:
    cienaCesAclEntry.setStatus("deprecated")
_CienaCesAclEntryInetAddrType_Type = InetAddressType
_CienaCesAclEntryInetAddrType_Object = MibTableColumn
cienaCesAclEntryInetAddrType = _CienaCesAclEntryInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 25, 1, 2, 1, 1, 1),
    _CienaCesAclEntryInetAddrType_Type()
)
cienaCesAclEntryInetAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesAclEntryInetAddrType.setStatus("deprecated")
_CienaCesAclEntryInetAddr_Type = InetAddress
_CienaCesAclEntryInetAddr_Object = MibTableColumn
cienaCesAclEntryInetAddr = _CienaCesAclEntryInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 25, 1, 2, 1, 1, 2),
    _CienaCesAclEntryInetAddr_Type()
)
cienaCesAclEntryInetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclEntryInetAddr.setStatus("deprecated")
_CienaCesAclEntryInetPrefixLength_Type = InetAddressPrefixLength
_CienaCesAclEntryInetPrefixLength_Object = MibTableColumn
cienaCesAclEntryInetPrefixLength = _CienaCesAclEntryInetPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 25, 1, 2, 1, 1, 3),
    _CienaCesAclEntryInetPrefixLength_Type()
)
cienaCesAclEntryInetPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesAclEntryInetPrefixLength.setStatus("deprecated")
_CienaCesAclEntryHits_Type = Counter32
_CienaCesAclEntryHits_Object = MibTableColumn
cienaCesAclEntryHits = _CienaCesAclEntryHits_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 25, 1, 2, 1, 1, 4),
    _CienaCesAclEntryHits_Type()
)
cienaCesAclEntryHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclEntryHits.setStatus("deprecated")
_CienaCesAclEntryBadPort_Type = Counter32
_CienaCesAclEntryBadPort_Object = MibTableColumn
cienaCesAclEntryBadPort = _CienaCesAclEntryBadPort_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 25, 1, 2, 1, 1, 5),
    _CienaCesAclEntryBadPort_Type()
)
cienaCesAclEntryBadPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclEntryBadPort.setStatus("deprecated")


class _CienaCesAclEntryDscpMask_Type(OctetString):
    """Custom type cienaCesAclEntryDscpMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_CienaCesAclEntryDscpMask_Type.__name__ = "OctetString"
_CienaCesAclEntryDscpMask_Object = MibTableColumn
cienaCesAclEntryDscpMask = _CienaCesAclEntryDscpMask_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 25, 1, 2, 1, 1, 6),
    _CienaCesAclEntryDscpMask_Type()
)
cienaCesAclEntryDscpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclEntryDscpMask.setStatus("deprecated")
_CienaCesAclEntryBadDscp_Type = Counter32
_CienaCesAclEntryBadDscp_Object = MibTableColumn
cienaCesAclEntryBadDscp = _CienaCesAclEntryBadDscp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 25, 1, 2, 1, 1, 7),
    _CienaCesAclEntryBadDscp_Type()
)
cienaCesAclEntryBadDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclEntryBadDscp.setStatus("deprecated")


class _CienaCesAclEntryPortBitMask_Type(OctetString):
    """Custom type cienaCesAclEntryPortBitMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_CienaCesAclEntryPortBitMask_Type.__name__ = "OctetString"
_CienaCesAclEntryPortBitMask_Object = MibTableColumn
cienaCesAclEntryPortBitMask = _CienaCesAclEntryPortBitMask_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 25, 1, 2, 1, 1, 8),
    _CienaCesAclEntryPortBitMask_Type()
)
cienaCesAclEntryPortBitMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclEntryPortBitMask.setStatus("deprecated")
_CienaCesAclEntryNotifInetAddrType_Type = InetAddressType
_CienaCesAclEntryNotifInetAddrType_Object = MibTableColumn
cienaCesAclEntryNotifInetAddrType = _CienaCesAclEntryNotifInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 25, 1, 2, 1, 1, 9),
    _CienaCesAclEntryNotifInetAddrType_Type()
)
cienaCesAclEntryNotifInetAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclEntryNotifInetAddrType.setStatus("deprecated")
_CienaCesAclEntryNotifInetAddr_Type = InetAddress
_CienaCesAclEntryNotifInetAddr_Object = MibTableColumn
cienaCesAclEntryNotifInetAddr = _CienaCesAclEntryNotifInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 25, 1, 2, 1, 1, 10),
    _CienaCesAclEntryNotifInetAddr_Type()
)
cienaCesAclEntryNotifInetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclEntryNotifInetAddr.setStatus("deprecated")
_CienaCesAclEntryNotifInetPrefixLength_Type = InetAddressPrefixLength
_CienaCesAclEntryNotifInetPrefixLength_Object = MibTableColumn
cienaCesAclEntryNotifInetPrefixLength = _CienaCesAclEntryNotifInetPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 25, 1, 2, 1, 1, 11),
    _CienaCesAclEntryNotifInetPrefixLength_Type()
)
cienaCesAclEntryNotifInetPrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclEntryNotifInetPrefixLength.setStatus("deprecated")
_CienaCesExtAclTable_Object = MibTable
cienaCesExtAclTable = _CienaCesExtAclTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 25, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cienaCesExtAclTable.setStatus("current")
_CienaCesExtAclEntry_Object = MibTableRow
cienaCesExtAclEntry = _CienaCesExtAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 25, 1, 2, 2, 1)
)
cienaCesExtAclEntry.setIndexNames(
    (0, "CIENA-CES-ACL-MIB", "cienaCesExtAclEntrySrcInetAddrType"),
    (0, "CIENA-CES-ACL-MIB", "cienaCesExtAclEntrySrcInetAddr"),
    (0, "CIENA-CES-ACL-MIB", "cienaCesExtAclEntrySrcInetPrefixLen"),
    (0, "CIENA-CES-ACL-MIB", "cienaCesExtAclEntryDstInetAddrType"),
    (0, "CIENA-CES-ACL-MIB", "cienaCesExtAclEntryDstInetAddr"),
    (0, "CIENA-CES-ACL-MIB", "cienaCesExtAclEntryDstInetPrefixLen"),
)
if mibBuilder.loadTexts:
    cienaCesExtAclEntry.setStatus("current")
_CienaCesExtAclEntrySrcInetAddrType_Type = InetAddressType
_CienaCesExtAclEntrySrcInetAddrType_Object = MibTableColumn
cienaCesExtAclEntrySrcInetAddrType = _CienaCesExtAclEntrySrcInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 25, 1, 2, 2, 1, 1),
    _CienaCesExtAclEntrySrcInetAddrType_Type()
)
cienaCesExtAclEntrySrcInetAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesExtAclEntrySrcInetAddrType.setStatus("current")


class _CienaCesExtAclEntrySrcInetAddr_Type(InetAddress):
    """Custom type cienaCesExtAclEntrySrcInetAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_CienaCesExtAclEntrySrcInetAddr_Type.__name__ = "InetAddress"
_CienaCesExtAclEntrySrcInetAddr_Object = MibTableColumn
cienaCesExtAclEntrySrcInetAddr = _CienaCesExtAclEntrySrcInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 25, 1, 2, 2, 1, 2),
    _CienaCesExtAclEntrySrcInetAddr_Type()
)
cienaCesExtAclEntrySrcInetAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesExtAclEntrySrcInetAddr.setStatus("current")
_CienaCesExtAclEntrySrcInetPrefixLen_Type = InetAddressPrefixLength
_CienaCesExtAclEntrySrcInetPrefixLen_Object = MibTableColumn
cienaCesExtAclEntrySrcInetPrefixLen = _CienaCesExtAclEntrySrcInetPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 25, 1, 2, 2, 1, 3),
    _CienaCesExtAclEntrySrcInetPrefixLen_Type()
)
cienaCesExtAclEntrySrcInetPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesExtAclEntrySrcInetPrefixLen.setStatus("current")
_CienaCesExtAclEntryDstInetAddrType_Type = InetAddressType
_CienaCesExtAclEntryDstInetAddrType_Object = MibTableColumn
cienaCesExtAclEntryDstInetAddrType = _CienaCesExtAclEntryDstInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 25, 1, 2, 2, 1, 4),
    _CienaCesExtAclEntryDstInetAddrType_Type()
)
cienaCesExtAclEntryDstInetAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesExtAclEntryDstInetAddrType.setStatus("current")


class _CienaCesExtAclEntryDstInetAddr_Type(InetAddress):
    """Custom type cienaCesExtAclEntryDstInetAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_CienaCesExtAclEntryDstInetAddr_Type.__name__ = "InetAddress"
_CienaCesExtAclEntryDstInetAddr_Object = MibTableColumn
cienaCesExtAclEntryDstInetAddr = _CienaCesExtAclEntryDstInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 25, 1, 2, 2, 1, 5),
    _CienaCesExtAclEntryDstInetAddr_Type()
)
cienaCesExtAclEntryDstInetAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesExtAclEntryDstInetAddr.setStatus("current")
_CienaCesExtAclEntryDstInetPrefixLen_Type = InetAddressPrefixLength
_CienaCesExtAclEntryDstInetPrefixLen_Object = MibTableColumn
cienaCesExtAclEntryDstInetPrefixLen = _CienaCesExtAclEntryDstInetPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 25, 1, 2, 2, 1, 6),
    _CienaCesExtAclEntryDstInetPrefixLen_Type()
)
cienaCesExtAclEntryDstInetPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesExtAclEntryDstInetPrefixLen.setStatus("current")
_CienaCesExtAclEntryNotifSrcInetAddrType_Type = InetAddressType
_CienaCesExtAclEntryNotifSrcInetAddrType_Object = MibTableColumn
cienaCesExtAclEntryNotifSrcInetAddrType = _CienaCesExtAclEntryNotifSrcInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 25, 1, 2, 2, 1, 7),
    _CienaCesExtAclEntryNotifSrcInetAddrType_Type()
)
cienaCesExtAclEntryNotifSrcInetAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesExtAclEntryNotifSrcInetAddrType.setStatus("current")
_CienaCesExtAclEntryNotifSrcInetAddr_Type = InetAddress
_CienaCesExtAclEntryNotifSrcInetAddr_Object = MibTableColumn
cienaCesExtAclEntryNotifSrcInetAddr = _CienaCesExtAclEntryNotifSrcInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 25, 1, 2, 2, 1, 8),
    _CienaCesExtAclEntryNotifSrcInetAddr_Type()
)
cienaCesExtAclEntryNotifSrcInetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesExtAclEntryNotifSrcInetAddr.setStatus("current")
_CienaCesExtAclEntryNotifSrcInetPrefixLen_Type = InetAddressPrefixLength
_CienaCesExtAclEntryNotifSrcInetPrefixLen_Object = MibTableColumn
cienaCesExtAclEntryNotifSrcInetPrefixLen = _CienaCesExtAclEntryNotifSrcInetPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 25, 1, 2, 2, 1, 9),
    _CienaCesExtAclEntryNotifSrcInetPrefixLen_Type()
)
cienaCesExtAclEntryNotifSrcInetPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesExtAclEntryNotifSrcInetPrefixLen.setStatus("current")
_CienaCesExtAclEntryNotifDstInetAddrType_Type = InetAddressType
_CienaCesExtAclEntryNotifDstInetAddrType_Object = MibTableColumn
cienaCesExtAclEntryNotifDstInetAddrType = _CienaCesExtAclEntryNotifDstInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 25, 1, 2, 2, 1, 10),
    _CienaCesExtAclEntryNotifDstInetAddrType_Type()
)
cienaCesExtAclEntryNotifDstInetAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesExtAclEntryNotifDstInetAddrType.setStatus("current")
_CienaCesExtAclEntryNotifDstInetAddr_Type = InetAddress
_CienaCesExtAclEntryNotifDstInetAddr_Object = MibTableColumn
cienaCesExtAclEntryNotifDstInetAddr = _CienaCesExtAclEntryNotifDstInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 25, 1, 2, 2, 1, 11),
    _CienaCesExtAclEntryNotifDstInetAddr_Type()
)
cienaCesExtAclEntryNotifDstInetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesExtAclEntryNotifDstInetAddr.setStatus("current")
_CienaCesExtAclEntryNotifDstInetPrefixLen_Type = InetAddressPrefixLength
_CienaCesExtAclEntryNotifDstInetPrefixLen_Object = MibTableColumn
cienaCesExtAclEntryNotifDstInetPrefixLen = _CienaCesExtAclEntryNotifDstInetPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 25, 1, 2, 2, 1, 12),
    _CienaCesExtAclEntryNotifDstInetPrefixLen_Type()
)
cienaCesExtAclEntryNotifDstInetPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesExtAclEntryNotifDstInetPrefixLen.setStatus("current")
_CienaCesExtAclEntryHits_Type = Counter32
_CienaCesExtAclEntryHits_Object = MibTableColumn
cienaCesExtAclEntryHits = _CienaCesExtAclEntryHits_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 25, 1, 2, 2, 1, 13),
    _CienaCesExtAclEntryHits_Type()
)
cienaCesExtAclEntryHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesExtAclEntryHits.setStatus("current")
_CienaCesExtAclEntryBadPort_Type = Counter32
_CienaCesExtAclEntryBadPort_Object = MibTableColumn
cienaCesExtAclEntryBadPort = _CienaCesExtAclEntryBadPort_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 25, 1, 2, 2, 1, 14),
    _CienaCesExtAclEntryBadPort_Type()
)
cienaCesExtAclEntryBadPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesExtAclEntryBadPort.setStatus("current")


class _CienaCesExtAclEntryDscpMask_Type(OctetString):
    """Custom type cienaCesExtAclEntryDscpMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_CienaCesExtAclEntryDscpMask_Type.__name__ = "OctetString"
_CienaCesExtAclEntryDscpMask_Object = MibTableColumn
cienaCesExtAclEntryDscpMask = _CienaCesExtAclEntryDscpMask_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 25, 1, 2, 2, 1, 15),
    _CienaCesExtAclEntryDscpMask_Type()
)
cienaCesExtAclEntryDscpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesExtAclEntryDscpMask.setStatus("current")
_CienaCesExtAclEntryBadDscp_Type = Counter32
_CienaCesExtAclEntryBadDscp_Object = MibTableColumn
cienaCesExtAclEntryBadDscp = _CienaCesExtAclEntryBadDscp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 25, 1, 2, 2, 1, 16),
    _CienaCesExtAclEntryBadDscp_Type()
)
cienaCesExtAclEntryBadDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesExtAclEntryBadDscp.setStatus("current")


class _CienaCesExtAclEntryPortBitMask_Type(OctetString):
    """Custom type cienaCesExtAclEntryPortBitMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_CienaCesExtAclEntryPortBitMask_Type.__name__ = "OctetString"
_CienaCesExtAclEntryPortBitMask_Object = MibTableColumn
cienaCesExtAclEntryPortBitMask = _CienaCesExtAclEntryPortBitMask_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 25, 1, 2, 2, 1, 17),
    _CienaCesExtAclEntryPortBitMask_Type()
)
cienaCesExtAclEntryPortBitMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesExtAclEntryPortBitMask.setStatus("current")


class _CienaCesExtAclEntryProtocol_Type(Bits):
    """Custom type cienaCesExtAclEntryProtocol based on Bits"""
    namedValues = NamedValues(
        *(("all", 15),
          ("icmp", 0),
          ("tcp", 1),
          ("udp", 2))
    )

_CienaCesExtAclEntryProtocol_Type.__name__ = "Bits"
_CienaCesExtAclEntryProtocol_Object = MibTableColumn
cienaCesExtAclEntryProtocol = _CienaCesExtAclEntryProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 25, 1, 2, 2, 1, 18),
    _CienaCesExtAclEntryProtocol_Type()
)
cienaCesExtAclEntryProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesExtAclEntryProtocol.setStatus("current")
_CienaCesExtAclEntryBadProtocol_Type = Counter32
_CienaCesExtAclEntryBadProtocol_Object = MibTableColumn
cienaCesExtAclEntryBadProtocol = _CienaCesExtAclEntryBadProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 25, 1, 2, 2, 1, 19),
    _CienaCesExtAclEntryBadProtocol_Type()
)
cienaCesExtAclEntryBadProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesExtAclEntryBadProtocol.setStatus("current")
_CienaCesAclMIBConformance_ObjectIdentity = ObjectIdentity
cienaCesAclMIBConformance = _CienaCesAclMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 25, 3)
)
_CienaCesAclMIBCompliances_ObjectIdentity = ObjectIdentity
cienaCesAclMIBCompliances = _CienaCesAclMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 25, 3, 1)
)
_CienaCesAclMIBGroups_ObjectIdentity = ObjectIdentity
cienaCesAclMIBGroups = _CienaCesAclMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 25, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-CES-ACL-MIB",
    **{"cienaCesAclMIB": cienaCesAclMIB,
       "cienaCesAclMIBObjects": cienaCesAclMIBObjects,
       "cienaCesAclGlobal": cienaCesAclGlobal,
       "cienaCesAclAdminState": cienaCesAclAdminState,
       "cienaCesAclCacheHit": cienaCesAclCacheHit,
       "cienaCesAclNoHit": cienaCesAclNoHit,
       "cienaCesAclBadPort": cienaCesAclBadPort,
       "cienaCesAclBadDscp": cienaCesAclBadDscp,
       "cienaCesAclOperState": cienaCesAclOperState,
       "cienaCesAclInUseEntries": cienaCesAclInUseEntries,
       "cienaCesAclMaxEntries": cienaCesAclMaxEntries,
       "cienaCesAclBadProtocol": cienaCesAclBadProtocol,
       "cienaCesAclRules": cienaCesAclRules,
       "cienaCesAclTable": cienaCesAclTable,
       "cienaCesAclEntry": cienaCesAclEntry,
       "cienaCesAclEntryInetAddrType": cienaCesAclEntryInetAddrType,
       "cienaCesAclEntryInetAddr": cienaCesAclEntryInetAddr,
       "cienaCesAclEntryInetPrefixLength": cienaCesAclEntryInetPrefixLength,
       "cienaCesAclEntryHits": cienaCesAclEntryHits,
       "cienaCesAclEntryBadPort": cienaCesAclEntryBadPort,
       "cienaCesAclEntryDscpMask": cienaCesAclEntryDscpMask,
       "cienaCesAclEntryBadDscp": cienaCesAclEntryBadDscp,
       "cienaCesAclEntryPortBitMask": cienaCesAclEntryPortBitMask,
       "cienaCesAclEntryNotifInetAddrType": cienaCesAclEntryNotifInetAddrType,
       "cienaCesAclEntryNotifInetAddr": cienaCesAclEntryNotifInetAddr,
       "cienaCesAclEntryNotifInetPrefixLength": cienaCesAclEntryNotifInetPrefixLength,
       "cienaCesExtAclTable": cienaCesExtAclTable,
       "cienaCesExtAclEntry": cienaCesExtAclEntry,
       "cienaCesExtAclEntrySrcInetAddrType": cienaCesExtAclEntrySrcInetAddrType,
       "cienaCesExtAclEntrySrcInetAddr": cienaCesExtAclEntrySrcInetAddr,
       "cienaCesExtAclEntrySrcInetPrefixLen": cienaCesExtAclEntrySrcInetPrefixLen,
       "cienaCesExtAclEntryDstInetAddrType": cienaCesExtAclEntryDstInetAddrType,
       "cienaCesExtAclEntryDstInetAddr": cienaCesExtAclEntryDstInetAddr,
       "cienaCesExtAclEntryDstInetPrefixLen": cienaCesExtAclEntryDstInetPrefixLen,
       "cienaCesExtAclEntryNotifSrcInetAddrType": cienaCesExtAclEntryNotifSrcInetAddrType,
       "cienaCesExtAclEntryNotifSrcInetAddr": cienaCesExtAclEntryNotifSrcInetAddr,
       "cienaCesExtAclEntryNotifSrcInetPrefixLen": cienaCesExtAclEntryNotifSrcInetPrefixLen,
       "cienaCesExtAclEntryNotifDstInetAddrType": cienaCesExtAclEntryNotifDstInetAddrType,
       "cienaCesExtAclEntryNotifDstInetAddr": cienaCesExtAclEntryNotifDstInetAddr,
       "cienaCesExtAclEntryNotifDstInetPrefixLen": cienaCesExtAclEntryNotifDstInetPrefixLen,
       "cienaCesExtAclEntryHits": cienaCesExtAclEntryHits,
       "cienaCesExtAclEntryBadPort": cienaCesExtAclEntryBadPort,
       "cienaCesExtAclEntryDscpMask": cienaCesExtAclEntryDscpMask,
       "cienaCesExtAclEntryBadDscp": cienaCesExtAclEntryBadDscp,
       "cienaCesExtAclEntryPortBitMask": cienaCesExtAclEntryPortBitMask,
       "cienaCesExtAclEntryProtocol": cienaCesExtAclEntryProtocol,
       "cienaCesExtAclEntryBadProtocol": cienaCesExtAclEntryBadProtocol,
       "cienaCesAclMIBConformance": cienaCesAclMIBConformance,
       "cienaCesAclMIBCompliances": cienaCesAclMIBCompliances,
       "cienaCesAclMIBGroups": cienaCesAclMIBGroups}
)
