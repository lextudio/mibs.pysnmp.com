# SNMP MIB module (ADIC-INTELLIGENT-STORAGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ADIC-INTELLIGENT-STORAGE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:33:46 2024
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





class AdicMibVersion(DisplayString):
    """Custom type AdicMibVersion based on DisplayString"""




class AdicREDIdentifier(Counter32):
    """Custom type AdicREDIdentifier based on Counter32"""




class AdicEnable(Integer32):
    """Custom type AdicEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )





class AdicAgentStatus(Integer32):
    """Custom type AdicAgentStatus based on Integer32"""
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
        *(("critical", 5),
          ("non-critical", 4),
          ("non-recoverable", 6),
          ("ok", 3),
          ("other", 1),
          ("unknown", 2))
    )





class AdicOnlineStatus(Integer32):
    """Custom type AdicOnlineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("offline", 2),
          ("online", 1),
          ("shutdown", 3))
    )





class AdicGlobalId(OctetString):
    """Custom type AdicGlobalId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )





class AdicComponentType(Integer32):
    """Custom type AdicComponentType based on Integer32"""
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
        *(("cmb", 2),
          ("controlModule", 6),
          ("expansionModule", 7),
          ("ioBlade", 3),
          ("mcb", 1),
          ("networkChasis", 5),
          ("powerSupply", 8),
          ("rcu", 4))
    )





class AdicInterfaceType(Integer32):
    """Custom type AdicInterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fibreChannel", 2),
          ("scsi", 1))
    )





class AdicSensorStatus(Integer32):
    """Custom type AdicSensorStatus based on Integer32"""
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
        *(("alarmHigh", 5),
          ("alarmLow", 4),
          ("noData", 7),
          ("nominal", 1),
          ("notInstalled", 6),
          ("warningHigh", 3),
          ("warningLow", 2))
    )





class AdicVoltageType(Integer32):
    """Custom type AdicVoltageType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ac", 2),
          ("dc", 1))
    )





class AdicDateAndTime(OctetString):
    """Custom type AdicDateAndTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(11, 11),
    )





class AdicTrapSeverity(Integer32):
    """Custom type AdicTrapSeverity based on Integer32"""
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
        *(("alarm", 2),
          ("emergency", 1),
          ("informational", 5),
          ("notice", 4),
          ("warning", 3))
    )





class AdicDoorStatus(Integer32):
    """Custom type AdicDoorStatus based on Integer32"""
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
        *(("closed", 2),
          ("closedAndLocked", 3),
          ("closedAndUnlocked", 4),
          ("contollerFailed", 5),
          ("noData", 7),
          ("notInstalled", 6),
          ("open", 1))
    )





class AdicDriveStatus(Integer32):
    """Custom type AdicDriveStatus based on Integer32"""
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
        *(("ejecting", 3),
          ("idle", 1),
          ("inserted", 4),
          ("loading", 2),
          ("noData", 7),
          ("notInstalled", 6),
          ("removed", 5))
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
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Adic_ObjectIdentity = ObjectIdentity
adic = _Adic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3764)
)
_Storage_ObjectIdentity = ObjectIdentity
storage = _Storage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3764, 1)
)
_Intelligent_ObjectIdentity = ObjectIdentity
intelligent = _Intelligent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1)
)
_ProductAgentInfo_ObjectIdentity = ObjectIdentity
productAgentInfo = _ProductAgentInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 10)
)
_ProductMibVersion_Type = AdicMibVersion
_ProductMibVersion_Object = MibScalar
productMibVersion = _ProductMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 10, 1),
    _ProductMibVersion_Type()
)
productMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productMibVersion.setStatus("mandatory")
_ProductSnmpAgentVersion_Type = DisplayString
_ProductSnmpAgentVersion_Object = MibScalar
productSnmpAgentVersion = _ProductSnmpAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 10, 2),
    _ProductSnmpAgentVersion_Type()
)
productSnmpAgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productSnmpAgentVersion.setStatus("mandatory")
_ProductName_Type = DisplayString
_ProductName_Object = MibScalar
productName = _ProductName_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 10, 3),
    _ProductName_Type()
)
productName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productName.setStatus("mandatory")
_ProductDisplayName_Type = DisplayString
_ProductDisplayName_Object = MibScalar
productDisplayName = _ProductDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 10, 4),
    _ProductDisplayName_Type()
)
productDisplayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productDisplayName.setStatus("mandatory")
_ProductDescription_Type = DisplayString
_ProductDescription_Object = MibScalar
productDescription = _ProductDescription_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 10, 5),
    _ProductDescription_Type()
)
productDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productDescription.setStatus("mandatory")
_ProductVendor_Type = DisplayString
_ProductVendor_Object = MibScalar
productVendor = _ProductVendor_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 10, 6),
    _ProductVendor_Type()
)
productVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productVendor.setStatus("mandatory")
_ProductVersion_Type = DisplayString
_ProductVersion_Object = MibScalar
productVersion = _ProductVersion_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 10, 7),
    _ProductVersion_Type()
)
productVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productVersion.setStatus("mandatory")
_ProductDisplayVersion_Type = DisplayString
_ProductDisplayVersion_Object = MibScalar
productDisplayVersion = _ProductDisplayVersion_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 10, 8),
    _ProductDisplayVersion_Type()
)
productDisplayVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productDisplayVersion.setStatus("mandatory")


