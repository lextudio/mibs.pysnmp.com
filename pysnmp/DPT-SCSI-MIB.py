# SNMP MIB module (DPT-SCSI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DPT-SCSI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:33:25 2024
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



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""




class DptSignature(DisplayString):
    """Custom type DptSignature based on DisplayString"""




class HostBusType(Integer32):
    """Custom type HostBusType based on Integer32"""
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
        *(("eisa", 3),
          ("invalid", 1),
          ("isa", 2),
          ("pci-32", 4),
          ("pci-64", 5))
    )





class ScsiBusType(Integer32):
    """Custom type ScsiBusType based on Integer32"""
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
        *(("differential", 3),
          ("fibreChannel", 5),
          ("invalid", 1),
          ("lvd", 4),
          ("singleEnded", 2))
    )





class IrqType(Integer32):
    """Custom type IrqType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("edge", 3),
          ("invalid", 1),
          ("level", 2))
    )





class DrqNumber(Integer32):
    """Custom type DrqNumber based on Integer32"""
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
        *(("five", 4),
          ("invalid", 1),
          ("notApplicable", 2),
          ("seven", 6),
          ("six", 5),
          ("zero", 3))
    )





class MemoryBankType(Integer32):
    """Custom type MemoryBankType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("dm4050DPT-ECC-EDO-SO-DIMM", 9),
          ("dm4070DPT-ECC-SD-DIMM", 10),
          ("empty", 3),
          ("invalid", 1),
          ("notApplicable", 2),
          ("sm4000DPT-ECC-SIMM", 6),
          ("sm4041DPT-ECC-DIMM", 7),
          ("sm4050DPT-ECC-EDO-SIMM", 8),
          ("standard-DIMM", 5),
          ("standard-SIMM", 4))
    )





class MemoryBankSize(Integer32):
    """Custom type MemoryBankSize based on Integer32"""
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
        *(("empty", 3),
          ("fivehundredtwelveMB", 11),
          ("fourMB", 5),
          ("hundredtwentyeightMB", 9),
          ("invalid", 1),
          ("notApplicable", 2),
          ("oneMB", 4),
          ("sixteenMB", 6),
          ("sixtyfourMB", 8),
          ("thirtytwoMB", 7),
          ("thousandtwentyfourMB", 12),
          ("twohundredfiftysixMB", 10))
    )





class CachingModule(Integer32):
    """Custom type CachingModule based on Integer32"""
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
        *(("cm4000", 4),
          ("embedded", 7),
          ("invalid", 1),
          ("none", 3),
          ("notApplicable", 2),
          ("ra4050", 8),
          ("ra4060", 9),
          ("rc4040", 5),
          ("rc4041", 6))
    )





class RaidModule(Integer32):
    """Custom type RaidModule based on Integer32"""
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
        *(("dm4000", 4),
          ("embedded", 7),
          ("invalid", 1),
          ("none", 3),
          ("notApplicable", 2),
          ("ra4050", 8),
          ("ra4060", 9),
          ("rc4040", 5),
          ("rc4041", 6))
    )





class BatteryBackupModule(Integer32):
    """Custom type BatteryBackupModule based on Integer32"""
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
        *(("bb4050", 5),
          ("bb4060", 6),
          ("embedded", 4),
          ("invalid", 1),
          ("none", 3),
          ("notApplicable", 2))
    )





class RaidType(Integer32):
    """Custom type RaidType based on Integer32"""
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
        *(("hotSpare", 7),
          ("invalid", 1),
          ("notAssigned", 2),
          ("raid-0", 3),
          ("raid-1", 4),
          ("raid-5", 5),
          ("redirected", 6))
    )





class SoftwareType(Integer32):
    """Custom type SoftwareType based on Integer32"""
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
        *(("application", 4),
          ("driver", 2),
          ("firmware", 1),
          ("operatingSystem", 3))
    )





class BusWidth(Integer32):
    """Custom type BusWidth based on Integer32"""
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
        *(("invalid", 1),
          ("narrow", 3),
          ("notApplicable", 6),
          ("serial", 2),
          ("wide", 4),
          ("wide32", 5))
    )





class BusTerminationType(Integer32):
    """Custom type BusTerminationType based on Integer32"""
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
        *(("auto", 5),
          ("highOnly", 4),
          ("invalid", 1),
          ("off", 3),
          ("on", 2))
    )





class ScsiVersion(Integer32):
    """Custom type ScsiVersion based on Integer32"""
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
        *(("invalid", 1),
          ("scsi-I", 2),
          ("scsi-II", 3),
          ("scsi-III", 4))
    )





class DeviceType(Integer32):
    """Custom type DeviceType based on Integer32"""
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
              97,
              98,
              99)
        )
    )
    namedValues = NamedValues(
        *(("cdRom", 6),
          ("commDev", 10),
          ("disk", 1),
          ("graphicsType10", 11),
          ("graphicsType11", 12),
          ("host", 98),
          ("jukebox", 9),
          ("optical", 8),
          ("printer", 3),
          ("processor", 4),
          ("saf-te", 97),
          ("scanner", 7),
          ("scc", 13),
          ("ses", 14),
          ("tape", 2),
          ("unknown", 99),
          ("writeOnce", 5))
    )





class DeviceStatus(Integer32):
    """Custom type DeviceStatus based on Integer32"""
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
        *(("abortActivity", 14),
          ("building", 11),
          ("degraded", 10),
          ("failed", 4),
          ("formatCertifying", 7),
          ("formatting", 6),
          ("invalid", 1),
          ("missing", 8),
          ("notCreated", 9),
          ("optimal", 2),
          ("rebuilding", 12),
          ("verifyFixing", 13),
          ("verifying", 3),
          ("warning", 5))
    )





class DeviceWriteMode(Integer32):
    """Custom type DeviceWriteMode based on Integer32"""
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
        *(("invalid", 1),
          ("noCache", 5),
          ("notApplicable", 2),
          ("writeBack", 3),
          ("writeThrough", 4))
    )





class YesNoStatus(Integer32):
    """Custom type YesNoStatus based on Integer32"""
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
        *(("invalid", 1),
          ("no", 5),
          ("notApplicable", 2),
          ("notSupported", 3),
          ("yes", 4))
    )





class LowHighStatus(Integer32):
    """Custom type LowHighStatus based on Integer32"""
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
        *(("high", 6),
          ("invalid", 1),
          ("low", 4),
          ("normal", 5),
          ("notApplicable", 2),
          ("notSupported", 3),
          ("veryHigh", 7))
    )





class BatteryStatus(Integer32):
    """Custom type BatteryStatus based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("bad", 7),
          ("discharge", 6),
          ("fastCharge", 5),
          ("full", 8),
          ("initCharge", 9),
          ("initDischarge", 10),
          ("initRecharge", 11),
          ("invalid", 1),
          ("maintenanceCharge", 13),
          ("maintenanceDischarge", 12),
          ("none", 3),
          ("notApplicable", 2),
          ("trickleCharge", 4))
    )





class HbaGenStatus(Integer32):
    """Custom type HbaGenStatus based on Integer32"""
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
        *(("error", 5),
          ("fail", 4),
          ("invalid", 1),
          ("notSupported", 2),
          ("ok", 3))
    )





class CommandType(Integer32):
    """Custom type CommandType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hostCmd", 1),
          ("scsiCmd", 2))
    )





class RowStatus(Integer32):
    """Custom type RowStatus based on Integer32"""
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
        *(("active", 2),
          ("createAndGo", 5),
          ("createAndWait", 6),
          ("destroy", 7),
          ("invalid", 1),
          ("notInService", 3),
          ("notReady", 4))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dpt_ObjectIdentity = ObjectIdentity
dpt = _Dpt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1597)
)
_DptScsi_ObjectIdentity = ObjectIdentity
dptScsi = _DptScsi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1597, 1)
)
_DptScsiSys_ObjectIdentity = ObjectIdentity
dptScsiSys = _DptScsiSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1597, 1, 1)
)
_DptScsiSysRevLevel_Type = DptSignature
_DptScsiSysRevLevel_Object = MibScalar
dptScsiSysRevLevel = _DptScsiSysRevLevel_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 1, 1),
    _DptScsiSysRevLevel_Type()
)
dptScsiSysRevLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiSysRevLevel.setStatus("mandatory")
_DptScsiSysEngineSignature_Type = DptSignature
_DptScsiSysEngineSignature_Object = MibScalar
dptScsiSysEngineSignature = _DptScsiSysEngineSignature_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 1, 2),
    _DptScsiSysEngineSignature_Type()
)
dptScsiSysEngineSignature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiSysEngineSignature.setStatus("mandatory")
_DptScsiSysDriverSignature_Type = DptSignature
_DptScsiSysDriverSignature_Object = MibScalar
dptScsiSysDriverSignature = _DptScsiSysDriverSignature_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 1, 3),
    _DptScsiSysDriverSignature_Type()
)
dptScsiSysDriverSignature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiSysDriverSignature.setStatus("mandatory")
_DptScsiSysEventLoggerSignature_Type = DptSignature
_DptScsiSysEventLoggerSignature_Object = MibScalar
dptScsiSysEventLoggerSignature = _DptScsiSysEventLoggerSignature_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 1, 4),
    _DptScsiSysEventLoggerSignature_Type()
)
dptScsiSysEventLoggerSignature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiSysEventLoggerSignature.setStatus("mandatory")


class _DptScsiSysMibRevMajor_Type(Integer32):
    """Custom type dptScsiSysMibRevMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DptScsiSysMibRevMajor_Type.__name__ = "Integer32"
_DptScsiSysMibRevMajor_Object = MibScalar
dptScsiSysMibRevMajor = _DptScsiSysMibRevMajor_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 1, 5),
    _DptScsiSysMibRevMajor_Type()
)
dptScsiSysMibRevMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiSysMibRevMajor.setStatus("mandatory")


class _DptScsiSysMibRevMinor_Type(Integer32):
    """Custom type dptScsiSysMibRevMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DptScsiSysMibRevMinor_Type.__name__ = "Integer32"
_DptScsiSysMibRevMinor_Object = MibScalar
dptScsiSysMibRevMinor = _DptScsiSysMibRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 1, 6),
    _DptScsiSysMibRevMinor_Type()
)
dptScsiSysMibRevMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiSysMibRevMinor.setStatus("mandatory")
_DptScsiHba_ObjectIdentity = ObjectIdentity
dptScsiHba = _DptScsiHba_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1597, 1, 2)
)
_DptScsiHbaTable_Object = MibTable
dptScsiHbaTable = _DptScsiHbaTable_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dptScsiHbaTable.setStatus("mandatory")
_DptScsiHbaEntry_Object = MibTableRow
dptScsiHbaEntry = _DptScsiHbaEntry_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 2, 1, 1)
)
dptScsiHbaEntry.setIndexNames(
    (0, "DPT-SCSI-MIB", "dptScsiHbaNumber"),
)
if mibBuilder.loadTexts:
    dptScsiHbaEntry.setStatus("mandatory")


class _DptScsiHbaNumber_Type(Integer32):
    """Custom type dptScsiHbaNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DptScsiHbaNumber_Type.__name__ = "Integer32"
_DptScsiHbaNumber_Object = MibTableColumn
dptScsiHbaNumber = _DptScsiHbaNumber_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 2, 1, 1, 1),
    _DptScsiHbaNumber_Type()
)
dptScsiHbaNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiHbaNumber.setStatus("mandatory")


class _DptScsiHbaVendor_Type(DisplayString):
    """Custom type dptScsiHbaVendor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_DptScsiHbaVendor_Type.__name__ = "DisplayString"
_DptScsiHbaVendor_Object = MibTableColumn
dptScsiHbaVendor = _DptScsiHbaVendor_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 2, 1, 1, 2),
    _DptScsiHbaVendor_Type()
)
dptScsiHbaVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiHbaVendor.setStatus("mandatory")


class _DptScsiHbaModel_Type(DisplayString):
    """Custom type dptScsiHbaModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_DptScsiHbaModel_Type.__name__ = "DisplayString"
_DptScsiHbaModel_Object = MibTableColumn
dptScsiHbaModel = _DptScsiHbaModel_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 2, 1, 1, 3),
    _DptScsiHbaModel_Type()
)
dptScsiHbaModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiHbaModel.setStatus("mandatory")


class _DptScsiHbaFirmware_Type(DisplayString):
    """Custom type dptScsiHbaFirmware based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_DptScsiHbaFirmware_Type.__name__ = "DisplayString"
_DptScsiHbaFirmware_Object = MibTableColumn
dptScsiHbaFirmware = _DptScsiHbaFirmware_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 2, 1, 1, 4),
    _DptScsiHbaFirmware_Type()
)
dptScsiHbaFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiHbaFirmware.setStatus("mandatory")


class _DptScsiHbaSerialNumber_Type(DisplayString):
    """Custom type dptScsiHbaSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DptScsiHbaSerialNumber_Type.__name__ = "DisplayString"
_DptScsiHbaSerialNumber_Object = MibTableColumn
dptScsiHbaSerialNumber = _DptScsiHbaSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 2, 1, 1, 5),
    _DptScsiHbaSerialNumber_Type()
)
dptScsiHbaSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiHbaSerialNumber.setStatus("mandatory")


class _DptScsiHbaAddress_Type(Integer32):
    """Custom type dptScsiHbaAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DptScsiHbaAddress_Type.__name__ = "Integer32"
