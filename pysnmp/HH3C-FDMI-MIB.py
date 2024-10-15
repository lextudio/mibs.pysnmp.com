# SNMP MIB module (HH3C-FDMI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-FDMI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:53:24 2024
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

(hh3cSan,) = mibBuilder.importSymbols(
    "HH3C-VSAN-MIB",
    "hh3cSan")

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

hh3cFdmi = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 7)
)
hh3cFdmi.setRevisions(
        ("2012-06-18 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cFdmiObjects_ObjectIdentity = ObjectIdentity
hh3cFdmiObjects = _Hh3cFdmiObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 7, 1)
)
_Hh3cFdmiInfo_ObjectIdentity = ObjectIdentity
hh3cFdmiInfo = _Hh3cFdmiInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 7, 1, 1)
)
_Hh3cFdmiHbaInfoTable_Object = MibTable
hh3cFdmiHbaInfoTable = _Hh3cFdmiHbaInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 7, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cFdmiHbaInfoTable.setStatus("current")
_Hh3cFdmiHbaInfoEntry_Object = MibTableRow
hh3cFdmiHbaInfoEntry = _Hh3cFdmiHbaInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 7, 1, 1, 1, 1)
)
hh3cFdmiHbaInfoEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "HH3C-FDMI-MIB", "hh3cFdmiHbaInfoFabricIndex"),
    (0, "HH3C-FDMI-MIB", "hh3cFdmiHbaInfoId"),
)
if mibBuilder.loadTexts:
    hh3cFdmiHbaInfoEntry.setStatus("current")
