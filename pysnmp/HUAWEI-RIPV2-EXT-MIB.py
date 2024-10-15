# SNMP MIB module (HUAWEI-RIPV2-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-RIPV2-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:05:43 2024
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hwRipv2Ext = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 120)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwRip2ProcInstTable_Object = MibTable
hwRip2ProcInstTable = _HwRip2ProcInstTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 120, 1)
)
if mibBuilder.loadTexts:
    hwRip2ProcInstTable.setStatus("current")
_HwRip2ProcInstEntry_Object = MibTableRow
hwRip2ProcInstEntry = _HwRip2ProcInstEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 120, 1, 1)
)
hwRip2ProcInstEntry.setIndexNames(
    (0, "HUAWEI-RIPV2-EXT-MIB", "hwRip2ProcessId"),
)
if mibBuilder.loadTexts:
    hwRip2ProcInstEntry.setStatus("current")


class _HwRip2ProcessId_Type(Integer32):
    """Custom type hwRip2ProcessId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwRip2ProcessId_Type.__name__ = "Integer32"
_HwRip2ProcessId_Object = MibTableColumn
hwRip2ProcessId = _HwRip2ProcessId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 120, 1, 1, 1),
    _HwRip2ProcessId_Type()
)
hwRip2ProcessId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwRip2ProcessId.setStatus("current")


class _HwRip2VrfName_Type(OctetString):
    """Custom type hwRip2VrfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwRip2VrfName_Type.__name__ = "OctetString"
_HwRip2VrfName_Object = MibTableColumn
hwRip2VrfName = _HwRip2VrfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 120, 1, 1, 2),
    _HwRip2VrfName_Type()
)
hwRip2VrfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRip2VrfName.setStatus("current")


class _HwRip2CurrentProcId_Type(Integer32):
    """Custom type hwRip2CurrentProcId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwRip2CurrentProcId_Type.__name__ = "Integer32"
_HwRip2CurrentProcId_Object = MibTableColumn
hwRip2CurrentProcId = _HwRip2CurrentProcId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 120, 1, 1, 3),
    _HwRip2CurrentProcId_Type()
)
hwRip2CurrentProcId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRip2CurrentProcId.setStatus("current")
_HwRip2Conformance_ObjectIdentity = ObjectIdentity
hwRip2Conformance = _HwRip2Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 120, 2)
)
_HwRip2Groups_ObjectIdentity = ObjectIdentity
hwRip2Groups = _HwRip2Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 120, 2, 1)
)
_HwRip2Compliances_ObjectIdentity = ObjectIdentity
hwRip2Compliances = _HwRip2Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 120, 2, 2)
)

# Managed Objects groups

hwRip2ExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 120, 2, 1, 2)
)
hwRip2ExtGroup.setObjects(
      *(("HUAWEI-RIPV2-EXT-MIB", "hwRip2VrfName"),
        ("HUAWEI-RIPV2-EXT-MIB", "hwRip2CurrentProcId"))
)
if mibBuilder.loadTexts:
    hwRip2ExtGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hwRip2Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 120, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hwRip2Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-RIPV2-EXT-MIB",
    **{"hwRipv2Ext": hwRipv2Ext,
       "hwRip2ProcInstTable": hwRip2ProcInstTable,
       "hwRip2ProcInstEntry": hwRip2ProcInstEntry,
       "hwRip2ProcessId": hwRip2ProcessId,
       "hwRip2VrfName": hwRip2VrfName,
       "hwRip2CurrentProcId": hwRip2CurrentProcId,
       "hwRip2Conformance": hwRip2Conformance,
       "hwRip2Groups": hwRip2Groups,
       "hwRip2ExtGroup": hwRip2ExtGroup,
       "hwRip2Compliances": hwRip2Compliances,
       "hwRip2Compliance": hwRip2Compliance}
)
