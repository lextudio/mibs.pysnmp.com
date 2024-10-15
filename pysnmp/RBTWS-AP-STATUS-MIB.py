# SNMP MIB module (RBTWS-AP-STATUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RBTWS-AP-STATUS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:45:31 2024
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

(RbtwsApAttachType,
 RbtwsApFingerprint,
 RbtwsApNum,
 RbtwsApPortOrDapNum,
 RbtwsApSerialNum,
 RbtwsApState,
 RbtwsChannelNum,
 RbtwsPowerLevel,
 RbtwsRadioChannelWidth,
 RbtwsRadioConfigState,
 RbtwsRadioEnable,
 RbtwsRadioMimoState,
 RbtwsRadioMode,
 RbtwsRadioNum,
 RbtwsRadioRate,
 RbtwsRadioType) = mibBuilder.importSymbols(
    "RBTWS-AP-TC",
    "RbtwsApAttachType",
    "RbtwsApFingerprint",
    "RbtwsApNum",
    "RbtwsApPortOrDapNum",
    "RbtwsApSerialNum",
    "RbtwsApState",
    "RbtwsChannelNum",
    "RbtwsPowerLevel",
    "RbtwsRadioChannelWidth",
    "RbtwsRadioConfigState",
    "RbtwsRadioEnable",
    "RbtwsRadioMimoState",
    "RbtwsRadioMode",
    "RbtwsRadioNum",
    "RbtwsRadioRate",
    "RbtwsRadioType")

(rbtwsMibs,) = mibBuilder.importSymbols(
    "RBTWS-ROOT-MIB",
    "rbtwsMibs")

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
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

rbtwsApStatusMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5)
)
rbtwsApStatusMib.setRevisions(
        ("2008-05-22 01:07",
         "2008-05-09 01:04",
         "2008-02-14 01:03",
         "2007-12-07 01:00",
         "2007-07-06 00:51",
         "2007-07-05 00:50",
         "2006-09-27 00:43",
         "2006-07-28 00:35",
         "2006-07-28 00:34",
         "2006-06-26 00:20",
         "2006-06-21 00:18",
         "2006-05-10 00:17",
         "2006-03-30 00:16")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RbtwsRadioOpRateSetSingleValue(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )



class RbtwsRadioOpRateSetMandatory(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 126),
    )



class RbtwsRadioOpRateSetDisabled(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 126),
    )



# MIB Managed Objects in the order of their OIDs

_RbtwsApStatusObjects_ObjectIdentity = ObjectIdentity
rbtwsApStatusObjects = _RbtwsApStatusObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1)
)
_RbtwsApStatDataObjects_ObjectIdentity = ObjectIdentity
rbtwsApStatDataObjects = _RbtwsApStatDataObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1)
)
_RbtwsApStatNumAps_Type = Unsigned32
_RbtwsApStatNumAps_Object = MibScalar
rbtwsApStatNumAps = _RbtwsApStatNumAps_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 1),
    _RbtwsApStatNumAps_Type()
)
rbtwsApStatNumAps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatNumAps.setStatus("current")
_RbtwsApStatApStatusTable_Object = MibTable
rbtwsApStatApStatusTable = _RbtwsApStatApStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 2)
)
if mibBuilder.loadTexts:
    rbtwsApStatApStatusTable.setStatus("current")
_RbtwsApStatApStatusEntry_Object = MibTableRow
rbtwsApStatApStatusEntry = _RbtwsApStatApStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 2, 1)
)
rbtwsApStatApStatusEntry.setIndexNames(
    (0, "RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusSerialNum"),
)
if mibBuilder.loadTexts:
    rbtwsApStatApStatusEntry.setStatus("current")
_RbtwsApStatApStatusSerialNum_Type = RbtwsApSerialNum
_RbtwsApStatApStatusSerialNum_Object = MibTableColumn
rbtwsApStatApStatusSerialNum = _RbtwsApStatApStatusSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 2, 1, 1),
    _RbtwsApStatApStatusSerialNum_Type()
)
rbtwsApStatApStatusSerialNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbtwsApStatApStatusSerialNum.setStatus("current")
_RbtwsApStatApStatusBaseMac_Type = MacAddress
_RbtwsApStatApStatusBaseMac_Object = MibTableColumn
rbtwsApStatApStatusBaseMac = _RbtwsApStatApStatusBaseMac_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 2, 1, 2),
    _RbtwsApStatApStatusBaseMac_Type()
)
rbtwsApStatApStatusBaseMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatApStatusBaseMac.setStatus("current")
_RbtwsApStatApStatusAttachType_Type = RbtwsApAttachType
_RbtwsApStatApStatusAttachType_Object = MibTableColumn
rbtwsApStatApStatusAttachType = _RbtwsApStatApStatusAttachType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 2, 1, 3),
    _RbtwsApStatApStatusAttachType_Type()
)
rbtwsApStatApStatusAttachType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatApStatusAttachType.setStatus("current")
_RbtwsApStatApStatusPortOrDapNum_Type = RbtwsApPortOrDapNum
_RbtwsApStatApStatusPortOrDapNum_Object = MibTableColumn
rbtwsApStatApStatusPortOrDapNum = _RbtwsApStatApStatusPortOrDapNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 2, 1, 4),
    _RbtwsApStatApStatusPortOrDapNum_Type()
)
rbtwsApStatApStatusPortOrDapNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatApStatusPortOrDapNum.setStatus("obsolete")
_RbtwsApStatApStatusApState_Type = RbtwsApState
_RbtwsApStatApStatusApState_Object = MibTableColumn
rbtwsApStatApStatusApState = _RbtwsApStatApStatusApState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 2, 1, 5),
    _RbtwsApStatApStatusApState_Type()
)
rbtwsApStatApStatusApState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatApStatusApState.setStatus("current")
_RbtwsApStatApStatusModel_Type = DisplayString
_RbtwsApStatApStatusModel_Object = MibTableColumn
rbtwsApStatApStatusModel = _RbtwsApStatApStatusModel_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 2, 1, 6),
    _RbtwsApStatApStatusModel_Type()
)
rbtwsApStatApStatusModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatApStatusModel.setStatus("current")
_RbtwsApStatApStatusFingerprint_Type = RbtwsApFingerprint
_RbtwsApStatApStatusFingerprint_Object = MibTableColumn
rbtwsApStatApStatusFingerprint = _RbtwsApStatApStatusFingerprint_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 2, 1, 7),
    _RbtwsApStatApStatusFingerprint_Type()
)
rbtwsApStatApStatusFingerprint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatApStatusFingerprint.setStatus("current")
_RbtwsApStatApStatusApName_Type = DisplayString
_RbtwsApStatApStatusApName_Object = MibTableColumn
rbtwsApStatApStatusApName = _RbtwsApStatApStatusApName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 2, 1, 8),
    _RbtwsApStatApStatusApName_Type()
)
rbtwsApStatApStatusApName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatApStatusApName.setStatus("current")
_RbtwsApStatApStatusVlan_Type = DisplayString
_RbtwsApStatApStatusVlan_Object = MibTableColumn
rbtwsApStatApStatusVlan = _RbtwsApStatApStatusVlan_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 2, 1, 9),
    _RbtwsApStatApStatusVlan_Type()
)
rbtwsApStatApStatusVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatApStatusVlan.setStatus("current")
_RbtwsApStatApStatusIpAddress_Type = IpAddress
_RbtwsApStatApStatusIpAddress_Object = MibTableColumn
rbtwsApStatApStatusIpAddress = _RbtwsApStatApStatusIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 2, 1, 10),
    _RbtwsApStatApStatusIpAddress_Type()
)
rbtwsApStatApStatusIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatApStatusIpAddress.setStatus("current")
_RbtwsApStatApStatusUptimeSecs_Type = Unsigned32
_RbtwsApStatApStatusUptimeSecs_Object = MibTableColumn
rbtwsApStatApStatusUptimeSecs = _RbtwsApStatApStatusUptimeSecs_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 2, 1, 11),
    _RbtwsApStatApStatusUptimeSecs_Type()
)
rbtwsApStatApStatusUptimeSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatApStatusUptimeSecs.setStatus("current")
_RbtwsApStatApStatusCpuInfo_Type = DisplayString
_RbtwsApStatApStatusCpuInfo_Object = MibTableColumn
rbtwsApStatApStatusCpuInfo = _RbtwsApStatApStatusCpuInfo_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 2, 1, 12),
    _RbtwsApStatApStatusCpuInfo_Type()
)
rbtwsApStatApStatusCpuInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatApStatusCpuInfo.setStatus("current")
_RbtwsApStatApStatusManufacturerId_Type = DisplayString
_RbtwsApStatApStatusManufacturerId_Object = MibTableColumn
rbtwsApStatApStatusManufacturerId = _RbtwsApStatApStatusManufacturerId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 2, 1, 13),
    _RbtwsApStatApStatusManufacturerId_Type()
)
rbtwsApStatApStatusManufacturerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatApStatusManufacturerId.setStatus("current")
_RbtwsApStatApStatusRamBytes_Type = Unsigned32
_RbtwsApStatApStatusRamBytes_Object = MibTableColumn
rbtwsApStatApStatusRamBytes = _RbtwsApStatApStatusRamBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 2, 1, 14),
    _RbtwsApStatApStatusRamBytes_Type()
)
rbtwsApStatApStatusRamBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatApStatusRamBytes.setStatus("current")
_RbtwsApStatApStatusHardwareRev_Type = DisplayString
_RbtwsApStatApStatusHardwareRev_Object = MibTableColumn
rbtwsApStatApStatusHardwareRev = _RbtwsApStatApStatusHardwareRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 2, 1, 15),
    _RbtwsApStatApStatusHardwareRev_Type()
)
rbtwsApStatApStatusHardwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatApStatusHardwareRev.setStatus("current")
_RbtwsApStatApStatusClientSessions_Type = Unsigned32
_RbtwsApStatApStatusClientSessions_Object = MibTableColumn
rbtwsApStatApStatusClientSessions = _RbtwsApStatApStatusClientSessions_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 2, 1, 16),
    _RbtwsApStatApStatusClientSessions_Type()
)
rbtwsApStatApStatusClientSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatApStatusClientSessions.setStatus("current")
_RbtwsApStatApStatusSoftwareVer_Type = DisplayString
_RbtwsApStatApStatusSoftwareVer_Object = MibTableColumn
rbtwsApStatApStatusSoftwareVer = _RbtwsApStatApStatusSoftwareVer_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 2, 1, 17),
    _RbtwsApStatApStatusSoftwareVer_Type()
)
rbtwsApStatApStatusSoftwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatApStatusSoftwareVer.setStatus("current")
_RbtwsApStatApStatusBootVer_Type = DisplayString
_RbtwsApStatApStatusBootVer_Object = MibTableColumn
rbtwsApStatApStatusBootVer = _RbtwsApStatApStatusBootVer_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 2, 1, 18),
    _RbtwsApStatApStatusBootVer_Type()
)
rbtwsApStatApStatusBootVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatApStatusBootVer.setStatus("current")
_RbtwsApStatApStatusApNum_Type = RbtwsApNum
_RbtwsApStatApStatusApNum_Object = MibTableColumn
rbtwsApStatApStatusApNum = _RbtwsApStatApStatusApNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 2, 1, 19),
    _RbtwsApStatApStatusApNum_Type()
)
rbtwsApStatApStatusApNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatApStatusApNum.setStatus("current")
_RbtwsApStatApStatusMacTable_Object = MibTable
rbtwsApStatApStatusMacTable = _RbtwsApStatApStatusMacTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 3)
)
if mibBuilder.loadTexts:
    rbtwsApStatApStatusMacTable.setStatus("current")
_RbtwsApStatApStatusMacEntry_Object = MibTableRow
rbtwsApStatApStatusMacEntry = _RbtwsApStatApStatusMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 3, 1)
)
rbtwsApStatApStatusMacEntry.setIndexNames(
    (0, "RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusMacBaseMac"),
)
if mibBuilder.loadTexts:
    rbtwsApStatApStatusMacEntry.setStatus("current")
