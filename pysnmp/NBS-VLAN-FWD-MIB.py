# SNMP MIB module (NBS-VLAN-FWD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NBS-VLAN-FWD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:25:06 2024
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

(InterfaceIndex,
 nbs) = mibBuilder.importSymbols(
    "NBS-CMMC-MIB",
    "InterfaceIndex",
    "nbs")

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

nbsVlanFwdMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 629, 215)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NbsVlanFwdGrp_ObjectIdentity = ObjectIdentity
nbsVlanFwdGrp = _NbsVlanFwdGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 215, 1)
)
if mibBuilder.loadTexts:
    nbsVlanFwdGrp.setStatus("current")
_NbsVlanFwdTableSize_Type = Unsigned32
_NbsVlanFwdTableSize_Object = MibScalar
nbsVlanFwdTableSize = _NbsVlanFwdTableSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 215, 1, 1),
    _NbsVlanFwdTableSize_Type()
)
nbsVlanFwdTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsVlanFwdTableSize.setStatus("current")
_NbsVlanFwdTable_Object = MibTable
nbsVlanFwdTable = _NbsVlanFwdTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 215, 1, 2)
)
if mibBuilder.loadTexts:
    nbsVlanFwdTable.setStatus("current")
_NbsVlanFwdEntry_Object = MibTableRow
nbsVlanFwdEntry = _NbsVlanFwdEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 215, 1, 2, 1)
)
nbsVlanFwdEntry.setIndexNames(
    (0, "NBS-VLAN-FWD-MIB", "nbsVlanFwdIfIndex"),
)
if mibBuilder.loadTexts:
    nbsVlanFwdEntry.setStatus("current")
_NbsVlanFwdIfIndex_Type = InterfaceIndex
_NbsVlanFwdIfIndex_Object = MibTableColumn
nbsVlanFwdIfIndex = _NbsVlanFwdIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 215, 1, 2, 1, 1),
    _NbsVlanFwdIfIndex_Type()
)
nbsVlanFwdIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbsVlanFwdIfIndex.setStatus("current")
_NbsVlanFwdVidList_Type = DisplayString
_NbsVlanFwdVidList_Object = MibTableColumn
nbsVlanFwdVidList = _NbsVlanFwdVidList_Object(
    (1, 3, 6, 1, 4, 1, 629, 215, 1, 2, 1, 2),
    _NbsVlanFwdVidList_Type()
)
nbsVlanFwdVidList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsVlanFwdVidList.setStatus("current")


class _NbsVlanFwdVid_Type(Integer32):
    """Custom type nbsVlanFwdVid based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_NbsVlanFwdVid_Type.__name__ = "Integer32"
_NbsVlanFwdVid_Object = MibTableColumn
nbsVlanFwdVid = _NbsVlanFwdVid_Object(
    (1, 3, 6, 1, 4, 1, 629, 215, 1, 2, 1, 3),
    _NbsVlanFwdVid_Type()
)
nbsVlanFwdVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsVlanFwdVid.setStatus("current")


class _NbsVlanFwdPriority_Type(Integer32):
    """Custom type nbsVlanFwdPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_NbsVlanFwdPriority_Type.__name__ = "Integer32"
_NbsVlanFwdPriority_Object = MibTableColumn
nbsVlanFwdPriority = _NbsVlanFwdPriority_Object(
    (1, 3, 6, 1, 4, 1, 629, 215, 1, 2, 1, 4),
    _NbsVlanFwdPriority_Type()
)
nbsVlanFwdPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsVlanFwdPriority.setStatus("current")


class _NbsVlanFwdEgressTagAction_Type(Integer32):
    """Custom type nbsVlanFwdEgressTagAction based on Integer32"""
    defaultValue = 4

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
        *(("add", 2),
          ("notSupported", 1),
          ("retain", 4),
          ("strip", 3))
    )


_NbsVlanFwdEgressTagAction_Type.__name__ = "Integer32"
_NbsVlanFwdEgressTagAction_Object = MibTableColumn
nbsVlanFwdEgressTagAction = _NbsVlanFwdEgressTagAction_Object(
    (1, 3, 6, 1, 4, 1, 629, 215, 1, 2, 1, 5),
    _NbsVlanFwdEgressTagAction_Type()
)
nbsVlanFwdEgressTagAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsVlanFwdEgressTagAction.setStatus("current")


