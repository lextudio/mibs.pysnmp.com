# SNMP MIB module (SVRSYS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SVRSYS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:58:46 2024
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
 TimeTicks,
 Unsigned32,
 enterprises,
 iso,
 mgmt) = mibBuilder.importSymbols(
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
    "iso",
    "mgmt")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class KBytes(Integer32):
    """Custom type KBytes based on Integer32"""




class BusTypes(Integer32):
    """Custom type BusTypes based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("cBus", 12),
          ("eisa", 5),
          ("isa", 4),
          ("mca", 6),
          ("mpi", 13),
          ("mpsa", 14),
          ("nuBus", 10),
          ("other", 2),
          ("pci", 8),
          ("pcmcia", 11),
          ("systemBus", 3),
          ("turbochannel", 7),
          ("unknown", 1),
          ("usb", 15),
          ("vme", 9))
    )





class SystemStatus(Integer32):
    """Custom type SystemStatus based on Integer32"""
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
        *(("failed", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )





class MemoryAddress(OctetString):
    """Custom type MemoryAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )





class ThermUnits(Integer32):
    """Custom type ThermUnits based on Integer32"""
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
        *(("degreesC", 4),
          ("degreesF", 3),
          ("other", 2),
          ("tempRelative", 5),
          ("unknown", 1))
    )





