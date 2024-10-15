# SNMP MIB module (CISCO-FDMI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-FDMI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:00:29 2024
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

(FcNameId,) = mibBuilder.importSymbols(
    "CISCO-ST-TC",
    "FcNameId")

(notifyVsanIndex,
 vsanIndex) = mibBuilder.importSymbols(
    "CISCO-VSAN-MIB",
    "notifyVsanIndex",
    "vsanIndex")

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

ciscoFdmiMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 373)
)
ciscoFdmiMIB.setRevisions(
        ("2003-11-07 00:00",
         "2003-08-24 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CFdmiRejectReasonCode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalidCommandCode", 1),
          ("invalidSize", 3),
          ("unableToPerformCmdReq", 2))
    )



class CFdmiRejectReasonCodeExpl(Integer32, TextualConvention):
    status = "current"
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
        *(("attrForSpecifiedHbaNotReg", 3),
          ("hbaAlreadyRegistered", 2),
          ("hbaAttrMultiAttribSameType", 4),
          ("hbaIdNotInRegPortList", 8),
          ("invalidHbaAttrBlockLen", 5),
          ("invalidPortAttrBlockLen", 12),
          ("noAdditionalExpl", 1),
          ("none", 13),
          ("origPortNotInRegPortList", 7),
          ("portAttrMultiAttrSameType", 11),
          ("portAttrNotRegistered", 9),
          ("portNotRegistered", 10),
          ("reqdHbaAttrNotPresent", 6))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoFdmiMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoFdmiMIBNotifications = _CiscoFdmiMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 373, 0)
)
_CiscoFdmiMIBObjects_ObjectIdentity = ObjectIdentity
ciscoFdmiMIBObjects = _CiscoFdmiMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 373, 1)
)
_CfdmiConfig_ObjectIdentity = ObjectIdentity
cfdmiConfig = _CfdmiConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 373, 1, 1)
)


class _CfdmiRejectRegNotifyEnable_Type(TruthValue):
    """Custom type cfdmiRejectRegNotifyEnable based on TruthValue"""


_CfdmiRejectRegNotifyEnable_Object = MibScalar
cfdmiRejectRegNotifyEnable = _CfdmiRejectRegNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 373, 1, 1, 1),
    _CfdmiRejectRegNotifyEnable_Type()
)
cfdmiRejectRegNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfdmiRejectRegNotifyEnable.setStatus("current")
_CfdmiInfo_ObjectIdentity = ObjectIdentity
cfdmiInfo = _CfdmiInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 373, 1, 2)
)
_CfdmiHbaInfoTable_Object = MibTable
cfdmiHbaInfoTable = _CfdmiHbaInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 373, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cfdmiHbaInfoTable.setStatus("current")
_CfdmiHbaInfoEntry_Object = MibTableRow
cfdmiHbaInfoEntry = _CfdmiHbaInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 373, 1, 2, 1, 1)
)
cfdmiHbaInfoEntry.setIndexNames(
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
    (0, "CISCO-FDMI-MIB", "cfdmiHbaInfoId"),
)
if mibBuilder.loadTexts:
    cfdmiHbaInfoEntry.setStatus("current")
_CfdmiHbaInfoId_Type = FcNameId
_CfdmiHbaInfoId_Object = MibTableColumn
cfdmiHbaInfoId = _CfdmiHbaInfoId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 373, 1, 2, 1, 1, 1),
    _CfdmiHbaInfoId_Type()
)
cfdmiHbaInfoId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfdmiHbaInfoId.setStatus("current")
_CfdmiHbaInfoNodeName_Type = FcNameId
_CfdmiHbaInfoNodeName_Object = MibTableColumn
cfdmiHbaInfoNodeName = _CfdmiHbaInfoNodeName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 373, 1, 2, 1, 1, 2),
    _CfdmiHbaInfoNodeName_Type()
)
cfdmiHbaInfoNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfdmiHbaInfoNodeName.setStatus("current")


