# SNMP MIB module (ACD-DESC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACD-DESC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:33:18 2024
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

(acdProducts,) = mibBuilder.importSymbols(
    "ACCEDIAN-SMI",
    "acdProducts")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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
 MacAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

acdDesc = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 1, 1)
)
acdDesc.setRevisions(
        ("2010-11-10 01:00",
         "2010-06-30 01:00",
         "2009-02-04 01:00",
         "2008-12-01 01:00",
         "2006-08-06 01:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AcdDescNotifications_ObjectIdentity = ObjectIdentity
acdDescNotifications = _AcdDescNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 1, 1, 0)
)
_AcdDescCommercialName_Type = DisplayString
_AcdDescCommercialName_Object = MibScalar
acdDescCommercialName = _AcdDescCommercialName_Object(
    (1, 3, 6, 1, 4, 1, 22420, 1, 1, 1),
    _AcdDescCommercialName_Type()
)
acdDescCommercialName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdDescCommercialName.setStatus("current")
_AcdDescMacBaseAddr_Type = MacAddress
_AcdDescMacBaseAddr_Object = MibScalar
acdDescMacBaseAddr = _AcdDescMacBaseAddr_Object(
    (1, 3, 6, 1, 4, 1, 22420, 1, 1, 2),
    _AcdDescMacBaseAddr_Type()
)
acdDescMacBaseAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdDescMacBaseAddr.setStatus("current")
_AcdDescIdentifier_Type = DisplayString
_AcdDescIdentifier_Object = MibScalar
acdDescIdentifier = _AcdDescIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 22420, 1, 1, 3),
    _AcdDescIdentifier_Type()
)
acdDescIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdDescIdentifier.setStatus("current")
_AcdDescFirmwareVersion_Type = DisplayString
_AcdDescFirmwareVersion_Object = MibScalar
acdDescFirmwareVersion = _AcdDescFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 22420, 1, 1, 4),
    _AcdDescFirmwareVersion_Type()
)
acdDescFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdDescFirmwareVersion.setStatus("current")
_AcdDescHardwareVersion_Type = DisplayString
_AcdDescHardwareVersion_Object = MibScalar
acdDescHardwareVersion = _AcdDescHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 22420, 1, 1, 5),
    _AcdDescHardwareVersion_Type()
)
acdDescHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdDescHardwareVersion.setStatus("current")
_AcdDescSerialNumber_Type = DisplayString
_AcdDescSerialNumber_Object = MibScalar
acdDescSerialNumber = _AcdDescSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 22420, 1, 1, 6),
    _AcdDescSerialNumber_Type()
)
acdDescSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdDescSerialNumber.setStatus("current")
_AcdDescConnectorTable_Object = MibTable
acdDescConnectorTable = _AcdDescConnectorTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 1, 1, 10)
)
if mibBuilder.loadTexts:
    acdDescConnectorTable.setStatus("current")
_AcdDescConnectorEntry_Object = MibTableRow
acdDescConnectorEntry = _AcdDescConnectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 1, 1, 10, 1)
)
acdDescConnectorEntry.setIndexNames(
    (0, "ACD-DESC-MIB", "acdDescConnectorID"),
)
if mibBuilder.loadTexts:
    acdDescConnectorEntry.setStatus("current")


