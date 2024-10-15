# SNMP MIB module (SIEMENS-HP4KHIM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SIEMENS-HP4KHIM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:52:16 2024
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
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

hp4khim = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51)
)
hp4khim.setRevisions(
        ("2006-06-07 07:47",)
)


# Types definitions



class DiscoveryStates(Integer32):
    """Custom type DiscoveryStates based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("busy", 3),
          ("done", 1),
          ("error", 2),
          ("finerr", 5),
          ("finok", 4),
          ("kill", 6))
    )





class DiscoveryModes(Integer32):
    """Custom type DiscoveryModes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              9)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("man", 1),
          ("undef", 9))
    )




# TEXTUAL-CONVENTIONS



class HimPEN(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )



class HimPabxId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class HimSwitchNumber(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )



class HimYesNo(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("other", 0),
          ("yes", 1))
    )



class HimPhoneNumber(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 22),
    )



class HimShelfNWType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("apdl", 4),
          ("apnw", 3),
          ("flex", 1),
          ("local", 2),
          ("other", 0))
    )



# MIB Managed Objects in the order of their OIDs

_Siemens_ObjectIdentity = ObjectIdentity
siemens = _Siemens_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329)
)
_IandcAdmin_ObjectIdentity = ObjectIdentity
iandcAdmin = _IandcAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 2)
)
_HimWelcomePage_ObjectIdentity = ObjectIdentity
himWelcomePage = _HimWelcomePage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 1)
)
_HimWelPgTable_Object = MibTable
himWelPgTable = _HimWelPgTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 1, 1)
)
if mibBuilder.loadTexts:
    himWelPgTable.setStatus("current")
_HimWelPgEntry_Object = MibTableRow
himWelPgEntry = _HimWelPgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 1, 1, 1)
)
himWelPgEntry.setIndexNames(
    (0, "SIEMENS-HP4KHIM-MIB", "himWelPgPabxId"),
)
if mibBuilder.loadTexts:
    himWelPgEntry.setStatus("current")
_HimWelPgPabxId_Type = HimPabxId
_HimWelPgPabxId_Object = MibTableColumn
himWelPgPabxId = _HimWelPgPabxId_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 1, 1, 1, 1),
    _HimWelPgPabxId_Type()
)
himWelPgPabxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himWelPgPabxId.setStatus("current")
_HimWelPgSysNo_Type = HimSwitchNumber
_HimWelPgSysNo_Object = MibTableColumn
himWelPgSysNo = _HimWelPgSysNo_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 1, 1, 1, 2),
    _HimWelPgSysNo_Type()
)
himWelPgSysNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himWelPgSysNo.setStatus("current")


class _HimHP4KVersion_Type(OctetString):
    """Custom type himHP4KVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_HimHP4KVersion_Type.__name__ = "OctetString"
_HimHP4KVersion_Object = MibTableColumn
himHP4KVersion = _HimHP4KVersion_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 1, 1, 1, 3),
    _HimHP4KVersion_Type()
)
himHP4KVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himHP4KVersion.setStatus("current")


class _HimSystemRelease_Type(OctetString):
    """Custom type himSystemRelease based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_HimSystemRelease_Type.__name__ = "OctetString"
_HimSystemRelease_Object = MibTableColumn
himSystemRelease = _HimSystemRelease_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 1, 1, 1, 4),
    _HimSystemRelease_Type()
)
himSystemRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSystemRelease.setStatus("current")


class _HimRevisionLevel_Type(OctetString):
    """Custom type himRevisionLevel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_HimRevisionLevel_Type.__name__ = "OctetString"
_HimRevisionLevel_Object = MibTableColumn
himRevisionLevel = _HimRevisionLevel_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 1, 1, 1, 5),
    _HimRevisionLevel_Type()
)
himRevisionLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himRevisionLevel.setStatus("current")


class _HimHWArchitecture_Type(OctetString):
    """Custom type himHWArchitecture based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_HimHWArchitecture_Type.__name__ = "OctetString"
_HimHWArchitecture_Object = MibTableColumn
himHWArchitecture = _HimHWArchitecture_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 1, 1, 1, 6),
    _HimHWArchitecture_Type()
)
himHWArchitecture.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himHWArchitecture.setStatus("current")


class _HimHWArchitectureType_Type(OctetString):
    """Custom type himHWArchitectureType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_HimHWArchitectureType_Type.__name__ = "OctetString"
_HimHWArchitectureType_Object = MibTableColumn
himHWArchitectureType = _HimHWArchitectureType_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 1, 1, 1, 7),
    _HimHWArchitectureType_Type()
)
himHWArchitectureType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himHWArchitectureType.setStatus("current")


class _HimOperationMode_Type(OctetString):
    """Custom type himOperationMode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_HimOperationMode_Type.__name__ = "OctetString"
_HimOperationMode_Object = MibTableColumn
himOperationMode = _HimOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 1, 1, 1, 8),
    _HimOperationMode_Type()
)
himOperationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himOperationMode.setStatus("current")


class _HimSWUProc1_Type(OctetString):
    """Custom type himSWUProc1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_HimSWUProc1_Type.__name__ = "OctetString"
_HimSWUProc1_Object = MibTableColumn
himSWUProc1 = _HimSWUProc1_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 1, 1, 1, 9),
    _HimSWUProc1_Type()
)
himSWUProc1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSWUProc1.setStatus("current")


class _HimSWUMemory1_Type(OctetString):
    """Custom type himSWUMemory1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_HimSWUMemory1_Type.__name__ = "OctetString"
_HimSWUMemory1_Object = MibTableColumn
himSWUMemory1 = _HimSWUMemory1_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 1, 1, 1, 10),
    _HimSWUMemory1_Type()
)
himSWUMemory1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSWUMemory1.setStatus("current")


class _HimSWUProc2_Type(OctetString):
    """Custom type himSWUProc2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_HimSWUProc2_Type.__name__ = "OctetString"
_HimSWUProc2_Object = MibTableColumn
himSWUProc2 = _HimSWUProc2_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 1, 1, 1, 11),
    _HimSWUProc2_Type()
)
himSWUProc2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSWUProc2.setStatus("current")


class _HimSWUMemory2_Type(OctetString):
    """Custom type himSWUMemory2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_HimSWUMemory2_Type.__name__ = "OctetString"
_HimSWUMemory2_Object = MibTableColumn
himSWUMemory2 = _HimSWUMemory2_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 1, 1, 1, 12),
    _HimSWUMemory2_Type()
)
himSWUMemory2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSWUMemory2.setStatus("current")
_HimSwitchData_ObjectIdentity = ObjectIdentity
himSwitchData = _HimSwitchData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 2)
)
_HimTechInfoTable_Object = MibTable
himTechInfoTable = _HimTechInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 2, 1)
)
if mibBuilder.loadTexts:
    himTechInfoTable.setStatus("current")
_HimTechInfoEntry_Object = MibTableRow
himTechInfoEntry = _HimTechInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 2, 1, 1)
)
himTechInfoEntry.setIndexNames(
    (0, "SIEMENS-HP4KHIM-MIB", "himTechInfoPabxId"),
    (0, "SIEMENS-HP4KHIM-MIB", "himTechInfoInfoNo"),
)
if mibBuilder.loadTexts:
    himTechInfoEntry.setStatus("current")
_HimTechInfoPabxId_Type = HimPabxId
_HimTechInfoPabxId_Object = MibTableColumn
himTechInfoPabxId = _HimTechInfoPabxId_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 2, 1, 1, 1),
    _HimTechInfoPabxId_Type()
)
himTechInfoPabxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himTechInfoPabxId.setStatus("current")


class _HimTechInfoInfoNo_Type(OctetString):
    """Custom type himTechInfoInfoNo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_HimTechInfoInfoNo_Type.__name__ = "OctetString"
_HimTechInfoInfoNo_Object = MibTableColumn
himTechInfoInfoNo = _HimTechInfoInfoNo_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 2, 1, 1, 2),
    _HimTechInfoInfoNo_Type()
)
himTechInfoInfoNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himTechInfoInfoNo.setStatus("current")


class _HimTechInfoDate_Type(OctetString):
    """Custom type himTechInfoDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_HimTechInfoDate_Type.__name__ = "OctetString"
_HimTechInfoDate_Object = MibTableColumn
himTechInfoDate = _HimTechInfoDate_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 2, 1, 1, 3),
    _HimTechInfoDate_Type()
)
himTechInfoDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himTechInfoDate.setStatus("current")


class _HimTechInfoTechnicalData_Type(OctetString):
    """Custom type himTechInfoTechnicalData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_HimTechInfoTechnicalData_Type.__name__ = "OctetString"
_HimTechInfoTechnicalData_Object = MibTableColumn
himTechInfoTechnicalData = _HimTechInfoTechnicalData_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 2, 1, 1, 4),
    _HimTechInfoTechnicalData_Type()
)
himTechInfoTechnicalData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himTechInfoTechnicalData.setStatus("current")


class _HimTechInfoNumber_Type(OctetString):
    """Custom type himTechInfoNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_HimTechInfoNumber_Type.__name__ = "OctetString"
_HimTechInfoNumber_Object = MibTableColumn
himTechInfoNumber = _HimTechInfoNumber_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 2, 1, 1, 5),
    _HimTechInfoNumber_Type()
)
himTechInfoNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himTechInfoNumber.setStatus("current")


class _HimTechInfoExtraText_Type(OctetString):
    """Custom type himTechInfoExtraText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_HimTechInfoExtraText_Type.__name__ = "OctetString"
_HimTechInfoExtraText_Object = MibTableColumn
himTechInfoExtraText = _HimTechInfoExtraText_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 2, 1, 1, 6),
    _HimTechInfoExtraText_Type()
)
himTechInfoExtraText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himTechInfoExtraText.setStatus("current")
_HimNotepadDataTable_Object = MibTable
himNotepadDataTable = _HimNotepadDataTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 2, 2)
)
if mibBuilder.loadTexts:
    himNotepadDataTable.setStatus("current")
_HimNotepadDataEntry_Object = MibTableRow
himNotepadDataEntry = _HimNotepadDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 2, 2, 1)
)
himNotepadDataEntry.setIndexNames(
    (0, "SIEMENS-HP4KHIM-MIB", "himNotepadDataPabxId"),
    (0, "SIEMENS-HP4KHIM-MIB", "himNotepadDataInfoNo"),
)
if mibBuilder.loadTexts:
    himNotepadDataEntry.setStatus("current")
_HimNotepadDataPabxId_Type = HimPabxId
_HimNotepadDataPabxId_Object = MibTableColumn
himNotepadDataPabxId = _HimNotepadDataPabxId_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 2, 2, 1, 1),
    _HimNotepadDataPabxId_Type()
)
himNotepadDataPabxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himNotepadDataPabxId.setStatus("current")
_HimNotepadDataInfoNo_Type = Unsigned32
_HimNotepadDataInfoNo_Object = MibTableColumn
himNotepadDataInfoNo = _HimNotepadDataInfoNo_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 2, 2, 1, 2),
    _HimNotepadDataInfoNo_Type()
)
himNotepadDataInfoNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himNotepadDataInfoNo.setStatus("current")


class _HimNotepadDataDate_Type(OctetString):
    """Custom type himNotepadDataDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_HimNotepadDataDate_Type.__name__ = "OctetString"
_HimNotepadDataDate_Object = MibTableColumn
himNotepadDataDate = _HimNotepadDataDate_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 2, 2, 1, 3),
    _HimNotepadDataDate_Type()
)
himNotepadDataDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himNotepadDataDate.setStatus("current")


class _HimNotepadDataText_Type(OctetString):
    """Custom type himNotepadDataText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 77),
    )


_HimNotepadDataText_Type.__name__ = "OctetString"
_HimNotepadDataText_Object = MibTableColumn
himNotepadDataText = _HimNotepadDataText_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 2, 2, 1, 4),
    _HimNotepadDataText_Type()
)
himNotepadDataText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himNotepadDataText.setStatus("current")
_HimProjPlanInfoTable_Object = MibTable
himProjPlanInfoTable = _HimProjPlanInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 2, 3)
)
if mibBuilder.loadTexts:
    himProjPlanInfoTable.setStatus("current")
_HimProjPlanInfoEntry_Object = MibTableRow
himProjPlanInfoEntry = _HimProjPlanInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 2, 3, 1)
)
himProjPlanInfoEntry.setIndexNames(
    (0, "SIEMENS-HP4KHIM-MIB", "himProjPlanPabxId"),
)
if mibBuilder.loadTexts:
    himProjPlanInfoEntry.setStatus("current")
_HimProjPlanPabxId_Type = HimPabxId
_HimProjPlanPabxId_Object = MibTableColumn
himProjPlanPabxId = _HimProjPlanPabxId_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 2, 3, 1, 1),
    _HimProjPlanPabxId_Type()
)
himProjPlanPabxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himProjPlanPabxId.setStatus("current")


class _HimProjPlanInfoFile_Type(OctetString):
    """Custom type himProjPlanInfoFile based on OctetString"""
    defaultValue = OctetString("ProjPlan.txt")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_HimProjPlanInfoFile_Type.__name__ = "OctetString"
_HimProjPlanInfoFile_Object = MibTableColumn
himProjPlanInfoFile = _HimProjPlanInfoFile_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 2, 3, 1, 2),
    _HimProjPlanInfoFile_Type()
)
himProjPlanInfoFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himProjPlanInfoFile.setStatus("current")


class _HimProjPlanInfoCreationDate_Type(OctetString):
    """Custom type himProjPlanInfoCreationDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_HimProjPlanInfoCreationDate_Type.__name__ = "OctetString"
_HimProjPlanInfoCreationDate_Object = MibTableColumn
himProjPlanInfoCreationDate = _HimProjPlanInfoCreationDate_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 2, 3, 1, 3),
    _HimProjPlanInfoCreationDate_Type()
)
himProjPlanInfoCreationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himProjPlanInfoCreationDate.setStatus("current")


class _HimProjPlanInfoCreationTime_Type(OctetString):
    """Custom type himProjPlanInfoCreationTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_HimProjPlanInfoCreationTime_Type.__name__ = "OctetString"
_HimProjPlanInfoCreationTime_Object = MibTableColumn
himProjPlanInfoCreationTime = _HimProjPlanInfoCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 2, 3, 1, 4),
    _HimProjPlanInfoCreationTime_Type()
)
himProjPlanInfoCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himProjPlanInfoCreationTime.setStatus("current")
_HimSpecSwitchData_ObjectIdentity = ObjectIdentity
himSpecSwitchData = _HimSpecSwitchData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 3)
)
_HimSpecShelfDataTable_Object = MibTable
himSpecShelfDataTable = _HimSpecShelfDataTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 3, 1)
)
if mibBuilder.loadTexts:
    himSpecShelfDataTable.setStatus("current")
_HimSpecShelfDataEntry_Object = MibTableRow
himSpecShelfDataEntry = _HimSpecShelfDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 3, 1, 1)
)
himSpecShelfDataEntry.setIndexNames(
    (0, "SIEMENS-HP4KHIM-MIB", "himSpecShelfDataPabxId"),
    (0, "SIEMENS-HP4KHIM-MIB", "himSpecShelfDataAddress"),
)
if mibBuilder.loadTexts:
    himSpecShelfDataEntry.setStatus("current")
_HimSpecShelfDataPabxId_Type = HimPabxId
_HimSpecShelfDataPabxId_Object = MibTableColumn
himSpecShelfDataPabxId = _HimSpecShelfDataPabxId_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 3, 1, 1, 1),
    _HimSpecShelfDataPabxId_Type()
)
himSpecShelfDataPabxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSpecShelfDataPabxId.setStatus("current")


class _HimSpecShelfDataAddress_Type(OctetString):
    """Custom type himSpecShelfDataAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_HimSpecShelfDataAddress_Type.__name__ = "OctetString"
_HimSpecShelfDataAddress_Object = MibTableColumn
himSpecShelfDataAddress = _HimSpecShelfDataAddress_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 3, 1, 1, 2),
    _HimSpecShelfDataAddress_Type()
)
himSpecShelfDataAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSpecShelfDataAddress.setStatus("current")


class _HimSpecShelfDataFrameType_Type(OctetString):
    """Custom type himSpecShelfDataFrameType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_HimSpecShelfDataFrameType_Type.__name__ = "OctetString"
_HimSpecShelfDataFrameType_Object = MibTableColumn
himSpecShelfDataFrameType = _HimSpecShelfDataFrameType_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 3, 1, 1, 3),
    _HimSpecShelfDataFrameType_Type()
)
himSpecShelfDataFrameType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSpecShelfDataFrameType.setStatus("current")


class _HimSpecShelfDataLTU_Type(Integer32):
    """Custom type himSpecShelfDataLTU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("ap370013", 10),
          ("ap37009", 9),
          ("cc40f", 2),
          ("cc80f", 4),
          ("cc80w", 3),
          ("ext-comp-x", 11),
          ("inch19", 8),
          ("l80xf", 5),
          ("l80xw", 6),
          ("ltuw", 7),
          ("other", 0),
          ("preatl", 1))
    )


_HimSpecShelfDataLTU_Type.__name__ = "Integer32"
_HimSpecShelfDataLTU_Object = MibTableColumn
himSpecShelfDataLTU = _HimSpecShelfDataLTU_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 3, 1, 1, 4),
    _HimSpecShelfDataLTU_Type()
)
himSpecShelfDataLTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSpecShelfDataLTU.setStatus("current")
_HimSpecShelfDataNetworkType_Type = HimShelfNWType
_HimSpecShelfDataNetworkType_Object = MibTableColumn
himSpecShelfDataNetworkType = _HimSpecShelfDataNetworkType_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 3, 1, 1, 5),
    _HimSpecShelfDataNetworkType_Type()
)
himSpecShelfDataNetworkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSpecShelfDataNetworkType.setStatus("current")
_HimSpecShelfDataNetworkAddress_Type = IpAddress
_HimSpecShelfDataNetworkAddress_Object = MibTableColumn
himSpecShelfDataNetworkAddress = _HimSpecShelfDataNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 3, 1, 1, 6),
    _HimSpecShelfDataNetworkAddress_Type()
)
himSpecShelfDataNetworkAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSpecShelfDataNetworkAddress.setStatus("current")


class _HimSpecShelfDataRemote_Type(OctetString):
    """Custom type himSpecShelfDataRemote based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_HimSpecShelfDataRemote_Type.__name__ = "OctetString"
_HimSpecShelfDataRemote_Object = MibTableColumn
himSpecShelfDataRemote = _HimSpecShelfDataRemote_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 3, 1, 1, 7),
    _HimSpecShelfDataRemote_Type()
)
himSpecShelfDataRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSpecShelfDataRemote.setStatus("current")


class _HimSpecShelfDataLocation_Type(OctetString):
    """Custom type himSpecShelfDataLocation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_HimSpecShelfDataLocation_Type.__name__ = "OctetString"
_HimSpecShelfDataLocation_Object = MibTableColumn
himSpecShelfDataLocation = _HimSpecShelfDataLocation_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 3, 1, 1, 8),
    _HimSpecShelfDataLocation_Type()
)
himSpecShelfDataLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSpecShelfDataLocation.setStatus("current")


class _HimSpecShelfDataLTUC_Type(OctetString):
    """Custom type himSpecShelfDataLTUC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_HimSpecShelfDataLTUC_Type.__name__ = "OctetString"
_HimSpecShelfDataLTUC_Object = MibTableColumn
himSpecShelfDataLTUC = _HimSpecShelfDataLTUC_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 3, 1, 1, 9),
    _HimSpecShelfDataLTUC_Type()
)
himSpecShelfDataLTUC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSpecShelfDataLTUC.setStatus("current")
_HimSWUBoardTable_Object = MibTable
himSWUBoardTable = _HimSWUBoardTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 3, 2)
)
if mibBuilder.loadTexts:
    himSWUBoardTable.setStatus("current")
_HimSWUBoardEntry_Object = MibTableRow
himSWUBoardEntry = _HimSWUBoardEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 3, 2, 1)
)
himSWUBoardEntry.setIndexNames(
    (0, "SIEMENS-HP4KHIM-MIB", "himSWUBoardPabxId"),
    (0, "SIEMENS-HP4KHIM-MIB", "himSWUBoardPEN"),
)
if mibBuilder.loadTexts:
    himSWUBoardEntry.setStatus("current")
_HimSWUBoardPabxId_Type = HimPabxId
_HimSWUBoardPabxId_Object = MibTableColumn
himSWUBoardPabxId = _HimSWUBoardPabxId_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 3, 2, 1, 1),
    _HimSWUBoardPabxId_Type()
)
himSWUBoardPabxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSWUBoardPabxId.setStatus("current")
_HimSWUBoardPEN_Type = HimPEN
_HimSWUBoardPEN_Object = MibTableColumn
himSWUBoardPEN = _HimSWUBoardPEN_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 3, 2, 1, 2),
    _HimSWUBoardPEN_Type()
)
himSWUBoardPEN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSWUBoardPEN.setStatus("current")


class _HimSWUBoardOverlayLTU_Type(OctetString):
    """Custom type himSWUBoardOverlayLTU based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_HimSWUBoardOverlayLTU_Type.__name__ = "OctetString"
_HimSWUBoardOverlayLTU_Object = MibTableColumn
himSWUBoardOverlayLTU = _HimSWUBoardOverlayLTU_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 3, 2, 1, 3),
    _HimSWUBoardOverlayLTU_Type()
)
himSWUBoardOverlayLTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSWUBoardOverlayLTU.setStatus("current")


class _HimSWUBoardType_Type(OctetString):
    """Custom type himSWUBoardType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_HimSWUBoardType_Type.__name__ = "OctetString"
_HimSWUBoardType_Object = MibTableColumn
himSWUBoardType = _HimSWUBoardType_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 3, 2, 1, 4),
    _HimSWUBoardType_Type()
)
himSWUBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSWUBoardType.setStatus("current")


class _HimSWUBoardNominal_Type(OctetString):
    """Custom type himSWUBoardNominal based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_HimSWUBoardNominal_Type.__name__ = "OctetString"
_HimSWUBoardNominal_Object = MibTableColumn
himSWUBoardNominal = _HimSWUBoardNominal_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 3, 2, 1, 5),
    _HimSWUBoardNominal_Type()
)
himSWUBoardNominal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSWUBoardNominal.setStatus("current")


class _HimSWUBoardActual_Type(OctetString):
    """Custom type himSWUBoardActual based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_HimSWUBoardActual_Type.__name__ = "OctetString"
_HimSWUBoardActual_Object = MibTableColumn
himSWUBoardActual = _HimSWUBoardActual_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 3, 2, 1, 6),
    _HimSWUBoardActual_Type()
)
himSWUBoardActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSWUBoardActual.setStatus("current")


class _HhimSWUBoardFirmware_Type(OctetString):
    """Custom type hhimSWUBoardFirmware based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_HhimSWUBoardFirmware_Type.__name__ = "OctetString"
_HhimSWUBoardFirmware_Object = MibTableColumn
hhimSWUBoardFirmware = _HhimSWUBoardFirmware_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 3, 2, 1, 7),
    _HhimSWUBoardFirmware_Type()
)
hhimSWUBoardFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hhimSWUBoardFirmware.setStatus("current")


class _HimSWUBoardRev_Type(OctetString):
    """Custom type himSWUBoardRev based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_HimSWUBoardRev_Type.__name__ = "OctetString"
_HimSWUBoardRev_Object = MibTableColumn
himSWUBoardRev = _HimSWUBoardRev_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 3, 2, 1, 8),
    _HimSWUBoardRev_Type()
)
himSWUBoardRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSWUBoardRev.setStatus("current")


class _HimSWUBoardFunctId_Type(OctetString):
    """Custom type himSWUBoardFunctId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_HimSWUBoardFunctId_Type.__name__ = "OctetString"
_HimSWUBoardFunctId_Object = MibTableColumn
himSWUBoardFunctId = _HimSWUBoardFunctId_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 3, 2, 1, 9),
    _HimSWUBoardFunctId_Type()
)
himSWUBoardFunctId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSWUBoardFunctId.setStatus("current")


class _HimSWUBoardMode_Type(OctetString):
    """Custom type himSWUBoardMode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_HimSWUBoardMode_Type.__name__ = "OctetString"
_HimSWUBoardMode_Object = MibTableColumn
himSWUBoardMode = _HimSWUBoardMode_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 3, 2, 1, 10),
    _HimSWUBoardMode_Type()
)
himSWUBoardMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSWUBoardMode.setStatus("current")


class _HimSWUBoardLWNo_Type(OctetString):
    """Custom type himSWUBoardLWNo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_HimSWUBoardLWNo_Type.__name__ = "OctetString"
_HimSWUBoardLWNo_Object = MibTableColumn
himSWUBoardLWNo = _HimSWUBoardLWNo_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 3, 2, 1, 11),
    _HimSWUBoardLWNo_Type()
)
himSWUBoardLWNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSWUBoardLWNo.setStatus("current")


class _HimSWUBoardLWInterVer_Type(OctetString):
    """Custom type himSWUBoardLWInterVer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_HimSWUBoardLWInterVer_Type.__name__ = "OctetString"
_HimSWUBoardLWInterVer_Object = MibTableColumn
himSWUBoardLWInterVer = _HimSWUBoardLWInterVer_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 3, 2, 1, 12),
    _HimSWUBoardLWInterVer_Type()
)
himSWUBoardLWInterVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSWUBoardLWInterVer.setStatus("current")


class _HimSWUBoardLWName_Type(OctetString):
    """Custom type himSWUBoardLWName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HimSWUBoardLWName_Type.__name__ = "OctetString"
_HimSWUBoardLWName_Object = MibTableColumn
himSWUBoardLWName = _HimSWUBoardLWName_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 3, 2, 1, 13),
    _HimSWUBoardLWName_Type()
)
himSWUBoardLWName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSWUBoardLWName.setStatus("current")


