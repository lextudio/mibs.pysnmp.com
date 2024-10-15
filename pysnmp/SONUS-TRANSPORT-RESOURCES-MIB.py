# SNMP MIB module (SONUS-TRANSPORT-RESOURCES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SONUS-TRANSPORT-RESOURCES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:57:14 2024
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

(sonusResourcesMIBs,) = mibBuilder.importSymbols(
    "SONUS-SMI",
    "sonusResourcesMIBs")


# MODULE-IDENTITY

sonusTransportResourcesMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SonusTransportResourcesMIBObjects_ObjectIdentity = ObjectIdentity
sonusTransportResourcesMIBObjects = _SonusTransportResourcesMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 4, 1)
)
_SonusNifStatTable_Object = MibTable
sonusNifStatTable = _SonusNifStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 4, 1, 1)
)
if mibBuilder.loadTexts:
    sonusNifStatTable.setStatus("current")
_SonusNifStatEntry_Object = MibTableRow
sonusNifStatEntry = _SonusNifStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 4, 1, 1, 1)
)
sonusNifStatEntry.setIndexNames(
    (0, "SONUS-TRANSPORT-RESOURCES-MIB", "sonusNifStatNifIndex"),
)
if mibBuilder.loadTexts:
    sonusNifStatEntry.setStatus("current")
_SonusNifStatNifIndex_Type = Integer32
_SonusNifStatNifIndex_Object = MibTableColumn
sonusNifStatNifIndex = _SonusNifStatNifIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 4, 1, 1, 1, 1),
    _SonusNifStatNifIndex_Type()
)
sonusNifStatNifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNifStatNifIndex.setStatus("current")


class _SonusNifStatState_Type(Integer32):
    """Custom type sonusNifStatState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dryUp", 3),
          ("inService", 2),
          ("outOfService", 1))
    )


_SonusNifStatState_Type.__name__ = "Integer32"
_SonusNifStatState_Object = MibTableColumn
sonusNifStatState = _SonusNifStatState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 4, 1, 1, 1, 2),
    _SonusNifStatState_Type()
)
sonusNifStatState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNifStatState.setStatus("current")
_SonusNifStatCallNum_Type = Integer32
_SonusNifStatCallNum_Object = MibTableColumn
sonusNifStatCallNum = _SonusNifStatCallNum_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 4, 1, 1, 1, 3),
    _SonusNifStatCallNum_Type()
)
sonusNifStatCallNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNifStatCallNum.setStatus("current")
_SonusNifStatResNum_Type = Integer32
_SonusNifStatResNum_Object = MibTableColumn
sonusNifStatResNum = _SonusNifStatResNum_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 4, 1, 1, 1, 4),
    _SonusNifStatResNum_Type()
)
sonusNifStatResNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNifStatResNum.setStatus("current")
_SonusNifStatSpeedCur_Type = Integer32
_SonusNifStatSpeedCur_Object = MibTableColumn
sonusNifStatSpeedCur = _SonusNifStatSpeedCur_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 4, 1, 1, 1, 5),
    _SonusNifStatSpeedCur_Type()
)
sonusNifStatSpeedCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNifStatSpeedCur.setStatus("current")
_SonusNifStatSpeedMax_Type = Integer32
_SonusNifStatSpeedMax_Object = MibTableColumn
sonusNifStatSpeedMax = _SonusNifStatSpeedMax_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 4, 1, 1, 1, 6),
    _SonusNifStatSpeedMax_Type()
)
sonusNifStatSpeedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNifStatSpeedMax.setStatus("current")
_SonusNifStatSpeedActual_Type = Integer32
_SonusNifStatSpeedActual_Object = MibTableColumn
sonusNifStatSpeedActual = _SonusNifStatSpeedActual_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 4, 1, 1, 1, 7),
    _SonusNifStatSpeedActual_Type()
)
sonusNifStatSpeedActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNifStatSpeedActual.setStatus("current")
_SonusNifStatSpeedDeviation_Type = Integer32
_SonusNifStatSpeedDeviation_Object = MibTableColumn
sonusNifStatSpeedDeviation = _SonusNifStatSpeedDeviation_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 4, 1, 1, 1, 8),
    _SonusNifStatSpeedDeviation_Type()
)
sonusNifStatSpeedDeviation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNifStatSpeedDeviation.setStatus("current")
_SonusPnsAdmnTable_Object = MibTable
sonusPnsAdmnTable = _SonusPnsAdmnTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 4, 1, 2)
)
if mibBuilder.loadTexts:
    sonusPnsAdmnTable.setStatus("current")
_SonusPnsAdmnEntry_Object = MibTableRow
sonusPnsAdmnEntry = _SonusPnsAdmnEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 4, 1, 2, 1)
)
sonusPnsAdmnEntry.setIndexNames(
    (0, "SONUS-TRANSPORT-RESOURCES-MIB", "sonusPnsAdmnShelf"),
    (0, "SONUS-TRANSPORT-RESOURCES-MIB", "sonusPnsAdmnSlot"),
)
if mibBuilder.loadTexts:
    sonusPnsAdmnEntry.setStatus("current")


class _SonusPnsAdmnShelf_Type(Integer32):
    """Custom type sonusPnsAdmnShelf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_SonusPnsAdmnShelf_Type.__name__ = "Integer32"
