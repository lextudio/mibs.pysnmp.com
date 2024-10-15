# SNMP MIB module (NMS-IF-APP-POLICY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NMS-IF-APP-POLICY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:27:56 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(nmsMgmt,) = mibBuilder.importSymbols(
    "NMS-SMI",
    "nmsMgmt")

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
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NmsIfAppPolicy_ObjectIdentity = ObjectIdentity
nmsIfAppPolicy = _NmsIfAppPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 65)
)
_NmsIfAppPolicyTable_Object = MibTable
nmsIfAppPolicyTable = _NmsIfAppPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 65, 1)
)
if mibBuilder.loadTexts:
    nmsIfAppPolicyTable.setStatus("mandatory")
_NmsIfAppPolicyEntry_Object = MibTableRow
nmsIfAppPolicyEntry = _NmsIfAppPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 65, 1, 1)
)
nmsIfAppPolicyEntry.setIndexNames(
    (0, "NMS-IF-APP-POLICY-MIB", "ponIfIndex"),
)
if mibBuilder.loadTexts:
    nmsIfAppPolicyEntry.setStatus("mandatory")
_NmsIfIndex_Type = Integer32
_NmsIfIndex_Object = MibTableColumn
nmsIfIndex = _NmsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 65, 1, 1, 1),
    _NmsIfIndex_Type()
)
nmsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsIfIndex.setStatus("mandatory")


class _NmsIfDescr_Type(DisplayString):
    """Custom type nmsIfDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NmsIfDescr_Type.__name__ = "DisplayString"
_NmsIfDescr_Object = MibTableColumn
nmsIfDescr = _NmsIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 65, 1, 1, 2),
    _NmsIfDescr_Type()
)
nmsIfDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsIfDescr.setStatus("mandatory")
_NmsIfInMacACL_Type = DisplayString
_NmsIfInMacACL_Object = MibTableColumn
nmsIfInMacACL = _NmsIfInMacACL_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 65, 1, 1, 3),
    _NmsIfInMacACL_Type()
)
nmsIfInMacACL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsIfInMacACL.setStatus("mandatory")
_NmsIfOutMacACL_Type = DisplayString
_NmsIfOutMacACL_Object = MibTableColumn
nmsIfOutMacACL = _NmsIfOutMacACL_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 65, 1, 1, 4),
    _NmsIfOutMacACL_Type()
)
nmsIfOutMacACL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsIfOutMacACL.setStatus("mandatory")
_NmsIfInIpACL_Type = DisplayString
_NmsIfInIpACL_Object = MibTableColumn
nmsIfInIpACL = _NmsIfInIpACL_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 65, 1, 1, 5),
    _NmsIfInIpACL_Type()
)
nmsIfInIpACL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsIfInIpACL.setStatus("mandatory")
_NmsIfOutIpACL_Type = DisplayString
_NmsIfOutIpACL_Object = MibTableColumn
nmsIfOutIpACL = _NmsIfOutIpACL_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 65, 1, 1, 6),
    _NmsIfOutIpACL_Type()
)
nmsIfOutIpACL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsIfOutIpACL.setStatus("mandatory")
_NmsIfInQosPolicyName_Type = DisplayString
_NmsIfInQosPolicyName_Object = MibTableColumn
nmsIfInQosPolicyName = _NmsIfInQosPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 65, 1, 1, 7),
    _NmsIfInQosPolicyName_Type()
)
nmsIfInQosPolicyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsIfInQosPolicyName.setStatus("mandatory")
_NmsIfOutQosPolicyName_Type = DisplayString
_NmsIfOutQosPolicyName_Object = MibTableColumn
nmsIfOutQosPolicyName = _NmsIfOutQosPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 9, 65, 1, 1, 8),
    _NmsIfOutQosPolicyName_Type()
)
nmsIfOutQosPolicyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsIfOutQosPolicyName.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NMS-IF-APP-POLICY-MIB",
    **{"nmsIfAppPolicy": nmsIfAppPolicy,
       "nmsIfAppPolicyTable": nmsIfAppPolicyTable,
       "nmsIfAppPolicyEntry": nmsIfAppPolicyEntry,
       "nmsIfIndex": nmsIfIndex,
       "nmsIfDescr": nmsIfDescr,
       "nmsIfInMacACL": nmsIfInMacACL,
       "nmsIfOutMacACL": nmsIfOutMacACL,
       "nmsIfInIpACL": nmsIfInIpACL,
       "nmsIfOutIpACL": nmsIfOutIpACL,
       "nmsIfInQosPolicyName": nmsIfInQosPolicyName,
       "nmsIfOutQosPolicyName": nmsIfOutQosPolicyName}
)
