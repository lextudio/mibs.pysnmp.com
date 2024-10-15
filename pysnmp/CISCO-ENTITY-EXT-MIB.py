# SNMP MIB module (CISCO-ENTITY-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ENTITY-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:59:35 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(Unsigned64,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "Unsigned64")

(entPhysicalContainedIn,
 entPhysicalDescr,
 entPhysicalEntry,
 entPhysicalIndex,
 entPhysicalName) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalContainedIn",
    "entPhysicalDescr",
    "entPhysicalEntry",
    "entPhysicalIndex",
    "entPhysicalName")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoEntityExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 195)
)
ciscoEntityExtMIB.setRevisions(
        ("2015-04-17 00:00",
         "2014-09-12 00:00",
         "2014-03-27 00:00",
         "2013-08-06 00:00",
         "2013-08-05 00:00",
         "2008-11-24 00:00",
         "2004-07-06 00:00",
         "2004-03-03 00:00",
         "2004-01-26 00:00",
         "2003-08-24 00:00",
         "2001-05-17 00:00",
         "2001-04-05 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ConfigRegisterValue(OctetString, TextualConvention):
    status = "current"
    displayHint = "2x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )



class BootImageList(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoEntityExtMIBObjects_ObjectIdentity = ObjectIdentity
ciscoEntityExtMIBObjects = _CiscoEntityExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 195, 1)
)
_CeExtPhysicalProcessorTable_Object = MibTable
ceExtPhysicalProcessorTable = _CeExtPhysicalProcessorTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 1)
)
if mibBuilder.loadTexts:
    ceExtPhysicalProcessorTable.setStatus("current")
_CeExtPhysicalProcessorEntry_Object = MibTableRow
ceExtPhysicalProcessorEntry = _CeExtPhysicalProcessorEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 1, 1)
)
ceExtPhysicalProcessorEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    ceExtPhysicalProcessorEntry.setStatus("current")
_CeExtProcessorRam_Type = Unsigned32
_CeExtProcessorRam_Object = MibTableColumn
ceExtProcessorRam = _CeExtProcessorRam_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 1, 1, 1),
    _CeExtProcessorRam_Type()
)
ceExtProcessorRam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceExtProcessorRam.setStatus("current")
if mibBuilder.loadTexts:
    ceExtProcessorRam.setUnits("bytes")
_CeExtNVRAMSize_Type = Unsigned32
_CeExtNVRAMSize_Object = MibTableColumn
ceExtNVRAMSize = _CeExtNVRAMSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 1, 1, 2),
    _CeExtNVRAMSize_Type()
)
ceExtNVRAMSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceExtNVRAMSize.setStatus("current")
if mibBuilder.loadTexts:
    ceExtNVRAMSize.setUnits("bytes")
_CeExtNVRAMUsed_Type = Unsigned32
_CeExtNVRAMUsed_Object = MibTableColumn
ceExtNVRAMUsed = _CeExtNVRAMUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 1, 1, 3),
    _CeExtNVRAMUsed_Type()
)
ceExtNVRAMUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceExtNVRAMUsed.setStatus("current")
if mibBuilder.loadTexts:
    ceExtNVRAMUsed.setUnits("bytes")
_CeExtProcessorRamOverflow_Type = Unsigned32
_CeExtProcessorRamOverflow_Object = MibTableColumn
ceExtProcessorRamOverflow = _CeExtProcessorRamOverflow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 1, 1, 4),
    _CeExtProcessorRamOverflow_Type()
)
ceExtProcessorRamOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceExtProcessorRamOverflow.setStatus("current")
if mibBuilder.loadTexts:
    ceExtProcessorRamOverflow.setUnits("bytes")
_CeExtHCProcessorRam_Type = Unsigned64
_CeExtHCProcessorRam_Object = MibTableColumn
ceExtHCProcessorRam = _CeExtHCProcessorRam_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 1, 1, 5),
    _CeExtHCProcessorRam_Type()
)
ceExtHCProcessorRam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceExtHCProcessorRam.setStatus("current")
if mibBuilder.loadTexts:
    ceExtHCProcessorRam.setUnits("bytes")