_RbtwsApStatApStatusMacBaseMac_Type = MacAddress
_RbtwsApStatApStatusMacBaseMac_Object = MibTableColumn
rbtwsApStatApStatusMacBaseMac = _RbtwsApStatApStatusMacBaseMac_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 3, 1, 1),
    _RbtwsApStatApStatusMacBaseMac_Type()
)
rbtwsApStatApStatusMacBaseMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbtwsApStatApStatusMacBaseMac.setStatus("current")
_RbtwsApStatApStatusMacSerialNum_Type = RbtwsApSerialNum
_RbtwsApStatApStatusMacSerialNum_Object = MibTableColumn
rbtwsApStatApStatusMacSerialNum = _RbtwsApStatApStatusMacSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 3, 1, 2),
    _RbtwsApStatApStatusMacSerialNum_Type()
)
rbtwsApStatApStatusMacSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatApStatusMacSerialNum.setStatus("current")
_RbtwsApStatApStatusMacAttachType_Type = RbtwsApAttachType
_RbtwsApStatApStatusMacAttachType_Object = MibTableColumn
rbtwsApStatApStatusMacAttachType = _RbtwsApStatApStatusMacAttachType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 3, 1, 3),
    _RbtwsApStatApStatusMacAttachType_Type()
)
rbtwsApStatApStatusMacAttachType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatApStatusMacAttachType.setStatus("current")
_RbtwsApStatApStatusMacPortOrDapNum_Type = RbtwsApPortOrDapNum
_RbtwsApStatApStatusMacPortOrDapNum_Object = MibTableColumn
rbtwsApStatApStatusMacPortOrDapNum = _RbtwsApStatApStatusMacPortOrDapNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 3, 1, 4),
    _RbtwsApStatApStatusMacPortOrDapNum_Type()
)
rbtwsApStatApStatusMacPortOrDapNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatApStatusMacPortOrDapNum.setStatus("obsolete")
_RbtwsApStatApStatusMacApState_Type = RbtwsApState
_RbtwsApStatApStatusMacApState_Object = MibTableColumn
rbtwsApStatApStatusMacApState = _RbtwsApStatApStatusMacApState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 3, 1, 5),
    _RbtwsApStatApStatusMacApState_Type()
)
rbtwsApStatApStatusMacApState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatApStatusMacApState.setStatus("current")
_RbtwsApStatApStatusMacModel_Type = DisplayString
_RbtwsApStatApStatusMacModel_Object = MibTableColumn
rbtwsApStatApStatusMacModel = _RbtwsApStatApStatusMacModel_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 3, 1, 6),
    _RbtwsApStatApStatusMacModel_Type()
)
rbtwsApStatApStatusMacModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatApStatusMacModel.setStatus("current")
_RbtwsApStatApStatusMacFingerprint_Type = RbtwsApFingerprint
_RbtwsApStatApStatusMacFingerprint_Object = MibTableColumn
rbtwsApStatApStatusMacFingerprint = _RbtwsApStatApStatusMacFingerprint_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 3, 1, 7),
    _RbtwsApStatApStatusMacFingerprint_Type()
)
rbtwsApStatApStatusMacFingerprint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatApStatusMacFingerprint.setStatus("current")
_RbtwsApStatApStatusMacApName_Type = DisplayString
_RbtwsApStatApStatusMacApName_Object = MibTableColumn
rbtwsApStatApStatusMacApName = _RbtwsApStatApStatusMacApName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 3, 1, 8),
    _RbtwsApStatApStatusMacApName_Type()
)
rbtwsApStatApStatusMacApName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatApStatusMacApName.setStatus("current")
_RbtwsApStatApStatusMacVlan_Type = DisplayString
_RbtwsApStatApStatusMacVlan_Object = MibTableColumn
rbtwsApStatApStatusMacVlan = _RbtwsApStatApStatusMacVlan_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 3, 1, 9),
    _RbtwsApStatApStatusMacVlan_Type()
)
rbtwsApStatApStatusMacVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatApStatusMacVlan.setStatus("current")
_RbtwsApStatApStatusMacIpAddress_Type = IpAddress
_RbtwsApStatApStatusMacIpAddress_Object = MibTableColumn
rbtwsApStatApStatusMacIpAddress = _RbtwsApStatApStatusMacIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 3, 1, 10),
    _RbtwsApStatApStatusMacIpAddress_Type()
)
rbtwsApStatApStatusMacIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatApStatusMacIpAddress.setStatus("current")
_RbtwsApStatApStatusMacUptimeSecs_Type = Unsigned32
_RbtwsApStatApStatusMacUptimeSecs_Object = MibTableColumn
rbtwsApStatApStatusMacUptimeSecs = _RbtwsApStatApStatusMacUptimeSecs_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 3, 1, 11),
    _RbtwsApStatApStatusMacUptimeSecs_Type()
)
rbtwsApStatApStatusMacUptimeSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatApStatusMacUptimeSecs.setStatus("current")
_RbtwsApStatApStatusMacCpuInfo_Type = DisplayString
_RbtwsApStatApStatusMacCpuInfo_Object = MibTableColumn
rbtwsApStatApStatusMacCpuInfo = _RbtwsApStatApStatusMacCpuInfo_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 3, 1, 12),
    _RbtwsApStatApStatusMacCpuInfo_Type()
)
rbtwsApStatApStatusMacCpuInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatApStatusMacCpuInfo.setStatus("current")
_RbtwsApStatApStatusMacManufacturerId_Type = DisplayString
_RbtwsApStatApStatusMacManufacturerId_Object = MibTableColumn
rbtwsApStatApStatusMacManufacturerId = _RbtwsApStatApStatusMacManufacturerId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 3, 1, 13),
    _RbtwsApStatApStatusMacManufacturerId_Type()
)
rbtwsApStatApStatusMacManufacturerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatApStatusMacManufacturerId.setStatus("current")
_RbtwsApStatApStatusMacRamBytes_Type = Unsigned32
_RbtwsApStatApStatusMacRamBytes_Object = MibTableColumn
rbtwsApStatApStatusMacRamBytes = _RbtwsApStatApStatusMacRamBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 3, 1, 14),
    _RbtwsApStatApStatusMacRamBytes_Type()
)
rbtwsApStatApStatusMacRamBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatApStatusMacRamBytes.setStatus("current")
_RbtwsApStatApStatusMacHardwareRev_Type = DisplayString
_RbtwsApStatApStatusMacHardwareRev_Object = MibTableColumn
rbtwsApStatApStatusMacHardwareRev = _RbtwsApStatApStatusMacHardwareRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 3, 1, 15),
    _RbtwsApStatApStatusMacHardwareRev_Type()
)
rbtwsApStatApStatusMacHardwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatApStatusMacHardwareRev.setStatus("current")
_RbtwsApStatApStatusMacClientSessions_Type = Unsigned32
_RbtwsApStatApStatusMacClientSessions_Object = MibTableColumn
rbtwsApStatApStatusMacClientSessions = _RbtwsApStatApStatusMacClientSessions_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 3, 1, 16),
    _RbtwsApStatApStatusMacClientSessions_Type()
)
rbtwsApStatApStatusMacClientSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatApStatusMacClientSessions.setStatus("current")
_RbtwsApStatApStatusMacSoftwareVer_Type = DisplayString
_RbtwsApStatApStatusMacSoftwareVer_Object = MibTableColumn
rbtwsApStatApStatusMacSoftwareVer = _RbtwsApStatApStatusMacSoftwareVer_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 3, 1, 17),
    _RbtwsApStatApStatusMacSoftwareVer_Type()
)
rbtwsApStatApStatusMacSoftwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatApStatusMacSoftwareVer.setStatus("current")
_RbtwsApStatApStatusMacBootVer_Type = DisplayString
_RbtwsApStatApStatusMacBootVer_Object = MibTableColumn
rbtwsApStatApStatusMacBootVer = _RbtwsApStatApStatusMacBootVer_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 3, 1, 18),
    _RbtwsApStatApStatusMacBootVer_Type()
)
rbtwsApStatApStatusMacBootVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatApStatusMacBootVer.setStatus("current")
_RbtwsApStatApStatusMacApNum_Type = RbtwsApNum
_RbtwsApStatApStatusMacApNum_Object = MibTableColumn
rbtwsApStatApStatusMacApNum = _RbtwsApStatApStatusMacApNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 3, 1, 19),
    _RbtwsApStatApStatusMacApNum_Type()
)
rbtwsApStatApStatusMacApNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatApStatusMacApNum.setStatus("current")
_RbtwsApStatRadioStatusTable_Object = MibTable
rbtwsApStatRadioStatusTable = _RbtwsApStatRadioStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 4)
)
if mibBuilder.loadTexts:
    rbtwsApStatRadioStatusTable.setStatus("current")
_RbtwsApStatRadioStatusEntry_Object = MibTableRow
rbtwsApStatRadioStatusEntry = _RbtwsApStatRadioStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 4, 1)
)
rbtwsApStatRadioStatusEntry.setIndexNames(
    (0, "RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioStatusApSerialNum"),
    (0, "RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioStatusRadioNum"),
)
if mibBuilder.loadTexts:
    rbtwsApStatRadioStatusEntry.setStatus("current")
_RbtwsApStatRadioStatusApSerialNum_Type = RbtwsApSerialNum
_RbtwsApStatRadioStatusApSerialNum_Object = MibTableColumn
rbtwsApStatRadioStatusApSerialNum = _RbtwsApStatRadioStatusApSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 4, 1, 1),
    _RbtwsApStatRadioStatusApSerialNum_Type()
)
rbtwsApStatRadioStatusApSerialNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbtwsApStatRadioStatusApSerialNum.setStatus("current")
_RbtwsApStatRadioStatusRadioNum_Type = RbtwsRadioNum
_RbtwsApStatRadioStatusRadioNum_Object = MibTableColumn
rbtwsApStatRadioStatusRadioNum = _RbtwsApStatRadioStatusRadioNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 4, 1, 2),
    _RbtwsApStatRadioStatusRadioNum_Type()
)
rbtwsApStatRadioStatusRadioNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbtwsApStatRadioStatusRadioNum.setStatus("current")
_RbtwsApStatRadioStatusBaseMac_Type = MacAddress
_RbtwsApStatRadioStatusBaseMac_Object = MibTableColumn
rbtwsApStatRadioStatusBaseMac = _RbtwsApStatRadioStatusBaseMac_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 4, 1, 3),
    _RbtwsApStatRadioStatusBaseMac_Type()
)
rbtwsApStatRadioStatusBaseMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioStatusBaseMac.setStatus("current")
_RbtwsApStatRadioStatusEnable_Type = RbtwsRadioEnable
_RbtwsApStatRadioStatusEnable_Object = MibTableColumn
rbtwsApStatRadioStatusEnable = _RbtwsApStatRadioStatusEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 4, 1, 4),
    _RbtwsApStatRadioStatusEnable_Type()
)
rbtwsApStatRadioStatusEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioStatusEnable.setStatus("obsolete")
_RbtwsApStatRadioStatusRadioConfigState_Type = RbtwsRadioConfigState
_RbtwsApStatRadioStatusRadioConfigState_Object = MibTableColumn
rbtwsApStatRadioStatusRadioConfigState = _RbtwsApStatRadioStatusRadioConfigState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 4, 1, 5),
    _RbtwsApStatRadioStatusRadioConfigState_Type()
)
rbtwsApStatRadioStatusRadioConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioStatusRadioConfigState.setStatus("current")
_RbtwsApStatRadioStatusCurrentPowerLevel_Type = RbtwsPowerLevel
_RbtwsApStatRadioStatusCurrentPowerLevel_Object = MibTableColumn
rbtwsApStatRadioStatusCurrentPowerLevel = _RbtwsApStatRadioStatusCurrentPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 4, 1, 6),
    _RbtwsApStatRadioStatusCurrentPowerLevel_Type()
)
rbtwsApStatRadioStatusCurrentPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioStatusCurrentPowerLevel.setStatus("current")
_RbtwsApStatRadioStatusCurrentChannelNum_Type = RbtwsChannelNum
_RbtwsApStatRadioStatusCurrentChannelNum_Object = MibTableColumn
rbtwsApStatRadioStatusCurrentChannelNum = _RbtwsApStatRadioStatusCurrentChannelNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 4, 1, 7),
    _RbtwsApStatRadioStatusCurrentChannelNum_Type()
)
rbtwsApStatRadioStatusCurrentChannelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioStatusCurrentChannelNum.setStatus("current")
_RbtwsApStatRadioStatusClientSessions_Type = Unsigned32
_RbtwsApStatRadioStatusClientSessions_Object = MibTableColumn
rbtwsApStatRadioStatusClientSessions = _RbtwsApStatRadioStatusClientSessions_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 4, 1, 8),
    _RbtwsApStatRadioStatusClientSessions_Type()
)
rbtwsApStatRadioStatusClientSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioStatusClientSessions.setStatus("current")
_RbtwsApStatRadioStatusMaxPowerLevel_Type = RbtwsPowerLevel
_RbtwsApStatRadioStatusMaxPowerLevel_Object = MibTableColumn
rbtwsApStatRadioStatusMaxPowerLevel = _RbtwsApStatRadioStatusMaxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 4, 1, 9),
    _RbtwsApStatRadioStatusMaxPowerLevel_Type()
)
rbtwsApStatRadioStatusMaxPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioStatusMaxPowerLevel.setStatus("current")
_RbtwsApStatRadioStatusRadioPhyType_Type = RbtwsRadioType
_RbtwsApStatRadioStatusRadioPhyType_Object = MibTableColumn
rbtwsApStatRadioStatusRadioPhyType = _RbtwsApStatRadioStatusRadioPhyType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 4, 1, 10),
    _RbtwsApStatRadioStatusRadioPhyType_Type()
)
rbtwsApStatRadioStatusRadioPhyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioStatusRadioPhyType.setStatus("current")
_RbtwsApStatRadioStatusRadioMode_Type = RbtwsRadioMode
_RbtwsApStatRadioStatusRadioMode_Object = MibTableColumn
rbtwsApStatRadioStatusRadioMode = _RbtwsApStatRadioStatusRadioMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 4, 1, 11),
    _RbtwsApStatRadioStatusRadioMode_Type()
)
rbtwsApStatRadioStatusRadioMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioStatusRadioMode.setStatus("current")
_RbtwsApStatRadioStatusRadioChannelWidth_Type = RbtwsRadioChannelWidth
_RbtwsApStatRadioStatusRadioChannelWidth_Object = MibTableColumn
rbtwsApStatRadioStatusRadioChannelWidth = _RbtwsApStatRadioStatusRadioChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 4, 1, 12),
    _RbtwsApStatRadioStatusRadioChannelWidth_Type()
)
rbtwsApStatRadioStatusRadioChannelWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioStatusRadioChannelWidth.setStatus("current")
_RbtwsApStatRadioStatusRadioMimoState_Type = RbtwsRadioMimoState
_RbtwsApStatRadioStatusRadioMimoState_Object = MibTableColumn
rbtwsApStatRadioStatusRadioMimoState = _RbtwsApStatRadioStatusRadioMimoState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 4, 1, 13),
    _RbtwsApStatRadioStatusRadioMimoState_Type()
)
rbtwsApStatRadioStatusRadioMimoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioStatusRadioMimoState.setStatus("current")
_RbtwsApStatRadioStatusMacTable_Object = MibTable
rbtwsApStatRadioStatusMacTable = _RbtwsApStatRadioStatusMacTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 5)
)
if mibBuilder.loadTexts:
    rbtwsApStatRadioStatusMacTable.setStatus("current")
_RbtwsApStatRadioStatusMacEntry_Object = MibTableRow
rbtwsApStatRadioStatusMacEntry = _RbtwsApStatRadioStatusMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 5, 1)
)
rbtwsApStatRadioStatusMacEntry.setIndexNames(
    (0, "RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioStatusMacBaseMac"),
)
if mibBuilder.loadTexts:
    rbtwsApStatRadioStatusMacEntry.setStatus("current")
