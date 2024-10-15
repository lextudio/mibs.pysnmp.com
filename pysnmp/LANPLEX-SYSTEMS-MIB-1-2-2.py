# SNMP MIB module (LANPLEX-SYSTEMS-MIB-1-2-2) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LANPLEX-SYSTEMS-MIB-1-2-2
# Produced by pysmi-1.5.4 at Mon Oct 14 22:17:18 2024
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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Synernetics_ObjectIdentity = ObjectIdentity
synernetics = _Synernetics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114)
)
_Lanplex_ObjectIdentity = ObjectIdentity
lanplex = _Lanplex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1)
)
_LpsProducts_ObjectIdentity = ObjectIdentity
lpsProducts = _LpsProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3)
)
_Lps6000_ObjectIdentity = ObjectIdentity
lps6000 = _Lps6000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2)
)
_Lps6012_ObjectIdentity = ObjectIdentity
lps6012 = _Lps6012_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 1)
)
_Lps6012System_ObjectIdentity = ObjectIdentity
lps6012System = _Lps6012System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 1, 1)
)
_Lps6012Chassis_ObjectIdentity = ObjectIdentity
lps6012Chassis = _Lps6012Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 1, 2)
)
_Lps6012ESM_ObjectIdentity = ObjectIdentity
lps6012ESM = _Lps6012ESM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 1, 3)
)
_Lps6012EFSM_ObjectIdentity = ObjectIdentity
lps6012EFSM = _Lps6012EFSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 1, 4)
)
_Lps6012TRSM_ObjectIdentity = ObjectIdentity
lps6012TRSM = _Lps6012TRSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 1, 5)
)
_Lps6012TMM_ObjectIdentity = ObjectIdentity
lps6012TMM = _Lps6012TMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 1, 6)
)
_Lps6004_ObjectIdentity = ObjectIdentity
lps6004 = _Lps6004_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 2)
)
_Lps6004System_ObjectIdentity = ObjectIdentity
lps6004System = _Lps6004System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 2, 1)
)
_Lps6004Chassis_ObjectIdentity = ObjectIdentity
lps6004Chassis = _Lps6004Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 2, 2)
)
_Lps6004ESM_ObjectIdentity = ObjectIdentity
lps6004ESM = _Lps6004ESM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 2, 3)
)
_Lps6004EFSM_ObjectIdentity = ObjectIdentity
lps6004EFSM = _Lps6004EFSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 2, 4)
)
_Lps6004TRSM_ObjectIdentity = ObjectIdentity
lps6004TRSM = _Lps6004TRSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 2, 5)
)
_Lps6004TMM_ObjectIdentity = ObjectIdentity
lps6004TMM = _Lps6004TMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 2, 2, 6)
)
_Lps2000_ObjectIdentity = ObjectIdentity
lps2000 = _Lps2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 3)
)
_Lps2500_ObjectIdentity = ObjectIdentity
lps2500 = _Lps2500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 3, 1)
)
_Lss2200_ObjectIdentity = ObjectIdentity
lss2200 = _Lss2200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 3, 2)
)
_Lps2016_ObjectIdentity = ObjectIdentity
lps2016 = _Lps2016_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 3, 3, 3)
)
_LanplexSystemsMib_ObjectIdentity = ObjectIdentity
lanplexSystemsMib = _LanplexSystemsMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 4)
)
_LpsSystem_ObjectIdentity = ObjectIdentity
lpsSystem = _LpsSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 1)
)
_LpsSystemId_Type = Integer32
_LpsSystemId_Object = MibScalar
lpsSystemId = _LpsSystemId_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 1, 1),
    _LpsSystemId_Type()
)
lpsSystemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsSystemId.setStatus("mandatory")


class _LpsSystemType_Type(Integer32):
    """Custom type lpsSystemType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lanplex2000", 3),
          ("lanplex6000", 2),
          ("other", 1))
    )


_LpsSystemType_Type.__name__ = "Integer32"
_LpsSystemType_Object = MibScalar
lpsSystemType = _LpsSystemType_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 1, 2),
    _LpsSystemType_Type()
)
lpsSystemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsSystemType.setStatus("mandatory")


class _LpsSystemName_Type(DisplayString):
    """Custom type lpsSystemName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_LpsSystemName_Type.__name__ = "DisplayString"
_LpsSystemName_Object = MibScalar
lpsSystemName = _LpsSystemName_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 1, 3),
    _LpsSystemName_Type()
)
lpsSystemName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpsSystemName.setStatus("mandatory")


class _LpsSystemManufacturer_Type(DisplayString):
    """Custom type lpsSystemManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_LpsSystemManufacturer_Type.__name__ = "DisplayString"
_LpsSystemManufacturer_Object = MibScalar
lpsSystemManufacturer = _LpsSystemManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 1, 4),
    _LpsSystemManufacturer_Type()
)
lpsSystemManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsSystemManufacturer.setStatus("mandatory")


class _LpsSystemHardwareRevision_Type(OctetString):
    """Custom type lpsSystemHardwareRevision based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_LpsSystemHardwareRevision_Type.__name__ = "OctetString"
_LpsSystemHardwareRevision_Object = MibScalar
lpsSystemHardwareRevision = _LpsSystemHardwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 1, 5),
    _LpsSystemHardwareRevision_Type()
)
lpsSystemHardwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsSystemHardwareRevision.setStatus("mandatory")
_LpsSystemMemorySize_Type = Integer32
_LpsSystemMemorySize_Object = MibScalar
lpsSystemMemorySize = _LpsSystemMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 1, 6),
    _LpsSystemMemorySize_Type()
)
lpsSystemMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsSystemMemorySize.setStatus("mandatory")
_LpsSystemFlashMemorySize_Type = Integer32
_LpsSystemFlashMemorySize_Object = MibScalar
lpsSystemFlashMemorySize = _LpsSystemFlashMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 1, 7),
    _LpsSystemFlashMemorySize_Type()
)
lpsSystemFlashMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsSystemFlashMemorySize.setStatus("mandatory")
_LpsSystemNvMemorySize_Type = Integer32
_LpsSystemNvMemorySize_Object = MibScalar
lpsSystemNvMemorySize = _LpsSystemNvMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 1, 8),
    _LpsSystemNvMemorySize_Type()
)
lpsSystemNvMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsSystemNvMemorySize.setStatus("mandatory")


class _LpsSystemSoftwareRevision_Type(OctetString):
    """Custom type lpsSystemSoftwareRevision based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_LpsSystemSoftwareRevision_Type.__name__ = "OctetString"
_LpsSystemSoftwareRevision_Object = MibScalar
lpsSystemSoftwareRevision = _LpsSystemSoftwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 1, 9),
    _LpsSystemSoftwareRevision_Type()
)
lpsSystemSoftwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsSystemSoftwareRevision.setStatus("mandatory")


class _LpsSystemBuildTime_Type(DisplayString):
    """Custom type lpsSystemBuildTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_LpsSystemBuildTime_Type.__name__ = "DisplayString"
_LpsSystemBuildTime_Object = MibScalar
lpsSystemBuildTime = _LpsSystemBuildTime_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 1, 10),
    _LpsSystemBuildTime_Type()
)
lpsSystemBuildTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsSystemBuildTime.setStatus("mandatory")
_LpsSystemSnmpRevision_Type = Integer32
_LpsSystemSnmpRevision_Object = MibScalar
lpsSystemSnmpRevision = _LpsSystemSnmpRevision_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 1, 11),
    _LpsSystemSnmpRevision_Type()
)
lpsSystemSnmpRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsSystemSnmpRevision.setStatus("mandatory")


class _LpsSystemRequestedSnmpMode_Type(Integer32):
    """Custom type lpsSystemRequestedSnmpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multiAgentMode", 2),
          ("singleAgentMode", 1))
    )


_LpsSystemRequestedSnmpMode_Type.__name__ = "Integer32"
_LpsSystemRequestedSnmpMode_Object = MibScalar
lpsSystemRequestedSnmpMode = _LpsSystemRequestedSnmpMode_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 1, 12),
    _LpsSystemRequestedSnmpMode_Type()
)
lpsSystemRequestedSnmpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpsSystemRequestedSnmpMode.setStatus("mandatory")


class _LpsSystemCurrentSnmpMode_Type(Integer32):
    """Custom type lpsSystemCurrentSnmpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multiAgentMode", 2),
          ("singleAgentMode", 1))
    )


_LpsSystemCurrentSnmpMode_Type.__name__ = "Integer32"
_LpsSystemCurrentSnmpMode_Object = MibScalar
lpsSystemCurrentSnmpMode = _LpsSystemCurrentSnmpMode_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 1, 13),
    _LpsSystemCurrentSnmpMode_Type()
)
lpsSystemCurrentSnmpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsSystemCurrentSnmpMode.setStatus("mandatory")


class _LpsSystemAction_Type(Integer32):
    """Custom type lpsSystemAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("reset", 2))
    )


_LpsSystemAction_Type.__name__ = "Integer32"
_LpsSystemAction_Object = MibScalar
lpsSystemAction = _LpsSystemAction_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 1, 14),
    _LpsSystemAction_Type()
)
lpsSystemAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpsSystemAction.setStatus("mandatory")


class _LpsSystemOvertemperature_Type(Integer32):
    """Custom type lpsSystemOvertemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("notSupported", 3),
          ("true", 1))
    )


_LpsSystemOvertemperature_Type.__name__ = "Integer32"
_LpsSystemOvertemperature_Object = MibScalar
lpsSystemOvertemperature = _LpsSystemOvertemperature_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 1, 15),
    _LpsSystemOvertemperature_Type()
)
lpsSystemOvertemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsSystemOvertemperature.setStatus("mandatory")


class _LpsSystemFanFailure_Type(Integer32):
    """Custom type lpsSystemFanFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("notSupported", 3),
          ("true", 1))
    )


_LpsSystemFanFailure_Type.__name__ = "Integer32"
_LpsSystemFanFailure_Object = MibScalar
lpsSystemFanFailure = _LpsSystemFanFailure_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 1, 16),
    _LpsSystemFanFailure_Type()
)
lpsSystemFanFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsSystemFanFailure.setStatus("mandatory")
_LpsSystemProtocolMask_Type = Integer32
_LpsSystemProtocolMask_Object = MibScalar
lpsSystemProtocolMask = _LpsSystemProtocolMask_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 1, 17),
    _LpsSystemProtocolMask_Type()
)
lpsSystemProtocolMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsSystemProtocolMask.setStatus("mandatory")
_LpsSlot_ObjectIdentity = ObjectIdentity
lpsSlot = _LpsSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 2)
)
_LpsSlotCount_Type = Integer32
_LpsSlotCount_Object = MibScalar
lpsSlotCount = _LpsSlotCount_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 2, 1),
    _LpsSlotCount_Type()
)
lpsSlotCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsSlotCount.setStatus("mandatory")
_LpsSlotTable_Object = MibTable
lpsSlotTable = _LpsSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 2, 2)
)
if mibBuilder.loadTexts:
    lpsSlotTable.setStatus("mandatory")
_LpsSlotEntry_Object = MibTableRow
lpsSlotEntry = _LpsSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 2, 2, 1)
)
lpsSlotEntry.setIndexNames(
    (0, "LANPLEX-SYSTEMS-MIB-1-2-2", "lpsSlotIndex"),
)
if mibBuilder.loadTexts:
    lpsSlotEntry.setStatus("mandatory")
_LpsSlotIndex_Type = Integer32
_LpsSlotIndex_Object = MibTableColumn
lpsSlotIndex = _LpsSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 2, 2, 1, 1),
    _LpsSlotIndex_Type()
)
lpsSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsSlotIndex.setStatus("mandatory")


class _LpsSlotBoardType_Type(Integer32):
    """Custom type lpsSlotBoardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("efsmBoard", 10),
          ("emptyLocation", 2),
          ("esmBoard", 7),
          ("fcmBoard", 8),
          ("lmmBoard", 9),
          ("other", 1),
          ("tmmBoard", 12),
          ("trsmBoard", 11))
    )


_LpsSlotBoardType_Type.__name__ = "Integer32"
_LpsSlotBoardType_Object = MibTableColumn
lpsSlotBoardType = _LpsSlotBoardType_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 2, 2, 1, 2),
    _LpsSlotBoardType_Type()
)
lpsSlotBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsSlotBoardType.setStatus("mandatory")


class _LpsSlotBoardRevision_Type(OctetString):
    """Custom type lpsSlotBoardRevision based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_LpsSlotBoardRevision_Type.__name__ = "OctetString"
_LpsSlotBoardRevision_Object = MibTableColumn
lpsSlotBoardRevision = _LpsSlotBoardRevision_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 2, 2, 1, 3),
    _LpsSlotBoardRevision_Type()
)
lpsSlotBoardRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsSlotBoardRevision.setStatus("mandatory")


class _LpsSlotBoardStatus_Type(Integer32):
    """Custom type lpsSlotBoardStatus based on Integer32"""
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
        *(("notPresent", 1),
          ("offline", 3),
          ("online", 4),
          ("testing", 2))
    )


_LpsSlotBoardStatus_Type.__name__ = "Integer32"
_LpsSlotBoardStatus_Object = MibTableColumn
lpsSlotBoardStatus = _LpsSlotBoardStatus_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 2, 2, 1, 4),
    _LpsSlotBoardStatus_Type()
)
lpsSlotBoardStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsSlotBoardStatus.setStatus("mandatory")


class _LpsSlotBoardName_Type(DisplayString):
    """Custom type lpsSlotBoardName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LpsSlotBoardName_Type.__name__ = "DisplayString"
_LpsSlotBoardName_Object = MibTableColumn
lpsSlotBoardName = _LpsSlotBoardName_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 2, 2, 1, 5),
    _LpsSlotBoardName_Type()
)
lpsSlotBoardName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsSlotBoardName.setStatus("mandatory")


class _LpsSlotBoardNameAbbrev_Type(DisplayString):
    """Custom type lpsSlotBoardNameAbbrev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_LpsSlotBoardNameAbbrev_Type.__name__ = "DisplayString"
_LpsSlotBoardNameAbbrev_Object = MibTableColumn
lpsSlotBoardNameAbbrev = _LpsSlotBoardNameAbbrev_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 2, 2, 1, 6),
    _LpsSlotBoardNameAbbrev_Type()
)
lpsSlotBoardNameAbbrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsSlotBoardNameAbbrev.setStatus("mandatory")
_LpsSlotEthernetPortCount_Type = Integer32
_LpsSlotEthernetPortCount_Object = MibTableColumn
lpsSlotEthernetPortCount = _LpsSlotEthernetPortCount_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 2, 2, 1, 7),
    _LpsSlotEthernetPortCount_Type()
)
lpsSlotEthernetPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsSlotEthernetPortCount.setStatus("mandatory")
_LpsSlotFddiMacCount_Type = Integer32
_LpsSlotFddiMacCount_Object = MibTableColumn
lpsSlotFddiMacCount = _LpsSlotFddiMacCount_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 2, 2, 1, 8),
    _LpsSlotFddiMacCount_Type()
)
lpsSlotFddiMacCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsSlotFddiMacCount.setStatus("mandatory")
_LpsSlotFddiPortCount_Type = Integer32
_LpsSlotFddiPortCount_Object = MibTableColumn
lpsSlotFddiPortCount = _LpsSlotFddiPortCount_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 2, 2, 1, 9),
    _LpsSlotFddiPortCount_Type()
)
lpsSlotFddiPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsSlotFddiPortCount.setStatus("mandatory")


class _LpsSlotOvertemperature_Type(Integer32):
    """Custom type lpsSlotOvertemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("notSupported", 3),
          ("true", 1))
    )


