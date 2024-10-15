# SNMP MIB module (GENERAL-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GENERAL-MGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:48:28 2024
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(dXS_3600_32S,) = mibBuilder.importSymbols(
    "SW3600PRIMGMT-MIB",
    "dXS-3600-32S")


# MODULE-IDENTITY

swGeneralMgmtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 127, 1, 20)
)


# Types definitions



class UnitList(OctetString):
    """Custom type UnitList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )




# TEXTUAL-CONVENTIONS



class Ipv6Address(OctetString, TextualConvention):
    status = "current"
    displayHint = "2x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )



# MIB Managed Objects in the order of their OIDs

_SwGenMgmtNotifications_ObjectIdentity = ObjectIdentity
swGenMgmtNotifications = _SwGenMgmtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 127, 1, 20, 0)
)
_SwGenMgmtMIBObjects_ObjectIdentity = ObjectIdentity
swGenMgmtMIBObjects = _SwGenMgmtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 127, 1, 20, 1)
)
_SwGenMgmtGroup_ObjectIdentity = ObjectIdentity
swGenMgmtGroup = _SwGenMgmtGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 127, 1, 20, 1, 1)
)
_SwGenFileSystemMgmt_ObjectIdentity = ObjectIdentity
swGenFileSystemMgmt = _SwGenFileSystemMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 127, 1, 20, 1, 1, 1)
)
_SwGenFileSystemMgmtTable_Object = MibTable
swGenFileSystemMgmtTable = _SwGenFileSystemMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 127, 1, 20, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    swGenFileSystemMgmtTable.setStatus("current")
_SwGenFileSystemMgmtEntry_Object = MibTableRow
swGenFileSystemMgmtEntry = _SwGenFileSystemMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 127, 1, 20, 1, 1, 1, 1, 1)
)
swGenFileSystemMgmtEntry.setIndexNames(
    (0, "GENERAL-MGMT-MIB", "swGenFileSystemMgmtIndex"),
)
if mibBuilder.loadTexts:
    swGenFileSystemMgmtEntry.setStatus("current")
_SwGenFileSystemMgmtIndex_Type = Integer32
_SwGenFileSystemMgmtIndex_Object = MibTableColumn
swGenFileSystemMgmtIndex = _SwGenFileSystemMgmtIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 127, 1, 20, 1, 1, 1, 1, 1, 1),
    _SwGenFileSystemMgmtIndex_Type()
)
swGenFileSystemMgmtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swGenFileSystemMgmtIndex.setStatus("current")


class _SwGenFileSystemMgmtDscr_Type(DisplayString):
    """Custom type swGenFileSystemMgmtDscr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwGenFileSystemMgmtDscr_Type.__name__ = "DisplayString"
_SwGenFileSystemMgmtDscr_Object = MibTableColumn
swGenFileSystemMgmtDscr = _SwGenFileSystemMgmtDscr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 127, 1, 20, 1, 1, 1, 1, 1, 2),
    _SwGenFileSystemMgmtDscr_Type()
)
swGenFileSystemMgmtDscr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swGenFileSystemMgmtDscr.setStatus("current")
_SwGenFileSystemMgmtServerAddrType_Type = InetAddressType
_SwGenFileSystemMgmtServerAddrType_Object = MibTableColumn
swGenFileSystemMgmtServerAddrType = _SwGenFileSystemMgmtServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 127, 1, 20, 1, 1, 1, 1, 1, 3),
    _SwGenFileSystemMgmtServerAddrType_Type()
)
swGenFileSystemMgmtServerAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swGenFileSystemMgmtServerAddrType.setStatus("current")
_SwGenFileSystemMgmtServerAddr_Type = InetAddress
_SwGenFileSystemMgmtServerAddr_Object = MibTableColumn
swGenFileSystemMgmtServerAddr = _SwGenFileSystemMgmtServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 127, 1, 20, 1, 1, 1, 1, 1, 4),
    _SwGenFileSystemMgmtServerAddr_Type()
)
swGenFileSystemMgmtServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swGenFileSystemMgmtServerAddr.setStatus("current")


