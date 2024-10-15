# SNMP MIB module (MOBILEIPV6-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MOBILEIPV6-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:22:36 2024
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

(ipv6InterfaceIfIndex,) = mibBuilder.importSymbols(
    "IP-MIB",
    "ipv6InterfaceIfIndex")

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

mip6MIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 133)
)
mip6MIB.setRevisions(
        ("2006-02-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Mip6BURequestRejectionCode(Integer32, TextualConvention):
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("admProhibited", 2),
          ("duplicateAddressDetectionFailed", 7),
          ("expiredCareofNonceIndex", 10),
          ("expiredHomeNonceIndex", 9),
          ("expiredNonces", 11),
          ("homeRegistrationNotSupported", 4),
          ("insufficientResource", 3),
          ("notHomeAgentForThisMobileNode", 6),
          ("notHomeSubnet", 5),
          ("reasonUnspecified", 1),
          ("registrationTypeChangeDisallowed", 12),
          ("sequenceNumberOutOfWindow", 8))
    )



# MIB Managed Objects in the order of their OIDs

_Mip6Notifications_ObjectIdentity = ObjectIdentity
mip6Notifications = _Mip6Notifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 133, 0)
)
_Mip6Objects_ObjectIdentity = ObjectIdentity
mip6Objects = _Mip6Objects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 133, 1)
)
_Mip6Core_ObjectIdentity = ObjectIdentity
mip6Core = _Mip6Core_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 133, 1, 1)
)
_Mip6System_ObjectIdentity = ObjectIdentity
mip6System = _Mip6System_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 133, 1, 1, 1)
)


class _Mip6Capabilities_Type(Bits):
    """Custom type mip6Capabilities based on Bits"""
    namedValues = NamedValues(
        *(("correspondentNode", 2),
          ("homeAgent", 1),
          ("mobileNode", 0))
    )

_Mip6Capabilities_Type.__name__ = "Bits"
_Mip6Capabilities_Object = MibScalar
mip6Capabilities = _Mip6Capabilities_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 1, 1, 1),
    _Mip6Capabilities_Type()
)
mip6Capabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6Capabilities.setStatus("current")


class _Mip6Status_Type(Integer32):
    """Custom type mip6Status based on Integer32"""
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


_Mip6Status_Type.__name__ = "Integer32"
_Mip6Status_Object = MibScalar
mip6Status = _Mip6Status_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 1, 1, 2),
    _Mip6Status_Type()
)
mip6Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mip6Status.setStatus("current")
_Mip6Bindings_ObjectIdentity = ObjectIdentity
mip6Bindings = _Mip6Bindings_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 133, 1, 1, 2)
)
_Mip6BindingCacheTable_Object = MibTable
mip6BindingCacheTable = _Mip6BindingCacheTable_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    mip6BindingCacheTable.setStatus("current")
_Mip6BindingCacheEntry_Object = MibTableRow
mip6BindingCacheEntry = _Mip6BindingCacheEntry_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 1, 2, 1, 1)
)
mip6BindingCacheEntry.setIndexNames(
    (0, "MOBILEIPV6-MIB", "mip6BindingHomeAddressType"),
    (0, "MOBILEIPV6-MIB", "mip6BindingHomeAddress"),
)
if mibBuilder.loadTexts:
    mip6BindingCacheEntry.setStatus("current")
_Mip6BindingHomeAddressType_Type = InetAddressType
_Mip6BindingHomeAddressType_Object = MibTableColumn
mip6BindingHomeAddressType = _Mip6BindingHomeAddressType_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 1, 2, 1, 1, 1),
    _Mip6BindingHomeAddressType_Type()
)
mip6BindingHomeAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mip6BindingHomeAddressType.setStatus("current")
_Mip6BindingHomeAddress_Type = InetAddress
_Mip6BindingHomeAddress_Object = MibTableColumn
mip6BindingHomeAddress = _Mip6BindingHomeAddress_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 1, 2, 1, 1, 2),
    _Mip6BindingHomeAddress_Type()
)
mip6BindingHomeAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mip6BindingHomeAddress.setStatus("current")
_Mip6BindingCOAType_Type = InetAddressType
_Mip6BindingCOAType_Object = MibTableColumn
mip6BindingCOAType = _Mip6BindingCOAType_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 1, 2, 1, 1, 3),
    _Mip6BindingCOAType_Type()
)
mip6BindingCOAType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6BindingCOAType.setStatus("current")
_Mip6BindingCOA_Type = InetAddress
_Mip6BindingCOA_Object = MibTableColumn
mip6BindingCOA = _Mip6BindingCOA_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 1, 2, 1, 1, 4),
    _Mip6BindingCOA_Type()
)
mip6BindingCOA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6BindingCOA.setStatus("current")
_Mip6BindingTimeRegistered_Type = DateAndTime
_Mip6BindingTimeRegistered_Object = MibTableColumn
mip6BindingTimeRegistered = _Mip6BindingTimeRegistered_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 1, 2, 1, 1, 5),
    _Mip6BindingTimeRegistered_Type()
)
mip6BindingTimeRegistered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6BindingTimeRegistered.setStatus("current")
_Mip6BindingTimeGranted_Type = Gauge32
_Mip6BindingTimeGranted_Object = MibTableColumn
mip6BindingTimeGranted = _Mip6BindingTimeGranted_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 1, 2, 1, 1, 6),
    _Mip6BindingTimeGranted_Type()
)
mip6BindingTimeGranted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6BindingTimeGranted.setStatus("current")
if mibBuilder.loadTexts:
    mip6BindingTimeGranted.setUnits("seconds")
_Mip6BindingTimeRemaining_Type = Gauge32
_Mip6BindingTimeRemaining_Object = MibTableColumn
mip6BindingTimeRemaining = _Mip6BindingTimeRemaining_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 1, 2, 1, 1, 7),
    _Mip6BindingTimeRemaining_Type()
)
mip6BindingTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6BindingTimeRemaining.setStatus("current")
if mibBuilder.loadTexts:
    mip6BindingTimeRemaining.setUnits("seconds")
_Mip6BindingHomeRegn_Type = TruthValue
_Mip6BindingHomeRegn_Object = MibTableColumn
mip6BindingHomeRegn = _Mip6BindingHomeRegn_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 1, 2, 1, 1, 8),
    _Mip6BindingHomeRegn_Type()
)
mip6BindingHomeRegn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6BindingHomeRegn.setStatus("current")


class _Mip6BindingMaxSeq_Type(Unsigned32):
    """Custom type mip6BindingMaxSeq based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Mip6BindingMaxSeq_Type.__name__ = "Unsigned32"
_Mip6BindingMaxSeq_Object = MibTableColumn
mip6BindingMaxSeq = _Mip6BindingMaxSeq_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 1, 2, 1, 1, 9),
    _Mip6BindingMaxSeq_Type()
)
mip6BindingMaxSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6BindingMaxSeq.setStatus("current")
_Mip6BindingUsageTS_Type = DateAndTime
_Mip6BindingUsageTS_Object = MibTableColumn
mip6BindingUsageTS = _Mip6BindingUsageTS_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 1, 2, 1, 1, 10),
    _Mip6BindingUsageTS_Type()
)
mip6BindingUsageTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6BindingUsageTS.setStatus("current")
_Mip6BindingUsageCount_Type = Gauge32
_Mip6BindingUsageCount_Object = MibTableColumn
mip6BindingUsageCount = _Mip6BindingUsageCount_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 1, 2, 1, 1, 11),
    _Mip6BindingUsageCount_Type()
)
mip6BindingUsageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6BindingUsageCount.setStatus("current")


class _Mip6BindingAdminStatus_Type(Integer32):
    """Custom type mip6BindingAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_Mip6BindingAdminStatus_Type.__name__ = "Integer32"
_Mip6BindingAdminStatus_Object = MibTableColumn
mip6BindingAdminStatus = _Mip6BindingAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 1, 2, 1, 1, 12),
    _Mip6BindingAdminStatus_Type()
)
mip6BindingAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mip6BindingAdminStatus.setStatus("current")
_Mip6BindingHistoryTable_Object = MibTable
mip6BindingHistoryTable = _Mip6BindingHistoryTable_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    mip6BindingHistoryTable.setStatus("current")
_Mip6BindingHistoryEntry_Object = MibTableRow
mip6BindingHistoryEntry = _Mip6BindingHistoryEntry_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 1, 2, 2, 1)
)
mip6BindingHistoryEntry.setIndexNames(
    (0, "MOBILEIPV6-MIB", "mip6BindingHstHomeAddressType"),
    (0, "MOBILEIPV6-MIB", "mip6BindingHstHomeAddress"),
    (0, "MOBILEIPV6-MIB", "mip6BindingHstIndex"),
)
if mibBuilder.loadTexts:
    mip6BindingHistoryEntry.setStatus("current")
_Mip6BindingHstHomeAddressType_Type = InetAddressType
_Mip6BindingHstHomeAddressType_Object = MibTableColumn
mip6BindingHstHomeAddressType = _Mip6BindingHstHomeAddressType_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 1, 2, 2, 1, 1),
    _Mip6BindingHstHomeAddressType_Type()
)
mip6BindingHstHomeAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mip6BindingHstHomeAddressType.setStatus("current")
_Mip6BindingHstHomeAddress_Type = InetAddress
_Mip6BindingHstHomeAddress_Object = MibTableColumn
mip6BindingHstHomeAddress = _Mip6BindingHstHomeAddress_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 1, 2, 2, 1, 2),
    _Mip6BindingHstHomeAddress_Type()
)
mip6BindingHstHomeAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mip6BindingHstHomeAddress.setStatus("current")