class _CfdmiHbaInfoMfg_Type(SnmpAdminString):
    """Custom type cfdmiHbaInfoMfg based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_CfdmiHbaInfoMfg_Type.__name__ = "SnmpAdminString"
_CfdmiHbaInfoMfg_Object = MibTableColumn
cfdmiHbaInfoMfg = _CfdmiHbaInfoMfg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 373, 1, 2, 1, 1, 3),
    _CfdmiHbaInfoMfg_Type()
)
cfdmiHbaInfoMfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfdmiHbaInfoMfg.setStatus("current")


class _CfdmiHbaInfoSn_Type(SnmpAdminString):
    """Custom type cfdmiHbaInfoSn based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_CfdmiHbaInfoSn_Type.__name__ = "SnmpAdminString"
_CfdmiHbaInfoSn_Object = MibTableColumn
cfdmiHbaInfoSn = _CfdmiHbaInfoSn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 373, 1, 2, 1, 1, 4),
    _CfdmiHbaInfoSn_Type()
)
cfdmiHbaInfoSn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfdmiHbaInfoSn.setStatus("current")


class _CfdmiHbaInfoModel_Type(SnmpAdminString):
    """Custom type cfdmiHbaInfoModel based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CfdmiHbaInfoModel_Type.__name__ = "SnmpAdminString"
_CfdmiHbaInfoModel_Object = MibTableColumn
cfdmiHbaInfoModel = _CfdmiHbaInfoModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 373, 1, 2, 1, 1, 5),
    _CfdmiHbaInfoModel_Type()
)
cfdmiHbaInfoModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfdmiHbaInfoModel.setStatus("current")


class _CfdmiHbaInfoModelDescr_Type(SnmpAdminString):
    """Custom type cfdmiHbaInfoModelDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CfdmiHbaInfoModelDescr_Type.__name__ = "SnmpAdminString"
_CfdmiHbaInfoModelDescr_Object = MibTableColumn
cfdmiHbaInfoModelDescr = _CfdmiHbaInfoModelDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 373, 1, 2, 1, 1, 6),
    _CfdmiHbaInfoModelDescr_Type()
)
cfdmiHbaInfoModelDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfdmiHbaInfoModelDescr.setStatus("current")


class _CfdmiHbaInfoHwVer_Type(SnmpAdminString):
    """Custom type cfdmiHbaInfoHwVer based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CfdmiHbaInfoHwVer_Type.__name__ = "SnmpAdminString"
_CfdmiHbaInfoHwVer_Object = MibTableColumn
cfdmiHbaInfoHwVer = _CfdmiHbaInfoHwVer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 373, 1, 2, 1, 1, 7),
    _CfdmiHbaInfoHwVer_Type()
)
cfdmiHbaInfoHwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfdmiHbaInfoHwVer.setStatus("current")


class _CfdmiHbaInfoDriverVer_Type(SnmpAdminString):
    """Custom type cfdmiHbaInfoDriverVer based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CfdmiHbaInfoDriverVer_Type.__name__ = "SnmpAdminString"
_CfdmiHbaInfoDriverVer_Object = MibTableColumn
cfdmiHbaInfoDriverVer = _CfdmiHbaInfoDriverVer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 373, 1, 2, 1, 1, 8),
    _CfdmiHbaInfoDriverVer_Type()
)
cfdmiHbaInfoDriverVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfdmiHbaInfoDriverVer.setStatus("current")


class _CfdmiHbaInfoOptROMVer_Type(SnmpAdminString):
    """Custom type cfdmiHbaInfoOptROMVer based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CfdmiHbaInfoOptROMVer_Type.__name__ = "SnmpAdminString"
_CfdmiHbaInfoOptROMVer_Object = MibTableColumn
cfdmiHbaInfoOptROMVer = _CfdmiHbaInfoOptROMVer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 373, 1, 2, 1, 1, 9),
    _CfdmiHbaInfoOptROMVer_Type()
)
cfdmiHbaInfoOptROMVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfdmiHbaInfoOptROMVer.setStatus("current")


class _CfdmiHbaInfoFwVer_Type(SnmpAdminString):
    """Custom type cfdmiHbaInfoFwVer based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CfdmiHbaInfoFwVer_Type.__name__ = "SnmpAdminString"