class PowerUnits(Integer32):
    """Custom type PowerUnits based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("ampsAC", 10),
          ("ampsDC", 9),
          ("milliAmpsAC", 8),
          ("milliAmpsDC", 7),
          ("milliVoltsAC", 4),
          ("milliVoltsDC", 3),
          ("other", 2),
          ("relative", 11),
          ("unknown", 1),
          ("voltsAC", 6),
          ("voltsDC", 5))
    )





class Boolean(Integer32):
    """Custom type Boolean based on Integer32"""
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




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dec_ObjectIdentity = ObjectIdentity
dec = _Dec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36)
)
_Ema_ObjectIdentity = ObjectIdentity
ema = _Ema_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2)
)
_Mib_extensions_1_ObjectIdentity = ObjectIdentity
mib_extensions_1 = _Mib_extensions_1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18)
)
_SvrSystem_ObjectIdentity = ObjectIdentity
svrSystem = _SvrSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22)
)
_SvrBaseSystem_ObjectIdentity = ObjectIdentity
svrBaseSystem = _SvrBaseSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1)
)
_SvrSysMibInfo_ObjectIdentity = ObjectIdentity
svrSysMibInfo = _SvrSysMibInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 1)
)
_SvrSysMibMajorRev_Type = Integer32
_SvrSysMibMajorRev_Object = MibScalar
svrSysMibMajorRev = _SvrSysMibMajorRev_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 1, 1),
    _SvrSysMibMajorRev_Type()
)
svrSysMibMajorRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrSysMibMajorRev.setStatus("mandatory")
_SvrSysMibMinorRev_Type = Integer32
_SvrSysMibMinorRev_Object = MibScalar
svrSysMibMinorRev = _SvrSysMibMinorRev_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 1, 2),
    _SvrSysMibMinorRev_Type()
)
svrSysMibMinorRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrSysMibMinorRev.setStatus("mandatory")
_SvrBaseSysDescr_ObjectIdentity = ObjectIdentity
svrBaseSysDescr = _SvrBaseSysDescr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 2)
)


class _SvrSystemFamily_Type(Integer32):
    """Custom type svrSystemFamily based on Integer32"""
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
        *(("alpha", 4),
          ("other", 2),
          ("unknown", 1),
          ("x86", 3))
    )


_SvrSystemFamily_Type.__name__ = "Integer32"
_SvrSystemFamily_Object = MibScalar
svrSystemFamily = _SvrSystemFamily_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 2, 1),
    _SvrSystemFamily_Type()
)
svrSystemFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrSystemFamily.setStatus("mandatory")
_SvrSystemModel_Type = DisplayString
_SvrSystemModel_Object = MibScalar
svrSystemModel = _SvrSystemModel_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 2, 2),
    _SvrSystemModel_Type()
)
svrSystemModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrSystemModel.setStatus("mandatory")
_SvrSystemDescr_Type = DisplayString
_SvrSystemDescr_Object = MibScalar
svrSystemDescr = _SvrSystemDescr_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 2, 3),
    _SvrSystemDescr_Type()
)
svrSystemDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrSystemDescr.setStatus("mandatory")
_SvrSystemBoardFruIndex_Type = Integer32
_SvrSystemBoardFruIndex_Object = MibScalar
svrSystemBoardFruIndex = _SvrSystemBoardFruIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 2, 4),
    _SvrSystemBoardFruIndex_Type()
)
svrSystemBoardFruIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrSystemBoardFruIndex.setStatus("mandatory")
_SvrSystemOCPDisplay_Type = DisplayString
_SvrSystemOCPDisplay_Object = MibScalar
svrSystemOCPDisplay = _SvrSystemOCPDisplay_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 2, 5),
    _SvrSystemOCPDisplay_Type()
)
svrSystemOCPDisplay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svrSystemOCPDisplay.setStatus("mandatory")


class _SvrSystemBootedOS_Type(Integer32):
    """Custom type svrSystemBootedOS based on Integer32"""
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
        *(("digitalUnix", 6),
          ("netWare", 4),
          ("openVms", 7),
          ("other", 2),
          ("scoUnix", 5),
          ("unknown", 1),
          ("windows", 8),
          ("windowsNT", 3))
    )


_SvrSystemBootedOS_Type.__name__ = "Integer32"
_SvrSystemBootedOS_Object = MibScalar
svrSystemBootedOS = _SvrSystemBootedOS_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 2, 6),
    _SvrSystemBootedOS_Type()
)
svrSystemBootedOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrSystemBootedOS.setStatus("mandatory")
_SvrSystemBootedOSVersion_Type = DisplayString
_SvrSystemBootedOSVersion_Object = MibScalar
svrSystemBootedOSVersion = _SvrSystemBootedOSVersion_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 2, 7),
    _SvrSystemBootedOSVersion_Type()
)
svrSystemBootedOSVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrSystemBootedOSVersion.setStatus("mandatory")
_SvrSystemShutdownReason_Type = DisplayString
_SvrSystemShutdownReason_Object = MibScalar
svrSystemShutdownReason = _SvrSystemShutdownReason_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 2, 8),
    _SvrSystemShutdownReason_Type()
)
svrSystemShutdownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrSystemShutdownReason.setStatus("mandatory")
_SvrSystemRemoteMgrNum_Type = DisplayString
_SvrSystemRemoteMgrNum_Object = MibScalar
svrSystemRemoteMgrNum = _SvrSystemRemoteMgrNum_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 2, 9),
    _SvrSystemRemoteMgrNum_Type()
)
svrSystemRemoteMgrNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svrSystemRemoteMgrNum.setStatus("mandatory")
_SvrFirmwareTable_Object = MibTable
svrFirmwareTable = _SvrFirmwareTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 2, 10)
)
if mibBuilder.loadTexts:
    svrFirmwareTable.setStatus("mandatory")
_SvrFirmwareEntry_Object = MibTableRow
svrFirmwareEntry = _SvrFirmwareEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 2, 10, 1)
)
svrFirmwareEntry.setIndexNames(
    (0, "SVRSYS-MIB", "svrFirmwareIndex"),
)
if mibBuilder.loadTexts:
    svrFirmwareEntry.setStatus("mandatory")
_SvrFirmwareIndex_Type = Integer32
_SvrFirmwareIndex_Object = MibTableColumn
svrFirmwareIndex = _SvrFirmwareIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 2, 10, 1, 1),
    _SvrFirmwareIndex_Type()
)
svrFirmwareIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrFirmwareIndex.setStatus("mandatory")
_SvrFirmwareDescr_Type = DisplayString
_SvrFirmwareDescr_Object = MibTableColumn
svrFirmwareDescr = _SvrFirmwareDescr_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 2, 10, 1, 2),
    _SvrFirmwareDescr_Type()
)
svrFirmwareDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrFirmwareDescr.setStatus("mandatory")
_SvrFirmwareRev_Type = DisplayString
_SvrFirmwareRev_Object = MibTableColumn
svrFirmwareRev = _SvrFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 2, 10, 1, 3),
    _SvrFirmwareRev_Type()
)
svrFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrFirmwareRev.setStatus("mandatory")
_SvrFwSymbolTable_Object = MibTable
svrFwSymbolTable = _SvrFwSymbolTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 2, 11)
)
if mibBuilder.loadTexts:
    svrFwSymbolTable.setStatus("mandatory")
_SvrFwSymbolEntry_Object = MibTableRow
svrFwSymbolEntry = _SvrFwSymbolEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 2, 11, 1)
)
svrFwSymbolEntry.setIndexNames(
    (0, "SVRSYS-MIB", "svrFwSymbolName"),
)
if mibBuilder.loadTexts:
    svrFwSymbolEntry.setStatus("mandatory")
_SvrFwSymbolName_Type = DisplayString
_SvrFwSymbolName_Object = MibTableColumn
svrFwSymbolName = _SvrFwSymbolName_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 2, 11, 1, 1),
    _SvrFwSymbolName_Type()
)
svrFwSymbolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrFwSymbolName.setStatus("mandatory")
_SvrFwSymbolValue_Type = OctetString
_SvrFwSymbolValue_Object = MibTableColumn
svrFwSymbolValue = _SvrFwSymbolValue_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 2, 11, 1, 2),
    _SvrFwSymbolValue_Type()
)
svrFwSymbolValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrFwSymbolValue.setStatus("mandatory")
_SvrProcessors_ObjectIdentity = ObjectIdentity
svrProcessors = _SvrProcessors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 3)
)
_SvrCpuPollInterval_Type = Integer32
_SvrCpuPollInterval_Object = MibScalar
svrCpuPollInterval = _SvrCpuPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 3, 1),
    _SvrCpuPollInterval_Type()
)
svrCpuPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svrCpuPollInterval.setStatus("mandatory")
_SvrCpuMinPollInterval_Type = Integer32
_SvrCpuMinPollInterval_Object = MibScalar
svrCpuMinPollInterval = _SvrCpuMinPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 3, 2),
    _SvrCpuMinPollInterval_Type()
)
svrCpuMinPollInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrCpuMinPollInterval.setStatus("mandatory")
_SvrCpuTable_Object = MibTable
svrCpuTable = _SvrCpuTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 3, 3)
)
if mibBuilder.loadTexts:
    svrCpuTable.setStatus("mandatory")
_SvrCpuEntry_Object = MibTableRow
svrCpuEntry = _SvrCpuEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 3, 3, 1)
)
svrCpuEntry.setIndexNames(
    (0, "SVRSYS-MIB", "svrCpuIndex"),
)
if mibBuilder.loadTexts:
    svrCpuEntry.setStatus("mandatory")
_SvrCpuIndex_Type = Integer32
_SvrCpuIndex_Object = MibTableColumn
svrCpuIndex = _SvrCpuIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 3, 3, 1, 1),
    _SvrCpuIndex_Type()
)
svrCpuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrCpuIndex.setStatus("mandatory")


class _SvrCpuType_Type(Integer32):
    """Custom type svrCpuType based on Integer32"""
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
        *(("alpha21064", 7),
          ("alpha21164", 8),
          ("i386", 3),
          ("i486", 4),
          ("other", 2),
          ("pentium", 5),
          ("pentiumPro", 6),
          ("unknown", 1))
    )


_SvrCpuType_Type.__name__ = "Integer32"
_SvrCpuType_Object = MibTableColumn
svrCpuType = _SvrCpuType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 3, 3, 1, 2),
    _SvrCpuType_Type()
)
svrCpuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrCpuType.setStatus("mandatory")
_SvrCpuManufacturer_Type = DisplayString
_SvrCpuManufacturer_Object = MibTableColumn
svrCpuManufacturer = _SvrCpuManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 3, 3, 1, 3),
    _SvrCpuManufacturer_Type()
)
svrCpuManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrCpuManufacturer.setStatus("mandatory")
_SvrCpuRevision_Type = DisplayString
_SvrCpuRevision_Object = MibTableColumn
svrCpuRevision = _SvrCpuRevision_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 3, 3, 1, 4),
    _SvrCpuRevision_Type()
)
svrCpuRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrCpuRevision.setStatus("mandatory")
_SvrCpuFruIndex_Type = Integer32
_SvrCpuFruIndex_Object = MibTableColumn
svrCpuFruIndex = _SvrCpuFruIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 3, 3, 1, 5),
    _SvrCpuFruIndex_Type()
)
svrCpuFruIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrCpuFruIndex.setStatus("mandatory")
_SvrCpuSpeed_Type = Integer32
_SvrCpuSpeed_Object = MibTableColumn
svrCpuSpeed = _SvrCpuSpeed_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 3, 3, 1, 6),
    _SvrCpuSpeed_Type()
)
svrCpuSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrCpuSpeed.setStatus("mandatory")
_SvrCpuUtilCurrent_Type = Integer32
_SvrCpuUtilCurrent_Object = MibTableColumn
svrCpuUtilCurrent = _SvrCpuUtilCurrent_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 3, 3, 1, 7),
    _SvrCpuUtilCurrent_Type()
)
svrCpuUtilCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrCpuUtilCurrent.setStatus("mandatory")
_SvrCpuAvgNextIndex_Type = Integer32
_SvrCpuAvgNextIndex_Object = MibTableColumn
svrCpuAvgNextIndex = _SvrCpuAvgNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 3, 3, 1, 8),
    _SvrCpuAvgNextIndex_Type()
)
svrCpuAvgNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrCpuAvgNextIndex.setStatus("mandatory")
_SvrCpuHrIndex_Type = Integer32
_SvrCpuHrIndex_Object = MibTableColumn
svrCpuHrIndex = _SvrCpuHrIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 3, 3, 1, 9),
    _SvrCpuHrIndex_Type()
)
svrCpuHrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrCpuHrIndex.setStatus("mandatory")
_SvrCpuAvgTable_Object = MibTable
svrCpuAvgTable = _SvrCpuAvgTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 3, 4)
)
if mibBuilder.loadTexts:
    svrCpuAvgTable.setStatus("mandatory")
_SvrCpuAvgEntry_Object = MibTableRow
svrCpuAvgEntry = _SvrCpuAvgEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 3, 4, 1)
)
svrCpuAvgEntry.setIndexNames(
    (0, "SVRSYS-MIB", "svrCpuIndex"),
    (0, "SVRSYS-MIB", "svrCpuAvgIndex"),
)
if mibBuilder.loadTexts:
    svrCpuAvgEntry.setStatus("mandatory")
_SvrCpuAvgIndex_Type = Integer32
_SvrCpuAvgIndex_Object = MibTableColumn
svrCpuAvgIndex = _SvrCpuAvgIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 3, 4, 1, 1),
    _SvrCpuAvgIndex_Type()
)
svrCpuAvgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrCpuAvgIndex.setStatus("mandatory")
_SvrCpuAvgInterval_Type = Integer32
_SvrCpuAvgInterval_Object = MibTableColumn
svrCpuAvgInterval = _SvrCpuAvgInterval_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 3, 4, 1, 2),
    _SvrCpuAvgInterval_Type()
)
svrCpuAvgInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svrCpuAvgInterval.setStatus("mandatory")


class _SvrCpuAvgStatus_Type(Integer32):
    """Custom type svrCpuAvgStatus based on Integer32"""
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
        *(("rowDisabled", 4),
          ("rowEnabled", 3),
          ("rowError", 5),
          ("rowInvalid", 2),
          ("underCreation", 1))
    )


_SvrCpuAvgStatus_Type.__name__ = "Integer32"
_SvrCpuAvgStatus_Object = MibTableColumn
svrCpuAvgStatus = _SvrCpuAvgStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 3, 4, 1, 3),
    _SvrCpuAvgStatus_Type()
)
svrCpuAvgStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svrCpuAvgStatus.setStatus("mandatory")
_SvrCpuAvgPersist_Type = Boolean
_SvrCpuAvgPersist_Object = MibTableColumn
svrCpuAvgPersist = _SvrCpuAvgPersist_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 3, 4, 1, 4),
    _SvrCpuAvgPersist_Type()
)
svrCpuAvgPersist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svrCpuAvgPersist.setStatus("mandatory")
_SvrCpuAvgValue_Type = Integer32
_SvrCpuAvgValue_Object = MibTableColumn
svrCpuAvgValue = _SvrCpuAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 3, 4, 1, 5),
    _SvrCpuAvgValue_Type()
)
svrCpuAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrCpuAvgValue.setStatus("mandatory")
_SvrCpuCacheTable_Object = MibTable
svrCpuCacheTable = _SvrCpuCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 3, 5)
)
if mibBuilder.loadTexts:
    svrCpuCacheTable.setStatus("mandatory")
_SvrCpuCacheEntry_Object = MibTableRow
svrCpuCacheEntry = _SvrCpuCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 3, 5, 1)
)
svrCpuCacheEntry.setIndexNames(
    (0, "SVRSYS-MIB", "svrCpuIndex"),
    (0, "SVRSYS-MIB", "svrCpuCacheIndex"),
)
if mibBuilder.loadTexts:
    svrCpuCacheEntry.setStatus("mandatory")
_SvrCpuCacheIndex_Type = Integer32
_SvrCpuCacheIndex_Object = MibTableColumn
svrCpuCacheIndex = _SvrCpuCacheIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 3, 5, 1, 1),
    _SvrCpuCacheIndex_Type()
)
svrCpuCacheIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrCpuCacheIndex.setStatus("mandatory")


class _SvrCpuCacheLevel_Type(Integer32):
    """Custom type svrCpuCacheLevel based on Integer32"""
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
        *(("other", 2),
          ("primary", 3),
          ("secondary", 4),
          ("tertiary", 5),
          ("unknown", 1))
    )


_SvrCpuCacheLevel_Type.__name__ = "Integer32"
_SvrCpuCacheLevel_Object = MibTableColumn
svrCpuCacheLevel = _SvrCpuCacheLevel_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 3, 5, 1, 2),
    _SvrCpuCacheLevel_Type()
)
svrCpuCacheLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrCpuCacheLevel.setStatus("mandatory")


class _SvrCpuCacheType_Type(Integer32):
    """Custom type svrCpuCacheType based on Integer32"""
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
        *(("external", 2),
          ("internal", 1),
          ("internalD", 4),
          ("internalI", 3))
    )


_SvrCpuCacheType_Type.__name__ = "Integer32"
_SvrCpuCacheType_Object = MibTableColumn
svrCpuCacheType = _SvrCpuCacheType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 3, 5, 1, 3),
    _SvrCpuCacheType_Type()
)
svrCpuCacheType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrCpuCacheType.setStatus("mandatory")
_SvrCpuCacheSize_Type = KBytes
_SvrCpuCacheSize_Object = MibTableColumn
svrCpuCacheSize = _SvrCpuCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 3, 5, 1, 4),
    _SvrCpuCacheSize_Type()
)
svrCpuCacheSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrCpuCacheSize.setStatus("mandatory")
_SvrCpuCacheSpeed_Type = Integer32
_SvrCpuCacheSpeed_Object = MibTableColumn
svrCpuCacheSpeed = _SvrCpuCacheSpeed_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 3, 5, 1, 5),
    _SvrCpuCacheSpeed_Type()
)
svrCpuCacheSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrCpuCacheSpeed.setStatus("mandatory")


class _SvrCpuCacheStatus_Type(Integer32):
    """Custom type svrCpuCacheStatus based on Integer32"""
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
        *(("disabled", 4),
          ("enabled", 3),
          ("other", 2),
          ("unknown", 1))
    )


_SvrCpuCacheStatus_Type.__name__ = "Integer32"
_SvrCpuCacheStatus_Object = MibTableColumn
svrCpuCacheStatus = _SvrCpuCacheStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 3, 5, 1, 6),
    _SvrCpuCacheStatus_Type()
)
svrCpuCacheStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrCpuCacheStatus.setStatus("mandatory")
_SvrMemory_ObjectIdentity = ObjectIdentity
svrMemory = _SvrMemory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 4)
)
_SvrPhysicalMemorySize_Type = KBytes
_SvrPhysicalMemorySize_Object = MibScalar
svrPhysicalMemorySize = _SvrPhysicalMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 4, 1),
    _SvrPhysicalMemorySize_Type()
)
svrPhysicalMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrPhysicalMemorySize.setStatus("mandatory")
_SvrPhysicalMemoryFree_Type = KBytes
_SvrPhysicalMemoryFree_Object = MibScalar
svrPhysicalMemoryFree = _SvrPhysicalMemoryFree_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 4, 2),
    _SvrPhysicalMemoryFree_Type()
)
svrPhysicalMemoryFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrPhysicalMemoryFree.setStatus("mandatory")
_SvrPagingMemorySize_Type = KBytes
_SvrPagingMemorySize_Object = MibScalar
svrPagingMemorySize = _SvrPagingMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 4, 3),
    _SvrPagingMemorySize_Type()
)
svrPagingMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrPagingMemorySize.setStatus("mandatory")
_SvrPagingMemoryFree_Type = KBytes
_SvrPagingMemoryFree_Object = MibScalar
svrPagingMemoryFree = _SvrPagingMemoryFree_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 4, 4),
    _SvrPagingMemoryFree_Type()
)
svrPagingMemoryFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrPagingMemoryFree.setStatus("mandatory")
_SvrMemComponentTable_Object = MibTable
svrMemComponentTable = _SvrMemComponentTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 4, 5)
)
if mibBuilder.loadTexts:
    svrMemComponentTable.setStatus("mandatory")
_SvrMemComponentEntry_Object = MibTableRow
svrMemComponentEntry = _SvrMemComponentEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 4, 5, 1)
)
svrMemComponentEntry.setIndexNames(
    (0, "SVRSYS-MIB", "svrMemIndex"),
)
if mibBuilder.loadTexts:
    svrMemComponentEntry.setStatus("mandatory")
_SvrMemIndex_Type = Integer32
_SvrMemIndex_Object = MibTableColumn
svrMemIndex = _SvrMemIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 4, 5, 1, 1),
    _SvrMemIndex_Type()
)
svrMemIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrMemIndex.setStatus("optional")


class _SvrMemType_Type(Integer32):
    """Custom type svrMemType based on Integer32"""
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
        *(("expansionROM", 9),
          ("expansionRam", 8),
          ("flashMemory", 6),
          ("nvram", 7),
          ("other", 2),
          ("shadowMemory", 4),
          ("systemMemory", 3),
          ("unknown", 1),
          ("videoMemory", 5))
    )


_SvrMemType_Type.__name__ = "Integer32"
_SvrMemType_Object = MibTableColumn
svrMemType = _SvrMemType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 4, 5, 1, 2),
    _SvrMemType_Type()
)
svrMemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrMemType.setStatus("optional")
_SvrMemSize_Type = KBytes
_SvrMemSize_Object = MibTableColumn
svrMemSize = _SvrMemSize_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 4, 5, 1, 3),
    _SvrMemSize_Type()
)
svrMemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrMemSize.setStatus("optional")
_SvrMemStartAddress_Type = MemoryAddress
_SvrMemStartAddress_Object = MibTableColumn
svrMemStartAddress = _SvrMemStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 4, 5, 1, 4),
    _SvrMemStartAddress_Type()
)
svrMemStartAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrMemStartAddress.setStatus("optional")


class _SvrMemPhysLocation_Type(Integer32):
    """Custom type svrMemPhysLocation based on Integer32"""
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
        *(("memoryBoard", 4),
          ("other", 2),
          ("processorBoard", 5),
          ("systemBoard", 3),
          ("unknown", 1))
    )


_SvrMemPhysLocation_Type.__name__ = "Integer32"
_SvrMemPhysLocation_Object = MibTableColumn
svrMemPhysLocation = _SvrMemPhysLocation_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 4, 5, 1, 5),
    _SvrMemPhysLocation_Type()
)
svrMemPhysLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrMemPhysLocation.setStatus("mandatory")


class _SvrMemEdcType_Type(Integer32):
    """Custom type svrMemEdcType based on Integer32"""
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
        *(("multiBitECC", 6),
          ("none", 3),
          ("other", 2),
          ("parity", 4),
          ("singleBitECC", 5),
          ("unknown", 1))
    )


_SvrMemEdcType_Type.__name__ = "Integer32"
_SvrMemEdcType_Object = MibTableColumn
svrMemEdcType = _SvrMemEdcType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 4, 5, 1, 6),
    _SvrMemEdcType_Type()
)
svrMemEdcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrMemEdcType.setStatus("mandatory")
_SvrMemElementSlots_Type = Integer32
_SvrMemElementSlots_Object = MibTableColumn
svrMemElementSlots = _SvrMemElementSlots_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 4, 5, 1, 7),
    _SvrMemElementSlots_Type()
)
svrMemElementSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrMemElementSlots.setStatus("mandatory")
_SvrMemElementSlotsUsed_Type = Integer32
_SvrMemElementSlotsUsed_Object = MibTableColumn
svrMemElementSlotsUsed = _SvrMemElementSlotsUsed_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 4, 5, 1, 8),
    _SvrMemElementSlotsUsed_Type()
)
svrMemElementSlotsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrMemElementSlotsUsed.setStatus("mandatory")
_SvrMemInterleafFactor_Type = Integer32
_SvrMemInterleafFactor_Object = MibTableColumn
svrMemInterleafFactor = _SvrMemInterleafFactor_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 4, 5, 1, 9),
    _SvrMemInterleafFactor_Type()
)
svrMemInterleafFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrMemInterleafFactor.setStatus("mandatory")
_SvrMemInterleafElement_Type = Integer32
_SvrMemInterleafElement_Object = MibTableColumn
svrMemInterleafElement = _SvrMemInterleafElement_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 4, 5, 1, 10),
    _SvrMemInterleafElement_Type()
)
svrMemInterleafElement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrMemInterleafElement.setStatus("mandatory")
_SvrMemFruIndex_Type = Integer32
_SvrMemFruIndex_Object = MibTableColumn
svrMemFruIndex = _SvrMemFruIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 4, 5, 1, 11),
    _SvrMemFruIndex_Type()
)
svrMemFruIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrMemFruIndex.setStatus("mandatory")
_SvrMemElementTable_Object = MibTable
svrMemElementTable = _SvrMemElementTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 4, 6)
)
if mibBuilder.loadTexts:
    svrMemElementTable.setStatus("mandatory")
_SvrMemElementEntry_Object = MibTableRow
svrMemElementEntry = _SvrMemElementEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 4, 6, 1)
)
svrMemElementEntry.setIndexNames(
    (0, "SVRSYS-MIB", "svrMemIndex"),
    (0, "SVRSYS-MIB", "svrMemElementIndex"),
)
if mibBuilder.loadTexts:
    svrMemElementEntry.setStatus("mandatory")
_SvrMemElementIndex_Type = Integer32
_SvrMemElementIndex_Object = MibTableColumn
svrMemElementIndex = _SvrMemElementIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 4, 6, 1, 1),
    _SvrMemElementIndex_Type()
)
svrMemElementIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrMemElementIndex.setStatus("mandatory")


class _SvrMemElementType_Type(Integer32):
    """Custom type svrMemElementType based on Integer32"""
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
        *(("dimm", 5),
          ("nonremoveable", 3),
          ("other", 2),
          ("simm", 4),
          ("unknown", 1))
    )


_SvrMemElementType_Type.__name__ = "Integer32"
_SvrMemElementType_Object = MibTableColumn
svrMemElementType = _SvrMemElementType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 4, 6, 1, 2),
    _SvrMemElementType_Type()
)
svrMemElementType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrMemElementType.setStatus("mandatory")
_SvrMemElementSlotNo_Type = Integer32
_SvrMemElementSlotNo_Object = MibTableColumn
svrMemElementSlotNo = _SvrMemElementSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 4, 6, 1, 3),
    _SvrMemElementSlotNo_Type()
)
svrMemElementSlotNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrMemElementSlotNo.setStatus("mandatory")
_SvrMemElementWidth_Type = Integer32
_SvrMemElementWidth_Object = MibTableColumn
svrMemElementWidth = _SvrMemElementWidth_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 4, 6, 1, 4),
    _SvrMemElementWidth_Type()
)
svrMemElementWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrMemElementWidth.setStatus("mandatory")
_SvrMemElementDepth_Type = KBytes
_SvrMemElementDepth_Object = MibTableColumn
svrMemElementDepth = _SvrMemElementDepth_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 4, 6, 1, 5),
    _SvrMemElementDepth_Type()
)
svrMemElementDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrMemElementDepth.setStatus("mandatory")
_SvrMemElementSpeed_Type = Integer32
_SvrMemElementSpeed_Object = MibTableColumn
svrMemElementSpeed = _SvrMemElementSpeed_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 4, 6, 1, 6),
    _SvrMemElementSpeed_Type()
)
svrMemElementSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrMemElementSpeed.setStatus("mandatory")
_SvrMemElementStatus_Type = SystemStatus
_SvrMemElementStatus_Object = MibTableColumn
svrMemElementStatus = _SvrMemElementStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 4, 6, 1, 7),
    _SvrMemElementStatus_Type()
)
svrMemElementStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrMemElementStatus.setStatus("mandatory")
_SvrBuses_ObjectIdentity = ObjectIdentity
svrBuses = _SvrBuses_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 5)
)
_SvrBusCount_Type = Integer32
_SvrBusCount_Object = MibScalar
svrBusCount = _SvrBusCount_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 5, 1),
    _SvrBusCount_Type()
)
svrBusCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrBusCount.setStatus("mandatory")
_SvrBusTable_Object = MibTable
svrBusTable = _SvrBusTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 5, 2)
)
if mibBuilder.loadTexts:
    svrBusTable.setStatus("mandatory")
_SvrBusEntry_Object = MibTableRow
svrBusEntry = _SvrBusEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 5, 2, 1)
)
svrBusEntry.setIndexNames(
    (0, "SVRSYS-MIB", "svrBusIndex"),
)
if mibBuilder.loadTexts:
    svrBusEntry.setStatus("mandatory")
_SvrBusIndex_Type = Integer32
_SvrBusIndex_Object = MibTableColumn
svrBusIndex = _SvrBusIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 5, 2, 1, 1),
    _SvrBusIndex_Type()
)
svrBusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrBusIndex.setStatus("mandatory")
_SvrBusType_Type = BusTypes
_SvrBusType_Object = MibTableColumn
svrBusType = _SvrBusType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 5, 2, 1, 2),
    _SvrBusType_Type()
)
svrBusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrBusType.setStatus("mandatory")
_SvrBusNumber_Type = Integer32
_SvrBusNumber_Object = MibTableColumn
svrBusNumber = _SvrBusNumber_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 5, 2, 1, 3),
    _SvrBusNumber_Type()
)
svrBusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrBusNumber.setStatus("mandatory")
_SvrBusSlotCount_Type = Integer32
_SvrBusSlotCount_Object = MibTableColumn
svrBusSlotCount = _SvrBusSlotCount_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 5, 2, 1, 4),
    _SvrBusSlotCount_Type()
)
svrBusSlotCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrBusSlotCount.setStatus("mandatory")
_SvrLogicalSlotTable_Object = MibTable
svrLogicalSlotTable = _SvrLogicalSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 5, 3)
)
if mibBuilder.loadTexts:
    svrLogicalSlotTable.setStatus("mandatory")
_SvrLogicalSlotEntry_Object = MibTableRow
svrLogicalSlotEntry = _SvrLogicalSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 5, 3, 1)
)
svrLogicalSlotEntry.setIndexNames(
    (0, "SVRSYS-MIB", "svrBusIndex"),
    (0, "SVRSYS-MIB", "svrLogicalSlotNumber"),
)
if mibBuilder.loadTexts:
    svrLogicalSlotEntry.setStatus("mandatory")
_SvrLogicalSlotNumber_Type = Integer32
_SvrLogicalSlotNumber_Object = MibTableColumn
svrLogicalSlotNumber = _SvrLogicalSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 5, 3, 1, 1),
    _SvrLogicalSlotNumber_Type()
)
svrLogicalSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrLogicalSlotNumber.setStatus("mandatory")
_SvrLogicalSlotDescr_Type = DisplayString
_SvrLogicalSlotDescr_Object = MibTableColumn
svrLogicalSlotDescr = _SvrLogicalSlotDescr_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 5, 3, 1, 2),
    _SvrLogicalSlotDescr_Type()
)
svrLogicalSlotDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svrLogicalSlotDescr.setStatus("mandatory")
_SvrLogicalSlotDeviceID_Type = Integer32
_SvrLogicalSlotDeviceID_Object = MibTableColumn
svrLogicalSlotDeviceID = _SvrLogicalSlotDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 5, 3, 1, 3),
    _SvrLogicalSlotDeviceID_Type()
)
svrLogicalSlotDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrLogicalSlotDeviceID.setStatus("mandatory")
_SvrLogicalSlotVendor_Type = DisplayString
_SvrLogicalSlotVendor_Object = MibTableColumn
svrLogicalSlotVendor = _SvrLogicalSlotVendor_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 5, 3, 1, 4),
    _SvrLogicalSlotVendor_Type()
)
svrLogicalSlotVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrLogicalSlotVendor.setStatus("mandatory")
_SvrLogicalSlotRevision_Type = DisplayString
_SvrLogicalSlotRevision_Object = MibTableColumn
svrLogicalSlotRevision = _SvrLogicalSlotRevision_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 5, 3, 1, 5),
    _SvrLogicalSlotRevision_Type()
)
svrLogicalSlotRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrLogicalSlotRevision.setStatus("mandatory")
_SvrLogicalSlotFnCount_Type = Integer32
_SvrLogicalSlotFnCount_Object = MibTableColumn
svrLogicalSlotFnCount = _SvrLogicalSlotFnCount_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 5, 3, 1, 6),
    _SvrLogicalSlotFnCount_Type()
)
svrLogicalSlotFnCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrLogicalSlotFnCount.setStatus("mandatory")
_SvrSlotFunctionTable_Object = MibTable
svrSlotFunctionTable = _SvrSlotFunctionTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 5, 4)
)
if mibBuilder.loadTexts:
    svrSlotFunctionTable.setStatus("mandatory")
_SvrSlotFunctionEntry_Object = MibTableRow
svrSlotFunctionEntry = _SvrSlotFunctionEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 5, 4, 1)
)
svrSlotFunctionEntry.setIndexNames(
    (0, "SVRSYS-MIB", "svrBusIndex"),
    (0, "SVRSYS-MIB", "svrLogicalSlotNumber"),
    (0, "SVRSYS-MIB", "svrSlotFnIndex"),
)
if mibBuilder.loadTexts:
    svrSlotFunctionEntry.setStatus("mandatory")
_SvrSlotFnIndex_Type = Integer32
_SvrSlotFnIndex_Object = MibTableColumn
svrSlotFnIndex = _SvrSlotFnIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 5, 4, 1, 1),
    _SvrSlotFnIndex_Type()
)
svrSlotFnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrSlotFnIndex.setStatus("mandatory")
_SvrSlotFnDevType_Type = DisplayString
_SvrSlotFnDevType_Object = MibTableColumn
svrSlotFnDevType = _SvrSlotFnDevType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 5, 4, 1, 2),
    _SvrSlotFnDevType_Type()
)
svrSlotFnDevType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrSlotFnDevType.setStatus("mandatory")
_SvrSlotFnRevision_Type = DisplayString
_SvrSlotFnRevision_Object = MibTableColumn
svrSlotFnRevision = _SvrSlotFnRevision_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 5, 4, 1, 3),
    _SvrSlotFnRevision_Type()
)
svrSlotFnRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrSlotFnRevision.setStatus("mandatory")
_SvrDevices_ObjectIdentity = ObjectIdentity
svrDevices = _SvrDevices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 6)
)
_SvrDeviceCount_Type = Integer32
_SvrDeviceCount_Object = MibScalar
svrDeviceCount = _SvrDeviceCount_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 6, 1),
    _SvrDeviceCount_Type()
)
svrDeviceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrDeviceCount.setStatus("mandatory")
_SvrSerialPortCount_Type = Integer32
_SvrSerialPortCount_Object = MibScalar
svrSerialPortCount = _SvrSerialPortCount_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 6, 2),
    _SvrSerialPortCount_Type()
)
svrSerialPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrSerialPortCount.setStatus("mandatory")
_SvrParallelPortCount_Type = Integer32
_SvrParallelPortCount_Object = MibScalar
svrParallelPortCount = _SvrParallelPortCount_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 6, 3),
    _SvrParallelPortCount_Type()
)
svrParallelPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrParallelPortCount.setStatus("mandatory")
_SvrConsoleKeyboard_ObjectIdentity = ObjectIdentity
svrConsoleKeyboard = _SvrConsoleKeyboard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 6, 4)
)
_SvrKeybdHrIndex_Type = Integer32
_SvrKeybdHrIndex_Object = MibScalar
svrKeybdHrIndex = _SvrKeybdHrIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 6, 4, 1),
    _SvrKeybdHrIndex_Type()
)
svrKeybdHrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrKeybdHrIndex.setStatus("mandatory")
_SvrKeybdDescr_Type = DisplayString
_SvrKeybdDescr_Object = MibScalar
svrKeybdDescr = _SvrKeybdDescr_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 6, 4, 2),
    _SvrKeybdDescr_Type()
)
svrKeybdDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrKeybdDescr.setStatus("mandatory")
_SvrConsoleDisplay_ObjectIdentity = ObjectIdentity
svrConsoleDisplay = _SvrConsoleDisplay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 6, 5)
)
_SvrVideoHrIndex_Type = Integer32
_SvrVideoHrIndex_Object = MibScalar
svrVideoHrIndex = _SvrVideoHrIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 6, 5, 1),
    _SvrVideoHrIndex_Type()
)
svrVideoHrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrVideoHrIndex.setStatus("mandatory")
_SvrVideoDescr_Type = DisplayString
_SvrVideoDescr_Object = MibScalar
svrVideoDescr = _SvrVideoDescr_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 6, 5, 2),
    _SvrVideoDescr_Type()
)
svrVideoDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrVideoDescr.setStatus("mandatory")
_SvrVideoXRes_Type = Integer32
_SvrVideoXRes_Object = MibScalar
svrVideoXRes = _SvrVideoXRes_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 6, 5, 3),
    _SvrVideoXRes_Type()
)
svrVideoXRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrVideoXRes.setStatus("mandatory")
_SvrVideoYRes_Type = Integer32
_SvrVideoYRes_Object = MibScalar
svrVideoYRes = _SvrVideoYRes_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 6, 5, 4),
    _SvrVideoYRes_Type()
)
svrVideoYRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrVideoYRes.setStatus("mandatory")
_SvrVideoNumColor_Type = Integer32
_SvrVideoNumColor_Object = MibScalar
svrVideoNumColor = _SvrVideoNumColor_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 6, 5, 5),
    _SvrVideoNumColor_Type()
)
svrVideoNumColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrVideoNumColor.setStatus("mandatory")
_SvrVideoRefreshRate_Type = Integer32
_SvrVideoRefreshRate_Object = MibScalar
svrVideoRefreshRate = _SvrVideoRefreshRate_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 6, 5, 6),
    _SvrVideoRefreshRate_Type()
)
svrVideoRefreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrVideoRefreshRate.setStatus("mandatory")


class _SvrVideoScanMode_Type(Integer32):
    """Custom type svrVideoScanMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("interlaced", 2),
          ("nonInterlaced", 3),
          ("unknown", 1))
    )