_DptScsiHbaAddress_Object = MibTableColumn
dptScsiHbaAddress = _DptScsiHbaAddress_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 2, 1, 1, 6),
    _DptScsiHbaAddress_Type()
)
dptScsiHbaAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiHbaAddress.setStatus("mandatory")
_DptScsiHbaHostBusType_Type = HostBusType
_DptScsiHbaHostBusType_Object = MibTableColumn
dptScsiHbaHostBusType = _DptScsiHbaHostBusType_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 2, 1, 1, 7),
    _DptScsiHbaHostBusType_Type()
)
dptScsiHbaHostBusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiHbaHostBusType.setStatus("mandatory")
_DptScsiHbaHostBusMaxTransferRate_Type = Integer32
_DptScsiHbaHostBusMaxTransferRate_Object = MibTableColumn
dptScsiHbaHostBusMaxTransferRate = _DptScsiHbaHostBusMaxTransferRate_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 2, 1, 1, 8),
    _DptScsiHbaHostBusMaxTransferRate_Type()
)
dptScsiHbaHostBusMaxTransferRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiHbaHostBusMaxTransferRate.setStatus("mandatory")


class _DptScsiHbaIrq_Type(Integer32):
    """Custom type dptScsiHbaIrq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DptScsiHbaIrq_Type.__name__ = "Integer32"
_DptScsiHbaIrq_Object = MibTableColumn
dptScsiHbaIrq = _DptScsiHbaIrq_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 2, 1, 1, 9),
    _DptScsiHbaIrq_Type()
)
dptScsiHbaIrq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiHbaIrq.setStatus("mandatory")
_DptScsiHbaIrqType_Type = IrqType
_DptScsiHbaIrqType_Object = MibTableColumn
dptScsiHbaIrqType = _DptScsiHbaIrqType_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 2, 1, 1, 10),
    _DptScsiHbaIrqType_Type()
)
dptScsiHbaIrqType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiHbaIrqType.setStatus("mandatory")
_DptScsiHbaDrq_Type = DrqNumber
_DptScsiHbaDrq_Object = MibTableColumn
dptScsiHbaDrq = _DptScsiHbaDrq_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 2, 1, 1, 11),
    _DptScsiHbaDrq_Type()
)
dptScsiHbaDrq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiHbaDrq.setStatus("deprecated")
_DptScsiHbaRaidModule_Type = RaidModule
_DptScsiHbaRaidModule_Object = MibTableColumn
dptScsiHbaRaidModule = _DptScsiHbaRaidModule_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 2, 1, 1, 12),
    _DptScsiHbaRaidModule_Type()
)
dptScsiHbaRaidModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiHbaRaidModule.setStatus("mandatory")
_DptScsiHbaCachingModule_Type = CachingModule
_DptScsiHbaCachingModule_Object = MibTableColumn
dptScsiHbaCachingModule = _DptScsiHbaCachingModule_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 2, 1, 1, 13),
    _DptScsiHbaCachingModule_Type()
)
dptScsiHbaCachingModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiHbaCachingModule.setStatus("deprecated")
_DptScsiHbaAudibleAlarmOn_Type = YesNoStatus
_DptScsiHbaAudibleAlarmOn_Object = MibTableColumn
dptScsiHbaAudibleAlarmOn = _DptScsiHbaAudibleAlarmOn_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 2, 1, 1, 14),
    _DptScsiHbaAudibleAlarmOn_Type()
)
dptScsiHbaAudibleAlarmOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiHbaAudibleAlarmOn.setStatus("mandatory")
_DptScsiHbaUpTime_Type = TimeTicks
_DptScsiHbaUpTime_Object = MibTableColumn
dptScsiHbaUpTime = _DptScsiHbaUpTime_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 2, 1, 1, 15),
    _DptScsiHbaUpTime_Type()
)
dptScsiHbaUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiHbaUpTime.setStatus("mandatory")
_DptScsiHbaEccEnabled_Type = YesNoStatus
_DptScsiHbaEccEnabled_Object = MibTableColumn
dptScsiHbaEccEnabled = _DptScsiHbaEccEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 2, 1, 1, 16),
    _DptScsiHbaEccEnabled_Type()
)
dptScsiHbaEccEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiHbaEccEnabled.setStatus("mandatory")


class _DptScsiHbaBackgroundTaskPriority_Type(Integer32):
    """Custom type dptScsiHbaBackgroundTaskPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_DptScsiHbaBackgroundTaskPriority_Type.__name__ = "Integer32"
_DptScsiHbaBackgroundTaskPriority_Object = MibTableColumn
dptScsiHbaBackgroundTaskPriority = _DptScsiHbaBackgroundTaskPriority_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 2, 1, 1, 17),
    _DptScsiHbaBackgroundTaskPriority_Type()
)
dptScsiHbaBackgroundTaskPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiHbaBackgroundTaskPriority.setStatus("mandatory")
_DptScsiHbaExclusionPeriodEnabled_Type = YesNoStatus
_DptScsiHbaExclusionPeriodEnabled_Object = MibTableColumn
dptScsiHbaExclusionPeriodEnabled = _DptScsiHbaExclusionPeriodEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 2, 1, 1, 18),
    _DptScsiHbaExclusionPeriodEnabled_Type()
)
dptScsiHbaExclusionPeriodEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiHbaExclusionPeriodEnabled.setStatus("deprecated")


class _DptScsiHbaExclusionPeriodStart_Type(Integer32):
    """Custom type dptScsiHbaExclusionPeriodStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_DptScsiHbaExclusionPeriodStart_Type.__name__ = "Integer32"
_DptScsiHbaExclusionPeriodStart_Object = MibTableColumn
dptScsiHbaExclusionPeriodStart = _DptScsiHbaExclusionPeriodStart_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 2, 1, 1, 19),
    _DptScsiHbaExclusionPeriodStart_Type()
)
dptScsiHbaExclusionPeriodStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiHbaExclusionPeriodStart.setStatus("deprecated")


class _DptScsiHbaExclusionPeriodEnd_Type(Integer32):
    """Custom type dptScsiHbaExclusionPeriodEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_DptScsiHbaExclusionPeriodEnd_Type.__name__ = "Integer32"
_DptScsiHbaExclusionPeriodEnd_Object = MibTableColumn
dptScsiHbaExclusionPeriodEnd = _DptScsiHbaExclusionPeriodEnd_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 2, 1, 1, 20),
    _DptScsiHbaExclusionPeriodEnd_Type()
)
dptScsiHbaExclusionPeriodEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiHbaExclusionPeriodEnd.setStatus("deprecated")


class _DptScsiHbaMaxReadAheadPercentage_Type(Integer32):
    """Custom type dptScsiHbaMaxReadAheadPercentage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 80),
    )


_DptScsiHbaMaxReadAheadPercentage_Type.__name__ = "Integer32"
_DptScsiHbaMaxReadAheadPercentage_Object = MibTableColumn
dptScsiHbaMaxReadAheadPercentage = _DptScsiHbaMaxReadAheadPercentage_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 2, 1, 1, 21),
    _DptScsiHbaMaxReadAheadPercentage_Type()
)
dptScsiHbaMaxReadAheadPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiHbaMaxReadAheadPercentage.setStatus("deprecated")


class _DptScsiHbaMaxDirtyPagesPercentage_Type(Integer32):
    """Custom type dptScsiHbaMaxDirtyPagesPercentage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DptScsiHbaMaxDirtyPagesPercentage_Type.__name__ = "Integer32"
_DptScsiHbaMaxDirtyPagesPercentage_Object = MibTableColumn
dptScsiHbaMaxDirtyPagesPercentage = _DptScsiHbaMaxDirtyPagesPercentage_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 2, 1, 1, 22),
    _DptScsiHbaMaxDirtyPagesPercentage_Type()
)
dptScsiHbaMaxDirtyPagesPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiHbaMaxDirtyPagesPercentage.setStatus("deprecated")
_DptScsiHbaWriteBackDelay_Type = Integer32
_DptScsiHbaWriteBackDelay_Object = MibTableColumn
dptScsiHbaWriteBackDelay = _DptScsiHbaWriteBackDelay_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 2, 1, 1, 23),
    _DptScsiHbaWriteBackDelay_Type()
)
dptScsiHbaWriteBackDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiHbaWriteBackDelay.setStatus("deprecated")
_DptScsiHbaTemperature_Type = LowHighStatus
_DptScsiHbaTemperature_Object = MibTableColumn
dptScsiHbaTemperature = _DptScsiHbaTemperature_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 2, 1, 1, 24),
    _DptScsiHbaTemperature_Type()
)
dptScsiHbaTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiHbaTemperature.setStatus("mandatory")
_DptScsiHbaVoltage_Type = LowHighStatus
_DptScsiHbaVoltage_Object = MibTableColumn
dptScsiHbaVoltage = _DptScsiHbaVoltage_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 2, 1, 1, 25),
    _DptScsiHbaVoltage_Type()
)
dptScsiHbaVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiHbaVoltage.setStatus("mandatory")


class _DptScsiHbaBadMemoryAddress_Type(Integer32):
    """Custom type dptScsiHbaBadMemoryAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DptScsiHbaBadMemoryAddress_Type.__name__ = "Integer32"
_DptScsiHbaBadMemoryAddress_Object = MibTableColumn
dptScsiHbaBadMemoryAddress = _DptScsiHbaBadMemoryAddress_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 2, 1, 1, 26),
    _DptScsiHbaBadMemoryAddress_Type()
)
dptScsiHbaBadMemoryAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiHbaBadMemoryAddress.setStatus("mandatory")
_DptScsiHbaBatteryModule_Type = BatteryBackupModule
_DptScsiHbaBatteryModule_Object = MibTableColumn
dptScsiHbaBatteryModule = _DptScsiHbaBatteryModule_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 2, 1, 1, 27),
    _DptScsiHbaBatteryModule_Type()
)
dptScsiHbaBatteryModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiHbaBatteryModule.setStatus("mandatory")
_DptScsiHbaBatteryStatus_Type = BatteryStatus
_DptScsiHbaBatteryStatus_Object = MibTableColumn
dptScsiHbaBatteryStatus = _DptScsiHbaBatteryStatus_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 2, 1, 1, 28),
    _DptScsiHbaBatteryStatus_Type()
)
dptScsiHbaBatteryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiHbaBatteryStatus.setStatus("mandatory")
_DptScsiHbaHighestBusWithDevices_Type = Integer32
_DptScsiHbaHighestBusWithDevices_Object = MibTableColumn
dptScsiHbaHighestBusWithDevices = _DptScsiHbaHighestBusWithDevices_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 2, 1, 1, 29),
    _DptScsiHbaHighestBusWithDevices_Type()
)
dptScsiHbaHighestBusWithDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiHbaHighestBusWithDevices.setStatus("mandatory")
_DptScsiHbaGeneralStatus_Type = HbaGenStatus
_DptScsiHbaGeneralStatus_Object = MibTableColumn
dptScsiHbaGeneralStatus = _DptScsiHbaGeneralStatus_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 2, 1, 1, 30),
    _DptScsiHbaGeneralStatus_Type()
)
dptScsiHbaGeneralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiHbaGeneralStatus.setStatus("mandatory")
_DptScsiHbaSmorSignature_Type = DptSignature
_DptScsiHbaSmorSignature_Object = MibTableColumn
dptScsiHbaSmorSignature = _DptScsiHbaSmorSignature_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 2, 1, 1, 31),
    _DptScsiHbaSmorSignature_Type()
)
dptScsiHbaSmorSignature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiHbaSmorSignature.setStatus("mandatory")
_DptScsiHbaBiosSignature_Type = DptSignature
_DptScsiHbaBiosSignature_Object = MibTableColumn
dptScsiHbaBiosSignature = _DptScsiHbaBiosSignature_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 2, 1, 1, 32),
    _DptScsiHbaBiosSignature_Type()
)
dptScsiHbaBiosSignature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiHbaBiosSignature.setStatus("mandatory")
_DptScsiHbaNvramLayout_Type = DisplayString
_DptScsiHbaNvramLayout_Object = MibTableColumn
dptScsiHbaNvramLayout = _DptScsiHbaNvramLayout_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 2, 1, 1, 33),
    _DptScsiHbaNvramLayout_Type()
)
dptScsiHbaNvramLayout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiHbaNvramLayout.setStatus("mandatory")
_DptScsiHbaCacheSocketTable_Object = MibTable
dptScsiHbaCacheSocketTable = _DptScsiHbaCacheSocketTable_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 2, 2)
)
if mibBuilder.loadTexts:
    dptScsiHbaCacheSocketTable.setStatus("mandatory")
_DptScsiHbaCacheSocketEntry_Object = MibTableRow
dptScsiHbaCacheSocketEntry = _DptScsiHbaCacheSocketEntry_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 2, 2, 1)
)
dptScsiHbaCacheSocketEntry.setIndexNames(
    (0, "DPT-SCSI-MIB", "dptScsiHbaNumber"),
    (0, "DPT-SCSI-MIB", "dptScsiHbaCacheSocketNumber"),
)
if mibBuilder.loadTexts:
    dptScsiHbaCacheSocketEntry.setStatus("mandatory")


class _DptScsiHbaCacheSocketNumber_Type(Integer32):
    """Custom type dptScsiHbaCacheSocketNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_DptScsiHbaCacheSocketNumber_Type.__name__ = "Integer32"
