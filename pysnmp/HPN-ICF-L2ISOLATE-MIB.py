# SNMP MIB module (HPN-ICF-L2ISOLATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-L2ISOLATE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:00:41 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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

hpnicfL2Isolate = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 103)
)
hpnicfL2Isolate.setRevisions(
        ("2009-05-06 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfL2IsolateObject_ObjectIdentity = ObjectIdentity
hpnicfL2IsolateObject = _HpnicfL2IsolateObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 103, 1)
)
_HpnicfL2IsolateEnableTable_Object = MibTable
hpnicfL2IsolateEnableTable = _HpnicfL2IsolateEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 103, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfL2IsolateEnableTable.setStatus("current")
_HpnicfL2IsolateEnableEntry_Object = MibTableRow
hpnicfL2IsolateEnableEntry = _HpnicfL2IsolateEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 103, 1, 1, 1)
)
hpnicfL2IsolateEnableEntry.setIndexNames(
    (0, "HPN-ICF-L2ISOLATE-MIB", "hpnicfL2IsolateVLANIndex"),
)
if mibBuilder.loadTexts:
    hpnicfL2IsolateEnableEntry.setStatus("current")


class _HpnicfL2IsolateVLANIndex_Type(Integer32):
    """Custom type hpnicfL2IsolateVLANIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HpnicfL2IsolateVLANIndex_Type.__name__ = "Integer32"
_HpnicfL2IsolateVLANIndex_Object = MibTableColumn
hpnicfL2IsolateVLANIndex = _HpnicfL2IsolateVLANIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 103, 1, 1, 1, 1),
    _HpnicfL2IsolateVLANIndex_Type()
)
hpnicfL2IsolateVLANIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfL2IsolateVLANIndex.setStatus("current")
_HpnicfL2IsolateEnable_Type = TruthValue
_HpnicfL2IsolateEnable_Object = MibTableColumn
hpnicfL2IsolateEnable = _HpnicfL2IsolateEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 103, 1, 1, 1, 2),
    _HpnicfL2IsolateEnable_Type()
)
hpnicfL2IsolateEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfL2IsolateEnable.setStatus("current")
_HpnicfL2IsolatePermitMACTable_Object = MibTable
hpnicfL2IsolatePermitMACTable = _HpnicfL2IsolatePermitMACTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 103, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfL2IsolatePermitMACTable.setStatus("current")
_HpnicfL2IsolatePermitMACEntry_Object = MibTableRow
hpnicfL2IsolatePermitMACEntry = _HpnicfL2IsolatePermitMACEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 103, 1, 2, 1)
)
hpnicfL2IsolatePermitMACEntry.setIndexNames(
    (0, "HPN-ICF-L2ISOLATE-MIB", "hpnicfL2IsolateVLANIndex"),
    (0, "HPN-ICF-L2ISOLATE-MIB", "hpnicfL2IsoLatePermitMAC"),
)
if mibBuilder.loadTexts:
    hpnicfL2IsolatePermitMACEntry.setStatus("current")
_HpnicfL2IsoLatePermitMAC_Type = MacAddress
_HpnicfL2IsoLatePermitMAC_Object = MibTableColumn
hpnicfL2IsoLatePermitMAC = _HpnicfL2IsoLatePermitMAC_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 103, 1, 2, 1, 1),
    _HpnicfL2IsoLatePermitMAC_Type()
)
hpnicfL2IsoLatePermitMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfL2IsoLatePermitMAC.setStatus("current")
_HpnicfL2IsoLatePermitMACRowStatus_Type = RowStatus
_HpnicfL2IsoLatePermitMACRowStatus_Object = MibTableColumn
hpnicfL2IsoLatePermitMACRowStatus = _HpnicfL2IsoLatePermitMACRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 103, 1, 2, 1, 2),
    _HpnicfL2IsoLatePermitMACRowStatus_Type()
)
hpnicfL2IsoLatePermitMACRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfL2IsoLatePermitMACRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-L2ISOLATE-MIB",
    **{"hpnicfL2Isolate": hpnicfL2Isolate,
       "hpnicfL2IsolateObject": hpnicfL2IsolateObject,
       "hpnicfL2IsolateEnableTable": hpnicfL2IsolateEnableTable,
       "hpnicfL2IsolateEnableEntry": hpnicfL2IsolateEnableEntry,
       "hpnicfL2IsolateVLANIndex": hpnicfL2IsolateVLANIndex,
       "hpnicfL2IsolateEnable": hpnicfL2IsolateEnable,
       "hpnicfL2IsolatePermitMACTable": hpnicfL2IsolatePermitMACTable,
       "hpnicfL2IsolatePermitMACEntry": hpnicfL2IsolatePermitMACEntry,
       "hpnicfL2IsoLatePermitMAC": hpnicfL2IsoLatePermitMAC,
       "hpnicfL2IsoLatePermitMACRowStatus": hpnicfL2IsoLatePermitMACRowStatus}
)
