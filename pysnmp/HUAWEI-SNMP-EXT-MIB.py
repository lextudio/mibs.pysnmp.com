# SNMP MIB module (HUAWEI-SNMP-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-SNMP-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:05:59 2024
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

(ifDescr,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifDescr",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hwSnmpExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 164)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwSnmpExtMIBObjects_ObjectIdentity = ObjectIdentity
hwSnmpExtMIBObjects = _HwSnmpExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 164, 1)
)


class _HwSnmpExtErrorCodeEnable_Type(EnabledStatus):
    """Custom type hwSnmpExtErrorCodeEnable based on EnabledStatus"""


_HwSnmpExtErrorCodeEnable_Object = MibScalar
hwSnmpExtErrorCodeEnable = _HwSnmpExtErrorCodeEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 164, 1, 1),
    _HwSnmpExtErrorCodeEnable_Type()
)
hwSnmpExtErrorCodeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSnmpExtErrorCodeEnable.setStatus("current")
_HwSnmpExtConformance_ObjectIdentity = ObjectIdentity
hwSnmpExtConformance = _HwSnmpExtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 164, 2)
)
_HwSnmpExtGroups_ObjectIdentity = ObjectIdentity
hwSnmpExtGroups = _HwSnmpExtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 164, 2, 1)
)
_HwSnmpExtCompliances_ObjectIdentity = ObjectIdentity
hwSnmpExtCompliances = _HwSnmpExtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 164, 2, 2)
)

# Managed Objects groups

hwSnmpExtRuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 164, 2, 1, 1)
)
hwSnmpExtRuleGroup.setObjects(
    ("HUAWEI-SNMP-EXT-MIB", "hwSnmpExtErrorCodeEnable")
)
if mibBuilder.loadTexts:
    hwSnmpExtRuleGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hwSnmpExtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 164, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hwSnmpExtCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-SNMP-EXT-MIB",
    **{"hwSnmpExtMIB": hwSnmpExtMIB,
       "hwSnmpExtMIBObjects": hwSnmpExtMIBObjects,
       "hwSnmpExtErrorCodeEnable": hwSnmpExtErrorCodeEnable,
       "hwSnmpExtConformance": hwSnmpExtConformance,
       "hwSnmpExtGroups": hwSnmpExtGroups,
       "hwSnmpExtRuleGroup": hwSnmpExtRuleGroup,
       "hwSnmpExtCompliances": hwSnmpExtCompliances,
       "hwSnmpExtCompliance": hwSnmpExtCompliance}
)
