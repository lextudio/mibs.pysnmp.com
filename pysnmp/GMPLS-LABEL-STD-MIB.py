# SNMP MIB module (GMPLS-LABEL-STD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GMPLS-LABEL-STD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:48:42 2024
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

(IndexIntegerNextFree,) = mibBuilder.importSymbols(
    "DIFFSERV-MIB",
    "IndexIntegerNextFree")

(GmplsFreeformLabelTC,
 GmplsLabelTypeTC) = mibBuilder.importSymbols(
    "GMPLS-TC-STD-MIB",
    "GmplsFreeformLabelTC",
    "GmplsLabelTypeTC")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(MplsLabel,
 mplsStdMIB) = mibBuilder.importSymbols(
    "MPLS-TC-STD-MIB",
    "MplsLabel",
    "mplsStdMIB")

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
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

gmplsLabelStdMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 16)
)
gmplsLabelStdMIB.setRevisions(
        ("2007-02-27 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_GmplsLabelObjects_ObjectIdentity = ObjectIdentity
gmplsLabelObjects = _GmplsLabelObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 16, 1)
)
_GmplsLabelIndexNext_Type = IndexIntegerNextFree
_GmplsLabelIndexNext_Object = MibScalar
gmplsLabelIndexNext = _GmplsLabelIndexNext_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 16, 1, 1),
    _GmplsLabelIndexNext_Type()
)
gmplsLabelIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmplsLabelIndexNext.setStatus("current")
_GmplsLabelTable_Object = MibTable
gmplsLabelTable = _GmplsLabelTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 16, 1, 2)
)
if mibBuilder.loadTexts:
    gmplsLabelTable.setStatus("current")
_GmplsLabelEntry_Object = MibTableRow
gmplsLabelEntry = _GmplsLabelEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 16, 1, 2, 1)
)
gmplsLabelEntry.setIndexNames(
    (0, "GMPLS-LABEL-STD-MIB", "gmplsLabelInterface"),
    (0, "GMPLS-LABEL-STD-MIB", "gmplsLabelIndex"),
    (0, "GMPLS-LABEL-STD-MIB", "gmplsLabelSubindex"),
)
if mibBuilder.loadTexts:
    gmplsLabelEntry.setStatus("current")
_GmplsLabelInterface_Type = InterfaceIndexOrZero
_GmplsLabelInterface_Object = MibTableColumn
gmplsLabelInterface = _GmplsLabelInterface_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 16, 1, 2, 1, 1),
    _GmplsLabelInterface_Type()
)
gmplsLabelInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gmplsLabelInterface.setStatus("current")


class _GmplsLabelIndex_Type(Unsigned32):
    """Custom type gmplsLabelIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_GmplsLabelIndex_Type.__name__ = "Unsigned32"
_GmplsLabelIndex_Object = MibTableColumn
gmplsLabelIndex = _GmplsLabelIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 16, 1, 2, 1, 2),
    _GmplsLabelIndex_Type()
)
gmplsLabelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gmplsLabelIndex.setStatus("current")


class _GmplsLabelSubindex_Type(Unsigned32):
    """Custom type gmplsLabelSubindex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_GmplsLabelSubindex_Type.__name__ = "Unsigned32"
_GmplsLabelSubindex_Object = MibTableColumn
gmplsLabelSubindex = _GmplsLabelSubindex_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 16, 1, 2, 1, 3),
    _GmplsLabelSubindex_Type()
)
gmplsLabelSubindex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gmplsLabelSubindex.setStatus("current")
_GmplsLabelType_Type = GmplsLabelTypeTC
_GmplsLabelType_Object = MibTableColumn
gmplsLabelType = _GmplsLabelType_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 16, 1, 2, 1, 4),
    _GmplsLabelType_Type()
)
gmplsLabelType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gmplsLabelType.setStatus("current")


class _GmplsLabelMplsLabel_Type(MplsLabel):
    """Custom type gmplsLabelMplsLabel based on MplsLabel"""
    defaultValue = 0


_GmplsLabelMplsLabel_Object = MibTableColumn
gmplsLabelMplsLabel = _GmplsLabelMplsLabel_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 16, 1, 2, 1, 5),
    _GmplsLabelMplsLabel_Type()
)
gmplsLabelMplsLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gmplsLabelMplsLabel.setStatus("current")