_CeExtConfigRegTable_Object = MibTable
ceExtConfigRegTable = _CeExtConfigRegTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 2)
)
if mibBuilder.loadTexts:
    ceExtConfigRegTable.setStatus("current")
_CeExtConfigRegEntry_Object = MibTableRow
ceExtConfigRegEntry = _CeExtConfigRegEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 2, 1)
)
ceExtConfigRegEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    ceExtConfigRegEntry.setStatus("current")
_CeExtConfigRegister_Type = ConfigRegisterValue
_CeExtConfigRegister_Object = MibTableColumn
ceExtConfigRegister = _CeExtConfigRegister_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 2, 1, 1),
    _CeExtConfigRegister_Type()
)
ceExtConfigRegister.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceExtConfigRegister.setStatus("current")
_CeExtConfigRegNext_Type = ConfigRegisterValue
_CeExtConfigRegNext_Object = MibTableColumn
ceExtConfigRegNext = _CeExtConfigRegNext_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 2, 1, 2),
    _CeExtConfigRegNext_Type()
)
ceExtConfigRegNext.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ceExtConfigRegNext.setStatus("current")
_CeExtSysBootImageList_Type = BootImageList
_CeExtSysBootImageList_Object = MibTableColumn
ceExtSysBootImageList = _CeExtSysBootImageList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 2, 1, 3),
    _CeExtSysBootImageList_Type()
)
ceExtSysBootImageList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ceExtSysBootImageList.setStatus("current")
_CeExtKickstartImageList_Type = BootImageList
_CeExtKickstartImageList_Object = MibTableColumn
ceExtKickstartImageList = _CeExtKickstartImageList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 2, 1, 4),
    _CeExtKickstartImageList_Type()
)
ceExtKickstartImageList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ceExtKickstartImageList.setStatus("current")
_CeExtEntityLEDTable_Object = MibTable
ceExtEntityLEDTable = _CeExtEntityLEDTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 3)
)
if mibBuilder.loadTexts:
    ceExtEntityLEDTable.setStatus("current")
_CeExtEntityLEDEntry_Object = MibTableRow
ceExtEntityLEDEntry = _CeExtEntityLEDEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 3, 1)
)
ceExtEntityLEDEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-ENTITY-EXT-MIB", "ceExtEntityLEDType"),
)
if mibBuilder.loadTexts:
    ceExtEntityLEDEntry.setStatus("current")


class _CeExtEntityLEDType_Type(Integer32):
    """Custom type ceExtEntityLEDType based on Integer32"""
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
        *(("active", 3),
          ("battery", 5),
          ("power", 4),
          ("status", 1),
          ("system", 2))
    )


_CeExtEntityLEDType_Type.__name__ = "Integer32"
_CeExtEntityLEDType_Object = MibTableColumn
ceExtEntityLEDType = _CeExtEntityLEDType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 3, 1, 1),
    _CeExtEntityLEDType_Type()
)
ceExtEntityLEDType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ceExtEntityLEDType.setStatus("current")


class _CeExtEntityLEDColor_Type(Integer32):
    """Custom type ceExtEntityLEDColor based on Integer32"""
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
        *(("amber", 3),
          ("green", 2),
          ("off", 1),
          ("red", 4))
    )


_CeExtEntityLEDColor_Type.__name__ = "Integer32"
_CeExtEntityLEDColor_Object = MibTableColumn
ceExtEntityLEDColor = _CeExtEntityLEDColor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 3, 1, 2),
    _CeExtEntityLEDColor_Type()
)
ceExtEntityLEDColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceExtEntityLEDColor.setStatus("current")
_CeExtEntPhysicalTable_Object = MibTable
ceExtEntPhysicalTable = _CeExtEntPhysicalTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 4)
)
if mibBuilder.loadTexts:
    ceExtEntPhysicalTable.setStatus("current")
_CeExtEntPhysicalEntry_Object = MibTableRow
ceExtEntPhysicalEntry = _CeExtEntPhysicalEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ceExtEntPhysicalEntry.setStatus("current")