_SvrVideoScanMode_Type.__name__ = "Integer32"
_SvrVideoScanMode_Object = MibScalar
svrVideoScanMode = _SvrVideoScanMode_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 6, 5, 7),
    _SvrVideoScanMode_Type()
)
svrVideoScanMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrVideoScanMode.setStatus("mandatory")
_SvrVideoMemory_Type = KBytes
_SvrVideoMemory_Object = MibScalar
svrVideoMemory = _SvrVideoMemory_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 6, 5, 8),
    _SvrVideoMemory_Type()
)
svrVideoMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrVideoMemory.setStatus("mandatory")
_SvrConsolePointDevice_ObjectIdentity = ObjectIdentity
svrConsolePointDevice = _SvrConsolePointDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 6, 6)
)
_SvrPointingHrIndex_Type = Integer32
_SvrPointingHrIndex_Object = MibScalar
svrPointingHrIndex = _SvrPointingHrIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 6, 6, 1),
    _SvrPointingHrIndex_Type()
)
svrPointingHrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrPointingHrIndex.setStatus("mandatory")
_SvrPointingDescr_Type = DisplayString
_SvrPointingDescr_Object = MibScalar
svrPointingDescr = _SvrPointingDescr_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 6, 6, 2),
    _SvrPointingDescr_Type()
)
svrPointingDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrPointingDescr.setStatus("mandatory")
_SvrNumButtons_Type = Integer32
_SvrNumButtons_Object = MibScalar
svrNumButtons = _SvrNumButtons_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 6, 6, 3),
    _SvrNumButtons_Type()
)
svrNumButtons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrNumButtons.setStatus("mandatory")
_SvrSerialPortTable_Object = MibTable
svrSerialPortTable = _SvrSerialPortTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 6, 7)
)
if mibBuilder.loadTexts:
    svrSerialPortTable.setStatus("mandatory")