class _SwGenFileSystemMgmtInterfaceName_Type(DisplayString):
    """Custom type swGenFileSystemMgmtInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_SwGenFileSystemMgmtInterfaceName_Type.__name__ = "DisplayString"
_SwGenFileSystemMgmtInterfaceName_Object = MibTableColumn
swGenFileSystemMgmtInterfaceName = _SwGenFileSystemMgmtInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 127, 1, 20, 1, 1, 1, 1, 1, 5),
    _SwGenFileSystemMgmtInterfaceName_Type()
)
swGenFileSystemMgmtInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swGenFileSystemMgmtInterfaceName.setStatus("current")


class _SwGenFileSystemMgmtTranserProtocol_Type(Integer32):
    """Custom type swGenFileSystemMgmtTranserProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 2),
          ("tftp", 1))
    )


_SwGenFileSystemMgmtTranserProtocol_Type.__name__ = "Integer32"
_SwGenFileSystemMgmtTranserProtocol_Object = MibTableColumn
swGenFileSystemMgmtTranserProtocol = _SwGenFileSystemMgmtTranserProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 127, 1, 20, 1, 1, 1, 1, 1, 10),
    _SwGenFileSystemMgmtTranserProtocol_Type()
)
swGenFileSystemMgmtTranserProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swGenFileSystemMgmtTranserProtocol.setStatus("current")
_SwGenFileSystemMgmtUserName_Type = DisplayString
_SwGenFileSystemMgmtUserName_Object = MibTableColumn
swGenFileSystemMgmtUserName = _SwGenFileSystemMgmtUserName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 127, 1, 20, 1, 1, 1, 1, 1, 11),
    _SwGenFileSystemMgmtUserName_Type()
)
swGenFileSystemMgmtUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swGenFileSystemMgmtUserName.setStatus("current")
_SwGenFileSystemMgmtPassword_Type = DisplayString
_SwGenFileSystemMgmtPassword_Object = MibTableColumn
swGenFileSystemMgmtPassword = _SwGenFileSystemMgmtPassword_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 127, 1, 20, 1, 1, 1, 1, 1, 12),
    _SwGenFileSystemMgmtPassword_Type()
)
swGenFileSystemMgmtPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swGenFileSystemMgmtPassword.setStatus("current")


class _SwGenFileSystemMgmtServerFileName_Type(DisplayString):
    """Custom type swGenFileSystemMgmtServerFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwGenFileSystemMgmtServerFileName_Type.__name__ = "DisplayString"
_SwGenFileSystemMgmtServerFileName_Object = MibTableColumn
swGenFileSystemMgmtServerFileName = _SwGenFileSystemMgmtServerFileName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 127, 1, 20, 1, 1, 1, 1, 1, 20),
    _SwGenFileSystemMgmtServerFileName_Type()
)
swGenFileSystemMgmtServerFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swGenFileSystemMgmtServerFileName.setStatus("current")


class _SwGenFileSystemMgmtDeviceFileName_Type(DisplayString):
    """Custom type swGenFileSystemMgmtDeviceFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwGenFileSystemMgmtDeviceFileName_Type.__name__ = "DisplayString"
_SwGenFileSystemMgmtDeviceFileName_Object = MibTableColumn
swGenFileSystemMgmtDeviceFileName = _SwGenFileSystemMgmtDeviceFileName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 127, 1, 20, 1, 1, 1, 1, 1, 21),
    _SwGenFileSystemMgmtDeviceFileName_Type()
)
swGenFileSystemMgmtDeviceFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swGenFileSystemMgmtDeviceFileName.setStatus("current")


class _SwGenFileSystemMgmtLoadType_Type(Integer32):
    """Custom type swGenFileSystemMgmtLoadType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("download", 3),
          ("other", 1),
          ("upload", 2))
    )


_SwGenFileSystemMgmtLoadType_Type.__name__ = "Integer32"
_SwGenFileSystemMgmtLoadType_Object = MibTableColumn
swGenFileSystemMgmtLoadType = _SwGenFileSystemMgmtLoadType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 127, 1, 20, 1, 1, 1, 1, 1, 30),
    _SwGenFileSystemMgmtLoadType_Type()
)
swGenFileSystemMgmtLoadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swGenFileSystemMgmtLoadType.setStatus("current")


class _SwGenFileSystemMgmtCtrl_Type(Integer32):
    """Custom type swGenFileSystemMgmtCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 2),
          ("other", 1),
          ("start", 3))
    )


