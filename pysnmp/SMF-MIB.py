# SNMP MIB module (SMF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SMF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:55:35 2024
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

(IANAsmfOpModeIdTC,
 IANAsmfRssaIdTC) = mibBuilder.importSymbols(
    "IANA-SMF-MIB",
    "IANAsmfOpModeIdTC",
    "IANAsmfRssaIdTC")

(InterfaceIndexOrZero,
 ifName) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifName")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

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
 experimental,
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
    "experimental",
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

smfMIB = ModuleIdentity(
    (1, 3, 6, 1, 3, 126)
)
smfMIB.setRevisions(
        ("2014-10-10 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SmfStatus(Integer32, TextualConvention):
    status = "current"
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



# MIB Managed Objects in the order of their OIDs

_SmfMIBNotifications_ObjectIdentity = ObjectIdentity
smfMIBNotifications = _SmfMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 3, 126, 0)
)
_SmfMIBNotifObjects_ObjectIdentity = ObjectIdentity
smfMIBNotifObjects = _SmfMIBNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 3, 126, 0, 0)
)
_SmfMIBNotifControl_ObjectIdentity = ObjectIdentity
smfMIBNotifControl = _SmfMIBNotifControl_ObjectIdentity(
    (1, 3, 6, 1, 3, 126, 0, 1)
)


class _SmfNotifDpdMemoryOverflowThreshold_Type(Integer32):
    """Custom type smfNotifDpdMemoryOverflowThreshold based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SmfNotifDpdMemoryOverflowThreshold_Type.__name__ = "Integer32"
_SmfNotifDpdMemoryOverflowThreshold_Object = MibScalar
smfNotifDpdMemoryOverflowThreshold = _SmfNotifDpdMemoryOverflowThreshold_Object(
    (1, 3, 6, 1, 3, 126, 0, 1, 1),
    _SmfNotifDpdMemoryOverflowThreshold_Type()
)
smfNotifDpdMemoryOverflowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smfNotifDpdMemoryOverflowThreshold.setStatus("current")
if mibBuilder.loadTexts:
    smfNotifDpdMemoryOverflowThreshold.setUnits("Events")


class _SmfNotifDpdMemoryOverflowWindow_Type(TimeTicks):
    """Custom type smfNotifDpdMemoryOverflowWindow based on TimeTicks"""
    defaultValue = 1


_SmfNotifDpdMemoryOverflowWindow_Object = MibScalar
smfNotifDpdMemoryOverflowWindow = _SmfNotifDpdMemoryOverflowWindow_Object(
    (1, 3, 6, 1, 3, 126, 0, 1, 2),
    _SmfNotifDpdMemoryOverflowWindow_Type()
)
smfNotifDpdMemoryOverflowWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smfNotifDpdMemoryOverflowWindow.setStatus("current")
_SmfMIBObjects_ObjectIdentity = ObjectIdentity
smfMIBObjects = _SmfMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 3, 126, 1)
)
_SmfCapabilitiesGroup_ObjectIdentity = ObjectIdentity
smfCapabilitiesGroup = _SmfCapabilitiesGroup_ObjectIdentity(
    (1, 3, 6, 1, 3, 126, 1, 1)
)
_SmfCapabilitiesTable_Object = MibTable
smfCapabilitiesTable = _SmfCapabilitiesTable_Object(
    (1, 3, 6, 1, 3, 126, 1, 1, 1)
)
if mibBuilder.loadTexts:
    smfCapabilitiesTable.setStatus("current")
_SmfCapabilitiesEntry_Object = MibTableRow
smfCapabilitiesEntry = _SmfCapabilitiesEntry_Object(
    (1, 3, 6, 1, 3, 126, 1, 1, 1, 1)
)
smfCapabilitiesEntry.setIndexNames(
    (0, "SMF-MIB", "smfCapabilitiesIndex"),
)
if mibBuilder.loadTexts:
    smfCapabilitiesEntry.setStatus("current")


class _SmfCapabilitiesIndex_Type(Integer32):
    """Custom type smfCapabilitiesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SmfCapabilitiesIndex_Type.__name__ = "Integer32"
_SmfCapabilitiesIndex_Object = MibTableColumn
smfCapabilitiesIndex = _SmfCapabilitiesIndex_Object(
    (1, 3, 6, 1, 3, 126, 1, 1, 1, 1, 1),
    _SmfCapabilitiesIndex_Type()
)
smfCapabilitiesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    smfCapabilitiesIndex.setStatus("current")
_SmfCapabilitiesOpModeID_Type = IANAsmfOpModeIdTC
_SmfCapabilitiesOpModeID_Object = MibTableColumn
smfCapabilitiesOpModeID = _SmfCapabilitiesOpModeID_Object(
    (1, 3, 6, 1, 3, 126, 1, 1, 1, 1, 2),
    _SmfCapabilitiesOpModeID_Type()
)
smfCapabilitiesOpModeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smfCapabilitiesOpModeID.setStatus("current")
_SmfCapabilitiesRssaID_Type = IANAsmfRssaIdTC
_SmfCapabilitiesRssaID_Object = MibTableColumn
smfCapabilitiesRssaID = _SmfCapabilitiesRssaID_Object(
    (1, 3, 6, 1, 3, 126, 1, 1, 1, 1, 3),
    _SmfCapabilitiesRssaID_Type()
)
smfCapabilitiesRssaID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smfCapabilitiesRssaID.setStatus("current")
_SmfConfigurationGroup_ObjectIdentity = ObjectIdentity
smfConfigurationGroup = _SmfConfigurationGroup_ObjectIdentity(
    (1, 3, 6, 1, 3, 126, 1, 2)
)


class _SmfCfgAdminStatus_Type(SmfStatus):
    """Custom type smfCfgAdminStatus based on SmfStatus"""


_SmfCfgAdminStatus_Object = MibScalar
smfCfgAdminStatus = _SmfCfgAdminStatus_Object(
    (1, 3, 6, 1, 3, 126, 1, 2, 1),
    _SmfCfgAdminStatus_Type()
)
smfCfgAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smfCfgAdminStatus.setStatus("current")
_SmfCfgSmfSysUpTime_Type = TimeTicks
_SmfCfgSmfSysUpTime_Object = MibScalar
smfCfgSmfSysUpTime = _SmfCfgSmfSysUpTime_Object(
    (1, 3, 6, 1, 3, 126, 1, 2, 2),
    _SmfCfgSmfSysUpTime_Type()
)
smfCfgSmfSysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smfCfgSmfSysUpTime.setStatus("current")


class _SmfCfgRouterIDAddrType_Type(InetAddressType):
    """Custom type smfCfgRouterIDAddrType based on InetAddressType"""
    defaultValue = 1

    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_SmfCfgRouterIDAddrType_Type.__name__ = "InetAddressType"
_SmfCfgRouterIDAddrType_Object = MibScalar
smfCfgRouterIDAddrType = _SmfCfgRouterIDAddrType_Object(
    (1, 3, 6, 1, 3, 126, 1, 2, 3),
    _SmfCfgRouterIDAddrType_Type()
)
smfCfgRouterIDAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smfCfgRouterIDAddrType.setStatus("current")


class _SmfCfgRouterID_Type(InetAddress):
    """Custom type smfCfgRouterID based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_SmfCfgRouterID_Type.__name__ = "InetAddress"
_SmfCfgRouterID_Object = MibScalar
smfCfgRouterID = _SmfCfgRouterID_Object(
    (1, 3, 6, 1, 3, 126, 1, 2, 4),
    _SmfCfgRouterID_Type()
)
smfCfgRouterID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smfCfgRouterID.setStatus("current")


class _SmfCfgOperationalMode_Type(Integer32):
    """Custom type smfCfgOperationalMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SmfCfgOperationalMode_Type.__name__ = "Integer32"