_DptScsiHbaCacheSocketNumber_Object = MibTableColumn
dptScsiHbaCacheSocketNumber = _DptScsiHbaCacheSocketNumber_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 2, 2, 1, 1),
    _DptScsiHbaCacheSocketNumber_Type()
)
dptScsiHbaCacheSocketNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiHbaCacheSocketNumber.setStatus("mandatory")
_DptScsiHbaCacheModuleType_Type = MemoryBankType
_DptScsiHbaCacheModuleType_Object = MibTableColumn
dptScsiHbaCacheModuleType = _DptScsiHbaCacheModuleType_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 2, 2, 1, 2),
    _DptScsiHbaCacheModuleType_Type()
)
dptScsiHbaCacheModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiHbaCacheModuleType.setStatus("mandatory")
_DptScsiHbaCacheModuleSize_Type = MemoryBankSize
_DptScsiHbaCacheModuleSize_Object = MibTableColumn
dptScsiHbaCacheModuleSize = _DptScsiHbaCacheModuleSize_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 2, 2, 1, 3),
    _DptScsiHbaCacheModuleSize_Type()
)
dptScsiHbaCacheModuleSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiHbaCacheModuleSize.setStatus("mandatory")
_DptScsiBus_ObjectIdentity = ObjectIdentity
dptScsiBus = _DptScsiBus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1597, 1, 3)
)
_DptScsiBusTable_Object = MibTable
dptScsiBusTable = _DptScsiBusTable_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dptScsiBusTable.setStatus("mandatory")
_DptScsiBusEntry_Object = MibTableRow
dptScsiBusEntry = _DptScsiBusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 3, 1, 1)
)
dptScsiBusEntry.setIndexNames(
    (0, "DPT-SCSI-MIB", "dptScsiHbaNumber"),
    (0, "DPT-SCSI-MIB", "dptScsiBusNumber"),
)
if mibBuilder.loadTexts:
    dptScsiBusEntry.setStatus("mandatory")


class _DptScsiBusNumber_Type(Integer32):
    """Custom type dptScsiBusNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DptScsiBusNumber_Type.__name__ = "Integer32"
_DptScsiBusNumber_Object = MibTableColumn
dptScsiBusNumber = _DptScsiBusNumber_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 3, 1, 1, 1),
    _DptScsiBusNumber_Type()
)
dptScsiBusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiBusNumber.setStatus("mandatory")
_DptScsiBusWidth_Type = BusWidth
_DptScsiBusWidth_Object = MibTableColumn
dptScsiBusWidth = _DptScsiBusWidth_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 3, 1, 1, 2),
    _DptScsiBusWidth_Type()
)
dptScsiBusWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiBusWidth.setStatus("mandatory")
_DptScsiBusType_Type = ScsiBusType
_DptScsiBusType_Object = MibTableColumn
dptScsiBusType = _DptScsiBusType_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 3, 1, 1, 3),
    _DptScsiBusType_Type()
)
dptScsiBusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiBusType.setStatus("mandatory")
_DptScsiBusMaxTransferRate_Type = Integer32
_DptScsiBusMaxTransferRate_Object = MibTableColumn
dptScsiBusMaxTransferRate = _DptScsiBusMaxTransferRate_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 3, 1, 1, 4),
    _DptScsiBusMaxTransferRate_Type()
)
dptScsiBusMaxTransferRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiBusMaxTransferRate.setStatus("mandatory")


class _DptScsiBusHbaScsiId_Type(Integer32):
    """Custom type dptScsiBusHbaScsiId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_DptScsiBusHbaScsiId_Type.__name__ = "Integer32"
_DptScsiBusHbaScsiId_Object = MibTableColumn
dptScsiBusHbaScsiId = _DptScsiBusHbaScsiId_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 3, 1, 1, 5),
    _DptScsiBusHbaScsiId_Type()
)
dptScsiBusHbaScsiId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiBusHbaScsiId.setStatus("mandatory")
_DptScsiBusHbaTermPower_Type = YesNoStatus
_DptScsiBusHbaTermPower_Object = MibTableColumn
dptScsiBusHbaTermPower = _DptScsiBusHbaTermPower_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 3, 1, 1, 6),
    _DptScsiBusHbaTermPower_Type()
)
dptScsiBusHbaTermPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiBusHbaTermPower.setStatus("mandatory")
_DptScsiBusHbaTermination_Type = BusTerminationType
_DptScsiBusHbaTermination_Object = MibTableColumn
dptScsiBusHbaTermination = _DptScsiBusHbaTermination_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 3, 1, 1, 7),
    _DptScsiBusHbaTermination_Type()
)
dptScsiBusHbaTermination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiBusHbaTermination.setStatus("mandatory")
_DptScsiDev_ObjectIdentity = ObjectIdentity
dptScsiDev = _DptScsiDev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1597, 1, 4)
)
_DptScsiDevTable_Object = MibTable
dptScsiDevTable = _DptScsiDevTable_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 4, 1)
)
if mibBuilder.loadTexts:
    dptScsiDevTable.setStatus("mandatory")
_DptScsiDevEntry_Object = MibTableRow
dptScsiDevEntry = _DptScsiDevEntry_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 4, 1, 1)
)
dptScsiDevEntry.setIndexNames(
    (0, "DPT-SCSI-MIB", "dptScsiHbaNumber"),
    (0, "DPT-SCSI-MIB", "dptScsiBusNumber"),
    (0, "DPT-SCSI-MIB", "dptScsiDevId"),
    (0, "DPT-SCSI-MIB", "dptScsiDevLun"),
    (0, "DPT-SCSI-MIB", "dptScsiDevLevel"),
)
if mibBuilder.loadTexts:
    dptScsiDevEntry.setStatus("mandatory")


class _DptScsiDevId_Type(Integer32):
    """Custom type dptScsiDevId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_DptScsiDevId_Type.__name__ = "Integer32"
_DptScsiDevId_Object = MibTableColumn
dptScsiDevId = _DptScsiDevId_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 4, 1, 1, 1),
    _DptScsiDevId_Type()
)
dptScsiDevId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiDevId.setStatus("mandatory")


class _DptScsiDevLun_Type(Integer32):
    """Custom type dptScsiDevLun based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DptScsiDevLun_Type.__name__ = "Integer32"
_DptScsiDevLun_Object = MibTableColumn
dptScsiDevLun = _DptScsiDevLun_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 4, 1, 1, 2),
    _DptScsiDevLun_Type()
)
dptScsiDevLun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiDevLun.setStatus("mandatory")


class _DptScsiDevLevel_Type(Integer32):
    """Custom type dptScsiDevLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_DptScsiDevLevel_Type.__name__ = "Integer32"
_DptScsiDevLevel_Object = MibTableColumn
dptScsiDevLevel = _DptScsiDevLevel_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 4, 1, 1, 3),
    _DptScsiDevLevel_Type()
)
dptScsiDevLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiDevLevel.setStatus("mandatory")


class _DptScsiDevVendor_Type(DisplayString):
    """Custom type dptScsiDevVendor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_DptScsiDevVendor_Type.__name__ = "DisplayString"
_DptScsiDevVendor_Object = MibTableColumn
dptScsiDevVendor = _DptScsiDevVendor_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 4, 1, 1, 4),
    _DptScsiDevVendor_Type()
)
dptScsiDevVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiDevVendor.setStatus("mandatory")


class _DptScsiDevModel_Type(DisplayString):
    """Custom type dptScsiDevModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_DptScsiDevModel_Type.__name__ = "DisplayString"
_DptScsiDevModel_Object = MibTableColumn
dptScsiDevModel = _DptScsiDevModel_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 4, 1, 1, 5),
    _DptScsiDevModel_Type()
)
dptScsiDevModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiDevModel.setStatus("mandatory")


class _DptScsiDevRevision_Type(DisplayString):
    """Custom type dptScsiDevRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_DptScsiDevRevision_Type.__name__ = "DisplayString"
_DptScsiDevRevision_Object = MibTableColumn
dptScsiDevRevision = _DptScsiDevRevision_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 4, 1, 1, 6),
    _DptScsiDevRevision_Type()
)
dptScsiDevRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiDevRevision.setStatus("mandatory")


class _DptScsiDevSerialNumber_Type(DisplayString):
    """Custom type dptScsiDevSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DptScsiDevSerialNumber_Type.__name__ = "DisplayString"
_DptScsiDevSerialNumber_Object = MibTableColumn
dptScsiDevSerialNumber = _DptScsiDevSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 4, 1, 1, 7),
    _DptScsiDevSerialNumber_Type()
)
dptScsiDevSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiDevSerialNumber.setStatus("mandatory")
_DptScsiDevStatus_Type = DeviceStatus
_DptScsiDevStatus_Object = MibTableColumn
dptScsiDevStatus = _DptScsiDevStatus_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 4, 1, 1, 8),
    _DptScsiDevStatus_Type()
)
dptScsiDevStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiDevStatus.setStatus("mandatory")
_DptScsiDevBusWidth_Type = BusWidth
_DptScsiDevBusWidth_Object = MibTableColumn
dptScsiDevBusWidth = _DptScsiDevBusWidth_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 4, 1, 1, 9),
    _DptScsiDevBusWidth_Type()
)
dptScsiDevBusWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiDevBusWidth.setStatus("mandatory")


class _DptScsiDevCapacity_Type(Integer32):
    """Custom type dptScsiDevCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DptScsiDevCapacity_Type.__name__ = "Integer32"
_DptScsiDevCapacity_Object = MibTableColumn
dptScsiDevCapacity = _DptScsiDevCapacity_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 4, 1, 1, 10),
    _DptScsiDevCapacity_Type()
)
dptScsiDevCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiDevCapacity.setStatus("mandatory")


class _DptScsiDevLogicalBlockSize_Type(Integer32):
    """Custom type dptScsiDevLogicalBlockSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DptScsiDevLogicalBlockSize_Type.__name__ = "Integer32"
_DptScsiDevLogicalBlockSize_Object = MibTableColumn
dptScsiDevLogicalBlockSize = _DptScsiDevLogicalBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 4, 1, 1, 11),
    _DptScsiDevLogicalBlockSize_Type()
)
dptScsiDevLogicalBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiDevLogicalBlockSize.setStatus("mandatory")


class _DptScsiDevPhysicalBlockSize_Type(Integer32):
    """Custom type dptScsiDevPhysicalBlockSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DptScsiDevPhysicalBlockSize_Type.__name__ = "Integer32"
_DptScsiDevPhysicalBlockSize_Object = MibTableColumn
dptScsiDevPhysicalBlockSize = _DptScsiDevPhysicalBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 4, 1, 1, 12),
    _DptScsiDevPhysicalBlockSize_Type()
)
dptScsiDevPhysicalBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiDevPhysicalBlockSize.setStatus("mandatory")
_DptScsiDevNegTransferRate_Type = Integer32
_DptScsiDevNegTransferRate_Object = MibTableColumn
dptScsiDevNegTransferRate = _DptScsiDevNegTransferRate_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 4, 1, 1, 13),
    _DptScsiDevNegTransferRate_Type()
)
dptScsiDevNegTransferRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiDevNegTransferRate.setStatus("mandatory")
_DptScsiDevRemovable_Type = YesNoStatus
_DptScsiDevRemovable_Object = MibTableColumn
dptScsiDevRemovable = _DptScsiDevRemovable_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 4, 1, 1, 14),
    _DptScsiDevRemovable_Type()
)
dptScsiDevRemovable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiDevRemovable.setStatus("mandatory")
_DptScsiDevEccEnabled_Type = YesNoStatus
_DptScsiDevEccEnabled_Object = MibTableColumn
dptScsiDevEccEnabled = _DptScsiDevEccEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 4, 1, 1, 15),
    _DptScsiDevEccEnabled_Type()
)
dptScsiDevEccEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiDevEccEnabled.setStatus("deprecated")
_DptScsiDevScsiVersion_Type = ScsiVersion
_DptScsiDevScsiVersion_Object = MibTableColumn
dptScsiDevScsiVersion = _DptScsiDevScsiVersion_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 4, 1, 1, 16),
    _DptScsiDevScsiVersion_Type()
)
dptScsiDevScsiVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiDevScsiVersion.setStatus("mandatory")
_DptScsiDevSoftReset_Type = YesNoStatus
_DptScsiDevSoftReset_Object = MibTableColumn
dptScsiDevSoftReset = _DptScsiDevSoftReset_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 4, 1, 1, 17),
    _DptScsiDevSoftReset_Type()
)
dptScsiDevSoftReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiDevSoftReset.setStatus("mandatory")
_DptScsiDevCmdQueuing_Type = YesNoStatus
_DptScsiDevCmdQueuing_Object = MibTableColumn
dptScsiDevCmdQueuing = _DptScsiDevCmdQueuing_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 4, 1, 1, 18),
    _DptScsiDevCmdQueuing_Type()
)
dptScsiDevCmdQueuing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiDevCmdQueuing.setStatus("mandatory")
_DptScsiDevLinkedCmds_Type = YesNoStatus
_DptScsiDevLinkedCmds_Object = MibTableColumn
dptScsiDevLinkedCmds = _DptScsiDevLinkedCmds_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 4, 1, 1, 19),
    _DptScsiDevLinkedCmds_Type()
)
dptScsiDevLinkedCmds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiDevLinkedCmds.setStatus("mandatory")
_DptScsiDevSynchronous_Type = YesNoStatus
_DptScsiDevSynchronous_Object = MibTableColumn
dptScsiDevSynchronous = _DptScsiDevSynchronous_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 4, 1, 1, 20),
    _DptScsiDevSynchronous_Type()
)
dptScsiDevSynchronous.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiDevSynchronous.setStatus("mandatory")
_DptScsiDevRelAddr_Type = YesNoStatus
_DptScsiDevRelAddr_Object = MibTableColumn
dptScsiDevRelAddr = _DptScsiDevRelAddr_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 4, 1, 1, 21),
    _DptScsiDevRelAddr_Type()
)
dptScsiDevRelAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiDevRelAddr.setStatus("mandatory")
_DptScsiDevSMART_Type = YesNoStatus
_DptScsiDevSMART_Object = MibTableColumn
dptScsiDevSMART = _DptScsiDevSMART_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 4, 1, 1, 22),
    _DptScsiDevSMART_Type()
)
dptScsiDevSMART.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiDevSMART.setStatus("mandatory")
_DptScsiDevSCAM_Type = YesNoStatus
_DptScsiDevSCAM_Object = MibTableColumn
dptScsiDevSCAM = _DptScsiDevSCAM_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 4, 1, 1, 23),
    _DptScsiDevSCAM_Type()
)
dptScsiDevSCAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiDevSCAM.setStatus("deprecated")


