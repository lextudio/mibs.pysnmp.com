# SNMP MIB module (CISCO-L2NAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-L2NAT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:03:48 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CiscoInetAddressMask,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoInetAddressMask")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
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
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

ciscoL2natMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 806)
)
ciscoL2natMIB.setRevisions(
        ("2013-04-16 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoL2natMIBObjects_ObjectIdentity = ObjectIdentity
ciscoL2natMIBObjects = _CiscoL2natMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1)
)
_Cl2natTotalInstances_Type = Counter32
_Cl2natTotalInstances_Object = MibScalar
cl2natTotalInstances = _Cl2natTotalInstances_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 1),
    _Cl2natTotalInstances_Type()
)
cl2natTotalInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cl2natTotalInstances.setStatus("current")
_Cl2natTotalMatched_Type = Counter64
_Cl2natTotalMatched_Object = MibScalar
cl2natTotalMatched = _Cl2natTotalMatched_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 2),
    _Cl2natTotalMatched_Type()
)
cl2natTotalMatched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cl2natTotalMatched.setStatus("current")
_Cl2natTotalUnmatched_Type = Counter64
_Cl2natTotalUnmatched_Object = MibScalar
cl2natTotalUnmatched = _Cl2natTotalUnmatched_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 3),
    _Cl2natTotalUnmatched_Type()
)
cl2natTotalUnmatched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cl2natTotalUnmatched.setStatus("current")
_Cl2natTotalFixups_Type = Counter64
_Cl2natTotalFixups_Object = MibScalar
cl2natTotalFixups = _Cl2natTotalFixups_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 4),
    _Cl2natTotalFixups_Type()
)
cl2natTotalFixups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cl2natTotalFixups.setStatus("current")
_Cl2natTotalTranslationEntryConfigured_Type = Unsigned32
_Cl2natTotalTranslationEntryConfigured_Object = MibScalar
cl2natTotalTranslationEntryConfigured = _Cl2natTotalTranslationEntryConfigured_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 5),
    _Cl2natTotalTranslationEntryConfigured_Type()
)
cl2natTotalTranslationEntryConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cl2natTotalTranslationEntryConfigured.setStatus("current")
_Cl2natTotalPacketTranslated_Type = Counter64
_Cl2natTotalPacketTranslated_Object = MibScalar
cl2natTotalPacketTranslated = _Cl2natTotalPacketTranslated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 6),
    _Cl2natTotalPacketTranslated_Type()
)
cl2natTotalPacketTranslated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cl2natTotalPacketTranslated.setStatus("current")
_Cl2natInstConfigInstanceTable_Object = MibTable
cl2natInstConfigInstanceTable = _Cl2natInstConfigInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 7)
)
if mibBuilder.loadTexts:
    cl2natInstConfigInstanceTable.setStatus("current")
_Cl2natInstConfigInstanceEntry_Object = MibTableRow
cl2natInstConfigInstanceEntry = _Cl2natInstConfigInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 7, 1)
)
cl2natInstConfigInstanceEntry.setIndexNames(
    (0, "CISCO-L2NAT-MIB", "cl2natInstConfigInstanceName"),
)
if mibBuilder.loadTexts:
    cl2natInstConfigInstanceEntry.setStatus("current")


class _Cl2natInstConfigInstanceName_Type(SnmpAdminString):
    """Custom type cl2natInstConfigInstanceName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_Cl2natInstConfigInstanceName_Type.__name__ = "SnmpAdminString"
_Cl2natInstConfigInstanceName_Object = MibTableColumn
cl2natInstConfigInstanceName = _Cl2natInstConfigInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 7, 1, 1),
    _Cl2natInstConfigInstanceName_Type()
)
cl2natInstConfigInstanceName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cl2natInstConfigInstanceName.setStatus("current")


class _Cl2natInstConfigPermitIn_Type(Bits):
    """Custom type cl2natInstConfigPermitIn based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("igmp", 1),
          ("multicast", 2),
          ("unmatched", 0))
    )

_Cl2natInstConfigPermitIn_Type.__name__ = "Bits"
_Cl2natInstConfigPermitIn_Object = MibTableColumn
cl2natInstConfigPermitIn = _Cl2natInstConfigPermitIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 7, 1, 2),
    _Cl2natInstConfigPermitIn_Type()
)
cl2natInstConfigPermitIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cl2natInstConfigPermitIn.setStatus("current")


