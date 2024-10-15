# SNMP MIB module (A3COM-HUAWEI-LswARP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-LswARP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:28:21 2024
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

(lswCommon,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "lswCommon")

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

hwLswArpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 4)
)
hwLswArpMib.setRevisions(
        ("2001-06-29 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwLswProxyArpObject_ObjectIdentity = ObjectIdentity
hwLswProxyArpObject = _HwLswProxyArpObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 4, 1)
)
if mibBuilder.loadTexts:
    hwLswProxyArpObject.setStatus("current")
_HwLswProxyArpEnableTable_Object = MibTable
hwLswProxyArpEnableTable = _HwLswProxyArpEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    hwLswProxyArpEnableTable.setStatus("current")
_HwLswProxyArpEnableEntry_Object = MibTableRow
hwLswProxyArpEnableEntry = _HwLswProxyArpEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 4, 1, 1, 1)
)
hwLswProxyArpEnableEntry.setIndexNames(
    (0, "A3COM-HUAWEI-LswARP-MIB", "hwLswIfIndex"),
)
if mibBuilder.loadTexts:
    hwLswProxyArpEnableEntry.setStatus("current")
_HwLswIfIndex_Type = Integer32
_HwLswIfIndex_Object = MibTableColumn
hwLswIfIndex = _HwLswIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 4, 1, 1, 1, 1),
    _HwLswIfIndex_Type()
)
hwLswIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLswIfIndex.setStatus("current")


class _HwLswProxyArpStatus_Type(Integer32):
    """Custom type hwLswProxyArpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_HwLswProxyArpStatus_Type.__name__ = "Integer32"
_HwLswProxyArpStatus_Object = MibTableColumn
hwLswProxyArpStatus = _HwLswProxyArpStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 4, 1, 1, 1, 2),
    _HwLswProxyArpStatus_Type()
)
hwLswProxyArpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLswProxyArpStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-LswARP-MIB",
    **{"hwLswArpMib": hwLswArpMib,
       "hwLswProxyArpObject": hwLswProxyArpObject,
       "hwLswProxyArpEnableTable": hwLswProxyArpEnableTable,
       "hwLswProxyArpEnableEntry": hwLswProxyArpEnableEntry,
       "hwLswIfIndex": hwLswIfIndex,
       "hwLswProxyArpStatus": hwLswProxyArpStatus}
)
