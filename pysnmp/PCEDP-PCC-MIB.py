# SNMP MIB module (PCEDP-PCC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PCEDP-PCC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:37:09 2024
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

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

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
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

pcedpPccMIB = ModuleIdentity(
    (1, 3, 6, 1, 3, 10000)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PcedpPccNotifications_ObjectIdentity = ObjectIdentity
pcedpPccNotifications = _PcedpPccNotifications_ObjectIdentity(
    (1, 3, 6, 1, 3, 10000, 0)
)
_PcedpPccMIBObjects_ObjectIdentity = ObjectIdentity
pcedpPccMIBObjects = _PcedpPccMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 3, 10000, 1)
)
_PcedpPccDiscoveryGroup_ObjectIdentity = ObjectIdentity
pcedpPccDiscoveryGroup = _PcedpPccDiscoveryGroup_ObjectIdentity(
    (1, 3, 6, 1, 3, 10000, 1, 1)
)


class _PcedpPccPceDiscoveryAdminStatus_Type(Integer32):
    """Custom type pcedpPccPceDiscoveryAdminStatus based on Integer32"""
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


_PcedpPccPceDiscoveryAdminStatus_Type.__name__ = "Integer32"
_PcedpPccPceDiscoveryAdminStatus_Object = MibScalar
pcedpPccPceDiscoveryAdminStatus = _PcedpPccPceDiscoveryAdminStatus_Object(
    (1, 3, 6, 1, 3, 10000, 1, 1, 1),
    _PcedpPccPceDiscoveryAdminStatus_Type()
)
pcedpPccPceDiscoveryAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pcedpPccPceDiscoveryAdminStatus.setStatus("current")
_PcedpPccPceDiscoveryTable_Object = MibTable
pcedpPccPceDiscoveryTable = _PcedpPccPceDiscoveryTable_Object(
    (1, 3, 6, 1, 3, 10000, 1, 1, 2)
)
if mibBuilder.loadTexts:
    pcedpPccPceDiscoveryTable.setStatus("current")
_PcedpPccPceDiscoveryEntry_Object = MibTableRow
pcedpPccPceDiscoveryEntry = _PcedpPccPceDiscoveryEntry_Object(
    (1, 3, 6, 1, 3, 10000, 1, 1, 2, 1)
)
pcedpPccPceDiscoveryEntry.setIndexNames(
    (0, "PCEDP-PCC-MIB", "pcedpPccPceIndex"),
)
if mibBuilder.loadTexts:
    pcedpPccPceDiscoveryEntry.setStatus("current")


