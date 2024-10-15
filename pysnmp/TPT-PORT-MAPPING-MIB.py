# SNMP MIB module (TPT-PORT-MAPPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPT-PORT-MAPPING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:07:07 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

(tpt_tpa_objs,) = mibBuilder.importSymbols(
    "TPT-TPAMIBS-MIB",
    "tpt-tpa-objs")


# MODULE-IDENTITY

tpt_port_mapping_objs = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 16)
)
tpt_port_mapping_objs.setRevisions(
        ("2016-10-03 12:00",
         "2016-05-25 18:54")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PortMappingTable_Object = MibTable
portMappingTable = _PortMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 16, 1)
)
if mibBuilder.loadTexts:
    portMappingTable.setStatus("current")
_PortMappingEntry_Object = MibTableRow
portMappingEntry = _PortMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 16, 1, 1)
)
portMappingEntry.setIndexNames(
    (0, "TPT-PORT-MAPPING-MIB", "portMappingLogicalSlot"),
    (0, "TPT-PORT-MAPPING-MIB", "portMappingLogicalPort"),
)
if mibBuilder.loadTexts:
    portMappingEntry.setStatus("current")
_PortMappingLogicalSlot_Type = Unsigned32
_PortMappingLogicalSlot_Object = MibTableColumn
portMappingLogicalSlot = _PortMappingLogicalSlot_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 16, 1, 1, 1),
    _PortMappingLogicalSlot_Type()
)
portMappingLogicalSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMappingLogicalSlot.setStatus("current")
_PortMappingLogicalPort_Type = Unsigned32
_PortMappingLogicalPort_Object = MibTableColumn
portMappingLogicalPort = _PortMappingLogicalPort_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 16, 1, 1, 2),
    _PortMappingLogicalPort_Type()
)
portMappingLogicalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMappingLogicalPort.setStatus("current")
_PortMappingLogicalIfIndex_Type = InterfaceIndex
_PortMappingLogicalIfIndex_Object = MibTableColumn
portMappingLogicalIfIndex = _PortMappingLogicalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 16, 1, 1, 3),
    _PortMappingLogicalIfIndex_Type()
)
portMappingLogicalIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMappingLogicalIfIndex.setStatus("current")
_PortMappingPhysicalSlot_Type = Unsigned32
_PortMappingPhysicalSlot_Object = MibTableColumn
portMappingPhysicalSlot = _PortMappingPhysicalSlot_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 16, 1, 1, 4),
    _PortMappingPhysicalSlot_Type()
)
portMappingPhysicalSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMappingPhysicalSlot.setStatus("current")
_PortMappingPhysicalPort_Type = Unsigned32
_PortMappingPhysicalPort_Object = MibTableColumn
portMappingPhysicalPort = _PortMappingPhysicalPort_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 16, 1, 1, 5),
    _PortMappingPhysicalPort_Type()
)
portMappingPhysicalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMappingPhysicalPort.setStatus("current")
_PortMappingPhysicalIfIndex_Type = InterfaceIndex
_PortMappingPhysicalIfIndex_Object = MibTableColumn
portMappingPhysicalIfIndex = _PortMappingPhysicalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 16, 1, 1, 6),
    _PortMappingPhysicalIfIndex_Type()
)
portMappingPhysicalIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMappingPhysicalIfIndex.setStatus("current")


class _PortMappingSegmentName_Type(OctetString):
    """Custom type portMappingSegmentName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_PortMappingSegmentName_Type.__name__ = "OctetString"
_PortMappingSegmentName_Object = MibTableColumn
portMappingSegmentName = _PortMappingSegmentName_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 16, 1, 1, 7),
    _PortMappingSegmentName_Type()
)
portMappingSegmentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMappingSegmentName.setStatus("obsolete")


class _PortMappingPhysicalVlanId_Type(Integer32):
    """Custom type portMappingPhysicalVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_PortMappingPhysicalVlanId_Type.__name__ = "Integer32"
_PortMappingPhysicalVlanId_Object = MibTableColumn
portMappingPhysicalVlanId = _PortMappingPhysicalVlanId_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 16, 1, 1, 8),
    _PortMappingPhysicalVlanId_Type()
)
portMappingPhysicalVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMappingPhysicalVlanId.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPT-PORT-MAPPING-MIB",
    **{"tpt-port-mapping-objs": tpt_port_mapping_objs,
       "portMappingTable": portMappingTable,
       "portMappingEntry": portMappingEntry,
       "portMappingLogicalSlot": portMappingLogicalSlot,
       "portMappingLogicalPort": portMappingLogicalPort,
       "portMappingLogicalIfIndex": portMappingLogicalIfIndex,
       "portMappingPhysicalSlot": portMappingPhysicalSlot,
       "portMappingPhysicalPort": portMappingPhysicalPort,
       "portMappingPhysicalIfIndex": portMappingPhysicalIfIndex,
       "portMappingSegmentName": portMappingSegmentName,
       "portMappingPhysicalVlanId": portMappingPhysicalVlanId}
)
