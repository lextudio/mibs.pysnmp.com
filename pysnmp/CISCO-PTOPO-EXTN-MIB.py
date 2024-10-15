# SNMP MIB module (CISCO-PTOPO-EXTN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-PTOPO-EXTN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:07:16 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(PhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(ptopoConnEntry,) = mibBuilder.importSymbols(
    "PTOPO-MIB",
    "ptopoConnEntry")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ciscoPtopoExtnMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 261)
)
ciscoPtopoExtnMIB.setRevisions(
        ("2002-05-12 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoPtopoExtnMIBObjects_ObjectIdentity = ObjectIdentity
ciscoPtopoExtnMIBObjects = _CiscoPtopoExtnMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 261, 1)
)
_CPtopoConnExtTable_Object = MibTable
cPtopoConnExtTable = _CPtopoConnExtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 261, 1, 1)
)
if mibBuilder.loadTexts:
    cPtopoConnExtTable.setStatus("current")
_CPtopoConnExtEntry_Object = MibTableRow
cPtopoConnExtEntry = _CPtopoConnExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 261, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cPtopoConnExtEntry.setStatus("current")


class _CPtopoConnExtLinkDirection_Type(Integer32):
    """Custom type cPtopoConnExtLinkDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("receive", 2),
          ("transmit", 1))
    )


_CPtopoConnExtLinkDirection_Type.__name__ = "Integer32"
_CPtopoConnExtLinkDirection_Object = MibTableColumn
cPtopoConnExtLinkDirection = _CPtopoConnExtLinkDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 261, 1, 1, 1, 1),
    _CPtopoConnExtLinkDirection_Type()
)
cPtopoConnExtLinkDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cPtopoConnExtLinkDirection.setStatus("current")
_CPtopoExtCdpTable_Object = MibTable
cPtopoExtCdpTable = _CPtopoExtCdpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 261, 1, 2)
)
if mibBuilder.loadTexts:
    cPtopoExtCdpTable.setStatus("current")
_CPtopoExtCdpEntry_Object = MibTableRow
cPtopoExtCdpEntry = _CPtopoExtCdpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 261, 1, 2, 1)
)
cPtopoExtCdpEntry.setIndexNames(
    (0, "CISCO-PTOPO-EXTN-MIB", "cPtopoExtCdpLocalChassis"),
    (0, "CISCO-PTOPO-EXTN-MIB", "cPtopoExtCdpLocalPort"),
)
if mibBuilder.loadTexts:
    cPtopoExtCdpEntry.setStatus("current")
_CPtopoExtCdpLocalChassis_Type = PhysicalIndex
_CPtopoExtCdpLocalChassis_Object = MibTableColumn
cPtopoExtCdpLocalChassis = _CPtopoExtCdpLocalChassis_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 261, 1, 2, 1, 1),
    _CPtopoExtCdpLocalChassis_Type()
)
cPtopoExtCdpLocalChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPtopoExtCdpLocalChassis.setStatus("current")
_CPtopoExtCdpLocalPort_Type = PhysicalIndex
_CPtopoExtCdpLocalPort_Object = MibTableColumn
cPtopoExtCdpLocalPort = _CPtopoExtCdpLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 261, 1, 2, 1, 2),
    _CPtopoExtCdpLocalPort_Type()
)
cPtopoExtCdpLocalPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cPtopoExtCdpLocalPort.setStatus("current")


class _CPtopoExtCdpDiscoveryState_Type(Integer32):
    """Custom type cPtopoExtCdpDiscoveryState based on Integer32"""
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
        *(("cdpDisabled", 1),
          ("discovered", 4),
          ("interfaceDown", 2),
          ("waiting", 3))
    )


_CPtopoExtCdpDiscoveryState_Type.__name__ = "Integer32"
_CPtopoExtCdpDiscoveryState_Object = MibTableColumn
cPtopoExtCdpDiscoveryState = _CPtopoExtCdpDiscoveryState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 261, 1, 2, 1, 3),
    _CPtopoExtCdpDiscoveryState_Type()
)
cPtopoExtCdpDiscoveryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPtopoExtCdpDiscoveryState.setStatus("current")


class _CPtopoExtCdpProxyIf_Type(InterfaceIndexOrZero):
    """Custom type cPtopoExtCdpProxyIf based on InterfaceIndexOrZero"""
    defaultValue = 0


_CPtopoExtCdpProxyIf_Object = MibTableColumn
cPtopoExtCdpProxyIf = _CPtopoExtCdpProxyIf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 261, 1, 2, 1, 4),
    _CPtopoExtCdpProxyIf_Type()
)
cPtopoExtCdpProxyIf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cPtopoExtCdpProxyIf.setStatus("current")
_CPtopoExtCdpRowStatus_Type = RowStatus
_CPtopoExtCdpRowStatus_Object = MibTableColumn
cPtopoExtCdpRowStatus = _CPtopoExtCdpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 261, 1, 2, 1, 5),
    _CPtopoExtCdpRowStatus_Type()
)
cPtopoExtCdpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cPtopoExtCdpRowStatus.setStatus("current")
_CPtopoExtnConformance_ObjectIdentity = ObjectIdentity
cPtopoExtnConformance = _CPtopoExtnConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 261, 3)
)
_CPtopoExtnCompliances_ObjectIdentity = ObjectIdentity
cPtopoExtnCompliances = _CPtopoExtnCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 261, 3, 1)
)
_CPtopoExtnGroups_ObjectIdentity = ObjectIdentity
cPtopoExtnGroups = _CPtopoExtnGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 261, 3, 2)
)
ptopoConnEntry.registerAugmentions(
    ("CISCO-PTOPO-EXTN-MIB",
     "cPtopoConnExtEntry")
)
cPtopoConnExtEntry.setIndexNames(*ptopoConnEntry.getIndexNames())

# Managed Objects groups

cPtopoConnExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 261, 3, 2, 1)
)
cPtopoConnExtGroup.setObjects(
    ("CISCO-PTOPO-EXTN-MIB", "cPtopoConnExtLinkDirection")
)
if mibBuilder.loadTexts:
    cPtopoConnExtGroup.setStatus("current")

cPtopoExtCdpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 261, 3, 2, 2)
)
cPtopoExtCdpGroup.setObjects(
      *(("CISCO-PTOPO-EXTN-MIB", "cPtopoExtCdpDiscoveryState"),
        ("CISCO-PTOPO-EXTN-MIB", "cPtopoExtCdpRowStatus"))
)
if mibBuilder.loadTexts:
    cPtopoExtCdpGroup.setStatus("current")

cPtopoExtCdpProxyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 261, 3, 2, 3)
)
cPtopoExtCdpProxyGroup.setObjects(
    ("CISCO-PTOPO-EXTN-MIB", "cPtopoExtCdpProxyIf")
)
if mibBuilder.loadTexts:
    cPtopoExtCdpProxyGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cPtopoExtnCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 261, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cPtopoExtnCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-PTOPO-EXTN-MIB",
    **{"ciscoPtopoExtnMIB": ciscoPtopoExtnMIB,
       "ciscoPtopoExtnMIBObjects": ciscoPtopoExtnMIBObjects,
       "cPtopoConnExtTable": cPtopoConnExtTable,
       "cPtopoConnExtEntry": cPtopoConnExtEntry,
       "cPtopoConnExtLinkDirection": cPtopoConnExtLinkDirection,
       "cPtopoExtCdpTable": cPtopoExtCdpTable,
       "cPtopoExtCdpEntry": cPtopoExtCdpEntry,
       "cPtopoExtCdpLocalChassis": cPtopoExtCdpLocalChassis,
       "cPtopoExtCdpLocalPort": cPtopoExtCdpLocalPort,
       "cPtopoExtCdpDiscoveryState": cPtopoExtCdpDiscoveryState,
       "cPtopoExtCdpProxyIf": cPtopoExtCdpProxyIf,
       "cPtopoExtCdpRowStatus": cPtopoExtCdpRowStatus,
       "cPtopoExtnConformance": cPtopoExtnConformance,
       "cPtopoExtnCompliances": cPtopoExtnCompliances,
       "cPtopoExtnCompliance": cPtopoExtnCompliance,
       "cPtopoExtnGroups": cPtopoExtnGroups,
       "cPtopoConnExtGroup": cPtopoConnExtGroup,
       "cPtopoExtCdpGroup": cPtopoExtCdpGroup,
       "cPtopoExtCdpProxyGroup": cPtopoExtCdpProxyGroup}
)
