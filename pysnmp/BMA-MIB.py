# SNMP MIB module (BMA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BMA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:48:27 2024
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

(IbDataPort,
 infinibandMIB) = mibBuilder.importSymbols(
    "IB-TC-MIB",
    "IbDataPort",
    "infinibandMIB")

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

(DateAndTime,
 DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ibBmaMIB = ModuleIdentity(
    (1, 3, 6, 1, 3, 117, 5)
)
ibBmaMIB.setRevisions(
        ("2005-09-01 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IbBmaObjects_ObjectIdentity = ObjectIdentity
ibBmaObjects = _IbBmaObjects_ObjectIdentity(
    (1, 3, 6, 1, 3, 117, 5, 1)
)
_IbBmaBmuInfo_ObjectIdentity = ObjectIdentity
ibBmaBmuInfo = _IbBmaBmuInfo_ObjectIdentity(
    (1, 3, 6, 1, 3, 117, 5, 1, 1)
)


class _IbBmaBaseboardManagedUnitType_Type(Integer32):
    """Custom type ibBmaBaseboardManagedUnitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ibModule", 1),
          ("managedChassis", 3),
          ("nonModule", 2))
    )


_IbBmaBaseboardManagedUnitType_Type.__name__ = "Integer32"
_IbBmaBaseboardManagedUnitType_Object = MibScalar
ibBmaBaseboardManagedUnitType = _IbBmaBaseboardManagedUnitType_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 1, 1),
    _IbBmaBaseboardManagedUnitType_Type()
)
ibBmaBaseboardManagedUnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaBaseboardManagedUnitType.setStatus("current")
_IbBmaIsIBMLSupported_Type = TruthValue
_IbBmaIsIBMLSupported_Object = MibScalar
ibBmaIsIBMLSupported = _IbBmaIsIBMLSupported_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 1, 2),
    _IbBmaIsIBMLSupported_Type()
)
ibBmaIsIBMLSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaIsIBMLSupported.setStatus("current")


class _IbBmaIBMLImplementation_Type(Integer32):
    """Custom type ibBmaIBMLImplementation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ibMlPhysical", 1),
          ("ibMlVirtual", 2),
          ("unknown", 3))
    )


_IbBmaIBMLImplementation_Type.__name__ = "Integer32"
_IbBmaIBMLImplementation_Object = MibScalar
ibBmaIBMLImplementation = _IbBmaIBMLImplementation_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 1, 3),
    _IbBmaIBMLImplementation_Type()
)
ibBmaIBMLImplementation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaIBMLImplementation.setStatus("current")
_IbBmaBKeyInfo_ObjectIdentity = ObjectIdentity
ibBmaBKeyInfo = _IbBmaBKeyInfo_ObjectIdentity(
    (1, 3, 6, 1, 3, 117, 5, 1, 2)
)
_IbBmaIsBKeyNVRAM_Type = TruthValue
_IbBmaIsBKeyNVRAM_Object = MibScalar
ibBmaIsBKeyNVRAM = _IbBmaIsBKeyNVRAM_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 2, 1),
    _IbBmaIsBKeyNVRAM_Type()
)
ibBmaIsBKeyNVRAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaIsBKeyNVRAM.setStatus("current")


class _IbBmaBKeyValue_Type(OctetString):
    """Custom type ibBmaBKeyValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_IbBmaBKeyValue_Type.__name__ = "OctetString"
_IbBmaBKeyValue_Object = MibScalar
ibBmaBKeyValue = _IbBmaBKeyValue_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 2, 2),
    _IbBmaBKeyValue_Type()
)
ibBmaBKeyValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaBKeyValue.setStatus("current")
_IbBmaBKeyProtectBit_Type = TruthValue
_IbBmaBKeyProtectBit_Object = MibScalar
ibBmaBKeyProtectBit = _IbBmaBKeyProtectBit_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 2, 3),
    _IbBmaBKeyProtectBit_Type()
)
ibBmaBKeyProtectBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaBKeyProtectBit.setStatus("current")


class _IbBmaBKeyLeasePeriod_Type(Integer32):
    """Custom type ibBmaBKeyLeasePeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbBmaBKeyLeasePeriod_Type.__name__ = "Integer32"
_IbBmaBKeyLeasePeriod_Object = MibScalar
ibBmaBKeyLeasePeriod = _IbBmaBKeyLeasePeriod_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 2, 4),
    _IbBmaBKeyLeasePeriod_Type()
)
ibBmaBKeyLeasePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaBKeyLeasePeriod.setStatus("current")
if mibBuilder.loadTexts:
    ibBmaBKeyLeasePeriod.setUnits("seconds")


class _IbBmaBKeyViolations_Type(Integer32):
    """Custom type ibBmaBKeyViolations based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbBmaBKeyViolations_Type.__name__ = "Integer32"
_IbBmaBKeyViolations_Object = MibScalar
ibBmaBKeyViolations = _IbBmaBKeyViolations_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 2, 5),
    _IbBmaBKeyViolations_Type()
)
ibBmaBKeyViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaBKeyViolations.setStatus("current")
_IbBmaVpd_ObjectIdentity = ObjectIdentity
ibBmaVpd = _IbBmaVpd_ObjectIdentity(
    (1, 3, 6, 1, 3, 117, 5, 1, 3)
)
_IbBmaModuleInfo_ObjectIdentity = ObjectIdentity
ibBmaModuleInfo = _IbBmaModuleInfo_ObjectIdentity(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 1)
)
_IbBmaModuleInfoTable_Object = MibTable
ibBmaModuleInfoTable = _IbBmaModuleInfoTable_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ibBmaModuleInfoTable.setStatus("current")
_IbBmaModuleInfoEntry_Object = MibTableRow
ibBmaModuleInfoEntry = _IbBmaModuleInfoEntry_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 1, 1, 1)
)
ibBmaModuleInfoEntry.setIndexNames(
    (0, "BMA-MIB", "ibBmaModuleInfoIndex"),
)
if mibBuilder.loadTexts:
    ibBmaModuleInfoEntry.setStatus("current")


class _IbBmaModuleInfoIndex_Type(Integer32):
    """Custom type ibBmaModuleInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IbBmaModuleInfoIndex_Type.__name__ = "Integer32"
_IbBmaModuleInfoIndex_Object = MibTableColumn
ibBmaModuleInfoIndex = _IbBmaModuleInfoIndex_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 1, 1, 1, 1),
    _IbBmaModuleInfoIndex_Type()
)
ibBmaModuleInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibBmaModuleInfoIndex.setStatus("current")


class _IbBmaModInfoModGuid_Type(OctetString):
    """Custom type ibBmaModInfoModGuid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_IbBmaModInfoModGuid_Type.__name__ = "OctetString"
_IbBmaModInfoModGuid_Object = MibTableColumn
ibBmaModInfoModGuid = _IbBmaModInfoModGuid_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 1, 1, 1, 2),
    _IbBmaModInfoModGuid_Type()
)
ibBmaModInfoModGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaModInfoModGuid.setStatus("current")


class _IbBmaModInfoModType_Type(Integer32):
    """Custom type ibBmaModInfoModType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("infiniBandModule", 2),
          ("notInfiniBandModule", 1),
          ("other", 3))
    )


_IbBmaModInfoModType_Type.__name__ = "Integer32"
_IbBmaModInfoModType_Object = MibTableColumn
ibBmaModInfoModType = _IbBmaModInfoModType_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 1, 1, 1, 3),
    _IbBmaModInfoModType_Type()
)
ibBmaModInfoModType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaModInfoModType.setStatus("current")


class _IbBmaModInfoModClass_Type(Integer32):
    """Custom type ibBmaModInfoModClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("fourXrepeater", 6),
          ("hca", 2),
          ("oneXrepeater", 5),
          ("other", 8),
          ("router", 4),
          ("switch", 3),
          ("tca", 1),
          ("twelveXrepeater", 7))
    )


_IbBmaModInfoModClass_Type.__name__ = "Integer32"
_IbBmaModInfoModClass_Object = MibTableColumn
ibBmaModInfoModClass = _IbBmaModInfoModClass_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 1, 1, 1, 4),
    _IbBmaModInfoModClass_Type()
)
ibBmaModInfoModClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaModInfoModClass.setStatus("current")


class _IbBmaModInfoNodeCount_Type(Integer32):
    """Custom type ibBmaModInfoNodeCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbBmaModInfoNodeCount_Type.__name__ = "Integer32"
_IbBmaModInfoNodeCount_Object = MibTableColumn
ibBmaModInfoNodeCount = _IbBmaModInfoNodeCount_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 1, 1, 1, 5),
    _IbBmaModInfoNodeCount_Type()
)
ibBmaModInfoNodeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaModInfoNodeCount.setStatus("current")


class _IbBmaModInfoLinkCount_Type(Integer32):
    """Custom type ibBmaModInfoLinkCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbBmaModInfoLinkCount_Type.__name__ = "Integer32"
_IbBmaModInfoLinkCount_Object = MibTableColumn
ibBmaModInfoLinkCount = _IbBmaModInfoLinkCount_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 1, 1, 1, 6),
    _IbBmaModInfoLinkCount_Type()
)
ibBmaModInfoLinkCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaModInfoLinkCount.setStatus("current")


class _IbBmaModInfoBckplaneLinkCnt_Type(Integer32):
    """Custom type ibBmaModInfoBckplaneLinkCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbBmaModInfoBckplaneLinkCnt_Type.__name__ = "Integer32"
