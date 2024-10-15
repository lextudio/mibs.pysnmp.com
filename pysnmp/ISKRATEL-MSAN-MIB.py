# SNMP MIB module (ISKRATEL-MSAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ISKRATEL-MSAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:11:52 2024
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

(dot1dBasePort,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(InetAddress,
 InetAddressIPv4,
 InetAddressIPv6,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv4",
    "InetAddressIPv6",
    "InetAddressType")

(VlanIndex,
 dot1qVlanIndex) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex",
    "dot1qVlanIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Bits,
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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(vdslLineConfProfileName,) = mibBuilder.importSymbols(
    "VDSL-LINE-MIB",
    "vdslLineConfProfileName")

(xdsl2LineAlarmConfTemplateEntry,
 xdsl2LineConfTemplateEntry) = mibBuilder.importSymbols(
    "VDSL2-LINE-MIB",
    "xdsl2LineAlarmConfTemplateEntry",
    "xdsl2LineConfTemplateEntry")


# MODULE-IDENTITY

msan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class VlanList(OctetString, TextualConvention):
    status = "current"


class Xdsl2PsdMaskDs(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 96),
    )



class Xdsl2PsdMaskUs(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )



class PortMask(OctetString, TextualConvention):
    status = "current"


class PercentByFives(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(15, 15),
        ValueRangeConstraint(20, 20),
        ValueRangeConstraint(25, 25),
        ValueRangeConstraint(30, 30),
        ValueRangeConstraint(35, 35),
        ValueRangeConstraint(40, 40),
        ValueRangeConstraint(45, 45),
        ValueRangeConstraint(50, 50),
        ValueRangeConstraint(55, 55),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(65, 65),
        ValueRangeConstraint(70, 70),
        ValueRangeConstraint(75, 75),
        ValueRangeConstraint(80, 80),
        ValueRangeConstraint(85, 85),
        ValueRangeConstraint(90, 90),
        ValueRangeConstraint(95, 95),
        ValueRangeConstraint(100, 100),
    )



# MIB Managed Objects in the order of their OIDs

_Iskratel_ObjectIdentity = ObjectIdentity
iskratel = _Iskratel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332)
)
_Si2000_ObjectIdentity = ObjectIdentity
si2000 = _Si2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1)
)
_MsanInfo_ObjectIdentity = ObjectIdentity
msanInfo = _MsanInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 1)
)
_MsanShelfInfo_ObjectIdentity = ObjectIdentity
msanShelfInfo = _MsanShelfInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 1, 1)
)
_MsanShelfId_Type = OctetString
_MsanShelfId_Object = MibScalar
msanShelfId = _MsanShelfId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 1, 1, 1),
    _MsanShelfId_Type()
)
msanShelfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShelfId.setStatus("current")
_MsanShelfType_Type = OctetString
_MsanShelfType_Object = MibScalar
msanShelfType = _MsanShelfType_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 1, 1, 2),
    _MsanShelfType_Type()
)
msanShelfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShelfType.setStatus("current")
_MsanShelfSize_Type = Integer32
_MsanShelfSize_Object = MibScalar
msanShelfSize = _MsanShelfSize_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 1, 1, 3),
    _MsanShelfSize_Type()
)
msanShelfSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShelfSize.setStatus("current")
_MsanBoardInfo_ObjectIdentity = ObjectIdentity
msanBoardInfo = _MsanBoardInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 1, 2)
)
_MsanBoardTable_Object = MibTable
msanBoardTable = _MsanBoardTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 1, 2, 1)
)
if mibBuilder.loadTexts:
    msanBoardTable.setStatus("deprecated")
_MsanBoardEntry_Object = MibTableRow
msanBoardEntry = _MsanBoardEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 1, 2, 1, 1)
)
msanBoardEntry.setIndexNames(
    (0, "ISKRATEL-MSAN-MIB", "msanBoardNr"),
)
if mibBuilder.loadTexts:
    msanBoardEntry.setStatus("deprecated")


class _MsanBoardNr_Type(Integer32):
    """Custom type msanBoardNr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_MsanBoardNr_Type.__name__ = "Integer32"
_MsanBoardNr_Object = MibTableColumn
msanBoardNr = _MsanBoardNr_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 1, 2, 1, 1, 1),
    _MsanBoardNr_Type()
)
msanBoardNr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanBoardNr.setStatus("deprecated")


class _MsanBoardParentNr_Type(Integer32):
    """Custom type msanBoardParentNr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_MsanBoardParentNr_Type.__name__ = "Integer32"
_MsanBoardParentNr_Object = MibTableColumn
msanBoardParentNr = _MsanBoardParentNr_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 1, 2, 1, 1, 2),
    _MsanBoardParentNr_Type()
)
msanBoardParentNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanBoardParentNr.setStatus("deprecated")


class _MsanBoardPosition_Type(Integer32):
    """Custom type msanBoardPosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_MsanBoardPosition_Type.__name__ = "Integer32"
_MsanBoardPosition_Object = MibTableColumn
msanBoardPosition = _MsanBoardPosition_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 1, 2, 1, 1, 3),
    _MsanBoardPosition_Type()
)
msanBoardPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanBoardPosition.setStatus("deprecated")
_MsanBoardType_Type = OctetString
_MsanBoardType_Object = MibTableColumn
msanBoardType = _MsanBoardType_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 1, 2, 1, 1, 4),
    _MsanBoardType_Type()
)
msanBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanBoardType.setStatus("deprecated")
_MsanBoardId_Type = OctetString
_MsanBoardId_Object = MibTableColumn
msanBoardId = _MsanBoardId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 1, 2, 1, 1, 5),
    _MsanBoardId_Type()
)
msanBoardId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanBoardId.setStatus("deprecated")
_MsanBoardSerialNr_Type = OctetString
_MsanBoardSerialNr_Object = MibTableColumn
msanBoardSerialNr = _MsanBoardSerialNr_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 1, 2, 1, 1, 6),
    _MsanBoardSerialNr_Type()
)
msanBoardSerialNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanBoardSerialNr.setStatus("deprecated")
_MsanBoardDescription_Type = OctetString
_MsanBoardDescription_Object = MibTableColumn
msanBoardDescription = _MsanBoardDescription_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 1, 2, 1, 1, 7),
    _MsanBoardDescription_Type()
)
msanBoardDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanBoardDescription.setStatus("deprecated")
_MsanSwInfo_ObjectIdentity = ObjectIdentity
msanSwInfo = _MsanSwInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 1, 3)
)
_MsanSwSteerVersion_Type = OctetString
_MsanSwSteerVersion_Object = MibScalar
msanSwSteerVersion = _MsanSwSteerVersion_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 1, 3, 1),
    _MsanSwSteerVersion_Type()
)
msanSwSteerVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanSwSteerVersion.setStatus("current")
_MsanSwBuildDirectory_Type = OctetString
_MsanSwBuildDirectory_Object = MibScalar
msanSwBuildDirectory = _MsanSwBuildDirectory_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 1, 3, 2),
    _MsanSwBuildDirectory_Type()
)
msanSwBuildDirectory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanSwBuildDirectory.setStatus("current")
_MsanSwBuildTime_Type = OctetString
_MsanSwBuildTime_Object = MibScalar
msanSwBuildTime = _MsanSwBuildTime_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 1, 3, 3),
    _MsanSwBuildTime_Type()
)
msanSwBuildTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanSwBuildTime.setStatus("current")
_MsanSwBranch_Type = OctetString
_MsanSwBranch_Object = MibScalar
msanSwBranch = _MsanSwBranch_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 1, 3, 4),
    _MsanSwBranch_Type()
)
msanSwBranch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanSwBranch.setStatus("current")
_MsanSwBuildReference_Type = Integer32
_MsanSwBuildReference_Object = MibScalar
msanSwBuildReference = _MsanSwBuildReference_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 1, 3, 5),
    _MsanSwBuildReference_Type()
)
msanSwBuildReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanSwBuildReference.setStatus("current")
_MsanSwILVersion_Type = OctetString
_MsanSwILVersion_Object = MibScalar
msanSwILVersion = _MsanSwILVersion_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 1, 3, 6),
    _MsanSwILVersion_Type()
)
msanSwILVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanSwILVersion.setStatus("current")
_MsanSwIpmiVersion_Type = OctetString
_MsanSwIpmiVersion_Object = MibScalar
msanSwIpmiVersion = _MsanSwIpmiVersion_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 1, 3, 7),
    _MsanSwIpmiVersion_Type()
)
msanSwIpmiVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanSwIpmiVersion.setStatus("current")
_MsanSwBspVersion_Type = OctetString
_MsanSwBspVersion_Object = MibScalar
msanSwBspVersion = _MsanSwBspVersion_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 1, 3, 8),
    _MsanSwBspVersion_Type()
)
msanSwBspVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanSwBspVersion.setStatus("current")
_MsanSwCPLDVersion_Type = OctetString
_MsanSwCPLDVersion_Object = MibScalar
msanSwCPLDVersion = _MsanSwCPLDVersion_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 1, 3, 9),
    _MsanSwCPLDVersion_Type()
)
msanSwCPLDVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanSwCPLDVersion.setStatus("current")
_MsanReservePackage_Type = OctetString
_MsanReservePackage_Object = MibScalar
msanReservePackage = _MsanReservePackage_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 1, 3, 10),
    _MsanReservePackage_Type()
)
msanReservePackage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanReservePackage.setStatus("current")
_MsanSwComponentTable_Object = MibTable
msanSwComponentTable = _MsanSwComponentTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 1, 3, 11)
)
if mibBuilder.loadTexts:
    msanSwComponentTable.setStatus("current")
_MsanSwComponentEntry_Object = MibTableRow
msanSwComponentEntry = _MsanSwComponentEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 1, 3, 11, 1)
)
msanSwComponentEntry.setIndexNames(
    (0, "ISKRATEL-MSAN-MIB", "msanSwComponentId"),
)
if mibBuilder.loadTexts:
    msanSwComponentEntry.setStatus("current")
_MsanSwComponentId_Type = Integer32
_MsanSwComponentId_Object = MibTableColumn
msanSwComponentId = _MsanSwComponentId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 1, 3, 11, 1, 1),
    _MsanSwComponentId_Type()
)
msanSwComponentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanSwComponentId.setStatus("current")
_MsanSwComponentName_Type = OctetString
_MsanSwComponentName_Object = MibTableColumn
msanSwComponentName = _MsanSwComponentName_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 1, 3, 11, 1, 2),
    _MsanSwComponentName_Type()
)
msanSwComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanSwComponentName.setStatus("current")
_MsanSwComponentSteerVersion_Type = OctetString
_MsanSwComponentSteerVersion_Object = MibTableColumn
msanSwComponentSteerVersion = _MsanSwComponentSteerVersion_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 1, 3, 11, 1, 3),
    _MsanSwComponentSteerVersion_Type()
)
msanSwComponentSteerVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanSwComponentSteerVersion.setStatus("current")
_MsanOtherInfo_ObjectIdentity = ObjectIdentity
msanOtherInfo = _MsanOtherInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 1, 4)
)
_MsanSnmpSetErrorReason_Type = OctetString
_MsanSnmpSetErrorReason_Object = MibScalar
msanSnmpSetErrorReason = _MsanSnmpSetErrorReason_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 1, 4, 1),
    _MsanSnmpSetErrorReason_Type()
)
msanSnmpSetErrorReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanSnmpSetErrorReason.setStatus("current")
_MsanAdditionalConf_ObjectIdentity = ObjectIdentity
msanAdditionalConf = _MsanAdditionalConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3)
)
_MsanSystem_ObjectIdentity = ObjectIdentity
msanSystem = _MsanSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 1)
)
_MsanDateTime_Type = OctetString
_MsanDateTime_Object = MibScalar
msanDateTime = _MsanDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 1, 1),
    _MsanDateTime_Type()
)
msanDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDateTime.setStatus("current")
_MsanShelfIdConf_Type = OctetString
_MsanShelfIdConf_Object = MibScalar
msanShelfIdConf = _MsanShelfIdConf_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 1, 2),
    _MsanShelfIdConf_Type()
)
msanShelfIdConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanShelfIdConf.setStatus("current")


class _MsanConfData_Type(Integer32):
    """Custom type msanConfData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSaved", 2),
          ("saved", 1))
    )


_MsanConfData_Type.__name__ = "Integer32"
_MsanConfData_Object = MibScalar
msanConfData = _MsanConfData_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 1, 3),
    _MsanConfData_Type()
)
msanConfData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanConfData.setStatus("current")
_MsanSwUpgrade_Type = OctetString
_MsanSwUpgrade_Object = MibScalar
msanSwUpgrade = _MsanSwUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 1, 4),
    _MsanSwUpgrade_Type()
)
msanSwUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanSwUpgrade.setStatus("deprecated")


class _MsanCliScriptCreate_Type(OctetString):
    """Custom type msanCliScriptCreate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MsanCliScriptCreate_Type.__name__ = "OctetString"
_MsanCliScriptCreate_Object = MibScalar
msanCliScriptCreate = _MsanCliScriptCreate_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 1, 5),
    _MsanCliScriptCreate_Type()
)
msanCliScriptCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanCliScriptCreate.setStatus("current")
_MsanCliScriptTable_Object = MibTable
msanCliScriptTable = _MsanCliScriptTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 1, 6)
)
if mibBuilder.loadTexts:
    msanCliScriptTable.setStatus("current")
_MsanCliScriptEntry_Object = MibTableRow
msanCliScriptEntry = _MsanCliScriptEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 1, 6, 1)
)
msanCliScriptEntry.setIndexNames(
    (0, "ISKRATEL-MSAN-MIB", "msanCliScriptName"),
)
if mibBuilder.loadTexts:
    msanCliScriptEntry.setStatus("current")


class _MsanCliScriptName_Type(OctetString):
    """Custom type msanCliScriptName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MsanCliScriptName_Type.__name__ = "OctetString"
_MsanCliScriptName_Object = MibTableColumn
msanCliScriptName = _MsanCliScriptName_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 1, 6, 1, 1),
    _MsanCliScriptName_Type()
)
msanCliScriptName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanCliScriptName.setStatus("current")


class _MsanCliScriptApply_Type(Integer32):
    """Custom type msanCliScriptApply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanCliScriptApply_Type.__name__ = "Integer32"
_MsanCliScriptApply_Object = MibTableColumn
msanCliScriptApply = _MsanCliScriptApply_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 1, 6, 1, 2),
    _MsanCliScriptApply_Type()
)
msanCliScriptApply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanCliScriptApply.setStatus("current")


class _MsanCliScriptApplyStatus_Type(Integer32):
    """Custom type msanCliScriptApplyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inProcess", 2),
          ("notInitiated", 1))
    )


_MsanCliScriptApplyStatus_Type.__name__ = "Integer32"
_MsanCliScriptApplyStatus_Object = MibTableColumn
msanCliScriptApplyStatus = _MsanCliScriptApplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 1, 6, 1, 3),
    _MsanCliScriptApplyStatus_Type()
)
msanCliScriptApplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanCliScriptApplyStatus.setStatus("current")
_MsanCliScriptRowStatus_Type = RowStatus
_MsanCliScriptRowStatus_Object = MibTableColumn
msanCliScriptRowStatus = _MsanCliScriptRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 1, 6, 1, 4),
    _MsanCliScriptRowStatus_Type()
)
msanCliScriptRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanCliScriptRowStatus.setStatus("current")


class _MsanCliPrompt_Type(OctetString):
    """Custom type msanCliPrompt based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MsanCliPrompt_Type.__name__ = "OctetString"
_MsanCliPrompt_Object = MibScalar
msanCliPrompt = _MsanCliPrompt_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 1, 7),
    _MsanCliPrompt_Type()
)
msanCliPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanCliPrompt.setStatus("current")


class _MsanChassisId_Type(Integer32):
    """Custom type msanChassisId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_MsanChassisId_Type.__name__ = "Integer32"
_MsanChassisId_Object = MibScalar
msanChassisId = _MsanChassisId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 1, 8),
    _MsanChassisId_Type()
)
msanChassisId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanChassisId.setStatus("current")
_MsanSwBootPackageTable_Object = MibTable
msanSwBootPackageTable = _MsanSwBootPackageTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 1, 9)
)
if mibBuilder.loadTexts:
    msanSwBootPackageTable.setStatus("current")
_MsanSwBootPackageEntry_Object = MibTableRow
msanSwBootPackageEntry = _MsanSwBootPackageEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 1, 9, 1)
)
msanSwBootPackageEntry.setIndexNames(
    (0, "ISKRATEL-MSAN-MIB", "msanSwBootPackageName"),
)
if mibBuilder.loadTexts:
    msanSwBootPackageEntry.setStatus("current")
_MsanSwBootPackageName_Type = DisplayString
_MsanSwBootPackageName_Object = MibTableColumn
msanSwBootPackageName = _MsanSwBootPackageName_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 1, 9, 1, 1),
    _MsanSwBootPackageName_Type()
)
msanSwBootPackageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanSwBootPackageName.setStatus("current")


class _MsanSwBootPackageStatus_Type(Integer32):
    """Custom type msanSwBootPackageStatus based on Integer32"""
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
          ("currentActive", 1),
          ("nextActive", 2),
          ("none", 4))
    )


_MsanSwBootPackageStatus_Type.__name__ = "Integer32"
_MsanSwBootPackageStatus_Object = MibTableColumn
msanSwBootPackageStatus = _MsanSwBootPackageStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 1, 9, 1, 2),
    _MsanSwBootPackageStatus_Type()
)
msanSwBootPackageStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanSwBootPackageStatus.setStatus("current")
_MsanSystemSwUpgrade_ObjectIdentity = ObjectIdentity
msanSystemSwUpgrade = _MsanSystemSwUpgrade_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 1, 10)
)


class _MsanSystemSwUpgradeStart_Type(Integer32):
    """Custom type msanSystemSwUpgradeStart based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanSystemSwUpgradeStart_Type.__name__ = "Integer32"
_MsanSystemSwUpgradeStart_Object = MibScalar
msanSystemSwUpgradeStart = _MsanSystemSwUpgradeStart_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 1, 10, 1),
    _MsanSystemSwUpgradeStart_Type()
)
msanSystemSwUpgradeStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanSystemSwUpgradeStart.setStatus("current")


class _MsanSystemSwUpgradeStatus_Type(Integer32):
    """Custom type msanSystemSwUpgradeStatus based on Integer32"""
    defaultValue = 4

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
        *(("failed", 3),
          ("inprogress", 1),
          ("notInitiated", 4),
          ("successful", 2))
    )


_MsanSystemSwUpgradeStatus_Type.__name__ = "Integer32"
_MsanSystemSwUpgradeStatus_Object = MibScalar
msanSystemSwUpgradeStatus = _MsanSystemSwUpgradeStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 1, 10, 2),
    _MsanSystemSwUpgradeStatus_Type()
)
msanSystemSwUpgradeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanSystemSwUpgradeStatus.setStatus("current")


class _MsanSystemSwUpgradeServerIpAddressType_Type(InetAddressType):
    """Custom type msanSystemSwUpgradeServerIpAddressType based on InetAddressType"""


_MsanSystemSwUpgradeServerIpAddressType_Object = MibScalar
msanSystemSwUpgradeServerIpAddressType = _MsanSystemSwUpgradeServerIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 1, 10, 3),
    _MsanSystemSwUpgradeServerIpAddressType_Type()
)
msanSystemSwUpgradeServerIpAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanSystemSwUpgradeServerIpAddressType.setStatus("current")
_MsanSystemSwUpgradeServerIpAddress_Type = InetAddress
_MsanSystemSwUpgradeServerIpAddress_Object = MibScalar
msanSystemSwUpgradeServerIpAddress = _MsanSystemSwUpgradeServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 1, 10, 4),
    _MsanSystemSwUpgradeServerIpAddress_Type()
)
msanSystemSwUpgradeServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanSystemSwUpgradeServerIpAddress.setStatus("current")


class _MsanSystemSwUpgradeServerDnsName_Type(DisplayString):
    """Custom type msanSystemSwUpgradeServerDnsName based on DisplayString"""
    defaultHexValue = ""


_MsanSystemSwUpgradeServerDnsName_Object = MibScalar
msanSystemSwUpgradeServerDnsName = _MsanSystemSwUpgradeServerDnsName_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 1, 10, 5),
    _MsanSystemSwUpgradeServerDnsName_Type()
)
msanSystemSwUpgradeServerDnsName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanSystemSwUpgradeServerDnsName.setStatus("current")


class _MsanSystemSwUpgradeProtocol_Type(Integer32):
    """Custom type msanSystemSwUpgradeProtocol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 2),
          ("sftp", 3),
          ("tftp", 1))
    )


_MsanSystemSwUpgradeProtocol_Type.__name__ = "Integer32"
_MsanSystemSwUpgradeProtocol_Object = MibScalar
msanSystemSwUpgradeProtocol = _MsanSystemSwUpgradeProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 1, 10, 6),
    _MsanSystemSwUpgradeProtocol_Type()
)
msanSystemSwUpgradeProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanSystemSwUpgradeProtocol.setStatus("current")


class _MsanSystemSwUpgradeProtocolPortId_Type(Integer32):
    """Custom type msanSystemSwUpgradeProtocolPortId based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_MsanSystemSwUpgradeProtocolPortId_Type.__name__ = "Integer32"
_MsanSystemSwUpgradeProtocolPortId_Object = MibScalar
msanSystemSwUpgradeProtocolPortId = _MsanSystemSwUpgradeProtocolPortId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 1, 10, 7),
    _MsanSystemSwUpgradeProtocolPortId_Type()
)
msanSystemSwUpgradeProtocolPortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanSystemSwUpgradeProtocolPortId.setStatus("current")


class _MsanSystemSwUpgradeUserName_Type(DisplayString):
    """Custom type msanSystemSwUpgradeUserName based on DisplayString"""
    defaultHexValue = ""


_MsanSystemSwUpgradeUserName_Object = MibScalar
msanSystemSwUpgradeUserName = _MsanSystemSwUpgradeUserName_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 1, 10, 8),
    _MsanSystemSwUpgradeUserName_Type()
)
msanSystemSwUpgradeUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanSystemSwUpgradeUserName.setStatus("current")


class _MsanSystemSwUpgradeUserPassword_Type(DisplayString):
    """Custom type msanSystemSwUpgradeUserPassword based on DisplayString"""
    defaultHexValue = ""


_MsanSystemSwUpgradeUserPassword_Object = MibScalar
msanSystemSwUpgradeUserPassword = _MsanSystemSwUpgradeUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 1, 10, 9),
    _MsanSystemSwUpgradeUserPassword_Type()
)
msanSystemSwUpgradeUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanSystemSwUpgradeUserPassword.setStatus("current")


class _MsanSystemSwUpgradePath_Type(DisplayString):
    """Custom type msanSystemSwUpgradePath based on DisplayString"""
    defaultHexValue = ""


_MsanSystemSwUpgradePath_Object = MibScalar
msanSystemSwUpgradePath = _MsanSystemSwUpgradePath_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 1, 10, 10),
    _MsanSystemSwUpgradePath_Type()
)
msanSystemSwUpgradePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanSystemSwUpgradePath.setStatus("current")


class _MsanSystemSwUpgradePackageName_Type(DisplayString):
    """Custom type msanSystemSwUpgradePackageName based on DisplayString"""
    defaultHexValue = ""


_MsanSystemSwUpgradePackageName_Object = MibScalar
msanSystemSwUpgradePackageName = _MsanSystemSwUpgradePackageName_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 1, 10, 11),
    _MsanSystemSwUpgradePackageName_Type()
)
msanSystemSwUpgradePackageName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanSystemSwUpgradePackageName.setStatus("current")
_MsanSystemLogsUpload_ObjectIdentity = ObjectIdentity
msanSystemLogsUpload = _MsanSystemLogsUpload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 1, 11)
)


class _MsanSystemLogsUploadStart_Type(Integer32):
    """Custom type msanSystemLogsUploadStart based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanSystemLogsUploadStart_Type.__name__ = "Integer32"
_MsanSystemLogsUploadStart_Object = MibScalar
msanSystemLogsUploadStart = _MsanSystemLogsUploadStart_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 1, 11, 1),
    _MsanSystemLogsUploadStart_Type()
)
msanSystemLogsUploadStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanSystemLogsUploadStart.setStatus("current")


class _MsanSystemLogsUploadStatus_Type(Integer32):
    """Custom type msanSystemLogsUploadStatus based on Integer32"""
    defaultValue = 4

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
        *(("failed", 3),
          ("inprogress", 1),
          ("notInitiated", 4),
          ("successful", 2))
    )


_MsanSystemLogsUploadStatus_Type.__name__ = "Integer32"
_MsanSystemLogsUploadStatus_Object = MibScalar
msanSystemLogsUploadStatus = _MsanSystemLogsUploadStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 1, 11, 2),
    _MsanSystemLogsUploadStatus_Type()
)
msanSystemLogsUploadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanSystemLogsUploadStatus.setStatus("current")


class _MsanSystemLogsUploadServerIpAddressType_Type(InetAddressType):
    """Custom type msanSystemLogsUploadServerIpAddressType based on InetAddressType"""


_MsanSystemLogsUploadServerIpAddressType_Object = MibScalar
msanSystemLogsUploadServerIpAddressType = _MsanSystemLogsUploadServerIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 1, 11, 3),
    _MsanSystemLogsUploadServerIpAddressType_Type()
)
msanSystemLogsUploadServerIpAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanSystemLogsUploadServerIpAddressType.setStatus("current")
_MsanSystemLogsUploadServerIpAddress_Type = InetAddress
_MsanSystemLogsUploadServerIpAddress_Object = MibScalar
msanSystemLogsUploadServerIpAddress = _MsanSystemLogsUploadServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 1, 11, 4),
    _MsanSystemLogsUploadServerIpAddress_Type()
)
msanSystemLogsUploadServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanSystemLogsUploadServerIpAddress.setStatus("current")


class _MsanSystemLogsUploadServerDnsName_Type(DisplayString):
    """Custom type msanSystemLogsUploadServerDnsName based on DisplayString"""
    defaultHexValue = ""


_MsanSystemLogsUploadServerDnsName_Object = MibScalar
msanSystemLogsUploadServerDnsName = _MsanSystemLogsUploadServerDnsName_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 1, 11, 5),
    _MsanSystemLogsUploadServerDnsName_Type()
)
msanSystemLogsUploadServerDnsName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanSystemLogsUploadServerDnsName.setStatus("current")


class _MsanSystemLogsUploadProtocol_Type(Integer32):
    """Custom type msanSystemLogsUploadProtocol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 2),
          ("sftp", 3),
          ("tftp", 1))
    )


_MsanSystemLogsUploadProtocol_Type.__name__ = "Integer32"
_MsanSystemLogsUploadProtocol_Object = MibScalar
msanSystemLogsUploadProtocol = _MsanSystemLogsUploadProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 1, 11, 6),
    _MsanSystemLogsUploadProtocol_Type()
)
msanSystemLogsUploadProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanSystemLogsUploadProtocol.setStatus("current")


class _MsanSystemLogsUploadProtocolPortId_Type(Integer32):
    """Custom type msanSystemLogsUploadProtocolPortId based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_MsanSystemLogsUploadProtocolPortId_Type.__name__ = "Integer32"
_MsanSystemLogsUploadProtocolPortId_Object = MibScalar
msanSystemLogsUploadProtocolPortId = _MsanSystemLogsUploadProtocolPortId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 1, 11, 7),
    _MsanSystemLogsUploadProtocolPortId_Type()
)
msanSystemLogsUploadProtocolPortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanSystemLogsUploadProtocolPortId.setStatus("current")


class _MsanSystemLogsUploadUserName_Type(DisplayString):
    """Custom type msanSystemLogsUploadUserName based on DisplayString"""
    defaultHexValue = ""


_MsanSystemLogsUploadUserName_Object = MibScalar
msanSystemLogsUploadUserName = _MsanSystemLogsUploadUserName_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 1, 11, 8),
    _MsanSystemLogsUploadUserName_Type()
)
msanSystemLogsUploadUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanSystemLogsUploadUserName.setStatus("current")


class _MsanSystemLogsUploadUserPassword_Type(DisplayString):
    """Custom type msanSystemLogsUploadUserPassword based on DisplayString"""
    defaultHexValue = ""


_MsanSystemLogsUploadUserPassword_Object = MibScalar
msanSystemLogsUploadUserPassword = _MsanSystemLogsUploadUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 1, 11, 9),
    _MsanSystemLogsUploadUserPassword_Type()
)
msanSystemLogsUploadUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanSystemLogsUploadUserPassword.setStatus("current")


class _MsanSystemLogsUploadPath_Type(DisplayString):
    """Custom type msanSystemLogsUploadPath based on DisplayString"""
    defaultHexValue = ""


_MsanSystemLogsUploadPath_Object = MibScalar
msanSystemLogsUploadPath = _MsanSystemLogsUploadPath_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 1, 11, 10),
    _MsanSystemLogsUploadPath_Type()
)
msanSystemLogsUploadPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanSystemLogsUploadPath.setStatus("current")


class _MsanSystemLogsUploadFileName_Type(DisplayString):
    """Custom type msanSystemLogsUploadFileName based on DisplayString"""
    defaultHexValue = ""


_MsanSystemLogsUploadFileName_Object = MibScalar
msanSystemLogsUploadFileName = _MsanSystemLogsUploadFileName_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 1, 11, 11),
    _MsanSystemLogsUploadFileName_Type()
)
msanSystemLogsUploadFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanSystemLogsUploadFileName.setStatus("current")
_MsanProfiles_ObjectIdentity = ObjectIdentity
msanProfiles = _MsanProfiles_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3)
)
_MsanVDSLProfileTable_Object = MibTable
msanVDSLProfileTable = _MsanVDSLProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 1)
)
if mibBuilder.loadTexts:
    msanVDSLProfileTable.setStatus("current")
_MsanVDSLProfileEntry_Object = MibTableRow
msanVDSLProfileEntry = _MsanVDSLProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 1, 1)
)
msanVDSLProfileEntry.setIndexNames(
    (0, "VDSL-LINE-MIB", "vdslLineConfProfileName"),
)
if mibBuilder.loadTexts:
    msanVDSLProfileEntry.setStatus("current")


class _MsanVDSLProfileType_Type(Integer32):
    """Custom type msanVDSLProfileType based on Integer32"""
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
        *(("default", 2),
          ("global", 4),
          ("local", 3),
          ("other", 1))
    )


_MsanVDSLProfileType_Type.__name__ = "Integer32"
_MsanVDSLProfileType_Object = MibTableColumn
msanVDSLProfileType = _MsanVDSLProfileType_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 1, 1, 1),
    _MsanVDSLProfileType_Type()
)
msanVDSLProfileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanVDSLProfileType.setStatus("current")


class _MsanVDSL2LineProfile_Type(Integer32):
    """Custom type msanVDSL2LineProfile based on Integer32"""
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
        *(("vdsl2profile12a", 3),
          ("vdsl2profile12b", 4),
          ("vdsl2profile17a", 5),
          ("vdsl2profile8c", 1),
          ("vdsl2profile8d", 2))
    )


_MsanVDSL2LineProfile_Type.__name__ = "Integer32"
_MsanVDSL2LineProfile_Object = MibTableColumn
msanVDSL2LineProfile = _MsanVDSL2LineProfile_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 1, 1, 2),
    _MsanVDSL2LineProfile_Type()
)
msanVDSL2LineProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanVDSL2LineProfile.setStatus("current")
_MsanServiceProfile_ObjectIdentity = ObjectIdentity
msanServiceProfile = _MsanServiceProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 2)
)
_MsanServiceProfileTable_Object = MibTable
msanServiceProfileTable = _MsanServiceProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 2, 1)
)
if mibBuilder.loadTexts:
    msanServiceProfileTable.setStatus("current")
_MsanServiceProfileEntry_Object = MibTableRow
msanServiceProfileEntry = _MsanServiceProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 2, 1, 1)
)
msanServiceProfileEntry.setIndexNames(
    (0, "ISKRATEL-MSAN-MIB", "msanServiceProfileName"),
)
if mibBuilder.loadTexts:
    msanServiceProfileEntry.setStatus("current")


class _MsanServiceProfileName_Type(OctetString):
    """Custom type msanServiceProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_MsanServiceProfileName_Type.__name__ = "OctetString"
_MsanServiceProfileName_Object = MibTableColumn
msanServiceProfileName = _MsanServiceProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 2, 1, 1, 1),
    _MsanServiceProfileName_Type()
)
msanServiceProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanServiceProfileName.setStatus("current")


class _MsanServiceProfileProtection_Type(Integer32):
    """Custom type msanServiceProfileProtection based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("protected", 1),
          ("unprotected", 0))
    )


_MsanServiceProfileProtection_Type.__name__ = "Integer32"
_MsanServiceProfileProtection_Object = MibTableColumn
msanServiceProfileProtection = _MsanServiceProfileProtection_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 2, 1, 1, 2),
    _MsanServiceProfileProtection_Type()
)
msanServiceProfileProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceProfileProtection.setStatus("current")


class _MsanServiceProfileStatus_Type(Integer32):
    """Custom type msanServiceProfileStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_MsanServiceProfileStatus_Type.__name__ = "Integer32"
_MsanServiceProfileStatus_Object = MibTableColumn
msanServiceProfileStatus = _MsanServiceProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 2, 1, 1, 3),
    _MsanServiceProfileStatus_Type()
)
msanServiceProfileStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanServiceProfileStatus.setStatus("current")
_MsanServiceProfileServiceFlowProfileName_Type = OctetString
_MsanServiceProfileServiceFlowProfileName_Object = MibTableColumn
msanServiceProfileServiceFlowProfileName = _MsanServiceProfileServiceFlowProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 2, 1, 1, 4),
    _MsanServiceProfileServiceFlowProfileName_Type()
)
msanServiceProfileServiceFlowProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceProfileServiceFlowProfileName.setStatus("current")
_MsanServiceProfileMulticastProfileName_Type = OctetString
_MsanServiceProfileMulticastProfileName_Object = MibTableColumn
msanServiceProfileMulticastProfileName = _MsanServiceProfileMulticastProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 2, 1, 1, 5),
    _MsanServiceProfileMulticastProfileName_Type()
)
msanServiceProfileMulticastProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceProfileMulticastProfileName.setStatus("current")
_MsanServiceProfileVlanProfileName_Type = OctetString
_MsanServiceProfileVlanProfileName_Object = MibTableColumn
msanServiceProfileVlanProfileName = _MsanServiceProfileVlanProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 2, 1, 1, 6),
    _MsanServiceProfileVlanProfileName_Type()
)
msanServiceProfileVlanProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceProfileVlanProfileName.setStatus("current")
_MsanServiceProfileL2cpProfileName_Type = OctetString
_MsanServiceProfileL2cpProfileName_Object = MibTableColumn
msanServiceProfileL2cpProfileName = _MsanServiceProfileL2cpProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 2, 1, 1, 7),
    _MsanServiceProfileL2cpProfileName_Type()
)
msanServiceProfileL2cpProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceProfileL2cpProfileName.setStatus("current")
_MsanServiceProfileSecurityProfileName_Type = OctetString
_MsanServiceProfileSecurityProfileName_Object = MibTableColumn
msanServiceProfileSecurityProfileName = _MsanServiceProfileSecurityProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 2, 1, 1, 8),
    _MsanServiceProfileSecurityProfileName_Type()
)
msanServiceProfileSecurityProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceProfileSecurityProfileName.setStatus("current")


class _MsanServiceProfileAtmVpi_Type(Integer32):
    """Custom type msanServiceProfileAtmVpi based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_MsanServiceProfileAtmVpi_Type.__name__ = "Integer32"
_MsanServiceProfileAtmVpi_Object = MibTableColumn
msanServiceProfileAtmVpi = _MsanServiceProfileAtmVpi_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 2, 1, 1, 9),
    _MsanServiceProfileAtmVpi_Type()
)
msanServiceProfileAtmVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceProfileAtmVpi.setStatus("current")


class _MsanServiceProfileAtmVci_Type(Integer32):
    """Custom type msanServiceProfileAtmVci based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(32, 255),
    )


_MsanServiceProfileAtmVci_Type.__name__ = "Integer32"
_MsanServiceProfileAtmVci_Object = MibTableColumn
msanServiceProfileAtmVci = _MsanServiceProfileAtmVci_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 2, 1, 1, 10),
    _MsanServiceProfileAtmVci_Type()
)
msanServiceProfileAtmVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceProfileAtmVci.setStatus("current")


class _MsanServiceProfileDhcpRa_Type(Integer32):
    """Custom type msanServiceProfileDhcpRa based on Integer32"""
    defaultValue = 0

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
        *(("allowAll", 3),
          ("allowClients", 1),
          ("allowServers", 2),
          ("disabled", 0))
    )


_MsanServiceProfileDhcpRa_Type.__name__ = "Integer32"
_MsanServiceProfileDhcpRa_Object = MibTableColumn
msanServiceProfileDhcpRa = _MsanServiceProfileDhcpRa_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 2, 1, 1, 11),
    _MsanServiceProfileDhcpRa_Type()
)
msanServiceProfileDhcpRa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceProfileDhcpRa.setStatus("current")


class _MsanServiceProfileDhcpRaTrustClients_Type(Integer32):
    """Custom type msanServiceProfileDhcpRaTrustClients based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notTrust", 0),
          ("trust", 1))
    )


_MsanServiceProfileDhcpRaTrustClients_Type.__name__ = "Integer32"
_MsanServiceProfileDhcpRaTrustClients_Object = MibTableColumn
msanServiceProfileDhcpRaTrustClients = _MsanServiceProfileDhcpRaTrustClients_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 2, 1, 1, 12),
    _MsanServiceProfileDhcpRaTrustClients_Type()
)
msanServiceProfileDhcpRaTrustClients.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceProfileDhcpRaTrustClients.setStatus("current")


class _MsanServiceProfileDhcpRaOpt82UnicastExtension_Type(Integer32):
    """Custom type msanServiceProfileDhcpRaOpt82UnicastExtension based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notUsed", 0),
          ("used", 1))
    )


_MsanServiceProfileDhcpRaOpt82UnicastExtension_Type.__name__ = "Integer32"
_MsanServiceProfileDhcpRaOpt82UnicastExtension_Object = MibTableColumn
msanServiceProfileDhcpRaOpt82UnicastExtension = _MsanServiceProfileDhcpRaOpt82UnicastExtension_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 2, 1, 1, 13),
    _MsanServiceProfileDhcpRaOpt82UnicastExtension_Type()
)
msanServiceProfileDhcpRaOpt82UnicastExtension.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceProfileDhcpRaOpt82UnicastExtension.setStatus("current")


class _MsanServiceProfileDhcpRaOpt82Insert_Type(Integer32):
    """Custom type msanServiceProfileDhcpRaOpt82Insert based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("insert", 1),
          ("notInsert", 0))
    )


_MsanServiceProfileDhcpRaOpt82Insert_Type.__name__ = "Integer32"
_MsanServiceProfileDhcpRaOpt82Insert_Object = MibTableColumn
msanServiceProfileDhcpRaOpt82Insert = _MsanServiceProfileDhcpRaOpt82Insert_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 2, 1, 1, 14),
    _MsanServiceProfileDhcpRaOpt82Insert_Type()
)
msanServiceProfileDhcpRaOpt82Insert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceProfileDhcpRaOpt82Insert.setStatus("current")


class _MsanServiceProfileDhcpRaRemoteId_Type(OctetString):
    """Custom type msanServiceProfileDhcpRaRemoteId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_MsanServiceProfileDhcpRaRemoteId_Type.__name__ = "OctetString"
_MsanServiceProfileDhcpRaRemoteId_Object = MibTableColumn
msanServiceProfileDhcpRaRemoteId = _MsanServiceProfileDhcpRaRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 2, 1, 1, 15),
    _MsanServiceProfileDhcpRaRemoteId_Type()
)
msanServiceProfileDhcpRaRemoteId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceProfileDhcpRaRemoteId.setStatus("current")


class _MsanServiceProfileDhcpRaRateLimit_Type(Unsigned32):
    """Custom type msanServiceProfileDhcpRaRateLimit based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_MsanServiceProfileDhcpRaRateLimit_Type.__name__ = "Unsigned32"
_MsanServiceProfileDhcpRaRateLimit_Object = MibTableColumn
msanServiceProfileDhcpRaRateLimit = _MsanServiceProfileDhcpRaRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 2, 1, 1, 16),
    _MsanServiceProfileDhcpRaRateLimit_Type()
)
msanServiceProfileDhcpRaRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceProfileDhcpRaRateLimit.setStatus("current")


class _MsanServiceProfilePppoeIA_Type(Integer32):
    """Custom type msanServiceProfilePppoeIA based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_MsanServiceProfilePppoeIA_Type.__name__ = "Integer32"
_MsanServiceProfilePppoeIA_Object = MibTableColumn
msanServiceProfilePppoeIA = _MsanServiceProfilePppoeIA_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 2, 1, 1, 17),
    _MsanServiceProfilePppoeIA_Type()
)
msanServiceProfilePppoeIA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceProfilePppoeIA.setStatus("current")


class _MsanServiceProfilePppoeIARateLimit_Type(Unsigned32):
    """Custom type msanServiceProfilePppoeIARateLimit based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_MsanServiceProfilePppoeIARateLimit_Type.__name__ = "Unsigned32"
_MsanServiceProfilePppoeIARateLimit_Object = MibTableColumn
msanServiceProfilePppoeIARateLimit = _MsanServiceProfilePppoeIARateLimit_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 2, 1, 1, 18),
    _MsanServiceProfilePppoeIARateLimit_Type()
)
msanServiceProfilePppoeIARateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceProfilePppoeIARateLimit.setStatus("current")


class _MsanServiceProfileDescription_Type(OctetString):
    """Custom type msanServiceProfileDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MsanServiceProfileDescription_Type.__name__ = "OctetString"
_MsanServiceProfileDescription_Object = MibTableColumn
msanServiceProfileDescription = _MsanServiceProfileDescription_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 2, 1, 1, 19),
    _MsanServiceProfileDescription_Type()
)
msanServiceProfileDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceProfileDescription.setStatus("current")
_MsanServiceProfileRowStatus_Type = RowStatus
_MsanServiceProfileRowStatus_Object = MibTableColumn
msanServiceProfileRowStatus = _MsanServiceProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 2, 1, 1, 20),
    _MsanServiceProfileRowStatus_Type()
)
msanServiceProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanServiceProfileRowStatus.setStatus("current")
_MsanServicePortProfileTable_Object = MibTable
msanServicePortProfileTable = _MsanServicePortProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 2, 2)
)
if mibBuilder.loadTexts:
    msanServicePortProfileTable.setStatus("current")
_MsanServicePortProfileEntry_Object = MibTableRow
msanServicePortProfileEntry = _MsanServicePortProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 2, 2, 1)
)
msanServicePortProfileEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ISKRATEL-MSAN-MIB", "msanServiceProfileName"),
)
if mibBuilder.loadTexts:
    msanServicePortProfileEntry.setStatus("current")
_MsanServicePortProfileRowStatus_Type = RowStatus
_MsanServicePortProfileRowStatus_Object = MibTableColumn
msanServicePortProfileRowStatus = _MsanServicePortProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 2, 2, 1, 1),
    _MsanServicePortProfileRowStatus_Type()
)
msanServicePortProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanServicePortProfileRowStatus.setStatus("current")
_MsanServiceFlowProfile_ObjectIdentity = ObjectIdentity
msanServiceFlowProfile = _MsanServiceFlowProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3)
)
_MsanServiceFlowProfileTable_Object = MibTable
msanServiceFlowProfileTable = _MsanServiceFlowProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1)
)
if mibBuilder.loadTexts:
    msanServiceFlowProfileTable.setStatus("current")
_MsanServiceFlowProfileEntry_Object = MibTableRow
msanServiceFlowProfileEntry = _MsanServiceFlowProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1, 1)
)
msanServiceFlowProfileEntry.setIndexNames(
    (0, "ISKRATEL-MSAN-MIB", "msanServiceFlowProfileName"),
)
if mibBuilder.loadTexts:
    msanServiceFlowProfileEntry.setStatus("current")


class _MsanServiceFlowProfileName_Type(OctetString):
    """Custom type msanServiceFlowProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MsanServiceFlowProfileName_Type.__name__ = "OctetString"
_MsanServiceFlowProfileName_Object = MibTableColumn
msanServiceFlowProfileName = _MsanServiceFlowProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1, 1, 1),
    _MsanServiceFlowProfileName_Type()
)
msanServiceFlowProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanServiceFlowProfileName.setStatus("current")


class _MsanServiceFlowProfileProtection_Type(Integer32):
    """Custom type msanServiceFlowProfileProtection based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("protected", 1),
          ("unprotected", 0))
    )


_MsanServiceFlowProfileProtection_Type.__name__ = "Integer32"
_MsanServiceFlowProfileProtection_Object = MibTableColumn
msanServiceFlowProfileProtection = _MsanServiceFlowProfileProtection_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1, 1, 2),
    _MsanServiceFlowProfileProtection_Type()
)
msanServiceFlowProfileProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceFlowProfileProtection.setStatus("current")


class _MsanServiceFlowProfileStatus_Type(Integer32):
    """Custom type msanServiceFlowProfileStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_MsanServiceFlowProfileStatus_Type.__name__ = "Integer32"
_MsanServiceFlowProfileStatus_Object = MibTableColumn
msanServiceFlowProfileStatus = _MsanServiceFlowProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1, 1, 3),
    _MsanServiceFlowProfileStatus_Type()
)
msanServiceFlowProfileStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanServiceFlowProfileStatus.setStatus("current")


class _MsanServiceFlowProfileMatchUsAny_Type(Integer32):
    """Custom type msanServiceFlowProfileMatchUsAny based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanServiceFlowProfileMatchUsAny_Type.__name__ = "Integer32"
_MsanServiceFlowProfileMatchUsAny_Object = MibTableColumn
msanServiceFlowProfileMatchUsAny = _MsanServiceFlowProfileMatchUsAny_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1, 1, 4),
    _MsanServiceFlowProfileMatchUsAny_Type()
)
msanServiceFlowProfileMatchUsAny.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceFlowProfileMatchUsAny.setStatus("current")


class _MsanServiceFlowProfileMatchUsMacDestAddr_Type(MacAddress):
    """Custom type msanServiceFlowProfileMatchUsMacDestAddr based on MacAddress"""
    defaultHexValue = ""


_MsanServiceFlowProfileMatchUsMacDestAddr_Object = MibTableColumn
msanServiceFlowProfileMatchUsMacDestAddr = _MsanServiceFlowProfileMatchUsMacDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1, 1, 5),
    _MsanServiceFlowProfileMatchUsMacDestAddr_Type()
)
msanServiceFlowProfileMatchUsMacDestAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceFlowProfileMatchUsMacDestAddr.setStatus("current")


class _MsanServiceFlowProfileMatchUsMacDestMask_Type(MacAddress):
    """Custom type msanServiceFlowProfileMatchUsMacDestMask based on MacAddress"""
    defaultHexValue = ""


_MsanServiceFlowProfileMatchUsMacDestMask_Object = MibTableColumn
msanServiceFlowProfileMatchUsMacDestMask = _MsanServiceFlowProfileMatchUsMacDestMask_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1, 1, 6),
    _MsanServiceFlowProfileMatchUsMacDestMask_Type()
)
msanServiceFlowProfileMatchUsMacDestMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceFlowProfileMatchUsMacDestMask.setStatus("current")


class _MsanServiceFlowProfileMatchUsMacSrcAddr_Type(MacAddress):
    """Custom type msanServiceFlowProfileMatchUsMacSrcAddr based on MacAddress"""
    defaultHexValue = ""


_MsanServiceFlowProfileMatchUsMacSrcAddr_Object = MibTableColumn
msanServiceFlowProfileMatchUsMacSrcAddr = _MsanServiceFlowProfileMatchUsMacSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1, 1, 7),
    _MsanServiceFlowProfileMatchUsMacSrcAddr_Type()
)
msanServiceFlowProfileMatchUsMacSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceFlowProfileMatchUsMacSrcAddr.setStatus("current")


class _MsanServiceFlowProfileMatchUsMacSrcMask_Type(MacAddress):
    """Custom type msanServiceFlowProfileMatchUsMacSrcMask based on MacAddress"""
    defaultHexValue = ""


_MsanServiceFlowProfileMatchUsMacSrcMask_Object = MibTableColumn
msanServiceFlowProfileMatchUsMacSrcMask = _MsanServiceFlowProfileMatchUsMacSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1, 1, 8),
    _MsanServiceFlowProfileMatchUsMacSrcMask_Type()
)
msanServiceFlowProfileMatchUsMacSrcMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceFlowProfileMatchUsMacSrcMask.setStatus("current")


class _MsanServiceFlowProfileMatchUsCPcp_Type(Integer32):
    """Custom type msanServiceFlowProfileMatchUsCPcp based on Integer32"""
    defaultValue = -1


_MsanServiceFlowProfileMatchUsCPcp_Object = MibTableColumn
msanServiceFlowProfileMatchUsCPcp = _MsanServiceFlowProfileMatchUsCPcp_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1, 1, 9),
    _MsanServiceFlowProfileMatchUsCPcp_Type()
)
msanServiceFlowProfileMatchUsCPcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceFlowProfileMatchUsCPcp.setStatus("current")


class _MsanServiceFlowProfileMatchUsSPcp_Type(Integer32):
    """Custom type msanServiceFlowProfileMatchUsSPcp based on Integer32"""
    defaultValue = -1


_MsanServiceFlowProfileMatchUsSPcp_Object = MibTableColumn
msanServiceFlowProfileMatchUsSPcp = _MsanServiceFlowProfileMatchUsSPcp_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1, 1, 10),
    _MsanServiceFlowProfileMatchUsSPcp_Type()
)
msanServiceFlowProfileMatchUsSPcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceFlowProfileMatchUsSPcp.setStatus("current")


class _MsanServiceFlowProfileMatchUsVlanProfile_Type(Integer32):
    """Custom type msanServiceFlowProfileMatchUsVlanProfile based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanServiceFlowProfileMatchUsVlanProfile_Type.__name__ = "Integer32"
_MsanServiceFlowProfileMatchUsVlanProfile_Object = MibTableColumn
msanServiceFlowProfileMatchUsVlanProfile = _MsanServiceFlowProfileMatchUsVlanProfile_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1, 1, 11),
    _MsanServiceFlowProfileMatchUsVlanProfile_Type()
)
msanServiceFlowProfileMatchUsVlanProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceFlowProfileMatchUsVlanProfile.setStatus("current")


class _MsanServiceFlowProfileMatchUsCVlanIdRange_Type(OctetString):
    """Custom type msanServiceFlowProfileMatchUsCVlanIdRange based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_MsanServiceFlowProfileMatchUsCVlanIdRange_Type.__name__ = "OctetString"
_MsanServiceFlowProfileMatchUsCVlanIdRange_Object = MibTableColumn
msanServiceFlowProfileMatchUsCVlanIdRange = _MsanServiceFlowProfileMatchUsCVlanIdRange_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1, 1, 12),
    _MsanServiceFlowProfileMatchUsCVlanIdRange_Type()
)
msanServiceFlowProfileMatchUsCVlanIdRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceFlowProfileMatchUsCVlanIdRange.setStatus("current")


class _MsanServiceFlowProfileMatchUsSVlanIdRange_Type(OctetString):
    """Custom type msanServiceFlowProfileMatchUsSVlanIdRange based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_MsanServiceFlowProfileMatchUsSVlanIdRange_Type.__name__ = "OctetString"
_MsanServiceFlowProfileMatchUsSVlanIdRange_Object = MibTableColumn
msanServiceFlowProfileMatchUsSVlanIdRange = _MsanServiceFlowProfileMatchUsSVlanIdRange_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1, 1, 13),
    _MsanServiceFlowProfileMatchUsSVlanIdRange_Type()
)
msanServiceFlowProfileMatchUsSVlanIdRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceFlowProfileMatchUsSVlanIdRange.setStatus("current")


class _MsanServiceFlowProfileMatchUsEthertype_Type(Integer32):
    """Custom type msanServiceFlowProfileMatchUsEthertype based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_MsanServiceFlowProfileMatchUsEthertype_Type.__name__ = "Integer32"
_MsanServiceFlowProfileMatchUsEthertype_Object = MibTableColumn
msanServiceFlowProfileMatchUsEthertype = _MsanServiceFlowProfileMatchUsEthertype_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1, 1, 14),
    _MsanServiceFlowProfileMatchUsEthertype_Type()
)
msanServiceFlowProfileMatchUsEthertype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceFlowProfileMatchUsEthertype.setStatus("current")


class _MsanServiceFlowProfileMatchUsIpProtocol_Type(Integer32):
    """Custom type msanServiceFlowProfileMatchUsIpProtocol based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_MsanServiceFlowProfileMatchUsIpProtocol_Type.__name__ = "Integer32"
_MsanServiceFlowProfileMatchUsIpProtocol_Object = MibTableColumn
msanServiceFlowProfileMatchUsIpProtocol = _MsanServiceFlowProfileMatchUsIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1, 1, 15),
    _MsanServiceFlowProfileMatchUsIpProtocol_Type()
)
msanServiceFlowProfileMatchUsIpProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceFlowProfileMatchUsIpProtocol.setStatus("current")


class _MsanServiceFlowProfileMatchUsIpSrcAddr_Type(IpAddress):
    """Custom type msanServiceFlowProfileMatchUsIpSrcAddr based on IpAddress"""
    defaultHexValue = ""


_MsanServiceFlowProfileMatchUsIpSrcAddr_Object = MibTableColumn
msanServiceFlowProfileMatchUsIpSrcAddr = _MsanServiceFlowProfileMatchUsIpSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1, 1, 16),
    _MsanServiceFlowProfileMatchUsIpSrcAddr_Type()
)
msanServiceFlowProfileMatchUsIpSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceFlowProfileMatchUsIpSrcAddr.setStatus("current")


class _MsanServiceFlowProfileMatchUsIpSrcMask_Type(IpAddress):
    """Custom type msanServiceFlowProfileMatchUsIpSrcMask based on IpAddress"""
    defaultHexValue = ""


_MsanServiceFlowProfileMatchUsIpSrcMask_Object = MibTableColumn
msanServiceFlowProfileMatchUsIpSrcMask = _MsanServiceFlowProfileMatchUsIpSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1, 1, 17),
    _MsanServiceFlowProfileMatchUsIpSrcMask_Type()
)
msanServiceFlowProfileMatchUsIpSrcMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceFlowProfileMatchUsIpSrcMask.setStatus("current")


class _MsanServiceFlowProfileMatchUsIpDestAddr_Type(IpAddress):
    """Custom type msanServiceFlowProfileMatchUsIpDestAddr based on IpAddress"""
    defaultHexValue = ""


_MsanServiceFlowProfileMatchUsIpDestAddr_Object = MibTableColumn
msanServiceFlowProfileMatchUsIpDestAddr = _MsanServiceFlowProfileMatchUsIpDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1, 1, 18),
    _MsanServiceFlowProfileMatchUsIpDestAddr_Type()
)
msanServiceFlowProfileMatchUsIpDestAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceFlowProfileMatchUsIpDestAddr.setStatus("current")


class _MsanServiceFlowProfileMatchUsIpDestMask_Type(IpAddress):
    """Custom type msanServiceFlowProfileMatchUsIpDestMask based on IpAddress"""
    defaultHexValue = ""


_MsanServiceFlowProfileMatchUsIpDestMask_Object = MibTableColumn
msanServiceFlowProfileMatchUsIpDestMask = _MsanServiceFlowProfileMatchUsIpDestMask_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1, 1, 19),
    _MsanServiceFlowProfileMatchUsIpDestMask_Type()
)
msanServiceFlowProfileMatchUsIpDestMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceFlowProfileMatchUsIpDestMask.setStatus("current")


class _MsanServiceFlowProfileMatchUsIpDscp_Type(Integer32):
    """Custom type msanServiceFlowProfileMatchUsIpDscp based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_MsanServiceFlowProfileMatchUsIpDscp_Type.__name__ = "Integer32"
_MsanServiceFlowProfileMatchUsIpDscp_Object = MibTableColumn
msanServiceFlowProfileMatchUsIpDscp = _MsanServiceFlowProfileMatchUsIpDscp_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1, 1, 20),
    _MsanServiceFlowProfileMatchUsIpDscp_Type()
)
msanServiceFlowProfileMatchUsIpDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceFlowProfileMatchUsIpDscp.setStatus("current")


class _MsanServiceFlowProfileMatchUsIpCsc_Type(Integer32):
    """Custom type msanServiceFlowProfileMatchUsIpCsc based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_MsanServiceFlowProfileMatchUsIpCsc_Type.__name__ = "Integer32"
_MsanServiceFlowProfileMatchUsIpCsc_Object = MibTableColumn
msanServiceFlowProfileMatchUsIpCsc = _MsanServiceFlowProfileMatchUsIpCsc_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1, 1, 21),
    _MsanServiceFlowProfileMatchUsIpCsc_Type()
)
msanServiceFlowProfileMatchUsIpCsc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceFlowProfileMatchUsIpCsc.setStatus("current")


class _MsanServiceFlowProfileMatchUsIpDropPrecedence_Type(Integer32):
    """Custom type msanServiceFlowProfileMatchUsIpDropPrecedence based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("highDrop", 3),
          ("lowDrop", 1),
          ("mediumDrop", 2),
          ("noDrop", 0),
          ("notDefined", -1))
    )


_MsanServiceFlowProfileMatchUsIpDropPrecedence_Type.__name__ = "Integer32"
_MsanServiceFlowProfileMatchUsIpDropPrecedence_Object = MibTableColumn
msanServiceFlowProfileMatchUsIpDropPrecedence = _MsanServiceFlowProfileMatchUsIpDropPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1, 1, 22),
    _MsanServiceFlowProfileMatchUsIpDropPrecedence_Type()
)
msanServiceFlowProfileMatchUsIpDropPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceFlowProfileMatchUsIpDropPrecedence.setStatus("current")


class _MsanServiceFlowProfileMatchUsTcpSrcPort_Type(Integer32):
    """Custom type msanServiceFlowProfileMatchUsTcpSrcPort based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_MsanServiceFlowProfileMatchUsTcpSrcPort_Type.__name__ = "Integer32"
_MsanServiceFlowProfileMatchUsTcpSrcPort_Object = MibTableColumn
msanServiceFlowProfileMatchUsTcpSrcPort = _MsanServiceFlowProfileMatchUsTcpSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1, 1, 23),
    _MsanServiceFlowProfileMatchUsTcpSrcPort_Type()
)
msanServiceFlowProfileMatchUsTcpSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceFlowProfileMatchUsTcpSrcPort.setStatus("current")


class _MsanServiceFlowProfileMatchUsTcpDestPort_Type(Integer32):
    """Custom type msanServiceFlowProfileMatchUsTcpDestPort based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_MsanServiceFlowProfileMatchUsTcpDestPort_Type.__name__ = "Integer32"
_MsanServiceFlowProfileMatchUsTcpDestPort_Object = MibTableColumn
msanServiceFlowProfileMatchUsTcpDestPort = _MsanServiceFlowProfileMatchUsTcpDestPort_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1, 1, 24),
    _MsanServiceFlowProfileMatchUsTcpDestPort_Type()
)
msanServiceFlowProfileMatchUsTcpDestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceFlowProfileMatchUsTcpDestPort.setStatus("current")


class _MsanServiceFlowProfileMatchUsUdpSrcPort_Type(Integer32):
    """Custom type msanServiceFlowProfileMatchUsUdpSrcPort based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_MsanServiceFlowProfileMatchUsUdpSrcPort_Type.__name__ = "Integer32"
_MsanServiceFlowProfileMatchUsUdpSrcPort_Object = MibTableColumn
msanServiceFlowProfileMatchUsUdpSrcPort = _MsanServiceFlowProfileMatchUsUdpSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1, 1, 25),
    _MsanServiceFlowProfileMatchUsUdpSrcPort_Type()
)
msanServiceFlowProfileMatchUsUdpSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceFlowProfileMatchUsUdpSrcPort.setStatus("current")


class _MsanServiceFlowProfileMatchUsUdpDstPort_Type(Integer32):
    """Custom type msanServiceFlowProfileMatchUsUdpDstPort based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_MsanServiceFlowProfileMatchUsUdpDstPort_Type.__name__ = "Integer32"
_MsanServiceFlowProfileMatchUsUdpDstPort_Object = MibTableColumn
msanServiceFlowProfileMatchUsUdpDstPort = _MsanServiceFlowProfileMatchUsUdpDstPort_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1, 1, 26),
    _MsanServiceFlowProfileMatchUsUdpDstPort_Type()
)
msanServiceFlowProfileMatchUsUdpDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceFlowProfileMatchUsUdpDstPort.setStatus("current")


class _MsanServiceFlowProfileMatchDsAny_Type(Integer32):
    """Custom type msanServiceFlowProfileMatchDsAny based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanServiceFlowProfileMatchDsAny_Type.__name__ = "Integer32"
_MsanServiceFlowProfileMatchDsAny_Object = MibTableColumn
msanServiceFlowProfileMatchDsAny = _MsanServiceFlowProfileMatchDsAny_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1, 1, 27),
    _MsanServiceFlowProfileMatchDsAny_Type()
)
msanServiceFlowProfileMatchDsAny.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceFlowProfileMatchDsAny.setStatus("current")


class _MsanServiceFlowProfileMatchDsMacDestAddr_Type(MacAddress):
    """Custom type msanServiceFlowProfileMatchDsMacDestAddr based on MacAddress"""
    defaultHexValue = ""


_MsanServiceFlowProfileMatchDsMacDestAddr_Object = MibTableColumn
msanServiceFlowProfileMatchDsMacDestAddr = _MsanServiceFlowProfileMatchDsMacDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1, 1, 28),
    _MsanServiceFlowProfileMatchDsMacDestAddr_Type()
)
msanServiceFlowProfileMatchDsMacDestAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceFlowProfileMatchDsMacDestAddr.setStatus("current")


class _MsanServiceFlowProfileMatchDsMacDestMask_Type(MacAddress):
    """Custom type msanServiceFlowProfileMatchDsMacDestMask based on MacAddress"""
    defaultHexValue = ""


_MsanServiceFlowProfileMatchDsMacDestMask_Object = MibTableColumn
msanServiceFlowProfileMatchDsMacDestMask = _MsanServiceFlowProfileMatchDsMacDestMask_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1, 1, 29),
    _MsanServiceFlowProfileMatchDsMacDestMask_Type()
)
msanServiceFlowProfileMatchDsMacDestMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceFlowProfileMatchDsMacDestMask.setStatus("current")


class _MsanServiceFlowProfileMatchDsMacSrcAddr_Type(MacAddress):
    """Custom type msanServiceFlowProfileMatchDsMacSrcAddr based on MacAddress"""
    defaultHexValue = ""


_MsanServiceFlowProfileMatchDsMacSrcAddr_Object = MibTableColumn
msanServiceFlowProfileMatchDsMacSrcAddr = _MsanServiceFlowProfileMatchDsMacSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1, 1, 30),
    _MsanServiceFlowProfileMatchDsMacSrcAddr_Type()
)
msanServiceFlowProfileMatchDsMacSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceFlowProfileMatchDsMacSrcAddr.setStatus("current")


class _MsanServiceFlowProfileMatchDsMacSrcMask_Type(MacAddress):
    """Custom type msanServiceFlowProfileMatchDsMacSrcMask based on MacAddress"""
    defaultHexValue = ""


_MsanServiceFlowProfileMatchDsMacSrcMask_Object = MibTableColumn
msanServiceFlowProfileMatchDsMacSrcMask = _MsanServiceFlowProfileMatchDsMacSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1, 1, 31),
    _MsanServiceFlowProfileMatchDsMacSrcMask_Type()
)
msanServiceFlowProfileMatchDsMacSrcMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceFlowProfileMatchDsMacSrcMask.setStatus("current")


class _MsanServiceFlowProfileMatchDsCPcp_Type(Integer32):
    """Custom type msanServiceFlowProfileMatchDsCPcp based on Integer32"""
    defaultValue = -1


_MsanServiceFlowProfileMatchDsCPcp_Object = MibTableColumn
msanServiceFlowProfileMatchDsCPcp = _MsanServiceFlowProfileMatchDsCPcp_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1, 1, 32),
    _MsanServiceFlowProfileMatchDsCPcp_Type()
)
msanServiceFlowProfileMatchDsCPcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceFlowProfileMatchDsCPcp.setStatus("current")


class _MsanServiceFlowProfileMatchDsSPcp_Type(Integer32):
    """Custom type msanServiceFlowProfileMatchDsSPcp based on Integer32"""
    defaultValue = -1


_MsanServiceFlowProfileMatchDsSPcp_Object = MibTableColumn
msanServiceFlowProfileMatchDsSPcp = _MsanServiceFlowProfileMatchDsSPcp_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1, 1, 33),
    _MsanServiceFlowProfileMatchDsSPcp_Type()
)
msanServiceFlowProfileMatchDsSPcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceFlowProfileMatchDsSPcp.setStatus("current")


class _MsanServiceFlowProfileMatchDsVlanProfile_Type(Integer32):
    """Custom type msanServiceFlowProfileMatchDsVlanProfile based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanServiceFlowProfileMatchDsVlanProfile_Type.__name__ = "Integer32"
_MsanServiceFlowProfileMatchDsVlanProfile_Object = MibTableColumn
msanServiceFlowProfileMatchDsVlanProfile = _MsanServiceFlowProfileMatchDsVlanProfile_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1, 1, 34),
    _MsanServiceFlowProfileMatchDsVlanProfile_Type()
)
msanServiceFlowProfileMatchDsVlanProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceFlowProfileMatchDsVlanProfile.setStatus("current")


class _MsanServiceFlowProfileMatchDsCVlanIdRange_Type(OctetString):
    """Custom type msanServiceFlowProfileMatchDsCVlanIdRange based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_MsanServiceFlowProfileMatchDsCVlanIdRange_Type.__name__ = "OctetString"
_MsanServiceFlowProfileMatchDsCVlanIdRange_Object = MibTableColumn
msanServiceFlowProfileMatchDsCVlanIdRange = _MsanServiceFlowProfileMatchDsCVlanIdRange_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1, 1, 35),
    _MsanServiceFlowProfileMatchDsCVlanIdRange_Type()
)
msanServiceFlowProfileMatchDsCVlanIdRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceFlowProfileMatchDsCVlanIdRange.setStatus("current")


class _MsanServiceFlowProfileMatchDsSVlanIdRange_Type(OctetString):
    """Custom type msanServiceFlowProfileMatchDsSVlanIdRange based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_MsanServiceFlowProfileMatchDsSVlanIdRange_Type.__name__ = "OctetString"
_MsanServiceFlowProfileMatchDsSVlanIdRange_Object = MibTableColumn
msanServiceFlowProfileMatchDsSVlanIdRange = _MsanServiceFlowProfileMatchDsSVlanIdRange_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1, 1, 36),
    _MsanServiceFlowProfileMatchDsSVlanIdRange_Type()
)
msanServiceFlowProfileMatchDsSVlanIdRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceFlowProfileMatchDsSVlanIdRange.setStatus("current")


class _MsanServiceFlowProfileMatchDsEthertype_Type(Integer32):
    """Custom type msanServiceFlowProfileMatchDsEthertype based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_MsanServiceFlowProfileMatchDsEthertype_Type.__name__ = "Integer32"
_MsanServiceFlowProfileMatchDsEthertype_Object = MibTableColumn
msanServiceFlowProfileMatchDsEthertype = _MsanServiceFlowProfileMatchDsEthertype_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1, 1, 37),
    _MsanServiceFlowProfileMatchDsEthertype_Type()
)
msanServiceFlowProfileMatchDsEthertype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceFlowProfileMatchDsEthertype.setStatus("current")


class _MsanServiceFlowProfileMatchDsIpProtocol_Type(Integer32):
    """Custom type msanServiceFlowProfileMatchDsIpProtocol based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_MsanServiceFlowProfileMatchDsIpProtocol_Type.__name__ = "Integer32"
_MsanServiceFlowProfileMatchDsIpProtocol_Object = MibTableColumn
msanServiceFlowProfileMatchDsIpProtocol = _MsanServiceFlowProfileMatchDsIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1, 1, 38),
    _MsanServiceFlowProfileMatchDsIpProtocol_Type()
)
msanServiceFlowProfileMatchDsIpProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceFlowProfileMatchDsIpProtocol.setStatus("current")


class _MsanServiceFlowProfileMatchDsIpSrcAddr_Type(IpAddress):
    """Custom type msanServiceFlowProfileMatchDsIpSrcAddr based on IpAddress"""
    defaultHexValue = ""


_MsanServiceFlowProfileMatchDsIpSrcAddr_Object = MibTableColumn
msanServiceFlowProfileMatchDsIpSrcAddr = _MsanServiceFlowProfileMatchDsIpSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1, 1, 39),
    _MsanServiceFlowProfileMatchDsIpSrcAddr_Type()
)
msanServiceFlowProfileMatchDsIpSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceFlowProfileMatchDsIpSrcAddr.setStatus("current")


class _MsanServiceFlowProfileMatchDsIpSrcMask_Type(IpAddress):
    """Custom type msanServiceFlowProfileMatchDsIpSrcMask based on IpAddress"""
    defaultHexValue = ""


_MsanServiceFlowProfileMatchDsIpSrcMask_Object = MibTableColumn
msanServiceFlowProfileMatchDsIpSrcMask = _MsanServiceFlowProfileMatchDsIpSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1, 1, 40),
    _MsanServiceFlowProfileMatchDsIpSrcMask_Type()
)
msanServiceFlowProfileMatchDsIpSrcMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceFlowProfileMatchDsIpSrcMask.setStatus("current")


class _MsanServiceFlowProfileMatchDsIpDestAddr_Type(IpAddress):
    """Custom type msanServiceFlowProfileMatchDsIpDestAddr based on IpAddress"""
    defaultHexValue = ""


_MsanServiceFlowProfileMatchDsIpDestAddr_Object = MibTableColumn
msanServiceFlowProfileMatchDsIpDestAddr = _MsanServiceFlowProfileMatchDsIpDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1, 1, 41),
    _MsanServiceFlowProfileMatchDsIpDestAddr_Type()
)
msanServiceFlowProfileMatchDsIpDestAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceFlowProfileMatchDsIpDestAddr.setStatus("current")


class _MsanServiceFlowProfileMatchDsIpDestMask_Type(IpAddress):
    """Custom type msanServiceFlowProfileMatchDsIpDestMask based on IpAddress"""
    defaultHexValue = ""


_MsanServiceFlowProfileMatchDsIpDestMask_Object = MibTableColumn
msanServiceFlowProfileMatchDsIpDestMask = _MsanServiceFlowProfileMatchDsIpDestMask_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1, 1, 42),
    _MsanServiceFlowProfileMatchDsIpDestMask_Type()
)
msanServiceFlowProfileMatchDsIpDestMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceFlowProfileMatchDsIpDestMask.setStatus("current")


class _MsanServiceFlowProfileMatchDsIpDscp_Type(Integer32):
    """Custom type msanServiceFlowProfileMatchDsIpDscp based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_MsanServiceFlowProfileMatchDsIpDscp_Type.__name__ = "Integer32"
_MsanServiceFlowProfileMatchDsIpDscp_Object = MibTableColumn
msanServiceFlowProfileMatchDsIpDscp = _MsanServiceFlowProfileMatchDsIpDscp_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1, 1, 43),
    _MsanServiceFlowProfileMatchDsIpDscp_Type()
)
msanServiceFlowProfileMatchDsIpDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceFlowProfileMatchDsIpDscp.setStatus("current")


class _MsanServiceFlowProfileMatchDsIpCsc_Type(Integer32):
    """Custom type msanServiceFlowProfileMatchDsIpCsc based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_MsanServiceFlowProfileMatchDsIpCsc_Type.__name__ = "Integer32"
_MsanServiceFlowProfileMatchDsIpCsc_Object = MibTableColumn
msanServiceFlowProfileMatchDsIpCsc = _MsanServiceFlowProfileMatchDsIpCsc_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1, 1, 44),
    _MsanServiceFlowProfileMatchDsIpCsc_Type()
)
msanServiceFlowProfileMatchDsIpCsc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceFlowProfileMatchDsIpCsc.setStatus("current")


class _MsanServiceFlowProfileMatchDsIpDropPrecedence_Type(Integer32):
    """Custom type msanServiceFlowProfileMatchDsIpDropPrecedence based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("highDrop", 3),
          ("lowDrop", 1),
          ("mediumDrop", 2),
          ("noDrop", 0),
          ("notDefined", -1))
    )


_MsanServiceFlowProfileMatchDsIpDropPrecedence_Type.__name__ = "Integer32"
_MsanServiceFlowProfileMatchDsIpDropPrecedence_Object = MibTableColumn
msanServiceFlowProfileMatchDsIpDropPrecedence = _MsanServiceFlowProfileMatchDsIpDropPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1, 1, 45),
    _MsanServiceFlowProfileMatchDsIpDropPrecedence_Type()
)
msanServiceFlowProfileMatchDsIpDropPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceFlowProfileMatchDsIpDropPrecedence.setStatus("current")


class _MsanServiceFlowProfileMatchDsTcpSrcPort_Type(Integer32):
    """Custom type msanServiceFlowProfileMatchDsTcpSrcPort based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_MsanServiceFlowProfileMatchDsTcpSrcPort_Type.__name__ = "Integer32"
_MsanServiceFlowProfileMatchDsTcpSrcPort_Object = MibTableColumn
msanServiceFlowProfileMatchDsTcpSrcPort = _MsanServiceFlowProfileMatchDsTcpSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1, 1, 46),
    _MsanServiceFlowProfileMatchDsTcpSrcPort_Type()
)
msanServiceFlowProfileMatchDsTcpSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceFlowProfileMatchDsTcpSrcPort.setStatus("current")


class _MsanServiceFlowProfileMatchDsTcpDestPort_Type(Integer32):
    """Custom type msanServiceFlowProfileMatchDsTcpDestPort based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_MsanServiceFlowProfileMatchDsTcpDestPort_Type.__name__ = "Integer32"
_MsanServiceFlowProfileMatchDsTcpDestPort_Object = MibTableColumn
msanServiceFlowProfileMatchDsTcpDestPort = _MsanServiceFlowProfileMatchDsTcpDestPort_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1, 1, 47),
    _MsanServiceFlowProfileMatchDsTcpDestPort_Type()
)
msanServiceFlowProfileMatchDsTcpDestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceFlowProfileMatchDsTcpDestPort.setStatus("current")


class _MsanServiceFlowProfileMatchDsUdpSrcPort_Type(Integer32):
    """Custom type msanServiceFlowProfileMatchDsUdpSrcPort based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_MsanServiceFlowProfileMatchDsUdpSrcPort_Type.__name__ = "Integer32"
_MsanServiceFlowProfileMatchDsUdpSrcPort_Object = MibTableColumn
msanServiceFlowProfileMatchDsUdpSrcPort = _MsanServiceFlowProfileMatchDsUdpSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1, 1, 48),
    _MsanServiceFlowProfileMatchDsUdpSrcPort_Type()
)
msanServiceFlowProfileMatchDsUdpSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceFlowProfileMatchDsUdpSrcPort.setStatus("current")


class _MsanServiceFlowProfileMatchDsUdpDstPort_Type(Integer32):
    """Custom type msanServiceFlowProfileMatchDsUdpDstPort based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_MsanServiceFlowProfileMatchDsUdpDstPort_Type.__name__ = "Integer32"
_MsanServiceFlowProfileMatchDsUdpDstPort_Object = MibTableColumn
msanServiceFlowProfileMatchDsUdpDstPort = _MsanServiceFlowProfileMatchDsUdpDstPort_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1, 1, 49),
    _MsanServiceFlowProfileMatchDsUdpDstPort_Type()
)
msanServiceFlowProfileMatchDsUdpDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceFlowProfileMatchDsUdpDstPort.setStatus("current")


class _MsanServiceFlowProfileUsCdr_Type(Integer32):
    """Custom type msanServiceFlowProfileUsCdr based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_MsanServiceFlowProfileUsCdr_Type.__name__ = "Integer32"
_MsanServiceFlowProfileUsCdr_Object = MibTableColumn
msanServiceFlowProfileUsCdr = _MsanServiceFlowProfileUsCdr_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1, 1, 50),
    _MsanServiceFlowProfileUsCdr_Type()
)
msanServiceFlowProfileUsCdr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceFlowProfileUsCdr.setStatus("current")
if mibBuilder.loadTexts:
    msanServiceFlowProfileUsCdr.setUnits("kbps")


class _MsanServiceFlowProfileUsCdrBurstSize_Type(Integer32):
    """Custom type msanServiceFlowProfileUsCdrBurstSize based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16384),
    )


_MsanServiceFlowProfileUsCdrBurstSize_Type.__name__ = "Integer32"
_MsanServiceFlowProfileUsCdrBurstSize_Object = MibTableColumn
msanServiceFlowProfileUsCdrBurstSize = _MsanServiceFlowProfileUsCdrBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1, 1, 51),
    _MsanServiceFlowProfileUsCdrBurstSize_Type()
)
msanServiceFlowProfileUsCdrBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceFlowProfileUsCdrBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    msanServiceFlowProfileUsCdrBurstSize.setUnits("kB")


class _MsanServiceFlowProfileUsPdr_Type(Integer32):
    """Custom type msanServiceFlowProfileUsPdr based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_MsanServiceFlowProfileUsPdr_Type.__name__ = "Integer32"
_MsanServiceFlowProfileUsPdr_Object = MibTableColumn
msanServiceFlowProfileUsPdr = _MsanServiceFlowProfileUsPdr_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1, 1, 52),
    _MsanServiceFlowProfileUsPdr_Type()
)
msanServiceFlowProfileUsPdr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceFlowProfileUsPdr.setStatus("current")
if mibBuilder.loadTexts:
    msanServiceFlowProfileUsPdr.setUnits("kbps")


class _MsanServiceFlowProfileUsPdrBurstSize_Type(Integer32):
    """Custom type msanServiceFlowProfileUsPdrBurstSize based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16384),
    )


_MsanServiceFlowProfileUsPdrBurstSize_Type.__name__ = "Integer32"
_MsanServiceFlowProfileUsPdrBurstSize_Object = MibTableColumn
msanServiceFlowProfileUsPdrBurstSize = _MsanServiceFlowProfileUsPdrBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1, 1, 53),
    _MsanServiceFlowProfileUsPdrBurstSize_Type()
)
msanServiceFlowProfileUsPdrBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceFlowProfileUsPdrBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    msanServiceFlowProfileUsPdrBurstSize.setUnits("kB")


class _MsanServiceFlowProfileUsMarkPcp_Type(Integer32):
    """Custom type msanServiceFlowProfileUsMarkPcp based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("copyFromCsc", 2),
          ("none", 1),
          ("userValue", 3))
    )


_MsanServiceFlowProfileUsMarkPcp_Type.__name__ = "Integer32"
_MsanServiceFlowProfileUsMarkPcp_Object = MibTableColumn
msanServiceFlowProfileUsMarkPcp = _MsanServiceFlowProfileUsMarkPcp_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1, 1, 54),
    _MsanServiceFlowProfileUsMarkPcp_Type()
)
msanServiceFlowProfileUsMarkPcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceFlowProfileUsMarkPcp.setStatus("current")


class _MsanServiceFlowProfileUsMarkPcpValue_Type(Integer32):
    """Custom type msanServiceFlowProfileUsMarkPcpValue based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_MsanServiceFlowProfileUsMarkPcpValue_Type.__name__ = "Integer32"
_MsanServiceFlowProfileUsMarkPcpValue_Object = MibTableColumn
msanServiceFlowProfileUsMarkPcpValue = _MsanServiceFlowProfileUsMarkPcpValue_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1, 1, 55),
    _MsanServiceFlowProfileUsMarkPcpValue_Type()
)
msanServiceFlowProfileUsMarkPcpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceFlowProfileUsMarkPcpValue.setStatus("current")


class _MsanServiceFlowProfileUsMarkDscp_Type(Integer32):
    """Custom type msanServiceFlowProfileUsMarkDscp based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("copyFromPcp", 2),
          ("none", 1),
          ("userValue", 3))
    )


_MsanServiceFlowProfileUsMarkDscp_Type.__name__ = "Integer32"
_MsanServiceFlowProfileUsMarkDscp_Object = MibTableColumn
msanServiceFlowProfileUsMarkDscp = _MsanServiceFlowProfileUsMarkDscp_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1, 1, 56),
    _MsanServiceFlowProfileUsMarkDscp_Type()
)
msanServiceFlowProfileUsMarkDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceFlowProfileUsMarkDscp.setStatus("current")


class _MsanServiceFlowProfileUsMarkDscpValue_Type(Integer32):
    """Custom type msanServiceFlowProfileUsMarkDscpValue based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_MsanServiceFlowProfileUsMarkDscpValue_Type.__name__ = "Integer32"
_MsanServiceFlowProfileUsMarkDscpValue_Object = MibTableColumn
msanServiceFlowProfileUsMarkDscpValue = _MsanServiceFlowProfileUsMarkDscpValue_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1, 1, 57),
    _MsanServiceFlowProfileUsMarkDscpValue_Type()
)
msanServiceFlowProfileUsMarkDscpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceFlowProfileUsMarkDscpValue.setStatus("current")


class _MsanServiceFlowProfileDsCdr_Type(Integer32):
    """Custom type msanServiceFlowProfileDsCdr based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_MsanServiceFlowProfileDsCdr_Type.__name__ = "Integer32"
_MsanServiceFlowProfileDsCdr_Object = MibTableColumn
msanServiceFlowProfileDsCdr = _MsanServiceFlowProfileDsCdr_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1, 1, 58),
    _MsanServiceFlowProfileDsCdr_Type()
)
msanServiceFlowProfileDsCdr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceFlowProfileDsCdr.setStatus("current")
if mibBuilder.loadTexts:
    msanServiceFlowProfileDsCdr.setUnits("kbps")


class _MsanServiceFlowProfileDsCdrBurstSize_Type(Integer32):
    """Custom type msanServiceFlowProfileDsCdrBurstSize based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16384),
    )


_MsanServiceFlowProfileDsCdrBurstSize_Type.__name__ = "Integer32"
_MsanServiceFlowProfileDsCdrBurstSize_Object = MibTableColumn
msanServiceFlowProfileDsCdrBurstSize = _MsanServiceFlowProfileDsCdrBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1, 1, 59),
    _MsanServiceFlowProfileDsCdrBurstSize_Type()
)
msanServiceFlowProfileDsCdrBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceFlowProfileDsCdrBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    msanServiceFlowProfileDsCdrBurstSize.setUnits("kB")


class _MsanServiceFlowProfileDsPdr_Type(Integer32):
    """Custom type msanServiceFlowProfileDsPdr based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_MsanServiceFlowProfileDsPdr_Type.__name__ = "Integer32"
_MsanServiceFlowProfileDsPdr_Object = MibTableColumn
msanServiceFlowProfileDsPdr = _MsanServiceFlowProfileDsPdr_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1, 1, 60),
    _MsanServiceFlowProfileDsPdr_Type()
)
msanServiceFlowProfileDsPdr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceFlowProfileDsPdr.setStatus("current")
if mibBuilder.loadTexts:
    msanServiceFlowProfileDsPdr.setUnits("kbps")


class _MsanServiceFlowProfileDsPdrBurstSize_Type(Integer32):
    """Custom type msanServiceFlowProfileDsPdrBurstSize based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16384),
    )


_MsanServiceFlowProfileDsPdrBurstSize_Type.__name__ = "Integer32"
_MsanServiceFlowProfileDsPdrBurstSize_Object = MibTableColumn
msanServiceFlowProfileDsPdrBurstSize = _MsanServiceFlowProfileDsPdrBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1, 1, 61),
    _MsanServiceFlowProfileDsPdrBurstSize_Type()
)
msanServiceFlowProfileDsPdrBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceFlowProfileDsPdrBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    msanServiceFlowProfileDsPdrBurstSize.setUnits("kB")


class _MsanServiceFlowProfileDsMarkPcp_Type(Integer32):
    """Custom type msanServiceFlowProfileDsMarkPcp based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("copyFromCsc", 2),
          ("none", 1),
          ("userValue", 3))
    )


_MsanServiceFlowProfileDsMarkPcp_Type.__name__ = "Integer32"
_MsanServiceFlowProfileDsMarkPcp_Object = MibTableColumn
msanServiceFlowProfileDsMarkPcp = _MsanServiceFlowProfileDsMarkPcp_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1, 1, 62),
    _MsanServiceFlowProfileDsMarkPcp_Type()
)
msanServiceFlowProfileDsMarkPcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceFlowProfileDsMarkPcp.setStatus("current")


class _MsanServiceFlowProfileDsMarkPcpValue_Type(Integer32):
    """Custom type msanServiceFlowProfileDsMarkPcpValue based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_MsanServiceFlowProfileDsMarkPcpValue_Type.__name__ = "Integer32"
_MsanServiceFlowProfileDsMarkPcpValue_Object = MibTableColumn
msanServiceFlowProfileDsMarkPcpValue = _MsanServiceFlowProfileDsMarkPcpValue_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1, 1, 63),
    _MsanServiceFlowProfileDsMarkPcpValue_Type()
)
msanServiceFlowProfileDsMarkPcpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceFlowProfileDsMarkPcpValue.setStatus("current")


class _MsanServiceFlowProfileDsMarkDscp_Type(Integer32):
    """Custom type msanServiceFlowProfileDsMarkDscp based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("copyFromPcp", 2),
          ("none", 1),
          ("userValue", 3))
    )


_MsanServiceFlowProfileDsMarkDscp_Type.__name__ = "Integer32"
_MsanServiceFlowProfileDsMarkDscp_Object = MibTableColumn
msanServiceFlowProfileDsMarkDscp = _MsanServiceFlowProfileDsMarkDscp_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1, 1, 64),
    _MsanServiceFlowProfileDsMarkDscp_Type()
)
msanServiceFlowProfileDsMarkDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceFlowProfileDsMarkDscp.setStatus("current")


class _MsanServiceFlowProfileDsMarkDscpValue_Type(Integer32):
    """Custom type msanServiceFlowProfileDsMarkDscpValue based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_MsanServiceFlowProfileDsMarkDscpValue_Type.__name__ = "Integer32"
_MsanServiceFlowProfileDsMarkDscpValue_Object = MibTableColumn
msanServiceFlowProfileDsMarkDscpValue = _MsanServiceFlowProfileDsMarkDscpValue_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1, 1, 65),
    _MsanServiceFlowProfileDsMarkDscpValue_Type()
)
msanServiceFlowProfileDsMarkDscpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceFlowProfileDsMarkDscpValue.setStatus("current")


class _MsanServiceFlowProfileDsQueuingPriority_Type(Integer32):
    """Custom type msanServiceFlowProfileDsQueuingPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MsanServiceFlowProfileDsQueuingPriority_Type.__name__ = "Integer32"
_MsanServiceFlowProfileDsQueuingPriority_Object = MibTableColumn
msanServiceFlowProfileDsQueuingPriority = _MsanServiceFlowProfileDsQueuingPriority_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1, 1, 66),
    _MsanServiceFlowProfileDsQueuingPriority_Type()
)
msanServiceFlowProfileDsQueuingPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceFlowProfileDsQueuingPriority.setStatus("current")


class _MsanServiceFlowProfileDsSchedulingMode_Type(Integer32):
    """Custom type msanServiceFlowProfileDsSchedulingMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("strict", 2),
          ("weighted", 1))
    )


_MsanServiceFlowProfileDsSchedulingMode_Type.__name__ = "Integer32"
_MsanServiceFlowProfileDsSchedulingMode_Object = MibTableColumn
msanServiceFlowProfileDsSchedulingMode = _MsanServiceFlowProfileDsSchedulingMode_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1, 1, 67),
    _MsanServiceFlowProfileDsSchedulingMode_Type()
)
msanServiceFlowProfileDsSchedulingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceFlowProfileDsSchedulingMode.setStatus("current")


class _MsanServiceFlowProfileDescription_Type(OctetString):
    """Custom type msanServiceFlowProfileDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MsanServiceFlowProfileDescription_Type.__name__ = "OctetString"
_MsanServiceFlowProfileDescription_Object = MibTableColumn
msanServiceFlowProfileDescription = _MsanServiceFlowProfileDescription_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1, 1, 68),
    _MsanServiceFlowProfileDescription_Type()
)
msanServiceFlowProfileDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanServiceFlowProfileDescription.setStatus("current")
_MsanServiceFlowProfileRowStatus_Type = RowStatus
_MsanServiceFlowProfileRowStatus_Object = MibTableColumn
msanServiceFlowProfileRowStatus = _MsanServiceFlowProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 3, 1, 1, 69),
    _MsanServiceFlowProfileRowStatus_Type()
)
msanServiceFlowProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanServiceFlowProfileRowStatus.setStatus("current")
_MsanVlanProfile_ObjectIdentity = ObjectIdentity
msanVlanProfile = _MsanVlanProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 4)
)
_MsanVlanProfileTable_Object = MibTable
msanVlanProfileTable = _MsanVlanProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 4, 1)
)
if mibBuilder.loadTexts:
    msanVlanProfileTable.setStatus("current")
_MsanVlanProfileEntry_Object = MibTableRow
msanVlanProfileEntry = _MsanVlanProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 4, 1, 1)
)
msanVlanProfileEntry.setIndexNames(
    (0, "ISKRATEL-MSAN-MIB", "msanVlanProfileName"),
)
if mibBuilder.loadTexts:
    msanVlanProfileEntry.setStatus("current")


class _MsanVlanProfileName_Type(OctetString):
    """Custom type msanVlanProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MsanVlanProfileName_Type.__name__ = "OctetString"
_MsanVlanProfileName_Object = MibTableColumn
msanVlanProfileName = _MsanVlanProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 4, 1, 1, 1),
    _MsanVlanProfileName_Type()
)
msanVlanProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanVlanProfileName.setStatus("current")


class _MsanVlanProfileProtection_Type(Integer32):
    """Custom type msanVlanProfileProtection based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("protected", 1),
          ("unprotected", 0))
    )


_MsanVlanProfileProtection_Type.__name__ = "Integer32"
_MsanVlanProfileProtection_Object = MibTableColumn
msanVlanProfileProtection = _MsanVlanProfileProtection_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 4, 1, 1, 2),
    _MsanVlanProfileProtection_Type()
)
msanVlanProfileProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanVlanProfileProtection.setStatus("current")


class _MsanVlanProfileStatus_Type(Integer32):
    """Custom type msanVlanProfileStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_MsanVlanProfileStatus_Type.__name__ = "Integer32"
_MsanVlanProfileStatus_Object = MibTableColumn
msanVlanProfileStatus = _MsanVlanProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 4, 1, 1, 3),
    _MsanVlanProfileStatus_Type()
)
msanVlanProfileStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanVlanProfileStatus.setStatus("current")


class _MsanVlanProfileCVid_Type(OctetString):
    """Custom type msanVlanProfileCVid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_MsanVlanProfileCVid_Type.__name__ = "OctetString"
_MsanVlanProfileCVid_Object = MibTableColumn
msanVlanProfileCVid = _MsanVlanProfileCVid_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 4, 1, 1, 4),
    _MsanVlanProfileCVid_Type()
)
msanVlanProfileCVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanVlanProfileCVid.setStatus("current")


class _MsanVlanProfileCVidNative_Type(Integer32):
    """Custom type msanVlanProfileCVidNative based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 4094),
    )


_MsanVlanProfileCVidNative_Type.__name__ = "Integer32"
_MsanVlanProfileCVidNative_Object = MibTableColumn
msanVlanProfileCVidNative = _MsanVlanProfileCVidNative_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 4, 1, 1, 5),
    _MsanVlanProfileCVidNative_Type()
)
msanVlanProfileCVidNative.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanVlanProfileCVidNative.setStatus("current")


class _MsanVlanProfileCVidRemark_Type(Integer32):
    """Custom type msanVlanProfileCVidRemark based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 4094),
    )


_MsanVlanProfileCVidRemark_Type.__name__ = "Integer32"
_MsanVlanProfileCVidRemark_Object = MibTableColumn
msanVlanProfileCVidRemark = _MsanVlanProfileCVidRemark_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 4, 1, 1, 6),
    _MsanVlanProfileCVidRemark_Type()
)
msanVlanProfileCVidRemark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanVlanProfileCVidRemark.setStatus("current")


class _MsanVlanProfileSVid_Type(Integer32):
    """Custom type msanVlanProfileSVid based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 4094),
    )


_MsanVlanProfileSVid_Type.__name__ = "Integer32"
_MsanVlanProfileSVid_Object = MibTableColumn
msanVlanProfileSVid = _MsanVlanProfileSVid_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 4, 1, 1, 7),
    _MsanVlanProfileSVid_Type()
)
msanVlanProfileSVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanVlanProfileSVid.setStatus("current")


class _MsanVlanProfileSEtherType_Type(Integer32):
    """Custom type msanVlanProfileSEtherType based on Integer32"""
    defaultHexValue = 34984


_MsanVlanProfileSEtherType_Object = MibTableColumn
msanVlanProfileSEtherType = _MsanVlanProfileSEtherType_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 4, 1, 1, 8),
    _MsanVlanProfileSEtherType_Type()
)
msanVlanProfileSEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanVlanProfileSEtherType.setStatus("current")


class _MsanVlanProfileDescription_Type(OctetString):
    """Custom type msanVlanProfileDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MsanVlanProfileDescription_Type.__name__ = "OctetString"
_MsanVlanProfileDescription_Object = MibTableColumn
msanVlanProfileDescription = _MsanVlanProfileDescription_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 4, 1, 1, 10),
    _MsanVlanProfileDescription_Type()
)
msanVlanProfileDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanVlanProfileDescription.setStatus("current")
_MsanVlanProfileRowStatus_Type = RowStatus
_MsanVlanProfileRowStatus_Object = MibTableColumn
msanVlanProfileRowStatus = _MsanVlanProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 4, 1, 1, 11),
    _MsanVlanProfileRowStatus_Type()
)
msanVlanProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanVlanProfileRowStatus.setStatus("current")


class _MsanVlanProfileNetworkPortCTag_Type(Integer32):
    """Custom type msanVlanProfileNetworkPortCTag based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notUse", 2),
          ("use", 1))
    )


_MsanVlanProfileNetworkPortCTag_Type.__name__ = "Integer32"
_MsanVlanProfileNetworkPortCTag_Object = MibTableColumn
msanVlanProfileNetworkPortCTag = _MsanVlanProfileNetworkPortCTag_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 4, 1, 1, 12),
    _MsanVlanProfileNetworkPortCTag_Type()
)
msanVlanProfileNetworkPortCTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanVlanProfileNetworkPortCTag.setStatus("current")
_MsanVlanPortProfileTable_Object = MibTable
msanVlanPortProfileTable = _MsanVlanPortProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 4, 2)
)
if mibBuilder.loadTexts:
    msanVlanPortProfileTable.setStatus("current")
_MsanVlanPortProfileEntry_Object = MibTableRow
msanVlanPortProfileEntry = _MsanVlanPortProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 4, 2, 1)
)
msanVlanPortProfileEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ISKRATEL-MSAN-MIB", "msanVlanProfileName"),
)
if mibBuilder.loadTexts:
    msanVlanPortProfileEntry.setStatus("current")
_MsanVlanPortProfileRowStatus_Type = RowStatus
_MsanVlanPortProfileRowStatus_Object = MibTableColumn
msanVlanPortProfileRowStatus = _MsanVlanPortProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 4, 2, 1, 1),
    _MsanVlanPortProfileRowStatus_Type()
)
msanVlanPortProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanVlanPortProfileRowStatus.setStatus("current")
_MsanMulticastProfile_ObjectIdentity = ObjectIdentity
msanMulticastProfile = _MsanMulticastProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 5)
)
_MsanMulticastProfileTable_Object = MibTable
msanMulticastProfileTable = _MsanMulticastProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 5, 1)
)
if mibBuilder.loadTexts:
    msanMulticastProfileTable.setStatus("current")
_MsanMulticastProfileEntry_Object = MibTableRow
msanMulticastProfileEntry = _MsanMulticastProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 5, 1, 1)
)
msanMulticastProfileEntry.setIndexNames(
    (0, "ISKRATEL-MSAN-MIB", "msanMulticastProfileName"),
)
if mibBuilder.loadTexts:
    msanMulticastProfileEntry.setStatus("current")


class _MsanMulticastProfileName_Type(OctetString):
    """Custom type msanMulticastProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MsanMulticastProfileName_Type.__name__ = "OctetString"
_MsanMulticastProfileName_Object = MibTableColumn
msanMulticastProfileName = _MsanMulticastProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 5, 1, 1, 1),
    _MsanMulticastProfileName_Type()
)
msanMulticastProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanMulticastProfileName.setStatus("current")


class _MsanMulticastProfileProtection_Type(Integer32):
    """Custom type msanMulticastProfileProtection based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("protected", 1),
          ("unprotected", 0))
    )


_MsanMulticastProfileProtection_Type.__name__ = "Integer32"
_MsanMulticastProfileProtection_Object = MibTableColumn
msanMulticastProfileProtection = _MsanMulticastProfileProtection_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 5, 1, 1, 2),
    _MsanMulticastProfileProtection_Type()
)
msanMulticastProfileProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanMulticastProfileProtection.setStatus("current")


class _MsanMulticastProfileStatus_Type(Integer32):
    """Custom type msanMulticastProfileStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_MsanMulticastProfileStatus_Type.__name__ = "Integer32"
_MsanMulticastProfileStatus_Object = MibTableColumn
msanMulticastProfileStatus = _MsanMulticastProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 5, 1, 1, 3),
    _MsanMulticastProfileStatus_Type()
)
msanMulticastProfileStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanMulticastProfileStatus.setStatus("current")


class _MsanMulticastProfileIgmpSnooping_Type(Integer32):
    """Custom type msanMulticastProfileIgmpSnooping based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_MsanMulticastProfileIgmpSnooping_Type.__name__ = "Integer32"
_MsanMulticastProfileIgmpSnooping_Object = MibTableColumn
msanMulticastProfileIgmpSnooping = _MsanMulticastProfileIgmpSnooping_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 5, 1, 1, 4),
    _MsanMulticastProfileIgmpSnooping_Type()
)
msanMulticastProfileIgmpSnooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanMulticastProfileIgmpSnooping.setStatus("current")


class _MsanMulticastProfileIgmpSnoopingFastLeave_Type(Integer32):
    """Custom type msanMulticastProfileIgmpSnoopingFastLeave based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_MsanMulticastProfileIgmpSnoopingFastLeave_Type.__name__ = "Integer32"
_MsanMulticastProfileIgmpSnoopingFastLeave_Object = MibTableColumn
msanMulticastProfileIgmpSnoopingFastLeave = _MsanMulticastProfileIgmpSnoopingFastLeave_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 5, 1, 1, 5),
    _MsanMulticastProfileIgmpSnoopingFastLeave_Type()
)
msanMulticastProfileIgmpSnoopingFastLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanMulticastProfileIgmpSnoopingFastLeave.setStatus("current")


class _MsanMulticastProfileIgmpSnoopingSuppression_Type(Integer32):
    """Custom type msanMulticastProfileIgmpSnoopingSuppression based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_MsanMulticastProfileIgmpSnoopingSuppression_Type.__name__ = "Integer32"
_MsanMulticastProfileIgmpSnoopingSuppression_Object = MibTableColumn
msanMulticastProfileIgmpSnoopingSuppression = _MsanMulticastProfileIgmpSnoopingSuppression_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 5, 1, 1, 6),
    _MsanMulticastProfileIgmpSnoopingSuppression_Type()
)
msanMulticastProfileIgmpSnoopingSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanMulticastProfileIgmpSnoopingSuppression.setStatus("current")


class _MsanMulticastProfileIgmpProxy_Type(Integer32):
    """Custom type msanMulticastProfileIgmpProxy based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_MsanMulticastProfileIgmpProxy_Type.__name__ = "Integer32"
_MsanMulticastProfileIgmpProxy_Object = MibTableColumn
msanMulticastProfileIgmpProxy = _MsanMulticastProfileIgmpProxy_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 5, 1, 1, 7),
    _MsanMulticastProfileIgmpProxy_Type()
)
msanMulticastProfileIgmpProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanMulticastProfileIgmpProxy.setStatus("current")
_MsanMulticastProfileIgmpProxyIpAddress_Type = IpAddress
_MsanMulticastProfileIgmpProxyIpAddress_Object = MibTableColumn
msanMulticastProfileIgmpProxyIpAddress = _MsanMulticastProfileIgmpProxyIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 5, 1, 1, 8),
    _MsanMulticastProfileIgmpProxyIpAddress_Type()
)
msanMulticastProfileIgmpProxyIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanMulticastProfileIgmpProxyIpAddress.setStatus("current")


class _MsanMulticastProfileIgmpFiltering_Type(Integer32):
    """Custom type msanMulticastProfileIgmpFiltering based on Integer32"""
    defaultValue = 1

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
        *(("allowAll", 0),
          ("allowQueries", 2),
          ("allowReports", 1),
          ("dropAll", 3))
    )


_MsanMulticastProfileIgmpFiltering_Type.__name__ = "Integer32"
_MsanMulticastProfileIgmpFiltering_Object = MibTableColumn
msanMulticastProfileIgmpFiltering = _MsanMulticastProfileIgmpFiltering_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 5, 1, 1, 9),
    _MsanMulticastProfileIgmpFiltering_Type()
)
msanMulticastProfileIgmpFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanMulticastProfileIgmpFiltering.setStatus("current")


class _MsanMulticastProfileMulticastGroupLimit_Type(Unsigned32):
    """Custom type msanMulticastProfileMulticastGroupLimit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_MsanMulticastProfileMulticastGroupLimit_Type.__name__ = "Unsigned32"
_MsanMulticastProfileMulticastGroupLimit_Object = MibTableColumn
msanMulticastProfileMulticastGroupLimit = _MsanMulticastProfileMulticastGroupLimit_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 5, 1, 1, 10),
    _MsanMulticastProfileMulticastGroupLimit_Type()
)
msanMulticastProfileMulticastGroupLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanMulticastProfileMulticastGroupLimit.setStatus("current")


class _MsanMulticastProfileMvr_Type(Integer32):
    """Custom type msanMulticastProfileMvr based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_MsanMulticastProfileMvr_Type.__name__ = "Integer32"
_MsanMulticastProfileMvr_Object = MibTableColumn
msanMulticastProfileMvr = _MsanMulticastProfileMvr_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 5, 1, 1, 11),
    _MsanMulticastProfileMvr_Type()
)
msanMulticastProfileMvr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanMulticastProfileMvr.setStatus("current")


class _MsanMulticastProfileDescription_Type(OctetString):
    """Custom type msanMulticastProfileDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MsanMulticastProfileDescription_Type.__name__ = "OctetString"
_MsanMulticastProfileDescription_Object = MibTableColumn
msanMulticastProfileDescription = _MsanMulticastProfileDescription_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 5, 1, 1, 12),
    _MsanMulticastProfileDescription_Type()
)
msanMulticastProfileDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanMulticastProfileDescription.setStatus("current")
_MsanMulticastProfileRowStatus_Type = RowStatus
_MsanMulticastProfileRowStatus_Object = MibTableColumn
msanMulticastProfileRowStatus = _MsanMulticastProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 5, 1, 1, 13),
    _MsanMulticastProfileRowStatus_Type()
)
msanMulticastProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanMulticastProfileRowStatus.setStatus("current")
_MsanMulticastProfileStaticGroupTable_Object = MibTable
msanMulticastProfileStaticGroupTable = _MsanMulticastProfileStaticGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 5, 2)
)
if mibBuilder.loadTexts:
    msanMulticastProfileStaticGroupTable.setStatus("current")
_MsanMulticastProfileStaticGroupEntry_Object = MibTableRow
msanMulticastProfileStaticGroupEntry = _MsanMulticastProfileStaticGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 5, 2, 1)
)
msanMulticastProfileStaticGroupEntry.setIndexNames(
    (0, "ISKRATEL-MSAN-MIB", "msanMulticastProfileName"),
    (0, "ISKRATEL-MSAN-MIB", "msanMulticastProfileStaticGroupIpAddr"),
)
if mibBuilder.loadTexts:
    msanMulticastProfileStaticGroupEntry.setStatus("current")
_MsanMulticastProfileStaticGroupIpAddr_Type = IpAddress
_MsanMulticastProfileStaticGroupIpAddr_Object = MibTableColumn
msanMulticastProfileStaticGroupIpAddr = _MsanMulticastProfileStaticGroupIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 5, 2, 1, 1),
    _MsanMulticastProfileStaticGroupIpAddr_Type()
)
msanMulticastProfileStaticGroupIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanMulticastProfileStaticGroupIpAddr.setStatus("current")
_MsanMulticastProfileStaticGroupRowStatus_Type = RowStatus
_MsanMulticastProfileStaticGroupRowStatus_Object = MibTableColumn
msanMulticastProfileStaticGroupRowStatus = _MsanMulticastProfileStaticGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 5, 2, 1, 9),
    _MsanMulticastProfileStaticGroupRowStatus_Type()
)
msanMulticastProfileStaticGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanMulticastProfileStaticGroupRowStatus.setStatus("current")
_MsanSecurityProfile_ObjectIdentity = ObjectIdentity
msanSecurityProfile = _MsanSecurityProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 6)
)
_MsanSecurityProfileTable_Object = MibTable
msanSecurityProfileTable = _MsanSecurityProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 6, 1)
)
if mibBuilder.loadTexts:
    msanSecurityProfileTable.setStatus("current")
_MsanSecurityProfileEntry_Object = MibTableRow
msanSecurityProfileEntry = _MsanSecurityProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 6, 1, 1)
)
msanSecurityProfileEntry.setIndexNames(
    (0, "ISKRATEL-MSAN-MIB", "msanSecurityProfileName"),
)
if mibBuilder.loadTexts:
    msanSecurityProfileEntry.setStatus("current")


class _MsanSecurityProfileName_Type(OctetString):
    """Custom type msanSecurityProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MsanSecurityProfileName_Type.__name__ = "OctetString"
_MsanSecurityProfileName_Object = MibTableColumn
msanSecurityProfileName = _MsanSecurityProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 6, 1, 1, 1),
    _MsanSecurityProfileName_Type()
)
msanSecurityProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanSecurityProfileName.setStatus("current")


class _MsanSecurityProfileProtection_Type(Integer32):
    """Custom type msanSecurityProfileProtection based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("protected", 1),
          ("unprotected", 0))
    )


_MsanSecurityProfileProtection_Type.__name__ = "Integer32"
_MsanSecurityProfileProtection_Object = MibTableColumn
msanSecurityProfileProtection = _MsanSecurityProfileProtection_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 6, 1, 1, 2),
    _MsanSecurityProfileProtection_Type()
)
msanSecurityProfileProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanSecurityProfileProtection.setStatus("current")


class _MsanSecurityProfileStatus_Type(Integer32):
    """Custom type msanSecurityProfileStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_MsanSecurityProfileStatus_Type.__name__ = "Integer32"
_MsanSecurityProfileStatus_Object = MibTableColumn
msanSecurityProfileStatus = _MsanSecurityProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 6, 1, 1, 3),
    _MsanSecurityProfileStatus_Type()
)
msanSecurityProfileStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanSecurityProfileStatus.setStatus("current")


class _MsanSecurityProfileProtectedPort_Type(Integer32):
    """Custom type msanSecurityProfileProtectedPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_MsanSecurityProfileProtectedPort_Type.__name__ = "Integer32"
_MsanSecurityProfileProtectedPort_Object = MibTableColumn
msanSecurityProfileProtectedPort = _MsanSecurityProfileProtectedPort_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 6, 1, 1, 4),
    _MsanSecurityProfileProtectedPort_Type()
)
msanSecurityProfileProtectedPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanSecurityProfileProtectedPort.setStatus("current")


class _MsanSecurityProfileMacSg_Type(Integer32):
    """Custom type msanSecurityProfileMacSg based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_MsanSecurityProfileMacSg_Type.__name__ = "Integer32"
_MsanSecurityProfileMacSg_Object = MibTableColumn
msanSecurityProfileMacSg = _MsanSecurityProfileMacSg_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 6, 1, 1, 5),
    _MsanSecurityProfileMacSg_Type()
)
msanSecurityProfileMacSg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanSecurityProfileMacSg.setStatus("current")


class _MsanSecurityProfileMacLimit_Type(Unsigned32):
    """Custom type msanSecurityProfileMacLimit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_MsanSecurityProfileMacLimit_Type.__name__ = "Unsigned32"
_MsanSecurityProfileMacLimit_Object = MibTableColumn
msanSecurityProfileMacLimit = _MsanSecurityProfileMacLimit_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 6, 1, 1, 6),
    _MsanSecurityProfileMacLimit_Type()
)
msanSecurityProfileMacLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanSecurityProfileMacLimit.setStatus("current")


class _MsanSecurityProfilePortSecurity_Type(Integer32):
    """Custom type msanSecurityProfilePortSecurity based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_MsanSecurityProfilePortSecurity_Type.__name__ = "Integer32"
_MsanSecurityProfilePortSecurity_Object = MibTableColumn
msanSecurityProfilePortSecurity = _MsanSecurityProfilePortSecurity_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 6, 1, 1, 7),
    _MsanSecurityProfilePortSecurity_Type()
)
msanSecurityProfilePortSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanSecurityProfilePortSecurity.setStatus("current")


class _MsanSecurityProfileIpSg_Type(Integer32):
    """Custom type msanSecurityProfileIpSg based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_MsanSecurityProfileIpSg_Type.__name__ = "Integer32"
_MsanSecurityProfileIpSg_Object = MibTableColumn
msanSecurityProfileIpSg = _MsanSecurityProfileIpSg_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 6, 1, 1, 8),
    _MsanSecurityProfileIpSg_Type()
)
msanSecurityProfileIpSg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanSecurityProfileIpSg.setStatus("current")


class _MsanSecurityProfileIpSgBindingLimit_Type(Unsigned32):
    """Custom type msanSecurityProfileIpSgBindingLimit based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_MsanSecurityProfileIpSgBindingLimit_Type.__name__ = "Unsigned32"
_MsanSecurityProfileIpSgBindingLimit_Object = MibTableColumn
msanSecurityProfileIpSgBindingLimit = _MsanSecurityProfileIpSgBindingLimit_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 6, 1, 1, 9),
    _MsanSecurityProfileIpSgBindingLimit_Type()
)
msanSecurityProfileIpSgBindingLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanSecurityProfileIpSgBindingLimit.setStatus("current")


class _MsanSecurityProfileIpSgFilteringMode_Type(Integer32):
    """Custom type msanSecurityProfileIpSgFilteringMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipAndMacSourceAddress", 2),
          ("ipSourceAddress", 1))
    )


_MsanSecurityProfileIpSgFilteringMode_Type.__name__ = "Integer32"
_MsanSecurityProfileIpSgFilteringMode_Object = MibTableColumn
msanSecurityProfileIpSgFilteringMode = _MsanSecurityProfileIpSgFilteringMode_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 6, 1, 1, 10),
    _MsanSecurityProfileIpSgFilteringMode_Type()
)
msanSecurityProfileIpSgFilteringMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanSecurityProfileIpSgFilteringMode.setStatus("current")


class _MsanSecurityProfileArpInspec_Type(Integer32):
    """Custom type msanSecurityProfileArpInspec based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_MsanSecurityProfileArpInspec_Type.__name__ = "Integer32"
_MsanSecurityProfileArpInspec_Object = MibTableColumn
msanSecurityProfileArpInspec = _MsanSecurityProfileArpInspec_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 6, 1, 1, 12),
    _MsanSecurityProfileArpInspec_Type()
)
msanSecurityProfileArpInspec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanSecurityProfileArpInspec.setStatus("current")


class _MsanSecurityProfileMacForward_Type(Integer32):
    """Custom type msanSecurityProfileMacForward based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_MsanSecurityProfileMacForward_Type.__name__ = "Integer32"
_MsanSecurityProfileMacForward_Object = MibTableColumn
msanSecurityProfileMacForward = _MsanSecurityProfileMacForward_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 6, 1, 1, 13),
    _MsanSecurityProfileMacForward_Type()
)
msanSecurityProfileMacForward.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanSecurityProfileMacForward.setStatus("current")


class _MsanSecurityProfileDescription_Type(OctetString):
    """Custom type msanSecurityProfileDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MsanSecurityProfileDescription_Type.__name__ = "OctetString"
_MsanSecurityProfileDescription_Object = MibTableColumn
msanSecurityProfileDescription = _MsanSecurityProfileDescription_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 6, 1, 1, 14),
    _MsanSecurityProfileDescription_Type()
)
msanSecurityProfileDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanSecurityProfileDescription.setStatus("current")
_MsanSecurityProfileRowStatus_Type = RowStatus
_MsanSecurityProfileRowStatus_Object = MibTableColumn
msanSecurityProfileRowStatus = _MsanSecurityProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 6, 1, 1, 15),
    _MsanSecurityProfileRowStatus_Type()
)
msanSecurityProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanSecurityProfileRowStatus.setStatus("current")
_MsanSecurityAclProfileTable_Object = MibTable
msanSecurityAclProfileTable = _MsanSecurityAclProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 6, 3)
)
if mibBuilder.loadTexts:
    msanSecurityAclProfileTable.setStatus("current")
_MsanSecurityAclProfileEntry_Object = MibTableRow
msanSecurityAclProfileEntry = _MsanSecurityAclProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 6, 3, 1)
)
msanSecurityAclProfileEntry.setIndexNames(
    (0, "ISKRATEL-MSAN-MIB", "msanSecurityProfileName"),
    (0, "ISKRATEL-MSAN-MIB", "msanSecurityAclProfileAclDirection"),
    (0, "ISKRATEL-MSAN-MIB", "msanSecurityAclProfileSequence"),
    (0, "ISKRATEL-MSAN-MIB", "msanSecurityAclProfileAclType"),
    (0, "ISKRATEL-MSAN-MIB", "msanSecurityAclProfileAclId"),
)
if mibBuilder.loadTexts:
    msanSecurityAclProfileEntry.setStatus("current")


class _MsanSecurityAclProfileAclDirection_Type(Integer32):
    """Custom type msanSecurityAclProfileAclDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )


_MsanSecurityAclProfileAclDirection_Type.__name__ = "Integer32"
_MsanSecurityAclProfileAclDirection_Object = MibTableColumn
msanSecurityAclProfileAclDirection = _MsanSecurityAclProfileAclDirection_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 6, 3, 1, 1),
    _MsanSecurityAclProfileAclDirection_Type()
)
msanSecurityAclProfileAclDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanSecurityAclProfileAclDirection.setStatus("current")


class _MsanSecurityAclProfileSequence_Type(Unsigned32):
    """Custom type msanSecurityAclProfileSequence based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_MsanSecurityAclProfileSequence_Type.__name__ = "Unsigned32"
_MsanSecurityAclProfileSequence_Object = MibTableColumn
msanSecurityAclProfileSequence = _MsanSecurityAclProfileSequence_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 6, 3, 1, 2),
    _MsanSecurityAclProfileSequence_Type()
)
msanSecurityAclProfileSequence.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanSecurityAclProfileSequence.setStatus("current")


class _MsanSecurityAclProfileAclType_Type(Integer32):
    """Custom type msanSecurityAclProfileAclType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ip", 1),
          ("mac", 2))
    )


_MsanSecurityAclProfileAclType_Type.__name__ = "Integer32"
_MsanSecurityAclProfileAclType_Object = MibTableColumn
msanSecurityAclProfileAclType = _MsanSecurityAclProfileAclType_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 6, 3, 1, 3),
    _MsanSecurityAclProfileAclType_Type()
)
msanSecurityAclProfileAclType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanSecurityAclProfileAclType.setStatus("current")
_MsanSecurityAclProfileAclId_Type = Unsigned32
_MsanSecurityAclProfileAclId_Object = MibTableColumn
msanSecurityAclProfileAclId = _MsanSecurityAclProfileAclId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 6, 3, 1, 4),
    _MsanSecurityAclProfileAclId_Type()
)
msanSecurityAclProfileAclId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanSecurityAclProfileAclId.setStatus("current")
_MsanSecurityAclProfileRowStatus_Type = RowStatus
_MsanSecurityAclProfileRowStatus_Object = MibTableColumn
msanSecurityAclProfileRowStatus = _MsanSecurityAclProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 6, 3, 1, 5),
    _MsanSecurityAclProfileRowStatus_Type()
)
msanSecurityAclProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanSecurityAclProfileRowStatus.setStatus("current")
_MsanL2cpProfile_ObjectIdentity = ObjectIdentity
msanL2cpProfile = _MsanL2cpProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 7)
)
_MsanL2cpProfileTable_Object = MibTable
msanL2cpProfileTable = _MsanL2cpProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 7, 1)
)
if mibBuilder.loadTexts:
    msanL2cpProfileTable.setStatus("current")
_MsanL2cpProfileEntry_Object = MibTableRow
msanL2cpProfileEntry = _MsanL2cpProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 7, 1, 1)
)
msanL2cpProfileEntry.setIndexNames(
    (0, "ISKRATEL-MSAN-MIB", "msanL2cpProfileName"),
)
if mibBuilder.loadTexts:
    msanL2cpProfileEntry.setStatus("current")


class _MsanL2cpProfileName_Type(OctetString):
    """Custom type msanL2cpProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MsanL2cpProfileName_Type.__name__ = "OctetString"
_MsanL2cpProfileName_Object = MibTableColumn
msanL2cpProfileName = _MsanL2cpProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 7, 1, 1, 1),
    _MsanL2cpProfileName_Type()
)
msanL2cpProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanL2cpProfileName.setStatus("current")


class _MsanL2cpProfileProtection_Type(Integer32):
    """Custom type msanL2cpProfileProtection based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("protected", 1),
          ("unprotected", 0))
    )


_MsanL2cpProfileProtection_Type.__name__ = "Integer32"
_MsanL2cpProfileProtection_Object = MibTableColumn
msanL2cpProfileProtection = _MsanL2cpProfileProtection_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 7, 1, 1, 2),
    _MsanL2cpProfileProtection_Type()
)
msanL2cpProfileProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanL2cpProfileProtection.setStatus("current")


class _MsanL2cpProfileStatus_Type(Integer32):
    """Custom type msanL2cpProfileStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_MsanL2cpProfileStatus_Type.__name__ = "Integer32"
_MsanL2cpProfileStatus_Object = MibTableColumn
msanL2cpProfileStatus = _MsanL2cpProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 7, 1, 1, 3),
    _MsanL2cpProfileStatus_Type()
)
msanL2cpProfileStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanL2cpProfileStatus.setStatus("current")


class _MsanL2cpProfileDescription_Type(OctetString):
    """Custom type msanL2cpProfileDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MsanL2cpProfileDescription_Type.__name__ = "OctetString"
_MsanL2cpProfileDescription_Object = MibTableColumn
msanL2cpProfileDescription = _MsanL2cpProfileDescription_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 7, 1, 1, 4),
    _MsanL2cpProfileDescription_Type()
)
msanL2cpProfileDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanL2cpProfileDescription.setStatus("current")
_MsanL2cpProfileRowStatus_Type = RowStatus
_MsanL2cpProfileRowStatus_Object = MibTableColumn
msanL2cpProfileRowStatus = _MsanL2cpProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 7, 1, 1, 5),
    _MsanL2cpProfileRowStatus_Type()
)
msanL2cpProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanL2cpProfileRowStatus.setStatus("current")
_MsanL2cpProtocolTable_Object = MibTable
msanL2cpProtocolTable = _MsanL2cpProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 7, 2)
)
if mibBuilder.loadTexts:
    msanL2cpProtocolTable.setStatus("current")
_MsanL2cpProtocolEntry_Object = MibTableRow
msanL2cpProtocolEntry = _MsanL2cpProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 7, 2, 1)
)
msanL2cpProtocolEntry.setIndexNames(
    (0, "ISKRATEL-MSAN-MIB", "msanL2cpProtocolName"),
)
if mibBuilder.loadTexts:
    msanL2cpProtocolEntry.setStatus("current")


class _MsanL2cpProtocolName_Type(OctetString):
    """Custom type msanL2cpProtocolName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MsanL2cpProtocolName_Type.__name__ = "OctetString"
_MsanL2cpProtocolName_Object = MibTableColumn
msanL2cpProtocolName = _MsanL2cpProtocolName_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 7, 2, 1, 1),
    _MsanL2cpProtocolName_Type()
)
msanL2cpProtocolName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanL2cpProtocolName.setStatus("current")


class _MsanL2cpProtocolMacDestAddr_Type(MacAddress):
    """Custom type msanL2cpProtocolMacDestAddr based on MacAddress"""
    defaultHexValue = ""


_MsanL2cpProtocolMacDestAddr_Object = MibTableColumn
msanL2cpProtocolMacDestAddr = _MsanL2cpProtocolMacDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 7, 2, 1, 2),
    _MsanL2cpProtocolMacDestAddr_Type()
)
msanL2cpProtocolMacDestAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanL2cpProtocolMacDestAddr.setStatus("current")


class _MsanL2cpProtocolEthertype_Type(Integer32):
    """Custom type msanL2cpProtocolEthertype based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_MsanL2cpProtocolEthertype_Type.__name__ = "Integer32"
_MsanL2cpProtocolEthertype_Object = MibTableColumn
msanL2cpProtocolEthertype = _MsanL2cpProtocolEthertype_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 7, 2, 1, 3),
    _MsanL2cpProtocolEthertype_Type()
)
msanL2cpProtocolEthertype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanL2cpProtocolEthertype.setStatus("current")


class _MsanL2cpProtocolSubtype_Type(Integer32):
    """Custom type msanL2cpProtocolSubtype based on Integer32"""
    defaultValue = -1


_MsanL2cpProtocolSubtype_Object = MibTableColumn
msanL2cpProtocolSubtype = _MsanL2cpProtocolSubtype_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 7, 2, 1, 4),
    _MsanL2cpProtocolSubtype_Type()
)
msanL2cpProtocolSubtype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanL2cpProtocolSubtype.setStatus("current")
_MsanL2cpProtocolRowStatus_Type = RowStatus
_MsanL2cpProtocolRowStatus_Object = MibTableColumn
msanL2cpProtocolRowStatus = _MsanL2cpProtocolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 7, 2, 1, 5),
    _MsanL2cpProtocolRowStatus_Type()
)
msanL2cpProtocolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanL2cpProtocolRowStatus.setStatus("current")
_MsanL2cpProfileProtocolTable_Object = MibTable
msanL2cpProfileProtocolTable = _MsanL2cpProfileProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 7, 3)
)
if mibBuilder.loadTexts:
    msanL2cpProfileProtocolTable.setStatus("current")
_MsanL2cpProfileProtocolEntry_Object = MibTableRow
msanL2cpProfileProtocolEntry = _MsanL2cpProfileProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 7, 3, 1)
)
msanL2cpProfileProtocolEntry.setIndexNames(
    (0, "ISKRATEL-MSAN-MIB", "msanL2cpProfileName"),
    (0, "ISKRATEL-MSAN-MIB", "msanL2cpProtocolName"),
)
if mibBuilder.loadTexts:
    msanL2cpProfileProtocolEntry.setStatus("current")


class _MsanL2cpProfileProtocolRule_Type(Integer32):
    """Custom type msanL2cpProfileProtocolRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discard", 1),
          ("peer", 2),
          ("tunnel", 3))
    )


_MsanL2cpProfileProtocolRule_Type.__name__ = "Integer32"
_MsanL2cpProfileProtocolRule_Object = MibTableColumn
msanL2cpProfileProtocolRule = _MsanL2cpProfileProtocolRule_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 7, 3, 1, 1),
    _MsanL2cpProfileProtocolRule_Type()
)
msanL2cpProfileProtocolRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanL2cpProfileProtocolRule.setStatus("current")
_MsanL2cpProfileProtocolRowStatus_Type = RowStatus
_MsanL2cpProfileProtocolRowStatus_Object = MibTableColumn
msanL2cpProfileProtocolRowStatus = _MsanL2cpProfileProtocolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 7, 3, 1, 2),
    _MsanL2cpProfileProtocolRowStatus_Type()
)
msanL2cpProfileProtocolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanL2cpProfileProtocolRowStatus.setStatus("current")
_MsanL2cpProfileVlanTable_Object = MibTable
msanL2cpProfileVlanTable = _MsanL2cpProfileVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 7, 4)
)
if mibBuilder.loadTexts:
    msanL2cpProfileVlanTable.setStatus("current")
_MsanL2cpProfileVlanEntry_Object = MibTableRow
msanL2cpProfileVlanEntry = _MsanL2cpProfileVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 7, 4, 1)
)
msanL2cpProfileVlanEntry.setIndexNames(
    (0, "ISKRATEL-MSAN-MIB", "msanL2cpProfileName"),
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    msanL2cpProfileVlanEntry.setStatus("current")
_MsanL2cpProfileVlanRowStatus_Type = RowStatus
_MsanL2cpProfileVlanRowStatus_Object = MibTableColumn
msanL2cpProfileVlanRowStatus = _MsanL2cpProfileVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 7, 4, 1, 1),
    _MsanL2cpProfileVlanRowStatus_Type()
)
msanL2cpProfileVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanL2cpProfileVlanRowStatus.setStatus("current")
_MsanXdslProfile_ObjectIdentity = ObjectIdentity
msanXdslProfile = _MsanXdslProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 8)
)
_MsanXdsl2LineConfTemplateTable_Object = MibTable
msanXdsl2LineConfTemplateTable = _MsanXdsl2LineConfTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 8, 1)
)
if mibBuilder.loadTexts:
    msanXdsl2LineConfTemplateTable.setStatus("current")
_MsanXdsl2LineConfTemplateEntry_Object = MibTableRow
msanXdsl2LineConfTemplateEntry = _MsanXdsl2LineConfTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 8, 1, 1)
)
if mibBuilder.loadTexts:
    msanXdsl2LineConfTemplateEntry.setStatus("current")


class _MsanXdsl2LineConfTempProtection_Type(Integer32):
    """Custom type msanXdsl2LineConfTempProtection based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("protected", 1),
          ("unprotected", 0))
    )


_MsanXdsl2LineConfTempProtection_Type.__name__ = "Integer32"
_MsanXdsl2LineConfTempProtection_Object = MibTableColumn
msanXdsl2LineConfTempProtection = _MsanXdsl2LineConfTempProtection_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 8, 1, 1, 1),
    _MsanXdsl2LineConfTempProtection_Type()
)
msanXdsl2LineConfTempProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanXdsl2LineConfTempProtection.setStatus("current")


class _MsanXdsl2LineConfTempStatus_Type(Integer32):
    """Custom type msanXdsl2LineConfTempStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_MsanXdsl2LineConfTempStatus_Type.__name__ = "Integer32"
_MsanXdsl2LineConfTempStatus_Object = MibTableColumn
msanXdsl2LineConfTempStatus = _MsanXdsl2LineConfTempStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 8, 1, 1, 2),
    _MsanXdsl2LineConfTempStatus_Type()
)
msanXdsl2LineConfTempStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanXdsl2LineConfTempStatus.setStatus("current")
_MsanXdsl2LineAlarmConfTemplateTable_Object = MibTable
msanXdsl2LineAlarmConfTemplateTable = _MsanXdsl2LineAlarmConfTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 8, 2)
)
if mibBuilder.loadTexts:
    msanXdsl2LineAlarmConfTemplateTable.setStatus("current")
_MsanXdsl2LineAlarmConfTemplateEntry_Object = MibTableRow
msanXdsl2LineAlarmConfTemplateEntry = _MsanXdsl2LineAlarmConfTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 8, 2, 1)
)
if mibBuilder.loadTexts:
    msanXdsl2LineAlarmConfTemplateEntry.setStatus("current")


class _MsanXdsl2LineAlarmConfTempProtection_Type(Integer32):
    """Custom type msanXdsl2LineAlarmConfTempProtection based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("protected", 1),
          ("unprotected", 0))
    )


_MsanXdsl2LineAlarmConfTempProtection_Type.__name__ = "Integer32"
_MsanXdsl2LineAlarmConfTempProtection_Object = MibTableColumn
msanXdsl2LineAlarmConfTempProtection = _MsanXdsl2LineAlarmConfTempProtection_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 8, 2, 1, 1),
    _MsanXdsl2LineAlarmConfTempProtection_Type()
)
msanXdsl2LineAlarmConfTempProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanXdsl2LineAlarmConfTempProtection.setStatus("current")


class _MsanXdsl2LineAlarmConfTempStatus_Type(Integer32):
    """Custom type msanXdsl2LineAlarmConfTempStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_MsanXdsl2LineAlarmConfTempStatus_Type.__name__ = "Integer32"
_MsanXdsl2LineAlarmConfTempStatus_Object = MibTableColumn
msanXdsl2LineAlarmConfTempStatus = _MsanXdsl2LineAlarmConfTempStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 8, 2, 1, 2),
    _MsanXdsl2LineAlarmConfTempStatus_Type()
)
msanXdsl2LineAlarmConfTempStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanXdsl2LineAlarmConfTempStatus.setStatus("current")


class _MsanProfileConfigStatus_Type(Integer32):
    """Custom type msanProfileConfigStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanProfileConfigStatus_Type.__name__ = "Integer32"
_MsanProfileConfigStatus_Object = MibScalar
msanProfileConfigStatus = _MsanProfileConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 3, 100),
    _MsanProfileConfigStatus_Type()
)
msanProfileConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanProfileConfigStatus.setStatus("current")
_MsanDhcpRelay_ObjectIdentity = ObjectIdentity
msanDhcpRelay = _MsanDhcpRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4)
)
_MsanDhcpRaGlobal_ObjectIdentity = ObjectIdentity
msanDhcpRaGlobal = _MsanDhcpRaGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 1)
)


class _MsanDhcpRaStatus_Type(Integer32):
    """Custom type msanDhcpRaStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanDhcpRaStatus_Type.__name__ = "Integer32"
_MsanDhcpRaStatus_Object = MibScalar
msanDhcpRaStatus = _MsanDhcpRaStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 1, 1),
    _MsanDhcpRaStatus_Type()
)
msanDhcpRaStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDhcpRaStatus.setStatus("current")


class _MsanDhcpRaMode_Type(Integer32):
    """Custom type msanDhcpRaMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("simplified", 2))
    )


_MsanDhcpRaMode_Type.__name__ = "Integer32"
_MsanDhcpRaMode_Object = MibScalar
msanDhcpRaMode = _MsanDhcpRaMode_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 1, 2),
    _MsanDhcpRaMode_Type()
)
msanDhcpRaMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDhcpRaMode.setStatus("current")


class _MsanDhcpRaCircuitType_Type(Integer32):
    """Custom type msanDhcpRaCircuitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("trusted", 1),
          ("untrusted", 2))
    )


_MsanDhcpRaCircuitType_Type.__name__ = "Integer32"
_MsanDhcpRaCircuitType_Object = MibScalar
msanDhcpRaCircuitType = _MsanDhcpRaCircuitType_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 1, 3),
    _MsanDhcpRaCircuitType_Type()
)
msanDhcpRaCircuitType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDhcpRaCircuitType.setStatus("current")


class _MsanDhcpRaOpt82_Type(Integer32):
    """Custom type msanDhcpRaOpt82 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanDhcpRaOpt82_Type.__name__ = "Integer32"
_MsanDhcpRaOpt82_Object = MibScalar
msanDhcpRaOpt82 = _MsanDhcpRaOpt82_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 1, 4),
    _MsanDhcpRaOpt82_Type()
)
msanDhcpRaOpt82.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDhcpRaOpt82.setStatus("current")


class _MsanDhcpRaOpt82ReplyMode_Type(Integer32):
    """Custom type msanDhcpRaOpt82ReplyMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("keep", 1),
          ("remove", 2))
    )


_MsanDhcpRaOpt82ReplyMode_Type.__name__ = "Integer32"
_MsanDhcpRaOpt82ReplyMode_Object = MibScalar
msanDhcpRaOpt82ReplyMode = _MsanDhcpRaOpt82ReplyMode_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 1, 5),
    _MsanDhcpRaOpt82ReplyMode_Type()
)
msanDhcpRaOpt82ReplyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDhcpRaOpt82ReplyMode.setStatus("current")


class _MsanDhcpRaOpt82CircuitIdStatus_Type(Integer32):
    """Custom type msanDhcpRaOpt82CircuitIdStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanDhcpRaOpt82CircuitIdStatus_Type.__name__ = "Integer32"
_MsanDhcpRaOpt82CircuitIdStatus_Object = MibScalar
msanDhcpRaOpt82CircuitIdStatus = _MsanDhcpRaOpt82CircuitIdStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 1, 6),
    _MsanDhcpRaOpt82CircuitIdStatus_Type()
)
msanDhcpRaOpt82CircuitIdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDhcpRaOpt82CircuitIdStatus.setStatus("current")


class _MsanDhcpRaOpt82RemoteIdStatus_Type(Integer32):
    """Custom type msanDhcpRaOpt82RemoteIdStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanDhcpRaOpt82RemoteIdStatus_Type.__name__ = "Integer32"
_MsanDhcpRaOpt82RemoteIdStatus_Object = MibScalar
msanDhcpRaOpt82RemoteIdStatus = _MsanDhcpRaOpt82RemoteIdStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 1, 7),
    _MsanDhcpRaOpt82RemoteIdStatus_Type()
)
msanDhcpRaOpt82RemoteIdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDhcpRaOpt82RemoteIdStatus.setStatus("current")


class _MsanDhcpRaOpt82UnicastExtStatus_Type(Integer32):
    """Custom type msanDhcpRaOpt82UnicastExtStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanDhcpRaOpt82UnicastExtStatus_Type.__name__ = "Integer32"
_MsanDhcpRaOpt82UnicastExtStatus_Object = MibScalar
msanDhcpRaOpt82UnicastExtStatus = _MsanDhcpRaOpt82UnicastExtStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 1, 8),
    _MsanDhcpRaOpt82UnicastExtStatus_Type()
)
msanDhcpRaOpt82UnicastExtStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDhcpRaOpt82UnicastExtStatus.setStatus("current")
_MsanDhcpRaFullModeSrvIpAddr_Type = IpAddress
_MsanDhcpRaFullModeSrvIpAddr_Object = MibScalar
msanDhcpRaFullModeSrvIpAddr = _MsanDhcpRaFullModeSrvIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 1, 9),
    _MsanDhcpRaFullModeSrvIpAddr_Type()
)
msanDhcpRaFullModeSrvIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDhcpRaFullModeSrvIpAddr.setStatus("current")
_MsanDhcpRaPortConfigTable_Object = MibTable
msanDhcpRaPortConfigTable = _MsanDhcpRaPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 2)
)
if mibBuilder.loadTexts:
    msanDhcpRaPortConfigTable.setStatus("current")
_MsanDhcpRaPortConfigEntry_Object = MibTableRow
msanDhcpRaPortConfigEntry = _MsanDhcpRaPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 2, 1)
)
msanDhcpRaPortConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    msanDhcpRaPortConfigEntry.setStatus("current")


class _MsanDhcpRaPortState_Type(Integer32):
    """Custom type msanDhcpRaPortState based on Integer32"""
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
        *(("disable", 4),
          ("enable", 1),
          ("enableCli", 2),
          ("enableSrv", 3))
    )


_MsanDhcpRaPortState_Type.__name__ = "Integer32"
_MsanDhcpRaPortState_Object = MibTableColumn
msanDhcpRaPortState = _MsanDhcpRaPortState_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 2, 1, 1),
    _MsanDhcpRaPortState_Type()
)
msanDhcpRaPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDhcpRaPortState.setStatus("current")
_MsanDhcpRaPortCircuitId_Type = OctetString
_MsanDhcpRaPortCircuitId_Object = MibTableColumn
msanDhcpRaPortCircuitId = _MsanDhcpRaPortCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 2, 1, 2),
    _MsanDhcpRaPortCircuitId_Type()
)
msanDhcpRaPortCircuitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDhcpRaPortCircuitId.setStatus("current")
_MsanDhcpRaPortRemoteId_Type = OctetString
_MsanDhcpRaPortRemoteId_Object = MibTableColumn
msanDhcpRaPortRemoteId = _MsanDhcpRaPortRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 2, 1, 3),
    _MsanDhcpRaPortRemoteId_Type()
)
msanDhcpRaPortRemoteId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDhcpRaPortRemoteId.setStatus("current")


class _MsanDhcpRaPortMeter_Type(Integer32):
    """Custom type msanDhcpRaPortMeter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanDhcpRaPortMeter_Type.__name__ = "Integer32"
_MsanDhcpRaPortMeter_Object = MibTableColumn
msanDhcpRaPortMeter = _MsanDhcpRaPortMeter_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 2, 1, 4),
    _MsanDhcpRaPortMeter_Type()
)
msanDhcpRaPortMeter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDhcpRaPortMeter.setStatus("current")
_MsanDhcpRaPortMaxDataRate_Type = Integer32
_MsanDhcpRaPortMaxDataRate_Object = MibTableColumn
msanDhcpRaPortMaxDataRate = _MsanDhcpRaPortMaxDataRate_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 2, 1, 5),
    _MsanDhcpRaPortMaxDataRate_Type()
)
msanDhcpRaPortMaxDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDhcpRaPortMaxDataRate.setStatus("current")
if mibBuilder.loadTexts:
    msanDhcpRaPortMaxDataRate.setUnits("kb/s")


class _MsanDhcpRaPortCircuitType_Type(Integer32):
    """Custom type msanDhcpRaPortCircuitType based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notConfigured", 3),
          ("trusted", 1),
          ("untrusted", 2))
    )


_MsanDhcpRaPortCircuitType_Type.__name__ = "Integer32"
_MsanDhcpRaPortCircuitType_Object = MibTableColumn
msanDhcpRaPortCircuitType = _MsanDhcpRaPortCircuitType_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 2, 1, 6),
    _MsanDhcpRaPortCircuitType_Type()
)
msanDhcpRaPortCircuitType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDhcpRaPortCircuitType.setStatus("current")


class _MsanDhcpRaPortOpt82_Type(Integer32):
    """Custom type msanDhcpRaPortOpt82 based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("notConfigured", 3))
    )


_MsanDhcpRaPortOpt82_Type.__name__ = "Integer32"
_MsanDhcpRaPortOpt82_Object = MibTableColumn
msanDhcpRaPortOpt82 = _MsanDhcpRaPortOpt82_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 2, 1, 7),
    _MsanDhcpRaPortOpt82_Type()
)
msanDhcpRaPortOpt82.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDhcpRaPortOpt82.setStatus("current")


class _MsanDhcpRaPortOpt82ReplyMode_Type(Integer32):
    """Custom type msanDhcpRaPortOpt82ReplyMode based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("keep", 1),
          ("notConfigured", 3),
          ("remove", 2))
    )


_MsanDhcpRaPortOpt82ReplyMode_Type.__name__ = "Integer32"
_MsanDhcpRaPortOpt82ReplyMode_Object = MibTableColumn
msanDhcpRaPortOpt82ReplyMode = _MsanDhcpRaPortOpt82ReplyMode_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 2, 1, 8),
    _MsanDhcpRaPortOpt82ReplyMode_Type()
)
msanDhcpRaPortOpt82ReplyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDhcpRaPortOpt82ReplyMode.setStatus("current")


class _MsanDhcpRaPortOpt82UnicastExtStatus_Type(Integer32):
    """Custom type msanDhcpRaPortOpt82UnicastExtStatus based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("notConfigured", 3))
    )


_MsanDhcpRaPortOpt82UnicastExtStatus_Type.__name__ = "Integer32"
_MsanDhcpRaPortOpt82UnicastExtStatus_Object = MibTableColumn
msanDhcpRaPortOpt82UnicastExtStatus = _MsanDhcpRaPortOpt82UnicastExtStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 2, 1, 9),
    _MsanDhcpRaPortOpt82UnicastExtStatus_Type()
)
msanDhcpRaPortOpt82UnicastExtStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDhcpRaPortOpt82UnicastExtStatus.setStatus("current")


class _MsanDhcpRaPortCircuitIdType_Type(Integer32):
    """Custom type msanDhcpRaPortCircuitIdType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("iskratel", 1),
          ("standard", 2))
    )


_MsanDhcpRaPortCircuitIdType_Type.__name__ = "Integer32"
_MsanDhcpRaPortCircuitIdType_Object = MibTableColumn
msanDhcpRaPortCircuitIdType = _MsanDhcpRaPortCircuitIdType_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 2, 1, 10),
    _MsanDhcpRaPortCircuitIdType_Type()
)
msanDhcpRaPortCircuitIdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDhcpRaPortCircuitIdType.setStatus("current")
_MsanDhcpRaFullModeVlanTable_Object = MibTable
msanDhcpRaFullModeVlanTable = _MsanDhcpRaFullModeVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 3)
)
if mibBuilder.loadTexts:
    msanDhcpRaFullModeVlanTable.setStatus("current")
_MsanDhcpRaFullModeVlanEntry_Object = MibTableRow
msanDhcpRaFullModeVlanEntry = _MsanDhcpRaFullModeVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 3, 1)
)
msanDhcpRaFullModeVlanEntry.setIndexNames(
    (0, "ISKRATEL-MSAN-MIB", "msanDhcpRaFullModeVlanId"),
    (0, "ISKRATEL-MSAN-MIB", "msanDhcpRaFullModeVlanSrvIpAddr"),
)
if mibBuilder.loadTexts:
    msanDhcpRaFullModeVlanEntry.setStatus("current")


class _MsanDhcpRaFullModeVlanId_Type(Integer32):
    """Custom type msanDhcpRaFullModeVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_MsanDhcpRaFullModeVlanId_Type.__name__ = "Integer32"
_MsanDhcpRaFullModeVlanId_Object = MibTableColumn
msanDhcpRaFullModeVlanId = _MsanDhcpRaFullModeVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 3, 1, 1),
    _MsanDhcpRaFullModeVlanId_Type()
)
msanDhcpRaFullModeVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanDhcpRaFullModeVlanId.setStatus("current")
_MsanDhcpRaFullModeVlanSrvIpAddr_Type = IpAddress
_MsanDhcpRaFullModeVlanSrvIpAddr_Object = MibTableColumn
msanDhcpRaFullModeVlanSrvIpAddr = _MsanDhcpRaFullModeVlanSrvIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 3, 1, 2),
    _MsanDhcpRaFullModeVlanSrvIpAddr_Type()
)
msanDhcpRaFullModeVlanSrvIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanDhcpRaFullModeVlanSrvIpAddr.setStatus("current")
_MsanDhcpRaFullModeVlanRowStatus_Type = RowStatus
_MsanDhcpRaFullModeVlanRowStatus_Object = MibTableColumn
msanDhcpRaFullModeVlanRowStatus = _MsanDhcpRaFullModeVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 3, 1, 3),
    _MsanDhcpRaFullModeVlanRowStatus_Type()
)
msanDhcpRaFullModeVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanDhcpRaFullModeVlanRowStatus.setStatus("current")
_MsanDhcpRaStatTable_Object = MibTable
msanDhcpRaStatTable = _MsanDhcpRaStatTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 5)
)
if mibBuilder.loadTexts:
    msanDhcpRaStatTable.setStatus("current")
_MsanDhcpRaStatEntry_Object = MibTableRow
msanDhcpRaStatEntry = _MsanDhcpRaStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 5, 1)
)
msanDhcpRaStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    msanDhcpRaStatEntry.setStatus("current")
_MsanDhcpRaStatDiscover_Type = Counter32
_MsanDhcpRaStatDiscover_Object = MibTableColumn
msanDhcpRaStatDiscover = _MsanDhcpRaStatDiscover_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 5, 1, 1),
    _MsanDhcpRaStatDiscover_Type()
)
msanDhcpRaStatDiscover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDhcpRaStatDiscover.setStatus("current")
_MsanDhcpRaStatRequest_Type = Counter32
_MsanDhcpRaStatRequest_Object = MibTableColumn
msanDhcpRaStatRequest = _MsanDhcpRaStatRequest_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 5, 1, 2),
    _MsanDhcpRaStatRequest_Type()
)
msanDhcpRaStatRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDhcpRaStatRequest.setStatus("current")
_MsanDhcpRaStatOffer_Type = Counter32
_MsanDhcpRaStatOffer_Object = MibTableColumn
msanDhcpRaStatOffer = _MsanDhcpRaStatOffer_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 5, 1, 3),
    _MsanDhcpRaStatOffer_Type()
)
msanDhcpRaStatOffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDhcpRaStatOffer.setStatus("current")
_MsanDhcpRaStatACK_Type = Counter32
_MsanDhcpRaStatACK_Object = MibTableColumn
msanDhcpRaStatACK = _MsanDhcpRaStatACK_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 5, 1, 4),
    _MsanDhcpRaStatACK_Type()
)
msanDhcpRaStatACK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDhcpRaStatACK.setStatus("current")
_MsanDhcpRaStatNAK_Type = Counter32
_MsanDhcpRaStatNAK_Object = MibTableColumn
msanDhcpRaStatNAK = _MsanDhcpRaStatNAK_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 5, 1, 5),
    _MsanDhcpRaStatNAK_Type()
)
msanDhcpRaStatNAK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDhcpRaStatNAK.setStatus("current")
_MsanDhcpRaStatDecline_Type = Counter32
_MsanDhcpRaStatDecline_Object = MibTableColumn
msanDhcpRaStatDecline = _MsanDhcpRaStatDecline_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 5, 1, 6),
    _MsanDhcpRaStatDecline_Type()
)
msanDhcpRaStatDecline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDhcpRaStatDecline.setStatus("current")
_MsanDhcpRaStatMaxPacketSizeExceeded_Type = Counter32
_MsanDhcpRaStatMaxPacketSizeExceeded_Object = MibTableColumn
msanDhcpRaStatMaxPacketSizeExceeded = _MsanDhcpRaStatMaxPacketSizeExceeded_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 5, 1, 7),
    _MsanDhcpRaStatMaxPacketSizeExceeded_Type()
)
msanDhcpRaStatMaxPacketSizeExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDhcpRaStatMaxPacketSizeExceeded.setStatus("current")
_MsanDhcpRaStatFrameErr_Type = Counter32
_MsanDhcpRaStatFrameErr_Object = MibTableColumn
msanDhcpRaStatFrameErr = _MsanDhcpRaStatFrameErr_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 5, 1, 8),
    _MsanDhcpRaStatFrameErr_Type()
)
msanDhcpRaStatFrameErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDhcpRaStatFrameErr.setStatus("current")
_MsanDhcpRaStatOpt82Present_Type = Counter32
_MsanDhcpRaStatOpt82Present_Object = MibTableColumn
msanDhcpRaStatOpt82Present = _MsanDhcpRaStatOpt82Present_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 5, 1, 9),
    _MsanDhcpRaStatOpt82Present_Type()
)
msanDhcpRaStatOpt82Present.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDhcpRaStatOpt82Present.setStatus("current")
_MsanDhcpRaStatFrameUnsync_Type = Counter32
_MsanDhcpRaStatFrameUnsync_Object = MibTableColumn
msanDhcpRaStatFrameUnsync = _MsanDhcpRaStatFrameUnsync_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 5, 1, 10),
    _MsanDhcpRaStatFrameUnsync_Type()
)
msanDhcpRaStatFrameUnsync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDhcpRaStatFrameUnsync.setStatus("current")
_MsanDhcpRaStatRelease_Type = Counter32
_MsanDhcpRaStatRelease_Object = MibTableColumn
msanDhcpRaStatRelease = _MsanDhcpRaStatRelease_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 5, 1, 11),
    _MsanDhcpRaStatRelease_Type()
)
msanDhcpRaStatRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDhcpRaStatRelease.setStatus("current")
_MsanDhcpRaStatInform_Type = Counter32
_MsanDhcpRaStatInform_Object = MibTableColumn
msanDhcpRaStatInform = _MsanDhcpRaStatInform_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 5, 1, 12),
    _MsanDhcpRaStatInform_Type()
)
msanDhcpRaStatInform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDhcpRaStatInform.setStatus("current")
_MsanDhcpRaVlanConfigTable_Object = MibTable
msanDhcpRaVlanConfigTable = _MsanDhcpRaVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 6)
)
if mibBuilder.loadTexts:
    msanDhcpRaVlanConfigTable.setStatus("current")
_MsanDhcpRaVlanConfigEntry_Object = MibTableRow
msanDhcpRaVlanConfigEntry = _MsanDhcpRaVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 6, 1)
)
msanDhcpRaVlanConfigEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    msanDhcpRaVlanConfigEntry.setStatus("current")


class _MsanDhcpRaVlanState_Type(Integer32):
    """Custom type msanDhcpRaVlanState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("notConfigured", 2))
    )


_MsanDhcpRaVlanState_Type.__name__ = "Integer32"
_MsanDhcpRaVlanState_Object = MibTableColumn
msanDhcpRaVlanState = _MsanDhcpRaVlanState_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 6, 1, 1),
    _MsanDhcpRaVlanState_Type()
)
msanDhcpRaVlanState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDhcpRaVlanState.setStatus("current")


class _MsanDhcpRaVlanMode_Type(Integer32):
    """Custom type msanDhcpRaVlanMode based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("notConfigured", 3),
          ("simplified", 2))
    )


_MsanDhcpRaVlanMode_Type.__name__ = "Integer32"
_MsanDhcpRaVlanMode_Object = MibTableColumn
msanDhcpRaVlanMode = _MsanDhcpRaVlanMode_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 6, 1, 2),
    _MsanDhcpRaVlanMode_Type()
)
msanDhcpRaVlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDhcpRaVlanMode.setStatus("current")


class _MsanDhcpRaVlanOpt82_Type(Integer32):
    """Custom type msanDhcpRaVlanOpt82 based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("notConfigured", 3))
    )


_MsanDhcpRaVlanOpt82_Type.__name__ = "Integer32"
_MsanDhcpRaVlanOpt82_Object = MibTableColumn
msanDhcpRaVlanOpt82 = _MsanDhcpRaVlanOpt82_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 6, 1, 3),
    _MsanDhcpRaVlanOpt82_Type()
)
msanDhcpRaVlanOpt82.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDhcpRaVlanOpt82.setStatus("current")


class _MsanDhcpRaVlanOpt82ReplyMode_Type(Integer32):
    """Custom type msanDhcpRaVlanOpt82ReplyMode based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("keep", 1),
          ("notConfigured", 3),
          ("remove", 2))
    )


_MsanDhcpRaVlanOpt82ReplyMode_Type.__name__ = "Integer32"
_MsanDhcpRaVlanOpt82ReplyMode_Object = MibTableColumn
msanDhcpRaVlanOpt82ReplyMode = _MsanDhcpRaVlanOpt82ReplyMode_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 6, 1, 4),
    _MsanDhcpRaVlanOpt82ReplyMode_Type()
)
msanDhcpRaVlanOpt82ReplyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDhcpRaVlanOpt82ReplyMode.setStatus("current")


class _MsanDhcpRaVlanOpt82UnicastExtStatus_Type(Integer32):
    """Custom type msanDhcpRaVlanOpt82UnicastExtStatus based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("notConfigured", 3))
    )


_MsanDhcpRaVlanOpt82UnicastExtStatus_Type.__name__ = "Integer32"
_MsanDhcpRaVlanOpt82UnicastExtStatus_Object = MibTableColumn
msanDhcpRaVlanOpt82UnicastExtStatus = _MsanDhcpRaVlanOpt82UnicastExtStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 6, 1, 5),
    _MsanDhcpRaVlanOpt82UnicastExtStatus_Type()
)
msanDhcpRaVlanOpt82UnicastExtStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDhcpRaVlanOpt82UnicastExtStatus.setStatus("current")


class _MsanDhcpRaVlanCircuitIdType_Type(Integer32):
    """Custom type msanDhcpRaVlanCircuitIdType based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("iskratel", 1),
          ("notConfigured", 3),
          ("standard", 2))
    )


_MsanDhcpRaVlanCircuitIdType_Type.__name__ = "Integer32"
_MsanDhcpRaVlanCircuitIdType_Object = MibTableColumn
msanDhcpRaVlanCircuitIdType = _MsanDhcpRaVlanCircuitIdType_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 6, 1, 6),
    _MsanDhcpRaVlanCircuitIdType_Type()
)
msanDhcpRaVlanCircuitIdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDhcpRaVlanCircuitIdType.setStatus("current")
_MsanDhcpRaPortVlanConfigTable_Object = MibTable
msanDhcpRaPortVlanConfigTable = _MsanDhcpRaPortVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 7)
)
if mibBuilder.loadTexts:
    msanDhcpRaPortVlanConfigTable.setStatus("current")
_MsanDhcpRaPortVlanConfigEntry_Object = MibTableRow
msanDhcpRaPortVlanConfigEntry = _MsanDhcpRaPortVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 7, 1)
)
msanDhcpRaPortVlanConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    msanDhcpRaPortVlanConfigEntry.setStatus("current")
_MsanDhcpRaPortVlanRemoteId_Type = OctetString
_MsanDhcpRaPortVlanRemoteId_Object = MibTableColumn
msanDhcpRaPortVlanRemoteId = _MsanDhcpRaPortVlanRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 7, 1, 1),
    _MsanDhcpRaPortVlanRemoteId_Type()
)
msanDhcpRaPortVlanRemoteId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDhcpRaPortVlanRemoteId.setStatus("current")
_MsanDhcpRaPortVlanConfigRowStatus_Type = RowStatus
_MsanDhcpRaPortVlanConfigRowStatus_Object = MibTableColumn
msanDhcpRaPortVlanConfigRowStatus = _MsanDhcpRaPortVlanConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 7, 1, 2),
    _MsanDhcpRaPortVlanConfigRowStatus_Type()
)
msanDhcpRaPortVlanConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanDhcpRaPortVlanConfigRowStatus.setStatus("current")
_MsanDhcpv6RaGlobal_ObjectIdentity = ObjectIdentity
msanDhcpv6RaGlobal = _MsanDhcpv6RaGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 100)
)


class _MsanDhcpv6RaState_Type(Integer32):
    """Custom type msanDhcpv6RaState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanDhcpv6RaState_Type.__name__ = "Integer32"
_MsanDhcpv6RaState_Object = MibScalar
msanDhcpv6RaState = _MsanDhcpv6RaState_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 100, 1),
    _MsanDhcpv6RaState_Type()
)
msanDhcpv6RaState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDhcpv6RaState.setStatus("current")


class _MsanDhcpv6RaMode_Type(Integer32):
    """Custom type msanDhcpv6RaMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ldra", 1)
    )


_MsanDhcpv6RaMode_Type.__name__ = "Integer32"
_MsanDhcpv6RaMode_Object = MibScalar
msanDhcpv6RaMode = _MsanDhcpv6RaMode_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 100, 2),
    _MsanDhcpv6RaMode_Type()
)
msanDhcpv6RaMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDhcpv6RaMode.setStatus("current")


class _MsanDhcpv6RaInterfaceIdStandard_Type(Integer32):
    """Custom type msanDhcpv6RaInterfaceIdStandard based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanDhcpv6RaInterfaceIdStandard_Type.__name__ = "Integer32"
_MsanDhcpv6RaInterfaceIdStandard_Object = MibScalar
msanDhcpv6RaInterfaceIdStandard = _MsanDhcpv6RaInterfaceIdStandard_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 100, 3),
    _MsanDhcpv6RaInterfaceIdStandard_Type()
)
msanDhcpv6RaInterfaceIdStandard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDhcpv6RaInterfaceIdStandard.setStatus("current")
_MsanDhcpv6Statistics_ObjectIdentity = ObjectIdentity
msanDhcpv6Statistics = _MsanDhcpv6Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 101)
)
_MsanDhcpv6RaPortStatTable_Object = MibTable
msanDhcpv6RaPortStatTable = _MsanDhcpv6RaPortStatTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 101, 1)
)
if mibBuilder.loadTexts:
    msanDhcpv6RaPortStatTable.setStatus("current")
_MsanDhcpv6RaPortStatEntry_Object = MibTableRow
msanDhcpv6RaPortStatEntry = _MsanDhcpv6RaPortStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 101, 1, 1)
)
msanDhcpv6RaPortStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    msanDhcpv6RaPortStatEntry.setStatus("current")
_MsanDhcpv6PortRaStatSolicit_Type = Integer32
_MsanDhcpv6PortRaStatSolicit_Object = MibTableColumn
msanDhcpv6PortRaStatSolicit = _MsanDhcpv6PortRaStatSolicit_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 101, 1, 1, 1),
    _MsanDhcpv6PortRaStatSolicit_Type()
)
msanDhcpv6PortRaStatSolicit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDhcpv6PortRaStatSolicit.setStatus("current")
_MsanDhcpv6PortRaStatAdvertise_Type = Integer32
_MsanDhcpv6PortRaStatAdvertise_Object = MibTableColumn
msanDhcpv6PortRaStatAdvertise = _MsanDhcpv6PortRaStatAdvertise_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 101, 1, 1, 2),
    _MsanDhcpv6PortRaStatAdvertise_Type()
)
msanDhcpv6PortRaStatAdvertise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDhcpv6PortRaStatAdvertise.setStatus("current")
_MsanDhcpv6PortRaStatRequest_Type = Integer32
_MsanDhcpv6PortRaStatRequest_Object = MibTableColumn
msanDhcpv6PortRaStatRequest = _MsanDhcpv6PortRaStatRequest_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 101, 1, 1, 3),
    _MsanDhcpv6PortRaStatRequest_Type()
)
msanDhcpv6PortRaStatRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDhcpv6PortRaStatRequest.setStatus("current")
_MsanDhcpv6PortRaStatReply_Type = Integer32
_MsanDhcpv6PortRaStatReply_Object = MibTableColumn
msanDhcpv6PortRaStatReply = _MsanDhcpv6PortRaStatReply_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 101, 1, 1, 4),
    _MsanDhcpv6PortRaStatReply_Type()
)
msanDhcpv6PortRaStatReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDhcpv6PortRaStatReply.setStatus("current")
_MsanDhcpv6PortRaStatRenew_Type = Integer32
_MsanDhcpv6PortRaStatRenew_Object = MibTableColumn
msanDhcpv6PortRaStatRenew = _MsanDhcpv6PortRaStatRenew_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 101, 1, 1, 5),
    _MsanDhcpv6PortRaStatRenew_Type()
)
msanDhcpv6PortRaStatRenew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDhcpv6PortRaStatRenew.setStatus("current")
_MsanDhcpv6PortRaStatRebind_Type = Integer32
_MsanDhcpv6PortRaStatRebind_Object = MibTableColumn
msanDhcpv6PortRaStatRebind = _MsanDhcpv6PortRaStatRebind_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 101, 1, 1, 6),
    _MsanDhcpv6PortRaStatRebind_Type()
)
msanDhcpv6PortRaStatRebind.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDhcpv6PortRaStatRebind.setStatus("current")
_MsanDhcpv6PortRaStatDecline_Type = Integer32
_MsanDhcpv6PortRaStatDecline_Object = MibTableColumn
msanDhcpv6PortRaStatDecline = _MsanDhcpv6PortRaStatDecline_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 101, 1, 1, 7),
    _MsanDhcpv6PortRaStatDecline_Type()
)
msanDhcpv6PortRaStatDecline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDhcpv6PortRaStatDecline.setStatus("current")
_MsanDhcpv6PortRaStatReconfigure_Type = Integer32
_MsanDhcpv6PortRaStatReconfigure_Object = MibTableColumn
msanDhcpv6PortRaStatReconfigure = _MsanDhcpv6PortRaStatReconfigure_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 101, 1, 1, 8),
    _MsanDhcpv6PortRaStatReconfigure_Type()
)
msanDhcpv6PortRaStatReconfigure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDhcpv6PortRaStatReconfigure.setStatus("current")
_MsanDhcpv6PortRaStatRelease_Type = Integer32
_MsanDhcpv6PortRaStatRelease_Object = MibTableColumn
msanDhcpv6PortRaStatRelease = _MsanDhcpv6PortRaStatRelease_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 101, 1, 1, 9),
    _MsanDhcpv6PortRaStatRelease_Type()
)
msanDhcpv6PortRaStatRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDhcpv6PortRaStatRelease.setStatus("current")
_MsanDhcpv6PortRaStatInformRequest_Type = Integer32
_MsanDhcpv6PortRaStatInformRequest_Object = MibTableColumn
msanDhcpv6PortRaStatInformRequest = _MsanDhcpv6PortRaStatInformRequest_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 101, 1, 1, 10),
    _MsanDhcpv6PortRaStatInformRequest_Type()
)
msanDhcpv6PortRaStatInformRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDhcpv6PortRaStatInformRequest.setStatus("current")
_MsanDhcpv6PortRaStatRelayForward_Type = Integer32
_MsanDhcpv6PortRaStatRelayForward_Object = MibTableColumn
msanDhcpv6PortRaStatRelayForward = _MsanDhcpv6PortRaStatRelayForward_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 101, 1, 1, 11),
    _MsanDhcpv6PortRaStatRelayForward_Type()
)
msanDhcpv6PortRaStatRelayForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDhcpv6PortRaStatRelayForward.setStatus("current")
_MsanDhcpv6PortRaStatRelayReply_Type = Integer32
_MsanDhcpv6PortRaStatRelayReply_Object = MibTableColumn
msanDhcpv6PortRaStatRelayReply = _MsanDhcpv6PortRaStatRelayReply_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 101, 1, 1, 12),
    _MsanDhcpv6PortRaStatRelayReply_Type()
)
msanDhcpv6PortRaStatRelayReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDhcpv6PortRaStatRelayReply.setStatus("current")
_MsanDhcpv6PortRaStatOversizeError_Type = Integer32
_MsanDhcpv6PortRaStatOversizeError_Object = MibTableColumn
msanDhcpv6PortRaStatOversizeError = _MsanDhcpv6PortRaStatOversizeError_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 101, 1, 1, 100),
    _MsanDhcpv6PortRaStatOversizeError_Type()
)
msanDhcpv6PortRaStatOversizeError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDhcpv6PortRaStatOversizeError.setStatus("current")
_MsanDhcpv6PortRaStatFrameError_Type = Integer32
_MsanDhcpv6PortRaStatFrameError_Object = MibTableColumn
msanDhcpv6PortRaStatFrameError = _MsanDhcpv6PortRaStatFrameError_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 101, 1, 1, 101),
    _MsanDhcpv6PortRaStatFrameError_Type()
)
msanDhcpv6PortRaStatFrameError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDhcpv6PortRaStatFrameError.setStatus("current")
_MsanDhcpv6PortRaStatFrameUnsyncError_Type = Integer32
_MsanDhcpv6PortRaStatFrameUnsyncError_Object = MibTableColumn
msanDhcpv6PortRaStatFrameUnsyncError = _MsanDhcpv6PortRaStatFrameUnsyncError_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 101, 1, 1, 102),
    _MsanDhcpv6PortRaStatFrameUnsyncError_Type()
)
msanDhcpv6PortRaStatFrameUnsyncError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDhcpv6PortRaStatFrameUnsyncError.setStatus("current")
_MsanDhcpv6PortRaStatSysError_Type = Integer32
_MsanDhcpv6PortRaStatSysError_Object = MibTableColumn
msanDhcpv6PortRaStatSysError = _MsanDhcpv6PortRaStatSysError_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 101, 1, 1, 103),
    _MsanDhcpv6PortRaStatSysError_Type()
)
msanDhcpv6PortRaStatSysError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDhcpv6PortRaStatSysError.setStatus("current")
_MsanDhcpv6RaStatSolicit_Type = Counter32
_MsanDhcpv6RaStatSolicit_Object = MibScalar
msanDhcpv6RaStatSolicit = _MsanDhcpv6RaStatSolicit_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 101, 100),
    _MsanDhcpv6RaStatSolicit_Type()
)
msanDhcpv6RaStatSolicit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDhcpv6RaStatSolicit.setStatus("current")
_MsanDhcpv6RaStatAdvertise_Type = Counter32
_MsanDhcpv6RaStatAdvertise_Object = MibScalar
msanDhcpv6RaStatAdvertise = _MsanDhcpv6RaStatAdvertise_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 101, 101),
    _MsanDhcpv6RaStatAdvertise_Type()
)
msanDhcpv6RaStatAdvertise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDhcpv6RaStatAdvertise.setStatus("current")
_MsanDhcpv6RaStatRequest_Type = Counter32
_MsanDhcpv6RaStatRequest_Object = MibScalar
msanDhcpv6RaStatRequest = _MsanDhcpv6RaStatRequest_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 101, 102),
    _MsanDhcpv6RaStatRequest_Type()
)
msanDhcpv6RaStatRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDhcpv6RaStatRequest.setStatus("current")
_MsanDhcpv6RaStatReply_Type = Counter32
_MsanDhcpv6RaStatReply_Object = MibScalar
msanDhcpv6RaStatReply = _MsanDhcpv6RaStatReply_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 101, 103),
    _MsanDhcpv6RaStatReply_Type()
)
msanDhcpv6RaStatReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDhcpv6RaStatReply.setStatus("current")
_MsanDhcpv6RaStatRenew_Type = Counter32
_MsanDhcpv6RaStatRenew_Object = MibScalar
msanDhcpv6RaStatRenew = _MsanDhcpv6RaStatRenew_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 101, 104),
    _MsanDhcpv6RaStatRenew_Type()
)
msanDhcpv6RaStatRenew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDhcpv6RaStatRenew.setStatus("current")
_MsanDhcpv6RaStatRebind_Type = Counter32
_MsanDhcpv6RaStatRebind_Object = MibScalar
msanDhcpv6RaStatRebind = _MsanDhcpv6RaStatRebind_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 101, 105),
    _MsanDhcpv6RaStatRebind_Type()
)
msanDhcpv6RaStatRebind.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDhcpv6RaStatRebind.setStatus("current")
_MsanDhcpv6RaStatDecline_Type = Counter32
_MsanDhcpv6RaStatDecline_Object = MibScalar
msanDhcpv6RaStatDecline = _MsanDhcpv6RaStatDecline_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 101, 106),
    _MsanDhcpv6RaStatDecline_Type()
)
msanDhcpv6RaStatDecline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDhcpv6RaStatDecline.setStatus("current")
_MsanDhcpv6RaStatReconfigure_Type = Counter32
_MsanDhcpv6RaStatReconfigure_Object = MibScalar
msanDhcpv6RaStatReconfigure = _MsanDhcpv6RaStatReconfigure_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 101, 107),
    _MsanDhcpv6RaStatReconfigure_Type()
)
msanDhcpv6RaStatReconfigure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDhcpv6RaStatReconfigure.setStatus("current")
_MsanDhcpv6RaStatRelease_Type = Counter32
_MsanDhcpv6RaStatRelease_Object = MibScalar
msanDhcpv6RaStatRelease = _MsanDhcpv6RaStatRelease_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 101, 108),
    _MsanDhcpv6RaStatRelease_Type()
)
msanDhcpv6RaStatRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDhcpv6RaStatRelease.setStatus("current")
_MsanDhcpv6RaStatInformRequest_Type = Counter32
_MsanDhcpv6RaStatInformRequest_Object = MibScalar
msanDhcpv6RaStatInformRequest = _MsanDhcpv6RaStatInformRequest_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 101, 109),
    _MsanDhcpv6RaStatInformRequest_Type()
)
msanDhcpv6RaStatInformRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDhcpv6RaStatInformRequest.setStatus("current")
_MsanDhcpv6RaStatRelayForward_Type = Counter32
_MsanDhcpv6RaStatRelayForward_Object = MibScalar
msanDhcpv6RaStatRelayForward = _MsanDhcpv6RaStatRelayForward_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 101, 110),
    _MsanDhcpv6RaStatRelayForward_Type()
)
msanDhcpv6RaStatRelayForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDhcpv6RaStatRelayForward.setStatus("current")
_MsanDhcpv6RaStatRelayReply_Type = Counter32
_MsanDhcpv6RaStatRelayReply_Object = MibScalar
msanDhcpv6RaStatRelayReply = _MsanDhcpv6RaStatRelayReply_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 101, 112),
    _MsanDhcpv6RaStatRelayReply_Type()
)
msanDhcpv6RaStatRelayReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDhcpv6RaStatRelayReply.setStatus("current")
_MsanDhcpv6RaStatOversizeError_Type = Counter32
_MsanDhcpv6RaStatOversizeError_Object = MibScalar
msanDhcpv6RaStatOversizeError = _MsanDhcpv6RaStatOversizeError_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 101, 200),
    _MsanDhcpv6RaStatOversizeError_Type()
)
msanDhcpv6RaStatOversizeError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDhcpv6RaStatOversizeError.setStatus("current")
_MsanDhcpv6RaStatFrameError_Type = Counter32
_MsanDhcpv6RaStatFrameError_Object = MibScalar
msanDhcpv6RaStatFrameError = _MsanDhcpv6RaStatFrameError_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 101, 201),
    _MsanDhcpv6RaStatFrameError_Type()
)
msanDhcpv6RaStatFrameError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDhcpv6RaStatFrameError.setStatus("current")
_MsanDhcpv6RaStatFrameUnsyncError_Type = Counter32
_MsanDhcpv6RaStatFrameUnsyncError_Object = MibScalar
msanDhcpv6RaStatFrameUnsyncError = _MsanDhcpv6RaStatFrameUnsyncError_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 101, 202),
    _MsanDhcpv6RaStatFrameUnsyncError_Type()
)
msanDhcpv6RaStatFrameUnsyncError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDhcpv6RaStatFrameUnsyncError.setStatus("current")
_MsanDhcpv6RaStatSysError_Type = Counter32
_MsanDhcpv6RaStatSysError_Object = MibScalar
msanDhcpv6RaStatSysError = _MsanDhcpv6RaStatSysError_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 101, 203),
    _MsanDhcpv6RaStatSysError_Type()
)
msanDhcpv6RaStatSysError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDhcpv6RaStatSysError.setStatus("current")
_MsanDhcpv6RaPortConfigTable_Object = MibTable
msanDhcpv6RaPortConfigTable = _MsanDhcpv6RaPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 102)
)
if mibBuilder.loadTexts:
    msanDhcpv6RaPortConfigTable.setStatus("current")
_MsanDhcpv6RaPortConfigEntry_Object = MibTableRow
msanDhcpv6RaPortConfigEntry = _MsanDhcpv6RaPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 102, 1)
)
msanDhcpv6RaPortConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    msanDhcpv6RaPortConfigEntry.setStatus("current")


class _MsanDhcpv6RaPortState_Type(Integer32):
    """Custom type msanDhcpv6RaPortState based on Integer32"""
    defaultValue = 1

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
        *(("disable", 4),
          ("enable", 1),
          ("enableCli", 2),
          ("enableSrv", 3))
    )


_MsanDhcpv6RaPortState_Type.__name__ = "Integer32"
_MsanDhcpv6RaPortState_Object = MibTableColumn
msanDhcpv6RaPortState = _MsanDhcpv6RaPortState_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 102, 1, 1),
    _MsanDhcpv6RaPortState_Type()
)
msanDhcpv6RaPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDhcpv6RaPortState.setStatus("current")


class _MsanDhcpv6RaPortTrusted_Type(Integer32):
    """Custom type msanDhcpv6RaPortTrusted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanDhcpv6RaPortTrusted_Type.__name__ = "Integer32"
_MsanDhcpv6RaPortTrusted_Object = MibTableColumn
msanDhcpv6RaPortTrusted = _MsanDhcpv6RaPortTrusted_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 102, 1, 2),
    _MsanDhcpv6RaPortTrusted_Type()
)
msanDhcpv6RaPortTrusted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDhcpv6RaPortTrusted.setStatus("current")


class _MsanDhcpv6RaPortInterfaceIdStandard_Type(Integer32):
    """Custom type msanDhcpv6RaPortInterfaceIdStandard based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanDhcpv6RaPortInterfaceIdStandard_Type.__name__ = "Integer32"
_MsanDhcpv6RaPortInterfaceIdStandard_Object = MibTableColumn
msanDhcpv6RaPortInterfaceIdStandard = _MsanDhcpv6RaPortInterfaceIdStandard_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 102, 1, 3),
    _MsanDhcpv6RaPortInterfaceIdStandard_Type()
)
msanDhcpv6RaPortInterfaceIdStandard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDhcpv6RaPortInterfaceIdStandard.setStatus("current")
_MsanDhcpv6RaPortInterfaceId_Type = OctetString
_MsanDhcpv6RaPortInterfaceId_Object = MibTableColumn
msanDhcpv6RaPortInterfaceId = _MsanDhcpv6RaPortInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 102, 1, 4),
    _MsanDhcpv6RaPortInterfaceId_Type()
)
msanDhcpv6RaPortInterfaceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDhcpv6RaPortInterfaceId.setStatus("current")
_MsanDhcpv6RaPortRemoteId_Type = OctetString
_MsanDhcpv6RaPortRemoteId_Object = MibTableColumn
msanDhcpv6RaPortRemoteId = _MsanDhcpv6RaPortRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 102, 1, 5),
    _MsanDhcpv6RaPortRemoteId_Type()
)
msanDhcpv6RaPortRemoteId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDhcpv6RaPortRemoteId.setStatus("current")


class _MsanDhcpv6RaPortRemoteIdEnterpriseNum_Type(Integer32):
    """Custom type msanDhcpv6RaPortRemoteIdEnterpriseNum based on Integer32"""
    defaultValue = 1332

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999999),
    )


_MsanDhcpv6RaPortRemoteIdEnterpriseNum_Type.__name__ = "Integer32"
_MsanDhcpv6RaPortRemoteIdEnterpriseNum_Object = MibTableColumn
msanDhcpv6RaPortRemoteIdEnterpriseNum = _MsanDhcpv6RaPortRemoteIdEnterpriseNum_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 102, 1, 6),
    _MsanDhcpv6RaPortRemoteIdEnterpriseNum_Type()
)
msanDhcpv6RaPortRemoteIdEnterpriseNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDhcpv6RaPortRemoteIdEnterpriseNum.setStatus("current")
_MsanDhcpv6RaVlanConfigTable_Object = MibTable
msanDhcpv6RaVlanConfigTable = _MsanDhcpv6RaVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 103)
)
if mibBuilder.loadTexts:
    msanDhcpv6RaVlanConfigTable.setStatus("current")
_MsanDhcpv6RaVlanConfigEntry_Object = MibTableRow
msanDhcpv6RaVlanConfigEntry = _MsanDhcpv6RaVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 103, 1)
)
msanDhcpv6RaVlanConfigEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    msanDhcpv6RaVlanConfigEntry.setStatus("current")


class _MsanDhcpv6RaVlanState_Type(Integer32):
    """Custom type msanDhcpv6RaVlanState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanDhcpv6RaVlanState_Type.__name__ = "Integer32"
_MsanDhcpv6RaVlanState_Object = MibTableColumn
msanDhcpv6RaVlanState = _MsanDhcpv6RaVlanState_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 103, 1, 1),
    _MsanDhcpv6RaVlanState_Type()
)
msanDhcpv6RaVlanState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDhcpv6RaVlanState.setStatus("current")


class _MsanDhcpv6RaVlanInterfaceIdStandard_Type(Integer32):
    """Custom type msanDhcpv6RaVlanInterfaceIdStandard based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanDhcpv6RaVlanInterfaceIdStandard_Type.__name__ = "Integer32"
_MsanDhcpv6RaVlanInterfaceIdStandard_Object = MibTableColumn
msanDhcpv6RaVlanInterfaceIdStandard = _MsanDhcpv6RaVlanInterfaceIdStandard_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 103, 1, 2),
    _MsanDhcpv6RaVlanInterfaceIdStandard_Type()
)
msanDhcpv6RaVlanInterfaceIdStandard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDhcpv6RaVlanInterfaceIdStandard.setStatus("current")
_MsanDhcpv6RaPortVlanConfigTable_Object = MibTable
msanDhcpv6RaPortVlanConfigTable = _MsanDhcpv6RaPortVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 104)
)
if mibBuilder.loadTexts:
    msanDhcpv6RaPortVlanConfigTable.setStatus("current")
_MsanDhcpv6RaPortVlanConfigEntry_Object = MibTableRow
msanDhcpv6RaPortVlanConfigEntry = _MsanDhcpv6RaPortVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 104, 1)
)
msanDhcpv6RaPortVlanConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    msanDhcpv6RaPortVlanConfigEntry.setStatus("current")
_MsanDhcpv6RaPortVlanRemoteId_Type = OctetString
_MsanDhcpv6RaPortVlanRemoteId_Object = MibTableColumn
msanDhcpv6RaPortVlanRemoteId = _MsanDhcpv6RaPortVlanRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 104, 1, 1),
    _MsanDhcpv6RaPortVlanRemoteId_Type()
)
msanDhcpv6RaPortVlanRemoteId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDhcpv6RaPortVlanRemoteId.setStatus("current")


class _MsanDhcpv6RaPortVlanRemoteIdEnterpriseNum_Type(Integer32):
    """Custom type msanDhcpv6RaPortVlanRemoteIdEnterpriseNum based on Integer32"""
    defaultValue = 1332

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999999),
    )


_MsanDhcpv6RaPortVlanRemoteIdEnterpriseNum_Type.__name__ = "Integer32"
_MsanDhcpv6RaPortVlanRemoteIdEnterpriseNum_Object = MibTableColumn
msanDhcpv6RaPortVlanRemoteIdEnterpriseNum = _MsanDhcpv6RaPortVlanRemoteIdEnterpriseNum_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 104, 1, 2),
    _MsanDhcpv6RaPortVlanRemoteIdEnterpriseNum_Type()
)
msanDhcpv6RaPortVlanRemoteIdEnterpriseNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDhcpv6RaPortVlanRemoteIdEnterpriseNum.setStatus("current")
_MsanDhcpv6RaPortVlanRowStatus_Type = RowStatus
_MsanDhcpv6RaPortVlanRowStatus_Object = MibTableColumn
msanDhcpv6RaPortVlanRowStatus = _MsanDhcpv6RaPortVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 4, 104, 1, 3),
    _MsanDhcpv6RaPortVlanRowStatus_Type()
)
msanDhcpv6RaPortVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanDhcpv6RaPortVlanRowStatus.setStatus("current")
_MsanSntp_ObjectIdentity = ObjectIdentity
msanSntp = _MsanSntp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 5)
)
_MsanSntpGlobal_ObjectIdentity = ObjectIdentity
msanSntpGlobal = _MsanSntpGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 5, 1)
)
_MsanSntpTzOffset_Type = OctetString
_MsanSntpTzOffset_Object = MibScalar
msanSntpTzOffset = _MsanSntpTzOffset_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 5, 1, 1),
    _MsanSntpTzOffset_Type()
)
msanSntpTzOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanSntpTzOffset.setStatus("current")


class _MsanSntpTzName_Type(OctetString):
    """Custom type msanSntpTzName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MsanSntpTzName_Type.__name__ = "OctetString"
_MsanSntpTzName_Object = MibScalar
msanSntpTzName = _MsanSntpTzName_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 5, 1, 2),
    _MsanSntpTzName_Type()
)
msanSntpTzName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanSntpTzName.setStatus("current")
_MsanSntpTzDstOffset_Type = OctetString
_MsanSntpTzDstOffset_Object = MibScalar
msanSntpTzDstOffset = _MsanSntpTzDstOffset_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 5, 1, 3),
    _MsanSntpTzDstOffset_Type()
)
msanSntpTzDstOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanSntpTzDstOffset.setStatus("current")


class _MsanSntpTzDstStartMonth_Type(Integer32):
    """Custom type msanSntpTzDstStartMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_MsanSntpTzDstStartMonth_Type.__name__ = "Integer32"
_MsanSntpTzDstStartMonth_Object = MibScalar
msanSntpTzDstStartMonth = _MsanSntpTzDstStartMonth_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 5, 1, 4),
    _MsanSntpTzDstStartMonth_Type()
)
msanSntpTzDstStartMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanSntpTzDstStartMonth.setStatus("current")


class _MsanSntpTzDstStartWeek_Type(Integer32):
    """Custom type msanSntpTzDstStartWeek based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_MsanSntpTzDstStartWeek_Type.__name__ = "Integer32"
_MsanSntpTzDstStartWeek_Object = MibScalar
msanSntpTzDstStartWeek = _MsanSntpTzDstStartWeek_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 5, 1, 5),
    _MsanSntpTzDstStartWeek_Type()
)
msanSntpTzDstStartWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanSntpTzDstStartWeek.setStatus("current")


class _MsanSntpTzDstStartDayInWeek_Type(Integer32):
    """Custom type msanSntpTzDstStartDayInWeek based on Integer32"""
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
        *(("friday", 5),
          ("monday", 1),
          ("saturday", 6),
          ("sunday", 7),
          ("thursday", 4),
          ("tuesday", 2),
          ("wednesday", 3))
    )


_MsanSntpTzDstStartDayInWeek_Type.__name__ = "Integer32"
_MsanSntpTzDstStartDayInWeek_Object = MibScalar
msanSntpTzDstStartDayInWeek = _MsanSntpTzDstStartDayInWeek_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 5, 1, 6),
    _MsanSntpTzDstStartDayInWeek_Type()
)
msanSntpTzDstStartDayInWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanSntpTzDstStartDayInWeek.setStatus("current")
_MsanSntpTzDstStartTime_Type = OctetString
_MsanSntpTzDstStartTime_Object = MibScalar
msanSntpTzDstStartTime = _MsanSntpTzDstStartTime_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 5, 1, 7),
    _MsanSntpTzDstStartTime_Type()
)
msanSntpTzDstStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanSntpTzDstStartTime.setStatus("current")


class _MsanSntpTzDstEndMonth_Type(Integer32):
    """Custom type msanSntpTzDstEndMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_MsanSntpTzDstEndMonth_Type.__name__ = "Integer32"
_MsanSntpTzDstEndMonth_Object = MibScalar
msanSntpTzDstEndMonth = _MsanSntpTzDstEndMonth_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 5, 1, 8),
    _MsanSntpTzDstEndMonth_Type()
)
msanSntpTzDstEndMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanSntpTzDstEndMonth.setStatus("current")


class _MsanSntpTzDstEndWeek_Type(Integer32):
    """Custom type msanSntpTzDstEndWeek based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_MsanSntpTzDstEndWeek_Type.__name__ = "Integer32"
_MsanSntpTzDstEndWeek_Object = MibScalar
msanSntpTzDstEndWeek = _MsanSntpTzDstEndWeek_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 5, 1, 9),
    _MsanSntpTzDstEndWeek_Type()
)
msanSntpTzDstEndWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanSntpTzDstEndWeek.setStatus("current")


class _MsanSntpTzDstEndDayInWeek_Type(Integer32):
    """Custom type msanSntpTzDstEndDayInWeek based on Integer32"""
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
        *(("friday", 5),
          ("monday", 1),
          ("saturday", 6),
          ("sunday", 7),
          ("thursday", 4),
          ("tuesday", 2),
          ("wednesday", 3))
    )


_MsanSntpTzDstEndDayInWeek_Type.__name__ = "Integer32"
_MsanSntpTzDstEndDayInWeek_Object = MibScalar
msanSntpTzDstEndDayInWeek = _MsanSntpTzDstEndDayInWeek_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 5, 1, 10),
    _MsanSntpTzDstEndDayInWeek_Type()
)
msanSntpTzDstEndDayInWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanSntpTzDstEndDayInWeek.setStatus("current")
_MsanSntpTzDstEndTime_Type = OctetString
_MsanSntpTzDstEndTime_Object = MibScalar
msanSntpTzDstEndTime = _MsanSntpTzDstEndTime_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 5, 1, 11),
    _MsanSntpTzDstEndTime_Type()
)
msanSntpTzDstEndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanSntpTzDstEndTime.setStatus("current")
_MsanSnmp_ObjectIdentity = ObjectIdentity
msanSnmp = _MsanSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 7)
)
_MsanSnmpGlobal_ObjectIdentity = ObjectIdentity
msanSnmpGlobal = _MsanSnmpGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 7, 1)
)


class _MsanSnmpTrapRecvUdpPort_Type(Unsigned32):
    """Custom type msanSnmpTrapRecvUdpPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MsanSnmpTrapRecvUdpPort_Type.__name__ = "Unsigned32"
_MsanSnmpTrapRecvUdpPort_Object = MibScalar
msanSnmpTrapRecvUdpPort = _MsanSnmpTrapRecvUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 7, 1, 1),
    _MsanSnmpTrapRecvUdpPort_Type()
)
msanSnmpTrapRecvUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanSnmpTrapRecvUdpPort.setStatus("current")
_MsanIgmpSnooping_ObjectIdentity = ObjectIdentity
msanIgmpSnooping = _MsanIgmpSnooping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8)
)
_MsanIgmpSnoopingGlobal_ObjectIdentity = ObjectIdentity
msanIgmpSnoopingGlobal = _MsanIgmpSnoopingGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 1)
)


class _MsanIgmpSnoopingReportSuppression_Type(Integer32):
    """Custom type msanIgmpSnoopingReportSuppression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_MsanIgmpSnoopingReportSuppression_Type.__name__ = "Integer32"
_MsanIgmpSnoopingReportSuppression_Object = MibScalar
msanIgmpSnoopingReportSuppression = _MsanIgmpSnoopingReportSuppression_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 1, 1),
    _MsanIgmpSnoopingReportSuppression_Type()
)
msanIgmpSnoopingReportSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIgmpSnoopingReportSuppression.setStatus("current")


class _MsanIgmpSnoopingAdminState_Type(Integer32):
    """Custom type msanIgmpSnoopingAdminState based on Integer32"""
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
        *(("disableAndBroadcast", 1),
          ("disableAndDiscard", 0),
          ("enable", 2),
          ("enableAndMrouterFlood", 4),
          ("enableAndUnknownGroupFlood", 3))
    )


_MsanIgmpSnoopingAdminState_Type.__name__ = "Integer32"
_MsanIgmpSnoopingAdminState_Object = MibScalar
msanIgmpSnoopingAdminState = _MsanIgmpSnoopingAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 1, 2),
    _MsanIgmpSnoopingAdminState_Type()
)
msanIgmpSnoopingAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIgmpSnoopingAdminState.setStatus("current")


class _MsanIgmpSnoopingLoggingVlanId_Type(Integer32):
    """Custom type msanIgmpSnoopingLoggingVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_MsanIgmpSnoopingLoggingVlanId_Type.__name__ = "Integer32"
_MsanIgmpSnoopingLoggingVlanId_Object = MibScalar
msanIgmpSnoopingLoggingVlanId = _MsanIgmpSnoopingLoggingVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 1, 3),
    _MsanIgmpSnoopingLoggingVlanId_Type()
)
msanIgmpSnoopingLoggingVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIgmpSnoopingLoggingVlanId.setStatus("current")


class _MsanIgmpSnoopingViolationAction_Type(Integer32):
    """Custom type msanIgmpSnoopingViolationAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("remove", 1))
    )


_MsanIgmpSnoopingViolationAction_Type.__name__ = "Integer32"
_MsanIgmpSnoopingViolationAction_Object = MibScalar
msanIgmpSnoopingViolationAction = _MsanIgmpSnoopingViolationAction_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 1, 4),
    _MsanIgmpSnoopingViolationAction_Type()
)
msanIgmpSnoopingViolationAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIgmpSnoopingViolationAction.setStatus("current")


class _MsanIgmpSnoopingFastLeaveAdminMode_Type(Integer32):
    """Custom type msanIgmpSnoopingFastLeaveAdminMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanIgmpSnoopingFastLeaveAdminMode_Type.__name__ = "Integer32"
_MsanIgmpSnoopingFastLeaveAdminMode_Object = MibScalar
msanIgmpSnoopingFastLeaveAdminMode = _MsanIgmpSnoopingFastLeaveAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 1, 5),
    _MsanIgmpSnoopingFastLeaveAdminMode_Type()
)
msanIgmpSnoopingFastLeaveAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIgmpSnoopingFastLeaveAdminMode.setStatus("current")


class _MsanIgmpSnoopingGroupMembershipInterval_Type(Integer32):
    """Custom type msanIgmpSnoopingGroupMembershipInterval based on Integer32"""
    defaultValue = 260

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 3600),
    )


_MsanIgmpSnoopingGroupMembershipInterval_Type.__name__ = "Integer32"
_MsanIgmpSnoopingGroupMembershipInterval_Object = MibScalar
msanIgmpSnoopingGroupMembershipInterval = _MsanIgmpSnoopingGroupMembershipInterval_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 1, 6),
    _MsanIgmpSnoopingGroupMembershipInterval_Type()
)
msanIgmpSnoopingGroupMembershipInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIgmpSnoopingGroupMembershipInterval.setStatus("current")


class _MsanIgmpSnoopingMaxResponseTime_Type(Integer32):
    """Custom type msanIgmpSnoopingMaxResponseTime based on Integer32"""
    defaultBinValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3599),
    )


_MsanIgmpSnoopingMaxResponseTime_Type.__name__ = "Integer32"
_MsanIgmpSnoopingMaxResponseTime_Object = MibScalar
msanIgmpSnoopingMaxResponseTime = _MsanIgmpSnoopingMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 1, 7),
    _MsanIgmpSnoopingMaxResponseTime_Type()
)
msanIgmpSnoopingMaxResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIgmpSnoopingMaxResponseTime.setStatus("current")


class _MsanIgmpVersion_Type(Integer32):
    """Custom type msanIgmpVersion based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("igmpAll", 1),
          ("igmpVersion2", 2),
          ("igmpVersion3", 3))
    )


_MsanIgmpVersion_Type.__name__ = "Integer32"
_MsanIgmpVersion_Object = MibScalar
msanIgmpVersion = _MsanIgmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 1, 8),
    _MsanIgmpVersion_Type()
)
msanIgmpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIgmpVersion.setStatus("current")


class _MsanIgmpClear_Type(Integer32):
    """Custom type msanIgmpClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanIgmpClear_Type.__name__ = "Integer32"
_MsanIgmpClear_Object = MibScalar
msanIgmpClear = _MsanIgmpClear_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 1, 9),
    _MsanIgmpClear_Type()
)
msanIgmpClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIgmpClear.setStatus("current")
_MsanIgmpSnoopingTable_Object = MibTable
msanIgmpSnoopingTable = _MsanIgmpSnoopingTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 2)
)
if mibBuilder.loadTexts:
    msanIgmpSnoopingTable.setStatus("current")
_MsanIgmpSnoopingEntry_Object = MibTableRow
msanIgmpSnoopingEntry = _MsanIgmpSnoopingEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 2, 1)
)
msanIgmpSnoopingEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    msanIgmpSnoopingEntry.setStatus("current")
_MsanIgmpSnoopingIntfStandaloneQuerier_Type = Integer32
_MsanIgmpSnoopingIntfStandaloneQuerier_Object = MibTableColumn
msanIgmpSnoopingIntfStandaloneQuerier = _MsanIgmpSnoopingIntfStandaloneQuerier_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 2, 1, 1),
    _MsanIgmpSnoopingIntfStandaloneQuerier_Type()
)
msanIgmpSnoopingIntfStandaloneQuerier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIgmpSnoopingIntfStandaloneQuerier.setStatus("current")
if mibBuilder.loadTexts:
    msanIgmpSnoopingIntfStandaloneQuerier.setUnits("seconds")


class _MsanIgmpSnoopingIntfFilter_Type(Integer32):
    """Custom type msanIgmpSnoopingIntfFilter based on Integer32"""
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
        *(("allowAll", 0),
          ("allowQueries", 2),
          ("allowReports", 1),
          ("dropAll", 3))
    )


_MsanIgmpSnoopingIntfFilter_Type.__name__ = "Integer32"
_MsanIgmpSnoopingIntfFilter_Object = MibTableColumn
msanIgmpSnoopingIntfFilter = _MsanIgmpSnoopingIntfFilter_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 2, 1, 2),
    _MsanIgmpSnoopingIntfFilter_Type()
)
msanIgmpSnoopingIntfFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIgmpSnoopingIntfFilter.setStatus("current")


class _MsanIgmpSnoopingGroupLimit_Type(Integer32):
    """Custom type msanIgmpSnoopingGroupLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_MsanIgmpSnoopingGroupLimit_Type.__name__ = "Integer32"
_MsanIgmpSnoopingGroupLimit_Object = MibTableColumn
msanIgmpSnoopingGroupLimit = _MsanIgmpSnoopingGroupLimit_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 2, 1, 3),
    _MsanIgmpSnoopingGroupLimit_Type()
)
msanIgmpSnoopingGroupLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIgmpSnoopingGroupLimit.setStatus("current")
_MsanSwitchIGMPVlanCurrentMrouterTable_Object = MibTable
msanSwitchIGMPVlanCurrentMrouterTable = _MsanSwitchIGMPVlanCurrentMrouterTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 3)
)
if mibBuilder.loadTexts:
    msanSwitchIGMPVlanCurrentMrouterTable.setStatus("current")
_MsanSwitchIGMPVlanCurrentMrouterEntry_Object = MibTableRow
msanSwitchIGMPVlanCurrentMrouterEntry = _MsanSwitchIGMPVlanCurrentMrouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 3, 1)
)
msanSwitchIGMPVlanCurrentMrouterEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    msanSwitchIGMPVlanCurrentMrouterEntry.setStatus("current")
_MsanSwitchIGMPVlanCurrentMrouterEnableState_Type = Integer32
_MsanSwitchIGMPVlanCurrentMrouterEnableState_Object = MibTableColumn
msanSwitchIGMPVlanCurrentMrouterEnableState = _MsanSwitchIGMPVlanCurrentMrouterEnableState_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 3, 1, 1),
    _MsanSwitchIGMPVlanCurrentMrouterEnableState_Type()
)
msanSwitchIGMPVlanCurrentMrouterEnableState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanSwitchIGMPVlanCurrentMrouterEnableState.setStatus("current")
_MsanSwitchIGMPSnoopingStaticIntfMulticastRouterTable_Object = MibTable
msanSwitchIGMPSnoopingStaticIntfMulticastRouterTable = _MsanSwitchIGMPSnoopingStaticIntfMulticastRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 4)
)
if mibBuilder.loadTexts:
    msanSwitchIGMPSnoopingStaticIntfMulticastRouterTable.setStatus("current")
_MsanSwitchIGMPSnoopingStaticIntfMulticastRouterEntry_Object = MibTableRow
msanSwitchIGMPSnoopingStaticIntfMulticastRouterEntry = _MsanSwitchIGMPSnoopingStaticIntfMulticastRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 4, 1)
)
msanSwitchIGMPSnoopingStaticIntfMulticastRouterEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    msanSwitchIGMPSnoopingStaticIntfMulticastRouterEntry.setStatus("current")


class _MsanSwitchIGMPSnoopingIntfIndex_Type(Unsigned32):
    """Custom type msanSwitchIGMPSnoopingIntfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MsanSwitchIGMPSnoopingIntfIndex_Type.__name__ = "Unsigned32"
_MsanSwitchIGMPSnoopingIntfIndex_Object = MibTableColumn
msanSwitchIGMPSnoopingIntfIndex = _MsanSwitchIGMPSnoopingIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 4, 1, 1),
    _MsanSwitchIGMPSnoopingIntfIndex_Type()
)
msanSwitchIGMPSnoopingIntfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanSwitchIGMPSnoopingIntfIndex.setStatus("current")


class _MsanSwitchIGMPSnoopingIntfAdminMode_Type(Integer32):
    """Custom type msanSwitchIGMPSnoopingIntfAdminMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanSwitchIGMPSnoopingIntfAdminMode_Type.__name__ = "Integer32"
_MsanSwitchIGMPSnoopingIntfAdminMode_Object = MibTableColumn
msanSwitchIGMPSnoopingIntfAdminMode = _MsanSwitchIGMPSnoopingIntfAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 4, 1, 2),
    _MsanSwitchIGMPSnoopingIntfAdminMode_Type()
)
msanSwitchIGMPSnoopingIntfAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanSwitchIGMPSnoopingIntfAdminMode.setStatus("deprecated")


class _MsanSwitchIGMPSnoopingIntfGroupMembershipInterval_Type(Integer32):
    """Custom type msanSwitchIGMPSnoopingIntfGroupMembershipInterval based on Integer32"""
    defaultValue = 260

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 3600),
    )


_MsanSwitchIGMPSnoopingIntfGroupMembershipInterval_Type.__name__ = "Integer32"
_MsanSwitchIGMPSnoopingIntfGroupMembershipInterval_Object = MibTableColumn
msanSwitchIGMPSnoopingIntfGroupMembershipInterval = _MsanSwitchIGMPSnoopingIntfGroupMembershipInterval_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 4, 1, 3),
    _MsanSwitchIGMPSnoopingIntfGroupMembershipInterval_Type()
)
msanSwitchIGMPSnoopingIntfGroupMembershipInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanSwitchIGMPSnoopingIntfGroupMembershipInterval.setStatus("deprecated")


class _MsanSwitchIGMPSnoopingIntfMaxResponseTime_Type(Integer32):
    """Custom type msanSwitchIGMPSnoopingIntfMaxResponseTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3599),
    )


_MsanSwitchIGMPSnoopingIntfMaxResponseTime_Type.__name__ = "Integer32"
_MsanSwitchIGMPSnoopingIntfMaxResponseTime_Object = MibTableColumn
msanSwitchIGMPSnoopingIntfMaxResponseTime = _MsanSwitchIGMPSnoopingIntfMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 4, 1, 4),
    _MsanSwitchIGMPSnoopingIntfMaxResponseTime_Type()
)
msanSwitchIGMPSnoopingIntfMaxResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanSwitchIGMPSnoopingIntfMaxResponseTime.setStatus("deprecated")


class _MsanSwitchIGMPSnoopingIntfMRPExpirationTime_Type(Integer32):
    """Custom type msanSwitchIGMPSnoopingIntfMRPExpirationTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_MsanSwitchIGMPSnoopingIntfMRPExpirationTime_Type.__name__ = "Integer32"
_MsanSwitchIGMPSnoopingIntfMRPExpirationTime_Object = MibTableColumn
msanSwitchIGMPSnoopingIntfMRPExpirationTime = _MsanSwitchIGMPSnoopingIntfMRPExpirationTime_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 4, 1, 5),
    _MsanSwitchIGMPSnoopingIntfMRPExpirationTime_Type()
)
msanSwitchIGMPSnoopingIntfMRPExpirationTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanSwitchIGMPSnoopingIntfMRPExpirationTime.setStatus("deprecated")


class _MsanSwitchIGMPSnoopingIntfFastLeaveAdminMode_Type(Integer32):
    """Custom type msanSwitchIGMPSnoopingIntfFastLeaveAdminMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanSwitchIGMPSnoopingIntfFastLeaveAdminMode_Type.__name__ = "Integer32"
_MsanSwitchIGMPSnoopingIntfFastLeaveAdminMode_Object = MibTableColumn
msanSwitchIGMPSnoopingIntfFastLeaveAdminMode = _MsanSwitchIGMPSnoopingIntfFastLeaveAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 4, 1, 6),
    _MsanSwitchIGMPSnoopingIntfFastLeaveAdminMode_Type()
)
msanSwitchIGMPSnoopingIntfFastLeaveAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanSwitchIGMPSnoopingIntfFastLeaveAdminMode.setStatus("deprecated")


class _MsanSwitchIGMPSnoopingStaticIntfMulticastRouterMode_Type(Integer32):
    """Custom type msanSwitchIGMPSnoopingStaticIntfMulticastRouterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanSwitchIGMPSnoopingStaticIntfMulticastRouterMode_Type.__name__ = "Integer32"
_MsanSwitchIGMPSnoopingStaticIntfMulticastRouterMode_Object = MibTableColumn
msanSwitchIGMPSnoopingStaticIntfMulticastRouterMode = _MsanSwitchIGMPSnoopingStaticIntfMulticastRouterMode_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 4, 1, 7),
    _MsanSwitchIGMPSnoopingStaticIntfMulticastRouterMode_Type()
)
msanSwitchIGMPSnoopingStaticIntfMulticastRouterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanSwitchIGMPSnoopingStaticIntfMulticastRouterMode.setStatus("current")
_MsanSwitchIGMPSnoopingIntfVlanIDs_Type = VlanList
_MsanSwitchIGMPSnoopingIntfVlanIDs_Object = MibTableColumn
msanSwitchIGMPSnoopingIntfVlanIDs = _MsanSwitchIGMPSnoopingIntfVlanIDs_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 4, 1, 8),
    _MsanSwitchIGMPSnoopingIntfVlanIDs_Type()
)
msanSwitchIGMPSnoopingIntfVlanIDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanSwitchIGMPSnoopingIntfVlanIDs.setStatus("deprecated")
_MsanSwitchIGMPVlanStaticMrouterTable_Object = MibTable
msanSwitchIGMPVlanStaticMrouterTable = _MsanSwitchIGMPVlanStaticMrouterTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 5)
)
if mibBuilder.loadTexts:
    msanSwitchIGMPVlanStaticMrouterTable.setStatus("deprecated")
_MsanSwitchIGMPVlanStaticMrouterEntry_Object = MibTableRow
msanSwitchIGMPVlanStaticMrouterEntry = _MsanSwitchIGMPVlanStaticMrouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 5, 1)
)
msanSwitchIGMPVlanStaticMrouterEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    msanSwitchIGMPVlanStaticMrouterEntry.setStatus("deprecated")
_MsanSwitchIGMPVlanStaticMrouterEnableState_Type = RowStatus
_MsanSwitchIGMPVlanStaticMrouterEnableState_Object = MibTableColumn
msanSwitchIGMPVlanStaticMrouterEnableState = _MsanSwitchIGMPVlanStaticMrouterEnableState_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 5, 1, 1),
    _MsanSwitchIGMPVlanStaticMrouterEnableState_Type()
)
msanSwitchIGMPVlanStaticMrouterEnableState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanSwitchIGMPVlanStaticMrouterEnableState.setStatus("deprecated")
_MsanSwitchIGMPSnoopingVlanTable_Object = MibTable
msanSwitchIGMPSnoopingVlanTable = _MsanSwitchIGMPSnoopingVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 6)
)
if mibBuilder.loadTexts:
    msanSwitchIGMPSnoopingVlanTable.setStatus("current")
_MsanSwitchIGMPSnoopingVlanEntry_Object = MibTableRow
msanSwitchIGMPSnoopingVlanEntry = _MsanSwitchIGMPSnoopingVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 6, 1)
)
msanSwitchIGMPSnoopingVlanEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    msanSwitchIGMPSnoopingVlanEntry.setStatus("current")


class _MsanSwitchIGMPSnoopingVlanAdminMode_Type(Integer32):
    """Custom type msanSwitchIGMPSnoopingVlanAdminMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_MsanSwitchIGMPSnoopingVlanAdminMode_Type.__name__ = "Integer32"
_MsanSwitchIGMPSnoopingVlanAdminMode_Object = MibTableColumn
msanSwitchIGMPSnoopingVlanAdminMode = _MsanSwitchIGMPSnoopingVlanAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 6, 1, 1),
    _MsanSwitchIGMPSnoopingVlanAdminMode_Type()
)
msanSwitchIGMPSnoopingVlanAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanSwitchIGMPSnoopingVlanAdminMode.setStatus("deprecated")


class _MsanSwitchIGMPSnoopingVlanGroupMembershipInterval_Type(Integer32):
    """Custom type msanSwitchIGMPSnoopingVlanGroupMembershipInterval based on Integer32"""
    defaultValue = 260

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 3600),
    )


_MsanSwitchIGMPSnoopingVlanGroupMembershipInterval_Type.__name__ = "Integer32"
_MsanSwitchIGMPSnoopingVlanGroupMembershipInterval_Object = MibTableColumn
msanSwitchIGMPSnoopingVlanGroupMembershipInterval = _MsanSwitchIGMPSnoopingVlanGroupMembershipInterval_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 6, 1, 2),
    _MsanSwitchIGMPSnoopingVlanGroupMembershipInterval_Type()
)
msanSwitchIGMPSnoopingVlanGroupMembershipInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanSwitchIGMPSnoopingVlanGroupMembershipInterval.setStatus("deprecated")


class _MsanSwitchIGMPSnoopingVlanMaxResponseTime_Type(Integer32):
    """Custom type msanSwitchIGMPSnoopingVlanMaxResponseTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3599),
    )


_MsanSwitchIGMPSnoopingVlanMaxResponseTime_Type.__name__ = "Integer32"
_MsanSwitchIGMPSnoopingVlanMaxResponseTime_Object = MibTableColumn
msanSwitchIGMPSnoopingVlanMaxResponseTime = _MsanSwitchIGMPSnoopingVlanMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 6, 1, 3),
    _MsanSwitchIGMPSnoopingVlanMaxResponseTime_Type()
)
msanSwitchIGMPSnoopingVlanMaxResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanSwitchIGMPSnoopingVlanMaxResponseTime.setStatus("deprecated")


class _MsanSwitchIGMPSnoopingVlanFastLeaveAdminMode_Type(Integer32):
    """Custom type msanSwitchIGMPSnoopingVlanFastLeaveAdminMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_MsanSwitchIGMPSnoopingVlanFastLeaveAdminMode_Type.__name__ = "Integer32"
_MsanSwitchIGMPSnoopingVlanFastLeaveAdminMode_Object = MibTableColumn
msanSwitchIGMPSnoopingVlanFastLeaveAdminMode = _MsanSwitchIGMPSnoopingVlanFastLeaveAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 6, 1, 4),
    _MsanSwitchIGMPSnoopingVlanFastLeaveAdminMode_Type()
)
msanSwitchIGMPSnoopingVlanFastLeaveAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanSwitchIGMPSnoopingVlanFastLeaveAdminMode.setStatus("deprecated")


class _MsanSwitchIGMPSnoopingVlanMRPExpirationTime_Type(Integer32):
    """Custom type msanSwitchIGMPSnoopingVlanMRPExpirationTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_MsanSwitchIGMPSnoopingVlanMRPExpirationTime_Type.__name__ = "Integer32"
_MsanSwitchIGMPSnoopingVlanMRPExpirationTime_Object = MibTableColumn
msanSwitchIGMPSnoopingVlanMRPExpirationTime = _MsanSwitchIGMPSnoopingVlanMRPExpirationTime_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 6, 1, 5),
    _MsanSwitchIGMPSnoopingVlanMRPExpirationTime_Type()
)
msanSwitchIGMPSnoopingVlanMRPExpirationTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanSwitchIGMPSnoopingVlanMRPExpirationTime.setStatus("deprecated")


class _MsanSwitchIGMPSnoopingVlanAdminState_Type(Integer32):
    """Custom type msanSwitchIGMPSnoopingVlanAdminState based on Integer32"""
    defaultValue = 0

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
        *(("disableAndBroadcast", 1),
          ("disableAndDiscard", 0),
          ("enable", 2),
          ("enableAndUnknownGroupFlood", 3))
    )


_MsanSwitchIGMPSnoopingVlanAdminState_Type.__name__ = "Integer32"
_MsanSwitchIGMPSnoopingVlanAdminState_Object = MibTableColumn
msanSwitchIGMPSnoopingVlanAdminState = _MsanSwitchIGMPSnoopingVlanAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 6, 1, 6),
    _MsanSwitchIGMPSnoopingVlanAdminState_Type()
)
msanSwitchIGMPSnoopingVlanAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanSwitchIGMPSnoopingVlanAdminState.setStatus("current")
_MsanSwitchIGMPProxyVlanTable_Object = MibTable
msanSwitchIGMPProxyVlanTable = _MsanSwitchIGMPProxyVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 7)
)
if mibBuilder.loadTexts:
    msanSwitchIGMPProxyVlanTable.setStatus("current")
_MsanSwitchIGMPProxyVlanEntry_Object = MibTableRow
msanSwitchIGMPProxyVlanEntry = _MsanSwitchIGMPProxyVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 7, 1)
)
msanSwitchIGMPProxyVlanEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
    (0, "ISKRATEL-MSAN-MIB", "msanSwitchIGMPProxyVlanIpAddr"),
)
if mibBuilder.loadTexts:
    msanSwitchIGMPProxyVlanEntry.setStatus("current")
_MsanSwitchIGMPProxyVlanIpAddr_Type = IpAddress
_MsanSwitchIGMPProxyVlanIpAddr_Object = MibTableColumn
msanSwitchIGMPProxyVlanIpAddr = _MsanSwitchIGMPProxyVlanIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 7, 1, 1),
    _MsanSwitchIGMPProxyVlanIpAddr_Type()
)
msanSwitchIGMPProxyVlanIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanSwitchIGMPProxyVlanIpAddr.setStatus("current")
_MsanSwitchIGMPProxyVlanRowStatus_Type = RowStatus
_MsanSwitchIGMPProxyVlanRowStatus_Object = MibTableColumn
msanSwitchIGMPProxyVlanRowStatus = _MsanSwitchIGMPProxyVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 7, 1, 2),
    _MsanSwitchIGMPProxyVlanRowStatus_Type()
)
msanSwitchIGMPProxyVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanSwitchIGMPProxyVlanRowStatus.setStatus("current")
_MsanIgmpStatistics_ObjectIdentity = ObjectIdentity
msanIgmpStatistics = _MsanIgmpStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 8)
)
_MsanIgmpStatGlobal_ObjectIdentity = ObjectIdentity
msanIgmpStatGlobal = _MsanIgmpStatGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 8, 1)
)
_MsanIgmpStatRxV1_Type = Counter32
_MsanIgmpStatRxV1_Object = MibScalar
msanIgmpStatRxV1 = _MsanIgmpStatRxV1_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 8, 1, 1),
    _MsanIgmpStatRxV1_Type()
)
msanIgmpStatRxV1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanIgmpStatRxV1.setStatus("current")
_MsanIgmpStatRxV2Join_Type = Counter32
_MsanIgmpStatRxV2Join_Object = MibScalar
msanIgmpStatRxV2Join = _MsanIgmpStatRxV2Join_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 8, 1, 2),
    _MsanIgmpStatRxV2Join_Type()
)
msanIgmpStatRxV2Join.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanIgmpStatRxV2Join.setStatus("current")
_MsanIgmpStatRxV2Leave_Type = Counter32
_MsanIgmpStatRxV2Leave_Object = MibScalar
msanIgmpStatRxV2Leave = _MsanIgmpStatRxV2Leave_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 8, 1, 3),
    _MsanIgmpStatRxV2Leave_Type()
)
msanIgmpStatRxV2Leave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanIgmpStatRxV2Leave.setStatus("current")
_MsanIgmpStatRxV3Report_Type = Counter32
_MsanIgmpStatRxV3Report_Object = MibScalar
msanIgmpStatRxV3Report = _MsanIgmpStatRxV3Report_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 8, 1, 4),
    _MsanIgmpStatRxV3Report_Type()
)
msanIgmpStatRxV3Report.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanIgmpStatRxV3Report.setStatus("current")
_MsanIgmpStatRxQuery_Type = Counter32
_MsanIgmpStatRxQuery_Object = MibScalar
msanIgmpStatRxQuery = _MsanIgmpStatRxQuery_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 8, 1, 5),
    _MsanIgmpStatRxQuery_Type()
)
msanIgmpStatRxQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanIgmpStatRxQuery.setStatus("current")
_MsanIgmpStatRxError_Type = Counter32
_MsanIgmpStatRxError_Object = MibScalar
msanIgmpStatRxError = _MsanIgmpStatRxError_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 8, 1, 6),
    _MsanIgmpStatRxError_Type()
)
msanIgmpStatRxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanIgmpStatRxError.setStatus("current")
_MsanIgmpStatRxBlockByIgmpFilter_Type = Counter32
_MsanIgmpStatRxBlockByIgmpFilter_Object = MibScalar
msanIgmpStatRxBlockByIgmpFilter = _MsanIgmpStatRxBlockByIgmpFilter_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 8, 1, 7),
    _MsanIgmpStatRxBlockByIgmpFilter_Type()
)
msanIgmpStatRxBlockByIgmpFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanIgmpStatRxBlockByIgmpFilter.setStatus("current")
_MsanIgmpStatRxBlockByMcastAcl_Type = Counter32
_MsanIgmpStatRxBlockByMcastAcl_Object = MibScalar
msanIgmpStatRxBlockByMcastAcl = _MsanIgmpStatRxBlockByMcastAcl_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 8, 1, 8),
    _MsanIgmpStatRxBlockByMcastAcl_Type()
)
msanIgmpStatRxBlockByMcastAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanIgmpStatRxBlockByMcastAcl.setStatus("current")
_MsanIgmpStatRxBlockByMcastCac_Type = Counter32
_MsanIgmpStatRxBlockByMcastCac_Object = MibScalar
msanIgmpStatRxBlockByMcastCac = _MsanIgmpStatRxBlockByMcastCac_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 8, 1, 9),
    _MsanIgmpStatRxBlockByMcastCac_Type()
)
msanIgmpStatRxBlockByMcastCac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanIgmpStatRxBlockByMcastCac.setStatus("current")
_MsanIgmpStatRxBlockByIgmpVersion_Type = Counter32
_MsanIgmpStatRxBlockByIgmpVersion_Object = MibScalar
msanIgmpStatRxBlockByIgmpVersion = _MsanIgmpStatRxBlockByIgmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 8, 1, 10),
    _MsanIgmpStatRxBlockByIgmpVersion_Type()
)
msanIgmpStatRxBlockByIgmpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanIgmpStatRxBlockByIgmpVersion.setStatus("current")
_MsanIgmpPortStatTable_Object = MibTable
msanIgmpPortStatTable = _MsanIgmpPortStatTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 8, 2)
)
if mibBuilder.loadTexts:
    msanIgmpPortStatTable.setStatus("current")
_MsanIgmpPortStatEntry_Object = MibTableRow
msanIgmpPortStatEntry = _MsanIgmpPortStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 8, 2, 1)
)
msanIgmpPortStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    msanIgmpPortStatEntry.setStatus("current")
_MsanIgmpPortStatRxV1_Type = Counter32
_MsanIgmpPortStatRxV1_Object = MibTableColumn
msanIgmpPortStatRxV1 = _MsanIgmpPortStatRxV1_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 8, 2, 1, 1),
    _MsanIgmpPortStatRxV1_Type()
)
msanIgmpPortStatRxV1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanIgmpPortStatRxV1.setStatus("current")
_MsanIgmpPortStatTxV1_Type = Counter32
_MsanIgmpPortStatTxV1_Object = MibTableColumn
msanIgmpPortStatTxV1 = _MsanIgmpPortStatTxV1_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 8, 2, 1, 2),
    _MsanIgmpPortStatTxV1_Type()
)
msanIgmpPortStatTxV1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanIgmpPortStatTxV1.setStatus("current")
_MsanIgmpPortStatRxV2Join_Type = Counter32
_MsanIgmpPortStatRxV2Join_Object = MibTableColumn
msanIgmpPortStatRxV2Join = _MsanIgmpPortStatRxV2Join_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 8, 2, 1, 3),
    _MsanIgmpPortStatRxV2Join_Type()
)
msanIgmpPortStatRxV2Join.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanIgmpPortStatRxV2Join.setStatus("current")
_MsanIgmpPortStatTxV2Join_Type = Counter32
_MsanIgmpPortStatTxV2Join_Object = MibTableColumn
msanIgmpPortStatTxV2Join = _MsanIgmpPortStatTxV2Join_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 8, 2, 1, 4),
    _MsanIgmpPortStatTxV2Join_Type()
)
msanIgmpPortStatTxV2Join.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanIgmpPortStatTxV2Join.setStatus("current")
_MsanIgmpPortStatRxV2Leave_Type = Counter32
_MsanIgmpPortStatRxV2Leave_Object = MibTableColumn
msanIgmpPortStatRxV2Leave = _MsanIgmpPortStatRxV2Leave_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 8, 2, 1, 5),
    _MsanIgmpPortStatRxV2Leave_Type()
)
msanIgmpPortStatRxV2Leave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanIgmpPortStatRxV2Leave.setStatus("current")
_MsanIgmpPortStatTxV2Leave_Type = Counter32
_MsanIgmpPortStatTxV2Leave_Object = MibTableColumn
msanIgmpPortStatTxV2Leave = _MsanIgmpPortStatTxV2Leave_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 8, 2, 1, 6),
    _MsanIgmpPortStatTxV2Leave_Type()
)
msanIgmpPortStatTxV2Leave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanIgmpPortStatTxV2Leave.setStatus("current")
_MsanIgmpPortStatRxV3Report_Type = Counter32
_MsanIgmpPortStatRxV3Report_Object = MibTableColumn
msanIgmpPortStatRxV3Report = _MsanIgmpPortStatRxV3Report_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 8, 2, 1, 7),
    _MsanIgmpPortStatRxV3Report_Type()
)
msanIgmpPortStatRxV3Report.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanIgmpPortStatRxV3Report.setStatus("current")
_MsanIgmpPortStatTxV3Report_Type = Counter32
_MsanIgmpPortStatTxV3Report_Object = MibTableColumn
msanIgmpPortStatTxV3Report = _MsanIgmpPortStatTxV3Report_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 8, 2, 1, 8),
    _MsanIgmpPortStatTxV3Report_Type()
)
msanIgmpPortStatTxV3Report.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanIgmpPortStatTxV3Report.setStatus("current")
_MsanIgmpPortStatRxQuery_Type = Counter32
_MsanIgmpPortStatRxQuery_Object = MibTableColumn
msanIgmpPortStatRxQuery = _MsanIgmpPortStatRxQuery_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 8, 2, 1, 9),
    _MsanIgmpPortStatRxQuery_Type()
)
msanIgmpPortStatRxQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanIgmpPortStatRxQuery.setStatus("current")
_MsanIgmpPortStatRxError_Type = Counter32
_MsanIgmpPortStatRxError_Object = MibTableColumn
msanIgmpPortStatRxError = _MsanIgmpPortStatRxError_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 8, 2, 1, 10),
    _MsanIgmpPortStatRxError_Type()
)
msanIgmpPortStatRxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanIgmpPortStatRxError.setStatus("current")
_MsanIgmpPortStatRxBlockByIgmpFilter_Type = Counter32
_MsanIgmpPortStatRxBlockByIgmpFilter_Object = MibTableColumn
msanIgmpPortStatRxBlockByIgmpFilter = _MsanIgmpPortStatRxBlockByIgmpFilter_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 8, 2, 1, 11),
    _MsanIgmpPortStatRxBlockByIgmpFilter_Type()
)
msanIgmpPortStatRxBlockByIgmpFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanIgmpPortStatRxBlockByIgmpFilter.setStatus("current")
_MsanIgmpPortStatRxBlockByMcastAcl_Type = Counter32
_MsanIgmpPortStatRxBlockByMcastAcl_Object = MibTableColumn
msanIgmpPortStatRxBlockByMcastAcl = _MsanIgmpPortStatRxBlockByMcastAcl_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 8, 2, 1, 12),
    _MsanIgmpPortStatRxBlockByMcastAcl_Type()
)
msanIgmpPortStatRxBlockByMcastAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanIgmpPortStatRxBlockByMcastAcl.setStatus("current")
_MsanIgmpPortStatRxBlockByMcastCac_Type = Counter32
_MsanIgmpPortStatRxBlockByMcastCac_Object = MibTableColumn
msanIgmpPortStatRxBlockByMcastCac = _MsanIgmpPortStatRxBlockByMcastCac_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 8, 2, 1, 13),
    _MsanIgmpPortStatRxBlockByMcastCac_Type()
)
msanIgmpPortStatRxBlockByMcastCac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanIgmpPortStatRxBlockByMcastCac.setStatus("current")
_MsanIgmpPortStatTxQuery_Type = Counter32
_MsanIgmpPortStatTxQuery_Object = MibTableColumn
msanIgmpPortStatTxQuery = _MsanIgmpPortStatTxQuery_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 8, 2, 1, 14),
    _MsanIgmpPortStatTxQuery_Type()
)
msanIgmpPortStatTxQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanIgmpPortStatTxQuery.setStatus("current")
_MsanIgmpPortStatRxBlockByIgmpVersion_Type = Counter32
_MsanIgmpPortStatRxBlockByIgmpVersion_Object = MibTableColumn
msanIgmpPortStatRxBlockByIgmpVersion = _MsanIgmpPortStatRxBlockByIgmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 8, 8, 2, 1, 15),
    _MsanIgmpPortStatRxBlockByIgmpVersion_Type()
)
msanIgmpPortStatRxBlockByIgmpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanIgmpPortStatRxBlockByIgmpVersion.setStatus("current")
_MsanPort_ObjectIdentity = ObjectIdentity
msanPort = _MsanPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 10)
)
_MsanPortGlobal_ObjectIdentity = ObjectIdentity
msanPortGlobal = _MsanPortGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 10, 1)
)
_MsanPortTable_Object = MibTable
msanPortTable = _MsanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 10, 2)
)
if mibBuilder.loadTexts:
    msanPortTable.setStatus("current")
_MsanPortEntry_Object = MibTableRow
msanPortEntry = _MsanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 10, 2, 1)
)
msanPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    msanPortEntry.setStatus("current")


class _MsanPortMNFlag_Type(Integer32):
    """Custom type msanPortMNFlag based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanPortMNFlag_Type.__name__ = "Integer32"
_MsanPortMNFlag_Object = MibTableColumn
msanPortMNFlag = _MsanPortMNFlag_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 10, 2, 1, 1),
    _MsanPortMNFlag_Type()
)
msanPortMNFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanPortMNFlag.setStatus("current")


class _MsanPortMasterSlave_Type(Integer32):
    """Custom type msanPortMasterSlave based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("master", 2),
          ("none", 1),
          ("slave", 3))
    )


_MsanPortMasterSlave_Type.__name__ = "Integer32"
_MsanPortMasterSlave_Object = MibTableColumn
msanPortMasterSlave = _MsanPortMasterSlave_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 10, 2, 1, 6),
    _MsanPortMasterSlave_Type()
)
msanPortMasterSlave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanPortMasterSlave.setStatus("current")


class _MsanPortNegCapAdvertisedBits_Type(Bits):
    """Custom type msanPortNegCapAdvertisedBits based on Bits"""
    namedValues = NamedValues(
        *(("b1000baseT", 14),
          ("b1000baseTFD", 15),
          ("b1000baseX", 12),
          ("b1000baseXFD", 13),
          ("b100baseT2", 6),
          ("b100baseT2FD", 7),
          ("b100baseT4", 3),
          ("b100baseTX", 4),
          ("b100baseTXFD", 5),
          ("b10baseT", 1),
          ("b10baseTFD", 2),
          ("bFdxAPause", 9),
          ("bFdxBPause", 11),
          ("bFdxPause", 8),
          ("bFdxSPause", 10),
          ("bOther", 0))
    )

_MsanPortNegCapAdvertisedBits_Type.__name__ = "Bits"
_MsanPortNegCapAdvertisedBits_Object = MibTableColumn
msanPortNegCapAdvertisedBits = _MsanPortNegCapAdvertisedBits_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 10, 2, 1, 7),
    _MsanPortNegCapAdvertisedBits_Type()
)
msanPortNegCapAdvertisedBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanPortNegCapAdvertisedBits.setStatus("current")


class _MsanPortSpeedDuplex_Type(Integer32):
    """Custom type msanPortSpeedDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10,
              11,
              15,
              16,
              18,
              26,
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("speed1000MbpsFD", 30),
          ("speed1000MbpsFDFiber", 26),
          ("speed100MbpsFD", 16),
          ("speed100MbpsFDFiber", 18),
          ("speed100MbpsHD", 15),
          ("speed10GbpsFDFiber", 31),
          ("speed10MbpsFD", 11),
          ("speed10MbpsHD", 10))
    )


_MsanPortSpeedDuplex_Type.__name__ = "Integer32"
_MsanPortSpeedDuplex_Object = MibTableColumn
msanPortSpeedDuplex = _MsanPortSpeedDuplex_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 10, 2, 1, 8),
    _MsanPortSpeedDuplex_Type()
)
msanPortSpeedDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanPortSpeedDuplex.setStatus("current")


class _MsanPortStpP2PAutoState_Type(Integer32):
    """Custom type msanPortStpP2PAutoState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanPortStpP2PAutoState_Type.__name__ = "Integer32"
_MsanPortStpP2PAutoState_Object = MibTableColumn
msanPortStpP2PAutoState = _MsanPortStpP2PAutoState_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 10, 2, 1, 20),
    _MsanPortStpP2PAutoState_Type()
)
msanPortStpP2PAutoState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanPortStpP2PAutoState.setStatus("current")


class _MsanPortUsageType_Type(Integer32):
    """Custom type msanPortUsageType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("downlink", 2),
          ("uplink", 1))
    )


_MsanPortUsageType_Type.__name__ = "Integer32"
_MsanPortUsageType_Object = MibTableColumn
msanPortUsageType = _MsanPortUsageType_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 10, 2, 1, 21),
    _MsanPortUsageType_Type()
)
msanPortUsageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanPortUsageType.setStatus("current")
_MsanPppoeIA_ObjectIdentity = ObjectIdentity
msanPppoeIA = _MsanPppoeIA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 11)
)
_MsanPppoeIAGlobal_ObjectIdentity = ObjectIdentity
msanPppoeIAGlobal = _MsanPppoeIAGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 11, 1)
)


class _MsanPppoeIAStatus_Type(Integer32):
    """Custom type msanPppoeIAStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanPppoeIAStatus_Type.__name__ = "Integer32"
_MsanPppoeIAStatus_Object = MibScalar
msanPppoeIAStatus = _MsanPppoeIAStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 11, 1, 1),
    _MsanPppoeIAStatus_Type()
)
msanPppoeIAStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanPppoeIAStatus.setStatus("current")


class _MsanPppoeIAVsaReplyMode_Type(Integer32):
    """Custom type msanPppoeIAVsaReplyMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("keep", 1),
          ("remove", 2))
    )


_MsanPppoeIAVsaReplyMode_Type.__name__ = "Integer32"
_MsanPppoeIAVsaReplyMode_Object = MibScalar
msanPppoeIAVsaReplyMode = _MsanPppoeIAVsaReplyMode_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 11, 1, 2),
    _MsanPppoeIAVsaReplyMode_Type()
)
msanPppoeIAVsaReplyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanPppoeIAVsaReplyMode.setStatus("current")


class _MsanPppoeIACircuitIdStatus_Type(Integer32):
    """Custom type msanPppoeIACircuitIdStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanPppoeIACircuitIdStatus_Type.__name__ = "Integer32"
_MsanPppoeIACircuitIdStatus_Object = MibScalar
msanPppoeIACircuitIdStatus = _MsanPppoeIACircuitIdStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 11, 1, 3),
    _MsanPppoeIACircuitIdStatus_Type()
)
msanPppoeIACircuitIdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanPppoeIACircuitIdStatus.setStatus("current")


class _MsanPppoeIARemoteIdStatus_Type(Integer32):
    """Custom type msanPppoeIARemoteIdStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanPppoeIARemoteIdStatus_Type.__name__ = "Integer32"
_MsanPppoeIARemoteIdStatus_Object = MibScalar
msanPppoeIARemoteIdStatus = _MsanPppoeIARemoteIdStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 11, 1, 4),
    _MsanPppoeIARemoteIdStatus_Type()
)
msanPppoeIARemoteIdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanPppoeIARemoteIdStatus.setStatus("current")
_MsanPppoeIAPortTable_Object = MibTable
msanPppoeIAPortTable = _MsanPppoeIAPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 11, 2)
)
if mibBuilder.loadTexts:
    msanPppoeIAPortTable.setStatus("current")
_MsanPppoeIAPortEntry_Object = MibTableRow
msanPppoeIAPortEntry = _MsanPppoeIAPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 11, 2, 1)
)
msanPppoeIAPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    msanPppoeIAPortEntry.setStatus("current")


class _MsanPppoeIAPortStatus_Type(Integer32):
    """Custom type msanPppoeIAPortStatus based on Integer32"""
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
        *(("disable", 2),
          ("enable", 1),
          ("enableClient", 3),
          ("enableServer", 4))
    )


_MsanPppoeIAPortStatus_Type.__name__ = "Integer32"
_MsanPppoeIAPortStatus_Object = MibTableColumn
msanPppoeIAPortStatus = _MsanPppoeIAPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 11, 2, 1, 1),
    _MsanPppoeIAPortStatus_Type()
)
msanPppoeIAPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanPppoeIAPortStatus.setStatus("current")
_MsanPppoeIAPortRemoteId_Type = OctetString
_MsanPppoeIAPortRemoteId_Object = MibTableColumn
msanPppoeIAPortRemoteId = _MsanPppoeIAPortRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 11, 2, 1, 2),
    _MsanPppoeIAPortRemoteId_Type()
)
msanPppoeIAPortRemoteId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanPppoeIAPortRemoteId.setStatus("current")


class _MsanPppoeIAPortCircuitType_Type(Integer32):
    """Custom type msanPppoeIAPortCircuitType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("trusted", 1),
          ("untrusted", 2))
    )


_MsanPppoeIAPortCircuitType_Type.__name__ = "Integer32"
_MsanPppoeIAPortCircuitType_Object = MibTableColumn
msanPppoeIAPortCircuitType = _MsanPppoeIAPortCircuitType_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 11, 2, 1, 3),
    _MsanPppoeIAPortCircuitType_Type()
)
msanPppoeIAPortCircuitType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanPppoeIAPortCircuitType.setStatus("current")
_MsanPppoeIaStatistics_ObjectIdentity = ObjectIdentity
msanPppoeIaStatistics = _MsanPppoeIaStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 11, 3)
)
_MsanPppoeIaStatPADI_Type = Counter32
_MsanPppoeIaStatPADI_Object = MibScalar
msanPppoeIaStatPADI = _MsanPppoeIaStatPADI_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 11, 3, 1),
    _MsanPppoeIaStatPADI_Type()
)
msanPppoeIaStatPADI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanPppoeIaStatPADI.setStatus("current")
_MsanPppoeIaStatPADR_Type = Counter32
_MsanPppoeIaStatPADR_Object = MibScalar
msanPppoeIaStatPADR = _MsanPppoeIaStatPADR_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 11, 3, 2),
    _MsanPppoeIaStatPADR_Type()
)
msanPppoeIaStatPADR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanPppoeIaStatPADR.setStatus("current")
_MsanPppoeIaStatPADO_Type = Counter32
_MsanPppoeIaStatPADO_Object = MibScalar
msanPppoeIaStatPADO = _MsanPppoeIaStatPADO_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 11, 3, 3),
    _MsanPppoeIaStatPADO_Type()
)
msanPppoeIaStatPADO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanPppoeIaStatPADO.setStatus("current")
_MsanPppoeIaStatPADS_Type = Counter32
_MsanPppoeIaStatPADS_Object = MibScalar
msanPppoeIaStatPADS = _MsanPppoeIaStatPADS_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 11, 3, 4),
    _MsanPppoeIaStatPADS_Type()
)
msanPppoeIaStatPADS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanPppoeIaStatPADS.setStatus("current")
_MsanPppoeIaStatPADT_Type = Counter32
_MsanPppoeIaStatPADT_Object = MibScalar
msanPppoeIaStatPADT = _MsanPppoeIaStatPADT_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 11, 3, 5),
    _MsanPppoeIaStatPADT_Type()
)
msanPppoeIaStatPADT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanPppoeIaStatPADT.setStatus("current")
_MsanPppoeIaStatUnsutableFrames_Type = Counter32
_MsanPppoeIaStatUnsutableFrames_Object = MibScalar
msanPppoeIaStatUnsutableFrames = _MsanPppoeIaStatUnsutableFrames_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 11, 3, 6),
    _MsanPppoeIaStatUnsutableFrames_Type()
)
msanPppoeIaStatUnsutableFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanPppoeIaStatUnsutableFrames.setStatus("current")
_MsanPppoeIaStatUnknownFrames_Type = Counter32
_MsanPppoeIaStatUnknownFrames_Object = MibScalar
msanPppoeIaStatUnknownFrames = _MsanPppoeIaStatUnknownFrames_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 11, 3, 7),
    _MsanPppoeIaStatUnknownFrames_Type()
)
msanPppoeIaStatUnknownFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanPppoeIaStatUnknownFrames.setStatus("current")
_MsanPppoeIaStatInvalidFrames_Type = Counter32
_MsanPppoeIaStatInvalidFrames_Object = MibScalar
msanPppoeIaStatInvalidFrames = _MsanPppoeIaStatInvalidFrames_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 11, 3, 8),
    _MsanPppoeIaStatInvalidFrames_Type()
)
msanPppoeIaStatInvalidFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanPppoeIaStatInvalidFrames.setStatus("current")
_MsanPppoeIaPortStatisticsTable_Object = MibTable
msanPppoeIaPortStatisticsTable = _MsanPppoeIaPortStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 11, 3, 9)
)
if mibBuilder.loadTexts:
    msanPppoeIaPortStatisticsTable.setStatus("current")
_MsanPppoeIaPortStatisticsEntry_Object = MibTableRow
msanPppoeIaPortStatisticsEntry = _MsanPppoeIaPortStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 11, 3, 9, 1)
)
msanPppoeIaPortStatisticsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    msanPppoeIaPortStatisticsEntry.setStatus("current")
_MsanPppoeIaPortStatPADI_Type = Counter32
_MsanPppoeIaPortStatPADI_Object = MibTableColumn
msanPppoeIaPortStatPADI = _MsanPppoeIaPortStatPADI_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 11, 3, 9, 1, 1),
    _MsanPppoeIaPortStatPADI_Type()
)
msanPppoeIaPortStatPADI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanPppoeIaPortStatPADI.setStatus("current")
_MsanPppoeIaPortStatPADR_Type = Counter32
_MsanPppoeIaPortStatPADR_Object = MibTableColumn
msanPppoeIaPortStatPADR = _MsanPppoeIaPortStatPADR_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 11, 3, 9, 1, 2),
    _MsanPppoeIaPortStatPADR_Type()
)
msanPppoeIaPortStatPADR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanPppoeIaPortStatPADR.setStatus("current")
_MsanPppoeIaPortStatPADO_Type = Counter32
_MsanPppoeIaPortStatPADO_Object = MibTableColumn
msanPppoeIaPortStatPADO = _MsanPppoeIaPortStatPADO_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 11, 3, 9, 1, 3),
    _MsanPppoeIaPortStatPADO_Type()
)
msanPppoeIaPortStatPADO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanPppoeIaPortStatPADO.setStatus("current")
_MsanPppoeIaPortStatPADS_Type = Counter32
_MsanPppoeIaPortStatPADS_Object = MibTableColumn
msanPppoeIaPortStatPADS = _MsanPppoeIaPortStatPADS_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 11, 3, 9, 1, 4),
    _MsanPppoeIaPortStatPADS_Type()
)
msanPppoeIaPortStatPADS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanPppoeIaPortStatPADS.setStatus("current")
_MsanPppoeIaPortStatPADT_Type = Counter32
_MsanPppoeIaPortStatPADT_Object = MibTableColumn
msanPppoeIaPortStatPADT = _MsanPppoeIaPortStatPADT_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 11, 3, 9, 1, 5),
    _MsanPppoeIaPortStatPADT_Type()
)
msanPppoeIaPortStatPADT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanPppoeIaPortStatPADT.setStatus("current")
_MsanPppoeIaPortStatUnsutableFrames_Type = Counter32
_MsanPppoeIaPortStatUnsutableFrames_Object = MibTableColumn
msanPppoeIaPortStatUnsutableFrames = _MsanPppoeIaPortStatUnsutableFrames_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 11, 3, 9, 1, 6),
    _MsanPppoeIaPortStatUnsutableFrames_Type()
)
msanPppoeIaPortStatUnsutableFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanPppoeIaPortStatUnsutableFrames.setStatus("current")
_MsanPppoeIaPortStatUnknownFrames_Type = Counter32
_MsanPppoeIaPortStatUnknownFrames_Object = MibTableColumn
msanPppoeIaPortStatUnknownFrames = _MsanPppoeIaPortStatUnknownFrames_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 11, 3, 9, 1, 7),
    _MsanPppoeIaPortStatUnknownFrames_Type()
)
msanPppoeIaPortStatUnknownFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanPppoeIaPortStatUnknownFrames.setStatus("current")
_MsanPppoeIaPortStatInvalidFrames_Type = Counter32
_MsanPppoeIaPortStatInvalidFrames_Object = MibTableColumn
msanPppoeIaPortStatInvalidFrames = _MsanPppoeIaPortStatInvalidFrames_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 11, 3, 9, 1, 8),
    _MsanPppoeIaPortStatInvalidFrames_Type()
)
msanPppoeIaPortStatInvalidFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanPppoeIaPortStatInvalidFrames.setStatus("current")
_MsanPppoeIaVlanTable_Object = MibTable
msanPppoeIaVlanTable = _MsanPppoeIaVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 11, 4)
)
if mibBuilder.loadTexts:
    msanPppoeIaVlanTable.setStatus("current")
_MsanPppoeIaVlanEntry_Object = MibTableRow
msanPppoeIaVlanEntry = _MsanPppoeIaVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 11, 4, 1)
)
msanPppoeIaVlanEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    msanPppoeIaVlanEntry.setStatus("current")


class _MsanPppoeIaVlanStatus_Type(Integer32):
    """Custom type msanPppoeIaVlanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanPppoeIaVlanStatus_Type.__name__ = "Integer32"
_MsanPppoeIaVlanStatus_Object = MibTableColumn
msanPppoeIaVlanStatus = _MsanPppoeIaVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 11, 4, 1, 1),
    _MsanPppoeIaVlanStatus_Type()
)
msanPppoeIaVlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanPppoeIaVlanStatus.setStatus("current")
_MsanQoS_ObjectIdentity = ObjectIdentity
msanQoS = _MsanQoS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12)
)
_MsanQosGlobal_ObjectIdentity = ObjectIdentity
msanQosGlobal = _MsanQosGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 1)
)
_MsanIpAclRuleTable_Object = MibTable
msanIpAclRuleTable = _MsanIpAclRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 2)
)
if mibBuilder.loadTexts:
    msanIpAclRuleTable.setStatus("current")
_MsanIpAclRuleEntry_Object = MibTableRow
msanIpAclRuleEntry = _MsanIpAclRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 2, 1)
)
msanIpAclRuleEntry.setIndexNames(
    (0, "ISKRATEL-MSAN-MIB", "msanIpAclIndex"),
    (0, "ISKRATEL-MSAN-MIB", "msanIpAclRuleIndex"),
)
if mibBuilder.loadTexts:
    msanIpAclRuleEntry.setStatus("current")


class _MsanIpAclIndex_Type(Integer32):
    """Custom type msanIpAclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 199),
    )


_MsanIpAclIndex_Type.__name__ = "Integer32"
_MsanIpAclIndex_Object = MibTableColumn
msanIpAclIndex = _MsanIpAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 2, 1, 1),
    _MsanIpAclIndex_Type()
)
msanIpAclIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanIpAclIndex.setStatus("current")


class _MsanIpAclRuleIndex_Type(Integer32):
    """Custom type msanIpAclRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_MsanIpAclRuleIndex_Type.__name__ = "Integer32"
_MsanIpAclRuleIndex_Object = MibTableColumn
msanIpAclRuleIndex = _MsanIpAclRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 2, 1, 2),
    _MsanIpAclRuleIndex_Type()
)
msanIpAclRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanIpAclRuleIndex.setStatus("current")


class _MsanIpAclRuleAssignVlanId_Type(Integer32):
    """Custom type msanIpAclRuleAssignVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MsanIpAclRuleAssignVlanId_Type.__name__ = "Integer32"
_MsanIpAclRuleAssignVlanId_Object = MibTableColumn
msanIpAclRuleAssignVlanId = _MsanIpAclRuleAssignVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 2, 1, 3),
    _MsanIpAclRuleAssignVlanId_Type()
)
msanIpAclRuleAssignVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIpAclRuleAssignVlanId.setStatus("current")
_MsanIpAclRuleAssignCoSPriority_Type = Integer32
_MsanIpAclRuleAssignCoSPriority_Object = MibTableColumn
msanIpAclRuleAssignCoSPriority = _MsanIpAclRuleAssignCoSPriority_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 2, 1, 4),
    _MsanIpAclRuleAssignCoSPriority_Type()
)
msanIpAclRuleAssignCoSPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIpAclRuleAssignCoSPriority.setStatus("deprecated")
_MsanIpAclRuleEgressIntf_Type = Integer32
_MsanIpAclRuleEgressIntf_Object = MibTableColumn
msanIpAclRuleEgressIntf = _MsanIpAclRuleEgressIntf_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 2, 1, 5),
    _MsanIpAclRuleEgressIntf_Type()
)
msanIpAclRuleEgressIntf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIpAclRuleEgressIntf.setStatus("deprecated")


class _MsanIpAclRuleAssignVlanId2_Type(Integer32):
    """Custom type msanIpAclRuleAssignVlanId2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MsanIpAclRuleAssignVlanId2_Type.__name__ = "Integer32"
_MsanIpAclRuleAssignVlanId2_Object = MibTableColumn
msanIpAclRuleAssignVlanId2 = _MsanIpAclRuleAssignVlanId2_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 2, 1, 6),
    _MsanIpAclRuleAssignVlanId2_Type()
)
msanIpAclRuleAssignVlanId2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIpAclRuleAssignVlanId2.setStatus("current")


class _MsanIpAclRuleRemoveVlanId_Type(Integer32):
    """Custom type msanIpAclRuleRemoveVlanId based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanIpAclRuleRemoveVlanId_Type.__name__ = "Integer32"
_MsanIpAclRuleRemoveVlanId_Object = MibTableColumn
msanIpAclRuleRemoveVlanId = _MsanIpAclRuleRemoveVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 2, 1, 7),
    _MsanIpAclRuleRemoveVlanId_Type()
)
msanIpAclRuleRemoveVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIpAclRuleRemoveVlanId.setStatus("current")


class _MsanIpAclRuleIcmpType_Type(Integer32):
    """Custom type msanIpAclRuleIcmpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              4,
              5,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("addressMaskReply", 18),
          ("addressMaskRequest", 17),
          ("destinationUnreachable", 3),
          ("echoReply", 0),
          ("echoRequest", 8),
          ("informationReply", 16),
          ("informationRequest", 15),
          ("parameterProblem", 12),
          ("redirect", 5),
          ("routerAdvertisement", 9),
          ("routerSolicitation", 10),
          ("sourceQuench", 4),
          ("timeExceeded", 11),
          ("timestampReply", 14),
          ("timestampRequest", 13))
    )


_MsanIpAclRuleIcmpType_Type.__name__ = "Integer32"
_MsanIpAclRuleIcmpType_Object = MibTableColumn
msanIpAclRuleIcmpType = _MsanIpAclRuleIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 2, 1, 8),
    _MsanIpAclRuleIcmpType_Type()
)
msanIpAclRuleIcmpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIpAclRuleIcmpType.setStatus("deprecated")
_MsanIpAclRuleDestMacAddr_Type = MacAddress
_MsanIpAclRuleDestMacAddr_Object = MibTableColumn
msanIpAclRuleDestMacAddr = _MsanIpAclRuleDestMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 2, 1, 9),
    _MsanIpAclRuleDestMacAddr_Type()
)
msanIpAclRuleDestMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIpAclRuleDestMacAddr.setStatus("current")
_MsanIpAclRuleDestMacMask_Type = MacAddress
_MsanIpAclRuleDestMacMask_Object = MibTableColumn
msanIpAclRuleDestMacMask = _MsanIpAclRuleDestMacMask_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 2, 1, 10),
    _MsanIpAclRuleDestMacMask_Type()
)
msanIpAclRuleDestMacMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIpAclRuleDestMacMask.setStatus("current")
_MsanIpAclRuleSrcMacAddr_Type = MacAddress
_MsanIpAclRuleSrcMacAddr_Object = MibTableColumn
msanIpAclRuleSrcMacAddr = _MsanIpAclRuleSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 2, 1, 11),
    _MsanIpAclRuleSrcMacAddr_Type()
)
msanIpAclRuleSrcMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIpAclRuleSrcMacAddr.setStatus("current")
_MsanIpAclRuleSrcMacMask_Type = MacAddress
_MsanIpAclRuleSrcMacMask_Object = MibTableColumn
msanIpAclRuleSrcMacMask = _MsanIpAclRuleSrcMacMask_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 2, 1, 12),
    _MsanIpAclRuleSrcMacMask_Type()
)
msanIpAclRuleSrcMacMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIpAclRuleSrcMacMask.setStatus("current")


class _MsanIpAclRuleCos_Type(Integer32):
    """Custom type msanIpAclRuleCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MsanIpAclRuleCos_Type.__name__ = "Integer32"
_MsanIpAclRuleCos_Object = MibTableColumn
msanIpAclRuleCos = _MsanIpAclRuleCos_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 2, 1, 13),
    _MsanIpAclRuleCos_Type()
)
msanIpAclRuleCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIpAclRuleCos.setStatus("current")


class _MsanIpAclRuleCos2_Type(Integer32):
    """Custom type msanIpAclRuleCos2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MsanIpAclRuleCos2_Type.__name__ = "Integer32"
_MsanIpAclRuleCos2_Object = MibTableColumn
msanIpAclRuleCos2 = _MsanIpAclRuleCos2_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 2, 1, 14),
    _MsanIpAclRuleCos2_Type()
)
msanIpAclRuleCos2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIpAclRuleCos2.setStatus("current")


class _MsanIpAclRuleVlanId_Type(Unsigned32):
    """Custom type msanIpAclRuleVlanId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MsanIpAclRuleVlanId_Type.__name__ = "Unsigned32"
_MsanIpAclRuleVlanId_Object = MibTableColumn
msanIpAclRuleVlanId = _MsanIpAclRuleVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 2, 1, 15),
    _MsanIpAclRuleVlanId_Type()
)
msanIpAclRuleVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIpAclRuleVlanId.setStatus("current")


class _MsanIpAclRuleVlanId2_Type(Unsigned32):
    """Custom type msanIpAclRuleVlanId2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MsanIpAclRuleVlanId2_Type.__name__ = "Unsigned32"
_MsanIpAclRuleVlanId2_Object = MibTableColumn
msanIpAclRuleVlanId2 = _MsanIpAclRuleVlanId2_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 2, 1, 16),
    _MsanIpAclRuleVlanId2_Type()
)
msanIpAclRuleVlanId2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIpAclRuleVlanId2.setStatus("current")


class _MsanIpAclRuleCVlanId_Type(Integer32):
    """Custom type msanIpAclRuleCVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MsanIpAclRuleCVlanId_Type.__name__ = "Integer32"
_MsanIpAclRuleCVlanId_Object = MibTableColumn
msanIpAclRuleCVlanId = _MsanIpAclRuleCVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 2, 1, 17),
    _MsanIpAclRuleCVlanId_Type()
)
msanIpAclRuleCVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIpAclRuleCVlanId.setStatus("current")


class _MsanIpAclRuleSVlanId_Type(Integer32):
    """Custom type msanIpAclRuleSVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MsanIpAclRuleSVlanId_Type.__name__ = "Integer32"
_MsanIpAclRuleSVlanId_Object = MibTableColumn
msanIpAclRuleSVlanId = _MsanIpAclRuleSVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 2, 1, 18),
    _MsanIpAclRuleSVlanId_Type()
)
msanIpAclRuleSVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIpAclRuleSVlanId.setStatus("current")


class _MsanIpAclRuleAssignCVlanId_Type(Integer32):
    """Custom type msanIpAclRuleAssignCVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MsanIpAclRuleAssignCVlanId_Type.__name__ = "Integer32"
_MsanIpAclRuleAssignCVlanId_Object = MibTableColumn
msanIpAclRuleAssignCVlanId = _MsanIpAclRuleAssignCVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 2, 1, 19),
    _MsanIpAclRuleAssignCVlanId_Type()
)
msanIpAclRuleAssignCVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIpAclRuleAssignCVlanId.setStatus("current")


class _MsanIpAclRuleAssignSVlanId_Type(Integer32):
    """Custom type msanIpAclRuleAssignSVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MsanIpAclRuleAssignSVlanId_Type.__name__ = "Integer32"
_MsanIpAclRuleAssignSVlanId_Object = MibTableColumn
msanIpAclRuleAssignSVlanId = _MsanIpAclRuleAssignSVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 2, 1, 20),
    _MsanIpAclRuleAssignSVlanId_Type()
)
msanIpAclRuleAssignSVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIpAclRuleAssignSVlanId.setStatus("current")


class _MsanIpAclRuleRemoveSVlanId_Type(Integer32):
    """Custom type msanIpAclRuleRemoveSVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanIpAclRuleRemoveSVlanId_Type.__name__ = "Integer32"
_MsanIpAclRuleRemoveSVlanId_Object = MibTableColumn
msanIpAclRuleRemoveSVlanId = _MsanIpAclRuleRemoveSVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 2, 1, 21),
    _MsanIpAclRuleRemoveSVlanId_Type()
)
msanIpAclRuleRemoveSVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIpAclRuleRemoveSVlanId.setStatus("current")


class _MsanIpAclRuleVlanIdRangeStart_Type(Unsigned32):
    """Custom type msanIpAclRuleVlanIdRangeStart based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MsanIpAclRuleVlanIdRangeStart_Type.__name__ = "Unsigned32"
_MsanIpAclRuleVlanIdRangeStart_Object = MibTableColumn
msanIpAclRuleVlanIdRangeStart = _MsanIpAclRuleVlanIdRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 2, 1, 22),
    _MsanIpAclRuleVlanIdRangeStart_Type()
)
msanIpAclRuleVlanIdRangeStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIpAclRuleVlanIdRangeStart.setStatus("current")


class _MsanIpAclRuleVlanIdRangeEnd_Type(Unsigned32):
    """Custom type msanIpAclRuleVlanIdRangeEnd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MsanIpAclRuleVlanIdRangeEnd_Type.__name__ = "Unsigned32"
_MsanIpAclRuleVlanIdRangeEnd_Object = MibTableColumn
msanIpAclRuleVlanIdRangeEnd = _MsanIpAclRuleVlanIdRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 2, 1, 23),
    _MsanIpAclRuleVlanIdRangeEnd_Type()
)
msanIpAclRuleVlanIdRangeEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIpAclRuleVlanIdRangeEnd.setStatus("current")


class _MsanIpAclRuleVlanId2RangeStart_Type(Unsigned32):
    """Custom type msanIpAclRuleVlanId2RangeStart based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MsanIpAclRuleVlanId2RangeStart_Type.__name__ = "Unsigned32"
_MsanIpAclRuleVlanId2RangeStart_Object = MibTableColumn
msanIpAclRuleVlanId2RangeStart = _MsanIpAclRuleVlanId2RangeStart_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 2, 1, 24),
    _MsanIpAclRuleVlanId2RangeStart_Type()
)
msanIpAclRuleVlanId2RangeStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIpAclRuleVlanId2RangeStart.setStatus("current")


class _MsanIpAclRuleVlanId2RangeEnd_Type(Unsigned32):
    """Custom type msanIpAclRuleVlanId2RangeEnd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MsanIpAclRuleVlanId2RangeEnd_Type.__name__ = "Unsigned32"
_MsanIpAclRuleVlanId2RangeEnd_Object = MibTableColumn
msanIpAclRuleVlanId2RangeEnd = _MsanIpAclRuleVlanId2RangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 2, 1, 25),
    _MsanIpAclRuleVlanId2RangeEnd_Type()
)
msanIpAclRuleVlanId2RangeEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIpAclRuleVlanId2RangeEnd.setStatus("current")


class _MsanIpAclRuleSVlanIdRangeStart_Type(Unsigned32):
    """Custom type msanIpAclRuleSVlanIdRangeStart based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MsanIpAclRuleSVlanIdRangeStart_Type.__name__ = "Unsigned32"
_MsanIpAclRuleSVlanIdRangeStart_Object = MibTableColumn
msanIpAclRuleSVlanIdRangeStart = _MsanIpAclRuleSVlanIdRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 2, 1, 26),
    _MsanIpAclRuleSVlanIdRangeStart_Type()
)
msanIpAclRuleSVlanIdRangeStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIpAclRuleSVlanIdRangeStart.setStatus("current")


class _MsanIpAclRuleSVlanIdRangeEnd_Type(Unsigned32):
    """Custom type msanIpAclRuleSVlanIdRangeEnd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MsanIpAclRuleSVlanIdRangeEnd_Type.__name__ = "Unsigned32"
_MsanIpAclRuleSVlanIdRangeEnd_Object = MibTableColumn
msanIpAclRuleSVlanIdRangeEnd = _MsanIpAclRuleSVlanIdRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 2, 1, 27),
    _MsanIpAclRuleSVlanIdRangeEnd_Type()
)
msanIpAclRuleSVlanIdRangeEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIpAclRuleSVlanIdRangeEnd.setStatus("current")


class _MsanIpAclRuleCVlanIdRangeStart_Type(Unsigned32):
    """Custom type msanIpAclRuleCVlanIdRangeStart based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MsanIpAclRuleCVlanIdRangeStart_Type.__name__ = "Unsigned32"
_MsanIpAclRuleCVlanIdRangeStart_Object = MibTableColumn
msanIpAclRuleCVlanIdRangeStart = _MsanIpAclRuleCVlanIdRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 2, 1, 28),
    _MsanIpAclRuleCVlanIdRangeStart_Type()
)
msanIpAclRuleCVlanIdRangeStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIpAclRuleCVlanIdRangeStart.setStatus("current")


class _MsanIpAclRuleCVlanIdRangeEnd_Type(Unsigned32):
    """Custom type msanIpAclRuleCVlanIdRangeEnd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MsanIpAclRuleCVlanIdRangeEnd_Type.__name__ = "Unsigned32"
_MsanIpAclRuleCVlanIdRangeEnd_Object = MibTableColumn
msanIpAclRuleCVlanIdRangeEnd = _MsanIpAclRuleCVlanIdRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 2, 1, 29),
    _MsanIpAclRuleCVlanIdRangeEnd_Type()
)
msanIpAclRuleCVlanIdRangeEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIpAclRuleCVlanIdRangeEnd.setStatus("current")
_MsanIpAclRuleSrcIpv6Address_Type = InetAddressIPv6
_MsanIpAclRuleSrcIpv6Address_Object = MibTableColumn
msanIpAclRuleSrcIpv6Address = _MsanIpAclRuleSrcIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 2, 1, 31),
    _MsanIpAclRuleSrcIpv6Address_Type()
)
msanIpAclRuleSrcIpv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIpAclRuleSrcIpv6Address.setStatus("current")


class _MsanIpAclRuleSrcIpv6AddressMaskLen_Type(Integer32):
    """Custom type msanIpAclRuleSrcIpv6AddressMaskLen based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_MsanIpAclRuleSrcIpv6AddressMaskLen_Type.__name__ = "Integer32"
_MsanIpAclRuleSrcIpv6AddressMaskLen_Object = MibTableColumn
msanIpAclRuleSrcIpv6AddressMaskLen = _MsanIpAclRuleSrcIpv6AddressMaskLen_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 2, 1, 32),
    _MsanIpAclRuleSrcIpv6AddressMaskLen_Type()
)
msanIpAclRuleSrcIpv6AddressMaskLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIpAclRuleSrcIpv6AddressMaskLen.setStatus("current")
_MsanIpAclRuleDestIpv6Address_Type = InetAddressIPv6
_MsanIpAclRuleDestIpv6Address_Object = MibTableColumn
msanIpAclRuleDestIpv6Address = _MsanIpAclRuleDestIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 2, 1, 33),
    _MsanIpAclRuleDestIpv6Address_Type()
)
msanIpAclRuleDestIpv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIpAclRuleDestIpv6Address.setStatus("current")


class _MsanIpAclRuleDestIpv6AddressMaskLen_Type(Integer32):
    """Custom type msanIpAclRuleDestIpv6AddressMaskLen based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_MsanIpAclRuleDestIpv6AddressMaskLen_Type.__name__ = "Integer32"
_MsanIpAclRuleDestIpv6AddressMaskLen_Object = MibTableColumn
msanIpAclRuleDestIpv6AddressMaskLen = _MsanIpAclRuleDestIpv6AddressMaskLen_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 2, 1, 34),
    _MsanIpAclRuleDestIpv6AddressMaskLen_Type()
)
msanIpAclRuleDestIpv6AddressMaskLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIpAclRuleDestIpv6AddressMaskLen.setStatus("current")
_MsanMacAclRuleTable_Object = MibTable
msanMacAclRuleTable = _MsanMacAclRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 3)
)
if mibBuilder.loadTexts:
    msanMacAclRuleTable.setStatus("current")
_MsanMacAclRuleEntry_Object = MibTableRow
msanMacAclRuleEntry = _MsanMacAclRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 3, 1)
)
msanMacAclRuleEntry.setIndexNames(
    (0, "ISKRATEL-MSAN-MIB", "msanMacAclIndex"),
    (0, "ISKRATEL-MSAN-MIB", "msanMacAclRuleIndex"),
)
if mibBuilder.loadTexts:
    msanMacAclRuleEntry.setStatus("current")


class _MsanMacAclIndex_Type(Integer32):
    """Custom type msanMacAclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_MsanMacAclIndex_Type.__name__ = "Integer32"
_MsanMacAclIndex_Object = MibTableColumn
msanMacAclIndex = _MsanMacAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 3, 1, 1),
    _MsanMacAclIndex_Type()
)
msanMacAclIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanMacAclIndex.setStatus("current")


class _MsanMacAclRuleIndex_Type(Integer32):
    """Custom type msanMacAclRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_MsanMacAclRuleIndex_Type.__name__ = "Integer32"
_MsanMacAclRuleIndex_Object = MibTableColumn
msanMacAclRuleIndex = _MsanMacAclRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 3, 1, 2),
    _MsanMacAclRuleIndex_Type()
)
msanMacAclRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanMacAclRuleIndex.setStatus("current")
_MsanMacAclRuleEgressIntf_Type = Integer32
_MsanMacAclRuleEgressIntf_Object = MibTableColumn
msanMacAclRuleEgressIntf = _MsanMacAclRuleEgressIntf_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 3, 1, 3),
    _MsanMacAclRuleEgressIntf_Type()
)
msanMacAclRuleEgressIntf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanMacAclRuleEgressIntf.setStatus("deprecated")


class _MsanMacAclRuleAssignVlanId_Type(Integer32):
    """Custom type msanMacAclRuleAssignVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MsanMacAclRuleAssignVlanId_Type.__name__ = "Integer32"
_MsanMacAclRuleAssignVlanId_Object = MibTableColumn
msanMacAclRuleAssignVlanId = _MsanMacAclRuleAssignVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 3, 1, 4),
    _MsanMacAclRuleAssignVlanId_Type()
)
msanMacAclRuleAssignVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanMacAclRuleAssignVlanId.setStatus("current")
_MsanMacAclRuleAssignCoSPriority_Type = Integer32
_MsanMacAclRuleAssignCoSPriority_Object = MibTableColumn
msanMacAclRuleAssignCoSPriority = _MsanMacAclRuleAssignCoSPriority_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 3, 1, 5),
    _MsanMacAclRuleAssignCoSPriority_Type()
)
msanMacAclRuleAssignCoSPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanMacAclRuleAssignCoSPriority.setStatus("deprecated")


class _MsanMacAclRuleAssignVlanId2_Type(Integer32):
    """Custom type msanMacAclRuleAssignVlanId2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MsanMacAclRuleAssignVlanId2_Type.__name__ = "Integer32"
_MsanMacAclRuleAssignVlanId2_Object = MibTableColumn
msanMacAclRuleAssignVlanId2 = _MsanMacAclRuleAssignVlanId2_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 3, 1, 6),
    _MsanMacAclRuleAssignVlanId2_Type()
)
msanMacAclRuleAssignVlanId2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanMacAclRuleAssignVlanId2.setStatus("current")


class _MsanMacAclRuleRemoveVlanId_Type(Integer32):
    """Custom type msanMacAclRuleRemoveVlanId based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanMacAclRuleRemoveVlanId_Type.__name__ = "Integer32"
_MsanMacAclRuleRemoveVlanId_Object = MibTableColumn
msanMacAclRuleRemoveVlanId = _MsanMacAclRuleRemoveVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 3, 1, 7),
    _MsanMacAclRuleRemoveVlanId_Type()
)
msanMacAclRuleRemoveVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanMacAclRuleRemoveVlanId.setStatus("current")
_MsanMacAclRuleCVlanId_Type = Integer32
_MsanMacAclRuleCVlanId_Object = MibTableColumn
msanMacAclRuleCVlanId = _MsanMacAclRuleCVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 3, 1, 8),
    _MsanMacAclRuleCVlanId_Type()
)
msanMacAclRuleCVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanMacAclRuleCVlanId.setStatus("current")
_MsanMacAclRuleSVlanId_Type = Integer32
_MsanMacAclRuleSVlanId_Object = MibTableColumn
msanMacAclRuleSVlanId = _MsanMacAclRuleSVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 3, 1, 9),
    _MsanMacAclRuleSVlanId_Type()
)
msanMacAclRuleSVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanMacAclRuleSVlanId.setStatus("current")


class _MsanMacAclRuleAssignCVlanId_Type(Integer32):
    """Custom type msanMacAclRuleAssignCVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MsanMacAclRuleAssignCVlanId_Type.__name__ = "Integer32"
_MsanMacAclRuleAssignCVlanId_Object = MibTableColumn
msanMacAclRuleAssignCVlanId = _MsanMacAclRuleAssignCVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 3, 1, 10),
    _MsanMacAclRuleAssignCVlanId_Type()
)
msanMacAclRuleAssignCVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanMacAclRuleAssignCVlanId.setStatus("current")


class _MsanMacAclRuleAssignSVlanId_Type(Integer32):
    """Custom type msanMacAclRuleAssignSVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MsanMacAclRuleAssignSVlanId_Type.__name__ = "Integer32"
_MsanMacAclRuleAssignSVlanId_Object = MibTableColumn
msanMacAclRuleAssignSVlanId = _MsanMacAclRuleAssignSVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 3, 1, 11),
    _MsanMacAclRuleAssignSVlanId_Type()
)
msanMacAclRuleAssignSVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanMacAclRuleAssignSVlanId.setStatus("current")


class _MsanMacAclRuleRemoveSVlanId_Type(Integer32):
    """Custom type msanMacAclRuleRemoveSVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanMacAclRuleRemoveSVlanId_Type.__name__ = "Integer32"
_MsanMacAclRuleRemoveSVlanId_Object = MibTableColumn
msanMacAclRuleRemoveSVlanId = _MsanMacAclRuleRemoveSVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 3, 1, 12),
    _MsanMacAclRuleRemoveSVlanId_Type()
)
msanMacAclRuleRemoveSVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanMacAclRuleRemoveSVlanId.setStatus("current")


class _MsanMacAclRuleSVlanIdRangeStart_Type(Unsigned32):
    """Custom type msanMacAclRuleSVlanIdRangeStart based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MsanMacAclRuleSVlanIdRangeStart_Type.__name__ = "Unsigned32"
_MsanMacAclRuleSVlanIdRangeStart_Object = MibTableColumn
msanMacAclRuleSVlanIdRangeStart = _MsanMacAclRuleSVlanIdRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 3, 1, 13),
    _MsanMacAclRuleSVlanIdRangeStart_Type()
)
msanMacAclRuleSVlanIdRangeStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanMacAclRuleSVlanIdRangeStart.setStatus("current")


class _MsanMacAclRuleSVlanIdRangeEnd_Type(Unsigned32):
    """Custom type msanMacAclRuleSVlanIdRangeEnd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MsanMacAclRuleSVlanIdRangeEnd_Type.__name__ = "Unsigned32"
_MsanMacAclRuleSVlanIdRangeEnd_Object = MibTableColumn
msanMacAclRuleSVlanIdRangeEnd = _MsanMacAclRuleSVlanIdRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 3, 1, 14),
    _MsanMacAclRuleSVlanIdRangeEnd_Type()
)
msanMacAclRuleSVlanIdRangeEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanMacAclRuleSVlanIdRangeEnd.setStatus("current")


class _MsanMacAclRuleCVlanIdRangeStart_Type(Unsigned32):
    """Custom type msanMacAclRuleCVlanIdRangeStart based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MsanMacAclRuleCVlanIdRangeStart_Type.__name__ = "Unsigned32"
_MsanMacAclRuleCVlanIdRangeStart_Object = MibTableColumn
msanMacAclRuleCVlanIdRangeStart = _MsanMacAclRuleCVlanIdRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 3, 1, 15),
    _MsanMacAclRuleCVlanIdRangeStart_Type()
)
msanMacAclRuleCVlanIdRangeStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanMacAclRuleCVlanIdRangeStart.setStatus("current")


class _MsanMacAclRuleCVlanIdRangeEnd_Type(Unsigned32):
    """Custom type msanMacAclRuleCVlanIdRangeEnd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MsanMacAclRuleCVlanIdRangeEnd_Type.__name__ = "Unsigned32"
_MsanMacAclRuleCVlanIdRangeEnd_Object = MibTableColumn
msanMacAclRuleCVlanIdRangeEnd = _MsanMacAclRuleCVlanIdRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 3, 1, 16),
    _MsanMacAclRuleCVlanIdRangeEnd_Type()
)
msanMacAclRuleCVlanIdRangeEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanMacAclRuleCVlanIdRangeEnd.setStatus("current")
_MsanCosQueueControlTable_Object = MibTable
msanCosQueueControlTable = _MsanCosQueueControlTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 4)
)
if mibBuilder.loadTexts:
    msanCosQueueControlTable.setStatus("current")
_MsanCosQueueControlEntry_Object = MibTableRow
msanCosQueueControlEntry = _MsanCosQueueControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 4, 1)
)
msanCosQueueControlEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    msanCosQueueControlEntry.setStatus("current")
_MsanCosQueueControlIntfBurstSize_Type = Integer32
_MsanCosQueueControlIntfBurstSize_Object = MibTableColumn
msanCosQueueControlIntfBurstSize = _MsanCosQueueControlIntfBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 4, 1, 1),
    _MsanCosQueueControlIntfBurstSize_Type()
)
msanCosQueueControlIntfBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanCosQueueControlIntfBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    msanCosQueueControlIntfBurstSize.setUnits("kilobyte")


class _MsanCosQueueIntfShapingRate_Type(Unsigned32):
    """Custom type msanCosQueueIntfShapingRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_MsanCosQueueIntfShapingRate_Type.__name__ = "Unsigned32"
_MsanCosQueueIntfShapingRate_Object = MibTableColumn
msanCosQueueIntfShapingRate = _MsanCosQueueIntfShapingRate_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 4, 1, 2),
    _MsanCosQueueIntfShapingRate_Type()
)
msanCosQueueIntfShapingRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanCosQueueIntfShapingRate.setStatus("current")
if mibBuilder.loadTexts:
    msanCosQueueIntfShapingRate.setUnits("kbps")
_MsanCosQueueTable_Object = MibTable
msanCosQueueTable = _MsanCosQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 5)
)
if mibBuilder.loadTexts:
    msanCosQueueTable.setStatus("current")
_MsanCosQueueEntry_Object = MibTableRow
msanCosQueueEntry = _MsanCosQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 5, 1)
)
msanCosQueueEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ISKRATEL-MSAN-MIB", "msanCosQueueIndex"),
)
if mibBuilder.loadTexts:
    msanCosQueueEntry.setStatus("current")


class _MsanCosQueueIndex_Type(Integer32):
    """Custom type msanCosQueueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_MsanCosQueueIndex_Type.__name__ = "Integer32"
_MsanCosQueueIndex_Object = MibTableColumn
msanCosQueueIndex = _MsanCosQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 5, 1, 1),
    _MsanCosQueueIndex_Type()
)
msanCosQueueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanCosQueueIndex.setStatus("current")


class _MsanCosQueueWeight_Type(Integer32):
    """Custom type msanCosQueueWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_MsanCosQueueWeight_Type.__name__ = "Integer32"
_MsanCosQueueWeight_Object = MibTableColumn
msanCosQueueWeight = _MsanCosQueueWeight_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 5, 1, 2),
    _MsanCosQueueWeight_Type()
)
msanCosQueueWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanCosQueueWeight.setStatus("current")


class _MsanCosQueueLength_Type(Integer32):
    """Custom type msanCosQueueLength based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 156),
    )


_MsanCosQueueLength_Type.__name__ = "Integer32"
_MsanCosQueueLength_Object = MibTableColumn
msanCosQueueLength = _MsanCosQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 5, 1, 3),
    _MsanCosQueueLength_Type()
)
msanCosQueueLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanCosQueueLength.setStatus("current")
_MsanCosMapIntfTrustTable_Object = MibTable
msanCosMapIntfTrustTable = _MsanCosMapIntfTrustTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 6)
)
if mibBuilder.loadTexts:
    msanCosMapIntfTrustTable.setStatus("current")
_MsanCosMapIntfTrustEntry_Object = MibTableRow
msanCosMapIntfTrustEntry = _MsanCosMapIntfTrustEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 6, 1)
)
msanCosMapIntfTrustEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    msanCosMapIntfTrustEntry.setStatus("current")


class _MsanCosMapIntfTrustMode_Type(Integer32):
    """Custom type msanCosMapIntfTrustMode based on Integer32"""
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
        *(("trustDot1p", 2),
          ("trustIpDscp", 4),
          ("trustIpPrecedence", 3),
          ("untrusted", 1))
    )


_MsanCosMapIntfTrustMode_Type.__name__ = "Integer32"
_MsanCosMapIntfTrustMode_Object = MibTableColumn
msanCosMapIntfTrustMode = _MsanCosMapIntfTrustMode_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 6, 1, 1),
    _MsanCosMapIntfTrustMode_Type()
)
msanCosMapIntfTrustMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanCosMapIntfTrustMode.setStatus("current")
_MsanQosProfileTable_Object = MibTable
msanQosProfileTable = _MsanQosProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 7)
)
if mibBuilder.loadTexts:
    msanQosProfileTable.setStatus("current")
_MsanQosProfileEntry_Object = MibTableRow
msanQosProfileEntry = _MsanQosProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 7, 1)
)
msanQosProfileEntry.setIndexNames(
    (0, "ISKRATEL-MSAN-MIB", "msanQosProfileName"),
)
if mibBuilder.loadTexts:
    msanQosProfileEntry.setStatus("current")


class _MsanQosProfileName_Type(OctetString):
    """Custom type msanQosProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MsanQosProfileName_Type.__name__ = "OctetString"
_MsanQosProfileName_Object = MibTableColumn
msanQosProfileName = _MsanQosProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 7, 1, 1),
    _MsanQosProfileName_Type()
)
msanQosProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanQosProfileName.setStatus("current")


class _MsanQosProfileMatchInAny_Type(Integer32):
    """Custom type msanQosProfileMatchInAny based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanQosProfileMatchInAny_Type.__name__ = "Integer32"
_MsanQosProfileMatchInAny_Object = MibTableColumn
msanQosProfileMatchInAny = _MsanQosProfileMatchInAny_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 7, 1, 2),
    _MsanQosProfileMatchInAny_Type()
)
msanQosProfileMatchInAny.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanQosProfileMatchInAny.setStatus("current")


class _MsanQosProfileMatchInMacDestAddr_Type(MacAddress):
    """Custom type msanQosProfileMatchInMacDestAddr based on MacAddress"""
    defaultHexValue = ""


_MsanQosProfileMatchInMacDestAddr_Object = MibTableColumn
msanQosProfileMatchInMacDestAddr = _MsanQosProfileMatchInMacDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 7, 1, 3),
    _MsanQosProfileMatchInMacDestAddr_Type()
)
msanQosProfileMatchInMacDestAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanQosProfileMatchInMacDestAddr.setStatus("current")


class _MsanQosProfileMatchInMacDestMask_Type(MacAddress):
    """Custom type msanQosProfileMatchInMacDestMask based on MacAddress"""
    defaultHexValue = ""


_MsanQosProfileMatchInMacDestMask_Object = MibTableColumn
msanQosProfileMatchInMacDestMask = _MsanQosProfileMatchInMacDestMask_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 7, 1, 4),
    _MsanQosProfileMatchInMacDestMask_Type()
)
msanQosProfileMatchInMacDestMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanQosProfileMatchInMacDestMask.setStatus("current")


class _MsanQosProfileMatchInMacSrcAddr_Type(MacAddress):
    """Custom type msanQosProfileMatchInMacSrcAddr based on MacAddress"""
    defaultHexValue = ""


_MsanQosProfileMatchInMacSrcAddr_Object = MibTableColumn
msanQosProfileMatchInMacSrcAddr = _MsanQosProfileMatchInMacSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 7, 1, 5),
    _MsanQosProfileMatchInMacSrcAddr_Type()
)
msanQosProfileMatchInMacSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanQosProfileMatchInMacSrcAddr.setStatus("current")


class _MsanQosProfileMatchInMacSrcMask_Type(MacAddress):
    """Custom type msanQosProfileMatchInMacSrcMask based on MacAddress"""
    defaultHexValue = ""


_MsanQosProfileMatchInMacSrcMask_Object = MibTableColumn
msanQosProfileMatchInMacSrcMask = _MsanQosProfileMatchInMacSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 7, 1, 6),
    _MsanQosProfileMatchInMacSrcMask_Type()
)
msanQosProfileMatchInMacSrcMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanQosProfileMatchInMacSrcMask.setStatus("current")


class _MsanQosProfileMatchInCos_Type(Integer32):
    """Custom type msanQosProfileMatchInCos based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_MsanQosProfileMatchInCos_Type.__name__ = "Integer32"
_MsanQosProfileMatchInCos_Object = MibTableColumn
msanQosProfileMatchInCos = _MsanQosProfileMatchInCos_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 7, 1, 7),
    _MsanQosProfileMatchInCos_Type()
)
msanQosProfileMatchInCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanQosProfileMatchInCos.setStatus("current")


class _MsanQosProfileMatchInCos2_Type(Integer32):
    """Custom type msanQosProfileMatchInCos2 based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_MsanQosProfileMatchInCos2_Type.__name__ = "Integer32"
_MsanQosProfileMatchInCos2_Object = MibTableColumn
msanQosProfileMatchInCos2 = _MsanQosProfileMatchInCos2_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 7, 1, 8),
    _MsanQosProfileMatchInCos2_Type()
)
msanQosProfileMatchInCos2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanQosProfileMatchInCos2.setStatus("current")


class _MsanQosProfileMatchInVlanId_Type(Integer32):
    """Custom type msanQosProfileMatchInVlanId based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 4094),
    )


_MsanQosProfileMatchInVlanId_Type.__name__ = "Integer32"
_MsanQosProfileMatchInVlanId_Object = MibTableColumn
msanQosProfileMatchInVlanId = _MsanQosProfileMatchInVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 7, 1, 9),
    _MsanQosProfileMatchInVlanId_Type()
)
msanQosProfileMatchInVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanQosProfileMatchInVlanId.setStatus("current")


class _MsanQosProfileMatchInVlanId2_Type(Integer32):
    """Custom type msanQosProfileMatchInVlanId2 based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 4094),
    )


_MsanQosProfileMatchInVlanId2_Type.__name__ = "Integer32"
_MsanQosProfileMatchInVlanId2_Object = MibTableColumn
msanQosProfileMatchInVlanId2 = _MsanQosProfileMatchInVlanId2_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 7, 1, 10),
    _MsanQosProfileMatchInVlanId2_Type()
)
msanQosProfileMatchInVlanId2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanQosProfileMatchInVlanId2.setStatus("current")


class _MsanQosProfileMatchInEthertype_Type(Integer32):
    """Custom type msanQosProfileMatchInEthertype based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_MsanQosProfileMatchInEthertype_Type.__name__ = "Integer32"
_MsanQosProfileMatchInEthertype_Object = MibTableColumn
msanQosProfileMatchInEthertype = _MsanQosProfileMatchInEthertype_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 7, 1, 11),
    _MsanQosProfileMatchInEthertype_Type()
)
msanQosProfileMatchInEthertype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanQosProfileMatchInEthertype.setStatus("current")


class _MsanQosProfileMatchInIpProtocol_Type(Integer32):
    """Custom type msanQosProfileMatchInIpProtocol based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_MsanQosProfileMatchInIpProtocol_Type.__name__ = "Integer32"
_MsanQosProfileMatchInIpProtocol_Object = MibTableColumn
msanQosProfileMatchInIpProtocol = _MsanQosProfileMatchInIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 7, 1, 12),
    _MsanQosProfileMatchInIpProtocol_Type()
)
msanQosProfileMatchInIpProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanQosProfileMatchInIpProtocol.setStatus("current")


class _MsanQosProfileMatchInIpSrcAddr_Type(IpAddress):
    """Custom type msanQosProfileMatchInIpSrcAddr based on IpAddress"""
    defaultHexValue = ""


_MsanQosProfileMatchInIpSrcAddr_Object = MibTableColumn
msanQosProfileMatchInIpSrcAddr = _MsanQosProfileMatchInIpSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 7, 1, 13),
    _MsanQosProfileMatchInIpSrcAddr_Type()
)
msanQosProfileMatchInIpSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanQosProfileMatchInIpSrcAddr.setStatus("current")


class _MsanQosProfileMatchInIpSrcMask_Type(IpAddress):
    """Custom type msanQosProfileMatchInIpSrcMask based on IpAddress"""
    defaultHexValue = ""


_MsanQosProfileMatchInIpSrcMask_Object = MibTableColumn
msanQosProfileMatchInIpSrcMask = _MsanQosProfileMatchInIpSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 7, 1, 14),
    _MsanQosProfileMatchInIpSrcMask_Type()
)
msanQosProfileMatchInIpSrcMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanQosProfileMatchInIpSrcMask.setStatus("current")


class _MsanQosProfileMatchInIpDestAddr_Type(IpAddress):
    """Custom type msanQosProfileMatchInIpDestAddr based on IpAddress"""
    defaultHexValue = ""


_MsanQosProfileMatchInIpDestAddr_Object = MibTableColumn
msanQosProfileMatchInIpDestAddr = _MsanQosProfileMatchInIpDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 7, 1, 15),
    _MsanQosProfileMatchInIpDestAddr_Type()
)
msanQosProfileMatchInIpDestAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanQosProfileMatchInIpDestAddr.setStatus("current")


class _MsanQosProfileMatchInIpDestMask_Type(IpAddress):
    """Custom type msanQosProfileMatchInIpDestMask based on IpAddress"""
    defaultHexValue = ""


_MsanQosProfileMatchInIpDestMask_Object = MibTableColumn
msanQosProfileMatchInIpDestMask = _MsanQosProfileMatchInIpDestMask_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 7, 1, 16),
    _MsanQosProfileMatchInIpDestMask_Type()
)
msanQosProfileMatchInIpDestMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanQosProfileMatchInIpDestMask.setStatus("current")


class _MsanQosProfileMatchInIpDscp_Type(Integer32):
    """Custom type msanQosProfileMatchInIpDscp based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_MsanQosProfileMatchInIpDscp_Type.__name__ = "Integer32"
_MsanQosProfileMatchInIpDscp_Object = MibTableColumn
msanQosProfileMatchInIpDscp = _MsanQosProfileMatchInIpDscp_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 7, 1, 17),
    _MsanQosProfileMatchInIpDscp_Type()
)
msanQosProfileMatchInIpDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanQosProfileMatchInIpDscp.setStatus("current")


class _MsanQosProfileMatchInIpPrecedence_Type(Integer32):
    """Custom type msanQosProfileMatchInIpPrecedence based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_MsanQosProfileMatchInIpPrecedence_Type.__name__ = "Integer32"
_MsanQosProfileMatchInIpPrecedence_Object = MibTableColumn
msanQosProfileMatchInIpPrecedence = _MsanQosProfileMatchInIpPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 7, 1, 18),
    _MsanQosProfileMatchInIpPrecedence_Type()
)
msanQosProfileMatchInIpPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanQosProfileMatchInIpPrecedence.setStatus("current")


class _MsanQosProfileMatchInIpTosBits_Type(OctetString):
    """Custom type msanQosProfileMatchInIpTosBits based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_MsanQosProfileMatchInIpTosBits_Type.__name__ = "OctetString"
_MsanQosProfileMatchInIpTosBits_Object = MibTableColumn
msanQosProfileMatchInIpTosBits = _MsanQosProfileMatchInIpTosBits_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 7, 1, 19),
    _MsanQosProfileMatchInIpTosBits_Type()
)
msanQosProfileMatchInIpTosBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanQosProfileMatchInIpTosBits.setStatus("current")


class _MsanQosProfileMatchInIpTosMask_Type(OctetString):
    """Custom type msanQosProfileMatchInIpTosMask based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_MsanQosProfileMatchInIpTosMask_Type.__name__ = "OctetString"
_MsanQosProfileMatchInIpTosMask_Object = MibTableColumn
msanQosProfileMatchInIpTosMask = _MsanQosProfileMatchInIpTosMask_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 7, 1, 20),
    _MsanQosProfileMatchInIpTosMask_Type()
)
msanQosProfileMatchInIpTosMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanQosProfileMatchInIpTosMask.setStatus("current")


class _MsanQosProfileMatchInL4SrcPort_Type(Integer32):
    """Custom type msanQosProfileMatchInL4SrcPort based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_MsanQosProfileMatchInL4SrcPort_Type.__name__ = "Integer32"
_MsanQosProfileMatchInL4SrcPort_Object = MibTableColumn
msanQosProfileMatchInL4SrcPort = _MsanQosProfileMatchInL4SrcPort_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 7, 1, 21),
    _MsanQosProfileMatchInL4SrcPort_Type()
)
msanQosProfileMatchInL4SrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanQosProfileMatchInL4SrcPort.setStatus("current")


class _MsanQosProfileMatchInL4DestPort_Type(Integer32):
    """Custom type msanQosProfileMatchInL4DestPort based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_MsanQosProfileMatchInL4DestPort_Type.__name__ = "Integer32"
_MsanQosProfileMatchInL4DestPort_Object = MibTableColumn
msanQosProfileMatchInL4DestPort = _MsanQosProfileMatchInL4DestPort_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 7, 1, 22),
    _MsanQosProfileMatchInL4DestPort_Type()
)
msanQosProfileMatchInL4DestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanQosProfileMatchInL4DestPort.setStatus("current")


class _MsanQosProfileMatchOutAny_Type(Integer32):
    """Custom type msanQosProfileMatchOutAny based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanQosProfileMatchOutAny_Type.__name__ = "Integer32"
_MsanQosProfileMatchOutAny_Object = MibTableColumn
msanQosProfileMatchOutAny = _MsanQosProfileMatchOutAny_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 7, 1, 23),
    _MsanQosProfileMatchOutAny_Type()
)
msanQosProfileMatchOutAny.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanQosProfileMatchOutAny.setStatus("current")


class _MsanQosProfileMatchOutMacDestAddr_Type(MacAddress):
    """Custom type msanQosProfileMatchOutMacDestAddr based on MacAddress"""
    defaultHexValue = ""


_MsanQosProfileMatchOutMacDestAddr_Object = MibTableColumn
msanQosProfileMatchOutMacDestAddr = _MsanQosProfileMatchOutMacDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 7, 1, 24),
    _MsanQosProfileMatchOutMacDestAddr_Type()
)
msanQosProfileMatchOutMacDestAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanQosProfileMatchOutMacDestAddr.setStatus("current")


class _MsanQosProfileMatchOutMacDestMask_Type(MacAddress):
    """Custom type msanQosProfileMatchOutMacDestMask based on MacAddress"""
    defaultHexValue = ""


_MsanQosProfileMatchOutMacDestMask_Object = MibTableColumn
msanQosProfileMatchOutMacDestMask = _MsanQosProfileMatchOutMacDestMask_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 7, 1, 25),
    _MsanQosProfileMatchOutMacDestMask_Type()
)
msanQosProfileMatchOutMacDestMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanQosProfileMatchOutMacDestMask.setStatus("current")


class _MsanQosProfileMatchOutMacSrcAddr_Type(MacAddress):
    """Custom type msanQosProfileMatchOutMacSrcAddr based on MacAddress"""
    defaultHexValue = ""


_MsanQosProfileMatchOutMacSrcAddr_Object = MibTableColumn
msanQosProfileMatchOutMacSrcAddr = _MsanQosProfileMatchOutMacSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 7, 1, 26),
    _MsanQosProfileMatchOutMacSrcAddr_Type()
)
msanQosProfileMatchOutMacSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanQosProfileMatchOutMacSrcAddr.setStatus("current")


class _MsanQosProfileMatchOutMacSrcMask_Type(MacAddress):
    """Custom type msanQosProfileMatchOutMacSrcMask based on MacAddress"""
    defaultHexValue = ""


_MsanQosProfileMatchOutMacSrcMask_Object = MibTableColumn
msanQosProfileMatchOutMacSrcMask = _MsanQosProfileMatchOutMacSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 7, 1, 27),
    _MsanQosProfileMatchOutMacSrcMask_Type()
)
msanQosProfileMatchOutMacSrcMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanQosProfileMatchOutMacSrcMask.setStatus("current")


class _MsanQosProfileMatchOutCos_Type(Integer32):
    """Custom type msanQosProfileMatchOutCos based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_MsanQosProfileMatchOutCos_Type.__name__ = "Integer32"
_MsanQosProfileMatchOutCos_Object = MibTableColumn
msanQosProfileMatchOutCos = _MsanQosProfileMatchOutCos_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 7, 1, 28),
    _MsanQosProfileMatchOutCos_Type()
)
msanQosProfileMatchOutCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanQosProfileMatchOutCos.setStatus("current")


class _MsanQosProfileMatchOutCos2_Type(Integer32):
    """Custom type msanQosProfileMatchOutCos2 based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_MsanQosProfileMatchOutCos2_Type.__name__ = "Integer32"
_MsanQosProfileMatchOutCos2_Object = MibTableColumn
msanQosProfileMatchOutCos2 = _MsanQosProfileMatchOutCos2_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 7, 1, 29),
    _MsanQosProfileMatchOutCos2_Type()
)
msanQosProfileMatchOutCos2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanQosProfileMatchOutCos2.setStatus("current")


class _MsanQosProfileMatchOutVlanId_Type(Integer32):
    """Custom type msanQosProfileMatchOutVlanId based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 4094),
    )


_MsanQosProfileMatchOutVlanId_Type.__name__ = "Integer32"
_MsanQosProfileMatchOutVlanId_Object = MibTableColumn
msanQosProfileMatchOutVlanId = _MsanQosProfileMatchOutVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 7, 1, 30),
    _MsanQosProfileMatchOutVlanId_Type()
)
msanQosProfileMatchOutVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanQosProfileMatchOutVlanId.setStatus("current")


class _MsanQosProfileMatchOutVlanId2_Type(Integer32):
    """Custom type msanQosProfileMatchOutVlanId2 based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 4094),
    )


_MsanQosProfileMatchOutVlanId2_Type.__name__ = "Integer32"
_MsanQosProfileMatchOutVlanId2_Object = MibTableColumn
msanQosProfileMatchOutVlanId2 = _MsanQosProfileMatchOutVlanId2_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 7, 1, 31),
    _MsanQosProfileMatchOutVlanId2_Type()
)
msanQosProfileMatchOutVlanId2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanQosProfileMatchOutVlanId2.setStatus("current")


class _MsanQosProfileMatchOutEthertype_Type(Integer32):
    """Custom type msanQosProfileMatchOutEthertype based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_MsanQosProfileMatchOutEthertype_Type.__name__ = "Integer32"
_MsanQosProfileMatchOutEthertype_Object = MibTableColumn
msanQosProfileMatchOutEthertype = _MsanQosProfileMatchOutEthertype_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 7, 1, 32),
    _MsanQosProfileMatchOutEthertype_Type()
)
msanQosProfileMatchOutEthertype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanQosProfileMatchOutEthertype.setStatus("current")


class _MsanQosProfileMatchOutIpProtocol_Type(Integer32):
    """Custom type msanQosProfileMatchOutIpProtocol based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_MsanQosProfileMatchOutIpProtocol_Type.__name__ = "Integer32"
_MsanQosProfileMatchOutIpProtocol_Object = MibTableColumn
msanQosProfileMatchOutIpProtocol = _MsanQosProfileMatchOutIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 7, 1, 33),
    _MsanQosProfileMatchOutIpProtocol_Type()
)
msanQosProfileMatchOutIpProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanQosProfileMatchOutIpProtocol.setStatus("current")


class _MsanQosProfileMatchOutIpSrcAddr_Type(IpAddress):
    """Custom type msanQosProfileMatchOutIpSrcAddr based on IpAddress"""
    defaultHexValue = ""


_MsanQosProfileMatchOutIpSrcAddr_Object = MibTableColumn
msanQosProfileMatchOutIpSrcAddr = _MsanQosProfileMatchOutIpSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 7, 1, 34),
    _MsanQosProfileMatchOutIpSrcAddr_Type()
)
msanQosProfileMatchOutIpSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanQosProfileMatchOutIpSrcAddr.setStatus("current")


class _MsanQosProfileMatchOutIpSrcMask_Type(IpAddress):
    """Custom type msanQosProfileMatchOutIpSrcMask based on IpAddress"""
    defaultHexValue = ""


_MsanQosProfileMatchOutIpSrcMask_Object = MibTableColumn
msanQosProfileMatchOutIpSrcMask = _MsanQosProfileMatchOutIpSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 7, 1, 35),
    _MsanQosProfileMatchOutIpSrcMask_Type()
)
msanQosProfileMatchOutIpSrcMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanQosProfileMatchOutIpSrcMask.setStatus("current")


class _MsanQosProfileMatchOutIpDestAddr_Type(IpAddress):
    """Custom type msanQosProfileMatchOutIpDestAddr based on IpAddress"""
    defaultHexValue = ""


_MsanQosProfileMatchOutIpDestAddr_Object = MibTableColumn
msanQosProfileMatchOutIpDestAddr = _MsanQosProfileMatchOutIpDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 7, 1, 36),
    _MsanQosProfileMatchOutIpDestAddr_Type()
)
msanQosProfileMatchOutIpDestAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanQosProfileMatchOutIpDestAddr.setStatus("current")


class _MsanQosProfileMatchOutIpDestMask_Type(IpAddress):
    """Custom type msanQosProfileMatchOutIpDestMask based on IpAddress"""
    defaultHexValue = ""


_MsanQosProfileMatchOutIpDestMask_Object = MibTableColumn
msanQosProfileMatchOutIpDestMask = _MsanQosProfileMatchOutIpDestMask_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 7, 1, 37),
    _MsanQosProfileMatchOutIpDestMask_Type()
)
msanQosProfileMatchOutIpDestMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanQosProfileMatchOutIpDestMask.setStatus("current")


class _MsanQosProfileMatchOutIpDscp_Type(Integer32):
    """Custom type msanQosProfileMatchOutIpDscp based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_MsanQosProfileMatchOutIpDscp_Type.__name__ = "Integer32"
_MsanQosProfileMatchOutIpDscp_Object = MibTableColumn
msanQosProfileMatchOutIpDscp = _MsanQosProfileMatchOutIpDscp_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 7, 1, 38),
    _MsanQosProfileMatchOutIpDscp_Type()
)
msanQosProfileMatchOutIpDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanQosProfileMatchOutIpDscp.setStatus("current")


class _MsanQosProfileMatchOutIpPrecedence_Type(Integer32):
    """Custom type msanQosProfileMatchOutIpPrecedence based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_MsanQosProfileMatchOutIpPrecedence_Type.__name__ = "Integer32"
_MsanQosProfileMatchOutIpPrecedence_Object = MibTableColumn
msanQosProfileMatchOutIpPrecedence = _MsanQosProfileMatchOutIpPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 7, 1, 39),
    _MsanQosProfileMatchOutIpPrecedence_Type()
)
msanQosProfileMatchOutIpPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanQosProfileMatchOutIpPrecedence.setStatus("current")


class _MsanQosProfileMatchOutIpTosBits_Type(OctetString):
    """Custom type msanQosProfileMatchOutIpTosBits based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_MsanQosProfileMatchOutIpTosBits_Type.__name__ = "OctetString"
_MsanQosProfileMatchOutIpTosBits_Object = MibTableColumn
msanQosProfileMatchOutIpTosBits = _MsanQosProfileMatchOutIpTosBits_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 7, 1, 40),
    _MsanQosProfileMatchOutIpTosBits_Type()
)
msanQosProfileMatchOutIpTosBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanQosProfileMatchOutIpTosBits.setStatus("current")


class _MsanQosProfileMatchOutIpTosMask_Type(OctetString):
    """Custom type msanQosProfileMatchOutIpTosMask based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_MsanQosProfileMatchOutIpTosMask_Type.__name__ = "OctetString"
_MsanQosProfileMatchOutIpTosMask_Object = MibTableColumn
msanQosProfileMatchOutIpTosMask = _MsanQosProfileMatchOutIpTosMask_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 7, 1, 41),
    _MsanQosProfileMatchOutIpTosMask_Type()
)
msanQosProfileMatchOutIpTosMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanQosProfileMatchOutIpTosMask.setStatus("current")


class _MsanQosProfileMatchOutL4SrcPort_Type(Integer32):
    """Custom type msanQosProfileMatchOutL4SrcPort based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_MsanQosProfileMatchOutL4SrcPort_Type.__name__ = "Integer32"
_MsanQosProfileMatchOutL4SrcPort_Object = MibTableColumn
msanQosProfileMatchOutL4SrcPort = _MsanQosProfileMatchOutL4SrcPort_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 7, 1, 42),
    _MsanQosProfileMatchOutL4SrcPort_Type()
)
msanQosProfileMatchOutL4SrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanQosProfileMatchOutL4SrcPort.setStatus("current")


class _MsanQosProfileMatchOutL4DestPort_Type(Integer32):
    """Custom type msanQosProfileMatchOutL4DestPort based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_MsanQosProfileMatchOutL4DestPort_Type.__name__ = "Integer32"
_MsanQosProfileMatchOutL4DestPort_Object = MibTableColumn
msanQosProfileMatchOutL4DestPort = _MsanQosProfileMatchOutL4DestPort_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 7, 1, 43),
    _MsanQosProfileMatchOutL4DestPort_Type()
)
msanQosProfileMatchOutL4DestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanQosProfileMatchOutL4DestPort.setStatus("current")


class _MsanQosProfileInCdr_Type(Integer32):
    """Custom type msanQosProfileInCdr based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1000000),
    )


_MsanQosProfileInCdr_Type.__name__ = "Integer32"
_MsanQosProfileInCdr_Object = MibTableColumn
msanQosProfileInCdr = _MsanQosProfileInCdr_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 7, 1, 44),
    _MsanQosProfileInCdr_Type()
)
msanQosProfileInCdr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanQosProfileInCdr.setStatus("current")
if mibBuilder.loadTexts:
    msanQosProfileInCdr.setUnits("kbps")


class _MsanQosProfileInPdr_Type(Integer32):
    """Custom type msanQosProfileInPdr based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1000000),
    )


_MsanQosProfileInPdr_Type.__name__ = "Integer32"
_MsanQosProfileInPdr_Object = MibTableColumn
msanQosProfileInPdr = _MsanQosProfileInPdr_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 7, 1, 45),
    _MsanQosProfileInPdr_Type()
)
msanQosProfileInPdr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanQosProfileInPdr.setStatus("current")
if mibBuilder.loadTexts:
    msanQosProfileInPdr.setUnits("kbps")


class _MsanQosProfileOutCdr_Type(Integer32):
    """Custom type msanQosProfileOutCdr based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1000000),
    )


_MsanQosProfileOutCdr_Type.__name__ = "Integer32"
_MsanQosProfileOutCdr_Object = MibTableColumn
msanQosProfileOutCdr = _MsanQosProfileOutCdr_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 7, 1, 46),
    _MsanQosProfileOutCdr_Type()
)
msanQosProfileOutCdr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanQosProfileOutCdr.setStatus("current")
if mibBuilder.loadTexts:
    msanQosProfileOutCdr.setUnits("kbps")


class _MsanQosProfileOutPdr_Type(Integer32):
    """Custom type msanQosProfileOutPdr based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1000000),
    )


_MsanQosProfileOutPdr_Type.__name__ = "Integer32"
_MsanQosProfileOutPdr_Object = MibTableColumn
msanQosProfileOutPdr = _MsanQosProfileOutPdr_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 7, 1, 47),
    _MsanQosProfileOutPdr_Type()
)
msanQosProfileOutPdr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanQosProfileOutPdr.setStatus("current")
if mibBuilder.loadTexts:
    msanQosProfileOutPdr.setUnits("kbps")


class _MsanQosProfileInTrustMode_Type(Integer32):
    """Custom type msanQosProfileInTrustMode based on Integer32"""
    defaultValue = 1

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
        *(("trustCos", 2),
          ("trustDscp", 3),
          ("untrustMarkCos", 4),
          ("untrustMarkDscp", 5),
          ("untrusted", 1))
    )


_MsanQosProfileInTrustMode_Type.__name__ = "Integer32"
_MsanQosProfileInTrustMode_Object = MibTableColumn
msanQosProfileInTrustMode = _MsanQosProfileInTrustMode_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 7, 1, 48),
    _MsanQosProfileInTrustMode_Type()
)
msanQosProfileInTrustMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanQosProfileInTrustMode.setStatus("current")


class _MsanQosProfileInMarkCos_Type(Integer32):
    """Custom type msanQosProfileInMarkCos based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_MsanQosProfileInMarkCos_Type.__name__ = "Integer32"
_MsanQosProfileInMarkCos_Object = MibTableColumn
msanQosProfileInMarkCos = _MsanQosProfileInMarkCos_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 7, 1, 49),
    _MsanQosProfileInMarkCos_Type()
)
msanQosProfileInMarkCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanQosProfileInMarkCos.setStatus("current")


class _MsanQosProfileInMarkDscp_Type(Integer32):
    """Custom type msanQosProfileInMarkDscp based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_MsanQosProfileInMarkDscp_Type.__name__ = "Integer32"
_MsanQosProfileInMarkDscp_Object = MibTableColumn
msanQosProfileInMarkDscp = _MsanQosProfileInMarkDscp_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 7, 1, 50),
    _MsanQosProfileInMarkDscp_Type()
)
msanQosProfileInMarkDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanQosProfileInMarkDscp.setStatus("current")
_MsanQosProfileRowStatus_Type = RowStatus
_MsanQosProfileRowStatus_Object = MibTableColumn
msanQosProfileRowStatus = _MsanQosProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 7, 1, 51),
    _MsanQosProfileRowStatus_Type()
)
msanQosProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanQosProfileRowStatus.setStatus("current")


class _MsanQosProfilePriority_Type(Integer32):
    """Custom type msanQosProfilePriority based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("normal", 1))
    )


_MsanQosProfilePriority_Type.__name__ = "Integer32"
_MsanQosProfilePriority_Object = MibTableColumn
msanQosProfilePriority = _MsanQosProfilePriority_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 7, 1, 52),
    _MsanQosProfilePriority_Type()
)
msanQosProfilePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanQosProfilePriority.setStatus("current")
_MsanQosProfileInCdrBurstSize_Type = Integer32
_MsanQosProfileInCdrBurstSize_Object = MibTableColumn
msanQosProfileInCdrBurstSize = _MsanQosProfileInCdrBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 7, 1, 53),
    _MsanQosProfileInCdrBurstSize_Type()
)
msanQosProfileInCdrBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanQosProfileInCdrBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    msanQosProfileInCdrBurstSize.setUnits("kB")
_MsanQosProfileInPdrBurstSize_Type = Integer32
_MsanQosProfileInPdrBurstSize_Object = MibTableColumn
msanQosProfileInPdrBurstSize = _MsanQosProfileInPdrBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 7, 1, 54),
    _MsanQosProfileInPdrBurstSize_Type()
)
msanQosProfileInPdrBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanQosProfileInPdrBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    msanQosProfileInPdrBurstSize.setUnits("kB")
_MsanQosProfileOutCdrBurstSize_Type = Integer32
_MsanQosProfileOutCdrBurstSize_Object = MibTableColumn
msanQosProfileOutCdrBurstSize = _MsanQosProfileOutCdrBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 7, 1, 55),
    _MsanQosProfileOutCdrBurstSize_Type()
)
msanQosProfileOutCdrBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanQosProfileOutCdrBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    msanQosProfileOutCdrBurstSize.setUnits("kB")


class _MsanQosProfileOutPdrBurstSize_Type(Integer32):
    """Custom type msanQosProfileOutPdrBurstSize based on Integer32"""
    defaultValue = 64


_MsanQosProfileOutPdrBurstSize_Object = MibTableColumn
msanQosProfileOutPdrBurstSize = _MsanQosProfileOutPdrBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 7, 1, 56),
    _MsanQosProfileOutPdrBurstSize_Type()
)
msanQosProfileOutPdrBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanQosProfileOutPdrBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    msanQosProfileOutPdrBurstSize.setUnits("kB")
_MsanQosProfileMatchInSrcIpv6Address_Type = InetAddressIPv6
_MsanQosProfileMatchInSrcIpv6Address_Object = MibTableColumn
msanQosProfileMatchInSrcIpv6Address = _MsanQosProfileMatchInSrcIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 7, 1, 58),
    _MsanQosProfileMatchInSrcIpv6Address_Type()
)
msanQosProfileMatchInSrcIpv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanQosProfileMatchInSrcIpv6Address.setStatus("current")


class _MsanQosProfileMatchInSrcIpv6AddressMaskLen_Type(Integer32):
    """Custom type msanQosProfileMatchInSrcIpv6AddressMaskLen based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_MsanQosProfileMatchInSrcIpv6AddressMaskLen_Type.__name__ = "Integer32"
_MsanQosProfileMatchInSrcIpv6AddressMaskLen_Object = MibTableColumn
msanQosProfileMatchInSrcIpv6AddressMaskLen = _MsanQosProfileMatchInSrcIpv6AddressMaskLen_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 7, 1, 59),
    _MsanQosProfileMatchInSrcIpv6AddressMaskLen_Type()
)
msanQosProfileMatchInSrcIpv6AddressMaskLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanQosProfileMatchInSrcIpv6AddressMaskLen.setStatus("current")
_MsanQosProfileMatchInDestIpv6Address_Type = InetAddressIPv6
_MsanQosProfileMatchInDestIpv6Address_Object = MibTableColumn
msanQosProfileMatchInDestIpv6Address = _MsanQosProfileMatchInDestIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 7, 1, 60),
    _MsanQosProfileMatchInDestIpv6Address_Type()
)
msanQosProfileMatchInDestIpv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanQosProfileMatchInDestIpv6Address.setStatus("current")


class _MsanQosProfileMatchInDestIpv6AddressMaskLen_Type(Integer32):
    """Custom type msanQosProfileMatchInDestIpv6AddressMaskLen based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_MsanQosProfileMatchInDestIpv6AddressMaskLen_Type.__name__ = "Integer32"
_MsanQosProfileMatchInDestIpv6AddressMaskLen_Object = MibTableColumn
msanQosProfileMatchInDestIpv6AddressMaskLen = _MsanQosProfileMatchInDestIpv6AddressMaskLen_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 7, 1, 61),
    _MsanQosProfileMatchInDestIpv6AddressMaskLen_Type()
)
msanQosProfileMatchInDestIpv6AddressMaskLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanQosProfileMatchInDestIpv6AddressMaskLen.setStatus("current")
_MsanQosProfileMatchOutSrcIpv6Address_Type = InetAddressIPv6
_MsanQosProfileMatchOutSrcIpv6Address_Object = MibTableColumn
msanQosProfileMatchOutSrcIpv6Address = _MsanQosProfileMatchOutSrcIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 7, 1, 63),
    _MsanQosProfileMatchOutSrcIpv6Address_Type()
)
msanQosProfileMatchOutSrcIpv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanQosProfileMatchOutSrcIpv6Address.setStatus("current")


class _MsanQosProfileMatchOutSrcIpv6AddressMaskLen_Type(Integer32):
    """Custom type msanQosProfileMatchOutSrcIpv6AddressMaskLen based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_MsanQosProfileMatchOutSrcIpv6AddressMaskLen_Type.__name__ = "Integer32"
_MsanQosProfileMatchOutSrcIpv6AddressMaskLen_Object = MibTableColumn
msanQosProfileMatchOutSrcIpv6AddressMaskLen = _MsanQosProfileMatchOutSrcIpv6AddressMaskLen_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 7, 1, 64),
    _MsanQosProfileMatchOutSrcIpv6AddressMaskLen_Type()
)
msanQosProfileMatchOutSrcIpv6AddressMaskLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanQosProfileMatchOutSrcIpv6AddressMaskLen.setStatus("current")
_MsanQosProfileMatchOutDestIpv6Address_Type = InetAddressIPv6
_MsanQosProfileMatchOutDestIpv6Address_Object = MibTableColumn
msanQosProfileMatchOutDestIpv6Address = _MsanQosProfileMatchOutDestIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 7, 1, 65),
    _MsanQosProfileMatchOutDestIpv6Address_Type()
)
msanQosProfileMatchOutDestIpv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanQosProfileMatchOutDestIpv6Address.setStatus("current")


class _MsanQosProfileMatchOutDestIpv6AddressMaskLen_Type(Integer32):
    """Custom type msanQosProfileMatchOutDestIpv6AddressMaskLen based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_MsanQosProfileMatchOutDestIpv6AddressMaskLen_Type.__name__ = "Integer32"
_MsanQosProfileMatchOutDestIpv6AddressMaskLen_Object = MibTableColumn
msanQosProfileMatchOutDestIpv6AddressMaskLen = _MsanQosProfileMatchOutDestIpv6AddressMaskLen_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 7, 1, 66),
    _MsanQosProfileMatchOutDestIpv6AddressMaskLen_Type()
)
msanQosProfileMatchOutDestIpv6AddressMaskLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanQosProfileMatchOutDestIpv6AddressMaskLen.setStatus("current")
_MsanQosIntfProfileTable_Object = MibTable
msanQosIntfProfileTable = _MsanQosIntfProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 8)
)
if mibBuilder.loadTexts:
    msanQosIntfProfileTable.setStatus("current")
_MsanQosIntfProfileEntry_Object = MibTableRow
msanQosIntfProfileEntry = _MsanQosIntfProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 8, 1)
)
msanQosIntfProfileEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ISKRATEL-MSAN-MIB", "msanQosProfileName"),
)
if mibBuilder.loadTexts:
    msanQosIntfProfileEntry.setStatus("current")


class _MsanQosIntfProfileAtmVpi_Type(Integer32):
    """Custom type msanQosIntfProfileAtmVpi based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_MsanQosIntfProfileAtmVpi_Type.__name__ = "Integer32"
_MsanQosIntfProfileAtmVpi_Object = MibTableColumn
msanQosIntfProfileAtmVpi = _MsanQosIntfProfileAtmVpi_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 8, 1, 1),
    _MsanQosIntfProfileAtmVpi_Type()
)
msanQosIntfProfileAtmVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanQosIntfProfileAtmVpi.setStatus("current")


class _MsanQosIntfProfileAtmVci_Type(Integer32):
    """Custom type msanQosIntfProfileAtmVci based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_MsanQosIntfProfileAtmVci_Type.__name__ = "Integer32"
_MsanQosIntfProfileAtmVci_Object = MibTableColumn
msanQosIntfProfileAtmVci = _MsanQosIntfProfileAtmVci_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 8, 1, 2),
    _MsanQosIntfProfileAtmVci_Type()
)
msanQosIntfProfileAtmVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanQosIntfProfileAtmVci.setStatus("current")
_MsanQosIntfProfileRowStatus_Type = RowStatus
_MsanQosIntfProfileRowStatus_Object = MibTableColumn
msanQosIntfProfileRowStatus = _MsanQosIntfProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 8, 1, 3),
    _MsanQosIntfProfileRowStatus_Type()
)
msanQosIntfProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanQosIntfProfileRowStatus.setStatus("current")
_MsanQosStatistics_ObjectIdentity = ObjectIdentity
msanQosStatistics = _MsanQosStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 9)
)
_MsanQosPortStatTable_Object = MibTable
msanQosPortStatTable = _MsanQosPortStatTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 9, 1)
)
if mibBuilder.loadTexts:
    msanQosPortStatTable.setStatus("current")
_MsanQosPortStatEntry_Object = MibTableRow
msanQosPortStatEntry = _MsanQosPortStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 9, 1, 1)
)
msanQosPortStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    msanQosPortStatEntry.setStatus("current")
_MsanQosPortStatInDroppedFrames_Type = Counter32
_MsanQosPortStatInDroppedFrames_Object = MibTableColumn
msanQosPortStatInDroppedFrames = _MsanQosPortStatInDroppedFrames_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 9, 1, 1, 1),
    _MsanQosPortStatInDroppedFrames_Type()
)
msanQosPortStatInDroppedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanQosPortStatInDroppedFrames.setStatus("current")
_MsanQosPortStatOutDroppedFrames_Type = Counter32
_MsanQosPortStatOutDroppedFrames_Object = MibTableColumn
msanQosPortStatOutDroppedFrames = _MsanQosPortStatOutDroppedFrames_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 9, 1, 1, 2),
    _MsanQosPortStatOutDroppedFrames_Type()
)
msanQosPortStatOutDroppedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanQosPortStatOutDroppedFrames.setStatus("current")
_MsanQosPortProfileStatTable_Object = MibTable
msanQosPortProfileStatTable = _MsanQosPortProfileStatTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 9, 2)
)
if mibBuilder.loadTexts:
    msanQosPortProfileStatTable.setStatus("current")
_MsanQosPortProfileStatEntry_Object = MibTableRow
msanQosPortProfileStatEntry = _MsanQosPortProfileStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 9, 2, 1)
)
msanQosPortProfileStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ISKRATEL-MSAN-MIB", "msanQosProfileName"),
)
if mibBuilder.loadTexts:
    msanQosPortProfileStatEntry.setStatus("current")
_MsanQosPortProfileStatQueueCurrent_Type = Integer32
_MsanQosPortProfileStatQueueCurrent_Object = MibTableColumn
msanQosPortProfileStatQueueCurrent = _MsanQosPortProfileStatQueueCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 9, 2, 1, 1),
    _MsanQosPortProfileStatQueueCurrent_Type()
)
msanQosPortProfileStatQueueCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanQosPortProfileStatQueueCurrent.setStatus("current")
_MsanQosPortProfileStatQueueAverage_Type = Integer32
_MsanQosPortProfileStatQueueAverage_Object = MibTableColumn
msanQosPortProfileStatQueueAverage = _MsanQosPortProfileStatQueueAverage_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 9, 2, 1, 2),
    _MsanQosPortProfileStatQueueAverage_Type()
)
msanQosPortProfileStatQueueAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanQosPortProfileStatQueueAverage.setStatus("current")
_MsanQosPortProfileStatQueueMax_Type = Integer32
_MsanQosPortProfileStatQueueMax_Object = MibTableColumn
msanQosPortProfileStatQueueMax = _MsanQosPortProfileStatQueueMax_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 9, 2, 1, 3),
    _MsanQosPortProfileStatQueueMax_Type()
)
msanQosPortProfileStatQueueMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanQosPortProfileStatQueueMax.setStatus("current")
_MsanIpAclTable_Object = MibTable
msanIpAclTable = _MsanIpAclTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 10)
)
if mibBuilder.loadTexts:
    msanIpAclTable.setStatus("current")
_MsanIpAclEntry_Object = MibTableRow
msanIpAclEntry = _MsanIpAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 10, 1)
)
msanIpAclEntry.setIndexNames(
    (0, "ISKRATEL-MSAN-MIB", "msanIpAclId"),
)
if mibBuilder.loadTexts:
    msanIpAclEntry.setStatus("current")


class _MsanIpAclId_Type(Integer32):
    """Custom type msanIpAclId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 199),
    )


_MsanIpAclId_Type.__name__ = "Integer32"
_MsanIpAclId_Object = MibTableColumn
msanIpAclId = _MsanIpAclId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 10, 1, 1),
    _MsanIpAclId_Type()
)
msanIpAclId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanIpAclId.setStatus("current")


class _MsanIpAclProtection_Type(Integer32):
    """Custom type msanIpAclProtection based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("protected", 1),
          ("unprotected", 0))
    )


_MsanIpAclProtection_Type.__name__ = "Integer32"
_MsanIpAclProtection_Object = MibTableColumn
msanIpAclProtection = _MsanIpAclProtection_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 10, 1, 2),
    _MsanIpAclProtection_Type()
)
msanIpAclProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIpAclProtection.setStatus("current")


class _MsanIpAclStatus_Type(Integer32):
    """Custom type msanIpAclStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_MsanIpAclStatus_Type.__name__ = "Integer32"
_MsanIpAclStatus_Object = MibTableColumn
msanIpAclStatus = _MsanIpAclStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 10, 1, 4),
    _MsanIpAclStatus_Type()
)
msanIpAclStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanIpAclStatus.setStatus("current")
_MsanMacAclTable_Object = MibTable
msanMacAclTable = _MsanMacAclTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 11)
)
if mibBuilder.loadTexts:
    msanMacAclTable.setStatus("current")
_MsanMacAclEntry_Object = MibTableRow
msanMacAclEntry = _MsanMacAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 11, 1)
)
msanMacAclEntry.setIndexNames(
    (0, "ISKRATEL-MSAN-MIB", "msanMacAclId"),
)
if mibBuilder.loadTexts:
    msanMacAclEntry.setStatus("current")


class _MsanMacAclId_Type(Integer32):
    """Custom type msanMacAclId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 199),
    )


_MsanMacAclId_Type.__name__ = "Integer32"
_MsanMacAclId_Object = MibTableColumn
msanMacAclId = _MsanMacAclId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 11, 1, 1),
    _MsanMacAclId_Type()
)
msanMacAclId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanMacAclId.setStatus("current")


class _MsanMacAclProtection_Type(Integer32):
    """Custom type msanMacAclProtection based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("protected", 1),
          ("unprotected", 0))
    )


_MsanMacAclProtection_Type.__name__ = "Integer32"
_MsanMacAclProtection_Object = MibTableColumn
msanMacAclProtection = _MsanMacAclProtection_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 11, 1, 3),
    _MsanMacAclProtection_Type()
)
msanMacAclProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanMacAclProtection.setStatus("current")


class _MsanMacAclStatus_Type(Integer32):
    """Custom type msanMacAclStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_MsanMacAclStatus_Type.__name__ = "Integer32"
_MsanMacAclStatus_Object = MibTableColumn
msanMacAclStatus = _MsanMacAclStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 12, 11, 1, 4),
    _MsanMacAclStatus_Type()
)
msanMacAclStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanMacAclStatus.setStatus("current")
_MsanForwardingDb_ObjectIdentity = ObjectIdentity
msanForwardingDb = _MsanForwardingDb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 13)
)
_MsanForwardingDbGlobal_ObjectIdentity = ObjectIdentity
msanForwardingDbGlobal = _MsanForwardingDbGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 13, 3)
)


class _MsanAddressLearningMode_Type(Integer32):
    """Custom type msanAddressLearningMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("macOnly", 1),
          ("noMacOnly", 2))
    )


_MsanAddressLearningMode_Type.__name__ = "Integer32"
_MsanAddressLearningMode_Object = MibScalar
msanAddressLearningMode = _MsanAddressLearningMode_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 13, 3, 1),
    _MsanAddressLearningMode_Type()
)
msanAddressLearningMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanAddressLearningMode.setStatus("deprecated")


class _MsanAddressLearningVlanId_Type(Integer32):
    """Custom type msanAddressLearningVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_MsanAddressLearningVlanId_Type.__name__ = "Integer32"
_MsanAddressLearningVlanId_Object = MibScalar
msanAddressLearningVlanId = _MsanAddressLearningVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 13, 3, 2),
    _MsanAddressLearningVlanId_Type()
)
msanAddressLearningVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanAddressLearningVlanId.setStatus("deprecated")


class _MsanSwitchAddressAgingTimeout_Type(Integer32):
    """Custom type msanSwitchAddressAgingTimeout based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_MsanSwitchAddressAgingTimeout_Type.__name__ = "Integer32"
_MsanSwitchAddressAgingTimeout_Object = MibScalar
msanSwitchAddressAgingTimeout = _MsanSwitchAddressAgingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 13, 3, 3),
    _MsanSwitchAddressAgingTimeout_Type()
)
msanSwitchAddressAgingTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanSwitchAddressAgingTimeout.setStatus("current")
_MsanDiagnostics_ObjectIdentity = ObjectIdentity
msanDiagnostics = _MsanDiagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 14)
)
_MsanDiagnosticsGlobal_ObjectIdentity = ObjectIdentity
msanDiagnosticsGlobal = _MsanDiagnosticsGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 14, 1)
)
_MsanDiagnosticsFanSpeedLevel_Type = Integer32
_MsanDiagnosticsFanSpeedLevel_Object = MibScalar
msanDiagnosticsFanSpeedLevel = _MsanDiagnosticsFanSpeedLevel_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 14, 1, 1),
    _MsanDiagnosticsFanSpeedLevel_Type()
)
msanDiagnosticsFanSpeedLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDiagnosticsFanSpeedLevel.setStatus("current")
_MsanDiagnosticsMaxFanSpeedLevel_Type = Integer32
_MsanDiagnosticsMaxFanSpeedLevel_Object = MibScalar
msanDiagnosticsMaxFanSpeedLevel = _MsanDiagnosticsMaxFanSpeedLevel_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 14, 1, 2),
    _MsanDiagnosticsMaxFanSpeedLevel_Type()
)
msanDiagnosticsMaxFanSpeedLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDiagnosticsMaxFanSpeedLevel.setStatus("current")
_MsanDiagnosticsTestTable_Object = MibTable
msanDiagnosticsTestTable = _MsanDiagnosticsTestTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 14, 2)
)
if mibBuilder.loadTexts:
    msanDiagnosticsTestTable.setStatus("current")
_MsanDiagnosticsTestEntry_Object = MibTableRow
msanDiagnosticsTestEntry = _MsanDiagnosticsTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 14, 2, 1)
)
msanDiagnosticsTestEntry.setIndexNames(
    (0, "ISKRATEL-MSAN-MIB", "msanDiagnosticsTestCode"),
)
if mibBuilder.loadTexts:
    msanDiagnosticsTestEntry.setStatus("current")


class _MsanDiagnosticsTestCode_Type(Integer32):
    """Custom type msanDiagnosticsTestCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999999),
    )


_MsanDiagnosticsTestCode_Type.__name__ = "Integer32"
_MsanDiagnosticsTestCode_Object = MibTableColumn
msanDiagnosticsTestCode = _MsanDiagnosticsTestCode_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 14, 2, 1, 1),
    _MsanDiagnosticsTestCode_Type()
)
msanDiagnosticsTestCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanDiagnosticsTestCode.setStatus("current")
_MsanDiagnosticsTestName_Type = OctetString
_MsanDiagnosticsTestName_Object = MibTableColumn
msanDiagnosticsTestName = _MsanDiagnosticsTestName_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 14, 2, 1, 2),
    _MsanDiagnosticsTestName_Type()
)
msanDiagnosticsTestName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDiagnosticsTestName.setStatus("current")


class _MsanDiagnosticsTestActivity_Type(Integer32):
    """Custom type msanDiagnosticsTestActivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("testOff", 2),
          ("testOn", 1))
    )


_MsanDiagnosticsTestActivity_Type.__name__ = "Integer32"
_MsanDiagnosticsTestActivity_Object = MibTableColumn
msanDiagnosticsTestActivity = _MsanDiagnosticsTestActivity_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 14, 2, 1, 3),
    _MsanDiagnosticsTestActivity_Type()
)
msanDiagnosticsTestActivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDiagnosticsTestActivity.setStatus("current")


class _MsanDiagnosticsTestTime_Type(Unsigned32):
    """Custom type msanDiagnosticsTestTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 999999900),
    )


_MsanDiagnosticsTestTime_Type.__name__ = "Unsigned32"
_MsanDiagnosticsTestTime_Object = MibTableColumn
msanDiagnosticsTestTime = _MsanDiagnosticsTestTime_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 14, 2, 1, 4),
    _MsanDiagnosticsTestTime_Type()
)
msanDiagnosticsTestTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDiagnosticsTestTime.setStatus("current")


class _MsanDiagnosticsTestPriority_Type(Integer32):
    """Custom type msanDiagnosticsTestPriority based on Integer32"""
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
        *(("high", 2),
          ("low", 0),
          ("medium", 1),
          ("veryHigh", 3))
    )


_MsanDiagnosticsTestPriority_Type.__name__ = "Integer32"
_MsanDiagnosticsTestPriority_Object = MibTableColumn
msanDiagnosticsTestPriority = _MsanDiagnosticsTestPriority_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 14, 2, 1, 6),
    _MsanDiagnosticsTestPriority_Type()
)
msanDiagnosticsTestPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDiagnosticsTestPriority.setStatus("current")


class _MsanDiagnosticsTestType_Type(Integer32):
    """Custom type msanDiagnosticsTestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("testAtReload", 1),
          ("testDaily", 3),
          ("testPeriodically", 2))
    )


_MsanDiagnosticsTestType_Type.__name__ = "Integer32"
_MsanDiagnosticsTestType_Object = MibTableColumn
msanDiagnosticsTestType = _MsanDiagnosticsTestType_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 14, 2, 1, 7),
    _MsanDiagnosticsTestType_Type()
)
msanDiagnosticsTestType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDiagnosticsTestType.setStatus("current")
_MsanDiagnosticsTestTimeMin_Type = Integer32
_MsanDiagnosticsTestTimeMin_Object = MibTableColumn
msanDiagnosticsTestTimeMin = _MsanDiagnosticsTestTimeMin_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 14, 2, 1, 8),
    _MsanDiagnosticsTestTimeMin_Type()
)
msanDiagnosticsTestTimeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDiagnosticsTestTimeMin.setStatus("current")
_MsanDiagnosticsTestTimeMax_Type = Integer32
_MsanDiagnosticsTestTimeMax_Object = MibTableColumn
msanDiagnosticsTestTimeMax = _MsanDiagnosticsTestTimeMax_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 14, 2, 1, 9),
    _MsanDiagnosticsTestTimeMax_Type()
)
msanDiagnosticsTestTimeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDiagnosticsTestTimeMax.setStatus("current")
_MsanDiagnosticsErrorTable_Object = MibTable
msanDiagnosticsErrorTable = _MsanDiagnosticsErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 14, 3)
)
if mibBuilder.loadTexts:
    msanDiagnosticsErrorTable.setStatus("current")
_MsanDiagnosticsErrorEntry_Object = MibTableRow
msanDiagnosticsErrorEntry = _MsanDiagnosticsErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 14, 3, 1)
)
msanDiagnosticsErrorEntry.setIndexNames(
    (0, "ISKRATEL-MSAN-MIB", "msanDiagnosticsErrorCode"),
)
if mibBuilder.loadTexts:
    msanDiagnosticsErrorEntry.setStatus("current")


class _MsanDiagnosticsErrorCode_Type(Integer32):
    """Custom type msanDiagnosticsErrorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999999),
    )


_MsanDiagnosticsErrorCode_Type.__name__ = "Integer32"
_MsanDiagnosticsErrorCode_Object = MibTableColumn
msanDiagnosticsErrorCode = _MsanDiagnosticsErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 14, 3, 1, 1),
    _MsanDiagnosticsErrorCode_Type()
)
msanDiagnosticsErrorCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanDiagnosticsErrorCode.setStatus("current")
_MsanDiagnosticsErrorDescription_Type = OctetString
_MsanDiagnosticsErrorDescription_Object = MibTableColumn
msanDiagnosticsErrorDescription = _MsanDiagnosticsErrorDescription_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 14, 3, 1, 2),
    _MsanDiagnosticsErrorDescription_Type()
)
msanDiagnosticsErrorDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDiagnosticsErrorDescription.setStatus("current")


class _MsanDiagnosticsErrorPriority_Type(Integer32):
    """Custom type msanDiagnosticsErrorPriority based on Integer32"""
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
        *(("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("warning", 4))
    )


_MsanDiagnosticsErrorPriority_Type.__name__ = "Integer32"
_MsanDiagnosticsErrorPriority_Object = MibTableColumn
msanDiagnosticsErrorPriority = _MsanDiagnosticsErrorPriority_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 14, 3, 1, 3),
    _MsanDiagnosticsErrorPriority_Type()
)
msanDiagnosticsErrorPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDiagnosticsErrorPriority.setStatus("current")
_MsanDiagnosticsErrorObjectType_Type = OctetString
_MsanDiagnosticsErrorObjectType_Object = MibTableColumn
msanDiagnosticsErrorObjectType = _MsanDiagnosticsErrorObjectType_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 14, 3, 1, 4),
    _MsanDiagnosticsErrorObjectType_Type()
)
msanDiagnosticsErrorObjectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDiagnosticsErrorObjectType.setStatus("current")
_MsanDiagnosticsErrorMeasure_Type = OctetString
_MsanDiagnosticsErrorMeasure_Object = MibTableColumn
msanDiagnosticsErrorMeasure = _MsanDiagnosticsErrorMeasure_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 14, 3, 1, 5),
    _MsanDiagnosticsErrorMeasure_Type()
)
msanDiagnosticsErrorMeasure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDiagnosticsErrorMeasure.setStatus("current")


class _MsanDiagnosticsErrorMeasureActive_Type(Integer32):
    """Custom type msanDiagnosticsErrorMeasureActive based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notActive", 0))
    )


_MsanDiagnosticsErrorMeasureActive_Type.__name__ = "Integer32"
_MsanDiagnosticsErrorMeasureActive_Object = MibTableColumn
msanDiagnosticsErrorMeasureActive = _MsanDiagnosticsErrorMeasureActive_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 14, 3, 1, 6),
    _MsanDiagnosticsErrorMeasureActive_Type()
)
msanDiagnosticsErrorMeasureActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDiagnosticsErrorMeasureActive.setStatus("current")
_MsanDiagnosticsErrorProbableCause_Type = Integer32
_MsanDiagnosticsErrorProbableCause_Object = MibTableColumn
msanDiagnosticsErrorProbableCause = _MsanDiagnosticsErrorProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 14, 3, 1, 7),
    _MsanDiagnosticsErrorProbableCause_Type()
)
msanDiagnosticsErrorProbableCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDiagnosticsErrorProbableCause.setStatus("current")
_MsanDiagnosticsErrorObjectTypeId_Type = Integer32
_MsanDiagnosticsErrorObjectTypeId_Object = MibTableColumn
msanDiagnosticsErrorObjectTypeId = _MsanDiagnosticsErrorObjectTypeId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 14, 3, 1, 8),
    _MsanDiagnosticsErrorObjectTypeId_Type()
)
msanDiagnosticsErrorObjectTypeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDiagnosticsErrorObjectTypeId.setStatus("current")
_MsanDiagnosticsErrorMeasureId_Type = Integer32
_MsanDiagnosticsErrorMeasureId_Object = MibTableColumn
msanDiagnosticsErrorMeasureId = _MsanDiagnosticsErrorMeasureId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 14, 3, 1, 9),
    _MsanDiagnosticsErrorMeasureId_Type()
)
msanDiagnosticsErrorMeasureId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDiagnosticsErrorMeasureId.setStatus("current")
_MsanDiagnosticsTempTable_Object = MibTable
msanDiagnosticsTempTable = _MsanDiagnosticsTempTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 14, 4)
)
if mibBuilder.loadTexts:
    msanDiagnosticsTempTable.setStatus("current")
_MsanDiagnosticsTempEntry_Object = MibTableRow
msanDiagnosticsTempEntry = _MsanDiagnosticsTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 14, 4, 1)
)
msanDiagnosticsTempEntry.setIndexNames(
    (0, "ISKRATEL-MSAN-MIB", "msanDiagnosticsTempSensorID"),
)
if mibBuilder.loadTexts:
    msanDiagnosticsTempEntry.setStatus("current")


class _MsanDiagnosticsTempSensorID_Type(Integer32):
    """Custom type msanDiagnosticsTempSensorID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MsanDiagnosticsTempSensorID_Type.__name__ = "Integer32"
_MsanDiagnosticsTempSensorID_Object = MibTableColumn
msanDiagnosticsTempSensorID = _MsanDiagnosticsTempSensorID_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 14, 4, 1, 1),
    _MsanDiagnosticsTempSensorID_Type()
)
msanDiagnosticsTempSensorID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanDiagnosticsTempSensorID.setStatus("current")
_MsanDiagnosticsTempSensorName_Type = OctetString
_MsanDiagnosticsTempSensorName_Object = MibTableColumn
msanDiagnosticsTempSensorName = _MsanDiagnosticsTempSensorName_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 14, 4, 1, 2),
    _MsanDiagnosticsTempSensorName_Type()
)
msanDiagnosticsTempSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDiagnosticsTempSensorName.setStatus("current")
_MsanDiagnosticsTempCurrent_Type = Integer32
_MsanDiagnosticsTempCurrent_Object = MibTableColumn
msanDiagnosticsTempCurrent = _MsanDiagnosticsTempCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 14, 4, 1, 3),
    _MsanDiagnosticsTempCurrent_Type()
)
msanDiagnosticsTempCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDiagnosticsTempCurrent.setStatus("current")
_MsanDiagnosticsTempCriticUnderheatThreshold_Type = Integer32
_MsanDiagnosticsTempCriticUnderheatThreshold_Object = MibTableColumn
msanDiagnosticsTempCriticUnderheatThreshold = _MsanDiagnosticsTempCriticUnderheatThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 14, 4, 1, 4),
    _MsanDiagnosticsTempCriticUnderheatThreshold_Type()
)
msanDiagnosticsTempCriticUnderheatThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDiagnosticsTempCriticUnderheatThreshold.setStatus("current")
_MsanDiagnosticsTempUnderheatThreshold_Type = Integer32
_MsanDiagnosticsTempUnderheatThreshold_Object = MibTableColumn
msanDiagnosticsTempUnderheatThreshold = _MsanDiagnosticsTempUnderheatThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 14, 4, 1, 5),
    _MsanDiagnosticsTempUnderheatThreshold_Type()
)
msanDiagnosticsTempUnderheatThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDiagnosticsTempUnderheatThreshold.setStatus("current")
_MsanDiagnosticsTempOverheatThreshold_Type = Integer32
_MsanDiagnosticsTempOverheatThreshold_Object = MibTableColumn
msanDiagnosticsTempOverheatThreshold = _MsanDiagnosticsTempOverheatThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 14, 4, 1, 6),
    _MsanDiagnosticsTempOverheatThreshold_Type()
)
msanDiagnosticsTempOverheatThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDiagnosticsTempOverheatThreshold.setStatus("current")
_MsanDiagnosticsTempCriticOverheatThreshold_Type = Integer32
_MsanDiagnosticsTempCriticOverheatThreshold_Object = MibTableColumn
msanDiagnosticsTempCriticOverheatThreshold = _MsanDiagnosticsTempCriticOverheatThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 14, 4, 1, 7),
    _MsanDiagnosticsTempCriticOverheatThreshold_Type()
)
msanDiagnosticsTempCriticOverheatThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDiagnosticsTempCriticOverheatThreshold.setStatus("current")
_MsanDiagnosticsErrorFilterTable_Object = MibTable
msanDiagnosticsErrorFilterTable = _MsanDiagnosticsErrorFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 14, 5)
)
if mibBuilder.loadTexts:
    msanDiagnosticsErrorFilterTable.setStatus("current")
_MsanDiagnosticsErrorFilterEntry_Object = MibTableRow
msanDiagnosticsErrorFilterEntry = _MsanDiagnosticsErrorFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 14, 5, 1)
)
msanDiagnosticsErrorFilterEntry.setIndexNames(
    (0, "ISKRATEL-MSAN-MIB", "msanDiagnosticsErrorFilterErrMask"),
    (0, "ISKRATEL-MSAN-MIB", "msanDiagnosticsErrorFilterObjMask"),
)
if mibBuilder.loadTexts:
    msanDiagnosticsErrorFilterEntry.setStatus("current")


class _MsanDiagnosticsErrorFilterErrMask_Type(OctetString):
    """Custom type msanDiagnosticsErrorFilterErrMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_MsanDiagnosticsErrorFilterErrMask_Type.__name__ = "OctetString"
_MsanDiagnosticsErrorFilterErrMask_Object = MibTableColumn
msanDiagnosticsErrorFilterErrMask = _MsanDiagnosticsErrorFilterErrMask_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 14, 5, 1, 1),
    _MsanDiagnosticsErrorFilterErrMask_Type()
)
msanDiagnosticsErrorFilterErrMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanDiagnosticsErrorFilterErrMask.setStatus("current")


class _MsanDiagnosticsErrorFilterObjMask_Type(OctetString):
    """Custom type msanDiagnosticsErrorFilterObjMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_MsanDiagnosticsErrorFilterObjMask_Type.__name__ = "OctetString"
_MsanDiagnosticsErrorFilterObjMask_Object = MibTableColumn
msanDiagnosticsErrorFilterObjMask = _MsanDiagnosticsErrorFilterObjMask_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 14, 5, 1, 2),
    _MsanDiagnosticsErrorFilterObjMask_Type()
)
msanDiagnosticsErrorFilterObjMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanDiagnosticsErrorFilterObjMask.setStatus("current")
_MsanDiagnosticsErrorFilterRowStatus_Type = RowStatus
_MsanDiagnosticsErrorFilterRowStatus_Object = MibTableColumn
msanDiagnosticsErrorFilterRowStatus = _MsanDiagnosticsErrorFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 14, 5, 1, 3),
    _MsanDiagnosticsErrorFilterRowStatus_Type()
)
msanDiagnosticsErrorFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanDiagnosticsErrorFilterRowStatus.setStatus("current")
_MsanDiagnosticsErrorSeverityTable_Object = MibTable
msanDiagnosticsErrorSeverityTable = _MsanDiagnosticsErrorSeverityTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 14, 6)
)
if mibBuilder.loadTexts:
    msanDiagnosticsErrorSeverityTable.setStatus("current")
_MsanDiagnosticsErrorSeverityEntry_Object = MibTableRow
msanDiagnosticsErrorSeverityEntry = _MsanDiagnosticsErrorSeverityEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 14, 6, 1)
)
msanDiagnosticsErrorSeverityEntry.setIndexNames(
    (0, "ISKRATEL-MSAN-MIB", "msanDiagnosticsErrorSeverityErrCode"),
    (0, "ISKRATEL-MSAN-MIB", "msanDiagnosticsErrorSeverityObjMask"),
)
if mibBuilder.loadTexts:
    msanDiagnosticsErrorSeverityEntry.setStatus("current")
_MsanDiagnosticsErrorSeverityErrCode_Type = Integer32
_MsanDiagnosticsErrorSeverityErrCode_Object = MibTableColumn
msanDiagnosticsErrorSeverityErrCode = _MsanDiagnosticsErrorSeverityErrCode_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 14, 6, 1, 1),
    _MsanDiagnosticsErrorSeverityErrCode_Type()
)
msanDiagnosticsErrorSeverityErrCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanDiagnosticsErrorSeverityErrCode.setStatus("current")


class _MsanDiagnosticsErrorSeverityErrPriority_Type(Integer32):
    """Custom type msanDiagnosticsErrorSeverityErrPriority based on Integer32"""
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
        *(("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("warning", 4))
    )


_MsanDiagnosticsErrorSeverityErrPriority_Type.__name__ = "Integer32"
_MsanDiagnosticsErrorSeverityErrPriority_Object = MibTableColumn
msanDiagnosticsErrorSeverityErrPriority = _MsanDiagnosticsErrorSeverityErrPriority_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 14, 6, 1, 2),
    _MsanDiagnosticsErrorSeverityErrPriority_Type()
)
msanDiagnosticsErrorSeverityErrPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanDiagnosticsErrorSeverityErrPriority.setStatus("current")


class _MsanDiagnosticsErrorSeverityObjMask_Type(OctetString):
    """Custom type msanDiagnosticsErrorSeverityObjMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_MsanDiagnosticsErrorSeverityObjMask_Type.__name__ = "OctetString"
_MsanDiagnosticsErrorSeverityObjMask_Object = MibTableColumn
msanDiagnosticsErrorSeverityObjMask = _MsanDiagnosticsErrorSeverityObjMask_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 14, 6, 1, 3),
    _MsanDiagnosticsErrorSeverityObjMask_Type()
)
msanDiagnosticsErrorSeverityObjMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanDiagnosticsErrorSeverityObjMask.setStatus("current")
_MsanDiagnosticsErrorSeverityRowStatus_Type = RowStatus
_MsanDiagnosticsErrorSeverityRowStatus_Object = MibTableColumn
msanDiagnosticsErrorSeverityRowStatus = _MsanDiagnosticsErrorSeverityRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 14, 6, 1, 4),
    _MsanDiagnosticsErrorSeverityRowStatus_Type()
)
msanDiagnosticsErrorSeverityRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanDiagnosticsErrorSeverityRowStatus.setStatus("current")
_MsanPpp_ObjectIdentity = ObjectIdentity
msanPpp = _MsanPpp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 15)
)
_MsanPppGlobal_ObjectIdentity = ObjectIdentity
msanPppGlobal = _MsanPppGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 15, 1)
)
_MsanPppLocalIpAddress_Type = IpAddress
_MsanPppLocalIpAddress_Object = MibScalar
msanPppLocalIpAddress = _MsanPppLocalIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 15, 1, 1),
    _MsanPppLocalIpAddress_Type()
)
msanPppLocalIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanPppLocalIpAddress.setStatus("current")
_MsanPppRemoteIpAddress_Type = IpAddress
_MsanPppRemoteIpAddress_Object = MibScalar
msanPppRemoteIpAddress = _MsanPppRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 15, 1, 2),
    _MsanPppRemoteIpAddress_Type()
)
msanPppRemoteIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanPppRemoteIpAddress.setStatus("current")


class _MsanPppAuthProtocol_Type(Integer32):
    """Custom type msanPppAuthProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("chap", 1),
          ("none", 0),
          ("pap", 2))
    )


_MsanPppAuthProtocol_Type.__name__ = "Integer32"
_MsanPppAuthProtocol_Object = MibScalar
msanPppAuthProtocol = _MsanPppAuthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 15, 1, 3),
    _MsanPppAuthProtocol_Type()
)
msanPppAuthProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanPppAuthProtocol.setStatus("current")
_MsanPppEchoInterval_Type = Integer32
_MsanPppEchoInterval_Object = MibScalar
msanPppEchoInterval = _MsanPppEchoInterval_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 15, 1, 4),
    _MsanPppEchoInterval_Type()
)
msanPppEchoInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanPppEchoInterval.setStatus("current")
if mibBuilder.loadTexts:
    msanPppEchoInterval.setUnits("seconds")


class _MsanPppVanJacobsonCompression_Type(Integer32):
    """Custom type msanPppVanJacobsonCompression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanPppVanJacobsonCompression_Type.__name__ = "Integer32"
_MsanPppVanJacobsonCompression_Object = MibScalar
msanPppVanJacobsonCompression = _MsanPppVanJacobsonCompression_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 15, 1, 5),
    _MsanPppVanJacobsonCompression_Type()
)
msanPppVanJacobsonCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanPppVanJacobsonCompression.setStatus("current")


class _MsanPppAdminState_Type(Integer32):
    """Custom type msanPppAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanPppAdminState_Type.__name__ = "Integer32"
_MsanPppAdminState_Object = MibScalar
msanPppAdminState = _MsanPppAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 15, 1, 6),
    _MsanPppAdminState_Type()
)
msanPppAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanPppAdminState.setStatus("current")
_MsanAlarmPanel_ObjectIdentity = ObjectIdentity
msanAlarmPanel = _MsanAlarmPanel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 16)
)
_MsanAlarmPanelGlobal_ObjectIdentity = ObjectIdentity
msanAlarmPanelGlobal = _MsanAlarmPanelGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 16, 1)
)


class _MsanAlarmPanelAudioAlarmPriority_Type(Integer32):
    """Custom type msanAlarmPanelAudioAlarmPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("major", 2),
          ("minor", 3))
    )


_MsanAlarmPanelAudioAlarmPriority_Type.__name__ = "Integer32"
_MsanAlarmPanelAudioAlarmPriority_Object = MibScalar
msanAlarmPanelAudioAlarmPriority = _MsanAlarmPanelAudioAlarmPriority_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 16, 1, 1),
    _MsanAlarmPanelAudioAlarmPriority_Type()
)
msanAlarmPanelAudioAlarmPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanAlarmPanelAudioAlarmPriority.setStatus("current")


class _MsanAlarmPanelSerialPortType_Type(Integer32):
    """Custom type msanAlarmPanelSerialPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alarmPanel", 3),
          ("mps", 2),
          ("noConnection", 1))
    )


_MsanAlarmPanelSerialPortType_Type.__name__ = "Integer32"
_MsanAlarmPanelSerialPortType_Object = MibScalar
msanAlarmPanelSerialPortType = _MsanAlarmPanelSerialPortType_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 16, 1, 2),
    _MsanAlarmPanelSerialPortType_Type()
)
msanAlarmPanelSerialPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanAlarmPanelSerialPortType.setStatus("current")
_MsanAlarmPanelTable_Object = MibTable
msanAlarmPanelTable = _MsanAlarmPanelTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 16, 2)
)
if mibBuilder.loadTexts:
    msanAlarmPanelTable.setStatus("current")
_MsanAlarmPanelEntry_Object = MibTableRow
msanAlarmPanelEntry = _MsanAlarmPanelEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 16, 2, 1)
)
msanAlarmPanelEntry.setIndexNames(
    (0, "ISKRATEL-MSAN-MIB", "msanAlarmPanelIndex"),
)
if mibBuilder.loadTexts:
    msanAlarmPanelEntry.setStatus("current")


class _MsanAlarmPanelIndex_Type(Integer32):
    """Custom type msanAlarmPanelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_MsanAlarmPanelIndex_Type.__name__ = "Integer32"
_MsanAlarmPanelIndex_Object = MibTableColumn
msanAlarmPanelIndex = _MsanAlarmPanelIndex_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 16, 2, 1, 1),
    _MsanAlarmPanelIndex_Type()
)
msanAlarmPanelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanAlarmPanelIndex.setStatus("current")


class _MsanAlarmPanelConnectionState_Type(Integer32):
    """Custom type msanAlarmPanelConnectionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_MsanAlarmPanelConnectionState_Type.__name__ = "Integer32"
_MsanAlarmPanelConnectionState_Object = MibTableColumn
msanAlarmPanelConnectionState = _MsanAlarmPanelConnectionState_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 16, 2, 1, 2),
    _MsanAlarmPanelConnectionState_Type()
)
msanAlarmPanelConnectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAlarmPanelConnectionState.setStatus("current")


class _MsanAlarmPanelAdminState_Type(Integer32):
    """Custom type msanAlarmPanelAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("equipped", 1),
          ("unequipped", 0))
    )


_MsanAlarmPanelAdminState_Type.__name__ = "Integer32"
_MsanAlarmPanelAdminState_Object = MibTableColumn
msanAlarmPanelAdminState = _MsanAlarmPanelAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 16, 2, 1, 3),
    _MsanAlarmPanelAdminState_Type()
)
msanAlarmPanelAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanAlarmPanelAdminState.setStatus("current")
_MsanAlarmPanelIndicatorTable_Object = MibTable
msanAlarmPanelIndicatorTable = _MsanAlarmPanelIndicatorTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 16, 3)
)
if mibBuilder.loadTexts:
    msanAlarmPanelIndicatorTable.setStatus("current")
_MsanAlarmPanelIndicatorEntry_Object = MibTableRow
msanAlarmPanelIndicatorEntry = _MsanAlarmPanelIndicatorEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 16, 3, 1)
)
msanAlarmPanelIndicatorEntry.setIndexNames(
    (0, "ISKRATEL-MSAN-MIB", "msanAlarmPanelIndex"),
    (0, "ISKRATEL-MSAN-MIB", "msanAlarmPanelIndicatorIndex"),
)
if mibBuilder.loadTexts:
    msanAlarmPanelIndicatorEntry.setStatus("current")


class _MsanAlarmPanelIndicatorIndex_Type(Integer32):
    """Custom type msanAlarmPanelIndicatorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_MsanAlarmPanelIndicatorIndex_Type.__name__ = "Integer32"
_MsanAlarmPanelIndicatorIndex_Object = MibTableColumn
msanAlarmPanelIndicatorIndex = _MsanAlarmPanelIndicatorIndex_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 16, 3, 1, 1),
    _MsanAlarmPanelIndicatorIndex_Type()
)
msanAlarmPanelIndicatorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanAlarmPanelIndicatorIndex.setStatus("current")
_MsanAlarmPanelIndicatorErrCode_Type = Integer32
_MsanAlarmPanelIndicatorErrCode_Object = MibTableColumn
msanAlarmPanelIndicatorErrCode = _MsanAlarmPanelIndicatorErrCode_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 16, 3, 1, 2),
    _MsanAlarmPanelIndicatorErrCode_Type()
)
msanAlarmPanelIndicatorErrCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanAlarmPanelIndicatorErrCode.setStatus("current")
_MsanAlarmPanelInputTable_Object = MibTable
msanAlarmPanelInputTable = _MsanAlarmPanelInputTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 16, 4)
)
if mibBuilder.loadTexts:
    msanAlarmPanelInputTable.setStatus("current")
_MsanAlarmPanelInputEntry_Object = MibTableRow
msanAlarmPanelInputEntry = _MsanAlarmPanelInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 16, 4, 1)
)
msanAlarmPanelInputEntry.setIndexNames(
    (0, "ISKRATEL-MSAN-MIB", "msanAlarmPanelIndex"),
    (0, "ISKRATEL-MSAN-MIB", "msanAlarmPanelInputIndex"),
)
if mibBuilder.loadTexts:
    msanAlarmPanelInputEntry.setStatus("current")


class _MsanAlarmPanelInputIndex_Type(Integer32):
    """Custom type msanAlarmPanelInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_MsanAlarmPanelInputIndex_Type.__name__ = "Integer32"
_MsanAlarmPanelInputIndex_Object = MibTableColumn
msanAlarmPanelInputIndex = _MsanAlarmPanelInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 16, 4, 1, 1),
    _MsanAlarmPanelInputIndex_Type()
)
msanAlarmPanelInputIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanAlarmPanelInputIndex.setStatus("current")
_MsanAlarmPanelInputErrCode_Type = Integer32
_MsanAlarmPanelInputErrCode_Object = MibTableColumn
msanAlarmPanelInputErrCode = _MsanAlarmPanelInputErrCode_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 16, 4, 1, 2),
    _MsanAlarmPanelInputErrCode_Type()
)
msanAlarmPanelInputErrCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanAlarmPanelInputErrCode.setStatus("current")


class _MsanAlarmPanelInputActiveLevel_Type(Integer32):
    """Custom type msanAlarmPanelInputActiveLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0))
    )


_MsanAlarmPanelInputActiveLevel_Type.__name__ = "Integer32"
_MsanAlarmPanelInputActiveLevel_Object = MibTableColumn
msanAlarmPanelInputActiveLevel = _MsanAlarmPanelInputActiveLevel_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 16, 4, 1, 3),
    _MsanAlarmPanelInputActiveLevel_Type()
)
msanAlarmPanelInputActiveLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanAlarmPanelInputActiveLevel.setStatus("current")
_MsanMvr_ObjectIdentity = ObjectIdentity
msanMvr = _MsanMvr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 17)
)
_MsanMvrGlobal_ObjectIdentity = ObjectIdentity
msanMvrGlobal = _MsanMvrGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 17, 1)
)
_MsanMvrPortTable_Object = MibTable
msanMvrPortTable = _MsanMvrPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 17, 2)
)
if mibBuilder.loadTexts:
    msanMvrPortTable.setStatus("current")
_MsanMvrPortEntry_Object = MibTableRow
msanMvrPortEntry = _MsanMvrPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 17, 2, 1)
)
msanMvrPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    msanMvrPortEntry.setStatus("current")


class _MsanMvrPortAdminMode_Type(Integer32):
    """Custom type msanMvrPortAdminMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanMvrPortAdminMode_Type.__name__ = "Integer32"
_MsanMvrPortAdminMode_Object = MibTableColumn
msanMvrPortAdminMode = _MsanMvrPortAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 17, 2, 1, 1),
    _MsanMvrPortAdminMode_Type()
)
msanMvrPortAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanMvrPortAdminMode.setStatus("current")
_MsanMvrMulticastGroupTable_Object = MibTable
msanMvrMulticastGroupTable = _MsanMvrMulticastGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 17, 3)
)
if mibBuilder.loadTexts:
    msanMvrMulticastGroupTable.setStatus("current")
_MsanMvrMulticastGroupEntry_Object = MibTableRow
msanMvrMulticastGroupEntry = _MsanMvrMulticastGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 17, 3, 1)
)
msanMvrMulticastGroupEntry.setIndexNames(
    (0, "ISKRATEL-MSAN-MIB", "msanMvrMulticastGroupMVlanId"),
    (0, "ISKRATEL-MSAN-MIB", "msanMvrMulticastGroupStartIp"),
)
if mibBuilder.loadTexts:
    msanMvrMulticastGroupEntry.setStatus("current")
_MsanMvrMulticastGroupMVlanId_Type = Integer32
_MsanMvrMulticastGroupMVlanId_Object = MibTableColumn
msanMvrMulticastGroupMVlanId = _MsanMvrMulticastGroupMVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 17, 3, 1, 1),
    _MsanMvrMulticastGroupMVlanId_Type()
)
msanMvrMulticastGroupMVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanMvrMulticastGroupMVlanId.setStatus("current")
_MsanMvrMulticastGroupStartIp_Type = IpAddress
_MsanMvrMulticastGroupStartIp_Object = MibTableColumn
msanMvrMulticastGroupStartIp = _MsanMvrMulticastGroupStartIp_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 17, 3, 1, 2),
    _MsanMvrMulticastGroupStartIp_Type()
)
msanMvrMulticastGroupStartIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanMvrMulticastGroupStartIp.setStatus("current")
_MsanMvrMulticastGroupEndIp_Type = IpAddress
_MsanMvrMulticastGroupEndIp_Object = MibTableColumn
msanMvrMulticastGroupEndIp = _MsanMvrMulticastGroupEndIp_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 17, 3, 1, 3),
    _MsanMvrMulticastGroupEndIp_Type()
)
msanMvrMulticastGroupEndIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanMvrMulticastGroupEndIp.setStatus("current")
_MsanMvrMulticastGroupRowStatus_Type = RowStatus
_MsanMvrMulticastGroupRowStatus_Object = MibTableColumn
msanMvrMulticastGroupRowStatus = _MsanMvrMulticastGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 17, 3, 1, 4),
    _MsanMvrMulticastGroupRowStatus_Type()
)
msanMvrMulticastGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanMvrMulticastGroupRowStatus.setStatus("current")
_MsanMvrConfigTable_Object = MibTable
msanMvrConfigTable = _MsanMvrConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 17, 4)
)
if mibBuilder.loadTexts:
    msanMvrConfigTable.setStatus("current")
_MsanMvrConfigEntry_Object = MibTableRow
msanMvrConfigEntry = _MsanMvrConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 17, 4, 1)
)
msanMvrConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ISKRATEL-MSAN-MIB", "msanMvrConfigCVlanId"),
    (0, "ISKRATEL-MSAN-MIB", "msanMvrConfigMVlanId"),
)
if mibBuilder.loadTexts:
    msanMvrConfigEntry.setStatus("current")


class _MsanMvrConfigCVlanId_Type(Integer32):
    """Custom type msanMvrConfigCVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_MsanMvrConfigCVlanId_Type.__name__ = "Integer32"
_MsanMvrConfigCVlanId_Object = MibTableColumn
msanMvrConfigCVlanId = _MsanMvrConfigCVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 17, 4, 1, 1),
    _MsanMvrConfigCVlanId_Type()
)
msanMvrConfigCVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanMvrConfigCVlanId.setStatus("current")


class _MsanMvrConfigMVlanId_Type(Integer32):
    """Custom type msanMvrConfigMVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4092),
    )


_MsanMvrConfigMVlanId_Type.__name__ = "Integer32"
_MsanMvrConfigMVlanId_Object = MibTableColumn
msanMvrConfigMVlanId = _MsanMvrConfigMVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 17, 4, 1, 2),
    _MsanMvrConfigMVlanId_Type()
)
msanMvrConfigMVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanMvrConfigMVlanId.setStatus("current")


class _MsanMvrConfigCos_Type(Integer32):
    """Custom type msanMvrConfigCos based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_MsanMvrConfigCos_Type.__name__ = "Integer32"
_MsanMvrConfigCos_Object = MibTableColumn
msanMvrConfigCos = _MsanMvrConfigCos_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 17, 4, 1, 3),
    _MsanMvrConfigCos_Type()
)
msanMvrConfigCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanMvrConfigCos.setStatus("current")
_MsanMvrConfigRowStatus_Type = RowStatus
_MsanMvrConfigRowStatus_Object = MibTableColumn
msanMvrConfigRowStatus = _MsanMvrConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 17, 4, 1, 4),
    _MsanMvrConfigRowStatus_Type()
)
msanMvrConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanMvrConfigRowStatus.setStatus("current")
_MsanMvrDvlanTable_Object = MibTable
msanMvrDvlanTable = _MsanMvrDvlanTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 17, 5)
)
if mibBuilder.loadTexts:
    msanMvrDvlanTable.setStatus("current")
_MsanMvrDvlanEntry_Object = MibTableRow
msanMvrDvlanEntry = _MsanMvrDvlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 17, 5, 1)
)
msanMvrDvlanEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    msanMvrDvlanEntry.setStatus("current")


class _MsanMvrDvlanRmOuterTagStatus_Type(Integer32):
    """Custom type msanMvrDvlanRmOuterTagStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanMvrDvlanRmOuterTagStatus_Type.__name__ = "Integer32"
_MsanMvrDvlanRmOuterTagStatus_Object = MibTableColumn
msanMvrDvlanRmOuterTagStatus = _MsanMvrDvlanRmOuterTagStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 17, 5, 1, 1),
    _MsanMvrDvlanRmOuterTagStatus_Type()
)
msanMvrDvlanRmOuterTagStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanMvrDvlanRmOuterTagStatus.setStatus("current")


class _MsanMvrDvlanEthertypeRewriteStatus_Type(Integer32):
    """Custom type msanMvrDvlanEthertypeRewriteStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanMvrDvlanEthertypeRewriteStatus_Type.__name__ = "Integer32"
_MsanMvrDvlanEthertypeRewriteStatus_Object = MibTableColumn
msanMvrDvlanEthertypeRewriteStatus = _MsanMvrDvlanEthertypeRewriteStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 17, 5, 1, 2),
    _MsanMvrDvlanEthertypeRewriteStatus_Type()
)
msanMvrDvlanEthertypeRewriteStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanMvrDvlanEthertypeRewriteStatus.setStatus("current")
_MsanRemoteAccess_ObjectIdentity = ObjectIdentity
msanRemoteAccess = _MsanRemoteAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 18)
)
_MsanRemoteAccessGlobal_ObjectIdentity = ObjectIdentity
msanRemoteAccessGlobal = _MsanRemoteAccessGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 18, 1)
)
_MsanRemoteAccessFilterTable_Object = MibTable
msanRemoteAccessFilterTable = _MsanRemoteAccessFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 18, 2)
)
if mibBuilder.loadTexts:
    msanRemoteAccessFilterTable.setStatus("deprecated")
_MsanRemoteAccessFilterEntry_Object = MibTableRow
msanRemoteAccessFilterEntry = _MsanRemoteAccessFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 18, 2, 1)
)
msanRemoteAccessFilterEntry.setIndexNames(
    (0, "ISKRATEL-MSAN-MIB", "msanRemoteAccessFilterRuleIndex"),
)
if mibBuilder.loadTexts:
    msanRemoteAccessFilterEntry.setStatus("deprecated")


class _MsanRemoteAccessFilterRuleIndex_Type(Integer32):
    """Custom type msanRemoteAccessFilterRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_MsanRemoteAccessFilterRuleIndex_Type.__name__ = "Integer32"
_MsanRemoteAccessFilterRuleIndex_Object = MibTableColumn
msanRemoteAccessFilterRuleIndex = _MsanRemoteAccessFilterRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 18, 2, 1, 1),
    _MsanRemoteAccessFilterRuleIndex_Type()
)
msanRemoteAccessFilterRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanRemoteAccessFilterRuleIndex.setStatus("deprecated")
_MsanRemoteAccessFilterIp_Type = IpAddress
_MsanRemoteAccessFilterIp_Object = MibTableColumn
msanRemoteAccessFilterIp = _MsanRemoteAccessFilterIp_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 18, 2, 1, 2),
    _MsanRemoteAccessFilterIp_Type()
)
msanRemoteAccessFilterIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanRemoteAccessFilterIp.setStatus("deprecated")
_MsanRemoteAccessFilterNetmask_Type = IpAddress
_MsanRemoteAccessFilterNetmask_Object = MibTableColumn
msanRemoteAccessFilterNetmask = _MsanRemoteAccessFilterNetmask_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 18, 2, 1, 3),
    _MsanRemoteAccessFilterNetmask_Type()
)
msanRemoteAccessFilterNetmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanRemoteAccessFilterNetmask.setStatus("deprecated")


class _MsanRemoteAccessFilterAction_Type(Integer32):
    """Custom type msanRemoteAccessFilterAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("deny", 2))
    )


_MsanRemoteAccessFilterAction_Type.__name__ = "Integer32"
_MsanRemoteAccessFilterAction_Object = MibTableColumn
msanRemoteAccessFilterAction = _MsanRemoteAccessFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 18, 2, 1, 4),
    _MsanRemoteAccessFilterAction_Type()
)
msanRemoteAccessFilterAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanRemoteAccessFilterAction.setStatus("deprecated")
_MsanRemoteAccessFilterRowStatus_Type = RowStatus
_MsanRemoteAccessFilterRowStatus_Object = MibTableColumn
msanRemoteAccessFilterRowStatus = _MsanRemoteAccessFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 18, 2, 1, 5),
    _MsanRemoteAccessFilterRowStatus_Type()
)
msanRemoteAccessFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanRemoteAccessFilterRowStatus.setStatus("deprecated")
_MsanDslSpecific_ObjectIdentity = ObjectIdentity
msanDslSpecific = _MsanDslSpecific_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19)
)
_MsanDslSpecificGlobal_ObjectIdentity = ObjectIdentity
msanDslSpecificGlobal = _MsanDslSpecificGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 1)
)


class _MsanDslSpecificSystemState_Type(Integer32):
    """Custom type msanDslSpecificSystemState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              12)
        )
    )
    namedValues = NamedValues(
        *(("notReady", 12),
          ("operational", 4))
    )


_MsanDslSpecificSystemState_Type.__name__ = "Integer32"
_MsanDslSpecificSystemState_Object = MibScalar
msanDslSpecificSystemState = _MsanDslSpecificSystemState_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 1, 1),
    _MsanDslSpecificSystemState_Type()
)
msanDslSpecificSystemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDslSpecificSystemState.setStatus("current")
_MsanDslSpecificSystemFirmware_Type = OctetString
_MsanDslSpecificSystemFirmware_Object = MibScalar
msanDslSpecificSystemFirmware = _MsanDslSpecificSystemFirmware_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 1, 2),
    _MsanDslSpecificSystemFirmware_Type()
)
msanDslSpecificSystemFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDslSpecificSystemFirmware.setStatus("current")
_MsanDslSpecificTable_Object = MibTable
msanDslSpecificTable = _MsanDslSpecificTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 3)
)
if mibBuilder.loadTexts:
    msanDslSpecificTable.setStatus("current")
_MsanDslSpecificEntry_Object = MibTableRow
msanDslSpecificEntry = _MsanDslSpecificEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 3, 1)
)
msanDslSpecificEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    msanDslSpecificEntry.setStatus("current")
_MsanDslSpecificDsPsdMask_Type = OctetString
_MsanDslSpecificDsPsdMask_Object = MibTableColumn
msanDslSpecificDsPsdMask = _MsanDslSpecificDsPsdMask_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 3, 1, 1),
    _MsanDslSpecificDsPsdMask_Type()
)
msanDslSpecificDsPsdMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDslSpecificDsPsdMask.setStatus("current")


class _MsanDslSpecificUsPsdMask_Type(OctetString):
    """Custom type msanDslSpecificUsPsdMask based on OctetString"""
    defaultValue = OctetString("ANSI_FTTCab_M11")


_MsanDslSpecificUsPsdMask_Object = MibTableColumn
msanDslSpecificUsPsdMask = _MsanDslSpecificUsPsdMask_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 3, 1, 2),
    _MsanDslSpecificUsPsdMask_Type()
)
msanDslSpecificUsPsdMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDslSpecificUsPsdMask.setStatus("current")


class _MsanDslSpecificLineState_Type(Integer32):
    """Custom type msanDslSpecificLineState based on Integer32"""
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
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("activateInitTrain", 2),
          ("activeFullPower", 3),
          ("activeLowPower", 4),
          ("atpPtmLoopback", 6),
          ("dspDigitalLoopback", 7),
          ("hybridLoopback", 9),
          ("idle", 1),
          ("lineDriverDigitalLoopback", 8),
          ("loopDiagnosticsDelt", 12),
          ("loopDiagnosticsDeltInit", 11),
          ("quiet", 0),
          ("selt", 14),
          ("seltInits", 13),
          ("testMode", 10),
          ("unitFail", 5))
    )


_MsanDslSpecificLineState_Type.__name__ = "Integer32"
_MsanDslSpecificLineState_Object = MibTableColumn
msanDslSpecificLineState = _MsanDslSpecificLineState_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 3, 1, 3),
    _MsanDslSpecificLineState_Type()
)
msanDslSpecificLineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDslSpecificLineState.setStatus("current")


class _MsanDslSpecificMaxDelayDs_Type(Integer32):
    """Custom type msanDslSpecificMaxDelayDs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_MsanDslSpecificMaxDelayDs_Type.__name__ = "Integer32"
_MsanDslSpecificMaxDelayDs_Object = MibTableColumn
msanDslSpecificMaxDelayDs = _MsanDslSpecificMaxDelayDs_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 3, 1, 4),
    _MsanDslSpecificMaxDelayDs_Type()
)
msanDslSpecificMaxDelayDs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDslSpecificMaxDelayDs.setStatus("current")
if mibBuilder.loadTexts:
    msanDslSpecificMaxDelayDs.setUnits("milliseconds")


class _MsanDslSpecificMaxDelayUs_Type(Integer32):
    """Custom type msanDslSpecificMaxDelayUs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_MsanDslSpecificMaxDelayUs_Type.__name__ = "Integer32"
_MsanDslSpecificMaxDelayUs_Object = MibTableColumn
msanDslSpecificMaxDelayUs = _MsanDslSpecificMaxDelayUs_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 3, 1, 5),
    _MsanDslSpecificMaxDelayUs_Type()
)
msanDslSpecificMaxDelayUs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDslSpecificMaxDelayUs.setStatus("current")
if mibBuilder.loadTexts:
    msanDslSpecificMaxDelayUs.setUnits("milliseconds")


class _MsanDslSpecificMinProtectionDs_Type(Integer32):
    """Custom type msanDslSpecificMinProtectionDs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 160),
    )


_MsanDslSpecificMinProtectionDs_Type.__name__ = "Integer32"
_MsanDslSpecificMinProtectionDs_Object = MibTableColumn
msanDslSpecificMinProtectionDs = _MsanDslSpecificMinProtectionDs_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 3, 1, 6),
    _MsanDslSpecificMinProtectionDs_Type()
)
msanDslSpecificMinProtectionDs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDslSpecificMinProtectionDs.setStatus("current")
if mibBuilder.loadTexts:
    msanDslSpecificMinProtectionDs.setUnits("symbols")


class _MsanDslSpecificMinProtectionUs_Type(Integer32):
    """Custom type msanDslSpecificMinProtectionUs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 160),
    )


_MsanDslSpecificMinProtectionUs_Type.__name__ = "Integer32"
_MsanDslSpecificMinProtectionUs_Object = MibTableColumn
msanDslSpecificMinProtectionUs = _MsanDslSpecificMinProtectionUs_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 3, 1, 7),
    _MsanDslSpecificMinProtectionUs_Type()
)
msanDslSpecificMinProtectionUs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDslSpecificMinProtectionUs.setStatus("current")


class _MsanDslSpecificMaxSnrmDs_Type(Unsigned32):
    """Custom type msanDslSpecificMaxSnrmDs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_MsanDslSpecificMaxSnrmDs_Type.__name__ = "Unsigned32"
_MsanDslSpecificMaxSnrmDs_Object = MibTableColumn
msanDslSpecificMaxSnrmDs = _MsanDslSpecificMaxSnrmDs_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 3, 1, 8),
    _MsanDslSpecificMaxSnrmDs_Type()
)
msanDslSpecificMaxSnrmDs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDslSpecificMaxSnrmDs.setStatus("current")
if mibBuilder.loadTexts:
    msanDslSpecificMaxSnrmDs.setUnits("0.1 dB")


class _MsanDslSpecificMinSnrmDs_Type(Unsigned32):
    """Custom type msanDslSpecificMinSnrmDs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_MsanDslSpecificMinSnrmDs_Type.__name__ = "Unsigned32"
_MsanDslSpecificMinSnrmDs_Object = MibTableColumn
msanDslSpecificMinSnrmDs = _MsanDslSpecificMinSnrmDs_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 3, 1, 9),
    _MsanDslSpecificMinSnrmDs_Type()
)
msanDslSpecificMinSnrmDs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDslSpecificMinSnrmDs.setStatus("current")
if mibBuilder.loadTexts:
    msanDslSpecificMinSnrmDs.setUnits("0.1 dB")


class _MsanDslSpecificMaxSnrmUs_Type(Unsigned32):
    """Custom type msanDslSpecificMaxSnrmUs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_MsanDslSpecificMaxSnrmUs_Type.__name__ = "Unsigned32"
_MsanDslSpecificMaxSnrmUs_Object = MibTableColumn
msanDslSpecificMaxSnrmUs = _MsanDslSpecificMaxSnrmUs_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 3, 1, 10),
    _MsanDslSpecificMaxSnrmUs_Type()
)
msanDslSpecificMaxSnrmUs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDslSpecificMaxSnrmUs.setStatus("current")
if mibBuilder.loadTexts:
    msanDslSpecificMaxSnrmUs.setUnits("0.1 dB")


class _MsanDslSpecificMinSnrmUs_Type(Unsigned32):
    """Custom type msanDslSpecificMinSnrmUs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_MsanDslSpecificMinSnrmUs_Type.__name__ = "Unsigned32"
_MsanDslSpecificMinSnrmUs_Object = MibTableColumn
msanDslSpecificMinSnrmUs = _MsanDslSpecificMinSnrmUs_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 3, 1, 11),
    _MsanDslSpecificMinSnrmUs_Type()
)
msanDslSpecificMinSnrmUs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDslSpecificMinSnrmUs.setStatus("current")
if mibBuilder.loadTexts:
    msanDslSpecificMinSnrmUs.setUnits("0.1 dB")


class _MsanDslSpecificRaUsNrmDs_Type(Unsigned32):
    """Custom type msanDslSpecificRaUsNrmDs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_MsanDslSpecificRaUsNrmDs_Type.__name__ = "Unsigned32"
_MsanDslSpecificRaUsNrmDs_Object = MibTableColumn
msanDslSpecificRaUsNrmDs = _MsanDslSpecificRaUsNrmDs_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 3, 1, 12),
    _MsanDslSpecificRaUsNrmDs_Type()
)
msanDslSpecificRaUsNrmDs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDslSpecificRaUsNrmDs.setStatus("current")
if mibBuilder.loadTexts:
    msanDslSpecificRaUsNrmDs.setUnits("0.1 dB")


class _MsanDslSpecificRaUsNrmUs_Type(Unsigned32):
    """Custom type msanDslSpecificRaUsNrmUs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_MsanDslSpecificRaUsNrmUs_Type.__name__ = "Unsigned32"
_MsanDslSpecificRaUsNrmUs_Object = MibTableColumn
msanDslSpecificRaUsNrmUs = _MsanDslSpecificRaUsNrmUs_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 3, 1, 13),
    _MsanDslSpecificRaUsNrmUs_Type()
)
msanDslSpecificRaUsNrmUs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDslSpecificRaUsNrmUs.setStatus("current")
if mibBuilder.loadTexts:
    msanDslSpecificRaUsNrmUs.setUnits("0.1 dB")


class _MsanDslSpecificRaUsTimeDs_Type(Unsigned32):
    """Custom type msanDslSpecificRaUsTimeDs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_MsanDslSpecificRaUsTimeDs_Type.__name__ = "Unsigned32"
_MsanDslSpecificRaUsTimeDs_Object = MibTableColumn
msanDslSpecificRaUsTimeDs = _MsanDslSpecificRaUsTimeDs_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 3, 1, 14),
    _MsanDslSpecificRaUsTimeDs_Type()
)
msanDslSpecificRaUsTimeDs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDslSpecificRaUsTimeDs.setStatus("current")
if mibBuilder.loadTexts:
    msanDslSpecificRaUsTimeDs.setUnits("seconds")


class _MsanDslSpecificRaUsTimeUs_Type(Unsigned32):
    """Custom type msanDslSpecificRaUsTimeUs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_MsanDslSpecificRaUsTimeUs_Type.__name__ = "Unsigned32"
_MsanDslSpecificRaUsTimeUs_Object = MibTableColumn
msanDslSpecificRaUsTimeUs = _MsanDslSpecificRaUsTimeUs_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 3, 1, 15),
    _MsanDslSpecificRaUsTimeUs_Type()
)
msanDslSpecificRaUsTimeUs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDslSpecificRaUsTimeUs.setStatus("current")
if mibBuilder.loadTexts:
    msanDslSpecificRaUsTimeUs.setUnits("seconds")


class _MsanDslSpecificRaDsNrmDs_Type(Unsigned32):
    """Custom type msanDslSpecificRaDsNrmDs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_MsanDslSpecificRaDsNrmDs_Type.__name__ = "Unsigned32"
_MsanDslSpecificRaDsNrmDs_Object = MibTableColumn
msanDslSpecificRaDsNrmDs = _MsanDslSpecificRaDsNrmDs_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 3, 1, 16),
    _MsanDslSpecificRaDsNrmDs_Type()
)
msanDslSpecificRaDsNrmDs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDslSpecificRaDsNrmDs.setStatus("current")
if mibBuilder.loadTexts:
    msanDslSpecificRaDsNrmDs.setUnits("0.1 dB")


class _MsanDslSpecificRaDsNrmUs_Type(Unsigned32):
    """Custom type msanDslSpecificRaDsNrmUs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_MsanDslSpecificRaDsNrmUs_Type.__name__ = "Unsigned32"
_MsanDslSpecificRaDsNrmUs_Object = MibTableColumn
msanDslSpecificRaDsNrmUs = _MsanDslSpecificRaDsNrmUs_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 3, 1, 17),
    _MsanDslSpecificRaDsNrmUs_Type()
)
msanDslSpecificRaDsNrmUs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDslSpecificRaDsNrmUs.setStatus("current")
if mibBuilder.loadTexts:
    msanDslSpecificRaDsNrmUs.setUnits("0.1 dB")


class _MsanDslSpecificRaDsTimeDs_Type(Unsigned32):
    """Custom type msanDslSpecificRaDsTimeDs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_MsanDslSpecificRaDsTimeDs_Type.__name__ = "Unsigned32"
_MsanDslSpecificRaDsTimeDs_Object = MibTableColumn
msanDslSpecificRaDsTimeDs = _MsanDslSpecificRaDsTimeDs_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 3, 1, 18),
    _MsanDslSpecificRaDsTimeDs_Type()
)
msanDslSpecificRaDsTimeDs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDslSpecificRaDsTimeDs.setStatus("current")
if mibBuilder.loadTexts:
    msanDslSpecificRaDsTimeDs.setUnits("seconds")


class _MsanDslSpecificRaDsTimeUs_Type(Unsigned32):
    """Custom type msanDslSpecificRaDsTimeUs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_MsanDslSpecificRaDsTimeUs_Type.__name__ = "Unsigned32"
_MsanDslSpecificRaDsTimeUs_Object = MibTableColumn
msanDslSpecificRaDsTimeUs = _MsanDslSpecificRaDsTimeUs_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 3, 1, 19),
    _MsanDslSpecificRaDsTimeUs_Type()
)
msanDslSpecificRaDsTimeUs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDslSpecificRaDsTimeUs.setStatus("current")
if mibBuilder.loadTexts:
    msanDslSpecificRaDsTimeUs.setUnits("seconds")


class _MsanDslSpecificL0Time_Type(Unsigned32):
    """Custom type msanDslSpecificL0Time based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanDslSpecificL0Time_Type.__name__ = "Unsigned32"
_MsanDslSpecificL0Time_Object = MibTableColumn
msanDslSpecificL0Time = _MsanDslSpecificL0Time_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 3, 1, 20),
    _MsanDslSpecificL0Time_Type()
)
msanDslSpecificL0Time.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDslSpecificL0Time.setStatus("current")
if mibBuilder.loadTexts:
    msanDslSpecificL0Time.setUnits("seconds")


class _MsanDslSpecificL2Time_Type(Unsigned32):
    """Custom type msanDslSpecificL2Time based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanDslSpecificL2Time_Type.__name__ = "Unsigned32"
_MsanDslSpecificL2Time_Object = MibTableColumn
msanDslSpecificL2Time = _MsanDslSpecificL2Time_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 3, 1, 21),
    _MsanDslSpecificL2Time_Type()
)
msanDslSpecificL2Time.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDslSpecificL2Time.setStatus("current")
if mibBuilder.loadTexts:
    msanDslSpecificL2Time.setUnits("seconds")


class _MsanDslSpecificL2Atpr_Type(Unsigned32):
    """Custom type msanDslSpecificL2Atpr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_MsanDslSpecificL2Atpr_Type.__name__ = "Unsigned32"
_MsanDslSpecificL2Atpr_Object = MibTableColumn
msanDslSpecificL2Atpr = _MsanDslSpecificL2Atpr_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 3, 1, 22),
    _MsanDslSpecificL2Atpr_Type()
)
msanDslSpecificL2Atpr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDslSpecificL2Atpr.setStatus("current")
if mibBuilder.loadTexts:
    msanDslSpecificL2Atpr.setUnits("dB")


class _MsanDslSpecificL2Atprt_Type(Unsigned32):
    """Custom type msanDslSpecificL2Atprt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_MsanDslSpecificL2Atprt_Type.__name__ = "Unsigned32"
_MsanDslSpecificL2Atprt_Object = MibTableColumn
msanDslSpecificL2Atprt = _MsanDslSpecificL2Atprt_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 3, 1, 23),
    _MsanDslSpecificL2Atprt_Type()
)
msanDslSpecificL2Atprt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDslSpecificL2Atprt.setStatus("current")
if mibBuilder.loadTexts:
    msanDslSpecificL2Atprt.setUnits("dB")


class _MsanDslSpecificScMaskDs_Type(OctetString):
    """Custom type msanDslSpecificScMaskDs based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_MsanDslSpecificScMaskDs_Type.__name__ = "OctetString"
_MsanDslSpecificScMaskDs_Object = MibTableColumn
msanDslSpecificScMaskDs = _MsanDslSpecificScMaskDs_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 3, 1, 24),
    _MsanDslSpecificScMaskDs_Type()
)
msanDslSpecificScMaskDs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDslSpecificScMaskDs.setStatus("current")


class _MsanDslSpecificScMaskUs_Type(OctetString):
    """Custom type msanDslSpecificScMaskUs based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_MsanDslSpecificScMaskUs_Type.__name__ = "OctetString"
_MsanDslSpecificScMaskUs_Object = MibTableColumn
msanDslSpecificScMaskUs = _MsanDslSpecificScMaskUs_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 3, 1, 25),
    _MsanDslSpecificScMaskUs_Type()
)
msanDslSpecificScMaskUs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDslSpecificScMaskUs.setStatus("current")


class _MsanDslSpecificRfiBands_Type(OctetString):
    """Custom type msanDslSpecificRfiBands based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MsanDslSpecificRfiBands_Type.__name__ = "OctetString"
_MsanDslSpecificRfiBands_Object = MibTableColumn
msanDslSpecificRfiBands = _MsanDslSpecificRfiBands_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 3, 1, 26),
    _MsanDslSpecificRfiBands_Type()
)
msanDslSpecificRfiBands.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDslSpecificRfiBands.setStatus("current")


class _MsanDslSpecificMaxNomPsdDs_Type(Integer32):
    """Custom type msanDslSpecificMaxNomPsdDs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-600, -300),
    )


_MsanDslSpecificMaxNomPsdDs_Type.__name__ = "Integer32"
_MsanDslSpecificMaxNomPsdDs_Object = MibTableColumn
msanDslSpecificMaxNomPsdDs = _MsanDslSpecificMaxNomPsdDs_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 3, 1, 27),
    _MsanDslSpecificMaxNomPsdDs_Type()
)
msanDslSpecificMaxNomPsdDs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDslSpecificMaxNomPsdDs.setStatus("current")
if mibBuilder.loadTexts:
    msanDslSpecificMaxNomPsdDs.setUnits("0.1 dBm/Hz")


class _MsanDslSpecificMaxNomPsdUs_Type(Integer32):
    """Custom type msanDslSpecificMaxNomPsdUs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-600, -300),
    )


_MsanDslSpecificMaxNomPsdUs_Type.__name__ = "Integer32"
_MsanDslSpecificMaxNomPsdUs_Object = MibTableColumn
msanDslSpecificMaxNomPsdUs = _MsanDslSpecificMaxNomPsdUs_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 3, 1, 28),
    _MsanDslSpecificMaxNomPsdUs_Type()
)
msanDslSpecificMaxNomPsdUs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDslSpecificMaxNomPsdUs.setStatus("current")
if mibBuilder.loadTexts:
    msanDslSpecificMaxNomPsdUs.setUnits("0.1 dBm/Hz")


class _MsanDslSpecificMaxNomAtpDs_Type(Unsigned32):
    """Custom type msanDslSpecificMaxNomAtpDs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanDslSpecificMaxNomAtpDs_Type.__name__ = "Unsigned32"
_MsanDslSpecificMaxNomAtpDs_Object = MibTableColumn
msanDslSpecificMaxNomAtpDs = _MsanDslSpecificMaxNomAtpDs_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 3, 1, 29),
    _MsanDslSpecificMaxNomAtpDs_Type()
)
msanDslSpecificMaxNomAtpDs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDslSpecificMaxNomAtpDs.setStatus("current")
if mibBuilder.loadTexts:
    msanDslSpecificMaxNomAtpDs.setUnits("0.1 dBm")


class _MsanDslSpecificMaxNomAtpUs_Type(Unsigned32):
    """Custom type msanDslSpecificMaxNomAtpUs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanDslSpecificMaxNomAtpUs_Type.__name__ = "Unsigned32"
_MsanDslSpecificMaxNomAtpUs_Object = MibTableColumn
msanDslSpecificMaxNomAtpUs = _MsanDslSpecificMaxNomAtpUs_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 3, 1, 30),
    _MsanDslSpecificMaxNomAtpUs_Type()
)
msanDslSpecificMaxNomAtpUs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDslSpecificMaxNomAtpUs.setStatus("current")
if mibBuilder.loadTexts:
    msanDslSpecificMaxNomAtpUs.setUnits("0.1 dBm")


class _MsanDslSpecificMaxAggRxPwrUs_Type(Integer32):
    """Custom type msanDslSpecificMaxAggRxPwrUs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-255, 255),
    )


_MsanDslSpecificMaxAggRxPwrUs_Type.__name__ = "Integer32"
_MsanDslSpecificMaxAggRxPwrUs_Object = MibTableColumn
msanDslSpecificMaxAggRxPwrUs = _MsanDslSpecificMaxAggRxPwrUs_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 3, 1, 31),
    _MsanDslSpecificMaxAggRxPwrUs_Type()
)
msanDslSpecificMaxAggRxPwrUs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDslSpecificMaxAggRxPwrUs.setStatus("current")
if mibBuilder.loadTexts:
    msanDslSpecificMaxAggRxPwrUs.setUnits("0.1 dBm")


class _MsanDslSpecificClassMask_Type(Integer32):
    """Custom type msanDslSpecificClassMask based on Integer32"""
    defaultValue = 8

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
              16,
              17,
              18,
              19,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("b997E17_M2x_A", 21),
          ("b997_M1c_A_7", 13),
          ("b997_M1x_M", 15),
          ("b997_M1x_M_8", 14),
          ("b997_M2x_A", 17),
          ("b997_M2x_M", 18),
          ("b997_M2x_M_8", 16),
          ("b998ADE17_M2x_A", 11),
          ("b998ADE17_M2x_B", 12),
          ("b998ADE17_M2x_NUS0_M", 10),
          ("b998E17_M2x_NUS0", 8),
          ("b998E17_M2x_NUS0_M", 9),
          ("b998_M1x_A", 1),
          ("b998_M1x_B", 2),
          ("b998_M1x_NUS0", 3),
          ("b998_M2x_A", 4),
          ("b998_M2x_B", 6),
          ("b998_M2x_M", 5),
          ("b998_M2x_NUS0", 7),
          ("bHPE17_M1_NUS0", 19),
          ("bHPE30_M1_NUS0", 20))
    )


_MsanDslSpecificClassMask_Type.__name__ = "Integer32"
_MsanDslSpecificClassMask_Object = MibTableColumn
msanDslSpecificClassMask = _MsanDslSpecificClassMask_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 3, 1, 32),
    _MsanDslSpecificClassMask_Type()
)
msanDslSpecificClassMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDslSpecificClassMask.setStatus("current")


class _MsanDslSpecificDpboEsEL_Type(Unsigned32):
    """Custom type msanDslSpecificDpboEsEL based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 511),
    )


_MsanDslSpecificDpboEsEL_Type.__name__ = "Unsigned32"
_MsanDslSpecificDpboEsEL_Object = MibTableColumn
msanDslSpecificDpboEsEL = _MsanDslSpecificDpboEsEL_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 3, 1, 35),
    _MsanDslSpecificDpboEsEL_Type()
)
msanDslSpecificDpboEsEL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDslSpecificDpboEsEL.setStatus("current")
if mibBuilder.loadTexts:
    msanDslSpecificDpboEsEL.setUnits("0.5 dB")


class _MsanDslSpecificUpboKLF_Type(Integer32):
    """Custom type msanDslSpecificUpboKLF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("disableUpbo", 3),
          ("override", 2))
    )


_MsanDslSpecificUpboKLF_Type.__name__ = "Integer32"
_MsanDslSpecificUpboKLF_Object = MibTableColumn
msanDslSpecificUpboKLF = _MsanDslSpecificUpboKLF_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 3, 1, 36),
    _MsanDslSpecificUpboKLF_Type()
)
msanDslSpecificUpboKLF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDslSpecificUpboKLF.setStatus("current")


class _MsanDslSpecificUpboKL_Type(Unsigned32):
    """Custom type msanDslSpecificUpboKL based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1280),
    )


_MsanDslSpecificUpboKL_Type.__name__ = "Unsigned32"
_MsanDslSpecificUpboKL_Object = MibTableColumn
msanDslSpecificUpboKL = _MsanDslSpecificUpboKL_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 3, 1, 37),
    _MsanDslSpecificUpboKL_Type()
)
msanDslSpecificUpboKL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDslSpecificUpboKL.setStatus("current")
if mibBuilder.loadTexts:
    msanDslSpecificUpboKL.setUnits("0.1 dB")


class _MsanDslSpecificSelt_Type(Integer32):
    """Custom type msanDslSpecificSelt based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("force", 2),
          ("inhibit", 1))
    )


_MsanDslSpecificSelt_Type.__name__ = "Integer32"
_MsanDslSpecificSelt_Object = MibTableColumn
msanDslSpecificSelt = _MsanDslSpecificSelt_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 3, 1, 39),
    _MsanDslSpecificSelt_Type()
)
msanDslSpecificSelt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDslSpecificSelt.setStatus("current")


class _MsanDslSpecificSeltStatus_Type(Integer32):
    """Custom type msanDslSpecificSeltStatus based on Integer32"""
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
        *(("aborted", 6),
          ("adminUp", 9),
          ("cannotRun", 5),
          ("failed", 7),
          ("illegalMode", 8),
          ("inProgress", 3),
          ("noResources", 11),
          ("none", 1),
          ("success", 2),
          ("tableFull", 10),
          ("undefinedError", 12),
          ("unsupported", 4))
    )


_MsanDslSpecificSeltStatus_Type.__name__ = "Integer32"
_MsanDslSpecificSeltStatus_Object = MibTableColumn
msanDslSpecificSeltStatus = _MsanDslSpecificSeltStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 3, 1, 40),
    _MsanDslSpecificSeltStatus_Type()
)
msanDslSpecificSeltStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDslSpecificSeltStatus.setStatus("current")


class _MsanDslSpecificPhyRDs_Type(Integer32):
    """Custom type msanDslSpecificPhyRDs based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("disabled", 1),
          ("enabled", 2))
    )


_MsanDslSpecificPhyRDs_Type.__name__ = "Integer32"
_MsanDslSpecificPhyRDs_Object = MibTableColumn
msanDslSpecificPhyRDs = _MsanDslSpecificPhyRDs_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 3, 1, 41),
    _MsanDslSpecificPhyRDs_Type()
)
msanDslSpecificPhyRDs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDslSpecificPhyRDs.setStatus("current")


class _MsanDslSpecificPhyRUs_Type(Integer32):
    """Custom type msanDslSpecificPhyRUs based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("disabled", 1),
          ("enabled", 2))
    )


_MsanDslSpecificPhyRUs_Type.__name__ = "Integer32"
_MsanDslSpecificPhyRUs_Object = MibTableColumn
msanDslSpecificPhyRUs = _MsanDslSpecificPhyRUs_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 3, 1, 42),
    _MsanDslSpecificPhyRUs_Type()
)
msanDslSpecificPhyRUs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDslSpecificPhyRUs.setStatus("current")


class _MsanDslSpecificUpboUs1a_Type(Integer32):
    """Custom type msanDslSpecificUpboUs1a based on Integer32"""
    defaultValue = 4000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4000, 8095),
    )


_MsanDslSpecificUpboUs1a_Type.__name__ = "Integer32"
_MsanDslSpecificUpboUs1a_Object = MibTableColumn
msanDslSpecificUpboUs1a = _MsanDslSpecificUpboUs1a_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 3, 1, 43),
    _MsanDslSpecificUpboUs1a_Type()
)
msanDslSpecificUpboUs1a.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDslSpecificUpboUs1a.setStatus("current")
if mibBuilder.loadTexts:
    msanDslSpecificUpboUs1a.setUnits("0.01 dBm/Hz")


class _MsanDslSpecificUpboUs1b_Type(Integer32):
    """Custom type msanDslSpecificUpboUs1b based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MsanDslSpecificUpboUs1b_Type.__name__ = "Integer32"
_MsanDslSpecificUpboUs1b_Object = MibTableColumn
msanDslSpecificUpboUs1b = _MsanDslSpecificUpboUs1b_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 3, 1, 44),
    _MsanDslSpecificUpboUs1b_Type()
)
msanDslSpecificUpboUs1b.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDslSpecificUpboUs1b.setStatus("current")
if mibBuilder.loadTexts:
    msanDslSpecificUpboUs1b.setUnits("0.01 dBm/Hz")


class _MsanDslSpecificUpboUs2a_Type(Integer32):
    """Custom type msanDslSpecificUpboUs2a based on Integer32"""
    defaultValue = 4000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4000, 8095),
    )


_MsanDslSpecificUpboUs2a_Type.__name__ = "Integer32"
_MsanDslSpecificUpboUs2a_Object = MibTableColumn
msanDslSpecificUpboUs2a = _MsanDslSpecificUpboUs2a_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 3, 1, 45),
    _MsanDslSpecificUpboUs2a_Type()
)
msanDslSpecificUpboUs2a.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDslSpecificUpboUs2a.setStatus("current")
if mibBuilder.loadTexts:
    msanDslSpecificUpboUs2a.setUnits("0.01 dBm/Hz")


class _MsanDslSpecificUpboUs2b_Type(Integer32):
    """Custom type msanDslSpecificUpboUs2b based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MsanDslSpecificUpboUs2b_Type.__name__ = "Integer32"
_MsanDslSpecificUpboUs2b_Object = MibTableColumn
msanDslSpecificUpboUs2b = _MsanDslSpecificUpboUs2b_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 3, 1, 46),
    _MsanDslSpecificUpboUs2b_Type()
)
msanDslSpecificUpboUs2b.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDslSpecificUpboUs2b.setStatus("current")
if mibBuilder.loadTexts:
    msanDslSpecificUpboUs2b.setUnits("0.01 dBm/Hz")


class _MsanDslSpecificUpboUs3a_Type(Integer32):
    """Custom type msanDslSpecificUpboUs3a based on Integer32"""
    defaultValue = 4000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4000, 8095),
    )


_MsanDslSpecificUpboUs3a_Type.__name__ = "Integer32"
_MsanDslSpecificUpboUs3a_Object = MibTableColumn
msanDslSpecificUpboUs3a = _MsanDslSpecificUpboUs3a_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 3, 1, 47),
    _MsanDslSpecificUpboUs3a_Type()
)
msanDslSpecificUpboUs3a.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDslSpecificUpboUs3a.setStatus("current")
if mibBuilder.loadTexts:
    msanDslSpecificUpboUs3a.setUnits("0.01 dBm/Hz")


class _MsanDslSpecificUpboUs3b_Type(Integer32):
    """Custom type msanDslSpecificUpboUs3b based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MsanDslSpecificUpboUs3b_Type.__name__ = "Integer32"
_MsanDslSpecificUpboUs3b_Object = MibTableColumn
msanDslSpecificUpboUs3b = _MsanDslSpecificUpboUs3b_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 3, 1, 48),
    _MsanDslSpecificUpboUs3b_Type()
)
msanDslSpecificUpboUs3b.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDslSpecificUpboUs3b.setStatus("current")
if mibBuilder.loadTexts:
    msanDslSpecificUpboUs3b.setUnits("0.01 dBm/Hz")


class _MsanDslSpecificUpboUs4a_Type(Integer32):
    """Custom type msanDslSpecificUpboUs4a based on Integer32"""
    defaultValue = 4000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4000, 8095),
    )


_MsanDslSpecificUpboUs4a_Type.__name__ = "Integer32"
_MsanDslSpecificUpboUs4a_Object = MibTableColumn
msanDslSpecificUpboUs4a = _MsanDslSpecificUpboUs4a_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 3, 1, 49),
    _MsanDslSpecificUpboUs4a_Type()
)
msanDslSpecificUpboUs4a.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDslSpecificUpboUs4a.setStatus("current")
if mibBuilder.loadTexts:
    msanDslSpecificUpboUs4a.setUnits("0.01 dBm/Hz")


class _MsanDslSpecificUpboUs4b_Type(Integer32):
    """Custom type msanDslSpecificUpboUs4b based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MsanDslSpecificUpboUs4b_Type.__name__ = "Integer32"
_MsanDslSpecificUpboUs4b_Object = MibTableColumn
msanDslSpecificUpboUs4b = _MsanDslSpecificUpboUs4b_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 3, 1, 50),
    _MsanDslSpecificUpboUs4b_Type()
)
msanDslSpecificUpboUs4b.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDslSpecificUpboUs4b.setStatus("current")
if mibBuilder.loadTexts:
    msanDslSpecificUpboUs4b.setUnits("0.01 dBm/Hz")
_MsanDslSpecificDpboEPsdMask_Type = OctetString
_MsanDslSpecificDpboEPsdMask_Object = MibTableColumn
msanDslSpecificDpboEPsdMask = _MsanDslSpecificDpboEPsdMask_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 3, 1, 51),
    _MsanDslSpecificDpboEPsdMask_Type()
)
msanDslSpecificDpboEPsdMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDslSpecificDpboEPsdMask.setStatus("current")


class _MsanDslSpecificDpboEsCmA_Type(Unsigned32):
    """Custom type msanDslSpecificDpboEsCmA based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 640),
    )


_MsanDslSpecificDpboEsCmA_Type.__name__ = "Unsigned32"
_MsanDslSpecificDpboEsCmA_Object = MibTableColumn
msanDslSpecificDpboEsCmA = _MsanDslSpecificDpboEsCmA_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 3, 1, 52),
    _MsanDslSpecificDpboEsCmA_Type()
)
msanDslSpecificDpboEsCmA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanDslSpecificDpboEsCmA.setStatus("current")
if mibBuilder.loadTexts:
    msanDslSpecificDpboEsCmA.setUnits("2^-8")


class _MsanDslSpecificDpboEsCmB_Type(Unsigned32):
    """Custom type msanDslSpecificDpboEsCmB based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 640),
    )


_MsanDslSpecificDpboEsCmB_Type.__name__ = "Unsigned32"
_MsanDslSpecificDpboEsCmB_Object = MibTableColumn
msanDslSpecificDpboEsCmB = _MsanDslSpecificDpboEsCmB_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 3, 1, 53),
    _MsanDslSpecificDpboEsCmB_Type()
)
msanDslSpecificDpboEsCmB.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanDslSpecificDpboEsCmB.setStatus("current")
if mibBuilder.loadTexts:
    msanDslSpecificDpboEsCmB.setUnits("2^-8")


class _MsanDslSpecificDpboEsCmC_Type(Unsigned32):
    """Custom type msanDslSpecificDpboEsCmC based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 640),
    )


_MsanDslSpecificDpboEsCmC_Type.__name__ = "Unsigned32"
_MsanDslSpecificDpboEsCmC_Object = MibTableColumn
msanDslSpecificDpboEsCmC = _MsanDslSpecificDpboEsCmC_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 3, 1, 54),
    _MsanDslSpecificDpboEsCmC_Type()
)
msanDslSpecificDpboEsCmC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanDslSpecificDpboEsCmC.setStatus("current")
if mibBuilder.loadTexts:
    msanDslSpecificDpboEsCmC.setUnits("2^-8")


class _MsanDslSpecificDpboMus_Type(Unsigned32):
    """Custom type msanDslSpecificDpboMus based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanDslSpecificDpboMus_Type.__name__ = "Unsigned32"
_MsanDslSpecificDpboMus_Object = MibTableColumn
msanDslSpecificDpboMus = _MsanDslSpecificDpboMus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 3, 1, 55),
    _MsanDslSpecificDpboMus_Type()
)
msanDslSpecificDpboMus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanDslSpecificDpboMus.setStatus("current")
if mibBuilder.loadTexts:
    msanDslSpecificDpboMus.setUnits("0.5 dBm/Hz")


class _MsanDslSpecificDpboFMin_Type(Unsigned32):
    """Custom type msanDslSpecificDpboFMin based on Unsigned32"""
    defaultValue = 32

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_MsanDslSpecificDpboFMin_Type.__name__ = "Unsigned32"
_MsanDslSpecificDpboFMin_Object = MibTableColumn
msanDslSpecificDpboFMin = _MsanDslSpecificDpboFMin_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 3, 1, 56),
    _MsanDslSpecificDpboFMin_Type()
)
msanDslSpecificDpboFMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanDslSpecificDpboFMin.setStatus("current")
if mibBuilder.loadTexts:
    msanDslSpecificDpboFMin.setUnits("4.3125 kHz")


class _MsanDslSpecificDpboFMax_Type(Unsigned32):
    """Custom type msanDslSpecificDpboFMax based on Unsigned32"""
    defaultValue = 512

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 6956),
    )


_MsanDslSpecificDpboFMax_Type.__name__ = "Unsigned32"
_MsanDslSpecificDpboFMax_Object = MibTableColumn
msanDslSpecificDpboFMax = _MsanDslSpecificDpboFMax_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 3, 1, 57),
    _MsanDslSpecificDpboFMax_Type()
)
msanDslSpecificDpboFMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanDslSpecificDpboFMax.setStatus("current")
if mibBuilder.loadTexts:
    msanDslSpecificDpboFMax.setUnits("4.3125 kHz")
_MsanDslPsdMaskDsTable_Object = MibTable
msanDslPsdMaskDsTable = _MsanDslPsdMaskDsTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 4)
)
if mibBuilder.loadTexts:
    msanDslPsdMaskDsTable.setStatus("current")
_MsanDslPsdMaskDsEntry_Object = MibTableRow
msanDslPsdMaskDsEntry = _MsanDslPsdMaskDsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 4, 1)
)
msanDslPsdMaskDsEntry.setIndexNames(
    (0, "ISKRATEL-MSAN-MIB", "msanDslPsdMaskDsName"),
)
if mibBuilder.loadTexts:
    msanDslPsdMaskDsEntry.setStatus("current")


class _MsanDslPsdMaskDsName_Type(OctetString):
    """Custom type msanDslPsdMaskDsName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MsanDslPsdMaskDsName_Type.__name__ = "OctetString"
_MsanDslPsdMaskDsName_Object = MibTableColumn
msanDslPsdMaskDsName = _MsanDslPsdMaskDsName_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 4, 1, 1),
    _MsanDslPsdMaskDsName_Type()
)
msanDslPsdMaskDsName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanDslPsdMaskDsName.setStatus("current")


class _MsanDslPsdMaskDsType_Type(Integer32):
    """Custom type msanDslPsdMaskDsType based on Integer32"""

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("configured", 2),
          ("default", 1))
    )


_MsanDslPsdMaskDsType_Type.__name__ = "Integer32"
_MsanDslPsdMaskDsType_Object = MibTableColumn
msanDslPsdMaskDsType = _MsanDslPsdMaskDsType_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 4, 1, 2),
    _MsanDslPsdMaskDsType_Type()
)
msanDslPsdMaskDsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDslPsdMaskDsType.setStatus("current")


class _MsanDslPsdMaskDsShape_Type(Xdsl2PsdMaskDs):
    """Custom type msanDslPsdMaskDsShape based on Xdsl2PsdMaskDs"""
    defaultHexValue = "0"


_MsanDslPsdMaskDsShape_Object = MibTableColumn
msanDslPsdMaskDsShape = _MsanDslPsdMaskDsShape_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 4, 1, 3),
    _MsanDslPsdMaskDsShape_Type()
)
msanDslPsdMaskDsShape.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDslPsdMaskDsShape.setStatus("current")
_MsanDslPsdMaskDsRowStatus_Type = RowStatus
_MsanDslPsdMaskDsRowStatus_Object = MibTableColumn
msanDslPsdMaskDsRowStatus = _MsanDslPsdMaskDsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 4, 1, 4),
    _MsanDslPsdMaskDsRowStatus_Type()
)
msanDslPsdMaskDsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanDslPsdMaskDsRowStatus.setStatus("current")
_MsanDslPsdMaskUsTable_Object = MibTable
msanDslPsdMaskUsTable = _MsanDslPsdMaskUsTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 5)
)
if mibBuilder.loadTexts:
    msanDslPsdMaskUsTable.setStatus("current")
_MsanDslPsdMaskUsEntry_Object = MibTableRow
msanDslPsdMaskUsEntry = _MsanDslPsdMaskUsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 5, 1)
)
msanDslPsdMaskUsEntry.setIndexNames(
    (0, "ISKRATEL-MSAN-MIB", "msanDslPsdMaskUsName"),
)
if mibBuilder.loadTexts:
    msanDslPsdMaskUsEntry.setStatus("current")


class _MsanDslPsdMaskUsName_Type(OctetString):
    """Custom type msanDslPsdMaskUsName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MsanDslPsdMaskUsName_Type.__name__ = "OctetString"
_MsanDslPsdMaskUsName_Object = MibTableColumn
msanDslPsdMaskUsName = _MsanDslPsdMaskUsName_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 5, 1, 1),
    _MsanDslPsdMaskUsName_Type()
)
msanDslPsdMaskUsName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanDslPsdMaskUsName.setStatus("current")


class _MsanDslPsdMaskUsType_Type(Integer32):
    """Custom type msanDslPsdMaskUsType based on Integer32"""

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("configured", 2),
          ("default", 1))
    )


_MsanDslPsdMaskUsType_Type.__name__ = "Integer32"
_MsanDslPsdMaskUsType_Object = MibTableColumn
msanDslPsdMaskUsType = _MsanDslPsdMaskUsType_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 5, 1, 2),
    _MsanDslPsdMaskUsType_Type()
)
msanDslPsdMaskUsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDslPsdMaskUsType.setStatus("current")


class _MsanDslPsdMaskUsShape_Type(Xdsl2PsdMaskUs):
    """Custom type msanDslPsdMaskUsShape based on Xdsl2PsdMaskUs"""
    defaultHexValue = "0"


_MsanDslPsdMaskUsShape_Object = MibTableColumn
msanDslPsdMaskUsShape = _MsanDslPsdMaskUsShape_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 5, 1, 3),
    _MsanDslPsdMaskUsShape_Type()
)
msanDslPsdMaskUsShape.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDslPsdMaskUsShape.setStatus("current")
_MsanDslPsdMaskUsRowStatus_Type = RowStatus
_MsanDslPsdMaskUsRowStatus_Object = MibTableColumn
msanDslPsdMaskUsRowStatus = _MsanDslPsdMaskUsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 5, 1, 4),
    _MsanDslPsdMaskUsRowStatus_Type()
)
msanDslPsdMaskUsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanDslPsdMaskUsRowStatus.setStatus("current")
_MsanDslSeltStatusTable_Object = MibTable
msanDslSeltStatusTable = _MsanDslSeltStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 6)
)
if mibBuilder.loadTexts:
    msanDslSeltStatusTable.setStatus("current")
_MsanDslSeltStatusEntry_Object = MibTableRow
msanDslSeltStatusEntry = _MsanDslSeltStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 6, 1)
)
msanDslSeltStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    msanDslSeltStatusEntry.setStatus("current")


class _MsanDslSeltStatusNoiseType_Type(OctetString):
    """Custom type msanDslSeltStatusNoiseType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_MsanDslSeltStatusNoiseType_Type.__name__ = "OctetString"
_MsanDslSeltStatusNoiseType_Object = MibTableColumn
msanDslSeltStatusNoiseType = _MsanDslSeltStatusNoiseType_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 6, 1, 1),
    _MsanDslSeltStatusNoiseType_Type()
)
msanDslSeltStatusNoiseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDslSeltStatusNoiseType.setStatus("current")
_MsanDslSeltStatusNoiseMrgDs_Type = Integer32
_MsanDslSeltStatusNoiseMrgDs_Object = MibTableColumn
msanDslSeltStatusNoiseMrgDs = _MsanDslSeltStatusNoiseMrgDs_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 6, 1, 2),
    _MsanDslSeltStatusNoiseMrgDs_Type()
)
msanDslSeltStatusNoiseMrgDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDslSeltStatusNoiseMrgDs.setStatus("current")
if mibBuilder.loadTexts:
    msanDslSeltStatusNoiseMrgDs.setUnits("0.1 dB")
_MsanDslSeltStatusNoiseMrgUs_Type = Integer32
_MsanDslSeltStatusNoiseMrgUs_Object = MibTableColumn
msanDslSeltStatusNoiseMrgUs = _MsanDslSeltStatusNoiseMrgUs_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 6, 1, 3),
    _MsanDslSeltStatusNoiseMrgUs_Type()
)
msanDslSeltStatusNoiseMrgUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDslSeltStatusNoiseMrgUs.setStatus("current")
if mibBuilder.loadTexts:
    msanDslSeltStatusNoiseMrgUs.setUnits("0.1 dB")
_MsanDslSeltStatusNumTonesDs_Type = Integer32
_MsanDslSeltStatusNumTonesDs_Object = MibTableColumn
msanDslSeltStatusNumTonesDs = _MsanDslSeltStatusNumTonesDs_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 6, 1, 4),
    _MsanDslSeltStatusNumTonesDs_Type()
)
msanDslSeltStatusNumTonesDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDslSeltStatusNumTonesDs.setStatus("current")
_MsanDslSeltStatusNumTonesUs_Type = Integer32
_MsanDslSeltStatusNumTonesUs_Object = MibTableColumn
msanDslSeltStatusNumTonesUs = _MsanDslSeltStatusNumTonesUs_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 6, 1, 5),
    _MsanDslSeltStatusNumTonesUs_Type()
)
msanDslSeltStatusNumTonesUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDslSeltStatusNumTonesUs.setStatus("current")
_MsanDslSeltStatusMaxRateDs_Type = Integer32
_MsanDslSeltStatusMaxRateDs_Object = MibTableColumn
msanDslSeltStatusMaxRateDs = _MsanDslSeltStatusMaxRateDs_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 6, 1, 6),
    _MsanDslSeltStatusMaxRateDs_Type()
)
msanDslSeltStatusMaxRateDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDslSeltStatusMaxRateDs.setStatus("current")
if mibBuilder.loadTexts:
    msanDslSeltStatusMaxRateDs.setUnits("kbps")
_MsanDslSeltStatusMaxRateUs_Type = Integer32
_MsanDslSeltStatusMaxRateUs_Object = MibTableColumn
msanDslSeltStatusMaxRateUs = _MsanDslSeltStatusMaxRateUs_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 6, 1, 7),
    _MsanDslSeltStatusMaxRateUs_Type()
)
msanDslSeltStatusMaxRateUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDslSeltStatusMaxRateUs.setStatus("current")
if mibBuilder.loadTexts:
    msanDslSeltStatusMaxRateUs.setUnits("kbps")


class _MsanDslSeltStatusCableType_Type(OctetString):
    """Custom type msanDslSeltStatusCableType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_MsanDslSeltStatusCableType_Type.__name__ = "OctetString"
_MsanDslSeltStatusCableType_Object = MibTableColumn
msanDslSeltStatusCableType = _MsanDslSeltStatusCableType_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 6, 1, 8),
    _MsanDslSeltStatusCableType_Type()
)
msanDslSeltStatusCableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDslSeltStatusCableType.setStatus("current")
_MsanDslSeltStatusCableLenght_Type = Integer32
_MsanDslSeltStatusCableLenght_Object = MibTableColumn
msanDslSeltStatusCableLenght = _MsanDslSeltStatusCableLenght_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 6, 1, 9),
    _MsanDslSeltStatusCableLenght_Type()
)
msanDslSeltStatusCableLenght.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDslSeltStatusCableLenght.setStatus("current")
if mibBuilder.loadTexts:
    msanDslSeltStatusCableLenght.setUnits("m")
_MsanDslSeltStatusFitError_Type = Integer32
_MsanDslSeltStatusFitError_Object = MibTableColumn
msanDslSeltStatusFitError = _MsanDslSeltStatusFitError_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 6, 1, 10),
    _MsanDslSeltStatusFitError_Type()
)
msanDslSeltStatusFitError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDslSeltStatusFitError.setStatus("current")
if mibBuilder.loadTexts:
    msanDslSeltStatusFitError.setUnits("%")


class _MsanDslSeltStatusLoopTermination_Type(Integer32):
    """Custom type msanDslSeltStatusLoopTermination based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("open", 2),
          ("short", 3),
          ("unknown", 1))
    )


_MsanDslSeltStatusLoopTermination_Type.__name__ = "Integer32"
_MsanDslSeltStatusLoopTermination_Object = MibTableColumn
msanDslSeltStatusLoopTermination = _MsanDslSeltStatusLoopTermination_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 19, 6, 1, 11),
    _MsanDslSeltStatusLoopTermination_Type()
)
msanDslSeltStatusLoopTermination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanDslSeltStatusLoopTermination.setStatus("current")
_MsanPortMirroring_ObjectIdentity = ObjectIdentity
msanPortMirroring = _MsanPortMirroring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 20)
)
_MsanPortMirroringGlobal_ObjectIdentity = ObjectIdentity
msanPortMirroringGlobal = _MsanPortMirroringGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 20, 1)
)
_MsanPortMirroringTable_Object = MibTable
msanPortMirroringTable = _MsanPortMirroringTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 20, 2)
)
if mibBuilder.loadTexts:
    msanPortMirroringTable.setStatus("current")
_MsanPortMirroringEntry_Object = MibTableRow
msanPortMirroringEntry = _MsanPortMirroringEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 20, 2, 1)
)
msanPortMirroringEntry.setIndexNames(
    (0, "ISKRATEL-MSAN-MIB", "msanPortMirroringSessionId"),
)
if mibBuilder.loadTexts:
    msanPortMirroringEntry.setStatus("current")
_MsanPortMirroringSessionId_Type = Integer32
_MsanPortMirroringSessionId_Object = MibTableColumn
msanPortMirroringSessionId = _MsanPortMirroringSessionId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 20, 2, 1, 1),
    _MsanPortMirroringSessionId_Type()
)
msanPortMirroringSessionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanPortMirroringSessionId.setStatus("current")


class _MsanPortMirroringAdminState_Type(Integer32):
    """Custom type msanPortMirroringAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_MsanPortMirroringAdminState_Type.__name__ = "Integer32"
_MsanPortMirroringAdminState_Object = MibTableColumn
msanPortMirroringAdminState = _MsanPortMirroringAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 20, 2, 1, 2),
    _MsanPortMirroringAdminState_Type()
)
msanPortMirroringAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanPortMirroringAdminState.setStatus("current")
_MsanPortMirroringDestPort_Type = Integer32
_MsanPortMirroringDestPort_Object = MibTableColumn
msanPortMirroringDestPort = _MsanPortMirroringDestPort_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 20, 2, 1, 3),
    _MsanPortMirroringDestPort_Type()
)
msanPortMirroringDestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanPortMirroringDestPort.setStatus("current")
_MsanPortMirroringMemberTable_Object = MibTable
msanPortMirroringMemberTable = _MsanPortMirroringMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 20, 3)
)
if mibBuilder.loadTexts:
    msanPortMirroringMemberTable.setStatus("current")
_MsanPortMirroringMemberEntry_Object = MibTableRow
msanPortMirroringMemberEntry = _MsanPortMirroringMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 20, 3, 1)
)
msanPortMirroringMemberEntry.setIndexNames(
    (0, "ISKRATEL-MSAN-MIB", "msanPortMirroringSessionId"),
    (0, "ISKRATEL-MSAN-MIB", "msanPortMirroringMemberSrcPort"),
)
if mibBuilder.loadTexts:
    msanPortMirroringMemberEntry.setStatus("current")
_MsanPortMirroringMemberSrcPort_Type = Integer32
_MsanPortMirroringMemberSrcPort_Object = MibTableColumn
msanPortMirroringMemberSrcPort = _MsanPortMirroringMemberSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 20, 3, 1, 1),
    _MsanPortMirroringMemberSrcPort_Type()
)
msanPortMirroringMemberSrcPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanPortMirroringMemberSrcPort.setStatus("current")


class _MsanPortMirroringMemberDirection_Type(Integer32):
    """Custom type msanPortMirroringMemberDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rx", 2),
          ("tx", 1),
          ("txAndRx", 3))
    )


_MsanPortMirroringMemberDirection_Type.__name__ = "Integer32"
_MsanPortMirroringMemberDirection_Object = MibTableColumn
msanPortMirroringMemberDirection = _MsanPortMirroringMemberDirection_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 20, 3, 1, 2),
    _MsanPortMirroringMemberDirection_Type()
)
msanPortMirroringMemberDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanPortMirroringMemberDirection.setStatus("current")
_MsanPortMirroringMemberRowStatus_Type = RowStatus
_MsanPortMirroringMemberRowStatus_Object = MibTableColumn
msanPortMirroringMemberRowStatus = _MsanPortMirroringMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 20, 3, 1, 3),
    _MsanPortMirroringMemberRowStatus_Type()
)
msanPortMirroringMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanPortMirroringMemberRowStatus.setStatus("current")
_MsanResetWithDelay_ObjectIdentity = ObjectIdentity
msanResetWithDelay = _MsanResetWithDelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 21)
)
_MsanResetWithDelayGlobal_ObjectIdentity = ObjectIdentity
msanResetWithDelayGlobal = _MsanResetWithDelayGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 21, 1)
)


class _MsanResetDelay_Type(Integer32):
    """Custom type msanResetDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_MsanResetDelay_Type.__name__ = "Integer32"
_MsanResetDelay_Object = MibScalar
msanResetDelay = _MsanResetDelay_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 21, 1, 1),
    _MsanResetDelay_Type()
)
msanResetDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanResetDelay.setStatus("current")
if mibBuilder.loadTexts:
    msanResetDelay.setUnits("seconds")
_MsanMacTable_ObjectIdentity = ObjectIdentity
msanMacTable = _MsanMacTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 22)
)
_MsanMacTableGlobal_ObjectIdentity = ObjectIdentity
msanMacTableGlobal = _MsanMacTableGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 22, 1)
)
_MsanMacTableLength_Type = Unsigned32
_MsanMacTableLength_Object = MibScalar
msanMacTableLength = _MsanMacTableLength_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 22, 1, 1),
    _MsanMacTableLength_Type()
)
msanMacTableLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanMacTableLength.setStatus("current")
_MsanMacTableUsed_Type = Unsigned32
_MsanMacTableUsed_Object = MibScalar
msanMacTableUsed = _MsanMacTableUsed_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 22, 1, 2),
    _MsanMacTableUsed_Type()
)
msanMacTableUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanMacTableUsed.setStatus("current")
_MsanMacTableCAMTable_Object = MibTable
msanMacTableCAMTable = _MsanMacTableCAMTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 22, 2)
)
if mibBuilder.loadTexts:
    msanMacTableCAMTable.setStatus("current")
_MsanMacTableCAMEntry_Object = MibTableRow
msanMacTableCAMEntry = _MsanMacTableCAMEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 22, 2, 1)
)
msanMacTableCAMEntry.setIndexNames(
    (0, "ISKRATEL-MSAN-MIB", "msanMacTableCAMIndex"),
)
if mibBuilder.loadTexts:
    msanMacTableCAMEntry.setStatus("current")
_MsanMacTableCAMIndex_Type = Integer32
_MsanMacTableCAMIndex_Object = MibTableColumn
msanMacTableCAMIndex = _MsanMacTableCAMIndex_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 22, 2, 1, 1),
    _MsanMacTableCAMIndex_Type()
)
msanMacTableCAMIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanMacTableCAMIndex.setStatus("current")
_MsanMacTableMacAddress_Type = MacAddress
_MsanMacTableMacAddress_Object = MibTableColumn
msanMacTableMacAddress = _MsanMacTableMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 22, 2, 1, 2),
    _MsanMacTableMacAddress_Type()
)
msanMacTableMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanMacTableMacAddress.setStatus("current")
_MsanMacTablePort_Type = Integer32
_MsanMacTablePort_Object = MibTableColumn
msanMacTablePort = _MsanMacTablePort_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 22, 2, 1, 3),
    _MsanMacTablePort_Type()
)
msanMacTablePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanMacTablePort.setStatus("current")
_MsanMacTableVLAN_Type = Integer32
_MsanMacTableVLAN_Object = MibTableColumn
msanMacTableVLAN = _MsanMacTableVLAN_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 22, 2, 1, 4),
    _MsanMacTableVLAN_Type()
)
msanMacTableVLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanMacTableVLAN.setStatus("current")


class _MsanMacTableType_Type(Integer32):
    """Custom type msanMacTableType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("learned", 1),
          ("managment", 2),
          ("static", 3))
    )


_MsanMacTableType_Type.__name__ = "Integer32"
_MsanMacTableType_Object = MibTableColumn
msanMacTableType = _MsanMacTableType_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 22, 2, 1, 5),
    _MsanMacTableType_Type()
)
msanMacTableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanMacTableType.setStatus("current")
_MsanAcs_ObjectIdentity = ObjectIdentity
msanAcs = _MsanAcs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 23)
)
_MsanAcsGlobal_ObjectIdentity = ObjectIdentity
msanAcsGlobal = _MsanAcsGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 23, 1)
)
_MsanAcsServerUrl_Type = OctetString
_MsanAcsServerUrl_Object = MibScalar
msanAcsServerUrl = _MsanAcsServerUrl_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 23, 1, 1),
    _MsanAcsServerUrl_Type()
)
msanAcsServerUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanAcsServerUrl.setStatus("current")
_MsanPrimaryDnsIpAddress_Type = IpAddress
_MsanPrimaryDnsIpAddress_Object = MibScalar
msanPrimaryDnsIpAddress = _MsanPrimaryDnsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 23, 1, 2),
    _MsanPrimaryDnsIpAddress_Type()
)
msanPrimaryDnsIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanPrimaryDnsIpAddress.setStatus("current")
_MsanSecondaryDnsIpAddress_Type = IpAddress
_MsanSecondaryDnsIpAddress_Object = MibScalar
msanSecondaryDnsIpAddress = _MsanSecondaryDnsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 23, 1, 3),
    _MsanSecondaryDnsIpAddress_Type()
)
msanSecondaryDnsIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanSecondaryDnsIpAddress.setStatus("current")
_MsanAcsDomainName_Type = OctetString
_MsanAcsDomainName_Object = MibScalar
msanAcsDomainName = _MsanAcsDomainName_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 23, 1, 4),
    _MsanAcsDomainName_Type()
)
msanAcsDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanAcsDomainName.setStatus("current")


class _MsanAcsClientStatus_Type(Integer32):
    """Custom type msanAcsClientStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanAcsClientStatus_Type.__name__ = "Integer32"
_MsanAcsClientStatus_Object = MibScalar
msanAcsClientStatus = _MsanAcsClientStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 23, 1, 5),
    _MsanAcsClientStatus_Type()
)
msanAcsClientStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanAcsClientStatus.setStatus("current")


class _MsanAcsBackupConf_Type(Integer32):
    """Custom type msanAcsBackupConf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanAcsBackupConf_Type.__name__ = "Integer32"
_MsanAcsBackupConf_Object = MibScalar
msanAcsBackupConf = _MsanAcsBackupConf_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 23, 1, 6),
    _MsanAcsBackupConf_Type()
)
msanAcsBackupConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanAcsBackupConf.setStatus("current")
_MsanStp_ObjectIdentity = ObjectIdentity
msanStp = _MsanStp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 24)
)
_MsanStpGlobal_ObjectIdentity = ObjectIdentity
msanStpGlobal = _MsanStpGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 24, 1)
)
_MsanStpBpduFilterTable_Object = MibTable
msanStpBpduFilterTable = _MsanStpBpduFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 24, 2)
)
if mibBuilder.loadTexts:
    msanStpBpduFilterTable.setStatus("current")
_MsanStpBpduFilterEntry_Object = MibTableRow
msanStpBpduFilterEntry = _MsanStpBpduFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 24, 2, 1)
)
msanStpBpduFilterEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    msanStpBpduFilterEntry.setStatus("current")


class _MsanStpBpduFilter_Type(Integer32):
    """Custom type msanStpBpduFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_MsanStpBpduFilter_Type.__name__ = "Integer32"
_MsanStpBpduFilter_Object = MibTableColumn
msanStpBpduFilter = _MsanStpBpduFilter_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 24, 2, 1, 1),
    _MsanStpBpduFilter_Type()
)
msanStpBpduFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanStpBpduFilter.setStatus("current")
_MsanStpSwitchConfigGroup_ObjectIdentity = ObjectIdentity
msanStpSwitchConfigGroup = _MsanStpSwitchConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 24, 3)
)


class _MsanStpCstBridgePriority_Type(Unsigned32):
    """Custom type msanStpCstBridgePriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_MsanStpCstBridgePriority_Type.__name__ = "Unsigned32"
_MsanStpCstBridgePriority_Object = MibScalar
msanStpCstBridgePriority = _MsanStpCstBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 24, 3, 1),
    _MsanStpCstBridgePriority_Type()
)
msanStpCstBridgePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanStpCstBridgePriority.setStatus("current")
_MsanStpMstTable_Object = MibTable
msanStpMstTable = _MsanStpMstTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 24, 4)
)
if mibBuilder.loadTexts:
    msanStpMstTable.setStatus("current")
_MsanStpMstEntry_Object = MibTableRow
msanStpMstEntry = _MsanStpMstEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 24, 4, 1)
)
msanStpMstEntry.setIndexNames(
    (0, "ISKRATEL-MSAN-MIB", "msanStpMstId"),
)
if mibBuilder.loadTexts:
    msanStpMstEntry.setStatus("current")
_MsanStpMstId_Type = Unsigned32
_MsanStpMstId_Object = MibTableColumn
msanStpMstId = _MsanStpMstId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 24, 4, 1, 1),
    _MsanStpMstId_Type()
)
msanStpMstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanStpMstId.setStatus("current")


class _MsanStpMstBridgePriority_Type(Unsigned32):
    """Custom type msanStpMstBridgePriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_MsanStpMstBridgePriority_Type.__name__ = "Unsigned32"
_MsanStpMstBridgePriority_Object = MibTableColumn
msanStpMstBridgePriority = _MsanStpMstBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 24, 4, 1, 2),
    _MsanStpMstBridgePriority_Type()
)
msanStpMstBridgePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanStpMstBridgePriority.setStatus("current")
_MsanStpMstRowStatus_Type = RowStatus
_MsanStpMstRowStatus_Object = MibTableColumn
msanStpMstRowStatus = _MsanStpMstRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 24, 4, 1, 3),
    _MsanStpMstRowStatus_Type()
)
msanStpMstRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanStpMstRowStatus.setStatus("current")
_MsanStpMstVlanTable_Object = MibTable
msanStpMstVlanTable = _MsanStpMstVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 24, 5)
)
if mibBuilder.loadTexts:
    msanStpMstVlanTable.setStatus("current")
_MsanStpMstVlanEntry_Object = MibTableRow
msanStpMstVlanEntry = _MsanStpMstVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 24, 5, 1)
)
msanStpMstVlanEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
    (0, "ISKRATEL-MSAN-MIB", "msanStpMstId"),
)
if mibBuilder.loadTexts:
    msanStpMstVlanEntry.setStatus("current")
_MsanStpMstVlanRowStatus_Type = RowStatus
_MsanStpMstVlanRowStatus_Object = MibTableColumn
msanStpMstVlanRowStatus = _MsanStpMstVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 24, 5, 1, 1),
    _MsanStpMstVlanRowStatus_Type()
)
msanStpMstVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanStpMstVlanRowStatus.setStatus("current")
_MsanStpMstPortTable_Object = MibTable
msanStpMstPortTable = _MsanStpMstPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 24, 6)
)
if mibBuilder.loadTexts:
    msanStpMstPortTable.setStatus("current")
_MsanStpMstPortEntry_Object = MibTableRow
msanStpMstPortEntry = _MsanStpMstPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 24, 6, 1)
)
msanStpMstPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ISKRATEL-MSAN-MIB", "msanStpMstId"),
)
if mibBuilder.loadTexts:
    msanStpMstPortEntry.setStatus("current")


class _MsanStpMstPortPathCost_Type(Unsigned32):
    """Custom type msanStpMstPortPathCost based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_MsanStpMstPortPathCost_Type.__name__ = "Unsigned32"
_MsanStpMstPortPathCost_Object = MibTableColumn
msanStpMstPortPathCost = _MsanStpMstPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 24, 6, 1, 1),
    _MsanStpMstPortPathCost_Type()
)
msanStpMstPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanStpMstPortPathCost.setStatus("current")


class _MsanStpMstPortPriority_Type(Unsigned32):
    """Custom type msanStpMstPortPriority based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_MsanStpMstPortPriority_Type.__name__ = "Unsigned32"
_MsanStpMstPortPriority_Object = MibTableColumn
msanStpMstPortPriority = _MsanStpMstPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 24, 6, 1, 2),
    _MsanStpMstPortPriority_Type()
)
msanStpMstPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanStpMstPortPriority.setStatus("current")
_MsanStpPortTable_Object = MibTable
msanStpPortTable = _MsanStpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 24, 7)
)
if mibBuilder.loadTexts:
    msanStpPortTable.setStatus("current")
_MsanStpPortEntry_Object = MibTableRow
msanStpPortEntry = _MsanStpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 24, 7, 1)
)
msanStpPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    msanStpPortEntry.setStatus("current")


class _MsanStpPortHelloTime_Type(Integer32):
    """Custom type msanStpPortHelloTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_MsanStpPortHelloTime_Type.__name__ = "Integer32"
_MsanStpPortHelloTime_Object = MibTableColumn
msanStpPortHelloTime = _MsanStpPortHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 24, 7, 1, 1),
    _MsanStpPortHelloTime_Type()
)
msanStpPortHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanStpPortHelloTime.setStatus("current")
_MsanStpCstPortTable_Object = MibTable
msanStpCstPortTable = _MsanStpCstPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 24, 8)
)
if mibBuilder.loadTexts:
    msanStpCstPortTable.setStatus("current")
_MsanStpCstPortEntry_Object = MibTableRow
msanStpCstPortEntry = _MsanStpCstPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 24, 8, 1)
)
msanStpCstPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    msanStpCstPortEntry.setStatus("current")


class _MsanStpCstPortPathCost_Type(Unsigned32):
    """Custom type msanStpCstPortPathCost based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_MsanStpCstPortPathCost_Type.__name__ = "Unsigned32"
_MsanStpCstPortPathCost_Object = MibTableColumn
msanStpCstPortPathCost = _MsanStpCstPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 24, 8, 1, 1),
    _MsanStpCstPortPathCost_Type()
)
msanStpCstPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanStpCstPortPathCost.setStatus("current")


class _MsanStpCstExtPortPathCost_Type(Unsigned32):
    """Custom type msanStpCstExtPortPathCost based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_MsanStpCstExtPortPathCost_Type.__name__ = "Unsigned32"
_MsanStpCstExtPortPathCost_Object = MibTableColumn
msanStpCstExtPortPathCost = _MsanStpCstExtPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 24, 8, 1, 2),
    _MsanStpCstExtPortPathCost_Type()
)
msanStpCstExtPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanStpCstExtPortPathCost.setStatus("current")
_MsanAuthentication_ObjectIdentity = ObjectIdentity
msanAuthentication = _MsanAuthentication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 25)
)
_MsanAuthenticationGlobal_ObjectIdentity = ObjectIdentity
msanAuthenticationGlobal = _MsanAuthenticationGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 25, 1)
)


class _MsanAuthenticationListCreate_Type(DisplayString):
    """Custom type msanAuthenticationListCreate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_MsanAuthenticationListCreate_Type.__name__ = "DisplayString"
_MsanAuthenticationListCreate_Object = MibScalar
msanAuthenticationListCreate = _MsanAuthenticationListCreate_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 25, 2),
    _MsanAuthenticationListCreate_Type()
)
msanAuthenticationListCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanAuthenticationListCreate.setStatus("deprecated")
_MsanAuthenticationListTable_Object = MibTable
msanAuthenticationListTable = _MsanAuthenticationListTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 25, 3)
)
if mibBuilder.loadTexts:
    msanAuthenticationListTable.setStatus("current")
_MsanAuthenticationListEntry_Object = MibTableRow
msanAuthenticationListEntry = _MsanAuthenticationListEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 25, 3, 1)
)
msanAuthenticationListEntry.setIndexNames(
    (0, "ISKRATEL-MSAN-MIB", "msanAuthenticationListName"),
)
if mibBuilder.loadTexts:
    msanAuthenticationListEntry.setStatus("current")


class _MsanAuthenticationListName_Type(DisplayString):
    """Custom type msanAuthenticationListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_MsanAuthenticationListName_Type.__name__ = "DisplayString"
_MsanAuthenticationListName_Object = MibTableColumn
msanAuthenticationListName = _MsanAuthenticationListName_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 25, 3, 1, 1),
    _MsanAuthenticationListName_Type()
)
msanAuthenticationListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanAuthenticationListName.setStatus("current")


class _MsanAuthenticationListMethod1_Type(Integer32):
    """Custom type msanAuthenticationListMethod1 based on Integer32"""
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
        *(("local", 1),
          ("radius", 2),
          ("reject", 3),
          ("tacacs", 4))
    )


_MsanAuthenticationListMethod1_Type.__name__ = "Integer32"
_MsanAuthenticationListMethod1_Object = MibTableColumn
msanAuthenticationListMethod1 = _MsanAuthenticationListMethod1_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 25, 3, 1, 2),
    _MsanAuthenticationListMethod1_Type()
)
msanAuthenticationListMethod1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanAuthenticationListMethod1.setStatus("current")


class _MsanAuthenticationListMethod2_Type(Integer32):
    """Custom type msanAuthenticationListMethod2 based on Integer32"""
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
        *(("local", 2),
          ("radius", 3),
          ("reject", 4),
          ("tacacs", 5),
          ("undefined", 1))
    )


_MsanAuthenticationListMethod2_Type.__name__ = "Integer32"
_MsanAuthenticationListMethod2_Object = MibTableColumn
msanAuthenticationListMethod2 = _MsanAuthenticationListMethod2_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 25, 3, 1, 3),
    _MsanAuthenticationListMethod2_Type()
)
msanAuthenticationListMethod2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanAuthenticationListMethod2.setStatus("current")


class _MsanAuthenticationListMethod3_Type(Integer32):
    """Custom type msanAuthenticationListMethod3 based on Integer32"""
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
        *(("local", 2),
          ("radius", 3),
          ("reject", 4),
          ("tacacs", 5),
          ("undefined", 1))
    )


_MsanAuthenticationListMethod3_Type.__name__ = "Integer32"
_MsanAuthenticationListMethod3_Object = MibTableColumn
msanAuthenticationListMethod3 = _MsanAuthenticationListMethod3_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 25, 3, 1, 4),
    _MsanAuthenticationListMethod3_Type()
)
msanAuthenticationListMethod3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanAuthenticationListMethod3.setStatus("current")
_MsanAuthenticationListStatus_Type = RowStatus
_MsanAuthenticationListStatus_Object = MibTableColumn
msanAuthenticationListStatus = _MsanAuthenticationListStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 25, 3, 1, 5),
    _MsanAuthenticationListStatus_Type()
)
msanAuthenticationListStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanAuthenticationListStatus.setStatus("current")
_MsanPortSecurity_ObjectIdentity = ObjectIdentity
msanPortSecurity = _MsanPortSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 26)
)
_MsanPortSecurityGlobal_ObjectIdentity = ObjectIdentity
msanPortSecurityGlobal = _MsanPortSecurityGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 26, 1)
)
_MsanPortSecurityStatMacTable_Object = MibTable
msanPortSecurityStatMacTable = _MsanPortSecurityStatMacTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 26, 2)
)
if mibBuilder.loadTexts:
    msanPortSecurityStatMacTable.setStatus("current")
_MsanPortSecurityStatMacEntry_Object = MibTableRow
msanPortSecurityStatMacEntry = _MsanPortSecurityStatMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 26, 2, 1)
)
msanPortSecurityStatMacEntry.setIndexNames(
    (0, "ISKRATEL-MSAN-MIB", "msanPortSecurityStatMacIf"),
    (0, "ISKRATEL-MSAN-MIB", "msanPortSecurityStatMacVlanId"),
    (0, "ISKRATEL-MSAN-MIB", "msanPortSecurityStatMacMacAddress"),
)
if mibBuilder.loadTexts:
    msanPortSecurityStatMacEntry.setStatus("current")
_MsanPortSecurityStatMacIf_Type = Integer32
_MsanPortSecurityStatMacIf_Object = MibTableColumn
msanPortSecurityStatMacIf = _MsanPortSecurityStatMacIf_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 26, 2, 1, 1),
    _MsanPortSecurityStatMacIf_Type()
)
msanPortSecurityStatMacIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanPortSecurityStatMacIf.setStatus("current")


class _MsanPortSecurityStatMacVlanId_Type(Integer32):
    """Custom type msanPortSecurityStatMacVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_MsanPortSecurityStatMacVlanId_Type.__name__ = "Integer32"
_MsanPortSecurityStatMacVlanId_Object = MibTableColumn
msanPortSecurityStatMacVlanId = _MsanPortSecurityStatMacVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 26, 2, 1, 2),
    _MsanPortSecurityStatMacVlanId_Type()
)
msanPortSecurityStatMacVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanPortSecurityStatMacVlanId.setStatus("current")
_MsanPortSecurityStatMacMacAddress_Type = MacAddress
_MsanPortSecurityStatMacMacAddress_Object = MibTableColumn
msanPortSecurityStatMacMacAddress = _MsanPortSecurityStatMacMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 26, 2, 1, 3),
    _MsanPortSecurityStatMacMacAddress_Type()
)
msanPortSecurityStatMacMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanPortSecurityStatMacMacAddress.setStatus("current")
_MsanPortSecurityStatMacRowStatus_Type = RowStatus
_MsanPortSecurityStatMacRowStatus_Object = MibTableColumn
msanPortSecurityStatMacRowStatus = _MsanPortSecurityStatMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 26, 2, 1, 5),
    _MsanPortSecurityStatMacRowStatus_Type()
)
msanPortSecurityStatMacRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanPortSecurityStatMacRowStatus.setStatus("current")
_MsanPortSecurityPortVlanTable_Object = MibTable
msanPortSecurityPortVlanTable = _MsanPortSecurityPortVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 26, 3)
)
if mibBuilder.loadTexts:
    msanPortSecurityPortVlanTable.setStatus("current")
_MsanPortSecurityPortVlanEntry_Object = MibTableRow
msanPortSecurityPortVlanEntry = _MsanPortSecurityPortVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 26, 3, 1)
)
msanPortSecurityPortVlanEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    msanPortSecurityPortVlanEntry.setStatus("current")


class _MsanPortSecurityPortVlanDynamicLimit_Type(Integer32):
    """Custom type msanPortSecurityPortVlanDynamicLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_MsanPortSecurityPortVlanDynamicLimit_Type.__name__ = "Integer32"
_MsanPortSecurityPortVlanDynamicLimit_Object = MibTableColumn
msanPortSecurityPortVlanDynamicLimit = _MsanPortSecurityPortVlanDynamicLimit_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 26, 3, 1, 1),
    _MsanPortSecurityPortVlanDynamicLimit_Type()
)
msanPortSecurityPortVlanDynamicLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanPortSecurityPortVlanDynamicLimit.setStatus("current")
_MsanPortSecurityPortVlanRowStatus_Type = RowStatus
_MsanPortSecurityPortVlanRowStatus_Object = MibTableColumn
msanPortSecurityPortVlanRowStatus = _MsanPortSecurityPortVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 26, 3, 1, 2),
    _MsanPortSecurityPortVlanRowStatus_Type()
)
msanPortSecurityPortVlanRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanPortSecurityPortVlanRowStatus.setStatus("current")
_MsanLag_ObjectIdentity = ObjectIdentity
msanLag = _MsanLag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 27)
)
_MsanLagGlobal_ObjectIdentity = ObjectIdentity
msanLagGlobal = _MsanLagGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 27, 1)
)
_MsanLagDetailedConfigTable_Object = MibTable
msanLagDetailedConfigTable = _MsanLagDetailedConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 27, 2)
)
if mibBuilder.loadTexts:
    msanLagDetailedConfigTable.setStatus("current")
_MsanLagDetailedConfigEntry_Object = MibTableRow
msanLagDetailedConfigEntry = _MsanLagDetailedConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 27, 2, 1)
)
msanLagDetailedConfigEntry.setIndexNames(
    (0, "ISKRATEL-MSAN-MIB", "msanLagDetailedLagIndex"),
    (0, "ISKRATEL-MSAN-MIB", "msanLagDetailedIfIndex"),
)
if mibBuilder.loadTexts:
    msanLagDetailedConfigEntry.setStatus("current")
_MsanLagDetailedLagIndex_Type = Integer32
_MsanLagDetailedLagIndex_Object = MibTableColumn
msanLagDetailedLagIndex = _MsanLagDetailedLagIndex_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 27, 2, 1, 1),
    _MsanLagDetailedLagIndex_Type()
)
msanLagDetailedLagIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanLagDetailedLagIndex.setStatus("current")
_MsanLagDetailedIfIndex_Type = Integer32
_MsanLagDetailedIfIndex_Object = MibTableColumn
msanLagDetailedIfIndex = _MsanLagDetailedIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 27, 2, 1, 2),
    _MsanLagDetailedIfIndex_Type()
)
msanLagDetailedIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanLagDetailedIfIndex.setStatus("current")
_MsanLagDetailedPortSpeed_Type = ObjectIdentifier
_MsanLagDetailedPortSpeed_Object = MibTableColumn
msanLagDetailedPortSpeed = _MsanLagDetailedPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 27, 2, 1, 3),
    _MsanLagDetailedPortSpeed_Type()
)
msanLagDetailedPortSpeed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanLagDetailedPortSpeed.setStatus("current")


class _MsanLagDetailedPortStatus_Type(Integer32):
    """Custom type msanLagDetailedPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_MsanLagDetailedPortStatus_Type.__name__ = "Integer32"
_MsanLagDetailedPortStatus_Object = MibTableColumn
msanLagDetailedPortStatus = _MsanLagDetailedPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 27, 2, 1, 4),
    _MsanLagDetailedPortStatus_Type()
)
msanLagDetailedPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanLagDetailedPortStatus.setStatus("current")
_MsanLagDetailedRowStatus_Type = RowStatus
_MsanLagDetailedRowStatus_Object = MibTableColumn
msanLagDetailedRowStatus = _MsanLagDetailedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 27, 2, 1, 5),
    _MsanLagDetailedRowStatus_Type()
)
msanLagDetailedRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanLagDetailedRowStatus.setStatus("current")
_MsanLagTable_Object = MibTable
msanLagTable = _MsanLagTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 27, 3)
)
if mibBuilder.loadTexts:
    msanLagTable.setStatus("current")
_MsanLagEntry_Object = MibTableRow
msanLagEntry = _MsanLagEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 27, 3, 1)
)
msanLagEntry.setIndexNames(
    (0, "ISKRATEL-MSAN-MIB", "msanLagIndex"),
)
if mibBuilder.loadTexts:
    msanLagEntry.setStatus("current")
_MsanLagIndex_Type = Integer32
_MsanLagIndex_Object = MibTableColumn
msanLagIndex = _MsanLagIndex_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 27, 3, 1, 1),
    _MsanLagIndex_Type()
)
msanLagIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanLagIndex.setStatus("current")
_MsanLagMaxFrameSize_Type = Integer32
_MsanLagMaxFrameSize_Object = MibTableColumn
msanLagMaxFrameSize = _MsanLagMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 27, 3, 1, 2),
    _MsanLagMaxFrameSize_Type()
)
msanLagMaxFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanLagMaxFrameSize.setStatus("current")


class _MsanLagDVlanTagMode_Type(Integer32):
    """Custom type msanLagDVlanTagMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanLagDVlanTagMode_Type.__name__ = "Integer32"
_MsanLagDVlanTagMode_Object = MibTableColumn
msanLagDVlanTagMode = _MsanLagDVlanTagMode_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 27, 3, 1, 3),
    _MsanLagDVlanTagMode_Type()
)
msanLagDVlanTagMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanLagDVlanTagMode.setStatus("current")
_MsanRadiusServer_ObjectIdentity = ObjectIdentity
msanRadiusServer = _MsanRadiusServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 28)
)
_MsanRadiusServerGlobal_ObjectIdentity = ObjectIdentity
msanRadiusServerGlobal = _MsanRadiusServerGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 28, 1)
)
_MsanRadiusServerConfigTable_Object = MibTable
msanRadiusServerConfigTable = _MsanRadiusServerConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 28, 2)
)
if mibBuilder.loadTexts:
    msanRadiusServerConfigTable.setStatus("current")
_MsanRadiusServerConfigEntry_Object = MibTableRow
msanRadiusServerConfigEntry = _MsanRadiusServerConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 28, 2, 1)
)
msanRadiusServerConfigEntry.setIndexNames(
    (0, "ISKRATEL-MSAN-MIB", "msanRadiusServerAddress"),
)
if mibBuilder.loadTexts:
    msanRadiusServerConfigEntry.setStatus("current")
_MsanRadiusServerAddress_Type = IpAddress
_MsanRadiusServerAddress_Object = MibTableColumn
msanRadiusServerAddress = _MsanRadiusServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 28, 2, 1, 1),
    _MsanRadiusServerAddress_Type()
)
msanRadiusServerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanRadiusServerAddress.setStatus("current")


class _MsanRadiusServerPort_Type(Unsigned32):
    """Custom type msanRadiusServerPort based on Unsigned32"""
    defaultValue = 1812

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MsanRadiusServerPort_Type.__name__ = "Unsigned32"
_MsanRadiusServerPort_Object = MibTableColumn
msanRadiusServerPort = _MsanRadiusServerPort_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 28, 2, 1, 2),
    _MsanRadiusServerPort_Type()
)
msanRadiusServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanRadiusServerPort.setStatus("current")


class _MsanRadiusServerSecret_Type(DisplayString):
    """Custom type msanRadiusServerSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_MsanRadiusServerSecret_Type.__name__ = "DisplayString"
_MsanRadiusServerSecret_Object = MibTableColumn
msanRadiusServerSecret = _MsanRadiusServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 28, 2, 1, 3),
    _MsanRadiusServerSecret_Type()
)
msanRadiusServerSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanRadiusServerSecret.setStatus("current")


class _MsanRadiusServerPrimaryMode_Type(Integer32):
    """Custom type msanRadiusServerPrimaryMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanRadiusServerPrimaryMode_Type.__name__ = "Integer32"
_MsanRadiusServerPrimaryMode_Object = MibTableColumn
msanRadiusServerPrimaryMode = _MsanRadiusServerPrimaryMode_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 28, 2, 1, 4),
    _MsanRadiusServerPrimaryMode_Type()
)
msanRadiusServerPrimaryMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanRadiusServerPrimaryMode.setStatus("current")


class _MsanRadiusServerCurrentMode_Type(Integer32):
    """Custom type msanRadiusServerCurrentMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_MsanRadiusServerCurrentMode_Type.__name__ = "Integer32"
_MsanRadiusServerCurrentMode_Object = MibTableColumn
msanRadiusServerCurrentMode = _MsanRadiusServerCurrentMode_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 28, 2, 1, 5),
    _MsanRadiusServerCurrentMode_Type()
)
msanRadiusServerCurrentMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanRadiusServerCurrentMode.setStatus("current")


class _MsanRadiusServerMsgAuth_Type(Integer32):
    """Custom type msanRadiusServerMsgAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanRadiusServerMsgAuth_Type.__name__ = "Integer32"
_MsanRadiusServerMsgAuth_Object = MibTableColumn
msanRadiusServerMsgAuth = _MsanRadiusServerMsgAuth_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 28, 2, 1, 6),
    _MsanRadiusServerMsgAuth_Type()
)
msanRadiusServerMsgAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanRadiusServerMsgAuth.setStatus("current")
_MsanRadiusServerStatus_Type = RowStatus
_MsanRadiusServerStatus_Object = MibTableColumn
msanRadiusServerStatus = _MsanRadiusServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 28, 2, 1, 7),
    _MsanRadiusServerStatus_Type()
)
msanRadiusServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanRadiusServerStatus.setStatus("current")
_MsanNetwork_ObjectIdentity = ObjectIdentity
msanNetwork = _MsanNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 29)
)
_MsanNetworkGlobal_ObjectIdentity = ObjectIdentity
msanNetworkGlobal = _MsanNetworkGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 29, 1)
)
_MsanNetworkIPAddress_Type = IpAddress
_MsanNetworkIPAddress_Object = MibScalar
msanNetworkIPAddress = _MsanNetworkIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 29, 1, 1),
    _MsanNetworkIPAddress_Type()
)
msanNetworkIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanNetworkIPAddress.setStatus("current")
_MsanNetworkSubnetMask_Type = IpAddress
_MsanNetworkSubnetMask_Object = MibScalar
msanNetworkSubnetMask = _MsanNetworkSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 29, 1, 2),
    _MsanNetworkSubnetMask_Type()
)
msanNetworkSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanNetworkSubnetMask.setStatus("current")
_MsanNetworkDefaultGateway_Type = IpAddress
_MsanNetworkDefaultGateway_Object = MibScalar
msanNetworkDefaultGateway = _MsanNetworkDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 29, 1, 3),
    _MsanNetworkDefaultGateway_Type()
)
msanNetworkDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanNetworkDefaultGateway.setStatus("current")
_MsanNetworkDhcpSrvIpAddr_Type = IpAddress
_MsanNetworkDhcpSrvIpAddr_Object = MibScalar
msanNetworkDhcpSrvIpAddr = _MsanNetworkDhcpSrvIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 29, 1, 4),
    _MsanNetworkDhcpSrvIpAddr_Type()
)
msanNetworkDhcpSrvIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanNetworkDhcpSrvIpAddr.setStatus("current")


class _MsanNetworkDhcpSrvVendorSpecific_Type(Integer32):
    """Custom type msanNetworkDhcpSrvVendorSpecific based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanNetworkDhcpSrvVendorSpecific_Type.__name__ = "Integer32"
_MsanNetworkDhcpSrvVendorSpecific_Object = MibScalar
msanNetworkDhcpSrvVendorSpecific = _MsanNetworkDhcpSrvVendorSpecific_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 29, 1, 5),
    _MsanNetworkDhcpSrvVendorSpecific_Type()
)
msanNetworkDhcpSrvVendorSpecific.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanNetworkDhcpSrvVendorSpecific.setStatus("current")
_MsanNetworkDhcpClientLeaseObtained_Type = OctetString
_MsanNetworkDhcpClientLeaseObtained_Object = MibScalar
msanNetworkDhcpClientLeaseObtained = _MsanNetworkDhcpClientLeaseObtained_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 29, 1, 6),
    _MsanNetworkDhcpClientLeaseObtained_Type()
)
msanNetworkDhcpClientLeaseObtained.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanNetworkDhcpClientLeaseObtained.setStatus("current")
_MsanNetworkDhcpClientLeaseExpires_Type = OctetString
_MsanNetworkDhcpClientLeaseExpires_Object = MibScalar
msanNetworkDhcpClientLeaseExpires = _MsanNetworkDhcpClientLeaseExpires_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 29, 1, 7),
    _MsanNetworkDhcpClientLeaseExpires_Type()
)
msanNetworkDhcpClientLeaseExpires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanNetworkDhcpClientLeaseExpires.setStatus("current")


class _MsanNetworkDhcpClientLocalOpt82_Type(Integer32):
    """Custom type msanNetworkDhcpClientLocalOpt82 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanNetworkDhcpClientLocalOpt82_Type.__name__ = "Integer32"
_MsanNetworkDhcpClientLocalOpt82_Object = MibScalar
msanNetworkDhcpClientLocalOpt82 = _MsanNetworkDhcpClientLocalOpt82_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 29, 1, 8),
    _MsanNetworkDhcpClientLocalOpt82_Type()
)
msanNetworkDhcpClientLocalOpt82.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanNetworkDhcpClientLocalOpt82.setStatus("current")
_MsanNetworkDhcpClientVlanTable_Object = MibTable
msanNetworkDhcpClientVlanTable = _MsanNetworkDhcpClientVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 29, 2)
)
if mibBuilder.loadTexts:
    msanNetworkDhcpClientVlanTable.setStatus("current")
_MsanNetworkDhcpClientVlanEntry_Object = MibTableRow
msanNetworkDhcpClientVlanEntry = _MsanNetworkDhcpClientVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 29, 2, 1)
)
msanNetworkDhcpClientVlanEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    msanNetworkDhcpClientVlanEntry.setStatus("current")


class _MsanNetworkDhcpClientVlanLocalOpt82_Type(Integer32):
    """Custom type msanNetworkDhcpClientVlanLocalOpt82 based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanNetworkDhcpClientVlanLocalOpt82_Type.__name__ = "Integer32"
_MsanNetworkDhcpClientVlanLocalOpt82_Object = MibTableColumn
msanNetworkDhcpClientVlanLocalOpt82 = _MsanNetworkDhcpClientVlanLocalOpt82_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 29, 2, 1, 1),
    _MsanNetworkDhcpClientVlanLocalOpt82_Type()
)
msanNetworkDhcpClientVlanLocalOpt82.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanNetworkDhcpClientVlanLocalOpt82.setStatus("current")
_MsanStormControl_ObjectIdentity = ObjectIdentity
msanStormControl = _MsanStormControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 30)
)
_MsanStormControlGlobal_ObjectIdentity = ObjectIdentity
msanStormControlGlobal = _MsanStormControlGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 30, 1)
)
_MsanPortStormControlTable_Object = MibTable
msanPortStormControlTable = _MsanPortStormControlTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 30, 2)
)
if mibBuilder.loadTexts:
    msanPortStormControlTable.setStatus("current")
_MsanPortStormControlEntry_Object = MibTableRow
msanPortStormControlEntry = _MsanPortStormControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 30, 2, 1)
)
msanPortStormControlEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    msanPortStormControlEntry.setStatus("current")


class _MsanPortBroadcastControlMode_Type(Integer32):
    """Custom type msanPortBroadcastControlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanPortBroadcastControlMode_Type.__name__ = "Integer32"
_MsanPortBroadcastControlMode_Object = MibTableColumn
msanPortBroadcastControlMode = _MsanPortBroadcastControlMode_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 30, 2, 1, 1),
    _MsanPortBroadcastControlMode_Type()
)
msanPortBroadcastControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanPortBroadcastControlMode.setStatus("current")
_MsanPortBroadcastControlThreshold_Type = Integer32
_MsanPortBroadcastControlThreshold_Object = MibTableColumn
msanPortBroadcastControlThreshold = _MsanPortBroadcastControlThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 30, 2, 1, 2),
    _MsanPortBroadcastControlThreshold_Type()
)
msanPortBroadcastControlThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanPortBroadcastControlThreshold.setStatus("current")
if mibBuilder.loadTexts:
    msanPortBroadcastControlThreshold.setUnits("packets per second")


class _MsanPortMulticastControlMode_Type(Integer32):
    """Custom type msanPortMulticastControlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanPortMulticastControlMode_Type.__name__ = "Integer32"
_MsanPortMulticastControlMode_Object = MibTableColumn
msanPortMulticastControlMode = _MsanPortMulticastControlMode_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 30, 2, 1, 3),
    _MsanPortMulticastControlMode_Type()
)
msanPortMulticastControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanPortMulticastControlMode.setStatus("current")
_MsanPortMulticastControlThreshold_Type = Integer32
_MsanPortMulticastControlThreshold_Object = MibTableColumn
msanPortMulticastControlThreshold = _MsanPortMulticastControlThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 30, 2, 1, 4),
    _MsanPortMulticastControlThreshold_Type()
)
msanPortMulticastControlThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanPortMulticastControlThreshold.setStatus("current")
if mibBuilder.loadTexts:
    msanPortMulticastControlThreshold.setUnits("packets per second")


class _MsanPortUnicastControlMode_Type(Integer32):
    """Custom type msanPortUnicastControlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanPortUnicastControlMode_Type.__name__ = "Integer32"
_MsanPortUnicastControlMode_Object = MibTableColumn
msanPortUnicastControlMode = _MsanPortUnicastControlMode_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 30, 2, 1, 5),
    _MsanPortUnicastControlMode_Type()
)
msanPortUnicastControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanPortUnicastControlMode.setStatus("current")
_MsanPortUnicastControlThreshold_Type = Integer32
_MsanPortUnicastControlThreshold_Object = MibTableColumn
msanPortUnicastControlThreshold = _MsanPortUnicastControlThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 30, 2, 1, 6),
    _MsanPortUnicastControlThreshold_Type()
)
msanPortUnicastControlThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanPortUnicastControlThreshold.setStatus("current")
if mibBuilder.loadTexts:
    msanPortUnicastControlThreshold.setUnits("packets per second")
_MsanUserConfig_ObjectIdentity = ObjectIdentity
msanUserConfig = _MsanUserConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 31)
)
_MsanUserConfigGlobal_ObjectIdentity = ObjectIdentity
msanUserConfigGlobal = _MsanUserConfigGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 31, 1)
)


class _MsanUserConfigCheckPassword_Type(OctetString):
    """Custom type msanUserConfigCheckPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MsanUserConfigCheckPassword_Type.__name__ = "OctetString"
_MsanUserConfigCheckPassword_Object = MibScalar
msanUserConfigCheckPassword = _MsanUserConfigCheckPassword_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 31, 1, 1),
    _MsanUserConfigCheckPassword_Type()
)
msanUserConfigCheckPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanUserConfigCheckPassword.setStatus("current")
_MsanUserConfigTable_Object = MibTable
msanUserConfigTable = _MsanUserConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 31, 2)
)
if mibBuilder.loadTexts:
    msanUserConfigTable.setStatus("current")
_MsanUserConfigEntry_Object = MibTableRow
msanUserConfigEntry = _MsanUserConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 31, 2, 1)
)
msanUserConfigEntry.setIndexNames(
    (0, "ISKRATEL-MSAN-MIB", "msanUserIndex"),
)
if mibBuilder.loadTexts:
    msanUserConfigEntry.setStatus("current")
_MsanUserIndex_Type = Integer32
_MsanUserIndex_Object = MibTableColumn
msanUserIndex = _MsanUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 31, 2, 1, 1),
    _MsanUserIndex_Type()
)
msanUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanUserIndex.setStatus("current")


class _MsanUserAccessMode_Type(Integer32):
    """Custom type msanUserAccessMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("read", 1),
          ("write", 2))
    )


_MsanUserAccessMode_Type.__name__ = "Integer32"
_MsanUserAccessMode_Object = MibTableColumn
msanUserAccessMode = _MsanUserAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 31, 2, 1, 2),
    _MsanUserAccessMode_Type()
)
msanUserAccessMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanUserAccessMode.setStatus("current")
_MsanSfp_ObjectIdentity = ObjectIdentity
msanSfp = _MsanSfp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 32)
)
_MsanSfpGlobal_ObjectIdentity = ObjectIdentity
msanSfpGlobal = _MsanSfpGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 32, 1)
)
_MsanSfpInfoTable_Object = MibTable
msanSfpInfoTable = _MsanSfpInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 32, 2)
)
if mibBuilder.loadTexts:
    msanSfpInfoTable.setStatus("current")
_MsanSfpInfoEntry_Object = MibTableRow
msanSfpInfoEntry = _MsanSfpInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 32, 2, 1)
)
msanSfpInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    msanSfpInfoEntry.setStatus("current")


class _MsanSfpInfoState_Type(Integer32):
    """Custom type msanSfpInfoState based on Integer32"""
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
        *(("adminOff", 1),
          ("loss", 4),
          ("notAvaliable", 5),
          ("notPresent", 7),
          ("operWithAl", 3),
          ("operational", 2),
          ("presNoDiag", 6))
    )


_MsanSfpInfoState_Type.__name__ = "Integer32"
_MsanSfpInfoState_Object = MibTableColumn
msanSfpInfoState = _MsanSfpInfoState_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 32, 2, 1, 1),
    _MsanSfpInfoState_Type()
)
msanSfpInfoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanSfpInfoState.setStatus("current")


class _MsanSfpInfoInterfaceType_Type(Integer32):
    """Custom type msanSfpInfoInterfaceType based on Integer32"""
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
        *(("ad", 4),
          ("no", 3),
          ("not", 2),
          ("sfp", 1),
          ("xfp", 5))
    )


_MsanSfpInfoInterfaceType_Type.__name__ = "Integer32"
_MsanSfpInfoInterfaceType_Object = MibTableColumn
msanSfpInfoInterfaceType = _MsanSfpInfoInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 32, 2, 1, 2),
    _MsanSfpInfoInterfaceType_Type()
)
msanSfpInfoInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanSfpInfoInterfaceType.setStatus("current")
_MsanSfpInfoNominalBitrate_Type = Integer32
_MsanSfpInfoNominalBitrate_Object = MibTableColumn
msanSfpInfoNominalBitrate = _MsanSfpInfoNominalBitrate_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 32, 2, 1, 3),
    _MsanSfpInfoNominalBitrate_Type()
)
msanSfpInfoNominalBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanSfpInfoNominalBitrate.setStatus("current")
_MsanSfpInfoNominalRange_Type = OctetString
_MsanSfpInfoNominalRange_Object = MibTableColumn
msanSfpInfoNominalRange = _MsanSfpInfoNominalRange_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 32, 2, 1, 4),
    _MsanSfpInfoNominalRange_Type()
)
msanSfpInfoNominalRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanSfpInfoNominalRange.setStatus("current")
_MsanSfpInfoVendor_Type = OctetString
_MsanSfpInfoVendor_Object = MibTableColumn
msanSfpInfoVendor = _MsanSfpInfoVendor_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 32, 2, 1, 5),
    _MsanSfpInfoVendor_Type()
)
msanSfpInfoVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanSfpInfoVendor.setStatus("current")
_MsanSfpInfoIeeeVendorId_Type = Integer32
_MsanSfpInfoIeeeVendorId_Object = MibTableColumn
msanSfpInfoIeeeVendorId = _MsanSfpInfoIeeeVendorId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 32, 2, 1, 6),
    _MsanSfpInfoIeeeVendorId_Type()
)
msanSfpInfoIeeeVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanSfpInfoIeeeVendorId.setStatus("current")
_MsanSfpInfoPartNr_Type = OctetString
_MsanSfpInfoPartNr_Object = MibTableColumn
msanSfpInfoPartNr = _MsanSfpInfoPartNr_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 32, 2, 1, 7),
    _MsanSfpInfoPartNr_Type()
)
msanSfpInfoPartNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanSfpInfoPartNr.setStatus("current")
_MsanSfpInfoRevisionNr_Type = OctetString
_MsanSfpInfoRevisionNr_Object = MibTableColumn
msanSfpInfoRevisionNr = _MsanSfpInfoRevisionNr_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 32, 2, 1, 8),
    _MsanSfpInfoRevisionNr_Type()
)
msanSfpInfoRevisionNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanSfpInfoRevisionNr.setStatus("current")
_MsanSfpInfoSerialNr_Type = OctetString
_MsanSfpInfoSerialNr_Object = MibTableColumn
msanSfpInfoSerialNr = _MsanSfpInfoSerialNr_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 32, 2, 1, 9),
    _MsanSfpInfoSerialNr_Type()
)
msanSfpInfoSerialNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanSfpInfoSerialNr.setStatus("current")
_MsanSfpInfoManufacturingDate_Type = OctetString
_MsanSfpInfoManufacturingDate_Object = MibTableColumn
msanSfpInfoManufacturingDate = _MsanSfpInfoManufacturingDate_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 32, 2, 1, 10),
    _MsanSfpInfoManufacturingDate_Type()
)
msanSfpInfoManufacturingDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanSfpInfoManufacturingDate.setStatus("current")
_MsanSfpInfoWavelength_Type = Integer32
_MsanSfpInfoWavelength_Object = MibTableColumn
msanSfpInfoWavelength = _MsanSfpInfoWavelength_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 32, 2, 1, 11),
    _MsanSfpInfoWavelength_Type()
)
msanSfpInfoWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanSfpInfoWavelength.setStatus("current")
_MsanSfpDiagnosticsTable_Object = MibTable
msanSfpDiagnosticsTable = _MsanSfpDiagnosticsTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 32, 3)
)
if mibBuilder.loadTexts:
    msanSfpDiagnosticsTable.setStatus("current")
_MsanSfpDiagnosticsEntry_Object = MibTableRow
msanSfpDiagnosticsEntry = _MsanSfpDiagnosticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 32, 3, 1)
)
msanSfpDiagnosticsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    msanSfpDiagnosticsEntry.setStatus("current")


class _MsanSfpDiagnosticsSignal_Type(Integer32):
    """Custom type msanSfpDiagnosticsSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("loss", 1),
          ("notSupported", 3),
          ("ok", 2))
    )


_MsanSfpDiagnosticsSignal_Type.__name__ = "Integer32"
_MsanSfpDiagnosticsSignal_Object = MibTableColumn
msanSfpDiagnosticsSignal = _MsanSfpDiagnosticsSignal_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 32, 3, 1, 1),
    _MsanSfpDiagnosticsSignal_Type()
)
msanSfpDiagnosticsSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanSfpDiagnosticsSignal.setStatus("current")
_MsanSfpDiagnosticsTempCurrent_Type = Integer32
_MsanSfpDiagnosticsTempCurrent_Object = MibTableColumn
msanSfpDiagnosticsTempCurrent = _MsanSfpDiagnosticsTempCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 32, 3, 1, 2),
    _MsanSfpDiagnosticsTempCurrent_Type()
)
msanSfpDiagnosticsTempCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanSfpDiagnosticsTempCurrent.setStatus("current")
_MsanSfpDiagnosticsTempMin_Type = Integer32
_MsanSfpDiagnosticsTempMin_Object = MibTableColumn
msanSfpDiagnosticsTempMin = _MsanSfpDiagnosticsTempMin_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 32, 3, 1, 3),
    _MsanSfpDiagnosticsTempMin_Type()
)
msanSfpDiagnosticsTempMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanSfpDiagnosticsTempMin.setStatus("current")
_MsanSfpDiagnosticsTempMax_Type = Integer32
_MsanSfpDiagnosticsTempMax_Object = MibTableColumn
msanSfpDiagnosticsTempMax = _MsanSfpDiagnosticsTempMax_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 32, 3, 1, 4),
    _MsanSfpDiagnosticsTempMax_Type()
)
msanSfpDiagnosticsTempMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanSfpDiagnosticsTempMax.setStatus("current")
_MsanSfpDiagnosticsVoltageCurrent_Type = Integer32
_MsanSfpDiagnosticsVoltageCurrent_Object = MibTableColumn
msanSfpDiagnosticsVoltageCurrent = _MsanSfpDiagnosticsVoltageCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 32, 3, 1, 6),
    _MsanSfpDiagnosticsVoltageCurrent_Type()
)
msanSfpDiagnosticsVoltageCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanSfpDiagnosticsVoltageCurrent.setStatus("current")
if mibBuilder.loadTexts:
    msanSfpDiagnosticsVoltageCurrent.setUnits("0.01 V")
_MsanSfpDiagnosticsVoltageMin_Type = Integer32
_MsanSfpDiagnosticsVoltageMin_Object = MibTableColumn
msanSfpDiagnosticsVoltageMin = _MsanSfpDiagnosticsVoltageMin_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 32, 3, 1, 7),
    _MsanSfpDiagnosticsVoltageMin_Type()
)
msanSfpDiagnosticsVoltageMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanSfpDiagnosticsVoltageMin.setStatus("current")
if mibBuilder.loadTexts:
    msanSfpDiagnosticsVoltageMin.setUnits("0.01 V")
_MsanSfpDiagnosticsVoltageMax_Type = Integer32
_MsanSfpDiagnosticsVoltageMax_Object = MibTableColumn
msanSfpDiagnosticsVoltageMax = _MsanSfpDiagnosticsVoltageMax_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 32, 3, 1, 8),
    _MsanSfpDiagnosticsVoltageMax_Type()
)
msanSfpDiagnosticsVoltageMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanSfpDiagnosticsVoltageMax.setStatus("current")
if mibBuilder.loadTexts:
    msanSfpDiagnosticsVoltageMax.setUnits("0.01 V")
_MsanSfpDiagnosticsTxBiasCrrCurrent_Type = Integer32
_MsanSfpDiagnosticsTxBiasCrrCurrent_Object = MibTableColumn
msanSfpDiagnosticsTxBiasCrrCurrent = _MsanSfpDiagnosticsTxBiasCrrCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 32, 3, 1, 9),
    _MsanSfpDiagnosticsTxBiasCrrCurrent_Type()
)
msanSfpDiagnosticsTxBiasCrrCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanSfpDiagnosticsTxBiasCrrCurrent.setStatus("current")
if mibBuilder.loadTexts:
    msanSfpDiagnosticsTxBiasCrrCurrent.setUnits("0.01 mA")
_MsanSfpDiagnosticsTxBiasCrrMin_Type = Integer32
_MsanSfpDiagnosticsTxBiasCrrMin_Object = MibTableColumn
msanSfpDiagnosticsTxBiasCrrMin = _MsanSfpDiagnosticsTxBiasCrrMin_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 32, 3, 1, 10),
    _MsanSfpDiagnosticsTxBiasCrrMin_Type()
)
msanSfpDiagnosticsTxBiasCrrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanSfpDiagnosticsTxBiasCrrMin.setStatus("current")
if mibBuilder.loadTexts:
    msanSfpDiagnosticsTxBiasCrrMin.setUnits("0.01 mA")
_MsanSfpDiagnosticsTxBiasCrrMax_Type = Integer32
_MsanSfpDiagnosticsTxBiasCrrMax_Object = MibTableColumn
msanSfpDiagnosticsTxBiasCrrMax = _MsanSfpDiagnosticsTxBiasCrrMax_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 32, 3, 1, 11),
    _MsanSfpDiagnosticsTxBiasCrrMax_Type()
)
msanSfpDiagnosticsTxBiasCrrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanSfpDiagnosticsTxBiasCrrMax.setStatus("current")
if mibBuilder.loadTexts:
    msanSfpDiagnosticsTxBiasCrrMax.setUnits("0.01 mA")
_MsanSfpDiagnosticsTxPowerCurrent_Type = Integer32
_MsanSfpDiagnosticsTxPowerCurrent_Object = MibTableColumn
msanSfpDiagnosticsTxPowerCurrent = _MsanSfpDiagnosticsTxPowerCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 32, 3, 1, 12),
    _MsanSfpDiagnosticsTxPowerCurrent_Type()
)
msanSfpDiagnosticsTxPowerCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanSfpDiagnosticsTxPowerCurrent.setStatus("current")
if mibBuilder.loadTexts:
    msanSfpDiagnosticsTxPowerCurrent.setUnits("0.01 mW")
_MsanSfpDiagnosticsTxPowerMin_Type = Integer32
_MsanSfpDiagnosticsTxPowerMin_Object = MibTableColumn
msanSfpDiagnosticsTxPowerMin = _MsanSfpDiagnosticsTxPowerMin_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 32, 3, 1, 13),
    _MsanSfpDiagnosticsTxPowerMin_Type()
)
msanSfpDiagnosticsTxPowerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanSfpDiagnosticsTxPowerMin.setStatus("current")
if mibBuilder.loadTexts:
    msanSfpDiagnosticsTxPowerMin.setUnits("0.01 mW")
_MsanSfpDiagnosticsTxPowerMax_Type = Integer32
_MsanSfpDiagnosticsTxPowerMax_Object = MibTableColumn
msanSfpDiagnosticsTxPowerMax = _MsanSfpDiagnosticsTxPowerMax_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 32, 3, 1, 14),
    _MsanSfpDiagnosticsTxPowerMax_Type()
)
msanSfpDiagnosticsTxPowerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanSfpDiagnosticsTxPowerMax.setStatus("current")
if mibBuilder.loadTexts:
    msanSfpDiagnosticsTxPowerMax.setUnits("0.01 mW")
_MsanSfpDiagnosticsRxPowerCurrent_Type = Integer32
_MsanSfpDiagnosticsRxPowerCurrent_Object = MibTableColumn
msanSfpDiagnosticsRxPowerCurrent = _MsanSfpDiagnosticsRxPowerCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 32, 3, 1, 15),
    _MsanSfpDiagnosticsRxPowerCurrent_Type()
)
msanSfpDiagnosticsRxPowerCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanSfpDiagnosticsRxPowerCurrent.setStatus("current")
if mibBuilder.loadTexts:
    msanSfpDiagnosticsRxPowerCurrent.setUnits("0.0001 mW")
_MsanSfpDiagnosticsRxPowerMin_Type = Integer32
_MsanSfpDiagnosticsRxPowerMin_Object = MibTableColumn
msanSfpDiagnosticsRxPowerMin = _MsanSfpDiagnosticsRxPowerMin_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 32, 3, 1, 16),
    _MsanSfpDiagnosticsRxPowerMin_Type()
)
msanSfpDiagnosticsRxPowerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanSfpDiagnosticsRxPowerMin.setStatus("current")
if mibBuilder.loadTexts:
    msanSfpDiagnosticsRxPowerMin.setUnits("0.0001 mW")
_MsanSfpDiagnosticsRxPowerMax_Type = Integer32
_MsanSfpDiagnosticsRxPowerMax_Object = MibTableColumn
msanSfpDiagnosticsRxPowerMax = _MsanSfpDiagnosticsRxPowerMax_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 32, 3, 1, 17),
    _MsanSfpDiagnosticsRxPowerMax_Type()
)
msanSfpDiagnosticsRxPowerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanSfpDiagnosticsRxPowerMax.setStatus("current")
if mibBuilder.loadTexts:
    msanSfpDiagnosticsRxPowerMax.setUnits("0.0001 mW")


class _MsanSfpDiagnosticsTempStatus_Type(Integer32):
    """Custom type msanSfpDiagnosticsTempStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 3),
          ("sfpDiagAlarm", 2),
          ("sfpDiagNoAlarm", 1))
    )


_MsanSfpDiagnosticsTempStatus_Type.__name__ = "Integer32"
_MsanSfpDiagnosticsTempStatus_Object = MibTableColumn
msanSfpDiagnosticsTempStatus = _MsanSfpDiagnosticsTempStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 32, 3, 1, 19),
    _MsanSfpDiagnosticsTempStatus_Type()
)
msanSfpDiagnosticsTempStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanSfpDiagnosticsTempStatus.setStatus("current")


class _MsanSfpDiagnosticsVoltageStatus_Type(Integer32):
    """Custom type msanSfpDiagnosticsVoltageStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 3),
          ("sfpDiagAlarm", 2),
          ("sfpDiagNoAlarm", 1))
    )


_MsanSfpDiagnosticsVoltageStatus_Type.__name__ = "Integer32"
_MsanSfpDiagnosticsVoltageStatus_Object = MibTableColumn
msanSfpDiagnosticsVoltageStatus = _MsanSfpDiagnosticsVoltageStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 32, 3, 1, 20),
    _MsanSfpDiagnosticsVoltageStatus_Type()
)
msanSfpDiagnosticsVoltageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanSfpDiagnosticsVoltageStatus.setStatus("current")


class _MsanSfpDiagnosticsTxBiasStatus_Type(Integer32):
    """Custom type msanSfpDiagnosticsTxBiasStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 3),
          ("sfpDiagAlarm", 2),
          ("sfpDiagNoAlarm", 1))
    )


_MsanSfpDiagnosticsTxBiasStatus_Type.__name__ = "Integer32"
_MsanSfpDiagnosticsTxBiasStatus_Object = MibTableColumn
msanSfpDiagnosticsTxBiasStatus = _MsanSfpDiagnosticsTxBiasStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 32, 3, 1, 21),
    _MsanSfpDiagnosticsTxBiasStatus_Type()
)
msanSfpDiagnosticsTxBiasStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanSfpDiagnosticsTxBiasStatus.setStatus("current")


class _MsanSfpDiagnosticsTxPowerStatus_Type(Integer32):
    """Custom type msanSfpDiagnosticsTxPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 3),
          ("sfpDiagAlarm", 2),
          ("sfpDiagNoAlarm", 1))
    )


_MsanSfpDiagnosticsTxPowerStatus_Type.__name__ = "Integer32"
_MsanSfpDiagnosticsTxPowerStatus_Object = MibTableColumn
msanSfpDiagnosticsTxPowerStatus = _MsanSfpDiagnosticsTxPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 32, 3, 1, 22),
    _MsanSfpDiagnosticsTxPowerStatus_Type()
)
msanSfpDiagnosticsTxPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanSfpDiagnosticsTxPowerStatus.setStatus("current")


class _MsanSfpDiagnosticsRxPowerStatus_Type(Integer32):
    """Custom type msanSfpDiagnosticsRxPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 3),
          ("sfpDiagAlarm", 2),
          ("sfpDiagNoAlarm", 1))
    )


_MsanSfpDiagnosticsRxPowerStatus_Type.__name__ = "Integer32"
_MsanSfpDiagnosticsRxPowerStatus_Object = MibTableColumn
msanSfpDiagnosticsRxPowerStatus = _MsanSfpDiagnosticsRxPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 32, 3, 1, 23),
    _MsanSfpDiagnosticsRxPowerStatus_Type()
)
msanSfpDiagnosticsRxPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanSfpDiagnosticsRxPowerStatus.setStatus("current")
_MsanMacSg_ObjectIdentity = ObjectIdentity
msanMacSg = _MsanMacSg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 34)
)
_MsanMacSgGlobal_ObjectIdentity = ObjectIdentity
msanMacSgGlobal = _MsanMacSgGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 34, 1)
)


class _MsanMacSgStatus_Type(Integer32):
    """Custom type msanMacSgStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanMacSgStatus_Type.__name__ = "Integer32"
_MsanMacSgStatus_Object = MibScalar
msanMacSgStatus = _MsanMacSgStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 34, 1, 1),
    _MsanMacSgStatus_Type()
)
msanMacSgStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanMacSgStatus.setStatus("current")
_MsanMacSgPortTable_Object = MibTable
msanMacSgPortTable = _MsanMacSgPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 34, 2)
)
if mibBuilder.loadTexts:
    msanMacSgPortTable.setStatus("current")
_MsanMacSgPortEntry_Object = MibTableRow
msanMacSgPortEntry = _MsanMacSgPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 34, 2, 1)
)
msanMacSgPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    msanMacSgPortEntry.setStatus("current")


class _MsanMacSgPortStatus_Type(Integer32):
    """Custom type msanMacSgPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanMacSgPortStatus_Type.__name__ = "Integer32"
_MsanMacSgPortStatus_Object = MibTableColumn
msanMacSgPortStatus = _MsanMacSgPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 34, 2, 1, 1),
    _MsanMacSgPortStatus_Type()
)
msanMacSgPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanMacSgPortStatus.setStatus("current")
_MsanMacSgPortViolationsCounter_Type = Integer32
_MsanMacSgPortViolationsCounter_Object = MibTableColumn
msanMacSgPortViolationsCounter = _MsanMacSgPortViolationsCounter_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 34, 2, 1, 2),
    _MsanMacSgPortViolationsCounter_Type()
)
msanMacSgPortViolationsCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanMacSgPortViolationsCounter.setStatus("current")
_MsanErrorDisable_ObjectIdentity = ObjectIdentity
msanErrorDisable = _MsanErrorDisable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 35)
)
_MsanErrorDisableGlobal_ObjectIdentity = ObjectIdentity
msanErrorDisableGlobal = _MsanErrorDisableGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 35, 1)
)
_MsanErrorDisableInterval_Type = Integer32
_MsanErrorDisableInterval_Object = MibScalar
msanErrorDisableInterval = _MsanErrorDisableInterval_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 35, 1, 1),
    _MsanErrorDisableInterval_Type()
)
msanErrorDisableInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanErrorDisableInterval.setStatus("current")
if mibBuilder.loadTexts:
    msanErrorDisableInterval.setUnits("minutes")


class _MsanErrorDisableMacSgDetectionStatus_Type(Integer32):
    """Custom type msanErrorDisableMacSgDetectionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanErrorDisableMacSgDetectionStatus_Type.__name__ = "Integer32"
_MsanErrorDisableMacSgDetectionStatus_Object = MibScalar
msanErrorDisableMacSgDetectionStatus = _MsanErrorDisableMacSgDetectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 35, 1, 2),
    _MsanErrorDisableMacSgDetectionStatus_Type()
)
msanErrorDisableMacSgDetectionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanErrorDisableMacSgDetectionStatus.setStatus("current")


class _MsanErrorDisableMacSgRecoveryStatus_Type(Integer32):
    """Custom type msanErrorDisableMacSgRecoveryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanErrorDisableMacSgRecoveryStatus_Type.__name__ = "Integer32"
_MsanErrorDisableMacSgRecoveryStatus_Object = MibScalar
msanErrorDisableMacSgRecoveryStatus = _MsanErrorDisableMacSgRecoveryStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 35, 1, 3),
    _MsanErrorDisableMacSgRecoveryStatus_Type()
)
msanErrorDisableMacSgRecoveryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanErrorDisableMacSgRecoveryStatus.setStatus("current")
_MsanErrorDisablePortTable_Object = MibTable
msanErrorDisablePortTable = _MsanErrorDisablePortTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 35, 2)
)
if mibBuilder.loadTexts:
    msanErrorDisablePortTable.setStatus("current")
_MsanErrorDisablePortEntry_Object = MibTableRow
msanErrorDisablePortEntry = _MsanErrorDisablePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 35, 2, 1)
)
msanErrorDisablePortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    msanErrorDisablePortEntry.setStatus("current")


class _MsanErrorDisablePortStatus_Type(Integer32):
    """Custom type msanErrorDisablePortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("errorDisable", 2),
          ("regular", 1))
    )


_MsanErrorDisablePortStatus_Type.__name__ = "Integer32"
_MsanErrorDisablePortStatus_Object = MibTableColumn
msanErrorDisablePortStatus = _MsanErrorDisablePortStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 35, 2, 1, 1),
    _MsanErrorDisablePortStatus_Type()
)
msanErrorDisablePortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanErrorDisablePortStatus.setStatus("current")
_MsanErrorDisablePortCause_Type = OctetString
_MsanErrorDisablePortCause_Object = MibTableColumn
msanErrorDisablePortCause = _MsanErrorDisablePortCause_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 35, 2, 1, 2),
    _MsanErrorDisablePortCause_Type()
)
msanErrorDisablePortCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanErrorDisablePortCause.setStatus("current")
_MsanErrorDisablePortTimeLeft_Type = Integer32
_MsanErrorDisablePortTimeLeft_Object = MibTableColumn
msanErrorDisablePortTimeLeft = _MsanErrorDisablePortTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 35, 2, 1, 3),
    _MsanErrorDisablePortTimeLeft_Type()
)
msanErrorDisablePortTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanErrorDisablePortTimeLeft.setStatus("current")
if mibBuilder.loadTexts:
    msanErrorDisablePortTimeLeft.setUnits("sec")
_MsanErrorDisablePortCounter_Type = Integer32
_MsanErrorDisablePortCounter_Object = MibTableColumn
msanErrorDisablePortCounter = _MsanErrorDisablePortCounter_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 35, 2, 1, 4),
    _MsanErrorDisablePortCounter_Type()
)
msanErrorDisablePortCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanErrorDisablePortCounter.setStatus("current")
_MsanAdsl_ObjectIdentity = ObjectIdentity
msanAdsl = _MsanAdsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36)
)
_MsanAdslGlobal_ObjectIdentity = ObjectIdentity
msanAdslGlobal = _MsanAdslGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 1)
)
_MsanAdslAtucPhysExtnTable_Object = MibTable
msanAdslAtucPhysExtnTable = _MsanAdslAtucPhysExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 2)
)
if mibBuilder.loadTexts:
    msanAdslAtucPhysExtnTable.setStatus("current")
_MsanAdslAtucPhysExtnEntry_Object = MibTableRow
msanAdslAtucPhysExtnEntry = _MsanAdslAtucPhysExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 2, 1)
)
msanAdslAtucPhysExtnEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    msanAdslAtucPhysExtnEntry.setStatus("current")


class _MsanAdslAtucPhysExtnOpState_Type(Integer32):
    """Custom type msanAdslAtucPhysExtnOpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              8,
              16,
              24,
              26,
              27,
              46,
              128,
              131,
              132,
              133,
              139,
              140)
        )
    )
    namedValues = NamedValues(
        *(("atmLpTest", 133),
          ("bootupLoad", 8),
          ("data", 1),
          ("delt", 140),
          ("deltTraining", 139),
          ("discovery", 46),
          ("dlTest", 131),
          ("fastRetrainInProg", 27),
          ("framerSync", 26),
          ("handshake", 16),
          ("idle", 0),
          ("llTest", 128),
          ("training", 24),
          ("txTest", 132))
    )


_MsanAdslAtucPhysExtnOpState_Type.__name__ = "Integer32"
_MsanAdslAtucPhysExtnOpState_Object = MibTableColumn
msanAdslAtucPhysExtnOpState = _MsanAdslAtucPhysExtnOpState_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 2, 1, 1),
    _MsanAdslAtucPhysExtnOpState_Type()
)
msanAdslAtucPhysExtnOpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAtucPhysExtnOpState.setStatus("current")


class _MsanAdslAtucPhysExtnActualStd_Type(Integer32):
    """Custom type msanAdslAtucPhysExtnActualStd based on Integer32"""
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
              9,
              26,
              27,
              28,
              29,
              30,
              48,
              64,
              80)
        )
    )
    namedValues = NamedValues(
        *(("adi", 5),
          ("adsl2", 26),
          ("adsl2Auto", 29),
          ("adsl2Plus", 27),
          ("adsl2PlusAuto", 30),
          ("adslPlus", 48),
          ("alctl", 6),
          ("alctl14", 3),
          ("gDmt", 2),
          ("gLite", 1),
          ("gspanPlus", 64),
          ("gspanPlusPlus", 80),
          ("multimode", 4),
          ("readsl2", 28),
          ("t1413", 0),
          ("t1413auto", 9))
    )


_MsanAdslAtucPhysExtnActualStd_Type.__name__ = "Integer32"
_MsanAdslAtucPhysExtnActualStd_Object = MibTableColumn
msanAdslAtucPhysExtnActualStd = _MsanAdslAtucPhysExtnActualStd_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 2, 1, 2),
    _MsanAdslAtucPhysExtnActualStd_Type()
)
msanAdslAtucPhysExtnActualStd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAtucPhysExtnActualStd.setStatus("current")
_MsanAdslAtucPhysExtnBertError_Type = Integer32
_MsanAdslAtucPhysExtnBertError_Object = MibTableColumn
msanAdslAtucPhysExtnBertError = _MsanAdslAtucPhysExtnBertError_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 2, 1, 3),
    _MsanAdslAtucPhysExtnBertError_Type()
)
msanAdslAtucPhysExtnBertError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAtucPhysExtnBertError.setStatus("current")
_MsanAdslAtucPhysExtnTxAtmCellCounter_Type = Counter32
_MsanAdslAtucPhysExtnTxAtmCellCounter_Object = MibTableColumn
msanAdslAtucPhysExtnTxAtmCellCounter = _MsanAdslAtucPhysExtnTxAtmCellCounter_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 2, 1, 4),
    _MsanAdslAtucPhysExtnTxAtmCellCounter_Type()
)
msanAdslAtucPhysExtnTxAtmCellCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAtucPhysExtnTxAtmCellCounter.setStatus("current")
_MsanAdslAtucPhysExtnRxAtmCellCounter_Type = Integer32
_MsanAdslAtucPhysExtnRxAtmCellCounter_Object = MibTableColumn
msanAdslAtucPhysExtnRxAtmCellCounter = _MsanAdslAtucPhysExtnRxAtmCellCounter_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 2, 1, 5),
    _MsanAdslAtucPhysExtnRxAtmCellCounter_Type()
)
msanAdslAtucPhysExtnRxAtmCellCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAtucPhysExtnRxAtmCellCounter.setStatus("current")
_MsanAdslAtucPhysExtnStartProgress_Type = Integer32
_MsanAdslAtucPhysExtnStartProgress_Object = MibTableColumn
msanAdslAtucPhysExtnStartProgress = _MsanAdslAtucPhysExtnStartProgress_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 2, 1, 6),
    _MsanAdslAtucPhysExtnStartProgress_Type()
)
msanAdslAtucPhysExtnStartProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAtucPhysExtnStartProgress.setStatus("current")
_MsanAdslAtucPhysExtnIdleBertError_Type = Integer32
_MsanAdslAtucPhysExtnIdleBertError_Object = MibTableColumn
msanAdslAtucPhysExtnIdleBertError = _MsanAdslAtucPhysExtnIdleBertError_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 2, 1, 7),
    _MsanAdslAtucPhysExtnIdleBertError_Type()
)
msanAdslAtucPhysExtnIdleBertError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAtucPhysExtnIdleBertError.setStatus("current")
_MsanAdslAtucPhysExtnIdleBertCells_Type = Integer32
_MsanAdslAtucPhysExtnIdleBertCells_Object = MibTableColumn
msanAdslAtucPhysExtnIdleBertCells = _MsanAdslAtucPhysExtnIdleBertCells_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 2, 1, 8),
    _MsanAdslAtucPhysExtnIdleBertCells_Type()
)
msanAdslAtucPhysExtnIdleBertCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAtucPhysExtnIdleBertCells.setStatus("current")


class _MsanAdslAtucPhysExtnBertSync_Type(Integer32):
    """Custom type msanAdslAtucPhysExtnBertSync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              128)
        )
    )
    namedValues = NamedValues(
        *(("bertInSync", 128),
          ("bertOutOfSync", 0))
    )


_MsanAdslAtucPhysExtnBertSync_Type.__name__ = "Integer32"
_MsanAdslAtucPhysExtnBertSync_Object = MibTableColumn
msanAdslAtucPhysExtnBertSync = _MsanAdslAtucPhysExtnBertSync_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 2, 1, 9),
    _MsanAdslAtucPhysExtnBertSync_Type()
)
msanAdslAtucPhysExtnBertSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAtucPhysExtnBertSync.setStatus("current")


class _MsanAdslAtucPhysExtnParametricTestResult_Type(Integer32):
    """Custom type msanAdslAtucPhysExtnParametricTestResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dspIfFail", 2),
          ("fail", 1),
          ("ok", 0))
    )


_MsanAdslAtucPhysExtnParametricTestResult_Type.__name__ = "Integer32"
_MsanAdslAtucPhysExtnParametricTestResult_Object = MibTableColumn
msanAdslAtucPhysExtnParametricTestResult = _MsanAdslAtucPhysExtnParametricTestResult_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 2, 1, 10),
    _MsanAdslAtucPhysExtnParametricTestResult_Type()
)
msanAdslAtucPhysExtnParametricTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAtucPhysExtnParametricTestResult.setStatus("current")


class _MsanAdslAtucPhysExtnSeltInfoValid_Type(Integer32):
    """Custom type msanAdslAtucPhysExtnSeltInfoValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              32768,
              33024,
              33280)
        )
    )
    namedValues = NamedValues(
        *(("lostConnection", 33024),
          ("noResponseSeltEngine", 33280),
          ("notConnected", 32768),
          ("true", 1))
    )


_MsanAdslAtucPhysExtnSeltInfoValid_Type.__name__ = "Integer32"
_MsanAdslAtucPhysExtnSeltInfoValid_Object = MibTableColumn
msanAdslAtucPhysExtnSeltInfoValid = _MsanAdslAtucPhysExtnSeltInfoValid_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 2, 1, 11),
    _MsanAdslAtucPhysExtnSeltInfoValid_Type()
)
msanAdslAtucPhysExtnSeltInfoValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAtucPhysExtnSeltInfoValid.setStatus("current")
_MsanAdslAtucPhysExtnSeltLoopLen_Type = Integer32
_MsanAdslAtucPhysExtnSeltLoopLen_Object = MibTableColumn
msanAdslAtucPhysExtnSeltLoopLen = _MsanAdslAtucPhysExtnSeltLoopLen_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 2, 1, 12),
    _MsanAdslAtucPhysExtnSeltLoopLen_Type()
)
msanAdslAtucPhysExtnSeltLoopLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAtucPhysExtnSeltLoopLen.setStatus("current")


class _MsanAdslAtucPhysExtnSeltLoopEnd_Type(Integer32):
    """Custom type msanAdslAtucPhysExtnSeltLoopEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 0),
          ("short", 1),
          ("unknown", 2))
    )


_MsanAdslAtucPhysExtnSeltLoopEnd_Type.__name__ = "Integer32"
_MsanAdslAtucPhysExtnSeltLoopEnd_Object = MibTableColumn
msanAdslAtucPhysExtnSeltLoopEnd = _MsanAdslAtucPhysExtnSeltLoopEnd_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 2, 1, 13),
    _MsanAdslAtucPhysExtnSeltLoopEnd_Type()
)
msanAdslAtucPhysExtnSeltLoopEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAtucPhysExtnSeltLoopEnd.setStatus("current")


class _MsanAdslAtucPhysExtnSeltLoopGauge_Type(Integer32):
    """Custom type msanAdslAtucPhysExtnSeltLoopGauge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("equal24awg", 1),
          ("equal26awg", 0),
          ("greater26awg", -1),
          ("less26awg", 2),
          ("unknownAwg", 3))
    )


_MsanAdslAtucPhysExtnSeltLoopGauge_Type.__name__ = "Integer32"
_MsanAdslAtucPhysExtnSeltLoopGauge_Object = MibTableColumn
msanAdslAtucPhysExtnSeltLoopGauge = _MsanAdslAtucPhysExtnSeltLoopGauge_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 2, 1, 14),
    _MsanAdslAtucPhysExtnSeltLoopGauge_Type()
)
msanAdslAtucPhysExtnSeltLoopGauge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAtucPhysExtnSeltLoopGauge.setStatus("current")
_MsanAdslAtucPhysExtnSeltUpShannonCap_Type = Gauge32
_MsanAdslAtucPhysExtnSeltUpShannonCap_Object = MibTableColumn
msanAdslAtucPhysExtnSeltUpShannonCap = _MsanAdslAtucPhysExtnSeltUpShannonCap_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 2, 1, 15),
    _MsanAdslAtucPhysExtnSeltUpShannonCap_Type()
)
msanAdslAtucPhysExtnSeltUpShannonCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAtucPhysExtnSeltUpShannonCap.setStatus("current")
_MsanAdslAtucPhysExtnSeltDownShannonCap_Type = Gauge32
_MsanAdslAtucPhysExtnSeltDownShannonCap_Object = MibTableColumn
msanAdslAtucPhysExtnSeltDownShannonCap = _MsanAdslAtucPhysExtnSeltDownShannonCap_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 2, 1, 16),
    _MsanAdslAtucPhysExtnSeltDownShannonCap_Type()
)
msanAdslAtucPhysExtnSeltDownShannonCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAtucPhysExtnSeltDownShannonCap.setStatus("current")


class _MsanAdslAtucPhysExtnSeltInbandNoise_Type(OctetString):
    """Custom type msanAdslAtucPhysExtnSeltInbandNoise based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_MsanAdslAtucPhysExtnSeltInbandNoise_Type.__name__ = "OctetString"
_MsanAdslAtucPhysExtnSeltInbandNoise_Object = MibTableColumn
msanAdslAtucPhysExtnSeltInbandNoise = _MsanAdslAtucPhysExtnSeltInbandNoise_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 2, 1, 17),
    _MsanAdslAtucPhysExtnSeltInbandNoise_Type()
)
msanAdslAtucPhysExtnSeltInbandNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAtucPhysExtnSeltInbandNoise.setStatus("current")


class _MsanAdslAtucPhysExtnSeltTerminationResp_Type(OctetString):
    """Custom type msanAdslAtucPhysExtnSeltTerminationResp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 720),
    )


_MsanAdslAtucPhysExtnSeltTerminationResp_Type.__name__ = "OctetString"
_MsanAdslAtucPhysExtnSeltTerminationResp_Object = MibTableColumn
msanAdslAtucPhysExtnSeltTerminationResp = _MsanAdslAtucPhysExtnSeltTerminationResp_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 2, 1, 18),
    _MsanAdslAtucPhysExtnSeltTerminationResp_Type()
)
msanAdslAtucPhysExtnSeltTerminationResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAtucPhysExtnSeltTerminationResp.setStatus("current")


class _MsanAdslAtucPhysExtnSeltUpMgnAtRate_Type(OctetString):
    """Custom type msanAdslAtucPhysExtnSeltUpMgnAtRate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1200),
    )


_MsanAdslAtucPhysExtnSeltUpMgnAtRate_Type.__name__ = "OctetString"
_MsanAdslAtucPhysExtnSeltUpMgnAtRate_Object = MibTableColumn
msanAdslAtucPhysExtnSeltUpMgnAtRate = _MsanAdslAtucPhysExtnSeltUpMgnAtRate_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 2, 1, 19),
    _MsanAdslAtucPhysExtnSeltUpMgnAtRate_Type()
)
msanAdslAtucPhysExtnSeltUpMgnAtRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAtucPhysExtnSeltUpMgnAtRate.setStatus("current")


class _MsanAdslAtucPhysExtnSeltDownMgnAtRate_Type(OctetString):
    """Custom type msanAdslAtucPhysExtnSeltDownMgnAtRate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1200),
    )


_MsanAdslAtucPhysExtnSeltDownMgnAtRate_Type.__name__ = "OctetString"
_MsanAdslAtucPhysExtnSeltDownMgnAtRate_Object = MibTableColumn
msanAdslAtucPhysExtnSeltDownMgnAtRate = _MsanAdslAtucPhysExtnSeltDownMgnAtRate_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 2, 1, 20),
    _MsanAdslAtucPhysExtnSeltDownMgnAtRate_Type()
)
msanAdslAtucPhysExtnSeltDownMgnAtRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAtucPhysExtnSeltDownMgnAtRate.setStatus("current")


class _MsanAdslAtucPhysExtnDataBoostStatus_Type(Integer32):
    """Custom type msanAdslAtucPhysExtnDataBoostStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              32768)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 32768))
    )


_MsanAdslAtucPhysExtnDataBoostStatus_Type.__name__ = "Integer32"
_MsanAdslAtucPhysExtnDataBoostStatus_Object = MibTableColumn
msanAdslAtucPhysExtnDataBoostStatus = _MsanAdslAtucPhysExtnDataBoostStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 2, 1, 21),
    _MsanAdslAtucPhysExtnDataBoostStatus_Type()
)
msanAdslAtucPhysExtnDataBoostStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAtucPhysExtnDataBoostStatus.setStatus("current")


class _MsanAdslAtucPhysExtnTestArray_Type(OctetString):
    """Custom type msanAdslAtucPhysExtnTestArray based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_MsanAdslAtucPhysExtnTestArray_Type.__name__ = "OctetString"
_MsanAdslAtucPhysExtnTestArray_Object = MibTableColumn
msanAdslAtucPhysExtnTestArray = _MsanAdslAtucPhysExtnTestArray_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 2, 1, 22),
    _MsanAdslAtucPhysExtnTestArray_Type()
)
msanAdslAtucPhysExtnTestArray.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAtucPhysExtnTestArray.setStatus("current")
_MsanAdslAtucPhysExtnChanPerfCD_Type = Integer32
_MsanAdslAtucPhysExtnChanPerfCD_Object = MibTableColumn
msanAdslAtucPhysExtnChanPerfCD = _MsanAdslAtucPhysExtnChanPerfCD_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 2, 1, 23),
    _MsanAdslAtucPhysExtnChanPerfCD_Type()
)
msanAdslAtucPhysExtnChanPerfCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAtucPhysExtnChanPerfCD.setStatus("current")
_MsanAdslAtucPhysExtnChanPerfBE_Type = Integer32
_MsanAdslAtucPhysExtnChanPerfBE_Object = MibTableColumn
msanAdslAtucPhysExtnChanPerfBE = _MsanAdslAtucPhysExtnChanPerfBE_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 2, 1, 24),
    _MsanAdslAtucPhysExtnChanPerfBE_Type()
)
msanAdslAtucPhysExtnChanPerfBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAtucPhysExtnChanPerfBE.setStatus("current")
_MsanAdslAtucPhysExtnDeltHLINSCus_Type = Integer32
_MsanAdslAtucPhysExtnDeltHLINSCus_Object = MibTableColumn
msanAdslAtucPhysExtnDeltHLINSCus = _MsanAdslAtucPhysExtnDeltHLINSCus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 2, 1, 25),
    _MsanAdslAtucPhysExtnDeltHLINSCus_Type()
)
msanAdslAtucPhysExtnDeltHLINSCus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAtucPhysExtnDeltHLINSCus.setStatus("current")


class _MsanAdslAtucPhysExtnDeltHLINpsus_Type(OctetString):
    """Custom type msanAdslAtucPhysExtnDeltHLINpsus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MsanAdslAtucPhysExtnDeltHLINpsus_Type.__name__ = "OctetString"
_MsanAdslAtucPhysExtnDeltHLINpsus_Object = MibTableColumn
msanAdslAtucPhysExtnDeltHLINpsus = _MsanAdslAtucPhysExtnDeltHLINpsus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 2, 1, 26),
    _MsanAdslAtucPhysExtnDeltHLINpsus_Type()
)
msanAdslAtucPhysExtnDeltHLINpsus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAtucPhysExtnDeltHLINpsus.setStatus("current")
_MsanAdslAtucPhysExtnDeltHLOGMTus_Type = Integer32
_MsanAdslAtucPhysExtnDeltHLOGMTus_Object = MibTableColumn
msanAdslAtucPhysExtnDeltHLOGMTus = _MsanAdslAtucPhysExtnDeltHLOGMTus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 2, 1, 27),
    _MsanAdslAtucPhysExtnDeltHLOGMTus_Type()
)
msanAdslAtucPhysExtnDeltHLOGMTus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAtucPhysExtnDeltHLOGMTus.setStatus("current")


class _MsanAdslAtucPhysExtnDeltHLOGpsus_Type(OctetString):
    """Custom type msanAdslAtucPhysExtnDeltHLOGpsus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MsanAdslAtucPhysExtnDeltHLOGpsus_Type.__name__ = "OctetString"
_MsanAdslAtucPhysExtnDeltHLOGpsus_Object = MibTableColumn
msanAdslAtucPhysExtnDeltHLOGpsus = _MsanAdslAtucPhysExtnDeltHLOGpsus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 2, 1, 28),
    _MsanAdslAtucPhysExtnDeltHLOGpsus_Type()
)
msanAdslAtucPhysExtnDeltHLOGpsus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAtucPhysExtnDeltHLOGpsus.setStatus("current")
_MsanAdslAtucPhysExtnDeltQLNMTus_Type = Integer32
_MsanAdslAtucPhysExtnDeltQLNMTus_Object = MibTableColumn
msanAdslAtucPhysExtnDeltQLNMTus = _MsanAdslAtucPhysExtnDeltQLNMTus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 2, 1, 29),
    _MsanAdslAtucPhysExtnDeltQLNMTus_Type()
)
msanAdslAtucPhysExtnDeltQLNMTus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAtucPhysExtnDeltQLNMTus.setStatus("current")


class _MsanAdslAtucPhysExtnDeltQLNpsus_Type(OctetString):
    """Custom type msanAdslAtucPhysExtnDeltQLNpsus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MsanAdslAtucPhysExtnDeltQLNpsus_Type.__name__ = "OctetString"
_MsanAdslAtucPhysExtnDeltQLNpsus_Object = MibTableColumn
msanAdslAtucPhysExtnDeltQLNpsus = _MsanAdslAtucPhysExtnDeltQLNpsus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 2, 1, 30),
    _MsanAdslAtucPhysExtnDeltQLNpsus_Type()
)
msanAdslAtucPhysExtnDeltQLNpsus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAtucPhysExtnDeltQLNpsus.setStatus("current")


class _MsanAdslAtucPhysExtnDeltLastTxState_Type(Integer32):
    """Custom type msanAdslAtucPhysExtnDeltLastTxState based on Integer32"""
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
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32)
        )
    )
    namedValues = NamedValues(
        *(("dmtatuccomb1", 2),
          ("dmtatuccomb2", 4),
          ("dmtatuccomb3", 8),
          ("dmtatucect", 16),
          ("dmtatucexchmarker", 25),
          ("dmtatucg9941", 0),
          ("dmtatucicomb1", 5),
          ("dmtatucicomb2", 9),
          ("dmtatuclineprob", 6),
          ("dmtatucmedley", 24),
          ("dmtatucmsg1", 21),
          ("dmtatucmsg2", 26),
          ("dmtatucmsgfmt", 10),
          ("dmtatucmsgpcb", 11),
          ("dmtatucparams", 29),
          ("dmtatucquiet1", 1),
          ("dmtatucquiet2", 3),
          ("dmtatucquiet3", 7),
          ("dmtatucquiet4", 12),
          ("dmtatucreverb1", 13),
          ("dmtatucreverb2", 15),
          ("dmtatucreverb3", 17),
          ("dmtatucreverb4", 19),
          ("dmtatucreverb5", 22),
          ("dmtatucreverb6", 27),
          ("dmtatucreverb7", 30),
          ("dmtatucsegue1", 20),
          ("dmtatucsegue2", 23),
          ("dmtatucsegue3", 28),
          ("dmtatucsegue4", 31),
          ("dmtatucshowtime", 32),
          ("dmtatuctref1", 14),
          ("dmtatuctref2", 18))
    )


_MsanAdslAtucPhysExtnDeltLastTxState_Type.__name__ = "Integer32"
_MsanAdslAtucPhysExtnDeltLastTxState_Object = MibTableColumn
msanAdslAtucPhysExtnDeltLastTxState = _MsanAdslAtucPhysExtnDeltLastTxState_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 2, 1, 31),
    _MsanAdslAtucPhysExtnDeltLastTxState_Type()
)
msanAdslAtucPhysExtnDeltLastTxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAtucPhysExtnDeltLastTxState.setStatus("current")


class _MsanAdslAtucPhysExtnPMState_Type(Integer32):
    """Custom type msanAdslAtucPhysExtnPMState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("l0", 0),
          ("l2", 2),
          ("l3", 3))
    )


_MsanAdslAtucPhysExtnPMState_Type.__name__ = "Integer32"
_MsanAdslAtucPhysExtnPMState_Object = MibTableColumn
msanAdslAtucPhysExtnPMState = _MsanAdslAtucPhysExtnPMState_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 2, 1, 32),
    _MsanAdslAtucPhysExtnPMState_Type()
)
msanAdslAtucPhysExtnPMState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAtucPhysExtnPMState.setStatus("current")
_MsanAdslAtucPhysExtnChanPerfCU_Type = Integer32
_MsanAdslAtucPhysExtnChanPerfCU_Object = MibTableColumn
msanAdslAtucPhysExtnChanPerfCU = _MsanAdslAtucPhysExtnChanPerfCU_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 2, 1, 33),
    _MsanAdslAtucPhysExtnChanPerfCU_Type()
)
msanAdslAtucPhysExtnChanPerfCU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAtucPhysExtnChanPerfCU.setStatus("current")
_MsanAdslAtucPhysExtnExtendedPsdStatus_Type = TruthValue
_MsanAdslAtucPhysExtnExtendedPsdStatus_Object = MibTableColumn
msanAdslAtucPhysExtnExtendedPsdStatus = _MsanAdslAtucPhysExtnExtendedPsdStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 2, 1, 34),
    _MsanAdslAtucPhysExtnExtendedPsdStatus_Type()
)
msanAdslAtucPhysExtnExtendedPsdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAtucPhysExtnExtendedPsdStatus.setStatus("current")
_MsanAdslAtucPhysExtnChipVersion_Type = Integer32
_MsanAdslAtucPhysExtnChipVersion_Object = MibTableColumn
msanAdslAtucPhysExtnChipVersion = _MsanAdslAtucPhysExtnChipVersion_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 2, 1, 35),
    _MsanAdslAtucPhysExtnChipVersion_Type()
)
msanAdslAtucPhysExtnChipVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAtucPhysExtnChipVersion.setStatus("current")
_MsanAdslAtucPhysExtnPilotTone_Type = Integer32
_MsanAdslAtucPhysExtnPilotTone_Object = MibTableColumn
msanAdslAtucPhysExtnPilotTone = _MsanAdslAtucPhysExtnPilotTone_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 2, 1, 36),
    _MsanAdslAtucPhysExtnPilotTone_Type()
)
msanAdslAtucPhysExtnPilotTone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAtucPhysExtnPilotTone.setStatus("current")
_MsanAdslAtucMSGds_Type = Gauge32
_MsanAdslAtucMSGds_Object = MibTableColumn
msanAdslAtucMSGds = _MsanAdslAtucMSGds_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 2, 1, 37),
    _MsanAdslAtucMSGds_Type()
)
msanAdslAtucMSGds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAtucMSGds.setStatus("current")


class _MsanAdslAtucPhysExtnPsdMaskMode_Type(Integer32):
    """Custom type msanAdslAtucPhysExtnPsdMaskMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              4,
              259,
              275,
              291,
              32768,
              32771,
              32772,
              49152)
        )
    )
    namedValues = NamedValues(
        *(("adsl2NonovlpFlat", 259),
          ("adsl2NonovlpM1", 275),
          ("adsl2NonovlpM2", 291),
          ("cabMsk2", 4),
          ("cabMsk2Rfi", 32772),
          ("coMsk2", 0),
          ("coMsk2Rfi", 32768),
          ("coMsk2Rfi0", 49152),
          ("flatMsk", 3),
          ("flatMskRfi", 32771))
    )


_MsanAdslAtucPhysExtnPsdMaskMode_Type.__name__ = "Integer32"
_MsanAdslAtucPhysExtnPsdMaskMode_Object = MibTableColumn
msanAdslAtucPhysExtnPsdMaskMode = _MsanAdslAtucPhysExtnPsdMaskMode_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 2, 1, 38),
    _MsanAdslAtucPhysExtnPsdMaskMode_Type()
)
msanAdslAtucPhysExtnPsdMaskMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAtucPhysExtnPsdMaskMode.setStatus("current")
_MsanAdslAtucPhysExtnDeltSNRMTus_Type = Integer32
_MsanAdslAtucPhysExtnDeltSNRMTus_Object = MibTableColumn
msanAdslAtucPhysExtnDeltSNRMTus = _MsanAdslAtucPhysExtnDeltSNRMTus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 2, 1, 39),
    _MsanAdslAtucPhysExtnDeltSNRMTus_Type()
)
msanAdslAtucPhysExtnDeltSNRMTus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAtucPhysExtnDeltSNRMTus.setStatus("current")


class _MsanAdslAtucPhysExtnDeltCurrStatus_Type(Integer32):
    """Custom type msanAdslAtucPhysExtnDeltCurrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              17,
              34,
              68,
              136,
              255)
        )
    )
    namedValues = NamedValues(
        *(("failedCrcError", 34),
          ("failedInsufficientCapacity", 17),
          ("failedTimeOut", 68),
          ("failedUnexpectedContent", 136),
          ("failedUnknown", 0),
          ("success", 255))
    )


_MsanAdslAtucPhysExtnDeltCurrStatus_Type.__name__ = "Integer32"
_MsanAdslAtucPhysExtnDeltCurrStatus_Object = MibTableColumn
msanAdslAtucPhysExtnDeltCurrStatus = _MsanAdslAtucPhysExtnDeltCurrStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 2, 1, 40),
    _MsanAdslAtucPhysExtnDeltCurrStatus_Type()
)
msanAdslAtucPhysExtnDeltCurrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAtucPhysExtnDeltCurrStatus.setStatus("current")
_MsanAdslAtucSATN_Type = Integer32
_MsanAdslAtucSATN_Object = MibTableColumn
msanAdslAtucSATN = _MsanAdslAtucSATN_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 2, 1, 41),
    _MsanAdslAtucSATN_Type()
)
msanAdslAtucSATN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAtucSATN.setStatus("current")


class _MsanAdslAtucPhysExtnSystemVendorId_Type(OctetString):
    """Custom type msanAdslAtucPhysExtnSystemVendorId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_MsanAdslAtucPhysExtnSystemVendorId_Type.__name__ = "OctetString"
_MsanAdslAtucPhysExtnSystemVendorId_Object = MibTableColumn
msanAdslAtucPhysExtnSystemVendorId = _MsanAdslAtucPhysExtnSystemVendorId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 2, 1, 42),
    _MsanAdslAtucPhysExtnSystemVendorId_Type()
)
msanAdslAtucPhysExtnSystemVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAtucPhysExtnSystemVendorId.setStatus("current")
_MsanAdslAtucPhysExtnSelfTestResult_Type = Gauge32
_MsanAdslAtucPhysExtnSelfTestResult_Object = MibTableColumn
msanAdslAtucPhysExtnSelfTestResult = _MsanAdslAtucPhysExtnSelfTestResult_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 2, 1, 43),
    _MsanAdslAtucPhysExtnSelfTestResult_Type()
)
msanAdslAtucPhysExtnSelfTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAtucPhysExtnSelfTestResult.setStatus("current")


class _MsanAdslAtucPhysExtnG9941VendorId_Type(OctetString):
    """Custom type msanAdslAtucPhysExtnG9941VendorId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_MsanAdslAtucPhysExtnG9941VendorId_Type.__name__ = "OctetString"
_MsanAdslAtucPhysExtnG9941VendorId_Object = MibTableColumn
msanAdslAtucPhysExtnG9941VendorId = _MsanAdslAtucPhysExtnG9941VendorId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 2, 1, 44),
    _MsanAdslAtucPhysExtnG9941VendorId_Type()
)
msanAdslAtucPhysExtnG9941VendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAtucPhysExtnG9941VendorId.setStatus("current")


class _MsanAdslAtucPhysExtnTsspsUs_Type(OctetString):
    """Custom type msanAdslAtucPhysExtnTsspsUs based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MsanAdslAtucPhysExtnTsspsUs_Type.__name__ = "OctetString"
_MsanAdslAtucPhysExtnTsspsUs_Object = MibTableColumn
msanAdslAtucPhysExtnTsspsUs = _MsanAdslAtucPhysExtnTsspsUs_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 2, 1, 45),
    _MsanAdslAtucPhysExtnTsspsUs_Type()
)
msanAdslAtucPhysExtnTsspsUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAtucPhysExtnTsspsUs.setStatus("current")
_MsanAdslAtucPhysExtnActPsdUs_Type = Integer32
_MsanAdslAtucPhysExtnActPsdUs_Object = MibTableColumn
msanAdslAtucPhysExtnActPsdUs = _MsanAdslAtucPhysExtnActPsdUs_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 2, 1, 46),
    _MsanAdslAtucPhysExtnActPsdUs_Type()
)
msanAdslAtucPhysExtnActPsdUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAtucPhysExtnActPsdUs.setStatus("current")


class _MsanAdslAtucPhysExtnGainspsUs_Type(OctetString):
    """Custom type msanAdslAtucPhysExtnGainspsUs based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MsanAdslAtucPhysExtnGainspsUs_Type.__name__ = "OctetString"
_MsanAdslAtucPhysExtnGainspsUs_Object = MibTableColumn
msanAdslAtucPhysExtnGainspsUs = _MsanAdslAtucPhysExtnGainspsUs_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 2, 1, 47),
    _MsanAdslAtucPhysExtnGainspsUs_Type()
)
msanAdslAtucPhysExtnGainspsUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAtucPhysExtnGainspsUs.setStatus("current")
_MsanAdslAtucPhysExtnStartBin_Type = Integer32
_MsanAdslAtucPhysExtnStartBin_Object = MibTableColumn
msanAdslAtucPhysExtnStartBin = _MsanAdslAtucPhysExtnStartBin_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 2, 1, 48),
    _MsanAdslAtucPhysExtnStartBin_Type()
)
msanAdslAtucPhysExtnStartBin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAtucPhysExtnStartBin.setStatus("current")


class _MsanAdslAtucPhysExtnStartupErrorCode_Type(Integer32):
    """Custom type msanAdslAtucPhysExtnStartupErrorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              65536,
              131072,
              262144)
        )
    )
    namedValues = NamedValues(
        *(("startupErrorCodeMaxnomAtpDs", 4),
          ("startupErrorCodeMaxnomAtpUs", 262144),
          ("startupErrorCodeMaxnomPsdDs", 1),
          ("startupErrorCodeMaxnomPsdUs", 65536),
          ("startupErrorCodeOk", 0),
          ("startupErrorCodePsdMaskDs", 2),
          ("startupErrorCodePsdMaskUs", 131072))
    )


_MsanAdslAtucPhysExtnStartupErrorCode_Type.__name__ = "Integer32"
_MsanAdslAtucPhysExtnStartupErrorCode_Object = MibTableColumn
msanAdslAtucPhysExtnStartupErrorCode = _MsanAdslAtucPhysExtnStartupErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 2, 1, 49),
    _MsanAdslAtucPhysExtnStartupErrorCode_Type()
)
msanAdslAtucPhysExtnStartupErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAtucPhysExtnStartupErrorCode.setStatus("current")
_MsanAdslAtucPhysExtnBitSwapCount_Type = Unsigned32
_MsanAdslAtucPhysExtnBitSwapCount_Object = MibTableColumn
msanAdslAtucPhysExtnBitSwapCount = _MsanAdslAtucPhysExtnBitSwapCount_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 2, 1, 50),
    _MsanAdslAtucPhysExtnBitSwapCount_Type()
)
msanAdslAtucPhysExtnBitSwapCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAtucPhysExtnBitSwapCount.setStatus("current")


class _MsanAdslAtucPhysExtnModPhase_Type(Integer32):
    """Custom type msanAdslAtucPhysExtnModPhase based on Integer32"""
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
        *(("flatRateCheck", 0),
          ("flatShowtime", 4),
          ("modRateCheck", 2),
          ("modShowtime", 3),
          ("snrMeasure", 1))
    )


_MsanAdslAtucPhysExtnModPhase_Type.__name__ = "Integer32"
_MsanAdslAtucPhysExtnModPhase_Object = MibTableColumn
msanAdslAtucPhysExtnModPhase = _MsanAdslAtucPhysExtnModPhase_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 2, 1, 51),
    _MsanAdslAtucPhysExtnModPhase_Type()
)
msanAdslAtucPhysExtnModPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAtucPhysExtnModPhase.setStatus("current")
_MsanAdslLineExtnTable_Object = MibTable
msanAdslLineExtnTable = _MsanAdslLineExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 3)
)
if mibBuilder.loadTexts:
    msanAdslLineExtnTable.setStatus("current")
_MsanAdslLineExtnEntry_Object = MibTableRow
msanAdslLineExtnEntry = _MsanAdslLineExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 3, 1)
)
msanAdslLineExtnEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    msanAdslLineExtnEntry.setStatus("current")


class _MsanAdslLineExtnAction_Type(Integer32):
    """Custom type msanAdslLineExtnAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              5,
              6,
              7,
              10,
              26,
              27,
              30,
              32,
              101,
              102,
              4134,
              8193,
              8194,
              8195,
              8196,
              8197,
              8198)
        )
    )
    namedValues = NamedValues(
        *(("abortReq", 2),
          ("analogLb", 6),
          ("atmLp", 10),
          ("digitalLb", 7),
          ("hybridLossTest", 8193),
          ("idleNoisePerBinTest", 8198),
          ("rcvFilterTest", 8195),
          ("rcvLinearityTest", 8194),
          ("rcvPowerPerBinTest", 8196),
          ("selt", 4134),
          ("shutdown", 101),
          ("spectrumCMtpr", 30),
          ("spectrumMedley", 26),
          ("spectrumPilot", 27),
          ("spectrumRMtpr", 32),
          ("spectrumReverb", 5),
          ("startup", 0),
          ("totalIdleNoiseTest", 8197),
          ("wakeup", 102))
    )


_MsanAdslLineExtnAction_Type.__name__ = "Integer32"
_MsanAdslLineExtnAction_Object = MibTableColumn
msanAdslLineExtnAction = _MsanAdslLineExtnAction_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 3, 1, 1),
    _MsanAdslLineExtnAction_Type()
)
msanAdslLineExtnAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanAdslLineExtnAction.setStatus("current")


class _MsanAdslLineExtnUtopiaL2RxAddr_Type(Integer32):
    """Custom type msanAdslLineExtnUtopiaL2RxAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_MsanAdslLineExtnUtopiaL2RxAddr_Type.__name__ = "Integer32"
_MsanAdslLineExtnUtopiaL2RxAddr_Object = MibTableColumn
msanAdslLineExtnUtopiaL2RxAddr = _MsanAdslLineExtnUtopiaL2RxAddr_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 3, 1, 2),
    _MsanAdslLineExtnUtopiaL2RxAddr_Type()
)
msanAdslLineExtnUtopiaL2RxAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslLineExtnUtopiaL2RxAddr.setStatus("current")


class _MsanAdslLineExtnUtopiaL2TxAddr_Type(Integer32):
    """Custom type msanAdslLineExtnUtopiaL2TxAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_MsanAdslLineExtnUtopiaL2TxAddr_Type.__name__ = "Integer32"
_MsanAdslLineExtnUtopiaL2TxAddr_Object = MibTableColumn
msanAdslLineExtnUtopiaL2TxAddr = _MsanAdslLineExtnUtopiaL2TxAddr_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 3, 1, 3),
    _MsanAdslLineExtnUtopiaL2TxAddr_Type()
)
msanAdslLineExtnUtopiaL2TxAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslLineExtnUtopiaL2TxAddr.setStatus("current")


class _MsanAdslLineExtnTransAtucCap_Type(Bits):
    """Custom type msanAdslLineExtnTransAtucCap based on Bits"""
    namedValues = NamedValues(
        *(("adslPlusPotsNonOverlapped", 13),
          ("adslPlusPotsOverlapped", 18),
          ("ansit1413", 0),
          ("etsi", 1),
          ("q9921GspanPlusPlusPotsNonOverlapped", 20),
          ("q9921GspanPlusPlusPotsOverlapped", 21),
          ("q9921GspanPlusPotsNonOverlapped", 31),
          ("q9921GspanPlusPotsOverlapped", 30),
          ("q9921IsdnNonOverlapped", 4),
          ("q9921PotsNonOverlapped", 2),
          ("q9921PotsOverlapped", 3),
          ("q9921isdnOverlapped", 5),
          ("q9921tcmIsdnNonOverlapped", 6),
          ("q9921tcmIsdnOverlapped", 7),
          ("q9921tcmIsdnSymmetric", 12),
          ("q9922potsNonOverlapeed", 8),
          ("q9922potsOverlapped", 9),
          ("q9922tcmIsdnNonOverlapped", 10),
          ("q9922tcmIsdnOverlapped", 11),
          ("q9923Adsl2PotsNonOverlapped", 28),
          ("q9923Adsl2PotsOverlapped", 29),
          ("q9923AnnexMPotsExtUsNonOverlapped", 56),
          ("q9923AnnexMPotsExtUsOverlapped", 57),
          ("q9923IsdnNonOverlapped", 34),
          ("q9923IsdnOverlapped", 35),
          ("q9923Readsl2PotsNonOverlapped", 23),
          ("q9923Readsl2PotsOverlapped", 22),
          ("q9925Adsl2PlusPotsNonOverlapped", 26),
          ("q9925Adsl2PlusPotsOverlapped", 27),
          ("q9925AnnexMPotsExtUsNonOverlapped", 60),
          ("q9925AnnexMPotsExtUsOverlapped", 61),
          ("q9925IsdnNonOverlapped", 42),
          ("q9925IsdnOverlapped", 43),
          ("vdslNonOverlapped", 25),
          ("vdslOverlapped", 24))
    )

_MsanAdslLineExtnTransAtucCap_Type.__name__ = "Bits"
_MsanAdslLineExtnTransAtucCap_Object = MibTableColumn
msanAdslLineExtnTransAtucCap = _MsanAdslLineExtnTransAtucCap_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 3, 1, 4),
    _MsanAdslLineExtnTransAtucCap_Type()
)
msanAdslLineExtnTransAtucCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslLineExtnTransAtucCap.setStatus("current")


class _MsanAdslLineExtnTransAtucActual_Type(Bits):
    """Custom type msanAdslLineExtnTransAtucActual based on Bits"""
    namedValues = NamedValues(
        *(("adslPlusPotsNonOverlapped", 13),
          ("adslPlusPotsOverlapped", 18),
          ("ansit1413", 0),
          ("etsi", 1),
          ("q9921GspanPlusPlusPotsNonOverlapped", 20),
          ("q9921GspanPlusPlusPotsOverlapped", 21),
          ("q9921GspanPlusPotsNonOverlapped", 31),
          ("q9921GspanPlusPotsOverlapped", 30),
          ("q9921IsdnNonOverlapped", 4),
          ("q9921PotsNonOverlapped", 2),
          ("q9921PotsOverlapped", 3),
          ("q9921isdnOverlapped", 5),
          ("q9921tcmIsdnNonOverlapped", 6),
          ("q9921tcmIsdnOverlapped", 7),
          ("q9921tcmIsdnSymmetric", 12),
          ("q9922potsNonOverlapeed", 8),
          ("q9922potsOverlapped", 9),
          ("q9922tcmIsdnNonOverlapped", 10),
          ("q9922tcmIsdnOverlapped", 11),
          ("q9923Adsl2PotsNonOverlapped", 28),
          ("q9923Adsl2PotsOverlapped", 29),
          ("q9923AnnexMPotsExtUsNonOverlapped", 56),
          ("q9923AnnexMPotsExtUsOverlapped", 57),
          ("q9923IsdnNonOverlapped", 34),
          ("q9923IsdnOverlapped", 35),
          ("q9923Readsl2PotsNonOverlapped", 23),
          ("q9923Readsl2PotsOverlapped", 22),
          ("q9925Adsl2PlusPotsNonOverlapped", 26),
          ("q9925Adsl2PlusPotsOverlapped", 27),
          ("q9925AnnexMPotsExtUsNonOverlapped", 60),
          ("q9925AnnexMPotsExtUsOverlapped", 61),
          ("q9925IsdnNonOverlapped", 42),
          ("q9925IsdnOverlapped", 43),
          ("vdslNonOverlapped", 25),
          ("vdslOverlapped", 24))
    )

_MsanAdslLineExtnTransAtucActual_Type.__name__ = "Bits"
_MsanAdslLineExtnTransAtucActual_Object = MibTableColumn
msanAdslLineExtnTransAtucActual = _MsanAdslLineExtnTransAtucActual_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 3, 1, 5),
    _MsanAdslLineExtnTransAtucActual_Type()
)
msanAdslLineExtnTransAtucActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslLineExtnTransAtucActual.setStatus("current")


class _MsanAdslLineExtnClockType_Type(Integer32):
    """Custom type msanAdslLineExtnClockType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4)
        )
    )
    namedValues = NamedValues(
        *(("crystal", 4),
          ("oscillator", 0))
    )


_MsanAdslLineExtnClockType_Type.__name__ = "Integer32"
_MsanAdslLineExtnClockType_Object = MibTableColumn
msanAdslLineExtnClockType = _MsanAdslLineExtnClockType_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 3, 1, 6),
    _MsanAdslLineExtnClockType_Type()
)
msanAdslLineExtnClockType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslLineExtnClockType.setStatus("current")


class _MsanAdslLineExtnLineDmtTrellis_Type(Integer32):
    """Custom type msanAdslLineExtnLineDmtTrellis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("trellisOff", 2),
          ("trellisOn", 1))
    )


_MsanAdslLineExtnLineDmtTrellis_Type.__name__ = "Integer32"
_MsanAdslLineExtnLineDmtTrellis_Object = MibTableColumn
msanAdslLineExtnLineDmtTrellis = _MsanAdslLineExtnLineDmtTrellis_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 3, 1, 7),
    _MsanAdslLineExtnLineDmtTrellis_Type()
)
msanAdslLineExtnLineDmtTrellis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslLineExtnLineDmtTrellis.setStatus("current")


class _MsanAdslLineExtnTransAturCap_Type(Bits):
    """Custom type msanAdslLineExtnTransAturCap based on Bits"""
    namedValues = NamedValues(
        *(("adslPlusPotsNonOverlapped", 13),
          ("adslPlusPotsOverlapped", 18),
          ("ansit1413", 0),
          ("etsi", 1),
          ("q9921GspanPlusPlusPotsNonOverlapped", 20),
          ("q9921GspanPlusPlusPotsOverlapped", 21),
          ("q9921GspanPlusPotsNonOverlapped", 31),
          ("q9921GspanPlusPotsOverlapped", 30),
          ("q9921IsdnNonOverlapped", 4),
          ("q9921PotsNonOverlapped", 2),
          ("q9921PotsOverlapped", 3),
          ("q9921isdnOverlapped", 5),
          ("q9921tcmIsdnNonOverlapped", 6),
          ("q9921tcmIsdnOverlapped", 7),
          ("q9921tcmIsdnSymmetric", 12),
          ("q9922potsNonOverlapeed", 8),
          ("q9922potsOverlapped", 9),
          ("q9922tcmIsdnNonOverlapped", 10),
          ("q9922tcmIsdnOverlapped", 11),
          ("q9923Adsl2PotsNonOverlapped", 28),
          ("q9923Adsl2PotsOverlapped", 29),
          ("q9923AnnexMPotsExtUsNonOverlapped", 56),
          ("q9923AnnexMPotsExtUsOverlapped", 57),
          ("q9923IsdnNonOverlapped", 34),
          ("q9923IsdnOverlapped", 35),
          ("q9923Readsl2PotsNonOverlapped", 23),
          ("q9923Readsl2PotsOverlapped", 22),
          ("q9925Adsl2PlusPotsNonOverlapped", 26),
          ("q9925Adsl2PlusPotsOverlapped", 27),
          ("q9925AnnexMPotsExtUsNonOverlapped", 60),
          ("q9925AnnexMPotsExtUsOverlapped", 61),
          ("q9925IsdnNonOverlapped", 42),
          ("q9925IsdnOverlapped", 43),
          ("vdslNonOverlapped", 25),
          ("vdslOverlapped", 24))
    )

_MsanAdslLineExtnTransAturCap_Type.__name__ = "Bits"
_MsanAdslLineExtnTransAturCap_Object = MibTableColumn
msanAdslLineExtnTransAturCap = _MsanAdslLineExtnTransAturCap_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 3, 1, 8),
    _MsanAdslLineExtnTransAturCap_Type()
)
msanAdslLineExtnTransAturCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslLineExtnTransAturCap.setStatus("current")


class _MsanAdslLineExtnPMConfPMSF_Type(Integer32):
    """Custom type msanAdslLineExtnPMConfPMSF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("l0ToL2StateForce", 2),
          ("l2ToL0StateForce", 4),
          ("l3StateForce", 3),
          ("l3ToL0StateForce", 0))
    )


_MsanAdslLineExtnPMConfPMSF_Type.__name__ = "Integer32"
_MsanAdslLineExtnPMConfPMSF_Object = MibTableColumn
msanAdslLineExtnPMConfPMSF = _MsanAdslLineExtnPMConfPMSF_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 3, 1, 9),
    _MsanAdslLineExtnPMConfPMSF_Type()
)
msanAdslLineExtnPMConfPMSF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanAdslLineExtnPMConfPMSF.setStatus("current")


class _MsanAdslLineExtnDeltConfLDSF_Type(Integer32):
    """Custom type msanAdslLineExtnDeltConfLDSF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("force", 1),
          ("inhibit", 0))
    )


_MsanAdslLineExtnDeltConfLDSF_Type.__name__ = "Integer32"
_MsanAdslLineExtnDeltConfLDSF_Object = MibTableColumn
msanAdslLineExtnDeltConfLDSF = _MsanAdslLineExtnDeltConfLDSF_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 3, 1, 10),
    _MsanAdslLineExtnDeltConfLDSF_Type()
)
msanAdslLineExtnDeltConfLDSF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanAdslLineExtnDeltConfLDSF.setStatus("current")


class _MsanAdslLineExtnTransAtucConfig_Type(Bits):
    """Custom type msanAdslLineExtnTransAtucConfig based on Bits"""
    namedValues = NamedValues(
        *(("adslPlusPotsNonOverlapped", 13),
          ("adslPlusPotsOverlapped", 18),
          ("ansit1413", 0),
          ("etsi", 1),
          ("q9921GspanPlusPlusPotsNonOverlapped", 20),
          ("q9921GspanPlusPlusPotsOverlapped", 21),
          ("q9921GspanPlusPotsNonOverlapped", 31),
          ("q9921GspanPlusPotsOverlapped", 30),
          ("q9921IsdnNonOverlapped", 4),
          ("q9921PotsNonOverlapped", 2),
          ("q9921PotsOverlapped", 3),
          ("q9921isdnOverlapped", 5),
          ("q9921tcmIsdnNonOverlapped", 6),
          ("q9921tcmIsdnOverlapped", 7),
          ("q9921tcmIsdnSymmetric", 12),
          ("q9922potsNonOverlapeed", 8),
          ("q9922potsOverlapped", 9),
          ("q9922tcmIsdnNonOverlapped", 10),
          ("q9922tcmIsdnOverlapped", 11),
          ("q9923Adsl2PotsNonOverlapped", 28),
          ("q9923Adsl2PotsOverlapped", 29),
          ("q9923AnnexMPotsExtUsNonOverlapped", 56),
          ("q9923AnnexMPotsExtUsOverlapped", 57),
          ("q9923IsdnNonOverlapped", 34),
          ("q9923IsdnOverlapped", 35),
          ("q9923Readsl2PotsNonOverlapped", 23),
          ("q9923Readsl2PotsOverlapped", 22),
          ("q9925Adsl2PlusPotsNonOverlapped", 26),
          ("q9925Adsl2PlusPotsOverlapped", 27),
          ("q9925AnnexMPotsExtUsNonOverlapped", 60),
          ("q9925AnnexMPotsExtUsOverlapped", 61),
          ("q9925IsdnNonOverlapped", 42),
          ("q9925IsdnOverlapped", 43))
    )

_MsanAdslLineExtnTransAtucConfig_Type.__name__ = "Bits"
_MsanAdslLineExtnTransAtucConfig_Object = MibTableColumn
msanAdslLineExtnTransAtucConfig = _MsanAdslLineExtnTransAtucConfig_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 3, 1, 11),
    _MsanAdslLineExtnTransAtucConfig_Type()
)
msanAdslLineExtnTransAtucConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanAdslLineExtnTransAtucConfig.setStatus("current")
_MsanAdslLineExtnAtucCurrOutputPwr_Type = Integer32
_MsanAdslLineExtnAtucCurrOutputPwr_Object = MibTableColumn
msanAdslLineExtnAtucCurrOutputPwr = _MsanAdslLineExtnAtucCurrOutputPwr_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 3, 1, 12),
    _MsanAdslLineExtnAtucCurrOutputPwr_Type()
)
msanAdslLineExtnAtucCurrOutputPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslLineExtnAtucCurrOutputPwr.setStatus("current")


class _MsanAdslLineExtnAtucBinSNRMargin_Type(OctetString):
    """Custom type msanAdslLineExtnAtucBinSNRMargin based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MsanAdslLineExtnAtucBinSNRMargin_Type.__name__ = "OctetString"
_MsanAdslLineExtnAtucBinSNRMargin_Object = MibTableColumn
msanAdslLineExtnAtucBinSNRMargin = _MsanAdslLineExtnAtucBinSNRMargin_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 3, 1, 13),
    _MsanAdslLineExtnAtucBinSNRMargin_Type()
)
msanAdslLineExtnAtucBinSNRMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslLineExtnAtucBinSNRMargin.setStatus("current")


class _MsanAdslLineExtnUtopiaL2RxAddrSecond_Type(Integer32):
    """Custom type msanAdslLineExtnUtopiaL2RxAddrSecond based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_MsanAdslLineExtnUtopiaL2RxAddrSecond_Type.__name__ = "Integer32"
_MsanAdslLineExtnUtopiaL2RxAddrSecond_Object = MibTableColumn
msanAdslLineExtnUtopiaL2RxAddrSecond = _MsanAdslLineExtnUtopiaL2RxAddrSecond_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 3, 1, 14),
    _MsanAdslLineExtnUtopiaL2RxAddrSecond_Type()
)
msanAdslLineExtnUtopiaL2RxAddrSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslLineExtnUtopiaL2RxAddrSecond.setStatus("current")


class _MsanAdslLineExtnUtopiaL2TxAddrSecond_Type(Integer32):
    """Custom type msanAdslLineExtnUtopiaL2TxAddrSecond based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_MsanAdslLineExtnUtopiaL2TxAddrSecond_Type.__name__ = "Integer32"
_MsanAdslLineExtnUtopiaL2TxAddrSecond_Object = MibTableColumn
msanAdslLineExtnUtopiaL2TxAddrSecond = _MsanAdslLineExtnUtopiaL2TxAddrSecond_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 3, 1, 15),
    _MsanAdslLineExtnUtopiaL2TxAddrSecond_Type()
)
msanAdslLineExtnUtopiaL2TxAddrSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslLineExtnUtopiaL2TxAddrSecond.setStatus("current")


class _MsanAdslLineExtnDsBinSnrUpdate_Type(Integer32):
    """Custom type msanAdslLineExtnDsBinSnrUpdate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_MsanAdslLineExtnDsBinSnrUpdate_Type.__name__ = "Integer32"
_MsanAdslLineExtnDsBinSnrUpdate_Object = MibTableColumn
msanAdslLineExtnDsBinSnrUpdate = _MsanAdslLineExtnDsBinSnrUpdate_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 3, 1, 16),
    _MsanAdslLineExtnDsBinSnrUpdate_Type()
)
msanAdslLineExtnDsBinSnrUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanAdslLineExtnDsBinSnrUpdate.setStatus("current")


class _MsanAdslLineExtnServiceType_Type(Integer32):
    """Custom type msanAdslLineExtnServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("adsl2", 7),
          ("adsl2AutoAnnexM", 9),
          ("adsl2plus", 6),
          ("adsl2plusAutoAnnexM", 8),
          ("gDmt", 4),
          ("multimode", 1),
          ("reAdsl2", 10),
          ("reserved", 2),
          ("t1413", 3))
    )


_MsanAdslLineExtnServiceType_Type.__name__ = "Integer32"
_MsanAdslLineExtnServiceType_Object = MibTableColumn
msanAdslLineExtnServiceType = _MsanAdslLineExtnServiceType_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 3, 1, 17),
    _MsanAdslLineExtnServiceType_Type()
)
msanAdslLineExtnServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslLineExtnServiceType.setStatus("current")
_MsanAdslAturPhysExtnTable_Object = MibTable
msanAdslAturPhysExtnTable = _MsanAdslAturPhysExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 4)
)
if mibBuilder.loadTexts:
    msanAdslAturPhysExtnTable.setStatus("current")
_MsanAdslAturPhysExtnEntry_Object = MibTableRow
msanAdslAturPhysExtnEntry = _MsanAdslAturPhysExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 4, 1)
)
msanAdslAturPhysExtnEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    msanAdslAturPhysExtnEntry.setStatus("current")


class _MsanAdslAturPhysExtnConfig_Type(OctetString):
    """Custom type msanAdslAturPhysExtnConfig based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_MsanAdslAturPhysExtnConfig_Type.__name__ = "OctetString"
_MsanAdslAturPhysExtnConfig_Object = MibTableColumn
msanAdslAturPhysExtnConfig = _MsanAdslAturPhysExtnConfig_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 4, 1, 1),
    _MsanAdslAturPhysExtnConfig_Type()
)
msanAdslAturPhysExtnConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAturPhysExtnConfig.setStatus("current")
_MsanAdslAturPhysExtnChanPerfCD_Type = Integer32
_MsanAdslAturPhysExtnChanPerfCD_Object = MibTableColumn
msanAdslAturPhysExtnChanPerfCD = _MsanAdslAturPhysExtnChanPerfCD_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 4, 1, 2),
    _MsanAdslAturPhysExtnChanPerfCD_Type()
)
msanAdslAturPhysExtnChanPerfCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAturPhysExtnChanPerfCD.setStatus("current")
_MsanAdslAturPhysExtnChanPerfCU_Type = Integer32
_MsanAdslAturPhysExtnChanPerfCU_Object = MibTableColumn
msanAdslAturPhysExtnChanPerfCU = _MsanAdslAturPhysExtnChanPerfCU_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 4, 1, 3),
    _MsanAdslAturPhysExtnChanPerfCU_Type()
)
msanAdslAturPhysExtnChanPerfCU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAturPhysExtnChanPerfCU.setStatus("current")
_MsanAdslAturPhysExtnChanPerfBE_Type = Integer32
_MsanAdslAturPhysExtnChanPerfBE_Object = MibTableColumn
msanAdslAturPhysExtnChanPerfBE = _MsanAdslAturPhysExtnChanPerfBE_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 4, 1, 4),
    _MsanAdslAturPhysExtnChanPerfBE_Type()
)
msanAdslAturPhysExtnChanPerfBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAturPhysExtnChanPerfBE.setStatus("current")
_MsanAdslAturPhysExtnDeltHLINSCds_Type = Integer32
_MsanAdslAturPhysExtnDeltHLINSCds_Object = MibTableColumn
msanAdslAturPhysExtnDeltHLINSCds = _MsanAdslAturPhysExtnDeltHLINSCds_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 4, 1, 5),
    _MsanAdslAturPhysExtnDeltHLINSCds_Type()
)
msanAdslAturPhysExtnDeltHLINSCds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAturPhysExtnDeltHLINSCds.setStatus("current")


class _MsanAdslAturPhysExtnDeltHLINpsds_Type(OctetString):
    """Custom type msanAdslAturPhysExtnDeltHLINpsds based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )


_MsanAdslAturPhysExtnDeltHLINpsds_Type.__name__ = "OctetString"
_MsanAdslAturPhysExtnDeltHLINpsds_Object = MibTableColumn
msanAdslAturPhysExtnDeltHLINpsds = _MsanAdslAturPhysExtnDeltHLINpsds_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 4, 1, 6),
    _MsanAdslAturPhysExtnDeltHLINpsds_Type()
)
msanAdslAturPhysExtnDeltHLINpsds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAturPhysExtnDeltHLINpsds.setStatus("current")
_MsanAdslAturPhysExtnDeltHLOGMTds_Type = Integer32
_MsanAdslAturPhysExtnDeltHLOGMTds_Object = MibTableColumn
msanAdslAturPhysExtnDeltHLOGMTds = _MsanAdslAturPhysExtnDeltHLOGMTds_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 4, 1, 7),
    _MsanAdslAturPhysExtnDeltHLOGMTds_Type()
)
msanAdslAturPhysExtnDeltHLOGMTds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAturPhysExtnDeltHLOGMTds.setStatus("current")


class _MsanAdslAturPhysExtnDeltHLOGpsus_Type(OctetString):
    """Custom type msanAdslAturPhysExtnDeltHLOGpsus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_MsanAdslAturPhysExtnDeltHLOGpsus_Type.__name__ = "OctetString"
_MsanAdslAturPhysExtnDeltHLOGpsus_Object = MibTableColumn
msanAdslAturPhysExtnDeltHLOGpsus = _MsanAdslAturPhysExtnDeltHLOGpsus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 4, 1, 8),
    _MsanAdslAturPhysExtnDeltHLOGpsus_Type()
)
msanAdslAturPhysExtnDeltHLOGpsus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAturPhysExtnDeltHLOGpsus.setStatus("current")
_MsanAdslAturPhysExtnDeltQLNMTds_Type = Integer32
_MsanAdslAturPhysExtnDeltQLNMTds_Object = MibTableColumn
msanAdslAturPhysExtnDeltQLNMTds = _MsanAdslAturPhysExtnDeltQLNMTds_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 4, 1, 9),
    _MsanAdslAturPhysExtnDeltQLNMTds_Type()
)
msanAdslAturPhysExtnDeltQLNMTds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAturPhysExtnDeltQLNMTds.setStatus("current")


class _MsanAdslAturPhysExtnDeltQLNpsds_Type(OctetString):
    """Custom type msanAdslAturPhysExtnDeltQLNpsds based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_MsanAdslAturPhysExtnDeltQLNpsds_Type.__name__ = "OctetString"
_MsanAdslAturPhysExtnDeltQLNpsds_Object = MibTableColumn
msanAdslAturPhysExtnDeltQLNpsds = _MsanAdslAturPhysExtnDeltQLNpsds_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 4, 1, 10),
    _MsanAdslAturPhysExtnDeltQLNpsds_Type()
)
msanAdslAturPhysExtnDeltQLNpsds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAturPhysExtnDeltQLNpsds.setStatus("current")


class _MsanAdslAturPhysExtnDeltLastTxState_Type(Integer32):
    """Custom type msanAdslAturPhysExtnDeltLastTxState based on Integer32"""
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
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("dmtaturcomb1", 2),
          ("dmtaturcomb2", 4),
          ("dmtaturcomb3", 8),
          ("dmtaturect", 17),
          ("dmtaturexchmarker", 24),
          ("dmtaturg9941", 0),
          ("dmtaturicomb1", 5),
          ("dmtaturicomb2", 9),
          ("dmtaturlineprob", 6),
          ("dmtaturmedley", 23),
          ("dmtaturmsg1", 22),
          ("dmtaturmsg2", 25),
          ("dmtaturmsgfmt", 10),
          ("dmtaturmsgpcb", 11),
          ("dmtaturparams", 28),
          ("dmtaturquiet1", 1),
          ("dmtaturquiet2", 3),
          ("dmtaturquiet3", 7),
          ("dmtaturquiet4", 13),
          ("dmtaturquiet5", 15),
          ("dmtaturreverb1", 12),
          ("dmtaturreverb2", 14),
          ("dmtaturreverb3", 16),
          ("dmtaturreverb4", 18),
          ("dmtaturreverb5", 20),
          ("dmtaturreverb6", 26),
          ("dmtaturreverb7", 29),
          ("dmtatursegue1", 19),
          ("dmtatursegue2", 21),
          ("dmtatursegue3", 27),
          ("dmtatursegue4", 30),
          ("dmtaturshowtime", 31))
    )


_MsanAdslAturPhysExtnDeltLastTxState_Type.__name__ = "Integer32"
_MsanAdslAturPhysExtnDeltLastTxState_Object = MibTableColumn
msanAdslAturPhysExtnDeltLastTxState = _MsanAdslAturPhysExtnDeltLastTxState_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 4, 1, 11),
    _MsanAdslAturPhysExtnDeltLastTxState_Type()
)
msanAdslAturPhysExtnDeltLastTxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAturPhysExtnDeltLastTxState.setStatus("current")
_MsanAdslAturMSGus_Type = Gauge32
_MsanAdslAturMSGus_Object = MibTableColumn
msanAdslAturMSGus = _MsanAdslAturMSGus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 4, 1, 12),
    _MsanAdslAturMSGus_Type()
)
msanAdslAturMSGus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAturMSGus.setStatus("current")
_MsanAdslAturDeltSNRMTds_Type = Gauge32
_MsanAdslAturDeltSNRMTds_Object = MibTableColumn
msanAdslAturDeltSNRMTds = _MsanAdslAturDeltSNRMTds_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 4, 1, 13),
    _MsanAdslAturDeltSNRMTds_Type()
)
msanAdslAturDeltSNRMTds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAturDeltSNRMTds.setStatus("current")
_MsanAdslAturSATN_Type = Integer32
_MsanAdslAturSATN_Object = MibTableColumn
msanAdslAturSATN = _MsanAdslAturSATN_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 4, 1, 14),
    _MsanAdslAturSATN_Type()
)
msanAdslAturSATN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAturSATN.setStatus("current")


class _MsanAdslAturPhysExtnSystemVendorId_Type(OctetString):
    """Custom type msanAdslAturPhysExtnSystemVendorId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_MsanAdslAturPhysExtnSystemVendorId_Type.__name__ = "OctetString"
_MsanAdslAturPhysExtnSystemVendorId_Object = MibTableColumn
msanAdslAturPhysExtnSystemVendorId = _MsanAdslAturPhysExtnSystemVendorId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 4, 1, 15),
    _MsanAdslAturPhysExtnSystemVendorId_Type()
)
msanAdslAturPhysExtnSystemVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAturPhysExtnSystemVendorId.setStatus("current")


class _MsanAdslAturPhysExtnGainspsDs_Type(OctetString):
    """Custom type msanAdslAturPhysExtnGainspsDs based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_MsanAdslAturPhysExtnGainspsDs_Type.__name__ = "OctetString"
_MsanAdslAturPhysExtnGainspsDs_Object = MibTableColumn
msanAdslAturPhysExtnGainspsDs = _MsanAdslAturPhysExtnGainspsDs_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 4, 1, 16),
    _MsanAdslAturPhysExtnGainspsDs_Type()
)
msanAdslAturPhysExtnGainspsDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAturPhysExtnGainspsDs.setStatus("current")
_MsanAdslAturPhysExtnSelfTestResult_Type = Gauge32
_MsanAdslAturPhysExtnSelfTestResult_Object = MibTableColumn
msanAdslAturPhysExtnSelfTestResult = _MsanAdslAturPhysExtnSelfTestResult_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 4, 1, 17),
    _MsanAdslAturPhysExtnSelfTestResult_Type()
)
msanAdslAturPhysExtnSelfTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAturPhysExtnSelfTestResult.setStatus("current")


class _MsanAdslAturPhysExtnG9941VendorId_Type(OctetString):
    """Custom type msanAdslAturPhysExtnG9941VendorId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_MsanAdslAturPhysExtnG9941VendorId_Type.__name__ = "OctetString"
_MsanAdslAturPhysExtnG9941VendorId_Object = MibTableColumn
msanAdslAturPhysExtnG9941VendorId = _MsanAdslAturPhysExtnG9941VendorId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 4, 1, 18),
    _MsanAdslAturPhysExtnG9941VendorId_Type()
)
msanAdslAturPhysExtnG9941VendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAturPhysExtnG9941VendorId.setStatus("current")


class _MsanAdslAturPhysExtnTsspsDs_Type(OctetString):
    """Custom type msanAdslAturPhysExtnTsspsDs based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MsanAdslAturPhysExtnTsspsDs_Type.__name__ = "OctetString"
_MsanAdslAturPhysExtnTsspsDs_Object = MibTableColumn
msanAdslAturPhysExtnTsspsDs = _MsanAdslAturPhysExtnTsspsDs_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 4, 1, 19),
    _MsanAdslAturPhysExtnTsspsDs_Type()
)
msanAdslAturPhysExtnTsspsDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAturPhysExtnTsspsDs.setStatus("current")
_MsanAdslAturPhysExtnActPsdDs_Type = Integer32
_MsanAdslAturPhysExtnActPsdDs_Object = MibTableColumn
msanAdslAturPhysExtnActPsdDs = _MsanAdslAturPhysExtnActPsdDs_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 4, 1, 20),
    _MsanAdslAturPhysExtnActPsdDs_Type()
)
msanAdslAturPhysExtnActPsdDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAturPhysExtnActPsdDs.setStatus("current")
_MsanAdslAturPhysExtnBitSwapCount_Type = Unsigned32
_MsanAdslAturPhysExtnBitSwapCount_Object = MibTableColumn
msanAdslAturPhysExtnBitSwapCount = _MsanAdslAturPhysExtnBitSwapCount_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 4, 1, 21),
    _MsanAdslAturPhysExtnBitSwapCount_Type()
)
msanAdslAturPhysExtnBitSwapCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAturPhysExtnBitSwapCount.setStatus("current")


class _MsanAdslAturPhysExtnPsdMaskMode_Type(Integer32):
    """Custom type msanAdslAturPhysExtnPsdMaskMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              4,
              259,
              275,
              291,
              32768,
              32771,
              32772,
              49152)
        )
    )
    namedValues = NamedValues(
        *(("adsl2NonovlpFlat", 259),
          ("adsl2NonovlpM1", 275),
          ("adsl2NonovlpM2", 291),
          ("cabMsk2", 4),
          ("cabMsk2Rfi", 32772),
          ("coMsk2", 0),
          ("coMsk2Rfi", 32768),
          ("coMsk2Rfi0", 49152),
          ("flatMsk", 3),
          ("flatMskRfi", 32771))
    )


_MsanAdslAturPhysExtnPsdMaskMode_Type.__name__ = "Integer32"
_MsanAdslAturPhysExtnPsdMaskMode_Object = MibTableColumn
msanAdslAturPhysExtnPsdMaskMode = _MsanAdslAturPhysExtnPsdMaskMode_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 36, 4, 1, 22),
    _MsanAdslAturPhysExtnPsdMaskMode_Type()
)
msanAdslAturPhysExtnPsdMaskMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanAdslAturPhysExtnPsdMaskMode.setStatus("current")
_MsanEaps_ObjectIdentity = ObjectIdentity
msanEaps = _MsanEaps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 37)
)
_MsanEapsGlobal_ObjectIdentity = ObjectIdentity
msanEapsGlobal = _MsanEapsGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 37, 1)
)


class _MsanEapsAdminState_Type(Integer32):
    """Custom type msanEapsAdminState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanEapsAdminState_Type.__name__ = "Integer32"
_MsanEapsAdminState_Object = MibScalar
msanEapsAdminState = _MsanEapsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 37, 1, 1),
    _MsanEapsAdminState_Type()
)
msanEapsAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanEapsAdminState.setStatus("current")
_MsanEapsDomainTable_Object = MibTable
msanEapsDomainTable = _MsanEapsDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 37, 2)
)
if mibBuilder.loadTexts:
    msanEapsDomainTable.setStatus("current")
_MsanEapsDomainEntry_Object = MibTableRow
msanEapsDomainEntry = _MsanEapsDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 37, 2, 1)
)
msanEapsDomainEntry.setIndexNames(
    (0, "ISKRATEL-MSAN-MIB", "msanEapsDomainName"),
)
if mibBuilder.loadTexts:
    msanEapsDomainEntry.setStatus("current")


class _MsanEapsDomainName_Type(OctetString):
    """Custom type msanEapsDomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_MsanEapsDomainName_Type.__name__ = "OctetString"
_MsanEapsDomainName_Object = MibTableColumn
msanEapsDomainName = _MsanEapsDomainName_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 37, 2, 1, 2),
    _MsanEapsDomainName_Type()
)
msanEapsDomainName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanEapsDomainName.setStatus("current")


class _MsanEapsDomainDeviceRole_Type(Integer32):
    """Custom type msanEapsDomainDeviceRole based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("transit", 2))
    )


_MsanEapsDomainDeviceRole_Type.__name__ = "Integer32"
_MsanEapsDomainDeviceRole_Object = MibTableColumn
msanEapsDomainDeviceRole = _MsanEapsDomainDeviceRole_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 37, 2, 1, 3),
    _MsanEapsDomainDeviceRole_Type()
)
msanEapsDomainDeviceRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanEapsDomainDeviceRole.setStatus("current")


class _MsanEapsDomainHelloTime_Type(Integer32):
    """Custom type msanEapsDomainHelloTime based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_MsanEapsDomainHelloTime_Type.__name__ = "Integer32"
_MsanEapsDomainHelloTime_Object = MibTableColumn
msanEapsDomainHelloTime = _MsanEapsDomainHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 37, 2, 1, 4),
    _MsanEapsDomainHelloTime_Type()
)
msanEapsDomainHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanEapsDomainHelloTime.setStatus("current")


class _MsanEapsDomainFailTimeout_Type(Integer32):
    """Custom type msanEapsDomainFailTimeout based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 300),
    )


_MsanEapsDomainFailTimeout_Type.__name__ = "Integer32"
_MsanEapsDomainFailTimeout_Object = MibTableColumn
msanEapsDomainFailTimeout = _MsanEapsDomainFailTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 37, 2, 1, 5),
    _MsanEapsDomainFailTimeout_Type()
)
msanEapsDomainFailTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanEapsDomainFailTimeout.setStatus("current")


class _MsanEapsDomainAdminState_Type(Integer32):
    """Custom type msanEapsDomainAdminState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanEapsDomainAdminState_Type.__name__ = "Integer32"
_MsanEapsDomainAdminState_Object = MibTableColumn
msanEapsDomainAdminState = _MsanEapsDomainAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 37, 2, 1, 6),
    _MsanEapsDomainAdminState_Type()
)
msanEapsDomainAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanEapsDomainAdminState.setStatus("current")
_MsanEapsDomainPrimaryIfIndex_Type = Integer32
_MsanEapsDomainPrimaryIfIndex_Object = MibTableColumn
msanEapsDomainPrimaryIfIndex = _MsanEapsDomainPrimaryIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 37, 2, 1, 7),
    _MsanEapsDomainPrimaryIfIndex_Type()
)
msanEapsDomainPrimaryIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanEapsDomainPrimaryIfIndex.setStatus("current")
_MsanEapsDomainSecondaryIfIndex_Type = Integer32
_MsanEapsDomainSecondaryIfIndex_Object = MibTableColumn
msanEapsDomainSecondaryIfIndex = _MsanEapsDomainSecondaryIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 37, 2, 1, 8),
    _MsanEapsDomainSecondaryIfIndex_Type()
)
msanEapsDomainSecondaryIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanEapsDomainSecondaryIfIndex.setStatus("current")
_MsanEapsDomainCntrlVlanId_Type = Integer32
_MsanEapsDomainCntrlVlanId_Object = MibTableColumn
msanEapsDomainCntrlVlanId = _MsanEapsDomainCntrlVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 37, 2, 1, 9),
    _MsanEapsDomainCntrlVlanId_Type()
)
msanEapsDomainCntrlVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanEapsDomainCntrlVlanId.setStatus("current")
_MsanEapsDomainRowStatus_Type = RowStatus
_MsanEapsDomainRowStatus_Object = MibTableColumn
msanEapsDomainRowStatus = _MsanEapsDomainRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 37, 2, 1, 10),
    _MsanEapsDomainRowStatus_Type()
)
msanEapsDomainRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanEapsDomainRowStatus.setStatus("current")
_MsanEapsDomainProtVlanTable_Object = MibTable
msanEapsDomainProtVlanTable = _MsanEapsDomainProtVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 37, 3)
)
if mibBuilder.loadTexts:
    msanEapsDomainProtVlanTable.setStatus("current")
_MsanEapsDomainProtVlanEntry_Object = MibTableRow
msanEapsDomainProtVlanEntry = _MsanEapsDomainProtVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 37, 3, 1)
)
msanEapsDomainProtVlanEntry.setIndexNames(
    (0, "ISKRATEL-MSAN-MIB", "msanEapsDomainName"),
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    msanEapsDomainProtVlanEntry.setStatus("current")
_MsanEapsDomainProtVlanRowStatus_Type = RowStatus
_MsanEapsDomainProtVlanRowStatus_Object = MibTableColumn
msanEapsDomainProtVlanRowStatus = _MsanEapsDomainProtVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 37, 3, 1, 1),
    _MsanEapsDomainProtVlanRowStatus_Type()
)
msanEapsDomainProtVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanEapsDomainProtVlanRowStatus.setStatus("current")
_MsanCpe_ObjectIdentity = ObjectIdentity
msanCpe = _MsanCpe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 38)
)
_MsanCpeGlobal_ObjectIdentity = ObjectIdentity
msanCpeGlobal = _MsanCpeGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 38, 1)
)


class _MsanCpeReset_Type(Unsigned32):
    """Custom type msanCpeReset based on Unsigned32"""
    defaultValue = 0


_MsanCpeReset_Object = MibScalar
msanCpeReset = _MsanCpeReset_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 38, 1, 1),
    _MsanCpeReset_Type()
)
msanCpeReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanCpeReset.setStatus("current")
if mibBuilder.loadTexts:
    msanCpeReset.setUnits("ifIndex")


class _MsanCpeSendConfig_Type(Unsigned32):
    """Custom type msanCpeSendConfig based on Unsigned32"""
    defaultValue = 0


_MsanCpeSendConfig_Object = MibScalar
msanCpeSendConfig = _MsanCpeSendConfig_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 38, 1, 2),
    _MsanCpeSendConfig_Type()
)
msanCpeSendConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanCpeSendConfig.setStatus("current")
if mibBuilder.loadTexts:
    msanCpeSendConfig.setUnits("ifIndex")


class _MsanCpeApiMajorVersion_Type(OctetString):
    """Custom type msanCpeApiMajorVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MsanCpeApiMajorVersion_Type.__name__ = "OctetString"
_MsanCpeApiMajorVersion_Object = MibScalar
msanCpeApiMajorVersion = _MsanCpeApiMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 38, 1, 3),
    _MsanCpeApiMajorVersion_Type()
)
msanCpeApiMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanCpeApiMajorVersion.setStatus("current")


class _MsanCpeApiMinorVersion_Type(OctetString):
    """Custom type msanCpeApiMinorVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MsanCpeApiMinorVersion_Type.__name__ = "OctetString"
_MsanCpeApiMinorVersion_Object = MibScalar
msanCpeApiMinorVersion = _MsanCpeApiMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 38, 1, 4),
    _MsanCpeApiMinorVersion_Type()
)
msanCpeApiMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanCpeApiMinorVersion.setStatus("current")
_MsanCpeTypeTable_Object = MibTable
msanCpeTypeTable = _MsanCpeTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 38, 2)
)
if mibBuilder.loadTexts:
    msanCpeTypeTable.setStatus("current")
_MsanCpeTypeEntry_Object = MibTableRow
msanCpeTypeEntry = _MsanCpeTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 38, 2, 1)
)
msanCpeTypeEntry.setIndexNames(
    (0, "ISKRATEL-MSAN-MIB", "msanCpeTypeName"),
)
if mibBuilder.loadTexts:
    msanCpeTypeEntry.setStatus("current")


class _MsanCpeTypeName_Type(OctetString):
    """Custom type msanCpeTypeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_MsanCpeTypeName_Type.__name__ = "OctetString"
_MsanCpeTypeName_Object = MibTableColumn
msanCpeTypeName = _MsanCpeTypeName_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 38, 2, 1, 1),
    _MsanCpeTypeName_Type()
)
msanCpeTypeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanCpeTypeName.setStatus("current")
_MsanCpeTypePortNum_Type = Integer32
_MsanCpeTypePortNum_Object = MibTableColumn
msanCpeTypePortNum = _MsanCpeTypePortNum_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 38, 2, 1, 2),
    _MsanCpeTypePortNum_Type()
)
msanCpeTypePortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanCpeTypePortNum.setStatus("current")
_MsanCpeIntfTypeTable_Object = MibTable
msanCpeIntfTypeTable = _MsanCpeIntfTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 38, 3)
)
if mibBuilder.loadTexts:
    msanCpeIntfTypeTable.setStatus("current")
_MsanCpeIntfTypeEntry_Object = MibTableRow
msanCpeIntfTypeEntry = _MsanCpeIntfTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 38, 3, 1)
)
msanCpeIntfTypeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ISKRATEL-MSAN-MIB", "msanCpeTypeName"),
)
if mibBuilder.loadTexts:
    msanCpeIntfTypeEntry.setStatus("current")
_MsanCpeIntfTypeRowStatus_Type = RowStatus
_MsanCpeIntfTypeRowStatus_Object = MibTableColumn
msanCpeIntfTypeRowStatus = _MsanCpeIntfTypeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 38, 3, 1, 1),
    _MsanCpeIntfTypeRowStatus_Type()
)
msanCpeIntfTypeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanCpeIntfTypeRowStatus.setStatus("current")


class _MsanCpeIntfTypeHwVersion_Type(OctetString):
    """Custom type msanCpeIntfTypeHwVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MsanCpeIntfTypeHwVersion_Type.__name__ = "OctetString"
_MsanCpeIntfTypeHwVersion_Object = MibTableColumn
msanCpeIntfTypeHwVersion = _MsanCpeIntfTypeHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 38, 3, 1, 2),
    _MsanCpeIntfTypeHwVersion_Type()
)
msanCpeIntfTypeHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanCpeIntfTypeHwVersion.setStatus("current")


class _MsanCpeIntfTypeSwVersion_Type(OctetString):
    """Custom type msanCpeIntfTypeSwVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MsanCpeIntfTypeSwVersion_Type.__name__ = "OctetString"
_MsanCpeIntfTypeSwVersion_Object = MibTableColumn
msanCpeIntfTypeSwVersion = _MsanCpeIntfTypeSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 38, 3, 1, 3),
    _MsanCpeIntfTypeSwVersion_Type()
)
msanCpeIntfTypeSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanCpeIntfTypeSwVersion.setStatus("current")
_MsanCpeIntfPortTable_Object = MibTable
msanCpeIntfPortTable = _MsanCpeIntfPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 38, 4)
)
if mibBuilder.loadTexts:
    msanCpeIntfPortTable.setStatus("current")
_MsanCpeIntfPortEntry_Object = MibTableRow
msanCpeIntfPortEntry = _MsanCpeIntfPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 38, 4, 1)
)
msanCpeIntfPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ISKRATEL-MSAN-MIB", "msanCpeIntfPortId"),
)
if mibBuilder.loadTexts:
    msanCpeIntfPortEntry.setStatus("current")
_MsanCpeIntfPortId_Type = Integer32
_MsanCpeIntfPortId_Object = MibTableColumn
msanCpeIntfPortId = _MsanCpeIntfPortId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 38, 4, 1, 1),
    _MsanCpeIntfPortId_Type()
)
msanCpeIntfPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanCpeIntfPortId.setStatus("current")


class _MsanCpeIntfPortPowerMode_Type(Integer32):
    """Custom type msanCpeIntfPortPowerMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fullPowerDown", 1),
          ("normal", 0),
          ("sleep", 2))
    )


_MsanCpeIntfPortPowerMode_Type.__name__ = "Integer32"
_MsanCpeIntfPortPowerMode_Object = MibTableColumn
msanCpeIntfPortPowerMode = _MsanCpeIntfPortPowerMode_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 38, 4, 1, 2),
    _MsanCpeIntfPortPowerMode_Type()
)
msanCpeIntfPortPowerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanCpeIntfPortPowerMode.setStatus("current")


class _MsanCpeIntfPortLinkMode_Type(Integer32):
    """Custom type msanCpeIntfPortLinkMode based on Integer32"""
    defaultValue = 0

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
        *(("autonegotiation", 0),
          ("speed100MbpsFD", 1),
          ("speed100MbpsHD", 2),
          ("speed10MbpsFD", 3),
          ("speed10MbpsHD", 4))
    )


_MsanCpeIntfPortLinkMode_Type.__name__ = "Integer32"
_MsanCpeIntfPortLinkMode_Object = MibTableColumn
msanCpeIntfPortLinkMode = _MsanCpeIntfPortLinkMode_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 38, 4, 1, 3),
    _MsanCpeIntfPortLinkMode_Type()
)
msanCpeIntfPortLinkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanCpeIntfPortLinkMode.setStatus("current")


class _MsanCpeIntfPortPvid_Type(Integer32):
    """Custom type msanCpeIntfPortPvid based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_MsanCpeIntfPortPvid_Type.__name__ = "Integer32"
_MsanCpeIntfPortPvid_Object = MibTableColumn
msanCpeIntfPortPvid = _MsanCpeIntfPortPvid_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 38, 4, 1, 4),
    _MsanCpeIntfPortPvid_Type()
)
msanCpeIntfPortPvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanCpeIntfPortPvid.setStatus("current")


class _MsanCpeIntfPortCos_Type(Integer32):
    """Custom type msanCpeIntfPortCos based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MsanCpeIntfPortCos_Type.__name__ = "Integer32"
_MsanCpeIntfPortCos_Object = MibTableColumn
msanCpeIntfPortCos = _MsanCpeIntfPortCos_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 38, 4, 1, 5),
    _MsanCpeIntfPortCos_Type()
)
msanCpeIntfPortCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanCpeIntfPortCos.setStatus("current")


class _MsanCpeIntfPortOverrideVid_Type(Integer32):
    """Custom type msanCpeIntfPortOverrideVid based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanCpeIntfPortOverrideVid_Type.__name__ = "Integer32"
_MsanCpeIntfPortOverrideVid_Object = MibTableColumn
msanCpeIntfPortOverrideVid = _MsanCpeIntfPortOverrideVid_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 38, 4, 1, 6),
    _MsanCpeIntfPortOverrideVid_Type()
)
msanCpeIntfPortOverrideVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanCpeIntfPortOverrideVid.setStatus("current")


class _MsanCpeIntfPortOverrideCos_Type(Integer32):
    """Custom type msanCpeIntfPortOverrideCos based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanCpeIntfPortOverrideCos_Type.__name__ = "Integer32"
_MsanCpeIntfPortOverrideCos_Object = MibTableColumn
msanCpeIntfPortOverrideCos = _MsanCpeIntfPortOverrideCos_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 38, 4, 1, 7),
    _MsanCpeIntfPortOverrideCos_Type()
)
msanCpeIntfPortOverrideCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanCpeIntfPortOverrideCos.setStatus("current")


class _MsanCpeIntfPortProtection_Type(Integer32):
    """Custom type msanCpeIntfPortProtection based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("protected", 1),
          ("unprotected", 0))
    )


_MsanCpeIntfPortProtection_Type.__name__ = "Integer32"
_MsanCpeIntfPortProtection_Object = MibTableColumn
msanCpeIntfPortProtection = _MsanCpeIntfPortProtection_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 38, 4, 1, 8),
    _MsanCpeIntfPortProtection_Type()
)
msanCpeIntfPortProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanCpeIntfPortProtection.setStatus("current")


class _MsanCpeIntfPortStatus_Type(Integer32):
    """Custom type msanCpeIntfPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_MsanCpeIntfPortStatus_Type.__name__ = "Integer32"
_MsanCpeIntfPortStatus_Object = MibTableColumn
msanCpeIntfPortStatus = _MsanCpeIntfPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 38, 4, 1, 9),
    _MsanCpeIntfPortStatus_Type()
)
msanCpeIntfPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanCpeIntfPortStatus.setStatus("current")
_MsanCpeTrafficTable_Object = MibTable
msanCpeTrafficTable = _MsanCpeTrafficTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 38, 5)
)
if mibBuilder.loadTexts:
    msanCpeTrafficTable.setStatus("current")
_MsanCpeTrafficEntry_Object = MibTableRow
msanCpeTrafficEntry = _MsanCpeTrafficEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 38, 5, 1)
)
msanCpeTrafficEntry.setIndexNames(
    (0, "ISKRATEL-MSAN-MIB", "msanCpeTrafficId"),
)
if mibBuilder.loadTexts:
    msanCpeTrafficEntry.setStatus("current")
_MsanCpeTrafficId_Type = Integer32
_MsanCpeTrafficId_Object = MibTableColumn
msanCpeTrafficId = _MsanCpeTrafficId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 38, 5, 1, 1),
    _MsanCpeTrafficId_Type()
)
msanCpeTrafficId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanCpeTrafficId.setStatus("current")


class _MsanCpeTrafficName_Type(OctetString):
    """Custom type msanCpeTrafficName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MsanCpeTrafficName_Type.__name__ = "OctetString"
_MsanCpeTrafficName_Object = MibTableColumn
msanCpeTrafficName = _MsanCpeTrafficName_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 38, 5, 1, 2),
    _MsanCpeTrafficName_Type()
)
msanCpeTrafficName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanCpeTrafficName.setStatus("current")


class _MsanCpeTrafficSpeed_Type(Integer32):
    """Custom type msanCpeTrafficSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_MsanCpeTrafficSpeed_Type.__name__ = "Integer32"
_MsanCpeTrafficSpeed_Object = MibTableColumn
msanCpeTrafficSpeed = _MsanCpeTrafficSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 38, 5, 1, 3),
    _MsanCpeTrafficSpeed_Type()
)
msanCpeTrafficSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanCpeTrafficSpeed.setStatus("current")
if mibBuilder.loadTexts:
    msanCpeTrafficSpeed.setUnits("kbit/s")


class _MsanCpeTrafficFlowCntrlMode_Type(Integer32):
    """Custom type msanCpeTrafficFlowCntrlMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanCpeTrafficFlowCntrlMode_Type.__name__ = "Integer32"
_MsanCpeTrafficFlowCntrlMode_Object = MibTableColumn
msanCpeTrafficFlowCntrlMode = _MsanCpeTrafficFlowCntrlMode_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 38, 5, 1, 4),
    _MsanCpeTrafficFlowCntrlMode_Type()
)
msanCpeTrafficFlowCntrlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanCpeTrafficFlowCntrlMode.setStatus("current")
_MsanCpeTrafficRowStatus_Type = RowStatus
_MsanCpeTrafficRowStatus_Object = MibTableColumn
msanCpeTrafficRowStatus = _MsanCpeTrafficRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 38, 5, 1, 5),
    _MsanCpeTrafficRowStatus_Type()
)
msanCpeTrafficRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanCpeTrafficRowStatus.setStatus("current")


class _MsanCpeTrafficProtection_Type(Integer32):
    """Custom type msanCpeTrafficProtection based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("protected", 1),
          ("unprotected", 0))
    )


_MsanCpeTrafficProtection_Type.__name__ = "Integer32"
_MsanCpeTrafficProtection_Object = MibTableColumn
msanCpeTrafficProtection = _MsanCpeTrafficProtection_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 38, 5, 1, 6),
    _MsanCpeTrafficProtection_Type()
)
msanCpeTrafficProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanCpeTrafficProtection.setStatus("current")


class _MsanCpeTrafficStatus_Type(Integer32):
    """Custom type msanCpeTrafficStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_MsanCpeTrafficStatus_Type.__name__ = "Integer32"
_MsanCpeTrafficStatus_Object = MibTableColumn
msanCpeTrafficStatus = _MsanCpeTrafficStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 38, 5, 1, 7),
    _MsanCpeTrafficStatus_Type()
)
msanCpeTrafficStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanCpeTrafficStatus.setStatus("current")
_MsanCpeServiceTable_Object = MibTable
msanCpeServiceTable = _MsanCpeServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 38, 6)
)
if mibBuilder.loadTexts:
    msanCpeServiceTable.setStatus("current")
_MsanCpeServiceEntry_Object = MibTableRow
msanCpeServiceEntry = _MsanCpeServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 38, 6, 1)
)
msanCpeServiceEntry.setIndexNames(
    (0, "ISKRATEL-MSAN-MIB", "msanCpeServiceId"),
)
if mibBuilder.loadTexts:
    msanCpeServiceEntry.setStatus("current")
_MsanCpeServiceId_Type = Integer32
_MsanCpeServiceId_Object = MibTableColumn
msanCpeServiceId = _MsanCpeServiceId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 38, 6, 1, 1),
    _MsanCpeServiceId_Type()
)
msanCpeServiceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanCpeServiceId.setStatus("current")


class _MsanCpeServiceName_Type(OctetString):
    """Custom type msanCpeServiceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MsanCpeServiceName_Type.__name__ = "OctetString"
_MsanCpeServiceName_Object = MibTableColumn
msanCpeServiceName = _MsanCpeServiceName_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 38, 6, 1, 2),
    _MsanCpeServiceName_Type()
)
msanCpeServiceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanCpeServiceName.setStatus("current")


class _MsanCpeServiceCVlanId_Type(Integer32):
    """Custom type msanCpeServiceCVlanId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_MsanCpeServiceCVlanId_Type.__name__ = "Integer32"
_MsanCpeServiceCVlanId_Object = MibTableColumn
msanCpeServiceCVlanId = _MsanCpeServiceCVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 38, 6, 1, 3),
    _MsanCpeServiceCVlanId_Type()
)
msanCpeServiceCVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanCpeServiceCVlanId.setStatus("current")


class _MsanCpeServiceCCos_Type(Integer32):
    """Custom type msanCpeServiceCCos based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MsanCpeServiceCCos_Type.__name__ = "Integer32"
_MsanCpeServiceCCos_Object = MibTableColumn
msanCpeServiceCCos = _MsanCpeServiceCCos_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 38, 6, 1, 4),
    _MsanCpeServiceCCos_Type()
)
msanCpeServiceCCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanCpeServiceCCos.setStatus("current")


class _MsanCpeServiceTrafficId_Type(Integer32):
    """Custom type msanCpeServiceTrafficId based on Integer32"""
    defaultValue = 0


_MsanCpeServiceTrafficId_Object = MibTableColumn
msanCpeServiceTrafficId = _MsanCpeServiceTrafficId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 38, 6, 1, 5),
    _MsanCpeServiceTrafficId_Type()
)
msanCpeServiceTrafficId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanCpeServiceTrafficId.setStatus("current")


class _MsanCpeServiceUntaggedPorts_Type(OctetString):
    """Custom type msanCpeServiceUntaggedPorts based on OctetString"""
    defaultHexValue = "0"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_MsanCpeServiceUntaggedPorts_Type.__name__ = "OctetString"
_MsanCpeServiceUntaggedPorts_Object = MibTableColumn
msanCpeServiceUntaggedPorts = _MsanCpeServiceUntaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 38, 6, 1, 6),
    _MsanCpeServiceUntaggedPorts_Type()
)
msanCpeServiceUntaggedPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanCpeServiceUntaggedPorts.setStatus("current")


class _MsanCpeServiceTaggedPorts_Type(OctetString):
    """Custom type msanCpeServiceTaggedPorts based on OctetString"""
    defaultHexValue = "0"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_MsanCpeServiceTaggedPorts_Type.__name__ = "OctetString"
_MsanCpeServiceTaggedPorts_Object = MibTableColumn
msanCpeServiceTaggedPorts = _MsanCpeServiceTaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 38, 6, 1, 7),
    _MsanCpeServiceTaggedPorts_Type()
)
msanCpeServiceTaggedPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanCpeServiceTaggedPorts.setStatus("current")


class _MsanCpeServiceCMltcstMode_Type(Integer32):
    """Custom type msanCpeServiceCMltcstMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disableIGMPprocessing", 0),
          ("igmpV2SnoopFastLeave", 2),
          ("igmpV2SnoopNormalLeave", 1))
    )


_MsanCpeServiceCMltcstMode_Type.__name__ = "Integer32"
_MsanCpeServiceCMltcstMode_Object = MibTableColumn
msanCpeServiceCMltcstMode = _MsanCpeServiceCMltcstMode_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 38, 6, 1, 8),
    _MsanCpeServiceCMltcstMode_Type()
)
msanCpeServiceCMltcstMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanCpeServiceCMltcstMode.setStatus("current")
_MsanCpeServiceRowStatus_Type = RowStatus
_MsanCpeServiceRowStatus_Object = MibTableColumn
msanCpeServiceRowStatus = _MsanCpeServiceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 38, 6, 1, 9),
    _MsanCpeServiceRowStatus_Type()
)
msanCpeServiceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanCpeServiceRowStatus.setStatus("current")


class _MsanCpeServiceTypeName_Type(OctetString):
    """Custom type msanCpeServiceTypeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_MsanCpeServiceTypeName_Type.__name__ = "OctetString"
_MsanCpeServiceTypeName_Object = MibTableColumn
msanCpeServiceTypeName = _MsanCpeServiceTypeName_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 38, 6, 1, 10),
    _MsanCpeServiceTypeName_Type()
)
msanCpeServiceTypeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanCpeServiceTypeName.setStatus("current")


class _MsanCpeServiceProtection_Type(Integer32):
    """Custom type msanCpeServiceProtection based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("protected", 1),
          ("unprotected", 0))
    )


_MsanCpeServiceProtection_Type.__name__ = "Integer32"
_MsanCpeServiceProtection_Object = MibTableColumn
msanCpeServiceProtection = _MsanCpeServiceProtection_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 38, 6, 1, 11),
    _MsanCpeServiceProtection_Type()
)
msanCpeServiceProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanCpeServiceProtection.setStatus("current")


class _MsanCpeServiceStatus_Type(Integer32):
    """Custom type msanCpeServiceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_MsanCpeServiceStatus_Type.__name__ = "Integer32"
_MsanCpeServiceStatus_Object = MibTableColumn
msanCpeServiceStatus = _MsanCpeServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 38, 6, 1, 12),
    _MsanCpeServiceStatus_Type()
)
msanCpeServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanCpeServiceStatus.setStatus("current")
_MsanCpeIntfServiceTable_Object = MibTable
msanCpeIntfServiceTable = _MsanCpeIntfServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 38, 7)
)
if mibBuilder.loadTexts:
    msanCpeIntfServiceTable.setStatus("current")
_MsanCpeIntfServiceEntry_Object = MibTableRow
msanCpeIntfServiceEntry = _MsanCpeIntfServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 38, 7, 1)
)
msanCpeIntfServiceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ISKRATEL-MSAN-MIB", "msanCpeServiceId"),
)
if mibBuilder.loadTexts:
    msanCpeIntfServiceEntry.setStatus("current")
_MsanCpeIntfServiceRowStatus_Type = RowStatus
_MsanCpeIntfServiceRowStatus_Object = MibTableColumn
msanCpeIntfServiceRowStatus = _MsanCpeIntfServiceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 38, 7, 1, 1),
    _MsanCpeIntfServiceRowStatus_Type()
)
msanCpeIntfServiceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanCpeIntfServiceRowStatus.setStatus("current")
_MsanBoard_ObjectIdentity = ObjectIdentity
msanBoard = _MsanBoard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 39)
)
_MsanBoardGlobal_ObjectIdentity = ObjectIdentity
msanBoardGlobal = _MsanBoardGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 39, 1)
)


class _MsanBoardReset_Type(Integer32):
    """Custom type msanBoardReset based on Integer32"""
    defaultValue = 0


_MsanBoardReset_Object = MibScalar
msanBoardReset = _MsanBoardReset_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 39, 1, 1),
    _MsanBoardReset_Type()
)
msanBoardReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanBoardReset.setStatus("current")
_MsanBoardConfTable_Object = MibTable
msanBoardConfTable = _MsanBoardConfTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 39, 2)
)
if mibBuilder.loadTexts:
    msanBoardConfTable.setStatus("current")
_MsanBoardConfEntry_Object = MibTableRow
msanBoardConfEntry = _MsanBoardConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 39, 2, 1)
)
msanBoardConfEntry.setIndexNames(
    (0, "ISKRATEL-MSAN-MIB", "msanBoardConfNr"),
)
if mibBuilder.loadTexts:
    msanBoardConfEntry.setStatus("current")


class _MsanBoardConfNr_Type(Integer32):
    """Custom type msanBoardConfNr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_MsanBoardConfNr_Type.__name__ = "Integer32"
_MsanBoardConfNr_Object = MibTableColumn
msanBoardConfNr = _MsanBoardConfNr_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 39, 2, 1, 1),
    _MsanBoardConfNr_Type()
)
msanBoardConfNr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanBoardConfNr.setStatus("current")


class _MsanBoardConfParentNr_Type(Integer32):
    """Custom type msanBoardConfParentNr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_MsanBoardConfParentNr_Type.__name__ = "Integer32"
_MsanBoardConfParentNr_Object = MibTableColumn
msanBoardConfParentNr = _MsanBoardConfParentNr_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 39, 2, 1, 2),
    _MsanBoardConfParentNr_Type()
)
msanBoardConfParentNr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanBoardConfParentNr.setStatus("current")


class _MsanBoardConfPosition_Type(Integer32):
    """Custom type msanBoardConfPosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_MsanBoardConfPosition_Type.__name__ = "Integer32"
_MsanBoardConfPosition_Object = MibTableColumn
msanBoardConfPosition = _MsanBoardConfPosition_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 39, 2, 1, 3),
    _MsanBoardConfPosition_Type()
)
msanBoardConfPosition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanBoardConfPosition.setStatus("current")
_MsanBoardConfType_Type = OctetString
_MsanBoardConfType_Object = MibTableColumn
msanBoardConfType = _MsanBoardConfType_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 39, 2, 1, 4),
    _MsanBoardConfType_Type()
)
msanBoardConfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanBoardConfType.setStatus("current")
_MsanBoardConfRequiredId_Type = OctetString
_MsanBoardConfRequiredId_Object = MibTableColumn
msanBoardConfRequiredId = _MsanBoardConfRequiredId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 39, 2, 1, 5),
    _MsanBoardConfRequiredId_Type()
)
msanBoardConfRequiredId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanBoardConfRequiredId.setStatus("current")
_MsanBoardConfActualId_Type = OctetString
_MsanBoardConfActualId_Object = MibTableColumn
msanBoardConfActualId = _MsanBoardConfActualId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 39, 2, 1, 6),
    _MsanBoardConfActualId_Type()
)
msanBoardConfActualId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanBoardConfActualId.setStatus("current")
_MsanBoardConfSerialNr_Type = OctetString
_MsanBoardConfSerialNr_Object = MibTableColumn
msanBoardConfSerialNr = _MsanBoardConfSerialNr_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 39, 2, 1, 7),
    _MsanBoardConfSerialNr_Type()
)
msanBoardConfSerialNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanBoardConfSerialNr.setStatus("current")
_MsanBoardConfDescription_Type = OctetString
_MsanBoardConfDescription_Object = MibTableColumn
msanBoardConfDescription = _MsanBoardConfDescription_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 39, 2, 1, 8),
    _MsanBoardConfDescription_Type()
)
msanBoardConfDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanBoardConfDescription.setStatus("current")


class _MsanBoardConfStatus_Type(Integer32):
    """Custom type msanBoardConfStatus based on Integer32"""
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
        *(("boardNotPresent", 3),
          ("boardPresentInitProcess", 4),
          ("boardPresentNotAccessible", 2),
          ("boardPresentRunning", 1))
    )


_MsanBoardConfStatus_Type.__name__ = "Integer32"
_MsanBoardConfStatus_Object = MibTableColumn
msanBoardConfStatus = _MsanBoardConfStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 39, 2, 1, 9),
    _MsanBoardConfStatus_Type()
)
msanBoardConfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanBoardConfStatus.setStatus("current")
_MsanBoardConfRowStatus_Type = RowStatus
_MsanBoardConfRowStatus_Object = MibTableColumn
msanBoardConfRowStatus = _MsanBoardConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 39, 2, 1, 10),
    _MsanBoardConfRowStatus_Type()
)
msanBoardConfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanBoardConfRowStatus.setStatus("current")
_MsanBoardConfSwSteerVersion_Type = OctetString
_MsanBoardConfSwSteerVersion_Object = MibTableColumn
msanBoardConfSwSteerVersion = _MsanBoardConfSwSteerVersion_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 39, 2, 1, 11),
    _MsanBoardConfSwSteerVersion_Type()
)
msanBoardConfSwSteerVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanBoardConfSwSteerVersion.setStatus("current")
_MsanBoardConfSwBuildDirectory_Type = OctetString
_MsanBoardConfSwBuildDirectory_Object = MibTableColumn
msanBoardConfSwBuildDirectory = _MsanBoardConfSwBuildDirectory_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 39, 2, 1, 12),
    _MsanBoardConfSwBuildDirectory_Type()
)
msanBoardConfSwBuildDirectory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanBoardConfSwBuildDirectory.setStatus("current")
_MsanBoardConfSwBuildTime_Type = OctetString
_MsanBoardConfSwBuildTime_Object = MibTableColumn
msanBoardConfSwBuildTime = _MsanBoardConfSwBuildTime_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 39, 2, 1, 13),
    _MsanBoardConfSwBuildTime_Type()
)
msanBoardConfSwBuildTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanBoardConfSwBuildTime.setStatus("current")
_MsanBoardConfSwBranch_Type = OctetString
_MsanBoardConfSwBranch_Object = MibTableColumn
msanBoardConfSwBranch = _MsanBoardConfSwBranch_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 39, 2, 1, 14),
    _MsanBoardConfSwBranch_Type()
)
msanBoardConfSwBranch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanBoardConfSwBranch.setStatus("current")
_MsanBoardConfSwBuildReference_Type = OctetString
_MsanBoardConfSwBuildReference_Object = MibTableColumn
msanBoardConfSwBuildReference = _MsanBoardConfSwBuildReference_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 39, 2, 1, 15),
    _MsanBoardConfSwBuildReference_Type()
)
msanBoardConfSwBuildReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanBoardConfSwBuildReference.setStatus("current")
_MsanBoardListTable_Object = MibTable
msanBoardListTable = _MsanBoardListTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 39, 3)
)
if mibBuilder.loadTexts:
    msanBoardListTable.setStatus("current")
_MsanBoardListEntry_Object = MibTableRow
msanBoardListEntry = _MsanBoardListEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 39, 3, 1)
)
msanBoardListEntry.setIndexNames(
    (0, "ISKRATEL-MSAN-MIB", "msanBoardListId"),
)
if mibBuilder.loadTexts:
    msanBoardListEntry.setStatus("current")
_MsanBoardListId_Type = OctetString
_MsanBoardListId_Object = MibTableColumn
msanBoardListId = _MsanBoardListId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 39, 3, 1, 1),
    _MsanBoardListId_Type()
)
msanBoardListId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanBoardListId.setStatus("current")
_MsanBoardListType_Type = OctetString
_MsanBoardListType_Object = MibTableColumn
msanBoardListType = _MsanBoardListType_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 39, 3, 1, 2),
    _MsanBoardListType_Type()
)
msanBoardListType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanBoardListType.setStatus("current")
_MsanFtpServer_ObjectIdentity = ObjectIdentity
msanFtpServer = _MsanFtpServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 40)
)
_MsanFtpServerGlobal_ObjectIdentity = ObjectIdentity
msanFtpServerGlobal = _MsanFtpServerGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 40, 1)
)


class _MsanFtpServerAdminState_Type(Integer32):
    """Custom type msanFtpServerAdminState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanFtpServerAdminState_Type.__name__ = "Integer32"
_MsanFtpServerAdminState_Object = MibScalar
msanFtpServerAdminState = _MsanFtpServerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 40, 1, 1),
    _MsanFtpServerAdminState_Type()
)
msanFtpServerAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanFtpServerAdminState.setStatus("current")
_MsanAppRateLimit_ObjectIdentity = ObjectIdentity
msanAppRateLimit = _MsanAppRateLimit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 41)
)
_MsanAppRateLimitGlobal_ObjectIdentity = ObjectIdentity
msanAppRateLimitGlobal = _MsanAppRateLimitGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 41, 1)
)
_MsanAppRateLimitTable_Object = MibTable
msanAppRateLimitTable = _MsanAppRateLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 41, 2)
)
if mibBuilder.loadTexts:
    msanAppRateLimitTable.setStatus("current")
_MsanAppRateLimitEntry_Object = MibTableRow
msanAppRateLimitEntry = _MsanAppRateLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 41, 2, 1)
)
msanAppRateLimitEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    msanAppRateLimitEntry.setStatus("current")


class _MsanAppRateLimitDhcp_Type(Integer32):
    """Custom type msanAppRateLimitDhcp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_MsanAppRateLimitDhcp_Type.__name__ = "Integer32"
_MsanAppRateLimitDhcp_Object = MibTableColumn
msanAppRateLimitDhcp = _MsanAppRateLimitDhcp_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 41, 2, 1, 1),
    _MsanAppRateLimitDhcp_Type()
)
msanAppRateLimitDhcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanAppRateLimitDhcp.setStatus("current")
if mibBuilder.loadTexts:
    msanAppRateLimitDhcp.setUnits("pps")


class _MsanAppRateLimitDhcpState_Type(Integer32):
    """Custom type msanAppRateLimitDhcpState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanAppRateLimitDhcpState_Type.__name__ = "Integer32"
_MsanAppRateLimitDhcpState_Object = MibTableColumn
msanAppRateLimitDhcpState = _MsanAppRateLimitDhcpState_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 41, 2, 1, 2),
    _MsanAppRateLimitDhcpState_Type()
)
msanAppRateLimitDhcpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanAppRateLimitDhcpState.setStatus("current")


class _MsanAppRateLimitPppoe_Type(Integer32):
    """Custom type msanAppRateLimitPppoe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_MsanAppRateLimitPppoe_Type.__name__ = "Integer32"
_MsanAppRateLimitPppoe_Object = MibTableColumn
msanAppRateLimitPppoe = _MsanAppRateLimitPppoe_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 41, 2, 1, 3),
    _MsanAppRateLimitPppoe_Type()
)
msanAppRateLimitPppoe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanAppRateLimitPppoe.setStatus("current")
if mibBuilder.loadTexts:
    msanAppRateLimitPppoe.setUnits("pps")


class _MsanAppRateLimitPppoeState_Type(Integer32):
    """Custom type msanAppRateLimitPppoeState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanAppRateLimitPppoeState_Type.__name__ = "Integer32"
_MsanAppRateLimitPppoeState_Object = MibTableColumn
msanAppRateLimitPppoeState = _MsanAppRateLimitPppoeState_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 41, 2, 1, 4),
    _MsanAppRateLimitPppoeState_Type()
)
msanAppRateLimitPppoeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanAppRateLimitPppoeState.setStatus("current")


class _MsanAppRateLimitIgmp_Type(Integer32):
    """Custom type msanAppRateLimitIgmp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_MsanAppRateLimitIgmp_Type.__name__ = "Integer32"
_MsanAppRateLimitIgmp_Object = MibTableColumn
msanAppRateLimitIgmp = _MsanAppRateLimitIgmp_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 41, 2, 1, 5),
    _MsanAppRateLimitIgmp_Type()
)
msanAppRateLimitIgmp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanAppRateLimitIgmp.setStatus("current")
if mibBuilder.loadTexts:
    msanAppRateLimitIgmp.setUnits("pps")


class _MsanAppRateLimitIgmpState_Type(Integer32):
    """Custom type msanAppRateLimitIgmpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanAppRateLimitIgmpState_Type.__name__ = "Integer32"
_MsanAppRateLimitIgmpState_Object = MibTableColumn
msanAppRateLimitIgmpState = _MsanAppRateLimitIgmpState_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 41, 2, 1, 6),
    _MsanAppRateLimitIgmpState_Type()
)
msanAppRateLimitIgmpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanAppRateLimitIgmpState.setStatus("current")


class _MsanAppRateLimitStp_Type(Integer32):
    """Custom type msanAppRateLimitStp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_MsanAppRateLimitStp_Type.__name__ = "Integer32"
_MsanAppRateLimitStp_Object = MibTableColumn
msanAppRateLimitStp = _MsanAppRateLimitStp_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 41, 2, 1, 7),
    _MsanAppRateLimitStp_Type()
)
msanAppRateLimitStp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanAppRateLimitStp.setStatus("current")
if mibBuilder.loadTexts:
    msanAppRateLimitStp.setUnits("pps")


class _MsanAppRateLimitStpState_Type(Integer32):
    """Custom type msanAppRateLimitStpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanAppRateLimitStpState_Type.__name__ = "Integer32"
_MsanAppRateLimitStpState_Object = MibTableColumn
msanAppRateLimitStpState = _MsanAppRateLimitStpState_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 41, 2, 1, 8),
    _MsanAppRateLimitStpState_Type()
)
msanAppRateLimitStpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanAppRateLimitStpState.setStatus("current")


class _MsanAppRateLimitMn_Type(Integer32):
    """Custom type msanAppRateLimitMn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_MsanAppRateLimitMn_Type.__name__ = "Integer32"
_MsanAppRateLimitMn_Object = MibTableColumn
msanAppRateLimitMn = _MsanAppRateLimitMn_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 41, 2, 1, 9),
    _MsanAppRateLimitMn_Type()
)
msanAppRateLimitMn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanAppRateLimitMn.setStatus("current")
if mibBuilder.loadTexts:
    msanAppRateLimitMn.setUnits("pps")


class _MsanAppRateLimitMnState_Type(Integer32):
    """Custom type msanAppRateLimitMnState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanAppRateLimitMnState_Type.__name__ = "Integer32"
_MsanAppRateLimitMnState_Object = MibTableColumn
msanAppRateLimitMnState = _MsanAppRateLimitMnState_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 41, 2, 1, 10),
    _MsanAppRateLimitMnState_Type()
)
msanAppRateLimitMnState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanAppRateLimitMnState.setStatus("current")
_MsanMlinec_ObjectIdentity = ObjectIdentity
msanMlinec = _MsanMlinec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 50)
)
_MsanMlinecGlobal_ObjectIdentity = ObjectIdentity
msanMlinecGlobal = _MsanMlinecGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 50, 1)
)


class _MsanMlinecAdminState_Type(Integer32):
    """Custom type msanMlinecAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanMlinecAdminState_Type.__name__ = "Integer32"
_MsanMlinecAdminState_Object = MibScalar
msanMlinecAdminState = _MsanMlinecAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 50, 1, 1),
    _MsanMlinecAdminState_Type()
)
msanMlinecAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanMlinecAdminState.setStatus("current")
_MsanMulticast_ObjectIdentity = ObjectIdentity
msanMulticast = _MsanMulticast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 100)
)
_MsanMulticastGlobal_ObjectIdentity = ObjectIdentity
msanMulticastGlobal = _MsanMulticastGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 100, 1)
)
_MsanMulticastIntfStaticGroupTable_Object = MibTable
msanMulticastIntfStaticGroupTable = _MsanMulticastIntfStaticGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 100, 2)
)
if mibBuilder.loadTexts:
    msanMulticastIntfStaticGroupTable.setStatus("deprecated")
_MsanMulticastIntfStaticGroupEntry_Object = MibTableRow
msanMulticastIntfStaticGroupEntry = _MsanMulticastIntfStaticGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 100, 2, 1)
)
msanMulticastIntfStaticGroupEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ISKRATEL-MSAN-MIB", "msanMulticastIntfStaticGroupIPAddr"),
)
if mibBuilder.loadTexts:
    msanMulticastIntfStaticGroupEntry.setStatus("deprecated")
_MsanMulticastIntfStaticGroupIPAddr_Type = IpAddress
_MsanMulticastIntfStaticGroupIPAddr_Object = MibTableColumn
msanMulticastIntfStaticGroupIPAddr = _MsanMulticastIntfStaticGroupIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 100, 2, 1, 1),
    _MsanMulticastIntfStaticGroupIPAddr_Type()
)
msanMulticastIntfStaticGroupIPAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanMulticastIntfStaticGroupIPAddr.setStatus("deprecated")
_MsanMulticastIntfStaticGroupRowStatus_Type = RowStatus
_MsanMulticastIntfStaticGroupRowStatus_Object = MibTableColumn
msanMulticastIntfStaticGroupRowStatus = _MsanMulticastIntfStaticGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 100, 2, 1, 2),
    _MsanMulticastIntfStaticGroupRowStatus_Type()
)
msanMulticastIntfStaticGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanMulticastIntfStaticGroupRowStatus.setStatus("deprecated")
_MsanMulticastGroupTable_Object = MibTable
msanMulticastGroupTable = _MsanMulticastGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 100, 3)
)
if mibBuilder.loadTexts:
    msanMulticastGroupTable.setStatus("current")
_MsanMulticastGroupEntry_Object = MibTableRow
msanMulticastGroupEntry = _MsanMulticastGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 100, 3, 1)
)
msanMulticastGroupEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
    (0, "ISKRATEL-MSAN-MIB", "msanMulticastGroupIpAddr"),
)
if mibBuilder.loadTexts:
    msanMulticastGroupEntry.setStatus("current")
_MsanMulticastGroupIpAddr_Type = IpAddress
_MsanMulticastGroupIpAddr_Object = MibTableColumn
msanMulticastGroupIpAddr = _MsanMulticastGroupIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 100, 3, 1, 1),
    _MsanMulticastGroupIpAddr_Type()
)
msanMulticastGroupIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanMulticastGroupIpAddr.setStatus("current")
_MsanMulticastGroupName_Type = OctetString
_MsanMulticastGroupName_Object = MibTableColumn
msanMulticastGroupName = _MsanMulticastGroupName_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 100, 3, 1, 2),
    _MsanMulticastGroupName_Type()
)
msanMulticastGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanMulticastGroupName.setStatus("current")
_MsanMulticastGroupRowStatus_Type = RowStatus
_MsanMulticastGroupRowStatus_Object = MibTableColumn
msanMulticastGroupRowStatus = _MsanMulticastGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 100, 3, 1, 3),
    _MsanMulticastGroupRowStatus_Type()
)
msanMulticastGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanMulticastGroupRowStatus.setStatus("current")
_MsanMulticastAclListTable_Object = MibTable
msanMulticastAclListTable = _MsanMulticastAclListTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 100, 4)
)
if mibBuilder.loadTexts:
    msanMulticastAclListTable.setStatus("deprecated")
_MsanMulticastAclListEntry_Object = MibTableRow
msanMulticastAclListEntry = _MsanMulticastAclListEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 100, 4, 1)
)
msanMulticastAclListEntry.setIndexNames(
    (0, "ISKRATEL-MSAN-MIB", "msanMulticastAclListId"),
)
if mibBuilder.loadTexts:
    msanMulticastAclListEntry.setStatus("deprecated")


class _MsanMulticastAclListId_Type(Integer32):
    """Custom type msanMulticastAclListId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanMulticastAclListId_Type.__name__ = "Integer32"
_MsanMulticastAclListId_Object = MibTableColumn
msanMulticastAclListId = _MsanMulticastAclListId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 100, 4, 1, 1),
    _MsanMulticastAclListId_Type()
)
msanMulticastAclListId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanMulticastAclListId.setStatus("deprecated")
_MsanMulticastAclListName_Type = SnmpAdminString
_MsanMulticastAclListName_Object = MibTableColumn
msanMulticastAclListName = _MsanMulticastAclListName_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 100, 4, 1, 2),
    _MsanMulticastAclListName_Type()
)
msanMulticastAclListName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanMulticastAclListName.setStatus("deprecated")
_MsanMulticastAclListRowStatus_Type = RowStatus
_MsanMulticastAclListRowStatus_Object = MibTableColumn
msanMulticastAclListRowStatus = _MsanMulticastAclListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 100, 4, 1, 3),
    _MsanMulticastAclListRowStatus_Type()
)
msanMulticastAclListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanMulticastAclListRowStatus.setStatus("deprecated")
_MsanMulticastAclListGroupTable_Object = MibTable
msanMulticastAclListGroupTable = _MsanMulticastAclListGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 100, 5)
)
if mibBuilder.loadTexts:
    msanMulticastAclListGroupTable.setStatus("deprecated")
_MsanMulticastAclListGroupEntry_Object = MibTableRow
msanMulticastAclListGroupEntry = _MsanMulticastAclListGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 100, 5, 1)
)
msanMulticastAclListGroupEntry.setIndexNames(
    (0, "ISKRATEL-MSAN-MIB", "msanMulticastAclListId"),
    (0, "ISKRATEL-MSAN-MIB", "msanMulticastAclGroupIpAddr"),
)
if mibBuilder.loadTexts:
    msanMulticastAclListGroupEntry.setStatus("deprecated")
_MsanMulticastAclGroupIpAddr_Type = IpAddress
_MsanMulticastAclGroupIpAddr_Object = MibTableColumn
msanMulticastAclGroupIpAddr = _MsanMulticastAclGroupIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 100, 5, 1, 1),
    _MsanMulticastAclGroupIpAddr_Type()
)
msanMulticastAclGroupIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanMulticastAclGroupIpAddr.setStatus("deprecated")
_MsanMulticastAclListGroupRowStatus_Type = RowStatus
_MsanMulticastAclListGroupRowStatus_Object = MibTableColumn
msanMulticastAclListGroupRowStatus = _MsanMulticastAclListGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 100, 5, 1, 2),
    _MsanMulticastAclListGroupRowStatus_Type()
)
msanMulticastAclListGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanMulticastAclListGroupRowStatus.setStatus("deprecated")
_MsanMulticastAclIntfListTable_Object = MibTable
msanMulticastAclIntfListTable = _MsanMulticastAclIntfListTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 100, 6)
)
if mibBuilder.loadTexts:
    msanMulticastAclIntfListTable.setStatus("deprecated")
_MsanMulticastAclIntfListEntry_Object = MibTableRow
msanMulticastAclIntfListEntry = _MsanMulticastAclIntfListEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 100, 6, 1)
)
msanMulticastAclIntfListEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ISKRATEL-MSAN-MIB", "msanMulticastAclListId"),
)
if mibBuilder.loadTexts:
    msanMulticastAclIntfListEntry.setStatus("deprecated")


class _MsanMulticastAclIntfListMode_Type(Integer32):
    """Custom type msanMulticastAclIntfListMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("deny", 2))
    )


_MsanMulticastAclIntfListMode_Type.__name__ = "Integer32"
_MsanMulticastAclIntfListMode_Object = MibTableColumn
msanMulticastAclIntfListMode = _MsanMulticastAclIntfListMode_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 100, 6, 1, 1),
    _MsanMulticastAclIntfListMode_Type()
)
msanMulticastAclIntfListMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanMulticastAclIntfListMode.setStatus("deprecated")
_MsanMulticastAclIntfListRowStatus_Type = RowStatus
_MsanMulticastAclIntfListRowStatus_Object = MibTableColumn
msanMulticastAclIntfListRowStatus = _MsanMulticastAclIntfListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 100, 6, 1, 2),
    _MsanMulticastAclIntfListRowStatus_Type()
)
msanMulticastAclIntfListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanMulticastAclIntfListRowStatus.setStatus("deprecated")
_MsanMulticastAclListVlanGroupTable_Object = MibTable
msanMulticastAclListVlanGroupTable = _MsanMulticastAclListVlanGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 100, 7)
)
if mibBuilder.loadTexts:
    msanMulticastAclListVlanGroupTable.setStatus("deprecated")
_MsanMulticastAclListVlanGroupEntry_Object = MibTableRow
msanMulticastAclListVlanGroupEntry = _MsanMulticastAclListVlanGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 100, 7, 1)
)
msanMulticastAclListVlanGroupEntry.setIndexNames(
    (0, "ISKRATEL-MSAN-MIB", "msanMulticastAclListId"),
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
    (0, "ISKRATEL-MSAN-MIB", "msanMulticastAclListVlanGroupIpAddr"),
)
if mibBuilder.loadTexts:
    msanMulticastAclListVlanGroupEntry.setStatus("deprecated")
_MsanMulticastAclListVlanGroupIpAddr_Type = IpAddress
_MsanMulticastAclListVlanGroupIpAddr_Object = MibTableColumn
msanMulticastAclListVlanGroupIpAddr = _MsanMulticastAclListVlanGroupIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 100, 7, 1, 1),
    _MsanMulticastAclListVlanGroupIpAddr_Type()
)
msanMulticastAclListVlanGroupIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanMulticastAclListVlanGroupIpAddr.setStatus("deprecated")
_MsanMulticastAclListVlanGroupRowStatus_Type = RowStatus
_MsanMulticastAclListVlanGroupRowStatus_Object = MibTableColumn
msanMulticastAclListVlanGroupRowStatus = _MsanMulticastAclListVlanGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 100, 7, 1, 2),
    _MsanMulticastAclListVlanGroupRowStatus_Type()
)
msanMulticastAclListVlanGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanMulticastAclListVlanGroupRowStatus.setStatus("deprecated")
_MsanMulticastIntfVlanStaticGroupTable_Object = MibTable
msanMulticastIntfVlanStaticGroupTable = _MsanMulticastIntfVlanStaticGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 100, 8)
)
if mibBuilder.loadTexts:
    msanMulticastIntfVlanStaticGroupTable.setStatus("current")
_MsanMulticastIntfVlanStaticGroupEntry_Object = MibTableRow
msanMulticastIntfVlanStaticGroupEntry = _MsanMulticastIntfVlanStaticGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 100, 8, 1)
)
msanMulticastIntfVlanStaticGroupEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
    (0, "ISKRATEL-MSAN-MIB", "msanMulticastIntfVlanStaticGroupIpAddr"),
)
if mibBuilder.loadTexts:
    msanMulticastIntfVlanStaticGroupEntry.setStatus("current")
_MsanMulticastIntfVlanStaticGroupIpAddr_Type = IpAddress
_MsanMulticastIntfVlanStaticGroupIpAddr_Object = MibTableColumn
msanMulticastIntfVlanStaticGroupIpAddr = _MsanMulticastIntfVlanStaticGroupIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 100, 8, 1, 1),
    _MsanMulticastIntfVlanStaticGroupIpAddr_Type()
)
msanMulticastIntfVlanStaticGroupIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanMulticastIntfVlanStaticGroupIpAddr.setStatus("current")
_MsanMulticastIntfVlanStaticGroupRowStatus_Type = RowStatus
_MsanMulticastIntfVlanStaticGroupRowStatus_Object = MibTableColumn
msanMulticastIntfVlanStaticGroupRowStatus = _MsanMulticastIntfVlanStaticGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 100, 8, 1, 2),
    _MsanMulticastIntfVlanStaticGroupRowStatus_Type()
)
msanMulticastIntfVlanStaticGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanMulticastIntfVlanStaticGroupRowStatus.setStatus("current")
_MsanMulticastAccessListTable_Object = MibTable
msanMulticastAccessListTable = _MsanMulticastAccessListTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 100, 9)
)
if mibBuilder.loadTexts:
    msanMulticastAccessListTable.setStatus("current")
_MsanMulticastAccessListEntry_Object = MibTableRow
msanMulticastAccessListEntry = _MsanMulticastAccessListEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 100, 9, 1)
)
msanMulticastAccessListEntry.setIndexNames(
    (0, "ISKRATEL-MSAN-MIB", "msanMulticastAccessListName"),
)
if mibBuilder.loadTexts:
    msanMulticastAccessListEntry.setStatus("current")


class _MsanMulticastAccessListName_Type(OctetString):
    """Custom type msanMulticastAccessListName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MsanMulticastAccessListName_Type.__name__ = "OctetString"
_MsanMulticastAccessListName_Object = MibTableColumn
msanMulticastAccessListName = _MsanMulticastAccessListName_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 100, 9, 1, 1),
    _MsanMulticastAccessListName_Type()
)
msanMulticastAccessListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanMulticastAccessListName.setStatus("current")
_MsanMulticastAccessListRowStatus_Type = RowStatus
_MsanMulticastAccessListRowStatus_Object = MibTableColumn
msanMulticastAccessListRowStatus = _MsanMulticastAccessListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 100, 9, 1, 2),
    _MsanMulticastAccessListRowStatus_Type()
)
msanMulticastAccessListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanMulticastAccessListRowStatus.setStatus("current")
_MsanMulticastAccessListGroupTable_Object = MibTable
msanMulticastAccessListGroupTable = _MsanMulticastAccessListGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 100, 10)
)
if mibBuilder.loadTexts:
    msanMulticastAccessListGroupTable.setStatus("current")
_MsanMulticastAccessListGroupEntry_Object = MibTableRow
msanMulticastAccessListGroupEntry = _MsanMulticastAccessListGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 100, 10, 1)
)
msanMulticastAccessListGroupEntry.setIndexNames(
    (0, "ISKRATEL-MSAN-MIB", "msanMulticastAccessListName"),
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
    (0, "ISKRATEL-MSAN-MIB", "msanMulticastAccessListGroupIpAddr"),
)
if mibBuilder.loadTexts:
    msanMulticastAccessListGroupEntry.setStatus("current")
_MsanMulticastAccessListGroupIpAddr_Type = IpAddress
_MsanMulticastAccessListGroupIpAddr_Object = MibTableColumn
msanMulticastAccessListGroupIpAddr = _MsanMulticastAccessListGroupIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 100, 10, 1, 1),
    _MsanMulticastAccessListGroupIpAddr_Type()
)
msanMulticastAccessListGroupIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanMulticastAccessListGroupIpAddr.setStatus("current")
_MsanMulticastAccessListGroupRowStatus_Type = RowStatus
_MsanMulticastAccessListGroupRowStatus_Object = MibTableColumn
msanMulticastAccessListGroupRowStatus = _MsanMulticastAccessListGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 100, 10, 1, 2),
    _MsanMulticastAccessListGroupRowStatus_Type()
)
msanMulticastAccessListGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanMulticastAccessListGroupRowStatus.setStatus("current")
_MsanMulticastAccessListIntfTable_Object = MibTable
msanMulticastAccessListIntfTable = _MsanMulticastAccessListIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 100, 11)
)
if mibBuilder.loadTexts:
    msanMulticastAccessListIntfTable.setStatus("current")
_MsanMulticastAccessListIntfEntry_Object = MibTableRow
msanMulticastAccessListIntfEntry = _MsanMulticastAccessListIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 100, 11, 1)
)
msanMulticastAccessListIntfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ISKRATEL-MSAN-MIB", "msanMulticastAccessListName"),
)
if mibBuilder.loadTexts:
    msanMulticastAccessListIntfEntry.setStatus("current")


class _MsanMulticastAccessListIntfMode_Type(Integer32):
    """Custom type msanMulticastAccessListIntfMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("deny", 2))
    )


_MsanMulticastAccessListIntfMode_Type.__name__ = "Integer32"
_MsanMulticastAccessListIntfMode_Object = MibTableColumn
msanMulticastAccessListIntfMode = _MsanMulticastAccessListIntfMode_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 100, 11, 1, 1),
    _MsanMulticastAccessListIntfMode_Type()
)
msanMulticastAccessListIntfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanMulticastAccessListIntfMode.setStatus("current")
_MsanMulticastAccessListIntfRowStatus_Type = RowStatus
_MsanMulticastAccessListIntfRowStatus_Object = MibTableColumn
msanMulticastAccessListIntfRowStatus = _MsanMulticastAccessListIntfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 100, 11, 1, 2),
    _MsanMulticastAccessListIntfRowStatus_Type()
)
msanMulticastAccessListIntfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanMulticastAccessListIntfRowStatus.setStatus("current")
_MsanSwitchMFDBTable_Object = MibTable
msanSwitchMFDBTable = _MsanSwitchMFDBTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 100, 12)
)
if mibBuilder.loadTexts:
    msanSwitchMFDBTable.setStatus("current")
_MsanSwitchMFDBEntry_Object = MibTableRow
msanSwitchMFDBEntry = _MsanSwitchMFDBEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 100, 12, 1)
)
msanSwitchMFDBEntry.setIndexNames(
    (0, "ISKRATEL-MSAN-MIB", "msanSwitchMFDBProtocolType"),
    (0, "ISKRATEL-MSAN-MIB", "msanSwitchMFDBVlanId"),
    (0, "ISKRATEL-MSAN-MIB", "msanSwitchMFDBMacAddress"),
)
if mibBuilder.loadTexts:
    msanSwitchMFDBEntry.setStatus("current")


class _MsanSwitchMFDBProtocolType_Type(Integer32):
    """Custom type msanSwitchMFDBProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("gmrp", 2),
          ("igmp", 3),
          ("static", 1))
    )


_MsanSwitchMFDBProtocolType_Type.__name__ = "Integer32"
_MsanSwitchMFDBProtocolType_Object = MibTableColumn
msanSwitchMFDBProtocolType = _MsanSwitchMFDBProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 100, 12, 1, 1),
    _MsanSwitchMFDBProtocolType_Type()
)
msanSwitchMFDBProtocolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanSwitchMFDBProtocolType.setStatus("current")
_MsanSwitchMFDBVlanId_Type = VlanIndex
_MsanSwitchMFDBVlanId_Object = MibTableColumn
msanSwitchMFDBVlanId = _MsanSwitchMFDBVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 100, 12, 1, 2),
    _MsanSwitchMFDBVlanId_Type()
)
msanSwitchMFDBVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanSwitchMFDBVlanId.setStatus("current")
_MsanSwitchMFDBMacAddress_Type = MacAddress
_MsanSwitchMFDBMacAddress_Object = MibTableColumn
msanSwitchMFDBMacAddress = _MsanSwitchMFDBMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 100, 12, 1, 3),
    _MsanSwitchMFDBMacAddress_Type()
)
msanSwitchMFDBMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanSwitchMFDBMacAddress.setStatus("current")


class _MsanSwitchMFDBType_Type(Integer32):
    """Custom type msanSwitchMFDBType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_MsanSwitchMFDBType_Type.__name__ = "Integer32"
_MsanSwitchMFDBType_Object = MibTableColumn
msanSwitchMFDBType = _MsanSwitchMFDBType_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 100, 12, 1, 4),
    _MsanSwitchMFDBType_Type()
)
msanSwitchMFDBType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanSwitchMFDBType.setStatus("current")
_MsanSwitchMFDBDescription_Type = DisplayString
_MsanSwitchMFDBDescription_Object = MibTableColumn
msanSwitchMFDBDescription = _MsanSwitchMFDBDescription_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 100, 12, 1, 5),
    _MsanSwitchMFDBDescription_Type()
)
msanSwitchMFDBDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanSwitchMFDBDescription.setStatus("current")
_MsanSwitchMFDBForwardingPortMask_Type = PortMask
_MsanSwitchMFDBForwardingPortMask_Object = MibTableColumn
msanSwitchMFDBForwardingPortMask = _MsanSwitchMFDBForwardingPortMask_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 100, 12, 1, 6),
    _MsanSwitchMFDBForwardingPortMask_Type()
)
msanSwitchMFDBForwardingPortMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanSwitchMFDBForwardingPortMask.setStatus("current")
_MsanSwitchMFDBFilteringPortMask_Type = PortMask
_MsanSwitchMFDBFilteringPortMask_Object = MibTableColumn
msanSwitchMFDBFilteringPortMask = _MsanSwitchMFDBFilteringPortMask_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 100, 12, 1, 7),
    _MsanSwitchMFDBFilteringPortMask_Type()
)
msanSwitchMFDBFilteringPortMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanSwitchMFDBFilteringPortMask.setStatus("current")
_MsanFiltering_ObjectIdentity = ObjectIdentity
msanFiltering = _MsanFiltering_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 101)
)
_MsanFilteringGlobal_ObjectIdentity = ObjectIdentity
msanFilteringGlobal = _MsanFilteringGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 101, 2)
)
_MsanFilteringFilterTable_Object = MibTable
msanFilteringFilterTable = _MsanFilteringFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 101, 3)
)
if mibBuilder.loadTexts:
    msanFilteringFilterTable.setStatus("deprecated")
_MsanFilteringFilterEntry_Object = MibTableRow
msanFilteringFilterEntry = _MsanFilteringFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 101, 3, 1)
)
msanFilteringFilterEntry.setIndexNames(
    (0, "ISKRATEL-MSAN-MIB", "msanFilteringFilterId"),
)
if mibBuilder.loadTexts:
    msanFilteringFilterEntry.setStatus("deprecated")


class _MsanFilteringFilterId_Type(Integer32):
    """Custom type msanFilteringFilterId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
        ValueRangeConstraint(301, 500),
    )


_MsanFilteringFilterId_Type.__name__ = "Integer32"
_MsanFilteringFilterId_Object = MibTableColumn
msanFilteringFilterId = _MsanFilteringFilterId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 101, 3, 1, 1),
    _MsanFilteringFilterId_Type()
)
msanFilteringFilterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanFilteringFilterId.setStatus("deprecated")
_MsanFilteringFilterName_Type = OctetString
_MsanFilteringFilterName_Object = MibTableColumn
msanFilteringFilterName = _MsanFilteringFilterName_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 101, 3, 1, 2),
    _MsanFilteringFilterName_Type()
)
msanFilteringFilterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanFilteringFilterName.setStatus("deprecated")


class _MsanFilteringFilterType_Type(Integer32):
    """Custom type msanFilteringFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_MsanFilteringFilterType_Type.__name__ = "Integer32"
_MsanFilteringFilterType_Object = MibTableColumn
msanFilteringFilterType = _MsanFilteringFilterType_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 101, 3, 1, 3),
    _MsanFilteringFilterType_Type()
)
msanFilteringFilterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanFilteringFilterType.setStatus("deprecated")


class _MsanFilteringFilterRowStatus_Type(RowStatus):
    """Custom type msanFilteringFilterRowStatus based on RowStatus"""


_MsanFilteringFilterRowStatus_Object = MibTableColumn
msanFilteringFilterRowStatus = _MsanFilteringFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 101, 3, 1, 4),
    _MsanFilteringFilterRowStatus_Type()
)
msanFilteringFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanFilteringFilterRowStatus.setStatus("deprecated")
_MsanFilteringAssignFilterTable_Object = MibTable
msanFilteringAssignFilterTable = _MsanFilteringAssignFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 101, 4)
)
if mibBuilder.loadTexts:
    msanFilteringAssignFilterTable.setStatus("deprecated")
_MsanFilteringAssignFilterEntry_Object = MibTableRow
msanFilteringAssignFilterEntry = _MsanFilteringAssignFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 101, 4, 1)
)
msanFilteringAssignFilterEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ISKRATEL-MSAN-MIB", "msanFilteringFilterId"),
)
if mibBuilder.loadTexts:
    msanFilteringAssignFilterEntry.setStatus("deprecated")


class _MsanFilteringAssignFilterVid_Type(Integer32):
    """Custom type msanFilteringAssignFilterVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_MsanFilteringAssignFilterVid_Type.__name__ = "Integer32"
_MsanFilteringAssignFilterVid_Object = MibTableColumn
msanFilteringAssignFilterVid = _MsanFilteringAssignFilterVid_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 101, 4, 1, 1),
    _MsanFilteringAssignFilterVid_Type()
)
msanFilteringAssignFilterVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanFilteringAssignFilterVid.setStatus("deprecated")


class _MsanFilteringAssignFilterCos_Type(Integer32):
    """Custom type msanFilteringAssignFilterCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MsanFilteringAssignFilterCos_Type.__name__ = "Integer32"
_MsanFilteringAssignFilterCos_Object = MibTableColumn
msanFilteringAssignFilterCos = _MsanFilteringAssignFilterCos_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 101, 4, 1, 2),
    _MsanFilteringAssignFilterCos_Type()
)
msanFilteringAssignFilterCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanFilteringAssignFilterCos.setStatus("deprecated")


class _MsanFilteringAssignFilterDscp_Type(Integer32):
    """Custom type msanFilteringAssignFilterDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_MsanFilteringAssignFilterDscp_Type.__name__ = "Integer32"
_MsanFilteringAssignFilterDscp_Object = MibTableColumn
msanFilteringAssignFilterDscp = _MsanFilteringAssignFilterDscp_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 101, 4, 1, 3),
    _MsanFilteringAssignFilterDscp_Type()
)
msanFilteringAssignFilterDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanFilteringAssignFilterDscp.setStatus("deprecated")


class _MsanFilteringAssignFilterPrec_Type(Integer32):
    """Custom type msanFilteringAssignFilterPrec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MsanFilteringAssignFilterPrec_Type.__name__ = "Integer32"
_MsanFilteringAssignFilterPrec_Object = MibTableColumn
msanFilteringAssignFilterPrec = _MsanFilteringAssignFilterPrec_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 101, 4, 1, 4),
    _MsanFilteringAssignFilterPrec_Type()
)
msanFilteringAssignFilterPrec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanFilteringAssignFilterPrec.setStatus("deprecated")


class _MsanFilteringAssignFilterRowStatus_Type(RowStatus):
    """Custom type msanFilteringAssignFilterRowStatus based on RowStatus"""


_MsanFilteringAssignFilterRowStatus_Object = MibTableColumn
msanFilteringAssignFilterRowStatus = _MsanFilteringAssignFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 101, 4, 1, 5),
    _MsanFilteringAssignFilterRowStatus_Type()
)
msanFilteringAssignFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanFilteringAssignFilterRowStatus.setStatus("deprecated")
_MsanFilteringRuleTable_Object = MibTable
msanFilteringRuleTable = _MsanFilteringRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 101, 5)
)
if mibBuilder.loadTexts:
    msanFilteringRuleTable.setStatus("deprecated")
_MsanFilteringRuleEntry_Object = MibTableRow
msanFilteringRuleEntry = _MsanFilteringRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 101, 5, 1)
)
msanFilteringRuleEntry.setIndexNames(
    (0, "ISKRATEL-MSAN-MIB", "msanFilteringRuleId"),
    (0, "ISKRATEL-MSAN-MIB", "msanFilteringFilterId"),
)
if mibBuilder.loadTexts:
    msanFilteringRuleEntry.setStatus("deprecated")


class _MsanFilteringRuleId_Type(Integer32):
    """Custom type msanFilteringRuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MsanFilteringRuleId_Type.__name__ = "Integer32"
_MsanFilteringRuleId_Object = MibTableColumn
msanFilteringRuleId = _MsanFilteringRuleId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 101, 5, 1, 1),
    _MsanFilteringRuleId_Type()
)
msanFilteringRuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanFilteringRuleId.setStatus("deprecated")


class _MsanFilteringRuleResponse_Type(Integer32):
    """Custom type msanFilteringRuleResponse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("deny", 2))
    )


_MsanFilteringRuleResponse_Type.__name__ = "Integer32"
_MsanFilteringRuleResponse_Object = MibTableColumn
msanFilteringRuleResponse = _MsanFilteringRuleResponse_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 101, 5, 1, 2),
    _MsanFilteringRuleResponse_Type()
)
msanFilteringRuleResponse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanFilteringRuleResponse.setStatus("deprecated")
_MsanFilteringRuleFromMac_Type = MacAddress
_MsanFilteringRuleFromMac_Object = MibTableColumn
msanFilteringRuleFromMac = _MsanFilteringRuleFromMac_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 101, 5, 1, 3),
    _MsanFilteringRuleFromMac_Type()
)
msanFilteringRuleFromMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanFilteringRuleFromMac.setStatus("deprecated")
_MsanFilteringRuleFromMacMask_Type = MacAddress
_MsanFilteringRuleFromMacMask_Object = MibTableColumn
msanFilteringRuleFromMacMask = _MsanFilteringRuleFromMacMask_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 101, 5, 1, 4),
    _MsanFilteringRuleFromMacMask_Type()
)
msanFilteringRuleFromMacMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanFilteringRuleFromMacMask.setStatus("deprecated")
_MsanFilteringRuleFromIp_Type = IpAddress
_MsanFilteringRuleFromIp_Object = MibTableColumn
msanFilteringRuleFromIp = _MsanFilteringRuleFromIp_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 101, 5, 1, 5),
    _MsanFilteringRuleFromIp_Type()
)
msanFilteringRuleFromIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanFilteringRuleFromIp.setStatus("deprecated")
_MsanFilteringRuleFromMask_Type = IpAddress
_MsanFilteringRuleFromMask_Object = MibTableColumn
msanFilteringRuleFromMask = _MsanFilteringRuleFromMask_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 101, 5, 1, 6),
    _MsanFilteringRuleFromMask_Type()
)
msanFilteringRuleFromMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanFilteringRuleFromMask.setStatus("deprecated")


class _MsanFilteringRuleFromPortLow_Type(Unsigned32):
    """Custom type msanFilteringRuleFromPortLow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MsanFilteringRuleFromPortLow_Type.__name__ = "Unsigned32"
_MsanFilteringRuleFromPortLow_Object = MibTableColumn
msanFilteringRuleFromPortLow = _MsanFilteringRuleFromPortLow_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 101, 5, 1, 7),
    _MsanFilteringRuleFromPortLow_Type()
)
msanFilteringRuleFromPortLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanFilteringRuleFromPortLow.setStatus("deprecated")


class _MsanFilteringRuleFromPortHigh_Type(Unsigned32):
    """Custom type msanFilteringRuleFromPortHigh based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MsanFilteringRuleFromPortHigh_Type.__name__ = "Unsigned32"
_MsanFilteringRuleFromPortHigh_Object = MibTableColumn
msanFilteringRuleFromPortHigh = _MsanFilteringRuleFromPortHigh_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 101, 5, 1, 8),
    _MsanFilteringRuleFromPortHigh_Type()
)
msanFilteringRuleFromPortHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanFilteringRuleFromPortHigh.setStatus("deprecated")
_MsanFilteringRuleToMac_Type = MacAddress
_MsanFilteringRuleToMac_Object = MibTableColumn
msanFilteringRuleToMac = _MsanFilteringRuleToMac_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 101, 5, 1, 9),
    _MsanFilteringRuleToMac_Type()
)
msanFilteringRuleToMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanFilteringRuleToMac.setStatus("deprecated")
_MsanFilteringRuleToMacMask_Type = MacAddress
_MsanFilteringRuleToMacMask_Object = MibTableColumn
msanFilteringRuleToMacMask = _MsanFilteringRuleToMacMask_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 101, 5, 1, 10),
    _MsanFilteringRuleToMacMask_Type()
)
msanFilteringRuleToMacMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanFilteringRuleToMacMask.setStatus("deprecated")
_MsanFilteringRuleToIp_Type = IpAddress
_MsanFilteringRuleToIp_Object = MibTableColumn
msanFilteringRuleToIp = _MsanFilteringRuleToIp_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 101, 5, 1, 11),
    _MsanFilteringRuleToIp_Type()
)
msanFilteringRuleToIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanFilteringRuleToIp.setStatus("deprecated")
_MsanFilteringRuleToMask_Type = IpAddress
_MsanFilteringRuleToMask_Object = MibTableColumn
msanFilteringRuleToMask = _MsanFilteringRuleToMask_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 101, 5, 1, 12),
    _MsanFilteringRuleToMask_Type()
)
msanFilteringRuleToMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanFilteringRuleToMask.setStatus("deprecated")


class _MsanFilteringRuleToPortLow_Type(Unsigned32):
    """Custom type msanFilteringRuleToPortLow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MsanFilteringRuleToPortLow_Type.__name__ = "Unsigned32"
_MsanFilteringRuleToPortLow_Object = MibTableColumn
msanFilteringRuleToPortLow = _MsanFilteringRuleToPortLow_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 101, 5, 1, 13),
    _MsanFilteringRuleToPortLow_Type()
)
msanFilteringRuleToPortLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanFilteringRuleToPortLow.setStatus("deprecated")


class _MsanFilteringRuleToPortHigh_Type(Unsigned32):
    """Custom type msanFilteringRuleToPortHigh based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MsanFilteringRuleToPortHigh_Type.__name__ = "Unsigned32"
_MsanFilteringRuleToPortHigh_Object = MibTableColumn
msanFilteringRuleToPortHigh = _MsanFilteringRuleToPortHigh_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 101, 5, 1, 14),
    _MsanFilteringRuleToPortHigh_Type()
)
msanFilteringRuleToPortHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanFilteringRuleToPortHigh.setStatus("deprecated")
_MsanFilteringRuleEtherProto_Type = OctetString
_MsanFilteringRuleEtherProto_Object = MibTableColumn
msanFilteringRuleEtherProto = _MsanFilteringRuleEtherProto_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 101, 5, 1, 15),
    _MsanFilteringRuleEtherProto_Type()
)
msanFilteringRuleEtherProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanFilteringRuleEtherProto.setStatus("deprecated")
_MsanFilteringRuleIpProto_Type = OctetString
_MsanFilteringRuleIpProto_Object = MibTableColumn
msanFilteringRuleIpProto = _MsanFilteringRuleIpProto_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 101, 5, 1, 16),
    _MsanFilteringRuleIpProto_Type()
)
msanFilteringRuleIpProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanFilteringRuleIpProto.setStatus("deprecated")


class _MsanFilteringRuleIcmType_Type(Unsigned32):
    """Custom type msanFilteringRuleIcmType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanFilteringRuleIcmType_Type.__name__ = "Unsigned32"
_MsanFilteringRuleIcmType_Object = MibTableColumn
msanFilteringRuleIcmType = _MsanFilteringRuleIcmType_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 101, 5, 1, 17),
    _MsanFilteringRuleIcmType_Type()
)
msanFilteringRuleIcmType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanFilteringRuleIcmType.setStatus("deprecated")


class _MsanFilteringRulePrec_Type(Unsigned32):
    """Custom type msanFilteringRulePrec based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MsanFilteringRulePrec_Type.__name__ = "Unsigned32"
_MsanFilteringRulePrec_Object = MibTableColumn
msanFilteringRulePrec = _MsanFilteringRulePrec_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 101, 5, 1, 18),
    _MsanFilteringRulePrec_Type()
)
msanFilteringRulePrec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanFilteringRulePrec.setStatus("deprecated")


class _MsanFilteringRuleTos_Type(Unsigned32):
    """Custom type msanFilteringRuleTos based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MsanFilteringRuleTos_Type.__name__ = "Unsigned32"
_MsanFilteringRuleTos_Object = MibTableColumn
msanFilteringRuleTos = _MsanFilteringRuleTos_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 101, 5, 1, 19),
    _MsanFilteringRuleTos_Type()
)
msanFilteringRuleTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanFilteringRuleTos.setStatus("deprecated")


class _MsanFilteringRuleVid_Type(Unsigned32):
    """Custom type msanFilteringRuleVid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_MsanFilteringRuleVid_Type.__name__ = "Unsigned32"
_MsanFilteringRuleVid_Object = MibTableColumn
msanFilteringRuleVid = _MsanFilteringRuleVid_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 101, 5, 1, 20),
    _MsanFilteringRuleVid_Type()
)
msanFilteringRuleVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanFilteringRuleVid.setStatus("deprecated")


class _MsanFilteringRuleCos_Type(Unsigned32):
    """Custom type msanFilteringRuleCos based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MsanFilteringRuleCos_Type.__name__ = "Unsigned32"
_MsanFilteringRuleCos_Object = MibTableColumn
msanFilteringRuleCos = _MsanFilteringRuleCos_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 101, 5, 1, 21),
    _MsanFilteringRuleCos_Type()
)
msanFilteringRuleCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanFilteringRuleCos.setStatus("deprecated")


class _MsanFilteringRuleTag_Type(Integer32):
    """Custom type msanFilteringRuleTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("qinq-tagged", 3),
          ("tagged", 2),
          ("untagged", 1))
    )


_MsanFilteringRuleTag_Type.__name__ = "Integer32"
_MsanFilteringRuleTag_Object = MibTableColumn
msanFilteringRuleTag = _MsanFilteringRuleTag_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 101, 5, 1, 22),
    _MsanFilteringRuleTag_Type()
)
msanFilteringRuleTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanFilteringRuleTag.setStatus("deprecated")


class _MsanFilteringRuleRowStatus_Type(RowStatus):
    """Custom type msanFilteringRuleRowStatus based on RowStatus"""


_MsanFilteringRuleRowStatus_Object = MibTableColumn
msanFilteringRuleRowStatus = _MsanFilteringRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 101, 5, 1, 23),
    _MsanFilteringRuleRowStatus_Type()
)
msanFilteringRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanFilteringRuleRowStatus.setStatus("deprecated")
_MsanFilteringAttachedFilterTable_Object = MibTable
msanFilteringAttachedFilterTable = _MsanFilteringAttachedFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 101, 6)
)
if mibBuilder.loadTexts:
    msanFilteringAttachedFilterTable.setStatus("deprecated")
_MsanFilteringAttachedFilterEntry_Object = MibTableRow
msanFilteringAttachedFilterEntry = _MsanFilteringAttachedFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 101, 6, 1)
)
msanFilteringAttachedFilterEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ISKRATEL-MSAN-MIB", "msanFilteringFilterId"),
)
if mibBuilder.loadTexts:
    msanFilteringAttachedFilterEntry.setStatus("deprecated")


class _MsanFilteringAttachedFilterDirect_Type(Integer32):
    """Custom type msanFilteringAttachedFilterDirect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 2))
    )


_MsanFilteringAttachedFilterDirect_Type.__name__ = "Integer32"
_MsanFilteringAttachedFilterDirect_Object = MibTableColumn
msanFilteringAttachedFilterDirect = _MsanFilteringAttachedFilterDirect_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 101, 6, 1, 1),
    _MsanFilteringAttachedFilterDirect_Type()
)
msanFilteringAttachedFilterDirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanFilteringAttachedFilterDirect.setStatus("deprecated")
_MsanFilteringAttachedFilterRowStatus_Type = RowStatus
_MsanFilteringAttachedFilterRowStatus_Object = MibTableColumn
msanFilteringAttachedFilterRowStatus = _MsanFilteringAttachedFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 101, 6, 1, 2),
    _MsanFilteringAttachedFilterRowStatus_Type()
)
msanFilteringAttachedFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanFilteringAttachedFilterRowStatus.setStatus("deprecated")
_MsanBridge_ObjectIdentity = ObjectIdentity
msanBridge = _MsanBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 102)
)
_MsanBridgeGlobal_ObjectIdentity = ObjectIdentity
msanBridgeGlobal = _MsanBridgeGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 102, 1)
)


class _MsanBridgeMode_Type(Integer32):
    """Custom type msanBridgeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bridge", 1),
          ("ccx", 2))
    )


_MsanBridgeMode_Type.__name__ = "Integer32"
_MsanBridgeMode_Object = MibScalar
msanBridgeMode = _MsanBridgeMode_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 102, 1, 1),
    _MsanBridgeMode_Type()
)
msanBridgeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanBridgeMode.setStatus("deprecated")


class _MsanBridgeMacTableSize_Type(Integer32):
    """Custom type msanBridgeMacTableSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 4095),
    )


_MsanBridgeMacTableSize_Type.__name__ = "Integer32"
_MsanBridgeMacTableSize_Object = MibScalar
msanBridgeMacTableSize = _MsanBridgeMacTableSize_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 102, 1, 2),
    _MsanBridgeMacTableSize_Type()
)
msanBridgeMacTableSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanBridgeMacTableSize.setStatus("deprecated")


class _MsanBridgeRedAdminMode_Type(Integer32):
    """Custom type msanBridgeRedAdminMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanBridgeRedAdminMode_Type.__name__ = "Integer32"
_MsanBridgeRedAdminMode_Object = MibScalar
msanBridgeRedAdminMode = _MsanBridgeRedAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 102, 1, 3),
    _MsanBridgeRedAdminMode_Type()
)
msanBridgeRedAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanBridgeRedAdminMode.setStatus("deprecated")
_MsanBridgeCCXTable_Object = MibTable
msanBridgeCCXTable = _MsanBridgeCCXTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 102, 2)
)
if mibBuilder.loadTexts:
    msanBridgeCCXTable.setStatus("deprecated")
_MsanBridgeCCXEntry_Object = MibTableRow
msanBridgeCCXEntry = _MsanBridgeCCXEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 102, 2, 1)
)
msanBridgeCCXEntry.setIndexNames(
    (0, "ISKRATEL-MSAN-MIB", "msanBridgeCCXInterface1"),
    (0, "ISKRATEL-MSAN-MIB", "msanBridgeCCXInterface2"),
)
if mibBuilder.loadTexts:
    msanBridgeCCXEntry.setStatus("deprecated")
_MsanBridgeCCXInterface1_Type = InterfaceIndex
_MsanBridgeCCXInterface1_Object = MibTableColumn
msanBridgeCCXInterface1 = _MsanBridgeCCXInterface1_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 102, 2, 1, 1),
    _MsanBridgeCCXInterface1_Type()
)
msanBridgeCCXInterface1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanBridgeCCXInterface1.setStatus("deprecated")
_MsanBridgeCCXInterface2_Type = InterfaceIndex
_MsanBridgeCCXInterface2_Object = MibTableColumn
msanBridgeCCXInterface2 = _MsanBridgeCCXInterface2_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 102, 2, 1, 2),
    _MsanBridgeCCXInterface2_Type()
)
msanBridgeCCXInterface2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanBridgeCCXInterface2.setStatus("deprecated")
_MsanBridgeCCXRowStatus_Type = RowStatus
_MsanBridgeCCXRowStatus_Object = MibTableColumn
msanBridgeCCXRowStatus = _MsanBridgeCCXRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 102, 2, 1, 3),
    _MsanBridgeCCXRowStatus_Type()
)
msanBridgeCCXRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanBridgeCCXRowStatus.setStatus("deprecated")
_MsanIPSG_ObjectIdentity = ObjectIdentity
msanIPSG = _MsanIPSG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 103)
)
_MsanIPSGGlobal_ObjectIdentity = ObjectIdentity
msanIPSGGlobal = _MsanIPSGGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 103, 1)
)


class _MsanIPSGAdminMode_Type(Integer32):
    """Custom type msanIPSGAdminMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanIPSGAdminMode_Type.__name__ = "Integer32"
_MsanIPSGAdminMode_Object = MibScalar
msanIPSGAdminMode = _MsanIPSGAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 103, 1, 1),
    _MsanIPSGAdminMode_Type()
)
msanIPSGAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIPSGAdminMode.setStatus("current")


class _MsanIPSGStoreAdminMode_Type(Integer32):
    """Custom type msanIPSGStoreAdminMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanIPSGStoreAdminMode_Type.__name__ = "Integer32"
_MsanIPSGStoreAdminMode_Object = MibScalar
msanIPSGStoreAdminMode = _MsanIPSGStoreAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 103, 1, 2),
    _MsanIPSGStoreAdminMode_Type()
)
msanIPSGStoreAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIPSGStoreAdminMode.setStatus("current")


class _MsanIPSGIpv6AdminMode_Type(Integer32):
    """Custom type msanIPSGIpv6AdminMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanIPSGIpv6AdminMode_Type.__name__ = "Integer32"
_MsanIPSGIpv6AdminMode_Object = MibScalar
msanIPSGIpv6AdminMode = _MsanIPSGIpv6AdminMode_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 103, 1, 3),
    _MsanIPSGIpv6AdminMode_Type()
)
msanIPSGIpv6AdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIPSGIpv6AdminMode.setStatus("current")


class _MsanIPSGClearDynamicBinds_Type(Integer32):
    """Custom type msanIPSGClearDynamicBinds based on Integer32"""
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
        *(("clear-all", 2),
          ("clear-dhcpv4", 3),
          ("clear-dhcpv6", 4),
          ("clear-nd", 5),
          ("disable", 1))
    )


_MsanIPSGClearDynamicBinds_Type.__name__ = "Integer32"
_MsanIPSGClearDynamicBinds_Object = MibScalar
msanIPSGClearDynamicBinds = _MsanIPSGClearDynamicBinds_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 103, 1, 4),
    _MsanIPSGClearDynamicBinds_Type()
)
msanIPSGClearDynamicBinds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIPSGClearDynamicBinds.setStatus("current")
_MsanIPSGIntfTable_Object = MibTable
msanIPSGIntfTable = _MsanIPSGIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 103, 2)
)
if mibBuilder.loadTexts:
    msanIPSGIntfTable.setStatus("current")
_MsanIPSGIntfEntry_Object = MibTableRow
msanIPSGIntfEntry = _MsanIPSGIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 103, 2, 1)
)
msanIPSGIntfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    msanIPSGIntfEntry.setStatus("current")


class _MsanIPSGIntfAdminMode_Type(Integer32):
    """Custom type msanIPSGIntfAdminMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanIPSGIntfAdminMode_Type.__name__ = "Integer32"
_MsanIPSGIntfAdminMode_Object = MibTableColumn
msanIPSGIntfAdminMode = _MsanIPSGIntfAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 103, 2, 1, 1),
    _MsanIPSGIntfAdminMode_Type()
)
msanIPSGIntfAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIPSGIntfAdminMode.setStatus("current")


class _MsanIPSGIntfBindsLimit_Type(Integer32):
    """Custom type msanIPSGIntfBindsLimit based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MsanIPSGIntfBindsLimit_Type.__name__ = "Integer32"
_MsanIPSGIntfBindsLimit_Object = MibTableColumn
msanIPSGIntfBindsLimit = _MsanIPSGIntfBindsLimit_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 103, 2, 1, 2),
    _MsanIPSGIntfBindsLimit_Type()
)
msanIPSGIntfBindsLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIPSGIntfBindsLimit.setStatus("current")


class _MsanIPSGIntfFilteringMode_Type(Integer32):
    """Custom type msanIPSGIntfFilteringMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipmac", 2),
          ("iponly", 1))
    )


_MsanIPSGIntfFilteringMode_Type.__name__ = "Integer32"
_MsanIPSGIntfFilteringMode_Object = MibTableColumn
msanIPSGIntfFilteringMode = _MsanIPSGIntfFilteringMode_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 103, 2, 1, 3),
    _MsanIPSGIntfFilteringMode_Type()
)
msanIPSGIntfFilteringMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIPSGIntfFilteringMode.setStatus("current")


class _MsanIPSGIntfIpv6AdminMode_Type(Integer32):
    """Custom type msanIPSGIntfIpv6AdminMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanIPSGIntfIpv6AdminMode_Type.__name__ = "Integer32"
_MsanIPSGIntfIpv6AdminMode_Object = MibTableColumn
msanIPSGIntfIpv6AdminMode = _MsanIPSGIntfIpv6AdminMode_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 103, 2, 1, 4),
    _MsanIPSGIntfIpv6AdminMode_Type()
)
msanIPSGIntfIpv6AdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIPSGIntfIpv6AdminMode.setStatus("current")


class _MsanIPSGIntfBindsLimitDhcpv6_Type(Integer32):
    """Custom type msanIPSGIntfBindsLimitDhcpv6 based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MsanIPSGIntfBindsLimitDhcpv6_Type.__name__ = "Integer32"
_MsanIPSGIntfBindsLimitDhcpv6_Object = MibTableColumn
msanIPSGIntfBindsLimitDhcpv6 = _MsanIPSGIntfBindsLimitDhcpv6_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 103, 2, 1, 5),
    _MsanIPSGIntfBindsLimitDhcpv6_Type()
)
msanIPSGIntfBindsLimitDhcpv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIPSGIntfBindsLimitDhcpv6.setStatus("current")


class _MsanIPSGIntfBindsLimitND_Type(Integer32):
    """Custom type msanIPSGIntfBindsLimitND based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MsanIPSGIntfBindsLimitND_Type.__name__ = "Integer32"
_MsanIPSGIntfBindsLimitND_Object = MibTableColumn
msanIPSGIntfBindsLimitND = _MsanIPSGIntfBindsLimitND_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 103, 2, 1, 6),
    _MsanIPSGIntfBindsLimitND_Type()
)
msanIPSGIntfBindsLimitND.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIPSGIntfBindsLimitND.setStatus("current")


class _MsanIPSGIntfClearDynamicBinds_Type(Integer32):
    """Custom type msanIPSGIntfClearDynamicBinds based on Integer32"""
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
        *(("clear-all", 2),
          ("clear-dhcpv4", 3),
          ("clear-dhcpv6", 4),
          ("clear-nd", 5),
          ("disable", 1))
    )


_MsanIPSGIntfClearDynamicBinds_Type.__name__ = "Integer32"
_MsanIPSGIntfClearDynamicBinds_Object = MibTableColumn
msanIPSGIntfClearDynamicBinds = _MsanIPSGIntfClearDynamicBinds_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 103, 2, 1, 7),
    _MsanIPSGIntfClearDynamicBinds_Type()
)
msanIPSGIntfClearDynamicBinds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIPSGIntfClearDynamicBinds.setStatus("current")
_MsanIPSGBindingsTable_Object = MibTable
msanIPSGBindingsTable = _MsanIPSGBindingsTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 103, 3)
)
if mibBuilder.loadTexts:
    msanIPSGBindingsTable.setStatus("deprecated")
_MsanIPSGBindingsEntry_Object = MibTableRow
msanIPSGBindingsEntry = _MsanIPSGBindingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 103, 3, 1)
)
msanIPSGBindingsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ISKRATEL-MSAN-MIB", "msanIPSGBindVlan"),
    (0, "ISKRATEL-MSAN-MIB", "msanIPSGBindMac"),
)
if mibBuilder.loadTexts:
    msanIPSGBindingsEntry.setStatus("deprecated")
_MsanIPSGBindIp_Type = IpAddress
_MsanIPSGBindIp_Object = MibTableColumn
msanIPSGBindIp = _MsanIPSGBindIp_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 103, 3, 1, 1),
    _MsanIPSGBindIp_Type()
)
msanIPSGBindIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIPSGBindIp.setStatus("deprecated")
_MsanIPSGBindVlan_Type = VlanIndex
_MsanIPSGBindVlan_Object = MibTableColumn
msanIPSGBindVlan = _MsanIPSGBindVlan_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 103, 3, 1, 2),
    _MsanIPSGBindVlan_Type()
)
msanIPSGBindVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanIPSGBindVlan.setStatus("deprecated")
_MsanIPSGBindMac_Type = MacAddress
_MsanIPSGBindMac_Object = MibTableColumn
msanIPSGBindMac = _MsanIPSGBindMac_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 103, 3, 1, 3),
    _MsanIPSGBindMac_Type()
)
msanIPSGBindMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanIPSGBindMac.setStatus("deprecated")
_MsanIPSGBindLeaseRemainingTime_Type = TimeTicks
_MsanIPSGBindLeaseRemainingTime_Object = MibTableColumn
msanIPSGBindLeaseRemainingTime = _MsanIPSGBindLeaseRemainingTime_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 103, 3, 1, 4),
    _MsanIPSGBindLeaseRemainingTime_Type()
)
msanIPSGBindLeaseRemainingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanIPSGBindLeaseRemainingTime.setStatus("deprecated")


class _MsanIPSGBindType_Type(Integer32):
    """Custom type msanIPSGBindType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_MsanIPSGBindType_Type.__name__ = "Integer32"
_MsanIPSGBindType_Object = MibTableColumn
msanIPSGBindType = _MsanIPSGBindType_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 103, 3, 1, 5),
    _MsanIPSGBindType_Type()
)
msanIPSGBindType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanIPSGBindType.setStatus("deprecated")
_MsanIPSGBindMatchedFrames_Type = Counter32
_MsanIPSGBindMatchedFrames_Object = MibTableColumn
msanIPSGBindMatchedFrames = _MsanIPSGBindMatchedFrames_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 103, 3, 1, 6),
    _MsanIPSGBindMatchedFrames_Type()
)
msanIPSGBindMatchedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanIPSGBindMatchedFrames.setStatus("deprecated")
_MsanIPSGBindRowStatus_Type = RowStatus
_MsanIPSGBindRowStatus_Object = MibTableColumn
msanIPSGBindRowStatus = _MsanIPSGBindRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 103, 3, 1, 7),
    _MsanIPSGBindRowStatus_Type()
)
msanIPSGBindRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanIPSGBindRowStatus.setStatus("deprecated")
_MsanIPSGIpv4PortStaticBindTable_Object = MibTable
msanIPSGIpv4PortStaticBindTable = _MsanIPSGIpv4PortStaticBindTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 103, 4)
)
if mibBuilder.loadTexts:
    msanIPSGIpv4PortStaticBindTable.setStatus("current")
_MsanIPSGIpv4PortStaticBindEntry_Object = MibTableRow
msanIPSGIpv4PortStaticBindEntry = _MsanIPSGIpv4PortStaticBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 103, 4, 1)
)
msanIPSGIpv4PortStaticBindEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ISKRATEL-MSAN-MIB", "msanIPSGIpv4PortStaticBindMacAddress"),
    (0, "ISKRATEL-MSAN-MIB", "msanIPSGIpv4PortStaticBindVlanId"),
    (0, "ISKRATEL-MSAN-MIB", "msanIPSGIpv4PortStaticBindIpAddress"),
)
if mibBuilder.loadTexts:
    msanIPSGIpv4PortStaticBindEntry.setStatus("current")
_MsanIPSGIpv4PortStaticBindMacAddress_Type = MacAddress
_MsanIPSGIpv4PortStaticBindMacAddress_Object = MibTableColumn
msanIPSGIpv4PortStaticBindMacAddress = _MsanIPSGIpv4PortStaticBindMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 103, 4, 1, 1),
    _MsanIPSGIpv4PortStaticBindMacAddress_Type()
)
msanIPSGIpv4PortStaticBindMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanIPSGIpv4PortStaticBindMacAddress.setStatus("current")
_MsanIPSGIpv4PortStaticBindVlanId_Type = VlanIndex
_MsanIPSGIpv4PortStaticBindVlanId_Object = MibTableColumn
msanIPSGIpv4PortStaticBindVlanId = _MsanIPSGIpv4PortStaticBindVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 103, 4, 1, 2),
    _MsanIPSGIpv4PortStaticBindVlanId_Type()
)
msanIPSGIpv4PortStaticBindVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanIPSGIpv4PortStaticBindVlanId.setStatus("current")
_MsanIPSGIpv4PortStaticBindIpAddress_Type = InetAddressIPv4
_MsanIPSGIpv4PortStaticBindIpAddress_Object = MibTableColumn
msanIPSGIpv4PortStaticBindIpAddress = _MsanIPSGIpv4PortStaticBindIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 103, 4, 1, 3),
    _MsanIPSGIpv4PortStaticBindIpAddress_Type()
)
msanIPSGIpv4PortStaticBindIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanIPSGIpv4PortStaticBindIpAddress.setStatus("current")
_MsanIPSGIpv4PortStaticBindMatchedFrames_Type = Counter32
_MsanIPSGIpv4PortStaticBindMatchedFrames_Object = MibTableColumn
msanIPSGIpv4PortStaticBindMatchedFrames = _MsanIPSGIpv4PortStaticBindMatchedFrames_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 103, 4, 1, 4),
    _MsanIPSGIpv4PortStaticBindMatchedFrames_Type()
)
msanIPSGIpv4PortStaticBindMatchedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanIPSGIpv4PortStaticBindMatchedFrames.setStatus("current")
_MsanIPSGIpv4PortStaticBindRowStatus_Type = RowStatus
_MsanIPSGIpv4PortStaticBindRowStatus_Object = MibTableColumn
msanIPSGIpv4PortStaticBindRowStatus = _MsanIPSGIpv4PortStaticBindRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 103, 4, 1, 5),
    _MsanIPSGIpv4PortStaticBindRowStatus_Type()
)
msanIPSGIpv4PortStaticBindRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanIPSGIpv4PortStaticBindRowStatus.setStatus("current")
_MsanIPSGIpv6PortStaticBindTable_Object = MibTable
msanIPSGIpv6PortStaticBindTable = _MsanIPSGIpv6PortStaticBindTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 103, 5)
)
if mibBuilder.loadTexts:
    msanIPSGIpv6PortStaticBindTable.setStatus("current")
_MsanIPSGIpv6PortStaticBindEntry_Object = MibTableRow
msanIPSGIpv6PortStaticBindEntry = _MsanIPSGIpv6PortStaticBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 103, 5, 1)
)
msanIPSGIpv6PortStaticBindEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ISKRATEL-MSAN-MIB", "msanIPSGIpv6PortStaticBindMacAddress"),
    (0, "ISKRATEL-MSAN-MIB", "msanIPSGIpv6PortStaticBindVlanId"),
    (0, "ISKRATEL-MSAN-MIB", "msanIPSGIpv6PortStaticBindIpAddress"),
)
if mibBuilder.loadTexts:
    msanIPSGIpv6PortStaticBindEntry.setStatus("current")
_MsanIPSGIpv6PortStaticBindMacAddress_Type = MacAddress
_MsanIPSGIpv6PortStaticBindMacAddress_Object = MibTableColumn
msanIPSGIpv6PortStaticBindMacAddress = _MsanIPSGIpv6PortStaticBindMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 103, 5, 1, 1),
    _MsanIPSGIpv6PortStaticBindMacAddress_Type()
)
msanIPSGIpv6PortStaticBindMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanIPSGIpv6PortStaticBindMacAddress.setStatus("current")
_MsanIPSGIpv6PortStaticBindVlanId_Type = VlanIndex
_MsanIPSGIpv6PortStaticBindVlanId_Object = MibTableColumn
msanIPSGIpv6PortStaticBindVlanId = _MsanIPSGIpv6PortStaticBindVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 103, 5, 1, 2),
    _MsanIPSGIpv6PortStaticBindVlanId_Type()
)
msanIPSGIpv6PortStaticBindVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanIPSGIpv6PortStaticBindVlanId.setStatus("current")
_MsanIPSGIpv6PortStaticBindIpAddress_Type = InetAddressIPv6
_MsanIPSGIpv6PortStaticBindIpAddress_Object = MibTableColumn
msanIPSGIpv6PortStaticBindIpAddress = _MsanIPSGIpv6PortStaticBindIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 103, 5, 1, 3),
    _MsanIPSGIpv6PortStaticBindIpAddress_Type()
)
msanIPSGIpv6PortStaticBindIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanIPSGIpv6PortStaticBindIpAddress.setStatus("current")
_MsanIPSGIpv6PortStaticBindMatchedFrames_Type = Counter32
_MsanIPSGIpv6PortStaticBindMatchedFrames_Object = MibTableColumn
msanIPSGIpv6PortStaticBindMatchedFrames = _MsanIPSGIpv6PortStaticBindMatchedFrames_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 103, 5, 1, 4),
    _MsanIPSGIpv6PortStaticBindMatchedFrames_Type()
)
msanIPSGIpv6PortStaticBindMatchedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanIPSGIpv6PortStaticBindMatchedFrames.setStatus("current")
_MsanIPSGIpv6PortStaticBindRowStatus_Type = RowStatus
_MsanIPSGIpv6PortStaticBindRowStatus_Object = MibTableColumn
msanIPSGIpv6PortStaticBindRowStatus = _MsanIPSGIpv6PortStaticBindRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 103, 5, 1, 5),
    _MsanIPSGIpv6PortStaticBindRowStatus_Type()
)
msanIPSGIpv6PortStaticBindRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanIPSGIpv6PortStaticBindRowStatus.setStatus("current")
_MsanIPSGPortBindCurrentTable_Object = MibTable
msanIPSGPortBindCurrentTable = _MsanIPSGPortBindCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 103, 6)
)
if mibBuilder.loadTexts:
    msanIPSGPortBindCurrentTable.setStatus("current")
_MsanIPSGPortBindCurrentEntry_Object = MibTableRow
msanIPSGPortBindCurrentEntry = _MsanIPSGPortBindCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 103, 6, 1)
)
msanIPSGPortBindCurrentEntry.setIndexNames(
    (0, "ISKRATEL-MSAN-MIB", "msanIPSGPortBindCurrentId"),
)
if mibBuilder.loadTexts:
    msanIPSGPortBindCurrentEntry.setStatus("current")
_MsanIPSGPortBindCurrentId_Type = Integer32
_MsanIPSGPortBindCurrentId_Object = MibTableColumn
msanIPSGPortBindCurrentId = _MsanIPSGPortBindCurrentId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 103, 6, 1, 1),
    _MsanIPSGPortBindCurrentId_Type()
)
msanIPSGPortBindCurrentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanIPSGPortBindCurrentId.setStatus("current")
_MsanIPSGPortBindCurrentIfIndex_Type = InterfaceIndex
_MsanIPSGPortBindCurrentIfIndex_Object = MibTableColumn
msanIPSGPortBindCurrentIfIndex = _MsanIPSGPortBindCurrentIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 103, 6, 1, 2),
    _MsanIPSGPortBindCurrentIfIndex_Type()
)
msanIPSGPortBindCurrentIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanIPSGPortBindCurrentIfIndex.setStatus("current")
_MsanIPSGPortBindCurrentMacAddress_Type = MacAddress
_MsanIPSGPortBindCurrentMacAddress_Object = MibTableColumn
msanIPSGPortBindCurrentMacAddress = _MsanIPSGPortBindCurrentMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 103, 6, 1, 3),
    _MsanIPSGPortBindCurrentMacAddress_Type()
)
msanIPSGPortBindCurrentMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanIPSGPortBindCurrentMacAddress.setStatus("current")
_MsanIPSGPortBindCurrentVlanId_Type = VlanIndex
_MsanIPSGPortBindCurrentVlanId_Object = MibTableColumn
msanIPSGPortBindCurrentVlanId = _MsanIPSGPortBindCurrentVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 103, 6, 1, 4),
    _MsanIPSGPortBindCurrentVlanId_Type()
)
msanIPSGPortBindCurrentVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanIPSGPortBindCurrentVlanId.setStatus("current")
_MsanIPSGPortBindCurrentIpAddressType_Type = InetAddressType
_MsanIPSGPortBindCurrentIpAddressType_Object = MibTableColumn
msanIPSGPortBindCurrentIpAddressType = _MsanIPSGPortBindCurrentIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 103, 6, 1, 5),
    _MsanIPSGPortBindCurrentIpAddressType_Type()
)
msanIPSGPortBindCurrentIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanIPSGPortBindCurrentIpAddressType.setStatus("current")
_MsanIPSGPortBindCurrentIpAddress_Type = InetAddress
_MsanIPSGPortBindCurrentIpAddress_Object = MibTableColumn
msanIPSGPortBindCurrentIpAddress = _MsanIPSGPortBindCurrentIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 103, 6, 1, 6),
    _MsanIPSGPortBindCurrentIpAddress_Type()
)
msanIPSGPortBindCurrentIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanIPSGPortBindCurrentIpAddress.setStatus("current")
_MsanIPSGPortBindCurrentLeaseRemainingTime_Type = TimeTicks
_MsanIPSGPortBindCurrentLeaseRemainingTime_Object = MibTableColumn
msanIPSGPortBindCurrentLeaseRemainingTime = _MsanIPSGPortBindCurrentLeaseRemainingTime_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 103, 6, 1, 7),
    _MsanIPSGPortBindCurrentLeaseRemainingTime_Type()
)
msanIPSGPortBindCurrentLeaseRemainingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanIPSGPortBindCurrentLeaseRemainingTime.setStatus("current")


class _MsanIPSGPortBindCurrentType_Type(Integer32):
    """Custom type msanIPSGPortBindCurrentType based on Integer32"""
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
        *(("dynamic-dhcpv4", 2),
          ("dynamic-dhcpv6", 3),
          ("dynamic-nd", 4),
          ("static", 1))
    )


_MsanIPSGPortBindCurrentType_Type.__name__ = "Integer32"
_MsanIPSGPortBindCurrentType_Object = MibTableColumn
msanIPSGPortBindCurrentType = _MsanIPSGPortBindCurrentType_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 103, 6, 1, 8),
    _MsanIPSGPortBindCurrentType_Type()
)
msanIPSGPortBindCurrentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanIPSGPortBindCurrentType.setStatus("current")
_MsanIPSGPortBindCurrentMatchedFrames_Type = Counter32
_MsanIPSGPortBindCurrentMatchedFrames_Object = MibTableColumn
msanIPSGPortBindCurrentMatchedFrames = _MsanIPSGPortBindCurrentMatchedFrames_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 103, 6, 1, 9),
    _MsanIPSGPortBindCurrentMatchedFrames_Type()
)
msanIPSGPortBindCurrentMatchedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanIPSGPortBindCurrentMatchedFrames.setStatus("current")
_MsanVlan_ObjectIdentity = ObjectIdentity
msanVlan = _MsanVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 105)
)
_MsanVlanGlobal_ObjectIdentity = ObjectIdentity
msanVlanGlobal = _MsanVlanGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 105, 1)
)


class _MsanDVlanTagMode_Type(Integer32):
    """Custom type msanDVlanTagMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanDVlanTagMode_Type.__name__ = "Integer32"
_MsanDVlanTagMode_Object = MibScalar
msanDVlanTagMode = _MsanDVlanTagMode_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 105, 1, 1),
    _MsanDVlanTagMode_Type()
)
msanDVlanTagMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDVlanTagMode.setStatus("deprecated")


class _MsanVlanRemarkAdminState_Type(Integer32):
    """Custom type msanVlanRemarkAdminState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanVlanRemarkAdminState_Type.__name__ = "Integer32"
_MsanVlanRemarkAdminState_Object = MibScalar
msanVlanRemarkAdminState = _MsanVlanRemarkAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 105, 1, 2),
    _MsanVlanRemarkAdminState_Type()
)
msanVlanRemarkAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanVlanRemarkAdminState.setStatus("deprecated")
_MsanInternalVlanId_Type = Integer32
_MsanInternalVlanId_Object = MibScalar
msanInternalVlanId = _MsanInternalVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 105, 1, 3),
    _MsanInternalVlanId_Type()
)
msanInternalVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanInternalVlanId.setStatus("current")
_MsanPortVlanTable_Object = MibTable
msanPortVlanTable = _MsanPortVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 105, 2)
)
if mibBuilder.loadTexts:
    msanPortVlanTable.setStatus("deprecated")
_MsanPortVlanEntry_Object = MibTableRow
msanPortVlanEntry = _MsanPortVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 105, 2, 1)
)
msanPortVlanEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    msanPortVlanEntry.setStatus("deprecated")


class _MsanPortVlanMode_Type(Integer32):
    """Custom type msanPortVlanMode based on Integer32"""
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
        *(("access", 0),
          ("dot1qtunnel", 2),
          ("trunk", 1),
          ("vlanStacking", 3))
    )


_MsanPortVlanMode_Type.__name__ = "Integer32"
_MsanPortVlanMode_Object = MibTableColumn
msanPortVlanMode = _MsanPortVlanMode_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 105, 2, 1, 1),
    _MsanPortVlanMode_Type()
)
msanPortVlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanPortVlanMode.setStatus("deprecated")


class _MsanPortVlanStackPriority_Type(Integer32):
    """Custom type msanPortVlanStackPriority based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("mapPriorityFromOuterTag", 0),
          ("priority1", 1),
          ("priority2", 2),
          ("priority3", 3),
          ("priority4", 4),
          ("priority5", 5),
          ("priority6", 6),
          ("priority7", 7))
    )


_MsanPortVlanStackPriority_Type.__name__ = "Integer32"
_MsanPortVlanStackPriority_Object = MibTableColumn
msanPortVlanStackPriority = _MsanPortVlanStackPriority_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 105, 2, 1, 2),
    _MsanPortVlanStackPriority_Type()
)
msanPortVlanStackPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanPortVlanStackPriority.setStatus("deprecated")
_MsanPortVlanStackVlanId_Type = Integer32
_MsanPortVlanStackVlanId_Object = MibTableColumn
msanPortVlanStackVlanId = _MsanPortVlanStackVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 105, 2, 1, 3),
    _MsanPortVlanStackVlanId_Type()
)
msanPortVlanStackVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanPortVlanStackVlanId.setStatus("deprecated")
_MsanPortDVlanMapTable_Object = MibTable
msanPortDVlanMapTable = _MsanPortDVlanMapTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 105, 3)
)
if mibBuilder.loadTexts:
    msanPortDVlanMapTable.setStatus("deprecated")
_MsanPortDVlanMapEntry_Object = MibTableRow
msanPortDVlanMapEntry = _MsanPortDVlanMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 105, 3, 1)
)
msanPortDVlanMapEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ISKRATEL-MSAN-MIB", "msanPortDVlanMapInTagVlanId"),
)
if mibBuilder.loadTexts:
    msanPortDVlanMapEntry.setStatus("deprecated")
_MsanPortDVlanMapInTagVlanId_Type = Integer32
_MsanPortDVlanMapInTagVlanId_Object = MibTableColumn
msanPortDVlanMapInTagVlanId = _MsanPortDVlanMapInTagVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 105, 3, 1, 1),
    _MsanPortDVlanMapInTagVlanId_Type()
)
msanPortDVlanMapInTagVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanPortDVlanMapInTagVlanId.setStatus("deprecated")
_MsanPortDVlanMapOutTagVlanId_Type = Integer32
_MsanPortDVlanMapOutTagVlanId_Object = MibTableColumn
msanPortDVlanMapOutTagVlanId = _MsanPortDVlanMapOutTagVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 105, 3, 1, 2),
    _MsanPortDVlanMapOutTagVlanId_Type()
)
msanPortDVlanMapOutTagVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanPortDVlanMapOutTagVlanId.setStatus("deprecated")
_MsanPortDVlanMapRowStatus_Type = RowStatus
_MsanPortDVlanMapRowStatus_Object = MibTableColumn
msanPortDVlanMapRowStatus = _MsanPortDVlanMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 105, 3, 1, 3),
    _MsanPortDVlanMapRowStatus_Type()
)
msanPortDVlanMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanPortDVlanMapRowStatus.setStatus("deprecated")
_MsanPortVlanRemarkTable_Object = MibTable
msanPortVlanRemarkTable = _MsanPortVlanRemarkTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 105, 4)
)
if mibBuilder.loadTexts:
    msanPortVlanRemarkTable.setStatus("current")
_MsanPortVlanRemarkEntry_Object = MibTableRow
msanPortVlanRemarkEntry = _MsanPortVlanRemarkEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 105, 4, 1)
)
msanPortVlanRemarkEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ISKRATEL-MSAN-MIB", "msanPortVlanRemarkSrcVlanId"),
)
if mibBuilder.loadTexts:
    msanPortVlanRemarkEntry.setStatus("current")


class _MsanPortVlanRemarkSrcVlanId_Type(Integer32):
    """Custom type msanPortVlanRemarkSrcVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_MsanPortVlanRemarkSrcVlanId_Type.__name__ = "Integer32"
_MsanPortVlanRemarkSrcVlanId_Object = MibTableColumn
msanPortVlanRemarkSrcVlanId = _MsanPortVlanRemarkSrcVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 105, 4, 1, 1),
    _MsanPortVlanRemarkSrcVlanId_Type()
)
msanPortVlanRemarkSrcVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanPortVlanRemarkSrcVlanId.setStatus("current")


class _MsanPortVlanRemarkDstVlanId_Type(Integer32):
    """Custom type msanPortVlanRemarkDstVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_MsanPortVlanRemarkDstVlanId_Type.__name__ = "Integer32"
_MsanPortVlanRemarkDstVlanId_Object = MibTableColumn
msanPortVlanRemarkDstVlanId = _MsanPortVlanRemarkDstVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 105, 4, 1, 2),
    _MsanPortVlanRemarkDstVlanId_Type()
)
msanPortVlanRemarkDstVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanPortVlanRemarkDstVlanId.setStatus("current")
_MsanPortVlanRemarkRowStatus_Type = RowStatus
_MsanPortVlanRemarkRowStatus_Object = MibTableColumn
msanPortVlanRemarkRowStatus = _MsanPortVlanRemarkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 105, 4, 1, 3),
    _MsanPortVlanRemarkRowStatus_Type()
)
msanPortVlanRemarkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanPortVlanRemarkRowStatus.setStatus("current")
_MsanPortDVlanTable_Object = MibTable
msanPortDVlanTable = _MsanPortDVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 105, 5)
)
if mibBuilder.loadTexts:
    msanPortDVlanTable.setStatus("current")
_MsanPortDVlanEntry_Object = MibTableRow
msanPortDVlanEntry = _MsanPortDVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 105, 5, 1)
)
msanPortDVlanEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    msanPortDVlanEntry.setStatus("current")


class _MsanPortDVlanTagMode_Type(Integer32):
    """Custom type msanPortDVlanTagMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanPortDVlanTagMode_Type.__name__ = "Integer32"
_MsanPortDVlanTagMode_Object = MibTableColumn
msanPortDVlanTagMode = _MsanPortDVlanTagMode_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 105, 5, 1, 1),
    _MsanPortDVlanTagMode_Type()
)
msanPortDVlanTagMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanPortDVlanTagMode.setStatus("current")
_MsanPortDVlanStackVlanId_Type = Integer32
_MsanPortDVlanStackVlanId_Object = MibTableColumn
msanPortDVlanStackVlanId = _MsanPortDVlanStackVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 105, 5, 1, 2),
    _MsanPortDVlanStackVlanId_Type()
)
msanPortDVlanStackVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanPortDVlanStackVlanId.setStatus("current")


class _MsanPortDVlanStackPriority_Type(Integer32):
    """Custom type msanPortDVlanStackPriority based on Integer32"""
    defaultValue = 0

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
              7)
        )
    )
    namedValues = NamedValues(
        *(("priority0", 0),
          ("priority1", 1),
          ("priority2", 2),
          ("priority3", 3),
          ("priority4", 4),
          ("priority5", 5),
          ("priority6", 6),
          ("priority7", 7))
    )


_MsanPortDVlanStackPriority_Type.__name__ = "Integer32"
_MsanPortDVlanStackPriority_Object = MibTableColumn
msanPortDVlanStackPriority = _MsanPortDVlanStackPriority_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 105, 5, 1, 3),
    _MsanPortDVlanStackPriority_Type()
)
msanPortDVlanStackPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanPortDVlanStackPriority.setStatus("current")
_MsanPortDVlanConfigTable_Object = MibTable
msanPortDVlanConfigTable = _MsanPortDVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 105, 6)
)
if mibBuilder.loadTexts:
    msanPortDVlanConfigTable.setStatus("current")
_MsanPortDVlanConfigEntry_Object = MibTableRow
msanPortDVlanConfigEntry = _MsanPortDVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 105, 6, 1)
)
msanPortDVlanConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ISKRATEL-MSAN-MIB", "msanDVlanConfigInTagVlanId"),
    (0, "ISKRATEL-MSAN-MIB", "msanDVlanConfigInTagPriority"),
)
if mibBuilder.loadTexts:
    msanPortDVlanConfigEntry.setStatus("current")
_MsanDVlanConfigInTagVlanId_Type = Integer32
_MsanDVlanConfigInTagVlanId_Object = MibTableColumn
msanDVlanConfigInTagVlanId = _MsanDVlanConfigInTagVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 105, 6, 1, 1),
    _MsanDVlanConfigInTagVlanId_Type()
)
msanDVlanConfigInTagVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanDVlanConfigInTagVlanId.setStatus("current")


class _MsanDVlanConfigInTagPriority_Type(Integer32):
    """Custom type msanDVlanConfigInTagPriority based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("priority0", 0),
          ("priority1", 1),
          ("priority2", 2),
          ("priority3", 3),
          ("priority4", 4),
          ("priority5", 5),
          ("priority6", 6),
          ("priority7", 7),
          ("unspecified", 8))
    )


_MsanDVlanConfigInTagPriority_Type.__name__ = "Integer32"
_MsanDVlanConfigInTagPriority_Object = MibTableColumn
msanDVlanConfigInTagPriority = _MsanDVlanConfigInTagPriority_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 105, 6, 1, 2),
    _MsanDVlanConfigInTagPriority_Type()
)
msanDVlanConfigInTagPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanDVlanConfigInTagPriority.setStatus("current")
_MsanDVlanConfigOutTagVlanId_Type = Integer32
_MsanDVlanConfigOutTagVlanId_Object = MibTableColumn
msanDVlanConfigOutTagVlanId = _MsanDVlanConfigOutTagVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 105, 6, 1, 3),
    _MsanDVlanConfigOutTagVlanId_Type()
)
msanDVlanConfigOutTagVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanDVlanConfigOutTagVlanId.setStatus("current")


class _MsanDVlanConfigOutTagPriority_Type(Integer32):
    """Custom type msanDVlanConfigOutTagPriority based on Integer32"""
    defaultValue = 0

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
              8)
        )
    )
    namedValues = NamedValues(
        *(("priority0", 0),
          ("priority1", 1),
          ("priority2", 2),
          ("priority3", 3),
          ("priority4", 4),
          ("priority5", 5),
          ("priority6", 6),
          ("priority7", 7),
          ("unspecified", 8))
    )


_MsanDVlanConfigOutTagPriority_Type.__name__ = "Integer32"
_MsanDVlanConfigOutTagPriority_Object = MibTableColumn
msanDVlanConfigOutTagPriority = _MsanDVlanConfigOutTagPriority_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 105, 6, 1, 4),
    _MsanDVlanConfigOutTagPriority_Type()
)
msanDVlanConfigOutTagPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanDVlanConfigOutTagPriority.setStatus("current")
_MsanDVlanConfigRowStatus_Type = RowStatus
_MsanDVlanConfigRowStatus_Object = MibTableColumn
msanDVlanConfigRowStatus = _MsanDVlanConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 105, 6, 1, 5),
    _MsanDVlanConfigRowStatus_Type()
)
msanDVlanConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanDVlanConfigRowStatus.setStatus("current")
_MsanPortVlanRemarkAdminTable_Object = MibTable
msanPortVlanRemarkAdminTable = _MsanPortVlanRemarkAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 105, 7)
)
if mibBuilder.loadTexts:
    msanPortVlanRemarkAdminTable.setStatus("current")
_MsanPortVlanRemarkAdminEntry_Object = MibTableRow
msanPortVlanRemarkAdminEntry = _MsanPortVlanRemarkAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 105, 7, 1)
)
msanPortVlanRemarkAdminEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    msanPortVlanRemarkAdminEntry.setStatus("current")


class _MsanPortVlanRemarkAdminMode_Type(Integer32):
    """Custom type msanPortVlanRemarkAdminMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanPortVlanRemarkAdminMode_Type.__name__ = "Integer32"
_MsanPortVlanRemarkAdminMode_Object = MibTableColumn
msanPortVlanRemarkAdminMode = _MsanPortVlanRemarkAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 105, 7, 1, 1),
    _MsanPortVlanRemarkAdminMode_Type()
)
msanPortVlanRemarkAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanPortVlanRemarkAdminMode.setStatus("current")
_MsanAtm_ObjectIdentity = ObjectIdentity
msanAtm = _MsanAtm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 106)
)
_MsanAtmGlobal_ObjectIdentity = ObjectIdentity
msanAtmGlobal = _MsanAtmGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 106, 1)
)
_MsanPortAtmPvcTable_Object = MibTable
msanPortAtmPvcTable = _MsanPortAtmPvcTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 106, 2)
)
if mibBuilder.loadTexts:
    msanPortAtmPvcTable.setStatus("current")
_MsanPortAtmPvcEntry_Object = MibTableRow
msanPortAtmPvcEntry = _MsanPortAtmPvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 106, 2, 1)
)
msanPortAtmPvcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ISKRATEL-MSAN-MIB", "msanPortAtmPvcVpi"),
    (0, "ISKRATEL-MSAN-MIB", "msanPortAtmPvcVci"),
)
if mibBuilder.loadTexts:
    msanPortAtmPvcEntry.setStatus("current")


class _MsanPortAtmPvcVpi_Type(Integer32):
    """Custom type msanPortAtmPvcVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanPortAtmPvcVpi_Type.__name__ = "Integer32"
_MsanPortAtmPvcVpi_Object = MibTableColumn
msanPortAtmPvcVpi = _MsanPortAtmPvcVpi_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 106, 2, 1, 1),
    _MsanPortAtmPvcVpi_Type()
)
msanPortAtmPvcVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanPortAtmPvcVpi.setStatus("current")


class _MsanPortAtmPvcVci_Type(Integer32):
    """Custom type msanPortAtmPvcVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 255),
    )


_MsanPortAtmPvcVci_Type.__name__ = "Integer32"
_MsanPortAtmPvcVci_Object = MibTableColumn
msanPortAtmPvcVci = _MsanPortAtmPvcVci_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 106, 2, 1, 2),
    _MsanPortAtmPvcVci_Type()
)
msanPortAtmPvcVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanPortAtmPvcVci.setStatus("current")


class _MsanPortAtmPvcPvid_Type(Integer32):
    """Custom type msanPortAtmPvcPvid based on Integer32"""
    defaultBinValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_MsanPortAtmPvcPvid_Type.__name__ = "Integer32"
_MsanPortAtmPvcPvid_Object = MibTableColumn
msanPortAtmPvcPvid = _MsanPortAtmPvcPvid_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 106, 2, 1, 3),
    _MsanPortAtmPvcPvid_Type()
)
msanPortAtmPvcPvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanPortAtmPvcPvid.setStatus("current")
_MsanPortAtmPvcRowStatus_Type = RowStatus
_MsanPortAtmPvcRowStatus_Object = MibTableColumn
msanPortAtmPvcRowStatus = _MsanPortAtmPvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 106, 2, 1, 4),
    _MsanPortAtmPvcRowStatus_Type()
)
msanPortAtmPvcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanPortAtmPvcRowStatus.setStatus("current")
_MsanEnergyMeter_ObjectIdentity = ObjectIdentity
msanEnergyMeter = _MsanEnergyMeter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 107)
)
_MsanEnergyMeterGlobal_ObjectIdentity = ObjectIdentity
msanEnergyMeterGlobal = _MsanEnergyMeterGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 107, 1)
)
_MsanEnergyMeterIpAddress_Type = IpAddress
_MsanEnergyMeterIpAddress_Object = MibScalar
msanEnergyMeterIpAddress = _MsanEnergyMeterIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 107, 1, 1),
    _MsanEnergyMeterIpAddress_Type()
)
msanEnergyMeterIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanEnergyMeterIpAddress.setStatus("current")


class _MsanEnergyMeterTcpPort_Type(Unsigned32):
    """Custom type msanEnergyMeterTcpPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MsanEnergyMeterTcpPort_Type.__name__ = "Unsigned32"
_MsanEnergyMeterTcpPort_Object = MibScalar
msanEnergyMeterTcpPort = _MsanEnergyMeterTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 107, 1, 2),
    _MsanEnergyMeterTcpPort_Type()
)
msanEnergyMeterTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanEnergyMeterTcpPort.setStatus("current")
_MsanEnergyMeterAddress_Type = Unsigned32
_MsanEnergyMeterAddress_Object = MibScalar
msanEnergyMeterAddress = _MsanEnergyMeterAddress_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 107, 1, 3),
    _MsanEnergyMeterAddress_Type()
)
msanEnergyMeterAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanEnergyMeterAddress.setStatus("current")


class _MsanEnergyMeterPassword_Type(Unsigned32):
    """Custom type msanEnergyMeterPassword based on Unsigned32"""
    defaultValue = 0


_MsanEnergyMeterPassword_Object = MibScalar
msanEnergyMeterPassword = _MsanEnergyMeterPassword_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 107, 1, 4),
    _MsanEnergyMeterPassword_Type()
)
msanEnergyMeterPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanEnergyMeterPassword.setStatus("current")


class _MsanEnergyMeterSerialNo_Type(OctetString):
    """Custom type msanEnergyMeterSerialNo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_MsanEnergyMeterSerialNo_Type.__name__ = "OctetString"
_MsanEnergyMeterSerialNo_Object = MibScalar
msanEnergyMeterSerialNo = _MsanEnergyMeterSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 107, 1, 5),
    _MsanEnergyMeterSerialNo_Type()
)
msanEnergyMeterSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanEnergyMeterSerialNo.setStatus("current")
_MsanEnergyMeterDateTime_Type = OctetString
_MsanEnergyMeterDateTime_Object = MibScalar
msanEnergyMeterDateTime = _MsanEnergyMeterDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 107, 1, 6),
    _MsanEnergyMeterDateTime_Type()
)
msanEnergyMeterDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanEnergyMeterDateTime.setStatus("current")
_MsanEnergyMeterCurrTariff_Type = Unsigned32
_MsanEnergyMeterCurrTariff_Object = MibScalar
msanEnergyMeterCurrTariff = _MsanEnergyMeterCurrTariff_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 107, 1, 7),
    _MsanEnergyMeterCurrTariff_Type()
)
msanEnergyMeterCurrTariff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanEnergyMeterCurrTariff.setStatus("current")
_MsanEnergyMeterCurrPower_Type = Unsigned32
_MsanEnergyMeterCurrPower_Object = MibScalar
msanEnergyMeterCurrPower = _MsanEnergyMeterCurrPower_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 107, 1, 8),
    _MsanEnergyMeterCurrPower_Type()
)
msanEnergyMeterCurrPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanEnergyMeterCurrPower.setStatus("current")
if mibBuilder.loadTexts:
    msanEnergyMeterCurrPower.setUnits("0.01 kW")
_MsanEnergyMeterCoreVersion_Type = Unsigned32
_MsanEnergyMeterCoreVersion_Object = MibScalar
msanEnergyMeterCoreVersion = _MsanEnergyMeterCoreVersion_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 107, 1, 9),
    _MsanEnergyMeterCoreVersion_Type()
)
msanEnergyMeterCoreVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanEnergyMeterCoreVersion.setStatus("current")
_MsanEnergyMeterFwType_Type = Unsigned32
_MsanEnergyMeterFwType_Object = MibScalar
msanEnergyMeterFwType = _MsanEnergyMeterFwType_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 107, 1, 10),
    _MsanEnergyMeterFwType_Type()
)
msanEnergyMeterFwType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanEnergyMeterFwType.setStatus("current")
_MsanEnergyMeterFwVersion_Type = Unsigned32
_MsanEnergyMeterFwVersion_Object = MibScalar
msanEnergyMeterFwVersion = _MsanEnergyMeterFwVersion_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 107, 1, 11),
    _MsanEnergyMeterFwVersion_Type()
)
msanEnergyMeterFwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanEnergyMeterFwVersion.setStatus("current")
_MsanEnergyMeterFwCreationDate_Type = OctetString
_MsanEnergyMeterFwCreationDate_Object = MibScalar
msanEnergyMeterFwCreationDate = _MsanEnergyMeterFwCreationDate_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 107, 1, 12),
    _MsanEnergyMeterFwCreationDate_Type()
)
msanEnergyMeterFwCreationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanEnergyMeterFwCreationDate.setStatus("current")
_MsanEnergyMeterEnergyTable_Object = MibTable
msanEnergyMeterEnergyTable = _MsanEnergyMeterEnergyTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 107, 2)
)
if mibBuilder.loadTexts:
    msanEnergyMeterEnergyTable.setStatus("current")
_MsanEnergyMeterEnergyEntry_Object = MibTableRow
msanEnergyMeterEnergyEntry = _MsanEnergyMeterEnergyEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 107, 2, 1)
)
msanEnergyMeterEnergyEntry.setIndexNames(
    (0, "ISKRATEL-MSAN-MIB", "msanEnergyMeterTariff"),
    (0, "ISKRATEL-MSAN-MIB", "msanEnergyMeterDepth"),
)
if mibBuilder.loadTexts:
    msanEnergyMeterEnergyEntry.setStatus("current")


class _MsanEnergyMeterTariff_Type(Unsigned32):
    """Custom type msanEnergyMeterTariff based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MsanEnergyMeterTariff_Type.__name__ = "Unsigned32"
_MsanEnergyMeterTariff_Object = MibTableColumn
msanEnergyMeterTariff = _MsanEnergyMeterTariff_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 107, 2, 1, 1),
    _MsanEnergyMeterTariff_Type()
)
msanEnergyMeterTariff.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanEnergyMeterTariff.setStatus("current")


class _MsanEnergyMeterDepth_Type(Unsigned32):
    """Custom type msanEnergyMeterDepth based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 13),
    )


_MsanEnergyMeterDepth_Type.__name__ = "Unsigned32"
_MsanEnergyMeterDepth_Object = MibTableColumn
msanEnergyMeterDepth = _MsanEnergyMeterDepth_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 107, 2, 1, 2),
    _MsanEnergyMeterDepth_Type()
)
msanEnergyMeterDepth.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanEnergyMeterDepth.setStatus("current")
_MsanEnergyMeterEnergyValue_Type = Unsigned32
_MsanEnergyMeterEnergyValue_Object = MibTableColumn
msanEnergyMeterEnergyValue = _MsanEnergyMeterEnergyValue_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 107, 2, 1, 3),
    _MsanEnergyMeterEnergyValue_Type()
)
msanEnergyMeterEnergyValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanEnergyMeterEnergyValue.setStatus("current")
if mibBuilder.loadTexts:
    msanEnergyMeterEnergyValue.setUnits("0.01 kWh")
_MsanEnergyMeterEnergySumTable_Object = MibTable
msanEnergyMeterEnergySumTable = _MsanEnergyMeterEnergySumTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 107, 3)
)
if mibBuilder.loadTexts:
    msanEnergyMeterEnergySumTable.setStatus("current")
_MsanEnergyMeterEnergySumEntry_Object = MibTableRow
msanEnergyMeterEnergySumEntry = _MsanEnergyMeterEnergySumEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 107, 3, 1)
)
msanEnergyMeterEnergySumEntry.setIndexNames(
    (0, "ISKRATEL-MSAN-MIB", "msanEnergyMeterDepth"),
)
if mibBuilder.loadTexts:
    msanEnergyMeterEnergySumEntry.setStatus("current")
_MsanEnergyMeterEnergySumValue_Type = Unsigned32
_MsanEnergyMeterEnergySumValue_Object = MibTableColumn
msanEnergyMeterEnergySumValue = _MsanEnergyMeterEnergySumValue_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 107, 3, 1, 1),
    _MsanEnergyMeterEnergySumValue_Type()
)
msanEnergyMeterEnergySumValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanEnergyMeterEnergySumValue.setStatus("current")
if mibBuilder.loadTexts:
    msanEnergyMeterEnergySumValue.setUnits("0.01 kWh")
_MsanArpInspection_ObjectIdentity = ObjectIdentity
msanArpInspection = _MsanArpInspection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 108)
)
_MsanArpInspectionGlobal_ObjectIdentity = ObjectIdentity
msanArpInspectionGlobal = _MsanArpInspectionGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 108, 1)
)


class _MsanArpInspectionAdminMode_Type(Integer32):
    """Custom type msanArpInspectionAdminMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanArpInspectionAdminMode_Type.__name__ = "Integer32"
_MsanArpInspectionAdminMode_Object = MibScalar
msanArpInspectionAdminMode = _MsanArpInspectionAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 108, 1, 1),
    _MsanArpInspectionAdminMode_Type()
)
msanArpInspectionAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanArpInspectionAdminMode.setStatus("current")
_MsanArpInspectionPortTable_Object = MibTable
msanArpInspectionPortTable = _MsanArpInspectionPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 108, 2)
)
if mibBuilder.loadTexts:
    msanArpInspectionPortTable.setStatus("current")
_MsanArpInspectionPortEntry_Object = MibTableRow
msanArpInspectionPortEntry = _MsanArpInspectionPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 108, 2, 1)
)
msanArpInspectionPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    msanArpInspectionPortEntry.setStatus("current")


class _MsanArpInspectionPortAdminMode_Type(Integer32):
    """Custom type msanArpInspectionPortAdminMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanArpInspectionPortAdminMode_Type.__name__ = "Integer32"
_MsanArpInspectionPortAdminMode_Object = MibTableColumn
msanArpInspectionPortAdminMode = _MsanArpInspectionPortAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 108, 2, 1, 1),
    _MsanArpInspectionPortAdminMode_Type()
)
msanArpInspectionPortAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanArpInspectionPortAdminMode.setStatus("current")
_MsanArpInspectionPortStatDroppedFrames_Type = Integer32
_MsanArpInspectionPortStatDroppedFrames_Object = MibTableColumn
msanArpInspectionPortStatDroppedFrames = _MsanArpInspectionPortStatDroppedFrames_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 108, 2, 1, 2),
    _MsanArpInspectionPortStatDroppedFrames_Type()
)
msanArpInspectionPortStatDroppedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanArpInspectionPortStatDroppedFrames.setStatus("current")
_MsanArpInspectionVlanTable_Object = MibTable
msanArpInspectionVlanTable = _MsanArpInspectionVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 108, 3)
)
if mibBuilder.loadTexts:
    msanArpInspectionVlanTable.setStatus("current")
_MsanArpInspectionVlanEntry_Object = MibTableRow
msanArpInspectionVlanEntry = _MsanArpInspectionVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 108, 3, 1)
)
msanArpInspectionVlanEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    msanArpInspectionVlanEntry.setStatus("current")


class _MsanArpInspectionVlanAdminMode_Type(Integer32):
    """Custom type msanArpInspectionVlanAdminMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanArpInspectionVlanAdminMode_Type.__name__ = "Integer32"
_MsanArpInspectionVlanAdminMode_Object = MibTableColumn
msanArpInspectionVlanAdminMode = _MsanArpInspectionVlanAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 108, 3, 1, 1),
    _MsanArpInspectionVlanAdminMode_Type()
)
msanArpInspectionVlanAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanArpInspectionVlanAdminMode.setStatus("current")
_MsanArpInspectionVlanStatDroppedFrames_Type = Integer32
_MsanArpInspectionVlanStatDroppedFrames_Object = MibTableColumn
msanArpInspectionVlanStatDroppedFrames = _MsanArpInspectionVlanStatDroppedFrames_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 108, 3, 1, 2),
    _MsanArpInspectionVlanStatDroppedFrames_Type()
)
msanArpInspectionVlanStatDroppedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanArpInspectionVlanStatDroppedFrames.setStatus("current")
_MsanIsa_ObjectIdentity = ObjectIdentity
msanIsa = _MsanIsa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109)
)
_MsanIsaGlobal_ObjectIdentity = ObjectIdentity
msanIsaGlobal = _MsanIsaGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 1)
)


class _MsanIsaTalAdminMode_Type(Integer32):
    """Custom type msanIsaTalAdminMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanIsaTalAdminMode_Type.__name__ = "Integer32"
_MsanIsaTalAdminMode_Object = MibScalar
msanIsaTalAdminMode = _MsanIsaTalAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 1, 1),
    _MsanIsaTalAdminMode_Type()
)
msanIsaTalAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIsaTalAdminMode.setStatus("current")


class _MsanIsaDasServerPort_Type(Unsigned32):
    """Custom type msanIsaDasServerPort based on Unsigned32"""
    defaultValue = 3799

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MsanIsaDasServerPort_Type.__name__ = "Unsigned32"
_MsanIsaDasServerPort_Object = MibScalar
msanIsaDasServerPort = _MsanIsaDasServerPort_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 1, 2),
    _MsanIsaDasServerPort_Type()
)
msanIsaDasServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIsaDasServerPort.setStatus("current")


class _MsanIsaDasServerSecret_Type(DisplayString):
    """Custom type msanIsaDasServerSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MsanIsaDasServerSecret_Type.__name__ = "DisplayString"
_MsanIsaDasServerSecret_Object = MibScalar
msanIsaDasServerSecret = _MsanIsaDasServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 1, 3),
    _MsanIsaDasServerSecret_Type()
)
msanIsaDasServerSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIsaDasServerSecret.setStatus("current")


class _MsanIsaRadiusServerRetries_Type(Unsigned32):
    """Custom type msanIsaRadiusServerRetries based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_MsanIsaRadiusServerRetries_Type.__name__ = "Unsigned32"
_MsanIsaRadiusServerRetries_Object = MibScalar
msanIsaRadiusServerRetries = _MsanIsaRadiusServerRetries_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 1, 4),
    _MsanIsaRadiusServerRetries_Type()
)
msanIsaRadiusServerRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIsaRadiusServerRetries.setStatus("current")


class _MsanIsaRadiusServerTimeout_Type(Unsigned32):
    """Custom type msanIsaRadiusServerTimeout based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_MsanIsaRadiusServerTimeout_Type.__name__ = "Unsigned32"
_MsanIsaRadiusServerTimeout_Object = MibScalar
msanIsaRadiusServerTimeout = _MsanIsaRadiusServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 1, 5),
    _MsanIsaRadiusServerTimeout_Type()
)
msanIsaRadiusServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIsaRadiusServerTimeout.setStatus("current")
if mibBuilder.loadTexts:
    msanIsaRadiusServerTimeout.setUnits("seconds")
_MsanIsaStatistics_ObjectIdentity = ObjectIdentity
msanIsaStatistics = _MsanIsaStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 2)
)
_MsanIsaPortStatTable_Object = MibTable
msanIsaPortStatTable = _MsanIsaPortStatTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 2, 1)
)
if mibBuilder.loadTexts:
    msanIsaPortStatTable.setStatus("current")
_MsanIsaPortStatEntry_Object = MibTableRow
msanIsaPortStatEntry = _MsanIsaPortStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 2, 1, 1)
)
msanIsaPortStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    msanIsaPortStatEntry.setStatus("current")
_MsanIsaPortStatTalMatchedFrames_Type = Counter32
_MsanIsaPortStatTalMatchedFrames_Object = MibTableColumn
msanIsaPortStatTalMatchedFrames = _MsanIsaPortStatTalMatchedFrames_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 2, 1, 1, 1),
    _MsanIsaPortStatTalMatchedFrames_Type()
)
msanIsaPortStatTalMatchedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanIsaPortStatTalMatchedFrames.setStatus("current")
_MsanIsaPortStatTalDroppedFrames_Type = Counter32
_MsanIsaPortStatTalDroppedFrames_Object = MibTableColumn
msanIsaPortStatTalDroppedFrames = _MsanIsaPortStatTalDroppedFrames_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 2, 1, 1, 2),
    _MsanIsaPortStatTalDroppedFrames_Type()
)
msanIsaPortStatTalDroppedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanIsaPortStatTalDroppedFrames.setStatus("current")
_MsanIsaPortStatAuthenReqSent_Type = Counter32
_MsanIsaPortStatAuthenReqSent_Object = MibTableColumn
msanIsaPortStatAuthenReqSent = _MsanIsaPortStatAuthenReqSent_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 2, 1, 1, 3),
    _MsanIsaPortStatAuthenReqSent_Type()
)
msanIsaPortStatAuthenReqSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanIsaPortStatAuthenReqSent.setStatus("current")
_MsanIsaPortStatAuthenReqConfirmed_Type = Counter32
_MsanIsaPortStatAuthenReqConfirmed_Object = MibTableColumn
msanIsaPortStatAuthenReqConfirmed = _MsanIsaPortStatAuthenReqConfirmed_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 2, 1, 1, 4),
    _MsanIsaPortStatAuthenReqConfirmed_Type()
)
msanIsaPortStatAuthenReqConfirmed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanIsaPortStatAuthenReqConfirmed.setStatus("current")
_MsanIsaPortStatAuthenReqRejected_Type = Counter32
_MsanIsaPortStatAuthenReqRejected_Object = MibTableColumn
msanIsaPortStatAuthenReqRejected = _MsanIsaPortStatAuthenReqRejected_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 2, 1, 1, 6),
    _MsanIsaPortStatAuthenReqRejected_Type()
)
msanIsaPortStatAuthenReqRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanIsaPortStatAuthenReqRejected.setStatus("current")
_MsanIsaPortStatAuthenTimeoutExpired_Type = Counter32
_MsanIsaPortStatAuthenTimeoutExpired_Object = MibTableColumn
msanIsaPortStatAuthenTimeoutExpired = _MsanIsaPortStatAuthenTimeoutExpired_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 2, 1, 1, 7),
    _MsanIsaPortStatAuthenTimeoutExpired_Type()
)
msanIsaPortStatAuthenTimeoutExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanIsaPortStatAuthenTimeoutExpired.setStatus("current")
_MsanIsaPortStatAuthorReqSent_Type = Counter32
_MsanIsaPortStatAuthorReqSent_Object = MibTableColumn
msanIsaPortStatAuthorReqSent = _MsanIsaPortStatAuthorReqSent_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 2, 1, 1, 8),
    _MsanIsaPortStatAuthorReqSent_Type()
)
msanIsaPortStatAuthorReqSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanIsaPortStatAuthorReqSent.setStatus("current")
_MsanIsaPortStatAuthorReqConfirmed_Type = Counter32
_MsanIsaPortStatAuthorReqConfirmed_Object = MibTableColumn
msanIsaPortStatAuthorReqConfirmed = _MsanIsaPortStatAuthorReqConfirmed_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 2, 1, 1, 9),
    _MsanIsaPortStatAuthorReqConfirmed_Type()
)
msanIsaPortStatAuthorReqConfirmed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanIsaPortStatAuthorReqConfirmed.setStatus("current")
_MsanIsaPortStatAuthorReqRejected_Type = Counter32
_MsanIsaPortStatAuthorReqRejected_Object = MibTableColumn
msanIsaPortStatAuthorReqRejected = _MsanIsaPortStatAuthorReqRejected_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 2, 1, 1, 10),
    _MsanIsaPortStatAuthorReqRejected_Type()
)
msanIsaPortStatAuthorReqRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanIsaPortStatAuthorReqRejected.setStatus("current")
_MsanIsaPortStatAuthorTimeoutExpired_Type = Counter32
_MsanIsaPortStatAuthorTimeoutExpired_Object = MibTableColumn
msanIsaPortStatAuthorTimeoutExpired = _MsanIsaPortStatAuthorTimeoutExpired_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 2, 1, 1, 11),
    _MsanIsaPortStatAuthorTimeoutExpired_Type()
)
msanIsaPortStatAuthorTimeoutExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanIsaPortStatAuthorTimeoutExpired.setStatus("current")
_MsanIsaStatLoginReq_Type = Counter32
_MsanIsaStatLoginReq_Object = MibScalar
msanIsaStatLoginReq = _MsanIsaStatLoginReq_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 2, 2),
    _MsanIsaStatLoginReq_Type()
)
msanIsaStatLoginReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanIsaStatLoginReq.setStatus("current")
_MsanIsaStatLoginUnsuccessfulReq_Type = Counter32
_MsanIsaStatLoginUnsuccessfulReq_Object = MibScalar
msanIsaStatLoginUnsuccessfulReq = _MsanIsaStatLoginUnsuccessfulReq_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 2, 3),
    _MsanIsaStatLoginUnsuccessfulReq_Type()
)
msanIsaStatLoginUnsuccessfulReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanIsaStatLoginUnsuccessfulReq.setStatus("current")
_MsanIsaRadiusServerTable_Object = MibTable
msanIsaRadiusServerTable = _MsanIsaRadiusServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 3)
)
if mibBuilder.loadTexts:
    msanIsaRadiusServerTable.setStatus("current")
_MsanIsaRadiusServerEntry_Object = MibTableRow
msanIsaRadiusServerEntry = _MsanIsaRadiusServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 3, 1)
)
msanIsaRadiusServerEntry.setIndexNames(
    (0, "ISKRATEL-MSAN-MIB", "msanIsaRadiusServerIpAddress"),
    (0, "ISKRATEL-MSAN-MIB", "msanIsaRadiusServerType"),
)
if mibBuilder.loadTexts:
    msanIsaRadiusServerEntry.setStatus("current")
_MsanIsaRadiusServerIpAddress_Type = IpAddress
_MsanIsaRadiusServerIpAddress_Object = MibTableColumn
msanIsaRadiusServerIpAddress = _MsanIsaRadiusServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 3, 1, 1),
    _MsanIsaRadiusServerIpAddress_Type()
)
msanIsaRadiusServerIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanIsaRadiusServerIpAddress.setStatus("current")


class _MsanIsaRadiusServerType_Type(Integer32):
    """Custom type msanIsaRadiusServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accounting", 2),
          ("authentication", 1))
    )


_MsanIsaRadiusServerType_Type.__name__ = "Integer32"
_MsanIsaRadiusServerType_Object = MibTableColumn
msanIsaRadiusServerType = _MsanIsaRadiusServerType_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 3, 1, 2),
    _MsanIsaRadiusServerType_Type()
)
msanIsaRadiusServerType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanIsaRadiusServerType.setStatus("current")


class _MsanIsaRadiusServerPort_Type(Unsigned32):
    """Custom type msanIsaRadiusServerPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MsanIsaRadiusServerPort_Type.__name__ = "Unsigned32"
_MsanIsaRadiusServerPort_Object = MibTableColumn
msanIsaRadiusServerPort = _MsanIsaRadiusServerPort_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 3, 1, 3),
    _MsanIsaRadiusServerPort_Type()
)
msanIsaRadiusServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIsaRadiusServerPort.setStatus("current")


class _MsanIsaRadiusServerSecret_Type(DisplayString):
    """Custom type msanIsaRadiusServerSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MsanIsaRadiusServerSecret_Type.__name__ = "DisplayString"
_MsanIsaRadiusServerSecret_Object = MibTableColumn
msanIsaRadiusServerSecret = _MsanIsaRadiusServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 3, 1, 4),
    _MsanIsaRadiusServerSecret_Type()
)
msanIsaRadiusServerSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIsaRadiusServerSecret.setStatus("current")


class _MsanIsaRadiusServerPrimaryMode_Type(Integer32):
    """Custom type msanIsaRadiusServerPrimaryMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_MsanIsaRadiusServerPrimaryMode_Type.__name__ = "Integer32"
_MsanIsaRadiusServerPrimaryMode_Object = MibTableColumn
msanIsaRadiusServerPrimaryMode = _MsanIsaRadiusServerPrimaryMode_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 3, 1, 5),
    _MsanIsaRadiusServerPrimaryMode_Type()
)
msanIsaRadiusServerPrimaryMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIsaRadiusServerPrimaryMode.setStatus("current")
_MsanIsaRadiusServerRowStatus_Type = RowStatus
_MsanIsaRadiusServerRowStatus_Object = MibTableColumn
msanIsaRadiusServerRowStatus = _MsanIsaRadiusServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 3, 1, 6),
    _MsanIsaRadiusServerRowStatus_Type()
)
msanIsaRadiusServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanIsaRadiusServerRowStatus.setStatus("current")
_MsanIsaPortTable_Object = MibTable
msanIsaPortTable = _MsanIsaPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 5)
)
if mibBuilder.loadTexts:
    msanIsaPortTable.setStatus("current")
_MsanIsaPortEntry_Object = MibTableRow
msanIsaPortEntry = _MsanIsaPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 5, 1)
)
msanIsaPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    msanIsaPortEntry.setStatus("current")


class _MsanIsaPortTalAdminMode_Type(Integer32):
    """Custom type msanIsaPortTalAdminMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanIsaPortTalAdminMode_Type.__name__ = "Integer32"
_MsanIsaPortTalAdminMode_Object = MibTableColumn
msanIsaPortTalAdminMode = _MsanIsaPortTalAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 5, 1, 1),
    _MsanIsaPortTalAdminMode_Type()
)
msanIsaPortTalAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIsaPortTalAdminMode.setStatus("current")


class _MsanIsaPortAuthentication_Type(Integer32):
    """Custom type msanIsaPortAuthentication based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanIsaPortAuthentication_Type.__name__ = "Integer32"
_MsanIsaPortAuthentication_Object = MibTableColumn
msanIsaPortAuthentication = _MsanIsaPortAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 5, 1, 2),
    _MsanIsaPortAuthentication_Type()
)
msanIsaPortAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIsaPortAuthentication.setStatus("current")


class _MsanIsaPortAuthorization_Type(Integer32):
    """Custom type msanIsaPortAuthorization based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanIsaPortAuthorization_Type.__name__ = "Integer32"
_MsanIsaPortAuthorization_Object = MibTableColumn
msanIsaPortAuthorization = _MsanIsaPortAuthorization_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 5, 1, 3),
    _MsanIsaPortAuthorization_Type()
)
msanIsaPortAuthorization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIsaPortAuthorization.setStatus("current")


class _MsanIsaPortAccounting_Type(Integer32):
    """Custom type msanIsaPortAccounting based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanIsaPortAccounting_Type.__name__ = "Integer32"
_MsanIsaPortAccounting_Object = MibTableColumn
msanIsaPortAccounting = _MsanIsaPortAccounting_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 5, 1, 4),
    _MsanIsaPortAccounting_Type()
)
msanIsaPortAccounting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIsaPortAccounting.setStatus("current")


class _MsanIsaPortLoginMask_Type(Bits):
    """Custom type msanIsaPortLoginMask based on Bits"""
    defaultBinValue = "1"

    namedValues = NamedValues(
        *(("circuitId", 0),
          ("clientId", 3),
          ("remoteId", 1),
          ("sourceIP", 5),
          ("sourceMAC", 4),
          ("userPattern", 6),
          ("vendorId", 2))
    )

_MsanIsaPortLoginMask_Type.__name__ = "Bits"
_MsanIsaPortLoginMask_Object = MibTableColumn
msanIsaPortLoginMask = _MsanIsaPortLoginMask_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 5, 1, 5),
    _MsanIsaPortLoginMask_Type()
)
msanIsaPortLoginMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIsaPortLoginMask.setStatus("current")


class _MsanIsaPortLoginUserPatternMask_Type(OctetString):
    """Custom type msanIsaPortLoginUserPatternMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MsanIsaPortLoginUserPatternMask_Type.__name__ = "OctetString"
_MsanIsaPortLoginUserPatternMask_Object = MibTableColumn
msanIsaPortLoginUserPatternMask = _MsanIsaPortLoginUserPatternMask_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 5, 1, 6),
    _MsanIsaPortLoginUserPatternMask_Type()
)
msanIsaPortLoginUserPatternMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIsaPortLoginUserPatternMask.setStatus("current")


class _MsanIsaPortTalAutomaticReq_Type(Integer32):
    """Custom type msanIsaPortTalAutomaticReq based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanIsaPortTalAutomaticReq_Type.__name__ = "Integer32"
_MsanIsaPortTalAutomaticReq_Object = MibTableColumn
msanIsaPortTalAutomaticReq = _MsanIsaPortTalAutomaticReq_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 5, 1, 7),
    _MsanIsaPortTalAutomaticReq_Type()
)
msanIsaPortTalAutomaticReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIsaPortTalAutomaticReq.setStatus("current")
_MsanIsaTalPortMatchTable_Object = MibTable
msanIsaTalPortMatchTable = _MsanIsaTalPortMatchTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 6)
)
if mibBuilder.loadTexts:
    msanIsaTalPortMatchTable.setStatus("current")
_MsanIsaTalPortMatchEntry_Object = MibTableRow
msanIsaTalPortMatchEntry = _MsanIsaTalPortMatchEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 6, 1)
)
msanIsaTalPortMatchEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    msanIsaTalPortMatchEntry.setStatus("current")


class _MsanIsaTalPortMatchEthertype_Type(Integer32):
    """Custom type msanIsaTalPortMatchEthertype based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_MsanIsaTalPortMatchEthertype_Type.__name__ = "Integer32"
_MsanIsaTalPortMatchEthertype_Object = MibTableColumn
msanIsaTalPortMatchEthertype = _MsanIsaTalPortMatchEthertype_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 6, 1, 1),
    _MsanIsaTalPortMatchEthertype_Type()
)
msanIsaTalPortMatchEthertype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIsaTalPortMatchEthertype.setStatus("current")


class _MsanIsaTalPortMatchMacSrcAddr_Type(MacAddress):
    """Custom type msanIsaTalPortMatchMacSrcAddr based on MacAddress"""
    defaultHexValue = ""


_MsanIsaTalPortMatchMacSrcAddr_Object = MibTableColumn
msanIsaTalPortMatchMacSrcAddr = _MsanIsaTalPortMatchMacSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 6, 1, 2),
    _MsanIsaTalPortMatchMacSrcAddr_Type()
)
msanIsaTalPortMatchMacSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIsaTalPortMatchMacSrcAddr.setStatus("current")


class _MsanIsaTalPortMatchMacSrcMask_Type(MacAddress):
    """Custom type msanIsaTalPortMatchMacSrcMask based on MacAddress"""
    defaultHexValue = ""


_MsanIsaTalPortMatchMacSrcMask_Object = MibTableColumn
msanIsaTalPortMatchMacSrcMask = _MsanIsaTalPortMatchMacSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 6, 1, 3),
    _MsanIsaTalPortMatchMacSrcMask_Type()
)
msanIsaTalPortMatchMacSrcMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIsaTalPortMatchMacSrcMask.setStatus("current")


class _MsanIsaTalPortMatchVlanId_Type(Integer32):
    """Custom type msanIsaTalPortMatchVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 4094),
    )


_MsanIsaTalPortMatchVlanId_Type.__name__ = "Integer32"
_MsanIsaTalPortMatchVlanId_Object = MibTableColumn
msanIsaTalPortMatchVlanId = _MsanIsaTalPortMatchVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 6, 1, 4),
    _MsanIsaTalPortMatchVlanId_Type()
)
msanIsaTalPortMatchVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIsaTalPortMatchVlanId.setStatus("current")


class _MsanIsaTalPortMatchIpSrcAddr_Type(IpAddress):
    """Custom type msanIsaTalPortMatchIpSrcAddr based on IpAddress"""
    defaultHexValue = ""


_MsanIsaTalPortMatchIpSrcAddr_Object = MibTableColumn
msanIsaTalPortMatchIpSrcAddr = _MsanIsaTalPortMatchIpSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 6, 1, 5),
    _MsanIsaTalPortMatchIpSrcAddr_Type()
)
msanIsaTalPortMatchIpSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIsaTalPortMatchIpSrcAddr.setStatus("current")


class _MsanIsaTalPortMatchIpSrcMask_Type(IpAddress):
    """Custom type msanIsaTalPortMatchIpSrcMask based on IpAddress"""
    defaultHexValue = ""


_MsanIsaTalPortMatchIpSrcMask_Object = MibTableColumn
msanIsaTalPortMatchIpSrcMask = _MsanIsaTalPortMatchIpSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 6, 1, 6),
    _MsanIsaTalPortMatchIpSrcMask_Type()
)
msanIsaTalPortMatchIpSrcMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIsaTalPortMatchIpSrcMask.setStatus("current")


class _MsanIsaTalPortMatchDhcpType_Type(Integer32):
    """Custom type msanIsaTalPortMatchDhcpType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discover", 1),
          ("request", 2),
          ("undefined", 0))
    )


_MsanIsaTalPortMatchDhcpType_Type.__name__ = "Integer32"
_MsanIsaTalPortMatchDhcpType_Object = MibTableColumn
msanIsaTalPortMatchDhcpType = _MsanIsaTalPortMatchDhcpType_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 6, 1, 7),
    _MsanIsaTalPortMatchDhcpType_Type()
)
msanIsaTalPortMatchDhcpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIsaTalPortMatchDhcpType.setStatus("current")
_MsanIsaTalPortMatchDhcpOpt60VendorId_Type = DisplayString
_MsanIsaTalPortMatchDhcpOpt60VendorId_Object = MibTableColumn
msanIsaTalPortMatchDhcpOpt60VendorId = _MsanIsaTalPortMatchDhcpOpt60VendorId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 6, 1, 8),
    _MsanIsaTalPortMatchDhcpOpt60VendorId_Type()
)
msanIsaTalPortMatchDhcpOpt60VendorId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIsaTalPortMatchDhcpOpt60VendorId.setStatus("current")
_MsanIsaTalPortMatchDhcpOpt61ClientId_Type = DisplayString
_MsanIsaTalPortMatchDhcpOpt61ClientId_Object = MibTableColumn
msanIsaTalPortMatchDhcpOpt61ClientId = _MsanIsaTalPortMatchDhcpOpt61ClientId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 6, 1, 9),
    _MsanIsaTalPortMatchDhcpOpt61ClientId_Type()
)
msanIsaTalPortMatchDhcpOpt61ClientId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIsaTalPortMatchDhcpOpt61ClientId.setStatus("current")


class _MsanIsaTalPortMatchDhcpOpt61ClientIdMacAddr_Type(MacAddress):
    """Custom type msanIsaTalPortMatchDhcpOpt61ClientIdMacAddr based on MacAddress"""
    defaultHexValue = ""


_MsanIsaTalPortMatchDhcpOpt61ClientIdMacAddr_Object = MibTableColumn
msanIsaTalPortMatchDhcpOpt61ClientIdMacAddr = _MsanIsaTalPortMatchDhcpOpt61ClientIdMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 6, 1, 10),
    _MsanIsaTalPortMatchDhcpOpt61ClientIdMacAddr_Type()
)
msanIsaTalPortMatchDhcpOpt61ClientIdMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIsaTalPortMatchDhcpOpt61ClientIdMacAddr.setStatus("current")
_MsanIsaTalPortMatchDhcpOpt82RemoteId_Type = DisplayString
_MsanIsaTalPortMatchDhcpOpt82RemoteId_Object = MibTableColumn
msanIsaTalPortMatchDhcpOpt82RemoteId = _MsanIsaTalPortMatchDhcpOpt82RemoteId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 6, 1, 11),
    _MsanIsaTalPortMatchDhcpOpt82RemoteId_Type()
)
msanIsaTalPortMatchDhcpOpt82RemoteId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIsaTalPortMatchDhcpOpt82RemoteId.setStatus("current")


class _MsanIsaTalPortMatchUserBits_Type(OctetString):
    """Custom type msanIsaTalPortMatchUserBits based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MsanIsaTalPortMatchUserBits_Type.__name__ = "OctetString"
_MsanIsaTalPortMatchUserBits_Object = MibTableColumn
msanIsaTalPortMatchUserBits = _MsanIsaTalPortMatchUserBits_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 6, 1, 12),
    _MsanIsaTalPortMatchUserBits_Type()
)
msanIsaTalPortMatchUserBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIsaTalPortMatchUserBits.setStatus("current")


class _MsanIsaTalPortMatchUserMask_Type(OctetString):
    """Custom type msanIsaTalPortMatchUserMask based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MsanIsaTalPortMatchUserMask_Type.__name__ = "OctetString"
_MsanIsaTalPortMatchUserMask_Object = MibTableColumn
msanIsaTalPortMatchUserMask = _MsanIsaTalPortMatchUserMask_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 6, 1, 13),
    _MsanIsaTalPortMatchUserMask_Type()
)
msanIsaTalPortMatchUserMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIsaTalPortMatchUserMask.setStatus("current")
_MsanIsaTalPatternMatchTable_Object = MibTable
msanIsaTalPatternMatchTable = _MsanIsaTalPatternMatchTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 7)
)
if mibBuilder.loadTexts:
    msanIsaTalPatternMatchTable.setStatus("current")
_MsanIsaTalPatternMatchEntry_Object = MibTableRow
msanIsaTalPatternMatchEntry = _MsanIsaTalPatternMatchEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 7, 1)
)
msanIsaTalPatternMatchEntry.setIndexNames(
    (0, "ISKRATEL-MSAN-MIB", "msanIsaTalPatternMatchName"),
)
if mibBuilder.loadTexts:
    msanIsaTalPatternMatchEntry.setStatus("current")


class _MsanIsaTalPatternMatchName_Type(OctetString):
    """Custom type msanIsaTalPatternMatchName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_MsanIsaTalPatternMatchName_Type.__name__ = "OctetString"
_MsanIsaTalPatternMatchName_Object = MibTableColumn
msanIsaTalPatternMatchName = _MsanIsaTalPatternMatchName_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 7, 1, 1),
    _MsanIsaTalPatternMatchName_Type()
)
msanIsaTalPatternMatchName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanIsaTalPatternMatchName.setStatus("current")


class _MsanIsaTalPatternMatchEthertype_Type(Integer32):
    """Custom type msanIsaTalPatternMatchEthertype based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_MsanIsaTalPatternMatchEthertype_Type.__name__ = "Integer32"
_MsanIsaTalPatternMatchEthertype_Object = MibTableColumn
msanIsaTalPatternMatchEthertype = _MsanIsaTalPatternMatchEthertype_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 7, 1, 2),
    _MsanIsaTalPatternMatchEthertype_Type()
)
msanIsaTalPatternMatchEthertype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIsaTalPatternMatchEthertype.setStatus("current")


class _MsanIsaTalPatternMatchMacSrcAddr_Type(MacAddress):
    """Custom type msanIsaTalPatternMatchMacSrcAddr based on MacAddress"""
    defaultHexValue = ""


_MsanIsaTalPatternMatchMacSrcAddr_Object = MibTableColumn
msanIsaTalPatternMatchMacSrcAddr = _MsanIsaTalPatternMatchMacSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 7, 1, 3),
    _MsanIsaTalPatternMatchMacSrcAddr_Type()
)
msanIsaTalPatternMatchMacSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIsaTalPatternMatchMacSrcAddr.setStatus("current")


class _MsanIsaTalPatternMatchMacSrcMask_Type(MacAddress):
    """Custom type msanIsaTalPatternMatchMacSrcMask based on MacAddress"""
    defaultHexValue = ""


_MsanIsaTalPatternMatchMacSrcMask_Object = MibTableColumn
msanIsaTalPatternMatchMacSrcMask = _MsanIsaTalPatternMatchMacSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 7, 1, 4),
    _MsanIsaTalPatternMatchMacSrcMask_Type()
)
msanIsaTalPatternMatchMacSrcMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIsaTalPatternMatchMacSrcMask.setStatus("current")


class _MsanIsaTalPatternMatchVlanId_Type(Integer32):
    """Custom type msanIsaTalPatternMatchVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 4094),
    )


_MsanIsaTalPatternMatchVlanId_Type.__name__ = "Integer32"
_MsanIsaTalPatternMatchVlanId_Object = MibTableColumn
msanIsaTalPatternMatchVlanId = _MsanIsaTalPatternMatchVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 7, 1, 5),
    _MsanIsaTalPatternMatchVlanId_Type()
)
msanIsaTalPatternMatchVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIsaTalPatternMatchVlanId.setStatus("current")


class _MsanIsaTalPatternMatchIpSrcAddr_Type(IpAddress):
    """Custom type msanIsaTalPatternMatchIpSrcAddr based on IpAddress"""
    defaultHexValue = ""


_MsanIsaTalPatternMatchIpSrcAddr_Object = MibTableColumn
msanIsaTalPatternMatchIpSrcAddr = _MsanIsaTalPatternMatchIpSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 7, 1, 6),
    _MsanIsaTalPatternMatchIpSrcAddr_Type()
)
msanIsaTalPatternMatchIpSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIsaTalPatternMatchIpSrcAddr.setStatus("current")


class _MsanIsaTalPatternMatchIpSrcMask_Type(IpAddress):
    """Custom type msanIsaTalPatternMatchIpSrcMask based on IpAddress"""
    defaultHexValue = ""


_MsanIsaTalPatternMatchIpSrcMask_Object = MibTableColumn
msanIsaTalPatternMatchIpSrcMask = _MsanIsaTalPatternMatchIpSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 7, 1, 7),
    _MsanIsaTalPatternMatchIpSrcMask_Type()
)
msanIsaTalPatternMatchIpSrcMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIsaTalPatternMatchIpSrcMask.setStatus("current")


class _MsanIsaTalPatternMatchDhcpType_Type(Integer32):
    """Custom type msanIsaTalPatternMatchDhcpType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discover", 1),
          ("request", 2),
          ("undefined", 0))
    )


_MsanIsaTalPatternMatchDhcpType_Type.__name__ = "Integer32"
_MsanIsaTalPatternMatchDhcpType_Object = MibTableColumn
msanIsaTalPatternMatchDhcpType = _MsanIsaTalPatternMatchDhcpType_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 7, 1, 8),
    _MsanIsaTalPatternMatchDhcpType_Type()
)
msanIsaTalPatternMatchDhcpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIsaTalPatternMatchDhcpType.setStatus("current")
_MsanIsaTalPatternMatchDhcpOpt60VendorId_Type = DisplayString
_MsanIsaTalPatternMatchDhcpOpt60VendorId_Object = MibTableColumn
msanIsaTalPatternMatchDhcpOpt60VendorId = _MsanIsaTalPatternMatchDhcpOpt60VendorId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 7, 1, 9),
    _MsanIsaTalPatternMatchDhcpOpt60VendorId_Type()
)
msanIsaTalPatternMatchDhcpOpt60VendorId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIsaTalPatternMatchDhcpOpt60VendorId.setStatus("current")
_MsanIsaTalPatternMatchDhcpOpt61ClientId_Type = DisplayString
_MsanIsaTalPatternMatchDhcpOpt61ClientId_Object = MibTableColumn
msanIsaTalPatternMatchDhcpOpt61ClientId = _MsanIsaTalPatternMatchDhcpOpt61ClientId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 7, 1, 10),
    _MsanIsaTalPatternMatchDhcpOpt61ClientId_Type()
)
msanIsaTalPatternMatchDhcpOpt61ClientId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIsaTalPatternMatchDhcpOpt61ClientId.setStatus("current")


class _MsanIsaTalPatternMatchDhcpOpt61ClientIdMacAddr_Type(MacAddress):
    """Custom type msanIsaTalPatternMatchDhcpOpt61ClientIdMacAddr based on MacAddress"""
    defaultHexValue = ""


_MsanIsaTalPatternMatchDhcpOpt61ClientIdMacAddr_Object = MibTableColumn
msanIsaTalPatternMatchDhcpOpt61ClientIdMacAddr = _MsanIsaTalPatternMatchDhcpOpt61ClientIdMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 7, 1, 11),
    _MsanIsaTalPatternMatchDhcpOpt61ClientIdMacAddr_Type()
)
msanIsaTalPatternMatchDhcpOpt61ClientIdMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIsaTalPatternMatchDhcpOpt61ClientIdMacAddr.setStatus("current")
_MsanIsaTalPatternMatchDhcpOpt82RemoteId_Type = DisplayString
_MsanIsaTalPatternMatchDhcpOpt82RemoteId_Object = MibTableColumn
msanIsaTalPatternMatchDhcpOpt82RemoteId = _MsanIsaTalPatternMatchDhcpOpt82RemoteId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 7, 1, 12),
    _MsanIsaTalPatternMatchDhcpOpt82RemoteId_Type()
)
msanIsaTalPatternMatchDhcpOpt82RemoteId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIsaTalPatternMatchDhcpOpt82RemoteId.setStatus("current")


class _MsanIsaTalPatternMatchUserBits_Type(OctetString):
    """Custom type msanIsaTalPatternMatchUserBits based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MsanIsaTalPatternMatchUserBits_Type.__name__ = "OctetString"
_MsanIsaTalPatternMatchUserBits_Object = MibTableColumn
msanIsaTalPatternMatchUserBits = _MsanIsaTalPatternMatchUserBits_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 7, 1, 13),
    _MsanIsaTalPatternMatchUserBits_Type()
)
msanIsaTalPatternMatchUserBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIsaTalPatternMatchUserBits.setStatus("current")


class _MsanIsaTalPatternMatchUserMask_Type(OctetString):
    """Custom type msanIsaTalPatternMatchUserMask based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MsanIsaTalPatternMatchUserMask_Type.__name__ = "OctetString"
_MsanIsaTalPatternMatchUserMask_Object = MibTableColumn
msanIsaTalPatternMatchUserMask = _MsanIsaTalPatternMatchUserMask_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 7, 1, 14),
    _MsanIsaTalPatternMatchUserMask_Type()
)
msanIsaTalPatternMatchUserMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIsaTalPatternMatchUserMask.setStatus("current")


class _MsanIsaTalPatternMatchLoginMask_Type(Bits):
    """Custom type msanIsaTalPatternMatchLoginMask based on Bits"""
    defaultBinValue = "1"

    namedValues = NamedValues(
        *(("circuitId", 0),
          ("clientId", 3),
          ("remoteId", 1),
          ("sourceIP", 5),
          ("sourceMAC", 4),
          ("userPattern", 6),
          ("vendorId", 2))
    )

_MsanIsaTalPatternMatchLoginMask_Type.__name__ = "Bits"
_MsanIsaTalPatternMatchLoginMask_Object = MibTableColumn
msanIsaTalPatternMatchLoginMask = _MsanIsaTalPatternMatchLoginMask_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 7, 1, 15),
    _MsanIsaTalPatternMatchLoginMask_Type()
)
msanIsaTalPatternMatchLoginMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIsaTalPatternMatchLoginMask.setStatus("current")
_MsanIsaTalPatternMatchRowStatus_Type = RowStatus
_MsanIsaTalPatternMatchRowStatus_Object = MibTableColumn
msanIsaTalPatternMatchRowStatus = _MsanIsaTalPatternMatchRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 7, 1, 16),
    _MsanIsaTalPatternMatchRowStatus_Type()
)
msanIsaTalPatternMatchRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanIsaTalPatternMatchRowStatus.setStatus("current")
_MsanIsaTalPortPatternMatchTable_Object = MibTable
msanIsaTalPortPatternMatchTable = _MsanIsaTalPortPatternMatchTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 8)
)
if mibBuilder.loadTexts:
    msanIsaTalPortPatternMatchTable.setStatus("current")
_MsanIsaTalPortPatternMatchEntry_Object = MibTableRow
msanIsaTalPortPatternMatchEntry = _MsanIsaTalPortPatternMatchEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 8, 1)
)
msanIsaTalPortPatternMatchEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ISKRATEL-MSAN-MIB", "msanIsaTalPatternMatchName"),
)
if mibBuilder.loadTexts:
    msanIsaTalPortPatternMatchEntry.setStatus("current")
_MsanIsaTalPortPatternMatchRowStatus_Type = RowStatus
_MsanIsaTalPortPatternMatchRowStatus_Object = MibTableColumn
msanIsaTalPortPatternMatchRowStatus = _MsanIsaTalPortPatternMatchRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 109, 8, 1, 1),
    _MsanIsaTalPortPatternMatchRowStatus_Type()
)
msanIsaTalPortPatternMatchRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanIsaTalPortPatternMatchRowStatus.setStatus("current")
_MsanSync_ObjectIdentity = ObjectIdentity
msanSync = _MsanSync_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 110)
)
_MsanSyncGlobal_ObjectIdentity = ObjectIdentity
msanSyncGlobal = _MsanSyncGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 110, 1)
)
_MsanSyncTable_Object = MibTable
msanSyncTable = _MsanSyncTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 110, 2)
)
if mibBuilder.loadTexts:
    msanSyncTable.setStatus("current")
_MsanSyncEntry_Object = MibTableRow
msanSyncEntry = _MsanSyncEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 110, 2, 1)
)
msanSyncEntry.setIndexNames(
    (0, "ISKRATEL-MSAN-MIB", "msanSyncBoardPosition"),
    (0, "ISKRATEL-MSAN-MIB", "msanSyncSourcePriority"),
)
if mibBuilder.loadTexts:
    msanSyncEntry.setStatus("current")


class _MsanSyncBoardPosition_Type(Integer32):
    """Custom type msanSyncBoardPosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_MsanSyncBoardPosition_Type.__name__ = "Integer32"
_MsanSyncBoardPosition_Object = MibTableColumn
msanSyncBoardPosition = _MsanSyncBoardPosition_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 110, 2, 1, 1),
    _MsanSyncBoardPosition_Type()
)
msanSyncBoardPosition.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanSyncBoardPosition.setStatus("current")


class _MsanSyncSourcePriority_Type(Integer32):
    """Custom type msanSyncSourcePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_MsanSyncSourcePriority_Type.__name__ = "Integer32"
_MsanSyncSourcePriority_Object = MibTableColumn
msanSyncSourcePriority = _MsanSyncSourcePriority_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 110, 2, 1, 2),
    _MsanSyncSourcePriority_Type()
)
msanSyncSourcePriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msanSyncSourcePriority.setStatus("current")


class _MsanSyncSourceType_Type(Integer32):
    """Custom type msanSyncSourceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5,
              6,
              8,
              14,
              15,
              16,
              40)
        )
    )
    namedValues = NamedValues(
        *(("ext-10mhz", 5),
          ("ext-1hz", 6),
          ("ext-2mhz", 4),
          ("free-run", 40),
          ("mlvds-bp", 8),
          ("pps-bp", 14),
          ("ptp-eth", 15),
          ("sync-eth", 16))
    )


_MsanSyncSourceType_Type.__name__ = "Integer32"
_MsanSyncSourceType_Object = MibTableColumn
msanSyncSourceType = _MsanSyncSourceType_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 110, 2, 1, 3),
    _MsanSyncSourceType_Type()
)
msanSyncSourceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanSyncSourceType.setStatus("current")


class _MsanSyncSourceId_Type(Integer32):
    """Custom type msanSyncSourceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input-1", 1),
          ("input-2", 2))
    )


_MsanSyncSourceId_Type.__name__ = "Integer32"
_MsanSyncSourceId_Object = MibTableColumn
msanSyncSourceId = _MsanSyncSourceId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 110, 2, 1, 4),
    _MsanSyncSourceId_Type()
)
msanSyncSourceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanSyncSourceId.setStatus("current")
_MsanSyncSourceEthPortId_Type = InterfaceIndex
_MsanSyncSourceEthPortId_Object = MibTableColumn
msanSyncSourceEthPortId = _MsanSyncSourceEthPortId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 110, 2, 1, 5),
    _MsanSyncSourceEthPortId_Type()
)
msanSyncSourceEthPortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanSyncSourceEthPortId.setStatus("current")


class _MsanSyncDestinationType_Type(Integer32):
    """Custom type msanSyncDestinationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              10)
        )
    )
    namedValues = NamedValues(
        *(("global", 10),
          ("local", 0))
    )


_MsanSyncDestinationType_Type.__name__ = "Integer32"
_MsanSyncDestinationType_Object = MibTableColumn
msanSyncDestinationType = _MsanSyncDestinationType_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 110, 2, 1, 6),
    _MsanSyncDestinationType_Type()
)
msanSyncDestinationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanSyncDestinationType.setStatus("current")


class _MsanSyncDestinationMlvdsId_Type(Integer32):
    """Custom type msanSyncDestinationMlvdsId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mlvds-1", 1),
          ("mlvds-2", 2))
    )


_MsanSyncDestinationMlvdsId_Type.__name__ = "Integer32"
_MsanSyncDestinationMlvdsId_Object = MibTableColumn
msanSyncDestinationMlvdsId = _MsanSyncDestinationMlvdsId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 110, 2, 1, 7),
    _MsanSyncDestinationMlvdsId_Type()
)
msanSyncDestinationMlvdsId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanSyncDestinationMlvdsId.setStatus("current")


class _MsanSyncSourceSuitability_Type(Integer32):
    """Custom type msanSyncSourceSuitability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("suitable", 1),
          ("undefined", 0),
          ("unsuitable", 2))
    )


_MsanSyncSourceSuitability_Type.__name__ = "Integer32"
_MsanSyncSourceSuitability_Object = MibTableColumn
msanSyncSourceSuitability = _MsanSyncSourceSuitability_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 110, 2, 1, 8),
    _MsanSyncSourceSuitability_Type()
)
msanSyncSourceSuitability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanSyncSourceSuitability.setStatus("current")


class _MsanSyncSourceActivity_Type(Integer32):
    """Custom type msanSyncSourceActivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2),
          ("undefined", 0))
    )


_MsanSyncSourceActivity_Type.__name__ = "Integer32"
_MsanSyncSourceActivity_Object = MibTableColumn
msanSyncSourceActivity = _MsanSyncSourceActivity_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 110, 2, 1, 9),
    _MsanSyncSourceActivity_Type()
)
msanSyncSourceActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanSyncSourceActivity.setStatus("current")
_MsanSyncRowStatus_Type = RowStatus
_MsanSyncRowStatus_Object = MibTableColumn
msanSyncRowStatus = _MsanSyncRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 110, 2, 1, 10),
    _MsanSyncRowStatus_Type()
)
msanSyncRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msanSyncRowStatus.setStatus("current")
xdsl2LineConfTemplateEntry.registerAugmentions(
    ("ISKRATEL-MSAN-MIB",
     "msanXdsl2LineConfTemplateEntry")
)
msanXdsl2LineConfTemplateEntry.setIndexNames(*xdsl2LineConfTemplateEntry.getIndexNames())
xdsl2LineAlarmConfTemplateEntry.registerAugmentions(
    ("ISKRATEL-MSAN-MIB",
     "msanXdsl2LineAlarmConfTemplateEntry")
)
msanXdsl2LineAlarmConfTemplateEntry.setIndexNames(*xdsl2LineAlarmConfTemplateEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ISKRATEL-MSAN-MIB",
    **{"VlanList": VlanList,
       "Xdsl2PsdMaskDs": Xdsl2PsdMaskDs,
       "Xdsl2PsdMaskUs": Xdsl2PsdMaskUs,
       "PortMask": PortMask,
       "PercentByFives": PercentByFives,
       "iskratel": iskratel,
       "si2000": si2000,
       "products": products,
       "msan": msan,
       "msanInfo": msanInfo,
       "msanShelfInfo": msanShelfInfo,
       "msanShelfId": msanShelfId,
       "msanShelfType": msanShelfType,
       "msanShelfSize": msanShelfSize,
       "msanBoardInfo": msanBoardInfo,
       "msanBoardTable": msanBoardTable,
       "msanBoardEntry": msanBoardEntry,
       "msanBoardNr": msanBoardNr,
       "msanBoardParentNr": msanBoardParentNr,
       "msanBoardPosition": msanBoardPosition,
       "msanBoardType": msanBoardType,
       "msanBoardId": msanBoardId,
       "msanBoardSerialNr": msanBoardSerialNr,
       "msanBoardDescription": msanBoardDescription,
       "msanSwInfo": msanSwInfo,
       "msanSwSteerVersion": msanSwSteerVersion,
       "msanSwBuildDirectory": msanSwBuildDirectory,
       "msanSwBuildTime": msanSwBuildTime,
       "msanSwBranch": msanSwBranch,
       "msanSwBuildReference": msanSwBuildReference,
       "msanSwILVersion": msanSwILVersion,
       "msanSwIpmiVersion": msanSwIpmiVersion,
       "msanSwBspVersion": msanSwBspVersion,
       "msanSwCPLDVersion": msanSwCPLDVersion,
       "msanReservePackage": msanReservePackage,
       "msanSwComponentTable": msanSwComponentTable,
       "msanSwComponentEntry": msanSwComponentEntry,
       "msanSwComponentId": msanSwComponentId,
       "msanSwComponentName": msanSwComponentName,
       "msanSwComponentSteerVersion": msanSwComponentSteerVersion,
       "msanOtherInfo": msanOtherInfo,
       "msanSnmpSetErrorReason": msanSnmpSetErrorReason,
       "msanAdditionalConf": msanAdditionalConf,
       "msanSystem": msanSystem,
       "msanDateTime": msanDateTime,
       "msanShelfIdConf": msanShelfIdConf,
       "msanConfData": msanConfData,
       "msanSwUpgrade": msanSwUpgrade,
       "msanCliScriptCreate": msanCliScriptCreate,
       "msanCliScriptTable": msanCliScriptTable,
       "msanCliScriptEntry": msanCliScriptEntry,
       "msanCliScriptName": msanCliScriptName,
       "msanCliScriptApply": msanCliScriptApply,
       "msanCliScriptApplyStatus": msanCliScriptApplyStatus,
       "msanCliScriptRowStatus": msanCliScriptRowStatus,
       "msanCliPrompt": msanCliPrompt,
       "msanChassisId": msanChassisId,
       "msanSwBootPackageTable": msanSwBootPackageTable,
       "msanSwBootPackageEntry": msanSwBootPackageEntry,
       "msanSwBootPackageName": msanSwBootPackageName,
       "msanSwBootPackageStatus": msanSwBootPackageStatus,
       "msanSystemSwUpgrade": msanSystemSwUpgrade,
       "msanSystemSwUpgradeStart": msanSystemSwUpgradeStart,
       "msanSystemSwUpgradeStatus": msanSystemSwUpgradeStatus,
       "msanSystemSwUpgradeServerIpAddressType": msanSystemSwUpgradeServerIpAddressType,
       "msanSystemSwUpgradeServerIpAddress": msanSystemSwUpgradeServerIpAddress,
       "msanSystemSwUpgradeServerDnsName": msanSystemSwUpgradeServerDnsName,
       "msanSystemSwUpgradeProtocol": msanSystemSwUpgradeProtocol,
       "msanSystemSwUpgradeProtocolPortId": msanSystemSwUpgradeProtocolPortId,
       "msanSystemSwUpgradeUserName": msanSystemSwUpgradeUserName,
       "msanSystemSwUpgradeUserPassword": msanSystemSwUpgradeUserPassword,
       "msanSystemSwUpgradePath": msanSystemSwUpgradePath,
       "msanSystemSwUpgradePackageName": msanSystemSwUpgradePackageName,
       "msanSystemLogsUpload": msanSystemLogsUpload,
       "msanSystemLogsUploadStart": msanSystemLogsUploadStart,
       "msanSystemLogsUploadStatus": msanSystemLogsUploadStatus,
       "msanSystemLogsUploadServerIpAddressType": msanSystemLogsUploadServerIpAddressType,
       "msanSystemLogsUploadServerIpAddress": msanSystemLogsUploadServerIpAddress,
       "msanSystemLogsUploadServerDnsName": msanSystemLogsUploadServerDnsName,
       "msanSystemLogsUploadProtocol": msanSystemLogsUploadProtocol,
       "msanSystemLogsUploadProtocolPortId": msanSystemLogsUploadProtocolPortId,
       "msanSystemLogsUploadUserName": msanSystemLogsUploadUserName,
       "msanSystemLogsUploadUserPassword": msanSystemLogsUploadUserPassword,
       "msanSystemLogsUploadPath": msanSystemLogsUploadPath,
       "msanSystemLogsUploadFileName": msanSystemLogsUploadFileName,
       "msanProfiles": msanProfiles,
       "msanVDSLProfileTable": msanVDSLProfileTable,
       "msanVDSLProfileEntry": msanVDSLProfileEntry,
       "msanVDSLProfileType": msanVDSLProfileType,
       "msanVDSL2LineProfile": msanVDSL2LineProfile,
       "msanServiceProfile": msanServiceProfile,
       "msanServiceProfileTable": msanServiceProfileTable,
       "msanServiceProfileEntry": msanServiceProfileEntry,
       "msanServiceProfileName": msanServiceProfileName,
       "msanServiceProfileProtection": msanServiceProfileProtection,
       "msanServiceProfileStatus": msanServiceProfileStatus,
       "msanServiceProfileServiceFlowProfileName": msanServiceProfileServiceFlowProfileName,
       "msanServiceProfileMulticastProfileName": msanServiceProfileMulticastProfileName,
       "msanServiceProfileVlanProfileName": msanServiceProfileVlanProfileName,
       "msanServiceProfileL2cpProfileName": msanServiceProfileL2cpProfileName,
       "msanServiceProfileSecurityProfileName": msanServiceProfileSecurityProfileName,
       "msanServiceProfileAtmVpi": msanServiceProfileAtmVpi,
       "msanServiceProfileAtmVci": msanServiceProfileAtmVci,
       "msanServiceProfileDhcpRa": msanServiceProfileDhcpRa,
       "msanServiceProfileDhcpRaTrustClients": msanServiceProfileDhcpRaTrustClients,
       "msanServiceProfileDhcpRaOpt82UnicastExtension": msanServiceProfileDhcpRaOpt82UnicastExtension,
       "msanServiceProfileDhcpRaOpt82Insert": msanServiceProfileDhcpRaOpt82Insert,
       "msanServiceProfileDhcpRaRemoteId": msanServiceProfileDhcpRaRemoteId,
       "msanServiceProfileDhcpRaRateLimit": msanServiceProfileDhcpRaRateLimit,
       "msanServiceProfilePppoeIA": msanServiceProfilePppoeIA,
       "msanServiceProfilePppoeIARateLimit": msanServiceProfilePppoeIARateLimit,
       "msanServiceProfileDescription": msanServiceProfileDescription,
       "msanServiceProfileRowStatus": msanServiceProfileRowStatus,
       "msanServicePortProfileTable": msanServicePortProfileTable,
       "msanServicePortProfileEntry": msanServicePortProfileEntry,
       "msanServicePortProfileRowStatus": msanServicePortProfileRowStatus,
       "msanServiceFlowProfile": msanServiceFlowProfile,
       "msanServiceFlowProfileTable": msanServiceFlowProfileTable,
       "msanServiceFlowProfileEntry": msanServiceFlowProfileEntry,
       "msanServiceFlowProfileName": msanServiceFlowProfileName,
       "msanServiceFlowProfileProtection": msanServiceFlowProfileProtection,
       "msanServiceFlowProfileStatus": msanServiceFlowProfileStatus,
       "msanServiceFlowProfileMatchUsAny": msanServiceFlowProfileMatchUsAny,
       "msanServiceFlowProfileMatchUsMacDestAddr": msanServiceFlowProfileMatchUsMacDestAddr,
       "msanServiceFlowProfileMatchUsMacDestMask": msanServiceFlowProfileMatchUsMacDestMask,
       "msanServiceFlowProfileMatchUsMacSrcAddr": msanServiceFlowProfileMatchUsMacSrcAddr,
       "msanServiceFlowProfileMatchUsMacSrcMask": msanServiceFlowProfileMatchUsMacSrcMask,
       "msanServiceFlowProfileMatchUsCPcp": msanServiceFlowProfileMatchUsCPcp,
       "msanServiceFlowProfileMatchUsSPcp": msanServiceFlowProfileMatchUsSPcp,
       "msanServiceFlowProfileMatchUsVlanProfile": msanServiceFlowProfileMatchUsVlanProfile,
       "msanServiceFlowProfileMatchUsCVlanIdRange": msanServiceFlowProfileMatchUsCVlanIdRange,
       "msanServiceFlowProfileMatchUsSVlanIdRange": msanServiceFlowProfileMatchUsSVlanIdRange,
       "msanServiceFlowProfileMatchUsEthertype": msanServiceFlowProfileMatchUsEthertype,
       "msanServiceFlowProfileMatchUsIpProtocol": msanServiceFlowProfileMatchUsIpProtocol,
       "msanServiceFlowProfileMatchUsIpSrcAddr": msanServiceFlowProfileMatchUsIpSrcAddr,
       "msanServiceFlowProfileMatchUsIpSrcMask": msanServiceFlowProfileMatchUsIpSrcMask,
       "msanServiceFlowProfileMatchUsIpDestAddr": msanServiceFlowProfileMatchUsIpDestAddr,
       "msanServiceFlowProfileMatchUsIpDestMask": msanServiceFlowProfileMatchUsIpDestMask,
       "msanServiceFlowProfileMatchUsIpDscp": msanServiceFlowProfileMatchUsIpDscp,
       "msanServiceFlowProfileMatchUsIpCsc": msanServiceFlowProfileMatchUsIpCsc,
       "msanServiceFlowProfileMatchUsIpDropPrecedence": msanServiceFlowProfileMatchUsIpDropPrecedence,
       "msanServiceFlowProfileMatchUsTcpSrcPort": msanServiceFlowProfileMatchUsTcpSrcPort,
       "msanServiceFlowProfileMatchUsTcpDestPort": msanServiceFlowProfileMatchUsTcpDestPort,
       "msanServiceFlowProfileMatchUsUdpSrcPort": msanServiceFlowProfileMatchUsUdpSrcPort,
       "msanServiceFlowProfileMatchUsUdpDstPort": msanServiceFlowProfileMatchUsUdpDstPort,
       "msanServiceFlowProfileMatchDsAny": msanServiceFlowProfileMatchDsAny,
       "msanServiceFlowProfileMatchDsMacDestAddr": msanServiceFlowProfileMatchDsMacDestAddr,
       "msanServiceFlowProfileMatchDsMacDestMask": msanServiceFlowProfileMatchDsMacDestMask,
       "msanServiceFlowProfileMatchDsMacSrcAddr": msanServiceFlowProfileMatchDsMacSrcAddr,
       "msanServiceFlowProfileMatchDsMacSrcMask": msanServiceFlowProfileMatchDsMacSrcMask,
       "msanServiceFlowProfileMatchDsCPcp": msanServiceFlowProfileMatchDsCPcp,
       "msanServiceFlowProfileMatchDsSPcp": msanServiceFlowProfileMatchDsSPcp,
       "msanServiceFlowProfileMatchDsVlanProfile": msanServiceFlowProfileMatchDsVlanProfile,
       "msanServiceFlowProfileMatchDsCVlanIdRange": msanServiceFlowProfileMatchDsCVlanIdRange,
       "msanServiceFlowProfileMatchDsSVlanIdRange": msanServiceFlowProfileMatchDsSVlanIdRange,
       "msanServiceFlowProfileMatchDsEthertype": msanServiceFlowProfileMatchDsEthertype,
       "msanServiceFlowProfileMatchDsIpProtocol": msanServiceFlowProfileMatchDsIpProtocol,
       "msanServiceFlowProfileMatchDsIpSrcAddr": msanServiceFlowProfileMatchDsIpSrcAddr,
       "msanServiceFlowProfileMatchDsIpSrcMask": msanServiceFlowProfileMatchDsIpSrcMask,
       "msanServiceFlowProfileMatchDsIpDestAddr": msanServiceFlowProfileMatchDsIpDestAddr,
       "msanServiceFlowProfileMatchDsIpDestMask": msanServiceFlowProfileMatchDsIpDestMask,
       "msanServiceFlowProfileMatchDsIpDscp": msanServiceFlowProfileMatchDsIpDscp,
       "msanServiceFlowProfileMatchDsIpCsc": msanServiceFlowProfileMatchDsIpCsc,
       "msanServiceFlowProfileMatchDsIpDropPrecedence": msanServiceFlowProfileMatchDsIpDropPrecedence,
       "msanServiceFlowProfileMatchDsTcpSrcPort": msanServiceFlowProfileMatchDsTcpSrcPort,
       "msanServiceFlowProfileMatchDsTcpDestPort": msanServiceFlowProfileMatchDsTcpDestPort,
       "msanServiceFlowProfileMatchDsUdpSrcPort": msanServiceFlowProfileMatchDsUdpSrcPort,
       "msanServiceFlowProfileMatchDsUdpDstPort": msanServiceFlowProfileMatchDsUdpDstPort,
       "msanServiceFlowProfileUsCdr": msanServiceFlowProfileUsCdr,
       "msanServiceFlowProfileUsCdrBurstSize": msanServiceFlowProfileUsCdrBurstSize,
       "msanServiceFlowProfileUsPdr": msanServiceFlowProfileUsPdr,
       "msanServiceFlowProfileUsPdrBurstSize": msanServiceFlowProfileUsPdrBurstSize,
       "msanServiceFlowProfileUsMarkPcp": msanServiceFlowProfileUsMarkPcp,
       "msanServiceFlowProfileUsMarkPcpValue": msanServiceFlowProfileUsMarkPcpValue,
       "msanServiceFlowProfileUsMarkDscp": msanServiceFlowProfileUsMarkDscp,
       "msanServiceFlowProfileUsMarkDscpValue": msanServiceFlowProfileUsMarkDscpValue,
       "msanServiceFlowProfileDsCdr": msanServiceFlowProfileDsCdr,
       "msanServiceFlowProfileDsCdrBurstSize": msanServiceFlowProfileDsCdrBurstSize,
       "msanServiceFlowProfileDsPdr": msanServiceFlowProfileDsPdr,
       "msanServiceFlowProfileDsPdrBurstSize": msanServiceFlowProfileDsPdrBurstSize,
       "msanServiceFlowProfileDsMarkPcp": msanServiceFlowProfileDsMarkPcp,
       "msanServiceFlowProfileDsMarkPcpValue": msanServiceFlowProfileDsMarkPcpValue,
       "msanServiceFlowProfileDsMarkDscp": msanServiceFlowProfileDsMarkDscp,
       "msanServiceFlowProfileDsMarkDscpValue": msanServiceFlowProfileDsMarkDscpValue,
       "msanServiceFlowProfileDsQueuingPriority": msanServiceFlowProfileDsQueuingPriority,
       "msanServiceFlowProfileDsSchedulingMode": msanServiceFlowProfileDsSchedulingMode,
       "msanServiceFlowProfileDescription": msanServiceFlowProfileDescription,
       "msanServiceFlowProfileRowStatus": msanServiceFlowProfileRowStatus,
       "msanVlanProfile": msanVlanProfile,
       "msanVlanProfileTable": msanVlanProfileTable,
       "msanVlanProfileEntry": msanVlanProfileEntry,
       "msanVlanProfileName": msanVlanProfileName,
       "msanVlanProfileProtection": msanVlanProfileProtection,
       "msanVlanProfileStatus": msanVlanProfileStatus,
       "msanVlanProfileCVid": msanVlanProfileCVid,
       "msanVlanProfileCVidNative": msanVlanProfileCVidNative,
       "msanVlanProfileCVidRemark": msanVlanProfileCVidRemark,
       "msanVlanProfileSVid": msanVlanProfileSVid,
       "msanVlanProfileSEtherType": msanVlanProfileSEtherType,
       "msanVlanProfileDescription": msanVlanProfileDescription,
       "msanVlanProfileRowStatus": msanVlanProfileRowStatus,
       "msanVlanProfileNetworkPortCTag": msanVlanProfileNetworkPortCTag,
       "msanVlanPortProfileTable": msanVlanPortProfileTable,
       "msanVlanPortProfileEntry": msanVlanPortProfileEntry,
       "msanVlanPortProfileRowStatus": msanVlanPortProfileRowStatus,
       "msanMulticastProfile": msanMulticastProfile,
       "msanMulticastProfileTable": msanMulticastProfileTable,
       "msanMulticastProfileEntry": msanMulticastProfileEntry,
       "msanMulticastProfileName": msanMulticastProfileName,
       "msanMulticastProfileProtection": msanMulticastProfileProtection,
       "msanMulticastProfileStatus": msanMulticastProfileStatus,
       "msanMulticastProfileIgmpSnooping": msanMulticastProfileIgmpSnooping,
       "msanMulticastProfileIgmpSnoopingFastLeave": msanMulticastProfileIgmpSnoopingFastLeave,
       "msanMulticastProfileIgmpSnoopingSuppression": msanMulticastProfileIgmpSnoopingSuppression,
       "msanMulticastProfileIgmpProxy": msanMulticastProfileIgmpProxy,
       "msanMulticastProfileIgmpProxyIpAddress": msanMulticastProfileIgmpProxyIpAddress,
       "msanMulticastProfileIgmpFiltering": msanMulticastProfileIgmpFiltering,
       "msanMulticastProfileMulticastGroupLimit": msanMulticastProfileMulticastGroupLimit,
       "msanMulticastProfileMvr": msanMulticastProfileMvr,
       "msanMulticastProfileDescription": msanMulticastProfileDescription,
       "msanMulticastProfileRowStatus": msanMulticastProfileRowStatus,
       "msanMulticastProfileStaticGroupTable": msanMulticastProfileStaticGroupTable,
       "msanMulticastProfileStaticGroupEntry": msanMulticastProfileStaticGroupEntry,
       "msanMulticastProfileStaticGroupIpAddr": msanMulticastProfileStaticGroupIpAddr,
       "msanMulticastProfileStaticGroupRowStatus": msanMulticastProfileStaticGroupRowStatus,
       "msanSecurityProfile": msanSecurityProfile,
       "msanSecurityProfileTable": msanSecurityProfileTable,
       "msanSecurityProfileEntry": msanSecurityProfileEntry,
       "msanSecurityProfileName": msanSecurityProfileName,
       "msanSecurityProfileProtection": msanSecurityProfileProtection,
       "msanSecurityProfileStatus": msanSecurityProfileStatus,
       "msanSecurityProfileProtectedPort": msanSecurityProfileProtectedPort,
       "msanSecurityProfileMacSg": msanSecurityProfileMacSg,
       "msanSecurityProfileMacLimit": msanSecurityProfileMacLimit,
       "msanSecurityProfilePortSecurity": msanSecurityProfilePortSecurity,
       "msanSecurityProfileIpSg": msanSecurityProfileIpSg,
       "msanSecurityProfileIpSgBindingLimit": msanSecurityProfileIpSgBindingLimit,
       "msanSecurityProfileIpSgFilteringMode": msanSecurityProfileIpSgFilteringMode,
       "msanSecurityProfileArpInspec": msanSecurityProfileArpInspec,
       "msanSecurityProfileMacForward": msanSecurityProfileMacForward,
       "msanSecurityProfileDescription": msanSecurityProfileDescription,
       "msanSecurityProfileRowStatus": msanSecurityProfileRowStatus,
       "msanSecurityAclProfileTable": msanSecurityAclProfileTable,
       "msanSecurityAclProfileEntry": msanSecurityAclProfileEntry,
       "msanSecurityAclProfileAclDirection": msanSecurityAclProfileAclDirection,
       "msanSecurityAclProfileSequence": msanSecurityAclProfileSequence,
       "msanSecurityAclProfileAclType": msanSecurityAclProfileAclType,
       "msanSecurityAclProfileAclId": msanSecurityAclProfileAclId,
       "msanSecurityAclProfileRowStatus": msanSecurityAclProfileRowStatus,
       "msanL2cpProfile": msanL2cpProfile,
       "msanL2cpProfileTable": msanL2cpProfileTable,
       "msanL2cpProfileEntry": msanL2cpProfileEntry,
       "msanL2cpProfileName": msanL2cpProfileName,
       "msanL2cpProfileProtection": msanL2cpProfileProtection,
       "msanL2cpProfileStatus": msanL2cpProfileStatus,
       "msanL2cpProfileDescription": msanL2cpProfileDescription,
       "msanL2cpProfileRowStatus": msanL2cpProfileRowStatus,
       "msanL2cpProtocolTable": msanL2cpProtocolTable,
       "msanL2cpProtocolEntry": msanL2cpProtocolEntry,
       "msanL2cpProtocolName": msanL2cpProtocolName,
       "msanL2cpProtocolMacDestAddr": msanL2cpProtocolMacDestAddr,
       "msanL2cpProtocolEthertype": msanL2cpProtocolEthertype,
       "msanL2cpProtocolSubtype": msanL2cpProtocolSubtype,
       "msanL2cpProtocolRowStatus": msanL2cpProtocolRowStatus,
       "msanL2cpProfileProtocolTable": msanL2cpProfileProtocolTable,
       "msanL2cpProfileProtocolEntry": msanL2cpProfileProtocolEntry,
       "msanL2cpProfileProtocolRule": msanL2cpProfileProtocolRule,
       "msanL2cpProfileProtocolRowStatus": msanL2cpProfileProtocolRowStatus,
       "msanL2cpProfileVlanTable": msanL2cpProfileVlanTable,
       "msanL2cpProfileVlanEntry": msanL2cpProfileVlanEntry,
       "msanL2cpProfileVlanRowStatus": msanL2cpProfileVlanRowStatus,
       "msanXdslProfile": msanXdslProfile,
       "msanXdsl2LineConfTemplateTable": msanXdsl2LineConfTemplateTable,
       "msanXdsl2LineConfTemplateEntry": msanXdsl2LineConfTemplateEntry,
       "msanXdsl2LineConfTempProtection": msanXdsl2LineConfTempProtection,
       "msanXdsl2LineConfTempStatus": msanXdsl2LineConfTempStatus,
       "msanXdsl2LineAlarmConfTemplateTable": msanXdsl2LineAlarmConfTemplateTable,
       "msanXdsl2LineAlarmConfTemplateEntry": msanXdsl2LineAlarmConfTemplateEntry,
       "msanXdsl2LineAlarmConfTempProtection": msanXdsl2LineAlarmConfTempProtection,
       "msanXdsl2LineAlarmConfTempStatus": msanXdsl2LineAlarmConfTempStatus,
       "msanProfileConfigStatus": msanProfileConfigStatus,
       "msanDhcpRelay": msanDhcpRelay,
       "msanDhcpRaGlobal": msanDhcpRaGlobal,
       "msanDhcpRaStatus": msanDhcpRaStatus,
       "msanDhcpRaMode": msanDhcpRaMode,
       "msanDhcpRaCircuitType": msanDhcpRaCircuitType,
       "msanDhcpRaOpt82": msanDhcpRaOpt82,
       "msanDhcpRaOpt82ReplyMode": msanDhcpRaOpt82ReplyMode,
       "msanDhcpRaOpt82CircuitIdStatus": msanDhcpRaOpt82CircuitIdStatus,
       "msanDhcpRaOpt82RemoteIdStatus": msanDhcpRaOpt82RemoteIdStatus,
       "msanDhcpRaOpt82UnicastExtStatus": msanDhcpRaOpt82UnicastExtStatus,
       "msanDhcpRaFullModeSrvIpAddr": msanDhcpRaFullModeSrvIpAddr,
       "msanDhcpRaPortConfigTable": msanDhcpRaPortConfigTable,
       "msanDhcpRaPortConfigEntry": msanDhcpRaPortConfigEntry,
       "msanDhcpRaPortState": msanDhcpRaPortState,
       "msanDhcpRaPortCircuitId": msanDhcpRaPortCircuitId,
       "msanDhcpRaPortRemoteId": msanDhcpRaPortRemoteId,
       "msanDhcpRaPortMeter": msanDhcpRaPortMeter,
       "msanDhcpRaPortMaxDataRate": msanDhcpRaPortMaxDataRate,
       "msanDhcpRaPortCircuitType": msanDhcpRaPortCircuitType,
       "msanDhcpRaPortOpt82": msanDhcpRaPortOpt82,
       "msanDhcpRaPortOpt82ReplyMode": msanDhcpRaPortOpt82ReplyMode,
       "msanDhcpRaPortOpt82UnicastExtStatus": msanDhcpRaPortOpt82UnicastExtStatus,
       "msanDhcpRaPortCircuitIdType": msanDhcpRaPortCircuitIdType,
       "msanDhcpRaFullModeVlanTable": msanDhcpRaFullModeVlanTable,
       "msanDhcpRaFullModeVlanEntry": msanDhcpRaFullModeVlanEntry,
       "msanDhcpRaFullModeVlanId": msanDhcpRaFullModeVlanId,
       "msanDhcpRaFullModeVlanSrvIpAddr": msanDhcpRaFullModeVlanSrvIpAddr,
       "msanDhcpRaFullModeVlanRowStatus": msanDhcpRaFullModeVlanRowStatus,
       "msanDhcpRaStatTable": msanDhcpRaStatTable,
       "msanDhcpRaStatEntry": msanDhcpRaStatEntry,
       "msanDhcpRaStatDiscover": msanDhcpRaStatDiscover,
       "msanDhcpRaStatRequest": msanDhcpRaStatRequest,
       "msanDhcpRaStatOffer": msanDhcpRaStatOffer,
       "msanDhcpRaStatACK": msanDhcpRaStatACK,
       "msanDhcpRaStatNAK": msanDhcpRaStatNAK,
       "msanDhcpRaStatDecline": msanDhcpRaStatDecline,
       "msanDhcpRaStatMaxPacketSizeExceeded": msanDhcpRaStatMaxPacketSizeExceeded,
       "msanDhcpRaStatFrameErr": msanDhcpRaStatFrameErr,
       "msanDhcpRaStatOpt82Present": msanDhcpRaStatOpt82Present,
       "msanDhcpRaStatFrameUnsync": msanDhcpRaStatFrameUnsync,
       "msanDhcpRaStatRelease": msanDhcpRaStatRelease,
       "msanDhcpRaStatInform": msanDhcpRaStatInform,
       "msanDhcpRaVlanConfigTable": msanDhcpRaVlanConfigTable,
       "msanDhcpRaVlanConfigEntry": msanDhcpRaVlanConfigEntry,
       "msanDhcpRaVlanState": msanDhcpRaVlanState,
       "msanDhcpRaVlanMode": msanDhcpRaVlanMode,
       "msanDhcpRaVlanOpt82": msanDhcpRaVlanOpt82,
       "msanDhcpRaVlanOpt82ReplyMode": msanDhcpRaVlanOpt82ReplyMode,
       "msanDhcpRaVlanOpt82UnicastExtStatus": msanDhcpRaVlanOpt82UnicastExtStatus,
       "msanDhcpRaVlanCircuitIdType": msanDhcpRaVlanCircuitIdType,
       "msanDhcpRaPortVlanConfigTable": msanDhcpRaPortVlanConfigTable,
       "msanDhcpRaPortVlanConfigEntry": msanDhcpRaPortVlanConfigEntry,
       "msanDhcpRaPortVlanRemoteId": msanDhcpRaPortVlanRemoteId,
       "msanDhcpRaPortVlanConfigRowStatus": msanDhcpRaPortVlanConfigRowStatus,
       "msanDhcpv6RaGlobal": msanDhcpv6RaGlobal,
       "msanDhcpv6RaState": msanDhcpv6RaState,
       "msanDhcpv6RaMode": msanDhcpv6RaMode,
       "msanDhcpv6RaInterfaceIdStandard": msanDhcpv6RaInterfaceIdStandard,
       "msanDhcpv6Statistics": msanDhcpv6Statistics,
       "msanDhcpv6RaPortStatTable": msanDhcpv6RaPortStatTable,
       "msanDhcpv6RaPortStatEntry": msanDhcpv6RaPortStatEntry,
       "msanDhcpv6PortRaStatSolicit": msanDhcpv6PortRaStatSolicit,
       "msanDhcpv6PortRaStatAdvertise": msanDhcpv6PortRaStatAdvertise,
       "msanDhcpv6PortRaStatRequest": msanDhcpv6PortRaStatRequest,
       "msanDhcpv6PortRaStatReply": msanDhcpv6PortRaStatReply,
       "msanDhcpv6PortRaStatRenew": msanDhcpv6PortRaStatRenew,
       "msanDhcpv6PortRaStatRebind": msanDhcpv6PortRaStatRebind,
       "msanDhcpv6PortRaStatDecline": msanDhcpv6PortRaStatDecline,
       "msanDhcpv6PortRaStatReconfigure": msanDhcpv6PortRaStatReconfigure,
       "msanDhcpv6PortRaStatRelease": msanDhcpv6PortRaStatRelease,
       "msanDhcpv6PortRaStatInformRequest": msanDhcpv6PortRaStatInformRequest,
       "msanDhcpv6PortRaStatRelayForward": msanDhcpv6PortRaStatRelayForward,
       "msanDhcpv6PortRaStatRelayReply": msanDhcpv6PortRaStatRelayReply,
       "msanDhcpv6PortRaStatOversizeError": msanDhcpv6PortRaStatOversizeError,
       "msanDhcpv6PortRaStatFrameError": msanDhcpv6PortRaStatFrameError,
       "msanDhcpv6PortRaStatFrameUnsyncError": msanDhcpv6PortRaStatFrameUnsyncError,
       "msanDhcpv6PortRaStatSysError": msanDhcpv6PortRaStatSysError,
       "msanDhcpv6RaStatSolicit": msanDhcpv6RaStatSolicit,
       "msanDhcpv6RaStatAdvertise": msanDhcpv6RaStatAdvertise,
       "msanDhcpv6RaStatRequest": msanDhcpv6RaStatRequest,
       "msanDhcpv6RaStatReply": msanDhcpv6RaStatReply,
       "msanDhcpv6RaStatRenew": msanDhcpv6RaStatRenew,
       "msanDhcpv6RaStatRebind": msanDhcpv6RaStatRebind,
       "msanDhcpv6RaStatDecline": msanDhcpv6RaStatDecline,
       "msanDhcpv6RaStatReconfigure": msanDhcpv6RaStatReconfigure,
       "msanDhcpv6RaStatRelease": msanDhcpv6RaStatRelease,
       "msanDhcpv6RaStatInformRequest": msanDhcpv6RaStatInformRequest,
       "msanDhcpv6RaStatRelayForward": msanDhcpv6RaStatRelayForward,
       "msanDhcpv6RaStatRelayReply": msanDhcpv6RaStatRelayReply,
       "msanDhcpv6RaStatOversizeError": msanDhcpv6RaStatOversizeError,
       "msanDhcpv6RaStatFrameError": msanDhcpv6RaStatFrameError,
       "msanDhcpv6RaStatFrameUnsyncError": msanDhcpv6RaStatFrameUnsyncError,
       "msanDhcpv6RaStatSysError": msanDhcpv6RaStatSysError,
       "msanDhcpv6RaPortConfigTable": msanDhcpv6RaPortConfigTable,
       "msanDhcpv6RaPortConfigEntry": msanDhcpv6RaPortConfigEntry,
       "msanDhcpv6RaPortState": msanDhcpv6RaPortState,
       "msanDhcpv6RaPortTrusted": msanDhcpv6RaPortTrusted,
       "msanDhcpv6RaPortInterfaceIdStandard": msanDhcpv6RaPortInterfaceIdStandard,
       "msanDhcpv6RaPortInterfaceId": msanDhcpv6RaPortInterfaceId,
       "msanDhcpv6RaPortRemoteId": msanDhcpv6RaPortRemoteId,
       "msanDhcpv6RaPortRemoteIdEnterpriseNum": msanDhcpv6RaPortRemoteIdEnterpriseNum,
       "msanDhcpv6RaVlanConfigTable": msanDhcpv6RaVlanConfigTable,
       "msanDhcpv6RaVlanConfigEntry": msanDhcpv6RaVlanConfigEntry,
       "msanDhcpv6RaVlanState": msanDhcpv6RaVlanState,
       "msanDhcpv6RaVlanInterfaceIdStandard": msanDhcpv6RaVlanInterfaceIdStandard,
       "msanDhcpv6RaPortVlanConfigTable": msanDhcpv6RaPortVlanConfigTable,
       "msanDhcpv6RaPortVlanConfigEntry": msanDhcpv6RaPortVlanConfigEntry,
       "msanDhcpv6RaPortVlanRemoteId": msanDhcpv6RaPortVlanRemoteId,
       "msanDhcpv6RaPortVlanRemoteIdEnterpriseNum": msanDhcpv6RaPortVlanRemoteIdEnterpriseNum,
       "msanDhcpv6RaPortVlanRowStatus": msanDhcpv6RaPortVlanRowStatus,
       "msanSntp": msanSntp,
       "msanSntpGlobal": msanSntpGlobal,
       "msanSntpTzOffset": msanSntpTzOffset,
       "msanSntpTzName": msanSntpTzName,
       "msanSntpTzDstOffset": msanSntpTzDstOffset,
       "msanSntpTzDstStartMonth": msanSntpTzDstStartMonth,
       "msanSntpTzDstStartWeek": msanSntpTzDstStartWeek,
       "msanSntpTzDstStartDayInWeek": msanSntpTzDstStartDayInWeek,
       "msanSntpTzDstStartTime": msanSntpTzDstStartTime,
       "msanSntpTzDstEndMonth": msanSntpTzDstEndMonth,
       "msanSntpTzDstEndWeek": msanSntpTzDstEndWeek,
       "msanSntpTzDstEndDayInWeek": msanSntpTzDstEndDayInWeek,
       "msanSntpTzDstEndTime": msanSntpTzDstEndTime,
       "msanSnmp": msanSnmp,
       "msanSnmpGlobal": msanSnmpGlobal,
       "msanSnmpTrapRecvUdpPort": msanSnmpTrapRecvUdpPort,
       "msanIgmpSnooping": msanIgmpSnooping,
       "msanIgmpSnoopingGlobal": msanIgmpSnoopingGlobal,
       "msanIgmpSnoopingReportSuppression": msanIgmpSnoopingReportSuppression,
       "msanIgmpSnoopingAdminState": msanIgmpSnoopingAdminState,
       "msanIgmpSnoopingLoggingVlanId": msanIgmpSnoopingLoggingVlanId,
       "msanIgmpSnoopingViolationAction": msanIgmpSnoopingViolationAction,
       "msanIgmpSnoopingFastLeaveAdminMode": msanIgmpSnoopingFastLeaveAdminMode,
       "msanIgmpSnoopingGroupMembershipInterval": msanIgmpSnoopingGroupMembershipInterval,
       "msanIgmpSnoopingMaxResponseTime": msanIgmpSnoopingMaxResponseTime,
       "msanIgmpVersion": msanIgmpVersion,
       "msanIgmpClear": msanIgmpClear,
       "msanIgmpSnoopingTable": msanIgmpSnoopingTable,
       "msanIgmpSnoopingEntry": msanIgmpSnoopingEntry,
       "msanIgmpSnoopingIntfStandaloneQuerier": msanIgmpSnoopingIntfStandaloneQuerier,
       "msanIgmpSnoopingIntfFilter": msanIgmpSnoopingIntfFilter,
       "msanIgmpSnoopingGroupLimit": msanIgmpSnoopingGroupLimit,
       "msanSwitchIGMPVlanCurrentMrouterTable": msanSwitchIGMPVlanCurrentMrouterTable,
       "msanSwitchIGMPVlanCurrentMrouterEntry": msanSwitchIGMPVlanCurrentMrouterEntry,
       "msanSwitchIGMPVlanCurrentMrouterEnableState": msanSwitchIGMPVlanCurrentMrouterEnableState,
       "msanSwitchIGMPSnoopingStaticIntfMulticastRouterTable": msanSwitchIGMPSnoopingStaticIntfMulticastRouterTable,
       "msanSwitchIGMPSnoopingStaticIntfMulticastRouterEntry": msanSwitchIGMPSnoopingStaticIntfMulticastRouterEntry,
       "msanSwitchIGMPSnoopingIntfIndex": msanSwitchIGMPSnoopingIntfIndex,
       "msanSwitchIGMPSnoopingIntfAdminMode": msanSwitchIGMPSnoopingIntfAdminMode,
       "msanSwitchIGMPSnoopingIntfGroupMembershipInterval": msanSwitchIGMPSnoopingIntfGroupMembershipInterval,
       "msanSwitchIGMPSnoopingIntfMaxResponseTime": msanSwitchIGMPSnoopingIntfMaxResponseTime,
       "msanSwitchIGMPSnoopingIntfMRPExpirationTime": msanSwitchIGMPSnoopingIntfMRPExpirationTime,
       "msanSwitchIGMPSnoopingIntfFastLeaveAdminMode": msanSwitchIGMPSnoopingIntfFastLeaveAdminMode,
       "msanSwitchIGMPSnoopingStaticIntfMulticastRouterMode": msanSwitchIGMPSnoopingStaticIntfMulticastRouterMode,
       "msanSwitchIGMPSnoopingIntfVlanIDs": msanSwitchIGMPSnoopingIntfVlanIDs,
       "msanSwitchIGMPVlanStaticMrouterTable": msanSwitchIGMPVlanStaticMrouterTable,
       "msanSwitchIGMPVlanStaticMrouterEntry": msanSwitchIGMPVlanStaticMrouterEntry,
       "msanSwitchIGMPVlanStaticMrouterEnableState": msanSwitchIGMPVlanStaticMrouterEnableState,
       "msanSwitchIGMPSnoopingVlanTable": msanSwitchIGMPSnoopingVlanTable,
       "msanSwitchIGMPSnoopingVlanEntry": msanSwitchIGMPSnoopingVlanEntry,
       "msanSwitchIGMPSnoopingVlanAdminMode": msanSwitchIGMPSnoopingVlanAdminMode,
       "msanSwitchIGMPSnoopingVlanGroupMembershipInterval": msanSwitchIGMPSnoopingVlanGroupMembershipInterval,
       "msanSwitchIGMPSnoopingVlanMaxResponseTime": msanSwitchIGMPSnoopingVlanMaxResponseTime,
       "msanSwitchIGMPSnoopingVlanFastLeaveAdminMode": msanSwitchIGMPSnoopingVlanFastLeaveAdminMode,
       "msanSwitchIGMPSnoopingVlanMRPExpirationTime": msanSwitchIGMPSnoopingVlanMRPExpirationTime,
       "msanSwitchIGMPSnoopingVlanAdminState": msanSwitchIGMPSnoopingVlanAdminState,
       "msanSwitchIGMPProxyVlanTable": msanSwitchIGMPProxyVlanTable,
       "msanSwitchIGMPProxyVlanEntry": msanSwitchIGMPProxyVlanEntry,
       "msanSwitchIGMPProxyVlanIpAddr": msanSwitchIGMPProxyVlanIpAddr,
       "msanSwitchIGMPProxyVlanRowStatus": msanSwitchIGMPProxyVlanRowStatus,
       "msanIgmpStatistics": msanIgmpStatistics,
       "msanIgmpStatGlobal": msanIgmpStatGlobal,
       "msanIgmpStatRxV1": msanIgmpStatRxV1,
       "msanIgmpStatRxV2Join": msanIgmpStatRxV2Join,
       "msanIgmpStatRxV2Leave": msanIgmpStatRxV2Leave,
       "msanIgmpStatRxV3Report": msanIgmpStatRxV3Report,
       "msanIgmpStatRxQuery": msanIgmpStatRxQuery,
       "msanIgmpStatRxError": msanIgmpStatRxError,
       "msanIgmpStatRxBlockByIgmpFilter": msanIgmpStatRxBlockByIgmpFilter,
       "msanIgmpStatRxBlockByMcastAcl": msanIgmpStatRxBlockByMcastAcl,
       "msanIgmpStatRxBlockByMcastCac": msanIgmpStatRxBlockByMcastCac,
       "msanIgmpStatRxBlockByIgmpVersion": msanIgmpStatRxBlockByIgmpVersion,
       "msanIgmpPortStatTable": msanIgmpPortStatTable,
       "msanIgmpPortStatEntry": msanIgmpPortStatEntry,
       "msanIgmpPortStatRxV1": msanIgmpPortStatRxV1,
       "msanIgmpPortStatTxV1": msanIgmpPortStatTxV1,
       "msanIgmpPortStatRxV2Join": msanIgmpPortStatRxV2Join,
       "msanIgmpPortStatTxV2Join": msanIgmpPortStatTxV2Join,
       "msanIgmpPortStatRxV2Leave": msanIgmpPortStatRxV2Leave,
       "msanIgmpPortStatTxV2Leave": msanIgmpPortStatTxV2Leave,
       "msanIgmpPortStatRxV3Report": msanIgmpPortStatRxV3Report,
       "msanIgmpPortStatTxV3Report": msanIgmpPortStatTxV3Report,
       "msanIgmpPortStatRxQuery": msanIgmpPortStatRxQuery,
       "msanIgmpPortStatRxError": msanIgmpPortStatRxError,
       "msanIgmpPortStatRxBlockByIgmpFilter": msanIgmpPortStatRxBlockByIgmpFilter,
       "msanIgmpPortStatRxBlockByMcastAcl": msanIgmpPortStatRxBlockByMcastAcl,
       "msanIgmpPortStatRxBlockByMcastCac": msanIgmpPortStatRxBlockByMcastCac,
       "msanIgmpPortStatTxQuery": msanIgmpPortStatTxQuery,
       "msanIgmpPortStatRxBlockByIgmpVersion": msanIgmpPortStatRxBlockByIgmpVersion,
       "msanPort": msanPort,
       "msanPortGlobal": msanPortGlobal,
       "msanPortTable": msanPortTable,
       "msanPortEntry": msanPortEntry,
       "msanPortMNFlag": msanPortMNFlag,
       "msanPortMasterSlave": msanPortMasterSlave,
       "msanPortNegCapAdvertisedBits": msanPortNegCapAdvertisedBits,
       "msanPortSpeedDuplex": msanPortSpeedDuplex,
       "msanPortStpP2PAutoState": msanPortStpP2PAutoState,
       "msanPortUsageType": msanPortUsageType,
       "msanPppoeIA": msanPppoeIA,
       "msanPppoeIAGlobal": msanPppoeIAGlobal,
       "msanPppoeIAStatus": msanPppoeIAStatus,
       "msanPppoeIAVsaReplyMode": msanPppoeIAVsaReplyMode,
       "msanPppoeIACircuitIdStatus": msanPppoeIACircuitIdStatus,
       "msanPppoeIARemoteIdStatus": msanPppoeIARemoteIdStatus,
       "msanPppoeIAPortTable": msanPppoeIAPortTable,
       "msanPppoeIAPortEntry": msanPppoeIAPortEntry,
       "msanPppoeIAPortStatus": msanPppoeIAPortStatus,
       "msanPppoeIAPortRemoteId": msanPppoeIAPortRemoteId,
       "msanPppoeIAPortCircuitType": msanPppoeIAPortCircuitType,
       "msanPppoeIaStatistics": msanPppoeIaStatistics,
       "msanPppoeIaStatPADI": msanPppoeIaStatPADI,
       "msanPppoeIaStatPADR": msanPppoeIaStatPADR,
       "msanPppoeIaStatPADO": msanPppoeIaStatPADO,
       "msanPppoeIaStatPADS": msanPppoeIaStatPADS,
       "msanPppoeIaStatPADT": msanPppoeIaStatPADT,
       "msanPppoeIaStatUnsutableFrames": msanPppoeIaStatUnsutableFrames,
       "msanPppoeIaStatUnknownFrames": msanPppoeIaStatUnknownFrames,
       "msanPppoeIaStatInvalidFrames": msanPppoeIaStatInvalidFrames,
       "msanPppoeIaPortStatisticsTable": msanPppoeIaPortStatisticsTable,
       "msanPppoeIaPortStatisticsEntry": msanPppoeIaPortStatisticsEntry,
       "msanPppoeIaPortStatPADI": msanPppoeIaPortStatPADI,
       "msanPppoeIaPortStatPADR": msanPppoeIaPortStatPADR,
       "msanPppoeIaPortStatPADO": msanPppoeIaPortStatPADO,
       "msanPppoeIaPortStatPADS": msanPppoeIaPortStatPADS,
       "msanPppoeIaPortStatPADT": msanPppoeIaPortStatPADT,
       "msanPppoeIaPortStatUnsutableFrames": msanPppoeIaPortStatUnsutableFrames,
       "msanPppoeIaPortStatUnknownFrames": msanPppoeIaPortStatUnknownFrames,
       "msanPppoeIaPortStatInvalidFrames": msanPppoeIaPortStatInvalidFrames,
       "msanPppoeIaVlanTable": msanPppoeIaVlanTable,
       "msanPppoeIaVlanEntry": msanPppoeIaVlanEntry,
       "msanPppoeIaVlanStatus": msanPppoeIaVlanStatus,
       "msanQoS": msanQoS,
       "msanQosGlobal": msanQosGlobal,
       "msanIpAclRuleTable": msanIpAclRuleTable,
       "msanIpAclRuleEntry": msanIpAclRuleEntry,
       "msanIpAclIndex": msanIpAclIndex,
       "msanIpAclRuleIndex": msanIpAclRuleIndex,
       "msanIpAclRuleAssignVlanId": msanIpAclRuleAssignVlanId,
       "msanIpAclRuleAssignCoSPriority": msanIpAclRuleAssignCoSPriority,
       "msanIpAclRuleEgressIntf": msanIpAclRuleEgressIntf,
       "msanIpAclRuleAssignVlanId2": msanIpAclRuleAssignVlanId2,
       "msanIpAclRuleRemoveVlanId": msanIpAclRuleRemoveVlanId,
       "msanIpAclRuleIcmpType": msanIpAclRuleIcmpType,
       "msanIpAclRuleDestMacAddr": msanIpAclRuleDestMacAddr,
       "msanIpAclRuleDestMacMask": msanIpAclRuleDestMacMask,
       "msanIpAclRuleSrcMacAddr": msanIpAclRuleSrcMacAddr,
       "msanIpAclRuleSrcMacMask": msanIpAclRuleSrcMacMask,
       "msanIpAclRuleCos": msanIpAclRuleCos,
       "msanIpAclRuleCos2": msanIpAclRuleCos2,
       "msanIpAclRuleVlanId": msanIpAclRuleVlanId,
       "msanIpAclRuleVlanId2": msanIpAclRuleVlanId2,
       "msanIpAclRuleCVlanId": msanIpAclRuleCVlanId,
       "msanIpAclRuleSVlanId": msanIpAclRuleSVlanId,
       "msanIpAclRuleAssignCVlanId": msanIpAclRuleAssignCVlanId,
       "msanIpAclRuleAssignSVlanId": msanIpAclRuleAssignSVlanId,
       "msanIpAclRuleRemoveSVlanId": msanIpAclRuleRemoveSVlanId,
       "msanIpAclRuleVlanIdRangeStart": msanIpAclRuleVlanIdRangeStart,
       "msanIpAclRuleVlanIdRangeEnd": msanIpAclRuleVlanIdRangeEnd,
       "msanIpAclRuleVlanId2RangeStart": msanIpAclRuleVlanId2RangeStart,
       "msanIpAclRuleVlanId2RangeEnd": msanIpAclRuleVlanId2RangeEnd,
       "msanIpAclRuleSVlanIdRangeStart": msanIpAclRuleSVlanIdRangeStart,
       "msanIpAclRuleSVlanIdRangeEnd": msanIpAclRuleSVlanIdRangeEnd,
       "msanIpAclRuleCVlanIdRangeStart": msanIpAclRuleCVlanIdRangeStart,
       "msanIpAclRuleCVlanIdRangeEnd": msanIpAclRuleCVlanIdRangeEnd,
       "msanIpAclRuleSrcIpv6Address": msanIpAclRuleSrcIpv6Address,
       "msanIpAclRuleSrcIpv6AddressMaskLen": msanIpAclRuleSrcIpv6AddressMaskLen,
       "msanIpAclRuleDestIpv6Address": msanIpAclRuleDestIpv6Address,
       "msanIpAclRuleDestIpv6AddressMaskLen": msanIpAclRuleDestIpv6AddressMaskLen,
       "msanMacAclRuleTable": msanMacAclRuleTable,
       "msanMacAclRuleEntry": msanMacAclRuleEntry,
       "msanMacAclIndex": msanMacAclIndex,
       "msanMacAclRuleIndex": msanMacAclRuleIndex,
       "msanMacAclRuleEgressIntf": msanMacAclRuleEgressIntf,
       "msanMacAclRuleAssignVlanId": msanMacAclRuleAssignVlanId,
       "msanMacAclRuleAssignCoSPriority": msanMacAclRuleAssignCoSPriority,
       "msanMacAclRuleAssignVlanId2": msanMacAclRuleAssignVlanId2,
       "msanMacAclRuleRemoveVlanId": msanMacAclRuleRemoveVlanId,
       "msanMacAclRuleCVlanId": msanMacAclRuleCVlanId,
       "msanMacAclRuleSVlanId": msanMacAclRuleSVlanId,
       "msanMacAclRuleAssignCVlanId": msanMacAclRuleAssignCVlanId,
       "msanMacAclRuleAssignSVlanId": msanMacAclRuleAssignSVlanId,
       "msanMacAclRuleRemoveSVlanId": msanMacAclRuleRemoveSVlanId,
       "msanMacAclRuleSVlanIdRangeStart": msanMacAclRuleSVlanIdRangeStart,
       "msanMacAclRuleSVlanIdRangeEnd": msanMacAclRuleSVlanIdRangeEnd,
       "msanMacAclRuleCVlanIdRangeStart": msanMacAclRuleCVlanIdRangeStart,
       "msanMacAclRuleCVlanIdRangeEnd": msanMacAclRuleCVlanIdRangeEnd,
       "msanCosQueueControlTable": msanCosQueueControlTable,
       "msanCosQueueControlEntry": msanCosQueueControlEntry,
       "msanCosQueueControlIntfBurstSize": msanCosQueueControlIntfBurstSize,
       "msanCosQueueIntfShapingRate": msanCosQueueIntfShapingRate,
       "msanCosQueueTable": msanCosQueueTable,
       "msanCosQueueEntry": msanCosQueueEntry,
       "msanCosQueueIndex": msanCosQueueIndex,
       "msanCosQueueWeight": msanCosQueueWeight,
       "msanCosQueueLength": msanCosQueueLength,
       "msanCosMapIntfTrustTable": msanCosMapIntfTrustTable,
       "msanCosMapIntfTrustEntry": msanCosMapIntfTrustEntry,
       "msanCosMapIntfTrustMode": msanCosMapIntfTrustMode,
       "msanQosProfileTable": msanQosProfileTable,
       "msanQosProfileEntry": msanQosProfileEntry,
       "msanQosProfileName": msanQosProfileName,
       "msanQosProfileMatchInAny": msanQosProfileMatchInAny,
       "msanQosProfileMatchInMacDestAddr": msanQosProfileMatchInMacDestAddr,
       "msanQosProfileMatchInMacDestMask": msanQosProfileMatchInMacDestMask,
       "msanQosProfileMatchInMacSrcAddr": msanQosProfileMatchInMacSrcAddr,
       "msanQosProfileMatchInMacSrcMask": msanQosProfileMatchInMacSrcMask,
       "msanQosProfileMatchInCos": msanQosProfileMatchInCos,
       "msanQosProfileMatchInCos2": msanQosProfileMatchInCos2,
       "msanQosProfileMatchInVlanId": msanQosProfileMatchInVlanId,
       "msanQosProfileMatchInVlanId2": msanQosProfileMatchInVlanId2,
       "msanQosProfileMatchInEthertype": msanQosProfileMatchInEthertype,
       "msanQosProfileMatchInIpProtocol": msanQosProfileMatchInIpProtocol,
       "msanQosProfileMatchInIpSrcAddr": msanQosProfileMatchInIpSrcAddr,
       "msanQosProfileMatchInIpSrcMask": msanQosProfileMatchInIpSrcMask,
       "msanQosProfileMatchInIpDestAddr": msanQosProfileMatchInIpDestAddr,
       "msanQosProfileMatchInIpDestMask": msanQosProfileMatchInIpDestMask,
       "msanQosProfileMatchInIpDscp": msanQosProfileMatchInIpDscp,
       "msanQosProfileMatchInIpPrecedence": msanQosProfileMatchInIpPrecedence,
       "msanQosProfileMatchInIpTosBits": msanQosProfileMatchInIpTosBits,
       "msanQosProfileMatchInIpTosMask": msanQosProfileMatchInIpTosMask,
       "msanQosProfileMatchInL4SrcPort": msanQosProfileMatchInL4SrcPort,
       "msanQosProfileMatchInL4DestPort": msanQosProfileMatchInL4DestPort,
       "msanQosProfileMatchOutAny": msanQosProfileMatchOutAny,
       "msanQosProfileMatchOutMacDestAddr": msanQosProfileMatchOutMacDestAddr,
       "msanQosProfileMatchOutMacDestMask": msanQosProfileMatchOutMacDestMask,
       "msanQosProfileMatchOutMacSrcAddr": msanQosProfileMatchOutMacSrcAddr,
       "msanQosProfileMatchOutMacSrcMask": msanQosProfileMatchOutMacSrcMask,
       "msanQosProfileMatchOutCos": msanQosProfileMatchOutCos,
       "msanQosProfileMatchOutCos2": msanQosProfileMatchOutCos2,
       "msanQosProfileMatchOutVlanId": msanQosProfileMatchOutVlanId,
       "msanQosProfileMatchOutVlanId2": msanQosProfileMatchOutVlanId2,
       "msanQosProfileMatchOutEthertype": msanQosProfileMatchOutEthertype,
       "msanQosProfileMatchOutIpProtocol": msanQosProfileMatchOutIpProtocol,
       "msanQosProfileMatchOutIpSrcAddr": msanQosProfileMatchOutIpSrcAddr,
       "msanQosProfileMatchOutIpSrcMask": msanQosProfileMatchOutIpSrcMask,
       "msanQosProfileMatchOutIpDestAddr": msanQosProfileMatchOutIpDestAddr,
       "msanQosProfileMatchOutIpDestMask": msanQosProfileMatchOutIpDestMask,
       "msanQosProfileMatchOutIpDscp": msanQosProfileMatchOutIpDscp,
       "msanQosProfileMatchOutIpPrecedence": msanQosProfileMatchOutIpPrecedence,
       "msanQosProfileMatchOutIpTosBits": msanQosProfileMatchOutIpTosBits,
       "msanQosProfileMatchOutIpTosMask": msanQosProfileMatchOutIpTosMask,
       "msanQosProfileMatchOutL4SrcPort": msanQosProfileMatchOutL4SrcPort,
       "msanQosProfileMatchOutL4DestPort": msanQosProfileMatchOutL4DestPort,
       "msanQosProfileInCdr": msanQosProfileInCdr,
       "msanQosProfileInPdr": msanQosProfileInPdr,
       "msanQosProfileOutCdr": msanQosProfileOutCdr,
       "msanQosProfileOutPdr": msanQosProfileOutPdr,
       "msanQosProfileInTrustMode": msanQosProfileInTrustMode,
       "msanQosProfileInMarkCos": msanQosProfileInMarkCos,
       "msanQosProfileInMarkDscp": msanQosProfileInMarkDscp,
       "msanQosProfileRowStatus": msanQosProfileRowStatus,
       "msanQosProfilePriority": msanQosProfilePriority,
       "msanQosProfileInCdrBurstSize": msanQosProfileInCdrBurstSize,
       "msanQosProfileInPdrBurstSize": msanQosProfileInPdrBurstSize,
       "msanQosProfileOutCdrBurstSize": msanQosProfileOutCdrBurstSize,
       "msanQosProfileOutPdrBurstSize": msanQosProfileOutPdrBurstSize,
       "msanQosProfileMatchInSrcIpv6Address": msanQosProfileMatchInSrcIpv6Address,
       "msanQosProfileMatchInSrcIpv6AddressMaskLen": msanQosProfileMatchInSrcIpv6AddressMaskLen,
       "msanQosProfileMatchInDestIpv6Address": msanQosProfileMatchInDestIpv6Address,
       "msanQosProfileMatchInDestIpv6AddressMaskLen": msanQosProfileMatchInDestIpv6AddressMaskLen,
       "msanQosProfileMatchOutSrcIpv6Address": msanQosProfileMatchOutSrcIpv6Address,
       "msanQosProfileMatchOutSrcIpv6AddressMaskLen": msanQosProfileMatchOutSrcIpv6AddressMaskLen,
       "msanQosProfileMatchOutDestIpv6Address": msanQosProfileMatchOutDestIpv6Address,
       "msanQosProfileMatchOutDestIpv6AddressMaskLen": msanQosProfileMatchOutDestIpv6AddressMaskLen,
       "msanQosIntfProfileTable": msanQosIntfProfileTable,
       "msanQosIntfProfileEntry": msanQosIntfProfileEntry,
       "msanQosIntfProfileAtmVpi": msanQosIntfProfileAtmVpi,
       "msanQosIntfProfileAtmVci": msanQosIntfProfileAtmVci,
       "msanQosIntfProfileRowStatus": msanQosIntfProfileRowStatus,
       "msanQosStatistics": msanQosStatistics,
       "msanQosPortStatTable": msanQosPortStatTable,
       "msanQosPortStatEntry": msanQosPortStatEntry,
       "msanQosPortStatInDroppedFrames": msanQosPortStatInDroppedFrames,
       "msanQosPortStatOutDroppedFrames": msanQosPortStatOutDroppedFrames,
       "msanQosPortProfileStatTable": msanQosPortProfileStatTable,
       "msanQosPortProfileStatEntry": msanQosPortProfileStatEntry,
       "msanQosPortProfileStatQueueCurrent": msanQosPortProfileStatQueueCurrent,
       "msanQosPortProfileStatQueueAverage": msanQosPortProfileStatQueueAverage,
       "msanQosPortProfileStatQueueMax": msanQosPortProfileStatQueueMax,
       "msanIpAclTable": msanIpAclTable,
       "msanIpAclEntry": msanIpAclEntry,
       "msanIpAclId": msanIpAclId,
       "msanIpAclProtection": msanIpAclProtection,
       "msanIpAclStatus": msanIpAclStatus,
       "msanMacAclTable": msanMacAclTable,
       "msanMacAclEntry": msanMacAclEntry,
       "msanMacAclId": msanMacAclId,
       "msanMacAclProtection": msanMacAclProtection,
       "msanMacAclStatus": msanMacAclStatus,
       "msanForwardingDb": msanForwardingDb,
       "msanForwardingDbGlobal": msanForwardingDbGlobal,
       "msanAddressLearningMode": msanAddressLearningMode,
       "msanAddressLearningVlanId": msanAddressLearningVlanId,
       "msanSwitchAddressAgingTimeout": msanSwitchAddressAgingTimeout,
       "msanDiagnostics": msanDiagnostics,
       "msanDiagnosticsGlobal": msanDiagnosticsGlobal,
       "msanDiagnosticsFanSpeedLevel": msanDiagnosticsFanSpeedLevel,
       "msanDiagnosticsMaxFanSpeedLevel": msanDiagnosticsMaxFanSpeedLevel,
       "msanDiagnosticsTestTable": msanDiagnosticsTestTable,
       "msanDiagnosticsTestEntry": msanDiagnosticsTestEntry,
       "msanDiagnosticsTestCode": msanDiagnosticsTestCode,
       "msanDiagnosticsTestName": msanDiagnosticsTestName,
       "msanDiagnosticsTestActivity": msanDiagnosticsTestActivity,
       "msanDiagnosticsTestTime": msanDiagnosticsTestTime,
       "msanDiagnosticsTestPriority": msanDiagnosticsTestPriority,
       "msanDiagnosticsTestType": msanDiagnosticsTestType,
       "msanDiagnosticsTestTimeMin": msanDiagnosticsTestTimeMin,
       "msanDiagnosticsTestTimeMax": msanDiagnosticsTestTimeMax,
       "msanDiagnosticsErrorTable": msanDiagnosticsErrorTable,
       "msanDiagnosticsErrorEntry": msanDiagnosticsErrorEntry,
       "msanDiagnosticsErrorCode": msanDiagnosticsErrorCode,
       "msanDiagnosticsErrorDescription": msanDiagnosticsErrorDescription,
       "msanDiagnosticsErrorPriority": msanDiagnosticsErrorPriority,
       "msanDiagnosticsErrorObjectType": msanDiagnosticsErrorObjectType,
       "msanDiagnosticsErrorMeasure": msanDiagnosticsErrorMeasure,
       "msanDiagnosticsErrorMeasureActive": msanDiagnosticsErrorMeasureActive,
       "msanDiagnosticsErrorProbableCause": msanDiagnosticsErrorProbableCause,
       "msanDiagnosticsErrorObjectTypeId": msanDiagnosticsErrorObjectTypeId,
       "msanDiagnosticsErrorMeasureId": msanDiagnosticsErrorMeasureId,
       "msanDiagnosticsTempTable": msanDiagnosticsTempTable,
       "msanDiagnosticsTempEntry": msanDiagnosticsTempEntry,
       "msanDiagnosticsTempSensorID": msanDiagnosticsTempSensorID,
       "msanDiagnosticsTempSensorName": msanDiagnosticsTempSensorName,
       "msanDiagnosticsTempCurrent": msanDiagnosticsTempCurrent,
       "msanDiagnosticsTempCriticUnderheatThreshold": msanDiagnosticsTempCriticUnderheatThreshold,
       "msanDiagnosticsTempUnderheatThreshold": msanDiagnosticsTempUnderheatThreshold,
       "msanDiagnosticsTempOverheatThreshold": msanDiagnosticsTempOverheatThreshold,
       "msanDiagnosticsTempCriticOverheatThreshold": msanDiagnosticsTempCriticOverheatThreshold,
       "msanDiagnosticsErrorFilterTable": msanDiagnosticsErrorFilterTable,
       "msanDiagnosticsErrorFilterEntry": msanDiagnosticsErrorFilterEntry,
       "msanDiagnosticsErrorFilterErrMask": msanDiagnosticsErrorFilterErrMask,
       "msanDiagnosticsErrorFilterObjMask": msanDiagnosticsErrorFilterObjMask,
       "msanDiagnosticsErrorFilterRowStatus": msanDiagnosticsErrorFilterRowStatus,
       "msanDiagnosticsErrorSeverityTable": msanDiagnosticsErrorSeverityTable,
       "msanDiagnosticsErrorSeverityEntry": msanDiagnosticsErrorSeverityEntry,
       "msanDiagnosticsErrorSeverityErrCode": msanDiagnosticsErrorSeverityErrCode,
       "msanDiagnosticsErrorSeverityErrPriority": msanDiagnosticsErrorSeverityErrPriority,
       "msanDiagnosticsErrorSeverityObjMask": msanDiagnosticsErrorSeverityObjMask,
       "msanDiagnosticsErrorSeverityRowStatus": msanDiagnosticsErrorSeverityRowStatus,
       "msanPpp": msanPpp,
       "msanPppGlobal": msanPppGlobal,
       "msanPppLocalIpAddress": msanPppLocalIpAddress,
       "msanPppRemoteIpAddress": msanPppRemoteIpAddress,
       "msanPppAuthProtocol": msanPppAuthProtocol,
       "msanPppEchoInterval": msanPppEchoInterval,
       "msanPppVanJacobsonCompression": msanPppVanJacobsonCompression,
       "msanPppAdminState": msanPppAdminState,
       "msanAlarmPanel": msanAlarmPanel,
       "msanAlarmPanelGlobal": msanAlarmPanelGlobal,
       "msanAlarmPanelAudioAlarmPriority": msanAlarmPanelAudioAlarmPriority,
       "msanAlarmPanelSerialPortType": msanAlarmPanelSerialPortType,
       "msanAlarmPanelTable": msanAlarmPanelTable,
       "msanAlarmPanelEntry": msanAlarmPanelEntry,
       "msanAlarmPanelIndex": msanAlarmPanelIndex,
       "msanAlarmPanelConnectionState": msanAlarmPanelConnectionState,
       "msanAlarmPanelAdminState": msanAlarmPanelAdminState,
       "msanAlarmPanelIndicatorTable": msanAlarmPanelIndicatorTable,
       "msanAlarmPanelIndicatorEntry": msanAlarmPanelIndicatorEntry,
       "msanAlarmPanelIndicatorIndex": msanAlarmPanelIndicatorIndex,
       "msanAlarmPanelIndicatorErrCode": msanAlarmPanelIndicatorErrCode,
       "msanAlarmPanelInputTable": msanAlarmPanelInputTable,
       "msanAlarmPanelInputEntry": msanAlarmPanelInputEntry,
       "msanAlarmPanelInputIndex": msanAlarmPanelInputIndex,
       "msanAlarmPanelInputErrCode": msanAlarmPanelInputErrCode,
       "msanAlarmPanelInputActiveLevel": msanAlarmPanelInputActiveLevel,
       "msanMvr": msanMvr,
       "msanMvrGlobal": msanMvrGlobal,
       "msanMvrPortTable": msanMvrPortTable,
       "msanMvrPortEntry": msanMvrPortEntry,
       "msanMvrPortAdminMode": msanMvrPortAdminMode,
       "msanMvrMulticastGroupTable": msanMvrMulticastGroupTable,
       "msanMvrMulticastGroupEntry": msanMvrMulticastGroupEntry,
       "msanMvrMulticastGroupMVlanId": msanMvrMulticastGroupMVlanId,
       "msanMvrMulticastGroupStartIp": msanMvrMulticastGroupStartIp,
       "msanMvrMulticastGroupEndIp": msanMvrMulticastGroupEndIp,
       "msanMvrMulticastGroupRowStatus": msanMvrMulticastGroupRowStatus,
       "msanMvrConfigTable": msanMvrConfigTable,
       "msanMvrConfigEntry": msanMvrConfigEntry,
       "msanMvrConfigCVlanId": msanMvrConfigCVlanId,
       "msanMvrConfigMVlanId": msanMvrConfigMVlanId,
       "msanMvrConfigCos": msanMvrConfigCos,
       "msanMvrConfigRowStatus": msanMvrConfigRowStatus,
       "msanMvrDvlanTable": msanMvrDvlanTable,
       "msanMvrDvlanEntry": msanMvrDvlanEntry,
       "msanMvrDvlanRmOuterTagStatus": msanMvrDvlanRmOuterTagStatus,
       "msanMvrDvlanEthertypeRewriteStatus": msanMvrDvlanEthertypeRewriteStatus,
       "msanRemoteAccess": msanRemoteAccess,
       "msanRemoteAccessGlobal": msanRemoteAccessGlobal,
       "msanRemoteAccessFilterTable": msanRemoteAccessFilterTable,
       "msanRemoteAccessFilterEntry": msanRemoteAccessFilterEntry,
       "msanRemoteAccessFilterRuleIndex": msanRemoteAccessFilterRuleIndex,
       "msanRemoteAccessFilterIp": msanRemoteAccessFilterIp,
       "msanRemoteAccessFilterNetmask": msanRemoteAccessFilterNetmask,
       "msanRemoteAccessFilterAction": msanRemoteAccessFilterAction,
       "msanRemoteAccessFilterRowStatus": msanRemoteAccessFilterRowStatus,
       "msanDslSpecific": msanDslSpecific,
       "msanDslSpecificGlobal": msanDslSpecificGlobal,
       "msanDslSpecificSystemState": msanDslSpecificSystemState,
       "msanDslSpecificSystemFirmware": msanDslSpecificSystemFirmware,
       "msanDslSpecificTable": msanDslSpecificTable,
       "msanDslSpecificEntry": msanDslSpecificEntry,
       "msanDslSpecificDsPsdMask": msanDslSpecificDsPsdMask,
       "msanDslSpecificUsPsdMask": msanDslSpecificUsPsdMask,
       "msanDslSpecificLineState": msanDslSpecificLineState,
       "msanDslSpecificMaxDelayDs": msanDslSpecificMaxDelayDs,
       "msanDslSpecificMaxDelayUs": msanDslSpecificMaxDelayUs,
       "msanDslSpecificMinProtectionDs": msanDslSpecificMinProtectionDs,
       "msanDslSpecificMinProtectionUs": msanDslSpecificMinProtectionUs,
       "msanDslSpecificMaxSnrmDs": msanDslSpecificMaxSnrmDs,
       "msanDslSpecificMinSnrmDs": msanDslSpecificMinSnrmDs,
       "msanDslSpecificMaxSnrmUs": msanDslSpecificMaxSnrmUs,
       "msanDslSpecificMinSnrmUs": msanDslSpecificMinSnrmUs,
       "msanDslSpecificRaUsNrmDs": msanDslSpecificRaUsNrmDs,
       "msanDslSpecificRaUsNrmUs": msanDslSpecificRaUsNrmUs,
       "msanDslSpecificRaUsTimeDs": msanDslSpecificRaUsTimeDs,
       "msanDslSpecificRaUsTimeUs": msanDslSpecificRaUsTimeUs,
       "msanDslSpecificRaDsNrmDs": msanDslSpecificRaDsNrmDs,
       "msanDslSpecificRaDsNrmUs": msanDslSpecificRaDsNrmUs,
       "msanDslSpecificRaDsTimeDs": msanDslSpecificRaDsTimeDs,
       "msanDslSpecificRaDsTimeUs": msanDslSpecificRaDsTimeUs,
       "msanDslSpecificL0Time": msanDslSpecificL0Time,
       "msanDslSpecificL2Time": msanDslSpecificL2Time,
       "msanDslSpecificL2Atpr": msanDslSpecificL2Atpr,
       "msanDslSpecificL2Atprt": msanDslSpecificL2Atprt,
       "msanDslSpecificScMaskDs": msanDslSpecificScMaskDs,
       "msanDslSpecificScMaskUs": msanDslSpecificScMaskUs,
       "msanDslSpecificRfiBands": msanDslSpecificRfiBands,
       "msanDslSpecificMaxNomPsdDs": msanDslSpecificMaxNomPsdDs,
       "msanDslSpecificMaxNomPsdUs": msanDslSpecificMaxNomPsdUs,
       "msanDslSpecificMaxNomAtpDs": msanDslSpecificMaxNomAtpDs,
       "msanDslSpecificMaxNomAtpUs": msanDslSpecificMaxNomAtpUs,
       "msanDslSpecificMaxAggRxPwrUs": msanDslSpecificMaxAggRxPwrUs,
       "msanDslSpecificClassMask": msanDslSpecificClassMask,
       "msanDslSpecificDpboEsEL": msanDslSpecificDpboEsEL,
       "msanDslSpecificUpboKLF": msanDslSpecificUpboKLF,
       "msanDslSpecificUpboKL": msanDslSpecificUpboKL,
       "msanDslSpecificSelt": msanDslSpecificSelt,
       "msanDslSpecificSeltStatus": msanDslSpecificSeltStatus,
       "msanDslSpecificPhyRDs": msanDslSpecificPhyRDs,
       "msanDslSpecificPhyRUs": msanDslSpecificPhyRUs,
       "msanDslSpecificUpboUs1a": msanDslSpecificUpboUs1a,
       "msanDslSpecificUpboUs1b": msanDslSpecificUpboUs1b,
       "msanDslSpecificUpboUs2a": msanDslSpecificUpboUs2a,
       "msanDslSpecificUpboUs2b": msanDslSpecificUpboUs2b,
       "msanDslSpecificUpboUs3a": msanDslSpecificUpboUs3a,
       "msanDslSpecificUpboUs3b": msanDslSpecificUpboUs3b,
       "msanDslSpecificUpboUs4a": msanDslSpecificUpboUs4a,
       "msanDslSpecificUpboUs4b": msanDslSpecificUpboUs4b,
       "msanDslSpecificDpboEPsdMask": msanDslSpecificDpboEPsdMask,
       "msanDslSpecificDpboEsCmA": msanDslSpecificDpboEsCmA,
       "msanDslSpecificDpboEsCmB": msanDslSpecificDpboEsCmB,
       "msanDslSpecificDpboEsCmC": msanDslSpecificDpboEsCmC,
       "msanDslSpecificDpboMus": msanDslSpecificDpboMus,
       "msanDslSpecificDpboFMin": msanDslSpecificDpboFMin,
       "msanDslSpecificDpboFMax": msanDslSpecificDpboFMax,
       "msanDslPsdMaskDsTable": msanDslPsdMaskDsTable,
       "msanDslPsdMaskDsEntry": msanDslPsdMaskDsEntry,
       "msanDslPsdMaskDsName": msanDslPsdMaskDsName,
       "msanDslPsdMaskDsType": msanDslPsdMaskDsType,
       "msanDslPsdMaskDsShape": msanDslPsdMaskDsShape,
       "msanDslPsdMaskDsRowStatus": msanDslPsdMaskDsRowStatus,
       "msanDslPsdMaskUsTable": msanDslPsdMaskUsTable,
       "msanDslPsdMaskUsEntry": msanDslPsdMaskUsEntry,
       "msanDslPsdMaskUsName": msanDslPsdMaskUsName,
       "msanDslPsdMaskUsType": msanDslPsdMaskUsType,
       "msanDslPsdMaskUsShape": msanDslPsdMaskUsShape,
       "msanDslPsdMaskUsRowStatus": msanDslPsdMaskUsRowStatus,
       "msanDslSeltStatusTable": msanDslSeltStatusTable,
       "msanDslSeltStatusEntry": msanDslSeltStatusEntry,
       "msanDslSeltStatusNoiseType": msanDslSeltStatusNoiseType,
       "msanDslSeltStatusNoiseMrgDs": msanDslSeltStatusNoiseMrgDs,
       "msanDslSeltStatusNoiseMrgUs": msanDslSeltStatusNoiseMrgUs,
       "msanDslSeltStatusNumTonesDs": msanDslSeltStatusNumTonesDs,
       "msanDslSeltStatusNumTonesUs": msanDslSeltStatusNumTonesUs,
       "msanDslSeltStatusMaxRateDs": msanDslSeltStatusMaxRateDs,
       "msanDslSeltStatusMaxRateUs": msanDslSeltStatusMaxRateUs,
       "msanDslSeltStatusCableType": msanDslSeltStatusCableType,
       "msanDslSeltStatusCableLenght": msanDslSeltStatusCableLenght,
       "msanDslSeltStatusFitError": msanDslSeltStatusFitError,
       "msanDslSeltStatusLoopTermination": msanDslSeltStatusLoopTermination,
       "msanPortMirroring": msanPortMirroring,
       "msanPortMirroringGlobal": msanPortMirroringGlobal,
       "msanPortMirroringTable": msanPortMirroringTable,
       "msanPortMirroringEntry": msanPortMirroringEntry,
       "msanPortMirroringSessionId": msanPortMirroringSessionId,
       "msanPortMirroringAdminState": msanPortMirroringAdminState,
       "msanPortMirroringDestPort": msanPortMirroringDestPort,
       "msanPortMirroringMemberTable": msanPortMirroringMemberTable,
       "msanPortMirroringMemberEntry": msanPortMirroringMemberEntry,
       "msanPortMirroringMemberSrcPort": msanPortMirroringMemberSrcPort,
       "msanPortMirroringMemberDirection": msanPortMirroringMemberDirection,
       "msanPortMirroringMemberRowStatus": msanPortMirroringMemberRowStatus,
       "msanResetWithDelay": msanResetWithDelay,
       "msanResetWithDelayGlobal": msanResetWithDelayGlobal,
       "msanResetDelay": msanResetDelay,
       "msanMacTable": msanMacTable,
       "msanMacTableGlobal": msanMacTableGlobal,
       "msanMacTableLength": msanMacTableLength,
       "msanMacTableUsed": msanMacTableUsed,
       "msanMacTableCAMTable": msanMacTableCAMTable,
       "msanMacTableCAMEntry": msanMacTableCAMEntry,
       "msanMacTableCAMIndex": msanMacTableCAMIndex,
       "msanMacTableMacAddress": msanMacTableMacAddress,
       "msanMacTablePort": msanMacTablePort,
       "msanMacTableVLAN": msanMacTableVLAN,
       "msanMacTableType": msanMacTableType,
       "msanAcs": msanAcs,
       "msanAcsGlobal": msanAcsGlobal,
       "msanAcsServerUrl": msanAcsServerUrl,
       "msanPrimaryDnsIpAddress": msanPrimaryDnsIpAddress,
       "msanSecondaryDnsIpAddress": msanSecondaryDnsIpAddress,
       "msanAcsDomainName": msanAcsDomainName,
       "msanAcsClientStatus": msanAcsClientStatus,
       "msanAcsBackupConf": msanAcsBackupConf,
       "msanStp": msanStp,
       "msanStpGlobal": msanStpGlobal,
       "msanStpBpduFilterTable": msanStpBpduFilterTable,
       "msanStpBpduFilterEntry": msanStpBpduFilterEntry,
       "msanStpBpduFilter": msanStpBpduFilter,
       "msanStpSwitchConfigGroup": msanStpSwitchConfigGroup,
       "msanStpCstBridgePriority": msanStpCstBridgePriority,
       "msanStpMstTable": msanStpMstTable,
       "msanStpMstEntry": msanStpMstEntry,
       "msanStpMstId": msanStpMstId,
       "msanStpMstBridgePriority": msanStpMstBridgePriority,
       "msanStpMstRowStatus": msanStpMstRowStatus,
       "msanStpMstVlanTable": msanStpMstVlanTable,
       "msanStpMstVlanEntry": msanStpMstVlanEntry,
       "msanStpMstVlanRowStatus": msanStpMstVlanRowStatus,
       "msanStpMstPortTable": msanStpMstPortTable,
       "msanStpMstPortEntry": msanStpMstPortEntry,
       "msanStpMstPortPathCost": msanStpMstPortPathCost,
       "msanStpMstPortPriority": msanStpMstPortPriority,
       "msanStpPortTable": msanStpPortTable,
       "msanStpPortEntry": msanStpPortEntry,
       "msanStpPortHelloTime": msanStpPortHelloTime,
       "msanStpCstPortTable": msanStpCstPortTable,
       "msanStpCstPortEntry": msanStpCstPortEntry,
       "msanStpCstPortPathCost": msanStpCstPortPathCost,
       "msanStpCstExtPortPathCost": msanStpCstExtPortPathCost,
       "msanAuthentication": msanAuthentication,
       "msanAuthenticationGlobal": msanAuthenticationGlobal,
       "msanAuthenticationListCreate": msanAuthenticationListCreate,
       "msanAuthenticationListTable": msanAuthenticationListTable,
       "msanAuthenticationListEntry": msanAuthenticationListEntry,
       "msanAuthenticationListName": msanAuthenticationListName,
       "msanAuthenticationListMethod1": msanAuthenticationListMethod1,
       "msanAuthenticationListMethod2": msanAuthenticationListMethod2,
       "msanAuthenticationListMethod3": msanAuthenticationListMethod3,
       "msanAuthenticationListStatus": msanAuthenticationListStatus,
       "msanPortSecurity": msanPortSecurity,
       "msanPortSecurityGlobal": msanPortSecurityGlobal,
       "msanPortSecurityStatMacTable": msanPortSecurityStatMacTable,
       "msanPortSecurityStatMacEntry": msanPortSecurityStatMacEntry,
       "msanPortSecurityStatMacIf": msanPortSecurityStatMacIf,
       "msanPortSecurityStatMacVlanId": msanPortSecurityStatMacVlanId,
       "msanPortSecurityStatMacMacAddress": msanPortSecurityStatMacMacAddress,
       "msanPortSecurityStatMacRowStatus": msanPortSecurityStatMacRowStatus,
       "msanPortSecurityPortVlanTable": msanPortSecurityPortVlanTable,
       "msanPortSecurityPortVlanEntry": msanPortSecurityPortVlanEntry,
       "msanPortSecurityPortVlanDynamicLimit": msanPortSecurityPortVlanDynamicLimit,
       "msanPortSecurityPortVlanRowStatus": msanPortSecurityPortVlanRowStatus,
       "msanLag": msanLag,
       "msanLagGlobal": msanLagGlobal,
       "msanLagDetailedConfigTable": msanLagDetailedConfigTable,
       "msanLagDetailedConfigEntry": msanLagDetailedConfigEntry,
       "msanLagDetailedLagIndex": msanLagDetailedLagIndex,
       "msanLagDetailedIfIndex": msanLagDetailedIfIndex,
       "msanLagDetailedPortSpeed": msanLagDetailedPortSpeed,
       "msanLagDetailedPortStatus": msanLagDetailedPortStatus,
       "msanLagDetailedRowStatus": msanLagDetailedRowStatus,
       "msanLagTable": msanLagTable,
       "msanLagEntry": msanLagEntry,
       "msanLagIndex": msanLagIndex,
       "msanLagMaxFrameSize": msanLagMaxFrameSize,
       "msanLagDVlanTagMode": msanLagDVlanTagMode,
       "msanRadiusServer": msanRadiusServer,
       "msanRadiusServerGlobal": msanRadiusServerGlobal,
       "msanRadiusServerConfigTable": msanRadiusServerConfigTable,
       "msanRadiusServerConfigEntry": msanRadiusServerConfigEntry,
       "msanRadiusServerAddress": msanRadiusServerAddress,
       "msanRadiusServerPort": msanRadiusServerPort,
       "msanRadiusServerSecret": msanRadiusServerSecret,
       "msanRadiusServerPrimaryMode": msanRadiusServerPrimaryMode,
       "msanRadiusServerCurrentMode": msanRadiusServerCurrentMode,
       "msanRadiusServerMsgAuth": msanRadiusServerMsgAuth,
       "msanRadiusServerStatus": msanRadiusServerStatus,
       "msanNetwork": msanNetwork,
       "msanNetworkGlobal": msanNetworkGlobal,
       "msanNetworkIPAddress": msanNetworkIPAddress,
       "msanNetworkSubnetMask": msanNetworkSubnetMask,
       "msanNetworkDefaultGateway": msanNetworkDefaultGateway,
       "msanNetworkDhcpSrvIpAddr": msanNetworkDhcpSrvIpAddr,
       "msanNetworkDhcpSrvVendorSpecific": msanNetworkDhcpSrvVendorSpecific,
       "msanNetworkDhcpClientLeaseObtained": msanNetworkDhcpClientLeaseObtained,
       "msanNetworkDhcpClientLeaseExpires": msanNetworkDhcpClientLeaseExpires,
       "msanNetworkDhcpClientLocalOpt82": msanNetworkDhcpClientLocalOpt82,
       "msanNetworkDhcpClientVlanTable": msanNetworkDhcpClientVlanTable,
       "msanNetworkDhcpClientVlanEntry": msanNetworkDhcpClientVlanEntry,
       "msanNetworkDhcpClientVlanLocalOpt82": msanNetworkDhcpClientVlanLocalOpt82,
       "msanStormControl": msanStormControl,
       "msanStormControlGlobal": msanStormControlGlobal,
       "msanPortStormControlTable": msanPortStormControlTable,
       "msanPortStormControlEntry": msanPortStormControlEntry,
       "msanPortBroadcastControlMode": msanPortBroadcastControlMode,
       "msanPortBroadcastControlThreshold": msanPortBroadcastControlThreshold,
       "msanPortMulticastControlMode": msanPortMulticastControlMode,
       "msanPortMulticastControlThreshold": msanPortMulticastControlThreshold,
       "msanPortUnicastControlMode": msanPortUnicastControlMode,
       "msanPortUnicastControlThreshold": msanPortUnicastControlThreshold,
       "msanUserConfig": msanUserConfig,
       "msanUserConfigGlobal": msanUserConfigGlobal,
       "msanUserConfigCheckPassword": msanUserConfigCheckPassword,
       "msanUserConfigTable": msanUserConfigTable,
       "msanUserConfigEntry": msanUserConfigEntry,
       "msanUserIndex": msanUserIndex,
       "msanUserAccessMode": msanUserAccessMode,
       "msanSfp": msanSfp,
       "msanSfpGlobal": msanSfpGlobal,
       "msanSfpInfoTable": msanSfpInfoTable,
       "msanSfpInfoEntry": msanSfpInfoEntry,
       "msanSfpInfoState": msanSfpInfoState,
       "msanSfpInfoInterfaceType": msanSfpInfoInterfaceType,
       "msanSfpInfoNominalBitrate": msanSfpInfoNominalBitrate,
       "msanSfpInfoNominalRange": msanSfpInfoNominalRange,
       "msanSfpInfoVendor": msanSfpInfoVendor,
       "msanSfpInfoIeeeVendorId": msanSfpInfoIeeeVendorId,
       "msanSfpInfoPartNr": msanSfpInfoPartNr,
       "msanSfpInfoRevisionNr": msanSfpInfoRevisionNr,
       "msanSfpInfoSerialNr": msanSfpInfoSerialNr,
       "msanSfpInfoManufacturingDate": msanSfpInfoManufacturingDate,
       "msanSfpInfoWavelength": msanSfpInfoWavelength,
       "msanSfpDiagnosticsTable": msanSfpDiagnosticsTable,
       "msanSfpDiagnosticsEntry": msanSfpDiagnosticsEntry,
       "msanSfpDiagnosticsSignal": msanSfpDiagnosticsSignal,
       "msanSfpDiagnosticsTempCurrent": msanSfpDiagnosticsTempCurrent,
       "msanSfpDiagnosticsTempMin": msanSfpDiagnosticsTempMin,
       "msanSfpDiagnosticsTempMax": msanSfpDiagnosticsTempMax,
       "msanSfpDiagnosticsVoltageCurrent": msanSfpDiagnosticsVoltageCurrent,
       "msanSfpDiagnosticsVoltageMin": msanSfpDiagnosticsVoltageMin,
       "msanSfpDiagnosticsVoltageMax": msanSfpDiagnosticsVoltageMax,
       "msanSfpDiagnosticsTxBiasCrrCurrent": msanSfpDiagnosticsTxBiasCrrCurrent,
       "msanSfpDiagnosticsTxBiasCrrMin": msanSfpDiagnosticsTxBiasCrrMin,
       "msanSfpDiagnosticsTxBiasCrrMax": msanSfpDiagnosticsTxBiasCrrMax,
       "msanSfpDiagnosticsTxPowerCurrent": msanSfpDiagnosticsTxPowerCurrent,
       "msanSfpDiagnosticsTxPowerMin": msanSfpDiagnosticsTxPowerMin,
       "msanSfpDiagnosticsTxPowerMax": msanSfpDiagnosticsTxPowerMax,
       "msanSfpDiagnosticsRxPowerCurrent": msanSfpDiagnosticsRxPowerCurrent,
       "msanSfpDiagnosticsRxPowerMin": msanSfpDiagnosticsRxPowerMin,
       "msanSfpDiagnosticsRxPowerMax": msanSfpDiagnosticsRxPowerMax,
       "msanSfpDiagnosticsTempStatus": msanSfpDiagnosticsTempStatus,
       "msanSfpDiagnosticsVoltageStatus": msanSfpDiagnosticsVoltageStatus,
       "msanSfpDiagnosticsTxBiasStatus": msanSfpDiagnosticsTxBiasStatus,
       "msanSfpDiagnosticsTxPowerStatus": msanSfpDiagnosticsTxPowerStatus,
       "msanSfpDiagnosticsRxPowerStatus": msanSfpDiagnosticsRxPowerStatus,
       "msanMacSg": msanMacSg,
       "msanMacSgGlobal": msanMacSgGlobal,
       "msanMacSgStatus": msanMacSgStatus,
       "msanMacSgPortTable": msanMacSgPortTable,
       "msanMacSgPortEntry": msanMacSgPortEntry,
       "msanMacSgPortStatus": msanMacSgPortStatus,
       "msanMacSgPortViolationsCounter": msanMacSgPortViolationsCounter,
       "msanErrorDisable": msanErrorDisable,
       "msanErrorDisableGlobal": msanErrorDisableGlobal,
       "msanErrorDisableInterval": msanErrorDisableInterval,
       "msanErrorDisableMacSgDetectionStatus": msanErrorDisableMacSgDetectionStatus,
       "msanErrorDisableMacSgRecoveryStatus": msanErrorDisableMacSgRecoveryStatus,
       "msanErrorDisablePortTable": msanErrorDisablePortTable,
       "msanErrorDisablePortEntry": msanErrorDisablePortEntry,
       "msanErrorDisablePortStatus": msanErrorDisablePortStatus,
       "msanErrorDisablePortCause": msanErrorDisablePortCause,
       "msanErrorDisablePortTimeLeft": msanErrorDisablePortTimeLeft,
       "msanErrorDisablePortCounter": msanErrorDisablePortCounter,
       "msanAdsl": msanAdsl,
       "msanAdslGlobal": msanAdslGlobal,
       "msanAdslAtucPhysExtnTable": msanAdslAtucPhysExtnTable,
       "msanAdslAtucPhysExtnEntry": msanAdslAtucPhysExtnEntry,
       "msanAdslAtucPhysExtnOpState": msanAdslAtucPhysExtnOpState,
       "msanAdslAtucPhysExtnActualStd": msanAdslAtucPhysExtnActualStd,
       "msanAdslAtucPhysExtnBertError": msanAdslAtucPhysExtnBertError,
       "msanAdslAtucPhysExtnTxAtmCellCounter": msanAdslAtucPhysExtnTxAtmCellCounter,
       "msanAdslAtucPhysExtnRxAtmCellCounter": msanAdslAtucPhysExtnRxAtmCellCounter,
       "msanAdslAtucPhysExtnStartProgress": msanAdslAtucPhysExtnStartProgress,
       "msanAdslAtucPhysExtnIdleBertError": msanAdslAtucPhysExtnIdleBertError,
       "msanAdslAtucPhysExtnIdleBertCells": msanAdslAtucPhysExtnIdleBertCells,
       "msanAdslAtucPhysExtnBertSync": msanAdslAtucPhysExtnBertSync,
       "msanAdslAtucPhysExtnParametricTestResult": msanAdslAtucPhysExtnParametricTestResult,
       "msanAdslAtucPhysExtnSeltInfoValid": msanAdslAtucPhysExtnSeltInfoValid,
       "msanAdslAtucPhysExtnSeltLoopLen": msanAdslAtucPhysExtnSeltLoopLen,
       "msanAdslAtucPhysExtnSeltLoopEnd": msanAdslAtucPhysExtnSeltLoopEnd,
       "msanAdslAtucPhysExtnSeltLoopGauge": msanAdslAtucPhysExtnSeltLoopGauge,
       "msanAdslAtucPhysExtnSeltUpShannonCap": msanAdslAtucPhysExtnSeltUpShannonCap,
       "msanAdslAtucPhysExtnSeltDownShannonCap": msanAdslAtucPhysExtnSeltDownShannonCap,
       "msanAdslAtucPhysExtnSeltInbandNoise": msanAdslAtucPhysExtnSeltInbandNoise,
       "msanAdslAtucPhysExtnSeltTerminationResp": msanAdslAtucPhysExtnSeltTerminationResp,
       "msanAdslAtucPhysExtnSeltUpMgnAtRate": msanAdslAtucPhysExtnSeltUpMgnAtRate,
       "msanAdslAtucPhysExtnSeltDownMgnAtRate": msanAdslAtucPhysExtnSeltDownMgnAtRate,
       "msanAdslAtucPhysExtnDataBoostStatus": msanAdslAtucPhysExtnDataBoostStatus,
       "msanAdslAtucPhysExtnTestArray": msanAdslAtucPhysExtnTestArray,
       "msanAdslAtucPhysExtnChanPerfCD": msanAdslAtucPhysExtnChanPerfCD,
       "msanAdslAtucPhysExtnChanPerfBE": msanAdslAtucPhysExtnChanPerfBE,
       "msanAdslAtucPhysExtnDeltHLINSCus": msanAdslAtucPhysExtnDeltHLINSCus,
       "msanAdslAtucPhysExtnDeltHLINpsus": msanAdslAtucPhysExtnDeltHLINpsus,
       "msanAdslAtucPhysExtnDeltHLOGMTus": msanAdslAtucPhysExtnDeltHLOGMTus,
       "msanAdslAtucPhysExtnDeltHLOGpsus": msanAdslAtucPhysExtnDeltHLOGpsus,
       "msanAdslAtucPhysExtnDeltQLNMTus": msanAdslAtucPhysExtnDeltQLNMTus,
       "msanAdslAtucPhysExtnDeltQLNpsus": msanAdslAtucPhysExtnDeltQLNpsus,
       "msanAdslAtucPhysExtnDeltLastTxState": msanAdslAtucPhysExtnDeltLastTxState,
       "msanAdslAtucPhysExtnPMState": msanAdslAtucPhysExtnPMState,
       "msanAdslAtucPhysExtnChanPerfCU": msanAdslAtucPhysExtnChanPerfCU,
       "msanAdslAtucPhysExtnExtendedPsdStatus": msanAdslAtucPhysExtnExtendedPsdStatus,
       "msanAdslAtucPhysExtnChipVersion": msanAdslAtucPhysExtnChipVersion,
       "msanAdslAtucPhysExtnPilotTone": msanAdslAtucPhysExtnPilotTone,
       "msanAdslAtucMSGds": msanAdslAtucMSGds,
       "msanAdslAtucPhysExtnPsdMaskMode": msanAdslAtucPhysExtnPsdMaskMode,
       "msanAdslAtucPhysExtnDeltSNRMTus": msanAdslAtucPhysExtnDeltSNRMTus,
       "msanAdslAtucPhysExtnDeltCurrStatus": msanAdslAtucPhysExtnDeltCurrStatus,
       "msanAdslAtucSATN": msanAdslAtucSATN,
       "msanAdslAtucPhysExtnSystemVendorId": msanAdslAtucPhysExtnSystemVendorId,
       "msanAdslAtucPhysExtnSelfTestResult": msanAdslAtucPhysExtnSelfTestResult,
       "msanAdslAtucPhysExtnG9941VendorId": msanAdslAtucPhysExtnG9941VendorId,
       "msanAdslAtucPhysExtnTsspsUs": msanAdslAtucPhysExtnTsspsUs,
       "msanAdslAtucPhysExtnActPsdUs": msanAdslAtucPhysExtnActPsdUs,
       "msanAdslAtucPhysExtnGainspsUs": msanAdslAtucPhysExtnGainspsUs,
       "msanAdslAtucPhysExtnStartBin": msanAdslAtucPhysExtnStartBin,
       "msanAdslAtucPhysExtnStartupErrorCode": msanAdslAtucPhysExtnStartupErrorCode,
       "msanAdslAtucPhysExtnBitSwapCount": msanAdslAtucPhysExtnBitSwapCount,
       "msanAdslAtucPhysExtnModPhase": msanAdslAtucPhysExtnModPhase,
       "msanAdslLineExtnTable": msanAdslLineExtnTable,
       "msanAdslLineExtnEntry": msanAdslLineExtnEntry,
       "msanAdslLineExtnAction": msanAdslLineExtnAction,
       "msanAdslLineExtnUtopiaL2RxAddr": msanAdslLineExtnUtopiaL2RxAddr,
       "msanAdslLineExtnUtopiaL2TxAddr": msanAdslLineExtnUtopiaL2TxAddr,
       "msanAdslLineExtnTransAtucCap": msanAdslLineExtnTransAtucCap,
       "msanAdslLineExtnTransAtucActual": msanAdslLineExtnTransAtucActual,
       "msanAdslLineExtnClockType": msanAdslLineExtnClockType,
       "msanAdslLineExtnLineDmtTrellis": msanAdslLineExtnLineDmtTrellis,
       "msanAdslLineExtnTransAturCap": msanAdslLineExtnTransAturCap,
       "msanAdslLineExtnPMConfPMSF": msanAdslLineExtnPMConfPMSF,
       "msanAdslLineExtnDeltConfLDSF": msanAdslLineExtnDeltConfLDSF,
       "msanAdslLineExtnTransAtucConfig": msanAdslLineExtnTransAtucConfig,
       "msanAdslLineExtnAtucCurrOutputPwr": msanAdslLineExtnAtucCurrOutputPwr,
       "msanAdslLineExtnAtucBinSNRMargin": msanAdslLineExtnAtucBinSNRMargin,
       "msanAdslLineExtnUtopiaL2RxAddrSecond": msanAdslLineExtnUtopiaL2RxAddrSecond,
       "msanAdslLineExtnUtopiaL2TxAddrSecond": msanAdslLineExtnUtopiaL2TxAddrSecond,
       "msanAdslLineExtnDsBinSnrUpdate": msanAdslLineExtnDsBinSnrUpdate,
       "msanAdslLineExtnServiceType": msanAdslLineExtnServiceType,
       "msanAdslAturPhysExtnTable": msanAdslAturPhysExtnTable,
       "msanAdslAturPhysExtnEntry": msanAdslAturPhysExtnEntry,
       "msanAdslAturPhysExtnConfig": msanAdslAturPhysExtnConfig,
       "msanAdslAturPhysExtnChanPerfCD": msanAdslAturPhysExtnChanPerfCD,
       "msanAdslAturPhysExtnChanPerfCU": msanAdslAturPhysExtnChanPerfCU,
       "msanAdslAturPhysExtnChanPerfBE": msanAdslAturPhysExtnChanPerfBE,
       "msanAdslAturPhysExtnDeltHLINSCds": msanAdslAturPhysExtnDeltHLINSCds,
       "msanAdslAturPhysExtnDeltHLINpsds": msanAdslAturPhysExtnDeltHLINpsds,
       "msanAdslAturPhysExtnDeltHLOGMTds": msanAdslAturPhysExtnDeltHLOGMTds,
       "msanAdslAturPhysExtnDeltHLOGpsus": msanAdslAturPhysExtnDeltHLOGpsus,
       "msanAdslAturPhysExtnDeltQLNMTds": msanAdslAturPhysExtnDeltQLNMTds,
       "msanAdslAturPhysExtnDeltQLNpsds": msanAdslAturPhysExtnDeltQLNpsds,
       "msanAdslAturPhysExtnDeltLastTxState": msanAdslAturPhysExtnDeltLastTxState,
       "msanAdslAturMSGus": msanAdslAturMSGus,
       "msanAdslAturDeltSNRMTds": msanAdslAturDeltSNRMTds,
       "msanAdslAturSATN": msanAdslAturSATN,
       "msanAdslAturPhysExtnSystemVendorId": msanAdslAturPhysExtnSystemVendorId,
       "msanAdslAturPhysExtnGainspsDs": msanAdslAturPhysExtnGainspsDs,
       "msanAdslAturPhysExtnSelfTestResult": msanAdslAturPhysExtnSelfTestResult,
       "msanAdslAturPhysExtnG9941VendorId": msanAdslAturPhysExtnG9941VendorId,
       "msanAdslAturPhysExtnTsspsDs": msanAdslAturPhysExtnTsspsDs,
       "msanAdslAturPhysExtnActPsdDs": msanAdslAturPhysExtnActPsdDs,
       "msanAdslAturPhysExtnBitSwapCount": msanAdslAturPhysExtnBitSwapCount,
       "msanAdslAturPhysExtnPsdMaskMode": msanAdslAturPhysExtnPsdMaskMode,
       "msanEaps": msanEaps,
       "msanEapsGlobal": msanEapsGlobal,
       "msanEapsAdminState": msanEapsAdminState,
       "msanEapsDomainTable": msanEapsDomainTable,
       "msanEapsDomainEntry": msanEapsDomainEntry,
       "msanEapsDomainName": msanEapsDomainName,
       "msanEapsDomainDeviceRole": msanEapsDomainDeviceRole,
       "msanEapsDomainHelloTime": msanEapsDomainHelloTime,
       "msanEapsDomainFailTimeout": msanEapsDomainFailTimeout,
       "msanEapsDomainAdminState": msanEapsDomainAdminState,
       "msanEapsDomainPrimaryIfIndex": msanEapsDomainPrimaryIfIndex,
       "msanEapsDomainSecondaryIfIndex": msanEapsDomainSecondaryIfIndex,
       "msanEapsDomainCntrlVlanId": msanEapsDomainCntrlVlanId,
       "msanEapsDomainRowStatus": msanEapsDomainRowStatus,
       "msanEapsDomainProtVlanTable": msanEapsDomainProtVlanTable,
       "msanEapsDomainProtVlanEntry": msanEapsDomainProtVlanEntry,
       "msanEapsDomainProtVlanRowStatus": msanEapsDomainProtVlanRowStatus,
       "msanCpe": msanCpe,
       "msanCpeGlobal": msanCpeGlobal,
       "msanCpeReset": msanCpeReset,
       "msanCpeSendConfig": msanCpeSendConfig,
       "msanCpeApiMajorVersion": msanCpeApiMajorVersion,
       "msanCpeApiMinorVersion": msanCpeApiMinorVersion,
       "msanCpeTypeTable": msanCpeTypeTable,
       "msanCpeTypeEntry": msanCpeTypeEntry,
       "msanCpeTypeName": msanCpeTypeName,
       "msanCpeTypePortNum": msanCpeTypePortNum,
       "msanCpeIntfTypeTable": msanCpeIntfTypeTable,
       "msanCpeIntfTypeEntry": msanCpeIntfTypeEntry,
       "msanCpeIntfTypeRowStatus": msanCpeIntfTypeRowStatus,
       "msanCpeIntfTypeHwVersion": msanCpeIntfTypeHwVersion,
       "msanCpeIntfTypeSwVersion": msanCpeIntfTypeSwVersion,
       "msanCpeIntfPortTable": msanCpeIntfPortTable,
       "msanCpeIntfPortEntry": msanCpeIntfPortEntry,
       "msanCpeIntfPortId": msanCpeIntfPortId,
       "msanCpeIntfPortPowerMode": msanCpeIntfPortPowerMode,
       "msanCpeIntfPortLinkMode": msanCpeIntfPortLinkMode,
       "msanCpeIntfPortPvid": msanCpeIntfPortPvid,
       "msanCpeIntfPortCos": msanCpeIntfPortCos,
       "msanCpeIntfPortOverrideVid": msanCpeIntfPortOverrideVid,
       "msanCpeIntfPortOverrideCos": msanCpeIntfPortOverrideCos,
       "msanCpeIntfPortProtection": msanCpeIntfPortProtection,
       "msanCpeIntfPortStatus": msanCpeIntfPortStatus,
       "msanCpeTrafficTable": msanCpeTrafficTable,
       "msanCpeTrafficEntry": msanCpeTrafficEntry,
       "msanCpeTrafficId": msanCpeTrafficId,
       "msanCpeTrafficName": msanCpeTrafficName,
       "msanCpeTrafficSpeed": msanCpeTrafficSpeed,
       "msanCpeTrafficFlowCntrlMode": msanCpeTrafficFlowCntrlMode,
       "msanCpeTrafficRowStatus": msanCpeTrafficRowStatus,
       "msanCpeTrafficProtection": msanCpeTrafficProtection,
       "msanCpeTrafficStatus": msanCpeTrafficStatus,
       "msanCpeServiceTable": msanCpeServiceTable,
       "msanCpeServiceEntry": msanCpeServiceEntry,
       "msanCpeServiceId": msanCpeServiceId,
       "msanCpeServiceName": msanCpeServiceName,
       "msanCpeServiceCVlanId": msanCpeServiceCVlanId,
       "msanCpeServiceCCos": msanCpeServiceCCos,
       "msanCpeServiceTrafficId": msanCpeServiceTrafficId,
       "msanCpeServiceUntaggedPorts": msanCpeServiceUntaggedPorts,
       "msanCpeServiceTaggedPorts": msanCpeServiceTaggedPorts,
       "msanCpeServiceCMltcstMode": msanCpeServiceCMltcstMode,
       "msanCpeServiceRowStatus": msanCpeServiceRowStatus,
       "msanCpeServiceTypeName": msanCpeServiceTypeName,
       "msanCpeServiceProtection": msanCpeServiceProtection,
       "msanCpeServiceStatus": msanCpeServiceStatus,
       "msanCpeIntfServiceTable": msanCpeIntfServiceTable,
       "msanCpeIntfServiceEntry": msanCpeIntfServiceEntry,
       "msanCpeIntfServiceRowStatus": msanCpeIntfServiceRowStatus,
       "msanBoard": msanBoard,
       "msanBoardGlobal": msanBoardGlobal,
       "msanBoardReset": msanBoardReset,
       "msanBoardConfTable": msanBoardConfTable,
       "msanBoardConfEntry": msanBoardConfEntry,
       "msanBoardConfNr": msanBoardConfNr,
       "msanBoardConfParentNr": msanBoardConfParentNr,
       "msanBoardConfPosition": msanBoardConfPosition,
       "msanBoardConfType": msanBoardConfType,
       "msanBoardConfRequiredId": msanBoardConfRequiredId,
       "msanBoardConfActualId": msanBoardConfActualId,
       "msanBoardConfSerialNr": msanBoardConfSerialNr,
       "msanBoardConfDescription": msanBoardConfDescription,
       "msanBoardConfStatus": msanBoardConfStatus,
       "msanBoardConfRowStatus": msanBoardConfRowStatus,
       "msanBoardConfSwSteerVersion": msanBoardConfSwSteerVersion,
       "msanBoardConfSwBuildDirectory": msanBoardConfSwBuildDirectory,
       "msanBoardConfSwBuildTime": msanBoardConfSwBuildTime,
       "msanBoardConfSwBranch": msanBoardConfSwBranch,
       "msanBoardConfSwBuildReference": msanBoardConfSwBuildReference,
       "msanBoardListTable": msanBoardListTable,
       "msanBoardListEntry": msanBoardListEntry,
       "msanBoardListId": msanBoardListId,
       "msanBoardListType": msanBoardListType,
       "msanFtpServer": msanFtpServer,
       "msanFtpServerGlobal": msanFtpServerGlobal,
       "msanFtpServerAdminState": msanFtpServerAdminState,
       "msanAppRateLimit": msanAppRateLimit,
       "msanAppRateLimitGlobal": msanAppRateLimitGlobal,
       "msanAppRateLimitTable": msanAppRateLimitTable,
       "msanAppRateLimitEntry": msanAppRateLimitEntry,
       "msanAppRateLimitDhcp": msanAppRateLimitDhcp,
       "msanAppRateLimitDhcpState": msanAppRateLimitDhcpState,
       "msanAppRateLimitPppoe": msanAppRateLimitPppoe,
       "msanAppRateLimitPppoeState": msanAppRateLimitPppoeState,
       "msanAppRateLimitIgmp": msanAppRateLimitIgmp,
       "msanAppRateLimitIgmpState": msanAppRateLimitIgmpState,
       "msanAppRateLimitStp": msanAppRateLimitStp,
       "msanAppRateLimitStpState": msanAppRateLimitStpState,
       "msanAppRateLimitMn": msanAppRateLimitMn,
       "msanAppRateLimitMnState": msanAppRateLimitMnState,
       "msanMlinec": msanMlinec,
       "msanMlinecGlobal": msanMlinecGlobal,
       "msanMlinecAdminState": msanMlinecAdminState,
       "msanMulticast": msanMulticast,
       "msanMulticastGlobal": msanMulticastGlobal,
       "msanMulticastIntfStaticGroupTable": msanMulticastIntfStaticGroupTable,
       "msanMulticastIntfStaticGroupEntry": msanMulticastIntfStaticGroupEntry,
       "msanMulticastIntfStaticGroupIPAddr": msanMulticastIntfStaticGroupIPAddr,
       "msanMulticastIntfStaticGroupRowStatus": msanMulticastIntfStaticGroupRowStatus,
       "msanMulticastGroupTable": msanMulticastGroupTable,
       "msanMulticastGroupEntry": msanMulticastGroupEntry,
       "msanMulticastGroupIpAddr": msanMulticastGroupIpAddr,
       "msanMulticastGroupName": msanMulticastGroupName,
       "msanMulticastGroupRowStatus": msanMulticastGroupRowStatus,
       "msanMulticastAclListTable": msanMulticastAclListTable,
       "msanMulticastAclListEntry": msanMulticastAclListEntry,
       "msanMulticastAclListId": msanMulticastAclListId,
       "msanMulticastAclListName": msanMulticastAclListName,
       "msanMulticastAclListRowStatus": msanMulticastAclListRowStatus,
       "msanMulticastAclListGroupTable": msanMulticastAclListGroupTable,
       "msanMulticastAclListGroupEntry": msanMulticastAclListGroupEntry,
       "msanMulticastAclGroupIpAddr": msanMulticastAclGroupIpAddr,
       "msanMulticastAclListGroupRowStatus": msanMulticastAclListGroupRowStatus,
       "msanMulticastAclIntfListTable": msanMulticastAclIntfListTable,
       "msanMulticastAclIntfListEntry": msanMulticastAclIntfListEntry,
       "msanMulticastAclIntfListMode": msanMulticastAclIntfListMode,
       "msanMulticastAclIntfListRowStatus": msanMulticastAclIntfListRowStatus,
       "msanMulticastAclListVlanGroupTable": msanMulticastAclListVlanGroupTable,
       "msanMulticastAclListVlanGroupEntry": msanMulticastAclListVlanGroupEntry,
       "msanMulticastAclListVlanGroupIpAddr": msanMulticastAclListVlanGroupIpAddr,
       "msanMulticastAclListVlanGroupRowStatus": msanMulticastAclListVlanGroupRowStatus,
       "msanMulticastIntfVlanStaticGroupTable": msanMulticastIntfVlanStaticGroupTable,
       "msanMulticastIntfVlanStaticGroupEntry": msanMulticastIntfVlanStaticGroupEntry,
       "msanMulticastIntfVlanStaticGroupIpAddr": msanMulticastIntfVlanStaticGroupIpAddr,
       "msanMulticastIntfVlanStaticGroupRowStatus": msanMulticastIntfVlanStaticGroupRowStatus,
       "msanMulticastAccessListTable": msanMulticastAccessListTable,
       "msanMulticastAccessListEntry": msanMulticastAccessListEntry,
       "msanMulticastAccessListName": msanMulticastAccessListName,
       "msanMulticastAccessListRowStatus": msanMulticastAccessListRowStatus,
       "msanMulticastAccessListGroupTable": msanMulticastAccessListGroupTable,
       "msanMulticastAccessListGroupEntry": msanMulticastAccessListGroupEntry,
       "msanMulticastAccessListGroupIpAddr": msanMulticastAccessListGroupIpAddr,
       "msanMulticastAccessListGroupRowStatus": msanMulticastAccessListGroupRowStatus,
       "msanMulticastAccessListIntfTable": msanMulticastAccessListIntfTable,
       "msanMulticastAccessListIntfEntry": msanMulticastAccessListIntfEntry,
       "msanMulticastAccessListIntfMode": msanMulticastAccessListIntfMode,
       "msanMulticastAccessListIntfRowStatus": msanMulticastAccessListIntfRowStatus,
       "msanSwitchMFDBTable": msanSwitchMFDBTable,
       "msanSwitchMFDBEntry": msanSwitchMFDBEntry,
       "msanSwitchMFDBProtocolType": msanSwitchMFDBProtocolType,
       "msanSwitchMFDBVlanId": msanSwitchMFDBVlanId,
       "msanSwitchMFDBMacAddress": msanSwitchMFDBMacAddress,
       "msanSwitchMFDBType": msanSwitchMFDBType,
       "msanSwitchMFDBDescription": msanSwitchMFDBDescription,
       "msanSwitchMFDBForwardingPortMask": msanSwitchMFDBForwardingPortMask,
       "msanSwitchMFDBFilteringPortMask": msanSwitchMFDBFilteringPortMask,
       "msanFiltering": msanFiltering,
       "msanFilteringGlobal": msanFilteringGlobal,
       "msanFilteringFilterTable": msanFilteringFilterTable,
       "msanFilteringFilterEntry": msanFilteringFilterEntry,
       "msanFilteringFilterId": msanFilteringFilterId,
       "msanFilteringFilterName": msanFilteringFilterName,
       "msanFilteringFilterType": msanFilteringFilterType,
       "msanFilteringFilterRowStatus": msanFilteringFilterRowStatus,
       "msanFilteringAssignFilterTable": msanFilteringAssignFilterTable,
       "msanFilteringAssignFilterEntry": msanFilteringAssignFilterEntry,
       "msanFilteringAssignFilterVid": msanFilteringAssignFilterVid,
       "msanFilteringAssignFilterCos": msanFilteringAssignFilterCos,
       "msanFilteringAssignFilterDscp": msanFilteringAssignFilterDscp,
       "msanFilteringAssignFilterPrec": msanFilteringAssignFilterPrec,
       "msanFilteringAssignFilterRowStatus": msanFilteringAssignFilterRowStatus,
       "msanFilteringRuleTable": msanFilteringRuleTable,
       "msanFilteringRuleEntry": msanFilteringRuleEntry,
       "msanFilteringRuleId": msanFilteringRuleId,
       "msanFilteringRuleResponse": msanFilteringRuleResponse,
       "msanFilteringRuleFromMac": msanFilteringRuleFromMac,
       "msanFilteringRuleFromMacMask": msanFilteringRuleFromMacMask,
       "msanFilteringRuleFromIp": msanFilteringRuleFromIp,
       "msanFilteringRuleFromMask": msanFilteringRuleFromMask,
       "msanFilteringRuleFromPortLow": msanFilteringRuleFromPortLow,
       "msanFilteringRuleFromPortHigh": msanFilteringRuleFromPortHigh,
       "msanFilteringRuleToMac": msanFilteringRuleToMac,
       "msanFilteringRuleToMacMask": msanFilteringRuleToMacMask,
       "msanFilteringRuleToIp": msanFilteringRuleToIp,
       "msanFilteringRuleToMask": msanFilteringRuleToMask,
       "msanFilteringRuleToPortLow": msanFilteringRuleToPortLow,
       "msanFilteringRuleToPortHigh": msanFilteringRuleToPortHigh,
       "msanFilteringRuleEtherProto": msanFilteringRuleEtherProto,
       "msanFilteringRuleIpProto": msanFilteringRuleIpProto,
       "msanFilteringRuleIcmType": msanFilteringRuleIcmType,
       "msanFilteringRulePrec": msanFilteringRulePrec,
       "msanFilteringRuleTos": msanFilteringRuleTos,
       "msanFilteringRuleVid": msanFilteringRuleVid,
       "msanFilteringRuleCos": msanFilteringRuleCos,
       "msanFilteringRuleTag": msanFilteringRuleTag,
       "msanFilteringRuleRowStatus": msanFilteringRuleRowStatus,
       "msanFilteringAttachedFilterTable": msanFilteringAttachedFilterTable,
       "msanFilteringAttachedFilterEntry": msanFilteringAttachedFilterEntry,
       "msanFilteringAttachedFilterDirect": msanFilteringAttachedFilterDirect,
       "msanFilteringAttachedFilterRowStatus": msanFilteringAttachedFilterRowStatus,
       "msanBridge": msanBridge,
       "msanBridgeGlobal": msanBridgeGlobal,
       "msanBridgeMode": msanBridgeMode,
       "msanBridgeMacTableSize": msanBridgeMacTableSize,
       "msanBridgeRedAdminMode": msanBridgeRedAdminMode,
       "msanBridgeCCXTable": msanBridgeCCXTable,
       "msanBridgeCCXEntry": msanBridgeCCXEntry,
       "msanBridgeCCXInterface1": msanBridgeCCXInterface1,
       "msanBridgeCCXInterface2": msanBridgeCCXInterface2,
       "msanBridgeCCXRowStatus": msanBridgeCCXRowStatus,
       "msanIPSG": msanIPSG,
       "msanIPSGGlobal": msanIPSGGlobal,
       "msanIPSGAdminMode": msanIPSGAdminMode,
       "msanIPSGStoreAdminMode": msanIPSGStoreAdminMode,
       "msanIPSGIpv6AdminMode": msanIPSGIpv6AdminMode,
       "msanIPSGClearDynamicBinds": msanIPSGClearDynamicBinds,
       "msanIPSGIntfTable": msanIPSGIntfTable,
       "msanIPSGIntfEntry": msanIPSGIntfEntry,
       "msanIPSGIntfAdminMode": msanIPSGIntfAdminMode,
       "msanIPSGIntfBindsLimit": msanIPSGIntfBindsLimit,
       "msanIPSGIntfFilteringMode": msanIPSGIntfFilteringMode,
       "msanIPSGIntfIpv6AdminMode": msanIPSGIntfIpv6AdminMode,
       "msanIPSGIntfBindsLimitDhcpv6": msanIPSGIntfBindsLimitDhcpv6,
       "msanIPSGIntfBindsLimitND": msanIPSGIntfBindsLimitND,
       "msanIPSGIntfClearDynamicBinds": msanIPSGIntfClearDynamicBinds,
       "msanIPSGBindingsTable": msanIPSGBindingsTable,
       "msanIPSGBindingsEntry": msanIPSGBindingsEntry,
       "msanIPSGBindIp": msanIPSGBindIp,
       "msanIPSGBindVlan": msanIPSGBindVlan,
       "msanIPSGBindMac": msanIPSGBindMac,
       "msanIPSGBindLeaseRemainingTime": msanIPSGBindLeaseRemainingTime,
       "msanIPSGBindType": msanIPSGBindType,
       "msanIPSGBindMatchedFrames": msanIPSGBindMatchedFrames,
       "msanIPSGBindRowStatus": msanIPSGBindRowStatus,
       "msanIPSGIpv4PortStaticBindTable": msanIPSGIpv4PortStaticBindTable,
       "msanIPSGIpv4PortStaticBindEntry": msanIPSGIpv4PortStaticBindEntry,
       "msanIPSGIpv4PortStaticBindMacAddress": msanIPSGIpv4PortStaticBindMacAddress,
       "msanIPSGIpv4PortStaticBindVlanId": msanIPSGIpv4PortStaticBindVlanId,
       "msanIPSGIpv4PortStaticBindIpAddress": msanIPSGIpv4PortStaticBindIpAddress,
       "msanIPSGIpv4PortStaticBindMatchedFrames": msanIPSGIpv4PortStaticBindMatchedFrames,
       "msanIPSGIpv4PortStaticBindRowStatus": msanIPSGIpv4PortStaticBindRowStatus,
       "msanIPSGIpv6PortStaticBindTable": msanIPSGIpv6PortStaticBindTable,
       "msanIPSGIpv6PortStaticBindEntry": msanIPSGIpv6PortStaticBindEntry,
       "msanIPSGIpv6PortStaticBindMacAddress": msanIPSGIpv6PortStaticBindMacAddress,
       "msanIPSGIpv6PortStaticBindVlanId": msanIPSGIpv6PortStaticBindVlanId,
       "msanIPSGIpv6PortStaticBindIpAddress": msanIPSGIpv6PortStaticBindIpAddress,
       "msanIPSGIpv6PortStaticBindMatchedFrames": msanIPSGIpv6PortStaticBindMatchedFrames,
       "msanIPSGIpv6PortStaticBindRowStatus": msanIPSGIpv6PortStaticBindRowStatus,
       "msanIPSGPortBindCurrentTable": msanIPSGPortBindCurrentTable,
       "msanIPSGPortBindCurrentEntry": msanIPSGPortBindCurrentEntry,
       "msanIPSGPortBindCurrentId": msanIPSGPortBindCurrentId,
       "msanIPSGPortBindCurrentIfIndex": msanIPSGPortBindCurrentIfIndex,
       "msanIPSGPortBindCurrentMacAddress": msanIPSGPortBindCurrentMacAddress,
       "msanIPSGPortBindCurrentVlanId": msanIPSGPortBindCurrentVlanId,
       "msanIPSGPortBindCurrentIpAddressType": msanIPSGPortBindCurrentIpAddressType,
       "msanIPSGPortBindCurrentIpAddress": msanIPSGPortBindCurrentIpAddress,
       "msanIPSGPortBindCurrentLeaseRemainingTime": msanIPSGPortBindCurrentLeaseRemainingTime,
       "msanIPSGPortBindCurrentType": msanIPSGPortBindCurrentType,
       "msanIPSGPortBindCurrentMatchedFrames": msanIPSGPortBindCurrentMatchedFrames,
       "msanVlan": msanVlan,
       "msanVlanGlobal": msanVlanGlobal,
       "msanDVlanTagMode": msanDVlanTagMode,
       "msanVlanRemarkAdminState": msanVlanRemarkAdminState,
       "msanInternalVlanId": msanInternalVlanId,
       "msanPortVlanTable": msanPortVlanTable,
       "msanPortVlanEntry": msanPortVlanEntry,
       "msanPortVlanMode": msanPortVlanMode,
       "msanPortVlanStackPriority": msanPortVlanStackPriority,
       "msanPortVlanStackVlanId": msanPortVlanStackVlanId,
       "msanPortDVlanMapTable": msanPortDVlanMapTable,
       "msanPortDVlanMapEntry": msanPortDVlanMapEntry,
       "msanPortDVlanMapInTagVlanId": msanPortDVlanMapInTagVlanId,
       "msanPortDVlanMapOutTagVlanId": msanPortDVlanMapOutTagVlanId,
       "msanPortDVlanMapRowStatus": msanPortDVlanMapRowStatus,
       "msanPortVlanRemarkTable": msanPortVlanRemarkTable,
       "msanPortVlanRemarkEntry": msanPortVlanRemarkEntry,
       "msanPortVlanRemarkSrcVlanId": msanPortVlanRemarkSrcVlanId,
       "msanPortVlanRemarkDstVlanId": msanPortVlanRemarkDstVlanId,
       "msanPortVlanRemarkRowStatus": msanPortVlanRemarkRowStatus,
       "msanPortDVlanTable": msanPortDVlanTable,
       "msanPortDVlanEntry": msanPortDVlanEntry,
       "msanPortDVlanTagMode": msanPortDVlanTagMode,
       "msanPortDVlanStackVlanId": msanPortDVlanStackVlanId,
       "msanPortDVlanStackPriority": msanPortDVlanStackPriority,
       "msanPortDVlanConfigTable": msanPortDVlanConfigTable,
       "msanPortDVlanConfigEntry": msanPortDVlanConfigEntry,
       "msanDVlanConfigInTagVlanId": msanDVlanConfigInTagVlanId,
       "msanDVlanConfigInTagPriority": msanDVlanConfigInTagPriority,
       "msanDVlanConfigOutTagVlanId": msanDVlanConfigOutTagVlanId,
       "msanDVlanConfigOutTagPriority": msanDVlanConfigOutTagPriority,
       "msanDVlanConfigRowStatus": msanDVlanConfigRowStatus,
       "msanPortVlanRemarkAdminTable": msanPortVlanRemarkAdminTable,
       "msanPortVlanRemarkAdminEntry": msanPortVlanRemarkAdminEntry,
       "msanPortVlanRemarkAdminMode": msanPortVlanRemarkAdminMode,
       "msanAtm": msanAtm,
       "msanAtmGlobal": msanAtmGlobal,
       "msanPortAtmPvcTable": msanPortAtmPvcTable,
       "msanPortAtmPvcEntry": msanPortAtmPvcEntry,
       "msanPortAtmPvcVpi": msanPortAtmPvcVpi,
       "msanPortAtmPvcVci": msanPortAtmPvcVci,
       "msanPortAtmPvcPvid": msanPortAtmPvcPvid,
       "msanPortAtmPvcRowStatus": msanPortAtmPvcRowStatus,
       "msanEnergyMeter": msanEnergyMeter,
       "msanEnergyMeterGlobal": msanEnergyMeterGlobal,
       "msanEnergyMeterIpAddress": msanEnergyMeterIpAddress,
       "msanEnergyMeterTcpPort": msanEnergyMeterTcpPort,
       "msanEnergyMeterAddress": msanEnergyMeterAddress,
       "msanEnergyMeterPassword": msanEnergyMeterPassword,
       "msanEnergyMeterSerialNo": msanEnergyMeterSerialNo,
       "msanEnergyMeterDateTime": msanEnergyMeterDateTime,
       "msanEnergyMeterCurrTariff": msanEnergyMeterCurrTariff,
       "msanEnergyMeterCurrPower": msanEnergyMeterCurrPower,
       "msanEnergyMeterCoreVersion": msanEnergyMeterCoreVersion,
       "msanEnergyMeterFwType": msanEnergyMeterFwType,
       "msanEnergyMeterFwVersion": msanEnergyMeterFwVersion,
       "msanEnergyMeterFwCreationDate": msanEnergyMeterFwCreationDate,
       "msanEnergyMeterEnergyTable": msanEnergyMeterEnergyTable,
       "msanEnergyMeterEnergyEntry": msanEnergyMeterEnergyEntry,
       "msanEnergyMeterTariff": msanEnergyMeterTariff,
       "msanEnergyMeterDepth": msanEnergyMeterDepth,
       "msanEnergyMeterEnergyValue": msanEnergyMeterEnergyValue,
       "msanEnergyMeterEnergySumTable": msanEnergyMeterEnergySumTable,
       "msanEnergyMeterEnergySumEntry": msanEnergyMeterEnergySumEntry,
       "msanEnergyMeterEnergySumValue": msanEnergyMeterEnergySumValue,
       "msanArpInspection": msanArpInspection,
       "msanArpInspectionGlobal": msanArpInspectionGlobal,
       "msanArpInspectionAdminMode": msanArpInspectionAdminMode,
       "msanArpInspectionPortTable": msanArpInspectionPortTable,
       "msanArpInspectionPortEntry": msanArpInspectionPortEntry,
       "msanArpInspectionPortAdminMode": msanArpInspectionPortAdminMode,
       "msanArpInspectionPortStatDroppedFrames": msanArpInspectionPortStatDroppedFrames,
       "msanArpInspectionVlanTable": msanArpInspectionVlanTable,
       "msanArpInspectionVlanEntry": msanArpInspectionVlanEntry,
       "msanArpInspectionVlanAdminMode": msanArpInspectionVlanAdminMode,
       "msanArpInspectionVlanStatDroppedFrames": msanArpInspectionVlanStatDroppedFrames,
       "msanIsa": msanIsa,
       "msanIsaGlobal": msanIsaGlobal,
       "msanIsaTalAdminMode": msanIsaTalAdminMode,
       "msanIsaDasServerPort": msanIsaDasServerPort,
       "msanIsaDasServerSecret": msanIsaDasServerSecret,
       "msanIsaRadiusServerRetries": msanIsaRadiusServerRetries,
       "msanIsaRadiusServerTimeout": msanIsaRadiusServerTimeout,
       "msanIsaStatistics": msanIsaStatistics,
       "msanIsaPortStatTable": msanIsaPortStatTable,
       "msanIsaPortStatEntry": msanIsaPortStatEntry,
       "msanIsaPortStatTalMatchedFrames": msanIsaPortStatTalMatchedFrames,
       "msanIsaPortStatTalDroppedFrames": msanIsaPortStatTalDroppedFrames,
       "msanIsaPortStatAuthenReqSent": msanIsaPortStatAuthenReqSent,
       "msanIsaPortStatAuthenReqConfirmed": msanIsaPortStatAuthenReqConfirmed,
       "msanIsaPortStatAuthenReqRejected": msanIsaPortStatAuthenReqRejected,
       "msanIsaPortStatAuthenTimeoutExpired": msanIsaPortStatAuthenTimeoutExpired,
       "msanIsaPortStatAuthorReqSent": msanIsaPortStatAuthorReqSent,
       "msanIsaPortStatAuthorReqConfirmed": msanIsaPortStatAuthorReqConfirmed,
       "msanIsaPortStatAuthorReqRejected": msanIsaPortStatAuthorReqRejected,
       "msanIsaPortStatAuthorTimeoutExpired": msanIsaPortStatAuthorTimeoutExpired,
       "msanIsaStatLoginReq": msanIsaStatLoginReq,
       "msanIsaStatLoginUnsuccessfulReq": msanIsaStatLoginUnsuccessfulReq,
       "msanIsaRadiusServerTable": msanIsaRadiusServerTable,
       "msanIsaRadiusServerEntry": msanIsaRadiusServerEntry,
       "msanIsaRadiusServerIpAddress": msanIsaRadiusServerIpAddress,
       "msanIsaRadiusServerType": msanIsaRadiusServerType,
       "msanIsaRadiusServerPort": msanIsaRadiusServerPort,
       "msanIsaRadiusServerSecret": msanIsaRadiusServerSecret,
       "msanIsaRadiusServerPrimaryMode": msanIsaRadiusServerPrimaryMode,
       "msanIsaRadiusServerRowStatus": msanIsaRadiusServerRowStatus,
       "msanIsaPortTable": msanIsaPortTable,
       "msanIsaPortEntry": msanIsaPortEntry,
       "msanIsaPortTalAdminMode": msanIsaPortTalAdminMode,
       "msanIsaPortAuthentication": msanIsaPortAuthentication,
       "msanIsaPortAuthorization": msanIsaPortAuthorization,
       "msanIsaPortAccounting": msanIsaPortAccounting,
       "msanIsaPortLoginMask": msanIsaPortLoginMask,
       "msanIsaPortLoginUserPatternMask": msanIsaPortLoginUserPatternMask,
       "msanIsaPortTalAutomaticReq": msanIsaPortTalAutomaticReq,
       "msanIsaTalPortMatchTable": msanIsaTalPortMatchTable,
       "msanIsaTalPortMatchEntry": msanIsaTalPortMatchEntry,
       "msanIsaTalPortMatchEthertype": msanIsaTalPortMatchEthertype,
       "msanIsaTalPortMatchMacSrcAddr": msanIsaTalPortMatchMacSrcAddr,
       "msanIsaTalPortMatchMacSrcMask": msanIsaTalPortMatchMacSrcMask,
       "msanIsaTalPortMatchVlanId": msanIsaTalPortMatchVlanId,
       "msanIsaTalPortMatchIpSrcAddr": msanIsaTalPortMatchIpSrcAddr,
       "msanIsaTalPortMatchIpSrcMask": msanIsaTalPortMatchIpSrcMask,
       "msanIsaTalPortMatchDhcpType": msanIsaTalPortMatchDhcpType,
       "msanIsaTalPortMatchDhcpOpt60VendorId": msanIsaTalPortMatchDhcpOpt60VendorId,
       "msanIsaTalPortMatchDhcpOpt61ClientId": msanIsaTalPortMatchDhcpOpt61ClientId,
       "msanIsaTalPortMatchDhcpOpt61ClientIdMacAddr": msanIsaTalPortMatchDhcpOpt61ClientIdMacAddr,
       "msanIsaTalPortMatchDhcpOpt82RemoteId": msanIsaTalPortMatchDhcpOpt82RemoteId,
       "msanIsaTalPortMatchUserBits": msanIsaTalPortMatchUserBits,
       "msanIsaTalPortMatchUserMask": msanIsaTalPortMatchUserMask,
       "msanIsaTalPatternMatchTable": msanIsaTalPatternMatchTable,
       "msanIsaTalPatternMatchEntry": msanIsaTalPatternMatchEntry,
       "msanIsaTalPatternMatchName": msanIsaTalPatternMatchName,
       "msanIsaTalPatternMatchEthertype": msanIsaTalPatternMatchEthertype,
       "msanIsaTalPatternMatchMacSrcAddr": msanIsaTalPatternMatchMacSrcAddr,
       "msanIsaTalPatternMatchMacSrcMask": msanIsaTalPatternMatchMacSrcMask,
       "msanIsaTalPatternMatchVlanId": msanIsaTalPatternMatchVlanId,
       "msanIsaTalPatternMatchIpSrcAddr": msanIsaTalPatternMatchIpSrcAddr,
       "msanIsaTalPatternMatchIpSrcMask": msanIsaTalPatternMatchIpSrcMask,
       "msanIsaTalPatternMatchDhcpType": msanIsaTalPatternMatchDhcpType,
       "msanIsaTalPatternMatchDhcpOpt60VendorId": msanIsaTalPatternMatchDhcpOpt60VendorId,
       "msanIsaTalPatternMatchDhcpOpt61ClientId": msanIsaTalPatternMatchDhcpOpt61ClientId,
       "msanIsaTalPatternMatchDhcpOpt61ClientIdMacAddr": msanIsaTalPatternMatchDhcpOpt61ClientIdMacAddr,
       "msanIsaTalPatternMatchDhcpOpt82RemoteId": msanIsaTalPatternMatchDhcpOpt82RemoteId,
       "msanIsaTalPatternMatchUserBits": msanIsaTalPatternMatchUserBits,
       "msanIsaTalPatternMatchUserMask": msanIsaTalPatternMatchUserMask,
       "msanIsaTalPatternMatchLoginMask": msanIsaTalPatternMatchLoginMask,
       "msanIsaTalPatternMatchRowStatus": msanIsaTalPatternMatchRowStatus,
       "msanIsaTalPortPatternMatchTable": msanIsaTalPortPatternMatchTable,
       "msanIsaTalPortPatternMatchEntry": msanIsaTalPortPatternMatchEntry,
       "msanIsaTalPortPatternMatchRowStatus": msanIsaTalPortPatternMatchRowStatus,
       "msanSync": msanSync,
       "msanSyncGlobal": msanSyncGlobal,
       "msanSyncTable": msanSyncTable,
       "msanSyncEntry": msanSyncEntry,
       "msanSyncBoardPosition": msanSyncBoardPosition,
       "msanSyncSourcePriority": msanSyncSourcePriority,
       "msanSyncSourceType": msanSyncSourceType,
       "msanSyncSourceId": msanSyncSourceId,
       "msanSyncSourceEthPortId": msanSyncSourceEthPortId,
       "msanSyncDestinationType": msanSyncDestinationType,
       "msanSyncDestinationMlvdsId": msanSyncDestinationMlvdsId,
       "msanSyncSourceSuitability": msanSyncSourceSuitability,
       "msanSyncSourceActivity": msanSyncSourceActivity,
       "msanSyncRowStatus": msanSyncRowStatus}
)
