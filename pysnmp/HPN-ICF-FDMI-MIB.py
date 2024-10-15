# SNMP MIB module (HPN-ICF-FDMI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-FDMI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:00:24 2024
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

(FcNameIdOrZero,
 fcmInstanceIndex) = mibBuilder.importSymbols(
    "FC-MGMT-MIB",
    "FcNameIdOrZero",
    "fcmInstanceIndex")

(hpnicfSan,) = mibBuilder.importSymbols(
    "HPN-ICF-VSAN-MIB",
    "hpnicfSan")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(T11FabricIndex,) = mibBuilder.importSymbols(
    "T11-TC-MIB",
    "T11FabricIndex")


# MODULE-IDENTITY

hpnicfFdmi = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 7)
)
hpnicfFdmi.setRevisions(
        ("2012-06-18 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfFdmiObjects_ObjectIdentity = ObjectIdentity
hpnicfFdmiObjects = _HpnicfFdmiObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 7, 1)
)
_HpnicfFdmiInfo_ObjectIdentity = ObjectIdentity
hpnicfFdmiInfo = _HpnicfFdmiInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 7, 1, 1)
)
_HpnicfFdmiHbaInfoTable_Object = MibTable
hpnicfFdmiHbaInfoTable = _HpnicfFdmiHbaInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 7, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfFdmiHbaInfoTable.setStatus("current")
_HpnicfFdmiHbaInfoEntry_Object = MibTableRow
hpnicfFdmiHbaInfoEntry = _HpnicfFdmiHbaInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 7, 1, 1, 1, 1)
)
hpnicfFdmiHbaInfoEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "HPN-ICF-FDMI-MIB", "hpnicfFdmiHbaInfoFabricIndex"),
    (0, "HPN-ICF-FDMI-MIB", "hpnicfFdmiHbaInfoId"),
)
if mibBuilder.loadTexts:
    hpnicfFdmiHbaInfoEntry.setStatus("current")
