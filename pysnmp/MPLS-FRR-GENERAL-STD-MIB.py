# SNMP MIB module (MPLS-FRR-GENERAL-STD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MPLS-FRR-GENERAL-STD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:22:55 2024
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

(InterfaceIndexOrZero,
 ifCounterDiscontinuityGroup,
 ifGeneralInformationGroup) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifCounterDiscontinuityGroup",
    "ifGeneralInformationGroup")

(MplsBitRate,
 MplsTunnelAffinity,
 MplsTunnelIndex,
 MplsTunnelInstanceIndex) = mibBuilder.importSymbols(
    "MPLS-TC-STD-MIB",
    "MplsBitRate",
    "MplsTunnelAffinity",
    "MplsTunnelIndex",
    "MplsTunnelInstanceIndex")

(mplsTunnelARHopIndex,
 mplsTunnelARHopListIndex,
 mplsTunnelGroup,
 mplsTunnelScalarGroup) = mibBuilder.importSymbols(
    "MPLS-TE-STD-MIB",
    "mplsTunnelARHopIndex",
    "mplsTunnelARHopListIndex",
    "mplsTunnelGroup",
    "mplsTunnelScalarGroup")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 RowStatus,
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

mplsFrrGeneralMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 202)
)
mplsFrrGeneralMIB.setRevisions(
        ("2011-11-03 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MplsFrrGeneralObjects_ObjectIdentity = ObjectIdentity
mplsFrrGeneralObjects = _MplsFrrGeneralObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 202, 1)
)


class _MplsFrrGeneralProtectionMethod_Type(Integer32):
    """Custom type mplsFrrGeneralProtectionMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("facilityBackup", 3),
          ("oneToOneBackup", 2),
          ("unknown", 1))
    )


_MplsFrrGeneralProtectionMethod_Type.__name__ = "Integer32"
_MplsFrrGeneralProtectionMethod_Object = MibScalar
mplsFrrGeneralProtectionMethod = _MplsFrrGeneralProtectionMethod_Object(
    (1, 3, 6, 1, 2, 1, 202, 1, 1),
    _MplsFrrGeneralProtectionMethod_Type()
)
mplsFrrGeneralProtectionMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mplsFrrGeneralProtectionMethod.setStatus("current")
_MplsFrrGeneralIngressTunnelInstances_Type = Counter32
_MplsFrrGeneralIngressTunnelInstances_Object = MibScalar
mplsFrrGeneralIngressTunnelInstances = _MplsFrrGeneralIngressTunnelInstances_Object(
    (1, 3, 6, 1, 2, 1, 202, 1, 2),
    _MplsFrrGeneralIngressTunnelInstances_Type()
)
mplsFrrGeneralIngressTunnelInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsFrrGeneralIngressTunnelInstances.setStatus("current")
_MplsFrrGeneralConstraintsTable_Object = MibTable
mplsFrrGeneralConstraintsTable = _MplsFrrGeneralConstraintsTable_Object(
    (1, 3, 6, 1, 2, 1, 202, 1, 3)
)
if mibBuilder.loadTexts:
    mplsFrrGeneralConstraintsTable.setStatus("current")
_MplsFrrGeneralConstraintsEntry_Object = MibTableRow
mplsFrrGeneralConstraintsEntry = _MplsFrrGeneralConstraintsEntry_Object(
    (1, 3, 6, 1, 2, 1, 202, 1, 3, 1)
)
mplsFrrGeneralConstraintsEntry.setIndexNames(
    (0, "MPLS-FRR-GENERAL-STD-MIB", "mplsFrrGeneralConstraintsIfIndexOrZero"),
    (0, "MPLS-FRR-GENERAL-STD-MIB", "mplsFrrGeneralConstraintsTunnelIndex"),
    (0, "MPLS-FRR-GENERAL-STD-MIB", "mplsFrrGeneralConstraintsTunnelInstance"),
)
if mibBuilder.loadTexts:
    mplsFrrGeneralConstraintsEntry.setStatus("current")
_MplsFrrGeneralConstraintsIfIndexOrZero_Type = InterfaceIndexOrZero
_MplsFrrGeneralConstraintsIfIndexOrZero_Object = MibTableColumn
mplsFrrGeneralConstraintsIfIndexOrZero = _MplsFrrGeneralConstraintsIfIndexOrZero_Object(
    (1, 3, 6, 1, 2, 1, 202, 1, 3, 1, 1),
    _MplsFrrGeneralConstraintsIfIndexOrZero_Type()
)
mplsFrrGeneralConstraintsIfIndexOrZero.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsFrrGeneralConstraintsIfIndexOrZero.setStatus("current")
_MplsFrrGeneralConstraintsTunnelIndex_Type = MplsTunnelIndex
_MplsFrrGeneralConstraintsTunnelIndex_Object = MibTableColumn
mplsFrrGeneralConstraintsTunnelIndex = _MplsFrrGeneralConstraintsTunnelIndex_Object(
    (1, 3, 6, 1, 2, 1, 202, 1, 3, 1, 2),
    _MplsFrrGeneralConstraintsTunnelIndex_Type()
)
mplsFrrGeneralConstraintsTunnelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsFrrGeneralConstraintsTunnelIndex.setStatus("current")
_MplsFrrGeneralConstraintsTunnelInstance_Type = MplsTunnelInstanceIndex
_MplsFrrGeneralConstraintsTunnelInstance_Object = MibTableColumn
mplsFrrGeneralConstraintsTunnelInstance = _MplsFrrGeneralConstraintsTunnelInstance_Object(
    (1, 3, 6, 1, 2, 1, 202, 1, 3, 1, 3),
    _MplsFrrGeneralConstraintsTunnelInstance_Type()
)
mplsFrrGeneralConstraintsTunnelInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mplsFrrGeneralConstraintsTunnelInstance.setStatus("current")


class _MplsFrrGeneralConstraintsProtectionType_Type(Integer32):
    """Custom type mplsFrrGeneralConstraintsProtectionType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkProtection", 1),
          ("nodeProtection", 2))
    )