class _AcdDescConnectorID_Type(Unsigned32):
    """Custom type acdDescConnectorID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_AcdDescConnectorID_Type.__name__ = "Unsigned32"
_AcdDescConnectorID_Object = MibTableColumn
acdDescConnectorID = _AcdDescConnectorID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 1, 1, 10, 1, 1),
    _AcdDescConnectorID_Type()
)
acdDescConnectorID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdDescConnectorID.setStatus("current")
_AcdDescConnectorName_Type = DisplayString
_AcdDescConnectorName_Object = MibTableColumn
acdDescConnectorName = _AcdDescConnectorName_Object(
    (1, 3, 6, 1, 4, 1, 22420, 1, 1, 10, 1, 2),
    _AcdDescConnectorName_Type()
)
acdDescConnectorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdDescConnectorName.setStatus("current")


class _AcdDescConnectorType_Type(Integer32):
    """Custom type acdDescConnectorType based on Integer32"""
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
        *(("bnc", 5),
          ("db9", 4),
          ("fAUI", 6),
          ("fiberLC", 14),
          ("fiberMIC", 9),
          ("fiberSC", 8),
          ("fiberST", 10),
          ("hssdc", 13),
          ("mAUI", 7),
          ("mtrj", 12),
          ("other", 1),
          ("rj45", 2),
          ("rj45S", 3),
          ("telco", 11))
    )


_AcdDescConnectorType_Type.__name__ = "Integer32"
_AcdDescConnectorType_Object = MibTableColumn
acdDescConnectorType = _AcdDescConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 22420, 1, 1, 10, 1, 3),
    _AcdDescConnectorType_Type()
)
acdDescConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdDescConnectorType.setStatus("current")
_AcdDescConnectorPoESupport_Type = TruthValue
_AcdDescConnectorPoESupport_Object = MibTableColumn
acdDescConnectorPoESupport = _AcdDescConnectorPoESupport_Object(
    (1, 3, 6, 1, 4, 1, 22420, 1, 1, 10, 1, 4),
    _AcdDescConnectorPoESupport_Type()
)
acdDescConnectorPoESupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdDescConnectorPoESupport.setStatus("current")
_AcdDescPwrTable_Object = MibTable
acdDescPwrTable = _AcdDescPwrTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 1, 1, 11)
)
if mibBuilder.loadTexts:
    acdDescPwrTable.setStatus("current")
_AcdDescPwrEntry_Object = MibTableRow
acdDescPwrEntry = _AcdDescPwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 1, 1, 11, 1)
)
acdDescPwrEntry.setIndexNames(
    (0, "ACD-DESC-MIB", "acdDescPwrID"),
)
if mibBuilder.loadTexts:
    acdDescPwrEntry.setStatus("current")


class _AcdDescPwrID_Type(Unsigned32):
    """Custom type acdDescPwrID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_AcdDescPwrID_Type.__name__ = "Unsigned32"
_AcdDescPwrID_Object = MibTableColumn
acdDescPwrID = _AcdDescPwrID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 1, 1, 11, 1, 1),
    _AcdDescPwrID_Type()
)
acdDescPwrID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdDescPwrID.setStatus("current")
_AcdDescPwrName_Type = DisplayString
_AcdDescPwrName_Object = MibTableColumn
acdDescPwrName = _AcdDescPwrName_Object(
    (1, 3, 6, 1, 4, 1, 22420, 1, 1, 11, 1, 2),
    _AcdDescPwrName_Type()
)
acdDescPwrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdDescPwrName.setStatus("current")


class _AcdDescPwrType_Type(Integer32):
    """Custom type acdDescPwrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pwrminus48volts", 2),
          ("pwrplus5volts", 1))
    )


_AcdDescPwrType_Type.__name__ = "Integer32"
_AcdDescPwrType_Object = MibTableColumn
acdDescPwrType = _AcdDescPwrType_Object(
    (1, 3, 6, 1, 4, 1, 22420, 1, 1, 11, 1, 3),
    _AcdDescPwrType_Type()
)
acdDescPwrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdDescPwrType.setStatus("current")
_AcdDescPwrPresent_Type = TruthValue
_AcdDescPwrPresent_Object = MibTableColumn
acdDescPwrPresent = _AcdDescPwrPresent_Object(
    (1, 3, 6, 1, 4, 1, 22420, 1, 1, 11, 1, 4),
    _AcdDescPwrPresent_Type()
)
acdDescPwrPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdDescPwrPresent.setStatus("current")
_AcdDescTsTable_Object = MibTable
acdDescTsTable = _AcdDescTsTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 1, 1, 12)
)
if mibBuilder.loadTexts:
    acdDescTsTable.setStatus("current")
_AcdDescTsEntry_Object = MibTableRow
acdDescTsEntry = _AcdDescTsEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 1, 1, 12, 1)
)
acdDescTsEntry.setIndexNames(
    (0, "ACD-DESC-MIB", "acdDescTsID"),
)
if mibBuilder.loadTexts:
    acdDescTsEntry.setStatus("current")


class _AcdDescTsID_Type(Unsigned32):
    """Custom type acdDescTsID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_AcdDescTsID_Type.__name__ = "Unsigned32"