_HpnicfFdmiHbaInfoFabricIndex_Type = T11FabricIndex
_HpnicfFdmiHbaInfoFabricIndex_Object = MibTableColumn
hpnicfFdmiHbaInfoFabricIndex = _HpnicfFdmiHbaInfoFabricIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 7, 1, 1, 1, 1, 1),
    _HpnicfFdmiHbaInfoFabricIndex_Type()
)
hpnicfFdmiHbaInfoFabricIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfFdmiHbaInfoFabricIndex.setStatus("current")
_HpnicfFdmiHbaInfoId_Type = FcNameIdOrZero
_HpnicfFdmiHbaInfoId_Object = MibTableColumn
hpnicfFdmiHbaInfoId = _HpnicfFdmiHbaInfoId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 7, 1, 1, 1, 1, 2),
    _HpnicfFdmiHbaInfoId_Type()
)
hpnicfFdmiHbaInfoId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfFdmiHbaInfoId.setStatus("current")
_HpnicfFdmiHbaInfoNodeName_Type = FcNameIdOrZero
_HpnicfFdmiHbaInfoNodeName_Object = MibTableColumn
hpnicfFdmiHbaInfoNodeName = _HpnicfFdmiHbaInfoNodeName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 7, 1, 1, 1, 1, 3),
    _HpnicfFdmiHbaInfoNodeName_Type()
)
hpnicfFdmiHbaInfoNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFdmiHbaInfoNodeName.setStatus("current")
_HpnicfFdmiHbaInfoMfg_Type = SnmpAdminString
_HpnicfFdmiHbaInfoMfg_Object = MibTableColumn
hpnicfFdmiHbaInfoMfg = _HpnicfFdmiHbaInfoMfg_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 7, 1, 1, 1, 1, 4),
    _HpnicfFdmiHbaInfoMfg_Type()
)
hpnicfFdmiHbaInfoMfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFdmiHbaInfoMfg.setStatus("current")
_HpnicfFdmiHbaInfoSn_Type = SnmpAdminString
_HpnicfFdmiHbaInfoSn_Object = MibTableColumn
hpnicfFdmiHbaInfoSn = _HpnicfFdmiHbaInfoSn_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 7, 1, 1, 1, 1, 5),
    _HpnicfFdmiHbaInfoSn_Type()
)
hpnicfFdmiHbaInfoSn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFdmiHbaInfoSn.setStatus("current")
_HpnicfFdmiHbaInfoModel_Type = SnmpAdminString
_HpnicfFdmiHbaInfoModel_Object = MibTableColumn
hpnicfFdmiHbaInfoModel = _HpnicfFdmiHbaInfoModel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 7, 1, 1, 1, 1, 6),
    _HpnicfFdmiHbaInfoModel_Type()
)
hpnicfFdmiHbaInfoModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFdmiHbaInfoModel.setStatus("current")
_HpnicfFdmiHbaInfoModelDescr_Type = SnmpAdminString
_HpnicfFdmiHbaInfoModelDescr_Object = MibTableColumn
hpnicfFdmiHbaInfoModelDescr = _HpnicfFdmiHbaInfoModelDescr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 7, 1, 1, 1, 1, 7),
    _HpnicfFdmiHbaInfoModelDescr_Type()
)
hpnicfFdmiHbaInfoModelDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFdmiHbaInfoModelDescr.setStatus("current")
_HpnicfFdmiHbaInfoHwVer_Type = SnmpAdminString
_HpnicfFdmiHbaInfoHwVer_Object = MibTableColumn
hpnicfFdmiHbaInfoHwVer = _HpnicfFdmiHbaInfoHwVer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 7, 1, 1, 1, 1, 8),
    _HpnicfFdmiHbaInfoHwVer_Type()
)
hpnicfFdmiHbaInfoHwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFdmiHbaInfoHwVer.setStatus("current")
_HpnicfFdmiHbaInfoDriverVer_Type = SnmpAdminString
_HpnicfFdmiHbaInfoDriverVer_Object = MibTableColumn
hpnicfFdmiHbaInfoDriverVer = _HpnicfFdmiHbaInfoDriverVer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 7, 1, 1, 1, 1, 9),
    _HpnicfFdmiHbaInfoDriverVer_Type()
)
hpnicfFdmiHbaInfoDriverVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFdmiHbaInfoDriverVer.setStatus("current")
_HpnicfFdmiHbaInfoOptROMVer_Type = SnmpAdminString
_HpnicfFdmiHbaInfoOptROMVer_Object = MibTableColumn
hpnicfFdmiHbaInfoOptROMVer = _HpnicfFdmiHbaInfoOptROMVer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 7, 1, 1, 1, 1, 10),
    _HpnicfFdmiHbaInfoOptROMVer_Type()
)
hpnicfFdmiHbaInfoOptROMVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFdmiHbaInfoOptROMVer.setStatus("current")
_HpnicfFdmiHbaInfoFwVer_Type = SnmpAdminString
_HpnicfFdmiHbaInfoFwVer_Object = MibTableColumn
hpnicfFdmiHbaInfoFwVer = _HpnicfFdmiHbaInfoFwVer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 7, 1, 1, 1, 1, 11),
    _HpnicfFdmiHbaInfoFwVer_Type()
)
hpnicfFdmiHbaInfoFwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFdmiHbaInfoFwVer.setStatus("current")
_HpnicfFdmiHbaInfoOSInfo_Type = SnmpAdminString
_HpnicfFdmiHbaInfoOSInfo_Object = MibTableColumn
hpnicfFdmiHbaInfoOSInfo = _HpnicfFdmiHbaInfoOSInfo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 7, 1, 1, 1, 1, 12),
    _HpnicfFdmiHbaInfoOSInfo_Type()
)
hpnicfFdmiHbaInfoOSInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFdmiHbaInfoOSInfo.setStatus("current")
_HpnicfFdmiHbaInfoMaxCTPayload_Type = Unsigned32
_HpnicfFdmiHbaInfoMaxCTPayload_Object = MibTableColumn
hpnicfFdmiHbaInfoMaxCTPayload = _HpnicfFdmiHbaInfoMaxCTPayload_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 7, 1, 1, 1, 1, 13),
    _HpnicfFdmiHbaInfoMaxCTPayload_Type()
)
hpnicfFdmiHbaInfoMaxCTPayload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFdmiHbaInfoMaxCTPayload.setStatus("current")
_HpnicfFdmiHbaPortTable_Object = MibTable
hpnicfFdmiHbaPortTable = _HpnicfFdmiHbaPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 7, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfFdmiHbaPortTable.setStatus("current")
_HpnicfFdmiHbaPortEntry_Object = MibTableRow
hpnicfFdmiHbaPortEntry = _HpnicfFdmiHbaPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 7, 1, 1, 2, 1)
)
hpnicfFdmiHbaPortEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "HPN-ICF-FDMI-MIB", "hpnicfFdmiHbaInfoFabricIndex"),
    (0, "HPN-ICF-FDMI-MIB", "hpnicfFdmiHbaInfoId"),
    (0, "HPN-ICF-FDMI-MIB", "hpnicfFdmiHbaPortId"),
)
if mibBuilder.loadTexts:
    hpnicfFdmiHbaPortEntry.setStatus("current")
