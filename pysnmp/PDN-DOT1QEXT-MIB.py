# SNMP MIB module (PDN-DOT1QEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PDN-DOT1QEXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:37:32 2024
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

(pdn_dot1q,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "pdn-dot1q")

(TblCmd,) = mibBuilder.importSymbols(
    "PDN-TC",
    "TblCmd")

(dot1qVlanStaticEntry,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "dot1qVlanStaticEntry")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

pdnDot1qExt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 39, 1)
)
pdnDot1qExt.setRevisions(
        ("2005-07-26 00:00",
         "2003-11-12 00:00",
         "2002-11-30 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PdnDot1qExtObjects_ObjectIdentity = ObjectIdentity
pdnDot1qExtObjects = _PdnDot1qExtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 39, 1, 1)
)
_PdnDot1qVlanStaticExtTable_Object = MibTable
pdnDot1qVlanStaticExtTable = _PdnDot1qVlanStaticExtTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 39, 1, 1, 1)
)
if mibBuilder.loadTexts:
    pdnDot1qVlanStaticExtTable.setStatus("current")
_PdnDot1qVlanStaticExtEntry_Object = MibTableRow
pdnDot1qVlanStaticExtEntry = _PdnDot1qVlanStaticExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 39, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    pdnDot1qVlanStaticExtEntry.setStatus("current")


class _PdnDot1qVlanStaticSecureModeStatus_Type(Integer32):
    """Custom type pdnDot1qVlanStaticSecureModeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_PdnDot1qVlanStaticSecureModeStatus_Type.__name__ = "Integer32"
_PdnDot1qVlanStaticSecureModeStatus_Object = MibTableColumn
pdnDot1qVlanStaticSecureModeStatus = _PdnDot1qVlanStaticSecureModeStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 39, 1, 1, 1, 1, 1),
    _PdnDot1qVlanStaticSecureModeStatus_Type()
)
pdnDot1qVlanStaticSecureModeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnDot1qVlanStaticSecureModeStatus.setStatus("current")


class _PdnDot1qVlanStaticProxyArpStatus_Type(Integer32):
    """Custom type pdnDot1qVlanStaticProxyArpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_PdnDot1qVlanStaticProxyArpStatus_Type.__name__ = "Integer32"
_PdnDot1qVlanStaticProxyArpStatus_Object = MibTableColumn
pdnDot1qVlanStaticProxyArpStatus = _PdnDot1qVlanStaticProxyArpStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 39, 1, 1, 1, 1, 2),
    _PdnDot1qVlanStaticProxyArpStatus_Type()
)
pdnDot1qVlanStaticProxyArpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnDot1qVlanStaticProxyArpStatus.setStatus("current")
_PdnDot1qVlanStaticUplink_Type = Integer32
_PdnDot1qVlanStaticUplink_Object = MibTableColumn
pdnDot1qVlanStaticUplink = _PdnDot1qVlanStaticUplink_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 39, 1, 1, 1, 1, 3),
    _PdnDot1qVlanStaticUplink_Type()
)
pdnDot1qVlanStaticUplink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnDot1qVlanStaticUplink.setStatus("current")
_PdnDot1qVlanStaticDefaultNHR_Type = IpAddress
_PdnDot1qVlanStaticDefaultNHR_Object = MibTableColumn
pdnDot1qVlanStaticDefaultNHR = _PdnDot1qVlanStaticDefaultNHR_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 39, 1, 1, 1, 1, 4),
    _PdnDot1qVlanStaticDefaultNHR_Type()
)
pdnDot1qVlanStaticDefaultNHR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnDot1qVlanStaticDefaultNHR.setStatus("current")


class _PdnDot1qVlanStaticOuterTag_Type(Integer32):
    """Custom type pdnDot1qVlanStaticOuterTag based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_PdnDot1qVlanStaticOuterTag_Type.__name__ = "Integer32"
_PdnDot1qVlanStaticOuterTag_Object = MibTableColumn
pdnDot1qVlanStaticOuterTag = _PdnDot1qVlanStaticOuterTag_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 39, 1, 1, 1, 1, 5),
    _PdnDot1qVlanStaticOuterTag_Type()
)
pdnDot1qVlanStaticOuterTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnDot1qVlanStaticOuterTag.setStatus("current")


class _PdnDot1qVlanStaticOuterDefaultPriority_Type(Integer32):
    """Custom type pdnDot1qVlanStaticOuterDefaultPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PdnDot1qVlanStaticOuterDefaultPriority_Type.__name__ = "Integer32"
