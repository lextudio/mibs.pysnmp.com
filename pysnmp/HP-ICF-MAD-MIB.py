# SNMP MIB module (HP-ICF-MAD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-MAD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:57:47 2024
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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

hpicfMadMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 95)
)
hpicfMadMIB.setRevisions(
        ("2012-12-12 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfMadNotifications_ObjectIdentity = ObjectIdentity
hpicfMadNotifications = _HpicfMadNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 95, 0)
)
_HpicfMadObjects_ObjectIdentity = ObjectIdentity
hpicfMadObjects = _HpicfMadObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 95, 1)
)
_HpicfMadLacpAggObjects_ObjectIdentity = ObjectIdentity
hpicfMadLacpAggObjects = _HpicfMadLacpAggObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 95, 1, 1)
)
_HpicfMadLacpAggTable_Object = MibTable
hpicfMadLacpAggTable = _HpicfMadLacpAggTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 95, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfMadLacpAggTable.setStatus("current")
_HpicfMadLacpAggEntry_Object = MibTableRow
hpicfMadLacpAggEntry = _HpicfMadLacpAggEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 95, 1, 1, 1, 1)
)
hpicfMadLacpAggEntry.setIndexNames(
    (0, "HP-ICF-MAD-MIB", "hpicfMadLacpAggTrunkId"),
)
if mibBuilder.loadTexts:
    hpicfMadLacpAggEntry.setStatus("current")