class _CeEntPhysicalSecondSerialNum_Type(SnmpAdminString):
    """Custom type ceEntPhysicalSecondSerialNum based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CeEntPhysicalSecondSerialNum_Type.__name__ = "SnmpAdminString"
_CeEntPhysicalSecondSerialNum_Object = MibTableColumn
ceEntPhysicalSecondSerialNum = _CeEntPhysicalSecondSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 4, 1, 1),
    _CeEntPhysicalSecondSerialNum_Type()
)
ceEntPhysicalSecondSerialNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ceEntPhysicalSecondSerialNum.setStatus("current")
_CeExtNotificationControlObjects_ObjectIdentity = ObjectIdentity
ceExtNotificationControlObjects = _CeExtNotificationControlObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 5)
)


class _CeExtEntDoorNotifEnable_Type(TruthValue):
    """Custom type ceExtEntDoorNotifEnable based on TruthValue"""


_CeExtEntDoorNotifEnable_Object = MibScalar
ceExtEntDoorNotifEnable = _CeExtEntDoorNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 5, 1),
    _CeExtEntDoorNotifEnable_Type()
)
ceExtEntDoorNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ceExtEntDoorNotifEnable.setStatus("current")


class _CeExtEntBreakOutPortNotifEnable_Type(TruthValue):
    """Custom type ceExtEntBreakOutPortNotifEnable based on TruthValue"""


_CeExtEntBreakOutPortNotifEnable_Object = MibScalar
ceExtEntBreakOutPortNotifEnable = _CeExtEntBreakOutPortNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 5, 2),
    _CeExtEntBreakOutPortNotifEnable_Type()
)
ceExtEntBreakOutPortNotifEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceExtEntBreakOutPortNotifEnable.setStatus("current")


class _CeExtEntUsbModemNotifEnable_Type(TruthValue):
    """Custom type ceExtEntUsbModemNotifEnable based on TruthValue"""


_CeExtEntUsbModemNotifEnable_Object = MibScalar
ceExtEntUsbModemNotifEnable = _CeExtEntUsbModemNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 5, 3),
    _CeExtEntUsbModemNotifEnable_Type()
)
ceExtEntUsbModemNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ceExtEntUsbModemNotifEnable.setStatus("current")
_CeExtUSBModemTable_Object = MibTable
ceExtUSBModemTable = _CeExtUSBModemTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 6)
)
if mibBuilder.loadTexts:
    ceExtUSBModemTable.setStatus("current")
_CeExtUSBModemEntry_Object = MibTableRow
ceExtUSBModemEntry = _CeExtUSBModemEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 6, 1)
)
ceExtUSBModemEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    ceExtUSBModemEntry.setStatus("current")


class _CeExtUSBModemIMEI_Type(SnmpAdminString):
    """Custom type ceExtUSBModemIMEI based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CeExtUSBModemIMEI_Type.__name__ = "SnmpAdminString"
_CeExtUSBModemIMEI_Object = MibTableColumn
ceExtUSBModemIMEI = _CeExtUSBModemIMEI_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 6, 1, 1),
    _CeExtUSBModemIMEI_Type()
)
ceExtUSBModemIMEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceExtUSBModemIMEI.setStatus("current")


class _CeExtUSBModemIMSI_Type(SnmpAdminString):
    """Custom type ceExtUSBModemIMSI based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CeExtUSBModemIMSI_Type.__name__ = "SnmpAdminString"
_CeExtUSBModemIMSI_Object = MibTableColumn
ceExtUSBModemIMSI = _CeExtUSBModemIMSI_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 6, 1, 2),
    _CeExtUSBModemIMSI_Type()
)
ceExtUSBModemIMSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceExtUSBModemIMSI.setStatus("current")


class _CeExtUSBModemServiceProvider_Type(SnmpAdminString):
    """Custom type ceExtUSBModemServiceProvider based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CeExtUSBModemServiceProvider_Type.__name__ = "SnmpAdminString"
_CeExtUSBModemServiceProvider_Object = MibTableColumn
ceExtUSBModemServiceProvider = _CeExtUSBModemServiceProvider_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 6, 1, 3),
    _CeExtUSBModemServiceProvider_Type()
)
ceExtUSBModemServiceProvider.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceExtUSBModemServiceProvider.setStatus("current")


