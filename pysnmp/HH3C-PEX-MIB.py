# SNMP MIB module (HH3C-PEX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-PEX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:54:27 2024
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

(entPhysicalDescr,
 entPhysicalIndex) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalDescr",
    "entPhysicalIndex")

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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

hh3cPex = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 129)
)
hh3cPex.setRevisions(
        ("2012-11-12 11:29",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cPexSpecInfo_ObjectIdentity = ObjectIdentity
hh3cPexSpecInfo = _Hh3cPexSpecInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 129, 1)
)
_Hh3cPexPortMinId_Type = Integer32
_Hh3cPexPortMinId_Object = MibScalar
hh3cPexPortMinId = _Hh3cPexPortMinId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 129, 1, 1),
    _Hh3cPexPortMinId_Type()
)
hh3cPexPortMinId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPexPortMinId.setStatus("current")
_Hh3cPexPortMaxId_Type = Integer32
_Hh3cPexPortMaxId_Object = MibScalar
hh3cPexPortMaxId = _Hh3cPexPortMaxId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 129, 1, 2),
    _Hh3cPexPortMaxId_Type()
)
hh3cPexPortMaxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPexPortMaxId.setStatus("current")
_Hh3cPexMinAssociateId_Type = Integer32
_Hh3cPexMinAssociateId_Object = MibScalar
hh3cPexMinAssociateId = _Hh3cPexMinAssociateId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 129, 1, 3),
    _Hh3cPexMinAssociateId_Type()
)
hh3cPexMinAssociateId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPexMinAssociateId.setStatus("current")
_Hh3cPexMaxAssociateId_Type = Integer32
_Hh3cPexMaxAssociateId_Object = MibScalar
hh3cPexMaxAssociateId = _Hh3cPexMaxAssociateId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 129, 1, 4),
    _Hh3cPexMaxAssociateId_Type()
)
hh3cPexMaxAssociateId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPexMaxAssociateId.setStatus("current")
_Hh3cPexMaxPortPerPexPort_Type = Integer32
_Hh3cPexMaxPortPerPexPort_Object = MibScalar
hh3cPexMaxPortPerPexPort = _Hh3cPexMaxPortPerPexPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 129, 1, 5),
    _Hh3cPexMaxPortPerPexPort_Type()
)
hh3cPexMaxPortPerPexPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPexMaxPortPerPexPort.setStatus("current")
_Hh3cPexTable_ObjectIdentity = ObjectIdentity
hh3cPexTable = _Hh3cPexTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 129, 2)
)
_Hh3cPexPortTable_Object = MibTable
hh3cPexPortTable = _Hh3cPexPortTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 129, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cPexPortTable.setStatus("current")
_Hh3cPexPortEntry_Object = MibTableRow
hh3cPexPortEntry = _Hh3cPexPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 129, 2, 1, 1)
)
hh3cPexPortEntry.setIndexNames(
    (0, "HH3C-PEX-MIB", "hh3cPexPortId"),
)
if mibBuilder.loadTexts:
    hh3cPexPortEntry.setStatus("current")


class _Hh3cPexPortId_Type(Integer32):
    """Custom type hh3cPexPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cPexPortId_Type.__name__ = "Integer32"
_Hh3cPexPortId_Object = MibTableColumn
hh3cPexPortId = _Hh3cPexPortId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 129, 2, 1, 1, 1),
    _Hh3cPexPortId_Type()
)
hh3cPexPortId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cPexPortId.setStatus("current")


class _Hh3cPexPortAssociateId_Type(Integer32):
    """Custom type hh3cPexPortAssociateId based on Integer32"""
    defaultValue = 65535


_Hh3cPexPortAssociateId_Object = MibTableColumn
hh3cPexPortAssociateId = _Hh3cPexPortAssociateId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 129, 2, 1, 1, 2),
    _Hh3cPexPortAssociateId_Type()
)
hh3cPexPortAssociateId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPexPortAssociateId.setStatus("current")


class _Hh3cPexPortEntPhysicalIndex_Type(Integer32):
    """Custom type hh3cPexPortEntPhysicalIndex based on Integer32"""
    defaultValue = 0


_Hh3cPexPortEntPhysicalIndex_Object = MibTableColumn
hh3cPexPortEntPhysicalIndex = _Hh3cPexPortEntPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 129, 2, 1, 1, 3),
    _Hh3cPexPortEntPhysicalIndex_Type()
)
hh3cPexPortEntPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPexPortEntPhysicalIndex.setStatus("current")


class _Hh3cPexPortDescr_Type(DisplayString):
    """Custom type hh3cPexPortDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_Hh3cPexPortDescr_Type.__name__ = "DisplayString"