_IbBmaModInfoBckplaneLinkCnt_Object = MibTableColumn
ibBmaModInfoBckplaneLinkCnt = _IbBmaModInfoBckplaneLinkCnt_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 1, 1, 1, 7),
    _IbBmaModInfoBckplaneLinkCnt_Type()
)
ibBmaModInfoBckplaneLinkCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaModInfoBckplaneLinkCnt.setStatus("current")


class _IbBmaModInfoIbmlCount_Type(Integer32):
    """Custom type ibBmaModInfoIbmlCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbBmaModInfoIbmlCount_Type.__name__ = "Integer32"
_IbBmaModInfoIbmlCount_Object = MibTableColumn
ibBmaModInfoIbmlCount = _IbBmaModInfoIbmlCount_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 1, 1, 1, 8),
    _IbBmaModInfoIbmlCount_Type()
)
ibBmaModInfoIbmlCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaModInfoIbmlCount.setStatus("current")


class _IbBmaModInfoBckPlaneIbmlCnt_Type(Integer32):
    """Custom type ibBmaModInfoBckPlaneIbmlCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbBmaModInfoBckPlaneIbmlCnt_Type.__name__ = "Integer32"
_IbBmaModInfoBckPlaneIbmlCnt_Object = MibTableColumn
ibBmaModInfoBckPlaneIbmlCnt = _IbBmaModInfoBckPlaneIbmlCnt_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 1, 1, 1, 9),
    _IbBmaModInfoBckPlaneIbmlCnt_Type()
)
ibBmaModInfoBckPlaneIbmlCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaModInfoBckPlaneIbmlCnt.setStatus("current")


class _IbBmaModInfoModuleSize_Type(OctetString):
    """Custom type ibBmaModInfoModuleSize based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_IbBmaModInfoModuleSize_Type.__name__ = "OctetString"
_IbBmaModInfoModuleSize_Object = MibTableColumn
ibBmaModInfoModuleSize = _IbBmaModInfoModuleSize_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 1, 1, 1, 10),
    _IbBmaModInfoModuleSize_Type()
)
ibBmaModInfoModuleSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaModInfoModuleSize.setStatus("current")


class _IbBmaModInfoFormFactor_Type(Integer32):
    """Custom type ibBmaModInfoFormFactor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("cardEdgeBoard", 12),
          ("compactPci", 9),
          ("deviceBay", 13),
          ("internalMezzanineBoard", 11),
          ("lowProfilePci", 8),
          ("nonRemovable", 2),
          ("otherRemovable", 14),
          ("pci", 7),
          ("standard", 3),
          ("standardWide", 4),
          ("tall", 5),
          ("tallWide", 6),
          ("unspecified", 1),
          ("vme", 10))
    )


_IbBmaModInfoFormFactor_Type.__name__ = "Integer32"
_IbBmaModInfoFormFactor_Object = MibTableColumn
ibBmaModInfoFormFactor = _IbBmaModInfoFormFactor_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 1, 1, 1, 11),
    _IbBmaModInfoFormFactor_Type()
)
ibBmaModInfoFormFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaModInfoFormFactor.setStatus("current")
_IbBmaChassisInfo_ObjectIdentity = ObjectIdentity
ibBmaChassisInfo = _IbBmaChassisInfo_ObjectIdentity(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 2)
)


class _IbBmaChasInfoChassisGuid_Type(OctetString):
    """Custom type ibBmaChasInfoChassisGuid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_IbBmaChasInfoChassisGuid_Type.__name__ = "OctetString"
_IbBmaChasInfoChassisGuid_Object = MibScalar
ibBmaChasInfoChassisGuid = _IbBmaChasInfoChassisGuid_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 2, 1),
    _IbBmaChasInfoChassisGuid_Type()
)
ibBmaChasInfoChassisGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaChasInfoChassisGuid.setStatus("current")


class _IbBmaChasInfoSlotCount_Type(Integer32):
    """Custom type ibBmaChasInfoSlotCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_IbBmaChasInfoSlotCount_Type.__name__ = "Integer32"
_IbBmaChasInfoSlotCount_Object = MibScalar
ibBmaChasInfoSlotCount = _IbBmaChasInfoSlotCount_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 2, 2),
    _IbBmaChasInfoSlotCount_Type()
)
ibBmaChasInfoSlotCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaChasInfoSlotCount.setStatus("current")
_IbBmaChasInfoSlotTable_Object = MibTable
ibBmaChasInfoSlotTable = _IbBmaChasInfoSlotTable_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 2, 3)
)
if mibBuilder.loadTexts:
    ibBmaChasInfoSlotTable.setStatus("current")
_IbBmaChasInfoSlotEntry_Object = MibTableRow
ibBmaChasInfoSlotEntry = _IbBmaChasInfoSlotEntry_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 2, 3, 1)
)
ibBmaChasInfoSlotEntry.setIndexNames(
    (0, "BMA-MIB", "ibBmaChasInfoSlotIndex"),
)
if mibBuilder.loadTexts:
    ibBmaChasInfoSlotEntry.setStatus("current")


class _IbBmaChasInfoSlotIndex_Type(Integer32):
    """Custom type ibBmaChasInfoSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_IbBmaChasInfoSlotIndex_Type.__name__ = "Integer32"
_IbBmaChasInfoSlotIndex_Object = MibTableColumn
ibBmaChasInfoSlotIndex = _IbBmaChasInfoSlotIndex_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 2, 3, 1, 1),
    _IbBmaChasInfoSlotIndex_Type()
)
ibBmaChasInfoSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibBmaChasInfoSlotIndex.setStatus("current")


class _IbBmaChasInfoAssignedSlotNum_Type(Integer32):
    """Custom type ibBmaChasInfoAssignedSlotNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IbBmaChasInfoAssignedSlotNum_Type.__name__ = "Integer32"
_IbBmaChasInfoAssignedSlotNum_Object = MibTableColumn
ibBmaChasInfoAssignedSlotNum = _IbBmaChasInfoAssignedSlotNum_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 2, 3, 1, 2),
    _IbBmaChasInfoAssignedSlotNum_Type()
)
ibBmaChasInfoAssignedSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaChasInfoAssignedSlotNum.setStatus("current")


class _IbBmaChasInfoSlotConnStatus_Type(Integer32):
    """Custom type ibBmaChasInfoSlotConnStatus based on Integer32"""
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
        *(("notImplemented", 1),
          ("oneConnectToStandardSlot", 2),
          ("oneConnectToTallSlot", 3),
          ("twoConnectToTallSlot", 4))
    )


_IbBmaChasInfoSlotConnStatus_Type.__name__ = "Integer32"
_IbBmaChasInfoSlotConnStatus_Object = MibTableColumn
ibBmaChasInfoSlotConnStatus = _IbBmaChasInfoSlotConnStatus_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 2, 3, 1, 3),
    _IbBmaChasInfoSlotConnStatus_Type()
)
ibBmaChasInfoSlotConnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaChasInfoSlotConnStatus.setStatus("current")


class _IbBmaChasInfoCmeAccess_Type(Integer32):
    """Custom type ibBmaChasInfoCmeAccess based on Integer32"""
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
        *(("accessViaPriPort", 2),
          ("notAccessible", 3),
          ("reserved", 4),
          ("unspecified", 1))
    )


_IbBmaChasInfoCmeAccess_Type.__name__ = "Integer32"
_IbBmaChasInfoCmeAccess_Object = MibTableColumn
ibBmaChasInfoCmeAccess = _IbBmaChasInfoCmeAccess_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 2, 3, 1, 4),
    _IbBmaChasInfoCmeAccess_Type()
)
ibBmaChasInfoCmeAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaChasInfoCmeAccess.setStatus("current")


class _IbBmaChasInfoProxyAccess_Type(Integer32):
    """Custom type ibBmaChasInfoProxyAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hasProxyAccess", 2),
          ("noProxyAccess", 1))
    )


_IbBmaChasInfoProxyAccess_Type.__name__ = "Integer32"
_IbBmaChasInfoProxyAccess_Object = MibTableColumn
ibBmaChasInfoProxyAccess = _IbBmaChasInfoProxyAccess_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 2, 3, 1, 5),
    _IbBmaChasInfoProxyAccess_Type()
)
ibBmaChasInfoProxyAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaChasInfoProxyAccess.setStatus("current")


class _IbBmaChasInfoLockDrivesCtr_Type(Integer32):
    """Custom type ibBmaChasInfoLockDrivesCtr based on Integer32"""
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
        *(("lockDrivesCmeCtr", 2),
          ("lockReleaseForCmeCtr", 3),
          ("reserved", 4),
          ("unspecified", 1))
    )


_IbBmaChasInfoLockDrivesCtr_Type.__name__ = "Integer32"
_IbBmaChasInfoLockDrivesCtr_Object = MibTableColumn
ibBmaChasInfoLockDrivesCtr = _IbBmaChasInfoLockDrivesCtr_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 2, 3, 1, 6),
    _IbBmaChasInfoLockDrivesCtr_Type()
)
ibBmaChasInfoLockDrivesCtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaChasInfoLockDrivesCtr.setStatus("current")


class _IbBmaChasInfoMechLockPresent_Type(Integer32):
    """Custom type ibBmaChasInfoMechLockPresent based on Integer32"""
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
        *(("hasLock", 2),
          ("noLock", 3),
          ("reserved", 4),
          ("unspecified", 1))
    )


_IbBmaChasInfoMechLockPresent_Type.__name__ = "Integer32"
_IbBmaChasInfoMechLockPresent_Object = MibTableColumn
ibBmaChasInfoMechLockPresent = _IbBmaChasInfoMechLockPresent_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 2, 3, 1, 7),
    _IbBmaChasInfoMechLockPresent_Type()
)
ibBmaChasInfoMechLockPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaChasInfoMechLockPresent.setStatus("current")
_IbBmaFruInfo_ObjectIdentity = ObjectIdentity
ibBmaFruInfo = _IbBmaFruInfo_ObjectIdentity(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 3)
)
_IbBmaFruInfoTable_Object = MibTable
ibBmaFruInfoTable = _IbBmaFruInfoTable_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    ibBmaFruInfoTable.setStatus("current")
_IbBmaFruInfoEntry_Object = MibTableRow
ibBmaFruInfoEntry = _IbBmaFruInfoEntry_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 3, 1, 1)
)
ibBmaFruInfoEntry.setIndexNames(
    (0, "BMA-MIB", "ibBmaFruInfoIndex"),
)
if mibBuilder.loadTexts:
    ibBmaFruInfoEntry.setStatus("current")


class _IbBmaFruInfoIndex_Type(Integer32):
    """Custom type ibBmaFruInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_IbBmaFruInfoIndex_Type.__name__ = "Integer32"