_MplsFrrGeneralConstraintsProtectionType_Type.__name__ = "Integer32"
_MplsFrrGeneralConstraintsProtectionType_Object = MibTableColumn
mplsFrrGeneralConstraintsProtectionType = _MplsFrrGeneralConstraintsProtectionType_Object(
    (1, 3, 6, 1, 2, 1, 202, 1, 3, 1, 4),
    _MplsFrrGeneralConstraintsProtectionType_Type()
)
mplsFrrGeneralConstraintsProtectionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsFrrGeneralConstraintsProtectionType.setStatus("current")


class _MplsFrrGeneralConstraintsSetupPrio_Type(Unsigned32):
    """Custom type mplsFrrGeneralConstraintsSetupPrio based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MplsFrrGeneralConstraintsSetupPrio_Type.__name__ = "Unsigned32"
_MplsFrrGeneralConstraintsSetupPrio_Object = MibTableColumn
mplsFrrGeneralConstraintsSetupPrio = _MplsFrrGeneralConstraintsSetupPrio_Object(
    (1, 3, 6, 1, 2, 1, 202, 1, 3, 1, 5),
    _MplsFrrGeneralConstraintsSetupPrio_Type()
)
mplsFrrGeneralConstraintsSetupPrio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsFrrGeneralConstraintsSetupPrio.setStatus("current")


class _MplsFrrGeneralConstraintsHoldingPrio_Type(Unsigned32):
    """Custom type mplsFrrGeneralConstraintsHoldingPrio based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MplsFrrGeneralConstraintsHoldingPrio_Type.__name__ = "Unsigned32"