class _ProductLibraryClass_Type(Integer32):
    """Custom type productLibraryClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              10)
        )
    )
    namedValues = NamedValues(
        *(("basic", 1),
          ("intelligent", 2),
          ("virtual", 10))
    )


_ProductLibraryClass_Type.__name__ = "Integer32"
_ProductLibraryClass_Object = MibScalar
productLibraryClass = _ProductLibraryClass_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 10, 9),
    _ProductLibraryClass_Type()
)
productLibraryClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productLibraryClass.setStatus("mandatory")
_ProductSerialNumber_Type = DisplayString
_ProductSerialNumber_Object = MibScalar
productSerialNumber = _ProductSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 10, 10),
    _ProductSerialNumber_Type()
)
productSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productSerialNumber.setStatus("mandatory")
_GlobalData_ObjectIdentity = ObjectIdentity
globalData = _GlobalData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 20)
)
_AgentGlobalStatus_Type = AdicAgentStatus
_AgentGlobalStatus_Object = MibScalar
agentGlobalStatus = _AgentGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 20, 1),
    _AgentGlobalStatus_Type()
)
agentGlobalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentGlobalStatus.setStatus("mandatory")
_AgentLastGlobalStatus_Type = AdicAgentStatus
_AgentLastGlobalStatus_Object = MibScalar
agentLastGlobalStatus = _AgentLastGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 20, 2),
    _AgentLastGlobalStatus_Type()
)
agentLastGlobalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentLastGlobalStatus.setStatus("mandatory")
_AgentTimeStamp_Type = Integer32
_AgentTimeStamp_Object = MibScalar
agentTimeStamp = _AgentTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 20, 3),
    _AgentTimeStamp_Type()
)
agentTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentTimeStamp.setStatus("mandatory")
_AgentGetTimeOut_Type = Integer32
_AgentGetTimeOut_Object = MibScalar
agentGetTimeOut = _AgentGetTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 20, 4),
    _AgentGetTimeOut_Type()
)
agentGetTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentGetTimeOut.setStatus("mandatory")
_AgentModifiers_Type = Integer32
_AgentModifiers_Object = MibScalar
agentModifiers = _AgentModifiers_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 20, 5),
    _AgentModifiers_Type()
)
agentModifiers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentModifiers.setStatus("mandatory")
_AgentRefreshRate_Type = Integer32
_AgentRefreshRate_Object = MibScalar
agentRefreshRate = _AgentRefreshRate_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 20, 6),
    _AgentRefreshRate_Type()
)
agentRefreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentRefreshRate.setStatus("mandatory")
_Components_ObjectIdentity = ObjectIdentity
components = _Components_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 30)
)
_ComponentTable_Object = MibTable
componentTable = _ComponentTable_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 30, 10)
)
if mibBuilder.loadTexts:
    componentTable.setStatus("mandatory")
_ComponentEntry_Object = MibTableRow
componentEntry = _ComponentEntry_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 30, 10, 1)
)
componentEntry.setIndexNames(
    (0, "ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
)
if mibBuilder.loadTexts:
    componentEntry.setStatus("mandatory")
_ComponentId_Type = AdicGlobalId
_ComponentId_Object = MibTableColumn
componentId = _ComponentId_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 30, 10, 1, 1),
    _ComponentId_Type()
)
componentId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentId.setStatus("mandatory")
_ComponentType_Type = AdicComponentType
_ComponentType_Object = MibTableColumn
componentType = _ComponentType_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 30, 10, 1, 2),
    _ComponentType_Type()
)
componentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentType.setStatus("mandatory")


class _ComponentDisplayName_Type(DisplayString):
    """Custom type componentDisplayName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_ComponentDisplayName_Type.__name__ = "DisplayString"
_ComponentDisplayName_Object = MibTableColumn
componentDisplayName = _ComponentDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 30, 10, 1, 3),
    _ComponentDisplayName_Type()
)
componentDisplayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentDisplayName.setStatus("mandatory")
_ComponentInfo_Type = DisplayString
_ComponentInfo_Object = MibTableColumn
componentInfo = _ComponentInfo_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 30, 10, 1, 4),
    _ComponentInfo_Type()
)
componentInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    componentInfo.setStatus("mandatory")