_Hh3cFdmiHbaInfoFabricIndex_Type = T11FabricIndex
_Hh3cFdmiHbaInfoFabricIndex_Object = MibTableColumn
hh3cFdmiHbaInfoFabricIndex = _Hh3cFdmiHbaInfoFabricIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 7, 1, 1, 1, 1, 1),
    _Hh3cFdmiHbaInfoFabricIndex_Type()
)
hh3cFdmiHbaInfoFabricIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cFdmiHbaInfoFabricIndex.setStatus("current")
_Hh3cFdmiHbaInfoId_Type = FcNameIdOrZero
_Hh3cFdmiHbaInfoId_Object = MibTableColumn
hh3cFdmiHbaInfoId = _Hh3cFdmiHbaInfoId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 7, 1, 1, 1, 1, 2),
    _Hh3cFdmiHbaInfoId_Type()
)
hh3cFdmiHbaInfoId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cFdmiHbaInfoId.setStatus("current")
_Hh3cFdmiHbaInfoNodeName_Type = FcNameIdOrZero
_Hh3cFdmiHbaInfoNodeName_Object = MibTableColumn
hh3cFdmiHbaInfoNodeName = _Hh3cFdmiHbaInfoNodeName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 7, 1, 1, 1, 1, 3),
    _Hh3cFdmiHbaInfoNodeName_Type()
)
hh3cFdmiHbaInfoNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFdmiHbaInfoNodeName.setStatus("current")
_Hh3cFdmiHbaInfoMfg_Type = SnmpAdminString
_Hh3cFdmiHbaInfoMfg_Object = MibTableColumn
hh3cFdmiHbaInfoMfg = _Hh3cFdmiHbaInfoMfg_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 7, 1, 1, 1, 1, 4),
    _Hh3cFdmiHbaInfoMfg_Type()
)
hh3cFdmiHbaInfoMfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFdmiHbaInfoMfg.setStatus("current")
_Hh3cFdmiHbaInfoSn_Type = SnmpAdminString
_Hh3cFdmiHbaInfoSn_Object = MibTableColumn
hh3cFdmiHbaInfoSn = _Hh3cFdmiHbaInfoSn_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 7, 1, 1, 1, 1, 5),
    _Hh3cFdmiHbaInfoSn_Type()
)
hh3cFdmiHbaInfoSn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFdmiHbaInfoSn.setStatus("current")
_Hh3cFdmiHbaInfoModel_Type = SnmpAdminString
_Hh3cFdmiHbaInfoModel_Object = MibTableColumn
hh3cFdmiHbaInfoModel = _Hh3cFdmiHbaInfoModel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 7, 1, 1, 1, 1, 6),
    _Hh3cFdmiHbaInfoModel_Type()
)
hh3cFdmiHbaInfoModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFdmiHbaInfoModel.setStatus("current")
_Hh3cFdmiHbaInfoModelDescr_Type = SnmpAdminString
_Hh3cFdmiHbaInfoModelDescr_Object = MibTableColumn
hh3cFdmiHbaInfoModelDescr = _Hh3cFdmiHbaInfoModelDescr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 7, 1, 1, 1, 1, 7),
    _Hh3cFdmiHbaInfoModelDescr_Type()
)
hh3cFdmiHbaInfoModelDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFdmiHbaInfoModelDescr.setStatus("current")
_Hh3cFdmiHbaInfoHwVer_Type = SnmpAdminString
_Hh3cFdmiHbaInfoHwVer_Object = MibTableColumn
hh3cFdmiHbaInfoHwVer = _Hh3cFdmiHbaInfoHwVer_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 7, 1, 1, 1, 1, 8),
    _Hh3cFdmiHbaInfoHwVer_Type()
)
hh3cFdmiHbaInfoHwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFdmiHbaInfoHwVer.setStatus("current")
_Hh3cFdmiHbaInfoDriverVer_Type = SnmpAdminString
_Hh3cFdmiHbaInfoDriverVer_Object = MibTableColumn
hh3cFdmiHbaInfoDriverVer = _Hh3cFdmiHbaInfoDriverVer_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 7, 1, 1, 1, 1, 9),
    _Hh3cFdmiHbaInfoDriverVer_Type()
)
hh3cFdmiHbaInfoDriverVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFdmiHbaInfoDriverVer.setStatus("current")
_Hh3cFdmiHbaInfoOptROMVer_Type = SnmpAdminString
_Hh3cFdmiHbaInfoOptROMVer_Object = MibTableColumn
hh3cFdmiHbaInfoOptROMVer = _Hh3cFdmiHbaInfoOptROMVer_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 7, 1, 1, 1, 1, 10),
    _Hh3cFdmiHbaInfoOptROMVer_Type()
)
hh3cFdmiHbaInfoOptROMVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFdmiHbaInfoOptROMVer.setStatus("current")
_Hh3cFdmiHbaInfoFwVer_Type = SnmpAdminString
_Hh3cFdmiHbaInfoFwVer_Object = MibTableColumn
hh3cFdmiHbaInfoFwVer = _Hh3cFdmiHbaInfoFwVer_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 7, 1, 1, 1, 1, 11),
    _Hh3cFdmiHbaInfoFwVer_Type()
)
hh3cFdmiHbaInfoFwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFdmiHbaInfoFwVer.setStatus("current")
_Hh3cFdmiHbaInfoOSInfo_Type = SnmpAdminString
_Hh3cFdmiHbaInfoOSInfo_Object = MibTableColumn
hh3cFdmiHbaInfoOSInfo = _Hh3cFdmiHbaInfoOSInfo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 7, 1, 1, 1, 1, 12),
    _Hh3cFdmiHbaInfoOSInfo_Type()
)
hh3cFdmiHbaInfoOSInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFdmiHbaInfoOSInfo.setStatus("current")
_Hh3cFdmiHbaInfoMaxCTPayload_Type = Unsigned32
_Hh3cFdmiHbaInfoMaxCTPayload_Object = MibTableColumn
hh3cFdmiHbaInfoMaxCTPayload = _Hh3cFdmiHbaInfoMaxCTPayload_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 7, 1, 1, 1, 1, 13),
    _Hh3cFdmiHbaInfoMaxCTPayload_Type()
)
hh3cFdmiHbaInfoMaxCTPayload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFdmiHbaInfoMaxCTPayload.setStatus("current")
_Hh3cFdmiHbaPortTable_Object = MibTable
hh3cFdmiHbaPortTable = _Hh3cFdmiHbaPortTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 7, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cFdmiHbaPortTable.setStatus("current")
_Hh3cFdmiHbaPortEntry_Object = MibTableRow
hh3cFdmiHbaPortEntry = _Hh3cFdmiHbaPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 7, 1, 1, 2, 1)
)
hh3cFdmiHbaPortEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "HH3C-FDMI-MIB", "hh3cFdmiHbaInfoFabricIndex"),
    (0, "HH3C-FDMI-MIB", "hh3cFdmiHbaInfoId"),
    (0, "HH3C-FDMI-MIB", "hh3cFdmiHbaPortId"),
)
if mibBuilder.loadTexts:
    hh3cFdmiHbaPortEntry.setStatus("current")
_Hh3cFdmiHbaPortId_Type = FcNameIdOrZero
_Hh3cFdmiHbaPortId_Object = MibTableColumn
hh3cFdmiHbaPortId = _Hh3cFdmiHbaPortId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 7, 1, 1, 2, 1, 1),
    _Hh3cFdmiHbaPortId_Type()
)
hh3cFdmiHbaPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cFdmiHbaPortId.setStatus("current")


