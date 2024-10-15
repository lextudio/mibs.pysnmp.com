# SNMP MIB module (ALCATEL-IND1-DHCPV6-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-DHCPV6-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:35:51 2024
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

(softentIND1Ipv6,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1Ipv6")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(ipv6IfIndex,) = mibBuilder.importSymbols(
    "IPV6-MIB",
    "ipv6IfIndex")

(Ipv6Address,
 Ipv6IfIndexOrZero) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address",
    "Ipv6IfIndexOrZero")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

alcatelIND1DHCPv6MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 2)
)
alcatelIND1DHCPv6MIB.setRevisions(
        ("2013-03-22 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1DHCPv6MIBNotifications_ObjectIdentity = ObjectIdentity
alcatelIND1DHCPv6MIBNotifications = _AlcatelIND1DHCPv6MIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 2, 0)
)
_AlcatelIND1DHCPv6MIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1DHCPv6MIBObjects = _AlcatelIND1DHCPv6MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 2, 1)
)
_AlaDHCPv6RelayConfig_ObjectIdentity = ObjectIdentity
alaDHCPv6RelayConfig = _AlaDHCPv6RelayConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 2, 1, 1)
)


class _AlaDHCPv6RelayAdminStatus_Type(Integer32):
    """Custom type alaDHCPv6RelayAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AlaDHCPv6RelayAdminStatus_Type.__name__ = "Integer32"
_AlaDHCPv6RelayAdminStatus_Object = MibScalar
alaDHCPv6RelayAdminStatus = _AlaDHCPv6RelayAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 2, 1, 1, 1),
    _AlaDHCPv6RelayAdminStatus_Type()
)
alaDHCPv6RelayAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDHCPv6RelayAdminStatus.setStatus("current")
_AlaDHCPv6SrvConfig_ObjectIdentity = ObjectIdentity
alaDHCPv6SrvConfig = _AlaDHCPv6SrvConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 2, 1, 2)
)


class _AlaDHCPv6SrvGlobalConfigStatus_Type(Integer32):
    """Custom type alaDHCPv6SrvGlobalConfigStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AlaDHCPv6SrvGlobalConfigStatus_Type.__name__ = "Integer32"
_AlaDHCPv6SrvGlobalConfigStatus_Object = MibScalar
alaDHCPv6SrvGlobalConfigStatus = _AlaDHCPv6SrvGlobalConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 2, 1, 2, 1),
    _AlaDHCPv6SrvGlobalConfigStatus_Type()
)
alaDHCPv6SrvGlobalConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDHCPv6SrvGlobalConfigStatus.setStatus("current")


class _AlaDHCPv6SrvGlobalRestart_Type(Integer32):
    """Custom type alaDHCPv6SrvGlobalRestart based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("restart", 2))
    )


_AlaDHCPv6SrvGlobalRestart_Type.__name__ = "Integer32"
_AlaDHCPv6SrvGlobalRestart_Object = MibScalar
alaDHCPv6SrvGlobalRestart = _AlaDHCPv6SrvGlobalRestart_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 2, 1, 2, 2),
    _AlaDHCPv6SrvGlobalRestart_Type()
)
alaDHCPv6SrvGlobalRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDHCPv6SrvGlobalRestart.setStatus("current")


class _AlaDHCPv6SrvGlobalClearStat_Type(Integer32):
    """Custom type alaDHCPv6SrvGlobalClearStat based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("reset", 2))
    )


_AlaDHCPv6SrvGlobalClearStat_Type.__name__ = "Integer32"
_AlaDHCPv6SrvGlobalClearStat_Object = MibScalar
alaDHCPv6SrvGlobalClearStat = _AlaDHCPv6SrvGlobalClearStat_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 2, 1, 2, 3),
    _AlaDHCPv6SrvGlobalClearStat_Type()
)
alaDHCPv6SrvGlobalClearStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDHCPv6SrvGlobalClearStat.setStatus("current")
_AlaDHCPv6RelayInterfaceTable_Object = MibTable
alaDHCPv6RelayInterfaceTable = _AlaDHCPv6RelayInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 2, 1, 3)
)
if mibBuilder.loadTexts:
    alaDHCPv6RelayInterfaceTable.setStatus("current")