_CfdmiHbaInfoFwVer_Object = MibTableColumn
cfdmiHbaInfoFwVer = _CfdmiHbaInfoFwVer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 373, 1, 2, 1, 1, 10),
    _CfdmiHbaInfoFwVer_Type()
)
cfdmiHbaInfoFwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfdmiHbaInfoFwVer.setStatus("current")


class _CfdmiHbaInfoOSInfo_Type(SnmpAdminString):
    """Custom type cfdmiHbaInfoOSInfo based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CfdmiHbaInfoOSInfo_Type.__name__ = "SnmpAdminString"
_CfdmiHbaInfoOSInfo_Object = MibTableColumn
cfdmiHbaInfoOSInfo = _CfdmiHbaInfoOSInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 373, 1, 2, 1, 1, 11),
    _CfdmiHbaInfoOSInfo_Type()
)
cfdmiHbaInfoOSInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfdmiHbaInfoOSInfo.setStatus("current")
_CfdmiHbaInfoMaxCTPayload_Type = Unsigned32
_CfdmiHbaInfoMaxCTPayload_Object = MibTableColumn
cfdmiHbaInfoMaxCTPayload = _CfdmiHbaInfoMaxCTPayload_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 373, 1, 2, 1, 1, 12),
    _CfdmiHbaInfoMaxCTPayload_Type()
)
cfdmiHbaInfoMaxCTPayload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfdmiHbaInfoMaxCTPayload.setStatus("current")
if mibBuilder.loadTexts:
    cfdmiHbaInfoMaxCTPayload.setUnits("32-bit words")
_CfdmiHbaPortTable_Object = MibTable
cfdmiHbaPortTable = _CfdmiHbaPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 373, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cfdmiHbaPortTable.setStatus("current")
_CfdmiHbaPortEntry_Object = MibTableRow
cfdmiHbaPortEntry = _CfdmiHbaPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 373, 1, 2, 2, 1)
)
cfdmiHbaPortEntry.setIndexNames(
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
    (0, "CISCO-FDMI-MIB", "cfdmiHbaInfoId"),
    (0, "CISCO-FDMI-MIB", "cfdmiHbaPortId"),
)
if mibBuilder.loadTexts:
    cfdmiHbaPortEntry.setStatus("current")
_CfdmiHbaPortId_Type = FcNameId
_CfdmiHbaPortId_Object = MibTableColumn
cfdmiHbaPortId = _CfdmiHbaPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 373, 1, 2, 2, 1, 1),
    _CfdmiHbaPortId_Type()
)
cfdmiHbaPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfdmiHbaPortId.setStatus("current")
_CfdmiHbaPortSupportedFC4Type_Type = OctetString
_CfdmiHbaPortSupportedFC4Type_Object = MibTableColumn
cfdmiHbaPortSupportedFC4Type = _CfdmiHbaPortSupportedFC4Type_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 373, 1, 2, 2, 1, 2),
    _CfdmiHbaPortSupportedFC4Type_Type()
)
cfdmiHbaPortSupportedFC4Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfdmiHbaPortSupportedFC4Type.setStatus("current")
_CfdmiHbaPortSupportedSpeed_Type = Unsigned32
_CfdmiHbaPortSupportedSpeed_Object = MibTableColumn
cfdmiHbaPortSupportedSpeed = _CfdmiHbaPortSupportedSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 373, 1, 2, 2, 1, 3),
    _CfdmiHbaPortSupportedSpeed_Type()
)
cfdmiHbaPortSupportedSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfdmiHbaPortSupportedSpeed.setStatus("current")
_CfdmiHbaPortCurrentSpeed_Type = Unsigned32
_CfdmiHbaPortCurrentSpeed_Object = MibTableColumn
cfdmiHbaPortCurrentSpeed = _CfdmiHbaPortCurrentSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 373, 1, 2, 2, 1, 4),
    _CfdmiHbaPortCurrentSpeed_Type()
)
cfdmiHbaPortCurrentSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfdmiHbaPortCurrentSpeed.setStatus("current")
_CfdmiHbaPortMaxFrameSize_Type = Unsigned32
_CfdmiHbaPortMaxFrameSize_Object = MibTableColumn
cfdmiHbaPortMaxFrameSize = _CfdmiHbaPortMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 373, 1, 2, 2, 1, 5),
    _CfdmiHbaPortMaxFrameSize_Type()
)
cfdmiHbaPortMaxFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfdmiHbaPortMaxFrameSize.setStatus("current")


class _CfdmiHbaPortOsDevName_Type(SnmpAdminString):
    """Custom type cfdmiHbaPortOsDevName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CfdmiHbaPortOsDevName_Type.__name__ = "SnmpAdminString"
