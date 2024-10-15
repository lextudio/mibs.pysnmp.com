# SNMP MIB module (HUAWEI-MDNS-RELAY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-MDNS-RELAY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:04:54 2024
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

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

hwMdnsRelayMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 326)
)
hwMdnsRelayMIB.setRevisions(
        ("2014-01-06 11:16",
         "2014-01-06 11:16")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwMdnsRelayObjects_ObjectIdentity = ObjectIdentity
hwMdnsRelayObjects = _HwMdnsRelayObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 326, 1)
)
_HwMdnsRelayGatewayIPGlobal_Type = IpAddress
_HwMdnsRelayGatewayIPGlobal_Object = MibScalar
hwMdnsRelayGatewayIPGlobal = _HwMdnsRelayGatewayIPGlobal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 326, 1, 1),
    _HwMdnsRelayGatewayIPGlobal_Type()
)
hwMdnsRelayGatewayIPGlobal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMdnsRelayGatewayIPGlobal.setStatus("current")
_HwMdnsRelaySourceIPGlobal_Type = IpAddress
_HwMdnsRelaySourceIPGlobal_Object = MibScalar
hwMdnsRelaySourceIPGlobal = _HwMdnsRelaySourceIPGlobal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 326, 1, 2),
    _HwMdnsRelaySourceIPGlobal_Type()
)
hwMdnsRelaySourceIPGlobal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMdnsRelaySourceIPGlobal.setStatus("current")
_HwMdnsRelayCfgTable_Object = MibTable
hwMdnsRelayCfgTable = _HwMdnsRelayCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 326, 1, 3)
)
if mibBuilder.loadTexts:
    hwMdnsRelayCfgTable.setStatus("current")
_HwMdnsRelayCfgEntry_Object = MibTableRow
hwMdnsRelayCfgEntry = _HwMdnsRelayCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 326, 1, 3, 1)
)
hwMdnsRelayCfgEntry.setIndexNames(
    (0, "HUAWEI-MDNS-RELAY-MIB", "hwMdnsRelayVlanId"),
)
if mibBuilder.loadTexts:
    hwMdnsRelayCfgEntry.setStatus("current")


class _HwMdnsRelayVlanId_Type(Integer32):
    """Custom type hwMdnsRelayVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HwMdnsRelayVlanId_Type.__name__ = "Integer32"
_HwMdnsRelayVlanId_Object = MibTableColumn
hwMdnsRelayVlanId = _HwMdnsRelayVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 326, 1, 3, 1, 1),
    _HwMdnsRelayVlanId_Type()
)
hwMdnsRelayVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMdnsRelayVlanId.setStatus("current")


class _HwMdnsRelayEnable_Type(Integer32):
    """Custom type hwMdnsRelayEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_HwMdnsRelayEnable_Type.__name__ = "Integer32"
_HwMdnsRelayEnable_Object = MibTableColumn
hwMdnsRelayEnable = _HwMdnsRelayEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 326, 1, 3, 1, 2),
    _HwMdnsRelayEnable_Type()
)
hwMdnsRelayEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMdnsRelayEnable.setStatus("current")


class _HwMdnsRelayProbeInterval_Type(Integer32):
    """Custom type hwMdnsRelayProbeInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 38400),
    )


_HwMdnsRelayProbeInterval_Type.__name__ = "Integer32"
_HwMdnsRelayProbeInterval_Object = MibTableColumn
hwMdnsRelayProbeInterval = _HwMdnsRelayProbeInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 326, 1, 3, 1, 3),
    _HwMdnsRelayProbeInterval_Type()
)
hwMdnsRelayProbeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMdnsRelayProbeInterval.setStatus("current")
_HwMdnsRelayMibConformance_ObjectIdentity = ObjectIdentity
hwMdnsRelayMibConformance = _HwMdnsRelayMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 326, 2)
)
_HwMdnsRelayMibGroups_ObjectIdentity = ObjectIdentity
hwMdnsRelayMibGroups = _HwMdnsRelayMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 326, 2, 1)
)
_HwMdnsRelayMIBCompliances_ObjectIdentity = ObjectIdentity
hwMdnsRelayMIBCompliances = _HwMdnsRelayMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 326, 2, 2)
)

# Managed Objects groups

hwMdnsRelayMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 326, 2, 1, 1)
)
hwMdnsRelayMibGroup.setObjects(
      *(("HUAWEI-MDNS-RELAY-MIB", "hwMdnsRelayGatewayIPGlobal"),
        ("HUAWEI-MDNS-RELAY-MIB", "hwMdnsRelaySourceIPGlobal"),
        ("HUAWEI-MDNS-RELAY-MIB", "hwMdnsRelayVlanId"),
        ("HUAWEI-MDNS-RELAY-MIB", "hwMdnsRelayEnable"),
        ("HUAWEI-MDNS-RELAY-MIB", "hwMdnsRelayProbeInterval"))
)
if mibBuilder.loadTexts:
    hwMdnsRelayMibGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hwMdnsRelayMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 326, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hwMdnsRelayMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-MDNS-RELAY-MIB",
    **{"hwMdnsRelayMIB": hwMdnsRelayMIB,
       "hwMdnsRelayObjects": hwMdnsRelayObjects,
       "hwMdnsRelayGatewayIPGlobal": hwMdnsRelayGatewayIPGlobal,
       "hwMdnsRelaySourceIPGlobal": hwMdnsRelaySourceIPGlobal,
       "hwMdnsRelayCfgTable": hwMdnsRelayCfgTable,
       "hwMdnsRelayCfgEntry": hwMdnsRelayCfgEntry,
       "hwMdnsRelayVlanId": hwMdnsRelayVlanId,
       "hwMdnsRelayEnable": hwMdnsRelayEnable,
       "hwMdnsRelayProbeInterval": hwMdnsRelayProbeInterval,
       "hwMdnsRelayMibConformance": hwMdnsRelayMibConformance,
       "hwMdnsRelayMibGroups": hwMdnsRelayMibGroups,
       "hwMdnsRelayMibGroup": hwMdnsRelayMibGroup,
       "hwMdnsRelayMIBCompliances": hwMdnsRelayMIBCompliances,
       "hwMdnsRelayMIBCompliance": hwMdnsRelayMIBCompliance}
)