_SvrSerialPortEntry_Object = MibTableRow
svrSerialPortEntry = _SvrSerialPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 6, 7, 1)
)
svrSerialPortEntry.setIndexNames(
    (0, "SVRSYS-MIB", "svrSerialIndex"),
)
if mibBuilder.loadTexts:
    svrSerialPortEntry.setStatus("mandatory")
_SvrSerialIndex_Type = Integer32
_SvrSerialIndex_Object = MibTableColumn
svrSerialIndex = _SvrSerialIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 6, 7, 1, 1),
    _SvrSerialIndex_Type()
)
svrSerialIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrSerialIndex.setStatus("mandatory")
_SvrSerialPortDescr_Type = DisplayString
_SvrSerialPortDescr_Object = MibTableColumn
svrSerialPortDescr = _SvrSerialPortDescr_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 6, 7, 1, 2),
    _SvrSerialPortDescr_Type()
)
svrSerialPortDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrSerialPortDescr.setStatus("mandatory")
_SvrSerialHrIndex_Type = Integer32
_SvrSerialHrIndex_Object = MibTableColumn
svrSerialHrIndex = _SvrSerialHrIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 6, 7, 1, 3),
    _SvrSerialHrIndex_Type()
)
svrSerialHrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrSerialHrIndex.setStatus("mandatory")
_SvrParallelPortTable_Object = MibTable
svrParallelPortTable = _SvrParallelPortTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 6, 8)
)
if mibBuilder.loadTexts:
    svrParallelPortTable.setStatus("mandatory")
_SvrParallelPortEntry_Object = MibTableRow
svrParallelPortEntry = _SvrParallelPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 6, 8, 1)
)
svrParallelPortEntry.setIndexNames(
    (0, "SVRSYS-MIB", "svrParallelIndex"),
)
if mibBuilder.loadTexts:
    svrParallelPortEntry.setStatus("mandatory")
_SvrParallelIndex_Type = Integer32
_SvrParallelIndex_Object = MibTableColumn
svrParallelIndex = _SvrParallelIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 6, 8, 1, 1),
    _SvrParallelIndex_Type()
)
svrParallelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrParallelIndex.setStatus("mandatory")
_SvrParallelPortDescr_Type = DisplayString
_SvrParallelPortDescr_Object = MibTableColumn
svrParallelPortDescr = _SvrParallelPortDescr_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 6, 8, 1, 2),
    _SvrParallelPortDescr_Type()
)
svrParallelPortDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrParallelPortDescr.setStatus("mandatory")
_SvrParallelHrIndex_Type = Integer32
_SvrParallelHrIndex_Object = MibTableColumn
svrParallelHrIndex = _SvrParallelHrIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 6, 8, 1, 3),
    _SvrParallelHrIndex_Type()
)
svrParallelHrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrParallelHrIndex.setStatus("mandatory")
_SvrDeviceTable_Object = MibTable
svrDeviceTable = _SvrDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 6, 9)
)
if mibBuilder.loadTexts:
    svrDeviceTable.setStatus("mandatory")