class _NbsVlanFwdEgressTagCapability_Type(OctetString):
    """Custom type nbsVlanFwdEgressTagCapability based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_NbsVlanFwdEgressTagCapability_Type.__name__ = "OctetString"
_NbsVlanFwdEgressTagCapability_Object = MibTableColumn
nbsVlanFwdEgressTagCapability = _NbsVlanFwdEgressTagCapability_Object(
    (1, 3, 6, 1, 4, 1, 629, 215, 1, 2, 1, 6),
    _NbsVlanFwdEgressTagCapability_Type()
)
nbsVlanFwdEgressTagCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsVlanFwdEgressTagCapability.setStatus("current")


class _NbsVlanFwdIngressTagAction_Type(Integer32):
    """Custom type nbsVlanFwdIngressTagAction based on Integer32"""
    defaultValue = 4

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
        *(("add", 2),
          ("notSupported", 1),
          ("retain", 4),
          ("strip", 3))
    )


_NbsVlanFwdIngressTagAction_Type.__name__ = "Integer32"
_NbsVlanFwdIngressTagAction_Object = MibTableColumn
nbsVlanFwdIngressTagAction = _NbsVlanFwdIngressTagAction_Object(
    (1, 3, 6, 1, 4, 1, 629, 215, 1, 2, 1, 7),
    _NbsVlanFwdIngressTagAction_Type()
)
nbsVlanFwdIngressTagAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsVlanFwdIngressTagAction.setStatus("current")


class _NbsVlanFwdIngressTagCapability_Type(OctetString):
    """Custom type nbsVlanFwdIngressTagCapability based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_NbsVlanFwdIngressTagCapability_Type.__name__ = "OctetString"
_NbsVlanFwdIngressTagCapability_Object = MibTableColumn
nbsVlanFwdIngressTagCapability = _NbsVlanFwdIngressTagCapability_Object(
    (1, 3, 6, 1, 4, 1, 629, 215, 1, 2, 1, 8),
    _NbsVlanFwdIngressTagCapability_Type()
)
nbsVlanFwdIngressTagCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsVlanFwdIngressTagCapability.setStatus("current")
_NbsVlanControlGrp_ObjectIdentity = ObjectIdentity
nbsVlanControlGrp = _NbsVlanControlGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 215, 2)
)
if mibBuilder.loadTexts:
    nbsVlanControlGrp.setStatus("current")
_NbsVlanControlTableSize_Type = Unsigned32
_NbsVlanControlTableSize_Object = MibScalar
nbsVlanControlTableSize = _NbsVlanControlTableSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 215, 2, 1),
    _NbsVlanControlTableSize_Type()
)
nbsVlanControlTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsVlanControlTableSize.setStatus("current")
_NbsVlanControlTable_Object = MibTable
nbsVlanControlTable = _NbsVlanControlTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 215, 2, 2)
)
if mibBuilder.loadTexts:
    nbsVlanControlTable.setStatus("current")
_NbsVlanControlEntry_Object = MibTableRow
nbsVlanControlEntry = _NbsVlanControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 215, 2, 2, 1)
)
nbsVlanControlEntry.setIndexNames(
    (0, "NBS-VLAN-FWD-MIB", "nbsVlanControlIfIndex"),
)
if mibBuilder.loadTexts:
    nbsVlanControlEntry.setStatus("current")
_NbsVlanControlIfIndex_Type = InterfaceIndex
_NbsVlanControlIfIndex_Object = MibTableColumn
nbsVlanControlIfIndex = _NbsVlanControlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 215, 2, 2, 1, 1),
    _NbsVlanControlIfIndex_Type()
)
nbsVlanControlIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbsVlanControlIfIndex.setStatus("current")


class _NbsVlanControlMgmtVid_Type(Integer32):
    """Custom type nbsVlanControlMgmtVid based on Integer32"""
    defaultValue = 4094

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_NbsVlanControlMgmtVid_Type.__name__ = "Integer32"
_NbsVlanControlMgmtVid_Object = MibTableColumn
nbsVlanControlMgmtVid = _NbsVlanControlMgmtVid_Object(
    (1, 3, 6, 1, 4, 1, 629, 215, 2, 2, 1, 2),
    _NbsVlanControlMgmtVid_Type()
)
nbsVlanControlMgmtVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsVlanControlMgmtVid.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NBS-VLAN-FWD-MIB",
    **{"nbsVlanFwdMib": nbsVlanFwdMib,
       "nbsVlanFwdGrp": nbsVlanFwdGrp,
       "nbsVlanFwdTableSize": nbsVlanFwdTableSize,
       "nbsVlanFwdTable": nbsVlanFwdTable,
       "nbsVlanFwdEntry": nbsVlanFwdEntry,
       "nbsVlanFwdIfIndex": nbsVlanFwdIfIndex,
       "nbsVlanFwdVidList": nbsVlanFwdVidList,
       "nbsVlanFwdVid": nbsVlanFwdVid,
       "nbsVlanFwdPriority": nbsVlanFwdPriority,
       "nbsVlanFwdEgressTagAction": nbsVlanFwdEgressTagAction,
       "nbsVlanFwdEgressTagCapability": nbsVlanFwdEgressTagCapability,
       "nbsVlanFwdIngressTagAction": nbsVlanFwdIngressTagAction,
       "nbsVlanFwdIngressTagCapability": nbsVlanFwdIngressTagCapability,
       "nbsVlanControlGrp": nbsVlanControlGrp,
       "nbsVlanControlTableSize": nbsVlanControlTableSize,
       "nbsVlanControlTable": nbsVlanControlTable,
       "nbsVlanControlEntry": nbsVlanControlEntry,
       "nbsVlanControlIfIndex": nbsVlanControlIfIndex,
       "nbsVlanControlMgmtVid": nbsVlanControlMgmtVid}
)
