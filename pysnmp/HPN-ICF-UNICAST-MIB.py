# SNMP MIB module (HPN-ICF-UNICAST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-UNICAST-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:02:04 2024
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpnicfUnicast = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 44)
)
hpnicfUnicast.setRevisions(
        ("2005-03-24 14:54",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfURPFTable_Object = MibTable
hpnicfURPFTable = _HpnicfURPFTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 44, 1)
)
if mibBuilder.loadTexts:
    hpnicfURPFTable.setStatus("current")
_HpnicfURPFEntry_Object = MibTableRow
hpnicfURPFEntry = _HpnicfURPFEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 44, 1, 1)
)
hpnicfURPFEntry.setIndexNames(
    (0, "HPN-ICF-UNICAST-MIB", "hpnicfURPFIfIndex"),
)
if mibBuilder.loadTexts:
    hpnicfURPFEntry.setStatus("current")
_HpnicfURPFIfIndex_Type = Integer32
_HpnicfURPFIfIndex_Object = MibTableColumn
hpnicfURPFIfIndex = _HpnicfURPFIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 44, 1, 1, 1),
    _HpnicfURPFIfIndex_Type()
)
hpnicfURPFIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfURPFIfIndex.setStatus("current")


class _HpnicfURPFEnabled_Type(TruthValue):
    """Custom type hpnicfURPFEnabled based on TruthValue"""


_HpnicfURPFEnabled_Object = MibTableColumn
hpnicfURPFEnabled = _HpnicfURPFEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 44, 1, 1, 2),
    _HpnicfURPFEnabled_Type()
)
hpnicfURPFEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfURPFEnabled.setStatus("current")
_HpnicfURPFSlotID_Type = Integer32
_HpnicfURPFSlotID_Object = MibTableColumn
hpnicfURPFSlotID = _HpnicfURPFSlotID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 44, 1, 1, 3),
    _HpnicfURPFSlotID_Type()
)
hpnicfURPFSlotID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfURPFSlotID.setStatus("current")
_HpnicfURPFTotalReceivedPacket_Type = Counter64
_HpnicfURPFTotalReceivedPacket_Object = MibTableColumn
hpnicfURPFTotalReceivedPacket = _HpnicfURPFTotalReceivedPacket_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 44, 1, 1, 4),
    _HpnicfURPFTotalReceivedPacket_Type()
)
hpnicfURPFTotalReceivedPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfURPFTotalReceivedPacket.setStatus("current")
_HpnicfURPFDroppedPacket_Type = Counter64
_HpnicfURPFDroppedPacket_Object = MibTableColumn
hpnicfURPFDroppedPacket = _HpnicfURPFDroppedPacket_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 44, 1, 1, 5),
    _HpnicfURPFDroppedPacket_Type()
)
hpnicfURPFDroppedPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfURPFDroppedPacket.setStatus("current")


class _HpnicfURPFClearStat_Type(Integer32):
    """Custom type hpnicfURPFClearStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("reserved", 0),
          ("reset", 1))
    )


_HpnicfURPFClearStat_Type.__name__ = "Integer32"
_HpnicfURPFClearStat_Object = MibTableColumn
hpnicfURPFClearStat = _HpnicfURPFClearStat_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 44, 1, 1, 6),
    _HpnicfURPFClearStat_Type()
)
hpnicfURPFClearStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfURPFClearStat.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-UNICAST-MIB",
    **{"hpnicfUnicast": hpnicfUnicast,
       "hpnicfURPFTable": hpnicfURPFTable,
       "hpnicfURPFEntry": hpnicfURPFEntry,
       "hpnicfURPFIfIndex": hpnicfURPFIfIndex,
       "hpnicfURPFEnabled": hpnicfURPFEnabled,
       "hpnicfURPFSlotID": hpnicfURPFSlotID,
       "hpnicfURPFTotalReceivedPacket": hpnicfURPFTotalReceivedPacket,
       "hpnicfURPFDroppedPacket": hpnicfURPFDroppedPacket,
       "hpnicfURPFClearStat": hpnicfURPFClearStat}
)