_IbBmaFruInfoIndex_Object = MibTableColumn
ibBmaFruInfoIndex = _IbBmaFruInfoIndex_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 3, 1, 1, 1),
    _IbBmaFruInfoIndex_Type()
)
ibBmaFruInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibBmaFruInfoIndex.setStatus("current")


class _IbBmaFruInfoType_Type(Integer32):
    """Custom type ibBmaFruInfoType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("boardOrCard", 8),
          ("coolingModule", 11),
          ("infinibandModBackplane", 3),
          ("infinibandModule", 2),
          ("infinibandSwitchMod", 4),
          ("mainChassis", 5),
          ("memoryCard", 15),
          ("memoryModule", 14),
          ("oem", 16),
          ("otherModAssembly", 10),
          ("platformSystem", 6),
          ("powerConverterSuppyMod", 9),
          ("processorModule", 13),
          ("standaloneProduct", 7),
          ("subChassis", 12),
          ("unspecified", 1))
    )


_IbBmaFruInfoType_Type.__name__ = "Integer32"
_IbBmaFruInfoType_Object = MibTableColumn
ibBmaFruInfoType = _IbBmaFruInfoType_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 3, 1, 1, 2),
    _IbBmaFruInfoType_Type()
)
ibBmaFruInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaFruInfoType.setStatus("current")


class _IbBmaFruInfoGuidType_Type(Integer32):
    """Custom type ibBmaFruInfoGuidType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("guid16", 4),
          ("guid48", 3),
          ("guid64", 2),
          ("guid8", 5),
          ("none", 1))
    )


_IbBmaFruInfoGuidType_Type.__name__ = "Integer32"
_IbBmaFruInfoGuidType_Object = MibTableColumn
ibBmaFruInfoGuidType = _IbBmaFruInfoGuidType_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 3, 1, 1, 3),
    _IbBmaFruInfoGuidType_Type()
)
ibBmaFruInfoGuidType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaFruInfoGuidType.setStatus("current")


class _IbBmaFruInfoGuidValue_Type(OctetString):
    """Custom type ibBmaFruInfoGuidValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_IbBmaFruInfoGuidValue_Type.__name__ = "OctetString"
_IbBmaFruInfoGuidValue_Object = MibTableColumn
ibBmaFruInfoGuidValue = _IbBmaFruInfoGuidValue_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 3, 1, 1, 4),
    _IbBmaFruInfoGuidValue_Type()
)
ibBmaFruInfoGuidValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaFruInfoGuidValue.setStatus("current")


class _IbBmaFruInfoSerialNumber_Type(OctetString):
    """Custom type ibBmaFruInfoSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_IbBmaFruInfoSerialNumber_Type.__name__ = "OctetString"
_IbBmaFruInfoSerialNumber_Object = MibTableColumn
ibBmaFruInfoSerialNumber = _IbBmaFruInfoSerialNumber_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 3, 1, 1, 5),
    _IbBmaFruInfoSerialNumber_Type()
)
ibBmaFruInfoSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaFruInfoSerialNumber.setStatus("current")


class _IbBmaFruInfoPartNumber_Type(OctetString):
    """Custom type ibBmaFruInfoPartNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_IbBmaFruInfoPartNumber_Type.__name__ = "OctetString"
_IbBmaFruInfoPartNumber_Object = MibTableColumn
ibBmaFruInfoPartNumber = _IbBmaFruInfoPartNumber_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 3, 1, 1, 6),
    _IbBmaFruInfoPartNumber_Type()
)
ibBmaFruInfoPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaFruInfoPartNumber.setStatus("current")


class _IbBmaFruInfoModelName_Type(OctetString):
    """Custom type ibBmaFruInfoModelName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_IbBmaFruInfoModelName_Type.__name__ = "OctetString"
_IbBmaFruInfoModelName_Object = MibTableColumn
ibBmaFruInfoModelName = _IbBmaFruInfoModelName_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 3, 1, 1, 7),
    _IbBmaFruInfoModelName_Type()
)
ibBmaFruInfoModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaFruInfoModelName.setStatus("current")


class _IbBmaFruInfoVersion_Type(OctetString):
    """Custom type ibBmaFruInfoVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_IbBmaFruInfoVersion_Type.__name__ = "OctetString"
_IbBmaFruInfoVersion_Object = MibTableColumn
ibBmaFruInfoVersion = _IbBmaFruInfoVersion_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 3, 1, 1, 8),
    _IbBmaFruInfoVersion_Type()
)
ibBmaFruInfoVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaFruInfoVersion.setStatus("current")


class _IbBmaFruInfoManufacturerName_Type(OctetString):
    """Custom type ibBmaFruInfoManufacturerName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_IbBmaFruInfoManufacturerName_Type.__name__ = "OctetString"
_IbBmaFruInfoManufacturerName_Object = MibTableColumn
ibBmaFruInfoManufacturerName = _IbBmaFruInfoManufacturerName_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 3, 1, 1, 9),
    _IbBmaFruInfoManufacturerName_Type()
)
ibBmaFruInfoManufacturerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaFruInfoManufacturerName.setStatus("current")


class _IbBmaFruInfoProductName_Type(OctetString):
    """Custom type ibBmaFruInfoProductName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_IbBmaFruInfoProductName_Type.__name__ = "OctetString"
_IbBmaFruInfoProductName_Object = MibTableColumn
ibBmaFruInfoProductName = _IbBmaFruInfoProductName_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 3, 1, 1, 10),
    _IbBmaFruInfoProductName_Type()
)
ibBmaFruInfoProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaFruInfoProductName.setStatus("current")


class _IbBmaFruInfoManufacturerID_Type(OctetString):
    """Custom type ibBmaFruInfoManufacturerID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_IbBmaFruInfoManufacturerID_Type.__name__ = "OctetString"
_IbBmaFruInfoManufacturerID_Object = MibTableColumn
ibBmaFruInfoManufacturerID = _IbBmaFruInfoManufacturerID_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 3, 1, 1, 11),
    _IbBmaFruInfoManufacturerID_Type()
)
ibBmaFruInfoManufacturerID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaFruInfoManufacturerID.setStatus("current")
_IbBmaFruInfoManDateAndTime_Type = DateAndTime
_IbBmaFruInfoManDateAndTime_Object = MibTableColumn
ibBmaFruInfoManDateAndTime = _IbBmaFruInfoManDateAndTime_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 3, 1, 1, 12),
    _IbBmaFruInfoManDateAndTime_Type()
)
ibBmaFruInfoManDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaFruInfoManDateAndTime.setStatus("current")
_IbBmaPortConnectInfo_ObjectIdentity = ObjectIdentity
ibBmaPortConnectInfo = _IbBmaPortConnectInfo_ObjectIdentity(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 4)
)


class _IbBmaPortConNumConnection_Type(Integer32):
    """Custom type ibBmaPortConNumConnection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_IbBmaPortConNumConnection_Type.__name__ = "Integer32"
_IbBmaPortConNumConnection_Object = MibScalar
ibBmaPortConNumConnection = _IbBmaPortConNumConnection_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 4, 1),
    _IbBmaPortConNumConnection_Type()
)
ibBmaPortConNumConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaPortConNumConnection.setStatus("current")
_IbBmaPortConnectTable_Object = MibTable
ibBmaPortConnectTable = _IbBmaPortConnectTable_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 4, 2)
)
if mibBuilder.loadTexts:
    ibBmaPortConnectTable.setStatus("current")
_IbBmaPortConnectEntry_Object = MibTableRow
ibBmaPortConnectEntry = _IbBmaPortConnectEntry_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 4, 2, 1)
)
ibBmaPortConnectEntry.setIndexNames(
    (0, "BMA-MIB", "ibBmaPortConnectIndex"),
)
if mibBuilder.loadTexts:
    ibBmaPortConnectEntry.setStatus("current")


class _IbBmaPortConnectIndex_Type(Integer32):
    """Custom type ibBmaPortConnectIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_IbBmaPortConnectIndex_Type.__name__ = "Integer32"