class _ComponentLocation_Type(DisplayString):
    """Custom type componentLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_ComponentLocation_Type.__name__ = "DisplayString"
_ComponentLocation_Object = MibTableColumn
componentLocation = _ComponentLocation_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 30, 10, 1, 5),
    _ComponentLocation_Type()
)
componentLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentLocation.setStatus("mandatory")


class _ComponentVendor_Type(DisplayString):
    """Custom type componentVendor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_ComponentVendor_Type.__name__ = "DisplayString"
_ComponentVendor_Object = MibTableColumn
componentVendor = _ComponentVendor_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 30, 10, 1, 6),
    _ComponentVendor_Type()
)
componentVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentVendor.setStatus("mandatory")


class _ComponentSn_Type(DisplayString):
    """Custom type componentSn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_ComponentSn_Type.__name__ = "DisplayString"
_ComponentSn_Object = MibTableColumn
componentSn = _ComponentSn_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 30, 10, 1, 7),
    _ComponentSn_Type()
)
componentSn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentSn.setStatus("mandatory")


class _ComponentStatus_Type(Integer32):
    """Custom type componentStatus based on Integer32"""
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
        *(("failed", 5),
          ("ok", 3),
          ("unknown", 1),
          ("unused", 2),
          ("warning", 4))
    )


_ComponentStatus_Type.__name__ = "Integer32"
_ComponentStatus_Object = MibTableColumn
componentStatus = _ComponentStatus_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 30, 10, 1, 8),
    _ComponentStatus_Type()
)
componentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentStatus.setStatus("mandatory")


class _ComponentControl_Type(Integer32):
    """Custom type componentControl based on Integer32"""
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
        *(("offline", 3),
          ("online", 4),
          ("resetColdStart", 1),
          ("resetWarmStart", 2))
    )


_ComponentControl_Type.__name__ = "Integer32"
_ComponentControl_Object = MibTableColumn
componentControl = _ComponentControl_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 30, 10, 1, 9),
    _ComponentControl_Type()
)
componentControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    componentControl.setStatus("mandatory")
_ComponentREDId_Type = AdicREDIdentifier
_ComponentREDId_Object = MibTableColumn
componentREDId = _ComponentREDId_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 30, 10, 1, 10),
    _ComponentREDId_Type()
)
componentREDId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentREDId.setStatus("mandatory")
_ComponentFirmwareVersion_Type = DisplayString
_ComponentFirmwareVersion_Object = MibTableColumn
componentFirmwareVersion = _ComponentFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 30, 10, 1, 11),
    _ComponentFirmwareVersion_Type()
)
componentFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentFirmwareVersion.setStatus("mandatory")
_ComponentGeoAddrAisle_Type = Integer32
_ComponentGeoAddrAisle_Object = MibTableColumn
componentGeoAddrAisle = _ComponentGeoAddrAisle_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 30, 10, 1, 12),
    _ComponentGeoAddrAisle_Type()
)
componentGeoAddrAisle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentGeoAddrAisle.setStatus("mandatory")
_ComponentGeoAddrFrame_Type = Integer32
_ComponentGeoAddrFrame_Object = MibTableColumn
componentGeoAddrFrame = _ComponentGeoAddrFrame_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 30, 10, 1, 13),
    _ComponentGeoAddrFrame_Type()
)
componentGeoAddrFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentGeoAddrFrame.setStatus("mandatory")
_ComponentGeoAddrRack_Type = Integer32
_ComponentGeoAddrRack_Object = MibTableColumn
componentGeoAddrRack = _ComponentGeoAddrRack_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 30, 10, 1, 14),
    _ComponentGeoAddrRack_Type()
)
componentGeoAddrRack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentGeoAddrRack.setStatus("mandatory")
_ComponentGeoAddrChassis_Type = Integer32
_ComponentGeoAddrChassis_Object = MibTableColumn
componentGeoAddrChassis = _ComponentGeoAddrChassis_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 30, 10, 1, 15),
    _ComponentGeoAddrChassis_Type()
)
componentGeoAddrChassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentGeoAddrChassis.setStatus("mandatory")
_ComponentGeoAddrBlade_Type = Integer32
_ComponentGeoAddrBlade_Object = MibTableColumn
componentGeoAddrBlade = _ComponentGeoAddrBlade_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 30, 10, 1, 16),
    _ComponentGeoAddrBlade_Type()
)
componentGeoAddrBlade.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentGeoAddrBlade.setStatus("mandatory")
_ComponentIpAddress_Type = IpAddress
_ComponentIpAddress_Object = MibTableColumn
componentIpAddress = _ComponentIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 30, 10, 1, 17),
    _ComponentIpAddress_Type()
)
componentIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentIpAddress.setStatus("mandatory")
_Software_ObjectIdentity = ObjectIdentity
software = _Software_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 100)
)
_Hardware_ObjectIdentity = ObjectIdentity
hardware = _Hardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200)
)
_PowerAndCooling_ObjectIdentity = ObjectIdentity
powerAndCooling = _PowerAndCooling_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 200)
)
_PowerSupplyTable_Object = MibTable
powerSupplyTable = _PowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 200, 10)
)
if mibBuilder.loadTexts:
    powerSupplyTable.setStatus("optional")
_PowerSupplyEntry_Object = MibTableRow
powerSupplyEntry = _PowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 200, 10, 1)
)
powerSupplyEntry.setIndexNames(
    (0, "ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
    (0, "ADIC-INTELLIGENT-STORAGE-MIB", "powerSupplyIndex"),
)
if mibBuilder.loadTexts:
    powerSupplyEntry.setStatus("optional")
_PowerSupplyIndex_Type = Integer32
_PowerSupplyIndex_Object = MibTableColumn
powerSupplyIndex = _PowerSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 200, 10, 1, 1),
    _PowerSupplyIndex_Type()
)
powerSupplyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyIndex.setStatus("optional")
_PowerSupplyName_Type = DisplayString
_PowerSupplyName_Object = MibTableColumn
powerSupplyName = _PowerSupplyName_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 200, 10, 1, 2),
    _PowerSupplyName_Type()
)
powerSupplyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyName.setStatus("optional")
_PowerSupplyWattage_Type = Integer32
_PowerSupplyWattage_Object = MibTableColumn
powerSupplyWattage = _PowerSupplyWattage_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 200, 10, 1, 3),
    _PowerSupplyWattage_Type()
)
powerSupplyWattage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyWattage.setStatus("optional")
_PowerSupplyType_Type = AdicVoltageType
_PowerSupplyType_Object = MibTableColumn
powerSupplyType = _PowerSupplyType_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 200, 10, 1, 4),
    _PowerSupplyType_Type()
)
powerSupplyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyType.setStatus("optional")
_PowerSupplyREDId_Type = AdicREDIdentifier
_PowerSupplyREDId_Object = MibTableColumn
powerSupplyREDId = _PowerSupplyREDId_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 200, 10, 1, 5),
    _PowerSupplyREDId_Type()
)
powerSupplyREDId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyREDId.setStatus("optional")
_PowerSupplyRatedVoltage_Type = Integer32
_PowerSupplyRatedVoltage_Object = MibTableColumn
powerSupplyRatedVoltage = _PowerSupplyRatedVoltage_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 200, 10, 1, 6),
    _PowerSupplyRatedVoltage_Type()
)
powerSupplyRatedVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyRatedVoltage.setStatus("optional")
_PowerSupplyLocation_Type = DisplayString
_PowerSupplyLocation_Object = MibTableColumn
powerSupplyLocation = _PowerSupplyLocation_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 200, 10, 1, 7),
    _PowerSupplyLocation_Type()
)
powerSupplyLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyLocation.setStatus("optional")
_VoltageSensorTable_Object = MibTable
voltageSensorTable = _VoltageSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 200, 20)
)
if mibBuilder.loadTexts:
    voltageSensorTable.setStatus("optional")
_VoltageSensorEntry_Object = MibTableRow
voltageSensorEntry = _VoltageSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 200, 20, 1)
)
voltageSensorEntry.setIndexNames(
    (0, "ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
    (0, "ADIC-INTELLIGENT-STORAGE-MIB", "powerSupplyIndex"),
    (0, "ADIC-INTELLIGENT-STORAGE-MIB", "voltageSensorIndex"),
)
if mibBuilder.loadTexts:
    voltageSensorEntry.setStatus("optional")
_VoltageSensorIndex_Type = Integer32
_VoltageSensorIndex_Object = MibTableColumn
voltageSensorIndex = _VoltageSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 200, 20, 1, 1),
    _VoltageSensorIndex_Type()
)
voltageSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageSensorIndex.setStatus("optional")
_VoltageSensorName_Type = DisplayString
_VoltageSensorName_Object = MibTableColumn
voltageSensorName = _VoltageSensorName_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 200, 20, 1, 2),
    _VoltageSensorName_Type()
)
voltageSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageSensorName.setStatus("optional")
_VoltageSensorStatus_Type = AdicSensorStatus
_VoltageSensorStatus_Object = MibTableColumn
voltageSensorStatus = _VoltageSensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 200, 20, 1, 3),
    _VoltageSensorStatus_Type()
)
voltageSensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageSensorStatus.setStatus("optional")
_VoltageSensorMillivolts_Type = Integer32
_VoltageSensorMillivolts_Object = MibTableColumn
voltageSensorMillivolts = _VoltageSensorMillivolts_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 200, 20, 1, 4),
    _VoltageSensorMillivolts_Type()
)
voltageSensorMillivolts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageSensorMillivolts.setStatus("optional")
_VoltageSensorType_Type = AdicVoltageType
_VoltageSensorType_Object = MibTableColumn
voltageSensorType = _VoltageSensorType_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 200, 20, 1, 5),
    _VoltageSensorType_Type()
)
voltageSensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageSensorType.setStatus("optional")
_VoltageSensorNominalLo_Type = Integer32
_VoltageSensorNominalLo_Object = MibTableColumn
voltageSensorNominalLo = _VoltageSensorNominalLo_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 200, 20, 1, 6),
    _VoltageSensorNominalLo_Type()
)
voltageSensorNominalLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageSensorNominalLo.setStatus("optional")
_VoltageSensorNominalHi_Type = Integer32
_VoltageSensorNominalHi_Object = MibTableColumn
voltageSensorNominalHi = _VoltageSensorNominalHi_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 200, 20, 1, 7),
    _VoltageSensorNominalHi_Type()
)
voltageSensorNominalHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageSensorNominalHi.setStatus("optional")
_VoltageSensorWarningLo_Type = Integer32
_VoltageSensorWarningLo_Object = MibTableColumn
voltageSensorWarningLo = _VoltageSensorWarningLo_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 200, 20, 1, 8),
    _VoltageSensorWarningLo_Type()
)
voltageSensorWarningLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageSensorWarningLo.setStatus("optional")
_VoltageSensorWarningHi_Type = Integer32
_VoltageSensorWarningHi_Object = MibTableColumn
voltageSensorWarningHi = _VoltageSensorWarningHi_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 200, 20, 1, 9),
    _VoltageSensorWarningHi_Type()
)
voltageSensorWarningHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageSensorWarningHi.setStatus("optional")
_VoltageSensorLocation_Type = DisplayString
_VoltageSensorLocation_Object = MibTableColumn
voltageSensorLocation = _VoltageSensorLocation_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 200, 20, 1, 10),
    _VoltageSensorLocation_Type()
)
voltageSensorLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageSensorLocation.setStatus("optional")
_VoltageSensorREDId_Type = AdicREDIdentifier
_VoltageSensorREDId_Object = MibTableColumn
voltageSensorREDId = _VoltageSensorREDId_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 200, 20, 1, 11),
    _VoltageSensorREDId_Type()
)
voltageSensorREDId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageSensorREDId.setStatus("optional")
_TemperatureSensorTable_Object = MibTable
temperatureSensorTable = _TemperatureSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 200, 30)
)
if mibBuilder.loadTexts:
    temperatureSensorTable.setStatus("optional")
_TemperatureSensorEntry_Object = MibTableRow
temperatureSensorEntry = _TemperatureSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 200, 30, 1)
)
temperatureSensorEntry.setIndexNames(
    (0, "ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
    (0, "ADIC-INTELLIGENT-STORAGE-MIB", "temperatureSensorIndex"),
)
if mibBuilder.loadTexts:
    temperatureSensorEntry.setStatus("optional")
_TemperatureSensorIndex_Type = Integer32
_TemperatureSensorIndex_Object = MibTableColumn
temperatureSensorIndex = _TemperatureSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 200, 30, 1, 1),
    _TemperatureSensorIndex_Type()
)
temperatureSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensorIndex.setStatus("optional")
_TemperatureSensorName_Type = DisplayString
_TemperatureSensorName_Object = MibTableColumn
temperatureSensorName = _TemperatureSensorName_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 200, 30, 1, 2),
    _TemperatureSensorName_Type()
)
temperatureSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensorName.setStatus("optional")
_TemperatureSensorStatus_Type = AdicSensorStatus
_TemperatureSensorStatus_Object = MibTableColumn
temperatureSensorStatus = _TemperatureSensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 200, 30, 1, 3),
    _TemperatureSensorStatus_Type()
)
temperatureSensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensorStatus.setStatus("optional")
_TemperatureSensorDegreesCelsius_Type = Integer32
_TemperatureSensorDegreesCelsius_Object = MibTableColumn
temperatureSensorDegreesCelsius = _TemperatureSensorDegreesCelsius_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 200, 30, 1, 4),
    _TemperatureSensorDegreesCelsius_Type()
)
temperatureSensorDegreesCelsius.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensorDegreesCelsius.setStatus("optional")
_TemperatureSensorNominalLo_Type = Integer32
_TemperatureSensorNominalLo_Object = MibTableColumn
temperatureSensorNominalLo = _TemperatureSensorNominalLo_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 200, 30, 1, 5),
    _TemperatureSensorNominalLo_Type()
)
temperatureSensorNominalLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensorNominalLo.setStatus("optional")
_TemperatureSensorNominalHi_Type = Integer32
_TemperatureSensorNominalHi_Object = MibTableColumn
temperatureSensorNominalHi = _TemperatureSensorNominalHi_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 200, 30, 1, 6),
    _TemperatureSensorNominalHi_Type()
)
temperatureSensorNominalHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensorNominalHi.setStatus("optional")
_TemperatureSensorWarningLo_Type = Integer32
_TemperatureSensorWarningLo_Object = MibTableColumn
temperatureSensorWarningLo = _TemperatureSensorWarningLo_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 200, 30, 1, 7),
    _TemperatureSensorWarningLo_Type()
)
temperatureSensorWarningLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensorWarningLo.setStatus("optional")
_TemperatureSensorWarningHi_Type = Integer32
_TemperatureSensorWarningHi_Object = MibTableColumn
temperatureSensorWarningHi = _TemperatureSensorWarningHi_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 200, 30, 1, 8),
    _TemperatureSensorWarningHi_Type()
)
temperatureSensorWarningHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensorWarningHi.setStatus("optional")
_TemperatureSensorLocation_Type = DisplayString
_TemperatureSensorLocation_Object = MibTableColumn
temperatureSensorLocation = _TemperatureSensorLocation_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 200, 30, 1, 9),
    _TemperatureSensorLocation_Type()
)
temperatureSensorLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensorLocation.setStatus("optional")
_TemperatureSensorREDId_Type = AdicREDIdentifier
_TemperatureSensorREDId_Object = MibTableColumn
temperatureSensorREDId = _TemperatureSensorREDId_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 200, 30, 1, 10),
    _TemperatureSensorREDId_Type()
)
temperatureSensorREDId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensorREDId.setStatus("optional")
_CoolingFanTable_Object = MibTable
coolingFanTable = _CoolingFanTable_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 200, 40)
)
if mibBuilder.loadTexts:
    coolingFanTable.setStatus("optional")
_CoolingFanEntry_Object = MibTableRow
coolingFanEntry = _CoolingFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 200, 40, 1)
)
coolingFanEntry.setIndexNames(
    (0, "ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
    (0, "ADIC-INTELLIGENT-STORAGE-MIB", "coolingFanIndex"),
)
if mibBuilder.loadTexts:
    coolingFanEntry.setStatus("optional")
_CoolingFanIndex_Type = Integer32
_CoolingFanIndex_Object = MibTableColumn
coolingFanIndex = _CoolingFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 200, 40, 1, 1),
    _CoolingFanIndex_Type()
)
coolingFanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingFanIndex.setStatus("optional")
_CoolingFanName_Type = DisplayString
_CoolingFanName_Object = MibTableColumn
coolingFanName = _CoolingFanName_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 200, 40, 1, 2),
    _CoolingFanName_Type()
)
coolingFanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingFanName.setStatus("optional")
_CoolingFanStatus_Type = AdicSensorStatus
_CoolingFanStatus_Object = MibTableColumn
coolingFanStatus = _CoolingFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 200, 40, 1, 3),
    _CoolingFanStatus_Type()
)
coolingFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingFanStatus.setStatus("optional")
_CoolingFanRPM_Type = Integer32
_CoolingFanRPM_Object = MibTableColumn
coolingFanRPM = _CoolingFanRPM_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 200, 40, 1, 4),
    _CoolingFanRPM_Type()
)
coolingFanRPM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingFanRPM.setStatus("optional")
_CoolingFanNominalLo_Type = Integer32
_CoolingFanNominalLo_Object = MibTableColumn
coolingFanNominalLo = _CoolingFanNominalLo_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 200, 40, 1, 5),
    _CoolingFanNominalLo_Type()
)
coolingFanNominalLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingFanNominalLo.setStatus("optional")
_CoolingFanNominalHi_Type = Integer32
_CoolingFanNominalHi_Object = MibTableColumn
coolingFanNominalHi = _CoolingFanNominalHi_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 200, 40, 1, 6),
    _CoolingFanNominalHi_Type()
)
coolingFanNominalHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingFanNominalHi.setStatus("optional")
_CoolingFanWarningLo_Type = Integer32
_CoolingFanWarningLo_Object = MibTableColumn
coolingFanWarningLo = _CoolingFanWarningLo_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 200, 40, 1, 7),
    _CoolingFanWarningLo_Type()
)
coolingFanWarningLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingFanWarningLo.setStatus("optional")
_CoolingFanWarningHi_Type = Integer32
_CoolingFanWarningHi_Object = MibTableColumn
coolingFanWarningHi = _CoolingFanWarningHi_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 200, 40, 1, 8),
    _CoolingFanWarningHi_Type()
)
coolingFanWarningHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingFanWarningHi.setStatus("optional")
_CoolingFanLocation_Type = DisplayString
_CoolingFanLocation_Object = MibTableColumn
coolingFanLocation = _CoolingFanLocation_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 200, 40, 1, 9),
    _CoolingFanLocation_Type()
)
coolingFanLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingFanLocation.setStatus("optional")
_CoolingFanREDId_Type = AdicREDIdentifier
_CoolingFanREDId_Object = MibTableColumn
coolingFanREDId = _CoolingFanREDId_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 200, 200, 40, 1, 10),
    _CoolingFanREDId_Type()
)
coolingFanREDId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coolingFanREDId.setStatus("optional")
_Sml_ObjectIdentity = ObjectIdentity
sml = _Sml_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 300)
)
_Network_ObjectIdentity = ObjectIdentity
network = _Network_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 400)
)
_Notification_ObjectIdentity = ObjectIdentity
notification = _Notification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 500)
)
_TrapPayloadTable_Object = MibTable
trapPayloadTable = _TrapPayloadTable_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 500, 10)
)
if mibBuilder.loadTexts:
    trapPayloadTable.setStatus("mandatory")
_TrapPayloadEntry_Object = MibTableRow
trapPayloadEntry = _TrapPayloadEntry_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 500, 10, 1)
)
trapPayloadEntry.setIndexNames(
    (0, "ADIC-INTELLIGENT-STORAGE-MIB", "trapSequenceNumber"),
)
if mibBuilder.loadTexts:
    trapPayloadEntry.setStatus("mandatory")
_TrapSequenceNumber_Type = Integer32
_TrapSequenceNumber_Object = MibTableColumn
trapSequenceNumber = _TrapSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 500, 10, 1, 1),
    _TrapSequenceNumber_Type()
)
trapSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapSequenceNumber.setStatus("mandatory")
_TrapSeverity_Type = Integer32
_TrapSeverity_Object = MibTableColumn
trapSeverity = _TrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 500, 10, 1, 2),
    _TrapSeverity_Type()
)
trapSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapSeverity.setStatus("mandatory")
_TrapSummaryText_Type = DisplayString
_TrapSummaryText_Object = MibTableColumn
trapSummaryText = _TrapSummaryText_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 500, 10, 1, 3),
    _TrapSummaryText_Type()
)
trapSummaryText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapSummaryText.setStatus("mandatory")


class _TrapIntendedUsage_Type(Integer32):
    """Custom type trapIntendedUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("public", 1),
          ("triggerRefresh", 2))
    )