class _Mip6BindingHstIndex_Type(Unsigned32):
    """Custom type mip6BindingHstIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Mip6BindingHstIndex_Type.__name__ = "Unsigned32"
_Mip6BindingHstIndex_Object = MibTableColumn
mip6BindingHstIndex = _Mip6BindingHstIndex_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 1, 2, 2, 1, 3),
    _Mip6BindingHstIndex_Type()
)
mip6BindingHstIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mip6BindingHstIndex.setStatus("current")
_Mip6BindingHstCOAType_Type = InetAddressType
_Mip6BindingHstCOAType_Object = MibTableColumn
mip6BindingHstCOAType = _Mip6BindingHstCOAType_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 1, 2, 2, 1, 4),
    _Mip6BindingHstCOAType_Type()
)
mip6BindingHstCOAType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6BindingHstCOAType.setStatus("current")
_Mip6BindingHstCOA_Type = InetAddress
_Mip6BindingHstCOA_Object = MibTableColumn
mip6BindingHstCOA = _Mip6BindingHstCOA_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 1, 2, 2, 1, 5),
    _Mip6BindingHstCOA_Type()
)
mip6BindingHstCOA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6BindingHstCOA.setStatus("current")
_Mip6BindingHstTimeRegistered_Type = DateAndTime
_Mip6BindingHstTimeRegistered_Object = MibTableColumn
mip6BindingHstTimeRegistered = _Mip6BindingHstTimeRegistered_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 1, 2, 2, 1, 6),
    _Mip6BindingHstTimeRegistered_Type()
)
mip6BindingHstTimeRegistered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6BindingHstTimeRegistered.setStatus("current")
_Mip6BindingHstTimeExpired_Type = DateAndTime
_Mip6BindingHstTimeExpired_Object = MibTableColumn
mip6BindingHstTimeExpired = _Mip6BindingHstTimeExpired_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 1, 2, 2, 1, 7),
    _Mip6BindingHstTimeExpired_Type()
)
mip6BindingHstTimeExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6BindingHstTimeExpired.setStatus("current")
_Mip6BindingHstHomeRegn_Type = TruthValue
_Mip6BindingHstHomeRegn_Object = MibTableColumn
mip6BindingHstHomeRegn = _Mip6BindingHstHomeRegn_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 1, 2, 2, 1, 8),
    _Mip6BindingHstHomeRegn_Type()
)
mip6BindingHstHomeRegn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6BindingHstHomeRegn.setStatus("current")
_Mip6BindingHstUsageTS_Type = DateAndTime
_Mip6BindingHstUsageTS_Object = MibTableColumn
mip6BindingHstUsageTS = _Mip6BindingHstUsageTS_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 1, 2, 2, 1, 9),
    _Mip6BindingHstUsageTS_Type()
)
mip6BindingHstUsageTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6BindingHstUsageTS.setStatus("current")
_Mip6BindingHstUsageCount_Type = Gauge32
_Mip6BindingHstUsageCount_Object = MibTableColumn
mip6BindingHstUsageCount = _Mip6BindingHstUsageCount_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 1, 2, 2, 1, 10),
    _Mip6BindingHstUsageCount_Type()
)
mip6BindingHstUsageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6BindingHstUsageCount.setStatus("current")
_Mip6Stats_ObjectIdentity = ObjectIdentity
mip6Stats = _Mip6Stats_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 133, 1, 1, 3)
)
_Mip6TotalTraffic_ObjectIdentity = ObjectIdentity
mip6TotalTraffic = _Mip6TotalTraffic_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 133, 1, 1, 3, 1)
)
_Mip6InOctets_Type = Counter32
_Mip6InOctets_Object = MibScalar
mip6InOctets = _Mip6InOctets_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 1, 3, 1, 1),
    _Mip6InOctets_Type()
)
mip6InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6InOctets.setStatus("current")
_Mip6HCInOctets_Type = Counter64
_Mip6HCInOctets_Object = MibScalar
mip6HCInOctets = _Mip6HCInOctets_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 1, 3, 1, 2),
    _Mip6HCInOctets_Type()
)
mip6HCInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6HCInOctets.setStatus("current")
_Mip6InPkts_Type = Counter32
_Mip6InPkts_Object = MibScalar
mip6InPkts = _Mip6InPkts_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 1, 3, 1, 3),
    _Mip6InPkts_Type()
)
mip6InPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6InPkts.setStatus("current")
_Mip6HCInPkts_Type = Counter64
_Mip6HCInPkts_Object = MibScalar
mip6HCInPkts = _Mip6HCInPkts_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 1, 3, 1, 4),
    _Mip6HCInPkts_Type()
)
mip6HCInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6HCInPkts.setStatus("current")
_Mip6OutOctets_Type = Counter32
_Mip6OutOctets_Object = MibScalar
mip6OutOctets = _Mip6OutOctets_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 1, 3, 1, 5),
    _Mip6OutOctets_Type()
)
mip6OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6OutOctets.setStatus("current")
_Mip6HCOutOctets_Type = Counter64
_Mip6HCOutOctets_Object = MibScalar
mip6HCOutOctets = _Mip6HCOutOctets_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 1, 3, 1, 6),
    _Mip6HCOutOctets_Type()
)
mip6HCOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6HCOutOctets.setStatus("current")
_Mip6OutPkts_Type = Counter32
_Mip6OutPkts_Object = MibScalar
mip6OutPkts = _Mip6OutPkts_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 1, 3, 1, 7),
    _Mip6OutPkts_Type()
)
mip6OutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6OutPkts.setStatus("current")
_Mip6HCOutPkts_Type = Counter64
_Mip6HCOutPkts_Object = MibScalar
mip6HCOutPkts = _Mip6HCOutPkts_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 1, 3, 1, 8),
    _Mip6HCOutPkts_Type()
)
mip6HCOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6HCOutPkts.setStatus("current")
_Mip6CounterDiscontinuityTime_Type = TimeStamp
_Mip6CounterDiscontinuityTime_Object = MibScalar
mip6CounterDiscontinuityTime = _Mip6CounterDiscontinuityTime_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 1, 3, 1, 9),
    _Mip6CounterDiscontinuityTime_Type()
)
mip6CounterDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6CounterDiscontinuityTime.setStatus("current")
_Mip6NodeTrafficTable_Object = MibTable
mip6NodeTrafficTable = _Mip6NodeTrafficTable_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    mip6NodeTrafficTable.setStatus("current")
_Mip6NodeTrafficEntry_Object = MibTableRow
mip6NodeTrafficEntry = _Mip6NodeTrafficEntry_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 1, 3, 2, 1)
)
mip6NodeTrafficEntry.setIndexNames(
    (0, "MOBILEIPV6-MIB", "mip6BindingHomeAddressType"),
    (0, "MOBILEIPV6-MIB", "mip6BindingHomeAddress"),
)
if mibBuilder.loadTexts:
    mip6NodeTrafficEntry.setStatus("current")
_Mip6NodeInOctets_Type = Counter32
_Mip6NodeInOctets_Object = MibTableColumn
mip6NodeInOctets = _Mip6NodeInOctets_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 1, 3, 2, 1, 1),
    _Mip6NodeInOctets_Type()
)
mip6NodeInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6NodeInOctets.setStatus("current")
_Mip6HCNodeInOctets_Type = Counter64
_Mip6HCNodeInOctets_Object = MibTableColumn
mip6HCNodeInOctets = _Mip6HCNodeInOctets_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 1, 3, 2, 1, 2),
    _Mip6HCNodeInOctets_Type()
)
mip6HCNodeInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6HCNodeInOctets.setStatus("current")
_Mip6NodeInPkts_Type = Counter32
_Mip6NodeInPkts_Object = MibTableColumn
mip6NodeInPkts = _Mip6NodeInPkts_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 1, 3, 2, 1, 3),
    _Mip6NodeInPkts_Type()
)
mip6NodeInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6NodeInPkts.setStatus("current")
_Mip6HCNodeInPkts_Type = Counter64
_Mip6HCNodeInPkts_Object = MibTableColumn
mip6HCNodeInPkts = _Mip6HCNodeInPkts_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 1, 3, 2, 1, 4),
    _Mip6HCNodeInPkts_Type()
)
mip6HCNodeInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6HCNodeInPkts.setStatus("current")
_Mip6NodeOutOctets_Type = Counter32
_Mip6NodeOutOctets_Object = MibTableColumn
mip6NodeOutOctets = _Mip6NodeOutOctets_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 1, 3, 2, 1, 5),
    _Mip6NodeOutOctets_Type()
)
mip6NodeOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6NodeOutOctets.setStatus("current")
_Mip6HCNodeOutOctets_Type = Counter64
_Mip6HCNodeOutOctets_Object = MibTableColumn
mip6HCNodeOutOctets = _Mip6HCNodeOutOctets_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 1, 3, 2, 1, 6),
    _Mip6HCNodeOutOctets_Type()
)
mip6HCNodeOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6HCNodeOutOctets.setStatus("current")
_Mip6NodeOutPkts_Type = Counter32
_Mip6NodeOutPkts_Object = MibTableColumn
mip6NodeOutPkts = _Mip6NodeOutPkts_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 1, 3, 2, 1, 7),
    _Mip6NodeOutPkts_Type()
)
mip6NodeOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6NodeOutPkts.setStatus("current")
_Mip6HCNodeOutPkts_Type = Counter64
_Mip6HCNodeOutPkts_Object = MibTableColumn
mip6HCNodeOutPkts = _Mip6HCNodeOutPkts_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 1, 3, 2, 1, 8),
    _Mip6HCNodeOutPkts_Type()
)
mip6HCNodeOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6HCNodeOutPkts.setStatus("current")
_Mip6NodeCtrDiscontinuityTime_Type = TimeStamp
_Mip6NodeCtrDiscontinuityTime_Object = MibTableColumn
mip6NodeCtrDiscontinuityTime = _Mip6NodeCtrDiscontinuityTime_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 1, 3, 2, 1, 9),
    _Mip6NodeCtrDiscontinuityTime_Type()
)
mip6NodeCtrDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6NodeCtrDiscontinuityTime.setStatus("current")
_Mip6Mn_ObjectIdentity = ObjectIdentity
mip6Mn = _Mip6Mn_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 133, 1, 2)
)
_Mip6MnSystem_ObjectIdentity = ObjectIdentity
mip6MnSystem = _Mip6MnSystem_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 133, 1, 2, 1)
)
_Mip6MnHomeAddressTable_Object = MibTable
mip6MnHomeAddressTable = _Mip6MnHomeAddressTable_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    mip6MnHomeAddressTable.setStatus("current")
_Mip6MnHomeAddressEntry_Object = MibTableRow
mip6MnHomeAddressEntry = _Mip6MnHomeAddressEntry_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 2, 1, 1, 1)
)
mip6MnHomeAddressEntry.setIndexNames(
    (0, "MOBILEIPV6-MIB", "mip6MnHomeAddressType"),
    (0, "MOBILEIPV6-MIB", "mip6MnHomeAddress"),
)
if mibBuilder.loadTexts:
    mip6MnHomeAddressEntry.setStatus("current")
_Mip6MnHomeAddressType_Type = InetAddressType
_Mip6MnHomeAddressType_Object = MibTableColumn
mip6MnHomeAddressType = _Mip6MnHomeAddressType_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 2, 1, 1, 1, 1),
    _Mip6MnHomeAddressType_Type()
)
mip6MnHomeAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mip6MnHomeAddressType.setStatus("current")
_Mip6MnHomeAddress_Type = InetAddress
_Mip6MnHomeAddress_Object = MibTableColumn
mip6MnHomeAddress = _Mip6MnHomeAddress_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 2, 1, 1, 1, 2),
    _Mip6MnHomeAddress_Type()
)
mip6MnHomeAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mip6MnHomeAddress.setStatus("current")


class _Mip6MnHomeAddressState_Type(Integer32):
    """Custom type mip6MnHomeAddressState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("home", 2),
          ("isolated", 5),
          ("pending", 4),
          ("registered", 3),
          ("unknown", 1))
    )


_Mip6MnHomeAddressState_Type.__name__ = "Integer32"
_Mip6MnHomeAddressState_Object = MibTableColumn
mip6MnHomeAddressState = _Mip6MnHomeAddressState_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 2, 1, 1, 1, 3),
    _Mip6MnHomeAddressState_Type()
)
mip6MnHomeAddressState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6MnHomeAddressState.setStatus("current")
_Mip6MnConf_ObjectIdentity = ObjectIdentity
mip6MnConf = _Mip6MnConf_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 133, 1, 2, 2)
)
_Mip6MnDiscoveryRequests_Type = Counter32
_Mip6MnDiscoveryRequests_Object = MibScalar
mip6MnDiscoveryRequests = _Mip6MnDiscoveryRequests_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 2, 2, 1),
    _Mip6MnDiscoveryRequests_Type()
)
mip6MnDiscoveryRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6MnDiscoveryRequests.setStatus("current")
_Mip6MnDiscoveryReplies_Type = Counter32
_Mip6MnDiscoveryReplies_Object = MibScalar
mip6MnDiscoveryReplies = _Mip6MnDiscoveryReplies_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 2, 2, 2),
    _Mip6MnDiscoveryReplies_Type()
)
mip6MnDiscoveryReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6MnDiscoveryReplies.setStatus("current")
_Mip6MnDiscoveryTimeouts_Type = Counter32
_Mip6MnDiscoveryTimeouts_Object = MibScalar
mip6MnDiscoveryTimeouts = _Mip6MnDiscoveryTimeouts_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 2, 2, 3),
    _Mip6MnDiscoveryTimeouts_Type()
)
mip6MnDiscoveryTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6MnDiscoveryTimeouts.setStatus("current")
_Mip6MnPrefixSolicitationsSent_Type = Counter32
_Mip6MnPrefixSolicitationsSent_Object = MibScalar
mip6MnPrefixSolicitationsSent = _Mip6MnPrefixSolicitationsSent_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 2, 2, 4),
    _Mip6MnPrefixSolicitationsSent_Type()
)
mip6MnPrefixSolicitationsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6MnPrefixSolicitationsSent.setStatus("current")
_Mip6MnPrefixAdvsRecd_Type = Counter32
_Mip6MnPrefixAdvsRecd_Object = MibScalar
mip6MnPrefixAdvsRecd = _Mip6MnPrefixAdvsRecd_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 2, 2, 5),
    _Mip6MnPrefixAdvsRecd_Type()
)
mip6MnPrefixAdvsRecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6MnPrefixAdvsRecd.setStatus("current")
_Mip6MnPrefixAdvsIgnored_Type = Counter32
_Mip6MnPrefixAdvsIgnored_Object = MibScalar
mip6MnPrefixAdvsIgnored = _Mip6MnPrefixAdvsIgnored_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 2, 2, 6),
    _Mip6MnPrefixAdvsIgnored_Type()
)
mip6MnPrefixAdvsIgnored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6MnPrefixAdvsIgnored.setStatus("current")
_Mip6MnMovedToFN_Type = Counter32
_Mip6MnMovedToFN_Object = MibScalar
mip6MnMovedToFN = _Mip6MnMovedToFN_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 2, 2, 7),
    _Mip6MnMovedToFN_Type()
)
mip6MnMovedToFN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6MnMovedToFN.setStatus("current")
_Mip6MnMovedToHN_Type = Counter32
_Mip6MnMovedToHN_Object = MibScalar
mip6MnMovedToHN = _Mip6MnMovedToHN_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 2, 2, 8),
    _Mip6MnMovedToHN_Type()
)
mip6MnMovedToHN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6MnMovedToHN.setStatus("current")
_Mip6MnRegistration_ObjectIdentity = ObjectIdentity
mip6MnRegistration = _Mip6MnRegistration_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 133, 1, 2, 3)
)
_Mip6MnBLTable_Object = MibTable
mip6MnBLTable = _Mip6MnBLTable_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    mip6MnBLTable.setStatus("current")
_Mip6MnBLEntry_Object = MibTableRow
mip6MnBLEntry = _Mip6MnBLEntry_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 2, 3, 1, 1)
)
mip6MnBLEntry.setIndexNames(
    (0, "MOBILEIPV6-MIB", "mip6MnHomeAddressType"),
    (0, "MOBILEIPV6-MIB", "mip6MnHomeAddress"),
    (0, "MOBILEIPV6-MIB", "mip6MnBLNodeAddressType"),
    (0, "MOBILEIPV6-MIB", "mip6MnBLNodeAddress"),
)
if mibBuilder.loadTexts:
    mip6MnBLEntry.setStatus("current")
