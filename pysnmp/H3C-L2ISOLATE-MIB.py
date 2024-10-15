# SNMP MIB module (H3C-L2ISOLATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H3C-L2ISOLATE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:50:46 2024
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

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

h3cL2Isolate = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 103)
)
h3cL2Isolate.setRevisions(
        ("2009-05-06 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cL2IsolateObject_ObjectIdentity = ObjectIdentity
h3cL2IsolateObject = _H3cL2IsolateObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 103, 1)
)
_H3cL2IsolateEnableTable_Object = MibTable
h3cL2IsolateEnableTable = _H3cL2IsolateEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 103, 1, 1)
)
if mibBuilder.loadTexts:
    h3cL2IsolateEnableTable.setStatus("current")
_H3cL2IsolateEnableEntry_Object = MibTableRow
h3cL2IsolateEnableEntry = _H3cL2IsolateEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 103, 1, 1, 1)
)
h3cL2IsolateEnableEntry.setIndexNames(
    (0, "H3C-L2ISOLATE-MIB", "h3cL2IsolateVLANIndex"),
)
if mibBuilder.loadTexts:
    h3cL2IsolateEnableEntry.setStatus("current")


class _H3cL2IsolateVLANIndex_Type(Integer32):
    """Custom type h3cL2IsolateVLANIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_H3cL2IsolateVLANIndex_Type.__name__ = "Integer32"
_H3cL2IsolateVLANIndex_Object = MibTableColumn
h3cL2IsolateVLANIndex = _H3cL2IsolateVLANIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 103, 1, 1, 1, 1),
    _H3cL2IsolateVLANIndex_Type()
)
h3cL2IsolateVLANIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cL2IsolateVLANIndex.setStatus("current")
_H3cL2IsolateEnable_Type = TruthValue
_H3cL2IsolateEnable_Object = MibTableColumn
h3cL2IsolateEnable = _H3cL2IsolateEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 103, 1, 1, 1, 2),
    _H3cL2IsolateEnable_Type()
)
h3cL2IsolateEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cL2IsolateEnable.setStatus("current")
_H3cL2IsolatePermitMACTable_Object = MibTable
h3cL2IsolatePermitMACTable = _H3cL2IsolatePermitMACTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 103, 1, 2)
)
if mibBuilder.loadTexts:
    h3cL2IsolatePermitMACTable.setStatus("current")
_H3cL2IsolatePermitMACEntry_Object = MibTableRow
h3cL2IsolatePermitMACEntry = _H3cL2IsolatePermitMACEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 103, 1, 2, 1)
)
h3cL2IsolatePermitMACEntry.setIndexNames(
    (0, "H3C-L2ISOLATE-MIB", "h3cL2IsolateVLANIndex"),
    (0, "H3C-L2ISOLATE-MIB", "h3cL2IsoLatePermitMAC"),
)
if mibBuilder.loadTexts:
    h3cL2IsolatePermitMACEntry.setStatus("current")
_H3cL2IsoLatePermitMAC_Type = MacAddress
_H3cL2IsoLatePermitMAC_Object = MibTableColumn
h3cL2IsoLatePermitMAC = _H3cL2IsoLatePermitMAC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 103, 1, 2, 1, 1),
    _H3cL2IsoLatePermitMAC_Type()
)
h3cL2IsoLatePermitMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cL2IsoLatePermitMAC.setStatus("current")
_H3cL2IsoLatePermitMACRowStatus_Type = RowStatus
_H3cL2IsoLatePermitMACRowStatus_Object = MibTableColumn
h3cL2IsoLatePermitMACRowStatus = _H3cL2IsoLatePermitMACRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 103, 1, 2, 1, 2),
    _H3cL2IsoLatePermitMACRowStatus_Type()
)
h3cL2IsoLatePermitMACRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cL2IsoLatePermitMACRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-L2ISOLATE-MIB",
    **{"h3cL2Isolate": h3cL2Isolate,
       "h3cL2IsolateObject": h3cL2IsolateObject,
       "h3cL2IsolateEnableTable": h3cL2IsolateEnableTable,
       "h3cL2IsolateEnableEntry": h3cL2IsolateEnableEntry,
       "h3cL2IsolateVLANIndex": h3cL2IsolateVLANIndex,
       "h3cL2IsolateEnable": h3cL2IsolateEnable,
       "h3cL2IsolatePermitMACTable": h3cL2IsolatePermitMACTable,
       "h3cL2IsolatePermitMACEntry": h3cL2IsolatePermitMACEntry,
       "h3cL2IsoLatePermitMAC": h3cL2IsoLatePermitMAC,
       "h3cL2IsoLatePermitMACRowStatus": h3cL2IsoLatePermitMACRowStatus}
)