_PdnDot1qVlanStaticOuterDefaultPriority_Object = MibTableColumn
pdnDot1qVlanStaticOuterDefaultPriority = _PdnDot1qVlanStaticOuterDefaultPriority_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 39, 1, 1, 1, 1, 6),
    _PdnDot1qVlanStaticOuterDefaultPriority_Type()
)
pdnDot1qVlanStaticOuterDefaultPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnDot1qVlanStaticOuterDefaultPriority.setStatus("current")


class _PdnDot1qVlanStaticOuterEthertype_Type(Integer32):
    """Custom type pdnDot1qVlanStaticOuterEthertype based on Integer32"""
    defaultValue = 33024

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PdnDot1qVlanStaticOuterEthertype_Type.__name__ = "Integer32"
_PdnDot1qVlanStaticOuterEthertype_Object = MibTableColumn
pdnDot1qVlanStaticOuterEthertype = _PdnDot1qVlanStaticOuterEthertype_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 39, 1, 1, 1, 1, 7),
    _PdnDot1qVlanStaticOuterEthertype_Type()
)
pdnDot1qVlanStaticOuterEthertype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnDot1qVlanStaticOuterEthertype.setStatus("current")
_PdnDot1BasePortPIWGTable_Object = MibTable
pdnDot1BasePortPIWGTable = _PdnDot1BasePortPIWGTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 39, 1, 1, 2)
)
if mibBuilder.loadTexts:
    pdnDot1BasePortPIWGTable.setStatus("current")
_PdnDot1BasePortPIWGEntry_Object = MibTableRow
pdnDot1BasePortPIWGEntry = _PdnDot1BasePortPIWGEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 39, 1, 1, 2, 1)
)
pdnDot1BasePortPIWGEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "PDN-DOT1QEXT-MIB", "pdnDot1BasePort"),
)
if mibBuilder.loadTexts:
    pdnDot1BasePortPIWGEntry.setStatus("current")


class _PdnDot1BasePort_Type(Unsigned32):
    """Custom type pdnDot1BasePort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PdnDot1BasePort_Type.__name__ = "Unsigned32"
_PdnDot1BasePort_Object = MibTableColumn
pdnDot1BasePort = _PdnDot1BasePort_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 39, 1, 1, 2, 1, 1),
    _PdnDot1BasePort_Type()
)
pdnDot1BasePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdnDot1BasePort.setStatus("current")


class _PdnDot1BasePortPIWGId_Type(Unsigned32):
    """Custom type pdnDot1BasePortPIWGId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_PdnDot1BasePortPIWGId_Type.__name__ = "Unsigned32"
_PdnDot1BasePortPIWGId_Object = MibTableColumn
pdnDot1BasePortPIWGId = _PdnDot1BasePortPIWGId_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 39, 1, 1, 2, 1, 2),
    _PdnDot1BasePortPIWGId_Type()
)
pdnDot1BasePortPIWGId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnDot1BasePortPIWGId.setStatus("current")
_PdnDot1BasePortPIWGCircuit_Type = ObjectIdentifier
_PdnDot1BasePortPIWGCircuit_Object = MibTableColumn
pdnDot1BasePortPIWGCircuit = _PdnDot1BasePortPIWGCircuit_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 39, 1, 1, 2, 1, 3),
    _PdnDot1BasePortPIWGCircuit_Type()
)
pdnDot1BasePortPIWGCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnDot1BasePortPIWGCircuit.setStatus("current")
_PdnDot1TpFdbClear_Type = TblCmd
_PdnDot1TpFdbClear_Object = MibScalar
pdnDot1TpFdbClear = _PdnDot1TpFdbClear_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 39, 1, 1, 3),
    _PdnDot1TpFdbClear_Type()
)
pdnDot1TpFdbClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnDot1TpFdbClear.setStatus("current")
_PdnDot1qExtConformance_ObjectIdentity = ObjectIdentity
pdnDot1qExtConformance = _PdnDot1qExtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 39, 1, 2)
)
_PdnDot1qExtGroups_ObjectIdentity = ObjectIdentity
pdnDot1qExtGroups = _PdnDot1qExtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 39, 1, 2, 1)
)
_PdnDot1qExtCompliances_ObjectIdentity = ObjectIdentity
pdnDot1qExtCompliances = _PdnDot1qExtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 39, 1, 2, 2)
)
dot1qVlanStaticEntry.registerAugmentions(
    ("PDN-DOT1QEXT-MIB",
     "pdnDot1qVlanStaticExtEntry")
)
pdnDot1qVlanStaticExtEntry.setIndexNames(*dot1qVlanStaticEntry.getIndexNames())