_Mip6MnBLNodeAddressType_Type = InetAddressType
_Mip6MnBLNodeAddressType_Object = MibTableColumn
mip6MnBLNodeAddressType = _Mip6MnBLNodeAddressType_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 2, 3, 1, 1, 1),
    _Mip6MnBLNodeAddressType_Type()
)
mip6MnBLNodeAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mip6MnBLNodeAddressType.setStatus("current")
_Mip6MnBLNodeAddress_Type = InetAddress
_Mip6MnBLNodeAddress_Object = MibTableColumn
mip6MnBLNodeAddress = _Mip6MnBLNodeAddress_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 2, 3, 1, 1, 2),
    _Mip6MnBLNodeAddress_Type()
)
mip6MnBLNodeAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mip6MnBLNodeAddress.setStatus("current")
_Mip6MnBLCOAType_Type = InetAddressType
_Mip6MnBLCOAType_Object = MibTableColumn
mip6MnBLCOAType = _Mip6MnBLCOAType_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 2, 3, 1, 1, 3),
    _Mip6MnBLCOAType_Type()
)
mip6MnBLCOAType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6MnBLCOAType.setStatus("current")
_Mip6MnBLCOA_Type = InetAddress
_Mip6MnBLCOA_Object = MibTableColumn
mip6MnBLCOA = _Mip6MnBLCOA_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 2, 3, 1, 1, 4),
    _Mip6MnBLCOA_Type()
)
mip6MnBLCOA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6MnBLCOA.setStatus("current")
_Mip6MnBLLifeTimeRequested_Type = Unsigned32
_Mip6MnBLLifeTimeRequested_Object = MibTableColumn
mip6MnBLLifeTimeRequested = _Mip6MnBLLifeTimeRequested_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 2, 3, 1, 1, 5),
    _Mip6MnBLLifeTimeRequested_Type()
)
mip6MnBLLifeTimeRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6MnBLLifeTimeRequested.setStatus("current")
if mibBuilder.loadTexts:
    mip6MnBLLifeTimeRequested.setUnits("seconds")
_Mip6MnBLLifeTimeGranted_Type = Unsigned32
_Mip6MnBLLifeTimeGranted_Object = MibTableColumn
mip6MnBLLifeTimeGranted = _Mip6MnBLLifeTimeGranted_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 2, 3, 1, 1, 6),
    _Mip6MnBLLifeTimeGranted_Type()
)
mip6MnBLLifeTimeGranted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6MnBLLifeTimeGranted.setStatus("current")
if mibBuilder.loadTexts:
    mip6MnBLLifeTimeGranted.setUnits("seconds")


class _Mip6MnBLMaxSeq_Type(Unsigned32):
    """Custom type mip6MnBLMaxSeq based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Mip6MnBLMaxSeq_Type.__name__ = "Unsigned32"
_Mip6MnBLMaxSeq_Object = MibTableColumn
mip6MnBLMaxSeq = _Mip6MnBLMaxSeq_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 2, 3, 1, 1, 7),
    _Mip6MnBLMaxSeq_Type()
)
mip6MnBLMaxSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6MnBLMaxSeq.setStatus("current")
_Mip6MnBLTimeSent_Type = DateAndTime
_Mip6MnBLTimeSent_Object = MibTableColumn
mip6MnBLTimeSent = _Mip6MnBLTimeSent_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 2, 3, 1, 1, 8),
    _Mip6MnBLTimeSent_Type()
)
mip6MnBLTimeSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6MnBLTimeSent.setStatus("current")
_Mip6MnBLAccepted_Type = TruthValue
_Mip6MnBLAccepted_Object = MibTableColumn
mip6MnBLAccepted = _Mip6MnBLAccepted_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 2, 3, 1, 1, 9),
    _Mip6MnBLAccepted_Type()
)
mip6MnBLAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6MnBLAccepted.setStatus("current")
_Mip6MnBLAcceptedTime_Type = DateAndTime
_Mip6MnBLAcceptedTime_Object = MibTableColumn
mip6MnBLAcceptedTime = _Mip6MnBLAcceptedTime_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 2, 3, 1, 1, 10),
    _Mip6MnBLAcceptedTime_Type()
)
mip6MnBLAcceptedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6MnBLAcceptedTime.setStatus("current")
_Mip6MnBLRetransmissions_Type = Gauge32
_Mip6MnBLRetransmissions_Object = MibTableColumn
mip6MnBLRetransmissions = _Mip6MnBLRetransmissions_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 2, 3, 1, 1, 11),
    _Mip6MnBLRetransmissions_Type()
)
mip6MnBLRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6MnBLRetransmissions.setStatus("current")
_Mip6MnBLDontSendBUFlag_Type = TruthValue
_Mip6MnBLDontSendBUFlag_Object = MibTableColumn
mip6MnBLDontSendBUFlag = _Mip6MnBLDontSendBUFlag_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 2, 3, 1, 1, 12),
    _Mip6MnBLDontSendBUFlag_Type()
)
mip6MnBLDontSendBUFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6MnBLDontSendBUFlag.setStatus("current")
_Mip6MnRegnCounters_ObjectIdentity = ObjectIdentity
mip6MnRegnCounters = _Mip6MnRegnCounters_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 133, 1, 2, 3, 2)
)
_Mip6MnMobilityMessagesSent_Type = Counter32
_Mip6MnMobilityMessagesSent_Object = MibScalar
mip6MnMobilityMessagesSent = _Mip6MnMobilityMessagesSent_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 2, 3, 2, 1),
    _Mip6MnMobilityMessagesSent_Type()
)
mip6MnMobilityMessagesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6MnMobilityMessagesSent.setStatus("current")
_Mip6MnMobilityMessagesRecd_Type = Counter32
_Mip6MnMobilityMessagesRecd_Object = MibScalar
mip6MnMobilityMessagesRecd = _Mip6MnMobilityMessagesRecd_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 2, 3, 2, 2),
    _Mip6MnMobilityMessagesRecd_Type()
)
mip6MnMobilityMessagesRecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6MnMobilityMessagesRecd.setStatus("current")
_Mip6MnBUsToHA_Type = Counter32
_Mip6MnBUsToHA_Object = MibScalar
mip6MnBUsToHA = _Mip6MnBUsToHA_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 2, 3, 2, 3),
    _Mip6MnBUsToHA_Type()
)
mip6MnBUsToHA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6MnBUsToHA.setStatus("current")
_Mip6MnBUAcksFromHA_Type = Counter32
_Mip6MnBUAcksFromHA_Object = MibScalar
mip6MnBUAcksFromHA = _Mip6MnBUAcksFromHA_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 2, 3, 2, 4),
    _Mip6MnBUAcksFromHA_Type()
)
mip6MnBUAcksFromHA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6MnBUAcksFromHA.setStatus("current")
_Mip6MnBUsToCN_Type = Counter32
_Mip6MnBUsToCN_Object = MibScalar
mip6MnBUsToCN = _Mip6MnBUsToCN_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 2, 3, 2, 5),
    _Mip6MnBUsToCN_Type()
)
mip6MnBUsToCN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6MnBUsToCN.setStatus("current")
_Mip6MnBUAcksFromCN_Type = Counter32
_Mip6MnBUAcksFromCN_Object = MibScalar
mip6MnBUAcksFromCN = _Mip6MnBUAcksFromCN_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 2, 3, 2, 6),
    _Mip6MnBUAcksFromCN_Type()
)
mip6MnBUAcksFromCN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6MnBUAcksFromCN.setStatus("current")
_Mip6MnBindingErrorsFromCN_Type = Counter32
_Mip6MnBindingErrorsFromCN_Object = MibScalar
mip6MnBindingErrorsFromCN = _Mip6MnBindingErrorsFromCN_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 2, 3, 2, 7),
    _Mip6MnBindingErrorsFromCN_Type()
)
mip6MnBindingErrorsFromCN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6MnBindingErrorsFromCN.setStatus("current")
_Mip6MnICMPErrorsRecd_Type = Counter32
_Mip6MnICMPErrorsRecd_Object = MibScalar
mip6MnICMPErrorsRecd = _Mip6MnICMPErrorsRecd_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 2, 3, 2, 8),
    _Mip6MnICMPErrorsRecd_Type()
)
mip6MnICMPErrorsRecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6MnICMPErrorsRecd.setStatus("current")
_Mip6MnBRRequestsRecd_Type = Counter32
_Mip6MnBRRequestsRecd_Object = MibScalar
mip6MnBRRequestsRecd = _Mip6MnBRRequestsRecd_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 2, 3, 2, 9),
    _Mip6MnBRRequestsRecd_Type()
)
mip6MnBRRequestsRecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6MnBRRequestsRecd.setStatus("current")
_Mip6Cn_ObjectIdentity = ObjectIdentity
mip6Cn = _Mip6Cn_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 133, 1, 3)
)
_Mip6CnSystem_ObjectIdentity = ObjectIdentity
mip6CnSystem = _Mip6CnSystem_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 133, 1, 3, 1)
)
_Mip6CnStats_ObjectIdentity = ObjectIdentity
mip6CnStats = _Mip6CnStats_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 133, 1, 3, 2)
)
_Mip6CnGlobalStats_ObjectIdentity = ObjectIdentity
mip6CnGlobalStats = _Mip6CnGlobalStats_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 133, 1, 3, 2, 1)
)
_Mip6CnHomeTestInitsRecd_Type = Counter32
_Mip6CnHomeTestInitsRecd_Object = MibScalar
mip6CnHomeTestInitsRecd = _Mip6CnHomeTestInitsRecd_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 3, 2, 1, 1),
    _Mip6CnHomeTestInitsRecd_Type()
)
mip6CnHomeTestInitsRecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6CnHomeTestInitsRecd.setStatus("current")
_Mip6CnHomeTestsSent_Type = Counter32
_Mip6CnHomeTestsSent_Object = MibScalar
mip6CnHomeTestsSent = _Mip6CnHomeTestsSent_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 3, 2, 1, 2),
    _Mip6CnHomeTestsSent_Type()
)
mip6CnHomeTestsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6CnHomeTestsSent.setStatus("current")
_Mip6CnCareOfTestInitsRecd_Type = Counter32
_Mip6CnCareOfTestInitsRecd_Object = MibScalar
mip6CnCareOfTestInitsRecd = _Mip6CnCareOfTestInitsRecd_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 3, 2, 1, 3),
    _Mip6CnCareOfTestInitsRecd_Type()
)
mip6CnCareOfTestInitsRecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6CnCareOfTestInitsRecd.setStatus("current")
_Mip6CnCareOfTestsSent_Type = Counter32
_Mip6CnCareOfTestsSent_Object = MibScalar
mip6CnCareOfTestsSent = _Mip6CnCareOfTestsSent_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 3, 2, 1, 4),
    _Mip6CnCareOfTestsSent_Type()
)
mip6CnCareOfTestsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6CnCareOfTestsSent.setStatus("current")
_Mip6CnBUsRecd_Type = Counter32
_Mip6CnBUsRecd_Object = MibScalar
mip6CnBUsRecd = _Mip6CnBUsRecd_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 3, 2, 1, 5),
    _Mip6CnBUsRecd_Type()
)
mip6CnBUsRecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6CnBUsRecd.setStatus("current")
_Mip6CnBUAcksSent_Type = Counter32
_Mip6CnBUAcksSent_Object = MibScalar
mip6CnBUAcksSent = _Mip6CnBUAcksSent_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 3, 2, 1, 6),
    _Mip6CnBUAcksSent_Type()
)
mip6CnBUAcksSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6CnBUAcksSent.setStatus("current")
_Mip6CnBRsSent_Type = Counter32
_Mip6CnBRsSent_Object = MibScalar
mip6CnBRsSent = _Mip6CnBRsSent_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 3, 2, 1, 7),
    _Mip6CnBRsSent_Type()
)
mip6CnBRsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6CnBRsSent.setStatus("current")
_Mip6CnBindingErrors_Type = Counter32
_Mip6CnBindingErrors_Object = MibScalar
mip6CnBindingErrors = _Mip6CnBindingErrors_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 3, 2, 1, 8),
    _Mip6CnBindingErrors_Type()
)
mip6CnBindingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6CnBindingErrors.setStatus("current")
_Mip6CnBUsAccepted_Type = Counter32
_Mip6CnBUsAccepted_Object = MibScalar
mip6CnBUsAccepted = _Mip6CnBUsAccepted_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 3, 2, 1, 9),
    _Mip6CnBUsAccepted_Type()
)
mip6CnBUsAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6CnBUsAccepted.setStatus("current")
_Mip6CnBUsRejected_Type = Counter32
_Mip6CnBUsRejected_Object = MibScalar
mip6CnBUsRejected = _Mip6CnBUsRejected_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 3, 2, 1, 10),
    _Mip6CnBUsRejected_Type()
)
mip6CnBUsRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6CnBUsRejected.setStatus("current")
_Mip6CnReasonUnspecified_Type = Counter32
_Mip6CnReasonUnspecified_Object = MibScalar
mip6CnReasonUnspecified = _Mip6CnReasonUnspecified_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 3, 2, 1, 11),
    _Mip6CnReasonUnspecified_Type()
)
mip6CnReasonUnspecified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6CnReasonUnspecified.setStatus("current")
_Mip6CnInsufficientResource_Type = Counter32
_Mip6CnInsufficientResource_Object = MibScalar
mip6CnInsufficientResource = _Mip6CnInsufficientResource_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 3, 2, 1, 12),
    _Mip6CnInsufficientResource_Type()
)
mip6CnInsufficientResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6CnInsufficientResource.setStatus("current")
_Mip6CnHomeRegnNotSupported_Type = Counter32
_Mip6CnHomeRegnNotSupported_Object = MibScalar
mip6CnHomeRegnNotSupported = _Mip6CnHomeRegnNotSupported_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 3, 2, 1, 13),
    _Mip6CnHomeRegnNotSupported_Type()
)
mip6CnHomeRegnNotSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6CnHomeRegnNotSupported.setStatus("current")
_Mip6CnSeqNumberOutOfWindow_Type = Counter32
_Mip6CnSeqNumberOutOfWindow_Object = MibScalar
mip6CnSeqNumberOutOfWindow = _Mip6CnSeqNumberOutOfWindow_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 3, 2, 1, 14),
    _Mip6CnSeqNumberOutOfWindow_Type()
)
mip6CnSeqNumberOutOfWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6CnSeqNumberOutOfWindow.setStatus("current")
_Mip6CnExpiredHomeNonceIndex_Type = Counter32
_Mip6CnExpiredHomeNonceIndex_Object = MibScalar
mip6CnExpiredHomeNonceIndex = _Mip6CnExpiredHomeNonceIndex_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 3, 2, 1, 15),
    _Mip6CnExpiredHomeNonceIndex_Type()
)
mip6CnExpiredHomeNonceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6CnExpiredHomeNonceIndex.setStatus("current")
_Mip6CnExpiredCareOfNonceIndex_Type = Counter32
_Mip6CnExpiredCareOfNonceIndex_Object = MibScalar
mip6CnExpiredCareOfNonceIndex = _Mip6CnExpiredCareOfNonceIndex_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 3, 2, 1, 16),
    _Mip6CnExpiredCareOfNonceIndex_Type()
)
mip6CnExpiredCareOfNonceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6CnExpiredCareOfNonceIndex.setStatus("current")
_Mip6CnExpiredNonce_Type = Counter32
_Mip6CnExpiredNonce_Object = MibScalar
mip6CnExpiredNonce = _Mip6CnExpiredNonce_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 3, 2, 1, 17),
    _Mip6CnExpiredNonce_Type()
)
mip6CnExpiredNonce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6CnExpiredNonce.setStatus("current")
_Mip6CnRegTypeChangeDisallowed_Type = Counter32
_Mip6CnRegTypeChangeDisallowed_Object = MibScalar
mip6CnRegTypeChangeDisallowed = _Mip6CnRegTypeChangeDisallowed_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 3, 2, 1, 18),
    _Mip6CnRegTypeChangeDisallowed_Type()
)
mip6CnRegTypeChangeDisallowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6CnRegTypeChangeDisallowed.setStatus("current")
_Mip6CnCounterTable_Object = MibTable
mip6CnCounterTable = _Mip6CnCounterTable_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 3, 2, 2)
)
if mibBuilder.loadTexts:
    mip6CnCounterTable.setStatus("current")
_Mip6CnCounterEntry_Object = MibTableRow
mip6CnCounterEntry = _Mip6CnCounterEntry_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 3, 2, 2, 1)
)
mip6CnCounterEntry.setIndexNames(
    (0, "MOBILEIPV6-MIB", "mip6BindingHomeAddressType"),
    (0, "MOBILEIPV6-MIB", "mip6BindingHomeAddress"),
)
if mibBuilder.loadTexts:
    mip6CnCounterEntry.setStatus("current")
_Mip6CnBURequestsAccepted_Type = Counter32
_Mip6CnBURequestsAccepted_Object = MibTableColumn
mip6CnBURequestsAccepted = _Mip6CnBURequestsAccepted_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 3, 2, 2, 1, 1),
    _Mip6CnBURequestsAccepted_Type()
)
mip6CnBURequestsAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6CnBURequestsAccepted.setStatus("current")
_Mip6CnBURequestsRejected_Type = Counter32
_Mip6CnBURequestsRejected_Object = MibTableColumn
mip6CnBURequestsRejected = _Mip6CnBURequestsRejected_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 3, 2, 2, 1, 2),
    _Mip6CnBURequestsRejected_Type()
)
mip6CnBURequestsRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6CnBURequestsRejected.setStatus("current")
_Mip6CnBCEntryCreationTime_Type = DateAndTime
_Mip6CnBCEntryCreationTime_Object = MibTableColumn
mip6CnBCEntryCreationTime = _Mip6CnBCEntryCreationTime_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 3, 2, 2, 1, 3),
    _Mip6CnBCEntryCreationTime_Type()
)
mip6CnBCEntryCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6CnBCEntryCreationTime.setStatus("current")
_Mip6CnBUAcceptedTime_Type = DateAndTime
_Mip6CnBUAcceptedTime_Object = MibTableColumn
mip6CnBUAcceptedTime = _Mip6CnBUAcceptedTime_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 3, 2, 2, 1, 4),
    _Mip6CnBUAcceptedTime_Type()
)
mip6CnBUAcceptedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6CnBUAcceptedTime.setStatus("current")
_Mip6CnBURejectionTime_Type = DateAndTime
_Mip6CnBURejectionTime_Object = MibTableColumn
mip6CnBURejectionTime = _Mip6CnBURejectionTime_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 3, 2, 2, 1, 5),
    _Mip6CnBURejectionTime_Type()
)
mip6CnBURejectionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6CnBURejectionTime.setStatus("current")
_Mip6CnBURejectionCode_Type = Mip6BURequestRejectionCode
_Mip6CnBURejectionCode_Object = MibTableColumn
mip6CnBURejectionCode = _Mip6CnBURejectionCode_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 3, 2, 2, 1, 6),
    _Mip6CnBURejectionCode_Type()
)
mip6CnBURejectionCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6CnBURejectionCode.setStatus("current")
_Mip6CnCtrDiscontinuityTime_Type = TimeStamp
_Mip6CnCtrDiscontinuityTime_Object = MibTableColumn
mip6CnCtrDiscontinuityTime = _Mip6CnCtrDiscontinuityTime_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 3, 2, 2, 1, 7),
    _Mip6CnCtrDiscontinuityTime_Type()
)
mip6CnCtrDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6CnCtrDiscontinuityTime.setStatus("current")
_Mip6Ha_ObjectIdentity = ObjectIdentity
mip6Ha = _Mip6Ha_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 133, 1, 4)
)
_Mip6HaAdvertisement_ObjectIdentity = ObjectIdentity
mip6HaAdvertisement = _Mip6HaAdvertisement_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 133, 1, 4, 1)
)
_Mip6HaAdvsRecd_Type = Counter32
_Mip6HaAdvsRecd_Object = MibScalar
mip6HaAdvsRecd = _Mip6HaAdvsRecd_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 4, 1, 1),
    _Mip6HaAdvsRecd_Type()
)
mip6HaAdvsRecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6HaAdvsRecd.setStatus("current")
_Mip6HaAdvsSent_Type = Counter32
_Mip6HaAdvsSent_Object = MibScalar
mip6HaAdvsSent = _Mip6HaAdvsSent_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 4, 1, 2),
    _Mip6HaAdvsSent_Type()
)
mip6HaAdvsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6HaAdvsSent.setStatus("current")
_Mip6HaConfTable_Object = MibTable
mip6HaConfTable = _Mip6HaConfTable_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 4, 1, 3)
)
if mibBuilder.loadTexts:
    mip6HaConfTable.setStatus("current")
_Mip6HaConfEntry_Object = MibTableRow
mip6HaConfEntry = _Mip6HaConfEntry_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 4, 1, 3, 1)
)
mip6HaConfEntry.setIndexNames(
    (0, "IP-MIB", "ipv6InterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    mip6HaConfEntry.setStatus("current")


class _Mip6HaAdvPreference_Type(Integer32):
    """Custom type mip6HaAdvPreference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Mip6HaAdvPreference_Type.__name__ = "Integer32"