_MplsFrrGeneralConstraintsHoldingPrio_Object = MibTableColumn
mplsFrrGeneralConstraintsHoldingPrio = _MplsFrrGeneralConstraintsHoldingPrio_Object(
    (1, 3, 6, 1, 2, 1, 202, 1, 3, 1, 6),
    _MplsFrrGeneralConstraintsHoldingPrio_Type()
)
mplsFrrGeneralConstraintsHoldingPrio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsFrrGeneralConstraintsHoldingPrio.setStatus("current")


class _MplsFrrGeneralConstraintsInclAnyAffinity_Type(MplsTunnelAffinity):
    """Custom type mplsFrrGeneralConstraintsInclAnyAffinity based on MplsTunnelAffinity"""
    defaultValue = 0


_MplsFrrGeneralConstraintsInclAnyAffinity_Object = MibTableColumn
mplsFrrGeneralConstraintsInclAnyAffinity = _MplsFrrGeneralConstraintsInclAnyAffinity_Object(
    (1, 3, 6, 1, 2, 1, 202, 1, 3, 1, 7),
    _MplsFrrGeneralConstraintsInclAnyAffinity_Type()
)
mplsFrrGeneralConstraintsInclAnyAffinity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsFrrGeneralConstraintsInclAnyAffinity.setStatus("current")


class _MplsFrrGeneralConstraintsInclAllAffinity_Type(MplsTunnelAffinity):
    """Custom type mplsFrrGeneralConstraintsInclAllAffinity based on MplsTunnelAffinity"""
    defaultValue = 0


_MplsFrrGeneralConstraintsInclAllAffinity_Object = MibTableColumn
mplsFrrGeneralConstraintsInclAllAffinity = _MplsFrrGeneralConstraintsInclAllAffinity_Object(
    (1, 3, 6, 1, 2, 1, 202, 1, 3, 1, 8),
    _MplsFrrGeneralConstraintsInclAllAffinity_Type()
)
mplsFrrGeneralConstraintsInclAllAffinity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsFrrGeneralConstraintsInclAllAffinity.setStatus("current")


class _MplsFrrGeneralConstraintsExclAnyAffinity_Type(MplsTunnelAffinity):
    """Custom type mplsFrrGeneralConstraintsExclAnyAffinity based on MplsTunnelAffinity"""
    defaultValue = 0


_MplsFrrGeneralConstraintsExclAnyAffinity_Object = MibTableColumn
mplsFrrGeneralConstraintsExclAnyAffinity = _MplsFrrGeneralConstraintsExclAnyAffinity_Object(
    (1, 3, 6, 1, 2, 1, 202, 1, 3, 1, 9),
    _MplsFrrGeneralConstraintsExclAnyAffinity_Type()
)
mplsFrrGeneralConstraintsExclAnyAffinity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsFrrGeneralConstraintsExclAnyAffinity.setStatus("current")


class _MplsFrrGeneralConstraintsHopLimit_Type(Unsigned32):
    """Custom type mplsFrrGeneralConstraintsHopLimit based on Unsigned32"""
    defaultValue = 32

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MplsFrrGeneralConstraintsHopLimit_Type.__name__ = "Unsigned32"
_MplsFrrGeneralConstraintsHopLimit_Object = MibTableColumn
mplsFrrGeneralConstraintsHopLimit = _MplsFrrGeneralConstraintsHopLimit_Object(
    (1, 3, 6, 1, 2, 1, 202, 1, 3, 1, 10),
    _MplsFrrGeneralConstraintsHopLimit_Type()
)
mplsFrrGeneralConstraintsHopLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsFrrGeneralConstraintsHopLimit.setStatus("current")


class _MplsFrrGeneralConstraintsBandwidth_Type(MplsBitRate):
    """Custom type mplsFrrGeneralConstraintsBandwidth based on MplsBitRate"""
    defaultValue = 0


