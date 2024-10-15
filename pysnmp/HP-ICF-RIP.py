# SNMP MIB module (HP-ICF-RIP) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-RIP
# Produced by pysmi-1.5.4 at Mon Oct 14 21:58:04 2024
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

(IANAipRouteProtocol,) = mibBuilder.importSymbols(
    "IANA-RTPROTO-MIB",
    "IANAipRouteProtocol")

(rip2IfConfEntry,) = mibBuilder.importSymbols(
    "RIPv2-MIB",
    "rip2IfConfEntry")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpicfRip = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 13)
)
hpicfRip.setRevisions(
        ("2003-05-13 02:17",
         "2001-11-13 03:39")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfRipObjects_ObjectIdentity = ObjectIdentity
hpicfRipObjects = _HpicfRipObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 13, 1)
)
_HpicfRipGeneral_ObjectIdentity = ObjectIdentity
hpicfRipGeneral = _HpicfRipGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 13, 1, 1)
)


class _HpicfRipAdminStatus_Type(Integer32):
    """Custom type hpicfRipAdminStatus based on Integer32"""
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


_HpicfRipAdminStatus_Type.__name__ = "Integer32"
_HpicfRipAdminStatus_Object = MibScalar
hpicfRipAdminStatus = _HpicfRipAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 13, 1, 1, 1),
    _HpicfRipAdminStatus_Type()
)
hpicfRipAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfRipAdminStatus.setStatus("current")


class _HpicfRipDefaultMetric_Type(Integer32):
    """Custom type hpicfRipDefaultMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_HpicfRipDefaultMetric_Type.__name__ = "Integer32"
_HpicfRipDefaultMetric_Object = MibScalar
hpicfRipDefaultMetric = _HpicfRipDefaultMetric_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 13, 1, 1, 2),
    _HpicfRipDefaultMetric_Type()
)
hpicfRipDefaultMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfRipDefaultMetric.setStatus("current")
_HpicfRipAutoSummary_Type = TruthValue
_HpicfRipAutoSummary_Object = MibScalar
hpicfRipAutoSummary = _HpicfRipAutoSummary_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 13, 1, 1, 3),
    _HpicfRipAutoSummary_Type()
)
hpicfRipAutoSummary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfRipAutoSummary.setStatus("current")


class _HpicfRipDistance_Type(Integer32):
    """Custom type hpicfRipDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HpicfRipDistance_Type.__name__ = "Integer32"
_HpicfRipDistance_Object = MibScalar
hpicfRipDistance = _HpicfRipDistance_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 13, 1, 1, 4),
    _HpicfRipDistance_Type()
)
hpicfRipDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfRipDistance.setStatus("current")
_HpicfRipIfConfTable_Object = MibTable
hpicfRipIfConfTable = _HpicfRipIfConfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 13, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfRipIfConfTable.setStatus("current")
_HpicfRipIfConfEntry_Object = MibTableRow
hpicfRipIfConfEntry = _HpicfRipIfConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 13, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hpicfRipIfConfEntry.setStatus("current")


class _HpicfRipIfConfDoPoison_Type(TruthValue):
    """Custom type hpicfRipIfConfDoPoison based on TruthValue"""


_HpicfRipIfConfDoPoison_Object = MibTableColumn
hpicfRipIfConfDoPoison = _HpicfRipIfConfDoPoison_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 13, 1, 2, 1, 1),
    _HpicfRipIfConfDoPoison_Type()
)
hpicfRipIfConfDoPoison.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfRipIfConfDoPoison.setStatus("current")