_Mip6HaAdvPreference_Object = MibTableColumn
mip6HaAdvPreference = _Mip6HaAdvPreference_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 4, 1, 3, 1, 1),
    _Mip6HaAdvPreference_Type()
)
mip6HaAdvPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mip6HaAdvPreference.setStatus("current")


class _Mip6HaAdvLifetime_Type(Integer32):
    """Custom type mip6HaAdvLifetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Mip6HaAdvLifetime_Type.__name__ = "Integer32"
_Mip6HaAdvLifetime_Object = MibTableColumn
mip6HaAdvLifetime = _Mip6HaAdvLifetime_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 4, 1, 3, 1, 2),
    _Mip6HaAdvLifetime_Type()
)
mip6HaAdvLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mip6HaAdvLifetime.setStatus("current")
if mibBuilder.loadTexts:
    mip6HaAdvLifetime.setUnits("seconds")


class _Mip6HaPrefixAdv_Type(Integer32):
    """Custom type mip6HaPrefixAdv based on Integer32"""
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


_Mip6HaPrefixAdv_Type.__name__ = "Integer32"
_Mip6HaPrefixAdv_Object = MibTableColumn
mip6HaPrefixAdv = _Mip6HaPrefixAdv_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 4, 1, 3, 1, 3),
    _Mip6HaPrefixAdv_Type()
)
mip6HaPrefixAdv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mip6HaPrefixAdv.setStatus("current")


class _Mip6HaPrefixSolicitation_Type(Integer32):
    """Custom type mip6HaPrefixSolicitation based on Integer32"""
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


_Mip6HaPrefixSolicitation_Type.__name__ = "Integer32"
_Mip6HaPrefixSolicitation_Object = MibTableColumn
mip6HaPrefixSolicitation = _Mip6HaPrefixSolicitation_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 4, 1, 3, 1, 4),
    _Mip6HaPrefixSolicitation_Type()
)
mip6HaPrefixSolicitation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mip6HaPrefixSolicitation.setStatus("current")


class _Mip6HaMCastCtlMsgSupport_Type(Integer32):
    """Custom type mip6HaMCastCtlMsgSupport based on Integer32"""
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


_Mip6HaMCastCtlMsgSupport_Type.__name__ = "Integer32"
_Mip6HaMCastCtlMsgSupport_Object = MibTableColumn
mip6HaMCastCtlMsgSupport = _Mip6HaMCastCtlMsgSupport_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 4, 1, 3, 1, 5),
    _Mip6HaMCastCtlMsgSupport_Type()
)
mip6HaMCastCtlMsgSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mip6HaMCastCtlMsgSupport.setStatus("current")
_Mip6HaListTable_Object = MibTable
mip6HaListTable = _Mip6HaListTable_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 4, 1, 4)
)
if mibBuilder.loadTexts:
    mip6HaListTable.setStatus("current")
_Mip6HaListEntry_Object = MibTableRow
mip6HaListEntry = _Mip6HaListEntry_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 4, 1, 4, 1)
)
mip6HaListEntry.setIndexNames(
    (0, "IP-MIB", "ipv6InterfaceIfIndex"),
    (0, "MOBILEIPV6-MIB", "mip6HaLinkLocalAddressType"),
    (0, "MOBILEIPV6-MIB", "mip6HaLinkLocalAddress"),
)
if mibBuilder.loadTexts:
    mip6HaListEntry.setStatus("current")
_Mip6HaLinkLocalAddressType_Type = InetAddressType
_Mip6HaLinkLocalAddressType_Object = MibTableColumn
mip6HaLinkLocalAddressType = _Mip6HaLinkLocalAddressType_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 4, 1, 4, 1, 1),
    _Mip6HaLinkLocalAddressType_Type()
)
mip6HaLinkLocalAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mip6HaLinkLocalAddressType.setStatus("current")
_Mip6HaLinkLocalAddress_Type = InetAddress
_Mip6HaLinkLocalAddress_Object = MibTableColumn
mip6HaLinkLocalAddress = _Mip6HaLinkLocalAddress_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 4, 1, 4, 1, 2),
    _Mip6HaLinkLocalAddress_Type()
)
mip6HaLinkLocalAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mip6HaLinkLocalAddress.setStatus("current")
_Mip6HaPreference_Type = Integer32
_Mip6HaPreference_Object = MibTableColumn
mip6HaPreference = _Mip6HaPreference_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 4, 1, 4, 1, 3),
    _Mip6HaPreference_Type()
)
mip6HaPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6HaPreference.setStatus("current")
_Mip6HaRecvLifeTime_Type = Gauge32
_Mip6HaRecvLifeTime_Object = MibTableColumn
mip6HaRecvLifeTime = _Mip6HaRecvLifeTime_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 4, 1, 4, 1, 4),
    _Mip6HaRecvLifeTime_Type()
)
mip6HaRecvLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6HaRecvLifeTime.setStatus("current")
_Mip6HaRecvTimeStamp_Type = DateAndTime
_Mip6HaRecvTimeStamp_Object = MibTableColumn
mip6HaRecvTimeStamp = _Mip6HaRecvTimeStamp_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 4, 1, 4, 1, 5),
    _Mip6HaRecvTimeStamp_Type()
)
mip6HaRecvTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6HaRecvTimeStamp.setStatus("current")
_Mip6HaGlAddrTable_Object = MibTable
mip6HaGlAddrTable = _Mip6HaGlAddrTable_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 4, 1, 5)
)
if mibBuilder.loadTexts:
    mip6HaGlAddrTable.setStatus("current")
_Mip6HaGlAddrEntry_Object = MibTableRow
mip6HaGlAddrEntry = _Mip6HaGlAddrEntry_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 4, 1, 5, 1)
)
mip6HaGlAddrEntry.setIndexNames(
    (0, "IP-MIB", "ipv6InterfaceIfIndex"),
    (0, "MOBILEIPV6-MIB", "mip6HaLinkLocalAddressType"),
    (0, "MOBILEIPV6-MIB", "mip6HaLinkLocalAddress"),
    (0, "MOBILEIPV6-MIB", "mip6HaGaAddrSeqNo"),
)
if mibBuilder.loadTexts:
    mip6HaGlAddrEntry.setStatus("current")


class _Mip6HaGaAddrSeqNo_Type(Integer32):
    """Custom type mip6HaGaAddrSeqNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Mip6HaGaAddrSeqNo_Type.__name__ = "Integer32"