_LpsSlotOvertemperature_Type.__name__ = "Integer32"
_LpsSlotOvertemperature_Object = MibTableColumn
lpsSlotOvertemperature = _LpsSlotOvertemperature_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 2, 2, 1, 10),
    _LpsSlotOvertemperature_Type()
)
lpsSlotOvertemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsSlotOvertemperature.setStatus("mandatory")
_LpsSlotTokenRingPortCount_Type = Integer32
_LpsSlotTokenRingPortCount_Object = MibTableColumn
lpsSlotTokenRingPortCount = _LpsSlotTokenRingPortCount_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 2, 2, 1, 11),
    _LpsSlotTokenRingPortCount_Type()
)
lpsSlotTokenRingPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsSlotTokenRingPortCount.setStatus("mandatory")
_LpsControlPanel_ObjectIdentity = ObjectIdentity
lpsControlPanel = _LpsControlPanel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 3)
)


class _LpsControlPanelHardwareRevision_Type(OctetString):
    """Custom type lpsControlPanelHardwareRevision based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpsControlPanelHardwareRevision_Type.__name__ = "OctetString"
_LpsControlPanelHardwareRevision_Object = MibScalar
lpsControlPanelHardwareRevision = _LpsControlPanelHardwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 3, 1),
    _LpsControlPanelHardwareRevision_Type()
)
lpsControlPanelHardwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsControlPanelHardwareRevision.setStatus("mandatory")


class _LpsControlPanelSoftwareRevision_Type(OctetString):
    """Custom type lpsControlPanelSoftwareRevision based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpsControlPanelSoftwareRevision_Type.__name__ = "OctetString"
_LpsControlPanelSoftwareRevision_Object = MibScalar
lpsControlPanelSoftwareRevision = _LpsControlPanelSoftwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 3, 2),
    _LpsControlPanelSoftwareRevision_Type()
)
lpsControlPanelSoftwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsControlPanelSoftwareRevision.setStatus("mandatory")
_LpsControlPanelLines_Type = Integer32
_LpsControlPanelLines_Object = MibScalar
lpsControlPanelLines = _LpsControlPanelLines_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 3, 3),
    _LpsControlPanelLines_Type()
)
lpsControlPanelLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsControlPanelLines.setStatus("mandatory")
_LpsControlPanelColumns_Type = Integer32
_LpsControlPanelColumns_Object = MibScalar
lpsControlPanelColumns = _LpsControlPanelColumns_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 3, 4),
    _LpsControlPanelColumns_Type()
)
lpsControlPanelColumns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsControlPanelColumns.setStatus("mandatory")


class _LpsControlPanelText_Type(OctetString):
    """Custom type lpsControlPanelText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_LpsControlPanelText_Type.__name__ = "OctetString"
_LpsControlPanelText_Object = MibScalar
lpsControlPanelText = _LpsControlPanelText_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 3, 5),
    _LpsControlPanelText_Type()
)
lpsControlPanelText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsControlPanelText.setStatus("mandatory")
_LpsPowerSupply_ObjectIdentity = ObjectIdentity
lpsPowerSupply = _LpsPowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 4)
)
_LpsPowerSupplyCount_Type = Integer32
_LpsPowerSupplyCount_Object = MibScalar
lpsPowerSupplyCount = _LpsPowerSupplyCount_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 4, 1),
    _LpsPowerSupplyCount_Type()
)
lpsPowerSupplyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsPowerSupplyCount.setStatus("mandatory")
_LpsPowerSupplyStatusTable_Object = MibTable
lpsPowerSupplyStatusTable = _LpsPowerSupplyStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 4, 2)
)
if mibBuilder.loadTexts:
    lpsPowerSupplyStatusTable.setStatus("mandatory")
_LpsPowerSupplyStatusEntry_Object = MibTableRow
lpsPowerSupplyStatusEntry = _LpsPowerSupplyStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 4, 2, 1)
)
lpsPowerSupplyStatusEntry.setIndexNames(
    (0, "LANPLEX-SYSTEMS-MIB-1-2-2", "lpsPowerSupplyStatusIndex"),
)
if mibBuilder.loadTexts:
    lpsPowerSupplyStatusEntry.setStatus("mandatory")
_LpsPowerSupplyStatusIndex_Type = Integer32
_LpsPowerSupplyStatusIndex_Object = MibTableColumn
lpsPowerSupplyStatusIndex = _LpsPowerSupplyStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 4, 2, 1, 1),
    _LpsPowerSupplyStatusIndex_Type()
)
lpsPowerSupplyStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsPowerSupplyStatusIndex.setStatus("mandatory")
_LpsPowerSupplyStatus_Type = Integer32
_LpsPowerSupplyStatus_Object = MibTableColumn
lpsPowerSupplyStatus = _LpsPowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 4, 2, 1, 2),
    _LpsPowerSupplyStatus_Type()
)
lpsPowerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsPowerSupplyStatus.setStatus("mandatory")
_LpsPowerSupplyStatusSupported_Type = Integer32
_LpsPowerSupplyStatusSupported_Object = MibTableColumn
lpsPowerSupplyStatusSupported = _LpsPowerSupplyStatusSupported_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 4, 2, 1, 3),
    _LpsPowerSupplyStatusSupported_Type()
)
lpsPowerSupplyStatusSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsPowerSupplyStatusSupported.setStatus("mandatory")
_LpsSnmp_ObjectIdentity = ObjectIdentity
lpsSnmp = _LpsSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 5)
)
_LpsSnmpAgentId_Type = Integer32
_LpsSnmpAgentId_Object = MibScalar
lpsSnmpAgentId = _LpsSnmpAgentId_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 5, 1),
    _LpsSnmpAgentId_Type()
)
lpsSnmpAgentId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsSnmpAgentId.setStatus("mandatory")


class _LpsSnmpInternalAgentTrapMask_Type(OctetString):
    """Custom type lpsSnmpInternalAgentTrapMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_LpsSnmpInternalAgentTrapMask_Type.__name__ = "OctetString"
_LpsSnmpInternalAgentTrapMask_Object = MibScalar
lpsSnmpInternalAgentTrapMask = _LpsSnmpInternalAgentTrapMask_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 5, 2),
    _LpsSnmpInternalAgentTrapMask_Type()
)
lpsSnmpInternalAgentTrapMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpsSnmpInternalAgentTrapMask.setStatus("mandatory")
_LpsSnmpInternalAgentTrapDestinationMask_Type = Integer32
_LpsSnmpInternalAgentTrapDestinationMask_Object = MibScalar
lpsSnmpInternalAgentTrapDestinationMask = _LpsSnmpInternalAgentTrapDestinationMask_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 5, 3),
    _LpsSnmpInternalAgentTrapDestinationMask_Type()
)
lpsSnmpInternalAgentTrapDestinationMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpsSnmpInternalAgentTrapDestinationMask.setStatus("mandatory")


class _LpsSnmpProxyInternalRequests_Type(Integer32):
    """Custom type lpsSnmpProxyInternalRequests based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_LpsSnmpProxyInternalRequests_Type.__name__ = "Integer32"
_LpsSnmpProxyInternalRequests_Object = MibScalar
lpsSnmpProxyInternalRequests = _LpsSnmpProxyInternalRequests_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 5, 4),
    _LpsSnmpProxyInternalRequests_Type()
)
lpsSnmpProxyInternalRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpsSnmpProxyInternalRequests.setStatus("deprecated")


class _LpsSnmpInternalProxyRequestMaxAge_Type(Integer32):
    """Custom type lpsSnmpInternalProxyRequestMaxAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_LpsSnmpInternalProxyRequestMaxAge_Type.__name__ = "Integer32"
_LpsSnmpInternalProxyRequestMaxAge_Object = MibScalar
lpsSnmpInternalProxyRequestMaxAge = _LpsSnmpInternalProxyRequestMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 5, 5),
    _LpsSnmpInternalProxyRequestMaxAge_Type()
)
lpsSnmpInternalProxyRequestMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpsSnmpInternalProxyRequestMaxAge.setStatus("mandatory")


class _LpsSnmpProxyInternalTraps_Type(Integer32):
    """Custom type lpsSnmpProxyInternalTraps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_LpsSnmpProxyInternalTraps_Type.__name__ = "Integer32"
_LpsSnmpProxyInternalTraps_Object = MibScalar
lpsSnmpProxyInternalTraps = _LpsSnmpProxyInternalTraps_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 5, 6),
    _LpsSnmpProxyInternalTraps_Type()
)
lpsSnmpProxyInternalTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpsSnmpProxyInternalTraps.setStatus("deprecated")
_LpsSnmpInternalProxyTable_Object = MibTable
lpsSnmpInternalProxyTable = _LpsSnmpInternalProxyTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 5, 7)
)
if mibBuilder.loadTexts:
    lpsSnmpInternalProxyTable.setStatus("mandatory")
_LpsSnmpInternalProxyEntry_Object = MibTableRow
lpsSnmpInternalProxyEntry = _LpsSnmpInternalProxyEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 5, 7, 1)
)
lpsSnmpInternalProxyEntry.setIndexNames(
    (0, "LANPLEX-SYSTEMS-MIB-1-2-2", "lpsSnmpInternalProxyAgentId"),
    (0, "LANPLEX-SYSTEMS-MIB-1-2-2", "lpsSnmpInternalProxyAccessClass"),
)
if mibBuilder.loadTexts:
    lpsSnmpInternalProxyEntry.setStatus("mandatory")
_LpsSnmpInternalProxyAgentId_Type = Integer32
_LpsSnmpInternalProxyAgentId_Object = MibTableColumn
lpsSnmpInternalProxyAgentId = _LpsSnmpInternalProxyAgentId_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 5, 7, 1, 1),
    _LpsSnmpInternalProxyAgentId_Type()
)
lpsSnmpInternalProxyAgentId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsSnmpInternalProxyAgentId.setStatus("mandatory")


class _LpsSnmpInternalProxyAccessClass_Type(Integer32):
    """Custom type lpsSnmpInternalProxyAccessClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("readOnly", 1),
          ("readWrite", 2))
    )


_LpsSnmpInternalProxyAccessClass_Type.__name__ = "Integer32"
_LpsSnmpInternalProxyAccessClass_Object = MibTableColumn
lpsSnmpInternalProxyAccessClass = _LpsSnmpInternalProxyAccessClass_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 5, 7, 1, 2),
    _LpsSnmpInternalProxyAccessClass_Type()
)
lpsSnmpInternalProxyAccessClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsSnmpInternalProxyAccessClass.setStatus("mandatory")
_LpsSnmpInternalProxyCommunity_Type = OctetString
_LpsSnmpInternalProxyCommunity_Object = MibTableColumn
lpsSnmpInternalProxyCommunity = _LpsSnmpInternalProxyCommunity_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 5, 7, 1, 3),
    _LpsSnmpInternalProxyCommunity_Type()
)
lpsSnmpInternalProxyCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsSnmpInternalProxyCommunity.setStatus("mandatory")
_LpsAgent_ObjectIdentity = ObjectIdentity
lpsAgent = _LpsAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 6)
)


class _LpsAgentRequestMaxAge_Type(Integer32):
    """Custom type lpsAgentRequestMaxAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_LpsAgentRequestMaxAge_Type.__name__ = "Integer32"
_LpsAgentRequestMaxAge_Object = MibScalar
lpsAgentRequestMaxAge = _LpsAgentRequestMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 6, 1),
    _LpsAgentRequestMaxAge_Type()
)
lpsAgentRequestMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpsAgentRequestMaxAge.setStatus("mandatory")


class _LpsAgentProxyRemoteSmtRequests_Type(Integer32):
    """Custom type lpsAgentProxyRemoteSmtRequests based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_LpsAgentProxyRemoteSmtRequests_Type.__name__ = "Integer32"
_LpsAgentProxyRemoteSmtRequests_Object = MibScalar
lpsAgentProxyRemoteSmtRequests = _LpsAgentProxyRemoteSmtRequests_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 6, 2),
    _LpsAgentProxyRemoteSmtRequests_Type()
)
lpsAgentProxyRemoteSmtRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpsAgentProxyRemoteSmtRequests.setStatus("deprecated")


class _LpsAgentRemoteSmtProxyRequestMaxAge_Type(Integer32):
    """Custom type lpsAgentRemoteSmtProxyRequestMaxAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_LpsAgentRemoteSmtProxyRequestMaxAge_Type.__name__ = "Integer32"
_LpsAgentRemoteSmtProxyRequestMaxAge_Object = MibScalar
lpsAgentRemoteSmtProxyRequestMaxAge = _LpsAgentRemoteSmtProxyRequestMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 6, 3),
    _LpsAgentRemoteSmtProxyRequestMaxAge_Type()
)
lpsAgentRemoteSmtProxyRequestMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpsAgentRemoteSmtProxyRequestMaxAge.setStatus("mandatory")


class _LpsAgentProxyRemoteSmtEvents_Type(Integer32):
    """Custom type lpsAgentProxyRemoteSmtEvents based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_LpsAgentProxyRemoteSmtEvents_Type.__name__ = "Integer32"
_LpsAgentProxyRemoteSmtEvents_Object = MibScalar
lpsAgentProxyRemoteSmtEvents = _LpsAgentProxyRemoteSmtEvents_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 6, 4),
    _LpsAgentProxyRemoteSmtEvents_Type()
)
lpsAgentProxyRemoteSmtEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpsAgentProxyRemoteSmtEvents.setStatus("mandatory")
_LpsAgentTrapDescriptionTable_Object = MibTable
lpsAgentTrapDescriptionTable = _LpsAgentTrapDescriptionTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 6, 5)
)
if mibBuilder.loadTexts:
    lpsAgentTrapDescriptionTable.setStatus("mandatory")
_LpsAgentTrapDescriptionTableEntry_Object = MibTableRow
lpsAgentTrapDescriptionTableEntry = _LpsAgentTrapDescriptionTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 6, 5, 1)
)
lpsAgentTrapDescriptionTableEntry.setIndexNames(
    (0, "LANPLEX-SYSTEMS-MIB-1-2-2", "lpsAgentTrapDescriptionIndex"),
)
if mibBuilder.loadTexts:
    lpsAgentTrapDescriptionTableEntry.setStatus("mandatory")
_LpsAgentTrapDescriptionIndex_Type = Integer32
_LpsAgentTrapDescriptionIndex_Object = MibTableColumn
lpsAgentTrapDescriptionIndex = _LpsAgentTrapDescriptionIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 6, 5, 1, 1),
    _LpsAgentTrapDescriptionIndex_Type()
)
lpsAgentTrapDescriptionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsAgentTrapDescriptionIndex.setStatus("mandatory")
_LpsAgentTrapEnterprise_Type = ObjectIdentifier
_LpsAgentTrapEnterprise_Object = MibTableColumn
lpsAgentTrapEnterprise = _LpsAgentTrapEnterprise_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 6, 5, 1, 2),
    _LpsAgentTrapEnterprise_Type()
)
lpsAgentTrapEnterprise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsAgentTrapEnterprise.setStatus("mandatory")
_LpsAgentTrapNumber_Type = Integer32
_LpsAgentTrapNumber_Object = MibTableColumn
lpsAgentTrapNumber = _LpsAgentTrapNumber_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 6, 5, 1, 3),
    _LpsAgentTrapNumber_Type()
)
lpsAgentTrapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsAgentTrapNumber.setStatus("mandatory")
_LpsAgentTrapDestinationTable_Object = MibTable
lpsAgentTrapDestinationTable = _LpsAgentTrapDestinationTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 6, 6)
)
if mibBuilder.loadTexts:
    lpsAgentTrapDestinationTable.setStatus("mandatory")
_LpsAgentTrapDestinationTableEntry_Object = MibTableRow
lpsAgentTrapDestinationTableEntry = _LpsAgentTrapDestinationTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 6, 6, 1)
)
lpsAgentTrapDestinationTableEntry.setIndexNames(
    (0, "LANPLEX-SYSTEMS-MIB-1-2-2", "lpsAgentTrapDestinationAddressType"),
    (0, "LANPLEX-SYSTEMS-MIB-1-2-2", "lpsAgentTrapDestinationAddress"),
)
if mibBuilder.loadTexts:
    lpsAgentTrapDestinationTableEntry.setStatus("mandatory")