_AlaDHCPv6RelayInterfaceEntry_Object = MibTableRow
alaDHCPv6RelayInterfaceEntry = _AlaDHCPv6RelayInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 2, 1, 3, 1)
)
alaDHCPv6RelayInterfaceEntry.setIndexNames(
    (0, "IPV6-MIB", "ipv6IfIndex"),
)
if mibBuilder.loadTexts:
    alaDHCPv6RelayInterfaceEntry.setStatus("current")


class _AlaDHCPv6RelayInterfaceAdminStatus_Type(Integer32):
    """Custom type alaDHCPv6RelayInterfaceAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AlaDHCPv6RelayInterfaceAdminStatus_Type.__name__ = "Integer32"
_AlaDHCPv6RelayInterfaceAdminStatus_Object = MibTableColumn
alaDHCPv6RelayInterfaceAdminStatus = _AlaDHCPv6RelayInterfaceAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 2, 1, 3, 1, 1),
    _AlaDHCPv6RelayInterfaceAdminStatus_Type()
)
alaDHCPv6RelayInterfaceAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDHCPv6RelayInterfaceAdminStatus.setStatus("current")
_AlaDHCPv6RelayDestinationTable_Object = MibTable
alaDHCPv6RelayDestinationTable = _AlaDHCPv6RelayDestinationTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 2, 1, 4)
)
if mibBuilder.loadTexts:
    alaDHCPv6RelayDestinationTable.setStatus("current")
_AlaDHCPv6RelayDestinationEntry_Object = MibTableRow
alaDHCPv6RelayDestinationEntry = _AlaDHCPv6RelayDestinationEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 2, 1, 4, 1)
)
alaDHCPv6RelayDestinationEntry.setIndexNames(
    (0, "IPV6-MIB", "ipv6IfIndex"),
    (0, "ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6RelayDestinationAddressType"),
    (0, "ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6RelayDestinationAddress"),
)
if mibBuilder.loadTexts:
    alaDHCPv6RelayDestinationEntry.setStatus("current")
_AlaDHCPv6RelayDestinationAddressType_Type = InetAddressType
_AlaDHCPv6RelayDestinationAddressType_Object = MibTableColumn
alaDHCPv6RelayDestinationAddressType = _AlaDHCPv6RelayDestinationAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 2, 1, 4, 1, 1),
    _AlaDHCPv6RelayDestinationAddressType_Type()
)
alaDHCPv6RelayDestinationAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDHCPv6RelayDestinationAddressType.setStatus("current")
_AlaDHCPv6RelayDestinationAddress_Type = InetAddress
_AlaDHCPv6RelayDestinationAddress_Object = MibTableColumn
alaDHCPv6RelayDestinationAddress = _AlaDHCPv6RelayDestinationAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 2, 1, 4, 1, 2),
    _AlaDHCPv6RelayDestinationAddress_Type()
)
alaDHCPv6RelayDestinationAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDHCPv6RelayDestinationAddress.setStatus("current")
_AlaDHCPv6RelayDestinationRowStatus_Type = RowStatus
_AlaDHCPv6RelayDestinationRowStatus_Object = MibTableColumn
alaDHCPv6RelayDestinationRowStatus = _AlaDHCPv6RelayDestinationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 2, 1, 4, 1, 3),
    _AlaDHCPv6RelayDestinationRowStatus_Type()
)
alaDHCPv6RelayDestinationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDHCPv6RelayDestinationRowStatus.setStatus("current")
_AlaDHCPv6SrvLease_ObjectIdentity = ObjectIdentity
alaDHCPv6SrvLease = _AlaDHCPv6SrvLease_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 2, 1, 5)
)
_AlaDHCPv6SrvLeaseTable_Object = MibTable
alaDHCPv6SrvLeaseTable = _AlaDHCPv6SrvLeaseTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 2, 1, 5, 1)
)
if mibBuilder.loadTexts:
    alaDHCPv6SrvLeaseTable.setStatus("current")
_AlaDHCPv6SrvLeaseEntry_Object = MibTableRow
alaDHCPv6SrvLeaseEntry = _AlaDHCPv6SrvLeaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 2, 1, 5, 1, 1)
)
alaDHCPv6SrvLeaseEntry.setIndexNames(
    (0, "ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6SrvLeaseIpv6Address"),
)
if mibBuilder.loadTexts:
    alaDHCPv6SrvLeaseEntry.setStatus("current")
_AlaDHCPv6SrvLeaseIpv6Address_Type = Ipv6Address
_AlaDHCPv6SrvLeaseIpv6Address_Object = MibTableColumn
alaDHCPv6SrvLeaseIpv6Address = _AlaDHCPv6SrvLeaseIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 2, 1, 5, 1, 1, 1),
    _AlaDHCPv6SrvLeaseIpv6Address_Type()
)
alaDHCPv6SrvLeaseIpv6Address.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDHCPv6SrvLeaseIpv6Address.setStatus("current")
_AlaDHCPv6SrvLeaseLeaseGrant_Type = DateAndTime
_AlaDHCPv6SrvLeaseLeaseGrant_Object = MibTableColumn
alaDHCPv6SrvLeaseLeaseGrant = _AlaDHCPv6SrvLeaseLeaseGrant_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 2, 1, 5, 1, 1, 2),
    _AlaDHCPv6SrvLeaseLeaseGrant_Type()
)
alaDHCPv6SrvLeaseLeaseGrant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDHCPv6SrvLeaseLeaseGrant.setStatus("current")
_AlaDHCPv6SrvLeasePrefLeaseExpiry_Type = DateAndTime
_AlaDHCPv6SrvLeasePrefLeaseExpiry_Object = MibTableColumn
alaDHCPv6SrvLeasePrefLeaseExpiry = _AlaDHCPv6SrvLeasePrefLeaseExpiry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 2, 1, 5, 1, 1, 3),
    _AlaDHCPv6SrvLeasePrefLeaseExpiry_Type()
)
alaDHCPv6SrvLeasePrefLeaseExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDHCPv6SrvLeasePrefLeaseExpiry.setStatus("current")
_AlaDHCPv6SrvLeaseValidLeaseExpiry_Type = DateAndTime
_AlaDHCPv6SrvLeaseValidLeaseExpiry_Object = MibTableColumn
alaDHCPv6SrvLeaseValidLeaseExpiry = _AlaDHCPv6SrvLeaseValidLeaseExpiry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 2, 1, 5, 1, 1, 4),
    _AlaDHCPv6SrvLeaseValidLeaseExpiry_Type()
)
alaDHCPv6SrvLeaseValidLeaseExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDHCPv6SrvLeaseValidLeaseExpiry.setStatus("current")


class _AlaDHCPv6SrvLeaseType_Type(Integer32):
    """Custom type alaDHCPv6SrvLeaseType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("manual", 3),
          ("unavailable", 1))
    )