_SvrDeviceEntry_Object = MibTableRow
svrDeviceEntry = _SvrDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 6, 9, 1)
)
svrDeviceEntry.setIndexNames(
    (0, "SVRSYS-MIB", "svrDevIndex"),
)
if mibBuilder.loadTexts:
    svrDeviceEntry.setStatus("mandatory")
_SvrDevIndex_Type = Integer32
_SvrDevIndex_Object = MibTableColumn
svrDevIndex = _SvrDevIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 6, 9, 1, 1),
    _SvrDevIndex_Type()
)
svrDevIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrDevIndex.setStatus("mandatory")
_SvrDevDescr_Type = DisplayString
_SvrDevDescr_Object = MibTableColumn
svrDevDescr = _SvrDevDescr_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 6, 9, 1, 2),
    _SvrDevDescr_Type()
)
svrDevDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrDevDescr.setStatus("mandatory")
_SvrDevBusInterfaceType_Type = BusTypes
_SvrDevBusInterfaceType_Object = MibTableColumn
svrDevBusInterfaceType = _SvrDevBusInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 6, 9, 1, 3),
    _SvrDevBusInterfaceType_Type()
)
svrDevBusInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrDevBusInterfaceType.setStatus("mandatory")
_SvrDevBusNumber_Type = Integer32
_SvrDevBusNumber_Object = MibTableColumn
svrDevBusNumber = _SvrDevBusNumber_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 6, 9, 1, 4),
    _SvrDevBusNumber_Type()
)
svrDevBusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrDevBusNumber.setStatus("mandatory")
_SvrDevSlotNumber_Type = Integer32
_SvrDevSlotNumber_Object = MibTableColumn
svrDevSlotNumber = _SvrDevSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 6, 9, 1, 5),
    _SvrDevSlotNumber_Type()
)
svrDevSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrDevSlotNumber.setStatus("mandatory")
_SvrDevFruIndex_Type = Integer32
_SvrDevFruIndex_Object = MibTableColumn
svrDevFruIndex = _SvrDevFruIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 6, 9, 1, 6),
    _SvrDevFruIndex_Type()
)
svrDevFruIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrDevFruIndex.setStatus("mandatory")
_SvrDevCPUAffinity_Type = Integer32
_SvrDevCPUAffinity_Object = MibTableColumn
svrDevCPUAffinity = _SvrDevCPUAffinity_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 6, 9, 1, 7),
    _SvrDevCPUAffinity_Type()
)
svrDevCPUAffinity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrDevCPUAffinity.setStatus("mandatory")
_SvrDevHrIndex_Type = Integer32
_SvrDevHrIndex_Object = MibTableColumn
svrDevHrIndex = _SvrDevHrIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 6, 9, 1, 8),
    _SvrDevHrIndex_Type()
)
svrDevHrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrDevHrIndex.setStatus("mandatory")
_SvrDevInterruptTable_Object = MibTable
svrDevInterruptTable = _SvrDevInterruptTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 6, 10)
)
if mibBuilder.loadTexts:
    svrDevInterruptTable.setStatus("mandatory")
_SvrDevIntEntry_Object = MibTableRow
svrDevIntEntry = _SvrDevIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 6, 10, 1)
)
svrDevIntEntry.setIndexNames(
    (0, "SVRSYS-MIB", "svrDevIndex"),
    (0, "SVRSYS-MIB", "svrDevIntIndex"),
)
if mibBuilder.loadTexts:
    svrDevIntEntry.setStatus("mandatory")
_SvrDevIntIndex_Type = Integer32
_SvrDevIntIndex_Object = MibTableColumn
svrDevIntIndex = _SvrDevIntIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 6, 10, 1, 1),
    _SvrDevIntIndex_Type()
)
svrDevIntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrDevIntIndex.setStatus("mandatory")
_SvrDevIntLevel_Type = Integer32
_SvrDevIntLevel_Object = MibTableColumn
svrDevIntLevel = _SvrDevIntLevel_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 6, 10, 1, 2),
    _SvrDevIntLevel_Type()
)
svrDevIntLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrDevIntLevel.setStatus("mandatory")
_SvrDevIntVector_Type = Integer32
_SvrDevIntVector_Object = MibTableColumn
svrDevIntVector = _SvrDevIntVector_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 6, 10, 1, 3),
    _SvrDevIntVector_Type()
)
svrDevIntVector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrDevIntVector.setStatus("mandatory")
_SvrDevIntShared_Type = Boolean
_SvrDevIntShared_Object = MibTableColumn
svrDevIntShared = _SvrDevIntShared_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 6, 10, 1, 4),
    _SvrDevIntShared_Type()
)
svrDevIntShared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrDevIntShared.setStatus("mandatory")


class _SvrDevIntTrigger_Type(Integer32):
    """Custom type svrDevIntTrigger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("latch", 2),
          ("level", 1))
    )


_SvrDevIntTrigger_Type.__name__ = "Integer32"
_SvrDevIntTrigger_Object = MibTableColumn
svrDevIntTrigger = _SvrDevIntTrigger_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 6, 10, 1, 5),
    _SvrDevIntTrigger_Type()
)
svrDevIntTrigger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrDevIntTrigger.setStatus("mandatory")
_SvrDevMemTable_Object = MibTable
svrDevMemTable = _SvrDevMemTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 6, 11)
)
if mibBuilder.loadTexts:
    svrDevMemTable.setStatus("mandatory")
_SvrDevMemEntry_Object = MibTableRow
svrDevMemEntry = _SvrDevMemEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 6, 11, 1)
)
svrDevMemEntry.setIndexNames(
    (0, "SVRSYS-MIB", "svrDevIndex"),
    (0, "SVRSYS-MIB", "svrDevMemIndex"),
)
if mibBuilder.loadTexts:
    svrDevMemEntry.setStatus("mandatory")
_SvrDevMemIndex_Type = Integer32
_SvrDevMemIndex_Object = MibTableColumn
svrDevMemIndex = _SvrDevMemIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 6, 11, 1, 1),
    _SvrDevMemIndex_Type()
)
svrDevMemIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrDevMemIndex.setStatus("mandatory")
_SvrDevMemAddress_Type = MemoryAddress
_SvrDevMemAddress_Object = MibTableColumn
svrDevMemAddress = _SvrDevMemAddress_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 6, 11, 1, 2),
    _SvrDevMemAddress_Type()
)
svrDevMemAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrDevMemAddress.setStatus("mandatory")
_SvrDevMemLength_Type = Integer32
_SvrDevMemLength_Object = MibTableColumn
svrDevMemLength = _SvrDevMemLength_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 6, 11, 1, 3),
    _SvrDevMemLength_Type()
)
svrDevMemLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrDevMemLength.setStatus("mandatory")


class _SvrDevMemMapping_Type(Integer32):
    """Custom type svrDevMemMapping based on Integer32"""
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
        *(("ioSpaceMapped", 4),
          ("memoryMapped", 3),
          ("other", 2),
          ("unknown", 1))
    )


_SvrDevMemMapping_Type.__name__ = "Integer32"
_SvrDevMemMapping_Object = MibTableColumn
svrDevMemMapping = _SvrDevMemMapping_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 6, 11, 1, 4),
    _SvrDevMemMapping_Type()
)
svrDevMemMapping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrDevMemMapping.setStatus("mandatory")
_SvrDevDmaTable_Object = MibTable
svrDevDmaTable = _SvrDevDmaTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 6, 12)
)
if mibBuilder.loadTexts:
    svrDevDmaTable.setStatus("mandatory")
_SvrDevDmaEntry_Object = MibTableRow
svrDevDmaEntry = _SvrDevDmaEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 6, 12, 1)
)
svrDevDmaEntry.setIndexNames(
    (0, "SVRSYS-MIB", "svrDevIndex"),
    (0, "SVRSYS-MIB", "svrDevDmaIndex"),
)
if mibBuilder.loadTexts:
    svrDevDmaEntry.setStatus("mandatory")
_SvrDevDmaIndex_Type = Integer32
_SvrDevDmaIndex_Object = MibTableColumn
svrDevDmaIndex = _SvrDevDmaIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 6, 12, 1, 2),
    _SvrDevDmaIndex_Type()
)
svrDevDmaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrDevDmaIndex.setStatus("mandatory")
_SvrDevDmaChannel_Type = Integer32
_SvrDevDmaChannel_Object = MibTableColumn
svrDevDmaChannel = _SvrDevDmaChannel_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 6, 12, 1, 3),
    _SvrDevDmaChannel_Type()
)
svrDevDmaChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrDevDmaChannel.setStatus("mandatory")
_SvrPhysicalConfiguration_ObjectIdentity = ObjectIdentity
svrPhysicalConfiguration = _SvrPhysicalConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 7)
)


class _SvrChassisType_Type(Integer32):
    """Custom type svrChassisType based on Integer32"""
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
        *(("desktop", 3),
          ("laptop", 7),
          ("miniTower", 5),
          ("other", 2),
          ("rackMount", 6),
          ("tower", 4),
          ("unknown", 1))
    )


_SvrChassisType_Type.__name__ = "Integer32"
_SvrChassisType_Object = MibScalar
svrChassisType = _SvrChassisType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 7, 1),
    _SvrChassisType_Type()
)
svrChassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrChassisType.setStatus("mandatory")
_SvrChassisFruIndex_Type = Integer32
_SvrChassisFruIndex_Object = MibScalar
svrChassisFruIndex = _SvrChassisFruIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 7, 2),
    _SvrChassisFruIndex_Type()
)
svrChassisFruIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrChassisFruIndex.setStatus("mandatory")
_SvrFruTable_Object = MibTable
svrFruTable = _SvrFruTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 7, 3)
)
if mibBuilder.loadTexts:
    svrFruTable.setStatus("mandatory")
_SvrFruEntry_Object = MibTableRow
svrFruEntry = _SvrFruEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 7, 3, 1)
)
svrFruEntry.setIndexNames(
    (0, "SVRSYS-MIB", "svrFruIndex"),
)
if mibBuilder.loadTexts:
    svrFruEntry.setStatus("mandatory")
_SvrFruIndex_Type = Integer32
_SvrFruIndex_Object = MibTableColumn
svrFruIndex = _SvrFruIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 7, 3, 1, 1),
    _SvrFruIndex_Type()
)
svrFruIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrFruIndex.setStatus("mandatory")


class _SvrFruType_Type(Integer32):
    """Custom type svrFruType based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("chassis", 10),
          ("fan", 11),
          ("ioCard", 12),
          ("memoryCard", 5),
          ("memoryModule", 6),
          ("motherBoard", 3),
          ("other", 2),
          ("peripheralDevice", 7),
          ("powerSupply", 9),
          ("processor", 4),
          ("systemBusBridge", 8),
          ("unknown", 1))
    )