_IbBmaPortConnectIndex_Object = MibTableColumn
ibBmaPortConnectIndex = _IbBmaPortConnectIndex_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 4, 2, 1, 1),
    _IbBmaPortConnectIndex_Type()
)
ibBmaPortConnectIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibBmaPortConnectIndex.setStatus("current")


class _IbBmaPortConInternalCon_Type(Integer32):
    """Custom type ibBmaPortConInternalCon based on Integer32"""
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
        *(("noInternelConnection", 4),
          ("terminateAfterGoing", 3),
          ("terminateWithoutGoing", 2),
          ("unspecified", 1))
    )


_IbBmaPortConInternalCon_Type.__name__ = "Integer32"
_IbBmaPortConInternalCon_Object = MibTableColumn
ibBmaPortConInternalCon = _IbBmaPortConInternalCon_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 4, 2, 1, 2),
    _IbBmaPortConInternalCon_Type()
)
ibBmaPortConInternalCon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaPortConInternalCon.setStatus("current")


class _IbBmaPortConMediaClass_Type(Integer32):
    """Custom type ibBmaPortConMediaClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("copper", 2),
          ("fiber", 3),
          ("pcb", 4),
          ("repeaterThenCopper", 5),
          ("repeaterThenFiber", 6),
          ("repeaterThenNode", 7),
          ("reserved", 8),
          ("unspecified", 1))
    )


_IbBmaPortConMediaClass_Type.__name__ = "Integer32"
_IbBmaPortConMediaClass_Object = MibTableColumn
ibBmaPortConMediaClass = _IbBmaPortConMediaClass_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 4, 2, 1, 3),
    _IbBmaPortConMediaClass_Type()
)
ibBmaPortConMediaClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaPortConMediaClass.setStatus("current")


class _IbBmaPortConConClass_Type(Integer32):
    """Custom type ibBmaPortConConClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("backplaneSide", 3),
          ("moduleSide", 4),
          ("noInfo", 6),
          ("nonRemovable", 5),
          ("nonSpecifyRemovable", 2),
          ("reserved", 7),
          ("unspecified", 1))
    )


_IbBmaPortConConClass_Type.__name__ = "Integer32"
_IbBmaPortConConClass_Object = MibTableColumn
ibBmaPortConConClass = _IbBmaPortConConClass_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 4, 2, 1, 4),
    _IbBmaPortConConClass_Type()
)
ibBmaPortConConClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaPortConConClass.setStatus("current")
_IbBmaModPowerInfo_ObjectIdentity = ObjectIdentity
ibBmaModPowerInfo = _IbBmaModPowerInfo_ObjectIdentity(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 5)
)


class _IbBmaOperThermalPower_Type(Integer32):
    """Custom type ibBmaOperThermalPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 131071),
    )


_IbBmaOperThermalPower_Type.__name__ = "Integer32"
_IbBmaOperThermalPower_Object = MibScalar
ibBmaOperThermalPower = _IbBmaOperThermalPower_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 5, 1),
    _IbBmaOperThermalPower_Type()
)
ibBmaOperThermalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaOperThermalPower.setStatus("current")


class _IbBmaOperCurrent_Type(Integer32):
    """Custom type ibBmaOperCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_IbBmaOperCurrent_Type.__name__ = "Integer32"
_IbBmaOperCurrent_Object = MibScalar
ibBmaOperCurrent = _IbBmaOperCurrent_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 5, 2),
    _IbBmaOperCurrent_Type()
)
ibBmaOperCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaOperCurrent.setStatus("current")


class _IbBmaIdleCurrent_Type(Integer32):
    """Custom type ibBmaIdleCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_IbBmaIdleCurrent_Type.__name__ = "Integer32"
_IbBmaIdleCurrent_Object = MibScalar
ibBmaIdleCurrent = _IbBmaIdleCurrent_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 5, 3),
    _IbBmaIdleCurrent_Type()
)
ibBmaIdleCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaIdleCurrent.setStatus("current")


class _IbBmaInitCurrent_Type(Integer32):
    """Custom type ibBmaInitCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_IbBmaInitCurrent_Type.__name__ = "Integer32"
_IbBmaInitCurrent_Object = MibScalar
ibBmaInitCurrent = _IbBmaInitCurrent_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 5, 4),
    _IbBmaInitCurrent_Type()
)
ibBmaInitCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaInitCurrent.setStatus("current")


class _IbBmaInitTime_Type(Integer32):
    """Custom type ibBmaInitTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbBmaInitTime_Type.__name__ = "Integer32"
_IbBmaInitTime_Object = MibScalar
ibBmaInitTime = _IbBmaInitTime_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 5, 5),
    _IbBmaInitTime_Type()
)
ibBmaInitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaInitTime.setStatus("current")
_IbBmaIsMStandbySupported_Type = TruthValue
_IbBmaIsMStandbySupported_Object = MibScalar
ibBmaIsMStandbySupported = _IbBmaIsMStandbySupported_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 5, 6),
    _IbBmaIsMStandbySupported_Type()
)
ibBmaIsMStandbySupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaIsMStandbySupported.setStatus("current")
_IbBmaIsPowerMgmtSupported_Type = TruthValue
_IbBmaIsPowerMgmtSupported_Object = MibScalar
ibBmaIsPowerMgmtSupported = _IbBmaIsPowerMgmtSupported_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 5, 7),
    _IbBmaIsPowerMgmtSupported_Type()
)
ibBmaIsPowerMgmtSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaIsPowerMgmtSupported.setStatus("current")
_IbBmaIsUSleepSupported_Type = TruthValue
_IbBmaIsUSleepSupported_Object = MibScalar
ibBmaIsUSleepSupported = _IbBmaIsUSleepSupported_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 5, 8),
    _IbBmaIsUSleepSupported_Type()
)
ibBmaIsUSleepSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaIsUSleepSupported.setStatus("current")
_IbBmaIsUStandbySupported_Type = TruthValue
_IbBmaIsUStandbySupported_Object = MibScalar
ibBmaIsUStandbySupported = _IbBmaIsUStandbySupported_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 5, 9),
    _IbBmaIsUStandbySupported_Type()
)
ibBmaIsUStandbySupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaIsUStandbySupported.setStatus("current")


class _IbBmaPowerClass_Type(Integer32):
    """Custom type ibBmaPowerClass based on Integer32"""
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
        *(("other", 4),
          ("powerClass1", 2),
          ("powerClass2", 3),
          ("unspecified", 1))
    )


_IbBmaPowerClass_Type.__name__ = "Integer32"
_IbBmaPowerClass_Object = MibScalar
ibBmaPowerClass = _IbBmaPowerClass_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 5, 10),
    _IbBmaPowerClass_Type()
)
ibBmaPowerClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaPowerClass.setStatus("current")


class _IbBmaRedundantPower_Type(Integer32):
    """Custom type ibBmaRedundantPower based on Integer32"""
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
        *(("noRedundancy", 2),
          ("redundancy", 3),
          ("reserved", 4),
          ("unspecified", 1))
    )


_IbBmaRedundantPower_Type.__name__ = "Integer32"
_IbBmaRedundantPower_Object = MibScalar
ibBmaRedundantPower = _IbBmaRedundantPower_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 5, 11),
    _IbBmaRedundantPower_Type()
)
ibBmaRedundantPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaRedundantPower.setStatus("current")
_IbBmaPowerMgmtInfo_ObjectIdentity = ObjectIdentity
ibBmaPowerMgmtInfo = _IbBmaPowerMgmtInfo_ObjectIdentity(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 6)
)


class _IbBmaPowerMgmtIocCount_Type(Integer32):
    """Custom type ibBmaPowerMgmtIocCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IbBmaPowerMgmtIocCount_Type.__name__ = "Integer32"
_IbBmaPowerMgmtIocCount_Object = MibScalar
ibBmaPowerMgmtIocCount = _IbBmaPowerMgmtIocCount_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 6, 1),
    _IbBmaPowerMgmtIocCount_Type()
)
ibBmaPowerMgmtIocCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaPowerMgmtIocCount.setStatus("current")
_IbBmaPowerMgmtIocTable_Object = MibTable
ibBmaPowerMgmtIocTable = _IbBmaPowerMgmtIocTable_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 6, 2)
)
if mibBuilder.loadTexts:
    ibBmaPowerMgmtIocTable.setStatus("current")
_IbBmaPowerMgmtIocEntry_Object = MibTableRow
ibBmaPowerMgmtIocEntry = _IbBmaPowerMgmtIocEntry_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 6, 2, 1)
)
ibBmaPowerMgmtIocEntry.setIndexNames(
    (0, "BMA-MIB", "ibBmaPowerMgmtIocIndex"),
)
if mibBuilder.loadTexts:
    ibBmaPowerMgmtIocEntry.setStatus("current")