class _DptScsiDevBadBlockNumber_Type(Integer32):
    """Custom type dptScsiDevBadBlockNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DptScsiDevBadBlockNumber_Type.__name__ = "Integer32"
_DptScsiDevBadBlockNumber_Object = MibTableColumn
dptScsiDevBadBlockNumber = _DptScsiDevBadBlockNumber_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 4, 1, 1, 24),
    _DptScsiDevBadBlockNumber_Type()
)
dptScsiDevBadBlockNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiDevBadBlockNumber.setStatus("mandatory")


class _DptScsiDevBadBlockCount_Type(Integer32):
    """Custom type dptScsiDevBadBlockCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DptScsiDevBadBlockCount_Type.__name__ = "Integer32"
_DptScsiDevBadBlockCount_Object = MibTableColumn
dptScsiDevBadBlockCount = _DptScsiDevBadBlockCount_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 4, 1, 1, 25),
    _DptScsiDevBadBlockCount_Type()
)
dptScsiDevBadBlockCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiDevBadBlockCount.setStatus("mandatory")
_DptScsiDevErrorsAboveThreshold_Type = YesNoStatus
_DptScsiDevErrorsAboveThreshold_Object = MibTableColumn
dptScsiDevErrorsAboveThreshold = _DptScsiDevErrorsAboveThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 4, 1, 1, 26),
    _DptScsiDevErrorsAboveThreshold_Type()
)
dptScsiDevErrorsAboveThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiDevErrorsAboveThreshold.setStatus("deprecated")
_DptScsiDevDriveLockingOn_Type = YesNoStatus
_DptScsiDevDriveLockingOn_Object = MibTableColumn
dptScsiDevDriveLockingOn = _DptScsiDevDriveLockingOn_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 4, 1, 1, 27),
    _DptScsiDevDriveLockingOn_Type()
)
dptScsiDevDriveLockingOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiDevDriveLockingOn.setStatus("deprecated")
_DptScsiDevLastReqSenseInfo_Type = DisplayString
_DptScsiDevLastReqSenseInfo_Object = MibTableColumn
dptScsiDevLastReqSenseInfo = _DptScsiDevLastReqSenseInfo_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 4, 1, 1, 28),
    _DptScsiDevLastReqSenseInfo_Type()
)
dptScsiDevLastReqSenseInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiDevLastReqSenseInfo.setStatus("mandatory")
_DptScsiDevReadCachingOn_Type = YesNoStatus
_DptScsiDevReadCachingOn_Object = MibTableColumn
dptScsiDevReadCachingOn = _DptScsiDevReadCachingOn_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 4, 1, 1, 29),
    _DptScsiDevReadCachingOn_Type()
)
dptScsiDevReadCachingOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiDevReadCachingOn.setStatus("deprecated")
_DptScsiDevReadCacheMaxRecord_Type = Integer32
_DptScsiDevReadCacheMaxRecord_Object = MibTableColumn
dptScsiDevReadCacheMaxRecord = _DptScsiDevReadCacheMaxRecord_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 4, 1, 1, 30),
    _DptScsiDevReadCacheMaxRecord_Type()
)
dptScsiDevReadCacheMaxRecord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiDevReadCacheMaxRecord.setStatus("deprecated")
_DptScsiDevWriteCachingOn_Type = YesNoStatus
_DptScsiDevWriteCachingOn_Object = MibTableColumn
dptScsiDevWriteCachingOn = _DptScsiDevWriteCachingOn_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 4, 1, 1, 31),
    _DptScsiDevWriteCachingOn_Type()
)
dptScsiDevWriteCachingOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiDevWriteCachingOn.setStatus("deprecated")
_DptScsiDevWriteCacheMaxRecord_Type = Integer32
_DptScsiDevWriteCacheMaxRecord_Object = MibTableColumn
dptScsiDevWriteCacheMaxRecord = _DptScsiDevWriteCacheMaxRecord_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 4, 1, 1, 32),
    _DptScsiDevWriteCacheMaxRecord_Type()
)
dptScsiDevWriteCacheMaxRecord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiDevWriteCacheMaxRecord.setStatus("deprecated")
_DptScsiDevWriteMode_Type = DeviceWriteMode
_DptScsiDevWriteMode_Object = MibTableColumn
dptScsiDevWriteMode = _DptScsiDevWriteMode_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 4, 1, 1, 33),
    _DptScsiDevWriteMode_Type()
)
dptScsiDevWriteMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiDevWriteMode.setStatus("mandatory")
_DptScsiDevSmartStatusOk_Type = YesNoStatus
_DptScsiDevSmartStatusOk_Object = MibTableColumn
dptScsiDevSmartStatusOk = _DptScsiDevSmartStatusOk_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 4, 1, 1, 34),
    _DptScsiDevSmartStatusOk_Type()
)
dptScsiDevSmartStatusOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiDevSmartStatusOk.setStatus("mandatory")
_DptScsiDevType_Type = DeviceType
_DptScsiDevType_Object = MibTableColumn
dptScsiDevType = _DptScsiDevType_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 4, 1, 1, 35),
    _DptScsiDevType_Type()
)
dptScsiDevType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiDevType.setStatus("mandatory")
_DptScsiArr_ObjectIdentity = ObjectIdentity
dptScsiArr = _DptScsiArr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1597, 1, 5)
)
_DptScsiArrTable_Object = MibTable
dptScsiArrTable = _DptScsiArrTable_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 5, 1)
)
if mibBuilder.loadTexts:
    dptScsiArrTable.setStatus("mandatory")
_DptScsiArrEntry_Object = MibTableRow
dptScsiArrEntry = _DptScsiArrEntry_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 5, 1, 1)
)
dptScsiArrEntry.setIndexNames(
    (0, "DPT-SCSI-MIB", "dptScsiHbaNumber"),
    (0, "DPT-SCSI-MIB", "dptScsiBusNumber"),
    (0, "DPT-SCSI-MIB", "dptScsiDevId"),
    (0, "DPT-SCSI-MIB", "dptScsiDevLun"),
    (0, "DPT-SCSI-MIB", "dptScsiDevLevel"),
)
if mibBuilder.loadTexts:
    dptScsiArrEntry.setStatus("mandatory")
_DptScsiArrType_Type = RaidType
_DptScsiArrType_Object = MibTableColumn
dptScsiArrType = _DptScsiArrType_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 5, 1, 1, 1),
    _DptScsiArrType_Type()
)
dptScsiArrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiArrType.setStatus("mandatory")
_DptScsiArrOwner_Type = SoftwareType
_DptScsiArrOwner_Object = MibTableColumn
dptScsiArrOwner = _DptScsiArrOwner_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 5, 1, 1, 2),
    _DptScsiArrOwner_Type()
)
dptScsiArrOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiArrOwner.setStatus("mandatory")


class _DptScsiArrName_Type(DisplayString):
    """Custom type dptScsiArrName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_DptScsiArrName_Type.__name__ = "DisplayString"
_DptScsiArrName_Object = MibTableColumn
dptScsiArrName = _DptScsiArrName_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 5, 1, 1, 3),
    _DptScsiArrName_Type()
)
dptScsiArrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiArrName.setStatus("mandatory")


class _DptScsiArrBackgroundProgress_Type(Integer32):
    """Custom type dptScsiArrBackgroundProgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DptScsiArrBackgroundProgress_Type.__name__ = "Integer32"
_DptScsiArrBackgroundProgress_Object = MibTableColumn
dptScsiArrBackgroundProgress = _DptScsiArrBackgroundProgress_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 5, 1, 1, 4),
    _DptScsiArrBackgroundProgress_Type()
)
dptScsiArrBackgroundProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiArrBackgroundProgress.setStatus("mandatory")
_DptScsiArrEntryStatus_Type = RowStatus
_DptScsiArrEntryStatus_Object = MibTableColumn
dptScsiArrEntryStatus = _DptScsiArrEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 5, 1, 1, 5),
    _DptScsiArrEntryStatus_Type()
)
dptScsiArrEntryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiArrEntryStatus.setStatus("mandatory")
_DptScsiArrMemberTable_Object = MibTable
dptScsiArrMemberTable = _DptScsiArrMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 5, 2)
)
if mibBuilder.loadTexts:
    dptScsiArrMemberTable.setStatus("mandatory")
_DptScsiArrMemberEntry_Object = MibTableRow
dptScsiArrMemberEntry = _DptScsiArrMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 5, 2, 1)
)
dptScsiArrMemberEntry.setIndexNames(
    (0, "DPT-SCSI-MIB", "dptScsiHbaNumber"),
    (0, "DPT-SCSI-MIB", "dptScsiBusNumber"),
    (0, "DPT-SCSI-MIB", "dptScsiDevId"),
    (0, "DPT-SCSI-MIB", "dptScsiDevLun"),
    (0, "DPT-SCSI-MIB", "dptScsiDevLevel"),
    (0, "DPT-SCSI-MIB", "dptScsiHbaNumberMember"),
    (0, "DPT-SCSI-MIB", "dptScsiBusNumberMember"),
    (0, "DPT-SCSI-MIB", "dptScsiDevIdMember"),
    (0, "DPT-SCSI-MIB", "dptScsiDevLunMember"),
    (0, "DPT-SCSI-MIB", "dptScsiDevLevelMember"),
)
if mibBuilder.loadTexts:
    dptScsiArrMemberEntry.setStatus("mandatory")


