# SNMP MIB module (HUAWEI-IPV6-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-IPV6-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:04:11 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ipv6IfIndex,) = mibBuilder.importSymbols(
    "IPV6-MIB",
    "ipv6IfIndex")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hwIpv6Mib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 153)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwIpv6MibObjects_ObjectIdentity = ObjectIdentity
hwIpv6MibObjects = _HwIpv6MibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 153, 1)
)
_HwIpv6IfTable_Object = MibTable
hwIpv6IfTable = _HwIpv6IfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 153, 1, 1)
)
if mibBuilder.loadTexts:
    hwIpv6IfTable.setStatus("current")
_HwIpv6IfEntry_Object = MibTableRow
hwIpv6IfEntry = _HwIpv6IfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 153, 1, 1, 1)
)
hwIpv6IfEntry.setIndexNames(
    (0, "IPV6-MIB", "ipv6IfIndex"),
)
if mibBuilder.loadTexts:
    hwIpv6IfEntry.setStatus("current")
_HwIpv6IfDescr_Type = DisplayString
_HwIpv6IfDescr_Object = MibTableColumn
hwIpv6IfDescr = _HwIpv6IfDescr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 153, 1, 1, 1, 1),
    _HwIpv6IfDescr_Type()
)
hwIpv6IfDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpv6IfDescr.setStatus("current")
_HwIpv6IfEnableFlag_Type = EnabledStatus
_HwIpv6IfEnableFlag_Object = MibTableColumn
hwIpv6IfEnableFlag = _HwIpv6IfEnableFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 153, 1, 1, 1, 2),
    _HwIpv6IfEnableFlag_Type()
)
hwIpv6IfEnableFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpv6IfEnableFlag.setStatus("current")
_HwIpv6MibConformance_ObjectIdentity = ObjectIdentity
hwIpv6MibConformance = _HwIpv6MibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 153, 2)
)
_HwIpv6Compliances_ObjectIdentity = ObjectIdentity
hwIpv6Compliances = _HwIpv6Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 153, 2, 1)
)
_HwIpv6Groups_ObjectIdentity = ObjectIdentity
hwIpv6Groups = _HwIpv6Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 153, 2, 2)
)

# Managed Objects groups

hwIpv6Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 153, 2, 2, 1)
)
hwIpv6Group.setObjects(
      *(("HUAWEI-IPV6-MIB", "hwIpv6IfDescr"),
        ("HUAWEI-IPV6-MIB", "hwIpv6IfEnableFlag"))
)
if mibBuilder.loadTexts:
    hwIpv6Group.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hwIpv6Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 153, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hwIpv6Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-IPV6-MIB",
    **{"hwIpv6Mib": hwIpv6Mib,
       "hwIpv6MibObjects": hwIpv6MibObjects,
       "hwIpv6IfTable": hwIpv6IfTable,
       "hwIpv6IfEntry": hwIpv6IfEntry,
       "hwIpv6IfDescr": hwIpv6IfDescr,
       "hwIpv6IfEnableFlag": hwIpv6IfEnableFlag,
       "hwIpv6MibConformance": hwIpv6MibConformance,
       "hwIpv6Compliances": hwIpv6Compliances,
       "hwIpv6Compliance": hwIpv6Compliance,
       "hwIpv6Groups": hwIpv6Groups,
       "hwIpv6Group": hwIpv6Group}
)
