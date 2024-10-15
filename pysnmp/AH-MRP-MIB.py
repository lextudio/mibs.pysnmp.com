# SNMP MIB module (AH-MRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AH-MRP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:35:00 2024
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

(AhNodeID,
 AhString,
 ahAPMRP) = mibBuilder.importSymbols(
    "AH-SMI-MIB",
    "AhNodeID",
    "AhString",
    "ahAPMRP")

(ifEntry,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifEntry",
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


# MODULE-IDENTITY

ahMRP = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AhLinkType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ahETHERNET", 0),
          ("ahWIRELESS", 1))
    )



# MIB Managed Objects in the order of their OIDs

_AhNeighborTable_Object = MibTable
ahNeighborTable = _AhNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ahNeighborTable.setStatus("current")
_AhNeighborEntry_Object = MibTableRow
ahNeighborEntry = _AhNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1, 1, 1)
)
ahNeighborEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "AH-MRP-MIB", "ahNeighberAPId"),
)
if mibBuilder.loadTexts:
    ahNeighborEntry.setStatus("current")
_AhNeighberAPId_Type = AhNodeID
_AhNeighberAPId_Object = MibTableColumn
ahNeighberAPId = _AhNeighberAPId_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1, 1, 1, 1),
    _AhNeighberAPId_Type()
)
ahNeighberAPId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahNeighberAPId.setStatus("current")
_AhLinkCost_Type = Counter32
_AhLinkCost_Object = MibTableColumn
ahLinkCost = _AhLinkCost_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1, 1, 1, 2),
    _AhLinkCost_Type()
)
ahLinkCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahLinkCost.setStatus("current")
_AhRSSI_Type = Integer32
_AhRSSI_Object = MibTableColumn
ahRSSI = _AhRSSI_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1, 1, 1, 3),
    _AhRSSI_Type()
)
ahRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahRSSI.setStatus("current")
_AhLinkUptime_Type = Counter32
_AhLinkUptime_Object = MibTableColumn
ahLinkUptime = _AhLinkUptime_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1, 1, 1, 4),
    _AhLinkUptime_Type()
)
ahLinkUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahLinkUptime.setStatus("current")
_AhLinkType_Type = AhLinkType
_AhLinkType_Object = MibTableColumn
ahLinkType = _AhLinkType_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1, 1, 1, 5),
    _AhLinkType_Type()
)
ahLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahLinkType.setStatus("current")
_AhRxDataFrames_Type = Counter32
_AhRxDataFrames_Object = MibTableColumn
ahRxDataFrames = _AhRxDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1, 1, 1, 6),
    _AhRxDataFrames_Type()
)
ahRxDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahRxDataFrames.setStatus("current")
_AhRXDataOctets_Type = Counter32
_AhRXDataOctets_Object = MibTableColumn
ahRXDataOctets = _AhRXDataOctets_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1, 1, 1, 7),
    _AhRXDataOctets_Type()
)
ahRXDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahRXDataOctets.setStatus("current")
_AhRxMgtFrames_Type = Counter32
_AhRxMgtFrames_Object = MibTableColumn
ahRxMgtFrames = _AhRxMgtFrames_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1, 1, 1, 8),
    _AhRxMgtFrames_Type()
)
ahRxMgtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahRxMgtFrames.setStatus("current")
_AhRxUnicastFrames_Type = Counter32
_AhRxUnicastFrames_Object = MibTableColumn
ahRxUnicastFrames = _AhRxUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1, 1, 1, 9),
    _AhRxUnicastFrames_Type()
)
ahRxUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahRxUnicastFrames.setStatus("current")
_AhRxMulticastFrames_Type = Counter32
_AhRxMulticastFrames_Object = MibTableColumn
ahRxMulticastFrames = _AhRxMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1, 1, 1, 10),
    _AhRxMulticastFrames_Type()
)
ahRxMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahRxMulticastFrames.setStatus("current")
_AhRxBroadcastFrames_Type = Counter32
_AhRxBroadcastFrames_Object = MibTableColumn
ahRxBroadcastFrames = _AhRxBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1, 1, 1, 11),
    _AhRxBroadcastFrames_Type()
)
ahRxBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahRxBroadcastFrames.setStatus("current")
_AhTxDataFrames_Type = Counter32
_AhTxDataFrames_Object = MibTableColumn
ahTxDataFrames = _AhTxDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1, 1, 1, 12),
    _AhTxDataFrames_Type()
)
ahTxDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahTxDataFrames.setStatus("current")
_AhTxMgtFrames_Type = Counter32
_AhTxMgtFrames_Object = MibTableColumn
ahTxMgtFrames = _AhTxMgtFrames_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1, 1, 1, 13),
    _AhTxMgtFrames_Type()
)
ahTxMgtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahTxMgtFrames.setStatus("current")
_AhTxDataOctets_Type = Counter32
_AhTxDataOctets_Object = MibTableColumn
ahTxDataOctets = _AhTxDataOctets_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1, 1, 1, 14),
    _AhTxDataOctets_Type()
)
ahTxDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahTxDataOctets.setStatus("current")
_AhTxUnicastFrames_Type = Counter32
_AhTxUnicastFrames_Object = MibTableColumn
ahTxUnicastFrames = _AhTxUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1, 1, 1, 15),
    _AhTxUnicastFrames_Type()
)
ahTxUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahTxUnicastFrames.setStatus("current")
_AhTxMulticastFrames_Type = Counter32
_AhTxMulticastFrames_Object = MibTableColumn
ahTxMulticastFrames = _AhTxMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1, 1, 1, 16),
    _AhTxMulticastFrames_Type()
)
ahTxMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahTxMulticastFrames.setStatus("current")
_AhTxBroadcastFrames_Type = Counter32
_AhTxBroadcastFrames_Object = MibTableColumn
ahTxBroadcastFrames = _AhTxBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1, 1, 1, 17),
    _AhTxBroadcastFrames_Type()
)
ahTxBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahTxBroadcastFrames.setStatus("current")
_AhTxBeDataFrames_Type = Counter32
_AhTxBeDataFrames_Object = MibTableColumn
ahTxBeDataFrames = _AhTxBeDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1, 1, 1, 18),
    _AhTxBeDataFrames_Type()
)
ahTxBeDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahTxBeDataFrames.setStatus("current")
_AhTxBgDataFrames_Type = Counter32
_AhTxBgDataFrames_Object = MibTableColumn
ahTxBgDataFrames = _AhTxBgDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1, 1, 1, 19),
    _AhTxBgDataFrames_Type()
)
ahTxBgDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahTxBgDataFrames.setStatus("current")
_AhTxViDataFrames_Type = Counter32
_AhTxViDataFrames_Object = MibTableColumn
ahTxViDataFrames = _AhTxViDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1, 1, 1, 20),
    _AhTxViDataFrames_Type()
)
ahTxViDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahTxViDataFrames.setStatus("current")
_AhTxVoDataFrames_Type = Counter32
_AhTxVoDataFrames_Object = MibTableColumn
ahTxVoDataFrames = _AhTxVoDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 26928, 1, 1, 1, 3, 1, 1, 1, 21),
    _AhTxVoDataFrames_Type()
)
ahTxVoDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahTxVoDataFrames.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AH-MRP-MIB",
    **{"AhLinkType": AhLinkType,
       "ahMRP": ahMRP,
       "ahNeighborTable": ahNeighborTable,
       "ahNeighborEntry": ahNeighborEntry,
       "ahNeighberAPId": ahNeighberAPId,
       "ahLinkCost": ahLinkCost,
       "ahRSSI": ahRSSI,
       "ahLinkUptime": ahLinkUptime,
       "ahLinkType": ahLinkType,
       "ahRxDataFrames": ahRxDataFrames,
       "ahRXDataOctets": ahRXDataOctets,
       "ahRxMgtFrames": ahRxMgtFrames,
       "ahRxUnicastFrames": ahRxUnicastFrames,
       "ahRxMulticastFrames": ahRxMulticastFrames,
       "ahRxBroadcastFrames": ahRxBroadcastFrames,
       "ahTxDataFrames": ahTxDataFrames,
       "ahTxMgtFrames": ahTxMgtFrames,
       "ahTxDataOctets": ahTxDataOctets,
       "ahTxUnicastFrames": ahTxUnicastFrames,
       "ahTxMulticastFrames": ahTxMulticastFrames,
       "ahTxBroadcastFrames": ahTxBroadcastFrames,
       "ahTxBeDataFrames": ahTxBeDataFrames,
       "ahTxBgDataFrames": ahTxBgDataFrames,
       "ahTxViDataFrames": ahTxViDataFrames,
       "ahTxVoDataFrames": ahTxVoDataFrames}
)
