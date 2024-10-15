# SNMP MIB module (DEV-ID-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DEV-ID-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:26:04 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

nbDevId = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 16)
)
nbDevId.setRevisions(
        ("2006-02-22 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Nbase_ObjectIdentity = ObjectIdentity
nbase = _Nbase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629)
)
_NbSwitchG1_ObjectIdentity = ObjectIdentity
nbSwitchG1 = _NbSwitchG1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1)
)
_NbSwitchG1Il_ObjectIdentity = ObjectIdentity
nbSwitchG1Il = _NbSwitchG1Il_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50)
)
_NbDevIdTypeName_Type = DisplayString
_NbDevIdTypeName_Object = MibScalar
nbDevIdTypeName = _NbDevIdTypeName_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 16, 1),
    _NbDevIdTypeName_Type()
)
nbDevIdTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbDevIdTypeName.setStatus("current")


class _NbDevIdSysName_Type(DisplayString):
    """Custom type nbDevIdSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NbDevIdSysName_Type.__name__ = "DisplayString"
_NbDevIdSysName_Object = MibScalar
nbDevIdSysName = _NbDevIdSysName_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 16, 2),
    _NbDevIdSysName_Type()
)
nbDevIdSysName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbDevIdSysName.setStatus("current")


class _NbDevIdBaseMAC_Type(OctetString):
    """Custom type nbDevIdBaseMAC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_NbDevIdBaseMAC_Type.__name__ = "OctetString"
_NbDevIdBaseMAC_Object = MibScalar
nbDevIdBaseMAC = _NbDevIdBaseMAC_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 16, 3),
    _NbDevIdBaseMAC_Type()
)
nbDevIdBaseMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbDevIdBaseMAC.setStatus("current")
_NbDevIdHardware_ObjectIdentity = ObjectIdentity
nbDevIdHardware = _NbDevIdHardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 16, 4)
)
_NbDevIdHardwareVersion_Type = Integer32
_NbDevIdHardwareVersion_Object = MibScalar
nbDevIdHardwareVersion = _NbDevIdHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 16, 4, 2),
    _NbDevIdHardwareVersion_Type()
)
nbDevIdHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbDevIdHardwareVersion.setStatus("current")
_NbDevIdHardwareSerial_ObjectIdentity = ObjectIdentity
nbDevIdHardwareSerial = _NbDevIdHardwareSerial_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 16, 4, 3)
)
_NbDevIdHardwareSerialBoard_Type = DisplayString
_NbDevIdHardwareSerialBoard_Object = MibScalar
nbDevIdHardwareSerialBoard = _NbDevIdHardwareSerialBoard_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 16, 4, 3, 1),
    _NbDevIdHardwareSerialBoard_Type()
)
nbDevIdHardwareSerialBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbDevIdHardwareSerialBoard.setStatus("current")
_NbDevIdHardwareSerialUnit_Type = DisplayString
_NbDevIdHardwareSerialUnit_Object = MibScalar
nbDevIdHardwareSerialUnit = _NbDevIdHardwareSerialUnit_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 16, 4, 3, 2),
    _NbDevIdHardwareSerialUnit_Type()
)
nbDevIdHardwareSerialUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbDevIdHardwareSerialUnit.setStatus("current")
_NbDevIdHardwareCpuNumber_Type = Integer32
_NbDevIdHardwareCpuNumber_Object = MibScalar
nbDevIdHardwareCpuNumber = _NbDevIdHardwareCpuNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 16, 4, 4),
    _NbDevIdHardwareCpuNumber_Type()
)
nbDevIdHardwareCpuNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbDevIdHardwareCpuNumber.setStatus("current")
_NbDevIdCpuTable_Object = MibTable
nbDevIdCpuTable = _NbDevIdCpuTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 16, 4, 5)
)
if mibBuilder.loadTexts:
    nbDevIdCpuTable.setStatus("current")
_NbDevIdCpuEntry_Object = MibTableRow
nbDevIdCpuEntry = _NbDevIdCpuEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 16, 4, 5, 1)
)
nbDevIdCpuEntry.setIndexNames(
    (0, "DEV-ID-MIB", "nbDevIdCpuIndex"),
)
if mibBuilder.loadTexts:
    nbDevIdCpuEntry.setStatus("current")