_SwGenFileSystemMgmtCtrl_Type.__name__ = "Integer32"
_SwGenFileSystemMgmtCtrl_Object = MibTableColumn
swGenFileSystemMgmtCtrl = _SwGenFileSystemMgmtCtrl_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 127, 1, 20, 1, 1, 1, 1, 1, 100),
    _SwGenFileSystemMgmtCtrl_Type()
)
swGenFileSystemMgmtCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swGenFileSystemMgmtCtrl.setStatus("current")
_SwGenFileSystemBootupFileMgmtTable_Object = MibTable
swGenFileSystemBootupFileMgmtTable = _SwGenFileSystemBootupFileMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 127, 1, 20, 1, 1, 5)
)
if mibBuilder.loadTexts:
    swGenFileSystemBootupFileMgmtTable.setStatus("current")
_SwGenFileSystemBootupFileMgmtEntry_Object = MibTableRow
swGenFileSystemBootupFileMgmtEntry = _SwGenFileSystemBootupFileMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 127, 1, 20, 1, 1, 5, 1)
)
swGenFileSystemBootupFileMgmtEntry.setIndexNames(
    (0, "GENERAL-MGMT-MIB", "swGenMgmtUnitID"),
)
if mibBuilder.loadTexts:
    swGenFileSystemBootupFileMgmtEntry.setStatus("current")
_SwGenMgmtUnitID_Type = Integer32
_SwGenMgmtUnitID_Object = MibTableColumn
swGenMgmtUnitID = _SwGenMgmtUnitID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 127, 1, 20, 1, 1, 5, 1, 1),
    _SwGenMgmtUnitID_Type()
)
swGenMgmtUnitID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swGenMgmtUnitID.setStatus("current")


class _SwGenFileSystemBootImage_Type(DisplayString):
    """Custom type swGenFileSystemBootImage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwGenFileSystemBootImage_Type.__name__ = "DisplayString"
_SwGenFileSystemBootImage_Object = MibTableColumn
swGenFileSystemBootImage = _SwGenFileSystemBootImage_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 127, 1, 20, 1, 1, 5, 1, 3),
    _SwGenFileSystemBootImage_Type()
)
swGenFileSystemBootImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swGenFileSystemBootImage.setStatus("current")


class _SwGenFileSystemBootConfig_Type(DisplayString):
    """Custom type swGenFileSystemBootConfig based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwGenFileSystemBootConfig_Type.__name__ = "DisplayString"
_SwGenFileSystemBootConfig_Object = MibTableColumn
swGenFileSystemBootConfig = _SwGenFileSystemBootConfig_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 127, 1, 20, 1, 1, 5, 1, 5),
    _SwGenFileSystemBootConfig_Type()
)
swGenFileSystemBootConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swGenFileSystemBootConfig.setStatus("current")
_SwGenFileSystemActiveConfigIncrement_Type = TruthValue
_SwGenFileSystemActiveConfigIncrement_Object = MibTableColumn
swGenFileSystemActiveConfigIncrement = _SwGenFileSystemActiveConfigIncrement_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 127, 1, 20, 1, 1, 5, 1, 10),
    _SwGenFileSystemActiveConfigIncrement_Type()
)
swGenFileSystemActiveConfigIncrement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swGenFileSystemActiveConfigIncrement.setStatus("current")


class _SwGenFileSystemActiveConfig_Type(DisplayString):
    """Custom type swGenFileSystemActiveConfig based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwGenFileSystemActiveConfig_Type.__name__ = "DisplayString"
_SwGenFileSystemActiveConfig_Object = MibTableColumn
swGenFileSystemActiveConfig = _SwGenFileSystemActiveConfig_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 127, 1, 20, 1, 1, 5, 1, 11),
    _SwGenFileSystemActiveConfig_Type()
)
swGenFileSystemActiveConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swGenFileSystemActiveConfig.setStatus("current")
_SwGenExpansionModuleMgmtTable_Object = MibTable
swGenExpansionModuleMgmtTable = _SwGenExpansionModuleMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 127, 1, 20, 1, 1, 8)
)
if mibBuilder.loadTexts:
    swGenExpansionModuleMgmtTable.setStatus("current")
_SwGenExpansionModuleMgmtEntry_Object = MibTableRow
swGenExpansionModuleMgmtEntry = _SwGenExpansionModuleMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 127, 1, 20, 1, 1, 8, 1)
)
swGenExpansionModuleMgmtEntry.setIndexNames(
    (0, "GENERAL-MGMT-MIB", "swGenMgmtUnitID"),
    (0, "GENERAL-MGMT-MIB", "swGenExpansionModuleMgmtSlotID"),
)
if mibBuilder.loadTexts:
    swGenExpansionModuleMgmtEntry.setStatus("current")
_SwGenExpansionModuleMgmtSlotID_Type = Integer32
_SwGenExpansionModuleMgmtSlotID_Object = MibTableColumn
swGenExpansionModuleMgmtSlotID = _SwGenExpansionModuleMgmtSlotID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 127, 1, 20, 1, 1, 8, 1, 2),
    _SwGenExpansionModuleMgmtSlotID_Type()
)
swGenExpansionModuleMgmtSlotID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swGenExpansionModuleMgmtSlotID.setStatus("current")


class _SwGenExpansionModuleMgmtBootup_Type(DisplayString):
    """Custom type swGenExpansionModuleMgmtBootup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwGenExpansionModuleMgmtBootup_Type.__name__ = "DisplayString"