class _IbBmaPowerMgmtIocIndex_Type(Integer32):
    """Custom type ibBmaPowerMgmtIocIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_IbBmaPowerMgmtIocIndex_Type.__name__ = "Integer32"
_IbBmaPowerMgmtIocIndex_Object = MibTableColumn
ibBmaPowerMgmtIocIndex = _IbBmaPowerMgmtIocIndex_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 6, 2, 1, 1),
    _IbBmaPowerMgmtIocIndex_Type()
)
ibBmaPowerMgmtIocIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibBmaPowerMgmtIocIndex.setStatus("current")
_IbBmaPMIsIDozeSupported_Type = TruthValue
_IbBmaPMIsIDozeSupported_Object = MibTableColumn
ibBmaPMIsIDozeSupported = _IbBmaPMIsIDozeSupported_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 6, 2, 1, 2),
    _IbBmaPMIsIDozeSupported_Type()
)
ibBmaPMIsIDozeSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaPMIsIDozeSupported.setStatus("current")
_IbBmaPMIsINapSupported_Type = TruthValue
_IbBmaPMIsINapSupported_Object = MibTableColumn
ibBmaPMIsINapSupported = _IbBmaPMIsINapSupported_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 6, 2, 1, 3),
    _IbBmaPMIsINapSupported_Type()
)
ibBmaPMIsINapSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaPMIsINapSupported.setStatus("current")
_IbBmaPMIsISleepSupported_Type = TruthValue
_IbBmaPMIsISleepSupported_Object = MibTableColumn
ibBmaPMIsISleepSupported = _IbBmaPMIsISleepSupported_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 6, 2, 1, 4),
    _IbBmaPMIsISleepSupported_Type()
)
ibBmaPMIsISleepSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaPMIsISleepSupported.setStatus("current")
_IbBmaPMIsIStandbySupported_Type = TruthValue
_IbBmaPMIsIStandbySupported_Object = MibTableColumn
ibBmaPMIsIStandbySupported = _IbBmaPMIsIStandbySupported_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 6, 2, 1, 5),
    _IbBmaPMIsIStandbySupported_Type()
)
ibBmaPMIsIStandbySupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaPMIsIStandbySupported.setStatus("current")
_IbBmaPMWREIsIDozeSupported_Type = TruthValue
_IbBmaPMWREIsIDozeSupported_Object = MibTableColumn
ibBmaPMWREIsIDozeSupported = _IbBmaPMWREIsIDozeSupported_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 6, 2, 1, 6),
    _IbBmaPMWREIsIDozeSupported_Type()
)
ibBmaPMWREIsIDozeSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaPMWREIsIDozeSupported.setStatus("current")
_IbBmaPMWREIsINapSupported_Type = TruthValue
_IbBmaPMWREIsINapSupported_Object = MibTableColumn
ibBmaPMWREIsINapSupported = _IbBmaPMWREIsINapSupported_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 6, 2, 1, 7),
    _IbBmaPMWREIsINapSupported_Type()
)
ibBmaPMWREIsINapSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaPMWREIsINapSupported.setStatus("current")
_IbBmaPMWREIsISleepSupported_Type = TruthValue
_IbBmaPMWREIsISleepSupported_Object = MibTableColumn
ibBmaPMWREIsISleepSupported = _IbBmaPMWREIsISleepSupported_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 6, 2, 1, 8),
    _IbBmaPMWREIsISleepSupported_Type()
)
ibBmaPMWREIsISleepSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaPMWREIsISleepSupported.setStatus("current")
_IbBmaPMWREIsIStandbySupported_Type = TruthValue
_IbBmaPMWREIsIStandbySupported_Object = MibTableColumn
ibBmaPMWREIsIStandbySupported = _IbBmaPMWREIsIStandbySupported_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 6, 2, 1, 9),
    _IbBmaPMWREIsIStandbySupported_Type()
)
ibBmaPMWREIsIStandbySupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaPMWREIsIStandbySupported.setStatus("current")


class _IbBmaPwrMgtIDozeCurrent_Type(Integer32):
    """Custom type ibBmaPwrMgtIDozeCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16384),
    )


_IbBmaPwrMgtIDozeCurrent_Type.__name__ = "Integer32"
_IbBmaPwrMgtIDozeCurrent_Object = MibTableColumn
ibBmaPwrMgtIDozeCurrent = _IbBmaPwrMgtIDozeCurrent_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 6, 2, 1, 10),
    _IbBmaPwrMgtIDozeCurrent_Type()
)
ibBmaPwrMgtIDozeCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaPwrMgtIDozeCurrent.setStatus("current")


class _IbBmaPwrMgtINapCurrent_Type(Integer32):
    """Custom type ibBmaPwrMgtINapCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16384),
    )


_IbBmaPwrMgtINapCurrent_Type.__name__ = "Integer32"
_IbBmaPwrMgtINapCurrent_Object = MibTableColumn
ibBmaPwrMgtINapCurrent = _IbBmaPwrMgtINapCurrent_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 6, 2, 1, 11),
    _IbBmaPwrMgtINapCurrent_Type()
)
ibBmaPwrMgtINapCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaPwrMgtINapCurrent.setStatus("current")


class _IbBmaPwrMgtISleepCurrent_Type(Integer32):
    """Custom type ibBmaPwrMgtISleepCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16384),
    )


_IbBmaPwrMgtISleepCurrent_Type.__name__ = "Integer32"
_IbBmaPwrMgtISleepCurrent_Object = MibTableColumn
ibBmaPwrMgtISleepCurrent = _IbBmaPwrMgtISleepCurrent_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 6, 2, 1, 12),
    _IbBmaPwrMgtISleepCurrent_Type()
)
ibBmaPwrMgtISleepCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaPwrMgtISleepCurrent.setStatus("current")


class _IbBmaPwrMgtIStandbyCurrent_Type(Integer32):
    """Custom type ibBmaPwrMgtIStandbyCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16384),
    )


_IbBmaPwrMgtIStandbyCurrent_Type.__name__ = "Integer32"
_IbBmaPwrMgtIStandbyCurrent_Object = MibTableColumn
ibBmaPwrMgtIStandbyCurrent = _IbBmaPwrMgtIStandbyCurrent_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 6, 2, 1, 13),
    _IbBmaPwrMgtIStandbyCurrent_Type()
)
ibBmaPwrMgtIStandbyCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaPwrMgtIStandbyCurrent.setStatus("current")
_IbBmaCmeInfo_ObjectIdentity = ObjectIdentity
ibBmaCmeInfo = _IbBmaCmeInfo_ObjectIdentity(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 7)
)


class _IbBmaCmeGuidType_Type(Integer32):
    """Custom type ibBmaCmeGuidType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("guid16", 4),
          ("guid48", 3),
          ("guid64", 2),
          ("guid8", 5),
          ("none", 1))
    )


_IbBmaCmeGuidType_Type.__name__ = "Integer32"
_IbBmaCmeGuidType_Object = MibScalar
ibBmaCmeGuidType = _IbBmaCmeGuidType_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 7, 1),
    _IbBmaCmeGuidType_Type()
)
ibBmaCmeGuidType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaCmeGuidType.setStatus("current")


class _IbBmaCmeGuidValue_Type(OctetString):
    """Custom type ibBmaCmeGuidValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_IbBmaCmeGuidValue_Type.__name__ = "OctetString"
_IbBmaCmeGuidValue_Object = MibScalar
ibBmaCmeGuidValue = _IbBmaCmeGuidValue_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 7, 2),
    _IbBmaCmeGuidValue_Type()
)
ibBmaCmeGuidValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaCmeGuidValue.setStatus("current")


class _IbBmaCmeFirmMinorRev_Type(OctetString):
    """Custom type ibBmaCmeFirmMinorRev based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_IbBmaCmeFirmMinorRev_Type.__name__ = "OctetString"
_IbBmaCmeFirmMinorRev_Object = MibScalar
ibBmaCmeFirmMinorRev = _IbBmaCmeFirmMinorRev_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 7, 3),
    _IbBmaCmeFirmMinorRev_Type()
)
ibBmaCmeFirmMinorRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaCmeFirmMinorRev.setStatus("current")


class _IbBmaCmeFirmMajorRev_Type(OctetString):
    """Custom type ibBmaCmeFirmMajorRev based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_IbBmaCmeFirmMajorRev_Type.__name__ = "OctetString"
_IbBmaCmeFirmMajorRev_Object = MibScalar
ibBmaCmeFirmMajorRev = _IbBmaCmeFirmMajorRev_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 7, 4),
    _IbBmaCmeFirmMajorRev_Type()
)
ibBmaCmeFirmMajorRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaCmeFirmMajorRev.setStatus("current")


class _IbBmaCmeSlotNumbers_Type(OctetString):
    """Custom type ibBmaCmeSlotNumbers based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_IbBmaCmeSlotNumbers_Type.__name__ = "OctetString"
_IbBmaCmeSlotNumbers_Object = MibScalar
ibBmaCmeSlotNumbers = _IbBmaCmeSlotNumbers_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 7, 5),
    _IbBmaCmeSlotNumbers_Type()
)
ibBmaCmeSlotNumbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaCmeSlotNumbers.setStatus("current")
_IbBmaOemInfo_ObjectIdentity = ObjectIdentity
ibBmaOemInfo = _IbBmaOemInfo_ObjectIdentity(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 8)
)
_IbBmaOemTable_Object = MibTable
ibBmaOemTable = _IbBmaOemTable_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 8, 1)
)
if mibBuilder.loadTexts:
    ibBmaOemTable.setStatus("current")
_IbBmaOemEntry_Object = MibTableRow
ibBmaOemEntry = _IbBmaOemEntry_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 8, 1, 1)
)
ibBmaOemEntry.setIndexNames(
    (0, "BMA-MIB", "ibBmaOemIndex"),
)
if mibBuilder.loadTexts:
    ibBmaOemEntry.setStatus("current")