class _DptScsiArrMemberStripeSize_Type(Integer32):
    """Custom type dptScsiArrMemberStripeSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DptScsiArrMemberStripeSize_Type.__name__ = "Integer32"
_DptScsiArrMemberStripeSize_Object = MibTableColumn
dptScsiArrMemberStripeSize = _DptScsiArrMemberStripeSize_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 5, 2, 1, 1),
    _DptScsiArrMemberStripeSize_Type()
)
dptScsiArrMemberStripeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiArrMemberStripeSize.setStatus("mandatory")
_DptScsiArrMemberEntryStatus_Type = RowStatus
_DptScsiArrMemberEntryStatus_Object = MibTableColumn
dptScsiArrMemberEntryStatus = _DptScsiArrMemberEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 5, 2, 1, 2),
    _DptScsiArrMemberEntryStatus_Type()
)
dptScsiArrMemberEntryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiArrMemberEntryStatus.setStatus("mandatory")
_DptScsiStats_ObjectIdentity = ObjectIdentity
dptScsiStats = _DptScsiStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1597, 1, 6)
)
_DptScsiStatsHbaTable_Object = MibTable
dptScsiStatsHbaTable = _DptScsiStatsHbaTable_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 6, 1)
)
if mibBuilder.loadTexts:
    dptScsiStatsHbaTable.setStatus("mandatory")
_DptScsiStatsHbaEntry_Object = MibTableRow
dptScsiStatsHbaEntry = _DptScsiStatsHbaEntry_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 6, 1, 1)
)
dptScsiStatsHbaEntry.setIndexNames(
    (0, "DPT-SCSI-MIB", "dptScsiHbaNumber"),
)
if mibBuilder.loadTexts:
    dptScsiStatsHbaEntry.setStatus("mandatory")
_DptScsiStatsHbaCacheTotalPages_Type = Gauge32
_DptScsiStatsHbaCacheTotalPages_Object = MibTableColumn
dptScsiStatsHbaCacheTotalPages = _DptScsiStatsHbaCacheTotalPages_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 6, 1, 1, 1),
    _DptScsiStatsHbaCacheTotalPages_Type()
)
dptScsiStatsHbaCacheTotalPages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiStatsHbaCacheTotalPages.setStatus("mandatory")
_DptScsiStatsHbaCacheUsedPages_Type = Gauge32
_DptScsiStatsHbaCacheUsedPages_Object = MibTableColumn
dptScsiStatsHbaCacheUsedPages = _DptScsiStatsHbaCacheUsedPages_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 6, 1, 1, 2),
    _DptScsiStatsHbaCacheUsedPages_Type()
)
dptScsiStatsHbaCacheUsedPages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiStatsHbaCacheUsedPages.setStatus("mandatory")
_DptScsiStatsHbaCacheDirtyPages_Type = Gauge32
_DptScsiStatsHbaCacheDirtyPages_Object = MibTableColumn
dptScsiStatsHbaCacheDirtyPages = _DptScsiStatsHbaCacheDirtyPages_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 6, 1, 1, 3),
    _DptScsiStatsHbaCacheDirtyPages_Type()
)
dptScsiStatsHbaCacheDirtyPages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiStatsHbaCacheDirtyPages.setStatus("mandatory")
_DptScsiStatsHbaCacheReadAheadPages_Type = Gauge32
_DptScsiStatsHbaCacheReadAheadPages_Object = MibTableColumn
dptScsiStatsHbaCacheReadAheadPages = _DptScsiStatsHbaCacheReadAheadPages_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 6, 1, 1, 4),
    _DptScsiStatsHbaCacheReadAheadPages_Type()
)
dptScsiStatsHbaCacheReadAheadPages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiStatsHbaCacheReadAheadPages.setStatus("mandatory")
_DptScsiStatsHbaCacheLockedPages_Type = Gauge32
_DptScsiStatsHbaCacheLockedPages_Object = MibTableColumn
dptScsiStatsHbaCacheLockedPages = _DptScsiStatsHbaCacheLockedPages_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 6, 1, 1, 5),
    _DptScsiStatsHbaCacheLockedPages_Type()
)
dptScsiStatsHbaCacheLockedPages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiStatsHbaCacheLockedPages.setStatus("mandatory")
_DptScsiStatsHbaCacheEccFaultPages_Type = Gauge32
_DptScsiStatsHbaCacheEccFaultPages_Object = MibTableColumn
dptScsiStatsHbaCacheEccFaultPages = _DptScsiStatsHbaCacheEccFaultPages_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 6, 1, 1, 6),
    _DptScsiStatsHbaCacheEccFaultPages_Type()
)
dptScsiStatsHbaCacheEccFaultPages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiStatsHbaCacheEccFaultPages.setStatus("mandatory")
_DptScsiStatsHbaCommands_Type = Counter32
_DptScsiStatsHbaCommands_Object = MibTableColumn
dptScsiStatsHbaCommands = _DptScsiStatsHbaCommands_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 6, 1, 1, 7),
    _DptScsiStatsHbaCommands_Type()
)
dptScsiStatsHbaCommands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiStatsHbaCommands.setStatus("mandatory")
_DptScsiStatsHbaMisAlignedTransfers_Type = Counter32
_DptScsiStatsHbaMisAlignedTransfers_Object = MibTableColumn
dptScsiStatsHbaMisAlignedTransfers = _DptScsiStatsHbaMisAlignedTransfers_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 6, 1, 1, 8),
    _DptScsiStatsHbaMisAlignedTransfers_Type()
)
dptScsiStatsHbaMisAlignedTransfers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiStatsHbaMisAlignedTransfers.setStatus("mandatory")
_DptScsiStatsHbaScsiResets_Type = Counter32
_DptScsiStatsHbaScsiResets_Object = MibTableColumn
dptScsiStatsHbaScsiResets = _DptScsiStatsHbaScsiResets_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 6, 1, 1, 9),
    _DptScsiStatsHbaScsiResets_Type()
)
dptScsiStatsHbaScsiResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiStatsHbaScsiResets.setStatus("mandatory")
_DptScsiStatsDevTable_Object = MibTable
dptScsiStatsDevTable = _DptScsiStatsDevTable_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 6, 2)
)
if mibBuilder.loadTexts:
    dptScsiStatsDevTable.setStatus("mandatory")
_DptScsiStatsDevEntry_Object = MibTableRow
dptScsiStatsDevEntry = _DptScsiStatsDevEntry_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 6, 2, 1)
)
dptScsiStatsDevEntry.setIndexNames(
    (0, "DPT-SCSI-MIB", "dptScsiHbaNumber"),
    (0, "DPT-SCSI-MIB", "dptScsiBusNumber"),
    (0, "DPT-SCSI-MIB", "dptScsiDevId"),
    (0, "DPT-SCSI-MIB", "dptScsiDevLun"),
    (0, "DPT-SCSI-MIB", "dptScsiDevLevel"),
)
if mibBuilder.loadTexts:
    dptScsiStatsDevEntry.setStatus("mandatory")
_DptScsiStatsDevReadTotalSectors_Type = Counter32
_DptScsiStatsDevReadTotalSectors_Object = MibTableColumn
dptScsiStatsDevReadTotalSectors = _DptScsiStatsDevReadTotalSectors_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 6, 2, 1, 1),
    _DptScsiStatsDevReadTotalSectors_Type()
)
dptScsiStatsDevReadTotalSectors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiStatsDevReadTotalSectors.setStatus("mandatory")
_DptScsiStatsDevReadCacheHits_Type = Counter32
_DptScsiStatsDevReadCacheHits_Object = MibTableColumn
dptScsiStatsDevReadCacheHits = _DptScsiStatsDevReadCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 6, 2, 1, 2),
    _DptScsiStatsDevReadCacheHits_Type()
)
dptScsiStatsDevReadCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiStatsDevReadCacheHits.setStatus("mandatory")
_DptScsiStatsDevReadAheadHits_Type = Counter32
_DptScsiStatsDevReadAheadHits_Object = MibTableColumn
dptScsiStatsDevReadAheadHits = _DptScsiStatsDevReadAheadHits_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 6, 2, 1, 3),
    _DptScsiStatsDevReadAheadHits_Type()
)
dptScsiStatsDevReadAheadHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiStatsDevReadAheadHits.setStatus("mandatory")
_DptScsiStatsDevWriteTotalSectors_Type = Counter32
_DptScsiStatsDevWriteTotalSectors_Object = MibTableColumn
dptScsiStatsDevWriteTotalSectors = _DptScsiStatsDevWriteTotalSectors_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 6, 2, 1, 4),
    _DptScsiStatsDevWriteTotalSectors_Type()
)
dptScsiStatsDevWriteTotalSectors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiStatsDevWriteTotalSectors.setStatus("mandatory")
_DptScsiStatsDevWriteCacheHits_Type = Counter32
_DptScsiStatsDevWriteCacheHits_Object = MibTableColumn
dptScsiStatsDevWriteCacheHits = _DptScsiStatsDevWriteCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 6, 2, 1, 5),
    _DptScsiStatsDevWriteCacheHits_Type()
)
dptScsiStatsDevWriteCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiStatsDevWriteCacheHits.setStatus("mandatory")
_DptScsiStatsDevWriteBacks_Type = Counter32
_DptScsiStatsDevWriteBacks_Object = MibTableColumn
dptScsiStatsDevWriteBacks = _DptScsiStatsDevWriteBacks_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 6, 2, 1, 6),
    _DptScsiStatsDevWriteBacks_Type()
)
dptScsiStatsDevWriteBacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiStatsDevWriteBacks.setStatus("mandatory")
_DptScsiStatsDevStripesCrosseds_Type = Counter32
_DptScsiStatsDevStripesCrosseds_Object = MibTableColumn
dptScsiStatsDevStripesCrosseds = _DptScsiStatsDevStripesCrosseds_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 6, 2, 1, 7),
    _DptScsiStatsDevStripesCrosseds_Type()
)
dptScsiStatsDevStripesCrosseds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiStatsDevStripesCrosseds.setStatus("mandatory")
_DptScsiStatsDevRWCmdsTable_Object = MibTable
dptScsiStatsDevRWCmdsTable = _DptScsiStatsDevRWCmdsTable_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 6, 3)
)
if mibBuilder.loadTexts:
    dptScsiStatsDevRWCmdsTable.setStatus("mandatory")
_DptScsiStatsDevRWCmdsEntry_Object = MibTableRow
dptScsiStatsDevRWCmdsEntry = _DptScsiStatsDevRWCmdsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 6, 3, 1)
)
dptScsiStatsDevRWCmdsEntry.setIndexNames(
    (0, "DPT-SCSI-MIB", "dptScsiHbaNumber"),
    (0, "DPT-SCSI-MIB", "dptScsiBusNumber"),
    (0, "DPT-SCSI-MIB", "dptScsiDevId"),
    (0, "DPT-SCSI-MIB", "dptScsiDevLun"),
    (0, "DPT-SCSI-MIB", "dptScsiDevLevel"),
    (0, "DPT-SCSI-MIB", "dptScsiStatsDevRWCmdsType"),
)
if mibBuilder.loadTexts:
    dptScsiStatsDevRWCmdsEntry.setStatus("mandatory")
_DptScsiStatsDevRWCmdsType_Type = CommandType
_DptScsiStatsDevRWCmdsType_Object = MibTableColumn
dptScsiStatsDevRWCmdsType = _DptScsiStatsDevRWCmdsType_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 6, 3, 1, 1),
    _DptScsiStatsDevRWCmdsType_Type()
)
dptScsiStatsDevRWCmdsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiStatsDevRWCmdsType.setStatus("mandatory")
_DptScsiStatsDevRead1Ks_Type = Counter32
_DptScsiStatsDevRead1Ks_Object = MibTableColumn
dptScsiStatsDevRead1Ks = _DptScsiStatsDevRead1Ks_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 6, 3, 1, 2),
    _DptScsiStatsDevRead1Ks_Type()
)
dptScsiStatsDevRead1Ks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiStatsDevRead1Ks.setStatus("mandatory")
_DptScsiStatsDevRead2Ks_Type = Counter32
_DptScsiStatsDevRead2Ks_Object = MibTableColumn
dptScsiStatsDevRead2Ks = _DptScsiStatsDevRead2Ks_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 6, 3, 1, 3),
    _DptScsiStatsDevRead2Ks_Type()
)
dptScsiStatsDevRead2Ks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiStatsDevRead2Ks.setStatus("mandatory")
_DptScsiStatsDevRead4Ks_Type = Counter32
_DptScsiStatsDevRead4Ks_Object = MibTableColumn
dptScsiStatsDevRead4Ks = _DptScsiStatsDevRead4Ks_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 6, 3, 1, 4),
    _DptScsiStatsDevRead4Ks_Type()
)
dptScsiStatsDevRead4Ks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiStatsDevRead4Ks.setStatus("mandatory")
_DptScsiStatsDevRead8Ks_Type = Counter32
_DptScsiStatsDevRead8Ks_Object = MibTableColumn
dptScsiStatsDevRead8Ks = _DptScsiStatsDevRead8Ks_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 6, 3, 1, 5),
    _DptScsiStatsDevRead8Ks_Type()
)
dptScsiStatsDevRead8Ks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiStatsDevRead8Ks.setStatus("mandatory")
_DptScsiStatsDevRead16Ks_Type = Counter32
_DptScsiStatsDevRead16Ks_Object = MibTableColumn
dptScsiStatsDevRead16Ks = _DptScsiStatsDevRead16Ks_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 6, 3, 1, 6),
    _DptScsiStatsDevRead16Ks_Type()
)
dptScsiStatsDevRead16Ks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiStatsDevRead16Ks.setStatus("mandatory")
_DptScsiStatsDevRead32Ks_Type = Counter32
_DptScsiStatsDevRead32Ks_Object = MibTableColumn
dptScsiStatsDevRead32Ks = _DptScsiStatsDevRead32Ks_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 6, 3, 1, 7),
    _DptScsiStatsDevRead32Ks_Type()
)
dptScsiStatsDevRead32Ks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiStatsDevRead32Ks.setStatus("mandatory")
_DptScsiStatsDevRead64Ks_Type = Counter32
_DptScsiStatsDevRead64Ks_Object = MibTableColumn
dptScsiStatsDevRead64Ks = _DptScsiStatsDevRead64Ks_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 6, 3, 1, 8),
    _DptScsiStatsDevRead64Ks_Type()
)
dptScsiStatsDevRead64Ks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiStatsDevRead64Ks.setStatus("mandatory")
_DptScsiStatsDevRead128Ks_Type = Counter32
_DptScsiStatsDevRead128Ks_Object = MibTableColumn
dptScsiStatsDevRead128Ks = _DptScsiStatsDevRead128Ks_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 6, 3, 1, 9),
    _DptScsiStatsDevRead128Ks_Type()
)
dptScsiStatsDevRead128Ks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiStatsDevRead128Ks.setStatus("mandatory")
_DptScsiStatsDevRead256Ks_Type = Counter32
_DptScsiStatsDevRead256Ks_Object = MibTableColumn
dptScsiStatsDevRead256Ks = _DptScsiStatsDevRead256Ks_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 6, 3, 1, 10),
    _DptScsiStatsDevRead256Ks_Type()
)
dptScsiStatsDevRead256Ks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiStatsDevRead256Ks.setStatus("mandatory")
_DptScsiStatsDevRead512Ks_Type = Counter32
_DptScsiStatsDevRead512Ks_Object = MibTableColumn
dptScsiStatsDevRead512Ks = _DptScsiStatsDevRead512Ks_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 6, 3, 1, 11),
    _DptScsiStatsDevRead512Ks_Type()
)
dptScsiStatsDevRead512Ks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiStatsDevRead512Ks.setStatus("mandatory")
_DptScsiStatsDevRead1MBs_Type = Counter32
_DptScsiStatsDevRead1MBs_Object = MibTableColumn
dptScsiStatsDevRead1MBs = _DptScsiStatsDevRead1MBs_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 6, 3, 1, 12),
    _DptScsiStatsDevRead1MBs_Type()
)
dptScsiStatsDevRead1MBs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiStatsDevRead1MBs.setStatus("mandatory")
_DptScsiStatsDevReadGreater1MBs_Type = Counter32
_DptScsiStatsDevReadGreater1MBs_Object = MibTableColumn
dptScsiStatsDevReadGreater1MBs = _DptScsiStatsDevReadGreater1MBs_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 6, 3, 1, 13),
    _DptScsiStatsDevReadGreater1MBs_Type()
)
dptScsiStatsDevReadGreater1MBs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiStatsDevReadGreater1MBs.setStatus("mandatory")
_DptScsiStatsDevWrite1Ks_Type = Counter32
_DptScsiStatsDevWrite1Ks_Object = MibTableColumn
dptScsiStatsDevWrite1Ks = _DptScsiStatsDevWrite1Ks_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 6, 3, 1, 14),
    _DptScsiStatsDevWrite1Ks_Type()
)
dptScsiStatsDevWrite1Ks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiStatsDevWrite1Ks.setStatus("mandatory")
_DptScsiStatsDevWrite2Ks_Type = Counter32
_DptScsiStatsDevWrite2Ks_Object = MibTableColumn
dptScsiStatsDevWrite2Ks = _DptScsiStatsDevWrite2Ks_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 6, 3, 1, 15),
    _DptScsiStatsDevWrite2Ks_Type()
)
dptScsiStatsDevWrite2Ks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiStatsDevWrite2Ks.setStatus("mandatory")
_DptScsiStatsDevWrite4Ks_Type = Counter32
_DptScsiStatsDevWrite4Ks_Object = MibTableColumn
dptScsiStatsDevWrite4Ks = _DptScsiStatsDevWrite4Ks_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 6, 3, 1, 16),
    _DptScsiStatsDevWrite4Ks_Type()
)
dptScsiStatsDevWrite4Ks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiStatsDevWrite4Ks.setStatus("mandatory")
_DptScsiStatsDevWrite8Ks_Type = Counter32
_DptScsiStatsDevWrite8Ks_Object = MibTableColumn
dptScsiStatsDevWrite8Ks = _DptScsiStatsDevWrite8Ks_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 6, 3, 1, 17),
    _DptScsiStatsDevWrite8Ks_Type()
)
dptScsiStatsDevWrite8Ks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiStatsDevWrite8Ks.setStatus("mandatory")
_DptScsiStatsDevWrite16Ks_Type = Counter32
_DptScsiStatsDevWrite16Ks_Object = MibTableColumn
dptScsiStatsDevWrite16Ks = _DptScsiStatsDevWrite16Ks_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 6, 3, 1, 18),
    _DptScsiStatsDevWrite16Ks_Type()
)
dptScsiStatsDevWrite16Ks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiStatsDevWrite16Ks.setStatus("mandatory")
_DptScsiStatsDevWrite32Ks_Type = Counter32
_DptScsiStatsDevWrite32Ks_Object = MibTableColumn
dptScsiStatsDevWrite32Ks = _DptScsiStatsDevWrite32Ks_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 6, 3, 1, 19),
    _DptScsiStatsDevWrite32Ks_Type()
)
dptScsiStatsDevWrite32Ks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiStatsDevWrite32Ks.setStatus("mandatory")
_DptScsiStatsDevWrite64Ks_Type = Counter32
_DptScsiStatsDevWrite64Ks_Object = MibTableColumn
dptScsiStatsDevWrite64Ks = _DptScsiStatsDevWrite64Ks_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 6, 3, 1, 20),
    _DptScsiStatsDevWrite64Ks_Type()
)
dptScsiStatsDevWrite64Ks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiStatsDevWrite64Ks.setStatus("mandatory")
_DptScsiStatsDevWrite128Ks_Type = Counter32
_DptScsiStatsDevWrite128Ks_Object = MibTableColumn
dptScsiStatsDevWrite128Ks = _DptScsiStatsDevWrite128Ks_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 6, 3, 1, 21),
    _DptScsiStatsDevWrite128Ks_Type()
)
dptScsiStatsDevWrite128Ks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiStatsDevWrite128Ks.setStatus("mandatory")
_DptScsiStatsDevWrite256Ks_Type = Counter32
_DptScsiStatsDevWrite256Ks_Object = MibTableColumn
dptScsiStatsDevWrite256Ks = _DptScsiStatsDevWrite256Ks_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 6, 3, 1, 22),
    _DptScsiStatsDevWrite256Ks_Type()
)
dptScsiStatsDevWrite256Ks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiStatsDevWrite256Ks.setStatus("mandatory")
_DptScsiStatsDevWrite512Ks_Type = Counter32
_DptScsiStatsDevWrite512Ks_Object = MibTableColumn
dptScsiStatsDevWrite512Ks = _DptScsiStatsDevWrite512Ks_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 6, 3, 1, 23),
    _DptScsiStatsDevWrite512Ks_Type()
)
dptScsiStatsDevWrite512Ks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiStatsDevWrite512Ks.setStatus("mandatory")
_DptScsiStatsDevWrite1MBs_Type = Counter32
_DptScsiStatsDevWrite1MBs_Object = MibTableColumn
dptScsiStatsDevWrite1MBs = _DptScsiStatsDevWrite1MBs_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 6, 3, 1, 24),
    _DptScsiStatsDevWrite1MBs_Type()
)
dptScsiStatsDevWrite1MBs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiStatsDevWrite1MBs.setStatus("mandatory")
_DptScsiStatsDevWriteGreater1MBs_Type = Counter32
_DptScsiStatsDevWriteGreater1MBs_Object = MibTableColumn
dptScsiStatsDevWriteGreater1MBs = _DptScsiStatsDevWriteGreater1MBs_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 6, 3, 1, 25),
    _DptScsiStatsDevWriteGreater1MBs_Type()
)
dptScsiStatsDevWriteGreater1MBs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiStatsDevWriteGreater1MBs.setStatus("mandatory")
_DptScsiEvent_ObjectIdentity = ObjectIdentity
dptScsiEvent = _DptScsiEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1597, 1, 7)
)


class _DptScsiEventInfo_Type(DisplayString):
    """Custom type dptScsiEventInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_DptScsiEventInfo_Type.__name__ = "DisplayString"