_SwGenExpansionModuleMgmtBootup_Object = MibTableColumn
swGenExpansionModuleMgmtBootup = _SwGenExpansionModuleMgmtBootup_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 127, 1, 20, 1, 1, 8, 1, 3),
    _SwGenExpansionModuleMgmtBootup_Type()
)
swGenExpansionModuleMgmtBootup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swGenExpansionModuleMgmtBootup.setStatus("current")


class _SwGenExpansionModuleMgmtCurrent_Type(DisplayString):
    """Custom type swGenExpansionModuleMgmtCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwGenExpansionModuleMgmtCurrent_Type.__name__ = "DisplayString"
_SwGenExpansionModuleMgmtCurrent_Object = MibTableColumn
swGenExpansionModuleMgmtCurrent = _SwGenExpansionModuleMgmtCurrent_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 127, 1, 20, 1, 1, 8, 1, 4),
    _SwGenExpansionModuleMgmtCurrent_Type()
)
swGenExpansionModuleMgmtCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swGenExpansionModuleMgmtCurrent.setStatus("current")


class _SwGenExpansionModuleBootupPortModeInfo_Type(OctetString):
    """Custom type swGenExpansionModuleBootupPortModeInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_SwGenExpansionModuleBootupPortModeInfo_Type.__name__ = "OctetString"
_SwGenExpansionModuleBootupPortModeInfo_Object = MibTableColumn
swGenExpansionModuleBootupPortModeInfo = _SwGenExpansionModuleBootupPortModeInfo_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 127, 1, 20, 1, 1, 8, 1, 5),
    _SwGenExpansionModuleBootupPortModeInfo_Type()
)
swGenExpansionModuleBootupPortModeInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swGenExpansionModuleBootupPortModeInfo.setStatus("current")


class _SwGenExpansionModuleCurrentPortModeMGT_Type(OctetString):
    """Custom type swGenExpansionModuleCurrentPortModeMGT based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_SwGenExpansionModuleCurrentPortModeMGT_Type.__name__ = "OctetString"
_SwGenExpansionModuleCurrentPortModeMGT_Object = MibTableColumn
swGenExpansionModuleCurrentPortModeMGT = _SwGenExpansionModuleCurrentPortModeMGT_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 127, 1, 20, 1, 1, 8, 1, 6),
    _SwGenExpansionModuleCurrentPortModeMGT_Type()
)
swGenExpansionModuleCurrentPortModeMGT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swGenExpansionModuleCurrentPortModeMGT.setStatus("current")


class _SwGenExpansionModuleEquippedModulePortMode_Type(OctetString):
    """Custom type swGenExpansionModuleEquippedModulePortMode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_SwGenExpansionModuleEquippedModulePortMode_Type.__name__ = "OctetString"
_SwGenExpansionModuleEquippedModulePortMode_Object = MibTableColumn
swGenExpansionModuleEquippedModulePortMode = _SwGenExpansionModuleEquippedModulePortMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 127, 1, 20, 1, 1, 8, 1, 7),
    _SwGenExpansionModuleEquippedModulePortMode_Type()
)
swGenExpansionModuleEquippedModulePortMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swGenExpansionModuleEquippedModulePortMode.setStatus("current")


class _SwGenMgmtReboot_Type(Integer32):
    """Custom type swGenMgmtReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("start", 2))
    )


_SwGenMgmtReboot_Type.__name__ = "Integer32"
_SwGenMgmtReboot_Object = MibScalar
swGenMgmtReboot = _SwGenMgmtReboot_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 127, 1, 20, 1, 1, 10),
    _SwGenMgmtReboot_Type()
)
swGenMgmtReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swGenMgmtReboot.setStatus("current")


class _SwGenMgmtSaveConfigFileName_Type(DisplayString):
    """Custom type swGenMgmtSaveConfigFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwGenMgmtSaveConfigFileName_Type.__name__ = "DisplayString"
