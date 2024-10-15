# SNMP MIB module (INTEL-L3LINK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INTEL-L3LINK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:09:51 2024
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

(mib2ext,) = mibBuilder.importSymbols(
    "INTEL-GEN-MIB",
    "mib2ext")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_L3Link_ObjectIdentity = ObjectIdentity
l3Link = _L3Link_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 12)
)
_Interface_ObjectIdentity = ObjectIdentity
interface = _Interface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 12, 1)
)
_L3lkInterfaceTable_Object = MibTable
l3lkInterfaceTable = _L3lkInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 12, 1, 1)
)
if mibBuilder.loadTexts:
    l3lkInterfaceTable.setStatus("mandatory")
_L3lkInterfaceEntry_Object = MibTableRow
l3lkInterfaceEntry = _L3lkInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 12, 1, 1, 1)
)
l3lkInterfaceEntry.setIndexNames(
    (0, "INTEL-L3LINK-MIB", "l3lkInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    l3lkInterfaceEntry.setStatus("mandatory")
_L3lkInterfaceIfIndex_Type = Integer32
_L3lkInterfaceIfIndex_Object = MibTableColumn
l3lkInterfaceIfIndex = _L3lkInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 12, 1, 1, 1, 1),
    _L3lkInterfaceIfIndex_Type()
)
l3lkInterfaceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3lkInterfaceIfIndex.setStatus("mandatory")
_L3lkInterfaceVlanId_Type = Integer32
_L3lkInterfaceVlanId_Object = MibTableColumn
l3lkInterfaceVlanId = _L3lkInterfaceVlanId_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 12, 1, 1, 1, 2),
    _L3lkInterfaceVlanId_Type()
)
l3lkInterfaceVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l3lkInterfaceVlanId.setStatus("mandatory")


class _L3lkInterfaceStatus_Type(Integer32):
    """Custom type l3lkInterfaceStatus based on Integer32"""
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


_L3lkInterfaceStatus_Type.__name__ = "Integer32"
_L3lkInterfaceStatus_Object = MibTableColumn
l3lkInterfaceStatus = _L3lkInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 12, 1, 1, 1, 3),
    _L3lkInterfaceStatus_Type()
)
l3lkInterfaceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l3lkInterfaceStatus.setStatus("mandatory")


class _L3lkInterfaceCreateObj_Type(OctetString):
    """Custom type l3lkInterfaceCreateObj based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_L3lkInterfaceCreateObj_Type.__name__ = "OctetString"
_L3lkInterfaceCreateObj_Object = MibTableColumn
l3lkInterfaceCreateObj = _L3lkInterfaceCreateObj_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 12, 1, 1, 1, 4),
    _L3lkInterfaceCreateObj_Type()
)
l3lkInterfaceCreateObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l3lkInterfaceCreateObj.setStatus("mandatory")


class _L3lkInterfaceDeleteObj_Type(Integer32):
    """Custom type l3lkInterfaceDeleteObj based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("delete", 1)
    )


_L3lkInterfaceDeleteObj_Type.__name__ = "Integer32"
_L3lkInterfaceDeleteObj_Object = MibTableColumn
l3lkInterfaceDeleteObj = _L3lkInterfaceDeleteObj_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 12, 1, 1, 1, 5),
    _L3lkInterfaceDeleteObj_Type()
)
l3lkInterfaceDeleteObj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l3lkInterfaceDeleteObj.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INTEL-L3LINK-MIB",
    **{"l3Link": l3Link,
       "interface": interface,
       "l3lkInterfaceTable": l3lkInterfaceTable,
       "l3lkInterfaceEntry": l3lkInterfaceEntry,
       "l3lkInterfaceIfIndex": l3lkInterfaceIfIndex,
       "l3lkInterfaceVlanId": l3lkInterfaceVlanId,
       "l3lkInterfaceStatus": l3lkInterfaceStatus,
       "l3lkInterfaceCreateObj": l3lkInterfaceCreateObj,
       "l3lkInterfaceDeleteObj": l3lkInterfaceDeleteObj}
)