class _Hh3cFdmiHbaPortSupportedFC4Type_Type(OctetString):
    """Custom type hh3cFdmiHbaPortSupportedFC4Type based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(32, 32),
    )


_Hh3cFdmiHbaPortSupportedFC4Type_Type.__name__ = "OctetString"
_Hh3cFdmiHbaPortSupportedFC4Type_Object = MibTableColumn
hh3cFdmiHbaPortSupportedFC4Type = _Hh3cFdmiHbaPortSupportedFC4Type_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 7, 1, 1, 2, 1, 2),
    _Hh3cFdmiHbaPortSupportedFC4Type_Type()
)
hh3cFdmiHbaPortSupportedFC4Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFdmiHbaPortSupportedFC4Type.setStatus("current")
_Hh3cFdmiHbaPortSupportedSpeed_Type = Unsigned32
_Hh3cFdmiHbaPortSupportedSpeed_Object = MibTableColumn
hh3cFdmiHbaPortSupportedSpeed = _Hh3cFdmiHbaPortSupportedSpeed_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 7, 1, 1, 2, 1, 3),
    _Hh3cFdmiHbaPortSupportedSpeed_Type()
)
hh3cFdmiHbaPortSupportedSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFdmiHbaPortSupportedSpeed.setStatus("current")
_Hh3cFdmiHbaPortCurrentSpeed_Type = Unsigned32
_Hh3cFdmiHbaPortCurrentSpeed_Object = MibTableColumn
hh3cFdmiHbaPortCurrentSpeed = _Hh3cFdmiHbaPortCurrentSpeed_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 7, 1, 1, 2, 1, 4),
    _Hh3cFdmiHbaPortCurrentSpeed_Type()
)
hh3cFdmiHbaPortCurrentSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFdmiHbaPortCurrentSpeed.setStatus("current")
_Hh3cFdmiHbaPortMaxFrameSize_Type = Unsigned32
_Hh3cFdmiHbaPortMaxFrameSize_Object = MibTableColumn
hh3cFdmiHbaPortMaxFrameSize = _Hh3cFdmiHbaPortMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 7, 1, 1, 2, 1, 5),
    _Hh3cFdmiHbaPortMaxFrameSize_Type()
)
hh3cFdmiHbaPortMaxFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFdmiHbaPortMaxFrameSize.setStatus("current")
_Hh3cFdmiHbaPortOsDevName_Type = SnmpAdminString
_Hh3cFdmiHbaPortOsDevName_Object = MibTableColumn
hh3cFdmiHbaPortOsDevName = _Hh3cFdmiHbaPortOsDevName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 7, 1, 1, 2, 1, 6),
    _Hh3cFdmiHbaPortOsDevName_Type()
)
hh3cFdmiHbaPortOsDevName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFdmiHbaPortOsDevName.setStatus("current")
_Hh3cFdmiHbaPortHostName_Type = SnmpAdminString
_Hh3cFdmiHbaPortHostName_Object = MibTableColumn
hh3cFdmiHbaPortHostName = _Hh3cFdmiHbaPortHostName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 7, 1, 1, 2, 1, 7),
    _Hh3cFdmiHbaPortHostName_Type()
)
hh3cFdmiHbaPortHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFdmiHbaPortHostName.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-FDMI-MIB",
    **{"hh3cFdmi": hh3cFdmi,
       "hh3cFdmiObjects": hh3cFdmiObjects,
       "hh3cFdmiInfo": hh3cFdmiInfo,
       "hh3cFdmiHbaInfoTable": hh3cFdmiHbaInfoTable,
       "hh3cFdmiHbaInfoEntry": hh3cFdmiHbaInfoEntry,
       "hh3cFdmiHbaInfoFabricIndex": hh3cFdmiHbaInfoFabricIndex,
       "hh3cFdmiHbaInfoId": hh3cFdmiHbaInfoId,
       "hh3cFdmiHbaInfoNodeName": hh3cFdmiHbaInfoNodeName,
       "hh3cFdmiHbaInfoMfg": hh3cFdmiHbaInfoMfg,
       "hh3cFdmiHbaInfoSn": hh3cFdmiHbaInfoSn,
       "hh3cFdmiHbaInfoModel": hh3cFdmiHbaInfoModel,
       "hh3cFdmiHbaInfoModelDescr": hh3cFdmiHbaInfoModelDescr,
       "hh3cFdmiHbaInfoHwVer": hh3cFdmiHbaInfoHwVer,
       "hh3cFdmiHbaInfoDriverVer": hh3cFdmiHbaInfoDriverVer,
       "hh3cFdmiHbaInfoOptROMVer": hh3cFdmiHbaInfoOptROMVer,
       "hh3cFdmiHbaInfoFwVer": hh3cFdmiHbaInfoFwVer,
       "hh3cFdmiHbaInfoOSInfo": hh3cFdmiHbaInfoOSInfo,
       "hh3cFdmiHbaInfoMaxCTPayload": hh3cFdmiHbaInfoMaxCTPayload,
       "hh3cFdmiHbaPortTable": hh3cFdmiHbaPortTable,
       "hh3cFdmiHbaPortEntry": hh3cFdmiHbaPortEntry,
       "hh3cFdmiHbaPortId": hh3cFdmiHbaPortId,
       "hh3cFdmiHbaPortSupportedFC4Type": hh3cFdmiHbaPortSupportedFC4Type,
       "hh3cFdmiHbaPortSupportedSpeed": hh3cFdmiHbaPortSupportedSpeed,
       "hh3cFdmiHbaPortCurrentSpeed": hh3cFdmiHbaPortCurrentSpeed,
       "hh3cFdmiHbaPortMaxFrameSize": hh3cFdmiHbaPortMaxFrameSize,
       "hh3cFdmiHbaPortOsDevName": hh3cFdmiHbaPortOsDevName,
       "hh3cFdmiHbaPortHostName": hh3cFdmiHbaPortHostName}
)