class _Cl2natInstConfigPermitOut_Type(Bits):
    """Custom type cl2natInstConfigPermitOut based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("igmp", 1),
          ("multicast", 2),
          ("unmatched", 0))
    )

_Cl2natInstConfigPermitOut_Type.__name__ = "Bits"
_Cl2natInstConfigPermitOut_Object = MibTableColumn
cl2natInstConfigPermitOut = _Cl2natInstConfigPermitOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 7, 1, 3),
    _Cl2natInstConfigPermitOut_Type()
)
cl2natInstConfigPermitOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cl2natInstConfigPermitOut.setStatus("current")


class _Cl2natInstConfigFixup_Type(Bits):
    """Custom type cl2natInstConfigFixup based on Bits"""
    defaultBinValue = "1111"

    namedValues = NamedValues(
        *(("arp", 0),
          ("cip", 3),
          ("icmp", 1),
          ("profinet", 2),
          ("snmp", 4))
    )

_Cl2natInstConfigFixup_Type.__name__ = "Bits"
_Cl2natInstConfigFixup_Object = MibTableColumn
cl2natInstConfigFixup = _Cl2natInstConfigFixup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 7, 1, 4),
    _Cl2natInstConfigFixup_Type()
)
cl2natInstConfigFixup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cl2natInstConfigFixup.setStatus("current")
_Cl2natInstConfigStorageType_Type = StorageType
_Cl2natInstConfigStorageType_Object = MibTableColumn
cl2natInstConfigStorageType = _Cl2natInstConfigStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 7, 1, 5),
    _Cl2natInstConfigStorageType_Type()
)
cl2natInstConfigStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cl2natInstConfigStorageType.setStatus("current")
_Cl2natInstConfigInstanceRowStatus_Type = RowStatus
_Cl2natInstConfigInstanceRowStatus_Object = MibTableColumn
cl2natInstConfigInstanceRowStatus = _Cl2natInstConfigInstanceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 7, 1, 6),
    _Cl2natInstConfigInstanceRowStatus_Type()
)
cl2natInstConfigInstanceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cl2natInstConfigInstanceRowStatus.setStatus("current")
_Cl2natInstIpInstanceIpTable_Object = MibTable
cl2natInstIpInstanceIpTable = _Cl2natInstIpInstanceIpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 8)
)
if mibBuilder.loadTexts:
    cl2natInstIpInstanceIpTable.setStatus("current")
_Cl2natInstIpInstanceIpEntry_Object = MibTableRow
cl2natInstIpInstanceIpEntry = _Cl2natInstIpInstanceIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 8, 1)
)
cl2natInstIpInstanceIpEntry.setIndexNames(
    (0, "CISCO-L2NAT-MIB", "cl2natInstConfigInstanceName"),
    (0, "CISCO-L2NAT-MIB", "cl2natInstIpDirection"),
    (0, "CISCO-L2NAT-MIB", "cl2natInstIpFromIpAddressType"),
    (0, "CISCO-L2NAT-MIB", "cl2natInstIpFromIpAddress"),
    (0, "CISCO-L2NAT-MIB", "cl2natInstIpAddressType"),
)
if mibBuilder.loadTexts:
    cl2natInstIpInstanceIpEntry.setStatus("current")


class _Cl2natInstIpDirection_Type(Integer32):
    """Custom type cl2natInstIpDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inside", 1),
          ("outside", 2))
    )


_Cl2natInstIpDirection_Type.__name__ = "Integer32"
_Cl2natInstIpDirection_Object = MibTableColumn
cl2natInstIpDirection = _Cl2natInstIpDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 8, 1, 1),
    _Cl2natInstIpDirection_Type()
)
cl2natInstIpDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cl2natInstIpDirection.setStatus("current")


class _Cl2natInstIpAddressType_Type(Integer32):
    """Custom type cl2natInstIpAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("host", 1),
          ("network", 3),
          ("range", 2))
    )


_Cl2natInstIpAddressType_Type.__name__ = "Integer32"
_Cl2natInstIpAddressType_Object = MibTableColumn
cl2natInstIpAddressType = _Cl2natInstIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 8, 1, 2),
    _Cl2natInstIpAddressType_Type()
)
cl2natInstIpAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cl2natInstIpAddressType.setStatus("current")
_Cl2natInstIpFromIpAddressType_Type = InetAddressType
_Cl2natInstIpFromIpAddressType_Object = MibTableColumn
cl2natInstIpFromIpAddressType = _Cl2natInstIpFromIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 8, 1, 3),
    _Cl2natInstIpFromIpAddressType_Type()
)
cl2natInstIpFromIpAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cl2natInstIpFromIpAddressType.setStatus("current")


class _Cl2natInstIpFromIpAddress_Type(InetAddress):
    """Custom type cl2natInstIpFromIpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_Cl2natInstIpFromIpAddress_Type.__name__ = "InetAddress"
_Cl2natInstIpFromIpAddress_Object = MibTableColumn
cl2natInstIpFromIpAddress = _Cl2natInstIpFromIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 8, 1, 4),
    _Cl2natInstIpFromIpAddress_Type()
)
cl2natInstIpFromIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cl2natInstIpFromIpAddress.setStatus("current")
_Cl2natInstIpToIpAddressType_Type = InetAddressType
_Cl2natInstIpToIpAddressType_Object = MibTableColumn
cl2natInstIpToIpAddressType = _Cl2natInstIpToIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 8, 1, 5),
    _Cl2natInstIpToIpAddressType_Type()
)
cl2natInstIpToIpAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cl2natInstIpToIpAddressType.setStatus("current")


class _Cl2natInstIpToIpAddress_Type(InetAddress):
    """Custom type cl2natInstIpToIpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_Cl2natInstIpToIpAddress_Type.__name__ = "InetAddress"
_Cl2natInstIpToIpAddress_Object = MibTableColumn
cl2natInstIpToIpAddress = _Cl2natInstIpToIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 8, 1, 6),
    _Cl2natInstIpToIpAddress_Type()
)
cl2natInstIpToIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cl2natInstIpToIpAddress.setStatus("current")
_Cl2natInstIpAddressMask_Type = CiscoInetAddressMask
_Cl2natInstIpAddressMask_Object = MibTableColumn
cl2natInstIpAddressMask = _Cl2natInstIpAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 8, 1, 7),
    _Cl2natInstIpAddressMask_Type()
)
cl2natInstIpAddressMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cl2natInstIpAddressMask.setStatus("current")


class _Cl2natInstIpRange_Type(Integer32):
    """Custom type cl2natInstIpRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_Cl2natInstIpRange_Type.__name__ = "Integer32"