_SmfCfgOperationalMode_Object = MibScalar
smfCfgOperationalMode = _SmfCfgOperationalMode_Object(
    (1, 3, 6, 1, 3, 126, 1, 2, 5),
    _SmfCfgOperationalMode_Type()
)
smfCfgOperationalMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smfCfgOperationalMode.setStatus("current")


class _SmfCfgRssaMember_Type(Integer32):
    """Custom type smfCfgRssaMember based on Integer32"""
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
        *(("always", 2),
          ("never", 3),
          ("potential", 1))
    )


_SmfCfgRssaMember_Type.__name__ = "Integer32"
_SmfCfgRssaMember_Object = MibScalar
smfCfgRssaMember = _SmfCfgRssaMember_Object(
    (1, 3, 6, 1, 3, 126, 1, 2, 6),
    _SmfCfgRssaMember_Type()
)
smfCfgRssaMember.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smfCfgRssaMember.setStatus("current")


class _SmfCfgIpv4Dpd_Type(Integer32):
    """Custom type smfCfgIpv4Dpd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hashBased", 1),
          ("identificationBased", 2))
    )


_SmfCfgIpv4Dpd_Type.__name__ = "Integer32"
_SmfCfgIpv4Dpd_Object = MibScalar
smfCfgIpv4Dpd = _SmfCfgIpv4Dpd_Object(
    (1, 3, 6, 1, 3, 126, 1, 2, 7),
    _SmfCfgIpv4Dpd_Type()
)
smfCfgIpv4Dpd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smfCfgIpv4Dpd.setStatus("current")


class _SmfCfgIpv6Dpd_Type(Integer32):
    """Custom type smfCfgIpv6Dpd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hashBased", 1),
          ("identificationBased", 2))
    )


_SmfCfgIpv6Dpd_Type.__name__ = "Integer32"
_SmfCfgIpv6Dpd_Object = MibScalar
smfCfgIpv6Dpd = _SmfCfgIpv6Dpd_Object(
    (1, 3, 6, 1, 3, 126, 1, 2, 8),
    _SmfCfgIpv6Dpd_Type()
)
smfCfgIpv6Dpd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smfCfgIpv6Dpd.setStatus("current")


class _SmfCfgMaxPktLifetime_Type(Integer32):
    """Custom type smfCfgMaxPktLifetime based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SmfCfgMaxPktLifetime_Type.__name__ = "Integer32"
_SmfCfgMaxPktLifetime_Object = MibScalar
smfCfgMaxPktLifetime = _SmfCfgMaxPktLifetime_Object(
    (1, 3, 6, 1, 3, 126, 1, 2, 9),
    _SmfCfgMaxPktLifetime_Type()
)
smfCfgMaxPktLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smfCfgMaxPktLifetime.setStatus("current")
if mibBuilder.loadTexts:
    smfCfgMaxPktLifetime.setUnits("Seconds")


class _SmfCfgDpdEntryMaxLifetime_Type(Integer32):
    """Custom type smfCfgDpdEntryMaxLifetime based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65525),
    )


_SmfCfgDpdEntryMaxLifetime_Type.__name__ = "Integer32"
_SmfCfgDpdEntryMaxLifetime_Object = MibScalar
smfCfgDpdEntryMaxLifetime = _SmfCfgDpdEntryMaxLifetime_Object(
    (1, 3, 6, 1, 3, 126, 1, 2, 10),
    _SmfCfgDpdEntryMaxLifetime_Type()
)
smfCfgDpdEntryMaxLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smfCfgDpdEntryMaxLifetime.setStatus("current")
if mibBuilder.loadTexts:
    smfCfgDpdEntryMaxLifetime.setUnits("Seconds")


class _SmfCfgNhdpRssaMesgTLVIncluded_Type(TruthValue):
    """Custom type smfCfgNhdpRssaMesgTLVIncluded based on TruthValue"""


_SmfCfgNhdpRssaMesgTLVIncluded_Object = MibScalar
smfCfgNhdpRssaMesgTLVIncluded = _SmfCfgNhdpRssaMesgTLVIncluded_Object(
    (1, 3, 6, 1, 3, 126, 1, 2, 11),
    _SmfCfgNhdpRssaMesgTLVIncluded_Type()
)
smfCfgNhdpRssaMesgTLVIncluded.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smfCfgNhdpRssaMesgTLVIncluded.setStatus("current")


class _SmfCfgNhdpRssaAddrBlockTLVIncluded_Type(TruthValue):
    """Custom type smfCfgNhdpRssaAddrBlockTLVIncluded based on TruthValue"""


_SmfCfgNhdpRssaAddrBlockTLVIncluded_Object = MibScalar
smfCfgNhdpRssaAddrBlockTLVIncluded = _SmfCfgNhdpRssaAddrBlockTLVIncluded_Object(
    (1, 3, 6, 1, 3, 126, 1, 2, 12),
    _SmfCfgNhdpRssaAddrBlockTLVIncluded_Type()
)
smfCfgNhdpRssaAddrBlockTLVIncluded.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smfCfgNhdpRssaAddrBlockTLVIncluded.setStatus("current")
_SmfCfgAddrForwardingTable_Object = MibTable
smfCfgAddrForwardingTable = _SmfCfgAddrForwardingTable_Object(
    (1, 3, 6, 1, 3, 126, 1, 2, 13)
)
if mibBuilder.loadTexts:
    smfCfgAddrForwardingTable.setStatus("current")
_SmfCfgAddrForwardingEntry_Object = MibTableRow
smfCfgAddrForwardingEntry = _SmfCfgAddrForwardingEntry_Object(
    (1, 3, 6, 1, 3, 126, 1, 2, 13, 1)
)
smfCfgAddrForwardingEntry.setIndexNames(
    (0, "SMF-MIB", "smfCfgAddrForwardingIndex"),
)
if mibBuilder.loadTexts:
    smfCfgAddrForwardingEntry.setStatus("current")


class _SmfCfgAddrForwardingIndex_Type(Integer32):
    """Custom type smfCfgAddrForwardingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SmfCfgAddrForwardingIndex_Type.__name__ = "Integer32"
_SmfCfgAddrForwardingIndex_Object = MibTableColumn
smfCfgAddrForwardingIndex = _SmfCfgAddrForwardingIndex_Object(
    (1, 3, 6, 1, 3, 126, 1, 2, 13, 1, 1),
    _SmfCfgAddrForwardingIndex_Type()
)
smfCfgAddrForwardingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    smfCfgAddrForwardingIndex.setStatus("current")
_SmfCfgAddrForwardingGroupName_Type = SnmpAdminString
_SmfCfgAddrForwardingGroupName_Object = MibTableColumn
smfCfgAddrForwardingGroupName = _SmfCfgAddrForwardingGroupName_Object(
    (1, 3, 6, 1, 3, 126, 1, 2, 13, 1, 2),
    _SmfCfgAddrForwardingGroupName_Type()
)
smfCfgAddrForwardingGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    smfCfgAddrForwardingGroupName.setStatus("current")


class _SmfCfgAddrForwardingAddrType_Type(InetAddressType):
    """Custom type smfCfgAddrForwardingAddrType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_SmfCfgAddrForwardingAddrType_Type.__name__ = "InetAddressType"
_SmfCfgAddrForwardingAddrType_Object = MibTableColumn
smfCfgAddrForwardingAddrType = _SmfCfgAddrForwardingAddrType_Object(
    (1, 3, 6, 1, 3, 126, 1, 2, 13, 1, 3),
    _SmfCfgAddrForwardingAddrType_Type()
)
smfCfgAddrForwardingAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    smfCfgAddrForwardingAddrType.setStatus("current")