_TrapIntendedUsage_Type.__name__ = "Integer32"
_TrapIntendedUsage_Object = MibTableColumn
trapIntendedUsage = _TrapIntendedUsage_Object(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 500, 10, 1, 4),
    _TrapIntendedUsage_Type()
)
trapIntendedUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapIntendedUsage.setStatus("mandatory")

# Managed Objects groups


# Notification objects

startupSequenceComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 0, 500)
)
startupSequenceComplete.setObjects(
      *(("ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSummaryText"))
)
if mibBuilder.loadTexts:
    startupSequenceComplete.setStatus(
        ""
    )

shutdownSequenceInitiated = NotificationType(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 0, 501)
)
shutdownSequenceInitiated.setObjects(
      *(("ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "trapSummaryText"))
)
if mibBuilder.loadTexts:
    shutdownSequenceInitiated.setStatus(
        ""
    )

componentAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 0, 502)
)
componentAdded.setObjects(
      *(("ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "componentType"))
)
if mibBuilder.loadTexts:
    componentAdded.setStatus(
        ""
    )

componentRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 0, 503)
)
componentRemoved.setObjects(
      *(("ADIC-INTELLIGENT-STORAGE-MIB", "componentId"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "componentType"))
)
if mibBuilder.loadTexts:
    componentRemoved.setStatus(
        ""
    )

productLibraryClassChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 3764, 1, 1, 0, 504)
)
productLibraryClassChange.setObjects(
      *(("ADIC-INTELLIGENT-STORAGE-MIB", "productLibraryClass"),
        ("ADIC-INTELLIGENT-STORAGE-MIB", "productLibraryClass"))
)
if mibBuilder.loadTexts:
    productLibraryClassChange.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADIC-INTELLIGENT-STORAGE-MIB",
    **{"Boolean": Boolean,
       "AdicMibVersion": AdicMibVersion,
       "AdicREDIdentifier": AdicREDIdentifier,
       "AdicEnable": AdicEnable,
       "AdicAgentStatus": AdicAgentStatus,
       "AdicOnlineStatus": AdicOnlineStatus,
       "AdicGlobalId": AdicGlobalId,
       "AdicComponentType": AdicComponentType,
       "AdicInterfaceType": AdicInterfaceType,
       "AdicSensorStatus": AdicSensorStatus,
       "AdicVoltageType": AdicVoltageType,
       "AdicDateAndTime": AdicDateAndTime,
       "AdicTrapSeverity": AdicTrapSeverity,
       "AdicDoorStatus": AdicDoorStatus,
       "AdicDriveStatus": AdicDriveStatus,
       "RowStatus": RowStatus,
       "adic": adic,
       "storage": storage,
       "intelligent": intelligent,
       "startupSequenceComplete": startupSequenceComplete,
       "shutdownSequenceInitiated": shutdownSequenceInitiated,
       "componentAdded": componentAdded,
       "componentRemoved": componentRemoved,
       "productLibraryClassChange": productLibraryClassChange,
       "productAgentInfo": productAgentInfo,
       "productMibVersion": productMibVersion,
       "productSnmpAgentVersion": productSnmpAgentVersion,
       "productName": productName,
       "productDisplayName": productDisplayName,
       "productDescription": productDescription,
       "productVendor": productVendor,
       "productVersion": productVersion,
       "productDisplayVersion": productDisplayVersion,
       "productLibraryClass": productLibraryClass,
       "productSerialNumber": productSerialNumber,
       "globalData": globalData,
       "agentGlobalStatus": agentGlobalStatus,
       "agentLastGlobalStatus": agentLastGlobalStatus,
       "agentTimeStamp": agentTimeStamp,
       "agentGetTimeOut": agentGetTimeOut,
       "agentModifiers": agentModifiers,
       "agentRefreshRate": agentRefreshRate,
       "components": components,
       "componentTable": componentTable,
       "componentEntry": componentEntry,
       "componentId": componentId,
       "componentType": componentType,
       "componentDisplayName": componentDisplayName,
       "componentInfo": componentInfo,
       "componentLocation": componentLocation,
       "componentVendor": componentVendor,
       "componentSn": componentSn,
       "componentStatus": componentStatus,
       "componentControl": componentControl,
       "componentREDId": componentREDId,
       "componentFirmwareVersion": componentFirmwareVersion,
       "componentGeoAddrAisle": componentGeoAddrAisle,
       "componentGeoAddrFrame": componentGeoAddrFrame,
       "componentGeoAddrRack": componentGeoAddrRack,
       "componentGeoAddrChassis": componentGeoAddrChassis,
       "componentGeoAddrBlade": componentGeoAddrBlade,
       "componentIpAddress": componentIpAddress,
       "software": software,
       "hardware": hardware,
       "powerAndCooling": powerAndCooling,
       "powerSupplyTable": powerSupplyTable,
       "powerSupplyEntry": powerSupplyEntry,
       "powerSupplyIndex": powerSupplyIndex,
       "powerSupplyName": powerSupplyName,
       "powerSupplyWattage": powerSupplyWattage,
       "powerSupplyType": powerSupplyType,
       "powerSupplyREDId": powerSupplyREDId,
       "powerSupplyRatedVoltage": powerSupplyRatedVoltage,
       "powerSupplyLocation": powerSupplyLocation,
       "voltageSensorTable": voltageSensorTable,
       "voltageSensorEntry": voltageSensorEntry,
       "voltageSensorIndex": voltageSensorIndex,
       "voltageSensorName": voltageSensorName,
       "voltageSensorStatus": voltageSensorStatus,
       "voltageSensorMillivolts": voltageSensorMillivolts,
       "voltageSensorType": voltageSensorType,
       "voltageSensorNominalLo": voltageSensorNominalLo,
       "voltageSensorNominalHi": voltageSensorNominalHi,
       "voltageSensorWarningLo": voltageSensorWarningLo,
       "voltageSensorWarningHi": voltageSensorWarningHi,
       "voltageSensorLocation": voltageSensorLocation,
       "voltageSensorREDId": voltageSensorREDId,
       "temperatureSensorTable": temperatureSensorTable,
       "temperatureSensorEntry": temperatureSensorEntry,
       "temperatureSensorIndex": temperatureSensorIndex,
       "temperatureSensorName": temperatureSensorName,
       "temperatureSensorStatus": temperatureSensorStatus,
       "temperatureSensorDegreesCelsius": temperatureSensorDegreesCelsius,
       "temperatureSensorNominalLo": temperatureSensorNominalLo,
       "temperatureSensorNominalHi": temperatureSensorNominalHi,
       "temperatureSensorWarningLo": temperatureSensorWarningLo,
       "temperatureSensorWarningHi": temperatureSensorWarningHi,
       "temperatureSensorLocation": temperatureSensorLocation,
       "temperatureSensorREDId": temperatureSensorREDId,
       "coolingFanTable": coolingFanTable,
       "coolingFanEntry": coolingFanEntry,
       "coolingFanIndex": coolingFanIndex,
       "coolingFanName": coolingFanName,
       "coolingFanStatus": coolingFanStatus,
       "coolingFanRPM": coolingFanRPM,
       "coolingFanNominalLo": coolingFanNominalLo,
       "coolingFanNominalHi": coolingFanNominalHi,
       "coolingFanWarningLo": coolingFanWarningLo,
       "coolingFanWarningHi": coolingFanWarningHi,
       "coolingFanLocation": coolingFanLocation,
       "coolingFanREDId": coolingFanREDId,
       "sml": sml,
       "network": network,
       "notification": notification,
       "trapPayloadTable": trapPayloadTable,
       "trapPayloadEntry": trapPayloadEntry,
       "trapSequenceNumber": trapSequenceNumber,
       "trapSeverity": trapSeverity,
       "trapSummaryText": trapSummaryText,
       "trapIntendedUsage": trapIntendedUsage}
)