_Mip6HaGaAddrSeqNo_Object = MibTableColumn
mip6HaGaAddrSeqNo = _Mip6HaGaAddrSeqNo_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 4, 1, 5, 1, 1),
    _Mip6HaGaAddrSeqNo_Type()
)
mip6HaGaAddrSeqNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mip6HaGaAddrSeqNo.setStatus("current")
_Mip6HaGaGlobalAddressType_Type = InetAddressType
_Mip6HaGaGlobalAddressType_Object = MibTableColumn
mip6HaGaGlobalAddressType = _Mip6HaGaGlobalAddressType_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 4, 1, 5, 1, 2),
    _Mip6HaGaGlobalAddressType_Type()
)
mip6HaGaGlobalAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6HaGaGlobalAddressType.setStatus("current")
_Mip6HaGaGlobalAddress_Type = InetAddress
_Mip6HaGaGlobalAddress_Object = MibTableColumn
mip6HaGaGlobalAddress = _Mip6HaGaGlobalAddress_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 4, 1, 5, 1, 3),
    _Mip6HaGaGlobalAddress_Type()
)
mip6HaGaGlobalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6HaGaGlobalAddress.setStatus("current")
_Mip6HaStats_ObjectIdentity = ObjectIdentity
mip6HaStats = _Mip6HaStats_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 133, 1, 4, 2)
)
_Mip6HaGlobalStats_ObjectIdentity = ObjectIdentity
mip6HaGlobalStats = _Mip6HaGlobalStats_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 133, 1, 4, 2, 1)
)
_Mip6HaHomeTestInitsRecd_Type = Counter32
_Mip6HaHomeTestInitsRecd_Object = MibScalar
mip6HaHomeTestInitsRecd = _Mip6HaHomeTestInitsRecd_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 4, 2, 1, 1),
    _Mip6HaHomeTestInitsRecd_Type()
)
mip6HaHomeTestInitsRecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6HaHomeTestInitsRecd.setStatus("current")
_Mip6HaHomeTestsSent_Type = Counter32
_Mip6HaHomeTestsSent_Object = MibScalar
mip6HaHomeTestsSent = _Mip6HaHomeTestsSent_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 4, 2, 1, 2),
    _Mip6HaHomeTestsSent_Type()
)
mip6HaHomeTestsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6HaHomeTestsSent.setStatus("current")
_Mip6HaBUsRecd_Type = Counter32
_Mip6HaBUsRecd_Object = MibScalar
mip6HaBUsRecd = _Mip6HaBUsRecd_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 4, 2, 1, 3),
    _Mip6HaBUsRecd_Type()
)
mip6HaBUsRecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6HaBUsRecd.setStatus("current")
_Mip6HaBUAcksSent_Type = Counter32
_Mip6HaBUAcksSent_Object = MibScalar
mip6HaBUAcksSent = _Mip6HaBUAcksSent_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 4, 2, 1, 4),
    _Mip6HaBUAcksSent_Type()
)
mip6HaBUAcksSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6HaBUAcksSent.setStatus("current")
_Mip6HaBRAdviceSent_Type = Counter32
_Mip6HaBRAdviceSent_Object = MibScalar
mip6HaBRAdviceSent = _Mip6HaBRAdviceSent_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 4, 2, 1, 5),
    _Mip6HaBRAdviceSent_Type()
)
mip6HaBRAdviceSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6HaBRAdviceSent.setStatus("current")
_Mip6HaBUsAccepted_Type = Counter32
_Mip6HaBUsAccepted_Object = MibScalar
mip6HaBUsAccepted = _Mip6HaBUsAccepted_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 4, 2, 1, 6),
    _Mip6HaBUsAccepted_Type()
)
mip6HaBUsAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6HaBUsAccepted.setStatus("current")
_Mip6HaPrefDiscoverReqd_Type = Counter32
_Mip6HaPrefDiscoverReqd_Object = MibScalar
mip6HaPrefDiscoverReqd = _Mip6HaPrefDiscoverReqd_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 4, 2, 1, 7),
    _Mip6HaPrefDiscoverReqd_Type()
)
mip6HaPrefDiscoverReqd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6HaPrefDiscoverReqd.setStatus("current")
_Mip6HaReasonUnspecified_Type = Counter32
_Mip6HaReasonUnspecified_Object = MibScalar
mip6HaReasonUnspecified = _Mip6HaReasonUnspecified_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 4, 2, 1, 8),
    _Mip6HaReasonUnspecified_Type()
)
mip6HaReasonUnspecified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6HaReasonUnspecified.setStatus("current")
_Mip6HaAdmProhibited_Type = Counter32
_Mip6HaAdmProhibited_Object = MibScalar
mip6HaAdmProhibited = _Mip6HaAdmProhibited_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 4, 2, 1, 9),
    _Mip6HaAdmProhibited_Type()
)
mip6HaAdmProhibited.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6HaAdmProhibited.setStatus("current")
_Mip6HaInsufficientResource_Type = Counter32
_Mip6HaInsufficientResource_Object = MibScalar
mip6HaInsufficientResource = _Mip6HaInsufficientResource_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 4, 2, 1, 10),
    _Mip6HaInsufficientResource_Type()
)
mip6HaInsufficientResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6HaInsufficientResource.setStatus("current")
_Mip6HaHomeRegnNotSupported_Type = Counter32
_Mip6HaHomeRegnNotSupported_Object = MibScalar
mip6HaHomeRegnNotSupported = _Mip6HaHomeRegnNotSupported_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 4, 2, 1, 11),
    _Mip6HaHomeRegnNotSupported_Type()
)
mip6HaHomeRegnNotSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6HaHomeRegnNotSupported.setStatus("current")
_Mip6HaNotHomeSubnet_Type = Counter32
_Mip6HaNotHomeSubnet_Object = MibScalar
mip6HaNotHomeSubnet = _Mip6HaNotHomeSubnet_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 4, 2, 1, 12),
    _Mip6HaNotHomeSubnet_Type()
)
mip6HaNotHomeSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6HaNotHomeSubnet.setStatus("current")
_Mip6HaNotHomeAgentForThisMN_Type = Counter32
_Mip6HaNotHomeAgentForThisMN_Object = MibScalar
mip6HaNotHomeAgentForThisMN = _Mip6HaNotHomeAgentForThisMN_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 4, 2, 1, 13),
    _Mip6HaNotHomeAgentForThisMN_Type()
)
mip6HaNotHomeAgentForThisMN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6HaNotHomeAgentForThisMN.setStatus("current")
_Mip6HaDupAddrDetectionFailed_Type = Counter32
_Mip6HaDupAddrDetectionFailed_Object = MibScalar
mip6HaDupAddrDetectionFailed = _Mip6HaDupAddrDetectionFailed_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 4, 2, 1, 14),
    _Mip6HaDupAddrDetectionFailed_Type()
)
mip6HaDupAddrDetectionFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6HaDupAddrDetectionFailed.setStatus("current")
_Mip6HaSeqNumberOutOfWindow_Type = Counter32
_Mip6HaSeqNumberOutOfWindow_Object = MibScalar
mip6HaSeqNumberOutOfWindow = _Mip6HaSeqNumberOutOfWindow_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 4, 2, 1, 15),
    _Mip6HaSeqNumberOutOfWindow_Type()
)
mip6HaSeqNumberOutOfWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6HaSeqNumberOutOfWindow.setStatus("current")
_Mip6HaExpiredHomeNonceIndex_Type = Counter32
_Mip6HaExpiredHomeNonceIndex_Object = MibScalar
mip6HaExpiredHomeNonceIndex = _Mip6HaExpiredHomeNonceIndex_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 4, 2, 1, 16),
    _Mip6HaExpiredHomeNonceIndex_Type()
)
mip6HaExpiredHomeNonceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6HaExpiredHomeNonceIndex.setStatus("current")
_Mip6HaRegTypeChangeDisallowed_Type = Counter32
_Mip6HaRegTypeChangeDisallowed_Object = MibScalar
mip6HaRegTypeChangeDisallowed = _Mip6HaRegTypeChangeDisallowed_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 4, 2, 1, 17),
    _Mip6HaRegTypeChangeDisallowed_Type()
)
mip6HaRegTypeChangeDisallowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6HaRegTypeChangeDisallowed.setStatus("current")
_Mip6HaCounterTable_Object = MibTable
mip6HaCounterTable = _Mip6HaCounterTable_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 4, 2, 2)
)
if mibBuilder.loadTexts:
    mip6HaCounterTable.setStatus("current")
_Mip6HaCounterEntry_Object = MibTableRow
mip6HaCounterEntry = _Mip6HaCounterEntry_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 4, 2, 2, 1)
)
mip6HaCounterEntry.setIndexNames(
    (0, "MOBILEIPV6-MIB", "mip6BindingHomeAddressType"),
    (0, "MOBILEIPV6-MIB", "mip6BindingHomeAddress"),
)
if mibBuilder.loadTexts:
    mip6HaCounterEntry.setStatus("current")
_Mip6HaBURequestsAccepted_Type = Counter32
_Mip6HaBURequestsAccepted_Object = MibTableColumn
mip6HaBURequestsAccepted = _Mip6HaBURequestsAccepted_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 4, 2, 2, 1, 1),
    _Mip6HaBURequestsAccepted_Type()
)
mip6HaBURequestsAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6HaBURequestsAccepted.setStatus("current")
_Mip6HaBURequestsDenied_Type = Counter32
_Mip6HaBURequestsDenied_Object = MibTableColumn
mip6HaBURequestsDenied = _Mip6HaBURequestsDenied_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 4, 2, 2, 1, 2),
    _Mip6HaBURequestsDenied_Type()
)
mip6HaBURequestsDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6HaBURequestsDenied.setStatus("current")
_Mip6HaBCEntryCreationTime_Type = DateAndTime
_Mip6HaBCEntryCreationTime_Object = MibTableColumn
mip6HaBCEntryCreationTime = _Mip6HaBCEntryCreationTime_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 4, 2, 2, 1, 3),
    _Mip6HaBCEntryCreationTime_Type()
)
mip6HaBCEntryCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6HaBCEntryCreationTime.setStatus("current")
if mibBuilder.loadTexts:
    mip6HaBCEntryCreationTime.setUnits("seconds")
