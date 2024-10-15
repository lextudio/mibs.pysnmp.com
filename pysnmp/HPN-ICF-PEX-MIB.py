# SNMP MIB module (HPN-ICF-PEX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-PEX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:01:26 2024
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hpnicfPex = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 129)
)
hpnicfPex.setRevisions(
        ("2012-11-12 11:29",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfPexSpecInfo_ObjectIdentity = ObjectIdentity
hpnicfPexSpecInfo = _HpnicfPexSpecInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 129, 1)
)
_HpnicfPexPortMinId_Type = Integer32
_HpnicfPexPortMinId_Object = MibScalar
hpnicfPexPortMinId = _HpnicfPexPortMinId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 129, 1, 1),
    _HpnicfPexPortMinId_Type()
)
hpnicfPexPortMinId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPexPortMinId.setStatus("current")
_HpnicfPexPortMaxId_Type = Integer32
_HpnicfPexPortMaxId_Object = MibScalar
hpnicfPexPortMaxId = _HpnicfPexPortMaxId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 129, 1, 2),
    _HpnicfPexPortMaxId_Type()
)
hpnicfPexPortMaxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPexPortMaxId.setStatus("current")
_HpnicfPexMinAssociateId_Type = Integer32
_HpnicfPexMinAssociateId_Object = MibScalar
hpnicfPexMinAssociateId = _HpnicfPexMinAssociateId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 129, 1, 3),
    _HpnicfPexMinAssociateId_Type()
)
hpnicfPexMinAssociateId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPexMinAssociateId.setStatus("current")
_HpnicfPexMaxAssociateId_Type = Integer32
_HpnicfPexMaxAssociateId_Object = MibScalar
hpnicfPexMaxAssociateId = _HpnicfPexMaxAssociateId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 129, 1, 4),
    _HpnicfPexMaxAssociateId_Type()
)
hpnicfPexMaxAssociateId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPexMaxAssociateId.setStatus("current")
_HpnicfPexMaxPortPerPexPort_Type = Integer32
_HpnicfPexMaxPortPerPexPort_Object = MibScalar
hpnicfPexMaxPortPerPexPort = _HpnicfPexMaxPortPerPexPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 129, 1, 5),
    _HpnicfPexMaxPortPerPexPort_Type()
)
hpnicfPexMaxPortPerPexPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPexMaxPortPerPexPort.setStatus("current")
_HpnicfPexTable_ObjectIdentity = ObjectIdentity
hpnicfPexTable = _HpnicfPexTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 129, 2)
)
_HpnicfPexPortTable_Object = MibTable
hpnicfPexPortTable = _HpnicfPexPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 129, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfPexPortTable.setStatus("current")
_HpnicfPexPortEntry_Object = MibTableRow
hpnicfPexPortEntry = _HpnicfPexPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 129, 2, 1, 1)
)
hpnicfPexPortEntry.setIndexNames(
    (0, "HPN-ICF-PEX-MIB", "hpnicfPexPortId"),
)
if mibBuilder.loadTexts:
    hpnicfPexPortEntry.setStatus("current")


class _HpnicfPexPortId_Type(Integer32):
    """Custom type hpnicfPexPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfPexPortId_Type.__name__ = "Integer32"
_HpnicfPexPortId_Object = MibTableColumn
hpnicfPexPortId = _HpnicfPexPortId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 129, 2, 1, 1, 1),
    _HpnicfPexPortId_Type()
)
hpnicfPexPortId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfPexPortId.setStatus("current")


class _HpnicfPexPortAssociateId_Type(Integer32):
    """Custom type hpnicfPexPortAssociateId based on Integer32"""
    defaultValue = 65535


_HpnicfPexPortAssociateId_Object = MibTableColumn
hpnicfPexPortAssociateId = _HpnicfPexPortAssociateId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 129, 2, 1, 1, 2),
    _HpnicfPexPortAssociateId_Type()
)
hpnicfPexPortAssociateId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPexPortAssociateId.setStatus("current")


class _HpnicfPexPortEntPhysicalIndex_Type(Integer32):
    """Custom type hpnicfPexPortEntPhysicalIndex based on Integer32"""
    defaultValue = 0


_HpnicfPexPortEntPhysicalIndex_Object = MibTableColumn
hpnicfPexPortEntPhysicalIndex = _HpnicfPexPortEntPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 129, 2, 1, 1, 3),
    _HpnicfPexPortEntPhysicalIndex_Type()
)
hpnicfPexPortEntPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPexPortEntPhysicalIndex.setStatus("current")


class _HpnicfPexPortDescr_Type(DisplayString):
    """Custom type hpnicfPexPortDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_HpnicfPexPortDescr_Type.__name__ = "DisplayString"