class _LpsAgentTrapDestinationAddressType_Type(Integer32):
    """Custom type lpsAgentTrapDestinationAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ip", 1)
    )


_LpsAgentTrapDestinationAddressType_Type.__name__ = "Integer32"
_LpsAgentTrapDestinationAddressType_Object = MibTableColumn
lpsAgentTrapDestinationAddressType = _LpsAgentTrapDestinationAddressType_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 6, 6, 1, 1),
    _LpsAgentTrapDestinationAddressType_Type()
)
lpsAgentTrapDestinationAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsAgentTrapDestinationAddressType.setStatus("mandatory")
_LpsAgentTrapDestinationAddress_Type = OctetString
_LpsAgentTrapDestinationAddress_Object = MibTableColumn
lpsAgentTrapDestinationAddress = _LpsAgentTrapDestinationAddress_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 6, 6, 1, 2),
    _LpsAgentTrapDestinationAddress_Type()
)
lpsAgentTrapDestinationAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsAgentTrapDestinationAddress.setStatus("mandatory")


class _LpsAgentTrapDestinationTrapMask_Type(OctetString):
    """Custom type lpsAgentTrapDestinationTrapMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_LpsAgentTrapDestinationTrapMask_Type.__name__ = "OctetString"
_LpsAgentTrapDestinationTrapMask_Object = MibTableColumn
lpsAgentTrapDestinationTrapMask = _LpsAgentTrapDestinationTrapMask_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 6, 6, 1, 3),
    _LpsAgentTrapDestinationTrapMask_Type()
)
lpsAgentTrapDestinationTrapMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpsAgentTrapDestinationTrapMask.setStatus("mandatory")


class _LpsAgentTrapDestinationEntryStatus_Type(Integer32):
    """Custom type lpsAgentTrapDestinationEntryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_LpsAgentTrapDestinationEntryStatus_Type.__name__ = "Integer32"
_LpsAgentTrapDestinationEntryStatus_Object = MibTableColumn
lpsAgentTrapDestinationEntryStatus = _LpsAgentTrapDestinationEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 6, 6, 1, 4),
    _LpsAgentTrapDestinationEntryStatus_Type()
)
lpsAgentTrapDestinationEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpsAgentTrapDestinationEntryStatus.setStatus("mandatory")
_LpsInterface_ObjectIdentity = ObjectIdentity
lpsInterface = _LpsInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 7)
)
_LpsInterfaceLocationTable_Object = MibTable
lpsInterfaceLocationTable = _LpsInterfaceLocationTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 7, 1)
)
if mibBuilder.loadTexts:
    lpsInterfaceLocationTable.setStatus("mandatory")
_LpsInterfaceLocationEntry_Object = MibTableRow
lpsInterfaceLocationEntry = _LpsInterfaceLocationEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 7, 1, 1)
)
lpsInterfaceLocationEntry.setIndexNames(
    (0, "LANPLEX-SYSTEMS-MIB-1-2-2", "lpsInterfaceLocationIfIndex"),
)
if mibBuilder.loadTexts:
    lpsInterfaceLocationEntry.setStatus("mandatory")
_LpsInterfaceLocationIfIndex_Type = Integer32
_LpsInterfaceLocationIfIndex_Object = MibTableColumn
lpsInterfaceLocationIfIndex = _LpsInterfaceLocationIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 7, 1, 1, 1),
    _LpsInterfaceLocationIfIndex_Type()
)
lpsInterfaceLocationIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsInterfaceLocationIfIndex.setStatus("mandatory")


class _LpsInterfaceLocationInterfaceType_Type(Integer32):
    """Custom type lpsInterfaceLocationInterfaceType based on Integer32"""
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
        *(("ethernetPort", 2),
          ("fddiMac", 3),
          ("other", 1),
          ("tokenringPort", 4))
    )


_LpsInterfaceLocationInterfaceType_Type.__name__ = "Integer32"
_LpsInterfaceLocationInterfaceType_Object = MibTableColumn
lpsInterfaceLocationInterfaceType = _LpsInterfaceLocationInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 7, 1, 1, 2),
    _LpsInterfaceLocationInterfaceType_Type()
)
lpsInterfaceLocationInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsInterfaceLocationInterfaceType.setStatus("mandatory")


class _LpsInterfaceLocationType_Type(Integer32):
    """Custom type lpsInterfaceLocationType based on Integer32"""
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
        *(("chassis", 3),
          ("modularCard", 4),
          ("modularSlot", 2),
          ("other", 1))
    )


_LpsInterfaceLocationType_Type.__name__ = "Integer32"
_LpsInterfaceLocationType_Object = MibTableColumn
lpsInterfaceLocationType = _LpsInterfaceLocationType_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 7, 1, 1, 3),
    _LpsInterfaceLocationType_Type()
)
lpsInterfaceLocationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsInterfaceLocationType.setStatus("mandatory")
_LpsInterfaceLocationTypeIndex_Type = Integer32
_LpsInterfaceLocationTypeIndex_Object = MibTableColumn
lpsInterfaceLocationTypeIndex = _LpsInterfaceLocationTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 7, 1, 1, 4),
    _LpsInterfaceLocationTypeIndex_Type()
)
lpsInterfaceLocationTypeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsInterfaceLocationTypeIndex.setStatus("mandatory")
_LpsInterfaceLocationLocalIndex_Type = Integer32
_LpsInterfaceLocationLocalIndex_Object = MibTableColumn
lpsInterfaceLocationLocalIndex = _LpsInterfaceLocationLocalIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 7, 1, 1, 5),
    _LpsInterfaceLocationLocalIndex_Type()
)
lpsInterfaceLocationLocalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsInterfaceLocationLocalIndex.setStatus("mandatory")
_LpsEthernetPort_ObjectIdentity = ObjectIdentity
lpsEthernetPort = _LpsEthernetPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 8)
)
_LpsEthernetPortCount_Type = Integer32
_LpsEthernetPortCount_Object = MibScalar
lpsEthernetPortCount = _LpsEthernetPortCount_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 8, 1),
    _LpsEthernetPortCount_Type()
)
lpsEthernetPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsEthernetPortCount.setStatus("mandatory")
_LpsEthernetPortTable_Object = MibTable
lpsEthernetPortTable = _LpsEthernetPortTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 8, 2)
)
if mibBuilder.loadTexts:
    lpsEthernetPortTable.setStatus("mandatory")
_LpsEthernetPortEntry_Object = MibTableRow
lpsEthernetPortEntry = _LpsEthernetPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 8, 2, 1)
)
lpsEthernetPortEntry.setIndexNames(
    (0, "LANPLEX-SYSTEMS-MIB-1-2-2", "lpsEthernetPortIndex"),
)
if mibBuilder.loadTexts:
    lpsEthernetPortEntry.setStatus("mandatory")
_LpsEthernetPortIndex_Type = Integer32
_LpsEthernetPortIndex_Object = MibTableColumn
lpsEthernetPortIndex = _LpsEthernetPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 8, 2, 1, 1),
    _LpsEthernetPortIndex_Type()
)
lpsEthernetPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsEthernetPortIndex.setStatus("mandatory")
_LpsEthernetPortIfIndex_Type = Integer32
_LpsEthernetPortIfIndex_Object = MibTableColumn
lpsEthernetPortIfIndex = _LpsEthernetPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 8, 2, 1, 2),
    _LpsEthernetPortIfIndex_Type()
)
lpsEthernetPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsEthernetPortIfIndex.setStatus("mandatory")


class _LpsEthernetPortLabel_Type(DisplayString):
    """Custom type lpsEthernetPortLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_LpsEthernetPortLabel_Type.__name__ = "DisplayString"
_LpsEthernetPortLabel_Object = MibTableColumn
lpsEthernetPortLabel = _LpsEthernetPortLabel_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 8, 2, 1, 3),
    _LpsEthernetPortLabel_Type()
)
lpsEthernetPortLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpsEthernetPortLabel.setStatus("mandatory")


class _LpsEthernetPortLinkStatus_Type(Integer32):
    """Custom type lpsEthernetPortLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inActive", 2))
    )


_LpsEthernetPortLinkStatus_Type.__name__ = "Integer32"
_LpsEthernetPortLinkStatus_Object = MibTableColumn
lpsEthernetPortLinkStatus = _LpsEthernetPortLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 8, 2, 1, 4),
    _LpsEthernetPortLinkStatus_Type()
)
lpsEthernetPortLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsEthernetPortLinkStatus.setStatus("mandatory")


class _LpsEthernetPortType_Type(Integer32):
    """Custom type lpsEthernetPortType based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("aui", 4),
          ("bnc10Base2", 5),
          ("other", 6),
          ("rj2110BaseT", 1),
          ("rj45100BaseT", 7),
          ("rj4510BaseT", 2),
          ("sc100BaseFx", 8),
          ("st10BaseFL", 3),
          ("untermBnc10Base2", 9))
    )


_LpsEthernetPortType_Type.__name__ = "Integer32"
_LpsEthernetPortType_Object = MibTableColumn
lpsEthernetPortType = _LpsEthernetPortType_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 8, 2, 1, 5),
    _LpsEthernetPortType_Type()
)
lpsEthernetPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsEthernetPortType.setStatus("mandatory")
_LpsEthernetPortRateTable_Object = MibTable
lpsEthernetPortRateTable = _LpsEthernetPortRateTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 8, 3)
)
if mibBuilder.loadTexts:
    lpsEthernetPortRateTable.setStatus("mandatory")
_LpsEthernetPortRateEntry_Object = MibTableRow
lpsEthernetPortRateEntry = _LpsEthernetPortRateEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 8, 3, 1)
)
lpsEthernetPortRateEntry.setIndexNames(
    (0, "LANPLEX-SYSTEMS-MIB-1-2-2", "lpsEthernetPortRateIndex"),
)
if mibBuilder.loadTexts:
    lpsEthernetPortRateEntry.setStatus("mandatory")
_LpsEthernetPortRateIndex_Type = Integer32
_LpsEthernetPortRateIndex_Object = MibTableColumn
lpsEthernetPortRateIndex = _LpsEthernetPortRateIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 8, 3, 1, 1),
    _LpsEthernetPortRateIndex_Type()
)
lpsEthernetPortRateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsEthernetPortRateIndex.setStatus("mandatory")
_LpsEthernetPortRateByteReceiveRate_Type = Integer32
_LpsEthernetPortRateByteReceiveRate_Object = MibTableColumn
lpsEthernetPortRateByteReceiveRate = _LpsEthernetPortRateByteReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 8, 3, 1, 2),
    _LpsEthernetPortRateByteReceiveRate_Type()
)
lpsEthernetPortRateByteReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsEthernetPortRateByteReceiveRate.setStatus("mandatory")
_LpsEthernetPortRatePeakByteReceiveRate_Type = Integer32
_LpsEthernetPortRatePeakByteReceiveRate_Object = MibTableColumn
lpsEthernetPortRatePeakByteReceiveRate = _LpsEthernetPortRatePeakByteReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 8, 3, 1, 3),
    _LpsEthernetPortRatePeakByteReceiveRate_Type()
)
lpsEthernetPortRatePeakByteReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsEthernetPortRatePeakByteReceiveRate.setStatus("mandatory")
_LpsEthernetPortRateFrameReceiveRate_Type = Integer32
_LpsEthernetPortRateFrameReceiveRate_Object = MibTableColumn
lpsEthernetPortRateFrameReceiveRate = _LpsEthernetPortRateFrameReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 8, 3, 1, 4),
    _LpsEthernetPortRateFrameReceiveRate_Type()
)
lpsEthernetPortRateFrameReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsEthernetPortRateFrameReceiveRate.setStatus("mandatory")
_LpsEthernetPortRatePeakFrameReceiveRate_Type = Integer32
_LpsEthernetPortRatePeakFrameReceiveRate_Object = MibTableColumn
lpsEthernetPortRatePeakFrameReceiveRate = _LpsEthernetPortRatePeakFrameReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 8, 3, 1, 5),
    _LpsEthernetPortRatePeakFrameReceiveRate_Type()
)
lpsEthernetPortRatePeakFrameReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsEthernetPortRatePeakFrameReceiveRate.setStatus("mandatory")
_LpsEthernetPortRateByteTransmitRate_Type = Integer32
_LpsEthernetPortRateByteTransmitRate_Object = MibTableColumn
lpsEthernetPortRateByteTransmitRate = _LpsEthernetPortRateByteTransmitRate_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 8, 3, 1, 6),
    _LpsEthernetPortRateByteTransmitRate_Type()
)
lpsEthernetPortRateByteTransmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsEthernetPortRateByteTransmitRate.setStatus("mandatory")
_LpsEthernetPortRatePeakByteTransmitRate_Type = Integer32
_LpsEthernetPortRatePeakByteTransmitRate_Object = MibTableColumn
lpsEthernetPortRatePeakByteTransmitRate = _LpsEthernetPortRatePeakByteTransmitRate_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 8, 3, 1, 7),
    _LpsEthernetPortRatePeakByteTransmitRate_Type()
)
lpsEthernetPortRatePeakByteTransmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsEthernetPortRatePeakByteTransmitRate.setStatus("mandatory")
_LpsEthernetPortRateFrameTransmitRate_Type = Integer32
_LpsEthernetPortRateFrameTransmitRate_Object = MibTableColumn
lpsEthernetPortRateFrameTransmitRate = _LpsEthernetPortRateFrameTransmitRate_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 8, 3, 1, 8),
    _LpsEthernetPortRateFrameTransmitRate_Type()
)
lpsEthernetPortRateFrameTransmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsEthernetPortRateFrameTransmitRate.setStatus("mandatory")
_LpsEthernetPortRatePeakFrameTransmitRate_Type = Integer32
_LpsEthernetPortRatePeakFrameTransmitRate_Object = MibTableColumn
lpsEthernetPortRatePeakFrameTransmitRate = _LpsEthernetPortRatePeakFrameTransmitRate_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 8, 3, 1, 9),
    _LpsEthernetPortRatePeakFrameTransmitRate_Type()
)
lpsEthernetPortRatePeakFrameTransmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsEthernetPortRatePeakFrameTransmitRate.setStatus("mandatory")
_LpsSmt_ObjectIdentity = ObjectIdentity
lpsSmt = _LpsSmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9)
)
_LpsSmtCount_Type = Integer32
_LpsSmtCount_Object = MibScalar
lpsSmtCount = _LpsSmtCount_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 1),
    _LpsSmtCount_Type()
)
lpsSmtCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsSmtCount.setStatus("mandatory")
_LpsSmtFddiMacBeaconTable_Object = MibTable
lpsSmtFddiMacBeaconTable = _LpsSmtFddiMacBeaconTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 4)
)
if mibBuilder.loadTexts:
    lpsSmtFddiMacBeaconTable.setStatus("mandatory")
_LpsSmtFddiMacBeaconEntry_Object = MibTableRow
lpsSmtFddiMacBeaconEntry = _LpsSmtFddiMacBeaconEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 4, 1)
)
lpsSmtFddiMacBeaconEntry.setIndexNames(
    (0, "LANPLEX-SYSTEMS-MIB-1-2-2", "lpsSmtFddiMacBeaconSmtIndex"),
    (0, "LANPLEX-SYSTEMS-MIB-1-2-2", "lpsSmtFddiMacBeaconIndex"),
)
if mibBuilder.loadTexts:
    lpsSmtFddiMacBeaconEntry.setStatus("mandatory")
_LpsSmtFddiMacBeaconSmtIndex_Type = Integer32
_LpsSmtFddiMacBeaconSmtIndex_Object = MibTableColumn
lpsSmtFddiMacBeaconSmtIndex = _LpsSmtFddiMacBeaconSmtIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 4, 1, 1),
    _LpsSmtFddiMacBeaconSmtIndex_Type()
)
lpsSmtFddiMacBeaconSmtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsSmtFddiMacBeaconSmtIndex.setStatus("mandatory")
_LpsSmtFddiMacBeaconIndex_Type = Integer32
_LpsSmtFddiMacBeaconIndex_Object = MibTableColumn
lpsSmtFddiMacBeaconIndex = _LpsSmtFddiMacBeaconIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 4, 1, 2),
    _LpsSmtFddiMacBeaconIndex_Type()
)
lpsSmtFddiMacBeaconIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsSmtFddiMacBeaconIndex.setStatus("mandatory")


