# SNMP MIB module (NMS-EPON-ONU-UNI-IF-ACL-APP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NMS-EPON-ONU-UNI-IF-ACL-APP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:27:52 2024
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

(llidIfIndex,) = mibBuilder.importSymbols(
    "NMS-EPON-LLID",
    "llidIfIndex")

(nmsEPONGroup,) = mibBuilder.importSymbols(
    "NMS-SMI",
    "nmsEPONGroup")

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

_NmsEponOnuUniIfAppPolicy_ObjectIdentity = ObjectIdentity
nmsEponOnuUniIfAppPolicy = _NmsEponOnuUniIfAppPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 105)
)
_NmsEponOnuUniIfAppPolicyTable_Object = MibTable
nmsEponOnuUniIfAppPolicyTable = _NmsEponOnuUniIfAppPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 105, 1)
)
if mibBuilder.loadTexts:
    nmsEponOnuUniIfAppPolicyTable.setStatus("mandatory")
_NmsEponOnuUniIfAppPolicyEntry_Object = MibTableRow
nmsEponOnuUniIfAppPolicyEntry = _NmsEponOnuUniIfAppPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 105, 1, 1)
)
nmsEponOnuUniIfAppPolicyEntry.setIndexNames(
    (0, "NMS-EPON-LLID", "llidIfIndex"),
    (0, "NMS-EPON-ONU-UNI-IF-ACL-APP-MIB", "nmsOnuUniIfIndex"),
)
if mibBuilder.loadTexts:
    nmsEponOnuUniIfAppPolicyEntry.setStatus("mandatory")
_LlidIfIndex_Type = Integer32
_LlidIfIndex_Object = MibTableColumn
llidIfIndex = _LlidIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 105, 1, 1, 1),
    _LlidIfIndex_Type()
)
llidIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llidIfIndex.setStatus("mandatory")
_NmsOnuUniIfIndex_Type = Integer32
_NmsOnuUniIfIndex_Object = MibTableColumn
nmsOnuUniIfIndex = _NmsOnuUniIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 105, 1, 1, 2),
    _NmsOnuUniIfIndex_Type()
)
nmsOnuUniIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsOnuUniIfIndex.setStatus("mandatory")
_NmsOnuUniIfInMacACL_Type = DisplayString
_NmsOnuUniIfInMacACL_Object = MibTableColumn
nmsOnuUniIfInMacACL = _NmsOnuUniIfInMacACL_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 105, 1, 1, 3),
    _NmsOnuUniIfInMacACL_Type()
)
nmsOnuUniIfInMacACL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsOnuUniIfInMacACL.setStatus("mandatory")
_NmsOnuUniIfOutMacACL_Type = DisplayString
_NmsOnuUniIfOutMacACL_Object = MibTableColumn
nmsOnuUniIfOutMacACL = _NmsOnuUniIfOutMacACL_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 105, 1, 1, 4),
    _NmsOnuUniIfOutMacACL_Type()
)
nmsOnuUniIfOutMacACL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsOnuUniIfOutMacACL.setStatus("mandatory")
_NmsOnuUniIfInIpACL_Type = DisplayString
_NmsOnuUniIfInIpACL_Object = MibTableColumn
nmsOnuUniIfInIpACL = _NmsOnuUniIfInIpACL_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 105, 1, 1, 5),
    _NmsOnuUniIfInIpACL_Type()
)
nmsOnuUniIfInIpACL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsOnuUniIfInIpACL.setStatus("mandatory")
_NmsOnuUniIfOutIpACL_Type = DisplayString
_NmsOnuUniIfOutIpACL_Object = MibTableColumn
nmsOnuUniIfOutIpACL = _NmsOnuUniIfOutIpACL_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 105, 1, 1, 6),
    _NmsOnuUniIfOutIpACL_Type()
)
nmsOnuUniIfOutIpACL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsOnuUniIfOutIpACL.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NMS-EPON-ONU-UNI-IF-ACL-APP-MIB",
    **{"nmsEponOnuUniIfAppPolicy": nmsEponOnuUniIfAppPolicy,
       "nmsEponOnuUniIfAppPolicyTable": nmsEponOnuUniIfAppPolicyTable,
       "nmsEponOnuUniIfAppPolicyEntry": nmsEponOnuUniIfAppPolicyEntry,
       "llidIfIndex": llidIfIndex,
       "nmsOnuUniIfIndex": nmsOnuUniIfIndex,
       "nmsOnuUniIfInMacACL": nmsOnuUniIfInMacACL,
       "nmsOnuUniIfOutMacACL": nmsOnuUniIfOutMacACL,
       "nmsOnuUniIfInIpACL": nmsOnuUniIfInIpACL,
       "nmsOnuUniIfOutIpACL": nmsOnuUniIfOutIpACL}
)