class _NbDevIdCpuIndex_Type(Integer32):
    """Custom type nbDevIdCpuIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NbDevIdCpuIndex_Type.__name__ = "Integer32"
_NbDevIdCpuIndex_Object = MibTableColumn
nbDevIdCpuIndex = _NbDevIdCpuIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 16, 4, 5, 1, 1),
    _NbDevIdCpuIndex_Type()
)
nbDevIdCpuIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbDevIdCpuIndex.setStatus("current")
_NbDevIdCpuSerial_Type = DisplayString
_NbDevIdCpuSerial_Object = MibTableColumn
nbDevIdCpuSerial = _NbDevIdCpuSerial_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 16, 4, 5, 1, 4),
    _NbDevIdCpuSerial_Type()
)
nbDevIdCpuSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbDevIdCpuSerial.setStatus("current")
_NbDevIdCpuDescr_Type = DisplayString
_NbDevIdCpuDescr_Object = MibTableColumn
nbDevIdCpuDescr = _NbDevIdCpuDescr_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 16, 4, 5, 1, 9),
    _NbDevIdCpuDescr_Type()
)
nbDevIdCpuDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbDevIdCpuDescr.setStatus("current")
_NbDevIdSoftware_ObjectIdentity = ObjectIdentity
nbDevIdSoftware = _NbDevIdSoftware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 16, 5)
)
_NbDevIdSoftwareMasterOSVers_Type = DisplayString
_NbDevIdSoftwareMasterOSVers_Object = MibScalar
nbDevIdSoftwareMasterOSVers = _NbDevIdSoftwareMasterOSVers_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 16, 5, 1),
    _NbDevIdSoftwareMasterOSVers_Type()
)
nbDevIdSoftwareMasterOSVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbDevIdSoftwareMasterOSVers.setStatus("current")
_NbDevIdSoftwareBuildTime_Type = DisplayString
_NbDevIdSoftwareBuildTime_Object = MibScalar
nbDevIdSoftwareBuildTime = _NbDevIdSoftwareBuildTime_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 16, 5, 2),
    _NbDevIdSoftwareBuildTime_Type()
)
nbDevIdSoftwareBuildTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbDevIdSoftwareBuildTime.setStatus("current")
_NbDevIdMibTable_Object = MibTable
nbDevIdMibTable = _NbDevIdMibTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 16, 5, 3)
)
if mibBuilder.loadTexts:
    nbDevIdMibTable.setStatus("current")
_NbDevIdMibEntry_Object = MibTableRow
nbDevIdMibEntry = _NbDevIdMibEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 16, 5, 3, 1)
)
nbDevIdMibEntry.setIndexNames(
    (0, "DEV-ID-MIB", "nbDevIdMibStdName"),
)
if mibBuilder.loadTexts:
    nbDevIdMibEntry.setStatus("current")


class _NbDevIdMibStdName_Type(DisplayString):
    """Custom type nbDevIdMibStdName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 32),
    )


_NbDevIdMibStdName_Type.__name__ = "DisplayString"
_NbDevIdMibStdName_Object = MibTableColumn
nbDevIdMibStdName = _NbDevIdMibStdName_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 16, 5, 3, 1, 1),
    _NbDevIdMibStdName_Type()
)
nbDevIdMibStdName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbDevIdMibStdName.setStatus("current")