class _CeExtUSBModemSignalStrength_Type(SnmpAdminString):
    """Custom type ceExtUSBModemSignalStrength based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CeExtUSBModemSignalStrength_Type.__name__ = "SnmpAdminString"
_CeExtUSBModemSignalStrength_Object = MibTableColumn
ceExtUSBModemSignalStrength = _CeExtUSBModemSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 195, 1, 6, 1, 4),
    _CeExtUSBModemSignalStrength_Type()
)
ceExtUSBModemSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceExtUSBModemSignalStrength.setStatus("current")
_CeExtMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
ceExtMIBNotificationPrefix = _CeExtMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 195, 2)
)
_CiscoEntityExtMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoEntityExtMIBNotifications = _CiscoEntityExtMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 195, 2, 0)
)
_CiscoEntityExtMIBConformance_ObjectIdentity = ObjectIdentity
ciscoEntityExtMIBConformance = _CiscoEntityExtMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 195, 3)
)
_CiscoEntityExtMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoEntityExtMIBCompliances = _CiscoEntityExtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 1)
)
_CiscoEntityExtMIBGroups_ObjectIdentity = ObjectIdentity
ciscoEntityExtMIBGroups = _CiscoEntityExtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 2)
)
entPhysicalEntry.registerAugmentions(
    ("CISCO-ENTITY-EXT-MIB",
     "ceExtEntPhysicalEntry")
)
ceExtEntPhysicalEntry.setIndexNames(*entPhysicalEntry.getIndexNames())

# Managed Objects groups

ceExtPhysicalProcessorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 2, 1)
)
ceExtPhysicalProcessorGroup.setObjects(
      *(("CISCO-ENTITY-EXT-MIB", "ceExtProcessorRam"),
        ("CISCO-ENTITY-EXT-MIB", "ceExtNVRAMSize"),
        ("CISCO-ENTITY-EXT-MIB", "ceExtNVRAMUsed"))
)
if mibBuilder.loadTexts:
    ceExtPhysicalProcessorGroup.setStatus("current")

ciscoEntityExtConfigRegGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 2, 2)
)
ciscoEntityExtConfigRegGroup.setObjects(
      *(("CISCO-ENTITY-EXT-MIB", "ceExtConfigRegister"),
        ("CISCO-ENTITY-EXT-MIB", "ceExtConfigRegNext"))
)
if mibBuilder.loadTexts:
    ciscoEntityExtConfigRegGroup.setStatus("current")

ceExtSysBootImageListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 2, 3)
)
ceExtSysBootImageListGroup.setObjects(
    ("CISCO-ENTITY-EXT-MIB", "ceExtSysBootImageList")
)
if mibBuilder.loadTexts:
    ceExtSysBootImageListGroup.setStatus("current")

ciscoEntityExtLEDGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 2, 4)
)
ciscoEntityExtLEDGroup.setObjects(
    ("CISCO-ENTITY-EXT-MIB", "ceExtEntityLEDColor")
)
if mibBuilder.loadTexts:
    ciscoEntityExtLEDGroup.setStatus("current")

ceExtSysBootImageListGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 2, 5)
)
ceExtSysBootImageListGroupRev1.setObjects(
    ("CISCO-ENTITY-EXT-MIB", "ceExtKickstartImageList")
)
if mibBuilder.loadTexts:
    ceExtSysBootImageListGroupRev1.setStatus("current")

ciscoExtEntityPhysicalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 2, 6)
)
ciscoExtEntityPhysicalGroup.setObjects(
    ("CISCO-ENTITY-EXT-MIB", "ceEntPhysicalSecondSerialNum")
)
if mibBuilder.loadTexts:
    ciscoExtEntityPhysicalGroup.setStatus("current")

ceExtPhyProcessorOverflowGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 2, 7)
)
ceExtPhyProcessorOverflowGroup.setObjects(
    ("CISCO-ENTITY-EXT-MIB", "ceExtProcessorRamOverflow")
)
if mibBuilder.loadTexts:
    ceExtPhyProcessorOverflowGroup.setStatus("current")

ceExtPhyProcessorHCGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 2, 8)
)
ceExtPhyProcessorHCGroup.setObjects(
    ("CISCO-ENTITY-EXT-MIB", "ceExtHCProcessorRam")
)
if mibBuilder.loadTexts:
    ceExtPhyProcessorHCGroup.setStatus("current")

ceExtEntDoorNotifControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 2, 10)
)
ceExtEntDoorNotifControlGroup.setObjects(
    ("CISCO-ENTITY-EXT-MIB", "ceExtEntDoorNotifEnable")
)
if mibBuilder.loadTexts:
    ceExtEntDoorNotifControlGroup.setStatus("current")

ceExtBreakOutPortNotifControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 2, 12)
)
ceExtBreakOutPortNotifControlGroup.setObjects(
    ("CISCO-ENTITY-EXT-MIB", "ceExtEntBreakOutPortNotifEnable")
)
if mibBuilder.loadTexts:
    ceExtBreakOutPortNotifControlGroup.setStatus("current")

ceExtUSBModemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 2, 13)
)
ceExtUSBModemGroup.setObjects(
      *(("CISCO-ENTITY-EXT-MIB", "ceExtUSBModemIMEI"),
        ("CISCO-ENTITY-EXT-MIB", "ceExtUSBModemIMSI"),
        ("CISCO-ENTITY-EXT-MIB", "ceExtUSBModemServiceProvider"),
        ("CISCO-ENTITY-EXT-MIB", "ceExtUSBModemSignalStrength"))
)
if mibBuilder.loadTexts:
    ceExtUSBModemGroup.setStatus("current")

ceExtUsbModemNotifControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 2, 15)
)
ceExtUsbModemNotifControlGroup.setObjects(
    ("CISCO-ENTITY-EXT-MIB", "ceExtEntUsbModemNotifEnable")
)
if mibBuilder.loadTexts:
    ceExtUsbModemNotifControlGroup.setStatus("current")


# Notification objects

ceExtEntDoorCloseNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 195, 2, 0, 1)
)
ceExtEntDoorCloseNotif.setObjects(
      *(("ENTITY-MIB", "entPhysicalDescr"),
        ("ENTITY-MIB", "entPhysicalName"))
)
if mibBuilder.loadTexts:
    ceExtEntDoorCloseNotif.setStatus(
        "current"
    )

ceExtEntDoorOpenNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 195, 2, 0, 2)
)
ceExtEntDoorOpenNotif.setObjects(
      *(("ENTITY-MIB", "entPhysicalDescr"),
        ("ENTITY-MIB", "entPhysicalName"))
)
if mibBuilder.loadTexts:
    ceExtEntDoorOpenNotif.setStatus(
        "current"
    )

ceExtBreakOutPortInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 195, 2, 0, 3)
)
ceExtBreakOutPortInserted.setObjects(
      *(("ENTITY-MIB", "entPhysicalContainedIn"),
        ("ENTITY-MIB", "entPhysicalName"))
)
if mibBuilder.loadTexts:
    ceExtBreakOutPortInserted.setStatus(
        "current"
    )

ceExtBreakOutPortRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 195, 2, 0, 4)
)
ceExtBreakOutPortRemoved.setObjects(
      *(("ENTITY-MIB", "entPhysicalContainedIn"),
        ("ENTITY-MIB", "entPhysicalName"))
)
if mibBuilder.loadTexts:
    ceExtBreakOutPortRemoved.setStatus(
        "current"
    )

ceExtUSBModemPlugInNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 195, 2, 0, 5)
)
ceExtUSBModemPlugInNotif.setObjects(
      *(("ENTITY-MIB", "entPhysicalContainedIn"),
        ("ENTITY-MIB", "entPhysicalDescr"))
)
if mibBuilder.loadTexts:
    ceExtUSBModemPlugInNotif.setStatus(
        "current"
    )

ceExtUSBModemPlugOutNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 195, 2, 0, 6)
)
ceExtUSBModemPlugOutNotif.setObjects(
      *(("ENTITY-MIB", "entPhysicalContainedIn"),
        ("ENTITY-MIB", "entPhysicalDescr"))
)
if mibBuilder.loadTexts:
    ceExtUSBModemPlugOutNotif.setStatus(
        "current"
    )


# Notifications groups

ceExtEntDoorNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 2, 9)
)
ceExtEntDoorNotifGroup.setObjects(
      *(("CISCO-ENTITY-EXT-MIB", "ceExtEntDoorCloseNotif"),
        ("CISCO-ENTITY-EXT-MIB", "ceExtEntDoorOpenNotif"))
)
if mibBuilder.loadTexts:
    ceExtEntDoorNotifGroup.setStatus(
        "current"
    )

ceExtBreakOutPortNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 2, 11)
)
ceExtBreakOutPortNotifGroup.setObjects(
      *(("CISCO-ENTITY-EXT-MIB", "ceExtBreakOutPortInserted"),
        ("CISCO-ENTITY-EXT-MIB", "ceExtBreakOutPortRemoved"))
)
if mibBuilder.loadTexts:
    ceExtBreakOutPortNotifGroup.setStatus(
        "current"
    )

ceExtUsbModemNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 2, 14)
)
ceExtUsbModemNotificationsGroup.setObjects(
      *(("CISCO-ENTITY-EXT-MIB", "ceExtUSBModemPlugInNotif"),
        ("CISCO-ENTITY-EXT-MIB", "ceExtUSBModemPlugOutNotif"))
)
if mibBuilder.loadTexts:
    ceExtUsbModemNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoEntityExtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoEntityExtMIBCompliance.setStatus(
        "deprecated"
    )

ciscoEntityExtMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoEntityExtMIBComplianceRev1.setStatus(
        "deprecated"
    )

ciscoEntityExtMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoEntityExtMIBComplianceRev2.setStatus(
        "deprecated"
    )

ciscoEntityExtMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoEntityExtMIBComplianceRev3.setStatus(
        "deprecated"
    )

ciscoEntityExtMIBComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 1, 5)
)
if mibBuilder.loadTexts:
    ciscoEntityExtMIBComplianceRev4.setStatus(
        "deprecated"
    )

ciscoEntityExtMIBComplianceRev5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 1, 6)
)
if mibBuilder.loadTexts:
    ciscoEntityExtMIBComplianceRev5.setStatus(
        "deprecated"
    )

ciscoEntityExtMIBComplianceRev6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 195, 3, 1, 7)
)
if mibBuilder.loadTexts:
    ciscoEntityExtMIBComplianceRev6.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ENTITY-EXT-MIB",
    **{"ConfigRegisterValue": ConfigRegisterValue,
       "BootImageList": BootImageList,
       "ciscoEntityExtMIB": ciscoEntityExtMIB,
       "ciscoEntityExtMIBObjects": ciscoEntityExtMIBObjects,
       "ceExtPhysicalProcessorTable": ceExtPhysicalProcessorTable,
       "ceExtPhysicalProcessorEntry": ceExtPhysicalProcessorEntry,
       "ceExtProcessorRam": ceExtProcessorRam,
       "ceExtNVRAMSize": ceExtNVRAMSize,
       "ceExtNVRAMUsed": ceExtNVRAMUsed,
       "ceExtProcessorRamOverflow": ceExtProcessorRamOverflow,
       "ceExtHCProcessorRam": ceExtHCProcessorRam,
       "ceExtConfigRegTable": ceExtConfigRegTable,
       "ceExtConfigRegEntry": ceExtConfigRegEntry,
       "ceExtConfigRegister": ceExtConfigRegister,
       "ceExtConfigRegNext": ceExtConfigRegNext,
       "ceExtSysBootImageList": ceExtSysBootImageList,
       "ceExtKickstartImageList": ceExtKickstartImageList,
       "ceExtEntityLEDTable": ceExtEntityLEDTable,
       "ceExtEntityLEDEntry": ceExtEntityLEDEntry,
       "ceExtEntityLEDType": ceExtEntityLEDType,
       "ceExtEntityLEDColor": ceExtEntityLEDColor,
       "ceExtEntPhysicalTable": ceExtEntPhysicalTable,
       "ceExtEntPhysicalEntry": ceExtEntPhysicalEntry,
       "ceEntPhysicalSecondSerialNum": ceEntPhysicalSecondSerialNum,
       "ceExtNotificationControlObjects": ceExtNotificationControlObjects,
       "ceExtEntDoorNotifEnable": ceExtEntDoorNotifEnable,
       "ceExtEntBreakOutPortNotifEnable": ceExtEntBreakOutPortNotifEnable,
       "ceExtEntUsbModemNotifEnable": ceExtEntUsbModemNotifEnable,
       "ceExtUSBModemTable": ceExtUSBModemTable,
       "ceExtUSBModemEntry": ceExtUSBModemEntry,
       "ceExtUSBModemIMEI": ceExtUSBModemIMEI,
       "ceExtUSBModemIMSI": ceExtUSBModemIMSI,
       "ceExtUSBModemServiceProvider": ceExtUSBModemServiceProvider,
       "ceExtUSBModemSignalStrength": ceExtUSBModemSignalStrength,
       "ceExtMIBNotificationPrefix": ceExtMIBNotificationPrefix,
       "ciscoEntityExtMIBNotifications": ciscoEntityExtMIBNotifications,
       "ceExtEntDoorCloseNotif": ceExtEntDoorCloseNotif,
       "ceExtEntDoorOpenNotif": ceExtEntDoorOpenNotif,
       "ceExtBreakOutPortInserted": ceExtBreakOutPortInserted,
       "ceExtBreakOutPortRemoved": ceExtBreakOutPortRemoved,
       "ceExtUSBModemPlugInNotif": ceExtUSBModemPlugInNotif,
       "ceExtUSBModemPlugOutNotif": ceExtUSBModemPlugOutNotif,
       "ciscoEntityExtMIBConformance": ciscoEntityExtMIBConformance,
       "ciscoEntityExtMIBCompliances": ciscoEntityExtMIBCompliances,
       "ciscoEntityExtMIBCompliance": ciscoEntityExtMIBCompliance,
       "ciscoEntityExtMIBComplianceRev1": ciscoEntityExtMIBComplianceRev1,
       "ciscoEntityExtMIBComplianceRev2": ciscoEntityExtMIBComplianceRev2,
       "ciscoEntityExtMIBComplianceRev3": ciscoEntityExtMIBComplianceRev3,
       "ciscoEntityExtMIBComplianceRev4": ciscoEntityExtMIBComplianceRev4,
       "ciscoEntityExtMIBComplianceRev5": ciscoEntityExtMIBComplianceRev5,
       "ciscoEntityExtMIBComplianceRev6": ciscoEntityExtMIBComplianceRev6,
       "ciscoEntityExtMIBGroups": ciscoEntityExtMIBGroups,
       "ceExtPhysicalProcessorGroup": ceExtPhysicalProcessorGroup,
       "ciscoEntityExtConfigRegGroup": ciscoEntityExtConfigRegGroup,
       "ceExtSysBootImageListGroup": ceExtSysBootImageListGroup,
       "ciscoEntityExtLEDGroup": ciscoEntityExtLEDGroup,
       "ceExtSysBootImageListGroupRev1": ceExtSysBootImageListGroupRev1,
       "ciscoExtEntityPhysicalGroup": ciscoExtEntityPhysicalGroup,
       "ceExtPhyProcessorOverflowGroup": ceExtPhyProcessorOverflowGroup,
       "ceExtPhyProcessorHCGroup": ceExtPhyProcessorHCGroup,
       "ceExtEntDoorNotifGroup": ceExtEntDoorNotifGroup,
       "ceExtEntDoorNotifControlGroup": ceExtEntDoorNotifControlGroup,
       "ceExtBreakOutPortNotifGroup": ceExtBreakOutPortNotifGroup,
       "ceExtBreakOutPortNotifControlGroup": ceExtBreakOutPortNotifControlGroup,
       "ceExtUSBModemGroup": ceExtUSBModemGroup,
       "ceExtUsbModemNotificationsGroup": ceExtUsbModemNotificationsGroup,
       "ceExtUsbModemNotifControlGroup": ceExtUsbModemNotifControlGroup}
)