_Mip6HaBUAcceptedTime_Type = DateAndTime
_Mip6HaBUAcceptedTime_Object = MibTableColumn
mip6HaBUAcceptedTime = _Mip6HaBUAcceptedTime_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 4, 2, 2, 1, 4),
    _Mip6HaBUAcceptedTime_Type()
)
mip6HaBUAcceptedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6HaBUAcceptedTime.setStatus("current")
_Mip6HaBURejectionTime_Type = DateAndTime
_Mip6HaBURejectionTime_Object = MibTableColumn
mip6HaBURejectionTime = _Mip6HaBURejectionTime_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 4, 2, 2, 1, 5),
    _Mip6HaBURejectionTime_Type()
)
mip6HaBURejectionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6HaBURejectionTime.setStatus("current")
_Mip6HaRecentBURejectionCode_Type = Mip6BURequestRejectionCode
_Mip6HaRecentBURejectionCode_Object = MibTableColumn
mip6HaRecentBURejectionCode = _Mip6HaRecentBURejectionCode_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 4, 2, 2, 1, 6),
    _Mip6HaRecentBURejectionCode_Type()
)
mip6HaRecentBURejectionCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6HaRecentBURejectionCode.setStatus("current")
_Mip6HaCtrDiscontinuityTime_Type = TimeStamp
_Mip6HaCtrDiscontinuityTime_Object = MibTableColumn
mip6HaCtrDiscontinuityTime = _Mip6HaCtrDiscontinuityTime_Object(
    (1, 3, 6, 1, 2, 1, 133, 1, 4, 2, 2, 1, 7),
    _Mip6HaCtrDiscontinuityTime_Type()
)
mip6HaCtrDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mip6HaCtrDiscontinuityTime.setStatus("current")
_Mip6Conformance_ObjectIdentity = ObjectIdentity
mip6Conformance = _Mip6Conformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 133, 2)
)
_Mip6Groups_ObjectIdentity = ObjectIdentity
mip6Groups = _Mip6Groups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 133, 2, 1)
)
_Mip6Compliances_ObjectIdentity = ObjectIdentity
mip6Compliances = _Mip6Compliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 133, 2, 2)
)

# Managed Objects groups

mip6SystemGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 133, 2, 1, 1)
)
mip6SystemGroup.setObjects(
      *(("MOBILEIPV6-MIB", "mip6Capabilities"),
        ("MOBILEIPV6-MIB", "mip6Status"))
)
if mibBuilder.loadTexts:
    mip6SystemGroup.setStatus("current")

mip6BindingCacheGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 133, 2, 1, 2)
)
mip6BindingCacheGroup.setObjects(
      *(("MOBILEIPV6-MIB", "mip6BindingCOAType"),
        ("MOBILEIPV6-MIB", "mip6BindingCOA"),
        ("MOBILEIPV6-MIB", "mip6BindingTimeRegistered"),
        ("MOBILEIPV6-MIB", "mip6BindingTimeGranted"),
        ("MOBILEIPV6-MIB", "mip6BindingTimeRemaining"),
        ("MOBILEIPV6-MIB", "mip6BindingMaxSeq"),
        ("MOBILEIPV6-MIB", "mip6BindingHomeRegn"),
        ("MOBILEIPV6-MIB", "mip6BindingUsageTS"),
        ("MOBILEIPV6-MIB", "mip6BindingUsageCount"),
        ("MOBILEIPV6-MIB", "mip6BindingAdminStatus"))
)
if mibBuilder.loadTexts:
    mip6BindingCacheGroup.setStatus("current")

mip6BindingHstGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 133, 2, 1, 3)
)
mip6BindingHstGroup.setObjects(
      *(("MOBILEIPV6-MIB", "mip6BindingHstCOAType"),
        ("MOBILEIPV6-MIB", "mip6BindingHstCOA"),
        ("MOBILEIPV6-MIB", "mip6BindingHstTimeRegistered"),
        ("MOBILEIPV6-MIB", "mip6BindingHstTimeExpired"),
        ("MOBILEIPV6-MIB", "mip6BindingHstHomeRegn"),
        ("MOBILEIPV6-MIB", "mip6BindingHstUsageTS"),
        ("MOBILEIPV6-MIB", "mip6BindingHstUsageCount"))
)
if mibBuilder.loadTexts:
    mip6BindingHstGroup.setStatus("current")

mip6TotalTrafficGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 133, 2, 1, 4)
)
mip6TotalTrafficGroup.setObjects(
      *(("MOBILEIPV6-MIB", "mip6InOctets"),
        ("MOBILEIPV6-MIB", "mip6HCInOctets"),
        ("MOBILEIPV6-MIB", "mip6InPkts"),
        ("MOBILEIPV6-MIB", "mip6HCInPkts"),
        ("MOBILEIPV6-MIB", "mip6OutOctets"),
        ("MOBILEIPV6-MIB", "mip6HCOutOctets"),
        ("MOBILEIPV6-MIB", "mip6OutPkts"),
        ("MOBILEIPV6-MIB", "mip6HCOutPkts"),
        ("MOBILEIPV6-MIB", "mip6CounterDiscontinuityTime"))
)
if mibBuilder.loadTexts:
    mip6TotalTrafficGroup.setStatus("current")

mip6NodeTrafficGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 133, 2, 1, 5)
)
mip6NodeTrafficGroup.setObjects(
      *(("MOBILEIPV6-MIB", "mip6NodeInOctets"),
        ("MOBILEIPV6-MIB", "mip6HCNodeInOctets"),
        ("MOBILEIPV6-MIB", "mip6NodeInPkts"),
        ("MOBILEIPV6-MIB", "mip6HCNodeInPkts"),
        ("MOBILEIPV6-MIB", "mip6NodeOutOctets"),
        ("MOBILEIPV6-MIB", "mip6HCNodeOutOctets"),
        ("MOBILEIPV6-MIB", "mip6NodeOutPkts"),
        ("MOBILEIPV6-MIB", "mip6HCNodeOutPkts"),
        ("MOBILEIPV6-MIB", "mip6NodeCtrDiscontinuityTime"))
)
if mibBuilder.loadTexts:
    mip6NodeTrafficGroup.setStatus("current")

mip6MnSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 133, 2, 1, 6)
)
mip6MnSystemGroup.setObjects(
    ("MOBILEIPV6-MIB", "mip6MnHomeAddressState")
)
if mibBuilder.loadTexts:
    mip6MnSystemGroup.setStatus("current")

mip6MnConfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 133, 2, 1, 7)
)
mip6MnConfGroup.setObjects(
      *(("MOBILEIPV6-MIB", "mip6MnDiscoveryRequests"),
        ("MOBILEIPV6-MIB", "mip6MnDiscoveryReplies"),
        ("MOBILEIPV6-MIB", "mip6MnDiscoveryTimeouts"),
        ("MOBILEIPV6-MIB", "mip6MnPrefixSolicitationsSent"),
        ("MOBILEIPV6-MIB", "mip6MnPrefixAdvsRecd"),
        ("MOBILEIPV6-MIB", "mip6MnPrefixAdvsIgnored"),
        ("MOBILEIPV6-MIB", "mip6MnMovedToFN"),
        ("MOBILEIPV6-MIB", "mip6MnMovedToHN"))
)
if mibBuilder.loadTexts:
    mip6MnConfGroup.setStatus("current")

mip6MnRegistrationGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 133, 2, 1, 8)
)
mip6MnRegistrationGroup.setObjects(
      *(("MOBILEIPV6-MIB", "mip6MnBLCOAType"),
        ("MOBILEIPV6-MIB", "mip6MnBLCOA"),
        ("MOBILEIPV6-MIB", "mip6MnBLLifeTimeRequested"),
        ("MOBILEIPV6-MIB", "mip6MnBLLifeTimeGranted"),
        ("MOBILEIPV6-MIB", "mip6MnBLMaxSeq"),
        ("MOBILEIPV6-MIB", "mip6MnBLTimeSent"),
        ("MOBILEIPV6-MIB", "mip6MnBLAccepted"),
        ("MOBILEIPV6-MIB", "mip6MnBLAcceptedTime"),
        ("MOBILEIPV6-MIB", "mip6MnBLRetransmissions"),
        ("MOBILEIPV6-MIB", "mip6MnBLDontSendBUFlag"),
        ("MOBILEIPV6-MIB", "mip6MnMobilityMessagesSent"),
        ("MOBILEIPV6-MIB", "mip6MnMobilityMessagesRecd"),
        ("MOBILEIPV6-MIB", "mip6MnBUsToHA"),
        ("MOBILEIPV6-MIB", "mip6MnBUAcksFromHA"),
        ("MOBILEIPV6-MIB", "mip6MnBUsToCN"),
        ("MOBILEIPV6-MIB", "mip6MnBUAcksFromCN"),
        ("MOBILEIPV6-MIB", "mip6MnBindingErrorsFromCN"),
        ("MOBILEIPV6-MIB", "mip6MnICMPErrorsRecd"),
        ("MOBILEIPV6-MIB", "mip6MnBRRequestsRecd"))
)
if mibBuilder.loadTexts:
    mip6MnRegistrationGroup.setStatus("current")

mip6CnStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 133, 2, 1, 9)
)
mip6CnStatsGroup.setObjects(
      *(("MOBILEIPV6-MIB", "mip6CnBURequestsAccepted"),
        ("MOBILEIPV6-MIB", "mip6CnBURequestsRejected"),
        ("MOBILEIPV6-MIB", "mip6CnBCEntryCreationTime"),
        ("MOBILEIPV6-MIB", "mip6CnBUAcceptedTime"),
        ("MOBILEIPV6-MIB", "mip6CnBURejectionTime"),
        ("MOBILEIPV6-MIB", "mip6CnBURejectionCode"),
        ("MOBILEIPV6-MIB", "mip6CnCtrDiscontinuityTime"))
)
if mibBuilder.loadTexts:
    mip6CnStatsGroup.setStatus("current")

mip6HaSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 133, 2, 1, 10)
)
mip6HaSystemGroup.setObjects(
      *(("MOBILEIPV6-MIB", "mip6HaAdvsRecd"),
        ("MOBILEIPV6-MIB", "mip6HaAdvsSent"),
        ("MOBILEIPV6-MIB", "mip6HaAdvPreference"),
        ("MOBILEIPV6-MIB", "mip6HaAdvLifetime"),
        ("MOBILEIPV6-MIB", "mip6HaPrefixAdv"),
        ("MOBILEIPV6-MIB", "mip6HaPrefixSolicitation"),
        ("MOBILEIPV6-MIB", "mip6HaMCastCtlMsgSupport"))
)
if mibBuilder.loadTexts:
    mip6HaSystemGroup.setStatus("current")

mip6HaListGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 133, 2, 1, 11)
)
mip6HaListGroup.setObjects(
      *(("MOBILEIPV6-MIB", "mip6HaPreference"),
        ("MOBILEIPV6-MIB", "mip6HaRecvLifeTime"),
        ("MOBILEIPV6-MIB", "mip6HaRecvTimeStamp"),
        ("MOBILEIPV6-MIB", "mip6HaGaGlobalAddressType"),
        ("MOBILEIPV6-MIB", "mip6HaGaGlobalAddress"))
)
if mibBuilder.loadTexts:
    mip6HaListGroup.setStatus("current")

mip6HaStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 133, 2, 1, 12)
)
mip6HaStatsGroup.setObjects(
      *(("MOBILEIPV6-MIB", "mip6HaBURequestsAccepted"),
        ("MOBILEIPV6-MIB", "mip6HaBURequestsDenied"),
        ("MOBILEIPV6-MIB", "mip6HaBCEntryCreationTime"),
        ("MOBILEIPV6-MIB", "mip6HaBUAcceptedTime"),
        ("MOBILEIPV6-MIB", "mip6HaBURejectionTime"),
        ("MOBILEIPV6-MIB", "mip6HaRecentBURejectionCode"),
        ("MOBILEIPV6-MIB", "mip6HaCtrDiscontinuityTime"))
)
if mibBuilder.loadTexts:
    mip6HaStatsGroup.setStatus("current")