class _PcedpPccPceIndex_Type(Integer32):
    """Custom type pcedpPccPceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PcedpPccPceIndex_Type.__name__ = "Integer32"
_PcedpPccPceIndex_Object = MibTableColumn
pcedpPccPceIndex = _PcedpPccPceIndex_Object(
    (1, 3, 6, 1, 3, 10000, 1, 1, 2, 1, 1),
    _PcedpPccPceIndex_Type()
)
pcedpPccPceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pcedpPccPceIndex.setStatus("current")
_PcedpPccPceIPv4Address_Type = IpAddress
_PcedpPccPceIPv4Address_Object = MibTableColumn
pcedpPccPceIPv4Address = _PcedpPccPceIPv4Address_Object(
    (1, 3, 6, 1, 3, 10000, 1, 1, 2, 1, 2),
    _PcedpPccPceIPv4Address_Type()
)
pcedpPccPceIPv4Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcedpPccPceIPv4Address.setStatus("current")
_PcedpPccPceIPv6Address_Type = Ipv6Address
_PcedpPccPceIPv6Address_Object = MibTableColumn
pcedpPccPceIPv6Address = _PcedpPccPceIPv6Address_Object(
    (1, 3, 6, 1, 3, 10000, 1, 1, 2, 1, 3),
    _PcedpPccPceIPv6Address_Type()
)
pcedpPccPceIPv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcedpPccPceIPv6Address.setStatus("current")
_PcedpPccPceTimeDiscovered_Type = TimeStamp
_PcedpPccPceTimeDiscovered_Object = MibTableColumn
pcedpPccPceTimeDiscovered = _PcedpPccPceTimeDiscovered_Object(
    (1, 3, 6, 1, 3, 10000, 1, 1, 2, 1, 4),
    _PcedpPccPceTimeDiscovered_Type()
)
pcedpPccPceTimeDiscovered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcedpPccPceTimeDiscovered.setStatus("current")
_PcedpPccPceLastUpdated_Type = TimeStamp
_PcedpPccPceLastUpdated_Object = MibTableColumn
pcedpPccPceLastUpdated = _PcedpPccPceLastUpdated_Object(
    (1, 3, 6, 1, 3, 10000, 1, 1, 2, 1, 5),
    _PcedpPccPceLastUpdated_Type()
)
pcedpPccPceLastUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcedpPccPceLastUpdated.setStatus("current")
_PcedpPccPcesCapabilityGroup_ObjectIdentity = ObjectIdentity
pcedpPccPcesCapabilityGroup = _PcedpPccPcesCapabilityGroup_ObjectIdentity(
    (1, 3, 6, 1, 3, 10000, 1, 2)
)
_PcedpPccPcesActivityGroup_ObjectIdentity = ObjectIdentity
pcedpPccPcesActivityGroup = _PcedpPccPcesActivityGroup_ObjectIdentity(
    (1, 3, 6, 1, 3, 10000, 1, 3)
)
_PcedpPccConformance_ObjectIdentity = ObjectIdentity
pcedpPccConformance = _PcedpPccConformance_ObjectIdentity(
    (1, 3, 6, 1, 3, 10000, 2)
)
_PcedpPccGroups_ObjectIdentity = ObjectIdentity
pcedpPccGroups = _PcedpPccGroups_ObjectIdentity(
    (1, 3, 6, 1, 3, 10000, 2, 1)
)
_PcedpPccCompliances_ObjectIdentity = ObjectIdentity
pcedpPccCompliances = _PcedpPccCompliances_ObjectIdentity(
    (1, 3, 6, 1, 3, 10000, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pcedpPccGeneralPceInformation = ModuleCompliance(
    (1, 3, 6, 1, 3, 10000, 2, 2, 1)
)
if mibBuilder.loadTexts:
    pcedpPccGeneralPceInformation.setStatus(
        "current"
    )

pcedpPccDetailledPceInformation = ModuleCompliance(
    (1, 3, 6, 1, 3, 10000, 2, 2, 2)
)
if mibBuilder.loadTexts:
    pcedpPccDetailledPceInformation.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PCEDP-PCC-MIB",
    **{"pcedpPccMIB": pcedpPccMIB,
       "pcedpPccNotifications": pcedpPccNotifications,
       "pcedpPccMIBObjects": pcedpPccMIBObjects,
       "pcedpPccDiscoveryGroup": pcedpPccDiscoveryGroup,
       "pcedpPccPceDiscoveryAdminStatus": pcedpPccPceDiscoveryAdminStatus,
       "pcedpPccPceDiscoveryTable": pcedpPccPceDiscoveryTable,
       "pcedpPccPceDiscoveryEntry": pcedpPccPceDiscoveryEntry,
       "pcedpPccPceIndex": pcedpPccPceIndex,
       "pcedpPccPceIPv4Address": pcedpPccPceIPv4Address,
       "pcedpPccPceIPv6Address": pcedpPccPceIPv6Address,
       "pcedpPccPceTimeDiscovered": pcedpPccPceTimeDiscovered,
       "pcedpPccPceLastUpdated": pcedpPccPceLastUpdated,
       "pcedpPccPcesCapabilityGroup": pcedpPccPcesCapabilityGroup,
       "pcedpPccPcesActivityGroup": pcedpPccPcesActivityGroup,
       "pcedpPccConformance": pcedpPccConformance,
       "pcedpPccGroups": pcedpPccGroups,
       "pcedpPccCompliances": pcedpPccCompliances,
       "pcedpPccGeneralPceInformation": pcedpPccGeneralPceInformation,
       "pcedpPccDetailledPceInformation": pcedpPccDetailledPceInformation}
)