_DptScsiEventInfo_Object = MibScalar
dptScsiEventInfo = _DptScsiEventInfo_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 7, 1),
    _DptScsiEventInfo_Type()
)
dptScsiEventInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dptScsiEventInfo.setStatus("mandatory")
_DptScsiEventAuxVoltage_Type = LowHighStatus
_DptScsiEventAuxVoltage_Object = MibScalar
dptScsiEventAuxVoltage = _DptScsiEventAuxVoltage_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 7, 2),
    _DptScsiEventAuxVoltage_Type()
)
dptScsiEventAuxVoltage.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dptScsiEventAuxVoltage.setStatus("mandatory")
_DptScsiDummy_ObjectIdentity = ObjectIdentity
dptScsiDummy = _DptScsiDummy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1597, 1, 8)
)


class _DptScsiHbaNumberMember_Type(Integer32):
    """Custom type dptScsiHbaNumberMember based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DptScsiHbaNumberMember_Type.__name__ = "Integer32"
_DptScsiHbaNumberMember_Object = MibScalar
dptScsiHbaNumberMember = _DptScsiHbaNumberMember_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 8, 1),
    _DptScsiHbaNumberMember_Type()
)
dptScsiHbaNumberMember.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dptScsiHbaNumberMember.setStatus("mandatory")


class _DptScsiBusNumberMember_Type(Integer32):
    """Custom type dptScsiBusNumberMember based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DptScsiBusNumberMember_Type.__name__ = "Integer32"
_DptScsiBusNumberMember_Object = MibScalar
dptScsiBusNumberMember = _DptScsiBusNumberMember_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 8, 2),
    _DptScsiBusNumberMember_Type()
)
dptScsiBusNumberMember.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dptScsiBusNumberMember.setStatus("mandatory")


class _DptScsiDevIdMember_Type(Integer32):
    """Custom type dptScsiDevIdMember based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_DptScsiDevIdMember_Type.__name__ = "Integer32"
_DptScsiDevIdMember_Object = MibScalar
dptScsiDevIdMember = _DptScsiDevIdMember_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 8, 3),
    _DptScsiDevIdMember_Type()
)
dptScsiDevIdMember.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dptScsiDevIdMember.setStatus("mandatory")


class _DptScsiDevLunMember_Type(Integer32):
    """Custom type dptScsiDevLunMember based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DptScsiDevLunMember_Type.__name__ = "Integer32"
_DptScsiDevLunMember_Object = MibScalar
dptScsiDevLunMember = _DptScsiDevLunMember_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 8, 4),
    _DptScsiDevLunMember_Type()
)
dptScsiDevLunMember.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dptScsiDevLunMember.setStatus("mandatory")