class _IbBmaOemIndex_Type(Integer32):
    """Custom type ibBmaOemIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_IbBmaOemIndex_Type.__name__ = "Integer32"
_IbBmaOemIndex_Object = MibTableColumn
ibBmaOemIndex = _IbBmaOemIndex_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 8, 1, 1, 1),
    _IbBmaOemIndex_Type()
)
ibBmaOemIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibBmaOemIndex.setStatus("current")


class _IbBmaOemIdType_Type(Integer32):
    """Custom type ibBmaOemIdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("companyId", 2),
          ("enterpriseNumBased", 3),
          ("other", 1))
    )


_IbBmaOemIdType_Type.__name__ = "Integer32"
_IbBmaOemIdType_Object = MibTableColumn
ibBmaOemIdType = _IbBmaOemIdType_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 8, 1, 1, 2),
    _IbBmaOemIdType_Type()
)
ibBmaOemIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaOemIdType.setStatus("current")


class _IbBmaOemIdValue_Type(OctetString):
    """Custom type ibBmaOemIdValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_IbBmaOemIdValue_Type.__name__ = "OctetString"
_IbBmaOemIdValue_Object = MibTableColumn
ibBmaOemIdValue = _IbBmaOemIdValue_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 8, 1, 1, 3),
    _IbBmaOemIdValue_Type()
)
ibBmaOemIdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaOemIdValue.setStatus("current")


class _IbBmaOemDataLength_Type(Integer32):
    """Custom type ibBmaOemDataLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbBmaOemDataLength_Type.__name__ = "Integer32"
_IbBmaOemDataLength_Object = MibTableColumn
ibBmaOemDataLength = _IbBmaOemDataLength_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 8, 1, 1, 4),
    _IbBmaOemDataLength_Type()
)
ibBmaOemDataLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaOemDataLength.setStatus("current")


class _IbBmaOemDataBuf_Type(OctetString):
    """Custom type ibBmaOemDataBuf based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )


_IbBmaOemDataBuf_Type.__name__ = "OctetString"
_IbBmaOemDataBuf_Object = MibTableColumn
ibBmaOemDataBuf = _IbBmaOemDataBuf_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 8, 1, 1, 5),
    _IbBmaOemDataBuf_Type()
)
ibBmaOemDataBuf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaOemDataBuf.setStatus("current")
_IbBmaBuddyInfo_ObjectIdentity = ObjectIdentity
ibBmaBuddyInfo = _IbBmaBuddyInfo_ObjectIdentity(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 9)
)


class _IbBmaBuddyCount_Type(Integer32):
    """Custom type ibBmaBuddyCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IbBmaBuddyCount_Type.__name__ = "Integer32"
_IbBmaBuddyCount_Object = MibScalar
ibBmaBuddyCount = _IbBmaBuddyCount_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 9, 1),
    _IbBmaBuddyCount_Type()
)
ibBmaBuddyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaBuddyCount.setStatus("current")
_IbBmaBuddyTable_Object = MibTable
ibBmaBuddyTable = _IbBmaBuddyTable_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 9, 2)
)
if mibBuilder.loadTexts:
    ibBmaBuddyTable.setStatus("current")
_IbBmaBuddyEntry_Object = MibTableRow
ibBmaBuddyEntry = _IbBmaBuddyEntry_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 9, 2, 1)
)
ibBmaBuddyEntry.setIndexNames(
    (0, "BMA-MIB", "ibBmaBuddyIndex"),
)
if mibBuilder.loadTexts:
    ibBmaBuddyEntry.setStatus("current")


class _IbBmaBuddyIndex_Type(Integer32):
    """Custom type ibBmaBuddyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IbBmaBuddyIndex_Type.__name__ = "Integer32"
_IbBmaBuddyIndex_Object = MibTableColumn
ibBmaBuddyIndex = _IbBmaBuddyIndex_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 9, 2, 1, 1),
    _IbBmaBuddyIndex_Type()
)
ibBmaBuddyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibBmaBuddyIndex.setStatus("current")


class _IbBmaBuddyGuidType_Type(Integer32):
    """Custom type ibBmaBuddyGuidType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("guid16", 4),
          ("guid48", 3),
          ("guid64", 2),
          ("guid8", 5),
          ("none", 1))
    )


_IbBmaBuddyGuidType_Type.__name__ = "Integer32"
_IbBmaBuddyGuidType_Object = MibTableColumn
ibBmaBuddyGuidType = _IbBmaBuddyGuidType_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 9, 2, 1, 2),
    _IbBmaBuddyGuidType_Type()
)
ibBmaBuddyGuidType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaBuddyGuidType.setStatus("current")


class _IbBmaBuddyGuidValue_Type(OctetString):
    """Custom type ibBmaBuddyGuidValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_IbBmaBuddyGuidValue_Type.__name__ = "OctetString"
_IbBmaBuddyGuidValue_Object = MibTableColumn
ibBmaBuddyGuidValue = _IbBmaBuddyGuidValue_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 9, 2, 1, 3),
    _IbBmaBuddyGuidValue_Type()
)
ibBmaBuddyGuidValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaBuddyGuidValue.setStatus("current")
_IbBmaAssetTagInfo_ObjectIdentity = ObjectIdentity
ibBmaAssetTagInfo = _IbBmaAssetTagInfo_ObjectIdentity(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 10)
)
_IbBmaAssetTagTable_Object = MibTable
ibBmaAssetTagTable = _IbBmaAssetTagTable_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 10, 1)
)
if mibBuilder.loadTexts:
    ibBmaAssetTagTable.setStatus("current")
_IbBmaAssetTagEntry_Object = MibTableRow
ibBmaAssetTagEntry = _IbBmaAssetTagEntry_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 10, 1, 1)
)
ibBmaAssetTagEntry.setIndexNames(
    (0, "BMA-MIB", "ibBmaAssetTagIndex"),
)
if mibBuilder.loadTexts:
    ibBmaAssetTagEntry.setStatus("current")


class _IbBmaAssetTagIndex_Type(Integer32):
    """Custom type ibBmaAssetTagIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IbBmaAssetTagIndex_Type.__name__ = "Integer32"
_IbBmaAssetTagIndex_Object = MibTableColumn
ibBmaAssetTagIndex = _IbBmaAssetTagIndex_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 10, 1, 1, 1),
    _IbBmaAssetTagIndex_Type()
)
ibBmaAssetTagIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibBmaAssetTagIndex.setStatus("current")


class _IbBmaAssetTagFruHandle_Type(Integer32):
    """Custom type ibBmaAssetTagFruHandle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IbBmaAssetTagFruHandle_Type.__name__ = "Integer32"
_IbBmaAssetTagFruHandle_Object = MibTableColumn
ibBmaAssetTagFruHandle = _IbBmaAssetTagFruHandle_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 10, 1, 1, 2),
    _IbBmaAssetTagFruHandle_Type()
)
ibBmaAssetTagFruHandle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaAssetTagFruHandle.setStatus("current")


class _IbBmaAssetTagLength_Type(Integer32):
    """Custom type ibBmaAssetTagLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IbBmaAssetTagLength_Type.__name__ = "Integer32"
_IbBmaAssetTagLength_Object = MibTableColumn
ibBmaAssetTagLength = _IbBmaAssetTagLength_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 10, 1, 1, 3),
    _IbBmaAssetTagLength_Type()
)
ibBmaAssetTagLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaAssetTagLength.setStatus("current")