class _HimSWUBoardLWDate_Type(OctetString):
    """Custom type himSWUBoardLWDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_HimSWUBoardLWDate_Type.__name__ = "OctetString"
_HimSWUBoardLWDate_Object = MibTableColumn
himSWUBoardLWDate = _HimSWUBoardLWDate_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 3, 2, 1, 14),
    _HimSWUBoardLWDate_Type()
)
himSWUBoardLWDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSWUBoardLWDate.setStatus("current")
_HimSWUPeriphery_ObjectIdentity = ObjectIdentity
himSWUPeriphery = _HimSWUPeriphery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 4)
)
_HimPSIOAssTable_Object = MibTable
himPSIOAssTable = _HimPSIOAssTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 4, 1)
)
if mibBuilder.loadTexts:
    himPSIOAssTable.setStatus("current")
_HimPSIOAssEntry_Object = MibTableRow
himPSIOAssEntry = _HimPSIOAssEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 4, 1, 1)
)
himPSIOAssEntry.setIndexNames(
    (0, "SIEMENS-HP4KHIM-MIB", "himPSIOAssPabxId"),
    (0, "SIEMENS-HP4KHIM-MIB", "himPSIOAssPEN"),
)
if mibBuilder.loadTexts:
    himPSIOAssEntry.setStatus("current")
_HimPSIOAssPabxId_Type = HimPabxId
_HimPSIOAssPabxId_Object = MibTableColumn
himPSIOAssPabxId = _HimPSIOAssPabxId_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 4, 1, 1, 1),
    _HimPSIOAssPabxId_Type()
)
himPSIOAssPabxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himPSIOAssPabxId.setStatus("current")
_HimPSIOAssPEN_Type = HimPEN
_HimPSIOAssPEN_Object = MibTableColumn
himPSIOAssPEN = _HimPSIOAssPEN_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 4, 1, 1, 2),
    _HimPSIOAssPEN_Type()
)
himPSIOAssPEN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himPSIOAssPEN.setStatus("current")


class _HimPSIOAssAssembly_Type(OctetString):
    """Custom type himPSIOAssAssembly based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_HimPSIOAssAssembly_Type.__name__ = "OctetString"
_HimPSIOAssAssembly_Object = MibTableColumn
himPSIOAssAssembly = _HimPSIOAssAssembly_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 4, 1, 1, 3),
    _HimPSIOAssAssembly_Type()
)
himPSIOAssAssembly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himPSIOAssAssembly.setStatus("current")


class _HimPSIOAssActual_Type(OctetString):
    """Custom type himPSIOAssActual based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_HimPSIOAssActual_Type.__name__ = "OctetString"
_HimPSIOAssActual_Object = MibTableColumn
himPSIOAssActual = _HimPSIOAssActual_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 4, 1, 1, 4),
    _HimPSIOAssActual_Type()
)
himPSIOAssActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himPSIOAssActual.setStatus("current")


class _HimPSIOAssFirmware_Type(OctetString):
    """Custom type himPSIOAssFirmware based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_HimPSIOAssFirmware_Type.__name__ = "OctetString"
_HimPSIOAssFirmware_Object = MibTableColumn
himPSIOAssFirmware = _HimPSIOAssFirmware_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 4, 1, 1, 5),
    _HimPSIOAssFirmware_Type()
)
himPSIOAssFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himPSIOAssFirmware.setStatus("current")
_HimSerialLineTable_Object = MibTable
himSerialLineTable = _HimSerialLineTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 4, 2)
)
if mibBuilder.loadTexts:
    himSerialLineTable.setStatus("current")
_HimSerialLineEntry_Object = MibTableRow
himSerialLineEntry = _HimSerialLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 4, 2, 1)
)
himSerialLineEntry.setIndexNames(
    (0, "SIEMENS-HP4KHIM-MIB", "himSerialLinePabxId"),
    (0, "SIEMENS-HP4KHIM-MIB", "himSerialLineNumber"),
)
if mibBuilder.loadTexts:
    himSerialLineEntry.setStatus("current")
_HimSerialLinePabxId_Type = HimPabxId
_HimSerialLinePabxId_Object = MibTableColumn
himSerialLinePabxId = _HimSerialLinePabxId_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 4, 2, 1, 1),
    _HimSerialLinePabxId_Type()
)
himSerialLinePabxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSerialLinePabxId.setStatus("current")


class _HimSerialLineNumber_Type(Unsigned32):
    """Custom type himSerialLineNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 63),
    )


_HimSerialLineNumber_Type.__name__ = "Unsigned32"
_HimSerialLineNumber_Object = MibTableColumn
himSerialLineNumber = _HimSerialLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 4, 2, 1, 2),
    _HimSerialLineNumber_Type()
)
himSerialLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSerialLineNumber.setStatus("current")


class _HimSerialLineBoardType_Type(OctetString):
    """Custom type himSerialLineBoardType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_HimSerialLineBoardType_Type.__name__ = "OctetString"
_HimSerialLineBoardType_Object = MibTableColumn
himSerialLineBoardType = _HimSerialLineBoardType_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 4, 2, 1, 3),
    _HimSerialLineBoardType_Type()
)
himSerialLineBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSerialLineBoardType.setStatus("current")
_HimSerialLineSpeed_Type = Unsigned32
_HimSerialLineSpeed_Object = MibTableColumn
himSerialLineSpeed = _HimSerialLineSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 4, 2, 1, 4),
    _HimSerialLineSpeed_Type()
)
himSerialLineSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSerialLineSpeed.setStatus("current")


class _HimSerialLineLogDevName_Type(OctetString):
    """Custom type himSerialLineLogDevName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_HimSerialLineLogDevName_Type.__name__ = "OctetString"
_HimSerialLineLogDevName_Object = MibTableColumn
himSerialLineLogDevName = _HimSerialLineLogDevName_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 4, 2, 1, 5),
    _HimSerialLineLogDevName_Type()
)
himSerialLineLogDevName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSerialLineLogDevName.setStatus("current")


class _HimSerialLineDevType_Type(OctetString):
    """Custom type himSerialLineDevType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_HimSerialLineDevType_Type.__name__ = "OctetString"
_HimSerialLineDevType_Object = MibTableColumn
himSerialLineDevType = _HimSerialLineDevType_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 4, 2, 1, 6),
    _HimSerialLineDevType_Type()
)
himSerialLineDevType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSerialLineDevType.setStatus("current")


class _HimSerialLineType_Type(Integer32):
    """Custom type himSerialLineType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("asy", 1),
          ("other", 0),
          ("v24", 2))
    )


_HimSerialLineType_Type.__name__ = "Integer32"
_HimSerialLineType_Object = MibTableColumn
himSerialLineType = _HimSerialLineType_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 4, 2, 1, 7),
    _HimSerialLineType_Type()
)
himSerialLineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSerialLineType.setStatus("current")
_HimSCSIDevTable_Object = MibTable
himSCSIDevTable = _HimSCSIDevTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 4, 3)
)
if mibBuilder.loadTexts:
    himSCSIDevTable.setStatus("current")
_HimSCSIDevEntry_Object = MibTableRow
himSCSIDevEntry = _HimSCSIDevEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 4, 3, 1)
)
himSCSIDevEntry.setIndexNames(
    (0, "SIEMENS-HP4KHIM-MIB", "himSCSIDevPabxId"),
    (0, "SIEMENS-HP4KHIM-MIB", "himSCSIDevId"),
)
if mibBuilder.loadTexts:
    himSCSIDevEntry.setStatus("current")
_HimSCSIDevPabxId_Type = HimPabxId
_HimSCSIDevPabxId_Object = MibTableColumn
himSCSIDevPabxId = _HimSCSIDevPabxId_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 4, 3, 1, 1),
    _HimSCSIDevPabxId_Type()
)
himSCSIDevPabxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSCSIDevPabxId.setStatus("current")


class _HimSCSIDevId_Type(Unsigned32):
    """Custom type himSCSIDevId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HimSCSIDevId_Type.__name__ = "Unsigned32"
_HimSCSIDevId_Object = MibTableColumn
himSCSIDevId = _HimSCSIDevId_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 4, 3, 1, 2),
    _HimSCSIDevId_Type()
)
himSCSIDevId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSCSIDevId.setStatus("current")


class _HimSCSIDevType_Type(OctetString):
    """Custom type himSCSIDevType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 13),
    )


_HimSCSIDevType_Type.__name__ = "OctetString"
_HimSCSIDevType_Object = MibTableColumn
himSCSIDevType = _HimSCSIDevType_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 4, 3, 1, 3),
    _HimSCSIDevType_Type()
)
himSCSIDevType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSCSIDevType.setStatus("current")


class _HimSCSIDevName_Type(OctetString):
    """Custom type himSCSIDevName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_HimSCSIDevName_Type.__name__ = "OctetString"
_HimSCSIDevName_Object = MibTableColumn
himSCSIDevName = _HimSCSIDevName_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 4, 3, 1, 4),
    _HimSCSIDevName_Type()
)
himSCSIDevName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSCSIDevName.setStatus("current")


class _HimSCSIDevFirmware_Type(OctetString):
    """Custom type himSCSIDevFirmware based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_HimSCSIDevFirmware_Type.__name__ = "OctetString"
_HimSCSIDevFirmware_Object = MibTableColumn
himSCSIDevFirmware = _HimSCSIDevFirmware_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 4, 3, 1, 5),
    _HimSCSIDevFirmware_Type()
)
himSCSIDevFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSCSIDevFirmware.setStatus("current")


class _HimSCSIDevLoadDrive_Type(OctetString):
    """Custom type himSCSIDevLoadDrive based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_HimSCSIDevLoadDrive_Type.__name__ = "OctetString"
_HimSCSIDevLoadDrive_Object = MibTableColumn
himSCSIDevLoadDrive = _HimSCSIDevLoadDrive_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 4, 3, 1, 6),
    _HimSCSIDevLoadDrive_Type()
)
himSCSIDevLoadDrive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSCSIDevLoadDrive.setStatus("current")
_HimCentralSwitchData_ObjectIdentity = ObjectIdentity
himCentralSwitchData = _HimCentralSwitchData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 5)
)
_HimCabinetTable_Object = MibTable
himCabinetTable = _HimCabinetTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 5, 1)
)
if mibBuilder.loadTexts:
    himCabinetTable.setStatus("current")
_HimCabinetEntry_Object = MibTableRow
himCabinetEntry = _HimCabinetEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 5, 1, 1)
)
himCabinetEntry.setIndexNames(
    (0, "SIEMENS-HP4KHIM-MIB", "himCabPabxId"),
    (0, "SIEMENS-HP4KHIM-MIB", "himCabAddr"),
)
if mibBuilder.loadTexts:
    himCabinetEntry.setStatus("current")
_HimCabPabxId_Type = HimPabxId
_HimCabPabxId_Object = MibTableColumn
himCabPabxId = _HimCabPabxId_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 5, 1, 1, 1),
    _HimCabPabxId_Type()
)
himCabPabxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himCabPabxId.setStatus("current")


class _HimCabAddr_Type(OctetString):
    """Custom type himCabAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_HimCabAddr_Type.__name__ = "OctetString"
_HimCabAddr_Object = MibTableColumn
himCabAddr = _HimCabAddr_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 5, 1, 1, 2),
    _HimCabAddr_Type()
)
himCabAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himCabAddr.setStatus("current")


class _HimCabPhysAddr_Type(OctetString):
    """Custom type himCabPhysAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_HimCabPhysAddr_Type.__name__ = "OctetString"
_HimCabPhysAddr_Object = MibTableColumn
himCabPhysAddr = _HimCabPhysAddr_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 5, 1, 1, 3),
    _HimCabPhysAddr_Type()
)
himCabPhysAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himCabPhysAddr.setStatus("current")


class _HimCabCabinet_Type(OctetString):
    """Custom type himCabCabinet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_HimCabCabinet_Type.__name__ = "OctetString"
_HimCabCabinet_Object = MibTableColumn
himCabCabinet = _HimCabCabinet_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 5, 1, 1, 4),
    _HimCabCabinet_Type()
)
himCabCabinet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himCabCabinet.setStatus("current")


class _HimCabPartNo_Type(OctetString):
    """Custom type himCabPartNo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_HimCabPartNo_Type.__name__ = "OctetString"
_HimCabPartNo_Object = MibTableColumn
himCabPartNo = _HimCabPartNo_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 5, 1, 1, 5),
    _HimCabPartNo_Type()
)
himCabPartNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himCabPartNo.setStatus("current")


class _HimCabShelfNo_Type(Unsigned32):
    """Custom type himCabShelfNo based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_HimCabShelfNo_Type.__name__ = "Unsigned32"
_HimCabShelfNo_Object = MibTableColumn
himCabShelfNo = _HimCabShelfNo_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 5, 1, 1, 6),
    _HimCabShelfNo_Type()
)
himCabShelfNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himCabShelfNo.setStatus("current")


class _HimCabFrame_Type(OctetString):
    """Custom type himCabFrame based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_HimCabFrame_Type.__name__ = "OctetString"
_HimCabFrame_Object = MibTableColumn
himCabFrame = _HimCabFrame_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 5, 1, 1, 7),
    _HimCabFrame_Type()
)
himCabFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himCabFrame.setStatus("current")


class _HimCabPid1_Type(OctetString):
    """Custom type himCabPid1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_HimCabPid1_Type.__name__ = "OctetString"
_HimCabPid1_Object = MibTableColumn
himCabPid1 = _HimCabPid1_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 5, 1, 1, 8),
    _HimCabPid1_Type()
)
himCabPid1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himCabPid1.setStatus("current")


class _HimCabPid2_Type(OctetString):
    """Custom type himCabPid2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_HimCabPid2_Type.__name__ = "OctetString"
_HimCabPid2_Object = MibTableColumn
himCabPid2 = _HimCabPid2_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 5, 1, 1, 9),
    _HimCabPid2_Type()
)
himCabPid2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himCabPid2.setStatus("current")


class _HimCabPid3_Type(OctetString):
    """Custom type himCabPid3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_HimCabPid3_Type.__name__ = "OctetString"
_HimCabPid3_Object = MibTableColumn
himCabPid3 = _HimCabPid3_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 5, 1, 1, 10),
    _HimCabPid3_Type()
)
himCabPid3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himCabPid3.setStatus("current")


class _HimCabLTUNo_Type(OctetString):
    """Custom type himCabLTUNo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_HimCabLTUNo_Type.__name__ = "OctetString"
_HimCabLTUNo_Object = MibTableColumn
himCabLTUNo = _HimCabLTUNo_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 5, 1, 1, 11),
    _HimCabLTUNo_Type()
)
himCabLTUNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himCabLTUNo.setStatus("current")
_HimMemScalingTable_Object = MibTable
himMemScalingTable = _HimMemScalingTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 5, 2)
)
if mibBuilder.loadTexts:
    himMemScalingTable.setStatus("current")
_HimMemScalingEntry_Object = MibTableRow
himMemScalingEntry = _HimMemScalingEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 5, 2, 1)
)
himMemScalingEntry.setIndexNames(
    (0, "SIEMENS-HP4KHIM-MIB", "himMemScalingPabxId"),
    (0, "SIEMENS-HP4KHIM-MIB", "himMemScalingUnit"),
)
if mibBuilder.loadTexts:
    himMemScalingEntry.setStatus("current")
_HimMemScalingPabxId_Type = HimPabxId
_HimMemScalingPabxId_Object = MibTableColumn
himMemScalingPabxId = _HimMemScalingPabxId_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 5, 2, 1, 1),
    _HimMemScalingPabxId_Type()
)
himMemScalingPabxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himMemScalingPabxId.setStatus("current")


class _HimMemScalingUnit_Type(OctetString):
    """Custom type himMemScalingUnit based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_HimMemScalingUnit_Type.__name__ = "OctetString"
_HimMemScalingUnit_Object = MibTableColumn
himMemScalingUnit = _HimMemScalingUnit_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 5, 2, 1, 2),
    _HimMemScalingUnit_Type()
)
himMemScalingUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himMemScalingUnit.setStatus("current")
_HimMemScalingUsed_Type = Integer32
_HimMemScalingUsed_Object = MibTableColumn
himMemScalingUsed = _HimMemScalingUsed_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 5, 2, 1, 3),
    _HimMemScalingUsed_Type()
)
himMemScalingUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himMemScalingUsed.setStatus("current")
_HimMemScalingMaxUsed_Type = Integer32
_HimMemScalingMaxUsed_Object = MibTableColumn
himMemScalingMaxUsed = _HimMemScalingMaxUsed_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 5, 2, 1, 4),
    _HimMemScalingMaxUsed_Type()
)
himMemScalingMaxUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himMemScalingMaxUsed.setStatus("current")
_HimMemScalingAllocated_Type = Integer32
_HimMemScalingAllocated_Object = MibTableColumn
himMemScalingAllocated = _HimMemScalingAllocated_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 5, 2, 1, 5),
    _HimMemScalingAllocated_Type()
)
himMemScalingAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himMemScalingAllocated.setStatus("current")
_HimMemScalingStandard_Type = Integer32
_HimMemScalingStandard_Object = MibTableColumn
himMemScalingStandard = _HimMemScalingStandard_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 5, 2, 1, 6),
    _HimMemScalingStandard_Type()
)
himMemScalingStandard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himMemScalingStandard.setStatus("current")
_HimMemScalingSysMax_Type = Integer32
_HimMemScalingSysMax_Object = MibTableColumn
himMemScalingSysMax = _HimMemScalingSysMax_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 5, 2, 1, 7),
    _HimMemScalingSysMax_Type()
)
himMemScalingSysMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himMemScalingSysMax.setStatus("current")
_HimGeneralSwitchData_ObjectIdentity = ObjectIdentity
himGeneralSwitchData = _HimGeneralSwitchData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6)
)
_HimDBConfSys_ObjectIdentity = ObjectIdentity
himDBConfSys = _HimDBConfSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 1)
)
_HimDBConfSysTable_Object = MibTable
himDBConfSysTable = _HimDBConfSysTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 1, 1)
)
if mibBuilder.loadTexts:
    himDBConfSysTable.setStatus("current")
_HimDBConfSysEntry_Object = MibTableRow
himDBConfSysEntry = _HimDBConfSysEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 1, 1, 1)
)
himDBConfSysEntry.setIndexNames(
    (0, "SIEMENS-HP4KHIM-MIB", "himDBConfSysPabxId"),
)
if mibBuilder.loadTexts:
    himDBConfSysEntry.setStatus("current")
_HimDBConfSysPabxId_Type = HimPabxId
_HimDBConfSysPabxId_Object = MibTableColumn
himDBConfSysPabxId = _HimDBConfSysPabxId_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 1, 1, 1, 1),
    _HimDBConfSysPabxId_Type()
)
himDBConfSysPabxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himDBConfSysPabxId.setStatus("current")


class _HimDBConfSysClass1_Type(OctetString):
    """Custom type himDBConfSysClass1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_HimDBConfSysClass1_Type.__name__ = "OctetString"
_HimDBConfSysClass1_Object = MibTableColumn
himDBConfSysClass1 = _HimDBConfSysClass1_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 1, 1, 1, 2),
    _HimDBConfSysClass1_Type()
)
himDBConfSysClass1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himDBConfSysClass1.setStatus("current")


class _HimDBConfSysClass2_Type(OctetString):
    """Custom type himDBConfSysClass2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_HimDBConfSysClass2_Type.__name__ = "OctetString"
_HimDBConfSysClass2_Object = MibTableColumn
himDBConfSysClass2 = _HimDBConfSysClass2_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 1, 1, 1, 3),
    _HimDBConfSysClass2_Type()
)
himDBConfSysClass2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himDBConfSysClass2.setStatus("current")


class _HimDBConfSysHWAss1_Type(OctetString):
    """Custom type himDBConfSysHWAss1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_HimDBConfSysHWAss1_Type.__name__ = "OctetString"
_HimDBConfSysHWAss1_Object = MibTableColumn
himDBConfSysHWAss1 = _HimDBConfSysHWAss1_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 1, 1, 1, 4),
    _HimDBConfSysHWAss1_Type()
)
himDBConfSysHWAss1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himDBConfSysHWAss1.setStatus("current")


class _HimDBConfSysHWAss2_Type(OctetString):
    """Custom type himDBConfSysHWAss2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_HimDBConfSysHWAss2_Type.__name__ = "OctetString"
_HimDBConfSysHWAss2_Object = MibTableColumn
himDBConfSysHWAss2 = _HimDBConfSysHWAss2_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 1, 1, 1, 5),
    _HimDBConfSysHWAss2_Type()
)
himDBConfSysHWAss2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himDBConfSysHWAss2.setStatus("current")


class _HimDBConfSysDevLine1_Type(OctetString):
    """Custom type himDBConfSysDevLine1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_HimDBConfSysDevLine1_Type.__name__ = "OctetString"
_HimDBConfSysDevLine1_Object = MibTableColumn
himDBConfSysDevLine1 = _HimDBConfSysDevLine1_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 1, 1, 1, 6),
    _HimDBConfSysDevLine1_Type()
)
himDBConfSysDevLine1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himDBConfSysDevLine1.setStatus("current")


class _HimDBConfSysDevLine2_Type(OctetString):
    """Custom type himDBConfSysDevLine2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_HimDBConfSysDevLine2_Type.__name__ = "OctetString"
_HimDBConfSysDevLine2_Object = MibTableColumn
himDBConfSysDevLine2 = _HimDBConfSysDevLine2_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 1, 1, 1, 7),
    _HimDBConfSysDevLine2_Type()
)
himDBConfSysDevLine2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himDBConfSysDevLine2.setStatus("current")


class _HimDBConfSysOpMode_Type(Integer32):
    """Custom type himDBConfSysOpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("duplex", 2),
          ("other", 0),
          ("simplex", 1))
    )


_HimDBConfSysOpMode_Type.__name__ = "Integer32"
_HimDBConfSysOpMode_Object = MibTableColumn
himDBConfSysOpMode = _HimDBConfSysOpMode_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 1, 1, 1, 8),
    _HimDBConfSysOpMode_Type()
)
himDBConfSysOpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himDBConfSysOpMode.setStatus("current")


class _HimDBConfSysResType_Type(OctetString):
    """Custom type himDBConfSysResType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_HimDBConfSysResType_Type.__name__ = "OctetString"
_HimDBConfSysResType_Object = MibTableColumn
himDBConfSysResType = _HimDBConfSysResType_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 1, 1, 1, 9),
    _HimDBConfSysResType_Type()
)
himDBConfSysResType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himDBConfSysResType.setStatus("current")


class _HimDBConfSysHWArch_Type(OctetString):
    """Custom type himDBConfSysHWArch based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_HimDBConfSysHWArch_Type.__name__ = "OctetString"
_HimDBConfSysHWArch_Object = MibTableColumn
himDBConfSysHWArch = _HimDBConfSysHWArch_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 1, 1, 1, 10),
    _HimDBConfSysHWArch_Type()
)
himDBConfSysHWArch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himDBConfSysHWArch.setStatus("current")


class _HimDBConfSysHWArchType_Type(OctetString):
    """Custom type himDBConfSysHWArchType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_HimDBConfSysHWArchType_Type.__name__ = "OctetString"
_HimDBConfSysHWArchType_Object = MibTableColumn
himDBConfSysHWArchType = _HimDBConfSysHWArchType_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 1, 1, 1, 11),
    _HimDBConfSysHWArchType_Type()
)
himDBConfSysHWArchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himDBConfSysHWArchType.setStatus("current")
_HimDBConfSysNo_Type = HimSwitchNumber
_HimDBConfSysNo_Object = MibTableColumn
himDBConfSysNo = _HimDBConfSysNo_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 1, 1, 1, 12),
    _HimDBConfSysNo_Type()
)
himDBConfSysNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himDBConfSysNo.setStatus("current")


class _HimDBConfSysLoc_Type(Integer32):
    """Custom type himDBConfSysLoc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("customer", 1),
          ("other", 0),
          ("support", 2),
          ("testlab", 3))
    )


_HimDBConfSysLoc_Type.__name__ = "Integer32"
_HimDBConfSysLoc_Object = MibTableColumn
himDBConfSysLoc = _HimDBConfSysLoc_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 1, 1, 1, 13),
    _HimDBConfSysLoc_Type()
)
himDBConfSysLoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himDBConfSysLoc.setStatus("current")


class _HimDBConfSysBaseApp_Type(OctetString):
    """Custom type himDBConfSysBaseApp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_HimDBConfSysBaseApp_Type.__name__ = "OctetString"
_HimDBConfSysBaseApp_Object = MibTableColumn
himDBConfSysBaseApp = _HimDBConfSysBaseApp_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 1, 1, 1, 14),
    _HimDBConfSysBaseApp_Type()
)
himDBConfSysBaseApp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himDBConfSysBaseApp.setStatus("current")


class _HimDBConfSysDBApp_Type(OctetString):
    """Custom type himDBConfSysDBApp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_HimDBConfSysDBApp_Type.__name__ = "OctetString"
_HimDBConfSysDBApp_Object = MibTableColumn
himDBConfSysDBApp = _HimDBConfSysDBApp_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 1, 1, 1, 15),
    _HimDBConfSysDBApp_Type()
)
himDBConfSysDBApp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himDBConfSysDBApp.setStatus("current")


class _HimDBConfSysID_Type(OctetString):
    """Custom type himDBConfSysID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_HimDBConfSysID_Type.__name__ = "OctetString"
_HimDBConfSysID_Object = MibTableColumn
himDBConfSysID = _HimDBConfSysID_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 1, 1, 1, 16),
    _HimDBConfSysID_Type()
)
himDBConfSysID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himDBConfSysID.setStatus("current")
_HimDBConfHW_ObjectIdentity = ObjectIdentity
himDBConfHW = _HimDBConfHW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 2)
)
_HimDBConfHWTable_Object = MibTable
himDBConfHWTable = _HimDBConfHWTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 2, 1)
)
if mibBuilder.loadTexts:
    himDBConfHWTable.setStatus("current")
_HimDBConfHWEntry_Object = MibTableRow
himDBConfHWEntry = _HimDBConfHWEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 2, 1, 1)
)
himDBConfHWEntry.setIndexNames(
    (0, "SIEMENS-HP4KHIM-MIB", "himDBConfHWPabxId"),
)
if mibBuilder.loadTexts:
    himDBConfHWEntry.setStatus("current")
_HimDBConfHWPabxId_Type = HimPabxId
_HimDBConfHWPabxId_Object = MibTableColumn
himDBConfHWPabxId = _HimDBConfHWPabxId_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 2, 1, 1, 1),
    _HimDBConfHWPabxId_Type()
)
himDBConfHWPabxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himDBConfHWPabxId.setStatus("current")


class _HimDBConfHWLTG_Type(Integer32):
    """Custom type himDBConfHWLTG based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_HimDBConfHWLTG_Type.__name__ = "Integer32"
_HimDBConfHWLTG_Object = MibTableColumn
himDBConfHWLTG = _HimDBConfHWLTG_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 2, 1, 1, 2),
    _HimDBConfHWLTG_Type()
)
himDBConfHWLTG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himDBConfHWLTG.setStatus("current")