_AcdDescTsID_Object = MibTableColumn
acdDescTsID = _AcdDescTsID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 1, 1, 12, 1, 1),
    _AcdDescTsID_Type()
)
acdDescTsID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdDescTsID.setStatus("current")
_AcdDescTsCurrentTemp_Type = Integer32
_AcdDescTsCurrentTemp_Object = MibTableColumn
acdDescTsCurrentTemp = _AcdDescTsCurrentTemp_Object(
    (1, 3, 6, 1, 4, 1, 22420, 1, 1, 12, 1, 2),
    _AcdDescTsCurrentTemp_Type()
)
acdDescTsCurrentTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdDescTsCurrentTemp.setStatus("current")
_AcdDescTsFirstThres_Type = Integer32
_AcdDescTsFirstThres_Object = MibTableColumn
acdDescTsFirstThres = _AcdDescTsFirstThres_Object(
    (1, 3, 6, 1, 4, 1, 22420, 1, 1, 12, 1, 3),
    _AcdDescTsFirstThres_Type()
)
acdDescTsFirstThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdDescTsFirstThres.setStatus("current")
_AcdDescTsFisrtThresPass_Type = TruthValue
_AcdDescTsFisrtThresPass_Object = MibTableColumn
acdDescTsFisrtThresPass = _AcdDescTsFisrtThresPass_Object(
    (1, 3, 6, 1, 4, 1, 22420, 1, 1, 12, 1, 4),
    _AcdDescTsFisrtThresPass_Type()
)
acdDescTsFisrtThresPass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdDescTsFisrtThresPass.setStatus("current")
_AcdDescTsSecondThres_Type = Integer32
_AcdDescTsSecondThres_Object = MibTableColumn
acdDescTsSecondThres = _AcdDescTsSecondThres_Object(
    (1, 3, 6, 1, 4, 1, 22420, 1, 1, 12, 1, 5),
    _AcdDescTsSecondThres_Type()
)
acdDescTsSecondThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdDescTsSecondThres.setStatus("current")
_AcdDescTsSecondThresPass_Type = TruthValue
_AcdDescTsSecondThresPass_Object = MibTableColumn
acdDescTsSecondThresPass = _AcdDescTsSecondThresPass_Object(
    (1, 3, 6, 1, 4, 1, 22420, 1, 1, 12, 1, 6),
    _AcdDescTsSecondThresPass_Type()
)
acdDescTsSecondThresPass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdDescTsSecondThresPass.setStatus("current")
_AcdDescMIBObjects_ObjectIdentity = ObjectIdentity
acdDescMIBObjects = _AcdDescMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 1, 1, 15)
)
_AcdDescConformance_ObjectIdentity = ObjectIdentity
acdDescConformance = _AcdDescConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 1, 1, 15, 1)
)
_AcdDescCompliances_ObjectIdentity = ObjectIdentity
acdDescCompliances = _AcdDescCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 1, 1, 15, 1, 1)
)
_AcdDescGroups_ObjectIdentity = ObjectIdentity
acdDescGroups = _AcdDescGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 1, 1, 15, 1, 2)
)


class _AcdDescCpuUsageCurrent_Type(Gauge32):
    """Custom type acdDescCpuUsageCurrent based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AcdDescCpuUsageCurrent_Type.__name__ = "Gauge32"
_AcdDescCpuUsageCurrent_Object = MibScalar
acdDescCpuUsageCurrent = _AcdDescCpuUsageCurrent_Object(
    (1, 3, 6, 1, 4, 1, 22420, 1, 1, 20),
    _AcdDescCpuUsageCurrent_Type()
)
acdDescCpuUsageCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdDescCpuUsageCurrent.setStatus("current")
if mibBuilder.loadTexts:
    acdDescCpuUsageCurrent.setUnits("percent")


class _AcdDescCpuUsageAverage15_Type(Gauge32):
    """Custom type acdDescCpuUsageAverage15 based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AcdDescCpuUsageAverage15_Type.__name__ = "Gauge32"
_AcdDescCpuUsageAverage15_Object = MibScalar
acdDescCpuUsageAverage15 = _AcdDescCpuUsageAverage15_Object(
    (1, 3, 6, 1, 4, 1, 22420, 1, 1, 21),
    _AcdDescCpuUsageAverage15_Type()
)
acdDescCpuUsageAverage15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdDescCpuUsageAverage15.setStatus("current")
if mibBuilder.loadTexts:
    acdDescCpuUsageAverage15.setUnits("percent")