_CfdmiHbaPortOsDevName_Object = MibTableColumn
cfdmiHbaPortOsDevName = _CfdmiHbaPortOsDevName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 373, 1, 2, 2, 1, 6),
    _CfdmiHbaPortOsDevName_Type()
)
cfdmiHbaPortOsDevName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfdmiHbaPortOsDevName.setStatus("current")


class _CfdmiHbaPortHostName_Type(SnmpAdminString):
    """Custom type cfdmiHbaPortHostName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CfdmiHbaPortHostName_Type.__name__ = "SnmpAdminString"
_CfdmiHbaPortHostName_Object = MibTableColumn
cfdmiHbaPortHostName = _CfdmiHbaPortHostName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 373, 1, 2, 2, 1, 7),
    _CfdmiHbaPortHostName_Type()
)
cfdmiHbaPortHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfdmiHbaPortHostName.setStatus("current")
_CfdmiRejectReasonCode_Type = CFdmiRejectReasonCode
_CfdmiRejectReasonCode_Object = MibScalar
cfdmiRejectReasonCode = _CfdmiRejectReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 373, 1, 2, 3),
    _CfdmiRejectReasonCode_Type()
)
cfdmiRejectReasonCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cfdmiRejectReasonCode.setStatus("current")
_CfdmiRejectReasonCodeExpl_Type = CFdmiRejectReasonCodeExpl
_CfdmiRejectReasonCodeExpl_Object = MibScalar
cfdmiRejectReasonCodeExpl = _CfdmiRejectReasonCodeExpl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 373, 1, 2, 4),
    _CfdmiRejectReasonCodeExpl_Type()
)
cfdmiRejectReasonCodeExpl.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cfdmiRejectReasonCodeExpl.setStatus("current")


class _CfdmiNotifyRegOperType_Type(Integer32):
    """Custom type cfdmiNotifyRegOperType based on Integer32"""
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
        *(("regHAT", 2),
          ("regHBA", 1),
          ("regPA", 4),
          ("regPRT", 3))
    )


_CfdmiNotifyRegOperType_Type.__name__ = "Integer32"
_CfdmiNotifyRegOperType_Object = MibScalar
cfdmiNotifyRegOperType = _CfdmiNotifyRegOperType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 373, 1, 2, 5),
    _CfdmiNotifyRegOperType_Type()
)
cfdmiNotifyRegOperType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cfdmiNotifyRegOperType.setStatus("current")
_CfdmiNotifyHBAPortId_Type = FcNameId
_CfdmiNotifyHBAPortId_Object = MibScalar
cfdmiNotifyHBAPortId = _CfdmiNotifyHBAPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 373, 1, 2, 6),
    _CfdmiNotifyHBAPortId_Type()
)
cfdmiNotifyHBAPortId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cfdmiNotifyHBAPortId.setStatus("current")
_CfdmiStatistics_ObjectIdentity = ObjectIdentity
cfdmiStatistics = _CfdmiStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 373, 1, 3)
)
_CiscoFdmiMIBConformance_ObjectIdentity = ObjectIdentity
ciscoFdmiMIBConformance = _CiscoFdmiMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 373, 2)
)
_CiscoFdmiMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoFdmiMIBCompliances = _CiscoFdmiMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 373, 2, 1)
)
_CiscoFdmiMIBGroups_ObjectIdentity = ObjectIdentity
ciscoFdmiMIBGroups = _CiscoFdmiMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 373, 2, 2)
)

# Managed Objects groups

cfdmiConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 373, 2, 2, 1)
)
cfdmiConfigGroup.setObjects(
    ("CISCO-FDMI-MIB", "cfdmiRejectRegNotifyEnable")
)
if mibBuilder.loadTexts:
    cfdmiConfigGroup.setStatus("current")

cfdmiHbaInformationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 373, 2, 2, 2)
)
cfdmiHbaInformationGroup.setObjects(
      *(("CISCO-FDMI-MIB", "cfdmiHbaInfoNodeName"),
        ("CISCO-FDMI-MIB", "cfdmiHbaInfoMfg"),
        ("CISCO-FDMI-MIB", "cfdmiHbaInfoSn"),
        ("CISCO-FDMI-MIB", "cfdmiHbaInfoModel"),
        ("CISCO-FDMI-MIB", "cfdmiHbaInfoModelDescr"),
        ("CISCO-FDMI-MIB", "cfdmiHbaInfoHwVer"),
        ("CISCO-FDMI-MIB", "cfdmiHbaInfoDriverVer"),
        ("CISCO-FDMI-MIB", "cfdmiHbaInfoOptROMVer"),
        ("CISCO-FDMI-MIB", "cfdmiHbaInfoFwVer"),
        ("CISCO-FDMI-MIB", "cfdmiHbaInfoOSInfo"),
        ("CISCO-FDMI-MIB", "cfdmiHbaInfoMaxCTPayload"),
        ("CISCO-FDMI-MIB", "cfdmiRejectReasonCode"),
        ("CISCO-FDMI-MIB", "cfdmiRejectReasonCodeExpl"),
        ("CISCO-FDMI-MIB", "cfdmiNotifyRegOperType"),
        ("CISCO-FDMI-MIB", "cfdmiNotifyHBAPortId"))
)
if mibBuilder.loadTexts:
    cfdmiHbaInformationGroup.setStatus("current")

cfdmiHbaPortInformationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 373, 2, 2, 3)
)
cfdmiHbaPortInformationGroup.setObjects(
      *(("CISCO-FDMI-MIB", "cfdmiHbaPortSupportedFC4Type"),
        ("CISCO-FDMI-MIB", "cfdmiHbaPortSupportedSpeed"),
        ("CISCO-FDMI-MIB", "cfdmiHbaPortCurrentSpeed"),
        ("CISCO-FDMI-MIB", "cfdmiHbaPortMaxFrameSize"),
        ("CISCO-FDMI-MIB", "cfdmiHbaPortOsDevName"),
        ("CISCO-FDMI-MIB", "cfdmiHbaPortHostName"))
)
if mibBuilder.loadTexts:
    cfdmiHbaPortInformationGroup.setStatus("current")


# Notification objects

cfdmiRejectRegNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 373, 0, 1)
)
cfdmiRejectRegNotify.setObjects(
      *(("CISCO-VSAN-MIB", "notifyVsanIndex"),
        ("CISCO-FDMI-MIB", "cfdmiNotifyRegOperType"),
        ("CISCO-FDMI-MIB", "cfdmiNotifyHBAPortId"),
        ("CISCO-FDMI-MIB", "cfdmiRejectReasonCode"),
        ("CISCO-FDMI-MIB", "cfdmiRejectReasonCodeExpl"))
)
if mibBuilder.loadTexts:
    cfdmiRejectRegNotify.setStatus(
        "current"
    )


# Notifications groups

cfdmiNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 373, 2, 2, 4)
)
cfdmiNotificationGroup.setObjects(
    ("CISCO-FDMI-MIB", "cfdmiRejectRegNotify")
)
if mibBuilder.loadTexts:
    cfdmiNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoFdmiMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 373, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoFdmiMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FDMI-MIB",
    **{"CFdmiRejectReasonCode": CFdmiRejectReasonCode,
       "CFdmiRejectReasonCodeExpl": CFdmiRejectReasonCodeExpl,
       "ciscoFdmiMIB": ciscoFdmiMIB,
       "ciscoFdmiMIBNotifications": ciscoFdmiMIBNotifications,
       "cfdmiRejectRegNotify": cfdmiRejectRegNotify,
       "ciscoFdmiMIBObjects": ciscoFdmiMIBObjects,
       "cfdmiConfig": cfdmiConfig,
       "cfdmiRejectRegNotifyEnable": cfdmiRejectRegNotifyEnable,
       "cfdmiInfo": cfdmiInfo,
       "cfdmiHbaInfoTable": cfdmiHbaInfoTable,
       "cfdmiHbaInfoEntry": cfdmiHbaInfoEntry,
       "cfdmiHbaInfoId": cfdmiHbaInfoId,
       "cfdmiHbaInfoNodeName": cfdmiHbaInfoNodeName,
       "cfdmiHbaInfoMfg": cfdmiHbaInfoMfg,
       "cfdmiHbaInfoSn": cfdmiHbaInfoSn,
       "cfdmiHbaInfoModel": cfdmiHbaInfoModel,
       "cfdmiHbaInfoModelDescr": cfdmiHbaInfoModelDescr,
       "cfdmiHbaInfoHwVer": cfdmiHbaInfoHwVer,
       "cfdmiHbaInfoDriverVer": cfdmiHbaInfoDriverVer,
       "cfdmiHbaInfoOptROMVer": cfdmiHbaInfoOptROMVer,
       "cfdmiHbaInfoFwVer": cfdmiHbaInfoFwVer,
       "cfdmiHbaInfoOSInfo": cfdmiHbaInfoOSInfo,
       "cfdmiHbaInfoMaxCTPayload": cfdmiHbaInfoMaxCTPayload,
       "cfdmiHbaPortTable": cfdmiHbaPortTable,
       "cfdmiHbaPortEntry": cfdmiHbaPortEntry,
       "cfdmiHbaPortId": cfdmiHbaPortId,
       "cfdmiHbaPortSupportedFC4Type": cfdmiHbaPortSupportedFC4Type,
       "cfdmiHbaPortSupportedSpeed": cfdmiHbaPortSupportedSpeed,
       "cfdmiHbaPortCurrentSpeed": cfdmiHbaPortCurrentSpeed,
       "cfdmiHbaPortMaxFrameSize": cfdmiHbaPortMaxFrameSize,
       "cfdmiHbaPortOsDevName": cfdmiHbaPortOsDevName,
       "cfdmiHbaPortHostName": cfdmiHbaPortHostName,
       "cfdmiRejectReasonCode": cfdmiRejectReasonCode,
       "cfdmiRejectReasonCodeExpl": cfdmiRejectReasonCodeExpl,
       "cfdmiNotifyRegOperType": cfdmiNotifyRegOperType,
       "cfdmiNotifyHBAPortId": cfdmiNotifyHBAPortId,
       "cfdmiStatistics": cfdmiStatistics,
       "ciscoFdmiMIBConformance": ciscoFdmiMIBConformance,
       "ciscoFdmiMIBCompliances": ciscoFdmiMIBCompliances,
       "ciscoFdmiMIBCompliance": ciscoFdmiMIBCompliance,
       "ciscoFdmiMIBGroups": ciscoFdmiMIBGroups,
       "cfdmiConfigGroup": cfdmiConfigGroup,
       "cfdmiHbaInformationGroup": cfdmiHbaInformationGroup,
       "cfdmiHbaPortInformationGroup": cfdmiHbaPortInformationGroup,
       "cfdmiNotificationGroup": cfdmiNotificationGroup}
)