class _HimDBConfHWLTU_Type(Integer32):
    """Custom type himDBConfHWLTU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
        ValueRangeConstraint(17, 99),
    )


_HimDBConfHWLTU_Type.__name__ = "Integer32"
_HimDBConfHWLTU_Object = MibTableColumn
himDBConfHWLTU = _HimDBConfHWLTU_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 2, 1, 1, 3),
    _HimDBConfHWLTU_Type()
)
himDBConfHWLTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himDBConfHWLTU.setStatus("current")
_HimDBConfHWLines_Type = Integer32
_HimDBConfHWLines_Object = MibTableColumn
himDBConfHWLines = _HimDBConfHWLines_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 2, 1, 1, 4),
    _HimDBConfHWLines_Type()
)
himDBConfHWLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himDBConfHWLines.setStatus("current")
_HimDBConfHWPorts_Type = Integer32
_HimDBConfHWPorts_Object = MibTableColumn
himDBConfHWPorts = _HimDBConfHWPorts_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 2, 1, 1, 5),
    _HimDBConfHWPorts_Type()
)
himDBConfHWPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himDBConfHWPorts.setStatus("current")
_HimDBConfHWPBC_Type = Integer32
_HimDBConfHWPBC_Object = MibTableColumn
himDBConfHWPBC = _HimDBConfHWPBC_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 2, 1, 1, 6),
    _HimDBConfHWPBC_Type()
)
himDBConfHWPBC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himDBConfHWPBC.setStatus("current")
_HimDBConfHWMTSBdPerGSN_Type = Integer32
_HimDBConfHWMTSBdPerGSN_Object = MibTableColumn
himDBConfHWMTSBdPerGSN = _HimDBConfHWMTSBdPerGSN_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 2, 1, 1, 7),
    _HimDBConfHWMTSBdPerGSN_Type()
)
himDBConfHWMTSBdPerGSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himDBConfHWMTSBdPerGSN.setStatus("current")
_HimDBConfHWSIUPPerLTU_Type = Integer32
_HimDBConfHWSIUPPerLTU_Object = MibTableColumn
himDBConfHWSIUPPerLTU = _HimDBConfHWSIUPPerLTU_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 2, 1, 1, 8),
    _HimDBConfHWSIUPPerLTU_Type()
)
himDBConfHWSIUPPerLTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himDBConfHWSIUPPerLTU.setStatus("current")
_HimDBConfHWDIUCPerLTU_Type = Integer32
_HimDBConfHWDIUCPerLTU_Object = MibTableColumn
himDBConfHWDIUCPerLTU = _HimDBConfHWDIUCPerLTU_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 2, 1, 1, 9),
    _HimDBConfHWDIUCPerLTU_Type()
)
himDBConfHWDIUCPerLTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himDBConfHWDIUCPerLTU.setStatus("current")
_HimDBConfHWHwyPerMTSBd_Type = Integer32
_HimDBConfHWHwyPerMTSBd_Object = MibTableColumn
himDBConfHWHwyPerMTSBd = _HimDBConfHWHwyPerMTSBd_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 2, 1, 1, 10),
    _HimDBConfHWHwyPerMTSBd_Type()
)
himDBConfHWHwyPerMTSBd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himDBConfHWHwyPerMTSBd.setStatus("current")
_HimDBConfHWHDLCPerDCL_Type = Integer32
_HimDBConfHWHDLCPerDCL_Object = MibTableColumn
himDBConfHWHDLCPerDCL = _HimDBConfHWHDLCPerDCL_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 2, 1, 1, 11),
    _HimDBConfHWHDLCPerDCL_Type()
)
himDBConfHWHDLCPerDCL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himDBConfHWHDLCPerDCL.setStatus("current")
_HimDBConfHWPBCPerDCL_Type = Integer32
_HimDBConfHWPBCPerDCL_Object = MibTableColumn
himDBConfHWPBCPerDCL = _HimDBConfHWPBCPerDCL_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 2, 1, 1, 12),
    _HimDBConfHWPBCPerDCL_Type()
)
himDBConfHWPBCPerDCL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himDBConfHWPBCPerDCL.setStatus("current")
_HimDBConfHWStdSIULine_Type = Integer32
_HimDBConfHWStdSIULine_Object = MibTableColumn
himDBConfHWStdSIULine = _HimDBConfHWStdSIULine_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 2, 1, 1, 13),
    _HimDBConfHWStdSIULine_Type()
)
himDBConfHWStdSIULine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himDBConfHWStdSIULine.setStatus("current")
_HimDBConfHWConfLine_Type = Integer32
_HimDBConfHWConfLine_Object = MibTableColumn
himDBConfHWConfLine = _HimDBConfHWConfLine_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 2, 1, 1, 14),
    _HimDBConfHWConfLine_Type()
)
himDBConfHWConfLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himDBConfHWConfLine.setStatus("current")


class _HimDBConfHWDBDim_Type(OctetString):
    """Custom type himDBConfHWDBDim based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_HimDBConfHWDBDim_Type.__name__ = "OctetString"
_HimDBConfHWDBDim_Object = MibTableColumn
himDBConfHWDBDim = _HimDBConfHWDBDim_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 2, 1, 1, 15),
    _HimDBConfHWDBDim_Type()
)
himDBConfHWDBDim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himDBConfHWDBDim.setStatus("current")
_HimDBConfHWTableVer_Type = Integer32
_HimDBConfHWTableVer_Object = MibTableColumn
himDBConfHWTableVer = _HimDBConfHWTableVer_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 2, 1, 1, 16),
    _HimDBConfHWTableVer_Type()
)
himDBConfHWTableVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himDBConfHWTableVer.setStatus("current")
_HimHWData_ObjectIdentity = ObjectIdentity
himHWData = _HimHWData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 3)
)
_HimHWDataTable_Object = MibTable
himHWDataTable = _HimHWDataTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 3, 1)
)
if mibBuilder.loadTexts:
    himHWDataTable.setStatus("current")
_HimHWDataEntry_Object = MibTableRow
himHWDataEntry = _HimHWDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 3, 1, 1)
)
himHWDataEntry.setIndexNames(
    (0, "SIEMENS-HP4KHIM-MIB", "himHWDataPabxId"),
)
if mibBuilder.loadTexts:
    himHWDataEntry.setStatus("current")
_HimHWDataPabxId_Type = HimPabxId
_HimHWDataPabxId_Object = MibTableColumn
himHWDataPabxId = _HimHWDataPabxId_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 3, 1, 1, 1),
    _HimHWDataPabxId_Type()
)
himHWDataPabxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himHWDataPabxId.setStatus("current")


class _HimHWArch_Type(OctetString):
    """Custom type himHWArch based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_HimHWArch_Type.__name__ = "OctetString"
_HimHWArch_Object = MibTableColumn
himHWArch = _HimHWArch_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 3, 1, 1, 2),
    _HimHWArch_Type()
)
himHWArch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himHWArch.setStatus("current")


class _HimHWArchType_Type(OctetString):
    """Custom type himHWArchType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_HimHWArchType_Type.__name__ = "OctetString"
_HimHWArchType_Object = MibTableColumn
himHWArchType = _HimHWArchType_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 3, 1, 1, 3),
    _HimHWArchType_Type()
)
himHWArchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himHWArchType.setStatus("current")


class _HimHWOpMode_Type(OctetString):
    """Custom type himHWOpMode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_HimHWOpMode_Type.__name__ = "OctetString"
_HimHWOpMode_Object = MibTableColumn
himHWOpMode = _HimHWOpMode_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 3, 1, 1, 4),
    _HimHWOpMode_Type()
)
himHWOpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himHWOpMode.setStatus("current")


class _HimHWSWUProc1_Type(OctetString):
    """Custom type himHWSWUProc1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_HimHWSWUProc1_Type.__name__ = "OctetString"
_HimHWSWUProc1_Object = MibTableColumn
himHWSWUProc1 = _HimHWSWUProc1_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 3, 1, 1, 5),
    _HimHWSWUProc1_Type()
)
himHWSWUProc1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himHWSWUProc1.setStatus("current")


class _HimHWSWUMem1_Type(OctetString):
    """Custom type himHWSWUMem1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_HimHWSWUMem1_Type.__name__ = "OctetString"
_HimHWSWUMem1_Object = MibTableColumn
himHWSWUMem1 = _HimHWSWUMem1_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 3, 1, 1, 6),
    _HimHWSWUMem1_Type()
)
himHWSWUMem1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himHWSWUMem1.setStatus("current")


class _HimHWSWUProc2_Type(OctetString):
    """Custom type himHWSWUProc2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_HimHWSWUProc2_Type.__name__ = "OctetString"
_HimHWSWUProc2_Object = MibTableColumn
himHWSWUProc2 = _HimHWSWUProc2_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 3, 1, 1, 7),
    _HimHWSWUProc2_Type()
)
himHWSWUProc2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himHWSWUProc2.setStatus("current")


class _HimHWSWUMem2_Type(OctetString):
    """Custom type himHWSWUMem2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_HimHWSWUMem2_Type.__name__ = "OctetString"
_HimHWSWUMem2_Object = MibTableColumn
himHWSWUMem2 = _HimHWSWUMem2_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 3, 1, 1, 8),
    _HimHWSWUMem2_Type()
)
himHWSWUMem2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himHWSWUMem2.setStatus("current")


class _HimHWADPProc_Type(OctetString):
    """Custom type himHWADPProc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_HimHWADPProc_Type.__name__ = "OctetString"
_HimHWADPProc_Object = MibTableColumn
himHWADPProc = _HimHWADPProc_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 3, 1, 1, 9),
    _HimHWADPProc_Type()
)
himHWADPProc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himHWADPProc.setStatus("current")


class _HimHWADPMem_Type(OctetString):
    """Custom type himHWADPMem based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_HimHWADPMem_Type.__name__ = "OctetString"
_HimHWADPMem_Object = MibTableColumn
himHWADPMem = _HimHWADPMem_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 3, 1, 1, 10),
    _HimHWADPMem_Type()
)
himHWADPMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himHWADPMem.setStatus("current")
_HimLWDataOnCB_ObjectIdentity = ObjectIdentity
himLWDataOnCB = _HimLWDataOnCB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 4)
)
_HimLWDataOnCBTable_Object = MibTable
himLWDataOnCBTable = _HimLWDataOnCBTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 4, 1)
)
if mibBuilder.loadTexts:
    himLWDataOnCBTable.setStatus("current")
_HimLWDataOnCBEntry_Object = MibTableRow
himLWDataOnCBEntry = _HimLWDataOnCBEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 4, 1, 1)
)
himLWDataOnCBEntry.setIndexNames(
    (0, "SIEMENS-HP4KHIM-MIB", "himLWDataOnCBPabxId"),
)
if mibBuilder.loadTexts:
    himLWDataOnCBEntry.setStatus("current")
_HimLWDataOnCBPabxId_Type = HimPabxId
_HimLWDataOnCBPabxId_Object = MibTableColumn
himLWDataOnCBPabxId = _HimLWDataOnCBPabxId_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 4, 1, 1, 1),
    _HimLWDataOnCBPabxId_Type()
)
himLWDataOnCBPabxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himLWDataOnCBPabxId.setStatus("current")


class _HimLWOnCBAss_Type(OctetString):
    """Custom type himLWOnCBAss based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_HimLWOnCBAss_Type.__name__ = "OctetString"
_HimLWOnCBAss_Object = MibTableColumn
himLWOnCBAss = _HimLWOnCBAss_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 4, 1, 1, 2),
    _HimLWOnCBAss_Type()
)
himLWOnCBAss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himLWOnCBAss.setStatus("current")


class _HimLWOnCBPBCAddr_Type(OctetString):
    """Custom type himLWOnCBPBCAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_HimLWOnCBPBCAddr_Type.__name__ = "OctetString"
_HimLWOnCBPBCAddr_Object = MibTableColumn
himLWOnCBPBCAddr = _HimLWOnCBPBCAddr_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 4, 1, 1, 3),
    _HimLWOnCBPBCAddr_Type()
)
himLWOnCBPBCAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himLWOnCBPBCAddr.setStatus("current")


class _HimLWOnCBFileName_Type(OctetString):
    """Custom type himLWOnCBFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HimLWOnCBFileName_Type.__name__ = "OctetString"
_HimLWOnCBFileName_Object = MibTableColumn
himLWOnCBFileName = _HimLWOnCBFileName_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 4, 1, 1, 4),
    _HimLWOnCBFileName_Type()
)
himLWOnCBFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himLWOnCBFileName.setStatus("current")


class _HimLWOnCBProdTime_Type(OctetString):
    """Custom type himLWOnCBProdTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_HimLWOnCBProdTime_Type.__name__ = "OctetString"
_HimLWOnCBProdTime_Object = MibTableColumn
himLWOnCBProdTime = _HimLWOnCBProdTime_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 4, 1, 1, 5),
    _HimLWOnCBProdTime_Type()
)
himLWOnCBProdTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himLWOnCBProdTime.setStatus("current")
_HimLWDataOnProc_ObjectIdentity = ObjectIdentity
himLWDataOnProc = _HimLWDataOnProc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 5)
)
_HimLWOnProcTable_Object = MibTable
himLWOnProcTable = _HimLWOnProcTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 5, 1)
)
if mibBuilder.loadTexts:
    himLWOnProcTable.setStatus("current")
_HimLWOnProcEntry_Object = MibTableRow
himLWOnProcEntry = _HimLWOnProcEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 5, 1, 1)
)
himLWOnProcEntry.setIndexNames(
    (0, "SIEMENS-HP4KHIM-MIB", "himLWOnProcPabxId"),
    (0, "SIEMENS-HP4KHIM-MIB", "himLWOnProcAss"),
    (0, "SIEMENS-HP4KHIM-MIB", "himLWOnProcInfoType"),
)
if mibBuilder.loadTexts:
    himLWOnProcEntry.setStatus("current")
_HimLWOnProcPabxId_Type = HimPabxId
_HimLWOnProcPabxId_Object = MibTableColumn
himLWOnProcPabxId = _HimLWOnProcPabxId_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 5, 1, 1, 1),
    _HimLWOnProcPabxId_Type()
)
himLWOnProcPabxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himLWOnProcPabxId.setStatus("current")


class _HimLWOnProcAss_Type(OctetString):
    """Custom type himLWOnProcAss based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_HimLWOnProcAss_Type.__name__ = "OctetString"
_HimLWOnProcAss_Object = MibTableColumn
himLWOnProcAss = _HimLWOnProcAss_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 5, 1, 1, 2),
    _HimLWOnProcAss_Type()
)
himLWOnProcAss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himLWOnProcAss.setStatus("current")


class _HimLWOnProcInfoType_Type(OctetString):
    """Custom type himLWOnProcInfoType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_HimLWOnProcInfoType_Type.__name__ = "OctetString"
_HimLWOnProcInfoType_Object = MibTableColumn
himLWOnProcInfoType = _HimLWOnProcInfoType_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 5, 1, 1, 3),
    _HimLWOnProcInfoType_Type()
)
himLWOnProcInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himLWOnProcInfoType.setStatus("current")


class _HimLWOnProcLWId_Type(OctetString):
    """Custom type himLWOnProcLWId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_HimLWOnProcLWId_Type.__name__ = "OctetString"
_HimLWOnProcLWId_Object = MibTableColumn
himLWOnProcLWId = _HimLWOnProcLWId_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 5, 1, 1, 4),
    _HimLWOnProcLWId_Type()
)
himLWOnProcLWId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himLWOnProcLWId.setStatus("current")


class _HimLWOnProcLWIdCMP_Type(OctetString):
    """Custom type himLWOnProcLWIdCMP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_HimLWOnProcLWIdCMP_Type.__name__ = "OctetString"
_HimLWOnProcLWIdCMP_Object = MibTableColumn
himLWOnProcLWIdCMP = _HimLWOnProcLWIdCMP_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 5, 1, 1, 5),
    _HimLWOnProcLWIdCMP_Type()
)
himLWOnProcLWIdCMP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himLWOnProcLWIdCMP.setStatus("current")


class _HimLWOnProcLWIdLP_Type(OctetString):
    """Custom type himLWOnProcLWIdLP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_HimLWOnProcLWIdLP_Type.__name__ = "OctetString"
_HimLWOnProcLWIdLP_Object = MibTableColumn
himLWOnProcLWIdLP = _HimLWOnProcLWIdLP_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 5, 1, 1, 6),
    _HimLWOnProcLWIdLP_Type()
)
himLWOnProcLWIdLP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himLWOnProcLWIdLP.setStatus("current")
_HimLWDataOnCSIU_ObjectIdentity = ObjectIdentity
himLWDataOnCSIU = _HimLWDataOnCSIU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 6)
)
_HimLWOnCSIUTable_Object = MibTable
himLWOnCSIUTable = _HimLWOnCSIUTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 6, 1)
)
if mibBuilder.loadTexts:
    himLWOnCSIUTable.setStatus("current")
_HimLWOnCSIUEntry_Object = MibTableRow
himLWOnCSIUEntry = _HimLWOnCSIUEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 6, 1, 1)
)
himLWOnCSIUEntry.setIndexNames(
    (0, "SIEMENS-HP4KHIM-MIB", "himLWOnCSIUPabxId"),
    (0, "SIEMENS-HP4KHIM-MIB", "himLWOnCSIUNominal"),
    (0, "SIEMENS-HP4KHIM-MIB", "himLWOnCSIULWNo"),
)
if mibBuilder.loadTexts:
    himLWOnCSIUEntry.setStatus("current")
_HimLWOnCSIUPabxId_Type = HimPabxId
_HimLWOnCSIUPabxId_Object = MibTableColumn
himLWOnCSIUPabxId = _HimLWOnCSIUPabxId_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 6, 1, 1, 1),
    _HimLWOnCSIUPabxId_Type()
)
himLWOnCSIUPabxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himLWOnCSIUPabxId.setStatus("current")


class _HimLWOnCSIUNominal_Type(OctetString):
    """Custom type himLWOnCSIUNominal based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_HimLWOnCSIUNominal_Type.__name__ = "OctetString"
_HimLWOnCSIUNominal_Object = MibTableColumn
himLWOnCSIUNominal = _HimLWOnCSIUNominal_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 6, 1, 1, 2),
    _HimLWOnCSIUNominal_Type()
)
himLWOnCSIUNominal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himLWOnCSIUNominal.setStatus("current")


class _HimLWOnCSIULWNo_Type(OctetString):
    """Custom type himLWOnCSIULWNo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_HimLWOnCSIULWNo_Type.__name__ = "OctetString"
_HimLWOnCSIULWNo_Object = MibTableColumn
himLWOnCSIULWNo = _HimLWOnCSIULWNo_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 6, 1, 1, 3),
    _HimLWOnCSIULWNo_Type()
)
himLWOnCSIULWNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himLWOnCSIULWNo.setStatus("current")


class _HimLWOnCSIUProc_Type(OctetString):
    """Custom type himLWOnCSIUProc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_HimLWOnCSIUProc_Type.__name__ = "OctetString"
_HimLWOnCSIUProc_Object = MibTableColumn
himLWOnCSIUProc = _HimLWOnCSIUProc_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 6, 1, 1, 4),
    _HimLWOnCSIUProc_Type()
)
himLWOnCSIUProc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himLWOnCSIUProc.setStatus("current")


class _HimLWOnCSIUSlot_Type(OctetString):
    """Custom type himLWOnCSIUSlot based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_HimLWOnCSIUSlot_Type.__name__ = "OctetString"
_HimLWOnCSIUSlot_Object = MibTableColumn
himLWOnCSIUSlot = _HimLWOnCSIUSlot_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 6, 1, 1, 5),
    _HimLWOnCSIUSlot_Type()
)
himLWOnCSIUSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himLWOnCSIUSlot.setStatus("current")


class _HimLWOnCSIUActual_Type(OctetString):
    """Custom type himLWOnCSIUActual based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_HimLWOnCSIUActual_Type.__name__ = "OctetString"
_HimLWOnCSIUActual_Object = MibTableColumn
himLWOnCSIUActual = _HimLWOnCSIUActual_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 6, 1, 1, 6),
    _HimLWOnCSIUActual_Type()
)
himLWOnCSIUActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himLWOnCSIUActual.setStatus("current")


class _HimLWOnCSIUFileName_Type(OctetString):
    """Custom type himLWOnCSIUFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HimLWOnCSIUFileName_Type.__name__ = "OctetString"
_HimLWOnCSIUFileName_Object = MibTableColumn
himLWOnCSIUFileName = _HimLWOnCSIUFileName_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 6, 1, 1, 7),
    _HimLWOnCSIUFileName_Type()
)
himLWOnCSIUFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himLWOnCSIUFileName.setStatus("current")


class _HimLWOnCSIUFileProd_Type(OctetString):
    """Custom type himLWOnCSIUFileProd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_HimLWOnCSIUFileProd_Type.__name__ = "OctetString"
_HimLWOnCSIUFileProd_Object = MibTableColumn
himLWOnCSIUFileProd = _HimLWOnCSIUFileProd_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 6, 1, 1, 8),
    _HimLWOnCSIUFileProd_Type()
)
himLWOnCSIUFileProd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himLWOnCSIUFileProd.setStatus("current")
_HimMacAddress_ObjectIdentity = ObjectIdentity
himMacAddress = _HimMacAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 7)
)
_HimMacAddrTable_Object = MibTable
himMacAddrTable = _HimMacAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 7, 1)
)
if mibBuilder.loadTexts:
    himMacAddrTable.setStatus("current")
_HimMacAddrEntry_Object = MibTableRow
himMacAddrEntry = _HimMacAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 7, 1, 1)
)
himMacAddrEntry.setIndexNames(
    (0, "SIEMENS-HP4KHIM-MIB", "himMacAddrPabxId"),
    (0, "SIEMENS-HP4KHIM-MIB", "himMacAddrProc"),
    (0, "SIEMENS-HP4KHIM-MIB", "himMacAddrInfoType"),
)
if mibBuilder.loadTexts:
    himMacAddrEntry.setStatus("current")
_HimMacAddrPabxId_Type = HimPabxId
_HimMacAddrPabxId_Object = MibTableColumn
himMacAddrPabxId = _HimMacAddrPabxId_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 7, 1, 1, 1),
    _HimMacAddrPabxId_Type()
)
himMacAddrPabxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himMacAddrPabxId.setStatus("current")


class _HimMacAddrProc_Type(OctetString):
    """Custom type himMacAddrProc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_HimMacAddrProc_Type.__name__ = "OctetString"
_HimMacAddrProc_Object = MibTableColumn
himMacAddrProc = _HimMacAddrProc_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 7, 1, 1, 2),
    _HimMacAddrProc_Type()
)
himMacAddrProc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himMacAddrProc.setStatus("current")


class _HimMacAddrInfoType_Type(OctetString):
    """Custom type himMacAddrInfoType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_HimMacAddrInfoType_Type.__name__ = "OctetString"
_HimMacAddrInfoType_Object = MibTableColumn
himMacAddrInfoType = _HimMacAddrInfoType_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 7, 1, 1, 3),
    _HimMacAddrInfoType_Type()
)
himMacAddrInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himMacAddrInfoType.setStatus("current")
_HimMacAddrCLan_Type = MacAddress
_HimMacAddrCLan_Object = MibTableColumn
himMacAddrCLan = _HimMacAddrCLan_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 7, 1, 1, 4),
    _HimMacAddrCLan_Type()
)
himMacAddrCLan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himMacAddrCLan.setStatus("current")
_HimMacAddrIPDA_Type = MacAddress
_HimMacAddrIPDA_Object = MibTableColumn
himMacAddrIPDA = _HimMacAddrIPDA_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 6, 7, 1, 1, 5),
    _HimMacAddrIPDA_Type()
)
himMacAddrIPDA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himMacAddrIPDA.setStatus("current")
_HimFeatures_ObjectIdentity = ObjectIdentity
himFeatures = _HimFeatures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 7)
)
_HimMarketingFeatures_ObjectIdentity = ObjectIdentity
himMarketingFeatures = _HimMarketingFeatures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 7, 1)
)
_HimMarkFeatTable_Object = MibTable
himMarkFeatTable = _HimMarkFeatTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 7, 1, 1)
)
if mibBuilder.loadTexts:
    himMarkFeatTable.setStatus("current")
_HimMarkFeatEntry_Object = MibTableRow
himMarkFeatEntry = _HimMarkFeatEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 7, 1, 1, 1)
)
himMarkFeatEntry.setIndexNames(
    (0, "SIEMENS-HP4KHIM-MIB", "himMarkFeatPabxId"),
)
if mibBuilder.loadTexts:
    himMarkFeatEntry.setStatus("current")
_HimMarkFeatPabxId_Type = HimPabxId
_HimMarkFeatPabxId_Object = MibTableColumn
himMarkFeatPabxId = _HimMarkFeatPabxId_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 7, 1, 1, 1, 1),
    _HimMarkFeatPabxId_Type()
)
himMarkFeatPabxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himMarkFeatPabxId.setStatus("current")


class _HimMarkFeatVer_Type(OctetString):
    """Custom type himMarkFeatVer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_HimMarkFeatVer_Type.__name__ = "OctetString"
_HimMarkFeatVer_Object = MibTableColumn
himMarkFeatVer = _HimMarkFeatVer_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 7, 1, 1, 1, 2),
    _HimMarkFeatVer_Type()
)
himMarkFeatVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himMarkFeatVer.setStatus("current")


class _HimMarkFeatSerNo_Type(OctetString):
    """Custom type himMarkFeatSerNo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_HimMarkFeatSerNo_Type.__name__ = "OctetString"
_HimMarkFeatSerNo_Object = MibTableColumn
himMarkFeatSerNo = _HimMarkFeatSerNo_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 7, 1, 1, 1, 3),
    _HimMarkFeatSerNo_Type()
)
himMarkFeatSerNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himMarkFeatSerNo.setStatus("current")


class _HimMarkFeatHWId_Type(OctetString):
    """Custom type himMarkFeatHWId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_HimMarkFeatHWId_Type.__name__ = "OctetString"
_HimMarkFeatHWId_Object = MibTableColumn
himMarkFeatHWId = _HimMarkFeatHWId_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 7, 1, 1, 1, 4),
    _HimMarkFeatHWId_Type()
)
himMarkFeatHWId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himMarkFeatHWId.setStatus("current")


class _HimMarkFeatInstallDate_Type(OctetString):
    """Custom type himMarkFeatInstallDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_HimMarkFeatInstallDate_Type.__name__ = "OctetString"
_HimMarkFeatInstallDate_Object = MibTableColumn
himMarkFeatInstallDate = _HimMarkFeatInstallDate_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 7, 1, 1, 1, 5),
    _HimMarkFeatInstallDate_Type()
)
himMarkFeatInstallDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himMarkFeatInstallDate.setStatus("current")


class _HimMarkFeatExpiryDate_Type(OctetString):
    """Custom type himMarkFeatExpiryDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_HimMarkFeatExpiryDate_Type.__name__ = "OctetString"
_HimMarkFeatExpiryDate_Object = MibTableColumn
himMarkFeatExpiryDate = _HimMarkFeatExpiryDate_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 7, 1, 1, 1, 6),
    _HimMarkFeatExpiryDate_Type()
)
himMarkFeatExpiryDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himMarkFeatExpiryDate.setStatus("current")