_Hh3cPexPortDescr_Object = MibTableColumn
hh3cPexPortDescr = _Hh3cPexPortDescr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 129, 2, 1, 1, 4),
    _Hh3cPexPortDescr_Type()
)
hh3cPexPortDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPexPortDescr.setStatus("current")


class _Hh3cPexPortStatus_Type(Integer32):
    """Custom type hh3cPexPortStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("loading", 2),
          ("offline", 1),
          ("online", 3))
    )


_Hh3cPexPortStatus_Type.__name__ = "Integer32"
_Hh3cPexPortStatus_Object = MibTableColumn
hh3cPexPortStatus = _Hh3cPexPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 129, 2, 1, 1, 5),
    _Hh3cPexPortStatus_Type()
)
hh3cPexPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPexPortStatus.setStatus("current")
_Hh3cPexPortRowStatus_Type = RowStatus
_Hh3cPexPortRowStatus_Object = MibTableColumn
hh3cPexPortRowStatus = _Hh3cPexPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 129, 2, 1, 1, 6),
    _Hh3cPexPortRowStatus_Type()
)
hh3cPexPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPexPortRowStatus.setStatus("current")
_Hh3cPexPhyPortTable_Object = MibTable
hh3cPexPhyPortTable = _Hh3cPexPhyPortTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 129, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cPexPhyPortTable.setStatus("current")
_Hh3cPexPhyPortEntry_Object = MibTableRow
hh3cPexPhyPortEntry = _Hh3cPexPhyPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 129, 2, 2, 1)
)
hh3cPexPhyPortEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    hh3cPexPhyPortEntry.setStatus("current")


class _Hh3cPexPhyPortStatus_Type(Integer32):
    """Custom type hh3cPexPhyPortStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 3),
          ("down", 2),
          ("forwarding", 4),
          ("unknown", 1))
    )


_Hh3cPexPhyPortStatus_Type.__name__ = "Integer32"
_Hh3cPexPhyPortStatus_Object = MibTableColumn
hh3cPexPhyPortStatus = _Hh3cPexPhyPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 129, 2, 2, 1, 1),
    _Hh3cPexPhyPortStatus_Type()
)
hh3cPexPhyPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPexPhyPortStatus.setStatus("current")


class _Hh3cPexPhyPortBelongToPexPort_Type(Integer32):
    """Custom type hh3cPexPhyPortBelongToPexPort based on Integer32"""
    defaultValue = 0


_Hh3cPexPhyPortBelongToPexPort_Object = MibTableColumn
hh3cPexPhyPortBelongToPexPort = _Hh3cPexPhyPortBelongToPexPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 129, 2, 2, 1, 2),
    _Hh3cPexPhyPortBelongToPexPort_Type()
)
hh3cPexPhyPortBelongToPexPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPexPhyPortBelongToPexPort.setStatus("current")
_Hh3cPexPhyPortNeighborEntIndex_Type = Integer32
_Hh3cPexPhyPortNeighborEntIndex_Object = MibTableColumn
hh3cPexPhyPortNeighborEntIndex = _Hh3cPexPhyPortNeighborEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 129, 2, 2, 1, 3),
    _Hh3cPexPhyPortNeighborEntIndex_Type()
)
hh3cPexPhyPortNeighborEntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPexPhyPortNeighborEntIndex.setStatus("current")
_Hh3cPexTraps_ObjectIdentity = ObjectIdentity
hh3cPexTraps = _Hh3cPexTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 129, 3)
)
_Hh3cPexTrapPrefix_ObjectIdentity = ObjectIdentity
hh3cPexTrapPrefix = _Hh3cPexTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 129, 3, 0)
)
_Hh3cPexTrapObjects_ObjectIdentity = ObjectIdentity
hh3cPexTrapObjects = _Hh3cPexTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 129, 4)
)
_Hh3cPexEntPhysicalIndexBind_Type = Integer32
_Hh3cPexEntPhysicalIndexBind_Object = MibScalar
hh3cPexEntPhysicalIndexBind = _Hh3cPexEntPhysicalIndexBind_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 129, 4, 1),
    _Hh3cPexEntPhysicalIndexBind_Type()
)
hh3cPexEntPhysicalIndexBind.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cPexEntPhysicalIndexBind.setStatus("current")