class _GmplsLabelPortWavelength_Type(Unsigned32):
    """Custom type gmplsLabelPortWavelength based on Unsigned32"""
    defaultValue = 0


_GmplsLabelPortWavelength_Object = MibTableColumn
gmplsLabelPortWavelength = _GmplsLabelPortWavelength_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 16, 1, 2, 1, 6),
    _GmplsLabelPortWavelength_Type()
)
gmplsLabelPortWavelength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gmplsLabelPortWavelength.setStatus("current")


class _GmplsLabelFreeform_Type(GmplsFreeformLabelTC):
    """Custom type gmplsLabelFreeform based on GmplsFreeformLabelTC"""
    defaultHexValue = "00"


_GmplsLabelFreeform_Object = MibTableColumn
gmplsLabelFreeform = _GmplsLabelFreeform_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 16, 1, 2, 1, 7),
    _GmplsLabelFreeform_Type()
)
gmplsLabelFreeform.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gmplsLabelFreeform.setStatus("current")


class _GmplsLabelSonetSdhSignalIndex_Type(Integer32):
    """Custom type gmplsLabelSonetSdhSignalIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_GmplsLabelSonetSdhSignalIndex_Type.__name__ = "Integer32"
_GmplsLabelSonetSdhSignalIndex_Object = MibTableColumn
gmplsLabelSonetSdhSignalIndex = _GmplsLabelSonetSdhSignalIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 16, 1, 2, 1, 8),
    _GmplsLabelSonetSdhSignalIndex_Type()
)
gmplsLabelSonetSdhSignalIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gmplsLabelSonetSdhSignalIndex.setStatus("current")


class _GmplsLabelSdhVc_Type(Integer32):
    """Custom type gmplsLabelSdhVc based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_GmplsLabelSdhVc_Type.__name__ = "Integer32"
_GmplsLabelSdhVc_Object = MibTableColumn
gmplsLabelSdhVc = _GmplsLabelSdhVc_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 16, 1, 2, 1, 9),
    _GmplsLabelSdhVc_Type()
)
gmplsLabelSdhVc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gmplsLabelSdhVc.setStatus("current")


class _GmplsLabelSdhVcBranch_Type(Integer32):
    """Custom type gmplsLabelSdhVcBranch based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_GmplsLabelSdhVcBranch_Type.__name__ = "Integer32"
_GmplsLabelSdhVcBranch_Object = MibTableColumn
gmplsLabelSdhVcBranch = _GmplsLabelSdhVcBranch_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 16, 1, 2, 1, 10),
    _GmplsLabelSdhVcBranch_Type()
)
gmplsLabelSdhVcBranch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gmplsLabelSdhVcBranch.setStatus("current")


class _GmplsLabelSonetSdhBranch_Type(Integer32):
    """Custom type gmplsLabelSonetSdhBranch based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_GmplsLabelSonetSdhBranch_Type.__name__ = "Integer32"
_GmplsLabelSonetSdhBranch_Object = MibTableColumn
gmplsLabelSonetSdhBranch = _GmplsLabelSonetSdhBranch_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 16, 1, 2, 1, 11),
    _GmplsLabelSonetSdhBranch_Type()
)
gmplsLabelSonetSdhBranch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gmplsLabelSonetSdhBranch.setStatus("current")