_MplsFrrGeneralConstraintsBandwidth_Object = MibTableColumn
mplsFrrGeneralConstraintsBandwidth = _MplsFrrGeneralConstraintsBandwidth_Object(
    (1, 3, 6, 1, 2, 1, 202, 1, 3, 1, 11),
    _MplsFrrGeneralConstraintsBandwidth_Type()
)
mplsFrrGeneralConstraintsBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsFrrGeneralConstraintsBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    mplsFrrGeneralConstraintsBandwidth.setUnits("kilobits per second")


class _MplsFrrGeneralConstraintsStorageType_Type(StorageType):
    """Custom type mplsFrrGeneralConstraintsStorageType based on StorageType"""


_MplsFrrGeneralConstraintsStorageType_Object = MibTableColumn
mplsFrrGeneralConstraintsStorageType = _MplsFrrGeneralConstraintsStorageType_Object(
    (1, 3, 6, 1, 2, 1, 202, 1, 3, 1, 12),
    _MplsFrrGeneralConstraintsStorageType_Type()
)
mplsFrrGeneralConstraintsStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsFrrGeneralConstraintsStorageType.setStatus("current")
_MplsFrrGeneralConstraintsRowStatus_Type = RowStatus
_MplsFrrGeneralConstraintsRowStatus_Object = MibTableColumn
mplsFrrGeneralConstraintsRowStatus = _MplsFrrGeneralConstraintsRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 202, 1, 3, 1, 13),
    _MplsFrrGeneralConstraintsRowStatus_Type()
)
mplsFrrGeneralConstraintsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsFrrGeneralConstraintsRowStatus.setStatus("current")
_MplsFrrGeneralTunnelARHopTable_Object = MibTable
mplsFrrGeneralTunnelARHopTable = _MplsFrrGeneralTunnelARHopTable_Object(
    (1, 3, 6, 1, 2, 1, 202, 1, 4)
)
if mibBuilder.loadTexts:
    mplsFrrGeneralTunnelARHopTable.setStatus("current")
_MplsFrrGeneralTunnelARHopEntry_Object = MibTableRow
mplsFrrGeneralTunnelARHopEntry = _MplsFrrGeneralTunnelARHopEntry_Object(
    (1, 3, 6, 1, 2, 1, 202, 1, 4, 1)
)
mplsFrrGeneralTunnelARHopEntry.setIndexNames(
    (0, "MPLS-TE-STD-MIB", "mplsTunnelARHopListIndex"),
    (0, "MPLS-TE-STD-MIB", "mplsTunnelARHopIndex"),
)
if mibBuilder.loadTexts:
    mplsFrrGeneralTunnelARHopEntry.setStatus("current")


class _MplsFrrGeneralTunnelARHopSessionAttributeFlags_Type(Bits):
    """Custom type mplsFrrGeneralTunnelARHopSessionAttributeFlags based on Bits"""
    namedValues = NamedValues(
        *(("arHopSessionAttrFlagsUnsupported", 0),
          ("bandwidthProtectionDesired", 4),
          ("labelRecordingDesired", 2),
          ("localProtectionDesired", 1),
          ("nodeProtectionDesired", 5),
          ("sestyleDesired", 3))
    )

_MplsFrrGeneralTunnelARHopSessionAttributeFlags_Type.__name__ = "Bits"
_MplsFrrGeneralTunnelARHopSessionAttributeFlags_Object = MibTableColumn
mplsFrrGeneralTunnelARHopSessionAttributeFlags = _MplsFrrGeneralTunnelARHopSessionAttributeFlags_Object(
    (1, 3, 6, 1, 2, 1, 202, 1, 4, 1, 1),
    _MplsFrrGeneralTunnelARHopSessionAttributeFlags_Type()
)
mplsFrrGeneralTunnelARHopSessionAttributeFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsFrrGeneralTunnelARHopSessionAttributeFlags.setStatus("current")


class _MplsFrrGeneralTunnelARHopRROSubObjectFlags_Type(Bits):
    """Custom type mplsFrrGeneralTunnelARHopRROSubObjectFlags based on Bits"""
    namedValues = NamedValues(
        *(("arHopRROSubObjectFlagsUnsupported", 0),
          ("bandwidthProtection", 3),
          ("localProtectionAvailable", 1),
          ("localProtectionInUse", 2),
          ("nodeProtection", 4))
    )