_HpnicfPexPortDescr_Object = MibTableColumn
hpnicfPexPortDescr = _HpnicfPexPortDescr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 129, 2, 1, 1, 4),
    _HpnicfPexPortDescr_Type()
)
hpnicfPexPortDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPexPortDescr.setStatus("current")


class _HpnicfPexPortStatus_Type(Integer32):
    """Custom type hpnicfPexPortStatus based on Integer32"""
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


_HpnicfPexPortStatus_Type.__name__ = "Integer32"
_HpnicfPexPortStatus_Object = MibTableColumn
hpnicfPexPortStatus = _HpnicfPexPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 129, 2, 1, 1, 5),
    _HpnicfPexPortStatus_Type()
)
hpnicfPexPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPexPortStatus.setStatus("current")
_HpnicfPexPortRowStatus_Type = RowStatus
_HpnicfPexPortRowStatus_Object = MibTableColumn
hpnicfPexPortRowStatus = _HpnicfPexPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 129, 2, 1, 1, 6),
    _HpnicfPexPortRowStatus_Type()
)
hpnicfPexPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPexPortRowStatus.setStatus("current")
_HpnicfPexPhyPortTable_Object = MibTable
hpnicfPexPhyPortTable = _HpnicfPexPhyPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 129, 2, 2)
)
if mibBuilder.loadTexts:
    hpnicfPexPhyPortTable.setStatus("current")
_HpnicfPexPhyPortEntry_Object = MibTableRow
hpnicfPexPhyPortEntry = _HpnicfPexPhyPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 129, 2, 2, 1)
)
hpnicfPexPhyPortEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    hpnicfPexPhyPortEntry.setStatus("current")


class _HpnicfPexPhyPortStatus_Type(Integer32):
    """Custom type hpnicfPexPhyPortStatus based on Integer32"""
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


_HpnicfPexPhyPortStatus_Type.__name__ = "Integer32"
_HpnicfPexPhyPortStatus_Object = MibTableColumn
hpnicfPexPhyPortStatus = _HpnicfPexPhyPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 129, 2, 2, 1, 1),
    _HpnicfPexPhyPortStatus_Type()
)
hpnicfPexPhyPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPexPhyPortStatus.setStatus("current")


class _HpnicfPexPhyPortBelongToPexPort_Type(Integer32):
    """Custom type hpnicfPexPhyPortBelongToPexPort based on Integer32"""
    defaultValue = 0


_HpnicfPexPhyPortBelongToPexPort_Object = MibTableColumn
hpnicfPexPhyPortBelongToPexPort = _HpnicfPexPhyPortBelongToPexPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 129, 2, 2, 1, 2),
    _HpnicfPexPhyPortBelongToPexPort_Type()
)
hpnicfPexPhyPortBelongToPexPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPexPhyPortBelongToPexPort.setStatus("current")
_HpnicfPexPhyPortNeighborEntIndex_Type = Integer32
_HpnicfPexPhyPortNeighborEntIndex_Object = MibTableColumn
hpnicfPexPhyPortNeighborEntIndex = _HpnicfPexPhyPortNeighborEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 129, 2, 2, 1, 3),
    _HpnicfPexPhyPortNeighborEntIndex_Type()
)
hpnicfPexPhyPortNeighborEntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPexPhyPortNeighborEntIndex.setStatus("current")
_HpnicfPexTraps_ObjectIdentity = ObjectIdentity
hpnicfPexTraps = _HpnicfPexTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 129, 3)
)
_HpnicfPexTrapPrefix_ObjectIdentity = ObjectIdentity
hpnicfPexTrapPrefix = _HpnicfPexTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 129, 3, 0)
)
_HpnicfPexTrapObjects_ObjectIdentity = ObjectIdentity
hpnicfPexTrapObjects = _HpnicfPexTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 129, 4)
)
_HpnicfPexEntPhysicalIndexBind_Type = Integer32
_HpnicfPexEntPhysicalIndexBind_Object = MibScalar
hpnicfPexEntPhysicalIndexBind = _HpnicfPexEntPhysicalIndexBind_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 129, 4, 1),
    _HpnicfPexEntPhysicalIndexBind_Type()
)
hpnicfPexEntPhysicalIndexBind.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfPexEntPhysicalIndexBind.setStatus("current")