class _HpicfRipIfConfCost_Type(Integer32):
    """Custom type hpicfRipIfConfCost based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_HpicfRipIfConfCost_Type.__name__ = "Integer32"
_HpicfRipIfConfCost_Object = MibTableColumn
hpicfRipIfConfCost = _HpicfRipIfConfCost_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 13, 1, 2, 1, 2),
    _HpicfRipIfConfCost_Type()
)
hpicfRipIfConfCost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfRipIfConfCost.setStatus("current")
_HpicfRipRedistTable_Object = MibTable
hpicfRipRedistTable = _HpicfRipRedistTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 13, 1, 3)
)
if mibBuilder.loadTexts:
    hpicfRipRedistTable.setStatus("current")
_HpicfRipRedistEntry_Object = MibTableRow
hpicfRipRedistEntry = _HpicfRipRedistEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 13, 1, 3, 1)
)
hpicfRipRedistEntry.setIndexNames(
    (0, "HP-ICF-RIP", "hpicfRipRedistSrcProto"),
)
if mibBuilder.loadTexts:
    hpicfRipRedistEntry.setStatus("current")
_HpicfRipRedistSrcProto_Type = IANAipRouteProtocol
_HpicfRipRedistSrcProto_Object = MibTableColumn
hpicfRipRedistSrcProto = _HpicfRipRedistSrcProto_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 13, 1, 3, 1, 1),
    _HpicfRipRedistSrcProto_Type()
)
hpicfRipRedistSrcProto.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfRipRedistSrcProto.setStatus("current")
_HpicfRipRedistEnabled_Type = TruthValue
_HpicfRipRedistEnabled_Object = MibTableColumn
hpicfRipRedistEnabled = _HpicfRipRedistEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 13, 1, 3, 1, 2),
    _HpicfRipRedistEnabled_Type()
)
hpicfRipRedistEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfRipRedistEnabled.setStatus("current")
_HpicfRipRedistRestrictTable_Object = MibTable
hpicfRipRedistRestrictTable = _HpicfRipRedistRestrictTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 13, 1, 4)
)
if mibBuilder.loadTexts:
    hpicfRipRedistRestrictTable.setStatus("current")
_HpicfRipRedistRestrictEntry_Object = MibTableRow
hpicfRipRedistRestrictEntry = _HpicfRipRedistRestrictEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 13, 1, 4, 1)
)
hpicfRipRedistRestrictEntry.setIndexNames(
    (0, "HP-ICF-RIP", "hpicfRipRedistRestrictAddr"),
    (0, "HP-ICF-RIP", "hpicfRipRedistRestrictMask"),
)
if mibBuilder.loadTexts:
    hpicfRipRedistRestrictEntry.setStatus("current")
_HpicfRipRedistRestrictAddr_Type = IpAddress
_HpicfRipRedistRestrictAddr_Object = MibTableColumn
hpicfRipRedistRestrictAddr = _HpicfRipRedistRestrictAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 13, 1, 4, 1, 1),
    _HpicfRipRedistRestrictAddr_Type()
)
hpicfRipRedistRestrictAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfRipRedistRestrictAddr.setStatus("current")
_HpicfRipRedistRestrictMask_Type = IpAddress
_HpicfRipRedistRestrictMask_Object = MibTableColumn
hpicfRipRedistRestrictMask = _HpicfRipRedistRestrictMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 13, 1, 4, 1, 2),
    _HpicfRipRedistRestrictMask_Type()
)
hpicfRipRedistRestrictMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfRipRedistRestrictMask.setStatus("current")
_HpicfRipRedistRestrictStatus_Type = RowStatus
_HpicfRipRedistRestrictStatus_Object = MibTableColumn
hpicfRipRedistRestrictStatus = _HpicfRipRedistRestrictStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 13, 1, 4, 1, 3),
    _HpicfRipRedistRestrictStatus_Type()
)
hpicfRipRedistRestrictStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfRipRedistRestrictStatus.setStatus("current")
_HpicfRipConformance_ObjectIdentity = ObjectIdentity
hpicfRipConformance = _HpicfRipConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 13, 2)
)
_HpicfRipGroups_ObjectIdentity = ObjectIdentity
hpicfRipGroups = _HpicfRipGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 13, 2, 1)
)
_HpicfRipCompliances_ObjectIdentity = ObjectIdentity
hpicfRipCompliances = _HpicfRipCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 13, 2, 2)
)
rip2IfConfEntry.registerAugmentions(
    ("HP-ICF-RIP",
     "hpicfRipIfConfEntry")
)
hpicfRipIfConfEntry.setIndexNames(*rip2IfConfEntry.getIndexNames())

# Managed Objects groups

hpicfRipBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 13, 2, 1, 1)
)
hpicfRipBaseGroup.setObjects(
      *(("HP-ICF-RIP", "hpicfRipAdminStatus"),
        ("HP-ICF-RIP", "hpicfRipDefaultMetric"),
        ("HP-ICF-RIP", "hpicfRipAutoSummary"))
)
if mibBuilder.loadTexts:
    hpicfRipBaseGroup.setStatus("current")

hpicfRipIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 13, 2, 1, 2)
)
hpicfRipIfGroup.setObjects(
      *(("HP-ICF-RIP", "hpicfRipIfConfDoPoison"),
        ("HP-ICF-RIP", "hpicfRipIfConfCost"))
)
if mibBuilder.loadTexts:
    hpicfRipIfGroup.setStatus("current")

hpicfRipRedistGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 13, 2, 1, 3)
)
hpicfRipRedistGroup.setObjects(
      *(("HP-ICF-RIP", "hpicfRipRedistEnabled"),
        ("HP-ICF-RIP", "hpicfRipRedistRestrictStatus"))
)
if mibBuilder.loadTexts:
    hpicfRipRedistGroup.setStatus("current")

hpicfRipDistanceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 13, 2, 1, 4)
)
hpicfRipDistanceGroup.setObjects(
    ("HP-ICF-RIP", "hpicfRipDistance")
)
if mibBuilder.loadTexts:
    hpicfRipDistanceGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfRipCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 13, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hpicfRipCompliance.setStatus(
        "current"
    )

hpicfRipDistanceCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 13, 2, 2, 2)
)
if mibBuilder.loadTexts:
    hpicfRipDistanceCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-RIP",
    **{"hpicfRip": hpicfRip,
       "hpicfRipObjects": hpicfRipObjects,
       "hpicfRipGeneral": hpicfRipGeneral,
       "hpicfRipAdminStatus": hpicfRipAdminStatus,
       "hpicfRipDefaultMetric": hpicfRipDefaultMetric,
       "hpicfRipAutoSummary": hpicfRipAutoSummary,
       "hpicfRipDistance": hpicfRipDistance,
       "hpicfRipIfConfTable": hpicfRipIfConfTable,
       "hpicfRipIfConfEntry": hpicfRipIfConfEntry,
       "hpicfRipIfConfDoPoison": hpicfRipIfConfDoPoison,
       "hpicfRipIfConfCost": hpicfRipIfConfCost,
       "hpicfRipRedistTable": hpicfRipRedistTable,
       "hpicfRipRedistEntry": hpicfRipRedistEntry,
       "hpicfRipRedistSrcProto": hpicfRipRedistSrcProto,
       "hpicfRipRedistEnabled": hpicfRipRedistEnabled,
       "hpicfRipRedistRestrictTable": hpicfRipRedistRestrictTable,
       "hpicfRipRedistRestrictEntry": hpicfRipRedistRestrictEntry,
       "hpicfRipRedistRestrictAddr": hpicfRipRedistRestrictAddr,
       "hpicfRipRedistRestrictMask": hpicfRipRedistRestrictMask,
       "hpicfRipRedistRestrictStatus": hpicfRipRedistRestrictStatus,
       "hpicfRipConformance": hpicfRipConformance,
       "hpicfRipGroups": hpicfRipGroups,
       "hpicfRipBaseGroup": hpicfRipBaseGroup,
       "hpicfRipIfGroup": hpicfRipIfGroup,
       "hpicfRipRedistGroup": hpicfRipRedistGroup,
       "hpicfRipDistanceGroup": hpicfRipDistanceGroup,
       "hpicfRipCompliances": hpicfRipCompliances,
       "hpicfRipCompliance": hpicfRipCompliance,
       "hpicfRipDistanceCompliance": hpicfRipDistanceCompliance}
)