_SvrFruType_Type.__name__ = "Integer32"
_SvrFruType_Object = MibTableColumn
svrFruType = _SvrFruType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 7, 3, 1, 2),
    _SvrFruType_Type()
)
svrFruType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrFruType.setStatus("mandatory")
_SvrFruDescr_Type = DisplayString
_SvrFruDescr_Object = MibTableColumn
svrFruDescr = _SvrFruDescr_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 7, 3, 1, 3),
    _SvrFruDescr_Type()
)
svrFruDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svrFruDescr.setStatus("mandatory")
_SvrFruVendor_Type = DisplayString
_SvrFruVendor_Object = MibTableColumn
svrFruVendor = _SvrFruVendor_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 7, 3, 1, 4),
    _SvrFruVendor_Type()
)
svrFruVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrFruVendor.setStatus("mandatory")
_SvrFruPartNumber_Type = DisplayString
_SvrFruPartNumber_Object = MibTableColumn
svrFruPartNumber = _SvrFruPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 7, 3, 1, 5),
    _SvrFruPartNumber_Type()
)
svrFruPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrFruPartNumber.setStatus("mandatory")
_SvrFruRevision_Type = DisplayString
_SvrFruRevision_Object = MibTableColumn
svrFruRevision = _SvrFruRevision_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 7, 3, 1, 6),
    _SvrFruRevision_Type()
)
svrFruRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrFruRevision.setStatus("mandatory")
_SvrFruFirmwareRevision_Type = DisplayString
_SvrFruFirmwareRevision_Object = MibTableColumn
svrFruFirmwareRevision = _SvrFruFirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 7, 3, 1, 7),
    _SvrFruFirmwareRevision_Type()
)
svrFruFirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrFruFirmwareRevision.setStatus("mandatory")
_SvrFruSerialNumber_Type = DisplayString
_SvrFruSerialNumber_Object = MibTableColumn
svrFruSerialNumber = _SvrFruSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 7, 3, 1, 8),
    _SvrFruSerialNumber_Type()
)
svrFruSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrFruSerialNumber.setStatus("mandatory")
_SvrFruAssetNo_Type = DisplayString
_SvrFruAssetNo_Object = MibTableColumn
svrFruAssetNo = _SvrFruAssetNo_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 7, 3, 1, 9),
    _SvrFruAssetNo_Type()
)
svrFruAssetNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svrFruAssetNo.setStatus("mandatory")


class _SvrFruClass_Type(Integer32):
    """Custom type svrFruClass based on Integer32"""
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
        *(("currentBoardInSlot", 3),
          ("other", 2),
          ("parentBoard", 5),
          ("priorBoardInSlot", 4),
          ("priorParentBoard", 6),
          ("priorParentSystem", 7),
          ("unknown", 1))
    )


_SvrFruClass_Type.__name__ = "Integer32"
_SvrFruClass_Object = MibTableColumn
svrFruClass = _SvrFruClass_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 7, 3, 1, 10),
    _SvrFruClass_Type()
)
svrFruClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrFruClass.setStatus("mandatory")
_SvrEnvironment_ObjectIdentity = ObjectIdentity
svrEnvironment = _SvrEnvironment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 8)
)
_SvrThermalSystem_ObjectIdentity = ObjectIdentity
svrThermalSystem = _SvrThermalSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 8, 1)
)
_SvrThermalSensorCount_Type = Integer32
_SvrThermalSensorCount_Object = MibScalar
svrThermalSensorCount = _SvrThermalSensorCount_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 8, 1, 1),
    _SvrThermalSensorCount_Type()
)
svrThermalSensorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrThermalSensorCount.setStatus("mandatory")
_SvrThermalSensorTable_Object = MibTable
svrThermalSensorTable = _SvrThermalSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 8, 1, 2)
)
if mibBuilder.loadTexts:
    svrThermalSensorTable.setStatus("mandatory")
_SvrThermalSensorEntry_Object = MibTableRow
svrThermalSensorEntry = _SvrThermalSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 8, 1, 2, 1)
)
svrThermalSensorEntry.setIndexNames(
    (0, "SVRSYS-MIB", "svrThSensorIndex"),
)
if mibBuilder.loadTexts:
    svrThermalSensorEntry.setStatus("mandatory")
_SvrThSensorIndex_Type = Integer32
_SvrThSensorIndex_Object = MibTableColumn
svrThSensorIndex = _SvrThSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 8, 1, 2, 1, 1),
    _SvrThSensorIndex_Type()
)
svrThSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrThSensorIndex.setStatus("mandatory")
_SvrThSensorLocation_Type = DisplayString
_SvrThSensorLocation_Object = MibTableColumn
svrThSensorLocation = _SvrThSensorLocation_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 8, 1, 2, 1, 2),
    _SvrThSensorLocation_Type()
)
svrThSensorLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svrThSensorLocation.setStatus("mandatory")
_SvrThSensorReading_Type = Integer32
_SvrThSensorReading_Object = MibTableColumn
svrThSensorReading = _SvrThSensorReading_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 8, 1, 2, 1, 3),
    _SvrThSensorReading_Type()
)
svrThSensorReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrThSensorReading.setStatus("mandatory")
_SvrThSensorReadingUnits_Type = ThermUnits
_SvrThSensorReadingUnits_Object = MibTableColumn
svrThSensorReadingUnits = _SvrThSensorReadingUnits_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 8, 1, 2, 1, 4),
    _SvrThSensorReadingUnits_Type()
)
svrThSensorReadingUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrThSensorReadingUnits.setStatus("mandatory")
_SvrThSensorLowThresh_Type = Integer32
_SvrThSensorLowThresh_Object = MibTableColumn
svrThSensorLowThresh = _SvrThSensorLowThresh_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 8, 1, 2, 1, 5),
    _SvrThSensorLowThresh_Type()
)
svrThSensorLowThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrThSensorLowThresh.setStatus("mandatory")
_SvrThSensorHighThresh_Type = Integer32
_SvrThSensorHighThresh_Object = MibTableColumn
svrThSensorHighThresh = _SvrThSensorHighThresh_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 8, 1, 2, 1, 6),
    _SvrThSensorHighThresh_Type()
)
svrThSensorHighThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrThSensorHighThresh.setStatus("mandatory")
_SvrThSensorShutSoonThresh_Type = Integer32
_SvrThSensorShutSoonThresh_Object = MibTableColumn
svrThSensorShutSoonThresh = _SvrThSensorShutSoonThresh_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 8, 1, 2, 1, 7),
    _SvrThSensorShutSoonThresh_Type()
)
svrThSensorShutSoonThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrThSensorShutSoonThresh.setStatus("mandatory")
_SvrThSensorShutNowThresh_Type = Integer32
_SvrThSensorShutNowThresh_Object = MibTableColumn
svrThSensorShutNowThresh = _SvrThSensorShutNowThresh_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 8, 1, 2, 1, 8),
    _SvrThSensorShutNowThresh_Type()
)
svrThSensorShutNowThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrThSensorShutNowThresh.setStatus("mandatory")
_SvrThSensorThreshUnits_Type = ThermUnits
_SvrThSensorThreshUnits_Object = MibTableColumn
svrThSensorThreshUnits = _SvrThSensorThreshUnits_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 8, 1, 2, 1, 9),
    _SvrThSensorThreshUnits_Type()
)
svrThSensorThreshUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrThSensorThreshUnits.setStatus("mandatory")


class _SvrThSensorStatus_Type(Integer32):
    """Custom type svrThSensorStatus based on Integer32"""
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
        *(("high", 7),
          ("highWarning", 6),
          ("low", 3),
          ("lowWarning", 4),
          ("other", 2),
          ("statusOk", 5),
          ("unknown", 1))
    )


_SvrThSensorStatus_Type.__name__ = "Integer32"
_SvrThSensorStatus_Object = MibTableColumn
svrThSensorStatus = _SvrThSensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 8, 1, 2, 1, 10),
    _SvrThSensorStatus_Type()
)
svrThSensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrThSensorStatus.setStatus("mandatory")
_SvrThSensorFruIndex_Type = Integer32
_SvrThSensorFruIndex_Object = MibTableColumn
svrThSensorFruIndex = _SvrThSensorFruIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 8, 1, 2, 1, 11),
    _SvrThSensorFruIndex_Type()
)
svrThSensorFruIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrThSensorFruIndex.setStatus("mandatory")
_SvrCoolingSystem_ObjectIdentity = ObjectIdentity
svrCoolingSystem = _SvrCoolingSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 8, 2)
)
_SvrFanCount_Type = Integer32
_SvrFanCount_Object = MibScalar
svrFanCount = _SvrFanCount_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 8, 2, 1),
    _SvrFanCount_Type()
)
svrFanCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrFanCount.setStatus("mandatory")
_SvrFanTable_Object = MibTable
svrFanTable = _SvrFanTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 8, 2, 2)
)
if mibBuilder.loadTexts:
    svrFanTable.setStatus("mandatory")
_SvrFanEntry_Object = MibTableRow
svrFanEntry = _SvrFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 8, 2, 2, 1)
)
svrFanEntry.setIndexNames(
    (0, "SVRSYS-MIB", "svrFanIndex"),
)
if mibBuilder.loadTexts:
    svrFanEntry.setStatus("mandatory")
_SvrFanIndex_Type = Integer32
_SvrFanIndex_Object = MibTableColumn
svrFanIndex = _SvrFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 8, 2, 2, 1, 1),
    _SvrFanIndex_Type()
)
svrFanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrFanIndex.setStatus("mandatory")
_SvrFanLocation_Type = DisplayString
_SvrFanLocation_Object = MibTableColumn
svrFanLocation = _SvrFanLocation_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 8, 2, 2, 1, 2),
    _SvrFanLocation_Type()
)
svrFanLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svrFanLocation.setStatus("mandatory")


class _SvrFanStatus_Type(Integer32):
    """Custom type svrFanStatus based on Integer32"""
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
        *(("backup", 3),
          ("failed", 4),
          ("running", 2),
          ("unknown", 1))
    )