class _HimMarkFeatConfCode_Type(OctetString):
    """Custom type himMarkFeatConfCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_HimMarkFeatConfCode_Type.__name__ = "OctetString"
_HimMarkFeatConfCode_Object = MibTableColumn
himMarkFeatConfCode = _HimMarkFeatConfCode_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 7, 1, 1, 1, 7),
    _HimMarkFeatConfCode_Type()
)
himMarkFeatConfCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himMarkFeatConfCode.setStatus("current")
_HimMarkFeatTrialModeAct_Type = HimYesNo
_HimMarkFeatTrialModeAct_Object = MibTableColumn
himMarkFeatTrialModeAct = _HimMarkFeatTrialModeAct_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 7, 1, 1, 1, 8),
    _HimMarkFeatTrialModeAct_Type()
)
himMarkFeatTrialModeAct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himMarkFeatTrialModeAct.setStatus("current")
_HimMarkFeatTrialRemDays_Type = Integer32
_HimMarkFeatTrialRemDays_Object = MibTableColumn
himMarkFeatTrialRemDays = _HimMarkFeatTrialRemDays_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 7, 1, 1, 1, 9),
    _HimMarkFeatTrialRemDays_Type()
)
himMarkFeatTrialRemDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himMarkFeatTrialRemDays.setStatus("current")
_HimSalesFeatTable_Object = MibTable
himSalesFeatTable = _HimSalesFeatTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 7, 1, 2)
)
if mibBuilder.loadTexts:
    himSalesFeatTable.setStatus("current")
_HimSalesFeatEntry_Object = MibTableRow
himSalesFeatEntry = _HimSalesFeatEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 7, 1, 2, 1)
)
himSalesFeatEntry.setIndexNames(
    (0, "SIEMENS-HP4KHIM-MIB", "himSalesFeatPabxId"),
    (0, "SIEMENS-HP4KHIM-MIB", "himSalesFeatMarketPackId"),
)
if mibBuilder.loadTexts:
    himSalesFeatEntry.setStatus("current")
_HimSalesFeatPabxId_Type = HimPabxId
_HimSalesFeatPabxId_Object = MibTableColumn
himSalesFeatPabxId = _HimSalesFeatPabxId_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 7, 1, 2, 1, 1),
    _HimSalesFeatPabxId_Type()
)
himSalesFeatPabxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSalesFeatPabxId.setStatus("current")


class _HimSalesFeatMarketPackId_Type(OctetString):
    """Custom type himSalesFeatMarketPackId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_HimSalesFeatMarketPackId_Type.__name__ = "OctetString"
_HimSalesFeatMarketPackId_Object = MibTableColumn
himSalesFeatMarketPackId = _HimSalesFeatMarketPackId_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 7, 1, 2, 1, 2),
    _HimSalesFeatMarketPackId_Type()
)
himSalesFeatMarketPackId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSalesFeatMarketPackId.setStatus("current")


class _HimSalesFeatMarketPack_Type(OctetString):
    """Custom type himSalesFeatMarketPack based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_HimSalesFeatMarketPack_Type.__name__ = "OctetString"
_HimSalesFeatMarketPack_Object = MibTableColumn
himSalesFeatMarketPack = _HimSalesFeatMarketPack_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 7, 1, 2, 1, 3),
    _HimSalesFeatMarketPack_Type()
)
himSalesFeatMarketPack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSalesFeatMarketPack.setStatus("current")


class _HimSalesFeatContract_Type(OctetString):
    """Custom type himSalesFeatContract based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_HimSalesFeatContract_Type.__name__ = "OctetString"
_HimSalesFeatContract_Object = MibTableColumn
himSalesFeatContract = _HimSalesFeatContract_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 7, 1, 2, 1, 4),
    _HimSalesFeatContract_Type()
)
himSalesFeatContract.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSalesFeatContract.setStatus("current")


class _HimSalesFeatUsed_Type(OctetString):
    """Custom type himSalesFeatUsed based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_HimSalesFeatUsed_Type.__name__ = "OctetString"
_HimSalesFeatUsed_Object = MibTableColumn
himSalesFeatUsed = _HimSalesFeatUsed_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 7, 1, 2, 1, 5),
    _HimSalesFeatUsed_Type()
)
himSalesFeatUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSalesFeatUsed.setStatus("current")


class _HimSalesFeatFree_Type(OctetString):
    """Custom type himSalesFeatFree based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_HimSalesFeatFree_Type.__name__ = "OctetString"
_HimSalesFeatFree_Object = MibTableColumn
himSalesFeatFree = _HimSalesFeatFree_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 7, 1, 2, 1, 6),
    _HimSalesFeatFree_Type()
)
himSalesFeatFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSalesFeatFree.setStatus("current")


class _HimSalesFeatMarkForTrial_Type(OctetString):
    """Custom type himSalesFeatMarkForTrial based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_HimSalesFeatMarkForTrial_Type.__name__ = "OctetString"
_HimSalesFeatMarkForTrial_Object = MibTableColumn
himSalesFeatMarkForTrial = _HimSalesFeatMarkForTrial_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 7, 1, 2, 1, 7),
    _HimSalesFeatMarkForTrial_Type()
)
himSalesFeatMarkForTrial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSalesFeatMarkForTrial.setStatus("current")
_HimTechFeatures_ObjectIdentity = ObjectIdentity
himTechFeatures = _HimTechFeatures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 7, 2)
)
_HimTechFeatTable_Object = MibTable
himTechFeatTable = _HimTechFeatTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 7, 2, 1)
)
if mibBuilder.loadTexts:
    himTechFeatTable.setStatus("current")
_HimTechFeatEntry_Object = MibTableRow
himTechFeatEntry = _HimTechFeatEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 7, 2, 1, 1)
)
himTechFeatEntry.setIndexNames(
    (0, "SIEMENS-HP4KHIM-MIB", "himTechFeatPabxId"),
    (0, "SIEMENS-HP4KHIM-MIB", "himTechFeatId"),
)
if mibBuilder.loadTexts:
    himTechFeatEntry.setStatus("current")
_HimTechFeatPabxId_Type = HimPabxId
_HimTechFeatPabxId_Object = MibTableColumn
himTechFeatPabxId = _HimTechFeatPabxId_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 7, 2, 1, 1, 1),
    _HimTechFeatPabxId_Type()
)
himTechFeatPabxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himTechFeatPabxId.setStatus("current")


class _HimTechFeatId_Type(OctetString):
    """Custom type himTechFeatId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_HimTechFeatId_Type.__name__ = "OctetString"
_HimTechFeatId_Object = MibTableColumn
himTechFeatId = _HimTechFeatId_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 7, 2, 1, 1, 2),
    _HimTechFeatId_Type()
)
himTechFeatId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himTechFeatId.setStatus("current")


class _HimTechFeatName_Type(OctetString):
    """Custom type himTechFeatName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 70),
    )


_HimTechFeatName_Type.__name__ = "OctetString"
_HimTechFeatName_Object = MibTableColumn
himTechFeatName = _HimTechFeatName_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 7, 2, 1, 1, 3),
    _HimTechFeatName_Type()
)
himTechFeatName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himTechFeatName.setStatus("current")
_HimTechFeatState_Type = HimYesNo
_HimTechFeatState_Object = MibTableColumn
himTechFeatState = _HimTechFeatState_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 7, 2, 1, 1, 4),
    _HimTechFeatState_Type()
)
himTechFeatState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himTechFeatState.setStatus("current")
_HimAPSPatches_ObjectIdentity = ObjectIdentity
himAPSPatches = _HimAPSPatches_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 8)
)
_HimSwitchAPS_ObjectIdentity = ObjectIdentity
himSwitchAPS = _HimSwitchAPS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 8, 1)
)
_HimSwitchAPSTable_Object = MibTable
himSwitchAPSTable = _HimSwitchAPSTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 8, 1, 1)
)
if mibBuilder.loadTexts:
    himSwitchAPSTable.setStatus("current")
_HimSwitchAPSEntry_Object = MibTableRow
himSwitchAPSEntry = _HimSwitchAPSEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 8, 1, 1, 1)
)
himSwitchAPSEntry.setIndexNames(
    (0, "SIEMENS-HP4KHIM-MIB", "himSwitchAPSPabxId"),
    (0, "SIEMENS-HP4KHIM-MIB", "himSwitchAPSName"),
)
if mibBuilder.loadTexts:
    himSwitchAPSEntry.setStatus("current")
_HimSwitchAPSPabxId_Type = HimPabxId
_HimSwitchAPSPabxId_Object = MibTableColumn
himSwitchAPSPabxId = _HimSwitchAPSPabxId_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 8, 1, 1, 1, 1),
    _HimSwitchAPSPabxId_Type()
)
himSwitchAPSPabxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSwitchAPSPabxId.setStatus("current")


class _HimSwitchAPSName_Type(OctetString):
    """Custom type himSwitchAPSName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_HimSwitchAPSName_Type.__name__ = "OctetString"
_HimSwitchAPSName_Object = MibTableColumn
himSwitchAPSName = _HimSwitchAPSName_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 8, 1, 1, 1, 2),
    _HimSwitchAPSName_Type()
)
himSwitchAPSName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSwitchAPSName.setStatus("current")


class _HimSwitchAPSCorrVer_Type(OctetString):
    """Custom type himSwitchAPSCorrVer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_HimSwitchAPSCorrVer_Type.__name__ = "OctetString"
_HimSwitchAPSCorrVer_Object = MibTableColumn
himSwitchAPSCorrVer = _HimSwitchAPSCorrVer_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 8, 1, 1, 1, 3),
    _HimSwitchAPSCorrVer_Type()
)
himSwitchAPSCorrVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSwitchAPSCorrVer.setStatus("current")


class _HimSwitchAPSPartNo_Type(OctetString):
    """Custom type himSwitchAPSPartNo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_HimSwitchAPSPartNo_Type.__name__ = "OctetString"
_HimSwitchAPSPartNo_Object = MibTableColumn
himSwitchAPSPartNo = _HimSwitchAPSPartNo_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 8, 1, 1, 1, 4),
    _HimSwitchAPSPartNo_Type()
)
himSwitchAPSPartNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSwitchAPSPartNo.setStatus("current")
_HimReplacedAMOs_ObjectIdentity = ObjectIdentity
himReplacedAMOs = _HimReplacedAMOs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 8, 2)
)
_HimReplAMOTable_Object = MibTable
himReplAMOTable = _HimReplAMOTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 8, 2, 1)
)
if mibBuilder.loadTexts:
    himReplAMOTable.setStatus("current")
_HimReplAMOEntry_Object = MibTableRow
himReplAMOEntry = _HimReplAMOEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 8, 2, 1, 1)
)
himReplAMOEntry.setIndexNames(
    (0, "SIEMENS-HP4KHIM-MIB", "himReplAMOPabxId"),
    (0, "SIEMENS-HP4KHIM-MIB", "himReplAMOAPS"),
    (0, "SIEMENS-HP4KHIM-MIB", "himReplAMOName"),
)
if mibBuilder.loadTexts:
    himReplAMOEntry.setStatus("current")
_HimReplAMOPabxId_Type = HimPabxId
_HimReplAMOPabxId_Object = MibTableColumn
himReplAMOPabxId = _HimReplAMOPabxId_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 8, 2, 1, 1, 1),
    _HimReplAMOPabxId_Type()
)
himReplAMOPabxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himReplAMOPabxId.setStatus("current")


class _HimReplAMOAPS_Type(OctetString):
    """Custom type himReplAMOAPS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_HimReplAMOAPS_Type.__name__ = "OctetString"
_HimReplAMOAPS_Object = MibTableColumn
himReplAMOAPS = _HimReplAMOAPS_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 8, 2, 1, 1, 2),
    _HimReplAMOAPS_Type()
)
himReplAMOAPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himReplAMOAPS.setStatus("current")


class _HimReplAMOName_Type(OctetString):
    """Custom type himReplAMOName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_HimReplAMOName_Type.__name__ = "OctetString"
_HimReplAMOName_Object = MibTableColumn
himReplAMOName = _HimReplAMOName_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 8, 2, 1, 1, 3),
    _HimReplAMOName_Type()
)
himReplAMOName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himReplAMOName.setStatus("current")


class _HimReplAMOInAPSDir_Type(OctetString):
    """Custom type himReplAMOInAPSDir based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 22),
    )


_HimReplAMOInAPSDir_Type.__name__ = "OctetString"
_HimReplAMOInAPSDir_Object = MibTableColumn
himReplAMOInAPSDir = _HimReplAMOInAPSDir_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 8, 2, 1, 1, 4),
    _HimReplAMOInAPSDir_Type()
)
himReplAMOInAPSDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himReplAMOInAPSDir.setStatus("current")


class _HimReplAMOSubsystem_Type(OctetString):
    """Custom type himReplAMOSubsystem based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 22),
    )


_HimReplAMOSubsystem_Type.__name__ = "OctetString"
_HimReplAMOSubsystem_Object = MibTableColumn
himReplAMOSubsystem = _HimReplAMOSubsystem_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 8, 2, 1, 1, 5),
    _HimReplAMOSubsystem_Type()
)
himReplAMOSubsystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himReplAMOSubsystem.setStatus("current")
_HimPatchInfo_ObjectIdentity = ObjectIdentity
himPatchInfo = _HimPatchInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 8, 3)
)
_HimPatchInfoTable_Object = MibTable
himPatchInfoTable = _HimPatchInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 8, 3, 1)
)
if mibBuilder.loadTexts:
    himPatchInfoTable.setStatus("current")
_HimPatchInfoEntry_Object = MibTableRow
himPatchInfoEntry = _HimPatchInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 8, 3, 1, 1)
)
himPatchInfoEntry.setIndexNames(
    (0, "SIEMENS-HP4KHIM-MIB", "himPatchInfoPabxId"),
    (0, "SIEMENS-HP4KHIM-MIB", "himPatchInfoPatchNo"),
)
if mibBuilder.loadTexts:
    himPatchInfoEntry.setStatus("current")
_HimPatchInfoPabxId_Type = HimPabxId
_HimPatchInfoPabxId_Object = MibTableColumn
himPatchInfoPabxId = _HimPatchInfoPabxId_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 8, 3, 1, 1, 1),
    _HimPatchInfoPabxId_Type()
)
himPatchInfoPabxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himPatchInfoPabxId.setStatus("current")


class _HimPatchInfoPatchNo_Type(OctetString):
    """Custom type himPatchInfoPatchNo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_HimPatchInfoPatchNo_Type.__name__ = "OctetString"
_HimPatchInfoPatchNo_Object = MibTableColumn
himPatchInfoPatchNo = _HimPatchInfoPatchNo_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 8, 3, 1, 1, 2),
    _HimPatchInfoPatchNo_Type()
)
himPatchInfoPatchNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himPatchInfoPatchNo.setStatus("current")


class _HimPatchInfoPatchGroup_Type(OctetString):
    """Custom type himPatchInfoPatchGroup based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_HimPatchInfoPatchGroup_Type.__name__ = "OctetString"
_HimPatchInfoPatchGroup_Object = MibTableColumn
himPatchInfoPatchGroup = _HimPatchInfoPatchGroup_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 8, 3, 1, 1, 3),
    _HimPatchInfoPatchGroup_Type()
)
himPatchInfoPatchGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himPatchInfoPatchGroup.setStatus("current")
_HimPatchInfoOpt_Type = HimYesNo
_HimPatchInfoOpt_Object = MibTableColumn
himPatchInfoOpt = _HimPatchInfoOpt_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 8, 3, 1, 1, 4),
    _HimPatchInfoOpt_Type()
)
himPatchInfoOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himPatchInfoOpt.setStatus("current")


class _HimPatchInfoActHD_Type(OctetString):
    """Custom type himPatchInfoActHD based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_HimPatchInfoActHD_Type.__name__ = "OctetString"
_HimPatchInfoActHD_Object = MibTableColumn
himPatchInfoActHD = _HimPatchInfoActHD_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 8, 3, 1, 1, 5),
    _HimPatchInfoActHD_Type()
)
himPatchInfoActHD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himPatchInfoActHD.setStatus("current")


class _HimPatchInfoActADP_Type(OctetString):
    """Custom type himPatchInfoActADP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_HimPatchInfoActADP_Type.__name__ = "OctetString"
_HimPatchInfoActADP_Object = MibTableColumn
himPatchInfoActADP = _HimPatchInfoActADP_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 8, 3, 1, 1, 6),
    _HimPatchInfoActADP_Type()
)
himPatchInfoActADP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himPatchInfoActADP.setStatus("current")


class _HimPatchInfoActBP_Type(OctetString):
    """Custom type himPatchInfoActBP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_HimPatchInfoActBP_Type.__name__ = "OctetString"
_HimPatchInfoActBP_Object = MibTableColumn
himPatchInfoActBP = _HimPatchInfoActBP_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 8, 3, 1, 1, 7),
    _HimPatchInfoActBP_Type()
)
himPatchInfoActBP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himPatchInfoActBP.setStatus("current")
_HimSWVersion_ObjectIdentity = ObjectIdentity
himSWVersion = _HimSWVersion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 9)
)
_HimSWVerOnProcTable_Object = MibTable
himSWVerOnProcTable = _HimSWVerOnProcTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 9, 1)
)
if mibBuilder.loadTexts:
    himSWVerOnProcTable.setStatus("current")
_HimSWVerOnProcEntry_Object = MibTableRow
himSWVerOnProcEntry = _HimSWVerOnProcEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 9, 1, 1)
)
himSWVerOnProcEntry.setIndexNames(
    (0, "SIEMENS-HP4KHIM-MIB", "himSWVerOnProcPabxId"),
    (0, "SIEMENS-HP4KHIM-MIB", "himSWVerOnProcSrc"),
)
if mibBuilder.loadTexts:
    himSWVerOnProcEntry.setStatus("current")
_HimSWVerOnProcPabxId_Type = HimPabxId
_HimSWVerOnProcPabxId_Object = MibTableColumn
himSWVerOnProcPabxId = _HimSWVerOnProcPabxId_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 9, 1, 1, 1),
    _HimSWVerOnProcPabxId_Type()
)
himSWVerOnProcPabxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSWVerOnProcPabxId.setStatus("current")


class _HimSWVerOnProcSrc_Type(OctetString):
    """Custom type himSWVerOnProcSrc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_HimSWVerOnProcSrc_Type.__name__ = "OctetString"
_HimSWVerOnProcSrc_Object = MibTableColumn
himSWVerOnProcSrc = _HimSWVerOnProcSrc_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 9, 1, 1, 2),
    _HimSWVerOnProcSrc_Type()
)
himSWVerOnProcSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSWVerOnProcSrc.setStatus("current")


class _HimSWVerOnProcSWVer_Type(OctetString):
    """Custom type himSWVerOnProcSWVer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_HimSWVerOnProcSWVer_Type.__name__ = "OctetString"
_HimSWVerOnProcSWVer_Object = MibTableColumn
himSWVerOnProcSWVer = _HimSWVerOnProcSWVer_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 9, 1, 1, 3),
    _HimSWVerOnProcSWVer_Type()
)
himSWVerOnProcSWVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSWVerOnProcSWVer.setStatus("current")


class _HimSWVerOnProcItemCodeNoPrefix_Type(OctetString):
    """Custom type himSWVerOnProcItemCodeNoPrefix based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_HimSWVerOnProcItemCodeNoPrefix_Type.__name__ = "OctetString"
_HimSWVerOnProcItemCodeNoPrefix_Object = MibTableColumn
himSWVerOnProcItemCodeNoPrefix = _HimSWVerOnProcItemCodeNoPrefix_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 9, 1, 1, 4),
    _HimSWVerOnProcItemCodeNoPrefix_Type()
)
himSWVerOnProcItemCodeNoPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSWVerOnProcItemCodeNoPrefix.setStatus("current")


class _HimSWVerOnProcHP4KVer_Type(OctetString):
    """Custom type himSWVerOnProcHP4KVer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_HimSWVerOnProcHP4KVer_Type.__name__ = "OctetString"
_HimSWVerOnProcHP4KVer_Object = MibTableColumn
himSWVerOnProcHP4KVer = _HimSWVerOnProcHP4KVer_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 9, 1, 1, 5),
    _HimSWVerOnProcHP4KVer_Type()
)
himSWVerOnProcHP4KVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSWVerOnProcHP4KVer.setStatus("current")


class _HimSWVerOnProcSysRel_Type(OctetString):
    """Custom type himSWVerOnProcSysRel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_HimSWVerOnProcSysRel_Type.__name__ = "OctetString"
_HimSWVerOnProcSysRel_Object = MibTableColumn
himSWVerOnProcSysRel = _HimSWVerOnProcSysRel_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 9, 1, 1, 6),
    _HimSWVerOnProcSysRel_Type()
)
himSWVerOnProcSysRel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSWVerOnProcSysRel.setStatus("current")


class _HimSWVerOnProcCountry_Type(OctetString):
    """Custom type himSWVerOnProcCountry based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_HimSWVerOnProcCountry_Type.__name__ = "OctetString"
_HimSWVerOnProcCountry_Object = MibTableColumn
himSWVerOnProcCountry = _HimSWVerOnProcCountry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 9, 1, 1, 7),
    _HimSWVerOnProcCountry_Type()
)
himSWVerOnProcCountry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSWVerOnProcCountry.setStatus("current")


class _HimSWVerOnProcCountryCode_Type(OctetString):
    """Custom type himSWVerOnProcCountryCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_HimSWVerOnProcCountryCode_Type.__name__ = "OctetString"
_HimSWVerOnProcCountryCode_Object = MibTableColumn
himSWVerOnProcCountryCode = _HimSWVerOnProcCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 9, 1, 1, 8),
    _HimSWVerOnProcCountryCode_Type()
)
himSWVerOnProcCountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSWVerOnProcCountryCode.setStatus("current")


class _HimSWVerOnProcRevNo_Type(OctetString):
    """Custom type himSWVerOnProcRevNo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_HimSWVerOnProcRevNo_Type.__name__ = "OctetString"
_HimSWVerOnProcRevNo_Object = MibTableColumn
himSWVerOnProcRevNo = _HimSWVerOnProcRevNo_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 9, 1, 1, 9),
    _HimSWVerOnProcRevNo_Type()
)
himSWVerOnProcRevNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSWVerOnProcRevNo.setStatus("current")
_HimSwPkgVersion_ObjectIdentity = ObjectIdentity
himSwPkgVersion = _HimSwPkgVersion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 10)
)
_HimSWPkgVerTable_Object = MibTable
himSWPkgVerTable = _HimSWPkgVerTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 10, 1)
)
if mibBuilder.loadTexts:
    himSWPkgVerTable.setStatus("current")
_HimSWPkgVerEntry_Object = MibTableRow
himSWPkgVerEntry = _HimSWPkgVerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 10, 1, 1)
)
himSWPkgVerEntry.setIndexNames(
    (0, "SIEMENS-HP4KHIM-MIB", "himSWPkgVerPabxId"),
    (0, "SIEMENS-HP4KHIM-MIB", "himSWPkgVerPkgAbbr"),
)
if mibBuilder.loadTexts:
    himSWPkgVerEntry.setStatus("current")
_HimSWPkgVerPabxId_Type = HimPabxId
_HimSWPkgVerPabxId_Object = MibTableColumn
himSWPkgVerPabxId = _HimSWPkgVerPabxId_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 10, 1, 1, 1),
    _HimSWPkgVerPabxId_Type()
)
himSWPkgVerPabxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSWPkgVerPabxId.setStatus("current")


class _HimSWPkgVerPkgAbbr_Type(OctetString):
    """Custom type himSWPkgVerPkgAbbr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HimSWPkgVerPkgAbbr_Type.__name__ = "OctetString"
_HimSWPkgVerPkgAbbr_Object = MibTableColumn
himSWPkgVerPkgAbbr = _HimSWPkgVerPkgAbbr_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 10, 1, 1, 2),
    _HimSWPkgVerPkgAbbr_Type()
)
himSWPkgVerPkgAbbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSWPkgVerPkgAbbr.setStatus("current")


class _HimSWPkgVerPkgName_Type(OctetString):
    """Custom type himSWPkgVerPkgName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_HimSWPkgVerPkgName_Type.__name__ = "OctetString"
_HimSWPkgVerPkgName_Object = MibTableColumn
himSWPkgVerPkgName = _HimSWPkgVerPkgName_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 10, 1, 1, 3),
    _HimSWPkgVerPkgName_Type()
)
himSWPkgVerPkgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSWPkgVerPkgName.setStatus("current")


class _HimSWPkgVerVersion_Type(OctetString):
    """Custom type himSWPkgVerVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_HimSWPkgVerVersion_Type.__name__ = "OctetString"
_HimSWPkgVerVersion_Object = MibTableColumn
himSWPkgVerVersion = _HimSWPkgVerVersion_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 10, 1, 1, 4),
    _HimSWPkgVerVersion_Type()
)
himSWPkgVerVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSWPkgVerVersion.setStatus("current")


class _HimSWPkgVerInstAt_Type(OctetString):
    """Custom type himSWPkgVerInstAt based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_HimSWPkgVerInstAt_Type.__name__ = "OctetString"
_HimSWPkgVerInstAt_Object = MibTableColumn
himSWPkgVerInstAt = _HimSWPkgVerInstAt_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 10, 1, 1, 5),
    _HimSWPkgVerInstAt_Type()
)
himSWPkgVerInstAt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSWPkgVerInstAt.setStatus("current")


class _HimSWPkgVerStatus_Type(Integer32):
    """Custom type himSWPkgVerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("complete", 2),
          ("other", 0),
          ("partial", 1))
    )


_HimSWPkgVerStatus_Type.__name__ = "Integer32"
_HimSWPkgVerStatus_Object = MibTableColumn
himSWPkgVerStatus = _HimSWPkgVerStatus_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 10, 1, 1, 6),
    _HimSWPkgVerStatus_Type()
)
himSWPkgVerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSWPkgVerStatus.setStatus("current")
_HimSystem_ObjectIdentity = ObjectIdentity
himSystem = _HimSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 11)
)
_HimSysBasicTable_Object = MibTable
himSysBasicTable = _HimSysBasicTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 11, 1)
)
if mibBuilder.loadTexts:
    himSysBasicTable.setStatus("current")
_HimSysBasicEntry_Object = MibTableRow
himSysBasicEntry = _HimSysBasicEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 11, 1, 1)
)
himSysBasicEntry.setIndexNames(
    (0, "SIEMENS-HP4KHIM-MIB", "himSysBasicPabxId"),
)
if mibBuilder.loadTexts:
    himSysBasicEntry.setStatus("current")
_HimSysBasicPabxId_Type = HimPabxId
_HimSysBasicPabxId_Object = MibTableColumn
himSysBasicPabxId = _HimSysBasicPabxId_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 11, 1, 1, 1),
    _HimSysBasicPabxId_Type()
)
himSysBasicPabxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSysBasicPabxId.setStatus("current")