_SonusPnsAdmnShelf_Object = MibTableColumn
sonusPnsAdmnShelf = _SonusPnsAdmnShelf_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 4, 1, 2, 1, 1),
    _SonusPnsAdmnShelf_Type()
)
sonusPnsAdmnShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusPnsAdmnShelf.setStatus("current")


class _SonusPnsAdmnSlot_Type(Integer32):
    """Custom type sonusPnsAdmnSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SonusPnsAdmnSlot_Type.__name__ = "Integer32"
_SonusPnsAdmnSlot_Object = MibTableColumn
sonusPnsAdmnSlot = _SonusPnsAdmnSlot_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 4, 1, 2, 1, 2),
    _SonusPnsAdmnSlot_Type()
)
sonusPnsAdmnSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusPnsAdmnSlot.setStatus("current")


class _SonusPnsAdmnReservedUdpPorts_Type(Integer32):
    """Custom type sonusPnsAdmnReservedUdpPorts based on Integer32"""
    defaultValue = 5120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SonusPnsAdmnReservedUdpPorts_Type.__name__ = "Integer32"
_SonusPnsAdmnReservedUdpPorts_Object = MibTableColumn
sonusPnsAdmnReservedUdpPorts = _SonusPnsAdmnReservedUdpPorts_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 4, 1, 2, 1, 3),
    _SonusPnsAdmnReservedUdpPorts_Type()
)
sonusPnsAdmnReservedUdpPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusPnsAdmnReservedUdpPorts.setStatus("current")
_SonusPnsAdmnRowStatus_Type = RowStatus
_SonusPnsAdmnRowStatus_Object = MibTableColumn
sonusPnsAdmnRowStatus = _SonusPnsAdmnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 4, 1, 2, 1, 4),
    _SonusPnsAdmnRowStatus_Type()
)
sonusPnsAdmnRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusPnsAdmnRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SONUS-TRANSPORT-RESOURCES-MIB",
    **{"sonusTransportResourcesMIB": sonusTransportResourcesMIB,
       "sonusTransportResourcesMIBObjects": sonusTransportResourcesMIBObjects,
       "sonusNifStatTable": sonusNifStatTable,
       "sonusNifStatEntry": sonusNifStatEntry,
       "sonusNifStatNifIndex": sonusNifStatNifIndex,
       "sonusNifStatState": sonusNifStatState,
       "sonusNifStatCallNum": sonusNifStatCallNum,
       "sonusNifStatResNum": sonusNifStatResNum,
       "sonusNifStatSpeedCur": sonusNifStatSpeedCur,
       "sonusNifStatSpeedMax": sonusNifStatSpeedMax,
       "sonusNifStatSpeedActual": sonusNifStatSpeedActual,
       "sonusNifStatSpeedDeviation": sonusNifStatSpeedDeviation,
       "sonusPnsAdmnTable": sonusPnsAdmnTable,
       "sonusPnsAdmnEntry": sonusPnsAdmnEntry,
       "sonusPnsAdmnShelf": sonusPnsAdmnShelf,
       "sonusPnsAdmnSlot": sonusPnsAdmnSlot,
       "sonusPnsAdmnReservedUdpPorts": sonusPnsAdmnReservedUdpPorts,
       "sonusPnsAdmnRowStatus": sonusPnsAdmnRowStatus}
)