_SvrFanStatus_Type.__name__ = "Integer32"
_SvrFanStatus_Object = MibTableColumn
svrFanStatus = _SvrFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 8, 2, 2, 1, 3),
    _SvrFanStatus_Type()
)
svrFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrFanStatus.setStatus("mandatory")
_SvrFanBackup_Type = Integer32
_SvrFanBackup_Object = MibTableColumn
svrFanBackup = _SvrFanBackup_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 8, 2, 2, 1, 4),
    _SvrFanBackup_Type()
)
svrFanBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrFanBackup.setStatus("mandatory")
_SvrFanFruIndex_Type = Integer32
_SvrFanFruIndex_Object = MibTableColumn
svrFanFruIndex = _SvrFanFruIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 8, 2, 2, 1, 5),
    _SvrFanFruIndex_Type()
)
svrFanFruIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrFanFruIndex.setStatus("mandatory")
_SvrPowerSystem_ObjectIdentity = ObjectIdentity
svrPowerSystem = _SvrPowerSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 8, 3)
)
_SvrPowerRedunEnable_Type = Boolean
_SvrPowerRedunEnable_Object = MibScalar
svrPowerRedunEnable = _SvrPowerRedunEnable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 8, 3, 1),
    _SvrPowerRedunEnable_Type()
)
svrPowerRedunEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrPowerRedunEnable.setStatus("mandatory")
_SvrPowerSensorCount_Type = Integer32
_SvrPowerSensorCount_Object = MibScalar
svrPowerSensorCount = _SvrPowerSensorCount_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 8, 3, 2),
    _SvrPowerSensorCount_Type()
)
svrPowerSensorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrPowerSensorCount.setStatus("mandatory")
_SvrPowerSupplyCount_Type = Integer32
_SvrPowerSupplyCount_Object = MibScalar
svrPowerSupplyCount = _SvrPowerSupplyCount_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 8, 3, 3),
    _SvrPowerSupplyCount_Type()
)
svrPowerSupplyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrPowerSupplyCount.setStatus("mandatory")
_SvrPowerSensorTable_Object = MibTable
svrPowerSensorTable = _SvrPowerSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 8, 3, 4)
)
if mibBuilder.loadTexts:
    svrPowerSensorTable.setStatus("mandatory")
_SvrPowerSensorEntry_Object = MibTableRow
svrPowerSensorEntry = _SvrPowerSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 8, 3, 4, 1)
)
svrPowerSensorEntry.setIndexNames(
    (0, "SVRSYS-MIB", "svrPowerSensorIndex"),
)
if mibBuilder.loadTexts:
    svrPowerSensorEntry.setStatus("mandatory")
_SvrPowerSensorIndex_Type = Integer32
_SvrPowerSensorIndex_Object = MibTableColumn
svrPowerSensorIndex = _SvrPowerSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 8, 3, 4, 1, 1),
    _SvrPowerSensorIndex_Type()
)
svrPowerSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrPowerSensorIndex.setStatus("mandatory")
_SvrPowerSensorLocation_Type = DisplayString
_SvrPowerSensorLocation_Object = MibTableColumn
svrPowerSensorLocation = _SvrPowerSensorLocation_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 8, 3, 4, 1, 2),
    _SvrPowerSensorLocation_Type()
)
svrPowerSensorLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svrPowerSensorLocation.setStatus("mandatory")
_SvrPowerSensorRating_Type = Integer32
_SvrPowerSensorRating_Object = MibTableColumn
svrPowerSensorRating = _SvrPowerSensorRating_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 8, 3, 4, 1, 3),
    _SvrPowerSensorRating_Type()
)
svrPowerSensorRating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrPowerSensorRating.setStatus("mandatory")
_SvrPowerSensorReading_Type = Integer32
_SvrPowerSensorReading_Object = MibTableColumn
svrPowerSensorReading = _SvrPowerSensorReading_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 8, 3, 4, 1, 4),
    _SvrPowerSensorReading_Type()
)
svrPowerSensorReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrPowerSensorReading.setStatus("mandatory")
_SvrPowerSensorReadingUnits_Type = PowerUnits
_SvrPowerSensorReadingUnits_Object = MibTableColumn
svrPowerSensorReadingUnits = _SvrPowerSensorReadingUnits_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 8, 3, 4, 1, 5),
    _SvrPowerSensorReadingUnits_Type()
)
svrPowerSensorReadingUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrPowerSensorReadingUnits.setStatus("mandatory")
_SvrPowerSensorNeedPwrThresh_Type = Integer32
_SvrPowerSensorNeedPwrThresh_Object = MibTableColumn
svrPowerSensorNeedPwrThresh = _SvrPowerSensorNeedPwrThresh_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 8, 3, 4, 1, 6),
    _SvrPowerSensorNeedPwrThresh_Type()
)
svrPowerSensorNeedPwrThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrPowerSensorNeedPwrThresh.setStatus("mandatory")
_SvrPowerSensorLowThresh_Type = Integer32
_SvrPowerSensorLowThresh_Object = MibTableColumn
svrPowerSensorLowThresh = _SvrPowerSensorLowThresh_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 8, 3, 4, 1, 7),
    _SvrPowerSensorLowThresh_Type()
)
svrPowerSensorLowThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrPowerSensorLowThresh.setStatus("mandatory")
_SvrPowerSensorHighThresh_Type = Integer32
_SvrPowerSensorHighThresh_Object = MibTableColumn
svrPowerSensorHighThresh = _SvrPowerSensorHighThresh_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 8, 3, 4, 1, 8),
    _SvrPowerSensorHighThresh_Type()
)
svrPowerSensorHighThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrPowerSensorHighThresh.setStatus("mandatory")
_SvrPowerSensorShutNowThresh_Type = Integer32
_SvrPowerSensorShutNowThresh_Object = MibTableColumn
svrPowerSensorShutNowThresh = _SvrPowerSensorShutNowThresh_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 8, 3, 4, 1, 9),
    _SvrPowerSensorShutNowThresh_Type()
)
svrPowerSensorShutNowThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrPowerSensorShutNowThresh.setStatus("mandatory")
_SvrPowerSensorThreshUnits_Type = PowerUnits
_SvrPowerSensorThreshUnits_Object = MibTableColumn
svrPowerSensorThreshUnits = _SvrPowerSensorThreshUnits_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 8, 3, 4, 1, 10),
    _SvrPowerSensorThreshUnits_Type()
)
svrPowerSensorThreshUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrPowerSensorThreshUnits.setStatus("mandatory")


class _SvrPowerSensorStatus_Type(Integer32):
    """Custom type svrPowerSensorStatus based on Integer32"""
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
        *(("high", 7),
          ("highWarning", 6),
          ("low", 3),
          ("lowWarning", 4),
          ("other", 2),
          ("statusOk", 5),
          ("unknown", 1))
    )


_SvrPowerSensorStatus_Type.__name__ = "Integer32"
_SvrPowerSensorStatus_Object = MibTableColumn
svrPowerSensorStatus = _SvrPowerSensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 8, 3, 4, 1, 11),
    _SvrPowerSensorStatus_Type()
)
svrPowerSensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrPowerSensorStatus.setStatus("mandatory")
_SvrPowerSensorFruIndex_Type = Integer32
_SvrPowerSensorFruIndex_Object = MibTableColumn
svrPowerSensorFruIndex = _SvrPowerSensorFruIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 8, 3, 4, 1, 12),
    _SvrPowerSensorFruIndex_Type()
)
svrPowerSensorFruIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrPowerSensorFruIndex.setStatus("mandatory")
_SvrPowerSupplyTable_Object = MibTable
svrPowerSupplyTable = _SvrPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 8, 3, 5)
)
if mibBuilder.loadTexts:
    svrPowerSupplyTable.setStatus("mandatory")
_SvrPowerSupplyEntry_Object = MibTableRow
svrPowerSupplyEntry = _SvrPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 8, 3, 5, 1)
)
svrPowerSupplyEntry.setIndexNames(
    (0, "SVRSYS-MIB", "svrPowerSupplyIndex"),
)
if mibBuilder.loadTexts:
    svrPowerSupplyEntry.setStatus("mandatory")
_SvrPowerSupplyIndex_Type = Integer32
_SvrPowerSupplyIndex_Object = MibTableColumn
svrPowerSupplyIndex = _SvrPowerSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 8, 3, 5, 1, 1),
    _SvrPowerSupplyIndex_Type()
)
svrPowerSupplyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrPowerSupplyIndex.setStatus("mandatory")


class _SvrPowerSupplyStatus_Type(Integer32):
    """Custom type svrPowerSupplyStatus based on Integer32"""
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
        *(("backup", 3),
          ("failed", 5),
          ("running", 2),
          ("unknown", 1),
          ("warning", 4))
    )