class _GmplsLabelSonetSdhGroupBranch_Type(Integer32):
    """Custom type gmplsLabelSonetSdhGroupBranch based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_GmplsLabelSonetSdhGroupBranch_Type.__name__ = "Integer32"
_GmplsLabelSonetSdhGroupBranch_Object = MibTableColumn
gmplsLabelSonetSdhGroupBranch = _GmplsLabelSonetSdhGroupBranch_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 16, 1, 2, 1, 12),
    _GmplsLabelSonetSdhGroupBranch_Type()
)
gmplsLabelSonetSdhGroupBranch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gmplsLabelSonetSdhGroupBranch.setStatus("current")


class _GmplsLabelWavebandId_Type(Unsigned32):
    """Custom type gmplsLabelWavebandId based on Unsigned32"""
    defaultValue = 0


_GmplsLabelWavebandId_Object = MibTableColumn
gmplsLabelWavebandId = _GmplsLabelWavebandId_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 16, 1, 2, 1, 13),
    _GmplsLabelWavebandId_Type()
)
gmplsLabelWavebandId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gmplsLabelWavebandId.setStatus("current")


class _GmplsLabelWavebandStart_Type(Unsigned32):
    """Custom type gmplsLabelWavebandStart based on Unsigned32"""
    defaultValue = 0


_GmplsLabelWavebandStart_Object = MibTableColumn
gmplsLabelWavebandStart = _GmplsLabelWavebandStart_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 16, 1, 2, 1, 14),
    _GmplsLabelWavebandStart_Type()
)
gmplsLabelWavebandStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gmplsLabelWavebandStart.setStatus("current")


class _GmplsLabelWavebandEnd_Type(Unsigned32):
    """Custom type gmplsLabelWavebandEnd based on Unsigned32"""
    defaultValue = 0


_GmplsLabelWavebandEnd_Object = MibTableColumn
gmplsLabelWavebandEnd = _GmplsLabelWavebandEnd_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 16, 1, 2, 1, 15),
    _GmplsLabelWavebandEnd_Type()
)
gmplsLabelWavebandEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gmplsLabelWavebandEnd.setStatus("current")


class _GmplsLabelStorageType_Type(StorageType):
    """Custom type gmplsLabelStorageType based on StorageType"""


_GmplsLabelStorageType_Object = MibTableColumn
gmplsLabelStorageType = _GmplsLabelStorageType_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 16, 1, 2, 1, 16),
    _GmplsLabelStorageType_Type()
)
gmplsLabelStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gmplsLabelStorageType.setStatus("current")
_GmplsLabelRowStatus_Type = RowStatus
_GmplsLabelRowStatus_Object = MibTableColumn
gmplsLabelRowStatus = _GmplsLabelRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 166, 16, 1, 2, 1, 17),
    _GmplsLabelRowStatus_Type()
)
gmplsLabelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    gmplsLabelRowStatus.setStatus("current")
_GmplsLabelConformance_ObjectIdentity = ObjectIdentity
gmplsLabelConformance = _GmplsLabelConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 16, 2)
)
_GmplsLabelGroups_ObjectIdentity = ObjectIdentity
gmplsLabelGroups = _GmplsLabelGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 16, 2, 1)
)
_GmplsLabelCompliances_ObjectIdentity = ObjectIdentity
gmplsLabelCompliances = _GmplsLabelCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 166, 16, 2, 2)
)

# Managed Objects groups

gmplsLabelTableGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 166, 16, 2, 1, 1)
)
gmplsLabelTableGroup.setObjects(
      *(("GMPLS-LABEL-STD-MIB", "gmplsLabelIndexNext"),
        ("GMPLS-LABEL-STD-MIB", "gmplsLabelType"),
        ("GMPLS-LABEL-STD-MIB", "gmplsLabelStorageType"),
        ("GMPLS-LABEL-STD-MIB", "gmplsLabelRowStatus"))
)
if mibBuilder.loadTexts:
    gmplsLabelTableGroup.setStatus("current")

gmplsLabelPacketGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 166, 16, 2, 1, 2)
)
gmplsLabelPacketGroup.setObjects(
    ("GMPLS-LABEL-STD-MIB", "gmplsLabelMplsLabel")
)
if mibBuilder.loadTexts:
    gmplsLabelPacketGroup.setStatus("current")

gmplsLabelPortWavelengthGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 166, 16, 2, 1, 3)
)
gmplsLabelPortWavelengthGroup.setObjects(
    ("GMPLS-LABEL-STD-MIB", "gmplsLabelPortWavelength")
)
if mibBuilder.loadTexts:
    gmplsLabelPortWavelengthGroup.setStatus("current")

gmplsLabelFreeformGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 166, 16, 2, 1, 4)
)
gmplsLabelFreeformGroup.setObjects(
    ("GMPLS-LABEL-STD-MIB", "gmplsLabelFreeform")
)
if mibBuilder.loadTexts:
    gmplsLabelFreeformGroup.setStatus("current")

gmplsLabelSonetSdhGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 166, 16, 2, 1, 5)
)
gmplsLabelSonetSdhGroup.setObjects(
      *(("GMPLS-LABEL-STD-MIB", "gmplsLabelSonetSdhSignalIndex"),
        ("GMPLS-LABEL-STD-MIB", "gmplsLabelSdhVc"),
        ("GMPLS-LABEL-STD-MIB", "gmplsLabelSdhVcBranch"),
        ("GMPLS-LABEL-STD-MIB", "gmplsLabelSonetSdhBranch"),
        ("GMPLS-LABEL-STD-MIB", "gmplsLabelSonetSdhGroupBranch"))
)
if mibBuilder.loadTexts:
    gmplsLabelSonetSdhGroup.setStatus("current")

gmplsLabelWavebandGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 166, 16, 2, 1, 6)
)
gmplsLabelWavebandGroup.setObjects(
      *(("GMPLS-LABEL-STD-MIB", "gmplsLabelWavebandId"),
        ("GMPLS-LABEL-STD-MIB", "gmplsLabelWavebandStart"),
        ("GMPLS-LABEL-STD-MIB", "gmplsLabelWavebandEnd"))
)
if mibBuilder.loadTexts:
    gmplsLabelWavebandGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

gmplsLabelModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 166, 16, 2, 2, 1)
)
if mibBuilder.loadTexts:
    gmplsLabelModuleReadOnlyCompliance.setStatus(
        "current"
    )

gmplsLabelModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 166, 16, 2, 2, 2)
)
if mibBuilder.loadTexts:
    gmplsLabelModuleFullCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GMPLS-LABEL-STD-MIB",
    **{"gmplsLabelStdMIB": gmplsLabelStdMIB,
       "gmplsLabelObjects": gmplsLabelObjects,
       "gmplsLabelIndexNext": gmplsLabelIndexNext,
       "gmplsLabelTable": gmplsLabelTable,
       "gmplsLabelEntry": gmplsLabelEntry,
       "gmplsLabelInterface": gmplsLabelInterface,
       "gmplsLabelIndex": gmplsLabelIndex,
       "gmplsLabelSubindex": gmplsLabelSubindex,
       "gmplsLabelType": gmplsLabelType,
       "gmplsLabelMplsLabel": gmplsLabelMplsLabel,
       "gmplsLabelPortWavelength": gmplsLabelPortWavelength,
       "gmplsLabelFreeform": gmplsLabelFreeform,
       "gmplsLabelSonetSdhSignalIndex": gmplsLabelSonetSdhSignalIndex,
       "gmplsLabelSdhVc": gmplsLabelSdhVc,
       "gmplsLabelSdhVcBranch": gmplsLabelSdhVcBranch,
       "gmplsLabelSonetSdhBranch": gmplsLabelSonetSdhBranch,
       "gmplsLabelSonetSdhGroupBranch": gmplsLabelSonetSdhGroupBranch,
       "gmplsLabelWavebandId": gmplsLabelWavebandId,
       "gmplsLabelWavebandStart": gmplsLabelWavebandStart,
       "gmplsLabelWavebandEnd": gmplsLabelWavebandEnd,
       "gmplsLabelStorageType": gmplsLabelStorageType,
       "gmplsLabelRowStatus": gmplsLabelRowStatus,
       "gmplsLabelConformance": gmplsLabelConformance,
       "gmplsLabelGroups": gmplsLabelGroups,
       "gmplsLabelTableGroup": gmplsLabelTableGroup,
       "gmplsLabelPacketGroup": gmplsLabelPacketGroup,
       "gmplsLabelPortWavelengthGroup": gmplsLabelPortWavelengthGroup,
       "gmplsLabelFreeformGroup": gmplsLabelFreeformGroup,
       "gmplsLabelSonetSdhGroup": gmplsLabelSonetSdhGroup,
       "gmplsLabelWavebandGroup": gmplsLabelWavebandGroup,
       "gmplsLabelCompliances": gmplsLabelCompliances,
       "gmplsLabelModuleReadOnlyCompliance": gmplsLabelModuleReadOnlyCompliance,
       "gmplsLabelModuleFullCompliance": gmplsLabelModuleFullCompliance}
)