class _DptScsiDevLevelMember_Type(Integer32):
    """Custom type dptScsiDevLevelMember based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_DptScsiDevLevelMember_Type.__name__ = "Integer32"
_DptScsiDevLevelMember_Object = MibScalar
dptScsiDevLevelMember = _DptScsiDevLevelMember_Object(
    (1, 3, 6, 1, 4, 1, 1597, 1, 8, 5),
    _DptScsiDevLevelMember_Type()
)
dptScsiDevLevelMember.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dptScsiDevLevelMember.setStatus("mandatory")

# Managed Objects groups


# Notification objects

dptOtherTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1597, 0, 14)
)
dptOtherTrap.setObjects(
    ("DPT-SCSI-MIB", "dptScsiEventInfo")
)
if mibBuilder.loadTexts:
    dptOtherTrap.setStatus(
        ""
    )

dptHbaVoltageNormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1597, 0, 100)
)
dptHbaVoltageNormalTrap.setObjects(
      *(("DPT-SCSI-MIB", "dptScsiHbaVoltage"),
        ("DPT-SCSI-MIB", "dptScsiHbaNumber"))
)
if mibBuilder.loadTexts:
    dptHbaVoltageNormalTrap.setStatus(
        ""
    )

dptHbaTemperatureNormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1597, 0, 101)
)
dptHbaTemperatureNormalTrap.setObjects(
      *(("DPT-SCSI-MIB", "dptScsiHbaTemperature"),
        ("DPT-SCSI-MIB", "dptScsiHbaNumber"))
)
if mibBuilder.loadTexts:
    dptHbaTemperatureNormalTrap.setStatus(
        ""
    )

dptHbaEccRAMErrorNotFoundTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1597, 0, 102)
)
dptHbaEccRAMErrorNotFoundTrap.setObjects(
      *(("DPT-SCSI-MIB", "dptScsiHbaBadMemoryAddress"),
        ("DPT-SCSI-MIB", "dptScsiHbaNumber"))
)
if mibBuilder.loadTexts:
    dptHbaEccRAMErrorNotFoundTrap.setStatus(
        ""
    )

dptDevStatusChangedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1597, 0, 103)
)
dptDevStatusChangedTrap.setObjects(
      *(("DPT-SCSI-MIB", "dptScsiDevStatus"),
        ("DPT-SCSI-MIB", "dptScsiHbaNumber"),
        ("DPT-SCSI-MIB", "dptScsiBusNumber"),
        ("DPT-SCSI-MIB", "dptScsiDevId"),
        ("DPT-SCSI-MIB", "dptScsiDevLun"),
        ("DPT-SCSI-MIB", "dptScsiDevLevel"))
)
if mibBuilder.loadTexts:
    dptDevStatusChangedTrap.setStatus(
        ""
    )

dptDevReqSenseTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1597, 0, 104)
)
dptDevReqSenseTrap.setObjects(
      *(("DPT-SCSI-MIB", "dptScsiDevLastReqSenseInfo"),
        ("DPT-SCSI-MIB", "dptScsiHbaNumber"),
        ("DPT-SCSI-MIB", "dptScsiBusNumber"),
        ("DPT-SCSI-MIB", "dptScsiDevId"),
        ("DPT-SCSI-MIB", "dptScsiDevLun"),
        ("DPT-SCSI-MIB", "dptScsiDevLevel"))
)
if mibBuilder.loadTexts:
    dptDevReqSenseTrap.setStatus(
        ""
    )

dptArrayChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1597, 0, 105)
)
dptArrayChangeTrap.setObjects(
      *(("DPT-SCSI-MIB", "dptScsiHbaNumber"),
        ("DPT-SCSI-MIB", "dptScsiBusNumber"),
        ("DPT-SCSI-MIB", "dptScsiDevId"),
        ("DPT-SCSI-MIB", "dptScsiDevLun"),
        ("DPT-SCSI-MIB", "dptScsiDevLevel"))
)
if mibBuilder.loadTexts:
    dptArrayChangeTrap.setStatus(
        ""
    )

dptBatteryChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1597, 0, 106)
)
dptBatteryChangeTrap.setObjects(
      *(("DPT-SCSI-MIB", "dptScsiHbaNumber"),
        ("DPT-SCSI-MIB", "dptScsiHbaBatteryStatus"))
)
if mibBuilder.loadTexts:
    dptBatteryChangeTrap.setStatus(
        ""
    )

dptHbaAuxVoltageNormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1597, 0, 107)
)
dptHbaAuxVoltageNormalTrap.setObjects(
      *(("DPT-SCSI-MIB", "dptScsiEventAuxVoltage"),
        ("DPT-SCSI-MIB", "dptScsiHbaNumber"))
)
if mibBuilder.loadTexts:
    dptHbaAuxVoltageNormalTrap.setStatus(
        ""
    )

dptHbaEccRAMErrorCorrectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1597, 0, 200)
)
dptHbaEccRAMErrorCorrectedTrap.setObjects(
      *(("DPT-SCSI-MIB", "dptScsiHbaBadMemoryAddress"),
        ("DPT-SCSI-MIB", "dptScsiHbaNumber"))
)
if mibBuilder.loadTexts:
    dptHbaEccRAMErrorCorrectedTrap.setStatus(
        ""
    )

dptDevBlockReassignedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1597, 0, 201)
)
dptDevBlockReassignedTrap.setObjects(
      *(("DPT-SCSI-MIB", "dptScsiDevBadBlockNumber"),
        ("DPT-SCSI-MIB", "dptScsiHbaNumber"),
        ("DPT-SCSI-MIB", "dptScsiBusNumber"),
        ("DPT-SCSI-MIB", "dptScsiDevId"),
        ("DPT-SCSI-MIB", "dptScsiDevLun"),
        ("DPT-SCSI-MIB", "dptScsiDevLevel"))
)
if mibBuilder.loadTexts:
    dptDevBlockReassignedTrap.setStatus(
        ""
    )

dptDevReqSenseErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1597, 0, 202)
)
dptDevReqSenseErrorTrap.setObjects(
      *(("DPT-SCSI-MIB", "dptScsiDevLastReqSenseInfo"),
        ("DPT-SCSI-MIB", "dptScsiHbaNumber"),
        ("DPT-SCSI-MIB", "dptScsiBusNumber"),
        ("DPT-SCSI-MIB", "dptScsiDevId"),
        ("DPT-SCSI-MIB", "dptScsiDevLun"),
        ("DPT-SCSI-MIB", "dptScsiDevLevel"))
)
if mibBuilder.loadTexts:
    dptDevReqSenseErrorTrap.setStatus(
        ""
    )

dptHbaVoltageChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1597, 0, 300)
)
dptHbaVoltageChangeTrap.setObjects(
      *(("DPT-SCSI-MIB", "dptScsiHbaVoltage"),
        ("DPT-SCSI-MIB", "dptScsiHbaNumber"))
)
if mibBuilder.loadTexts:
    dptHbaVoltageChangeTrap.setStatus(
        ""
    )

dptHbaTemperatureHighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1597, 0, 301)
)
dptHbaTemperatureHighTrap.setObjects(
      *(("DPT-SCSI-MIB", "dptScsiHbaTemperature"),
        ("DPT-SCSI-MIB", "dptScsiHbaNumber"))
)
if mibBuilder.loadTexts:
    dptHbaTemperatureHighTrap.setStatus(
        ""
    )

dptHbaEccRAMErrorUncorrectableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1597, 0, 302)
)
dptHbaEccRAMErrorUncorrectableTrap.setObjects(
      *(("DPT-SCSI-MIB", "dptScsiHbaBadMemoryAddress"),
        ("DPT-SCSI-MIB", "dptScsiHbaNumber"))
)
if mibBuilder.loadTexts:
    dptHbaEccRAMErrorUncorrectableTrap.setStatus(
        ""
    )

dptArrayStatusChangeDegradedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1597, 0, 303)
)
dptArrayStatusChangeDegradedTrap.setObjects(
      *(("DPT-SCSI-MIB", "dptScsiDevStatus"),
        ("DPT-SCSI-MIB", "dptScsiHbaNumber"),
        ("DPT-SCSI-MIB", "dptScsiBusNumber"),
        ("DPT-SCSI-MIB", "dptScsiDevId"),
        ("DPT-SCSI-MIB", "dptScsiDevLun"),
        ("DPT-SCSI-MIB", "dptScsiDevLevel"))
)
if mibBuilder.loadTexts:
    dptArrayStatusChangeDegradedTrap.setStatus(
        ""
    )

dptDevReqSenseSeriousErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1597, 0, 304)
)
dptDevReqSenseSeriousErrorTrap.setObjects(
      *(("DPT-SCSI-MIB", "dptScsiDevLastReqSenseInfo"),
        ("DPT-SCSI-MIB", "dptScsiHbaNumber"),
        ("DPT-SCSI-MIB", "dptScsiBusNumber"),
        ("DPT-SCSI-MIB", "dptScsiDevId"),
        ("DPT-SCSI-MIB", "dptScsiDevLun"),
        ("DPT-SCSI-MIB", "dptScsiDevLevel"))
)
if mibBuilder.loadTexts:
    dptDevReqSenseSeriousErrorTrap.setStatus(
        ""
    )

dptDevArrayDataInconsistencyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1597, 0, 305)
)
dptDevArrayDataInconsistencyTrap.setObjects(
      *(("DPT-SCSI-MIB", "dptScsiDevBadBlockNumber"),
        ("DPT-SCSI-MIB", "dptScsiDevBadBlockCount"),
        ("DPT-SCSI-MIB", "dptScsiHbaNumber"),
        ("DPT-SCSI-MIB", "dptScsiBusNumber"),
        ("DPT-SCSI-MIB", "dptScsiDevId"),
        ("DPT-SCSI-MIB", "dptScsiDevLun"),
        ("DPT-SCSI-MIB", "dptScsiDevLevel"))
)
if mibBuilder.loadTexts:
    dptDevArrayDataInconsistencyTrap.setStatus(
        ""
    )

dptHbaErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1597, 0, 306)
)
dptHbaErrorTrap.setObjects(
    ("DPT-SCSI-MIB", "dptScsiHbaNumber")
)
if mibBuilder.loadTexts:
    dptHbaErrorTrap.setStatus(
        ""
    )

dptDevFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1597, 0, 307)
)
dptDevFailedTrap.setObjects(
      *(("DPT-SCSI-MIB", "dptScsiHbaNumber"),
        ("DPT-SCSI-MIB", "dptScsiBusNumber"),
        ("DPT-SCSI-MIB", "dptScsiDevId"),
        ("DPT-SCSI-MIB", "dptScsiDevLun"),
        ("DPT-SCSI-MIB", "dptScsiDevLevel"))
)
if mibBuilder.loadTexts:
    dptDevFailedTrap.setStatus(
        ""
    )

dptDevSmartFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1597, 0, 308)
)
dptDevSmartFailedTrap.setObjects(
      *(("DPT-SCSI-MIB", "dptScsiHbaNumber"),
        ("DPT-SCSI-MIB", "dptScsiBusNumber"),
        ("DPT-SCSI-MIB", "dptScsiDevId"),
        ("DPT-SCSI-MIB", "dptScsiDevLun"),
        ("DPT-SCSI-MIB", "dptScsiDevLevel"))
)
if mibBuilder.loadTexts:
    dptDevSmartFailedTrap.setStatus(
        ""
    )

dptHbaAuxVoltageChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1597, 0, 309)
)
dptHbaAuxVoltageChangeTrap.setObjects(
      *(("DPT-SCSI-MIB", "dptScsiEventAuxVoltage"),
        ("DPT-SCSI-MIB", "dptScsiHbaNumber"))
)
if mibBuilder.loadTexts:
    dptHbaAuxVoltageChangeTrap.setStatus(
        ""
    )

dptHbaTemperatureVeryHighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1597, 0, 400)
)
dptHbaTemperatureVeryHighTrap.setObjects(
      *(("DPT-SCSI-MIB", "dptScsiHbaTemperature"),
        ("DPT-SCSI-MIB", "dptScsiHbaNumber"))
)
if mibBuilder.loadTexts:
    dptHbaTemperatureVeryHighTrap.setStatus(
        ""
    )

dptArrayStatusChangeFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1597, 0, 401)
)
dptArrayStatusChangeFailedTrap.setObjects(
      *(("DPT-SCSI-MIB", "dptScsiDevStatus"),
        ("DPT-SCSI-MIB", "dptScsiHbaNumber"),
        ("DPT-SCSI-MIB", "dptScsiBusNumber"),
        ("DPT-SCSI-MIB", "dptScsiDevId"),
        ("DPT-SCSI-MIB", "dptScsiDevLun"),
        ("DPT-SCSI-MIB", "dptScsiDevLevel"))
)
if mibBuilder.loadTexts:
    dptArrayStatusChangeFailedTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DPT-SCSI-MIB",
    **{"DisplayString": DisplayString,
       "DptSignature": DptSignature,
       "HostBusType": HostBusType,
       "ScsiBusType": ScsiBusType,
       "IrqType": IrqType,
       "DrqNumber": DrqNumber,
       "MemoryBankType": MemoryBankType,
       "MemoryBankSize": MemoryBankSize,
       "CachingModule": CachingModule,
       "RaidModule": RaidModule,
       "BatteryBackupModule": BatteryBackupModule,
       "RaidType": RaidType,
       "SoftwareType": SoftwareType,
       "BusWidth": BusWidth,
       "BusTerminationType": BusTerminationType,
       "ScsiVersion": ScsiVersion,
       "DeviceType": DeviceType,
       "DeviceStatus": DeviceStatus,
       "DeviceWriteMode": DeviceWriteMode,
       "YesNoStatus": YesNoStatus,
       "LowHighStatus": LowHighStatus,
       "BatteryStatus": BatteryStatus,
       "HbaGenStatus": HbaGenStatus,
       "CommandType": CommandType,
       "RowStatus": RowStatus,
       "dpt": dpt,
       "dptOtherTrap": dptOtherTrap,
       "dptHbaVoltageNormalTrap": dptHbaVoltageNormalTrap,
       "dptHbaTemperatureNormalTrap": dptHbaTemperatureNormalTrap,
       "dptHbaEccRAMErrorNotFoundTrap": dptHbaEccRAMErrorNotFoundTrap,
       "dptDevStatusChangedTrap": dptDevStatusChangedTrap,
       "dptDevReqSenseTrap": dptDevReqSenseTrap,
       "dptArrayChangeTrap": dptArrayChangeTrap,
       "dptBatteryChangeTrap": dptBatteryChangeTrap,
       "dptHbaAuxVoltageNormalTrap": dptHbaAuxVoltageNormalTrap,
       "dptHbaEccRAMErrorCorrectedTrap": dptHbaEccRAMErrorCorrectedTrap,
       "dptDevBlockReassignedTrap": dptDevBlockReassignedTrap,
       "dptDevReqSenseErrorTrap": dptDevReqSenseErrorTrap,
       "dptHbaVoltageChangeTrap": dptHbaVoltageChangeTrap,
       "dptHbaTemperatureHighTrap": dptHbaTemperatureHighTrap,
       "dptHbaEccRAMErrorUncorrectableTrap": dptHbaEccRAMErrorUncorrectableTrap,
       "dptArrayStatusChangeDegradedTrap": dptArrayStatusChangeDegradedTrap,
       "dptDevReqSenseSeriousErrorTrap": dptDevReqSenseSeriousErrorTrap,
       "dptDevArrayDataInconsistencyTrap": dptDevArrayDataInconsistencyTrap,
       "dptHbaErrorTrap": dptHbaErrorTrap,
       "dptDevFailedTrap": dptDevFailedTrap,
       "dptDevSmartFailedTrap": dptDevSmartFailedTrap,
       "dptHbaAuxVoltageChangeTrap": dptHbaAuxVoltageChangeTrap,
       "dptHbaTemperatureVeryHighTrap": dptHbaTemperatureVeryHighTrap,
       "dptArrayStatusChangeFailedTrap": dptArrayStatusChangeFailedTrap,
       "dptScsi": dptScsi,
       "dptScsiSys": dptScsiSys,
       "dptScsiSysRevLevel": dptScsiSysRevLevel,
       "dptScsiSysEngineSignature": dptScsiSysEngineSignature,
       "dptScsiSysDriverSignature": dptScsiSysDriverSignature,
       "dptScsiSysEventLoggerSignature": dptScsiSysEventLoggerSignature,
       "dptScsiSysMibRevMajor": dptScsiSysMibRevMajor,
       "dptScsiSysMibRevMinor": dptScsiSysMibRevMinor,
       "dptScsiHba": dptScsiHba,
       "dptScsiHbaTable": dptScsiHbaTable,
       "dptScsiHbaEntry": dptScsiHbaEntry,
       "dptScsiHbaNumber": dptScsiHbaNumber,
       "dptScsiHbaVendor": dptScsiHbaVendor,
       "dptScsiHbaModel": dptScsiHbaModel,
       "dptScsiHbaFirmware": dptScsiHbaFirmware,
       "dptScsiHbaSerialNumber": dptScsiHbaSerialNumber,
       "dptScsiHbaAddress": dptScsiHbaAddress,
       "dptScsiHbaHostBusType": dptScsiHbaHostBusType,
       "dptScsiHbaHostBusMaxTransferRate": dptScsiHbaHostBusMaxTransferRate,
       "dptScsiHbaIrq": dptScsiHbaIrq,
       "dptScsiHbaIrqType": dptScsiHbaIrqType,
       "dptScsiHbaDrq": dptScsiHbaDrq,
       "dptScsiHbaRaidModule": dptScsiHbaRaidModule,
       "dptScsiHbaCachingModule": dptScsiHbaCachingModule,
       "dptScsiHbaAudibleAlarmOn": dptScsiHbaAudibleAlarmOn,
       "dptScsiHbaUpTime": dptScsiHbaUpTime,
       "dptScsiHbaEccEnabled": dptScsiHbaEccEnabled,
       "dptScsiHbaBackgroundTaskPriority": dptScsiHbaBackgroundTaskPriority,
       "dptScsiHbaExclusionPeriodEnabled": dptScsiHbaExclusionPeriodEnabled,
       "dptScsiHbaExclusionPeriodStart": dptScsiHbaExclusionPeriodStart,
       "dptScsiHbaExclusionPeriodEnd": dptScsiHbaExclusionPeriodEnd,
       "dptScsiHbaMaxReadAheadPercentage": dptScsiHbaMaxReadAheadPercentage,
       "dptScsiHbaMaxDirtyPagesPercentage": dptScsiHbaMaxDirtyPagesPercentage,
       "dptScsiHbaWriteBackDelay": dptScsiHbaWriteBackDelay,
       "dptScsiHbaTemperature": dptScsiHbaTemperature,
       "dptScsiHbaVoltage": dptScsiHbaVoltage,
       "dptScsiHbaBadMemoryAddress": dptScsiHbaBadMemoryAddress,
       "dptScsiHbaBatteryModule": dptScsiHbaBatteryModule,
       "dptScsiHbaBatteryStatus": dptScsiHbaBatteryStatus,
       "dptScsiHbaHighestBusWithDevices": dptScsiHbaHighestBusWithDevices,
       "dptScsiHbaGeneralStatus": dptScsiHbaGeneralStatus,
       "dptScsiHbaSmorSignature": dptScsiHbaSmorSignature,
       "dptScsiHbaBiosSignature": dptScsiHbaBiosSignature,
       "dptScsiHbaNvramLayout": dptScsiHbaNvramLayout,
       "dptScsiHbaCacheSocketTable": dptScsiHbaCacheSocketTable,
       "dptScsiHbaCacheSocketEntry": dptScsiHbaCacheSocketEntry,
       "dptScsiHbaCacheSocketNumber": dptScsiHbaCacheSocketNumber,
       "dptScsiHbaCacheModuleType": dptScsiHbaCacheModuleType,
       "dptScsiHbaCacheModuleSize": dptScsiHbaCacheModuleSize,
       "dptScsiBus": dptScsiBus,
       "dptScsiBusTable": dptScsiBusTable,
       "dptScsiBusEntry": dptScsiBusEntry,
       "dptScsiBusNumber": dptScsiBusNumber,
       "dptScsiBusWidth": dptScsiBusWidth,
       "dptScsiBusType": dptScsiBusType,
       "dptScsiBusMaxTransferRate": dptScsiBusMaxTransferRate,
       "dptScsiBusHbaScsiId": dptScsiBusHbaScsiId,
       "dptScsiBusHbaTermPower": dptScsiBusHbaTermPower,
       "dptScsiBusHbaTermination": dptScsiBusHbaTermination,
       "dptScsiDev": dptScsiDev,
       "dptScsiDevTable": dptScsiDevTable,
       "dptScsiDevEntry": dptScsiDevEntry,
       "dptScsiDevId": dptScsiDevId,
       "dptScsiDevLun": dptScsiDevLun,
       "dptScsiDevLevel": dptScsiDevLevel,
       "dptScsiDevVendor": dptScsiDevVendor,
       "dptScsiDevModel": dptScsiDevModel,
       "dptScsiDevRevision": dptScsiDevRevision,
       "dptScsiDevSerialNumber": dptScsiDevSerialNumber,
       "dptScsiDevStatus": dptScsiDevStatus,
       "dptScsiDevBusWidth": dptScsiDevBusWidth,
       "dptScsiDevCapacity": dptScsiDevCapacity,
       "dptScsiDevLogicalBlockSize": dptScsiDevLogicalBlockSize,
       "dptScsiDevPhysicalBlockSize": dptScsiDevPhysicalBlockSize,
       "dptScsiDevNegTransferRate": dptScsiDevNegTransferRate,
       "dptScsiDevRemovable": dptScsiDevRemovable,
       "dptScsiDevEccEnabled": dptScsiDevEccEnabled,
       "dptScsiDevScsiVersion": dptScsiDevScsiVersion,
       "dptScsiDevSoftReset": dptScsiDevSoftReset,
       "dptScsiDevCmdQueuing": dptScsiDevCmdQueuing,
       "dptScsiDevLinkedCmds": dptScsiDevLinkedCmds,
       "dptScsiDevSynchronous": dptScsiDevSynchronous,
       "dptScsiDevRelAddr": dptScsiDevRelAddr,
       "dptScsiDevSMART": dptScsiDevSMART,
       "dptScsiDevSCAM": dptScsiDevSCAM,
       "dptScsiDevBadBlockNumber": dptScsiDevBadBlockNumber,
       "dptScsiDevBadBlockCount": dptScsiDevBadBlockCount,
       "dptScsiDevErrorsAboveThreshold": dptScsiDevErrorsAboveThreshold,
       "dptScsiDevDriveLockingOn": dptScsiDevDriveLockingOn,
       "dptScsiDevLastReqSenseInfo": dptScsiDevLastReqSenseInfo,
       "dptScsiDevReadCachingOn": dptScsiDevReadCachingOn,
       "dptScsiDevReadCacheMaxRecord": dptScsiDevReadCacheMaxRecord,
       "dptScsiDevWriteCachingOn": dptScsiDevWriteCachingOn,
       "dptScsiDevWriteCacheMaxRecord": dptScsiDevWriteCacheMaxRecord,
       "dptScsiDevWriteMode": dptScsiDevWriteMode,
       "dptScsiDevSmartStatusOk": dptScsiDevSmartStatusOk,
       "dptScsiDevType": dptScsiDevType,
       "dptScsiArr": dptScsiArr,
       "dptScsiArrTable": dptScsiArrTable,
       "dptScsiArrEntry": dptScsiArrEntry,
       "dptScsiArrType": dptScsiArrType,
       "dptScsiArrOwner": dptScsiArrOwner,
       "dptScsiArrName": dptScsiArrName,
       "dptScsiArrBackgroundProgress": dptScsiArrBackgroundProgress,
       "dptScsiArrEntryStatus": dptScsiArrEntryStatus,
       "dptScsiArrMemberTable": dptScsiArrMemberTable,
       "dptScsiArrMemberEntry": dptScsiArrMemberEntry,
       "dptScsiArrMemberStripeSize": dptScsiArrMemberStripeSize,
       "dptScsiArrMemberEntryStatus": dptScsiArrMemberEntryStatus,
       "dptScsiStats": dptScsiStats,
       "dptScsiStatsHbaTable": dptScsiStatsHbaTable,
       "dptScsiStatsHbaEntry": dptScsiStatsHbaEntry,
       "dptScsiStatsHbaCacheTotalPages": dptScsiStatsHbaCacheTotalPages,
       "dptScsiStatsHbaCacheUsedPages": dptScsiStatsHbaCacheUsedPages,
       "dptScsiStatsHbaCacheDirtyPages": dptScsiStatsHbaCacheDirtyPages,
       "dptScsiStatsHbaCacheReadAheadPages": dptScsiStatsHbaCacheReadAheadPages,
       "dptScsiStatsHbaCacheLockedPages": dptScsiStatsHbaCacheLockedPages,
       "dptScsiStatsHbaCacheEccFaultPages": dptScsiStatsHbaCacheEccFaultPages,
       "dptScsiStatsHbaCommands": dptScsiStatsHbaCommands,
       "dptScsiStatsHbaMisAlignedTransfers": dptScsiStatsHbaMisAlignedTransfers,
       "dptScsiStatsHbaScsiResets": dptScsiStatsHbaScsiResets,
       "dptScsiStatsDevTable": dptScsiStatsDevTable,
       "dptScsiStatsDevEntry": dptScsiStatsDevEntry,
       "dptScsiStatsDevReadTotalSectors": dptScsiStatsDevReadTotalSectors,
       "dptScsiStatsDevReadCacheHits": dptScsiStatsDevReadCacheHits,
       "dptScsiStatsDevReadAheadHits": dptScsiStatsDevReadAheadHits,
       "dptScsiStatsDevWriteTotalSectors": dptScsiStatsDevWriteTotalSectors,
       "dptScsiStatsDevWriteCacheHits": dptScsiStatsDevWriteCacheHits,
       "dptScsiStatsDevWriteBacks": dptScsiStatsDevWriteBacks,
       "dptScsiStatsDevStripesCrosseds": dptScsiStatsDevStripesCrosseds,
       "dptScsiStatsDevRWCmdsTable": dptScsiStatsDevRWCmdsTable,
       "dptScsiStatsDevRWCmdsEntry": dptScsiStatsDevRWCmdsEntry,
       "dptScsiStatsDevRWCmdsType": dptScsiStatsDevRWCmdsType,
       "dptScsiStatsDevRead1Ks": dptScsiStatsDevRead1Ks,
       "dptScsiStatsDevRead2Ks": dptScsiStatsDevRead2Ks,
       "dptScsiStatsDevRead4Ks": dptScsiStatsDevRead4Ks,
       "dptScsiStatsDevRead8Ks": dptScsiStatsDevRead8Ks,
       "dptScsiStatsDevRead16Ks": dptScsiStatsDevRead16Ks,
       "dptScsiStatsDevRead32Ks": dptScsiStatsDevRead32Ks,
       "dptScsiStatsDevRead64Ks": dptScsiStatsDevRead64Ks,
       "dptScsiStatsDevRead128Ks": dptScsiStatsDevRead128Ks,
       "dptScsiStatsDevRead256Ks": dptScsiStatsDevRead256Ks,
       "dptScsiStatsDevRead512Ks": dptScsiStatsDevRead512Ks,
       "dptScsiStatsDevRead1MBs": dptScsiStatsDevRead1MBs,
       "dptScsiStatsDevReadGreater1MBs": dptScsiStatsDevReadGreater1MBs,
       "dptScsiStatsDevWrite1Ks": dptScsiStatsDevWrite1Ks,
       "dptScsiStatsDevWrite2Ks": dptScsiStatsDevWrite2Ks,
       "dptScsiStatsDevWrite4Ks": dptScsiStatsDevWrite4Ks,
       "dptScsiStatsDevWrite8Ks": dptScsiStatsDevWrite8Ks,
       "dptScsiStatsDevWrite16Ks": dptScsiStatsDevWrite16Ks,
       "dptScsiStatsDevWrite32Ks": dptScsiStatsDevWrite32Ks,
       "dptScsiStatsDevWrite64Ks": dptScsiStatsDevWrite64Ks,
       "dptScsiStatsDevWrite128Ks": dptScsiStatsDevWrite128Ks,
       "dptScsiStatsDevWrite256Ks": dptScsiStatsDevWrite256Ks,
       "dptScsiStatsDevWrite512Ks": dptScsiStatsDevWrite512Ks,
       "dptScsiStatsDevWrite1MBs": dptScsiStatsDevWrite1MBs,
       "dptScsiStatsDevWriteGreater1MBs": dptScsiStatsDevWriteGreater1MBs,
       "dptScsiEvent": dptScsiEvent,
       "dptScsiEventInfo": dptScsiEventInfo,
       "dptScsiEventAuxVoltage": dptScsiEventAuxVoltage,
       "dptScsiDummy": dptScsiDummy,
       "dptScsiHbaNumberMember": dptScsiHbaNumberMember,
       "dptScsiBusNumberMember": dptScsiBusNumberMember,
       "dptScsiDevIdMember": dptScsiDevIdMember,
       "dptScsiDevLunMember": dptScsiDevLunMember,
       "dptScsiDevLevelMember": dptScsiDevLevelMember}
)
