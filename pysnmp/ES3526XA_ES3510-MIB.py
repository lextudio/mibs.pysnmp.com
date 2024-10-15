# SNMP MIB module (ES3526XA_ES3510-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ES3526XA_ES3510-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:40:44 2024
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

(BridgeId,
 MacAddress,
 Timeout,
 dot1dStpPort,
 dot1dStpPortEntry) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "BridgeId",
    "MacAddress",
    "Timeout",
    "dot1dStpPort",
    "dot1dStpPortEntry")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(PortList,
 VlanIndex) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanIndex")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(MacAddress,) = mibBuilder.importSymbols(
    "TOKEN-RING-RMON-MIB",
    "MacAddress")


# MODULE-IDENTITY

es3526XA_ES3510MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5)
)
es3526XA_ES3510MIB.setRevisions(
        ("2001-09-06 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class KeySegment(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )



class ValidStatus(Integer32, TextualConvention):
    status = "current"
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



class StaPathCostMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("long", 2),
          ("short", 1))
    )



# MIB Managed Objects in the order of their OIDs

_Accton_ObjectIdentity = ObjectIdentity
accton = _Accton_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259)
)
_Edgecore_ObjectIdentity = ObjectIdentity
edgecore = _Edgecore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8)
)
_CheetahSwitchMgt_ObjectIdentity = ObjectIdentity
cheetahSwitchMgt = _CheetahSwitchMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1)
)
_Es3526XA_ES3510MIBObjects_ObjectIdentity = ObjectIdentity
es3526XA_ES3510MIBObjects = _Es3526XA_ES3510MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1)
)
_SwitchMgt_ObjectIdentity = ObjectIdentity
switchMgt = _SwitchMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 1)
)


class _SwitchManagementVlan_Type(Integer32):
    """Custom type switchManagementVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4092),
    )


_SwitchManagementVlan_Type.__name__ = "Integer32"
_SwitchManagementVlan_Object = MibScalar
switchManagementVlan = _SwitchManagementVlan_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 1, 1),
    _SwitchManagementVlan_Type()
)
switchManagementVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchManagementVlan.setStatus("current")
_SwitchNumber_Type = Integer32
_SwitchNumber_Object = MibScalar
switchNumber = _SwitchNumber_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 1, 2),
    _SwitchNumber_Type()
)
switchNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchNumber.setStatus("current")
_SwitchInfoTable_Object = MibTable
switchInfoTable = _SwitchInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 1, 3)
)
if mibBuilder.loadTexts:
    switchInfoTable.setStatus("current")
_SwitchInfoEntry_Object = MibTableRow
switchInfoEntry = _SwitchInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 1, 3, 1)
)
switchInfoEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "swUnitIndex"),
)
if mibBuilder.loadTexts:
    switchInfoEntry.setStatus("current")
_SwUnitIndex_Type = Integer32
_SwUnitIndex_Object = MibTableColumn
swUnitIndex = _SwUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 1, 3, 1, 1),
    _SwUnitIndex_Type()
)
swUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swUnitIndex.setStatus("current")


class _SwHardwareVer_Type(DisplayString):
    """Custom type swHardwareVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SwHardwareVer_Type.__name__ = "DisplayString"
_SwHardwareVer_Object = MibTableColumn
swHardwareVer = _SwHardwareVer_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 1, 3, 1, 2),
    _SwHardwareVer_Type()
)
swHardwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swHardwareVer.setStatus("current")


class _SwMicrocodeVer_Type(DisplayString):
    """Custom type swMicrocodeVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SwMicrocodeVer_Type.__name__ = "DisplayString"
_SwMicrocodeVer_Object = MibTableColumn
swMicrocodeVer = _SwMicrocodeVer_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 1, 3, 1, 3),
    _SwMicrocodeVer_Type()
)
swMicrocodeVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMicrocodeVer.setStatus("current")


class _SwLoaderVer_Type(DisplayString):
    """Custom type swLoaderVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SwLoaderVer_Type.__name__ = "DisplayString"
_SwLoaderVer_Object = MibTableColumn
swLoaderVer = _SwLoaderVer_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 1, 3, 1, 4),
    _SwLoaderVer_Type()
)
swLoaderVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swLoaderVer.setStatus("current")


class _SwBootRomVer_Type(DisplayString):
    """Custom type swBootRomVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SwBootRomVer_Type.__name__ = "DisplayString"
_SwBootRomVer_Object = MibTableColumn
swBootRomVer = _SwBootRomVer_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 1, 3, 1, 5),
    _SwBootRomVer_Type()
)
swBootRomVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBootRomVer.setStatus("current")


class _SwOpCodeVer_Type(DisplayString):
    """Custom type swOpCodeVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SwOpCodeVer_Type.__name__ = "DisplayString"
_SwOpCodeVer_Object = MibTableColumn
swOpCodeVer = _SwOpCodeVer_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 1, 3, 1, 6),
    _SwOpCodeVer_Type()
)
swOpCodeVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swOpCodeVer.setStatus("current")
_SwPortNumber_Type = Integer32
_SwPortNumber_Object = MibTableColumn
swPortNumber = _SwPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 1, 3, 1, 7),
    _SwPortNumber_Type()
)
swPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortNumber.setStatus("current")


class _SwPowerStatus_Type(Integer32):
    """Custom type swPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("internalAndRedundantPower", 3),
          ("internalPower", 1),
          ("redundantPower", 2))
    )


_SwPowerStatus_Type.__name__ = "Integer32"
_SwPowerStatus_Object = MibTableColumn
swPowerStatus = _SwPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 1, 3, 1, 8),
    _SwPowerStatus_Type()
)
swPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPowerStatus.setStatus("current")


class _SwRoleInSystem_Type(Integer32):
    """Custom type swRoleInSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("backupMaster", 2),
          ("master", 1),
          ("slave", 3))
    )


_SwRoleInSystem_Type.__name__ = "Integer32"
_SwRoleInSystem_Object = MibTableColumn
swRoleInSystem = _SwRoleInSystem_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 1, 3, 1, 9),
    _SwRoleInSystem_Type()
)
swRoleInSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRoleInSystem.setStatus("current")


class _SwSerialNumber_Type(DisplayString):
    """Custom type swSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SwSerialNumber_Type.__name__ = "DisplayString"
_SwSerialNumber_Object = MibTableColumn
swSerialNumber = _SwSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 1, 3, 1, 10),
    _SwSerialNumber_Type()
)
swSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSerialNumber.setStatus("current")


class _SwServiceTag_Type(DisplayString):
    """Custom type swServiceTag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SwServiceTag_Type.__name__ = "DisplayString"
_SwServiceTag_Object = MibTableColumn
swServiceTag = _SwServiceTag_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 1, 3, 1, 13),
    _SwServiceTag_Type()
)
swServiceTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swServiceTag.setStatus("current")


class _SwitchOperState_Type(Integer32):
    """Custom type switchOperState based on Integer32"""
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
          ("noncritical", 4),
          ("nonrecoverable", 6),
          ("ok", 3),
          ("other", 1),
          ("unknown", 2))
    )


_SwitchOperState_Type.__name__ = "Integer32"
_SwitchOperState_Object = MibScalar
switchOperState = _SwitchOperState_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 1, 4),
    _SwitchOperState_Type()
)
switchOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchOperState.setStatus("current")
_SwitchProductId_ObjectIdentity = ObjectIdentity
switchProductId = _SwitchProductId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 1, 5)
)


class _SwProdName_Type(DisplayString):
    """Custom type swProdName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_SwProdName_Type.__name__ = "DisplayString"
_SwProdName_Object = MibScalar
swProdName = _SwProdName_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 1, 5, 1),
    _SwProdName_Type()
)
swProdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swProdName.setStatus("current")


class _SwProdManufacturer_Type(DisplayString):
    """Custom type swProdManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_SwProdManufacturer_Type.__name__ = "DisplayString"
_SwProdManufacturer_Object = MibScalar
swProdManufacturer = _SwProdManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 1, 5, 2),
    _SwProdManufacturer_Type()
)
swProdManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swProdManufacturer.setStatus("current")


class _SwProdDescription_Type(DisplayString):
    """Custom type swProdDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_SwProdDescription_Type.__name__ = "DisplayString"
_SwProdDescription_Object = MibScalar
swProdDescription = _SwProdDescription_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 1, 5, 3),
    _SwProdDescription_Type()
)
swProdDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swProdDescription.setStatus("current")


class _SwProdVersion_Type(DisplayString):
    """Custom type swProdVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_SwProdVersion_Type.__name__ = "DisplayString"
_SwProdVersion_Object = MibScalar
swProdVersion = _SwProdVersion_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 1, 5, 4),
    _SwProdVersion_Type()
)
swProdVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swProdVersion.setStatus("current")


class _SwProdUrl_Type(DisplayString):
    """Custom type swProdUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_SwProdUrl_Type.__name__ = "DisplayString"
_SwProdUrl_Object = MibScalar
swProdUrl = _SwProdUrl_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 1, 5, 5),
    _SwProdUrl_Type()
)
swProdUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swProdUrl.setStatus("current")
_SwIdentifier_Type = Integer32
_SwIdentifier_Object = MibScalar
swIdentifier = _SwIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 1, 5, 6),
    _SwIdentifier_Type()
)
swIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIdentifier.setStatus("current")


class _SwChassisServiceTag_Type(DisplayString):
    """Custom type swChassisServiceTag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SwChassisServiceTag_Type.__name__ = "DisplayString"
_SwChassisServiceTag_Object = MibScalar
swChassisServiceTag = _SwChassisServiceTag_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 1, 5, 7),
    _SwChassisServiceTag_Type()
)
swChassisServiceTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swChassisServiceTag.setStatus("current")
_AmtrMgt_ObjectIdentity = ObjectIdentity
amtrMgt = _AmtrMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 1, 8)
)
_AmtrMacAddrAgingStatus_Type = EnabledStatus
_AmtrMacAddrAgingStatus_Object = MibScalar
amtrMacAddrAgingStatus = _AmtrMacAddrAgingStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 1, 8, 3),
    _AmtrMacAddrAgingStatus_Type()
)
amtrMacAddrAgingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    amtrMacAddrAgingStatus.setStatus("current")
_AmtrMacAddrDelete_Type = EnabledStatus
_AmtrMacAddrDelete_Object = MibScalar
amtrMacAddrDelete = _AmtrMacAddrDelete_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 1, 8, 4),
    _AmtrMacAddrDelete_Type()
)
amtrMacAddrDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    amtrMacAddrDelete.setStatus("current")
_PortMgt_ObjectIdentity = ObjectIdentity
portMgt = _PortMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 2)
)
_PortTable_Object = MibTable
portTable = _PortTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 2, 1)
)
if mibBuilder.loadTexts:
    portTable.setStatus("current")
_PortEntry_Object = MibTableRow
portEntry = _PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 2, 1, 1)
)
portEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    portEntry.setStatus("current")
_PortIndex_Type = Integer32
_PortIndex_Object = MibTableColumn
portIndex = _PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 2, 1, 1, 1),
    _PortIndex_Type()
)
portIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portIndex.setStatus("current")


class _PortName_Type(DisplayString):
    """Custom type portName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_PortName_Type.__name__ = "DisplayString"
_PortName_Object = MibTableColumn
portName = _PortName_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 2, 1, 1, 2),
    _PortName_Type()
)
portName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portName.setStatus("current")


class _PortType_Type(Integer32):
    """Custom type portType based on Integer32"""
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
        *(("hundredBaseFX", 3),
          ("hundredBaseFxScMultiMode", 10),
          ("hundredBaseFxScSingleMode", 9),
          ("hundredBaseTX", 2),
          ("other", 1),
          ("thousandBaseGBIC", 7),
          ("thousandBaseLX", 5),
          ("thousandBaseSX", 4),
          ("thousandBaseSfp", 8),
          ("thousandBaseT", 6))
    )


_PortType_Type.__name__ = "Integer32"
_PortType_Object = MibTableColumn
portType = _PortType_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 2, 1, 1, 3),
    _PortType_Type()
)
portType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portType.setStatus("current")


class _PortSpeedDpxCfg_Type(Integer32):
    """Custom type portSpeedDpxCfg based on Integer32"""
    defaultValue = 2

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
        *(("fullDuplex10", 3),
          ("fullDuplex100", 5),
          ("fullDuplex1000", 7),
          ("halfDuplex10", 2),
          ("halfDuplex100", 4),
          ("halfDuplex1000", 6),
          ("reserved", 1))
    )


_PortSpeedDpxCfg_Type.__name__ = "Integer32"
_PortSpeedDpxCfg_Object = MibTableColumn
portSpeedDpxCfg = _PortSpeedDpxCfg_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 2, 1, 1, 4),
    _PortSpeedDpxCfg_Type()
)
portSpeedDpxCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSpeedDpxCfg.setStatus("current")


class _PortFlowCtrlCfg_Type(Integer32):
    """Custom type portFlowCtrlCfg based on Integer32"""
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
        *(("backPressure", 3),
          ("disabled", 2),
          ("dot3xFlowControl", 4),
          ("enabled", 1))
    )


_PortFlowCtrlCfg_Type.__name__ = "Integer32"
_PortFlowCtrlCfg_Object = MibTableColumn
portFlowCtrlCfg = _PortFlowCtrlCfg_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 2, 1, 1, 5),
    _PortFlowCtrlCfg_Type()
)
portFlowCtrlCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portFlowCtrlCfg.setStatus("current")


class _PortCapabilities_Type(Bits):
    """Custom type portCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("portCap1000full", 5),
          ("portCap1000half", 4),
          ("portCap100full", 3),
          ("portCap100half", 2),
          ("portCap10full", 1),
          ("portCap10half", 0),
          ("portCapFlowCtrl", 15),
          ("portCapSym", 14),
          ("reserved10", 10),
          ("reserved11", 11),
          ("reserved12", 12),
          ("reserved13", 13),
          ("reserved6", 6),
          ("reserved7", 7),
          ("reserved8", 8),
          ("reserved9", 9))
    )

_PortCapabilities_Type.__name__ = "Bits"
_PortCapabilities_Object = MibTableColumn
portCapabilities = _PortCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 2, 1, 1, 6),
    _PortCapabilities_Type()
)
portCapabilities.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portCapabilities.setStatus("current")


class _PortAutonegotiation_Type(Integer32):
    """Custom type portAutonegotiation based on Integer32"""
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


_PortAutonegotiation_Type.__name__ = "Integer32"
_PortAutonegotiation_Object = MibTableColumn
portAutonegotiation = _PortAutonegotiation_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 2, 1, 1, 7),
    _PortAutonegotiation_Type()
)
portAutonegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portAutonegotiation.setStatus("current")


class _PortSpeedDpxStatus_Type(Integer32):
    """Custom type portSpeedDpxStatus based on Integer32"""
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
        *(("error", 1),
          ("fullDuplex10", 3),
          ("fullDuplex100", 5),
          ("fullDuplex1000", 7),
          ("halfDuplex10", 2),
          ("halfDuplex100", 4),
          ("halfDuplex1000", 6))
    )


_PortSpeedDpxStatus_Type.__name__ = "Integer32"
_PortSpeedDpxStatus_Object = MibTableColumn
portSpeedDpxStatus = _PortSpeedDpxStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 2, 1, 1, 8),
    _PortSpeedDpxStatus_Type()
)
portSpeedDpxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSpeedDpxStatus.setStatus("current")


class _PortFlowCtrlStatus_Type(Integer32):
    """Custom type portFlowCtrlStatus based on Integer32"""
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
        *(("backPressure", 2),
          ("dot3xFlowControl", 3),
          ("error", 1),
          ("none", 4))
    )


_PortFlowCtrlStatus_Type.__name__ = "Integer32"
_PortFlowCtrlStatus_Object = MibTableColumn
portFlowCtrlStatus = _PortFlowCtrlStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 2, 1, 1, 9),
    _PortFlowCtrlStatus_Type()
)
portFlowCtrlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portFlowCtrlStatus.setStatus("current")
_PortTrunkIndex_Type = Integer32
_PortTrunkIndex_Object = MibTableColumn
portTrunkIndex = _PortTrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 2, 1, 1, 10),
    _PortTrunkIndex_Type()
)
portTrunkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTrunkIndex.setStatus("current")
_TrunkMgt_ObjectIdentity = ObjectIdentity
trunkMgt = _TrunkMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 3)
)
_TrunkMaxId_Type = Integer32
_TrunkMaxId_Object = MibScalar
trunkMaxId = _TrunkMaxId_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 3, 1),
    _TrunkMaxId_Type()
)
trunkMaxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkMaxId.setStatus("current")
_TrunkValidNumber_Type = Integer32
_TrunkValidNumber_Object = MibScalar
trunkValidNumber = _TrunkValidNumber_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 3, 2),
    _TrunkValidNumber_Type()
)
trunkValidNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkValidNumber.setStatus("current")
_TrunkTable_Object = MibTable
trunkTable = _TrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 3, 3)
)
if mibBuilder.loadTexts:
    trunkTable.setStatus("current")
_TrunkEntry_Object = MibTableRow
trunkEntry = _TrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 3, 3, 1)
)
trunkEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "trunkIndex"),
)
if mibBuilder.loadTexts:
    trunkEntry.setStatus("current")
_TrunkIndex_Type = Integer32
_TrunkIndex_Object = MibTableColumn
trunkIndex = _TrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 3, 3, 1, 1),
    _TrunkIndex_Type()
)
trunkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trunkIndex.setStatus("current")
_TrunkPorts_Type = PortList
_TrunkPorts_Object = MibTableColumn
trunkPorts = _TrunkPorts_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 3, 3, 1, 2),
    _TrunkPorts_Type()
)
trunkPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trunkPorts.setStatus("current")


class _TrunkCreation_Type(Integer32):
    """Custom type trunkCreation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lacp", 2),
          ("static", 1))
    )


_TrunkCreation_Type.__name__ = "Integer32"
_TrunkCreation_Object = MibTableColumn
trunkCreation = _TrunkCreation_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 3, 3, 1, 3),
    _TrunkCreation_Type()
)
trunkCreation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkCreation.setStatus("current")
_TrunkStatus_Type = ValidStatus
_TrunkStatus_Object = MibTableColumn
trunkStatus = _TrunkStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 3, 3, 1, 4),
    _TrunkStatus_Type()
)
trunkStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trunkStatus.setStatus("current")
_LacpMgt_ObjectIdentity = ObjectIdentity
lacpMgt = _LacpMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 4)
)
_LacpPortTable_Object = MibTable
lacpPortTable = _LacpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 4, 1)
)
if mibBuilder.loadTexts:
    lacpPortTable.setStatus("current")
_LacpPortEntry_Object = MibTableRow
lacpPortEntry = _LacpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 4, 1, 1)
)
lacpPortEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "lacpPortIndex"),
)
if mibBuilder.loadTexts:
    lacpPortEntry.setStatus("current")
_LacpPortIndex_Type = Integer32
_LacpPortIndex_Object = MibTableColumn
lacpPortIndex = _LacpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 4, 1, 1, 1),
    _LacpPortIndex_Type()
)
lacpPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lacpPortIndex.setStatus("current")


class _LacpPortStatus_Type(Integer32):
    """Custom type lacpPortStatus based on Integer32"""
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


_LacpPortStatus_Type.__name__ = "Integer32"
_LacpPortStatus_Object = MibTableColumn
lacpPortStatus = _LacpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 4, 1, 1, 2),
    _LacpPortStatus_Type()
)
lacpPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lacpPortStatus.setStatus("current")
_StaMgt_ObjectIdentity = ObjectIdentity
staMgt = _StaMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5)
)


class _StaSystemStatus_Type(EnabledStatus):
    """Custom type staSystemStatus based on EnabledStatus"""


_StaSystemStatus_Object = MibScalar
staSystemStatus = _StaSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 1),
    _StaSystemStatus_Type()
)
staSystemStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staSystemStatus.setStatus("current")
_StaPortTable_Object = MibTable
staPortTable = _StaPortTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 2)
)
if mibBuilder.loadTexts:
    staPortTable.setStatus("current")
_StaPortEntry_Object = MibTableRow
staPortEntry = _StaPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 2, 1)
)
staPortEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "staPortIndex"),
)
if mibBuilder.loadTexts:
    staPortEntry.setStatus("current")
_StaPortIndex_Type = Integer32
_StaPortIndex_Object = MibTableColumn
staPortIndex = _StaPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 2, 1, 1),
    _StaPortIndex_Type()
)
staPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    staPortIndex.setStatus("current")
_StaPortFastForward_Type = EnabledStatus
_StaPortFastForward_Object = MibTableColumn
staPortFastForward = _StaPortFastForward_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 2, 1, 2),
    _StaPortFastForward_Type()
)
staPortFastForward.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staPortFastForward.setStatus("current")
_StaPortProtocolMigration_Type = TruthValue
_StaPortProtocolMigration_Object = MibTableColumn
staPortProtocolMigration = _StaPortProtocolMigration_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 2, 1, 3),
    _StaPortProtocolMigration_Type()
)
staPortProtocolMigration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staPortProtocolMigration.setStatus("current")
_StaPortAdminEdgePort_Type = TruthValue
_StaPortAdminEdgePort_Object = MibTableColumn
staPortAdminEdgePort = _StaPortAdminEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 2, 1, 4),
    _StaPortAdminEdgePort_Type()
)
staPortAdminEdgePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staPortAdminEdgePort.setStatus("current")
_StaPortOperEdgePort_Type = TruthValue
_StaPortOperEdgePort_Object = MibTableColumn
staPortOperEdgePort = _StaPortOperEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 2, 1, 5),
    _StaPortOperEdgePort_Type()
)
staPortOperEdgePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPortOperEdgePort.setStatus("current")


class _StaPortAdminPointToPoint_Type(Integer32):
    """Custom type staPortAdminPointToPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("forceFalse", 1),
          ("forceTrue", 0))
    )


_StaPortAdminPointToPoint_Type.__name__ = "Integer32"
_StaPortAdminPointToPoint_Object = MibTableColumn
staPortAdminPointToPoint = _StaPortAdminPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 2, 1, 6),
    _StaPortAdminPointToPoint_Type()
)
staPortAdminPointToPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staPortAdminPointToPoint.setStatus("current")
_StaPortOperPointToPoint_Type = TruthValue
_StaPortOperPointToPoint_Object = MibTableColumn
staPortOperPointToPoint = _StaPortOperPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 2, 1, 7),
    _StaPortOperPointToPoint_Type()
)
staPortOperPointToPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPortOperPointToPoint.setStatus("current")


class _StaPortLongPathCost_Type(Integer32):
    """Custom type staPortLongPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_StaPortLongPathCost_Type.__name__ = "Integer32"
_StaPortLongPathCost_Object = MibTableColumn
staPortLongPathCost = _StaPortLongPathCost_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 2, 1, 8),
    _StaPortLongPathCost_Type()
)
staPortLongPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staPortLongPathCost.setStatus("current")


class _StaPortSystemStatus_Type(EnabledStatus):
    """Custom type staPortSystemStatus based on EnabledStatus"""


_StaPortSystemStatus_Object = MibTableColumn
staPortSystemStatus = _StaPortSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 2, 1, 9),
    _StaPortSystemStatus_Type()
)
staPortSystemStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staPortSystemStatus.setStatus("current")


class _StaProtocolType_Type(Integer32):
    """Custom type staProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mstp", 3),
          ("rstp", 2),
          ("stp", 1))
    )


_StaProtocolType_Type.__name__ = "Integer32"
_StaProtocolType_Object = MibScalar
staProtocolType = _StaProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 3),
    _StaProtocolType_Type()
)
staProtocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staProtocolType.setStatus("current")


class _StaTxHoldCount_Type(Integer32):
    """Custom type staTxHoldCount based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_StaTxHoldCount_Type.__name__ = "Integer32"
_StaTxHoldCount_Object = MibScalar
staTxHoldCount = _StaTxHoldCount_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 4),
    _StaTxHoldCount_Type()
)
staTxHoldCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staTxHoldCount.setStatus("current")


class _StaPathCostMethod_Type(StaPathCostMode):
    """Custom type staPathCostMethod based on StaPathCostMode"""


_StaPathCostMethod_Object = MibScalar
staPathCostMethod = _StaPathCostMethod_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 5),
    _StaPathCostMethod_Type()
)
staPathCostMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staPathCostMethod.setStatus("current")
_XstMgt_ObjectIdentity = ObjectIdentity
xstMgt = _XstMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 6)
)


class _MstName_Type(DisplayString):
    """Custom type mstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MstName_Type.__name__ = "DisplayString"
_MstName_Object = MibScalar
mstName = _MstName_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 6, 1),
    _MstName_Type()
)
mstName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstName.setStatus("current")
_MstRevision_Type = Integer32
_MstRevision_Object = MibScalar
mstRevision = _MstRevision_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 6, 2),
    _MstRevision_Type()
)
mstRevision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstRevision.setStatus("current")


class _MstMaxHops_Type(Integer32):
    """Custom type mstMaxHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_MstMaxHops_Type.__name__ = "Integer32"
_MstMaxHops_Object = MibScalar
mstMaxHops = _MstMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 6, 3),
    _MstMaxHops_Type()
)
mstMaxHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstMaxHops.setStatus("current")
_XstInstanceCfgTable_Object = MibTable
xstInstanceCfgTable = _XstInstanceCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 6, 4)
)
if mibBuilder.loadTexts:
    xstInstanceCfgTable.setStatus("current")
_XstInstanceCfgEntry_Object = MibTableRow
xstInstanceCfgEntry = _XstInstanceCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 6, 4, 1)
)
xstInstanceCfgEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "xstInstanceCfgIndex"),
)
if mibBuilder.loadTexts:
    xstInstanceCfgEntry.setStatus("current")


class _XstInstanceCfgIndex_Type(Integer32):
    """Custom type xstInstanceCfgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_XstInstanceCfgIndex_Type.__name__ = "Integer32"
_XstInstanceCfgIndex_Object = MibTableColumn
xstInstanceCfgIndex = _XstInstanceCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 6, 4, 1, 1),
    _XstInstanceCfgIndex_Type()
)
xstInstanceCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xstInstanceCfgIndex.setStatus("current")


class _XstInstanceCfgPriority_Type(Integer32):
    """Custom type xstInstanceCfgPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_XstInstanceCfgPriority_Type.__name__ = "Integer32"
_XstInstanceCfgPriority_Object = MibTableColumn
xstInstanceCfgPriority = _XstInstanceCfgPriority_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 6, 4, 1, 2),
    _XstInstanceCfgPriority_Type()
)
xstInstanceCfgPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xstInstanceCfgPriority.setStatus("current")
_XstInstanceCfgTimeSinceTopologyChange_Type = TimeTicks
_XstInstanceCfgTimeSinceTopologyChange_Object = MibTableColumn
xstInstanceCfgTimeSinceTopologyChange = _XstInstanceCfgTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 6, 4, 1, 3),
    _XstInstanceCfgTimeSinceTopologyChange_Type()
)
xstInstanceCfgTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgTimeSinceTopologyChange.setStatus("current")
_XstInstanceCfgTopChanges_Type = Integer32
_XstInstanceCfgTopChanges_Object = MibTableColumn
xstInstanceCfgTopChanges = _XstInstanceCfgTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 6, 4, 1, 4),
    _XstInstanceCfgTopChanges_Type()
)
xstInstanceCfgTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgTopChanges.setStatus("current")
_XstInstanceCfgDesignatedRoot_Type = BridgeId
_XstInstanceCfgDesignatedRoot_Object = MibTableColumn
xstInstanceCfgDesignatedRoot = _XstInstanceCfgDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 6, 4, 1, 5),
    _XstInstanceCfgDesignatedRoot_Type()
)
xstInstanceCfgDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgDesignatedRoot.setStatus("current")
_XstInstanceCfgRootCost_Type = Integer32
_XstInstanceCfgRootCost_Object = MibTableColumn
xstInstanceCfgRootCost = _XstInstanceCfgRootCost_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 6, 4, 1, 6),
    _XstInstanceCfgRootCost_Type()
)
xstInstanceCfgRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgRootCost.setStatus("current")
_XstInstanceCfgRootPort_Type = Integer32
_XstInstanceCfgRootPort_Object = MibTableColumn
xstInstanceCfgRootPort = _XstInstanceCfgRootPort_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 6, 4, 1, 7),
    _XstInstanceCfgRootPort_Type()
)
xstInstanceCfgRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgRootPort.setStatus("current")
_XstInstanceCfgMaxAge_Type = Timeout
_XstInstanceCfgMaxAge_Object = MibTableColumn
xstInstanceCfgMaxAge = _XstInstanceCfgMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 6, 4, 1, 8),
    _XstInstanceCfgMaxAge_Type()
)
xstInstanceCfgMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgMaxAge.setStatus("current")
_XstInstanceCfgHelloTime_Type = Timeout
_XstInstanceCfgHelloTime_Object = MibTableColumn
xstInstanceCfgHelloTime = _XstInstanceCfgHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 6, 4, 1, 9),
    _XstInstanceCfgHelloTime_Type()
)
xstInstanceCfgHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgHelloTime.setStatus("current")
_XstInstanceCfgHoldTime_Type = Timeout
_XstInstanceCfgHoldTime_Object = MibTableColumn
xstInstanceCfgHoldTime = _XstInstanceCfgHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 6, 4, 1, 10),
    _XstInstanceCfgHoldTime_Type()
)
xstInstanceCfgHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgHoldTime.setStatus("current")
_XstInstanceCfgForwardDelay_Type = Timeout
_XstInstanceCfgForwardDelay_Object = MibTableColumn
xstInstanceCfgForwardDelay = _XstInstanceCfgForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 6, 4, 1, 11),
    _XstInstanceCfgForwardDelay_Type()
)
xstInstanceCfgForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgForwardDelay.setStatus("current")
_XstInstanceCfgBridgeMaxAge_Type = Timeout
_XstInstanceCfgBridgeMaxAge_Object = MibTableColumn
xstInstanceCfgBridgeMaxAge = _XstInstanceCfgBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 6, 4, 1, 12),
    _XstInstanceCfgBridgeMaxAge_Type()
)
xstInstanceCfgBridgeMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgBridgeMaxAge.setStatus("current")
_XstInstanceCfgBridgeHelloTime_Type = Timeout
_XstInstanceCfgBridgeHelloTime_Object = MibTableColumn
xstInstanceCfgBridgeHelloTime = _XstInstanceCfgBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 6, 4, 1, 13),
    _XstInstanceCfgBridgeHelloTime_Type()
)
xstInstanceCfgBridgeHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgBridgeHelloTime.setStatus("current")
_XstInstanceCfgBridgeForwardDelay_Type = Timeout
_XstInstanceCfgBridgeForwardDelay_Object = MibTableColumn
xstInstanceCfgBridgeForwardDelay = _XstInstanceCfgBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 6, 4, 1, 14),
    _XstInstanceCfgBridgeForwardDelay_Type()
)
xstInstanceCfgBridgeForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgBridgeForwardDelay.setStatus("current")
_XstInstanceCfgTxHoldCount_Type = Integer32
_XstInstanceCfgTxHoldCount_Object = MibTableColumn
xstInstanceCfgTxHoldCount = _XstInstanceCfgTxHoldCount_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 6, 4, 1, 15),
    _XstInstanceCfgTxHoldCount_Type()
)
xstInstanceCfgTxHoldCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgTxHoldCount.setStatus("current")
_XstInstanceCfgPathCostMethod_Type = StaPathCostMode
_XstInstanceCfgPathCostMethod_Object = MibTableColumn
xstInstanceCfgPathCostMethod = _XstInstanceCfgPathCostMethod_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 6, 4, 1, 16),
    _XstInstanceCfgPathCostMethod_Type()
)
xstInstanceCfgPathCostMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgPathCostMethod.setStatus("current")
_XstInstancePortTable_Object = MibTable
xstInstancePortTable = _XstInstancePortTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 6, 5)
)
if mibBuilder.loadTexts:
    xstInstancePortTable.setStatus("current")
_XstInstancePortEntry_Object = MibTableRow
xstInstancePortEntry = _XstInstancePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 6, 5, 1)
)
xstInstancePortEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "xstInstancePortInstance"),
    (0, "ES3526XA_ES3510-MIB", "xstInstancePortPort"),
)
if mibBuilder.loadTexts:
    xstInstancePortEntry.setStatus("current")
_XstInstancePortInstance_Type = Integer32
_XstInstancePortInstance_Object = MibTableColumn
xstInstancePortInstance = _XstInstancePortInstance_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 6, 5, 1, 1),
    _XstInstancePortInstance_Type()
)
xstInstancePortInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xstInstancePortInstance.setStatus("current")
_XstInstancePortPort_Type = Integer32
_XstInstancePortPort_Object = MibTableColumn
xstInstancePortPort = _XstInstancePortPort_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 6, 5, 1, 2),
    _XstInstancePortPort_Type()
)
xstInstancePortPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xstInstancePortPort.setStatus("current")


class _XstInstancePortPriority_Type(Integer32):
    """Custom type xstInstancePortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_XstInstancePortPriority_Type.__name__ = "Integer32"
_XstInstancePortPriority_Object = MibTableColumn
xstInstancePortPriority = _XstInstancePortPriority_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 6, 5, 1, 3),
    _XstInstancePortPriority_Type()
)
xstInstancePortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xstInstancePortPriority.setStatus("current")


class _XstInstancePortState_Type(Integer32):
    """Custom type xstInstancePortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discarding", 1),
          ("forwarding", 3),
          ("learning", 2))
    )


_XstInstancePortState_Type.__name__ = "Integer32"
_XstInstancePortState_Object = MibTableColumn
xstInstancePortState = _XstInstancePortState_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 6, 5, 1, 4),
    _XstInstancePortState_Type()
)
xstInstancePortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstancePortState.setStatus("current")
_XstInstancePortEnable_Type = EnabledStatus
_XstInstancePortEnable_Object = MibTableColumn
xstInstancePortEnable = _XstInstancePortEnable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 6, 5, 1, 5),
    _XstInstancePortEnable_Type()
)
xstInstancePortEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstancePortEnable.setStatus("current")


class _XstInstancePortPathCost_Type(Integer32):
    """Custom type xstInstancePortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_XstInstancePortPathCost_Type.__name__ = "Integer32"
_XstInstancePortPathCost_Object = MibTableColumn
xstInstancePortPathCost = _XstInstancePortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 6, 5, 1, 6),
    _XstInstancePortPathCost_Type()
)
xstInstancePortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xstInstancePortPathCost.setStatus("current")
_XstInstancePortDesignatedRoot_Type = BridgeId
_XstInstancePortDesignatedRoot_Object = MibTableColumn
xstInstancePortDesignatedRoot = _XstInstancePortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 6, 5, 1, 7),
    _XstInstancePortDesignatedRoot_Type()
)
xstInstancePortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstancePortDesignatedRoot.setStatus("current")
_XstInstancePortDesignatedCost_Type = Integer32
_XstInstancePortDesignatedCost_Object = MibTableColumn
xstInstancePortDesignatedCost = _XstInstancePortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 6, 5, 1, 8),
    _XstInstancePortDesignatedCost_Type()
)
xstInstancePortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstancePortDesignatedCost.setStatus("current")
_XstInstancePortDesignatedBridge_Type = BridgeId
_XstInstancePortDesignatedBridge_Object = MibTableColumn
xstInstancePortDesignatedBridge = _XstInstancePortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 6, 5, 1, 9),
    _XstInstancePortDesignatedBridge_Type()
)
xstInstancePortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstancePortDesignatedBridge.setStatus("current")


class _XstInstancePortDesignatedPort_Type(OctetString):
    """Custom type xstInstancePortDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_XstInstancePortDesignatedPort_Type.__name__ = "OctetString"
_XstInstancePortDesignatedPort_Object = MibTableColumn
xstInstancePortDesignatedPort = _XstInstancePortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 6, 5, 1, 10),
    _XstInstancePortDesignatedPort_Type()
)
xstInstancePortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstancePortDesignatedPort.setStatus("current")
_XstInstancePortForwardTransitions_Type = Counter32
_XstInstancePortForwardTransitions_Object = MibTableColumn
xstInstancePortForwardTransitions = _XstInstancePortForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 6, 5, 1, 11),
    _XstInstancePortForwardTransitions_Type()
)
xstInstancePortForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstancePortForwardTransitions.setStatus("current")


class _XstInstancePortPortRole_Type(Integer32):
    """Custom type xstInstancePortPortRole based on Integer32"""
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
        *(("alternate", 4),
          ("backup", 5),
          ("designated", 3),
          ("disabled", 1),
          ("master", 6),
          ("root", 2))
    )


_XstInstancePortPortRole_Type.__name__ = "Integer32"
_XstInstancePortPortRole_Object = MibTableColumn
xstInstancePortPortRole = _XstInstancePortPortRole_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 6, 5, 1, 12),
    _XstInstancePortPortRole_Type()
)
xstInstancePortPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstancePortPortRole.setStatus("current")
_MstInstanceEditTable_Object = MibTable
mstInstanceEditTable = _MstInstanceEditTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 6, 6)
)
if mibBuilder.loadTexts:
    mstInstanceEditTable.setStatus("current")
_MstInstanceEditEntry_Object = MibTableRow
mstInstanceEditEntry = _MstInstanceEditEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 6, 6, 1)
)
mstInstanceEditEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "mstInstanceEditIndex"),
)
if mibBuilder.loadTexts:
    mstInstanceEditEntry.setStatus("current")


class _MstInstanceEditIndex_Type(Integer32):
    """Custom type mstInstanceEditIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_MstInstanceEditIndex_Type.__name__ = "Integer32"
_MstInstanceEditIndex_Object = MibTableColumn
mstInstanceEditIndex = _MstInstanceEditIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 6, 6, 1, 1),
    _MstInstanceEditIndex_Type()
)
mstInstanceEditIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mstInstanceEditIndex.setStatus("current")


class _MstInstanceEditVlansMap_Type(OctetString):
    """Custom type mstInstanceEditVlansMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MstInstanceEditVlansMap_Type.__name__ = "OctetString"
_MstInstanceEditVlansMap_Object = MibTableColumn
mstInstanceEditVlansMap = _MstInstanceEditVlansMap_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 6, 6, 1, 2),
    _MstInstanceEditVlansMap_Type()
)
mstInstanceEditVlansMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mstInstanceEditVlansMap.setStatus("current")


class _MstInstanceEditVlansMap2k_Type(OctetString):
    """Custom type mstInstanceEditVlansMap2k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MstInstanceEditVlansMap2k_Type.__name__ = "OctetString"
_MstInstanceEditVlansMap2k_Object = MibTableColumn
mstInstanceEditVlansMap2k = _MstInstanceEditVlansMap2k_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 6, 6, 1, 3),
    _MstInstanceEditVlansMap2k_Type()
)
mstInstanceEditVlansMap2k.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mstInstanceEditVlansMap2k.setStatus("current")


class _MstInstanceEditVlansMap3k_Type(OctetString):
    """Custom type mstInstanceEditVlansMap3k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MstInstanceEditVlansMap3k_Type.__name__ = "OctetString"
_MstInstanceEditVlansMap3k_Object = MibTableColumn
mstInstanceEditVlansMap3k = _MstInstanceEditVlansMap3k_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 6, 6, 1, 4),
    _MstInstanceEditVlansMap3k_Type()
)
mstInstanceEditVlansMap3k.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mstInstanceEditVlansMap3k.setStatus("current")


class _MstInstanceEditVlansMap4k_Type(OctetString):
    """Custom type mstInstanceEditVlansMap4k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MstInstanceEditVlansMap4k_Type.__name__ = "OctetString"
_MstInstanceEditVlansMap4k_Object = MibTableColumn
mstInstanceEditVlansMap4k = _MstInstanceEditVlansMap4k_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 6, 6, 1, 5),
    _MstInstanceEditVlansMap4k_Type()
)
mstInstanceEditVlansMap4k.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mstInstanceEditVlansMap4k.setStatus("current")
_MstInstanceEditRemainingHops_Type = Integer32
_MstInstanceEditRemainingHops_Object = MibTableColumn
mstInstanceEditRemainingHops = _MstInstanceEditRemainingHops_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 6, 6, 1, 6),
    _MstInstanceEditRemainingHops_Type()
)
mstInstanceEditRemainingHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstInstanceEditRemainingHops.setStatus("current")
_MstInstanceOperTable_Object = MibTable
mstInstanceOperTable = _MstInstanceOperTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 6, 7)
)
if mibBuilder.loadTexts:
    mstInstanceOperTable.setStatus("current")
_MstInstanceOperEntry_Object = MibTableRow
mstInstanceOperEntry = _MstInstanceOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 6, 7, 1)
)
mstInstanceOperEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "mstInstanceOperIndex"),
)
if mibBuilder.loadTexts:
    mstInstanceOperEntry.setStatus("current")


class _MstInstanceOperIndex_Type(Integer32):
    """Custom type mstInstanceOperIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_MstInstanceOperIndex_Type.__name__ = "Integer32"
_MstInstanceOperIndex_Object = MibTableColumn
mstInstanceOperIndex = _MstInstanceOperIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 6, 7, 1, 1),
    _MstInstanceOperIndex_Type()
)
mstInstanceOperIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mstInstanceOperIndex.setStatus("current")


class _MstInstanceOperVlansMap_Type(OctetString):
    """Custom type mstInstanceOperVlansMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MstInstanceOperVlansMap_Type.__name__ = "OctetString"
_MstInstanceOperVlansMap_Object = MibTableColumn
mstInstanceOperVlansMap = _MstInstanceOperVlansMap_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 6, 7, 1, 2),
    _MstInstanceOperVlansMap_Type()
)
mstInstanceOperVlansMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstInstanceOperVlansMap.setStatus("current")


class _MstInstanceOperVlansMap2k_Type(OctetString):
    """Custom type mstInstanceOperVlansMap2k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MstInstanceOperVlansMap2k_Type.__name__ = "OctetString"
_MstInstanceOperVlansMap2k_Object = MibTableColumn
mstInstanceOperVlansMap2k = _MstInstanceOperVlansMap2k_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 6, 7, 1, 3),
    _MstInstanceOperVlansMap2k_Type()
)
mstInstanceOperVlansMap2k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstInstanceOperVlansMap2k.setStatus("current")


class _MstInstanceOperVlansMap3k_Type(OctetString):
    """Custom type mstInstanceOperVlansMap3k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MstInstanceOperVlansMap3k_Type.__name__ = "OctetString"
_MstInstanceOperVlansMap3k_Object = MibTableColumn
mstInstanceOperVlansMap3k = _MstInstanceOperVlansMap3k_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 6, 7, 1, 4),
    _MstInstanceOperVlansMap3k_Type()
)
mstInstanceOperVlansMap3k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstInstanceOperVlansMap3k.setStatus("current")


class _MstInstanceOperVlansMap4k_Type(OctetString):
    """Custom type mstInstanceOperVlansMap4k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MstInstanceOperVlansMap4k_Type.__name__ = "OctetString"
_MstInstanceOperVlansMap4k_Object = MibTableColumn
mstInstanceOperVlansMap4k = _MstInstanceOperVlansMap4k_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 6, 7, 1, 5),
    _MstInstanceOperVlansMap4k_Type()
)
mstInstanceOperVlansMap4k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstInstanceOperVlansMap4k.setStatus("current")
_StaLoopbackDetectionPortTable_Object = MibTable
staLoopbackDetectionPortTable = _StaLoopbackDetectionPortTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 7)
)
if mibBuilder.loadTexts:
    staLoopbackDetectionPortTable.setStatus("current")
_StaLoopbackDetectionPortEntry_Object = MibTableRow
staLoopbackDetectionPortEntry = _StaLoopbackDetectionPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 7, 1)
)
staLoopbackDetectionPortEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "staLoopbackDetectionPortIfIndex"),
)
if mibBuilder.loadTexts:
    staLoopbackDetectionPortEntry.setStatus("current")
_StaLoopbackDetectionPortIfIndex_Type = InterfaceIndex
_StaLoopbackDetectionPortIfIndex_Object = MibTableColumn
staLoopbackDetectionPortIfIndex = _StaLoopbackDetectionPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 7, 1, 1),
    _StaLoopbackDetectionPortIfIndex_Type()
)
staLoopbackDetectionPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    staLoopbackDetectionPortIfIndex.setStatus("current")
_StaLoopbackDetectionPortStatus_Type = EnabledStatus
_StaLoopbackDetectionPortStatus_Object = MibTableColumn
staLoopbackDetectionPortStatus = _StaLoopbackDetectionPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 7, 1, 2),
    _StaLoopbackDetectionPortStatus_Type()
)
staLoopbackDetectionPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staLoopbackDetectionPortStatus.setStatus("current")
_StaLoopbackDetectionPortTrapStatus_Type = EnabledStatus
_StaLoopbackDetectionPortTrapStatus_Object = MibTableColumn
staLoopbackDetectionPortTrapStatus = _StaLoopbackDetectionPortTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 7, 1, 3),
    _StaLoopbackDetectionPortTrapStatus_Type()
)
staLoopbackDetectionPortTrapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staLoopbackDetectionPortTrapStatus.setStatus("current")


class _StaLoopbackDetectionPortReleaseMode_Type(Integer32):
    """Custom type staLoopbackDetectionPortReleaseMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )


_StaLoopbackDetectionPortReleaseMode_Type.__name__ = "Integer32"
_StaLoopbackDetectionPortReleaseMode_Object = MibTableColumn
staLoopbackDetectionPortReleaseMode = _StaLoopbackDetectionPortReleaseMode_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 7, 1, 4),
    _StaLoopbackDetectionPortReleaseMode_Type()
)
staLoopbackDetectionPortReleaseMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staLoopbackDetectionPortReleaseMode.setStatus("current")


class _StaLoopbackDetectionPortRelease_Type(Integer32):
    """Custom type staLoopbackDetectionPortRelease based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noRelease", 1),
          ("release", 2))
    )


_StaLoopbackDetectionPortRelease_Type.__name__ = "Integer32"
_StaLoopbackDetectionPortRelease_Object = MibTableColumn
staLoopbackDetectionPortRelease = _StaLoopbackDetectionPortRelease_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 5, 7, 1, 5),
    _StaLoopbackDetectionPortRelease_Type()
)
staLoopbackDetectionPortRelease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staLoopbackDetectionPortRelease.setStatus("current")
_TftpMgt_ObjectIdentity = ObjectIdentity
tftpMgt = _TftpMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 6)
)


class _TftpFileType_Type(Integer32):
    """Custom type tftpFileType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("config", 2),
          ("opcode", 1))
    )


_TftpFileType_Type.__name__ = "Integer32"
_TftpFileType_Object = MibScalar
tftpFileType = _TftpFileType_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 6, 1),
    _TftpFileType_Type()
)
tftpFileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpFileType.setStatus("current")


class _TftpSrcFile_Type(DisplayString):
    """Custom type tftpSrcFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TftpSrcFile_Type.__name__ = "DisplayString"
_TftpSrcFile_Object = MibScalar
tftpSrcFile = _TftpSrcFile_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 6, 2),
    _TftpSrcFile_Type()
)
tftpSrcFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpSrcFile.setStatus("current")


class _TftpDestFile_Type(DisplayString):
    """Custom type tftpDestFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TftpDestFile_Type.__name__ = "DisplayString"
_TftpDestFile_Object = MibScalar
tftpDestFile = _TftpDestFile_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 6, 3),
    _TftpDestFile_Type()
)
tftpDestFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpDestFile.setStatus("current")
_TftpServer_Type = IpAddress
_TftpServer_Object = MibScalar
tftpServer = _TftpServer_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 6, 4),
    _TftpServer_Type()
)
tftpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpServer.setStatus("current")


class _TftpAction_Type(Integer32):
    """Custom type tftpAction based on Integer32"""
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
        *(("downloadToPROM", 2),
          ("downloadToRAM", 3),
          ("notDownloading", 1),
          ("upload", 4))
    )


_TftpAction_Type.__name__ = "Integer32"
_TftpAction_Object = MibScalar
tftpAction = _TftpAction_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 6, 5),
    _TftpAction_Type()
)
tftpAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpAction.setStatus("current")


class _TftpStatus_Type(Integer32):
    """Custom type tftpStatus based on Integer32"""
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
        *(("tftpDownloadChecksumError", 5),
          ("tftpDownloadIncompatibleImage", 6),
          ("tftpGeneralError", 3),
          ("tftpNoResponseFromServer", 4),
          ("tftpStatusUnknown", 2),
          ("tftpSuccess", 1),
          ("tftpTftpAccessViolation", 8),
          ("tftpTftpFileNotFound", 7))
    )


_TftpStatus_Type.__name__ = "Integer32"
_TftpStatus_Object = MibScalar
tftpStatus = _TftpStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 6, 6),
    _TftpStatus_Type()
)
tftpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tftpStatus.setStatus("current")
_RestartMgt_ObjectIdentity = ObjectIdentity
restartMgt = _RestartMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 7)
)


class _RestartOpCodeFile_Type(DisplayString):
    """Custom type restartOpCodeFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RestartOpCodeFile_Type.__name__ = "DisplayString"
_RestartOpCodeFile_Object = MibScalar
restartOpCodeFile = _RestartOpCodeFile_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 7, 1),
    _RestartOpCodeFile_Type()
)
restartOpCodeFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restartOpCodeFile.setStatus("current")


class _RestartConfigFile_Type(DisplayString):
    """Custom type restartConfigFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RestartConfigFile_Type.__name__ = "DisplayString"
_RestartConfigFile_Object = MibScalar
restartConfigFile = _RestartConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 7, 2),
    _RestartConfigFile_Type()
)
restartConfigFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restartConfigFile.setStatus("current")


class _RestartControl_Type(Integer32):
    """Custom type restartControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("coldBoot", 3),
          ("running", 1),
          ("warmBoot", 2))
    )


_RestartControl_Type.__name__ = "Integer32"
_RestartControl_Object = MibScalar
restartControl = _RestartControl_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 7, 3),
    _RestartControl_Type()
)
restartControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restartControl.setStatus("current")
_MirrorMgt_ObjectIdentity = ObjectIdentity
mirrorMgt = _MirrorMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 8)
)
_MirrorTable_Object = MibTable
mirrorTable = _MirrorTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 8, 1)
)
if mibBuilder.loadTexts:
    mirrorTable.setStatus("current")
_MirrorEntry_Object = MibTableRow
mirrorEntry = _MirrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 8, 1, 1)
)
mirrorEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "mirrorDestinationPort"),
    (0, "ES3526XA_ES3510-MIB", "mirrorSourcePort"),
)
if mibBuilder.loadTexts:
    mirrorEntry.setStatus("current")
_MirrorDestinationPort_Type = Integer32
_MirrorDestinationPort_Object = MibTableColumn
mirrorDestinationPort = _MirrorDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 8, 1, 1, 1),
    _MirrorDestinationPort_Type()
)
mirrorDestinationPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mirrorDestinationPort.setStatus("current")
_MirrorSourcePort_Type = Integer32
_MirrorSourcePort_Object = MibTableColumn
mirrorSourcePort = _MirrorSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 8, 1, 1, 2),
    _MirrorSourcePort_Type()
)
mirrorSourcePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mirrorSourcePort.setStatus("current")


class _MirrorType_Type(Integer32):
    """Custom type mirrorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("rx", 1),
          ("tx", 2))
    )


_MirrorType_Type.__name__ = "Integer32"
_MirrorType_Object = MibTableColumn
mirrorType = _MirrorType_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 8, 1, 1, 3),
    _MirrorType_Type()
)
mirrorType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mirrorType.setStatus("current")
_MirrorStatus_Type = ValidStatus
_MirrorStatus_Object = MibTableColumn
mirrorStatus = _MirrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 8, 1, 1, 4),
    _MirrorStatus_Type()
)
mirrorStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mirrorStatus.setStatus("current")
_IgmpSnoopMgt_ObjectIdentity = ObjectIdentity
igmpSnoopMgt = _IgmpSnoopMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 9)
)


class _IgmpSnoopStatus_Type(Integer32):
    """Custom type igmpSnoopStatus based on Integer32"""
    defaultValue = 1

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


_IgmpSnoopStatus_Type.__name__ = "Integer32"
_IgmpSnoopStatus_Object = MibScalar
igmpSnoopStatus = _IgmpSnoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 9, 1),
    _IgmpSnoopStatus_Type()
)
igmpSnoopStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopStatus.setStatus("current")


class _IgmpSnoopQuerier_Type(Integer32):
    """Custom type igmpSnoopQuerier based on Integer32"""
    defaultValue = 1

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


_IgmpSnoopQuerier_Type.__name__ = "Integer32"
_IgmpSnoopQuerier_Object = MibScalar
igmpSnoopQuerier = _IgmpSnoopQuerier_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 9, 2),
    _IgmpSnoopQuerier_Type()
)
igmpSnoopQuerier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopQuerier.setStatus("current")


class _IgmpSnoopQueryCount_Type(Integer32):
    """Custom type igmpSnoopQueryCount based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_IgmpSnoopQueryCount_Type.__name__ = "Integer32"
_IgmpSnoopQueryCount_Object = MibScalar
igmpSnoopQueryCount = _IgmpSnoopQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 9, 3),
    _IgmpSnoopQueryCount_Type()
)
igmpSnoopQueryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopQueryCount.setStatus("current")


class _IgmpSnoopQueryInterval_Type(Integer32):
    """Custom type igmpSnoopQueryInterval based on Integer32"""
    defaultValue = 125

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 125),
    )


_IgmpSnoopQueryInterval_Type.__name__ = "Integer32"
_IgmpSnoopQueryInterval_Object = MibScalar
igmpSnoopQueryInterval = _IgmpSnoopQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 9, 4),
    _IgmpSnoopQueryInterval_Type()
)
igmpSnoopQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopQueryInterval.setStatus("current")


class _IgmpSnoopQueryMaxResponseTime_Type(Integer32):
    """Custom type igmpSnoopQueryMaxResponseTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 25),
    )


_IgmpSnoopQueryMaxResponseTime_Type.__name__ = "Integer32"
_IgmpSnoopQueryMaxResponseTime_Object = MibScalar
igmpSnoopQueryMaxResponseTime = _IgmpSnoopQueryMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 9, 5),
    _IgmpSnoopQueryMaxResponseTime_Type()
)
igmpSnoopQueryMaxResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopQueryMaxResponseTime.setStatus("current")


class _IgmpSnoopQueryTimeout_Type(Integer32):
    """Custom type igmpSnoopQueryTimeout based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 500),
    )


_IgmpSnoopQueryTimeout_Type.__name__ = "Integer32"
_IgmpSnoopQueryTimeout_Object = MibScalar
igmpSnoopQueryTimeout = _IgmpSnoopQueryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 9, 6),
    _IgmpSnoopQueryTimeout_Type()
)
igmpSnoopQueryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopQueryTimeout.setStatus("current")


class _IgmpSnoopVersion_Type(Integer32):
    """Custom type igmpSnoopVersion based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_IgmpSnoopVersion_Type.__name__ = "Integer32"
_IgmpSnoopVersion_Object = MibScalar
igmpSnoopVersion = _IgmpSnoopVersion_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 9, 7),
    _IgmpSnoopVersion_Type()
)
igmpSnoopVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopVersion.setStatus("current")
_IgmpSnoopRouterCurrentTable_Object = MibTable
igmpSnoopRouterCurrentTable = _IgmpSnoopRouterCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 9, 8)
)
if mibBuilder.loadTexts:
    igmpSnoopRouterCurrentTable.setStatus("current")
_IgmpSnoopRouterCurrentEntry_Object = MibTableRow
igmpSnoopRouterCurrentEntry = _IgmpSnoopRouterCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 9, 8, 1)
)
igmpSnoopRouterCurrentEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "igmpSnoopRouterCurrentVlanIndex"),
)
if mibBuilder.loadTexts:
    igmpSnoopRouterCurrentEntry.setStatus("current")
_IgmpSnoopRouterCurrentVlanIndex_Type = Unsigned32
_IgmpSnoopRouterCurrentVlanIndex_Object = MibTableColumn
igmpSnoopRouterCurrentVlanIndex = _IgmpSnoopRouterCurrentVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 9, 8, 1, 1),
    _IgmpSnoopRouterCurrentVlanIndex_Type()
)
igmpSnoopRouterCurrentVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopRouterCurrentVlanIndex.setStatus("current")
_IgmpSnoopRouterCurrentPorts_Type = PortList
_IgmpSnoopRouterCurrentPorts_Object = MibTableColumn
igmpSnoopRouterCurrentPorts = _IgmpSnoopRouterCurrentPorts_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 9, 8, 1, 2),
    _IgmpSnoopRouterCurrentPorts_Type()
)
igmpSnoopRouterCurrentPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopRouterCurrentPorts.setStatus("current")
_IgmpSnoopRouterCurrentStatus_Type = PortList
_IgmpSnoopRouterCurrentStatus_Object = MibTableColumn
igmpSnoopRouterCurrentStatus = _IgmpSnoopRouterCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 9, 8, 1, 3),
    _IgmpSnoopRouterCurrentStatus_Type()
)
igmpSnoopRouterCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopRouterCurrentStatus.setStatus("current")
_IgmpSnoopRouterStaticTable_Object = MibTable
igmpSnoopRouterStaticTable = _IgmpSnoopRouterStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 9, 9)
)
if mibBuilder.loadTexts:
    igmpSnoopRouterStaticTable.setStatus("current")
_IgmpSnoopRouterStaticEntry_Object = MibTableRow
igmpSnoopRouterStaticEntry = _IgmpSnoopRouterStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 9, 9, 1)
)
igmpSnoopRouterStaticEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "igmpSnoopRouterStaticVlanIndex"),
)
if mibBuilder.loadTexts:
    igmpSnoopRouterStaticEntry.setStatus("current")
_IgmpSnoopRouterStaticVlanIndex_Type = Unsigned32
_IgmpSnoopRouterStaticVlanIndex_Object = MibTableColumn
igmpSnoopRouterStaticVlanIndex = _IgmpSnoopRouterStaticVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 9, 9, 1, 1),
    _IgmpSnoopRouterStaticVlanIndex_Type()
)
igmpSnoopRouterStaticVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopRouterStaticVlanIndex.setStatus("current")
_IgmpSnoopRouterStaticPorts_Type = PortList
_IgmpSnoopRouterStaticPorts_Object = MibTableColumn
igmpSnoopRouterStaticPorts = _IgmpSnoopRouterStaticPorts_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 9, 9, 1, 2),
    _IgmpSnoopRouterStaticPorts_Type()
)
igmpSnoopRouterStaticPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpSnoopRouterStaticPorts.setStatus("current")
_IgmpSnoopRouterStaticStatus_Type = ValidStatus
_IgmpSnoopRouterStaticStatus_Object = MibTableColumn
igmpSnoopRouterStaticStatus = _IgmpSnoopRouterStaticStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 9, 9, 1, 3),
    _IgmpSnoopRouterStaticStatus_Type()
)
igmpSnoopRouterStaticStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpSnoopRouterStaticStatus.setStatus("current")
_IgmpSnoopMulticastCurrentTable_Object = MibTable
igmpSnoopMulticastCurrentTable = _IgmpSnoopMulticastCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 9, 10)
)
if mibBuilder.loadTexts:
    igmpSnoopMulticastCurrentTable.setStatus("current")
_IgmpSnoopMulticastCurrentEntry_Object = MibTableRow
igmpSnoopMulticastCurrentEntry = _IgmpSnoopMulticastCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 9, 10, 1)
)
igmpSnoopMulticastCurrentEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "igmpSnoopMulticastCurrentVlanIndex"),
    (0, "ES3526XA_ES3510-MIB", "igmpSnoopMulticastCurrentIpAddress"),
)
if mibBuilder.loadTexts:
    igmpSnoopMulticastCurrentEntry.setStatus("current")
_IgmpSnoopMulticastCurrentVlanIndex_Type = Unsigned32
_IgmpSnoopMulticastCurrentVlanIndex_Object = MibTableColumn
igmpSnoopMulticastCurrentVlanIndex = _IgmpSnoopMulticastCurrentVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 9, 10, 1, 1),
    _IgmpSnoopMulticastCurrentVlanIndex_Type()
)
igmpSnoopMulticastCurrentVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopMulticastCurrentVlanIndex.setStatus("current")
_IgmpSnoopMulticastCurrentIpAddress_Type = IpAddress
_IgmpSnoopMulticastCurrentIpAddress_Object = MibTableColumn
igmpSnoopMulticastCurrentIpAddress = _IgmpSnoopMulticastCurrentIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 9, 10, 1, 2),
    _IgmpSnoopMulticastCurrentIpAddress_Type()
)
igmpSnoopMulticastCurrentIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopMulticastCurrentIpAddress.setStatus("current")
_IgmpSnoopMulticastCurrentPorts_Type = PortList
_IgmpSnoopMulticastCurrentPorts_Object = MibTableColumn
igmpSnoopMulticastCurrentPorts = _IgmpSnoopMulticastCurrentPorts_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 9, 10, 1, 3),
    _IgmpSnoopMulticastCurrentPorts_Type()
)
igmpSnoopMulticastCurrentPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopMulticastCurrentPorts.setStatus("current")
_IgmpSnoopMulticastCurrentStatus_Type = PortList
_IgmpSnoopMulticastCurrentStatus_Object = MibTableColumn
igmpSnoopMulticastCurrentStatus = _IgmpSnoopMulticastCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 9, 10, 1, 4),
    _IgmpSnoopMulticastCurrentStatus_Type()
)
igmpSnoopMulticastCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopMulticastCurrentStatus.setStatus("current")
_IgmpSnoopMulticastStaticTable_Object = MibTable
igmpSnoopMulticastStaticTable = _IgmpSnoopMulticastStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 9, 11)
)
if mibBuilder.loadTexts:
    igmpSnoopMulticastStaticTable.setStatus("current")
_IgmpSnoopMulticastStaticEntry_Object = MibTableRow
igmpSnoopMulticastStaticEntry = _IgmpSnoopMulticastStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 9, 11, 1)
)
igmpSnoopMulticastStaticEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "igmpSnoopMulticastStaticVlanIndex"),
    (0, "ES3526XA_ES3510-MIB", "igmpSnoopMulticastStaticIpAddress"),
)
if mibBuilder.loadTexts:
    igmpSnoopMulticastStaticEntry.setStatus("current")
_IgmpSnoopMulticastStaticVlanIndex_Type = Unsigned32
_IgmpSnoopMulticastStaticVlanIndex_Object = MibTableColumn
igmpSnoopMulticastStaticVlanIndex = _IgmpSnoopMulticastStaticVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 9, 11, 1, 1),
    _IgmpSnoopMulticastStaticVlanIndex_Type()
)
igmpSnoopMulticastStaticVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopMulticastStaticVlanIndex.setStatus("current")
_IgmpSnoopMulticastStaticIpAddress_Type = IpAddress
_IgmpSnoopMulticastStaticIpAddress_Object = MibTableColumn
igmpSnoopMulticastStaticIpAddress = _IgmpSnoopMulticastStaticIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 9, 11, 1, 2),
    _IgmpSnoopMulticastStaticIpAddress_Type()
)
igmpSnoopMulticastStaticIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopMulticastStaticIpAddress.setStatus("current")
_IgmpSnoopMulticastStaticPorts_Type = PortList
_IgmpSnoopMulticastStaticPorts_Object = MibTableColumn
igmpSnoopMulticastStaticPorts = _IgmpSnoopMulticastStaticPorts_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 9, 11, 1, 3),
    _IgmpSnoopMulticastStaticPorts_Type()
)
igmpSnoopMulticastStaticPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpSnoopMulticastStaticPorts.setStatus("current")
_IgmpSnoopMulticastStaticStatus_Type = ValidStatus
_IgmpSnoopMulticastStaticStatus_Object = MibTableColumn
igmpSnoopMulticastStaticStatus = _IgmpSnoopMulticastStaticStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 9, 11, 1, 4),
    _IgmpSnoopMulticastStaticStatus_Type()
)
igmpSnoopMulticastStaticStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpSnoopMulticastStaticStatus.setStatus("current")
_IgmpSnoopCurrentVlanTable_Object = MibTable
igmpSnoopCurrentVlanTable = _IgmpSnoopCurrentVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 9, 14)
)
if mibBuilder.loadTexts:
    igmpSnoopCurrentVlanTable.setStatus("current")
_IgmpSnoopCurrentVlanEntry_Object = MibTableRow
igmpSnoopCurrentVlanEntry = _IgmpSnoopCurrentVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 9, 14, 1)
)
igmpSnoopCurrentVlanEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "igmpSnoopCurrentVlanIndex"),
)
if mibBuilder.loadTexts:
    igmpSnoopCurrentVlanEntry.setStatus("current")
_IgmpSnoopCurrentVlanIndex_Type = Unsigned32
_IgmpSnoopCurrentVlanIndex_Object = MibTableColumn
igmpSnoopCurrentVlanIndex = _IgmpSnoopCurrentVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 9, 14, 1, 1),
    _IgmpSnoopCurrentVlanIndex_Type()
)
igmpSnoopCurrentVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopCurrentVlanIndex.setStatus("current")
_IgmpSnoopCurrentVlanImmediateLeave_Type = EnabledStatus
_IgmpSnoopCurrentVlanImmediateLeave_Object = MibTableColumn
igmpSnoopCurrentVlanImmediateLeave = _IgmpSnoopCurrentVlanImmediateLeave_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 9, 14, 1, 3),
    _IgmpSnoopCurrentVlanImmediateLeave_Type()
)
igmpSnoopCurrentVlanImmediateLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopCurrentVlanImmediateLeave.setStatus("current")
_IgmpSnoopLeaveProxy_Type = EnabledStatus
_IgmpSnoopLeaveProxy_Object = MibScalar
igmpSnoopLeaveProxy = _IgmpSnoopLeaveProxy_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 9, 15),
    _IgmpSnoopLeaveProxy_Type()
)
igmpSnoopLeaveProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopLeaveProxy.setStatus("current")
_IgmpSnoopFilterStatus_Type = EnabledStatus
_IgmpSnoopFilterStatus_Object = MibScalar
igmpSnoopFilterStatus = _IgmpSnoopFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 9, 17),
    _IgmpSnoopFilterStatus_Type()
)
igmpSnoopFilterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopFilterStatus.setStatus("current")
_IgmpSnoopProfileTable_Object = MibTable
igmpSnoopProfileTable = _IgmpSnoopProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 9, 18)
)
if mibBuilder.loadTexts:
    igmpSnoopProfileTable.setStatus("current")
_IgmpSnoopProfileEntry_Object = MibTableRow
igmpSnoopProfileEntry = _IgmpSnoopProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 9, 18, 1)
)
igmpSnoopProfileEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "igmpSnoopProfileId"),
)
if mibBuilder.loadTexts:
    igmpSnoopProfileEntry.setStatus("current")
_IgmpSnoopProfileId_Type = Unsigned32
_IgmpSnoopProfileId_Object = MibTableColumn
igmpSnoopProfileId = _IgmpSnoopProfileId_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 9, 18, 1, 1),
    _IgmpSnoopProfileId_Type()
)
igmpSnoopProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopProfileId.setStatus("current")


class _IgmpSnoopProfileAction_Type(Integer32):
    """Custom type igmpSnoopProfileAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )


_IgmpSnoopProfileAction_Type.__name__ = "Integer32"
_IgmpSnoopProfileAction_Object = MibTableColumn
igmpSnoopProfileAction = _IgmpSnoopProfileAction_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 9, 18, 1, 2),
    _IgmpSnoopProfileAction_Type()
)
igmpSnoopProfileAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopProfileAction.setStatus("current")
_IgmpSnoopProfileStatus_Type = ValidStatus
_IgmpSnoopProfileStatus_Object = MibTableColumn
igmpSnoopProfileStatus = _IgmpSnoopProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 9, 18, 1, 3),
    _IgmpSnoopProfileStatus_Type()
)
igmpSnoopProfileStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopProfileStatus.setStatus("current")
_IgmpSnoopProfileCtl_ObjectIdentity = ObjectIdentity
igmpSnoopProfileCtl = _IgmpSnoopProfileCtl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 9, 19)
)
_IgmpSnoopProfileCtlId_Type = Unsigned32
_IgmpSnoopProfileCtlId_Object = MibScalar
igmpSnoopProfileCtlId = _IgmpSnoopProfileCtlId_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 9, 19, 1),
    _IgmpSnoopProfileCtlId_Type()
)
igmpSnoopProfileCtlId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopProfileCtlId.setStatus("current")
_IgmpSnoopProfileCtlInetAddressType_Type = InetAddressType
_IgmpSnoopProfileCtlInetAddressType_Object = MibScalar
igmpSnoopProfileCtlInetAddressType = _IgmpSnoopProfileCtlInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 9, 19, 2),
    _IgmpSnoopProfileCtlInetAddressType_Type()
)
igmpSnoopProfileCtlInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopProfileCtlInetAddressType.setStatus("current")
_IgmpSnoopProfileCtlStartInetAddress_Type = InetAddress
_IgmpSnoopProfileCtlStartInetAddress_Object = MibScalar
igmpSnoopProfileCtlStartInetAddress = _IgmpSnoopProfileCtlStartInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 9, 19, 3),
    _IgmpSnoopProfileCtlStartInetAddress_Type()
)
igmpSnoopProfileCtlStartInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopProfileCtlStartInetAddress.setStatus("current")
_IgmpSnoopProfileCtlEndInetAddress_Type = InetAddress
_IgmpSnoopProfileCtlEndInetAddress_Object = MibScalar
igmpSnoopProfileCtlEndInetAddress = _IgmpSnoopProfileCtlEndInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 9, 19, 4),
    _IgmpSnoopProfileCtlEndInetAddress_Type()
)
igmpSnoopProfileCtlEndInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopProfileCtlEndInetAddress.setStatus("current")


class _IgmpSnoopProfileCtlAction_Type(Integer32):
    """Custom type igmpSnoopProfileCtlAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("create", 2),
          ("destroy", 3),
          ("noAction", 1))
    )


_IgmpSnoopProfileCtlAction_Type.__name__ = "Integer32"
_IgmpSnoopProfileCtlAction_Object = MibScalar
igmpSnoopProfileCtlAction = _IgmpSnoopProfileCtlAction_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 9, 19, 5),
    _IgmpSnoopProfileCtlAction_Type()
)
igmpSnoopProfileCtlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopProfileCtlAction.setStatus("current")
_IgmpSnoopProfileRangeTable_Object = MibTable
igmpSnoopProfileRangeTable = _IgmpSnoopProfileRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 9, 20)
)
if mibBuilder.loadTexts:
    igmpSnoopProfileRangeTable.setStatus("current")
_IgmpSnoopProfileRangeEntry_Object = MibTableRow
igmpSnoopProfileRangeEntry = _IgmpSnoopProfileRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 9, 20, 1)
)
igmpSnoopProfileRangeEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "igmpSnoopProfileRangeProfileId"),
    (0, "ES3526XA_ES3510-MIB", "igmpSnoopProfileRangeInetAddressType"),
    (0, "ES3526XA_ES3510-MIB", "igmpSnoopProfileRangeStartInetAddress"),
)
if mibBuilder.loadTexts:
    igmpSnoopProfileRangeEntry.setStatus("current")
_IgmpSnoopProfileRangeProfileId_Type = Unsigned32
_IgmpSnoopProfileRangeProfileId_Object = MibTableColumn
igmpSnoopProfileRangeProfileId = _IgmpSnoopProfileRangeProfileId_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 9, 20, 1, 1),
    _IgmpSnoopProfileRangeProfileId_Type()
)
igmpSnoopProfileRangeProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopProfileRangeProfileId.setStatus("current")
_IgmpSnoopProfileRangeInetAddressType_Type = InetAddressType
_IgmpSnoopProfileRangeInetAddressType_Object = MibTableColumn
igmpSnoopProfileRangeInetAddressType = _IgmpSnoopProfileRangeInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 9, 20, 1, 2),
    _IgmpSnoopProfileRangeInetAddressType_Type()
)
igmpSnoopProfileRangeInetAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopProfileRangeInetAddressType.setStatus("current")
_IgmpSnoopProfileRangeStartInetAddress_Type = InetAddress
_IgmpSnoopProfileRangeStartInetAddress_Object = MibTableColumn
igmpSnoopProfileRangeStartInetAddress = _IgmpSnoopProfileRangeStartInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 9, 20, 1, 3),
    _IgmpSnoopProfileRangeStartInetAddress_Type()
)
igmpSnoopProfileRangeStartInetAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopProfileRangeStartInetAddress.setStatus("current")
_IgmpSnoopProfileRangeEndInetAddress_Type = InetAddress
_IgmpSnoopProfileRangeEndInetAddress_Object = MibTableColumn
igmpSnoopProfileRangeEndInetAddress = _IgmpSnoopProfileRangeEndInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 9, 20, 1, 4),
    _IgmpSnoopProfileRangeEndInetAddress_Type()
)
igmpSnoopProfileRangeEndInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopProfileRangeEndInetAddress.setStatus("current")


class _IgmpSnoopProfileRangeAction_Type(Integer32):
    """Custom type igmpSnoopProfileRangeAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )


_IgmpSnoopProfileRangeAction_Type.__name__ = "Integer32"
_IgmpSnoopProfileRangeAction_Object = MibTableColumn
igmpSnoopProfileRangeAction = _IgmpSnoopProfileRangeAction_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 9, 20, 1, 5),
    _IgmpSnoopProfileRangeAction_Type()
)
igmpSnoopProfileRangeAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopProfileRangeAction.setStatus("current")
_IgmpSnoopFilterPortTable_Object = MibTable
igmpSnoopFilterPortTable = _IgmpSnoopFilterPortTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 9, 21)
)
if mibBuilder.loadTexts:
    igmpSnoopFilterPortTable.setStatus("current")
_IgmpSnoopFilterPortEntry_Object = MibTableRow
igmpSnoopFilterPortEntry = _IgmpSnoopFilterPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 9, 21, 1)
)
igmpSnoopFilterPortEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "igmpSnoopFilterPortIndex"),
)
if mibBuilder.loadTexts:
    igmpSnoopFilterPortEntry.setStatus("current")
_IgmpSnoopFilterPortIndex_Type = Unsigned32
_IgmpSnoopFilterPortIndex_Object = MibTableColumn
igmpSnoopFilterPortIndex = _IgmpSnoopFilterPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 9, 21, 1, 1),
    _IgmpSnoopFilterPortIndex_Type()
)
igmpSnoopFilterPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopFilterPortIndex.setStatus("current")
_IgmpSnoopFilterPortProfileId_Type = Integer32
_IgmpSnoopFilterPortProfileId_Object = MibTableColumn
igmpSnoopFilterPortProfileId = _IgmpSnoopFilterPortProfileId_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 9, 21, 1, 2),
    _IgmpSnoopFilterPortProfileId_Type()
)
igmpSnoopFilterPortProfileId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopFilterPortProfileId.setStatus("current")
_IgmpSnoopThrottlePortTable_Object = MibTable
igmpSnoopThrottlePortTable = _IgmpSnoopThrottlePortTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 9, 22)
)
if mibBuilder.loadTexts:
    igmpSnoopThrottlePortTable.setStatus("current")
_IgmpSnoopThrottlePortEntry_Object = MibTableRow
igmpSnoopThrottlePortEntry = _IgmpSnoopThrottlePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 9, 22, 1)
)
igmpSnoopThrottlePortEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "igmpSnoopThrottlePortIndex"),
)
if mibBuilder.loadTexts:
    igmpSnoopThrottlePortEntry.setStatus("current")
_IgmpSnoopThrottlePortIndex_Type = Unsigned32
_IgmpSnoopThrottlePortIndex_Object = MibTableColumn
igmpSnoopThrottlePortIndex = _IgmpSnoopThrottlePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 9, 22, 1, 1),
    _IgmpSnoopThrottlePortIndex_Type()
)
igmpSnoopThrottlePortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopThrottlePortIndex.setStatus("current")
_IgmpSnoopThrottlePortRunningStatus_Type = TruthValue
_IgmpSnoopThrottlePortRunningStatus_Object = MibTableColumn
igmpSnoopThrottlePortRunningStatus = _IgmpSnoopThrottlePortRunningStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 9, 22, 1, 2),
    _IgmpSnoopThrottlePortRunningStatus_Type()
)
igmpSnoopThrottlePortRunningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopThrottlePortRunningStatus.setStatus("current")


class _IgmpSnoopThrottlePortAction_Type(Integer32):
    """Custom type igmpSnoopThrottlePortAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("replace", 1))
    )


_IgmpSnoopThrottlePortAction_Type.__name__ = "Integer32"
_IgmpSnoopThrottlePortAction_Object = MibTableColumn
igmpSnoopThrottlePortAction = _IgmpSnoopThrottlePortAction_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 9, 22, 1, 3),
    _IgmpSnoopThrottlePortAction_Type()
)
igmpSnoopThrottlePortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopThrottlePortAction.setStatus("current")


class _IgmpSnoopThrottlePortMaxGroups_Type(Integer32):
    """Custom type igmpSnoopThrottlePortMaxGroups based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_IgmpSnoopThrottlePortMaxGroups_Type.__name__ = "Integer32"
_IgmpSnoopThrottlePortMaxGroups_Object = MibTableColumn
igmpSnoopThrottlePortMaxGroups = _IgmpSnoopThrottlePortMaxGroups_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 9, 22, 1, 4),
    _IgmpSnoopThrottlePortMaxGroups_Type()
)
igmpSnoopThrottlePortMaxGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopThrottlePortMaxGroups.setStatus("current")
_IgmpSnoopThrottlePortCurrentGroups_Type = Integer32
_IgmpSnoopThrottlePortCurrentGroups_Object = MibTableColumn
igmpSnoopThrottlePortCurrentGroups = _IgmpSnoopThrottlePortCurrentGroups_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 9, 22, 1, 5),
    _IgmpSnoopThrottlePortCurrentGroups_Type()
)
igmpSnoopThrottlePortCurrentGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopThrottlePortCurrentGroups.setStatus("current")
_IpMgt_ObjectIdentity = ObjectIdentity
ipMgt = _IpMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 10)
)
_NetConfigTable_Object = MibTable
netConfigTable = _NetConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 10, 1)
)
if mibBuilder.loadTexts:
    netConfigTable.setStatus("current")
_NetConfigEntry_Object = MibTableRow
netConfigEntry = _NetConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 10, 1, 1)
)
netConfigEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "netConfigIfIndex"),
    (0, "ES3526XA_ES3510-MIB", "netConfigIPAddress"),
    (0, "ES3526XA_ES3510-MIB", "netConfigSubnetMask"),
)
if mibBuilder.loadTexts:
    netConfigEntry.setStatus("current")
_NetConfigIfIndex_Type = Integer32
_NetConfigIfIndex_Object = MibTableColumn
netConfigIfIndex = _NetConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 10, 1, 1, 1),
    _NetConfigIfIndex_Type()
)
netConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    netConfigIfIndex.setStatus("current")
_NetConfigIPAddress_Type = IpAddress
_NetConfigIPAddress_Object = MibTableColumn
netConfigIPAddress = _NetConfigIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 10, 1, 1, 2),
    _NetConfigIPAddress_Type()
)
netConfigIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    netConfigIPAddress.setStatus("current")
_NetConfigSubnetMask_Type = IpAddress
_NetConfigSubnetMask_Object = MibTableColumn
netConfigSubnetMask = _NetConfigSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 10, 1, 1, 3),
    _NetConfigSubnetMask_Type()
)
netConfigSubnetMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    netConfigSubnetMask.setStatus("current")


class _NetConfigPrimaryInterface_Type(Integer32):
    """Custom type netConfigPrimaryInterface based on Integer32"""
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


_NetConfigPrimaryInterface_Type.__name__ = "Integer32"
_NetConfigPrimaryInterface_Object = MibTableColumn
netConfigPrimaryInterface = _NetConfigPrimaryInterface_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 10, 1, 1, 4),
    _NetConfigPrimaryInterface_Type()
)
netConfigPrimaryInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    netConfigPrimaryInterface.setStatus("current")


class _NetConfigUnnumbered_Type(Integer32):
    """Custom type netConfigUnnumbered based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notUnnumbered", 2),
          ("unnumbered", 1))
    )


_NetConfigUnnumbered_Type.__name__ = "Integer32"
_NetConfigUnnumbered_Object = MibTableColumn
netConfigUnnumbered = _NetConfigUnnumbered_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 10, 1, 1, 5),
    _NetConfigUnnumbered_Type()
)
netConfigUnnumbered.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    netConfigUnnumbered.setStatus("current")
_NetConfigStatus_Type = RowStatus
_NetConfigStatus_Object = MibTableColumn
netConfigStatus = _NetConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 10, 1, 1, 6),
    _NetConfigStatus_Type()
)
netConfigStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    netConfigStatus.setStatus("current")
_NetDefaultGateway_Type = IpAddress
_NetDefaultGateway_Object = MibScalar
netDefaultGateway = _NetDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 10, 2),
    _NetDefaultGateway_Type()
)
netDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netDefaultGateway.setStatus("current")


class _IpHttpState_Type(Integer32):
    """Custom type ipHttpState based on Integer32"""
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


_IpHttpState_Type.__name__ = "Integer32"
_IpHttpState_Object = MibScalar
ipHttpState = _IpHttpState_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 10, 3),
    _IpHttpState_Type()
)
ipHttpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipHttpState.setStatus("current")


class _IpHttpPort_Type(Integer32):
    """Custom type ipHttpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IpHttpPort_Type.__name__ = "Integer32"
_IpHttpPort_Object = MibScalar
ipHttpPort = _IpHttpPort_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 10, 4),
    _IpHttpPort_Type()
)
ipHttpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipHttpPort.setStatus("current")


class _IpDhcpRestart_Type(Integer32):
    """Custom type ipDhcpRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noRestart", 2),
          ("restart", 1))
    )


_IpDhcpRestart_Type.__name__ = "Integer32"
_IpDhcpRestart_Object = MibScalar
ipDhcpRestart = _IpDhcpRestart_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 10, 5),
    _IpDhcpRestart_Type()
)
ipDhcpRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipDhcpRestart.setStatus("current")


class _IpHttpsState_Type(Integer32):
    """Custom type ipHttpsState based on Integer32"""
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


_IpHttpsState_Type.__name__ = "Integer32"
_IpHttpsState_Object = MibScalar
ipHttpsState = _IpHttpsState_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 10, 6),
    _IpHttpsState_Type()
)
ipHttpsState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipHttpsState.setStatus("current")


class _IpHttpsPort_Type(Integer32):
    """Custom type ipHttpsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IpHttpsPort_Type.__name__ = "Integer32"
_IpHttpsPort_Object = MibScalar
ipHttpsPort = _IpHttpsPort_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 10, 7),
    _IpHttpsPort_Type()
)
ipHttpsPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipHttpsPort.setStatus("current")
_PingMgt_ObjectIdentity = ObjectIdentity
pingMgt = _PingMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 10, 15)
)
_PingIpAddress_Type = IpAddress
_PingIpAddress_Object = MibScalar
pingIpAddress = _PingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 10, 15, 1),
    _PingIpAddress_Type()
)
pingIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pingIpAddress.setStatus("current")


class _PingPacketSize_Type(Integer32):
    """Custom type pingPacketSize based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 512),
    )


_PingPacketSize_Type.__name__ = "Integer32"
_PingPacketSize_Object = MibScalar
pingPacketSize = _PingPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 10, 15, 2),
    _PingPacketSize_Type()
)
pingPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pingPacketSize.setStatus("current")
_PingRoundTripTime_Type = Integer32
_PingRoundTripTime_Object = MibScalar
pingRoundTripTime = _PingRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 10, 15, 3),
    _PingRoundTripTime_Type()
)
pingRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingRoundTripTime.setStatus("current")
if mibBuilder.loadTexts:
    pingRoundTripTime.setUnits("milliseconds")
_PingCompleted_Type = TruthValue
_PingCompleted_Object = MibScalar
pingCompleted = _PingCompleted_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 10, 15, 4),
    _PingCompleted_Type()
)
pingCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingCompleted.setStatus("current")


class _PingAction_Type(Integer32):
    """Custom type pingAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("pingStart", 2))
    )


_PingAction_Type.__name__ = "Integer32"
_PingAction_Object = MibScalar
pingAction = _PingAction_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 10, 15, 5),
    _PingAction_Type()
)
pingAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pingAction.setStatus("current")
_BcastStormMgt_ObjectIdentity = ObjectIdentity
bcastStormMgt = _BcastStormMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 11)
)
_BcastStormTable_Object = MibTable
bcastStormTable = _BcastStormTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 11, 1)
)
if mibBuilder.loadTexts:
    bcastStormTable.setStatus("current")
_BcastStormEntry_Object = MibTableRow
bcastStormEntry = _BcastStormEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 11, 1, 1)
)
bcastStormEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "bcastStormIfIndex"),
)
if mibBuilder.loadTexts:
    bcastStormEntry.setStatus("current")
_BcastStormIfIndex_Type = Integer32
_BcastStormIfIndex_Object = MibTableColumn
bcastStormIfIndex = _BcastStormIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 11, 1, 1, 1),
    _BcastStormIfIndex_Type()
)
bcastStormIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bcastStormIfIndex.setStatus("current")


class _BcastStormStatus_Type(Integer32):
    """Custom type bcastStormStatus based on Integer32"""
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


_BcastStormStatus_Type.__name__ = "Integer32"
_BcastStormStatus_Object = MibTableColumn
bcastStormStatus = _BcastStormStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 11, 1, 1, 2),
    _BcastStormStatus_Type()
)
bcastStormStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcastStormStatus.setStatus("current")


class _BcastStormOctetRateScale_Type(Integer32):
    """Custom type bcastStormOctetRateScale based on Integer32"""
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
        *(("scale-100k", 1),
          ("scale-10k", 2),
          ("scale-1k", 3),
          ("scale-1m", 0))
    )


_BcastStormOctetRateScale_Type.__name__ = "Integer32"
_BcastStormOctetRateScale_Object = MibTableColumn
bcastStormOctetRateScale = _BcastStormOctetRateScale_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 11, 1, 1, 3),
    _BcastStormOctetRateScale_Type()
)
bcastStormOctetRateScale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcastStormOctetRateScale.setStatus("current")


class _BcastStormOctetRateLevel_Type(Integer32):
    """Custom type bcastStormOctetRateLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_BcastStormOctetRateLevel_Type.__name__ = "Integer32"
_BcastStormOctetRateLevel_Object = MibTableColumn
bcastStormOctetRateLevel = _BcastStormOctetRateLevel_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 11, 1, 1, 5),
    _BcastStormOctetRateLevel_Type()
)
bcastStormOctetRateLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcastStormOctetRateLevel.setStatus("current")
_VlanMgt_ObjectIdentity = ObjectIdentity
vlanMgt = _VlanMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 12)
)
_VlanTable_Object = MibTable
vlanTable = _VlanTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 12, 1)
)
if mibBuilder.loadTexts:
    vlanTable.setStatus("current")
_VlanEntry_Object = MibTableRow
vlanEntry = _VlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 12, 1, 1)
)
vlanEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "vlanIndex"),
)
if mibBuilder.loadTexts:
    vlanEntry.setStatus("current")
_VlanIndex_Type = Unsigned32
_VlanIndex_Object = MibTableColumn
vlanIndex = _VlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 12, 1, 1, 1),
    _VlanIndex_Type()
)
vlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vlanIndex.setStatus("current")


class _VlanAddressMethod_Type(Integer32):
    """Custom type vlanAddressMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bootp", 2),
          ("dhcp", 3),
          ("user", 1))
    )


_VlanAddressMethod_Type.__name__ = "Integer32"
_VlanAddressMethod_Object = MibTableColumn
vlanAddressMethod = _VlanAddressMethod_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 12, 1, 1, 2),
    _VlanAddressMethod_Type()
)
vlanAddressMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanAddressMethod.setStatus("current")
_VlanPortTable_Object = MibTable
vlanPortTable = _VlanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 12, 2)
)
if mibBuilder.loadTexts:
    vlanPortTable.setStatus("current")
_VlanPortEntry_Object = MibTableRow
vlanPortEntry = _VlanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 12, 2, 1)
)
vlanPortEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "vlanPortIndex"),
)
if mibBuilder.loadTexts:
    vlanPortEntry.setStatus("current")
_VlanPortIndex_Type = Integer32
_VlanPortIndex_Object = MibTableColumn
vlanPortIndex = _VlanPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 12, 2, 1, 1),
    _VlanPortIndex_Type()
)
vlanPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vlanPortIndex.setStatus("current")


class _VlanPortMode_Type(Integer32):
    """Custom type vlanPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("access", 3),
          ("dot1qTrunk", 2),
          ("hybrid", 1))
    )


_VlanPortMode_Type.__name__ = "Integer32"
_VlanPortMode_Object = MibTableColumn
vlanPortMode = _VlanPortMode_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 12, 2, 1, 2),
    _VlanPortMode_Type()
)
vlanPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPortMode.setStatus("current")


class _VlanPortPrivateVlanType_Type(Integer32):
    """Custom type vlanPortPrivateVlanType based on Integer32"""
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
        *(("community", 3),
          ("isolated", 2),
          ("normal", 1),
          ("promiscous", 4))
    )


_VlanPortPrivateVlanType_Type.__name__ = "Integer32"
_VlanPortPrivateVlanType_Object = MibTableColumn
vlanPortPrivateVlanType = _VlanPortPrivateVlanType_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 12, 2, 1, 3),
    _VlanPortPrivateVlanType_Type()
)
vlanPortPrivateVlanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPortPrivateVlanType.setStatus("current")
_PriorityMgt_ObjectIdentity = ObjectIdentity
priorityMgt = _PriorityMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 13)
)


class _PrioIpPrecDscpStatus_Type(Integer32):
    """Custom type prioIpPrecDscpStatus based on Integer32"""
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
        *(("disabled", 1),
          ("dscp", 3),
          ("precedence", 2),
          ("tos", 4))
    )


_PrioIpPrecDscpStatus_Type.__name__ = "Integer32"
_PrioIpPrecDscpStatus_Object = MibScalar
prioIpPrecDscpStatus = _PrioIpPrecDscpStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 13, 1),
    _PrioIpPrecDscpStatus_Type()
)
prioIpPrecDscpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioIpPrecDscpStatus.setStatus("current")
_PrioIpPrecTable_Object = MibTable
prioIpPrecTable = _PrioIpPrecTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 13, 2)
)
if mibBuilder.loadTexts:
    prioIpPrecTable.setStatus("current")
_PrioIpPrecEntry_Object = MibTableRow
prioIpPrecEntry = _PrioIpPrecEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 13, 2, 1)
)
prioIpPrecEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "prioIpPrecPort"),
    (0, "ES3526XA_ES3510-MIB", "prioIpPrecValue"),
)
if mibBuilder.loadTexts:
    prioIpPrecEntry.setStatus("current")
_PrioIpPrecPort_Type = Integer32
_PrioIpPrecPort_Object = MibTableColumn
prioIpPrecPort = _PrioIpPrecPort_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 13, 2, 1, 2),
    _PrioIpPrecPort_Type()
)
prioIpPrecPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prioIpPrecPort.setStatus("current")


class _PrioIpPrecValue_Type(Integer32):
    """Custom type prioIpPrecValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PrioIpPrecValue_Type.__name__ = "Integer32"
_PrioIpPrecValue_Object = MibTableColumn
prioIpPrecValue = _PrioIpPrecValue_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 13, 2, 1, 3),
    _PrioIpPrecValue_Type()
)
prioIpPrecValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prioIpPrecValue.setStatus("current")


class _PrioIpPrecCos_Type(Integer32):
    """Custom type prioIpPrecCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PrioIpPrecCos_Type.__name__ = "Integer32"
_PrioIpPrecCos_Object = MibTableColumn
prioIpPrecCos = _PrioIpPrecCos_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 13, 2, 1, 4),
    _PrioIpPrecCos_Type()
)
prioIpPrecCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioIpPrecCos.setStatus("current")
_PrioIpPrecRestoreDefault_Type = Integer32
_PrioIpPrecRestoreDefault_Object = MibScalar
prioIpPrecRestoreDefault = _PrioIpPrecRestoreDefault_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 13, 3),
    _PrioIpPrecRestoreDefault_Type()
)
prioIpPrecRestoreDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioIpPrecRestoreDefault.setStatus("current")
_PrioIpDscpTable_Object = MibTable
prioIpDscpTable = _PrioIpDscpTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 13, 4)
)
if mibBuilder.loadTexts:
    prioIpDscpTable.setStatus("current")
_PrioIpDscpEntry_Object = MibTableRow
prioIpDscpEntry = _PrioIpDscpEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 13, 4, 1)
)
prioIpDscpEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "prioIpDscpPort"),
    (0, "ES3526XA_ES3510-MIB", "prioIpDscpValue"),
)
if mibBuilder.loadTexts:
    prioIpDscpEntry.setStatus("current")
_PrioIpDscpPort_Type = Integer32
_PrioIpDscpPort_Object = MibTableColumn
prioIpDscpPort = _PrioIpDscpPort_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 13, 4, 1, 1),
    _PrioIpDscpPort_Type()
)
prioIpDscpPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prioIpDscpPort.setStatus("current")


class _PrioIpDscpValue_Type(Integer32):
    """Custom type prioIpDscpValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_PrioIpDscpValue_Type.__name__ = "Integer32"
_PrioIpDscpValue_Object = MibTableColumn
prioIpDscpValue = _PrioIpDscpValue_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 13, 4, 1, 2),
    _PrioIpDscpValue_Type()
)
prioIpDscpValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prioIpDscpValue.setStatus("current")


class _PrioIpDscpCos_Type(Integer32):
    """Custom type prioIpDscpCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PrioIpDscpCos_Type.__name__ = "Integer32"
_PrioIpDscpCos_Object = MibTableColumn
prioIpDscpCos = _PrioIpDscpCos_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 13, 4, 1, 3),
    _PrioIpDscpCos_Type()
)
prioIpDscpCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioIpDscpCos.setStatus("current")
_PrioIpDscpRestoreDefault_Type = Integer32
_PrioIpDscpRestoreDefault_Object = MibScalar
prioIpDscpRestoreDefault = _PrioIpDscpRestoreDefault_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 13, 5),
    _PrioIpDscpRestoreDefault_Type()
)
prioIpDscpRestoreDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioIpDscpRestoreDefault.setStatus("current")


class _PrioIpPortEnableStatus_Type(Integer32):
    """Custom type prioIpPortEnableStatus based on Integer32"""
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


_PrioIpPortEnableStatus_Type.__name__ = "Integer32"
_PrioIpPortEnableStatus_Object = MibScalar
prioIpPortEnableStatus = _PrioIpPortEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 13, 6),
    _PrioIpPortEnableStatus_Type()
)
prioIpPortEnableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioIpPortEnableStatus.setStatus("current")
_PrioIpPortTable_Object = MibTable
prioIpPortTable = _PrioIpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 13, 7)
)
if mibBuilder.loadTexts:
    prioIpPortTable.setStatus("current")
_PrioIpPortEntry_Object = MibTableRow
prioIpPortEntry = _PrioIpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 13, 7, 1)
)
prioIpPortEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "prioIpPortPhysPort"),
    (0, "ES3526XA_ES3510-MIB", "prioIpPortValue"),
)
if mibBuilder.loadTexts:
    prioIpPortEntry.setStatus("current")
_PrioIpPortPhysPort_Type = Integer32
_PrioIpPortPhysPort_Object = MibTableColumn
prioIpPortPhysPort = _PrioIpPortPhysPort_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 13, 7, 1, 1),
    _PrioIpPortPhysPort_Type()
)
prioIpPortPhysPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prioIpPortPhysPort.setStatus("current")


class _PrioIpPortValue_Type(Integer32):
    """Custom type prioIpPortValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PrioIpPortValue_Type.__name__ = "Integer32"
_PrioIpPortValue_Object = MibTableColumn
prioIpPortValue = _PrioIpPortValue_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 13, 7, 1, 2),
    _PrioIpPortValue_Type()
)
prioIpPortValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prioIpPortValue.setStatus("current")


class _PrioIpPortCos_Type(Integer32):
    """Custom type prioIpPortCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PrioIpPortCos_Type.__name__ = "Integer32"
_PrioIpPortCos_Object = MibTableColumn
prioIpPortCos = _PrioIpPortCos_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 13, 7, 1, 3),
    _PrioIpPortCos_Type()
)
prioIpPortCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prioIpPortCos.setStatus("current")


class _PrioIpPortStatus_Type(Integer32):
    """Custom type prioIpPortStatus based on Integer32"""
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


_PrioIpPortStatus_Type.__name__ = "Integer32"
_PrioIpPortStatus_Object = MibTableColumn
prioIpPortStatus = _PrioIpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 13, 7, 1, 4),
    _PrioIpPortStatus_Type()
)
prioIpPortStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prioIpPortStatus.setStatus("current")
_PrioCopy_ObjectIdentity = ObjectIdentity
prioCopy = _PrioCopy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 13, 8)
)
_PrioCopyIpPrec_Type = OctetString
_PrioCopyIpPrec_Object = MibScalar
prioCopyIpPrec = _PrioCopyIpPrec_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 13, 8, 1),
    _PrioCopyIpPrec_Type()
)
prioCopyIpPrec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioCopyIpPrec.setStatus("current")
_PrioCopyIpDscp_Type = OctetString
_PrioCopyIpDscp_Object = MibScalar
prioCopyIpDscp = _PrioCopyIpDscp_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 13, 8, 2),
    _PrioCopyIpDscp_Type()
)
prioCopyIpDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioCopyIpDscp.setStatus("current")
_PrioCopyIpPort_Type = OctetString
_PrioCopyIpPort_Object = MibScalar
prioCopyIpPort = _PrioCopyIpPort_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 13, 8, 3),
    _PrioCopyIpPort_Type()
)
prioCopyIpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioCopyIpPort.setStatus("current")
_PrioWrrTable_Object = MibTable
prioWrrTable = _PrioWrrTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 13, 9)
)
if mibBuilder.loadTexts:
    prioWrrTable.setStatus("current")
_PrioWrrEntry_Object = MibTableRow
prioWrrEntry = _PrioWrrEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 13, 9, 1)
)
prioWrrEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "prioWrrTrafficClass"),
)
if mibBuilder.loadTexts:
    prioWrrEntry.setStatus("current")


class _PrioWrrTrafficClass_Type(Integer32):
    """Custom type prioWrrTrafficClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PrioWrrTrafficClass_Type.__name__ = "Integer32"
_PrioWrrTrafficClass_Object = MibTableColumn
prioWrrTrafficClass = _PrioWrrTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 13, 9, 1, 1),
    _PrioWrrTrafficClass_Type()
)
prioWrrTrafficClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prioWrrTrafficClass.setStatus("current")


class _PrioWrrWeight_Type(Integer32):
    """Custom type prioWrrWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_PrioWrrWeight_Type.__name__ = "Integer32"
_PrioWrrWeight_Object = MibTableColumn
prioWrrWeight = _PrioWrrWeight_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 13, 9, 1, 2),
    _PrioWrrWeight_Type()
)
prioWrrWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioWrrWeight.setStatus("current")


class _PrioQueueMode_Type(Integer32):
    """Custom type prioQueueMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("hybrid", 4),
          ("strict", 2),
          ("wrr", 1))
    )


_PrioQueueMode_Type.__name__ = "Integer32"
_PrioQueueMode_Object = MibScalar
prioQueueMode = _PrioQueueMode_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 13, 10),
    _PrioQueueMode_Type()
)
prioQueueMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioQueueMode.setStatus("current")
_PrioIpTosTable_Object = MibTable
prioIpTosTable = _PrioIpTosTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 13, 11)
)
if mibBuilder.loadTexts:
    prioIpTosTable.setStatus("current")
_PrioIpTosEntry_Object = MibTableRow
prioIpTosEntry = _PrioIpTosEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 13, 11, 1)
)
prioIpTosEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "prioIpTosPort"),
    (0, "ES3526XA_ES3510-MIB", "prioIpTosValue"),
)
if mibBuilder.loadTexts:
    prioIpTosEntry.setStatus("current")
_PrioIpTosPort_Type = Integer32
_PrioIpTosPort_Object = MibTableColumn
prioIpTosPort = _PrioIpTosPort_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 13, 11, 1, 2),
    _PrioIpTosPort_Type()
)
prioIpTosPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prioIpTosPort.setStatus("current")


class _PrioIpTosValue_Type(Integer32):
    """Custom type prioIpTosValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PrioIpTosValue_Type.__name__ = "Integer32"
_PrioIpTosValue_Object = MibTableColumn
prioIpTosValue = _PrioIpTosValue_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 13, 11, 1, 3),
    _PrioIpTosValue_Type()
)
prioIpTosValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prioIpTosValue.setStatus("current")


class _PrioIpTosCos_Type(Integer32):
    """Custom type prioIpTosCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PrioIpTosCos_Type.__name__ = "Integer32"
_PrioIpTosCos_Object = MibTableColumn
prioIpTosCos = _PrioIpTosCos_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 13, 11, 1, 4),
    _PrioIpTosCos_Type()
)
prioIpTosCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioIpTosCos.setStatus("current")
_PrioIpTosRestoreDefault_Type = Integer32
_PrioIpTosRestoreDefault_Object = MibScalar
prioIpTosRestoreDefault = _PrioIpTosRestoreDefault_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 13, 12),
    _PrioIpTosRestoreDefault_Type()
)
prioIpTosRestoreDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioIpTosRestoreDefault.setStatus("current")
_TrapDestMgt_ObjectIdentity = ObjectIdentity
trapDestMgt = _TrapDestMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 14)
)
_TrapDestTable_Object = MibTable
trapDestTable = _TrapDestTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 14, 1)
)
if mibBuilder.loadTexts:
    trapDestTable.setStatus("current")
_TrapDestEntry_Object = MibTableRow
trapDestEntry = _TrapDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 14, 1, 1)
)
trapDestEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "trapDestAddress"),
)
if mibBuilder.loadTexts:
    trapDestEntry.setStatus("current")
_TrapDestAddress_Type = IpAddress
_TrapDestAddress_Object = MibTableColumn
trapDestAddress = _TrapDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 14, 1, 1, 1),
    _TrapDestAddress_Type()
)
trapDestAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapDestAddress.setStatus("current")


class _TrapDestCommunity_Type(OctetString):
    """Custom type trapDestCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TrapDestCommunity_Type.__name__ = "OctetString"
_TrapDestCommunity_Object = MibTableColumn
trapDestCommunity = _TrapDestCommunity_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 14, 1, 1, 2),
    _TrapDestCommunity_Type()
)
trapDestCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trapDestCommunity.setStatus("current")
_TrapDestStatus_Type = ValidStatus
_TrapDestStatus_Object = MibTableColumn
trapDestStatus = _TrapDestStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 14, 1, 1, 3),
    _TrapDestStatus_Type()
)
trapDestStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trapDestStatus.setStatus("current")


class _TrapDestVersion_Type(Integer32):
    """Custom type trapDestVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("version1", 1),
          ("version2", 2))
    )


_TrapDestVersion_Type.__name__ = "Integer32"
_TrapDestVersion_Object = MibTableColumn
trapDestVersion = _TrapDestVersion_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 14, 1, 1, 4),
    _TrapDestVersion_Type()
)
trapDestVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trapDestVersion.setStatus("current")


class _TrapDestUdpPort_Type(Integer32):
    """Custom type trapDestUdpPort based on Integer32"""
    defaultValue = 162

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TrapDestUdpPort_Type.__name__ = "Integer32"
_TrapDestUdpPort_Object = MibTableColumn
trapDestUdpPort = _TrapDestUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 14, 1, 1, 5),
    _TrapDestUdpPort_Type()
)
trapDestUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trapDestUdpPort.setStatus("current")
_QosMgt_ObjectIdentity = ObjectIdentity
qosMgt = _QosMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16)
)
_RateLimitMgt_ObjectIdentity = ObjectIdentity
rateLimitMgt = _RateLimitMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 1)
)
_RateLimitPortTable_Object = MibTable
rateLimitPortTable = _RateLimitPortTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 1, 2)
)
if mibBuilder.loadTexts:
    rateLimitPortTable.setStatus("current")
_RateLimitPortEntry_Object = MibTableRow
rateLimitPortEntry = _RateLimitPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 1, 2, 1)
)
rateLimitPortEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "rlPortIndex"),
)
if mibBuilder.loadTexts:
    rateLimitPortEntry.setStatus("current")
_RlPortIndex_Type = Integer32
_RlPortIndex_Object = MibTableColumn
rlPortIndex = _RlPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 1, 2, 1, 1),
    _RlPortIndex_Type()
)
rlPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlPortIndex.setStatus("current")
_RlPortInputStatus_Type = EnabledStatus
_RlPortInputStatus_Object = MibTableColumn
rlPortInputStatus = _RlPortInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 1, 2, 1, 6),
    _RlPortInputStatus_Type()
)
rlPortInputStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPortInputStatus.setStatus("current")
_RlPortOutputStatus_Type = EnabledStatus
_RlPortOutputStatus_Object = MibTableColumn
rlPortOutputStatus = _RlPortOutputStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 1, 2, 1, 7),
    _RlPortOutputStatus_Type()
)
rlPortOutputStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPortOutputStatus.setStatus("current")


class _RlPortInputLevel_Type(Integer32):
    """Custom type rlPortInputLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_RlPortInputLevel_Type.__name__ = "Integer32"
_RlPortInputLevel_Object = MibTableColumn
rlPortInputLevel = _RlPortInputLevel_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 1, 2, 1, 8),
    _RlPortInputLevel_Type()
)
rlPortInputLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPortInputLevel.setStatus("current")


class _RlPortInputScale_Type(Integer32):
    """Custom type rlPortInputScale based on Integer32"""
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
        *(("scale-100k", 2),
          ("scale-10k", 3),
          ("scale-10m", 0),
          ("scale-1k", 4),
          ("scale-1m", 1))
    )


_RlPortInputScale_Type.__name__ = "Integer32"
_RlPortInputScale_Object = MibTableColumn
rlPortInputScale = _RlPortInputScale_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 1, 2, 1, 9),
    _RlPortInputScale_Type()
)
rlPortInputScale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPortInputScale.setStatus("current")


class _RlPortOutputLevel_Type(Integer32):
    """Custom type rlPortOutputLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_RlPortOutputLevel_Type.__name__ = "Integer32"
_RlPortOutputLevel_Object = MibTableColumn
rlPortOutputLevel = _RlPortOutputLevel_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 1, 2, 1, 10),
    _RlPortOutputLevel_Type()
)
rlPortOutputLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPortOutputLevel.setStatus("current")


class _RlPortOutputScale_Type(Integer32):
    """Custom type rlPortOutputScale based on Integer32"""
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
        *(("scale-100k", 2),
          ("scale-10k", 3),
          ("scale-10m", 0),
          ("scale-1k", 4),
          ("scale-1m", 1))
    )


_RlPortOutputScale_Type.__name__ = "Integer32"
_RlPortOutputScale_Object = MibTableColumn
rlPortOutputScale = _RlPortOutputScale_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 1, 2, 1, 11),
    _RlPortOutputScale_Type()
)
rlPortOutputScale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPortOutputScale.setStatus("current")
_CosMgt_ObjectIdentity = ObjectIdentity
cosMgt = _CosMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 3)
)
_PrioAclToCosMappingTable_Object = MibTable
prioAclToCosMappingTable = _PrioAclToCosMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 3, 1)
)
if mibBuilder.loadTexts:
    prioAclToCosMappingTable.setStatus("current")
_PrioAclToCosMappingEntry_Object = MibTableRow
prioAclToCosMappingEntry = _PrioAclToCosMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 3, 1, 1)
)
prioAclToCosMappingEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "prioAclToCosMappingIfIndex"),
    (0, "ES3526XA_ES3510-MIB", "prioAclToCosMappingAclName"),
)
if mibBuilder.loadTexts:
    prioAclToCosMappingEntry.setStatus("current")
_PrioAclToCosMappingIfIndex_Type = Integer32
_PrioAclToCosMappingIfIndex_Object = MibTableColumn
prioAclToCosMappingIfIndex = _PrioAclToCosMappingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 3, 1, 1, 1),
    _PrioAclToCosMappingIfIndex_Type()
)
prioAclToCosMappingIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prioAclToCosMappingIfIndex.setStatus("current")


class _PrioAclToCosMappingAclName_Type(DisplayString):
    """Custom type prioAclToCosMappingAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_PrioAclToCosMappingAclName_Type.__name__ = "DisplayString"
_PrioAclToCosMappingAclName_Object = MibTableColumn
prioAclToCosMappingAclName = _PrioAclToCosMappingAclName_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 3, 1, 1, 2),
    _PrioAclToCosMappingAclName_Type()
)
prioAclToCosMappingAclName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prioAclToCosMappingAclName.setStatus("current")


class _PrioAclToCosMappingCosValue_Type(Integer32):
    """Custom type prioAclToCosMappingCosValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PrioAclToCosMappingCosValue_Type.__name__ = "Integer32"
_PrioAclToCosMappingCosValue_Object = MibTableColumn
prioAclToCosMappingCosValue = _PrioAclToCosMappingCosValue_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 3, 1, 1, 3),
    _PrioAclToCosMappingCosValue_Type()
)
prioAclToCosMappingCosValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prioAclToCosMappingCosValue.setStatus("current")
_PrioAclToCosMappingStatus_Type = RowStatus
_PrioAclToCosMappingStatus_Object = MibTableColumn
prioAclToCosMappingStatus = _PrioAclToCosMappingStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 3, 1, 1, 4),
    _PrioAclToCosMappingStatus_Type()
)
prioAclToCosMappingStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prioAclToCosMappingStatus.setStatus("current")
_DiffServMgt_ObjectIdentity = ObjectIdentity
diffServMgt = _DiffServMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4)
)
_DiffServPortTable_Object = MibTable
diffServPortTable = _DiffServPortTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 9)
)
if mibBuilder.loadTexts:
    diffServPortTable.setStatus("current")
_DiffServPortEntry_Object = MibTableRow
diffServPortEntry = _DiffServPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 9, 1)
)
diffServPortEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "diffServPortIfIndex"),
)
if mibBuilder.loadTexts:
    diffServPortEntry.setStatus("current")
_DiffServPortIfIndex_Type = Integer32
_DiffServPortIfIndex_Object = MibTableColumn
diffServPortIfIndex = _DiffServPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 9, 1, 1),
    _DiffServPortIfIndex_Type()
)
diffServPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServPortIfIndex.setStatus("current")
_DiffServPortPolicyMapIndex_Type = Integer32
_DiffServPortPolicyMapIndex_Object = MibTableColumn
diffServPortPolicyMapIndex = _DiffServPortPolicyMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 9, 1, 2),
    _DiffServPortPolicyMapIndex_Type()
)
diffServPortPolicyMapIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffServPortPolicyMapIndex.setStatus("current")
_DiffServPortIngressIpAclIndex_Type = Integer32
_DiffServPortIngressIpAclIndex_Object = MibTableColumn
diffServPortIngressIpAclIndex = _DiffServPortIngressIpAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 9, 1, 3),
    _DiffServPortIngressIpAclIndex_Type()
)
diffServPortIngressIpAclIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffServPortIngressIpAclIndex.setStatus("current")
_DiffServPortIngressMacAclIndex_Type = Integer32
_DiffServPortIngressMacAclIndex_Object = MibTableColumn
diffServPortIngressMacAclIndex = _DiffServPortIngressMacAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 9, 1, 4),
    _DiffServPortIngressMacAclIndex_Type()
)
diffServPortIngressMacAclIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffServPortIngressMacAclIndex.setStatus("current")
_DiffServPolicyMapTable_Object = MibTable
diffServPolicyMapTable = _DiffServPolicyMapTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 10)
)
if mibBuilder.loadTexts:
    diffServPolicyMapTable.setStatus("current")
_DiffServPolicyMapEntry_Object = MibTableRow
diffServPolicyMapEntry = _DiffServPolicyMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 10, 1)
)
diffServPolicyMapEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "diffServPolicyMapIndex"),
)
if mibBuilder.loadTexts:
    diffServPolicyMapEntry.setStatus("current")
_DiffServPolicyMapIndex_Type = Integer32
_DiffServPolicyMapIndex_Object = MibTableColumn
diffServPolicyMapIndex = _DiffServPolicyMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 10, 1, 1),
    _DiffServPolicyMapIndex_Type()
)
diffServPolicyMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServPolicyMapIndex.setStatus("current")


class _DiffServPolicyMapName_Type(DisplayString):
    """Custom type diffServPolicyMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_DiffServPolicyMapName_Type.__name__ = "DisplayString"
_DiffServPolicyMapName_Object = MibTableColumn
diffServPolicyMapName = _DiffServPolicyMapName_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 10, 1, 2),
    _DiffServPolicyMapName_Type()
)
diffServPolicyMapName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServPolicyMapName.setStatus("current")


class _DiffServPolicyMapDescription_Type(DisplayString):
    """Custom type diffServPolicyMapDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_DiffServPolicyMapDescription_Type.__name__ = "DisplayString"
_DiffServPolicyMapDescription_Object = MibTableColumn
diffServPolicyMapDescription = _DiffServPolicyMapDescription_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 10, 1, 3),
    _DiffServPolicyMapDescription_Type()
)
diffServPolicyMapDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServPolicyMapDescription.setStatus("current")


class _DiffServPolicyMapElementIndexList_Type(OctetString):
    """Custom type diffServPolicyMapElementIndexList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DiffServPolicyMapElementIndexList_Type.__name__ = "OctetString"
_DiffServPolicyMapElementIndexList_Object = MibTableColumn
diffServPolicyMapElementIndexList = _DiffServPolicyMapElementIndexList_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 10, 1, 4),
    _DiffServPolicyMapElementIndexList_Type()
)
diffServPolicyMapElementIndexList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServPolicyMapElementIndexList.setStatus("current")
_DiffServPolicyMapStatus_Type = RowStatus
_DiffServPolicyMapStatus_Object = MibTableColumn
diffServPolicyMapStatus = _DiffServPolicyMapStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 10, 1, 5),
    _DiffServPolicyMapStatus_Type()
)
diffServPolicyMapStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServPolicyMapStatus.setStatus("current")
_DiffServPolicyMapAttachCtl_ObjectIdentity = ObjectIdentity
diffServPolicyMapAttachCtl = _DiffServPolicyMapAttachCtl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 11)
)
_DiffServPolicyMapAttachCtlIndex_Type = Integer32
_DiffServPolicyMapAttachCtlIndex_Object = MibScalar
diffServPolicyMapAttachCtlIndex = _DiffServPolicyMapAttachCtlIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 11, 1),
    _DiffServPolicyMapAttachCtlIndex_Type()
)
diffServPolicyMapAttachCtlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffServPolicyMapAttachCtlIndex.setStatus("current")
_DiffServPolicyMapAttachCtlElementIndex_Type = Integer32
_DiffServPolicyMapAttachCtlElementIndex_Object = MibScalar
diffServPolicyMapAttachCtlElementIndex = _DiffServPolicyMapAttachCtlElementIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 11, 2),
    _DiffServPolicyMapAttachCtlElementIndex_Type()
)
diffServPolicyMapAttachCtlElementIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffServPolicyMapAttachCtlElementIndex.setStatus("current")


class _DiffServPolicyMapAttachCtlAction_Type(Integer32):
    """Custom type diffServPolicyMapAttachCtlAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("attach", 2),
          ("detach", 3),
          ("noAction", 1))
    )


_DiffServPolicyMapAttachCtlAction_Type.__name__ = "Integer32"
_DiffServPolicyMapAttachCtlAction_Object = MibScalar
diffServPolicyMapAttachCtlAction = _DiffServPolicyMapAttachCtlAction_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 11, 3),
    _DiffServPolicyMapAttachCtlAction_Type()
)
diffServPolicyMapAttachCtlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffServPolicyMapAttachCtlAction.setStatus("current")
_DiffServPolicyMapElementTable_Object = MibTable
diffServPolicyMapElementTable = _DiffServPolicyMapElementTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 12)
)
if mibBuilder.loadTexts:
    diffServPolicyMapElementTable.setStatus("current")
_DiffServPolicyMapElementEntry_Object = MibTableRow
diffServPolicyMapElementEntry = _DiffServPolicyMapElementEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 12, 1)
)
diffServPolicyMapElementEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "diffServPolicyMapElementIndex"),
)
if mibBuilder.loadTexts:
    diffServPolicyMapElementEntry.setStatus("current")
_DiffServPolicyMapElementIndex_Type = Integer32
_DiffServPolicyMapElementIndex_Object = MibTableColumn
diffServPolicyMapElementIndex = _DiffServPolicyMapElementIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 12, 1, 1),
    _DiffServPolicyMapElementIndex_Type()
)
diffServPolicyMapElementIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServPolicyMapElementIndex.setStatus("current")


class _DiffServPolicyMapElementClassMapIndex_Type(Integer32):
    """Custom type diffServPolicyMapElementClassMapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DiffServPolicyMapElementClassMapIndex_Type.__name__ = "Integer32"
_DiffServPolicyMapElementClassMapIndex_Object = MibTableColumn
diffServPolicyMapElementClassMapIndex = _DiffServPolicyMapElementClassMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 12, 1, 2),
    _DiffServPolicyMapElementClassMapIndex_Type()
)
diffServPolicyMapElementClassMapIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServPolicyMapElementClassMapIndex.setStatus("current")
_DiffServPolicyMapElementMeterIndex_Type = Integer32
_DiffServPolicyMapElementMeterIndex_Object = MibTableColumn
diffServPolicyMapElementMeterIndex = _DiffServPolicyMapElementMeterIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 12, 1, 3),
    _DiffServPolicyMapElementMeterIndex_Type()
)
diffServPolicyMapElementMeterIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServPolicyMapElementMeterIndex.setStatus("current")


class _DiffServPolicyMapElementActionIndex_Type(Integer32):
    """Custom type diffServPolicyMapElementActionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DiffServPolicyMapElementActionIndex_Type.__name__ = "Integer32"
_DiffServPolicyMapElementActionIndex_Object = MibTableColumn
diffServPolicyMapElementActionIndex = _DiffServPolicyMapElementActionIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 12, 1, 4),
    _DiffServPolicyMapElementActionIndex_Type()
)
diffServPolicyMapElementActionIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServPolicyMapElementActionIndex.setStatus("current")
_DiffServPolicyMapElementStatus_Type = RowStatus
_DiffServPolicyMapElementStatus_Object = MibTableColumn
diffServPolicyMapElementStatus = _DiffServPolicyMapElementStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 12, 1, 5),
    _DiffServPolicyMapElementStatus_Type()
)
diffServPolicyMapElementStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServPolicyMapElementStatus.setStatus("current")
_DiffServClassMapTable_Object = MibTable
diffServClassMapTable = _DiffServClassMapTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 13)
)
if mibBuilder.loadTexts:
    diffServClassMapTable.setStatus("current")
_DiffServClassMapEntry_Object = MibTableRow
diffServClassMapEntry = _DiffServClassMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 13, 1)
)
diffServClassMapEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "diffServClassMapIndex"),
)
if mibBuilder.loadTexts:
    diffServClassMapEntry.setStatus("current")
_DiffServClassMapIndex_Type = Integer32
_DiffServClassMapIndex_Object = MibTableColumn
diffServClassMapIndex = _DiffServClassMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 13, 1, 1),
    _DiffServClassMapIndex_Type()
)
diffServClassMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServClassMapIndex.setStatus("current")


class _DiffServClassMapName_Type(DisplayString):
    """Custom type diffServClassMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_DiffServClassMapName_Type.__name__ = "DisplayString"
_DiffServClassMapName_Object = MibTableColumn
diffServClassMapName = _DiffServClassMapName_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 13, 1, 2),
    _DiffServClassMapName_Type()
)
diffServClassMapName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServClassMapName.setStatus("current")


class _DiffServClassMapDescription_Type(DisplayString):
    """Custom type diffServClassMapDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_DiffServClassMapDescription_Type.__name__ = "DisplayString"
_DiffServClassMapDescription_Object = MibTableColumn
diffServClassMapDescription = _DiffServClassMapDescription_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 13, 1, 3),
    _DiffServClassMapDescription_Type()
)
diffServClassMapDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServClassMapDescription.setStatus("current")


class _DiffServClassMapMatchType_Type(Integer32):
    """Custom type diffServClassMapMatchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("matchAll", 2),
          ("matchAny", 1))
    )


_DiffServClassMapMatchType_Type.__name__ = "Integer32"
_DiffServClassMapMatchType_Object = MibTableColumn
diffServClassMapMatchType = _DiffServClassMapMatchType_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 13, 1, 4),
    _DiffServClassMapMatchType_Type()
)
diffServClassMapMatchType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServClassMapMatchType.setStatus("current")


class _DiffServClassMapElementIndexTypeList_Type(OctetString):
    """Custom type diffServClassMapElementIndexTypeList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DiffServClassMapElementIndexTypeList_Type.__name__ = "OctetString"
_DiffServClassMapElementIndexTypeList_Object = MibTableColumn
diffServClassMapElementIndexTypeList = _DiffServClassMapElementIndexTypeList_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 13, 1, 5),
    _DiffServClassMapElementIndexTypeList_Type()
)
diffServClassMapElementIndexTypeList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServClassMapElementIndexTypeList.setStatus("current")


class _DiffServClassMapElementIndexList_Type(OctetString):
    """Custom type diffServClassMapElementIndexList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DiffServClassMapElementIndexList_Type.__name__ = "OctetString"
_DiffServClassMapElementIndexList_Object = MibTableColumn
diffServClassMapElementIndexList = _DiffServClassMapElementIndexList_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 13, 1, 6),
    _DiffServClassMapElementIndexList_Type()
)
diffServClassMapElementIndexList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServClassMapElementIndexList.setStatus("current")
_DiffServClassMapStatus_Type = RowStatus
_DiffServClassMapStatus_Object = MibTableColumn
diffServClassMapStatus = _DiffServClassMapStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 13, 1, 7),
    _DiffServClassMapStatus_Type()
)
diffServClassMapStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServClassMapStatus.setStatus("current")
_DiffServClassMapAttachCtl_ObjectIdentity = ObjectIdentity
diffServClassMapAttachCtl = _DiffServClassMapAttachCtl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 14)
)
_DiffServClassMapAttachCtlIndex_Type = Integer32
_DiffServClassMapAttachCtlIndex_Object = MibScalar
diffServClassMapAttachCtlIndex = _DiffServClassMapAttachCtlIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 14, 1),
    _DiffServClassMapAttachCtlIndex_Type()
)
diffServClassMapAttachCtlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffServClassMapAttachCtlIndex.setStatus("current")


class _DiffServClassMapAttachCtlElementIndexType_Type(Integer32):
    """Custom type diffServClassMapAttachCtlElementIndexType based on Integer32"""
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
        *(("acl", 3),
          ("ipAce", 2),
          ("ipv6Ace", 4),
          ("macAce", 1))
    )


_DiffServClassMapAttachCtlElementIndexType_Type.__name__ = "Integer32"
_DiffServClassMapAttachCtlElementIndexType_Object = MibScalar
diffServClassMapAttachCtlElementIndexType = _DiffServClassMapAttachCtlElementIndexType_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 14, 2),
    _DiffServClassMapAttachCtlElementIndexType_Type()
)
diffServClassMapAttachCtlElementIndexType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffServClassMapAttachCtlElementIndexType.setStatus("current")
_DiffServClassMapAttachCtlElementIndex_Type = Integer32
_DiffServClassMapAttachCtlElementIndex_Object = MibScalar
diffServClassMapAttachCtlElementIndex = _DiffServClassMapAttachCtlElementIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 14, 3),
    _DiffServClassMapAttachCtlElementIndex_Type()
)
diffServClassMapAttachCtlElementIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffServClassMapAttachCtlElementIndex.setStatus("current")


class _DiffServClassMapAttachCtlAction_Type(Integer32):
    """Custom type diffServClassMapAttachCtlAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("attach", 2),
          ("detach", 3),
          ("noAction", 1))
    )


_DiffServClassMapAttachCtlAction_Type.__name__ = "Integer32"
_DiffServClassMapAttachCtlAction_Object = MibScalar
diffServClassMapAttachCtlAction = _DiffServClassMapAttachCtlAction_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 14, 4),
    _DiffServClassMapAttachCtlAction_Type()
)
diffServClassMapAttachCtlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffServClassMapAttachCtlAction.setStatus("current")
_DiffServAclTable_Object = MibTable
diffServAclTable = _DiffServAclTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 15)
)
if mibBuilder.loadTexts:
    diffServAclTable.setStatus("current")
_DiffServAclEntry_Object = MibTableRow
diffServAclEntry = _DiffServAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 15, 1)
)
diffServAclEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "diffServAclIndex"),
)
if mibBuilder.loadTexts:
    diffServAclEntry.setStatus("current")
_DiffServAclIndex_Type = Integer32
_DiffServAclIndex_Object = MibTableColumn
diffServAclIndex = _DiffServAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 15, 1, 1),
    _DiffServAclIndex_Type()
)
diffServAclIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServAclIndex.setStatus("current")


class _DiffServAclName_Type(DisplayString):
    """Custom type diffServAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_DiffServAclName_Type.__name__ = "DisplayString"
_DiffServAclName_Object = MibTableColumn
diffServAclName = _DiffServAclName_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 15, 1, 2),
    _DiffServAclName_Type()
)
diffServAclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServAclName.setStatus("current")


class _DiffServAclType_Type(Integer32):
    """Custom type diffServAclType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ipextended", 3),
          ("ipstandard", 2),
          ("mac", 1))
    )


_DiffServAclType_Type.__name__ = "Integer32"
_DiffServAclType_Object = MibTableColumn
diffServAclType = _DiffServAclType_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 15, 1, 3),
    _DiffServAclType_Type()
)
diffServAclType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServAclType.setStatus("current")


class _DiffServAclAceIndexList_Type(OctetString):
    """Custom type diffServAclAceIndexList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DiffServAclAceIndexList_Type.__name__ = "OctetString"
_DiffServAclAceIndexList_Object = MibTableColumn
diffServAclAceIndexList = _DiffServAclAceIndexList_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 15, 1, 4),
    _DiffServAclAceIndexList_Type()
)
diffServAclAceIndexList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServAclAceIndexList.setStatus("current")
_DiffServAclStatus_Type = RowStatus
_DiffServAclStatus_Object = MibTableColumn
diffServAclStatus = _DiffServAclStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 15, 1, 5),
    _DiffServAclStatus_Type()
)
diffServAclStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServAclStatus.setStatus("current")
_DiffServAclAttachCtl_ObjectIdentity = ObjectIdentity
diffServAclAttachCtl = _DiffServAclAttachCtl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 16)
)
_DiffServAclAttachCtlIndex_Type = Integer32
_DiffServAclAttachCtlIndex_Object = MibScalar
diffServAclAttachCtlIndex = _DiffServAclAttachCtlIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 16, 1),
    _DiffServAclAttachCtlIndex_Type()
)
diffServAclAttachCtlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffServAclAttachCtlIndex.setStatus("current")


class _DiffServAclAttachCtlAceType_Type(Integer32):
    """Custom type diffServAclAttachCtlAceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipAce", 2),
          ("macAce", 1))
    )


_DiffServAclAttachCtlAceType_Type.__name__ = "Integer32"
_DiffServAclAttachCtlAceType_Object = MibScalar
diffServAclAttachCtlAceType = _DiffServAclAttachCtlAceType_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 16, 2),
    _DiffServAclAttachCtlAceType_Type()
)
diffServAclAttachCtlAceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffServAclAttachCtlAceType.setStatus("current")
_DiffServAclAttachCtlAceIndex_Type = Integer32
_DiffServAclAttachCtlAceIndex_Object = MibScalar
diffServAclAttachCtlAceIndex = _DiffServAclAttachCtlAceIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 16, 3),
    _DiffServAclAttachCtlAceIndex_Type()
)
diffServAclAttachCtlAceIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffServAclAttachCtlAceIndex.setStatus("current")


class _DiffServAclAttachCtlAction_Type(Integer32):
    """Custom type diffServAclAttachCtlAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("attach", 2),
          ("detach", 3),
          ("noAction", 1))
    )


_DiffServAclAttachCtlAction_Type.__name__ = "Integer32"
_DiffServAclAttachCtlAction_Object = MibScalar
diffServAclAttachCtlAction = _DiffServAclAttachCtlAction_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 16, 4),
    _DiffServAclAttachCtlAction_Type()
)
diffServAclAttachCtlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffServAclAttachCtlAction.setStatus("current")
_DiffServIpAceTable_Object = MibTable
diffServIpAceTable = _DiffServIpAceTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 17)
)
if mibBuilder.loadTexts:
    diffServIpAceTable.setStatus("current")
_DiffServIpAceEntry_Object = MibTableRow
diffServIpAceEntry = _DiffServIpAceEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 17, 1)
)
diffServIpAceEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "diffServIpAceIndex"),
)
if mibBuilder.loadTexts:
    diffServIpAceEntry.setStatus("current")
_DiffServIpAceIndex_Type = Integer32
_DiffServIpAceIndex_Object = MibTableColumn
diffServIpAceIndex = _DiffServIpAceIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 17, 1, 1),
    _DiffServIpAceIndex_Type()
)
diffServIpAceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServIpAceIndex.setStatus("current")


class _DiffServIpAceType_Type(Integer32):
    """Custom type diffServIpAceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("extended", 2),
          ("standard", 1))
    )


_DiffServIpAceType_Type.__name__ = "Integer32"
_DiffServIpAceType_Object = MibTableColumn
diffServIpAceType = _DiffServIpAceType_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 17, 1, 2),
    _DiffServIpAceType_Type()
)
diffServIpAceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpAceType.setStatus("current")


class _DiffServIpAceAccess_Type(Integer32):
    """Custom type diffServIpAceAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )


_DiffServIpAceAccess_Type.__name__ = "Integer32"
_DiffServIpAceAccess_Object = MibTableColumn
diffServIpAceAccess = _DiffServIpAceAccess_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 17, 1, 3),
    _DiffServIpAceAccess_Type()
)
diffServIpAceAccess.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpAceAccess.setStatus("current")
_DiffServIpAceSourceIpAddr_Type = Integer32
_DiffServIpAceSourceIpAddr_Object = MibTableColumn
diffServIpAceSourceIpAddr = _DiffServIpAceSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 17, 1, 4),
    _DiffServIpAceSourceIpAddr_Type()
)
diffServIpAceSourceIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpAceSourceIpAddr.setStatus("current")
_DiffServIpAceSourceIpAddrBitmask_Type = Integer32
_DiffServIpAceSourceIpAddrBitmask_Object = MibTableColumn
diffServIpAceSourceIpAddrBitmask = _DiffServIpAceSourceIpAddrBitmask_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 17, 1, 5),
    _DiffServIpAceSourceIpAddrBitmask_Type()
)
diffServIpAceSourceIpAddrBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpAceSourceIpAddrBitmask.setStatus("current")
_DiffServIpAceDestIpAddr_Type = Integer32
_DiffServIpAceDestIpAddr_Object = MibTableColumn
diffServIpAceDestIpAddr = _DiffServIpAceDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 17, 1, 6),
    _DiffServIpAceDestIpAddr_Type()
)
diffServIpAceDestIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpAceDestIpAddr.setStatus("current")
_DiffServIpAceDestIpAddrBitmask_Type = Integer32
_DiffServIpAceDestIpAddrBitmask_Object = MibTableColumn
diffServIpAceDestIpAddrBitmask = _DiffServIpAceDestIpAddrBitmask_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 17, 1, 7),
    _DiffServIpAceDestIpAddrBitmask_Type()
)
diffServIpAceDestIpAddrBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpAceDestIpAddrBitmask.setStatus("current")


class _DiffServIpAceProtocol_Type(Integer32):
    """Custom type diffServIpAceProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_DiffServIpAceProtocol_Type.__name__ = "Integer32"
_DiffServIpAceProtocol_Object = MibTableColumn
diffServIpAceProtocol = _DiffServIpAceProtocol_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 17, 1, 8),
    _DiffServIpAceProtocol_Type()
)
diffServIpAceProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpAceProtocol.setStatus("current")


class _DiffServIpAcePrec_Type(Integer32):
    """Custom type diffServIpAcePrec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_DiffServIpAcePrec_Type.__name__ = "Integer32"
_DiffServIpAcePrec_Object = MibTableColumn
diffServIpAcePrec = _DiffServIpAcePrec_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 17, 1, 9),
    _DiffServIpAcePrec_Type()
)
diffServIpAcePrec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpAcePrec.setStatus("current")


class _DiffServIpAceTos_Type(Integer32):
    """Custom type diffServIpAceTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_DiffServIpAceTos_Type.__name__ = "Integer32"
_DiffServIpAceTos_Object = MibTableColumn
diffServIpAceTos = _DiffServIpAceTos_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 17, 1, 10),
    _DiffServIpAceTos_Type()
)
diffServIpAceTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpAceTos.setStatus("current")


class _DiffServIpAceDscp_Type(Integer32):
    """Custom type diffServIpAceDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_DiffServIpAceDscp_Type.__name__ = "Integer32"
_DiffServIpAceDscp_Object = MibTableColumn
diffServIpAceDscp = _DiffServIpAceDscp_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 17, 1, 11),
    _DiffServIpAceDscp_Type()
)
diffServIpAceDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpAceDscp.setStatus("current")


class _DiffServIpAceSourcePortOp_Type(Integer32):
    """Custom type diffServIpAceSourcePortOp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("equal", 2),
          ("noOperator", 1),
          ("range", 3))
    )


_DiffServIpAceSourcePortOp_Type.__name__ = "Integer32"
_DiffServIpAceSourcePortOp_Object = MibTableColumn
diffServIpAceSourcePortOp = _DiffServIpAceSourcePortOp_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 17, 1, 12),
    _DiffServIpAceSourcePortOp_Type()
)
diffServIpAceSourcePortOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpAceSourcePortOp.setStatus("current")


class _DiffServIpAceMinSourcePort_Type(Integer32):
    """Custom type diffServIpAceMinSourcePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DiffServIpAceMinSourcePort_Type.__name__ = "Integer32"
_DiffServIpAceMinSourcePort_Object = MibTableColumn
diffServIpAceMinSourcePort = _DiffServIpAceMinSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 17, 1, 13),
    _DiffServIpAceMinSourcePort_Type()
)
diffServIpAceMinSourcePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpAceMinSourcePort.setStatus("current")


class _DiffServIpAceMaxSourcePort_Type(Integer32):
    """Custom type diffServIpAceMaxSourcePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DiffServIpAceMaxSourcePort_Type.__name__ = "Integer32"
_DiffServIpAceMaxSourcePort_Object = MibTableColumn
diffServIpAceMaxSourcePort = _DiffServIpAceMaxSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 17, 1, 14),
    _DiffServIpAceMaxSourcePort_Type()
)
diffServIpAceMaxSourcePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpAceMaxSourcePort.setStatus("current")


class _DiffServIpAceSourcePortBitmask_Type(Integer32):
    """Custom type diffServIpAceSourcePortBitmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DiffServIpAceSourcePortBitmask_Type.__name__ = "Integer32"
_DiffServIpAceSourcePortBitmask_Object = MibTableColumn
diffServIpAceSourcePortBitmask = _DiffServIpAceSourcePortBitmask_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 17, 1, 15),
    _DiffServIpAceSourcePortBitmask_Type()
)
diffServIpAceSourcePortBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpAceSourcePortBitmask.setStatus("current")


class _DiffServIpAceDestPortOp_Type(Integer32):
    """Custom type diffServIpAceDestPortOp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("equal", 2),
          ("noOperator", 1),
          ("range", 3))
    )


_DiffServIpAceDestPortOp_Type.__name__ = "Integer32"
_DiffServIpAceDestPortOp_Object = MibTableColumn
diffServIpAceDestPortOp = _DiffServIpAceDestPortOp_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 17, 1, 16),
    _DiffServIpAceDestPortOp_Type()
)
diffServIpAceDestPortOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpAceDestPortOp.setStatus("current")


class _DiffServIpAceMinDestPort_Type(Integer32):
    """Custom type diffServIpAceMinDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DiffServIpAceMinDestPort_Type.__name__ = "Integer32"
_DiffServIpAceMinDestPort_Object = MibTableColumn
diffServIpAceMinDestPort = _DiffServIpAceMinDestPort_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 17, 1, 17),
    _DiffServIpAceMinDestPort_Type()
)
diffServIpAceMinDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpAceMinDestPort.setStatus("current")


class _DiffServIpAceMaxDestPort_Type(Integer32):
    """Custom type diffServIpAceMaxDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DiffServIpAceMaxDestPort_Type.__name__ = "Integer32"
_DiffServIpAceMaxDestPort_Object = MibTableColumn
diffServIpAceMaxDestPort = _DiffServIpAceMaxDestPort_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 17, 1, 18),
    _DiffServIpAceMaxDestPort_Type()
)
diffServIpAceMaxDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpAceMaxDestPort.setStatus("current")


class _DiffServIpAceDestPortBitmask_Type(Integer32):
    """Custom type diffServIpAceDestPortBitmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DiffServIpAceDestPortBitmask_Type.__name__ = "Integer32"
_DiffServIpAceDestPortBitmask_Object = MibTableColumn
diffServIpAceDestPortBitmask = _DiffServIpAceDestPortBitmask_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 17, 1, 19),
    _DiffServIpAceDestPortBitmask_Type()
)
diffServIpAceDestPortBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpAceDestPortBitmask.setStatus("current")


class _DiffServIpAceControlCode_Type(Integer32):
    """Custom type diffServIpAceControlCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_DiffServIpAceControlCode_Type.__name__ = "Integer32"
_DiffServIpAceControlCode_Object = MibTableColumn
diffServIpAceControlCode = _DiffServIpAceControlCode_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 17, 1, 20),
    _DiffServIpAceControlCode_Type()
)
diffServIpAceControlCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpAceControlCode.setStatus("current")


class _DiffServIpAceControlCodeBitmask_Type(Integer32):
    """Custom type diffServIpAceControlCodeBitmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_DiffServIpAceControlCodeBitmask_Type.__name__ = "Integer32"
_DiffServIpAceControlCodeBitmask_Object = MibTableColumn
diffServIpAceControlCodeBitmask = _DiffServIpAceControlCodeBitmask_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 17, 1, 21),
    _DiffServIpAceControlCodeBitmask_Type()
)
diffServIpAceControlCodeBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpAceControlCodeBitmask.setStatus("current")
_DiffServIpAceStatus_Type = RowStatus
_DiffServIpAceStatus_Object = MibTableColumn
diffServIpAceStatus = _DiffServIpAceStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 17, 1, 22),
    _DiffServIpAceStatus_Type()
)
diffServIpAceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpAceStatus.setStatus("current")
_DiffServMacAceTable_Object = MibTable
diffServMacAceTable = _DiffServMacAceTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 18)
)
if mibBuilder.loadTexts:
    diffServMacAceTable.setStatus("current")
_DiffServMacAceEntry_Object = MibTableRow
diffServMacAceEntry = _DiffServMacAceEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 18, 1)
)
diffServMacAceEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "diffServMacAceIndex"),
)
if mibBuilder.loadTexts:
    diffServMacAceEntry.setStatus("current")
_DiffServMacAceIndex_Type = Integer32
_DiffServMacAceIndex_Object = MibTableColumn
diffServMacAceIndex = _DiffServMacAceIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 18, 1, 1),
    _DiffServMacAceIndex_Type()
)
diffServMacAceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServMacAceIndex.setStatus("current")


class _DiffServMacAceAccess_Type(Integer32):
    """Custom type diffServMacAceAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )


_DiffServMacAceAccess_Type.__name__ = "Integer32"
_DiffServMacAceAccess_Object = MibTableColumn
diffServMacAceAccess = _DiffServMacAceAccess_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 18, 1, 2),
    _DiffServMacAceAccess_Type()
)
diffServMacAceAccess.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMacAceAccess.setStatus("current")


class _DiffServMacAcePktformat_Type(Integer32):
    """Custom type diffServMacAcePktformat based on Integer32"""
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
        *(("any", 1),
          ("tagged802Dot3", 5),
          ("tagggedEth2", 4),
          ("untagged-Eth2", 2),
          ("untagged802Dot3", 3))
    )


_DiffServMacAcePktformat_Type.__name__ = "Integer32"
_DiffServMacAcePktformat_Object = MibTableColumn
diffServMacAcePktformat = _DiffServMacAcePktformat_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 18, 1, 3),
    _DiffServMacAcePktformat_Type()
)
diffServMacAcePktformat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMacAcePktformat.setStatus("current")
_DiffServMacAceSourceMacAddr_Type = MacAddress
_DiffServMacAceSourceMacAddr_Object = MibTableColumn
diffServMacAceSourceMacAddr = _DiffServMacAceSourceMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 18, 1, 4),
    _DiffServMacAceSourceMacAddr_Type()
)
diffServMacAceSourceMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMacAceSourceMacAddr.setStatus("current")
_DiffServMacAceSourceMacAddrBitmask_Type = MacAddress
_DiffServMacAceSourceMacAddrBitmask_Object = MibTableColumn
diffServMacAceSourceMacAddrBitmask = _DiffServMacAceSourceMacAddrBitmask_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 18, 1, 5),
    _DiffServMacAceSourceMacAddrBitmask_Type()
)
diffServMacAceSourceMacAddrBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMacAceSourceMacAddrBitmask.setStatus("current")
_DiffServMacAceDestMacAddr_Type = MacAddress
_DiffServMacAceDestMacAddr_Object = MibTableColumn
diffServMacAceDestMacAddr = _DiffServMacAceDestMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 18, 1, 6),
    _DiffServMacAceDestMacAddr_Type()
)
diffServMacAceDestMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMacAceDestMacAddr.setStatus("current")
_DiffServMacAceDestMacAddrBitmask_Type = MacAddress
_DiffServMacAceDestMacAddrBitmask_Object = MibTableColumn
diffServMacAceDestMacAddrBitmask = _DiffServMacAceDestMacAddrBitmask_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 18, 1, 7),
    _DiffServMacAceDestMacAddrBitmask_Type()
)
diffServMacAceDestMacAddrBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMacAceDestMacAddrBitmask.setStatus("current")


class _DiffServMacAceVidOp_Type(Integer32):
    """Custom type diffServMacAceVidOp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("equal", 2),
          ("noOperator", 1),
          ("range", 3))
    )


_DiffServMacAceVidOp_Type.__name__ = "Integer32"
_DiffServMacAceVidOp_Object = MibTableColumn
diffServMacAceVidOp = _DiffServMacAceVidOp_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 18, 1, 8),
    _DiffServMacAceVidOp_Type()
)
diffServMacAceVidOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMacAceVidOp.setStatus("current")


class _DiffServMacAceMinVid_Type(Integer32):
    """Custom type diffServMacAceMinVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_DiffServMacAceMinVid_Type.__name__ = "Integer32"
_DiffServMacAceMinVid_Object = MibTableColumn
diffServMacAceMinVid = _DiffServMacAceMinVid_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 18, 1, 9),
    _DiffServMacAceMinVid_Type()
)
diffServMacAceMinVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMacAceMinVid.setStatus("current")


class _DiffServMacAceVidBitmask_Type(Integer32):
    """Custom type diffServMacAceVidBitmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_DiffServMacAceVidBitmask_Type.__name__ = "Integer32"
_DiffServMacAceVidBitmask_Object = MibTableColumn
diffServMacAceVidBitmask = _DiffServMacAceVidBitmask_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 18, 1, 10),
    _DiffServMacAceVidBitmask_Type()
)
diffServMacAceVidBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMacAceVidBitmask.setStatus("current")


class _DiffServMacAceMaxVid_Type(Integer32):
    """Custom type diffServMacAceMaxVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_DiffServMacAceMaxVid_Type.__name__ = "Integer32"
_DiffServMacAceMaxVid_Object = MibTableColumn
diffServMacAceMaxVid = _DiffServMacAceMaxVid_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 18, 1, 11),
    _DiffServMacAceMaxVid_Type()
)
diffServMacAceMaxVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMacAceMaxVid.setStatus("current")


class _DiffServMacAceEtherTypeOp_Type(Integer32):
    """Custom type diffServMacAceEtherTypeOp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("equal", 2),
          ("noOperator", 1),
          ("range", 3))
    )


_DiffServMacAceEtherTypeOp_Type.__name__ = "Integer32"
_DiffServMacAceEtherTypeOp_Object = MibTableColumn
diffServMacAceEtherTypeOp = _DiffServMacAceEtherTypeOp_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 18, 1, 12),
    _DiffServMacAceEtherTypeOp_Type()
)
diffServMacAceEtherTypeOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMacAceEtherTypeOp.setStatus("current")


class _DiffServMacAceEtherTypeBitmask_Type(Integer32):
    """Custom type diffServMacAceEtherTypeBitmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DiffServMacAceEtherTypeBitmask_Type.__name__ = "Integer32"
_DiffServMacAceEtherTypeBitmask_Object = MibTableColumn
diffServMacAceEtherTypeBitmask = _DiffServMacAceEtherTypeBitmask_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 18, 1, 13),
    _DiffServMacAceEtherTypeBitmask_Type()
)
diffServMacAceEtherTypeBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMacAceEtherTypeBitmask.setStatus("current")


class _DiffServMacAceMinEtherType_Type(Integer32):
    """Custom type diffServMacAceMinEtherType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1536, 65535),
    )


_DiffServMacAceMinEtherType_Type.__name__ = "Integer32"
_DiffServMacAceMinEtherType_Object = MibTableColumn
diffServMacAceMinEtherType = _DiffServMacAceMinEtherType_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 18, 1, 14),
    _DiffServMacAceMinEtherType_Type()
)
diffServMacAceMinEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMacAceMinEtherType.setStatus("current")


class _DiffServMacAceMaxEtherType_Type(Integer32):
    """Custom type diffServMacAceMaxEtherType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1536, 65535),
    )


_DiffServMacAceMaxEtherType_Type.__name__ = "Integer32"
_DiffServMacAceMaxEtherType_Object = MibTableColumn
diffServMacAceMaxEtherType = _DiffServMacAceMaxEtherType_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 18, 1, 15),
    _DiffServMacAceMaxEtherType_Type()
)
diffServMacAceMaxEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMacAceMaxEtherType.setStatus("current")
_DiffServMacAceStatus_Type = RowStatus
_DiffServMacAceStatus_Object = MibTableColumn
diffServMacAceStatus = _DiffServMacAceStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 18, 1, 16),
    _DiffServMacAceStatus_Type()
)
diffServMacAceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMacAceStatus.setStatus("current")
_DiffServActionTable_Object = MibTable
diffServActionTable = _DiffServActionTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 19)
)
if mibBuilder.loadTexts:
    diffServActionTable.setStatus("current")
_DiffServActionEntry_Object = MibTableRow
diffServActionEntry = _DiffServActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 19, 1)
)
diffServActionEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "diffServActionIndex"),
)
if mibBuilder.loadTexts:
    diffServActionEntry.setStatus("current")
_DiffServActionIndex_Type = Integer32
_DiffServActionIndex_Object = MibTableColumn
diffServActionIndex = _DiffServActionIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 19, 1, 1),
    _DiffServActionIndex_Type()
)
diffServActionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServActionIndex.setStatus("current")


class _DiffServActionList_Type(Bits):
    """Custom type diffServActionList based on Bits"""
    namedValues = NamedValues(
        *(("actionPktNewDscp", 2),
          ("actionPktNewIpPrec", 1),
          ("actionPktNewPri", 0),
          ("actionRedDrop", 4),
          ("actionRedPktNewDscp", 3))
    )

_DiffServActionList_Type.__name__ = "Bits"
_DiffServActionList_Object = MibTableColumn
diffServActionList = _DiffServActionList_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 19, 1, 2),
    _DiffServActionList_Type()
)
diffServActionList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServActionList.setStatus("current")


class _DiffServActionPktNewPri_Type(Integer32):
    """Custom type diffServActionPktNewPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DiffServActionPktNewPri_Type.__name__ = "Integer32"
_DiffServActionPktNewPri_Object = MibTableColumn
diffServActionPktNewPri = _DiffServActionPktNewPri_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 19, 1, 3),
    _DiffServActionPktNewPri_Type()
)
diffServActionPktNewPri.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServActionPktNewPri.setStatus("current")


class _DiffServActionPktNewIpPrec_Type(Integer32):
    """Custom type diffServActionPktNewIpPrec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DiffServActionPktNewIpPrec_Type.__name__ = "Integer32"
_DiffServActionPktNewIpPrec_Object = MibTableColumn
diffServActionPktNewIpPrec = _DiffServActionPktNewIpPrec_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 19, 1, 4),
    _DiffServActionPktNewIpPrec_Type()
)
diffServActionPktNewIpPrec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServActionPktNewIpPrec.setStatus("current")


class _DiffServActionPktNewDscp_Type(Integer32):
    """Custom type diffServActionPktNewDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_DiffServActionPktNewDscp_Type.__name__ = "Integer32"
_DiffServActionPktNewDscp_Object = MibTableColumn
diffServActionPktNewDscp = _DiffServActionPktNewDscp_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 19, 1, 5),
    _DiffServActionPktNewDscp_Type()
)
diffServActionPktNewDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServActionPktNewDscp.setStatus("current")


class _DiffServActionRedPktNewDscp_Type(Integer32):
    """Custom type diffServActionRedPktNewDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_DiffServActionRedPktNewDscp_Type.__name__ = "Integer32"
_DiffServActionRedPktNewDscp_Object = MibTableColumn
diffServActionRedPktNewDscp = _DiffServActionRedPktNewDscp_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 19, 1, 6),
    _DiffServActionRedPktNewDscp_Type()
)
diffServActionRedPktNewDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServActionRedPktNewDscp.setStatus("current")
_DiffServActionRedDrop_Type = EnabledStatus
_DiffServActionRedDrop_Object = MibTableColumn
diffServActionRedDrop = _DiffServActionRedDrop_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 19, 1, 7),
    _DiffServActionRedDrop_Type()
)
diffServActionRedDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServActionRedDrop.setStatus("current")
_DiffServActionStatus_Type = RowStatus
_DiffServActionStatus_Object = MibTableColumn
diffServActionStatus = _DiffServActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 19, 1, 8),
    _DiffServActionStatus_Type()
)
diffServActionStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServActionStatus.setStatus("current")
_DiffServMeterTable_Object = MibTable
diffServMeterTable = _DiffServMeterTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 20)
)
if mibBuilder.loadTexts:
    diffServMeterTable.setStatus("current")
_DiffServMeterEntry_Object = MibTableRow
diffServMeterEntry = _DiffServMeterEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 20, 1)
)
diffServMeterEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "diffServActionIndex"),
)
if mibBuilder.loadTexts:
    diffServMeterEntry.setStatus("current")
_DiffServMeterIndex_Type = Integer32
_DiffServMeterIndex_Object = MibTableColumn
diffServMeterIndex = _DiffServMeterIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 20, 1, 1),
    _DiffServMeterIndex_Type()
)
diffServMeterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServMeterIndex.setStatus("current")


class _DiffServMeterModel_Type(Integer32):
    """Custom type diffServMeterModel based on Integer32"""
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
        *(("default", 1),
          ("flow", 2),
          ("srTcmColorAware", 6),
          ("srTcmColorBlind", 5),
          ("trTcmColorAware", 4),
          ("trTcmColorBlind", 3))
    )


_DiffServMeterModel_Type.__name__ = "Integer32"
_DiffServMeterModel_Object = MibTableColumn
diffServMeterModel = _DiffServMeterModel_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 20, 1, 2),
    _DiffServMeterModel_Type()
)
diffServMeterModel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMeterModel.setStatus("current")


class _DiffServMeterRate_Type(Integer32):
    """Custom type diffServMeterRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_DiffServMeterRate_Type.__name__ = "Integer32"
_DiffServMeterRate_Object = MibTableColumn
diffServMeterRate = _DiffServMeterRate_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 20, 1, 3),
    _DiffServMeterRate_Type()
)
diffServMeterRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMeterRate.setStatus("current")


class _DiffServMeterBurstSize_Type(Integer32):
    """Custom type diffServMeterBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1522),
    )


_DiffServMeterBurstSize_Type.__name__ = "Integer32"
_DiffServMeterBurstSize_Object = MibTableColumn
diffServMeterBurstSize = _DiffServMeterBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 20, 1, 4),
    _DiffServMeterBurstSize_Type()
)
diffServMeterBurstSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMeterBurstSize.setStatus("current")
_DiffServMeterInterval_Type = Integer32
_DiffServMeterInterval_Object = MibTableColumn
diffServMeterInterval = _DiffServMeterInterval_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 20, 1, 5),
    _DiffServMeterInterval_Type()
)
diffServMeterInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMeterInterval.setStatus("current")
_DiffServMeterStatus_Type = RowStatus
_DiffServMeterStatus_Object = MibTableColumn
diffServMeterStatus = _DiffServMeterStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 16, 4, 20, 1, 6),
    _DiffServMeterStatus_Type()
)
diffServMeterStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMeterStatus.setStatus("current")
_SecurityMgt_ObjectIdentity = ObjectIdentity
securityMgt = _SecurityMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17)
)
_PortSecurityMgt_ObjectIdentity = ObjectIdentity
portSecurityMgt = _PortSecurityMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 2)
)
_PortSecPortTable_Object = MibTable
portSecPortTable = _PortSecPortTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 2, 1)
)
if mibBuilder.loadTexts:
    portSecPortTable.setStatus("current")
_PortSecPortEntry_Object = MibTableRow
portSecPortEntry = _PortSecPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 2, 1, 1)
)
portSecPortEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "portSecPortIndex"),
)
if mibBuilder.loadTexts:
    portSecPortEntry.setStatus("current")
_PortSecPortIndex_Type = Integer32
_PortSecPortIndex_Object = MibTableColumn
portSecPortIndex = _PortSecPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 2, 1, 1, 1),
    _PortSecPortIndex_Type()
)
portSecPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portSecPortIndex.setStatus("current")
_PortSecPortStatus_Type = EnabledStatus
_PortSecPortStatus_Object = MibTableColumn
portSecPortStatus = _PortSecPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 2, 1, 1, 2),
    _PortSecPortStatus_Type()
)
portSecPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecPortStatus.setStatus("current")


class _PortSecAction_Type(Integer32):
    """Custom type portSecAction based on Integer32"""
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
        *(("none", 1),
          ("shutdown", 3),
          ("trap", 2),
          ("trapAndShutdown", 4))
    )


_PortSecAction_Type.__name__ = "Integer32"
_PortSecAction_Object = MibTableColumn
portSecAction = _PortSecAction_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 2, 1, 1, 3),
    _PortSecAction_Type()
)
portSecAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecAction.setStatus("current")


class _PortSecMaxMacCount_Type(Integer32):
    """Custom type portSecMaxMacCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_PortSecMaxMacCount_Type.__name__ = "Integer32"
_PortSecMaxMacCount_Object = MibTableColumn
portSecMaxMacCount = _PortSecMaxMacCount_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 2, 1, 1, 4),
    _PortSecMaxMacCount_Type()
)
portSecMaxMacCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecMaxMacCount.setStatus("current")
_RadiusMgt_ObjectIdentity = ObjectIdentity
radiusMgt = _RadiusMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 4)
)


class _RadiusServerGlobalAuthPort_Type(Integer32):
    """Custom type radiusServerGlobalAuthPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RadiusServerGlobalAuthPort_Type.__name__ = "Integer32"
_RadiusServerGlobalAuthPort_Object = MibScalar
radiusServerGlobalAuthPort = _RadiusServerGlobalAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 4, 1),
    _RadiusServerGlobalAuthPort_Type()
)
radiusServerGlobalAuthPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusServerGlobalAuthPort.setStatus("current")


class _RadiusServerGlobalAcctPort_Type(Integer32):
    """Custom type radiusServerGlobalAcctPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RadiusServerGlobalAcctPort_Type.__name__ = "Integer32"
_RadiusServerGlobalAcctPort_Object = MibScalar
radiusServerGlobalAcctPort = _RadiusServerGlobalAcctPort_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 4, 2),
    _RadiusServerGlobalAcctPort_Type()
)
radiusServerGlobalAcctPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusServerGlobalAcctPort.setStatus("current")


class _RadiusServerGlobalKey_Type(DisplayString):
    """Custom type radiusServerGlobalKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_RadiusServerGlobalKey_Type.__name__ = "DisplayString"
_RadiusServerGlobalKey_Object = MibScalar
radiusServerGlobalKey = _RadiusServerGlobalKey_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 4, 3),
    _RadiusServerGlobalKey_Type()
)
radiusServerGlobalKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusServerGlobalKey.setStatus("current")


class _RadiusServerGlobalRetransmit_Type(Integer32):
    """Custom type radiusServerGlobalRetransmit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_RadiusServerGlobalRetransmit_Type.__name__ = "Integer32"
_RadiusServerGlobalRetransmit_Object = MibScalar
radiusServerGlobalRetransmit = _RadiusServerGlobalRetransmit_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 4, 4),
    _RadiusServerGlobalRetransmit_Type()
)
radiusServerGlobalRetransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusServerGlobalRetransmit.setStatus("current")


class _RadiusServerGlobalTimeout_Type(Integer32):
    """Custom type radiusServerGlobalTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RadiusServerGlobalTimeout_Type.__name__ = "Integer32"
_RadiusServerGlobalTimeout_Object = MibScalar
radiusServerGlobalTimeout = _RadiusServerGlobalTimeout_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 4, 5),
    _RadiusServerGlobalTimeout_Type()
)
radiusServerGlobalTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusServerGlobalTimeout.setStatus("current")
_RadiusServerTable_Object = MibTable
radiusServerTable = _RadiusServerTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 4, 7)
)
if mibBuilder.loadTexts:
    radiusServerTable.setStatus("current")
_RadiusServerEntry_Object = MibTableRow
radiusServerEntry = _RadiusServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 4, 7, 1)
)
radiusServerEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "radiusServerIndex"),
)
if mibBuilder.loadTexts:
    radiusServerEntry.setStatus("current")
_RadiusServerIndex_Type = Integer32
_RadiusServerIndex_Object = MibTableColumn
radiusServerIndex = _RadiusServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 4, 7, 1, 1),
    _RadiusServerIndex_Type()
)
radiusServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    radiusServerIndex.setStatus("current")
_RadiusServerAddress_Type = IpAddress
_RadiusServerAddress_Object = MibTableColumn
radiusServerAddress = _RadiusServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 4, 7, 1, 2),
    _RadiusServerAddress_Type()
)
radiusServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radiusServerAddress.setStatus("current")


class _RadiusServerAuthPortNumber_Type(Integer32):
    """Custom type radiusServerAuthPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RadiusServerAuthPortNumber_Type.__name__ = "Integer32"
_RadiusServerAuthPortNumber_Object = MibTableColumn
radiusServerAuthPortNumber = _RadiusServerAuthPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 4, 7, 1, 3),
    _RadiusServerAuthPortNumber_Type()
)
radiusServerAuthPortNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radiusServerAuthPortNumber.setStatus("current")


class _RadiusServerAcctPortNumber_Type(Integer32):
    """Custom type radiusServerAcctPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RadiusServerAcctPortNumber_Type.__name__ = "Integer32"
_RadiusServerAcctPortNumber_Object = MibTableColumn
radiusServerAcctPortNumber = _RadiusServerAcctPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 4, 7, 1, 4),
    _RadiusServerAcctPortNumber_Type()
)
radiusServerAcctPortNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radiusServerAcctPortNumber.setStatus("current")


class _RadiusServerKey_Type(DisplayString):
    """Custom type radiusServerKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_RadiusServerKey_Type.__name__ = "DisplayString"
_RadiusServerKey_Object = MibTableColumn
radiusServerKey = _RadiusServerKey_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 4, 7, 1, 5),
    _RadiusServerKey_Type()
)
radiusServerKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusServerKey.setStatus("current")


class _RadiusServerRetransmit_Type(Integer32):
    """Custom type radiusServerRetransmit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_RadiusServerRetransmit_Type.__name__ = "Integer32"
_RadiusServerRetransmit_Object = MibTableColumn
radiusServerRetransmit = _RadiusServerRetransmit_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 4, 7, 1, 6),
    _RadiusServerRetransmit_Type()
)
radiusServerRetransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusServerRetransmit.setStatus("current")


class _RadiusServerTimeout_Type(Integer32):
    """Custom type radiusServerTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RadiusServerTimeout_Type.__name__ = "Integer32"
_RadiusServerTimeout_Object = MibTableColumn
radiusServerTimeout = _RadiusServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 4, 7, 1, 7),
    _RadiusServerTimeout_Type()
)
radiusServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusServerTimeout.setStatus("current")
_RadiusServerStatus_Type = ValidStatus
_RadiusServerStatus_Object = MibTableColumn
radiusServerStatus = _RadiusServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 4, 7, 1, 8),
    _RadiusServerStatus_Type()
)
radiusServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radiusServerStatus.setStatus("current")
_TacacsMgt_ObjectIdentity = ObjectIdentity
tacacsMgt = _TacacsMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 5)
)


class _TacacsPlusServerGlobalPortNumber_Type(Integer32):
    """Custom type tacacsPlusServerGlobalPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TacacsPlusServerGlobalPortNumber_Type.__name__ = "Integer32"
_TacacsPlusServerGlobalPortNumber_Object = MibScalar
tacacsPlusServerGlobalPortNumber = _TacacsPlusServerGlobalPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 5, 2),
    _TacacsPlusServerGlobalPortNumber_Type()
)
tacacsPlusServerGlobalPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsPlusServerGlobalPortNumber.setStatus("current")


class _TacacsPlusServerGlobalKey_Type(DisplayString):
    """Custom type tacacsPlusServerGlobalKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_TacacsPlusServerGlobalKey_Type.__name__ = "DisplayString"
_TacacsPlusServerGlobalKey_Object = MibScalar
tacacsPlusServerGlobalKey = _TacacsPlusServerGlobalKey_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 5, 3),
    _TacacsPlusServerGlobalKey_Type()
)
tacacsPlusServerGlobalKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsPlusServerGlobalKey.setStatus("current")
_TacacsPlusServerTable_Object = MibTable
tacacsPlusServerTable = _TacacsPlusServerTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 5, 4)
)
if mibBuilder.loadTexts:
    tacacsPlusServerTable.setStatus("current")
_TacacsPlusServerEntry_Object = MibTableRow
tacacsPlusServerEntry = _TacacsPlusServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 5, 4, 1)
)
tacacsPlusServerEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "tacacsPlusServerIndex"),
)
if mibBuilder.loadTexts:
    tacacsPlusServerEntry.setStatus("current")
_TacacsPlusServerIndex_Type = Integer32
_TacacsPlusServerIndex_Object = MibTableColumn
tacacsPlusServerIndex = _TacacsPlusServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 5, 4, 1, 1),
    _TacacsPlusServerIndex_Type()
)
tacacsPlusServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tacacsPlusServerIndex.setStatus("current")
_TacacsPlusServerAddress_Type = IpAddress
_TacacsPlusServerAddress_Object = MibTableColumn
tacacsPlusServerAddress = _TacacsPlusServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 5, 4, 1, 2),
    _TacacsPlusServerAddress_Type()
)
tacacsPlusServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tacacsPlusServerAddress.setStatus("current")


class _TacacsPlusServerPortNumber_Type(Integer32):
    """Custom type tacacsPlusServerPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TacacsPlusServerPortNumber_Type.__name__ = "Integer32"
_TacacsPlusServerPortNumber_Object = MibTableColumn
tacacsPlusServerPortNumber = _TacacsPlusServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 5, 4, 1, 3),
    _TacacsPlusServerPortNumber_Type()
)
tacacsPlusServerPortNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tacacsPlusServerPortNumber.setStatus("current")


class _TacacsPlusServerKey_Type(DisplayString):
    """Custom type tacacsPlusServerKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_TacacsPlusServerKey_Type.__name__ = "DisplayString"
_TacacsPlusServerKey_Object = MibTableColumn
tacacsPlusServerKey = _TacacsPlusServerKey_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 5, 4, 1, 4),
    _TacacsPlusServerKey_Type()
)
tacacsPlusServerKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tacacsPlusServerKey.setStatus("current")
_TacacsPlusServerStatus_Type = ValidStatus
_TacacsPlusServerStatus_Object = MibTableColumn
tacacsPlusServerStatus = _TacacsPlusServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 5, 4, 1, 8),
    _TacacsPlusServerStatus_Type()
)
tacacsPlusServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tacacsPlusServerStatus.setStatus("current")


class _TacacsPlusServerRetransmit_Type(Integer32):
    """Custom type tacacsPlusServerRetransmit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_TacacsPlusServerRetransmit_Type.__name__ = "Integer32"
_TacacsPlusServerRetransmit_Object = MibTableColumn
tacacsPlusServerRetransmit = _TacacsPlusServerRetransmit_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 5, 4, 1, 9),
    _TacacsPlusServerRetransmit_Type()
)
tacacsPlusServerRetransmit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tacacsPlusServerRetransmit.setStatus("current")


class _TacacsPlusServerTimeout_Type(Integer32):
    """Custom type tacacsPlusServerTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 540),
    )


_TacacsPlusServerTimeout_Type.__name__ = "Integer32"
_TacacsPlusServerTimeout_Object = MibTableColumn
tacacsPlusServerTimeout = _TacacsPlusServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 5, 4, 1, 10),
    _TacacsPlusServerTimeout_Type()
)
tacacsPlusServerTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tacacsPlusServerTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tacacsPlusServerTimeout.setUnits("seconds")


class _TacacsPlusServerGlobalRetransmit_Type(Integer32):
    """Custom type tacacsPlusServerGlobalRetransmit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_TacacsPlusServerGlobalRetransmit_Type.__name__ = "Integer32"
_TacacsPlusServerGlobalRetransmit_Object = MibScalar
tacacsPlusServerGlobalRetransmit = _TacacsPlusServerGlobalRetransmit_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 5, 5),
    _TacacsPlusServerGlobalRetransmit_Type()
)
tacacsPlusServerGlobalRetransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsPlusServerGlobalRetransmit.setStatus("current")


class _TacacsPlusServerGlobalTimeout_Type(Integer32):
    """Custom type tacacsPlusServerGlobalTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 540),
    )


_TacacsPlusServerGlobalTimeout_Type.__name__ = "Integer32"
_TacacsPlusServerGlobalTimeout_Object = MibScalar
tacacsPlusServerGlobalTimeout = _TacacsPlusServerGlobalTimeout_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 5, 6),
    _TacacsPlusServerGlobalTimeout_Type()
)
tacacsPlusServerGlobalTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsPlusServerGlobalTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tacacsPlusServerGlobalTimeout.setUnits("seconds")
_SshMgt_ObjectIdentity = ObjectIdentity
sshMgt = _SshMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 6)
)
_SshServerStatus_Type = EnabledStatus
_SshServerStatus_Object = MibScalar
sshServerStatus = _SshServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 6, 1),
    _SshServerStatus_Type()
)
sshServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshServerStatus.setStatus("current")
_SshServerMajorVersion_Type = Integer32
_SshServerMajorVersion_Object = MibScalar
sshServerMajorVersion = _SshServerMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 6, 2),
    _SshServerMajorVersion_Type()
)
sshServerMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshServerMajorVersion.setStatus("current")
_SshServerMinorVersion_Type = Integer32
_SshServerMinorVersion_Object = MibScalar
sshServerMinorVersion = _SshServerMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 6, 3),
    _SshServerMinorVersion_Type()
)
sshServerMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshServerMinorVersion.setStatus("current")


class _SshTimeout_Type(Integer32):
    """Custom type sshTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_SshTimeout_Type.__name__ = "Integer32"
_SshTimeout_Object = MibScalar
sshTimeout = _SshTimeout_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 6, 4),
    _SshTimeout_Type()
)
sshTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshTimeout.setStatus("current")
if mibBuilder.loadTexts:
    sshTimeout.setUnits("seconds")


class _SshAuthRetries_Type(Integer32):
    """Custom type sshAuthRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_SshAuthRetries_Type.__name__ = "Integer32"
_SshAuthRetries_Object = MibScalar
sshAuthRetries = _SshAuthRetries_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 6, 5),
    _SshAuthRetries_Type()
)
sshAuthRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshAuthRetries.setStatus("current")
_SshConnInfoTable_Object = MibTable
sshConnInfoTable = _SshConnInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 6, 6)
)
if mibBuilder.loadTexts:
    sshConnInfoTable.setStatus("current")
_SshConnInfoEntry_Object = MibTableRow
sshConnInfoEntry = _SshConnInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 6, 6, 1)
)
sshConnInfoEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "sshConnID"),
)
if mibBuilder.loadTexts:
    sshConnInfoEntry.setStatus("current")
_SshConnID_Type = Integer32
_SshConnID_Object = MibTableColumn
sshConnID = _SshConnID_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 6, 6, 1, 1),
    _SshConnID_Type()
)
sshConnID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sshConnID.setStatus("current")
_SshConnMajorVersion_Type = Integer32
_SshConnMajorVersion_Object = MibTableColumn
sshConnMajorVersion = _SshConnMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 6, 6, 1, 2),
    _SshConnMajorVersion_Type()
)
sshConnMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshConnMajorVersion.setStatus("current")
_SshConnMinorVersion_Type = Integer32
_SshConnMinorVersion_Object = MibTableColumn
sshConnMinorVersion = _SshConnMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 6, 6, 1, 3),
    _SshConnMinorVersion_Type()
)
sshConnMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshConnMinorVersion.setStatus("current")


class _SshConnStatus_Type(Integer32):
    """Custom type sshConnStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("authenticationStart", 2),
          ("negotiationStart", 1),
          ("sessionStart", 3))
    )


_SshConnStatus_Type.__name__ = "Integer32"
_SshConnStatus_Object = MibTableColumn
sshConnStatus = _SshConnStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 6, 6, 1, 5),
    _SshConnStatus_Type()
)
sshConnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshConnStatus.setStatus("current")


class _SshConnUserName_Type(DisplayString):
    """Custom type sshConnUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_SshConnUserName_Type.__name__ = "DisplayString"
_SshConnUserName_Object = MibTableColumn
sshConnUserName = _SshConnUserName_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 6, 6, 1, 6),
    _SshConnUserName_Type()
)
sshConnUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshConnUserName.setStatus("current")


class _SshDisconnect_Type(Integer32):
    """Custom type sshDisconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disconnect", 2),
          ("noDisconnect", 1))
    )


_SshDisconnect_Type.__name__ = "Integer32"
_SshDisconnect_Object = MibTableColumn
sshDisconnect = _SshDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 6, 6, 1, 7),
    _SshDisconnect_Type()
)
sshDisconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshDisconnect.setStatus("current")


class _SshConnEncryptionTypeStr_Type(DisplayString):
    """Custom type sshConnEncryptionTypeStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SshConnEncryptionTypeStr_Type.__name__ = "DisplayString"
_SshConnEncryptionTypeStr_Object = MibTableColumn
sshConnEncryptionTypeStr = _SshConnEncryptionTypeStr_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 6, 6, 1, 8),
    _SshConnEncryptionTypeStr_Type()
)
sshConnEncryptionTypeStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshConnEncryptionTypeStr.setStatus("current")


class _SshKeySize_Type(Integer32):
    """Custom type sshKeySize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 896),
    )


_SshKeySize_Type.__name__ = "Integer32"
_SshKeySize_Object = MibScalar
sshKeySize = _SshKeySize_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 6, 7),
    _SshKeySize_Type()
)
sshKeySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshKeySize.setStatus("current")
_SshRsaHostKey1_Type = KeySegment
_SshRsaHostKey1_Object = MibScalar
sshRsaHostKey1 = _SshRsaHostKey1_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 6, 8),
    _SshRsaHostKey1_Type()
)
sshRsaHostKey1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshRsaHostKey1.setStatus("current")
_SshRsaHostKey2_Type = KeySegment
_SshRsaHostKey2_Object = MibScalar
sshRsaHostKey2 = _SshRsaHostKey2_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 6, 9),
    _SshRsaHostKey2_Type()
)
sshRsaHostKey2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshRsaHostKey2.setStatus("current")
_SshRsaHostKey3_Type = KeySegment
_SshRsaHostKey3_Object = MibScalar
sshRsaHostKey3 = _SshRsaHostKey3_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 6, 10),
    _SshRsaHostKey3_Type()
)
sshRsaHostKey3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshRsaHostKey3.setStatus("current")
_SshRsaHostKey4_Type = KeySegment
_SshRsaHostKey4_Object = MibScalar
sshRsaHostKey4 = _SshRsaHostKey4_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 6, 11),
    _SshRsaHostKey4_Type()
)
sshRsaHostKey4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshRsaHostKey4.setStatus("current")
_SshRsaHostKey5_Type = KeySegment
_SshRsaHostKey5_Object = MibScalar
sshRsaHostKey5 = _SshRsaHostKey5_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 6, 12),
    _SshRsaHostKey5_Type()
)
sshRsaHostKey5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshRsaHostKey5.setStatus("current")
_SshRsaHostKey6_Type = KeySegment
_SshRsaHostKey6_Object = MibScalar
sshRsaHostKey6 = _SshRsaHostKey6_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 6, 13),
    _SshRsaHostKey6_Type()
)
sshRsaHostKey6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshRsaHostKey6.setStatus("current")
_SshRsaHostKey7_Type = KeySegment
_SshRsaHostKey7_Object = MibScalar
sshRsaHostKey7 = _SshRsaHostKey7_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 6, 14),
    _SshRsaHostKey7_Type()
)
sshRsaHostKey7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshRsaHostKey7.setStatus("current")
_SshRsaHostKey8_Type = KeySegment
_SshRsaHostKey8_Object = MibScalar
sshRsaHostKey8 = _SshRsaHostKey8_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 6, 15),
    _SshRsaHostKey8_Type()
)
sshRsaHostKey8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshRsaHostKey8.setStatus("current")
_SshDsaHostKey1_Type = KeySegment
_SshDsaHostKey1_Object = MibScalar
sshDsaHostKey1 = _SshDsaHostKey1_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 6, 16),
    _SshDsaHostKey1_Type()
)
sshDsaHostKey1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshDsaHostKey1.setStatus("current")
_SshDsaHostKey2_Type = KeySegment
_SshDsaHostKey2_Object = MibScalar
sshDsaHostKey2 = _SshDsaHostKey2_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 6, 17),
    _SshDsaHostKey2_Type()
)
sshDsaHostKey2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshDsaHostKey2.setStatus("current")
_SshDsaHostKey3_Type = KeySegment
_SshDsaHostKey3_Object = MibScalar
sshDsaHostKey3 = _SshDsaHostKey3_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 6, 18),
    _SshDsaHostKey3_Type()
)
sshDsaHostKey3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshDsaHostKey3.setStatus("current")
_SshDsaHostKey4_Type = KeySegment
_SshDsaHostKey4_Object = MibScalar
sshDsaHostKey4 = _SshDsaHostKey4_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 6, 19),
    _SshDsaHostKey4_Type()
)
sshDsaHostKey4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshDsaHostKey4.setStatus("current")
_SshDsaHostKey5_Type = KeySegment
_SshDsaHostKey5_Object = MibScalar
sshDsaHostKey5 = _SshDsaHostKey5_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 6, 20),
    _SshDsaHostKey5_Type()
)
sshDsaHostKey5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshDsaHostKey5.setStatus("current")
_SshDsaHostKey6_Type = KeySegment
_SshDsaHostKey6_Object = MibScalar
sshDsaHostKey6 = _SshDsaHostKey6_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 6, 21),
    _SshDsaHostKey6_Type()
)
sshDsaHostKey6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshDsaHostKey6.setStatus("current")
_SshDsaHostKey7_Type = KeySegment
_SshDsaHostKey7_Object = MibScalar
sshDsaHostKey7 = _SshDsaHostKey7_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 6, 22),
    _SshDsaHostKey7_Type()
)
sshDsaHostKey7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshDsaHostKey7.setStatus("current")
_SshDsaHostKey8_Type = KeySegment
_SshDsaHostKey8_Object = MibScalar
sshDsaHostKey8 = _SshDsaHostKey8_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 6, 23),
    _SshDsaHostKey8_Type()
)
sshDsaHostKey8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshDsaHostKey8.setStatus("current")


class _SshHostKeyGenAction_Type(Integer32):
    """Custom type sshHostKeyGenAction based on Integer32"""
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
        *(("genBothKeys", 4),
          ("genDsaKey", 3),
          ("genRsaKey", 2),
          ("noGen", 1))
    )


_SshHostKeyGenAction_Type.__name__ = "Integer32"
_SshHostKeyGenAction_Object = MibScalar
sshHostKeyGenAction = _SshHostKeyGenAction_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 6, 24),
    _SshHostKeyGenAction_Type()
)
sshHostKeyGenAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshHostKeyGenAction.setStatus("current")


class _SshHostKeyGenStatus_Type(Integer32):
    """Custom type sshHostKeyGenStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failure", 3),
          ("success", 2),
          ("unknown", 1))
    )


_SshHostKeyGenStatus_Type.__name__ = "Integer32"
_SshHostKeyGenStatus_Object = MibScalar
sshHostKeyGenStatus = _SshHostKeyGenStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 6, 25),
    _SshHostKeyGenStatus_Type()
)
sshHostKeyGenStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshHostKeyGenStatus.setStatus("current")


class _SshHostKeySaveAction_Type(Integer32):
    """Custom type sshHostKeySaveAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noSave", 1),
          ("save", 2))
    )


_SshHostKeySaveAction_Type.__name__ = "Integer32"
_SshHostKeySaveAction_Object = MibScalar
sshHostKeySaveAction = _SshHostKeySaveAction_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 6, 26),
    _SshHostKeySaveAction_Type()
)
sshHostKeySaveAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshHostKeySaveAction.setStatus("current")


class _SshHostKeySaveStatus_Type(Integer32):
    """Custom type sshHostKeySaveStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failure", 3),
          ("success", 2),
          ("unknown", 1))
    )


_SshHostKeySaveStatus_Type.__name__ = "Integer32"
_SshHostKeySaveStatus_Object = MibScalar
sshHostKeySaveStatus = _SshHostKeySaveStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 6, 27),
    _SshHostKeySaveStatus_Type()
)
sshHostKeySaveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshHostKeySaveStatus.setStatus("current")


class _SshHostKeyDelAction_Type(Integer32):
    """Custom type sshHostKeyDelAction based on Integer32"""
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
        *(("delBothKeys", 4),
          ("delDsaKey", 3),
          ("delRsaKey", 2),
          ("noDel", 1))
    )


_SshHostKeyDelAction_Type.__name__ = "Integer32"
_SshHostKeyDelAction_Object = MibScalar
sshHostKeyDelAction = _SshHostKeyDelAction_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 6, 28),
    _SshHostKeyDelAction_Type()
)
sshHostKeyDelAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshHostKeyDelAction.setStatus("current")
_AclMgt_ObjectIdentity = ObjectIdentity
aclMgt = _AclMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 7)
)
_AclIpAceTable_Object = MibTable
aclIpAceTable = _AclIpAceTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 7, 1)
)
if mibBuilder.loadTexts:
    aclIpAceTable.setStatus("current")
_AclIpAceEntry_Object = MibTableRow
aclIpAceEntry = _AclIpAceEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 7, 1, 1)
)
aclIpAceEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "aclIpAceName"),
    (0, "ES3526XA_ES3510-MIB", "aclIpAceIndex"),
)
if mibBuilder.loadTexts:
    aclIpAceEntry.setStatus("current")


class _AclIpAceName_Type(DisplayString):
    """Custom type aclIpAceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_AclIpAceName_Type.__name__ = "DisplayString"
_AclIpAceName_Object = MibTableColumn
aclIpAceName = _AclIpAceName_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 7, 1, 1, 1),
    _AclIpAceName_Type()
)
aclIpAceName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclIpAceName.setStatus("current")


class _AclIpAceIndex_Type(Integer32):
    """Custom type aclIpAceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AclIpAceIndex_Type.__name__ = "Integer32"
_AclIpAceIndex_Object = MibTableColumn
aclIpAceIndex = _AclIpAceIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 7, 1, 1, 2),
    _AclIpAceIndex_Type()
)
aclIpAceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclIpAceIndex.setStatus("current")


class _AclIpAcePrecedence_Type(Integer32):
    """Custom type aclIpAcePrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AclIpAcePrecedence_Type.__name__ = "Integer32"
_AclIpAcePrecedence_Object = MibTableColumn
aclIpAcePrecedence = _AclIpAcePrecedence_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 7, 1, 1, 3),
    _AclIpAcePrecedence_Type()
)
aclIpAcePrecedence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclIpAcePrecedence.setStatus("current")


class _AclIpAceAction_Type(Integer32):
    """Custom type aclIpAceAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )


_AclIpAceAction_Type.__name__ = "Integer32"
_AclIpAceAction_Object = MibTableColumn
aclIpAceAction = _AclIpAceAction_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 7, 1, 1, 4),
    _AclIpAceAction_Type()
)
aclIpAceAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpAceAction.setStatus("current")
_AclIpAceSourceIpAddr_Type = IpAddress
_AclIpAceSourceIpAddr_Object = MibTableColumn
aclIpAceSourceIpAddr = _AclIpAceSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 7, 1, 1, 5),
    _AclIpAceSourceIpAddr_Type()
)
aclIpAceSourceIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpAceSourceIpAddr.setStatus("current")
_AclIpAceSourceIpAddrBitmask_Type = IpAddress
_AclIpAceSourceIpAddrBitmask_Object = MibTableColumn
aclIpAceSourceIpAddrBitmask = _AclIpAceSourceIpAddrBitmask_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 7, 1, 1, 6),
    _AclIpAceSourceIpAddrBitmask_Type()
)
aclIpAceSourceIpAddrBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpAceSourceIpAddrBitmask.setStatus("current")
_AclIpAceDestIpAddr_Type = IpAddress
_AclIpAceDestIpAddr_Object = MibTableColumn
aclIpAceDestIpAddr = _AclIpAceDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 7, 1, 1, 7),
    _AclIpAceDestIpAddr_Type()
)
aclIpAceDestIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpAceDestIpAddr.setStatus("current")
_AclIpAceDestIpAddrBitmask_Type = IpAddress
_AclIpAceDestIpAddrBitmask_Object = MibTableColumn
aclIpAceDestIpAddrBitmask = _AclIpAceDestIpAddrBitmask_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 7, 1, 1, 8),
    _AclIpAceDestIpAddrBitmask_Type()
)
aclIpAceDestIpAddrBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpAceDestIpAddrBitmask.setStatus("current")


class _AclIpAceProtocol_Type(Integer32):
    """Custom type aclIpAceProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_AclIpAceProtocol_Type.__name__ = "Integer32"
_AclIpAceProtocol_Object = MibTableColumn
aclIpAceProtocol = _AclIpAceProtocol_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 7, 1, 1, 9),
    _AclIpAceProtocol_Type()
)
aclIpAceProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpAceProtocol.setStatus("current")


class _AclIpAcePrec_Type(Integer32):
    """Custom type aclIpAcePrec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_AclIpAcePrec_Type.__name__ = "Integer32"
_AclIpAcePrec_Object = MibTableColumn
aclIpAcePrec = _AclIpAcePrec_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 7, 1, 1, 10),
    _AclIpAcePrec_Type()
)
aclIpAcePrec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpAcePrec.setStatus("current")


class _AclIpAceTos_Type(Integer32):
    """Custom type aclIpAceTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AclIpAceTos_Type.__name__ = "Integer32"
_AclIpAceTos_Object = MibTableColumn
aclIpAceTos = _AclIpAceTos_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 7, 1, 1, 11),
    _AclIpAceTos_Type()
)
aclIpAceTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpAceTos.setStatus("current")


class _AclIpAceDscp_Type(Integer32):
    """Custom type aclIpAceDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_AclIpAceDscp_Type.__name__ = "Integer32"
_AclIpAceDscp_Object = MibTableColumn
aclIpAceDscp = _AclIpAceDscp_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 7, 1, 1, 12),
    _AclIpAceDscp_Type()
)
aclIpAceDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpAceDscp.setStatus("current")


class _AclIpAceSourcePortOp_Type(Integer32):
    """Custom type aclIpAceSourcePortOp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("equal", 2),
          ("noOperator", 1),
          ("range", 3))
    )


_AclIpAceSourcePortOp_Type.__name__ = "Integer32"
_AclIpAceSourcePortOp_Object = MibTableColumn
aclIpAceSourcePortOp = _AclIpAceSourcePortOp_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 7, 1, 1, 13),
    _AclIpAceSourcePortOp_Type()
)
aclIpAceSourcePortOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpAceSourcePortOp.setStatus("current")


class _AclIpAceMinSourcePort_Type(Integer32):
    """Custom type aclIpAceMinSourcePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclIpAceMinSourcePort_Type.__name__ = "Integer32"
_AclIpAceMinSourcePort_Object = MibTableColumn
aclIpAceMinSourcePort = _AclIpAceMinSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 7, 1, 1, 14),
    _AclIpAceMinSourcePort_Type()
)
aclIpAceMinSourcePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpAceMinSourcePort.setStatus("current")


class _AclIpAceMaxSourcePort_Type(Integer32):
    """Custom type aclIpAceMaxSourcePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclIpAceMaxSourcePort_Type.__name__ = "Integer32"
_AclIpAceMaxSourcePort_Object = MibTableColumn
aclIpAceMaxSourcePort = _AclIpAceMaxSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 7, 1, 1, 15),
    _AclIpAceMaxSourcePort_Type()
)
aclIpAceMaxSourcePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpAceMaxSourcePort.setStatus("current")


class _AclIpAceDestPortOp_Type(Integer32):
    """Custom type aclIpAceDestPortOp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("equal", 2),
          ("noOperator", 1),
          ("range", 3))
    )


_AclIpAceDestPortOp_Type.__name__ = "Integer32"
_AclIpAceDestPortOp_Object = MibTableColumn
aclIpAceDestPortOp = _AclIpAceDestPortOp_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 7, 1, 1, 17),
    _AclIpAceDestPortOp_Type()
)
aclIpAceDestPortOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpAceDestPortOp.setStatus("current")


class _AclIpAceMinDestPort_Type(Integer32):
    """Custom type aclIpAceMinDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclIpAceMinDestPort_Type.__name__ = "Integer32"
_AclIpAceMinDestPort_Object = MibTableColumn
aclIpAceMinDestPort = _AclIpAceMinDestPort_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 7, 1, 1, 18),
    _AclIpAceMinDestPort_Type()
)
aclIpAceMinDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpAceMinDestPort.setStatus("current")


class _AclIpAceMaxDestPort_Type(Integer32):
    """Custom type aclIpAceMaxDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclIpAceMaxDestPort_Type.__name__ = "Integer32"
_AclIpAceMaxDestPort_Object = MibTableColumn
aclIpAceMaxDestPort = _AclIpAceMaxDestPort_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 7, 1, 1, 19),
    _AclIpAceMaxDestPort_Type()
)
aclIpAceMaxDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpAceMaxDestPort.setStatus("current")


class _AclIpAceControlCode_Type(Integer32):
    """Custom type aclIpAceControlCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AclIpAceControlCode_Type.__name__ = "Integer32"
_AclIpAceControlCode_Object = MibTableColumn
aclIpAceControlCode = _AclIpAceControlCode_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 7, 1, 1, 21),
    _AclIpAceControlCode_Type()
)
aclIpAceControlCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpAceControlCode.setStatus("current")


class _AclIpAceControlCodeBitmask_Type(Integer32):
    """Custom type aclIpAceControlCodeBitmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AclIpAceControlCodeBitmask_Type.__name__ = "Integer32"
_AclIpAceControlCodeBitmask_Object = MibTableColumn
aclIpAceControlCodeBitmask = _AclIpAceControlCodeBitmask_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 7, 1, 1, 22),
    _AclIpAceControlCodeBitmask_Type()
)
aclIpAceControlCodeBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpAceControlCodeBitmask.setStatus("current")
_AclIpAceStatus_Type = RowStatus
_AclIpAceStatus_Object = MibTableColumn
aclIpAceStatus = _AclIpAceStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 7, 1, 1, 23),
    _AclIpAceStatus_Type()
)
aclIpAceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpAceStatus.setStatus("current")
_AclMacAceTable_Object = MibTable
aclMacAceTable = _AclMacAceTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 7, 2)
)
if mibBuilder.loadTexts:
    aclMacAceTable.setStatus("current")
_AclMacAceEntry_Object = MibTableRow
aclMacAceEntry = _AclMacAceEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 7, 2, 1)
)
aclMacAceEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "aclMacAceName"),
    (0, "ES3526XA_ES3510-MIB", "aclMacAceIndex"),
)
if mibBuilder.loadTexts:
    aclMacAceEntry.setStatus("current")


class _AclMacAceName_Type(DisplayString):
    """Custom type aclMacAceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_AclMacAceName_Type.__name__ = "DisplayString"
_AclMacAceName_Object = MibTableColumn
aclMacAceName = _AclMacAceName_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 7, 2, 1, 1),
    _AclMacAceName_Type()
)
aclMacAceName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclMacAceName.setStatus("current")


class _AclMacAceIndex_Type(Integer32):
    """Custom type aclMacAceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AclMacAceIndex_Type.__name__ = "Integer32"
_AclMacAceIndex_Object = MibTableColumn
aclMacAceIndex = _AclMacAceIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 7, 2, 1, 2),
    _AclMacAceIndex_Type()
)
aclMacAceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclMacAceIndex.setStatus("current")


class _AclMacAcePrecedence_Type(Integer32):
    """Custom type aclMacAcePrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AclMacAcePrecedence_Type.__name__ = "Integer32"
_AclMacAcePrecedence_Object = MibTableColumn
aclMacAcePrecedence = _AclMacAcePrecedence_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 7, 2, 1, 3),
    _AclMacAcePrecedence_Type()
)
aclMacAcePrecedence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclMacAcePrecedence.setStatus("current")


class _AclMacAceAction_Type(Integer32):
    """Custom type aclMacAceAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )


_AclMacAceAction_Type.__name__ = "Integer32"
_AclMacAceAction_Object = MibTableColumn
aclMacAceAction = _AclMacAceAction_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 7, 2, 1, 4),
    _AclMacAceAction_Type()
)
aclMacAceAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacAceAction.setStatus("current")


class _AclMacAcePktformat_Type(Integer32):
    """Custom type aclMacAcePktformat based on Integer32"""
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
        *(("any", 1),
          ("tagged802Dot3", 5),
          ("tagggedEth2", 4),
          ("untagged-Eth2", 2),
          ("untagged802Dot3", 3))
    )


_AclMacAcePktformat_Type.__name__ = "Integer32"
_AclMacAcePktformat_Object = MibTableColumn
aclMacAcePktformat = _AclMacAcePktformat_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 7, 2, 1, 5),
    _AclMacAcePktformat_Type()
)
aclMacAcePktformat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacAcePktformat.setStatus("current")


class _AclMacAceSourceMacAddr_Type(OctetString):
    """Custom type aclMacAceSourceMacAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_AclMacAceSourceMacAddr_Type.__name__ = "OctetString"
_AclMacAceSourceMacAddr_Object = MibTableColumn
aclMacAceSourceMacAddr = _AclMacAceSourceMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 7, 2, 1, 6),
    _AclMacAceSourceMacAddr_Type()
)
aclMacAceSourceMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacAceSourceMacAddr.setStatus("current")


class _AclMacAceSourceMacAddrBitmask_Type(OctetString):
    """Custom type aclMacAceSourceMacAddrBitmask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_AclMacAceSourceMacAddrBitmask_Type.__name__ = "OctetString"
_AclMacAceSourceMacAddrBitmask_Object = MibTableColumn
aclMacAceSourceMacAddrBitmask = _AclMacAceSourceMacAddrBitmask_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 7, 2, 1, 7),
    _AclMacAceSourceMacAddrBitmask_Type()
)
aclMacAceSourceMacAddrBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacAceSourceMacAddrBitmask.setStatus("current")


class _AclMacAceDestMacAddr_Type(OctetString):
    """Custom type aclMacAceDestMacAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_AclMacAceDestMacAddr_Type.__name__ = "OctetString"
_AclMacAceDestMacAddr_Object = MibTableColumn
aclMacAceDestMacAddr = _AclMacAceDestMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 7, 2, 1, 8),
    _AclMacAceDestMacAddr_Type()
)
aclMacAceDestMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacAceDestMacAddr.setStatus("current")


class _AclMacAceDestMacAddrBitmask_Type(OctetString):
    """Custom type aclMacAceDestMacAddrBitmask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_AclMacAceDestMacAddrBitmask_Type.__name__ = "OctetString"
_AclMacAceDestMacAddrBitmask_Object = MibTableColumn
aclMacAceDestMacAddrBitmask = _AclMacAceDestMacAddrBitmask_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 7, 2, 1, 9),
    _AclMacAceDestMacAddrBitmask_Type()
)
aclMacAceDestMacAddrBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacAceDestMacAddrBitmask.setStatus("current")


class _AclMacAceVidOp_Type(Integer32):
    """Custom type aclMacAceVidOp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noOperator", 1),
          ("range", 3))
    )


_AclMacAceVidOp_Type.__name__ = "Integer32"
_AclMacAceVidOp_Object = MibTableColumn
aclMacAceVidOp = _AclMacAceVidOp_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 7, 2, 1, 10),
    _AclMacAceVidOp_Type()
)
aclMacAceVidOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacAceVidOp.setStatus("current")


class _AclMacAceMinVid_Type(Integer32):
    """Custom type aclMacAceMinVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AclMacAceMinVid_Type.__name__ = "Integer32"
_AclMacAceMinVid_Object = MibTableColumn
aclMacAceMinVid = _AclMacAceMinVid_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 7, 2, 1, 11),
    _AclMacAceMinVid_Type()
)
aclMacAceMinVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacAceMinVid.setStatus("current")


class _AclMacAceMaxVid_Type(Integer32):
    """Custom type aclMacAceMaxVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AclMacAceMaxVid_Type.__name__ = "Integer32"
_AclMacAceMaxVid_Object = MibTableColumn
aclMacAceMaxVid = _AclMacAceMaxVid_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 7, 2, 1, 13),
    _AclMacAceMaxVid_Type()
)
aclMacAceMaxVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacAceMaxVid.setStatus("current")


class _AclMacAceEtherTypeOp_Type(Integer32):
    """Custom type aclMacAceEtherTypeOp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noOperator", 1),
          ("range", 3))
    )


_AclMacAceEtherTypeOp_Type.__name__ = "Integer32"
_AclMacAceEtherTypeOp_Object = MibTableColumn
aclMacAceEtherTypeOp = _AclMacAceEtherTypeOp_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 7, 2, 1, 14),
    _AclMacAceEtherTypeOp_Type()
)
aclMacAceEtherTypeOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacAceEtherTypeOp.setStatus("current")


class _AclMacAceMinEtherType_Type(Integer32):
    """Custom type aclMacAceMinEtherType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclMacAceMinEtherType_Type.__name__ = "Integer32"
_AclMacAceMinEtherType_Object = MibTableColumn
aclMacAceMinEtherType = _AclMacAceMinEtherType_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 7, 2, 1, 16),
    _AclMacAceMinEtherType_Type()
)
aclMacAceMinEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacAceMinEtherType.setStatus("current")


class _AclMacAceMaxEtherType_Type(Integer32):
    """Custom type aclMacAceMaxEtherType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclMacAceMaxEtherType_Type.__name__ = "Integer32"
_AclMacAceMaxEtherType_Object = MibTableColumn
aclMacAceMaxEtherType = _AclMacAceMaxEtherType_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 7, 2, 1, 17),
    _AclMacAceMaxEtherType_Type()
)
aclMacAceMaxEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacAceMaxEtherType.setStatus("current")
_AclMacAceStatus_Type = RowStatus
_AclMacAceStatus_Object = MibTableColumn
aclMacAceStatus = _AclMacAceStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 7, 2, 1, 18),
    _AclMacAceStatus_Type()
)
aclMacAceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacAceStatus.setStatus("current")
_AclAclGroupTable_Object = MibTable
aclAclGroupTable = _AclAclGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 7, 3)
)
if mibBuilder.loadTexts:
    aclAclGroupTable.setStatus("current")
_AclAclGroupEntry_Object = MibTableRow
aclAclGroupEntry = _AclAclGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 7, 3, 1)
)
aclAclGroupEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "aclAclGroupIfIndex"),
)
if mibBuilder.loadTexts:
    aclAclGroupEntry.setStatus("current")
_AclAclGroupIfIndex_Type = Integer32
_AclAclGroupIfIndex_Object = MibTableColumn
aclAclGroupIfIndex = _AclAclGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 7, 3, 1, 1),
    _AclAclGroupIfIndex_Type()
)
aclAclGroupIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclAclGroupIfIndex.setStatus("current")


class _AclAclGroupIngressIpAcl_Type(DisplayString):
    """Custom type aclAclGroupIngressIpAcl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AclAclGroupIngressIpAcl_Type.__name__ = "DisplayString"
_AclAclGroupIngressIpAcl_Object = MibTableColumn
aclAclGroupIngressIpAcl = _AclAclGroupIngressIpAcl_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 7, 3, 1, 2),
    _AclAclGroupIngressIpAcl_Type()
)
aclAclGroupIngressIpAcl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclAclGroupIngressIpAcl.setStatus("current")


class _AclAclGroupEgressIpAcl_Type(DisplayString):
    """Custom type aclAclGroupEgressIpAcl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AclAclGroupEgressIpAcl_Type.__name__ = "DisplayString"
_AclAclGroupEgressIpAcl_Object = MibTableColumn
aclAclGroupEgressIpAcl = _AclAclGroupEgressIpAcl_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 7, 3, 1, 3),
    _AclAclGroupEgressIpAcl_Type()
)
aclAclGroupEgressIpAcl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclAclGroupEgressIpAcl.setStatus("current")


class _AclAclGroupIngressMacAcl_Type(DisplayString):
    """Custom type aclAclGroupIngressMacAcl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AclAclGroupIngressMacAcl_Type.__name__ = "DisplayString"
_AclAclGroupIngressMacAcl_Object = MibTableColumn
aclAclGroupIngressMacAcl = _AclAclGroupIngressMacAcl_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 7, 3, 1, 4),
    _AclAclGroupIngressMacAcl_Type()
)
aclAclGroupIngressMacAcl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclAclGroupIngressMacAcl.setStatus("current")


class _AclAclGroupEgressMacAcl_Type(DisplayString):
    """Custom type aclAclGroupEgressMacAcl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AclAclGroupEgressMacAcl_Type.__name__ = "DisplayString"
_AclAclGroupEgressMacAcl_Object = MibTableColumn
aclAclGroupEgressMacAcl = _AclAclGroupEgressMacAcl_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 7, 3, 1, 5),
    _AclAclGroupEgressMacAcl_Type()
)
aclAclGroupEgressMacAcl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclAclGroupEgressMacAcl.setStatus("current")
_IpFilterMgt_ObjectIdentity = ObjectIdentity
ipFilterMgt = _IpFilterMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 9)
)
_IpFilterSnmpTable_Object = MibTable
ipFilterSnmpTable = _IpFilterSnmpTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 9, 1)
)
if mibBuilder.loadTexts:
    ipFilterSnmpTable.setStatus("current")
_IpFilterSnmpEntry_Object = MibTableRow
ipFilterSnmpEntry = _IpFilterSnmpEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 9, 1, 1)
)
ipFilterSnmpEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "ipFilterSnmpStartAddress"),
)
if mibBuilder.loadTexts:
    ipFilterSnmpEntry.setStatus("current")
_IpFilterSnmpStartAddress_Type = IpAddress
_IpFilterSnmpStartAddress_Object = MibTableColumn
ipFilterSnmpStartAddress = _IpFilterSnmpStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 9, 1, 1, 1),
    _IpFilterSnmpStartAddress_Type()
)
ipFilterSnmpStartAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipFilterSnmpStartAddress.setStatus("current")
_IpFilterSnmpEndAddress_Type = IpAddress
_IpFilterSnmpEndAddress_Object = MibTableColumn
ipFilterSnmpEndAddress = _IpFilterSnmpEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 9, 1, 1, 2),
    _IpFilterSnmpEndAddress_Type()
)
ipFilterSnmpEndAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipFilterSnmpEndAddress.setStatus("current")
_IpFilterSnmpStatus_Type = ValidStatus
_IpFilterSnmpStatus_Object = MibTableColumn
ipFilterSnmpStatus = _IpFilterSnmpStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 9, 1, 1, 3),
    _IpFilterSnmpStatus_Type()
)
ipFilterSnmpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipFilterSnmpStatus.setStatus("current")
_IpFilterHTTPTable_Object = MibTable
ipFilterHTTPTable = _IpFilterHTTPTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 9, 2)
)
if mibBuilder.loadTexts:
    ipFilterHTTPTable.setStatus("current")
_IpFilterHTTPEntry_Object = MibTableRow
ipFilterHTTPEntry = _IpFilterHTTPEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 9, 2, 1)
)
ipFilterHTTPEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "ipFilterHTTPStartAddress"),
)
if mibBuilder.loadTexts:
    ipFilterHTTPEntry.setStatus("current")
_IpFilterHTTPStartAddress_Type = IpAddress
_IpFilterHTTPStartAddress_Object = MibTableColumn
ipFilterHTTPStartAddress = _IpFilterHTTPStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 9, 2, 1, 1),
    _IpFilterHTTPStartAddress_Type()
)
ipFilterHTTPStartAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipFilterHTTPStartAddress.setStatus("current")
_IpFilterHTTPEndAddress_Type = IpAddress
_IpFilterHTTPEndAddress_Object = MibTableColumn
ipFilterHTTPEndAddress = _IpFilterHTTPEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 9, 2, 1, 2),
    _IpFilterHTTPEndAddress_Type()
)
ipFilterHTTPEndAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipFilterHTTPEndAddress.setStatus("current")
_IpFilterHTTPStatus_Type = ValidStatus
_IpFilterHTTPStatus_Object = MibTableColumn
ipFilterHTTPStatus = _IpFilterHTTPStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 9, 2, 1, 3),
    _IpFilterHTTPStatus_Type()
)
ipFilterHTTPStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipFilterHTTPStatus.setStatus("current")
_IpFilterTelnetTable_Object = MibTable
ipFilterTelnetTable = _IpFilterTelnetTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 9, 3)
)
if mibBuilder.loadTexts:
    ipFilterTelnetTable.setStatus("current")
_IpFilterTelnetEntry_Object = MibTableRow
ipFilterTelnetEntry = _IpFilterTelnetEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 9, 3, 1)
)
ipFilterTelnetEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "ipFilterTelnetStartAddress"),
)
if mibBuilder.loadTexts:
    ipFilterTelnetEntry.setStatus("current")
_IpFilterTelnetStartAddress_Type = IpAddress
_IpFilterTelnetStartAddress_Object = MibTableColumn
ipFilterTelnetStartAddress = _IpFilterTelnetStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 9, 3, 1, 1),
    _IpFilterTelnetStartAddress_Type()
)
ipFilterTelnetStartAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipFilterTelnetStartAddress.setStatus("current")
_IpFilterTelnetEndAddress_Type = IpAddress
_IpFilterTelnetEndAddress_Object = MibTableColumn
ipFilterTelnetEndAddress = _IpFilterTelnetEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 9, 3, 1, 2),
    _IpFilterTelnetEndAddress_Type()
)
ipFilterTelnetEndAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipFilterTelnetEndAddress.setStatus("current")
_IpFilterTelnetStatus_Type = ValidStatus
_IpFilterTelnetStatus_Object = MibTableColumn
ipFilterTelnetStatus = _IpFilterTelnetStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 17, 9, 3, 1, 3),
    _IpFilterTelnetStatus_Type()
)
ipFilterTelnetStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipFilterTelnetStatus.setStatus("current")
_SysLogMgt_ObjectIdentity = ObjectIdentity
sysLogMgt = _SysLogMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 19)
)


class _SysLogStatus_Type(Integer32):
    """Custom type sysLogStatus based on Integer32"""
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


_SysLogStatus_Type.__name__ = "Integer32"
_SysLogStatus_Object = MibScalar
sysLogStatus = _SysLogStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 19, 1),
    _SysLogStatus_Type()
)
sysLogStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogStatus.setStatus("current")


class _SysLogHistoryFlashLevel_Type(Integer32):
    """Custom type sysLogHistoryFlashLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SysLogHistoryFlashLevel_Type.__name__ = "Integer32"
_SysLogHistoryFlashLevel_Object = MibScalar
sysLogHistoryFlashLevel = _SysLogHistoryFlashLevel_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 19, 2),
    _SysLogHistoryFlashLevel_Type()
)
sysLogHistoryFlashLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogHistoryFlashLevel.setStatus("current")


class _SysLogHistoryRamLevel_Type(Integer32):
    """Custom type sysLogHistoryRamLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SysLogHistoryRamLevel_Type.__name__ = "Integer32"
_SysLogHistoryRamLevel_Object = MibScalar
sysLogHistoryRamLevel = _SysLogHistoryRamLevel_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 19, 3),
    _SysLogHistoryRamLevel_Type()
)
sysLogHistoryRamLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogHistoryRamLevel.setStatus("current")
_RemoteLogMgt_ObjectIdentity = ObjectIdentity
remoteLogMgt = _RemoteLogMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 19, 6)
)
_RemoteLogStatus_Type = EnabledStatus
_RemoteLogStatus_Object = MibScalar
remoteLogStatus = _RemoteLogStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 19, 6, 1),
    _RemoteLogStatus_Type()
)
remoteLogStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteLogStatus.setStatus("current")


class _RemoteLogLevel_Type(Integer32):
    """Custom type remoteLogLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RemoteLogLevel_Type.__name__ = "Integer32"
_RemoteLogLevel_Object = MibScalar
remoteLogLevel = _RemoteLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 19, 6, 2),
    _RemoteLogLevel_Type()
)
remoteLogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteLogLevel.setStatus("current")


class _RemoteLogFacilityType_Type(Integer32):
    """Custom type remoteLogFacilityType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(16,
              17,
              18,
              19,
              20,
              21,
              22,
              23)
        )
    )
    namedValues = NamedValues(
        *(("localUse0", 16),
          ("localUse1", 17),
          ("localUse2", 18),
          ("localUse3", 19),
          ("localUse4", 20),
          ("localUse5", 21),
          ("localUse6", 22),
          ("localUse7", 23))
    )


_RemoteLogFacilityType_Type.__name__ = "Integer32"
_RemoteLogFacilityType_Object = MibScalar
remoteLogFacilityType = _RemoteLogFacilityType_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 19, 6, 3),
    _RemoteLogFacilityType_Type()
)
remoteLogFacilityType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteLogFacilityType.setStatus("current")
_RemoteLogServerTable_Object = MibTable
remoteLogServerTable = _RemoteLogServerTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 19, 6, 4)
)
if mibBuilder.loadTexts:
    remoteLogServerTable.setStatus("current")
_RemoteLogServerEntry_Object = MibTableRow
remoteLogServerEntry = _RemoteLogServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 19, 6, 4, 1)
)
remoteLogServerEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "remoteLogServerIp"),
)
if mibBuilder.loadTexts:
    remoteLogServerEntry.setStatus("current")
_RemoteLogServerIp_Type = IpAddress
_RemoteLogServerIp_Object = MibTableColumn
remoteLogServerIp = _RemoteLogServerIp_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 19, 6, 4, 1, 1),
    _RemoteLogServerIp_Type()
)
remoteLogServerIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    remoteLogServerIp.setStatus("current")
_RemoteLogServerStatus_Type = ValidStatus
_RemoteLogServerStatus_Object = MibTableColumn
remoteLogServerStatus = _RemoteLogServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 19, 6, 4, 1, 2),
    _RemoteLogServerStatus_Type()
)
remoteLogServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    remoteLogServerStatus.setStatus("current")
_SmtpMgt_ObjectIdentity = ObjectIdentity
smtpMgt = _SmtpMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 19, 7)
)
_SmtpStatus_Type = EnabledStatus
_SmtpStatus_Object = MibScalar
smtpStatus = _SmtpStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 19, 7, 1),
    _SmtpStatus_Type()
)
smtpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpStatus.setStatus("current")


class _SmtpSeverityLevel_Type(Integer32):
    """Custom type smtpSeverityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SmtpSeverityLevel_Type.__name__ = "Integer32"
_SmtpSeverityLevel_Object = MibScalar
smtpSeverityLevel = _SmtpSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 19, 7, 2),
    _SmtpSeverityLevel_Type()
)
smtpSeverityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpSeverityLevel.setStatus("current")


class _SmtpSourceEMail_Type(DisplayString):
    """Custom type smtpSourceEMail based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 41),
    )


_SmtpSourceEMail_Type.__name__ = "DisplayString"
_SmtpSourceEMail_Object = MibScalar
smtpSourceEMail = _SmtpSourceEMail_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 19, 7, 3),
    _SmtpSourceEMail_Type()
)
smtpSourceEMail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpSourceEMail.setStatus("current")
_SmtpServerIpTable_Object = MibTable
smtpServerIpTable = _SmtpServerIpTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 19, 7, 4)
)
if mibBuilder.loadTexts:
    smtpServerIpTable.setStatus("current")
_SmtpServerIpEntry_Object = MibTableRow
smtpServerIpEntry = _SmtpServerIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 19, 7, 4, 1)
)
smtpServerIpEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "smtpServerIp"),
)
if mibBuilder.loadTexts:
    smtpServerIpEntry.setStatus("current")
_SmtpServerIp_Type = IpAddress
_SmtpServerIp_Object = MibTableColumn
smtpServerIp = _SmtpServerIp_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 19, 7, 4, 1, 1),
    _SmtpServerIp_Type()
)
smtpServerIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    smtpServerIp.setStatus("current")
_SmtpServerIpStatus_Type = ValidStatus
_SmtpServerIpStatus_Object = MibTableColumn
smtpServerIpStatus = _SmtpServerIpStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 19, 7, 4, 1, 2),
    _SmtpServerIpStatus_Type()
)
smtpServerIpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    smtpServerIpStatus.setStatus("current")
_SmtpDestEMailTable_Object = MibTable
smtpDestEMailTable = _SmtpDestEMailTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 19, 7, 5)
)
if mibBuilder.loadTexts:
    smtpDestEMailTable.setStatus("current")
_SmtpDestEMailEntry_Object = MibTableRow
smtpDestEMailEntry = _SmtpDestEMailEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 19, 7, 5, 1)
)
smtpDestEMailEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "smtpDestEMail"),
)
if mibBuilder.loadTexts:
    smtpDestEMailEntry.setStatus("current")


class _SmtpDestEMail_Type(DisplayString):
    """Custom type smtpDestEMail based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 41),
    )


_SmtpDestEMail_Type.__name__ = "DisplayString"
_SmtpDestEMail_Object = MibTableColumn
smtpDestEMail = _SmtpDestEMail_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 19, 7, 5, 1, 1),
    _SmtpDestEMail_Type()
)
smtpDestEMail.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    smtpDestEMail.setStatus("current")
_SmtpDestEMailStatus_Type = ValidStatus
_SmtpDestEMailStatus_Object = MibTableColumn
smtpDestEMailStatus = _SmtpDestEMailStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 19, 7, 5, 1, 2),
    _SmtpDestEMailStatus_Type()
)
smtpDestEMailStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    smtpDestEMailStatus.setStatus("current")
_LineMgt_ObjectIdentity = ObjectIdentity
lineMgt = _LineMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 20)
)
_ConsoleMgt_ObjectIdentity = ObjectIdentity
consoleMgt = _ConsoleMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 20, 1)
)


class _ConsoleDataBits_Type(Integer32):
    """Custom type consoleDataBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("databits7", 1),
          ("databits8", 2))
    )


_ConsoleDataBits_Type.__name__ = "Integer32"
_ConsoleDataBits_Object = MibScalar
consoleDataBits = _ConsoleDataBits_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 20, 1, 1),
    _ConsoleDataBits_Type()
)
consoleDataBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consoleDataBits.setStatus("current")


class _ConsoleParity_Type(Integer32):
    """Custom type consoleParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("partyEven", 2),
          ("partyNone", 1),
          ("partyOdd", 3))
    )


_ConsoleParity_Type.__name__ = "Integer32"
_ConsoleParity_Object = MibScalar
consoleParity = _ConsoleParity_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 20, 1, 2),
    _ConsoleParity_Type()
)
consoleParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consoleParity.setStatus("current")


class _ConsoleStopBits_Type(Integer32):
    """Custom type consoleStopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stopbits1", 1),
          ("stopbits2", 2))
    )


_ConsoleStopBits_Type.__name__ = "Integer32"
_ConsoleStopBits_Object = MibScalar
consoleStopBits = _ConsoleStopBits_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 20, 1, 4),
    _ConsoleStopBits_Type()
)
consoleStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consoleStopBits.setStatus("current")


class _ConsoleExecTimeout_Type(Integer32):
    """Custom type consoleExecTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ConsoleExecTimeout_Type.__name__ = "Integer32"
_ConsoleExecTimeout_Object = MibScalar
consoleExecTimeout = _ConsoleExecTimeout_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 20, 1, 5),
    _ConsoleExecTimeout_Type()
)
consoleExecTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consoleExecTimeout.setStatus("current")


class _ConsolePasswordThreshold_Type(Integer32):
    """Custom type consolePasswordThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_ConsolePasswordThreshold_Type.__name__ = "Integer32"
_ConsolePasswordThreshold_Object = MibScalar
consolePasswordThreshold = _ConsolePasswordThreshold_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 20, 1, 6),
    _ConsolePasswordThreshold_Type()
)
consolePasswordThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consolePasswordThreshold.setStatus("current")


class _ConsoleSilentTime_Type(Integer32):
    """Custom type consoleSilentTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ConsoleSilentTime_Type.__name__ = "Integer32"
_ConsoleSilentTime_Object = MibScalar
consoleSilentTime = _ConsoleSilentTime_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 20, 1, 7),
    _ConsoleSilentTime_Type()
)
consoleSilentTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consoleSilentTime.setStatus("current")
_ConsoleAdminBaudRate_Type = Integer32
_ConsoleAdminBaudRate_Object = MibScalar
consoleAdminBaudRate = _ConsoleAdminBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 20, 1, 8),
    _ConsoleAdminBaudRate_Type()
)
consoleAdminBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consoleAdminBaudRate.setStatus("current")
_ConsoleOperBaudRate_Type = Integer32
_ConsoleOperBaudRate_Object = MibScalar
consoleOperBaudRate = _ConsoleOperBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 20, 1, 9),
    _ConsoleOperBaudRate_Type()
)
consoleOperBaudRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consoleOperBaudRate.setStatus("current")


class _ConsoleLoginResponseTimeout_Type(Integer32):
    """Custom type consoleLoginResponseTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_ConsoleLoginResponseTimeout_Type.__name__ = "Integer32"
_ConsoleLoginResponseTimeout_Object = MibScalar
consoleLoginResponseTimeout = _ConsoleLoginResponseTimeout_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 20, 1, 10),
    _ConsoleLoginResponseTimeout_Type()
)
consoleLoginResponseTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consoleLoginResponseTimeout.setStatus("current")
_TelnetMgt_ObjectIdentity = ObjectIdentity
telnetMgt = _TelnetMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 20, 2)
)


class _TelnetExecTimeout_Type(Integer32):
    """Custom type telnetExecTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TelnetExecTimeout_Type.__name__ = "Integer32"
_TelnetExecTimeout_Object = MibScalar
telnetExecTimeout = _TelnetExecTimeout_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 20, 2, 1),
    _TelnetExecTimeout_Type()
)
telnetExecTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetExecTimeout.setStatus("current")


class _TelnetPasswordThreshold_Type(Integer32):
    """Custom type telnetPasswordThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_TelnetPasswordThreshold_Type.__name__ = "Integer32"
_TelnetPasswordThreshold_Object = MibScalar
telnetPasswordThreshold = _TelnetPasswordThreshold_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 20, 2, 2),
    _TelnetPasswordThreshold_Type()
)
telnetPasswordThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetPasswordThreshold.setStatus("current")


class _TelnetLoginResponseTimeout_Type(Integer32):
    """Custom type telnetLoginResponseTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_TelnetLoginResponseTimeout_Type.__name__ = "Integer32"
_TelnetLoginResponseTimeout_Object = MibScalar
telnetLoginResponseTimeout = _TelnetLoginResponseTimeout_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 20, 2, 3),
    _TelnetLoginResponseTimeout_Type()
)
telnetLoginResponseTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetLoginResponseTimeout.setStatus("current")
_SysTimeMgt_ObjectIdentity = ObjectIdentity
sysTimeMgt = _SysTimeMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 23)
)
_SntpMgt_ObjectIdentity = ObjectIdentity
sntpMgt = _SntpMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 23, 1)
)
_SntpStatus_Type = EnabledStatus
_SntpStatus_Object = MibScalar
sntpStatus = _SntpStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 23, 1, 1),
    _SntpStatus_Type()
)
sntpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpStatus.setStatus("current")


class _SntpServiceMode_Type(Integer32):
    """Custom type sntpServiceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("unicast", 1)
    )


_SntpServiceMode_Type.__name__ = "Integer32"
_SntpServiceMode_Object = MibScalar
sntpServiceMode = _SntpServiceMode_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 23, 1, 2),
    _SntpServiceMode_Type()
)
sntpServiceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpServiceMode.setStatus("current")


class _SntpPollInterval_Type(Integer32):
    """Custom type sntpPollInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 16384),
    )


_SntpPollInterval_Type.__name__ = "Integer32"
_SntpPollInterval_Object = MibScalar
sntpPollInterval = _SntpPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 23, 1, 3),
    _SntpPollInterval_Type()
)
sntpPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpPollInterval.setStatus("current")
_SntpServerTable_Object = MibTable
sntpServerTable = _SntpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 23, 1, 4)
)
if mibBuilder.loadTexts:
    sntpServerTable.setStatus("current")
_SntpServerEntry_Object = MibTableRow
sntpServerEntry = _SntpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 23, 1, 4, 1)
)
sntpServerEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "sntpServerIndex"),
)
if mibBuilder.loadTexts:
    sntpServerEntry.setStatus("current")


class _SntpServerIndex_Type(Integer32):
    """Custom type sntpServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_SntpServerIndex_Type.__name__ = "Integer32"
_SntpServerIndex_Object = MibTableColumn
sntpServerIndex = _SntpServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 23, 1, 4, 1, 1),
    _SntpServerIndex_Type()
)
sntpServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sntpServerIndex.setStatus("current")
_SntpServerIpAddress_Type = IpAddress
_SntpServerIpAddress_Object = MibTableColumn
sntpServerIpAddress = _SntpServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 23, 1, 4, 1, 2),
    _SntpServerIpAddress_Type()
)
sntpServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpServerIpAddress.setStatus("current")


class _SysCurrentTime_Type(DisplayString):
    """Custom type sysCurrentTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_SysCurrentTime_Type.__name__ = "DisplayString"
_SysCurrentTime_Object = MibScalar
sysCurrentTime = _SysCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 23, 2),
    _SysCurrentTime_Type()
)
sysCurrentTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysCurrentTime.setStatus("current")


class _SysTimeZone_Type(DisplayString):
    """Custom type sysTimeZone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_SysTimeZone_Type.__name__ = "DisplayString"
_SysTimeZone_Object = MibScalar
sysTimeZone = _SysTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 23, 3),
    _SysTimeZone_Type()
)
sysTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeZone.setStatus("current")


class _SysTimeZoneName_Type(DisplayString):
    """Custom type sysTimeZoneName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_SysTimeZoneName_Type.__name__ = "DisplayString"
_SysTimeZoneName_Object = MibScalar
sysTimeZoneName = _SysTimeZoneName_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 23, 4),
    _SysTimeZoneName_Type()
)
sysTimeZoneName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeZoneName.setStatus("current")
_NtpMgt_ObjectIdentity = ObjectIdentity
ntpMgt = _NtpMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 23, 5)
)
_NtpStatus_Type = EnabledStatus
_NtpStatus_Object = MibScalar
ntpStatus = _NtpStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 23, 5, 1),
    _NtpStatus_Type()
)
ntpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpStatus.setStatus("current")


class _NtpServiceMode_Type(Integer32):
    """Custom type ntpServiceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("unicast", 1)
    )


_NtpServiceMode_Type.__name__ = "Integer32"
_NtpServiceMode_Object = MibScalar
ntpServiceMode = _NtpServiceMode_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 23, 5, 2),
    _NtpServiceMode_Type()
)
ntpServiceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpServiceMode.setStatus("current")


class _NtpPollInterval_Type(Integer32):
    """Custom type ntpPollInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 16384),
    )


_NtpPollInterval_Type.__name__ = "Integer32"
_NtpPollInterval_Object = MibScalar
ntpPollInterval = _NtpPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 23, 5, 3),
    _NtpPollInterval_Type()
)
ntpPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpPollInterval.setStatus("current")
_NtpAuthenticateStatus_Type = EnabledStatus
_NtpAuthenticateStatus_Object = MibScalar
ntpAuthenticateStatus = _NtpAuthenticateStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 23, 5, 4),
    _NtpAuthenticateStatus_Type()
)
ntpAuthenticateStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpAuthenticateStatus.setStatus("current")
_NtpServerTable_Object = MibTable
ntpServerTable = _NtpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 23, 5, 5)
)
if mibBuilder.loadTexts:
    ntpServerTable.setStatus("current")
_NtpServerEntry_Object = MibTableRow
ntpServerEntry = _NtpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 23, 5, 5, 1)
)
ntpServerEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "ntpServerIpAddress"),
)
if mibBuilder.loadTexts:
    ntpServerEntry.setStatus("current")
_NtpServerIpAddress_Type = IpAddress
_NtpServerIpAddress_Object = MibTableColumn
ntpServerIpAddress = _NtpServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 23, 5, 5, 1, 1),
    _NtpServerIpAddress_Type()
)
ntpServerIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntpServerIpAddress.setStatus("current")


class _NtpServerVersion_Type(Integer32):
    """Custom type ntpServerVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_NtpServerVersion_Type.__name__ = "Integer32"
_NtpServerVersion_Object = MibTableColumn
ntpServerVersion = _NtpServerVersion_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 23, 5, 5, 1, 2),
    _NtpServerVersion_Type()
)
ntpServerVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntpServerVersion.setStatus("current")


class _NtpServerKeyId_Type(Integer32):
    """Custom type ntpServerKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NtpServerKeyId_Type.__name__ = "Integer32"
_NtpServerKeyId_Object = MibTableColumn
ntpServerKeyId = _NtpServerKeyId_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 23, 5, 5, 1, 3),
    _NtpServerKeyId_Type()
)
ntpServerKeyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpServerKeyId.setStatus("current")


class _NtpServerStatus_Type(Integer32):
    """Custom type ntpServerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("create", 1),
          ("destroy", 3))
    )


_NtpServerStatus_Type.__name__ = "Integer32"
_NtpServerStatus_Object = MibTableColumn
ntpServerStatus = _NtpServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 23, 5, 5, 1, 4),
    _NtpServerStatus_Type()
)
ntpServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntpServerStatus.setStatus("current")
_NtpAuthKeyTable_Object = MibTable
ntpAuthKeyTable = _NtpAuthKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 23, 5, 6)
)
if mibBuilder.loadTexts:
    ntpAuthKeyTable.setStatus("current")
_NtpAuthKeyEntry_Object = MibTableRow
ntpAuthKeyEntry = _NtpAuthKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 23, 5, 6, 1)
)
ntpAuthKeyEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "ntpAuthKeyId"),
)
if mibBuilder.loadTexts:
    ntpAuthKeyEntry.setStatus("current")


class _NtpAuthKeyId_Type(Integer32):
    """Custom type ntpAuthKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_NtpAuthKeyId_Type.__name__ = "Integer32"
_NtpAuthKeyId_Object = MibTableColumn
ntpAuthKeyId = _NtpAuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 23, 5, 6, 1, 1),
    _NtpAuthKeyId_Type()
)
ntpAuthKeyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntpAuthKeyId.setStatus("current")


class _NtpAuthKeyWord_Type(OctetString):
    """Custom type ntpAuthKeyWord based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_NtpAuthKeyWord_Type.__name__ = "OctetString"
_NtpAuthKeyWord_Object = MibTableColumn
ntpAuthKeyWord = _NtpAuthKeyWord_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 23, 5, 6, 1, 2),
    _NtpAuthKeyWord_Type()
)
ntpAuthKeyWord.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntpAuthKeyWord.setStatus("current")


class _NtpAuthKeyStatus_Type(Integer32):
    """Custom type ntpAuthKeyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("create", 1),
          ("destroy", 3))
    )


_NtpAuthKeyStatus_Type.__name__ = "Integer32"
_NtpAuthKeyStatus_Object = MibTableColumn
ntpAuthKeyStatus = _NtpAuthKeyStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 23, 5, 6, 1, 3),
    _NtpAuthKeyStatus_Type()
)
ntpAuthKeyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntpAuthKeyStatus.setStatus("current")
_FileMgt_ObjectIdentity = ObjectIdentity
fileMgt = _FileMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 24)
)
_FileCopyMgt_ObjectIdentity = ObjectIdentity
fileCopyMgt = _FileCopyMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 24, 1)
)


class _FileCopySrcOperType_Type(Integer32):
    """Custom type fileCopySrcOperType based on Integer32"""
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
        *(("file", 1),
          ("runningCfg", 2),
          ("startUpCfg", 3),
          ("tftp", 4),
          ("unit", 5))
    )


_FileCopySrcOperType_Type.__name__ = "Integer32"
_FileCopySrcOperType_Object = MibScalar
fileCopySrcOperType = _FileCopySrcOperType_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 24, 1, 1),
    _FileCopySrcOperType_Type()
)
fileCopySrcOperType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileCopySrcOperType.setStatus("current")


class _FileCopySrcFileName_Type(DisplayString):
    """Custom type fileCopySrcFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FileCopySrcFileName_Type.__name__ = "DisplayString"
_FileCopySrcFileName_Object = MibScalar
fileCopySrcFileName = _FileCopySrcFileName_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 24, 1, 2),
    _FileCopySrcFileName_Type()
)
fileCopySrcFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileCopySrcFileName.setStatus("current")


class _FileCopyDestOperType_Type(Integer32):
    """Custom type fileCopyDestOperType based on Integer32"""
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
        *(("file", 1),
          ("runningCfg", 2),
          ("startUpCfg", 3),
          ("tftp", 4),
          ("unit", 5))
    )


_FileCopyDestOperType_Type.__name__ = "Integer32"
_FileCopyDestOperType_Object = MibScalar
fileCopyDestOperType = _FileCopyDestOperType_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 24, 1, 3),
    _FileCopyDestOperType_Type()
)
fileCopyDestOperType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileCopyDestOperType.setStatus("current")


class _FileCopyDestFileName_Type(DisplayString):
    """Custom type fileCopyDestFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FileCopyDestFileName_Type.__name__ = "DisplayString"
_FileCopyDestFileName_Object = MibScalar
fileCopyDestFileName = _FileCopyDestFileName_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 24, 1, 4),
    _FileCopyDestFileName_Type()
)
fileCopyDestFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileCopyDestFileName.setStatus("current")


class _FileCopyFileType_Type(Integer32):
    """Custom type fileCopyFileType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bootRom", 3),
          ("config", 2),
          ("opcode", 1))
    )


_FileCopyFileType_Type.__name__ = "Integer32"
_FileCopyFileType_Object = MibScalar
fileCopyFileType = _FileCopyFileType_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 24, 1, 5),
    _FileCopyFileType_Type()
)
fileCopyFileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileCopyFileType.setStatus("current")
_FileCopyTftpServer_Type = IpAddress
_FileCopyTftpServer_Object = MibScalar
fileCopyTftpServer = _FileCopyTftpServer_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 24, 1, 6),
    _FileCopyTftpServer_Type()
)
fileCopyTftpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileCopyTftpServer.setStatus("current")
_FileCopyUnitId_Type = Integer32
_FileCopyUnitId_Object = MibScalar
fileCopyUnitId = _FileCopyUnitId_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 24, 1, 7),
    _FileCopyUnitId_Type()
)
fileCopyUnitId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileCopyUnitId.setStatus("current")


class _FileCopyAction_Type(Integer32):
    """Custom type fileCopyAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("copy", 2),
          ("notCopying", 1))
    )


_FileCopyAction_Type.__name__ = "Integer32"
_FileCopyAction_Object = MibScalar
fileCopyAction = _FileCopyAction_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 24, 1, 8),
    _FileCopyAction_Type()
)
fileCopyAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileCopyAction.setStatus("current")


class _FileCopyStatus_Type(Integer32):
    """Custom type fileCopyStatus based on Integer32"""
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
        *(("fileCopyBusy", 17),
          ("fileCopyCompleted", 31),
          ("fileCopyError", 29),
          ("fileCopyFileSizeExceed", 21),
          ("fileCopyHeaderChecksumError", 24),
          ("fileCopyImageChecksumError", 25),
          ("fileCopyImageTypeError", 23),
          ("fileCopyMagicWordError", 22),
          ("fileCopyParaError", 16),
          ("fileCopyReadFileError", 19),
          ("fileCopySetStartupError", 20),
          ("fileCopySuccess", 30),
          ("fileCopyTftpAccessViolation", 3),
          ("fileCopyTftpCompleted", 15),
          ("fileCopyTftpDiskFull", 4),
          ("fileCopyTftpFileExisted", 7),
          ("fileCopyTftpFileNotFound", 2),
          ("fileCopyTftpIllegalOperation", 5),
          ("fileCopyTftpNoSuchUser", 8),
          ("fileCopyTftpReceiverError", 11),
          ("fileCopyTftpSendError", 10),
          ("fileCopyTftpSocketBindError", 13),
          ("fileCopyTftpSocketOpenError", 12),
          ("fileCopyTftpTimeout", 9),
          ("fileCopyTftpUndefError", 1),
          ("fileCopyTftpUnkownTransferId", 6),
          ("fileCopyTftpUserCancel", 14),
          ("fileCopyUnknown", 18),
          ("fileCopyWriteFlashError", 27),
          ("fileCopyWriteFlashFinish", 26),
          ("fileCopyWriteFlashProgramming", 28))
    )


_FileCopyStatus_Type.__name__ = "Integer32"
_FileCopyStatus_Object = MibScalar
fileCopyStatus = _FileCopyStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 24, 1, 9),
    _FileCopyStatus_Type()
)
fileCopyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileCopyStatus.setStatus("current")


class _FileCopyTftpErrMsg_Type(DisplayString):
    """Custom type fileCopyTftpErrMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FileCopyTftpErrMsg_Type.__name__ = "DisplayString"
_FileCopyTftpErrMsg_Object = MibScalar
fileCopyTftpErrMsg = _FileCopyTftpErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 24, 1, 10),
    _FileCopyTftpErrMsg_Type()
)
fileCopyTftpErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileCopyTftpErrMsg.setStatus("current")
_FileInfoMgt_ObjectIdentity = ObjectIdentity
fileInfoMgt = _FileInfoMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 24, 2)
)
_FileInfoTable_Object = MibTable
fileInfoTable = _FileInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 24, 2, 1)
)
if mibBuilder.loadTexts:
    fileInfoTable.setStatus("current")
_FileInfoEntry_Object = MibTableRow
fileInfoEntry = _FileInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 24, 2, 1, 1)
)
fileInfoEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "fileInfoUnitID"),
    (1, "ES3526XA_ES3510-MIB", "fileInfoFileName"),
)
if mibBuilder.loadTexts:
    fileInfoEntry.setStatus("current")
_FileInfoUnitID_Type = Integer32
_FileInfoUnitID_Object = MibTableColumn
fileInfoUnitID = _FileInfoUnitID_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 24, 2, 1, 1, 1),
    _FileInfoUnitID_Type()
)
fileInfoUnitID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fileInfoUnitID.setStatus("current")


class _FileInfoFileName_Type(DisplayString):
    """Custom type fileInfoFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FileInfoFileName_Type.__name__ = "DisplayString"
_FileInfoFileName_Object = MibTableColumn
fileInfoFileName = _FileInfoFileName_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 24, 2, 1, 1, 2),
    _FileInfoFileName_Type()
)
fileInfoFileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fileInfoFileName.setStatus("current")


class _FileInfoFileType_Type(Integer32):
    """Custom type fileInfoFileType based on Integer32"""
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
        *(("certificate", 8),
          ("cmdlog", 4),
          ("config", 5),
          ("diag", 1),
          ("postlog", 6),
          ("private", 7),
          ("runtime", 2),
          ("syslog", 3),
          ("webarchive", 9))
    )


_FileInfoFileType_Type.__name__ = "Integer32"
_FileInfoFileType_Object = MibTableColumn
fileInfoFileType = _FileInfoFileType_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 24, 2, 1, 1, 3),
    _FileInfoFileType_Type()
)
fileInfoFileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileInfoFileType.setStatus("current")
_FileInfoIsStartUp_Type = TruthValue
_FileInfoIsStartUp_Object = MibTableColumn
fileInfoIsStartUp = _FileInfoIsStartUp_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 24, 2, 1, 1, 4),
    _FileInfoIsStartUp_Type()
)
fileInfoIsStartUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileInfoIsStartUp.setStatus("current")
_FileInfoFileSize_Type = Integer32
_FileInfoFileSize_Object = MibTableColumn
fileInfoFileSize = _FileInfoFileSize_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 24, 2, 1, 1, 5),
    _FileInfoFileSize_Type()
)
fileInfoFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileInfoFileSize.setStatus("current")
if mibBuilder.loadTexts:
    fileInfoFileSize.setUnits("bytes")


class _FileInfoCreationTime_Type(DisplayString):
    """Custom type fileInfoCreationTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_FileInfoCreationTime_Type.__name__ = "DisplayString"
_FileInfoCreationTime_Object = MibTableColumn
fileInfoCreationTime = _FileInfoCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 24, 2, 1, 1, 6),
    _FileInfoCreationTime_Type()
)
fileInfoCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileInfoCreationTime.setStatus("current")


class _FileInfoDelete_Type(Integer32):
    """Custom type fileInfoDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("noDelete", 1))
    )


_FileInfoDelete_Type.__name__ = "Integer32"
_FileInfoDelete_Object = MibTableColumn
fileInfoDelete = _FileInfoDelete_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 24, 2, 1, 1, 7),
    _FileInfoDelete_Type()
)
fileInfoDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileInfoDelete.setStatus("current")
_DnsMgt_ObjectIdentity = ObjectIdentity
dnsMgt = _DnsMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 26)
)
_DnsDomainLookup_Type = EnabledStatus
_DnsDomainLookup_Object = MibScalar
dnsDomainLookup = _DnsDomainLookup_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 26, 1),
    _DnsDomainLookup_Type()
)
dnsDomainLookup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsDomainLookup.setStatus("current")


class _DnsDomainName_Type(DisplayString):
    """Custom type dnsDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DnsDomainName_Type.__name__ = "DisplayString"
_DnsDomainName_Object = MibScalar
dnsDomainName = _DnsDomainName_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 26, 2),
    _DnsDomainName_Type()
)
dnsDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsDomainName.setStatus("current")
_DnsHostTable_Object = MibTable
dnsHostTable = _DnsHostTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 26, 3)
)
if mibBuilder.loadTexts:
    dnsHostTable.setStatus("current")
_DnsHostEntry_Object = MibTableRow
dnsHostEntry = _DnsHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 26, 3, 1)
)
dnsHostEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "dnsHostName"),
    (0, "ES3526XA_ES3510-MIB", "dnsHostIndex"),
)
if mibBuilder.loadTexts:
    dnsHostEntry.setStatus("current")


class _DnsHostName_Type(DisplayString):
    """Custom type dnsHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_DnsHostName_Type.__name__ = "DisplayString"
_DnsHostName_Object = MibTableColumn
dnsHostName = _DnsHostName_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 26, 3, 1, 1),
    _DnsHostName_Type()
)
dnsHostName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dnsHostName.setStatus("current")


class _DnsHostIndex_Type(Integer32):
    """Custom type dnsHostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_DnsHostIndex_Type.__name__ = "Integer32"
_DnsHostIndex_Object = MibTableColumn
dnsHostIndex = _DnsHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 26, 3, 1, 2),
    _DnsHostIndex_Type()
)
dnsHostIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dnsHostIndex.setStatus("current")
_DnsHostIp_Type = IpAddress
_DnsHostIp_Object = MibTableColumn
dnsHostIp = _DnsHostIp_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 26, 3, 1, 3),
    _DnsHostIp_Type()
)
dnsHostIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dnsHostIp.setStatus("current")
_DnsAliasTable_Object = MibTable
dnsAliasTable = _DnsAliasTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 26, 4)
)
if mibBuilder.loadTexts:
    dnsAliasTable.setStatus("current")
_DnsAliasEntry_Object = MibTableRow
dnsAliasEntry = _DnsAliasEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 26, 4, 1)
)
dnsAliasEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "dnsAliasName"),
    (0, "ES3526XA_ES3510-MIB", "dnsAliasAlias"),
)
if mibBuilder.loadTexts:
    dnsAliasEntry.setStatus("current")


class _DnsAliasName_Type(DisplayString):
    """Custom type dnsAliasName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_DnsAliasName_Type.__name__ = "DisplayString"
_DnsAliasName_Object = MibTableColumn
dnsAliasName = _DnsAliasName_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 26, 4, 1, 1),
    _DnsAliasName_Type()
)
dnsAliasName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsAliasName.setStatus("current")


class _DnsAliasAlias_Type(DisplayString):
    """Custom type dnsAliasAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_DnsAliasAlias_Type.__name__ = "DisplayString"
_DnsAliasAlias_Object = MibTableColumn
dnsAliasAlias = _DnsAliasAlias_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 26, 4, 1, 2),
    _DnsAliasAlias_Type()
)
dnsAliasAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsAliasAlias.setStatus("current")
_DnsDomainListTable_Object = MibTable
dnsDomainListTable = _DnsDomainListTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 26, 5)
)
if mibBuilder.loadTexts:
    dnsDomainListTable.setStatus("current")
_DnsDomainListEntry_Object = MibTableRow
dnsDomainListEntry = _DnsDomainListEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 26, 5, 1)
)
dnsDomainListEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "dnsDomainListName"),
)
if mibBuilder.loadTexts:
    dnsDomainListEntry.setStatus("current")


class _DnsDomainListName_Type(DisplayString):
    """Custom type dnsDomainListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_DnsDomainListName_Type.__name__ = "DisplayString"
_DnsDomainListName_Object = MibTableColumn
dnsDomainListName = _DnsDomainListName_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 26, 5, 1, 1),
    _DnsDomainListName_Type()
)
dnsDomainListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dnsDomainListName.setStatus("current")
_DnsDomainListStatus_Type = ValidStatus
_DnsDomainListStatus_Object = MibTableColumn
dnsDomainListStatus = _DnsDomainListStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 26, 5, 1, 2),
    _DnsDomainListStatus_Type()
)
dnsDomainListStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dnsDomainListStatus.setStatus("current")
_DnsNameServerTable_Object = MibTable
dnsNameServerTable = _DnsNameServerTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 26, 6)
)
if mibBuilder.loadTexts:
    dnsNameServerTable.setStatus("current")
_DnsNameServerEntry_Object = MibTableRow
dnsNameServerEntry = _DnsNameServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 26, 6, 1)
)
dnsNameServerEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "dnsNameServerIndex"),
)
if mibBuilder.loadTexts:
    dnsNameServerEntry.setStatus("current")


class _DnsNameServerIndex_Type(Integer32):
    """Custom type dnsNameServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_DnsNameServerIndex_Type.__name__ = "Integer32"
_DnsNameServerIndex_Object = MibTableColumn
dnsNameServerIndex = _DnsNameServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 26, 6, 1, 1),
    _DnsNameServerIndex_Type()
)
dnsNameServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dnsNameServerIndex.setStatus("current")
_DnsNameServerIp_Type = IpAddress
_DnsNameServerIp_Object = MibTableColumn
dnsNameServerIp = _DnsNameServerIp_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 26, 6, 1, 2),
    _DnsNameServerIp_Type()
)
dnsNameServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsNameServerIp.setStatus("current")
_DnsCacheTable_Object = MibTable
dnsCacheTable = _DnsCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 26, 7)
)
if mibBuilder.loadTexts:
    dnsCacheTable.setStatus("current")
_DnsCacheEntry_Object = MibTableRow
dnsCacheEntry = _DnsCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 26, 7, 1)
)
dnsCacheEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "dnsCacheIndex"),
)
if mibBuilder.loadTexts:
    dnsCacheEntry.setStatus("current")
_DnsCacheIndex_Type = Integer32
_DnsCacheIndex_Object = MibTableColumn
dnsCacheIndex = _DnsCacheIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 26, 7, 1, 1),
    _DnsCacheIndex_Type()
)
dnsCacheIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dnsCacheIndex.setStatus("current")
_DnsCacheFlag_Type = Integer32
_DnsCacheFlag_Object = MibTableColumn
dnsCacheFlag = _DnsCacheFlag_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 26, 7, 1, 2),
    _DnsCacheFlag_Type()
)
dnsCacheFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsCacheFlag.setStatus("current")


class _DnsCacheType_Type(Integer32):
    """Custom type dnsCacheType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("address", 1),
          ("cname", 2))
    )


_DnsCacheType_Type.__name__ = "Integer32"
_DnsCacheType_Object = MibTableColumn
dnsCacheType = _DnsCacheType_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 26, 7, 1, 3),
    _DnsCacheType_Type()
)
dnsCacheType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsCacheType.setStatus("current")
_DnsCacheIp_Type = IpAddress
_DnsCacheIp_Object = MibTableColumn
dnsCacheIp = _DnsCacheIp_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 26, 7, 1, 4),
    _DnsCacheIp_Type()
)
dnsCacheIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsCacheIp.setStatus("current")


class _DnsCacheTtl_Type(Integer32):
    """Custom type dnsCacheTtl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 876000),
    )


_DnsCacheTtl_Type.__name__ = "Integer32"
_DnsCacheTtl_Object = MibTableColumn
dnsCacheTtl = _DnsCacheTtl_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 26, 7, 1, 5),
    _DnsCacheTtl_Type()
)
dnsCacheTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsCacheTtl.setStatus("current")


class _DnsCacheDomain_Type(DisplayString):
    """Custom type dnsCacheDomain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_DnsCacheDomain_Type.__name__ = "DisplayString"
_DnsCacheDomain_Object = MibTableColumn
dnsCacheDomain = _DnsCacheDomain_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 26, 7, 1, 6),
    _DnsCacheDomain_Type()
)
dnsCacheDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsCacheDomain.setStatus("current")
_MvrMgt_ObjectIdentity = ObjectIdentity
mvrMgt = _MvrMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 44)
)
_MvrStatus_Type = EnabledStatus
_MvrStatus_Object = MibScalar
mvrStatus = _MvrStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 44, 1),
    _MvrStatus_Type()
)
mvrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrStatus.setStatus("current")
_MvrVlanId_Type = Integer32
_MvrVlanId_Object = MibScalar
mvrVlanId = _MvrVlanId_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 44, 2),
    _MvrVlanId_Type()
)
mvrVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrVlanId.setStatus("current")
_MvrMaxGroups_Type = Integer32
_MvrMaxGroups_Object = MibScalar
mvrMaxGroups = _MvrMaxGroups_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 44, 3),
    _MvrMaxGroups_Type()
)
mvrMaxGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrMaxGroups.setStatus("current")
_MvrCurrentGroups_Type = Integer32
_MvrCurrentGroups_Object = MibScalar
mvrCurrentGroups = _MvrCurrentGroups_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 44, 4),
    _MvrCurrentGroups_Type()
)
mvrCurrentGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrCurrentGroups.setStatus("current")
_MvrGroupsCtl_ObjectIdentity = ObjectIdentity
mvrGroupsCtl = _MvrGroupsCtl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 44, 5)
)
_MvrGroupsCtlId_Type = IpAddress
_MvrGroupsCtlId_Object = MibScalar
mvrGroupsCtlId = _MvrGroupsCtlId_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 44, 5, 1),
    _MvrGroupsCtlId_Type()
)
mvrGroupsCtlId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrGroupsCtlId.setStatus("current")
_MvrGroupsCtlCount_Type = Integer32
_MvrGroupsCtlCount_Object = MibScalar
mvrGroupsCtlCount = _MvrGroupsCtlCount_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 44, 5, 2),
    _MvrGroupsCtlCount_Type()
)
mvrGroupsCtlCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrGroupsCtlCount.setStatus("current")


class _MvrGroupsCtlAction_Type(Integer32):
    """Custom type mvrGroupsCtlAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("destory", 2),
          ("noAction", 0))
    )


_MvrGroupsCtlAction_Type.__name__ = "Integer32"
_MvrGroupsCtlAction_Object = MibScalar
mvrGroupsCtlAction = _MvrGroupsCtlAction_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 44, 5, 3),
    _MvrGroupsCtlAction_Type()
)
mvrGroupsCtlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrGroupsCtlAction.setStatus("current")
_MvrGroupTable_Object = MibTable
mvrGroupTable = _MvrGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 44, 6)
)
if mibBuilder.loadTexts:
    mvrGroupTable.setStatus("current")
_MvrGroupEntry_Object = MibTableRow
mvrGroupEntry = _MvrGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 44, 6, 1)
)
mvrGroupEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "mvrGroupId"),
)
if mibBuilder.loadTexts:
    mvrGroupEntry.setStatus("current")
_MvrGroupId_Type = IpAddress
_MvrGroupId_Object = MibTableColumn
mvrGroupId = _MvrGroupId_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 44, 6, 1, 1),
    _MvrGroupId_Type()
)
mvrGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mvrGroupId.setStatus("current")


class _MvrGroutActive_Type(Integer32):
    """Custom type mvrGroutActive based on Integer32"""
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


_MvrGroutActive_Type.__name__ = "Integer32"
_MvrGroutActive_Object = MibTableColumn
mvrGroutActive = _MvrGroutActive_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 44, 6, 1, 2),
    _MvrGroutActive_Type()
)
mvrGroutActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrGroutActive.setStatus("current")


class _MvrGroupStatus_Type(Integer32):
    """Custom type mvrGroupStatus based on Integer32"""
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


_MvrGroupStatus_Type.__name__ = "Integer32"
_MvrGroupStatus_Object = MibTableColumn
mvrGroupStatus = _MvrGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 44, 6, 1, 3),
    _MvrGroupStatus_Type()
)
mvrGroupStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrGroupStatus.setStatus("current")
_MvrGroupStaticTable_Object = MibTable
mvrGroupStaticTable = _MvrGroupStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 44, 7)
)
if mibBuilder.loadTexts:
    mvrGroupStaticTable.setStatus("current")
_MvrGroupStaticEntry_Object = MibTableRow
mvrGroupStaticEntry = _MvrGroupStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 44, 7, 1)
)
mvrGroupStaticEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "mvrGroupStaticAddress"),
)
if mibBuilder.loadTexts:
    mvrGroupStaticEntry.setStatus("current")
_MvrGroupStaticAddress_Type = IpAddress
_MvrGroupStaticAddress_Object = MibTableColumn
mvrGroupStaticAddress = _MvrGroupStaticAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 44, 7, 1, 1),
    _MvrGroupStaticAddress_Type()
)
mvrGroupStaticAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mvrGroupStaticAddress.setStatus("current")
_MvrGroupStaticPorts_Type = PortList
_MvrGroupStaticPorts_Object = MibTableColumn
mvrGroupStaticPorts = _MvrGroupStaticPorts_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 44, 7, 1, 2),
    _MvrGroupStaticPorts_Type()
)
mvrGroupStaticPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrGroupStaticPorts.setStatus("current")


class _MvrGroupStaticStatus_Type(Integer32):
    """Custom type mvrGroupStaticStatus based on Integer32"""
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


_MvrGroupStaticStatus_Type.__name__ = "Integer32"
_MvrGroupStaticStatus_Object = MibTableColumn
mvrGroupStaticStatus = _MvrGroupStaticStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 44, 7, 1, 3),
    _MvrGroupStaticStatus_Type()
)
mvrGroupStaticStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrGroupStaticStatus.setStatus("current")
_MvrGroupCurrentTable_Object = MibTable
mvrGroupCurrentTable = _MvrGroupCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 44, 8)
)
if mibBuilder.loadTexts:
    mvrGroupCurrentTable.setStatus("current")
_MvrGroupCurrentEntry_Object = MibTableRow
mvrGroupCurrentEntry = _MvrGroupCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 44, 8, 1)
)
mvrGroupCurrentEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "mvrGroupCurrentAddress"),
)
if mibBuilder.loadTexts:
    mvrGroupCurrentEntry.setStatus("current")
_MvrGroupCurrentAddress_Type = IpAddress
_MvrGroupCurrentAddress_Object = MibTableColumn
mvrGroupCurrentAddress = _MvrGroupCurrentAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 44, 8, 1, 1),
    _MvrGroupCurrentAddress_Type()
)
mvrGroupCurrentAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mvrGroupCurrentAddress.setStatus("current")
_MvrGroupCurrentPorts_Type = PortList
_MvrGroupCurrentPorts_Object = MibTableColumn
mvrGroupCurrentPorts = _MvrGroupCurrentPorts_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 44, 8, 1, 2),
    _MvrGroupCurrentPorts_Type()
)
mvrGroupCurrentPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrGroupCurrentPorts.setStatus("current")
_MvrPortTable_Object = MibTable
mvrPortTable = _MvrPortTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 44, 9)
)
if mibBuilder.loadTexts:
    mvrPortTable.setStatus("current")
_MvrPortEntry_Object = MibTableRow
mvrPortEntry = _MvrPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 44, 9, 1)
)
mvrPortEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "mvrIfIndex"),
)
if mibBuilder.loadTexts:
    mvrPortEntry.setStatus("current")
_MvrIfIndex_Type = InterfaceIndex
_MvrIfIndex_Object = MibTableColumn
mvrIfIndex = _MvrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 44, 9, 1, 1),
    _MvrIfIndex_Type()
)
mvrIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mvrIfIndex.setStatus("current")


class _MvrPortType_Type(Integer32):
    """Custom type mvrPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("receiver", 2),
          ("source", 1))
    )


_MvrPortType_Type.__name__ = "Integer32"
_MvrPortType_Object = MibTableColumn
mvrPortType = _MvrPortType_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 44, 9, 1, 2),
    _MvrPortType_Type()
)
mvrPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrPortType.setStatus("current")
_MvrPortImmediateLeave_Type = EnabledStatus
_MvrPortImmediateLeave_Object = MibTableColumn
mvrPortImmediateLeave = _MvrPortImmediateLeave_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 44, 9, 1, 3),
    _MvrPortImmediateLeave_Type()
)
mvrPortImmediateLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrPortImmediateLeave.setStatus("current")


class _MvrPortActive_Type(Integer32):
    """Custom type mvrPortActive based on Integer32"""
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


_MvrPortActive_Type.__name__ = "Integer32"
_MvrPortActive_Object = MibTableColumn
mvrPortActive = _MvrPortActive_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 44, 9, 1, 4),
    _MvrPortActive_Type()
)
mvrPortActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrPortActive.setStatus("current")
_MvrRunningStatus_Type = TruthValue
_MvrRunningStatus_Object = MibScalar
mvrRunningStatus = _MvrRunningStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 44, 10),
    _MvrRunningStatus_Type()
)
mvrRunningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrRunningStatus.setStatus("current")
_DhcpSnoopMgt_ObjectIdentity = ObjectIdentity
dhcpSnoopMgt = _DhcpSnoopMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 46)
)
_DhcpSnoopGlobal_ObjectIdentity = ObjectIdentity
dhcpSnoopGlobal = _DhcpSnoopGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 46, 1)
)
_DhcpSnoopEnable_Type = EnabledStatus
_DhcpSnoopEnable_Object = MibScalar
dhcpSnoopEnable = _DhcpSnoopEnable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 46, 1, 1),
    _DhcpSnoopEnable_Type()
)
dhcpSnoopEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopEnable.setStatus("current")
_DhcpSnoopVerifyMacAddressEnable_Type = EnabledStatus
_DhcpSnoopVerifyMacAddressEnable_Object = MibScalar
dhcpSnoopVerifyMacAddressEnable = _DhcpSnoopVerifyMacAddressEnable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 46, 1, 2),
    _DhcpSnoopVerifyMacAddressEnable_Type()
)
dhcpSnoopVerifyMacAddressEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopVerifyMacAddressEnable.setStatus("current")
_DhcpSnoopInformationOptionEnable_Type = EnabledStatus
_DhcpSnoopInformationOptionEnable_Object = MibScalar
dhcpSnoopInformationOptionEnable = _DhcpSnoopInformationOptionEnable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 46, 1, 3),
    _DhcpSnoopInformationOptionEnable_Type()
)
dhcpSnoopInformationOptionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopInformationOptionEnable.setStatus("current")


class _DhcpSnoopInformationOptionPolicy_Type(Integer32):
    """Custom type dhcpSnoopInformationOptionPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("keep", 2),
          ("replace", 3))
    )


_DhcpSnoopInformationOptionPolicy_Type.__name__ = "Integer32"
_DhcpSnoopInformationOptionPolicy_Object = MibScalar
dhcpSnoopInformationOptionPolicy = _DhcpSnoopInformationOptionPolicy_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 46, 1, 4),
    _DhcpSnoopInformationOptionPolicy_Type()
)
dhcpSnoopInformationOptionPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopInformationOptionPolicy.setStatus("current")
_DhcpSnoopVlan_ObjectIdentity = ObjectIdentity
dhcpSnoopVlan = _DhcpSnoopVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 46, 2)
)
_DhcpSnoopVlanConfigTable_Object = MibTable
dhcpSnoopVlanConfigTable = _DhcpSnoopVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 46, 2, 1)
)
if mibBuilder.loadTexts:
    dhcpSnoopVlanConfigTable.setStatus("current")
_DhcpSnoopVlanConfigEntry_Object = MibTableRow
dhcpSnoopVlanConfigEntry = _DhcpSnoopVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 46, 2, 1, 1)
)
dhcpSnoopVlanConfigEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "dhcpSnoopVlanIndex"),
)
if mibBuilder.loadTexts:
    dhcpSnoopVlanConfigEntry.setStatus("current")
_DhcpSnoopVlanIndex_Type = VlanIndex
_DhcpSnoopVlanIndex_Object = MibTableColumn
dhcpSnoopVlanIndex = _DhcpSnoopVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 46, 2, 1, 1, 1),
    _DhcpSnoopVlanIndex_Type()
)
dhcpSnoopVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpSnoopVlanIndex.setStatus("current")
_DhcpSnoopVlanEnable_Type = EnabledStatus
_DhcpSnoopVlanEnable_Object = MibTableColumn
dhcpSnoopVlanEnable = _DhcpSnoopVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 46, 2, 1, 1, 2),
    _DhcpSnoopVlanEnable_Type()
)
dhcpSnoopVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopVlanEnable.setStatus("current")
_DhcpSnoopInterface_ObjectIdentity = ObjectIdentity
dhcpSnoopInterface = _DhcpSnoopInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 46, 3)
)
_DhcpSnoopPortConfigTable_Object = MibTable
dhcpSnoopPortConfigTable = _DhcpSnoopPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 46, 3, 1)
)
if mibBuilder.loadTexts:
    dhcpSnoopPortConfigTable.setStatus("current")
_DhcpSnoopPortConfigEntry_Object = MibTableRow
dhcpSnoopPortConfigEntry = _DhcpSnoopPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 46, 3, 1, 1)
)
dhcpSnoopPortConfigEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "dhcpSnoopPortIfIndex"),
)
if mibBuilder.loadTexts:
    dhcpSnoopPortConfigEntry.setStatus("current")
_DhcpSnoopPortIfIndex_Type = InterfaceIndex
_DhcpSnoopPortIfIndex_Object = MibTableColumn
dhcpSnoopPortIfIndex = _DhcpSnoopPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 46, 3, 1, 1, 1),
    _DhcpSnoopPortIfIndex_Type()
)
dhcpSnoopPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpSnoopPortIfIndex.setStatus("current")
_DhcpSnoopPortTrustEnable_Type = EnabledStatus
_DhcpSnoopPortTrustEnable_Object = MibTableColumn
dhcpSnoopPortTrustEnable = _DhcpSnoopPortTrustEnable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 46, 3, 1, 1, 2),
    _DhcpSnoopPortTrustEnable_Type()
)
dhcpSnoopPortTrustEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopPortTrustEnable.setStatus("current")
_DhcpSnoopBindings_ObjectIdentity = ObjectIdentity
dhcpSnoopBindings = _DhcpSnoopBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 46, 4)
)
_DhcpSnoopBindingsTable_Object = MibTable
dhcpSnoopBindingsTable = _DhcpSnoopBindingsTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 46, 4, 1)
)
if mibBuilder.loadTexts:
    dhcpSnoopBindingsTable.setStatus("current")
_DhcpSnoopBindingsEntry_Object = MibTableRow
dhcpSnoopBindingsEntry = _DhcpSnoopBindingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 46, 4, 1, 1)
)
dhcpSnoopBindingsEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "dhcpSnoopBindingsVlanIndex"),
    (0, "ES3526XA_ES3510-MIB", "dhcpSnoopBindingsMacAddress"),
)
if mibBuilder.loadTexts:
    dhcpSnoopBindingsEntry.setStatus("current")
_DhcpSnoopBindingsVlanIndex_Type = VlanIndex
_DhcpSnoopBindingsVlanIndex_Object = MibTableColumn
dhcpSnoopBindingsVlanIndex = _DhcpSnoopBindingsVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 46, 4, 1, 1, 1),
    _DhcpSnoopBindingsVlanIndex_Type()
)
dhcpSnoopBindingsVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpSnoopBindingsVlanIndex.setStatus("current")
_DhcpSnoopBindingsMacAddress_Type = MacAddress
_DhcpSnoopBindingsMacAddress_Object = MibTableColumn
dhcpSnoopBindingsMacAddress = _DhcpSnoopBindingsMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 46, 4, 1, 1, 2),
    _DhcpSnoopBindingsMacAddress_Type()
)
dhcpSnoopBindingsMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpSnoopBindingsMacAddress.setStatus("current")
_DhcpSnoopBindingsAddrType_Type = InetAddressType
_DhcpSnoopBindingsAddrType_Object = MibTableColumn
dhcpSnoopBindingsAddrType = _DhcpSnoopBindingsAddrType_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 46, 4, 1, 1, 3),
    _DhcpSnoopBindingsAddrType_Type()
)
dhcpSnoopBindingsAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopBindingsAddrType.setStatus("current")


class _DhcpSnoopBindingsEntryType_Type(Integer32):
    """Custom type dhcpSnoopBindingsEntryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 2))
    )


_DhcpSnoopBindingsEntryType_Type.__name__ = "Integer32"
_DhcpSnoopBindingsEntryType_Object = MibTableColumn
dhcpSnoopBindingsEntryType = _DhcpSnoopBindingsEntryType_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 46, 4, 1, 1, 4),
    _DhcpSnoopBindingsEntryType_Type()
)
dhcpSnoopBindingsEntryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopBindingsEntryType.setStatus("current")
_DhcpSnoopBindingsIpAddress_Type = IpAddress
_DhcpSnoopBindingsIpAddress_Object = MibTableColumn
dhcpSnoopBindingsIpAddress = _DhcpSnoopBindingsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 46, 4, 1, 1, 5),
    _DhcpSnoopBindingsIpAddress_Type()
)
dhcpSnoopBindingsIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopBindingsIpAddress.setStatus("current")
_DhcpSnoopBindingsPortIfIndex_Type = InterfaceIndex
_DhcpSnoopBindingsPortIfIndex_Object = MibTableColumn
dhcpSnoopBindingsPortIfIndex = _DhcpSnoopBindingsPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 46, 4, 1, 1, 6),
    _DhcpSnoopBindingsPortIfIndex_Type()
)
dhcpSnoopBindingsPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopBindingsPortIfIndex.setStatus("current")
_DhcpSnoopBindingsLeaseTime_Type = Unsigned32
_DhcpSnoopBindingsLeaseTime_Object = MibTableColumn
dhcpSnoopBindingsLeaseTime = _DhcpSnoopBindingsLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 46, 4, 1, 1, 7),
    _DhcpSnoopBindingsLeaseTime_Type()
)
dhcpSnoopBindingsLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopBindingsLeaseTime.setStatus("current")
_DhcpSnoopStatistics_ObjectIdentity = ObjectIdentity
dhcpSnoopStatistics = _DhcpSnoopStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 46, 5)
)
_DhcpSnoopTotalForwardedPkts_Type = Counter32
_DhcpSnoopTotalForwardedPkts_Object = MibScalar
dhcpSnoopTotalForwardedPkts = _DhcpSnoopTotalForwardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 46, 5, 1),
    _DhcpSnoopTotalForwardedPkts_Type()
)
dhcpSnoopTotalForwardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopTotalForwardedPkts.setStatus("current")
_DhcpSnoopUntrustedPortDroppedPkts_Type = Counter32
_DhcpSnoopUntrustedPortDroppedPkts_Object = MibScalar
dhcpSnoopUntrustedPortDroppedPkts = _DhcpSnoopUntrustedPortDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 46, 5, 3),
    _DhcpSnoopUntrustedPortDroppedPkts_Type()
)
dhcpSnoopUntrustedPortDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopUntrustedPortDroppedPkts.setStatus("current")
_ClusterMgt_ObjectIdentity = ObjectIdentity
clusterMgt = _ClusterMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 47)
)
_ClusterEnable_Type = EnabledStatus
_ClusterEnable_Object = MibScalar
clusterEnable = _ClusterEnable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 47, 1),
    _ClusterEnable_Type()
)
clusterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clusterEnable.setStatus("current")
_ClusterCommanderEnable_Type = EnabledStatus
_ClusterCommanderEnable_Object = MibScalar
clusterCommanderEnable = _ClusterCommanderEnable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 47, 2),
    _ClusterCommanderEnable_Type()
)
clusterCommanderEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clusterCommanderEnable.setStatus("current")
_ClusterIpPool_Type = IpAddress
_ClusterIpPool_Object = MibScalar
clusterIpPool = _ClusterIpPool_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 47, 4),
    _ClusterIpPool_Type()
)
clusterIpPool.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clusterIpPool.setStatus("current")


class _ClusterClearCandidateTable_Type(Integer32):
    """Custom type clusterClearCandidateTable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("noClear", 1))
    )


_ClusterClearCandidateTable_Type.__name__ = "Integer32"
_ClusterClearCandidateTable_Object = MibScalar
clusterClearCandidateTable = _ClusterClearCandidateTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 47, 5),
    _ClusterClearCandidateTable_Type()
)
clusterClearCandidateTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clusterClearCandidateTable.setStatus("current")


class _ClusterRole_Type(Integer32):
    """Custom type clusterRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("activeMember", 3),
          ("candidate", 2),
          ("commander", 1),
          ("disabled", 5))
    )


_ClusterRole_Type.__name__ = "Integer32"
_ClusterRole_Object = MibScalar
clusterRole = _ClusterRole_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 47, 6),
    _ClusterRole_Type()
)
clusterRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterRole.setStatus("current")
_ClusterMemberCount_Type = Counter32
_ClusterMemberCount_Object = MibScalar
clusterMemberCount = _ClusterMemberCount_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 47, 7),
    _ClusterMemberCount_Type()
)
clusterMemberCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterMemberCount.setStatus("current")
_ClusterCandidateCount_Type = Counter32
_ClusterCandidateCount_Object = MibScalar
clusterCandidateCount = _ClusterCandidateCount_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 47, 8),
    _ClusterCandidateCount_Type()
)
clusterCandidateCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterCandidateCount.setStatus("current")
_ClusterCandidateTable_Object = MibTable
clusterCandidateTable = _ClusterCandidateTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 47, 9)
)
if mibBuilder.loadTexts:
    clusterCandidateTable.setStatus("current")
_ClusterCandidateEntry_Object = MibTableRow
clusterCandidateEntry = _ClusterCandidateEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 47, 9, 1)
)
clusterCandidateEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "clusterCandidateMacAddr"),
)
if mibBuilder.loadTexts:
    clusterCandidateEntry.setStatus("current")
_ClusterCandidateMacAddr_Type = MacAddress
_ClusterCandidateMacAddr_Object = MibTableColumn
clusterCandidateMacAddr = _ClusterCandidateMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 47, 9, 1, 1),
    _ClusterCandidateMacAddr_Type()
)
clusterCandidateMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clusterCandidateMacAddr.setStatus("current")


class _ClusterCandidateDesc_Type(DisplayString):
    """Custom type clusterCandidateDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 42),
    )


_ClusterCandidateDesc_Type.__name__ = "DisplayString"
_ClusterCandidateDesc_Object = MibTableColumn
clusterCandidateDesc = _ClusterCandidateDesc_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 47, 9, 1, 3),
    _ClusterCandidateDesc_Type()
)
clusterCandidateDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterCandidateDesc.setStatus("current")


class _ClusterCandidateRole_Type(Integer32):
    """Custom type clusterCandidateRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("activeMember", 3),
          ("candidate", 2),
          ("inactiveMember", 4))
    )


_ClusterCandidateRole_Type.__name__ = "Integer32"
_ClusterCandidateRole_Object = MibTableColumn
clusterCandidateRole = _ClusterCandidateRole_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 47, 9, 1, 4),
    _ClusterCandidateRole_Type()
)
clusterCandidateRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterCandidateRole.setStatus("current")
_ClusterMemberTable_Object = MibTable
clusterMemberTable = _ClusterMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 47, 10)
)
if mibBuilder.loadTexts:
    clusterMemberTable.setStatus("current")
_ClusterMemberEntry_Object = MibTableRow
clusterMemberEntry = _ClusterMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 47, 10, 1)
)
clusterMemberEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "clusterMemberId"),
)
if mibBuilder.loadTexts:
    clusterMemberEntry.setStatus("current")
_ClusterMemberId_Type = Unsigned32
_ClusterMemberId_Object = MibTableColumn
clusterMemberId = _ClusterMemberId_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 47, 10, 1, 1),
    _ClusterMemberId_Type()
)
clusterMemberId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clusterMemberId.setStatus("current")
_ClusterMemberMacAddr_Type = MacAddress
_ClusterMemberMacAddr_Object = MibTableColumn
clusterMemberMacAddr = _ClusterMemberMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 47, 10, 1, 2),
    _ClusterMemberMacAddr_Type()
)
clusterMemberMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterMemberMacAddr.setStatus("current")


class _ClusterMemberDesc_Type(DisplayString):
    """Custom type clusterMemberDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 42),
    )


_ClusterMemberDesc_Type.__name__ = "DisplayString"
_ClusterMemberDesc_Object = MibTableColumn
clusterMemberDesc = _ClusterMemberDesc_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 47, 10, 1, 3),
    _ClusterMemberDesc_Type()
)
clusterMemberDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterMemberDesc.setStatus("current")


class _ClusterMemberActive_Type(Integer32):
    """Custom type clusterMemberActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("activeMember", 3),
          ("inactiveMember", 4))
    )


_ClusterMemberActive_Type.__name__ = "Integer32"
_ClusterMemberActive_Object = MibTableColumn
clusterMemberActive = _ClusterMemberActive_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 47, 10, 1, 4),
    _ClusterMemberActive_Type()
)
clusterMemberActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterMemberActive.setStatus("current")
_ClusterMemberAddCtl_ObjectIdentity = ObjectIdentity
clusterMemberAddCtl = _ClusterMemberAddCtl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 47, 11)
)
_ClusterMemberAddCtlMacAddr_Type = MacAddress
_ClusterMemberAddCtlMacAddr_Object = MibScalar
clusterMemberAddCtlMacAddr = _ClusterMemberAddCtlMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 47, 11, 1),
    _ClusterMemberAddCtlMacAddr_Type()
)
clusterMemberAddCtlMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clusterMemberAddCtlMacAddr.setStatus("current")
_ClusterMemberAddCtlId_Type = Unsigned32
_ClusterMemberAddCtlId_Object = MibScalar
clusterMemberAddCtlId = _ClusterMemberAddCtlId_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 47, 11, 2),
    _ClusterMemberAddCtlId_Type()
)
clusterMemberAddCtlId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clusterMemberAddCtlId.setStatus("current")


class _ClusterMemberAddCtlAction_Type(Integer32):
    """Custom type clusterMemberAddCtlAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("add", 2),
          ("noAdd", 1))
    )


_ClusterMemberAddCtlAction_Type.__name__ = "Integer32"
_ClusterMemberAddCtlAction_Object = MibScalar
clusterMemberAddCtlAction = _ClusterMemberAddCtlAction_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 47, 11, 5),
    _ClusterMemberAddCtlAction_Type()
)
clusterMemberAddCtlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clusterMemberAddCtlAction.setStatus("current")
_ClusterMemberRemoveCtl_ObjectIdentity = ObjectIdentity
clusterMemberRemoveCtl = _ClusterMemberRemoveCtl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 47, 12)
)
_ClusterMemberRemoveCtlId_Type = Unsigned32
_ClusterMemberRemoveCtlId_Object = MibScalar
clusterMemberRemoveCtlId = _ClusterMemberRemoveCtlId_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 47, 12, 1),
    _ClusterMemberRemoveCtlId_Type()
)
clusterMemberRemoveCtlId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clusterMemberRemoveCtlId.setStatus("current")


class _ClusterMemberRemoveCtlAction_Type(Integer32):
    """Custom type clusterMemberRemoveCtlAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noRemove", 1),
          ("remove", 2))
    )


_ClusterMemberRemoveCtlAction_Type.__name__ = "Integer32"
_ClusterMemberRemoveCtlAction_Object = MibScalar
clusterMemberRemoveCtlAction = _ClusterMemberRemoveCtlAction_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 47, 12, 2),
    _ClusterMemberRemoveCtlAction_Type()
)
clusterMemberRemoveCtlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clusterMemberRemoveCtlAction.setStatus("current")
_IpSrcGuardMgt_ObjectIdentity = ObjectIdentity
ipSrcGuardMgt = _IpSrcGuardMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 48)
)
_IpSrcGuardConfigTable_Object = MibTable
ipSrcGuardConfigTable = _IpSrcGuardConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 48, 1)
)
if mibBuilder.loadTexts:
    ipSrcGuardConfigTable.setStatus("current")
_IpSrcGuardConfigEntry_Object = MibTableRow
ipSrcGuardConfigEntry = _IpSrcGuardConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 48, 1, 1)
)
ipSrcGuardConfigEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "ipSrcGuardPortIfIndex"),
)
if mibBuilder.loadTexts:
    ipSrcGuardConfigEntry.setStatus("current")
_IpSrcGuardPortIfIndex_Type = InterfaceIndex
_IpSrcGuardPortIfIndex_Object = MibTableColumn
ipSrcGuardPortIfIndex = _IpSrcGuardPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 48, 1, 1, 1),
    _IpSrcGuardPortIfIndex_Type()
)
ipSrcGuardPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipSrcGuardPortIfIndex.setStatus("current")


class _IpSrcGuardMode_Type(Integer32):
    """Custom type ipSrcGuardMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("diabled", 0),
          ("srcIp", 1),
          ("srcIpMac", 2))
    )


_IpSrcGuardMode_Type.__name__ = "Integer32"
_IpSrcGuardMode_Object = MibTableColumn
ipSrcGuardMode = _IpSrcGuardMode_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 48, 1, 1, 2),
    _IpSrcGuardMode_Type()
)
ipSrcGuardMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSrcGuardMode.setStatus("current")
_IpSrcGuardAddrTable_Object = MibTable
ipSrcGuardAddrTable = _IpSrcGuardAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 48, 2)
)
if mibBuilder.loadTexts:
    ipSrcGuardAddrTable.setStatus("current")
_IpSrcGuardAddrEntry_Object = MibTableRow
ipSrcGuardAddrEntry = _IpSrcGuardAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 48, 2, 1)
)
ipSrcGuardAddrEntry.setIndexNames(
    (0, "ES3526XA_ES3510-MIB", "ipSrcGuardBindingsVlanIndex"),
    (0, "ES3526XA_ES3510-MIB", "ipSrcGuardBindingsMacAddress"),
)
if mibBuilder.loadTexts:
    ipSrcGuardAddrEntry.setStatus("current")
_IpSrcGuardBindingsVlanIndex_Type = VlanIndex
_IpSrcGuardBindingsVlanIndex_Object = MibTableColumn
ipSrcGuardBindingsVlanIndex = _IpSrcGuardBindingsVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 48, 2, 1, 1),
    _IpSrcGuardBindingsVlanIndex_Type()
)
ipSrcGuardBindingsVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipSrcGuardBindingsVlanIndex.setStatus("current")
_IpSrcGuardBindingsMacAddress_Type = MacAddress
_IpSrcGuardBindingsMacAddress_Object = MibTableColumn
ipSrcGuardBindingsMacAddress = _IpSrcGuardBindingsMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 48, 2, 1, 2),
    _IpSrcGuardBindingsMacAddress_Type()
)
ipSrcGuardBindingsMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipSrcGuardBindingsMacAddress.setStatus("current")
_IpSrcGuardBindingsAddrType_Type = InetAddressType
_IpSrcGuardBindingsAddrType_Object = MibTableColumn
ipSrcGuardBindingsAddrType = _IpSrcGuardBindingsAddrType_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 48, 2, 1, 3),
    _IpSrcGuardBindingsAddrType_Type()
)
ipSrcGuardBindingsAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipSrcGuardBindingsAddrType.setStatus("current")


class _IpSrcGuardBindingsEntryType_Type(Integer32):
    """Custom type ipSrcGuardBindingsEntryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 3))
    )


_IpSrcGuardBindingsEntryType_Type.__name__ = "Integer32"
_IpSrcGuardBindingsEntryType_Object = MibTableColumn
ipSrcGuardBindingsEntryType = _IpSrcGuardBindingsEntryType_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 48, 2, 1, 4),
    _IpSrcGuardBindingsEntryType_Type()
)
ipSrcGuardBindingsEntryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSrcGuardBindingsEntryType.setStatus("current")
_IpSrcGuardBindingsIpAddress_Type = IpAddress
_IpSrcGuardBindingsIpAddress_Object = MibTableColumn
ipSrcGuardBindingsIpAddress = _IpSrcGuardBindingsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 48, 2, 1, 5),
    _IpSrcGuardBindingsIpAddress_Type()
)
ipSrcGuardBindingsIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipSrcGuardBindingsIpAddress.setStatus("current")
_IpSrcGuardBindingsPortIfIndex_Type = InterfaceIndex
_IpSrcGuardBindingsPortIfIndex_Object = MibTableColumn
ipSrcGuardBindingsPortIfIndex = _IpSrcGuardBindingsPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 48, 2, 1, 6),
    _IpSrcGuardBindingsPortIfIndex_Type()
)
ipSrcGuardBindingsPortIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipSrcGuardBindingsPortIfIndex.setStatus("current")
_IpSrcGuardBindingsLeaseTime_Type = Unsigned32
_IpSrcGuardBindingsLeaseTime_Object = MibTableColumn
ipSrcGuardBindingsLeaseTime = _IpSrcGuardBindingsLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 48, 2, 1, 7),
    _IpSrcGuardBindingsLeaseTime_Type()
)
ipSrcGuardBindingsLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSrcGuardBindingsLeaseTime.setStatus("current")
_IpSrcGuardBindingsStatus_Type = RowStatus
_IpSrcGuardBindingsStatus_Object = MibTableColumn
ipSrcGuardBindingsStatus = _IpSrcGuardBindingsStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 1, 48, 2, 1, 8),
    _IpSrcGuardBindingsStatus_Type()
)
ipSrcGuardBindingsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipSrcGuardBindingsStatus.setStatus("current")
_Es3526XA_ES3510Notifications_ObjectIdentity = ObjectIdentity
es3526XA_ES3510Notifications = _Es3526XA_ES3510Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 2)
)
_Es3526XA_ES3510Traps_ObjectIdentity = ObjectIdentity
es3526XA_ES3510Traps = _Es3526XA_ES3510Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 2, 1)
)
_Es3526XA_ES3510TrapsPrefix_ObjectIdentity = ObjectIdentity
es3526XA_ES3510TrapsPrefix = _Es3526XA_ES3510TrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 2, 1, 0)
)
_Es3526XA_ES3510Conformance_ObjectIdentity = ObjectIdentity
es3526XA_ES3510Conformance = _Es3526XA_ES3510Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 3)
)

# Managed Objects groups


# Notification objects

swPowerStatusChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 2, 1, 0, 1)
)
swPowerStatusChangeTrap.setObjects(
      *(("ES3526XA_ES3510-MIB", "swIndivPowerUnitIndex"),
        ("ES3526XA_ES3510-MIB", "swIndivPowerIndex"),
        ("ES3526XA_ES3510-MIB", "swIndivPowerStatus"))
)
if mibBuilder.loadTexts:
    swPowerStatusChangeTrap.setStatus(
        "current"
    )

swIpFilterRejectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 2, 1, 0, 40)
)
swIpFilterRejectTrap.setObjects(
      *(("ES3526XA_ES3510-MIB", "trapIpFilterRejectMode"),
        ("ES3526XA_ES3510-MIB", "trapIpFilterRejectIp"))
)
if mibBuilder.loadTexts:
    swIpFilterRejectTrap.setStatus(
        "current"
    )

swSmtpConnFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 2, 1, 0, 41)
)
swSmtpConnFailureTrap.setObjects(
    ("ES3526XA_ES3510-MIB", "smtpServerIp")
)
if mibBuilder.loadTexts:
    swSmtpConnFailureTrap.setStatus(
        "current"
    )

swAuthenticationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 2, 1, 0, 66)
)
swAuthenticationFailure.setObjects(
      *(("ES3526XA_ES3510-MIB", "trapVarLoginUserName"),
        ("ES3526XA_ES3510-MIB", "trapVarLoginMethod"),
        ("ES3526XA_ES3510-MIB", "trapVarLoginIPAddress"),
        ("ES3526XA_ES3510-MIB", "trapVarLoginTime"))
)
if mibBuilder.loadTexts:
    swAuthenticationFailure.setStatus(
        "current"
    )

swAuthenticationSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 2, 1, 0, 67)
)
swAuthenticationSuccess.setObjects(
      *(("ES3526XA_ES3510-MIB", "trapVarLoginUserName"),
        ("ES3526XA_ES3510-MIB", "trapVarLoginMethod"),
        ("ES3526XA_ES3510-MIB", "trapVarLoginIPAddress"),
        ("ES3526XA_ES3510-MIB", "trapVarLoginTime"))
)
if mibBuilder.loadTexts:
    swAuthenticationSuccess.setStatus(
        "current"
    )

swVlanChangeStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 5, 2, 1, 0, 251)
)
swVlanChangeStatus.setObjects(
      *(("ES3526XA_ES3510-MIB", "vlanChangeStatus"),
        ("ES3526XA_ES3510-MIB", "vlanChangeVlan"),
        ("ES3526XA_ES3510-MIB", "vlanChangePortIfIndex"))
)
if mibBuilder.loadTexts:
    swVlanChangeStatus.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ES3526XA_ES3510-MIB",
    **{"KeySegment": KeySegment,
       "ValidStatus": ValidStatus,
       "StaPathCostMode": StaPathCostMode,
       "accton": accton,
       "edgecore": edgecore,
       "cheetahSwitchMgt": cheetahSwitchMgt,
       "es3526XA_ES3510MIB": es3526XA_ES3510MIB,
       "es3526XA_ES3510MIBObjects": es3526XA_ES3510MIBObjects,
       "switchMgt": switchMgt,
       "switchManagementVlan": switchManagementVlan,
       "switchNumber": switchNumber,
       "switchInfoTable": switchInfoTable,
       "switchInfoEntry": switchInfoEntry,
       "swUnitIndex": swUnitIndex,
       "swHardwareVer": swHardwareVer,
       "swMicrocodeVer": swMicrocodeVer,
       "swLoaderVer": swLoaderVer,
       "swBootRomVer": swBootRomVer,
       "swOpCodeVer": swOpCodeVer,
       "swPortNumber": swPortNumber,
       "swPowerStatus": swPowerStatus,
       "swRoleInSystem": swRoleInSystem,
       "swSerialNumber": swSerialNumber,
       "swServiceTag": swServiceTag,
       "switchOperState": switchOperState,
       "switchProductId": switchProductId,
       "swProdName": swProdName,
       "swProdManufacturer": swProdManufacturer,
       "swProdDescription": swProdDescription,
       "swProdVersion": swProdVersion,
       "swProdUrl": swProdUrl,
       "swIdentifier": swIdentifier,
       "swChassisServiceTag": swChassisServiceTag,
       "amtrMgt": amtrMgt,
       "amtrMacAddrAgingStatus": amtrMacAddrAgingStatus,
       "amtrMacAddrDelete": amtrMacAddrDelete,
       "portMgt": portMgt,
       "portTable": portTable,
       "portEntry": portEntry,
       "portIndex": portIndex,
       "portName": portName,
       "portType": portType,
       "portSpeedDpxCfg": portSpeedDpxCfg,
       "portFlowCtrlCfg": portFlowCtrlCfg,
       "portCapabilities": portCapabilities,
       "portAutonegotiation": portAutonegotiation,
       "portSpeedDpxStatus": portSpeedDpxStatus,
       "portFlowCtrlStatus": portFlowCtrlStatus,
       "portTrunkIndex": portTrunkIndex,
       "trunkMgt": trunkMgt,
       "trunkMaxId": trunkMaxId,
       "trunkValidNumber": trunkValidNumber,
       "trunkTable": trunkTable,
       "trunkEntry": trunkEntry,
       "trunkIndex": trunkIndex,
       "trunkPorts": trunkPorts,
       "trunkCreation": trunkCreation,
       "trunkStatus": trunkStatus,
       "lacpMgt": lacpMgt,
       "lacpPortTable": lacpPortTable,
       "lacpPortEntry": lacpPortEntry,
       "lacpPortIndex": lacpPortIndex,
       "lacpPortStatus": lacpPortStatus,
       "staMgt": staMgt,
       "staSystemStatus": staSystemStatus,
       "staPortTable": staPortTable,
       "staPortEntry": staPortEntry,
       "staPortIndex": staPortIndex,
       "staPortFastForward": staPortFastForward,
       "staPortProtocolMigration": staPortProtocolMigration,
       "staPortAdminEdgePort": staPortAdminEdgePort,
       "staPortOperEdgePort": staPortOperEdgePort,
       "staPortAdminPointToPoint": staPortAdminPointToPoint,
       "staPortOperPointToPoint": staPortOperPointToPoint,
       "staPortLongPathCost": staPortLongPathCost,
       "staPortSystemStatus": staPortSystemStatus,
       "staProtocolType": staProtocolType,
       "staTxHoldCount": staTxHoldCount,
       "staPathCostMethod": staPathCostMethod,
       "xstMgt": xstMgt,
       "mstName": mstName,
       "mstRevision": mstRevision,
       "mstMaxHops": mstMaxHops,
       "xstInstanceCfgTable": xstInstanceCfgTable,
       "xstInstanceCfgEntry": xstInstanceCfgEntry,
       "xstInstanceCfgIndex": xstInstanceCfgIndex,
       "xstInstanceCfgPriority": xstInstanceCfgPriority,
       "xstInstanceCfgTimeSinceTopologyChange": xstInstanceCfgTimeSinceTopologyChange,
       "xstInstanceCfgTopChanges": xstInstanceCfgTopChanges,
       "xstInstanceCfgDesignatedRoot": xstInstanceCfgDesignatedRoot,
       "xstInstanceCfgRootCost": xstInstanceCfgRootCost,
       "xstInstanceCfgRootPort": xstInstanceCfgRootPort,
       "xstInstanceCfgMaxAge": xstInstanceCfgMaxAge,
       "xstInstanceCfgHelloTime": xstInstanceCfgHelloTime,
       "xstInstanceCfgHoldTime": xstInstanceCfgHoldTime,
       "xstInstanceCfgForwardDelay": xstInstanceCfgForwardDelay,
       "xstInstanceCfgBridgeMaxAge": xstInstanceCfgBridgeMaxAge,
       "xstInstanceCfgBridgeHelloTime": xstInstanceCfgBridgeHelloTime,
       "xstInstanceCfgBridgeForwardDelay": xstInstanceCfgBridgeForwardDelay,
       "xstInstanceCfgTxHoldCount": xstInstanceCfgTxHoldCount,
       "xstInstanceCfgPathCostMethod": xstInstanceCfgPathCostMethod,
       "xstInstancePortTable": xstInstancePortTable,
       "xstInstancePortEntry": xstInstancePortEntry,
       "xstInstancePortInstance": xstInstancePortInstance,
       "xstInstancePortPort": xstInstancePortPort,
       "xstInstancePortPriority": xstInstancePortPriority,
       "xstInstancePortState": xstInstancePortState,
       "xstInstancePortEnable": xstInstancePortEnable,
       "xstInstancePortPathCost": xstInstancePortPathCost,
       "xstInstancePortDesignatedRoot": xstInstancePortDesignatedRoot,
       "xstInstancePortDesignatedCost": xstInstancePortDesignatedCost,
       "xstInstancePortDesignatedBridge": xstInstancePortDesignatedBridge,
       "xstInstancePortDesignatedPort": xstInstancePortDesignatedPort,
       "xstInstancePortForwardTransitions": xstInstancePortForwardTransitions,
       "xstInstancePortPortRole": xstInstancePortPortRole,
       "mstInstanceEditTable": mstInstanceEditTable,
       "mstInstanceEditEntry": mstInstanceEditEntry,
       "mstInstanceEditIndex": mstInstanceEditIndex,
       "mstInstanceEditVlansMap": mstInstanceEditVlansMap,
       "mstInstanceEditVlansMap2k": mstInstanceEditVlansMap2k,
       "mstInstanceEditVlansMap3k": mstInstanceEditVlansMap3k,
       "mstInstanceEditVlansMap4k": mstInstanceEditVlansMap4k,
       "mstInstanceEditRemainingHops": mstInstanceEditRemainingHops,
       "mstInstanceOperTable": mstInstanceOperTable,
       "mstInstanceOperEntry": mstInstanceOperEntry,
       "mstInstanceOperIndex": mstInstanceOperIndex,
       "mstInstanceOperVlansMap": mstInstanceOperVlansMap,
       "mstInstanceOperVlansMap2k": mstInstanceOperVlansMap2k,
       "mstInstanceOperVlansMap3k": mstInstanceOperVlansMap3k,
       "mstInstanceOperVlansMap4k": mstInstanceOperVlansMap4k,
       "staLoopbackDetectionPortTable": staLoopbackDetectionPortTable,
       "staLoopbackDetectionPortEntry": staLoopbackDetectionPortEntry,
       "staLoopbackDetectionPortIfIndex": staLoopbackDetectionPortIfIndex,
       "staLoopbackDetectionPortStatus": staLoopbackDetectionPortStatus,
       "staLoopbackDetectionPortTrapStatus": staLoopbackDetectionPortTrapStatus,
       "staLoopbackDetectionPortReleaseMode": staLoopbackDetectionPortReleaseMode,
       "staLoopbackDetectionPortRelease": staLoopbackDetectionPortRelease,
       "tftpMgt": tftpMgt,
       "tftpFileType": tftpFileType,
       "tftpSrcFile": tftpSrcFile,
       "tftpDestFile": tftpDestFile,
       "tftpServer": tftpServer,
       "tftpAction": tftpAction,
       "tftpStatus": tftpStatus,
       "restartMgt": restartMgt,
       "restartOpCodeFile": restartOpCodeFile,
       "restartConfigFile": restartConfigFile,
       "restartControl": restartControl,
       "mirrorMgt": mirrorMgt,
       "mirrorTable": mirrorTable,
       "mirrorEntry": mirrorEntry,
       "mirrorDestinationPort": mirrorDestinationPort,
       "mirrorSourcePort": mirrorSourcePort,
       "mirrorType": mirrorType,
       "mirrorStatus": mirrorStatus,
       "igmpSnoopMgt": igmpSnoopMgt,
       "igmpSnoopStatus": igmpSnoopStatus,
       "igmpSnoopQuerier": igmpSnoopQuerier,
       "igmpSnoopQueryCount": igmpSnoopQueryCount,
       "igmpSnoopQueryInterval": igmpSnoopQueryInterval,
       "igmpSnoopQueryMaxResponseTime": igmpSnoopQueryMaxResponseTime,
       "igmpSnoopQueryTimeout": igmpSnoopQueryTimeout,
       "igmpSnoopVersion": igmpSnoopVersion,
       "igmpSnoopRouterCurrentTable": igmpSnoopRouterCurrentTable,
       "igmpSnoopRouterCurrentEntry": igmpSnoopRouterCurrentEntry,
       "igmpSnoopRouterCurrentVlanIndex": igmpSnoopRouterCurrentVlanIndex,
       "igmpSnoopRouterCurrentPorts": igmpSnoopRouterCurrentPorts,
       "igmpSnoopRouterCurrentStatus": igmpSnoopRouterCurrentStatus,
       "igmpSnoopRouterStaticTable": igmpSnoopRouterStaticTable,
       "igmpSnoopRouterStaticEntry": igmpSnoopRouterStaticEntry,
       "igmpSnoopRouterStaticVlanIndex": igmpSnoopRouterStaticVlanIndex,
       "igmpSnoopRouterStaticPorts": igmpSnoopRouterStaticPorts,
       "igmpSnoopRouterStaticStatus": igmpSnoopRouterStaticStatus,
       "igmpSnoopMulticastCurrentTable": igmpSnoopMulticastCurrentTable,
       "igmpSnoopMulticastCurrentEntry": igmpSnoopMulticastCurrentEntry,
       "igmpSnoopMulticastCurrentVlanIndex": igmpSnoopMulticastCurrentVlanIndex,
       "igmpSnoopMulticastCurrentIpAddress": igmpSnoopMulticastCurrentIpAddress,
       "igmpSnoopMulticastCurrentPorts": igmpSnoopMulticastCurrentPorts,
       "igmpSnoopMulticastCurrentStatus": igmpSnoopMulticastCurrentStatus,
       "igmpSnoopMulticastStaticTable": igmpSnoopMulticastStaticTable,
       "igmpSnoopMulticastStaticEntry": igmpSnoopMulticastStaticEntry,
       "igmpSnoopMulticastStaticVlanIndex": igmpSnoopMulticastStaticVlanIndex,
       "igmpSnoopMulticastStaticIpAddress": igmpSnoopMulticastStaticIpAddress,
       "igmpSnoopMulticastStaticPorts": igmpSnoopMulticastStaticPorts,
       "igmpSnoopMulticastStaticStatus": igmpSnoopMulticastStaticStatus,
       "igmpSnoopCurrentVlanTable": igmpSnoopCurrentVlanTable,
       "igmpSnoopCurrentVlanEntry": igmpSnoopCurrentVlanEntry,
       "igmpSnoopCurrentVlanIndex": igmpSnoopCurrentVlanIndex,
       "igmpSnoopCurrentVlanImmediateLeave": igmpSnoopCurrentVlanImmediateLeave,
       "igmpSnoopLeaveProxy": igmpSnoopLeaveProxy,
       "igmpSnoopFilterStatus": igmpSnoopFilterStatus,
       "igmpSnoopProfileTable": igmpSnoopProfileTable,
       "igmpSnoopProfileEntry": igmpSnoopProfileEntry,
       "igmpSnoopProfileId": igmpSnoopProfileId,
       "igmpSnoopProfileAction": igmpSnoopProfileAction,
       "igmpSnoopProfileStatus": igmpSnoopProfileStatus,
       "igmpSnoopProfileCtl": igmpSnoopProfileCtl,
       "igmpSnoopProfileCtlId": igmpSnoopProfileCtlId,
       "igmpSnoopProfileCtlInetAddressType": igmpSnoopProfileCtlInetAddressType,
       "igmpSnoopProfileCtlStartInetAddress": igmpSnoopProfileCtlStartInetAddress,
       "igmpSnoopProfileCtlEndInetAddress": igmpSnoopProfileCtlEndInetAddress,
       "igmpSnoopProfileCtlAction": igmpSnoopProfileCtlAction,
       "igmpSnoopProfileRangeTable": igmpSnoopProfileRangeTable,
       "igmpSnoopProfileRangeEntry": igmpSnoopProfileRangeEntry,
       "igmpSnoopProfileRangeProfileId": igmpSnoopProfileRangeProfileId,
       "igmpSnoopProfileRangeInetAddressType": igmpSnoopProfileRangeInetAddressType,
       "igmpSnoopProfileRangeStartInetAddress": igmpSnoopProfileRangeStartInetAddress,
       "igmpSnoopProfileRangeEndInetAddress": igmpSnoopProfileRangeEndInetAddress,
       "igmpSnoopProfileRangeAction": igmpSnoopProfileRangeAction,
       "igmpSnoopFilterPortTable": igmpSnoopFilterPortTable,
       "igmpSnoopFilterPortEntry": igmpSnoopFilterPortEntry,
       "igmpSnoopFilterPortIndex": igmpSnoopFilterPortIndex,
       "igmpSnoopFilterPortProfileId": igmpSnoopFilterPortProfileId,
       "igmpSnoopThrottlePortTable": igmpSnoopThrottlePortTable,
       "igmpSnoopThrottlePortEntry": igmpSnoopThrottlePortEntry,
       "igmpSnoopThrottlePortIndex": igmpSnoopThrottlePortIndex,
       "igmpSnoopThrottlePortRunningStatus": igmpSnoopThrottlePortRunningStatus,
       "igmpSnoopThrottlePortAction": igmpSnoopThrottlePortAction,
       "igmpSnoopThrottlePortMaxGroups": igmpSnoopThrottlePortMaxGroups,
       "igmpSnoopThrottlePortCurrentGroups": igmpSnoopThrottlePortCurrentGroups,
       "ipMgt": ipMgt,
       "netConfigTable": netConfigTable,
       "netConfigEntry": netConfigEntry,
       "netConfigIfIndex": netConfigIfIndex,
       "netConfigIPAddress": netConfigIPAddress,
       "netConfigSubnetMask": netConfigSubnetMask,
       "netConfigPrimaryInterface": netConfigPrimaryInterface,
       "netConfigUnnumbered": netConfigUnnumbered,
       "netConfigStatus": netConfigStatus,
       "netDefaultGateway": netDefaultGateway,
       "ipHttpState": ipHttpState,
       "ipHttpPort": ipHttpPort,
       "ipDhcpRestart": ipDhcpRestart,
       "ipHttpsState": ipHttpsState,
       "ipHttpsPort": ipHttpsPort,
       "pingMgt": pingMgt,
       "pingIpAddress": pingIpAddress,
       "pingPacketSize": pingPacketSize,
       "pingRoundTripTime": pingRoundTripTime,
       "pingCompleted": pingCompleted,
       "pingAction": pingAction,
       "bcastStormMgt": bcastStormMgt,
       "bcastStormTable": bcastStormTable,
       "bcastStormEntry": bcastStormEntry,
       "bcastStormIfIndex": bcastStormIfIndex,
       "bcastStormStatus": bcastStormStatus,
       "bcastStormOctetRateScale": bcastStormOctetRateScale,
       "bcastStormOctetRateLevel": bcastStormOctetRateLevel,
       "vlanMgt": vlanMgt,
       "vlanTable": vlanTable,
       "vlanEntry": vlanEntry,
       "vlanIndex": vlanIndex,
       "vlanAddressMethod": vlanAddressMethod,
       "vlanPortTable": vlanPortTable,
       "vlanPortEntry": vlanPortEntry,
       "vlanPortIndex": vlanPortIndex,
       "vlanPortMode": vlanPortMode,
       "vlanPortPrivateVlanType": vlanPortPrivateVlanType,
       "priorityMgt": priorityMgt,
       "prioIpPrecDscpStatus": prioIpPrecDscpStatus,
       "prioIpPrecTable": prioIpPrecTable,
       "prioIpPrecEntry": prioIpPrecEntry,
       "prioIpPrecPort": prioIpPrecPort,
       "prioIpPrecValue": prioIpPrecValue,
       "prioIpPrecCos": prioIpPrecCos,
       "prioIpPrecRestoreDefault": prioIpPrecRestoreDefault,
       "prioIpDscpTable": prioIpDscpTable,
       "prioIpDscpEntry": prioIpDscpEntry,
       "prioIpDscpPort": prioIpDscpPort,
       "prioIpDscpValue": prioIpDscpValue,
       "prioIpDscpCos": prioIpDscpCos,
       "prioIpDscpRestoreDefault": prioIpDscpRestoreDefault,
       "prioIpPortEnableStatus": prioIpPortEnableStatus,
       "prioIpPortTable": prioIpPortTable,
       "prioIpPortEntry": prioIpPortEntry,
       "prioIpPortPhysPort": prioIpPortPhysPort,
       "prioIpPortValue": prioIpPortValue,
       "prioIpPortCos": prioIpPortCos,
       "prioIpPortStatus": prioIpPortStatus,
       "prioCopy": prioCopy,
       "prioCopyIpPrec": prioCopyIpPrec,
       "prioCopyIpDscp": prioCopyIpDscp,
       "prioCopyIpPort": prioCopyIpPort,
       "prioWrrTable": prioWrrTable,
       "prioWrrEntry": prioWrrEntry,
       "prioWrrTrafficClass": prioWrrTrafficClass,
       "prioWrrWeight": prioWrrWeight,
       "prioQueueMode": prioQueueMode,
       "prioIpTosTable": prioIpTosTable,
       "prioIpTosEntry": prioIpTosEntry,
       "prioIpTosPort": prioIpTosPort,
       "prioIpTosValue": prioIpTosValue,
       "prioIpTosCos": prioIpTosCos,
       "prioIpTosRestoreDefault": prioIpTosRestoreDefault,
       "trapDestMgt": trapDestMgt,
       "trapDestTable": trapDestTable,
       "trapDestEntry": trapDestEntry,
       "trapDestAddress": trapDestAddress,
       "trapDestCommunity": trapDestCommunity,
       "trapDestStatus": trapDestStatus,
       "trapDestVersion": trapDestVersion,
       "trapDestUdpPort": trapDestUdpPort,
       "qosMgt": qosMgt,
       "rateLimitMgt": rateLimitMgt,
       "rateLimitPortTable": rateLimitPortTable,
       "rateLimitPortEntry": rateLimitPortEntry,
       "rlPortIndex": rlPortIndex,
       "rlPortInputStatus": rlPortInputStatus,
       "rlPortOutputStatus": rlPortOutputStatus,
       "rlPortInputLevel": rlPortInputLevel,
       "rlPortInputScale": rlPortInputScale,
       "rlPortOutputLevel": rlPortOutputLevel,
       "rlPortOutputScale": rlPortOutputScale,
       "cosMgt": cosMgt,
       "prioAclToCosMappingTable": prioAclToCosMappingTable,
       "prioAclToCosMappingEntry": prioAclToCosMappingEntry,
       "prioAclToCosMappingIfIndex": prioAclToCosMappingIfIndex,
       "prioAclToCosMappingAclName": prioAclToCosMappingAclName,
       "prioAclToCosMappingCosValue": prioAclToCosMappingCosValue,
       "prioAclToCosMappingStatus": prioAclToCosMappingStatus,
       "diffServMgt": diffServMgt,
       "diffServPortTable": diffServPortTable,
       "diffServPortEntry": diffServPortEntry,
       "diffServPortIfIndex": diffServPortIfIndex,
       "diffServPortPolicyMapIndex": diffServPortPolicyMapIndex,
       "diffServPortIngressIpAclIndex": diffServPortIngressIpAclIndex,
       "diffServPortIngressMacAclIndex": diffServPortIngressMacAclIndex,
       "diffServPolicyMapTable": diffServPolicyMapTable,
       "diffServPolicyMapEntry": diffServPolicyMapEntry,
       "diffServPolicyMapIndex": diffServPolicyMapIndex,
       "diffServPolicyMapName": diffServPolicyMapName,
       "diffServPolicyMapDescription": diffServPolicyMapDescription,
       "diffServPolicyMapElementIndexList": diffServPolicyMapElementIndexList,
       "diffServPolicyMapStatus": diffServPolicyMapStatus,
       "diffServPolicyMapAttachCtl": diffServPolicyMapAttachCtl,
       "diffServPolicyMapAttachCtlIndex": diffServPolicyMapAttachCtlIndex,
       "diffServPolicyMapAttachCtlElementIndex": diffServPolicyMapAttachCtlElementIndex,
       "diffServPolicyMapAttachCtlAction": diffServPolicyMapAttachCtlAction,
       "diffServPolicyMapElementTable": diffServPolicyMapElementTable,
       "diffServPolicyMapElementEntry": diffServPolicyMapElementEntry,
       "diffServPolicyMapElementIndex": diffServPolicyMapElementIndex,
       "diffServPolicyMapElementClassMapIndex": diffServPolicyMapElementClassMapIndex,
       "diffServPolicyMapElementMeterIndex": diffServPolicyMapElementMeterIndex,
       "diffServPolicyMapElementActionIndex": diffServPolicyMapElementActionIndex,
       "diffServPolicyMapElementStatus": diffServPolicyMapElementStatus,
       "diffServClassMapTable": diffServClassMapTable,
       "diffServClassMapEntry": diffServClassMapEntry,
       "diffServClassMapIndex": diffServClassMapIndex,
       "diffServClassMapName": diffServClassMapName,
       "diffServClassMapDescription": diffServClassMapDescription,
       "diffServClassMapMatchType": diffServClassMapMatchType,
       "diffServClassMapElementIndexTypeList": diffServClassMapElementIndexTypeList,
       "diffServClassMapElementIndexList": diffServClassMapElementIndexList,
       "diffServClassMapStatus": diffServClassMapStatus,
       "diffServClassMapAttachCtl": diffServClassMapAttachCtl,
       "diffServClassMapAttachCtlIndex": diffServClassMapAttachCtlIndex,
       "diffServClassMapAttachCtlElementIndexType": diffServClassMapAttachCtlElementIndexType,
       "diffServClassMapAttachCtlElementIndex": diffServClassMapAttachCtlElementIndex,
       "diffServClassMapAttachCtlAction": diffServClassMapAttachCtlAction,
       "diffServAclTable": diffServAclTable,
       "diffServAclEntry": diffServAclEntry,
       "diffServAclIndex": diffServAclIndex,
       "diffServAclName": diffServAclName,
       "diffServAclType": diffServAclType,
       "diffServAclAceIndexList": diffServAclAceIndexList,
       "diffServAclStatus": diffServAclStatus,
       "diffServAclAttachCtl": diffServAclAttachCtl,
       "diffServAclAttachCtlIndex": diffServAclAttachCtlIndex,
       "diffServAclAttachCtlAceType": diffServAclAttachCtlAceType,
       "diffServAclAttachCtlAceIndex": diffServAclAttachCtlAceIndex,
       "diffServAclAttachCtlAction": diffServAclAttachCtlAction,
       "diffServIpAceTable": diffServIpAceTable,
       "diffServIpAceEntry": diffServIpAceEntry,
       "diffServIpAceIndex": diffServIpAceIndex,
       "diffServIpAceType": diffServIpAceType,
       "diffServIpAceAccess": diffServIpAceAccess,
       "diffServIpAceSourceIpAddr": diffServIpAceSourceIpAddr,
       "diffServIpAceSourceIpAddrBitmask": diffServIpAceSourceIpAddrBitmask,
       "diffServIpAceDestIpAddr": diffServIpAceDestIpAddr,
       "diffServIpAceDestIpAddrBitmask": diffServIpAceDestIpAddrBitmask,
       "diffServIpAceProtocol": diffServIpAceProtocol,
       "diffServIpAcePrec": diffServIpAcePrec,
       "diffServIpAceTos": diffServIpAceTos,
       "diffServIpAceDscp": diffServIpAceDscp,
       "diffServIpAceSourcePortOp": diffServIpAceSourcePortOp,
       "diffServIpAceMinSourcePort": diffServIpAceMinSourcePort,
       "diffServIpAceMaxSourcePort": diffServIpAceMaxSourcePort,
       "diffServIpAceSourcePortBitmask": diffServIpAceSourcePortBitmask,
       "diffServIpAceDestPortOp": diffServIpAceDestPortOp,
       "diffServIpAceMinDestPort": diffServIpAceMinDestPort,
       "diffServIpAceMaxDestPort": diffServIpAceMaxDestPort,
       "diffServIpAceDestPortBitmask": diffServIpAceDestPortBitmask,
       "diffServIpAceControlCode": diffServIpAceControlCode,
       "diffServIpAceControlCodeBitmask": diffServIpAceControlCodeBitmask,
       "diffServIpAceStatus": diffServIpAceStatus,
       "diffServMacAceTable": diffServMacAceTable,
       "diffServMacAceEntry": diffServMacAceEntry,
       "diffServMacAceIndex": diffServMacAceIndex,
       "diffServMacAceAccess": diffServMacAceAccess,
       "diffServMacAcePktformat": diffServMacAcePktformat,
       "diffServMacAceSourceMacAddr": diffServMacAceSourceMacAddr,
       "diffServMacAceSourceMacAddrBitmask": diffServMacAceSourceMacAddrBitmask,
       "diffServMacAceDestMacAddr": diffServMacAceDestMacAddr,
       "diffServMacAceDestMacAddrBitmask": diffServMacAceDestMacAddrBitmask,
       "diffServMacAceVidOp": diffServMacAceVidOp,
       "diffServMacAceMinVid": diffServMacAceMinVid,
       "diffServMacAceVidBitmask": diffServMacAceVidBitmask,
       "diffServMacAceMaxVid": diffServMacAceMaxVid,
       "diffServMacAceEtherTypeOp": diffServMacAceEtherTypeOp,
       "diffServMacAceEtherTypeBitmask": diffServMacAceEtherTypeBitmask,
       "diffServMacAceMinEtherType": diffServMacAceMinEtherType,
       "diffServMacAceMaxEtherType": diffServMacAceMaxEtherType,
       "diffServMacAceStatus": diffServMacAceStatus,
       "diffServActionTable": diffServActionTable,
       "diffServActionEntry": diffServActionEntry,
       "diffServActionIndex": diffServActionIndex,
       "diffServActionList": diffServActionList,
       "diffServActionPktNewPri": diffServActionPktNewPri,
       "diffServActionPktNewIpPrec": diffServActionPktNewIpPrec,
       "diffServActionPktNewDscp": diffServActionPktNewDscp,
       "diffServActionRedPktNewDscp": diffServActionRedPktNewDscp,
       "diffServActionRedDrop": diffServActionRedDrop,
       "diffServActionStatus": diffServActionStatus,
       "diffServMeterTable": diffServMeterTable,
       "diffServMeterEntry": diffServMeterEntry,
       "diffServMeterIndex": diffServMeterIndex,
       "diffServMeterModel": diffServMeterModel,
       "diffServMeterRate": diffServMeterRate,
       "diffServMeterBurstSize": diffServMeterBurstSize,
       "diffServMeterInterval": diffServMeterInterval,
       "diffServMeterStatus": diffServMeterStatus,
       "securityMgt": securityMgt,
       "portSecurityMgt": portSecurityMgt,
       "portSecPortTable": portSecPortTable,
       "portSecPortEntry": portSecPortEntry,
       "portSecPortIndex": portSecPortIndex,
       "portSecPortStatus": portSecPortStatus,
       "portSecAction": portSecAction,
       "portSecMaxMacCount": portSecMaxMacCount,
       "radiusMgt": radiusMgt,
       "radiusServerGlobalAuthPort": radiusServerGlobalAuthPort,
       "radiusServerGlobalAcctPort": radiusServerGlobalAcctPort,
       "radiusServerGlobalKey": radiusServerGlobalKey,
       "radiusServerGlobalRetransmit": radiusServerGlobalRetransmit,
       "radiusServerGlobalTimeout": radiusServerGlobalTimeout,
       "radiusServerTable": radiusServerTable,
       "radiusServerEntry": radiusServerEntry,
       "radiusServerIndex": radiusServerIndex,
       "radiusServerAddress": radiusServerAddress,
       "radiusServerAuthPortNumber": radiusServerAuthPortNumber,
       "radiusServerAcctPortNumber": radiusServerAcctPortNumber,
       "radiusServerKey": radiusServerKey,
       "radiusServerRetransmit": radiusServerRetransmit,
       "radiusServerTimeout": radiusServerTimeout,
       "radiusServerStatus": radiusServerStatus,
       "tacacsMgt": tacacsMgt,
       "tacacsPlusServerGlobalPortNumber": tacacsPlusServerGlobalPortNumber,
       "tacacsPlusServerGlobalKey": tacacsPlusServerGlobalKey,
       "tacacsPlusServerTable": tacacsPlusServerTable,
       "tacacsPlusServerEntry": tacacsPlusServerEntry,
       "tacacsPlusServerIndex": tacacsPlusServerIndex,
       "tacacsPlusServerAddress": tacacsPlusServerAddress,
       "tacacsPlusServerPortNumber": tacacsPlusServerPortNumber,
       "tacacsPlusServerKey": tacacsPlusServerKey,
       "tacacsPlusServerStatus": tacacsPlusServerStatus,
       "tacacsPlusServerRetransmit": tacacsPlusServerRetransmit,
       "tacacsPlusServerTimeout": tacacsPlusServerTimeout,
       "tacacsPlusServerGlobalRetransmit": tacacsPlusServerGlobalRetransmit,
       "tacacsPlusServerGlobalTimeout": tacacsPlusServerGlobalTimeout,
       "sshMgt": sshMgt,
       "sshServerStatus": sshServerStatus,
       "sshServerMajorVersion": sshServerMajorVersion,
       "sshServerMinorVersion": sshServerMinorVersion,
       "sshTimeout": sshTimeout,
       "sshAuthRetries": sshAuthRetries,
       "sshConnInfoTable": sshConnInfoTable,
       "sshConnInfoEntry": sshConnInfoEntry,
       "sshConnID": sshConnID,
       "sshConnMajorVersion": sshConnMajorVersion,
       "sshConnMinorVersion": sshConnMinorVersion,
       "sshConnStatus": sshConnStatus,
       "sshConnUserName": sshConnUserName,
       "sshDisconnect": sshDisconnect,
       "sshConnEncryptionTypeStr": sshConnEncryptionTypeStr,
       "sshKeySize": sshKeySize,
       "sshRsaHostKey1": sshRsaHostKey1,
       "sshRsaHostKey2": sshRsaHostKey2,
       "sshRsaHostKey3": sshRsaHostKey3,
       "sshRsaHostKey4": sshRsaHostKey4,
       "sshRsaHostKey5": sshRsaHostKey5,
       "sshRsaHostKey6": sshRsaHostKey6,
       "sshRsaHostKey7": sshRsaHostKey7,
       "sshRsaHostKey8": sshRsaHostKey8,
       "sshDsaHostKey1": sshDsaHostKey1,
       "sshDsaHostKey2": sshDsaHostKey2,
       "sshDsaHostKey3": sshDsaHostKey3,
       "sshDsaHostKey4": sshDsaHostKey4,
       "sshDsaHostKey5": sshDsaHostKey5,
       "sshDsaHostKey6": sshDsaHostKey6,
       "sshDsaHostKey7": sshDsaHostKey7,
       "sshDsaHostKey8": sshDsaHostKey8,
       "sshHostKeyGenAction": sshHostKeyGenAction,
       "sshHostKeyGenStatus": sshHostKeyGenStatus,
       "sshHostKeySaveAction": sshHostKeySaveAction,
       "sshHostKeySaveStatus": sshHostKeySaveStatus,
       "sshHostKeyDelAction": sshHostKeyDelAction,
       "aclMgt": aclMgt,
       "aclIpAceTable": aclIpAceTable,
       "aclIpAceEntry": aclIpAceEntry,
       "aclIpAceName": aclIpAceName,
       "aclIpAceIndex": aclIpAceIndex,
       "aclIpAcePrecedence": aclIpAcePrecedence,
       "aclIpAceAction": aclIpAceAction,
       "aclIpAceSourceIpAddr": aclIpAceSourceIpAddr,
       "aclIpAceSourceIpAddrBitmask": aclIpAceSourceIpAddrBitmask,
       "aclIpAceDestIpAddr": aclIpAceDestIpAddr,
       "aclIpAceDestIpAddrBitmask": aclIpAceDestIpAddrBitmask,
       "aclIpAceProtocol": aclIpAceProtocol,
       "aclIpAcePrec": aclIpAcePrec,
       "aclIpAceTos": aclIpAceTos,
       "aclIpAceDscp": aclIpAceDscp,
       "aclIpAceSourcePortOp": aclIpAceSourcePortOp,
       "aclIpAceMinSourcePort": aclIpAceMinSourcePort,
       "aclIpAceMaxSourcePort": aclIpAceMaxSourcePort,
       "aclIpAceDestPortOp": aclIpAceDestPortOp,
       "aclIpAceMinDestPort": aclIpAceMinDestPort,
       "aclIpAceMaxDestPort": aclIpAceMaxDestPort,
       "aclIpAceControlCode": aclIpAceControlCode,
       "aclIpAceControlCodeBitmask": aclIpAceControlCodeBitmask,
       "aclIpAceStatus": aclIpAceStatus,
       "aclMacAceTable": aclMacAceTable,
       "aclMacAceEntry": aclMacAceEntry,
       "aclMacAceName": aclMacAceName,
       "aclMacAceIndex": aclMacAceIndex,
       "aclMacAcePrecedence": aclMacAcePrecedence,
       "aclMacAceAction": aclMacAceAction,
       "aclMacAcePktformat": aclMacAcePktformat,
       "aclMacAceSourceMacAddr": aclMacAceSourceMacAddr,
       "aclMacAceSourceMacAddrBitmask": aclMacAceSourceMacAddrBitmask,
       "aclMacAceDestMacAddr": aclMacAceDestMacAddr,
       "aclMacAceDestMacAddrBitmask": aclMacAceDestMacAddrBitmask,
       "aclMacAceVidOp": aclMacAceVidOp,
       "aclMacAceMinVid": aclMacAceMinVid,
       "aclMacAceMaxVid": aclMacAceMaxVid,
       "aclMacAceEtherTypeOp": aclMacAceEtherTypeOp,
       "aclMacAceMinEtherType": aclMacAceMinEtherType,
       "aclMacAceMaxEtherType": aclMacAceMaxEtherType,
       "aclMacAceStatus": aclMacAceStatus,
       "aclAclGroupTable": aclAclGroupTable,
       "aclAclGroupEntry": aclAclGroupEntry,
       "aclAclGroupIfIndex": aclAclGroupIfIndex,
       "aclAclGroupIngressIpAcl": aclAclGroupIngressIpAcl,
       "aclAclGroupEgressIpAcl": aclAclGroupEgressIpAcl,
       "aclAclGroupIngressMacAcl": aclAclGroupIngressMacAcl,
       "aclAclGroupEgressMacAcl": aclAclGroupEgressMacAcl,
       "ipFilterMgt": ipFilterMgt,
       "ipFilterSnmpTable": ipFilterSnmpTable,
       "ipFilterSnmpEntry": ipFilterSnmpEntry,
       "ipFilterSnmpStartAddress": ipFilterSnmpStartAddress,
       "ipFilterSnmpEndAddress": ipFilterSnmpEndAddress,
       "ipFilterSnmpStatus": ipFilterSnmpStatus,
       "ipFilterHTTPTable": ipFilterHTTPTable,
       "ipFilterHTTPEntry": ipFilterHTTPEntry,
       "ipFilterHTTPStartAddress": ipFilterHTTPStartAddress,
       "ipFilterHTTPEndAddress": ipFilterHTTPEndAddress,
       "ipFilterHTTPStatus": ipFilterHTTPStatus,
       "ipFilterTelnetTable": ipFilterTelnetTable,
       "ipFilterTelnetEntry": ipFilterTelnetEntry,
       "ipFilterTelnetStartAddress": ipFilterTelnetStartAddress,
       "ipFilterTelnetEndAddress": ipFilterTelnetEndAddress,
       "ipFilterTelnetStatus": ipFilterTelnetStatus,
       "sysLogMgt": sysLogMgt,
       "sysLogStatus": sysLogStatus,
       "sysLogHistoryFlashLevel": sysLogHistoryFlashLevel,
       "sysLogHistoryRamLevel": sysLogHistoryRamLevel,
       "remoteLogMgt": remoteLogMgt,
       "remoteLogStatus": remoteLogStatus,
       "remoteLogLevel": remoteLogLevel,
       "remoteLogFacilityType": remoteLogFacilityType,
       "remoteLogServerTable": remoteLogServerTable,
       "remoteLogServerEntry": remoteLogServerEntry,
       "remoteLogServerIp": remoteLogServerIp,
       "remoteLogServerStatus": remoteLogServerStatus,
       "smtpMgt": smtpMgt,
       "smtpStatus": smtpStatus,
       "smtpSeverityLevel": smtpSeverityLevel,
       "smtpSourceEMail": smtpSourceEMail,
       "smtpServerIpTable": smtpServerIpTable,
       "smtpServerIpEntry": smtpServerIpEntry,
       "smtpServerIp": smtpServerIp,
       "smtpServerIpStatus": smtpServerIpStatus,
       "smtpDestEMailTable": smtpDestEMailTable,
       "smtpDestEMailEntry": smtpDestEMailEntry,
       "smtpDestEMail": smtpDestEMail,
       "smtpDestEMailStatus": smtpDestEMailStatus,
       "lineMgt": lineMgt,
       "consoleMgt": consoleMgt,
       "consoleDataBits": consoleDataBits,
       "consoleParity": consoleParity,
       "consoleStopBits": consoleStopBits,
       "consoleExecTimeout": consoleExecTimeout,
       "consolePasswordThreshold": consolePasswordThreshold,
       "consoleSilentTime": consoleSilentTime,
       "consoleAdminBaudRate": consoleAdminBaudRate,
       "consoleOperBaudRate": consoleOperBaudRate,
       "consoleLoginResponseTimeout": consoleLoginResponseTimeout,
       "telnetMgt": telnetMgt,
       "telnetExecTimeout": telnetExecTimeout,
       "telnetPasswordThreshold": telnetPasswordThreshold,
       "telnetLoginResponseTimeout": telnetLoginResponseTimeout,
       "sysTimeMgt": sysTimeMgt,
       "sntpMgt": sntpMgt,
       "sntpStatus": sntpStatus,
       "sntpServiceMode": sntpServiceMode,
       "sntpPollInterval": sntpPollInterval,
       "sntpServerTable": sntpServerTable,
       "sntpServerEntry": sntpServerEntry,
       "sntpServerIndex": sntpServerIndex,
       "sntpServerIpAddress": sntpServerIpAddress,
       "sysCurrentTime": sysCurrentTime,
       "sysTimeZone": sysTimeZone,
       "sysTimeZoneName": sysTimeZoneName,
       "ntpMgt": ntpMgt,
       "ntpStatus": ntpStatus,
       "ntpServiceMode": ntpServiceMode,
       "ntpPollInterval": ntpPollInterval,
       "ntpAuthenticateStatus": ntpAuthenticateStatus,
       "ntpServerTable": ntpServerTable,
       "ntpServerEntry": ntpServerEntry,
       "ntpServerIpAddress": ntpServerIpAddress,
       "ntpServerVersion": ntpServerVersion,
       "ntpServerKeyId": ntpServerKeyId,
       "ntpServerStatus": ntpServerStatus,
       "ntpAuthKeyTable": ntpAuthKeyTable,
       "ntpAuthKeyEntry": ntpAuthKeyEntry,
       "ntpAuthKeyId": ntpAuthKeyId,
       "ntpAuthKeyWord": ntpAuthKeyWord,
       "ntpAuthKeyStatus": ntpAuthKeyStatus,
       "fileMgt": fileMgt,
       "fileCopyMgt": fileCopyMgt,
       "fileCopySrcOperType": fileCopySrcOperType,
       "fileCopySrcFileName": fileCopySrcFileName,
       "fileCopyDestOperType": fileCopyDestOperType,
       "fileCopyDestFileName": fileCopyDestFileName,
       "fileCopyFileType": fileCopyFileType,
       "fileCopyTftpServer": fileCopyTftpServer,
       "fileCopyUnitId": fileCopyUnitId,
       "fileCopyAction": fileCopyAction,
       "fileCopyStatus": fileCopyStatus,
       "fileCopyTftpErrMsg": fileCopyTftpErrMsg,
       "fileInfoMgt": fileInfoMgt,
       "fileInfoTable": fileInfoTable,
       "fileInfoEntry": fileInfoEntry,
       "fileInfoUnitID": fileInfoUnitID,
       "fileInfoFileName": fileInfoFileName,
       "fileInfoFileType": fileInfoFileType,
       "fileInfoIsStartUp": fileInfoIsStartUp,
       "fileInfoFileSize": fileInfoFileSize,
       "fileInfoCreationTime": fileInfoCreationTime,
       "fileInfoDelete": fileInfoDelete,
       "dnsMgt": dnsMgt,
       "dnsDomainLookup": dnsDomainLookup,
       "dnsDomainName": dnsDomainName,
       "dnsHostTable": dnsHostTable,
       "dnsHostEntry": dnsHostEntry,
       "dnsHostName": dnsHostName,
       "dnsHostIndex": dnsHostIndex,
       "dnsHostIp": dnsHostIp,
       "dnsAliasTable": dnsAliasTable,
       "dnsAliasEntry": dnsAliasEntry,
       "dnsAliasName": dnsAliasName,
       "dnsAliasAlias": dnsAliasAlias,
       "dnsDomainListTable": dnsDomainListTable,
       "dnsDomainListEntry": dnsDomainListEntry,
       "dnsDomainListName": dnsDomainListName,
       "dnsDomainListStatus": dnsDomainListStatus,
       "dnsNameServerTable": dnsNameServerTable,
       "dnsNameServerEntry": dnsNameServerEntry,
       "dnsNameServerIndex": dnsNameServerIndex,
       "dnsNameServerIp": dnsNameServerIp,
       "dnsCacheTable": dnsCacheTable,
       "dnsCacheEntry": dnsCacheEntry,
       "dnsCacheIndex": dnsCacheIndex,
       "dnsCacheFlag": dnsCacheFlag,
       "dnsCacheType": dnsCacheType,
       "dnsCacheIp": dnsCacheIp,
       "dnsCacheTtl": dnsCacheTtl,
       "dnsCacheDomain": dnsCacheDomain,
       "mvrMgt": mvrMgt,
       "mvrStatus": mvrStatus,
       "mvrVlanId": mvrVlanId,
       "mvrMaxGroups": mvrMaxGroups,
       "mvrCurrentGroups": mvrCurrentGroups,
       "mvrGroupsCtl": mvrGroupsCtl,
       "mvrGroupsCtlId": mvrGroupsCtlId,
       "mvrGroupsCtlCount": mvrGroupsCtlCount,
       "mvrGroupsCtlAction": mvrGroupsCtlAction,
       "mvrGroupTable": mvrGroupTable,
       "mvrGroupEntry": mvrGroupEntry,
       "mvrGroupId": mvrGroupId,
       "mvrGroutActive": mvrGroutActive,
       "mvrGroupStatus": mvrGroupStatus,
       "mvrGroupStaticTable": mvrGroupStaticTable,
       "mvrGroupStaticEntry": mvrGroupStaticEntry,
       "mvrGroupStaticAddress": mvrGroupStaticAddress,
       "mvrGroupStaticPorts": mvrGroupStaticPorts,
       "mvrGroupStaticStatus": mvrGroupStaticStatus,
       "mvrGroupCurrentTable": mvrGroupCurrentTable,
       "mvrGroupCurrentEntry": mvrGroupCurrentEntry,
       "mvrGroupCurrentAddress": mvrGroupCurrentAddress,
       "mvrGroupCurrentPorts": mvrGroupCurrentPorts,
       "mvrPortTable": mvrPortTable,
       "mvrPortEntry": mvrPortEntry,
       "mvrIfIndex": mvrIfIndex,
       "mvrPortType": mvrPortType,
       "mvrPortImmediateLeave": mvrPortImmediateLeave,
       "mvrPortActive": mvrPortActive,
       "mvrRunningStatus": mvrRunningStatus,
       "dhcpSnoopMgt": dhcpSnoopMgt,
       "dhcpSnoopGlobal": dhcpSnoopGlobal,
       "dhcpSnoopEnable": dhcpSnoopEnable,
       "dhcpSnoopVerifyMacAddressEnable": dhcpSnoopVerifyMacAddressEnable,
       "dhcpSnoopInformationOptionEnable": dhcpSnoopInformationOptionEnable,
       "dhcpSnoopInformationOptionPolicy": dhcpSnoopInformationOptionPolicy,
       "dhcpSnoopVlan": dhcpSnoopVlan,
       "dhcpSnoopVlanConfigTable": dhcpSnoopVlanConfigTable,
       "dhcpSnoopVlanConfigEntry": dhcpSnoopVlanConfigEntry,
       "dhcpSnoopVlanIndex": dhcpSnoopVlanIndex,
       "dhcpSnoopVlanEnable": dhcpSnoopVlanEnable,
       "dhcpSnoopInterface": dhcpSnoopInterface,
       "dhcpSnoopPortConfigTable": dhcpSnoopPortConfigTable,
       "dhcpSnoopPortConfigEntry": dhcpSnoopPortConfigEntry,
       "dhcpSnoopPortIfIndex": dhcpSnoopPortIfIndex,
       "dhcpSnoopPortTrustEnable": dhcpSnoopPortTrustEnable,
       "dhcpSnoopBindings": dhcpSnoopBindings,
       "dhcpSnoopBindingsTable": dhcpSnoopBindingsTable,
       "dhcpSnoopBindingsEntry": dhcpSnoopBindingsEntry,
       "dhcpSnoopBindingsVlanIndex": dhcpSnoopBindingsVlanIndex,
       "dhcpSnoopBindingsMacAddress": dhcpSnoopBindingsMacAddress,
       "dhcpSnoopBindingsAddrType": dhcpSnoopBindingsAddrType,
       "dhcpSnoopBindingsEntryType": dhcpSnoopBindingsEntryType,
       "dhcpSnoopBindingsIpAddress": dhcpSnoopBindingsIpAddress,
       "dhcpSnoopBindingsPortIfIndex": dhcpSnoopBindingsPortIfIndex,
       "dhcpSnoopBindingsLeaseTime": dhcpSnoopBindingsLeaseTime,
       "dhcpSnoopStatistics": dhcpSnoopStatistics,
       "dhcpSnoopTotalForwardedPkts": dhcpSnoopTotalForwardedPkts,
       "dhcpSnoopUntrustedPortDroppedPkts": dhcpSnoopUntrustedPortDroppedPkts,
       "clusterMgt": clusterMgt,
       "clusterEnable": clusterEnable,
       "clusterCommanderEnable": clusterCommanderEnable,
       "clusterIpPool": clusterIpPool,
       "clusterClearCandidateTable": clusterClearCandidateTable,
       "clusterRole": clusterRole,
       "clusterMemberCount": clusterMemberCount,
       "clusterCandidateCount": clusterCandidateCount,
       "clusterCandidateTable": clusterCandidateTable,
       "clusterCandidateEntry": clusterCandidateEntry,
       "clusterCandidateMacAddr": clusterCandidateMacAddr,
       "clusterCandidateDesc": clusterCandidateDesc,
       "clusterCandidateRole": clusterCandidateRole,
       "clusterMemberTable": clusterMemberTable,
       "clusterMemberEntry": clusterMemberEntry,
       "clusterMemberId": clusterMemberId,
       "clusterMemberMacAddr": clusterMemberMacAddr,
       "clusterMemberDesc": clusterMemberDesc,
       "clusterMemberActive": clusterMemberActive,
       "clusterMemberAddCtl": clusterMemberAddCtl,
       "clusterMemberAddCtlMacAddr": clusterMemberAddCtlMacAddr,
       "clusterMemberAddCtlId": clusterMemberAddCtlId,
       "clusterMemberAddCtlAction": clusterMemberAddCtlAction,
       "clusterMemberRemoveCtl": clusterMemberRemoveCtl,
       "clusterMemberRemoveCtlId": clusterMemberRemoveCtlId,
       "clusterMemberRemoveCtlAction": clusterMemberRemoveCtlAction,
       "ipSrcGuardMgt": ipSrcGuardMgt,
       "ipSrcGuardConfigTable": ipSrcGuardConfigTable,
       "ipSrcGuardConfigEntry": ipSrcGuardConfigEntry,
       "ipSrcGuardPortIfIndex": ipSrcGuardPortIfIndex,
       "ipSrcGuardMode": ipSrcGuardMode,
       "ipSrcGuardAddrTable": ipSrcGuardAddrTable,
       "ipSrcGuardAddrEntry": ipSrcGuardAddrEntry,
       "ipSrcGuardBindingsVlanIndex": ipSrcGuardBindingsVlanIndex,
       "ipSrcGuardBindingsMacAddress": ipSrcGuardBindingsMacAddress,
       "ipSrcGuardBindingsAddrType": ipSrcGuardBindingsAddrType,
       "ipSrcGuardBindingsEntryType": ipSrcGuardBindingsEntryType,
       "ipSrcGuardBindingsIpAddress": ipSrcGuardBindingsIpAddress,
       "ipSrcGuardBindingsPortIfIndex": ipSrcGuardBindingsPortIfIndex,
       "ipSrcGuardBindingsLeaseTime": ipSrcGuardBindingsLeaseTime,
       "ipSrcGuardBindingsStatus": ipSrcGuardBindingsStatus,
       "es3526XA_ES3510Notifications": es3526XA_ES3510Notifications,
       "es3526XA_ES3510Traps": es3526XA_ES3510Traps,
       "es3526XA_ES3510TrapsPrefix": es3526XA_ES3510TrapsPrefix,
       "swPowerStatusChangeTrap": swPowerStatusChangeTrap,
       "swIpFilterRejectTrap": swIpFilterRejectTrap,
       "swSmtpConnFailureTrap": swSmtpConnFailureTrap,
       "swAuthenticationFailure": swAuthenticationFailure,
       "swAuthenticationSuccess": swAuthenticationSuccess,
       "swVlanChangeStatus": swVlanChangeStatus,
       "es3526XA_ES3510Conformance": es3526XA_ES3510Conformance}
)