_MplsFrrGeneralTunnelARHopRROSubObjectFlags_Type.__name__ = "Bits"
_MplsFrrGeneralTunnelARHopRROSubObjectFlags_Object = MibTableColumn
mplsFrrGeneralTunnelARHopRROSubObjectFlags = _MplsFrrGeneralTunnelARHopRROSubObjectFlags_Object(
    (1, 3, 6, 1, 2, 1, 202, 1, 4, 1, 2),
    _MplsFrrGeneralTunnelARHopRROSubObjectFlags_Type()
)
mplsFrrGeneralTunnelARHopRROSubObjectFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsFrrGeneralTunnelARHopRROSubObjectFlags.setStatus("current")
_MplsFrrGeneralConformance_ObjectIdentity = ObjectIdentity
mplsFrrGeneralConformance = _MplsFrrGeneralConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 202, 2)
)
_MplsFrrGeneralCompliances_ObjectIdentity = ObjectIdentity
mplsFrrGeneralCompliances = _MplsFrrGeneralCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 202, 2, 1)
)
_MplsFrrGeneralGroups_ObjectIdentity = ObjectIdentity
mplsFrrGeneralGroups = _MplsFrrGeneralGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 202, 2, 2)
)

# Managed Objects groups

mplsFrrGeneralScalarGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 202, 2, 2, 1)
)
mplsFrrGeneralScalarGroup.setObjects(
      *(("MPLS-FRR-GENERAL-STD-MIB", "mplsFrrGeneralIngressTunnelInstances"),
        ("MPLS-FRR-GENERAL-STD-MIB", "mplsFrrGeneralProtectionMethod"))
)
if mibBuilder.loadTexts:
    mplsFrrGeneralScalarGroup.setStatus("current")

mplsFrrGeneralConstraintsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 202, 2, 2, 2)
)
mplsFrrGeneralConstraintsGroup.setObjects(
      *(("MPLS-FRR-GENERAL-STD-MIB", "mplsFrrGeneralConstraintsProtectionType"),
        ("MPLS-FRR-GENERAL-STD-MIB", "mplsFrrGeneralConstraintsSetupPrio"),
        ("MPLS-FRR-GENERAL-STD-MIB", "mplsFrrGeneralConstraintsHoldingPrio"),
        ("MPLS-FRR-GENERAL-STD-MIB", "mplsFrrGeneralConstraintsInclAnyAffinity"),
        ("MPLS-FRR-GENERAL-STD-MIB", "mplsFrrGeneralConstraintsInclAllAffinity"),
        ("MPLS-FRR-GENERAL-STD-MIB", "mplsFrrGeneralConstraintsExclAnyAffinity"),
        ("MPLS-FRR-GENERAL-STD-MIB", "mplsFrrGeneralConstraintsHopLimit"),
        ("MPLS-FRR-GENERAL-STD-MIB", "mplsFrrGeneralConstraintsBandwidth"),
        ("MPLS-FRR-GENERAL-STD-MIB", "mplsFrrGeneralConstraintsStorageType"),
        ("MPLS-FRR-GENERAL-STD-MIB", "mplsFrrGeneralConstraintsRowStatus"))
)
if mibBuilder.loadTexts:
    mplsFrrGeneralConstraintsGroup.setStatus("current")

mplsFrrGeneralTunnelARHopGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 202, 2, 2, 3)
)
mplsFrrGeneralTunnelARHopGroup.setObjects(
      *(("MPLS-FRR-GENERAL-STD-MIB", "mplsFrrGeneralTunnelARHopSessionAttributeFlags"),
        ("MPLS-FRR-GENERAL-STD-MIB", "mplsFrrGeneralTunnelARHopRROSubObjectFlags"))
)
if mibBuilder.loadTexts:
    mplsFrrGeneralTunnelARHopGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

mplsFrrGeneralModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 202, 2, 1, 1)
)
if mibBuilder.loadTexts:
    mplsFrrGeneralModuleFullCompliance.setStatus(
        "current"
    )

mplsFrrGeneralModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 202, 2, 1, 2)
)
if mibBuilder.loadTexts:
    mplsFrrGeneralModuleReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MPLS-FRR-GENERAL-STD-MIB",
    **{"mplsFrrGeneralMIB": mplsFrrGeneralMIB,
       "mplsFrrGeneralObjects": mplsFrrGeneralObjects,
       "mplsFrrGeneralProtectionMethod": mplsFrrGeneralProtectionMethod,
       "mplsFrrGeneralIngressTunnelInstances": mplsFrrGeneralIngressTunnelInstances,
       "mplsFrrGeneralConstraintsTable": mplsFrrGeneralConstraintsTable,
       "mplsFrrGeneralConstraintsEntry": mplsFrrGeneralConstraintsEntry,
       "mplsFrrGeneralConstraintsIfIndexOrZero": mplsFrrGeneralConstraintsIfIndexOrZero,
       "mplsFrrGeneralConstraintsTunnelIndex": mplsFrrGeneralConstraintsTunnelIndex,
       "mplsFrrGeneralConstraintsTunnelInstance": mplsFrrGeneralConstraintsTunnelInstance,
       "mplsFrrGeneralConstraintsProtectionType": mplsFrrGeneralConstraintsProtectionType,
       "mplsFrrGeneralConstraintsSetupPrio": mplsFrrGeneralConstraintsSetupPrio,
       "mplsFrrGeneralConstraintsHoldingPrio": mplsFrrGeneralConstraintsHoldingPrio,
       "mplsFrrGeneralConstraintsInclAnyAffinity": mplsFrrGeneralConstraintsInclAnyAffinity,
       "mplsFrrGeneralConstraintsInclAllAffinity": mplsFrrGeneralConstraintsInclAllAffinity,
       "mplsFrrGeneralConstraintsExclAnyAffinity": mplsFrrGeneralConstraintsExclAnyAffinity,
       "mplsFrrGeneralConstraintsHopLimit": mplsFrrGeneralConstraintsHopLimit,
       "mplsFrrGeneralConstraintsBandwidth": mplsFrrGeneralConstraintsBandwidth,
       "mplsFrrGeneralConstraintsStorageType": mplsFrrGeneralConstraintsStorageType,
       "mplsFrrGeneralConstraintsRowStatus": mplsFrrGeneralConstraintsRowStatus,
       "mplsFrrGeneralTunnelARHopTable": mplsFrrGeneralTunnelARHopTable,
       "mplsFrrGeneralTunnelARHopEntry": mplsFrrGeneralTunnelARHopEntry,
       "mplsFrrGeneralTunnelARHopSessionAttributeFlags": mplsFrrGeneralTunnelARHopSessionAttributeFlags,
       "mplsFrrGeneralTunnelARHopRROSubObjectFlags": mplsFrrGeneralTunnelARHopRROSubObjectFlags,
       "mplsFrrGeneralConformance": mplsFrrGeneralConformance,
       "mplsFrrGeneralCompliances": mplsFrrGeneralCompliances,
       "mplsFrrGeneralModuleFullCompliance": mplsFrrGeneralModuleFullCompliance,
       "mplsFrrGeneralModuleReadOnlyCompliance": mplsFrrGeneralModuleReadOnlyCompliance,
       "mplsFrrGeneralGroups": mplsFrrGeneralGroups,
       "mplsFrrGeneralScalarGroup": mplsFrrGeneralScalarGroup,
       "mplsFrrGeneralConstraintsGroup": mplsFrrGeneralConstraintsGroup,
       "mplsFrrGeneralTunnelARHopGroup": mplsFrrGeneralTunnelARHopGroup}
)