# Managed Objects groups

pdnDot1qVlanExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 39, 1, 2, 1, 1)
)
pdnDot1qVlanExtGroup.setObjects(
      *(("PDN-DOT1QEXT-MIB", "pdnDot1qVlanStaticSecureModeStatus"),
        ("PDN-DOT1QEXT-MIB", "pdnDot1qVlanStaticProxyArpStatus"),
        ("PDN-DOT1QEXT-MIB", "pdnDot1qVlanStaticUplink"),
        ("PDN-DOT1QEXT-MIB", "pdnDot1qVlanStaticDefaultNHR"))
)
if mibBuilder.loadTexts:
    pdnDot1qVlanExtGroup.setStatus("current")

pdnDot1BasePortPIWGGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 39, 1, 2, 1, 2)
)
pdnDot1BasePortPIWGGroup.setObjects(
      *(("PDN-DOT1QEXT-MIB", "pdnDot1BasePortPIWGId"),
        ("PDN-DOT1QEXT-MIB", "pdnDot1BasePortPIWGCircuit"))
)
if mibBuilder.loadTexts:
    pdnDot1BasePortPIWGGroup.setStatus("current")

pdnDot1GeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 39, 1, 2, 1, 3)
)
pdnDot1GeneralGroup.setObjects(
    ("PDN-DOT1QEXT-MIB", "pdnDot1TpFdbClear")
)
if mibBuilder.loadTexts:
    pdnDot1GeneralGroup.setStatus("current")

pdnDot1dVlanStackingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 39, 1, 2, 1, 4)
)
pdnDot1dVlanStackingGroup.setObjects(
      *(("PDN-DOT1QEXT-MIB", "pdnDot1qVlanStaticOuterTag"),
        ("PDN-DOT1QEXT-MIB", "pdnDot1qVlanStaticOuterDefaultPriority"),
        ("PDN-DOT1QEXT-MIB", "pdnDot1qVlanStaticOuterEthertype"))
)
if mibBuilder.loadTexts:
    pdnDot1dVlanStackingGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pdnDot1qExtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 39, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    pdnDot1qExtCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDN-DOT1QEXT-MIB",
    **{"pdnDot1qExt": pdnDot1qExt,
       "pdnDot1qExtObjects": pdnDot1qExtObjects,
       "pdnDot1qVlanStaticExtTable": pdnDot1qVlanStaticExtTable,
       "pdnDot1qVlanStaticExtEntry": pdnDot1qVlanStaticExtEntry,
       "pdnDot1qVlanStaticSecureModeStatus": pdnDot1qVlanStaticSecureModeStatus,
       "pdnDot1qVlanStaticProxyArpStatus": pdnDot1qVlanStaticProxyArpStatus,
       "pdnDot1qVlanStaticUplink": pdnDot1qVlanStaticUplink,
       "pdnDot1qVlanStaticDefaultNHR": pdnDot1qVlanStaticDefaultNHR,
       "pdnDot1qVlanStaticOuterTag": pdnDot1qVlanStaticOuterTag,
       "pdnDot1qVlanStaticOuterDefaultPriority": pdnDot1qVlanStaticOuterDefaultPriority,
       "pdnDot1qVlanStaticOuterEthertype": pdnDot1qVlanStaticOuterEthertype,
       "pdnDot1BasePortPIWGTable": pdnDot1BasePortPIWGTable,
       "pdnDot1BasePortPIWGEntry": pdnDot1BasePortPIWGEntry,
       "pdnDot1BasePort": pdnDot1BasePort,
       "pdnDot1BasePortPIWGId": pdnDot1BasePortPIWGId,
       "pdnDot1BasePortPIWGCircuit": pdnDot1BasePortPIWGCircuit,
       "pdnDot1TpFdbClear": pdnDot1TpFdbClear,
       "pdnDot1qExtConformance": pdnDot1qExtConformance,
       "pdnDot1qExtGroups": pdnDot1qExtGroups,
       "pdnDot1qVlanExtGroup": pdnDot1qVlanExtGroup,
       "pdnDot1BasePortPIWGGroup": pdnDot1BasePortPIWGGroup,
       "pdnDot1GeneralGroup": pdnDot1GeneralGroup,
       "pdnDot1dVlanStackingGroup": pdnDot1dVlanStackingGroup,
       "pdnDot1qExtCompliances": pdnDot1qExtCompliances,
       "pdnDot1qExtCompliance": pdnDot1qExtCompliance}
)