class _HpicfMadLacpAggTrunkId_Type(Integer32):
    """Custom type hpicfMadLacpAggTrunkId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpicfMadLacpAggTrunkId_Type.__name__ = "Integer32"
_HpicfMadLacpAggTrunkId_Object = MibTableColumn
hpicfMadLacpAggTrunkId = _HpicfMadLacpAggTrunkId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 95, 1, 1, 1, 1, 1),
    _HpicfMadLacpAggTrunkId_Type()
)
hpicfMadLacpAggTrunkId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfMadLacpAggTrunkId.setStatus("current")


class _HpicfMadPassthroughLacpAggAdminStatus_Type(Integer32):
    """Custom type hpicfMadPassthroughLacpAggAdminStatus based on Integer32"""
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


_HpicfMadPassthroughLacpAggAdminStatus_Type.__name__ = "Integer32"
_HpicfMadPassthroughLacpAggAdminStatus_Object = MibTableColumn
hpicfMadPassthroughLacpAggAdminStatus = _HpicfMadPassthroughLacpAggAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 95, 1, 1, 1, 1, 2),
    _HpicfMadPassthroughLacpAggAdminStatus_Type()
)
hpicfMadPassthroughLacpAggAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfMadPassthroughLacpAggAdminStatus.setStatus("current")
_HpicfMadLacpAggPortStatsTable_Object = MibTable
hpicfMadLacpAggPortStatsTable = _HpicfMadLacpAggPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 95, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfMadLacpAggPortStatsTable.setStatus("current")
_HpicfMadLacpAggPortStatsEntry_Object = MibTableRow
hpicfMadLacpAggPortStatsEntry = _HpicfMadLacpAggPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 95, 1, 1, 2, 1)
)
hpicfMadLacpAggPortStatsEntry.setIndexNames(
    (0, "HP-ICF-MAD-MIB", "hpicfMadLacpAggPortIndex"),
)
if mibBuilder.loadTexts:
    hpicfMadLacpAggPortStatsEntry.setStatus("current")
_HpicfMadLacpAggPortIndex_Type = InterfaceIndex
_HpicfMadLacpAggPortIndex_Object = MibTableColumn
hpicfMadLacpAggPortIndex = _HpicfMadLacpAggPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 95, 1, 1, 2, 1, 1),
    _HpicfMadLacpAggPortIndex_Type()
)
hpicfMadLacpAggPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfMadLacpAggPortIndex.setStatus("current")
_HpicfMadPassthroughLacpAggPDUsRx_Type = Counter32
_HpicfMadPassthroughLacpAggPDUsRx_Object = MibTableColumn
hpicfMadPassthroughLacpAggPDUsRx = _HpicfMadPassthroughLacpAggPDUsRx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 95, 1, 1, 2, 1, 2),
    _HpicfMadPassthroughLacpAggPDUsRx_Type()
)
hpicfMadPassthroughLacpAggPDUsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMadPassthroughLacpAggPDUsRx.setStatus("current")
_HpicfMadPassthroughLacpAggPDUsTx_Type = Counter32
_HpicfMadPassthroughLacpAggPDUsTx_Object = MibTableColumn
hpicfMadPassthroughLacpAggPDUsTx = _HpicfMadPassthroughLacpAggPDUsTx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 95, 1, 1, 2, 1, 3),
    _HpicfMadPassthroughLacpAggPDUsTx_Type()
)
hpicfMadPassthroughLacpAggPDUsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMadPassthroughLacpAggPDUsTx.setStatus("current")
_HpicfMadPassthroughLacpAggPDUsDropped_Type = Counter32
_HpicfMadPassthroughLacpAggPDUsDropped_Object = MibTableColumn
hpicfMadPassthroughLacpAggPDUsDropped = _HpicfMadPassthroughLacpAggPDUsDropped_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 95, 1, 1, 2, 1, 4),
    _HpicfMadPassthroughLacpAggPDUsDropped_Type()
)
hpicfMadPassthroughLacpAggPDUsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfMadPassthroughLacpAggPDUsDropped.setStatus("current")
_HpicfMadConformance_ObjectIdentity = ObjectIdentity
hpicfMadConformance = _HpicfMadConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 95, 2)
)
_HpicfMadLacpAggGoups_ObjectIdentity = ObjectIdentity
hpicfMadLacpAggGoups = _HpicfMadLacpAggGoups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 95, 2, 1)
)
_HpicfMadLacpAggCompliances_ObjectIdentity = ObjectIdentity
hpicfMadLacpAggCompliances = _HpicfMadLacpAggCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 95, 2, 2)
)

# Managed Objects groups

hpicfMadLacpAggConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 95, 2, 1, 1)
)
hpicfMadLacpAggConfigGroup.setObjects(
    ("HP-ICF-MAD-MIB", "hpicfMadPassthroughLacpAggAdminStatus")
)
if mibBuilder.loadTexts:
    hpicfMadLacpAggConfigGroup.setStatus("current")

hpicfMadLacpAggStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 95, 2, 1, 2)
)
hpicfMadLacpAggStatisticsGroup.setObjects(
      *(("HP-ICF-MAD-MIB", "hpicfMadPassthroughLacpAggPDUsRx"),
        ("HP-ICF-MAD-MIB", "hpicfMadPassthroughLacpAggPDUsTx"),
        ("HP-ICF-MAD-MIB", "hpicfMadPassthroughLacpAggPDUsDropped"))
)
if mibBuilder.loadTexts:
    hpicfMadLacpAggStatisticsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfMadLacpAggCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 95, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hpicfMadLacpAggCompliance1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-MAD-MIB",
    **{"hpicfMadMIB": hpicfMadMIB,
       "hpicfMadNotifications": hpicfMadNotifications,
       "hpicfMadObjects": hpicfMadObjects,
       "hpicfMadLacpAggObjects": hpicfMadLacpAggObjects,
       "hpicfMadLacpAggTable": hpicfMadLacpAggTable,
       "hpicfMadLacpAggEntry": hpicfMadLacpAggEntry,
       "hpicfMadLacpAggTrunkId": hpicfMadLacpAggTrunkId,
       "hpicfMadPassthroughLacpAggAdminStatus": hpicfMadPassthroughLacpAggAdminStatus,
       "hpicfMadLacpAggPortStatsTable": hpicfMadLacpAggPortStatsTable,
       "hpicfMadLacpAggPortStatsEntry": hpicfMadLacpAggPortStatsEntry,
       "hpicfMadLacpAggPortIndex": hpicfMadLacpAggPortIndex,
       "hpicfMadPassthroughLacpAggPDUsRx": hpicfMadPassthroughLacpAggPDUsRx,
       "hpicfMadPassthroughLacpAggPDUsTx": hpicfMadPassthroughLacpAggPDUsTx,
       "hpicfMadPassthroughLacpAggPDUsDropped": hpicfMadPassthroughLacpAggPDUsDropped,
       "hpicfMadConformance": hpicfMadConformance,
       "hpicfMadLacpAggGoups": hpicfMadLacpAggGoups,
       "hpicfMadLacpAggConfigGroup": hpicfMadLacpAggConfigGroup,
       "hpicfMadLacpAggStatisticsGroup": hpicfMadLacpAggStatisticsGroup,
       "hpicfMadLacpAggCompliances": hpicfMadLacpAggCompliances,
       "hpicfMadLacpAggCompliance1": hpicfMadLacpAggCompliance1}
)