class _HimSysBasicDomain_Type(OctetString):
    """Custom type himSysBasicDomain based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_HimSysBasicDomain_Type.__name__ = "OctetString"
_HimSysBasicDomain_Object = MibTableColumn
himSysBasicDomain = _HimSysBasicDomain_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 11, 1, 1, 2),
    _HimSysBasicDomain_Type()
)
himSysBasicDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSysBasicDomain.setStatus("current")


class _HimSysBasicNodeNo_Type(OctetString):
    """Custom type himSysBasicNodeNo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_HimSysBasicNodeNo_Type.__name__ = "OctetString"
_HimSysBasicNodeNo_Object = MibTableColumn
himSysBasicNodeNo = _HimSysBasicNodeNo_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 11, 1, 1, 3),
    _HimSysBasicNodeNo_Type()
)
himSysBasicNodeNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSysBasicNodeNo.setStatus("current")
_HimSysBasicLEGK_Type = HimYesNo
_HimSysBasicLEGK_Object = MibTableColumn
himSysBasicLEGK = _HimSysBasicLEGK_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 11, 1, 1, 4),
    _HimSysBasicLEGK_Type()
)
himSysBasicLEGK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSysBasicLEGK.setStatus("current")
_HimSysLANCardsTable_Object = MibTable
himSysLANCardsTable = _HimSysLANCardsTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 11, 2)
)
if mibBuilder.loadTexts:
    himSysLANCardsTable.setStatus("current")
_HimSysLANCardsEntry_Object = MibTableRow
himSysLANCardsEntry = _HimSysLANCardsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 11, 2, 1)
)
himSysLANCardsEntry.setIndexNames(
    (0, "SIEMENS-HP4KHIM-MIB", "himSysLANCardsPabxId"),
    (0, "SIEMENS-HP4KHIM-MIB", "himSysLANCardsIPAddr"),
)
if mibBuilder.loadTexts:
    himSysLANCardsEntry.setStatus("current")
_HimSysLANCardsPabxId_Type = HimPabxId
_HimSysLANCardsPabxId_Object = MibTableColumn
himSysLANCardsPabxId = _HimSysLANCardsPabxId_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 11, 2, 1, 1),
    _HimSysLANCardsPabxId_Type()
)
himSysLANCardsPabxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSysLANCardsPabxId.setStatus("current")
_HimSysLANCardsIPAddr_Type = IpAddress
_HimSysLANCardsIPAddr_Object = MibTableColumn
himSysLANCardsIPAddr = _HimSysLANCardsIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 11, 2, 1, 2),
    _HimSysLANCardsIPAddr_Type()
)
himSysLANCardsIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSysLANCardsIPAddr.setStatus("current")
_HimSysLANCardsNetMask_Type = IpAddress
_HimSysLANCardsNetMask_Object = MibTableColumn
himSysLANCardsNetMask = _HimSysLANCardsNetMask_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 11, 2, 1, 3),
    _HimSysLANCardsNetMask_Type()
)
himSysLANCardsNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSysLANCardsNetMask.setStatus("current")
_HimSysLANCardsBroadCast_Type = IpAddress
_HimSysLANCardsBroadCast_Object = MibTableColumn
himSysLANCardsBroadCast = _HimSysLANCardsBroadCast_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 11, 2, 1, 4),
    _HimSysLANCardsBroadCast_Type()
)
himSysLANCardsBroadCast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSysLANCardsBroadCast.setStatus("current")


class _HimSysLANCardsType_Type(Integer32):
    """Custom type himSysLANCardsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 1),
          ("other", 0),
          ("tokenring", 2))
    )


_HimSysLANCardsType_Type.__name__ = "Integer32"
_HimSysLANCardsType_Object = MibTableColumn
himSysLANCardsType = _HimSysLANCardsType_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 11, 2, 1, 5),
    _HimSysLANCardsType_Type()
)
himSysLANCardsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSysLANCardsType.setStatus("current")


class _HimSysLANCardsStatus_Type(Integer32):
    """Custom type himSysLANCardsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("configured", 4),
          ("disabled", 2),
          ("enabled", 1),
          ("other", 0),
          ("stale", 3),
          ("unconfigured", 5))
    )


_HimSysLANCardsStatus_Type.__name__ = "Integer32"
_HimSysLANCardsStatus_Object = MibTableColumn
himSysLANCardsStatus = _HimSysLANCardsStatus_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 11, 2, 1, 6),
    _HimSysLANCardsStatus_Type()
)
himSysLANCardsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSysLANCardsStatus.setStatus("current")
_HimSysHostsTable_Object = MibTable
himSysHostsTable = _HimSysHostsTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 11, 3)
)
if mibBuilder.loadTexts:
    himSysHostsTable.setStatus("current")
_HimSysHostsEntry_Object = MibTableRow
himSysHostsEntry = _HimSysHostsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 11, 3, 1)
)
himSysHostsEntry.setIndexNames(
    (0, "SIEMENS-HP4KHIM-MIB", "himSysHostsPabxId"),
    (0, "SIEMENS-HP4KHIM-MIB", "himSysHostsNo"),
)
if mibBuilder.loadTexts:
    himSysHostsEntry.setStatus("current")
_HimSysHostsPabxId_Type = HimPabxId
_HimSysHostsPabxId_Object = MibTableColumn
himSysHostsPabxId = _HimSysHostsPabxId_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 11, 3, 1, 1),
    _HimSysHostsPabxId_Type()
)
himSysHostsPabxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSysHostsPabxId.setStatus("current")


class _HimSysHostsNo_Type(Integer32):
    """Custom type himSysHostsNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HimSysHostsNo_Type.__name__ = "Integer32"
_HimSysHostsNo_Object = MibTableColumn
himSysHostsNo = _HimSysHostsNo_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 11, 3, 1, 2),
    _HimSysHostsNo_Type()
)
himSysHostsNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSysHostsNo.setStatus("current")
_HimSysHostsIPAddr_Type = IpAddress
_HimSysHostsIPAddr_Object = MibTableColumn
himSysHostsIPAddr = _HimSysHostsIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 11, 3, 1, 3),
    _HimSysHostsIPAddr_Type()
)
himSysHostsIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSysHostsIPAddr.setStatus("current")


class _HimSysHostsName_Type(OctetString):
    """Custom type himSysHostsName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_HimSysHostsName_Type.__name__ = "OctetString"
_HimSysHostsName_Object = MibTableColumn
himSysHostsName = _HimSysHostsName_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 11, 3, 1, 4),
    _HimSysHostsName_Type()
)
himSysHostsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSysHostsName.setStatus("current")
_HimSysWAMLConn_ObjectIdentity = ObjectIdentity
himSysWAMLConn = _HimSysWAMLConn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 11, 4)
)
_HimSysWAMLConnTable_Object = MibTable
himSysWAMLConnTable = _HimSysWAMLConnTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 11, 4, 1)
)
if mibBuilder.loadTexts:
    himSysWAMLConnTable.setStatus("current")
_HimSysWAMLConnEntry_Object = MibTableRow
himSysWAMLConnEntry = _HimSysWAMLConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 11, 4, 1, 1)
)
himSysWAMLConnEntry.setIndexNames(
    (0, "SIEMENS-HP4KHIM-MIB", "himSysWAMLConnPabxId"),
    (0, "SIEMENS-HP4KHIM-MIB", "himSysWAMLConnLTG"),
    (0, "SIEMENS-HP4KHIM-MIB", "himSysWAMLConnLTU"),
    (0, "SIEMENS-HP4KHIM-MIB", "himSysWAMLConnSlot"),
)
if mibBuilder.loadTexts:
    himSysWAMLConnEntry.setStatus("current")
_HimSysWAMLConnPabxId_Type = HimPabxId
_HimSysWAMLConnPabxId_Object = MibTableColumn
himSysWAMLConnPabxId = _HimSysWAMLConnPabxId_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 11, 4, 1, 1, 1),
    _HimSysWAMLConnPabxId_Type()
)
himSysWAMLConnPabxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSysWAMLConnPabxId.setStatus("current")


class _HimSysWAMLConnLTG_Type(Integer32):
    """Custom type himSysWAMLConnLTG based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_HimSysWAMLConnLTG_Type.__name__ = "Integer32"
_HimSysWAMLConnLTG_Object = MibTableColumn
himSysWAMLConnLTG = _HimSysWAMLConnLTG_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 11, 4, 1, 1, 2),
    _HimSysWAMLConnLTG_Type()
)
himSysWAMLConnLTG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSysWAMLConnLTG.setStatus("current")


class _HimSysWAMLConnLTU_Type(Integer32):
    """Custom type himSysWAMLConnLTU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_HimSysWAMLConnLTU_Type.__name__ = "Integer32"
_HimSysWAMLConnLTU_Object = MibTableColumn
himSysWAMLConnLTU = _HimSysWAMLConnLTU_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 11, 4, 1, 1, 3),
    _HimSysWAMLConnLTU_Type()
)
himSysWAMLConnLTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSysWAMLConnLTU.setStatus("current")


class _HimSysWAMLConnSlot_Type(Integer32):
    """Custom type himSysWAMLConnSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 145),
    )


_HimSysWAMLConnSlot_Type.__name__ = "Integer32"
_HimSysWAMLConnSlot_Object = MibTableColumn
himSysWAMLConnSlot = _HimSysWAMLConnSlot_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 11, 4, 1, 1, 4),
    _HimSysWAMLConnSlot_Type()
)
himSysWAMLConnSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSysWAMLConnSlot.setStatus("current")
_HimSysWAMLConnRufNr_Type = HimPhoneNumber
_HimSysWAMLConnRufNr_Object = MibTableColumn
himSysWAMLConnRufNr = _HimSysWAMLConnRufNr_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 11, 4, 1, 1, 5),
    _HimSysWAMLConnRufNr_Type()
)
himSysWAMLConnRufNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSysWAMLConnRufNr.setStatus("current")
_HimSysWAMLConnBChl_Type = Unsigned32
_HimSysWAMLConnBChl_Object = MibTableColumn
himSysWAMLConnBChl = _HimSysWAMLConnBChl_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 11, 4, 1, 1, 6),
    _HimSysWAMLConnBChl_Type()
)
himSysWAMLConnBChl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSysWAMLConnBChl.setStatus("current")


class _HimSysWAMLConnStatus_Type(OctetString):
    """Custom type himSysWAMLConnStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_HimSysWAMLConnStatus_Type.__name__ = "OctetString"
_HimSysWAMLConnStatus_Object = MibTableColumn
himSysWAMLConnStatus = _HimSysWAMLConnStatus_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 11, 4, 1, 1, 7),
    _HimSysWAMLConnStatus_Type()
)
himSysWAMLConnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSysWAMLConnStatus.setStatus("current")
_HimSysWAMLConnIPTable_Object = MibTable
himSysWAMLConnIPTable = _HimSysWAMLConnIPTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 11, 4, 2)
)
if mibBuilder.loadTexts:
    himSysWAMLConnIPTable.setStatus("current")
_HimSysWAMLConnIPEntry_Object = MibTableRow
himSysWAMLConnIPEntry = _HimSysWAMLConnIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 11, 4, 2, 1)
)
himSysWAMLConnIPEntry.setIndexNames(
    (0, "SIEMENS-HP4KHIM-MIB", "himSysWAMLConnIPPabxId"),
    (0, "SIEMENS-HP4KHIM-MIB", "himSysWAMLConnIPLTG"),
    (0, "SIEMENS-HP4KHIM-MIB", "himSysWAMLConnIPLTU"),
    (0, "SIEMENS-HP4KHIM-MIB", "himSysWAMLConnIPSlot"),
    (0, "SIEMENS-HP4KHIM-MIB", "himSysWAMLConnIPIfName"),
)
if mibBuilder.loadTexts:
    himSysWAMLConnIPEntry.setStatus("current")
_HimSysWAMLConnIPPabxId_Type = HimPabxId
_HimSysWAMLConnIPPabxId_Object = MibTableColumn
himSysWAMLConnIPPabxId = _HimSysWAMLConnIPPabxId_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 11, 4, 2, 1, 1),
    _HimSysWAMLConnIPPabxId_Type()
)
himSysWAMLConnIPPabxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSysWAMLConnIPPabxId.setStatus("current")


class _HimSysWAMLConnIPLTG_Type(Integer32):
    """Custom type himSysWAMLConnIPLTG based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_HimSysWAMLConnIPLTG_Type.__name__ = "Integer32"
_HimSysWAMLConnIPLTG_Object = MibTableColumn
himSysWAMLConnIPLTG = _HimSysWAMLConnIPLTG_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 11, 4, 2, 1, 2),
    _HimSysWAMLConnIPLTG_Type()
)
himSysWAMLConnIPLTG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSysWAMLConnIPLTG.setStatus("current")


class _HimSysWAMLConnIPLTU_Type(Integer32):
    """Custom type himSysWAMLConnIPLTU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_HimSysWAMLConnIPLTU_Type.__name__ = "Integer32"
_HimSysWAMLConnIPLTU_Object = MibTableColumn
himSysWAMLConnIPLTU = _HimSysWAMLConnIPLTU_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 11, 4, 2, 1, 3),
    _HimSysWAMLConnIPLTU_Type()
)
himSysWAMLConnIPLTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSysWAMLConnIPLTU.setStatus("current")


class _HimSysWAMLConnIPSlot_Type(Integer32):
    """Custom type himSysWAMLConnIPSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 145),
    )


_HimSysWAMLConnIPSlot_Type.__name__ = "Integer32"
_HimSysWAMLConnIPSlot_Object = MibTableColumn
himSysWAMLConnIPSlot = _HimSysWAMLConnIPSlot_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 11, 4, 2, 1, 4),
    _HimSysWAMLConnIPSlot_Type()
)
himSysWAMLConnIPSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSysWAMLConnIPSlot.setStatus("current")


class _HimSysWAMLConnIPIfName_Type(OctetString):
    """Custom type himSysWAMLConnIPIfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_HimSysWAMLConnIPIfName_Type.__name__ = "OctetString"
_HimSysWAMLConnIPIfName_Object = MibTableColumn
himSysWAMLConnIPIfName = _HimSysWAMLConnIPIfName_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 11, 4, 2, 1, 5),
    _HimSysWAMLConnIPIfName_Type()
)
himSysWAMLConnIPIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSysWAMLConnIPIfName.setStatus("current")
_HimSysWAMLConnIPAddr_Type = IpAddress
_HimSysWAMLConnIPAddr_Object = MibTableColumn
himSysWAMLConnIPAddr = _HimSysWAMLConnIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 11, 4, 2, 1, 6),
    _HimSysWAMLConnIPAddr_Type()
)
himSysWAMLConnIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSysWAMLConnIPAddr.setStatus("current")
_HimSysWAMLConnIPNetMask_Type = IpAddress
_HimSysWAMLConnIPNetMask_Object = MibTableColumn
himSysWAMLConnIPNetMask = _HimSysWAMLConnIPNetMask_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 11, 4, 2, 1, 7),
    _HimSysWAMLConnIPNetMask_Type()
)
himSysWAMLConnIPNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSysWAMLConnIPNetMask.setStatus("current")
_HimBoards_ObjectIdentity = ObjectIdentity
himBoards = _HimBoards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 12)
)
_HimBoardBasicTable_Object = MibTable
himBoardBasicTable = _HimBoardBasicTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 12, 1)
)
if mibBuilder.loadTexts:
    himBoardBasicTable.setStatus("current")
_HimBoardBasicEntry_Object = MibTableRow
himBoardBasicEntry = _HimBoardBasicEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 12, 1, 1)
)
himBoardBasicEntry.setIndexNames(
    (0, "SIEMENS-HP4KHIM-MIB", "himBoardBasicPabxId"),
    (0, "SIEMENS-HP4KHIM-MIB", "himBoardBasicLTG"),
    (0, "SIEMENS-HP4KHIM-MIB", "himBoardBasicLTU"),
    (0, "SIEMENS-HP4KHIM-MIB", "himBoardBasicSlot"),
)
if mibBuilder.loadTexts:
    himBoardBasicEntry.setStatus("current")
_HimBoardBasicPabxId_Type = HimPabxId
_HimBoardBasicPabxId_Object = MibTableColumn
himBoardBasicPabxId = _HimBoardBasicPabxId_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 12, 1, 1, 1),
    _HimBoardBasicPabxId_Type()
)
himBoardBasicPabxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himBoardBasicPabxId.setStatus("current")


class _HimBoardBasicLTG_Type(Integer32):
    """Custom type himBoardBasicLTG based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_HimBoardBasicLTG_Type.__name__ = "Integer32"
_HimBoardBasicLTG_Object = MibTableColumn
himBoardBasicLTG = _HimBoardBasicLTG_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 12, 1, 1, 2),
    _HimBoardBasicLTG_Type()
)
himBoardBasicLTG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himBoardBasicLTG.setStatus("current")


class _HimBoardBasicLTU_Type(Integer32):
    """Custom type himBoardBasicLTU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_HimBoardBasicLTU_Type.__name__ = "Integer32"
_HimBoardBasicLTU_Object = MibTableColumn
himBoardBasicLTU = _HimBoardBasicLTU_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 12, 1, 1, 3),
    _HimBoardBasicLTU_Type()
)
himBoardBasicLTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himBoardBasicLTU.setStatus("current")


class _HimBoardBasicSlot_Type(Integer32):
    """Custom type himBoardBasicSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 145),
    )


_HimBoardBasicSlot_Type.__name__ = "Integer32"
_HimBoardBasicSlot_Object = MibTableColumn
himBoardBasicSlot = _HimBoardBasicSlot_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 12, 1, 1, 4),
    _HimBoardBasicSlot_Type()
)
himBoardBasicSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himBoardBasicSlot.setStatus("current")


class _HimBoardBasicFuncId_Type(Integer32):
    """Custom type himBoardBasicFuncId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HimBoardBasicFuncId_Type.__name__ = "Integer32"
_HimBoardBasicFuncId_Object = MibTableColumn
himBoardBasicFuncId = _HimBoardBasicFuncId_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 12, 1, 1, 5),
    _HimBoardBasicFuncId_Type()
)
himBoardBasicFuncId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himBoardBasicFuncId.setStatus("current")


class _HimBoardBasicCat_Type(Integer32):
    """Custom type himBoardBasicCat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("acgen", 5),
          ("diu", 6),
          ("ipgw", 7),
          ("ltg", 1),
          ("ltu", 2),
          ("other", 0),
          ("per", 3),
          ("perhw", 4),
          ("rg", 8),
          ("siup", 9),
          ("tmd", 10))
    )


_HimBoardBasicCat_Type.__name__ = "Integer32"
_HimBoardBasicCat_Object = MibTableColumn
himBoardBasicCat = _HimBoardBasicCat_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 12, 1, 1, 6),
    _HimBoardBasicCat_Type()
)
himBoardBasicCat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himBoardBasicCat.setStatus("current")


class _HimBoardBasicName_Type(OctetString):
    """Custom type himBoardBasicName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_HimBoardBasicName_Type.__name__ = "OctetString"
_HimBoardBasicName_Object = MibTableColumn
himBoardBasicName = _HimBoardBasicName_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 12, 1, 1, 7),
    _HimBoardBasicName_Type()
)
himBoardBasicName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himBoardBasicName.setStatus("current")
_HimBoardBasicVOIPSec_Type = HimYesNo
_HimBoardBasicVOIPSec_Object = MibTableColumn
himBoardBasicVOIPSec = _HimBoardBasicVOIPSec_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 12, 1, 1, 8),
    _HimBoardBasicVOIPSec_Type()
)
himBoardBasicVOIPSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himBoardBasicVOIPSec.setStatus("current")


class _HimBoardBasicLWVar_Type(OctetString):
    """Custom type himBoardBasicLWVar based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_HimBoardBasicLWVar_Type.__name__ = "OctetString"
_HimBoardBasicLWVar_Object = MibTableColumn
himBoardBasicLWVar = _HimBoardBasicLWVar_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 12, 1, 1, 9),
    _HimBoardBasicLWVar_Type()
)
himBoardBasicLWVar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himBoardBasicLWVar.setStatus("current")


class _HimBoardBasicNoCirc_Type(Integer32):
    """Custom type himBoardBasicNoCirc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HimBoardBasicNoCirc_Type.__name__ = "Integer32"
_HimBoardBasicNoCirc_Object = MibTableColumn
himBoardBasicNoCirc = _HimBoardBasicNoCirc_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 12, 1, 1, 10),
    _HimBoardBasicNoCirc_Type()
)
himBoardBasicNoCirc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himBoardBasicNoCirc.setStatus("current")
_HimBoardIPTable_Object = MibTable
himBoardIPTable = _HimBoardIPTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 12, 2)
)
if mibBuilder.loadTexts:
    himBoardIPTable.setStatus("current")
_HimBoardIPEntry_Object = MibTableRow
himBoardIPEntry = _HimBoardIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 12, 2, 1)
)
if mibBuilder.loadTexts:
    himBoardIPEntry.setStatus("current")
_HimBoardIPGwyIPAddr_Type = IpAddress
_HimBoardIPGwyIPAddr_Object = MibTableColumn
himBoardIPGwyIPAddr = _HimBoardIPGwyIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 12, 2, 1, 1),
    _HimBoardIPGwyIPAddr_Type()
)
himBoardIPGwyIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himBoardIPGwyIPAddr.setStatus("current")
_HimBoardIPSrcIPAddr_Type = IpAddress
_HimBoardIPSrcIPAddr_Object = MibTableColumn
himBoardIPSrcIPAddr = _HimBoardIPSrcIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 12, 2, 1, 2),
    _HimBoardIPSrcIPAddr_Type()
)
himBoardIPSrcIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himBoardIPSrcIPAddr.setStatus("current")
_HimBoardIPNetMask_Type = IpAddress
_HimBoardIPNetMask_Object = MibTableColumn
himBoardIPNetMask = _HimBoardIPNetMask_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 12, 2, 1, 3),
    _HimBoardIPNetMask_Type()
)
himBoardIPNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himBoardIPNetMask.setStatus("current")
_HimBoardIPDefRouter_Type = IpAddress
_HimBoardIPDefRouter_Object = MibTableColumn
himBoardIPDefRouter = _HimBoardIPDefRouter_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 12, 2, 1, 4),
    _HimBoardIPDefRouter_Type()
)
himBoardIPDefRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himBoardIPDefRouter.setStatus("current")
_HimBoardIPCustLANIP_Type = IpAddress
_HimBoardIPCustLANIP_Object = MibTableColumn
himBoardIPCustLANIP = _HimBoardIPCustLANIP_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 12, 2, 1, 5),
    _HimBoardIPCustLANIP_Type()
)
himBoardIPCustLANIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himBoardIPCustLANIP.setStatus("current")
_HimBoardIPSTMI2IGWSubMask_Type = IpAddress
_HimBoardIPSTMI2IGWSubMask_Object = MibTableColumn
himBoardIPSTMI2IGWSubMask = _HimBoardIPSTMI2IGWSubMask_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 12, 2, 1, 6),
    _HimBoardIPSTMI2IGWSubMask_Type()
)
himBoardIPSTMI2IGWSubMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himBoardIPSTMI2IGWSubMask.setStatus("current")
_HimBoardIPDefGWIP_Type = IpAddress
_HimBoardIPDefGWIP_Object = MibTableColumn
himBoardIPDefGWIP = _HimBoardIPDefGWIP_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 12, 2, 1, 7),
    _HimBoardIPDefGWIP_Type()
)
himBoardIPDefGWIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himBoardIPDefGWIP.setStatus("current")
_HimBoardIPManStatIP_Type = IpAddress
_HimBoardIPManStatIP_Object = MibTableColumn
himBoardIPManStatIP = _HimBoardIPManStatIP_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 12, 2, 1, 8),
    _HimBoardIPManStatIP_Type()
)
himBoardIPManStatIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himBoardIPManStatIP.setStatus("current")


class _HimBoardIPManStatPort_Type(Integer32):
    """Custom type himBoardIPManStatPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_HimBoardIPManStatPort_Type.__name__ = "Integer32"
_HimBoardIPManStatPort_Object = MibTableColumn
himBoardIPManStatPort = _HimBoardIPManStatPort_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 12, 2, 1, 9),
    _HimBoardIPManStatPort_Type()
)
himBoardIPManStatPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himBoardIPManStatPort.setStatus("current")
_HimBoardIPBckpServIP_Type = IpAddress
_HimBoardIPBckpServIP_Object = MibTableColumn
himBoardIPBckpServIP = _HimBoardIPBckpServIP_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 12, 2, 1, 10),
    _HimBoardIPBckpServIP_Type()
)
himBoardIPBckpServIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himBoardIPBckpServIP.setStatus("current")


class _HimBoardIPBckpServPort_Type(Integer32):
    """Custom type himBoardIPBckpServPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HimBoardIPBckpServPort_Type.__name__ = "Integer32"
_HimBoardIPBckpServPort_Object = MibTableColumn
himBoardIPBckpServPort = _HimBoardIPBckpServPort_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 12, 2, 1, 11),
    _HimBoardIPBckpServPort_Type()
)
himBoardIPBckpServPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himBoardIPBckpServPort.setStatus("current")
_HimBoardLocTable_Object = MibTable
himBoardLocTable = _HimBoardLocTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 12, 3)
)
if mibBuilder.loadTexts:
    himBoardLocTable.setStatus("current")
_HimBoardLocEntry_Object = MibTableRow
himBoardLocEntry = _HimBoardLocEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 12, 3, 1)
)
himBoardLocEntry.setIndexNames(
    (0, "SIEMENS-HP4KHIM-MIB", "himBoardBasicPabxId"),
    (0, "SIEMENS-HP4KHIM-MIB", "himBoardBasicLTG"),
    (0, "SIEMENS-HP4KHIM-MIB", "himBoardBasicLTU"),
    (0, "SIEMENS-HP4KHIM-MIB", "himBoardBasicSlot"),
)
if mibBuilder.loadTexts:
    himBoardLocEntry.setStatus("current")


class _HimBoardLocId_Type(Integer32):
    """Custom type himBoardLocId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_HimBoardLocId_Type.__name__ = "Integer32"
_HimBoardLocId_Object = MibTableColumn
himBoardLocId = _HimBoardLocId_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 12, 3, 1, 1),
    _HimBoardLocId_Type()
)
himBoardLocId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himBoardLocId.setStatus("current")


class _HimBoardLocLoc_Type(OctetString):
    """Custom type himBoardLocLoc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_HimBoardLocLoc_Type.__name__ = "OctetString"