_RbtwsApStatRadioStatusMacBaseMac_Type = MacAddress
_RbtwsApStatRadioStatusMacBaseMac_Object = MibTableColumn
rbtwsApStatRadioStatusMacBaseMac = _RbtwsApStatRadioStatusMacBaseMac_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 5, 1, 1),
    _RbtwsApStatRadioStatusMacBaseMac_Type()
)
rbtwsApStatRadioStatusMacBaseMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbtwsApStatRadioStatusMacBaseMac.setStatus("current")
_RbtwsApStatRadioStatusMacApSerialNum_Type = RbtwsApSerialNum
_RbtwsApStatRadioStatusMacApSerialNum_Object = MibTableColumn
rbtwsApStatRadioStatusMacApSerialNum = _RbtwsApStatRadioStatusMacApSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 5, 1, 2),
    _RbtwsApStatRadioStatusMacApSerialNum_Type()
)
rbtwsApStatRadioStatusMacApSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioStatusMacApSerialNum.setStatus("current")
_RbtwsApStatRadioStatusMacRadioNum_Type = RbtwsRadioNum
_RbtwsApStatRadioStatusMacRadioNum_Object = MibTableColumn
rbtwsApStatRadioStatusMacRadioNum = _RbtwsApStatRadioStatusMacRadioNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 5, 1, 3),
    _RbtwsApStatRadioStatusMacRadioNum_Type()
)
rbtwsApStatRadioStatusMacRadioNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioStatusMacRadioNum.setStatus("current")
_RbtwsApStatRadioStatusMacEnable_Type = RbtwsRadioEnable
_RbtwsApStatRadioStatusMacEnable_Object = MibTableColumn
rbtwsApStatRadioStatusMacEnable = _RbtwsApStatRadioStatusMacEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 5, 1, 4),
    _RbtwsApStatRadioStatusMacEnable_Type()
)
rbtwsApStatRadioStatusMacEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioStatusMacEnable.setStatus("obsolete")
_RbtwsApStatRadioStatusMacRadioConfigState_Type = RbtwsRadioConfigState
_RbtwsApStatRadioStatusMacRadioConfigState_Object = MibTableColumn
rbtwsApStatRadioStatusMacRadioConfigState = _RbtwsApStatRadioStatusMacRadioConfigState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 5, 1, 5),
    _RbtwsApStatRadioStatusMacRadioConfigState_Type()
)
rbtwsApStatRadioStatusMacRadioConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioStatusMacRadioConfigState.setStatus("current")
_RbtwsApStatRadioStatusMacCurrentPowerLevel_Type = RbtwsPowerLevel
_RbtwsApStatRadioStatusMacCurrentPowerLevel_Object = MibTableColumn
rbtwsApStatRadioStatusMacCurrentPowerLevel = _RbtwsApStatRadioStatusMacCurrentPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 5, 1, 6),
    _RbtwsApStatRadioStatusMacCurrentPowerLevel_Type()
)
rbtwsApStatRadioStatusMacCurrentPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioStatusMacCurrentPowerLevel.setStatus("current")
_RbtwsApStatRadioStatusMacCurrentChannelNum_Type = RbtwsChannelNum
_RbtwsApStatRadioStatusMacCurrentChannelNum_Object = MibTableColumn
rbtwsApStatRadioStatusMacCurrentChannelNum = _RbtwsApStatRadioStatusMacCurrentChannelNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 5, 1, 7),
    _RbtwsApStatRadioStatusMacCurrentChannelNum_Type()
)
rbtwsApStatRadioStatusMacCurrentChannelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioStatusMacCurrentChannelNum.setStatus("current")
_RbtwsApStatRadioStatusMacClientSessions_Type = Unsigned32
_RbtwsApStatRadioStatusMacClientSessions_Object = MibTableColumn
rbtwsApStatRadioStatusMacClientSessions = _RbtwsApStatRadioStatusMacClientSessions_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 5, 1, 8),
    _RbtwsApStatRadioStatusMacClientSessions_Type()
)
rbtwsApStatRadioStatusMacClientSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioStatusMacClientSessions.setStatus("current")
_RbtwsApStatRadioStatusMacMaxPowerLevel_Type = RbtwsPowerLevel
_RbtwsApStatRadioStatusMacMaxPowerLevel_Object = MibTableColumn
rbtwsApStatRadioStatusMacMaxPowerLevel = _RbtwsApStatRadioStatusMacMaxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 5, 1, 9),
    _RbtwsApStatRadioStatusMacMaxPowerLevel_Type()
)
rbtwsApStatRadioStatusMacMaxPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioStatusMacMaxPowerLevel.setStatus("current")
_RbtwsApStatRadioStatusMacRadioPhyType_Type = RbtwsRadioType
_RbtwsApStatRadioStatusMacRadioPhyType_Object = MibTableColumn
rbtwsApStatRadioStatusMacRadioPhyType = _RbtwsApStatRadioStatusMacRadioPhyType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 5, 1, 10),
    _RbtwsApStatRadioStatusMacRadioPhyType_Type()
)
rbtwsApStatRadioStatusMacRadioPhyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioStatusMacRadioPhyType.setStatus("current")
_RbtwsApStatRadioStatusMacRadioMode_Type = RbtwsRadioMode
_RbtwsApStatRadioStatusMacRadioMode_Object = MibTableColumn
rbtwsApStatRadioStatusMacRadioMode = _RbtwsApStatRadioStatusMacRadioMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 5, 1, 11),
    _RbtwsApStatRadioStatusMacRadioMode_Type()
)
rbtwsApStatRadioStatusMacRadioMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioStatusMacRadioMode.setStatus("current")
_RbtwsApStatRadioStatusMacRadioChannelWidth_Type = RbtwsRadioChannelWidth
_RbtwsApStatRadioStatusMacRadioChannelWidth_Object = MibTableColumn
rbtwsApStatRadioStatusMacRadioChannelWidth = _RbtwsApStatRadioStatusMacRadioChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 5, 1, 12),
    _RbtwsApStatRadioStatusMacRadioChannelWidth_Type()
)
rbtwsApStatRadioStatusMacRadioChannelWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioStatusMacRadioChannelWidth.setStatus("current")
_RbtwsApStatRadioStatusMacRadioMimoState_Type = RbtwsRadioMimoState
_RbtwsApStatRadioStatusMacRadioMimoState_Object = MibTableColumn
rbtwsApStatRadioStatusMacRadioMimoState = _RbtwsApStatRadioStatusMacRadioMimoState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 5, 1, 13),
    _RbtwsApStatRadioStatusMacRadioMimoState_Type()
)
rbtwsApStatRadioStatusMacRadioMimoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioStatusMacRadioMimoState.setStatus("current")
_RbtwsApStatRadioServiceTable_Object = MibTable
rbtwsApStatRadioServiceTable = _RbtwsApStatRadioServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 6)
)
if mibBuilder.loadTexts:
    rbtwsApStatRadioServiceTable.setStatus("current")
_RbtwsApStatRadioServiceEntry_Object = MibTableRow
rbtwsApStatRadioServiceEntry = _RbtwsApStatRadioServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 6, 1)
)
rbtwsApStatRadioServiceEntry.setIndexNames(
    (0, "RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioServApSerialNum"),
    (0, "RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioServRadioNum"),
    (0, "RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioServSsid"),
)
if mibBuilder.loadTexts:
    rbtwsApStatRadioServiceEntry.setStatus("current")
_RbtwsApStatRadioServApSerialNum_Type = RbtwsApSerialNum
_RbtwsApStatRadioServApSerialNum_Object = MibTableColumn
rbtwsApStatRadioServApSerialNum = _RbtwsApStatRadioServApSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 6, 1, 1),
    _RbtwsApStatRadioServApSerialNum_Type()
)
rbtwsApStatRadioServApSerialNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbtwsApStatRadioServApSerialNum.setStatus("current")
_RbtwsApStatRadioServRadioNum_Type = RbtwsRadioNum
_RbtwsApStatRadioServRadioNum_Object = MibTableColumn
rbtwsApStatRadioServRadioNum = _RbtwsApStatRadioServRadioNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 6, 1, 2),
    _RbtwsApStatRadioServRadioNum_Type()
)
rbtwsApStatRadioServRadioNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbtwsApStatRadioServRadioNum.setStatus("current")


class _RbtwsApStatRadioServSsid_Type(DisplayString):
    """Custom type rbtwsApStatRadioServSsid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RbtwsApStatRadioServSsid_Type.__name__ = "DisplayString"
_RbtwsApStatRadioServSsid_Object = MibTableColumn
rbtwsApStatRadioServSsid = _RbtwsApStatRadioServSsid_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 6, 1, 3),
    _RbtwsApStatRadioServSsid_Type()
)
rbtwsApStatRadioServSsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbtwsApStatRadioServSsid.setStatus("current")
_RbtwsApStatRadioServBssid_Type = MacAddress
_RbtwsApStatRadioServBssid_Object = MibTableColumn
rbtwsApStatRadioServBssid = _RbtwsApStatRadioServBssid_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 6, 1, 4),
    _RbtwsApStatRadioServBssid_Type()
)
rbtwsApStatRadioServBssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioServBssid.setStatus("current")
_RbtwsApStatRadioServServiceProfileName_Type = DisplayString
_RbtwsApStatRadioServServiceProfileName_Object = MibTableColumn
rbtwsApStatRadioServServiceProfileName = _RbtwsApStatRadioServServiceProfileName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 6, 1, 5),
    _RbtwsApStatRadioServServiceProfileName_Type()
)
rbtwsApStatRadioServServiceProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioServServiceProfileName.setStatus("current")
_RbtwsApStatRadioServiceMacTable_Object = MibTable
rbtwsApStatRadioServiceMacTable = _RbtwsApStatRadioServiceMacTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 7)
)
if mibBuilder.loadTexts:
    rbtwsApStatRadioServiceMacTable.setStatus("current")
_RbtwsApStatRadioServiceMacEntry_Object = MibTableRow
rbtwsApStatRadioServiceMacEntry = _RbtwsApStatRadioServiceMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 7, 1)
)
rbtwsApStatRadioServiceMacEntry.setIndexNames(
    (0, "RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioServMacBssid"),
)
if mibBuilder.loadTexts:
    rbtwsApStatRadioServiceMacEntry.setStatus("current")
_RbtwsApStatRadioServMacBssid_Type = MacAddress
_RbtwsApStatRadioServMacBssid_Object = MibTableColumn
rbtwsApStatRadioServMacBssid = _RbtwsApStatRadioServMacBssid_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 7, 1, 1),
    _RbtwsApStatRadioServMacBssid_Type()
)
rbtwsApStatRadioServMacBssid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbtwsApStatRadioServMacBssid.setStatus("current")
_RbtwsApStatRadioServMacApSerialNum_Type = RbtwsApSerialNum
_RbtwsApStatRadioServMacApSerialNum_Object = MibTableColumn
rbtwsApStatRadioServMacApSerialNum = _RbtwsApStatRadioServMacApSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 7, 1, 2),
    _RbtwsApStatRadioServMacApSerialNum_Type()
)
rbtwsApStatRadioServMacApSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioServMacApSerialNum.setStatus("current")
_RbtwsApStatRadioServMacRadioNum_Type = RbtwsRadioNum
_RbtwsApStatRadioServMacRadioNum_Object = MibTableColumn
rbtwsApStatRadioServMacRadioNum = _RbtwsApStatRadioServMacRadioNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 7, 1, 3),
    _RbtwsApStatRadioServMacRadioNum_Type()
)
rbtwsApStatRadioServMacRadioNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioServMacRadioNum.setStatus("current")


class _RbtwsApStatRadioServMacSsid_Type(DisplayString):
    """Custom type rbtwsApStatRadioServMacSsid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RbtwsApStatRadioServMacSsid_Type.__name__ = "DisplayString"
_RbtwsApStatRadioServMacSsid_Object = MibTableColumn
rbtwsApStatRadioServMacSsid = _RbtwsApStatRadioServMacSsid_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 7, 1, 4),
    _RbtwsApStatRadioServMacSsid_Type()
)
rbtwsApStatRadioServMacSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioServMacSsid.setStatus("current")
_RbtwsApStatRadioServMacServiceProfileName_Type = DisplayString
_RbtwsApStatRadioServMacServiceProfileName_Object = MibTableColumn
rbtwsApStatRadioServMacServiceProfileName = _RbtwsApStatRadioServMacServiceProfileName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 7, 1, 5),
    _RbtwsApStatRadioServMacServiceProfileName_Type()
)
rbtwsApStatRadioServMacServiceProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioServMacServiceProfileName.setStatus("current")
_RbtwsApStatRadioServiceOpRateSetTable_Object = MibTable
rbtwsApStatRadioServiceOpRateSetTable = _RbtwsApStatRadioServiceOpRateSetTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 8)
)
if mibBuilder.loadTexts:
    rbtwsApStatRadioServiceOpRateSetTable.setStatus("current")
_RbtwsApStatRadioServiceOpRateSetEntry_Object = MibTableRow
rbtwsApStatRadioServiceOpRateSetEntry = _RbtwsApStatRadioServiceOpRateSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 8, 1)
)
rbtwsApStatRadioServiceOpRateSetEntry.setIndexNames(
    (0, "RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioSORSetApSerialNum"),
    (0, "RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioSORSetRadioNum"),
    (0, "RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioSORSetSsid"),
)
if mibBuilder.loadTexts:
    rbtwsApStatRadioServiceOpRateSetEntry.setStatus("current")
_RbtwsApStatRadioSORSetApSerialNum_Type = RbtwsApSerialNum
_RbtwsApStatRadioSORSetApSerialNum_Object = MibTableColumn
rbtwsApStatRadioSORSetApSerialNum = _RbtwsApStatRadioSORSetApSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 8, 1, 1),
    _RbtwsApStatRadioSORSetApSerialNum_Type()
)
rbtwsApStatRadioSORSetApSerialNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbtwsApStatRadioSORSetApSerialNum.setStatus("current")
_RbtwsApStatRadioSORSetRadioNum_Type = RbtwsRadioNum
_RbtwsApStatRadioSORSetRadioNum_Object = MibTableColumn
rbtwsApStatRadioSORSetRadioNum = _RbtwsApStatRadioSORSetRadioNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 8, 1, 2),
    _RbtwsApStatRadioSORSetRadioNum_Type()
)
rbtwsApStatRadioSORSetRadioNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbtwsApStatRadioSORSetRadioNum.setStatus("current")