_SvrPowerSupplyStatus_Type.__name__ = "Integer32"
_SvrPowerSupplyStatus_Object = MibTableColumn
svrPowerSupplyStatus = _SvrPowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 8, 3, 5, 1, 2),
    _SvrPowerSupplyStatus_Type()
)
svrPowerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrPowerSupplyStatus.setStatus("mandatory")
_SvrPowerSupplyFruIndex_Type = Integer32
_SvrPowerSupplyFruIndex_Object = MibTableColumn
svrPowerSupplyFruIndex = _SvrPowerSupplyFruIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 22, 1, 8, 3, 5, 1, 3),
    _SvrPowerSupplyFruIndex_Type()
)
svrPowerSupplyFruIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svrPowerSupplyFruIndex.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SVRSYS-MIB",
    **{"KBytes": KBytes,
       "BusTypes": BusTypes,
       "SystemStatus": SystemStatus,
       "MemoryAddress": MemoryAddress,
       "ThermUnits": ThermUnits,
       "PowerUnits": PowerUnits,
       "Boolean": Boolean,
       "dec": dec,
       "ema": ema,
       "mib-extensions-1": mib_extensions_1,
       "svrSystem": svrSystem,
       "svrBaseSystem": svrBaseSystem,
       "svrSysMibInfo": svrSysMibInfo,
       "svrSysMibMajorRev": svrSysMibMajorRev,
       "svrSysMibMinorRev": svrSysMibMinorRev,
       "svrBaseSysDescr": svrBaseSysDescr,
       "svrSystemFamily": svrSystemFamily,
       "svrSystemModel": svrSystemModel,
       "svrSystemDescr": svrSystemDescr,
       "svrSystemBoardFruIndex": svrSystemBoardFruIndex,
       "svrSystemOCPDisplay": svrSystemOCPDisplay,
       "svrSystemBootedOS": svrSystemBootedOS,
       "svrSystemBootedOSVersion": svrSystemBootedOSVersion,
       "svrSystemShutdownReason": svrSystemShutdownReason,
       "svrSystemRemoteMgrNum": svrSystemRemoteMgrNum,
       "svrFirmwareTable": svrFirmwareTable,
       "svrFirmwareEntry": svrFirmwareEntry,
       "svrFirmwareIndex": svrFirmwareIndex,
       "svrFirmwareDescr": svrFirmwareDescr,
       "svrFirmwareRev": svrFirmwareRev,
       "svrFwSymbolTable": svrFwSymbolTable,
       "svrFwSymbolEntry": svrFwSymbolEntry,
       "svrFwSymbolName": svrFwSymbolName,
       "svrFwSymbolValue": svrFwSymbolValue,
       "svrProcessors": svrProcessors,
       "svrCpuPollInterval": svrCpuPollInterval,
       "svrCpuMinPollInterval": svrCpuMinPollInterval,
       "svrCpuTable": svrCpuTable,
       "svrCpuEntry": svrCpuEntry,
       "svrCpuIndex": svrCpuIndex,
       "svrCpuType": svrCpuType,
       "svrCpuManufacturer": svrCpuManufacturer,
       "svrCpuRevision": svrCpuRevision,
       "svrCpuFruIndex": svrCpuFruIndex,
       "svrCpuSpeed": svrCpuSpeed,
       "svrCpuUtilCurrent": svrCpuUtilCurrent,
       "svrCpuAvgNextIndex": svrCpuAvgNextIndex,
       "svrCpuHrIndex": svrCpuHrIndex,
       "svrCpuAvgTable": svrCpuAvgTable,
       "svrCpuAvgEntry": svrCpuAvgEntry,
       "svrCpuAvgIndex": svrCpuAvgIndex,
       "svrCpuAvgInterval": svrCpuAvgInterval,
       "svrCpuAvgStatus": svrCpuAvgStatus,
       "svrCpuAvgPersist": svrCpuAvgPersist,
       "svrCpuAvgValue": svrCpuAvgValue,
       "svrCpuCacheTable": svrCpuCacheTable,
       "svrCpuCacheEntry": svrCpuCacheEntry,
       "svrCpuCacheIndex": svrCpuCacheIndex,
       "svrCpuCacheLevel": svrCpuCacheLevel,
       "svrCpuCacheType": svrCpuCacheType,
       "svrCpuCacheSize": svrCpuCacheSize,
       "svrCpuCacheSpeed": svrCpuCacheSpeed,
       "svrCpuCacheStatus": svrCpuCacheStatus,
       "svrMemory": svrMemory,
       "svrPhysicalMemorySize": svrPhysicalMemorySize,
       "svrPhysicalMemoryFree": svrPhysicalMemoryFree,
       "svrPagingMemorySize": svrPagingMemorySize,
       "svrPagingMemoryFree": svrPagingMemoryFree,
       "svrMemComponentTable": svrMemComponentTable,
       "svrMemComponentEntry": svrMemComponentEntry,
       "svrMemIndex": svrMemIndex,
       "svrMemType": svrMemType,
       "svrMemSize": svrMemSize,
       "svrMemStartAddress": svrMemStartAddress,
       "svrMemPhysLocation": svrMemPhysLocation,
       "svrMemEdcType": svrMemEdcType,
       "svrMemElementSlots": svrMemElementSlots,
       "svrMemElementSlotsUsed": svrMemElementSlotsUsed,
       "svrMemInterleafFactor": svrMemInterleafFactor,
       "svrMemInterleafElement": svrMemInterleafElement,
       "svrMemFruIndex": svrMemFruIndex,
       "svrMemElementTable": svrMemElementTable,
       "svrMemElementEntry": svrMemElementEntry,
       "svrMemElementIndex": svrMemElementIndex,
       "svrMemElementType": svrMemElementType,
       "svrMemElementSlotNo": svrMemElementSlotNo,
       "svrMemElementWidth": svrMemElementWidth,
       "svrMemElementDepth": svrMemElementDepth,
       "svrMemElementSpeed": svrMemElementSpeed,
       "svrMemElementStatus": svrMemElementStatus,
       "svrBuses": svrBuses,
       "svrBusCount": svrBusCount,
       "svrBusTable": svrBusTable,
       "svrBusEntry": svrBusEntry,
       "svrBusIndex": svrBusIndex,
       "svrBusType": svrBusType,
       "svrBusNumber": svrBusNumber,
       "svrBusSlotCount": svrBusSlotCount,
       "svrLogicalSlotTable": svrLogicalSlotTable,
       "svrLogicalSlotEntry": svrLogicalSlotEntry,
       "svrLogicalSlotNumber": svrLogicalSlotNumber,
       "svrLogicalSlotDescr": svrLogicalSlotDescr,
       "svrLogicalSlotDeviceID": svrLogicalSlotDeviceID,
       "svrLogicalSlotVendor": svrLogicalSlotVendor,
       "svrLogicalSlotRevision": svrLogicalSlotRevision,
       "svrLogicalSlotFnCount": svrLogicalSlotFnCount,
       "svrSlotFunctionTable": svrSlotFunctionTable,
       "svrSlotFunctionEntry": svrSlotFunctionEntry,
       "svrSlotFnIndex": svrSlotFnIndex,
       "svrSlotFnDevType": svrSlotFnDevType,
       "svrSlotFnRevision": svrSlotFnRevision,
       "svrDevices": svrDevices,
       "svrDeviceCount": svrDeviceCount,
       "svrSerialPortCount": svrSerialPortCount,
       "svrParallelPortCount": svrParallelPortCount,
       "svrConsoleKeyboard": svrConsoleKeyboard,
       "svrKeybdHrIndex": svrKeybdHrIndex,
       "svrKeybdDescr": svrKeybdDescr,
       "svrConsoleDisplay": svrConsoleDisplay,
       "svrVideoHrIndex": svrVideoHrIndex,
       "svrVideoDescr": svrVideoDescr,
       "svrVideoXRes": svrVideoXRes,
       "svrVideoYRes": svrVideoYRes,
       "svrVideoNumColor": svrVideoNumColor,
       "svrVideoRefreshRate": svrVideoRefreshRate,
       "svrVideoScanMode": svrVideoScanMode,
       "svrVideoMemory": svrVideoMemory,
       "svrConsolePointDevice": svrConsolePointDevice,
       "svrPointingHrIndex": svrPointingHrIndex,
       "svrPointingDescr": svrPointingDescr,
       "svrNumButtons": svrNumButtons,
       "svrSerialPortTable": svrSerialPortTable,
       "svrSerialPortEntry": svrSerialPortEntry,
       "svrSerialIndex": svrSerialIndex,
       "svrSerialPortDescr": svrSerialPortDescr,
       "svrSerialHrIndex": svrSerialHrIndex,
       "svrParallelPortTable": svrParallelPortTable,
       "svrParallelPortEntry": svrParallelPortEntry,
       "svrParallelIndex": svrParallelIndex,
       "svrParallelPortDescr": svrParallelPortDescr,
       "svrParallelHrIndex": svrParallelHrIndex,
       "svrDeviceTable": svrDeviceTable,
       "svrDeviceEntry": svrDeviceEntry,
       "svrDevIndex": svrDevIndex,
       "svrDevDescr": svrDevDescr,
       "svrDevBusInterfaceType": svrDevBusInterfaceType,
       "svrDevBusNumber": svrDevBusNumber,
       "svrDevSlotNumber": svrDevSlotNumber,
       "svrDevFruIndex": svrDevFruIndex,
       "svrDevCPUAffinity": svrDevCPUAffinity,
       "svrDevHrIndex": svrDevHrIndex,
       "svrDevInterruptTable": svrDevInterruptTable,
       "svrDevIntEntry": svrDevIntEntry,
       "svrDevIntIndex": svrDevIntIndex,
       "svrDevIntLevel": svrDevIntLevel,
       "svrDevIntVector": svrDevIntVector,
       "svrDevIntShared": svrDevIntShared,
       "svrDevIntTrigger": svrDevIntTrigger,
       "svrDevMemTable": svrDevMemTable,
       "svrDevMemEntry": svrDevMemEntry,
       "svrDevMemIndex": svrDevMemIndex,
       "svrDevMemAddress": svrDevMemAddress,
       "svrDevMemLength": svrDevMemLength,
       "svrDevMemMapping": svrDevMemMapping,
       "svrDevDmaTable": svrDevDmaTable,
       "svrDevDmaEntry": svrDevDmaEntry,
       "svrDevDmaIndex": svrDevDmaIndex,
       "svrDevDmaChannel": svrDevDmaChannel,
       "svrPhysicalConfiguration": svrPhysicalConfiguration,
       "svrChassisType": svrChassisType,
       "svrChassisFruIndex": svrChassisFruIndex,
       "svrFruTable": svrFruTable,
       "svrFruEntry": svrFruEntry,
       "svrFruIndex": svrFruIndex,
       "svrFruType": svrFruType,
       "svrFruDescr": svrFruDescr,
       "svrFruVendor": svrFruVendor,
       "svrFruPartNumber": svrFruPartNumber,
       "svrFruRevision": svrFruRevision,
       "svrFruFirmwareRevision": svrFruFirmwareRevision,
       "svrFruSerialNumber": svrFruSerialNumber,
       "svrFruAssetNo": svrFruAssetNo,
       "svrFruClass": svrFruClass,
       "svrEnvironment": svrEnvironment,
       "svrThermalSystem": svrThermalSystem,
       "svrThermalSensorCount": svrThermalSensorCount,
       "svrThermalSensorTable": svrThermalSensorTable,
       "svrThermalSensorEntry": svrThermalSensorEntry,
       "svrThSensorIndex": svrThSensorIndex,
       "svrThSensorLocation": svrThSensorLocation,
       "svrThSensorReading": svrThSensorReading,
       "svrThSensorReadingUnits": svrThSensorReadingUnits,
       "svrThSensorLowThresh": svrThSensorLowThresh,
       "svrThSensorHighThresh": svrThSensorHighThresh,
       "svrThSensorShutSoonThresh": svrThSensorShutSoonThresh,
       "svrThSensorShutNowThresh": svrThSensorShutNowThresh,
       "svrThSensorThreshUnits": svrThSensorThreshUnits,
       "svrThSensorStatus": svrThSensorStatus,
       "svrThSensorFruIndex": svrThSensorFruIndex,
       "svrCoolingSystem": svrCoolingSystem,
       "svrFanCount": svrFanCount,
       "svrFanTable": svrFanTable,
       "svrFanEntry": svrFanEntry,
       "svrFanIndex": svrFanIndex,
       "svrFanLocation": svrFanLocation,
       "svrFanStatus": svrFanStatus,
       "svrFanBackup": svrFanBackup,
       "svrFanFruIndex": svrFanFruIndex,
       "svrPowerSystem": svrPowerSystem,
       "svrPowerRedunEnable": svrPowerRedunEnable,
       "svrPowerSensorCount": svrPowerSensorCount,
       "svrPowerSupplyCount": svrPowerSupplyCount,
       "svrPowerSensorTable": svrPowerSensorTable,
       "svrPowerSensorEntry": svrPowerSensorEntry,
       "svrPowerSensorIndex": svrPowerSensorIndex,
       "svrPowerSensorLocation": svrPowerSensorLocation,
       "svrPowerSensorRating": svrPowerSensorRating,
       "svrPowerSensorReading": svrPowerSensorReading,
       "svrPowerSensorReadingUnits": svrPowerSensorReadingUnits,
       "svrPowerSensorNeedPwrThresh": svrPowerSensorNeedPwrThresh,
       "svrPowerSensorLowThresh": svrPowerSensorLowThresh,
       "svrPowerSensorHighThresh": svrPowerSensorHighThresh,
       "svrPowerSensorShutNowThresh": svrPowerSensorShutNowThresh,
       "svrPowerSensorThreshUnits": svrPowerSensorThreshUnits,
       "svrPowerSensorStatus": svrPowerSensorStatus,
       "svrPowerSensorFruIndex": svrPowerSensorFruIndex,
       "svrPowerSupplyTable": svrPowerSupplyTable,
       "svrPowerSupplyEntry": svrPowerSupplyEntry,
       "svrPowerSupplyIndex": svrPowerSupplyIndex,
       "svrPowerSupplyStatus": svrPowerSupplyStatus,
       "svrPowerSupplyFruIndex": svrPowerSupplyFruIndex}
)