_HpnicfFdmiHbaPortId_Type = FcNameIdOrZero
_HpnicfFdmiHbaPortId_Object = MibTableColumn
hpnicfFdmiHbaPortId = _HpnicfFdmiHbaPortId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 7, 1, 1, 2, 1, 1),
    _HpnicfFdmiHbaPortId_Type()
)
hpnicfFdmiHbaPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfFdmiHbaPortId.setStatus("current")


class _HpnicfFdmiHbaPortSupportedFC4Type_Type(OctetString):
    """Custom type hpnicfFdmiHbaPortSupportedFC4Type based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(32, 32),
    )


_HpnicfFdmiHbaPortSupportedFC4Type_Type.__name__ = "OctetString"
_HpnicfFdmiHbaPortSupportedFC4Type_Object = MibTableColumn
hpnicfFdmiHbaPortSupportedFC4Type = _HpnicfFdmiHbaPortSupportedFC4Type_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 7, 1, 1, 2, 1, 2),
    _HpnicfFdmiHbaPortSupportedFC4Type_Type()
)
hpnicfFdmiHbaPortSupportedFC4Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFdmiHbaPortSupportedFC4Type.setStatus("current")
_HpnicfFdmiHbaPortSupportedSpeed_Type = Unsigned32
_HpnicfFdmiHbaPortSupportedSpeed_Object = MibTableColumn
hpnicfFdmiHbaPortSupportedSpeed = _HpnicfFdmiHbaPortSupportedSpeed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 7, 1, 1, 2, 1, 3),
    _HpnicfFdmiHbaPortSupportedSpeed_Type()
)
hpnicfFdmiHbaPortSupportedSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFdmiHbaPortSupportedSpeed.setStatus("current")
_HpnicfFdmiHbaPortCurrentSpeed_Type = Unsigned32
_HpnicfFdmiHbaPortCurrentSpeed_Object = MibTableColumn
hpnicfFdmiHbaPortCurrentSpeed = _HpnicfFdmiHbaPortCurrentSpeed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 7, 1, 1, 2, 1, 4),
    _HpnicfFdmiHbaPortCurrentSpeed_Type()
)
hpnicfFdmiHbaPortCurrentSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFdmiHbaPortCurrentSpeed.setStatus("current")
_HpnicfFdmiHbaPortMaxFrameSize_Type = Unsigned32
_HpnicfFdmiHbaPortMaxFrameSize_Object = MibTableColumn
hpnicfFdmiHbaPortMaxFrameSize = _HpnicfFdmiHbaPortMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 7, 1, 1, 2, 1, 5),
    _HpnicfFdmiHbaPortMaxFrameSize_Type()
)
hpnicfFdmiHbaPortMaxFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFdmiHbaPortMaxFrameSize.setStatus("current")
_HpnicfFdmiHbaPortOsDevName_Type = SnmpAdminString
_HpnicfFdmiHbaPortOsDevName_Object = MibTableColumn
hpnicfFdmiHbaPortOsDevName = _HpnicfFdmiHbaPortOsDevName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 7, 1, 1, 2, 1, 6),
    _HpnicfFdmiHbaPortOsDevName_Type()
)
hpnicfFdmiHbaPortOsDevName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFdmiHbaPortOsDevName.setStatus("current")
_HpnicfFdmiHbaPortHostName_Type = SnmpAdminString
_HpnicfFdmiHbaPortHostName_Object = MibTableColumn
hpnicfFdmiHbaPortHostName = _HpnicfFdmiHbaPortHostName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 7, 1, 1, 2, 1, 7),
    _HpnicfFdmiHbaPortHostName_Type()
)
hpnicfFdmiHbaPortHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFdmiHbaPortHostName.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-FDMI-MIB",
    **{"hpnicfFdmi": hpnicfFdmi,
       "hpnicfFdmiObjects": hpnicfFdmiObjects,
       "hpnicfFdmiInfo": hpnicfFdmiInfo,
       "hpnicfFdmiHbaInfoTable": hpnicfFdmiHbaInfoTable,
       "hpnicfFdmiHbaInfoEntry": hpnicfFdmiHbaInfoEntry,
       "hpnicfFdmiHbaInfoFabricIndex": hpnicfFdmiHbaInfoFabricIndex,
       "hpnicfFdmiHbaInfoId": hpnicfFdmiHbaInfoId,
       "hpnicfFdmiHbaInfoNodeName": hpnicfFdmiHbaInfoNodeName,
       "hpnicfFdmiHbaInfoMfg": hpnicfFdmiHbaInfoMfg,
       "hpnicfFdmiHbaInfoSn": hpnicfFdmiHbaInfoSn,
       "hpnicfFdmiHbaInfoModel": hpnicfFdmiHbaInfoModel,
       "hpnicfFdmiHbaInfoModelDescr": hpnicfFdmiHbaInfoModelDescr,
       "hpnicfFdmiHbaInfoHwVer": hpnicfFdmiHbaInfoHwVer,
       "hpnicfFdmiHbaInfoDriverVer": hpnicfFdmiHbaInfoDriverVer,
       "hpnicfFdmiHbaInfoOptROMVer": hpnicfFdmiHbaInfoOptROMVer,
       "hpnicfFdmiHbaInfoFwVer": hpnicfFdmiHbaInfoFwVer,
       "hpnicfFdmiHbaInfoOSInfo": hpnicfFdmiHbaInfoOSInfo,
       "hpnicfFdmiHbaInfoMaxCTPayload": hpnicfFdmiHbaInfoMaxCTPayload,
       "hpnicfFdmiHbaPortTable": hpnicfFdmiHbaPortTable,
       "hpnicfFdmiHbaPortEntry": hpnicfFdmiHbaPortEntry,
       "hpnicfFdmiHbaPortId": hpnicfFdmiHbaPortId,
       "hpnicfFdmiHbaPortSupportedFC4Type": hpnicfFdmiHbaPortSupportedFC4Type,
       "hpnicfFdmiHbaPortSupportedSpeed": hpnicfFdmiHbaPortSupportedSpeed,
       "hpnicfFdmiHbaPortCurrentSpeed": hpnicfFdmiHbaPortCurrentSpeed,
       "hpnicfFdmiHbaPortMaxFrameSize": hpnicfFdmiHbaPortMaxFrameSize,
       "hpnicfFdmiHbaPortOsDevName": hpnicfFdmiHbaPortOsDevName,
       "hpnicfFdmiHbaPortHostName": hpnicfFdmiHbaPortHostName}
)