_SwGenMgmtSaveConfigFileName_Object = MibScalar
swGenMgmtSaveConfigFileName = _SwGenMgmtSaveConfigFileName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 127, 1, 20, 1, 1, 11),
    _SwGenMgmtSaveConfigFileName_Type()
)
swGenMgmtSaveConfigFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swGenMgmtSaveConfigFileName.setStatus("current")


class _SwGenMgmtSave_Type(Integer32):
    """Custom type swGenMgmtSave based on Integer32"""
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
        *(("all", 4),
          ("configuration", 2),
          ("log", 3),
          ("other", 1))
    )


_SwGenMgmtSave_Type.__name__ = "Integer32"
_SwGenMgmtSave_Object = MibScalar
swGenMgmtSave = _SwGenMgmtSave_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 127, 1, 20, 1, 1, 12),
    _SwGenMgmtSave_Type()
)
swGenMgmtSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swGenMgmtSave.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GENERAL-MGMT-MIB",
    **{"Ipv6Address": Ipv6Address,
       "UnitList": UnitList,
       "swGeneralMgmtMIB": swGeneralMgmtMIB,
       "swGenMgmtNotifications": swGenMgmtNotifications,
       "swGenMgmtMIBObjects": swGenMgmtMIBObjects,
       "swGenMgmtGroup": swGenMgmtGroup,
       "swGenFileSystemMgmt": swGenFileSystemMgmt,
       "swGenFileSystemMgmtTable": swGenFileSystemMgmtTable,
       "swGenFileSystemMgmtEntry": swGenFileSystemMgmtEntry,
       "swGenFileSystemMgmtIndex": swGenFileSystemMgmtIndex,
       "swGenFileSystemMgmtDscr": swGenFileSystemMgmtDscr,
       "swGenFileSystemMgmtServerAddrType": swGenFileSystemMgmtServerAddrType,
       "swGenFileSystemMgmtServerAddr": swGenFileSystemMgmtServerAddr,
       "swGenFileSystemMgmtInterfaceName": swGenFileSystemMgmtInterfaceName,
       "swGenFileSystemMgmtTranserProtocol": swGenFileSystemMgmtTranserProtocol,
       "swGenFileSystemMgmtUserName": swGenFileSystemMgmtUserName,
       "swGenFileSystemMgmtPassword": swGenFileSystemMgmtPassword,
       "swGenFileSystemMgmtServerFileName": swGenFileSystemMgmtServerFileName,
       "swGenFileSystemMgmtDeviceFileName": swGenFileSystemMgmtDeviceFileName,
       "swGenFileSystemMgmtLoadType": swGenFileSystemMgmtLoadType,
       "swGenFileSystemMgmtCtrl": swGenFileSystemMgmtCtrl,
       "swGenFileSystemBootupFileMgmtTable": swGenFileSystemBootupFileMgmtTable,
       "swGenFileSystemBootupFileMgmtEntry": swGenFileSystemBootupFileMgmtEntry,
       "swGenMgmtUnitID": swGenMgmtUnitID,
       "swGenFileSystemBootImage": swGenFileSystemBootImage,
       "swGenFileSystemBootConfig": swGenFileSystemBootConfig,
       "swGenFileSystemActiveConfigIncrement": swGenFileSystemActiveConfigIncrement,
       "swGenFileSystemActiveConfig": swGenFileSystemActiveConfig,
       "swGenExpansionModuleMgmtTable": swGenExpansionModuleMgmtTable,
       "swGenExpansionModuleMgmtEntry": swGenExpansionModuleMgmtEntry,
       "swGenExpansionModuleMgmtSlotID": swGenExpansionModuleMgmtSlotID,
       "swGenExpansionModuleMgmtBootup": swGenExpansionModuleMgmtBootup,
       "swGenExpansionModuleMgmtCurrent": swGenExpansionModuleMgmtCurrent,
       "swGenExpansionModuleBootupPortModeInfo": swGenExpansionModuleBootupPortModeInfo,
       "swGenExpansionModuleCurrentPortModeMGT": swGenExpansionModuleCurrentPortModeMGT,
       "swGenExpansionModuleEquippedModulePortMode": swGenExpansionModuleEquippedModulePortMode,
       "swGenMgmtReboot": swGenMgmtReboot,
       "swGenMgmtSaveConfigFileName": swGenMgmtSaveConfigFileName,
       "swGenMgmtSave": swGenMgmtSave}
)