class _SmfCfgAddrForwardingAddress_Type(InetAddress):
    """Custom type smfCfgAddrForwardingAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_SmfCfgAddrForwardingAddress_Type.__name__ = "InetAddress"
_SmfCfgAddrForwardingAddress_Object = MibTableColumn
smfCfgAddrForwardingAddress = _SmfCfgAddrForwardingAddress_Object(
    (1, 3, 6, 1, 3, 126, 1, 2, 13, 1, 4),
    _SmfCfgAddrForwardingAddress_Type()
)
smfCfgAddrForwardingAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    smfCfgAddrForwardingAddress.setStatus("current")
_SmfCfgAddrForwardingAddrPrefixLength_Type = InetAddressPrefixLength
_SmfCfgAddrForwardingAddrPrefixLength_Object = MibTableColumn
smfCfgAddrForwardingAddrPrefixLength = _SmfCfgAddrForwardingAddrPrefixLength_Object(
    (1, 3, 6, 1, 3, 126, 1, 2, 13, 1, 5),
    _SmfCfgAddrForwardingAddrPrefixLength_Type()
)
smfCfgAddrForwardingAddrPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    smfCfgAddrForwardingAddrPrefixLength.setStatus("current")
_SmfCfgAddrForwardingStatus_Type = RowStatus
_SmfCfgAddrForwardingStatus_Object = MibTableColumn
smfCfgAddrForwardingStatus = _SmfCfgAddrForwardingStatus_Object(
    (1, 3, 6, 1, 3, 126, 1, 2, 13, 1, 6),
    _SmfCfgAddrForwardingStatus_Type()
)
smfCfgAddrForwardingStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    smfCfgAddrForwardingStatus.setStatus("current")
_SmfCfgInterfaceTable_Object = MibTable
smfCfgInterfaceTable = _SmfCfgInterfaceTable_Object(
    (1, 3, 6, 1, 3, 126, 1, 2, 14)
)
if mibBuilder.loadTexts:
    smfCfgInterfaceTable.setStatus("current")
_SmfCfgInterfaceEntry_Object = MibTableRow
smfCfgInterfaceEntry = _SmfCfgInterfaceEntry_Object(
    (1, 3, 6, 1, 3, 126, 1, 2, 14, 1)
)
smfCfgInterfaceEntry.setIndexNames(
    (0, "SMF-MIB", "smfCfgIfIndex"),
)
if mibBuilder.loadTexts:
    smfCfgInterfaceEntry.setStatus("current")
_SmfCfgIfIndex_Type = InterfaceIndexOrZero
_SmfCfgIfIndex_Object = MibTableColumn
smfCfgIfIndex = _SmfCfgIfIndex_Object(
    (1, 3, 6, 1, 3, 126, 1, 2, 14, 1, 1),
    _SmfCfgIfIndex_Type()
)
smfCfgIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    smfCfgIfIndex.setStatus("current")


class _SmfCfgIfAdminStatus_Type(SmfStatus):
    """Custom type smfCfgIfAdminStatus based on SmfStatus"""


_SmfCfgIfAdminStatus_Object = MibTableColumn
smfCfgIfAdminStatus = _SmfCfgIfAdminStatus_Object(
    (1, 3, 6, 1, 3, 126, 1, 2, 14, 1, 2),
    _SmfCfgIfAdminStatus_Type()
)
smfCfgIfAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    smfCfgIfAdminStatus.setStatus("current")
_SmfCfgIfSmfUpTime_Type = TimeTicks
_SmfCfgIfSmfUpTime_Object = MibTableColumn
smfCfgIfSmfUpTime = _SmfCfgIfSmfUpTime_Object(
    (1, 3, 6, 1, 3, 126, 1, 2, 14, 1, 3),
    _SmfCfgIfSmfUpTime_Type()
)
smfCfgIfSmfUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smfCfgIfSmfUpTime.setStatus("current")
_SmfCfgIfRowStatus_Type = RowStatus
_SmfCfgIfRowStatus_Object = MibTableColumn
smfCfgIfRowStatus = _SmfCfgIfRowStatus_Object(
    (1, 3, 6, 1, 3, 126, 1, 2, 14, 1, 4),
    _SmfCfgIfRowStatus_Type()
)
smfCfgIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    smfCfgIfRowStatus.setStatus("current")
_SmfStateGroup_ObjectIdentity = ObjectIdentity
smfStateGroup = _SmfStateGroup_ObjectIdentity(
    (1, 3, 6, 1, 3, 126, 1, 3)
)
_SmfStateNodeRsStatusIncluded_Type = TruthValue
_SmfStateNodeRsStatusIncluded_Object = MibScalar
smfStateNodeRsStatusIncluded = _SmfStateNodeRsStatusIncluded_Object(
    (1, 3, 6, 1, 3, 126, 1, 3, 1),
    _SmfStateNodeRsStatusIncluded_Type()
)
smfStateNodeRsStatusIncluded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smfStateNodeRsStatusIncluded.setStatus("current")
_SmfStateDpdMemoryOverflow_Type = Counter32
_SmfStateDpdMemoryOverflow_Object = MibScalar
smfStateDpdMemoryOverflow = _SmfStateDpdMemoryOverflow_Object(
    (1, 3, 6, 1, 3, 126, 1, 3, 2),
    _SmfStateDpdMemoryOverflow_Type()
)
smfStateDpdMemoryOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smfStateDpdMemoryOverflow.setStatus("current")
if mibBuilder.loadTexts:
    smfStateDpdMemoryOverflow.setUnits("DPD Records")
_SmfStateNeighborTable_Object = MibTable
smfStateNeighborTable = _SmfStateNeighborTable_Object(
    (1, 3, 6, 1, 3, 126, 1, 3, 3)
)
if mibBuilder.loadTexts:
    smfStateNeighborTable.setStatus("current")
_SmfStateNeighborEntry_Object = MibTableRow
smfStateNeighborEntry = _SmfStateNeighborEntry_Object(
    (1, 3, 6, 1, 3, 126, 1, 3, 3, 1)
)
smfStateNeighborEntry.setIndexNames(
    (0, "SMF-MIB", "smfStateNeighborIpAddrType"),
    (0, "SMF-MIB", "smfStateNeighborIpAddr"),
    (0, "SMF-MIB", "smfStateNeighborPrefixLen"),
)
if mibBuilder.loadTexts:
    smfStateNeighborEntry.setStatus("current")


class _SmfStateNeighborIpAddrType_Type(InetAddressType):
    """Custom type smfStateNeighborIpAddrType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_SmfStateNeighborIpAddrType_Type.__name__ = "InetAddressType"
_SmfStateNeighborIpAddrType_Object = MibTableColumn
smfStateNeighborIpAddrType = _SmfStateNeighborIpAddrType_Object(
    (1, 3, 6, 1, 3, 126, 1, 3, 3, 1, 1),
    _SmfStateNeighborIpAddrType_Type()
)
smfStateNeighborIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    smfStateNeighborIpAddrType.setStatus("current")