_AlaDHCPv6SrvLeaseType_Type.__name__ = "Integer32"
_AlaDHCPv6SrvLeaseType_Object = MibTableColumn
alaDHCPv6SrvLeaseType = _AlaDHCPv6SrvLeaseType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 2, 1, 5, 1, 1, 5),
    _AlaDHCPv6SrvLeaseType_Type()
)
alaDHCPv6SrvLeaseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDHCPv6SrvLeaseType.setStatus("current")
_AlaDHCPv6SrvTrapsObj_ObjectIdentity = ObjectIdentity
alaDHCPv6SrvTrapsObj = _AlaDHCPv6SrvTrapsObj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 2, 1, 6)
)


class _AlaDHCPv6SrvLeaseThresholdStatus_Type(Integer32):
    """Custom type alaDHCPv6SrvLeaseThresholdStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("crossedAbove80Threshold", 2),
          ("crossedBelow80Threshold", 1),
          ("reached100Threshold", 3))
    )


_AlaDHCPv6SrvLeaseThresholdStatus_Type.__name__ = "Integer32"
_AlaDHCPv6SrvLeaseThresholdStatus_Object = MibScalar
alaDHCPv6SrvLeaseThresholdStatus = _AlaDHCPv6SrvLeaseThresholdStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 2, 1, 6, 1),
    _AlaDHCPv6SrvLeaseThresholdStatus_Type()
)
alaDHCPv6SrvLeaseThresholdStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDHCPv6SrvLeaseThresholdStatus.setStatus("current")
_AlaDHCPv6SrvSubnetDescriptor_Type = DisplayString
_AlaDHCPv6SrvSubnetDescriptor_Object = MibScalar
alaDHCPv6SrvSubnetDescriptor = _AlaDHCPv6SrvSubnetDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 2, 1, 6, 2),
    _AlaDHCPv6SrvSubnetDescriptor_Type()
)
alaDHCPv6SrvSubnetDescriptor.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDHCPv6SrvSubnetDescriptor.setStatus("current")
_AlcatelIND1DHCPv6MIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1DHCPv6MIBConformance = _AlcatelIND1DHCPv6MIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 2, 2)
)
_AlcatelIND1DHCPv6MIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1DHCPv6MIBCompliances = _AlcatelIND1DHCPv6MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 2, 2, 1)
)
_AlcatelIND1DHCPv6MIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1DHCPv6MIBGroups = _AlcatelIND1DHCPv6MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 2, 2, 2)
)

# Managed Objects groups

alaDHCPv6RelayGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 2, 2, 2, 1)
)
alaDHCPv6RelayGroup.setObjects(
      *(("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6RelayAdminStatus"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6RelayInterfaceAdminStatus"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6RelayDestinationRowStatus"))
)
if mibBuilder.loadTexts:
    alaDHCPv6RelayGroup.setStatus("current")

alaDHCPv6SrvGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 2, 2, 2, 2)
)
alaDHCPv6SrvGroup.setObjects(
      *(("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6SrvGlobalConfigStatus"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6SrvGlobalRestart"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6SrvGlobalClearStat"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6SrvLeaseLeaseGrant"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6SrvLeasePrefLeaseExpiry"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6SrvLeaseValidLeaseExpiry"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6SrvLeaseType"))
)
if mibBuilder.loadTexts:
    alaDHCPv6SrvGroup.setStatus("current")

alaDHCPv6SrvLeaseUtilizationThresholdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 2, 2, 2, 4)
)
alaDHCPv6SrvLeaseUtilizationThresholdGroup.setObjects(
      *(("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6SrvLeaseThresholdStatus"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6SrvSubnetDescriptor"))
)
if mibBuilder.loadTexts:
    alaDHCPv6SrvLeaseUtilizationThresholdGroup.setStatus("current")


# Notification objects

alaDHCPv6SrvLeaseUtilizationThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 2, 0, 1)
)
alaDHCPv6SrvLeaseUtilizationThresholdTrap.setObjects(
      *(("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6SrvLeaseThresholdStatus"),
        ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6SrvSubnetDescriptor"))
)
if mibBuilder.loadTexts:
    alaDHCPv6SrvLeaseUtilizationThresholdTrap.setStatus(
        "current"
    )


# Notifications groups

alaDHCPv6SrvNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 2, 2, 2, 3)
)
alaDHCPv6SrvNotificationsGroup.setObjects(
    ("ALCATEL-IND1-DHCPV6-MIB", "alaDHCPv6SrvLeaseUtilizationThresholdTrap")
)
if mibBuilder.loadTexts:
    alaDHCPv6SrvNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alaDHCPv6Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 29, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    alaDHCPv6Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-DHCPV6-MIB",
    **{"alcatelIND1DHCPv6MIB": alcatelIND1DHCPv6MIB,
       "alcatelIND1DHCPv6MIBNotifications": alcatelIND1DHCPv6MIBNotifications,
       "alaDHCPv6SrvLeaseUtilizationThresholdTrap": alaDHCPv6SrvLeaseUtilizationThresholdTrap,
       "alcatelIND1DHCPv6MIBObjects": alcatelIND1DHCPv6MIBObjects,
       "alaDHCPv6RelayConfig": alaDHCPv6RelayConfig,
       "alaDHCPv6RelayAdminStatus": alaDHCPv6RelayAdminStatus,
       "alaDHCPv6SrvConfig": alaDHCPv6SrvConfig,
       "alaDHCPv6SrvGlobalConfigStatus": alaDHCPv6SrvGlobalConfigStatus,
       "alaDHCPv6SrvGlobalRestart": alaDHCPv6SrvGlobalRestart,
       "alaDHCPv6SrvGlobalClearStat": alaDHCPv6SrvGlobalClearStat,
       "alaDHCPv6RelayInterfaceTable": alaDHCPv6RelayInterfaceTable,
       "alaDHCPv6RelayInterfaceEntry": alaDHCPv6RelayInterfaceEntry,
       "alaDHCPv6RelayInterfaceAdminStatus": alaDHCPv6RelayInterfaceAdminStatus,
       "alaDHCPv6RelayDestinationTable": alaDHCPv6RelayDestinationTable,
       "alaDHCPv6RelayDestinationEntry": alaDHCPv6RelayDestinationEntry,
       "alaDHCPv6RelayDestinationAddressType": alaDHCPv6RelayDestinationAddressType,
       "alaDHCPv6RelayDestinationAddress": alaDHCPv6RelayDestinationAddress,
       "alaDHCPv6RelayDestinationRowStatus": alaDHCPv6RelayDestinationRowStatus,
       "alaDHCPv6SrvLease": alaDHCPv6SrvLease,
       "alaDHCPv6SrvLeaseTable": alaDHCPv6SrvLeaseTable,
       "alaDHCPv6SrvLeaseEntry": alaDHCPv6SrvLeaseEntry,
       "alaDHCPv6SrvLeaseIpv6Address": alaDHCPv6SrvLeaseIpv6Address,
       "alaDHCPv6SrvLeaseLeaseGrant": alaDHCPv6SrvLeaseLeaseGrant,
       "alaDHCPv6SrvLeasePrefLeaseExpiry": alaDHCPv6SrvLeasePrefLeaseExpiry,
       "alaDHCPv6SrvLeaseValidLeaseExpiry": alaDHCPv6SrvLeaseValidLeaseExpiry,
       "alaDHCPv6SrvLeaseType": alaDHCPv6SrvLeaseType,
       "alaDHCPv6SrvTrapsObj": alaDHCPv6SrvTrapsObj,
       "alaDHCPv6SrvLeaseThresholdStatus": alaDHCPv6SrvLeaseThresholdStatus,
       "alaDHCPv6SrvSubnetDescriptor": alaDHCPv6SrvSubnetDescriptor,
       "alcatelIND1DHCPv6MIBConformance": alcatelIND1DHCPv6MIBConformance,
       "alcatelIND1DHCPv6MIBCompliances": alcatelIND1DHCPv6MIBCompliances,
       "alaDHCPv6Compliance": alaDHCPv6Compliance,
       "alcatelIND1DHCPv6MIBGroups": alcatelIND1DHCPv6MIBGroups,
       "alaDHCPv6RelayGroup": alaDHCPv6RelayGroup,
       "alaDHCPv6SrvGroup": alaDHCPv6SrvGroup,
       "alaDHCPv6SrvNotificationsGroup": alaDHCPv6SrvNotificationsGroup,
       "alaDHCPv6SrvLeaseUtilizationThresholdGroup": alaDHCPv6SrvLeaseUtilizationThresholdGroup}
)