class _IbBmaAssetTagValue_Type(OctetString):
    """Custom type ibBmaAssetTagValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )


_IbBmaAssetTagValue_Type.__name__ = "OctetString"
_IbBmaAssetTagValue_Object = MibTableColumn
ibBmaAssetTagValue = _IbBmaAssetTagValue_Object(
    (1, 3, 6, 1, 3, 117, 5, 1, 3, 10, 1, 1, 4),
    _IbBmaAssetTagValue_Type()
)
ibBmaAssetTagValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibBmaAssetTagValue.setStatus("current")
_IbBmaConformance_ObjectIdentity = ObjectIdentity
ibBmaConformance = _IbBmaConformance_ObjectIdentity(
    (1, 3, 6, 1, 3, 117, 5, 2)
)
_IbBmaCompliances_ObjectIdentity = ObjectIdentity
ibBmaCompliances = _IbBmaCompliances_ObjectIdentity(
    (1, 3, 6, 1, 3, 117, 5, 2, 1)
)
_IbBmaGroups_ObjectIdentity = ObjectIdentity
ibBmaGroups = _IbBmaGroups_ObjectIdentity(
    (1, 3, 6, 1, 3, 117, 5, 2, 2)
)

# Managed Objects groups

ibBmaBmuInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 117, 5, 2, 2, 1)
)
ibBmaBmuInfoGroup.setObjects(
      *(("BMA-MIB", "ibBmaBaseboardManagedUnitType"),
        ("BMA-MIB", "ibBmaIsIBMLSupported"),
        ("BMA-MIB", "ibBmaIBMLImplementation"))
)
if mibBuilder.loadTexts:
    ibBmaBmuInfoGroup.setStatus("current")

ibBmaBKeyInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 117, 5, 2, 2, 2)
)
ibBmaBKeyInfoGroup.setObjects(
      *(("BMA-MIB", "ibBmaIsBKeyNVRAM"),
        ("BMA-MIB", "ibBmaBKeyValue"),
        ("BMA-MIB", "ibBmaBKeyProtectBit"),
        ("BMA-MIB", "ibBmaBKeyLeasePeriod"),
        ("BMA-MIB", "ibBmaBKeyViolations"))
)
if mibBuilder.loadTexts:
    ibBmaBKeyInfoGroup.setStatus("current")

ibBmaModuleInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 117, 5, 2, 2, 3)
)
ibBmaModuleInfoGroup.setObjects(
      *(("BMA-MIB", "ibBmaModInfoModGuid"),
        ("BMA-MIB", "ibBmaModInfoModType"),
        ("BMA-MIB", "ibBmaModInfoModClass"),
        ("BMA-MIB", "ibBmaModInfoNodeCount"),
        ("BMA-MIB", "ibBmaModInfoLinkCount"),
        ("BMA-MIB", "ibBmaModInfoBckplaneLinkCnt"),
        ("BMA-MIB", "ibBmaModInfoIbmlCount"),
        ("BMA-MIB", "ibBmaModInfoBckPlaneIbmlCnt"),
        ("BMA-MIB", "ibBmaModInfoModuleSize"),
        ("BMA-MIB", "ibBmaModInfoFormFactor"))
)
if mibBuilder.loadTexts:
    ibBmaModuleInfoGroup.setStatus("current")

ibBmaChassisInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 117, 5, 2, 2, 4)
)
ibBmaChassisInfoGroup.setObjects(
      *(("BMA-MIB", "ibBmaChasInfoChassisGuid"),
        ("BMA-MIB", "ibBmaChasInfoSlotCount"),
        ("BMA-MIB", "ibBmaChasInfoAssignedSlotNum"),
        ("BMA-MIB", "ibBmaChasInfoSlotConnStatus"),
        ("BMA-MIB", "ibBmaChasInfoCmeAccess"),
        ("BMA-MIB", "ibBmaChasInfoProxyAccess"),
        ("BMA-MIB", "ibBmaChasInfoLockDrivesCtr"),
        ("BMA-MIB", "ibBmaChasInfoMechLockPresent"))
)
if mibBuilder.loadTexts:
    ibBmaChassisInfoGroup.setStatus("current")

ibBmaFruInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 117, 5, 2, 2, 5)
)
ibBmaFruInfoGroup.setObjects(
      *(("BMA-MIB", "ibBmaFruInfoType"),
        ("BMA-MIB", "ibBmaFruInfoGuidType"),
        ("BMA-MIB", "ibBmaFruInfoGuidValue"),
        ("BMA-MIB", "ibBmaFruInfoSerialNumber"),
        ("BMA-MIB", "ibBmaFruInfoPartNumber"),
        ("BMA-MIB", "ibBmaFruInfoModelName"),
        ("BMA-MIB", "ibBmaFruInfoVersion"),
        ("BMA-MIB", "ibBmaFruInfoManufacturerName"),
        ("BMA-MIB", "ibBmaFruInfoProductName"),
        ("BMA-MIB", "ibBmaFruInfoManufacturerID"),
        ("BMA-MIB", "ibBmaFruInfoManDateAndTime"))
)
if mibBuilder.loadTexts:
    ibBmaFruInfoGroup.setStatus("current")

ibBmaPortConnectInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 117, 5, 2, 2, 6)
)
ibBmaPortConnectInfoGroup.setObjects(
      *(("BMA-MIB", "ibBmaPortConNumConnection"),
        ("BMA-MIB", "ibBmaPortConInternalCon"),
        ("BMA-MIB", "ibBmaPortConMediaClass"),
        ("BMA-MIB", "ibBmaPortConConClass"))
)
if mibBuilder.loadTexts:
    ibBmaPortConnectInfoGroup.setStatus("current")

ibBmaModPowerInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 117, 5, 2, 2, 7)
)
ibBmaModPowerInfoGroup.setObjects(
      *(("BMA-MIB", "ibBmaOperThermalPower"),
        ("BMA-MIB", "ibBmaOperCurrent"),
        ("BMA-MIB", "ibBmaIdleCurrent"),
        ("BMA-MIB", "ibBmaInitCurrent"),
        ("BMA-MIB", "ibBmaInitTime"),
        ("BMA-MIB", "ibBmaIsMStandbySupported"),
        ("BMA-MIB", "ibBmaIsPowerMgmtSupported"),
        ("BMA-MIB", "ibBmaIsUSleepSupported"),
        ("BMA-MIB", "ibBmaIsUStandbySupported"),
        ("BMA-MIB", "ibBmaPowerClass"),
        ("BMA-MIB", "ibBmaRedundantPower"))
)
if mibBuilder.loadTexts:
    ibBmaModPowerInfoGroup.setStatus("current")

ibBmaPowerMgmtInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 117, 5, 2, 2, 8)
)
ibBmaPowerMgmtInfoGroup.setObjects(
      *(("BMA-MIB", "ibBmaPowerMgmtIocCount"),
        ("BMA-MIB", "ibBmaPMIsIDozeSupported"),
        ("BMA-MIB", "ibBmaPMIsINapSupported"),
        ("BMA-MIB", "ibBmaPMIsISleepSupported"),
        ("BMA-MIB", "ibBmaPMIsIStandbySupported"),
        ("BMA-MIB", "ibBmaPMWREIsIDozeSupported"),
        ("BMA-MIB", "ibBmaPMWREIsINapSupported"),
        ("BMA-MIB", "ibBmaPMWREIsISleepSupported"),
        ("BMA-MIB", "ibBmaPMWREIsIStandbySupported"),
        ("BMA-MIB", "ibBmaPwrMgtIDozeCurrent"),
        ("BMA-MIB", "ibBmaPwrMgtINapCurrent"),
        ("BMA-MIB", "ibBmaPwrMgtISleepCurrent"),
        ("BMA-MIB", "ibBmaPwrMgtIStandbyCurrent"))
)
if mibBuilder.loadTexts:
    ibBmaPowerMgmtInfoGroup.setStatus("current")

ibBmaCmeInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 117, 5, 2, 2, 9)
)
ibBmaCmeInfoGroup.setObjects(
      *(("BMA-MIB", "ibBmaCmeGuidType"),
        ("BMA-MIB", "ibBmaCmeGuidValue"),
        ("BMA-MIB", "ibBmaCmeFirmMinorRev"),
        ("BMA-MIB", "ibBmaCmeFirmMajorRev"),
        ("BMA-MIB", "ibBmaCmeSlotNumbers"))
)
if mibBuilder.loadTexts:
    ibBmaCmeInfoGroup.setStatus("current")

ibBmaOemInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 117, 5, 2, 2, 10)
)
ibBmaOemInfoGroup.setObjects(
      *(("BMA-MIB", "ibBmaOemIdType"),
        ("BMA-MIB", "ibBmaOemIdValue"),
        ("BMA-MIB", "ibBmaOemDataLength"),
        ("BMA-MIB", "ibBmaOemDataBuf"))
)
if mibBuilder.loadTexts:
    ibBmaOemInfoGroup.setStatus("current")

ibBmaBuddyInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 117, 5, 2, 2, 11)
)
ibBmaBuddyInfoGroup.setObjects(
      *(("BMA-MIB", "ibBmaBuddyCount"),
        ("BMA-MIB", "ibBmaBuddyGuidType"),
        ("BMA-MIB", "ibBmaBuddyGuidValue"))
)
if mibBuilder.loadTexts:
    ibBmaBuddyInfoGroup.setStatus("current")

ibBmaAssetTagInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 117, 5, 2, 2, 12)
)
ibBmaAssetTagInfoGroup.setObjects(
      *(("BMA-MIB", "ibBmaAssetTagFruHandle"),
        ("BMA-MIB", "ibBmaAssetTagLength"),
        ("BMA-MIB", "ibBmaAssetTagValue"))
)
if mibBuilder.loadTexts:
    ibBmaAssetTagInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ibBmaBasicNodeCompliance = ModuleCompliance(
    (1, 3, 6, 1, 3, 117, 5, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ibBmaBasicNodeCompliance.setStatus(
        "current"
    )

ibBmaFullNodeCompliance = ModuleCompliance(
    (1, 3, 6, 1, 3, 117, 5, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ibBmaFullNodeCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BMA-MIB",
    **{"ibBmaMIB": ibBmaMIB,
       "ibBmaObjects": ibBmaObjects,
       "ibBmaBmuInfo": ibBmaBmuInfo,
       "ibBmaBaseboardManagedUnitType": ibBmaBaseboardManagedUnitType,
       "ibBmaIsIBMLSupported": ibBmaIsIBMLSupported,
       "ibBmaIBMLImplementation": ibBmaIBMLImplementation,
       "ibBmaBKeyInfo": ibBmaBKeyInfo,
       "ibBmaIsBKeyNVRAM": ibBmaIsBKeyNVRAM,
       "ibBmaBKeyValue": ibBmaBKeyValue,
       "ibBmaBKeyProtectBit": ibBmaBKeyProtectBit,
       "ibBmaBKeyLeasePeriod": ibBmaBKeyLeasePeriod,
       "ibBmaBKeyViolations": ibBmaBKeyViolations,
       "ibBmaVpd": ibBmaVpd,
       "ibBmaModuleInfo": ibBmaModuleInfo,
       "ibBmaModuleInfoTable": ibBmaModuleInfoTable,
       "ibBmaModuleInfoEntry": ibBmaModuleInfoEntry,
       "ibBmaModuleInfoIndex": ibBmaModuleInfoIndex,
       "ibBmaModInfoModGuid": ibBmaModInfoModGuid,
       "ibBmaModInfoModType": ibBmaModInfoModType,
       "ibBmaModInfoModClass": ibBmaModInfoModClass,
       "ibBmaModInfoNodeCount": ibBmaModInfoNodeCount,
       "ibBmaModInfoLinkCount": ibBmaModInfoLinkCount,
       "ibBmaModInfoBckplaneLinkCnt": ibBmaModInfoBckplaneLinkCnt,
       "ibBmaModInfoIbmlCount": ibBmaModInfoIbmlCount,
       "ibBmaModInfoBckPlaneIbmlCnt": ibBmaModInfoBckPlaneIbmlCnt,
       "ibBmaModInfoModuleSize": ibBmaModInfoModuleSize,
       "ibBmaModInfoFormFactor": ibBmaModInfoFormFactor,
       "ibBmaChassisInfo": ibBmaChassisInfo,
       "ibBmaChasInfoChassisGuid": ibBmaChasInfoChassisGuid,
       "ibBmaChasInfoSlotCount": ibBmaChasInfoSlotCount,
       "ibBmaChasInfoSlotTable": ibBmaChasInfoSlotTable,
       "ibBmaChasInfoSlotEntry": ibBmaChasInfoSlotEntry,
       "ibBmaChasInfoSlotIndex": ibBmaChasInfoSlotIndex,
       "ibBmaChasInfoAssignedSlotNum": ibBmaChasInfoAssignedSlotNum,
       "ibBmaChasInfoSlotConnStatus": ibBmaChasInfoSlotConnStatus,
       "ibBmaChasInfoCmeAccess": ibBmaChasInfoCmeAccess,
       "ibBmaChasInfoProxyAccess": ibBmaChasInfoProxyAccess,
       "ibBmaChasInfoLockDrivesCtr": ibBmaChasInfoLockDrivesCtr,
       "ibBmaChasInfoMechLockPresent": ibBmaChasInfoMechLockPresent,
       "ibBmaFruInfo": ibBmaFruInfo,
       "ibBmaFruInfoTable": ibBmaFruInfoTable,
       "ibBmaFruInfoEntry": ibBmaFruInfoEntry,
       "ibBmaFruInfoIndex": ibBmaFruInfoIndex,
       "ibBmaFruInfoType": ibBmaFruInfoType,
       "ibBmaFruInfoGuidType": ibBmaFruInfoGuidType,
       "ibBmaFruInfoGuidValue": ibBmaFruInfoGuidValue,
       "ibBmaFruInfoSerialNumber": ibBmaFruInfoSerialNumber,
       "ibBmaFruInfoPartNumber": ibBmaFruInfoPartNumber,
       "ibBmaFruInfoModelName": ibBmaFruInfoModelName,
       "ibBmaFruInfoVersion": ibBmaFruInfoVersion,
       "ibBmaFruInfoManufacturerName": ibBmaFruInfoManufacturerName,
       "ibBmaFruInfoProductName": ibBmaFruInfoProductName,
       "ibBmaFruInfoManufacturerID": ibBmaFruInfoManufacturerID,
       "ibBmaFruInfoManDateAndTime": ibBmaFruInfoManDateAndTime,
       "ibBmaPortConnectInfo": ibBmaPortConnectInfo,
       "ibBmaPortConNumConnection": ibBmaPortConNumConnection,
       "ibBmaPortConnectTable": ibBmaPortConnectTable,
       "ibBmaPortConnectEntry": ibBmaPortConnectEntry,
       "ibBmaPortConnectIndex": ibBmaPortConnectIndex,
       "ibBmaPortConInternalCon": ibBmaPortConInternalCon,
       "ibBmaPortConMediaClass": ibBmaPortConMediaClass,
       "ibBmaPortConConClass": ibBmaPortConConClass,
       "ibBmaModPowerInfo": ibBmaModPowerInfo,
       "ibBmaOperThermalPower": ibBmaOperThermalPower,
       "ibBmaOperCurrent": ibBmaOperCurrent,
       "ibBmaIdleCurrent": ibBmaIdleCurrent,
       "ibBmaInitCurrent": ibBmaInitCurrent,
       "ibBmaInitTime": ibBmaInitTime,
       "ibBmaIsMStandbySupported": ibBmaIsMStandbySupported,
       "ibBmaIsPowerMgmtSupported": ibBmaIsPowerMgmtSupported,
       "ibBmaIsUSleepSupported": ibBmaIsUSleepSupported,
       "ibBmaIsUStandbySupported": ibBmaIsUStandbySupported,
       "ibBmaPowerClass": ibBmaPowerClass,
       "ibBmaRedundantPower": ibBmaRedundantPower,
       "ibBmaPowerMgmtInfo": ibBmaPowerMgmtInfo,
       "ibBmaPowerMgmtIocCount": ibBmaPowerMgmtIocCount,
       "ibBmaPowerMgmtIocTable": ibBmaPowerMgmtIocTable,
       "ibBmaPowerMgmtIocEntry": ibBmaPowerMgmtIocEntry,
       "ibBmaPowerMgmtIocIndex": ibBmaPowerMgmtIocIndex,
       "ibBmaPMIsIDozeSupported": ibBmaPMIsIDozeSupported,
       "ibBmaPMIsINapSupported": ibBmaPMIsINapSupported,
       "ibBmaPMIsISleepSupported": ibBmaPMIsISleepSupported,
       "ibBmaPMIsIStandbySupported": ibBmaPMIsIStandbySupported,
       "ibBmaPMWREIsIDozeSupported": ibBmaPMWREIsIDozeSupported,
       "ibBmaPMWREIsINapSupported": ibBmaPMWREIsINapSupported,
       "ibBmaPMWREIsISleepSupported": ibBmaPMWREIsISleepSupported,
       "ibBmaPMWREIsIStandbySupported": ibBmaPMWREIsIStandbySupported,
       "ibBmaPwrMgtIDozeCurrent": ibBmaPwrMgtIDozeCurrent,
       "ibBmaPwrMgtINapCurrent": ibBmaPwrMgtINapCurrent,
       "ibBmaPwrMgtISleepCurrent": ibBmaPwrMgtISleepCurrent,
       "ibBmaPwrMgtIStandbyCurrent": ibBmaPwrMgtIStandbyCurrent,
       "ibBmaCmeInfo": ibBmaCmeInfo,
       "ibBmaCmeGuidType": ibBmaCmeGuidType,
       "ibBmaCmeGuidValue": ibBmaCmeGuidValue,
       "ibBmaCmeFirmMinorRev": ibBmaCmeFirmMinorRev,
       "ibBmaCmeFirmMajorRev": ibBmaCmeFirmMajorRev,
       "ibBmaCmeSlotNumbers": ibBmaCmeSlotNumbers,
       "ibBmaOemInfo": ibBmaOemInfo,
       "ibBmaOemTable": ibBmaOemTable,
       "ibBmaOemEntry": ibBmaOemEntry,
       "ibBmaOemIndex": ibBmaOemIndex,
       "ibBmaOemIdType": ibBmaOemIdType,
       "ibBmaOemIdValue": ibBmaOemIdValue,
       "ibBmaOemDataLength": ibBmaOemDataLength,
       "ibBmaOemDataBuf": ibBmaOemDataBuf,
       "ibBmaBuddyInfo": ibBmaBuddyInfo,
       "ibBmaBuddyCount": ibBmaBuddyCount,
       "ibBmaBuddyTable": ibBmaBuddyTable,
       "ibBmaBuddyEntry": ibBmaBuddyEntry,
       "ibBmaBuddyIndex": ibBmaBuddyIndex,
       "ibBmaBuddyGuidType": ibBmaBuddyGuidType,
       "ibBmaBuddyGuidValue": ibBmaBuddyGuidValue,
       "ibBmaAssetTagInfo": ibBmaAssetTagInfo,
       "ibBmaAssetTagTable": ibBmaAssetTagTable,
       "ibBmaAssetTagEntry": ibBmaAssetTagEntry,
       "ibBmaAssetTagIndex": ibBmaAssetTagIndex,
       "ibBmaAssetTagFruHandle": ibBmaAssetTagFruHandle,
       "ibBmaAssetTagLength": ibBmaAssetTagLength,
       "ibBmaAssetTagValue": ibBmaAssetTagValue,
       "ibBmaConformance": ibBmaConformance,
       "ibBmaCompliances": ibBmaCompliances,
       "ibBmaBasicNodeCompliance": ibBmaBasicNodeCompliance,
       "ibBmaFullNodeCompliance": ibBmaFullNodeCompliance,
       "ibBmaGroups": ibBmaGroups,
       "ibBmaBmuInfoGroup": ibBmaBmuInfoGroup,
       "ibBmaBKeyInfoGroup": ibBmaBKeyInfoGroup,
       "ibBmaModuleInfoGroup": ibBmaModuleInfoGroup,
       "ibBmaChassisInfoGroup": ibBmaChassisInfoGroup,
       "ibBmaFruInfoGroup": ibBmaFruInfoGroup,
       "ibBmaPortConnectInfoGroup": ibBmaPortConnectInfoGroup,
       "ibBmaModPowerInfoGroup": ibBmaModPowerInfoGroup,
       "ibBmaPowerMgmtInfoGroup": ibBmaPowerMgmtInfoGroup,
       "ibBmaCmeInfoGroup": ibBmaCmeInfoGroup,
       "ibBmaOemInfoGroup": ibBmaOemInfoGroup,
       "ibBmaBuddyInfoGroup": ibBmaBuddyInfoGroup,
       "ibBmaAssetTagInfoGroup": ibBmaAssetTagInfoGroup}
)