class _LpsSmtFddiMacBeaconHistory_Type(OctetString):
    """Custom type lpsSmtFddiMacBeaconHistory based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_LpsSmtFddiMacBeaconHistory_Type.__name__ = "OctetString"
_LpsSmtFddiMacBeaconHistory_Object = MibTableColumn
lpsSmtFddiMacBeaconHistory = _LpsSmtFddiMacBeaconHistory_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 4, 1, 3),
    _LpsSmtFddiMacBeaconHistory_Type()
)
lpsSmtFddiMacBeaconHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsSmtFddiMacBeaconHistory.setStatus("mandatory")
_LpsSmtFddiMacRateTable_Object = MibTable
lpsSmtFddiMacRateTable = _LpsSmtFddiMacRateTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 5)
)
if mibBuilder.loadTexts:
    lpsSmtFddiMacRateTable.setStatus("mandatory")
_LpsSmtFddiMacRateEntry_Object = MibTableRow
lpsSmtFddiMacRateEntry = _LpsSmtFddiMacRateEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 5, 1)
)
lpsSmtFddiMacRateEntry.setIndexNames(
    (0, "LANPLEX-SYSTEMS-MIB-1-2-2", "lpsSmtFddiMacRateSmtIndex"),
    (0, "LANPLEX-SYSTEMS-MIB-1-2-2", "lpsSmtFddiMacRateIndex"),
)
if mibBuilder.loadTexts:
    lpsSmtFddiMacRateEntry.setStatus("mandatory")
_LpsSmtFddiMacRateSmtIndex_Type = Integer32
_LpsSmtFddiMacRateSmtIndex_Object = MibTableColumn
lpsSmtFddiMacRateSmtIndex = _LpsSmtFddiMacRateSmtIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 5, 1, 1),
    _LpsSmtFddiMacRateSmtIndex_Type()
)
lpsSmtFddiMacRateSmtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsSmtFddiMacRateSmtIndex.setStatus("mandatory")
_LpsSmtFddiMacRateIndex_Type = Integer32
_LpsSmtFddiMacRateIndex_Object = MibTableColumn
lpsSmtFddiMacRateIndex = _LpsSmtFddiMacRateIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 5, 1, 2),
    _LpsSmtFddiMacRateIndex_Type()
)
lpsSmtFddiMacRateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsSmtFddiMacRateIndex.setStatus("mandatory")
_LpsSmtFddiMacRateByteReceiveRate_Type = Integer32
_LpsSmtFddiMacRateByteReceiveRate_Object = MibTableColumn
lpsSmtFddiMacRateByteReceiveRate = _LpsSmtFddiMacRateByteReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 5, 1, 3),
    _LpsSmtFddiMacRateByteReceiveRate_Type()
)
lpsSmtFddiMacRateByteReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsSmtFddiMacRateByteReceiveRate.setStatus("mandatory")
_LpsSmtFddiMacRatePeakByteReceiveRate_Type = Integer32
_LpsSmtFddiMacRatePeakByteReceiveRate_Object = MibTableColumn
lpsSmtFddiMacRatePeakByteReceiveRate = _LpsSmtFddiMacRatePeakByteReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 5, 1, 4),
    _LpsSmtFddiMacRatePeakByteReceiveRate_Type()
)
lpsSmtFddiMacRatePeakByteReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsSmtFddiMacRatePeakByteReceiveRate.setStatus("mandatory")
_LpsSmtFddiMacRateFrameReceiveRate_Type = Integer32
_LpsSmtFddiMacRateFrameReceiveRate_Object = MibTableColumn
lpsSmtFddiMacRateFrameReceiveRate = _LpsSmtFddiMacRateFrameReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 5, 1, 5),
    _LpsSmtFddiMacRateFrameReceiveRate_Type()
)
lpsSmtFddiMacRateFrameReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsSmtFddiMacRateFrameReceiveRate.setStatus("mandatory")
_LpsSmtFddiMacRatePeakFrameReceiveRate_Type = Integer32
_LpsSmtFddiMacRatePeakFrameReceiveRate_Object = MibTableColumn
lpsSmtFddiMacRatePeakFrameReceiveRate = _LpsSmtFddiMacRatePeakFrameReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 5, 1, 6),
    _LpsSmtFddiMacRatePeakFrameReceiveRate_Type()
)
lpsSmtFddiMacRatePeakFrameReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsSmtFddiMacRatePeakFrameReceiveRate.setStatus("mandatory")
_LpsSmtFddiMacRateByteTransmitRate_Type = Integer32
_LpsSmtFddiMacRateByteTransmitRate_Object = MibTableColumn
lpsSmtFddiMacRateByteTransmitRate = _LpsSmtFddiMacRateByteTransmitRate_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 5, 1, 7),
    _LpsSmtFddiMacRateByteTransmitRate_Type()
)
lpsSmtFddiMacRateByteTransmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsSmtFddiMacRateByteTransmitRate.setStatus("mandatory")
_LpsSmtFddiMacRatePeakByteTransmitRate_Type = Integer32
_LpsSmtFddiMacRatePeakByteTransmitRate_Object = MibTableColumn
lpsSmtFddiMacRatePeakByteTransmitRate = _LpsSmtFddiMacRatePeakByteTransmitRate_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 5, 1, 8),
    _LpsSmtFddiMacRatePeakByteTransmitRate_Type()
)
lpsSmtFddiMacRatePeakByteTransmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsSmtFddiMacRatePeakByteTransmitRate.setStatus("mandatory")
_LpsSmtFddiMacRateFrameTransmitRate_Type = Integer32
_LpsSmtFddiMacRateFrameTransmitRate_Object = MibTableColumn
lpsSmtFddiMacRateFrameTransmitRate = _LpsSmtFddiMacRateFrameTransmitRate_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 5, 1, 9),
    _LpsSmtFddiMacRateFrameTransmitRate_Type()
)
lpsSmtFddiMacRateFrameTransmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsSmtFddiMacRateFrameTransmitRate.setStatus("mandatory")
_LpsSmtFddiMacRatePeakFrameTransmitRate_Type = Integer32
_LpsSmtFddiMacRatePeakFrameTransmitRate_Object = MibTableColumn
lpsSmtFddiMacRatePeakFrameTransmitRate = _LpsSmtFddiMacRatePeakFrameTransmitRate_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 5, 1, 10),
    _LpsSmtFddiMacRatePeakFrameTransmitRate_Type()
)
lpsSmtFddiMacRatePeakFrameTransmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsSmtFddiMacRatePeakFrameTransmitRate.setStatus("mandatory")
_LpsSmtFddiPortTable_Object = MibTable
lpsSmtFddiPortTable = _LpsSmtFddiPortTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 6)
)
if mibBuilder.loadTexts:
    lpsSmtFddiPortTable.setStatus("mandatory")
_LpsSmtFddiPortEntry_Object = MibTableRow
lpsSmtFddiPortEntry = _LpsSmtFddiPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 6, 1)
)
lpsSmtFddiPortEntry.setIndexNames(
    (0, "LANPLEX-SYSTEMS-MIB-1-2-2", "lpsSmtFddiPortSmtIndex"),
    (0, "LANPLEX-SYSTEMS-MIB-1-2-2", "lpsSmtFddiPortIndex"),
)
if mibBuilder.loadTexts:
    lpsSmtFddiPortEntry.setStatus("mandatory")
_LpsSmtFddiPortSmtIndex_Type = Integer32
_LpsSmtFddiPortSmtIndex_Object = MibTableColumn
lpsSmtFddiPortSmtIndex = _LpsSmtFddiPortSmtIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 6, 1, 1),
    _LpsSmtFddiPortSmtIndex_Type()
)
lpsSmtFddiPortSmtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsSmtFddiPortSmtIndex.setStatus("mandatory")
_LpsSmtFddiPortIndex_Type = Integer32
_LpsSmtFddiPortIndex_Object = MibTableColumn
lpsSmtFddiPortIndex = _LpsSmtFddiPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 6, 1, 2),
    _LpsSmtFddiPortIndex_Type()
)
lpsSmtFddiPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsSmtFddiPortIndex.setStatus("mandatory")


class _LpsSmtFddiPortLocationType_Type(Integer32):
    """Custom type lpsSmtFddiPortLocationType based on Integer32"""
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
        *(("chassis", 3),
          ("modularCard", 4),
          ("modularSlot", 2),
          ("other", 1))
    )


_LpsSmtFddiPortLocationType_Type.__name__ = "Integer32"
_LpsSmtFddiPortLocationType_Object = MibTableColumn
lpsSmtFddiPortLocationType = _LpsSmtFddiPortLocationType_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 6, 1, 3),
    _LpsSmtFddiPortLocationType_Type()
)
lpsSmtFddiPortLocationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsSmtFddiPortLocationType.setStatus("mandatory")
_LpsSmtFddiPortLocationTypeIndex_Type = Integer32
_LpsSmtFddiPortLocationTypeIndex_Object = MibTableColumn
lpsSmtFddiPortLocationTypeIndex = _LpsSmtFddiPortLocationTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 6, 1, 4),
    _LpsSmtFddiPortLocationTypeIndex_Type()
)
lpsSmtFddiPortLocationTypeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsSmtFddiPortLocationTypeIndex.setStatus("mandatory")
_LpsSmtFddiPortLocationLocalIndex_Type = Integer32
_LpsSmtFddiPortLocationLocalIndex_Object = MibTableColumn
lpsSmtFddiPortLocationLocalIndex = _LpsSmtFddiPortLocationLocalIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 6, 1, 5),
    _LpsSmtFddiPortLocationLocalIndex_Type()
)
lpsSmtFddiPortLocationLocalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsSmtFddiPortLocationLocalIndex.setStatus("mandatory")


class _LpsSmtFddiPortLabel_Type(DisplayString):
    """Custom type lpsSmtFddiPortLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_LpsSmtFddiPortLabel_Type.__name__ = "DisplayString"
_LpsSmtFddiPortLabel_Object = MibTableColumn
lpsSmtFddiPortLabel = _LpsSmtFddiPortLabel_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 9, 6, 1, 6),
    _LpsSmtFddiPortLabel_Type()
)
lpsSmtFddiPortLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpsSmtFddiPortLabel.setStatus("mandatory")
_LpsBridge_ObjectIdentity = ObjectIdentity
lpsBridge = _LpsBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10)
)
_LpsBridgeCount_Type = Integer32
_LpsBridgeCount_Object = MibScalar
lpsBridgeCount = _LpsBridgeCount_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 1),
    _LpsBridgeCount_Type()
)
lpsBridgeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsBridgeCount.setStatus("mandatory")
_LpsBridgeTable_Object = MibTable
lpsBridgeTable = _LpsBridgeTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 2)
)
if mibBuilder.loadTexts:
    lpsBridgeTable.setStatus("mandatory")
_LpsBridgeEntry_Object = MibTableRow
lpsBridgeEntry = _LpsBridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 2, 1)
)
lpsBridgeEntry.setIndexNames(
    (0, "LANPLEX-SYSTEMS-MIB-1-2-2", "lpsBridgeIndex"),
)
if mibBuilder.loadTexts:
    lpsBridgeEntry.setStatus("mandatory")
_LpsBridgeIndex_Type = Integer32
_LpsBridgeIndex_Object = MibTableColumn
lpsBridgeIndex = _LpsBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 2, 1, 1),
    _LpsBridgeIndex_Type()
)
lpsBridgeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsBridgeIndex.setStatus("mandatory")
_LpsBridgePortCount_Type = Integer32
_LpsBridgePortCount_Object = MibTableColumn
lpsBridgePortCount = _LpsBridgePortCount_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 2, 1, 2),
    _LpsBridgePortCount_Type()
)
lpsBridgePortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsBridgePortCount.setStatus("mandatory")
_LpsBridgeAddressTableSize_Type = Integer32
_LpsBridgeAddressTableSize_Object = MibTableColumn
lpsBridgeAddressTableSize = _LpsBridgeAddressTableSize_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 2, 1, 3),
    _LpsBridgeAddressTableSize_Type()
)
lpsBridgeAddressTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsBridgeAddressTableSize.setStatus("mandatory")
_LpsBridgeAddressTableCount_Type = Integer32
_LpsBridgeAddressTableCount_Object = MibTableColumn
lpsBridgeAddressTableCount = _LpsBridgeAddressTableCount_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 2, 1, 4),
    _LpsBridgeAddressTableCount_Type()
)
lpsBridgeAddressTableCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsBridgeAddressTableCount.setStatus("mandatory")
_LpsBridgeAddressTablePeakCount_Type = Integer32
_LpsBridgeAddressTablePeakCount_Object = MibTableColumn
lpsBridgeAddressTablePeakCount = _LpsBridgeAddressTablePeakCount_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 2, 1, 5),
    _LpsBridgeAddressTablePeakCount_Type()
)
lpsBridgeAddressTablePeakCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsBridgeAddressTablePeakCount.setStatus("mandatory")
_LpsBridgeAddressThreshold_Type = Integer32
_LpsBridgeAddressThreshold_Object = MibTableColumn
lpsBridgeAddressThreshold = _LpsBridgeAddressThreshold_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 2, 1, 6),
    _LpsBridgeAddressThreshold_Type()
)
lpsBridgeAddressThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpsBridgeAddressThreshold.setStatus("mandatory")


class _LpsBridgeMode_Type(Integer32):
    """Custom type lpsBridgeMode based on Integer32"""
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
        *(("expressMode", 1),
          ("ibmSRBridgeMode", 6),
          ("ieee8021dBridgeMode", 2),
          ("ieee8021dSRBridgeMode", 5),
          ("ieee8021dSRTBridgeMode", 4),
          ("notSupported", 3),
          ("srExpressBridgeMode", 8),
          ("srtBBridgeMode", 7))
    )


_LpsBridgeMode_Type.__name__ = "Integer32"
_LpsBridgeMode_Object = MibTableColumn
lpsBridgeMode = _LpsBridgeMode_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 2, 1, 7),
    _LpsBridgeMode_Type()
)
lpsBridgeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpsBridgeMode.setStatus("mandatory")
_LpsBridgeBackbonePort_Type = Integer32
_LpsBridgeBackbonePort_Object = MibTableColumn
lpsBridgeBackbonePort = _LpsBridgeBackbonePort_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 2, 1, 8),
    _LpsBridgeBackbonePort_Type()
)
lpsBridgeBackbonePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpsBridgeBackbonePort.setStatus("mandatory")


class _LpsBridgeIpFragmentationEnabled_Type(Integer32):
    """Custom type lpsBridgeIpFragmentationEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("notSupported", 3),
          ("true", 1))
    )


_LpsBridgeIpFragmentationEnabled_Type.__name__ = "Integer32"
_LpsBridgeIpFragmentationEnabled_Object = MibTableColumn
lpsBridgeIpFragmentationEnabled = _LpsBridgeIpFragmentationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 2, 1, 9),
    _LpsBridgeIpFragmentationEnabled_Type()
)
lpsBridgeIpFragmentationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpsBridgeIpFragmentationEnabled.setStatus("mandatory")


class _LpsBridgeTrFddiTranslationMode_Type(Integer32):
    """Custom type lpsBridgeTrFddiTranslationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backbone", 2),
          ("native", 1))
    )


_LpsBridgeTrFddiTranslationMode_Type.__name__ = "Integer32"
_LpsBridgeTrFddiTranslationMode_Object = MibTableColumn
lpsBridgeTrFddiTranslationMode = _LpsBridgeTrFddiTranslationMode_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 2, 1, 10),
    _LpsBridgeTrFddiTranslationMode_Type()
)
lpsBridgeTrFddiTranslationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpsBridgeTrFddiTranslationMode.setStatus("mandatory")
_LpsBridgePortTable_Object = MibTable
lpsBridgePortTable = _LpsBridgePortTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 3)
)
if mibBuilder.loadTexts:
    lpsBridgePortTable.setStatus("mandatory")