# Managed Objects groups


# Notification objects

hh3cPexPortOnline = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 129, 3, 0, 1)
)
hh3cPexPortOnline.setObjects(
      *(("HH3C-PEX-MIB", "hh3cPexPortId"),
        ("HH3C-PEX-MIB", "hh3cPexPortDescr"))
)
if mibBuilder.loadTexts:
    hh3cPexPortOnline.setStatus(
        "current"
    )

hh3cPexPortOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 129, 3, 0, 2)
)
hh3cPexPortOffline.setObjects(
      *(("HH3C-PEX-MIB", "hh3cPexPortId"),
        ("HH3C-PEX-MIB", "hh3cPexPortDescr"))
)
if mibBuilder.loadTexts:
    hh3cPexPortOffline.setStatus(
        "current"
    )

hh3cPexPhyPortForwarding = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 129, 3, 0, 3)
)
hh3cPexPhyPortForwarding.setObjects(
      *(("HH3C-PEX-MIB", "hh3cPexEntPhysicalIndexBind"),
        ("ENTITY-MIB", "entPhysicalDescr"))
)
if mibBuilder.loadTexts:
    hh3cPexPhyPortForwarding.setStatus(
        "current"
    )

hh3cPexPhyPortBlocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 129, 3, 0, 4)
)
hh3cPexPhyPortBlocked.setObjects(
      *(("HH3C-PEX-MIB", "hh3cPexEntPhysicalIndexBind"),
        ("ENTITY-MIB", "entPhysicalDescr"))
)
if mibBuilder.loadTexts:
    hh3cPexPhyPortBlocked.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-PEX-MIB",
    **{"hh3cPex": hh3cPex,
       "hh3cPexSpecInfo": hh3cPexSpecInfo,
       "hh3cPexPortMinId": hh3cPexPortMinId,
       "hh3cPexPortMaxId": hh3cPexPortMaxId,
       "hh3cPexMinAssociateId": hh3cPexMinAssociateId,
       "hh3cPexMaxAssociateId": hh3cPexMaxAssociateId,
       "hh3cPexMaxPortPerPexPort": hh3cPexMaxPortPerPexPort,
       "hh3cPexTable": hh3cPexTable,
       "hh3cPexPortTable": hh3cPexPortTable,
       "hh3cPexPortEntry": hh3cPexPortEntry,
       "hh3cPexPortId": hh3cPexPortId,
       "hh3cPexPortAssociateId": hh3cPexPortAssociateId,
       "hh3cPexPortEntPhysicalIndex": hh3cPexPortEntPhysicalIndex,
       "hh3cPexPortDescr": hh3cPexPortDescr,
       "hh3cPexPortStatus": hh3cPexPortStatus,
       "hh3cPexPortRowStatus": hh3cPexPortRowStatus,
       "hh3cPexPhyPortTable": hh3cPexPhyPortTable,
       "hh3cPexPhyPortEntry": hh3cPexPhyPortEntry,
       "hh3cPexPhyPortStatus": hh3cPexPhyPortStatus,
       "hh3cPexPhyPortBelongToPexPort": hh3cPexPhyPortBelongToPexPort,
       "hh3cPexPhyPortNeighborEntIndex": hh3cPexPhyPortNeighborEntIndex,
       "hh3cPexTraps": hh3cPexTraps,
       "hh3cPexTrapPrefix": hh3cPexTrapPrefix,
       "hh3cPexPortOnline": hh3cPexPortOnline,
       "hh3cPexPortOffline": hh3cPexPortOffline,
       "hh3cPexPhyPortForwarding": hh3cPexPhyPortForwarding,
       "hh3cPexPhyPortBlocked": hh3cPexPhyPortBlocked,
       "hh3cPexTrapObjects": hh3cPexTrapObjects,
       "hh3cPexEntPhysicalIndexBind": hh3cPexEntPhysicalIndexBind}
)