_Cl2natInstIpRange_Object = MibTableColumn
cl2natInstIpRange = _Cl2natInstIpRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 8, 1, 8),
    _Cl2natInstIpRange_Type()
)
cl2natInstIpRange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cl2natInstIpRange.setStatus("current")
_Cl2natInstStorageIpStorageType_Type = StorageType
_Cl2natInstStorageIpStorageType_Object = MibTableColumn
cl2natInstStorageIpStorageType = _Cl2natInstStorageIpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 8, 1, 9),
    _Cl2natInstStorageIpStorageType_Type()
)
cl2natInstStorageIpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cl2natInstStorageIpStorageType.setStatus("current")
_Cl2natInstIpRowStatus_Type = RowStatus
_Cl2natInstIpRowStatus_Object = MibTableColumn
cl2natInstIpRowStatus = _Cl2natInstIpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 8, 1, 10),
    _Cl2natInstIpRowStatus_Type()
)
cl2natInstIpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cl2natInstIpRowStatus.setStatus("current")
_Cl2natInterfaceConfigTable_Object = MibTable
cl2natInterfaceConfigTable = _Cl2natInterfaceConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 9)
)
if mibBuilder.loadTexts:
    cl2natInterfaceConfigTable.setStatus("current")
_Cl2natInterfaceConfigEntry_Object = MibTableRow
cl2natInterfaceConfigEntry = _Cl2natInterfaceConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 9, 1)
)
cl2natInterfaceConfigEntry.setIndexNames(
    (0, "CISCO-L2NAT-MIB", "cl2natInterfaceConfigIfIndex"),
    (0, "CISCO-L2NAT-MIB", "cl2natInterfaceConfigVlanIndex"),
)
if mibBuilder.loadTexts:
    cl2natInterfaceConfigEntry.setStatus("current")
_Cl2natInterfaceConfigIfIndex_Type = Unsigned32
_Cl2natInterfaceConfigIfIndex_Object = MibTableColumn
cl2natInterfaceConfigIfIndex = _Cl2natInterfaceConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 9, 1, 1),
    _Cl2natInterfaceConfigIfIndex_Type()
)
cl2natInterfaceConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cl2natInterfaceConfigIfIndex.setStatus("current")
_Cl2natInterfaceConfigVlanIndex_Type = Unsigned32
_Cl2natInterfaceConfigVlanIndex_Object = MibTableColumn
cl2natInterfaceConfigVlanIndex = _Cl2natInterfaceConfigVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 9, 1, 2),
    _Cl2natInterfaceConfigVlanIndex_Type()
)
cl2natInterfaceConfigVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cl2natInterfaceConfigVlanIndex.setStatus("current")