class _AcdDescCpuUsageAverage30_Type(Gauge32):
    """Custom type acdDescCpuUsageAverage30 based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AcdDescCpuUsageAverage30_Type.__name__ = "Gauge32"
_AcdDescCpuUsageAverage30_Object = MibScalar
acdDescCpuUsageAverage30 = _AcdDescCpuUsageAverage30_Object(
    (1, 3, 6, 1, 4, 1, 22420, 1, 1, 22),
    _AcdDescCpuUsageAverage30_Type()
)
acdDescCpuUsageAverage30.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdDescCpuUsageAverage30.setStatus("current")
if mibBuilder.loadTexts:
    acdDescCpuUsageAverage30.setUnits("percent")


class _AcdDescCpuUsageAverage60_Type(Gauge32):
    """Custom type acdDescCpuUsageAverage60 based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AcdDescCpuUsageAverage60_Type.__name__ = "Gauge32"
_AcdDescCpuUsageAverage60_Object = MibScalar
acdDescCpuUsageAverage60 = _AcdDescCpuUsageAverage60_Object(
    (1, 3, 6, 1, 4, 1, 22420, 1, 1, 23),
    _AcdDescCpuUsageAverage60_Type()
)
acdDescCpuUsageAverage60.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdDescCpuUsageAverage60.setStatus("current")
if mibBuilder.loadTexts:
    acdDescCpuUsageAverage60.setUnits("percent")