mip6CnGlobalStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 133, 2, 1, 13)
)
mip6CnGlobalStatsGroup.setObjects(
      *(("MOBILEIPV6-MIB", "mip6CnHomeTestInitsRecd"),
        ("MOBILEIPV6-MIB", "mip6CnHomeTestsSent"),
        ("MOBILEIPV6-MIB", "mip6CnCareOfTestInitsRecd"),
        ("MOBILEIPV6-MIB", "mip6CnCareOfTestsSent"),
        ("MOBILEIPV6-MIB", "mip6CnBUsRecd"),
        ("MOBILEIPV6-MIB", "mip6CnBUAcksSent"),
        ("MOBILEIPV6-MIB", "mip6CnBRsSent"),
        ("MOBILEIPV6-MIB", "mip6CnBindingErrors"),
        ("MOBILEIPV6-MIB", "mip6CnBUsAccepted"),
        ("MOBILEIPV6-MIB", "mip6CnBUsRejected"),
        ("MOBILEIPV6-MIB", "mip6CnReasonUnspecified"),
        ("MOBILEIPV6-MIB", "mip6CnInsufficientResource"),
        ("MOBILEIPV6-MIB", "mip6CnHomeRegnNotSupported"),
        ("MOBILEIPV6-MIB", "mip6CnSeqNumberOutOfWindow"),
        ("MOBILEIPV6-MIB", "mip6CnExpiredHomeNonceIndex"),
        ("MOBILEIPV6-MIB", "mip6CnExpiredCareOfNonceIndex"),
        ("MOBILEIPV6-MIB", "mip6CnExpiredNonce"),
        ("MOBILEIPV6-MIB", "mip6CnRegTypeChangeDisallowed"))
)
if mibBuilder.loadTexts:
    mip6CnGlobalStatsGroup.setStatus("current")

mip6HaGlobalStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 133, 2, 1, 14)
)
mip6HaGlobalStatsGroup.setObjects(
      *(("MOBILEIPV6-MIB", "mip6HaHomeTestInitsRecd"),
        ("MOBILEIPV6-MIB", "mip6HaHomeTestsSent"),
        ("MOBILEIPV6-MIB", "mip6HaBUsRecd"),
        ("MOBILEIPV6-MIB", "mip6HaBUAcksSent"),
        ("MOBILEIPV6-MIB", "mip6HaBRAdviceSent"),
        ("MOBILEIPV6-MIB", "mip6HaBUsAccepted"),
        ("MOBILEIPV6-MIB", "mip6HaPrefDiscoverReqd"),
        ("MOBILEIPV6-MIB", "mip6HaReasonUnspecified"),
        ("MOBILEIPV6-MIB", "mip6HaAdmProhibited"),
        ("MOBILEIPV6-MIB", "mip6HaInsufficientResource"),
        ("MOBILEIPV6-MIB", "mip6HaHomeRegnNotSupported"),
        ("MOBILEIPV6-MIB", "mip6HaNotHomeSubnet"),
        ("MOBILEIPV6-MIB", "mip6HaNotHomeAgentForThisMN"),
        ("MOBILEIPV6-MIB", "mip6HaDupAddrDetectionFailed"),
        ("MOBILEIPV6-MIB", "mip6HaSeqNumberOutOfWindow"),
        ("MOBILEIPV6-MIB", "mip6HaExpiredHomeNonceIndex"),
        ("MOBILEIPV6-MIB", "mip6HaRegTypeChangeDisallowed"))
)
if mibBuilder.loadTexts:
    mip6HaGlobalStatsGroup.setStatus("current")

mip6BindingCacheCtlGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 133, 2, 1, 15)
)
mip6BindingCacheCtlGroup.setObjects(
    ("MOBILEIPV6-MIB", "mip6BindingAdminStatus")
)
if mibBuilder.loadTexts:
    mip6BindingCacheCtlGroup.setStatus("current")


# Notification objects

mip6MnRegistered = NotificationType(
    (1, 3, 6, 1, 2, 1, 133, 0, 1)
)
mip6MnRegistered.setObjects(
      *(("MOBILEIPV6-MIB", "mip6BindingTimeRegistered"),
        ("MOBILEIPV6-MIB", "mip6BindingCOAType"),
        ("MOBILEIPV6-MIB", "mip6BindingCOA"))
)
if mibBuilder.loadTexts:
    mip6MnRegistered.setStatus(
        "current"
    )

mip6MnDeRegistered = NotificationType(
    (1, 3, 6, 1, 2, 1, 133, 0, 2)
)
mip6MnDeRegistered.setObjects(
      *(("MOBILEIPV6-MIB", "mip6BindingTimeRegistered"),
        ("MOBILEIPV6-MIB", "mip6BindingCOAType"),
        ("MOBILEIPV6-MIB", "mip6BindingCOA"))
)
if mibBuilder.loadTexts:
    mip6MnDeRegistered.setStatus(
        "current"
    )

mip6MnCOAChanged = NotificationType(
    (1, 3, 6, 1, 2, 1, 133, 0, 3)
)
mip6MnCOAChanged.setObjects(
      *(("MOBILEIPV6-MIB", "mip6BindingTimeRegistered"),
        ("MOBILEIPV6-MIB", "mip6BindingCOAType"),
        ("MOBILEIPV6-MIB", "mip6BindingCOA"))
)
if mibBuilder.loadTexts:
    mip6MnCOAChanged.setStatus(
        "current"
    )

mip6MnBindingExpiredAtHA = NotificationType(
    (1, 3, 6, 1, 2, 1, 133, 0, 4)
)
mip6MnBindingExpiredAtHA.setObjects(
      *(("MOBILEIPV6-MIB", "mip6BindingTimeRegistered"),
        ("MOBILEIPV6-MIB", "mip6BindingCOAType"),
        ("MOBILEIPV6-MIB", "mip6BindingCOA"))
)
if mibBuilder.loadTexts:
    mip6MnBindingExpiredAtHA.setStatus(
        "current"
    )

mip6MnBindingExpiredAtCN = NotificationType(
    (1, 3, 6, 1, 2, 1, 133, 0, 5)
)
mip6MnBindingExpiredAtCN.setObjects(
      *(("MOBILEIPV6-MIB", "mip6BindingTimeRegistered"),
        ("MOBILEIPV6-MIB", "mip6BindingCOAType"),
        ("MOBILEIPV6-MIB", "mip6BindingCOA"))
)
if mibBuilder.loadTexts:
    mip6MnBindingExpiredAtCN.setStatus(
        "current"
    )


# Notifications groups

mip6NotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 133, 2, 1, 16)
)
mip6NotificationGroup.setObjects(
      *(("MOBILEIPV6-MIB", "mip6MnRegistered"),
        ("MOBILEIPV6-MIB", "mip6MnDeRegistered"),
        ("MOBILEIPV6-MIB", "mip6MnCOAChanged"),
        ("MOBILEIPV6-MIB", "mip6MnBindingExpiredAtHA"),
        ("MOBILEIPV6-MIB", "mip6MnBindingExpiredAtCN"))
)
if mibBuilder.loadTexts:
    mip6NotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

mip6CoreCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 133, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mip6CoreCompliance.setStatus(
        "current"
    )

mip6Compliance2 = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 133, 2, 2, 2)
)
if mibBuilder.loadTexts:
    mip6Compliance2.setStatus(
        "current"
    )

mip6Compliance3 = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 133, 2, 2, 3)
)
if mibBuilder.loadTexts:
    mip6Compliance3.setStatus(
        "current"
    )

mip6CoreReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 133, 2, 2, 4)
)
if mibBuilder.loadTexts:
    mip6CoreReadOnlyCompliance.setStatus(
        "current"
    )

mip6ReadOnlyCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 133, 2, 2, 5)
)
if mibBuilder.loadTexts:
    mip6ReadOnlyCompliance2.setStatus(
        "current"
    )

mip6ReadOnlyCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 133, 2, 2, 6)
)
if mibBuilder.loadTexts:
    mip6ReadOnlyCompliance3.setStatus(
        "current"
    )

mip6MnCoreCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 133, 2, 2, 7)
)
if mibBuilder.loadTexts:
    mip6MnCoreCompliance.setStatus(
        "current"
    )

mip6MnCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 133, 2, 2, 8)
)
if mibBuilder.loadTexts:
    mip6MnCompliance2.setStatus(
        "current"
    )

mip6CnCoreCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 133, 2, 2, 9)
)
if mibBuilder.loadTexts:
    mip6CnCoreCompliance.setStatus(
        "current"
    )

mip6CnCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 133, 2, 2, 10)
)
if mibBuilder.loadTexts:
    mip6CnCompliance.setStatus(
        "current"
    )

mip6HaCoreCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 133, 2, 2, 11)
)
if mibBuilder.loadTexts:
    mip6HaCoreCompliance.setStatus(
        "current"
    )

mip6HaCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 133, 2, 2, 12)
)
if mibBuilder.loadTexts:
    mip6HaCompliance2.setStatus(
        "current"
    )

mip6HaCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 133, 2, 2, 13)
)
if mibBuilder.loadTexts:
    mip6HaCompliance3.setStatus(
        "current"
    )

mip6HaCoreReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 133, 2, 2, 14)
)
if mibBuilder.loadTexts:
    mip6HaCoreReadOnlyCompliance.setStatus(
        "current"
    )

mip6HaReadOnlyCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 133, 2, 2, 15)
)
if mibBuilder.loadTexts:
    mip6HaReadOnlyCompliance2.setStatus(
        "current"
    )

mip6HaReadOnlyCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 133, 2, 2, 16)
)
if mibBuilder.loadTexts:
    mip6HaReadOnlyCompliance3.setStatus(
        "current"
    )