class _Cl2natInterfaceConfigInstanceName_Type(SnmpAdminString):
    """Custom type cl2natInterfaceConfigInstanceName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_Cl2natInterfaceConfigInstanceName_Type.__name__ = "SnmpAdminString"
_Cl2natInterfaceConfigInstanceName_Object = MibTableColumn
cl2natInterfaceConfigInstanceName = _Cl2natInterfaceConfigInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 9, 1, 3),
    _Cl2natInterfaceConfigInstanceName_Type()
)
cl2natInterfaceConfigInstanceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cl2natInterfaceConfigInstanceName.setStatus("current")
_Cl2natInterfaceConfigStorageType_Type = StorageType
_Cl2natInterfaceConfigStorageType_Object = MibTableColumn
cl2natInterfaceConfigStorageType = _Cl2natInterfaceConfigStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 9, 1, 4),
    _Cl2natInterfaceConfigStorageType_Type()
)
cl2natInterfaceConfigStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cl2natInterfaceConfigStorageType.setStatus("current")
_Cl2natInterfaceConfigRowStatus_Type = RowStatus
_Cl2natInterfaceConfigRowStatus_Object = MibTableColumn
cl2natInterfaceConfigRowStatus = _Cl2natInterfaceConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 9, 1, 5),
    _Cl2natInterfaceConfigRowStatus_Type()
)
cl2natInterfaceConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cl2natInterfaceConfigRowStatus.setStatus("current")
_Cl2natInterfaceStatisticsTable_Object = MibTable
cl2natInterfaceStatisticsTable = _Cl2natInterfaceStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 10)
)
if mibBuilder.loadTexts:
    cl2natInterfaceStatisticsTable.setStatus("current")
_Cl2natInterfaceStatisticsEntry_Object = MibTableRow
cl2natInterfaceStatisticsEntry = _Cl2natInterfaceStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 10, 1)
)
cl2natInterfaceStatisticsEntry.setIndexNames(
    (0, "CISCO-L2NAT-MIB", "cl2natInterfaceConfigIfIndex"),
    (0, "CISCO-L2NAT-MIB", "cl2natInterfaceConfigVlanIndex"),
)
if mibBuilder.loadTexts:
    cl2natInterfaceStatisticsEntry.setStatus("current")
_Cl2natFixupArpIn_Type = Counter64
_Cl2natFixupArpIn_Object = MibTableColumn
cl2natFixupArpIn = _Cl2natFixupArpIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 10, 1, 1),
    _Cl2natFixupArpIn_Type()
)
cl2natFixupArpIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cl2natFixupArpIn.setStatus("current")
_Cl2natFixupIcmpIn_Type = Counter64
_Cl2natFixupIcmpIn_Object = MibTableColumn
cl2natFixupIcmpIn = _Cl2natFixupIcmpIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 10, 1, 2),
    _Cl2natFixupIcmpIn_Type()
)
cl2natFixupIcmpIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cl2natFixupIcmpIn.setStatus("current")
_Cl2natFixupCipIn_Type = Counter64
_Cl2natFixupCipIn_Object = MibTableColumn
cl2natFixupCipIn = _Cl2natFixupCipIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 10, 1, 3),
    _Cl2natFixupCipIn_Type()
)
cl2natFixupCipIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cl2natFixupCipIn.setStatus("current")
_Cl2natFixupProfinetIn_Type = Counter64
_Cl2natFixupProfinetIn_Object = MibTableColumn
cl2natFixupProfinetIn = _Cl2natFixupProfinetIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 10, 1, 4),
    _Cl2natFixupProfinetIn_Type()
)
cl2natFixupProfinetIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cl2natFixupProfinetIn.setStatus("current")
_Cl2natFixupFtpIn_Type = Counter64
_Cl2natFixupFtpIn_Object = MibTableColumn
cl2natFixupFtpIn = _Cl2natFixupFtpIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 10, 1, 5),
    _Cl2natFixupFtpIn_Type()
)
cl2natFixupFtpIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cl2natFixupFtpIn.setStatus("current")
_Cl2natFixupSnmpIn_Type = Counter64
_Cl2natFixupSnmpIn_Object = MibTableColumn
cl2natFixupSnmpIn = _Cl2natFixupSnmpIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 10, 1, 6),
    _Cl2natFixupSnmpIn_Type()
)
cl2natFixupSnmpIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cl2natFixupSnmpIn.setStatus("current")
_Cl2natFixupSipIn_Type = Counter64
_Cl2natFixupSipIn_Object = MibTableColumn
cl2natFixupSipIn = _Cl2natFixupSipIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 10, 1, 7),
    _Cl2natFixupSipIn_Type()
)
cl2natFixupSipIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cl2natFixupSipIn.setStatus("current")
_Cl2natFixupSccpIn_Type = Counter64
_Cl2natFixupSccpIn_Object = MibTableColumn
cl2natFixupSccpIn = _Cl2natFixupSccpIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 10, 1, 8),
    _Cl2natFixupSccpIn_Type()
)
cl2natFixupSccpIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cl2natFixupSccpIn.setStatus("current")
_Cl2natUnmatchedIn_Type = Counter64
_Cl2natUnmatchedIn_Object = MibTableColumn
cl2natUnmatchedIn = _Cl2natUnmatchedIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 10, 1, 9),
    _Cl2natUnmatchedIn_Type()
)
cl2natUnmatchedIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cl2natUnmatchedIn.setStatus("current")
_Cl2natTranslatedUnicastIn_Type = Counter64
_Cl2natTranslatedUnicastIn_Object = MibTableColumn
cl2natTranslatedUnicastIn = _Cl2natTranslatedUnicastIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 10, 1, 10),
    _Cl2natTranslatedUnicastIn_Type()
)
cl2natTranslatedUnicastIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cl2natTranslatedUnicastIn.setStatus("current")
_Cl2natDroppedUnicastIn_Type = Counter64
_Cl2natDroppedUnicastIn_Object = MibTableColumn
cl2natDroppedUnicastIn = _Cl2natDroppedUnicastIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 10, 1, 11),
    _Cl2natDroppedUnicastIn_Type()
)
cl2natDroppedUnicastIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cl2natDroppedUnicastIn.setStatus("current")
_Cl2natDroppedMulticastIn_Type = Counter64
_Cl2natDroppedMulticastIn_Object = MibTableColumn
cl2natDroppedMulticastIn = _Cl2natDroppedMulticastIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 10, 1, 12),
    _Cl2natDroppedMulticastIn_Type()
)
cl2natDroppedMulticastIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cl2natDroppedMulticastIn.setStatus("current")
_Cl2natPassThruUnicastIn_Type = Counter64
_Cl2natPassThruUnicastIn_Object = MibTableColumn
cl2natPassThruUnicastIn = _Cl2natPassThruUnicastIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 10, 1, 13),
    _Cl2natPassThruUnicastIn_Type()
)
cl2natPassThruUnicastIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cl2natPassThruUnicastIn.setStatus("current")
_Cl2natPassThruMulticastIn_Type = Counter64
_Cl2natPassThruMulticastIn_Object = MibTableColumn
cl2natPassThruMulticastIn = _Cl2natPassThruMulticastIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 10, 1, 14),
    _Cl2natPassThruMulticastIn_Type()
)
cl2natPassThruMulticastIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cl2natPassThruMulticastIn.setStatus("current")
_Cl2natPassThruIgmpIn_Type = Counter64
_Cl2natPassThruIgmpIn_Object = MibTableColumn
cl2natPassThruIgmpIn = _Cl2natPassThruIgmpIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 10, 1, 15),
    _Cl2natPassThruIgmpIn_Type()
)
cl2natPassThruIgmpIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cl2natPassThruIgmpIn.setStatus("current")
_Cl2natDroppedIgmpIn_Type = Counter64
_Cl2natDroppedIgmpIn_Object = MibTableColumn
cl2natDroppedIgmpIn = _Cl2natDroppedIgmpIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 10, 1, 16),
    _Cl2natDroppedIgmpIn_Type()
)
cl2natDroppedIgmpIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cl2natDroppedIgmpIn.setStatus("current")
_Cl2natFixupArpOut_Type = Counter64
_Cl2natFixupArpOut_Object = MibTableColumn
cl2natFixupArpOut = _Cl2natFixupArpOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 10, 1, 17),
    _Cl2natFixupArpOut_Type()
)
cl2natFixupArpOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cl2natFixupArpOut.setStatus("current")
_Cl2natFixupIcmpOut_Type = Counter64
_Cl2natFixupIcmpOut_Object = MibTableColumn
cl2natFixupIcmpOut = _Cl2natFixupIcmpOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 10, 1, 18),
    _Cl2natFixupIcmpOut_Type()
)
cl2natFixupIcmpOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cl2natFixupIcmpOut.setStatus("current")
_Cl2natFixupCipOut_Type = Counter64
_Cl2natFixupCipOut_Object = MibTableColumn
cl2natFixupCipOut = _Cl2natFixupCipOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 10, 1, 19),
    _Cl2natFixupCipOut_Type()
)
cl2natFixupCipOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cl2natFixupCipOut.setStatus("current")
_Cl2natFixupProfinetOut_Type = Counter64
_Cl2natFixupProfinetOut_Object = MibTableColumn
cl2natFixupProfinetOut = _Cl2natFixupProfinetOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 10, 1, 20),
    _Cl2natFixupProfinetOut_Type()
)
cl2natFixupProfinetOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cl2natFixupProfinetOut.setStatus("current")
_Cl2natFixupFtpOut_Type = Counter64
_Cl2natFixupFtpOut_Object = MibTableColumn
cl2natFixupFtpOut = _Cl2natFixupFtpOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 10, 1, 21),
    _Cl2natFixupFtpOut_Type()
)
cl2natFixupFtpOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cl2natFixupFtpOut.setStatus("current")
_Cl2natFixupSnmpOut_Type = Counter64
_Cl2natFixupSnmpOut_Object = MibTableColumn
cl2natFixupSnmpOut = _Cl2natFixupSnmpOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 10, 1, 22),
    _Cl2natFixupSnmpOut_Type()
)
cl2natFixupSnmpOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cl2natFixupSnmpOut.setStatus("current")
_Cl2natFixupSipOut_Type = Counter64
_Cl2natFixupSipOut_Object = MibTableColumn
cl2natFixupSipOut = _Cl2natFixupSipOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 10, 1, 23),
    _Cl2natFixupSipOut_Type()
)
cl2natFixupSipOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cl2natFixupSipOut.setStatus("current")
_Cl2natFixupSccpOut_Type = Counter64
_Cl2natFixupSccpOut_Object = MibTableColumn
cl2natFixupSccpOut = _Cl2natFixupSccpOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 10, 1, 24),
    _Cl2natFixupSccpOut_Type()
)
cl2natFixupSccpOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cl2natFixupSccpOut.setStatus("current")
_Cl2natUnmatchedOut_Type = Counter64
_Cl2natUnmatchedOut_Object = MibTableColumn
cl2natUnmatchedOut = _Cl2natUnmatchedOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 10, 1, 25),
    _Cl2natUnmatchedOut_Type()
)
cl2natUnmatchedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cl2natUnmatchedOut.setStatus("current")
_Cl2natDroppedUnicastOut_Type = Counter64
_Cl2natDroppedUnicastOut_Object = MibTableColumn
cl2natDroppedUnicastOut = _Cl2natDroppedUnicastOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 10, 1, 26),
    _Cl2natDroppedUnicastOut_Type()
)
cl2natDroppedUnicastOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cl2natDroppedUnicastOut.setStatus("current")
_Cl2natTranslatedUnicastOut_Type = Counter64
_Cl2natTranslatedUnicastOut_Object = MibTableColumn
cl2natTranslatedUnicastOut = _Cl2natTranslatedUnicastOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 10, 1, 27),
    _Cl2natTranslatedUnicastOut_Type()
)
cl2natTranslatedUnicastOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cl2natTranslatedUnicastOut.setStatus("current")
_Cl2natPassThruUnicastOut_Type = Counter64
_Cl2natPassThruUnicastOut_Object = MibTableColumn
cl2natPassThruUnicastOut = _Cl2natPassThruUnicastOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 10, 1, 28),
    _Cl2natPassThruUnicastOut_Type()
)
cl2natPassThruUnicastOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cl2natPassThruUnicastOut.setStatus("current")
_Cl2natDroppedMulticastOut_Type = Counter64
_Cl2natDroppedMulticastOut_Object = MibTableColumn
cl2natDroppedMulticastOut = _Cl2natDroppedMulticastOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 10, 1, 29),
    _Cl2natDroppedMulticastOut_Type()
)
cl2natDroppedMulticastOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cl2natDroppedMulticastOut.setStatus("current")
_Cl2natPassThruMulticastOut_Type = Counter64
_Cl2natPassThruMulticastOut_Object = MibTableColumn
cl2natPassThruMulticastOut = _Cl2natPassThruMulticastOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 10, 1, 30),
    _Cl2natPassThruMulticastOut_Type()
)
cl2natPassThruMulticastOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cl2natPassThruMulticastOut.setStatus("current")
_Cl2natDroppedIgmpOut_Type = Counter64
_Cl2natDroppedIgmpOut_Object = MibTableColumn
cl2natDroppedIgmpOut = _Cl2natDroppedIgmpOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 10, 1, 31),
    _Cl2natDroppedIgmpOut_Type()
)
cl2natDroppedIgmpOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cl2natDroppedIgmpOut.setStatus("current")
_Cl2natPassThruIgmpOut_Type = Counter64
_Cl2natPassThruIgmpOut_Object = MibTableColumn
cl2natPassThruIgmpOut = _Cl2natPassThruIgmpOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 10, 1, 32),
    _Cl2natPassThruIgmpOut_Type()
)
cl2natPassThruIgmpOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cl2natPassThruIgmpOut.setStatus("current")
_Cl2natInterfaceIpStatisticsTable_Object = MibTable
cl2natInterfaceIpStatisticsTable = _Cl2natInterfaceIpStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 11)
)
if mibBuilder.loadTexts:
    cl2natInterfaceIpStatisticsTable.setStatus("current")
_Cl2natInterfaceIpStatisticsEntry_Object = MibTableRow
cl2natInterfaceIpStatisticsEntry = _Cl2natInterfaceIpStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 11, 1)
)
cl2natInterfaceIpStatisticsEntry.setIndexNames(
    (0, "CISCO-L2NAT-MIB", "cl2natInterfaceConfigIfIndex"),
    (0, "CISCO-L2NAT-MIB", "cl2natInterfaceConfigVlanIndex"),
    (0, "CISCO-L2NAT-MIB", "cl2natInstIpDirection"),
    (0, "CISCO-L2NAT-MIB", "cl2natInstIpFromIpAddressType"),
    (0, "CISCO-L2NAT-MIB", "cl2natInstIpFromIpAddress"),
)
if mibBuilder.loadTexts:
    cl2natInterfaceIpStatisticsEntry.setStatus("current")
_Cl2natTranslatesIn_Type = Counter64
_Cl2natTranslatesIn_Object = MibTableColumn
cl2natTranslatesIn = _Cl2natTranslatesIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 11, 1, 1),
    _Cl2natTranslatesIn_Type()
)
cl2natTranslatesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cl2natTranslatesIn.setStatus("current")
_Cl2natTranslatesOut_Type = Counter64
_Cl2natTranslatesOut_Object = MibTableColumn
cl2natTranslatesOut = _Cl2natTranslatesOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 1, 11, 1, 2),
    _Cl2natTranslatesOut_Type()
)
cl2natTranslatesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cl2natTranslatesOut.setStatus("current")
_CiscoL2natMIBConformance_ObjectIdentity = ObjectIdentity
ciscoL2natMIBConformance = _CiscoL2natMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 3)
)
_CiscoL2natMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoL2natMIBCompliances = _CiscoL2natMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 3, 1)
)
_CiscoL2natMIBGroups_ObjectIdentity = ObjectIdentity
ciscoL2natMIBGroups = _CiscoL2natMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 3, 2)
)

# Managed Objects groups

cl2natGlobalStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 3, 2, 1)
)
cl2natGlobalStatisticsGroup.setObjects(
      *(("CISCO-L2NAT-MIB", "cl2natTotalInstances"),
        ("CISCO-L2NAT-MIB", "cl2natTotalMatched"),
        ("CISCO-L2NAT-MIB", "cl2natTotalUnmatched"),
        ("CISCO-L2NAT-MIB", "cl2natTotalFixups"),
        ("CISCO-L2NAT-MIB", "cl2natTotalTranslationEntryConfigured"),
        ("CISCO-L2NAT-MIB", "cl2natTotalPacketTranslated"))
)
if mibBuilder.loadTexts:
    cl2natGlobalStatisticsGroup.setStatus("current")

cl2natInstanceConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 3, 2, 2)
)
cl2natInstanceConfigGroup.setObjects(
      *(("CISCO-L2NAT-MIB", "cl2natInstConfigPermitIn"),
        ("CISCO-L2NAT-MIB", "cl2natInstConfigPermitOut"),
        ("CISCO-L2NAT-MIB", "cl2natInstConfigFixup"),
        ("CISCO-L2NAT-MIB", "cl2natInstIpRange"),
        ("CISCO-L2NAT-MIB", "cl2natInstIpToIpAddress"),
        ("CISCO-L2NAT-MIB", "cl2natInstIpToIpAddressType"),
        ("CISCO-L2NAT-MIB", "cl2natInstConfigInstanceRowStatus"),
        ("CISCO-L2NAT-MIB", "cl2natInterfaceConfigRowStatus"),
        ("CISCO-L2NAT-MIB", "cl2natInstIpAddressMask"),
        ("CISCO-L2NAT-MIB", "cl2natInterfaceConfigInstanceName"),
        ("CISCO-L2NAT-MIB", "cl2natInstIpRowStatus"),
        ("CISCO-L2NAT-MIB", "cl2natInstConfigStorageType"),
        ("CISCO-L2NAT-MIB", "cl2natInstStorageIpStorageType"),
        ("CISCO-L2NAT-MIB", "cl2natInterfaceConfigStorageType"))
)
if mibBuilder.loadTexts:
    cl2natInstanceConfigGroup.setStatus("current")

cl2natInstanceStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 3, 2, 3)
)
cl2natInstanceStatisticsGroup.setObjects(
      *(("CISCO-L2NAT-MIB", "cl2natUnmatchedIn"),
        ("CISCO-L2NAT-MIB", "cl2natDroppedUnicastIn"),
        ("CISCO-L2NAT-MIB", "cl2natTranslatedUnicastIn"),
        ("CISCO-L2NAT-MIB", "cl2natFixupArpIn"),
        ("CISCO-L2NAT-MIB", "cl2natFixupIcmpIn"),
        ("CISCO-L2NAT-MIB", "cl2natFixupCipIn"),
        ("CISCO-L2NAT-MIB", "cl2natFixupProfinetIn"),
        ("CISCO-L2NAT-MIB", "cl2natFixupFtpIn"),
        ("CISCO-L2NAT-MIB", "cl2natFixupSnmpIn"),
        ("CISCO-L2NAT-MIB", "cl2natFixupSipIn"),
        ("CISCO-L2NAT-MIB", "cl2natFixupSccpIn"),
        ("CISCO-L2NAT-MIB", "cl2natUnmatchedOut"),
        ("CISCO-L2NAT-MIB", "cl2natDroppedUnicastOut"),
        ("CISCO-L2NAT-MIB", "cl2natTranslatedUnicastOut"),
        ("CISCO-L2NAT-MIB", "cl2natFixupArpOut"),
        ("CISCO-L2NAT-MIB", "cl2natFixupIcmpOut"),
        ("CISCO-L2NAT-MIB", "cl2natFixupCipOut"),
        ("CISCO-L2NAT-MIB", "cl2natFixupProfinetOut"),
        ("CISCO-L2NAT-MIB", "cl2natFixupFtpOut"),
        ("CISCO-L2NAT-MIB", "cl2natFixupSnmpOut"),
        ("CISCO-L2NAT-MIB", "cl2natFixupSipOut"),
        ("CISCO-L2NAT-MIB", "cl2natFixupSccpOut"),
        ("CISCO-L2NAT-MIB", "cl2natPassThruUnicastIn"),
        ("CISCO-L2NAT-MIB", "cl2natPassThruUnicastOut"),
        ("CISCO-L2NAT-MIB", "cl2natDroppedMulticastIn"),
        ("CISCO-L2NAT-MIB", "cl2natDroppedMulticastOut"),
        ("CISCO-L2NAT-MIB", "cl2natPassThruMulticastIn"),
        ("CISCO-L2NAT-MIB", "cl2natPassThruMulticastOut"),
        ("CISCO-L2NAT-MIB", "cl2natDroppedIgmpIn"),
        ("CISCO-L2NAT-MIB", "cl2natDroppedIgmpOut"),
        ("CISCO-L2NAT-MIB", "cl2natPassThruIgmpIn"),
        ("CISCO-L2NAT-MIB", "cl2natPassThruIgmpOut"))
)
if mibBuilder.loadTexts:
    cl2natInstanceStatisticsGroup.setStatus("current")

cl2natInstanceTranslationStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 3, 2, 4)
)
cl2natInstanceTranslationStatisticsGroup.setObjects(
      *(("CISCO-L2NAT-MIB", "cl2natTranslatesIn"),
        ("CISCO-L2NAT-MIB", "cl2natTranslatesOut"))
)
if mibBuilder.loadTexts:
    cl2natInstanceTranslationStatisticsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoL2natMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 806, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoL2natMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-L2NAT-MIB",
    **{"ciscoL2natMIB": ciscoL2natMIB,
       "ciscoL2natMIBObjects": ciscoL2natMIBObjects,
       "cl2natTotalInstances": cl2natTotalInstances,
       "cl2natTotalMatched": cl2natTotalMatched,
       "cl2natTotalUnmatched": cl2natTotalUnmatched,
       "cl2natTotalFixups": cl2natTotalFixups,
       "cl2natTotalTranslationEntryConfigured": cl2natTotalTranslationEntryConfigured,
       "cl2natTotalPacketTranslated": cl2natTotalPacketTranslated,
       "cl2natInstConfigInstanceTable": cl2natInstConfigInstanceTable,
       "cl2natInstConfigInstanceEntry": cl2natInstConfigInstanceEntry,
       "cl2natInstConfigInstanceName": cl2natInstConfigInstanceName,
       "cl2natInstConfigPermitIn": cl2natInstConfigPermitIn,
       "cl2natInstConfigPermitOut": cl2natInstConfigPermitOut,
       "cl2natInstConfigFixup": cl2natInstConfigFixup,
       "cl2natInstConfigStorageType": cl2natInstConfigStorageType,
       "cl2natInstConfigInstanceRowStatus": cl2natInstConfigInstanceRowStatus,
       "cl2natInstIpInstanceIpTable": cl2natInstIpInstanceIpTable,
       "cl2natInstIpInstanceIpEntry": cl2natInstIpInstanceIpEntry,
       "cl2natInstIpDirection": cl2natInstIpDirection,
       "cl2natInstIpAddressType": cl2natInstIpAddressType,
       "cl2natInstIpFromIpAddressType": cl2natInstIpFromIpAddressType,
       "cl2natInstIpFromIpAddress": cl2natInstIpFromIpAddress,
       "cl2natInstIpToIpAddressType": cl2natInstIpToIpAddressType,
       "cl2natInstIpToIpAddress": cl2natInstIpToIpAddress,
       "cl2natInstIpAddressMask": cl2natInstIpAddressMask,
       "cl2natInstIpRange": cl2natInstIpRange,
       "cl2natInstStorageIpStorageType": cl2natInstStorageIpStorageType,
       "cl2natInstIpRowStatus": cl2natInstIpRowStatus,
       "cl2natInterfaceConfigTable": cl2natInterfaceConfigTable,
       "cl2natInterfaceConfigEntry": cl2natInterfaceConfigEntry,
       "cl2natInterfaceConfigIfIndex": cl2natInterfaceConfigIfIndex,
       "cl2natInterfaceConfigVlanIndex": cl2natInterfaceConfigVlanIndex,
       "cl2natInterfaceConfigInstanceName": cl2natInterfaceConfigInstanceName,
       "cl2natInterfaceConfigStorageType": cl2natInterfaceConfigStorageType,
       "cl2natInterfaceConfigRowStatus": cl2natInterfaceConfigRowStatus,
       "cl2natInterfaceStatisticsTable": cl2natInterfaceStatisticsTable,
       "cl2natInterfaceStatisticsEntry": cl2natInterfaceStatisticsEntry,
       "cl2natFixupArpIn": cl2natFixupArpIn,
       "cl2natFixupIcmpIn": cl2natFixupIcmpIn,
       "cl2natFixupCipIn": cl2natFixupCipIn,
       "cl2natFixupProfinetIn": cl2natFixupProfinetIn,
       "cl2natFixupFtpIn": cl2natFixupFtpIn,
       "cl2natFixupSnmpIn": cl2natFixupSnmpIn,
       "cl2natFixupSipIn": cl2natFixupSipIn,
       "cl2natFixupSccpIn": cl2natFixupSccpIn,
       "cl2natUnmatchedIn": cl2natUnmatchedIn,
       "cl2natTranslatedUnicastIn": cl2natTranslatedUnicastIn,
       "cl2natDroppedUnicastIn": cl2natDroppedUnicastIn,
       "cl2natDroppedMulticastIn": cl2natDroppedMulticastIn,
       "cl2natPassThruUnicastIn": cl2natPassThruUnicastIn,
       "cl2natPassThruMulticastIn": cl2natPassThruMulticastIn,
       "cl2natPassThruIgmpIn": cl2natPassThruIgmpIn,
       "cl2natDroppedIgmpIn": cl2natDroppedIgmpIn,
       "cl2natFixupArpOut": cl2natFixupArpOut,
       "cl2natFixupIcmpOut": cl2natFixupIcmpOut,
       "cl2natFixupCipOut": cl2natFixupCipOut,
       "cl2natFixupProfinetOut": cl2natFixupProfinetOut,
       "cl2natFixupFtpOut": cl2natFixupFtpOut,
       "cl2natFixupSnmpOut": cl2natFixupSnmpOut,
       "cl2natFixupSipOut": cl2natFixupSipOut,
       "cl2natFixupSccpOut": cl2natFixupSccpOut,
       "cl2natUnmatchedOut": cl2natUnmatchedOut,
       "cl2natDroppedUnicastOut": cl2natDroppedUnicastOut,
       "cl2natTranslatedUnicastOut": cl2natTranslatedUnicastOut,
       "cl2natPassThruUnicastOut": cl2natPassThruUnicastOut,
       "cl2natDroppedMulticastOut": cl2natDroppedMulticastOut,
       "cl2natPassThruMulticastOut": cl2natPassThruMulticastOut,
       "cl2natDroppedIgmpOut": cl2natDroppedIgmpOut,
       "cl2natPassThruIgmpOut": cl2natPassThruIgmpOut,
       "cl2natInterfaceIpStatisticsTable": cl2natInterfaceIpStatisticsTable,
       "cl2natInterfaceIpStatisticsEntry": cl2natInterfaceIpStatisticsEntry,
       "cl2natTranslatesIn": cl2natTranslatesIn,
       "cl2natTranslatesOut": cl2natTranslatesOut,
       "ciscoL2natMIBConformance": ciscoL2natMIBConformance,
       "ciscoL2natMIBCompliances": ciscoL2natMIBCompliances,
       "ciscoL2natMIBCompliance": ciscoL2natMIBCompliance,
       "ciscoL2natMIBGroups": ciscoL2natMIBGroups,
       "cl2natGlobalStatisticsGroup": cl2natGlobalStatisticsGroup,
       "cl2natInstanceConfigGroup": cl2natInstanceConfigGroup,
       "cl2natInstanceStatisticsGroup": cl2natInstanceStatisticsGroup,
       "cl2natInstanceTranslationStatisticsGroup": cl2natInstanceTranslationStatisticsGroup}
)