class _AcdDescCpuUsageAverage900_Type(Gauge32):
    """Custom type acdDescCpuUsageAverage900 based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AcdDescCpuUsageAverage900_Type.__name__ = "Gauge32"
_AcdDescCpuUsageAverage900_Object = MibScalar
acdDescCpuUsageAverage900 = _AcdDescCpuUsageAverage900_Object(
    (1, 3, 6, 1, 4, 1, 22420, 1, 1, 24),
    _AcdDescCpuUsageAverage900_Type()
)
acdDescCpuUsageAverage900.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdDescCpuUsageAverage900.setStatus("current")
if mibBuilder.loadTexts:
    acdDescCpuUsageAverage900.setUnits("percent")

# Managed Objects groups

acdDescGenGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 1, 1, 15, 1, 2, 1)
)
acdDescGenGroup.setObjects(
      *(("ACD-DESC-MIB", "acdDescCommercialName"),
        ("ACD-DESC-MIB", "acdDescMacBaseAddr"),
        ("ACD-DESC-MIB", "acdDescIdentifier"),
        ("ACD-DESC-MIB", "acdDescFirmwareVersion"),
        ("ACD-DESC-MIB", "acdDescHardwareVersion"),
        ("ACD-DESC-MIB", "acdDescSerialNumber"),
        ("ACD-DESC-MIB", "acdDescCpuUsageCurrent"),
        ("ACD-DESC-MIB", "acdDescCpuUsageAverage15"),
        ("ACD-DESC-MIB", "acdDescCpuUsageAverage30"),
        ("ACD-DESC-MIB", "acdDescCpuUsageAverage60"),
        ("ACD-DESC-MIB", "acdDescCpuUsageAverage900"))
)
if mibBuilder.loadTexts:
    acdDescGenGroup.setStatus("current")

acdDescConnectorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 1, 1, 15, 1, 2, 2)
)
acdDescConnectorGroup.setObjects(
      *(("ACD-DESC-MIB", "acdDescConnectorName"),
        ("ACD-DESC-MIB", "acdDescConnectorType"),
        ("ACD-DESC-MIB", "acdDescConnectorPoESupport"))
)
if mibBuilder.loadTexts:
    acdDescConnectorGroup.setStatus("current")

acdDescPwrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 1, 1, 15, 1, 2, 3)
)
acdDescPwrGroup.setObjects(
      *(("ACD-DESC-MIB", "acdDescPwrName"),
        ("ACD-DESC-MIB", "acdDescPwrType"),
        ("ACD-DESC-MIB", "acdDescPwrPresent"))
)
if mibBuilder.loadTexts:
    acdDescPwrGroup.setStatus("current")

acdDescTsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 1, 1, 15, 1, 2, 4)
)
acdDescTsGroup.setObjects(
      *(("ACD-DESC-MIB", "acdDescTsCurrentTemp"),
        ("ACD-DESC-MIB", "acdDescTsFirstThres"),
        ("ACD-DESC-MIB", "acdDescTsFisrtThresPass"),
        ("ACD-DESC-MIB", "acdDescTsSecondThres"),
        ("ACD-DESC-MIB", "acdDescTsSecondThresPass"))
)
if mibBuilder.loadTexts:
    acdDescTsGroup.setStatus("current")


# Notification objects

acdPowerLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 22420, 1, 1, 0, 1)
)
acdPowerLost.setObjects(
      *(("ACD-DESC-MIB", "acdDescCommercialName"),
        ("ACD-DESC-MIB", "acdDescMacBaseAddr"),
        ("ACD-DESC-MIB", "acdDescIdentifier"),
        ("ACD-DESC-MIB", "acdDescSerialNumber"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    acdPowerLost.setStatus(
        "current"
    )


# Notifications groups

acdDescNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 22420, 1, 1, 15, 1, 2, 5)
)
acdDescNotificationsGroup.setObjects(
    ("ACD-DESC-MIB", "acdPowerLost")
)
if mibBuilder.loadTexts:
    acdDescNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

acdAlarmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 22420, 1, 1, 15, 1, 1, 1)
)
if mibBuilder.loadTexts:
    acdAlarmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACD-DESC-MIB",
    **{"acdDesc": acdDesc,
       "acdDescNotifications": acdDescNotifications,
       "acdPowerLost": acdPowerLost,
       "acdDescCommercialName": acdDescCommercialName,
       "acdDescMacBaseAddr": acdDescMacBaseAddr,
       "acdDescIdentifier": acdDescIdentifier,
       "acdDescFirmwareVersion": acdDescFirmwareVersion,
       "acdDescHardwareVersion": acdDescHardwareVersion,
       "acdDescSerialNumber": acdDescSerialNumber,
       "acdDescConnectorTable": acdDescConnectorTable,
       "acdDescConnectorEntry": acdDescConnectorEntry,
       "acdDescConnectorID": acdDescConnectorID,
       "acdDescConnectorName": acdDescConnectorName,
       "acdDescConnectorType": acdDescConnectorType,
       "acdDescConnectorPoESupport": acdDescConnectorPoESupport,
       "acdDescPwrTable": acdDescPwrTable,
       "acdDescPwrEntry": acdDescPwrEntry,
       "acdDescPwrID": acdDescPwrID,
       "acdDescPwrName": acdDescPwrName,
       "acdDescPwrType": acdDescPwrType,
       "acdDescPwrPresent": acdDescPwrPresent,
       "acdDescTsTable": acdDescTsTable,
       "acdDescTsEntry": acdDescTsEntry,
       "acdDescTsID": acdDescTsID,
       "acdDescTsCurrentTemp": acdDescTsCurrentTemp,
       "acdDescTsFirstThres": acdDescTsFirstThres,
       "acdDescTsFisrtThresPass": acdDescTsFisrtThresPass,
       "acdDescTsSecondThres": acdDescTsSecondThres,
       "acdDescTsSecondThresPass": acdDescTsSecondThresPass,
       "acdDescMIBObjects": acdDescMIBObjects,
       "acdDescConformance": acdDescConformance,
       "acdDescCompliances": acdDescCompliances,
       "acdAlarmCompliance": acdAlarmCompliance,
       "acdDescGroups": acdDescGroups,
       "acdDescGenGroup": acdDescGenGroup,
       "acdDescConnectorGroup": acdDescConnectorGroup,
       "acdDescPwrGroup": acdDescPwrGroup,
       "acdDescTsGroup": acdDescTsGroup,
       "acdDescNotificationsGroup": acdDescNotificationsGroup,
       "acdDescCpuUsageCurrent": acdDescCpuUsageCurrent,
       "acdDescCpuUsageAverage15": acdDescCpuUsageAverage15,
       "acdDescCpuUsageAverage30": acdDescCpuUsageAverage30,
       "acdDescCpuUsageAverage60": acdDescCpuUsageAverage60,
       "acdDescCpuUsageAverage900": acdDescCpuUsageAverage900}
)