_HimBoardLocLoc_Object = MibTableColumn
himBoardLocLoc = _HimBoardLocLoc_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 12, 3, 1, 2),
    _HimBoardLocLoc_Type()
)
himBoardLocLoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himBoardLocLoc.setStatus("current")
_HimBoardLocPhoneNo_Type = HimPhoneNumber
_HimBoardLocPhoneNo_Object = MibTableColumn
himBoardLocPhoneNo = _HimBoardLocPhoneNo_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 12, 3, 1, 3),
    _HimBoardLocPhoneNo_Type()
)
himBoardLocPhoneNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himBoardLocPhoneNo.setStatus("current")
_HimBoardLocFaxNo_Type = HimPhoneNumber
_HimBoardLocFaxNo_Object = MibTableColumn
himBoardLocFaxNo = _HimBoardLocFaxNo_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 12, 3, 1, 4),
    _HimBoardLocFaxNo_Type()
)
himBoardLocFaxNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himBoardLocFaxNo.setStatus("current")
_HimIPDA_ObjectIdentity = ObjectIdentity
himIPDA = _HimIPDA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 13)
)
_HimIPDAGenData_ObjectIdentity = ObjectIdentity
himIPDAGenData = _HimIPDAGenData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 13, 1)
)
_HimIPDAGenTable_Object = MibTable
himIPDAGenTable = _HimIPDAGenTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 13, 1, 1)
)
if mibBuilder.loadTexts:
    himIPDAGenTable.setStatus("current")
_HimIPDAGenEntry_Object = MibTableRow
himIPDAGenEntry = _HimIPDAGenEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 13, 1, 1, 1)
)
himIPDAGenEntry.setIndexNames(
    (0, "SIEMENS-HP4KHIM-MIB", "himIPDAGenPabxId"),
)
if mibBuilder.loadTexts:
    himIPDAGenEntry.setStatus("current")
_HimIPDAGenPabxId_Type = HimPabxId
_HimIPDAGenPabxId_Object = MibTableColumn
himIPDAGenPabxId = _HimIPDAGenPabxId_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 13, 1, 1, 1, 1),
    _HimIPDAGenPabxId_Type()
)
himIPDAGenPabxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himIPDAGenPabxId.setStatus("current")


class _HimIPDAGenSpeed_Type(Integer32):
    """Custom type himIPDAGenSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(100, 100),
    )


_HimIPDAGenSpeed_Type.__name__ = "Integer32"
_HimIPDAGenSpeed_Object = MibTableColumn
himIPDAGenSpeed = _HimIPDAGenSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 13, 1, 1, 1, 2),
    _HimIPDAGenSpeed_Type()
)
himIPDAGenSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himIPDAGenSpeed.setStatus("current")


class _HimIPDAGenMode_Type(Integer32):
    """Custom type himIPDAGenMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fullduplex", 1),
          ("halfduplex", 2),
          ("other", 3))
    )


_HimIPDAGenMode_Type.__name__ = "Integer32"
_HimIPDAGenMode_Object = MibTableColumn
himIPDAGenMode = _HimIPDAGenMode_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 13, 1, 1, 1, 3),
    _HimIPDAGenMode_Type()
)
himIPDAGenMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himIPDAGenMode.setStatus("current")


class _HimIPDAGenPayConn_Type(Integer32):
    """Custom type himIPDAGenPayConn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HimIPDAGenPayConn_Type.__name__ = "Integer32"
_HimIPDAGenPayConn_Object = MibTableColumn
himIPDAGenPayConn = _HimIPDAGenPayConn_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 13, 1, 1, 1, 4),
    _HimIPDAGenPayConn_Type()
)
himIPDAGenPayConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himIPDAGenPayConn.setStatus("current")


class _HimIPDAGenSigConn_Type(Integer32):
    """Custom type himIPDAGenSigConn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HimIPDAGenSigConn_Type.__name__ = "Integer32"
_HimIPDAGenSigConn_Object = MibTableColumn
himIPDAGenSigConn = _HimIPDAGenSigConn_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 13, 1, 1, 1, 5),
    _HimIPDAGenSigConn_Type()
)
himIPDAGenSigConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himIPDAGenSigConn.setStatus("current")
_HimIPDAGenIPTable_Object = MibTable
himIPDAGenIPTable = _HimIPDAGenIPTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 13, 1, 2)
)
if mibBuilder.loadTexts:
    himIPDAGenIPTable.setStatus("current")
_HimIPDAGenIPEntry_Object = MibTableRow
himIPDAGenIPEntry = _HimIPDAGenIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 13, 1, 2, 1)
)
if mibBuilder.loadTexts:
    himIPDAGenIPEntry.setStatus("current")
_HimIPDAGenIPNetAddr_Type = IpAddress
_HimIPDAGenIPNetAddr_Object = MibTableColumn
himIPDAGenIPNetAddr = _HimIPDAGenIPNetAddr_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 13, 1, 2, 1, 1),
    _HimIPDAGenIPNetAddr_Type()
)
himIPDAGenIPNetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himIPDAGenIPNetAddr.setStatus("current")
_HimIPDAGenIPNetMask_Type = IpAddress
_HimIPDAGenIPNetMask_Object = MibTableColumn
himIPDAGenIPNetMask = _HimIPDAGenIPNetMask_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 13, 1, 2, 1, 2),
    _HimIPDAGenIPNetMask_Type()
)
himIPDAGenIPNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himIPDAGenIPNetMask.setStatus("current")
_HimIPDAGenIPCCAAddr_Type = IpAddress
_HimIPDAGenIPCCAAddr_Object = MibTableColumn
himIPDAGenIPCCAAddr = _HimIPDAGenIPCCAAddr_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 13, 1, 2, 1, 3),
    _HimIPDAGenIPCCAAddr_Type()
)
himIPDAGenIPCCAAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himIPDAGenIPCCAAddr.setStatus("current")
_HimIPDAGenIPCCBAddr_Type = IpAddress
_HimIPDAGenIPCCBAddr_Object = MibTableColumn
himIPDAGenIPCCBAddr = _HimIPDAGenIPCCBAddr_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 13, 1, 2, 1, 4),
    _HimIPDAGenIPCCBAddr_Type()
)
himIPDAGenIPCCBAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himIPDAGenIPCCBAddr.setStatus("current")
_HimIPDAGenIPDefRoutAddr_Type = IpAddress
_HimIPDAGenIPDefRoutAddr_Object = MibTableColumn
himIPDAGenIPDefRoutAddr = _HimIPDAGenIPDefRoutAddr_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 13, 1, 2, 1, 5),
    _HimIPDAGenIPDefRoutAddr_Type()
)
himIPDAGenIPDefRoutAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himIPDAGenIPDefRoutAddr.setStatus("current")
_HimIPDAGenIPSurvNetAddr_Type = IpAddress
_HimIPDAGenIPSurvNetAddr_Object = MibTableColumn
himIPDAGenIPSurvNetAddr = _HimIPDAGenIPSurvNetAddr_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 13, 1, 2, 1, 6),
    _HimIPDAGenIPSurvNetAddr_Type()
)
himIPDAGenIPSurvNetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himIPDAGenIPSurvNetAddr.setStatus("current")
_HimIPDAAPData_ObjectIdentity = ObjectIdentity
himIPDAAPData = _HimIPDAAPData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 13, 2)
)
_HimIPDABasicTable_Object = MibTable
himIPDABasicTable = _HimIPDABasicTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 13, 2, 1)
)
if mibBuilder.loadTexts:
    himIPDABasicTable.setStatus("current")
_HimIPDABasicEntry_Object = MibTableRow
himIPDABasicEntry = _HimIPDABasicEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 13, 2, 1, 1)
)
himIPDABasicEntry.setIndexNames(
    (0, "SIEMENS-HP4KHIM-MIB", "himIPDABasicPabxId"),
    (0, "SIEMENS-HP4KHIM-MIB", "himIPDABasicLTU"),
)
if mibBuilder.loadTexts:
    himIPDABasicEntry.setStatus("current")
_HimIPDABasicPabxId_Type = HimPabxId
_HimIPDABasicPabxId_Object = MibTableColumn
himIPDABasicPabxId = _HimIPDABasicPabxId_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 13, 2, 1, 1, 1),
    _HimIPDABasicPabxId_Type()
)
himIPDABasicPabxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himIPDABasicPabxId.setStatus("current")


class _HimIPDABasicLTU_Type(Integer32):
    """Custom type himIPDABasicLTU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(17, 99),
    )


_HimIPDABasicLTU_Type.__name__ = "Integer32"
_HimIPDABasicLTU_Object = MibTableColumn
himIPDABasicLTU = _HimIPDABasicLTU_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 13, 2, 1, 1, 2),
    _HimIPDABasicLTU_Type()
)
himIPDABasicLTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himIPDABasicLTU.setStatus("current")


class _HimIPDABasicConnType_Type(HimShelfNWType):
    """Custom type himIPDABasicConnType based on HimShelfNWType"""
    subtypeSpec = HimShelfNWType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 4),
    )


_HimIPDABasicConnType_Type.__name__ = "HimShelfNWType"
_HimIPDABasicConnType_Object = MibTableColumn
himIPDABasicConnType = _HimIPDABasicConnType_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 13, 2, 1, 1, 3),
    _HimIPDABasicConnType_Type()
)
himIPDABasicConnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himIPDABasicConnType.setStatus("current")


class _HimIPDABasicBChanNo_Type(Integer32):
    """Custom type himIPDABasicBChanNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_HimIPDABasicBChanNo_Type.__name__ = "Integer32"
_HimIPDABasicBChanNo_Object = MibTableColumn
himIPDABasicBChanNo = _HimIPDABasicBChanNo_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 13, 2, 1, 1, 4),
    _HimIPDABasicBChanNo_Type()
)
himIPDABasicBChanNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himIPDABasicBChanNo.setStatus("current")
_HimIPDABasicConvAMLaw_Type = HimYesNo
_HimIPDABasicConvAMLaw_Object = MibTableColumn
himIPDABasicConvAMLaw = _HimIPDABasicConvAMLaw_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 13, 2, 1, 1, 5),
    _HimIPDABasicConvAMLaw_Type()
)
himIPDABasicConvAMLaw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himIPDABasicConvAMLaw.setStatus("current")
_HimIPDAIPTable_Object = MibTable
himIPDAIPTable = _HimIPDAIPTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 13, 2, 2)
)
if mibBuilder.loadTexts:
    himIPDAIPTable.setStatus("current")
_HimIPDAIPEntry_Object = MibTableRow
himIPDAIPEntry = _HimIPDAIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 13, 2, 2, 1)
)
if mibBuilder.loadTexts:
    himIPDAIPEntry.setStatus("current")
_HimIPDAIPAccPtAddr_Type = IpAddress
_HimIPDAIPAccPtAddr_Object = MibTableColumn
himIPDAIPAccPtAddr = _HimIPDAIPAccPtAddr_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 13, 2, 2, 1, 1),
    _HimIPDAIPAccPtAddr_Type()
)
himIPDAIPAccPtAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himIPDAIPAccPtAddr.setStatus("current")
_HimIPDAIPTAccPtAddr_Type = IpAddress
_HimIPDAIPTAccPtAddr_Object = MibTableColumn
himIPDAIPTAccPtAddr = _HimIPDAIPTAccPtAddr_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 13, 2, 2, 1, 2),
    _HimIPDAIPTAccPtAddr_Type()
)
himIPDAIPTAccPtAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himIPDAIPTAccPtAddr.setStatus("current")
_HimIPDAIPAccPtRoutAddr_Type = IpAddress
_HimIPDAIPAccPtRoutAddr_Object = MibTableColumn
himIPDAIPAccPtRoutAddr = _HimIPDAIPAccPtRoutAddr_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 13, 2, 2, 1, 3),
    _HimIPDAIPAccPtRoutAddr_Type()
)
himIPDAIPAccPtRoutAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himIPDAIPAccPtRoutAddr.setStatus("current")
_HimIPDAIPNetMaskNW_Type = IpAddress
_HimIPDAIPNetMaskNW_Object = MibTableColumn
himIPDAIPNetMaskNW = _HimIPDAIPNetMaskNW_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 13, 2, 2, 1, 4),
    _HimIPDAIPNetMaskNW_Type()
)
himIPDAIPNetMaskNW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himIPDAIPNetMaskNW.setStatus("current")
_HimIPDAIPAccPtPriRoutAddr_Type = IpAddress
_HimIPDAIPAccPtPriRoutAddr_Object = MibTableColumn
himIPDAIPAccPtPriRoutAddr = _HimIPDAIPAccPtPriRoutAddr_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 13, 2, 2, 1, 5),
    _HimIPDAIPAccPtPriRoutAddr_Type()
)
himIPDAIPAccPtPriRoutAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himIPDAIPAccPtPriRoutAddr.setStatus("current")
_HimIPDAIPNetMaskDL_Type = IpAddress
_HimIPDAIPNetMaskDL_Object = MibTableColumn
himIPDAIPNetMaskDL = _HimIPDAIPNetMaskDL_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 13, 2, 2, 1, 6),
    _HimIPDAIPNetMaskDL_Type()
)
himIPDAIPNetMaskDL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himIPDAIPNetMaskDL.setStatus("current")
_HimIPDALocTable_Object = MibTable
himIPDALocTable = _HimIPDALocTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 13, 2, 3)
)
if mibBuilder.loadTexts:
    himIPDALocTable.setStatus("current")
_HimIPDALocEntry_Object = MibTableRow
himIPDALocEntry = _HimIPDALocEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 13, 2, 3, 1)
)
if mibBuilder.loadTexts:
    himIPDALocEntry.setStatus("current")


class _HimIPDALocId_Type(Integer32):
    """Custom type himIPDALocId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_HimIPDALocId_Type.__name__ = "Integer32"
_HimIPDALocId_Object = MibTableColumn
himIPDALocId = _HimIPDALocId_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 13, 2, 3, 1, 1),
    _HimIPDALocId_Type()
)
himIPDALocId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himIPDALocId.setStatus("current")


class _HimIPDALocLoc_Type(OctetString):
    """Custom type himIPDALocLoc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_HimIPDALocLoc_Type.__name__ = "OctetString"
_HimIPDALocLoc_Object = MibTableColumn
himIPDALocLoc = _HimIPDALocLoc_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 13, 2, 3, 1, 2),
    _HimIPDALocLoc_Type()
)
himIPDALocLoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himIPDALocLoc.setStatus("current")
_HimIPDALocPhoneNo_Type = HimPhoneNumber
_HimIPDALocPhoneNo_Object = MibTableColumn
himIPDALocPhoneNo = _HimIPDALocPhoneNo_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 13, 2, 3, 1, 3),
    _HimIPDALocPhoneNo_Type()
)
himIPDALocPhoneNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himIPDALocPhoneNo.setStatus("current")
_HimIPDALocFaxNo_Type = HimPhoneNumber
_HimIPDALocFaxNo_Object = MibTableColumn
himIPDALocFaxNo = _HimIPDALocFaxNo_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 13, 2, 3, 1, 4),
    _HimIPDALocFaxNo_Type()
)
himIPDALocFaxNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himIPDALocFaxNo.setStatus("current")
_HimInfo_ObjectIdentity = ObjectIdentity
himInfo = _HimInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 14)
)
_HimSubagentLastMsgNo_Type = Integer32
_HimSubagentLastMsgNo_Object = MibScalar
himSubagentLastMsgNo = _HimSubagentLastMsgNo_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 14, 1),
    _HimSubagentLastMsgNo_Type()
)
himSubagentLastMsgNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSubagentLastMsgNo.setStatus("current")
_HimSubagentLastMsgText_Type = OctetString
_HimSubagentLastMsgText_Object = MibScalar
himSubagentLastMsgText = _HimSubagentLastMsgText_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 14, 2),
    _HimSubagentLastMsgText_Type()
)
himSubagentLastMsgText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himSubagentLastMsgText.setStatus("current")
_HimResultData_Type = Integer32
_HimResultData_Object = MibScalar
himResultData = _HimResultData_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 14, 3),
    _HimResultData_Type()
)
himResultData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    himResultData.setStatus("current")
_HimDiscovery_ObjectIdentity = ObjectIdentity
himDiscovery = _HimDiscovery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 15)
)
_HimChanges_Type = Counter32
_HimChanges_Object = MibScalar
himChanges = _HimChanges_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 15, 1),
    _HimChanges_Type()
)
himChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himChanges.setStatus("current")
_HimDiscovTable_Object = MibTable
himDiscovTable = _HimDiscovTable_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 15, 2)
)
if mibBuilder.loadTexts:
    himDiscovTable.setStatus("current")
_HimDiscovEntry_Object = MibTableRow
himDiscovEntry = _HimDiscovEntry_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 15, 2, 1)
)
himDiscovEntry.setIndexNames(
    (0, "SIEMENS-HP4KHIM-MIB", "himDiscovPabxId"),
)
if mibBuilder.loadTexts:
    himDiscovEntry.setStatus("current")
_HimDiscovPabxId_Type = HimPabxId
_HimDiscovPabxId_Object = MibTableColumn
himDiscovPabxId = _HimDiscovPabxId_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 15, 2, 1, 1),
    _HimDiscovPabxId_Type()
)
himDiscovPabxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himDiscovPabxId.setStatus("current")
_HimDiscovPabxMnemonic_Type = DisplayString
_HimDiscovPabxMnemonic_Object = MibTableColumn
himDiscovPabxMnemonic = _HimDiscovPabxMnemonic_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 15, 2, 1, 2),
    _HimDiscovPabxMnemonic_Type()
)
himDiscovPabxMnemonic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himDiscovPabxMnemonic.setStatus("current")
_HimDiscovStatus_Type = DiscoveryStates
_HimDiscovStatus_Object = MibTableColumn
himDiscovStatus = _HimDiscovStatus_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 15, 2, 1, 3),
    _HimDiscovStatus_Type()
)
himDiscovStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    himDiscovStatus.setStatus("current")
_HimDiscovMode_Type = DiscoveryModes
_HimDiscovMode_Object = MibTableColumn
himDiscovMode = _HimDiscovMode_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 15, 2, 1, 4),
    _HimDiscovMode_Type()
)
himDiscovMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    himDiscovMode.setStatus("current")
_HimDiscovTimDat_Type = DisplayString
_HimDiscovTimDat_Object = MibTableColumn
himDiscovTimDat = _HimDiscovTimDat_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 15, 2, 1, 5),
    _HimDiscovTimDat_Type()
)
himDiscovTimDat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himDiscovTimDat.setStatus("current")
_HimDiscovErrTimDat_Type = DisplayString
_HimDiscovErrTimDat_Object = MibTableColumn
himDiscovErrTimDat = _HimDiscovErrTimDat_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 15, 2, 1, 6),
    _HimDiscovErrTimDat_Type()
)
himDiscovErrTimDat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    himDiscovErrTimDat.setStatus("current")
_HimMibConformance_ObjectIdentity = ObjectIdentity
himMibConformance = _HimMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 20)
)
_HimMibGroups_ObjectIdentity = ObjectIdentity
himMibGroups = _HimMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 20, 1)
)
_HimTrapGroup_ObjectIdentity = ObjectIdentity
himTrapGroup = _HimTrapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 21)
)
_HimTrapVariables_ObjectIdentity = ObjectIdentity
himTrapVariables = _HimTrapVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 21, 1)
)
_HimTrapPabxId_Type = Integer32
_HimTrapPabxId_Object = MibScalar
himTrapPabxId = _HimTrapPabxId_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 21, 1, 1),
    _HimTrapPabxId_Type()
)
himTrapPabxId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    himTrapPabxId.setStatus("current")
_HimTrapPabxMnemonic_Type = DisplayString
_HimTrapPabxMnemonic_Object = MibScalar
himTrapPabxMnemonic = _HimTrapPabxMnemonic_Object(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 21, 1, 2),
    _HimTrapPabxMnemonic_Type()
)
himTrapPabxMnemonic.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    himTrapPabxMnemonic.setStatus("current")
_HimTraps_ObjectIdentity = ObjectIdentity
himTraps = _HimTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 21, 2)
)
himBoardBasicEntry.registerAugmentions(
    ("SIEMENS-HP4KHIM-MIB",
     "himBoardIPEntry")
)
himBoardIPEntry.setIndexNames(*himBoardBasicEntry.getIndexNames())
himIPDAGenEntry.registerAugmentions(
    ("SIEMENS-HP4KHIM-MIB",
     "himIPDAGenIPEntry")
)
himIPDAGenIPEntry.setIndexNames(*himIPDAGenEntry.getIndexNames())
himIPDABasicEntry.registerAugmentions(
    ("SIEMENS-HP4KHIM-MIB",
     "himIPDAIPEntry")
)
himIPDAIPEntry.setIndexNames(*himIPDABasicEntry.getIndexNames())
himIPDABasicEntry.registerAugmentions(
    ("SIEMENS-HP4KHIM-MIB",
     "himIPDALocEntry")
)
himIPDALocEntry.setIndexNames(*himIPDABasicEntry.getIndexNames())

# Managed Objects groups

himWelcomePageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 20, 1, 1)
)
himWelcomePageGroup.setObjects(
      *(("SIEMENS-HP4KHIM-MIB", "himWelPgPabxId"),
        ("SIEMENS-HP4KHIM-MIB", "himWelPgSysNo"),
        ("SIEMENS-HP4KHIM-MIB", "himHP4KVersion"),
        ("SIEMENS-HP4KHIM-MIB", "himSystemRelease"),
        ("SIEMENS-HP4KHIM-MIB", "himRevisionLevel"),
        ("SIEMENS-HP4KHIM-MIB", "himHWArchitecture"),
        ("SIEMENS-HP4KHIM-MIB", "himHWArchitectureType"),
        ("SIEMENS-HP4KHIM-MIB", "himOperationMode"),
        ("SIEMENS-HP4KHIM-MIB", "himSWUProc1"),
        ("SIEMENS-HP4KHIM-MIB", "himSWUMemory1"),
        ("SIEMENS-HP4KHIM-MIB", "himSWUProc2"),
        ("SIEMENS-HP4KHIM-MIB", "himSWUMemory2"))
)
if mibBuilder.loadTexts:
    himWelcomePageGroup.setStatus("current")

himSwitchDataGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 20, 1, 2)
)
himSwitchDataGroup.setObjects(
      *(("SIEMENS-HP4KHIM-MIB", "himTechInfoPabxId"),
        ("SIEMENS-HP4KHIM-MIB", "himTechInfoInfoNo"),
        ("SIEMENS-HP4KHIM-MIB", "himTechInfoDate"),
        ("SIEMENS-HP4KHIM-MIB", "himTechInfoTechnicalData"),
        ("SIEMENS-HP4KHIM-MIB", "himTechInfoNumber"),
        ("SIEMENS-HP4KHIM-MIB", "himTechInfoExtraText"),
        ("SIEMENS-HP4KHIM-MIB", "himNotepadDataPabxId"),
        ("SIEMENS-HP4KHIM-MIB", "himNotepadDataInfoNo"),
        ("SIEMENS-HP4KHIM-MIB", "himNotepadDataDate"),
        ("SIEMENS-HP4KHIM-MIB", "himNotepadDataText"),
        ("SIEMENS-HP4KHIM-MIB", "himProjPlanPabxId"),
        ("SIEMENS-HP4KHIM-MIB", "himProjPlanInfoFile"),
        ("SIEMENS-HP4KHIM-MIB", "himProjPlanInfoCreationDate"),
        ("SIEMENS-HP4KHIM-MIB", "himProjPlanInfoCreationTime"))
)
if mibBuilder.loadTexts:
    himSwitchDataGroup.setStatus("current")

himSpecGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 20, 1, 3)
)
himSpecGroup.setObjects(
      *(("SIEMENS-HP4KHIM-MIB", "himSpecShelfDataPabxId"),
        ("SIEMENS-HP4KHIM-MIB", "himSpecShelfDataAddress"),
        ("SIEMENS-HP4KHIM-MIB", "himSpecShelfDataFrameType"),
        ("SIEMENS-HP4KHIM-MIB", "himSpecShelfDataLTU"),
        ("SIEMENS-HP4KHIM-MIB", "himSpecShelfDataNetworkType"),
        ("SIEMENS-HP4KHIM-MIB", "himSpecShelfDataNetworkAddress"),
        ("SIEMENS-HP4KHIM-MIB", "himSpecShelfDataRemote"),
        ("SIEMENS-HP4KHIM-MIB", "himSpecShelfDataLocation"),
        ("SIEMENS-HP4KHIM-MIB", "himSpecShelfDataLTUC"),
        ("SIEMENS-HP4KHIM-MIB", "himSWUBoardPabxId"),
        ("SIEMENS-HP4KHIM-MIB", "himSWUBoardPEN"),
        ("SIEMENS-HP4KHIM-MIB", "himSWUBoardOverlayLTU"),
        ("SIEMENS-HP4KHIM-MIB", "himSWUBoardType"),
        ("SIEMENS-HP4KHIM-MIB", "himSWUBoardNominal"),
        ("SIEMENS-HP4KHIM-MIB", "himSWUBoardActual"),
        ("SIEMENS-HP4KHIM-MIB", "hhimSWUBoardFirmware"),
        ("SIEMENS-HP4KHIM-MIB", "himSWUBoardRev"),
        ("SIEMENS-HP4KHIM-MIB", "himSWUBoardFunctId"),
        ("SIEMENS-HP4KHIM-MIB", "himSWUBoardMode"),
        ("SIEMENS-HP4KHIM-MIB", "himSWUBoardLWNo"),
        ("SIEMENS-HP4KHIM-MIB", "himSWUBoardLWInterVer"),
        ("SIEMENS-HP4KHIM-MIB", "himSWUBoardLWName"),
        ("SIEMENS-HP4KHIM-MIB", "himSWUBoardLWDate"))
)
if mibBuilder.loadTexts:
    himSpecGroup.setStatus("current")

himSWUPeripheryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 20, 1, 4)
)
himSWUPeripheryGroup.setObjects(
      *(("SIEMENS-HP4KHIM-MIB", "himPSIOAssPabxId"),
        ("SIEMENS-HP4KHIM-MIB", "himPSIOAssAssembly"),
        ("SIEMENS-HP4KHIM-MIB", "himPSIOAssPEN"),
        ("SIEMENS-HP4KHIM-MIB", "himPSIOAssActual"),
        ("SIEMENS-HP4KHIM-MIB", "himPSIOAssFirmware"),
        ("SIEMENS-HP4KHIM-MIB", "himSerialLinePabxId"),
        ("SIEMENS-HP4KHIM-MIB", "himSerialLineBoardType"),
        ("SIEMENS-HP4KHIM-MIB", "himSerialLineNumber"),
        ("SIEMENS-HP4KHIM-MIB", "himSerialLineSpeed"),
        ("SIEMENS-HP4KHIM-MIB", "himSerialLineLogDevName"),
        ("SIEMENS-HP4KHIM-MIB", "himSerialLineDevType"),
        ("SIEMENS-HP4KHIM-MIB", "himSerialLineType"),
        ("SIEMENS-HP4KHIM-MIB", "himSCSIDevPabxId"),
        ("SIEMENS-HP4KHIM-MIB", "himSCSIDevId"),
        ("SIEMENS-HP4KHIM-MIB", "himSCSIDevType"),
        ("SIEMENS-HP4KHIM-MIB", "himSCSIDevName"),
        ("SIEMENS-HP4KHIM-MIB", "himSCSIDevFirmware"),
        ("SIEMENS-HP4KHIM-MIB", "himSCSIDevLoadDrive"))
)
if mibBuilder.loadTexts:
    himSWUPeripheryGroup.setStatus("current")

himCentralSwitchGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 20, 1, 5)
)
himCentralSwitchGroup.setObjects(
      *(("SIEMENS-HP4KHIM-MIB", "himCabPabxId"),
        ("SIEMENS-HP4KHIM-MIB", "himCabAddr"),
        ("SIEMENS-HP4KHIM-MIB", "himCabPhysAddr"),
        ("SIEMENS-HP4KHIM-MIB", "himCabCabinet"),
        ("SIEMENS-HP4KHIM-MIB", "himCabPartNo"),
        ("SIEMENS-HP4KHIM-MIB", "himCabShelfNo"),
        ("SIEMENS-HP4KHIM-MIB", "himCabFrame"),
        ("SIEMENS-HP4KHIM-MIB", "himCabPid1"),
        ("SIEMENS-HP4KHIM-MIB", "himCabPid2"),
        ("SIEMENS-HP4KHIM-MIB", "himCabPid3"),
        ("SIEMENS-HP4KHIM-MIB", "himCabLTUNo"),
        ("SIEMENS-HP4KHIM-MIB", "himMemScalingPabxId"),
        ("SIEMENS-HP4KHIM-MIB", "himMemScalingUnit"),
        ("SIEMENS-HP4KHIM-MIB", "himMemScalingUsed"),
        ("SIEMENS-HP4KHIM-MIB", "himMemScalingMaxUsed"),
        ("SIEMENS-HP4KHIM-MIB", "himMemScalingAllocated"),
        ("SIEMENS-HP4KHIM-MIB", "himMemScalingStandard"),
        ("SIEMENS-HP4KHIM-MIB", "himMemScalingSysMax"))
)
if mibBuilder.loadTexts:
    himCentralSwitchGroup.setStatus("current")

himGeneralSwitchGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 20, 1, 6)
)
himGeneralSwitchGroup.setObjects(
      *(("SIEMENS-HP4KHIM-MIB", "himDBConfSysPabxId"),
        ("SIEMENS-HP4KHIM-MIB", "himDBConfSysClass1"),
        ("SIEMENS-HP4KHIM-MIB", "himDBConfSysClass2"),
        ("SIEMENS-HP4KHIM-MIB", "himDBConfSysHWAss1"),
        ("SIEMENS-HP4KHIM-MIB", "himDBConfSysHWAss2"),
        ("SIEMENS-HP4KHIM-MIB", "himDBConfSysDevLine1"),
        ("SIEMENS-HP4KHIM-MIB", "himDBConfSysDevLine2"),
        ("SIEMENS-HP4KHIM-MIB", "himDBConfSysOpMode"),
        ("SIEMENS-HP4KHIM-MIB", "himDBConfSysResType"),
        ("SIEMENS-HP4KHIM-MIB", "himDBConfSysHWArch"),
        ("SIEMENS-HP4KHIM-MIB", "himDBConfSysHWArchType"),
        ("SIEMENS-HP4KHIM-MIB", "himDBConfSysNo"),
        ("SIEMENS-HP4KHIM-MIB", "himDBConfSysLoc"),
        ("SIEMENS-HP4KHIM-MIB", "himDBConfSysBaseApp"),
        ("SIEMENS-HP4KHIM-MIB", "himDBConfSysDBApp"),
        ("SIEMENS-HP4KHIM-MIB", "himDBConfSysID"),
        ("SIEMENS-HP4KHIM-MIB", "himDBConfHWPabxId"),
        ("SIEMENS-HP4KHIM-MIB", "himDBConfHWLTG"),
        ("SIEMENS-HP4KHIM-MIB", "himDBConfHWLTU"),
        ("SIEMENS-HP4KHIM-MIB", "himDBConfHWLines"),
        ("SIEMENS-HP4KHIM-MIB", "himDBConfHWPorts"),
        ("SIEMENS-HP4KHIM-MIB", "himDBConfHWPBC"),
        ("SIEMENS-HP4KHIM-MIB", "himDBConfHWMTSBdPerGSN"),
        ("SIEMENS-HP4KHIM-MIB", "himDBConfHWSIUPPerLTU"),
        ("SIEMENS-HP4KHIM-MIB", "himDBConfHWDIUCPerLTU"),
        ("SIEMENS-HP4KHIM-MIB", "himDBConfHWHwyPerMTSBd"),
        ("SIEMENS-HP4KHIM-MIB", "himDBConfHWHDLCPerDCL"),
        ("SIEMENS-HP4KHIM-MIB", "himDBConfHWPBCPerDCL"),
        ("SIEMENS-HP4KHIM-MIB", "himDBConfHWStdSIULine"),
        ("SIEMENS-HP4KHIM-MIB", "himDBConfHWConfLine"),
        ("SIEMENS-HP4KHIM-MIB", "himDBConfHWDBDim"),
        ("SIEMENS-HP4KHIM-MIB", "himDBConfHWTableVer"),
        ("SIEMENS-HP4KHIM-MIB", "himHWDataPabxId"),
        ("SIEMENS-HP4KHIM-MIB", "himHWArch"),
        ("SIEMENS-HP4KHIM-MIB", "himHWArchType"),
        ("SIEMENS-HP4KHIM-MIB", "himHWOpMode"),
        ("SIEMENS-HP4KHIM-MIB", "himHWSWUProc1"),
        ("SIEMENS-HP4KHIM-MIB", "himHWSWUMem1"),
        ("SIEMENS-HP4KHIM-MIB", "himHWSWUProc2"),
        ("SIEMENS-HP4KHIM-MIB", "himHWSWUMem2"),
        ("SIEMENS-HP4KHIM-MIB", "himHWADPProc"),
        ("SIEMENS-HP4KHIM-MIB", "himHWADPMem"),
        ("SIEMENS-HP4KHIM-MIB", "himLWDataOnCBPabxId"),
        ("SIEMENS-HP4KHIM-MIB", "himLWOnCBAss"),
        ("SIEMENS-HP4KHIM-MIB", "himLWOnCBPBCAddr"),
        ("SIEMENS-HP4KHIM-MIB", "himLWOnCBFileName"),
        ("SIEMENS-HP4KHIM-MIB", "himLWOnCBProdTime"),
        ("SIEMENS-HP4KHIM-MIB", "himLWOnProcPabxId"),
        ("SIEMENS-HP4KHIM-MIB", "himLWOnProcAss"),
        ("SIEMENS-HP4KHIM-MIB", "himLWOnProcInfoType"),
        ("SIEMENS-HP4KHIM-MIB", "himLWOnProcLWId"),
        ("SIEMENS-HP4KHIM-MIB", "himLWOnProcLWIdCMP"),
        ("SIEMENS-HP4KHIM-MIB", "himLWOnProcLWIdLP"),
        ("SIEMENS-HP4KHIM-MIB", "himLWOnCSIUPabxId"),
        ("SIEMENS-HP4KHIM-MIB", "himLWOnCSIUProc"),
        ("SIEMENS-HP4KHIM-MIB", "himLWOnCSIUSlot"),
        ("SIEMENS-HP4KHIM-MIB", "himLWOnCSIUNominal"),
        ("SIEMENS-HP4KHIM-MIB", "himLWOnCSIUActual"),
        ("SIEMENS-HP4KHIM-MIB", "himLWOnCSIULWNo"),
        ("SIEMENS-HP4KHIM-MIB", "himLWOnCSIUFileName"),
        ("SIEMENS-HP4KHIM-MIB", "himLWOnCSIUFileProd"),
        ("SIEMENS-HP4KHIM-MIB", "himMacAddrPabxId"),
        ("SIEMENS-HP4KHIM-MIB", "himMacAddrProc"),
        ("SIEMENS-HP4KHIM-MIB", "himMacAddrInfoType"),
        ("SIEMENS-HP4KHIM-MIB", "himMacAddrCLan"),
        ("SIEMENS-HP4KHIM-MIB", "himMacAddrIPDA"))
)
if mibBuilder.loadTexts:
    himGeneralSwitchGroup.setStatus("current")

himFeaturesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 20, 1, 7)
)
himFeaturesGroup.setObjects(
      *(("SIEMENS-HP4KHIM-MIB", "himMacAddrPabxId"),
        ("SIEMENS-HP4KHIM-MIB", "himMacAddrProc"),
        ("SIEMENS-HP4KHIM-MIB", "himMacAddrCLan"),
        ("SIEMENS-HP4KHIM-MIB", "himMacAddrIPDA"),
        ("SIEMENS-HP4KHIM-MIB", "himMarkFeatPabxId"),
        ("SIEMENS-HP4KHIM-MIB", "himMarkFeatVer"),
        ("SIEMENS-HP4KHIM-MIB", "himMarkFeatSerNo"),
        ("SIEMENS-HP4KHIM-MIB", "himMarkFeatHWId"),
        ("SIEMENS-HP4KHIM-MIB", "himMarkFeatInstallDate"),
        ("SIEMENS-HP4KHIM-MIB", "himMarkFeatExpiryDate"),
        ("SIEMENS-HP4KHIM-MIB", "himMarkFeatConfCode"),
        ("SIEMENS-HP4KHIM-MIB", "himMarkFeatTrialModeAct"),
        ("SIEMENS-HP4KHIM-MIB", "himMarkFeatTrialRemDays"),
        ("SIEMENS-HP4KHIM-MIB", "himSalesFeatPabxId"),
        ("SIEMENS-HP4KHIM-MIB", "himSalesFeatMarketPackId"),
        ("SIEMENS-HP4KHIM-MIB", "himSalesFeatMarketPack"),
        ("SIEMENS-HP4KHIM-MIB", "himSalesFeatContract"),
        ("SIEMENS-HP4KHIM-MIB", "himSalesFeatUsed"),
        ("SIEMENS-HP4KHIM-MIB", "himSalesFeatFree"),
        ("SIEMENS-HP4KHIM-MIB", "himSalesFeatMarkForTrial"),
        ("SIEMENS-HP4KHIM-MIB", "himTechFeatPabxId"),
        ("SIEMENS-HP4KHIM-MIB", "himTechFeatId"),
        ("SIEMENS-HP4KHIM-MIB", "himTechFeatName"),
        ("SIEMENS-HP4KHIM-MIB", "himTechFeatState"))
)
if mibBuilder.loadTexts:
    himFeaturesGroup.setStatus("current")

himAPSPatchesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 20, 1, 8)
)
himAPSPatchesGroup.setObjects(
      *(("SIEMENS-HP4KHIM-MIB", "himSwitchAPSPabxId"),
        ("SIEMENS-HP4KHIM-MIB", "himSwitchAPSName"),
        ("SIEMENS-HP4KHIM-MIB", "himSwitchAPSCorrVer"),
        ("SIEMENS-HP4KHIM-MIB", "himSwitchAPSPartNo"),
        ("SIEMENS-HP4KHIM-MIB", "himReplAMOPabxId"),
        ("SIEMENS-HP4KHIM-MIB", "himReplAMOAPS"),
        ("SIEMENS-HP4KHIM-MIB", "himReplAMOName"),
        ("SIEMENS-HP4KHIM-MIB", "himReplAMOInAPSDir"),
        ("SIEMENS-HP4KHIM-MIB", "himReplAMOSubsystem"),
        ("SIEMENS-HP4KHIM-MIB", "himPatchInfoPabxId"),
        ("SIEMENS-HP4KHIM-MIB", "himPatchInfoPatchNo"),
        ("SIEMENS-HP4KHIM-MIB", "himPatchInfoPatchGroup"),
        ("SIEMENS-HP4KHIM-MIB", "himPatchInfoOpt"),
        ("SIEMENS-HP4KHIM-MIB", "himPatchInfoActHD"),
        ("SIEMENS-HP4KHIM-MIB", "himPatchInfoActADP"),
        ("SIEMENS-HP4KHIM-MIB", "himPatchInfoActBP"))
)
if mibBuilder.loadTexts:
    himAPSPatchesGroup.setStatus("current")

himSWVersionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 20, 1, 9)
)
himSWVersionGroup.setObjects(
      *(("SIEMENS-HP4KHIM-MIB", "himSWVerOnProcPabxId"),
        ("SIEMENS-HP4KHIM-MIB", "himSWVerOnProcSrc"),
        ("SIEMENS-HP4KHIM-MIB", "himSWVerOnProcSWVer"),
        ("SIEMENS-HP4KHIM-MIB", "himSWVerOnProcItemCodeNoPrefix"),
        ("SIEMENS-HP4KHIM-MIB", "himSWVerOnProcHP4KVer"),
        ("SIEMENS-HP4KHIM-MIB", "himSWVerOnProcSysRel"),
        ("SIEMENS-HP4KHIM-MIB", "himSWVerOnProcCountry"),
        ("SIEMENS-HP4KHIM-MIB", "himSWVerOnProcCountryCode"),
        ("SIEMENS-HP4KHIM-MIB", "himSWVerOnProcRevNo"))
)
if mibBuilder.loadTexts:
    himSWVersionGroup.setStatus("current")

himSWPkgVersionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 20, 1, 10)
)
himSWPkgVersionGroup.setObjects(
      *(("SIEMENS-HP4KHIM-MIB", "himSWPkgVerPabxId"),
        ("SIEMENS-HP4KHIM-MIB", "himSWPkgVerPkgAbbr"),
        ("SIEMENS-HP4KHIM-MIB", "himSWPkgVerPkgName"),
        ("SIEMENS-HP4KHIM-MIB", "himSWPkgVerVersion"),
        ("SIEMENS-HP4KHIM-MIB", "himSWPkgVerInstAt"),
        ("SIEMENS-HP4KHIM-MIB", "himSWPkgVerStatus"))
)
if mibBuilder.loadTexts:
    himSWPkgVersionGroup.setStatus("current")

himSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 20, 1, 11)
)
himSystemGroup.setObjects(
      *(("SIEMENS-HP4KHIM-MIB", "himSysBasicPabxId"),
        ("SIEMENS-HP4KHIM-MIB", "himSysBasicDomain"),
        ("SIEMENS-HP4KHIM-MIB", "himSysBasicNodeNo"),
        ("SIEMENS-HP4KHIM-MIB", "himSysBasicLEGK"),
        ("SIEMENS-HP4KHIM-MIB", "himSysLANCardsPabxId"),
        ("SIEMENS-HP4KHIM-MIB", "himSysLANCardsIPAddr"),
        ("SIEMENS-HP4KHIM-MIB", "himSysLANCardsNetMask"),
        ("SIEMENS-HP4KHIM-MIB", "himSysLANCardsBroadCast"),
        ("SIEMENS-HP4KHIM-MIB", "himSysLANCardsType"),
        ("SIEMENS-HP4KHIM-MIB", "himSysLANCardsStatus"),
        ("SIEMENS-HP4KHIM-MIB", "himSysHostsPabxId"),
        ("SIEMENS-HP4KHIM-MIB", "himSysHostsNo"),
        ("SIEMENS-HP4KHIM-MIB", "himSysHostsIPAddr"),
        ("SIEMENS-HP4KHIM-MIB", "himSysHostsName"),
        ("SIEMENS-HP4KHIM-MIB", "himSysWAMLConnPabxId"),
        ("SIEMENS-HP4KHIM-MIB", "himSysWAMLConnLTG"),
        ("SIEMENS-HP4KHIM-MIB", "himSysWAMLConnLTU"),
        ("SIEMENS-HP4KHIM-MIB", "himSysWAMLConnSlot"),
        ("SIEMENS-HP4KHIM-MIB", "himSysWAMLConnRufNr"),
        ("SIEMENS-HP4KHIM-MIB", "himSysWAMLConnBChl"),
        ("SIEMENS-HP4KHIM-MIB", "himSysWAMLConnStatus"),
        ("SIEMENS-HP4KHIM-MIB", "himSysWAMLConnIPPabxId"),
        ("SIEMENS-HP4KHIM-MIB", "himSysWAMLConnIPLTG"),
        ("SIEMENS-HP4KHIM-MIB", "himSysWAMLConnIPLTU"),
        ("SIEMENS-HP4KHIM-MIB", "himSysWAMLConnIPSlot"),
        ("SIEMENS-HP4KHIM-MIB", "himSysWAMLConnIPIfName"),
        ("SIEMENS-HP4KHIM-MIB", "himSysWAMLConnIPAddr"),
        ("SIEMENS-HP4KHIM-MIB", "himSysWAMLConnIPNetMask"))
)
if mibBuilder.loadTexts:
    himSystemGroup.setStatus("current")

himBoardsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 20, 1, 12)
)
himBoardsGroup.setObjects(
      *(("SIEMENS-HP4KHIM-MIB", "himBoardBasicPabxId"),
        ("SIEMENS-HP4KHIM-MIB", "himBoardBasicLTG"),
        ("SIEMENS-HP4KHIM-MIB", "himBoardBasicLTU"),
        ("SIEMENS-HP4KHIM-MIB", "himBoardBasicSlot"),
        ("SIEMENS-HP4KHIM-MIB", "himBoardBasicFuncId"),
        ("SIEMENS-HP4KHIM-MIB", "himBoardBasicCat"),
        ("SIEMENS-HP4KHIM-MIB", "himBoardBasicName"),
        ("SIEMENS-HP4KHIM-MIB", "himBoardBasicVOIPSec"),
        ("SIEMENS-HP4KHIM-MIB", "himBoardBasicLWVar"),
        ("SIEMENS-HP4KHIM-MIB", "himBoardBasicNoCirc"),
        ("SIEMENS-HP4KHIM-MIB", "himBoardIPGwyIPAddr"),
        ("SIEMENS-HP4KHIM-MIB", "himBoardIPSrcIPAddr"),
        ("SIEMENS-HP4KHIM-MIB", "himBoardIPNetMask"),
        ("SIEMENS-HP4KHIM-MIB", "himBoardIPDefRouter"),
        ("SIEMENS-HP4KHIM-MIB", "himBoardIPCustLANIP"),
        ("SIEMENS-HP4KHIM-MIB", "himBoardIPSTMI2IGWSubMask"),
        ("SIEMENS-HP4KHIM-MIB", "himBoardIPDefGWIP"),
        ("SIEMENS-HP4KHIM-MIB", "himBoardIPManStatIP"),
        ("SIEMENS-HP4KHIM-MIB", "himBoardIPManStatPort"),
        ("SIEMENS-HP4KHIM-MIB", "himBoardIPBckpServIP"),
        ("SIEMENS-HP4KHIM-MIB", "himBoardIPBckpServPort"),
        ("SIEMENS-HP4KHIM-MIB", "himBoardLocId"),
        ("SIEMENS-HP4KHIM-MIB", "himBoardLocLoc"),
        ("SIEMENS-HP4KHIM-MIB", "himBoardLocPhoneNo"),
        ("SIEMENS-HP4KHIM-MIB", "himBoardLocFaxNo"))
)
if mibBuilder.loadTexts:
    himBoardsGroup.setStatus("current")

himIPDAGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 20, 1, 13)
)
himIPDAGroup.setObjects(
      *(("SIEMENS-HP4KHIM-MIB", "himIPDABasicPabxId"),
        ("SIEMENS-HP4KHIM-MIB", "himIPDABasicLTU"),
        ("SIEMENS-HP4KHIM-MIB", "himIPDABasicConnType"),
        ("SIEMENS-HP4KHIM-MIB", "himIPDABasicBChanNo"),
        ("SIEMENS-HP4KHIM-MIB", "himIPDABasicConvAMLaw"),
        ("SIEMENS-HP4KHIM-MIB", "himIPDAGenPabxId"),
        ("SIEMENS-HP4KHIM-MIB", "himIPDAGenSpeed"),
        ("SIEMENS-HP4KHIM-MIB", "himIPDAGenMode"),
        ("SIEMENS-HP4KHIM-MIB", "himIPDAGenPayConn"),
        ("SIEMENS-HP4KHIM-MIB", "himIPDAGenSigConn"),
        ("SIEMENS-HP4KHIM-MIB", "himIPDAGenIPNetAddr"),
        ("SIEMENS-HP4KHIM-MIB", "himIPDAGenIPNetMask"),
        ("SIEMENS-HP4KHIM-MIB", "himIPDAGenIPCCAAddr"),
        ("SIEMENS-HP4KHIM-MIB", "himIPDAGenIPCCBAddr"),
        ("SIEMENS-HP4KHIM-MIB", "himIPDAGenIPDefRoutAddr"),
        ("SIEMENS-HP4KHIM-MIB", "himIPDAGenIPSurvNetAddr"),
        ("SIEMENS-HP4KHIM-MIB", "himIPDAIPAccPtAddr"),
        ("SIEMENS-HP4KHIM-MIB", "himIPDAIPTAccPtAddr"),
        ("SIEMENS-HP4KHIM-MIB", "himIPDAIPAccPtRoutAddr"),
        ("SIEMENS-HP4KHIM-MIB", "himIPDAIPNetMaskNW"),
        ("SIEMENS-HP4KHIM-MIB", "himIPDAIPAccPtPriRoutAddr"),
        ("SIEMENS-HP4KHIM-MIB", "himIPDAIPNetMaskDL"),
        ("SIEMENS-HP4KHIM-MIB", "himIPDALocId"),
        ("SIEMENS-HP4KHIM-MIB", "himIPDALocLoc"),
        ("SIEMENS-HP4KHIM-MIB", "himIPDALocPhoneNo"),
        ("SIEMENS-HP4KHIM-MIB", "himIPDALocFaxNo"))
)
if mibBuilder.loadTexts:
    himIPDAGroup.setStatus("current")

himInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 20, 1, 14)
)
himInfoGroup.setObjects(
      *(("SIEMENS-HP4KHIM-MIB", "himSubagentLastMsgNo"),
        ("SIEMENS-HP4KHIM-MIB", "himSubagentLastMsgText"),
        ("SIEMENS-HP4KHIM-MIB", "himResultData"))
)
if mibBuilder.loadTexts:
    himInfoGroup.setStatus("current")

himDiscoveryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 20, 1, 15)
)
himDiscoveryGroup.setObjects(
      *(("SIEMENS-HP4KHIM-MIB", "himChanges"),
        ("SIEMENS-HP4KHIM-MIB", "himDiscovPabxId"),
        ("SIEMENS-HP4KHIM-MIB", "himDiscovPabxMnemonic"),
        ("SIEMENS-HP4KHIM-MIB", "himDiscovStatus"),
        ("SIEMENS-HP4KHIM-MIB", "himDiscovMode"),
        ("SIEMENS-HP4KHIM-MIB", "himDiscovTimDat"),
        ("SIEMENS-HP4KHIM-MIB", "himDiscovErrTimDat"))
)
if mibBuilder.loadTexts:
    himDiscoveryGroup.setStatus("current")


# Notification objects

internalMessageHimSubagent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 21, 2, 0)
)
internalMessageHimSubagent.setObjects(
      *(("SIEMENS-HP4KHIM-MIB", "himSubagentLastMsgNo"),
        ("SIEMENS-HP4KHIM-MIB", "himSubagentLastMsgText"))
)
if mibBuilder.loadTexts:
    internalMessageHimSubagent.setStatus(
        "current"
    )

internalWarningHimSubagent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 21, 2, 1)
)
internalWarningHimSubagent.setObjects(
      *(("SIEMENS-HP4KHIM-MIB", "himSubagentLastMsgNo"),
        ("SIEMENS-HP4KHIM-MIB", "himSubagentLastMsgText"))
)
if mibBuilder.loadTexts:
    internalWarningHimSubagent.setStatus(
        "current"
    )

internalErrorHimSubagent = NotificationType(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 21, 2, 2)
)
internalErrorHimSubagent.setObjects(
      *(("SIEMENS-HP4KHIM-MIB", "himSubagentLastMsgNo"),
        ("SIEMENS-HP4KHIM-MIB", "himSubagentLastMsgText"))
)
if mibBuilder.loadTexts:
    internalErrorHimSubagent.setStatus(
        "current"
    )

himDiscovSucc = NotificationType(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 21, 2, 10)
)
himDiscovSucc.setObjects(
      *(("SIEMENS-HP4KHIM-MIB", "himTrapPabxId"),
        ("SIEMENS-HP4KHIM-MIB", "himTrapPabxMnemonic"))
)
if mibBuilder.loadTexts:
    himDiscovSucc.setStatus(
        "current"
    )

himDiscovErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 21, 2, 11)
)
himDiscovErr.setObjects(
      *(("SIEMENS-HP4KHIM-MIB", "himTrapPabxId"),
        ("SIEMENS-HP4KHIM-MIB", "himTrapPabxMnemonic"))
)
if mibBuilder.loadTexts:
    himDiscovErr.setStatus(
        "current"
    )

himDiscovBusy = NotificationType(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 21, 2, 19)
)
himDiscovBusy.setObjects(
      *(("SIEMENS-HP4KHIM-MIB", "himTrapPabxId"),
        ("SIEMENS-HP4KHIM-MIB", "himTrapPabxMnemonic"))
)
if mibBuilder.loadTexts:
    himDiscovBusy.setStatus(
        "current"
    )


# Notifications groups

himTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4329, 2, 51, 20, 1, 16)
)
himTrapsGroup.setObjects(
      *(("SIEMENS-HP4KHIM-MIB", "internalMessageHimSubagent"),
        ("SIEMENS-HP4KHIM-MIB", "internalWarningHimSubagent"),
        ("SIEMENS-HP4KHIM-MIB", "internalErrorHimSubagent"),
        ("SIEMENS-HP4KHIM-MIB", "himDiscovSucc"),
        ("SIEMENS-HP4KHIM-MIB", "himDiscovErr"),
        ("SIEMENS-HP4KHIM-MIB", "himDiscovBusy"))
)
if mibBuilder.loadTexts:
    himTrapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SIEMENS-HP4KHIM-MIB",
    **{"HimPEN": HimPEN,
       "HimPabxId": HimPabxId,
       "HimSwitchNumber": HimSwitchNumber,
       "HimYesNo": HimYesNo,
       "DiscoveryStates": DiscoveryStates,
       "DiscoveryModes": DiscoveryModes,
       "HimPhoneNumber": HimPhoneNumber,
       "HimShelfNWType": HimShelfNWType,
       "siemens": siemens,
       "iandcAdmin": iandcAdmin,
       "hp4khim": hp4khim,
       "himWelcomePage": himWelcomePage,
       "himWelPgTable": himWelPgTable,
       "himWelPgEntry": himWelPgEntry,
       "himWelPgPabxId": himWelPgPabxId,
       "himWelPgSysNo": himWelPgSysNo,
       "himHP4KVersion": himHP4KVersion,
       "himSystemRelease": himSystemRelease,
       "himRevisionLevel": himRevisionLevel,
       "himHWArchitecture": himHWArchitecture,
       "himHWArchitectureType": himHWArchitectureType,
       "himOperationMode": himOperationMode,
       "himSWUProc1": himSWUProc1,
       "himSWUMemory1": himSWUMemory1,
       "himSWUProc2": himSWUProc2,
       "himSWUMemory2": himSWUMemory2,
       "himSwitchData": himSwitchData,
       "himTechInfoTable": himTechInfoTable,
       "himTechInfoEntry": himTechInfoEntry,
       "himTechInfoPabxId": himTechInfoPabxId,
       "himTechInfoInfoNo": himTechInfoInfoNo,
       "himTechInfoDate": himTechInfoDate,
       "himTechInfoTechnicalData": himTechInfoTechnicalData,
       "himTechInfoNumber": himTechInfoNumber,
       "himTechInfoExtraText": himTechInfoExtraText,
       "himNotepadDataTable": himNotepadDataTable,
       "himNotepadDataEntry": himNotepadDataEntry,
       "himNotepadDataPabxId": himNotepadDataPabxId,
       "himNotepadDataInfoNo": himNotepadDataInfoNo,
       "himNotepadDataDate": himNotepadDataDate,
       "himNotepadDataText": himNotepadDataText,
       "himProjPlanInfoTable": himProjPlanInfoTable,
       "himProjPlanInfoEntry": himProjPlanInfoEntry,
       "himProjPlanPabxId": himProjPlanPabxId,
       "himProjPlanInfoFile": himProjPlanInfoFile,
       "himProjPlanInfoCreationDate": himProjPlanInfoCreationDate,
       "himProjPlanInfoCreationTime": himProjPlanInfoCreationTime,
       "himSpecSwitchData": himSpecSwitchData,
       "himSpecShelfDataTable": himSpecShelfDataTable,
       "himSpecShelfDataEntry": himSpecShelfDataEntry,
       "himSpecShelfDataPabxId": himSpecShelfDataPabxId,
       "himSpecShelfDataAddress": himSpecShelfDataAddress,
       "himSpecShelfDataFrameType": himSpecShelfDataFrameType,
       "himSpecShelfDataLTU": himSpecShelfDataLTU,
       "himSpecShelfDataNetworkType": himSpecShelfDataNetworkType,
       "himSpecShelfDataNetworkAddress": himSpecShelfDataNetworkAddress,
       "himSpecShelfDataRemote": himSpecShelfDataRemote,
       "himSpecShelfDataLocation": himSpecShelfDataLocation,
       "himSpecShelfDataLTUC": himSpecShelfDataLTUC,
       "himSWUBoardTable": himSWUBoardTable,
       "himSWUBoardEntry": himSWUBoardEntry,
       "himSWUBoardPabxId": himSWUBoardPabxId,
       "himSWUBoardPEN": himSWUBoardPEN,
       "himSWUBoardOverlayLTU": himSWUBoardOverlayLTU,
       "himSWUBoardType": himSWUBoardType,
       "himSWUBoardNominal": himSWUBoardNominal,
       "himSWUBoardActual": himSWUBoardActual,
       "hhimSWUBoardFirmware": hhimSWUBoardFirmware,
       "himSWUBoardRev": himSWUBoardRev,
       "himSWUBoardFunctId": himSWUBoardFunctId,
       "himSWUBoardMode": himSWUBoardMode,
       "himSWUBoardLWNo": himSWUBoardLWNo,
       "himSWUBoardLWInterVer": himSWUBoardLWInterVer,
       "himSWUBoardLWName": himSWUBoardLWName,
       "himSWUBoardLWDate": himSWUBoardLWDate,
       "himSWUPeriphery": himSWUPeriphery,
       "himPSIOAssTable": himPSIOAssTable,
       "himPSIOAssEntry": himPSIOAssEntry,
       "himPSIOAssPabxId": himPSIOAssPabxId,
       "himPSIOAssPEN": himPSIOAssPEN,
       "himPSIOAssAssembly": himPSIOAssAssembly,
       "himPSIOAssActual": himPSIOAssActual,
       "himPSIOAssFirmware": himPSIOAssFirmware,
       "himSerialLineTable": himSerialLineTable,
       "himSerialLineEntry": himSerialLineEntry,
       "himSerialLinePabxId": himSerialLinePabxId,
       "himSerialLineNumber": himSerialLineNumber,
       "himSerialLineBoardType": himSerialLineBoardType,
       "himSerialLineSpeed": himSerialLineSpeed,
       "himSerialLineLogDevName": himSerialLineLogDevName,
       "himSerialLineDevType": himSerialLineDevType,
       "himSerialLineType": himSerialLineType,
       "himSCSIDevTable": himSCSIDevTable,
       "himSCSIDevEntry": himSCSIDevEntry,
       "himSCSIDevPabxId": himSCSIDevPabxId,
       "himSCSIDevId": himSCSIDevId,
       "himSCSIDevType": himSCSIDevType,
       "himSCSIDevName": himSCSIDevName,
       "himSCSIDevFirmware": himSCSIDevFirmware,
       "himSCSIDevLoadDrive": himSCSIDevLoadDrive,
       "himCentralSwitchData": himCentralSwitchData,
       "himCabinetTable": himCabinetTable,
       "himCabinetEntry": himCabinetEntry,
       "himCabPabxId": himCabPabxId,
       "himCabAddr": himCabAddr,
       "himCabPhysAddr": himCabPhysAddr,
       "himCabCabinet": himCabCabinet,
       "himCabPartNo": himCabPartNo,
       "himCabShelfNo": himCabShelfNo,
       "himCabFrame": himCabFrame,
       "himCabPid1": himCabPid1,
       "himCabPid2": himCabPid2,
       "himCabPid3": himCabPid3,
       "himCabLTUNo": himCabLTUNo,
       "himMemScalingTable": himMemScalingTable,
       "himMemScalingEntry": himMemScalingEntry,
       "himMemScalingPabxId": himMemScalingPabxId,
       "himMemScalingUnit": himMemScalingUnit,
       "himMemScalingUsed": himMemScalingUsed,
       "himMemScalingMaxUsed": himMemScalingMaxUsed,
       "himMemScalingAllocated": himMemScalingAllocated,
       "himMemScalingStandard": himMemScalingStandard,
       "himMemScalingSysMax": himMemScalingSysMax,
       "himGeneralSwitchData": himGeneralSwitchData,
       "himDBConfSys": himDBConfSys,
       "himDBConfSysTable": himDBConfSysTable,
       "himDBConfSysEntry": himDBConfSysEntry,
       "himDBConfSysPabxId": himDBConfSysPabxId,
       "himDBConfSysClass1": himDBConfSysClass1,
       "himDBConfSysClass2": himDBConfSysClass2,
       "himDBConfSysHWAss1": himDBConfSysHWAss1,
       "himDBConfSysHWAss2": himDBConfSysHWAss2,
       "himDBConfSysDevLine1": himDBConfSysDevLine1,
       "himDBConfSysDevLine2": himDBConfSysDevLine2,
       "himDBConfSysOpMode": himDBConfSysOpMode,
       "himDBConfSysResType": himDBConfSysResType,
       "himDBConfSysHWArch": himDBConfSysHWArch,
       "himDBConfSysHWArchType": himDBConfSysHWArchType,
       "himDBConfSysNo": himDBConfSysNo,
       "himDBConfSysLoc": himDBConfSysLoc,
       "himDBConfSysBaseApp": himDBConfSysBaseApp,
       "himDBConfSysDBApp": himDBConfSysDBApp,
       "himDBConfSysID": himDBConfSysID,
       "himDBConfHW": himDBConfHW,
       "himDBConfHWTable": himDBConfHWTable,
       "himDBConfHWEntry": himDBConfHWEntry,
       "himDBConfHWPabxId": himDBConfHWPabxId,
       "himDBConfHWLTG": himDBConfHWLTG,
       "himDBConfHWLTU": himDBConfHWLTU,
       "himDBConfHWLines": himDBConfHWLines,
       "himDBConfHWPorts": himDBConfHWPorts,
       "himDBConfHWPBC": himDBConfHWPBC,
       "himDBConfHWMTSBdPerGSN": himDBConfHWMTSBdPerGSN,
       "himDBConfHWSIUPPerLTU": himDBConfHWSIUPPerLTU,
       "himDBConfHWDIUCPerLTU": himDBConfHWDIUCPerLTU,
       "himDBConfHWHwyPerMTSBd": himDBConfHWHwyPerMTSBd,
       "himDBConfHWHDLCPerDCL": himDBConfHWHDLCPerDCL,
       "himDBConfHWPBCPerDCL": himDBConfHWPBCPerDCL,
       "himDBConfHWStdSIULine": himDBConfHWStdSIULine,
       "himDBConfHWConfLine": himDBConfHWConfLine,
       "himDBConfHWDBDim": himDBConfHWDBDim,
       "himDBConfHWTableVer": himDBConfHWTableVer,
       "himHWData": himHWData,
       "himHWDataTable": himHWDataTable,
       "himHWDataEntry": himHWDataEntry,
       "himHWDataPabxId": himHWDataPabxId,
       "himHWArch": himHWArch,
       "himHWArchType": himHWArchType,
       "himHWOpMode": himHWOpMode,
       "himHWSWUProc1": himHWSWUProc1,
       "himHWSWUMem1": himHWSWUMem1,
       "himHWSWUProc2": himHWSWUProc2,
       "himHWSWUMem2": himHWSWUMem2,
       "himHWADPProc": himHWADPProc,
       "himHWADPMem": himHWADPMem,
       "himLWDataOnCB": himLWDataOnCB,
       "himLWDataOnCBTable": himLWDataOnCBTable,
       "himLWDataOnCBEntry": himLWDataOnCBEntry,
       "himLWDataOnCBPabxId": himLWDataOnCBPabxId,
       "himLWOnCBAss": himLWOnCBAss,
       "himLWOnCBPBCAddr": himLWOnCBPBCAddr,
       "himLWOnCBFileName": himLWOnCBFileName,
       "himLWOnCBProdTime": himLWOnCBProdTime,
       "himLWDataOnProc": himLWDataOnProc,
       "himLWOnProcTable": himLWOnProcTable,
       "himLWOnProcEntry": himLWOnProcEntry,
       "himLWOnProcPabxId": himLWOnProcPabxId,
       "himLWOnProcAss": himLWOnProcAss,
       "himLWOnProcInfoType": himLWOnProcInfoType,
       "himLWOnProcLWId": himLWOnProcLWId,
       "himLWOnProcLWIdCMP": himLWOnProcLWIdCMP,
       "himLWOnProcLWIdLP": himLWOnProcLWIdLP,
       "himLWDataOnCSIU": himLWDataOnCSIU,
       "himLWOnCSIUTable": himLWOnCSIUTable,
       "himLWOnCSIUEntry": himLWOnCSIUEntry,
       "himLWOnCSIUPabxId": himLWOnCSIUPabxId,
       "himLWOnCSIUNominal": himLWOnCSIUNominal,
       "himLWOnCSIULWNo": himLWOnCSIULWNo,
       "himLWOnCSIUProc": himLWOnCSIUProc,
       "himLWOnCSIUSlot": himLWOnCSIUSlot,
       "himLWOnCSIUActual": himLWOnCSIUActual,
       "himLWOnCSIUFileName": himLWOnCSIUFileName,
       "himLWOnCSIUFileProd": himLWOnCSIUFileProd,
       "himMacAddress": himMacAddress,
       "himMacAddrTable": himMacAddrTable,
       "himMacAddrEntry": himMacAddrEntry,
       "himMacAddrPabxId": himMacAddrPabxId,
       "himMacAddrProc": himMacAddrProc,
       "himMacAddrInfoType": himMacAddrInfoType,
       "himMacAddrCLan": himMacAddrCLan,
       "himMacAddrIPDA": himMacAddrIPDA,
       "himFeatures": himFeatures,
       "himMarketingFeatures": himMarketingFeatures,
       "himMarkFeatTable": himMarkFeatTable,
       "himMarkFeatEntry": himMarkFeatEntry,
       "himMarkFeatPabxId": himMarkFeatPabxId,
       "himMarkFeatVer": himMarkFeatVer,
       "himMarkFeatSerNo": himMarkFeatSerNo,
       "himMarkFeatHWId": himMarkFeatHWId,
       "himMarkFeatInstallDate": himMarkFeatInstallDate,
       "himMarkFeatExpiryDate": himMarkFeatExpiryDate,
       "himMarkFeatConfCode": himMarkFeatConfCode,
       "himMarkFeatTrialModeAct": himMarkFeatTrialModeAct,
       "himMarkFeatTrialRemDays": himMarkFeatTrialRemDays,
       "himSalesFeatTable": himSalesFeatTable,
       "himSalesFeatEntry": himSalesFeatEntry,
       "himSalesFeatPabxId": himSalesFeatPabxId,
       "himSalesFeatMarketPackId": himSalesFeatMarketPackId,
       "himSalesFeatMarketPack": himSalesFeatMarketPack,
       "himSalesFeatContract": himSalesFeatContract,
       "himSalesFeatUsed": himSalesFeatUsed,
       "himSalesFeatFree": himSalesFeatFree,
       "himSalesFeatMarkForTrial": himSalesFeatMarkForTrial,
       "himTechFeatures": himTechFeatures,
       "himTechFeatTable": himTechFeatTable,
       "himTechFeatEntry": himTechFeatEntry,
       "himTechFeatPabxId": himTechFeatPabxId,
       "himTechFeatId": himTechFeatId,
       "himTechFeatName": himTechFeatName,
       "himTechFeatState": himTechFeatState,
       "himAPSPatches": himAPSPatches,
       "himSwitchAPS": himSwitchAPS,
       "himSwitchAPSTable": himSwitchAPSTable,
       "himSwitchAPSEntry": himSwitchAPSEntry,
       "himSwitchAPSPabxId": himSwitchAPSPabxId,
       "himSwitchAPSName": himSwitchAPSName,
       "himSwitchAPSCorrVer": himSwitchAPSCorrVer,
       "himSwitchAPSPartNo": himSwitchAPSPartNo,
       "himReplacedAMOs": himReplacedAMOs,
       "himReplAMOTable": himReplAMOTable,
       "himReplAMOEntry": himReplAMOEntry,
       "himReplAMOPabxId": himReplAMOPabxId,
       "himReplAMOAPS": himReplAMOAPS,
       "himReplAMOName": himReplAMOName,
       "himReplAMOInAPSDir": himReplAMOInAPSDir,
       "himReplAMOSubsystem": himReplAMOSubsystem,
       "himPatchInfo": himPatchInfo,
       "himPatchInfoTable": himPatchInfoTable,
       "himPatchInfoEntry": himPatchInfoEntry,
       "himPatchInfoPabxId": himPatchInfoPabxId,
       "himPatchInfoPatchNo": himPatchInfoPatchNo,
       "himPatchInfoPatchGroup": himPatchInfoPatchGroup,
       "himPatchInfoOpt": himPatchInfoOpt,
       "himPatchInfoActHD": himPatchInfoActHD,
       "himPatchInfoActADP": himPatchInfoActADP,
       "himPatchInfoActBP": himPatchInfoActBP,
       "himSWVersion": himSWVersion,
       "himSWVerOnProcTable": himSWVerOnProcTable,
       "himSWVerOnProcEntry": himSWVerOnProcEntry,
       "himSWVerOnProcPabxId": himSWVerOnProcPabxId,
       "himSWVerOnProcSrc": himSWVerOnProcSrc,
       "himSWVerOnProcSWVer": himSWVerOnProcSWVer,
       "himSWVerOnProcItemCodeNoPrefix": himSWVerOnProcItemCodeNoPrefix,
       "himSWVerOnProcHP4KVer": himSWVerOnProcHP4KVer,
       "himSWVerOnProcSysRel": himSWVerOnProcSysRel,
       "himSWVerOnProcCountry": himSWVerOnProcCountry,
       "himSWVerOnProcCountryCode": himSWVerOnProcCountryCode,
       "himSWVerOnProcRevNo": himSWVerOnProcRevNo,
       "himSwPkgVersion": himSwPkgVersion,
       "himSWPkgVerTable": himSWPkgVerTable,
       "himSWPkgVerEntry": himSWPkgVerEntry,
       "himSWPkgVerPabxId": himSWPkgVerPabxId,
       "himSWPkgVerPkgAbbr": himSWPkgVerPkgAbbr,
       "himSWPkgVerPkgName": himSWPkgVerPkgName,
       "himSWPkgVerVersion": himSWPkgVerVersion,
       "himSWPkgVerInstAt": himSWPkgVerInstAt,
       "himSWPkgVerStatus": himSWPkgVerStatus,
       "himSystem": himSystem,
       "himSysBasicTable": himSysBasicTable,
       "himSysBasicEntry": himSysBasicEntry,
       "himSysBasicPabxId": himSysBasicPabxId,
       "himSysBasicDomain": himSysBasicDomain,
       "himSysBasicNodeNo": himSysBasicNodeNo,
       "himSysBasicLEGK": himSysBasicLEGK,
       "himSysLANCardsTable": himSysLANCardsTable,
       "himSysLANCardsEntry": himSysLANCardsEntry,
       "himSysLANCardsPabxId": himSysLANCardsPabxId,
       "himSysLANCardsIPAddr": himSysLANCardsIPAddr,
       "himSysLANCardsNetMask": himSysLANCardsNetMask,
       "himSysLANCardsBroadCast": himSysLANCardsBroadCast,
       "himSysLANCardsType": himSysLANCardsType,
       "himSysLANCardsStatus": himSysLANCardsStatus,
       "himSysHostsTable": himSysHostsTable,
       "himSysHostsEntry": himSysHostsEntry,
       "himSysHostsPabxId": himSysHostsPabxId,
       "himSysHostsNo": himSysHostsNo,
       "himSysHostsIPAddr": himSysHostsIPAddr,
       "himSysHostsName": himSysHostsName,
       "himSysWAMLConn": himSysWAMLConn,
       "himSysWAMLConnTable": himSysWAMLConnTable,
       "himSysWAMLConnEntry": himSysWAMLConnEntry,
       "himSysWAMLConnPabxId": himSysWAMLConnPabxId,
       "himSysWAMLConnLTG": himSysWAMLConnLTG,
       "himSysWAMLConnLTU": himSysWAMLConnLTU,
       "himSysWAMLConnSlot": himSysWAMLConnSlot,
       "himSysWAMLConnRufNr": himSysWAMLConnRufNr,
       "himSysWAMLConnBChl": himSysWAMLConnBChl,
       "himSysWAMLConnStatus": himSysWAMLConnStatus,
       "himSysWAMLConnIPTable": himSysWAMLConnIPTable,
       "himSysWAMLConnIPEntry": himSysWAMLConnIPEntry,
       "himSysWAMLConnIPPabxId": himSysWAMLConnIPPabxId,
       "himSysWAMLConnIPLTG": himSysWAMLConnIPLTG,
       "himSysWAMLConnIPLTU": himSysWAMLConnIPLTU,
       "himSysWAMLConnIPSlot": himSysWAMLConnIPSlot,
       "himSysWAMLConnIPIfName": himSysWAMLConnIPIfName,
       "himSysWAMLConnIPAddr": himSysWAMLConnIPAddr,
       "himSysWAMLConnIPNetMask": himSysWAMLConnIPNetMask,
       "himBoards": himBoards,
       "himBoardBasicTable": himBoardBasicTable,
       "himBoardBasicEntry": himBoardBasicEntry,
       "himBoardBasicPabxId": himBoardBasicPabxId,
       "himBoardBasicLTG": himBoardBasicLTG,
       "himBoardBasicLTU": himBoardBasicLTU,
       "himBoardBasicSlot": himBoardBasicSlot,
       "himBoardBasicFuncId": himBoardBasicFuncId,
       "himBoardBasicCat": himBoardBasicCat,
       "himBoardBasicName": himBoardBasicName,
       "himBoardBasicVOIPSec": himBoardBasicVOIPSec,
       "himBoardBasicLWVar": himBoardBasicLWVar,
       "himBoardBasicNoCirc": himBoardBasicNoCirc,
       "himBoardIPTable": himBoardIPTable,
       "himBoardIPEntry": himBoardIPEntry,
       "himBoardIPGwyIPAddr": himBoardIPGwyIPAddr,
       "himBoardIPSrcIPAddr": himBoardIPSrcIPAddr,
       "himBoardIPNetMask": himBoardIPNetMask,
       "himBoardIPDefRouter": himBoardIPDefRouter,
       "himBoardIPCustLANIP": himBoardIPCustLANIP,
       "himBoardIPSTMI2IGWSubMask": himBoardIPSTMI2IGWSubMask,
       "himBoardIPDefGWIP": himBoardIPDefGWIP,
       "himBoardIPManStatIP": himBoardIPManStatIP,
       "himBoardIPManStatPort": himBoardIPManStatPort,
       "himBoardIPBckpServIP": himBoardIPBckpServIP,
       "himBoardIPBckpServPort": himBoardIPBckpServPort,
       "himBoardLocTable": himBoardLocTable,
       "himBoardLocEntry": himBoardLocEntry,
       "himBoardLocId": himBoardLocId,
       "himBoardLocLoc": himBoardLocLoc,
       "himBoardLocPhoneNo": himBoardLocPhoneNo,
       "himBoardLocFaxNo": himBoardLocFaxNo,
       "himIPDA": himIPDA,
       "himIPDAGenData": himIPDAGenData,
       "himIPDAGenTable": himIPDAGenTable,
       "himIPDAGenEntry": himIPDAGenEntry,
       "himIPDAGenPabxId": himIPDAGenPabxId,
       "himIPDAGenSpeed": himIPDAGenSpeed,
       "himIPDAGenMode": himIPDAGenMode,
       "himIPDAGenPayConn": himIPDAGenPayConn,
       "himIPDAGenSigConn": himIPDAGenSigConn,
       "himIPDAGenIPTable": himIPDAGenIPTable,
       "himIPDAGenIPEntry": himIPDAGenIPEntry,
       "himIPDAGenIPNetAddr": himIPDAGenIPNetAddr,
       "himIPDAGenIPNetMask": himIPDAGenIPNetMask,
       "himIPDAGenIPCCAAddr": himIPDAGenIPCCAAddr,
       "himIPDAGenIPCCBAddr": himIPDAGenIPCCBAddr,
       "himIPDAGenIPDefRoutAddr": himIPDAGenIPDefRoutAddr,
       "himIPDAGenIPSurvNetAddr": himIPDAGenIPSurvNetAddr,
       "himIPDAAPData": himIPDAAPData,
       "himIPDABasicTable": himIPDABasicTable,
       "himIPDABasicEntry": himIPDABasicEntry,
       "himIPDABasicPabxId": himIPDABasicPabxId,
       "himIPDABasicLTU": himIPDABasicLTU,
       "himIPDABasicConnType": himIPDABasicConnType,
       "himIPDABasicBChanNo": himIPDABasicBChanNo,
       "himIPDABasicConvAMLaw": himIPDABasicConvAMLaw,
       "himIPDAIPTable": himIPDAIPTable,
       "himIPDAIPEntry": himIPDAIPEntry,
       "himIPDAIPAccPtAddr": himIPDAIPAccPtAddr,
       "himIPDAIPTAccPtAddr": himIPDAIPTAccPtAddr,
       "himIPDAIPAccPtRoutAddr": himIPDAIPAccPtRoutAddr,
       "himIPDAIPNetMaskNW": himIPDAIPNetMaskNW,
       "himIPDAIPAccPtPriRoutAddr": himIPDAIPAccPtPriRoutAddr,
       "himIPDAIPNetMaskDL": himIPDAIPNetMaskDL,
       "himIPDALocTable": himIPDALocTable,
       "himIPDALocEntry": himIPDALocEntry,
       "himIPDALocId": himIPDALocId,
       "himIPDALocLoc": himIPDALocLoc,
       "himIPDALocPhoneNo": himIPDALocPhoneNo,
       "himIPDALocFaxNo": himIPDALocFaxNo,
       "himInfo": himInfo,
       "himSubagentLastMsgNo": himSubagentLastMsgNo,
       "himSubagentLastMsgText": himSubagentLastMsgText,
       "himResultData": himResultData,
       "himDiscovery": himDiscovery,
       "himChanges": himChanges,
       "himDiscovTable": himDiscovTable,
       "himDiscovEntry": himDiscovEntry,
       "himDiscovPabxId": himDiscovPabxId,
       "himDiscovPabxMnemonic": himDiscovPabxMnemonic,
       "himDiscovStatus": himDiscovStatus,
       "himDiscovMode": himDiscovMode,
       "himDiscovTimDat": himDiscovTimDat,
       "himDiscovErrTimDat": himDiscovErrTimDat,
       "himMibConformance": himMibConformance,
       "himMibGroups": himMibGroups,
       "himWelcomePageGroup": himWelcomePageGroup,
       "himSwitchDataGroup": himSwitchDataGroup,
       "himSpecGroup": himSpecGroup,
       "himSWUPeripheryGroup": himSWUPeripheryGroup,
       "himCentralSwitchGroup": himCentralSwitchGroup,
       "himGeneralSwitchGroup": himGeneralSwitchGroup,
       "himFeaturesGroup": himFeaturesGroup,
       "himAPSPatchesGroup": himAPSPatchesGroup,
       "himSWVersionGroup": himSWVersionGroup,
       "himSWPkgVersionGroup": himSWPkgVersionGroup,
       "himSystemGroup": himSystemGroup,
       "himBoardsGroup": himBoardsGroup,
       "himIPDAGroup": himIPDAGroup,
       "himInfoGroup": himInfoGroup,
       "himDiscoveryGroup": himDiscoveryGroup,
       "himTrapsGroup": himTrapsGroup,
       "himTrapGroup": himTrapGroup,
       "himTrapVariables": himTrapVariables,
       "himTrapPabxId": himTrapPabxId,
       "himTrapPabxMnemonic": himTrapPabxMnemonic,
       "himTraps": himTraps,
       "internalMessageHimSubagent": internalMessageHimSubagent,
       "internalWarningHimSubagent": internalWarningHimSubagent,
       "internalErrorHimSubagent": internalErrorHimSubagent,
       "himDiscovSucc": himDiscovSucc,
       "himDiscovErr": himDiscovErr,
       "himDiscovBusy": himDiscovBusy}
)