class _RbtwsApStatRadioSORSetSsid_Type(DisplayString):
    """Custom type rbtwsApStatRadioSORSetSsid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RbtwsApStatRadioSORSetSsid_Type.__name__ = "DisplayString"
_RbtwsApStatRadioSORSetSsid_Object = MibTableColumn
rbtwsApStatRadioSORSetSsid = _RbtwsApStatRadioSORSetSsid_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 8, 1, 3),
    _RbtwsApStatRadioSORSetSsid_Type()
)
rbtwsApStatRadioSORSetSsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbtwsApStatRadioSORSetSsid.setStatus("current")
_RbtwsApStatRadioSORSetMandatory_Type = RbtwsRadioOpRateSetMandatory
_RbtwsApStatRadioSORSetMandatory_Object = MibTableColumn
rbtwsApStatRadioSORSetMandatory = _RbtwsApStatRadioSORSetMandatory_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 8, 1, 4),
    _RbtwsApStatRadioSORSetMandatory_Type()
)
rbtwsApStatRadioSORSetMandatory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioSORSetMandatory.setStatus("current")
_RbtwsApStatRadioSORSetDisabled_Type = RbtwsRadioOpRateSetDisabled
_RbtwsApStatRadioSORSetDisabled_Object = MibTableColumn
rbtwsApStatRadioSORSetDisabled = _RbtwsApStatRadioSORSetDisabled_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 8, 1, 5),
    _RbtwsApStatRadioSORSetDisabled_Type()
)
rbtwsApStatRadioSORSetDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioSORSetDisabled.setStatus("current")
_RbtwsApStatRadioSORSetBeacon_Type = RbtwsRadioOpRateSetSingleValue
_RbtwsApStatRadioSORSetBeacon_Object = MibTableColumn
rbtwsApStatRadioSORSetBeacon = _RbtwsApStatRadioSORSetBeacon_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 8, 1, 6),
    _RbtwsApStatRadioSORSetBeacon_Type()
)
rbtwsApStatRadioSORSetBeacon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioSORSetBeacon.setStatus("current")
_RbtwsApStatRadioSORSetMulticast_Type = RbtwsRadioOpRateSetSingleValue
_RbtwsApStatRadioSORSetMulticast_Object = MibTableColumn
rbtwsApStatRadioSORSetMulticast = _RbtwsApStatRadioSORSetMulticast_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 8, 1, 7),
    _RbtwsApStatRadioSORSetMulticast_Type()
)
rbtwsApStatRadioSORSetMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioSORSetMulticast.setStatus("current")
_RbtwsApStatRadioServiceOpRateSetMacTable_Object = MibTable
rbtwsApStatRadioServiceOpRateSetMacTable = _RbtwsApStatRadioServiceOpRateSetMacTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 9)
)
if mibBuilder.loadTexts:
    rbtwsApStatRadioServiceOpRateSetMacTable.setStatus("current")
_RbtwsApStatRadioServiceOpRateSetMacEntry_Object = MibTableRow
rbtwsApStatRadioServiceOpRateSetMacEntry = _RbtwsApStatRadioServiceOpRateSetMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 9, 1)
)
rbtwsApStatRadioServiceOpRateSetMacEntry.setIndexNames(
    (0, "RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioSORSetMacBssid"),
)
if mibBuilder.loadTexts:
    rbtwsApStatRadioServiceOpRateSetMacEntry.setStatus("current")
_RbtwsApStatRadioSORSetMacBssid_Type = MacAddress
_RbtwsApStatRadioSORSetMacBssid_Object = MibTableColumn
rbtwsApStatRadioSORSetMacBssid = _RbtwsApStatRadioSORSetMacBssid_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 9, 1, 1),
    _RbtwsApStatRadioSORSetMacBssid_Type()
)
rbtwsApStatRadioSORSetMacBssid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbtwsApStatRadioSORSetMacBssid.setStatus("current")
_RbtwsApStatRadioSORSetMacMandatory_Type = RbtwsRadioOpRateSetMandatory
_RbtwsApStatRadioSORSetMacMandatory_Object = MibTableColumn
rbtwsApStatRadioSORSetMacMandatory = _RbtwsApStatRadioSORSetMacMandatory_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 9, 1, 2),
    _RbtwsApStatRadioSORSetMacMandatory_Type()
)
rbtwsApStatRadioSORSetMacMandatory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioSORSetMacMandatory.setStatus("current")
_RbtwsApStatRadioSORSetMacDisabled_Type = RbtwsRadioOpRateSetDisabled
_RbtwsApStatRadioSORSetMacDisabled_Object = MibTableColumn
rbtwsApStatRadioSORSetMacDisabled = _RbtwsApStatRadioSORSetMacDisabled_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 9, 1, 3),
    _RbtwsApStatRadioSORSetMacDisabled_Type()
)
rbtwsApStatRadioSORSetMacDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioSORSetMacDisabled.setStatus("current")
_RbtwsApStatRadioSORSetMacBeacon_Type = RbtwsRadioOpRateSetSingleValue
_RbtwsApStatRadioSORSetMacBeacon_Object = MibTableColumn
rbtwsApStatRadioSORSetMacBeacon = _RbtwsApStatRadioSORSetMacBeacon_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 9, 1, 4),
    _RbtwsApStatRadioSORSetMacBeacon_Type()
)
rbtwsApStatRadioSORSetMacBeacon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioSORSetMacBeacon.setStatus("current")
_RbtwsApStatRadioSORSetMacMulticast_Type = RbtwsRadioOpRateSetSingleValue
_RbtwsApStatRadioSORSetMacMulticast_Object = MibTableColumn
rbtwsApStatRadioSORSetMacMulticast = _RbtwsApStatRadioSORSetMacMulticast_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 9, 1, 5),
    _RbtwsApStatRadioSORSetMacMulticast_Type()
)
rbtwsApStatRadioSORSetMacMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioSORSetMacMulticast.setStatus("current")
_RbtwsApStatRadioOpStatisticsTable_Object = MibTable
rbtwsApStatRadioOpStatisticsTable = _RbtwsApStatRadioOpStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 10)
)
if mibBuilder.loadTexts:
    rbtwsApStatRadioOpStatisticsTable.setStatus("current")
_RbtwsApStatRadioOpStatisticsEntry_Object = MibTableRow
rbtwsApStatRadioOpStatisticsEntry = _RbtwsApStatRadioOpStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 10, 1)
)
rbtwsApStatRadioOpStatisticsEntry.setIndexNames(
    (0, "RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioOpStatsApSerialNum"),
    (0, "RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioOpStatsRadioNum"),
)
if mibBuilder.loadTexts:
    rbtwsApStatRadioOpStatisticsEntry.setStatus("current")
_RbtwsApStatRadioOpStatsApSerialNum_Type = RbtwsApSerialNum
_RbtwsApStatRadioOpStatsApSerialNum_Object = MibTableColumn
rbtwsApStatRadioOpStatsApSerialNum = _RbtwsApStatRadioOpStatsApSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 10, 1, 1),
    _RbtwsApStatRadioOpStatsApSerialNum_Type()
)
rbtwsApStatRadioOpStatsApSerialNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbtwsApStatRadioOpStatsApSerialNum.setStatus("current")
_RbtwsApStatRadioOpStatsRadioNum_Type = RbtwsRadioNum
_RbtwsApStatRadioOpStatsRadioNum_Object = MibTableColumn
rbtwsApStatRadioOpStatsRadioNum = _RbtwsApStatRadioOpStatsRadioNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 10, 1, 2),
    _RbtwsApStatRadioOpStatsRadioNum_Type()
)
rbtwsApStatRadioOpStatsRadioNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbtwsApStatRadioOpStatsRadioNum.setStatus("current")
_RbtwsApStatRadioOpStatsTxUniPkt_Type = Counter64
_RbtwsApStatRadioOpStatsTxUniPkt_Object = MibTableColumn
rbtwsApStatRadioOpStatsTxUniPkt = _RbtwsApStatRadioOpStatsTxUniPkt_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 10, 1, 3),
    _RbtwsApStatRadioOpStatsTxUniPkt_Type()
)
rbtwsApStatRadioOpStatsTxUniPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioOpStatsTxUniPkt.setStatus("current")
_RbtwsApStatRadioOpStatsTxUniOctet_Type = Counter64
_RbtwsApStatRadioOpStatsTxUniOctet_Object = MibTableColumn
rbtwsApStatRadioOpStatsTxUniOctet = _RbtwsApStatRadioOpStatsTxUniOctet_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 10, 1, 4),
    _RbtwsApStatRadioOpStatsTxUniOctet_Type()
)
rbtwsApStatRadioOpStatsTxUniOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioOpStatsTxUniOctet.setStatus("current")
_RbtwsApStatRadioOpStatsTxMultiPkt_Type = Counter64
_RbtwsApStatRadioOpStatsTxMultiPkt_Object = MibTableColumn
rbtwsApStatRadioOpStatsTxMultiPkt = _RbtwsApStatRadioOpStatsTxMultiPkt_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 10, 1, 5),
    _RbtwsApStatRadioOpStatsTxMultiPkt_Type()
)
rbtwsApStatRadioOpStatsTxMultiPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioOpStatsTxMultiPkt.setStatus("current")
_RbtwsApStatRadioOpStatsTxMultiOctet_Type = Counter64
_RbtwsApStatRadioOpStatsTxMultiOctet_Object = MibTableColumn
rbtwsApStatRadioOpStatsTxMultiOctet = _RbtwsApStatRadioOpStatsTxMultiOctet_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 10, 1, 6),
    _RbtwsApStatRadioOpStatsTxMultiOctet_Type()
)
rbtwsApStatRadioOpStatsTxMultiOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioOpStatsTxMultiOctet.setStatus("current")
_RbtwsApStatRadioOpStatsRxPkt_Type = Counter64
_RbtwsApStatRadioOpStatsRxPkt_Object = MibTableColumn
rbtwsApStatRadioOpStatsRxPkt = _RbtwsApStatRadioOpStatsRxPkt_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 10, 1, 7),
    _RbtwsApStatRadioOpStatsRxPkt_Type()
)
rbtwsApStatRadioOpStatsRxPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioOpStatsRxPkt.setStatus("current")
_RbtwsApStatRadioOpStatsRxOctet_Type = Counter64
_RbtwsApStatRadioOpStatsRxOctet_Object = MibTableColumn
rbtwsApStatRadioOpStatsRxOctet = _RbtwsApStatRadioOpStatsRxOctet_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 10, 1, 8),
    _RbtwsApStatRadioOpStatsRxOctet_Type()
)
rbtwsApStatRadioOpStatsRxOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioOpStatsRxOctet.setStatus("current")
_RbtwsApStatRadioOpStatsUndcrptPkt_Type = Counter64
_RbtwsApStatRadioOpStatsUndcrptPkt_Object = MibTableColumn
rbtwsApStatRadioOpStatsUndcrptPkt = _RbtwsApStatRadioOpStatsUndcrptPkt_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 10, 1, 9),
    _RbtwsApStatRadioOpStatsUndcrptPkt_Type()
)
rbtwsApStatRadioOpStatsUndcrptPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioOpStatsUndcrptPkt.setStatus("current")
_RbtwsApStatRadioOpStatsUndcrptOctet_Type = Counter64
_RbtwsApStatRadioOpStatsUndcrptOctet_Object = MibTableColumn
rbtwsApStatRadioOpStatsUndcrptOctet = _RbtwsApStatRadioOpStatsUndcrptOctet_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 10, 1, 10),
    _RbtwsApStatRadioOpStatsUndcrptOctet_Type()
)
rbtwsApStatRadioOpStatsUndcrptOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioOpStatsUndcrptOctet.setStatus("current")
_RbtwsApStatRadioOpStatsPhyErr_Type = Counter64
_RbtwsApStatRadioOpStatsPhyErr_Object = MibTableColumn
rbtwsApStatRadioOpStatsPhyErr = _RbtwsApStatRadioOpStatsPhyErr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 10, 1, 11),
    _RbtwsApStatRadioOpStatsPhyErr_Type()
)
rbtwsApStatRadioOpStatsPhyErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioOpStatsPhyErr.setStatus("current")
_RbtwsApStatRadioOpStatsResetCount_Type = Counter32
_RbtwsApStatRadioOpStatsResetCount_Object = MibTableColumn
rbtwsApStatRadioOpStatsResetCount = _RbtwsApStatRadioOpStatsResetCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 10, 1, 12),
    _RbtwsApStatRadioOpStatsResetCount_Type()
)
rbtwsApStatRadioOpStatsResetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioOpStatsResetCount.setStatus("current")
_RbtwsApStatRadioOpStatsAutoTuneChannelChangeCount_Type = Counter32
_RbtwsApStatRadioOpStatsAutoTuneChannelChangeCount_Object = MibTableColumn
rbtwsApStatRadioOpStatsAutoTuneChannelChangeCount = _RbtwsApStatRadioOpStatsAutoTuneChannelChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 10, 1, 13),
    _RbtwsApStatRadioOpStatsAutoTuneChannelChangeCount_Type()
)
rbtwsApStatRadioOpStatsAutoTuneChannelChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioOpStatsAutoTuneChannelChangeCount.setStatus("current")
_RbtwsApStatRadioOpStatsTxRetriesCount_Type = Counter32
_RbtwsApStatRadioOpStatsTxRetriesCount_Object = MibTableColumn
rbtwsApStatRadioOpStatsTxRetriesCount = _RbtwsApStatRadioOpStatsTxRetriesCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 10, 1, 14),
    _RbtwsApStatRadioOpStatsTxRetriesCount_Type()
)
rbtwsApStatRadioOpStatsTxRetriesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioOpStatsTxRetriesCount.setStatus("current")
_RbtwsApStatRadioOpStatsUserSessions_Type = Gauge32
_RbtwsApStatRadioOpStatsUserSessions_Object = MibTableColumn
rbtwsApStatRadioOpStatsUserSessions = _RbtwsApStatRadioOpStatsUserSessions_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 10, 1, 15),
    _RbtwsApStatRadioOpStatsUserSessions_Type()
)
rbtwsApStatRadioOpStatsUserSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioOpStatsUserSessions.setStatus("current")
_RbtwsApStatRadioOpStatsNoiseFloor_Type = Integer32
_RbtwsApStatRadioOpStatsNoiseFloor_Object = MibTableColumn
rbtwsApStatRadioOpStatsNoiseFloor = _RbtwsApStatRadioOpStatsNoiseFloor_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 10, 1, 16),
    _RbtwsApStatRadioOpStatsNoiseFloor_Type()
)
rbtwsApStatRadioOpStatsNoiseFloor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioOpStatsNoiseFloor.setStatus("current")
_RbtwsApStatRadioOpStatisticsMacTable_Object = MibTable
rbtwsApStatRadioOpStatisticsMacTable = _RbtwsApStatRadioOpStatisticsMacTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 11)
)
if mibBuilder.loadTexts:
    rbtwsApStatRadioOpStatisticsMacTable.setStatus("current")
_RbtwsApStatRadioOpStatisticsMacEntry_Object = MibTableRow
rbtwsApStatRadioOpStatisticsMacEntry = _RbtwsApStatRadioOpStatisticsMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 11, 1)
)
rbtwsApStatRadioOpStatisticsMacEntry.setIndexNames(
    (0, "RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioOpStatsMacBaseMac"),
)
if mibBuilder.loadTexts:
    rbtwsApStatRadioOpStatisticsMacEntry.setStatus("current")
_RbtwsApStatRadioOpStatsMacBaseMac_Type = MacAddress
_RbtwsApStatRadioOpStatsMacBaseMac_Object = MibTableColumn
rbtwsApStatRadioOpStatsMacBaseMac = _RbtwsApStatRadioOpStatsMacBaseMac_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 11, 1, 1),
    _RbtwsApStatRadioOpStatsMacBaseMac_Type()
)
rbtwsApStatRadioOpStatsMacBaseMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbtwsApStatRadioOpStatsMacBaseMac.setStatus("current")
_RbtwsApStatRadioOpStatsMacTxUniPkt_Type = Counter64
_RbtwsApStatRadioOpStatsMacTxUniPkt_Object = MibTableColumn
rbtwsApStatRadioOpStatsMacTxUniPkt = _RbtwsApStatRadioOpStatsMacTxUniPkt_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 11, 1, 2),
    _RbtwsApStatRadioOpStatsMacTxUniPkt_Type()
)
rbtwsApStatRadioOpStatsMacTxUniPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioOpStatsMacTxUniPkt.setStatus("current")
_RbtwsApStatRadioOpStatsMacTxUniOctet_Type = Counter64
_RbtwsApStatRadioOpStatsMacTxUniOctet_Object = MibTableColumn
rbtwsApStatRadioOpStatsMacTxUniOctet = _RbtwsApStatRadioOpStatsMacTxUniOctet_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 11, 1, 3),
    _RbtwsApStatRadioOpStatsMacTxUniOctet_Type()
)
rbtwsApStatRadioOpStatsMacTxUniOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioOpStatsMacTxUniOctet.setStatus("current")
_RbtwsApStatRadioOpStatsMacTxMultiPkt_Type = Counter64
_RbtwsApStatRadioOpStatsMacTxMultiPkt_Object = MibTableColumn
rbtwsApStatRadioOpStatsMacTxMultiPkt = _RbtwsApStatRadioOpStatsMacTxMultiPkt_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 11, 1, 4),
    _RbtwsApStatRadioOpStatsMacTxMultiPkt_Type()
)
rbtwsApStatRadioOpStatsMacTxMultiPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioOpStatsMacTxMultiPkt.setStatus("current")
_RbtwsApStatRadioOpStatsMacTxMultiOctet_Type = Counter64
_RbtwsApStatRadioOpStatsMacTxMultiOctet_Object = MibTableColumn
rbtwsApStatRadioOpStatsMacTxMultiOctet = _RbtwsApStatRadioOpStatsMacTxMultiOctet_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 11, 1, 5),
    _RbtwsApStatRadioOpStatsMacTxMultiOctet_Type()
)
rbtwsApStatRadioOpStatsMacTxMultiOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioOpStatsMacTxMultiOctet.setStatus("current")
_RbtwsApStatRadioOpStatsMacRxPkt_Type = Counter64
_RbtwsApStatRadioOpStatsMacRxPkt_Object = MibTableColumn
rbtwsApStatRadioOpStatsMacRxPkt = _RbtwsApStatRadioOpStatsMacRxPkt_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 11, 1, 6),
    _RbtwsApStatRadioOpStatsMacRxPkt_Type()
)
rbtwsApStatRadioOpStatsMacRxPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioOpStatsMacRxPkt.setStatus("current")
_RbtwsApStatRadioOpStatsMacRxOctet_Type = Counter64
_RbtwsApStatRadioOpStatsMacRxOctet_Object = MibTableColumn
rbtwsApStatRadioOpStatsMacRxOctet = _RbtwsApStatRadioOpStatsMacRxOctet_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 11, 1, 7),
    _RbtwsApStatRadioOpStatsMacRxOctet_Type()
)
rbtwsApStatRadioOpStatsMacRxOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioOpStatsMacRxOctet.setStatus("current")
_RbtwsApStatRadioOpStatsMacUndcrptPkt_Type = Counter64
_RbtwsApStatRadioOpStatsMacUndcrptPkt_Object = MibTableColumn
rbtwsApStatRadioOpStatsMacUndcrptPkt = _RbtwsApStatRadioOpStatsMacUndcrptPkt_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 11, 1, 8),
    _RbtwsApStatRadioOpStatsMacUndcrptPkt_Type()
)
rbtwsApStatRadioOpStatsMacUndcrptPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioOpStatsMacUndcrptPkt.setStatus("current")
_RbtwsApStatRadioOpStatsMacUndcrptOctet_Type = Counter64
_RbtwsApStatRadioOpStatsMacUndcrptOctet_Object = MibTableColumn
rbtwsApStatRadioOpStatsMacUndcrptOctet = _RbtwsApStatRadioOpStatsMacUndcrptOctet_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 11, 1, 9),
    _RbtwsApStatRadioOpStatsMacUndcrptOctet_Type()
)
rbtwsApStatRadioOpStatsMacUndcrptOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioOpStatsMacUndcrptOctet.setStatus("current")
_RbtwsApStatRadioOpStatsMacPhyErr_Type = Counter64
_RbtwsApStatRadioOpStatsMacPhyErr_Object = MibTableColumn
rbtwsApStatRadioOpStatsMacPhyErr = _RbtwsApStatRadioOpStatsMacPhyErr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 11, 1, 10),
    _RbtwsApStatRadioOpStatsMacPhyErr_Type()
)
rbtwsApStatRadioOpStatsMacPhyErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioOpStatsMacPhyErr.setStatus("current")
_RbtwsApStatRadioOpStatsMacResetCount_Type = Counter32
_RbtwsApStatRadioOpStatsMacResetCount_Object = MibTableColumn
rbtwsApStatRadioOpStatsMacResetCount = _RbtwsApStatRadioOpStatsMacResetCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 11, 1, 11),
    _RbtwsApStatRadioOpStatsMacResetCount_Type()
)
rbtwsApStatRadioOpStatsMacResetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioOpStatsMacResetCount.setStatus("current")
_RbtwsApStatRadioOpStatsMacAutoTuneChannelChangeCount_Type = Counter32
_RbtwsApStatRadioOpStatsMacAutoTuneChannelChangeCount_Object = MibTableColumn
rbtwsApStatRadioOpStatsMacAutoTuneChannelChangeCount = _RbtwsApStatRadioOpStatsMacAutoTuneChannelChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 11, 1, 12),
    _RbtwsApStatRadioOpStatsMacAutoTuneChannelChangeCount_Type()
)
rbtwsApStatRadioOpStatsMacAutoTuneChannelChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioOpStatsMacAutoTuneChannelChangeCount.setStatus("current")
_RbtwsApStatRadioOpStatsMacTxRetriesCount_Type = Counter32
_RbtwsApStatRadioOpStatsMacTxRetriesCount_Object = MibTableColumn
rbtwsApStatRadioOpStatsMacTxRetriesCount = _RbtwsApStatRadioOpStatsMacTxRetriesCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 11, 1, 13),
    _RbtwsApStatRadioOpStatsMacTxRetriesCount_Type()
)
rbtwsApStatRadioOpStatsMacTxRetriesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioOpStatsMacTxRetriesCount.setStatus("current")
_RbtwsApStatRadioOpStatsMacUserSessions_Type = Gauge32
_RbtwsApStatRadioOpStatsMacUserSessions_Object = MibTableColumn
rbtwsApStatRadioOpStatsMacUserSessions = _RbtwsApStatRadioOpStatsMacUserSessions_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 11, 1, 14),
    _RbtwsApStatRadioOpStatsMacUserSessions_Type()
)
rbtwsApStatRadioOpStatsMacUserSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioOpStatsMacUserSessions.setStatus("current")
_RbtwsApStatRadioOpStatsMacNoiseFloor_Type = Integer32
_RbtwsApStatRadioOpStatsMacNoiseFloor_Object = MibTableColumn
rbtwsApStatRadioOpStatsMacNoiseFloor = _RbtwsApStatRadioOpStatsMacNoiseFloor_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 11, 1, 15),
    _RbtwsApStatRadioOpStatsMacNoiseFloor_Type()
)
rbtwsApStatRadioOpStatsMacNoiseFloor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioOpStatsMacNoiseFloor.setStatus("current")
_RbtwsApStatRadioRateOpStatisticsTable_Object = MibTable
rbtwsApStatRadioRateOpStatisticsTable = _RbtwsApStatRadioRateOpStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 12)
)
if mibBuilder.loadTexts:
    rbtwsApStatRadioRateOpStatisticsTable.setStatus("current")
_RbtwsApStatRadioRateOpStatisticsEntry_Object = MibTableRow
rbtwsApStatRadioRateOpStatisticsEntry = _RbtwsApStatRadioRateOpStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 12, 1)
)
rbtwsApStatRadioRateOpStatisticsEntry.setIndexNames(
    (0, "RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioRateOpStatsApSerialNum"),
    (0, "RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioRateOpStatsRadioNum"),
    (0, "RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioRateOpStatsRate"),
)
if mibBuilder.loadTexts:
    rbtwsApStatRadioRateOpStatisticsEntry.setStatus("current")
_RbtwsApStatRadioRateOpStatsApSerialNum_Type = RbtwsApSerialNum
_RbtwsApStatRadioRateOpStatsApSerialNum_Object = MibTableColumn
rbtwsApStatRadioRateOpStatsApSerialNum = _RbtwsApStatRadioRateOpStatsApSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 12, 1, 1),
    _RbtwsApStatRadioRateOpStatsApSerialNum_Type()
)
rbtwsApStatRadioRateOpStatsApSerialNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbtwsApStatRadioRateOpStatsApSerialNum.setStatus("current")
_RbtwsApStatRadioRateOpStatsRadioNum_Type = RbtwsRadioNum
_RbtwsApStatRadioRateOpStatsRadioNum_Object = MibTableColumn
rbtwsApStatRadioRateOpStatsRadioNum = _RbtwsApStatRadioRateOpStatsRadioNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 12, 1, 2),
    _RbtwsApStatRadioRateOpStatsRadioNum_Type()
)
rbtwsApStatRadioRateOpStatsRadioNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbtwsApStatRadioRateOpStatsRadioNum.setStatus("current")
_RbtwsApStatRadioRateOpStatsRate_Type = RbtwsRadioRate
_RbtwsApStatRadioRateOpStatsRate_Object = MibTableColumn
rbtwsApStatRadioRateOpStatsRate = _RbtwsApStatRadioRateOpStatsRate_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 12, 1, 3),
    _RbtwsApStatRadioRateOpStatsRate_Type()
)
rbtwsApStatRadioRateOpStatsRate.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbtwsApStatRadioRateOpStatsRate.setStatus("current")
_RbtwsApStatRadioRateOpStatsTxUniPkt_Type = Counter64
_RbtwsApStatRadioRateOpStatsTxUniPkt_Object = MibTableColumn
rbtwsApStatRadioRateOpStatsTxUniPkt = _RbtwsApStatRadioRateOpStatsTxUniPkt_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 12, 1, 4),
    _RbtwsApStatRadioRateOpStatsTxUniPkt_Type()
)
rbtwsApStatRadioRateOpStatsTxUniPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioRateOpStatsTxUniPkt.setStatus("current")
_RbtwsApStatRadioRateOpStatsTxUniOctet_Type = Counter64
_RbtwsApStatRadioRateOpStatsTxUniOctet_Object = MibTableColumn
rbtwsApStatRadioRateOpStatsTxUniOctet = _RbtwsApStatRadioRateOpStatsTxUniOctet_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 12, 1, 5),
    _RbtwsApStatRadioRateOpStatsTxUniOctet_Type()
)
rbtwsApStatRadioRateOpStatsTxUniOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioRateOpStatsTxUniOctet.setStatus("current")
_RbtwsApStatRadioRateOpStatsTxMultiPkt_Type = Counter64
_RbtwsApStatRadioRateOpStatsTxMultiPkt_Object = MibTableColumn
rbtwsApStatRadioRateOpStatsTxMultiPkt = _RbtwsApStatRadioRateOpStatsTxMultiPkt_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 12, 1, 6),
    _RbtwsApStatRadioRateOpStatsTxMultiPkt_Type()
)
rbtwsApStatRadioRateOpStatsTxMultiPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioRateOpStatsTxMultiPkt.setStatus("current")
_RbtwsApStatRadioRateOpStatsTxMultiOctet_Type = Counter64
_RbtwsApStatRadioRateOpStatsTxMultiOctet_Object = MibTableColumn
rbtwsApStatRadioRateOpStatsTxMultiOctet = _RbtwsApStatRadioRateOpStatsTxMultiOctet_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 12, 1, 7),
    _RbtwsApStatRadioRateOpStatsTxMultiOctet_Type()
)
rbtwsApStatRadioRateOpStatsTxMultiOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioRateOpStatsTxMultiOctet.setStatus("current")
_RbtwsApStatRadioRateOpStatsRxPkt_Type = Counter64
_RbtwsApStatRadioRateOpStatsRxPkt_Object = MibTableColumn
rbtwsApStatRadioRateOpStatsRxPkt = _RbtwsApStatRadioRateOpStatsRxPkt_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 12, 1, 8),
    _RbtwsApStatRadioRateOpStatsRxPkt_Type()
)
rbtwsApStatRadioRateOpStatsRxPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioRateOpStatsRxPkt.setStatus("current")
_RbtwsApStatRadioRateOpStatsRxOctet_Type = Counter64
_RbtwsApStatRadioRateOpStatsRxOctet_Object = MibTableColumn
rbtwsApStatRadioRateOpStatsRxOctet = _RbtwsApStatRadioRateOpStatsRxOctet_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 12, 1, 9),
    _RbtwsApStatRadioRateOpStatsRxOctet_Type()
)
rbtwsApStatRadioRateOpStatsRxOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioRateOpStatsRxOctet.setStatus("current")
_RbtwsApStatRadioRateOpStatsUndcrptPkt_Type = Counter64
_RbtwsApStatRadioRateOpStatsUndcrptPkt_Object = MibTableColumn
rbtwsApStatRadioRateOpStatsUndcrptPkt = _RbtwsApStatRadioRateOpStatsUndcrptPkt_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 12, 1, 10),
    _RbtwsApStatRadioRateOpStatsUndcrptPkt_Type()
)
rbtwsApStatRadioRateOpStatsUndcrptPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioRateOpStatsUndcrptPkt.setStatus("current")
_RbtwsApStatRadioRateOpStatsUndcrptOctet_Type = Counter64
_RbtwsApStatRadioRateOpStatsUndcrptOctet_Object = MibTableColumn
rbtwsApStatRadioRateOpStatsUndcrptOctet = _RbtwsApStatRadioRateOpStatsUndcrptOctet_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 12, 1, 11),
    _RbtwsApStatRadioRateOpStatsUndcrptOctet_Type()
)
rbtwsApStatRadioRateOpStatsUndcrptOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioRateOpStatsUndcrptOctet.setStatus("current")
_RbtwsApStatRadioRateOpStatsPhyErr_Type = Counter64
_RbtwsApStatRadioRateOpStatsPhyErr_Object = MibTableColumn
rbtwsApStatRadioRateOpStatsPhyErr = _RbtwsApStatRadioRateOpStatsPhyErr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 12, 1, 12),
    _RbtwsApStatRadioRateOpStatsPhyErr_Type()
)
rbtwsApStatRadioRateOpStatsPhyErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioRateOpStatsPhyErr.setStatus("current")
_RbtwsApStatRadioRateOpStatisticsMacTable_Object = MibTable
rbtwsApStatRadioRateOpStatisticsMacTable = _RbtwsApStatRadioRateOpStatisticsMacTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 13)
)
if mibBuilder.loadTexts:
    rbtwsApStatRadioRateOpStatisticsMacTable.setStatus("current")
_RbtwsApStatRadioRateOpStatisticsMacEntry_Object = MibTableRow
rbtwsApStatRadioRateOpStatisticsMacEntry = _RbtwsApStatRadioRateOpStatisticsMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 13, 1)
)
rbtwsApStatRadioRateOpStatisticsMacEntry.setIndexNames(
    (0, "RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioRateOpStatsMacBaseMac"),
    (0, "RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioRateOpStatsMacRate"),
)
if mibBuilder.loadTexts:
    rbtwsApStatRadioRateOpStatisticsMacEntry.setStatus("current")
_RbtwsApStatRadioRateOpStatsMacBaseMac_Type = MacAddress
_RbtwsApStatRadioRateOpStatsMacBaseMac_Object = MibTableColumn
rbtwsApStatRadioRateOpStatsMacBaseMac = _RbtwsApStatRadioRateOpStatsMacBaseMac_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 13, 1, 1),
    _RbtwsApStatRadioRateOpStatsMacBaseMac_Type()
)
rbtwsApStatRadioRateOpStatsMacBaseMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbtwsApStatRadioRateOpStatsMacBaseMac.setStatus("current")
_RbtwsApStatRadioRateOpStatsMacRate_Type = RbtwsRadioRate
_RbtwsApStatRadioRateOpStatsMacRate_Object = MibTableColumn
rbtwsApStatRadioRateOpStatsMacRate = _RbtwsApStatRadioRateOpStatsMacRate_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 13, 1, 2),
    _RbtwsApStatRadioRateOpStatsMacRate_Type()
)
rbtwsApStatRadioRateOpStatsMacRate.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbtwsApStatRadioRateOpStatsMacRate.setStatus("current")
_RbtwsApStatRadioRateOpStatsMacTxUniPkt_Type = Counter64
_RbtwsApStatRadioRateOpStatsMacTxUniPkt_Object = MibTableColumn
rbtwsApStatRadioRateOpStatsMacTxUniPkt = _RbtwsApStatRadioRateOpStatsMacTxUniPkt_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 13, 1, 3),
    _RbtwsApStatRadioRateOpStatsMacTxUniPkt_Type()
)
rbtwsApStatRadioRateOpStatsMacTxUniPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioRateOpStatsMacTxUniPkt.setStatus("current")
_RbtwsApStatRadioRateOpStatsMacTxUniOctet_Type = Counter64
_RbtwsApStatRadioRateOpStatsMacTxUniOctet_Object = MibTableColumn
rbtwsApStatRadioRateOpStatsMacTxUniOctet = _RbtwsApStatRadioRateOpStatsMacTxUniOctet_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 13, 1, 4),
    _RbtwsApStatRadioRateOpStatsMacTxUniOctet_Type()
)
rbtwsApStatRadioRateOpStatsMacTxUniOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioRateOpStatsMacTxUniOctet.setStatus("current")
_RbtwsApStatRadioRateOpStatsMacTxMultiPkt_Type = Counter64
_RbtwsApStatRadioRateOpStatsMacTxMultiPkt_Object = MibTableColumn
rbtwsApStatRadioRateOpStatsMacTxMultiPkt = _RbtwsApStatRadioRateOpStatsMacTxMultiPkt_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 13, 1, 5),
    _RbtwsApStatRadioRateOpStatsMacTxMultiPkt_Type()
)
rbtwsApStatRadioRateOpStatsMacTxMultiPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioRateOpStatsMacTxMultiPkt.setStatus("current")
_RbtwsApStatRadioRateOpStatsMacTxMultiOctet_Type = Counter64
_RbtwsApStatRadioRateOpStatsMacTxMultiOctet_Object = MibTableColumn
rbtwsApStatRadioRateOpStatsMacTxMultiOctet = _RbtwsApStatRadioRateOpStatsMacTxMultiOctet_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 13, 1, 6),
    _RbtwsApStatRadioRateOpStatsMacTxMultiOctet_Type()
)
rbtwsApStatRadioRateOpStatsMacTxMultiOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioRateOpStatsMacTxMultiOctet.setStatus("current")
_RbtwsApStatRadioRateOpStatsMacRxPkt_Type = Counter64
_RbtwsApStatRadioRateOpStatsMacRxPkt_Object = MibTableColumn
rbtwsApStatRadioRateOpStatsMacRxPkt = _RbtwsApStatRadioRateOpStatsMacRxPkt_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 13, 1, 7),
    _RbtwsApStatRadioRateOpStatsMacRxPkt_Type()
)
rbtwsApStatRadioRateOpStatsMacRxPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioRateOpStatsMacRxPkt.setStatus("current")
_RbtwsApStatRadioRateOpStatsMacRxOctet_Type = Counter64
_RbtwsApStatRadioRateOpStatsMacRxOctet_Object = MibTableColumn
rbtwsApStatRadioRateOpStatsMacRxOctet = _RbtwsApStatRadioRateOpStatsMacRxOctet_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 13, 1, 8),
    _RbtwsApStatRadioRateOpStatsMacRxOctet_Type()
)
rbtwsApStatRadioRateOpStatsMacRxOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioRateOpStatsMacRxOctet.setStatus("current")
_RbtwsApStatRadioRateOpStatsMacUndcrptPkt_Type = Counter64
_RbtwsApStatRadioRateOpStatsMacUndcrptPkt_Object = MibTableColumn
rbtwsApStatRadioRateOpStatsMacUndcrptPkt = _RbtwsApStatRadioRateOpStatsMacUndcrptPkt_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 13, 1, 9),
    _RbtwsApStatRadioRateOpStatsMacUndcrptPkt_Type()
)
rbtwsApStatRadioRateOpStatsMacUndcrptPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioRateOpStatsMacUndcrptPkt.setStatus("current")
_RbtwsApStatRadioRateOpStatsMacUndcrptOctet_Type = Counter64
_RbtwsApStatRadioRateOpStatsMacUndcrptOctet_Object = MibTableColumn
rbtwsApStatRadioRateOpStatsMacUndcrptOctet = _RbtwsApStatRadioRateOpStatsMacUndcrptOctet_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 13, 1, 10),
    _RbtwsApStatRadioRateOpStatsMacUndcrptOctet_Type()
)
rbtwsApStatRadioRateOpStatsMacUndcrptOctet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioRateOpStatsMacUndcrptOctet.setStatus("current")
_RbtwsApStatRadioRateOpStatsMacPhyErr_Type = Counter64
_RbtwsApStatRadioRateOpStatsMacPhyErr_Object = MibTableColumn
rbtwsApStatRadioRateOpStatsMacPhyErr = _RbtwsApStatRadioRateOpStatsMacPhyErr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 1, 13, 1, 11),
    _RbtwsApStatRadioRateOpStatsMacPhyErr_Type()
)
rbtwsApStatRadioRateOpStatsMacPhyErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbtwsApStatRadioRateOpStatsMacPhyErr.setStatus("current")
_RbtwsApStatusConformance_ObjectIdentity = ObjectIdentity
rbtwsApStatusConformance = _RbtwsApStatusConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 2)
)
_RbtwsApStatusCompliances_ObjectIdentity = ObjectIdentity
rbtwsApStatusCompliances = _RbtwsApStatusCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 2, 1)
)
_RbtwsApStatusGroups_ObjectIdentity = ObjectIdentity
rbtwsApStatusGroups = _RbtwsApStatusGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 2, 2)
)

# Managed Objects groups

rbtwsApStatusCommonGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 2, 2, 1)
)
rbtwsApStatusCommonGroup.setObjects(
      *(("RBTWS-AP-STATUS-MIB", "rbtwsApStatNumAps"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusBaseMac"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusAttachType"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusPortOrDapNum"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusApState"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusModel"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusFingerprint"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusApName"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusVlan"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusIpAddress"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusUptimeSecs"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusCpuInfo"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusManufacturerId"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusRamBytes"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusHardwareRev"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusMacSerialNum"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusMacAttachType"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusMacPortOrDapNum"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusMacApState"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusMacModel"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusMacFingerprint"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusMacApName"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusMacVlan"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusMacIpAddress"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusMacUptimeSecs"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusMacCpuInfo"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusMacManufacturerId"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusMacRamBytes"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusMacHardwareRev"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioStatusBaseMac"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioStatusEnable"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioStatusRadioConfigState"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioStatusCurrentPowerLevel"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioStatusCurrentChannelNum"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioStatusMacApSerialNum"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioStatusMacRadioNum"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioStatusMacEnable"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioStatusMacRadioConfigState"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioStatusMacCurrentPowerLevel"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioStatusMacCurrentChannelNum"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioServBssid"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioServServiceProfileName"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioServMacApSerialNum"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioServMacRadioNum"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioServMacSsid"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioServMacServiceProfileName"))
)
if mibBuilder.loadTexts:
    rbtwsApStatusCommonGroup.setStatus("obsolete")

rbtwsApStatusScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 2, 2, 2)
)
rbtwsApStatusScalarsGroup.setObjects(
    ("RBTWS-AP-STATUS-MIB", "rbtwsApStatNumAps")
)
if mibBuilder.loadTexts:
    rbtwsApStatusScalarsGroup.setStatus("current")

rbtwsApStatusApStatusTablesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 2, 2, 3)
)
rbtwsApStatusApStatusTablesGroup.setObjects(
      *(("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusBaseMac"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusAttachType"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusPortOrDapNum"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusApState"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusModel"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusFingerprint"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusApName"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusVlan"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusIpAddress"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusUptimeSecs"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusCpuInfo"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusManufacturerId"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusRamBytes"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusHardwareRev"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusClientSessions"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusMacSerialNum"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusMacAttachType"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusMacPortOrDapNum"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusMacApState"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusMacModel"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusMacFingerprint"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusMacApName"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusMacVlan"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusMacIpAddress"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusMacUptimeSecs"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusMacCpuInfo"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusMacManufacturerId"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusMacRamBytes"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusMacHardwareRev"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusMacClientSessions"))
)
if mibBuilder.loadTexts:
    rbtwsApStatusApStatusTablesGroup.setStatus("obsolete")

rbtwsApStatusRadioStatusTablesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 2, 2, 4)
)
rbtwsApStatusRadioStatusTablesGroup.setObjects(
      *(("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioStatusBaseMac"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioStatusEnable"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioStatusRadioConfigState"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioStatusCurrentPowerLevel"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioStatusCurrentChannelNum"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioStatusMacApSerialNum"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioStatusMacRadioNum"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioStatusMacEnable"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioStatusMacRadioConfigState"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioStatusMacCurrentPowerLevel"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioStatusMacCurrentChannelNum"))
)
if mibBuilder.loadTexts:
    rbtwsApStatusRadioStatusTablesGroup.setStatus("obsolete")

rbtwsApStatusRadioServiceTablesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 2, 2, 5)
)
rbtwsApStatusRadioServiceTablesGroup.setObjects(
      *(("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioServBssid"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioServServiceProfileName"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioServMacApSerialNum"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioServMacRadioNum"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioServMacSsid"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioServMacServiceProfileName"))
)
if mibBuilder.loadTexts:
    rbtwsApStatusRadioServiceTablesGroup.setStatus("current")

rbtwsApStatusRadioServiceOpRateSetTablesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 2, 2, 6)
)
rbtwsApStatusRadioServiceOpRateSetTablesGroup.setObjects(
      *(("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioSORSetMandatory"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioSORSetDisabled"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioSORSetBeacon"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioSORSetMulticast"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioSORSetMacMandatory"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioSORSetMacDisabled"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioSORSetMacBeacon"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioSORSetMacMulticast"))
)
if mibBuilder.loadTexts:
    rbtwsApStatusRadioServiceOpRateSetTablesGroup.setStatus("current")

rbtwsApStatusRadioOpStatisticsTablesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 2, 2, 7)
)
rbtwsApStatusRadioOpStatisticsTablesGroup.setObjects(
      *(("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioOpStatsTxUniPkt"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioOpStatsTxUniOctet"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioOpStatsTxMultiPkt"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioOpStatsTxMultiOctet"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioOpStatsRxPkt"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioOpStatsRxOctet"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioOpStatsUndcrptPkt"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioOpStatsUndcrptOctet"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioOpStatsPhyErr"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioOpStatsResetCount"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioOpStatsAutoTuneChannelChangeCount"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioOpStatsTxRetriesCount"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioOpStatsUserSessions"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioOpStatsNoiseFloor"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioOpStatsMacTxUniPkt"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioOpStatsMacTxUniOctet"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioOpStatsMacTxMultiPkt"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioOpStatsMacTxMultiOctet"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioOpStatsMacRxPkt"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioOpStatsMacRxOctet"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioOpStatsMacUndcrptPkt"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioOpStatsMacUndcrptOctet"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioOpStatsMacPhyErr"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioOpStatsMacResetCount"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioOpStatsMacAutoTuneChannelChangeCount"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioOpStatsMacTxRetriesCount"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioOpStatsMacUserSessions"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioOpStatsMacNoiseFloor"))
)
if mibBuilder.loadTexts:
    rbtwsApStatusRadioOpStatisticsTablesGroup.setStatus("current")

rbtwsApStatusRadioOpStatisticsPerRateTablesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 2, 2, 8)
)
rbtwsApStatusRadioOpStatisticsPerRateTablesGroup.setObjects(
      *(("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioRateOpStatsTxUniPkt"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioRateOpStatsTxUniOctet"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioRateOpStatsTxMultiPkt"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioRateOpStatsTxMultiOctet"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioRateOpStatsRxPkt"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioRateOpStatsRxOctet"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioRateOpStatsUndcrptPkt"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioRateOpStatsUndcrptOctet"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioRateOpStatsPhyErr"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioRateOpStatsMacTxUniPkt"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioRateOpStatsMacTxUniOctet"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioRateOpStatsMacTxMultiPkt"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioRateOpStatsMacTxMultiOctet"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioRateOpStatsMacRxPkt"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioRateOpStatsMacRxOctet"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioRateOpStatsMacUndcrptPkt"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioRateOpStatsMacUndcrptOctet"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioRateOpStatsMacPhyErr"))
)
if mibBuilder.loadTexts:
    rbtwsApStatusRadioOpStatisticsPerRateTablesGroup.setStatus("current")

rbtwsApStatusApStatusVersionsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 2, 2, 9)
)
rbtwsApStatusApStatusVersionsGroup.setObjects(
      *(("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusSoftwareVer"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusBootVer"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusMacSoftwareVer"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusMacBootVer"))
)
if mibBuilder.loadTexts:
    rbtwsApStatusApStatusVersionsGroup.setStatus("current")

rbtwsApStatusApStatusTablesGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 2, 2, 10)
)
rbtwsApStatusApStatusTablesGroupRev2.setObjects(
      *(("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusBaseMac"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusAttachType"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusApState"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusModel"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusFingerprint"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusApName"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusVlan"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusIpAddress"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusUptimeSecs"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusCpuInfo"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusManufacturerId"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusRamBytes"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusHardwareRev"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusClientSessions"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusApNum"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusMacSerialNum"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusMacAttachType"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusMacApState"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusMacModel"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusMacFingerprint"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusMacApName"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusMacVlan"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusMacIpAddress"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusMacUptimeSecs"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusMacCpuInfo"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusMacManufacturerId"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusMacRamBytes"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusMacHardwareRev"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusMacClientSessions"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatApStatusMacApNum"))
)
if mibBuilder.loadTexts:
    rbtwsApStatusApStatusTablesGroupRev2.setStatus("current")

rbtwsApStatusRadioStatusMaxPowerPhyTypeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 2, 2, 11)
)
rbtwsApStatusRadioStatusMaxPowerPhyTypeGroup.setObjects(
      *(("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioStatusMaxPowerLevel"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioStatusRadioPhyType"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioStatusMacMaxPowerLevel"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioStatusMacRadioPhyType"))
)
if mibBuilder.loadTexts:
    rbtwsApStatusRadioStatusMaxPowerPhyTypeGroup.setStatus("current")

rbtwsApStatusRadioStatusTablesGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 2, 2, 12)
)
rbtwsApStatusRadioStatusTablesGroupRev2.setObjects(
      *(("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioStatusBaseMac"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioStatusRadioConfigState"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioStatusCurrentPowerLevel"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioStatusCurrentChannelNum"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioStatusClientSessions"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioStatusRadioMode"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioStatusMacApSerialNum"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioStatusMacRadioNum"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioStatusMacRadioConfigState"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioStatusMacCurrentPowerLevel"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioStatusMacCurrentChannelNum"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioStatusMacClientSessions"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioStatusMacRadioMode"))
)
if mibBuilder.loadTexts:
    rbtwsApStatusRadioStatusTablesGroupRev2.setStatus("current")

rbtwsApStatusRadioStatusWideMimoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 2, 2, 13)
)
rbtwsApStatusRadioStatusWideMimoGroup.setObjects(
      *(("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioStatusRadioChannelWidth"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioStatusRadioMimoState"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioStatusMacRadioChannelWidth"),
        ("RBTWS-AP-STATUS-MIB", "rbtwsApStatRadioStatusMacRadioMimoState"))
)
if mibBuilder.loadTexts:
    rbtwsApStatusRadioStatusWideMimoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rbtwsApStatusCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rbtwsApStatusCompliance.setStatus(
        "obsolete"
    )

rbtwsApStatusComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    rbtwsApStatusComplianceRev2.setStatus(
        "obsolete"
    )

rbtwsApStatusComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 2, 1, 3)
)
if mibBuilder.loadTexts:
    rbtwsApStatusComplianceRev3.setStatus(
        "obsolete"
    )

rbtwsApStatusComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 5, 1, 2, 1, 4)
)
if mibBuilder.loadTexts:
    rbtwsApStatusComplianceRev4.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBTWS-AP-STATUS-MIB",
    **{"RbtwsRadioOpRateSetSingleValue": RbtwsRadioOpRateSetSingleValue,
       "RbtwsRadioOpRateSetMandatory": RbtwsRadioOpRateSetMandatory,
       "RbtwsRadioOpRateSetDisabled": RbtwsRadioOpRateSetDisabled,
       "rbtwsApStatusMib": rbtwsApStatusMib,
       "rbtwsApStatusObjects": rbtwsApStatusObjects,
       "rbtwsApStatDataObjects": rbtwsApStatDataObjects,
       "rbtwsApStatNumAps": rbtwsApStatNumAps,
       "rbtwsApStatApStatusTable": rbtwsApStatApStatusTable,
       "rbtwsApStatApStatusEntry": rbtwsApStatApStatusEntry,
       "rbtwsApStatApStatusSerialNum": rbtwsApStatApStatusSerialNum,
       "rbtwsApStatApStatusBaseMac": rbtwsApStatApStatusBaseMac,
       "rbtwsApStatApStatusAttachType": rbtwsApStatApStatusAttachType,
       "rbtwsApStatApStatusPortOrDapNum": rbtwsApStatApStatusPortOrDapNum,
       "rbtwsApStatApStatusApState": rbtwsApStatApStatusApState,
       "rbtwsApStatApStatusModel": rbtwsApStatApStatusModel,
       "rbtwsApStatApStatusFingerprint": rbtwsApStatApStatusFingerprint,
       "rbtwsApStatApStatusApName": rbtwsApStatApStatusApName,
       "rbtwsApStatApStatusVlan": rbtwsApStatApStatusVlan,
       "rbtwsApStatApStatusIpAddress": rbtwsApStatApStatusIpAddress,
       "rbtwsApStatApStatusUptimeSecs": rbtwsApStatApStatusUptimeSecs,
       "rbtwsApStatApStatusCpuInfo": rbtwsApStatApStatusCpuInfo,
       "rbtwsApStatApStatusManufacturerId": rbtwsApStatApStatusManufacturerId,
       "rbtwsApStatApStatusRamBytes": rbtwsApStatApStatusRamBytes,
       "rbtwsApStatApStatusHardwareRev": rbtwsApStatApStatusHardwareRev,
       "rbtwsApStatApStatusClientSessions": rbtwsApStatApStatusClientSessions,
       "rbtwsApStatApStatusSoftwareVer": rbtwsApStatApStatusSoftwareVer,
       "rbtwsApStatApStatusBootVer": rbtwsApStatApStatusBootVer,
       "rbtwsApStatApStatusApNum": rbtwsApStatApStatusApNum,
       "rbtwsApStatApStatusMacTable": rbtwsApStatApStatusMacTable,
       "rbtwsApStatApStatusMacEntry": rbtwsApStatApStatusMacEntry,
       "rbtwsApStatApStatusMacBaseMac": rbtwsApStatApStatusMacBaseMac,
       "rbtwsApStatApStatusMacSerialNum": rbtwsApStatApStatusMacSerialNum,
       "rbtwsApStatApStatusMacAttachType": rbtwsApStatApStatusMacAttachType,
       "rbtwsApStatApStatusMacPortOrDapNum": rbtwsApStatApStatusMacPortOrDapNum,
       "rbtwsApStatApStatusMacApState": rbtwsApStatApStatusMacApState,
       "rbtwsApStatApStatusMacModel": rbtwsApStatApStatusMacModel,
       "rbtwsApStatApStatusMacFingerprint": rbtwsApStatApStatusMacFingerprint,
       "rbtwsApStatApStatusMacApName": rbtwsApStatApStatusMacApName,
       "rbtwsApStatApStatusMacVlan": rbtwsApStatApStatusMacVlan,
       "rbtwsApStatApStatusMacIpAddress": rbtwsApStatApStatusMacIpAddress,
       "rbtwsApStatApStatusMacUptimeSecs": rbtwsApStatApStatusMacUptimeSecs,
       "rbtwsApStatApStatusMacCpuInfo": rbtwsApStatApStatusMacCpuInfo,
       "rbtwsApStatApStatusMacManufacturerId": rbtwsApStatApStatusMacManufacturerId,
       "rbtwsApStatApStatusMacRamBytes": rbtwsApStatApStatusMacRamBytes,
       "rbtwsApStatApStatusMacHardwareRev": rbtwsApStatApStatusMacHardwareRev,
       "rbtwsApStatApStatusMacClientSessions": rbtwsApStatApStatusMacClientSessions,
       "rbtwsApStatApStatusMacSoftwareVer": rbtwsApStatApStatusMacSoftwareVer,
       "rbtwsApStatApStatusMacBootVer": rbtwsApStatApStatusMacBootVer,
       "rbtwsApStatApStatusMacApNum": rbtwsApStatApStatusMacApNum,
       "rbtwsApStatRadioStatusTable": rbtwsApStatRadioStatusTable,
       "rbtwsApStatRadioStatusEntry": rbtwsApStatRadioStatusEntry,
       "rbtwsApStatRadioStatusApSerialNum": rbtwsApStatRadioStatusApSerialNum,
       "rbtwsApStatRadioStatusRadioNum": rbtwsApStatRadioStatusRadioNum,
       "rbtwsApStatRadioStatusBaseMac": rbtwsApStatRadioStatusBaseMac,
       "rbtwsApStatRadioStatusEnable": rbtwsApStatRadioStatusEnable,
       "rbtwsApStatRadioStatusRadioConfigState": rbtwsApStatRadioStatusRadioConfigState,
       "rbtwsApStatRadioStatusCurrentPowerLevel": rbtwsApStatRadioStatusCurrentPowerLevel,
       "rbtwsApStatRadioStatusCurrentChannelNum": rbtwsApStatRadioStatusCurrentChannelNum,
       "rbtwsApStatRadioStatusClientSessions": rbtwsApStatRadioStatusClientSessions,
       "rbtwsApStatRadioStatusMaxPowerLevel": rbtwsApStatRadioStatusMaxPowerLevel,
       "rbtwsApStatRadioStatusRadioPhyType": rbtwsApStatRadioStatusRadioPhyType,
       "rbtwsApStatRadioStatusRadioMode": rbtwsApStatRadioStatusRadioMode,
       "rbtwsApStatRadioStatusRadioChannelWidth": rbtwsApStatRadioStatusRadioChannelWidth,
       "rbtwsApStatRadioStatusRadioMimoState": rbtwsApStatRadioStatusRadioMimoState,
       "rbtwsApStatRadioStatusMacTable": rbtwsApStatRadioStatusMacTable,
       "rbtwsApStatRadioStatusMacEntry": rbtwsApStatRadioStatusMacEntry,
       "rbtwsApStatRadioStatusMacBaseMac": rbtwsApStatRadioStatusMacBaseMac,
       "rbtwsApStatRadioStatusMacApSerialNum": rbtwsApStatRadioStatusMacApSerialNum,
       "rbtwsApStatRadioStatusMacRadioNum": rbtwsApStatRadioStatusMacRadioNum,
       "rbtwsApStatRadioStatusMacEnable": rbtwsApStatRadioStatusMacEnable,
       "rbtwsApStatRadioStatusMacRadioConfigState": rbtwsApStatRadioStatusMacRadioConfigState,
       "rbtwsApStatRadioStatusMacCurrentPowerLevel": rbtwsApStatRadioStatusMacCurrentPowerLevel,
       "rbtwsApStatRadioStatusMacCurrentChannelNum": rbtwsApStatRadioStatusMacCurrentChannelNum,
       "rbtwsApStatRadioStatusMacClientSessions": rbtwsApStatRadioStatusMacClientSessions,
       "rbtwsApStatRadioStatusMacMaxPowerLevel": rbtwsApStatRadioStatusMacMaxPowerLevel,
       "rbtwsApStatRadioStatusMacRadioPhyType": rbtwsApStatRadioStatusMacRadioPhyType,
       "rbtwsApStatRadioStatusMacRadioMode": rbtwsApStatRadioStatusMacRadioMode,
       "rbtwsApStatRadioStatusMacRadioChannelWidth": rbtwsApStatRadioStatusMacRadioChannelWidth,
       "rbtwsApStatRadioStatusMacRadioMimoState": rbtwsApStatRadioStatusMacRadioMimoState,
       "rbtwsApStatRadioServiceTable": rbtwsApStatRadioServiceTable,
       "rbtwsApStatRadioServiceEntry": rbtwsApStatRadioServiceEntry,
       "rbtwsApStatRadioServApSerialNum": rbtwsApStatRadioServApSerialNum,
       "rbtwsApStatRadioServRadioNum": rbtwsApStatRadioServRadioNum,
       "rbtwsApStatRadioServSsid": rbtwsApStatRadioServSsid,
       "rbtwsApStatRadioServBssid": rbtwsApStatRadioServBssid,
       "rbtwsApStatRadioServServiceProfileName": rbtwsApStatRadioServServiceProfileName,
       "rbtwsApStatRadioServiceMacTable": rbtwsApStatRadioServiceMacTable,
       "rbtwsApStatRadioServiceMacEntry": rbtwsApStatRadioServiceMacEntry,
       "rbtwsApStatRadioServMacBssid": rbtwsApStatRadioServMacBssid,
       "rbtwsApStatRadioServMacApSerialNum": rbtwsApStatRadioServMacApSerialNum,
       "rbtwsApStatRadioServMacRadioNum": rbtwsApStatRadioServMacRadioNum,
       "rbtwsApStatRadioServMacSsid": rbtwsApStatRadioServMacSsid,
       "rbtwsApStatRadioServMacServiceProfileName": rbtwsApStatRadioServMacServiceProfileName,
       "rbtwsApStatRadioServiceOpRateSetTable": rbtwsApStatRadioServiceOpRateSetTable,
       "rbtwsApStatRadioServiceOpRateSetEntry": rbtwsApStatRadioServiceOpRateSetEntry,
       "rbtwsApStatRadioSORSetApSerialNum": rbtwsApStatRadioSORSetApSerialNum,
       "rbtwsApStatRadioSORSetRadioNum": rbtwsApStatRadioSORSetRadioNum,
       "rbtwsApStatRadioSORSetSsid": rbtwsApStatRadioSORSetSsid,
       "rbtwsApStatRadioSORSetMandatory": rbtwsApStatRadioSORSetMandatory,
       "rbtwsApStatRadioSORSetDisabled": rbtwsApStatRadioSORSetDisabled,
       "rbtwsApStatRadioSORSetBeacon": rbtwsApStatRadioSORSetBeacon,
       "rbtwsApStatRadioSORSetMulticast": rbtwsApStatRadioSORSetMulticast,
       "rbtwsApStatRadioServiceOpRateSetMacTable": rbtwsApStatRadioServiceOpRateSetMacTable,
       "rbtwsApStatRadioServiceOpRateSetMacEntry": rbtwsApStatRadioServiceOpRateSetMacEntry,
       "rbtwsApStatRadioSORSetMacBssid": rbtwsApStatRadioSORSetMacBssid,
       "rbtwsApStatRadioSORSetMacMandatory": rbtwsApStatRadioSORSetMacMandatory,
       "rbtwsApStatRadioSORSetMacDisabled": rbtwsApStatRadioSORSetMacDisabled,
       "rbtwsApStatRadioSORSetMacBeacon": rbtwsApStatRadioSORSetMacBeacon,
       "rbtwsApStatRadioSORSetMacMulticast": rbtwsApStatRadioSORSetMacMulticast,
       "rbtwsApStatRadioOpStatisticsTable": rbtwsApStatRadioOpStatisticsTable,
       "rbtwsApStatRadioOpStatisticsEntry": rbtwsApStatRadioOpStatisticsEntry,
       "rbtwsApStatRadioOpStatsApSerialNum": rbtwsApStatRadioOpStatsApSerialNum,
       "rbtwsApStatRadioOpStatsRadioNum": rbtwsApStatRadioOpStatsRadioNum,
       "rbtwsApStatRadioOpStatsTxUniPkt": rbtwsApStatRadioOpStatsTxUniPkt,
       "rbtwsApStatRadioOpStatsTxUniOctet": rbtwsApStatRadioOpStatsTxUniOctet,
       "rbtwsApStatRadioOpStatsTxMultiPkt": rbtwsApStatRadioOpStatsTxMultiPkt,
       "rbtwsApStatRadioOpStatsTxMultiOctet": rbtwsApStatRadioOpStatsTxMultiOctet,
       "rbtwsApStatRadioOpStatsRxPkt": rbtwsApStatRadioOpStatsRxPkt,
       "rbtwsApStatRadioOpStatsRxOctet": rbtwsApStatRadioOpStatsRxOctet,
       "rbtwsApStatRadioOpStatsUndcrptPkt": rbtwsApStatRadioOpStatsUndcrptPkt,
       "rbtwsApStatRadioOpStatsUndcrptOctet": rbtwsApStatRadioOpStatsUndcrptOctet,
       "rbtwsApStatRadioOpStatsPhyErr": rbtwsApStatRadioOpStatsPhyErr,
       "rbtwsApStatRadioOpStatsResetCount": rbtwsApStatRadioOpStatsResetCount,
       "rbtwsApStatRadioOpStatsAutoTuneChannelChangeCount": rbtwsApStatRadioOpStatsAutoTuneChannelChangeCount,
       "rbtwsApStatRadioOpStatsTxRetriesCount": rbtwsApStatRadioOpStatsTxRetriesCount,
       "rbtwsApStatRadioOpStatsUserSessions": rbtwsApStatRadioOpStatsUserSessions,
       "rbtwsApStatRadioOpStatsNoiseFloor": rbtwsApStatRadioOpStatsNoiseFloor,
       "rbtwsApStatRadioOpStatisticsMacTable": rbtwsApStatRadioOpStatisticsMacTable,
       "rbtwsApStatRadioOpStatisticsMacEntry": rbtwsApStatRadioOpStatisticsMacEntry,
       "rbtwsApStatRadioOpStatsMacBaseMac": rbtwsApStatRadioOpStatsMacBaseMac,
       "rbtwsApStatRadioOpStatsMacTxUniPkt": rbtwsApStatRadioOpStatsMacTxUniPkt,
       "rbtwsApStatRadioOpStatsMacTxUniOctet": rbtwsApStatRadioOpStatsMacTxUniOctet,
       "rbtwsApStatRadioOpStatsMacTxMultiPkt": rbtwsApStatRadioOpStatsMacTxMultiPkt,
       "rbtwsApStatRadioOpStatsMacTxMultiOctet": rbtwsApStatRadioOpStatsMacTxMultiOctet,
       "rbtwsApStatRadioOpStatsMacRxPkt": rbtwsApStatRadioOpStatsMacRxPkt,
       "rbtwsApStatRadioOpStatsMacRxOctet": rbtwsApStatRadioOpStatsMacRxOctet,
       "rbtwsApStatRadioOpStatsMacUndcrptPkt": rbtwsApStatRadioOpStatsMacUndcrptPkt,
       "rbtwsApStatRadioOpStatsMacUndcrptOctet": rbtwsApStatRadioOpStatsMacUndcrptOctet,
       "rbtwsApStatRadioOpStatsMacPhyErr": rbtwsApStatRadioOpStatsMacPhyErr,
       "rbtwsApStatRadioOpStatsMacResetCount": rbtwsApStatRadioOpStatsMacResetCount,
       "rbtwsApStatRadioOpStatsMacAutoTuneChannelChangeCount": rbtwsApStatRadioOpStatsMacAutoTuneChannelChangeCount,
       "rbtwsApStatRadioOpStatsMacTxRetriesCount": rbtwsApStatRadioOpStatsMacTxRetriesCount,
       "rbtwsApStatRadioOpStatsMacUserSessions": rbtwsApStatRadioOpStatsMacUserSessions,
       "rbtwsApStatRadioOpStatsMacNoiseFloor": rbtwsApStatRadioOpStatsMacNoiseFloor,
       "rbtwsApStatRadioRateOpStatisticsTable": rbtwsApStatRadioRateOpStatisticsTable,
       "rbtwsApStatRadioRateOpStatisticsEntry": rbtwsApStatRadioRateOpStatisticsEntry,
       "rbtwsApStatRadioRateOpStatsApSerialNum": rbtwsApStatRadioRateOpStatsApSerialNum,
       "rbtwsApStatRadioRateOpStatsRadioNum": rbtwsApStatRadioRateOpStatsRadioNum,
       "rbtwsApStatRadioRateOpStatsRate": rbtwsApStatRadioRateOpStatsRate,
       "rbtwsApStatRadioRateOpStatsTxUniPkt": rbtwsApStatRadioRateOpStatsTxUniPkt,
       "rbtwsApStatRadioRateOpStatsTxUniOctet": rbtwsApStatRadioRateOpStatsTxUniOctet,
       "rbtwsApStatRadioRateOpStatsTxMultiPkt": rbtwsApStatRadioRateOpStatsTxMultiPkt,
       "rbtwsApStatRadioRateOpStatsTxMultiOctet": rbtwsApStatRadioRateOpStatsTxMultiOctet,
       "rbtwsApStatRadioRateOpStatsRxPkt": rbtwsApStatRadioRateOpStatsRxPkt,
       "rbtwsApStatRadioRateOpStatsRxOctet": rbtwsApStatRadioRateOpStatsRxOctet,
       "rbtwsApStatRadioRateOpStatsUndcrptPkt": rbtwsApStatRadioRateOpStatsUndcrptPkt,
       "rbtwsApStatRadioRateOpStatsUndcrptOctet": rbtwsApStatRadioRateOpStatsUndcrptOctet,
       "rbtwsApStatRadioRateOpStatsPhyErr": rbtwsApStatRadioRateOpStatsPhyErr,
       "rbtwsApStatRadioRateOpStatisticsMacTable": rbtwsApStatRadioRateOpStatisticsMacTable,
       "rbtwsApStatRadioRateOpStatisticsMacEntry": rbtwsApStatRadioRateOpStatisticsMacEntry,
       "rbtwsApStatRadioRateOpStatsMacBaseMac": rbtwsApStatRadioRateOpStatsMacBaseMac,
       "rbtwsApStatRadioRateOpStatsMacRate": rbtwsApStatRadioRateOpStatsMacRate,
       "rbtwsApStatRadioRateOpStatsMacTxUniPkt": rbtwsApStatRadioRateOpStatsMacTxUniPkt,
       "rbtwsApStatRadioRateOpStatsMacTxUniOctet": rbtwsApStatRadioRateOpStatsMacTxUniOctet,
       "rbtwsApStatRadioRateOpStatsMacTxMultiPkt": rbtwsApStatRadioRateOpStatsMacTxMultiPkt,
       "rbtwsApStatRadioRateOpStatsMacTxMultiOctet": rbtwsApStatRadioRateOpStatsMacTxMultiOctet,
       "rbtwsApStatRadioRateOpStatsMacRxPkt": rbtwsApStatRadioRateOpStatsMacRxPkt,
       "rbtwsApStatRadioRateOpStatsMacRxOctet": rbtwsApStatRadioRateOpStatsMacRxOctet,
       "rbtwsApStatRadioRateOpStatsMacUndcrptPkt": rbtwsApStatRadioRateOpStatsMacUndcrptPkt,
       "rbtwsApStatRadioRateOpStatsMacUndcrptOctet": rbtwsApStatRadioRateOpStatsMacUndcrptOctet,
       "rbtwsApStatRadioRateOpStatsMacPhyErr": rbtwsApStatRadioRateOpStatsMacPhyErr,
       "rbtwsApStatusConformance": rbtwsApStatusConformance,
       "rbtwsApStatusCompliances": rbtwsApStatusCompliances,
       "rbtwsApStatusCompliance": rbtwsApStatusCompliance,
       "rbtwsApStatusComplianceRev2": rbtwsApStatusComplianceRev2,
       "rbtwsApStatusComplianceRev3": rbtwsApStatusComplianceRev3,
       "rbtwsApStatusComplianceRev4": rbtwsApStatusComplianceRev4,
       "rbtwsApStatusGroups": rbtwsApStatusGroups,
       "rbtwsApStatusCommonGroup": rbtwsApStatusCommonGroup,
       "rbtwsApStatusScalarsGroup": rbtwsApStatusScalarsGroup,
       "rbtwsApStatusApStatusTablesGroup": rbtwsApStatusApStatusTablesGroup,
       "rbtwsApStatusRadioStatusTablesGroup": rbtwsApStatusRadioStatusTablesGroup,
       "rbtwsApStatusRadioServiceTablesGroup": rbtwsApStatusRadioServiceTablesGroup,
       "rbtwsApStatusRadioServiceOpRateSetTablesGroup": rbtwsApStatusRadioServiceOpRateSetTablesGroup,
       "rbtwsApStatusRadioOpStatisticsTablesGroup": rbtwsApStatusRadioOpStatisticsTablesGroup,
       "rbtwsApStatusRadioOpStatisticsPerRateTablesGroup": rbtwsApStatusRadioOpStatisticsPerRateTablesGroup,
       "rbtwsApStatusApStatusVersionsGroup": rbtwsApStatusApStatusVersionsGroup,
       "rbtwsApStatusApStatusTablesGroupRev2": rbtwsApStatusApStatusTablesGroupRev2,
       "rbtwsApStatusRadioStatusMaxPowerPhyTypeGroup": rbtwsApStatusRadioStatusMaxPowerPhyTypeGroup,
       "rbtwsApStatusRadioStatusTablesGroupRev2": rbtwsApStatusRadioStatusTablesGroupRev2,
       "rbtwsApStatusRadioStatusWideMimoGroup": rbtwsApStatusRadioStatusWideMimoGroup}
)