# Managed Objects groups


# Notification objects

hpnicfPexPortOnline = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 129, 3, 0, 1)
)
hpnicfPexPortOnline.setObjects(
      *(("HPN-ICF-PEX-MIB", "hpnicfPexPortId"),
        ("HPN-ICF-PEX-MIB", "hpnicfPexPortDescr"))
)
if mibBuilder.loadTexts:
    hpnicfPexPortOnline.setStatus(
        "current"
    )

hpnicfPexPortOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 129, 3, 0, 2)
)
hpnicfPexPortOffline.setObjects(
      *(("HPN-ICF-PEX-MIB", "hpnicfPexPortId"),
        ("HPN-ICF-PEX-MIB", "hpnicfPexPortDescr"))
)
if mibBuilder.loadTexts:
    hpnicfPexPortOffline.setStatus(
        "current"
    )

hpnicfPexPhyPortForwarding = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 129, 3, 0, 3)
)
hpnicfPexPhyPortForwarding.setObjects(
      *(("HPN-ICF-PEX-MIB", "hpnicfPexEntPhysicalIndexBind"),
        ("ENTITY-MIB", "entPhysicalDescr"))
)
if mibBuilder.loadTexts:
    hpnicfPexPhyPortForwarding.setStatus(
        "current"
    )

hpnicfPexPhyPortBlocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 129, 3, 0, 4)
)
hpnicfPexPhyPortBlocked.setObjects(
      *(("HPN-ICF-PEX-MIB", "hpnicfPexEntPhysicalIndexBind"),
        ("ENTITY-MIB", "entPhysicalDescr"))
)
if mibBuilder.loadTexts:
    hpnicfPexPhyPortBlocked.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-PEX-MIB",
    **{"hpnicfPex": hpnicfPex,
       "hpnicfPexSpecInfo": hpnicfPexSpecInfo,
       "hpnicfPexPortMinId": hpnicfPexPortMinId,
       "hpnicfPexPortMaxId": hpnicfPexPortMaxId,
       "hpnicfPexMinAssociateId": hpnicfPexMinAssociateId,
       "hpnicfPexMaxAssociateId": hpnicfPexMaxAssociateId,
       "hpnicfPexMaxPortPerPexPort": hpnicfPexMaxPortPerPexPort,
       "hpnicfPexTable": hpnicfPexTable,
       "hpnicfPexPortTable": hpnicfPexPortTable,
       "hpnicfPexPortEntry": hpnicfPexPortEntry,
       "hpnicfPexPortId": hpnicfPexPortId,
       "hpnicfPexPortAssociateId": hpnicfPexPortAssociateId,
       "hpnicfPexPortEntPhysicalIndex": hpnicfPexPortEntPhysicalIndex,
       "hpnicfPexPortDescr": hpnicfPexPortDescr,
       "hpnicfPexPortStatus": hpnicfPexPortStatus,
       "hpnicfPexPortRowStatus": hpnicfPexPortRowStatus,
       "hpnicfPexPhyPortTable": hpnicfPexPhyPortTable,
       "hpnicfPexPhyPortEntry": hpnicfPexPhyPortEntry,
       "hpnicfPexPhyPortStatus": hpnicfPexPhyPortStatus,
       "hpnicfPexPhyPortBelongToPexPort": hpnicfPexPhyPortBelongToPexPort,
       "hpnicfPexPhyPortNeighborEntIndex": hpnicfPexPhyPortNeighborEntIndex,
       "hpnicfPexTraps": hpnicfPexTraps,
       "hpnicfPexTrapPrefix": hpnicfPexTrapPrefix,
       "hpnicfPexPortOnline": hpnicfPexPortOnline,
       "hpnicfPexPortOffline": hpnicfPexPortOffline,
       "hpnicfPexPhyPortForwarding": hpnicfPexPhyPortForwarding,
       "hpnicfPexPhyPortBlocked": hpnicfPexPhyPortBlocked,
       "hpnicfPexTrapObjects": hpnicfPexTrapObjects,
       "hpnicfPexEntPhysicalIndexBind": hpnicfPexEntPhysicalIndexBind}
)
