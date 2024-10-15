# SNMP MIB module (TPLINK-LLDPCOUNT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPLINK-LLDPCOUNT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:06:18 2024
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

(tplinkLldpMIBNotifications,
 tplinkLldpMIBObjects) = mibBuilder.importSymbols(
    "TPLINK-LLDP-MIB",
    "tplinkLldpMIBNotifications",
    "tplinkLldpMIBObjects")


# MODULE-IDENTITY


# Types definitions



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LldpCount_ObjectIdentity = ObjectIdentity
lldpCount = _LldpCount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 3)
)
_LldpGlobalCount_ObjectIdentity = ObjectIdentity
lldpGlobalCount = _LldpGlobalCount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 3, 1)
)


class _LldpGlobalCountUpdateTime_Type(OctetString):
    """Custom type lldpGlobalCountUpdateTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_LldpGlobalCountUpdateTime_Type.__name__ = "OctetString"
_LldpGlobalCountUpdateTime_Object = MibScalar
lldpGlobalCountUpdateTime = _LldpGlobalCountUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 3, 1, 1),
    _LldpGlobalCountUpdateTime_Type()
)
lldpGlobalCountUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpGlobalCountUpdateTime.setStatus("current")
_LldpGlobalCountNeighborInserted_Type = Integer32
_LldpGlobalCountNeighborInserted_Object = MibScalar
lldpGlobalCountNeighborInserted = _LldpGlobalCountNeighborInserted_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 3, 1, 2),
    _LldpGlobalCountNeighborInserted_Type()
)
lldpGlobalCountNeighborInserted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpGlobalCountNeighborInserted.setStatus("current")
_LldpGlobalCountNeighborDeleted_Type = Integer32
_LldpGlobalCountNeighborDeleted_Object = MibScalar
lldpGlobalCountNeighborDeleted = _LldpGlobalCountNeighborDeleted_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 3, 1, 3),
    _LldpGlobalCountNeighborDeleted_Type()
)
lldpGlobalCountNeighborDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpGlobalCountNeighborDeleted.setStatus("current")
_LldpGlobalCountNeighborDroped_Type = Integer32
_LldpGlobalCountNeighborDroped_Object = MibScalar
lldpGlobalCountNeighborDroped = _LldpGlobalCountNeighborDroped_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 3, 1, 4),
    _LldpGlobalCountNeighborDroped_Type()
)
lldpGlobalCountNeighborDroped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpGlobalCountNeighborDroped.setStatus("current")
_LldpGlobalCountNeighborAged_Type = Integer32
_LldpGlobalCountNeighborAged_Object = MibScalar
lldpGlobalCountNeighborAged = _LldpGlobalCountNeighborAged_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 3, 1, 5),
    _LldpGlobalCountNeighborAged_Type()
)
lldpGlobalCountNeighborAged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpGlobalCountNeighborAged.setStatus("current")
_LldpCountNeighborInfoTable_Object = MibTable
lldpCountNeighborInfoTable = _LldpCountNeighborInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 3, 2)
)
if mibBuilder.loadTexts:
    lldpCountNeighborInfoTable.setStatus("current")
_LldpCountNeighborInfoEntry_Object = MibTableRow
lldpCountNeighborInfoEntry = _LldpCountNeighborInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 3, 2, 1)
)
lldpCountNeighborInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    lldpCountNeighborInfoEntry.setStatus("current")


class _LldpCountNeighborPortId_Type(OctetString):
    """Custom type lldpCountNeighborPortId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LldpCountNeighborPortId_Type.__name__ = "OctetString"