class _NbDevIdMibName_Type(DisplayString):
    """Custom type nbDevIdMibName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 32),
    )


_NbDevIdMibName_Type.__name__ = "DisplayString"
_NbDevIdMibName_Object = MibTableColumn
nbDevIdMibName = _NbDevIdMibName_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 16, 5, 3, 1, 2),
    _NbDevIdMibName_Type()
)
nbDevIdMibName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbDevIdMibName.setStatus("current")
_NbDevIdMibTitle_Type = DisplayString
_NbDevIdMibTitle_Object = MibTableColumn
nbDevIdMibTitle = _NbDevIdMibTitle_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 16, 5, 3, 1, 5),
    _NbDevIdMibTitle_Type()
)
nbDevIdMibTitle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbDevIdMibTitle.setStatus("current")
_NbDevIdMibNote_Type = DisplayString
_NbDevIdMibNote_Object = MibTableColumn
nbDevIdMibNote = _NbDevIdMibNote_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 16, 5, 3, 1, 8),
    _NbDevIdMibNote_Type()
)
nbDevIdMibNote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbDevIdMibNote.setStatus("current")
_NbDevIdFirmware_Type = DisplayString
_NbDevIdFirmware_Object = MibScalar
nbDevIdFirmware = _NbDevIdFirmware_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 16, 6),
    _NbDevIdFirmware_Type()
)
nbDevIdFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbDevIdFirmware.setStatus("current")
_NbDevIdConformance_ObjectIdentity = ObjectIdentity
nbDevIdConformance = _NbDevIdConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 16, 101)
)
_NbDevIdMIBCompliances_ObjectIdentity = ObjectIdentity
nbDevIdMIBCompliances = _NbDevIdMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 16, 101, 1)
)
_NbDevIdMIBGroups_ObjectIdentity = ObjectIdentity
nbDevIdMIBGroups = _NbDevIdMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 16, 101, 2)
)

# Managed Objects groups

nbDevIdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 16, 101, 2, 1)
)
nbDevIdGroup.setObjects(
      *(("DEV-ID-MIB", "nbDevIdTypeName"),
        ("DEV-ID-MIB", "nbDevIdSysName"),
        ("DEV-ID-MIB", "nbDevIdBaseMAC"),
        ("DEV-ID-MIB", "nbDevIdHardwareVersion"),
        ("DEV-ID-MIB", "nbDevIdHardwareSerialBoard"),
        ("DEV-ID-MIB", "nbDevIdHardwareSerialUnit"),
        ("DEV-ID-MIB", "nbDevIdSoftwareMasterOSVers"),
        ("DEV-ID-MIB", "nbDevIdSoftwareBuildTime"),
        ("DEV-ID-MIB", "nbDevIdHardwareCpuNumber"),
        ("DEV-ID-MIB", "nbDevIdCpuSerial"),
        ("DEV-ID-MIB", "nbDevIdCpuDescr"))
)
if mibBuilder.loadTexts:
    nbDevIdGroup.setStatus("current")

nbDevIOptionaldGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 16, 101, 2, 2)
)
nbDevIOptionaldGroup.setObjects(
      *(("DEV-ID-MIB", "nbDevIdMibName"),
        ("DEV-ID-MIB", "nbDevIdMibTitle"),
        ("DEV-ID-MIB", "nbDevIdMibNote"),
        ("DEV-ID-MIB", "nbDevIdFirmware"))
)
if mibBuilder.loadTexts:
    nbDevIOptionaldGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

nbDevIdMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 16, 101, 1, 1)
)
if mibBuilder.loadTexts:
    nbDevIdMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DEV-ID-MIB",
    **{"nbase": nbase,
       "nbSwitchG1": nbSwitchG1,
       "nbSwitchG1Il": nbSwitchG1Il,
       "nbDevId": nbDevId,
       "nbDevIdTypeName": nbDevIdTypeName,
       "nbDevIdSysName": nbDevIdSysName,
       "nbDevIdBaseMAC": nbDevIdBaseMAC,
       "nbDevIdHardware": nbDevIdHardware,
       "nbDevIdHardwareVersion": nbDevIdHardwareVersion,
       "nbDevIdHardwareSerial": nbDevIdHardwareSerial,
       "nbDevIdHardwareSerialBoard": nbDevIdHardwareSerialBoard,
       "nbDevIdHardwareSerialUnit": nbDevIdHardwareSerialUnit,
       "nbDevIdHardwareCpuNumber": nbDevIdHardwareCpuNumber,
       "nbDevIdCpuTable": nbDevIdCpuTable,
       "nbDevIdCpuEntry": nbDevIdCpuEntry,
       "nbDevIdCpuIndex": nbDevIdCpuIndex,
       "nbDevIdCpuSerial": nbDevIdCpuSerial,
       "nbDevIdCpuDescr": nbDevIdCpuDescr,
       "nbDevIdSoftware": nbDevIdSoftware,
       "nbDevIdSoftwareMasterOSVers": nbDevIdSoftwareMasterOSVers,
       "nbDevIdSoftwareBuildTime": nbDevIdSoftwareBuildTime,
       "nbDevIdMibTable": nbDevIdMibTable,
       "nbDevIdMibEntry": nbDevIdMibEntry,
       "nbDevIdMibStdName": nbDevIdMibStdName,
       "nbDevIdMibName": nbDevIdMibName,
       "nbDevIdMibTitle": nbDevIdMibTitle,
       "nbDevIdMibNote": nbDevIdMibNote,
       "nbDevIdFirmware": nbDevIdFirmware,
       "nbDevIdConformance": nbDevIdConformance,
       "nbDevIdMIBCompliances": nbDevIdMIBCompliances,
       "nbDevIdMIBCompliance": nbDevIdMIBCompliance,
       "nbDevIdMIBGroups": nbDevIdMIBGroups,
       "nbDevIdGroup": nbDevIdGroup,
       "nbDevIOptionaldGroup": nbDevIOptionaldGroup}
)