class _SmfStateNeighborIpAddr_Type(InetAddress):
    """Custom type smfStateNeighborIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_SmfStateNeighborIpAddr_Type.__name__ = "InetAddress"
_SmfStateNeighborIpAddr_Object = MibTableColumn
smfStateNeighborIpAddr = _SmfStateNeighborIpAddr_Object(
    (1, 3, 6, 1, 3, 126, 1, 3, 3, 1, 2),
    _SmfStateNeighborIpAddr_Type()
)
smfStateNeighborIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    smfStateNeighborIpAddr.setStatus("current")
_SmfStateNeighborPrefixLen_Type = InetAddressPrefixLength
_SmfStateNeighborPrefixLen_Object = MibTableColumn
smfStateNeighborPrefixLen = _SmfStateNeighborPrefixLen_Object(
    (1, 3, 6, 1, 3, 126, 1, 3, 3, 1, 3),
    _SmfStateNeighborPrefixLen_Type()
)
smfStateNeighborPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    smfStateNeighborPrefixLen.setStatus("current")
if mibBuilder.loadTexts:
    smfStateNeighborPrefixLen.setUnits("bits")
_SmfStateNeighborRSSA_Type = IANAsmfRssaIdTC
_SmfStateNeighborRSSA_Object = MibTableColumn
smfStateNeighborRSSA = _SmfStateNeighborRSSA_Object(
    (1, 3, 6, 1, 3, 126, 1, 3, 3, 1, 4),
    _SmfStateNeighborRSSA_Type()
)
smfStateNeighborRSSA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smfStateNeighborRSSA.setStatus("current")
_SmfStateNeighborNextHopInterface_Type = InterfaceIndexOrZero
_SmfStateNeighborNextHopInterface_Object = MibTableColumn
smfStateNeighborNextHopInterface = _SmfStateNeighborNextHopInterface_Object(
    (1, 3, 6, 1, 3, 126, 1, 3, 3, 1, 6),
    _SmfStateNeighborNextHopInterface_Type()
)
smfStateNeighborNextHopInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smfStateNeighborNextHopInterface.setStatus("current")
_SmfPerformanceGroup_ObjectIdentity = ObjectIdentity
smfPerformanceGroup = _SmfPerformanceGroup_ObjectIdentity(
    (1, 3, 6, 1, 3, 126, 1, 4)
)
_SmfPerfGobalGroup_ObjectIdentity = ObjectIdentity
smfPerfGobalGroup = _SmfPerfGobalGroup_ObjectIdentity(
    (1, 3, 6, 1, 3, 126, 1, 4, 1)
)
_SmfPerfIpv4MultiPktsRecvTotal_Type = Counter32
_SmfPerfIpv4MultiPktsRecvTotal_Object = MibScalar
smfPerfIpv4MultiPktsRecvTotal = _SmfPerfIpv4MultiPktsRecvTotal_Object(
    (1, 3, 6, 1, 3, 126, 1, 4, 1, 1),
    _SmfPerfIpv4MultiPktsRecvTotal_Type()
)
smfPerfIpv4MultiPktsRecvTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smfPerfIpv4MultiPktsRecvTotal.setStatus("current")
if mibBuilder.loadTexts:
    smfPerfIpv4MultiPktsRecvTotal.setUnits("Packets")
_SmfPerfIpv4MultiPktsForwardedTotal_Type = Counter32
_SmfPerfIpv4MultiPktsForwardedTotal_Object = MibScalar
smfPerfIpv4MultiPktsForwardedTotal = _SmfPerfIpv4MultiPktsForwardedTotal_Object(
    (1, 3, 6, 1, 3, 126, 1, 4, 1, 2),
    _SmfPerfIpv4MultiPktsForwardedTotal_Type()
)
smfPerfIpv4MultiPktsForwardedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smfPerfIpv4MultiPktsForwardedTotal.setStatus("current")
if mibBuilder.loadTexts:
    smfPerfIpv4MultiPktsForwardedTotal.setUnits("Packets")
_SmfPerfIpv4DuplMultiPktsDetectedTotal_Type = Counter32
_SmfPerfIpv4DuplMultiPktsDetectedTotal_Object = MibScalar
smfPerfIpv4DuplMultiPktsDetectedTotal = _SmfPerfIpv4DuplMultiPktsDetectedTotal_Object(
    (1, 3, 6, 1, 3, 126, 1, 4, 1, 3),
    _SmfPerfIpv4DuplMultiPktsDetectedTotal_Type()
)
smfPerfIpv4DuplMultiPktsDetectedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smfPerfIpv4DuplMultiPktsDetectedTotal.setStatus("current")
if mibBuilder.loadTexts:
    smfPerfIpv4DuplMultiPktsDetectedTotal.setUnits("Packets")
_SmfPerfIpv4DroppedMultiPktsTTLExceededTotal_Type = Counter32
_SmfPerfIpv4DroppedMultiPktsTTLExceededTotal_Object = MibScalar
smfPerfIpv4DroppedMultiPktsTTLExceededTotal = _SmfPerfIpv4DroppedMultiPktsTTLExceededTotal_Object(
    (1, 3, 6, 1, 3, 126, 1, 4, 1, 4),
    _SmfPerfIpv4DroppedMultiPktsTTLExceededTotal_Type()
)
smfPerfIpv4DroppedMultiPktsTTLExceededTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smfPerfIpv4DroppedMultiPktsTTLExceededTotal.setStatus("current")
if mibBuilder.loadTexts:
    smfPerfIpv4DroppedMultiPktsTTLExceededTotal.setUnits("Packets")
_SmfPerfIpv4TTLLargerThanPreviousTotal_Type = Counter32
_SmfPerfIpv4TTLLargerThanPreviousTotal_Object = MibScalar
smfPerfIpv4TTLLargerThanPreviousTotal = _SmfPerfIpv4TTLLargerThanPreviousTotal_Object(
    (1, 3, 6, 1, 3, 126, 1, 4, 1, 5),
    _SmfPerfIpv4TTLLargerThanPreviousTotal_Type()
)
smfPerfIpv4TTLLargerThanPreviousTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smfPerfIpv4TTLLargerThanPreviousTotal.setStatus("current")
if mibBuilder.loadTexts:
    smfPerfIpv4TTLLargerThanPreviousTotal.setUnits("Packets")
_SmfPerfIpv6MultiPktsRecvTotal_Type = Counter32
_SmfPerfIpv6MultiPktsRecvTotal_Object = MibScalar
smfPerfIpv6MultiPktsRecvTotal = _SmfPerfIpv6MultiPktsRecvTotal_Object(
    (1, 3, 6, 1, 3, 126, 1, 4, 1, 6),
    _SmfPerfIpv6MultiPktsRecvTotal_Type()
)
smfPerfIpv6MultiPktsRecvTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smfPerfIpv6MultiPktsRecvTotal.setStatus("current")
if mibBuilder.loadTexts:
    smfPerfIpv6MultiPktsRecvTotal.setUnits("Packets")
_SmfPerfIpv6MultiPktsForwardedTotal_Type = Counter32
_SmfPerfIpv6MultiPktsForwardedTotal_Object = MibScalar
smfPerfIpv6MultiPktsForwardedTotal = _SmfPerfIpv6MultiPktsForwardedTotal_Object(
    (1, 3, 6, 1, 3, 126, 1, 4, 1, 7),
    _SmfPerfIpv6MultiPktsForwardedTotal_Type()
)
smfPerfIpv6MultiPktsForwardedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smfPerfIpv6MultiPktsForwardedTotal.setStatus("current")
if mibBuilder.loadTexts:
    smfPerfIpv6MultiPktsForwardedTotal.setUnits("Packets")
_SmfPerfIpv6DuplMultiPktsDetectedTotal_Type = Counter32
_SmfPerfIpv6DuplMultiPktsDetectedTotal_Object = MibScalar
smfPerfIpv6DuplMultiPktsDetectedTotal = _SmfPerfIpv6DuplMultiPktsDetectedTotal_Object(
    (1, 3, 6, 1, 3, 126, 1, 4, 1, 8),
    _SmfPerfIpv6DuplMultiPktsDetectedTotal_Type()
)
smfPerfIpv6DuplMultiPktsDetectedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smfPerfIpv6DuplMultiPktsDetectedTotal.setStatus("current")
if mibBuilder.loadTexts:
    smfPerfIpv6DuplMultiPktsDetectedTotal.setUnits("Packets")
_SmfPerfIpv6DroppedMultiPktsTTLExceededTotal_Type = Counter32
_SmfPerfIpv6DroppedMultiPktsTTLExceededTotal_Object = MibScalar
smfPerfIpv6DroppedMultiPktsTTLExceededTotal = _SmfPerfIpv6DroppedMultiPktsTTLExceededTotal_Object(
    (1, 3, 6, 1, 3, 126, 1, 4, 1, 9),
    _SmfPerfIpv6DroppedMultiPktsTTLExceededTotal_Type()
)
smfPerfIpv6DroppedMultiPktsTTLExceededTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smfPerfIpv6DroppedMultiPktsTTLExceededTotal.setStatus("current")
if mibBuilder.loadTexts:
    smfPerfIpv6DroppedMultiPktsTTLExceededTotal.setUnits("Packets")
_SmfPerfIpv6TTLLargerThanPreviousTotal_Type = Counter32
_SmfPerfIpv6TTLLargerThanPreviousTotal_Object = MibScalar
smfPerfIpv6TTLLargerThanPreviousTotal = _SmfPerfIpv6TTLLargerThanPreviousTotal_Object(
    (1, 3, 6, 1, 3, 126, 1, 4, 1, 10),
    _SmfPerfIpv6TTLLargerThanPreviousTotal_Type()
)
smfPerfIpv6TTLLargerThanPreviousTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smfPerfIpv6TTLLargerThanPreviousTotal.setStatus("current")
if mibBuilder.loadTexts:
    smfPerfIpv6TTLLargerThanPreviousTotal.setUnits("Packets")
_SmfPerfIpv6HAVAssistsReqdTotal_Type = Counter32
_SmfPerfIpv6HAVAssistsReqdTotal_Object = MibScalar
smfPerfIpv6HAVAssistsReqdTotal = _SmfPerfIpv6HAVAssistsReqdTotal_Object(
    (1, 3, 6, 1, 3, 126, 1, 4, 1, 11),
    _SmfPerfIpv6HAVAssistsReqdTotal_Type()
)
smfPerfIpv6HAVAssistsReqdTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smfPerfIpv6HAVAssistsReqdTotal.setStatus("current")
if mibBuilder.loadTexts:
    smfPerfIpv6HAVAssistsReqdTotal.setUnits("Packets")
_SmfPerfIpv6DpdHeaderInsertionsTotal_Type = Counter32
_SmfPerfIpv6DpdHeaderInsertionsTotal_Object = MibScalar
smfPerfIpv6DpdHeaderInsertionsTotal = _SmfPerfIpv6DpdHeaderInsertionsTotal_Object(
    (1, 3, 6, 1, 3, 126, 1, 4, 1, 12),
    _SmfPerfIpv6DpdHeaderInsertionsTotal_Type()
)
smfPerfIpv6DpdHeaderInsertionsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smfPerfIpv6DpdHeaderInsertionsTotal.setStatus("current")
if mibBuilder.loadTexts:
    smfPerfIpv6DpdHeaderInsertionsTotal.setUnits("Packets")
_SmfPerfInterfaceGroup_ObjectIdentity = ObjectIdentity
smfPerfInterfaceGroup = _SmfPerfInterfaceGroup_ObjectIdentity(
    (1, 3, 6, 1, 3, 126, 1, 4, 2)
)
_SmfPerfIpv4InterfacePerfTable_Object = MibTable
smfPerfIpv4InterfacePerfTable = _SmfPerfIpv4InterfacePerfTable_Object(
    (1, 3, 6, 1, 3, 126, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    smfPerfIpv4InterfacePerfTable.setStatus("current")
_SmfPerfIpv4InterfacePerfEntry_Object = MibTableRow
smfPerfIpv4InterfacePerfEntry = _SmfPerfIpv4InterfacePerfEntry_Object(
    (1, 3, 6, 1, 3, 126, 1, 4, 2, 1, 1)
)
smfPerfIpv4InterfacePerfEntry.setIndexNames(
    (0, "SMF-MIB", "smfCfgIfIndex"),
)
if mibBuilder.loadTexts:
    smfPerfIpv4InterfacePerfEntry.setStatus("current")
_SmfPerfIpv4MultiPktsRecvPerIf_Type = Counter32
_SmfPerfIpv4MultiPktsRecvPerIf_Object = MibTableColumn
smfPerfIpv4MultiPktsRecvPerIf = _SmfPerfIpv4MultiPktsRecvPerIf_Object(
    (1, 3, 6, 1, 3, 126, 1, 4, 2, 1, 1, 1),
    _SmfPerfIpv4MultiPktsRecvPerIf_Type()
)
smfPerfIpv4MultiPktsRecvPerIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smfPerfIpv4MultiPktsRecvPerIf.setStatus("current")
if mibBuilder.loadTexts:
    smfPerfIpv4MultiPktsRecvPerIf.setUnits("Packets")
_SmfPerfIpv4MultiPktsForwardedPerIf_Type = Counter32
_SmfPerfIpv4MultiPktsForwardedPerIf_Object = MibTableColumn
smfPerfIpv4MultiPktsForwardedPerIf = _SmfPerfIpv4MultiPktsForwardedPerIf_Object(
    (1, 3, 6, 1, 3, 126, 1, 4, 2, 1, 1, 2),
    _SmfPerfIpv4MultiPktsForwardedPerIf_Type()
)
smfPerfIpv4MultiPktsForwardedPerIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smfPerfIpv4MultiPktsForwardedPerIf.setStatus("current")
if mibBuilder.loadTexts:
    smfPerfIpv4MultiPktsForwardedPerIf.setUnits("Packets")
_SmfPerfIpv4DuplMultiPktsDetectedPerIf_Type = Counter32
_SmfPerfIpv4DuplMultiPktsDetectedPerIf_Object = MibTableColumn
smfPerfIpv4DuplMultiPktsDetectedPerIf = _SmfPerfIpv4DuplMultiPktsDetectedPerIf_Object(
    (1, 3, 6, 1, 3, 126, 1, 4, 2, 1, 1, 3),
    _SmfPerfIpv4DuplMultiPktsDetectedPerIf_Type()
)
smfPerfIpv4DuplMultiPktsDetectedPerIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smfPerfIpv4DuplMultiPktsDetectedPerIf.setStatus("current")
if mibBuilder.loadTexts:
    smfPerfIpv4DuplMultiPktsDetectedPerIf.setUnits("Packets")
_SmfPerfIpv4DroppedMultiPktsTTLExceededPerIf_Type = Counter32
_SmfPerfIpv4DroppedMultiPktsTTLExceededPerIf_Object = MibTableColumn
smfPerfIpv4DroppedMultiPktsTTLExceededPerIf = _SmfPerfIpv4DroppedMultiPktsTTLExceededPerIf_Object(
    (1, 3, 6, 1, 3, 126, 1, 4, 2, 1, 1, 4),
    _SmfPerfIpv4DroppedMultiPktsTTLExceededPerIf_Type()
)
smfPerfIpv4DroppedMultiPktsTTLExceededPerIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smfPerfIpv4DroppedMultiPktsTTLExceededPerIf.setStatus("current")
if mibBuilder.loadTexts:
    smfPerfIpv4DroppedMultiPktsTTLExceededPerIf.setUnits("Packets")
_SmfPerfIpv4TTLLargerThanPreviousPerIf_Type = Counter32
_SmfPerfIpv4TTLLargerThanPreviousPerIf_Object = MibTableColumn
smfPerfIpv4TTLLargerThanPreviousPerIf = _SmfPerfIpv4TTLLargerThanPreviousPerIf_Object(
    (1, 3, 6, 1, 3, 126, 1, 4, 2, 1, 1, 5),
    _SmfPerfIpv4TTLLargerThanPreviousPerIf_Type()
)
smfPerfIpv4TTLLargerThanPreviousPerIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smfPerfIpv4TTLLargerThanPreviousPerIf.setStatus("current")
if mibBuilder.loadTexts:
    smfPerfIpv4TTLLargerThanPreviousPerIf.setUnits("Packets")
_SmfPerfIpv6InterfacePerfTable_Object = MibTable
smfPerfIpv6InterfacePerfTable = _SmfPerfIpv6InterfacePerfTable_Object(
    (1, 3, 6, 1, 3, 126, 1, 4, 2, 2)
)
if mibBuilder.loadTexts:
    smfPerfIpv6InterfacePerfTable.setStatus("current")
_SmfPerfIpv6InterfacePerfEntry_Object = MibTableRow
smfPerfIpv6InterfacePerfEntry = _SmfPerfIpv6InterfacePerfEntry_Object(
    (1, 3, 6, 1, 3, 126, 1, 4, 2, 2, 1)
)
smfPerfIpv6InterfacePerfEntry.setIndexNames(
    (0, "SMF-MIB", "smfCfgIfIndex"),
)
if mibBuilder.loadTexts:
    smfPerfIpv6InterfacePerfEntry.setStatus("current")
_SmfPerfIpv6MultiPktsRecvPerIf_Type = Counter32
_SmfPerfIpv6MultiPktsRecvPerIf_Object = MibTableColumn
smfPerfIpv6MultiPktsRecvPerIf = _SmfPerfIpv6MultiPktsRecvPerIf_Object(
    (1, 3, 6, 1, 3, 126, 1, 4, 2, 2, 1, 1),
    _SmfPerfIpv6MultiPktsRecvPerIf_Type()
)
smfPerfIpv6MultiPktsRecvPerIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smfPerfIpv6MultiPktsRecvPerIf.setStatus("current")
if mibBuilder.loadTexts:
    smfPerfIpv6MultiPktsRecvPerIf.setUnits("Packets")
_SmfPerfIpv6MultiPktsForwardedPerIf_Type = Counter32
_SmfPerfIpv6MultiPktsForwardedPerIf_Object = MibTableColumn
smfPerfIpv6MultiPktsForwardedPerIf = _SmfPerfIpv6MultiPktsForwardedPerIf_Object(
    (1, 3, 6, 1, 3, 126, 1, 4, 2, 2, 1, 2),
    _SmfPerfIpv6MultiPktsForwardedPerIf_Type()
)
smfPerfIpv6MultiPktsForwardedPerIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smfPerfIpv6MultiPktsForwardedPerIf.setStatus("current")
if mibBuilder.loadTexts:
    smfPerfIpv6MultiPktsForwardedPerIf.setUnits("Packets")
_SmfPerfIpv6DuplMultiPktsDetectedPerIf_Type = Counter32
_SmfPerfIpv6DuplMultiPktsDetectedPerIf_Object = MibTableColumn
smfPerfIpv6DuplMultiPktsDetectedPerIf = _SmfPerfIpv6DuplMultiPktsDetectedPerIf_Object(
    (1, 3, 6, 1, 3, 126, 1, 4, 2, 2, 1, 3),
    _SmfPerfIpv6DuplMultiPktsDetectedPerIf_Type()
)
smfPerfIpv6DuplMultiPktsDetectedPerIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smfPerfIpv6DuplMultiPktsDetectedPerIf.setStatus("current")
if mibBuilder.loadTexts:
    smfPerfIpv6DuplMultiPktsDetectedPerIf.setUnits("Packets")
_SmfPerfIpv6DroppedMultiPktsTTLExceededPerIf_Type = Counter32
_SmfPerfIpv6DroppedMultiPktsTTLExceededPerIf_Object = MibTableColumn
smfPerfIpv6DroppedMultiPktsTTLExceededPerIf = _SmfPerfIpv6DroppedMultiPktsTTLExceededPerIf_Object(
    (1, 3, 6, 1, 3, 126, 1, 4, 2, 2, 1, 4),
    _SmfPerfIpv6DroppedMultiPktsTTLExceededPerIf_Type()
)
smfPerfIpv6DroppedMultiPktsTTLExceededPerIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smfPerfIpv6DroppedMultiPktsTTLExceededPerIf.setStatus("current")
if mibBuilder.loadTexts:
    smfPerfIpv6DroppedMultiPktsTTLExceededPerIf.setUnits("Packets")
_SmfPerfIpv6TTLLargerThanPreviousPerIf_Type = Counter32
_SmfPerfIpv6TTLLargerThanPreviousPerIf_Object = MibTableColumn
smfPerfIpv6TTLLargerThanPreviousPerIf = _SmfPerfIpv6TTLLargerThanPreviousPerIf_Object(
    (1, 3, 6, 1, 3, 126, 1, 4, 2, 2, 1, 5),
    _SmfPerfIpv6TTLLargerThanPreviousPerIf_Type()
)
smfPerfIpv6TTLLargerThanPreviousPerIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smfPerfIpv6TTLLargerThanPreviousPerIf.setStatus("current")
if mibBuilder.loadTexts:
    smfPerfIpv6TTLLargerThanPreviousPerIf.setUnits("Packets")
_SmfPerfIpv6HAVAssistsReqdPerIf_Type = Counter32
_SmfPerfIpv6HAVAssistsReqdPerIf_Object = MibTableColumn
smfPerfIpv6HAVAssistsReqdPerIf = _SmfPerfIpv6HAVAssistsReqdPerIf_Object(
    (1, 3, 6, 1, 3, 126, 1, 4, 2, 2, 1, 6),
    _SmfPerfIpv6HAVAssistsReqdPerIf_Type()
)
smfPerfIpv6HAVAssistsReqdPerIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smfPerfIpv6HAVAssistsReqdPerIf.setStatus("current")
if mibBuilder.loadTexts:
    smfPerfIpv6HAVAssistsReqdPerIf.setUnits("Packets")
_SmfPerfIpv6DpdHeaderInsertionsPerIf_Type = Counter32
_SmfPerfIpv6DpdHeaderInsertionsPerIf_Object = MibTableColumn
smfPerfIpv6DpdHeaderInsertionsPerIf = _SmfPerfIpv6DpdHeaderInsertionsPerIf_Object(
    (1, 3, 6, 1, 3, 126, 1, 4, 2, 2, 1, 7),
    _SmfPerfIpv6DpdHeaderInsertionsPerIf_Type()
)
smfPerfIpv6DpdHeaderInsertionsPerIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smfPerfIpv6DpdHeaderInsertionsPerIf.setStatus("current")
if mibBuilder.loadTexts:
    smfPerfIpv6DpdHeaderInsertionsPerIf.setUnits("Packets")
_SmfMIBConformance_ObjectIdentity = ObjectIdentity
smfMIBConformance = _SmfMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 3, 126, 2)
)
_SmfCompliances_ObjectIdentity = ObjectIdentity
smfCompliances = _SmfCompliances_ObjectIdentity(
    (1, 3, 6, 1, 3, 126, 2, 1)
)
_SmfMIBGroups_ObjectIdentity = ObjectIdentity
smfMIBGroups = _SmfMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 3, 126, 2, 2)
)

# Managed Objects groups

smfCapabObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 126, 2, 2, 1)
)
smfCapabObjectsGroup.setObjects(
      *(("SMF-MIB", "smfCapabilitiesOpModeID"),
        ("SMF-MIB", "smfCapabilitiesRssaID"))
)
if mibBuilder.loadTexts:
    smfCapabObjectsGroup.setStatus("current")

smfConfigObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 126, 2, 2, 2)
)
smfConfigObjectsGroup.setObjects(
      *(("SMF-MIB", "smfCfgAdminStatus"),
        ("SMF-MIB", "smfCfgSmfSysUpTime"),
        ("SMF-MIB", "smfCfgRouterIDAddrType"),
        ("SMF-MIB", "smfCfgRouterID"),
        ("SMF-MIB", "smfCfgOperationalMode"),
        ("SMF-MIB", "smfCfgRssaMember"),
        ("SMF-MIB", "smfCfgIpv4Dpd"),
        ("SMF-MIB", "smfCfgIpv6Dpd"),
        ("SMF-MIB", "smfCfgMaxPktLifetime"),
        ("SMF-MIB", "smfCfgDpdEntryMaxLifetime"),
        ("SMF-MIB", "smfCfgNhdpRssaMesgTLVIncluded"),
        ("SMF-MIB", "smfCfgNhdpRssaAddrBlockTLVIncluded"),
        ("SMF-MIB", "smfCfgAddrForwardingGroupName"),
        ("SMF-MIB", "smfCfgAddrForwardingAddrType"),
        ("SMF-MIB", "smfCfgAddrForwardingAddress"),
        ("SMF-MIB", "smfCfgAddrForwardingAddrPrefixLength"),
        ("SMF-MIB", "smfCfgAddrForwardingStatus"),
        ("SMF-MIB", "smfCfgIfAdminStatus"),
        ("SMF-MIB", "smfCfgIfSmfUpTime"),
        ("SMF-MIB", "smfCfgIfRowStatus"))
)
if mibBuilder.loadTexts:
    smfConfigObjectsGroup.setStatus("current")

smfStateObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 126, 2, 2, 3)
)
smfStateObjectsGroup.setObjects(
      *(("SMF-MIB", "smfStateNodeRsStatusIncluded"),
        ("SMF-MIB", "smfStateDpdMemoryOverflow"),
        ("SMF-MIB", "smfStateNeighborRSSA"),
        ("SMF-MIB", "smfStateNeighborNextHopInterface"))
)
if mibBuilder.loadTexts:
    smfStateObjectsGroup.setStatus("current")

smfPerfObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 126, 2, 2, 4)
)
smfPerfObjectsGroup.setObjects(
      *(("SMF-MIB", "smfPerfIpv4MultiPktsRecvTotal"),
        ("SMF-MIB", "smfPerfIpv4MultiPktsForwardedTotal"),
        ("SMF-MIB", "smfPerfIpv4DuplMultiPktsDetectedTotal"),
        ("SMF-MIB", "smfPerfIpv4DroppedMultiPktsTTLExceededTotal"),
        ("SMF-MIB", "smfPerfIpv4TTLLargerThanPreviousTotal"),
        ("SMF-MIB", "smfPerfIpv6MultiPktsRecvTotal"),
        ("SMF-MIB", "smfPerfIpv6MultiPktsForwardedTotal"),
        ("SMF-MIB", "smfPerfIpv6DuplMultiPktsDetectedTotal"),
        ("SMF-MIB", "smfPerfIpv6DroppedMultiPktsTTLExceededTotal"),
        ("SMF-MIB", "smfPerfIpv6TTLLargerThanPreviousTotal"),
        ("SMF-MIB", "smfPerfIpv6HAVAssistsReqdTotal"),
        ("SMF-MIB", "smfPerfIpv6DpdHeaderInsertionsTotal"),
        ("SMF-MIB", "smfPerfIpv4MultiPktsRecvPerIf"),
        ("SMF-MIB", "smfPerfIpv4MultiPktsForwardedPerIf"),
        ("SMF-MIB", "smfPerfIpv4DuplMultiPktsDetectedPerIf"),
        ("SMF-MIB", "smfPerfIpv4DroppedMultiPktsTTLExceededPerIf"),
        ("SMF-MIB", "smfPerfIpv4TTLLargerThanPreviousPerIf"),
        ("SMF-MIB", "smfPerfIpv6MultiPktsRecvPerIf"),
        ("SMF-MIB", "smfPerfIpv6MultiPktsForwardedPerIf"),
        ("SMF-MIB", "smfPerfIpv6DuplMultiPktsDetectedPerIf"),
        ("SMF-MIB", "smfPerfIpv6DroppedMultiPktsTTLExceededPerIf"),
        ("SMF-MIB", "smfPerfIpv6TTLLargerThanPreviousPerIf"),
        ("SMF-MIB", "smfPerfIpv6HAVAssistsReqdPerIf"),
        ("SMF-MIB", "smfPerfIpv6DpdHeaderInsertionsPerIf"))
)
if mibBuilder.loadTexts:
    smfPerfObjectsGroup.setStatus("current")

smfNotifObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 126, 2, 2, 5)
)
smfNotifObjectsGroup.setObjects(
      *(("SMF-MIB", "smfNotifDpdMemoryOverflowThreshold"),
        ("SMF-MIB", "smfNotifDpdMemoryOverflowWindow"))
)
if mibBuilder.loadTexts:
    smfNotifObjectsGroup.setStatus("current")


# Notification objects

smfNotifAdminStatusChange = NotificationType(
    (1, 3, 6, 1, 3, 126, 0, 0, 1)
)
smfNotifAdminStatusChange.setObjects(
      *(("SMF-MIB", "smfCfgRouterIDAddrType"),
        ("SMF-MIB", "smfCfgRouterID"),
        ("SMF-MIB", "smfCfgAdminStatus"))
)
if mibBuilder.loadTexts:
    smfNotifAdminStatusChange.setStatus(
        "current"
    )

smfNotifConfiguredOpModeChange = NotificationType(
    (1, 3, 6, 1, 3, 126, 0, 0, 2)
)
smfNotifConfiguredOpModeChange.setObjects(
      *(("SMF-MIB", "smfCfgRouterIDAddrType"),
        ("SMF-MIB", "smfCfgRouterID"),
        ("SMF-MIB", "smfCfgOperationalMode"))
)
if mibBuilder.loadTexts:
    smfNotifConfiguredOpModeChange.setStatus(
        "current"
    )

smfNotifIfAdminStatusChange = NotificationType(
    (1, 3, 6, 1, 3, 126, 0, 0, 3)
)
smfNotifIfAdminStatusChange.setObjects(
      *(("SMF-MIB", "smfCfgRouterIDAddrType"),
        ("SMF-MIB", "smfCfgRouterID"),
        ("IF-MIB", "ifName"),
        ("SMF-MIB", "smfCfgIfAdminStatus"))
)
if mibBuilder.loadTexts:
    smfNotifIfAdminStatusChange.setStatus(
        "current"
    )

smfNotifDpdMemoryOverflowEvent = NotificationType(
    (1, 3, 6, 1, 3, 126, 0, 0, 4)
)
smfNotifDpdMemoryOverflowEvent.setObjects(
      *(("SMF-MIB", "smfCfgRouterIDAddrType"),
        ("SMF-MIB", "smfCfgRouterID"),
        ("SMF-MIB", "smfStateDpdMemoryOverflow"))
)
if mibBuilder.loadTexts:
    smfNotifDpdMemoryOverflowEvent.setStatus(
        "current"
    )


# Notifications groups

smfNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 3, 126, 2, 2, 6)
)
smfNotificationsGroup.setObjects(
      *(("SMF-MIB", "smfNotifAdminStatusChange"),
        ("SMF-MIB", "smfNotifConfiguredOpModeChange"),
        ("SMF-MIB", "smfNotifIfAdminStatusChange"),
        ("SMF-MIB", "smfNotifDpdMemoryOverflowEvent"))
)
if mibBuilder.loadTexts:
    smfNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

smfBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 3, 126, 2, 1, 1)
)
if mibBuilder.loadTexts:
    smfBasicCompliance.setStatus(
        "current"
    )

smfFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 3, 126, 2, 1, 2)
)
if mibBuilder.loadTexts:
    smfFullCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SMF-MIB",
    **{"SmfStatus": SmfStatus,
       "smfMIB": smfMIB,
       "smfMIBNotifications": smfMIBNotifications,
       "smfMIBNotifObjects": smfMIBNotifObjects,
       "smfNotifAdminStatusChange": smfNotifAdminStatusChange,
       "smfNotifConfiguredOpModeChange": smfNotifConfiguredOpModeChange,
       "smfNotifIfAdminStatusChange": smfNotifIfAdminStatusChange,
       "smfNotifDpdMemoryOverflowEvent": smfNotifDpdMemoryOverflowEvent,
       "smfMIBNotifControl": smfMIBNotifControl,
       "smfNotifDpdMemoryOverflowThreshold": smfNotifDpdMemoryOverflowThreshold,
       "smfNotifDpdMemoryOverflowWindow": smfNotifDpdMemoryOverflowWindow,
       "smfMIBObjects": smfMIBObjects,
       "smfCapabilitiesGroup": smfCapabilitiesGroup,
       "smfCapabilitiesTable": smfCapabilitiesTable,
       "smfCapabilitiesEntry": smfCapabilitiesEntry,
       "smfCapabilitiesIndex": smfCapabilitiesIndex,
       "smfCapabilitiesOpModeID": smfCapabilitiesOpModeID,
       "smfCapabilitiesRssaID": smfCapabilitiesRssaID,
       "smfConfigurationGroup": smfConfigurationGroup,
       "smfCfgAdminStatus": smfCfgAdminStatus,
       "smfCfgSmfSysUpTime": smfCfgSmfSysUpTime,
       "smfCfgRouterIDAddrType": smfCfgRouterIDAddrType,
       "smfCfgRouterID": smfCfgRouterID,
       "smfCfgOperationalMode": smfCfgOperationalMode,
       "smfCfgRssaMember": smfCfgRssaMember,
       "smfCfgIpv4Dpd": smfCfgIpv4Dpd,
       "smfCfgIpv6Dpd": smfCfgIpv6Dpd,
       "smfCfgMaxPktLifetime": smfCfgMaxPktLifetime,
       "smfCfgDpdEntryMaxLifetime": smfCfgDpdEntryMaxLifetime,
       "smfCfgNhdpRssaMesgTLVIncluded": smfCfgNhdpRssaMesgTLVIncluded,
       "smfCfgNhdpRssaAddrBlockTLVIncluded": smfCfgNhdpRssaAddrBlockTLVIncluded,
       "smfCfgAddrForwardingTable": smfCfgAddrForwardingTable,
       "smfCfgAddrForwardingEntry": smfCfgAddrForwardingEntry,
       "smfCfgAddrForwardingIndex": smfCfgAddrForwardingIndex,
       "smfCfgAddrForwardingGroupName": smfCfgAddrForwardingGroupName,
       "smfCfgAddrForwardingAddrType": smfCfgAddrForwardingAddrType,
       "smfCfgAddrForwardingAddress": smfCfgAddrForwardingAddress,
       "smfCfgAddrForwardingAddrPrefixLength": smfCfgAddrForwardingAddrPrefixLength,
       "smfCfgAddrForwardingStatus": smfCfgAddrForwardingStatus,
       "smfCfgInterfaceTable": smfCfgInterfaceTable,
       "smfCfgInterfaceEntry": smfCfgInterfaceEntry,
       "smfCfgIfIndex": smfCfgIfIndex,
       "smfCfgIfAdminStatus": smfCfgIfAdminStatus,
       "smfCfgIfSmfUpTime": smfCfgIfSmfUpTime,
       "smfCfgIfRowStatus": smfCfgIfRowStatus,
       "smfStateGroup": smfStateGroup,
       "smfStateNodeRsStatusIncluded": smfStateNodeRsStatusIncluded,
       "smfStateDpdMemoryOverflow": smfStateDpdMemoryOverflow,
       "smfStateNeighborTable": smfStateNeighborTable,
       "smfStateNeighborEntry": smfStateNeighborEntry,
       "smfStateNeighborIpAddrType": smfStateNeighborIpAddrType,
       "smfStateNeighborIpAddr": smfStateNeighborIpAddr,
       "smfStateNeighborPrefixLen": smfStateNeighborPrefixLen,
       "smfStateNeighborRSSA": smfStateNeighborRSSA,
       "smfStateNeighborNextHopInterface": smfStateNeighborNextHopInterface,
       "smfPerformanceGroup": smfPerformanceGroup,
       "smfPerfGobalGroup": smfPerfGobalGroup,
       "smfPerfIpv4MultiPktsRecvTotal": smfPerfIpv4MultiPktsRecvTotal,
       "smfPerfIpv4MultiPktsForwardedTotal": smfPerfIpv4MultiPktsForwardedTotal,
       "smfPerfIpv4DuplMultiPktsDetectedTotal": smfPerfIpv4DuplMultiPktsDetectedTotal,
       "smfPerfIpv4DroppedMultiPktsTTLExceededTotal": smfPerfIpv4DroppedMultiPktsTTLExceededTotal,
       "smfPerfIpv4TTLLargerThanPreviousTotal": smfPerfIpv4TTLLargerThanPreviousTotal,
       "smfPerfIpv6MultiPktsRecvTotal": smfPerfIpv6MultiPktsRecvTotal,
       "smfPerfIpv6MultiPktsForwardedTotal": smfPerfIpv6MultiPktsForwardedTotal,
       "smfPerfIpv6DuplMultiPktsDetectedTotal": smfPerfIpv6DuplMultiPktsDetectedTotal,
       "smfPerfIpv6DroppedMultiPktsTTLExceededTotal": smfPerfIpv6DroppedMultiPktsTTLExceededTotal,
       "smfPerfIpv6TTLLargerThanPreviousTotal": smfPerfIpv6TTLLargerThanPreviousTotal,
       "smfPerfIpv6HAVAssistsReqdTotal": smfPerfIpv6HAVAssistsReqdTotal,
       "smfPerfIpv6DpdHeaderInsertionsTotal": smfPerfIpv6DpdHeaderInsertionsTotal,
       "smfPerfInterfaceGroup": smfPerfInterfaceGroup,
       "smfPerfIpv4InterfacePerfTable": smfPerfIpv4InterfacePerfTable,
       "smfPerfIpv4InterfacePerfEntry": smfPerfIpv4InterfacePerfEntry,
       "smfPerfIpv4MultiPktsRecvPerIf": smfPerfIpv4MultiPktsRecvPerIf,
       "smfPerfIpv4MultiPktsForwardedPerIf": smfPerfIpv4MultiPktsForwardedPerIf,
       "smfPerfIpv4DuplMultiPktsDetectedPerIf": smfPerfIpv4DuplMultiPktsDetectedPerIf,
       "smfPerfIpv4DroppedMultiPktsTTLExceededPerIf": smfPerfIpv4DroppedMultiPktsTTLExceededPerIf,
       "smfPerfIpv4TTLLargerThanPreviousPerIf": smfPerfIpv4TTLLargerThanPreviousPerIf,
       "smfPerfIpv6InterfacePerfTable": smfPerfIpv6InterfacePerfTable,
       "smfPerfIpv6InterfacePerfEntry": smfPerfIpv6InterfacePerfEntry,
       "smfPerfIpv6MultiPktsRecvPerIf": smfPerfIpv6MultiPktsRecvPerIf,
       "smfPerfIpv6MultiPktsForwardedPerIf": smfPerfIpv6MultiPktsForwardedPerIf,
       "smfPerfIpv6DuplMultiPktsDetectedPerIf": smfPerfIpv6DuplMultiPktsDetectedPerIf,
       "smfPerfIpv6DroppedMultiPktsTTLExceededPerIf": smfPerfIpv6DroppedMultiPktsTTLExceededPerIf,
       "smfPerfIpv6TTLLargerThanPreviousPerIf": smfPerfIpv6TTLLargerThanPreviousPerIf,
       "smfPerfIpv6HAVAssistsReqdPerIf": smfPerfIpv6HAVAssistsReqdPerIf,
       "smfPerfIpv6DpdHeaderInsertionsPerIf": smfPerfIpv6DpdHeaderInsertionsPerIf,
       "smfMIBConformance": smfMIBConformance,
       "smfCompliances": smfCompliances,
       "smfBasicCompliance": smfBasicCompliance,
       "smfFullCompliance": smfFullCompliance,
       "smfMIBGroups": smfMIBGroups,
       "smfCapabObjectsGroup": smfCapabObjectsGroup,
       "smfConfigObjectsGroup": smfConfigObjectsGroup,
       "smfStateObjectsGroup": smfStateObjectsGroup,
       "smfPerfObjectsGroup": smfPerfObjectsGroup,
       "smfNotifObjectsGroup": smfNotifObjectsGroup,
       "smfNotificationsGroup": smfNotificationsGroup}
)