_LldpCountNeighborPortId_Object = MibTableColumn
lldpCountNeighborPortId = _LldpCountNeighborPortId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 3, 2, 1, 1),
    _LldpCountNeighborPortId_Type()
)
lldpCountNeighborPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpCountNeighborPortId.setStatus("current")
_LldpNeighborFramesOut_Type = Integer32
_LldpNeighborFramesOut_Object = MibTableColumn
lldpNeighborFramesOut = _LldpNeighborFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 3, 2, 1, 2),
    _LldpNeighborFramesOut_Type()
)
lldpNeighborFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpNeighborFramesOut.setStatus("current")
_LldpNeighborFramesIn_Type = Integer32
_LldpNeighborFramesIn_Object = MibTableColumn
lldpNeighborFramesIn = _LldpNeighborFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 3, 2, 1, 3),
    _LldpNeighborFramesIn_Type()
)
lldpNeighborFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpNeighborFramesIn.setStatus("current")
_LldpNeighborFramesDiscarded_Type = Integer32
_LldpNeighborFramesDiscarded_Object = MibTableColumn
lldpNeighborFramesDiscarded = _LldpNeighborFramesDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 3, 2, 1, 4),
    _LldpNeighborFramesDiscarded_Type()
)
lldpNeighborFramesDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpNeighborFramesDiscarded.setStatus("current")
_LldpNeighborFramesInErrors_Type = Integer32
_LldpNeighborFramesInErrors_Object = MibTableColumn
lldpNeighborFramesInErrors = _LldpNeighborFramesInErrors_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 3, 2, 1, 5),
    _LldpNeighborFramesInErrors_Type()
)
lldpNeighborFramesInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpNeighborFramesInErrors.setStatus("current")
_LldpNeighborAgeOuts_Type = Integer32
_LldpNeighborAgeOuts_Object = MibTableColumn
lldpNeighborAgeOuts = _LldpNeighborAgeOuts_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 3, 2, 1, 6),
    _LldpNeighborAgeOuts_Type()
)
lldpNeighborAgeOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpNeighborAgeOuts.setStatus("current")
_LldpNeighborTlvDiscarded_Type = Integer32
_LldpNeighborTlvDiscarded_Object = MibTableColumn
lldpNeighborTlvDiscarded = _LldpNeighborTlvDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 3, 2, 1, 7),
    _LldpNeighborTlvDiscarded_Type()
)
lldpNeighborTlvDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpNeighborTlvDiscarded.setStatus("current")
_LldpNeighborTlvUnrecognized_Type = Integer32
_LldpNeighborTlvUnrecognized_Object = MibTableColumn
lldpNeighborTlvUnrecognized = _LldpNeighborTlvUnrecognized_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 3, 2, 1, 8),
    _LldpNeighborTlvUnrecognized_Type()
)
lldpNeighborTlvUnrecognized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpNeighborTlvUnrecognized.setStatus("current")

# Managed Objects groups


# Notification objects

lldpNeighborChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 2, 1)
)
lldpNeighborChange.setObjects(
      *(("TPLINK-LLDPCOUNT-MIB", "lldpGlobalCountNeighborInserted"),
        ("TPLINK-LLDPCOUNT-MIB", "lldpGlobalCountNeighborDeleted"),
        ("TPLINK-LLDPCOUNT-MIB", "lldpGlobalCountNeighborDroped"),
        ("TPLINK-LLDPCOUNT-MIB", "lldpGlobalCountNeighborAged"))
)
if mibBuilder.loadTexts:
    lldpNeighborChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-LLDPCOUNT-MIB",
    **{"MacAddress": MacAddress,
       "lldpCount": lldpCount,
       "lldpGlobalCount": lldpGlobalCount,
       "lldpGlobalCountUpdateTime": lldpGlobalCountUpdateTime,
       "lldpGlobalCountNeighborInserted": lldpGlobalCountNeighborInserted,
       "lldpGlobalCountNeighborDeleted": lldpGlobalCountNeighborDeleted,
       "lldpGlobalCountNeighborDroped": lldpGlobalCountNeighborDroped,
       "lldpGlobalCountNeighborAged": lldpGlobalCountNeighborAged,
       "lldpCountNeighborInfoTable": lldpCountNeighborInfoTable,
       "lldpCountNeighborInfoEntry": lldpCountNeighborInfoEntry,
       "lldpCountNeighborPortId": lldpCountNeighborPortId,
       "lldpNeighborFramesOut": lldpNeighborFramesOut,
       "lldpNeighborFramesIn": lldpNeighborFramesIn,
       "lldpNeighborFramesDiscarded": lldpNeighborFramesDiscarded,
       "lldpNeighborFramesInErrors": lldpNeighborFramesInErrors,
       "lldpNeighborAgeOuts": lldpNeighborAgeOuts,
       "lldpNeighborTlvDiscarded": lldpNeighborTlvDiscarded,
       "lldpNeighborTlvUnrecognized": lldpNeighborTlvUnrecognized,
       "lldpNeighborChange": lldpNeighborChange}
)