_LpsBridgePortEntry_Object = MibTableRow
lpsBridgePortEntry = _LpsBridgePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 3, 1)
)
lpsBridgePortEntry.setIndexNames(
    (0, "LANPLEX-SYSTEMS-MIB-1-2-2", "lpsBridgePortBridgeIndex"),
    (0, "LANPLEX-SYSTEMS-MIB-1-2-2", "lpsBridgePortIndex"),
)
if mibBuilder.loadTexts:
    lpsBridgePortEntry.setStatus("mandatory")
_LpsBridgePortBridgeIndex_Type = Integer32
_LpsBridgePortBridgeIndex_Object = MibTableColumn
lpsBridgePortBridgeIndex = _LpsBridgePortBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 3, 1, 1),
    _LpsBridgePortBridgeIndex_Type()
)
lpsBridgePortBridgeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsBridgePortBridgeIndex.setStatus("mandatory")
_LpsBridgePortIndex_Type = Integer32
_LpsBridgePortIndex_Object = MibTableColumn
lpsBridgePortIndex = _LpsBridgePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 3, 1, 2),
    _LpsBridgePortIndex_Type()
)
lpsBridgePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsBridgePortIndex.setStatus("mandatory")
_LpsBridgePortIfIndex_Type = Integer32
_LpsBridgePortIfIndex_Object = MibTableColumn
lpsBridgePortIfIndex = _LpsBridgePortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 3, 1, 3),
    _LpsBridgePortIfIndex_Type()
)
lpsBridgePortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsBridgePortIfIndex.setStatus("mandatory")


class _LpsBridgePortReceiveMulticastLimit_Type(Integer32):
    """Custom type lpsBridgePortReceiveMulticastLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LpsBridgePortReceiveMulticastLimit_Type.__name__ = "Integer32"
_LpsBridgePortReceiveMulticastLimit_Object = MibTableColumn
lpsBridgePortReceiveMulticastLimit = _LpsBridgePortReceiveMulticastLimit_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 3, 1, 4),
    _LpsBridgePortReceiveMulticastLimit_Type()
)
lpsBridgePortReceiveMulticastLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpsBridgePortReceiveMulticastLimit.setStatus("mandatory")


class _LpsBridgePortAddressAction_Type(Integer32):
    """Custom type lpsBridgePortAddressAction based on Integer32"""
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
        *(("flushAddress", 3),
          ("flushDynamicAddress", 4),
          ("freezeAddress", 2),
          ("other", 1))
    )


_LpsBridgePortAddressAction_Type.__name__ = "Integer32"
_LpsBridgePortAddressAction_Object = MibTableColumn
lpsBridgePortAddressAction = _LpsBridgePortAddressAction_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 3, 1, 5),
    _LpsBridgePortAddressAction_Type()
)
lpsBridgePortAddressAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpsBridgePortAddressAction.setStatus("mandatory")
_LpsBridgePortSpanningTreeFrameReceivedCounts_Type = Counter32
_LpsBridgePortSpanningTreeFrameReceivedCounts_Object = MibTableColumn
lpsBridgePortSpanningTreeFrameReceivedCounts = _LpsBridgePortSpanningTreeFrameReceivedCounts_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 3, 1, 6),
    _LpsBridgePortSpanningTreeFrameReceivedCounts_Type()
)
lpsBridgePortSpanningTreeFrameReceivedCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsBridgePortSpanningTreeFrameReceivedCounts.setStatus("mandatory")
_LpsBridgePortReceiveBlockedDiscards_Type = Counter32
_LpsBridgePortReceiveBlockedDiscards_Object = MibTableColumn
lpsBridgePortReceiveBlockedDiscards = _LpsBridgePortReceiveBlockedDiscards_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 3, 1, 7),
    _LpsBridgePortReceiveBlockedDiscards_Type()
)
lpsBridgePortReceiveBlockedDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsBridgePortReceiveBlockedDiscards.setStatus("mandatory")
_LpsBridgePortReceiveMulticastLimitExceededs_Type = Counter32
_LpsBridgePortReceiveMulticastLimitExceededs_Object = MibTableColumn
lpsBridgePortReceiveMulticastLimitExceededs = _LpsBridgePortReceiveMulticastLimitExceededs_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 3, 1, 8),
    _LpsBridgePortReceiveMulticastLimitExceededs_Type()
)
lpsBridgePortReceiveMulticastLimitExceededs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsBridgePortReceiveMulticastLimitExceededs.setStatus("mandatory")
_LpsBridgePortReceiveMulticastLimitExceededDiscards_Type = Counter32
_LpsBridgePortReceiveMulticastLimitExceededDiscards_Object = MibTableColumn
lpsBridgePortReceiveMulticastLimitExceededDiscards = _LpsBridgePortReceiveMulticastLimitExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 3, 1, 9),
    _LpsBridgePortReceiveMulticastLimitExceededDiscards_Type()
)
lpsBridgePortReceiveMulticastLimitExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsBridgePortReceiveMulticastLimitExceededDiscards.setStatus("mandatory")
_LpsBridgePortReceiveSecurityDiscards_Type = Counter32
_LpsBridgePortReceiveSecurityDiscards_Object = MibTableColumn
lpsBridgePortReceiveSecurityDiscards = _LpsBridgePortReceiveSecurityDiscards_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 3, 1, 10),
    _LpsBridgePortReceiveSecurityDiscards_Type()
)
lpsBridgePortReceiveSecurityDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsBridgePortReceiveSecurityDiscards.setStatus("mandatory")
_LpsBridgePortReceiveUnknownDiscards_Type = Counter32
_LpsBridgePortReceiveUnknownDiscards_Object = MibTableColumn
lpsBridgePortReceiveUnknownDiscards = _LpsBridgePortReceiveUnknownDiscards_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 3, 1, 11),
    _LpsBridgePortReceiveUnknownDiscards_Type()
)
lpsBridgePortReceiveUnknownDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsBridgePortReceiveUnknownDiscards.setStatus("mandatory")
_LpsBridgePortReceiveOtherDiscards_Type = Counter32
_LpsBridgePortReceiveOtherDiscards_Object = MibTableColumn
lpsBridgePortReceiveOtherDiscards = _LpsBridgePortReceiveOtherDiscards_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 3, 1, 12),
    _LpsBridgePortReceiveOtherDiscards_Type()
)
lpsBridgePortReceiveOtherDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsBridgePortReceiveOtherDiscards.setStatus("mandatory")
_LpsBridgePortReceiveErrorDiscards_Type = Counter32
_LpsBridgePortReceiveErrorDiscards_Object = MibTableColumn
lpsBridgePortReceiveErrorDiscards = _LpsBridgePortReceiveErrorDiscards_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 3, 1, 13),
    _LpsBridgePortReceiveErrorDiscards_Type()
)
lpsBridgePortReceiveErrorDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsBridgePortReceiveErrorDiscards.setStatus("mandatory")
_LpsBridgePortSameSegmentDiscards_Type = Counter32
_LpsBridgePortSameSegmentDiscards_Object = MibTableColumn
lpsBridgePortSameSegmentDiscards = _LpsBridgePortSameSegmentDiscards_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 3, 1, 14),
    _LpsBridgePortSameSegmentDiscards_Type()
)
lpsBridgePortSameSegmentDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsBridgePortSameSegmentDiscards.setStatus("mandatory")
_LpsBridgePortTransmitBlockedDiscards_Type = Counter32
_LpsBridgePortTransmitBlockedDiscards_Object = MibTableColumn
lpsBridgePortTransmitBlockedDiscards = _LpsBridgePortTransmitBlockedDiscards_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 3, 1, 15),
    _LpsBridgePortTransmitBlockedDiscards_Type()
)
lpsBridgePortTransmitBlockedDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsBridgePortTransmitBlockedDiscards.setStatus("mandatory")
_LpsBridgePortReceiveAllPathFilteredFrames_Type = Counter32
_LpsBridgePortReceiveAllPathFilteredFrames_Object = MibTableColumn
lpsBridgePortReceiveAllPathFilteredFrames = _LpsBridgePortReceiveAllPathFilteredFrames_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 3, 1, 16),
    _LpsBridgePortReceiveAllPathFilteredFrames_Type()
)
lpsBridgePortReceiveAllPathFilteredFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsBridgePortReceiveAllPathFilteredFrames.setStatus("mandatory")
_LpsBridgePortReceiveMulticastPathFilteredFrames_Type = Counter32
_LpsBridgePortReceiveMulticastPathFilteredFrames_Object = MibTableColumn
lpsBridgePortReceiveMulticastPathFilteredFrames = _LpsBridgePortReceiveMulticastPathFilteredFrames_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 3, 1, 17),
    _LpsBridgePortReceiveMulticastPathFilteredFrames_Type()
)
lpsBridgePortReceiveMulticastPathFilteredFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsBridgePortReceiveMulticastPathFilteredFrames.setStatus("mandatory")
_LpsBridgePortTransmitAllPathFilteredFrames_Type = Counter32
_LpsBridgePortTransmitAllPathFilteredFrames_Object = MibTableColumn
lpsBridgePortTransmitAllPathFilteredFrames = _LpsBridgePortTransmitAllPathFilteredFrames_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 3, 1, 18),
    _LpsBridgePortTransmitAllPathFilteredFrames_Type()
)
lpsBridgePortTransmitAllPathFilteredFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsBridgePortTransmitAllPathFilteredFrames.setStatus("mandatory")
_LpsBridgePortTransmitMulticastPathFilteredFrames_Type = Counter32
_LpsBridgePortTransmitMulticastPathFilteredFrames_Object = MibTableColumn
lpsBridgePortTransmitMulticastPathFilteredFrames = _LpsBridgePortTransmitMulticastPathFilteredFrames_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 3, 1, 19),
    _LpsBridgePortTransmitMulticastPathFilteredFrames_Type()
)
lpsBridgePortTransmitMulticastPathFilteredFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsBridgePortTransmitMulticastPathFilteredFrames.setStatus("mandatory")
_LpsBridgePortForwardedUnicastFrames_Type = Counter32
_LpsBridgePortForwardedUnicastFrames_Object = MibTableColumn
lpsBridgePortForwardedUnicastFrames = _LpsBridgePortForwardedUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 3, 1, 20),
    _LpsBridgePortForwardedUnicastFrames_Type()
)
lpsBridgePortForwardedUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsBridgePortForwardedUnicastFrames.setStatus("mandatory")
_LpsBridgePortForwardedUnicastOctets_Type = Counter32
_LpsBridgePortForwardedUnicastOctets_Object = MibTableColumn
lpsBridgePortForwardedUnicastOctets = _LpsBridgePortForwardedUnicastOctets_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 3, 1, 21),
    _LpsBridgePortForwardedUnicastOctets_Type()
)
lpsBridgePortForwardedUnicastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsBridgePortForwardedUnicastOctets.setStatus("mandatory")
_LpsBridgePortForwardedMulticastFrames_Type = Counter32
_LpsBridgePortForwardedMulticastFrames_Object = MibTableColumn
lpsBridgePortForwardedMulticastFrames = _LpsBridgePortForwardedMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 3, 1, 22),
    _LpsBridgePortForwardedMulticastFrames_Type()
)
lpsBridgePortForwardedMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsBridgePortForwardedMulticastFrames.setStatus("mandatory")
_LpsBridgePortForwardedMulticastOctets_Type = Counter32
_LpsBridgePortForwardedMulticastOctets_Object = MibTableColumn
lpsBridgePortForwardedMulticastOctets = _LpsBridgePortForwardedMulticastOctets_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 3, 1, 23),
    _LpsBridgePortForwardedMulticastOctets_Type()
)
lpsBridgePortForwardedMulticastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsBridgePortForwardedMulticastOctets.setStatus("mandatory")
_LpsBridgePortFloodedUnicastFrames_Type = Counter32
_LpsBridgePortFloodedUnicastFrames_Object = MibTableColumn
lpsBridgePortFloodedUnicastFrames = _LpsBridgePortFloodedUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 3, 1, 24),
    _LpsBridgePortFloodedUnicastFrames_Type()
)
lpsBridgePortFloodedUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsBridgePortFloodedUnicastFrames.setStatus("mandatory")
_LpsBridgePortFloodedUnicastOctets_Type = Counter32
_LpsBridgePortFloodedUnicastOctets_Object = MibTableColumn
lpsBridgePortFloodedUnicastOctets = _LpsBridgePortFloodedUnicastOctets_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 3, 1, 25),
    _LpsBridgePortFloodedUnicastOctets_Type()
)
lpsBridgePortFloodedUnicastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsBridgePortFloodedUnicastOctets.setStatus("mandatory")
_LpsBridgePortPairTable_Object = MibTable
lpsBridgePortPairTable = _LpsBridgePortPairTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 4)
)
if mibBuilder.loadTexts:
    lpsBridgePortPairTable.setStatus("mandatory")
_LpsBridgePortPairEntry_Object = MibTableRow
lpsBridgePortPairEntry = _LpsBridgePortPairEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 4, 1)
)
lpsBridgePortPairEntry.setIndexNames(
    (0, "LANPLEX-SYSTEMS-MIB-1-2-2", "lpsBridgePortPairBridgeIndex"),
    (0, "LANPLEX-SYSTEMS-MIB-1-2-2", "lpsBridgePortPairReceivePortIndex"),
    (0, "LANPLEX-SYSTEMS-MIB-1-2-2", "lpsBridgePortPairDestinationPortIndex"),
)
if mibBuilder.loadTexts:
    lpsBridgePortPairEntry.setStatus("mandatory")
_LpsBridgePortPairBridgeIndex_Type = Integer32
_LpsBridgePortPairBridgeIndex_Object = MibTableColumn
lpsBridgePortPairBridgeIndex = _LpsBridgePortPairBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 4, 1, 1),
    _LpsBridgePortPairBridgeIndex_Type()
)
lpsBridgePortPairBridgeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsBridgePortPairBridgeIndex.setStatus("mandatory")
_LpsBridgePortPairReceivePortIndex_Type = Integer32
_LpsBridgePortPairReceivePortIndex_Object = MibTableColumn
lpsBridgePortPairReceivePortIndex = _LpsBridgePortPairReceivePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 4, 1, 2),
    _LpsBridgePortPairReceivePortIndex_Type()
)
lpsBridgePortPairReceivePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsBridgePortPairReceivePortIndex.setStatus("mandatory")
_LpsBridgePortPairDestinationPortIndex_Type = Integer32
_LpsBridgePortPairDestinationPortIndex_Object = MibTableColumn
lpsBridgePortPairDestinationPortIndex = _LpsBridgePortPairDestinationPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 4, 1, 3),
    _LpsBridgePortPairDestinationPortIndex_Type()
)
lpsBridgePortPairDestinationPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsBridgePortPairDestinationPortIndex.setStatus("mandatory")
_LpsBridgePortPairForwardedToUnicastFrames_Type = Counter32
_LpsBridgePortPairForwardedToUnicastFrames_Object = MibTableColumn
lpsBridgePortPairForwardedToUnicastFrames = _LpsBridgePortPairForwardedToUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 4, 1, 4),
    _LpsBridgePortPairForwardedToUnicastFrames_Type()
)
lpsBridgePortPairForwardedToUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsBridgePortPairForwardedToUnicastFrames.setStatus("mandatory")
_LpsBridgePortPairForwardedToUnicastOctets_Type = Counter32
_LpsBridgePortPairForwardedToUnicastOctets_Object = MibTableColumn
lpsBridgePortPairForwardedToUnicastOctets = _LpsBridgePortPairForwardedToUnicastOctets_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 4, 1, 5),
    _LpsBridgePortPairForwardedToUnicastOctets_Type()
)
lpsBridgePortPairForwardedToUnicastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsBridgePortPairForwardedToUnicastOctets.setStatus("mandatory")
_LpsBridgePortAddressTable_Object = MibTable
lpsBridgePortAddressTable = _LpsBridgePortAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 5)
)
if mibBuilder.loadTexts:
    lpsBridgePortAddressTable.setStatus("mandatory")
_LpsBridgePortAddressEntry_Object = MibTableRow
lpsBridgePortAddressEntry = _LpsBridgePortAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 5, 1)
)
lpsBridgePortAddressEntry.setIndexNames(
    (0, "LANPLEX-SYSTEMS-MIB-1-2-2", "lpsBridgePortAddressBridgeIndex"),
    (0, "LANPLEX-SYSTEMS-MIB-1-2-2", "lpsBridgePortAddressPortIndex"),
    (0, "LANPLEX-SYSTEMS-MIB-1-2-2", "lpsBridgePortAddressIndex"),
)
if mibBuilder.loadTexts:
    lpsBridgePortAddressEntry.setStatus("mandatory")
_LpsBridgePortAddressBridgeIndex_Type = Integer32
_LpsBridgePortAddressBridgeIndex_Object = MibTableColumn
lpsBridgePortAddressBridgeIndex = _LpsBridgePortAddressBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 5, 1, 1),
    _LpsBridgePortAddressBridgeIndex_Type()
)
lpsBridgePortAddressBridgeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsBridgePortAddressBridgeIndex.setStatus("mandatory")
_LpsBridgePortAddressPortIndex_Type = Integer32
_LpsBridgePortAddressPortIndex_Object = MibTableColumn
lpsBridgePortAddressPortIndex = _LpsBridgePortAddressPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 5, 1, 2),
    _LpsBridgePortAddressPortIndex_Type()
)
lpsBridgePortAddressPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsBridgePortAddressPortIndex.setStatus("mandatory")
_LpsBridgePortAddressIndex_Type = Integer32
_LpsBridgePortAddressIndex_Object = MibTableColumn
lpsBridgePortAddressIndex = _LpsBridgePortAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 5, 1, 3),
    _LpsBridgePortAddressIndex_Type()
)
lpsBridgePortAddressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsBridgePortAddressIndex.setStatus("mandatory")


class _LpsBridgePortAddressRemoteAddress_Type(OctetString):
    """Custom type lpsBridgePortAddressRemoteAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_LpsBridgePortAddressRemoteAddress_Type.__name__ = "OctetString"