mip6NotificationCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 133, 2, 2, 17)
)
if mibBuilder.loadTexts:
    mip6NotificationCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MOBILEIPV6-MIB",
    **{"Mip6BURequestRejectionCode": Mip6BURequestRejectionCode,
       "mip6MIB": mip6MIB,
       "mip6Notifications": mip6Notifications,
       "mip6MnRegistered": mip6MnRegistered,
       "mip6MnDeRegistered": mip6MnDeRegistered,
       "mip6MnCOAChanged": mip6MnCOAChanged,
       "mip6MnBindingExpiredAtHA": mip6MnBindingExpiredAtHA,
       "mip6MnBindingExpiredAtCN": mip6MnBindingExpiredAtCN,
       "mip6Objects": mip6Objects,
       "mip6Core": mip6Core,
       "mip6System": mip6System,
       "mip6Capabilities": mip6Capabilities,
       "mip6Status": mip6Status,
       "mip6Bindings": mip6Bindings,
       "mip6BindingCacheTable": mip6BindingCacheTable,
       "mip6BindingCacheEntry": mip6BindingCacheEntry,
       "mip6BindingHomeAddressType": mip6BindingHomeAddressType,
       "mip6BindingHomeAddress": mip6BindingHomeAddress,
       "mip6BindingCOAType": mip6BindingCOAType,
       "mip6BindingCOA": mip6BindingCOA,
       "mip6BindingTimeRegistered": mip6BindingTimeRegistered,
       "mip6BindingTimeGranted": mip6BindingTimeGranted,
       "mip6BindingTimeRemaining": mip6BindingTimeRemaining,
       "mip6BindingHomeRegn": mip6BindingHomeRegn,
       "mip6BindingMaxSeq": mip6BindingMaxSeq,
       "mip6BindingUsageTS": mip6BindingUsageTS,
       "mip6BindingUsageCount": mip6BindingUsageCount,
       "mip6BindingAdminStatus": mip6BindingAdminStatus,
       "mip6BindingHistoryTable": mip6BindingHistoryTable,
       "mip6BindingHistoryEntry": mip6BindingHistoryEntry,
       "mip6BindingHstHomeAddressType": mip6BindingHstHomeAddressType,
       "mip6BindingHstHomeAddress": mip6BindingHstHomeAddress,
       "mip6BindingHstIndex": mip6BindingHstIndex,
       "mip6BindingHstCOAType": mip6BindingHstCOAType,
       "mip6BindingHstCOA": mip6BindingHstCOA,
       "mip6BindingHstTimeRegistered": mip6BindingHstTimeRegistered,
       "mip6BindingHstTimeExpired": mip6BindingHstTimeExpired,
       "mip6BindingHstHomeRegn": mip6BindingHstHomeRegn,
       "mip6BindingHstUsageTS": mip6BindingHstUsageTS,
       "mip6BindingHstUsageCount": mip6BindingHstUsageCount,
       "mip6Stats": mip6Stats,
       "mip6TotalTraffic": mip6TotalTraffic,
       "mip6InOctets": mip6InOctets,
       "mip6HCInOctets": mip6HCInOctets,
       "mip6InPkts": mip6InPkts,
       "mip6HCInPkts": mip6HCInPkts,
       "mip6OutOctets": mip6OutOctets,
       "mip6HCOutOctets": mip6HCOutOctets,
       "mip6OutPkts": mip6OutPkts,
       "mip6HCOutPkts": mip6HCOutPkts,
       "mip6CounterDiscontinuityTime": mip6CounterDiscontinuityTime,
       "mip6NodeTrafficTable": mip6NodeTrafficTable,
       "mip6NodeTrafficEntry": mip6NodeTrafficEntry,
       "mip6NodeInOctets": mip6NodeInOctets,
       "mip6HCNodeInOctets": mip6HCNodeInOctets,
       "mip6NodeInPkts": mip6NodeInPkts,
       "mip6HCNodeInPkts": mip6HCNodeInPkts,
       "mip6NodeOutOctets": mip6NodeOutOctets,
       "mip6HCNodeOutOctets": mip6HCNodeOutOctets,
       "mip6NodeOutPkts": mip6NodeOutPkts,
       "mip6HCNodeOutPkts": mip6HCNodeOutPkts,
       "mip6NodeCtrDiscontinuityTime": mip6NodeCtrDiscontinuityTime,
       "mip6Mn": mip6Mn,
       "mip6MnSystem": mip6MnSystem,
       "mip6MnHomeAddressTable": mip6MnHomeAddressTable,
       "mip6MnHomeAddressEntry": mip6MnHomeAddressEntry,
       "mip6MnHomeAddressType": mip6MnHomeAddressType,
       "mip6MnHomeAddress": mip6MnHomeAddress,
       "mip6MnHomeAddressState": mip6MnHomeAddressState,
       "mip6MnConf": mip6MnConf,
       "mip6MnDiscoveryRequests": mip6MnDiscoveryRequests,
       "mip6MnDiscoveryReplies": mip6MnDiscoveryReplies,
       "mip6MnDiscoveryTimeouts": mip6MnDiscoveryTimeouts,
       "mip6MnPrefixSolicitationsSent": mip6MnPrefixSolicitationsSent,
       "mip6MnPrefixAdvsRecd": mip6MnPrefixAdvsRecd,
       "mip6MnPrefixAdvsIgnored": mip6MnPrefixAdvsIgnored,
       "mip6MnMovedToFN": mip6MnMovedToFN,
       "mip6MnMovedToHN": mip6MnMovedToHN,
       "mip6MnRegistration": mip6MnRegistration,
       "mip6MnBLTable": mip6MnBLTable,
       "mip6MnBLEntry": mip6MnBLEntry,
       "mip6MnBLNodeAddressType": mip6MnBLNodeAddressType,
       "mip6MnBLNodeAddress": mip6MnBLNodeAddress,
       "mip6MnBLCOAType": mip6MnBLCOAType,
       "mip6MnBLCOA": mip6MnBLCOA,
       "mip6MnBLLifeTimeRequested": mip6MnBLLifeTimeRequested,
       "mip6MnBLLifeTimeGranted": mip6MnBLLifeTimeGranted,
       "mip6MnBLMaxSeq": mip6MnBLMaxSeq,
       "mip6MnBLTimeSent": mip6MnBLTimeSent,
       "mip6MnBLAccepted": mip6MnBLAccepted,
       "mip6MnBLAcceptedTime": mip6MnBLAcceptedTime,
       "mip6MnBLRetransmissions": mip6MnBLRetransmissions,
       "mip6MnBLDontSendBUFlag": mip6MnBLDontSendBUFlag,
       "mip6MnRegnCounters": mip6MnRegnCounters,
       "mip6MnMobilityMessagesSent": mip6MnMobilityMessagesSent,
       "mip6MnMobilityMessagesRecd": mip6MnMobilityMessagesRecd,
       "mip6MnBUsToHA": mip6MnBUsToHA,
       "mip6MnBUAcksFromHA": mip6MnBUAcksFromHA,
       "mip6MnBUsToCN": mip6MnBUsToCN,
       "mip6MnBUAcksFromCN": mip6MnBUAcksFromCN,
       "mip6MnBindingErrorsFromCN": mip6MnBindingErrorsFromCN,
       "mip6MnICMPErrorsRecd": mip6MnICMPErrorsRecd,
       "mip6MnBRRequestsRecd": mip6MnBRRequestsRecd,
       "mip6Cn": mip6Cn,
       "mip6CnSystem": mip6CnSystem,
       "mip6CnStats": mip6CnStats,
       "mip6CnGlobalStats": mip6CnGlobalStats,
       "mip6CnHomeTestInitsRecd": mip6CnHomeTestInitsRecd,
       "mip6CnHomeTestsSent": mip6CnHomeTestsSent,
       "mip6CnCareOfTestInitsRecd": mip6CnCareOfTestInitsRecd,
       "mip6CnCareOfTestsSent": mip6CnCareOfTestsSent,
       "mip6CnBUsRecd": mip6CnBUsRecd,
       "mip6CnBUAcksSent": mip6CnBUAcksSent,
       "mip6CnBRsSent": mip6CnBRsSent,
       "mip6CnBindingErrors": mip6CnBindingErrors,
       "mip6CnBUsAccepted": mip6CnBUsAccepted,
       "mip6CnBUsRejected": mip6CnBUsRejected,
       "mip6CnReasonUnspecified": mip6CnReasonUnspecified,
       "mip6CnInsufficientResource": mip6CnInsufficientResource,
       "mip6CnHomeRegnNotSupported": mip6CnHomeRegnNotSupported,
       "mip6CnSeqNumberOutOfWindow": mip6CnSeqNumberOutOfWindow,
       "mip6CnExpiredHomeNonceIndex": mip6CnExpiredHomeNonceIndex,
       "mip6CnExpiredCareOfNonceIndex": mip6CnExpiredCareOfNonceIndex,
       "mip6CnExpiredNonce": mip6CnExpiredNonce,
       "mip6CnRegTypeChangeDisallowed": mip6CnRegTypeChangeDisallowed,
       "mip6CnCounterTable": mip6CnCounterTable,
       "mip6CnCounterEntry": mip6CnCounterEntry,
       "mip6CnBURequestsAccepted": mip6CnBURequestsAccepted,
       "mip6CnBURequestsRejected": mip6CnBURequestsRejected,
       "mip6CnBCEntryCreationTime": mip6CnBCEntryCreationTime,
       "mip6CnBUAcceptedTime": mip6CnBUAcceptedTime,
       "mip6CnBURejectionTime": mip6CnBURejectionTime,
       "mip6CnBURejectionCode": mip6CnBURejectionCode,
       "mip6CnCtrDiscontinuityTime": mip6CnCtrDiscontinuityTime,
       "mip6Ha": mip6Ha,
       "mip6HaAdvertisement": mip6HaAdvertisement,
       "mip6HaAdvsRecd": mip6HaAdvsRecd,
       "mip6HaAdvsSent": mip6HaAdvsSent,
       "mip6HaConfTable": mip6HaConfTable,
       "mip6HaConfEntry": mip6HaConfEntry,
       "mip6HaAdvPreference": mip6HaAdvPreference,
       "mip6HaAdvLifetime": mip6HaAdvLifetime,
       "mip6HaPrefixAdv": mip6HaPrefixAdv,
       "mip6HaPrefixSolicitation": mip6HaPrefixSolicitation,
       "mip6HaMCastCtlMsgSupport": mip6HaMCastCtlMsgSupport,
       "mip6HaListTable": mip6HaListTable,
       "mip6HaListEntry": mip6HaListEntry,
       "mip6HaLinkLocalAddressType": mip6HaLinkLocalAddressType,
       "mip6HaLinkLocalAddress": mip6HaLinkLocalAddress,
       "mip6HaPreference": mip6HaPreference,
       "mip6HaRecvLifeTime": mip6HaRecvLifeTime,
       "mip6HaRecvTimeStamp": mip6HaRecvTimeStamp,
       "mip6HaGlAddrTable": mip6HaGlAddrTable,
       "mip6HaGlAddrEntry": mip6HaGlAddrEntry,
       "mip6HaGaAddrSeqNo": mip6HaGaAddrSeqNo,
       "mip6HaGaGlobalAddressType": mip6HaGaGlobalAddressType,
       "mip6HaGaGlobalAddress": mip6HaGaGlobalAddress,
       "mip6HaStats": mip6HaStats,
       "mip6HaGlobalStats": mip6HaGlobalStats,
       "mip6HaHomeTestInitsRecd": mip6HaHomeTestInitsRecd,
       "mip6HaHomeTestsSent": mip6HaHomeTestsSent,
       "mip6HaBUsRecd": mip6HaBUsRecd,
       "mip6HaBUAcksSent": mip6HaBUAcksSent,
       "mip6HaBRAdviceSent": mip6HaBRAdviceSent,
       "mip6HaBUsAccepted": mip6HaBUsAccepted,
       "mip6HaPrefDiscoverReqd": mip6HaPrefDiscoverReqd,
       "mip6HaReasonUnspecified": mip6HaReasonUnspecified,
       "mip6HaAdmProhibited": mip6HaAdmProhibited,
       "mip6HaInsufficientResource": mip6HaInsufficientResource,
       "mip6HaHomeRegnNotSupported": mip6HaHomeRegnNotSupported,
       "mip6HaNotHomeSubnet": mip6HaNotHomeSubnet,
       "mip6HaNotHomeAgentForThisMN": mip6HaNotHomeAgentForThisMN,
       "mip6HaDupAddrDetectionFailed": mip6HaDupAddrDetectionFailed,
       "mip6HaSeqNumberOutOfWindow": mip6HaSeqNumberOutOfWindow,
       "mip6HaExpiredHomeNonceIndex": mip6HaExpiredHomeNonceIndex,
       "mip6HaRegTypeChangeDisallowed": mip6HaRegTypeChangeDisallowed,
       "mip6HaCounterTable": mip6HaCounterTable,
       "mip6HaCounterEntry": mip6HaCounterEntry,
       "mip6HaBURequestsAccepted": mip6HaBURequestsAccepted,
       "mip6HaBURequestsDenied": mip6HaBURequestsDenied,
       "mip6HaBCEntryCreationTime": mip6HaBCEntryCreationTime,
       "mip6HaBUAcceptedTime": mip6HaBUAcceptedTime,
       "mip6HaBURejectionTime": mip6HaBURejectionTime,
       "mip6HaRecentBURejectionCode": mip6HaRecentBURejectionCode,
       "mip6HaCtrDiscontinuityTime": mip6HaCtrDiscontinuityTime,
       "mip6Conformance": mip6Conformance,
       "mip6Groups": mip6Groups,
       "mip6SystemGroup": mip6SystemGroup,
       "mip6BindingCacheGroup": mip6BindingCacheGroup,
       "mip6BindingHstGroup": mip6BindingHstGroup,
       "mip6TotalTrafficGroup": mip6TotalTrafficGroup,
       "mip6NodeTrafficGroup": mip6NodeTrafficGroup,
       "mip6MnSystemGroup": mip6MnSystemGroup,
       "mip6MnConfGroup": mip6MnConfGroup,
       "mip6MnRegistrationGroup": mip6MnRegistrationGroup,
       "mip6CnStatsGroup": mip6CnStatsGroup,
       "mip6HaSystemGroup": mip6HaSystemGroup,
       "mip6HaListGroup": mip6HaListGroup,
       "mip6HaStatsGroup": mip6HaStatsGroup,
       "mip6CnGlobalStatsGroup": mip6CnGlobalStatsGroup,
       "mip6HaGlobalStatsGroup": mip6HaGlobalStatsGroup,
       "mip6BindingCacheCtlGroup": mip6BindingCacheCtlGroup,
       "mip6NotificationGroup": mip6NotificationGroup,
       "mip6Compliances": mip6Compliances,
       "mip6CoreCompliance": mip6CoreCompliance,
       "mip6Compliance2": mip6Compliance2,
       "mip6Compliance3": mip6Compliance3,
       "mip6CoreReadOnlyCompliance": mip6CoreReadOnlyCompliance,
       "mip6ReadOnlyCompliance2": mip6ReadOnlyCompliance2,
       "mip6ReadOnlyCompliance3": mip6ReadOnlyCompliance3,
       "mip6MnCoreCompliance": mip6MnCoreCompliance,
       "mip6MnCompliance2": mip6MnCompliance2,
       "mip6CnCoreCompliance": mip6CnCoreCompliance,
       "mip6CnCompliance": mip6CnCompliance,
       "mip6HaCoreCompliance": mip6HaCoreCompliance,
       "mip6HaCompliance2": mip6HaCompliance2,
       "mip6HaCompliance3": mip6HaCompliance3,
       "mip6HaCoreReadOnlyCompliance": mip6HaCoreReadOnlyCompliance,
       "mip6HaReadOnlyCompliance2": mip6HaReadOnlyCompliance2,
       "mip6HaReadOnlyCompliance3": mip6HaReadOnlyCompliance3,
       "mip6NotificationCompliance": mip6NotificationCompliance}
)