_LpsBridgePortAddressRemoteAddress_Object = MibTableColumn
lpsBridgePortAddressRemoteAddress = _LpsBridgePortAddressRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 5, 1, 4),
    _LpsBridgePortAddressRemoteAddress_Type()
)
lpsBridgePortAddressRemoteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpsBridgePortAddressRemoteAddress.setStatus("mandatory")


class _LpsBridgePortAddressType_Type(Integer32):
    """Custom type lpsBridgePortAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_LpsBridgePortAddressType_Type.__name__ = "Integer32"
_LpsBridgePortAddressType_Object = MibTableColumn
lpsBridgePortAddressType = _LpsBridgePortAddressType_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 5, 1, 5),
    _LpsBridgePortAddressType_Type()
)
lpsBridgePortAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpsBridgePortAddressType.setStatus("mandatory")


class _LpsBridgePortAddressIsStatic_Type(Integer32):
    """Custom type lpsBridgePortAddressIsStatic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("isDynamic", 2),
          ("isStatic", 1))
    )


_LpsBridgePortAddressIsStatic_Type.__name__ = "Integer32"
_LpsBridgePortAddressIsStatic_Object = MibTableColumn
lpsBridgePortAddressIsStatic = _LpsBridgePortAddressIsStatic_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 5, 1, 6),
    _LpsBridgePortAddressIsStatic_Type()
)
lpsBridgePortAddressIsStatic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpsBridgePortAddressIsStatic.setStatus("mandatory")
_LpsBridgePortAddressStaticPort_Type = Integer32
_LpsBridgePortAddressStaticPort_Object = MibTableColumn
lpsBridgePortAddressStaticPort = _LpsBridgePortAddressStaticPort_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 5, 1, 7),
    _LpsBridgePortAddressStaticPort_Type()
)
lpsBridgePortAddressStaticPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsBridgePortAddressStaticPort.setStatus("mandatory")
_LpsBridgePortAddressAge_Type = Integer32
_LpsBridgePortAddressAge_Object = MibTableColumn
lpsBridgePortAddressAge = _LpsBridgePortAddressAge_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 5, 1, 8),
    _LpsBridgePortAddressAge_Type()
)
lpsBridgePortAddressAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsBridgePortAddressAge.setStatus("mandatory")


class _LpsBridgeStpGroupAddress_Type(OctetString):
    """Custom type lpsBridgeStpGroupAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_LpsBridgeStpGroupAddress_Type.__name__ = "OctetString"
_LpsBridgeStpGroupAddress_Object = MibScalar
lpsBridgeStpGroupAddress = _LpsBridgeStpGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 6),
    _LpsBridgeStpGroupAddress_Type()
)
lpsBridgeStpGroupAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpsBridgeStpGroupAddress.setStatus("mandatory")


class _LpsBridgeStpEnable_Type(Integer32):
    """Custom type lpsBridgeStpEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_LpsBridgeStpEnable_Type.__name__ = "Integer32"
_LpsBridgeStpEnable_Object = MibScalar
lpsBridgeStpEnable = _LpsBridgeStpEnable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 10, 7),
    _LpsBridgeStpEnable_Type()
)
lpsBridgeStpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpsBridgeStpEnable.setStatus("mandatory")
_LpsIpRouter_ObjectIdentity = ObjectIdentity
lpsIpRouter = _LpsIpRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 11)
)
_LpsNetworkMonitor_ObjectIdentity = ObjectIdentity
lpsNetworkMonitor = _LpsNetworkMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 12)
)
_LpsNetworkAnalyzerTable_Object = MibTable
lpsNetworkAnalyzerTable = _LpsNetworkAnalyzerTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 12, 1)
)
if mibBuilder.loadTexts:
    lpsNetworkAnalyzerTable.setStatus("mandatory")
_LpsNetworkAnalyzerTableEntry_Object = MibTableRow
lpsNetworkAnalyzerTableEntry = _LpsNetworkAnalyzerTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 12, 1, 1)
)
lpsNetworkAnalyzerTableEntry.setIndexNames(
    (0, "LANPLEX-SYSTEMS-MIB-1-2-2", "lpsNetworkAnalyzerBridgeIndex"),
    (0, "LANPLEX-SYSTEMS-MIB-1-2-2", "lpsNetworkAnalyzerBridgePortIndex"),
)
if mibBuilder.loadTexts:
    lpsNetworkAnalyzerTableEntry.setStatus("mandatory")
_LpsNetworkAnalyzerBridgeIndex_Type = Integer32
_LpsNetworkAnalyzerBridgeIndex_Object = MibTableColumn
lpsNetworkAnalyzerBridgeIndex = _LpsNetworkAnalyzerBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 12, 1, 1, 1),
    _LpsNetworkAnalyzerBridgeIndex_Type()
)
lpsNetworkAnalyzerBridgeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsNetworkAnalyzerBridgeIndex.setStatus("mandatory")
_LpsNetworkAnalyzerBridgePortIndex_Type = Integer32
_LpsNetworkAnalyzerBridgePortIndex_Object = MibTableColumn
lpsNetworkAnalyzerBridgePortIndex = _LpsNetworkAnalyzerBridgePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 12, 1, 1, 2),
    _LpsNetworkAnalyzerBridgePortIndex_Type()
)
lpsNetworkAnalyzerBridgePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsNetworkAnalyzerBridgePortIndex.setStatus("mandatory")


class _LpsNetworkAnalyzerPhysicalAddress_Type(OctetString):
    """Custom type lpsNetworkAnalyzerPhysicalAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_LpsNetworkAnalyzerPhysicalAddress_Type.__name__ = "OctetString"
_LpsNetworkAnalyzerPhysicalAddress_Object = MibTableColumn
lpsNetworkAnalyzerPhysicalAddress = _LpsNetworkAnalyzerPhysicalAddress_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 12, 1, 1, 3),
    _LpsNetworkAnalyzerPhysicalAddress_Type()
)
lpsNetworkAnalyzerPhysicalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsNetworkAnalyzerPhysicalAddress.setStatus("mandatory")


class _LpsNetworkAnalyzerStatus_Type(Integer32):
    """Custom type lpsNetworkAnalyzerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_LpsNetworkAnalyzerStatus_Type.__name__ = "Integer32"
_LpsNetworkAnalyzerStatus_Object = MibTableColumn
lpsNetworkAnalyzerStatus = _LpsNetworkAnalyzerStatus_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 12, 1, 1, 4),
    _LpsNetworkAnalyzerStatus_Type()
)
lpsNetworkAnalyzerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpsNetworkAnalyzerStatus.setStatus("mandatory")
_LpsNetworkPortMonitorTable_Object = MibTable
lpsNetworkPortMonitorTable = _LpsNetworkPortMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 12, 2)
)
if mibBuilder.loadTexts:
    lpsNetworkPortMonitorTable.setStatus("mandatory")
_LpsNetworkPortMonitorTableEntry_Object = MibTableRow
lpsNetworkPortMonitorTableEntry = _LpsNetworkPortMonitorTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 12, 2, 1)
)
lpsNetworkPortMonitorTableEntry.setIndexNames(
    (0, "LANPLEX-SYSTEMS-MIB-1-2-2", "lpsNetworkPortMonitorBridgeIndex"),
    (0, "LANPLEX-SYSTEMS-MIB-1-2-2", "lpsNetworkPortMonitorBridgePortIndex"),
)
if mibBuilder.loadTexts:
    lpsNetworkPortMonitorTableEntry.setStatus("mandatory")
_LpsNetworkPortMonitorBridgeIndex_Type = Integer32
_LpsNetworkPortMonitorBridgeIndex_Object = MibTableColumn
lpsNetworkPortMonitorBridgeIndex = _LpsNetworkPortMonitorBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 12, 2, 1, 1),
    _LpsNetworkPortMonitorBridgeIndex_Type()
)
lpsNetworkPortMonitorBridgeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsNetworkPortMonitorBridgeIndex.setStatus("mandatory")
_LpsNetworkPortMonitorBridgePortIndex_Type = Integer32
_LpsNetworkPortMonitorBridgePortIndex_Object = MibTableColumn
lpsNetworkPortMonitorBridgePortIndex = _LpsNetworkPortMonitorBridgePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 12, 2, 1, 2),
    _LpsNetworkPortMonitorBridgePortIndex_Type()
)
lpsNetworkPortMonitorBridgePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsNetworkPortMonitorBridgePortIndex.setStatus("mandatory")


class _LpsNetworkPortMonitorAnalyzerAddress_Type(OctetString):
    """Custom type lpsNetworkPortMonitorAnalyzerAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_LpsNetworkPortMonitorAnalyzerAddress_Type.__name__ = "OctetString"
_LpsNetworkPortMonitorAnalyzerAddress_Object = MibTableColumn
lpsNetworkPortMonitorAnalyzerAddress = _LpsNetworkPortMonitorAnalyzerAddress_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 12, 2, 1, 3),
    _LpsNetworkPortMonitorAnalyzerAddress_Type()
)
lpsNetworkPortMonitorAnalyzerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpsNetworkPortMonitorAnalyzerAddress.setStatus("mandatory")


class _LpsNetworkPortMonitorStatus_Type(Integer32):
    """Custom type lpsNetworkPortMonitorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_LpsNetworkPortMonitorStatus_Type.__name__ = "Integer32"
_LpsNetworkPortMonitorStatus_Object = MibTableColumn
lpsNetworkPortMonitorStatus = _LpsNetworkPortMonitorStatus_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 12, 2, 1, 4),
    _LpsNetworkPortMonitorStatus_Type()
)
lpsNetworkPortMonitorStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpsNetworkPortMonitorStatus.setStatus("mandatory")
_LpsTokenRingPort_ObjectIdentity = ObjectIdentity
lpsTokenRingPort = _LpsTokenRingPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 13)
)
_LpsTokenRingPortCount_Type = Integer32
_LpsTokenRingPortCount_Object = MibScalar
lpsTokenRingPortCount = _LpsTokenRingPortCount_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 13, 1),
    _LpsTokenRingPortCount_Type()
)
lpsTokenRingPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsTokenRingPortCount.setStatus("mandatory")
_LpsTokenRingPortTable_Object = MibTable
lpsTokenRingPortTable = _LpsTokenRingPortTable_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 13, 2)
)
if mibBuilder.loadTexts:
    lpsTokenRingPortTable.setStatus("mandatory")
_LpsTokenRingPortEntry_Object = MibTableRow
lpsTokenRingPortEntry = _LpsTokenRingPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 13, 2, 1)
)
lpsTokenRingPortEntry.setIndexNames(
    (0, "LANPLEX-SYSTEMS-MIB-1-2-2", "lpsTokenRingPortIndex"),
)
if mibBuilder.loadTexts:
    lpsTokenRingPortEntry.setStatus("mandatory")
_LpsTokenRingPortIndex_Type = Integer32
_LpsTokenRingPortIndex_Object = MibTableColumn
lpsTokenRingPortIndex = _LpsTokenRingPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 13, 2, 1, 1),
    _LpsTokenRingPortIndex_Type()
)
lpsTokenRingPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsTokenRingPortIndex.setStatus("mandatory")
_LpsTokenRingPortIfIndex_Type = Integer32
_LpsTokenRingPortIfIndex_Object = MibTableColumn
lpsTokenRingPortIfIndex = _LpsTokenRingPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 13, 2, 1, 2),
    _LpsTokenRingPortIfIndex_Type()
)
lpsTokenRingPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsTokenRingPortIfIndex.setStatus("mandatory")


class _LpsTokenRingPortLabel_Type(DisplayString):
    """Custom type lpsTokenRingPortLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_LpsTokenRingPortLabel_Type.__name__ = "DisplayString"
_LpsTokenRingPortLabel_Object = MibTableColumn
lpsTokenRingPortLabel = _LpsTokenRingPortLabel_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 13, 2, 1, 3),
    _LpsTokenRingPortLabel_Type()
)
lpsTokenRingPortLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpsTokenRingPortLabel.setStatus("mandatory")


class _LpsTokenRingPortInsertStatus_Type(Integer32):
    """Custom type lpsTokenRingPortInsertStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deinserted", 2),
          ("inserted", 1))
    )


_LpsTokenRingPortInsertStatus_Type.__name__ = "Integer32"
_LpsTokenRingPortInsertStatus_Object = MibTableColumn
lpsTokenRingPortInsertStatus = _LpsTokenRingPortInsertStatus_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 13, 2, 1, 4),
    _LpsTokenRingPortInsertStatus_Type()
)
lpsTokenRingPortInsertStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsTokenRingPortInsertStatus.setStatus("mandatory")


class _LpsTokenRingPortType_Type(Integer32):
    """Custom type lpsTokenRingPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 2),
          ("rj45", 1))
    )


_LpsTokenRingPortType_Type.__name__ = "Integer32"
_LpsTokenRingPortType_Object = MibTableColumn
lpsTokenRingPortType = _LpsTokenRingPortType_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 13, 2, 1, 5),
    _LpsTokenRingPortType_Type()
)
lpsTokenRingPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsTokenRingPortType.setStatus("mandatory")


class _LpsTokenRingPortMode_Type(Integer32):
    """Custom type lpsTokenRingPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lobe", 2),
          ("station", 1))
    )


_LpsTokenRingPortMode_Type.__name__ = "Integer32"
_LpsTokenRingPortMode_Object = MibTableColumn
lpsTokenRingPortMode = _LpsTokenRingPortMode_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 13, 2, 1, 6),
    _LpsTokenRingPortMode_Type()
)
lpsTokenRingPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpsTokenRingPortMode.setStatus("mandatory")


class _LpsTokenRingPortSpeed_Type(Integer32):
    """Custom type lpsTokenRingPortSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fourMegabit", 1),
          ("sixteenMegabit", 2),
          ("sixteenMegabitETR", 3))
    )


_LpsTokenRingPortSpeed_Type.__name__ = "Integer32"
_LpsTokenRingPortSpeed_Object = MibTableColumn
lpsTokenRingPortSpeed = _LpsTokenRingPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 13, 2, 1, 7),
    _LpsTokenRingPortSpeed_Type()
)
lpsTokenRingPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpsTokenRingPortSpeed.setStatus("mandatory")
_LpsTokenRingPortLineErrors_Type = Counter32
_LpsTokenRingPortLineErrors_Object = MibTableColumn
lpsTokenRingPortLineErrors = _LpsTokenRingPortLineErrors_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 13, 2, 1, 8),
    _LpsTokenRingPortLineErrors_Type()
)
lpsTokenRingPortLineErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsTokenRingPortLineErrors.setStatus("mandatory")
_LpsTokenRingPortBurstErrors_Type = Counter32
_LpsTokenRingPortBurstErrors_Object = MibTableColumn
lpsTokenRingPortBurstErrors = _LpsTokenRingPortBurstErrors_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 13, 2, 1, 9),
    _LpsTokenRingPortBurstErrors_Type()
)
lpsTokenRingPortBurstErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsTokenRingPortBurstErrors.setStatus("mandatory")
_LpsTokenRingPortACErrors_Type = Counter32
_LpsTokenRingPortACErrors_Object = MibTableColumn
lpsTokenRingPortACErrors = _LpsTokenRingPortACErrors_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 13, 2, 1, 10),
    _LpsTokenRingPortACErrors_Type()
)
lpsTokenRingPortACErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsTokenRingPortACErrors.setStatus("mandatory")
_LpsTokenRingPortAbortTransErrors_Type = Counter32
_LpsTokenRingPortAbortTransErrors_Object = MibTableColumn
lpsTokenRingPortAbortTransErrors = _LpsTokenRingPortAbortTransErrors_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 13, 2, 1, 11),
    _LpsTokenRingPortAbortTransErrors_Type()
)
lpsTokenRingPortAbortTransErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsTokenRingPortAbortTransErrors.setStatus("mandatory")
_LpsTokenRingPortInternalErrors_Type = Counter32
_LpsTokenRingPortInternalErrors_Object = MibTableColumn
lpsTokenRingPortInternalErrors = _LpsTokenRingPortInternalErrors_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 13, 2, 1, 12),
    _LpsTokenRingPortInternalErrors_Type()
)
lpsTokenRingPortInternalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsTokenRingPortInternalErrors.setStatus("mandatory")
_LpsTokenRingPortLostFrameErrors_Type = Counter32
_LpsTokenRingPortLostFrameErrors_Object = MibTableColumn
lpsTokenRingPortLostFrameErrors = _LpsTokenRingPortLostFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 13, 2, 1, 13),
    _LpsTokenRingPortLostFrameErrors_Type()
)
lpsTokenRingPortLostFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsTokenRingPortLostFrameErrors.setStatus("mandatory")
_LpsTokenRingPortReceiveCongestionErrors_Type = Counter32
_LpsTokenRingPortReceiveCongestionErrors_Object = MibTableColumn
lpsTokenRingPortReceiveCongestionErrors = _LpsTokenRingPortReceiveCongestionErrors_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 13, 2, 1, 14),
    _LpsTokenRingPortReceiveCongestionErrors_Type()
)
lpsTokenRingPortReceiveCongestionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsTokenRingPortReceiveCongestionErrors.setStatus("mandatory")
_LpsTokenRingPortFrameCopiedErrors_Type = Counter32
_LpsTokenRingPortFrameCopiedErrors_Object = MibTableColumn
lpsTokenRingPortFrameCopiedErrors = _LpsTokenRingPortFrameCopiedErrors_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 13, 2, 1, 15),
    _LpsTokenRingPortFrameCopiedErrors_Type()
)
lpsTokenRingPortFrameCopiedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsTokenRingPortFrameCopiedErrors.setStatus("mandatory")
_LpsTokenRingPortTokenErrors_Type = Counter32
_LpsTokenRingPortTokenErrors_Object = MibTableColumn
lpsTokenRingPortTokenErrors = _LpsTokenRingPortTokenErrors_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 13, 2, 1, 16),
    _LpsTokenRingPortTokenErrors_Type()
)
lpsTokenRingPortTokenErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsTokenRingPortTokenErrors.setStatus("mandatory")
_LpsTokenRingPortSoftErrors_Type = Counter32
_LpsTokenRingPortSoftErrors_Object = MibTableColumn
lpsTokenRingPortSoftErrors = _LpsTokenRingPortSoftErrors_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 13, 2, 1, 17),
    _LpsTokenRingPortSoftErrors_Type()
)
lpsTokenRingPortSoftErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsTokenRingPortSoftErrors.setStatus("mandatory")
_LpsTokenRingPortHardErrors_Type = Counter32
_LpsTokenRingPortHardErrors_Object = MibTableColumn
lpsTokenRingPortHardErrors = _LpsTokenRingPortHardErrors_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 13, 2, 1, 18),
    _LpsTokenRingPortHardErrors_Type()
)
lpsTokenRingPortHardErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsTokenRingPortHardErrors.setStatus("mandatory")
_LpsTokenRingPortTransmitBeacons_Type = Counter32
_LpsTokenRingPortTransmitBeacons_Object = MibTableColumn
lpsTokenRingPortTransmitBeacons = _LpsTokenRingPortTransmitBeacons_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 13, 2, 1, 19),
    _LpsTokenRingPortTransmitBeacons_Type()
)
lpsTokenRingPortTransmitBeacons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsTokenRingPortTransmitBeacons.setStatus("mandatory")
_LpsTokenRingPortLobeWires_Type = Counter32
_LpsTokenRingPortLobeWires_Object = MibTableColumn
lpsTokenRingPortLobeWires = _LpsTokenRingPortLobeWires_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 13, 2, 1, 20),
    _LpsTokenRingPortLobeWires_Type()
)
lpsTokenRingPortLobeWires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsTokenRingPortLobeWires.setStatus("mandatory")
_LpsTokenRingPortRemoves_Type = Counter32
_LpsTokenRingPortRemoves_Object = MibTableColumn
lpsTokenRingPortRemoves = _LpsTokenRingPortRemoves_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 13, 2, 1, 21),
    _LpsTokenRingPortRemoves_Type()
)
lpsTokenRingPortRemoves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsTokenRingPortRemoves.setStatus("mandatory")
_LpsTokenRingPortSingles_Type = Counter32
_LpsTokenRingPortSingles_Object = MibTableColumn
lpsTokenRingPortSingles = _LpsTokenRingPortSingles_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 13, 2, 1, 22),
    _LpsTokenRingPortSingles_Type()
)
lpsTokenRingPortSingles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsTokenRingPortSingles.setStatus("mandatory")
_LpsTokenRingPortFreqErrors_Type = Counter32
_LpsTokenRingPortFreqErrors_Object = MibTableColumn
lpsTokenRingPortFreqErrors = _LpsTokenRingPortFreqErrors_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 13, 2, 1, 23),
    _LpsTokenRingPortFreqErrors_Type()
)
lpsTokenRingPortFreqErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsTokenRingPortFreqErrors.setStatus("optional")
_LpsTokenRingPortRingStatus_Type = Integer32
_LpsTokenRingPortRingStatus_Object = MibTableColumn
lpsTokenRingPortRingStatus = _LpsTokenRingPortRingStatus_Object(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 13, 2, 1, 24),
    _LpsTokenRingPortRingStatus_Type()
)
lpsTokenRingPortRingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsTokenRingPortRingStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects

lpsSystemOverTemperatureEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 0, 1)
)
lpsSystemOverTemperatureEvent.setObjects(
    ("LANPLEX-SYSTEMS-MIB-1-2-2", "lpsSystemOvertemperature")
)
if mibBuilder.loadTexts:
    lpsSystemOverTemperatureEvent.setStatus(
        ""
    )

lpsPowerSupplyFailureEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 0, 2)
)
lpsPowerSupplyFailureEvent.setObjects(
      *(("LANPLEX-SYSTEMS-MIB-1-2-2", "lpsPowerSupplyStatusIndex"),
        ("LANPLEX-SYSTEMS-MIB-1-2-2", "lpsPowerSupplyStatus"),
        ("LANPLEX-SYSTEMS-MIB-1-2-2", "lpsPowerSupplyStatusSupported"))
)
if mibBuilder.loadTexts:
    lpsPowerSupplyFailureEvent.setStatus(
        ""
    )

lpsChassisSlotOverTemperatureEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 0, 3)
)
lpsChassisSlotOverTemperatureEvent.setObjects(
      *(("LANPLEX-SYSTEMS-MIB-1-2-2", "lpsSlotIndex"),
        ("LANPLEX-SYSTEMS-MIB-1-2-2", "lpsSlotBoardType"),
        ("LANPLEX-SYSTEMS-MIB-1-2-2", "lpsSlotBoardRevision"),
        ("LANPLEX-SYSTEMS-MIB-1-2-2", "lpsSlotBoardStatus"),
        ("LANPLEX-SYSTEMS-MIB-1-2-2", "lpsSlotOvertemperature"))
)
if mibBuilder.loadTexts:
    lpsChassisSlotOverTemperatureEvent.setStatus(
        ""
    )

lpsChassisSlotInsertEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 0, 4)
)
lpsChassisSlotInsertEvent.setObjects(
      *(("LANPLEX-SYSTEMS-MIB-1-2-2", "lpsSlotIndex"),
        ("LANPLEX-SYSTEMS-MIB-1-2-2", "lpsSlotBoardType"),
        ("LANPLEX-SYSTEMS-MIB-1-2-2", "lpsSlotBoardRevision"))
)
if mibBuilder.loadTexts:
    lpsChassisSlotInsertEvent.setStatus(
        ""
    )

lpsChassisSlotExtractEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 0, 5)
)
lpsChassisSlotExtractEvent.setObjects(
    ("LANPLEX-SYSTEMS-MIB-1-2-2", "lpsSlotIndex")
)
if mibBuilder.loadTexts:
    lpsChassisSlotExtractEvent.setStatus(
        ""
    )

lpsBridgeAddressThresholdEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 0, 6)
)
lpsBridgeAddressThresholdEvent.setObjects(
    ("LANPLEX-SYSTEMS-MIB-1-2-2", "lpsBridgeIndex")
)
if mibBuilder.loadTexts:
    lpsBridgeAddressThresholdEvent.setStatus(
        ""
    )

lpsSystemFanFailureEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 114, 1, 4, 0, 7)
)
lpsSystemFanFailureEvent.setObjects(
    ("LANPLEX-SYSTEMS-MIB-1-2-2", "lpsSystemFanFailure")
)
if mibBuilder.loadTexts:
    lpsSystemFanFailureEvent.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LANPLEX-SYSTEMS-MIB-1-2-2",
    **{"synernetics": synernetics,
       "lanplex": lanplex,
       "lpsProducts": lpsProducts,
       "lps6000": lps6000,
       "lps6012": lps6012,
       "lps6012System": lps6012System,
       "lps6012Chassis": lps6012Chassis,
       "lps6012ESM": lps6012ESM,
       "lps6012EFSM": lps6012EFSM,
       "lps6012TRSM": lps6012TRSM,
       "lps6012TMM": lps6012TMM,
       "lps6004": lps6004,
       "lps6004System": lps6004System,
       "lps6004Chassis": lps6004Chassis,
       "lps6004ESM": lps6004ESM,
       "lps6004EFSM": lps6004EFSM,
       "lps6004TRSM": lps6004TRSM,
       "lps6004TMM": lps6004TMM,
       "lps2000": lps2000,
       "lps2500": lps2500,
       "lss2200": lss2200,
       "lps2016": lps2016,
       "lanplexSystemsMib": lanplexSystemsMib,
       "lpsSystemOverTemperatureEvent": lpsSystemOverTemperatureEvent,
       "lpsPowerSupplyFailureEvent": lpsPowerSupplyFailureEvent,
       "lpsChassisSlotOverTemperatureEvent": lpsChassisSlotOverTemperatureEvent,
       "lpsChassisSlotInsertEvent": lpsChassisSlotInsertEvent,
       "lpsChassisSlotExtractEvent": lpsChassisSlotExtractEvent,
       "lpsBridgeAddressThresholdEvent": lpsBridgeAddressThresholdEvent,
       "lpsSystemFanFailureEvent": lpsSystemFanFailureEvent,
       "lpsSystem": lpsSystem,
       "lpsSystemId": lpsSystemId,
       "lpsSystemType": lpsSystemType,
       "lpsSystemName": lpsSystemName,
       "lpsSystemManufacturer": lpsSystemManufacturer,
       "lpsSystemHardwareRevision": lpsSystemHardwareRevision,
       "lpsSystemMemorySize": lpsSystemMemorySize,
       "lpsSystemFlashMemorySize": lpsSystemFlashMemorySize,
       "lpsSystemNvMemorySize": lpsSystemNvMemorySize,
       "lpsSystemSoftwareRevision": lpsSystemSoftwareRevision,
       "lpsSystemBuildTime": lpsSystemBuildTime,
       "lpsSystemSnmpRevision": lpsSystemSnmpRevision,
       "lpsSystemRequestedSnmpMode": lpsSystemRequestedSnmpMode,
       "lpsSystemCurrentSnmpMode": lpsSystemCurrentSnmpMode,
       "lpsSystemAction": lpsSystemAction,
       "lpsSystemOvertemperature": lpsSystemOvertemperature,
       "lpsSystemFanFailure": lpsSystemFanFailure,
       "lpsSystemProtocolMask": lpsSystemProtocolMask,
       "lpsSlot": lpsSlot,
       "lpsSlotCount": lpsSlotCount,
       "lpsSlotTable": lpsSlotTable,
       "lpsSlotEntry": lpsSlotEntry,
       "lpsSlotIndex": lpsSlotIndex,
       "lpsSlotBoardType": lpsSlotBoardType,
       "lpsSlotBoardRevision": lpsSlotBoardRevision,
       "lpsSlotBoardStatus": lpsSlotBoardStatus,
       "lpsSlotBoardName": lpsSlotBoardName,
       "lpsSlotBoardNameAbbrev": lpsSlotBoardNameAbbrev,
       "lpsSlotEthernetPortCount": lpsSlotEthernetPortCount,
       "lpsSlotFddiMacCount": lpsSlotFddiMacCount,
       "lpsSlotFddiPortCount": lpsSlotFddiPortCount,
       "lpsSlotOvertemperature": lpsSlotOvertemperature,
       "lpsSlotTokenRingPortCount": lpsSlotTokenRingPortCount,
       "lpsControlPanel": lpsControlPanel,
       "lpsControlPanelHardwareRevision": lpsControlPanelHardwareRevision,
       "lpsControlPanelSoftwareRevision": lpsControlPanelSoftwareRevision,
       "lpsControlPanelLines": lpsControlPanelLines,
       "lpsControlPanelColumns": lpsControlPanelColumns,
       "lpsControlPanelText": lpsControlPanelText,
       "lpsPowerSupply": lpsPowerSupply,
       "lpsPowerSupplyCount": lpsPowerSupplyCount,
       "lpsPowerSupplyStatusTable": lpsPowerSupplyStatusTable,
       "lpsPowerSupplyStatusEntry": lpsPowerSupplyStatusEntry,
       "lpsPowerSupplyStatusIndex": lpsPowerSupplyStatusIndex,
       "lpsPowerSupplyStatus": lpsPowerSupplyStatus,
       "lpsPowerSupplyStatusSupported": lpsPowerSupplyStatusSupported,
       "lpsSnmp": lpsSnmp,
       "lpsSnmpAgentId": lpsSnmpAgentId,
       "lpsSnmpInternalAgentTrapMask": lpsSnmpInternalAgentTrapMask,
       "lpsSnmpInternalAgentTrapDestinationMask": lpsSnmpInternalAgentTrapDestinationMask,
       "lpsSnmpProxyInternalRequests": lpsSnmpProxyInternalRequests,
       "lpsSnmpInternalProxyRequestMaxAge": lpsSnmpInternalProxyRequestMaxAge,
       "lpsSnmpProxyInternalTraps": lpsSnmpProxyInternalTraps,
       "lpsSnmpInternalProxyTable": lpsSnmpInternalProxyTable,
       "lpsSnmpInternalProxyEntry": lpsSnmpInternalProxyEntry,
       "lpsSnmpInternalProxyAgentId": lpsSnmpInternalProxyAgentId,
       "lpsSnmpInternalProxyAccessClass": lpsSnmpInternalProxyAccessClass,
       "lpsSnmpInternalProxyCommunity": lpsSnmpInternalProxyCommunity,
       "lpsAgent": lpsAgent,
       "lpsAgentRequestMaxAge": lpsAgentRequestMaxAge,
       "lpsAgentProxyRemoteSmtRequests": lpsAgentProxyRemoteSmtRequests,
       "lpsAgentRemoteSmtProxyRequestMaxAge": lpsAgentRemoteSmtProxyRequestMaxAge,
       "lpsAgentProxyRemoteSmtEvents": lpsAgentProxyRemoteSmtEvents,
       "lpsAgentTrapDescriptionTable": lpsAgentTrapDescriptionTable,
       "lpsAgentTrapDescriptionTableEntry": lpsAgentTrapDescriptionTableEntry,
       "lpsAgentTrapDescriptionIndex": lpsAgentTrapDescriptionIndex,
       "lpsAgentTrapEnterprise": lpsAgentTrapEnterprise,
       "lpsAgentTrapNumber": lpsAgentTrapNumber,
       "lpsAgentTrapDestinationTable": lpsAgentTrapDestinationTable,
       "lpsAgentTrapDestinationTableEntry": lpsAgentTrapDestinationTableEntry,
       "lpsAgentTrapDestinationAddressType": lpsAgentTrapDestinationAddressType,
       "lpsAgentTrapDestinationAddress": lpsAgentTrapDestinationAddress,
       "lpsAgentTrapDestinationTrapMask": lpsAgentTrapDestinationTrapMask,
       "lpsAgentTrapDestinationEntryStatus": lpsAgentTrapDestinationEntryStatus,
       "lpsInterface": lpsInterface,
       "lpsInterfaceLocationTable": lpsInterfaceLocationTable,
       "lpsInterfaceLocationEntry": lpsInterfaceLocationEntry,
       "lpsInterfaceLocationIfIndex": lpsInterfaceLocationIfIndex,
       "lpsInterfaceLocationInterfaceType": lpsInterfaceLocationInterfaceType,
       "lpsInterfaceLocationType": lpsInterfaceLocationType,
       "lpsInterfaceLocationTypeIndex": lpsInterfaceLocationTypeIndex,
       "lpsInterfaceLocationLocalIndex": lpsInterfaceLocationLocalIndex,
       "lpsEthernetPort": lpsEthernetPort,
       "lpsEthernetPortCount": lpsEthernetPortCount,
       "lpsEthernetPortTable": lpsEthernetPortTable,
       "lpsEthernetPortEntry": lpsEthernetPortEntry,
       "lpsEthernetPortIndex": lpsEthernetPortIndex,
       "lpsEthernetPortIfIndex": lpsEthernetPortIfIndex,
       "lpsEthernetPortLabel": lpsEthernetPortLabel,
       "lpsEthernetPortLinkStatus": lpsEthernetPortLinkStatus,
       "lpsEthernetPortType": lpsEthernetPortType,
       "lpsEthernetPortRateTable": lpsEthernetPortRateTable,
       "lpsEthernetPortRateEntry": lpsEthernetPortRateEntry,
       "lpsEthernetPortRateIndex": lpsEthernetPortRateIndex,
       "lpsEthernetPortRateByteReceiveRate": lpsEthernetPortRateByteReceiveRate,
       "lpsEthernetPortRatePeakByteReceiveRate": lpsEthernetPortRatePeakByteReceiveRate,
       "lpsEthernetPortRateFrameReceiveRate": lpsEthernetPortRateFrameReceiveRate,
       "lpsEthernetPortRatePeakFrameReceiveRate": lpsEthernetPortRatePeakFrameReceiveRate,
       "lpsEthernetPortRateByteTransmitRate": lpsEthernetPortRateByteTransmitRate,
       "lpsEthernetPortRatePeakByteTransmitRate": lpsEthernetPortRatePeakByteTransmitRate,
       "lpsEthernetPortRateFrameTransmitRate": lpsEthernetPortRateFrameTransmitRate,
       "lpsEthernetPortRatePeakFrameTransmitRate": lpsEthernetPortRatePeakFrameTransmitRate,
       "lpsSmt": lpsSmt,
       "lpsSmtCount": lpsSmtCount,
       "lpsSmtFddiMacBeaconTable": lpsSmtFddiMacBeaconTable,
       "lpsSmtFddiMacBeaconEntry": lpsSmtFddiMacBeaconEntry,
       "lpsSmtFddiMacBeaconSmtIndex": lpsSmtFddiMacBeaconSmtIndex,
       "lpsSmtFddiMacBeaconIndex": lpsSmtFddiMacBeaconIndex,
       "lpsSmtFddiMacBeaconHistory": lpsSmtFddiMacBeaconHistory,
       "lpsSmtFddiMacRateTable": lpsSmtFddiMacRateTable,
       "lpsSmtFddiMacRateEntry": lpsSmtFddiMacRateEntry,
       "lpsSmtFddiMacRateSmtIndex": lpsSmtFddiMacRateSmtIndex,
       "lpsSmtFddiMacRateIndex": lpsSmtFddiMacRateIndex,
       "lpsSmtFddiMacRateByteReceiveRate": lpsSmtFddiMacRateByteReceiveRate,
       "lpsSmtFddiMacRatePeakByteReceiveRate": lpsSmtFddiMacRatePeakByteReceiveRate,
       "lpsSmtFddiMacRateFrameReceiveRate": lpsSmtFddiMacRateFrameReceiveRate,
       "lpsSmtFddiMacRatePeakFrameReceiveRate": lpsSmtFddiMacRatePeakFrameReceiveRate,
       "lpsSmtFddiMacRateByteTransmitRate": lpsSmtFddiMacRateByteTransmitRate,
       "lpsSmtFddiMacRatePeakByteTransmitRate": lpsSmtFddiMacRatePeakByteTransmitRate,
       "lpsSmtFddiMacRateFrameTransmitRate": lpsSmtFddiMacRateFrameTransmitRate,
       "lpsSmtFddiMacRatePeakFrameTransmitRate": lpsSmtFddiMacRatePeakFrameTransmitRate,
       "lpsSmtFddiPortTable": lpsSmtFddiPortTable,
       "lpsSmtFddiPortEntry": lpsSmtFddiPortEntry,
       "lpsSmtFddiPortSmtIndex": lpsSmtFddiPortSmtIndex,
       "lpsSmtFddiPortIndex": lpsSmtFddiPortIndex,
       "lpsSmtFddiPortLocationType": lpsSmtFddiPortLocationType,
       "lpsSmtFddiPortLocationTypeIndex": lpsSmtFddiPortLocationTypeIndex,
       "lpsSmtFddiPortLocationLocalIndex": lpsSmtFddiPortLocationLocalIndex,
       "lpsSmtFddiPortLabel": lpsSmtFddiPortLabel,
       "lpsBridge": lpsBridge,
       "lpsBridgeCount": lpsBridgeCount,
       "lpsBridgeTable": lpsBridgeTable,
       "lpsBridgeEntry": lpsBridgeEntry,
       "lpsBridgeIndex": lpsBridgeIndex,
       "lpsBridgePortCount": lpsBridgePortCount,
       "lpsBridgeAddressTableSize": lpsBridgeAddressTableSize,
       "lpsBridgeAddressTableCount": lpsBridgeAddressTableCount,
       "lpsBridgeAddressTablePeakCount": lpsBridgeAddressTablePeakCount,
       "lpsBridgeAddressThreshold": lpsBridgeAddressThreshold,
       "lpsBridgeMode": lpsBridgeMode,
       "lpsBridgeBackbonePort": lpsBridgeBackbonePort,
       "lpsBridgeIpFragmentationEnabled": lpsBridgeIpFragmentationEnabled,
       "lpsBridgeTrFddiTranslationMode": lpsBridgeTrFddiTranslationMode,
       "lpsBridgePortTable": lpsBridgePortTable,
       "lpsBridgePortEntry": lpsBridgePortEntry,
       "lpsBridgePortBridgeIndex": lpsBridgePortBridgeIndex,
       "lpsBridgePortIndex": lpsBridgePortIndex,
       "lpsBridgePortIfIndex": lpsBridgePortIfIndex,
       "lpsBridgePortReceiveMulticastLimit": lpsBridgePortReceiveMulticastLimit,
       "lpsBridgePortAddressAction": lpsBridgePortAddressAction,
       "lpsBridgePortSpanningTreeFrameReceivedCounts": lpsBridgePortSpanningTreeFrameReceivedCounts,
       "lpsBridgePortReceiveBlockedDiscards": lpsBridgePortReceiveBlockedDiscards,
       "lpsBridgePortReceiveMulticastLimitExceededs": lpsBridgePortReceiveMulticastLimitExceededs,
       "lpsBridgePortReceiveMulticastLimitExceededDiscards": lpsBridgePortReceiveMulticastLimitExceededDiscards,
       "lpsBridgePortReceiveSecurityDiscards": lpsBridgePortReceiveSecurityDiscards,
       "lpsBridgePortReceiveUnknownDiscards": lpsBridgePortReceiveUnknownDiscards,
       "lpsBridgePortReceiveOtherDiscards": lpsBridgePortReceiveOtherDiscards,
       "lpsBridgePortReceiveErrorDiscards": lpsBridgePortReceiveErrorDiscards,
       "lpsBridgePortSameSegmentDiscards": lpsBridgePortSameSegmentDiscards,
       "lpsBridgePortTransmitBlockedDiscards": lpsBridgePortTransmitBlockedDiscards,
       "lpsBridgePortReceiveAllPathFilteredFrames": lpsBridgePortReceiveAllPathFilteredFrames,
       "lpsBridgePortReceiveMulticastPathFilteredFrames": lpsBridgePortReceiveMulticastPathFilteredFrames,
       "lpsBridgePortTransmitAllPathFilteredFrames": lpsBridgePortTransmitAllPathFilteredFrames,
       "lpsBridgePortTransmitMulticastPathFilteredFrames": lpsBridgePortTransmitMulticastPathFilteredFrames,
       "lpsBridgePortForwardedUnicastFrames": lpsBridgePortForwardedUnicastFrames,
       "lpsBridgePortForwardedUnicastOctets": lpsBridgePortForwardedUnicastOctets,
       "lpsBridgePortForwardedMulticastFrames": lpsBridgePortForwardedMulticastFrames,
       "lpsBridgePortForwardedMulticastOctets": lpsBridgePortForwardedMulticastOctets,
       "lpsBridgePortFloodedUnicastFrames": lpsBridgePortFloodedUnicastFrames,
       "lpsBridgePortFloodedUnicastOctets": lpsBridgePortFloodedUnicastOctets,
       "lpsBridgePortPairTable": lpsBridgePortPairTable,
       "lpsBridgePortPairEntry": lpsBridgePortPairEntry,
       "lpsBridgePortPairBridgeIndex": lpsBridgePortPairBridgeIndex,
       "lpsBridgePortPairReceivePortIndex": lpsBridgePortPairReceivePortIndex,
       "lpsBridgePortPairDestinationPortIndex": lpsBridgePortPairDestinationPortIndex,
       "lpsBridgePortPairForwardedToUnicastFrames": lpsBridgePortPairForwardedToUnicastFrames,
       "lpsBridgePortPairForwardedToUnicastOctets": lpsBridgePortPairForwardedToUnicastOctets,
       "lpsBridgePortAddressTable": lpsBridgePortAddressTable,
       "lpsBridgePortAddressEntry": lpsBridgePortAddressEntry,
       "lpsBridgePortAddressBridgeIndex": lpsBridgePortAddressBridgeIndex,
       "lpsBridgePortAddressPortIndex": lpsBridgePortAddressPortIndex,
       "lpsBridgePortAddressIndex": lpsBridgePortAddressIndex,
       "lpsBridgePortAddressRemoteAddress": lpsBridgePortAddressRemoteAddress,
       "lpsBridgePortAddressType": lpsBridgePortAddressType,
       "lpsBridgePortAddressIsStatic": lpsBridgePortAddressIsStatic,
       "lpsBridgePortAddressStaticPort": lpsBridgePortAddressStaticPort,
       "lpsBridgePortAddressAge": lpsBridgePortAddressAge,
       "lpsBridgeStpGroupAddress": lpsBridgeStpGroupAddress,
       "lpsBridgeStpEnable": lpsBridgeStpEnable,
       "lpsIpRouter": lpsIpRouter,
       "lpsNetworkMonitor": lpsNetworkMonitor,
       "lpsNetworkAnalyzerTable": lpsNetworkAnalyzerTable,
       "lpsNetworkAnalyzerTableEntry": lpsNetworkAnalyzerTableEntry,
       "lpsNetworkAnalyzerBridgeIndex": lpsNetworkAnalyzerBridgeIndex,
       "lpsNetworkAnalyzerBridgePortIndex": lpsNetworkAnalyzerBridgePortIndex,
       "lpsNetworkAnalyzerPhysicalAddress": lpsNetworkAnalyzerPhysicalAddress,
       "lpsNetworkAnalyzerStatus": lpsNetworkAnalyzerStatus,
       "lpsNetworkPortMonitorTable": lpsNetworkPortMonitorTable,
       "lpsNetworkPortMonitorTableEntry": lpsNetworkPortMonitorTableEntry,
       "lpsNetworkPortMonitorBridgeIndex": lpsNetworkPortMonitorBridgeIndex,
       "lpsNetworkPortMonitorBridgePortIndex": lpsNetworkPortMonitorBridgePortIndex,
       "lpsNetworkPortMonitorAnalyzerAddress": lpsNetworkPortMonitorAnalyzerAddress,
       "lpsNetworkPortMonitorStatus": lpsNetworkPortMonitorStatus,
       "lpsTokenRingPort": lpsTokenRingPort,
       "lpsTokenRingPortCount": lpsTokenRingPortCount,
       "lpsTokenRingPortTable": lpsTokenRingPortTable,
       "lpsTokenRingPortEntry": lpsTokenRingPortEntry,
       "lpsTokenRingPortIndex": lpsTokenRingPortIndex,
       "lpsTokenRingPortIfIndex": lpsTokenRingPortIfIndex,
       "lpsTokenRingPortLabel": lpsTokenRingPortLabel,
       "lpsTokenRingPortInsertStatus": lpsTokenRingPortInsertStatus,
       "lpsTokenRingPortType": lpsTokenRingPortType,
       "lpsTokenRingPortMode": lpsTokenRingPortMode,
       "lpsTokenRingPortSpeed": lpsTokenRingPortSpeed,
       "lpsTokenRingPortLineErrors": lpsTokenRingPortLineErrors,
       "lpsTokenRingPortBurstErrors": lpsTokenRingPortBurstErrors,
       "lpsTokenRingPortACErrors": lpsTokenRingPortACErrors,
       "lpsTokenRingPortAbortTransErrors": lpsTokenRingPortAbortTransErrors,
       "lpsTokenRingPortInternalErrors": lpsTokenRingPortInternalErrors,
       "lpsTokenRingPortLostFrameErrors": lpsTokenRingPortLostFrameErrors,
       "lpsTokenRingPortReceiveCongestionErrors": lpsTokenRingPortReceiveCongestionErrors,
       "lpsTokenRingPortFrameCopiedErrors": lpsTokenRingPortFrameCopiedErrors,
       "lpsTokenRingPortTokenErrors": lpsTokenRingPortTokenErrors,
       "lpsTokenRingPortSoftErrors": lpsTokenRingPortSoftErrors,
       "lpsTokenRingPortHardErrors": lpsTokenRingPortHardErrors,
       "lpsTokenRingPortTransmitBeacons": lpsTokenRingPortTransmitBeacons,
       "lpsTokenRingPortLobeWires": lpsTokenRingPortLobeWires,
       "lpsTokenRingPortRemoves": lpsTokenRingPortRemoves,
       "lpsTokenRingPortSingles": lpsTokenRingPortSingles,
       "lpsTokenRingPortFreqErrors": lpsTokenRingPortFreqErrors,
       "lpsTokenRingPortRingStatus": lpsTokenRingPortRingStatus}
)
